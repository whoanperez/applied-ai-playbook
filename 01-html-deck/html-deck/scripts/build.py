#!/usr/bin/env python3
"""
html-deck 2 · build.py  (MIT · Juan Camilo Pérez Cuervo)

Claude writes ONE file, deck.json (brand + story + slides with a layout name and
short text slots). This script draws everything else: layouts, art panels,
charts, icons, a contrast-checked palette, and runs content checks.

  python build.py deck.json --out deck.html          build
  python build.py deck.json --out deck.html --pdf deck.pdf   (+ PDF, needs playwright)
  python build.py --extract deck.html > deck.json    recover the source from a built deck
  python build.py --layouts                           list layouts and their fields

Exit code 1 when there are errors.
"""
import argparse, base64, colorsys, hashlib, html, json, mimetypes, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import art as ART

HERE = os.path.dirname(os.path.abspath(__file__))
TEMPLATE = os.path.join(HERE, "..", "assets", "template.html")

# ------------------------------------------------------------------ color
def rgb(h):
    h = h.strip().lstrip("#")
    if len(h) == 3: h = "".join(c * 2 for c in h)
    if not re.fullmatch(r"[0-9a-fA-F]{6}", h): raise ValueError(f"Not a hex color: #{h}")
    return tuple(int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))
def hx(c): return "#" + "".join(f"{round(max(0, min(1, v)) * 255):02x}" for v in c)
def mix(a, b, t):
    A, B = rgb(a), rgb(b); return hx(tuple(A[i] + (B[i] - A[i]) * t for i in range(3)))
def lum(h):
    f = lambda v: v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
    r, g, b = (f(v) for v in rgb(h)); return 0.2126 * r + 0.7152 * g + 0.0722 * b
def cr(a, b):
    x, y = lum(a), lum(b); return (max(x, y) + 0.05) / (min(x, y) + 0.05)
def towards(c, against, target, d):
    if cr(c, against) >= target: return c
    r_, g_, b_ = rgb(c); hh, l, s = colorsys.rgb_to_hls(r_, g_, b_)
    for _ in range(100):
        l = max(0, min(1, l + 0.01 * d)); c2 = hx(colorsys.hls_to_rgb(hh, l, s))
        if cr(c2, against) >= target: return c2
    return "#000000" if d < 0 else "#ffffff"
def best(fill, cands): return max(cands, key=lambda c: cr(c, fill))

def tokens(brand):
    P = brand.get("primary", "#1f3354")
    A = brand.get("accent") or None
    bgv = str(brand.get("background", "light")).lower()
    dark = bgv == "dark" or (bgv.startswith("#") and lum(bgv) < 0.2)
    block = A if (A and brand.get("block", "accent") != "primary") else P
    if not dark:
        paper = bgv if bgv.startswith("#") else mix("#ffffff", P, 0.018)
        paper2 = mix(paper, P, 0.065)
        line = mix(paper, P, 0.16); line_s = mix(paper, P, 0.34)
        ink = towards(mix("#0c0e11", P, 0.16), paper, 14, -1)
        text = towards(mix("#16181c", P, 0.10), paper, 11, -1)
        muted = towards(mix(text, paper, 0.42), paper, 4.8, -1)
        night = P if lum(P) < 0.09 else mix("#111318", P, 0.32)
        art_dark, art_light = night, paper
        d = -1
    else:
        paper = bgv if bgv.startswith("#") else mix("#0e0f13", P, 0.10)
        paper2 = mix(paper, "#ffffff", 0.07)
        line = mix(paper, "#ffffff", 0.14); line_s = mix(paper, "#ffffff", 0.3)
        ink = towards(mix("#ffffff", P, 0.08), paper, 14, 1)
        text = towards(mix("#eceef2", P, 0.06), paper, 11, 1)
        muted = towards(mix(text, paper, 0.4), paper, 4.8, 1)
        night = mix(P, "#000000", 0.25) if cr(mix(P, "#000000", 0.25), paper) > 1.35 else mix(paper, "#ffffff", 0.12)
        art_dark, art_light = mix(P, "#ffffff", 0.45), mix(paper, P, 0.25)
        d = 1
    on_block = best(block, ["#111111", "#ffffff", ink])
    block_text = towards(block, paper, 4.5, d)
    on_night = best(night, ["#ffffff", "#111111"])
    mark_night = block if cr(block, night) >= 2.2 else on_night
    chrome = mix("#18191c", P, 0.10)
    fonts = brand.get("fonts", {})
    fd = fonts.get("display") or "Archivo"; ft = fonts.get("text") or fd
    serif = lambda n: bool(re.search(r"serif|fraunces|playfair|lora|merriweather|newsreader|garamond|crimson|spectral|baskerville", n, re.I)) and not re.search(r"sans", n, re.I)
    stack = lambda n: f'"{n}",' + ('Georgia,"Times New Roman",serif' if serif(n) else 'system-ui,-apple-system,"Segoe UI",Arial,sans-serif')
    t = {"--paper": paper, "--paper-2": paper2, "--line": line, "--line-strong": line_s, "--ink": ink, "--text": text, "--muted": muted,
         "--block": block, "--on-block": on_block, "--mark-night": mark_night, "--block-text": block_text, "--night": night, "--on-night": on_night,
         "--focus": block_text, "--ok": "#2e7d4f" if not dark else "#5cc28a", "--bad": "#b3261e" if not dark else "#ff8a80",
         "--chrome-bg": chrome, "--chrome-panel": mix(chrome, "#ffffff", 0.06), "--chrome-text": "#e8e9ec",
         "--f-display": stack(fd), "--f-text": stack(ft),
         "--w-display": str(fonts.get("display_weight", 800 if fd == "Archivo" else 700)),
         "--tr-display": fonts.get("display_tracking", "-0.03em" if not serif(fd) else "-0.015em")}
    checks = [("text on paper", text, paper, 7), ("headings on paper", ink, paper, 7), ("muted on paper", muted, paper, 4.5),
              ("block color as text", block_text, paper, 4.5), ("text on color block", on_block, block, 4.5),
              ("text on dark panel", on_night, night, 4.5)]
    report = [(n, round(cr(a, b), 2), need) for n, a, b, need in checks]
    return t, report, dark, (fd, ft), (art_dark, art_light)

def fonts_link(names):
    sysf = {"system-ui", "arial", "helvetica", "georgia", "times new roman", "segoe ui", "verdana", "calibri"}
    fams = ["family=" + n.replace(" ", "+") + ":ital,wght@0,400;0,600;0,700;0,800;1,400" for n in dict.fromkeys(names) if n.lower() not in sysf]
    if not fams: return ""
    url = "https://fonts.googleapis.com/css2?" + "&".join(fams) + "&display=swap"
    return ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
            f'<link rel="stylesheet" href="{html.escape(url)}">')

# ------------------------------------------------------------------ text helpers
def esc(s): return html.escape(str(s or ""), quote=True)
def md(s):
    """Escape, then allow **bold** only."""
    return re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", esc(s))
def words(s): return len(re.findall(r"[\w'’\-]+", str(s or "")))

def data_uri(path, base):
    if not path: return ""
    if str(path).startswith(("data:", "http://", "https://")): return path
    p = path if os.path.isabs(path) else os.path.join(base, path)
    if not os.path.exists(p):
        WARN.append(f"Image not found: {path}"); return ""
    with open(p, "rb") as f: b = f.read()
    return f"data:{mimetypes.guess_type(p)[0] or 'image/png'};base64," + base64.b64encode(b).decode()

# ------------------------------------------------------------------ state
WARN, ERR = [], []
CTX = {}

def visual(sl, i, cls, w=800, h=900):
    """Art panel or user image for a slide."""
    img = sl.get("image")
    if img:
        src = data_uri(img, CTX["base"])
        if src:
            mono = " mono" if sl.get("mono", True) else ""
            return f'<div class="art {cls}"><img class="{mono.strip()}" src="{src}" alt="{esc(sl.get("alt",""))}"></div>'
    a = sl.get("art") or {}
    if isinstance(a, str): a = {"style": a}
    styles = CTX["styles"]
    hv = stable(sl, i)
    style = a.get("style") or styles[hv % len(styles)]
    if style not in ART.STYLES:
        WARN.append(f"Slide {i+1}: unknown art style '{style}', using {styles[0]}"); style = styles[0]
    seed = a.get("seed", hv % 997)
    return f'<div class="art {cls}">{ART.panel(style, seed, CTX["art_dark"], CTX["art_light"], w, h, uid=f"s{i}")}</div>'

def stable(sl, i):
    """A number that depends on the slide's id/title, not its position, so inserting slides doesn't reshuffle the art."""
    key = str(sl.get("id") or sl.get("title") or sl.get("quote") or sl.get("layout", "")) or str(i)
    return int(hashlib.md5(key.encode("utf-8")).hexdigest()[:8], 16)

def thumb(it, i, j):
    if it.get("image"):
        src = data_uri(it["image"], CTX["base"])
        if src: return f'<div class="thumb"><img class="mono" src="{src}" alt=""></div>'
    a = it.get("art")
    if a is None: return ""
    if isinstance(a, str): a = {"style": a}
    h = stable(it, i) + j
    st = a.get("style") or CTX["styles"][h % len(CTX["styles"])]
    return f'<div class="thumb">{ART.panel(st, a.get("seed", h % 997), CTX["art_dark"], CTX["art_light"], 600, 300, uid=f"t{i}_{j}")}</div>'

def head(sl, size="t-l", tag="h2"):
    out = ""
    if sl.get("kicker"): out += f'<p class="k">{md(sl["kicker"])}</p>'
    if sl.get("title"): out += f'<{tag} class="{size}">{md(sl["title"])}</{tag}>'
    return out
def body(sl, key="text", cls="b"):
    return f'<p class="{cls}">{md(sl[key])}</p>' if sl.get(key) else ""
def bullets(sl):
    bs = sl.get("bullets") or []
    if not bs: return ""
    li = []
    for b in bs:
        if isinstance(b, dict): li.append(f'<li><span><b>{md(b.get("title",""))}</b> {md(b.get("text",""))}</span></li>')
        else: li.append(f"<li><span>{md(b)}</span></li>")
    return '<ul class="bul">' + "".join(li) + "</ul>"
def meta(items):
    if not items: return ""
    return '<div class="meta">' + "".join(f'<div><span>{md(m.get("label",""))}</span>{md(m.get("value",""))}</div>' for m in items) + "</div>"

# ------------------------------------------------------------------ charts
def chart(c, i):
    t = (c or {}).get("type")
    if t in ("bars", "columns"):
        data = c.get("data") or []
        mx = c.get("max") or max([float(d.get("value", 0)) for d in data] + [1])
        suf = c.get("suffix", ""); pre = c.get("prefix", "")
        def fmt(v):
            v = float(v); return (f"{v:,.0f}" if v == int(v) else f"{v:,.1f}")
        if t == "bars":
            rows = "".join(f'<div class="bar{" hl" if d.get("hl") else ""}"><span class="bk">{md(d.get("label",""))}</span><span class="tr"><span class="fl" data-pct="{100*float(d.get("value",0))/mx:.2f}"></span></span><span class="bv">{esc(pre)}{fmt(d.get("value",0))}{esc(suf)}</span></div>' for d in data)
            return f'<div class="bars">{rows}</div>'
        cols = "".join(f'<div class="c{" hl" if d.get("hl") else ""}"><span class="cv">{esc(pre)}{fmt(d.get("value",0))}{esc(suf)}</span><span class="fl" data-pct="{100*float(d.get("value",0))/mx:.2f}"></span><span class="ck">{md(d.get("label",""))}</span></div>' for d in data)
        return f'<div class="colsch">{cols}</div>'
    if t == "timeline":
        pts = c.get("points") or []
        ps = []
        for p in pts:
            cl = p.get("state", "")
            was = f'<s>{md(p["was"])}</s>' if p.get("was") else ""
            tag = f'<span class="tag">{md(p["tag"])}</span>' if p.get("tag") else ""
            ps.append(f'<div class="p {esc(cl)}"><span class="dot"></span><div class="d">{was}{md(p.get("date",""))}</div><div class="x">{md(p.get("text",""))}{"<br>" if tag else ""}{tag}</div></div>')
        return f'<div class="tl" style="--n:{max(1,len(pts))}">{"".join(ps)}</div>'
    if t == "gantt":
        rows = []
        for r in c.get("rows") or []:
            bars = "".join(f'<span class="g-bar {esc(b.get("kind",""))}" data-start="{esc(b.get("start"))}"{" data-end=%s" % json.dumps(str(b["end"])) if b.get("end") else ""}>{md(b.get("text",""))}</span>' for b in r.get("bars") or [])
            sub = f'<br><span>{md(r["sub"])}</span>' if r.get("sub") else ""
            lab = f'<b>{md(r.get("label",""))}</b>' if r.get("sub") else md(r.get("label", ""))
            rows.append(f'<div class="g-row"><span class="g-lab">{lab}{sub}</span><div class="g-trk">{bars}</div></div>')
        marks = "".join(f'<span class="g-mark" data-at="{esc(m.get("at"))}"><span>{md(m.get("text",""))}</span></span>' for m in c.get("marks") or [])
        return (f'<div class="gantt" data-gantt data-from="{esc(c.get("from"))}" data-to="{esc(c.get("to"))}">'
                f'<div class="g-axis"><span></span><div class="g-scale"></div></div>{"".join(rows)}{marks}</div>')
    if t == "items":
        its = c.get("items") or []
        return '<div class="items" style="--n:%d">' % max(1, len(its)) + "".join(
            f'<div class="it{" hl" if it.get("hl") else ""}"><b>{md(it.get("title",""))}</b><p>{md(it.get("text",""))}</p></div>' for it in its) + "</div>"
    ERR.append(f"Unknown chart type '{t}' (use bars, columns, timeline, gantt or items)")
    return ""

# ------------------------------------------------------------------ layouts
def L_cover(sl, i):
    logo = f'<div class="lg"><img class="logo" src="{CTX["logo"]}" alt="{esc(CTX["org"])}"></div>' if CTX["logo"] else ""
    return (visual(sl, i, "", 620, 900) + '<div class="blk b1"></div><div class="blk b2"></div>' + logo +
            f'<div class="tx">{head(sl,"t-xl","h1")}{body(sl,"subtitle","lead")}{meta(sl.get("meta"))}</div>')

def L_agenda(sl, i):
    items = []
    n = 0
    for p in CTX["parts"]:
        if p.get("hide"): continue
        n += 1
        items.append(f'<button class="ai" data-go="{p["first"]}"><span class="n">{n:02d}</span><span><b>{md(p["title"])}</b><span>{md(p.get("desc",""))}</span></span><span class="m">{p.get("minutes","")} {"min" if p.get("minutes") else ""}</span></button>')
    return (visual(sl, i, "", 1600, 280) + '<div class="shade"></div>' + f'<h2 class="t-l">{md(sl.get("title") or "Agenda")}</h2>' +
            f'<div class="alist">{"".join(items)}</div>')

def L_section(sl, i):
    return (visual(sl, i, "", 1600, 900) + '<div class="veil"></div>' +
            f'<div class="sq on-block"><span>{md(sl.get("label",""))}</span><b>{esc(sl.get("number",""))}</b></div>' +
            f'<div class="tx">{head(sl)}{body(sl,"text","lead")}</div>')

def L_statement(sl, i):
    return (visual(sl, i, "", 380, 900) + '<div class="blk b1"></div>' + f'<div class="tx">{head(sl,"t-l")}{body(sl,"text","lead")}</div>')

def L_split(sl, i):
    kind = "on-night" if sl.get("tone") == "dark" else "on-block"
    strip = f'<div class="strip nite-s" style="background:var(--night)"><span>{esc(sl.get("label",""))}</span></div>'
    return (f'<div class="half {kind}"></div>' + strip + visual(sl, i, "", 764, 900) +
            f'<div class="tx {kind}" style="background:none">{head(sl,"t-l")}{body(sl)}{bullets(sl)}</div>')

def L_frame(sl, i):
    return ('<div class="edge"></div><div class="blk b1"></div>' + visual(sl, i, "", 540, 560) +
            f'<div class="tx">{head(sl,"t-l")}{body(sl)}{bullets(sl)}</div>')

def L_columns(sl, i):
    its = (sl.get("items") or [])[:4]
    numbered = sl.get("numbered", True)
    cols = []
    for j, it in enumerate(its):
        top = f'<span class="ic">{ART.icon(it["icon"])}</span>' if it.get("icon") else (f'<span class="num">{j+1:02d}</span>' if numbered else "")
        th = thumb(it if (it.get("art") or it.get("image")) else dict(it, art={}), i, j) if sl.get("thumbs", True) else thumb(it, i, j)
        cols.append(f'<div class="col">{top}<h3>{md(it.get("title",""))}</h3><p>{md(it.get("text",""))}</p>{th}</div>')
    return (f'<div class="edge"></div><div class="tx hd">{head(sl)}</div>' +
            f'<div class="cols" style="--n:{max(1,len(its))}">{"".join(cols)}</div>')

def L_process(sl, i):
    st = (sl.get("steps") or [])[:5]
    n = max(1, len(st))
    xs = [96 + 150 + k * ((1408 - 300) / max(1, n - 1)) for k in range(n)] if n > 1 else [800]
    ys = [430 if k % 2 == 0 else 520 for k in range(n)]
    pts = " ".join(f"{x:.0f},{y + 52:.0f}" for x, y in zip(xs, ys))
    wire = f'<svg class="wire" viewBox="0 0 1600 900" aria-hidden="true"><polyline points="{pts}" fill="none" stroke="var(--line-strong)" stroke-width="3" stroke-dasharray="2 10" stroke-linecap="round"/></svg>'
    out = []
    for k, (s, x, y) in enumerate(zip(st, xs, ys)):
        ic = ART.icon(s.get("icon") or "arrow")
        out.append(f'<div class="st" style="left:{x:.0f}px;top:{y:.0f}px"><span class="sq">{ic}</span><span class="no">{k+1:02d}</span><b>{md(s.get("title",""))}</b><p>{md(s.get("text",""))}</p></div>')
    return f'<div class="tx hd">{head(sl)}</div>' + wire + "".join(out) + '<div class="band"></div>'

def L_number(sl, i):
    kind = "on-night" if sl.get("tone") == "dark" else "on-block"
    return (f'<div class="half {kind}"><div class="fig">{esc(sl.get("value",""))}</div><div class="unit">{md(sl.get("unit",""))}</div><p class="cap">{md(sl.get("caption",""))}</p></div>' +
            f'<div class="tx">{head(sl,"t-l")}{body(sl)}{bullets(sl)}</div>')

def L_dark(sl, i):
    return (visual(sl, i, "", 940, 900) + '<div class="nite pnl"></div><div class="blk b1"></div>' +
            f'<div class="tx on-night" style="background:none">{head(sl,"t-l")}{body(sl)}{bullets(sl)}</div>')

def L_chart(sl, i):
    note = sl.get("note") or {}
    wide = " wide" if (sl.get("wide") or not note) else ""
    nt = ""
    if note and not wide:
        fig = f'<div class="fig">{esc(note["value"])}</div>' if note.get("value") else ""
        nt = f'<div class="note on-night">{fig}<p>{md(note.get("text",""))}</p></div>'
    return f'<div class="tx hd">{head(sl)}</div><div class="plot">{chart(sl.get("chart"), i)}</div>{nt}', wide

def L_compare(sl, i):
    states = sl.get("states") or []
    dflt = sl.get("default", len(states) - 1)
    btns = "".join(f'<button type="button" data-key="s{j}">{md(s.get("label",""))}</button>' for j, s in enumerate(states))
    panes = "".join(f'<div class="pane" data-pane="s{j}">{chart(s.get("chart"), i)}</div>' for j, s in enumerate(states))
    return (f'<div class="tx hd">{head(sl)}</div><div data-switch="s{dflt}"><div class="seg" role="group">{btns}</div>'
            f'<div class="panes">{panes}</div></div>')

def L_quote(sl, i):
    who = f'<p class="who"><b>{md(sl.get("who",""))}</b>{", " + md(sl["role"]) if sl.get("role") else ""}</p>'
    return (visual(sl, i, "", 460, 900) + '<div class="mark" aria-hidden="true">“</div>' +
            f'<div class="tx"><blockquote>{md(sl.get("quote",""))}</blockquote>{who}</div>')

def L_quiz(sl, i):
    opts = "".join(f'<button type="button"{" data-correct" if o.get("correct") else ""} data-explain="{esc(o.get("why",""))}"><i>{chr(65+j)}</i><span>{md(o.get("text",""))}</span></button>'
                   for j, o in enumerate(sl.get("options") or []))
    return (f'<div data-quiz><div class="tx hd">{head(sl,"t-m")}</div><div class="opts">{opts}</div>'
            f'<div class="pnl on-night"><p class="k">{md(sl.get("panel_title") or ("La respuesta" if CTX["lang"]=="es" else "The answer"))}</p><p class="fb" aria-live="polite"></p><p class="hint">{md(sl.get("hint",""))}</p></div></div>')

def L_checklist(sl, i):
    its = "".join(f'<label><input type="checkbox"><span>{md(t)}</span></label>' for t in (sl.get("items") or [])[:7])
    return (f'<div data-checklist><div class="tx hd">{head(sl)}</div><div class="list">{its}</div>'
            f'<div class="pnl on-block"><div class="cnt" data-count></div><p>{md(sl.get("note",""))}</p></div></div>')

def L_mosaic(sl, i):
    tiles = []
    for j, t in enumerate((sl.get("tiles") or [])[:6]):
        cls = "tile" + (" wide" if t.get("wide") else "")
        tone = t.get("tone")
        if tone == "block": cls += " on-block"
        elif tone == "dark": cls += " on-night"
        inner = ""
        if t.get("art") or t.get("image"):
            inner += thumb({"art": t.get("art") or {}, "image": t.get("image")}, i, j).replace('class="thumb"', 'style="position:absolute;inset:0"')
        if t.get("value"): inner += f'<span class="v" style="position:relative">{esc(t["value"])}</span>'
        if t.get("label"): inner += f'<span class="l" style="position:relative">{md(t["label"])}</span>'
        tiles.append(f'<div class="{cls}">{inner}</div>')
    return f'<div class="tx hd">{head(sl)}</div><div class="grid">{"".join(tiles)}</div>'

def L_sources(sl, i):
    rows = "".join(f'<tr><td>{("<a href=%s>" % json.dumps(r["url"])) if r.get("url") else ""}{md(r.get("source",""))}{"</a>" if r.get("url") else ""}</td><td>{md(r.get("use",""))}</td></tr>' for r in sl.get("rows") or [])
    th = sl.get("headers") or (["Source", "Used for"] if CTX["lang"] != "es" else ["Fuente", "Para qué"])
    return f'<div class="tx hd">{head(sl)}</div><table><thead><tr><th>{esc(th[0])}</th><th>{esc(th[1])}</th></tr></thead><tbody>{rows}</tbody></table>'

def L_closing(sl, i):
    kind = "on-night" if sl.get("tone") == "dark" else "on-block"
    return (f'<div class="half {kind}"></div>' + visual(sl, i, "", 700, 900) +
            f'<div class="tx {kind}" style="background:none">{head(sl,"t-xl")}{body(sl,"text","lead")}{meta(sl.get("meta"))}</div>')

LAYOUTS = {
    "cover": (L_cover, {"title": 12, "subtitle": 25}, ["title"]),
    "agenda": (L_agenda, {}, []),
    "section": (L_section, {"title": 12, "text": 25}, ["title", "number"]),
    "statement": (L_statement, {"title": 18, "text": 40}, ["title"]),
    "split": (L_split, {"title": 14, "text": 45}, ["title"]),
    "frame": (L_frame, {"title": 14, "text": 45}, ["title"]),
    "columns": (L_columns, {"title": 16}, ["title", "items"]),
    "process": (L_process, {"title": 16}, ["title", "steps"]),
    "number": (L_number, {"title": 14, "text": 40, "caption": 22}, ["value", "title"]),
    "dark": (L_dark, {"title": 14, "text": 45}, ["title"]),
    "chart": (L_chart, {"title": 16}, ["title", "chart"]),
    "compare": (L_compare, {"title": 16}, ["title", "states"]),
    "quote": (L_quote, {"quote": 40}, ["quote", "who"]),
    "quiz": (L_quiz, {"title": 22}, ["title", "options"]),
    "checklist": (L_checklist, {"title": 14, "note": 30}, ["title", "items"]),
    "mosaic": (L_mosaic, {"title": 16}, ["title", "tiles"]),
    "sources": (L_sources, {}, ["rows"]),
    "closing": (L_closing, {"title": 8, "text": 25}, ["title"]),
}
VISUAL = {"cover", "agenda", "section", "split", "frame", "columns", "process", "number", "dark", "chart", "compare", "quote", "mosaic", "closing", "quiz", "checklist"}
LABEL_TITLES = {"agenda", "sources", "quote", "closing", "cover", "section"}

def check_slide(sl, i):
    lay = sl.get("layout")
    _, budget, req = LAYOUTS[lay]
    for r in req:
        if not sl.get(r) and not (lay == "agenda"):
            ERR.append(f"Slide {i+1} ({lay}): missing '{r}'")
    for k, lim in budget.items():
        n = words(sl.get(k))
        if n > lim: WARN.append(f"Slide {i+1} ({lay}): '{k}' has {n} words (max {lim}). Cut it or move detail to notes.")
    for b in sl.get("bullets") or []:
        n = words(b if isinstance(b, str) else (b.get("title", "") + " " + b.get("text", "")))
        if n > 16: WARN.append(f"Slide {i+1}: a bullet has {n} words (max 16)")
    if len(sl.get("bullets") or []) > 5: WARN.append(f"Slide {i+1}: more than 5 bullets")
    for it in (sl.get("items") or []):
        if isinstance(it, dict) and words(it.get("text")) > 30: WARN.append(f"Slide {i+1}: an item text has {words(it.get('text'))} words (max 30)")
        if isinstance(it, str) and words(it) > 18: WARN.append(f"Slide {i+1}: a checklist item has {words(it)} words (max 18)")
    for s in (sl.get("steps") or []):
        if words(s.get("text")) > 18: WARN.append(f"Slide {i+1}: a step text has {words(s.get('text'))} words (max 18)")
    if lay not in LABEL_TITLES and sl.get("title") and words(sl["title"]) < 4:
        WARN.append(f"Slide {i+1} ({lay}): title '{sl['title']}' is a label. Write the takeaway as a sentence.")
    if lay not in ("agenda", "sources") and not str(sl.get("notes", "")).strip():
        WARN.append(f"Slide {i+1} ({lay}): no speaker notes")
    blob = json.dumps({k: v for k, v in sl.items() if k not in ("notes", "source", "art", "image", "number", "layout", "id", "part")}, ensure_ascii=False)
    if lay not in ("cover", "agenda", "sources", "closing", "section", "quiz", "checklist") and re.search(r"\d{2,}|%|€|\$", blob) and not sl.get("source"):
        WARN.append(f"Slide {i+1} ({lay}): has figures or dates but no 'source'")

def build(deck, base):
    WARN.clear(); ERR.clear()
    brand = deck.get("brand") or {}
    if not brand.get("primary"): ERR.append("brand.primary is required")
    t, report, dark, fonts, artc = tokens(brand if brand.get("primary") else {"primary": "#1f3354"})
    for n, r, need in report:
        if r < need: ERR.append(f"Contrast too low: {n} {r}:1 (needs {need}:1). Adjust the brand color.")
    fmt = deck.get("format", "slides")
    sty = brand.get("art") or ["lines", "contour"]
    if isinstance(sty, str): sty = [sty]
    CTX.update(base=base, art_dark=artc[0], art_light=artc[1], styles=[s for s in sty if s in ART.STYLES] or ["lines"],
               logo=data_uri(brand.get("logo"), base) if brand.get("logo") else "", org=brand.get("name", ""), lang=deck.get("lang", "en"))
    slides = deck.get("slides") or []
    if not slides: ERR.append("No slides")
    # parts
    parts, cur = [], None
    pmeta = {p["title"]: p for p in deck.get("parts") or [] if p.get("title")}
    for i, sl in enumerate(slides):
        p = sl.get("part") or cur or (deck.get("title") or "Deck")
        if p != cur:
            m = pmeta.get(p, {})
            parts.append({"title": p, "first": i, "desc": m.get("desc", ""), "minutes": m.get("minutes"), "hide": m.get("hide", i == 0), "n": 0})
            cur = p
        parts[-1]["n"] += 1
    total = deck.get("minutes") or sum((p["minutes"] or 0) for p in parts) or len(slides) * 2
    psum = sum((p["minutes"] or 0) for p in parts)
    if deck.get("minutes") and all(p["minutes"] for p in parts) and psum != deck["minutes"]:
        WARN.append(f"Parts add up to {psum} min but the deck says {deck['minutes']} min")
    known = sum(p["minutes"] or 0 for p in parts); unknown = [p for p in parts if not p["minutes"]]
    left = max(0, total - known); cnt = sum(p["n"] for p in unknown) or 1
    for p in unknown: p["minutes"] = max(1, round(left * p["n"] / cnt))
    CTX["parts"] = parts
    if not (deck.get("story") or {}).get("thesis"): WARN.append("story.thesis is missing: write the one sentence the audience must remember.")
    # render
    out, text_run = [], 0
    for i, sl in enumerate(slides):
        lay = sl.get("layout")
        if lay not in LAYOUTS:
            ERR.append(f"Slide {i+1}: unknown layout '{lay}'. Use one of: {', '.join(LAYOUTS)}"); continue
        check_slide(sl, i)
        text_run = 0 if lay in VISUAL else text_run + 1
        if text_run == 3: WARN.append(f"Slides {i-1}–{i+1}: three text-only slides in a row. Turn one into a chart, number, process or mosaic.")
        res = LAYOUTS[lay][0](sl, i)
        extra = ""
        if isinstance(res, tuple): res, extra = res
        ink = ""
        if lay == "split": ink = " ink-night" if sl.get("tone") == "dark" else " ink-block"
        src = f'<p class="src{ink}">{md(sl["source"])}</p>' if sl.get("source") else ""
        foot = f'<div class="foot{ink}"><span>{esc(deck.get("footer") or brand.get("name",""))}</span><span class="pg">{i+1:02d}</span></div>' if lay not in ("cover", "closing") else ""
        sid = esc(sl.get("id") or f"s{i+1}")
        out.append(f'<section class="slide L-{lay}{extra}" id="{sid}" data-notes="{esc(sl.get("notes",""))}">{res}{src}{foot}</section>')
    # assemble
    with open(TEMPLATE, encoding="utf-8") as f: src = f.read()
    css = "\n".join(f"  {k}:{v};" for k, v in t.items()) + ("\n  color-scheme:dark;" if dark else "") + "\n"
    if fmt == "carousel":
        css += "  --W:1080px;--H:1350px;\n"
    page = "@page{size:1080px 1350px;margin:0}" if fmt == "carousel" else "@page{size:1600px 900px;margin:0}"
    cfg = {"title": deck.get("title", "Deck"), "lang": CTX["lang"], "format": fmt, "org": CTX["org"],
           "parts": [{"title": p["title"], "first": p["first"], "minutes": p["minutes"]} for p in parts]}
    if deck.get("strings"): cfg["strings"] = deck["strings"]
    jsafe = lambda o: json.dumps(o, ensure_ascii=False).replace("</", "<\\/")
    src = (src.replace("{{TITLE}}", esc(cfg["title"])).replace("/*BRAND*/\n", css).replace("/*PAGE*/", page)
           .replace("<!--FONTS-->", fonts_link(fonts)).replace("<!--SLIDES-->", "\n".join(out))
           .replace("/*CONFIG*/", jsafe(cfg)).replace("/*SOURCE*/", jsafe(deck))
           .replace('<html lang="en">', f'<html lang="{esc(CTX["lang"])}">', 1))
    return src, report, len(out), parts

def main():
    ap = argparse.ArgumentParser(description="Build an html-deck from deck.json")
    ap.add_argument("deck", nargs="?", help="deck.json")
    ap.add_argument("--out", help="output .html")
    ap.add_argument("--pdf", help="also export a PDF (needs playwright + chromium)")
    ap.add_argument("--extract", metavar="HTML", help="print the deck.json embedded in a built deck")
    ap.add_argument("--layouts", action="store_true", help="list layouts and required fields")
    a = ap.parse_args()
    if a.layouts:
        for k, (_, b, req) in LAYOUTS.items(): print(f"{k:10} required: {', '.join(req) or '-'}  word limits: {b or '-'}")
        return
    if a.extract:
        s = open(a.extract, encoding="utf-8").read()
        m = re.search(r'<script type="application/json" id="deck-source">(.*?)</script>', s, re.S)
        if not m: sys.exit("No embedded deck source found")
        print(json.dumps(json.loads(m.group(1).replace("<\\/", "</")), ensure_ascii=False, indent=2)); return
    if not (a.deck and a.out): ap.error("deck.json and --out are required")
    try:
        deck = json.load(open(a.deck, encoding="utf-8"))
    except json.JSONDecodeError as e:
        sys.exit(f"ERROR deck.json is not valid JSON: {e}")
    html_, report, n, parts = build(deck, os.path.dirname(os.path.abspath(a.deck)))
    if not ERR or n:
        os.makedirs(os.path.dirname(os.path.abspath(a.out)) or ".", exist_ok=True)
        open(a.out, "w", encoding="utf-8").write(html_)
    print(f"Built {a.out} · {n} slides · {len(html_)//1024} KB · {deck.get('format','slides')} · {deck.get('lang','en')}")
    story = deck.get("story") or {}
    print("\nHEADLINES (read them alone: do they tell the story?)")
    if story.get("thesis"): print(f"  Thesis: {story['thesis']}")
    pfirst = {p["first"]: p["title"] for p in parts}
    for i, sl in enumerate(deck.get("slides") or []):
        if i in pfirst: print(f"  — {pfirst[i]}")
        t = sl.get("title") or sl.get("quote") or ""
        print(f"  {i+1:02d} [{sl.get('layout')}] {re.sub(r'[*]', '', str(t))}")
    print()
    for w in WARN: print("WARN ", w)
    for e in ERR: print("ERROR", e)
    if not WARN and not ERR: print("No warnings.")
    if a.pdf and not ERR:
        try:
            from playwright.sync_api import sync_playwright
            fmt = deck.get("format", "slides")
            with sync_playwright() as p:
                b = p.chromium.launch(); pg = b.new_page()
                pg.goto("file://" + os.path.abspath(a.out)); pg.wait_for_timeout(1500); pg.emulate_media(media="print")
                w, h = ("1080px", "1350px") if fmt == "carousel" else ("1600px", "900px")
                pg.pdf(path=a.pdf, width=w, height=h, print_background=True, prefer_css_page_size=True); b.close()
            print("PDF  ", a.pdf)
        except Exception as ex:
            print("WARN  PDF skipped:", ex, "— open the deck in Chrome and press P.")
    sys.exit(1 if ERR else 0)

if __name__ == "__main__":
    main()
