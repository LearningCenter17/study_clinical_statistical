---
id: CON-sensitivity-analysis
title: "敏感性分析与补充分析（Sensitivity Analysis vs Supplementary Analysis）"
categories: [sensitivity-analysis, supplementary-analysis, estimand, ich-e9r1, missing-data]
related: [CON-estimand, CON-missing-data, CON-MMRM, REF-ICH-E9R1]
sources: ["Claude 对话（inbox: sensitivity_analysis1.md）"]
status: draft
updated: 2026-11-05
---

> 出处待补：本卡内容来自 Claude 对话（inbox: sensitivity_analysis1.md），属 AI 生成内容，未引用原始文献，需对照 ICH E9(R1) 原文（sensitivity / supplementary analysis 相关章节）核实。

## 一句话定义

Sensitivity analysis（敏感性分析）：**换几种不同的假设，把主分析重新做一遍，看结论会不会变**——针对的是**同一个 estimand**。

## 为什么需要

主分析总是建立在某些假设上，最典型的是"缺失数据属于 MAR"，而这个假设**没法用数据验证**（见 [CON-missing-data](CON-missing-data.md#mar-无法被数据验证)）。既然验证不了，就换个思路：假如这个假设错了，结论还站得住吗？

类比：贷款买房按"利率 6%、收入不变"算出月供能承受。稳妥的做法是再算利率涨到 8%、收入降 20%、两者同时发生的情况；都扛得住，决定才算稳健。敏感性分析就是给试验结论做这种"压力测试"。

## 临床试验里的典型组合

| 分析 | 假设 |
|---|---|
| 主分析：[MMRM](CON-MMRM.md) | 缺失为 MAR |
| 敏感性分析 1：Jump to reference（J2R） | 停药者表现回到安慰剂组水平 |
| 敏感性分析 2：Tipping point | 逐步假设试验组缺失者更差，找到结论翻转的点 |
| 敏感性分析 3：模式混合模型（pattern mixture model） | 对不同退出模式分别做不同假设 |

各方法的细节见 [CON-missing-data](CON-missing-data.md#mar-何时站不住敏感性分析)。

如果几种分析结论一致，监管机构就比较放心；如果主分析显著、换个假设就不显著了，结论就会被质疑。

> 补充（Claude）：J2R 在 hypothetical + MAR 主分析下常作为敏感性分析，但在 treatment policy 策略下可能就是主分析的插补方法（见 [CON-missing-data](CON-missing-data.md#策略决定缺失怎么补)）。所以"某方法是不是敏感性分析"取决于它相对于哪个 estimand 和主分析。

## E9(R1) 的关键界定：敏感性分析 vs 补充分析

敏感性分析必须**针对同一个 estimand**，只是换估计时用的假设；要和 **supplementary analysis（补充分析）**区分开：

| | 敏感性分析 | 补充分析 |
|---|---|---|
| 回答的问题 | 同一个 estimand | 可以是不同的 estimand 或角度 |
| 目的 | 检验主分析结论是否稳健 | 更全面地理解疗效 |
| 例子 | 换缺失假设重做主分析 | 完成者分析、per-protocol 分析、亚组分析 |

## 常见坑

- **把 per-protocol 分析叫"敏感性分析"**：很常见，但按 E9(R1) 的定义，它回答的是另一个问题，严格来说属于补充分析。完成者分析同理（见 [CON-estimand](CON-estimand.md) 中"hypothetical ≠ 完成者分析"）。
- 敏感性分析不是为了得到更好看的结果，而是诚实地检验"如果我的假设错了，结论会怎样"。

> 补充（Claude）：读 SAP / TLF shell 时，可检查每个标为 sensitivity 的分析是否确实对应主 estimand；对应不上的应归入 supplementary。TLF 标题中两者的标注方式待建 TLF- 卡片时补充。

## 相关卡片

- [CON-estimand](CON-estimand.md)
- [CON-missing-data](CON-missing-data.md)
- [CON-MMRM](CON-MMRM.md)
- [REF-ICH-E9R1](../references/REF-ICH-E9R1.md)

## 出处

- Claude 对话（inbox: sensitivity_analysis1.md；AI 生成，原始出处待补）
