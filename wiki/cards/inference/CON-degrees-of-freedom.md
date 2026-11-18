---
id: CON-degrees-of-freedom
title: "自由度（Degrees of Freedom, df）"
categories: [inference, degrees-of-freedom, t-distribution, chi-square, variance]
related: [CON-t-distribution, MTH-t-test, CON-test-statistic, MTH-MMRM, CON-distribution-family, CON-p-value, GOT-ttest-student-vs-welch, CON-test-selection, CON-normal-distribution, CON-confidence-interval, MTH-ci-construction, MTH-chi-square, CON-chi-square-distribution, MTH-breslow-day]
sources: ["Claude 对话（inbox: degreeOfFreedom.md）"]
status: draft
updated: 2026-11-18
---

> 出处待补：本卡内容来自 Claude 对话（inbox: degreeOfFreedom.md），属 AI 生成内容，未引用原始文献。临界值表已移到 CON-t-distribution（见下文）。

## 一句话定义

**自由度 = 能自由变动、不受约束的数据个数。** 英文 degrees of freedom，缩写 df。

## 最经典的例子

随便写 3 个数，没有任何限制：3 个都能随便写，自由度 = 3。

加一个条件：**这 3 个数的平均值必须是 10**：

- 第 1 个数：随便写，如 5
- 第 2 个数：随便写，如 12
- 第 3 个数：**不能随便写了**，必须是 13（总和得是 30）

加了一个约束，就少了一个自由度：3 − 1 = 2。

## 为什么算标准差时会用掉一个自由度

算样本标准差要先算样本均值，再看每个数偏离均值多少。均值是从这批数据里算出来的，相当于给数据加了一个"偏差之和必须为 0"的约束，所以 n 个数据里只有 n − 1 个偏差是真正独立的信息。这也是为什么**样本方差公式分母是 n − 1 而不是 n**。

## 自由度为什么重要：决定零分布的形状

- **自由度小**（样本少）：用样本标准差估计总体标准差不太靠谱，不确定性大，t 分布尾巴很胖，需要更大的 t 值才能拒绝 H₀；
- **自由度大**（样本多）：估计越来越准，t 分布越来越接近正态分布。

形状变化的细节，以及双侧 P = 0.05 对应的临界 t 值随 df 变化的数值表（df = 2 时 4.30，df → ∞ 时 1.96），见 [CON-t-distribution](CON-t-distribution.md#数值临界值与同一个-t-的-p-值)。

> 整理记录（2026-11-17）：本节原有的临界 t 值表（来源：degreeOfFreedom.md）已移到 CON-t-distribution，与其他卡片中的同类数值合并为一张表，避免重复。

## 常见检验的自由度

| 检验 | 自由度 |
|---|---|
| 单样本 t 检验 | n − 1 |
| 两独立样本 t 检验（方差齐） | n₁ + n₂ − 2（每组各用掉一个来估计均值） |
| 配对 t 检验 | 配对数 − 1 |
| χ² 检验（r 行 × c 列表） | (r − 1)(c − 1) |
| 线性回归残差 | n − 参数个数 |

通用规律：**样本量减去你从数据里估计了几个参数**。每估计一个参数，就用掉一个自由度。

> 补充（Claude）：
>
> - χ² 列联表的 df 不是"样本量 − 参数数"，而是"格子数 − 约束数"：行合计和列合计固定后，(r − 1)(c − 1) 个格子可以自由填。思路相同（约束用掉自由度），但计数对象是格子而不是受试者。2×2 表 4 项相加为什么只相当于 1 个 Z² 的直观解释见 [CON-chi-square-distribution](CON-chi-square-distribution.md#两个近似要注意)。
> - 自由度不一定是整数：方差不齐时的 Welch / Satterthwaite t 检验（SAS PROC TTEST 的 Satterthwaite 行），以及 [MMRM](../methods/continuous/MTH-MMRM.md) 中的 Kenward-Roger 方法，都用近似公式算出非整数 df。所以 SAS 与 R 结果的 P 值差异，常要先核对 df 方法（t 检验的例子见 [GOT-ttest-student-vs-welch](../methods/continuous/GOT-ttest-student-vs-welch.md)）。
> - 待 Li 核实。

## 相关卡片

- [CON-t-distribution](CON-t-distribution.md)：自由度决定 t 分布形状
- [MTH-t-test](../methods/continuous/MTH-t-test.md)：自由度影响 t → P 的"翻译"
- [CON-test-statistic](CON-test-statistic.md)：χ² 等其他统计量
- [MTH-MMRM](../methods/continuous/MTH-MMRM.md)：Kenward-Roger 自由度

## 出处

- Claude 对话（inbox: degreeOfFreedom.md；AI 生成，原始出处待补）
