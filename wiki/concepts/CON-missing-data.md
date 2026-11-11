---
id: CON-missing-data
title: "缺失数据机制与敏感性分析（Missing Data Mechanisms: MCAR / MAR / MNAR）"
categories: [missing-data, estimand, sensitivity-analysis, hypothetical, treatment-policy, mcar, mar, mnar, tipping-point, retrieved-dropout]
related: [CON-estimand, CON-MMRM, REF-ICH-E9R1, GOT-ice-reason-collection, CON-sensitivity-analysis, CON-confirmatory-methods-overview]
sources: ["Claude 对话（inbox: hypothetical_vs_completers.md）", "Claude 对话（inbox: missing_1.md）", "Claude 对话（inbox: ae_discontinuation_mar_mnar.md）"]
status: draft
updated: 2026-11-05
---

> 出处待补：本卡内容来自 Claude 对话（inbox: hypothetical_vs_completers.md、missing_1.md、ae_discontinuation_mar_mnar.md），属 AI 生成内容，未引用原始文献，需对照 ICH E9(R1)、缺失数据相关文献（如 NRC 2010 报告）核实。

## 一句话定义

缺失机制描述"数据为什么缺失"与结局的关系，它决定了哪种分析方法能得到无偏估计；在 estimand 框架下，主要用于 hypothetical 策略中 ICE 后数据的估计。

## 三种机制与对应方法

| 机制 | 缺失和什么有关 | 直接删掉缺失者（完成者分析） | 能用的方法 |
|---|---|---|---|
| MCAR（Missing Completely At Random，完全随机缺失） | 什么都无关：既和病人情况无关，也和本该测到的值无关，纯属运气 | 没偏倚，只是样本少、精度低 | 完成者分析也无偏 |
| MAR（Missing At Random，随机缺失） | 只和**已观测**到的数据有关（基线、中心、停药前测量值等） | 有偏，但能用模型纠正 | [MMRM](CON-MMRM.md)、多重插补（MI），模型中纳入相关已观测信息 |
| MNAR（Missing Not At Random，非随机缺失） | 和**没观测到**的值本身有关，已有数据看不出端倪 | 有偏，模型也救不了 | 任何方法都无法完全纠正，只能做敏感性分析 |

### 例子

减肥药试验，第 6 个月体重缺失：

- **MCAR**：秤坏了一天；样本运输中摔碎；病人搬家（和身体状况无关）。
- **MAR**：前几个月体重一直降不下来的人更容易失去信心而退出（前几个月体重都有记录）。
- **MNAR**：病人第 6 个月偷偷反弹了，不好意思来复诊（前 5 个月一切正常）。

更多临床试验情境：

| 机制 | 例子 | 共同点 |
|---|---|---|
| MCAR | 中心实验室设备故障，某天样本结果丢失；血样溶血或摔碎；EDC 迁移出错丢了一批访视；受试者因配偶工作调动搬走；疫情封控导致某周访视全部取消 | 缺失原因和病情、疗效、副作用都无关 |
| MAR | 前几次 HbA1c 偏高的人更易退出；年龄大的人因行动不便错过访视；已报告 AE 的人更易停药退出（AE 已记录）；基线病情重的人更常错过后期访视；某些中心随访管理差（中心是已知协变量） | 把这些已观测信息放进模型（如 MMRM 中加入基线值、中心、既往测量值）就能合理推测 |
| MNAR | 抑郁症患者两次访视间急剧恶化未复诊，最后记录还显示好转；疼得太厉害没法出门而错过疼痛评分；体重反弹的人不来称重；复吸的人回避随访；肿瘤患者恶化住进别的医院，肿瘤评估没做 | 缺失原因正是那个没测到的结果本身，模型只能"猜" |

> 戒烟试验常规定"失访按复吸处理"，即预先把这类 MNAR 缺失按最不利结局处理。
>
> 补充（Claude）：这种做法在 estimand 框架下可看作把失访纳入终点定义（类似 composite 思路）；归类待 Li 核实。

### 归类取决于情境

同一个现象在不同情境下归类可能不同。例如"因 AE 退出"：如果 AE 已被记录且模型考虑了它，更接近 MAR；如果退出是因为一个没报告的、和结局相关的恶化，就是 MNAR。现实中三种机制往往混在一起，分类只是帮助思考的框架，最终靠敏感性分析兜底。

## 停药 ≠ 数据缺失

（来源：ae_discontinuation_mar_mnar.md）病人因 AE 等原因停药但**仍继续来访视**，数据就没有缺，谈不上 MAR / MNAR；在 treatment policy 策略下这些停药后数据直接使用。缺失问题只在两种情况下出现：

1. 停药后**也不再来评估**——真正失访；
2. **Hypothetical 策略**下，停药后数据被**按设计视为缺失**（即使测了也不用），要推测"假如没停药"的值。

## 因 AE 停药：偏 MAR 还是偏 MNAR？

（来源：ae_discontinuation_mar_mnar.md）没有固定答案，看两点：

| 判断点 | 偏 MAR | 偏 MNAR |
|---|---|---|
| ① AE 和疗效终点有没有关系 | 糖尿病试验因**皮疹**停药：皮疹与 HbA1c 基本无关，停药前轨迹能较好代表此人 | 抗抑郁药试验因**抑郁加重或自杀意念**停药：AE 本身就是疗效终点在恶化 |
| ② 停药前数据能否反映其状况 | AE 前几次访视已显示疗效变差，模型能利用 | AE 突然发生、之前一切正常，而 AE 又预示结局变差 |

> 分歧记录：此前 hypothetical_vs_completers.md 笼统称"因副作用停药者停药后结局很可能比 MAR 推测更差（MNAR）"；missing_1.md 把"已报告 AE 的人更易退出"列为 MAR 例子。本节材料给出了统一的判断框架（看 AE 与终点的关系、停药前数据是否有预兆），两种说法分别对应表中两列。原"⚠ 存在分歧"标记已据此改为本说明；是否认可此调和由 Li 判断。

## 策略决定缺失怎么补

（来源：ae_discontinuation_mar_mnar.md）

| 情形 | 倾向 / 常用方法 |
|---|---|
| Hypothetical 策略，AE 与疗效无关、停药前数据完整 | 主分析常假设 MAR："停药者如果继续服药，会像病史相似的继续服药者一样" |
| AE 本身反映疗效恶化 | MNAR，需敏感性分析 |
| **Treatment policy 策略下停药后又失访** | **标准 MAR 不合适**：模型会拿"继续服药的人"推测"已停药的人"，等于假设停药后药效还在。常用 J2R（停药后向对照组靠拢）或 **retrieved dropout 插补**（用同样停药但仍在随访的人的数据推测失访者） |

实际 SAP 里，因 AE 停药的主分析往往基于 MAR 或参考组插补，再配 tipping point 等敏感性分析，看结论在"更悲观的假设"下是否依然成立。

> 注意：J2R 的角色随策略不同——hypothetical + MAR 主分析下，J2R 常作为**敏感性分析**（见下文）；treatment policy 下，J2R / retrieved dropout 可能就是**主分析**的插补方法。

> 补充（Claude）：retrieved dropout 插补要求有足够多"停药但仍随访"的受试者，样本少时模型不稳定，此时常退回 reference-based 方法。待对照文献（如 Wang et al. / Polverejan & Dragalin 等关于 retrieved dropout 的研究）核实。

## MAR 无法被数据验证

能区分 MAR 和 MNAR 的恰恰是没测到的那部分数据，所以**无法用数据证明**缺失属于 MAR 还是 MNAR。MAR 永远只是一个假设——这就是为什么 E9(R1) 要求主分析之外必须配敏感性分析。

临床试验里真正的 MCAR 很少见，病人退出大多多少和病情或副作用有关；材料称这也是为什么现在监管机构基本不接受完成者分析作为主分析（**待核实**：需对照 EMA Guideline on Missing Data (2010)、NRC 2010 等原文）。

## 为什么完成者分析不等于 hypothetical 估计

- 完成者是自我选择出来的，不是随机子集；两组按不同程度筛掉人之后，随机化带来的可比性被破坏。
- 只有在 MCAR 下完成者分析才无偏。
- MMRM / MI 在 MAR 下利用停药者停药前的轨迹推测（例如停药前 HbA1c 或体重就下降得慢），而不是简单丢掉，从而部分纠正完成者分析的偏倚。

例子见 [CON-estimand 中的药 A / 药 B 对比](CON-estimand.md#composite-策略如何把耐受性算进结果)。

## 应对思路：减少缺失 → 收细原因 → 敏感性分析兜底

导致缺失的真实原因往往看不见（见 [GOT-ice-reason-collection](../gotchas/GOT-ice-reason-collection.md#更深一层真实原因往往收不上来)），所以临床试验主要靠三条路：

1. **尽量别让数据缺（最有效）**
   - 积极随访和留存：电话、提醒、交通补助、上门或远程访视。
   - E9(R1) 之后特别强调：**停药不等于退出试验**。停药后也尽量继续评估；这些停药后数据（retrieved dropout data）正是 treatment policy 策略需要的，还能用来推测彻底失访的人。
   - 访视窗口设得灵活些，错过了还能补。
2. **尽量把能收的原因收细**：停药原因选项具体、少依赖"其他"；失访前最后一次联系情况、最后测量值记录完整。这些不能证明缺失机制，但能帮统计师判断哪种假设更合理。
3. **承认不确定，用敏感性分析兜底**（见下节）。

思路：原因查不清，就先尽力减少缺失，再检验"如果最坏的情况是真的，结论还站得住吗"。

## MAR 何时站不住：敏感性分析

因副作用停药的人，停药后的结局很可能比 MAR 推测的更差（即 MNAR）。主分析通常基于 MAR，SAP 中再配以下敏感性分析：

- **Reference-based MI（jump to reference / copy reference）**：假设停药后的表现趋向对照组。
- **Tipping point 分析**：逐步往停药者的插补值里加惩罚（偏移量），例如假设失访者比 MAR 推测的再差 1、2、3 个单位，看到什么程度结论会翻转。如果要假设得非常极端才翻转，结论就算稳健。
- **模式混合模型（pattern mixture model）**：对不同退出模式分别做不同假设（来源：sensitivity_analysis1.md；方法细节待补）。

敏感性分析的总体定义及其与补充分析的区别见 [CON-sensitivity-analysis](CON-sensitivity-analysis.md)。

> 补充（Claude）：J2R 与 CR 并不相同：J2R（jump to reference）假设停药后均值立即"跳到"对照组的均值轨迹；CR（copy reference）假设停药者从一开始就按对照组的均值轨迹和协方差结构建模，停药前的疗效随相关性逐渐衰减而非立即消失。通常 J2R 比 CR 更保守。待对照 Carpenter, Roger & Kenward (2013) 等文献核实。

## 相关卡片

- [CON-estimand](CON-estimand.md)
- [CON-MMRM](CON-MMRM.md)
- [GOT-ice-reason-collection](../gotchas/GOT-ice-reason-collection.md)：缺失 / 停药原因的收集
- [CON-sensitivity-analysis](CON-sensitivity-analysis.md)：敏感性分析 vs 补充分析
- [REF-ICH-E9R1](../references/REF-ICH-E9R1.md)

## 出处

- Claude 对话（inbox: hypothetical_vs_completers.md；AI 生成，原始出处待补）
- Claude 对话（inbox: missing_1.md；AI 生成，原始出处待补）
- Claude 对话（inbox: ae_discontinuation_mar_mnar.md；AI 生成，原始出处待补）
