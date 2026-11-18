---
id: MTH-t-test
title: "t 检验：从 t 值到 P 值（t-test）"
categories: [inference, p-value, t-test, hypothesis-testing, degrees-of-freedom, standard-error]
related: [MTH-MMRM, CON-p-value, CON-null-hypothesis, CON-test-statistic, CON-t-distribution, CON-degrees-of-freedom, CON-type-I-II-error, CON-sample-size-power, GOT-ttest-student-vs-welch, CON-confidence-interval, CON-test-selection, CON-parametric-vs-nonparametric, CON-confirmatory-methods-overview, CON-normal-distribution, WF-sample-size-calc, MTH-ci-construction, CODE-ttest-sas-r-python, CON-distribution-family]
sources: ["Claude 对话（inbox: PValue_ttest.md）", "Claude 对话（inbox: t_test_mean.md）", "Claude 对话（inbox: t_example_correction.md）", "Claude 对话（inbox: t_conception.md）", "Claude 对话（inbox: pvalue_tvalue.md）"]
status: draft
updated: 2026-11-18
---

> 出处待补：本卡内容来自 Claude 对话（inbox: PValue_ttest.md、t_test_mean.md、t_example_correction.md、t_conception.md、pvalue_tvalue.md），属 AI 生成内容，未引用原始文献。文中表格的数值已由 Claude 按 t 分布复核（见文末）。

## 一句话定义

**t 检验是"做法"，P 值是这个做法最后给出的"答案"。** t 检验先把数据变成统计量 t，再通过 t 分布把 t 换成概率 P。

## 三个东西别混了

（来源：t_conception.md）**t 检验是一套流程，t 分布是这套流程里用来查 P 值的那把"尺子"。**

| 名称 | 英文 | 是什么 |
|---|---|---|
| t 检验 | t-test | 一种假设检验**方法**（整个流程） |
| t 值 | t statistic | 用你的数据算出来的**一个数** |
| t 分布 | t distribution | 一条**概率分布曲线**，H₀ 成立时 t 值应该长什么样 → 见 [CON-t-distribution](../../inference/CON-t-distribution.md) |

t 检验之所以叫 t 检验，正是因为它的检验统计量在 H₀ 下服从 t 分布。同理，χ² 检验用 χ² 分布，F 检验（ANOVA）用 F 分布（见 [CON-test-statistic](../../inference/CON-test-statistic.md)）。

## 流程

```
原始数据
   ↓  第一步：算 t 值
t 值（差异是"抖动幅度"的几倍）
   ↓  第二步：查 t 分布
P 值（药没用时，出现这么大 t 值的概率）
   ↓
和 0.05 比较，下结论
```

1. **把数据变成一个数字 t**：t = 差值 ÷ 标准误。
2. **把 t 翻译成概率 P**：去 t 分布里查，看这么大的 t 有多罕见。

展开成五步（来源：t_conception.md）：

1. **立假设**：H₀ 两组均值相等
2. **算 t 值**：均值差 / 标准误，如 t = 2.8
3. **找对应的 t 分布**：根据自由度（如 df = 38）确定用哪一条 t 分布曲线
4. **查位置换成 P**：看 2.8 在这条曲线上落在哪里，算出比 ±2.8 更极端的尾部面积，如 P = 0.008
5. **下结论**：P < 0.05，拒绝 H₀

第 3、4 步就是 t 分布出场的地方。

**打个比方**：t 值是**你考的分数**（如 85 分），t 分布是**全年级的成绩分布图**，P 值是**你排在前百分之几**。光知道 85 分没法判断好坏，放到成绩分布里一看是前 1%，才知道很突出。因为自由度不同，t 分布有很多条（不同年级的成绩分布不一样），所以第 3 步要先按自由度选对曲线。

## t 值是信噪比

（来源：t_test_mean.md）**t 值 = 差异是"噪音"的多少倍**，更准确地说：观察到的差异相当于几个标准误。这是所有检验统计量共同骨架在 t 检验里的样子（骨架见 [CON-test-statistic](../../inference/CON-test-statistic.md#一句话定义)）。两组比较时：

> t =（两组均值差）/ 均值差的标准误

- **分子：信号**。观察到的效果有多大，如新药组血压比安慰剂组多降 6 mmHg。
- **分母：噪音**。标准误（standard error），衡量"单靠随机抽样，这个均值差通常会晃动多少"。由数据的离散程度和样本量决定：个体差异越大，噪音越大；样本越多，噪音越小。

同样是均值差 6 mmHg，把样本量和个体差异两个因素分开、各变一个（来源：t_example_correction.md）：

| 情况 | 每组 n | SD | SE = SD·√(2/n) | t = 6 / SE |
|---|---|---|---|---|
| 基准 | 200 | 15 | 1.5 | 4.0 |
| 只减少样本量 | 15 | 15 | 5.5 | 1.1 |
| 只增大个体差异 | 200 | 50 | 5.0 | 1.2 |

后两行 t 值差不多，但原因不同：一个是人太少，一个是人与人之间差异太大。两者都让标准误变大、t 值变小，同样 6 mmHg 的均值差就不显著了。**差异大小一样，结论完全不同**——不能只看均值差，必须除以标准误。

**SE 对 SD 是线性的，对 n 是平方根关系**：SD 翻倍，SE 就翻倍；要让 SE 减半，样本量得翻四倍。

（数值已由 Claude 复核：15·√(2/15) ≈ 5.48，50·√(2/200) = 5.0。）

> 更正记录：t_test_mean.md 原例为"每组 200 人、数据集中，SE 1.5"对比"每组 15 人、数据很分散，SE 5.0"。按 SE 反推两行 SD 约为 15 和 13.7，"数据很分散"与数值不符，SE 变大几乎完全来自样本量。已按 t_example_correction.md 替换为上表。

## 怎么读 t 值

| t 值 | 含义 |
|---|---|
| t ≈ 0 | 两组几乎没差别 |
| \|t\| 在 1 左右 | 差异在正常随机波动范围内 |
| \|t\| ≈ 2 以上 | 差异超出常见波动；样本量不太小时大致对应 p < 0.05（正态分布的 1.96） |
| \|t\| 很大（如 5、10） | 差异远远超出随机波动 |

**正负号**只表示方向，哪组更大取决于谁减谁。

## 为什么叫 t 不叫 z

总体标准差未知、只能用样本标准差估计，所以这个比值服从 t 分布而不是标准正态。详见 [CON-t-distribution](../../inference/CON-t-distribution.md#t-与-z-的区别)。

> 整理记录（2026-11-17）：本节原文（来源：t_test_mean.md，含 Gosset 的来历）已移到 CON-t-distribution，作为 t 与 z 关系的唯一出处。

P 值不是 t 检验独有的：卡方检验、log-rank 检验最后也都输出 P 值，只是中间算的统计量和查的分布不一样。P 值的一般定义和计算条件见 [CON-p-value](../../inference/CON-p-value.md)，H₀ 的写法见 [CON-null-hypothesis](../../inference/CON-null-hypothesis.md)。

## 例子：降压药

- 两组差 6，标准误 1.63（每组 3 人；原始数据在之前的对话中，未随材料收录）
- **t = 6 ÷ 1.63 ≈ 3.67**：差异约为正常抖动的 3.7 倍
- 查自由度 4 的 t 分布：药没用时 |t| ≥ 3.67 的概率约 **0.02**，即 P 值

## t 值与 P 值的对应

### 规律 1：t 越大，P 越小

自由度 4（每组 3 人）：

| t 值 | 含义 | 双侧 P 值 |
|---|---|---|
| 1 | 差异 ≈ 1 倍抖动，很常见 | 0.37 |
| 2 | 差异 ≈ 2 倍抖动 | 0.12 |
| 2.78 | — | **0.05**（刚好卡线） |
| 3.67 | 上面的例子 | 0.02 |
| 4.60 | — | 0.01 |

### 规律 2：自由度（样本量）影响"翻译"

同样 t = 2，df = 4（每组 3 人）时双侧 P = 0.12，不显著；df → ∞ 时 P = 0.046，显著。样本少时 t 分布尾巴更厚，要求的证据更强。各 df 下的临界值和 P 值对照表见 [CON-t-distribution](../../inference/CON-t-distribution.md#数值临界值与同一个-t-的-p-值)。

df 怎么来：独立样本 t 检验约为 n₁ + n₂ − 2；Welch 检验的 df 另行计算，通常不是整数，见 [GOT-ttest-student-vs-welch](GOT-ttest-student-vs-welch.md)。

> 整理记录（2026-11-17）：本节原有两张表（来源：PValue_ttest.md 的 df = 4 与 ∞ 对比；pvalue_tvalue.md 的 df 梯度表）和关于尾巴厚度的解释已移到 CON-t-distribution，与 CON-degrees-of-freedom 的临界值表合并。

### 什么时候一一对应

（来源：pvalue_tvalue.md）**自由度和单侧 / 双侧都确定之后，t 值和 P 值一一对应**。两个条件缺一个，就不能直接对应：

- **自由度**：同一个 t，df 不同，P 不同（见规律 2）。
- **方向**：
  - 双侧检验的 P 只看 |t|，t = 2.0 与 t = −2.0 的 P 相同，所以严格说是 **|t|** 与 P 一一对应。
  - 单侧检验的 P 是双侧的一半（前提是效应方向与假设一致），如 df = 30、t = 2.0 时单侧 P ≈ 0.027。单侧 P 的条件和方向相反时的情况见 [CON-p-value](../../inference/CON-p-value.md)。

固定 df 和方向后，t 越大 P 越小，严格单调（即规律 1）。**P 值只是把 t 换算到"概率"尺度，本身不提供额外信息。**

所以报告时写成 **t(df) = 2.0，P = 0.055**，把 df 一起写出来，别人才能核对 P 值。

> 数值复核（Claude，R 4.5.2）：`pt(-2, 30)` = 0.0273（单侧）。各 df 下的双侧 P 值与临界值复核见 CON-t-distribution。

## 记住三句话

1. **t 值**：差异是噪声的几倍，衡量"信号有多强"。
2. **P 值**：药没用时，看到这么强的信号的概率，衡量"有多罕见"。
3. **t 检验**：先算 t，再通过 t 分布把它换成 P。

## 实现

SAS 输出里的 `t Value` 和 `Pr > |t|` 就是这一对：前者是第一步的结果，后者是第二步的结果。

现在软件一步到位，如 R 里 `t.test(x, y)` 直接给出 t 值、df、P 值。中间"查 t 分布"那一步就是 `pt()` 在做（来源：t_conception.md）：

```r
2 * pt(-abs(2.8), df = 38)   # 双侧 P 值 ≈ 0.008
```

过去没有电脑时，就是翻教科书后面的 t 分布表来查。

（数值已由 Claude 复核：df = 38 时双侧 0.01 / 0.005 临界值约 2.71 / 2.98，t = 2.8 的 P 落在两者之间，≈ 0.008。）

软件代码（同一组数据的 Python / R / SAS 写法、项目数据的写法、SAS PROC TTEST 输出的四张表与 ODS 抽取）见 [CODE-ttest-sas-r-python](CODE-ttest-sas-r-python.md)。

> 拆分记录（2026-11-17）：本节原有的三个小节（来源：calculate_p_value.md、summary_p.md）已拆到 CODE-ttest-sas-r-python，内容未改写。

## 相关卡片

- [CODE-ttest-sas-r-python](CODE-ttest-sas-r-python.md)：SAS / R / Python 代码与 PROC TTEST 输出
- [GOT-ttest-student-vs-welch](GOT-ttest-student-vs-welch.md)：Student vs Welch 默认设置不同导致 P 值对不上
- [CON-type-I-II-error](../../inference/CON-type-I-II-error.md)：α、β 与 power
- [MTH-MMRM](MTH-MMRM.md)：模型中的 t 检验与自由度方法
- [CON-p-value](../../inference/CON-p-value.md)：P 值的一般定义与计算条件
- [CON-null-hypothesis](../../inference/CON-null-hypothesis.md)

## 出处

- Claude 对话（inbox: PValue_ttest.md；AI 生成，原始出处待补）
- Claude 对话（inbox: t_test_mean.md；AI 生成，原始出处待补）
- Claude 对话（inbox: t_example_correction.md；AI 生成，原始出处待补）
- Claude 对话（inbox: t_conception.md；AI 生成，原始出处待补）
- Claude 对话（inbox: pvalue_tvalue.md；AI 生成，原始出处待补）

> 数值复核（Claude）：按 t 分布计算，df = 4 时 t = 1, 2, 3.67, 4.60 的双侧 P 值分别约为 0.374、0.116、0.021、0.010，临界值 t₀.₀₂₅,₄ = 2.776；df → ∞ 时 t = 2 的双侧 P ≈ 0.0455。与材料一致。
