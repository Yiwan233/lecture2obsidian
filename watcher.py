import sys
import os
import time
import json
import re
import argparse

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
from concurrent.futures import ThreadPoolExecutor, as_completed
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from langchain_openai import ChatOpenAI
from agent_config import Config
from tools.pdf_parser import parse_pdf_to_md
from tools.vector_db import ingest_document_to_chroma
from tools.obsidian_io import save_markdown_to_obsidian, sanitize_filename, get_all_vault_note_titles
from main_agent import run_autonomous_agent

DATA_DIR = os.path.join(Config.BASE_DIR, "data")

llm_extractor = ChatOpenAI(
    model=Config.MODEL_NAME,
    api_key=Config.DEEPSEEK_API_KEY,
    base_url=Config.DEEPSEEK_BASE_URL,
    temperature=0.1,
    max_tokens=4096,
    timeout=180,
    max_retries=2,
)
def clean_text_for_extraction(content: str, filename: str) -> str:
    """提取核心正文，过滤掉 TeX 的导言区和无用注释，最大化利用 Token"""
    if filename.lower().endswith('.tex'):
        # 1. 尝试只提取 \begin{document} 到 \end{document} 之间的真正内容
        match = re.search(r'\\begin\{document\}(.*?)\\end\{document\}', content, re.DOTALL)
        if match:
            content = match.group(1)
        
        # 2. 删除以 % 开头的整行注释（这在 TeX 中非常占篇幅）
        content = re.sub(r'(?m)^\s*%.*$', '', content)
    
    # 将阅读视野扩大到 60,000 字符（DeepSeek 的窗口足够大，能看完几十页书的纯文本内容）
    return content[:60000]
def _normalize_structure(raw: dict) -> dict:
    """向后兼容：将旧版 chapters 格式统一为新版 sections 递归格式"""
    if "sections" in raw:
        return raw
    if "chapters" in raw:
        sections = []
        for ch in raw["chapters"]:
            sections.append({
                "name": ch.get("chapter_name", "未命名章节"),
                "children": ch.get("items", [])
            })
        raw["sections"] = sections
        del raw["chapters"]
    return raw


def _flatten_sections(sections, parent_path=""):
    """递归展平多级结构 → [(层级路径, 条目dict), ...]"""
    items = []
    for sec in sections:
        name = sec.get("name", "未命名")
        current_path = f"{parent_path}/{name}" if parent_path else name
        if "children" in sec:
            items.extend(_flatten_sections(sec["children"], current_path))
        else:
            items.append((parent_path, sec))
    return items


def _collect_leaf_names(sections):
    """递归收集所有叶子条目名称"""
    names = []
    for sec in sections:
        if "children" in sec:
            names.extend(_collect_leaf_names(sec["children"]))
        else:
            names.append(sec.get("name", ""))
    return names


def extract_hierarchical_structure(content: str, filename: str) -> dict:
    """提取多级树状结构（支持任意深度：部 → 章 → 节 → 概念/例题）"""
    preview_text = clean_text_for_extraction(content, filename)
    print(f"\n🧠 正在进行宏观知识图谱分析...")
    print(f"   📄 文档: {filename}  |  📏 送入分析: {len(preview_text)} 字符  |  ⏳ 等待 DeepSeek 响应（最长 3 分钟）...")

    prompt = f"""
请阅读以下学术讲义节选，提取出一份结构化的目录。要求：

1. 识别文档的完整层级结构——可能是 2 级、3 级甚至 4 级（例如：部→章→节→小节）。
2. 每个层级标题作为 section 节点，叶子节点是【概念知识点 (concept)】或【例题 (example)】。
3. section 节点和叶子节点可以共存于同一个 children 列表中（有时一个章下面既有概念也有节）。
4. 严格输出合法的 JSON 格式。

JSON 格式说明：
- 每个节点必须有 "name" 字段
- 如果是层级标题（可继续展开），包含 "children" 列表
- 如果是叶子知识点，包含 "type" 字段，取值为 "concept" 或 "example"
- 不要使用旧的 "chapters" / "chapter_name" / "items" 格式

JSON 格式示例：
{{
  "document_name": "随机微积分讲义",
  "sections": [
    {{
      "name": "第一部分：基础理论",
      "children": [
        {{
          "name": "第一章：布朗运动",
          "children": [
            {{"name": "布朗运动的定义", "type": "concept"}},
            {{"name": "例1：计算增量的期望", "type": "example"}},
            {{
              "name": "第一节：增量性质",
              "children": [
                {{"name": "增量的独立性", "type": "concept"}}
              ]
            }}
          ]
        }}
      ]
    }}
  ]
}}

文本节选：
{preview_text}
"""
    try:
        response = llm_extractor.invoke(prompt).content.strip()
        if "```json" in response: response = response.split("```json")[1].split("```")[0]
        elif "```" in response: response = response.split("```")[1].split("```")[0]

        structure = json.loads(response.strip())
        structure = _normalize_structure(structure)
        return structure
    except Exception as e:
        print(f"⚠️ 图谱提取失败: {e}。退回基础模式。")
        return {
            "document_name": "默认文档",
            "sections": [{"name": "未分类", "children": [{"name": "全文核心总结", "type": "concept"}]}]
        }

# watcher.py 中的函数定义部分

def _render_sections(sections, depth=2):
    """递归渲染多级目录 → Markdown 字符串"""
    out = ""
    heading_prefix = "#" * min(depth, 6)  # Markdown 最多 6 级标题
    for sec in sections:
        name = sec.get("name", "未命名")
        if "children" in sec:
            out += f"\n{heading_prefix} 📑 {name}\n"
            out += _render_sections(sec["children"], depth + 1)
        else:
            icon = "💡" if sec.get("type") == "concept" else "📝"
            safe_name = sanitize_filename(name)
            out += f"- {icon} [[{safe_name}]]\n"
    return out


def create_global_index(structure: dict, raw_filename: str):
    """
    根据提取的树状结构，生成 Obsidian 全局 MOC 索引页。
    支持任意深度的层级（部→章→节→...），用 # / ## / ### / ... 对应。
    """
    doc_name = sanitize_filename(structure.get("document_name", os.path.splitext(raw_filename)[0]))
    sections = structure.get("sections", [])

    content = f"# 📚 {doc_name} - 知识索引\n\n"
    content += f"这是文档 **{doc_name}** 的全局 Map of Content (MOC)。\n"
    content += _render_sections(sections, depth=2)

    save_markdown_to_obsidian(
        content=content,
        filename=f"_00_Index_{doc_name}",
        document_name=doc_name,
        chapter=""
    )
    print(f"🌐 全局索引树已生成：_00_Index_{doc_name}.md")


def process_file(filepath: str, concurrency: int = 4):
    """处理单个 .md/.tex/.pdf 文件的核心逻辑（PDF 自动转 MD → 结构提取 → ChromaDB → MOC → 并发生成笔记）"""
    filename = os.path.basename(filepath)
    ext = os.path.splitext(filename)[1].lower()

    # PDF 先转换为 Markdown，然后继续处理生成的 .md
    if ext == ".pdf":
        print(f"\n[Processor] 📥 发现 PDF，调用 LlamaParse 转换: {filename}")
        if not parse_pdf_to_md(filepath):
            print("❌ PDF 解析失败，流程终止。")
            return
        filepath = filepath.rsplit(".pdf", 1)[0] + ".md"
        if not os.path.exists(filepath):
            print("❌ 转换后的 .md 文件未生成。")
            return
        filename = os.path.basename(filepath)
        print(f"✅ PDF 已转换为 Markdown: {filename}")

    print(f"\n[Processor] 📥 开始处理 {ext.upper()} 文档: {filename}")

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. 扫描全库
    print("🧠 正在同步全库知识索引...")
    global_vault_topics = get_all_vault_note_titles()
    print(f"📊 当前全库已存储 {len(global_vault_topics)} 个知识点。")

    # 2. 提取文档结构
    structure = extract_hierarchical_structure(content, filename)
    doc_name = sanitize_filename(structure.get("document_name", os.path.splitext(filename)[0]))

    # 3. 收集当前文档所有知识点（递归展平多级结构）
    sections = structure.get("sections", [])
    current_doc_topics = _collect_leaf_names(sections)
    flat_items = _flatten_sections(sections)  # [(层级路径, 条目dict), ...]

    # 4. 入库 ChromaDB
    print(f"📦 正在入库 {filename} 到 ChromaDB...")
    ingest_document_to_chroma(content, source_name=filename)

    # 5. 生成全局 MOC 索引
    create_global_index(structure, filename)

    # 6. 并发生成每个知识点的笔记
    print(f"🚀 使用 {concurrency} 个并发线程处理 {len(flat_items)} 个知识点...")

    with ThreadPoolExecutor(max_workers=concurrency) as executor:
        fut_map = {}
        for chapter_path, item in flat_items:
            fut = executor.submit(
                run_autonomous_agent,
                query=item.get("name"),
                item_type=item.get("type", "concept"),
                chapter=chapter_path if chapter_path else "未分类",
                document_name=doc_name,
                current_topics=current_doc_topics,
                global_topics=global_vault_topics,
            )
            fut_map[fut] = item.get("name")

        for fut in as_completed(fut_map):
            name = fut_map[fut]
            try:
                fut.result()
                print(f"  ✅ [{name}] 完成")
            except Exception as e:
                print(f"  ❌ [{name}] 失败: {e}")

    print(f"✅ 【{filename}】 全部解析并链接完成！赶快打开 Obsidian 看看关系图谱吧！")


class PDFHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        file_path = event.src_path
        filename = os.path.basename(file_path)
        time.sleep(1)  # 等文件写完毕

        if file_path.lower().endswith(('.md', '.tex')):
            process_file(file_path)
        elif file_path.lower().endswith('.pdf'):
            print(f"\n[Watcher] 👀 发现新 PDF，触发自动解析流: {filename}")
            if parse_pdf_to_md(file_path):
                # PDF 解析成功后，直接处理生成的 .md 文件
                md_path = file_path.rsplit(".pdf", 1)[0] + ".md"
                if os.path.exists(md_path):
                    process_file(md_path)
            else:
                print("❌ PDF 解析环节出错，流程终止。")
def start_watcher():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
    observer = Observer()
    observer.schedule(PDFHandler(), path=DATA_DIR, recursive=False)
    print(f"🕸️ 双链知识图谱工厂已启动！监听目录: {DATA_DIR}")
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Math Agent — 双链知识图谱工厂")
    parser.add_argument("files", nargs="*", help="要处理的 .md/.tex/.pdf 文件路径（支持通配符）")
    parser.add_argument("-c", "--concurrency", type=int, default=4, help="并发生成线程数（默认 4）")
    parser.add_argument("-a", "--all", action="store_true", help="处理 data/ 目录下所有文件（.md / .tex / .pdf）")
    args = parser.parse_args()

    if args.all:
        import glob
        patterns = ["*.md", "*.tex", "*.pdf", "*.MD", "*.TEX", "*.PDF"]
        all_files = []
        for pat in patterns:
            all_files.extend(glob.glob(os.path.join(DATA_DIR, pat)))
        all_files = sorted(set(all_files))
        if not all_files:
            print(f"📭 data/ 目录下没有可处理的文件。")
        else:
            print(f"📂 发现 {len(all_files)} 个文件待处理: {[os.path.basename(f) for f in all_files]}")
            for fp in all_files:
                process_file(fp, concurrency=args.concurrency)
    elif args.files:
        for fp in args.files:
            abs_path = os.path.abspath(fp)
            if not os.path.exists(abs_path):
                print(f"⚠️ 文件不存在: {abs_path}")
                continue
            process_file(abs_path, concurrency=args.concurrency)
    else:
        start_watcher()