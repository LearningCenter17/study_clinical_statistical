"""MkDocs hook：根据 wiki/glossary.md 生成"术语表（按英文 A–Z）"页面（glossary-en.md）。

glossary.md 是唯一数据源（按学习大纲分章、手工维护）；本页只是把同样的行按英文重新排序，
不落盘，只在构建时存在。改术语请改 glossary.md。
"""

import logging
import os
import re

from mkdocs.structure.files import File

log = logging.getLogger("mkdocs.hooks.glossary_en")

SRC = "glossary.md"
PAGE_URI = "glossary-en.md"


def _cells(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def _parse(text):
    """返回 [(chapter, 中文, English, 缩写, 主卡)]。"""
    rows, chapter, header = [], "", None
    for line in text.splitlines():
        if line.startswith("## "):
            chapter, header = line[3:].strip(), None
            continue
        if not line.startswith("|"):
            header = None
            continue
        cells = _cells(line)
        if header is None:
            header = cells
            continue
        if set("".join(cells)) <= set("-: "):
            continue  # 分隔行
        if len(cells) != 4:
            log.warning(f"glossary.md：这一行不是 4 列，已跳过：{line.strip()}")
            continue
        rows.append((chapter, *cells))
    return rows


def _sort_key(english):
    plain = english.replace("†", "")
    plain = re.sub(r"^[^A-Za-z0-9]+", "", plain)
    return plain.lower()


def _build(rows):
    rows = sorted(rows, key=lambda r: _sort_key(r[2]))
    out = [
        "---",
        "title: 术语表（按英文 A–Z）",
        "---",
        "",
        "> 本页由 [术语表](glossary.md) 在构建网站时自动生成，内容相同，只是按英文首字母重新排序，"
        "并多了一列\"章节\"。修改术语请改 `wiki/glossary.md`。"
        "**†** = 卡片中只出现一种语言、另一种由 Claude 补充，待 Li 核实。",
        "",
    ]
    letters = []
    for r in rows:
        k = _sort_key(r[2])
        letter = k[:1].upper() if k[:1].isalpha() else "#"
        if letter not in letters:
            letters.append(letter)
    out.append("跳转：" + " · ".join(f"[{l}](#{l.lower() if l != '#' else 'other'})" for l in letters))
    out.append("")
    current = None
    for chapter, zh, en, abbr, card in rows:
        k = _sort_key(en)
        letter = k[:1].upper() if k[:1].isalpha() else "#"
        if letter != current:
            current = letter
            anchor = letter.lower() if letter != "#" else "other"
            out += ["", f"## {letter} {{ #{anchor} }}", "",
                    "| English | 中文 | 缩写 | 主卡 | 章节 |", "|---|---|---|---|---|"]
        out.append(f"| {en} | {zh} | {abbr} | {card} | {chapter} |")
    out.append("")
    return "\n".join(out)


def on_files(files, config):
    src = os.path.join(config["docs_dir"], SRC)
    if not os.path.exists(src):
        log.warning(f"找不到 {SRC}，跳过英文术语表页面")
        return files
    with open(src, encoding="utf-8") as f:
        rows = _parse(f.read())
    if not rows:
        log.warning("glossary.md 中没有解析到术语行")
        return files
    files.append(File.generated(config, PAGE_URI, content=_build(rows)))
    return files
