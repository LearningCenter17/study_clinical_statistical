---
title: 中英术语对照
---

知识库中出现的统计术语的中英文对照，按学习大纲分章排列。**这里只做翻译和索引，不写定义**：每个术语的解释在"主卡"一列的卡片里（一个知识点只写在一张卡片里）。

- **†** = 卡片中只出现了中文或英文其中一种，另一种是 Claude 补充的常用译法，**待 Li 核实**（如 ICH E9(R1) 中文版的官方译名）。
- 主卡写"尚无卡片"的，表示卡片里只顺带提到、还没有专门解释，对应主题在 [索引](index.md) 中列为"待建"。
- 新增卡片引入新术语时，在对应章节加一行；术语的解释仍然写在卡片里。
- 按英文首字母查找见 [术语表（按英文 A–Z）](glossary-en.md)，那一页由本页自动生成。

## 1. 估计目标（Estimand）

| 中文 | English | 缩写 | 主卡 |
|---|---|---|---|
| 估计目标 | estimand | | [CON-estimand](cards/estimand/CON-estimand.md) |
| 伴发事件 | intercurrent event | ICE | [CON-estimand](cards/estimand/CON-estimand.md) |
| 群体层面汇总 † | population-level summary | | [CON-estimand](cards/estimand/CON-estimand.md) |
| 疗法策略 † | treatment policy strategy | | [CON-estimand](cards/estimand/CON-estimand.md) |
| 假想策略 † | hypothetical strategy | | [CON-estimand](cards/estimand/CON-estimand.md) |
| 复合变量策略 † | composite variable strategy | | [CON-estimand](cards/estimand/CON-estimand.md) |
| 在治策略 † | while on treatment strategy | | [CON-estimand](cards/estimand/CON-estimand.md) |
| 主层策略 † | principal stratum strategy | | [CON-estimand](cards/estimand/CON-estimand.md) |
| 救援药物 | rescue medication / rescue therapy | | [CON-rescue-medication](cards/estimand/CON-rescue-medication.md) |
| 救援触发条件 | rescue criteria | | [CON-rescue-medication](cards/estimand/CON-rescue-medication.md) |
| 合并用药 | concomitant medication | CM | [CON-rescue-medication](cards/estimand/CON-rescue-medication.md) |

## 2. 统计推断基础

| 中文 | English | 缩写 | 主卡 |
|---|---|---|---|
| 零假设 | null hypothesis | H₀ | [CON-null-hypothesis](cards/inference/CON-null-hypothesis.md) |
| 备择假设 | alternative hypothesis † | H₁ / Hₐ | [CON-p-value](cards/inference/CON-p-value.md) |
| 单侧 / 双侧检验 | one-sided / two-sided test † | | [CON-p-value](cards/inference/CON-p-value.md) |
| P 值 | P-value | | [CON-p-value](cards/inference/CON-p-value.md) |
| 零分布 | null distribution † | | [CON-p-value](cards/inference/CON-p-value.md) |
| 置换检验 | permutation test | | [CON-p-value](cards/inference/CON-p-value.md) |
| 精确检验 | exact test | | [CON-p-value](cards/inference/CON-p-value.md) |
| 检验统计量 | test statistic | | [CON-test-statistic](cards/inference/CON-test-statistic.md) |
| 自由度 | degrees of freedom | df | [CON-degrees-of-freedom](cards/inference/CON-degrees-of-freedom.md) |
| 第一类错误 | type I error | α | [CON-type-I-II-error](cards/inference/CON-type-I-II-error.md) |
| 第二类错误 | type II error | β | [CON-type-I-II-error](cards/inference/CON-type-I-II-error.md) |
| 检验效能 / 把握度 | power | 1 − β | [CON-type-I-II-error](cards/inference/CON-type-I-II-error.md) |
| 伯努利分布 / 二项分布 | Bernoulli / binomial distribution | | [CON-distribution-family](cards/inference/CON-distribution-family.md) |
| 正态分布 / 标准正态分布 | normal / standard normal distribution | N(0, 1) | [CON-normal-distribution](cards/inference/CON-normal-distribution.md) |
| 标准化 | standardization | z | [CON-normal-distribution](cards/inference/CON-normal-distribution.md) |
| 临界值 | critical value † | | [CON-t-distribution](cards/inference/CON-t-distribution.md) |
| t 分布 | Student's t distribution | | [CON-t-distribution](cards/inference/CON-t-distribution.md) |
| 卡方分布 | chi-square distribution | χ² | [CON-chi-square-distribution](cards/inference/CON-chi-square-distribution.md) |
| F 分布 | F distribution † | F | [CON-distribution-family](cards/inference/CON-distribution-family.md) |
| 中心极限定理 | central limit theorem † | CLT | [CON-distribution-family](cards/inference/CON-distribution-family.md) |
| 方差分析 | analysis of variance | ANOVA | [CON-distribution-family](cards/inference/CON-distribution-family.md) |
| 标准误 | standard error | SE | [MTH-t-test](cards/methods/continuous/MTH-t-test.md) |
| 效应量 | effect size | | [CON-sample-size-power](cards/design/CON-sample-size-power.md) |
| 置信区间 | confidence interval | CI | [CON-confidence-interval](cards/inference/CON-confidence-interval.md) |
| 点估计 | point estimate † | | [CON-confidence-interval](cards/inference/CON-confidence-interval.md) |
| 覆盖率 | coverage | | [CON-confidence-interval](cards/inference/CON-confidence-interval.md) |
| 可信区间 | credible interval | CrI | [CON-credible-interval](cards/inference/CON-credible-interval.md) |
| 频率学派 / 贝叶斯学派 | frequentist / Bayesian | | [CON-credible-interval](cards/inference/CON-credible-interval.md) |
| 先验 / 后验 | prior / posterior | | [CON-credible-interval](cards/inference/CON-credible-interval.md) |
| Wald 法 | Wald | | [MTH-ci-construction](cards/inference/MTH-ci-construction.md) |
| 精确法（单组率 CI） | Clopper-Pearson | | [MTH-ci-construction](cards/inference/MTH-ci-construction.md) |
| 参数方法 / 非参数方法 | parametric / nonparametric methods | | [CON-parametric-vs-nonparametric](cards/inference/CON-parametric-vs-nonparametric.md) |
| 渐近相对效率 | asymptotic relative efficiency | ARE | [CON-parametric-vs-nonparametric](cards/inference/CON-parametric-vs-nonparametric.md) |
| Mann-Whitney U 检验 / Wilcoxon 秩和检验 | Mann-Whitney U test / Wilcoxon rank-sum test | | [CON-test-selection](cards/inference/CON-test-selection.md) |
| Kruskal-Wallis 检验 | Kruskal-Wallis test | | [CON-test-selection](cards/inference/CON-test-selection.md) |
| Fisher 精确检验 | Fisher's exact test | | [CON-test-selection](cards/inference/CON-test-selection.md) |
| 连续性校正 | continuity correction | | [CON-continuity-correction](cards/inference/CON-continuity-correction.md) |
| Yates 校正 | Yates' continuity correction | | [CON-continuity-correction](cards/inference/CON-continuity-correction.md) |

## 3. 连续型终点

| 中文 | English | 缩写 | 主卡 |
|---|---|---|---|
| t 检验 | t-test | | [MTH-t-test](cards/methods/continuous/MTH-t-test.md) |
| 合并方差 t 检验 / Welch t 检验 | pooled (Student's) / Welch's t-test | | [GOT-ttest-student-vs-welch](cards/methods/continuous/GOT-ttest-student-vs-welch.md) |
| Satterthwaite 近似自由度 | Satterthwaite | | [GOT-ttest-student-vs-welch](cards/methods/continuous/GOT-ttest-student-vs-welch.md) |
| 协变量 / 协变量调整 | covariate / covariate adjustment | | [CON-covariate](cards/methods/continuous/CON-covariate.md) |
| 协方差分析 | analysis of covariance | ANCOVA | [CON-covariate](cards/methods/continuous/CON-covariate.md) |
| 回归 | regression |  | [CON-regression](cards/methods/CON-regression.md) |
| 回归系数 | regression coefficient † | β | [CON-regression](cards/methods/CON-regression.md) |
| 因变量 / 结局变量 | dependent / outcome variable † |  | [CON-regression](cards/methods/CON-regression.md) |
| 自变量 / 预测变量 | independent / predictor variable † |  | [CON-regression](cards/methods/CON-regression.md) |
| 线性回归 / 最小二乘法 | linear regression / ordinary least squares | OLS | [CON-regression](cards/methods/CON-regression.md) |
| 逻辑回归 | logistic regression |  | [CON-regression](cards/methods/CON-regression.md) |
| 广义线性模型 | generalized linear model † | GLM | [CON-regression](cards/methods/CON-regression.md) |
| 回归均值 | regression toward the mean |  | [CON-regression](cards/methods/CON-regression.md) |
| 率比 | rate ratio † | RR | [CON-regression](cards/methods/CON-regression.md) |
| 重复测量混合模型 | mixed model for repeated measures | MMRM | [MTH-MMRM](cards/methods/continuous/MTH-MMRM.md) |
| 非结构化协方差 | unstructured covariance † | UN | [MTH-MMRM](cards/methods/continuous/MTH-MMRM.md) |
| Kenward-Roger 自由度 | Kenward-Roger | KR | [MTH-MMRM](cards/methods/continuous/MTH-MMRM.md) |
| 最小二乘均值 † | least squares mean | LS mean | [MTH-MMRM](cards/methods/continuous/MTH-MMRM.md) |
| Hodges-Lehmann 估计 | Hodges-Lehmann estimator | HL | [GOT-skewed-small-sample](cards/methods/continuous/GOT-skewed-small-sample.md) |

## 4. 二分类与有序分类终点

| 中文 | English | 缩写 | 主卡 |
|---|---|---|---|
| 应答 / 应答者 | response / responder | | [CON-response-rate](cards/methods/binary/CON-response-rate.md) |
| 应答概率 / 应答率 | response probability / response rate | p / p̂ | [CON-response-rate](cards/methods/binary/CON-response-rate.md) |
| 客观缓解率 | objective response rate | ORR | [CON-response-rate](cards/methods/binary/CON-response-rate.md) |
| 最佳总体应答 | best overall response | BOR | [CON-response-rate](cards/methods/binary/CON-response-rate.md) |
| 确认 | confirmation | | [CON-response-rate](cards/methods/binary/CON-response-rate.md) |
| 应答者分析 | responder analysis | | [CON-response-rate](cards/methods/binary/CON-response-rate.md) |
| 卡方检验 | chi-square test / Pearson's chi-squared test | χ² | [MTH-chi-square](cards/methods/binary/MTH-chi-square.md) |
| 独立性检验 | test of independence | | [MTH-chi-square](cards/methods/binary/MTH-chi-square.md) |
| 拟合优度检验 | goodness-of-fit test | | [MTH-chi-square](cards/methods/binary/MTH-chi-square.md) |
| 观察频数 / 期望频数 | observed / expected frequency † | O / E | [MTH-chi-square](cards/methods/binary/MTH-chi-square.md) |
| CMH 检验 | Cochran-Mantel-Haenszel test | CMH | [MTH-CMH](cards/methods/binary/MTH-CMH.md) |
| MH 合并 OR | Mantel-Haenszel common odds ratio † | MH OR | [MTH-CMH](cards/methods/binary/MTH-CMH.md) |
| Breslow-Day 检验 | Breslow-Day test | | [MTH-breslow-day](cards/methods/binary/MTH-breslow-day.md) |
| OR 同质性 | homogeneity of odds ratios | | [MTH-breslow-day](cards/methods/binary/MTH-breslow-day.md) |
| Tarone 校正 | Tarone's adjustment † | | [MTH-breslow-day](cards/methods/binary/MTH-breslow-day.md) |
| 量的交互作用 / 质的交互作用 | quantitative / qualitative interaction | | [MTH-breslow-day](cards/methods/binary/MTH-breslow-day.md) |
| 辛普森悖论 | Simpson's paradox | | [MTH-CMH](cards/methods/binary/MTH-CMH.md) |
| 优势（赔率） | odds | | [CON-odds-ratio](cards/methods/binary/CON-odds-ratio.md) |
| 优势比 / 比值比 | odds ratio | OR | [CON-odds-ratio](cards/methods/binary/CON-odds-ratio.md) |
| 交叉乘积比 | cross-product ratio | | [CON-odds-ratio](cards/methods/binary/CON-odds-ratio.md) |
| 相对危险度 | relative risk | RR | [CON-odds-ratio](cards/methods/binary/CON-odds-ratio.md) |
| 率差 | risk difference | RD | [CON-odds-ratio](cards/methods/binary/CON-odds-ratio.md) |
| 率差 CI 方法 | Newcombe / Miettinen-Nurminen | | [MTH-ci-construction](cards/inference/MTH-ci-construction.md) |
| 有序分类数据 | ordinal data | | [CON-ordinal-data](cards/methods/ordinal/CON-ordinal-data.md) |
| 比例优势模型 / 有序 logistic 回归 | proportional odds model / ordinal logistic regression | PO | [MTH-proportional-odds-model](cards/methods/ordinal/MTH-proportional-odds-model.md) |
| 比例优势假设 | proportional odds assumption | | [MTH-proportional-odds-model](cards/methods/ordinal/MTH-proportional-odds-model.md) |

## 5. 生存分析

| 中文 | English | 缩写 | 主卡 |
|---|---|---|---|
| 风险比 | hazard ratio | HR | [CON-hazard-ratio](cards/methods/tte/CON-hazard-ratio.md) |
| 比例风险 | proportional hazards | PH | [CON-hazard-ratio](cards/methods/tte/CON-hazard-ratio.md) |
| log-rank 检验 | log-rank test | | [CON-logrank-vs-cox](cards/methods/tte/CON-logrank-vs-cox.md) |
| Cox 模型 | Cox proportional hazards model | | [CON-logrank-vs-cox](cards/methods/tte/CON-logrank-vs-cox.md) |
| 删失 | censoring | CNSR | [CON-censoring](cards/methods/tte/CON-censoring.md) |
| 似然 | likelihood | | [CON-survival-analysis-overview](cards/methods/tte/CON-survival-analysis-overview.md) |
| 结点（事件时间相同） | tied event times | | [CON-logrank-vs-cox](cards/methods/tte/CON-logrank-vs-cox.md) |
| Kaplan-Meier 法 | Kaplan-Meier | KM | [MTH-kaplan-meier](cards/methods/tte/MTH-kaplan-meier.md) |
| 生存分析 / 时间-事件分析 | survival analysis / time-to-event analysis | TTE | [CON-survival-analysis-overview](cards/methods/tte/CON-survival-analysis-overview.md) |
| 生存函数 | survival function † | S(t) | [CON-survival-analysis-overview](cards/methods/tte/CON-survival-analysis-overview.md) |
| 风险函数 | hazard function † | h(t) | [CON-survival-analysis-overview](cards/methods/tte/CON-survival-analysis-overview.md) |
| 累积风险 | cumulative hazard † | H(t) | [CON-survival-analysis-overview](cards/methods/tte/CON-survival-analysis-overview.md) |
| 中位生存时间 | median survival time † |  | [CON-survival-analysis-overview](cards/methods/tte/CON-survival-analysis-overview.md) |
| 在险人数 | number at risk |  | [MTH-kaplan-meier](cards/methods/tte/MTH-kaplan-meier.md) |
| 在险集 | risk set † |  | [MTH-kaplan-meier](cards/methods/tte/MTH-kaplan-meier.md) |
| 风险集（同在险集） | risk set † |  | [MTH-kaplan-meier](cards/methods/tte/MTH-kaplan-meier.md) |
| 未达到（中位生存时间） | not reached † | NR | [MTH-kaplan-meier](cards/methods/tte/MTH-kaplan-meier.md) |
| Greenwood 公式 | Greenwood's formula † |  | [MTH-kaplan-meier](cards/methods/tte/MTH-kaplan-meier.md) |
| 右删失 / 左删失 / 区间删失 | right / left / interval censoring † |  | [CON-censoring](cards/methods/tte/CON-censoring.md) |
| 行政删失 | administrative censoring † |  | [CON-censoring](cards/methods/tte/CON-censoring.md) |
| 失访 | loss to follow-up † |  | [CON-censoring](cards/methods/tte/CON-censoring.md) |
| 撤回知情同意 | withdrawal of consent † |  | [CON-censoring](cards/methods/tte/CON-censoring.md) |
| 删失日期 | censoring date † |  | [CON-censoring](cards/methods/tte/CON-censoring.md) |
| 非信息性删失 | non-informative censoring † |  | [CON-survival-analysis-overview](cards/methods/tte/CON-survival-analysis-overview.md) |
| 限制平均生存时间 | restricted mean survival time | RMST | [CON-survival-analysis-overview](cards/methods/tte/CON-survival-analysis-overview.md) |
| 加权 log-rank 检验 | weighted log-rank test (Fleming–Harrington) / MaxCombo |  | [CON-survival-analysis-overview](cards/methods/tte/CON-survival-analysis-overview.md) |
| 竞争风险 | competing risks |  | [CON-survival-analysis-overview](cards/methods/tte/CON-survival-analysis-overview.md) |
| 累积发生率函数 | cumulative incidence function | CIF | [CON-survival-analysis-overview](cards/methods/tte/CON-survival-analysis-overview.md) |
| Gray 检验 / Fine–Gray 模型 | Gray's test / Fine–Gray model |  | [CON-survival-analysis-overview](cards/methods/tte/CON-survival-analysis-overview.md) |
| Schoenfeld 残差 | Schoenfeld residuals |  | [CON-survival-analysis-overview](cards/methods/tte/CON-survival-analysis-overview.md) |
| 可靠性分析 | reliability analysis |  | [CON-survival-analysis-non-clinical](cards/non-clinical/CON-survival-analysis-non-clinical.md) |
| 持续时间分析 | duration analysis |  | [CON-survival-analysis-non-clinical](cards/non-clinical/CON-survival-analysis-non-clinical.md) |
| 事件史分析 | event history analysis |  | [CON-survival-analysis-non-clinical](cards/non-clinical/CON-survival-analysis-non-clinical.md) |
| 加速失效时间模型 † | accelerated failure time model † | AFT | [CON-survival-analysis-non-clinical](cards/non-clinical/CON-survival-analysis-non-clinical.md) |
| 留存曲线 | retention curve † |  | [CON-survival-analysis-non-clinical](cards/non-clinical/CON-survival-analysis-non-clinical.md) |
| 时间-事件分析数据集 | ADaM time-to-event dataset † | ADTTE | [CON-survival-analysis-overview](cards/methods/tte/CON-survival-analysis-overview.md) |
| 总生存期 | overall survival † | OS | [CON-survival-analysis-overview](cards/methods/tte/CON-survival-analysis-overview.md) |
| 无进展生存期 | progression-free survival † | PFS | [CON-survival-analysis-overview](cards/methods/tte/CON-survival-analysis-overview.md) |
| 至首次不良事件时间 | time to first adverse event † | TTAE | [CON-survival-analysis-overview](cards/methods/tte/CON-survival-analysis-overview.md) |

## 6. 缺失数据与敏感性分析

| 中文 | English | 缩写 | 主卡 |
|---|---|---|---|
| 完全随机缺失 | missing completely at random | MCAR | [CON-missing-data](cards/missing-data/CON-missing-data.md) |
| 随机缺失 | missing at random | MAR | [CON-missing-data](cards/missing-data/CON-missing-data.md) |
| 非随机缺失 | missing not at random | MNAR | [CON-missing-data](cards/missing-data/CON-missing-data.md) |
| 多重插补 | multiple imputation † | MI | [CON-missing-data](cards/missing-data/CON-missing-data.md) |
| 模式混合模型 | pattern mixture model | PMM | [CON-sensitivity-analysis](cards/missing-data/CON-sensitivity-analysis.md) |
| 临界点分析 | tipping point analysis † | | [CON-sensitivity-analysis](cards/missing-data/CON-sensitivity-analysis.md) |
| 跳至参照组 | jump to reference † | J2R | [CON-sensitivity-analysis](cards/missing-data/CON-sensitivity-analysis.md) |
| 停药后数据 | retrieved dropout data | | [CON-missing-data](cards/missing-data/CON-missing-data.md) |
| 敏感性分析 / 补充分析 | sensitivity analysis / supplementary analysis | | [CON-sensitivity-analysis](cards/missing-data/CON-sensitivity-analysis.md) |

## 7. 多重性

| 中文 | English | 缩写 | 主卡 |
|---|---|---|---|
| 多重性 / 多重比较 | multiplicity / multiple comparisons † | | 尚无卡片（提及于 [CON-type-I-II-error](cards/inference/CON-type-I-II-error.md)） |
| 族错误率 † | familywise error rate | FWER | 尚无卡片（提及于 [CON-type-I-II-error](cards/inference/CON-type-I-II-error.md)） |
| Bonferroni / Hochberg 法 | Bonferroni / Hochberg | | 尚无卡片 |
| 守门程序 / 分层检验 † | gatekeeping / hierarchical testing | | 尚无卡片 |
| α 消耗函数 | alpha spending function † | | 尚无卡片（提及于 [CON-sample-size-power](cards/design/CON-sample-size-power.md)） |

## 8. 样本量与试验设计

| 中文 | English | 缩写 | 主卡 |
|---|---|---|---|
| 样本量计算 | sample size calculation / determination | | [CON-sample-size-power](cards/design/CON-sample-size-power.md) |
| 样本量估算的依据 | sample size justification / rationale | | [CON-sample-size-power](cards/design/CON-sample-size-power.md) |
| 假设的治疗差值 | assumed treatment difference / target difference | δ | [CON-sample-size-power](cards/design/CON-sample-size-power.md) |
| 临床最小有意义差值 | minimal clinically important difference | MCID | [CON-sample-size-power](cards/design/CON-sample-size-power.md) |
| 脱落率 | dropout rate | | [CON-sample-size-power](cards/design/CON-sample-size-power.md) |
| Schoenfeld 事件数公式 | Schoenfeld formula | D | [WF-sample-size-calc](cards/design/WF-sample-size-calc.md) |
| 非劣效 / 非劣效界值 | non-inferiority / non-inferiority margin | NI / M | [CON-ni-sample-size](cards/design/CON-ni-sample-size.md) |
| 不等分配 | unequal allocation | k:1 | [CON-unequal-allocation](cards/design/CON-unequal-allocation.md) |
| 分层随机化 / 过度分层 | stratified randomization / over-stratification | | [CON-stratified-randomization](cards/design/CON-stratified-randomization.md) |
| 最小化法 | minimization | | [CON-stratified-randomization](cards/design/CON-stratified-randomization.md) |
| 预后因素 / 预测因素 | prognostic / predictive factor | | [CON-prognostic-factor](cards/design/CON-prognostic-factor.md) |
| 富集设计 | enrichment design † | | [CON-prognostic-factor](cards/design/CON-prognostic-factor.md) |
| 剂量限制性毒性 † | dose-limiting toxicity | DLT | [CON-dose-escalation-design](cards/design/CON-dose-escalation-design.md) |
| 最大耐受剂量 | maximum tolerated dose | MTD | [CON-dose-escalation-design](cards/design/CON-dose-escalation-design.md) |
| 基于规则 / 基于模型 / 模型辅助的设计 | rule-based / model-based / model-assisted designs | 3+3 / CRM、BLRM / BOIN | [CON-dose-escalation-design](cards/design/CON-dose-escalation-design.md) |
| 剂量扩展 | dose expansion | | [CON-dose-escalation-design](cards/design/CON-dose-escalation-design.md) |

## 人群与数据集

| 中文 | English | 缩写 | 主卡 |
|---|---|---|---|
| 意向性治疗 / 全分析集 † | intention-to-treat / full analysis set | ITT / FAS | [CON-null-hypothesis](cards/inference/CON-null-hypothesis.md) |

## 安全性

| 中文 | English | 缩写 | 主卡 |
|---|---|---|---|
| 妊娠报告表 | Pregnancy Report Form |  | [WF-pregnancy-reporting](cards/safety/WF-pregnancy-reporting.md) |
| 药物警戒 | pharmacovigilance |  | [WF-pregnancy-reporting](cards/safety/WF-pregnancy-reporting.md) |
| 安全数据库 † | safety database |  | [WF-pregnancy-reporting](cards/safety/WF-pregnancy-reporting.md) |
| 研发期间安全性更新报告 † | Development Safety Update Report | DSUR | [WF-pregnancy-reporting](cards/safety/WF-pregnancy-reporting.md) |
| 定期安全性更新报告 † | Periodic Safety Update Report | PSUR | [WF-pregnancy-reporting](cards/safety/WF-pregnancy-reporting.md) |
| 半衰期 | half-life † |  | [WF-pregnancy-reporting](cards/safety/WF-pregnancy-reporting.md) |
| 高效避孕措施 | highly effective contraception † |  | [WF-pregnancy-reporting](cards/safety/WF-pregnancy-reporting.md) |
| 重要医学事件术语列表 † | Important Medical Event Terms List | IME | [CON-sae-criteria](cards/cdisc/CON-sae-criteria.md) |
| Hy's Law（海氏法则）† | Hy's Law |  | [CON-sae-criteria](cards/cdisc/CON-sae-criteria.md) |
| 特别关注的不良事件 † | adverse event of special interest | AESI | [CON-sae-criteria](cards/cdisc/CON-sae-criteria.md) |

## CDISC 数据标准

| 中文 | English | 缩写 | 主卡 |
|---|---|---|---|
| 研究数据制表模型 † | Study Data Tabulation Model | SDTM | [CON-cdisc-variable-naming](cards/cdisc/CON-cdisc-variable-naming.md) |
| 分析数据模型 † | Analysis Data Model | ADaM | [CON-cdisc-variable-naming](cards/cdisc/CON-cdisc-variable-naming.md) |
| 数据定义文件 † | define.xml |  | [CON-cdisc-variable-naming](cards/cdisc/CON-cdisc-variable-naming.md) |
| 域（两位域代码，如 AE、LB、VS）† | domain |  | [CON-cdisc-variable-naming](cards/cdisc/CON-cdisc-variable-naming.md) |
| 首选术语 † | Preferred Term | PT | [CON-meddra-hierarchy](cards/cdisc/CON-meddra-hierarchy.md) |
| 系统器官分类 | body system / system organ class † | SOC | [CON-meddra-hierarchy](cards/cdisc/CON-meddra-hierarchy.md) |
| 监管活动医学词典 † | Medical Dictionary for Regulatory Activities | MedDRA | [CON-meddra-hierarchy](cards/cdisc/CON-meddra-hierarchy.md) |
| 低位语 | Lowest Level Term | LLT | [CON-meddra-hierarchy](cards/cdisc/CON-meddra-hierarchy.md) |
| 高位语 | High Level Term | HLT | [CON-meddra-hierarchy](cards/cdisc/CON-meddra-hierarchy.md) |
| 高位组语 | High Level Group Term | HLGT | [CON-meddra-hierarchy](cards/cdisc/CON-meddra-hierarchy.md) |
| 主 SOC | primary SOC |  | [CON-meddra-hierarchy](cards/cdisc/CON-meddra-hierarchy.md) |
| 多轴 | multiaxial |  | [CON-meddra-hierarchy](cards/cdisc/CON-meddra-hierarchy.md) |
| 字典编码术语 | Dictionary-Derived Term |  | [CON-meddra-hierarchy](cards/cdisc/CON-meddra-hierarchy.md) |
| 严重程度（强度） | severity / intensity |  | [CON-ae-severity-asev](cards/cdisc/CON-ae-severity-asev.md) |
| 严重不良事件 | serious adverse event | SAE | [CON-ae-severity-asev](cards/cdisc/CON-ae-severity-asev.md) |
| 先天异常或出生缺陷 | congenital anomaly or birth defect | AESCONG | [CON-sae-criteria](cards/cdisc/CON-sae-criteria.md) |
| 其他重要医学事件 | other medically important serious event | AESMIE | [CON-sae-criteria](cards/cdisc/CON-sae-criteria.md) |
| 持续或显著的残疾 / 功能丧失 | persistent or significant disability/incapacity | AESDISAB | [CON-sae-criteria](cards/cdisc/CON-sae-criteria.md) |
| 不良事件通用术语标准 † | Common Terminology Criteria for Adverse Events | CTCAE | [CON-ae-severity-asev](cards/cdisc/CON-ae-severity-asev.md) |
| 因果关系（与研究药物的相关性） | causality / relationship to study drug |  | [CON-ae-causality-arel](cards/cdisc/CON-ae-causality-arel.md) |
| 治疗期出现的不良事件 † | treatment-emergent adverse event | TEAE | [CON-ae-causality-arel](cards/cdisc/CON-ae-causality-arel.md) |
| 药物相关 TEAE / 药物不良反应 † | treatment-related TEAE / adverse drug reaction | ADR | [CON-ae-causality-arel](cards/cdisc/CON-ae-causality-arel.md) |
| 与非研究药物的关系 † | relationship to non-study treatment | AERELNST | [CON-ae-causality-arel](cards/cdisc/CON-ae-causality-arel.md) |
| 研究日 † | study day | --DY | [CON-reference-date-study-day](cards/cdisc/CON-reference-date-study-day.md) |
| 参考日期 | reference date |  | [CON-reference-date-study-day](cards/cdisc/CON-reference-date-study-day.md) |
| 受试者参考开始日期 † | Subject Reference Start Date | RFSTDTC | [CON-reference-date-study-day](cards/cdisc/CON-reference-date-study-day.md) |
| 日期填补标识 † | date imputation flag | --DTF | [CON-partial-date-imputation](cards/cdisc/CON-partial-date-imputation.md) |
| 不完整日期 † | partial date |  | [CON-partial-date-imputation](cards/cdisc/CON-partial-date-imputation.md) |
| 分析开始日期 † | Analysis Start Date | ASTDT | [CON-partial-date-imputation](cards/cdisc/CON-partial-date-imputation.md) |
| 衍生类型 † | derivation type | DTYPE | [CON-cdisc-variable-naming](cards/cdisc/CON-cdisc-variable-naming.md) |
| 研究阶段 † | epoch | EPOCH | [CON-sdtm-epoch](cards/cdisc/CON-sdtm-epoch.md) |
| 研究单元 † | element |  | [CON-sdtm-epoch](cards/cdisc/CON-sdtm-epoch.md) |
| 治疗组路线 † | arm |  | [CON-sdtm-epoch](cards/cdisc/CON-sdtm-epoch.md) |
| 试验设计域 † | trial design domains | TA / TE | [CON-sdtm-epoch](cards/cdisc/CON-sdtm-epoch.md) |
| 受试者单元域 † | Subject Elements | SE | [CON-sdtm-epoch](cards/cdisc/CON-sdtm-epoch.md) |
| 开放标签延长期 † | open-label extension | OLE | [CON-sdtm-epoch](cards/cdisc/CON-sdtm-epoch.md) |

## 非临床应用

| 中文 | English | 缩写 | 主卡 |
|---|---|---|---|
| 可靠性工程 | reliability engineering |  | [CON-reliability-engineering](cards/non-clinical/CON-reliability-engineering.md) |
| B10 寿命 | B10 life † | B10 | [CON-reliability-engineering](cards/non-clinical/CON-reliability-engineering.md) |
| 平均失效时间 | mean time to failure † | MTTF | [CON-reliability-engineering](cards/non-clinical/CON-reliability-engineering.md) |
| 平均故障间隔时间 | mean time between failures † | MTBF | [CON-reliability-engineering](cards/non-clinical/CON-reliability-engineering.md) |
| 可靠度 | reliability † |  | [CON-reliability-engineering](cards/non-clinical/CON-reliability-engineering.md) |
| 加速寿命试验 | accelerated life testing † | ALT | [CON-reliability-engineering](cards/non-clinical/CON-reliability-engineering.md) |
| 保修数据分析 | warranty analysis |  | [CON-reliability-engineering](cards/non-clinical/CON-reliability-engineering.md) |
| 预测性维护 | predictive maintenance † |  | [CON-reliability-engineering](cards/non-clinical/CON-reliability-engineering.md) |
| 时间依赖协变量 | time-varying covariate † |  | [CON-reliability-engineering](cards/non-clinical/CON-reliability-engineering.md) |
| Weibull 分布 | Weibull distribution |  | [CON-reliability-engineering](cards/non-clinical/CON-reliability-engineering.md) |
| 形状参数 | shape parameter † |  | [CON-reliability-engineering](cards/non-clinical/CON-reliability-engineering.md) |
| 浴盆曲线 | bathtub curve |  | [CON-reliability-engineering](cards/non-clinical/CON-reliability-engineering.md) |
