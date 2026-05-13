# Math Agent — 从讲义到 Obsidian 知识库

> **⚡ 请先阅读本文** —— 这是一份自包含的操作手册，读完即可独立完成从讲义到 Obsidian 知识图谱的全流程。

自动将数学讲义（`.md` / `.tex` / `.pdf`）转化为 Obsidian 双向链接知识库的流水线。

---

## 目录

- [快速开始（5 分钟）](#快速开始5-分钟)
- [三种运行模式](#三种运行模式)
- [命令速查表](#命令速查表)
- [产出物说明](#一篇讲义产出了什么)
- [流水线原理](#流水线工作原理)
- [项目结构](#项目结构)
- [配置参考](#配置参考)
- [FAQ](#faq)

---

## 快速开始（5 分钟）

### ① 环境要求

| 依赖 | 用途 | 如何获取 |
|------|------|----------|
| **Python 3.10+** | 运行流水线 | `python --version` 确认 |
| **Obsidian** | 查看生成的知识图谱 | [obsidian.md](https://obsidian.md) 免费下载 |
| **DeepSeek API Key** | 调用大模型提取知识点 | [platform.deepseek.com](https://platform.deepseek.com) 注册即送额度 |
| **LlamaParse API Key** | PDF 转 Markdown（可选，仅处理 PDF 时需要） | [cloud.llamaindex.ai](https://cloud.llamaindex.ai) 注册获取 |

### ② 配置 `.env`

在项目根目录创建 `.env` 文件（已创建则跳过）：

```env
# 必填 — 大模型 API
DEEPSEEK_API_KEY=sk-你的deepseek密钥

# 必填 — PDF 解析（不处理 PDF 可不填）
LLAMA_CLOUD_API_KEY=llx-你的llamaparse密钥

# 可选 — Obsidian 输出路径（默认指向下方路径，不同才改）
OBSIDIAN_NOTES_DIR=E:\你的Obsidian库路径
```

> 默认输出路径：`E:\我的仓库\3-Resources（灵感燃料库）`

### ③ 激活虚拟环境

```bash
# PowerShell
.\venv\Scripts\Activate.ps1

# CMD
.\venv\Scripts\activate.bat
```

> 也可用绝对路径跳过激活：`.\venv\Scripts\python watcher.py -a`

### ④ 放入讲义

将 `.md` / `.tex` / `.pdf` 文件放入 `data/` 目录：

```
data/
├── 概率论讲义.md
├── 实分析笔记.tex
├── Chapter1.pdf
└── Chapter2.pdf
```

### ⑤ 执行

```bash
# 一键处理 data/ 下所有文件
python watcher.py -a

# 或者指定并发数加速（默认 4）
python watcher.py -a -c 6
```

### ⑥ 查看结果

打开 Obsidian → 选择你的库路径 → 点击 **关系图谱**（Graph View）即可看到自动生成的 `[[双链]]` 网状知识结构。

---

## 三种运行模式

### 模式一：一键批量 `-a`（推荐）

```bash
python watcher.py -a           # 处理 data/ 下所有 .md / .tex / .pdf
python watcher.py -a -c 8      # 8 线程并发生成笔记
```

### 模式二：指定文件

```bash
python watcher.py data/概率论.md                # 单个文件
python watcher.py data/*.md                     # 通配符 — 所有 Markdown
python watcher.py data/*.md data/*.pdf          # 混合格式批量
python watcher.py data/Chapter1.pdf -c 6        # 单个 PDF + 并发
```

### 模式三：监听模式

```bash
python watcher.py               # 启动文件监听
```

启动后，将文件拖入 `data/` 即自动触发处理，适合持续批量导入。

### 模式四：TUI 仪表盘

```bash
python tui.py data/概率论.md               # 单个文件 + 实时进度面板
python tui.py data/*.md -c 6               # 批量 + 并发
```

实时效果：

```
┌──────────────────────────────────────────────────────────────────┐
│  📚 概率论.md      并发 4    总计 12    ✅ 8   🔄 3   ❌ 1   ⏱ 45s  │
├──────────────────────────────────────────────────────────────────┤
│  📑 第一章：随机事件与概率                                        │
│    ✅ 样本空间与事件                                              │
│    🔄 条件概率                                                   │
│    ⏳ 全概率公式与贝叶斯定理                                     │
│  📑 第二章：随机变量及其分布                                      │
│    ❌ 期望与方差                                                 │
│    🔄 矩母函数                                                   │
├──────────────────────────────────────────────────────────────────┤
│  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░  8/12  67%                           │
│  [14:32:04] ✅ 完成: 样本空间与事件                               │
│  [14:32:05] ❌ 失败: 期望与方差 — 逻辑审计未通过                  │
└──────────────────────────────────────────────────────────────────┘
```

---

## 命令速查表

| 命令 | 作用 |
|------|------|
| `python watcher.py -a` | 一键处理 `data/` 下所有文件 |
| `python watcher.py -a -c 8` | 同上，8 线程加速 |
| `python watcher.py data/xxx.md` | 处理指定文件 |
| `python watcher.py data/*.pdf` | 批量处理所有 PDF |
| `python watcher.py` | 启动文件监听模式 |
| `python tui.py data/xxx.md` | TUI 仪表盘（单文件） |
| `python tui.py data/*.md -c 6` | TUI 仪表盘（批量） |

---

## 一篇讲义产出了什么？

以 `概率论.md` 为例，处理后在 Obsidian 库中生成：

```
📂 概率论/
├── 📂 第一章：随机事件与概率/
│   ├── 样本空间与事件.md
│   ├── 条件概率.md
│   └── 例1：两枚硬币问题.md
├── 📂 第二章：随机变量及其分布/
│   ├── 离散型随机变量.md
│   └── ...
└── 📄 _00_Index_概率论.md   ← 全局索引 MOC
```

每个知识点笔记的结构：

```yaml
---
tags:
  - concept            # 概念用 concept，例题用 example
document: "[[概率论]]"
chapter: "[[第一章：随机事件与概率]]"
---

# 条件概率

严谨的数学定义、公式推导（严格 LaTeX）……

## 相关笔记
- [[全概率公式]]        ← 语义自动发现
- [[贝叶斯定理]]        ← 跨文档也能链接
```

**三种自动产物：**

| 产物 | 说明 |
|------|------|
| **知识点笔记** | 每个概念/例题独立成 `.md`，含 YAML frontmatter + LaTeX + 双链 |
| **全局索引 MOC** | `_00_Index_文档名.md` — 整篇讲义的树状目录 |
| **语义相关链接** | 每篇笔记末尾自动追加全库语义最相似的 3 篇已有笔记 |

---

## 流水线工作原理

```
data/ 中的文件 (.md / .tex / .pdf)
    │
    ├── 若是 .pdf ──▶ LlamaParse 转 .md ──┐
    │                                      │
    ▼                                      ▼
┌─────────────────────────┐
│ ① 知识图谱分析           │  LLM 通读全文 → 提取 章节 → 概念/例题 树状结构
└───────────┬─────────────┘
            ▼
┌─────────────────────────┐
│ ② ChromaDB 入库          │  文档切片 → 向量化存储（同文件自动去重）
└───────────┬─────────────┘
            ▼
┌─────────────────────────┐
│ ③ 生成全局 MOC 索引       │  创建 _00_Index_文档名.md
└───────────┬─────────────┘
            ▼
   ┌───────┴───────┐       ← ThreadPoolExecutor 并行（默认 4 线程）
   ▼               ▼
 概念 A           概念 B     ...
   │               │
   ├─ ChromaDB 检索相关上下文
   ├─ LLM 生成笔记正文（system prompt 防泄漏）
   ├─ LaTeX 闭合检查 + 逻辑审计（最多重试 2 次）
   └─ 写入 Obsidian + 全库语义相似 Top-3 链接
```

### 关键设计决策

**Prompt 泄漏防护** — 生成节点使用 system message 严格约束输出格式，后处理 `clean_output_for_obsidian()` 自动清洗代码块包裹、角色扮演文本、元文本等泄漏。

**跨科目污染防护** — ChromaDB 检索优先按文档名过滤，降级策略：精确匹配 → 尝试补 `.md` → 不限来源。System prompt 要求模型忽略跨学科上下文。

**LaTeX 闭环校验** — `check_latex_closures()` 检查 `$$` 和 `$` 成对闭合，不通过则带建议重试（最多 2 次）。

---

## 项目结构

```
math_agent/
├── watcher.py               ← 入口：CLI 命令 / 文件监听
├── tui.py                   ← 入口：Rich 实时仪表盘
├── main_agent.py            ← LangGraph 流水线（检索 → 生成 → 审计 → 保存）
├── agent_config.py          ← 全局配置（模型、路径、ChromaDB）
├── state.py                 ← LangGraph 状态类型定义
├── test_langsmith.py        ← DeepSeek 连通性测试
├── tools/
│   ├── vector_db.py         ← ChromaDB 入库 + 检索 + 语义相似度
│   ├── obsidian_io.py       ← Obsidian 文件 IO + 全库标题扫描
│   └── pdf_parser.py        ← PDF → Markdown（LlamaParse）
├── data/                    ← 讲义放这里
├── chroma_db/               ← ChromaDB 持久化目录（自动生成）
├── requirements.txt         ← Python 依赖
├── .env                     ← API Key 配置（不提交 Git）
└── CLAUDE.md                ← 📖 你正在读的文件
```

---

## 配置参考

### `agent_config.py` 可调参数

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `MODEL_NAME` | `deepseek-v4-pro` | DeepSeek 模型 |
| `DEEPSEEK_BASE_URL` | `https://api.deepseek.com` | API 地址 |
| `CHROMA_DB_PATH` | `./chroma_db` | 向量库路径 |
| `CHUNK_SIZE` | `1000` | 文档切片大小（字符） |
| `CHUNK_OVERLAP` | `150` | 切片重叠量 |
| `OBSIDIAN_NOTES_DIR` | `E:\我的仓库\3-Resources（灵感燃料库）` | 输出路径（可通过 `.env` 覆盖） |

### LLM 调用参数

| 参数 | 值 | 说明 |
|------|-----|------|
| `temperature` | `0.1` | 低温度保证数学严谨性 |
| `max_tokens` | `2048`（生成笔记）/ `4096`（结构提取） | 防止超长输出 |
| `timeout` | `180s` | API 超时保护 |
| `max_retries` | `2` | 失败自动重试 |

### 并发控制

```bash
-c 4    # 默认 4 线程（稳定优先）
-c 6    # 6 线程（推荐）
-c 8    # 8 线程（网络好时更快）
```

### `.env` 完整变量清单

```env
DEEPSEEK_API_KEY=sk-xxxxxxxx        # 必填
LLAMA_CLOUD_API_KEY=llx-xxxxxxxx    # 处理 PDF 必填
OBSIDIAN_NOTES_DIR=E:\你的库路径     # 可选（有默认值）
```

---

## FAQ

### Q: 处理 PDF 报错 "未配置 LLAMA_CLOUD_API_KEY"？

在 `.env` 中添加：
```env
LLAMA_CLOUD_API_KEY=llx-你的key
```
去 [cloud.llamaindex.ai](https://cloud.llamaindex.ai) 免费注册获取。

### Q: 一直卡在 "正在进行宏观知识图谱分析"？

大文档的 API 调用需要时间（最多 3 分钟超时）。如果频繁超时，将 `agent_config.py` 的 `CHUNK_SIZE` 调小（如 `60000` → `30000`）。

### Q: 生成的笔记质量不满意？

- 降低 temperature：在 `agent_config.py` 中将 `temperature` 从 `0.1` 调到 `0`
- 增加重试次数：在 `main_agent.py` 中将 `iteration >= 2` 改为更大的值
- 换用更强的模型：将 `MODEL_NAME` 改为 `deepseek-v4-pro`

### Q: Obsidian 关系图谱中看不到跨文档链接？

确认两点：
1. 两篇讲义都在同一个 Obsidian 库路径下
2. 语义相似度阈值 `0.25`（在 `vector_db.py` 的 `find_similar_notes()` 中），可酌情调低

### Q: 虚拟环境的依赖损坏了怎么办？

```bash
# 重新创建虚拟环境
python -m venv venv --clear
.\venv\Scripts\activate
pip install -r requirements.txt
```

### Q: 需要处理的文件超过 10 个？

分批处理避免 API 限流：

```bash
python watcher.py data/Chapter1.pdf data/Chapter2.pdf -c 4
python watcher.py data/Chapter3.pdf data/Chapter4.pdf -c 4
```
