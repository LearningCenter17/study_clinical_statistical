---
id: CON-reliability-engineering
title: "可靠性工程：生存分析在制造业的应用（B10 寿命、加速寿命试验、保修分析、Weibull 与浴盆曲线）（Reliability Engineering）"
categories: [non-clinical, reliability-engineering, survival, censoring, weibull, aft, accelerated-life-testing, warranty-analysis, predictive-maintenance, bathtub-curve, b10-life, mttf, mtbf]
related: [CON-survival-analysis-non-clinical, CON-survival-analysis-overview, MTH-kaplan-meier, CON-logrank-vs-cox, CON-hazard-ratio]
sources: ["Claude 对话（inbox: reliability_engineering.md）"]
status: draft
updated: 2026-11-19
---

> 出处待补：本卡内容来自 Claude 对话（inbox: reliability_engineering.md），属 AI 生成内容，未引用原始文献（如 Meeker & Escobar《Statistical Methods for Reliability Data》）。生存分析在各领域的概览见 [CON-survival-analysis-non-clinical](CON-survival-analysis-non-clinical.md)；方法本身（删失、S(t)、KM、Cox）见 [CON-survival-analysis-overview](../methods/tte/CON-survival-analysis-overview.md)。

## 一句话定义

生存分析用在制造业，就是**可靠性工程（Reliability Engineering）**。

## 为什么制造业特别需要

产品可靠性数据有一个突出特点：**绝大多数产品在观察期内都没坏**。一批零件测试 1000 小时，可能只坏了几个，其余全是删失。如果只看坏掉的那几个，会严重低估寿命；如果简单算"故障数 / 总数"，又没有利用时间信息。生存分析正好处理这种情况。

## 主要应用场景

**1. 寿命测试与设计验证**

在产品上市前测试零件、材料的寿命，估计常用的可靠性指标：

- **B10 寿命**：10% 的产品失效时的时间，汽车、轴承行业很常用
- **MTTF / MTBF**：平均失效时间 / 平均故障间隔时间
- **某时间点的可靠度**，比如"10 年后仍正常工作的比例"，就是生存函数 S(t)

> 补充（Claude）：换成临床试验的说法，B10 寿命就是 S(t) 降到 0.9 时对应的 t，和"中位生存时间"（S(t) 降到 0.5）是同一类分位数指标；MTTF 对应平均生存时间。有删失时平均值不能直接算，要靠参数模型外推，或者改用限制平均生存时间 RMST（见 [CON-survival-analysis-overview](../methods/tte/CON-survival-analysis-overview.md#4-ph-假设不成立时怎么办)）。待 Li 核实。

**2. 加速寿命试验（ALT）**

真实寿命可能长达十几年，没法等。做法是在高温、高电压、高振动等更严苛的条件下测试，用 AFT 模型把结果换算回正常使用条件下的寿命。AFT 模型在这里是核心工具。

> 补充（Claude）：AFT（加速失效时间模型）的简要说明见 [CON-survival-analysis-non-clinical](CON-survival-analysis-non-clinical.md) 末尾的补充。

**3. 保修数据分析（Warranty Analysis）**

- 起点：车辆售出日期
- 事件：某个零部件的保修索赔
- 删失：保修期内没有索赔，或者还没到保修期截止

用来预测未来的保修成本、尽早发现某批次或某供应商的零件有质量问题，决定是否召回。汽车行业这里有个特殊之处：时间尺度不只是日历时间，还有**里程**，两者都可以作为"时间"轴来分析。

**4. 维护策略与预测性维护**

分析设备多久需要维护，比较"定期更换"和"坏了再修"哪种更划算。现在工厂装了大量传感器，会把温度、振动等实时数据作为随时间变化的协变量放进 Cox 模型，预测设备的剩余寿命。

**5. 供应商与工艺比较**

比较不同供应商、不同生产线、不同工艺的零件寿命。这和临床试验里比较两个治疗组是同一回事：两条 KM 曲线加 log-rank 检验，或者 Cox 模型给出 HR（见 [MTH-kaplan-meier](../methods/tte/MTH-kaplan-meier.md)、[CON-logrank-vs-cox](../methods/tte/CON-logrank-vs-cox.md)、[CON-hazard-ratio](../methods/tte/CON-hazard-ratio.md)）。

## 和医疗领域的主要区别

| | 临床试验 | 制造业 |
|---|---|---|
| 常用模型 | KM + Cox（半参数） | **Weibull 等参数模型** |
| 原因 | 关注组间比较，不想假设分布 | 需要外推到很长的时间，必须有分布形式 |
| 常用软件 | R、SAS | Minitab、JMP、ReliaSoft (Weibull++)，也用 R |

制造业偏好 Weibull 分布，是因为它的形状参数能直接说明失效模式：小于 1 表示早期失效（制造缺陷），等于 1 表示随机失效，大于 1 表示磨损老化。这三种情况连起来就是工程上有名的**浴盆曲线（bathtub curve）**。

> 补充（Claude）：形状参数说的是风险函数 h(t)（见 [CON-survival-analysis-overview](../methods/tte/CON-survival-analysis-overview.md#2-核心概念)）随时间怎么变：小于 1 时 h(t) 随时间下降，等于 1 时 h(t) 恒定（即指数分布），大于 1 时 h(t) 随时间上升。浴盆曲线是 h(t) 先降、再平、后升的形状。临床试验里参数模型并非不用：需要外推时（如卫生经济学评估）也常用 Weibull，见 CON-survival-analysis-overview 第 4 节。待 Li 核实。

## 相关卡片

- [CON-survival-analysis-non-clinical](CON-survival-analysis-non-clinical.md)：生存分析在各领域的应用概览
- [CON-survival-analysis-overview](../methods/tte/CON-survival-analysis-overview.md)：删失、S(t) / h(t)、参数模型
- [MTH-kaplan-meier](../methods/tte/MTH-kaplan-meier.md)：KM 估计
- [CON-logrank-vs-cox](../methods/tte/CON-logrank-vs-cox.md)：组间比较的两种方法
- [CON-hazard-ratio](../methods/tte/CON-hazard-ratio.md)：Cox 模型的效应量

## 出处

- Claude 对话（inbox: reliability_engineering.md；AI 生成，原始出处待补）
