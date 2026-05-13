# tools/obsidian_io.py
import os
import re
from agent_config import Config

def sanitize_filename(name: str) -> str:
    """清理非法字符，保证在 Windows 和 Obsidian 中都是合法的文件名/文件夹名"""
    name = re.sub(r'[\\/*?:"<>|#^]', "", name)
    return name.strip()

def save_markdown_to_obsidian(content: str, filename: str, document_name: str = "", chapter: str = "") -> str:
    """
    保存文件。目录结构：根目录 / 文档名称 / 章节名称 / 笔记.md
    """
    target_dir = Config.OBSIDIAN_NOTES_DIR
    
    # 1. 如果有文档名，进入文档文件夹
    if document_name:
        target_dir = os.path.join(target_dir, sanitize_filename(document_name))
        
    # 2. 如果有章节名，按路径拆分逐级创建子文件夹（支持 "Part I/Chapter 1/Section 1" 多级结构）
    if chapter:
        for part in chapter.split("/"):
            part = part.strip()
            if part:
                target_dir = os.path.join(target_dir, sanitize_filename(part))

    # 3. 创建所有不存在的父级目录
    if not os.path.exists(target_dir):
        os.makedirs(target_dir, exist_ok=True)

    safe_filename = f"{sanitize_filename(filename)}.md"
    file_path = os.path.join(target_dir, safe_filename)

    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        # 返回相对路径方便查看
        relative_path = os.path.join(document_name, chapter, safe_filename)
        return f"✅ 已保存至: {relative_path}"
    except Exception as e:
        return f"❌ 保存失败: {str(e)}"
# tools/obsidian_io.py (在末尾添加)

def get_all_vault_note_titles() -> list[str]:
    """
    遍历整个灵感燃料库，获取所有已存在笔记的标题（文件名）
    用于实现跨文档的自动双向链接
    """
    vault_path = Config.OBSIDIAN_NOTES_DIR
    all_titles = []
    
    if not os.path.exists(vault_path):
        return []

    # 递归遍历文件夹
    for root, dirs, files in os.walk(vault_path):
        for file in files:
            if file.endswith(".md") and not file.startswith("_00_"):
                # 去掉 .md 后缀，作为知识点标题
                title = os.path.splitext(file)[0]
                all_titles.append(title)
                
    return list(set(all_titles)) # 去重