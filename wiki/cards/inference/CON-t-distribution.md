---
id: CON-t-distribution
title: "t 分布（Student's t Distribution）"
categories: [inference, t-distribution, degrees-of-freedom, null-distribution]
related: [MTH-t-test, CON-p-value, CON-test-statistic, CON-degrees-of-freedom, CON-distribution-family, CON-normal-distribution, CON-confidence-interval, MTH-ci-construction]
sources: ["Claude 对话（inbox: t_distribution.md）", "Claude 对话（inbox: t_conception.md）", "Claude 对话（inbox: distribution.md）", "Claude 对话（inbox: degreeOfFreedom.md）", "Claude 对话（inbox: PValue_ttest.md）", "Claude 对话（inbox: t_test_mean.md）", "Claude 对话（inbox: pvalue_tvalue.md）"]
status: draft
updated: 2026-11-17
---

> 出处待补：本卡内容来自 Claude 对话（inbox: t_distribution.md、t_conception.md、distribution.md、degreeOfFreedom.md、PValue_ttest.md、t_test_mean.md、pvalue_tvalue.md），属 AI 生成内容，未引用原始文献。

## 一句话定义

t 分布是一条概率分布曲线，描述 H₀ 成立时 t 值应该长什么样；它是 t 检验里把 t 值换成 P 值的那把"尺子"（t 检验 / t 值 / t 分布三者的区别见 [MTH-t-test](../methods/continuous/MTH-t-test.md#三个东西别混了)）。在假设检验中，它就是 t 统计量的零分布（见 [CON-p-value](CON-p-value.md)）。

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

尾巴胖是因为样本少时，分母里的标准差本身也估计得不准，额外放大 t 值的波动。这也是为什么同样 t = 2，df = 4 时 P = 0.12，df → ∞ 时 P = 0.046（见下表）。

### 数值：临界值与同一个 t 的 P 值

> 整理记录（2026-11-17）：下表合并了原先分散在 CON-degrees-of-freedom（临界值表）、MTH-t-test（"规律 2"及 df 梯度表）中的数值，内容未改。来源：临界值 df = 2 / 5 / 10 / 30 / ∞ 来自 degreeOfFreedom.md；df = 4 的两列来自 PValue_ttest.md；df = 5 / 10 / 30 / ∞ 的 P 值来自 pvalue_tvalue.md。"—"表示材料未给出。

| 自由度 | 双侧 α = 0.05 的临界 t 值 | t = 2 时的双侧 P 值 |
|---|---|---|
| 2 | 4.30 | — |
| 4（每组 3 人） | 2.78 | 0.12（不显著） |
| 5 | 2.571 | ≈ 0.102 |
| 10 | 2.228 | ≈ 0.073 |
| 30 | 2.042 | ≈ 0.055 |
| ∞（正态） | 1.960 | ≈ 0.046（显著） |

样本很小时，t 要超过 4 才算显著；样本够大，接近 2 就够了。

样本少时标准误本身估得不准，t 分布的"尾巴"更厚，要求的证据更强，P 值偏大。样本多了 t 分布趋近正态分布——所以"t 大于约 2 就显著"是**大样本下**的经验。

自由度本身是什么、各检验的 df 怎么算见 [CON-degrees-of-freedom](CON-degrees-of-freedom.md)；同一 df 下 t 与 P 的一一对应及报告写法见 [MTH-t-test](../methods/continuous/MTH-t-test.md#什么时候一一对应)。

> 数值复核（Claude）：双侧 α = 0.05 的 t 临界值 t₀.₉₇₅,df：df = 2 → 4.303，4 → 2.776，5 → 2.571，10 → 2.228，30 → 2.042，∞ → 1.960；`2*pt(-2, df)` 在 df = 4、5、10、30、∞ 时分别为 0.116、0.1019、0.0734、0.0546、0.0455。与材料一致。（原分别记录在 CON-degrees-of-freedom 与 MTH-t-test 中。）

## t 与 z 的区别

（来源：t_test_mean.md）如果总体标准差已知，这个比值就是 z 值，服从标准正态分布。实际中总体标准差未知，只能用样本标准差估计，多引入一层不确定性（样本小时尤甚），所以它服从尾巴稍"胖"的 **t 分布**；自由度越大越接近正态（见上表）。名字来自 Student's t——Gosset 在健力士（Guinness）啤酒厂工作时提出。

> 整理记录（2026-11-17）：本段原为 MTH-t-test 的"为什么叫 t 不叫 z"一节，移到这里作为 t 与 z 关系的唯一出处。CI 计算中临界值用 1.96 还是 t 见 [MTH-ci-construction](MTH-ci-construction.md#196-还是-t-临界值)。

### 多大的样本可以当 Z 分布用？⚠ 存在分歧（程度上的）

- **说法 A**（来源：distribution.md）："n ≥ 30 时，t 分布几乎与 Z 分布一致""当样本量够大（n ≥ 30）时，t 分布就和 Z 分布长得一模一样了"。适用场景概括为：**总体方差未知 + 小样本 ⇒ 用 t 分布**。
- **说法 B**（来源：本卡上方的临界值表，原在 [CON-degrees-of-freedom](CON-degrees-of-freedom.md)）：t 分布**只有 df → ∞ 时才等于**标准正态；df = 30 时双侧 0.05 临界值是 2.04，Z 是 1.96，仍有差别。

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

- [MTH-t-test](../methods/continuous/MTH-t-test.md)
- [CON-p-value](CON-p-value.md)：零分布
- [CON-test-statistic](CON-test-statistic.md)：t、χ²、F 各自对应的分布

## 出处

- Claude 对话（inbox: t_distribution.md；AI 生成，原始出处待补）
- Claude 对话（inbox: t_conception.md；AI 生成，原始出处待补）
- Claude 对话（inbox: distribution.md；AI 生成，原始出处待补）
- Claude 对话（inbox: degreeOfFreedom.md；AI 生成，原始出处待补；临界值表）
- Claude 对话（inbox: PValue_ttest.md；AI 生成，原始出处待补；df = 4 的数值）
- Claude 对话（inbox: t_test_mean.md；AI 生成，原始出处待补；t 与 z 的区别）
- Claude 对话（inbox: pvalue_tvalue.md；AI 生成，原始出处待补；df 梯度的 P 值）
