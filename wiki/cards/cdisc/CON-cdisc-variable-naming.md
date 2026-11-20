---
id: CON-cdisc-variable-naming
title: "ADaM / SDTM 变量命名规则：把变量名拆成零件（CDISC Variable Naming Conventions）"
categories: [cdisc, adam, sdtm, variable-naming, adsl, adae, adlb, adtte, bds, define-xml, statistical-programming]
related: [CON-survival-analysis-overview, CON-censoring, CON-reference-date-study-day, CON-meddra-hierarchy, CON-ae-severity-asev, CON-ae-causality-arel, CON-sae-criteria]
sources: ["Claude 对话（inbox: CDISC_1.md）", "Claude 对话（inbox: AEREL.md）"]
status: draft
updated: 2026-11-20
---

> 出处待补：本卡内容来自 Claude 对话（inbox: CDISC_1.md），属 AI 生成内容，未引用原始文献。需对照 CDISC SDTMIG、ADaMIG（含 ADaM OCCDS、ADTTE 规范）核实；具体项目以 define.xml 为准。

## 一句话定义

下面把变量名拆成"零件"，分类整理。大多数 ADaM / SDTM 变量都是这些零件拼起来的。

> 整理记录（2026-11-19）：材料末尾原写"比如之前说的 `SAF1FL`、`STRATAR`"，"之前说的"指更早一段对话，这里去掉了。ADTTE 变量（CNSR、ADT、EVNTDESC、CNSDTDSC）在生存分析里的用法见 [CON-censoring](../methods/tte/CON-censoring.md#在-adtte-里怎么体现) 和 [CON-survival-analysis-overview](../methods/tte/CON-survival-analysis-overview.md#6-落到临床编程上)。

## 一、主体词根（变量讲的是什么）

| 零件 | 英文 | 中文 | 例子 |
|---|---|---|---|
| `TRT` | Treatment | 治疗 | `TRT01P`、`TRTSDT` |
| `TR` | Treatment（带期号时的缩短写法） | 治疗 | `TR01SDT` |
| `AE` | Adverse Event | 不良事件 | `AESER`、`AEDECOD` |
| `PARAM` | Parameter | 分析参数 | `PARAM`、`PARAMCD` |
| `VAL` | Value | 值 | `AVAL` |
| `BASE` / `BL` | Baseline | 基线 | `BASE`、`ABLFL` |
| `CHG` | Change | 变化 | `CHG`、`PCHG` |
| `VISIT` | Visit | 访视 | `AVISIT` |
| `RAND` | Randomization | 随机化 | `RANDDT`、`RANDFL` |
| `DTH` | Death | 死亡 | `DTHFL`、`DTHDT` |
| `EOS` / `EOT` | End of Study / End of Treatment | 研究结束 / 治疗结束 | `EOSSTT`、`EOTSTT` |
| `DCS` / `DCT` | Discontinued from Study / Treatment | 退出研究 / 停止治疗 | `DCSREAS`、`DCTREAS` |
| `STT` | Status | 状态 | `EOSSTT` |
| `REAS` | Reason | 原因 | `DCSREAS` |
| `REASND` | Reason Not Done | 未做原因 | `LBREASND` |
| `SEV` | Severity | 严重程度 | `AESEV`、`ASEV` |
| `SER` | Serious | 严重（SAE 意义上的） | `AESER` |
| `REL` | Relationship / Causality | 相关性 | `AEREL` |
| `TOXGR` | Toxicity Grade | 毒性分级 | `ATOXGR` |
| `ACN` | Action | 采取的措施 | `AEACN` |
| `OUT` | Outcome | 转归 | `AEOUT` |
| `DECOD` | Decoded / Dictionary-Derived Term | 字典编码术语 | `AEDECOD` |
| `TERM` | Reported Term | 原始报告术语 | `AETERM` |
| `BODSYS` | Body System | 系统器官分类 | `AEBODSYS` |
| `NR` | Normal Range | 正常值范围 | `ANRIND`、`ANRLO` |
| `IND` | Indicator | 指示（判定结果） | `ANRIND` |
| `LO` / `HI` | Low / High | 下限 / 上限 | `ANRLO`、`ANRHI` |
| `CRIT` | Criterion | 分析标准 | `CRIT1`、`CRIT1FL` |
| `SHIFT` | Shift | 转换（基线到访视的变化类别） | `SHIFT1` |
| `DUR` | Duration | 持续时间 | `TRTDURD`、`ADURN` |
| `PER` / `PERIOD` | Period | 研究期 | `APERIOD` |
| `PHASE` | Phase | 阶段 | `APHASE` |
| `ONTRT` | On Treatment | 治疗期内 | `ONTRTFL` |
| `PRE` / `FUP` | Pre-treatment / Follow-up | 治疗前 / 随访期 | `PREFL`、`FUPFL` |
| `OCC` | Occurrence | 发生（首次出现） | `AOCCFL`、`AOCCPFL` |
| `SEQ` | Sequence Number | 序号 | `AESEQ`、`ASEQ` |
| `SRC` | Source | 来源 | `SRCDOM`、`SRCVAR`、`SRCSEQ` |
| `LSTALV` | Last Known Alive | 最后已知存活 | `LSTALVDT` |
| `CNSR` | Censor | 删失 | `CNSR`（ADTTE） |
| `EVNT` | Event | 事件 | `EVNTDESC` |

## 二、时间相关零件

| 零件 | 英文 | 中文 | 例子 |
|---|---|---|---|
| `S` / `ST` | Start | 开始 | `TRTSDT`、`ASTDT` |
| `E` / `EN` | End | 结束 | `TRTEDT`、`AENDT` |
| `DT` | Date | 日期（数值型） | `ADT`、`RANDDT` |
| `TM` | Time | 时间（数值型） | `ATM` |
| `DTM` | Datetime | 日期时间（数值型） | `ADTM`、`TRTSDTM` |
| `DTC` | Date/Time in Character (ISO 8601) | 字符型日期时间（SDTM 用） | `AESTDTC`、`RFSTDTC` |
| `DY` | Day | 研究日 | `ADY`、`AESTDY` |
| `DTF` | Date Imputation Flag | 日期填补标识 | `ASTDTF` |
| `TMF` | Time Imputation Flag | 时间填补标识 | `ASTTMF` |
| `TPT` | Time Point | 时间点 | `ATPT`、`LBTPT` |
| `D` / `M` / `Y` | Days / Months / Years | 以天 / 月 / 年计 | `TRTDURD` |

## 三、类型与格式后缀

| 后缀 | 英文 | 中文 | 例子 |
|---|---|---|---|
| `FL` | Flag | 标识（`Y`/`N` 或 `Y`/空） | `SAFFL`、`ABLFL` |
| `N` | Numeric | 字符变量的数值版本，用于排序 | `AVISITN`、`TRT01PN` |
| `C` | Character | 字符版本 | `AVALC` |
| `CD` | Code | 代码 | `PARAMCD`、`LBTESTCD` |
| `U` | Unit | 单位 | `AVALU`、`AGEU` |
| `GR` | Grouping | 分组 | `AGEGR1`、`RACEGR1` |
| `CAT` | Category | 分类 | `AVALCAT1` |
| `SCAT` | Subcategory | 子分类 | `LBSCAT` |
| `DESC` | Description | 描述 | `EVNTDESC` |
| `TYPE` | Type | 类型 | `DTYPE` |

## 四、前缀

| 前缀 | 英文 | 中文 | 例子 |
|---|---|---|---|
| `A` | Analysis | 分析版本（ADaM 里经过衍生或清理的值） | `AVAL`、`ADT`、`ASEV` |
| `B` | Baseline | 基线 | `BASE`、`BNRIND` |
| `P` | Percent | 百分比 | `PCHG` |
| `RF` | Reference | 参考（SDTM DM 里的参考日期） | `RFSTDTC` |
| `RFX` | Reference Exposure | 参考给药日期 | `RFXSTDTC` |
| `--` | 两位域代码占位 | 换成 AE、LB、VS 等 | `--STDTC` 即 `AESTDTC` |

## 五、计划 / 实际与编号

| 零件 | 含义 | 例子 |
|---|---|---|
| `P` / `A`（结尾） | Planned / Actual（计划 / 实际） | `TRT01P` vs `TRT01A` |
| `xx` | 两位期号（Period 01、02…） | `TRxxSDT` 即 `TR01SDT` |
| `y` | 一位序号（第几个分组或标准） | `AGEGRy` 即 `AGEGR1` |
| `zz` | 两位序号 | `ANLzzFL` 即 `ANL01FL` |

## 六、SDTM 通用结果类变量

| 后缀 | 英文 | 中文 |
|---|---|---|
| `--TESTCD` / `--TEST` | Test Short Name / Test Name | 检查项代码 / 名称 |
| `--ORRES` | Original Result | 原始结果 |
| `--ORRESU` | Original Units | 原始单位 |
| `--STRESC` | Standardized Result (Character) | 标准化结果（字符） |
| `--STRESN` | Standardized Result (Numeric) | 标准化结果（数值） |
| `--STRESU` | Standardized Units | 标准化单位 |
| `--STNRLO` / `--STNRHI` | Standardized Normal Range Lower / Upper Limit | 标准化正常值下限 / 上限 |
| `--STAT` | Completion Status | 完成状态（如 `NOT DONE`） |
| `--LOBXFL` / `--BLFL` | Last Observation Before Exposure / Baseline Flag | 用药前最后一次观测 / 基线标识 |
| `--PRESP` / `--OCCUR` | Pre-specified / Occurrence | 是否预设问题 / 是否发生 |

## 七、拆解示例

| 变量 | 拆解 | 含义 |
|---|---|---|
| `TRTSDTM` | TRT + S + DTM | 治疗开始日期时间 |
| `TR01EDT` | TR + 01 + E + DT | 第 1 期治疗结束日期 |
| `TRT01AN` | TRT + 01 + A + N | 第 1 期实际治疗（数值版） |
| `ASTDTF` | A + ST + DT + F | 分析开始日期的填补标识 |
| `BNRIND` | B + NR + IND | 基线正常值范围判定 |
| `AVALCAT1` | A + VAL + CAT + 1 | 分析值的第 1 种分类 |
| `AGEGR1N` | AGE + GR + 1 + N | 年龄分组 1（数值版） |
| `DCSREAS` | DCS + REAS | 退出研究的原因 |
| `AOCCPFL` | A + OCC + P + FL | 某个 PT 的首次发生标识 |
| `LBSTRESN` | LB + STRES + N | 实验室检查标准化结果（数值） |
| `RFXSTDTC` | RF + X + ST + DTC | 首次给药参考日期（ISO 字符型） |

有两点要注意：
- 同一个字母在不同位置意思可能不一样。比如 `P` 在 `TRT01P` 结尾是 Planned，在 `PCHG` 开头是 Percent，在 `AOCCPFL` 里是 PT（Preferred Term）。
- 带编号或 sponsor 自定义的变量（比如 `SAF1FL`、`STRATAR`）不一定遵循这些规律，最终以 define.xml 为准。

> 补充（Claude）：以下几处待 Li 对照 ADaMIG 核实：
>
> - `FL` 的取值：ADaMIG 中人群标识（如 `SAFFL`、`ITTFL`）一般要求 `Y`/`N`，其他记录级标识（如 `ABLFL`、`ANL01FL`）多为 `Y`/空，即材料说的两种情况分别对应哪类变量。
> - `DTYPE` 的全称是 Derivation Type（衍生类型），记录这一行是怎么衍生出来的，如 `LOCF`、`AVERAGE`；不只是泛指"类型"。
> - `ADT` / `ADY` 里的 `A` 是分析版本；研究日 `--DY` 没有第 0 天（第 1 天为参考日期当天，之前一天为 −1）。（这一点后来有了材料支持，算法与例子见 [CON-reference-date-study-day](CON-reference-date-study-day.md)。）

## 八、容易混淆的片段：REL / RF / REAS / RES

> 以下来自 Claude 对话（inbox: AEREL.md），AI 生成，出处待补。`AEREL` 本身见 [CON-ae-causality-arel](CON-ae-causality-arel.md)。

`REL` 不是 Reference，是 **Relationship**（关系）的缩写。Reference 对应的片段是 **`RF`**，比如 `RFSTDTC`、`RFICDT`。

同样的片段还出现在：
- `AERELNST`：AE + REL + NST（Non-Study Treatment），与非研究药物的关系
- `AREL`：A（Analysis）+ REL，分析用的因果关系

容易和 REL 混的几个片段：

| 片段 | 全称 | 例子 |
|---|---|---|
| `REL` | Relationship | `AEREL`、`AERELNST` |
| `RF` | Reference | `RFSTDTC`、`RFICDT` |
| `REAS` | Reason | `DCSREAS` |
| `RES` | Result | `LBORRES`、`LBSTRESN` |

区分的小窍门：Reference 只用两个字母 `RF`，而且总出现在**开头**；`REL`、`REAS`、`RES` 都是三四个字母，出现在域代码**后面**。

> 补充（Claude）：SDTM DM 里知情同意日期是 `RFICDTC`（ISO 字符型）；`RFICDT` 是 ADaM 中的数值型版本（如 ADSL 中由 sponsor 衍生），材料里的 `RFICDT` 应是指这个。待 Li 核实。

## 相关卡片

- [CON-censoring](../methods/tte/CON-censoring.md)：ADTTE 中 CNSR / ADT / EVNTDESC / CNSDTDSC 与删失规则
- [CON-survival-analysis-overview](../methods/tte/CON-survival-analysis-overview.md)：ADTTE 关键变量、`Surv(AVAL, 1 - CNSR)` 的方向
- [CON-reference-date-study-day](CON-reference-date-study-day.md)：参考日期与研究日的算法
- [CON-meddra-hierarchy](CON-meddra-hierarchy.md)：MedDRA 层级与 AE 编码变量（AEDECOD、AEBODSYS、AESOC）
- [CON-ae-severity-asev](CON-ae-severity-asev.md)：`AESEV` 与 `ASEV`，前缀 A 的一个实例
- [CON-ae-causality-arel](CON-ae-causality-arel.md)：`AEREL` 与 `AREL`
- [CON-sae-criteria](CON-sae-criteria.md)：`AES*` 一组 SAE 标准变量

## 出处

- Claude 对话（inbox: CDISC_1.md；AI 生成，原始出处待补）
- Claude 对话（inbox: AEREL.md；AI 生成，原始出处待补；第八节）
