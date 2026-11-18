# 生存分析概览
生存分析的英文是 Survival Analysis，也常叫 Time-to-Event Analysis。在工程领域叫 Reliability Analysis（可靠性分析），在经济、社会学领域叫 Duration Analysis 或 Event History Analysis

## 1. 它解决什么问题

生存分析研究的是**"到某个事件发生要多久"**，也就是 time-to-event。这里的"事件"不一定是死亡，也可以是疾病进展、复发、首次出现某种不良事件、退出治疗、达到缓解等。

它和普通回归最大的区别在于**删失（censoring）**：研究结束时，有的受试者事件还没发生，或者中途失访、撤回同意。我们只知道他的事件时间**大于**某个值，不知道确切时间。删失的人不能直接扔掉，否则结果会偏；也不能当作"事件发生"，否则会低估生存时间。生存分析的方法就是为了正确利用这部分"不完整"的信息。

最常见的是**右删失**：知道事件至少在某时间点之后才发生。另外还有左删失和区间删失，比如事件只在两次访视之间被发现，这在影像学评估进展时很常见。

## 2. 核心概念

| 概念 | 含义 |
|---|---|
| 生存函数 S(t) | P(T > t)，即活过时间 t 的概率，从 1 开始单调下降 |
| 风险函数 h(t) | 在 t 时刻仍"在险"的条件下，下一瞬间发生事件的速率 |
| 累积风险 H(t) | h(t) 的积分，S(t) = exp(−H(t)) |
| 中位生存时间 | S(t) 降到 0.5 时对应的 t |
| 在险人数（number at risk） | 在 t 时刻仍在观察中、尚未发生事件也未删失的人数 |

## 3. 三大常用方法

**① Kaplan–Meier（KM）估计：描述**

KM 是一种非参数方法。每到一个事件时间点，就用"(在险人数 − 事件数) / 在险人数"去乘前一步的生存率，得到一条阶梯状下降的曲线。删失的人在删失之前一直计入在险人数，之后才移出，曲线上通常用 "+" 标出删失位置。KM 能给出中位生存时间、某个时间点的生存率（比如 12 个月生存率）以及置信区间。

**② Log-rank 检验：比较组间曲线**

Log-rank 检验的原假设是两组的生存曲线相同。它在每个事件时间点比较观察到的事件数和期望事件数，再汇总起来。如果是分层随机化，就要用**分层 log-rank**。它的弱点是：两条曲线交叉时检验效能会很差。

**③ Cox 比例风险模型：量化效应、调整协变量**

模型形式为 h(t|X) = h₀(t)·exp(βX)。它是半参数模型，不需要设定基线风险 h₀(t) 的具体形式。主要输出是**风险比（HR）**，比如 HR = 0.7 表示治疗组任一时刻的事件风险是对照组的 70%。它的关键假设是**比例风险（PH）**，即 HR 不随时间变化。常用的检验方法有 Schoenfeld 残差和 log(−log S) 图。

## 4. PH 假设不成立时怎么办

- **RMST（限制平均生存时间）**：KM 曲线下到某个截断时间 τ 的面积，可以理解为"τ 之前平均多活了多久"。它不依赖 PH 假设，解读也直观，监管机构越来越接受。
- 分段 Cox 模型或带时间依赖系数的 Cox 模型。
- 加权 log-rank 检验（如 Fleming–Harrington），或 MaxCombo 检验。
- 参数模型（Weibull、对数正态等），在需要外推时常用，比如卫生经济学评估。

## 5. 进阶话题

- **竞争风险**：如果关注的是"复发"，但患者可能先死于其他原因，用 1−KM 会高估复发率。这时应该用**累积发生率函数（CIF）**，组间比较用 Gray 检验，回归用 Fine–Gray 模型。
- **非信息性删失假设**：前提是删失与事件风险无关。如果患者因病情恶化而退出，这个假设就被破坏了，需要做敏感性分析。
- **Estimand 框架（ICH E9(R1)）**：伴随事件（如换用救援治疗）怎么处理，会直接决定删失规则怎么写。

## 6. 落到临床编程上

**ADTTE 数据集**是标准载体，关键变量有：

- `PARAMCD` / `PARAM`：终点，例如 OS、PFS、TTAE
- `AVAL`：时间，常用 `ADT − STARTDT + 1`
- `CNSR`：**0 = 事件，1 = 删失**
- `EVNTDESC` / `CNSDTDSC`：事件或删失的原因，审阅时非常重要
- `STARTDT`、`ADT`、`SRCDOM`、`SRCVAR`：用于溯源

⚠️ **最常见的坑**：ADaM 里 `CNSR=1` 表示删失，而 R `survival` 包的 `Surv(time, status)` 里 `status=1` 表示**事件**。所以要写 `Surv(AVAL, 1 - CNSR)`。在 SAS 里则对应 `time AVAL*CNSR(1)`。

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

---

如果想深入某一块，比如 KM 的手算推导、RMST 的实现，或者某个 PFS 删失规则怎么写进 ADTTE，可以再展开讲。