---
id: CON-confirmatory-methods-overview
title: "确证性试验最常用的统计方法总览（Common Methods in Confirmatory Trials）"
categories: [overview, confirmatory-trial, ancova, mmrm, kaplan-meier, log-rank, cox, cmh, logistic, fisher-exact, chi-square, wilcoxon, negative-binomial, clopper-pearson, risk-difference, therapeutic-area, statistical-programming]
related: [CON-test-selection, CON-covariate, CON-MMRM, CON-logrank-vs-cox, CON-hazard-ratio, CON-parametric-vs-nonparametric, CON-missing-data, CON-sensitivity-analysis, CON-t-test-pvalue, CON-ordinal-data, CON-CMH, CON-proportional-odds-model]
sources: ["Claude 对话（inbox: most_pop_stat_test.md）"]
status: draft
updated: 2026-11-12
---

> 出处待补：本卡内容来自 Claude 对话（inbox: most_pop_stat_test.md），属 AI 生成内容，未引用原始文献。**排序是按行业惯例给的大致印象，不是统计出来的排名**，不同治疗领域的侧重点会不一样。

本卡是**导航页**：列出注册试验里实际最常用的方法，并指向各章的详细卡片。教科书式的"怎么选检验"见 [CON-test-selection](CON-test-selection.md)。

## 十种最常见的方法

| # | 方法 | English | 终点类型 | 典型用途 | 详见 |
|---|---|---|---|---|---|
| 1 | 协方差分析 | ANCOVA | 连续 | 单个时间点的主要终点，调整基线和分层因素（如第 24 周 HbA1c 变化） | [CON-covariate](CON-covariate.md)（第 3 章） |
| 2 | 混合效应重复测量模型 | MMRM | 连续 · 多访视 | 有脱落的多访视终点（如抑郁量表、肺功能） | [CON-MMRM](CON-MMRM.md)（第 3 章） |
| 3 | Kaplan-Meier 法 | Kaplan-Meier | 时间-事件 | 生存曲线、中位 OS / PFS | 第 5 章，待建 |
| 4 | Log-rank 检验 | Log-rank test | 时间-事件 | 肿瘤试验 OS / PFS 主要终点的检验 | [CON-logrank-vs-cox](CON-logrank-vs-cox.md) |
| 5 | Cox 比例风险模型 | Cox PH model | 时间-事件 | 风险比（HR）及 95% CI | [CON-hazard-ratio](CON-hazard-ratio.md)、[CON-logrank-vs-cox](CON-logrank-vs-cox.md) |
| 6 | CMH 检验 | Cochran-Mantel-Haenszel | 二分类 | 分层比较应答率（如 PASI 75、ACR20） | [CON-CMH](CON-CMH.md)（第 4 章；二分类部分待补） |
| 7 | Logistic 回归 | Logistic regression | 二分类 | 调整协变量后的比值比（OR） | 第 4 章，待建 |
| 8 | Fisher 确切概率法 | Fisher's exact test | 二分类 | 小样本、AE / SAE 发生率比较 | [CON-test-selection](CON-test-selection.md) |
| 9 | 卡方检验 | Chi-square test | 分类 | 大样本时的率比较、基线特征比较 | [CON-test-selection](CON-test-selection.md) |
| 10 | Wilcoxon 秩和检验 | Wilcoxon rank-sum / Mann-Whitney U | 连续 / 有序 | 偏态数据、敏感性分析 | [CON-parametric-vs-nonparametric](CON-parametric-vs-nonparametric.md)、[CON-sensitivity-analysis](CON-sensitivity-analysis.md) |

## 紧随其后的几个

- **负二项回归**：呼吸领域急性加重率的标准方法。
- **Clopper-Pearson 精确置信区间**：单臂肿瘤试验 ORR 的标配。
- **率差置信区间（Miettinen-Nurminen / Newcombe）**：用于非劣效试验、疫苗试验（第 4 章，待建）。
- **t 检验**：教科书里最常见，但在注册试验的主分析中通常被 ANCOVA 取代（t 检验本身见 [CON-t-test-pvalue](CON-t-test-pvalue.md)）。

## 两个实际观察

**1. 描述统计才是工作量最大的部分。** 按 TLF 数量算，绝大多数表格是描述统计：

- 连续变量：n、均值、SD、中位数、Q1/Q3、最小值/最大值
- 分类变量：频数和百分比
- 常见的表：人口学、基线特征、AE 汇总、实验室检查、生命体征

真正做假设检验的表只占一小部分。

**2. 按领域分，常用方法其实很集中：**

| 领域 | 核心方法 |
|---|---|
| 肿瘤 | KM、log-rank、Cox、Clopper-Pearson |
| 代谢 / 心血管指标 | ANCOVA、MMRM |
| 免疫 / 皮肤 | CMH、logistic、非应答者填补（缺失数据处理见 [CON-missing-data](CON-missing-data.md)） |
| 呼吸 | 负二项回归、MMRM |
| 安全性（所有领域） | 描述统计，偶尔用 Fisher |

## 对统计程序员的建议

先把前五个方法的 R 和 SAS 结果对齐练熟，就能覆盖大部分推断统计表。对齐的重点：

- ANCOVA 的 LS mean
- MMRM 的 KR 自由度（见 [CON-MMRM](CON-MMRM.md)）
- KM 的中位数 CI
- Cox 的 ties 处理（见 [CON-logrank-vs-cox](CON-logrank-vs-cox.md)）

> 补充（Claude）：SAS / R 对应实现速查，待 Li 核实。
>
> | 方法 | SAS | R |
> |---|---|---|
> | ANCOVA | `PROC GLM` / `PROC MIXED` + `LSMEANS` | `lm()` + `emmeans` |
> | MMRM | `PROC MIXED`（`REPEATED`，`DDFM=KR`） | `mmrm` 包 |
> | KM / log-rank | `PROC LIFETEST` | `survival::survfit()` / `survdiff()` |
> | Cox | `PROC PHREG` | `survival::coxph()` |
> | CMH | `PROC FREQ`（`CMH`） | `mantelhaen.test()` |
> | Logistic | `PROC LOGISTIC` | `glm(family = binomial)` |
> | Fisher | `PROC FREQ`（`EXACT FISHER`） | `fisher.test()` |
> | 负二项 | `PROC GENMOD`（`DIST=NEGBIN`，随访时间取 log 作 offset） | `MASS::glm.nb()` |
> | Clopper-Pearson | `PROC FREQ`（`BINOMIAL(EXACT)`） | `binom.test()` |
> | 率差 MN CI | `PROC FREQ`（`RISKDIFF(CL=MN)`） | 需用扩展包 |
>
> KM 中位数 CI 的常见不一致：SAS `PROC LIFETEST` 默认 `CONFTYPE=LOGLOG`，R `survfit()` 默认 `conf.type = "log"`。对齐时要在 R 里指定 `conf.type = "log-log"`。

## 相关卡片

- [CON-test-selection](CON-test-selection.md)：教科书式检验选择表
- [CON-covariate](CON-covariate.md)、[CON-MMRM](CON-MMRM.md)：第 3 章连续终点
- [CON-logrank-vs-cox](CON-logrank-vs-cox.md)、[CON-hazard-ratio](CON-hazard-ratio.md)：第 5 章生存分析

## 出处

- Claude 对话（inbox: most_pop_stat_test.md；AI 生成，原始出处待补）
