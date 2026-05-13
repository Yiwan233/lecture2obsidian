"""
补救脚本：只重新提取多级结构（1 次 API），然后把已生成的笔记搬到正确目录。
不重新生成笔记内容——保护已花的 API 额度。
"""
import sys
import os
import shutil

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

from agent_config import Config
from tools.obsidian_io import sanitize_filename, save_markdown_to_obsidian
from watcher import extract_hierarchical_structure, create_global_index, _flatten_sections, _collect_leaf_names


def find_existing_note(vault_doc_dir: str, item_name: str) -> str | None:
    """在文档文件夹下递归查找已生成的笔记文件，返回完整路径或 None"""
    safe_name = sanitize_filename(item_name) + ".md"
    for root, _, files in os.walk(vault_doc_dir):
        for f in files:
            if f == safe_name:
                return os.path.join(root, f)
    return None


def move_notes_to_new_structure(source_filepath: str, dry_run: bool = False):
    """
    1. 重新提取多级结构（1 次 API）
    2. 找到已生成的旧笔记 → 搬到新的多级目录
    3. 重新生成 MOC
    4. 清理空目录
    """
    filename = os.path.basename(source_filepath)
    print(f"\n{'[DRY RUN] ' if dry_run else ''}🔧 正在修复: {filename}")

    # 1. 读取源文件 + 重新提取结构
    if not os.path.exists(source_filepath):
        print(f"❌ 文件不存在: {source_filepath}")
        return

    with open(source_filepath, "r", encoding="utf-8") as f:
        content = f.read()

    structure = extract_hierarchical_structure(content, filename)
    doc_name = sanitize_filename(structure.get("document_name", os.path.splitext(filename)[0]))
    sections = structure.get("sections", [])
    flat_items = _flatten_sections(sections)

    vault_doc_dir = os.path.join(Config.OBSIDIAN_NOTES_DIR, doc_name)
    if not os.path.exists(vault_doc_dir):
        print(f"⚠️ 未找到已生成的文档目录: {vault_doc_dir}")
        print("   将按新结构从头生成笔记（请运行 python watcher.py -a）。")
        return

    # 2. 遍历叶子条目，搬移已有笔记
    moved = 0
    not_found = []
    for new_path, item in flat_items:
        item_name = item.get("name")
        old_file = find_existing_note(vault_doc_dir, item_name)

        if old_file:
            # 新路径
            new_dir = vault_doc_dir
            if new_path:
                for part in new_path.split("/"):
                    part = part.strip()
                    if part:
                        new_dir = os.path.join(new_dir, sanitize_filename(part))
            new_file = os.path.join(new_dir, sanitize_filename(item_name) + ".md")

            if os.path.abspath(old_file) == os.path.abspath(new_file):
                print(f"  ⏭ {item_name} 已在正确位置，跳过")
                continue

            if dry_run:
                print(f"  📦 {item_name}: {os.path.relpath(old_file, vault_doc_dir)} → {os.path.relpath(new_file, vault_doc_dir)}")
            else:
                os.makedirs(new_dir, exist_ok=True)
                shutil.move(old_file, new_file)
                print(f"  ✅ {item_name}: 已搬至 {os.path.relpath(new_file, vault_doc_dir)}")
            moved += 1
        else:
            not_found.append(item_name)

    # 3. 重新生成 MOC
    if not dry_run:
        create_global_index(structure, filename)
    else:
        print(f"\n  [DRY RUN] 将重新生成 MOC: _00_Index_{doc_name}.md")

    # 4. 清理空目录（旧 flat 层级留下的空文件夹）
    if not dry_run:
        cleaned = 0
        for root, dirs, files in os.walk(vault_doc_dir, topdown=False):
            if root == vault_doc_dir:
                continue
            if not os.listdir(root):
                os.rmdir(root)
                cleaned += 1
        if cleaned:
            print(f"\n🧹 已清理 {cleaned} 个空目录")

    # 总结
    print(f"\n📊 修复摘要:")
    print(f"   叶子知识点: {len(flat_items)}")
    print(f"   已搬移: {moved}")
    print(f"   未找到旧文件（需重新生成）: {len(not_found)}")
    if not_found:
        for name in not_found:
            print(f"     - {name}")
        print(f"\n💡 这些知识点需要运行 python watcher.py {source_filepath} 补充生成。")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="修复旧版扁平结构 → 新版多级结构（保护已有笔记内容）")
    parser.add_argument("files", nargs="+", help="源文件路径（.md / .tex / .pdf）")
    parser.add_argument("--dry-run", action="store_true", help="只预览搬移计划，不实际执行")
    args = parser.parse_args()

    for fp in args.files:
        ap = os.path.abspath(fp)
        if not os.path.exists(ap):
            print(f"⚠️ 文件不存在: {ap}")
            continue
        move_notes_to_new_structure(ap, dry_run=args.dry_run)
