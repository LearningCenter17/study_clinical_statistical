---
id: CON-test-selection
title: "常用统计检验的选择与临床示例（Choosing a Statistical Test）"
categories: [inference, test-selection, t-test, anova, chi-square, fisher-exact, mann-whitney, wilcoxon, kruskal-wallis, nonparametric, normality]
related: [CON-p-value, CON-test-statistic, GOT-ttest-student-vs-welch, CON-t-test-pvalue, CON-distribution-family, CON-degrees-of-freedom, CON-MMRM, CON-type-I-II-error]
sources: ["Claude 对话（inbox: sample_test_statistic.md）", "Claude 对话（inbox: calculate_p_value.md）"]
status: draft
updated: 2026-11-10
---

> 出处待补：本卡内容来自 Claude 对话（inbox: sample_test_statistic.md；快速选择表的雏形来自 calculate_p_value.md），属 AI 生成内容，未引用原始文献。示例中的 P 值已由 Claude 在 R 4.5.2 中复核。临床例子均为示意数据。

## 快速选择表

| 数据类型 | 两组 | 多组（≥ 3） | 配对 / 重复测量 |
|---|---|---|---|
| 连续 · 正态 | t 检验（默认 Welch） | ANOVA | 配对 t 检验 / 重复测量 ANOVA / MMRM |
| 连续 · 非正态 / 等级 | Mann-Whitney U | Kruskal-Wallis | Wilcoxon 符号秩检验 / Friedman |
| 分类 · 大样本 | 卡方检验 | 卡方检验（R×C） | McNemar 检验 |
| 分类 · 小样本 | Fisher 确切检验 | Fisher（R×C） | 精确 McNemar |

**注册试验的检验方法应当在 SAP 中预先指定**，而不是看完数据后再挑选。

> 补充（Claude）：临床试验的主要分析通常不是上表中的简单检验，而是调整基线和分层因素的 ANCOVA / [MMRM](CON-MMRM.md)、分层的 CMH 检验等（第 3、4 章）；上表的方法多用于次要终点、安全性和探索性分析。待 Li 核实。

## 一、连续变量（近似正态）

### 1. 独立样本 t 检验

**适用**：两组独立样本，连续变量，近似正态。**近似正态的前提下，Welch t 检验是两组独立样本比较的合理默认选择**（不要求方差齐；R 默认就是 Welch）。

**例子**：降压药 II 期 RCT，试验药 vs 安慰剂，主要终点为第 12 周 SBP 相对基线变化。H₀：两组平均变化相同；结果示例：试验组 −12.3 mmHg，安慰剂组 −4.1 mmHg，p < 0.001。

```r
t.test(CHG ~ TRT01P, data = adbp_wk12, var.equal = FALSE)  # Welch
```

同一受试者前后比较（如基线和第 12 周）用**配对 t 检验**（`paired = TRUE`）。t 检验的原理见 [CON-t-test-pvalue](CON-t-test-pvalue.md)。

> 分歧记录（已由 Li 裁定，2026-11-10）：sample_test_statistic.md 原文写"方差齐；方差不齐时用 Welch t 检验"，把 Welch 当作方差不齐时的替代；[GOT-ttest-student-vs-welch](../gotchas/GOT-ttest-student-vs-welch.md) 的建议是默认用 Welch、不靠方差齐性检验来选。Li 的结论：**近似正态的前提下，Welch t 检验是两组独立样本比较的合理默认选择**。理由（模拟与原因）见 GOT-ttest-student-vs-welch。

### 2. 方差分析（ANOVA）

**适用**：三组及以上独立样本，连续变量，近似正态，方差齐。

**例子**：剂量探索研究，安慰剂、10 mg、20 mg、40 mg 四组，比较第 24 周 HbA1c 变化值。H₀：四组均值全部相等。整体 p < 0.05 只能说明"**至少有一组不同**"，需要做**事后多重比较**（如 Dunnett 检验，各剂量组分别对比安慰剂）。

```r
fit <- aov(CHG ~ TRT01P, data = adlb_hba1c)
summary(fit)
library(multcomp)
summary(glht(fit, linfct = mcp(TRT01P = "Dunnett")))  # 各剂量 vs 安慰剂
```

实际注册试验中更常用 **ANCOVA**（基线值作协变量）或 **MMRM**（重复测量），单因素 ANOVA 是它们的基础。ANOVA 的 F 检验原理见 [CON-distribution-family](CON-distribution-family.md#f-分布)；事后比较属于多重性问题（第 7 章待建）。

## 二、分类变量 / 计数数据

### 3. 卡方检验

**适用**：两个分类变量是否关联；样本量较大，**每个格子的期望频数 ≥ 5**。

**例子**：抗感染药物试验，比较临床治愈率。

| | 治愈 | 未治愈 | 合计 |
|---|---|---|---|
| 试验药 | 168 | 32 | 200 |
| 对照药 | 146 | 54 | 200 |

治愈率 84% vs 73%，卡方检验 p ≈ 0.007。

```r
tab <- matrix(c(168, 32, 146, 54), nrow = 2, byrow = TRUE)
chisq.test(tab, correct = FALSE)
```

有分层因素（如中心、疾病严重程度）时通常用 **CMH 检验**（`mantelhaen.test()`，第 4 章待建）。卡方统计量的原理见 [CON-test-statistic](CON-test-statistic.md)。

> 数值复核（Claude）：`correct = FALSE` 时 p = 0.0074；R 默认带 Yates 连续性校正，p = 0.0106。所以同一张表"R 默认结果"和材料不同，要看是否加了 `correct = FALSE`。SAS PROC FREQ 的 `chisq` 选项两种都输出（"Chi-Square" 与 "Continuity Adj. Chi-Square"）。

### 4. Fisher 确切概率法

**适用**：2×2（或 R×C）表，**样本量小或任一格子期望频数 < 5** 时代替卡方检验。

**例子**：罕见病研究中比较两组严重不良事件（SAE）。

| | 发生 SAE | 未发生 | 合计 |
|---|---|---|---|
| 试验组 | 5 | 15 | 20 |
| 安慰剂组 | 1 | 19 | 20 |

有格子期望频数 = 3 < 5，卡方检验不可靠，改用 Fisher，p ≈ 0.18。

```r
fisher.test(matrix(c(5, 15, 1, 19), nrow = 2, byrow = TRUE))
```

安全性 TLF 中，AE 按 SOC / PT 汇总的组间比较经常用 Fisher，因为很多 PT 的发生例数很少。

> 数值复核（Claude）：期望频数为 3 / 17 / 3 / 17，Fisher p = 0.182。若硬做卡方（不校正）p = 0.077，比 Fisher 小一半多，R 会给出 "Chi-squared approximation may be incorrect" 警告，说明小样本下卡方近似偏乐观。
>
> 补充（Claude）："期望频数 < 5"的经典判据（Cochran）通常表述为"超过 20% 的格子期望频数 < 5，或任一格子 < 1"时不宜用卡方；2×2 表常简化为"任一格子 < 5"。待 Li 核实。

## 三、非参数检验（不满足正态，或为等级 / 有序数据）

### 5. Mann-Whitney U 检验（Wilcoxon 秩和检验）

**适用**：两组独立样本；数据严重偏态、有离群值、样本量小，或为有序等级数据。比较的是**分布 / 中位数位置**。

**例子**：两种术后镇痛方案的**住院天数**（右偏：大多 3–5 天，少数并发症患者 20+ 天）。方案 A 中位数 4 天（IQR 3–6），方案 B 中位数 6 天（IQR 4–9），p = 0.02。报告时用**中位数和 IQR**，而不是均值 ± SD。

```r
wilcox.test(LOS ~ TRT, data = adhosp)
```

另一个常见场景：疼痛 VAS 评分、改良 Rankin 量表（mRS）等**有序评分**。

> 补充（Claude）：Mann-Whitney 严格检验的是"一组的值倾向于大于另一组"（P(X > Y) ≠ 0.5），只有当两组分布形状相同、仅位置平移时，才能解释为"中位数不同"。SAS 用 `PROC NPAR1WAY` 的 `wilcoxon` 选项；与位置差对应的点估计和 CI 是 Hodges-Lehmann 估计（`hl` 选项）。待 Li 核实。

### 6. Kruskal-Wallis 检验

**适用**：三组及以上独立样本的非参数比较，相当于 ANOVA 的非参数版本。

**例子**：比较轻度、中度、重度 COPD 患者的血清 IL-6 水平（生物标志物通常严重右偏）。整体 p < 0.05 时再做两两比较（如 **Dunn 检验**，并做 Bonferroni / Holm 校正）。

```r
kruskal.test(AVAL ~ SEVERITY, data = adbm_il6)
library(FSA)
dunnTest(AVAL ~ SEVERITY, data = adbm_il6, method = "holm")
```

## 怎么判断"近似正态"

- 不要只看 Shapiro-Wilk 的 p 值：**大样本时几乎总是显著**。
- 结合 Q-Q 图、直方图和偏度一起判断。
- 样本量较大时（每组 n > 30–50），t 检验对轻度偏态比较稳健。

> 补充（Claude）：反过来，小样本时 Shapiro-Wilk 功效很低，"不显著"也不能证明正态——这与 [GOT-ttest-student-vs-welch](../gotchas/GOT-ttest-student-vs-welch.md) 中"不要靠预检验选方法"是同一个逻辑：预检验在大样本时过于敏感，在小样本时又检不出来。

## 相关卡片

- [CON-p-value](CON-p-value.md)：P 值计算四步
- [CON-test-statistic](CON-test-statistic.md)：t、χ²、log-rank 统计量
- [GOT-ttest-student-vs-welch](../gotchas/GOT-ttest-student-vs-welch.md)：Student vs Welch
- [CON-distribution-family](CON-distribution-family.md)：ANOVA 的 F 检验
- [CON-MMRM](CON-MMRM.md)：重复测量

## 出处

- Claude 对话（inbox: sample_test_statistic.md；AI 生成，原始出处待补）
- Claude 对话（inbox: calculate_p_value.md；快速选择表雏形）
