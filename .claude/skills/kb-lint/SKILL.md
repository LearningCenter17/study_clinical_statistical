---
name: kb-lint
description: Health check for the clinical statistics knowledge base. Use when the user runs /kb-lint or asks to check, audit or clean up the wiki cards.
---

# 知识库体检

只检查和报告，不自动修改。报告后询问 Li 要修哪些。

## 检查项

1. **断链**：卡片中的相对链接和 `related` 里的 ID 指向不存在的文件。
2. **孤立卡片**：没有被 `wiki/index.md` 收录，或没有任何其他卡片链接到它。
3. **字段缺失**：frontmatter 缺 `id`/`title`/`categories`/`status`/`updated`/`sources`，
   或 `id` 与文件名不一致。
4. **单向 related**：A 列了 B，B 没列 A。
5. **无出处**：`sources` 为空，或正文仍有"出处待补"。
6. **长期 draft**：`status: draft` 且 `updated` 早于 90 天前。
7. **疑似重复**：标题或主题高度相似的卡片。
8. **未处理分歧**：正文含"⚠ 存在分歧"。

## 输出

按检查项分组列表，每条给出文件路径和具体问题。最后给一个总数统计。
