---
id: CON-type-I-II-error
title: "第一类错误、第二类错误与检验效能（Type I / Type II Error and Power）"
categories: [inference, type-i-error, type-ii-error, alpha, beta, power, sample-size, multiplicity, hypothesis-testing]
related: [CON-null-hypothesis, CON-p-value, CON-t-test-pvalue, GOT-ni-hypothesis-direction, CON-test-statistic, CON-sample-size-power, GOT-ttest-student-vs-welch, CON-confidence-interval, CON-test-selection]
sources: ["Claude 对话（inbox: type_I_error.md）", "Claude 对话（inbox: type_II_error.md）"]
status: draft
updated: 2026-11-10
---

> 出处待补：本卡内容来自 Claude 对话（inbox: type_I_error.md、type_II_error.md），属 AI 生成内容，未引用原始文献。文中 R 结果已由 Claude 在 R 4.5.2 中实际运行复核（见文末）。

## 一句话定义

- **第一类错误（Type I error）**：H₀ 其实是真的，你却拒绝了它。临床里就是**药其实没效果，试验却显著，错误地宣布有效**。概率记作 **α**（显著性水平）。
- **第二类错误（Type II error）**：H₀ 其实是假的，你却没能拒绝它。临床里就是**药其实有效，试验却不显著，没能证明它有效**。概率记作 **β**；**1 − β 就是检验效能（power）**，即药真有效时试验能检测出来的概率。

H₀ 怎么写见 [CON-null-hypothesis](CON-null-hypothesis.md)。

## 四格表：法庭审判类比

H₀ 是"被告无罪"（无罪推定，对应"药无效"的默认立场）。

| | 真相：无罪（H₀ 真） | 真相：有罪（H₀ 假） |
|---|---|---|
| 判有罪（拒绝 H₀） | ❌ **第一类错误**：冤枉好人，概率 α | ✅ 正确，概率 = power（1 − β） |
| 判无罪（不拒绝 H₀） | ✅ 正确，概率 1 − α | ❌ **第二类错误**：放走坏人，概率 β |

| | 俗称 | 火灾报警器类比 |
|---|---|---|
| 第一类错误 | 假阳性，"没有却说有"；冤枉好人 / 虚惊一场 | 没着火，报警器响了（误报） |
| 第二类错误 | 假阴性，"有却没发现"；放走坏人 / 漏诊 | 着火了，报警器没响（漏报） |

**两者此消彼长**：门槛定得越严（α 越小），越不容易冤枉好人，但也越容易放走坏人。要同时降低两者，最直接的办法是**加大样本量**。

> 补充（Claude）：α 是"**H₀ 为真的前提下**拒绝 H₀ 的概率"，不是"一个显著结果是假阳性的概率"——后者还取决于有多少被测的药真的有效，不能直接等同于 α。P 值的定义见 [CON-p-value](CON-p-value.md)。待 Li 核实。

## 第一类错误（α）

### 为什么监管最在意它

后果是**一个无效的药被批准上市**：病人花钱、承担副作用却得不到疗效，还可能耽误有效治疗。这是公共健康风险，所以 FDA 等监管机构把**严格控制 α** 作为核心要求。

α 是**事先设定**的：定 α = 0.05，意思是接受最多 5% 的机会犯这种错（单侧检验常用 0.025）。

### 多重比较会让它膨胀

每做一次检验都有 5% 的机会假阳性。做很多次时：

- 做 1 次：犯错概率 5%
- 做 10 次独立检验：至少一次假阳性 ≈ 1 − 0.95¹⁰ ≈ **40%**

所以多个终点、多个剂量组、多次期中分析时，必须做**多重性校正**（Bonferroni、Hochberg、gatekeeping、α 消耗函数等），把**总体**第一类错误率（familywise error rate, FWER）控制在 0.05。这是大纲第 7 章（多重性）和第 8 章（成组序贯设计）要解决的问题（卡片待建）。

## 第二类错误（β）与 power

### 什么决定了 β

β 不像 α 那样直接"设定"，而是由以下因素共同决定：

| 因素 | 怎样变化会让 β 变小（power 变大） |
|---|---|
| **真实效应大小** | 效应越大越容易发现（降 20 比降 2 好检测） |
| **个体变异 SD** | 病人反应越一致，越容易发现 |
| **样本量 n** | 越大越好，这是唯一能直接控制的 |
| **α** | 放宽 α 会降低 β，但会增加第一类错误，一般不动 |

本质上，效应大、SD 小、n 大都是让"信号 / SE"变大，统计量更容易越过临界值（SE 与 n、SD 的关系见 [CON-t-test-pvalue](CON-t-test-pvalue.md#t-值是信噪比)）。

> 补充（Claude）："n 是唯一能直接控制的"是相对而言。设计上也能间接压低 SD 或 SE，例如协变量调整（ANCOVA 调整基线）、更精确的终点测量、更同质的入组人群、配对 / 交叉设计。待 Li 核实。

### 临床中的意义

1. **样本量计算的核心。** 试验设计时根据预期效应和 SD，算出达到 **80% 或 90% power**（即 β = 0.2 或 0.1）所需的样本量。SAP 里"以双侧 α = 0.05、90% power 检测出 X 的差异，需要每组 N 例"说的就是这个（怎么算见 [CON-sample-size-power](CON-sample-size-power.md)）。
2. **后果主要是"错失"。** 一个有效的药被放弃，病人失去一个治疗选择，药企损失巨额研发投入。所以 β 的容忍度（10%–20%）比 α（5%，单侧 2.5%）宽松。

### 最重要的解读原则：不显著 ≠ 无效

p > 0.05 只说明"证据不足"，不能说明"没有差异"。可能药确实没用，也可能只是**样本量太小、power 不足**。这时应该看置信区间：

- CI 很窄且紧贴 0 → 即使有效应也很小
- CI 很宽（比如 −2 到 +15）→ 数据根本不足以下结论

所以要证明"差不多"，需要专门设计**等效或非劣效试验**，不能拿一个不显著的优效试验来说事（非劣效的假设方向见 [GOT-ni-hypothesis-direction](../gotchas/GOT-ni-hypothesis-direction.md)）。

## 用 R 看一下

**第一类错误率**：两组真的没差别，重复做 10000 次 t 检验。

```r
set.seed(1)
p <- replicate(10000, t.test(rnorm(50), rnorm(50))$p.value)
mean(p < 0.05)   # ≈ 0.05，这就是第一类错误率
```

**power 随样本量变化**：药物真实效应 = 0.5 个 SD。

```r
set.seed(1)
power_at <- function(n) mean(replicate(5000,
  t.test(rnorm(n, 0.5), rnorm(n, 0))$p.value < 0.05))

sapply(c(20, 50, 86), power_at)
# ≈ 0.34  0.70  0.90   → n 越大，β 越小

power.t.test(delta = 0.5, sd = 1, power = 0.9)  # 理论计算：每组约 86 人
```

每组 20 人时，即便药真的有效，也有约 2/3 的概率得到"不显著"，这就是第二类错误。

> 运行复核（Claude，R 4.5.2）：第一段输出 0.0504；1 − 0.95¹⁰ = 0.401。第二段模拟输出 0.323 / 0.695 / 0.904，`power.t.test()` 理论值 0.338 / 0.697 / 0.903；90% power 所需 n = 85.03，向上取整为每组 86 人（80% power 时为 63.8 → 64 人）。模拟值随随机种子略有波动，与材料一致。

> 补充（Claude）：SAS 中对应的样本量 / power 计算是 `PROC POWER`，示例见 [CON-sample-size-power](CON-sample-size-power.md)。待 Li 核实。

## 记住两句话

- **第一类错误**："药没用，你却说它有用"，α 是你允许它发生的概率上限。
- **第二类错误**："药有用，你却没发现"，β 是它的概率，1 − β 是 power，主要靠足够的样本量来控制。

## 相关卡片

- [CON-confidence-interval](CON-confidence-interval.md)：CI 与 P 值的对应关系
- [CON-sample-size-power](CON-sample-size-power.md)：power 与样本量怎么算
- [CON-null-hypothesis](CON-null-hypothesis.md)：α、单侧 / 双侧须事先写进 H₀ 设定
- [CON-p-value](CON-p-value.md)：P 值与 α 的比较
- [CON-t-test-pvalue](CON-t-test-pvalue.md)：信号 / SE 与 power 的关系
- [GOT-ni-hypothesis-direction](../gotchas/GOT-ni-hypothesis-direction.md)：证明"差不多"要用非劣效设计

## 出处

- Claude 对话（inbox: type_I_error.md；AI 生成，原始出处待补）
- Claude 对话（inbox: type_II_error.md；AI 生成，原始出处待补）
