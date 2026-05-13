import sys
import os
import re
import math

# Windows GBK 终端适配：强制 stdout 使用 UTF-8，避免 emoji 打印崩溃
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
# 引入更强大的多语言切分器
from langchain_text_splitters import MarkdownTextSplitter, RecursiveCharacterTextSplitter, Language

from agent_config import Config

print("⏳ 正在加载本地 Embedding 模型...")
embeddings = HuggingFaceEmbeddings(model_name="BAAI/bge-small-zh-v1.5")
print("✅ 模型加载完毕！")
def ingest_document_to_chroma(file_content: str, source_name: str = "lecture_note"):
    """
    根据文件类型（.md 或 .tex）自动选择切片策略，并存入 ChromaDB。
    自动去重：同一 source_name 的旧切片会在写入前被清除。
    """
    target_db_path = Config.CHROMA_DB_PATH

    # 自动识别格式并选择对应的切片器
    if source_name.lower().endswith(".tex"):
        print("📐 识别到 LaTeX 源码，正在启用 TeX 语法切分引擎...")
        text_splitter = RecursiveCharacterTextSplitter.from_language(
            language=Language.LATEX,
            chunk_size=Config.CHUNK_SIZE,
            chunk_overlap=Config.CHUNK_OVERLAP
        )
    else:
        print("📝 识别到 Markdown 文档，启用 MD 语法切分引擎...")
        text_splitter = MarkdownTextSplitter(
            chunk_size=Config.CHUNK_SIZE,
            chunk_overlap=Config.CHUNK_OVERLAP
        )

    chunks = text_splitter.split_text(file_content)
    print(f"🔪 文档被智能切分为 {len(chunks)} 个片段。准备入库...")

    # 以追加模式打开（或创建）向量库
    vector_db = Chroma(
        persist_directory=target_db_path,
        embedding_function=embeddings,
        collection_metadata={"hnsw:space": "cosine"},
    )

    # 清除同一源的旧切片，避免重复
    existing = vector_db.get(where={"source": source_name})
    if existing and existing.get("ids"):
        vector_db.delete(ids=existing["ids"])
        print(f"🧹 已清除 {len(existing['ids'])} 个旧切片 ({source_name})")

    # 写入新切片
    vector_db.add_texts(
        texts=chunks,
        metadatas=[{"source": source_name, "chunk_index": i} for i in range(len(chunks))]
    )

    return f"✅ 成功将 {len(chunks)} 个片段存入向量库: {target_db_path}"
def retrieve_from_chroma(query: str, k: int = 3, source_filter: str = None) -> list[str]:
    """
    根据问题从数据库中检索最相关的讲义片段。
    如果指定 source_filter，则只返回该源文档的片段。
    自动兼容有无 .md 后缀的情况。
    """
    target_db_path = Config.CHROMA_DB_PATH
    if not os.path.exists(target_db_path): return ["⚠️ 知识库为空。"]
    vector_db = Chroma(persist_directory=target_db_path, embedding_function=embeddings)

    if source_filter:
        # 尝试匹配原始名称和加上 .md 的名称
        candidates = [source_filter]
        if not source_filter.endswith('.md'):
            candidates.append(source_filter + '.md')
        for name in candidates:
            results = vector_db.similarity_search(query, k=k, filter={"source": name})
            if len(results) >= k:
                return [doc.page_content for doc in results]
        # 都没有足够结果，降级为不限来源
        results = vector_db.similarity_search(query, k=k)
    else:
        results = vector_db.similarity_search(query, k=k)

    return [doc.page_content for doc in results]

def find_similar_notes(query_text: str, exclude_title: str = "", top_k: int = 3) -> list[str]:
    """
    在 Obsidian vault 所有已生成笔记中，找到与 query_text 语义最相似的 top_k 个笔记标题。
    不依赖 ChromaDB，遍历 .md 文件 + embedding 余弦相似度实时计算。
    """
    vault_path = Config.OBSIDIAN_NOTES_DIR
    if not os.path.exists(vault_path):
        return []

    note_texts, note_titles = [], []
    for root, _, files in os.walk(vault_path):
        for file in files:
            if not file.endswith(".md") or file.startswith("_"):
                continue
            title = os.path.splitext(file)[0]
            if title == exclude_title:
                continue
            filepath = os.path.join(root, file)
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()
            except Exception:
                continue
            # 去掉 YAML frontmatter
            content = re.sub(r'^---\n.*?\n---\n', '', content, flags=re.DOTALL)
            if not content.strip():
                continue
            note_texts.append(content)
            note_titles.append(title)

    if not note_texts:
        return []

    query_emb = embeddings.embed_query(query_text)
    all_embs = embeddings.embed_documents(note_texts)

    def _cosine_sim(a: list[float], b: list[float]) -> float:
        dot = sum(ai * bi for ai, bi in zip(a, b))
        na = math.sqrt(sum(ai * ai for ai in a))
        nb = math.sqrt(sum(bi * bi for bi in b))
        return dot / (na * nb) if na and nb else 0

    scored = [(title, _cosine_sim(query_emb, emb)) for title, emb in zip(note_titles, all_embs)]
    scored.sort(key=lambda x: x[1], reverse=True)

    return [title for title, sim in scored[:top_k] if sim > 0.25]

# ==========================================
# 批量入库脚本 (替换原来的测试代码)
# ==========================================
if __name__ == "__main__":
    import glob

    # 指定你的存放资料的文件夹
    DATA_FOLDER = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data")
    
    if not os.path.exists(DATA_FOLDER):
        os.makedirs(DATA_FOLDER)
        print(f"📁 已为你创建数据存放文件夹: {DATA_FOLDER}，请把 .md 或 .txt 文件放进去。")
    
    # 扫描文件夹下所有的 markdown 文件
    files = glob.glob(os.path.join(DATA_FOLDER, "*.md"))
    
    if not files:
        print("📭 data 文件夹里还没有文件呢，快放几个 .md 文件进去试试！")
    else:
        for file_path in files:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
                file_name = os.path.basename(file_path)
                print(f"\n📖 正在读取: {file_name}")
                print(ingest_document_to_chroma(content, source_name=file_name))
        
        # 顺便测试一下检索
        print("\n--- 检索测试 ---")
        print(retrieve_from_chroma("讲义里关于伊藤积分是怎么说的？"))