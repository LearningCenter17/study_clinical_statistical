---
id: CON-reference-date-study-day
title: "参考日期与研究日：RFSTDTC、DM 中的 RF 日期、--DY / ADY 的算法（Reference Date and Study Day）"
categories: [cdisc, sdtm, adam, reference-date, study-day, rfstdtc, trtsdt, dm, adsl, statistical-programming]
related: [CON-cdisc-variable-naming, CON-sdtm-epoch]
sources: ["Claude 对话（inbox: reference date.md）"]
status: draft
updated: 2026-11-20
---

> 出处待补：本卡内容来自 Claude 对话（inbox: reference date.md），属 AI 生成内容，未引用原始文献。需对照 CDISC SDTMIG（DM 域、--DY 定义）与 ADaMIG（ADSL、ADY）核实。变量名里 `RF`、`DY`、`DTC` 等零件的含义见 [CON-cdisc-variable-naming](CON-cdisc-variable-naming.md)。

## 一句话定义

"参考日期"（reference date）就是**用来做对照的基准日期**。别的日期都拿它来比，算出"在它之前还是之后、隔了几天"。

**最典型的用途：算研究日**

SDTM 里的研究日（`--DY`，比如 `AESTDY`、`LBDY`）就是相对于 `RFSTDTC` 算出来的：

- 日期 ≥ `RFSTDTC`：`--DY = 日期 − RFSTDTC + 1`
- 日期 < `RFSTDTC`：`--DY = 日期 − RFSTDTC`

举个例子，假设某受试者 `RFSTDTC` = 2026-03-10（首次用药日）：

| 事件 | 日期 | 研究日 |
|---|---|---|
| 签知情同意（`RFICDTC`） | 2026-02-20 | Day −18 |
| 筛选期化验 | 2026-03-01 | Day −9 |
| 首次用药（`RFSTDTC`） | 2026-03-10 | **Day 1** |
| 出现 AE | 2026-03-24 | Day 15 |

不同受试者入组的日历日期都不一样，换算成研究日之后，大家就在同一条时间轴上了，"Day 15 出现 AE"对谁都是一个意思。

**DM 里那几个 RF 日期，就是每个受试者时间轴上的几个关键节点**

```
签知情同意 ──── 首次用药 ──────── 末次用药 ──── 结束参与
RFICDTC         RFXSTDTC          RFXENDTC      RFPENDTC
                (RFSTDTC 通常也是这天)
```

其中 `RFSTDTC` 最特殊，它是计算研究日的那个"零点"，所以叫 Subject Reference Start Date。它具体取哪天由 sponsor 定义，最常见的是首次用药日，也有研究用随机化日。

到了 ADaM，`TRTSDT` 接过了这个角色：`ADY` 就是相对于 `TRTSDT` 算的，规则和上面一样，也没有 Day 0。

> 数值复核（Claude）：2026-02-20 到 2026-03-10 相差 18 天，在 RFSTDTC 之前，所以 Day −18；2026-03-01 相差 9 天，Day −9；2026-03-24 比 RFSTDTC 晚 14 天，加 1 得 Day 15。与材料一致。
>
> 补充（Claude）："没有 Day 0"的原因：参考日期当天记为 Day 1，前一天直接是 Day −1。所以两个研究日相减不一定等于实际间隔天数（如 Day −1 到 Day 1 实际只隔 1 天）。ADY 相对哪个日期算由 ADaMIG 交给 sponsor 定义，`TRTSDT` 是最常见的选择，具体以 define.xml / ADRG 为准。待 Li 核实。

## 相关卡片

- [CON-cdisc-variable-naming](CON-cdisc-variable-naming.md)：RF、DY、DTC 等变量名零件
- [CON-sdtm-epoch](CON-sdtm-epoch.md)：按阶段划分时间轴的 EPOCH

## 出处

- Claude 对话（inbox: reference date.md；AI 生成，原始出处待补）
