---
id: CON-sample-size-power
title: "Power 与样本量计算（Power and Sample Size Calculation）"
categories: [sample-size, power, design, type-ii-error, mcid, dropout, assumed-treatment-difference, target-difference, schoenfeld, non-inferiority, binary-endpoint, survival, gsdesign, unequal-allocation, continuity-correction, asas40]
related: [CON-type-I-II-error, MTH-t-test, CON-hazard-ratio, CON-logrank-vs-cox, CON-null-hypothesis, CON-p-value, CON-covariate, CON-dose-escalation-design, CON-normal-distribution, CON-confidence-interval, GOT-ni-hypothesis-direction, CON-response-rate, CON-stratified-randomization, CON-prognostic-factor]
sources: ["Claude 对话（inbox: power.md）", "Claude 对话（inbox: power_correction.md）", "Claude 对话（inbox: assumed_treatment_difference.md）", "Claude 对话（inbox: sample_size.md）", "Claude 对话（inbox: sample_size_ni_correction.md）", "Claude 对话（inbox: sample_size_rounding.md）", "Claude 对话（inbox: calculcate_sample_size.md）"]
status: draft
updated: 2026-11-17
---

> 出处待补：本卡内容来自 Claude 对话（inbox: power.md、power_correction.md、assumed_treatment_difference.md、sample_size.md、sample_size_ni_correction.md、sample_size_rounding.md、calculcate_sample_size.md），属 AI 生成内容，未引用原始文献。文中数值已由 Claude 在 R 4.5.2 中复核（见文末）。

## 一句话定义

**Power 计算**就是在试验开始前回答："如果药真的有我预期的那么好，我招这么多人，有多大把握能把它证明出来？"

反过来问更常见："要有 90% 的把握证明出来，我需要招多少人？"这就是**样本量计算**。两者是同一个计算的两个方向。

α、β、power 的定义见 [CON-type-I-II-error](../inference/CON-type-I-II-error.md)。

样本量由**主要终点的统计假设**决定：先确定各项输入，再按终点类型套用相应公式（来源：sample_size.md）。

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
| 分配比例 k | 两组人数比 | 1:1、2:1 等 |
| 检验类型 | 优效、非劣效或等效 | 非劣效还需要界值 M |
| 脱落率 | 预计丢失的受试者比例 | 常取 10%–20% |
| **输出 → n** | 每组样本量 | |

后三行来源：sample_size.md。**效应量和变异度的来源最关键**，通常来自 II 期数据或文献，SAP 中要写明依据。

## 手算一个例子（连续终点，两组均值比较）

降压药，预期比安慰剂多降 **δ = 5 mmHg**，**σ = 10**，双侧 α = 0.05，power 90%。

> **n（每组）= 2 × (z₁₋α/₂ + z₁₋β)² × σ² / δ²**

- z₁₋α/₂ = 1.96（双侧 0.05 的临界值）
- z₁₋β = 1.28（90% power 对应的分位数）

n = 2 × (1.96 + 1.28)² × 10² / 5² = 2 × 10.5 × 4 ≈ 84

### 84、85、86 人：各自从哪来

用正态近似公式和**精确分位数**（z₀.₉₇₅ = 1.959964，z₀.₉ = 1.281552）计算，n = 84.06，向上取整为**每组 85 人**。教科书中常见的"84 人"来自 z₀.₉ 取 1.28 的近似，会略低估人数。用 t 分布计算（R `power.t.test`、SAS `PROC POWER`）为 85.03，取整为**每组 86 人**；正式方案以软件结果为准（来源：sample_size_rounding.md）。

| 算法 | 原始结果 | 向上取整 |
|---|---|---|
| z 公式，z₀.₉ 取 1.28 | 83.98 | 84 |
| z 公式，精确分位数 | 84.06 | **85** |
| t 分布（软件） | 85.03 | **86** |

原则：**样本量一律向上取整**，保证实际 power 不低于目标值；**z 值用精确分位数**，1.28 把 z₀.₉ 取小了，人数偏少。

> 数值复核（Claude，R 4.5.2）：实际 power（t 分布）：每组 84 人为 0.8965，85 人为 0.8999（仍略低于 90%），86 人为 0.9032。所以按 t 分布要到 86 人才真正达到 90%。正态近似下 84 人为 0.8998、85 人为 0.9031。
>
> 更正记录（2026-11-16）：原先这里标着"存在分歧（轻微，取整方式）"警示：power.md 写"≈ 84 人/组"，sample_size.md 写"每组 85 人"。后续对话（sample_size_rounding.md）解释了两者的来源，并给出上面这段写法，已去掉警示标记。

**直观含义**：要求"信号 δ"至少是"噪音 SE"的 (1.96 + 1.28) ≈ 3.24 倍。1.96 用来越过临界值，1.28 保证世界 B 里 90% 的结果都在临界值之外。

R 验证：

```r
power.t.test(delta = 5, sd = 10, sig.level = 0.05, power = 0.9)
# n ≈ 85.03 per group
```

> 补充（Claude）：z 公式与 R 的 85.03 不同，是因为 `power.t.test()` 用 t 分布，对 SD 需要估计做了小样本修正（取整规则见上）。SAS 对应写法如下，待 Li 核实：
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
- 实际还要**按脱落率上调**：N最终 = n / (1 − 脱落率)。预计脱落 10%，85 / 0.9 = 94.4 → 95 人/组（power.md 原例按 84 算得 94；按软件的 86 则为 86 / 0.9 = 95.6 → 96）；sample_size.md 的例子是脱落 15%，85 / (1 − 0.15) = 100 人/组。

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

## 各终点的公式（两组，1:1 分配）

来源：sample_size.md。

**二分类终点（比较率）**：

$$n_{\text{每组}} = \frac{\left[z_{1-\alpha/2}\sqrt{2\bar p(1-\bar p)} + z_{1-\beta}\sqrt{p_1(1-p_1)+p_2(1-p_2)}\right]^2}{(p_1-p_2)^2}, \quad \bar p = (p_1+p_2)/2$$

**生存终点（log-rank 检验）**：先用 **Schoenfeld 公式**算需要的**事件数**：

$$D = \frac{4\,(z_{1-\alpha/2} + z_{1-\beta})^2}{(\ln HR)^2}$$

再根据入组期、随访期和事件发生率，把事件数换算成总人数。D 与 HR 的 CI 精度（SE ≈ 2/√D）同源，见 [CON-confidence-interval](../inference/CON-confidence-interval.md#生存终点看事件数)。

> 更正记录（2026-11-16）：Schoenfeld 公式原为 Claude 补充，sample_size.md 给出了相同公式，改为正文。原补充中"二分类 SAS 用 `PROC POWER` 的 `twosamplefreq`，生存用 `twosamplesurvival`"仍为 Claude 补充，待 Li 核实。

### 非劣效设计：Δ 是"真实差异到 H₀ 边界的距离"

通常用单侧 α = 0.025。样本量公式里的 Δ 本质是**真实差异与零假设边界之间的距离**。优效检验的边界是 0，非劣效检验的边界是 −M 或 +M（来源：sample_size_ni_correction.md）：

| 约定（真实差异 δ = 试验药 − 对照） | H₀ 边界 | 公式里的 Δ |
|---|---|---|
| 越高越好，M > 0（最常见） | −M | **δ + M** |
| 越低越好，M > 0 | +M | **M − δ** |
| 把 M 本身记为负数（如 M = −5 表示边界） | M | δ − M |

通用写法：**Δ = |真实差异 − H₀ 边界值|**。先把边界的位置定清楚，再算距离。各方向的 H₀ 写法见 [GOT-ni-hypothesis-direction](GOT-ni-hypothesis-direction.md)。

> 更正记录（2026-11-16）：sample_size.md 原文写"把 Δ 换成（真实差异 − 非劣效界值 M）"。这只在把 M 记为负数时成立。Claude 收录时指出符号问题，后续对话（sample_size_ni_correction.md）确认：M 取正、越高越好时应为 δ + M。

**符号写错的后果**（σ = 10、单侧 α = 0.025、power 90%、δ = 2、M = 5，越高越好）：

| 写法 | Δ | 每组人数 |
|---|---|---|
| 正确：δ + M | 7 | 约 43 |
| 错误：δ − M | −3（平方后按 3 计算） | 约 234 |

n ∝ 1/Δ²，符号一错人数差好几倍。**只有 δ = 0 时两种写法平方后相同**，错误不会暴露，所以这类错误容易被忽略。

> 数值复核（Claude，R 4.5.2）：z 公式 Δ = 7 → 42.9，Δ = 3 → 233.5；`power.t.test(..., alternative = "one.sided")` 分别为 43.9 和 234.5。与材料"约 43 / 约 234"一致（按 t 分布取整则为 44 / 235）。

**软件里怎么避免**：把边界和方向直接交给软件。

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

> 数值复核（Claude，R 4.5.2）：p₁ = 0.30、p₂ = 0.50、双侧 α = 0.05、power 80% 时，上面二分类公式得 92.998，与 `power.prop.test()` 的 n 完全一致（≈ 93 人/组）。HR = 0.7、双侧 α = 0.05、power 90% 时 Schoenfeld D ≈ 330.4 个事件。

## 不等分配（k:1）

> 补充（Claude）：本节公式由 Claude 补充。材料（stratification_example_check.md）只给出了 2:1 的结果"安慰剂 64、药物 128、共 192"。待 Li 对照教材（如 Chow, Shao & Wang）核实。

药物组 : 安慰剂组 = k : 1 时，**连续终点**较小组（安慰剂组）的人数：

$$n_{\text{小组}} = \left(1 + \frac{1}{k}\right)\frac{(z_{1-\alpha/2} + z_{1-\beta})^2\,\sigma^2}{\Delta^2}, \qquad n_{\text{大组}} = k \cdot n_{\text{小组}}$$

k = 1 时括号内为 2，就回到上文的 1:1 公式。

**例**（Δ = 5、σ = 10、双侧 α = 0.05、power 90%、2:1）：n小组 = 1.5 × 10.507 × 100 / 25 = 63.04 → **64**，药物组 128，**共 192 人**。这就是 [CON-stratified-randomization](CON-stratified-randomization.md) 中过度分层例子的 192。

**不等分配的代价**：总人数是 1:1 的 (1 + k)² / (4k) 倍。

| 分配 | 总人数倍数 | 本例（未取整的总人数） |
|---|---|---|
| 1:1 | 1 | 168.1 |
| 2:1 | 1.125 | 189.1 |
| 3:1 | 1.333 | 224.2 |

所以 2:1 只多花约 12.5% 的人，常用来让更多受试者接受试验药、积累更多安全性数据；超过 3:1 后效率下降明显。

**生存终点**：Schoenfeld 公式的系数 4 换成 (1 + k)² / k（k = 1 时为 4）：

$$D = \frac{(1+k)^2}{k} \cdot \frac{(z_{1-\alpha/2} + z_{1-\beta})^2}{(\ln HR)^2}$$

这与 HR 的 CI 精度 SE(log HR) ≈ (1 + k)/√(k·D) 同源，见 [CON-confidence-interval](../inference/CON-confidence-interval.md#生存终点看事件数)。

**软件**：R 的 `power.t.test()`、`power.prop.test()` 只支持等分配，不等分配可以直接按公式算（二分类的函数见下文 ASAS40 算例）；SAS `PROC POWER` 用 `groupweights = (1 2)` 配合 `ntotal = .`。

```r
k  <- 2
z2 <- (qnorm(0.975) + qnorm(0.90))^2
n_small <- ceiling((1 + 1/k) * z2 * 10^2 / 5^2)   # 64
c(placebo = n_small, drug = k * n_small, total = (1 + k) * n_small)
```

> 数值复核（Claude，R 4.5.2）：上面代码输出 64 / 128 / 192。按 t 分布，64 / 128 人的实际 power 为 0.901，达到 90%。SAS `groupweights` 写法未在 SAS 中运行过，待 Li 核实。

### 二分类终点的不等分配：ASAS40 算例

来源：calculcate_sample_size.md。终点 ASAS40（应答定义见 [CON-response-rate](../methods/binary/CON-response-rate.md#应答标准因疾病而异)），预期应答率安慰剂 p₁ = 20%、药物 p₂ = 45%，双侧 α = 0.05，power 80%，placebo : drug = 1 : 2（k = 2），脱落 15%。

$$n_{\text{pbo}} = \frac{\left[z_{1-\alpha/2}\sqrt{\bar p(1-\bar p)\left(1+\frac{1}{k}\right)} + z_{1-\beta}\sqrt{p_1(1-p_1) + \frac{p_2(1-p_2)}{k}}\right]^2}{(p_2 - p_1)^2}, \qquad \bar p = \frac{p_1 + k\,p_2}{1+k}$$

k = 1 时就是上文 1:1 的二分类公式。逐步计算：

1. 加权平均率：p̄ = (0.20 + 2 × 0.45) / 3 = 0.3667
2. 分子第一部分：1.96 × √(0.3667 × 0.6333 × 1.5) = 1.96 × 0.5902 = 1.1568
3. 分子第二部分：0.8416 × √(0.20 × 0.80 + 0.45 × 0.55 / 2) = 0.8416 × 0.5327 = 0.4483
4. n_pbo = (1.1568 + 0.4483)² / 0.25² = 2.5763 / 0.0625 = 41.22 → **42**。逐个核算 power：41 人为 79.8%，42 人为 80.8%，所以 42 是满足 80% 的最小人数。
5. 考虑脱落：安慰剂 42 / 0.85 = 49.4 → 50，药物组按比例 50 × 2 = 100。

| | 安慰剂组 | 药物组 | 总人数 |
|---|---|---|---|
| 可评价人数 | 42 | 84 | 126 |
| 考虑 15% 脱落后的入组人数 | 50 | 100 | **150** |

**连续性校正（Fleiss 校正）**：结果更保守，安慰剂约 48、药物 96、共 144 人；考虑脱落后约 57 + 114 = 171 人。**用哪种算法要在方案中写明**，以免核对时出现不同的数字。

```sas
proc power;
  twosamplefreq test=pchi
    groupproportions = (0.20 0.45)   /* 安慰剂组, 药物组 */
    groupweights     = (1 2)
    alpha            = 0.05
    sides            = 2
    power            = 0.80
    ntotal           = .;
run;
```

材料说结果应在 126 人左右，SAS 会自动把总人数取整为符合 1:2 比例的数。

```r
n_2prop <- function(p1, p2, k = 2, alpha = 0.05, power = 0.80) {
  za <- qnorm(1 - alpha/2); zb <- qnorm(power)
  pb <- (p1 + k*p2) / (1 + k)
  n1 <- (za*sqrt(pb*(1-pb)*(1 + 1/k)) +
         zb*sqrt(p1*(1-p1) + p2*(1-p2)/k))^2 / (p2 - p1)^2
  n1 <- ceiling(n1)
  c(placebo = n1, drug = k*n1, total = n1*(1 + k))
}

n <- n_2prop(0.20, 0.45)                  # 42, 84, 126
pbo <- unname(ceiling(n["placebo"] / 0.85))
c(placebo = pbo, drug = 2*pbo, total = 3*pbo)   # 50, 100, 150
```

**方案中可能的写法**：

> 假设安慰剂组和药物组的 ASAS40 应答率分别为 20% 和 45%，采用双侧 α = 0.05 的卡方检验，按 1:2 随机分配，共需 126 例可评价受试者（安慰剂组 42 例，药物组 84 例），可提供 80% 的把握度。考虑 15% 的脱落率，计划入组 150 例（安慰剂组 50 例，药物组 100 例）。

> 数值复核（Claude，R 4.5.2）：n_pbo 原始值 41.22；正态近似 power 41 人 0.798、42 人 0.808；Fleiss 校正 n' = n/4 × [1 + √(1 + 2(k + 1) / (k · n · |p₂ − p₁|))]² = 47.03 → 48，脱落后 48 / 0.85 → 57。以上均与材料一致。材料 R 代码原写 `ceiling(n["placebo"] / 0.85)`，会把名字带进结果（输出显示为 `placebo.placebo`），这里加了 `unname()`，数值不变。SAS 代码未运行，待 Li 核实（与上文 `groupweights` 一并）。
>
> 补充（Claude）：脱落调整的做法是先把**较小组**除以 (1 − 脱落率) 并取整，再按比例乘出大组，这样入组人数严格保持 1:2。若两组分别除以 0.85 再取整（49.4 → 50、98.8 → 99），比例就不再严格是 1:2。待 Li 核实。

## 实现

### R

来源：sample_size.md。

```r
# 连续变量
power.t.test(delta = 5, sd = 10, sig.level = 0.05, power = 0.90)

# 二分类变量
power.prop.test(p1 = 0.30, p2 = 0.50, sig.level = 0.05, power = 0.80)

# 生存分析（需要安装 gsDesign）
library(gsDesign)
nSurv(lambdaC = log(2)/12,   # 对照组中位生存期 12 个月
      hr = 0.7, eta = 0.05,  # eta 为脱落风险率
      T = 36, minfup = 12,   # 研究总时长和最短随访时间
      alpha = 0.025, beta = 0.1)
```

`power.t.test` 用 t 分布，结果比 z 公式略大，约每组 86 人（取整后）。

> 补充（Claude）：`nSurv` 这段未复核，本机没有安装 gsDesign。`lambdaC = log(2)/12` 是把中位生存期 12 个月换算成指数分布的风险率；`eta` 也是按月的风险率，不是百分比。参数含义以 gsDesign 文档为准，待 Li 核实。

### 软件

商业软件常用 PASS、nQuery、East；SAS 用 `PROC POWER`（连续终点示例见上文）。

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

- [CON-type-I-II-error](../inference/CON-type-I-II-error.md)：α、β、power 的定义
- [MTH-t-test](../methods/continuous/MTH-t-test.md)：信号 / SE
- [CON-hazard-ratio](../methods/tte/CON-hazard-ratio.md)：生存终点的效应量

## 出处

- Claude 对话（inbox: power.md；AI 生成，原始出处待补）
- Claude 对话（inbox: power_correction.md；AI 生成，原始出处待补）
- Claude 对话（inbox: assumed_treatment_difference.md；AI 生成，原始出处待补）
- Claude 对话（inbox: sample_size.md；AI 生成，原始出处待补）
- Claude 对话（inbox: sample_size_ni_correction.md；AI 生成，原始出处待补）
- Claude 对话（inbox: sample_size_rounding.md；AI 生成，原始出处待补）
- Claude 对话（inbox: calculcate_sample_size.md；AI 生成，原始出处待补）
- 建议对照：Schoenfeld (1981/1983) 事件数公式；Chow, Shao & Wang《Sample Size Calculations in Clinical Research》；ICH E9 第 3.5 节（样本量）

> 数值复核（Claude，R 4.5.2）：2 × (1.96 + 1.28)² × 100 / 25 = 83.98（用精确分位数 84.06）；`power.t.test(delta = 5, sd = 10, power = 0.9)` n = 85.03；90% / 80% power 所需 n 之比 = 1.34（约增加 1/3）；δ 减半 n 之比 = 4；84 / 0.9 = 93.3 → 94。以上与材料一致。δ = 3 时 power ≈ 0.49，见上文更正记录。δ = 2.5 时 n = 337.2；SE 1.54 与材料一致。
