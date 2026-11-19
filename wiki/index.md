---
title: 知识库索引
---

按学习大纲分章列出所有卡片（各类卡片混排：CON 概念、MTH 方法、WF 流程、CODE 代码、TLF 呈现、GOT 坑、REF 文献；左侧边栏则按主题文件夹排列）。新增或删除卡片时同步更新本页。
每章末尾的"待建"是该章还没有卡片的主题，建好后从这里删掉。

- 卡片状态 `draft` = 未核对，`reviewed` = 已对照原始出处核对。
- 新知识：放入 `inbox/`，在 Claude Code 中运行 `/kb-ingest`。
- 中英术语对照见 [术语表](glossary.md)；按终点类型选检验方法见 [检验方法选择树](decision-tree.md)。

## 1. 估计目标（Estimand）框架

先建立"分析到底在回答什么问题"的视角。

- [CON-estimand](cards/estimand/CON-estimand.md) — 估计目标的五个属性与伴发事件的五种策略
- [CON-rescue-medication](cards/estimand/CON-rescue-medication.md) — 救援药物的定义、典型例子及在 SDTM CM / ADaM 中的落地
- [GOT-ice-reason-collection](cards/estimand/GOT-ice-reason-collection.md) — 停药原因收集含糊会让按原因分配 ICE 策略落不了地
- [REF-ICH-E9R1](cards/regulatory/REF-ICH-E9R1.md) — ICH E9(R1) estimand 与敏感性分析（同时支撑第 6 章）

## 2. 统计推断核心概念

### 2.1 推断基础与核心假设

- [CON-null-hypothesis](cards/inference/CON-null-hypothesis.md) — H₀ 的四要素（终点、人群、参数、方向）、不同终点的写法、非劣效 H₀、须事先指定
- [CON-degrees-of-freedom](cards/inference/CON-degrees-of-freedom.md) — 自由度的含义、方差分母为何是 n − 1、df 决定零分布形状、常见检验的 df（临界值表见 CON-t-distribution）
- [CON-type-I-II-error](cards/inference/CON-type-I-II-error.md) — 第一类错误（α）与第二类错误（β）、power = 1 − β、影响 β 的因素、多重比较使 α 膨胀、不显著 ≠ 无效

### 2.2 核心统计量与分布族

- [CON-test-statistic](cards/inference/CON-test-statistic.md) — 检验统计量的共同骨架；t、χ²、log-rank 各适用什么数据，以及它们的"亲戚关系"；**统计量与零分布总表**（z / t / F / χ² 各用哪个分布、用于哪些检验、R 求 P 值的函数 pnorm / pt / pf / pchisq）
- [CON-distribution-family](cards/inference/CON-distribution-family.md) — 伯努利 → 二项 → 正态 → Z → t / χ² / F 的演化关系、各分布特点；F = 组间 / 组内变异及其用途（ANOVA、Type III 检验）
- [CON-normal-distribution](cards/inference/CON-normal-distribution.md) — 标准正态 N(0, 1) 只有一条、μ 定位置 σ 定胖瘦、标准化 z = (x − μ) / σ；1.96 是 97.5% 分位数及其数值求法（`qnorm`、`integrate` + `uniroot`）；1.96 vs t 临界值
- [CON-t-distribution](cards/inference/CON-t-distribution.md) — t 分布只由自由度决定、随 df 的形状变化；**各 df 的临界值与 t = 2 时 P 值对照表**；t 与 z 的区别（σ 未知、Gosset）及"n ≥ 30 当 Z 用"的分歧；与正态分布对比
- [CON-chi-square-distribution](cards/inference/CON-chi-square-distribution.md) — 卡方分布 = 独立标准正态的平方和；Z² 的均值 1、95% 分位数 1.96² = 3.84，自由度 = 独立项个数（df 2 → 5.99）；卡方检验每项 (O − E)/√E ≈ Z 的由来、期望值 ≥ 5 的原因、2×2 表 4 项只有 1 个自由度；R 模拟

### 2.3 检验方法的选择与计算

- [CON-p-value](cards/inference/CON-p-value.md) — P 值的定义、四个必备要素、零分布的前提假设、非参数 / 置换 / 精确检验；计算四步、z 检验手算示例、标准化不是数学上必须的、怎么解读
- [CON-test-selection](cards/inference/CON-test-selection.md) — t、ANOVA、卡方、Fisher、Mann-Whitney、Kruskal-Wallis 的适用条件、临床例子与 R 代码；怎么判断正态；怎么选见 [检验方法选择树](decision-tree.md)
- [CON-confirmatory-methods-overview](cards/methods/CON-confirmatory-methods-overview.md) — 导航页：确证性试验最常用的十种方法（ANCOVA、MMRM、KM、log-rank、Cox、CMH、logistic、Fisher、卡方、Wilcoxon）、按治疗领域的分布、描述统计占 TLF 大头、SAS / R 对齐重点
- [CON-continuity-correction](cards/inference/CON-continuity-correction.md) — 连续性校正：用连续分布近似离散计数时的"半格"修正（|O − E| − 0.5）；抛硬币例子（0.029 vs 0.057 vs 精确 0.0547）、2×2 表 Yates 校正、要不要用的争议（大样本不校正、小样本用 Fisher）；七个使用场景（卡方、CMH、两比率 z、比例 CI、McNemar 减 1、Wilcoxon、样本量 Fleiss）与不需要校正的方法
- [CON-parametric-vs-nonparametric](cards/inference/CON-parametric-vs-nonparametric.md) — 参数方法（假设分布、比较参数）vs 非参数方法（基于秩次、分布无关）：优缺点、秩次为何对离群值稳健、对应关系、秩和检验中英术语对照（rank-sum vs signed-rank、R 的 W 即 U）、"非参数 ≠ 无假设"
- [MTH-t-test](cards/methods/continuous/MTH-t-test.md) — t 检验 / t 值 / t 分布的区别、t 值 = 信噪比（SE 与 n、SD 的关系）、t 检验五步流程、怎么读 t 值、t 与 P 的对应（t 越大 P 越小、df 影响翻译、一一对应的条件）及报告写法 t(df) = …，P = …
- [CODE-ttest-sas-r-python](cards/methods/continuous/CODE-ttest-sas-r-python.md) — t 检验的 SAS / R / Python 代码：同一组数据三种软件的写法及 P 值为何不同（Student vs Welch 默认）、项目数据（ADEFF）写法、SAS PROC TTEST 四张输出表与 ODS 抽取 QC
- [GOT-ttest-student-vs-welch](cards/methods/continuous/GOT-ttest-student-vs-welch.md) — 同一数据 Python / R / SAS 的 t 检验 P 值不同：Student（等方差）vs Welch（不等方差）默认设置；n 不等时差异可达数十倍；为什么不建议先检验方差齐性再选

### 2.4 常见误区与结果解读

- [CON-confidence-interval](cards/inference/CON-confidence-interval.md) — CI 的定义与三个组成部分（估计值 ± 临界值 × SE）；"95%"的正确含义（重复试验的覆盖率，套圈类比）；95% CI 与双侧 α = 0.05 检验的等价关系、0（或 1）在不在 CI 内、不显著 ≠ 没差别、结果报告示例
- [MTH-ci-construction](cards/inference/MTH-ci-construction.md) — CI 怎么构造：1.96 vs t 临界值（小样本用 1.96 覆盖率不足）；不同统计量的方法（均值用 t、比例用 Clopper-Pearson / Wilson / Newcombe、HR / OR 在 log 尺度用 z）及 HR 算例
- [CON-credible-interval](cards/inference/CON-credible-interval.md) — 置信区间 vs 贝叶斯可信区间（CrI）：两派对"概率"的理解、先验与后验、27/60 应答率的两种区间（`binom.test` vs `qbeta`）、临床试验中何时用 CrI 及 CSR 的规范写法
- [CON-ci-width](cards/inference/CON-ci-width.md) — CI 宽度由什么决定（SD、n、置信水平、分析方法、率的大小、事件数）；生存终点看事件数 SE(log HR) ≈ 2/√D；窄 CI ≠ 结论可靠（偏倚、临床意义）
- [GOT-skewed-small-sample](cards/methods/continuous/GOT-skewed-small-sample.md) — 小样本偏态（CRP 例子）：均值本身不可靠，Welch 也救不了；log 转换（几何均数比）或 Mann-Whitney；方法须预先指定

待建：P 值的常见误解（2.4）、单侧 vs 双侧检验辨析（2.4）

## 3. 连续型终点：ANCOVA → MMRM

- [CON-regression](cards/methods/CON-regression.md) — 回归是什么：回归系数与预测、因变量 / 自变量；临床试验中 β₁ = 校正后的治疗效应（ANCOVA、MMRM 本质都是回归）；名字来自 Galton 的回归均值；按结局分家族（线性 → 均值差、logistic → OR、泊松 / 负二项 → 率比、Cox → HR）；普通回归 = OLS 线性回归
- [CON-covariate](cards/methods/continuous/CON-covariate.md) — 协变量是什么、为什么调整（降低噪音提高功效、校正组间不平衡）、ANOVA → ANCOVA、常见协变量（基线值、分层因素）、须预先指定
- [MTH-MMRM](cards/methods/continuous/MTH-MMRM.md) — 重复测量混合模型：设定、SAS/R 实现、TLF 呈现
- [GOT-mmrm-convergence](cards/methods/continuous/GOT-mmrm-convergence.md) — UN 协方差不收敛时的预设备选顺序

待建：ANCOVA 独立卡片（LS mean、模型假设、SAS / R 实现）、ANCOVA 与 MMRM 的关系

## 4. 二分类终点：CMH、logistic、率差置信区间

- [CON-response-rate](cards/methods/binary/CON-response-rate.md) — 应答的定义与各领域标准（RECIST、ACR20、PASI 75）；应答概率 p（真值）vs 应答率 p̂（估计）、ORR 与 CI 示例；RECIST 1.1 判定 PR / CR 的三个条件与确认（confirmation）；抛硬币 / `rbinom` 类比；同样适用于 AE 发生率；中英术语（response rate、responder analysis）、ASAS40 定义；ADRS 参数（OVRLRESP / BOR / CBOR）与 ORR 算法
- [CON-ordinal-data](cards/methods/ordinal/CON-ordinal-data.md) — 有序分类数据：能排序但不能做算术；临床例子（CTCAE、RECIST、mRS、CGI）；描述用 n (%)，比较用 CMH（row mean scores）/ Wilcoxon / proportional odds model；多级总分量表常当连续处理
- [CON-odds-ratio](cards/methods/binary/CON-odds-ratio.md) — odds 与概率的换算；OR = 两组 odds 之比 = ad / bc（交叉乘积比）、怎么解读；与率差 RD、相对危险度 RR 的区别（80% vs 70%：RD 10%、RR 1.14、OR 1.71，OR ≠ "可能性是几倍"，罕见事件时 OR ≈ RR）；为什么常用 OR（logistic、对称性、CMH）；TLF 报告与 R / SAS 代码
- [MTH-chi-square](cards/methods/binary/MTH-chi-square.md) — 卡方检验（Pearson χ²）：名字由来、独立性检验与拟合优度检验、2×2 表逐格手算 (O − E)² / E（χ² = 9.09，df = 1，p = 0.0026）、为什么要除以 E、R 复核与 Yates 校正
- [GOT-continuity-correction-r-vs-sas](cards/methods/binary/GOT-continuity-correction-r-vs-sas.md) — 双编程 P 值对不上：R 的 `chisq.test` / `mantelhaen.test` / `prop.test` / `mcnemar.test` / `wilcox.test` 默认校正，SAS PROC FREQ 大多不校正（CHISQ 两种都输出、CMH / AGREE / BINOMIAL / RISKDIFF 不校正），NPAR1WAY 例外；R 用 `correct = FALSE` 对齐
- [MTH-CMH](cards/methods/binary/MTH-CMH.md) — 二分类：分层比较应答率的思路、辛普森悖论算例（不分层 OR 0.57 vs CMH 合并 OR 1.63）、各层效应一致的前提与 Breslow-Day、SAS / R 写法（`correct = FALSE`）；有序：PROC FREQ 的 CMH 三个统计量怎么选（Nonzero Correlation / Row Mean Scores / General Association）、`SCORES=` 选项（table、rank ≈ Kruskal-Wallis / Wilcoxon、modridit = van Elteren）、行列顺序与排序注意事项
- [MTH-breslow-day](cards/methods/binary/MTH-breslow-day.md) — 各层 OR 同质（homogeneity）是 CMH 合并的前提；正例（OR 1.71 / 1.56）vs 反例（OR 4.0 / 0.29 → CMH = 0、OR_MH = 1，效应互相抵消）；BD 统计量（实际 vs 按 OR_MH 倒推的期望 aₖ，χ²(K − 1)）、量的 vs 质的交互、效能低常用 α = 0.10、不作门槛、Tarone 校正（SAS `BDT`、R DescTools）
- [MTH-proportional-odds-model](cards/methods/ordinal/MTH-proportional-odds-model.md) — 比例优势模型（有序 logistic）：累积 logit、共同 OR；比例优势假设的 score test 及其局限、partial PO（`UNEQUALSLOPES` / `nominal =`）；R（polr / clm）与 SAS 实现
- [GOT-ordinal-or-direction](cards/methods/ordinal/GOT-ordinal-or-direction.md) — SAS 默认对 P(Y ≤ k) 建模、R polr / clm 参数化带减号，OR 互为倒数；看 "Probabilities modeled…" 那行；加不加 `DESCENDING` 取决于哪端是好结局

待建：CMH 的 MH 率差与 RR、logistic 回归、率差（risk difference）置信区间方法（Wald、Newcombe、Miettinen-Nurminen）、单组率的 Clopper-Pearson 精确 CI（单臂试验 ORR）、非应答者填补（NRI）

## 5. 生存分析：KM、log-rank、Cox

- [CON-survival-analysis-overview](cards/methods/tte/CON-survival-analysis-overview.md) — 导航页：生存分析的别名、常见事件定义（OS、PFS、TTAE、至起效时间等，事件不一定是坏事）、删失（右 / 左 / 区间）、S(t) / h(t) / H(t) / 中位生存 / 在险人数；KM、log-rank、Cox 各管什么；PH 不成立时（RMST、分段 / 时变 Cox、加权 log-rank、MaxCombo、参数模型）；竞争风险（CIF、Gray、Fine–Gray）、非信息性删失、estimand；普通回归为什么处理不了删失、用似然（事件者贡献密度、删失者贡献 S(t)）改造；ADTTE 变量与 CNSR 方向、R `survival` / `tern` 代码、SAS vs R 的 CI 变换与 ties 默认
- [MTH-kaplan-meier](cards/methods/tte/MTH-kaplan-meier.md) — 6 人算例逐步手算 KM（在险 6 / 4 / 2、S = 0.833 / 0.625 / 0.313）；在险集规则（观测时间 ≥ t，事件 / 删失那一刻仍计入）；删失不让曲线下降但减少分母、在险少时 1 个事件让曲线减半；在险人数决定曲线可信度、暴露两组随访是否均衡、是 log-rank / Cox 的计算基础；number at risk 表（`tern::g_km`、`add_risktable`、`n.risk` QC）；闯关相乘与公式 ∏(1 − dᵢ/nᵢ)；含并列死亡的第二个算例（3, 5+, 6, 6, 9+, 12 → S = 0.833 / 0.417 / 0）；中位生存与 NR、Greenwood 方差、非信息性删失前提
- [CON-km-logrank-cox-example](cards/methods/tte/CON-km-logrank-cox-example.md) — 三件套各答什么问题（KM 描述 / log-rank 检验 / Cox 估计，类比均值 / t 检验 / 回归），TLF 生存表 = KM 中位 + log-rank p + Cox HR；两组 10 人串算：KM（A 组中位 NR、B 组 6 个月）、log-rank 逐时刻实际 vs 预期（A 实际 2、预期 3.93，χ² 3.35，p 0.067）、Cox HR 0.17（0.02–1.53）、Wald p 0.11
- [CON-censoring](cards/methods/tte/CON-censoring.md) — 删失的定义；常见原因（行政删失、失访、撤回同意、按 SAP 规则主动删失，如 PFS 中开始新抗肿瘤治疗）；删失日期取"最后一次能确认事件未发生"的日期（OS 最后确认存活、PFS 最后一次充分肿瘤评估）；ADTTE 中 CNSR（1 及以上区分删失原因）/ ADT / EVNTDESC / CNSDTDSC，先把 SAP 规则整理成表；右 / 区间 / 左删失，KM 只能处理右删失
- [CON-hazard-ratio](cards/methods/tte/CON-hazard-ratio.md) — HR 的含义（瞬时速率之比）、HR = 1 作为 H₀；为什么在 log 尺度分析；CI 与 Wald P 值算例、CI 不对称及 TLF QC（log 尺度等距、四舍五入导致的偏差、用全精度 β / SE 反算比对）；报告怎么读、HR ≠ 事件人数比例；R `summary(coxph)` 输出列对照
- [CON-logrank-vs-cox](cards/methods/tte/CON-logrank-vs-cox.md) — log-rank（曲线相同、给 P 值）与 Cox（HR = 1、给 HR 和 CI）的 H₀、分工、P 值与 CI 偶尔不一致的原因；SAS / R（分层 coxph、survdiff）代码

待建：KM 置信区间（Greenwood 方差、log / log-log 变换）、RMST 实现、竞争风险、Cox 模型细节（分层、协变量、ties）、比例风险假设检验方法

## 6. 缺失数据与敏感性分析

- [CON-missing-data](cards/missing-data/CON-missing-data.md) — MCAR/MAR/MNAR 定义与例子、因 AE 停药的归类、策略与插补方法（J2R、retrieved dropout）
- [CON-sensitivity-analysis](cards/missing-data/CON-sensitivity-analysis.md) — 敏感性分析的定义、典型组合与各方法说明（J2R / CR、tipping point、模式混合模型），及与补充分析（per-protocol、完成者分析）的区别

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

## CDISC 数据标准

SDTM / ADaM 的结构、变量命名规则，以及各分析数据集里与统计分析直接相关的约定。

- [CON-cdisc-variable-naming](cards/cdisc/CON-cdisc-variable-naming.md) — 把 ADaM / SDTM 变量名拆成零件：主体词根（TRT、AE、PARAM、BASE、CHG、DCS / DCT、NR、CRIT、OCC、CNSR…）、时间零件（S / E、DT / TM / DTM / DTC、DY、DTF）、类型后缀（FL、N、C、CD、GR、CAT）、前缀（A、B、P、RF、`--`）、计划 / 实际与编号（P / A、xx、y、zz）、SDTM 结果类变量（ORRES、STRESC / STRESN、STNRLO…）、11 个拆解示例；同一字母在不同位置含义不同，最终以 define.xml 为准

> ADTTE 的关键变量与 CNSR 方向目前写在 [CON-survival-analysis-overview](cards/methods/tte/CON-survival-analysis-overview.md#6-落到临床编程上)，删失相关的 CNSR / ADT / EVNTDESC / CNSDTDSC 写在 [CON-censoring](cards/methods/tte/CON-censoring.md#在-adtte-里怎么体现)。

## 非临床应用

统计方法在临床试验以外的领域（工程、互联网、金融等）怎么用，帮助理解方法本身。

- [CON-survival-analysis-non-clinical](cards/non-clinical/CON-survival-analysis-non-clinical.md) — 生存分析在工程、互联网、金融、保险、人力资源等 10 个领域的起点 / 事件 / 删失举例；可靠性分析、持续时间分析、事件史分析等别名；客户流失率直接相除为何有偏
- [CON-reliability-engineering](cards/non-clinical/CON-reliability-engineering.md) — 可靠性工程：制造业为何需要生存分析（大量删失）；寿命测试（B10、MTTF / MTBF、可靠度）、加速寿命试验与 AFT、保修数据分析（里程作时间轴）、预测性维护（时间依赖协变量 Cox）、供应商比较；与临床试验的区别（Weibull 参数模型、外推）；Weibull 形状参数与浴盆曲线
