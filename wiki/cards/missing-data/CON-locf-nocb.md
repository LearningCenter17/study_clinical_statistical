---
id: CON-locf-nocb
title: "LOCF 与 NOCB：末次观测值结转与下次观测值回填的方向（Last Observation Carried Forward / Next Observation Carried Backward）"
categories: [missing-data, single-imputation, locf, nocb, imputation, adam, dtype]
related: [CON-missing-data, CON-cdisc-variable-naming]
sources: ["Claude 对话（inbox: missing_data_1.md）"]
status: draft
updated: 2026-11-25
---

> 出处待补：本卡内容来自 Claude 对话（inbox: missing_data_1.md），属 AI 生成内容，未引用原始文献。需对照 NRC 2010 报告、EMA Guideline on Missing Data in Confirmatory Clinical Trials (2010) 等核实。
>
> 整理记录（2026-11-25）：材料原文"我上一条把 NOCB 写成'向前回填'"指对话中更早的回答，这里改为"表中把 NOCB 译作'向前回填'"；加了"一句话定义"和小节标题。

## 一句话定义

LOCF 和 NOCB 都是用同一受试者**另一次访视的观测值**填补缺失值的单一插补方法，区别在于填补的方向：

| 方法 | 全称 | 方向 | 中文 |
|---|---|---|---|
| **LOCF** | Last Observation Carried **Forward** | 前面的值 → 带到后面 | 末次观测值**向后**结转 |
| **NOCB** | Next Observation Carried **Backward** | 后面的值 → 带到前面 | 下次观测值**向前**回填 |

## 方向怎么理解

表中把 NOCB 译作"向前回填"，容易让人看混。中文的"前/后"有时指方向，有时指时间先后。最直白的理解是：

- **Forward**：用**以前**的值，填**以后**的缺失
- **Backward**：用**以后**的值，填**以前**的缺失

"Backward"在这里的意思是**在时间轴上往回**：把后面访视的值拿回来，填到前面缺失的访视上。

```
时间 →   Baseline    Week 2    Week 4
           12.0       缺失  ←── 8.5
                       ↑
              把后面的值"往回带"
```

> 补充（Claude）：
>
> - LOCF / NOCB 都是单一插补：只填一个值，当作真实观测，不反映填补带来的不确定性，方差会被低估。缺失机制与更合适的方法（MMRM、多重插补）见 [CON-missing-data](CON-missing-data.md)。
> - LOCF 隐含"缺失后病情不再变化"的假设。NRC 2010 报告和 EMA 2010 缺失数据指南都不建议把 LOCF 这类单一插补作为主分析，除非能论证这个假设合理；现在它更多出现在老试验、敏感性分析或特定终点定义中。待 Li 核实。
> - ADaM BDS 数据集中，LOCF 填补出来的记录通常另起一行，`DTYPE = "LOCF"`（`DTYPE` 见 [CON-cdisc-variable-naming](../cdisc/CON-cdisc-variable-naming.md)）。待 Li 核实。

## 相关卡片

- [CON-missing-data](CON-missing-data.md)：缺失机制与对应方法
- [CON-cdisc-variable-naming](../cdisc/CON-cdisc-variable-naming.md)：ADaM 的 `DTYPE`

## 出处

- Claude 对话（inbox: missing_data_1.md；AI 生成，原始出处待补）
