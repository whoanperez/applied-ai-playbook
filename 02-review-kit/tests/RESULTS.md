# How the review kit was tested

**[English](#english) · [Español](#español)**

## English

All tests ran on 6 October 2026 with **Claude Sonnet** answering as it would in a chat, with the same files and the same message, with and without the skill. Every answer was graded **blind** by two independent graders (Claude Opus), who saw anonymous, shuffled answers and an answer key, not which tool wrote them. The test documents and answer keys were written by separate agents that never saw the skills.

### rulebook-check
**Material:** a fictional call for proposals with **42 requirements**, and a fictional proposal that fails **8** of them on purpose: numbers just over a limit, a missing annex, a date outside the window, rules buried in footnotes. Files: [`examples/lcsa/`](../examples/lcsa/) and [`materials/rulebook-answer-key.md`](materials/rulebook-answer-key.md).

**Message:** "Review this proposal against the attached call…" (Claude alone) vs. "rulebook-check: review this proposal against the attached call…". 5 runs each in English, plus 1 control run each in Spanish.

| | Claude alone | rulebook-check |
|---|---|---|
| Failures found (of 8) | 8 in 5 of 5 runs | 8 in 5 of 5 runs |
| Requirements checked (of 42) | 32 to 40 (average 34–35) | **42 in 5 of 5 runs** |
| Requirements wrongly flagged as failing, per run | 0 to 2 | 0 to 2 |
| Answer length | about 1,600 words | about 3,600 words |
| Spanish control run | 8 of 8 · 34–35 of 42 | 8 of 8 · 42 of 42 |

The graders agreed on 96 of 96 failure scores. **What it means:** with the call attached, Claude alone found every seeded failure. The difference is coverage: it checked most requirements but left 2 to 10 unchecked, without saying which. The skill checked every requirement, every time, and showed the evidence for each one.

### review-tracker
**Material:** a fictional plan, version 1 (12 known flaws) and version 2, where 8 flaws are fixed, 3 are not, 1 is half-fixed, 2 edits broke something that was right before, and 1 new problem was added. Key: [`materials/tracker-answer-key.md`](materials/tracker-answer-key.md).

**Setup:** Claude alone received v1, v2 and its own previous review ("Review v2 against your previous review"). The skill received v1, v2 and the ledger it had written on v1.

| | Claude alone | review-tracker 1.0 | review-tracker 1.1 |
|---|---|---|---|
| Things that broke + new problem (of 3) | 3 in 5 of 5 runs | 3 in 5 of 5 runs | 3 in 5 of 5 runs |
| Correct status of the 12 old flaws | about 10–11 (range 6–12) | about 7 | about 10 (range 9–11) |

Version 1.0 marked real fixes as "partly fixed" because it wrote over-demanding criteria for what "fixed" means. Version 1.1 changed one rule (the criterion is the minimum that solves the problem; extras are suggestions) and was tested again with new runs. **What it means:** the tracker is as accurate as Claude alone with its previous review at hand, not more. Its value is that the ledger travels between chats and keeps the same yardstick; this test doesn't measure that.

### defense-rehearsal
Not measured. [`examples/lcsa/defense-rehearsal-transcript-en.md`](../examples/lcsa/defense-rehearsal-transcript-en.md) is a full rehearsal in which **the presenter is simulated** (an AI agent playing the head of the office).

### Background: why the kit looks like this
The first version was a general "expert reviewer" skill. In a blind test with 12 seeded flaws, Claude alone found 11.5 of 12 and the skill 12 of 12; on a second document written by an independent agent, both found 10 of 10. Finding problems in a document is something Claude already does well when it knows who you are and who will judge the work. So the kit focuses on what a single chat does less well: covering every rule, keeping track across versions, and rehearsing.

### Limits
- Small samples (5 runs per arm) and one model (Sonnet). Graders are AI models, not people.
- The test documents are fictional and written by AI agents. The skill author designed the tests; the documents and keys were written by agents that never saw the skills.
- review-tracker 1.1 was changed after its first test; that change is reported above.
- After testing, all three skills got one wording change: headings are translated into the user's language. The Spanish rulebook-check run in the examples uses that final wording (8 of 8, 42 of 42).

---

## Español

Todas las pruebas se corrieron el 6 de octubre de 2026 con **Claude Sonnet** respondiendo como lo haría en un chat: los mismos archivos y el mismo mensaje, con la skill y sin ella. Dos evaluadores independientes (Claude Opus) calificaron cada respuesta **a ciegas**: veían respuestas anónimas y mezcladas, más una clave de respuestas, sin saber qué herramienta escribió cada una. Los documentos de prueba y las claves los escribieron agentes distintos que nunca vieron las skills.

### rulebook-check
**Material:** una convocatoria ficticia con **42 requisitos** y una propuesta ficticia que incumple **8** a propósito: cifras apenas por encima de un límite, un anexo que falta, una fecha fuera de la ventana, reglas escondidas en notas al pie.

| | Claude solo | rulebook-check |
|---|---|---|
| Incumplimientos encontrados (de 8) | 8 en 5 de 5 corridas | 8 en 5 de 5 corridas |
| Requisitos revisados (de 42) | Entre 32 y 40 (promedio 34–35) | **42 en 5 de 5 corridas** |
| Requisitos marcados como incumplidos sin estarlo, por corrida | 0 a 2 | 0 a 2 |
| Largo de la respuesta | ~1.600 palabras | ~3.600 palabras |
| Corrida de control en español | 8 de 8 · 34–35 de 42 | 8 de 8 · 42 de 42 |

**Qué significa:** con la convocatoria adjunta, Claude solo encontró todos los incumplimientos sembrados. La diferencia está en la cobertura: dejó sin revisar entre 2 y 10 requisitos, sin decir cuáles. La skill revisó todos, todas las veces, y mostró la evidencia de cada uno.

### review-tracker
Plan ficticio en versión 1 (12 fallas conocidas) y versión 2 (8 arregladas, 3 sin arreglar, 1 a medias, 2 cosas que se dañaron con los cambios y 1 problema nuevo). Las dos versiones detectaron las 3 cosas nuevas en todas las corridas. La 1.0 marcaba arreglos reales como "a medias"; la 1.1 cambió una regla y se volvió a probar: queda tan precisa como Claude solo con su revisión anterior a mano, no más. Su valor es que el registro viaja entre conversaciones con la misma vara; esta prueba no mide eso.

### defense-rehearsal
Sin medición. El ejemplo es un ensayo completo con un **presentador simulado**.

### Antecedente y límites
La primera versión era un "revisor experto" general. En prueba a ciegas empató con Claude solo (11,5 frente a 12 de 12; 10 frente a 10 en un documento independiente), por eso el kit se enfoca en lo que un chat suelto no hace bien. Muestras pequeñas (5 corridas por brazo), un solo modelo, evaluadores que son modelos de IA, documentos ficticios. review-tracker 1.1 se ajustó después de su primera prueba. Después de las pruebas, las tres skills tuvieron un cambio de redacción (los títulos se traducen al idioma del usuario).
