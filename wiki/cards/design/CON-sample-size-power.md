---
id: CON-sample-size-power
title: "Power 与样本量计算（Power and Sample Size Calculation）"
categories: [sample-size, power, design, type-ii-error, mcid, dropout, assumed-treatment-difference, target-difference]
related: [WF-sample-size-calc, CON-ni-sample-size, CON-unequal-allocation, CON-type-I-II-error, MTH-t-test, CON-hazard-ratio, CON-logrank-vs-cox, CON-null-hypothesis, CON-p-value, CON-covariate, CON-dose-escalation-design, CON-normal-distribution, CON-confidence-interval, GOT-ni-hypothesis-direction, CON-response-rate, CON-stratified-randomization, CON-prognostic-factor]
sources: ["Claude 对话（inbox: power.md）", "Claude 对话（inbox: power_correction.md）", "Claude 对话（inbox: assumed_treatment_difference.md）", "Claude 对话（inbox: sample_size.md）"]
status: draft
updated: 2026-11-17
---

> 出处待补：本卡内容来自 Claude 对话（inbox: power.md、power_correction.md、assumed_treatment_difference.md、sample_size.md），属 AI 生成内容，未引用原始文献。文中数值已由 Claude 在 R 4.5.2 中复核（见文末）。
>
> 拆分记录（2026-11-17）：本卡原先还包含具体算法、非劣效和不等分配，已按"一个知识点一张卡"拆出到下面三张卡，内容未改写：
>
> - [WF-sample-size-calc](WF-sample-size-calc.md)：手算例子、84 / 85 / 86 人、各终点公式、R / SAS 实现
> - [CON-ni-sample-size](CON-ni-sample-size.md)：非劣效设计中的 Δ 与符号陷阱
> - [CON-unequal-allocation](CON-unequal-allocation.md)：不等分配（k:1）与 ASAS40 算例

## 一句话定义

**Power 计算**就是在试验开始前回答："如果药真的有我预期的那么好，我招这么多人，有多大把握能把它证明出来？"

反过来问更常见："要有 90% 的把握证明出来，我需要招多少人？"这就是**样本量计算**。两者是同一个计算的两个方向。

α、β、power 的定义见 [CON-type-I-II-error](../inference/CON-type-I-II-error.md)。

样本量由**主要终点的统计假设**决定：先确定各项输入，再按终点类型套用相应公式（来源：sample_size.md）。具体怎么算见 [WF-sample-size-calc](WF-sample-size-calc.md)。

### 术语

| 中文 | 英文 |
|---|---|
| 样本量计算 | sample size calculation / sample size determination |
| 样本量估算的依据 | sample size justification / sample size rationale |
| 把握度 / 检验效能 | power |
| 效应量 | effect size |
| 脱落率 | dropout rate |
| 非劣效界值 | non-inferiority margin |

方案中这一节通常叫 **"Sample Size Determination"** 或 **"Sample Size Justification"**。

## 核心画面：两个钟形曲线

想象检验统计量（比如两组差值）的抽样分布，在两种"世界"里各长什么样：

```
     世界A：药无效(H₀)          世界B：药有效(H₁)，真实差值=δ
          ╭──╮                        ╭──╮
         ╱    ╲                      ╱    ╲
        ╱      ╲                    ╱░░░░░░╲
       ╱        ╲                  ╱░░░░░░░░╲
  ────╱──────────╲──────────┬─────╱░░░░░░░░░░╲────
      0                  临界值        δ
                     (超过它就判显著)
```

- 临界值由 **α** 决定：世界 A 里越过它的面积 = 第一类错误。
- **Power = 世界 B 的曲线落在临界值右边的面积**（阴影部分），即药真有效时得到显著结果的概率。
- 世界 B 落在临界值左边的面积就是 **β**（第二类错误）。

**两条曲线分得越开、各自越窄，power 越大。**

- 分得开：真实效应 δ 大。
- 窄：SE 小，也就是 SD 小或 **n 大**（SE 与 n、SD 的关系见 [MTH-t-test](../methods/continuous/MTH-t-test.md#t-值是信噪比)）。

power 计算的本质：**调整 n，让两条曲线足够分开，使世界 B 有 80%–90% 落在临界值之外。**

## 需要输入什么

| 输入 | 含义 | 从哪来 |
|---|---|---|
| α | 第一类错误率 | 惯例：双侧 0.05，或单侧 0.025 |
| 1 − β | 目标 power | 惯例：80% 或 90% |
| δ | 预期的真实效应 | 既往研究、II 期数据、临床最小有意义差值（MCID） |
| σ / p | 变异度：连续终点用 SD，二分类终点用各组的率 | 既往研究 |
| 分配比例 k | 两组人数比 | 1:1、2:1 等（不等分配见 [CON-unequal-allocation](CON-unequal-allocation.md)） |
| 检验类型 | 优效、非劣效或等效 | 非劣效还需要界值 M（见 [CON-ni-sample-size](CON-ni-sample-size.md)） |
| 脱落率 | 预计丢失的受试者比例 | 常取 10%–20% |
| **输出 → n** | 每组样本量 | |

后三行来源：sample_size.md。**效应量和变异度的来源最关键**，通常来自 II 期数据或文献，SAP 中要写明依据。

## δ 的选择：假设的治疗差值（Assumed Treatment Difference）

（来源：assumed_treatment_difference.md）

**δ 是设计试验时假设的药物真实效果**，即药物组比安慰剂组预期多出来的差值。[WF-sample-size-calc](WF-sample-size-calc.md) 手算例子中 δ = 5 mmHg，意思是"预计这个降压药比安慰剂**多降 5 mmHg**"。

### 为什么 δ 减半，样本量要变 4 倍

信号 δ 要比噪音 SE 大约 3.24 倍，才有 90% 把握检测出来：

| | δ | 需要的 SE ≈ δ / 3.24 | 每组 n |
|---|---|---|---|
| 原来 | 5 mmHg | 1.54 | ≈ 85 |
| δ 减半 | 2.5 mmHg | 0.77（**SE 也要减半**） | ≈ 337 |

SE ∝ 1 / √n，要让 SE 减半，√n 就得翻倍，所以 **n 要变成 4 倍**。

```r
power.t.test(delta = 5,   sd = 10, power = 0.9)$n   # ≈ 85 人/组
power.t.test(delta = 2.5, sd = 10, power = 0.9)$n   # ≈ 337 人/组
```

**直观比喻**：在嘈杂的房间里听人说话，对方声音小了一半，不是靠近一点就够，而是要付出多得多的努力才能听清。效果越小越"安静"，越需要大样本把噪音压下去。

### 实际意义：δ 是设计里争议最大的输入

- **δ 估得太乐观**（比如定成 5，实际只有 2.5）→ 样本量不够，试验大概率失败。
- **δ 定得保守** → 样本量暴增，成本和时间成倍上升。

所以 δ 通常要参考 II 期数据、同类药物结果，以及**临床最小有意义差值（minimal clinically important difference, MCID）**：小于这个差值，即使统计显著，临床上也没意义。

> 补充（Claude）："大概率失败"的量级：按 δ = 5 设计（每组 86 人），真实效应只有 2.5 时 power ≈ 37%（R `power.t.test(n = 86, delta = 2.5, sd = 10)`）；真实效应 3 时约 49%，见下文误区 2。
>
> 补充（Claude）：δ 与 MCID 不一定相等。δ 是"预期的真实效应"（target difference），常常设得比 MCID 大；如果把 δ 设成 MCID，试验能可靠检测到临床上有意义的最小效应，但样本量更大。如何确定 δ 有专门的方法学指引（如英国 DELTA² 指南），待 Li 核实。

## 常见误区

**1. Power 是设计阶段的概念，不是对结果的描述。** 试验做完后再算"观察到的 power"（post-hoc power）基本没有意义，它只是 P 值的另一种写法。结果出来后应该看置信区间（"不显著 ≠ 无效"见 [CON-type-I-II-error](../inference/CON-type-I-II-error.md#最重要的解读原则不显著--无效)）。

**2. Power 依赖于假设的 δ。** "90% power"的完整说法是"**如果**真实效应是 5 mmHg，有 90% 把握检测出来"。真实效应若只有 3 mmHg，实际 power 会掉到**约 49%（接近一半）**。

为什么恰好约一半（来源：power_correction.md）：每组 85 人时，差值的 SE = 10 × √(2/85) ≈ 1.53，真实效应 3 ≈ 1.96 个 SE。世界 B 的曲线中心正好落在临界值 1.96 上，一半在左、一半在右，所以 power ≈ 50%；t 分布比正态略宽，实际约 0.49。

> **好记的直觉：当真实效应恰好等于"临界值 × SE"时，power 就是 50%，像抛硬币。** 原本按 90% power 设计的试验，真实效应只有预期的 60%（5 → 3），成功概率就跌到一半左右。

> 更正记录：power.md 原文写"实际 power 会掉到约 44%"。Claude 用 R 复核得 ≈ 49%（`power.t.test(n = 86, delta = 3, sd = 10)` 给出 0.498；正态近似 0.494），power_correction.md 确认 44% 为计算错误，已更正。

**3. 不同终点公式不同。**

| 终点 | 关键输入 |
|---|---|
| 连续 | δ 和 σ |
| 二分类 | 两组率（如 30% vs 45%） |
| 生存 | HR；power 取决于**事件数**而非总人数，所以生存试验常常"等到发生 N 个事件"才分析（HR 见 [CON-hazard-ratio](../methods/tte/CON-hazard-ratio.md)，log-rank 见 [CON-logrank-vs-cox](../methods/tte/CON-logrank-vs-cox.md)） |

各终点的具体公式见 [WF-sample-size-calc](WF-sample-size-calc.md#各终点的公式两组11-分配)。

## 其他会改变样本量的设计因素

来源：sample_size.md。

- **多重比较**（多个主要终点或多个剂量组）需要校正 α，如 Bonferroni 或分层检验程序（hierarchical testing），会增加样本量。多重性见第 7 章（待建）。
- **期中分析**（成组序贯设计）会消耗 α，样本量需相应放大，可用 gsDesign 或 rpact 计算。alpha spending 见第 8 章（待建）。
- **分层随机基本不进入这个计算**，除非 SAP 明确使用了基于协变量调整的方差。

> 注：这一条在原对话中回答的是"是否按分层因素增加样本量"。完整解释（为什么不需要、过度分层的真正问题、什么时候确实要加人）见 [CON-stratified-randomization](CON-stratified-randomization.md)。
>
> 补充（Claude）：协变量调整（ANCOVA）能降低残差方差、提高 power（见 [CON-covariate](../methods/continuous/CON-covariate.md)），但常规做法是不把这部分收益计入样本量，算是保守估计。待 Li 核实。

## 记住一句话

**power 计算就是在动手前确认：试验规模足够大，大到药真有效时不至于被噪音淹没。**

## 相关卡片

- [WF-sample-size-calc](WF-sample-size-calc.md)：具体怎么算（手算、公式、R / SAS）
- [CON-ni-sample-size](CON-ni-sample-size.md)：非劣效设计的样本量
- [CON-unequal-allocation](CON-unequal-allocation.md)：不等分配（k:1）
- [CON-type-I-II-error](../inference/CON-type-I-II-error.md)：α、β、power 的定义
- [MTH-t-test](../methods/continuous/MTH-t-test.md)：信号 / SE
- [CON-hazard-ratio](../methods/tte/CON-hazard-ratio.md)：生存终点的效应量

## 出处

- Claude 对话（inbox: power.md；AI 生成，原始出处待补）
- Claude 对话（inbox: power_correction.md；AI 生成，原始出处待补）
- Claude 对话（inbox: assumed_treatment_difference.md；AI 生成，原始出处待补）
- Claude 对话（inbox: sample_size.md；AI 生成，原始出处待补）
- 建议对照：Chow, Shao & Wang《Sample Size Calculations in Clinical Research》；ICH E9 第 3.5 节（样本量）

> 数值复核（Claude，R 4.5.2）：δ 减半 n 之比 = 4；δ = 2.5 时 n = 337.2；SE 1.54 与材料一致。δ = 3 时 power ≈ 0.49，见上文更正记录。
