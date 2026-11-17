---
id: CON-hazard-ratio
title: "风险比（Hazard Ratio, HR）"
categories: [survival, hazard-ratio, cox, log-rank, null-hypothesis]
related: [CON-null-hypothesis, CON-p-value, GOT-ni-hypothesis-direction, CON-logrank-vs-cox, CON-sample-size-power, CON-confidence-interval, CON-confirmatory-methods-overview]
sources: ["Claude 对话（inbox: h0_hr.md）", "Claude 对话（inbox: logrank_vs_cox.md）", "Claude 对话（inbox: CI_HR.md）", "Claude 对话（inbox: CI_HR_rounding.md）"]
status: draft
updated: 2026-11-16
---

> 出处待补：本卡内容来自 Claude 对话（inbox: h0_hr.md、CI_HR.md、CI_HR_rounding.md），属 AI 生成内容，未引用原始文献。

## 一句话定义

**HR（hazard ratio，风险比）是两组风险之比**，用在生存分析（比较"多久发生某事件"）中：

$$
HR = \frac{\text{新药组的风险}}{\text{对照组的风险}}
$$

"风险"（hazard）可通俗理解为：**一个还没出事的人，在接下来这一刻出事的可能性**。"出事"指试验关注的事件，如死亡、心梗、肿瘤进展。

更准确地说（来源：CI_HR.md）：hazard 是"**在时间 t 还没发生事件的人当中，下一瞬间发生事件的速率**"。HR = 0.72 的意思是：在**任何时间点**，治疗组仍处于风险中的人发生事件的瞬时速率，是对照组的 72%。

## HR 的三种情况

| HR | 含义 | 通俗说法 |
|---|---|---|
| **= 1** | 两组风险一样 | 药没作用 |
| **< 1** | 新药组风险更低 | 新药有保护作用 |
| **> 1** | 新药组风险更高 | 新药反而有害 |

所以生存分析中 **H₀ 写作 HR = 1**（"两组风险相同、新药没效果"），和连续变量里"均值差 = 0"是同一个意思。之所以是 1 而不是 0：两个相同的数相除得 1，相减才得 0。见 [CON-null-hypothesis](CON-null-hypothesis.md#不同终点的-h₀)。

## 例子：心血管试验（新药 vs 安慰剂，终点心梗）

- **HR = 0.7**：任何时刻，新药组发生心梗的风险只有安慰剂组的 70%，即**风险降低 30%**。
- **HR = 1.0**：两组风险一样。
- **HR = 1.5**：新药组风险是安慰剂组的 1.5 倍，**风险升高 50%**。

## 为什么在 log 尺度上分析

理解 HR 的关键一句话：**对 HR 取 log 之后，它就和"差值"一模一样了**（来源：CI_HR.md）。

| | HR | log(HR) |
|---|---|---|
| 本质 | 比值 | log(h₁) − log(h₀)，**本身就是差值** |
| 无效值 | **1** | **0** |
| 取值范围 | (0, ∞)，左右不对称：HR = 0.5 与 HR = 2 效应大小相同，但离 1 的距离不同 | (−∞, +∞)，左右对称：log(0.5) = −0.69，log(2) = +0.69 |
| 抽样分布 | 偏态，不接近正态 | 近似正态 |

所以 Cox 模型直接估计的是 **β = log(HR)** 及其标准误 **SE(β)**，CI 和检验都在 log 尺度上做。

## 算例：HR 的 CI 与 Wald P 值

β = −0.3285，SE = 0.109：

1. **log 尺度**：−0.3285 ± 1.96 × 0.109 → (−0.543, −0.115)
2. **取 exp**：**HR = 0.72，95% CI (0.58, 0.89)**
3. **Wald 检验**（Cox 模型自带）：z = β / SE = −0.3285 / 0.109 ≈ −3.0，p ≈ 0.003。逻辑和均值差的检验一样：估计值离 0 有几个 SE。

这个 CI **不以 0.72 为中心**：0.72 − 0.58 = 0.14，0.89 − 0.72 = 0.17。HR 的 CI 本来就不对称，因为它只在 log 尺度上对称。

> 数值复核（Claude，R 4.5.2）：exp 后为 0.7200 (0.5815, 0.8915)；z = −3.01，p = 0.0026，与材料一致。log 尺度下限 −0.5421（材料 −0.543 为舍入差）。

### TLF QC：log 尺度等距，但要考虑四舍五入

理论上 log(下限)、log(HR)、log(上限) 三者**等距**，两段距离都等于 1.96 × SE。但 TLF 上印的是**四舍五入到两位小数**的值，直接取 log 会有轻微偏差（来源：CI_HR_rounding.md）：

| | 值 | log 值 |
|---|---|---|
| 下限 | 0.58 | −0.5447 |
| HR | 0.72 | −0.3285 |
| 上限 | 0.89 | −0.1165 |

两段距离 0.216 与 0.212，相差 0.004。每个数的舍入误差最大 ±0.005，取 log 后两段就不完全相等。**这时不要误判成程序出错。**

QC 做法：

1. **用未四舍五入的数检查等距**：从 `coxph` 结果直接取 `coef`、`se(coef)`，或从中间数据集取全精度值。这时应该完全相等。
2. **只看 TLF 上的数时，允许一点误差**：两段距离差个零点零几是正常的；差得很大才说明有问题，比如 CI 根本不是在 log 尺度上算的。
3. **更稳妥：反过来算**。用全精度的 β 和 SE 自己算 exp(β ± 1.96 × SE)，四舍五入到两位小数后，和 TLF 上的数逐个比对。

> 更正记录（2026-11-16）：CI_HR.md 只说"三者应该等距"，没提舍入。Claude 收录时补充了舍入问题，后续对话（CI_HR_rounding.md）确认并给出上述 QC 做法。
>
> 补充（Claude）："零点零几"的容差和 HR 大小有关：log 的舍入误差约为 0.005 / 数值本身，所以数值越小误差越大。例如下限为 0.10 时，±0.005 在 log 尺度上约为 ±0.05。HR 或 CI 端点很小时，做法 1 或 3 更可靠。待 Li 核实。

CI 构造的一般规则（不同统计量用 t 还是 z、为什么 HR 用 1.96）见 [CON-confidence-interval](CON-confidence-interval.md#不同统计量的-ci-构造方法)。HR 的 CI 宽度几乎只取决于**事件数**（1:1 随机时 SE(log HR) ≈ 2/√D），见 [CON-confidence-interval](CON-confidence-interval.md#生存终点看事件数)。

## 怎么读报告

> HR = 0.70（95% CI: 0.58–0.85），P < 0.001

- 点估计 0.70 → 风险降低约 30%；
- 95% CI **不包含 1** → 和"没效果"有显著差别，P 值很小；
- 如果 CI 跨过 1（如 0.85–1.10）→ 不能排除"没效果"，P 值会大于 0.05。

## 常见坑

HR = 0.7 **不等于**"新药组出事的人少 30%"。HR 比较的是**每一时刻的风险**，最终出事人数的比例还取决于随访时间长短等因素。不过日常交流中"风险降低 30%"的说法是可以接受的。

**比例风险假设**：HR 的解释里"任何时间点"背后就是比例风险（proportional hazards）假设，即 HR 不随时间变化。如果两条 KM 曲线交叉，这个假设站不住，单个 HR 的解释力会下降（来源：CI_HR.md）。

> 补充（Claude）：PH 不成立时，单一 HR 只是某种时间平均，解读需谨慎；PH 检查方法见 [CON-logrank-vs-cox](CON-logrank-vs-cox.md#临床试验中的常见做法)。（此条最初是 Claude 补充，CI_HR.md 确认了"KM 曲线交叉 → PH 站不住"这一点。）

## 实现

SAS 中一般用 `PROC PHREG`（Cox 回归）估计 HR 及 95% CI，用 `PROC LIFETEST` 做 log-rank 检验给 P 值。两者的 H₀、分工和 SAS / R 代码见 [CON-logrank-vs-cox](CON-logrank-vs-cox.md#实现)。

R `summary(coxph(...))` 输出列与本卡概念的对应：

| 输出列 | 含义 |
|---|---|
| `coef` | β = log(HR) |
| `exp(coef)` | HR |
| `se(coef)` | SE(β) |
| `lower .95` / `upper .95` | HR 的 95% CI（已经取过 exp） |
| `Pr(>\|z\|)` | Wald P 值 |

> 更正记录：原始材料（h0_hr.md）称 PHREG 和 LIFETEST "检验的都是 HR 是否等于 1"。后续 Claude 对话（logrank_vs_cox.md）更正为：**PHREG 检验的是 HR = 1；log-rank 检验的是两组生存曲线相同，不估计 HR，只在比例风险假设下与 Cox 的 score 检验等价。**

## 相关卡片

- [CON-confidence-interval](CON-confidence-interval.md)：CI 与 P 值的对应关系、CI 构造方法、事件数决定 CI 宽度
- [CON-null-hypothesis](CON-null-hypothesis.md)
- [CON-p-value](CON-p-value.md)：log-rank 统计量作为检验统计量的例子
- [CON-logrank-vs-cox](CON-logrank-vs-cox.md)：log-rank 与 Cox 的分工

## 出处

- Claude 对话（inbox: h0_hr.md；AI 生成，原始出处待补）
- Claude 对话（inbox: logrank_vs_cox.md；AI 生成，原始出处待补）
- Claude 对话（inbox: CI_HR.md；AI 生成，原始出处待补）
- Claude 对话（inbox: CI_HR_rounding.md；AI 生成，原始出处待补）
