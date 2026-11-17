# Clinical Statistics Knowledge Base

这是一个临床试验统计知识库。知识只存在 `wiki/` 下的 Markdown 卡片里（Single Source of Truth），
skill 只负责检索和引用，不复制知识内容。

## 卡片分类：前缀 = 类型，文件夹 = 主题

两个维度各管一件事：**文件名前缀表示卡片类型，所在文件夹表示内容主题**。

### 类型（前缀）

| 前缀 | 类型 | 判断标准 | 例子 |
|---|---|---|---|
| `CON-` | 概念 | 解释"是什么、为什么"，本身不是一个可以跑的分析 | CON-p-value、CON-estimand、CON-stratified-randomization |
| `MTH-` | 统计方法 | 能"跑"的分析：输入数据，输出估计值 / CI / P 值 | MTH-MMRM、MTH-CMH、MTH-t-test |
| `WF-` | 操作流程 | 按步骤做一件事的流程 | WF-sample-size-calc |
| `CODE-` | 代码 | R / SAS 实现及两者结果比对 | CODE-mmrm-r-vs-sas |
| `TLF-` | TLF 呈现 | 统计结果在 TLF 中的标准呈现方式 | |
| `GOT-` | 坑 | 易错点、实现差异（SAS vs R 结果不一致等） | GOT-ttest-student-vs-welch |
| `REF-` | 法规 / 文献 | 指南与文献摘要 | REF-ICH-E9R1 |

estimand 相关内容不单设前缀，按类型取前缀、放进 `estimand/` 文件夹（如 CON-treatment-policy）。

### 主题（文件夹）

| 目录 | 放什么 |
|---|---|
| `wiki/cards/estimand/` | ICH E9(R1)、estimand 属性、ICE 处理策略 |
| `wiki/cards/inference/` | 统计推断基础：H₀、P 值、CI、分布、自由度、I / II 类错误、检验选择 |
| `wiki/cards/methods/` | 各终点的分析方法；跨终点的总览卡直接放这一层 |
| `wiki/cards/methods/continuous/` | t 检验、ANCOVA、MMRM |
| `wiki/cards/methods/binary/` | 应答率、CMH、logistic、率差 CI |
| `wiki/cards/methods/ordinal/` | 有序分类数据、比例优势模型 |
| `wiki/cards/methods/tte/` | KM、log-rank、Cox、HR |
| `wiki/cards/missing-data/` | 缺失机制、MI、tipping point、敏感性分析 |
| `wiki/cards/design/` | 随机化、分层、样本量、非劣效、多重性、剂量递增 |
| `wiki/cards/regulatory/` | FDA / EMA / ICH guidance 要点（REF- 卡片） |
| `inbox/` | 待收录的原始材料；处理后移到 `inbox/archive/` |
| `templates/` | 卡片模板 |

- 计划中但还没有卡片的主题（`methods/count/`、`safety/`）等第一张卡出现时再建文件夹。
- 新建主题文件夹时，同步在 `hooks/card_meta.py` 的 `SECTIONS` 里加中文名和顺序，否则侧边栏显示英文名、排在最后。
- 一张卡片只放一个文件夹（主题主归属），与它在 index 中的章节可以不同。

## 学习大纲（`wiki/index.md` 按此分章）

1. 估计目标（Estimand）框架
2. 统计推断核心概念：p 值、置信区间、功效、I 类错误。index 中再分四节：
   2.1 推断基础与核心假设（H₀、自由度、第一 / 二类错误与 power）；
   2.2 核心统计量与分布族；
   2.3 检验方法的选择与计算；
   2.4 常见误区与结果解读（如 P 值的误解、单双侧辨析）
3. 连续型终点：ANCOVA → MMRM
4. 二分类终点：CMH、logistic、率差置信区间
5. 生存分析：KM、log-rank、Cox
6. 缺失数据与敏感性分析
7. 多重性
8. 样本量与成组序贯设计

文件夹按主题分（网站侧边栏），索引按大纲章节分（`wiki/index.md`）：新卡片放进对应章节，不属于任何一章的放"大纲外主题"。
一张卡片只列在一个章节下（主归属），跨章关系用 `related` 和正文链接表达。

## 卡片规则

- 文件名 = 卡片 ID，如 `MTH-MMRM.md`；ID 全局唯一，用大写前缀加短横线。
- 必须有 YAML frontmatter：`id`, `title`, `categories`（即 tag）, `related`, `sources`, `status`, `updated`。
- `status`：`draft`（Claude 生成或未核对）/ `reviewed`（Li 已对照原始出处核对）。
  **Claude 永远不要自己把卡片改成 `reviewed`。**
- 卡片之间用标准 Markdown 相对链接，如 `[MMRM](../methods/continuous/MTH-MMRM.md)`（路径相对于当前卡片所在文件夹），
  不要用 `[[wikilink]]`（Quarto 渲染不了）。
- 一个知识点只写在一张卡片里；其他卡片链接过去，不复述。
- 每次新增或删除卡片，同步更新 `wiki/index.md`。
- 统计结论要写出处（`sources` 指向 REF- 卡片或原文献）；不确定的内容明确写"待核实"。
- 语言：正文中文为主，术语保留英文原文（如 intercurrent event、treatment policy strategy）。

## 常用命令

- `/kb-ingest` 处理 inbox 中的新材料
- `/kb-lint` 检查断链、孤立卡片、缺失字段
- `C:\ProgramData\miniconda3\python.exe -m mkdocs serve` 本地预览 wiki 网站；`... -m mkdocs build` 生成到 `site/`（配置见 `mkdocs.yml`，`hooks/card_meta.py`）。
  链接锚点按 MkDocs 规则生成：保留中文、`₀` 等字符和标题开头的编号（如 `#5-mann-whitney-u-检验wilcoxon-秩和检验`）；build 无 WARNING 才算链接全部有效。
