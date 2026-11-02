---
name: kb-ingest
description: Process raw material in inbox/ into knowledge base cards. Use when the user runs /kb-ingest, says 收录, 入库, ingest, or has dropped notes, guidance excerpts, PDFs or chat snippets into inbox/.
---

# 知识收录

把 `inbox/` 下的原始材料整理成 `wiki/` 卡片。先读项目根目录的 `CLAUDE.md` 了解规则。

## 步骤

1. **盘点**：列出 `inbox/` 下所有文件（忽略 `inbox/archive/`）。没有文件就告诉用户并结束。
2. **拆分知识点**：逐个文件读，拆成独立知识点。一个知识点 = 一张卡片能讲清楚的内容。
   判断归类：概念/方法 → `CON-`；坑/易错点 → `GOT-`；指南/文献 → `REF-`；TLF 呈现 → `TLF-`。
3. **查重**：每个知识点先在 `wiki/` 里 grep 关键词和同义词（中英文都查）。
   - 已有卡片 → **合并**进现有卡片的对应小节，不新建；更新 `updated` 日期。
   - 没有 → 用 `templates/card-template.md` 新建。
4. **写卡片**：
   - `status` 一律 `draft`。
   - `sources` 写材料的真实出处；材料里没写出处就写 `inbox: <原文件名>`，并在正文标"出处待补"。
   - 只写材料支持的内容。你自己补充的背景知识用 `> 补充（Claude）：` 引用块标出。
   - 补全 `related`，并在对方卡片的 `related` 里加回链。
5. **更新索引**：在 `wiki/index.md` 对应分类下加入新卡片，一行一个：`- [ID](相对路径) — 一句话`。
6. **归档**：把处理完的源文件移到 `inbox/archive/`，文件名前加日期 `YYYYMMDD_`。
7. **汇报**：列出新建了哪些卡片、合并进了哪些卡片、有哪些内容不确定需要 Li 核对。

## 注意

- 材料之间、材料与现有卡片之间有矛盾时，不要自行裁决：两种说法都写进卡片，标"⚠ 存在分歧"并在汇报中列出。
- 不要把卡片改成 `reviewed`。
