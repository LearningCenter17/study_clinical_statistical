---
id: GOT-ni-hypothesis-direction
title: "非劣效假设的方向写反（Non-inferiority H₀ Direction）"
categories: [non-inferiority, null-hypothesis, confidence-interval, design, sap, forest-plot]
related: [CON-null-hypothesis, CON-hazard-ratio, CON-p-value, CON-type-I-II-error, CON-confidence-interval]
sources: ["Claude 对话（inbox: ni_h0_direction.md）"]
status: draft
updated: 2026-11-10
---

> 出处待补：本卡内容来自 Claude 对话（inbox: ni_h0_direction.md），属 AI 生成内容，未引用原始文献。需对照 FDA *Non-Inferiority Clinical Trials to Establish Effectiveness* (2016)、ICH E10 等核实。

## 坑是什么

非劣效 H₀ 的 ≤ / ≥ 方向取决于终点**哪个方向代表"更好"**。套错方向，H₀ 就变成了另一回事。

真实案例（本知识库自己踩过）：[CON-null-hypothesis](../concepts/CON-null-hypothesis.md) 的原始材料把终点定义为"收缩压较基线的**变化值**"（降压后为负数，越负越好），却套用了"越大越好"的写法 H₀: μ新 − μ老 ≤ −Δ，方向写反了。

## 正确写法

**H₀ 永远是"新药比老药差，且差距达到或超过 Δ"**，用 ≤ 还是 ≥ 取决于"差"在数轴上的哪一边：

| 终点方向 | 例子 | H₀（劣效） | H₁（非劣效） | CI 判断 |
|---|---|---|---|---|
| 越大越好 | 应答率、血压**下降量**（正数） | μ新 − μ老 ≤ −Δ | μ新 − μ老 > −Δ | 差值 95% CI **下限** > −Δ |
| 越小越好 | 血压**变化值**（负数）、HbA1c、不良事件率 | μ新 − μ老 ≥ Δ | μ新 − μ老 < Δ | 差值 95% CI **上限** < Δ |
| 比值类，事件越少越好 | HR | HR ≥ Δ_HR（如 1.3） | HR < Δ_HR | HR 95% CI **上限** < 1.3 |

### 例子（越小越好，Δ = 3 mmHg）

| 老药平均变化 | 新药平均变化 | 差值（新 − 老） | 结论 |
|---|---|---|---|
| −12 | −10 | +2 < 3 | 落在非劣效区域 |
| −12 | −8 | +4 ≥ 3 | 劣效 |

（数值已由 Claude 复核。）

## 怎么避免

1. **在 SAP 里明确写出终点的方向**：例如"收缩压变化值，负值表示改善"；或直接把终点定义为"下降量"，统一成越大越好。
2. **用置信区间判断，并和 Δ 画在一起**：越小越好看 CI 上限，越大越好看 CI 下限。TLF 里画森林图时，非劣效界值线画在哪一侧也据此确定。

> 补充（Claude）：
>
> - 用双侧 95% CI 的一侧界限和 Δ 比较，等价于单侧 α = 0.025 的检验；SAP 中通常需写明这一对应。
> - 编程核对时，先确认差值的方向是"新 − 老"还是"老 − 新"（SAS 中由 CLASS 变量的参照组 / `ref=` 决定），方向反了，上下限和界值比较也要跟着反。
> - 待 Li 核实。

## 相关卡片

- [CON-type-I-II-error](../concepts/CON-type-I-II-error.md)：不显著 ≠ 无效，证明"差不多"需要非劣效 / 等效设计
- [CON-null-hypothesis](../concepts/CON-null-hypothesis.md)
- [CON-hazard-ratio](../concepts/CON-hazard-ratio.md)
- [CON-p-value](../concepts/CON-p-value.md)

## 出处

- Claude 对话（inbox: ni_h0_direction.md；AI 生成，原始出处待补）
