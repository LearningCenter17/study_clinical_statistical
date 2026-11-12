---
id: CON-parametric-vs-nonparametric
title: "参数方法与非参数方法（Parametric vs Nonparametric Methods）"
categories: [inference, parametric, nonparametric, rank-test, mann-whitney, wilcoxon, robustness, outlier, hodges-lehmann]
related: [CON-test-selection, CON-p-value, CON-distribution-family, CON-t-test-pvalue, CON-MMRM, CON-confidence-interval, GOT-skewed-small-sample, CON-covariate, CON-confirmatory-methods-overview, CON-ordinal-data, CON-CMH]
sources: ["Claude 对话（inbox: parametric.md）"]
status: draft
updated: 2026-11-12
---

> 出处待补：本卡内容来自 Claude 对话（inbox: parametric.md），属 AI 生成内容，未引用原始文献。

## 一句话定义

**"参数"指描述一个分布的那几个数字。** 例如正态分布完全由均值 μ 和标准差 σ 两个参数决定，知道这两个数，整条钟形曲线就确定了（各分布的参数见 [CON-distribution-family](CON-distribution-family.md)）。

- **参数方法**：先**假设数据服从某种已知分布**（通常是正态），再估计并比较这个分布的参数。
- **非参数方法**：**不假设数据服从某种具体分布**，也叫"分布无关"（distribution-free）；最常见的做法是**把原始数值换成秩次（排名）**再比较。

## 对比

| | 参数方法 | 非参数方法 |
|---|---|---|
| 例子 | t 检验（比较均值）、ANOVA、ANCOVA、[MMRM](CON-MMRM.md) | Mann-Whitney U、Wilcoxon 符号秩、Kruskal-Wallis、Friedman |
| 优点 | 假设成立时**效率最高（功效最大）**；直接给出效应量，如"均值差 −8.2 mmHg，95% CI −11.0 至 −5.4"（CI 读法见 [CON-confidence-interval](CON-confidence-interval.md)） | 不怕偏态、离群值和等级数据，假设条件少 |
| 缺点 | 假设不成立时可能出问题：极端值会把均值和 SD 都拉偏，t 检验失效 | 数据确实正态时功效略低（差别不大，约 95%）；主要给 P 值，效应量要另算（如 Hodges-Lehmann 估计）；不容易调整协变量 |

材料提到"之前 CRP 的例子"：一个 96 的极端值把均值和 SD 拉偏、t 检验失效。完整数据与三种方法的对比见 [GOT-skewed-small-sample](../gotchas/GOT-skewed-small-sample.md)。

## 为什么秩次对离群值稳健

以 Mann-Whitney U 检验为例：

| 原始值 | 3.2 | 4.1 | … | 31.0 | **96.0** |
|---|---|---|---|---|---|
| 排名 | 1 | 2 | … | 19 | **20** |

96 换成排名后只是"第 20 名"，和 31 只差 1 名，极端值的影响一下子就没了。

**打个比方**：比较两个班的考试成绩。

- **参数方法**：比较两个班的**平均分**。有个同学考了 0 分（缺考），平均分就被拉低了。
- **非参数方法**：把两个班的同学放在一起**排名**，看哪个班整体排得更靠前。那个 0 分只是"最后一名"，不会拖累太多。

## 对应关系

| 参数方法 | 非参数方法 |
|---|---|
| 两组 t 检验 | Mann-Whitney U（Wilcoxon 秩和） |
| 配对 t 检验 | Wilcoxon 符号秩检验 |
| 单因素 ANOVA | Kruskal-Wallis |
| 重复测量 ANOVA | Friedman |

各方法的适用条件、临床例子和代码见 [CON-test-selection](CON-test-selection.md)。

## 容易误解的地方

- **"非参数"不等于没有任何假设。** 例如 Mann-Whitney U 仍然假设两组独立；要把结果解释为"中位数不同"，还需要两组分布形状相似。它只是不要求数据服从正态分布。
- **卡方检验和 Fisher 检验通常也归入非参数方法**，因为它们同样不假设连续分布。所以 [CON-test-selection](CON-test-selection.md) 里"非参数检验"那一节，主要指**基于秩次**的那几种检验。

## 补充

> 补充（Claude）：
> - "约 95%"指渐近相对效率（asymptotic relative efficiency, ARE）：数据正态时 Wilcoxon 秩和检验相对 t 检验的 ARE = 3/π ≈ 0.955，即大约需要多 5% 的样本量达到同样功效。对任意连续分布，这个 ARE 不低于 0.864；在重尾分布下可以大于 1，即非参数方法反而功效更高。
> - "不容易调整协变量"：分层可用 van Elteren 检验（分层 Wilcoxon，SAS `PROC NPAR1WAY` 无直接选项，常用 `PROC FREQ` 的 `cmh2 scores=modridit` 实现，见 [CON-CMH](CON-CMH.md)）；调整连续协变量常改用秩 ANCOVA 或对变换后的数据做参数模型。
> - 效应量：SAS `PROC NPAR1WAY` 的 `hl` 选项给出 Hodges-Lehmann 位置差估计及 CI。
>
> 以上待 Li 核实。

## 相关卡片

- [CON-test-selection](CON-test-selection.md)：快速选择表与各检验的临床示例
- [CON-p-value](CON-p-value.md)：分布假设靠不住时从数据里构造零分布（非参数 / 置换 / 精确）
- [CON-distribution-family](CON-distribution-family.md)：分布及其参数

## 出处

- Claude 对话（inbox: parametric.md；AI 生成，原始出处待补）
