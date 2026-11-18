---
id: CON-prognostic-factor
title: "预后因素与预测因素（Prognostic vs Predictive Factor）"
categories: [design, prognostic-factor, predictive-factor, stratification, covariate, baseline, enrichment, subgroup, biomarker]
related: [CON-stratified-randomization, CON-covariate, CON-sample-size-power]
sources: ["Claude 对话（inbox: prognostic_factor.md）", "Claude 对话（inbox: stratification_imbalance_correction.md）"]
status: draft
updated: 2026-11-17
---

> 出处待补：本卡内容来自 Claude 对话（inbox: prognostic_factor.md、stratification_imbalance_correction.md），属 AI 生成内容，未引用原始文献。建议对照 ICH E9 第 2.3 节（分层随机）、EMA *Guideline on adjustment for baseline covariates in clinical trials*（2015）、FDA *Enrichment Strategies for Clinical Trials*（2019）。

## 一句话定义

**预后因素（prognostic factor）**：**不管接受什么治疗，都会影响患者结局的基线特征**。"强"预后因素指它对结局的影响很大，有时比治疗本身的效果还大。

**预测因素（predictive factor）**：影响**治疗效果大小**的因素（见下文对比）。

## 举例

| 疾病或研究 | 强预后因素 | 对结局的影响 |
|---|---|---|
| 肿瘤 | 分期（I 期与 IV 期）、ECOG 体能评分 | IV 期患者的生存期远短于早期患者，不论用什么药 |
| 心衰 | 射血分数（LVEF）、NYHA 分级 | 分级越高，住院率和死亡率越高 |
| 糖尿病 | 基线 HbA1c | 基线越高，HbA1c 下降的空间越大 |
| 高血压 | 基线血压 | 基线越高，降压幅度通常越大 |
| 多中心试验 | 地区或中心 | 医疗水平和患者构成不同，结局差异明显 |
| 很多疾病 | 年龄、既往治疗线数 | 年龄大、已经治疗失败多次的患者，结局通常较差 |

基线值作为协变量的例子（基线血压）见 [CON-covariate](../methods/continuous/CON-covariate.md)。

## 为什么强预后因素需要分层

假设一个肿瘤试验，IV 期患者的中位生存期是 6 个月，早期患者是 36 个月。如果随机化后偶然出现：

- 药物组：IV 期患者占 70%
- 安慰剂组：IV 期患者占 40%

药物组的生存期很可能更短，但原因是**药物组的病情本来就更重**，不是药物无效。

**此例为说明原理而故意夸大；样本量适中或较大时，简单随机化很少产生这么大的不均衡**（每组 100 人时出现 ≥ 30 个百分点差异的概率约 0.002%）。分层的价值主要在小样本、亚组、让分析与设计一致，以及提高精确度，见 [CON-stratified-randomization](CON-stratified-randomization.md#分层主要在什么时候有用)（来源：stratification_imbalance_correction.md）。

> 更正记录（2026-11-17）：prognostic_factor.md 原文写"分期对结局的影响太大，一点点不均衡就足以掩盖或扭曲真实的疗效"。后续对话（stratification_imbalance_correction.md）确认这个说法偏重，改为上面的写法。

所以，**预后因素影响越大，越需要通过分层保证它在两组中均衡**。对结局影响很小的因素，即使两组有些不均衡也不会改变结论，没必要分层。这也是分层因素只选 2 到 3 个最重要因素的依据，分层太多的问题见 [CON-stratified-randomization](CON-stratified-randomization.md)。

强预后因素通常**既用来分层，又在分析中作为协变量调整**（见 [CON-covariate](../methods/continuous/CON-covariate.md)）。

## 怎么判断是不是强预后因素

- **既往研究或文献**：如该疾病的自然病程研究、历史对照数据、前期试验
- **临床共识**：如肿瘤分期、指南中的风险分层工具
- **前期试验数据**：在 II 期数据中看哪些基线变量与结局的关系最强

## 容易混淆：预后因素 vs 预测因素

| | 预后因素（prognostic） | 预测因素（predictive） |
|---|---|---|
| 含义 | 影响结局本身，不论用什么治疗 | 影响**治疗效果的大小** |
| 例子 | 肿瘤分期：分期晚的患者用药或不用药，结局都更差 | HER2 阳性：只有 HER2 阳性的患者用曲妥珠单抗才有效 |
| 设计中的用途 | 作为分层因素或协变量，保证均衡、提高效率 | 用于富集设计、亚组分析，甚至只入组特定人群 |

有些因素**同时是预后因素和预测因素**，例如某些基因突变。

> 补充（Claude）：
>
> - HER2 本身就是"两者兼有"的典型：未经抗 HER2 治疗时，HER2 阳性乳腺癌预后较差（预后因素）；同时它决定了曲妥珠单抗是否有效（预测因素）。
> - 统计上，预后因素表现为**主效应**（结局 ~ 治疗 + 因素 中因素的系数），预测因素表现为**治疗 × 因素交互作用**。亚组分析的森林图看的就是后者，而亚组间的交互检验 power 通常很低。
> - 待 Li 核实。

## 相关卡片

- [CON-stratified-randomization](CON-stratified-randomization.md)：按强预后因素分层，但层数要少
- [CON-covariate](../methods/continuous/CON-covariate.md)：预后因素在分析中作为协变量调整
- [CON-sample-size-power](CON-sample-size-power.md)：协变量调整与样本量

## 出处

- Claude 对话（inbox: prognostic_factor.md；AI 生成，原始出处待补）
- Claude 对话（inbox: stratification_imbalance_correction.md；AI 生成，原始出处待补）
