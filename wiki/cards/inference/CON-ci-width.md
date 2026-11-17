---
id: CON-ci-width
title: "置信区间的宽度由什么决定（What Determines CI Width）"
categories: [inference, confidence-interval, precision, standard-error, sample-size, event-count, survival, bias]
related: [CON-confidence-interval, CON-covariate, CON-hazard-ratio, CON-logrank-vs-cox, WF-sample-size-calc, CON-unequal-allocation, CON-missing-data, CON-sample-size-power]
sources: ["Claude 对话（inbox: CI_1.md）", "Claude 对话（inbox: CI_width.md）"]
status: draft
updated: 2026-11-17
---

> 出处待补：本卡内容来自 Claude 对话（inbox: CI_1.md、CI_width.md），属 AI 生成内容，未引用原始文献。示例数值已由 Claude 在 R 4.5.2 中复核。
>
> 拆分记录（2026-11-17）：本卡内容原在 [CON-confidence-interval](CON-confidence-interval.md) 中，按"一个知识点一张卡"拆出，内容未改写。CI 的含义、与 P 值的对应仍在那张卡。

## 影响 CI 宽度的因素

不只是样本量（来源：CI_width.md）：

| 因素 | 影响 |
|---|---|
| **数据的变异**（SD） | SD 越大，CI 越宽 |
| **样本量 n** | n 越大，CI 越窄（按 1/√n 缩小） |
| **置信水平** | 99% 比 95% 宽 |
| **分析方法** | 如 ANCOVA 调整基线后残差变异变小，CI 更窄（见 [CON-covariate](../methods/continuous/CON-covariate.md)） |
| **比例本身的大小**（率类终点） | p 接近 50% 时 CI 最宽，接近 0 或 1 时更窄 |
| **事件数**（生存终点） | **起决定作用的是事件数，不是入组人数** |

所以 CI 窄，可能是因为样本量大，也可能是数据本身变异小，**不能直接推出"样本量够了"**。

> 更正记录（2026-11-16）：CI_1.md 原文写"窄说明样本量充足，宽说明不确定性大"。后续对话（CI_width.md）确认这把宽度只归因于样本量，说法不完整，已改为本节。

## 生存终点：看事件数

1:1 随机时，Cox 模型中 log(HR) 的标准误约为：

$$
SE(\log \widehat{HR}) \approx \frac{2}{\sqrt{D}}
$$

D 是两组**合计的事件数**。公式里没有入组人数 n，只有 D。删失的病人只贡献"到某时间点还没发生事件"这一点信息，决定 HR 估计精度的是观察到了多少个事件。

```r
hr_ci <- function(hr, D) {
  se <- 2 / sqrt(D)
  round(exp(log(hr) + c(-1, 1) * qnorm(0.975) * se), 2)
}

hr_ci(0.70, D = 30)     # (0.34, 1.43)  很宽，含 1
hr_ci(0.70, D = 100)    # (0.47, 1.04)  仍含 1
hr_ci(0.70, D = 300)    # (0.56, 0.88)  不含 1
```

| | 试验 A | 试验 B |
|---|---|---|
| 入组人数 | 1000 | 300 |
| 事件数 | 30（随访短、事件少） | 150 |
| HR 的 CI | **宽** | **窄** |

试验 A 人多，CI 反而更宽。所以肿瘤试验 SAP 里期中分析和最终分析都按**事件数**触发（如"观察到 200 个 PFS 事件时进行最终分析"），而不是按入组人数或日历时间。同样的道理在样本量计算里的体现见 [WF-sample-size-calc](../design/WF-sample-size-calc.md#各终点的公式两组11-分配)（power 取决于事件数、Schoenfeld 公式）。

> 数值复核（Claude，R 4.5.2）：上面三个 `hr_ci()` 结果与材料一致。若 HR 同为 0.70，试验 A（D = 30）为 (0.34, 1.43)，试验 B（D = 150）为 (0.51, 0.96)。
>
> 补充（Claude）：2/√D 来自 1:1 随机时 Var(log HR) ≈ 4/D 的近似（与 Schoenfeld 公式同源）。分配比例为 r:1 时，系数变为 (1 + r)/√(r·D)（不等分配见 [CON-unequal-allocation](../design/CON-unequal-allocation.md)）。待 Li 核实。

## 窄 CI 不等于结论可靠

CI 只反映**随机误差**，不反映**系统偏倚**：

- 数据有偏倚（大量缺失、揭盲、人群选择有问题）时，CI 可以很窄，但中心位置是偏的。缺失数据见 [CON-missing-data](../missing-data/CON-missing-data.md)。
- CI 窄也不代表效果有**临床意义**。样本量很大时，很小的差值也可能得到一个很窄、不含 0 的 CI：统计上显著，临床上未必重要（MCID 见 [CON-sample-size-power](../design/CON-sample-size-power.md)）。

解读 CI 要分开看：**中心位置**说明效应多大，**宽度**说明估计多精确，再结合研究设计和数据质量判断结论是否可信。

## 相关卡片

- [CON-confidence-interval](CON-confidence-interval.md)：CI 的含义与解读
- [CON-hazard-ratio](../methods/tte/CON-hazard-ratio.md)：HR 的 CI
- [WF-sample-size-calc](../design/WF-sample-size-calc.md)：Schoenfeld 事件数公式
- [CON-covariate](../methods/continuous/CON-covariate.md)：协变量调整使 CI 变窄

## 出处

- Claude 对话（inbox: CI_1.md；AI 生成，原始出处待补）
- Claude 对话（inbox: CI_width.md；AI 生成，原始出处待补）
