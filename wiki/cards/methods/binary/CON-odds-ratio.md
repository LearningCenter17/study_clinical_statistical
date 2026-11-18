---
id: CON-odds-ratio
title: "优势比 OR：odds、OR 与率差 RD、相对危险度 RR 的区别（Odds Ratio）"
categories: [binary-endpoint, odds, odds-ratio, relative-risk, risk-difference, cross-product-ratio, effect-measure, logistic, tlf]
related: [CON-response-rate, MTH-CMH, MTH-chi-square, CON-confidence-interval, MTH-ci-construction, MTH-proportional-odds-model, GOT-ordinal-or-direction, CON-confirmatory-methods-overview]
sources: ["Claude 对话（inbox: odds ratio.md）"]
status: draft
updated: 2026-11-18
---

> 出处待补：本卡内容来自 Claude 对话（inbox: odds ratio.md），属 AI 生成内容，未引用原始文献。所有算例数值已由 Claude 在 R 4.5.2 中复核。

OR 是 **Odds Ratio** 的缩写，中文叫**优势比**（也叫比值比）。要理解它，得先弄清楚 **odds** 是什么。

## 一、先理解 odds（优势、赔率）

**概率**和 **odds** 是描述同一件事的两种方式：

| | 定义 | 例子：100 人里 80 人应答 |
|---|---|---|
| **概率**（probability） | 发生的人数 ÷ **总人数** | 80/100 = **0.8**（80%） |
| **Odds** | 发生的人数 ÷ **没发生的人数** | 80/20 = **4** |

odds = 4 的意思是：**应答的人数是不应答的 4 倍**，也可以说成"4 比 1"。赌博里说的"赔率 4 比 1"，就是这个概念。

两者可以互相换算：

$$\text{odds} = \frac{p}{1 - p}, \qquad p = \frac{\text{odds}}{1 + \text{odds}}$$

一些对照：

| 概率 | 50% | 70% | 80% | 90% | 10% |
|---|---|---|---|---|---|
| Odds | 1 | 2.33 | 4 | 9 | 0.11 |

概率只能在 0 到 1 之间，odds 的范围则是 0 到无穷大。

> 补充（Claude）：应答概率 p 与应答率 p̂ 的区别见 [CON-response-rate](CON-response-rate.md)。

## 二、OR 就是两组 odds 的比

$$OR = \frac{\text{药物组的 odds}}{\text{安慰剂组的 odds}}$$

例子：

| | 应答 | 不应答 | Odds |
|---|---|---|---|
| 药物组 | 48 | 12 | 48/12 = **4.0** |
| 安慰剂 | 168 | 72 | 168/72 = **2.33** |

$$OR = 4.0 / 2.33 \approx 1.71$$

意思是：**药物组应答的 odds 是安慰剂组的 1.71 倍。**

> 整理记录（2026-11-18）：材料原文写"用前面第 1 层的例子"，指的是更早一段对话里的数据，本卡直接给出该表（药物组 48/60 = 80%，安慰剂 168/240 = 70%）。

## 三、2×2 表的简便公式

| | 应答 | 不应答 |
|---|---|---|
| 药物组 | a | b |
| 安慰剂 | c | d |

$$OR = \frac{a/b}{c/d} = \frac{a \times d}{b \times c}$$

就是**对角线相乘再相除**，所以 OR 也叫"交叉乘积比"（cross-product ratio）。前面 CMH 和卡方公式里出现的 **ad − bc**，也跟这个有关：两组没差别时 ad = bc，OR = 1。

> 补充（Claude）：本库的 [MTH-chi-square](MTH-chi-square.md) 和 [MTH-CMH](MTH-CMH.md) 用的是 O − E（观察 − 期望）的写法，没有直接出现 ad − bc；2×2 表中 a − E(a) = (ad − bc) / N，所以两种写法等价。待 Li 核实。

## 四、怎么解读

| OR | 含义（以应答为例） |
|---|---|
| **OR = 1** | 两组没有差别 |
| **OR > 1** | 药物组更容易应答（药物有利） |
| **OR < 1** | 药物组更不容易应答 |

如果结局是**坏事**（比如不良事件），方向就反过来：OR > 1 表示药物组更容易发生不良事件。

一般还会报告 **95% 置信区间**：

- 区间**不包含 1**，比如 (1.2, 2.5)：差异有统计学意义
- 区间**包含 1**，比如 (0.8, 2.1)：差异不显著

比值类指标的"无差别值"是 1、差值类是 0，这一对应关系的通用说明见 [CON-confidence-interval](../../inference/CON-confidence-interval.md)。

## 五、和另外两个指标的区别

同样用 80% vs 70% 这组数据：

| 指标 | 英文 | 计算 | 结果 | 含义 |
|---|---|---|---|---|
| **率差** | Risk Difference (RD) | 80% − 70% | **10%** | 药物组应答率高 10 个百分点 |
| **相对危险度** | Relative Risk (RR) | 80% / 70% | **1.14** | 药物组应答概率是安慰剂组的 1.14 倍 |
| **优势比** | Odds Ratio (OR) | 4.0 / 2.33 | **1.71** | 药物组应答 odds 是安慰剂组的 1.71 倍 |

**一个常见误区：** OR = 1.71 **不等于**"药物组应答的可能性是安慰剂组的 1.71 倍"。那是 RR 的含义，这里的 RR 只有 1.14。

只有当事件**很少见**（发生率低于约 10%）时，OR 才接近 RR。比如 2% vs 1%：RR = 2.0，OR ≈ 2.02，几乎一样。但像 ACR20 应答率这种常见的结局，OR 会明显**夸大**倍数关系。

## 六、为什么统计上常用 OR

既然 OR 不如 RR 直观，为什么还用得这么多？

1. **logistic 回归直接给出的就是 OR。** 回归系数取指数 exp(β) 就是 OR。调整协变量的二分类分析基本都用 logistic 回归。
2. **数学性质好。** OR 的取值范围是 0 到无穷大，没有上限的问题；RR 会受限制，比如安慰剂组应答率已经 70%，RR 最大也只能是 1/0.7 ≈ 1.43。
3. **对称性。** 把"应答"换成"不应答"来分析，OR 正好变成倒数（1.71 → 0.58），RR 就没有这个性质。
4. **病例对照研究只能算 OR。** 这是流行病学里 OR 的主要来源。
5. **CMH 和 Breslow-Day 都基于 OR**（见 [MTH-CMH](MTH-CMH.md#二分类终点分层比较应答率)）。

> 补充（Claude）：logistic 回归卡片待建（第 4 章）；有序终点的 OR（比例优势模型的共同 OR）见 [MTH-proportional-odds-model](../ordinal/MTH-proportional-odds-model.md)。

## 七、在临床试验 TLF 里

二分类疗效终点表（比如 ACR20 应答率）通常会同时报告：

- 各组应答率
- **率差**及其 95% CI：最直观，临床医生最容易理解
- **OR**（或 RR）及其 95% CI：来自 CMH 或 logistic 回归
- p 值

具体报告哪几个，以 SAP 的规定为准。率差 CI 的构造方法（Newcombe、Miettinen-Nurminen 等）见 [MTH-ci-construction](../../inference/MTH-ci-construction.md)。

```r
# R 计算 OR
tab <- matrix(c(48, 168, 12, 72), nrow = 2)   # 第1列应答，第2列不应答
(48 * 72) / (12 * 168)                         # 1.71

fisher.test(tab)$estimate     # 条件最大似然估计的 OR，和简单公式略有不同
fisher.test(tab)$conf.int     # 95% CI
```

```sas
proc freq data=adeff;
  tables trt01p*avalc / relrisk riskdiff;   /* relrisk 输出 OR 和 RR，riskdiff 输出率差 */
run;
```

> 数值复核（Claude，R 4.5.2）：简单公式 OR = 1.714；`fisher.test` 条件 MLE = 1.711，95% CI 0.83–3.76；log OR 的 Wald 95% CI 为 0.86–3.42。**这个例子的 CI 包含 1**（Pearson χ² 不校正 p = 0.12），即差异不显著，算例只用来演示 OR 怎么算。其他数值：RR = 1.143，2% vs 1% 时 OR = 2.020，1/0.7 = 1.43，1/1.714 = 0.583，均与材料一致。

> 补充（Claude）：SAS `PROC FREQ` 的 `RELRISK` 按表的**第 1 行比第 2 行、第 1 列为"事件"**计算。`TRT01P` 和 `AVALC` 默认按字母 / 格式值排序，如果"安慰剂"排在第 1 行或"N"排在第 1 列，输出的就是倒数或"不应答"的 OR。通常要用 `ORDER=DATA` / `ORDER=FORMATTED` 或排序变量控制行列顺序。同类方向问题见 [GOT-ordinal-or-direction](../ordinal/GOT-ordinal-or-direction.md)。SAS 代码未实际运行，待 Li 核实。

## 相关卡片

- [CON-response-rate](CON-response-rate.md)：应答概率与应答率
- [MTH-CMH](MTH-CMH.md)：分层的 MH 合并 OR、Breslow-Day
- [MTH-chi-square](MTH-chi-square.md)：2×2 表检验
- [CON-confidence-interval](../../inference/CON-confidence-interval.md)：比值的 CI 看是否包含 1
- [MTH-ci-construction](../../inference/MTH-ci-construction.md)：OR 在 log 尺度构造 CI、率差 CI 方法
- [MTH-proportional-odds-model](../ordinal/MTH-proportional-odds-model.md)：有序终点的共同 OR
- [GOT-ordinal-or-direction](../ordinal/GOT-ordinal-or-direction.md)：OR 方向互为倒数的坑

## 出处

- Claude 对话（inbox: odds ratio.md；AI 生成，原始出处待补）
