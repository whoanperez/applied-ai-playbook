---
name: html-deck
description: Turns the current conversation or project into a designed presentation delivered as one interactive HTML file in the user's brand, with bold color blocks, art panels, charts, speaker notes and a timer. It can also make a LinkedIn carousel PDF. Use it when the user says "html-deck", asks to turn this conversation, project, document or notes into a presentation, slides or deck, or wants a presentation without PowerPoint. Do not use it when the user explicitly asks for a .pptx file.
---

# html-deck

You write **one short file, `deck.json`**: the story, plus a list of slides, each with a layout name and a few text fields. `scripts/build.py` draws everything else: layout, color blocks, art panels, charts, icons, navigation, speaker notes, a palette with checked contrast, and content checks. Never write HTML or CSS for the deck.

Read `references/layouts.md` once before writing `deck.json`. Write `deck.json` in your working or output folder (never inside the skill), and run the scripts from there with their full path: `python <skill-folder>/scripts/build.py deck.json --out deck.html`. `logo` and `image` paths are relative to `deck.json`.

## 1. Read the context first
Look through the conversation and the project files and pull out the purpose, audience, duration, the key facts with their sources, and the brand. A brand can be an `html-deck brand` block, colors, fonts or a logo file.

## 2. Ask only what is missing, in one short message
- **No brand:** ask for the brand colors, or the colors they would like. Fonts and logo are optional. If they have none, propose a primary + accent pair that fits the topic and go ahead.
- **No audience or duration**, and you can't infer them: ask.
- **Too little content** for the duration: ask at most 3 specific questions.
If the user says "you decide", decide, and say what you chose in one line when you deliver.

## 3. Write the story before the slides
1. **Thesis:** one sentence the audience must remember, including the "so what". It goes in `story.thesis`.
2. **Spine:** choose one.
   - Situation → complication → resolution: briefings and decisions.
   - Answer first → three reasons → the ask: executives.
   - Problem → method → result: reports and cases.
   - Concept → example → practice: training.
3. **Titles are conclusions.** Every content title is a full sentence that states the takeaway ("Two dates moved; the rest still stands"), not a topic label ("Timeline"). Keep it within the layout's word limit (usually 16 words). Read in order, the titles alone should tell the whole story.
4. **Length:** about one slide per 1.5–2 minutes. Group the slides into 3–6 `parts`, which become the agenda and the progress bar.

## 4. Show, don't list
Pick the layout that *shows* each idea:

| Idea | Layout |
|---|---|
| One decisive figure | `number` |
| Comparison, ranking, trend, schedule | `chart` (bars, columns, timeline, gantt, items) |
| Before vs after, option A vs B | `compare` (interactive switch) |
| Steps or a method | `process` |
| 2–4 parallel points | `columns` |
| Several facts at a glance | `mosaic` |
| An argument with a strong visual | `split`, `frame` or `dark` |
| One claim to land (at most 1 in 4 slides) | `statement` |
| Involve the room | `quiz`, `checklist` |
| Structure | `cover`, `agenda`, `section`, `sources`, `closing` |

Rules:
- Alternate light slides, color-block slides (`split`, `number`) and dark slides (`dark`). Never put three text-only slides in a row.
- Stay inside the word limits in `layouts.md`. Put detail in `notes`; that is what speaker notes are for.
- Every slide gets `notes`: what to say and what to click.
- **Facts:** use only what is in the context or what you verified. Never invent numbers, quotes, logos or testimonials.
  - Any slide with figures or dates gets a `source`. If the figure came from the user without a source, cite it the way they gave it (for example "Source: internal inventory, Planning Office"). If you can't tell where it came from, write "Source: to be confirmed" and mention it when you deliver.
  - Label an organization as fictional (one line on the closing slide) only when you invented it, or when the user asks you to.
- Put `sources` just before `closing`.

## 5. Build and check
```bash
python <skill-folder>/scripts/build.py deck.json --out <short-name>.html
```
The build prints the **headline read-through** (the thesis and every title in order) and any warnings.
1. Read the headlines. If the story doesn't follow from them alone, rewrite titles, not decoration.
2. Fix every `ERROR` and any `WARN` about word limits, missing sources or text-only runs, then rebuild. One rebuild is usually enough.
3. If Playwright is available, also run `python <skill-folder>/scripts/render_check.py <short-name>.html --states`. It is cheap: no images. It reports text that had to shrink or still overflows. Shorten what it flags. Take screenshots (`--shots shots/`) and look at them only for slides it flags, or when the user asks for a visual check.

For a carousel, set `"format": "carousel"` and add `--pdf <name>.pdf`. If the PDF can't be made here, the user opens the HTML in Chrome and presses **P**.

## 6. Deliver
- Give the user the `.html` file (in Claude.ai, save it to the outputs folder). Keep `deck.json` next to it.
- Reply briefly:
  - what the deck argues (the thesis) and its length;
  - how to present it: ← → to move, **N** for notes and timer, **F** for full screen, **P** for PDF;
  - any choices you made for the user, and any "to be confirmed" sources.
- The deck loads its fonts from Google Fonts. Offline, it falls back to system fonts. If it will be shown without internet, say so, or use `"fonts": {"display": "Arial"}`.
- The first time a brand is set up, end with this block and suggest pasting it into the project instructions, so the next deck needs no questions:
```
html-deck brand
- Name: …
- Primary: #……  · Accent: #……  · Background: light|dark
- Fonts: display …, text …
- Logo: file name in the project | none
- Art: lines, waves  · Footer: …
```

## Changes later
The user asks for changes in plain words. Edit `deck.json` and rebuild; never patch the HTML by hand. Keep a previous version (`deck-v1.json`) only if the user asks for it. To keep a slide's art exactly as it was after you rename it, give the slide an `id`. If only the built HTML is available (for example, in a new conversation), recover the source first:
`python <skill-folder>/scripts/build.py --extract old-deck.html > deck.json`.
