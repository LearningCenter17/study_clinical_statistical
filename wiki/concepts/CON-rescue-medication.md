---
id: CON-rescue-medication
title: 救援药物（Rescue Medication / Rescue Therapy）
categories: [rescue-medication, intercurrent-event, estimand, sdtm, adam, design]
related: [CON-estimand, CON-missing-data, GOT-ice-reason-collection]
sources: ["Claude 对话（inbox: rescue medication1.md）"]
status: draft
updated: 2026-11-05
---

> 出处待补：本卡内容来自 Claude 对话（inbox: rescue medication1.md），属 AI 生成内容，未引用原始文献，需对照 protocol 示例 / SDTMIG / 文献核实。

## 一句话定义

Rescue medication（也称 rescue therapy / rescue treatment）是试验中当患者病情控制不住、继续只用试验药（或安慰剂）在伦理上说不过去时，按方案允许额外给予的治疗。目的是保护患者，不让他们因为留在试验里而受害。尤其是安慰剂组，没有救援机制的话很多试验过不了伦理审查。

## 典型例子

| 领域 | 触发条件 | 救援治疗 |
|---|---|---|
| 糖尿病 | HbA1c 或空腹血糖超过方案阈值 | 加用二甲双胍或胰岛素 |
| 哮喘 | 急性发作 | 沙丁胺醇（albuterol）等短效支气管扩张剂 |
| 疼痛 | 止痛效果不够 | 对乙酰氨基酚（paracetamol / acetaminophen） |
| 类风湿关节炎 | 疾病活动度没有改善 | 第 16 周起允许换到活性药或加用激素 |

## 特点

- **方案事先规定**：触发条件（rescue criteria）、可用药物、剂量都写在 protocol 里。
- **不同于合并用药（concomitant medication）**：合并用药治疗其他疾病或一直在用；救援药专门针对本研究疾病控制不佳。
- **救援药的使用本身常是终点**：如"至首次使用救援药的时间"、"救援药使用量"，在疼痛和哮喘试验中很常见。

## 在 estimand 中的角色

使用救援药是典型的 intercurrent event。常见做法是对救援药采用 hypothetical 策略（"假如没用救援药"情境容易想象、临床上有意义），详见 [CON-estimand](CON-estimand.md#hypothetical-策略对不同-ice-的合理性不同)。

## 对统计编程的影响

- **SDTM**：通常记录在 CM 域，用 `CMCAT` 或 `CMSCAT` 标记为 rescue，或在专门的 CRF 页收集。
- **ADaM**：派生救援标记或首次救援日期，用来决定哪些记录在 hypothetical 策略下被排除（如某个 ANLxxFL 在救援后置空）——这就是 estimand 落地的地方。

## 相关卡片

- [CON-estimand](CON-estimand.md)
- [CON-missing-data](CON-missing-data.md)
- [GOT-ice-reason-collection](../gotchas/GOT-ice-reason-collection.md)：同属"ICE 数据收集是统计分析上游"的问题

## 出处

- Claude 对话（inbox: rescue medication1.md；AI 生成，原始出处待补）
