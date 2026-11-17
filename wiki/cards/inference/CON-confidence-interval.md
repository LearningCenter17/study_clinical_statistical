---
id: CON-confidence-interval
title: "置信区间（Confidence Interval）：含义、构成、解读及与 P 值的对应"
categories: [inference, confidence-interval, p-value, hypothesis-testing, effect-size, reporting, point-estimate, standard-error, coverage, credible-interval, bayesian, precision, event-count]
related: [CON-p-value, CON-type-I-II-error, MTH-t-test, GOT-ttest-student-vs-welch, CON-hazard-ratio, GOT-ni-hypothesis-direction, CON-null-hypothesis, CON-parametric-vs-nonparametric, GOT-skewed-small-sample, CON-normal-distribution, CON-response-rate, CON-t-distribution, CON-degrees-of-freedom, CON-dose-escalation-design, CON-covariate, CON-sample-size-power, CON-missing-data, CON-logrank-vs-cox]
sources: ["Claude 对话（inbox: summary_p.md）", "Claude 对话（inbox: CI_1.md）", "Claude 对话（inbox: CI_1_correction.md）", "Claude 对话（inbox: CI_bayesian.md）", "Claude 对话（inbox: CI_width.md）"]
status: draft
updated: 2026-11-16
---

> 出处待补：本卡内容来自 Claude 对话（inbox: summary_p.md、CI_1.md、CI_1_correction.md、CI_bayesian.md、CI_width.md），属 AI 生成内容，未引用原始文献。示例数值已由 Claude 在 R 4.5.2 中复核。

## 一句话定义

置信区间（CI）是用样本数据**估计一个未知总体参数**时给出的**可能范围**，同时说明这个范围有多可靠（来源：CI_1.md）。

**95% CI 和 α = 0.05 的双侧检验是同一把尺子的两种说法**。CI 比 P 值多告诉你两件事：差值**可能有多大**，以及估计得**有多精确**。

## 为什么需要 CI

临床试验只能抽一部分患者做样本。样本算出的结果（如"Drug 组平均下降 8.2 分"）只是对真实值的**点估计**，换一批患者重做会略有不同。只报一个数字，读者看不出它有多准。CI 在点估计之外加一个范围：

> 平均下降 **8.2 分（95% CI：5.9，10.5）**

## 三个组成部分

```
   估计值   ±   临界值   ×   标准误（SE）
     ↓            ↓              ↓
  样本均值     1.96（95%）    SD / √n
  (中心)       (置信水平)     (估计的精度)
```

- **估计值**：区间的中心。
- **SE**：数据越分散、样本越少，SE 越大，区间越宽。
- **置信水平**：95% 最常用。要求的把握越高（如 99%），区间越宽。

"估计值 ± 1.96 × SE"作为**理解 CI 的思路**没问题（中心 ± 临界值 × 标准误），但实际**计算**时，临界值和构造方法要看统计量的类型（来源：CI_1_correction.md）。

> 更正记录（2026-11-16）：CI_1.md 原文把临界值写成 1.96。后续对话（CI_1_correction.md）确认这是简化写法，补充了下面两小节。

### 1.96 还是 t 临界值

| 情况 | 用什么 | 原因 |
|---|---|---|
| σ **已知**（现实中几乎没有） | z = **1.96** | 标准正态分布 |
| σ **未知**，用样本 s 代替 | t₀.₉₇₅,df | s 本身也有误差，t 分布更"胖"，把这部分不确定性算进去 |
| 样本量很大 | t ≈ 1.96 | df 越大，t 分布越接近正态 |

```r
round(qt(0.975, c(5, 10, 30, 59, 118, 1000)), 3)
#>  2.571  2.228  2.042  2.001  1.980  1.962
qnorm(0.975)
#>  1.960
```

- df = 5 时是 2.57。用 1.96 算出的 CI **偏窄**，实际覆盖率不到 95%。
- df = 59（单组 60 人）时是 2.00，与 1.96 差别很小；df 上千时基本相同。

所以**均值和均值差的 CI 应该用 t 临界值**。R 的 `t.test()`、`lm()` + `emmeans` 会自动用 t 分布。1.96 本身的来历见 [CON-normal-distribution](CON-normal-distribution.md)，t 临界值随 df 的变化见 [CON-t-distribution](CON-t-distribution.md)、[CON-degrees-of-freedom](CON-degrees-of-freedom.md)。

> 数值复核（Claude，R 4.5.2）：上面 6 个 t 临界值与材料一致。模拟（正态数据，n = 6 即 df = 5，重复 20000 次）用 1.96 构造均值 CI，实际覆盖率约 **89%**，印证"偏窄、不到 95%"。

### 不同统计量的 CI 构造方法

| 统计量 | CI 的构造方法 | 临界值 |
|---|---|---|
| 均值、均值差、LS mean 差 | 估计值 ± **t** × SE | t（df 由样本量或模型决定） |
| 单组比例 | Clopper-Pearson（精确法）或 Wilson | 不是简单的"± 临界值 × SE" |
| 比例差 | Newcombe、Miettinen-Nurminen 等 | 同上 |
| HR、OR | 先在 **log 尺度**上算，再取指数 | z = 1.96 |
| 中位生存期 | Brookmeyer-Crowley，常配 log-log 变换 | 基于 z |

**HR 的例子**：Cox 模型估计的是 log(HR)，即系数 β：

$$
\text{HR 的 95\% CI} = \exp\big(\hat\beta \pm 1.96 \times SE(\hat\beta)\big)
$$

这里用 1.96 是对的，因为基于大样本近似（Wald）。算完再取指数，所以 HR 的 CI **不对称**：HR = 0.65、CI (0.42, 1.01)，0.65 不在区间正中间（在 log 尺度上才居中）。

```r
cox <- coxph(Surv(AVAL, 1 - CNSR) ~ TRT01P, data = adsl)
b   <- coef(cox)
se  <- sqrt(vcov(cox))
exp(b + c(-1, 1) * qnorm(0.975) * se)   # 手算
exp(confint(cox))                        # 与 R 内置结果一致
```

> 补充（Claude）：代码中 `adsl` 是材料的写法。实际项目里 AVAL / CNSR 是 time-to-event 参数，通常在 ADTTE（按 PARAMCD 筛选），不在 ADSL。待 Li 核实。

**总结**：均值类用 t；比例类用精确法或 score 类方法；比值类（HR、OR）在 log 尺度上用 z。每个终点用哪种 CI 方法，SAP 里一般会写明，编程按 SAP 来。单组率的 CI 示例见 [CON-response-rate](../methods/binary/CON-response-rate.md)。

## 95% 到底是什么意思

这一点最容易理解错。

- ❌ **错误理解**："真实值有 95% 的概率落在 (5.9, 10.5) 之间。"
- ✅ **正确理解**："用同样的方法重复做很多次试验，每次都算一个 CI，大约 **95% 的 CI 会套住真实值**。"

真实值是固定的，只是我们不知道；会变的是每次试验算出来的区间。可以拿**套圈**理解：

```
真实值 →            ●
试验 1         [────●────]        ✓ 套中
试验 2      [────────●─]          ✓
试验 3                 ●  [────]  ✗ 没套中
试验 4          [──────●──]       ✓
...
100 次里大约 95 次套中
```

这个"覆盖率"可以用模拟验证：设定真实值，重复抽样 1000 次、每次算 CI、数有几次套中，结果约 0.95。思路同 [CON-response-rate](../methods/binary/CON-response-rate.md#抛硬币类比与模拟) 中用 `rbinom` 模拟应答人数。

> 注：材料提到"前面那段模拟代码"，但代码本身不在材料里，未收录。

### 为什么不能说"这个区间有 95% 的概率包含真实值"

在频率学派看来，真实值 μ 是固定的。某一个**已经算出来**的区间，比如 (46.5, 51.3)，要么包含 μ（概率 1），要么不包含（概率 0），没有"95% 概率包含"这种中间状态。**95% 描述的是这套方法的可靠性，不是这一个区间**（来源：CI_bayesian.md）。

套圈比喻：你的套圈成功率是 95%。但圈已经扔出去、落地了，它要么套中、要么没套中，只是你还没看到结果。

## 置信区间 vs 贝叶斯可信区间

"真实值有 95% 的概率落在这个区间里"描述的其实是**贝叶斯可信区间**（credible interval），不是置信区间。两派对"概率"的理解不同：

| | 频率学派（Frequentist） | 贝叶斯学派（Bayesian） |
|---|---|---|
| 真实值 μ 是什么 | **固定的**一个数，只是不知道 | 不确定的，**本身有一个概率分布** |
| 区间名称 | 置信区间（Confidence Interval） | 可信区间（Credible Interval） |
| 什么是随机的 | **区间**（每次试验算出来的都不同） | **参数**（对它的认识用概率描述） |
| 95% 的含义 | 重复很多次试验，约 95% 的区间会套住真实值 | 根据现有数据，真实值有 95% 的概率在这个区间里 |

### 可信区间怎么算

1. **先验**（prior）：试验前对参数的认识，比如根据历史数据认为应答率大约在 20% 到 40%。
2. **后验**（posterior）：结合试验数据更新对参数的认识。

可信区间直接取后验分布的中间 95%，所以可以说"真实值有 95% 的概率在这里面"。

### R 例子：同一份应答数据，两种区间

Drug 组 60 人中 27 人应答（同 [CON-response-rate](../methods/binary/CON-response-rate.md) 的例子）：

```r
x <- 27; n <- 60

# 频率学派：95% 置信区间（Clopper-Pearson）
binom.test(x, n)$conf.int

# 贝叶斯：95% 可信区间（均匀先验 Beta(1, 1)）
# 后验分布 = Beta(1 + 应答人数, 1 + 未应答人数)
qbeta(c(0.025, 0.975), 1 + x, 1 + n - x)
```

两个区间数值很接近，但**解释不同**：

- 置信区间：用这种方法反复做试验，95% 的区间会包含真实应答率。
- 可信区间：根据这些数据（加上"没有先验信息"的假设），真实应答率有 95% 的概率在这个范围里。

`qbeta()` 的用法和 `qnorm()`、`qt()` 一样，只是换成 **Beta 分布**。Beta 分布常用来描述一个比例的不确定性。

> 数值复核（Claude，R 4.5.2）：Clopper-Pearson 置信区间 (0.321, 0.584)；Beta(28, 34) 后验的 95% 可信区间 (0.331, 0.576)。材料说"大约都在 (0.32, 0.58) 附近"，大体一致，可信区间略窄。

### 在临床试验里

- **绝大多数注册试验**的主要分析用频率学派方法，TLF 报告**置信区间**，写 "95% CI"。
- **贝叶斯方法**用在特定场景：罕见病试验、儿科试验借用成人数据、适应性设计等（一期剂量递增中的应用见 [CON-dose-escalation-design](../design/CON-dose-escalation-design.md)）。这时报告**可信区间**，写 "95% CrI" 或 "95% credible interval"。

写 CSR 或解释结果时，**不要用"有 95% 的概率"描述置信区间**。规范写法是"95% CI 为 (5.9, 10.5)"，或"差值的 95% 置信区间不包含 0"。

> 更正记录（2026-11-16）：首次收录 CI_1.md 时，此处是 Claude 补充的一句"这是频率学派的解释……"。后续对话（CI_bayesian.md）确认并展开，已替换为本节。

## CI 与 P 值的对应

| CI 与"无差别值"的关系 | 等价于 | 含义 |
|---|---|---|
| **0 不在 CI 内** | p < 0.05 | "没差别"和数据不相容，结果显著 |
| **0 在 CI 内** | p ≥ 0.05 | "没差别"排除不了，结果不显著 |

"无差别值"对均值差、率差是 0；对 HR、OR 等比值是 1（见 [CON-hazard-ratio](../methods/tte/CON-hazard-ratio.md)）。

| 指标 | 无效值 | 举例 | 结论 |
|---|---|---|---|
| 差值（均值差、率差） | **0** | 差值 −5.2 (−8.1, −2.3) | 不含 0 → 显著 |
| 比值（HR、OR、RR） | **1** | HR 0.65 (0.42, 1.01) | 含 1 → 不显著 |

CI 能提供的信息比 P 值多：

- **效应有多大**：看中心位置。
- **估计得有多准**：看区间宽度。宽度由什么决定见下一节。

> 补充（Claude）：这种等价要求 CI 和检验**出自同一方法**（同一 SE、同一自由度、同一分布）。例如 t 检验的 Welch CI 对应 Welch 检验、Pooled CI 对应 Pooled 检验；混用时（如 Wald CI 配 score 检验、Hodges-Lehmann CI 配 Wilcoxon 检验、Cox 的 Wald CI 配 log-rank P 值）边界附近可能出现"CI 不含 0 但 p 略大于 0.05"之类不一致。待 Li 核实。（Cox Wald CI 配 log-rank P 值这一例，后续对话 CI_HR.md 已确认"偶尔不一致是正常的"，见 [CON-logrank-vs-cox](../methods/tte/CON-logrank-vs-cox.md#临床试验中的常见做法)。）

## CI 宽度由什么决定

不只是样本量（来源：CI_width.md）：

| 因素 | 影响 |
|---|---|
| **数据的变异**（SD） | SD 越大，CI 越宽 |
| **样本量 n** | n 越大，CI 越窄（按 1/√n 缩小） |
| **置信水平** | 99% 比 95% 宽 |
| **分析方法** | 如 ANCOVA 调整基线后残差变异变小，CI 更窄（见 [CON-covariate](../methods/continuous/CON-covariate.md)） |
| **比例本身的大小**（率类终点） | p 接近 50% 时 CI 最宽，接近 0 或 1 时更窄 |
| **事件数**（生存终点） | **起决定作用的是事件数，不是入组人数** |

所以 CI 窄，可能是因为样本量大，也可能是数据本身变异小，**不能直接推出"样本量够了"**。

> 更正记录（2026-11-16）：CI_1.md 原文写"窄说明样本量充足，宽说明不确定性大"。后续对话（CI_width.md）确认这把宽度只归因于样本量，说法不完整，已改为本节。

### 生存终点：看事件数

1:1 随机时，Cox 模型中 log(HR) 的标准误约为：

$$
SE(\log \widehat{HR}) \approx \frac{2}{\sqrt{D}}
$$

D 是两组**合计的事件数**。公式里没有入组人数 n，只有 D。删失的病人只贡献"到某时间点还没发生事件"这一点信息，决定 HR 估计精度的是观察到了多少个事件。

```r
hr_ci <- function(hr, D) {
  se <- 2 / sqrt(D)
  round(exp(log(hr) + c(-1, 1) * qnorm(0.975) * se), 2)
}

hr_ci(0.70, D = 30)     # (0.34, 1.43)  很宽，含 1
hr_ci(0.70, D = 100)    # (0.47, 1.04)  仍含 1
hr_ci(0.70, D = 300)    # (0.56, 0.88)  不含 1
```

| | 试验 A | 试验 B |
|---|---|---|
| 入组人数 | 1000 | 300 |
| 事件数 | 30（随访短、事件少） | 150 |
| HR 的 CI | **宽** | **窄** |

试验 A 人多，CI 反而更宽。所以肿瘤试验 SAP 里期中分析和最终分析都按**事件数**触发（如"观察到 200 个 PFS 事件时进行最终分析"），而不是按入组人数或日历时间。同样的道理在样本量计算里的体现见 [CON-sample-size-power](../design/CON-sample-size-power.md)（power 取决于事件数、Schoenfeld 公式）。

> 数值复核（Claude，R 4.5.2）：上面三个 `hr_ci()` 结果与材料一致。若 HR 同为 0.70，试验 A（D = 30）为 (0.34, 1.43)，试验 B（D = 150）为 (0.51, 0.96)。
>
> 补充（Claude）：2/√D 来自 1:1 随机时 Var(log HR) ≈ 4/D 的近似（与 Schoenfeld 公式同源）。分配比例为 r:1 时，系数变为 (1 + r)/√(r·D)。待 Li 核实。

### 窄 CI 不等于结论可靠

CI 只反映**随机误差**，不反映**系统偏倚**：

- 数据有偏倚（大量缺失、揭盲、人群选择有问题）时，CI 可以很窄，但中心位置是偏的。缺失数据见 [CON-missing-data](../missing-data/CON-missing-data.md)。
- CI 窄也不代表效果有**临床意义**。样本量很大时，很小的差值也可能得到一个很窄、不含 0 的 CI：统计上显著，临床上未必重要（MCID 见 [CON-sample-size-power](../design/CON-sample-size-power.md)）。

解读 CI 要分开看：**中心位置**说明效应多大，**宽度**说明估计多精确，再结合研究设计和数据质量判断结论是否可信。

## 不显著 ≠ 没差别

- 0 在 CI 里，只说明**不能排除**没差别，**不能证明**没差别。
- CI 窄而且围着 0 → 差别确实小；CI 宽 → 证据不够（样本量或事件数不足、变异大等，见上一节）。
- 例（来源：CI_1.md）：HR 0.65 (0.42, 1.01)，p 约 0.054，算"不显著"。但从 CI 看，药物可能把风险降低多达 58%（1 − 0.42），也可能基本无效。这说明**证据不够**，不是证明药物无效。只看 P 值看不出这一点。

  > 数值复核（Claude，R 4.5.2）：按 log 尺度对称反推，SE(log HR) ≈ 0.224，z ≈ −1.92，双侧 p ≈ 0.054，与材料一致。
- 要证明"两组一样"，需用**等效性检验或非劣效检验**：看的是**整个 CI** 是否落在预设界值以内（方向与界值见 [GOT-ni-hypothesis-direction](../design/GOT-ni-hypothesis-direction.md)）。

与 power 的关系见 [CON-type-I-II-error](CON-type-I-II-error.md#最重要的解读原则不显著--无效)。

## 报告示例

用 [CON-p-value](CON-p-value.md#实现软件里怎么算) 中的示例数据（A 组 115, 120, 125, 130, 128；B 组 105, 110, 108, 112, 109）：

> A 组（123.6 ± 6.1）显著高于 B 组（108.8 ± 2.6），均值差为 14.8（95% CI: 7.3–22.3），Welch t 检验 t = 4.99，df = 5.39，p ≈ 0.003。

报告里点估计、CI、检验方法、统计量、df、P 值齐全，而且 CI 与检验用的是同一种方法（Welch）。

> 数值复核（Claude，R 4.5.2）：均值 123.6 / 108.8，SD 6.11 / 2.59；Welch 95% CI 7.34–22.26，p = 0.0034，与材料一致。若用 Pooled，CI 为 7.96–21.64、p = 0.0011（见 [GOT-ttest-student-vs-welch](../methods/continuous/GOT-ttest-student-vs-welch.md)）。
>
> 补充（Claude）："123.6 ± 6.1"中 ± 后是 SD；报告时应写明是 SD 还是 SE，常见写法为 "mean (SD)"。待 Li 核实。

## 一句话主线

**t 值、F 值、置信区间都是"观测到的差别 ÷ 随机误差"这个思路的变形**（t 见 [MTH-t-test](../methods/continuous/MTH-t-test.md#t-值是信噪比)，F 见 [CON-distribution-family](CON-distribution-family.md#f-分布)）。

> 补充（Claude）：严格说，CI 是这个比值"反过来用"：差值 ± 临界值 × SE。t 检验问"差值是 SE 的几倍"，CI 问"在临界值倍 SE 的范围内，真实差值可能落在哪"。均值差的 95% CI = 差值 ± t₀.₉₇₅,df × SE。

## 相关卡片

- [CON-p-value](CON-p-value.md)：P 值的定义与解读
- [CON-type-I-II-error](CON-type-I-II-error.md)：不显著 ≠ 无效
- [MTH-t-test](../methods/continuous/MTH-t-test.md)：SAS PROC TTEST 的 Confidence Limits 表
- [GOT-ni-hypothesis-direction](../design/GOT-ni-hypothesis-direction.md)：非劣效用 CI 与 Δ 比较
- [CON-hazard-ratio](../methods/tte/CON-hazard-ratio.md)：比值类效应量的 CI 看是否跨 1
- [CON-response-rate](../methods/binary/CON-response-rate.md)：率的 CI 示例（ORR）
- [CON-normal-distribution](CON-normal-distribution.md)、[CON-t-distribution](CON-t-distribution.md)：临界值 1.96 与 t 临界值

## 出处

- Claude 对话（inbox: summary_p.md；AI 生成，原始出处待补）
- Claude 对话（inbox: CI_1.md；AI 生成，原始出处待补）
- Claude 对话（inbox: CI_1_correction.md；AI 生成，原始出处待补）
- Claude 对话（inbox: CI_bayesian.md；AI 生成，原始出处待补）
- Claude 对话（inbox: CI_width.md；AI 生成，原始出处待补）
