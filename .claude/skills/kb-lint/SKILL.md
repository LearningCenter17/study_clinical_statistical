---
name: kb-lint
description: Health check for the clinical statistics knowledge base. Use when the user runs /kb-lint or asks to check, audit or clean up the wiki cards.
---

# 知识库体检

只检查和报告，不自动修改。报告后询问 Li 要修哪些。

## 检查项

1. **断链与失效锚点**：卡片中的相对链接和 `related` 里的 ID 指向不存在的文件；链接里的 `#锚点` 在目标卡片中不存在。
   用 `C:\ProgramData\miniconda3\python.exe -m mkdocs build --strict` 检查（设环境变量 `NO_MKDOCS_2_WARNING=1` 去掉无关提示），
   输出中的每条 WARNING 都算一个问题。GitHub 发布也用 `--strict`，有 WARNING 时网站不会更新。
2. **孤立卡片**：没有被 `wiki/index.md` 收录，或没有任何其他卡片链接到它。
3. **字段缺失**：frontmatter 缺 `id`/`title`/`categories`/`status`/`updated`/`sources`，
   或 `id` 与文件名不一致。
4. **单向 related**：A 列了 B，B 没列 A。
5. **无出处**：`sources` 为空，或正文仍有"出处待补"。
6. **长期 draft**：`status: draft` 且 `updated` 早于 90 天前。
7. **疑似重复**：标题或主题高度相似的卡片。
8. **未处理分歧**：正文含"⚠ 存在分歧"。
9. **类型与位置**：
   - 文件名前缀不在 `CON- / MTH- / WF- / CODE- / TLF- / GOT- / REF-` 之内；
   - 卡片不在 `wiki/cards/<主题>/` 下；
   - 所在主题文件夹没有登记在 `hooks/card_meta.py` 的 `SECTIONS` 里（侧边栏会显示英文名、排在最后）；
   - 类型明显不符（如能直接跑出估计值 / P 值的方法却是 `CON-`），只提示，不自动判定。
10. **卡片过长**：正文超过约 200 行，或包含两个以上可以独立引用的知识点。列出行数和建议的拆分方式，由 Li 决定是否拆。
11. **重复内容**：同一张表格、同一组数值或同一段解释出现在两张以上卡片中（违反"一个知识点只写在一张卡片里"）。
    列出各处位置，建议哪张作为主卡。

## 输出

按检查项分组列表，每条给出文件路径和具体问题。最后给一个总数统计。
