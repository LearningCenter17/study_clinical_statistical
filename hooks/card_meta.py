"""MkDocs hook：在每张卡片标题下显示 frontmatter 中的状态、更新日期、相关卡片和出处，
并把侧边栏的文件夹名换成中文。卡片内容本身不做任何修改。"""

import posixpath

# 侧边栏：wiki/cards/ 下按主题分文件夹。这里给文件夹起中文名并定顺序（按学习大纲）。
# 新建主题文件夹时在这里加一行；没列出的文件夹排在最后，显示英文名。
SECTIONS = {
    "cards/estimand": "估计目标（Estimand）",
    "cards/inference": "统计推断基础",
    "cards/methods": "分析方法",
    "cards/methods/continuous": "连续型终点",
    "cards/methods/binary": "二分类终点",
    "cards/methods/ordinal": "有序分类终点",
    "cards/methods/tte": "生存分析",
    "cards/methods/count": "计数终点",
    "cards/missing-data": "缺失数据与敏感性分析",
    "cards/design": "试验设计",
    "cards/safety": "安全性分析",
    "cards/regulatory": "法规与指南",
    "cards/non-clinical": "非临床应用",
}
_ORDER = list(SECTIONS)

_id_to_path = {}


def on_files(files, config):
    _id_to_path.clear()
    for f in files.documentation_pages():
        stem = posixpath.splitext(posixpath.basename(f.src_uri))[0]
        _id_to_path[stem] = f.src_uri
    return files


def _section_dir(section):
    """文件夹路径 = 该 section 下所有页面路径的公共父目录。"""
    paths = []

    def walk(items):
        for it in items:
            if it.is_page:
                paths.append(posixpath.dirname(it.file.src_uri))
            elif it.is_section:
                walk(it.children)

    walk(section.children)
    return posixpath.commonpath(paths) if paths else ""


def _tidy(items):
    for it in items:
        if it.is_section:
            key = _section_dir(it)
            it.title = SECTIONS.get(key, it.title)
            it._kb_key = key
            _tidy(it.children)
    # 页面在前（按卡片类型：概念 → 方法 → 流程 → 代码 → TLF → 坑 → 文献），子文件夹按 SECTIONS 顺序在后
    def key(it):
        if it.is_section:
            return (1, _ORDER.index(it._kb_key) if it._kb_key in _ORDER else len(_ORDER), "")
        name = posixpath.basename(it.file.src_uri)
        prefix = name.split("-", 1)[0]
        return (0, _TYPE_ORDER.index(prefix) if prefix in _TYPE_ORDER else len(_TYPE_ORDER), name)

    items.sort(key=key)


# 顶层页面：索引 → 术语表 → 英文术语表（"glossary" 取自 glossary-en.md）→ 决策树（"decision" 取自 decision-tree.md）；
# 文件夹内：按卡片类型
_TYPE_ORDER = ["index.md", "glossary.md", "glossary", "decision", "CON", "MTH", "WF", "CODE", "TLF", "GOT", "REF"]


def on_nav(nav, config, files):
    items = []
    for it in nav.items:
        # 去掉 cards/ 这一层，主题文件夹直接放在侧边栏第一层
        if it.is_section and _section_dir(it) == "cards":
            for child in it.children:
                child.parent = None
            items.extend(it.children)
        else:
            items.append(it)
    _tidy(items)
    nav.items[:] = items
    return nav


def _as_list(value):
    if value is None:
        return []
    if isinstance(value, (list, tuple)):
        return [str(v) for v in value]
    return [str(value)]


def on_page_markdown(markdown, page, config, files):
    meta = page.meta or {}
    if "id" not in meta:
        return markdown

    here = posixpath.dirname(page.file.src_uri)
    status = str(meta.get("status", "draft"))
    badge = "✅ reviewed" if status == "reviewed" else "📝 draft（未核对）"

    lines = [f"**状态**：{badge} · **更新**：{meta.get('updated', '—')}"]

    related = []
    for rid in _as_list(meta.get("related")):
        target = _id_to_path.get(rid)
        if target:
            rel = posixpath.relpath(target, here or ".")
            related.append(f"[{rid}]({rel})")
        else:
            related.append(f"{rid}（未找到）")
    if related:
        lines.append("**相关**：" + " · ".join(related))

    sources = _as_list(meta.get("sources"))
    if sources:
        lines.append("**出处**：" + "；".join(sources))

    header = '<div class="card-meta" markdown>\n\n' + "  \n".join(lines) + "\n\n</div>\n\n"
    return header + markdown
