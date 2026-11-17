---
id: CON-credible-interval
title: "置信区间 vs 贝叶斯可信区间（Confidence Interval vs Credible Interval）"
categories: [inference, credible-interval, bayesian, frequentist, confidence-interval, prior, posterior, beta-distribution, reporting]
related: [CON-confidence-interval, CON-response-rate, CON-dose-escalation-design, CON-distribution-family]
sources: ["Claude 对话（inbox: CI_1.md）", "Claude 对话（inbox: CI_bayesian.md）"]
status: draft
updated: 2026-11-17
---

> 出处待补：本卡内容来自 Claude 对话（inbox: CI_1.md、CI_bayesian.md），属 AI 生成内容，未引用原始文献。示例数值已由 Claude 在 R 4.5.2 中复核。
>
> 拆分记录（2026-11-17）：本卡内容原在 [CON-confidence-interval](CON-confidence-interval.md) 中，按"一个知识点一张卡"拆出，内容未改写。置信区间"95%"的含义（套圈比喻、为什么不能说"95% 的概率包含真实值"）仍在那张卡。

## 两派对"概率"的理解不同

"真实值有 95% 的概率落在这个区间里"描述的其实是**贝叶斯可信区间**（credible interval），不是置信区间。两派对"概率"的理解不同：

| | 频率学派（Frequentist） | 贝叶斯学派（Bayesian） |
|---|---|---|
| 真实值 μ 是什么 | **固定的**一个数，只是不知道 | 不确定的，**本身有一个概率分布** |
| 区间名称 | 置信区间（Confidence Interval） | 可信区间（Credible Interval） |
| 什么是随机的 | **区间**（每次试验算出来的都不同） | **参数**（对它的认识用概率描述） |
| 95% 的含义 | 重复很多次试验，约 95% 的区间会套住真实值 | 根据现有数据，真实值有 95% 的概率在这个区间里 |

## 可信区间怎么算

1. **先验**（prior）：试验前对参数的认识，比如根据历史数据认为应答率大约在 20% 到 40%。
2. **后验**（posterior）：结合试验数据更新对参数的认识。

可信区间直接取后验分布的中间 95%，所以可以说"真实值有 95% 的概率在这里面"。

## R 例子：同一份应答数据，两种区间

Drug 组 60 人中 27 人应答（同 [CON-response-rate](../methods/binary/CON-response-rate.md) 的例子）：

```r
x <- 27; n <- 60

# 频率学派：95% 置信区间（Clopper-Pearson）
binom.test(x, n)$conf.int

# 贝叶斯：95% 可信区间（均匀先验 Beta(1, 1)）
# 后验分布 = Beta(1 + 应答人数, 1 + 未应答人数)
qbeta(c(0.025, 0.975), 1 + x, 1 + n - x)
```

两个区间数值很接近，但**解释不同**：

- 置信区间：用这种方法反复做试验，95% 的区间会包含真实应答率。
- 可信区间：根据这些数据（加上"没有先验信息"的假设），真实应答率有 95% 的概率在这个范围里。

`qbeta()` 的用法和 `qnorm()`、`qt()` 一样，只是换成 **Beta 分布**。Beta 分布常用来描述一个比例的不确定性。

> 数值复核（Claude，R 4.5.2）：Clopper-Pearson 置信区间 (0.321, 0.584)；Beta(28, 34) 后验的 95% 可信区间 (0.331, 0.576)。材料说"大约都在 (0.32, 0.58) 附近"，大体一致，可信区间略窄。

## 在临床试验里

- **绝大多数注册试验**的主要分析用频率学派方法，TLF 报告**置信区间**，写 "95% CI"。
- **贝叶斯方法**用在特定场景：罕见病试验、儿科试验借用成人数据、适应性设计等（一期剂量递增中的应用见 [CON-dose-escalation-design](../design/CON-dose-escalation-design.md)）。这时报告**可信区间**，写 "95% CrI" 或 "95% credible interval"。

写 CSR 或解释结果时，**不要用"有 95% 的概率"描述置信区间**。规范写法是"95% CI 为 (5.9, 10.5)"，或"差值的 95% 置信区间不包含 0"。

> 更正记录（2026-11-16）：首次收录 CI_1.md 时，此处是 Claude 补充的一句"这是频率学派的解释……"。后续对话（CI_bayesian.md）确认并展开，已替换为本节。

## 相关卡片

- [CON-confidence-interval](CON-confidence-interval.md)：置信区间的含义与解读
- [CON-response-rate](../methods/binary/CON-response-rate.md)：27/60 应答率的例子
- [CON-dose-escalation-design](../design/CON-dose-escalation-design.md)：贝叶斯方法在一期剂量递增中的应用

## 出处

- Claude 对话（inbox: CI_1.md；AI 生成，原始出处待补）
- Claude 对话（inbox: CI_bayesian.md；AI 生成，原始出处待补）
