---
id: CON-ni-sample-size
title: "非劣效设计的样本量：Δ 是到 H₀ 边界的距离（Sample Size for Non-inferiority Trials）"
categories: [sample-size, non-inferiority, ni-margin, hypothesis-direction, one-sided, proc-power]
related: [CON-sample-size-power, WF-sample-size-calc, GOT-ni-hypothesis-direction, CON-null-hypothesis]
sources: ["Claude 对话（inbox: sample_size.md）", "Claude 对话（inbox: sample_size_ni_correction.md）"]
status: draft
updated: 2026-11-17
---

> 出处待补：本卡内容来自 Claude 对话（inbox: sample_size.md、sample_size_ni_correction.md），属 AI 生成内容，未引用原始文献。文中数值已由 Claude 在 R 4.5.2 中复核。
>
> 拆分记录（2026-11-17）：本卡内容原为 [CON-sample-size-power](CON-sample-size-power.md) 的"非劣效设计"一节，按"一个知识点一张卡"拆出，内容未改写。

## Δ 是"真实差异到 H₀ 边界的距离"

通常用单侧 α = 0.025。样本量公式里的 Δ 本质是**真实差异与零假设边界之间的距离**。优效检验的边界是 0，非劣效检验的边界是 −M 或 +M（来源：sample_size_ni_correction.md）：

| 约定（真实差异 δ = 试验药 − 对照） | H₀ 边界 | 公式里的 Δ |
|---|---|---|
| 越高越好，M > 0（最常见） | −M | **δ + M** |
| 越低越好，M > 0 | +M | **M − δ** |
| 把 M 本身记为负数（如 M = −5 表示边界） | M | δ − M |

通用写法：**Δ = |真实差异 − H₀ 边界值|**。先把边界的位置定清楚，再算距离。各方向的 H₀ 写法见 [GOT-ni-hypothesis-direction](GOT-ni-hypothesis-direction.md)。样本量公式本身见 [WF-sample-size-calc](WF-sample-size-calc.md)。

> 更正记录（2026-11-16）：sample_size.md 原文写"把 Δ 换成（真实差异 − 非劣效界值 M）"。这只在把 M 记为负数时成立。Claude 收录时指出符号问题，后续对话（sample_size_ni_correction.md）确认：M 取正、越高越好时应为 δ + M。

## 符号写错的后果

（σ = 10、单侧 α = 0.025、power 90%、δ = 2、M = 5，越高越好）

| 写法 | Δ | 每组人数 |
|---|---|---|
| 正确：δ + M | 7 | 约 43 |
| 错误：δ − M | −3（平方后按 3 计算） | 约 234 |

n ∝ 1/Δ²，符号一错人数差好几倍。**只有 δ = 0 时两种写法平方后相同**，错误不会暴露，所以这类错误容易被忽略。

> 数值复核（Claude，R 4.5.2）：z 公式 Δ = 7 → 42.9，Δ = 3 → 233.5；`power.t.test(..., alternative = "one.sided")` 分别为 43.9 和 234.5。与材料"约 43 / 约 234"一致（按 t 分布取整则为 44 / 235）。

## 软件里怎么避免

把边界和方向直接交给软件。

```sas
proc power;
  twosamplemeans test=diff
    nullmeandiff = -5      /* H0 边界：-M */
    meandiff     = 2       /* 真实差异 δ */
    sides        = U       /* 上侧检验：越高越好 */
    alpha        = 0.025
    stddev       = 10
    power        = 0.90
    npergroup    = .;
run;
```

终点越低越好时，改成 `nullmeandiff = 5` 和 `sides = L`。

> 补充（Claude）：`TWOSAMPLEMEANS` 中零假设均值差的选项，SAS 文档里写作 `NULLDIFF=`。`NULLMEANDIFF=` 是否为可用别名未核实，运行前请对照所用 SAS 版本的 PROC POWER 文档。待 Li 核实。

R 的 `power.t.test` 没有边界参数，要自己算好距离再传入：

```r
power.t.test(delta = 2 + 5, sd = 10, sig.level = 0.025,
             power = 0.9, alternative = "one.sided")
```

## 相关卡片

- [GOT-ni-hypothesis-direction](GOT-ni-hypothesis-direction.md)：非劣效 H₀ 的方向写反
- [CON-null-hypothesis](../inference/CON-null-hypothesis.md)：非劣效 H₀ 的写法
- [WF-sample-size-calc](WF-sample-size-calc.md)：样本量公式与软件
- [CON-sample-size-power](CON-sample-size-power.md)：power 与样本量的基本概念

## 出处

- Claude 对话（inbox: sample_size.md；AI 生成，原始出处待补）
- Claude 对话（inbox: sample_size_ni_correction.md；AI 生成，原始出处待补）
- 建议对照：FDA *Non-Inferiority Clinical Trials to Establish Effectiveness*（2016）；Chow, Shao & Wang《Sample Size Calculations in Clinical Research》
