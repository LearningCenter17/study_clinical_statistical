---
id: CON-chi-square-distribution
title: "卡方分布：标准正态变量的平方和（Chi-square Distribution）"
categories: [inference, distribution, chi-square, standard-normal, degrees-of-freedom, critical-value, null-distribution, simulation]
related: [CON-distribution-family, CON-normal-distribution, CON-degrees-of-freedom, CON-test-statistic, MTH-chi-square, CON-test-selection, CON-t-distribution, CON-continuity-correction, MTH-breslow-day]
sources: ["Claude 对话（inbox: Chi-Square distribution.md）"]
status: draft
updated: 2026-11-18
---

> 出处待补：本卡内容来自 Claude 对话（inbox: Chi-Square distribution.md），属 AI 生成内容，未引用原始文献。临界值和模拟已由 Claude 在 R 4.5.2 中复核。

## 一句话定义

**卡方分布 = 若干个独立标准正态变量的平方和。** k 个互相独立的 Z 各自平方后相加，得到的数服从"自由度为 k 的卡方分布"。它是一个数学上定义好的分布，跟具体数据无关，就像正态分布一样，查表就能知道门槛。

卡方分布在整个分布家族（伯努利 → 二项 → 正态 → Z → t / χ² / F）中的位置见 [CON-distribution-family](CON-distribution-family.md#χ²-分布)。

## 第一步：什么是"标准正态变量"

就是服从**均值 0、标准差 1 的正态分布**的随机数，通常记作 Z，可以理解成"偏离了几个标准差"：Z = 2 就表示偏离了 2 个标准差。68% / 95%（±1.96）等性质见 [CON-normal-distribution](CON-normal-distribution.md)。

> 整理记录（2026-11-18）：材料本步还列了"68% 在 ±1 内、95% 在 ±1.96 内、超过 ±3 很少见"，这些已在 CON-normal-distribution，此处只链接。

## 第二步：标准正态的平方是什么样子

假设随机抽很多个 Z，每个都平方一下，看看 Z² 的分布：

| Z | Z² |
|---|---|
| 0.3 | 0.09 |
| −1.2 | 1.44 |
| 0.8 | 0.64 |
| −0.1 | 0.01 |
| 2.1 | 4.41 |

可以发现：

- Z² **永远不是负数**，因为平方抹掉了正负号
- 大部分 Z 落在 ±1 之间，所以大部分 Z² 小于 1，挤在 0 附近
- 偶尔有较大的 Z，平方后会拉出一条往右的长尾巴
- Z² 的平均值正好是 **1**
- 因为 95% 的 Z 在 ±1.96 以内，所以 95% 的 Z² 在 **1.96² = 3.84** 以内

**Z² 的这个分布，就叫"自由度为 1 的卡方分布"。** 这就是 3.84 这个门槛的来历。

## 第三步：多个加起来

如果把 k 个**互相独立**的 Z 各自平方后加起来：

$$Z_1^2 + Z_2^2 + \dots + Z_k^2$$

得到的这个数的分布就叫**"自由度为 k 的卡方分布"**。自由度就是"加了几个独立的项"。

- 它的平均值是 k（每项平均贡献 1）
- k 越大，分布越往右移，门槛也越高。df = 1 时是 3.84，df = 2 时是 5.99

> 数值复核（Claude）：`qchisq(0.95, 1:3)` = 3.841、5.991、7.815；1.96² = 3.8416。

## 第四步：和卡方检验连起来

卡方检验（见 [MTH-chi-square](../methods/binary/MTH-chi-square.md)）的公式里每一项是：

$$\frac{(O - E)^2}{E} = \left(\frac{O - E}{\sqrt{E}}\right)^2$$

括号里的 (O − E)/√E 是什么？

- O − E 是实际人数偏离期望人数多少
- √E 是计数数据的**标准差**（计数数据的方差约等于 E）
- 偏差 ÷ 标准差 = **偏离了几个标准差**

如果"没有关联"的假设成立，当样本量足够大时，每个格子的人数会近似服从正态分布（中心极限定理）。所以 (O − E)/√E **近似是一个标准正态变量 Z**，每一项就近似是 Z²。

把这些 Z² 加起来，就近似服从卡方分布。于是我们可以拿算出来的 χ² 去和卡方分布的门槛比较：

> 如果真的没有关联，χ² 应该像"几个 Z² 之和"那样，通常不会太大。
> 结果算出来 5.88，超过了 3.84，而"没有关联"时出现这么大值的概率不到 5%，所以拒绝"没有关联"。

> 补充（Claude）：这里对 P 值的表述（"没有关联时出现这么大值的概率"）与 [CON-p-value](CON-p-value.md#一句话定义) 的定义一致。χ² = 5.88、df = 1 对应 p ≈ 0.015。

## 两个"近似"要注意

**1. 为什么只是"近似"正态？**

人数是整数，严格来说不是正态分布，只有样本量大的时候才接近正态。这就是为什么**要求期望值 ≥ 5**：期望值太小时，计数的分布很偏、很离散，跟正态差得远，卡方近似就不准了，这时改用 Fisher 精确检验（判据和例子见 [CON-test-selection](CON-test-selection.md#4-fisher-确切概率法)）。

**2. 为什么 2×2 表加了 4 项，自由度却只有 1？**

定义里要求平方项"互相独立"，但 2×2 表的 4 个格子并不独立：边际合计固定以后，一个格子变了，其他三个都跟着变。所以这 4 项本质上是**同一个 Z² 拆成了 4 份**。

用头痛的例子验证：前面算过 z 检验的 z ≈ 2.43，而

$$2.43^2 \approx 5.88 = 4 \text{ 项之和}$$

正好是一个 Z 的平方，所以自由度是 1。

> 待补：头痛例子的原始 2×2 表不在本材料中（来自更早的对话），无法复核 4 项各自的数值。按材料给的数字：2.43² = 5.90，√5.88 = 2.425，差别来自四舍五入。同一关系在 [MTH-chi-square](../methods/binary/MTH-chi-square.md#r-复核) 的降压药算例中已复核：z = 3.015，z² = 9.091 = χ²。

> 补充（Claude）：一般 r × c 表的自由度为 (r − 1)(c − 1)，即"格子数 − 约束数"，见 [CON-degrees-of-freedom](CON-degrees-of-freedom.md#常见检验的自由度)。"2×2 表 χ² = 两比例 z 检验的 z²"这一关系本身见 [CON-test-statistic](CON-test-statistic.md#它们是亲戚)。严格地说，边际固定时每一项 (O − E)/√E 的方差小于 1，不是单独的标准正态，这正是 4 项加起来只相当于 1 个 Z² 的原因。待 Li 核实。

## 可以自己模拟看看

```r
set.seed(1)
z <- rnorm(100000)          # 10 万个标准正态随机数

mean(z^2)                   # ≈ 1
quantile(z^2, 0.95)         # ≈ 3.84
hist(z^2, breaks = 100, xlim = c(0, 10))   # 挤在 0 附近、右边拖长尾

# 3 个独立 Z² 相加 → 自由度为 3 的卡方
s <- rnorm(1e5)^2 + rnorm(1e5)^2 + rnorm(1e5)^2
mean(s)                     # ≈ 3
quantile(s, 0.95)           # ≈ 7.81，和 qchisq(0.95, 3) 一致
```

跑一下就能直观看到：Z² 的平均值是 1，95% 分位数正好是 3.84。

> 数值复核（Claude）：R 4.5.2 中按上面代码（`set.seed(1)`）实际得到 mean(z²) = 1.007、95% 分位数 = 3.89；3 项之和 mean = 2.995、95% 分位数 = 7.79。模拟值在理论值 3.841 / 7.815 附近波动，"正好是 3.84"指的是理论值，不是这次模拟的输出。

## 相关卡片

- [CON-distribution-family](CON-distribution-family.md)：χ² 在分布家族中的位置，以及 χ² → F
- [CON-normal-distribution](CON-normal-distribution.md)：标准正态、1.96
- [CON-degrees-of-freedom](CON-degrees-of-freedom.md)：列联表自由度
- [CON-test-statistic](CON-test-statistic.md)：χ² 作为零分布的检验，R 求 P 值 `pchisq()`
- [MTH-chi-square](../methods/binary/MTH-chi-square.md)：卡方检验的手算算例
- [CON-test-selection](CON-test-selection.md)：期望频数 < 5 时改用 Fisher
- [CON-t-distribution](CON-t-distribution.md)：另一个由 Z 和 χ² 构造的分布

## 出处

- Claude 对话（inbox: Chi-Square distribution.md；AI 生成，原始出处待补）
