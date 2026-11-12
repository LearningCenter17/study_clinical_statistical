<!-- 来源：Li 粘贴的 Claude 对话回复（2026-11-12），确认 CON-ordinal-data 中关于 proportional odds model 的三点补充（假设检验、SAS 方向、R 包），并展开细节。已合并进 CON-proportional-odds-model（新建）与 GOT-ordinal-or-direction（新建）。 -->

这三点都对，我补充几个细节，这样写卡片时更完整。

**1. 比例优势假设的检验**

- SAS 的 `PROC LOGISTIC` 在响应变量是有序的时候，会**自动输出 Score Test for the Proportional Odds Assumption**，不需要额外加选项。
- 这个 score test 在大样本时很容易显著，在稀疏格子时又不太可靠，所以不能只看 p 值。常见的补充做法是在每个切点分别拟合二分类 logistic，看几个 OR 是否大致接近。
- 如果假设不成立，可以用 partial proportional odds model：SAS 用 `UNEQUALSLOPES` 选项，R 用 `clm()` 的 `nominal =` 参数。

**2. SAS 的方向问题**

- 默认模型是 logit P(Y ≤ k) = α_k + βx，也就是对较低的有序值累积建模。输出的 Response Profile 下面会注明 "Probabilities modeled are cumulated over the lower Ordered Values"，**每次都应该看一下这行**。
- 加 `DESCENDING` 后改为对 P(Y ≥ k) 建模。
- 是否需要 `descending`，要看哪一端是"好"的结局。比如 mRS 越低越好，默认方向下 OR > 1 表示治疗组更倾向于低分，也就是更好的结局。所以**不是一律加 descending**，而是先确定编码方向，再确定 OR 如何解读。

**3. R 的参数化正好和 SAS 默认相反**

- `MASS::polr` 和 `ordinal::clm` 都用 logit P(Y ≤ k) = θ_k − βx，**β 前面是减号**。所以 β > 0 表示更倾向于较高的类别。
- 因此，R 的 `exp(coef)` 方向对应的是 SAS 加了 `DESCENDING` 之后的 OR。做 SAS 和 R 双重编程 QC 时，这里最容易出现"OR 互为倒数"的差异。
- 实际使用时要注意：
  - 响应变量必须是 `ordered` factor，并且 levels 的顺序要正确。
  - `polr` 需要设置 `Hess = TRUE`，否则 `summary()` 会重新拟合模型来计算标准误。
  - `clm` 的功能更全，支持 nominal effect；需要随机效应时可以用 `clmm`。

```r
library(ordinal)
adeff$AVALF <- factor(adeff$AVAL, levels = 0:6, ordered = TRUE)
fit <- clm(AVALF ~ TRT01P + STRATA, data = adeff, link = "logit")
nominal_test(fit)   # 检验比例优势假设
exp(-coef(fit)["TRT01PDrug"])  # 转换成 SAS 默认方向的 OR
```
