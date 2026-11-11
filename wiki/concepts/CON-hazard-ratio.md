---
id: CON-hazard-ratio
title: "风险比（Hazard Ratio, HR）"
categories: [survival, hazard-ratio, cox, log-rank, null-hypothesis]
related: [CON-null-hypothesis, CON-p-value, GOT-ni-hypothesis-direction, CON-logrank-vs-cox, CON-sample-size-power, CON-confidence-interval, CON-confirmatory-methods-overview]
sources: ["Claude 对话（inbox: h0_hr.md）", "Claude 对话（inbox: logrank_vs_cox.md）"]
status: draft
updated: 2026-11-10
---

> 出处待补：本卡内容来自 Claude 对话（inbox: h0_hr.md），属 AI 生成内容，未引用原始文献。

## 一句话定义

**HR（hazard ratio，风险比）是两组风险之比**，用在生存分析（比较"多久发生某事件"）中：

$$
HR = \frac{\text{新药组的风险}}{\text{对照组的风险}}
$$

"风险"（hazard）可通俗理解为：**一个还没出事的人，在接下来这一刻出事的可能性**。"出事"指试验关注的事件，如死亡、心梗、肿瘤进展。

## HR 的三种情况

| HR | 含义 | 通俗说法 |
|---|---|---|
| **= 1** | 两组风险一样 | 药没作用 |
| **< 1** | 新药组风险更低 | 新药有保护作用 |
| **> 1** | 新药组风险更高 | 新药反而有害 |

所以生存分析中 **H₀ 写作 HR = 1**（"两组风险相同、新药没效果"），和连续变量里"均值差 = 0"是同一个意思。之所以是 1 而不是 0：两个相同的数相除得 1，相减才得 0。见 [CON-null-hypothesis](CON-null-hypothesis.md#不同终点的-h)。

## 例子：心血管试验（新药 vs 安慰剂，终点心梗）

- **HR = 0.7**：任何时刻，新药组发生心梗的风险只有安慰剂组的 70%，即**风险降低 30%**。
- **HR = 1.0**：两组风险一样。
- **HR = 1.5**：新药组风险是安慰剂组的 1.5 倍，**风险升高 50%**。

## 怎么读报告

> HR = 0.70（95% CI: 0.58–0.85），P < 0.001

- 点估计 0.70 → 风险降低约 30%；
- 95% CI **不包含 1** → 和"没效果"有显著差别，P 值很小；
- 如果 CI 跨过 1（如 0.85–1.10）→ 不能排除"没效果"，P 值会大于 0.05。

## 常见坑

HR = 0.7 **不等于**"新药组出事的人少 30%"。HR 比较的是**每一时刻的风险**，最终出事人数的比例还取决于随访时间长短等因素。不过日常交流中"风险降低 30%"的说法是可以接受的。

> 补充（Claude）："任何时刻风险都是 70%"隐含了**比例风险（proportional hazards）假设**——HR 不随时间变化。若该假设不成立，单一 HR 只是某种时间平均，解读需谨慎；PH 检查方法见 [CON-logrank-vs-cox](CON-logrank-vs-cox.md#临床试验中的常见做法)。

## 实现

SAS 中一般用 `PROC PHREG`（Cox 回归）估计 HR 及 95% CI，用 `PROC LIFETEST` 做 log-rank 检验给 P 值。两者的 H₀、分工和代码见 [CON-logrank-vs-cox](CON-logrank-vs-cox.md)。

> 更正记录：原始材料（h0_hr.md）称 PHREG 和 LIFETEST "检验的都是 HR 是否等于 1"。后续 Claude 对话（logrank_vs_cox.md）更正为：**PHREG 检验的是 HR = 1；log-rank 检验的是两组生存曲线相同，不估计 HR，只在比例风险假设下与 Cox 的 score 检验等价。**

## 相关卡片

- [CON-confidence-interval](CON-confidence-interval.md)：CI 与 P 值的对应关系
- [CON-null-hypothesis](CON-null-hypothesis.md)
- [CON-p-value](CON-p-value.md)：log-rank 统计量作为检验统计量的例子
- [CON-logrank-vs-cox](CON-logrank-vs-cox.md)：log-rank 与 Cox 的分工

## 出处

- Claude 对话（inbox: h0_hr.md；AI 生成，原始出处待补）
- Claude 对话（inbox: logrank_vs_cox.md；AI 生成，原始出处待补）
