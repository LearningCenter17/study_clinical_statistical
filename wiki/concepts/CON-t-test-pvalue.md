---
id: CON-t-test-pvalue
title: "t 检验与 P 值（t-test and P-value）"
categories: [inference, p-value, t-test, hypothesis-testing, degrees-of-freedom, standard-error, z-test]
related: [CON-MMRM, CON-p-value, CON-null-hypothesis, CON-test-statistic, CON-t-distribution, CON-degrees-of-freedom, CON-type-I-II-error, CON-sample-size-power, GOT-ttest-student-vs-welch, CON-confidence-interval, CON-test-selection]
sources: ["Claude 对话（inbox: PValue_ttest.md）", "Claude 对话（inbox: t_test_mean.md）", "Claude 对话（inbox: t_example_correction.md）", "Claude 对话（inbox: t_conception.md）", "Claude 对话（inbox: summary_p.md）"]
status: draft
updated: 2026-11-10
---

> 出处待补：本卡内容来自 Claude 对话（inbox: PValue_ttest.md、t_test_mean.md、t_example_correction.md、t_conception.md、summary_p.md），属 AI 生成内容，未引用原始文献。文中表格的数值已由 Claude 按 t 分布复核（见文末）。

## 一句话定义

**t 检验是"做法"，P 值是这个做法最后给出的"答案"。** t 检验先把数据变成统计量 t，再通过 t 分布把 t 换成概率 P。

## 三个东西别混了

（来源：t_conception.md）**t 检验是一套流程，t 分布是这套流程里用来查 P 值的那把"尺子"。**

| 名称 | 英文 | 是什么 |
|---|---|---|
| t 检验 | t-test | 一种假设检验**方法**（整个流程） |
| t 值 | t statistic | 用你的数据算出来的**一个数** |
| t 分布 | t distribution | 一条**概率分布曲线**，H₀ 成立时 t 值应该长什么样 → 见 [CON-t-distribution](CON-t-distribution.md) |

t 检验之所以叫 t 检验，正是因为它的检验统计量在 H₀ 下服从 t 分布。同理，χ² 检验用 χ² 分布，F 检验（ANOVA）用 F 分布（见 [CON-test-statistic](CON-test-statistic.md)）。

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

（来源：t_test_mean.md）**t 值 = 差异是"噪音"的多少倍**，更准确地说：观察到的差异相当于几个标准误。两组比较时：

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

如果总体标准差已知，这个比值就是 z 值，服从标准正态分布。实际中总体标准差未知，只能用样本标准差估计，多引入一层不确定性（样本小时尤甚），所以它服从尾巴稍"胖"的 **t 分布**；自由度越大越接近正态（与下文"规律 2"一致）。名字来自 Student's t——Gosset 在健力士（Guinness）啤酒厂工作时提出。

P 值不是 t 检验独有的：卡方检验、log-rank 检验最后也都输出 P 值，只是中间算的统计量和查的分布不一样。P 值的一般定义和计算条件见 [CON-p-value](CON-p-value.md)，H₀ 的写法见 [CON-null-hypothesis](CON-null-hypothesis.md)。

## 例子：降压药

- 两组差 6，标准误 1.63（每组 3 人；原始数据在之前的对话中，未随材料收录）
- **t = 6 ÷ 1.63 ≈ 3.67**：差异约为正常抖动的 3.7 倍
- 查自由度 4 的 t 分布：药没用时 |t| ≥ 3.67 的概率约 **0.02**，即 P 值

## 规律 1：t 越大，P 越小

自由度 4（每组 3 人）：

| t 值 | 含义 | 双侧 P 值 |
|---|---|---|
| 1 | 差异 ≈ 1 倍抖动，很常见 | 0.37 |
| 2 | 差异 ≈ 2 倍抖动 | 0.12 |
| 2.78 | — | **0.05**（刚好卡线） |
| 3.67 | 上面的例子 | 0.02 |
| 4.60 | — | 0.01 |

## 规律 2：自由度（样本量）影响"翻译"

同样 t = 2：

| 每组人数 | 自由度 | t = 2 时的双侧 P 值 |
|---|---|---|
| 3 | 4 | 0.12（不显著） |
| 很多 | → ∞ | 0.046（显著） |

样本少时标准误本身估得不准，t 分布的"尾巴"更厚，要求的证据更强，P 值偏大。样本多了 t 分布趋近正态分布——所以"t 大于约 2 就显著"是**大样本下**的经验。t 分布形状随自由度的变化见 [CON-t-distribution](CON-t-distribution.md)。

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
> - SAS PROC TTEST 会同时输出 Pooled（等方差）和 Satterthwaite（不等方差，Welch）两行，自由度和 P 值不同；R 的 `t.test()` 默认是 Welch，Python `ttest_ind()` 默认是 Student。比对结果时先确认用的是哪一种，详见 [GOT-ttest-student-vs-welch](../gotchas/GOT-ttest-student-vs-welch.md)。
> - 同样的 `t Value` / `Pr > |t|` 也出现在 PROC MIXED 等模型的固定效应和 LS mean 差检验中，此时自由度由模型的自由度方法决定（如 [MMRM](CON-MMRM.md) 中的 Kenward-Roger）。

### SAS PROC TTEST 输出的四张表

（来源：summary_p.md）

| 表 | 内容 | 备注 |
|---|---|---|
| 1. Statistics | 各组 N、均值、SD、SE | |
| 2. Confidence Limits | 均值和均值差的 95% CI | CI 的读法见 [CON-confidence-interval](CON-confidence-interval.md) |
| 3. T-Tests | Pooled 和 Satterthwaite 各一行 | **最关键**；看 Method 列，取哪一行见 [GOT-ttest-student-vs-welch](../gotchas/GOT-ttest-student-vs-welch.md) |
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

- [GOT-ttest-student-vs-welch](../gotchas/GOT-ttest-student-vs-welch.md)：Student vs Welch 默认设置不同导致 P 值对不上
- [CON-type-I-II-error](CON-type-I-II-error.md)：α、β 与 power
- [CON-MMRM](CON-MMRM.md)：模型中的 t 检验与自由度方法
- [CON-p-value](CON-p-value.md)：P 值的一般定义与计算条件
- [CON-null-hypothesis](CON-null-hypothesis.md)

## 出处

- Claude 对话（inbox: PValue_ttest.md；AI 生成，原始出处待补）
- Claude 对话（inbox: t_test_mean.md；AI 生成，原始出处待补）
- Claude 对话（inbox: t_example_correction.md；AI 生成，原始出处待补）
- Claude 对话（inbox: t_conception.md；AI 生成，原始出处待补）
- Claude 对话（inbox: summary_p.md；AI 生成，原始出处待补）

> 数值复核（Claude）：按 t 分布计算，df = 4 时 t = 1, 2, 3.67, 4.60 的双侧 P 值分别约为 0.374、0.116、0.021、0.010，临界值 t₀.₀₂₅,₄ = 2.776；df → ∞ 时 t = 2 的双侧 P ≈ 0.0455。与材料一致。
