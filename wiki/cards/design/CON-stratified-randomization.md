---
id: CON-stratified-randomization
title: "分层随机化与过度分层（Stratified Randomization and Over-stratification）"
categories: [design, randomization, stratification, stratified-randomization, over-stratification, block-randomization, minimization, sample-size, irt, subgroup]
related: [CON-sample-size-power, CON-covariate, MTH-CMH, CON-logrank-vs-cox, CON-sensitivity-analysis, CON-prognostic-factor]
sources: ["Claude 对话（inbox: stratification_sample.md）", "Claude 对话（inbox: stratification_example_check.md）", "Claude 对话（inbox: stratification_imbalance_correction.md）"]
status: draft
updated: 2026-11-17
---

> 出处待补：本卡内容来自 Claude 对话（inbox: stratification_sample.md、stratification_example_check.md、stratification_imbalance_correction.md），属 AI 生成内容，未引用原始文献。建议对照 ICH E9 第 2.3 节（随机化）、EMA *Guideline on adjustment for baseline covariates in clinical trials*（2015）。

## 一句话定义

**分层随机化**：按预后因素（如地区、疾病严重程度；什么是强预后因素见 [CON-prognostic-factor](CON-prognostic-factor.md)）把受试者分成若干层，在每层内部用**区组随机**分配治疗，保证各层内两组大致均衡。

核心结论：**分层本身不增加样本量**。分层太多时，正确的做法是**减少分层**，而不是多招人。

## 为什么分层不需要增加人数

样本量是为**整体比较**算的，不需要在每一层内部都有足够的把握度。

分层分析（CMH、分层 log-rank、分层 Cox、把分层因素作为协变量）回答的仍然是**一个总体的治疗效应**：先在各层内比较药物组和安慰剂组，再把各层的信息合并成一个估计值。所以：

- 样本量（材料中的例子是 192 人）对应的把握度，是为合并后的**这一个比较**准备的。
- 每层只需要有一定数量的两组受试者参与比较，不需要每层单独达到显著。
- 只要每一层内部两组人数大致均衡，各层的信息就能有效合并。

**192 人从哪来**（来源：stratification_example_check.md）：Δ = 5、σ = 10、双侧 α = 0.05、power 90%，按 **2:1 分配**计算，安慰剂组 64 人、药物组 128 人，共 192 人。

计算过程（不等分配公式、与 1:1 的比较、R 代码）见 [CON-sample-size-power](CON-sample-size-power.md) 的"不等分配（k:1）"一节。

样本量计算本身见 [CON-sample-size-power](CON-sample-size-power.md)（"分层随机基本不进入这个计算"一条即回答的是本卡的问题）。各分层方法：CMH 见 [MTH-CMH](../methods/binary/MTH-CMH.md)，分层 log-rank / Cox 见 [CON-logrank-vs-cox](../methods/tte/CON-logrank-vs-cox.md)，协变量调整见 [CON-covariate](../methods/continuous/CON-covariate.md)。

## 分层主要在什么时候有用

（来源：stratification_imbalance_correction.md）

### 样本量适中或较大时，大的不均衡本来就很少见

随机化后两组某类患者比例的差异，大小主要取决于样本量。假设总体中某类患者（如 IV 期）占 50%：

| 每组人数 | 两组比例差异的标准差 | 差异 ≥ 30 个百分点的概率 |
|---|---|---|
| 20 | 约 16 个百分点 | 约 6% |
| 100 | 约 7 个百分点 | 约 0.002%，几乎不可能 |

正态近似：差异的标准差 = √(2 × 0.5 × 0.5 / n)。每组 100 人左右时，简单随机化几乎不可能出现 70% 对 40% 这样的情况，实际中更常见的是几个百分点的差异。

> 数值复核（Claude，R 4.5.2）：正态近似双侧概率 n = 20 为 5.8%，n = 100 为 0.0022%，与材料一致（材料按"任一方向"计）。精确二项计算 n = 20 为 8.1%（离散性使"恰好差 6 人 = 30%"被计入），n = 30 为 2.7%，n = 100 为 0.0027%。

### 分层的价值在哪

- 样本量适中或较大时，简单随机化通常已能保证大致均衡，分层在**均衡方面**的好处有限。
- **小样本**：每组二三十人时，较大的不均衡确实可能出现。
- **亚组**：总样本量大，亚组人数也可能很少（如"用过生物制剂且 X 线严重"的患者），分层能保证这些亚组内部均衡。
- **让分析与设计一致**（analyze as randomized）：随机化按哪些因素分层，分析就按这些因素分层或调整，结果的统计性质（如 I 类错误）才有保证。
- **提高精确度**：通过分析时的分层或协变量调整（见 [CON-covariate](../methods/continuous/CON-covariate.md)）。

> 补充（Claude）：材料说 "analyze as randomized" 是"前面提到"的，但本知识库此前没有收录。它的常见表述是：分析模型应包含随机化时使用的分层因素；只分层随机、分析不调整，会使方差估计偏保守（I 类错误偏低、power 损失）。待 Li 核实（可对照 EMA 协变量调整指南、ICH E9）。

## 分层太多的真正问题

问题不在于把握度不够，而在于以下三点。

### 1. 随机化的均衡性反而变差

每层内使用区组随机。层数太多时，很多层入组人数不到一个完整区组，就会出现大量**不完整的区组**。

例：192 人，2:1 分配，区组大小 6，分 24 层，平均每层只有 8 人。很多层停在区组中途，各层的不均衡加起来，整体均衡可能还不如不分层。这就是**过度分层（over-stratification）**。

具体算一下（来源：stratification_example_check.md，确认了 Claude 首次收录时的补充）：

- 2:1、区组大小 6，一个完整区组是 **4 个药物组 + 2 个安慰剂组**。
- 每层 8 人 = **1 个完整区组（6 人）+ 剩下 2 人**。
- 剩下的 2 人落在第二个区组的开头，而这个区组没有填满。他们可能是"药物、药物"、"安慰剂、安慰剂"或一个药物一个安慰剂，取决于区组内的随机顺序。

所以每层的最终分配不一定是 2:1。例如最后 2 人都是安慰剂时，该层是 4 药物 : 4 安慰剂，变成 **1:1**。24 层每一层都有这种偏差，加起来可能让整体比例偏离 2:1。

### 2. 分层分析中出现稀疏单元格

- 某层只有一组的受试者，或者某层没有事件发生，这一层对 CMH 或分层 log-rank 检验**贡献不了信息**，相当于浪费了这部分受试者。
- 分层 Cox 或 logistic 模型可能出现估计不稳定、**不收敛**。
- 这些情况会让实际 power 低于设计值。

### 3. 误分层的机会增加

分层因素越多，研究中心在 IRT 中**录错分层**的机会越多，后续需要做的敏感性分析也越多（敏感性分析见 [CON-sensitivity-analysis](../missing-data/CON-sensitivity-analysis.md)）。

> 补充（Claude）：误分层时，分析常要决定用 IRT 记录的分层（随机化时实际用的）还是 eCRF 上的真实值，SAP 中通常预先规定主分析用哪个、另一个做敏感性分析。待 Li 核实。

## 实际中怎么处理

| 做法 | 说明 |
|---|---|
| 限制分层因素的数量 | 一般只选 2 到 3 个最重要的预后因素，总层数控制在较少的范围内 |
| 合并类别 | 如把多个中心合并成地区，把连续变量按一个切点分成两类 |
| 使用最小化法（minimization） | 动态分配，可以同时平衡很多因素，不受层数限制 |
| 在 SAP 中预先规定合并规则 | 如"某层人数少于 X 时，与相邻层合并后再分析" |
| 分析时把分层因素作为协变量 | 用 ANCOVA 或 logistic 模型调整，而不是把每个组合都当作独立的层 |

经验规则：**总层数最好远小于 N / 区组大小**，保证大部分层都能填满几个完整区组。

用上例检验（来源：stratification_example_check.md）：

- N / 区组大小 = 192 / 6 = **32**，即整个试验最多只能装下 32 个完整区组。
- 分 24 层，层数已经**接近 32**，平均每层只有约 1.3 个区组，几乎每一层都会留下一个不完整区组，所以属于过度分层。
- 如果只分 **4 层**，每层约 48 人，即 8 个完整区组，不完整区组只在每层末尾出现一次，影响就很小。

> 补充（Claude）：minimization 不是完全随机的分配，监管上通常要求加入随机成分（如以一定概率分配到使不均衡最小的组），并在分析中调整用于 minimization 的因素。待 Li 核实。

## 什么时候确实需要增加人数

如果方案要求**在某个层或亚组内单独证明疗效**，就要为这个亚组单独计算样本量，总人数会增加。常见例子：

- 监管机构要求某个地区（如日本或中国人群）的结果与总体**一致**，需要该地区有足够的人数。
- 某个分层因素对应的亚组被设为**关键次要终点**，需要控制 α 并保证把握度（多重性见第 7 章，待建）。

这时增加人数的原因是**亚组分析的要求**，不是分层随机化本身。

## 相关卡片

- [CON-sample-size-power](CON-sample-size-power.md)：样本量计算；分层基本不进入计算
- [CON-covariate](../methods/continuous/CON-covariate.md)：分层因素作为协变量
- [MTH-CMH](../methods/binary/MTH-CMH.md)：分层分析二分类 / 有序终点
- [CON-logrank-vs-cox](../methods/tte/CON-logrank-vs-cox.md)：分层 log-rank 与分层 Cox

## 出处

- Claude 对话（inbox: stratification_sample.md；AI 生成，原始出处待补）
- Claude 对话（inbox: stratification_example_check.md；AI 生成，原始出处待补）
- Claude 对话（inbox: stratification_imbalance_correction.md；AI 生成，原始出处待补）
