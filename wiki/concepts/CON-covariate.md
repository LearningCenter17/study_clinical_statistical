---
id: CON-covariate
title: "协变量与协变量调整（Covariate Adjustment）"
categories: [continuous, covariate, baseline, ancova, stratification-factor, power, prespecification]
related: [CON-MMRM, CON-test-selection, CON-type-I-II-error, CON-distribution-family, CON-parametric-vs-nonparametric, CON-sample-size-power, CON-confirmatory-methods-overview, CON-ordinal-data, CON-CMH, CON-proportional-odds-model]
sources: ["Claude 对话（inbox: covariate.md）"]
status: draft
updated: 2026-11-12
---

> 出处待补：本卡内容来自 Claude 对话（inbox: covariate.md），属 AI 生成内容，未引用原始文献。

## 一句话定义

**协变量（covariate）就是你不是主要研究它，但它会影响结果，所以分析时要把它的影响考虑进去的变量。**

## 降压药的例子

想知道药物（分组）对血压下降有没有效果。但**病人入组时的基线血压**也会影响下降幅度：基线 180 的人往往比基线 140 的人降得多，这跟吃什么药关系不大，起点高本身就有更大的下降空间。

| 角色 | 变量 |
|---|---|
| 要研究的因素 | 分组（安慰剂 / 低剂量 / 高剂量） |
| 协变量 | 基线血压 |
| 结果 | 血压下降值 |

**打个比方**：比较三个补习班的效果，看期末成绩。学生入学水平本来就不一样，直接比期末分数不公平，更合理的是"在入学成绩相同的前提下，哪个班的学生期末更高"。入学成绩就是协变量。

## 为什么要调整

1. **减少噪音，看得更清楚。** 同一组病人的下降值差别很大，其中一部分是基线不同造成的。扣掉基线的影响后，组内剩下的"纯噪音"变小，药效更容易显现，**统计功效更高**（功效与噪音的关系见 [CON-type-I-II-error](CON-type-I-II-error.md#什么决定了-β)、[CON-sample-size-power](CON-sample-size-power.md)）。
2. **校正组间不平衡。** 随机化后各组基线一般差不多，但不会完全一样。如果高剂量组碰巧基线偏高，它降得多可能有一部分是基线造成的。加入协变量相当于问："**如果大家起点一样，各组差多少？**"

## 和 ANCOVA 的关系

| 模型 | 公式 |
|---|---|
| ANOVA | 结果 ~ 分组 |
| ANCOVA | 结果 ~ 分组 + 协变量 |

在 R 里就是多加一项：

```r
fit <- lm(chg ~ trt + base, data = adsl)
```

> 补充（Claude）：`CHG`、`BASE` 是 BDS 结构变量，通常在疗效数据集（如 ADEFF、ADVS）里，而不是 ADSL；材料的 `data = adsl` 应理解为示意。SAS 对应写法如下，待 Li 核实：
>
> ```sas
> proc glm data=adeff;
>   class trt01pn;
>   model chg = trt01pn base / solution;
>   lsmeans trt01pn / diff cl;
> run;
> ```
>
> ANCOVA 给出的组间比较是 **LS mean 差**（调整协变量后的均值差），其 F 检验见 [CON-distribution-family](CON-distribution-family.md#f-分布)。MMRM 中的 `base` 和 `base*avisitn` 就是同一思路在重复测量上的扩展（见 [CON-MMRM](CON-MMRM.md)）。

## 临床试验里常见的协变量

- **基线值**：最常见，ADaM 里的 `BASE`。
- **分层因素**：如中心、地区、疾病严重程度，通常是随机化时用过的。
- 有时也会加年龄、性别等。

**协变量一般要在 SAP 里提前规定好**，不能看完数据再挑哪个让结果更显著，否则有操纵结果的嫌疑（同样的道理见 [GOT-ttest-student-vs-welch](../gotchas/GOT-ttest-student-vs-welch.md#为什么不建议先检验方差齐性再选-student--welch)、[GOT-skewed-small-sample](../gotchas/GOT-skewed-small-sample.md#分析方法必须预先指定)）。

> 补充（Claude）：
> - 协变量应是**随机化前**测得的变量。随机化后测得、可能受治疗影响的变量（如治疗期间的合并用药）不应作为协变量，否则会破坏随机化带来的可比性。
> - 调整了基线后，以 `CHG` 或 `AVAL` 为因变量，治疗效应估计相同。
> - 监管指南：EMA《Guideline on adjustment for baseline covariates in clinical trials》（2015）、FDA《Adjusting for Covariates in Randomized Clinical Trials for Drugs and Biological Products》（2023）。名称与年份凭记忆给出，待 Li 核实后可建 REF 卡片。
> - 非参数方法调整协变量较难，见 [CON-parametric-vs-nonparametric](CON-parametric-vs-nonparametric.md)。

## 相关卡片

- [CON-MMRM](CON-MMRM.md)：基线及分层因素作为固定效应
- [CON-test-selection](CON-test-selection.md)：ANOVA 与 ANCOVA
- [CON-type-I-II-error](CON-type-I-II-error.md)：协变量调整降低噪音、提高 power

## 出处

- Claude 对话（inbox: covariate.md；AI 生成，原始出处待补）
