---
id: CON-test-statistic
title: "检验统计量：t、χ² 与 log-rank（Test Statistics）"
categories: [inference, test-statistic, t-test, chi-square, log-rank, hypothesis-testing]
related: [CON-p-value, MTH-t-test, CON-logrank-vs-cox, CON-null-hypothesis, CON-t-distribution, CON-degrees-of-freedom, CON-distribution-family, CON-type-I-II-error, CON-test-selection, CON-normal-distribution, CON-response-rate, MTH-CMH, MTH-chi-square]
sources: ["Claude 对话（inbox: Test_statistic.md）", "Claude 对话（inbox: calculate_pvalue.md）"]
status: draft
updated: 2026-11-18
---

> 出处待补：本卡内容来自 Claude 对话（inbox: Test_statistic.md、calculate_pvalue.md），属 AI 生成内容，未引用原始文献。

## 一句话定义

**不同类型的数据"偏离 H₀"的方式不一样，需要不同的尺子来量**；但几乎所有检验统计量都是同一个骨架：

> **（观察到的 − H₀ 下期望的）/ 随机波动的大小**

区别只在于"观察到的是什么"和"波动怎么算"。每个统计量在 H₀ 成立时都服从一个**已知分布**（t 分布、χ² 分布……），这样才能算出 P 值（见 [CON-p-value](CON-p-value.md)）。选哪个统计量，本质上是选"哪个数字在这种数据下有可靠的已知分布"。

## 为什么 t 值不够用

| 统计量 | 适用数据 | 做法 | t 检验为什么不行 |
|---|---|---|---|
| **t** | 连续数值，可以求均值，且均值大致服从正态 | 均值差 / 标准误（见 [MTH-t-test](../methods/continuous/MTH-t-test.md)） | — |
| **χ²** | 计数 / 分类数据，如"A 组 30 人中 12 人缓解，B 组 30 人中 5 人缓解" | 比较每个格子的观察频数与 H₀ 下期望频数：Σ (O − E)² / E | 每人只有"缓解 / 未缓解"，没有有意义的均值和标准差（硬算也行，但多组多类别时不自然） |
| **Log-rank** | 有删失的生存时间 | 在每个事件时间点，看两组"实际发生几个事件"与"两组风险一样时应发生几个"，把 (O − E) 累加再标准化；删失者在被删失前正常计入风险集，信息不浪费 | 有人失访、有人到研究结束仍未发生事件，真实生存时间未知，**没法求均值**；把删失时间当真实值做 t 检验会严重偏倚 |

## 对照表

| | t 检验 | χ² 检验 | Log-rank |
|---|---|---|---|
| 数据类型 | 连续 | 分类 / 计数 | 生存时间（含删失） |
| 比较的是 | 均值 | 频数 / 比例 | 整条生存曲线 |
| 临床例子 | 血压、HbA1c 变化 | 缓解率、AE 发生率 | OS、PFS |
| 对应 ADaM | ADLB、ADVS（CHG） | ADSL、ADAE 计数 | ADTTE（AVAL + CNSR） |

> 补充（Claude）：ADaM 一行是粗略对应。缓解率等疗效应答终点通常来自 BDS 结构的疗效数据集（如 ADRS、ADEFF 中的 AVALC 或 CRITy / CRITyFL），而不是 ADSL；ADSL 主要提供人群标志和分组。待 Li 结合项目规格核实。

## 它们是"亲戚"

- 2×2 表的 χ² 值 = 比较两个比例的 z 值的平方
- t² = 两组时的 F 值（ANOVA）
- Log-rank 统计量按 χ²(1) 分布算 P 值，可看作每个事件时间点上一系列 2×2 表的汇总（与 Mantel-Haenszel 检验同源）

所以与其说"有这么多种统计量"，不如说是**同一个思想针对不同数据结构的不同实现**。

> 补充（Claude）：第一条严格成立于 Pearson χ²（不加连续性校正）与合并方差的两比例 z 检验之间；带 Yates 连续性校正的 χ² 数值不同，R / SAS 的默认设置见 [MTH-chi-square](../methods/binary/MTH-chi-square.md#r-与-sasyates-连续性校正)。Mantel-Haenszel 的分层版本即 CMH 检验，见 [MTH-CMH](../methods/binary/MTH-CMH.md)。已由 Claude 按公式复核三条关系。
>
> 整理记录（2026-11-18）：原句"SAS PROC FREQ 同时输出带 Yates 连续性校正的 χ²"已归入 [MTH-chi-square](../methods/binary/MTH-chi-square.md#r-与-sasyates-连续性校正)，本处改为链接；"CMH 检验（第 4 章待建）"改为指向已建的 MTH-CMH。

## 统计量与零分布总表

> 整理记录（2026-11-17）：本节合并了原先分散在三张卡片中的同类表格，作为"哪种检验用哪个零分布"的唯一出处，内容未改：
>
> - CON-p-value"不同检验用不同的参照分布"的表格与说明（来源：calculate_pvalue.md）→ 下表"检验统计量""H₀ 下的分布""R 求 P 值"三列及表后前两条说明
> - CON-distribution-family"和检验统计量的对应"表（Claude 整理，非材料原文）→ 下表"作为零分布用于"一列

思路都一样：构造统计量，再查对应分布的尾巴。只是参照分布不同（来源：calculate_pvalue.md）：

| 检验 | 检验统计量 | H₀ 下的分布 | 作为零分布用于（Claude 整理） | R 求 P 值 |
|---|---|---|---|---|
| z 检验 | 估计值 / SE（σ 已知或大样本） | 标准正态 | 大样本比例检验、Wald 检验 | `2*pnorm(-abs(z))` |
| t 检验 | 估计值 / SE（σ 用样本估计） | t 分布（df） | t 检验、回归 / 混合模型中单个系数或 LS mean 差的检验 | `2*pt(-abs(t), df)` |
| ANOVA / ANCOVA 的 F 检验 | 组间 / 组内变异 | F 分布（df₁, df₂） | ANOVA、模型中的多自由度固定效应检验 | `pf(F, df1, df2, lower.tail=FALSE)` |
| 卡方检验 | Σ(观察 − 期望)² / 期望 | χ² 分布（df） | 列联表检验、log-rank、似然比检验 | `pchisq(x, df, lower.tail=FALSE)` |

- 严格地说，t 检验是把结果"标准化"成 **t 分布**，而不是标准正态。
- **F 和 χ² 检验只看右尾**，因为统计量只会是正数。
- 各分布的来历与构造关系见 [CON-distribution-family](CON-distribution-family.md)；用零分布算 P 值的完整流程见 [CON-p-value](CON-p-value.md#计算流程)。

> 补充（Claude）：表中 `2*pt(-abs(t), df)` 的写法默认零分布对称，所以双侧 P 值 = 单侧尾巴 × 2。F 和 χ² 是非对称分布，它们的"双侧"在常规用法里就是右尾，不需要乘 2。待 Li 核实。

## TLF 中的对应

做 TLF 时天天在用这个逻辑：

- 连续变量的 summary 表 → t 检验或 ANCOVA
- AE / 应答率表 → χ² 或 Fisher
- KM 图下面 → log-rank P 值（log-rank 与 Cox 的分工见 [CON-logrank-vs-cox](../methods/tte/CON-logrank-vs-cox.md)）

## 相关卡片

- [CON-test-selection](CON-test-selection.md)：选哪种检验、临床示例与代码
- [CON-p-value](CON-p-value.md)：检验统计量是计算 P 值的要素之一
- [MTH-t-test](../methods/continuous/MTH-t-test.md)
- [CON-logrank-vs-cox](../methods/tte/CON-logrank-vs-cox.md)
- [CON-null-hypothesis](CON-null-hypothesis.md)
- [CON-distribution-family](CON-distribution-family.md)：Z、t、χ²、F 分布之间的构造关系

## 出处

- Claude 对话（inbox: Test_statistic.md；AI 生成，原始出处待补）
- Claude 对话（inbox: calculate_pvalue.md；AI 生成，原始出处待补；统计量与零分布总表，原在 CON-p-value）
