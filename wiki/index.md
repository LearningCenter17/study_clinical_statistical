---
title: 知识库索引
---

按学习大纲分章列出所有卡片（各类卡片混排：CON 概念、MTH 方法、WF 流程、CODE 代码、TLF 呈现、GOT 坑、REF 文献；左侧边栏则按主题文件夹排列）。新增或删除卡片时同步更新本页。
每章末尾的"待建"是该章还没有卡片的主题，建好后从这里删掉。

## 1. 估计目标（Estimand）框架

先建立"分析到底在回答什么问题"的视角。

- [CON-estimand](cards/estimand/CON-estimand.md) — 估计目标的五个属性与伴发事件的五种策略
- [CON-rescue-medication](cards/estimand/CON-rescue-medication.md) — 救援药物的定义、典型例子及在 SDTM CM / ADaM 中的落地
- [GOT-ice-reason-collection](cards/estimand/GOT-ice-reason-collection.md) — 停药原因收集含糊会让按原因分配 ICE 策略落不了地
- [REF-ICH-E9R1](cards/regulatory/REF-ICH-E9R1.md) — ICH E9(R1) estimand 与敏感性分析（同时支撑第 6 章）

## 2. 统计推断核心概念

### 2.1 推断基础与核心假设

- [CON-null-hypothesis](cards/inference/CON-null-hypothesis.md) — H₀ 的四要素（终点、人群、参数、方向）、不同终点的写法、非劣效 H₀、须事先指定
- [CON-degrees-of-freedom](cards/inference/CON-degrees-of-freedom.md) — 自由度的含义、方差分母为何是 n − 1、临界 t 值随 df 变化、常见检验的 df
- [CON-type-I-II-error](cards/inference/CON-type-I-II-error.md) — 第一类错误（α）与第二类错误（β）、power = 1 − β、影响 β 的因素、多重比较使 α 膨胀、不显著 ≠ 无效

### 2.2 核心统计量与分布族

- [CON-test-statistic](cards/inference/CON-test-statistic.md) — 检验统计量的共同骨架；t、χ²、log-rank 各适用什么数据，以及它们的"亲戚关系"
- [CON-distribution-family](cards/inference/CON-distribution-family.md) — 伯努利 → 二项 → 正态 → Z → t / χ² / F 的演化关系、各分布特点；F = 组间 / 组内变异及其用途（ANOVA、Type III 检验）
- [CON-normal-distribution](cards/inference/CON-normal-distribution.md) — 标准正态 N(0, 1) 只有一条、μ 定位置 σ 定胖瘦、标准化 z = (x − μ) / σ；1.96 是 97.5% 分位数及其数值求法（`qnorm`、`integrate` + `uniroot`）；1.96 vs t 临界值
- [CON-t-distribution](cards/inference/CON-t-distribution.md) — t 分布只由自由度决定、随 df 的形状变化、与正态分布对比

### 2.3 检验方法的选择与计算

- [CON-p-value](cards/inference/CON-p-value.md) — P 值的定义、四个必备要素、零分布的前提假设、非参数 / 置换 / 精确检验；计算四步、z 检验手算示例、各检验的参照分布与 R 函数（pnorm / pt / pf / pchisq）、Python / R / SAS 实现、怎么解读
- [CON-test-selection](cards/inference/CON-test-selection.md) — 快速选择表（连续 / 分类 / 非参数 × 两组 / 多组 / 配对）；t、ANOVA、卡方、Fisher、Mann-Whitney、Kruskal-Wallis 的适用条件、临床例子与 R 代码；怎么判断正态
- [CON-confirmatory-methods-overview](cards/methods/CON-confirmatory-methods-overview.md) — 导航页：确证性试验最常用的十种方法（ANCOVA、MMRM、KM、log-rank、Cox、CMH、logistic、Fisher、卡方、Wilcoxon）、按治疗领域的分布、描述统计占 TLF 大头、SAS / R 对齐重点
- [CON-parametric-vs-nonparametric](cards/inference/CON-parametric-vs-nonparametric.md) — 参数方法（假设分布、比较参数）vs 非参数方法（基于秩次、分布无关）：优缺点、秩次为何对离群值稳健、对应关系、秩和检验中英术语对照（rank-sum vs signed-rank、R 的 W 即 U）、"非参数 ≠ 无假设"
- [MTH-t-test](cards/methods/continuous/MTH-t-test.md) — t 检验 / t 值 / t 分布的区别、t 值 = 信噪比（SE 与 n、SD 的关系）、t 检验五步流程、怎么读 t 值、t vs z、t 与 P 一一对应的条件（df + 单 / 双侧）及报告写法 t(df) = …，P = …、SAS PROC TTEST 四张输出表
- [GOT-ttest-student-vs-welch](cards/methods/continuous/GOT-ttest-student-vs-welch.md) — 同一数据 Python / R / SAS 的 t 检验 P 值不同：Student（等方差）vs Welch（不等方差）默认设置；n 不等时差异可达数十倍；为什么不建议先检验方差齐性再选

### 2.4 常见误区与结果解读

- [CON-confidence-interval](cards/inference/CON-confidence-interval.md) — CI 的定义与三个组成部分（估计值 ± 临界值 × SE）；1.96 vs t 临界值、不同统计量的 CI 构造（均值用 t、比例用精确 / score 法、HR / OR 在 log 尺度用 z）；"95%"的正确含义（重复试验的覆盖率，套圈类比）；置信区间 vs 贝叶斯可信区间（CrI）；CI 宽度由什么决定（SD、n、方法、率大小；生存终点看事件数 SE ≈ 2/√D）、窄 CI ≠ 结论可靠；95% CI 与双侧 α = 0.05 检验的等价关系、0（或 1）在不在 CI 内、不显著 ≠ 没差别、结果报告示例
- [GOT-skewed-small-sample](cards/methods/continuous/GOT-skewed-small-sample.md) — 小样本偏态（CRP 例子）：均值本身不可靠，Welch 也救不了；log 转换（几何均数比）或 Mann-Whitney；方法须预先指定

待建：P 值的常见误解（2.4）、单侧 vs 双侧检验辨析（2.4）

## 3. 连续型终点：ANCOVA → MMRM

- [CON-covariate](cards/methods/continuous/CON-covariate.md) — 协变量是什么、为什么调整（降低噪音提高功效、校正组间不平衡）、ANOVA → ANCOVA、常见协变量（基线值、分层因素）、须预先指定
- [MTH-MMRM](cards/methods/continuous/MTH-MMRM.md) — 重复测量混合模型：设定、SAS/R 实现、TLF 呈现
- [GOT-mmrm-convergence](cards/methods/continuous/GOT-mmrm-convergence.md) — UN 协方差不收敛时的预设备选顺序

待建：ANCOVA 独立卡片（LS mean、模型假设、SAS / R 实现）、ANCOVA 与 MMRM 的关系

## 4. 二分类终点：CMH、logistic、率差置信区间

- [CON-response-rate](cards/methods/binary/CON-response-rate.md) — 应答的定义与各领域标准（RECIST、ACR20、PASI 75）；应答概率 p（真值）vs 应答率 p̂（估计）、ORR 与 CI 示例；RECIST 1.1 判定 PR / CR 的三个条件与确认（confirmation）；抛硬币 / `rbinom` 类比；同样适用于 AE 发生率；中英术语（response rate、responder analysis）、ASAS40 定义；ADRS 参数（OVRLRESP / BOR / CBOR）与 ORR 算法
- [CON-ordinal-data](cards/methods/ordinal/CON-ordinal-data.md) — 有序分类数据：能排序但不能做算术；临床例子（CTCAE、RECIST、mRS、CGI）；描述用 n (%)，比较用 CMH（row mean scores）/ Wilcoxon / proportional odds model；多级总分量表常当连续处理
- [MTH-CMH](cards/methods/binary/MTH-CMH.md) — PROC FREQ 的 CMH 三个统计量怎么选（Nonzero Correlation / Row Mean Scores / General Association）、`SCORES=` 选项（table、rank ≈ Kruskal-Wallis / Wilcoxon、modridit = van Elteren）、行列顺序与排序注意事项
- [MTH-proportional-odds-model](cards/methods/ordinal/MTH-proportional-odds-model.md) — 比例优势模型（有序 logistic）：累积 logit、共同 OR；比例优势假设的 score test 及其局限、partial PO（`UNEQUALSLOPES` / `nominal =`）；R（polr / clm）与 SAS 实现
- [GOT-ordinal-or-direction](cards/methods/ordinal/GOT-ordinal-or-direction.md) — SAS 默认对 P(Y ≤ k) 建模、R polr / clm 参数化带减号，OR 互为倒数；看 "Probabilities modeled…" 那行；加不加 `DESCENDING` 取决于哪端是好结局

待建：CMH 用于二分类（共同 OR / RR、MH 率差、Breslow-Day）、logistic 回归与 odds ratio、率差（risk difference）置信区间方法（Wald、Newcombe、Miettinen-Nurminen）、单组率的 Clopper-Pearson 精确 CI（单臂试验 ORR）、非应答者填补（NRI）

## 5. 生存分析：KM、log-rank、Cox

- [CON-hazard-ratio](cards/methods/tte/CON-hazard-ratio.md) — HR 的含义（瞬时速率之比）、HR = 1 作为 H₀；为什么在 log 尺度分析；CI 与 Wald P 值算例、CI 不对称及 TLF QC（log 尺度等距、四舍五入导致的偏差、用全精度 β / SE 反算比对）；报告怎么读、HR ≠ 事件人数比例；R `summary(coxph)` 输出列对照
- [CON-logrank-vs-cox](cards/methods/tte/CON-logrank-vs-cox.md) — log-rank（曲线相同、给 P 值）与 Cox（HR = 1、给 HR 和 CI）的 H₀、分工、P 值与 CI 偶尔不一致的原因；SAS / R（分层 coxph、survdiff）代码

待建：Kaplan-Meier、Cox 模型细节（分层、协变量、ties）、比例风险假设检验方法、删失（censoring）规则

## 6. 缺失数据与敏感性分析

- [CON-missing-data](cards/missing-data/CON-missing-data.md) — MCAR/MAR/MNAR 定义与例子、因 AE 停药的归类、策略与插补方法（J2R、retrieved dropout）、tipping point
- [CON-sensitivity-analysis](cards/missing-data/CON-sensitivity-analysis.md) — 敏感性分析的定义、典型组合，及与补充分析（per-protocol、完成者分析）的区别

待建：multiple imputation 实现细节、reference-based MI（J2R、CR）独立卡片、tipping point 实现、模式混合模型（pattern mixture model）、retrieved dropout 插补

## 7. 多重性

（暂无卡片）

待建：Bonferroni、Holm、Hochberg、gatekeeping、graphical approach

## 8. 样本量与成组序贯设计

- [CON-sample-size-power](cards/design/CON-sample-size-power.md) — power 与样本量计算的概念：两个钟形曲线、需要哪些输入及从哪来、术语（sample size determination / justification）；δ（假设的治疗差值）的选择与 MCID、δ 减半 n 变 4 倍；post-hoc power 等常见误区；多重性、期中分析、分层对样本量的影响
- [WF-sample-size-calc](cards/design/WF-sample-size-calc.md) — 样本量计算的步骤；连续终点手算例子与 84 / 85 / 86 人的来源（向上取整、精确分位数、t 分布）；脱落调整；二分类公式、Schoenfeld 事件数公式；R（power.t.test、power.prop.test、gsDesign::nSurv）、SAS PROC POWER
- [CON-ni-sample-size](cards/design/CON-ni-sample-size.md) — 非劣效样本量：Δ = 真实差异到 H₀ 边界的距离（越高越好时 δ + M）；符号写反人数差好几倍且 δ = 0 时不暴露；SAS nullmeandiff / sides、R 写法
- [CON-unequal-allocation](cards/design/CON-unequal-allocation.md) — 不等分配 k:1：连续终点公式与 2:1 共 192 人例子；总人数是 1:1 的 (1 + k)² / 4k 倍；生存终点系数；二分类 ASAS40 1:2 算例、Fleiss 连续性校正、脱落调整与方案写法
- [GOT-ni-hypothesis-direction](cards/design/GOT-ni-hypothesis-direction.md) — 非劣效 H₀ 的 ≤ / ≥ 取决于终点"好"的方向；CI 上限 / 下限与 Δ 的比较
- [CON-stratified-randomization](cards/design/CON-stratified-randomization.md) — 分层随机化不增加样本量（样本量为合并后的整体比较而算）；分层什么时候真正有用（大样本下大不均衡本就罕见；小样本、亚组、analyze as randomized、提高精确度）；过度分层的三个真正问题（不完整区组致均衡变差、稀疏单元格、误分层）；限制层数、合并类别、minimization、协变量调整；总层数 ≪ N / 区组大小；亚组须单独证明疗效时才加人
- [CON-prognostic-factor](cards/design/CON-prognostic-factor.md) — 预后因素（不论治疗都影响结局的基线特征）的例子与判断依据；强预后因素为何要分层（分期不均衡扭曲疗效的例子）；预后因素 vs 预测因素（HER2）及各自在设计中的用途

待建：事件数换算成总人数（入组 / 随访 / 脱落假设）、非劣效界值 Δ 的确定、期中分析与 alpha spending（O'Brien-Fleming、Pocock、Lan-DeMets）

## 大纲外主题

暂不属于以上 8 章的主题先放这里，后续再决定归属。

- [CON-dose-escalation-design](cards/design/CON-dose-escalation-design.md) — 一期剂量递增设计：MTD 与目标毒性率；3+3（规则）、CRM / BLRM / EWOC（模型）、BOIN（模型辅助，查表执行）对比；Project Optimus；一期其他统计分析与 R 包

待建：亚组分析与森林图、计数终点的负二项回归（如呼吸领域急性加重率）、一期 PK 统计（NCA、剂量比例性 power model、浓度-QTc）
