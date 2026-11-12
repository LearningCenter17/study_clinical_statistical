---
id: CON-CMH
title: "CMH 检验：PROC FREQ 三个统计量与 SCORES= 选项（Cochran-Mantel-Haenszel）"
categories: [categorical, cmh, stratification, ordinal, van-elteren, wilcoxon, kruskal-wallis, sas, proc-freq, scores]
related: [CON-ordinal-data, CON-parametric-vs-nonparametric, CON-test-selection, CON-confirmatory-methods-overview, CON-covariate, CON-proportional-odds-model]
sources: ["Claude 对话（inbox: cmh_statistics.md）"]
status: draft
updated: 2026-11-12
---

> 出处待补：本卡内容来自 Claude 对话（inbox: cmh_statistics.md），属 AI 生成内容，未引用原始文献（如 SAS PROC FREQ 文档、Stokes, Davis & Koch《Categorical Data Analysis Using SAS》）。
>
> 本卡目前只覆盖"**三个统计量怎么选、`SCORES=` 怎么设**"。CMH 用于二分类终点时的内容（共同 OR / RR、Mantel-Haenszel 率差、Breslow-Day 齐性检验）尚待补充。

## CMH 三个统计量怎么选

SAS `PROC FREQ` 的 `CMH` 选项会同时输出三个统计量，按行、列变量是否有序来选：

| 统计量 | 行（治疗组） | 列（应答） | 自由度 |
|---|---|---|---|
| Nonzero Correlation | 有序 | 有序 | 1 |
| **Row Mean Scores Differ** | **无序** | **有序** | 行数 − 1 |
| General Association | 无序 | 无序 | (行 − 1)(列 − 1) |

**治疗组 vs 有序应答**（如 CGI-I、mRS，见 [CON-ordinal-data](CON-ordinal-data.md)）对应的是 **Row Mean Scores Differ**。

> 补充（Claude）：两组比较时行数 − 1 = 1，此时 Row Mean Scores Differ 与 Nonzero Correlation 数值相同。待 Li 核实。

## `SCORES=` 选项决定检验的具体形式

| 选项 | 得分 | 等价的检验 |
|---|---|---|
| `SCORES=TABLE`（默认） | 列变量的原始数值 | 要求编码的**间距有意义** |
| `SCORES=RANK` | 秩得分 | 不分层时等价于 **Kruskal-Wallis**；只有两组时等价于 **Wilcoxon rank-sum** |
| `SCORES=MODRIDIT` | 每层内把秩按 (n_h + 1) 标准化 | 分层时 Row Mean Scores 统计量就是 **van Elteren 检验**（分层 Wilcoxon） |
| `SCORES=RIDIT` | 和 modridit 类似，但标准化方式略有不同 | **不等同于** van Elteren |

Kruskal-Wallis、Wilcoxon 本身见 [CON-test-selection](CON-test-selection.md)；van Elteren 也出现在 [CON-parametric-vs-nonparametric](CON-parametric-vs-nonparametric.md) 的"不容易调整协变量"补充里。

> 补充（Claude）：
> - 等价关系可以从公式看出来。不分层时，Row Mean Scores 统计量为 Q = (n − 1) · Σᵢ nᵢ(s̄ᵢ − s̄)² / Σ(s − s̄)²，其中 s 是得分。把 s 换成秩，就是带结校正的 Kruskal-Wallis H。
> - 分层时各层分别计算得分。各层对统计量的贡献大致按 1/(n_h + 1)（modridit）或 1/n_h（ridit）加权，这就是两者"略有不同"的地方。
> - 以上为 Claude 推导和记忆，未对照 SAS 文档，待 Li 核实。

## 写代码时要注意

```sas
proc freq data=adeff;
  tables strata * trt01pn * aval / cmh scores=modridit;
run;
```

- **分层变量放最前面，治疗组必须在行的位置，应答在列的位置。** 顺序放反的话，Row Mean Scores 检验的就是另一个方向的假设。
- **应答变量的排序要正确。** 字符型变量默认可能按字母排序，所以最好用数值编码（如 `AVAL`），或者设置 `ORDER=`。`AVAL` / `AVALC` 的约定见 [CON-ordinal-data](CON-ordinal-data.md#adam-中的存储)。

> 更正记录（2026-11-12）：Claude 最初给的代码写的是 `avaln`。按 ADaM 更正（`AVALN` 不是 BDS 标准变量），这里应该用存有序编码的 `AVAL`。上面的代码已改。

## 相关卡片

- [CON-ordinal-data](CON-ordinal-data.md)：有序应答的分析方法
- [CON-parametric-vs-nonparametric](CON-parametric-vs-nonparametric.md)：van Elteren（分层 Wilcoxon）
- [CON-test-selection](CON-test-selection.md)：Wilcoxon、Kruskal-Wallis
- [CON-covariate](CON-covariate.md)：分层因素是常见的需要调整的变量
- [CON-confirmatory-methods-overview](CON-confirmatory-methods-overview.md)：CMH 在确证性试验中的位置

## 出处

- Claude 对话（inbox: cmh_statistics.md；AI 生成，原始出处待补）
