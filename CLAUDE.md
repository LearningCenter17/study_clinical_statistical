# Clinical Statistics Knowledge Base

这是一个临床试验统计知识库。知识只存在 `wiki/` 下的 Markdown 卡片里（Single Source of Truth），
skill 只负责检索和引用，不复制知识内容。

## 目录约定

| 目录 | 前缀 | 放什么 |
|---|---|---|
| `wiki/concepts/` | `CON-` | 统计概念与方法（estimand、MMRM、KM、CMH…） |
| `wiki/gotchas/` | `GOT-` | 坑、易错点、实现差异（SAS vs R 结果不一致等） |
| `wiki/references/` | `REF-` | 指南与文献摘要（ICH E9(R1)、FDA guidance、论文） |
| `wiki/tlf-patterns/` | `TLF-` | 统计结果在 TLF 中的标准呈现方式 |
| `inbox/` | — | 待收录的原始材料；处理后移到 `inbox/archive/` |
| `templates/` | — | 卡片模板 |

## 学习大纲（`wiki/index.md` 按此分章）

1. 估计目标（Estimand）框架
2. 统计推断核心概念：p 值、置信区间、功效、I 类错误
3. 连续型终点：ANCOVA → MMRM
4. 二分类终点：CMH、logistic、率差置信区间
5. 生存分析：KM、log-rank、Cox
6. 缺失数据与敏感性分析
7. 多重性
8. 样本量与成组序贯设计

目录按卡片类型（CON/GOT/REF/TLF）分，索引按大纲章节分：新卡片放进对应章节，不属于任何一章的放"大纲外主题"。
一张卡片只列在一个章节下（主归属），跨章关系用 `related` 和正文链接表达。

## 卡片规则

- 文件名 = 卡片 ID，如 `CON-MMRM.md`；ID 全局唯一，用大写短横线。
- 必须有 YAML frontmatter：`id`, `title`, `categories`（即 tag）, `related`, `sources`, `status`, `updated`。
- `status`：`draft`（Claude 生成或未核对）/ `reviewed`（Li 已对照原始出处核对）。
  **Claude 永远不要自己把卡片改成 `reviewed`。**
- 卡片之间用标准 Markdown 相对链接，如 `[MMRM](../concepts/CON-MMRM.md)`，
  不要用 `[[wikilink]]`（Quarto 渲染不了）。
- 一个知识点只写在一张卡片里；其他卡片链接过去，不复述。
- 每次新增或删除卡片，同步更新 `wiki/index.md`。
- 统计结论要写出处（`sources` 指向 REF- 卡片或原文献）；不确定的内容明确写"待核实"。
- 语言：正文中文为主，术语保留英文原文（如 intercurrent event、treatment policy strategy）。

## 常用命令

- `/kb-ingest` 处理 inbox 中的新材料
- `/kb-lint` 检查断链、孤立卡片、缺失字段
- `quarto preview` 本地预览 wiki 网站；`quarto render` 生成到 `_site/`
