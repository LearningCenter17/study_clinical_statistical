---
id: CON-confidence-interval
title: "置信区间（Confidence Interval）：含义、构成、解读及与 P 值的对应"
categories: [inference, confidence-interval, p-value, hypothesis-testing, effect-size, reporting, point-estimate, standard-error, coverage]
related: [MTH-ci-construction, CON-credible-interval, CON-ci-width, CON-p-value, CON-type-I-II-error, MTH-t-test, GOT-ttest-student-vs-welch, CON-hazard-ratio, GOT-ni-hypothesis-direction, CON-null-hypothesis, CON-parametric-vs-nonparametric, GOT-skewed-small-sample, CON-normal-distribution, CON-response-rate, CON-t-distribution, CON-degrees-of-freedom, CON-dose-escalation-design, CON-covariate, CON-sample-size-power, CON-missing-data, CON-logrank-vs-cox, WF-sample-size-calc, CON-unequal-allocation, CODE-ttest-sas-r-python]
sources: ["Claude 对话（inbox: summary_p.md）", "Claude 对话（inbox: CI_1.md）", "Claude 对话（inbox: CI_1_correction.md）", "Claude 对话（inbox: CI_bayesian.md）"]
status: draft
updated: 2026-11-17
---

> 出处待补：本卡内容来自 Claude 对话（inbox: summary_p.md、CI_1.md、CI_1_correction.md、CI_bayesian.md），属 AI 生成内容，未引用原始文献。示例数值已由 Claude 在 R 4.5.2 中复核。
>
> 拆分记录（2026-11-17）：本卡原先还包含 CI 的构造方法、贝叶斯可信区间和 CI 宽度，已按"一个知识点一张卡"拆出到下面三张卡，内容未改写：
>
> - [MTH-ci-construction](MTH-ci-construction.md)：1.96 还是 t 临界值、不同统计量的 CI 构造方法
> - [CON-credible-interval](CON-credible-interval.md)：置信区间 vs 贝叶斯可信区间
> - [CON-ci-width](CON-ci-width.md)：CI 宽度由什么决定、生存终点看事件数、窄 CI 不等于结论可靠

## 一句话定义

置信区间（CI）是用样本数据**估计一个未知总体参数**时给出的**可能范围**，同时说明这个范围有多可靠（来源：CI_1.md）。

**95% CI 和 α = 0.05 的双侧检验是同一把尺子的两种说法**。CI 比 P 值多告诉你两件事：差值**可能有多大**，以及估计得**有多精确**。

## 为什么需要 CI

临床试验只能抽一部分患者做样本。样本算出的结果（如"Drug 组平均下降 8.2 分"）只是对真实值的**点估计**，换一批患者重做会略有不同。只报一个数字，读者看不出它有多准。CI 在点估计之外加一个范围：

> 平均下降 **8.2 分（95% CI：5.9，10.5）**

## 三个组成部分

```
   估计值   ±   临界值   ×   标准误（SE）
     ↓            ↓              ↓
  样本均值     1.96（95%）    SD / √n
  (中心)       (置信水平)     (估计的精度)
```

- **估计值**：区间的中心。
- **SE**：数据越分散、样本越少，SE 越大，区间越宽。
- **置信水平**：95% 最常用。要求的把握越高（如 99%），区间越宽。

"估计值 ± 1.96 × SE"作为**理解 CI 的思路**没问题（中心 ± 临界值 × 标准误），但实际**计算**时，临界值和构造方法要看统计量的类型（来源：CI_1_correction.md），见 [MTH-ci-construction](MTH-ci-construction.md)。

## 95% 到底是什么意思

这一点最容易理解错。

- ❌ **错误理解**："真实值有 95% 的概率落在 (5.9, 10.5) 之间。"
- ✅ **正确理解**："用同样的方法重复做很多次试验，每次都算一个 CI，大约 **95% 的 CI 会套住真实值**。"

真实值是固定的，只是我们不知道；会变的是每次试验算出来的区间。可以拿**套圈**理解：

```
真实值 →            ●
试验 1         [────●────]        ✓ 套中
试验 2      [────────●─]          ✓
试验 3                 ●  [────]  ✗ 没套中
试验 4          [──────●──]       ✓
...
100 次里大约 95 次套中
```

这个"覆盖率"可以用模拟验证：设定真实值，重复抽样 1000 次、每次算 CI、数有几次套中，结果约 0.95。思路同 [CON-response-rate](../methods/binary/CON-response-rate.md#抛硬币类比与模拟) 中用 `rbinom` 模拟应答人数。

> 注：材料提到"前面那段模拟代码"，但代码本身不在材料里，未收录。

### 为什么不能说"这个区间有 95% 的概率包含真实值"

在频率学派看来，真实值 μ 是固定的。某一个**已经算出来**的区间，比如 (46.5, 51.3)，要么包含 μ（概率 1），要么不包含（概率 0），没有"95% 概率包含"这种中间状态。**95% 描述的是这套方法的可靠性，不是这一个区间**（来源：CI_bayesian.md）。

套圈比喻：你的套圈成功率是 95%。但圈已经扔出去、落地了，它要么套中、要么没套中，只是你还没看到结果。

"真实值有 95% 的概率落在这个区间里"描述的其实是**贝叶斯可信区间**，两者的区别和写 CSR 时的规范写法见 [CON-credible-interval](CON-credible-interval.md)。

## CI 与 P 值的对应

| CI 与"无差别值"的关系 | 等价于 | 含义 |
|---|---|---|
| **0 不在 CI 内** | p < 0.05 | "没差别"和数据不相容，结果显著 |
| **0 在 CI 内** | p ≥ 0.05 | "没差别"排除不了，结果不显著 |

"无差别值"对均值差、率差是 0；对 HR、OR 等比值是 1（见 [CON-hazard-ratio](../methods/tte/CON-hazard-ratio.md)）。

| 指标 | 无效值 | 举例 | 结论 |
|---|---|---|---|
| 差值（均值差、率差） | **0** | 差值 −5.2 (−8.1, −2.3) | 不含 0 → 显著 |
| 比值（HR、OR、RR） | **1** | HR 0.65 (0.42, 1.01) | 含 1 → 不显著 |

CI 能提供的信息比 P 值多：

- **效应有多大**：看中心位置。
- **估计得有多准**：看区间宽度。宽度由什么决定见 [CON-ci-width](CON-ci-width.md)。

> 补充（Claude）：这种等价要求 CI 和检验**出自同一方法**（同一 SE、同一自由度、同一分布）。例如 t 检验的 Welch CI 对应 Welch 检验、Pooled CI 对应 Pooled 检验；混用时（如 Wald CI 配 score 检验、Hodges-Lehmann CI 配 Wilcoxon 检验、Cox 的 Wald CI 配 log-rank P 值）边界附近可能出现"CI 不含 0 但 p 略大于 0.05"之类不一致。待 Li 核实。（Cox Wald CI 配 log-rank P 值这一例，后续对话 CI_HR.md 已确认"偶尔不一致是正常的"，见 [CON-logrank-vs-cox](../methods/tte/CON-logrank-vs-cox.md#临床试验中的常见做法)。）

## 不显著 ≠ 没差别

- 0 在 CI 里，只说明**不能排除**没差别，**不能证明**没差别。
- CI 窄而且围着 0 → 差别确实小；CI 宽 → 证据不够（样本量或事件数不足、变异大等，见 [CON-ci-width](CON-ci-width.md)）。
- 例（来源：CI_1.md）：HR 0.65 (0.42, 1.01)，p 约 0.054，算"不显著"。但从 CI 看，药物可能把风险降低多达 58%（1 − 0.42），也可能基本无效。这说明**证据不够**，不是证明药物无效。只看 P 值看不出这一点。

  > 数值复核（Claude，R 4.5.2）：按 log 尺度对称反推，SE(log HR) ≈ 0.224，z ≈ −1.92，双侧 p ≈ 0.054，与材料一致。
- 要证明"两组一样"，需用**等效性检验或非劣效检验**：看的是**整个 CI** 是否落在预设界值以内（方向与界值见 [GOT-ni-hypothesis-direction](../design/GOT-ni-hypothesis-direction.md)）。

与 power 的关系见 [CON-type-I-II-error](CON-type-I-II-error.md#最重要的解读原则不显著--无效)。

## 报告示例

用 [CODE-ttest-sas-r-python](../methods/continuous/CODE-ttest-sas-r-python.md#同一组数据python--r--sas) 中的示例数据（A 组 115, 120, 125, 130, 128；B 组 105, 110, 108, 112, 109）：

> A 组（123.6 ± 6.1）显著高于 B 组（108.8 ± 2.6），均值差为 14.8（95% CI: 7.3–22.3），Welch t 检验 t = 4.99，df = 5.39，p ≈ 0.003。

报告里点估计、CI、检验方法、统计量、df、P 值齐全，而且 CI 与检验用的是同一种方法（Welch）。

> 数值复核（Claude，R 4.5.2）：均值 123.6 / 108.8，SD 6.11 / 2.59；Welch 95% CI 7.34–22.26，p = 0.0034，与材料一致。若用 Pooled，CI 为 7.96–21.64、p = 0.0011（见 [GOT-ttest-student-vs-welch](../methods/continuous/GOT-ttest-student-vs-welch.md)）。
>
> 补充（Claude）："123.6 ± 6.1"中 ± 后是 SD；报告时应写明是 SD 还是 SE，常见写法为 "mean (SD)"。待 Li 核实。

## 一句话主线

**t 值、F 值、置信区间都是"观测到的差别 ÷ 随机误差"这个思路的变形**（t 见 [MTH-t-test](../methods/continuous/MTH-t-test.md#t-值是信噪比)，F 见 [CON-distribution-family](CON-distribution-family.md#f-分布)）。

> 补充（Claude）：严格说，CI 是这个比值"反过来用"：差值 ± 临界值 × SE。t 检验问"差值是 SE 的几倍"，CI 问"在临界值倍 SE 的范围内，真实差值可能落在哪"。均值差的 95% CI = 差值 ± t₀.₉₇₅,df × SE。

## 相关卡片

- [MTH-ci-construction](MTH-ci-construction.md)：各统计量的 CI 怎么构造
- [CON-credible-interval](CON-credible-interval.md)：贝叶斯可信区间
- [CON-ci-width](CON-ci-width.md)：CI 宽度由什么决定
- [CON-p-value](CON-p-value.md)：P 值的定义与解读
- [CON-type-I-II-error](CON-type-I-II-error.md)：不显著 ≠ 无效
- [MTH-t-test](../methods/continuous/MTH-t-test.md)：SAS PROC TTEST 的 Confidence Limits 表
- [GOT-ni-hypothesis-direction](../design/GOT-ni-hypothesis-direction.md)：非劣效用 CI 与 Δ 比较
- [CON-hazard-ratio](../methods/tte/CON-hazard-ratio.md)：比值类效应量的 CI 看是否跨 1
- [CON-response-rate](../methods/binary/CON-response-rate.md)：率的 CI 示例（ORR）

## 出处

- Claude 对话（inbox: summary_p.md；AI 生成，原始出处待补）
- Claude 对话（inbox: CI_1.md；AI 生成，原始出处待补）
- Claude 对话（inbox: CI_1_correction.md；AI 生成，原始出处待补）
- Claude 对话（inbox: CI_bayesian.md；AI 生成，原始出处待补）
