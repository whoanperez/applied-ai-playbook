"""
html-deck · art.py (MIT)
Procedural art panels (SVG) that take the place of photographs, plus a small
line-icon set. Everything is generated from a style name, a seed and the
brand's dark/light tones, so it is deterministic, offline and print-safe.
"""
import math, random

STYLES = ("lines", "waves", "contour", "arcs", "columns", "dots")

def _mix(a, b, t):
    a = a.lstrip("#"); b = b.lstrip("#")
    A = [int(a[i:i + 2], 16) for i in (0, 2, 4)]
    B = [int(b[i:i + 2], 16) for i in (0, 2, 4)]
    return "#" + "".join(f"{round(A[i] + (B[i] - A[i]) * t):02x}" for i in range(3))

def _f(x):
    return f"{x:.1f}".rstrip("0").rstrip(".")

def panel(style, seed, dark, light, w=800, h=900, uid="a"):
    """Return an <svg> string that fills its box (slice)."""
    r = random.Random(f"{style}-{seed}")
    tones = [_mix(light, dark, t) for t in (0.0, 0.18, 0.38, 0.6, 0.82, 1.0)]
    fn = {"lines": _lines, "waves": _waves, "contour": _contour, "arcs": _arcs,
          "columns": _columns, "dots": _dots}.get(style, _lines)
    body = fn(r, w, h, tones, uid)
    return (f'<svg class="art-svg" viewBox="0 0 {w} {h}" preserveAspectRatio="xMidYMid slice" '
            f'xmlns="http://www.w3.org/2000/svg" aria-hidden="true">{body}</svg>')

def _grad(uid, name, c1, c2, x2="0", y2="1"):
    return (f'<linearGradient id="{uid}{name}" x1="0" y1="0" x2="{x2}" y2="{y2}">'
            f'<stop offset="0" stop-color="{c1}"/><stop offset="1" stop-color="{c2}"/></linearGradient>')

def _lines(r, w, h, t, uid):
    # Looking up at a tower: planes converging to a vanishing point above the panel.
    vx, vy = w * r.uniform(0.35, 0.65), -h * r.uniform(0.6, 1.1)
    out = [f"<defs>{_grad(uid,'g',t[0],t[2])}{_grad(uid,'p',t[4],t[5])}{_grad(uid,'q',t[2],t[3])}</defs>",
           f'<rect width="{w}" height="{h}" fill="url(#{uid}g)"/>']
    xs = sorted(r.uniform(-w * 0.6, w * 1.6) for _ in range(9))
    for i in range(0, len(xs) - 1, 2):
        a, b = xs[i], xs[i + 1]
        fill = f"url(#{uid}p)" if i % 4 == 0 else f"url(#{uid}q)"
        out.append(f'<path d="M{_f(a)} {h} L{_f(b)} {h} L{_f(vx)} {_f(vy)} Z" fill="{fill}" opacity="{r.uniform(.55,.95):.2f}"/>')
    for k in range(46):
        x = -w * 0.8 + k * (w * 2.6 / 46) + r.uniform(-6, 6)
        out.append(f'<line x1="{_f(x)}" y1="{h}" x2="{_f(vx)}" y2="{_f(vy)}" stroke="{t[0]}" stroke-width="{r.choice([0.8,1.2,1.6])}" opacity="{r.uniform(.25,.6):.2f}"/>')
    # horizontal floor lines, compressed toward the vanishing point
    for k in range(1, 14):
        y = h - (h * 1.25) * (1 - 1 / (1 + k * 0.32))
        out.append(f'<line x1="0" y1="{_f(y)}" x2="{w}" y2="{_f(y)}" stroke="{t[5]}" stroke-width="1" opacity=".18"/>')
    return "".join(out)

def _waves(r, w, h, t, uid):
    # Op-art ribbons: equal dark/light bands that bend together, with a slow phase drift.
    n = r.randint(14, 18)
    amp = h * r.uniform(0.06, 0.1)
    freq = r.uniform(1.2, 2.0) * math.pi / w
    drift = r.uniform(0.18, 0.32)
    band = (h * 1.6) / n
    out = [f'<rect width="{w}" height="{h}" fill="{t[0]}"/>', f'<g transform="rotate({r.uniform(-12,12):.1f} {w/2} {h/2})">']
    def y_at(i, x):
        ph = i * drift
        return -h * 0.3 + i * band + amp * math.sin(freq * x + ph) + amp * 0.18 * math.sin(freq * 1.7 * x - ph)
    for i in range(0, n, 1):
        if i % 2:
            continue
        xs = [-w * 0.25 + s * (w * 1.5 / 120) for s in range(121)]
        top = [(x, y_at(i, x)) for x in xs]
        bot = [(x, y_at(i + 1, x)) for x in reversed(xs)]
        d = "M" + " L".join(f"{_f(x)} {_f(y)}" for x, y in top + bot) + " Z"
        out.append(f'<path d="{d}" fill="{t[5]}"/>')
    out.append("</g>")
    return "".join(out)

def _contour(r, w, h, t, uid):
    cx, cy = w * r.uniform(0.3, 0.7), h * r.uniform(0.3, 0.7)
    out = [f'<rect width="{w}" height="{h}" fill="{t[0]}"/>']
    ph = [r.uniform(0, 6.28) for _ in range(4)]
    for k in range(34, 0, -1):
        R = k * max(w, h) / 30
        pts = []
        for s in range(0, 73):
            a = s / 72 * 2 * math.pi
            n = 1 + 0.16 * math.sin(3 * a + ph[0] + k * 0.12) + 0.09 * math.sin(5 * a + ph[1]) + 0.05 * math.sin(7 * a + ph[2] - k * 0.2)
            pts.append((cx + R * n * math.cos(a), cy + R * n * 0.82 * math.sin(a)))
        d = "M" + " L".join(f"{_f(x)} {_f(y)}" for x, y in pts) + " Z"
        fill = t[1] if k % 6 == 0 else ("none")
        out.append(f'<path d="{d}" fill="{fill}" stroke="{t[4] if k % 5 else t[5]}" stroke-width="{2.2 if k % 5 == 0 else 1}" opacity="{.9 if k % 5 == 0 else .55}"/>')
    return "".join(out)

def _arcs(r, w, h, t, uid):
    corner = r.choice([(0, h), (w, h), (0, 0), (w, 0)])
    out = [f'<rect width="{w}" height="{h}" fill="{t[1]}"/>']
    R = math.hypot(w, h) * 1.05
    step = R / r.randint(9, 13)
    k = 0
    while R > step * 0.5:
        out.append(f'<circle cx="{corner[0]}" cy="{corner[1]}" r="{_f(R)}" fill="{[t[5],t[3],t[0],t[4],t[2]][k % 5]}"/>')
        R -= step * r.uniform(0.6, 1.25)
        k += 1
    # thin rhythm lines
    for i in range(1, 7):
        out.append(f'<circle cx="{corner[0]}" cy="{corner[1]}" r="{_f(i * step * 1.9)}" fill="none" stroke="{t[0]}" stroke-width="1" opacity=".35"/>')
    return "".join(out)

def _columns(r, w, h, t, uid):
    # A colonnade in raking light: cylinders shaded dark-light-dark, larger toward one side.
    out = [f"<defs>{_grad(uid,'bg',t[1],t[3])}"
           f'<linearGradient id="{uid}c" x1="0" y1="0" x2="1" y2="0">'
           f'<stop offset="0" stop-color="{t[4]}"/><stop offset=".22" stop-color="{t[2]}"/>'
           f'<stop offset=".42" stop-color="{t[1]}"/><stop offset=".78" stop-color="{t[3]}"/><stop offset="1" stop-color="{t[4]}"/></linearGradient>'
           f'{_grad(uid,"sh",t[0],t[5])}</defs>',
           f'<rect width="{w}" height="{h}" fill="url(#{uid}bg)"/>']
    x = -r.uniform(0, 40)
    k = 0
    grow = r.choice([True, False])
    while x < w:
        cw = (90 + k * 26) if grow else max(70, 260 - k * 26)
        gap = cw * 0.42
        out.append(f'<rect x="{_f(x)}" y="0" width="{_f(cw)}" height="{h}" fill="url(#{uid}c)"/>')
        out.append(f'<rect x="{_f(x + cw)}" y="0" width="{_f(gap * 0.6)}" height="{h}" fill="{t[5]}" opacity=".55"/>')
        x += cw + gap
        k += 1
    out.append(f'<rect width="{w}" height="{h}" fill="url(#{uid}sh)" opacity=".25"/>')
    return "".join(out)

def _dots(r, w, h, t, uid):
    gap = r.choice([22, 26, 30])
    fx, fy = w * r.uniform(0.2, 0.8), h * r.uniform(0.2, 0.8)
    maxd = math.hypot(w, h) * 0.8
    out = [f'<rect width="{w}" height="{h}" fill="{t[0]}"/>']
    for gy in range(0, h + gap, gap):
        off = (gap / 2) if (gy // gap) % 2 else 0
        for gx in range(0, w + gap, gap):
            x = gx + off
            d = math.hypot(x - fx, gy - fy) / maxd
            rad = (gap * 0.48) * max(0.06, 1 - d) ** 1.3
            out.append(f'<circle cx="{_f(x)}" cy="{gy}" r="{_f(rad)}" fill="{t[5]}"/>')
    return "".join(out)

# ---------------------------------------------------------------- icons
# 24×24 line icons, stroke=currentColor. Original simple geometry.
ICONS = {
    "calendar": '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>',
    "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    "shield": '<path d="M12 3 4 6v6c0 5 3.5 8 8 9 4.5-1 8-4 8-9V6z"/>',
    "scale": '<path d="M12 3v18M7 21h10M5 7h14M5 7l-3 7a3 3 0 0 0 6 0zM19 7l-3 7a3 3 0 0 0 6 0z"/>',
    "alert": '<path d="M12 3 2 20h20z"/><path d="M12 10v4M12 17v.5"/>',
    "check": '<circle cx="12" cy="12" r="9"/><path d="m8 12 3 3 5-6"/>',
    "chart": '<path d="M4 20V4M4 20h16"/><path d="M8 16v-4M12 16V8M16 16v-6"/>',
    "users": '<circle cx="9" cy="8" r="3.5"/><path d="M2 20c.5-4 3.5-6 7-6s6.5 2 7 6"/><path d="M16 4.5a3.5 3.5 0 0 1 0 7M18 14c2 .8 3.5 2.8 4 6"/>',
    "user": '<circle cx="12" cy="8" r="4"/><path d="M4 21c.7-4.5 4-7 8-7s7.3 2.5 8 7"/>',
    "document": '<path d="M14 3H6v18h12V7z"/><path d="M14 3v4h4M9 12h6M9 16h6"/>',
    "building": '<path d="M4 21V5l8-2v18M12 8h8v13M2 21h20"/><path d="M7 8h2M7 12h2M7 16h2M15 12h2M15 16h2"/>',
    "bank": '<path d="M3 9 12 4l9 5M4 9h16M6 9v8M10 9v8M14 9v8M18 9v8M3 20h18"/>',
    "globe": '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3 3 15 0 18M12 3c-3 3-3 15 0 18"/>',
    "target": '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1"/>',
    "flag": '<path d="M5 21V4M5 4h11l-2 4 2 4H5"/>',
    "bulb": '<path d="M9 18h6M10 21h4M12 3a6 6 0 0 0-3.5 10.9c.6.5 1 1.2 1 2V16h5v-.1c0-.8.4-1.5 1-2A6 6 0 0 0 12 3z"/>',
    "gear": '<circle cx="12" cy="12" r="3"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3M4.9 4.9 7 7M17 17l2.1 2.1M4.9 19.1 7 17M17 7l2.1-2.1"/>',
    "lock": '<rect x="5" y="10" width="14" height="11" rx="2"/><path d="M8 10V7a4 4 0 0 1 8 0v3"/>',
    "eye": '<path d="M2 12s3.6-7 10-7 10 7 10 7-3.6 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/>',
    "chat": '<path d="M4 5h16v11H9l-5 4z"/>',
    "money": '<rect x="2" y="6" width="20" height="12" rx="2"/><circle cx="12" cy="12" r="3"/><path d="M6 9v.5M18 14.5v.5"/>',
    "arrow": '<path d="M4 12h15M14 6l6 6-6 6"/>',
    "layers": '<path d="m12 3 9 5-9 5-9-5z"/><path d="m3 13 9 5 9-5"/>',
    "search": '<circle cx="11" cy="11" r="7"/><path d="m16 16 5 5"/>',
    "leaf": '<path d="M5 19c0-9 6-14 15-14 0 9-5 15-14 15"/><path d="M5 19 14 10"/>',
    "heart": '<path d="M12 20s-8-5-8-11a4.5 4.5 0 0 1 8-2.8A4.5 4.5 0 0 1 20 9c0 6-8 11-8 11z"/>',
    "book": '<path d="M4 4h6a3 3 0 0 1 2 1 3 3 0 0 1 2-1h6v15h-6a2 2 0 0 0-2 2 2 2 0 0 0-2-2H4z"/><path d="M12 5v16"/>',
    "ban": '<circle cx="12" cy="12" r="9"/><path d="m5.6 5.6 12.8 12.8"/>',
    "spark": '<path d="M12 3v5M12 16v5M3 12h5M16 12h5M6 6l3 3M15 15l3 3M6 18l3-3M15 9l3-3"/>',
    "cpu": '<rect x="6" y="6" width="12" height="12" rx="1"/><rect x="9.5" y="9.5" width="5" height="5"/><path d="M9 2v4M15 2v4M9 18v4M15 18v4M2 9h4M2 15h4M18 9h4M18 15h4"/>',
    "map": '<path d="m3 6 6-2 6 2 6-2v14l-6 2-6-2-6 2z"/><path d="M9 4v14M15 6v14"/>',
    "health": '<path d="M9 3h6v6h6v6h-6v6H9v-6H3V9h6z"/>',
    "education": '<path d="m2 9 10-5 10 5-10 5z"/><path d="M6 11v5c0 1.5 3 3 6 3s6-1.5 6-3v-5M22 9v6"/>',
}

def icon(name):
    p = ICONS.get(name) or ICONS["spark"]
    return (f'<svg class="ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{p}</svg>')
