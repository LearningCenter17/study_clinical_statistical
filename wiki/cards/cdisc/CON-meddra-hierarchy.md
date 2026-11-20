---
id: CON-meddra-hierarchy
title: "MedDRA 五层结构与 SDTM AE 编码变量：LLT / PT / HLT / HLGT / SOC、主 SOC 与 AEBODSYS（MedDRA Hierarchy）"
categories: [cdisc, sdtm, meddra, adverse-event, coding, soc, pt, aedecod, aebodsys, safety, tlf]
related: [CON-cdisc-variable-naming, CON-ae-severity-asev, CON-ae-causality-arel, CON-sae-criteria]
sources: ["Claude 对话（inbox: medDRA_1.md）"]
status: draft
updated: 2026-11-20
---

> 出处待补：本卡内容来自 Claude 对话（inbox: medDRA_1.md），属 AI 生成内容，未引用原始文献。需对照 MedDRA Introductory Guide、MedDRA Term Selection: Points to Consider 及 SDTMIG AE 域核实。

## 一句话定义

这些都是 **MedDRA** 编码字典里的层级，也就是 AE 编码后 SDTM AE 域里存的那一组变量。每一层都有"名称"和"代码"两个变量，所以一共 12 个。

> 整理记录（2026-11-19）：材料原小节标题为"和你列的变量一一对应"（指对话中用户列出的变量），这里改为"和 SDTM AE 变量的对应"。`DECOD`、`BODSYS` 等变量名零件见 [CON-cdisc-variable-naming](CON-cdisc-variable-naming.md)。

## MedDRA 的五层结构

从最细到最粗：

```
SOC   系统器官分类          Body System or Organ Class   （27 个）
 └─ HLGT  高位组语           High Level Group Term
     └─ HLT  高位语           High Level Term
         └─ PT  首选术语       Preferred Term (Dictionary-Derived Term)
             └─ LLT 低位语     Lowest Level Term             （最多，8 万多个）
```

举个例子，研究者在 CRF 上写的是 "feeling sick"：

| 层级 | 名称 |
|---|---|
| 原始报告（`AETERM`） | feeling sick |
| LLT | Feeling sick |
| PT | Nausea |
| HLT | Nausea and vomiting symptoms |
| HLGT | Gastrointestinal signs and symptoms |
| SOC | Gastrointestinal disorders |

编码时，coder 把研究者写的原话匹配到一个 **LLT**，再往上的 PT、HLT、HLGT、SOC 都由字典自动确定。LLT 里有很多同义词、口语和不同拼写（如 "feeling sick"、"queasy"），它们都会归到同一个 PT（Nausea）。

## 和 SDTM AE 变量的对应

| Label | SDTM 变量 | 层级 |
|---|---|---|
| Lowest Level Term / Code | `AELLT` / `AELLTCD` | LLT |
| Dictionary-Derived Term / Preferred Term Code | `AEDECOD` / `AEPTCD` | PT |
| High Level Term / Code | `AEHLT` / `AEHLTCD` | HLT |
| High Level Group Term / Code | `AEHLGT` / `AEHLGTCD` | HLGT |
| Body System or Organ Class / Code | `AEBODSYS` / `AEBDSYCD` | SOC（用于分析的那个） |
| Primary System Organ Class / Code | `AESOC` / `AESOCCD` | SOC（主 SOC） |

注意 PT 的名称变量不叫 `AEPT`，而叫 `AEDECOD`（Dictionary-Derived Term）。这是 SDTM 的通用命名：所有经过字典编码的术语都用 `--DECOD`，比如合并用药是 `CMDECOD`。

## 为什么有两个 SOC

因为 MedDRA 是**多轴**（multiaxial）的：一个 PT 可以同时属于几个 SOC，但只有一个被指定为**主 SOC**（primary SOC）。

比如 PT "Pneumonia" 同时在 "Infections and infestations" 和 "Respiratory, thoracic and mediastinal disorders" 两个 SOC 下，主 SOC 是 Infections and infestations（感染类的 PT，主 SOC 规定放在感染 SOC）。

- `AESOC`：固定是**主 SOC**
- `AEBODSYS`：sponsor **在分析和汇总表中使用**的 SOC

绝大多数研究里两者一样，因为一般都按主 SOC 汇总。但 SDTMIG 允许 `AEBODSYS` 不是主 SOC，所以分成两个变量。

## 在 TLF 里怎么用

最常见的 AE 汇总表就是 **SOC + PT** 两层：先按 `AEBODSYS` 分组，下面列 `AEDECOD`，统计发生人数和百分比。HLT / HLGT 比较少用，偶尔用于特定安全性分析（比如把某一类 AE 归在一起看）。LLT 一般只在列表（listing）里出现。

还有一点要注意：MedDRA 每年 3 月和 9 月各更新一次版本。同一个研究的数据要用同一个版本编码，版本号通常写在 define.xml 和 TLF 的脚注里。

> 补充（Claude）：SOC 个数 27、LLT 8 万多个是材料的说法，具体数字随 MedDRA 版本变化，待 Li 对照当前版本核实。ADaM ADAE 中通常直接沿用 `AEBODSYS`、`AEDECOD` 做汇总；AE 汇总表"发生人数"按受试者计（同一受试者同一 PT 多次只算一次），这通常借助 `AOCCPFL` 一类首次发生标识实现。待 Li 核实。

## 相关卡片

- [CON-cdisc-variable-naming](CON-cdisc-variable-naming.md)：`--DECOD`、`BODSYS`、`OCC` 等变量名零件
- [CON-ae-severity-asev](CON-ae-severity-asev.md)：按最严重程度汇总 AE、severity 与 seriousness 的区别
- [CON-ae-causality-arel](CON-ae-causality-arel.md)：药物相关 TEAE 按 SOC / PT 汇总
- [CON-sae-criteria](CON-sae-criteria.md)：EMA IME 列表（按 PT 整理）用于判断重要医学事件

## 出处

- Claude 对话（inbox: medDRA_1.md；AI 生成，原始出处待补）
