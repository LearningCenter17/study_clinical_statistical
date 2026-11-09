---
id: CON-t-distribution
title: "t 分布（Student's t Distribution）"
categories: [inference, t-distribution, degrees-of-freedom, null-distribution]
related: [CON-t-test-pvalue, CON-p-value, CON-test-statistic, CON-degrees-of-freedom, CON-distribution-family]
sources: ["Claude 对话（inbox: t_distribution.md）", "Claude 对话（inbox: t_conception.md）", "Claude 对话（inbox: distribution.md）"]
status: draft
updated: 2026-11-09
---

> 出处待补：本卡内容来自 Claude 对话（inbox: t_distribution.md、t_conception.md、distribution.md），属 AI 生成内容，未引用原始文献。

## 一句话定义

t 分布是一条概率分布曲线，描述 H₀ 成立时 t 值应该长什么样；它是 t 检验里把 t 值换成 P 值的那把"尺子"（t 检验 / t 值 / t 分布三者的区别见 [CON-t-test-pvalue](CON-t-test-pvalue.md#三个东西别混了)）。在假设检验中，它就是 t 统计量的零分布（见 [CON-p-value](CON-p-value.md)）。

## 只取决于自由度

t 分布的形状**只由自由度（df）决定**（自由度是什么、各检验怎么算见 [CON-degrees-of-freedom](CON-degrees-of-freedom.md)），和数据具体是什么无关：

- 不管测的是血压、体重还是 HbA1c；
- 不管数据均值是 5 还是 500，标准差是 0.1 还是 100；

只要自由度都是 20，用的就是同一条 t 分布曲线。

原因：t 值已经被"标准化"——分子除以标准误，单位和量级都被消掉，剩下的只是一个纯粹的倍数。所以数学家能提前把每个自由度的 t 分布算好，做成表格或函数，所有人通用。

**对于给定的自由度，t 分布是固定的；不同自由度对应不同的 t 分布**，所以它是一个"家族"，自由度是唯一的参数。

## 不变的特征

所有 t 分布都：

- 以 0 为中心，左右对称（H₀ 下差异为 0，正负偏离机会均等）；
- 钟形，看着像正态分布。

## 随自由度变化的特征

| 自由度 | 形状 |
|---|---|
| 小 | 峰矮、尾巴胖，极端值更常见 |
| 大 | 越来越瘦高，逐渐逼近标准正态分布 |
| → ∞ | 就是标准正态分布 |

尾巴胖是因为样本少时，分母里的标准差本身也估计得不准，额外放大 t 值的波动。这也是为什么同样 t = 2，df = 4 时 P = 0.12，df → ∞ 时 P = 0.046（见 [CON-t-test-pvalue](CON-t-test-pvalue.md#规律-2自由度样本量影响翻译)）。

### 多大的样本可以当 Z 分布用？⚠ 存在分歧（程度上的）

- **说法 A**（来源：distribution.md）："n ≥ 30 时，t 分布几乎与 Z 分布一致""当样本量够大（n ≥ 30）时，t 分布就和 Z 分布长得一模一样了"。适用场景概括为：**总体方差未知 + 小样本 ⇒ 用 t 分布**。
- **说法 B**（来源：本卡与 [CON-degrees-of-freedom](CON-degrees-of-freedom.md) 的临界值表）：t 分布**只有 df → ∞ 时才等于**标准正态；df = 30 时双侧 0.05 临界值是 2.04，Z 是 1.96，仍有差别。

两者不完全矛盾，"n ≥ 30"是教科书的经验门槛，说"几乎一致"大致可以，说"一模一样"偏绝对。

> 补充（Claude）：实务中总体方差总是未知的，所以软件（SAS PROC TTEST、R `t.test()`）不论样本大小都直接用 t 分布，不存在"n ≥ 30 就改用 Z"这一步；"n ≥ 30 用 Z"主要是查表时代的简化。待 Li 核实。

t 分布在整个分布家族（伯努利 → 二项 → 正态 → Z → t / χ² / F）中的位置见 [CON-distribution-family](CON-distribution-family.md)。

## 与正态分布对比

| | 参数 |
|---|---|
| 正态分布 | 两个：均值 μ、标准差 σ |
| t 分布（标准形式） | 一个：df |

这也是它好用的原因：一个自由度就锁定一条曲线，查起来非常方便。

## 实现

```r
pt(q, df)        # 累积概率；双侧 P = 2 * pt(-abs(t), df)
qt(0.975, df)    # 双侧 α = 0.05 的临界值
```

> 补充（Claude）：SAS 中对应函数为 `probt(t, df)`（累积概率）和 `tinv(p, df)`（分位数）。待 Li 核实。

## 相关卡片

- [CON-t-test-pvalue](CON-t-test-pvalue.md)
- [CON-p-value](CON-p-value.md)：零分布
- [CON-test-statistic](CON-test-statistic.md)：t、χ²、F 各自对应的分布

## 出处

- Claude 对话（inbox: t_distribution.md；AI 生成，原始出处待补）
- Claude 对话（inbox: t_conception.md；AI 生成，原始出处待补）
- Claude 对话（inbox: distribution.md；AI 生成，原始出处待补）
