---
id: CON-survival-analysis-overview
title: "生存分析概览：删失、核心函数、KM / log-rank / Cox 与 ADTTE（Survival Analysis Overview）"
categories: [overview, survival, time-to-event, censoring, kaplan-meier, log-rank, cox, proportional-hazards, rmst, competing-risks, adtte, tern, statistical-programming]
related: [CON-logrank-vs-cox, CON-hazard-ratio, CON-confirmatory-methods-overview, CON-estimand, CON-sensitivity-analysis, CON-stratified-randomization, CON-test-statistic, CON-ci-width, WF-sample-size-calc, CON-regression, MTH-kaplan-meier]
sources: ["Claude 对话（inbox: Survival Analysis.md）", "Claude 对话（inbox: regression.md）", "Claude 对话（inbox: at_risk_event.md）", "Claude 对话（inbox: Time_to_event_analysis_area.md）"]
status: draft
updated: 2026-11-19
---

> 出处待补：本卡内容来自 Claude 对话（inbox: Survival Analysis.md；"普通回归为什么处理不了删失"一节来自 regression.md；"常见的事件定义"来自 at_risk_event.md；"临床以外的应用"来自 Time_to_event_analysis_area.md），属 AI 生成内容，未引用原始文献（如 Collett《Modelling Survival Data in Medical Research》、Klein & Moeschberger、SAS PROC LIFETEST / PHREG 文档、CDISC ADaM ADTTE 规范）。本卡是第 5 章的导航页，各方法的细节在链接的卡片里。

## 名称

生存分析的英文是 Survival Analysis，也常叫 Time-to-Event Analysis。在工程领域叫 Reliability Analysis（可靠性分析），在经济、社会学领域叫 Duration Analysis 或 Event History Analysis。

### 临床以外的应用

> 以下来自 Claude 对话（inbox: Time_to_event_analysis_area.md），AI 生成，出处待补。

只要问题能写成"从某个起点开始，过多久会发生某件事"，并且存在"观察结束时事情还没发生"的情况（删失），就能用生存分析。

| 领域 | 起点 | 事件 | 删失的例子 |
|---|---|---|---|
| 工程 / 可靠性 | 设备开始运行 | 故障 | 测试结束时仍在正常运行 |
| 互联网 / SaaS | 用户注册 | 流失（取消订阅、不再活跃） | 统计截止时仍是活跃用户 |
| 金融 / 信贷 | 贷款发放 | 违约或提前还款 | 到观察期结束仍在正常还款 |
| 保险 / 精算 | 投保 | 理赔或身故 | 保单仍有效 |
| 人力资源 | 入职 | 离职 | 到现在仍在职 |
| 市场营销 | 收到优惠券 | 首次购买 | 还没买 |
| 软件工程 | Bug 被提交 | Bug 被修复 | 至今未关闭 |
| 社会学 / 经济学 | 失业 | 重新就业 | 调查结束时仍在找工作 |
| 刑事司法 | 出狱 | 再次犯罪 | 随访期内未再犯 |
| 生态学 | 动物被标记放生 | 死亡或迁出 | 研究结束仍被观测到 |

不同领域叫法不同（见上），但方法是同一套：

- 工程上叫可靠性分析，更常用 Weibull 等参数模型，AFT 名字里的 "failure" 就是从这里来的。
- 经济学、社会学叫持续时间分析（duration analysis）或事件史分析（event history analysis）。
- 互联网公司做用户留存时，留存曲线本质上就是 KM 曲线，Cox 模型用来分析"哪些因素让用户更早流失"。

以客户流失为例：用"已流失人数 / 总注册人数"直接算流失率是有偏的，因为最近注册的用户还没来得及流失，相当于被删失了。用 KM 处理之后，不同时期注册的用户才能放在一起公平比较。这和临床试验里删失患者不能直接扔掉或当作事件（见第 1 节），是完全相同的道理。

> 整理记录（2026-11-19）：材料中"不同领域叫法不同"一句与本卡"名称"一段重复，这里改为"见上"；最后一句补了指向第 1 节的说明。
>
> 补充（Claude）：AFT 即加速失效时间模型（accelerated failure time model），一种参数生存模型，假设协变量使事件时间按比例"加速"或"减速"；本库尚无专门卡片，待 Li 核实。

## 1. 它解决什么问题

生存分析研究的是**"到某个事件发生要多久"**，也就是 time-to-event。这里的"事件"不一定是死亡，也可以是疾病进展、复发、首次出现某种不良事件、退出治疗、达到缓解等。

> 以下来自 Claude 对话（inbox: at_risk_event.md），AI 生成，出处待补。

"事件"指的是研究方案里定义的那个终点，具体是什么取决于你研究什么。"生存分析"这个名字来自早期研究死亡时间，所以事件最初就是死亡，但这个方法后来被推广到任何"到某件事发生要多久"的问题。

常见的事件定义：

| 终点 | 事件是什么 |
|---|---|
| 总生存期（OS） | 任何原因的死亡，这时事件确实是"挂了" |
| 无进展生存期（PFS） | 疾病进展或死亡，以先发生者为准 |
| 至复发时间 | 疾病复发 |
| 至首次不良事件时间（TTAE） | 首次出现某种不良事件 |
| 至停药时间 | 因任何原因停止治疗 |
| 至起效时间 | 首次达到疗效标准，比如关节炎试验里首次达到 ACR20 |

最后一行说明，事件不一定是坏事。"至起效时间"里，事件是"病情好转"，这时曲线下降得越快越好。

它和普通回归最大的区别在于**删失（censoring）**：研究结束时，有的受试者事件还没发生，或者中途失访、撤回同意。我们只知道他的事件时间**大于**某个值，不知道确切时间。删失的人不能直接扔掉，否则结果会偏；也不能当作"事件发生"，否则会低估生存时间。生存分析的方法就是为了正确利用这部分"不完整"的信息。

最常见的是**右删失**：知道事件至少在某时间点之后才发生。另外还有左删失和区间删失，比如事件只在两次访视之间被发现，这在影像学评估进展时很常见。

### 普通回归为什么处理不了删失

> 以下来自 Claude 对话（inbox: regression.md），AI 生成，出处待补。回归本身是什么见 [CON-regression](../CON-regression.md)。

普通回归本身无法处理删失。这不是"可以处理但没处理"，而是它的数学结构里根本没有表达"只知道 Y 大于某个数"的位置。不过回归这个思路是可以改造的，改造后就能处理删失。

**为什么普通回归处理不了**

线性回归（最小二乘法）的做法是：让每个人的预测值和真实值的差距（残差）平方和最小。

> 残差 = 真实 Y − 预测 Y

这要求每个人都有一个确切的 Y。删失的受试者只知道"Y > 24"，没有确切数值，残差算不出来。你只能硬填一个数（比如 24）或者把他删掉，前面说过这两种做法都会造成偏倚。

逻辑回归也一样：它要求每个人的结局明确是"是"或"否"。中途失访的人两者都不是，同样没地方放。

**怎么改造才能处理**

关键在于换一种思路：不再"算差距"，而是改用似然（likelihood），也就是"在这个模型下，观察到这份数据的可能性有多大"。在这个框架下，两类人可以分开写：

- 事件发生的人（确切知道 Y = 5）：贡献"恰好在 5 发生"的概率。
- 删失的人（只知道 Y > 24）：贡献"超过 24 才发生"的概率，也就是 S(24)。

这样删失的人就有了合理的位置：他们的信息是"至少撑到了这个时间"，这个信息被如实写进了模型，既没丢掉，也没被夸大。

> 整理记录（2026-11-18）：材料原文写"删失的受试者 C"，C 是更早一段对话里的例子，这里去掉了代号；"前面说过"指本卡第 1 节"删失的人不能直接扔掉……也不能当作事件发生"。
>
> 补充（Claude）：写成公式，似然 L = ∏_{事件者} f(tᵢ) × ∏_{删失者} S(tᵢ)，f 为密度函数。参数模型（Weibull 等）直接最大化它；Cox 模型用的是只依赖事件时间排序的部分似然（partial likelihood），所以不必设定 h₀(t)。待 Li 核实。

## 2. 核心概念

| 概念 | 含义 |
|---|---|
| 生存函数 S(t) | P(T > t)，即活过时间 t 的概率，从 1 开始单调下降 |
| 风险函数 h(t) | 在 t 时刻仍"在险"的条件下，下一瞬间发生事件的速率 |
| 累积风险 H(t) | h(t) 的积分，S(t) = exp(−H(t)) |
| 中位生存时间 | S(t) 降到 0.5 时对应的 t |
| 在险人数（number at risk） | 在 t 时刻仍在观察中、尚未发生事件也未删失的人数（精确规则：观测时间 ≥ t 的人数，t 时刻发生事件或删失的人仍计入；算例见 [MTH-kaplan-meier](MTH-kaplan-meier.md#在险集规则)） |

## 3. 三大常用方法

**① Kaplan–Meier（KM）估计：描述**

KM 是一种非参数方法。每到一个事件时间点，就用"(在险人数 − 事件数) / 在险人数"去乘前一步的生存率，得到一条阶梯状下降的曲线。删失的人在删失之前一直计入在险人数，之后才移出，曲线上通常用 "+" 标出删失位置。KM 能给出中位生存时间、某个时间点的生存率（比如 12 个月生存率）以及置信区间。

→ 6 人算例的逐步手算、在险集规则、为什么在险人数决定曲线可信度、number at risk 表见 [MTH-kaplan-meier](MTH-kaplan-meier.md)。

> 整理记录（2026-11-19）：此处原有的 KM 公式补充（Claude）已原样移到 MTH-kaplan-meier。

**② Log-rank 检验：比较组间曲线**

Log-rank 检验的原假设是两组的生存曲线相同。它在每个事件时间点比较观察到的事件数和期望事件数，再汇总起来。如果是分层随机化，就要用**分层 log-rank**。它的弱点是：两条曲线交叉时检验效能会很差。

→ H₀ 的严格写法、和 Cox 的分工、P 值与 CI 偶尔不一致的原因、SAS / R 代码见 [CON-logrank-vs-cox](CON-logrank-vs-cox.md)；log-rank 统计量与 χ² 的关系见 [CON-test-statistic](../../inference/CON-test-statistic.md)；分层因素从哪来见 [CON-stratified-randomization](../../design/CON-stratified-randomization.md)。

**③ Cox 比例风险模型：量化效应、调整协变量**

模型形式为 h(t|X) = h₀(t)·exp(βX)。它是半参数模型，不需要设定基线风险 h₀(t) 的具体形式。主要输出是**风险比（HR）**，比如 HR = 0.7 表示治疗组任一时刻的事件风险是对照组的 70%。它的关键假设是**比例风险（PH）**，即 HR 不随时间变化。常用的检验方法有 Schoenfeld 残差和 log(−log S) 图。

→ HR 的含义、为什么在 log 尺度分析、CI 算例与 TLF QC 见 [CON-hazard-ratio](CON-hazard-ratio.md)；HR 的 CI 宽度取决于事件数见 [CON-ci-width](../../inference/CON-ci-width.md#生存终点看事件数)；事件数怎么算（Schoenfeld 公式）见 [WF-sample-size-calc](../../design/WF-sample-size-calc.md)。

## 4. PH 假设不成立时怎么办

- **RMST（限制平均生存时间）**：KM 曲线下到某个截断时间 τ 的面积，可以理解为"τ 之前平均多活了多久"。它不依赖 PH 假设，解读也直观，监管机构越来越接受。
- 分段 Cox 模型或带时间依赖系数的 Cox 模型。
- 加权 log-rank 检验（如 Fleming–Harrington），或 MaxCombo 检验。
- 参数模型（Weibull、对数正态等），在需要外推时常用，比如卫生经济学评估。

## 5. 进阶话题

- **竞争风险**：如果关注的是"复发"，但患者可能先死于其他原因，用 1−KM 会高估复发率。这时应该用**累积发生率函数（CIF）**，组间比较用 Gray 检验，回归用 Fine–Gray 模型。
- **非信息性删失假设**：前提是删失与事件风险无关。如果患者因病情恶化而退出，这个假设就被破坏了，需要做敏感性分析（见 [CON-sensitivity-analysis](../../missing-data/CON-sensitivity-analysis.md)）。
- **Estimand 框架（ICH E9(R1)）**：伴随事件（如换用救援治疗）怎么处理，会直接决定删失规则怎么写（见 [CON-estimand](../../estimand/CON-estimand.md)）。

> 补充（Claude）："伴随事件"即本库所称的 intercurrent event（ICE）。非信息性删失与连续终点里 MAR / MNAR 的问题是同一类，见 [CON-missing-data](../../missing-data/CON-missing-data.md)。

## 6. 落到临床编程上

**ADTTE 数据集**是标准载体，关键变量有：

- `PARAMCD` / `PARAM`：终点，例如 OS、PFS、TTAE
- `AVAL`：时间，常用 `ADT − STARTDT + 1`
- `CNSR`：**0 = 事件，1 = 删失**
- `EVNTDESC` / `CNSDTDSC`：事件或删失的原因，审阅时非常重要
- `STARTDT`、`ADT`、`SRCDOM`、`SRCVAR`：用于溯源

⚠️ **最常见的坑**：ADaM 里 `CNSR = 1` 表示删失，而 R `survival` 包的 `Surv(time, status)` 里 `status = 1` 表示**事件**，所以要写 `Surv(AVAL, 1 - CNSR)`；SAS 里对应 `time AVAL*CNSR(1)`。（这一点在 [CON-logrank-vs-cox](CON-logrank-vs-cox.md#实现) 的代码里也有说明。）

**R 实现示例：**

```r
library(survival)

fit <- survfit(Surv(AVAL, 1 - CNSR) ~ TRT01P, data = adtte)
summary(fit, times = c(6, 12, 24))                 # 时间点生存率
survdiff(Surv(AVAL, 1 - CNSR) ~ TRT01P + strata(STRAT1, STRAT2), data = adtte)  # 分层 log-rank
cox <- coxph(Surv(AVAL, 1 - CNSR) ~ TRT01P + strata(STRAT1, STRAT2), data = adtte)
cox.zph(cox)                                       # PH 假设检验
```

**出 TLF 时常用的工具：**

- `tern` 包（与 rtables 配套）里的 `surv_time()`、`surv_timepoint()`、`coxph_pairwise()` 和 `g_km()`，可以直接生成标准的 time-to-event 汇总表和带在险人数表的 KM 图。
- `ggsurvfit` 或 `survminer` 也可以画出版级的 KM 图。
- QC 时，可以用 SAS 的 `PROC LIFETEST` / `PROC PHREG` 做双编程对比。要注意置信区间的变换方法（log 还是 log-log）和处理并列事件的方法（Efron 还是 Breslow）。R 和 SAS 的默认设置不同，这是数值对不上的常见原因。

> 补充（Claude）：具体默认值——R `survfit()` 的 `conf.type` 默认 `"log"`，SAS `PROC LIFETEST` 的 `CONFTYPE=` 默认 `LOGLOG`；R `coxph()` 的 `ties` 默认 `"efron"`，SAS `PROC PHREG` 默认 `TIES=BRESLOW`（ties 部分另见 [CON-logrank-vs-cox](CON-logrank-vs-cox.md#二者的关系)）。所以 R 端对齐 SAS 时常写 `survfit(..., conf.type = "log-log")`、`coxph(..., ties = "breslow")`，或者两边都按 SAP 指定。待 Li 对照 SAS 文档核实。

## 相关卡片

- [CON-logrank-vs-cox](CON-logrank-vs-cox.md)：log-rank 与 Cox 的分工、SAS / R 代码
- [CON-hazard-ratio](CON-hazard-ratio.md)：HR 的含义与 CI
- [CON-confirmatory-methods-overview](../CON-confirmatory-methods-overview.md)：KM、log-rank、Cox 在确证性试验中的地位
- [CON-estimand](../../estimand/CON-estimand.md)：ICE 处理决定删失规则
- [CON-sensitivity-analysis](../../missing-data/CON-sensitivity-analysis.md)：删失假设的敏感性分析
- [CON-ci-width](../../inference/CON-ci-width.md)：HR 的 CI 宽度由事件数决定
- [WF-sample-size-calc](../../design/WF-sample-size-calc.md)：生存终点的事件数计算

## 出处

- Claude 对话（inbox: Survival Analysis.md；AI 生成，原始出处待补）
- Claude 对话（inbox: regression.md；AI 生成，原始出处待补；"普通回归为什么处理不了删失"一节）
- Claude 对话（inbox: at_risk_event.md；AI 生成，原始出处待补；第 1 节"常见的事件定义"）
- Claude 对话（inbox: Time_to_event_analysis_area.md；AI 生成，原始出处待补；"临床以外的应用"一节）
