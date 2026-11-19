---
id: CON-censoring
title: "删失：原因、删失日期怎么取、SAP 删失规则与 ADTTE 中的 CNSR（Censoring）"
categories: [survival, censoring, right-censoring, interval-censoring, left-censoring, administrative-censoring, loss-to-follow-up, sap, adtte, cnsr, pfs, os, statistical-programming, qc]
related: [CON-survival-analysis-overview, MTH-kaplan-meier, CON-estimand, CON-sensitivity-analysis, GOT-ice-reason-collection]
sources: ["Claude 对话（inbox: censoring.md）"]
status: draft
updated: 2026-11-19
---

> 出处待补：本卡内容来自 Claude 对话（inbox: censoring.md），属 AI 生成内容，未引用原始文献（如 CDISC ADaM ADTTE 规范、FDA《Clinical Trial Endpoints for the Approval of Cancer Drugs and Biologics》中的 PFS 删失规则表）。删失为什么不能扔掉、也不能当作事件，以及删失者在似然里怎么贡献信息，见 [CON-survival-analysis-overview](CON-survival-analysis-overview.md#1-它解决什么问题)。

## 一句话定义

删失的意思是：**到某个时间点为止，这个人还没有发生事件，但之后的情况我们看不到了。** 我们只知道他的事件时间"大于"这个时间。

删失的英文是 censoring（名词），形容词或过去分词是 censored。

## 常见的删失原因

**1. 研究结束（行政删失）**

数据截止时病人还活着、事件还没发生。这是最常见的，也最"干净"，因为跟病人病情无关，非信息性删失的假设基本成立（该假设见 [CON-survival-analysis-overview](CON-survival-analysis-overview.md#5-进阶话题)）。

**2. 失访**

病人搬家、联系不上，最后一次确认他还活着的日期就是删失日期。

**3. 撤回知情同意 / 退出研究**

不再收集数据，也在最后一次有效观察时删失。

> 补充（Claude）：失访、撤回同意背后的真实原因往往记录不清，这会影响能否判断删失是否"非信息性"，见 [GOT-ice-reason-collection](../../estimand/GOT-ice-reason-collection.md)。

**4. 按 SAP 规则主动删失**

这是临床试验里最讲究的部分。有些情况病人其实还在随访，但 SAP 规定在某个时间点"截断"。比如肿瘤试验的 PFS：

- 开始了新的抗肿瘤治疗 → 在开始新治疗前最后一次肿瘤评估时删失
- 连续漏掉两次以上评估后才发现进展 → 在最后一次正常评估时删失
- 基线后没有任何评估 → 在随机化当天删失

> 补充（Claude）："开始新治疗即删失"相当于对这个 intercurrent event 采取了 hypothetical 或 while-on-treatment 一类的处理，不同的 estimand 策略会导出不同的删失规则，见 [CON-estimand](../../estimand/CON-estimand.md)。上面三条是常见写法，具体以各试验 SAP 为准；"连续漏掉两次以上"的次数界定也随方案而定。待 Li 核实。

## 删失日期取哪一天

原则是：**取最后一次能确认"事件还没发生"的日期。**

- **OS**：最后一次确认存活的日期（任何访视、电话随访、实验室检查都可以作为证据）
- **PFS**：最后一次**充分的**肿瘤评估日期，而不是最后一次访视日期，因为访视当天没做影像，不能证明没有进展

日期取错是 TTE 分析里最常见的 QC 问题之一。

## 在 ADTTE 里怎么体现

| 变量 | 含义 |
|---|---|
| `CNSR` | 0 = 事件；1 及以上 = 删失（不同的正整数可以代表不同删失原因） |
| `ADT` | 事件日期或删失日期 |
| `EVNTDESC` | 事件或删失的文字描述，比如 "DEATH"、"LAST KNOWN ALIVE" |
| `CNSDTDSC` | 删失日期取自哪里，比如 "Last tumor assessment" |

所以**删失没有统一标准，是按每个终点在 SAP 里逐条定义的**。写 ADTTE 之前，一般要先把 SAP 里的事件和删失规则整理成表格（每种情况对应的 CNSR 值、ADT 来源），再照着表写代码，double programming 时也按这张表对照检查。

> 补充（Claude）：CNSR 用多个正整数区分删失原因时，分析代码里不能再写 `Surv(AVAL, 1 - CNSR)`（CNSR = 2 会得到 −1），应写 `Surv(AVAL, CNSR == 0)`；SAS `time AVAL*CNSR(1, 2, …)` 要列出所有删失取值。CNSR 方向的坑见 [CON-survival-analysis-overview](CON-survival-analysis-overview.md#6-落到临床编程上)。待 Li 核实。

## 删失的类型：上面说的都是"右删失"

临床试验里 99% 的情况是**右删失**：只知道事件发生在某个时间**之后**。另外还有：

- **区间删失**：只知道事件发生在两次访视之间，比如肿瘤进展只能在两次影像检查之间发现。标准分析一般直接用发现日期，当作右删失数据处理。
- **左删失**：只知道事件发生在某个时间**之前**，临床试验中很少见。

KM 只能处理右删失。

> 整理记录（2026-11-19）：CON-survival-analysis-overview 第 1 节原有一句同主题的话，已移到这里，原文为："最常见的是**右删失**：知道事件至少在某时间点之后才发生。另外还有左删失和区间删失，比如事件只在两次访视之间被发现，这在影像学评估进展时很常见。"
>
> 补充（Claude）：区间删失数据也有专门方法（如非参数的 Turnbull 估计、参数模型），"KM 只能处理右删失"指的是标准 KM。把发现日期当作事件日期时，两组评估间隔不同会造成偏倚，所以试验中两组的肿瘤评估时间表通常要求一致。待 Li 核实。

## 相关卡片

- [CON-survival-analysis-overview](CON-survival-analysis-overview.md)：删失在生存分析中的地位、似然、ADTTE 其他变量
- [MTH-kaplan-meier](MTH-kaplan-meier.md)：删失者在 KM 中怎么计入在险人数
- [CON-estimand](../../estimand/CON-estimand.md)：ICE 处理策略决定删失规则
- [CON-sensitivity-analysis](../../missing-data/CON-sensitivity-analysis.md)：删失假设的敏感性分析
- [GOT-ice-reason-collection](../../estimand/GOT-ice-reason-collection.md)：失访、撤回同意的原因记录

## 出处

- Claude 对话（inbox: censoring.md；AI 生成，原始出处待补）
