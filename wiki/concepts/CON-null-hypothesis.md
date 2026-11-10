---
id: CON-null-hypothesis
title: "零假设的定义（Null Hypothesis, H₀）"
categories: [inference, hypothesis-testing, null-hypothesis, superiority, non-inferiority, design]
related: [CON-p-value, CON-t-test-pvalue, CON-hazard-ratio, CON-estimand, GOT-ni-hypothesis-direction, CON-logrank-vs-cox, CON-test-statistic, CON-type-I-II-error, GOT-ttest-student-vs-welch, CON-confidence-interval]
sources: ["Claude 对话（inbox: p_value_h0.md）", "Claude 对话（inbox: ni_h0_direction.md）"]
status: draft
updated: 2026-11-10
---

> 出处待补：本卡内容来自 Claude 对话（inbox: p_value_h0.md、ni_h0_direction.md），属 AI 生成内容，未引用原始文献。

## 一句话定义

H₀ 通常就是**"你想推翻的那个说法"**。定义 H₀ 就是用一句精确的话说清楚：**"在哪些人里、比较哪个指标、用什么参数衡量，结论是没有差别"**。

## 为什么优效性试验的 H₀ 是"没有差别"

"没差别"是一个**具体的数值**（差值 = 0），有了它才能算出零分布，进而算出 P 值（见 [CON-p-value](CON-p-value.md)）。"有差别"可以是差 1、差 5、差 10……范围太宽，没法直接拿来计算。

## 写出 H₀ 的四个要素

例：双盲降压试验，200 名高血压患者随机分到新药组或安慰剂组。

| 要素 | 问题 | 本例 |
|---|---|---|
| ① 终点（Endpoint） | 比较什么指标？ | 第 12 周收缩压较基线的变化值 |
| ② 人群（Population） | 在哪些人里比较？ | 所有随机化的患者（ITT / FAS） |
| ③ 参数（Parameter） | 用什么量衡量差别？ | 两组**总体**均值之差 μ_新药 − μ_安慰剂 |
| ④ 方向（Direction） | 单侧还是双侧？ | 双侧，α = 0.05 |

$$
H_0: \mu_{\text{新药}} - \mu_{\text{安慰剂}} = 0 \qquad H_1: \mu_{\text{新药}} - \mu_{\text{安慰剂}} \neq 0
$$

通俗地说：在所有这类患者中，吃新药和吃安慰剂，12 周后血压平均变化是一样的。

> 补充（Claude）：这四个要素和 [estimand](CON-estimand.md) 的属性（population、variable、population-level summary）高度对应；estimand 还多了 treatment 定义和 intercurrent event 处理两项。H₀ 可以看作在给定 estimand 上"无效应"的数学表述。待 Li 核实。

## 不同终点的 H₀

| 终点类型 | 例子 | 参数 | H₀ |
|---|---|---|---|
| 连续变量 | 血压变化值 | 均值差 | μ_T − μ_P = 0 |
| 二分类 | 血压是否达标 | 达标率之差（或 OR） | p_T − p_P = 0（或 OR = 1） |
| 生存时间 | 发生心血管事件的时间 | 风险比 HR | HR = 1（见 [CON-hazard-ratio](CON-hazard-ratio.md)） |

注意：比值类参数（OR、HR）的"无差别"是 **= 1**，不是 = 0。

## 容易搞混的地方

**1. H₀ 讲的是"总体"，不是"样本"。** 这次试验的 200 人，两组均值差几 mmHg 是必然的，那是样本层面的事。H₀ 说的是"如果给**所有**这类患者用药"，真实差值等于 0。P 值回答的是：在总体真实差值为 0 的前提下，样本里出现这么大差异的可能性有多大。

**2. 双盲本身不是 H₀，而是让 H₀ 的检验"站得住"。**

- **随机化**保证两组开始时可比，组间差异只可能来自"药"或"运气"。
- **双盲**防止患者和医生的心理预期影响用药行为和结果评估，避免人为制造差异。

一旦 P 值很小、可以排除"运气"，剩下的解释就只有"药有效"。

**3. 非劣效试验的 H₀ 是反过来的。** 对照是已上市药物时，目标往往是证明"新药不比老药差太多"。设非劣效界值 Δ（如 3 mmHg）。本例终点是收缩压**变化值**（负数，越小越好）：

$$
H_0: \mu_{\text{新药}} - \mu_{\text{老药}} \ge \Delta \quad \text{（新药降压少了 Δ 或更多，即劣效）}
$$

$$
H_1: \mu_{\text{新药}} - \mu_{\text{老药}} < \Delta \quad \text{（非劣效）}
$$

推翻 H₀，才能得出"新药不劣于老药"。规律不变：**H₀ 永远是你想推翻的那个说法**——即"新药比老药差，且差距达到或超过 Δ"。

> 更正记录：原始材料（p_value_h0.md）写作 H₀: μ新 − μ老 ≤ −Δ，那是"越大越好"终点的写法，与本例终点方向不符；后续 Claude 对话（ni_h0_direction.md）已确认并更正。不同终点方向的通用写法见 [GOT-ni-hypothesis-direction](../gotchas/GOT-ni-hypothesis-direction.md)。

**4. H₀ 必须事先写好。** H₀、终点、分析人群、单侧还是双侧、α 值，都要在**揭盲之前**写进 Protocol 和 SAP。揭盲后才改 H₀ 或换终点，P 值就失去意义了。

## 一句话总结

双盲和随机化不出现在 H₀ 里，但它们保证了一旦推翻 H₀，"药有效"是唯一合理的解释。

## 相关卡片

- [CON-type-I-II-error](CON-type-I-II-error.md)：α、β 与 power
- [CON-p-value](CON-p-value.md)：H₀ 是计算 P 值的第一个要素
- [CON-t-test-pvalue](CON-t-test-pvalue.md)
- [CON-hazard-ratio](CON-hazard-ratio.md)
- [CON-estimand](CON-estimand.md)
- [GOT-ni-hypothesis-direction](../gotchas/GOT-ni-hypothesis-direction.md)：非劣效 H₀ 的方向

## 出处

- Claude 对话（inbox: p_value_h0.md；AI 生成，原始出处待补）
- Claude 对话（inbox: ni_h0_direction.md；AI 生成，原始出处待补）
