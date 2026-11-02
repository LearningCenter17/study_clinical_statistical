---
name: clinical-stats
description: Answer clinical trial statistics questions from Li's curated knowledge base. Use for estimand, intercurrent events, ICH E9(R1), MMRM, ANCOVA, mixed models, missing data, multiple imputation, tipping point, Kaplan-Meier, log-rank, Cox regression, hazard ratio, CMH, logistic regression, odds ratio, risk difference, multiplicity, gatekeeping, Hochberg, sample size, power, non-inferiority, interim analysis, sensitivity analysis, subgroup analysis, and how these appear in SAS or R output and TLFs. Also triggers on 统计, 估计目标, 缺失数据, 多重性, 样本量.
---

# Clinical Statistics 咨询

知识库根目录：`{{KB_ROOT}}`
（如果上面仍显示为未替换的占位符，说明你正在知识库项目内部运行，根目录就是当前项目根目录。）

所有知识在 `{{KB_ROOT}}/wiki/` 下的卡片里。本 skill 只负责查找和引用，不要在这里补充知识。

## 回答流程

1. **定位**：先读 `{{KB_ROOT}}/wiki/index.md`，找出相关卡片 ID。
   index 不够时，在 `{{KB_ROOT}}/wiki/` 下按关键词 grep 卡片正文和 `categories`。
2. **读卡**：只读相关的卡片（通常 1–4 张），顺着 `related` 最多再展开一层。
3. **回答**：基于卡片内容回答，用 `[CON-MMRM]` 这样的形式标注出处。
   - 卡片 `status: draft` 时，在引用处标注"（未审核）"。
   - 卡片里没有、需要用你自己的知识补充的部分，单独放在"卡片外补充"小节，
     并说明可信度。不要把卡片外内容伪装成知识库内容。
4. **建议入库**：如果回答里有值得长期保存的新知识点，最后用一行提示：
   "建议新增卡片：`CON-xxx`（一句话说明）"，并询问是否要写入 `inbox/`。

## 回答风格

- 先给结论，再给依据；需要代码时 SAS 和 R 都给（除非用户只问一种）。
- 涉及方法选择时，说清楚适用条件和关键假设。
- 涉及监管要求时，指明是哪份指南，不要泛泛说"FDA 要求"。
