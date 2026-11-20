这是 SAE 判定标准里的一条，对应变量 **`AESDISAB`**。

**完整说法**

Persistent or Significant Disability/Incapacity：**导致持续的或显著的残疾 / 功能丧失**。label 里的 "Signif" 是 Significant 的缩写，因为 SDTM 的 label 最多 40 个字符，写全放不下。

**怎么理解**

FDA 的定义（21 CFR 312.32）是：事件对受试者**进行正常日常生活的能力造成实质性破坏**（substantial disruption of a person's ability to conduct normal life functions）。

两个词的区别：
- **Persistent（持续的）**：影响长期存在，甚至永久
- **Significant（显著的）**：影响很大，即使最终能恢复

满足其中一个就算。

**例子**

| 算 SAE（AESDISAB = Y） | 不算 |
|---|---|
| 脑卒中后偏瘫 | 头痛、流感，休息几天就好 |
| 永久性听力或视力丧失 | 踝关节扭伤，短时间行动不便 |
| 严重周围神经病变，影响行走或手部功能 | 轻度皮疹 |

关键在于**对正常生活能力的影响程度和持续时间**，不是事件本身听起来严不严重。一次重度但很快恢复的事件，`AESEV` 可以是 `SEVERE`，但不一定满足这条标准。

**变量拆解**

`AESDISAB` = AE + **S**（Serious）+ **DISAB**（Disability），取值 `Y` / `N`。

和前面的 `AESCONG` 一样，这一条在实际数据里也比较少见。SAE 最常见的原因通常是 `AESHOSP`（需要住院或延长住院）。