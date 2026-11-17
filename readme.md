# Clinical Statistics Knowledge Base

临床试验统计知识库：Markdown 卡片是唯一知识源，同时服务于

- **Claude 咨询**：`clinical-stats` skill 在任何项目里回答统计问题时检索卡片并标注出处
- **Wiki 浏览**：MkDocs（Material 主题）把同一批卡片渲染成可搜索的网站

## 第一次使用

1. 把整个文件夹放到固定位置，例如 `C:\work\clinical-stats-kb`，然后初始化 Git：
   ```powershell
   cd C:\work\clinical-stats-kb
   git init; git add .; git commit -m "init knowledge base"
   ```
2. 安装全局咨询 skill（会把 SKILL.md 里的路径占位符替换成本仓库的实际路径）：
   ```powershell
   .\install.ps1
   # 两个 Claude Code 账号都要用的话，把两个 CLAUDE_CONFIG_DIR 都传进去：
   .\install.ps1 -ConfigDirs "<账号1配置目录>","<账号2配置目录>"
   ```
   如果提示脚本被禁止执行：`Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`
3. 安装 MkDocs（本机已装在 miniconda 的 Python 3.13 中），预览 wiki：
   ```powershell
   pip install mkdocs mkdocs-material jieba   # jieba 用于中文搜索分词
   C:\ProgramData\miniconda3\python.exe -m mkdocs serve   # 打开 http://127.0.0.1:8000
   ```
   配置在 `mkdocs.yml`；`hooks/card_meta.py` 在每张卡片标题下显示状态、相关卡片和出处。

## 日常流程

| 想做什么 | 怎么做 |
|---|---|
| 收录新知识 | 把笔记、guidance 摘录、PDF、对话片段丢进 `inbox/`，在本仓库的 Claude Code 里运行 `/kb-ingest` |
| 咨询 | 在任何项目里直接问统计问题，`clinical-stats` skill 会自动触发；也可以手动 `/clinical-stats` |
| 核对卡片 | 对照原始出处核对后，把 `status: draft` 改成 `reviewed`（只由你本人修改） |
| 体检 | 运行 `/kb-lint`，查断链、孤立卡片、缺字段、长期 draft |
| 看 wiki | `python -m mkdocs serve` 本地预览，或 `python -m mkdocs build` 生成静态网站到 `site/` |

## 结构

```
inbox/              待收录材料（处理后归档到 inbox/archive/）
wiki/index.md       总索引 + 待建卡片清单
wiki/cards/<主题>/  卡片，按主题分文件夹（estimand、inference、methods/…、missing-data、design、regulatory）
                    文件名前缀表示类型：CON 概念 / MTH 方法 / WF 流程 / CODE 代码 / TLF / GOT 坑 / REF 文献
mkdocs.yml, hooks/  网站配置；hooks/card_meta.py 定义侧边栏主题的中文名和顺序
templates/          卡片模板
.claude/skills/     clinical-stats（咨询）、kb-ingest（收录）、kb-lint（体检）
CLAUDE.md           给 Claude 的仓库规则
```

规则细节见 `CLAUDE.md`。

## 示例卡片

自带的 4 张卡片（estimand、MMRM、MMRM 不收敛、ICH E9(R1)）都是 `draft`，由 Claude 起草，
请对照 ICH E9(R1) 原文和你们的 SAP 核对后再改为 `reviewed`。
