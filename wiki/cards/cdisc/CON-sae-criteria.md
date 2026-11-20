---
id: CON-sae-criteria
title: "SAE 判定标准与 SDTM 变量：AESER 与 AESDTH / AESLIFE / AESHOSP / AESDISAB / AESCONG / AESMIE（SAE Criteria）"
categories: [cdisc, sdtm, adverse-event, sae, aeser, aescong, aesmie, ich-e2a, safety, congenital-anomaly, listing]
related: [CON-ae-severity-asev, CON-cdisc-variable-naming, WF-pregnancy-reporting]
sources: ["Claude 对话（inbox: congenital_anomaly.md）"]
status: draft
updated: 2026-11-20
---

> 出处待补：本卡内容来自 Claude 对话（inbox: congenital_anomaly.md），属 AI 生成内容，未引用原始文献。需对照 ICH E2A 与 SDTMIG AE 域核实。
>
> 整理记录（2026-11-20）：材料原文"前面说过 `AESER` 是'是否 SAE'"指更早的对话，这里改为链接；材料后半部分（妊娠报告与随访）放在 [WF-pregnancy-reporting](../safety/WF-pregnancy-reporting.md)。

## 一句话定义

Congenital Anomaly or Birth Defect 是 **SAE 的判定标准之一**，SDTM AE 域里对应的变量是 **`AESCONG`**。

**含义**

**Congenital Anomaly or Birth Defect**（先天异常或出生缺陷）：受试者在参加研究期间或之前接触了研究药物，后来生下的孩子有先天异常或出生缺陷。只要出现这种情况，这个不良事件就算严重不良事件（SAE）。

接触药物的可以是怀孕的女性受试者，也可以是男性受试者（伴侣怀孕），所以临床试验一般都有妊娠报告流程，受试者或其伴侣怀孕后要随访到分娩。（流程见 [WF-pregnancy-reporting](../safety/WF-pregnancy-reporting.md)）

**变量拆解**

`AESCONG` = AE + **S**（Serious）+ **CONG**（Congenital），取值 `Y` / `N`。

**它是一组 SAE 标准变量中的一个**

`AESER` 是"是否 SAE"（severity 与 seriousness 的区别见 [CON-ae-severity-asev](CON-ae-severity-asev.md)）。至于为什么是 SAE，SDTM 用一组 `AES*` 变量逐条记录，满足任何一条，`AESER` 就是 `Y`：

| 变量 | 英文 | 中文 |
|---|---|---|
| `AESDTH` | Results in Death | 导致死亡 |
| `AESLIFE` | Is Life Threatening | 危及生命 |
| `AESHOSP` | Requires or Prolongs Hospitalization | 需要住院或延长住院 |
| `AESDISAB` | Persist or Signif Disability/Incapacity | 导致持续或显著的残疾 / 功能丧失 |
| `AESCONG` | Congenital Anomaly or Birth Defect | 先天异常或出生缺陷 |
| `AESMIE` | Other Medically Important Serious Event | 其他重要医学事件 |

这几条来自 ICH E2A 对 SAE 的定义。`AESMIE` 是兜底条款：不满足前五条，但研究者从医学角度判断很重要（比如需要干预才能防止出现前面几种结果）。

**实际中**

`AESCONG = Y` 非常少见，大多数研究的 SAE 列表里这一列基本都是 `N`。但 CRF 上必须收集，SAE listing 里通常会把这几个标准都列出来，有的项目会合并成一列显示 SAE 原因。

> 补充（Claude）：SDTMIG AE 域另有 `AESCAN`（Involves Cancer）、`AESOD`（Occurred with Overdose）两个变量，它们不是 ICH E2A 的 SAE 标准，是部分 sponsor 沿用的历史收集项。`AESER = Y` 而所有 `AES*` 都是 `N`（或反过来）是常见的数据核查（edit check）问题。待 Li 核实。

## 相关卡片

- [CON-ae-severity-asev](CON-ae-severity-asev.md)：severity ≠ seriousness
- [CON-cdisc-variable-naming](CON-cdisc-variable-naming.md)：`S`、`FL` 等变量名零件
- [WF-pregnancy-reporting](../safety/WF-pregnancy-reporting.md)：妊娠报告与随访流程

## 出处

- Claude 对话（inbox: congenital_anomaly.md；AI 生成，原始出处待补）
