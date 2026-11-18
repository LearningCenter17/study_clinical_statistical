---
id: MTH-CMH
title: "CMH 检验：分层比较应答率、三个统计量与 SCORES= 选项（Cochran-Mantel-Haenszel）"
categories: [categorical, cmh, stratification, binary-endpoint, odds-ratio, mantel-haenszel, breslow-day, simpsons-paradox, ordinal, van-elteren, wilcoxon, kruskal-wallis, sas, proc-freq, scores]
related: [CON-ordinal-data, CON-parametric-vs-nonparametric, CON-test-selection, CON-confirmatory-methods-overview, CON-covariate, MTH-proportional-odds-model, CON-response-rate, CON-stratified-randomization, CON-test-statistic, MTH-chi-square, CON-continuity-correction, GOT-continuity-correction-r-vs-sas, CON-odds-ratio]
sources: ["Claude 对话（inbox: cmh_statistics.md）", "Claude 对话（inbox: CMH1.md）"]
status: draft
updated: 2026-11-18
---

> 出处待补：本卡内容来自 Claude 对话（inbox: cmh_statistics.md、CMH1.md），属 AI 生成内容，未引用原始文献（如 SAS PROC FREQ 文档、Stokes, Davis & Koch《Categorical Data Analysis Using SAS》）。示例数值已由 Claude 在 R 4.5.2 中复核。
>
> 本卡分两部分：**二分类终点**（分层比较应答率、MH 合并 OR、Breslow-Day）和**有序终点**（三个统计量怎么选、`SCORES=` 怎么设）。Mantel-Haenszel 率差与 RR 尚待补充。

## 二分类终点：分层比较应答率

（来源：CMH1.md）**CMH 检验**（Cochran-Mantel-Haenszel）可以理解成**"分组比较，再合并结论"**的卡方检验（卡方统计量的原理见 [CON-test-statistic](../../inference/CON-test-statistic.md)）。

### 它要解决什么问题

比如比较药物组和安慰剂组的应答率（应答 / 不应答）。最简单的做法是把所有人放进一张 2×2 表，做个卡方检验。

但如果病人本身差别很大，比如有的人之前用过生物制剂（更难治），有的人没用过（更好治），全部混在一起比，结果就可能被这种差异干扰。极端情况下甚至会出现**辛普森悖论**（Simpson's paradox）：每个亚组里药物都更好，合起来看却显得更差（见下文算例）。

### CMH 的做法

1. **先分层**：按"是否用过生物制剂"（也可以再加 X 光分级）把病人分成几组。
2. **每层内各比各的**：每一层单独做一张 2×2 表，药物组和安慰剂组只在同一层里比，相当于"苹果比苹果"。
3. **加权合并**：把各层的比较结果按样本量等信息加权汇总，得到一个总的检验结果和一个**共同的效应量**（通常是 CMH 合并的 OR 或风险差）。

一句话概括：**它回答的是"排除分层因素的影响以后，药物到底有没有效"。**

### 为什么临床试验里这么常用

- **和随机化设计对应**：如果随机化是按某些因素分层做的，分析时一般也按这些因素分层。ICH E9 的原则就是"按设计来分析"（analyze as randomized，见 [CON-stratified-randomization](../../design/CON-stratified-randomization.md#分层主要在什么时候有用)）。例如按 X 光分级和既往生物制剂分层随机的关节炎试验，二分类终点（比如 ACR20 应答率）的主分析通常就是用这两个因素做分层的 CMH 检验。
- **结果稳健**：不需要像 logistic 回归那样设定模型形式。
- **监管机构熟悉**：FDA / EMA 的审评人员都很常见这种方法。

### 一个前提：各层效应方向一致

CMH 默认**各层的效应方向大致一致**，也就是药物在每一层里都差不多有效。如果某一层药物有效、另一层反而有害，合并出来的数字就没什么意义了。所以一般会配一个 **Breslow-Day 检验**，看各层的 OR 是否同质。

### 程序里怎么做

- **SAS**：`PROC FREQ` 加 `TABLES strat1*strat2*trt*resp / CMH;`，最后两个变量是行和列，前面的都是分层变量。
- **R**：`mantelhaen.test(table(trt, resp, strata))`。如果要按"X 光 × 生物制剂"交叉分层，先把两个变量合成一个分层变量。

如果打算去掉分层，CMH 就会退化成普通的卡方检验或 Fisher 检验。不过如果随机化本身是分层做的，分析时把分层也去掉，通常需要在 SAP 里给出理由。

> 补充（Claude）：R 的 `mantelhaen.test()` 默认 `correct = TRUE`（连续性校正），SAS `PROC FREQ` 的 CMH 统计量不做连续性校正（各方法的 R / SAS 默认对照见 [GOT-continuity-correction-r-vs-sas](GOT-continuity-correction-r-vs-sas.md)；后续材料 Continuity correction.md 给出相同说法）。和 SAS 比对时，R 端要写 `correct = FALSE`（下文算例就是这样写的）。2×2×K 表时 SAS 会同时输出 MH 合并 OR / RR 和 Breslow-Day 检验。待 Li 核实。

### 算例：辛普森悖论

虚构的关节炎试验，终点是 **ACR20 应答率**，分层因素是**既往是否用过生物制剂**。为了看得更清楚，这里故意把两组人群设得很不均衡。

**第 1 层：没用过生物制剂（病情相对好治）**

| | 应答 | 不应答 | 合计 | 应答率 |
|---|---|---|---|---|
| 药物组 | 48 | 12 | 60 | **80%** |
| 安慰剂 | 168 | 72 | 240 | **70%** |

**第 2 层：用过生物制剂（病情难治）**

| | 应答 | 不应答 | 合计 | 应答率 |
|---|---|---|---|---|
| 药物组 | 96 | 144 | 240 | **40%** |
| 安慰剂 | 18 | 42 | 60 | **30%** |

在每一层里，药物组都比安慰剂组**高 10 个百分点**。

**如果不分层，直接合在一起：**

| | 应答 | 不应答 | 合计 | 应答率 |
|---|---|---|---|---|
| 药物组 | 144 | 156 | 300 | **48%** |
| 安慰剂 | 186 | 114 | 300 | **62%** |

结果变成药物组比安慰剂组**低 14 个百分点**。普通卡方检验 χ² ≈ 11.9，p < 0.001，看起来"药物显著更差"。

这就是辛普森悖论。原因是药物组里大部分人（240/300）是难治的老病人，安慰剂组里大部分人是好治的新病人。合在一起比，比的其实是"病人难不难治"，而不是"药好不好"。

**CMH 怎么算：**

**第一步：每层算"观察值 − 期望值"。** 这里只看药物组的应答人数。期望值的意思是：假设药物无效，这一层应答的人会按人数比例分到两组。

- 第 1 层：一共 216 人应答，药物组占 60/300 的人，期望 = 216 × 60/300 = 43.2，实际 48，**多出 4.8**
- 第 2 层：一共 114 人应答，药物组占 240/300，期望 = 114 × 240/300 = 91.2，实际 96，**多出 4.8**

**第二步：各层相加，再除以方差。**

- 偏差总和 = 4.8 + 4.8 = 9.6
- 各层方差之和 ≈ 9.71 + 11.35 = 21.06
- CMH 统计量 = 9.6² / 21.06 ≈ **4.38**，p ≈ **0.036**

**第三步：合并的效应量（MH 合并 OR）。**（OR 本身的定义和解读见 [CON-odds-ratio](CON-odds-ratio.md)。）

- 第 1 层 OR = (48×72)/(12×168) ≈ 1.71
- 第 2 层 OR = (96×42)/(144×18) ≈ 1.56
- MH 合并 OR ≈ **1.63**，也就是药物组应答的优势约为安慰剂组的 1.6 倍

两层的 OR 很接近（1.71 和 1.56），说明满足"各层效应一致"的前提，合并是合理的。

| 分析方法 | 结论 |
|---|---|
| 不分层卡方 | OR ≈ 0.57，药物**显著更差**（p < 0.001） |
| 分层 CMH | OR ≈ 1.63，药物**显著更好**（p ≈ 0.036） |

```r
tab <- array(c(48, 168, 12, 72,     # 第1层：药物应答, 安慰剂应答, 药物不应答, 安慰剂不应答
               96,  18, 144, 42),   # 第2层
             dim = c(2, 2, 2),
             dimnames = list(trt  = c("Drug", "Placebo"),
                             resp = c("Yes", "No"),
                             bio  = c("Naive", "Experienced")))

mantelhaen.test(tab, correct = FALSE)   # CMH ≈ 4.38, p ≈ 0.036, OR ≈ 1.63
```

真实的随机化试验里，组间人群不会这么不均衡，这正是分层随机化要防止的情况（见 [CON-stratified-randomization](../../design/CON-stratified-randomization.md)）。实际中 CMH 的作用通常没这么戏剧化，主要是去掉分层因素带来的噪音，让检验**更精确、效能更高**。

> 数值复核（Claude，R 4.5.2）：`mantelhaen.test(tab, correct = FALSE)` 给出 CMH = 4.377、p = 0.0364、MH 合并 OR = 1.625（95% CI 1.03–2.57）；两层期望值 43.2 / 91.2、方差 9.709 / 11.347、OR 1.714 / 1.556；不分层 χ² = 11.88（p = 0.0006）、OR = 0.566。以上均与材料一致。另按公式手算 Breslow-Day 统计量 = 0.043（p = 0.84），各层 OR 同质，与材料"两层 OR 很接近"的判断一致。

## 有序终点：CMH 三个统计量怎么选

SAS `PROC FREQ` 的 `CMH` 选项会同时输出三个统计量，按行、列变量是否有序来选：

| 统计量 | 行（治疗组） | 列（应答） | 自由度 |
|---|---|---|---|
| Nonzero Correlation | 有序 | 有序 | 1 |
| **Row Mean Scores Differ** | **无序** | **有序** | 行数 − 1 |
| General Association | 无序 | 无序 | (行 − 1)(列 − 1) |

**治疗组 vs 有序应答**（如 CGI-I、mRS，见 [CON-ordinal-data](../ordinal/CON-ordinal-data.md)）对应的是 **Row Mean Scores Differ**。

> 补充（Claude）：两组比较时行数 − 1 = 1，此时 Row Mean Scores Differ 与 Nonzero Correlation 数值相同。待 Li 核实。

## `SCORES=` 选项决定检验的具体形式

| 选项 | 得分 | 等价的检验 |
|---|---|---|
| `SCORES=TABLE`（默认） | 列变量的原始数值 | 要求编码的**间距有意义** |
| `SCORES=RANK` | 秩得分 | 不分层时等价于 **Kruskal-Wallis**；只有两组时等价于 **Wilcoxon rank-sum** |
| `SCORES=MODRIDIT` | 每层内把秩按 (n_h + 1) 标准化 | 分层时 Row Mean Scores 统计量就是 **van Elteren 检验**（分层 Wilcoxon） |
| `SCORES=RIDIT` | 和 modridit 类似，但标准化方式略有不同 | **不等同于** van Elteren |

Kruskal-Wallis、Wilcoxon 本身见 [CON-test-selection](../../inference/CON-test-selection.md)；van Elteren 也出现在 [CON-parametric-vs-nonparametric](../../inference/CON-parametric-vs-nonparametric.md) 的"不容易调整协变量"补充里。

> 补充（Claude）：
> - 等价关系可以从公式看出来。不分层时，Row Mean Scores 统计量为 Q = (n − 1) · Σᵢ nᵢ(s̄ᵢ − s̄)² / Σ(s − s̄)²，其中 s 是得分。把 s 换成秩，就是带结校正的 Kruskal-Wallis H。
> - 分层时各层分别计算得分。各层对统计量的贡献大致按 1/(n_h + 1)（modridit）或 1/n_h（ridit）加权，这就是两者"略有不同"的地方。
> - 以上为 Claude 推导和记忆，未对照 SAS 文档，待 Li 核实。

## 写代码时要注意

```sas
proc freq data=adeff;
  tables strata * trt01pn * aval / cmh scores=modridit;
run;
```

- **分层变量放最前面，治疗组必须在行的位置，应答在列的位置。** 顺序放反的话，Row Mean Scores 检验的就是另一个方向的假设。
- **应答变量的排序要正确。** 字符型变量默认可能按字母排序，所以最好用数值编码（如 `AVAL`），或者设置 `ORDER=`。`AVAL` / `AVALC` 的约定见 [CON-ordinal-data](../ordinal/CON-ordinal-data.md#adam-中的存储)。

> 更正记录（2026-11-12）：Claude 最初给的代码写的是 `avaln`。按 ADaM 更正（`AVALN` 不是 BDS 标准变量），这里应该用存有序编码的 `AVAL`。上面的代码已改。

## 相关卡片

- [CON-stratified-randomization](../../design/CON-stratified-randomization.md)：分层随机与"按设计来分析"
- [CON-response-rate](CON-response-rate.md)：应答率与 ACR20 等应答标准
- [CON-ordinal-data](../ordinal/CON-ordinal-data.md)：有序应答的分析方法
- [CON-parametric-vs-nonparametric](../../inference/CON-parametric-vs-nonparametric.md)：van Elteren（分层 Wilcoxon）
- [CON-test-selection](../../inference/CON-test-selection.md)：Wilcoxon、Kruskal-Wallis
- [CON-covariate](../continuous/CON-covariate.md)：分层因素是常见的需要调整的变量
- [CON-confirmatory-methods-overview](../CON-confirmatory-methods-overview.md)：CMH 在确证性试验中的位置

## 出处

- Claude 对话（inbox: cmh_statistics.md；AI 生成，原始出处待补）
- Claude 对话（inbox: CMH1.md；AI 生成，原始出处待补；二分类部分与辛普森悖论算例）
