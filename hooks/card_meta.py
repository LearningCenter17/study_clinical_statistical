"""MkDocs hook：在每张卡片标题下显示 frontmatter 中的状态、更新日期、相关卡片和出处，
并把侧边栏的文件夹名换成中文。卡片内容本身不做任何修改。"""

import posixpath

SECTION_TITLES = {
    "Concepts": "概念与方法",
    "Gotchas": "坑与易错点",
    "References": "指南与文献",
    "Tlf patterns": "TLF 呈现",
}

_id_to_path = {}


def on_files(files, config):
    _id_to_path.clear()
    for f in files.documentation_pages():
        stem = posixpath.splitext(posixpath.basename(f.src_uri))[0]
        _id_to_path[stem] = f.src_uri
    return files


def on_nav(nav, config, files):
    for item in nav.items:
        if item.is_section and item.title in SECTION_TITLES:
            item.title = SECTION_TITLES[item.title]
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
