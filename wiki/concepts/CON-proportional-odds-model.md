---
id: CON-proportional-odds-model
title: "比例优势模型（Proportional Odds Model / Ordinal Logistic Regression）"
categories: [ordinal, logistic, proportional-odds, cumulative-logit, odds-ratio, partial-proportional-odds, sas, proc-logistic, r, polr, clm]
related: [CON-ordinal-data, GOT-ordinal-or-direction, CON-CMH, CON-confirmatory-methods-overview, CON-covariate]
sources: ["Claude 对话（inbox: ordinal_data.md）", "Claude 对话（inbox: proportional_odds.md）"]
status: draft
updated: 2026-11-12
---

> 出处待补：本卡内容来自 Claude 对话（inbox: ordinal_data.md 与 proportional_odds.md），属 AI 生成内容，未引用原始文献。R 中的参数化方向已由 Claude 在 R 4.5.2 中用 `MASS::polr` 复核；本机未安装 `ordinal` 包，`clm` 相关代码未实际运行。

## 是什么

有序应答（如 mRS、WHO ordinal scale，见 [CON-ordinal-data](CON-ordinal-data.md)）的回归模型。它对**累积概率**建模：

logit P(Y ≤ k) = α_k + βx，k = 1, …, K − 1

- 每个切点 k 有自己的截距 α_k。
- **所有切点共用一个 β**，这就是"比例优势"假设。
- exp(β) 是一个**共同 OR**：不管在哪个切点把类别一分为二，治疗组"处于更低（或更高）类别"的 odds 之比都相同。

mRS、WHO ordinal scale 这类**主要终点**常用这个模型。方向怎么读是最容易出错的地方，见 [GOT-ordinal-or-direction](../gotchas/GOT-ordinal-or-direction.md)。

## 比例优势假设的检验

- **SAS**：响应变量有序时，`PROC LOGISTIC` 会**自动输出 Score Test for the Proportional Odds Assumption**，不需要额外加选项。
- **R**：`ordinal::nominal_test()`。
- **不能只看 p 值**：这个 score test 在大样本时很容易显著，格子稀疏时又不太可靠。
- **常见的补充做法**：在每个切点分别拟合二分类 logistic，看几个 OR 是否大致接近。

### 假设不成立时：partial proportional odds model

| 软件 | 写法 |
|---|---|
| SAS | `UNEQUALSLOPES` 选项 |
| R | `clm()` 的 `nominal =` 参数 |

## 实现

### R

- 响应变量必须是 **`ordered` factor**，levels 的顺序要正确。
- `MASS::polr` 要设置 **`Hess = TRUE`**，否则 `summary()` 会重新拟合模型来计算标准误。
- `ordinal::clm` 功能更全，支持 nominal effect；需要随机效应时用 `clmm`。

```r
library(ordinal)
adeff$AVALF <- factor(adeff$AVAL, levels = 0:6, ordered = TRUE)
fit <- clm(AVALF ~ TRT01P + STRATA, data = adeff, link = "logit")
nominal_test(fit)   # 检验比例优势假设
exp(-coef(fit)["TRT01PDrug"])  # 转换成 SAS 默认方向的 OR
```

> ⚠ 待核实（代码，Claude 用 `polr` 实际运行）：`TRT01P` 是字符变量时，R 按字母顺序把 **"Drug" 设为参照组**，系数名是 `TRT01PPlacebo`，所以 `coef(fit)["TRT01PDrug"]` 返回 **NA**。要先把安慰剂设为参照组：
>
> ```r
> adeff$TRT01P <- relevel(factor(adeff$TRT01P), ref = "Placebo")
> ```
>
> 之后上面最后一行才能取到 Drug vs Placebo 的系数。

### SAS

> 补充（Claude）：示意写法如下，待 Li 核实。
>
> ```sas
> proc logistic data=adeff;
>   class trt01p(ref="Placebo") strata / param=ref;
>   model aval = trt01p strata;   /* aval 多于两个取值时自动拟合累积 logit 模型 */
>   oddsratio trt01p;
> run;
> ```
>
> 先看输出 Response Profile 下面的建模方向说明，再读 OR（见 [GOT-ordinal-or-direction](../gotchas/GOT-ordinal-or-direction.md)）。

## 相关卡片

- [CON-ordinal-data](CON-ordinal-data.md)：有序数据是什么，还有哪些分析方法
- [GOT-ordinal-or-direction](../gotchas/GOT-ordinal-or-direction.md)：SAS 默认方向和 R 参数化相反，OR 会互为倒数
- [CON-CMH](CON-CMH.md)：另一种做法，不建模的分层检验
- [CON-covariate](CON-covariate.md)：分层因素和基线作协变量

## 出处

- Claude 对话（inbox: ordinal_data.md、proportional_odds.md；AI 生成，原始出处待补）
