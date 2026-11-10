---
id: CON-sample-size-power
title: "Power 与样本量计算（Power and Sample Size Calculation）"
categories: [sample-size, power, design, type-ii-error, mcid, dropout, assumed-treatment-difference, target-difference]
related: [CON-type-I-II-error, CON-t-test-pvalue, CON-hazard-ratio, CON-logrank-vs-cox, CON-null-hypothesis, CON-p-value]
sources: ["Claude 对话（inbox: power.md）", "Claude 对话（inbox: power_correction.md）", "Claude 对话（inbox: assumed_treatment_difference.md）"]
status: draft
updated: 2026-11-10
---

> 出处待补：本卡内容来自 Claude 对话（inbox: power.md、power_correction.md、assumed_treatment_difference.md），属 AI 生成内容，未引用原始文献。文中数值已由 Claude 在 R 4.5.2 中复核（见文末）。

## 一句话定义

**Power 计算**就是在试验开始前回答："如果药真的有我预期的那么好，我招这么多人，有多大把握能把它证明出来？"

反过来问更常见："要有 90% 的把握证明出来，我需要招多少人？"这就是**样本量计算**。两者是同一个计算的两个方向。

α、β、power 的定义见 [CON-type-I-II-error](CON-type-I-II-error.md)。

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
- 窄：SE 小，也就是 SD 小或 **n 大**（SE 与 n、SD 的关系见 [CON-t-test-pvalue](CON-t-test-pvalue.md#t-值是信噪比)）。

power 计算的本质：**调整 n，让两条曲线足够分开，使世界 B 有 80%–90% 落在临界值之外。**

## 需要输入什么

| 输入 | 含义 | 从哪来 |
|---|---|---|
| α | 第一类错误率 | 惯例：双侧 0.05 |
| 1 − β | 目标 power | 惯例：80% 或 90% |
| δ | 预期的真实效应 | 既往研究、II 期数据、临床最小有意义差值（MCID） |
| σ | 个体变异 SD | 既往研究 |
| **输出 → n** | 每组样本量 | |

## 手算一个例子（连续终点，两组均值比较）

降压药，预期比安慰剂多降 **δ = 5 mmHg**，**σ = 10**，双侧 α = 0.05，power 90%。

> **n（每组）= 2 × (z₁₋α/₂ + z₁₋β)² × σ² / δ²**

- z₁₋α/₂ = 1.96（双侧 0.05 的临界值）
- z₁₋β = 1.28（90% power 对应的分位数）

n = 2 × (1.96 + 1.28)² × 10² / 5² = 2 × 10.5 × 4 ≈ **84 人/组**

**直观含义**：要求"信号 δ"至少是"噪音 SE"的 (1.96 + 1.28) ≈ 3.24 倍。1.96 用来越过临界值，1.28 保证世界 B 里 90% 的结果都在临界值之外。

R 验证：

```r
power.t.test(delta = 5, sd = 10, sig.level = 0.05, power = 0.9)
# n ≈ 85.03 per group
```

> 补充（Claude）：手算 84 与 R 的 85.03 相差约 1 人，是因为上面的公式用正态分位数（z），`power.t.test()` 用 t 分布，对 SD 需要估计做了小样本修正。实际报告取整为每组 86 人。SAS 对应写法如下，待 Li 核实：
>
> ```sas
> proc power;
>   twosamplemeans test=diff
>     meandiff = 5
>     stddev   = 10
>     alpha    = 0.05
>     sides    = 2
>     power    = 0.9
>     npergroup = .;
> run;
> ```

### 几个关键规律

- **δ 减半 → n 变 4 倍**（δ 在分母且是平方）。预期效应估得太乐观，试验就会严重 underpowered。详见下文"δ 的选择"。
- power 从 80% 提到 90%，n 约增加 1/3。
- 实际还要**按脱落率上调**：预计脱落 10%，84 / 0.9 ≈ 94 人/组。

## δ 的选择：假设的治疗差值（Assumed Treatment Difference）

（来源：assumed_treatment_difference.md）

**δ 是设计试验时假设的药物真实效果**，即药物组比安慰剂组预期多出来的差值。上例 δ = 5 mmHg，意思是"预计这个降压药比安慰剂**多降 5 mmHg**"。

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

**1. Power 是设计阶段的概念，不是对结果的描述。** 试验做完后再算"观察到的 power"（post-hoc power）基本没有意义，它只是 P 值的另一种写法。结果出来后应该看置信区间（"不显著 ≠ 无效"见 [CON-type-I-II-error](CON-type-I-II-error.md#最重要的解读原则不显著--无效)）。

**2. Power 依赖于假设的 δ。** "90% power"的完整说法是"**如果**真实效应是 5 mmHg，有 90% 把握检测出来"。真实效应若只有 3 mmHg，实际 power 会掉到**约 49%（接近一半）**。

为什么恰好约一半（来源：power_correction.md）：每组 85 人时，差值的 SE = 10 × √(2/85) ≈ 1.53，真实效应 3 ≈ 1.96 个 SE。世界 B 的曲线中心正好落在临界值 1.96 上，一半在左、一半在右，所以 power ≈ 50%；t 分布比正态略宽，实际约 0.49。

> **好记的直觉：当真实效应恰好等于"临界值 × SE"时，power 就是 50%，像抛硬币。** 原本按 90% power 设计的试验，真实效应只有预期的 60%（5 → 3），成功概率就跌到一半左右。

> 更正记录：power.md 原文写"实际 power 会掉到约 44%"。Claude 用 R 复核得 ≈ 49%（`power.t.test(n = 86, delta = 3, sd = 10)` 给出 0.498；正态近似 0.494），power_correction.md 确认 44% 为计算错误，已更正。

**3. 不同终点公式不同。**

| 终点 | 关键输入 |
|---|---|
| 连续 | δ 和 σ |
| 二分类 | 两组率（如 30% vs 45%） |
| 生存 | HR；power 取决于**事件数**而非总人数，所以生存试验常常"等到发生 N 个事件"才分析（HR 见 [CON-hazard-ratio](CON-hazard-ratio.md)，log-rank 见 [CON-logrank-vs-cox](CON-logrank-vs-cox.md)） |

> 补充（Claude）：生存终点常用 Schoenfeld 公式估算所需事件数，1:1 随机时 D = 4 (z₁₋α/₂ + z₁₋β)² / (ln HR)²；再结合入组速度、随访时长和预期事件率推出总人数。二分类终点 SAS 用 `PROC POWER` 的 `twosamplefreq`，生存终点用 `twosamplesurvival`。待 Li 核实。

## 记住一句话

**power 计算就是在动手前确认：试验规模足够大，大到药真有效时不至于被噪音淹没。**

## 相关卡片

- [CON-type-I-II-error](CON-type-I-II-error.md)：α、β、power 的定义
- [CON-t-test-pvalue](CON-t-test-pvalue.md)：信号 / SE
- [CON-hazard-ratio](CON-hazard-ratio.md)：生存终点的效应量

## 出处

- Claude 对话（inbox: power.md；AI 生成，原始出处待补）
- Claude 对话（inbox: power_correction.md；AI 生成，原始出处待补）
- Claude 对话（inbox: assumed_treatment_difference.md；AI 生成，原始出处待补）

> 数值复核（Claude，R 4.5.2）：2 × (1.96 + 1.28)² × 100 / 25 = 83.98（用精确分位数 84.06）；`power.t.test(delta = 5, sd = 10, power = 0.9)` n = 85.03；90% / 80% power 所需 n 之比 = 1.34（约增加 1/3）；δ 减半 n 之比 = 4；84 / 0.9 = 93.3 → 94。以上与材料一致。δ = 3 时 power ≈ 0.49，见上文更正记录。δ = 2.5 时 n = 337.2；SE 1.54 与材料一致。
