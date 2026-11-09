（来源：Claude 对话回复，Li 于 2026-11-09 粘贴；AI 生成，未引用原始文献。背景：更正 h0_hr.md 中"LIFETEST 和 PHREG 检验的都是 HR = 1"的说法）

你的理解是对的，我上一条的说法不够严谨。更准确的表述如下：

## log-rank 检验

- **H₀：两组的生存曲线在所有时间点都相同**，即 S₁(t) = S₂(t)，等价于两组的风险函数在每一时刻都相等。
- 它是**非参数**方法，只比较每个事件时间点上"观察到的事件数"和"H₀ 下的期望事件数"，**不估计 HR，也不依赖比例风险（PH）假设才成立**。
- PH 假设影响的是它的**功效**：在 PH 成立时，log-rank 是最有效的检验；如果两条生存曲线交叉（比如前期新药组差、后期新药组好），正负差异会相互抵消，功效会明显下降。

## Cox 模型（PROC PHREG）

- 假设 h₁(t) = h₀(t)·e^β，HR = e^β 在整个时间段内恒定（PH 假设）。
- H₀：β = 0，即 **HR = 1**。这才是严格意义上"检验 HR = 1"。
- PHREG 会给出三种检验：似然比检验、score 检验、Wald 检验，同时给出 HR 的估计值和置信区间。

## 二者的关系

- 在 PH 模型框架下，"两组曲线相同"和"HR = 1"是一回事。
- 当 Cox 模型中**只有一个组别协变量**时，**log-rank 检验就是它的 score 检验**。没有结点（tied event times）时两者完全相同；有结点时，数值是否一致取决于 ties 的处理方法，可能略有差别。

## 临床试验中的常见做法

正是因为这种分工，SAP 里通常这样写：

- **P 值**：来自（分层）log-rank 检验，`PROC LIFETEST`
- **HR 及其 95% CI**：来自（分层）Cox 模型，`PROC PHREG`
- 同时检查 PH 假设（比如 log(−log S(t)) 图、Schoenfeld 残差或时间交互项），作为 HR 解释是否合理的依据

```sas
/* log-rank：检验生存曲线是否相同，给出 P 值 */
proc lifetest data=adtte;
  time aval * cnsr(1);
  strata trt / test=logrank;
run;

/* Cox：估计 HR 和 95% CI */
proc phreg data=adtte;
  class trt(ref="Placebo");
  model aval * cnsr(1) = trt / risklimits ties=efron;
run;
```

所以更正一下我之前那句话：**PHREG 检验的是 HR = 1；LIFETEST 的 log-rank 检验的是两组生存曲线相同，它不估计 HR，只是在比例风险假设下与 Cox 的 score 检验等价。**
