---
id: CON-normal-distribution
title: "正态分布、标准正态分布与 1.96（Normal Distribution, Standardization and 1.96）"
categories: [inference, distribution, normal, standard-normal, z-score, standardization, critical-value, qnorm, confidence-interval]
related: [CON-distribution-family, CON-t-distribution, CON-degrees-of-freedom, CON-confidence-interval, CON-t-test-pvalue, CON-sample-size-power, CON-test-statistic]
sources: ["Claude 对话（inbox: normal_distribution.md）"]
status: draft
updated: 2026-11-13
---

> 出处待补：本卡内容来自 Claude 对话（inbox: normal_distribution.md），属 AI 生成内容，未引用原始文献。文中数值已由 Claude 在 R 4.5.2 中逐项复核。

## 标准正态分布只有一条

**是的，标准正态分布只有一个，永远长一样。**

"标准"就是把两个参数固定死：**均值 = 0，标准差 = 1**，记作 N(0, 1)。参数都定了，曲线就只有这一条。所以 1.96、68–95–99.7 法则、`dnorm(0)` = 0.399 这些数字，对谁都一样。

> 补充（Claude，R 复核）：68–95–99.7 指 ±1、±2、±3 个标准差内的面积，精确值为 0.6827、0.9545、0.9973。

## 不一样的是"普通"正态分布

一般的正态分布 N(μ, σ²) 有两个可变参数，所以有无数条：

- **μ（均值）决定位置**：曲线往左或往右平移。
- **σ（标准差）决定胖瘦**：σ 大则矮胖，σ 小则高瘦。

```text
   σ 小（高瘦）       σ 大（矮胖）
      ╭╮
      ││            ╭────╮
     ╱  ╲         ╱        ╲
 ───╱────╲───   ─╱──────────╲─
     μ              μ
```

例如收缩压可能是 N(120, 15²)，体重可能是 N(70, 12²)。形状都是钟形，但位置和宽度不同。正态分布在整个分布家族里的位置见 [CON-distribution-family](CON-distribution-family.md)。

## 关键：所有正态分布都能变成同一个标准正态

只需一步**标准化**：

**z = (x − μ) / σ**

先减均值把中心移到 0，再除以标准差把宽度缩放到 1，任何正态分布都变成 N(0, 1)。

例：收缩压 150，均值 120，SD 15，则 z = (150 − 120) / 15 = 2，相当于标准正态里的 2。

```r
pnorm(150, mean = 120, sd = 15)   # 0.977
pnorm(2)                          # 0.977，完全一样
```

**这就是为什么只需要记一套数字（如 1.96），就能用于所有正态分布的问题。** 这也是检验统计量要写成"**估计值 / SE**"的原因：先标准化，再和统一的临界值比较（见 [CON-test-statistic](CON-test-statistic.md)、[CON-t-test-pvalue](CON-t-test-pvalue.md#t-值是信噪比)）。

## 对比：t 分布不是唯一的

t 分布有一个参数**自由度**，所以是一族曲线：df = 5 和 df = 100 长得不一样，临界值也不同（**2.571 vs 1.984**）。这也是为什么 `qt()` 必须给 `df`，而 `qnorm()` 不用。详见 [CON-t-distribution](CON-t-distribution.md)、[CON-degrees-of-freedom](CON-degrees-of-freedom.md)。

## 1.96 是什么

**1.96 是标准正态分布的 97.5% 分位数**：标准正态变量有 97.5% 的概率小于 1.96。曲线左右对称，所以 **−1.96 到 +1.96 之间正好包住 95% 的面积**，两边各剩 2.5%。

```text
           ╭───╮
         ╱       ╲
       ╱    95%    ╲
  2.5%╱             ╲2.5%
 ────┴───────┬───────┴────
   −1.96     0     +1.96
```

所以 1.96 是：

- 双侧 α = 0.05 检验的临界值；
- 95% CI 公式"**估计值 ± 1.96 × SE**"里的那个数（CI 见 [CON-confidence-interval](CON-confidence-interval.md)）；
- 样本量公式里的 z₁₋α/₂（见 [CON-sample-size-power](CON-sample-size-power.md)）。

## 1.96 是怎么算出来的

问题是：找一个 c，使标准正态曲线下 c 左边的面积等于 0.975。

左侧面积是对正态密度函数的积分：

**P(Z < c) = ∫₋∞ᶜ (1/√(2π)) · e^(−x²/2) dx = 0.975**

这个积分**没有代数解**，写不出"c = 某个公式"，只能用数值方法逼近。过去是统计学家算好后印成正态分布表，现在只需一行代码：

```r
qnorm(0.975)   # 1.959964
```

想看"笨办法"怎么逼近出来，可以手动做两步：先数值积分求面积，再反复调整 c，直到面积等于 0.975。

```r
# 第一步：给定 c，用数值积分求左侧面积
area <- function(c) integrate(dnorm, -Inf, c)$value
area(1.9)    # 0.9713  不够
area(2.0)    # 0.9772  多了
area(1.96)   # 0.9750  正好

# 第二步：让电脑自动找 area(c) = 0.975 的根
uniroot(function(c) area(c) - 0.975, c(0, 3))$root   # 1.959964
```

`qnorm` 内部做的本质上就是这件事，只是用了更快、更精确的算法。

> 数值复核（Claude，R 4.5.2）：`dnorm(0)` = 0.3989；`pnorm(150, 120, 15)` = `pnorm(2)` = 0.9772；`area(1.9)` = 0.9713，`area(2.0)` = 0.9772，`area(1.96)` = 0.9750；`qnorm(0.975)` = 1.959964；`qt(0.975, 5)` = 2.571，`qt(0.975, 100)` = 1.984。以上与材料一致。
>
> 一处小差别：`uniroot()` 用默认精度时输出 **1.959963**，加 `tol = 1e-10` 后才是 1.959964。差在第 7 位小数，不影响理解。

## 记住两个相关的点

- **1.96 只在大样本或 σ 已知时用**；小样本用 t 分布的临界值 `qt(0.975, df)`，它比 1.96 大。"多大算大样本"的分歧见 [CON-t-distribution](CON-t-distribution.md)。
- 常说的"**± 2 个 SD 覆盖约 95%**"，那个 2 就是 1.96 的取整（±2 实际覆盖 95.45%）。

## 相关卡片

- [CON-distribution-family](CON-distribution-family.md)：正态分布在伯努利 → 二项 → 正态 → Z → t / χ² / F 链条中的位置
- [CON-t-distribution](CON-t-distribution.md)：t 分布随自由度变化，逼近标准正态
- [CON-confidence-interval](CON-confidence-interval.md)：估计值 ± 1.96 × SE
- [CON-sample-size-power](CON-sample-size-power.md)：样本量公式中的 1.96 和 1.28

## 出处

- Claude 对话（inbox: normal_distribution.md；AI 生成，原始出处待补）
