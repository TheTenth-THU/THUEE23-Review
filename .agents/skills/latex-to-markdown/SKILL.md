---
name: latex-to-markdown
description: Use when converting .tex LaTeX source files into Obsidian Markdown files. Covers the full conversion workflow: splitting by sections, creating Index.md, converting formulas, mapping theorem environments to callouts, replacing includegraphics with wikilinks, and converting tikz content. Load latex-macros skill alongside for the macro lookup table.
---

# LaTeX → Markdown 转换规范

此文件记录从 `.tex` 源文件向 Obsidian Markdown 转换时的操作流程和排版规则。单个宏的处理速查见 `latex-macros` skill。

## 转换步骤

对于一门新课程，在正文转换前应先完成：

1. **拆分章节**：按 `\section`、`\subsection` 边界将 `.tex` 拆分为多个 `.md` 文件
2. **建立索引**：创建 `Index.md`（含 frontmatter + 课程信息）

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

- 每个 `\section` 为一个独立 `.md` 文件
- 较大 `\section`（内容超过 ~500 行）可进一步按 `\subsection` 拆分
- 文件名去除 LaTeX 宏，使用中英文混合的可读标题
