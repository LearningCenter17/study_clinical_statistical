---
id: CON-partial-date-imputation
title: "不完整日期的填补：AESTDTC → ASTDT / ASTDTF、填补标识取值与保守原则（Partial Date Imputation）"
categories: [cdisc, sdtm, adam, adae, partial-date, date-imputation, astdt, astdtf, aestdtc, iso-8601, teae, sap]
related: [CON-cdisc-variable-naming, CON-reference-date-study-day, CON-ae-severity-asev, CON-ae-causality-arel]
sources: ["Claude 对话（inbox: Analysis_Start_Date.md）"]
status: draft
updated: 2026-11-20
---

> 出处待补：本卡内容来自 Claude 对话（inbox: Analysis_Start_Date.md），属 AI 生成内容，未引用原始文献。需对照 ADaMIG（*DTF / *TMF 变量及受控术语）、ADaM OCCDS 与具体 SAP 核实。
>
> 整理记录（2026-11-20）：材料开头三行"变量名 + label"并进了下面这句定义；加粗小标题改为二级标题；加了指向变量命名、研究日卡片的链接。

## 一句话定义

`AESTDTC`（Start Date/Time of Adverse Event）、`ASTDT`（Analysis Start Date）、`ASTDTF`（Analysis Start Date Imputation Flag）这三个变量是同一个日期（AE 开始日期）在不同阶段的样子：**原始记录 → 分析用日期 → 填补标识**。

| 变量 | 所在 | 类型 | 含义 |
|---|---|---|---|
| `AESTDTC` | SDTM AE | 字符型（ISO 8601） | 收集到的 AE 开始日期，**可以不完整** |
| `ASTDT` | ADaM ADAE | 数值型 SAS 日期 | 分析用的开始日期，不完整时按 SAP **填补**成完整日期 |
| `ASTDTF` | ADaM ADAE | 字符型 | 记录 `ASTDT` 是否经过填补、填补了哪部分 |

拆开看：`AESTDTC` = AE + ST + DTC；`ASTDT` = A + ST + DT；`ASTDTF` = A + ST + DT + F（Flag）。（变量名零件见 [CON-cdisc-variable-naming](CON-cdisc-variable-naming.md#二时间相关零件)。）

## 为什么要这样分

受试者常常记不清 AE 哪天开始，CRF 上可能只填了年月，甚至只有年份。SDTM 照实记录，所以 `AESTDTC` 可能是：
- `2026-03-15`（完整）
- `2026-03`（缺日）
- `2026`（缺月和日）

但分析时需要一个完整日期才能判断它是不是 TEAE、算研究日（研究日见 [CON-reference-date-study-day](CON-reference-date-study-day.md)）。ADaM 就按 SAP 规则补全，存到 `ASTDT`，再用 `ASTDTF` 标明补了什么。

## ASTDTF 的取值（ADaM 受控术语）

| 值 | 含义 |
|---|---|
| 空 | 没有填补，原始日期完整 |
| `D` | 填补了日 |
| `M` | 填补了月和日 |
| `Y` | 填补了年、月和日 |

## 例子

假设受试者首次用药日 `TRTSDT` = 2026-03-10，SAP 的填补规则是"缺日补 1 号，缺月补 1 月 1 日；但如果和首次用药在同一年同一月，补成首次用药日"：

| AESTDTC | ASTDT | ASTDTF | 说明 |
|---|---|---|---|
| `2026-03-15` | 2026-03-15 | （空） | 完整，不填补 |
| `2026-02` | 2026-02-01 | `D` | 缺日，补 1 号 |
| `2026-03` | 2026-03-10 | `D` | 缺日，和首次用药同月，补成用药日 |
| `2026` | 2026-03-10 | `M` | 缺月日，和首次用药同年，补成用药日 |

后两行就是常见的**保守原则**：如果不能排除 AE 发生在用药之后，就把它当作用药后发生，算进 TEAE。直接补成 3 月 1 日的话，它会落在用药前，可能被漏掉。

## 注意
- 填补规则每个研究不同，一定按 SAP 来。结束日期（`AENDT` / `AENDTF`）的规则往往相反，一般补成最晚的可能日期。
- 时间部分也一样：`ASTDTM` 是日期时间，`ASTTMF` 是时间的填补标识。
- 列表（listing）里通常显示原始的 `AESTDTC`，或者在填补过的日期旁加标记，让读者知道哪些是填补的。

> 数值复核（Claude）：按材料给的规则逐行核对，四行结果一致。`2026-02` 本来就早于首次用药月，补 1 号即可；`2026-03`、`2026` 两行因可能发生在用药后，补成 `TRTSDT`。
>
> 补充（Claude）：
>
> - 时间填补标识 `ASTTMF` 的取值是 `H` / `M` / `S`（填补了时、分、秒），与日期的 `Y` / `M` / `D` 是两套。待 Li 核实。
> - SAP 里通常还有一条：填补后的开始日期不能晚于（已知的）结束日期，否则改用结束日期。
> - "保守原则"服务于 TEAE 判定；同样"宁可算进去"的思路也出现在 `ASEV` 缺失填成 `SEVERE`（[CON-ae-severity-asev](CON-ae-severity-asev.md)）、`AREL` 缺失填成 `RELATED`（[CON-ae-causality-arel](CON-ae-causality-arel.md)）。

## 相关卡片

- [CON-cdisc-variable-naming](CON-cdisc-variable-naming.md)：`ST`、`DTC` / `DT`、`DTF` 等变量名零件
- [CON-reference-date-study-day](CON-reference-date-study-day.md)：研究日的计算
- [CON-ae-severity-asev](CON-ae-severity-asev.md)：缺失严重程度的保守填补
- [CON-ae-causality-arel](CON-ae-causality-arel.md)：缺失因果关系的保守填补

## 出处

- Claude 对话（inbox: Analysis_Start_Date.md；AI 生成，原始出处待补）
