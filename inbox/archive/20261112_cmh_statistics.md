<!-- 来源：Li 粘贴的 Claude 对话回复（2026-11-12），确认 CON-ordinal-data 中"治疗组 vs 有序应答看 Row Mean Scores Differ"的补充，并展开 CMH 三个统计量与 SCORES= 选项。已合并进 CON-CMH（新建）与 CON-ordinal-data。 -->

对，这个说法是准确的。可以把它放进完整的选择逻辑里看。

**PROC FREQ 的 CMH 三个统计量怎么选**

| 统计量 | 行（治疗组） | 列（应答） | 自由度 |
|---|---|---|---|
| Nonzero Correlation | 有序 | 有序 | 1 |
| **Row Mean Scores Differ** | **无序** | **有序** | 行数 − 1 |
| General Association | 无序 | 无序 | (行−1)(列−1) |

治疗组 vs 有序应答（比如 CGI-I、mRS）对应的就是 Row Mean Scores Differ。

**`SCORES=` 选项决定检验的具体形式**

- `SCORES=TABLE`（默认）：用列变量的原始数值作为得分，要求编码的间距有意义。
- `SCORES=RANK`：用秩得分。不分层时等价于 Kruskal-Wallis；只有两组时等价于 Wilcoxon rank-sum。
- `SCORES=MODRIDIT`：在每层内把秩按 (n_h + 1) 标准化。分层时，Row Mean Scores 统计量就是 **van Elteren 检验**，也就是分层的 Wilcoxon。
- `SCORES=RIDIT`：和 modridit 类似，但标准化方式略有不同，不等同于 van Elteren。

**写代码时要注意**

```sas
proc freq data=adeff;
  tables strata * trt01pn * avaln / cmh scores=modridit;
run;
```

- 分层变量放在最前面，**治疗组必须在行的位置，应答在列的位置**。如果顺序放反，Row Mean Scores 检验的就成了另一个方向的假设。
- 应答变量的排序要正确。如果用字符型变量，默认可能按字母排序，所以最好用数值编码（比如 `AVAL`），或者设置 `ORDER=`。
- 结合上一条的讨论：上面例子里我写的 `avaln` 应该换成 `AVAL`，也就是存有序编码的那个变量。
