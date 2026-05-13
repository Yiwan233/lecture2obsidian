# tools/pdf_parser.py
import os
import asyncio
from dotenv import load_dotenv
from llama_parse import LlamaParse

_CURRENT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(_CURRENT_DIR, ".env"))

LLAMA_CLOUD_API_KEY = os.getenv("LLAMA_CLOUD_API_KEY", "")

def parse_pdf_to_md(pdf_path: str) -> bool:
    if not LLAMA_CLOUD_API_KEY:
        print("❌ 未配置 LLAMA_CLOUD_API_KEY，请在 .env 中添加 LLAMA_CLOUD_API_KEY=llx-你的key")
        return False

    print(f"\n🦙 正在调用 LlamaParse 专业云端解析: {os.path.basename(pdf_path)} ...")

    try:
        parser = LlamaParse(
            api_key=LLAMA_CLOUD_API_KEY,
            result_type="markdown",  # 强行要求输出 Markdown
            language="ch_sim",       # 支持中文
            num_workers=2
        )
        
        # 这是一个异步库，我们需要用 asyncio 跑它
        parsed_docs = asyncio.run(parser.aload_data(pdf_path))
        
        # 拼接所有页面的 Markdown 文本
        full_md = "\n\n".join([doc.text for doc in parsed_docs])
        
        output_path = pdf_path.replace(".pdf", ".md")
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(full_md)
            
        print(f"✅ 专业解析成功！Markdown 源码已生成: {output_path}")
        return True
        
    except Exception as e:
        print(f"❌ LlamaParse 解析失败: {e}")
        return False