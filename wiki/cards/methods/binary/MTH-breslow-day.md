---
id: MTH-breslow-day
title: "Breslow-Day 检验：各层 OR 是否同质（Breslow-Day Test for Homogeneity of Odds Ratios）"
categories: [binary-endpoint, breslow-day, homogeneity, odds-ratio, cmh, stratification, interaction, tarone, sas, proc-freq]
related: [MTH-CMH, CON-odds-ratio, CON-chi-square-distribution, CON-degrees-of-freedom, CON-stratified-randomization, CON-type-I-II-error]
sources: ["Claude 对话（inbox: CMH_OR_all.md）"]
status: draft
updated: 2026-11-18
---

> 出处待补：本卡内容来自 Claude 对话（inbox: CMH_OR_all.md），属 AI 生成内容，未引用原始文献（如 Breslow & Day 1980、Tarone 1985、SAS PROC FREQ 文档）。算例数值已由 Claude 在 R 4.5.2 中按公式复核（DescTools 未安装，`BreslowDayTest()` 未实际运行）。

本卡展开 [MTH-CMH](MTH-CMH.md#一个前提各层效应方向一致) 里的这句话：

> CMH 默认各层的效应方向大致一致，也就是药物在每一层里都差不多有效。如果某一层药物有效、另一层反而有害，合并出来的数字就没什么意义了。

这段话有三层意思：**各层效应一致**是什么意思，**为什么不一致时合并会出问题**，以及 **Breslow-Day 检验怎么检查这一点**。

## 一、"各层效应一致"是什么意思

CMH 把各层的结果合并成**一个**结论（一个 p 值、一个合并 OR），这背后有一个隐含假设：

> 药物在每一层里的效果**本来就是一样的**，各层的 OR 只是因为随机误差而略有不同。

所以合并出来的那个 OR 可以理解成"药物的那个共同效果"。如果药物在各层的效果本身就不一样，就不存在"共同效果"这回事，合并出来的数字也就失去了明确含义。

**"OR 同质"**（homogeneity of odds ratios）就是指各层的 OR 是同一个真实值的估计，彼此只有随机误差上的差异。（OR 本身见 [CON-odds-ratio](CON-odds-ratio.md)。）

## 二、正例：各层一致，可以放心合并

[MTH-CMH](MTH-CMH.md#算例辛普森悖论) 的辛普森悖论算例：

| | 药物应答率 | 安慰剂应答率 | OR |
|---|---|---|---|
| 第 1 层（未用过生物制剂） | 80% | 70% | 1.71 |
| 第 2 层（用过生物制剂） | 40% | 30% | 1.56 |
| **MH 合并** | | | **1.63** |

两层的 OR 很接近，药物在两层都有效。合并成 1.63 能代表药物的整体效果，没问题。

## 三、反例：各层方向相反，合并结果误导人

假设另一种药，每层每组各 100 人：

| | 药物应答率 | 安慰剂应答率 | OR |
|---|---|---|---|
| 第 1 层 | 80% | 50% | **4.0**（药物明显更好） |
| 第 2 层 | 30% | 60% | **0.29**（药物明显更差） |

代入 CMH：

- 第 1 层：药物组实际应答 80 人，期望 65 人，**多 15**
- 第 2 层：药物组实际应答 30 人，期望 45 人，**少 15**
- 合计偏差 = +15 − 15 = **0**

$$\text{CMH} = 0,\quad p = 1.0$$

$$OR_{MH} = \frac{80 \times 50/200 + 30 \times 40/200}{20 \times 50/200 + 70 \times 60/200} = \frac{20 + 6}{5 + 21} = 1.0$$

CMH 给出的结论是"**药物完全无效**"，OR = 1。

但实际情况是：药物对第 1 层的人**非常有效**，对第 2 层的人**明显有害**。正负效应互相抵消，被 CMH 合并成了 0。这就是 CMH "**先相加再平方**"（见 [MTH-CMH](MTH-CMH.md#算例辛普森悖论) 第二步）的副作用：方向一致时证据会累积，方向相反时证据会互相抵消。

所以合并之前，要先检查各层的效应是否一致。

## 四、Breslow-Day 检验在做什么

**Breslow-Day 检验**（Breslow-Day test）的原假设是：

> H₀：所有层的真实 OR 都相等

它的思路和卡方检验一样，也是"**实际值 vs 期望值**"：

1. **假设各层的 OR 都等于合并 OR**（OR_MH）
2. 在每层边际合计不变的前提下，**倒推出每层 aₖ 应该是多少**，使这张表的 OR 正好等于 OR_MH
3. 比较每层**实际的 aₖ** 和**倒推出来的期望 aₖ** 差多少
4. 把各层的偏差标准化、平方、相加，得到统计量，服从自由度为 **K − 1**（层数减 1）的卡方分布

$$BD = \sum_k \frac{\left(a_k - E(a_k \mid OR_{MH})\right)^2}{\operatorname{Var}(a_k \mid OR_{MH})} \sim \chi^2(K - 1)$$

自由度为什么是 K − 1：K 个层的 OR 用一个共同 OR 来拟合，用掉了 1 个自由度。（自由度的一般规律见 [CON-degrees-of-freedom](../../inference/CON-degrees-of-freedom.md)。）

**代入反例：** OR_MH = 1，所以期望表就是"两组应答率相同"：第 1 层期望 a = 65，第 2 层期望 a = 45。实际分别是 80 和 30，各偏离 15。

$$BD \approx 15^2/11.4 + 15^2/12.4 \approx 19.8 + 18.2 \approx 38,\quad df = 1,\quad p < 0.001$$

结论：各层 OR **显著不同质**，不能简单合并。

**代入正例：** 两层 OR 分别是 1.71 和 1.56，都很接近合并 OR 1.63，实际值和期望值差得很少，BD 很小，p 值很大。结论：同质，可以合并。

> 数值复核（Claude，R 4.5.2，按公式求解期望 aₖ 后计算）：
>
> - 反例：`mantelhaen.test(tab, correct = FALSE)` 给出 CMH = 0、MH OR = 1；各层 OR 4.0 / 0.286；期望 a = 65 / 45，方差 11.375 / 12.375（即 1 / (1/a + 1/b + 1/c + 1/d) 在期望表上的值）；BD = 37.96，p = 7.2 × 10⁻¹⁰。与材料一致。
> - 正例：期望 a = 47.56 / 96.45，方差 8.24 / 10.22，BD = 0.043，p = 0.84（同 MTH-CMH 中的数值复核）。

## 五、结果怎么解读

| Breslow-Day 结果 | 含义 | 处理方式 |
|---|---|---|
| **不显著** | 没有证据表明各层效应不同 | CMH 合并结果可以正常解读 |
| **显著** | 各层效应存在差异，即**分层因素和治疗之间存在交互作用** | 分层报告各层的结果，深入分析原因，谨慎解读合并 OR |

还要分清两种"不一致"：

- **量的差异**（quantitative interaction）：各层都有效，只是效果大小不同，比如 OR 分别是 3.0 和 1.5。合并结果仍有一定参考意义。
- **质的差异**（qualitative interaction）：方向相反，比如上面的 4.0 和 0.29。这时合并结果会严重误导。

严格来说，Breslow-Day 检验的是"OR 是否相等"，不只是"方向是否一致"。量的差异也可能让它显著。

## 六、实际使用中的注意事项

**1. 检验效能往往很低**

层数少或样本量不大时，即使各层确实存在差异，Breslow-Day 也常常检测不出来。所以很多 SAP 会用 **α = 0.10** 甚至更宽松的标准来判断。p 值不显著**不等于**证明了各层同质。

> 补充（Claude）："不显著 ≠ 证明没有差异"的一般原则见 [CON-type-I-II-error](../../inference/CON-type-I-II-error.md#最重要的解读原则不显著--无效)。

**2. 一般不作为"门槛"**

Breslow-Day 显著，通常并不会因此推翻主分析，而是作为**补充信息**。SAP 里一般这样写：主分析仍用 CMH，同时报告 Breslow-Day 的 p 值；如果显著，再补充各层的 OR 或森林图。

**3. 多个分层因素时**

如果按"X 光 × 既往生物制剂"交叉分层，就有 2 × 2 = **4 层**，Breslow-Day 的自由度是 **3**。

**4. Tarone 校正**

原始的 Breslow-Day 统计量有一点小偏差，Tarone 提出了一个校正版本。SAS 里加 `BDT` 选项就会输出 Tarone 校正后的结果。

> 补充（Claude）：Tarone 校正从 BD 中减去 [Σ(aₖ − E(aₖ))]² / ΣVar(aₖ)。上面两个例子里这一项为 0 或接近 0（正例 BD 0.04280 → 0.04279），所以校正前后几乎一样；校正在各层合计偏差不为 0 时才明显。待 Li 核实。

## 七、SAS 和 R

```sas
proc freq data=adeff;
  tables priorbio*trt01p*avalc / cmh bdt;
run;
```

对于 2×2×K 的表，SAS 在输出 CMH 结果时会**自动给出** Breslow-Day 检验。加上 `bdt` 选项后，会额外输出 Tarone 校正的版本。

```r
# R 自带的 mantelhaen.test() 不包含 Breslow-Day，需要用 DescTools 包
library(DescTools)

tab <- array(c(80, 50, 20, 50,    # 第1层：药物应答, 安慰剂应答, 药物不应答, 安慰剂不应答
               30, 60, 70, 40),   # 第2层
             dim = c(2, 2, 2))

mantelhaen.test(tab, correct = FALSE)    # CMH ≈ 0, OR = 1
BreslowDayTest(tab)                      # Breslow-Day，p < 0.001
BreslowDayTest(tab, correct = TRUE)      # Tarone 校正版
```

> 补充（Claude）：R 端用 `correct = FALSE` 是为了和 SAS 的 CMH 对齐，见 [GOT-continuity-correction-r-vs-sas](GOT-continuity-correction-r-vs-sas.md)。SAS 的行列顺序（哪一行是药物、哪一列是应答）会影响 OR 方向，见 [CON-odds-ratio](CON-odds-ratio.md#七在临床试验-tlf-里) 的补充说明。

## 相关卡片

- [MTH-CMH](MTH-CMH.md)：CMH 检验与 MH 合并 OR
- [CON-odds-ratio](CON-odds-ratio.md)：OR 的定义与解读
- [CON-chi-square-distribution](../../inference/CON-chi-square-distribution.md)：χ²(K − 1) 的来历
- [CON-degrees-of-freedom](../../inference/CON-degrees-of-freedom.md)：自由度
- [CON-stratified-randomization](../../design/CON-stratified-randomization.md)：分层因素从哪来
- [CON-type-I-II-error](../../inference/CON-type-I-II-error.md)：不显著 ≠ 无差异

## 出处

- Claude 对话（inbox: CMH_OR_all.md；AI 生成，原始出处待补）
