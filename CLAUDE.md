# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 项目概述

清华大学电子系推免复习资料库。将各门课程的知识点整理为 **Obsidian Markdown 文件组**，便于在 Obsidian 中浏览和复习。

## 目录结构

```
<XX> - <课程名>/         # 每门课程一个目录，XX 为课程代码缩写
├── raw/                 # 原始教材 PDF、老师讲义、试题等外部参考资料
├── res/                 # 图片、绘图等附件
├── Index.md             # 课程首页，可包含知识点结构导航的详细说明，**不应保留**课程教师、教材、考试信息等
├── <章节名>.md          # 各章节知识点
├─! CONTENT.md           # **应删除**的目录文件，已由 frontmatter 中的 scenes 定义章节顺序
└─* EXPORT.md            # 可选的导出文件
```

`raw/` 存放该课程的原始资料（教材 PDF、教师讲义、试卷等），可通过 pdf-mcp 工具直接阅读 PDF 文件。

目前已完成 Markdown 化的参考范本：**SS - 信号与系统**、**EM - 电磁场与波**、**SP - 固体物理基础**。

## Markdown 文件格式规范

### 文件组织

- 每章一个 `.md` 文件，文件名 = 章节标题（如 `Fourier 变换 (FT).md`）
- `Index.md` 为课程首页，包含：
  - YAML frontmatter（`longform` 配置，列出所有 scene 即章节）
  - 课程信息（可用 `![[]]` 嵌入图片）
  - 知识点导航列表
- 附件（图片、SVG）放在 `res/` 子目录下，在 frontmatter 中通过 `attachmentFolderPath` 指定

### Frontmatter 格式（Index.md）

```yaml
---
longform:
  format: scenes
  title: <课程名称>
  workflow: Default Workflow
  sceneFolder: /
  scenes:
    - <章节1>
    - <章节2>
    - - <父章节>       # 缩进表示层级
      - <子章节>
  ignoredFiles:
    - CONTENT
    - EXPORT
---
```

### 标题层级

一级标题保留给文件名，章节标题使用二级标题（`##`）开始，子章节依次使用 `###`、`####` 等。

标题前不添加编号，允许使用 LaTeX 宏（如 `\section{\(z\) 变换的定义}` 转为 `## $z$ 变换的定义`）。

### 数学公式

- 行内公式：`$...$`，不论是否内嵌 `cases` 等环境都必须**保持在同一行内**
- 块级公式：`$$...$$`，两个 `$$` 必须**单独成行**
- 使用 Obsidian 兼容的 LaTeX 语法
- 自定义宏：`\dif`（微分 d）、`\e`（自然常数 e）、`\I`（虚数 i）、`\v{...}`（向量）、`\dint`（积分）等

### Callout 语法（Obsidian 特有）

```markdown
> [!definition] 标题
> 内容

> [!theorem] 标题
> 内容

> [!note] 标题
> 内容

> [!tip]
> 内容

> [!danger] 标题
> 内容
```

### 内部链接与图片

- Wikilink 链接：`[[文件名]]` 或 `[[文件名|显示文本]]`
- 图片嵌入：`![[图片名.png]]`（图片在 `res/` 目录下）
- 块引用：`[[文件名#^blockid]]`，标注块 ID `^blockid` 应放在引用内容所在行末并间隔一个空格，对 Callout 块放在**标题行**末

## LaTeX → Markdown 转换

转换流程与排版规则见 `.claude/rules/latex-to-markdown.md`，宏处理速查表见 `.claude/rules/latex-macros.md`。

## Obsidian 配置

- 附件目录：`res/`（在 `.obsidian/app.json` 的 `attachmentFolderPath` 中配置）
- 需要安装的社区插件：Longform（用于长篇写作场景管理）
- 需要开启：Settings > Files & Links > Automatically update internal links
- 忽略文件：`EXPORT.*`、`README.*`、`scripts/`

## 当前进度

| 代码 | 课程 | 状态 |
|------|------|------|
| AC | 高等微积分 | 待转换 (tex) |
| CM | 复变函数与数理方程 | 待创建 |
| CN | 通信与网络 | 待创建 |
| CP | 计算机程序设计基础 | 待创建 |
| DA | 数据与算法 | 待创建 |
| DL | 数字逻辑与处理器基础 | 待创建 |
| DM | 离散数学 | 待创建 |
| EC | 电子电路与系统基础 | 待创建 |
| EM | 电磁场与波 | Markdown 待调整 |
| LA | 线性代数 | 待创建 |
| MC | 媒体与认知 | 待创建 |
| PR | 概率论与随机过程 | 待创建 |
| QS | 量子与统计 | 待创建 |
| SP | 固体物理基础 | Markdown 待调整 |
| SS | 信号与系统 | Markdown 待调整 |
| UP | 大学物理A | 待创建 |

## 工具提示

- LaTeX 公式在 Markdown 中的正确性需在 Obsidian 中验证，不能仅靠源码检查
- 各课程的原始 PDF 教材、讲义等存放在 `raw/` 子目录下，可通过 pdf-mcp 工具直接阅读
- `.tex` 文件中的 tikz 绘图无法直接转换为 Markdown，需截图后放入 `res/`
- 在编辑 `.md` 文件时，避免使用 Obsidian 不支持的 LaTeX 包（如 `nicematrix`、`tcolorbox` 等）
