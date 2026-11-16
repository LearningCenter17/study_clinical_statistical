---
id: CON-logrank-vs-cox
title: "log-rank 检验与 Cox 模型的分工（Log-rank Test vs Cox Model）"
categories: [survival, log-rank, cox, hazard-ratio, proportional-hazards, sas]
related: [CON-hazard-ratio, CON-null-hypothesis, CON-p-value, CON-test-statistic, CON-confirmatory-methods-overview, CON-confidence-interval]
sources: ["Claude 对话（inbox: logrank_vs_cox.md）", "Claude 对话（inbox: CI_HR.md）"]
status: draft
updated: 2026-11-16
---

> 出处待补：本卡内容来自 Claude 对话（inbox: logrank_vs_cox.md），属 AI 生成内容，未引用原始文献。需对照生存分析教材（如 Collett、Klein & Moeschberger）及 SAS PROC LIFETEST / PHREG 文档核实。

## 一句话定义

**log-rank 检验两组生存曲线是否相同，给 P 值；Cox 模型估计 HR 并检验 HR = 1，给 HR 及 95% CI。** 临床试验 SAP 中两者通常分工使用。

## 两者对比

| | log-rank 检验（`PROC LIFETEST`） | Cox 模型（`PROC PHREG`） |
|---|---|---|
| H₀ | 两组生存曲线在所有时间点都相同：S₁(t) = S₂(t)，等价于风险函数每一时刻都相等 | β = 0，即 **HR = 1**（严格意义上"检验 HR = 1"的是它） |
| 方法类型 | 非参数：比较每个事件时间点"观察到的事件数"与"H₀ 下的期望事件数" | 半参数模型：h₁(t) = h₀(t)·e^β，HR = e^β |
| 估计 HR？ | **不估计** | 给出 HR 估计值和置信区间 |
| 依赖 PH 假设？ | **检验的有效性不依赖**；PH 只影响功效 | 模型本身假设 HR 在整个时间段内恒定 |
| 输出的检验 | log-rank 统计量与 P 值 | 似然比检验、score 检验、Wald 检验 |

## PH 假设对 log-rank 的影响：功效

- PH 成立时，log-rank 是最有效的检验。
- 两条生存曲线**交叉**时（如前期新药组差、后期新药组好），正负差异相互抵消，功效明显下降。

## 二者的关系

- 在 PH 模型框架下，"两组曲线相同"和"HR = 1"是一回事。
- Cox 模型中**只有一个组别协变量**时，log-rank 检验就是它的 **score 检验**。无结点（tied event times）时两者完全相同；有结点时，数值是否一致取决于 ties 的处理方法，可能略有差别。

> 补充（Claude）：SAS PROC PHREG 默认 `ties=BRESLOW`，SAP 中常指定 `ties=EFRON`；与 LIFETEST log-rank 数值的精确对应关系随 ties 方法而变。做 SAS 与 R 核对时，R `survival::coxph()` 默认是 Efron，`survdiff()` 给 log-rank。具体哪种 ties 方法下 score 检验与 log-rank 完全一致，**待 Li 对照 SAS 文档核实**。

## 临床试验中的常见做法

SAP 里通常写：

- **P 值**：来自（分层）log-rank 检验，`PROC LIFETEST`
- **HR 及其 95% CI**：来自（分层）Cox 模型，`PROC PHREG`
- **检查 PH 假设**：log(−log S(t)) 图、Schoenfeld 残差或时间交互项，作为 HR 解释是否合理的依据

**P 值与 CI 偶尔"打架"是正常的**（来源：CI_HR.md）：P 值来自 log-rank，HR 的 CI 来自 Cox（Wald），两者方法不同，偶尔会出现 p 略大于 0.05、但 CI 刚好不包含 1 的情况。SAP 一般会写明各自用哪个方法。CI 与检验"同方法才严格等价"的一般原则见 [CON-confidence-interval](CON-confidence-interval.md#ci-与-p-值的对应)。

> log-rank 的计算思路（来源：CI_HR.md，与上文"方法类型"一致）：在每个事件时间点比较每组"实际发生的事件数"和"两组没差别时预期的事件数"，再把所有时间点加总。

## 实现

### SAS

```sas
/* log-rank：检验生存曲线是否相同，给出 P 值 */
proc lifetest data=adtte;
  time aval * cnsr(1);
  strata trt / test=logrank;
run;

/* Cox：估计 HR 和 95% CI */
proc phreg data=adtte;
  class trt(ref="Placebo");
  model aval * cnsr(1) = trt / risklimits ties=efron;
run;
```

`cnsr(1)` 表示 CNSR = 1 为删失（ADaM ADTTE 惯例）。

> 补充（Claude）：分层时，LIFETEST 用 `strata stratvar / group=trt test=logrank;`，PHREG 在 MODEL 后加 `strata stratvar;`。待核实。

### R

来源：CI_HR.md。

```r
library(survival)

# 分层 Cox：HR 及 95% CI
fit <- coxph(Surv(AVAL, 1 - CNSR) ~ TRT01P + strata(STRAT1), data = adtte)
summary(fit)   # 输出列含义见 CON-hazard-ratio 的"实现"一节

# 分层 log-rank 检验：P 值
survdiff(Surv(AVAL, 1 - CNSR) ~ TRT01P + strata(STRAT1), data = adtte)
```

ADTTE 中 CNSR = 1 表示删失，所以 R 的事件指示变量是 `1 - CNSR`（SAS 写 `cnsr(1)`）。

> 补充（Claude）：`coxph()` 默认 ties = Efron（与 SAS PHREG 默认 Breslow 不同，见上文）。`summary(fit)` 底部还会给出似然比、Wald、score（logrank）三个整体检验；单组别协变量、未分层时，score 检验与 `survdiff()` 的 log-rank 接近。待 Li 核实。

## 常见坑

- 把 log-rank 说成"检验 HR = 1"：不严谨。log-rank 不估计 HR，只在 PH 下与 Cox score 检验等价（本知识库 [CON-hazard-ratio](CON-hazard-ratio.md) 的原始材料就曾这样表述，已据本卡更正）。
- 生存曲线交叉时 log-rank 功效下降，单一 HR 也难以解释——PH 检查不能省。

## 相关卡片

- [CON-hazard-ratio](CON-hazard-ratio.md)
- [CON-null-hypothesis](CON-null-hypothesis.md)
- [CON-p-value](CON-p-value.md)

## 出处

- Claude 对话（inbox: logrank_vs_cox.md；AI 生成，原始出处待补）
- Claude 对话（inbox: CI_HR.md；AI 生成，原始出处待补）
