AESEV  和 ASEV两个变量记录的都是不良事件的**严重程度**（轻 / 中 / 重），区别在于来源：

| | `AESEV` | `ASEV` |
|---|---|---|
| 所在数据集 | SDTM **AE**（ADAE 里通常也会带过来） | ADaM **ADAE** |
| 英文 label | Severity/Intensity | Analysis Severity/Intensity |
| 含义 | **收集到的原始值**：研究者在 CRF 上填的 | **分析用的值**：按 SAP 规则处理过的，TLF 用这个 |
| 取值 | `MILD` / `MODERATE` / `SEVERE`（受控术语） | 通常同上 |

就是命名片段里那条规律：前缀 **A** 表示 Analysis（分析版本），`ASEV` 对 `AESEV`，跟 `AREL` 对 `AEREL`、`ASTDT` 对 `AESTDTC` 是一回事。

**ASEV 和 AESEV 什么时候不一样**

大部分记录两者相同，常见的不同情况有：
- **缺失填补**：研究者没填严重程度，SAP 常规定按最保守的情况处理，`ASEV` 填成 `SEVERE`（还会用一个标识变量记录这是填补的，具体名字看 spec）
- **从其他量表转换**：比如肿瘤研究按 CTCAE 分级（`AETOXGR`），SAP 可能规定把分级映射成轻 / 中 / 重
- **数据清理后的修正**

还常配一个数值版本 **`ASEVN`**（1 = MILD，2 = MODERATE，3 = SEVERE），方便排序。做"按最严重程度汇总"的表时，每个受试者每个 PT 只取 `ASEVN` 最大的那条。

**一个常见混淆：severity ≠ seriousness**

- **`AESEV` / `ASEV`（severity）**：强度有多大，轻、中还是重
- **`AESER`（serious）**：是否属于**严重不良事件（SAE）**，这是监管上的定义，比如导致死亡、危及生命、需要住院或延长住院、导致残疾、先天畸形等

两者是独立的：一次重度头痛可以是 `SEVERE` 但不是 SAE；一次轻度的症状如果导致住院，就是 SAE。TLF 里这两类表是分开做的。