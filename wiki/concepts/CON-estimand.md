---
id: CON-estimand
title: 估计目标（Estimand）
categories: [estimand, ich-e9r1, intercurrent-event, design]
related: [CON-MMRM, REF-ICH-E9R1, GOT-ice-reason-collection, CON-missing-data, CON-rescue-medication, CON-sensitivity-analysis, CON-null-hypothesis]
sources: [REF-ICH-E9R1, "Claude 对话（inbox: Estimand_1.md）", "Claude 对话（inbox: hypothetical_vs_completers.md）"]
status: draft
updated: 2026-11-05
---

## 一句话定义

Estimand 是对"这个试验到底要估计什么治疗效应"的精确描述，在选统计方法之前先定义清楚。

## 为什么需要 estimand

> 以下动机说明来自 Claude 对话（inbox: Estimand_1.md），AI 生成，出处待补。

例子：糖尿病试验，主要终点为第 24 周 HbA1c 相对基线变化，部分患者血糖控制太差而使用了救援药物。

- 直接使用救援后的 HbA1c → 估计的效果混入了救援药的作用；
- 删掉救援后的数据 → 估计的已经是另一个问题。

过去这类问题常被当作"缺失数据怎么处理"的技术问题讨论；ICH E9(R1) 的贡献是指出它其实是**想回答什么科学问题**，必须在设计阶段就说清楚。

## 五个属性

| 属性 | 含义 | 例子 |
|---|---|---|
| Treatment | 比较的治疗条件 | 试验药 vs 安慰剂，均在背景治疗之上 |
| Population | 目标人群 | 符合入排标准的成人 2 型糖尿病患者 |
| Variable（Endpoint） | 每个受试者层面测量的变量 | 第 26 周 HbA1c 相对基线变化 |
| Intercurrent events 处理 | 对伴发事件采用的策略 | 停药 → treatment policy；使用救援药 → hypothetical |
| Population-level summary | 人群层面的汇总量 | 组间均值差 |

## 伴发事件（Intercurrent Event, ICE）的五种策略

| 策略 | 思路 | 典型场景 |
|---|---|---|
| Treatment policy | ICE 发生后的数据照常使用，ICE 视为治疗策略的一部分 | 停药后继续随访测量 |
| Hypothetical | 估计"假如 ICE 没发生"时的效应 | 救援药使用后的数据不用，按 MAR 建模 |
| Composite variable | 把 ICE 纳入终点定义 | 停药记为"无应答" |
| While on treatment | 只关注 ICE 发生前的效应 | 症状缓解类、姑息治疗 |
| Principal stratum | 只针对某个潜在亚群（如"不会发生 ICE 的人"） | 研究较少，假设强 |

### 直观理解：策略 = 你想问哪个问题

> 以下来自 Claude 对话（inbox: Estimand_1.md），AI 生成，出处待补。

五种策略听起来像五种"计算方法"，其实是五种不同的**提问方式**。例：减肥药服用 6 个月看体重变化，有人中途因副作用自行停药。

| 提问 | 停药者怎么处理 | 对应策略 | 关心的是 |
|---|---|---|---|
| "医生开了这个药，6 个月后病人实际瘦了多少？" | 照算实际观测值，因为现实中就有人停药 | Treatment policy | 现实效果 |
| "如果病人坚持吃满 6 个月，能瘦多少？" | 停药后数据不用，推测"假如没停会怎样" | Hypothetical | 药物本身的效力 |
| "有多少人既坚持吃药、又成功瘦了 5 公斤？" | 停药本身算失败 | Composite | 效力 + 能否坚持（耐受性等） |

三个问题都合理，但答案不同。Estimand 框架要求**事先**说清楚问的是哪一个，不能等数据出来再挑结果好看的。

材料认为实际工作中主要碰到的是 treatment policy、hypothetical、composite 三种；while on treatment 和 principal stratum 较少见。

### Composite 策略如何把耐受性"算进"结果

Composite（停药 = 失败）下，药要拿高分必须同时：药效好 **且** 病人能坚持吃完。示例（各 100 人）：

| | 药 A | 药 B |
|---|---|---|
| 因副作用停药 | 5 人 | 40 人 |
| 完成者中瘦 ≥5 kg 的比例 | 60% | 90% |
| 只看完成者（原材料用作 hypothetical 的直观近似，**不严谨**，见下） | 60% | 90% → B 更好 |
| Composite：成功人数 | 95 × 60% ≈ 57 | 60 × 90% = 54 → A 略胜 |

药 B 单论药效强，但四成人受不了；composite 能反映这一点，hypothetical 则把它"假设掉"了。

停药不一定都因副作用（也可能觉得无效、搬家等），所以更准确地说，composite 衡量的是"药效 + 病人能否坚持"的综合结果，耐受性是其中主要因素。

**更正：hypothetical ≠ 完成者分析**（Claude 对话 inbox: hypothetical_vs_completers.md，AI 生成，出处待补）。完成者是自我选择出来的，不是随机子集；两组按不同程度筛掉人之后，随机化带来的可比性被破坏。药 B 的 90% 很可能高估了它在 hypothetical 意义下的真实效果。完成者分析只在 MCAR 下无偏；实际中 hypothetical 通常用 MMRM / MI 在 MAR 下估计，并配 MNAR 敏感性分析 → 详见 [CON-missing-data](CON-missing-data.md)。

### 按 ICE 原因分别选策略

> 以下来自 Claude 对话（inbox: Estimand_1.md），AI 生成，出处待补。

最"粗暴"的 composite 不论原因停药都算失败：简单、保守，但与药无关的停药（如搬家）也会拉低药的成绩。材料称 E9(R1) 允许**按停药原因分别选策略**，SAP 中常见混合使用，例如：

| 停药原因 | 处理 | 理由 |
|---|---|---|
| 不良事件 / 副作用 | 算失败（composite） | 与药有关，药该"负责" |
| 缺乏疗效 | 算失败（composite） | 同上 |
| 搬家、工作变动等 | 视为缺失，按"假如没停"推测（hypothetical） | 与药无关 |

所以 SAP 的 estimand 一节常会有一张表，列出每类 ICE 各自用什么策略。前提是停药原因被准确收集 → 见 [GOT-ice-reason-collection](../gotchas/GOT-ice-reason-collection.md)。

### Hypothetical 策略对不同 ICE 的合理性不同

> 以下来自 Claude 对话（inbox: hypothetical_vs_completers.md），AI 生成，出处待补。

- "假如没用[救援药](CON-rescue-medication.md)"是比较容易想象、临床上有意义的情境；
- "假如没有出现副作用、一直坚持吃"就比较可疑，因为副作用本身就是药的一部分。

因此不少统计师主张：救援药用 hypothetical；因副作用或无效停药更适合 treatment policy 或 composite。按原因分配策略，不仅是为了公平，也是因为有些 hypothetical 情境本身就不太站得住。

> ⚠ 存在分歧（程度上的）：上一节的表（Estimand_1.md）对搬家等与药无关的停药用 hypothetical、对 AE / 无效停药用 composite；本节材料对 AE / 无效停药给出 treatment policy **或** composite 两种选择。两者不矛盾，但具体选哪种取决于试验，待 Li 判断是否需要统一表述。

> 补充（Claude）：E9(R1) 原文表述为对不同的 intercurrent event 可采用不同策略；"按停药原因区分"是将不同原因的停药定义为不同类型 ICE 的常见做法。具体条文待对照 [REF-ICH-E9R1](../references/REF-ICH-E9R1.md) 核实。

## 和统计方法的关系

- Estimand 决定方法，不是反过来。
- 常见对应：hypothetical 策略 + MAR 假设 → [MMRM](CON-MMRM.md) 可作为主分析；
  treatment policy 策略需要收集 ICE 后数据，缺失部分常用 reference-based MI 等方法处理。
- 每个 estimand 应配有针对其主要假设的 sensitivity analysis（与 supplementary analysis 的区别见 [CON-sensitivity-analysis](CON-sensitivity-analysis.md)）。

## 对统计编程的影响

- ADaM 中需要能识别 ICE：发生日期、类型（停药、救援药、死亡等），通常在 ADSL 或专门的 ICE 数据集中派生。
- 分析数据集要能按策略切换"ICE 后数据是否使用"，常见做法是派生分析标志变量（如 ANLzzFL）。
- SAP 中每个 estimand 的五个属性应能一一对应到 TLF 的脚注或标题。
- ADaM 中的分析标记变量（如 ANL01FL）、救援后数据被排除或保留的规则，本质上就是在实现某个 estimand 策略。读 SAP 时可先找 estimand 一节，再看 ADaM 规格里这些规则如何落地。（Claude 对话 inbox: Estimand_1.md）
- 按原因区分策略依赖停药原因的数据质量（CRF、SDTM DS 域）→ [GOT-ice-reason-collection](../gotchas/GOT-ice-reason-collection.md)。

## 出处

- [ICH E9(R1)](../references/REF-ICH-E9R1.md)
- Claude 对话（inbox: Estimand_1.md；AI 生成，原始出处待补）
- Claude 对话（inbox: hypothetical_vs_completers.md；AI 生成，原始出处待补）
