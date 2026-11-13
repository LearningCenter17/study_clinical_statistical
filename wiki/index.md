---
title: 知识库索引
---

按学习大纲分章列出所有卡片（CON / GOT / REF / TLF 混排，前缀表示卡片类型）。新增或删除卡片时同步更新本页。
每章末尾的"待建"是该章还没有卡片的主题，建好后从这里删掉。

## 1. 估计目标（Estimand）框架

先建立"分析到底在回答什么问题"的视角。

- [CON-estimand](concepts/CON-estimand.md) — 估计目标的五个属性与伴发事件的五种策略
- [CON-rescue-medication](concepts/CON-rescue-medication.md) — 救援药物的定义、典型例子及在 SDTM CM / ADaM 中的落地
- [GOT-ice-reason-collection](gotchas/GOT-ice-reason-collection.md) — 停药原因收集含糊会让按原因分配 ICE 策略落不了地
- [REF-ICH-E9R1](references/REF-ICH-E9R1.md) — ICH E9(R1) estimand 与敏感性分析（同时支撑第 6 章）

## 2. 统计推断核心概念

### 2.1 推断基础与核心假设

- [CON-null-hypothesis](concepts/CON-null-hypothesis.md) — H₀ 的四要素（终点、人群、参数、方向）、不同终点的写法、非劣效 H₀、须事先指定
- [CON-degrees-of-freedom](concepts/CON-degrees-of-freedom.md) — 自由度的含义、方差分母为何是 n − 1、临界 t 值随 df 变化、常见检验的 df
- [CON-type-I-II-error](concepts/CON-type-I-II-error.md) — 第一类错误（α）与第二类错误（β）、power = 1 − β、影响 β 的因素、多重比较使 α 膨胀、不显著 ≠ 无效

### 2.2 核心统计量与分布族

- [CON-test-statistic](concepts/CON-test-statistic.md) — 检验统计量的共同骨架；t、χ²、log-rank 各适用什么数据，以及它们的"亲戚关系"
- [CON-distribution-family](concepts/CON-distribution-family.md) — 伯努利 → 二项 → 正态 → Z → t / χ² / F 的演化关系、各分布特点；F = 组间 / 组内变异及其用途（ANOVA、Type III 检验）
- [CON-normal-distribution](concepts/CON-normal-distribution.md) — 标准正态 N(0, 1) 只有一条、μ 定位置 σ 定胖瘦、标准化 z = (x − μ) / σ；1.96 是 97.5% 分位数及其数值求法（`qnorm`、`integrate` + `uniroot`）；1.96 vs t 临界值
- [CON-t-distribution](concepts/CON-t-distribution.md) — t 分布只由自由度决定、随 df 的形状变化、与正态分布对比

### 2.3 检验方法的选择与计算

- [CON-p-value](concepts/CON-p-value.md) — P 值的定义、四个必备要素、零分布的前提假设、非参数 / 置换 / 精确检验；计算四步、Python / R / SAS 实现、怎么解读
- [CON-test-selection](concepts/CON-test-selection.md) — 快速选择表（连续 / 分类 / 非参数 × 两组 / 多组 / 配对）；t、ANOVA、卡方、Fisher、Mann-Whitney、Kruskal-Wallis 的适用条件、临床例子与 R 代码；怎么判断正态
- [CON-confirmatory-methods-overview](concepts/CON-confirmatory-methods-overview.md) — 导航页：确证性试验最常用的十种方法（ANCOVA、MMRM、KM、log-rank、Cox、CMH、logistic、Fisher、卡方、Wilcoxon）、按治疗领域的分布、描述统计占 TLF 大头、SAS / R 对齐重点
- [CON-parametric-vs-nonparametric](concepts/CON-parametric-vs-nonparametric.md) — 参数方法（假设分布、比较参数）vs 非参数方法（基于秩次、分布无关）：优缺点、秩次为何对离群值稳健、对应关系、"非参数 ≠ 无假设"
- [CON-t-test-pvalue](concepts/CON-t-test-pvalue.md) — t 检验 / t 值 / t 分布的区别、t 值 = 信噪比（SE 与 n、SD 的关系）、t 检验五步流程、怎么读 t 值、t vs z、SAS PROC TTEST 四张输出表
- [GOT-ttest-student-vs-welch](gotchas/GOT-ttest-student-vs-welch.md) — 同一数据 Python / R / SAS 的 t 检验 P 值不同：Student（等方差）vs Welch（不等方差）默认设置；n 不等时差异可达数十倍；为什么不建议先检验方差齐性再选

### 2.4 常见误区与结果解读

- [CON-confidence-interval](concepts/CON-confidence-interval.md) — 95% CI 与双侧 α = 0.05 检验的等价关系、0（或 1）在不在 CI 内、不显著 ≠ 没差别、结果报告示例
- [GOT-skewed-small-sample](gotchas/GOT-skewed-small-sample.md) — 小样本偏态（CRP 例子）：均值本身不可靠，Welch 也救不了；log 转换（几何均数比）或 Mann-Whitney；方法须预先指定

待建：P 值的常见误解（2.4）、单侧 vs 双侧检验辨析（2.4）

## 3. 连续型终点：ANCOVA → MMRM

- [CON-covariate](concepts/CON-covariate.md) — 协变量是什么、为什么调整（降低噪音提高功效、校正组间不平衡）、ANOVA → ANCOVA、常见协变量（基线值、分层因素）、须预先指定
- [CON-MMRM](concepts/CON-MMRM.md) — 重复测量混合模型：设定、SAS/R 实现、TLF 呈现
- [GOT-mmrm-convergence](gotchas/GOT-mmrm-convergence.md) — UN 协方差不收敛时的预设备选顺序

待建：ANCOVA 独立卡片（LS mean、模型假设、SAS / R 实现）、ANCOVA 与 MMRM 的关系

## 4. 二分类终点：CMH、logistic、率差置信区间

- [CON-ordinal-data](concepts/CON-ordinal-data.md) — 有序分类数据：能排序但不能做算术；临床例子（CTCAE、RECIST、mRS、CGI）；描述用 n (%)，比较用 CMH（row mean scores）/ Wilcoxon / proportional odds model；多级总分量表常当连续处理
- [CON-CMH](concepts/CON-CMH.md) — PROC FREQ 的 CMH 三个统计量怎么选（Nonzero Correlation / Row Mean Scores / General Association）、`SCORES=` 选项（table、rank ≈ Kruskal-Wallis / Wilcoxon、modridit = van Elteren）、行列顺序与排序注意事项
- [CON-proportional-odds-model](concepts/CON-proportional-odds-model.md) — 比例优势模型（有序 logistic）：累积 logit、共同 OR；比例优势假设的 score test 及其局限、partial PO（`UNEQUALSLOPES` / `nominal =`）；R（polr / clm）与 SAS 实现
- [GOT-ordinal-or-direction](gotchas/GOT-ordinal-or-direction.md) — SAS 默认对 P(Y ≤ k) 建模、R polr / clm 参数化带减号，OR 互为倒数；看 "Probabilities modeled…" 那行；加不加 `DESCENDING` 取决于哪端是好结局

待建：CMH 用于二分类（共同 OR / RR、MH 率差、Breslow-Day）、logistic 回归与 odds ratio、率差（risk difference）置信区间方法（Wald、Newcombe、Miettinen-Nurminen）、单组率的 Clopper-Pearson 精确 CI（单臂试验 ORR）、非应答者填补（NRI）

## 5. 生存分析：KM、log-rank、Cox

- [CON-hazard-ratio](concepts/CON-hazard-ratio.md) — HR 的含义、HR = 1 作为 H₀、报告怎么读、HR ≠ 事件人数比例
- [CON-logrank-vs-cox](concepts/CON-logrank-vs-cox.md) — log-rank（曲线相同、给 P 值）与 Cox（HR = 1、给 HR 和 CI）的 H₀、分工与 SAS 代码

待建：Kaplan-Meier、Cox 模型细节（分层、协变量、ties）、比例风险假设检验方法、删失（censoring）规则

## 6. 缺失数据与敏感性分析

- [CON-missing-data](concepts/CON-missing-data.md) — MCAR/MAR/MNAR 定义与例子、因 AE 停药的归类、策略与插补方法（J2R、retrieved dropout）、tipping point
- [CON-sensitivity-analysis](concepts/CON-sensitivity-analysis.md) — 敏感性分析的定义、典型组合，及与补充分析（per-protocol、完成者分析）的区别

待建：multiple imputation 实现细节、reference-based MI（J2R、CR）独立卡片、tipping point 实现、模式混合模型（pattern mixture model）、retrieved dropout 插补

## 7. 多重性

（暂无卡片）

待建：Bonferroni、Holm、Hochberg、gatekeeping、graphical approach

## 8. 样本量与成组序贯设计

- [CON-sample-size-power](concepts/CON-sample-size-power.md) — power 与样本量计算：两个钟形曲线、输入（α、power、δ、σ）、n 公式手算、δ（假设的治疗差值）的选择与 MCID、δ 减半 n 变 4 倍、post-hoc power 误区、生存终点看事件数
- [GOT-ni-hypothesis-direction](gotchas/GOT-ni-hypothesis-direction.md) — 非劣效 H₀ 的 ≤ / ≥ 取决于终点"好"的方向；CI 上限 / 下限与 Δ 的比较

待建：二分类与生存终点的样本量公式、非劣效界值 Δ 的确定、期中分析与 alpha spending（O'Brien-Fleming、Pocock、Lan-DeMets）

## 大纲外主题

暂不属于以上 8 章的主题先放这里，后续再决定归属。

- [CON-dose-escalation-design](concepts/CON-dose-escalation-design.md) — 一期剂量递增设计：MTD 与目标毒性率；3+3（规则）、CRM / BLRM / EWOC（模型）、BOIN（模型辅助，查表执行）对比；Project Optimus；一期其他统计分析与 R 包

待建：亚组分析与森林图、计数终点的负二项回归（如呼吸领域急性加重率）、一期 PK 统计（NCA、剂量比例性 power model、浓度-QTc）
