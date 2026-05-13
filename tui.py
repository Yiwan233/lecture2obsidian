"""
TUI 模式 — 使用 Rich 实时渲染处理进度仪表盘。

用法:
  python tui.py data/随机微积分讲义.md
  python tui.py data/*.md -c 6
"""
import os
import sys
import time
import threading

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
from concurrent.futures import ThreadPoolExecutor, wait, FIRST_COMPLETED
from io import StringIO
from contextlib import redirect_stdout

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

from rich.live import Live
from rich.panel import Panel
from rich.progress import Progress, BarColumn, TextColumn, SpinnerColumn
from rich.console import Console, Group
from rich.text import Text
from rich.layout import Layout
from rich import box

from watcher import extract_hierarchical_structure, create_global_index, _flatten_sections, _collect_leaf_names
from tools.vector_db import ingest_document_to_chroma
from tools.obsidian_io import sanitize_filename, get_all_vault_note_titles
from main_agent import run_autonomous_agent


STATUS_ICON = {
    "pending": "⏳",
    "running": "🔄",
    "done": "✅",
    "failed": "❌",
}


def process_with_tui(filepath: str, concurrency: int = 4):
    console = Console()
    filename = os.path.basename(filepath)

    if not os.path.exists(filepath):
        console.print(f"[red]文件不存在: {filepath}[/red]")
        return

    # ── Phase 1: 读取 → 结构分析 → ChromaDB → MOC (顺序) ──
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    with Progress(SpinnerColumn(), TextColumn("[bold]{task.description}"), console=console) as p:
        t = p.add_task("🧠 提取文档结构...", total=None)
        structure = extract_hierarchical_structure(content, filename)
        p.update(t, description="📦 入库 ChromaDB...")
        ingest_document_to_chroma(content, source_name=filename)
        p.update(t, description="🌐 生成全局索引...")
        create_global_index(structure, filename)

    doc_name = sanitize_filename(structure.get("document_name", os.path.splitext(filename)[0]))
    sections = structure.get("sections", [])
    current_doc_topics = _collect_leaf_names(sections)
    flat_items = _flatten_sections(sections)  # [(层级路径, 条目dict), ...]
    items = [
        (path if path else "未分类", item)
        for path, item in flat_items
    ]
    global_vault_topics = get_all_vault_note_titles()

    # ── Phase 2: 并发生成 (Rich TUI 仪表盘) ──
    status: dict[str, dict] = {}
    for ch_name, item in items:
        status[item.get("name")] = {"chapter": ch_name, "status": "pending"}

    log_buffer: list[str] = []
    log_lock = threading.Lock()
    status_lock = threading.Lock()
    start_time = time.time()

    def add_log(msg: str):
        with log_lock:
            log_buffer.append(f"[{time.strftime('%H:%M:%S')}] {msg}")
            if len(log_buffer) > 100:
                log_buffer[:50] = []

    def make_dashboard():
        elapsed = time.time() - start_time
        with status_lock:
            done_cnt = sum(1 for s in status.values() if s["status"] == "done")
            fail_cnt = sum(1 for s in status.values() if s["status"] == "failed")
            run_cnt = sum(1 for s in status.values() if s["status"] == "running")
            total = len(status)

        # ── Header ──
        h = Text(f"📚 {filename}  ", style="bold cyan")
        h.append(f"并发 {concurrency}  ", style="yellow")
        h.append(f"总计 {total}  ", style="white")
        h.append(f"✅ {done_cnt}  ", style="green")
        h.append(f"🔄 {run_cnt}  ", style="blue")
        h.append(f"❌ {fail_cnt}  ", style="red")
        h.append(f"⏱ {elapsed:.0f}s", style="white")
        header = Panel(h, box=box.ROUNDED)

        # ── Body: 按章节分组 ──
        chapters: dict[str, list[str]] = {}
        with status_lock:
            for name, info in status.items():
                chapters.setdefault(info["chapter"], []).append(
                    f"  {STATUS_ICON.get(info['status'], '⏳')} {name}"
                )
        body_lines = []
        for ch, names in chapters.items():
            body_lines.append(f"\n[bold yellow]📑 {ch}[/bold yellow]")
            body_lines.extend(names)
        body = Panel("\n".join(body_lines), title="处理进度", box=box.ROUNDED, padding=(1, 2))

        # ── 进度条 ──
        prog = Progress(
            TextColumn("[bold]{task.description}"),
            BarColumn(),
            TextColumn("{task.completed}/{task.total}"),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        )
        prog.add_task("总进度", total=total, completed=done_cnt)

        # ── 日志 ──
        with log_lock:
            recent = log_buffer[-6:]
        log_text = "\n".join(recent) if recent else "[dim]等待处理...[/dim]"

        footer = Panel(
            Group(prog, Text("\n" + log_text)),
            title="最近日志",
            box=box.ROUNDED,
            height=9,
        )

        return Layout().split(
            Layout(header, size=3),
            Layout(body),
            Layout(footer, size=9),
        )

    # ── 单个概念的处理函数（捕获 stdout 到日志） ──
    def run_one(name: str, ch_name: str, item: dict):
        with status_lock:
            status[name]["status"] = "running"
        add_log(f"🔄 开始: {name}")

        buf = StringIO()
        with redirect_stdout(buf):
            try:
                run_autonomous_agent(
                    query=name,
                    item_type=item.get("type", "concept"),
                    chapter=ch_name,
                    document_name=doc_name,
                    current_topics=current_doc_topics,
                    global_topics=global_vault_topics,
                )
                new_st = "done"
                add_log(f"✅ 完成: {name}")
            except Exception as e:
                new_st = "failed"
                add_log(f"❌ 失败: {name} — {e}")

        with status_lock:
            status[name]["status"] = new_st

        for line in buf.getvalue().split("\n"):
            if line.strip():
                add_log(line.strip())

    # ── TUI 主循环 ──
    try:
        with Live(console=console, refresh_per_second=4, screen=True) as live:
            live.update(make_dashboard())

            with ThreadPoolExecutor(max_workers=concurrency) as executor:
                fut_map = {
                    executor.submit(run_one, it.get("name"), ch, it): it.get("name")
                    for ch, it in items
                }
                while fut_map:
                    done, fut_map = wait(fut_map, timeout=0.2, return_when=FIRST_COMPLETED)
                    live.update(make_dashboard())
    except KeyboardInterrupt:
        console.print("\n[yellow]⚠️ 用户中断[/yellow]")

    # ── 最终摘要 ──
    console.clear()
    with status_lock:
        d = sum(1 for s in status.values() if s["status"] == "done")
        f = sum(1 for s in status.values() if s["status"] == "failed")
    t = time.time() - start_time
    console.print(
        f"[bold green]✅ 处理完成！[/bold green]  "
        f"知识点 {len(status)}  成功 {d}  失败 {f}  耗时 {t:.0f}s"
    )


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Math Agent TUI — 实时仪表盘")
    parser.add_argument("files", nargs="+", help="要处理的 .md/.tex 文件")
    parser.add_argument("-c", "--concurrency", type=int, default=4, help="并发线程数（默认 4）")
    args = parser.parse_args()

    for fp in args.files:
        ap = os.path.abspath(fp)
        if not os.path.exists(ap):
            print(f"⚠️ 文件不存在: {ap}")
            continue
        process_with_tui(ap, concurrency=args.concurrency)
