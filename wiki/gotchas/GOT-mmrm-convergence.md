---
id: GOT-mmrm-convergence
title: MMRM 非结构化协方差不收敛
categories: [mixed-model, convergence, sap]
related: [CON-MMRM]
sources: []
status: draft
updated: 2026-11-02
---

## 现象

UN 协方差结构参数多（k 个访视需要 k(k+1)/2 个参数），访视多或样本少时容易不收敛，
SAS 报 "Did not converge" 或 G/R 矩阵非正定，R `mmrm` 报拟合失败。

## 正确做法

- **事先在 SAP 里写好备选顺序**，不收敛时按顺序依次尝试，例如：
  UN → 异质 Toeplitz（TOEPH）→ 异质 AR(1)（ARH(1)）→ 复合对称（CS）。
  具体顺序以本研究 SAP 为准。
- 不能看哪个结果"好看"再选结构；应选顺序中第一个收敛的。
- 输出中记录最终使用的协方差结构，TLF 脚注写明。

## 实现提示

- SAS：可加 `method=reml` 并调整 `maxiter`、`convh`；确认没有数据问题（如某访视几乎无观测）。
- R `mmrm`：默认会尝试多个优化器；协方差结构用 `us()`、`toeph()`、`ar1h()`、`cs()` 等函数切换。

## 出处

- 出处待补（建议补充 SAP 模板或方法学文献）
