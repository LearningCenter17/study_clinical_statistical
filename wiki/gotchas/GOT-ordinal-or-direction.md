---
id: GOT-ordinal-or-direction
title: "有序 logistic 的 OR 方向：SAS 默认与 R 参数化相反（OR 互为倒数）"
categories: [ordinal, proportional-odds, odds-ratio, sas-vs-r, proc-logistic, descending, polr, clm, qc, double-programming]
related: [CON-proportional-odds-model, CON-ordinal-data, GOT-ttest-student-vs-welch]
sources: ["Claude 对话（inbox: proportional_odds.md）"]
status: draft
updated: 2026-11-12
---

> 出处待补：本卡内容来自 Claude 对话（inbox: proportional_odds.md），属 AI 生成内容，未引用原始文献。R 的符号约定已由 Claude 在 R 4.5.2 中用 `MASS::polr` 复核（见下文）；SAS 部分未实际运行。

## 现象

同一个比例优势模型（见 [CON-proportional-odds-model](../concepts/CON-proportional-odds-model.md)），SAS 和 R 的双重编程 QC 时，最容易出现 **"OR 互为倒数"** 的差异。和 Student vs Welch 一样，这也是软件默认设置不同造成的（另见 [GOT-ttest-student-vs-welch](GOT-ttest-student-vs-welch.md)）。

## 原因：两边的模型写法不一样

| 软件 | 模型 | β > 0 的含义 |
|---|---|---|
| SAS `PROC LOGISTIC`（默认） | logit P(Y ≤ k) = α_k **+** βx | 更倾向于**较低**的类别 |
| SAS 加 `DESCENDING` | logit P(Y ≥ k) = α_k + βx | 更倾向于**较高**的类别 |
| R `MASS::polr`、`ordinal::clm` | logit P(Y ≤ k) = θ_k **−** βx | 更倾向于**较高**的类别 |

所以 **R 的 `exp(coef)` 方向对应 SAS 加了 `DESCENDING` 之后的 OR**，和 SAS 默认的 OR 互为倒数。

> Claude 复核（R 4.5.2，模拟数据 n = 300，0–6 级应答，Drug 组更倾向于低分）：
>
> - `polr` 给 `TRT01PPlacebo` 的系数是 **+0.79**，即安慰剂组更倾向于高分。
> - 逐个切点对 P(Y ≤ k) 拟合二分类 logistic，同一系数为 −0.69、−1.03、−0.87、−0.73、−0.62、−0.30，**符号相反**，与 SAS 默认的参数化一致。
>
> 由此确认了"R 参数化与 SAS 默认相反"。

## SAS：每次都看 Response Profile 下面那行

输出的 Response Profile 下面会注明：

> Probabilities modeled are cumulated over the lower Ordered Values

**每次都要看这一行**，确认模型在对哪一端累积。

## 加不加 `DESCENDING`？

**不是一律加。** 先确定编码方向，即哪一端是"好"的结局，再确定 OR 怎么解读。

例：**mRS 越低越好**。在 SAS 默认方向下（对 P(Y ≤ k) 建模，治疗组 vs 安慰剂），**OR > 1 表示治疗组更倾向于低分，也就是结局更好**。这时不加 `DESCENDING` 反而最直观。

## R 里转换到 SAS 默认方向

```r
exp(-coef(fit)["TRT01PDrug"])  # 取负号再取指数，得到 SAS 默认方向的 OR
```

使用前要确认参照组是安慰剂，否则系数名对不上，见 [CON-proportional-odds-model](../concepts/CON-proportional-odds-model.md#r) 的 ⚠ 说明。

## QC 核对清单

> 补充（Claude）：待 Li 核实。
>
> 1. 应答变量的编码和排序两边一致：R 用 ordered factor 的 levels，SAS 用 `ORDER=` 或数值编码。
> 2. 参照组一致：SAS `ref=`，R `relevel()`。
> 3. 核对 SAS 输出里的 "Probabilities modeled…" 那一行。
> 4. 比较时统一到同一个方向：R 取 `exp(-coef)`，或者 SAS 加 `DESCENDING`。

## 相关卡片

- [CON-proportional-odds-model](../concepts/CON-proportional-odds-model.md)：模型、假设检验与实现
- [CON-ordinal-data](../concepts/CON-ordinal-data.md)：有序数据
- [GOT-ttest-student-vs-welch](GOT-ttest-student-vs-welch.md)：另一个因软件默认设置不同导致结果不一致的例子

## 出处

- Claude 对话（inbox: proportional_odds.md；AI 生成，原始出处待补）
