---
id: CON-survival-analysis-non-clinical
title: "生存分析在临床以外的应用：工程、互联网、金融等领域的起点、事件与删失（Survival Analysis Beyond Clinical Trials）"
categories: [non-clinical, survival, time-to-event, censoring, reliability-analysis, duration-analysis, event-history-analysis, churn, retention, aft]
related: [CON-survival-analysis-overview, MTH-kaplan-meier]
sources: ["Claude 对话（inbox: Time_to_event_analysis_area.md）"]
status: draft
updated: 2026-11-19
---

> 出处待补：本卡内容来自 Claude 对话（inbox: Time_to_event_analysis_area.md），属 AI 生成内容，未引用原始文献。生存分析的方法本身（删失、KM、log-rank、Cox）见 [CON-survival-analysis-overview](../methods/tte/CON-survival-analysis-overview.md)。
>
> 整理记录（2026-11-19）：本卡内容原是 CON-survival-analysis-overview 的"临床以外的应用"小节，随"非临床应用"栏目建立原样移来；只把原文"（见上）""（见第 1 节）"两处卡内引用改成了指向原卡的链接。下面第一条整理记录是原小节里的。

## 各领域的起点、事件与删失

> 以下来自 Claude 对话（inbox: Time_to_event_analysis_area.md），AI 生成，出处待补。

只要问题能写成"从某个起点开始，过多久会发生某件事"，并且存在"观察结束时事情还没发生"的情况（删失），就能用生存分析。

| 领域 | 起点 | 事件 | 删失的例子 |
|---|---|---|---|
| 工程 / 可靠性 | 设备开始运行 | 故障 | 测试结束时仍在正常运行 |
| 互联网 / SaaS | 用户注册 | 流失（取消订阅、不再活跃） | 统计截止时仍是活跃用户 |
| 金融 / 信贷 | 贷款发放 | 违约或提前还款 | 到观察期结束仍在正常还款 |
| 保险 / 精算 | 投保 | 理赔或身故 | 保单仍有效 |
| 人力资源 | 入职 | 离职 | 到现在仍在职 |
| 市场营销 | 收到优惠券 | 首次购买 | 还没买 |
| 软件工程 | Bug 被提交 | Bug 被修复 | 至今未关闭 |
| 社会学 / 经济学 | 失业 | 重新就业 | 调查结束时仍在找工作 |
| 刑事司法 | 出狱 | 再次犯罪 | 随访期内未再犯 |
| 生态学 | 动物被标记放生 | 死亡或迁出 | 研究结束仍被观测到 |

不同领域叫法不同（见 [CON-survival-analysis-overview](../methods/tte/CON-survival-analysis-overview.md#名称)），但方法是同一套：

- 工程上叫可靠性分析，更常用 Weibull 等参数模型，AFT 名字里的 "failure" 就是从这里来的。
- 经济学、社会学叫持续时间分析（duration analysis）或事件史分析（event history analysis）。
- 互联网公司做用户留存时，留存曲线本质上就是 KM 曲线，Cox 模型用来分析"哪些因素让用户更早流失"。

以客户流失为例：用"已流失人数 / 总注册人数"直接算流失率是有偏的，因为最近注册的用户还没来得及流失，相当于被删失了。用 KM 处理之后，不同时期注册的用户才能放在一起公平比较。这和临床试验里删失患者不能直接扔掉或当作事件（见 [CON-survival-analysis-overview](../methods/tte/CON-survival-analysis-overview.md#1-它解决什么问题)），是完全相同的道理。

> 整理记录（2026-11-19）：材料中"不同领域叫法不同"一句与本卡"名称"一段重复，这里改为"见上"；最后一句补了指向第 1 节的说明。
>
> 补充（Claude）：AFT 即加速失效时间模型（accelerated failure time model），一种参数生存模型，假设协变量使事件时间按比例"加速"或"减速"；本库尚无专门卡片，待 Li 核实。

## 相关卡片

- [CON-survival-analysis-overview](../methods/tte/CON-survival-analysis-overview.md)：生存分析框架、删失、KM / log-rank / Cox
- [MTH-kaplan-meier](../methods/tte/MTH-kaplan-meier.md)：KM 估计（留存曲线即 KM 曲线）

## 出处

- Claude 对话（inbox: Time_to_event_analysis_area.md；AI 生成，原始出处待补）
