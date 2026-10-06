#!/usr/bin/env python3
"""
html-deck 2 · render_check.py (MIT) — optional; needs playwright + Chromium.
Opens the deck, visits every slide (and every compare state), reports text that
still overflows after auto-fit and JavaScript errors, and can save screenshots.

  python render_check.py deck.html [--shots DIR] [--states]
"""
import argparse, os, sys

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("deck", help="built .html deck")
    ap.add_argument("--shots", help="folder for one PNG per slide")
    ap.add_argument("--states", action="store_true", help="also screenshot every compare state")
    ap.add_argument("--scale", type=float, default=1.0, help="screenshot scale (default 1 = full 1600×900)")
    a = ap.parse_args()
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("playwright not installed: skip this check"); return 0
    errs, probs = [], []
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 1700, "height": 1050})
        pg.on("pageerror", lambda e: errs.append(str(e)))
        pg.on("console", lambda m: m.type == "error" and errs.append(m.text))
        pg.goto("file://" + os.path.abspath(a.deck)); pg.wait_for_timeout(1800)
        n = pg.evaluate("window.htmlDeck ? htmlDeck.count : 0")
        if not n:
            print("ERROR deck engine did not start"); return 1
        if a.shots: os.makedirs(a.shots, exist_ok=True)
        car = pg.evaluate("document.body.classList.contains('fmt-carousel')")
        W, H = (1080, 1350) if car else (1600, 900)
        pg.set_viewport_size({"width": W + 24 + 340, "height": H + 140})
        pg.wait_for_timeout(400)
        def shot(name):
            el = pg.query_selector("#hdFit")
            el.screenshot(path=os.path.join(a.shots, name), scale="css")
        for i in range(n):
            pg.evaluate(f"htmlDeck.go({i})"); pg.wait_for_timeout(900)
            info = pg.evaluate("""() => { const s=[...document.querySelectorAll('.slide')].find(x=>!x.hidden);
              const bad=[...s.querySelectorAll('.tx')].filter(e=>e.scrollHeight>e.clientHeight+10||e.scrollWidth>e.clientWidth+2).map(e=>e.className);
              const small=[...s.querySelectorAll('.tx')].filter(e=>parseFloat(getComputedStyle(e).getPropertyValue('--s'))<0.8).map(e=>e.className);
              return {id:s.id, bad, small} }""")
            for c in info["bad"]: probs.append(f"slide {i+1} ({info['id']}): text overflows its area ({c}) — shorten it")
            for c in info["small"]: probs.append(f"slide {i+1} ({info['id']}): text shrunk below 80% to fit ({c}) — consider shortening")
            if a.shots: shot(f"{i+1:02d}-{info['id']}.png")
            if a.states:
                keys = pg.evaluate("() => [...[...document.querySelectorAll('.slide')].find(x=>!x.hidden).querySelectorAll('[data-key]')].map(b=>b.getAttribute('data-key'))")
                for k in keys:
                    pg.evaluate(f"() => [...document.querySelectorAll('.slide')].find(x=>!x.hidden).querySelector('[data-key=\"{k}\"]').click()")
                    pg.wait_for_timeout(400)
                    if a.shots: shot(f"{i+1:02d}-{info['id']}--{k}.png")
        b.close()
    print(f"Checked {n} slides")
    for x in probs: print("WARN ", x)
    for e in errs: print("ERROR js:", e)
    if not probs and not errs: print("All text fits. No JavaScript errors.")
    return 1 if errs else 0

if __name__ == "__main__":
    sys.exit(main())
