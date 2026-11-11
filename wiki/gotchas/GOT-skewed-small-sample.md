---
id: GOT-skewed-small-sample
title: "小样本偏态数据：Welch t 检验也救不了（Skewed Data in Small Samples）"
categories: [t-test, welch, skewness, outlier, log-transformation, geometric-mean, mann-whitney, hodges-lehmann, biomarker, normality, prespecification]
related: [CON-parametric-vs-nonparametric, GOT-ttest-student-vs-welch, CON-test-selection, CON-confidence-interval, CON-p-value, CON-dose-escalation-design]
sources: ["Claude 对话（inbox: skewed_example.md）"]
status: draft
updated: 2026-11-11
---

> 出处待补：本卡内容来自 Claude 对话（inbox: skewed_example.md），属 AI 生成内容，未引用原始文献。数据为模拟示例。Claude 已在 R 4.5.2 中逐项复核，有 5 处与材料不符，标"⚠ 待核实"（汇总见文末）。

## 要点

> 小样本 + 偏态时，问题不在于"方差不等"，而在于**均值本身不可靠**，所以 Welch 救不了。生物标志物优先用 **log 转换**，有 0 值或负值时用 **非参数检验**。

这也是 Li 裁定"**近似正态的前提下**，Welch t 检验是两组独立样本比较的合理默认选择"（见 [CON-test-selection](../concepts/CON-test-selection.md)）中"近似正态"这个前提的反例：Welch 解决的是方差不齐（[GOT-ttest-student-vs-welch](GOT-ttest-student-vs-welch.md)），解决不了偏态。

## 例子：小样本 II 期试验的 CRP 比较

抗炎药小样本探索性研究，试验药组和安慰剂组**各 10 例**，比较第 4 周血清 CRP（mg/L）。

| 组别 | 第 4 周 CRP（mg/L） |
|---|---|
| 试验药 | 3.2, 4.1, 4.8, 5.5, 6.0, 6.9, 7.4, 8.8, 10.5, 12.0 |
| 安慰剂 | 6.5, 8.2, 9.9, 11.4, 13.0, 15.6, 18.3, 22.7, 31.0, **96.0** |

安慰剂组一位受试者第 4 周合并感染，CRP 达到 96。这在 CRP 数据中很常见，**属于真实值，不是录入错误，不能随意删除**。

### 第一步：描述分布

| | 试验药 | 安慰剂 |
|---|---|---|
| 均值 ± SD | 6.9 ± 2.8 | 23.3 ± **26.6** |
| 中位数（IQR） | 6.5（5.0–8.5） | 14.3（10.3–21.6） |
| 偏度 | 0.51 | **2.31** |
| Shapiro-Wilk p | 0.77 | **< 0.001** |

明显偏态的信号：

- 安慰剂组 **SD 大于均值**：只能为正的变量出现这种情况，基本说明右偏。
- 均值（23.3）远大于中位数（14.3），被一个极端值拉高。
- 偏度 > 2，正态性检验显著（正态性检验的局限见 [CON-test-selection](../concepts/CON-test-selection.md#怎么判断近似正态)）。

### 第二步：比较三种分析方法

| 方法 | 结果 | p 值 |
|---|---|---|
| Welch t 检验（原始数据） | 均值差 −16.4 | **0.085** |
| Mann-Whitney U 检验 | 中位数 6.5 vs 14.3 | **0.004** |
| log 转换后 Welch t 检验 | 几何均数比 0.39（95% CI 0.21–0.71） | **0.004** |

> ⚠ 待核实（数值，Claude 用 R 复核）：
> - 均值差：23.26 − 6.92 = **−16.34**，应为 −16.3；材料的 −16.4 是用四舍五入后的均值相减所致。
> - Mann-Whitney p：R `wilcox.test()` 默认（小样本无结时用精确法）给出 **p = 0.0021**，不是 0.004；正态近似加连续性校正为 0.0036，约等于材料的 0.004。材料的代码注释说用的是精确 p 值，与表中数字不一致。HL 位置差估计 −7.65（95% CI −17.2 至 −2.6）。
> - 其余一致：Welch p = 0.085；log t 检验 p = 0.0044；几何均数比 0.388，CI 0.213–0.706。

### 为什么 Welch t 检验在这里不合适

- **一个极端值把安慰剂组的 SD 从约 8 放大到 26.6**（去掉 96 后 SD = 7.8），标准误变大，t 统计量变小，功效大幅下降。
- 每组只有 10 例，中心极限定理帮不上忙，均值的抽样分布本身也不接近正态。
- 均值 23.3 不能代表安慰剂组的典型水平：10 例中有 9 例都低于这个值。

两组的差别其实很明显（试验组 10 例中有 8 例低于安慰剂组的中位数），但 t 检验得出了"不显著"。

> ⚠ 待核实（计数，Claude 核对原始数据）：
> - 安慰剂组低于均值 23.3 的是 **8 例**（31.0 和 96.0 高于均值），不是 9 例。
> - 试验组最大值 12.0 < 安慰剂组中位数 14.3，所以是 **10 例全部**低于安慰剂中位数，不是 8 例。
>
> 两处更正都不改变结论，反而让"差别很明显"更突出。

## 两种合适的做法

### 1. log 转换后 t 检验（生物标志物首选）

- log(CRP) 两组的 Shapiro-Wilk p 分别为 0.99 和 0.30，转换后接近正态。
- 解读：试验药组 CRP 的**几何均数**是安慰剂组的 **39%**，即降低约 61%。
- 优点：给出效应量和置信区间（CI 读法见 [CON-confidence-interval](../concepts/CON-confidence-interval.md)；比值类看是否包含 1），也容易扩展到 ANCOVA（加入 log 基线值）。

### 2. Mann-Whitney U 检验

- 不依赖分布假设，对极端值稳健（原理见 [CON-parametric-vs-nonparametric](../concepts/CON-parametric-vs-nonparametric.md)）。
- 缺点：只给 p 值和中位数，效应量需另算（如 Hodges-Lehmann 估计）。
- 适合有 0 值或负值、无法取对数的数据（例如变化值）。

## R 代码

```r
crp <- data.frame(
  TRT  = rep(c("Drug", "Placebo"), each = 10),
  AVAL = c(3.2, 4.1, 4.8, 5.5, 6.0, 6.9, 7.4, 8.8, 10.5, 12.0,
           6.5, 8.2, 9.9, 11.4, 13.0, 15.6, 18.3, 22.7, 31.0, 96.0)
)

# 1. 看分布
tapply(crp$AVAL, crp$TRT, summary)
tapply(crp$AVAL, crp$TRT, shapiro.test)
par(mfrow = c(1, 2))
qqnorm(crp$AVAL[crp$TRT == "Placebo"]); qqline(crp$AVAL[crp$TRT == "Placebo"])

# 2. Welch t 检验（不推荐）
t.test(AVAL ~ TRT, data = crp)

# 3. log 转换后 t 检验
fit <- t.test(log(AVAL) ~ TRT, data = crp)
exp(diff(rev(fit$estimate)))   # 几何均数比 Drug/Placebo ≈ 0.39
exp(-rev(fit$conf.int))        # 材料原文；⚠ 见下方说明
exp(fit$conf.int)              # Claude 更正：95% CI ≈ 0.21–0.71

# 4. Mann-Whitney U（小样本无结时 R 默认给精确 p 值）
wilcox.test(AVAL ~ TRT, data = crp, conf.int = TRUE)  # 含 Hodges-Lehmann 估计
```

> ⚠ 待核实（代码，Claude 实际运行）：`t.test(log(AVAL) ~ TRT)` 的 `conf.int` 已经是 Drug − Placebo 方向（因子水平 Drug 在前），直接 `exp(fit$conf.int)` 就得到 0.21–0.71。材料的 `exp(-rev(fit$conf.int))` 实际输出 **1.42–4.68**，是 Placebo / Drug 的比值 CI，与注释不符。上面已保留原行并加了更正行。

> 补充（Claude）：SAS 中 log 转换分析可在 DATA 步取 `log(aval)` 后用 PROC TTEST，或直接用 `proc ttest dist=lognormal`，后者直接输出几何均数及其比值和 CI。非参数用 `PROC NPAR1WAY wilcoxon hl`（`exact wilcoxon;` 语句给精确 p 值）。待 Li 核实。

## 分析方法必须预先指定

这个例子里三种方法的 p 值从 0.085 到 0.004 不等，正好说明为什么分析方法要**在 SAP 中预先指定**：看完结果再挑最小的 p 值，就是典型的数据驱动选择，监管机构不会接受（另见 [GOT-ttest-student-vs-welch](GOT-ttest-student-vs-welch.md#为什么不建议先检验方差齐性再选-student--welch)）。

## 相关卡片

- [CON-parametric-vs-nonparametric](../concepts/CON-parametric-vs-nonparametric.md)：秩次为何对离群值稳健
- [GOT-ttest-student-vs-welch](GOT-ttest-student-vs-welch.md)：Welch 解决的是方差不齐
- [CON-test-selection](../concepts/CON-test-selection.md)：怎么判断近似正态
- [CON-confidence-interval](../concepts/CON-confidence-interval.md)：比值类 CI 看是否包含 1

## 出处

- Claude 对话（inbox: skewed_example.md；AI 生成，原始出处待补）

> 数值复核汇总（Claude，R 4.5.2）：均值 6.92 / 23.26，SD 2.82 / 26.60，中位数 6.45 / 14.3，IQR（R 默认 type 7）4.98–8.45 / 10.28–21.6，偏度 0.51 / 2.31，Shapiro-Wilk p 0.77 / 0.00008，log 后 0.99 / 0.30，去掉 96 后安慰剂 SD 7.81。**与材料不符 5 处**：均值差 −16.4（应 −16.3）、Mann-Whitney p 0.004（精确法 0.0021）、"9 例低于均值"（应 8 例）、"8 例低于安慰剂中位数"（应 10 例）、CI 代码 `exp(-rev(...))`（输出 1.42–4.68）。
