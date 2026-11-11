---
id: CON-dose-escalation-design
title: "一期剂量递增设计（Dose-Escalation Designs: 3+3、CRM / BLRM、BOIN）"
categories: [phase-1, dose-escalation, mtd, dlt, 3+3, crm, blrm, ewoc, boin, model-assisted, project-optimus, bayesian]
related: [CON-distribution-family, GOT-skewed-small-sample, CON-sample-size-power]
sources: ["Claude 对话（inbox: phaseI_stat.md）"]
status: draft
updated: 2026-11-11
---

> 出处待补：本卡内容来自 Claude 对话（inbox: phaseI_stat.md），属 AI 生成内容，未引用原始文献。材料开头提到"上一条主要讲了 ANOVA 在一期里的位置"，那一条未收录进 inbox。

## 核心问题

一期剂量递增要回答：**在可接受的毒性范围内，最高能给到多大剂量？** 通常先定一个**目标毒性率**（如 DLT 发生率 25%–33%），再找毒性率接近这个比例的剂量，即 **MTD（maximum tolerated dose，最大耐受剂量）**。

这里的统计方法主要用来**做决策**（下一组用多大剂量、什么时候停），不是做假设检验。方法分三类：基于规则、基于模型、模型辅助。

## 一、基于规则的设计（rule-based）：3+3

- 每个剂量先入组 3 人
- 0/3 出现 DLT → 升到下一剂量
- 1/3 出现 DLT → 同剂量再加 3 人
  - 6 人中仍只有 1/6 → 升剂量
  - ≥ 2/6 → 停止，前一个剂量就是 MTD
- ≥ 2/3 出现 DLT → 停止

- **优点**：简单，不需要统计师实时参与。
- **缺点**：只看当前剂量的数据，信息利用率低；很多病人被分到低于有效剂量的组；找到的 MTD 不够准，实际毒性率常低于目标。

> 补充（Claude）：
> - 常见表述中，MTD 定义为"**6 人中 DLT ≤ 1 的最高剂量**"。所以 ≥ 2/3 停止时，前一剂量如果只有 3 人，通常要**补足到 6 人**确认，才能宣布为 MTD。材料没写这一步。
> - 3+3 隐含的目标毒性率大约在 1/6 到 1/3 之间，不是事先设定的参数。这也是它"实际毒性率常低于目标"的原因。
>
> 以上待 Li 核实。

## 二、基于模型的设计（model-based）

### CRM（continual reassessment method，持续再评估法）

假设剂量与 DLT 概率之间有一条**剂量-毒性曲线**。每入组一批病人，就用**所有剂量组的累积数据**更新这条曲线（贝叶斯方法），再选估计毒性率最接近目标的剂量给下一组。

- **优点**：利用全部数据，找 MTD 更准，更多病人分在接近最优的剂量上。
- **缺点**：要预设模型和先验，每次决策都要统计师跑模型，临床团队可能觉得像黑箱。

### BLRM / EWOC

- **BLRM（Bayesian logistic regression model，贝叶斯逻辑回归模型）**：用逻辑回归描述剂量-毒性关系。肿瘤一期很常用，尤其在大药企（如诺华）。
- **EWOC（escalation with overdose control，过量控制）**：选剂量时加一条约束："**所选剂量超过 MTD 的概率不能高于某个阈值（如 25%）**"，防止升得太快。常与 BLRM 一起用。

> 补充（Claude）：原始 CRM（O'Quigley 等 1990）允许跳级升剂量。实际使用中一般会加安全限制，如不跳级、首组从最低剂量开始。待 Li 核实。

## 三、模型辅助设计（model-assisted）

介于前两类之间：用统计模型算出决策规则，但**事先就能生成一张决策表**，执行时像 3+3 一样查表。

### BOIN（Bayesian optimal interval design，贝叶斯最优区间设计）

最受欢迎的一种。根据目标毒性率事先算出两个边界：

- 当前剂量观察到的 DLT 率 ≤ 下边界 λₑ → **升**剂量
- ≥ 上边界 λ_d → **降**剂量
- 介于中间 → **维持**

例如目标毒性率 30% 时，边界约为 **0.236 和 0.359**。

> 补充（Claude，已用 R 按公式复核）：BOIN 默认取 φ₁ = 0.6φ、φ₂ = 1.4φ（φ 为目标毒性率）。边界公式为
> λₑ = log[(1−φ₁)/(1−φ)] / log[φ(1−φ₁) / (φ₁(1−φ))]，
> λ_d = log[(1−φ)/(1−φ₂)] / log[φ₂(1−φ) / (φ(1−φ₂))]。
> φ = 0.30 时 λₑ = 0.2365、λ_d = 0.3585，与材料一致；φ = 0.25 时为 0.197 / 0.298；φ = 0.33 时为 0.260 / 0.395。公式和默认值出自 Liu & Yuan（2015）。文献未核对原文，待 Li 核实。本机未安装 `BOIN` 包，`get.boundary()` 的输出未实际运行。

- **优点**：执行和 3+3 一样简单，性能接近 CRM，FDA 已认可其为 fit-for-purpose 设计。
- 同类设计还有 **mTPI、mTPI-2、i3+3、Keyboard**。

> 补充（Claude）：FDA 对 BOIN 的 fit-for-purpose 认定一般说是在 2021 年，属于 Drug Development Tools 下的 Fit-for-Purpose Initiative。年份凭记忆，待 Li 核实。

## 三类设计对比

| | 3+3 | CRM / BLRM | BOIN 等 |
|---|---|---|---|
| 类型 | 规则 | 模型 | 模型辅助 |
| 用哪些数据决策 | 仅当前剂量 | 全部剂量 | 主要是当前剂量 |
| 执行难度 | 很简单 | 需实时建模 | 查表即可 |
| 找 MTD 的准确性 | 较差 | 好 | 好 |
| 趋势 | 逐渐被替代 | 大药企常用 | 越来越主流 |

**打个比方**：找"最辣能吃多辣"。

- **3+3**：每次三个人试一个辣度，没人受不了就加辣，两个人受不了就退回上一级。
- **CRM**：根据所有人吃所有辣度的反应，画一条"辣度-受不了比例"曲线，每次按曲线推荐最接近目标的辣度。
- **BOIN**：事先定好规则，"受不了的比例低于 24% 就加辣，高于 36% 就减辣"，照表执行。

## 剂量递增之外的一期统计分析

- **安全性**：AE、DLT、实验室检查、生命体征，按剂量组做描述性统计。
- **PK**：非房室分析（NCA）算 Cmax、AUC、t½，按剂量组汇总**几何均值和 CV%**。PK 参数通常右偏，几何均值的道理同 [GOT-skewed-small-sample](../gotchas/GOT-skewed-small-sample.md) 的 log 转换。
- **剂量比例性**：power model。
- **PK/PD、暴露-反应**：探索剂量或浓度与生物标志物、疗效信号的关系。
- **QT**：浓度-QTc 模型。

> 补充（Claude）：power model 一般写成 log(PK 参数) = α + β·log(剂量)。β 的 90% CI 落在预设区间内（如由 0.8–1.25 推导出的区间）即可判断剂量比例。待 Li 核实。

## 近年的新趋势

- **FDA Project Optimus**（主要针对肿瘤药）：不再只追求 MTD，而是找兼顾疗效和耐受性的"**最优剂量**"。因此现在一期常在 MTD 以下做**剂量扩展（dose expansion）**，随机比较 2 个及以上剂量。
- 相应出现了同时考虑毒性和疗效的设计，如 **BOIN12、U-BOIN、EffTox**。

> 补充（Claude）：Project Optimus 于 2021 年启动。相关指南为 FDA《Optimizing the Dosage of Human Prescription Drugs and Biologics for the Treatment of Oncologic Diseases》（2023 草案，2024 定稿）。名称和年份凭记忆给出，待 Li 核实后可建 REF 卡片。

## R 工具

| 方法 | R 包 |
|---|---|
| BOIN | `BOIN` |
| CRM | `dfcrm`、`bcrm` |
| BLRM / EWOC | `OncoBayes2`、`ewoc` |
| 设计模拟比较 | `escalation`、`UnifiedDoseFinding` |
| NCA | `PKNCA`、`NonCompart` |

BOIN 生成决策表只需一行：

```r
library(BOIN)
get.boundary(target = 0.3, ncohort = 10, cohortsize = 3)
```

> 包名来自材料，Claude 未逐一在 CRAN 上核对，待 Li 核实。

## 对统计编程的意义

设计选择和参数设定通常由统计师在方案和 SAP 阶段完成。编程时更多是按方案生成以下表格：

- **剂量递增过程汇总表**：每个 cohort 的剂量、人数、DLT 数
- 安全性表
- PK 表

## 相关卡片

- [CON-distribution-family](CON-distribution-family.md)：DLT 是二分类结局，每个剂量的 DLT 数服从二项分布
- [GOT-skewed-small-sample](../gotchas/GOT-skewed-small-sample.md)：右偏数据用几何均值 / log 转换
- [CON-sample-size-power](CON-sample-size-power.md)：确证性试验的样本量思路，与一期"决策导向"的设计形成对照

## 出处

- Claude 对话（inbox: phaseI_stat.md；AI 生成，原始出处待补）
