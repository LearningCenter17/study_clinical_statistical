---
id: CON-MMRM
title: 重复测量混合模型（Mixed Model for Repeated Measures, MMRM）
categories: [continuous, longitudinal, missing-data, mixed-model]
related: [CON-estimand, GOT-mmrm-convergence, CON-missing-data, CON-sensitivity-analysis, CON-t-test-pvalue, CON-p-value, CON-degrees-of-freedom, CON-distribution-family, CON-test-selection, CON-parametric-vs-nonparametric, CON-covariate, CON-confirmatory-methods-overview, CON-ordinal-data]
sources: [REF-ICH-E9R1]
status: draft
updated: 2026-11-12
---

## 一句话定义

对多次访视的连续型终点（通常是相对基线变化）建模，用非结构化协方差矩阵刻画同一受试者不同访视之间的相关性，
在 MAR 假设下利用所有已观测数据估计各访视的组间差异。

## 什么时候用 / 不该用

- **适合**：连续型终点、多次访视、主要比较某一访视（如第 26 周）的组间差，且 hypothetical 策略 + MAR 假设可接受。
- **不适合单独使用**：estimand 采用 treatment policy 策略且 ICE 后缺失数据较多时，MAR 假设往往不合理，
  需要配合 reference-based MI 等方法或作为 sensitivity analysis。

## 关键假设

- 缺失机制为 MAR（缺失只依赖于已观测数据）。
- 协方差结构设定正确（通常首选非结构化 UN，以减少错误设定风险）。
- 残差近似正态。

## 典型模型设定

- 因变量：CHG（相对基线变化）
- 固定效应：治疗、访视、治疗×访视、基线值、基线×访视，以及分层因素（为什么调整基线和分层因素见 [CON-covariate](CON-covariate.md)）
- 重复效应：访视，受试者内，协方差结构 UN
- 自由度：Kenward-Roger（常见于 SAP），调整的是 Type III 固定效应 F 检验和 LS mean 差 t 检验的分母自由度（F 检验见 [CON-distribution-family](CON-distribution-family.md#f-分布)）

## 实现

### SAS

```sas
proc mixed data=adeff method=reml;
  class trt01pn avisitn usubjid strat1;
  model chg = trt01pn avisitn trt01pn*avisitn base base*avisitn strat1
        / ddfm=kr solution;
  repeated avisitn / subject=usubjid type=un;
  lsmeans trt01pn*avisitn / diff cl alpha=0.05;
run;
```

### R（`mmrm` 包）

```r
library(mmrm)
library(emmeans)

fit <- mmrm(
  CHG ~ TRT01P * AVISIT + BASE * AVISIT + STRAT1 + us(AVISIT | USUBJID),
  data   = adeff,
  method = "Kenward-Roger"
)

emm <- emmeans(fit, ~ TRT01P | AVISIT)
contrast(emm, method = "trt.vs.ctrl")
```

## TLF 里怎么呈现

通常每个访视一行或只列主要访视：各组 n、LS Mean (SE)、组间 LS Mean 差 (95% CI)、p 值。
脚注写明模型的固定效应、协方差结构和自由度方法。

## 常见坑

- UN 不收敛时怎么办 → [GOT-mmrm-convergence](../gotchas/GOT-mmrm-convergence.md)
- `AVISIT` 必须是因子且水平顺序正确；基线访视不应进入模型。
- SAS 与 R 结果的小数位差异：先确认自由度方法、REML、参照组、因子水平是否一致。

## 出处

- [ICH E9(R1)](../references/REF-ICH-E9R1.md)（estimand 框架与 hypothetical 策略）
- `mmrm` 包文档（openpharma）— 出处待补具体版本
