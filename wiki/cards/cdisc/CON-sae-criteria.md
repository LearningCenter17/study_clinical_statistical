---
id: CON-sae-criteria
title: "SAE 判定标准与 SDTM 变量：AESER 与 AESDTH / AESLIFE / AESHOSP / AESDISAB / AESCONG / AESMIE，及残疾、重要医学事件的判断（SAE Criteria）"
categories: [cdisc, sdtm, adverse-event, sae, aeser, aescong, aesmie, aesdisab, ich-e2a, safety, congenital-anomaly, disability, ime-list, hys-law, aesi, listing]
related: [CON-ae-severity-asev, CON-cdisc-variable-naming, WF-pregnancy-reporting, CON-meddra-hierarchy]
sources: ["Claude 对话（inbox: congenital_anomaly.md）", "Claude 对话（inbox: Disability_incapacity.md）", "Claude 对话（inbox: Medically_Important.md）"]
status: draft
updated: 2026-11-20
---

> 出处待补：本卡内容来自 Claude 对话（inbox: congenital_anomaly.md；"逐条标准详解"来自 Disability_incapacity.md、Medically_Important.md），属 AI 生成内容，未引用原始文献。需对照 ICH E2A、21 CFR 312.32、EMA IME 列表与 SDTMIG AE 域核实。
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

## 逐条标准详解

> 以下两小节分别来自 Claude 对话（inbox: Disability_incapacity.md、Medically_Important.md），AI 生成，出处待补。`AESCONG` 见上文。
>
> 整理记录（2026-11-20）：两份材料中的加粗小标题改为四级标题；Medically_Important.md 末句"到这里六条标准就全了……满足任何一条，`AESER` 就是 `Y`"与本卡上方的表格重复，未再写入。

### AESDISAB：持续或显著的残疾 / 功能丧失

这是 SAE 判定标准里的一条，对应变量 **`AESDISAB`**。

#### 完整说法

Persistent or Significant Disability/Incapacity：**导致持续的或显著的残疾 / 功能丧失**。label 里的 "Signif" 是 Significant 的缩写，因为 SDTM 的 label 最多 40 个字符，写全放不下。

#### 怎么理解

FDA 的定义（21 CFR 312.32）是：事件对受试者**进行正常日常生活的能力造成实质性破坏**（substantial disruption of a person's ability to conduct normal life functions）。

两个词的区别：
- **Persistent（持续的）**：影响长期存在，甚至永久
- **Significant（显著的）**：影响很大，即使最终能恢复

满足其中一个就算。

#### 例子

| 算 SAE（AESDISAB = Y） | 不算 |
|---|---|
| 脑卒中后偏瘫 | 头痛、流感，休息几天就好 |
| 永久性听力或视力丧失 | 踝关节扭伤，短时间行动不便 |
| 严重周围神经病变，影响行走或手部功能 | 轻度皮疹 |

关键在于**对正常生活能力的影响程度和持续时间**，不是事件本身听起来严不严重。一次重度但很快恢复的事件，`AESEV` 可以是 `SEVERE`，但不一定满足这条标准。（severity 与 seriousness 的区别见 [CON-ae-severity-asev](CON-ae-severity-asev.md)。）

#### 变量拆解

`AESDISAB` = AE + **S**（Serious）+ **DISAB**（Disability），取值 `Y` / `N`。

和前面的 `AESCONG` 一样，这一条在实际数据里也比较少见。SAE 最常见的原因通常是 `AESHOSP`（需要住院或延长住院）。

### AESMIE：其他重要医学事件

这是 SAE 判定标准的最后一条，对应变量 **`AESMIE`**，是一条**兜底条款**。

#### 含义

Other Medically Important Serious Event：**其他具有重要医学意义的严重事件**。事件不满足前面五条（死亡、危及生命、住院、残疾、先天异常），但研究者根据**医学判断**认为它很重要，于是也按 SAE 处理。

ICH E2A 的说法大意是：这类事件可能不会马上危及生命或导致住院，但可能危害受试者，或者**需要医疗干预才能防止**出现前面几种严重后果。

#### ICH E2A / FDA 给的经典例子
- 因过敏性支气管痉挛在急诊室或家中接受强化治疗（没有住院）
- 没有导致住院的血液系统异常（如粒细胞缺乏）或惊厥发作
- 出现药物依赖或药物滥用

这几个例子的共同点：如果没及时处理，很可能发展成危及生命或需要住院的情况。

#### 实际中怎么判断

因为靠的是研究者的判断，不同人可能结论不同。为了统一，有两个常用工具：
- **EMA 的 IME 列表**（Important Medical Event Terms List）：EMA 按 MedDRA PT 整理的一份"重要医学事件"清单，很多 sponsor 拿来作参考
- **方案里事先规定**：有的方案会指定某些事件一律按 SAE 报告，比如符合 Hy's Law 的肝功能异常（转氨酶升高合并胆红素升高）、某些特别关注的不良事件（AESI），具体看方案

#### 变量拆解

`AESMIE` = AE + **S**（Serious）+ **MIE**（Medically Important Event），取值 `Y` / `N`。

> 补充（Claude）：ICH E2A 原文对这一条的表述是"important medical events that may not be immediately life-threatening or result in death or hospitalisation but may jeopardise the patient or may require intervention to prevent one of the other outcomes"，材料的"大意"与此一致。Hy's Law 指 ALT 或 AST > 3 × ULN 且总胆红素 > 2 × ULN、并排除其他原因，是 FDA 药物性肝损伤指南中的概念。待 Li 核实。

## 相关卡片

- [CON-ae-severity-asev](CON-ae-severity-asev.md)：severity ≠ seriousness
- [CON-cdisc-variable-naming](CON-cdisc-variable-naming.md)：`S`、`FL` 等变量名零件
- [WF-pregnancy-reporting](../safety/WF-pregnancy-reporting.md)：妊娠报告与随访流程
- [CON-meddra-hierarchy](CON-meddra-hierarchy.md)：IME 列表按 MedDRA PT 整理

## 出处

- Claude 对话（inbox: congenital_anomaly.md；AI 生成，原始出处待补）
- Claude 对话（inbox: Disability_incapacity.md；AI 生成，原始出处待补）
- Claude 对话（inbox: Medically_Important.md；AI 生成，原始出处待补）
