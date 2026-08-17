---
name: latex-to-markdown
description: Use when converting .tex LaTeX source files into Obsidian Markdown files. Handles formulas, theorem environments, includegraphics, TikZ, headings and Markdown assets; load latex-macros alongside for macro lookup. This skill performs source-syntax conversion rather than deciding the final knowledge architecture. When the goal is formal course notes, knowledge extraction, chapter reorganization, splitting, merging or content-quality review, also load organize-course-knowledge and follow its knowledge map for file boundaries and content selection.
---

# LaTeX → Markdown 转换规范

此文件记录从 `.tex` 源文件向 Obsidian Markdown 转换时的语法和资源处理流程。单个宏的处理速查见 `latex-macros` skill；知识提取、分节和正文组织见 `organize-course-knowledge` skill。

## 协作边界

+ 仅做等结构语法转换时，按源文件顺序转换，并明确未执行内容重构。
+ 整理正式课程笔记时，先使用 `organize-course-knowledge` 盘点来源、建立知识地图并确定文件职责，再用本 skill 转换对应知识单元。
+ 不要因为源文件使用 `\section`、定理环境或颜色强调，就自动认定其应成为独立章节、Callout 或核心内容。
+ 转换完成后交回 `organize-course-knowledge` 回修 Index、父章节、交叉链接和内容覆盖。

## 转换步骤

对于一门正式整理的新课程，在正文转换前应先完成：

1. **设计知识结构**：使用 `organize-course-knowledge` 判断概念依赖、章节职责和父子层级。
2. **建立索引框架**：创建仅包含 Longform frontmatter、知识地图和导航的 `Index.md`。
3. **映射源内容**：把 `.tex` 的 section、定理、证明、例题、图片和 TikZ 映射到拟议知识单元；记录缺失资源和无法确认的局部宏。

对于每个章节文件：

1. **转换公式**：LaTeX 公式语法基本保留，但需处理自定义宏（详见 `latex-macros` skill）
2. **定理环境**：`\begin{theorem}...\end{theorem}` 等转为 callout 语法 `> [!theorem]`，示例或例题使用 `> [!example]+`。例如：

```markdown
> [!example]+ XXX的应用：示例
> 考虑 ... ，求解 ...
>
> ---
>
> 要求解 ... ，需 ...
```

若例题太长或不重要，可使用 `> [!example]-`。

3. **处理图片**：用 `![[图片名.png]]` 替换 `\includegraphics`，图片文件放在 `res/` 目录下，若源文件中引用的图片未提供请在转换完成后告知需要补充
4. **tikz 内容**：使用 Obsidian 插件支持的 `tikz` 块格式，需注意块内应该是单独 LaTeX 文件的内容，且不应包含 Obsidian 不支持的宏包（如 `nicematrix`、`tcolorbox` 等）。例如：

````markdown
```tikz
\usepackage{circuitikz}

\begin{document}
\large
\begin{tikzpicture}
	% \draw ...
\end{tikzpicture}
\end{document}
```
````

`.tex` 的 PDF 编译结果放在课程目录下作为人工审查参考。

## 拆分粒度

+ 把 `\section` 和 `\subsection` 视为候选边界，不要视为最终文件边界。
+ 仅做等结构语法转换时，可默认每个 `\section` 对应一个 `.md` 文件。
+ 整理正式课程笔记时，依据同级 skill 的 `../organize-course-knowledge/references/splitting-heuristics.md` 判断拆分、合并和父章节；内容超过约 500 行只能触发复核，不能单独决定拆分。
+ 移动完整知识单元，不要按固定行数切割推导、证明或例题。
+ 文件名去除 LaTeX 宏，使用中英文混合的可读知识主题。
