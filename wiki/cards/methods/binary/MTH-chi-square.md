---
id: MTH-chi-square
title: "卡方检验：名字由来、两种用法与 2×2 表手算（Pearson's Chi-squared Test）"
categories: [binary-endpoint, chi-square, pearson-chi-square, contingency-table, test-of-independence, goodness-of-fit, expected-frequency, hypothesis-testing]
related: [CON-test-statistic, CON-test-selection, CON-distribution-family, CON-degrees-of-freedom, CON-p-value, MTH-CMH, CON-response-rate, CON-confirmatory-methods-overview]
sources: ["Claude 对话（inbox: Chi-squared test_1.md）"]
status: draft
updated: 2026-11-18
---

> 出处待补：本卡内容来自 Claude 对话（inbox: Chi-squared test_1.md），属 AI 生成内容，未引用原始文献。算例为示意数据，数值已由 Claude 在 R 4.5.2 中复核。

本卡讲卡方检验本身：名字、用途和一张 2×2 表的完整手算。其他内容在别的卡片里：

- 统计量的一般形式 Σ (O − E)² / E，以及它和 t、log-rank 的关系：[CON-test-statistic](../../inference/CON-test-statistic.md)
- 什么时候用卡方、什么时候改用 Fisher，以及临床例子和 R 代码：[CON-test-selection](../../inference/CON-test-selection.md#3-卡方检验)
- χ² 分布从哪来（Z 的平方和）：[CON-distribution-family](../../inference/CON-distribution-family.md#χ²-分布)
- 自由度 (r − 1)(c − 1)：[CON-degrees-of-freedom](../../inference/CON-degrees-of-freedom.md)
- 有分层因素时：[MTH-CMH](MTH-CMH.md#二分类终点分层比较应答率)

## 名称

卡方检验的英文是 Chi-square test（也写作 Chi-squared test），符号 χ²。全称是 Pearson's chi-squared test。

**名字的由来**：χ 是希腊字母，读作 "kai"（中文译成"卡"）。检验算出来的统计量服从一种叫卡方分布（chi-square distribution）的概率分布，"方"指的是平方，因为计算时要把偏差平方后相加。

## 它是干什么的

卡方检验专门处理分类数据的计数，也就是"多少人属于哪一类"这种数据，比如应答 / 不应答、男 / 女、有 / 无不良事件。它回答的问题是：观察到的人数分布，和"没有任何关联"时应有的分布，差得够不够大？

最常见的两种用法：

- **独立性检验（test of independence）**：两个分类变量有没有关系，比如"治疗组别"和"是否应答"有没有关联。
- **拟合优度检验（goodness-of-fit test）**：一个变量的分布是否符合某个预期比例，比如随机化后两组人数是否接近 1:1。

## 算例：2×2 表手算

下面用一个临床研究场景走一遍完整的卡方检验计算，看每一个数字是怎么算出来的，以及"除以 E"在实战中到底发挥了什么作用。

### 场景设定：新药疗效测试

假设你是一家药企的统计师，正在测试一款**降压新药**的效果。你找了 **100 名**高血压患者，随机分成两组（每组 50 人）：

- **新药组**：服用新药
- **安慰剂组**：服用没有药效的糖丸

一个月后，统计血压达标（有效）的人数，得到下面这张**实际观测表（Observed, O）**：

| | 血压达标（有效） | 血压未达标（无效） | **行总计** |
|---|---|---|---|
| **新药组** | **35** | **15** | **50** |
| **安慰剂组** | **20** | **30** | **50** |
| **列总计** | **55** | **45** | **100** |

肉眼看，新药组有 35 人达标，安慰剂组只有 20 人达标，好像新药挺管用的。但这有没有可能是"纯属运气"？我们来算一下卡方值。

### 第一步：计算理论期望表（Expected, E）

假设新药**完全没用**（零假设成立），那么两组患者的达标率应该一模一样。在全部 100 个人里，总共有 55 人达标（总达标率 55%），45 人未达标（总未达标率 45%）。

既然新药组和安慰剂组各有 50 人，按照"没区别"的理论推算，每组的期望人数 E 就是（公式：$\frac{\text{行总计} \times \text{列总计}}{\text{总人数}}$）：

- 两组期望达标人数：$50 \times 55\% = \mathbf{27.5}$ 人
- 两组期望未达标人数：$50 \times 45\% = \mathbf{22.5}$ 人

理论期望表（E）如下：

| | 血压达标（有效） | 血压未达标（无效） |
|---|---|---|
| **新药组** | **27.5** | **22.5** |
| **安慰剂组** | **27.5** | **22.5** |

### 第二步：逐格套用公式 (O − E)² / E

现在我们把 4 个格子里的"实际 O"和"期望 E"一一对比：

1. **新药-有效**：实际 35，期望 27.5（多出 7.5 人）
   $$\frac{(35 - 27.5)^2}{27.5} = \frac{7.5^2}{27.5} = \frac{56.25}{27.5} \approx \mathbf{2.045}$$
2. **新药-无效**：实际 15，期望 22.5（少了 7.5 人）
   $$\frac{(15 - 22.5)^2}{22.5} = \frac{(-7.5)^2}{22.5} = \frac{56.25}{22.5} = \mathbf{2.500}$$
3. **安慰剂-有效**：实际 20，期望 27.5（少了 7.5 人）
   $$\frac{(20 - 27.5)^2}{27.5} = \frac{(-7.5)^2}{27.5} = \frac{56.25}{27.5} \approx \mathbf{2.045}$$
4. **安慰剂-无效**：实际 30，期望 22.5（多出 7.5 人）
   $$\frac{(30 - 22.5)^2}{22.5} = \frac{7.5^2}{22.5} = \frac{56.25}{22.5} = \mathbf{2.500}$$

> **观察细节**：你看这 4 个格子的绝对偏差全都是 **7.5**（分子全是 56.25），但因为"有效组"的期望基数（27.5）比"无效组"的期望基数（22.5）大，所以除以 E 之后，无效组的相对偏差权重（2.500）比有效组（2.045）更高。

### 第三步：求和并得出结论

把 4 个格子的结果加起来，得到最终的卡方统计量：

$$\chi^2 = 2.045 + 2.500 + 2.045 + 2.500 = \mathbf{9.09}$$

- **怎么看这个 9.09？** 对于这种 2×2 的表格，自由度 df = (2 − 1) × (2 − 1) = 1。在统计学标准里，自由度为 1 时，卡方值只要超过 **3.84**，对应的 p 值就小于 0.05（意味着巧合的概率不到 5%）。
- **最终结论**：我们的 χ² = 9.09，远远大于 3.84（对应的 p ≈ 0.0026，巧合概率只有千分之二点六）。因此我们可以自信地宣布：**新药确实显著有效，绝不是运气！**

> ⚠ 存在分歧：材料把 P 值说成"巧合的概率"。[CON-p-value](../../inference/CON-p-value.md#一句话定义) 的定义是"H₀ 为真时，出现至少这么极端的统计量的概率"，这是在假设 H₀ 成立的前提下算出来的，不是"结果由巧合造成"的概率。两种说法都保留，待 Li 裁定。另外，P 值小只能说明差异不太可能只是随机波动，"绝不是运气"的说法比统计结论更强。

### R 复核

```r
tab <- matrix(c(35, 15,
                20, 30), nrow = 2, byrow = TRUE)
res <- chisq.test(tab, correct = FALSE)
res                                   # X-squared = 9.0909, df = 1, p-value = 0.002569
res$expected                          # 27.5 / 22.5
(tab - res$expected)^2 / res$expected # 2.045 / 2.500
qchisq(0.95, df = 1)                  # 临界值 3.841
```

> 数值复核（Claude）：R 4.5.2 结果与材料一致：χ² = 9.091，p = 0.0026，期望频数 27.5 / 22.5，临界值 3.841。不加 `correct = FALSE` 时 R 默认做 Yates 连续性校正，得 χ² = 7.92，p = 0.0049（见下节）。两比例 z 检验（合并方差）得 z = 3.015，z² = 9.091，与 χ² 相等，印证 [CON-test-statistic](../../inference/CON-test-statistic.md) 中"2×2 表的 χ² = z²"。

## R 与 SAS：Yates 连续性校正

> 整理记录（2026-11-18）：本节从 [CON-test-selection](../../inference/CON-test-selection.md#3-卡方检验) 的数值复核原样移入（该处保留其算例的 P 值），作为 R / SAS 卡方默认设置的主卡。

R 的 `chisq.test()` 对 2×2 表默认做 Yates 连续性校正（`correct = TRUE`）。

> 数值复核（Claude，原写在 CON-test-selection 抗感染算例下）：所以同一张表"R 默认结果"和材料不同，要看是否加了 `correct = FALSE`。SAS PROC FREQ 的 `chisq` 选项两种都输出（"Chi-Square" 与 "Continuity Adj. Chi-Square"）。

CMH 检验的连续性校正默认（R `mantelhaen.test()` 与 SAS 不同）见 [MTH-CMH](MTH-CMH.md#程序里怎么做)。

## 拟合优度检验

> 补充（Claude）：拟合优度检验在 R 中写作 `chisq.test(c(52, 48), p = c(0.5, 0.5))`（示意：随机化后两组 52 / 48 人，χ² = 0.16，p = 0.69）。自由度是类别数 − 1。待 Li 核实。

## 相关卡片

- [CON-test-statistic](../../inference/CON-test-statistic.md)：χ² 统计量的一般形式及与 t、log-rank 的关系
- [CON-test-selection](../../inference/CON-test-selection.md#3-卡方检验)：卡方检验的适用条件（期望频数 ≥ 5）和 Fisher 的替代
- [CON-distribution-family](../../inference/CON-distribution-family.md)：χ² 分布的构造
- [CON-degrees-of-freedom](../../inference/CON-degrees-of-freedom.md)：列联表自由度
- [CON-p-value](../../inference/CON-p-value.md)：P 值的定义
- [MTH-CMH](MTH-CMH.md)：分层版本
- [CON-response-rate](CON-response-rate.md)：应答率的比较

## 出处

- Claude 对话（inbox: Chi-squared test_1.md），AI 生成，出处待补
