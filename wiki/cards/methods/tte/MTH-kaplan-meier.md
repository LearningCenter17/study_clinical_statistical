---
id: MTH-kaplan-meier
title: "Kaplan-Meier 估计与在险人数：闯关相乘、逐步手算（含并列死亡）、在险集规则、中位生存与 number at risk 表（Kaplan-Meier Estimator and Number at Risk）"
categories: [survival, kaplan-meier, number-at-risk, censoring, risk-set, km-plot, tlf, tern, ggsurvfit, proc-lifetest, median-survival, greenwood, non-informative-censoring, tied-events]
related: [CON-survival-analysis-overview, CON-logrank-vs-cox, CON-hazard-ratio, CON-ci-width, CON-confirmatory-methods-overview, CON-survival-analysis-non-clinical, CON-reliability-engineering, CON-censoring]
sources: ["Claude 对话（inbox: at_risk_event.md）", "Claude 对话（inbox: Kaplan–Meier_1.md）"]
status: draft
updated: 2026-11-19
---

> 出处待补：本卡内容来自 Claude 对话（inbox: at_risk_event.md；"核心思路：闯关相乘"、"第二个例子"、"从曲线上读什么"、"关键前提"四节来自 Kaplan–Meier_1.md），属 AI 生成内容，未引用原始文献（如 Kaplan & Meier 1958、Collett《Modelling Survival Data in Medical Research》）。算例已由 Claude 在 R 4.5.2 中复核。生存分析的整体框架（删失、S(t)、log-rank、Cox）见 [CON-survival-analysis-overview](CON-survival-analysis-overview.md)；"事件"在各终点里指什么见该卡第 1 节。

## 一句话定义

"在险人数"（number at risk）指的是：**在某个时间点 t，仍在观察中、还"有可能"在这一刻发生事件的人数**。换句话说，就是到 t 为止既没发生事件、也没被删失的人。KM 估计在每个事件时间点用"(在险人数 − 事件数) / 在险人数"去乘前一步的生存率（见 [CON-survival-analysis-overview](CON-survival-analysis-overview.md#3-三大常用方法)）。

> 补充（Claude）：写成公式即 Ŝ(t) = ∏_{tᵢ ≤ t} (nᵢ − dᵢ) / nᵢ，nᵢ 为在险人数、dᵢ 为事件数。待 Li 核实。
>
> 整理记录（2026-11-19）：上面这条公式补充原写在 CON-survival-analysis-overview 的 KM 段落下（当时 KM 尚无独立卡片），随本卡建立原样移来。

## 核心思路：闯关相乘

> 以下来自 Claude 对话（inbox: Kaplan–Meier_1.md），AI 生成，出处待补。

**KM 估计 = 把"活过整段时间"拆成"一关一关地闯过去"，每一关的通过率相乘。**

活过 2 年 = 闯过第一次死亡发生的时间点 × 闯过第二次死亡时间点 × ……

每一关的通过率是：

> **该时刻的通过率 = 1 − (这一刻死了几个人 / 这一刻之前还在观察中的人数)**

"还在观察中的人数"叫**风险集（number at risk）**，就是此刻还活着、也还没被删失的人。

把这些通过率连乘起来，就是 KM 估计的生存函数 S(t)：

$$\hat S(t) = \prod_{t_i \le t}\left(1 - \frac{d_i}{n_i}\right)$$

KM 的巧妙之处在于：**删失的人在被删失之前都算数，删失之后就悄悄退出分母**，不当死亡处理，也不当存活到终点处理。（为什么删失的人既不能扔掉、也不能当成活到终点，见 [CON-survival-analysis-overview](CON-survival-analysis-overview.md#1-它解决什么问题)；删失的原因与类型见 [CON-censoring](CON-censoring.md)。）

> 整理记录（2026-11-19）：材料中"为什么需要它：删失问题"一节（扔掉删失者会浪费信息、当成活过终点会高估生存率）与 CON-survival-analysis-overview 第 1 节重复，未再写入，只保留了上面 KM 特有的一句。上方"一句话定义"下的公式补充（Claude）与这里材料给出的公式等价（(nᵢ − dᵢ)/nᵢ = 1 − dᵢ/nᵢ）。
>
> 补充（Claude）：材料把 number at risk 叫"风险集"。本库用"在险人数"指人数（number at risk），用"在险集"（risk set）指这群人本身；"风险集"与"在险集"是同一概念的不同译法。待 Li 确认用词。

## 一个小例子

6 个受试者，时间单位是月：

| 受试者 | 时间 | 状态 |
|---|---|---|
| A | 2 | 事件 |
| B | 3 | 删失（失访） |
| C | 5 | 事件 |
| D | 6 | 删失 |
| E | 8 | 事件 |
| F | 10 | 删失（试验结束） |

按时间顺序走一遍，看在险人数怎么变化，以及它怎么决定 KM 生存率：

| 时间 | 发生了什么 | 此刻在险人数 | 事件数 | 这一步的存活比例 | KM 生存率 S(t) |
|---|---|---|---|---|---|
| 0 | 开始 | 6 | – | – | 1.000 |
| 2 | A 发生事件 | **6** | 1 | 5/6 | 0.833 |
| 3 | B 删失 | 5（B 仍在内）→ B 移出后剩 4 | 0 | 不变 | 0.833 |
| 5 | C 发生事件 | **4** | 1 | 3/4 | 0.833 × 0.75 = 0.625 |
| 6 | D 删失 | 3（D 仍在内）→ D 移出后剩 2 | 0 | 不变 | 0.625 |
| 8 | E 发生事件 | **2** | 1 | 1/2 | 0.625 × 0.5 = 0.313 |
| 10 | F 删失 | 1 → 0 | 0 | 不变 | 0.313 |

> 整理记录（2026-11-19）：材料原表第 3、6 个月两行写作"5 → 移出后剩 4""3 → 移出后剩 2"。材料随后自己指出这种写法"容易让人以为 5 本身已经扣过 B 了"，准确说法是"第 3 个月在险 5 人（已扣掉 A，B 仍在内），B 删失后剩 4 人"。这里按材料的更正把括号说明写进了表格。

- **A 在第 2 个月发生事件**，从第 2 个月之后就不在险了，所以 6 → 5。
- **B 在第 3 个月删失**，第 3 个月之后也不在险了，所以 5 → 4。

把每个时间点"谁还在场"列出来就清楚了：

| 时间点 | 在场的人 | 在险人数 | 说明 |
|---|---|---|---|
| 第 2 个月 | A B C D E F | 6 | A 在这一刻发生事件，事件发生那一刻他仍算在险 |
| 第 3 个月 | B C D E F | 5 | A 已经出局；B 在这一刻删失，这一刻他仍算在险 |
| 第 5 个月 | C D E F | 4 | B 也出局了 |
| 第 8 个月 | E F | 2 | C（事件）、D（删失）出局 |

## 在险集规则

**在时间 t 的在险人数 = 观测时间 ≥ t 的人数。** 一个人在自己的事件时间或删失时间**那一刻仍然计入**在险人数，**之后**才移出。

所以第 3 个月的 5 人里包括 B 本人。B 在这一刻删失，没有发生事件，曲线不下降；B 移出后，下一个事件时间点（第 5 个月）的在险人数就变成 4。

另外，第 3 个月这一行其实不影响 KM 计算，因为那里没有事件。KM 只在**事件时间点**（第 2、5、8 个月）用到在险人数：分别是 6、4、2。

可以看到三点：

- **删失本身不让曲线下降**，但会让在险人数减少。B 在第 3 个月失访，他在第 2 个月那一步算进了分母，贡献了"前 3 个月没出事"的信息，之后才退出。
- **在险人数就是每一步的分母**。KM 的计算本质上就是不断地问："此刻还在场的人里，有多大比例熬过了这一刻？"
- **同样是 1 个事件，影响大小完全不同**：第 2 个月时 6 人在险，1 个事件让曲线下降约 17%；到第 8 个月只剩 2 人在险，1 个事件就让曲线直接**减半**。

> 数值复核（Claude，R 4.5.2）：`survfit(Surv(t, e) ~ 1)` 在事件时间 2 / 5 / 8 给出 n.risk = 6 / 4 / 2，S(t) = 0.833 / 0.625 / 0.3125（材料四舍五入为 0.313）；中位生存时间 = 8 个月（S(t) 在第 8 个月首次 ≤ 0.5）。`summary(fit, times = c(0, 3, 6, 9))` 给出 n.risk = 6 / 5 / 3 / 1，即第 3 个月 5 人、第 6 个月 3 人，与"观测时间 ≥ t"的规则一致。默认 log 变换下第 8 个月 S(t) 的 95% CI 为 0.067–1，几乎没有信息量，正好印证下文"在险人数少的地方置信区间很宽"。

## 第二个例子：有并列死亡

> 以下来自 Claude 对话（inbox: Kaplan–Meier_1.md），AI 生成，出处待补。

6 个病人的随访时间（月），"+" 表示删失：

**3, 5+, 6, 6, 9+, 12**

| 时间 | 风险集 n | 死亡 d | 这一关通过率 | 累计 S(t) |
|---|---|---|---|---|
| 3 | 6 | 1 | 5/6 | 0.833 |
| 5+ | — | 删失 1 人 | 不算一关 | 仍为 0.833 |
| 6 | 4 | 2 | 2/4 | 0.833 × 0.5 = 0.417 |
| 9+ | — | 删失 1 人 | 不算一关 | 仍为 0.417 |
| 12 | 1 | 1 | 0/1 | 0 |

需要注意的几点：

- **删失时 S(t) 不变**，只是下一关的分母变小了（第 6 个月时风险集是 4，不是 5，因为 5 月删失的那个人已经离开了）。
- **只在有死亡的时间点，曲线才往下掉一个台阶**，所以 KM 曲线是阶梯状的。
- 图上删失点一般画成小竖线 "|" 或 "+"，就是你在 TLF 里常见的那些小刻度。

> 数值复核（Claude，R 4.5.2）：`survfit(Surv(t, e) ~ 1)` 在 3 / 6 / 12 个月给出 n.risk = 6 / 4 / 1，n.event = 1 / 2 / 1，S(t) = 0.833 / 0.417 / 0；中位生存时间 = 6 个月。第 6 个月 2 人同时死亡，一步就用 2/4，这正是 KM 处理并列事件时间（tied event times）的方式。
>
> 补充（Claude）：最后一个观测是死亡时曲线降到 0；若最后一个观测是删失，曲线停在最后的高度，不会降到 0。

## 从曲线上读什么

> 以下来自 Claude 对话（inbox: Kaplan–Meier_1.md），AI 生成，出处待补。

- **中位生存时间**：S(t) 第一次降到 ≤ 0.5 的时间。上面的例子里是 6 个月。如果曲线一直没降到 0.5，就报告"未达到（NR）"。
- **某个时间点的生存率**：比如 12 个月生存率，直接读曲线高度，再配上置信区间。置信区间通常用 **Greenwood 公式**算方差，再做 log-log 变换，SAS 和 R 的默认设置不太一样，做 double programming 的时候常在这里对不上（具体默认值见本卡下文和 [CON-survival-analysis-overview](CON-survival-analysis-overview.md#6-落到临床编程上)）。
- **两组比较**：KM 本身只负责"描述"，比较两条曲线一般用 **log-rank 检验**，要估计效应大小就用 **Cox 模型**算 HR（见 [CON-logrank-vs-cox](CON-logrank-vs-cox.md)、[CON-hazard-ratio](CON-hazard-ratio.md)）。

> 补充（Claude）：中位生存时间的置信区间常用 Brookmeyer-Crowley 法，见 [MTH-ci-construction](../../inference/MTH-ci-construction.md)。上例 R 默认（log 变换）给出中位数 95% CI 为 6 至 NA，即上限"未达到"，TLF 里也写作 NR。待 Li 核实。

## 关键前提：非信息性删失

> 以下来自 Claude 对话（inbox: Kaplan–Meier_1.md），AI 生成，出处待补。

KM 默认**删失的人和留下的人，未来的风险是一样的**。如果病人是因为病情恶化才退出、被记为删失，这个假设就被破坏了，KM 会高估生存率。这也是 SAP 里要仔细定义删失规则的原因（比如开始新治疗算不算删失、末次评估日期怎么取，见 [CON-censoring](CON-censoring.md)）。

## 为什么这个数很重要

**1. 它决定了曲线在每个时间点有多可信**

在险人数多的地方，估计稳定，置信区间窄；在险人数少的地方，一个人的结局就能让曲线大幅跳动，置信区间很宽。KM 曲线尾部常常出现"断崖式下跌"或"长长的平台"，往往只是因为那里只剩几个人。看曲线时如果不看在险人数，很容易把尾部的随机波动当成真实的疗效差异。

**2. 它暴露两组随访是否均衡**

假设两组入组人数一样，但某一组的在险人数下降得特别快，而事件数并不多，说明这一组**删失特别多**：可能是因为不良反应退出，或者失访更多。这可能违反"非信息性删失"假设（见 [CON-survival-analysis-overview](CON-survival-analysis-overview.md#5-进阶话题)），是审阅者会追问的地方。

**3. log-rank 检验和 Cox 模型都建立在"在险集"上**

log-rank 检验在每个事件时间点，按两组的在险人数比例计算"期望事件数"，再和观察到的事件数比较。Cox 的部分似然也是在每个事件时间点，比较"发生事件的那个人"和"当时所有在险的人"。所以在险人数不只是用来展示的，它就是这些方法的计算基础。（两种方法的分工见 [CON-logrank-vs-cox](CON-logrank-vs-cox.md)。）

**4. 它是 KM 图的标准组成部分**

规范的 KM 图下方都会附一张 **number at risk 表**，列出各组在 0、3、6、9……个月时的在险人数。期刊（CONSORT 等报告规范）和监管审阅普遍期望看到它，没有这张表的 KM 图很难被正确解读。

> 补充（Claude）："CONSORT 等报告规范期望看到 number at risk 表"是材料的说法，具体条目待 Li 对照 CONSORT 原文核实。

**在 R 里出图时：**

- `tern::g_km()` 默认就会在图下方生成在险人数表。
- `ggsurvfit` 用 `+ add_risktable()` 添加。
- `print(survfit(...))` 给出中位生存时间及 95% CI（来自 Kaplan–Meier_1.md；完整的 ADTTE 代码和 `Surv(AVAL, 1 - CNSR)` 的方向问题见 [CON-survival-analysis-overview](CON-survival-analysis-overview.md#6-落到临床编程上)）。
- 想直接拿到具体数字做 QC，可以用 `summary(survfit(...), times = c(0, 3, 6, 9, 12))`，输出里的 `n.risk` 列就是在险人数，可以和 SAS `PROC LIFETEST` 的结果逐个时间点核对。

> 补充（Claude）：和 SAS 核对 KM 生存率的置信区间时，注意两边的默认变换不同（R `survfit` 默认 log，SAS LIFETEST 默认 log-log），见 [CON-survival-analysis-overview](CON-survival-analysis-overview.md#6-落到临床编程上)。

## 相关卡片

- [CON-survival-analysis-overview](CON-survival-analysis-overview.md)：生存分析框架、事件定义、删失
- [CON-logrank-vs-cox](CON-logrank-vs-cox.md)：同样建立在在险集上的两种方法
- [CON-hazard-ratio](CON-hazard-ratio.md)：Cox 模型的效应量
- [CON-ci-width](../../inference/CON-ci-width.md)：生存终点的信息量看事件数
- [CON-confirmatory-methods-overview](../CON-confirmatory-methods-overview.md)：KM 在确证性试验中的地位
- [CON-survival-analysis-non-clinical](../../non-clinical/CON-survival-analysis-non-clinical.md)：KM 在临床以外的应用（如用户留存曲线）
- [CON-reliability-engineering](../../non-clinical/CON-reliability-engineering.md)：制造业的可靠性工程（生存分析的非临床应用）
- [CON-censoring](CON-censoring.md)：删失的原因与类型（KM 只能处理右删失）
- [MTH-ci-construction](../../inference/MTH-ci-construction.md)：中位生存期 CI 的构造方法

## 出处

- Claude 对话（inbox: at_risk_event.md；AI 生成，原始出处待补）
- Claude 对话（inbox: Kaplan–Meier_1.md；AI 生成，原始出处待补）
