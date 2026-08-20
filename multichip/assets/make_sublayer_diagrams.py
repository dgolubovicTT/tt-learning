#!/usr/bin/env python3
"""
Generates the attention / MLP sublayer diagrams for megatron-on-a-mesh.html.

One layout definition, two renderers:
  *.excalidraw  -- open at excalidraw.com to edit by hand
  *.svg.frag    -- inline SVG spliced into the page (uses the page's CSS tokens)

Shapes assume no batch dimension: activations are [S, H]-style 2-D.
On device they are really 4-D [1, 1, S, H], which is why the ops say dim=3.

Symbols
  S  sequence length
  H  model dim                       args.dim
  Q  fused qkv width                 head_dim * (n_heads + 2 * n_kv_heads)
  h  attention inner width           n_heads * head_dim   (== H only sometimes)
  F  FFN inner dim                   args.hidden_dim
  N  chips in the tensor-parallel group
"""
import json

# ---------------------------------------------------------------- layout ----

S_X = 270                # activation-state column, RIGHT-aligned against the op box
O_X, O_W = 292, 214      # op box
W_X, W_W = 530, 176      # weight box, fed in from the right
ROW_H, PITCH = 48, 96
TOP = 52

COL, ROW, REP = "col", "row", "rep"     # how a weight is cut
CCL, COMPUTE, RESID = "ccl", "compute", "resid"


def step(op, kind=COMPUTE, weight=None, cut=None, wnote=None,
         out_shape=None, out_state=None, note=None):
    return dict(op=op, kind=kind, weight=weight, cut=cut, wnote=wnote,
                out_shape=out_shape, out_state=out_state, note=note)


ATTENTION = dict(
    name="attention-sublayer",
    title="Attention sublayer  ·  tensor-parallel over N chips",
    in_shape="[S, H/N]", in_state="fractured",
    steps=[
        step("all_gather   dim=3", CCL,
             out_shape="[S, H]", out_state="gathered",
             note="every chip now holds the whole feature vector"),
        step("rms_norm", COMPUTE, weight="gamma   [H]", cut=REP,
             wnote="replicated on every chip",
             out_shape="[S, H]", out_state="gathered"),
        step("linear   W_qkv", COMPUTE, weight="W_qkv   [H, Q/N]", cut=COL,
             wnote="cut on head boundaries",
             out_shape="[S, Q/N]", out_state="fractured by head",
             note="Q = head_dim x (n_heads + 2 n_kv_heads)"),
        step("split_heads", COMPUTE,
             out_shape="q,k,v  [S, h/N]", out_state="fractured by head",
             note="a reshape - no data moves"),
        step("sdpa   is_causal", COMPUTE,
             out_shape="[S, h/N]", out_state="fractured by head",
             note="a head only ever mixes with itself"),
        step("linear   W_o", COMPUTE, weight="W_o   [h/N, H]", cut=ROW,
             wnote="K = h = n_heads x head_dim",
             out_shape="[S, H]", out_state="PARTIAL",
             note="full shape, only this chip's terms of the sum"),
        step("reduce_scatter   dim=3", CCL,
             out_shape="[S, H/N]", out_state="fractured",
             note="adds the partials, keeps one slice"),
        step("add   residual", RESID, weight="residual   [S, H/N]", cut=None,
             wnote="never gathered, so layouts match",
             out_shape="[S, H/N]", out_state="fractured"),
    ],
)

MLP = dict(
    name="mlp-sublayer",
    title="MLP sublayer  ·  tensor-parallel over N chips",
    in_shape="[S, H/N]", in_state="fractured",
    steps=[
        step("all_gather   dim=3", CCL,
             out_shape="[S, H]", out_state="gathered"),
        step("rms_norm", COMPUTE, weight="gamma   [H]", cut=REP,
             wnote="replicated on every chip",
             out_shape="[S, H]", out_state="gathered"),
        step("linear   w1, w3", COMPUTE, weight="w1, w3   [H, F/N]", cut=COL,
             wnote="both cut at the same offsets",
             out_shape="[S, F/N]  x2", out_state="fractured on F",
             note="F = 28672 vs H = 8192 for Llama-70B"),
        step("mul   SiLU(w1) x w3", COMPUTE,
             out_shape="[S, F/N]", out_state="fractured on F",
             note="two operands, identical layout - elementwise"),
        step("linear   w2", COMPUTE, weight="w2   [F/N, H]", cut=ROW,
             wnote="F is now the contracted axis",
             out_shape="[S, H]", out_state="PARTIAL",
             note="full shape, only this chip's terms of the sum"),
        step("reduce_scatter   dim=3", CCL,
             out_shape="[S, H/N]", out_state="fractured",
             note="adds the partials, keeps one slice"),
        step("add   residual", RESID, weight="residual   [S, H/N]", cut=None,
             wnote="same layout on both sides",
             out_shape="[S, H/N]", out_state="fractured"),
    ],
)


def geometry(spec):
    """Resolve the spec into absolute coordinates shared by both renderers."""
    rows = []
    for i, st in enumerate(spec["steps"]):
        y = TOP + i * PITCH
        rows.append(dict(st, y=y))
    height = TOP + len(rows) * PITCH + 24
    return rows, height


# ------------------------------------------------------------------ SVG -----

SVG_FILL = {CCL: "var(--ccl-wash)", COMPUTE: "var(--surface-2)", RESID: "var(--surface)"}
SVG_STROKE = {CCL: "var(--ccl)", COMPUTE: "var(--rule)", RESID: "var(--resid)"}
SVG_SW = {CCL: "2", COMPUTE: "1.5", RESID: "1.5"}
CUT_COLOR = {COL: "var(--local)", ROW: "var(--ccl)", REP: "var(--muted)"}


def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
             .replace("x2", "&#215;2").replace(" x ", " &#215; "))


def txt(x, y, s, size=10.5, fill="currentColor", anchor="start", weight=None):
    w = f' font-weight="{weight}"' if weight else ""
    return (f'<text x="{x}" y="{y}" font-family="ui-monospace, monospace" '
            f'font-size="{size}" fill="{fill}" text-anchor="{anchor}"{w}>{esc(s)}</text>')


def weight_glyph(x, y, cut, mid):
    """The cut pattern, with this chip's piece shaded."""
    g, w, h = [], 58, 30
    c = CUT_COLOR.get(cut, "var(--muted)")
    g.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="none" stroke="{c}" stroke-width="1.4"/>')
    if cut == COL:
        for k in range(1, 4):
            g.append(f'<line x1="{x+k*w/4}" y1="{y}" x2="{x+k*w/4}" y2="{y+h}" stroke="{c}" stroke-width="1"/>')
        g.append(f'<rect x="{x}" y="{y}" width="{w/4}" height="{h}" fill="{c}" opacity="0.28"/>')
    elif cut == ROW:
        for k in range(1, 4):
            g.append(f'<line x1="{x}" y1="{y+k*h/4}" x2="{x+w}" y2="{y+k*h/4}" stroke="{c}" stroke-width="1"/>')
        g.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h/4}" fill="{c}" opacity="0.28"/>')
    elif cut == REP:
        g.append(f'<rect x="{x+3}" y="{y+3}" width="{w}" height="{h}" fill="none" stroke="{c}" '
                 f'stroke-width="1" stroke-dasharray="3 2"/>')
    return "".join(g), mid


def render_svg(spec):
    rows, H = geometry(spec)
    W = 790
    o = []
    o.append(f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="{esc(spec["aria"])}">')
    o.append('<defs><marker id="%s-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" '
             'orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="currentColor"/></marker>'
             '<marker id="%s-w" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5" markerHeight="5" '
             'orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="var(--muted)"/></marker></defs>'
             % (spec["name"], spec["name"]))

    o.append(txt(S_X, 16, "ACTIVATION OUT", 10, "var(--muted)", "end", weight="600"))
    o.append(txt(O_X, 16, "OPERATION", 10, "var(--muted)", weight="600"))
    o.append(txt(W_X, 16, "WEIGHT  ·  SECOND OPERAND", 10, "var(--muted)", weight="600"))

    cx = O_X + O_W / 2
    o.append(txt(S_X, 34, f'{spec["in_shape"]}   {spec["in_state"]}', 11, "var(--ink)", "end", weight="600"))
    o.append(f'<line x1="{cx}" y1="24" x2="{cx}" y2="{TOP-2}" stroke="currentColor" stroke-width="1.5" '
             f'marker-end="url(#{spec["name"]}-a)"/>')

    for r in rows:
        y = r["y"]
        o.append(f'<rect x="{O_X}" y="{y}" width="{O_W}" height="{ROW_H}" rx="3" '
                 f'fill="{SVG_FILL[r["kind"]]}" stroke="{SVG_STROKE[r["kind"]]}" stroke-width="{SVG_SW[r["kind"]]}"/>')
        o.append(txt(cx, y + 29, r["op"], 12.5, "var(--ink)", "middle", "600"))

        if r["weight"]:
            gy = y + (ROW_H - 30) / 2
            if r["cut"]:
                glyph, _ = weight_glyph(W_X, gy, r["cut"], None)
                o.append(glyph)
                o.append(txt(W_X + 66, y + 18, r["weight"], 10, "var(--ink)"))
                o.append(txt(W_X + 66, y + 32, r["wnote"], 9.5, "var(--muted)"))
                label = {COL: "column-cut", ROW: "row-cut", REP: "replicated"}[r["cut"]]
                o.append(txt(W_X, gy + 42, label, 9.5, CUT_COLOR[r["cut"]], weight="600"))
            else:
                o.append(txt(W_X, y + 20, r["weight"], 10, "var(--resid)"))
                o.append(txt(W_X, y + 34, r["wnote"], 9.5, "var(--muted)"))
            o.append(f'<line x1="{W_X-14}" y1="{y+ROW_H/2}" x2="{O_X+O_W+4}" y2="{y+ROW_H/2}" '
                     f'stroke="var(--muted)" stroke-width="1.2" marker-end="url(#{spec["name"]}-w)"/>')

        state_col = {"gathered": "var(--ccl)", "PARTIAL": "var(--ccl)"}.get(r["out_state"], "var(--ink-2)")
        o.append(txt(S_X, y + 22, r["out_shape"], 11, "var(--ink)", "end", weight="600"))
        o.append(txt(S_X, y + 36, r["out_state"], 10, state_col, "end",
                     weight="600" if r["out_state"] == "PARTIAL" else None))
        if r["note"]:
            o.append(txt(S_X, y + 50, r["note"], 9, "var(--muted)", "end"))

        if r is not rows[-1]:
            o.append(f'<line x1="{cx}" y1="{y+ROW_H}" x2="{cx}" y2="{y+PITCH-2}" stroke="currentColor" '
                     f'stroke-width="1.5" marker-end="url(#{spec["name"]}-a)"/>')

    o.append("</svg>")
    return "\n          ".join(o)


# ----------------------------------------------------------- excalidraw -----

EX_STROKE = {CCL: "#e8590c", COMPUTE: "#1e1e1e", RESID: "#6741d9"}
EX_BG = {CCL: "#ffec99", COMPUTE: "#f8f9fa", RESID: "#ffffff"}
EX_CUT = {COL: "#0b7285", ROW: "#e8590c", REP: "#868e96"}

_n = [0]


def _id():
    _n[0] += 1
    return f"el{_n[0]:04d}"


def _base(t, x, y, w, h, stroke="#1e1e1e", bg="transparent", **kw):
    e = dict(id=_id(), type=t, x=x, y=y, width=w, height=h, angle=0,
             strokeColor=stroke, backgroundColor=bg, fillStyle="solid",
             strokeWidth=1, strokeStyle="solid", roughness=1, opacity=100,
             groupIds=[], frameId=None, roundness=None, seed=_n[0] * 7919,
             version=1, versionNonce=_n[0] * 104729, isDeleted=False,
             boundElements=None, updated=1, link=None, locked=False)
    e.update(kw)
    return e


def ex_rect(x, y, w, h, stroke, bg, sw=1, rounded=True):
    return _base("rectangle", x, y, w, h, stroke, bg, strokeWidth=sw,
                 roundness={"type": 3} if rounded else None)


def ex_line(x1, y1, x2, y2, stroke="#1e1e1e", sw=1, arrow=False):
    t = "arrow" if arrow else "line"
    e = _base(t, x1, y1, abs(x2 - x1), abs(y2 - y1), stroke, strokeWidth=sw,
              points=[[0, 0], [x2 - x1, y2 - y1]], lastCommittedPoint=None,
              startBinding=None, endBinding=None, startArrowhead=None,
              endArrowhead="arrow" if arrow else None)
    return e


def ex_text(x, y, s, size=12, stroke="#1e1e1e", bold=False):
    lines = s.split("\n")
    w = max(len(l) for l in lines) * size * 0.6
    h = len(lines) * size * 1.25
    return _base("text", x, y, w, h, stroke, roundness=None, text=s, fontSize=size,
                 fontFamily=3, textAlign="left", verticalAlign="top",
                 containerId=None, originalText=s, lineHeight=1.25,
                 strokeWidth=2 if bold else 1)


def ex_rtext(right_x, y, s, size=12, stroke="#1e1e1e"):
    """Excalidraw positions text by its left edge; place it so it ends at right_x."""
    return ex_text(right_x - len(s) * size * 0.6, y, s, size, stroke)


def render_excalidraw(spec):
    _n[0] = 0
    rows, H = geometry(spec)
    els = []
    cx = O_X + O_W / 2

    els.append(ex_text(W_X, 8, spec["title"], 16, "#1e1e1e", bold=True))
    els.append(ex_rtext(S_X, 34, "ACTIVATION OUT", 10, "#868e96"))
    els.append(ex_text(O_X, 34, "OPERATION", 10, "#868e96"))
    els.append(ex_text(W_X, 34, "WEIGHT / SECOND OPERAND", 10, "#868e96"))

    els.append(ex_rtext(S_X, TOP - 26, f'{spec["in_shape"]}  {spec["in_state"]}', 11))
    els.append(ex_line(cx, TOP - 24, cx, TOP, arrow=True))

    for r in rows:
        y = r["y"]
        els.append(ex_rect(O_X, y, O_W, ROW_H, EX_STROKE[r["kind"]], EX_BG[r["kind"]],
                           sw=2 if r["kind"] == CCL else 1))
        els.append(ex_text(O_X + 12, y + 16, r["op"], 13, EX_STROKE[r["kind"]]))

        if r["weight"]:
            gy = y + (ROW_H - 30) / 2
            if r["cut"]:
                c = EX_CUT[r["cut"]]
                els.append(ex_rect(W_X, gy, 58, 30, c, "transparent", rounded=False))
                if r["cut"] == COL:
                    for k in range(1, 4):
                        els.append(ex_line(W_X + k * 14.5, gy, W_X + k * 14.5, gy + 30, c))
                    els.append(ex_rect(W_X, gy, 14.5, 30, c, c, rounded=False))
                elif r["cut"] == ROW:
                    for k in range(1, 4):
                        els.append(ex_line(W_X, gy + k * 7.5, W_X + 58, gy + k * 7.5, c))
                    els.append(ex_rect(W_X, gy, 58, 7.5, c, c, rounded=False))
                label = {COL: "column-cut", ROW: "row-cut", REP: "replicated"}[r["cut"]]
                els.append(ex_text(W_X, gy + 34, label, 10, c))
                els.append(ex_text(W_X + 66, y + 8, r["weight"], 11))
                els.append(ex_text(W_X + 66, y + 24, r["wnote"], 9, "#868e96"))
            else:
                els.append(ex_text(W_X, y + 12, r["weight"], 11, "#6741d9"))
                els.append(ex_text(W_X, y + 28, r["wnote"], 9, "#868e96"))
            els.append(ex_line(W_X - 14, y + ROW_H / 2, O_X + O_W + 4, y + ROW_H / 2, "#868e96", arrow=True))

        col = "#e8590c" if r["out_state"] in ("gathered", "PARTIAL") else "#1e1e1e"
        els.append(ex_rtext(S_X, y + 8, r["out_shape"], 12))
        els.append(ex_rtext(S_X, y + 24, r["out_state"], 10, col))
        if r["note"]:
            els.append(ex_rtext(S_X, y + 38, r["note"], 9, "#868e96"))

        if r is not rows[-1]:
            els.append(ex_line(cx, y + ROW_H, cx, y + PITCH, arrow=True))

    return dict(type="excalidraw", version=2, source="tt-learning/multichip",
                elements=els,
                appState={"gridSize": None, "viewBackgroundColor": "#ffffff"},
                files={})


# ------------------------------------------------------------------ main ----

ATTENTION["aria"] = (
    "The attention sublayer as eight operations in a column. Each row shows the weight as a second operand "
    "on the left with its cut pattern drawn, the operation in the middle, and the resulting activation shape "
    "and state on the right. The activation enters fractured with shape S by H over N. all_gather makes it "
    "gathered with shape S by H. rms_norm uses a replicated gamma and leaves it gathered. The W_qkv linear "
    "uses a column-cut weight of shape H by Q over N, cut on head boundaries, so the output is fractured by "
    "head. split_heads and sdpa move no data. The W_o linear uses a row-cut weight of shape h over N by H, "
    "where h is n_heads times head_dim, so its output is a partial of shape S by H. reduce_scatter adds the "
    "partials and returns a fractured slice, and the residual add matches layouts exactly.")
MLP["aria"] = (
    "The MLP sublayer as seven operations in a column, laid out the same way. The activation enters "
    "fractured, all_gather makes it gathered, rms_norm uses a replicated gamma. The w1 and w3 linears use "
    "column-cut weights of shape H by F over N cut at the same offsets, so both outputs are fractured on F "
    "identically. The SiLU multiply combines two operands with identical layout and moves no data. The w2 "
    "linear is row-cut with F as its contracted axis and produces a partial of shape S by H. reduce_scatter "
    "adds the partials and returns a fractured slice before the residual add.")

if __name__ == "__main__":
    import os
    here = os.path.dirname(os.path.abspath(__file__))
    for spec in (ATTENTION, MLP):
        with open(os.path.join(here, spec["name"] + ".excalidraw"), "w") as f:
            json.dump(render_excalidraw(spec), f, indent=1)
        with open(os.path.join(here, spec["name"] + ".svg.frag"), "w") as f:
            f.write(render_svg(spec))
        print("wrote", spec["name"], "(.excalidraw + .svg.frag)")
