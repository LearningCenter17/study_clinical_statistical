---
id: WF-pregnancy-reporting
title: "临床试验中的妊娠报告与随访：流程、报告期与试验结束后的处理（Pregnancy Reporting and Follow-up）"
categories: [safety, pregnancy, pharmacovigilance, sae, congenital-anomaly, contraception, half-life, dsur, psur, protocol]
related: [CON-sae-criteria, CON-ae-severity-asev]
sources: ["Claude 对话（inbox: congenital_anomaly.md）"]
status: draft
updated: 2026-11-20
---

> 出处待补：本卡内容来自 Claude 对话（inbox: congenital_anomaly.md），属 AI 生成内容，未引用原始文献。需对照 ICH E2A、ICH E6 GCP、CTFG《Recommendations related to contraception and pregnancy testing in clinical trials》及具体方案核实。先天异常作为 SAE 标准、`AESCONG` 变量见 [CON-sae-criteria](../cdisc/CON-sae-criteria.md)。
>
> 整理记录（2026-11-20）：材料原文以"对，"开头，并有"你们统计编程""你们方案""前面说的流程"等对话用语，这里去掉了"对，"和"你们"，把"前面说的流程"改为"上面的流程"；按内容加了四个小节标题。

## 一句话定义

怀孕要专门随访，而且随访可以超出试验本身的时间。

## 一般流程

1. **发现怀孕后立即报告**：研究者得知受试者（或男性受试者的伴侣）怀孕后，通常要在 24 小时内填专门的**妊娠报告表**（Pregnancy Report Form）报给 sponsor 的药物安全部门。怀孕本身不算 AE，但必须报告。女性受试者一般会停止用药。
2. **随访到妊娠结局**：一直跟到分娩、流产或终止妊娠，有的还会随访新生儿一段时间（比如出生后几周到一年，按方案规定）。
3. **伴侣怀孕要另外签同意**：伴侣不是受试者，收集她和孩子的信息前需要她单独签知情同意。

## 如果试验已经结束了怎么办

这是关键：**妊娠随访不受试验结束的限制**。即使受试者已经完成研究、数据库已经锁定，安全部门仍然会继续随访。这时信息走的是**药物警戒（pharmacovigilance）**的渠道：
- 记录在 sponsor 的**安全数据库**（如 Argus、ArisG），而不是临床数据库（EDC）
- 如果发现先天异常，按 SAE 要求**快速报告**给监管机构
- 会出现在后续的定期安全性报告里（比如 DSUR、PSUR）

所以统计编程用的 EDC 数据和 SDTM / ADaM 里，可能根本看不到这类事件。锁库后才知道的结局，不会出现在这次的 CSR 和 TLF 里。

## 为什么实际很少见

方案会尽量预防：育龄受试者必须做妊娠检测，要求研究期间和停药后一段时间内采取高效避孕措施（具体时长根据药物在体内存留的时间定，男性受试者也有相应要求）。所以试验中怀孕本来就少，出现先天异常的就更少了。

## 试验结束后怀孕还要不要随访

看怀孕发生在什么时候，分两种情况：

**1. 在方案规定的"报告期"内：要报告并随访**

方案会规定末次用药后多长时间内的怀孕仍需报告。这个时间段通常和避孕要求的时长一致，依据是药物在体内清除需要多久：
- 常见做法是覆盖药物的 **5 个半衰期**左右（这时体内基本清除干净了）
- 男性受试者往往再加上大约 **90 天**，对应一个精子生成周期
- **生物制剂**（比如单抗）半衰期长，报告期可能长达几个月

这期间怀孕，即使受试者已经完成研究、不再来访视，也要按上面的流程报告给 sponsor 的安全部门并随访到结局。所以方案会要求研究中心提醒受试者，这段时间内怀孕要主动告知。

**2. 超过报告期：一般不再收集**

药物已经清除，怀孕和研究药物没有合理的关联，方案不要求报告，也不随访。

有一个例外：如果研究者在试验结束后得知了某个 SAE（包括先天异常），并且认为**可能和研究药物有关**，按法规（如 ICH E6 GCP）应当报告给 sponsor，不管过了多久。

所以"做完试验后怀孕要不要随访"，具体时间点以方案里 **Pregnancy / Contraception** 相关章节为准。

> 补充（Claude）：
>
> - "24 小时内报告"、"5 个半衰期"、"男性再加约 90 天"是常见做法，具体以方案为准；CTFG 的避孕与妊娠检测建议是欧洲常引用的依据。待 Li 核实。
> - 统计编程侧：锁库前已知的妊娠及其结局一般记录在 EDC 的专门表单里，是否进 SDTM（如作为 AE、或放在自定义域）由 sponsor 决定，看 SDTM spec。待 Li 核实。

## 相关卡片

- [CON-sae-criteria](../cdisc/CON-sae-criteria.md)：先天异常作为 SAE 标准、`AESCONG`
- [CON-ae-severity-asev](../cdisc/CON-ae-severity-asev.md)：severity 与 seriousness

## 出处

- Claude 对话（inbox: congenital_anomaly.md；AI 生成，原始出处待补）
