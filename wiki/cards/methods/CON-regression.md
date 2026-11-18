---
id: CON-regression
title: "回归是什么：系数、校正后的治疗效应与按结局分的回归家族（Regression）"
categories: [overview, regression, linear-regression, logistic, cox, negative-binomial, poisson, glm, ols, covariate, regression-to-the-mean]
related: [CON-covariate, MTH-MMRM, CON-odds-ratio, CON-hazard-ratio, CON-survival-analysis-overview, CON-confirmatory-methods-overview, CON-degrees-of-freedom]
sources: ["Claude 对话（inbox: regression.md）"]
status: draft
updated: 2026-11-18
---

> 出处待补：本卡内容来自 Claude 对话（inbox: regression.md），属 AI 生成内容，未引用原始文献。材料后半部分"普通回归为什么处理不了删失、怎么用似然改造"放在 [CON-survival-analysis-overview](tte/CON-survival-analysis-overview.md#普通回归为什么处理不了删失)。

## 一句话定义

"回归"在统计里就是**用一个或几个变量去解释、预测另一个变量，并且量化它们之间的关系**。

## 一个直观例子

想知道身高和体重的关系。收集 100 个人的数据画成散点图，会看到大致"越高越重"的趋势。回归就是在这堆点里找一条**最能代表这个趋势的线**：

> 体重 = −100 + 1.0 × 身高(cm)

这条线能告诉你两件事：

- **关系有多大**：身高每多 1 cm，体重平均多 1 kg。这个 1.0 就是**回归系数**。
- **预测**：给一个身高 175 cm 的人，可以预测他的体重约 75 kg。

其中，被解释的变量（体重）叫**因变量、结局变量**；用来解释它的变量（身高）叫**自变量、预测变量、协变量**。

## 在临床试验里的用法

自变量通常放"治疗组别"，再加上年龄、基线值、分层因素等：

> 第 12 周疼痛评分变化 = β₀ + β₁ × 治疗组 + β₂ × 基线评分 + …

β₁ 就是"在其他因素相同的情况下，治疗组比对照组平均差多少"，也就是**校正后的治疗效应**。临床试验里常见的 ANCOVA、MMRM，本质上都是回归。

→ 为什么要调整协变量、ANOVA → ANCOVA、常见协变量见 [CON-covariate](continuous/CON-covariate.md)；MMRM 见 [MTH-MMRM](continuous/MTH-MMRM.md)。

## "回归"这个名字是怎么来的

这个词来自 19 世纪的英国学者高尔顿（Francis Galton）。他研究父母和子女的身高，发现特别高的父母，孩子往往没那么高；特别矮的父母，孩子往往没那么矮。子女身高有**"回归"到平均水平**的倾向，这就是"回归均值"（regression toward the mean）。他用来分析这种关系的方法后来就沿用了"回归"这个名字。如今这个词已经和"回到平均"的本义无关，泛指上面说的这类建模方法。

> 补充（Claude）：回归均值在临床试验里仍是一个实际问题：按"基线评分高于某值"入组时，即使无治疗，随访时评分也会平均回落一些。这是需要安慰剂对照、并在分析中调整基线值的原因之一。待 Li 核实。

## 按结局类型分家族

| 结局变量类型 | 回归方法 | 效应量 |
|---|---|---|
| 连续数值（血压、评分） | 线性回归 | 均值差 |
| 二分类（有效/无效） | 逻辑回归 | 比值比 OR |
| 计数（发作次数） | 泊松 / 负二项回归 | 率比 RR |
| 带删失的事件时间 | **Cox 回归** | 风险比 HR |

"普通回归"主要指第一行的线性回归，而 Cox 模型就是这个家族里专门处理生存数据的成员。

> 补充（Claude）：表中计数终点的"率比 RR"是 rate ratio，和 [CON-odds-ratio](binary/CON-odds-ratio.md#五和另外两个指标的区别) 里的相对危险度 RR（relative risk）缩写相同、含义不同，读 TLF 时要看清。OR 见 CON-odds-ratio，HR 见 [CON-hazard-ratio](tte/CON-hazard-ratio.md)；logistic 回归、负二项回归尚无独立卡片（待建）。

## 普通回归是什么

一般指线性回归（Linear Regression，常用最小二乘法 OLS 求解）：

$$Y = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + \dots + \text{误差}$$

它用自变量 X（治疗组、年龄、基线指标……）去解释和预测一个连续的结局 Y（血压、体重、某项评分……）。它有一个默认前提：每个人的 Y 都是确切观测到的。

广义上还包括逻辑回归（Logistic Regression，结局是"是/否"）等，统称广义线性模型。

普通回归本身无法处理删失，为什么以及怎么改造，见 [CON-survival-analysis-overview](tte/CON-survival-analysis-overview.md#普通回归为什么处理不了删失)。

> 补充（Claude）：线性回归残差的自由度是 n − 参数个数，见 [CON-degrees-of-freedom](../inference/CON-degrees-of-freedom.md#常见检验的自由度)。

## 相关卡片

- [CON-covariate](continuous/CON-covariate.md)：协变量调整、ANCOVA
- [MTH-MMRM](continuous/MTH-MMRM.md)：重复测量的回归模型
- [CON-odds-ratio](binary/CON-odds-ratio.md)：逻辑回归的效应量
- [CON-hazard-ratio](tte/CON-hazard-ratio.md)：Cox 回归的效应量
- [CON-survival-analysis-overview](tte/CON-survival-analysis-overview.md)：删失与似然
- [CON-confirmatory-methods-overview](CON-confirmatory-methods-overview.md)：各回归方法在确证性试验中的地位

## 出处

- Claude 对话（inbox: regression.md；AI 生成，原始出处待补）
