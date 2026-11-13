---
id: CON-confidence-interval
title: "置信区间与 P 值的对应关系（Confidence Interval）"
categories: [inference, confidence-interval, p-value, hypothesis-testing, effect-size, reporting]
related: [CON-p-value, CON-type-I-II-error, CON-t-test-pvalue, GOT-ttest-student-vs-welch, CON-hazard-ratio, GOT-ni-hypothesis-direction, CON-null-hypothesis, CON-parametric-vs-nonparametric, GOT-skewed-small-sample, CON-normal-distribution]
sources: ["Claude 对话（inbox: summary_p.md）"]
status: draft
updated: 2026-11-11
---

> 出处待补：本卡内容来自 Claude 对话（inbox: summary_p.md），属 AI 生成内容，未引用原始文献。示例数值已由 Claude 在 R 4.5.2 中复核。

## 一句话定义

**95% 置信区间（CI）和 α = 0.05 的双侧检验是同一把尺子的两种说法**；CI 比 P 值多告诉你一件事：差值**可能有多大**，以及估计得**有多精确**。

## CI 与 P 值的对应

| CI 与"无差别值"的关系 | 等价于 | 含义 |
|---|---|---|
| **0 不在 CI 内** | p < 0.05 | "没差别"和数据不相容，结果显著 |
| **0 在 CI 内** | p ≥ 0.05 | "没差别"排除不了，结果不显著 |

"无差别值"对均值差、率差是 0；对 HR、OR 等比值是 1（见 [CON-hazard-ratio](CON-hazard-ratio.md)）。

> 补充（Claude）：这种等价要求 CI 和检验**出自同一方法**（同一 SE、同一自由度、同一分布）。例如 t 检验的 Welch CI 对应 Welch 检验、Pooled CI 对应 Pooled 检验；混用时（如 Wald CI 配 score 检验、Hodges-Lehmann CI 配 Wilcoxon 检验、Cox 的 Wald CI 配 log-rank P 值）边界附近可能出现"CI 不含 0 但 p 略大于 0.05"之类不一致。待 Li 核实。

## 不显著 ≠ 没差别

- 0 在 CI 里，只说明**不能排除**没差别，**不能证明**没差别。
- CI 窄而且围着 0 → 差别确实小；CI 宽 → 证据不够，通常是样本量太小。
- 要证明"两组一样"，需用**等效性检验或非劣效检验**：看的是**整个 CI** 是否落在预设界值以内（方向与界值见 [GOT-ni-hypothesis-direction](../gotchas/GOT-ni-hypothesis-direction.md)）。

与 power 的关系见 [CON-type-I-II-error](CON-type-I-II-error.md#最重要的解读原则不显著--无效)。

## 报告示例

用 [CON-p-value](CON-p-value.md#实现软件里怎么算) 中的示例数据（A 组 115, 120, 125, 130, 128；B 组 105, 110, 108, 112, 109）：

> A 组（123.6 ± 6.1）显著高于 B 组（108.8 ± 2.6），均值差为 14.8（95% CI: 7.3–22.3），Welch t 检验 t = 4.99，df = 5.39，p ≈ 0.003。

报告里点估计、CI、检验方法、统计量、df、P 值齐全，而且 CI 与检验用的是同一种方法（Welch）。

> 数值复核（Claude，R 4.5.2）：均值 123.6 / 108.8，SD 6.11 / 2.59；Welch 95% CI 7.34–22.26，p = 0.0034，与材料一致。若用 Pooled，CI 为 7.96–21.64、p = 0.0011（见 [GOT-ttest-student-vs-welch](../gotchas/GOT-ttest-student-vs-welch.md)）。
>
> 补充（Claude）："123.6 ± 6.1"中 ± 后是 SD；报告时应写明是 SD 还是 SE，常见写法为 "mean (SD)"。待 Li 核实。

## 一句话主线

**t 值、F 值、置信区间都是"观测到的差别 ÷ 随机误差"这个思路的变形**（t 见 [CON-t-test-pvalue](CON-t-test-pvalue.md#t-值是信噪比)，F 见 [CON-distribution-family](CON-distribution-family.md#f-分布)）。

> 补充（Claude）：严格说，CI 是这个比值"反过来用"：差值 ± 临界值 × SE。t 检验问"差值是 SE 的几倍"，CI 问"在临界值倍 SE 的范围内，真实差值可能落在哪"。均值差的 95% CI = 差值 ± t₀.₉₇₅,df × SE。

## 相关卡片

- [CON-p-value](CON-p-value.md)：P 值的定义与解读
- [CON-type-I-II-error](CON-type-I-II-error.md)：不显著 ≠ 无效
- [CON-t-test-pvalue](CON-t-test-pvalue.md)：SAS PROC TTEST 的 Confidence Limits 表
- [GOT-ni-hypothesis-direction](../gotchas/GOT-ni-hypothesis-direction.md)：非劣效用 CI 与 Δ 比较
- [CON-hazard-ratio](CON-hazard-ratio.md)：比值类效应量的 CI 看是否跨 1

## 出处

- Claude 对话（inbox: summary_p.md；AI 生成，原始出处待补）
