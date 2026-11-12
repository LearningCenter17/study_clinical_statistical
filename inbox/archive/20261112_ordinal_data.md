**Ordinal data（有序分类数据）** 是指类别之间有**自然的顺序**，但相邻类别之间的**间距不一定相等**、也没有实际数值意义的数据。

判断标准可以拆成两条：
1. **能排序**：A < B < C 有意义（这点区别于 nominal，比如血型、性别）
2. **不能做算术**：从 1 到 2 的"距离"不一定等于从 2 到 3（这点区别于 interval/ratio，比如体重、血压）

所以即使你把它编码成 1, 2, 3, 4，这些数字也只代表顺序，算平均值在理论上是有问题的。

**临床试验中常见的例子**

| 例子 | 类别 |
|---|---|
| **AE severity (CTCAE grade)** | Grade 1 Mild → 2 Moderate → 3 Severe → 4 Life-threatening → 5 Death |
| **Tumor response (RECIST)** | CR > PR > SD > PD |
| **modified Rankin Scale (mRS)**，卒中试验 | 0（无症状）到 6（死亡） |
| **ECOG performance status** | 0–4（加上 5 = 死亡） |
| **Pain level（类别形式）** | None / Mild / Moderate / Severe |
| **Investigator/Patient Global Impression (CGI-I, PGI-C)** | Very much improved … Very much worse |
| **Likert scale 问卷题** | Strongly disagree → Strongly agree |
| **WHO COVID-19 ordinal scale** | 从未住院到机械通气到死亡，共 8–11 级 |

拿 CTCAE grade 举例：Grade 3 肯定比 Grade 2 严重，但不能说 Grade 4 是 Grade 2 的"两倍严重"，也不能说 2→3 的差距等于 3→4 的差距。

**分析上的影响**
- 描述性统计通常用 **n (%) by category**，而不是 mean (SD)。比如 AE summary table 按 max severity 计数。
- 组间比较常用 **Cochran-Mantel-Haenszel (CMH) test**（row mean scores）、**Wilcoxon rank-sum**，或 **proportional odds model**（ordinal logistic regression）。mRS、WHO ordinal scale 这类 primary endpoint 经常用 proportional odds model。
- 在 ADaM 里，通常会同时存 `AVALC`（文字类别）和 `AVAL`（数字编码），并用 `AVALCAT`/`AVALN` 等保持排序，方便 TLF 里按顺序显示。

**一个容易混淆的情况**：总分形式的量表（比如 HAM-D 总分 0–52，或 0–10 NRS 疼痛评分）严格来说也是 ordinal，但因为级数多，实际中常被当作 continuous 处理并用 MMRM/ANCOVA 分析。这在统计上属于惯例接受的近似。