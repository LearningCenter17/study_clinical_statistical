---
id: CON-km-logrank-cox-example
title: "生存分析三件套串起来算：KM、log-rank、Cox 各答什么问题与 10 人算例（KM, Log-rank and Cox: A Worked Example）"
categories: [survival, kaplan-meier, log-rank, cox, hazard-ratio, worked-example, tlf, median-survival]
related: [CON-survival-analysis-overview, MTH-kaplan-meier, CON-logrank-vs-cox, CON-hazard-ratio, CON-censoring, CON-confidence-interval]
sources: ["Claude 对话（inbox: KM_log_rank_cox_1.md）", "Claude 对话（inbox: KM_log_rank_cox_2.md）"]
status: draft
updated: 2026-11-19
---

> 出处待补：本卡内容来自 Claude 对话（inbox: KM_log_rank_cox_1.md、KM_log_rank_cox_2.md），属 AI 生成内容，未引用原始文献。算例已由 Claude 在 R 4.5.2 中复核。三种方法各自的细节见 [MTH-kaplan-meier](MTH-kaplan-meier.md)、[CON-logrank-vs-cox](CON-logrank-vs-cox.md)、[CON-hazard-ratio](CON-hazard-ratio.md)；总体框架见 [CON-survival-analysis-overview](CON-survival-analysis-overview.md)。

## 一句话定义

KM、log-rank、Cox 是生存分析的"标准三件套"，分别回答三个不同的问题（来自 KM_log_rank_cox_1.md）：

| 方法 | 回答的问题 | 输出 | 类比普通数据 |
|---|---|---|---|
| **KM** | 每组的生存情况是什么样？ | 生存曲线、中位时间、某时间点生存率 | 均值、标准差（描述） |
| **Log-rank** | 两组曲线有没有差别？ | p 值 | t 检验（检验） |
| **Cox** | 差别有多大？ | 风险比 HR 及 95% CI | 回归（估计效应） |

所以 TLF 里一张生存分析表通常是：KM 中位时间 + log-rank p 值 + Cox HR，三个一起报告。

> 整理记录（2026-11-19）：材料 1 中"它们的共同基础：每个事件时刻的风险集"一节（KM 用它算通过率、log-rank 比较实际与预期、Cox 构造偏似然）与 [MTH-kaplan-meier](MTH-kaplan-meier.md#为什么这个数很重要) 第 3 点重复，未再写入；"Log-rank 的直觉"和"三者之间的数学关系"并入 CON-logrank-vs-cox；"KM 不需要任何假设、可用来直观检查 PH"并入 MTH-kaplan-meier；R 代码与 CON-survival-analysis-overview 第 6 节重复，未再写入。

## 10 人算例

> 以下来自 Claude 对话（inbox: KM_log_rank_cox_2.md），AI 生成，出处待补。

### 数据

两组各 5 人，时间单位为月，"+" 表示删失：

- **治疗组 A**：4, 7+, 10, 12+, 15+
- **对照组 B**：2, 4, 6, 8+, 9

直观上看，A 组只有 2 人发生事件，B 组有 4 人。

### 第一步：KM（描述）

**A 组：**

| 时间 | 风险集 | 事件 | 通过率 | S(t) |
|---|---|---|---|---|
| 4 | 5 | 1 | 4/5 | 0.80 |
| 7+ | — | 删失 | 1 | 0.80 |
| 10 | 3 | 1 | 2/3 | 0.53 |
| 12+, 15+ | — | 删失 | 1 | 0.53 |

曲线一直没降到 0.5，所以**中位时间：未达到（NR）**。

**B 组：**

| 时间 | 风险集 | 事件 | 通过率 | S(t) |
|---|---|---|---|---|
| 2 | 5 | 1 | 4/5 | 0.80 |
| 4 | 4 | 1 | 3/4 | 0.60 |
| 6 | 3 | 1 | 2/3 | 0.40 |
| 8+ | — | 删失 | 1 | 0.40 |
| 9 | 1 | 1 | 0/1 | 0 |

**中位时间：6 个月**（S(t) 第一次 ≤ 0.5）。

KM 只告诉我们：A 组曲线在上面，看起来更好。但这个差别是不是偶然的？要靠下一步。

### 第二步：Log-rank（检验）

把两组合在一起，在每个事件时刻问：**如果两组没差别，A 组"应该"有几个事件？**

预期值 = 该时刻总事件数 × A 组风险集人数 / 总风险集人数

| 时间 | A 风险集 | B 风险集 | 总事件 | A 实际 | A 预期 |
|---|---|---|---|---|---|
| 2 | 5 | 5 | 1 | 0 | 1 × 5/10 = 0.50 |
| 4 | 5 | 4 | 2 | 1 | 2 × 5/9 = 1.11 |
| 6 | 4 | 3 | 1 | 0 | 1 × 4/7 = 0.57 |
| 9 | 3 | 1 | 1 | 0 | 1 × 3/4 = 0.75 |
| 10 | 3 | 0 | 1 | 1 | 1 × 3/3 = 1.00 |
| **合计** | | | **6** | **2** | **3.93** |

A 组**实际 2 个，预期 3.93 个**，少了将近 2 个；相应地，B 组实际 4 个，预期只有 2.07 个。

把这个差距标准化后得到卡方统计量 **3.35，p = 0.067**。

结论：A 组看起来更好，但样本太小，按 0.05 的标准不显著。

### 第三步：Cox（估计效应大小）

Cox 模型给出 **HR = 0.17，95% CI 0.02–1.53**。

意思是：A 组在任何时刻的事件风险大约只有 B 组的 17%，点估计看起来效果很强；但置信区间很宽，而且包含 1，说明数据不足以确定真的有效。这和 log-rank 的结论一致。

（Cox 默认报告的 Wald 检验 p = 0.11，跟 log-rank 的 0.067 不完全相同。样本很小时两种检验会有差别，样本量大时会非常接近。）

### 三步放在一起看

| 问题 | 方法 | 本例结果 |
|---|---|---|
| 生存情况如何？ | KM | A 组中位 NR，B 组中位 6 个月 |
| 差别是偶然的吗？ | Log-rank | p = 0.067，不显著 |
| 差别有多大？ | Cox | HR 0.17（0.02–1.53） |

这差不多就是一张标准 TTE 汇总表的结构。实际试验每组可能有几百人，台阶更密、置信区间更窄，但计算逻辑和这个 10 人例子完全一样。

> 数值复核（Claude，R 4.5.2）：
>
> - `survfit`：A 组 S(t) = 0.800 / 0.533，中位 NA（即 NR）；B 组 S(t) = 0.8 / 0.6 / 0.4 / 0，中位 6。
> - `survdiff`：B 组 O = 4、E = 2.07，A 组 O = 2、E = 3.93；χ² = 3.35（1 df），p = 0.067。
> - `coxph`（默认 Efron，以 B 为参照）：β = −1.80，HR = 0.165（材料四舍五入为 0.17），95% CI 0.018–1.525，Wald p = 0.112；改用 Breslow 时 HR = 0.166、CI 0.018–1.534，结论不变。
> - 同一个 `summary(coxph)` 里的 score 检验为 3.20（Efron）/ 3.18（Breslow），与 `survdiff` 的 3.35 不完全相同，因为第 4 个月两组各有 1 人同时发生事件（结点）。这正是 [CON-logrank-vs-cox](CON-logrank-vs-cox.md#二者的关系) 说的"有结点时 score 检验与 log-rank 可能略有差别"。
>
> 补充（Claude）：p = 0.067 不显著、HR 的 CI 包含 1，两者结论一致；P 值与 CI 偶尔"打架"的原因见 [CON-logrank-vs-cox](CON-logrank-vs-cox.md#临床试验中的常见做法)。待 Li 核实。

## 相关卡片

- [CON-survival-analysis-overview](CON-survival-analysis-overview.md)：生存分析框架
- [MTH-kaplan-meier](MTH-kaplan-meier.md)：KM 的逐步计算、在险集规则
- [CON-logrank-vs-cox](CON-logrank-vs-cox.md)：log-rank 与 Cox 的分工、PH 假设
- [CON-hazard-ratio](CON-hazard-ratio.md)：HR 的含义与 CI
- [CON-censoring](CON-censoring.md)：删失的原因与规则
- [CON-confidence-interval](../../inference/CON-confidence-interval.md)：CI 与 P 值的对应

## 出处

- Claude 对话（inbox: KM_log_rank_cox_1.md；AI 生成，原始出处待补）
- Claude 对话（inbox: KM_log_rank_cox_2.md；AI 生成，原始出处待补）
