---
id: CON-sdtm-epoch
title: "SDTM 中的 EPOCH：研究阶段的含义、取值、推导来源与 Element / Arm / Visit 的区别（EPOCH in SDTM）"
categories: [cdisc, sdtm, adam, epoch, element, arm, visit, trial-design, ta, te, se, aperiod, aphase, ole]
related: [CON-cdisc-variable-naming, CON-reference-date-study-day]
sources: ["Claude 对话（inbox: Epoch.md）"]
status: draft
updated: 2026-11-20
---

> 出处待补：本卡内容来自 Claude 对话（inbox: Epoch.md），属 AI 生成内容，未引用原始文献。需对照 SDTMIG（试验设计域 TA / TE / SE、EPOCH 变量）与 CDISC 受控术语（EPOCH codelist）核实。
>
> 整理记录（2026-11-20）：材料末尾原写"你以前做软件开发，可能会想到……"，属对话中针对个人的说法，这里改为"做过软件开发的人可能会想到……"；加粗小标题改为二级标题。

## 一句话定义

**EPOCH** 是 SDTM 里的一个变量，记录某条数据（一个 AE、一次化验、一次生命体征测量等）**发生在研究设计的哪个大阶段**。

“Epoch” 本来是个普通英文词，意思是一个有明显特征的时期，比如"一个时代"。它来自希腊语 epokhē，原意是"停顿、固定的时间点"，后来引申为"从某个点开始的一段时期"。所以它本身就有"一个阶段"的意思。

## 常见取值

取值来自 CDISC 受控术语，常见的有：

| EPOCH | 中文 |
|---|---|
| `SCREENING` | 筛选期 |
| `RUN-IN` | 导入期 |
| `TREATMENT` | 治疗期 |
| `BLINDED TREATMENT` | 双盲治疗期 |
| `OPEN LABEL TREATMENT` | 开放标签治疗期 |
| `FOLLOW-UP` | 随访期 |
| `LONG-TERM FOLLOW-UP` | 长期随访期 |

比如一个研究是"筛选 → 12 周双盲 → 开放标签延长（OLE）→ 安全随访"，就有 4 个 epoch。

## 它从哪来

EPOCH 不是 CRF 上直接收集的，而是**根据日期推出来的**：
- **试验设计域**（TA、TE）先定义研究有哪几个 epoch、每个 epoch 包含什么单元（element）
- **SE 域**（Subject Elements）记录每个受试者实际进入、离开每个单元的日期
- 各观测域（AE、LB、VS 等）里每条记录的日期落在哪个时间段，EPOCH 就取哪个值

## 几个容易混的概念

| 概念 | 含义 | 例子 |
|---|---|---|
| Epoch | 研究设计的大阶段，所有组共用 | 双盲治疗期 |
| Element | 阶段里的具体单元，各组可以不同 | 药物 A 治疗 / 安慰剂治疗 |
| Arm | 一个受试者从头到尾走的路线（element 的组合） | 筛选 → 药物 A → 随访 |
| Visit | 具体的一次访视 | Week 4 |

## 到了 ADaM

EPOCH 是 SDTM 的变量，主要用于描述数据。ADaM 做分析时一般用自己的变量来划分时间段：`APERIOD` / `APHASE`，以及 ADSL 的 `TRxxSDT` / `TRxxEDT`。（这些变量名的拆解见 [CON-cdisc-variable-naming](CON-cdisc-variable-naming.md)。）比如判断一个 AE 属于双盲期还是 OLE，通常按 AE 开始日期和各期的首次 / 末次用药日期比较，规则看 SAP，不直接照搬 EPOCH。

做过软件开发的人可能会想到 Unix epoch（1970-01-01）或机器学习里的训练轮次。这里的 Epoch 和那两个都没关系，就是"研究的一个阶段"。

> 补充（Claude）：
>
> - SDTM 中受试者每条观测记录的 EPOCH，与 DM 中的参考日期（`RFSTDTC` 等）一样都是"时间轴"信息，但 EPOCH 按阶段划分，研究日按天计（见 [CON-reference-date-study-day](CON-reference-date-study-day.md)）。
> - 材料表中的 EPOCH 取值是否都在当前版本的 CDISC 受控术语中（如 `LONG-TERM FOLLOW-UP`），以及 EPOCH 在各观测域中是 expected 还是 permissible，待 Li 对照 SDTMIG 与 CT 核实。

## 相关卡片

- [CON-cdisc-variable-naming](CON-cdisc-variable-naming.md)：`PER` / `PHASE`、`TRxxSDT` 等变量名零件
- [CON-reference-date-study-day](CON-reference-date-study-day.md)：受试者时间轴上的参考日期与研究日

## 出处

- Claude 对话（inbox: Epoch.md；AI 生成，原始出处待补）
