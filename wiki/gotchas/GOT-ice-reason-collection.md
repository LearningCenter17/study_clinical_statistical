---
id: GOT-ice-reason-collection
title: 停药原因收集含糊导致无法按原因选 ICE 策略
categories: [estimand, intercurrent-event, crf, sdtm, data-collection, missing-data]
related: [CON-estimand, REF-ICH-E9R1, CON-rescue-medication, CON-missing-data]
sources: ["Claude 对话（inbox: Estimand_1.md）", "Claude 对话（inbox: missing_1.md）"]
status: draft
updated: 2026-11-05
---

> 出处待补：本卡内容来自 Claude 对话（inbox: Estimand_1.md、missing_1.md），属 AI 生成内容，未引用原始文献，需对照 ICH E9(R1) 及 SDTMIG（DS 域）核实。

## 坑是什么

SAP 常按停药原因给不同类型的 intercurrent event 分配不同策略（如不良事件、缺乏疗效 → composite；搬家等与药无关 → hypothetical），详见 [CON-estimand](../concepts/CON-estimand.md#按-ice-原因分别选策略)。

**前提是停药原因被准确收集。** 如果 CRF 上停药原因的选项设计含糊（例如大量落入"其他"），统计师后面就无法把停药归到正确的 ICE 类型，按原因区分的策略也就落不了地。

## 涉及环节

- **EDC / CRF 设计**：停药原因的选项怎么设，是否能区分"与治疗相关"和"与治疗无关"的原因。
- **SDTM DS 域**：如 `DSDECOD` 等变量承载标准化后的处置原因，是 ADaM 派生 ICE 类型的上游。
- **ADaM**：ICE 类型和分析标记变量（如 ANLzzFL）依赖上述原因派生。

数据库设计其实是统计分析的上游。

## 更深一层：真实原因往往收不上来

（来源：missing_1.md）即使 CRF 设计得好，能记录的通常只是**表面原因**，例如：

- Lost to follow-up（失访）
- Withdrawal by subject（受试者撤回同意）
- Other

病人真实的想法（如"我体重反弹了，不好意思来"）几乎不可能被如实记下。同样一条"失访"，背后可能是搬家（接近 MCAR），也可能是病情变差（MNAR），从数据上分不出来——这正是 MNAR 最麻烦的地方。缺失机制的完整说明见 [CON-missing-data](../concepts/CON-missing-data.md)。

## 怎么避免

材料支持的做法（missing_1.md）：

- 停药原因选项设计得具体，少依赖"其他"。
- 失访前最后一次联系的情况、最后的测量值都要记录完整。这些虽然不能证明缺失机制，但能帮统计师判断哪种假设更合理——EDC 设计时就能发挥作用。
- **停药不等于退出试验**：停药后也尽量继续评估，收集 retrieved dropout data（见 [CON-missing-data](../concepts/CON-missing-data.md#应对思路减少缺失--收细原因--敏感性分析兜底)）。

> 补充（Claude）：以下为一般性建议，非材料原文，待 Li 核实。
>
> - 在 CRF 定稿前对照 SAP / protocol 的 estimand 定义，确认每类需要区分的 ICE 都有对应的停药原因选项。
> - 若保留"其他"，要求填写说明并预先规定其归类规则。
> - CRF 上把"停研究药物"与"退出研究"分开收集，二者对应的 ICE 和后续数据收集不同。

## 相关卡片

- [CON-estimand](../concepts/CON-estimand.md)
- [REF-ICH-E9R1](../references/REF-ICH-E9R1.md)
- [CON-missing-data](../concepts/CON-missing-data.md)
- [CON-rescue-medication](../concepts/CON-rescue-medication.md)

## 出处

- Claude 对话（inbox: Estimand_1.md；AI 生成，原始出处待补）
- Claude 对话（inbox: missing_1.md；AI 生成，原始出处待补）
