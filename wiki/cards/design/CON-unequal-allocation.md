---
id: CON-unequal-allocation
title: "不等分配（k:1）的样本量（Unequal Allocation）"
categories: [sample-size, unequal-allocation, allocation-ratio, binary-endpoint, survival, continuity-correction, dropout, asas40]
related: [CON-sample-size-power, WF-sample-size-calc, CON-stratified-randomization, CON-response-rate, CON-confidence-interval]
sources: ["Claude 对话（inbox: stratification_example_check.md）", "Claude 对话（inbox: calculcate_sample_size.md）"]
status: draft
updated: 2026-11-17
---

> 出处待补：本卡内容来自 Claude 对话（inbox: stratification_example_check.md、calculcate_sample_size.md），属 AI 生成内容，未引用原始文献。文中数值已由 Claude 在 R 4.5.2 中复核。
>
> 拆分记录（2026-11-17）：本卡内容原为 [CON-sample-size-power](CON-sample-size-power.md) 的"不等分配（k:1）"一节，按"一个知识点一张卡"拆出，内容未改写。1:1 的公式见 [WF-sample-size-calc](WF-sample-size-calc.md)。

## 连续终点

> 补充（Claude）：本节公式由 Claude 补充。材料（stratification_example_check.md）只给出了 2:1 的结果"安慰剂 64、药物 128、共 192"。待 Li 对照教材（如 Chow, Shao & Wang）核实。

药物组 : 安慰剂组 = k : 1 时，**连续终点**较小组（安慰剂组）的人数：

$$n_{\text{小组}} = \left(1 + \frac{1}{k}\right)\frac{(z_{1-\alpha/2} + z_{1-\beta})^2\,\sigma^2}{\Delta^2}, \qquad n_{\text{大组}} = k \cdot n_{\text{小组}}$$

k = 1 时括号内为 2，就回到 1:1 公式（见 [WF-sample-size-calc](WF-sample-size-calc.md#手算一个例子连续终点两组均值比较)）。

**例**（Δ = 5、σ = 10、双侧 α = 0.05、power 90%、2:1）：n小组 = 1.5 × 10.507 × 100 / 25 = 63.04 → **64**，药物组 128，**共 192 人**。这就是 [CON-stratified-randomization](CON-stratified-randomization.md) 中过度分层例子的 192。

## 不等分配的代价

总人数是 1:1 的 (1 + k)² / (4k) 倍。

| 分配 | 总人数倍数 | 本例（未取整的总人数） |
|---|---|---|
| 1:1 | 1 | 168.1 |
| 2:1 | 1.125 | 189.1 |
| 3:1 | 1.333 | 224.2 |

所以 2:1 只多花约 12.5% 的人，常用来让更多受试者接受试验药、积累更多安全性数据；超过 3:1 后效率下降明显。

## 生存终点

Schoenfeld 公式的系数 4 换成 (1 + k)² / k（k = 1 时为 4）：

$$D = \frac{(1+k)^2}{k} \cdot \frac{(z_{1-\alpha/2} + z_{1-\beta})^2}{(\ln HR)^2}$$

这与 HR 的 CI 精度 SE(log HR) ≈ (1 + k)/√(k·D) 同源，见 [CON-confidence-interval](../inference/CON-confidence-interval.md#生存终点看事件数)。

## 软件

R 的 `power.t.test()`、`power.prop.test()` 只支持等分配，不等分配可以直接按公式算（二分类的函数见下文 ASAS40 算例）；SAS `PROC POWER` 用 `groupweights = (1 2)` 配合 `ntotal = .`。

```r
k  <- 2
z2 <- (qnorm(0.975) + qnorm(0.90))^2
n_small <- ceiling((1 + 1/k) * z2 * 10^2 / 5^2)   # 64
c(placebo = n_small, drug = k * n_small, total = (1 + k) * n_small)
```

> 数值复核（Claude，R 4.5.2）：上面代码输出 64 / 128 / 192。按 t 分布，64 / 128 人的实际 power 为 0.901，达到 90%。SAS `groupweights` 写法未在 SAS 中运行过，待 Li 核实。

## 二分类终点：ASAS40 算例

来源：calculcate_sample_size.md。终点 ASAS40（应答定义见 [CON-response-rate](../methods/binary/CON-response-rate.md#应答标准因疾病而异)），预期应答率安慰剂 p₁ = 20%、药物 p₂ = 45%，双侧 α = 0.05，power 80%，placebo : drug = 1 : 2（k = 2），脱落 15%。

$$n_{\text{pbo}} = \frac{\left[z_{1-\alpha/2}\sqrt{\bar p(1-\bar p)\left(1+\frac{1}{k}\right)} + z_{1-\beta}\sqrt{p_1(1-p_1) + \frac{p_2(1-p_2)}{k}}\right]^2}{(p_2 - p_1)^2}, \qquad \bar p = \frac{p_1 + k\,p_2}{1+k}$$

k = 1 时就是 1:1 的二分类公式（见 [WF-sample-size-calc](WF-sample-size-calc.md#各终点的公式两组11-分配)）。逐步计算：

1. 加权平均率：p̄ = (0.20 + 2 × 0.45) / 3 = 0.3667
2. 分子第一部分：1.96 × √(0.3667 × 0.6333 × 1.5) = 1.96 × 0.5902 = 1.1568
3. 分子第二部分：0.8416 × √(0.20 × 0.80 + 0.45 × 0.55 / 2) = 0.8416 × 0.5327 = 0.4483
4. n_pbo = (1.1568 + 0.4483)² / 0.25² = 2.5763 / 0.0625 = 41.22 → **42**。逐个核算 power：41 人为 79.8%，42 人为 80.8%，所以 42 是满足 80% 的最小人数。
5. 考虑脱落：安慰剂 42 / 0.85 = 49.4 → 50，药物组按比例 50 × 2 = 100。

| | 安慰剂组 | 药物组 | 总人数 |
|---|---|---|---|
| 可评价人数 | 42 | 84 | 126 |
| 考虑 15% 脱落后的入组人数 | 50 | 100 | **150** |

**连续性校正（Fleiss 校正）**：结果更保守，安慰剂约 48、药物 96、共 144 人；考虑脱落后约 57 + 114 = 171 人。**用哪种算法要在方案中写明**，以免核对时出现不同的数字。

```sas
proc power;
  twosamplefreq test=pchi
    groupproportions = (0.20 0.45)   /* 安慰剂组, 药物组 */
    groupweights     = (1 2)
    alpha            = 0.05
    sides            = 2
    power            = 0.80
    ntotal           = .;
run;
```

材料说结果应在 126 人左右，SAS 会自动把总人数取整为符合 1:2 比例的数。

```r
n_2prop <- function(p1, p2, k = 2, alpha = 0.05, power = 0.80) {
  za <- qnorm(1 - alpha/2); zb <- qnorm(power)
  pb <- (p1 + k*p2) / (1 + k)
  n1 <- (za*sqrt(pb*(1-pb)*(1 + 1/k)) +
         zb*sqrt(p1*(1-p1) + p2*(1-p2)/k))^2 / (p2 - p1)^2
  n1 <- ceiling(n1)
  c(placebo = n1, drug = k*n1, total = n1*(1 + k))
}

n <- n_2prop(0.20, 0.45)                  # 42, 84, 126
pbo <- unname(ceiling(n["placebo"] / 0.85))
c(placebo = pbo, drug = 2*pbo, total = 3*pbo)   # 50, 100, 150
```

**方案中可能的写法**：

> 假设安慰剂组和药物组的 ASAS40 应答率分别为 20% 和 45%，采用双侧 α = 0.05 的卡方检验，按 1:2 随机分配，共需 126 例可评价受试者（安慰剂组 42 例，药物组 84 例），可提供 80% 的把握度。考虑 15% 的脱落率，计划入组 150 例（安慰剂组 50 例，药物组 100 例）。

> 数值复核（Claude，R 4.5.2）：n_pbo 原始值 41.22；正态近似 power 41 人 0.798、42 人 0.808；Fleiss 校正 n' = n/4 × [1 + √(1 + 2(k + 1) / (k · n · |p₂ − p₁|))]² = 47.03 → 48，脱落后 48 / 0.85 → 57。以上均与材料一致。材料 R 代码原写 `ceiling(n["placebo"] / 0.85)`，会把名字带进结果（输出显示为 `placebo.placebo`），这里加了 `unname()`，数值不变。SAS 代码未运行，待 Li 核实（与上文 `groupweights` 一并）。
>
> 补充（Claude）：脱落调整的做法是先把**较小组**除以 (1 − 脱落率) 并取整，再按比例乘出大组，这样入组人数严格保持 1:2。若两组分别除以 0.85 再取整（49.4 → 50、98.8 → 99），比例就不再严格是 1:2。待 Li 核实。

## 相关卡片

- [CON-sample-size-power](CON-sample-size-power.md)：power 与样本量的基本概念
- [WF-sample-size-calc](WF-sample-size-calc.md)：1:1 的公式与软件
- [CON-stratified-randomization](CON-stratified-randomization.md)：192 人的例子从这里来
- [CON-response-rate](../methods/binary/CON-response-rate.md)：ASAS40 应答定义

## 出处

- Claude 对话（inbox: stratification_example_check.md；AI 生成，原始出处待补）
- Claude 对话（inbox: calculcate_sample_size.md；AI 生成，原始出处待补）
- 建议对照：Chow, Shao & Wang《Sample Size Calculations in Clinical Research》；Fleiss, Levin & Paik《Statistical Methods for Rates and Proportions》（连续性校正）
