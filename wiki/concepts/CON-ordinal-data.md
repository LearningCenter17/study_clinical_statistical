---
id: CON-ordinal-data
title: "有序分类数据（Ordinal Data）"
categories: [data-type, ordinal, categorical, ctcae, recist, mrs, cmh, wilcoxon, proportional-odds, ordinal-logistic, adam, avalc]
related: [CON-test-selection, CON-parametric-vs-nonparametric, CON-confirmatory-methods-overview, CON-MMRM, CON-covariate, CON-CMH, CON-proportional-odds-model, GOT-ordinal-or-direction]
sources: ["Claude 对话（inbox: ordinal_data.md）", "Claude 对话（inbox: ordinal_data_adam_correction.md）", "Claude 对话（inbox: cmh_statistics.md）"]
status: draft
updated: 2026-11-12
---

> 出处待补：本卡内容来自 Claude 对话（inbox: ordinal_data.md），属 AI 生成内容，未引用原始文献。

## 一句话定义

**Ordinal data（有序分类数据）**：类别之间有**自然的顺序**，但相邻类别的**间距不一定相等**，数值本身也没有实际意义。

判断标准两条：

1. **能排序**：A < B < C 有意义。这一点区别于 **nominal**（无序分类，如血型、性别）。
2. **不能做算术**：从 1 到 2 的"距离"不一定等于从 2 到 3。这一点区别于 **interval / ratio**（如体重、血压）。

所以即使编码成 1、2、3、4，这些数字也只代表顺序，**算平均值在理论上有问题**。

## 临床试验中常见的例子

| 例子 | 类别 |
|---|---|
| **AE severity（CTCAE grade）** | Grade 1 Mild → 2 Moderate → 3 Severe → 4 Life-threatening → 5 Death |
| **Tumor response（RECIST）** | CR > PR > SD > PD |
| **modified Rankin Scale（mRS）**，卒中试验 | 0（无症状）到 6（死亡） |
| **ECOG performance status** | 0–4（加上 5 = 死亡） |
| **Pain level（类别形式）** | None / Mild / Moderate / Severe |
| **Investigator / Patient Global Impression（CGI-I、PGI-C）** | Very much improved … Very much worse |
| **Likert scale 问卷题** | Strongly disagree → Strongly agree |
| **WHO COVID-19 ordinal scale** | 从未住院到机械通气到死亡，共 8–11 级 |

以 CTCAE grade 为例：Grade 3 肯定比 Grade 2 严重，但不能说 Grade 4 是 Grade 2 的"两倍严重"，也不能说 2→3 的差距等于 3→4 的差距。

> 补充（Claude）：WHO 的 COVID-19 量表有过不止一个版本。早期的 ordinal scale for clinical improvement 约 8–9 级，2020 年发布的 WHO Clinical Progression Scale 为 0–10 共 11 级，所以材料写"8–11 级"。版本细节待 Li 核实。

## 分析上的影响

### 描述统计

用 **n (%) by category**，而不是 mean (SD)。例如 AE summary table 按**最严重等级（max severity）**计数。

### 组间比较

| 方法 | 说明 |
|---|---|
| **CMH 检验**（row mean scores） | 可按分层因素调整 |
| **Wilcoxon rank-sum**（Mann-Whitney U） | 基于秩次，见 [CON-test-selection](CON-test-selection.md#mann-whitney-u-检验wilcoxon-秩和检验)、[CON-parametric-vs-nonparametric](CON-parametric-vs-nonparametric.md) |
| **Proportional odds model**（ordinal logistic regression） | mRS、WHO ordinal scale 这类**主要终点**常用 |

**CMH 用哪个统计量**：治疗组是无序行、应答是有序列，所以看 **Row Mean Scores Differ**。分层时用 `scores=modridit`，就是 van Elteren 检验（分层 Wilcoxon）。三个统计量怎么选、`SCORES=` 各选项、代码与注意事项见 [CON-CMH](CON-CMH.md)。

> 这一点最初是 Claude 的补充，后续对话（cmh_statistics.md）确认了"说法准确"，并给出了完整的选择逻辑。示例代码原来写的 `avaln` 已更正为 `aval`，详见 CON-CMH 的更正记录。

**Proportional odds model** 给出一个**共同 OR**，比例优势假设需要检验。模型本身和 SAS / R 实现见 [CON-proportional-odds-model](CON-proportional-odds-model.md)；SAS 默认方向与 R 相反、OR 会互为倒数，见 [GOT-ordinal-or-direction](../gotchas/GOT-ordinal-or-direction.md)。

> 这几点最初是 Claude 的补充，后续对话（proportional_odds.md）确认了"都对"，并补充了细节。

### ADaM 中的存储

分两种情况：

| 情况 | 变量 | 说明 |
|---|---|---|
| **原生就是 ordinal 的参数**（如 mRS、ECOG、CGI-I） | `AVAL`（Num）+ `AVALC`（Char） | `AVALC` 存文字类别，`AVAL` 存对应的有序数字编码，**两者必须一一对应**。这样就够了 |
| **从 `AVAL` 再派生分类**（如把 eGFR 切成 CKD 分期） | `AVALCATy`（Char）+ `AVALCAyN`（Num），y = 1, 2, … | `AVALCAyN` 用来保证排序。注意变量名是 `AVALCA1N`，不是 `AVALCAT1N`，这是为了遵守 8 字符的限制 |

TLF 里按 `AVAL` 或 `AVALCAyN` 排序，类别就能按自然顺序显示。

> 更正记录（2026-11-12）：ordinal_data.md 原文写"用 `AVALCAT` / `AVALN` 等保持排序"。Claude 在后续对话中更正：`AVALN` 不是 BDS 标准变量（`AVAL` 本身就是数值型），`AVALCAT` 也漏了编号 y。上表按更正后的说法写（来源：inbox/archive/20261112_ordinal_data_adam_correction.md）。具体以 ADaMIG 和项目规格为准，待 Li 核实。

## 容易混淆：多级总分量表

**总分形式的量表**，如 HAM-D 总分（0–52）、0–10 NRS 疼痛评分，严格来说也是 ordinal。但因为级数多，实际中常被**当作 continuous 处理**，用 [MMRM](CON-MMRM.md) / ANCOVA（见 [CON-covariate](CON-covariate.md)）分析。这在统计上是惯例接受的近似。

> ⚠ 存在分歧（轻微）：[CON-test-selection](CON-test-selection.md) 把"疼痛 VAS 评分"列为 Mann-Whitney 的常见场景，即当作有序评分做非参数检验。本材料则说，0–10 NRS 这类多级疼痛评分实际中常当作连续变量，用 MMRM / ANCOVA 分析。两处说的量表不完全相同（VAS 是 0–100 mm 连续刻度，NRS 是 11 级整数）。哪种做法作为默认、在什么条件下改用非参数方法，待 Li 裁定。

## 相关卡片

- [CON-test-selection](CON-test-selection.md)：Mann-Whitney 用于有序评分
- [CON-parametric-vs-nonparametric](CON-parametric-vs-nonparametric.md)：秩次方法不怕等级数据
- [CON-confirmatory-methods-overview](CON-confirmatory-methods-overview.md)：CMH、logistic、Wilcoxon 在确证性试验中的位置
- [CON-MMRM](CON-MMRM.md)：多级总分量表当作连续变量分析

## 出处

- Claude 对话（inbox: ordinal_data.md；AI 生成，原始出处待补）
