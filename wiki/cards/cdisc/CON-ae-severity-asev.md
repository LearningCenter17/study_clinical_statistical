---
id: CON-ae-severity-asev
title: "AE 严重程度：AESEV 与 ASEV 的区别、ASEVN，以及 severity ≠ seriousness（AE Severity: AESEV vs ASEV）"
categories: [cdisc, sdtm, adam, adae, adverse-event, severity, aesev, asev, aeser, sae, ctcae, safety, tlf]
related: [CON-cdisc-variable-naming, CON-meddra-hierarchy, CON-ordinal-data, CON-ae-causality-arel, CON-sae-criteria, WF-pregnancy-reporting, CON-partial-date-imputation]
sources: ["Claude 对话（inbox: AESEV_ASEV.md）"]
status: draft
updated: 2026-11-20
---

> 出处待补：本卡内容来自 Claude 对话（inbox: AESEV_ASEV.md），属 AI 生成内容，未引用原始文献。需对照 SDTMIG AE 域、ADaM OCCDS（ADAE）规范、ICH E2A（SAE 定义）核实。
>
> 整理记录（2026-11-19）：材料原文"就是命名片段里那条规律"指更早对话中的变量命名整理，这里改为指向 CON-cdisc-variable-naming 的链接；另在 CTCAE、PT 两处加了指向相关卡片的链接。

## 一句话定义

`AESEV` 和 `ASEV` 两个变量记录的都是不良事件的**严重程度**（轻 / 中 / 重），区别在于来源：

| | `AESEV` | `ASEV` |
|---|---|---|
| 所在数据集 | SDTM **AE**（ADAE 里通常也会带过来） | ADaM **ADAE** |
| 英文 label | Severity/Intensity | Analysis Severity/Intensity |
| 含义 | **收集到的原始值**：研究者在 CRF 上填的 | **分析用的值**：按 SAP 规则处理过的，TLF 用这个 |
| 取值 | `MILD` / `MODERATE` / `SEVERE`（受控术语） | 通常同上 |

就是变量命名里那条规律（见 [CON-cdisc-variable-naming](CON-cdisc-variable-naming.md#四前缀)）：前缀 **A** 表示 Analysis（分析版本），`ASEV` 对 `AESEV`，跟 `AREL` 对 `AEREL`、`ASTDT` 对 `AESTDTC` 是一回事。

**ASEV 和 AESEV 什么时候不一样**

大部分记录两者相同，常见的不同情况有：
- **缺失填补**：研究者没填严重程度，SAP 常规定按最保守的情况处理，`ASEV` 填成 `SEVERE`（还会用一个标识变量记录这是填补的，具体名字看 spec）
- **从其他量表转换**：比如肿瘤研究按 CTCAE 分级（`AETOXGR`），SAP 可能规定把分级映射成轻 / 中 / 重（CTCAE 分级作为有序分类数据的例子见 [CON-ordinal-data](../methods/ordinal/CON-ordinal-data.md)）
- **数据清理后的修正**

还常配一个数值版本 **`ASEVN`**（1 = MILD，2 = MODERATE，3 = SEVERE），方便排序。做"按最严重程度汇总"的表时，每个受试者每个 PT 只取 `ASEVN` 最大的那条。（PT 见 [CON-meddra-hierarchy](CON-meddra-hierarchy.md)）

**一个常见混淆：severity ≠ seriousness**

- **`AESEV` / `ASEV`（severity）**：强度有多大，轻、中还是重
- **`AESER`（serious）**：是否属于**严重不良事件（SAE）**，这是监管上的定义，比如导致死亡、危及生命、需要住院或延长住院、导致残疾、先天畸形等

两者是独立的：一次重度头痛可以是 `SEVERE` 但不是 SAE；一次轻度的症状如果导致住院，就是 SAE。TLF 里这两类表是分开做的。

> 补充（Claude）：
>
> - SAE 的标准定义见 ICH E2A，材料列的几项（死亡、危及生命、住院或延长住院、残疾、先天畸形）之外还有"其他重要医学事件"一项。待 Li 核实。（这一点后来有了材料支持，六条标准及对应的 `AES*` 变量见 [CON-sae-criteria](CON-sae-criteria.md)。）
> - 缺失严重程度填成 `SEVERE` 时的填补标识，常见做法是 sponsor 自定义变量（如 `ASEVF`）或在 spec 中说明，ADaMIG 没有统一的标准变量名，以项目 spec / define.xml 为准。待 Li 核实。
> - `ASTDT` 是数值型日期，`AESTDTC` 是 ISO 8601 字符型，两者除了"分析版本"之外还有类型的转换（`DTC` → `DT`），见 [CON-cdisc-variable-naming](CON-cdisc-variable-naming.md#二时间相关零件)；不完整日期怎么填补成 `ASTDT` 见 [CON-partial-date-imputation](CON-partial-date-imputation.md)。

## 相关卡片

- [CON-cdisc-variable-naming](CON-cdisc-variable-naming.md)：前缀 A、SEV / SER 等变量名零件
- [CON-meddra-hierarchy](CON-meddra-hierarchy.md)：PT、SOC 与 AE 汇总表
- [CON-ordinal-data](../methods/ordinal/CON-ordinal-data.md)：CTCAE 分级作为有序分类数据
- [CON-ae-causality-arel](CON-ae-causality-arel.md)：同样"原始值 vs 分析值"的 `AEREL` / `AREL`
- [CON-sae-criteria](CON-sae-criteria.md)：SAE 的六条判定标准与 `AES*` 变量
- [WF-pregnancy-reporting](../safety/WF-pregnancy-reporting.md)：妊娠报告与随访
- [CON-partial-date-imputation](CON-partial-date-imputation.md)：日期的保守填补与 `ASTDTF`

## 出处

- Claude 对话（inbox: AESEV_ASEV.md；AI 生成，原始出处待补）
