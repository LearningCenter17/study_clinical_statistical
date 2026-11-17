---
id: CODE-ttest-sas-r-python
title: "t 检验的 SAS / R / Python 实现与输出（t-test in SAS, R and Python）"
categories: [t-test, code, sas, r, python, proc-ttest, ods, qc, student, welch]
related: [MTH-t-test, GOT-ttest-student-vs-welch, CON-confidence-interval, CON-p-value, MTH-MMRM]
sources: ["Claude 对话（inbox: calculate_p_value.md）", "Claude 对话（inbox: summary_p.md）"]
status: draft
updated: 2026-11-17
---

> 出处待补：本卡内容来自 Claude 对话（inbox: calculate_p_value.md、summary_p.md），属 AI 生成内容，未引用原始文献。
>
> 拆分记录（2026-11-17）：本卡内容原为 [MTH-t-test](MTH-t-test.md) 的"实现"一节中的三个小节，按"一个知识点一张卡"拆出，内容未改写。t 检验的原理、t 值怎么换成 P 值，仍在那张卡。

## 要解决的问题

同一个两组 t 检验，在 SAS、R、Python 里分别怎么写，输出怎么读，以及三者结果对不上时先查什么。

## 同一组数据：Python / R / SAS

> 整理记录（2026-11-17）：本节原在 CON-p-value 的"实现：软件里怎么算"一节（来源：calculate_p_value.md）。那一节的代码全是 t 检验，移到这里，内容未改。

实际分析中极少手动查表，而是直接调用统计函数（来源：calculate_p_value.md，同一组示例数据）：

```python
# Python (scipy.stats)
from scipy import stats
group1 = [115, 120, 125, 130, 128]
group2 = [105, 110, 108, 112, 109]
t_stat, p_value = stats.ttest_ind(group1, group2)
print(f"P 值: {p_value:.4f}")
```

```r
# R
group1 <- c(115, 120, 125, 130, 128)
group2 <- c(105, 110, 108, 112, 109)
result <- t.test(group1, group2)
print(result$p.value)
```

```sas
/* SAS */
proc ttest data=mydata;
  class group;
  var response;
run;
```

SAS 输出中的 `Pr > |t|` 即为双侧检验的 P 值。

> 补充（Claude）：**同一组数据，上面三段代码给出的 P 值并不相同**：Python 默认 Student t 检验（P = 0.0011），R 默认 Welch t 检验（P = 0.0034），SAS 两行都输出。原因与对齐方法见 [GOT-ttest-student-vs-welch](GOT-ttest-student-vs-welch.md)。这组数据的完整报告写法见 [CON-confidence-interval](../../inference/CON-confidence-interval.md#报告示例)。

## 项目数据的写法

> 补充（Claude）：以下代码非材料原文，待 Li 核实。
>
> ```sas
> proc ttest data=adeff;
>   class trt01pn;
>   var chg;
> run;
> ```
>
> ```r
> t.test(chg ~ trt01pn, data = adeff, var.equal = TRUE)  # 合并方差 t 检验
> ```
>
> - SAS PROC TTEST 会同时输出 Pooled（等方差）和 Satterthwaite（不等方差，Welch）两行，自由度和 P 值不同；R 的 `t.test()` 默认是 Welch，Python `ttest_ind()` 默认是 Student。比对结果时先确认用的是哪一种，详见 [GOT-ttest-student-vs-welch](GOT-ttest-student-vs-welch.md)。
> - 同样的 `t Value` / `Pr > |t|` 也出现在 PROC MIXED 等模型的固定效应和 LS mean 差检验中，此时自由度由模型的自由度方法决定（如 [MMRM](MTH-MMRM.md) 中的 Kenward-Roger）。

## SAS PROC TTEST 输出的四张表

（来源：summary_p.md）

| 表 | 内容 | 备注 |
|---|---|---|
| 1. Statistics | 各组 N、均值、SD、SE | |
| 2. Confidence Limits | 均值和均值差的 95% CI | CI 的读法见 [CON-confidence-interval](../../inference/CON-confidence-interval.md) |
| 3. T-Tests | Pooled 和 Satterthwaite 各一行 | **最关键**；看 Method 列，取哪一行见 [GOT-ttest-student-vs-welch](GOT-ttest-student-vs-welch.md) |
| 4. Equality of Variances | Folded F 检验 | 仅作参考，不要用它来选方法 |

QC 时可以用 `ods output TTests=...` 把结果抽出来，和 R 逐行比对。

> 补充（Claude）：示例写法如下，待 Li 核实（ODS 表名可用 `ods trace on;` 确认）：
>
> ```sas
> ods output Statistics=stat ConfLimits=cl TTests=tt Equality=eqv;
> proc ttest data=adeff;
>   class trt01pn;
>   var chg;
> run;
> ```
>
> 注意 Confidence Limits 表中 Pooled 与 Satterthwaite 的均值差 CI 也各有一行，报告时与 T-Tests 表取同一种方法。

## 相关卡片

- [MTH-t-test](MTH-t-test.md)：t 检验的原理与 t → P 的换算
- [GOT-ttest-student-vs-welch](GOT-ttest-student-vs-welch.md)：Student vs Welch 默认设置不同导致 P 值对不上
- [CON-confidence-interval](../../inference/CON-confidence-interval.md)：这组数据的报告示例
- [MTH-MMRM](MTH-MMRM.md)：模型中的 t 检验与自由度方法

## 出处

- Claude 对话（inbox: calculate_p_value.md；AI 生成，原始出处待补；Python / R / SAS 代码，原在 CON-p-value）
- Claude 对话（inbox: summary_p.md；AI 生成，原始出处待补；PROC TTEST 四张表）
