相关术语：

| 中文 | 英文 |
|---|---|
| 样本量计算 | sample size calculation 或 sample size determination |
| 样本量估算的依据（方案或 SAP 中的章节名） | sample size justification 或 sample size rationale |
| 把握度 / 检验效能 | power |
| 效应量 | effect size |
| 脱落率 | dropout rate |
| 非劣效界值 | non-inferiority margin |

方案中这一节通常叫 **"Sample Size Determination"** 或 **"Sample Size Justification"**。
样本量由**主要终点的统计假设**决定。先确定以下几个要素，再按终点类型套用相应的公式。

## 一、需要确定的要素

| 要素 | 含义 | 常用取值 |
|---|---|---|
| α | I 类错误 | 双侧 0.05，或单侧 0.025 |
| 1−β（power） | 把握度 | 80% 或 90% |
| Δ | 预期的组间差异（临床上有意义的效应量） | 来自前期研究或文献 |
| σ / p | 变异度（连续变量用标准差，二分类用各组的率） | 来自前期研究或文献 |
| 分配比例 k | 两组人数比 | 1:1、2:1 等 |
| 检验类型 | 优效、非劣效或等效 | 非劣效还需要界值 M |
| 脱落率 | 预计会丢失的受试者比例 | 10%–20% |

## 二、常用公式（两组，1:1 分配）

**1. 连续变量（比较均值）**

$$n_{\text{每组}} = \frac{2\,(z_{1-\alpha/2} + z_{1-\beta})^2\,\sigma^2}{\Delta^2}$$

例：α=0.05（双侧），power=90%，σ=10，Δ=5
→ z 值为 1.96 和 1.2816，n = 2×(3.2416)²×100/25 ≈ 84.1，向上取整为**每组 85 人**。

**2. 二分类变量（比较率）**

$$n_{\text{每组}} = \frac{\left[z_{1-\alpha/2}\sqrt{2\bar p(1-\bar p)} + z_{1-\beta}\sqrt{p_1(1-p_1)+p_2(1-p_2)}\right]^2}{(p_1-p_2)^2}$$

其中 $\bar p = (p_1+p_2)/2$。

**3. 生存分析（log-rank 检验）**

先算需要的**事件数**（Schoenfeld 公式），HR 为风险比：

$$D = \frac{4\,(z_{1-\alpha/2} + z_{1-\beta})^2}{(\ln HR)^2}$$

再根据入组期、随访期和事件发生率，把事件数换算成总人数。

**4. 非劣效设计**

把公式中的 Δ 换成 **(真实差异 − 非劣效界值 M)**，并通常使用单侧 α=0.025。

**5. 考虑脱落**

$$N_{\text{最终}} = \frac{n}{1 - \text{脱落率}}$$

例：85 / (1 − 0.15) = 100，即每组 100 人。

## 三、R 实现

```r
# 连续变量
power.t.test(delta = 5, sd = 10, sig.level = 0.05, power = 0.90)

# 二分类变量
power.prop.test(p1 = 0.30, p2 = 0.50, sig.level = 0.05, power = 0.80)

# 生存分析（需要安装 gsDesign）
library(gsDesign)
nSurv(lambdaC = log(2)/12,   # 对照组中位生存期 12 个月
      hr = 0.7, eta = 0.05,  # eta 为脱落风险率
      T = 36, minfup = 12,   # 研究总时长和最短随访时间
      alpha = 0.025, beta = 0.1)
```

`power.t.test` 用 t 分布计算，结果会比 z 公式略大，约每组 86 人。商业软件常用 PASS、nQuery、East，SAS 中用 `PROC POWER`。

## 四、实际中要注意

- **效应量和变异度的来源**最关键，通常来自 II 期数据或文献，SAP 中要写明依据。
- **多重比较**（多个主要终点或多个剂量组）需要校正 α，例如 Bonferroni 或分层检验程序（hierarchical testing），这会增加样本量。
- **期中分析**（成组序贯设计）会消耗 α，样本量需要相应放大，可以用 gsDesign 或 rpact 计算。
- 回到你上一个问题：**是否分层基本不进入这个计算**，除非 SAP 明确使用了基于协变量调整的方差。

