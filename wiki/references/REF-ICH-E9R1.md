---
id: REF-ICH-E9R1
title: ICH E9(R1) 临床试验中的估计目标与敏感性分析
categories: [guidance, ich, estimand]
related: [CON-estimand, GOT-ice-reason-collection, CON-sensitivity-analysis]
sources: [ICH E9(R1) Addendum, Step 4, 2019-11-20]
status: draft
updated: 2026-11-05
---

## 基本信息

- 全称：Addendum on Estimands and Sensitivity Analysis in Clinical Trials to the Guideline on Statistical Principles for Clinical Trials
- 发布：ICH Step 4，2019 年 11 月
- 地位：对 ICH E9（1998）的补充；FDA、EMA、NMPA 等均已采纳

## 核心内容

1. 提出 estimand 框架：试验目标 → estimand → 主估计方法 → sensitivity analysis，应保持一致。
2. 定义 estimand 的属性和伴发事件处理的五种策略 → 详见 [CON-estimand](../concepts/CON-estimand.md)。
3. 区分 sensitivity analysis（检验同一 estimand 下主分析假设的稳健性）与 supplementary analysis（其他分析）→ 详见 [CON-sensitivity-analysis](../concepts/CON-sensitivity-analysis.md)。
4. 强调 ICE 后数据的收集应由 estimand 决定。

## 对编程工作的影响

- SAP 和 TLF 需要以 estimand 为单位组织主分析和敏感性分析。
- ICE 的识别与派生成为 ADaM 设计的一部分。

## 原文

- ICH 官网 Efficacy Guidelines 页面下载 E9(R1) 原文（建议把 PDF 放入 `inbox/` 后用 `/kb-ingest` 补充细节）。
