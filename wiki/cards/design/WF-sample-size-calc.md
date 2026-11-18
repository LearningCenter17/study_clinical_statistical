---
id: WF-sample-size-calc
title: "样本量计算流程与各终点公式（Sample Size Calculation Workflow）"
categories: [sample-size, power, workflow, formula, rounding, dropout, binary-endpoint, survival, schoenfeld, proc-power, gsdesign]
related: [CON-sample-size-power, CON-ni-sample-size, CON-unequal-allocation, CON-type-I-II-error, CON-normal-distribution, MTH-t-test, CON-hazard-ratio, CON-logrank-vs-cox, CON-confidence-interval, CON-ci-width, CON-survival-analysis-overview]
sources: ["Claude 对话（inbox: power.md）", "Claude 对话（inbox: sample_size.md）", "Claude 对话（inbox: sample_size_rounding.md）"]
status: draft
updated: 2026-11-18
---

> 出处待补：本卡内容来自 Claude 对话（inbox: power.md、sample_size.md、sample_size_rounding.md），属 AI 生成内容，未引用原始文献。文中数值已由 Claude 在 R 4.5.2 中复核（见文末）。
>
> 拆分记录（2026-11-17）：本卡内容原在 [CON-sample-size-power](CON-sample-size-power.md) 中，按"一个知识点一张卡"拆出，内容未改写。power 的含义、各项输入从哪来、δ 怎么选，仍在那张卡。

## 步骤

> 补充（Claude）：以下步骤是按本卡各节整理的顺序，不是材料原文。待 Li 核实。
>
> 1. 定输入：α、power、δ、σ 或各组率、分配比例、检验类型、脱落率（见 [CON-sample-size-power](CON-sample-size-power.md#需要输入什么)）
> 2. 按终点类型选公式（见下文"各终点的公式"）；非劣效见 [CON-ni-sample-size](CON-ni-sample-size.md)，不等分配见 [CON-unequal-allocation](CON-unequal-allocation.md)
> 3. 计算，**向上取整**
> 4. 按脱落率上调
> 5. 用软件（R / SAS `PROC POWER` / PASS 等）核对，正式方案以软件结果为准
> 6. 写进方案的 Sample Size Determination 一节，写明算法和依据

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

**直观含义**：要求"信号 δ"至少是"噪音 SE"的 (1.96 + 1.28) ≈ 3.24 倍。1.96 用来越过临界值，1.28 保证世界 B 里 90% 的结果都在临界值之外（"世界 B"见 [CON-sample-size-power](CON-sample-size-power.md#核心画面两个钟形曲线)）。

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

- **δ 减半 → n 变 4 倍**（δ 在分母且是平方）。预期效应估得太乐观，试验就会严重 underpowered。详见 [CON-sample-size-power](CON-sample-size-power.md#δ-的选择假设的治疗差值assumed-treatment-difference)。
- power 从 80% 提到 90%，n 约增加 1/3。
- 实际还要**按脱落率上调**：N最终 = n / (1 − 脱落率)。预计脱落 10%，85 / 0.9 = 94.4 → 95 人/组（power.md 原例按 84 算得 94；按软件的 86 则为 86 / 0.9 = 95.6 → 96）；sample_size.md 的例子是脱落 15%，85 / (1 − 0.15) = 100 人/组。

## 各终点的公式（两组，1:1 分配）

来源：sample_size.md。

**二分类终点（比较率）**：

$$n_{\text{每组}} = \frac{\left[z_{1-\alpha/2}\sqrt{2\bar p(1-\bar p)} + z_{1-\beta}\sqrt{p_1(1-p_1)+p_2(1-p_2)}\right]^2}{(p_1-p_2)^2}, \quad \bar p = (p_1+p_2)/2$$

**生存终点（log-rank 检验）**：先用 **Schoenfeld 公式**算需要的**事件数**：

$$D = \frac{4\,(z_{1-\alpha/2} + z_{1-\beta})^2}{(\ln HR)^2}$$

再根据入组期、随访期和事件发生率，把事件数换算成总人数。D 与 HR 的 CI 精度（SE ≈ 2/√D）同源，见 [CON-ci-width](../inference/CON-ci-width.md#生存终点看事件数)。

> 更正记录（2026-11-16）：Schoenfeld 公式原为 Claude 补充，sample_size.md 给出了相同公式，改为正文。原补充中"二分类 SAS 用 `PROC POWER` 的 `twosamplefreq`，生存用 `twosamplesurvival`"仍为 Claude 补充，待 Li 核实。

> 数值复核（Claude，R 4.5.2）：p₁ = 0.30、p₂ = 0.50、双侧 α = 0.05、power 80% 时，上面二分类公式得 92.998，与 `power.prop.test()` 的 n 完全一致（≈ 93 人/组）。HR = 0.7、双侧 α = 0.05、power 90% 时 Schoenfeld D ≈ 330.4 个事件。

非劣效设计中公式里的差值怎么取见 [CON-ni-sample-size](CON-ni-sample-size.md)；k:1 分配的公式见 [CON-unequal-allocation](CON-unequal-allocation.md)。

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

## 相关卡片

- [CON-sample-size-power](CON-sample-size-power.md)：power 的含义、输入从哪来、δ 的选择、常见误区
- [CON-ni-sample-size](CON-ni-sample-size.md)：非劣效设计
- [CON-unequal-allocation](CON-unequal-allocation.md)：不等分配
- [CON-normal-distribution](../inference/CON-normal-distribution.md)：公式中的 1.96 和 1.28

## 出处

- Claude 对话（inbox: power.md；AI 生成，原始出处待补）
- Claude 对话（inbox: sample_size.md；AI 生成，原始出处待补）
- Claude 对话（inbox: sample_size_rounding.md；AI 生成，原始出处待补）
- 建议对照：Schoenfeld (1981/1983) 事件数公式；Chow, Shao & Wang《Sample Size Calculations in Clinical Research》

> 数值复核（Claude，R 4.5.2）：2 × (1.96 + 1.28)² × 100 / 25 = 83.98（用精确分位数 84.06）；`power.t.test(delta = 5, sd = 10, power = 0.9)` n = 85.03；90% / 80% power 所需 n 之比 = 1.34（约增加 1/3）；84 / 0.9 = 93.3 → 94。以上与材料一致。
