现有的问题：
1. 几张卡太大，一张卡里塞了好几个知识点

CON-sample-size-power 有 416 行，里面混着基本原理、δ 怎么选、非劣效、k:1 不等分配、ASAS40 算例和 R 代码。
CON-confidence-interval 有 299 行，混着定义、CI 与贝叶斯可信区间的区别、CI 宽度、报告写法。
CON-p-value（199 行）、CON-t-test-pvalue（231 行）、CON-test-statistic、CON-t-distribution 这四张内容互相重叠。例如"P 值怎么算"、"不同检验用什么参照分布"在两三张卡里各讲了一遍，违反了你在 CLAUDE.md 里自己定的"一个知识点只写一张卡"。

2. 卡片类型

增加一些卡片类型

前缀	内容	例子
CON-	概念	CON-stratification
MTH-	统计方法	MTH-ANCOVA, MTH-MMRM
EST-	estimand 相关	EST-treatment-policy
WF-	操作流程	WF-sample-size-calc
GOT-	常见坑	GOT-cmh-sparse-strata
REF-	法规/文献	REF-ICH-E9R1
CODE-	R/SAS 代码	CODE-mmrm-r-vs-sas

3.网站的侧边栏十分混乱
保留目前index
侧边栏按内容排
比如
├── cards/
│   ├── design/               # 随机化、分层、样本量、多重性
│   ├── estimand/             # ICH E9(R1)、ICE 处理策略
│   ├── methods/
│   │   ├── continuous/       # ANCOVA, MMRM, t-test
│   │   ├── binary/           # CMH, logistic, Newcombe CI
│   │   ├── tte/              # KM, log-rank, Cox
│   │   └── count/            # Poisson, NegBin
│   ├── missing-data/         # MI, tipping point, NRI, LOCF
│   ├── safety/               # AE 发生率、暴露校正
│   └── regulatory/           # FDA/EMA guidance 要点
├── decision-tree/
│   └── tree.yaml             # 检验选择树的唯一数据源，网
└── glossary.md               # 中英术语对照

4. 我比较喜欢mkdocs的界面，是否能改成mkdocs?