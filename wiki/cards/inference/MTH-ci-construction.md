---
id: MTH-ci-construction
title: "置信区间的构造方法：1.96 还是 t、各统计量用什么方法（Constructing Confidence Intervals）"
categories: [inference, confidence-interval, critical-value, t-distribution, z, clopper-pearson, wilson, newcombe, miettinen-nurminen, log-scale, wald, hazard-ratio]
related: [CON-confidence-interval, CON-normal-distribution, CON-t-distribution, CON-degrees-of-freedom, CON-hazard-ratio, CON-response-rate, MTH-t-test, CON-continuity-correction, GOT-continuity-correction-r-vs-sas]
sources: ["Claude 对话（inbox: CI_1.md）", "Claude 对话（inbox: CI_1_correction.md）"]
status: draft
updated: 2026-11-18
---

> 出处待补：本卡内容来自 Claude 对话（inbox: CI_1.md、CI_1_correction.md），属 AI 生成内容，未引用原始文献。示例数值已由 Claude 在 R 4.5.2 中复核。
>
> 拆分记录（2026-11-17）：本卡内容原在 [CON-confidence-interval](CON-confidence-interval.md) 中，按"一个知识点一张卡"拆出，内容未改写。CI 的含义和解读仍在那张卡。

## 一句话

"估计值 ± 1.96 × SE"是理解 CI 的思路（见 [CON-confidence-interval](CON-confidence-interval.md#三个组成部分)），但实际**计算**时，临界值和构造方法要看统计量的类型（来源：CI_1_correction.md）。

> 更正记录（2026-11-16）：CI_1.md 原文把临界值写成 1.96。后续对话（CI_1_correction.md）确认这是简化写法，补充了下面两小节。

## 1.96 还是 t 临界值

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

## 不同统计量的 CI 构造方法

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

## 相关卡片

- [CON-confidence-interval](CON-confidence-interval.md)：CI 的含义与解读
- [CON-normal-distribution](CON-normal-distribution.md)、[CON-t-distribution](CON-t-distribution.md)：临界值 1.96 与 t 临界值
- [CON-hazard-ratio](../methods/tte/CON-hazard-ratio.md)：HR 的 CI 算例与 TLF QC
- [CON-response-rate](../methods/binary/CON-response-rate.md)：单组率的 CI 示例

## 出处

- Claude 对话（inbox: CI_1.md；AI 生成，原始出处待补）
- Claude 对话（inbox: CI_1_correction.md；AI 生成，原始出处待补）
