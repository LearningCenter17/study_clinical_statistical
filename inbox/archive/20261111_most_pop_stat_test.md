下面是确证性临床试验里最常见的十种方法。排序是根据行业惯例给的大致印象，不是统计出来的排名，不同治疗领域的侧重点会不一样。

| # | 方法 | English | 终点类型 | 典型用途 |
|---|---|---|---|---|
| 1 | 协方差分析 | ANCOVA | 连续 | 单个时间点的主要终点，调整基线和分层因素（如第 24 周 HbA1c 变化） |
| 2 | 混合效应重复测量模型 | MMRM | 连续 · 多访视 | 有脱落的多访视终点（如抑郁量表、肺功能） |
| 3 | Kaplan-Meier 法 | Kaplan-Meier | 时间-事件 | 生存曲线、中位 OS / PFS |
| 4 | Log-rank 检验 | Log-rank test | 时间-事件 | 肿瘤试验 OS / PFS 主要终点的检验 |
| 5 | Cox 比例风险模型 | Cox PH model | 时间-事件 | 风险比（HR）及 95% CI |
| 6 | CMH 检验 | Cochran-Mantel-Haenszel | 二分类 | 分层比较应答率（如 PASI 75、ACR20） |
| 7 | Logistic 回归 | Logistic regression | 二分类 | 调整协变量后的比值比（OR） |
| 8 | Fisher 确切概率法 | Fisher's exact test | 二分类 | 小样本、AE / SAE 发生率比较 |
| 9 | 卡方检验 | Chi-square test | 分类 | 大样本时的率比较、基线特征比较 |
| 10 | Wilcoxon 秩和检验 | Wilcoxon rank-sum / Mann-Whitney U | 连续 / 有序 | 偏态数据、敏感性分析 |

## 紧随其后的几个

- **负二项回归**：呼吸领域的急性加重率，在那里基本是标准方法
- **Clopper-Pearson 精确置信区间**：单臂肿瘤试验 ORR 的标配
- **率差置信区间（Miettinen-Nurminen / Newcombe）**：非劣效试验、疫苗试验
- **t 检验**：教科书里最常见，但在注册试验的主分析中通常被 ANCOVA 取代

## 两个实际观察

**1. 描述统计才是工作量最大的部分。** 按 TLF 数量算，绝大多数表格是 n、均值、SD、中位数、Q1/Q3、最小值/最大值，以及频数和百分比，例如人口学、基线特征、AE 汇总、实验室检查、生命体征。真正做假设检验的表只占一小部分。

**2. 按领域划分，常用的方法其实很集中：**

| 领域 | 核心方法 |
|---|---|
| 肿瘤 | KM、log-rank、Cox、Clopper-Pearson |
| 代谢 / 心血管指标 | ANCOVA、MMRM |
| 免疫 / 皮肤 | CMH、logistic、非应答者填补 |
| 呼吸 | 负二项回归、MMRM |
| 安全性（所有领域） | 描述统计，偶尔用 Fisher |

对统计程序员来说，先把前五个方法的 R 和 SAS 结果对齐练熟（ANCOVA 的 LS mean、MMRM 的 KR 自由度、KM 的中位数 CI、Cox 的 ties 处理），就能覆盖大部分推断统计表的工作。