---
id: CON-estimand
title: 估计目标（Estimand）
categories: [estimand, ich-e9r1, intercurrent-event, design]
related: [CON-MMRM, REF-ICH-E9R1]
sources: [REF-ICH-E9R1]
status: draft
updated: 2026-11-02
---

## 一句话定义

Estimand 是对"这个试验到底要估计什么治疗效应"的精确描述，在选统计方法之前先定义清楚。

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

## 和统计方法的关系

- Estimand 决定方法，不是反过来。
- 常见对应：hypothetical 策略 + MAR 假设 → [MMRM](CON-MMRM.md) 可作为主分析；
  treatment policy 策略需要收集 ICE 后数据，缺失部分常用 reference-based MI 等方法处理。
- 每个 estimand 应配有针对其主要假设的 sensitivity analysis。

## 对统计编程的影响

- ADaM 中需要能识别 ICE：发生日期、类型（停药、救援药、死亡等），通常在 ADSL 或专门的 ICE 数据集中派生。
- 分析数据集要能按策略切换"ICE 后数据是否使用"，常见做法是派生分析标志变量（如 ANLzzFL）。
- SAP 中每个 estimand 的五个属性应能一一对应到 TLF 的脚注或标题。

## 出处

- [ICH E9(R1)](../references/REF-ICH-E9R1.md)
