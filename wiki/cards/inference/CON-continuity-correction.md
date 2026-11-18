---
id: CON-continuity-correction
title: "连续性校正：用连续分布近似离散计数时的半格修正（Continuity Correction / Yates' Correction）"
categories: [inference, continuity-correction, yates, normal-approximation, chi-square, cmh, mcnemar, wilcoxon, binomial, sample-size]
related: [GOT-continuity-correction-r-vs-sas, MTH-chi-square, CON-chi-square-distribution, MTH-CMH, CON-test-selection, CON-test-statistic, MTH-ci-construction, CON-unequal-allocation, CON-distribution-family]
sources: ["Claude 对话（inbox: Continuity correction.md）"]
status: draft
updated: 2026-11-18
---

> 出处待补：本卡内容来自 Claude 对话（inbox: Continuity correction.md），属 AI 生成内容，未引用原始文献。抛硬币和 Yates 算例的数值已由 Claude 在 R 4.5.2 中复核。R / SAS 的默认设置见 [GOT-continuity-correction-r-vs-sas](../methods/binary/GOT-continuity-correction-r-vs-sas.md)。

## 一句话定义

**用连续的分布（正态、卡方）去近似离散的计数时，做的一个"半格"修正。** 具体做法是把偏差 |O − E| 先减去 0.5，然后再参与计算。

## 为什么需要它

人数只能是整数：0、1、2、3……，是**一级一级的台阶**。而正态分布和卡方分布是**光滑的曲线**。拿光滑曲线去近似台阶，在边界上就会有误差。

可以把每个整数想象成一根**宽度为 1 的柱子**，比如"8"这根柱子实际上占据的是 7.5 到 8.5 这一段。如果要算"≥ 8"的概率，曲线下的面积应该从 **7.5** 开始算，而不是从 8 开始。如果从 8 开始，就漏掉了 8 号柱子的左半边。

这个"往外让半格"的修正就叫连续性校正。

> 补充（Claude）：二项 → 正态近似本身见 [CON-distribution-family](CON-distribution-family.md#二项--正态的近似条件)；卡方检验为什么是"近似"见 [CON-chi-square-distribution](CON-chi-square-distribution.md#两个近似要注意)。

## 一个直观的例子：抛硬币

抛 10 次硬币，问正面 ≥ 8 次的概率是多少？

**精确答案**（二项分布直接算）：

$$P(X \ge 8) = \frac{45 + 10 + 1}{1024} = 0.0547$$

**用正态近似**：均值 = 5，标准差 = √2.5 ≈ 1.58

| 方法 | 计算 | 结果 |
|---|---|---|
| 不校正 | P(Z ≥ (8 − 5)/1.58) = P(Z ≥ 1.90) | 0.029 ❌ 差了近一半 |
| 校正 | P(Z ≥ (7.5 − 5)/1.58) = P(Z ≥ 1.58) | **0.057** ✅ 接近 0.0547 |

样本小的时候，不校正会明显**低估 p 值**，让结果看起来比实际更显著。

> 数值复核（Claude）：`sum(dbinom(8:10, 10, 0.5))` = 0.0547；P(Z ≥ 1.897) = 0.0289；P(Z ≥ 1.581) = 0.0569。与材料一致。

## 用在卡方检验上：Yates 校正

对 2×2 表的卡方检验做连续性校正，叫做 **Yates 校正**（Yates' continuity correction），公式是：

$$\chi^2_{\text{Yates}} = \sum \frac{(|O - E| - 0.5)^2}{E}$$

用头痛的例子（偏差 |O − E| = 7.5）：

| | 偏差 | χ² | p 值 |
|---|---|---|---|
| 不校正 | 7.5 | 5.88 | 0.015 |
| Yates 校正 | 7.5 − 0.5 = **7.0** | **5.12** | **0.024** |

校正后 χ² 变小，p 值变大，结论更**保守**。

> 数值复核（Claude）：头痛例子的原始 2×2 表不在本材料中（同 [CON-chi-square-distribution](CON-chi-square-distribution.md#两个近似要注意) 的待补说明）。2×2 表四格偏差相等，所以 χ²_Yates = 5.88 × (7.0 / 7.5)² = 5.12，df = 1 时 p = 0.0236，与材料一致。另一个可复核的例子：[MTH-chi-square](../methods/binary/MTH-chi-square.md#r-复核) 的降压药 2×2 表，不校正 χ² = 9.09，Yates 校正 7.92。

CMH 也有同样的校正：分子从 [Σ(aₖ − Eₖ)]² 改为 (|Σ(aₖ − Eₖ)| − 0.5)²（CMH 本身见 [MTH-CMH](../methods/binary/MTH-CMH.md)）。

## 要不要用？

这一点统计学界一直有争议：

- **支持用的观点**：样本小时可以避免 p 值被低估，防止假阳性。
- **反对用的观点**：Yates 校正往往**矫枉过正**，p 值偏大、检验效能偏低。而且样本真小的时候，**直接用 Fisher 精确检验更好**，不需要靠近似加修正。样本大的时候，校正与否几乎没有区别。

现在比较主流的做法是：**样本够大就用不校正的 Pearson 卡方，样本小就用 Fisher 精确检验**，Yates 校正用得越来越少。临床试验里具体用哪个，以 SAP 的规定为准。

> 补充（Claude）："样本够大 / 样本小"的判据（期望频数 ≥ 5）见 [CON-test-selection](CON-test-selection.md#4-fisher-确切概率法)。

## 常见的使用场景

连续性校正只有一个使用场景：**把离散的计数结果，用连续分布（正态或卡方）去近似的时候。** 只要满足这一条，原则上就可以加校正。

**1. 2×2 卡方检验（Yates 校正）**

就是前面讲的情况。注意只用于 **2×2 表**（自由度 = 1）。更大的表（比如 3×2）一般不做校正，R 的 `chisq.test()` 对大表也不会自动加。

**2. CMH 检验**

分层的 2×2 表，原理相同。

**3. 两个比率的比较（z 检验）**

比如比较两组应答率，用正态近似：

$$z = \frac{|p_1 - p_2| - \text{校正项}}{SE}$$

它和 2×2 卡方检验等价，所以校正方式也对应。

**4. 单个比率的检验和置信区间**

比如"应答率是否高于 30%"，或者计算应答率的 95% 置信区间：

- 用正态近似的 **Wald 区间**可以加校正，每端往外扩 1/(2n)
- **Wilson 区间**也有带校正的版本
- **差值的置信区间**（比如两组应答率之差的 95% CI）同样可以加校正

这在疗效 TLF 里非常常见。（各类 CI 的构造方法见 [MTH-ci-construction](MTH-ci-construction.md)。）

**5. McNemar 检验（配对数据）**

比如同一批病人治疗前后是否应答：

$$\chi^2 = \frac{(|b - c| - 1)^2}{b + c}$$

b、c 是"前后结果不一致"的两个格子。注意这里减的是 **1** 而不是 0.5，因为统计量是基于两个计数的差。

**6. 非参数检验的正态近似**

比如 **Wilcoxon 秩和检验**、**符号秩检验**。样本较大时会用正态近似算 p 值，秩和也是离散的，所以也会加 0.5 校正。

**7. 样本量计算**

方案里根据应答率计算样本量时，有的公式（比如 Fleiss 公式）有带校正的版本，算出来的样本量会稍大一些（算例见 [CON-unequal-allocation](../design/CON-unequal-allocation.md)）。

## 不需要校正的情况

| 方法 | 原因 |
|---|---|
| Fisher 精确检验 | 直接用精确的离散分布计算，不做近似 |
| 精确二项检验 / Clopper-Pearson 区间 | 同上 |
| t 检验、ANCOVA | 数据本来就是连续的 |
| Log-rank、Cox 回归 | 不是基于这种计数近似 |
| 大于 2×2 的卡方检验 | 通常不做 |

## 在 TLF 里会碰到的地方

| TLF | 可能涉及的方法 |
|---|---|
| 二分类疗效终点表（如 ACR20 应答率） | 应答率的 95% CI、组间差值的 95% CI、CMH p 值 |
| 配对比较（如治疗前后转阴） | McNemar 检验 |
| 非参数分析（如评分数据） | Wilcoxon 检验 |
| 方案 / SAP 的样本量部分 | 带或不带校正的样本量公式 |

R 和 SAS 在这些方法上的默认设置不同，双编程核对时要先对齐，见 [GOT-continuity-correction-r-vs-sas](../methods/binary/GOT-continuity-correction-r-vs-sas.md)。

## 相关卡片

- [GOT-continuity-correction-r-vs-sas](../methods/binary/GOT-continuity-correction-r-vs-sas.md)：R / SAS 默认是否校正
- [MTH-chi-square](../methods/binary/MTH-chi-square.md)：Pearson 卡方检验
- [CON-chi-square-distribution](CON-chi-square-distribution.md)：卡方检验为什么是近似
- [MTH-CMH](../methods/binary/MTH-CMH.md)：分层 2×2 表
- [CON-test-selection](CON-test-selection.md)：卡方 vs Fisher
- [MTH-ci-construction](MTH-ci-construction.md)：比例和率差的 CI
- [CON-unequal-allocation](../design/CON-unequal-allocation.md)：Fleiss 校正的样本量

## 出处

- Claude 对话（inbox: Continuity correction.md；AI 生成，原始出处待补）
