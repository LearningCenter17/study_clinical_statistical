---
id: CON-p-value
title: "P 值的定义与计算条件（P-value）"
categories: [inference, p-value, hypothesis-testing, null-distribution, nonparametric, permutation-test, test-selection, software, effect-size]
related: [CON-null-hypothesis, CON-t-test-pvalue, CON-hazard-ratio, CON-MMRM, GOT-ni-hypothesis-direction, CON-logrank-vs-cox, CON-test-statistic, CON-t-distribution, CON-distribution-family, CON-type-I-II-error, CON-degrees-of-freedom, CON-sample-size-power, GOT-ttest-student-vs-welch, CON-confidence-interval, CON-test-selection]
sources: ["Claude 对话（inbox: p_value_requirement.md）", "Claude 对话（inbox: calculate_p_value.md）"]
status: draft
updated: 2026-11-10
---

> 出处待补：本卡内容来自 Claude 对话（inbox: p_value_requirement.md、calculate_p_value.md），属 AI 生成内容，未引用原始文献。

## 一句话定义

$$
P = P(T \text{ 至少和 } T_{obs} \text{ 一样极端} \mid H_0 \text{ 为真})
$$

**要算 P 值，必须知道"如果没有效果，结果通常长什么样"**（零分布）。零分布对了，P 值才有意义；零分布错了，P 值再小也是空中楼阁。

## 四个必备要素

| 要素 | 作用 | 例子 |
|---|---|---|
| 1. 明确的零假设 H₀ | P 值的全部计算都建立在"假设 H₀ 为真"上 | 两组均值相等、率差为 0、HR = 1 → 见 [CON-null-hypothesis](CON-null-hypothesis.md) |
| 2. 检验统计量 | 把数据压缩成一个数，衡量"偏离 H₀ 有多远" | t 值 = 均值差 / 标准误；χ² 值（观察频数与期望频数的差距）；log-rank 统计量（两条生存曲线的差异）→ 为什么需要不同统计量见 [CON-test-statistic](CON-test-statistic.md) |
| 3. H₀ 下统计量的分布（零分布） | **最关键**：拿实际统计量去对照，看落在分布的哪个位置 | H₀ 下 t 统计量服从 t 分布，χ² 统计量服从 χ² 分布 |
| 4. 备择假设的方向 | 决定"更极端"指哪一边 | 双侧：两个方向都算；单侧：只看一个方向 |

同一份数据，单侧 P 值通常是双侧的一半，所以方向必须**事先**定好、写进 SAP，不能看完数据再选。

> 补充（Claude）："单侧 = 双侧的一半"仅在零分布对称（如 t、正态）且观察效应落在单侧假设所指方向时成立；效应方向相反时，单侧 P 值接近 1 − 双侧 P/2。

t 检验是这套流程的一个具体实例 → [CON-t-test-pvalue](CON-t-test-pvalue.md)。

## 让零分布成立的前提假设

| 假设 | 含义 | 违反时的后果 |
|---|---|---|
| **随机性** | 随机抽样，或者随机分组 | P 值有概率意义的根本。没有随机化，组间差异可能来自混杂而不是偶然 |
| **独立性** | 观测之间互不影响 | 重复测量、整群数据当作独立样本处理，标准误被低估，P 值偏小 |
| **分布假设** | 如 t 检验要求近似正态 | 样本小时影响较大；样本大时中心极限定理会帮忙 |
| **其他模型假设** | 方差齐性、Cox 模型的比例风险等 | 模型设定错了，统计量的分布就不对 |

> 补充（Claude）：独立性一条正是重复测量数据要用 [MMRM](CON-MMRM.md) 等模型处理受试者内相关的原因。

## 分布假设靠不住时：从数据里构造零分布

- **非参数检验**：如 Wilcoxon、Mann-Whitney，基于秩，不要求正态。
- **置换检验（permutation test）**：H₀ 下组别标签可以互换，把标签随机打乱成千上万次，每次算一个统计量，得到经验零分布，再看实际值排在第几。非常直观，前提只是随机化本身。
- **精确检验**：如 Fisher 精确检验，在小样本、频数少的列联表中直接枚举所有可能的情况。

## 计算流程

```
定义 H₀ 和 H₁（含单/双侧）
        ↓
选检验统计量 → 用实际数据算出观测值 T_obs
        ↓
确定 H₀ 下 T 的分布（理论分布 或 置换/精确）
        ↓
P 值 = P(T 至少和 T_obs 一样极端 | H₀ 为真)
```

展开成四个基本步骤（来源：calculate_p_value.md）：

1. **设定假设**：H₀ 通常表示"无差异 / 无效应 / 无关联"（如两组药效没有区别）；备择假设 H₁（或 Hₐ）表示"有差异 / 有效应"。
2. **选择合适的统计检验方法**：根据数据类型、分布特征和样本量选择（见下表）。
3. **计算检验统计量**：把样本数据代入公式，算出 t、z、F 或 χ² 值。
4. **通过概率分布计算 P 值**：根据统计量及其自由度（[df](CON-degrees-of-freedom.md)），在对应的概率分布（标准正态、t、χ² 等，见 [CON-distribution-family](CON-distribution-family.md)）上算尾部面积；双侧检验算两侧尾部面积之和。

### 选哪种检验

按数据类型（连续正态 / 分类 / 非参数）和比较组数选：两组连续用 t 检验，多组用 ANOVA；分类用卡方，小样本用 Fisher；非参数用 Mann-Whitney U、Kruskal-Wallis。完整选择表、临床例子和代码见 [CON-test-selection](CON-test-selection.md)。

## 实现：软件里怎么算

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

> 补充（Claude）：**同一组数据，上面三段代码给出的 P 值并不相同**：Python 默认 Student t 检验（P = 0.0011），R 默认 Welch t 检验（P = 0.0034），SAS 两行都输出。原因与对齐方法见 [GOT-ttest-student-vs-welch](../gotchas/GOT-ttest-student-vs-welch.md)。

## 怎么解读

（来源：calculate_p_value.md）

- **P < 0.05**（通常标准）：拒绝 H₀，认为结果具有**统计学显著性**（observed difference is unlikely due to chance alone）。
- **P ≥ 0.05**：没有足够证据拒绝 H₀，差异可能由随机误差引起。这不等于证明了"没有差异"，见 [CON-type-I-II-error](CON-type-I-II-error.md#最重要的解读原则不显著--无效)。
- **P 值不代表效应量（effect size）的大小**，也不直接等同于临床上的实际意义；临床意义要看效应估计值和置信区间，并与 MCID 比较（见 [CON-sample-size-power](CON-sample-size-power.md#δ-的选择假设的治疗差值assumed-treatment-difference)）。

> 补充（Claude）：0.05 是事先设定的 α，比较规则必须在 SAP 中预先写明（见 [CON-null-hypothesis](CON-null-hypothesis.md)）。P 值的更多常见误解（如"P 值是 H₀ 为真的概率"）计划单独成卡，待建。

## 相关卡片

- [CON-test-selection](CON-test-selection.md)：选哪种检验、临床示例与代码
- [CON-confidence-interval](CON-confidence-interval.md)：CI 与 P 值的对应关系
- [CON-type-I-II-error](CON-type-I-II-error.md)：α、β 与 power
- [CON-null-hypothesis](CON-null-hypothesis.md)
- [CON-t-test-pvalue](CON-t-test-pvalue.md)
- [CON-hazard-ratio](CON-hazard-ratio.md)：log-rank / Cox 中的 H₀：HR = 1
- [CON-MMRM](CON-MMRM.md)

## 出处

- Claude 对话（inbox: p_value_requirement.md；AI 生成，原始出处待补）
- Claude 对话（inbox: calculate_p_value.md；AI 生成，原始出处待补）
