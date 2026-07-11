---
name: latex-macros
description: Use when converting .tex LaTeX source files to Obsidian Markdown. Provides a lookup table of LaTeX macros — which ones can be preserved (defined in preamble.sty) and which must be expanded to native LaTeX/MathJax syntax. Also covers theorem environment → callout mappings, section commands → heading mappings, and coloring/font commands → bold/italic conversions.
---

# LaTeX 宏在 Markdown 中的处理规则

此文件记录从 `.tex` 源文件向 Obsidian Markdown 转换时，各 LaTeX 宏的处理方式。

## 判断依据

Obsidian 中已加载 `preamble.sty` 作为 MathJax 宏定义片段（位于 `.obsidian/snippets/preamble.sty`）。此文件中定义的宏在 Markdown 公式中**可以直接使用**，无需展开。

`.tex` 源文件中可能另有局部 `\newcommand` 定义，这些宏**不**在 preamble.sty 中，必须在转换时展开为原生 LaTeX/MathJax 语法。

---

## 可以且应该保留的宏

以下宏在 `preamble.sty` 中已定义，Markdown 文件中**保持原样即可**：

### 微积分符号

| 宏 | 展开结果 | 用途 |
|-----|---------|------|
| `\dif` | `\mathop{}\!\mathrm{d}` | 微分算子 d |
| `\Dif` | `\mathop{}\!\mathrm{D}` | 大写微分算子 |
| `\dint` | `{\displaystyle\int}` | 行内 displaystyle 积分 |

### 向量符号

| 宏 | 展开结果 | 用途 |
|-----|---------|------|
| `\v{x}` | `\vec{\boldsymbol{x}}` | 向量 |
| `\vu{x}` | `\hat{\boldsymbol{x}}` | 单位向量 |
| `\vr` | `\v{r}` | 位置向量快捷方式 |
| `\vv` | `\v{v}` | 速度向量快捷方式 |

### 特殊常数

| 宏 | 展开结果 | 用途 |
|-----|---------|------|
| `\e` | `\mathrm{e}` | 自然常数 |
| `\I` | `\mathbb{i}` | 虚数单位（注意是 blackboard bold，不是 `i`） |
| `\J` | `\mathbb{j}` | 虚数单位 j |

### 函数名

| 宏 | 展开结果 | 用途 |
|-----|---------|------|
| `\Re` | `\mathop{}\!\mathrm{Re}` | 实部 |
| `\Im` | `\mathop{}\!\mathrm{Im}` | 虚部 |
| `\Sa` | `\mathop{\mathrm{Sa}}\nolimits` | 抽样函数 |
| `\sinc` | `\mathop{\mathrm{sinc}}\nolimits` | sinc 函数 |
| `\sgn` | `\mathop{\mathrm{sgn}}\nolimits` | 符号函数 |
| `\tr` | `\mathop{\mathrm{tr}}\nolimits` | 迹 |
| `\const` | `\mathop{\mathrm{const}}\nolimits` | 常数标记 |
| `\rmu{x}` | `\mathop{}\!\mathrm{x}` | 单位 |

### 量子/狄拉克符号

| 宏 | 展开结果 | 用途 |
|-----|---------|------|
| `\bra{x}` | `\left\langle x \right\vert` | 左态矢 $\left\langle x \right\vert$ |
| `\ket{x}` | `\left\vert x \right\rangle` | 右态矢 $\left\vert x \right\rangle$ |
| `\braket{x}` | `\left\langle x \right\rangle` | 内积 $\left\langle x \right\rangle$ |

### 重定义的标准命令

`preamble.sty` 重定义了 `\frac`、`\dfrac`、`\tfrac`、`\binom` 以调整排版。在 Markdown 中这些命令正常写即可——MathJax 会使用 preamble.sty 的重定义版本。

---

## 需要改为原生语法的宏

以下宏**不在** `preamble.sty` 中定义，转换时必须展开为原生写法。

### 来自 AC tex 文件的宏

| tex 宏 | Markdown 应写成 | 说明 |
|--------|----------------|------|
| `\R` | `\mathbb{R}` | 实数集 |
| `\tp` | `^\mathrm{T}` | 转置，如 `\v{A}\tp` → `\v{A}^\mathrm{T}` |
| `\V{x}` | `\v{x}` | 三重复向量（罕见），直接改用 `\v{x}` |
| `\sumi` | `\sum\limits_{n=1}^{\infty}` | 带默认下标的求和 |
| `\sumi[k]` | `\sum\limits_{k=1}^{\infty}` | 带参数下标的求和 |
| `\rot` | `\mathop{\mathrm{rot}}` | 旋度（仅 AC tex 中局部定义） |

### 通用的非标准宏（在任何 tex 中都应展开）

| tex 宏 | Markdown 应写成 | 说明 |
|--------|----------------|------|
| `\Z` | `\mathbb{Z}` | 整数集 |
| `\N` | `\mathbb{N}` | 自然数集 |
| `\Q` | `\mathbb{Q}` | 有理数集 |
| `\C` | `\mathbb{C}` | 复数集 |
| `\F` | `\mathscr{F}` | Fourier 变换的花体 F |

---

## 排版命令 → Markdown 结构

以下宏是 LaTeX 排版指令，在 Markdown 中应转为对应的原生结构：

### 定理/定义环境 → Callout

| tex 宏 | Markdown 写法 |
|--------|--------------|
| `\de{标题}{内容}` | `> [!definition] 标题` 下方缩进写内容 |
| `\den{标题}{内容}` | `> [!definition] 标题`（同上） |
| `\dep{标签}{标题}{内容}` | `> [!definition] 标题`（忽略标签） |
| `\di{标题}{内容}` | `> [!theorem] 标题` |
| `\din{标题}{内容}` | `> [!theorem] 标题`（同上） |
| `\dip{标签}{标题}{内容}` | `> [!theorem] 标题`（忽略标签） |
| `\zhu{标题}{内容}` | `> [!note] 标题` |

> `\de` vs `\den`/`\dep`、`\di` vs `\din`/`\dip` 的区别仅在于是否有 label/page 参数，在 Markdown 中一律简化为 `> [!definition]` / `> [!theorem]`。

### 章节命令 → Markdown 标题

Markdown 中以二级标题起始，一级标题保留给文件名。

| tex 宏 | Markdown |
|--------|---------|
| `\section{标题}` | `## 标题` |
| `\subsection{标题}` | `### 标题` |
| `\subsubsection{标题}` | `#### 标题` |
| `\Section{标题}` | `## 标题`（AC 中带星号编号的节） |
| `\Subsection{标题}` | `### 标题`（同上） |
| `\Subsubsection{标题}` | `#### 标题`（同上） |

### 着色/字体命令 → 移除或纯文本

| tex 宏 | 处理方式 |
|--------|---------|
| `\tboba{...}` | 改为 `**...**`（粗体） |
| `\mboba{...}` | 改为 `**\boldsymbol{...}**` |
| `\tbome{...}` | 改为 `**...**` |
| `\mbome{...}` | 改为 `**\boldsymbol{...}**` |
| `\tboqi{...}` | 改为 `*...*`（斜体，表示注释） |
| `\mboqi{...}` | 改为 `*\boldsymbol{...}*` |
| `\colors{...}` | 直接移除颜色命令 |

### 排版间距 → 忽略

| tex 宏 | 处理方式 |
|--------|---------|
| `\hang` | 忽略，Markdown 中无需悬挂缩进 |
| `\adjline` | 忽略，公式间距由 MathJax 自动处理 |
| `\page{...}` | 忽略，页码引用不适用于 Markdown |
| `\cfrac` | 改为标准 `\frac`（或 `\dfrac`） |

### proof/solution 环境

`\begin{proofs}...\end{proofs}` / `\begin{solution}...\end{solution}` 保留为普通段落文字，或视需要改为 `> [!note] 证明` / `> [!tip] 解` 等 callout。
