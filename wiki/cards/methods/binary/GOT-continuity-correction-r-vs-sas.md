---
id: GOT-continuity-correction-r-vs-sas
title: "R 与 SAS 的连续性校正默认值不同：双编程 P 值对不上（Continuity Correction Defaults in R vs SAS）"
categories: [gotcha, continuity-correction, yates, r-vs-sas, double-programming, qc, chi-square, cmh, mcnemar, wilcoxon, proc-freq, proc-npar1way]
related: [CON-continuity-correction, MTH-chi-square, MTH-CMH, MTH-ci-construction, CON-test-selection, GOT-ttest-student-vs-welch]
sources: ["Claude 对话（inbox: Continuity correction.md）"]
status: draft
updated: 2026-11-18
---

> 出处待补：本卡内容来自 Claude 对话（inbox: Continuity correction.md），属 AI 生成内容，未引用原始文献。R 各函数的默认值已由 Claude 在 R 4.5.2 中核对（`formals()`）；SAS 选项未实际运行，待对照 SAS 文档核实。连续性校正本身是什么、什么时候用，见 [CON-continuity-correction](../../inference/CON-continuity-correction.md)。

## 现象

做 R 和 SAS 双编程交叉核对（QC）时，这里是一个**常见的结果对不上的原因**：同一张表，R 和 SAS 算出的卡方、CMH、McNemar 等 P 值不一样。

## 原因：两边默认值不同

| 方法 | R 默认 | SAS 默认 |
|---|---|---|
| 2×2 卡方 | `chisq.test()` **校正** | `PROC FREQ /CHISQ` 校正和不校正**都输出** |
| CMH | `mantelhaen.test()` **校正** | `/CMH` **不校正** |
| 两比率比较 | `prop.test()` **校正** | — |
| 比率置信区间 | `prop.test()` 的 CI **校正**；`binom.test()` 是精确法 | `BINOMIAL` 默认 Wald **不校正**，要校正加 `BINOMIAL(CORRECT)` |
| 率差置信区间 | — | `RISKDIFF` 默认**不校正**，要校正加 `RISKDIFF(CORRECT)` |
| McNemar | `mcnemar.test()` **校正** | `/AGREE` **不校正** |
| Wilcoxon | `wilcox.test()` **校正**（使用正态近似时） | `PROC NPAR1WAY` **校正**，要关掉加 `CORRECT=NO` |

可以看出一个规律：**R 的默认值大多是校正的，SAS 的大多是不校正的**（NPAR1WAY 是例外）。

- R 端关掉校正：`chisq.test()`、`mantelhaen.test()`、`prop.test()` 都用 `correct = FALSE`。
- SAS `PROC FREQ /CHISQ`：读 "Chi-Square" 行是不校正的；"Continuity Adj. Chi-Square" 行是校正的。

> 整理记录（2026-11-18）：材料中有两张内容重叠的 R / SAS 对照表（"实际编程要注意"一节的 5 行表和"SAS 和 R 的默认设置"一节的 7 行表）。这里保留 7 行全表，5 行表多出的"怎么改"信息（`correct = FALSE`、SAS 两行输出的名称）写在表下两条。
>
> 数值复核（Claude）：R 4.5.2 中 `chisq.test`、`mantelhaen.test`、`prop.test`、`mcnemar.test`、`wilcox.test.default` 的 `correct` 参数默认值均为 `TRUE`。

## 怎么避免

1. **先看 SAP 规定的是哪一种**（校正 / 不校正 / Fisher 精确），两边都按 SAP 设。
2. R 和 SAS 结果对不上时，先检查校正选项是否一致，再对照 SAP 里规定的是哪一种。
3. 如果 SAS 的 CMH p 值和 R 的对不上，第一件事就是检查 R 有没有加 `correct = FALSE`。

算例：降压药 2×2 表，R 默认（Yates 校正）χ² = 7.92、p = 0.0049；`correct = FALSE` 时 χ² = 9.09、p = 0.0026，与 SAS "Chi-Square" 行对应（见 [MTH-chi-square](MTH-chi-square.md#r-复核)）。CMH 的写法见 [MTH-CMH](MTH-CMH.md#程序里怎么做)。

> 数值复核（Claude，原写在 CON-test-selection 抗感染算例下）：所以同一张表"R 默认结果"和材料不同，要看是否加了 `correct = FALSE`。SAS PROC FREQ 的 `chisq` 选项两种都输出（"Chi-Square" 与 "Continuity Adj. Chi-Square"）。
>
> 整理记录（2026-11-18）：上一条原在 CON-test-selection（抗感染算例，p = 0.0074 vs 0.0106），经 MTH-chi-square 移到本卡，原样保留。

> 补充（Claude）：同类的"默认设置不同导致 P 值对不上"还有 t 检验的 Student vs Welch，见 [GOT-ttest-student-vs-welch](../continuous/GOT-ttest-student-vs-welch.md)。

## 相关卡片

- [CON-continuity-correction](../../inference/CON-continuity-correction.md)：连续性校正的原理、争议和使用场景
- [MTH-chi-square](MTH-chi-square.md)：卡方检验及算例
- [MTH-CMH](MTH-CMH.md)：CMH 的 SAS / R 写法
- [MTH-ci-construction](../../inference/MTH-ci-construction.md)：比例和率差的 CI 方法
- [GOT-ttest-student-vs-welch](../continuous/GOT-ttest-student-vs-welch.md)：另一个 R / SAS 默认不同的例子

## 出处

- Claude 对话（inbox: Continuity correction.md；AI 生成，原始出处待补）
