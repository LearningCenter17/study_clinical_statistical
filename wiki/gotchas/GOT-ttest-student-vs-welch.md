---
id: GOT-ttest-student-vs-welch
title: "同一数据 t 检验 P 值不同：Student vs Welch 默认设置（Student's vs Welch's t-test）"
categories: [t-test, welch, satterthwaite, pooled-variance, sas-vs-r, python, software-default, degrees-of-freedom, two-stage-procedure, levene, type-i-error]
related: [CON-t-test-pvalue, CON-p-value, CON-degrees-of-freedom, CON-t-distribution, CON-distribution-family, CON-type-I-II-error, CON-null-hypothesis, CON-confidence-interval, CON-test-selection, GOT-skewed-small-sample]
sources: ["Claude 对话（inbox: ttest_student_vs_welch.md）", "Claude 对话（inbox: calculate_p_value.md）", "Claude 对话（inbox: summary_p.md）"]
status: draft
updated: 2026-11-11
---

> 出处待补：本卡内容来自 Claude 对话（inbox: ttest_student_vs_welch.md、summary_p.md），以及 Claude 对 calculate_p_value.md 示例代码的 R 复现，属 AI 生成内容，未引用原始文献。

## 现象

同一组数据，在 Python、R、SAS 里做"两独立样本 t 检验"，P 值对不上。例子来自 [CON-p-value](../concepts/CON-p-value.md#实现软件里怎么算)：

```
group1 = 115, 120, 125, 130, 128
group2 = 105, 110, 108, 112, 109
```

| 软件 | 默认方法 | 本例结果（Claude 用 R 4.5.2 复现） |
|---|---|---|
| Python `scipy.stats.ttest_ind()` | Student's t 检验（`equal_var = True`） | t = 4.99，df = 8，P = 0.0011 |
| R `t.test()` | Welch's t 检验（`var.equal = FALSE`） | t = 4.99，df = 5.39，P = 0.0034 |
| SAS `PROC TTEST` | 两行都输出：Pooled（= Student）与 Satterthwaite（= Welch） | 分别对应上面两行 |

## 原因

**默认是否假设方差齐性（两组总体方差相等）不同**（来源：ttest_student_vs_welch.md）：

- **Student's t 检验**：假设两组总体方差相等，用合并方差算标准误，df = n₁ + n₂ − 2。
- **Welch's t 检验**（不齐方差 t 检验）：不假设方差相等，标准误分别用两组方差算，并用 **Welch-Satterthwaite 方程**调整自由度（通常是非整数，见 [CON-degrees-of-freedom](../concepts/CON-degrees-of-freedom.md)）。

标准误和自由度的公式不同，P 值（以及可能的 t 值）就会不同。

SAS 里两种方法的叫法不同（来源：summary_p.md）：Student = **Pooled**（把两组方差合并估计，df = n₁ + n₂ − 2）；Welch = **Satterthwaite**（两组方差各算各的，再校正自由度，df 通常是小数且偏小）。PROC TTEST 的 T-Tests 表里看 **Method** 列区分。

### Satterthwaite 一定"更保守"吗？⚠ 存在分歧

- **说法 A**（summary_p.md）：Satterthwaite 的自由度偏小，"所以结果更保守"。
- **说法 B**（本卡"该用哪个"一节的补充，Claude 模拟复核）：自由度一定不大于 n₁ + n₂ − 2，但 SE 也换了算法，所以结论取决于哪组方差大：
  - **方差大的组人数少**（最危险的情况）：Pooled 低估 SE，偏向假阳性；Satterthwaite 更保守，且第一类错误率接近 α。
  - **方差大的组人数多**：Pooled 反而偏保守。Claude 模拟（每组 10 vs 40 人，SD 1 vs 2，H₀ 为真，20000 次）：Pooled 第一类错误率 0.006，Satterthwaite 0.050。这时 Satterthwaite 并不比 Pooled 保守，只是更**准确**。

两种说法在最常被提醒的情形（小组方差大）下一致；差别在于"更保守"是否普遍成立。

### 差异有多大？⚠ 存在分歧（程度上的）

- **说法 A**（ttest_student_vs_welch.md）：P 值（以及 t 统计量）会存在"**细微**差异"。
- **说法 B**（Claude 用 R 复现；summary_p.md 的小结与此一致："两组样本量相等时，两种方法的 t 值相同，只有自由度和 p 值不同"）：差异不一定细微，t 值也不一定变：
  - **两组人数相等时，两种方法的 t 值完全相同**（合并方差 SE 与 Welch SE 在 n₁ = n₂ 时代数上相等），只有 df 不同。上例 t 都是 4.99，P 值却差约 3 倍（0.0011 vs 0.0034），因为两组 SD 差别大（6.1 vs 2.6），Welch df 从 8 降到 5.39。
  - **两组人数不等时，t 值也会不同**。把 group2 加到 8 人（105, 110, 108, 112, 109, 107, 111, 106）：Student t = 6.35、df = 11、P = 0.00005；Welch t = 5.27、df = 4.82、P = 0.0037，差约 70 倍。

## 怎么让结果一致

显式指定参数，不要依赖默认值（来源：ttest_student_vs_welch.md）：

```python
# 方案 A（推荐）：Python 改用 Welch，与 R 默认一致
t_stat, p_value = stats.ttest_ind(group1, group2, equal_var=False)
```

```r
# 方案 B：R 改用 Student，与 Python 默认一致
result <- t.test(group1, group2, var.equal = TRUE)
```

SAS PROC TTEST 不需要改代码，但要**确认报告取的是 Pooled 行还是 Satterthwaite 行**。

## 该用哪个

材料的建议：多数统计学家更倾向**默认使用 Welch's t 检验**。两组样本量不等或方差不齐时，Student's t 检验容易带来较高的假阳性风险，Welch 更稳健。

上面 n 不等的例子正好说明这一点：方差大的组人数少时，Student 把 SE 低估，P 值小了约 70 倍。

**实践建议**（来源：summary_p.md）：默认用 Satterthwaite，**事先在 SAP 里写明**；不要靠方差齐性检验（SAS 的 Folded F）来选方法，小样本时这个检验几乎没有效能（原因与模拟见下一节）。

> 补充（Claude）：
> - "样本量不等 + 方差不齐"的方向有讲究：**方差大的组人数少**时 Student 偏向假阳性（如上例）；反过来方差大的组人数多时 Student 偏保守。两组人数相等时 Student 对方差不齐相当稳健。
> - 临床试验的主要分析通常不是简单 t 检验，而是 ANCOVA / MMRM，方法在 SAP 中预先指定；ANCOVA 本身假设组间残差方差相等。用哪种 t 检验、取 SAS 哪一行，以 SAP 为准。
> - 不建议先做方差齐性检验（如 F 检验、Levene 检验）再决定用 Student 还是 Welch，这种"两步法"会影响整体第一类错误率，直接用 Welch 更常见。详见下一节。
>
> 以上待 Li 核实。

## 为什么不建议"先检验方差齐性，再选 Student / Welch"

> 补充（Claude）：本节为 Claude 的解释与模拟，非 inbox 材料。待 Li 核实。

"两步法"指：先做方差齐性检验，显著就用 Welch，不显著就用 Student。它看似更稳妥，实际上第一类错误控制不住。

**模拟**（Claude，R 4.5.2）：H₀ 为真（两组均值相同），每种情形重复 20000 次，α = 0.05 下错误拒绝 H₀ 的比例，理想值 0.05。预检验用 F 检验（`var.test()`）。

| 每组人数 | 两组 SD | Student | Welch | 两步法 | F 检验检出方差不齐的比例 |
|---|---|---|---|---|---|
| 10 vs 40 | 2 vs 1 | **0.179** | 0.050 | **0.072** | 78% |
| 10 vs 40 | 1.5 vs 1 | **0.119** | 0.050 | **0.084** | 39% |
| 6 vs 24 | 2 vs 1 | **0.185** | 0.054 | **0.101** | 58% |
| 20 vs 20 | 1 vs 1 | 0.051 | 0.050 | 0.051 | — |
| 10 vs 40 | 1 vs 1 | 0.050 | 0.051 | 0.053 | — |

两步法比"一律用 Student"好一些，但始终不如直接用 Welch。原因有四：

1. **预检验的功效不够，最需要它的时候最容易漏掉。** 样本小、人数不等时 Student 最容易出问题，偏偏这时 F / Levene 检验的功效也最低。第二行 F 检验只检出 39% 的方差不齐，其余 61% 仍用了 Student，两步法错误率 0.084。
2. **"方差齐性检验不显著"不等于"方差相等"。** 和"不显著 ≠ 无效"是同一个道理（见 [CON-type-I-II-error](../concepts/CON-type-I-II-error.md#最重要的解读原则不显著--无效)）。两步法把"没检出来"当成"相等"。
3. **两步法改变了检验的性质。** 最终用哪个检验取决于数据在预检验中的表现，Student 和 Welch 各自的理论分布都没有考虑这层筛选，组合后的第一类错误率不再是 α。
4. **直接用 Welch 几乎没有代价。** 方差真的相等时（后两行），Welch 的错误率同样准确，只损失一点自由度，功效下降很小。

**临床试验语境**：分析方法须在 SAP 中事先指定（见 [CON-null-hypothesis](../concepts/CON-null-hypothesis.md)）。"看数据再选检验"是数据驱动的分析选择；即使 SAP 预先写明"若 Levene 检验显著则用 Welch"，规则是事先定的，但仍有上面 1–3 的统计问题。

模拟代码：

```r
set.seed(1)
sim <- function(n1, n2, s1, s2, R = 20000) {
  r <- replicate(R, {
    x <- rnorm(n1, 0, s1); y <- rnorm(n2, 0, s2)
    ps <- t.test(x, y, var.equal = TRUE)$p.value  # Student
    pw <- t.test(x, y)$p.value                    # Welch
    pf <- var.test(x, y)$p.value                  # F 检验（方差齐性）
    c(ps < .05, pw < .05, ifelse(pf < .05, pw, ps) < .05, pf < .05)
  })
  round(rowMeans(r), 3)  # Student, Welch, 两步法, F 检验拒绝率
}
sim(10, 40, 2, 1)
```

模拟用 F 检验而非 Levene 检验，结论方向应一致，具体数字会不同。

参考文献（Claude 凭记忆给出，**待核实**）：Zimmerman DW (2004), *British Journal of Mathematical and Statistical Psychology*；Rasch D, Kubinger KD, Moder K (2011), *Statistical Papers*。

## 相关卡片

- [GOT-skewed-small-sample](GOT-skewed-small-sample.md)：小样本偏态时 Welch 也救不了
- [CON-t-test-pvalue](../concepts/CON-t-test-pvalue.md)：t 检验流程与 SAS / R 代码
- [CON-p-value](../concepts/CON-p-value.md)：P 值计算四步与软件实现
- [CON-degrees-of-freedom](../concepts/CON-degrees-of-freedom.md)：非整数自由度
- [CON-distribution-family](../concepts/CON-distribution-family.md)：比较两组方差的 F 检验与 Levene 检验

## 出处

- Claude 对话（inbox: ttest_student_vs_welch.md；AI 生成，原始出处待补）
- Claude 对话（inbox: summary_p.md；AI 生成，原始出处待补）
- Claude 对话（inbox: calculate_p_value.md 示例数据；数值为 Claude 在 R 4.5.2 中复现）
- "为什么不建议两步法"一节：Claude 解释与 R 模拟（Li 提问后补充，2026-11-10）；文献待核实
