<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python" alt="Python 3.10+"/>
  <img src="https://img.shields.io/badge/Obsidian-知识图谱-8B5CF6?style=flat-square&logo=obsidian" alt="Obsidian"/>
  <img src="https://img.shields.io/badge/LLM-DeepSeek-4F46E5?style=flat-square" alt="DeepSeek"/>
  <img src="https://img.shields.io/badge/ChromaDB-向量检索-FF6B35?style=flat-square" alt="ChromaDB"/>
  <img src="https://img.shields.io/badge/license-MIT-green?style=flat-square" alt="MIT License"/>
</p>

<h1 align="center">📚 Lecture2Obsidian</h1>

<p align="center">
  <strong>将数学讲义自动转化为 Obsidian 双向链接知识库的智能流水线</strong>
  <br>
  支持 <code>.md</code> · <code>.tex</code> · <code>.pdf</code> → LLM 提取知识点 → ChromaDB 语义检索 → Obsidian 双链图谱
</p>

<p align="center">
  <sub>✨ 不再手动整理笔记，让 AI 帮你构建完整的数学知识网络</sub>
</p>

---

## 🌟 概述

**Lecture2Obsidian** 是一个端到端的自动化流水线，输入数学讲义（Markdown、LaTeX 或 PDF），输出结构化的 Obsidian 笔记库。每一篇笔记都包含严谨的数学定义、LaTeX 公式、YAML 元数据，以及跨文档的语义相关链接。

当你放入一篇新的讲义时，系统会：

1. **理解** — LLM 通读全文，提取章节和知识点树状结构
2. **关联** — ChromaDB 向量检索，自动发现全库语义相关笔记
3. **生成** — 为每个知识点独立生成 Obsidian 笔记，含前向/反向链接
4. **审计** — LaTeX 闭合校验 + 逻辑审计，保证输出质量

> 🎯 **核心理念**：将线性讲义转化为网状知识图谱，让知识点之间「自动连接」。

---

## ✨ 核心特性

| 特性 | 说明 |
|------|------|
| **多格式输入** | 支持 `.md`、`.tex`、`.pdf`（通过 LlamaParse 转换） |
| **LLM 驱动** | 基于 DeepSeek 模型，低温度（0.1）保证数学严谨性 |
| **向量检索** | ChromaDB 持久化存储，自动发现跨文档语义关联 |
| **并发加速** | ThreadPoolExecutor 多线程并行，默认 4 线程，最高 8 线程 |
| **质量保障** | LaTeX 闭合校验、逻辑审计、自动重试（最多 2 次） |
| **文件监听** | Watchdog 实时监控 `data/` 目录，拖入即处理 |
| **TUI 仪表盘** | Rich 构建的实时进度面板，一目了然 |
| **Prompt 防护** | 防泄漏 system prompt + 后处理清洗，输出纯净 Markdown |

---

## 🚀 快速开始

### 前置条件

- **Python 3.10+**
- **Obsidian** — [免费下载](https://obsidian.md)
- **DeepSeek API Key** — [注册获取](https://platform.deepseek.com)
- **LlamaParse API Key**（仅处理 PDF 时需要）— [注册获取](https://cloud.llamaindex.ai)

### 安装

```bash
# 1. 克隆仓库
git clone https://github.com/Yiwan233/lecture2obsidian.git
cd lecture2obsidian

# 2. 创建虚拟环境
python -m venv venv

# Windows
.\venv\Scripts\activate

# 3. 安装依赖
pip install -r requirements.txt

# 4. 配置环境变量
# 编辑 .env 文件填入你的 API Key
```

### 配置 `.env`

```env
DEEPSEEK_API_KEY=sk-你的deepseek密钥
LLAMA_CLOUD_API_KEY=llx-你的llamaparse密钥    # 可选，仅处理 PDF 时需要
OBSIDIAN_NOTES_DIR=E:\你的Obsidian库路径       # 可选，有默认值
```

### 使用

```bash
# 📦 一键处理 data/ 下所有文件（推荐）
python watcher.py -a

# 🚀 8 线程加速
python watcher.py -a -c 8

# 📄 处理指定文件
python watcher.py data/概率论讲义.md
python watcher.py data/*.pdf

# 👀 监听模式（拖入文件即自动处理）
python watcher.py

# 🖥️ TUI 仪表盘
python tui.py data/*.md -c 6
```

---

## 🏗️ 四种运行模式

### 1️⃣ 一键批量 `-a`

```bash
python watcher.py -a           # 处理 data/ 下所有 .md / .tex / .pdf
python watcher.py -a -c 8      # 8 线程并发生成笔记
```

### 2️⃣ 指定文件

```bash
python watcher.py data/概率论.md                # 单个文件
python watcher.py data/*.md                     # 通配符
python watcher.py data/*.md data/*.pdf          # 混合格式
python watcher.py data/Chapter1.pdf -c 6        # PDF + 并发
```

### 3️⃣ 监听模式

```bash
python watcher.py
```
启动后，将文件拖入 `data/` 即自动触发处理，适合持续批量导入。

### 4️⃣ TUI 仪表盘

```bash
python tui.py data/概率论.md               # 单文件
python tui.py data/*.md -c 6               # 批量 + 并发
```

实时面板效果：

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

## 📖 一篇讲义产出了什么？

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

每篇知识点笔记的结构：

```markdown
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

### 三种自动产物

| 产物 | 说明 |
|------|------|
| **知识点笔记** | 每个概念/例题独立成 `.md`，含 YAML frontmatter + LaTeX + 双链 |
| **全局索引 MOC** | `_00_Index_文档名.md` — 整篇讲义的树状目录 |
| **语义相关链接** | 每篇笔记末尾自动追加全库语义最相似的 3 篇已有笔记 |

---

## ⚙️ 流水线工作原理

```
data/ 中的文件 (.md / .tex / .pdf)
    │
    ├── 若是 .pdf ──▶ LlamaParse 转 .md ──┐
    │                                      │
    ▼                                      ▼
┌──────────────────────────────┐
│ ① 宏观知识图谱分析              │  LLM 通读全文 → 章节 → 知识点树状结构
└───────────┬──────────────────┘
            ▼
┌──────────────────────────────┐
│ ② ChromaDB 向量入库            │  文档切片 → 向量化存储（自动去重）
└───────────┬──────────────────┘
            ▼
┌──────────────────────────────┐
│ ③ 生成全局 MOC 索引            │  _00_Index_文档名.md
└───────────┬──────────────────┘
            ▼
   ┌───────┴───────┐       ← ThreadPoolExecutor 并行
   ▼               ▼
 概念 A           概念 B     ...
   │               │
   ├─ ChromaDB 检索相关上下文
   ├─ LLM 生成笔记正文（防泄漏 prompt）
   ├─ LaTeX 闭合检查 + 逻辑审计
   └─ 写入 Obsidian + 语义相似 Top-3 链接
```

### 关键设计

- **Prompt 泄漏防护** — System message 严格约束输出格式，后处理自动清洗代码块包裹、角色扮演文本等泄漏
- **跨科目污染防护** — ChromaDB 检索优先按文档名过滤，逐级降级：精确匹配 → 补 `.md` → 不限来源
- **LaTeX 闭环校验** — 检查 `$$` / `$` 成对闭合，不通过则带建议重试（最多 2 次）

---

## 📁 项目结构

```
lecture2obsidian/
├── watcher.py               ← 入口：CLI 命令 / 文件监听
├── tui.py                   ← 入口：Rich 实时仪表盘
├── main_agent.py            ← LangGraph 流水线核心
├── agent_config.py          ← 全局配置（模型、路径、ChromaDB）
├── state.py                 ← LangGraph 状态类型定义
├── fix_structure.py         ← 结构修复工具
├── test_langsmith.py        ← API 连通性测试
├── requirements.txt         ← Python 依赖
├── .env                     ← API Key 配置（不提交 Git）
├── CLAUDE.md                ← Claude 操作手册
├── tools/
│   ├── vector_db.py         ← ChromaDB 入库 + 检索 + 语义相似度
│   ├── obsidian_io.py       ← Obsidian 文件 IO + 全库标题扫描
│   └── pdf_parser.py        ← PDF → Markdown（LlamaParse）
├── data/                    ← 讲义存放目录
├── chroma_db/               ← ChromaDB 持久化目录（自动生成）
└── output/                  ← 输出缓存
```

---

## 🔧 配置参数

### `agent_config.py`

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `MODEL_NAME` | `deepseek-v4-pro` | DeepSeek 模型 |
| `DEEPSEEK_BASE_URL` | `https://api.deepseek.com` | API 地址 |
| `CHROMA_DB_PATH` | `./chroma_db` | 向量库路径 |
| `CHUNK_SIZE` | `1000` | 文档切片大小（字符） |
| `CHUNK_OVERLAP` | `150` | 切片重叠量 |
| `temperature` | `0.1` | 低温度保证数学严谨性 |

### 并发控制

```bash
-c 4    # 默认 4 线程（稳定优先）
-c 6    # 6 线程（推荐）
-c 8    # 8 线程（网络好时更快）
```

---

## ❓ FAQ

<details>
<summary><b>处理 PDF 报错 "未配置 LLAMA_CLOUD_API_KEY"？</b></summary>

在 `.env` 中添加 `LLAMA_CLOUD_API_KEY=llx-你的key`，去 [cloud.llamaindex.ai](https://cloud.llamaindex.ai) 免费注册获取。
</details>

<details>
<summary><b>一直卡在 "正在进行宏观知识图谱分析"？</b></summary>

大文档的 API 调用最多 3 分钟超时。如果频繁超时，将 `agent_config.py` 中的 `CHUNK_SIZE` 调小（如 `60000` → `30000`）。
</details>

<details>
<summary><b>生成的笔记质量不满意？</b></summary>

- 降低 `temperature` 到 `0`
- 增加重试次数（`main_agent.py` 中 `iteration >= 2` 改为更大值）
- 换用更强的模型（`MODEL_NAME` 改为 `deepseek-v4-pro`）
</details>

<details>
<summary><b>Obsidian 关系图谱中看不到跨文档链接？</b></summary>

1. 确认两篇讲义都在同一个 Obsidian 库路径下
2. 调低语义相似度阈值（`vector_db.py` 中 `find_similar_notes()` 的 `0.25`）
</details>

<details>
<summary><b>虚拟环境的依赖损坏了怎么办？</b></summary>

```bash
python -m venv venv --clear
.\venv\Scripts\activate
pip install -r requirements.txt
```
</details>

---

## 📊 技术栈

| 组件 | 技术 |
|------|------|
| **AI 模型** | DeepSeek (via LangChain ChatOpenAI) |
| **向量数据库** | ChromaDB + all-MiniLM-L6-v2 |
| **PDF 解析** | LlamaParse |
| **并行框架** | ThreadPoolExecutor |
| **文件监听** | watchdog |
| **TUI 界面** | Rich |
| **状态编排** | LangGraph |

---

## 📄 许可证

[MIT License](LICENSE)

---

<p align="center">
  <b>Lecture2Obsidian</b> — 让每篇讲义都成为你知识网络的一部分
  <br>
  <a href="https://github.com/Yiwan233/lecture2obsidian">GitHub</a>
</p>
