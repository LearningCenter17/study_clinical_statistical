---
id: CON-response-rate
title: "应答、应答概率与应答率（Response, Response Probability, Response Rate）"
categories: [binary-endpoint, response, response-rate, responder, orr, binomial, estimation, confidence-interval, adam, adrs, asas40]
related: [CON-distribution-family, CON-confidence-interval, CON-ordinal-data, MTH-CMH, CON-test-statistic, CON-confirmatory-methods-overview, CON-estimand, CON-test-selection, CON-sample-size-power, CON-unequal-allocation]
sources: ["Claude 对话（inbox: response_rate.md）", "Claude 对话（inbox: response_rate_recist_correction.md）", "Claude 对话（inbox: calculcate_sample_size.md）"]
status: draft
updated: 2026-11-17
---

> 出处待补：本卡内容来自 Claude 对话（inbox: response_rate.md、response_rate_recist_correction.md、calculcate_sample_size.md），属 AI 生成内容，未引用原始文献。示例 CI 已由 Claude 在 R 4.5.2 中复核（见下文）。

## 一句话定义

**应答（response）**：病人用药后，病情改善达到了**事先规定的标准**。每个病人最后只有两种结果：**应答（1）** 或 **未应答（0）**，所以应答是一个**二分类终点**。

- **应答概率（response probability，p）**：一个病人用了这个药后发生应答的可能性。它是**总体的真实值**，固定但不知道。
- **应答率（response rate，p̂）**：试验里**实际观察到的**比例 = 应答人数 ÷ 总人数，用来估计 p。

## 应答标准因疾病而异

| 领域 | 应答标准举例 |
|---|---|
| 实体瘤 | RECIST 评估为 CR（完全缓解）或 PR（部分缓解） |
| 类风湿关节炎 | ACR20：关节症状改善 ≥ 20% |
| 银屑病 | PASI 75：皮损评分改善 ≥ 75% |
| 抑郁症 | 量表评分较基线下降 ≥ 50% |
| 中轴型脊柱关节炎（含强直性脊柱炎） | ASAS40：ASAS 评估的 4 个方面中至少 3 个改善 ≥ 40%（且绝对值改善至少 2 分），其余方面没有恶化（来源：calculcate_sample_size.md） |

表中都是简化说法。ACR20、PASI 75 等的完整定义要看各自的评估标准和 SAP（来源：response_rate_recist_correction.md）。

RECIST 的 CR / PR / SD / PD 本身是有序分类，见 [CON-ordinal-data](../ordinal/CON-ordinal-data.md)。把它切成"CR 或 PR = 应答"后才变成二分类。

### RECIST 1.1：PR 和 CR 不只看靶病灶

PR 要**同时**满足三个条件：

| 条件 | 要求 |
|---|---|
| ① 靶病灶 | 直径总和比**基线**缩小 **≥ 30%** |
| ② 非靶病灶 | 不能进展（评估为 Non-CR/Non-PD 或未评估） |
| ③ 新病灶 | **不能出现**新病灶 |

非靶病灶明确进展，或出现新病灶时，即使靶病灶缩小了 50%，这次评估的总体结果也是 **PD**。

**CR** 更严格：所有靶病灶和非靶病灶全部消失，病理淋巴结短径 < 10 mm，并且没有新病灶。

### 确认（confirmation）

单次评估达到 CR 或 PR 还不算最终的应答，还要后续评估**确认**：

- 通常要求**间隔 ≥ 4 周**的下一次评估仍是 CR 或 PR，才算"确认的应答"（confirmed response）。
- RECIST 1.1：**单臂试验**中应答是主要终点时，必须确认；**随机对照试验**中 RECIST 本身不强制确认，但很多方案仍会要求。

具体按哪种规则，以方案和 SAP 为准。

> 更正记录（2026-11-16）：response_rate.md 的通俗例子原文写"肿瘤缩小 30% 以上就算应答"。后续对话（response_rate_recist_correction.md）确认这个说法过于简化，已按上面的三个条件和确认规则改写。RECIST 细节以 RECIST 1.1 原文为准，待 Li 核实。

## 真实值 vs 估计值

和 μ、σ 一样，p 是总体参数：

| | 真实值（总体） | 估计值（样本） |
|---|---|---|
| 符号 | **p** | **p̂**（p-hat） |
| 含义 | 这个药对这类病人的真实应答概率 | 试验里实际观察到的应答率 |
| 能否知道 | 不知道 | 能算：应答人数 ÷ 总人数 |

例：Drug 组 60 人，27 人应答：

$$
\hat{p} = \frac{27}{60} = 45\%
$$

换一批病人重做，可能是 42%，也可能是 48%，所以要给它配一个 CI，比如 **45%（95% CI：32%，58%）**。CI 的含义见 [CON-confidence-interval](../../inference/CON-confidence-interval.md)。

> 数值复核（Claude，R 4.5.2）：27/60 的 Wald CI = 32.4%–57.6%；Clopper-Pearson 精确 CI（`binom.test(27, 60)`）= 32.1%–58.4%。两者取整后都约为 32%–58%。材料没说用的是哪种方法。单臂试验 ORR 通常报 Clopper-Pearson（见 [CON-confirmatory-methods-overview](../CON-confirmatory-methods-overview.md)），各 CI 方法的对比待建卡片。

## 抛硬币类比与模拟

每个病人就像抛一次**不均匀的硬币**，正面朝上（应答）的概率是 p。药效越好，p 越大。这就是伯努利试验；n 个病人的应答人数服从二项分布 Binomial(n, p)，见 [CON-distribution-family](../../inference/CON-distribution-family.md)。

| | 抛硬币 | 病人用药 |
|---|---|---|
| 每次的结果 | 正面 / 反面 | 应答 / 不应答 |
| 概率 | 正面的概率 = 50% | 应答的概率 = p |
| 例子 | 一枚均匀的硬币 | p = 40% 的药 |

R 中模拟一次试验：

```r
x <- rbinom(1, n, p)   # n 个病人，每人以概率 p 应答，数一共几人应答
```

- `p = 0.05`：每个病人只有 5% 的机会应答，如疗效很弱的药或罕见事件
- `p = 0.30`：每个病人有 30% 的机会应答

模拟时 p 由我们设定，所以能检查 CI 有没有套住它。现实中 p 不知道，所以才要做试验、算 CI 来估计。

## 同样适用于不良事件

把"应答"换成"发生某种不良事件"，p 就是**不良事件的发生概率**。AE 汇总表里的发生率及其 CI，计算方法相同。

## 中英文术语

| 中文 | 英文 | 说明 |
|---|---|---|
| 应答概率 | **response probability** / probability of response | 真实的 p，多用在统计方法、SAP 中 |
| 应答率 | **response rate** | 试验中观察到的比例 p̂，TLF 里最常见 |
| 客观缓解率 | **ORR**（Objective Response Rate） | 肿瘤试验的标准说法 |
| 应答者 | **responder** | 达到应答标准的病人 |
| 应答者分析 | **responder analysis** | 按应答 / 未应答做的分析 |

实际文档里 **response rate** 用得最多。即便统计上指真实概率，SAP 和 CSR 里通常也写作 "true response rate"。

## ADaM 中的存储

肿瘤试验的 ADRS 里，上面几层判断一般分成不同参数（来源：response_rate_recist_correction.md）：

| PARAMCD（示例） | 含义 |
|---|---|
| `OVRLRESP` | 每次访视的总体评估（综合靶病灶、非靶病灶和新病灶） |
| `BOR` | 最佳总体应答（未确认） |
| `CBOR` | 确认的最佳总体应答 |

**ORR 通常基于确认的 BOR**：CR 或 PR 的人数 ÷ 分析人群人数。

```r
adrs |>
  filter(PARAMCD == "CBOR") |>              # 用确认的 BOR，而不是单次评估
  ...
  summarise(n_resp = sum(AVALC %in% c("CR", "PR")))
```

PARAMCD 的名称各公司不同（如 `BESTRSP`、`CBESTRSP`），以项目的 ADaM 规格书或 define.xml 为准。

> 补充（Claude）：分母是**分析人群的全部受试者**。没有 CBOR 记录或 BOR = NE 的人也要算在分母里，算作未应答。如果直接在 ADRS 上 `n()` 计数，这些人会漏掉，ORR 会偏高。所以通常先从 ADSL 取分析人群，再 left join CBOR。待 Li 结合 SAP 核实。

> 更正记录（2026-11-16）：response_rate.md 原文写"应答结果一般存在 ADRS 中，用 `AVALC = "Y"/"N"` 或 0/1 表示"。Claude 首次收录时已指出，肿瘤 ADRS 的 BOR `AVALC` 通常是 CR / PR / SD / PD / NE。后续对话（response_rate_recist_correction.md）给出了上面的参数结构，已替换。非肿瘤领域（ACR20、PASI 75）的应答常放在 ADEFF 等 BDS 数据集，可能用 Y/N 或 `CRITy` / `CRITyFL` 表示（Claude 补充，与 [CON-test-statistic](../../inference/CON-test-statistic.md) 一致）。待 Li 核实。

## 两组比较去哪里看

- 2×2 表比较两组应答率：卡方 / Fisher，见 [CON-test-selection](../../inference/CON-test-selection.md)
- 分层比较（如 PASI 75、ACR20）：CMH，见 [MTH-CMH](MTH-CMH.md)（二分类部分待补）
- 停药等伴发事件记为"无应答"属于 composite strategy，见 [CON-estimand](../../estimand/CON-estimand.md)

## 相关卡片

- [CON-distribution-family](../../inference/CON-distribution-family.md)：伯努利 → 二项
- [CON-confidence-interval](../../inference/CON-confidence-interval.md)：CI 的解读
- [CON-ordinal-data](../ordinal/CON-ordinal-data.md)：RECIST 应答等级是有序分类
- [CON-confirmatory-methods-overview](../CON-confirmatory-methods-overview.md)：ORR 的 Clopper-Pearson CI

## 出处

- Claude 对话（inbox: response_rate.md；AI 生成，原始出处待补）
- Claude 对话（inbox: response_rate_recist_correction.md；AI 生成，原始出处待补）
- Claude 对话（inbox: calculcate_sample_size.md；AI 生成，原始出处待补）
- 建议对照：RECIST 1.1（Eisenhauer et al., Eur J Cancer 2009）；CDISC ADaMIG 及 ADaM 肿瘤示例
