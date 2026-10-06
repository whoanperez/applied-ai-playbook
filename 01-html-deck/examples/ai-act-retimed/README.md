# Example · The AI Act, re-timed

A 20-minute briefing on the EU AI Act after the Digital Omnibus on AI (Regulation (EU) 2026/1744), presented by **Halden Observatory, a fictional organization** made to demonstrate html-deck. Dates were checked against EUR-Lex on 5 October 2026. This is general information, not legal advice.

| Brand | Deck | Source |
|---|---|---|
| Harbour (spruce + saffron, Archivo) | [ai-act-retimed-harbour.html](ai-act-retimed-harbour.html) | [deck-harbour.json](deck-harbour.json) |
| Parliament (oxblood + sky, IBM Plex) | [ai-act-retimed-parliament.html](ai-act-retimed-parliament.html) | [deck-parliament.json](deck-parliament.json) |
| Night (dark, indigo + amber, Bricolage) | [ai-act-retimed-night.html](ai-act-retimed-night.html) | [deck-night.json](deck-night.json) |

The three `deck-*.json` files are identical except for the `brand` block. To rebuild one:

```bash
python ../../html-deck/scripts/build.py deck-harbour.json --out ai-act-retimed-harbour.html
```

GitHub shows `.html` files as code: download the file and open it in a browser, or use the live link in the main README.

---

**Ejemplo en español:** una sesión informativa de 20 minutos sobre el EU AI Act tras el Digital Omnibus, presentada por un observatorio **ficticio**. Los tres archivos `deck-*.json` son iguales salvo el bloque `brand`. Para abrir un deck, descarga el `.html` y ábrelo en el navegador.
