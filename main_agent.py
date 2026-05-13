import os
import sys
import re
from typing import Optional

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path: sys.path.append(BASE_DIR)

from langgraph.graph import StateGraph, START, END
from langgraph.types import Command
from langchain_openai import ChatOpenAI

from agent_config import Config
from state import MathAgentState
from tools.vector_db import retrieve_from_chroma, find_similar_notes
from tools.obsidian_io import save_markdown_to_obsidian, sanitize_filename      

llm = ChatOpenAI(
    model=Config.MODEL_NAME, 
    api_key=Config.DEEPSEEK_API_KEY, 
    base_url=Config.DEEPSEEK_BASE_URL,
    max_tokens=2048,
    temperature=0.1
)

def check_latex_closures(text: str) -> Optional[str]:
    if text.count("$$") % 2 != 0: return "发现未闭合的独立公式区块 ($$ 不成对)。"
    if text.replace("$$", "").count("$") % 2 != 0: return "发现未闭合的行内公式 ($ 不成对)。"
    return None

def clean_output_for_obsidian(text: str) -> str:
    """清理 LLM 输出中的 prompt 泄漏，确保纯 Obsidian Markdown"""
    # 1. 移除代码块包裹标记
    text = re.sub(r'```(?:obsidian|markdown|md)?\s*', '', text)

    lines = text.split('\n')
    # 2. 找到第一个 Markdown 标题
    first_heading_idx = -1
    for i, line in enumerate(lines):
        if re.match(r'^#{1,2}\s+', line.strip()):
            first_heading_idx = i
            break

    # 如果标题前有内容且包含泄漏特征，截断
    if first_heading_idx > 0:
        pre = '\n'.join(lines[:first_heading_idx])
        if re.search(r'教授|Obsidian|好的|请注意|Here is|Based on', pre):
            lines = lines[first_heading_idx:]

    # 3. 逐行清理残留泄漏
    leak_prefixes = ['好的', '作为', '教授', '导师', 'Here is', 'Based on', 'I will']
    clean = []
    for line in lines:
        stripped = line.strip()
        if not stripped:
            clean.append(line)
            continue
        if any(stripped.startswith(p) for p in leak_prefixes):
            continue
        line = line.replace('Obsidian 格式笔记', '笔记')
        line = line.replace('Obsidian格式笔记', '笔记')
        clean.append(line)

    text = '\n'.join(clean)
    # 4. 清理多余空行
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()

# === 2. 节点函数 ===

def retrieve_node(state: MathAgentState):
    print(f"\n🔍 [检索] 正在寻找【{state['chapter']}】下的: '{state['query']}' ...")
    search_query = f"{state['chapter']} {state['query']}"
    # 优先从同一文档中检索，避免跨科目污染
    contexts = retrieve_from_chroma(search_query, k=3, source_filter=state['document_name'])
    return Command(update={"retrieved_contexts": contexts}, goto="generate_node")

def generate_node(state: MathAgentState):
    iteration = state.get('iteration', 0)
    print(f"✍️ [生成] 正在撰写笔记 (纠错次数: {iteration})...")

    all_available_topics = list(set(state['current_doc_topics'] + state['global_vault_topics']))
    valid_links = ", ".join([f"[[{sanitize_filename(t)}]]" for t in all_available_topics if t != state['query']])

    if state['item_type'] == "example":
        type_instruction = "这是一道【例题】。请给出：1. 题目描述；2. 详细推导。"
    else:
        type_instruction = "这是一个【理论知识点】。请给出严谨的定义、公式和推导。"

    # 用 system prompt（messages 第一条）约束模型行为，比在 user prompt 里"要求"有效得多
    system_msg = (
        "你是一位数学笔记生成助手。输出规则：\n"
        "1. 直接输出纯 Markdown 正文，禁止任何角色扮演、开场白、任务描述、元文本。\n"
        "2. 禁止使用 ```obsidian、```markdown 或任何代码块包裹内容。\n"
        "3. 禁止出现'作为教授''Obsidian 格式''好的''Here is'等 prompt 泄漏。\n"
        "4. 使用严格 LaTeX：行内公式用 $...$，独立公式用 $$...$$。\n"
        "5. 如果检索到的上下文与当前知识点明显属于不同学科，请忽略并基于自己的知识生成。\n"
        "6. 使用 [[双链]] 时，只对同一学科内自然出现的相关知识点进行链接，不要强行创造联系。"
    )

    user_prompt = f"""
生成关于【{state['query']}】的笔记。

{type_instruction}

【可用双链词汇】（只对自然出现且相关的概念使用 [[ ]] ）：
{valid_links}

【参考上下文】: {state['retrieved_contexts']}
{f"【修改建议】: {state['feedback']}" if state.get('feedback') else ""}
"""
    response = llm.invoke([
        {"role": "system", "content": system_msg},
        {"role": "user", "content": user_prompt}
    ])
    cleaned = clean_output_for_obsidian(response.content)
    return Command(update={"draft_note": cleaned}, goto="evaluate_node")

def evaluate_node(state: MathAgentState):
    iteration = state.get("iteration", 0)
    if iteration >= 2: return Command(goto="save_node")
    
    latex_error = check_latex_closures(state['draft_note'])
    if latex_error:
        return Command(update={"feedback": latex_error, "iteration": iteration + 1}, goto="generate_node")
    
    eval_prompt = f"检查笔记逻辑和推导是否准确。原文: {state['retrieved_contexts']} \n笔记：{state['draft_note']} \n完美回复 PASS，否则指出错误。"
    eval_res = llm.invoke(eval_prompt).content.strip()
    
    if "PASS" in eval_res.upper():
        return Command(goto="save_node")
    else:
        print(f"❌ [审计] 逻辑不通过: {eval_res}")
        return Command(update={"feedback": eval_res, "iteration": iteration + 1}, goto="generate_node")

def save_node(state: MathAgentState):
    print("💾 [保存] 正在落盘 Obsidian...")
    safe_title = sanitize_filename(state['query'])
    safe_doc = sanitize_filename(state['document_name'])

    # chapter 存完整层级路径（如 "Part I/Chapter 1/Section 1"），目录按 / 拆分创建
    chapter_full_path = state['chapter']
    # YAML frontmatter 只取最末级做 [[链接]]
    chapter_parts = [p.strip() for p in chapter_full_path.split("/") if p.strip()]
    chapter_for_yaml = sanitize_filename(chapter_parts[-1]) if chapter_parts else "未分类"

    yaml_header = (
        f"---\n"
        f"tags:\n  - {state['item_type']}\n"
        f"document: \"[[{safe_doc}]]\"\n"
        f"chapter: \"[[{chapter_for_yaml}]]\"\n"
        f"---\n\n"
    )
    final_content = yaml_header + f"# {state['query']}\n\n{state['draft_note']}"

    # 语义相关笔记 — 全库检索最相似的 Top-3
    related = find_similar_notes(state['draft_note'], exclude_title=state['query'], top_k=3)
    if related:
        final_content += "\n\n## 相关笔记\n"
        for title in related:
            final_content += f"- [[{title}]]\n"
        print(f"🔗 发现 {len(related)} 个语义相关笔记: {related}")

    result_msg = save_markdown_to_obsidian(
        content=final_content,
        filename=safe_title,
        document_name=safe_doc,
        chapter=chapter_full_path
    )
    print(result_msg)
    return Command(goto=END)

# === 3. 组装与接口 ===
workflow = StateGraph(MathAgentState)
workflow.add_node("retrieve_node", retrieve_node)
workflow.add_node("generate_node", generate_node)
workflow.add_node("evaluate_node", evaluate_node)
workflow.add_node("save_node", save_node)
workflow.add_edge(START, "retrieve_node")
app = workflow.compile()

def run_autonomous_agent(query: str, item_type: str, chapter: str, document_name: str, 
                         current_topics: list[str], global_topics: list[str]):
    print(f"\n🚀 流水线启动 -> 【{document_name}】::【{chapter}】::【{query}】")
    app.invoke({
        "query": query, 
        "item_type": item_type, 
        "chapter": chapter, 
        "document_name": document_name,
        "current_doc_topics": current_topics,
        "global_vault_topics": global_topics,
        "iteration": 0
    })