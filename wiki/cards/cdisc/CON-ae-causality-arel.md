---
id: CON-ae-causality-arel
title: "AE 因果关系：AEREL 与 AREL、常见取值与归并、药物相关 TEAE 表（AE Causality: AEREL vs AREL）"
categories: [cdisc, sdtm, adam, adae, adverse-event, causality, aerel, arel, aerelnst, teae, adr, safety, tlf]
related: [CON-ae-severity-asev, CON-cdisc-variable-naming, CON-meddra-hierarchy]
sources: ["Claude 对话（inbox: AEREL.md）"]
status: draft
updated: 2026-11-20
---

> 出处待补：本卡内容来自 Claude 对话（inbox: AEREL.md），属 AI 生成内容，未引用原始文献。需对照 SDTMIG AE 域、ADaM OCCDS（ADAE）规范、ICH E2A 核实。
>
> 整理记录（2026-11-20）：材料后半部分"`REL` 不是 Reference"及 REL / RF / REAS / RES 对照表属于变量命名规律，放进了 [CON-cdisc-variable-naming](CON-cdisc-variable-naming.md#八容易混淆的片段rel--rf--reas--res)；另在 `ASEV`、SOC / PT 两处加了指向相关卡片的链接。

## 一句话定义

`AEREL` 是 SDTM AE 域里的 **Causality**（因果关系）变量，记录**研究者判断**这个不良事件和研究药物有没有关系。

AEREL = AE + REL（Relationship），意思是"AE 与研究药物的关系"
它的 label 写作 Causality（因果关系），因为这里说的"关系"具体就是"是不是这个药引起的"。变量名用缩写 REL，label 用了更准确的说法，两者说的是同一件事。

**常见取值**

具体分几级由 sponsor 在 CRF 上定义（CDISC 没有强制的受控术语），常见的有两种：

| 五级（常见） | 二级 |
|---|---|
| NOT RELATED（无关） | NOT RELATED |
| UNLIKELY RELATED（可能无关） | NOT RELATED |
| POSSIBLY RELATED（可能有关） | RELATED |
| PROBABLY RELATED（很可能有关） | RELATED |
| RELATED / DEFINITELY RELATED（肯定有关） | RELATED |

**和 AREL 的关系**

跟 `AESEV` / `ASEV` 一样（见 [CON-ae-severity-asev](CON-ae-severity-asev.md)），前缀 A 表示分析版本：
- `AEREL`：研究者在 CRF 上填的原始判断
- `AREL`（Analysis Causality，ADAE）：按 SAP 规则处理后的值，TLF 用这个

常见的处理有两种：
- **归并成两类**：按 SAP 把多级合并成"相关 / 不相关"，上表右列就是常见的合并方式。像 UNLIKELY RELATED 归到哪边，各项目规定不同，一定要看 SAP。
- **缺失填补**：研究者没填时，通常按最保守的情况处理，填成 `RELATED`。

**在 TLF 里的用途**

最常见的是**药物相关的 TEAE** 汇总表（treatment-related TEAE，也叫 adverse drug reaction 表）：在 TEAE 里筛出 `AREL` 为相关的记录，再按 SOC / PT 汇总（见 [CON-meddra-hierarchy](CON-meddra-hierarchy.md#在-tlf-里怎么用)）。药物相关的 SAE、导致停药的药物相关 AE 等表也用它筛选。

**相关变量**
- `AERELNST`（Relationship to Non-Study Treatment）：和**非研究药物**（比如合并用药、背景治疗）的关系
- 研究有多种研究药物（比如联合用药）时，每种药的相关性通常放在 SUPPAE 里分别记录，变量名看项目 spec

还有一点：`AEREL` 是研究者的临床判断，不是统计结论。监管机构评估药物安全性时，会同时看所有 AE 的组间比较，不只看研究者判断为相关的那部分。

> 补充（Claude）：
>
> - ICH E2A 对上市前的药物不良反应（ADR）的定义是：与药物的因果关系"至少有合理的可能性"（reasonable possibility）。这正是 POSSIBLY RELATED 通常被归为"相关"的依据。待 Li 核实。
> - TEAE（treatment-emergent adverse event）的判定规则（首次用药后发生或加重，以及用药后多少天内算）由 SAP 定义，ADAE 中通常用 `TRTEMFL` 标识。本库尚无 TEAE 专门卡片。待 Li 核实。

## 相关卡片

- [CON-ae-severity-asev](CON-ae-severity-asev.md)：同样是"原始值 vs 分析值"的 `AESEV` / `ASEV`
- [CON-cdisc-variable-naming](CON-cdisc-variable-naming.md)：REL、RF 等变量名零件
- [CON-meddra-hierarchy](CON-meddra-hierarchy.md)：SOC / PT 汇总

## 出处

- Claude 对话（inbox: AEREL.md；AI 生成，原始出处待补）
