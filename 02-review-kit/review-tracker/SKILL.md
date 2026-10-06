---
name: review-tracker
description: Keeps a review standard for a piece of work across versions. The first time, it reviews the work and saves a review ledger (rubric, findings with IDs and what "fixed" looks like). On each new version it verifies every open finding, catches regressions (things that were right and broke) and new problems, and scores with the same rubric so versions can be compared. Use it when the user says "review-tracker", shares a new version or draft of something already reviewed, or asks what changed, what is still open, or whether the new version is better.
---

# review-tracker

Your job: make the review of a work **cumulative**. Each chat normally starts from zero: the criteria change, the score moves for no reason, and nobody checks whether a fix broke something else. You keep one ledger and judge every version against it.

## Find the ledger
Look in the conversation and the project files for `review-ledger.md`.
- **No ledger:** this is the first review. Go to A.
- **Ledger found:** go to B. If the user attached the previous version too, use it to see exactly what changed.

## A. First review: create the ledger
1. Work out what the work is, who will judge it and what they must decide. If you can't tell, ask once.
2. Review the whole work: consistency (totals, counts, dates, cross-references), evidence for claims, obligations of the field, people affected, feasibility and full cost, measures vs objective, failure modes.
3. Write the ledger with this structure:

```
# Review ledger — [work]
Judged by: [audience] · Standard: [what a demanding reviewer for that audience expects]

## Rubric (fixed — do not change between versions)
| Criterion | 1 = | 3 = | 5 = |
(5–6 criteria with concrete anchors)

## Findings
| ID | Severity | Where | Finding | Fixed when… | Could also | Status (v1) |
| F-01 | Critical | §5 | … | [the one core condition that resolves it] | [optional improvements] | Open |

## Versions
| Version | Date | Score | Open: C / I / M | Note |
```

**How to write "Fixed when…":** the *minimum* change that removes the core problem, as one testable condition (e.g., "the summary and the budget table give the same total"). Don't bundle extras into it. Put good-practice additions (extra detail, further evidence, nicer wording…) in **Could also**: they are suggestions, never conditions for Fixed. Split a finding in two if it really has two independent problems.

4. Deliver in the chat: a short verdict, the findings by severity with a proposed fix for each, and the score. Save the ledger as `review-ledger.md` (create the file if you can) and tell the user to keep it in the project, or paste it next time with the new version.

## B. New version: verify against the ledger
Work in this order. Don't trust the author's change log or summary: verify everything in the text itself.

1. **Each open finding:** check its "Fixed when…" criterion in the new version. Status: **Fixed** · **Partly fixed** (say exactly which part of the core condition remains) · **Not fixed** · **Can't tell**. A reworded passage with the same substance is Not fixed. Judge only the core condition: if it is met, the status is Fixed, even if the "Could also" items are missing (list those as optional). If an older ledger bundled extras into "Fixed when…", judge the core problem described in the Finding column.
2. **Regression sweep:** list every passage that changed (compare with the previous version if you have it; otherwise use the ledger's "Where" column and the change log). For each change, check everything that depends on it elsewhere in the work: totals, dates and timelines, scope and lists, cross-references, statements in other sections, the summary. A **regression** is something that was correct or consistent before and is now wrong or inconsistent because of an edit.
3. **New content:** review any new section or idea as fresh work and add new findings.
4. **Score** with the same rubric and anchors. Explain every change in score by naming the finding that moved it.
5. **Update the ledger:** new statuses, new IDs for regressions (R-01…) and new findings (continue the F numbers), and a new row in Versions.

Deliver in the chat, in the user's language (translate the headings and labels too):

```
**[work] · v[n] vs v[n-1]** · Score [x.x] → [y.y] / 5
**Verdict:** one sentence: better, ready or not, and the main reason.

### Status of the open findings
| ID | Finding | v[n-1] | v[n] | Evidence |
### Regressions (broke in this version)
1. **R-0x · [title]** · §… — what changed, what it broke, proposed fix.
### New findings
### Still to do before [audience]
The open items, most serious first, each with a proposed fix.
```

Then give the updated ledger (file or block to paste).

## Rules
- Same rubric, same anchors, every version. Never rescore old versions.
- A finding is Fixed when its core condition is met in the text, and only then. If the author says it is fixed and it isn't, say so. Don't hold a real fix hostage to optional improvements.
- Evidence for every status: section and a short quote.
- No invented sources. Name a law or standard only if you are sure it exists and applies.
