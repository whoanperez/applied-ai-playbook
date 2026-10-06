# deck.json reference

## Skeleton
```json
{
  "title": "The AI Act, re-timed",
  "lang": "en",
  "format": "slides",
  "minutes": 20,
  "footer": "Halden Observatory",
  "brand": {
    "name": "Halden Observatory",
    "primary": "#0F4C45",
    "accent": "#F2B134",
    "background": "light",
    "fonts": {"display": "Archivo", "text": "Archivo"},
    "logo": "logo.svg",
    "art": ["lines", "waves"]
  },
  "story": {"thesis": "One sentence the audience must remember.", "audience": "…", "ask": "…"},
  "parts": [
    {"title": "Opening", "minutes": 1, "hide": true},
    {"title": "What happened", "desc": "One regulation, three dates", "minutes": 4}
  ],
  "slides": [ … ]
}
```

- `lang`: `en` or `es` for the interface. For other languages add `"strings": {…}`; the keys are in the template.
- `format`: `slides` (16:9) or `carousel` (1080×1350; works best with cover, statement, number, chart, split and closing).
- **brand**
  - `primary` is required. It is used for dark panels, charts and art.
  - `accent` fills the big color blocks.
  - Add `"block": "primary"` to use the primary color for the blocks instead.
  - `background` is `light` (default), `dark` or a hex value.
  - `fonts` are Google Fonts names; the default is Archivo. Optional `display_weight` (400–800; serif display faces look best at 500–600) and `display_tracking` (e.g. `"-0.02em"`).
  - `logo` is a file path; it shows on the cover.
  - `art` is 1–2 art styles used across the deck (see the end of this page).
- **parts:** set `"part"` on the first slide of each part; the following slides inherit it. `minutes` per part drive the agenda and the timer, and should add up to the deck's `minutes`. If they're missing, `minutes` is split by slide count. The first part (cover and agenda) is hidden from the agenda list unless you set `"hide": false`.

**Fields every slide accepts:** `layout` (required), `part`, `kicker` (2–6 words above the title), `title`, `notes` (what to say and click), `source` (a short citation line), `id`.
**Visual slot:** layouts with a picture take `"art": {"style": "waves", "seed": 3}` or `"image": "photo.jpg"` (a user's file; shown in black and white unless `"mono": false`). With neither, an art panel is generated.
Text fields accept `**bold**`. Word limits are warnings, not errors, but keep to them.

---

## Layouts

**cover** — title ≤12 words, subtitle ≤25, meta list.
```json
{"layout":"cover","part":"Opening","kicker":"Briefing for the board","title":"The AI Act, re-timed","subtitle":"What changed, what didn't, and what to do this quarter.","meta":[{"label":"Date","value":"October 2026"},{"label":"Length","value":"20 minutes"}],"notes":"…"}
```

**agenda** — built automatically from `parts`.
```json
{"layout":"agenda","notes":"Click any line to jump to it."}
```

**section** — a part divider with a big number.
```json
{"layout":"section","part":"The new calendar","number":"02","label":"Part","title":"What moved, and by how much","text":"Optional, ≤25 words.","notes":"…"}
```

**statement** — one claim, very large. Title ≤18 words, text ≤40.
```json
{"layout":"statement","kicker":"What happened","title":"Nothing was repealed. The clock moved.","text":"One or two supporting sentences.","source":"Source: …","notes":"…"}
```

**split** — half color block with the argument; art on the other half; vertical label. Title ≤14, text ≤45, bullets ≤5 × 16 words. `"tone":"dark"` uses the dark panel instead of the color block.
```json
{"layout":"split","label":"WORK PLAN","kicker":"Proposal","title":"A small team can cover the whole inventory","text":"…","bullets":["Weeks 1–2: inventory","Weeks 3–4: classification"],"notes":"…"}
```

**frame** — text column with a picture in an offset color frame. Same limits as split. Bullets can be `{"title":"Method:","text":"primary sources"}`.

**dark** — dark panel over a large art panel. Same limits as split.

**number** — one huge figure on a color block, argument on the right. `value` ≤6 characters ("+16", "2.4M", "73%"), `unit`, `caption` ≤22 words, title ≤14, text ≤40 or bullets. `"tone":"dark"` is available.
```json
{"layout":"number","value":"+16","unit":"months","caption":"Extra time for Annex III systems.","kicker":"The new calendar","title":"High-risk systems gained more than a year","bullets":[{"title":"Annex III","text":"2 Aug 2026 → 2 Dec 2027"}],"source":"Source: …","notes":"…"}
```

**columns** — 2–4 parallel items, each with a big number or an `icon` (the icon replaces the number), a short title, text ≤30 words and an art thumbnail. Use `"numbered": false` when the items aren't a sequence, and `"thumbs": false` to drop the pictures.
```json
{"layout":"columns","title":"Four smaller changes reach beyond the deadlines","items":[{"icon":"eye","title":"Marking","text":"…"},{"icon":"ban","title":"New prohibitions","text":"…"}],"source":"…","notes":"…"}
```

**process** — 3–5 steps in a zigzag, each with an icon, a title of 1–3 words and text ≤18 words.
```json
{"layout":"process","title":"Four steps take a rule from text to action","steps":[{"icon":"search","title":"Read","text":"Primary sources first."},{"icon":"layers","title":"Classify","text":"Each system by risk."}],"notes":"…"}
```

**chart** — a chart plus an optional dark note box (`note.value` big figure, `note.text` ≤30 words). Use `"wide": true` or omit `note` to use the full width.
```json
{"layout":"chart","title":"Most of the work falls on Annex III systems","chart":{…},"note":{"value":"14","text":"systems need a high-risk plan before Dec 2027."},"source":"…","notes":"…"}
```

**compare** — an interactive switch between 2–3 states: before/after, option A/B, risks/controls, any pair worth toggling. Each state has a `label` and a `chart`. `default` is the index shown first (default: the last state).
```json
{"layout":"compare","title":"Two dates moved; the rest still stands","default":1,"states":[{"label":"Before (2024)","chart":{"type":"timeline","points":[…]}},{"label":"After (2026)","chart":{"type":"timeline","points":[…]}}],"source":"…","notes":"…"}
```

**mosaic** — up to 6 tiles in a 3×2 grid. A tile is a fact (`value` + `label`), a picture (`art` or `image`), or both. Use `"wide": true` to span two columns, and `"tone": "block"` or `"tone": "dark"` to color a tile. Give exactly one tile `"tone": "block"`.
```json
{"layout":"mosaic","title":"One regulation, adopted and in force within three weeks","tiles":[{"value":"8 Jul","label":"Adopted"},{"value":"27 Jul","label":"In force","tone":"block"},{"art":{"style":"waves"},"wide":true},{"value":"2026/1744","label":"Regulation number","tone":"dark"}],"source":"…","notes":"…"}
```

**quote** — a real quote only, ≤40 words, with `who` and `role`.

**quiz** — a question (title ≤22 words), 3–4 options with one `"correct": true`. Each option's `why` explains the answer without starting with "Correct" (the engine adds that).
```json
{"layout":"quiz","title":"A bank builds a new credit-scoring model. From when do the high-risk rules apply?","options":[{"text":"2 August 2026","why":"That was the original date."},{"text":"2 December 2027","correct":true,"why":"Credit scoring is an Annex III use."}],"notes":"Ask for a show of hands first."}
```

**checklist** — up to 7 actions (≤18 words each) to tick live, with a counter on a color panel and a `note` ≤30 words.

**sources** — `rows` of `{"source","use","url"}`. Optional `headers`.

**closing** — the one line to remember (≤8 words), text ≤25, meta (contact). `"tone":"dark"` is available.

---

## Charts (`chart` and `compare` states)
- **bars** (horizontal) and **columns** (vertical): up to 8 values. Mark the one that matters with `"hl": true`.
  `{"type":"bars","suffix":" months","max":18,"data":[{"label":"Annex III","value":16,"hl":true},{"label":"Annex I","value":12}]}`
  Optional `prefix` and `max`. Include the space in `suffix` (`" days"`); `"%"` needs none.
- **timeline:** 3–5 points (6 at most, with short texts). `state` is `done` (already happened) or `hl` (the key change). Optional `was` (the old date) and `tag`.
  `{"type":"timeline","points":[{"date":"2 Feb 2025","text":"Prohibitions apply","state":"done"},{"date":"2 Dec 2027","was":"was Aug 2026","text":"Annex III","state":"hl","tag":"+16 months"}]}`
- **gantt:** time ranges on a year scale. A bar without `end` runs to the end of the scale. `kind` is `hl` (key) or `was` (dashed, a former range). `marks` draws event lines.
  `{"type":"gantt","from":"2025","to":"2029","rows":[{"label":"High-risk, Annex III","sub":"Stand-alone uses","bars":[{"start":"2026-08","end":"2027-12","text":"was Aug 2026","kind":"was"},{"start":"2027-12","text":"From Dec 2027","kind":"hl"}]}],"marks":[{"at":"2026-07","text":"In force"}]}`
- **items:** 2–4 option cards: `{"type":"items","items":[{"title":"Mixed team","text":"…","hl":true}]}`

## Art styles
- `lines`: architecture seen from below
- `waves`: op-art ribbons
- `contour`: topographic lines
- `arcs`: concentric curves
- `columns`: a colonnade in raking light
- `dots`: halftone

Pick 1–2 per deck in `brand.art` so the deck looks like one series. The `seed` (any number) gives a different composition in the same style.

## Icons
calendar clock shield scale alert check chart users user document building bank globe target flag bulb gear lock eye chat money arrow layers search leaf heart book ban spark cpu map health education
