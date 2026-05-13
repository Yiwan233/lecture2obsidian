import os
from dotenv import load_dotenv

# 获取绝对路径
_CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

# 加载 .env
load_dotenv(os.path.join(_CURRENT_DIR, ".env"))

class Config:
    # --- 0. 路径配置 ---
    # 将 BASE_DIR 放入类中，方便其他脚本调用
    BASE_DIR = _CURRENT_DIR
    
    # --- 1. 模型配置 ---
    DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
    DEEPSEEK_BASE_URL = "https://api.deepseek.com"
    MODEL_NAME = "deepseek-v4-pro"
    
    # --- 2. Obsidian 配置 ---
    OBSIDIAN_NOTES_DIR = os.getenv("OBSIDIAN_NOTES_DIR") or r"E:\我的仓库\3-Resources（灵感燃料库）"

    # --- 3. 向量库 (ChromaDB) 配置 ---
    CHROMA_DB_PATH = os.path.join(BASE_DIR, "chroma_db")
    
    # --- 4. 切片参数 ---
    CHUNK_SIZE = 1000
    CHUNK_OVERLAP = 150

# 启动时的基础环境检查
if not Config.DEEPSEEK_API_KEY:
    raise RuntimeError(
        "❌ 未配置 DEEPSEEK_API_KEY！请在项目根目录的 .env 文件中添加: DEEPSEEK_API_KEY=sk-你的key"
    )

if not os.path.exists(Config.OBSIDIAN_NOTES_DIR):
    os.makedirs(Config.OBSIDIAN_NOTES_DIR, exist_ok=True)
    print(f"✅ 目录已就绪: {Config.OBSIDIAN_NOTES_DIR}")