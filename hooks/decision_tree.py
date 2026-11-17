"""MkDocs hook：根据 wiki/decision-tree/tree.yaml 生成"检验方法选择树"页面（decision-tree.md）。

tree.yaml 是唯一数据源；生成的页面不落盘，只在构建时存在。
树里引用的卡片 ID 不存在、或叶子缺少 from 时，记 WARNING（mkdocs build --strict 会因此失败）。
"""

import logging
import os
import posixpath

import yaml
from mkdocs.structure.files import File

log = logging.getLogger("mkdocs.hooks.decision_tree")

TREE_SRC = "decision-tree/tree.yaml"  # 相对于 docs_dir
PAGE_URI = "decision-tree.md"


def _card_paths(files):
    paths = {}
    for f in files.documentation_pages():
        stem = posixpath.splitext(posixpath.basename(f.src_uri))[0]
        paths[stem] = f.src_uri
    return paths


def _link(card_id, anchor, paths, where):
    if card_id not in paths:
        log.warning(f"tree.yaml: {where} 引用的卡片 {card_id} 不存在")
        return f"`{card_id}`（未找到）"
    href = paths[card_id] + (f"#{anchor}" if anchor else "")
    return f"[{card_id}]({href})"


def _mermaid_text(s):
    return str(s).replace('"', "#quot;")


class _Renderer:
    def __init__(self, paths):
        self.paths = paths
        self.lines = []      # 逐级列表
        self.graph = []      # mermaid
        self.pending = []    # 待建方法
        self.n = 0

    def _id(self):
        self.n += 1
        return f"n{self.n}"

    def leaf(self, res, depth, path):
        method = res.get("method", "（未写方法名）")
        card, anchor, src, note = res.get("card"), res.get("anchor"), res.get("from"), res.get("note")
        where = " > ".join(path)
        if not src:
            log.warning(f"tree.yaml: 叶子「{method}」（{where}）缺少 from")
        text = f"**{method}**"
        if note:
            text += f"：{note}"
        if card:
            text += f"。详见 {_link(card, anchor, self.paths, where)}"
        else:
            text += "。卡片待建"
            self.pending.append((method, where, src))
        if src and src != card:
            text += f"（依据：{_link(src, None, self.paths, where)}）"
        self.lines.append("    " * depth + f"- → {text}")

    def node(self, node, depth=0, path=()):
        nid = self._id()
        q = node.get("question", "（未写问题）")
        self.graph.append(f'    {nid}{{"{_mermaid_text(q)}"}}')
        self.lines.append("    " * depth + f"- **{q}**")
        for opt in node.get("options", []):
            ans = opt.get("answer", "")
            self.lines.append("    " * (depth + 1) + f"- {ans}")
            sub_path = path + (ans,)
            if "next" in opt:
                child = self.node(opt["next"], depth + 2, sub_path)
                self.graph.append(f'    {nid} -->|"{_mermaid_text(ans)}"| {child}')
            elif "result" in opt:
                lid = self._id()
                res = opt["result"]
                label = res.get("method", "")
                if not res.get("card"):
                    label += "（待建）"
                self.graph.append(f'    {lid}["{_mermaid_text(label)}"]')
                self.graph.append(f'    {nid} -->|"{_mermaid_text(ans)}"| {lid}')
                self.leaf(res, depth + 2, sub_path)
            else:
                log.warning(f"tree.yaml: 分支「{ans}」既没有 next 也没有 result")
        return nid


def _build_markdown(tree, paths):
    r = _Renderer(paths)
    r.node(tree["root"])
    out = [
        "---",
        f"title: {tree.get('title', '检验方法选择树')}",
        "---",
        "",
        "> 本页由 `wiki/decision-tree/tree.yaml` 在构建网站时自动生成，修改请改那个文件。"
        "每个推荐都标明了出自哪张卡片；方法的解释、代码和例子都在卡片里。",
        "",
        tree.get("intro", ""),
        "",
        "## 流程图",
        "",
        "```mermaid",
        "flowchart LR",
        *r.graph,
        "```",
        "",
        "## 逐级查找",
        "",
        *r.lines,
        "",
    ]
    if r.pending:
        out += ["## 还没有卡片的方法", "", "| 方法 | 位置 | 依据 |", "|---|---|---|"]
        for method, where, src in r.pending:
            out.append(f"| {method} | {where} | {_link(src, None, paths, where) if src else '—'} |")
        out.append("")
    return "\n".join(out)


def on_files(files, config):
    src = os.path.join(config["docs_dir"], TREE_SRC)
    if not os.path.exists(src):
        log.warning(f"找不到 {TREE_SRC}，跳过决策树页面")
        return files
    with open(src, encoding="utf-8") as f:
        tree = yaml.safe_load(f)
    md = _build_markdown(tree, _card_paths(files))
    files.append(File.generated(config, PAGE_URI, content=md))
    return files
