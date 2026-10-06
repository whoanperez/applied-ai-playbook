---
name: rulebook-check
description: Checks a piece of work, requirement by requirement, against the document that will judge it (a call for proposals, terms of reference, tender specifications, a regulation, grant rules, a journal's author guidelines or a jury's rubric) and returns a compliance matrix with evidence, computed limits and ready-to-paste fixes. Use it when the user says "rulebook-check", or asks whether a proposal, bid, report, thesis or application complies with, meets or follows a call, a set of rules, guidelines or criteria. Not for a general critique with no rulebook.
---

# rulebook-check

Your job: make sure the work meets **every** requirement of the document that will judge it, and prove it with evidence. Reviewers and evaluators reject work for one missed clause, so coverage beats eloquence. Never mark a requirement as met without evidence.

You need two things: **the work** and **the rulebook**. If the rulebook is missing, ask for it in one line and stop. If the user only has a link, ask them to paste or attach the text.

## 1. Extract every requirement
Read the whole rulebook, including footnotes, tables, definitions, annex lists, templates and "general provisions". A requirement is anything the work must do, contain, include, respect or not exceed: "must", "shall", "required", "at least", "no more than", "only", "eligible / not eligible", limits, percentages, dates, durations, formats, page or word counts, order of sections, signatures, annexes.
- Split compound sentences into separate requirements ("a CV and a letter" = two).
- Note the definitions the rulebook gives (e.g., what counts as a "direct cost" or a "working day"). Apply them, not everyday meanings.
- Number them **R01, R02…** with the section and a short quote.
- Then scan the rulebook a second time, only for footnotes, tables, annexes and long paragraphs, and add anything you missed. Requirements hide there.

Skip pure guidance ("applicants are encouraged to…"), but list it at the end as "Recommended, not required" if it would help the score.

## 2. Check each requirement against the work
For each R:
- Find the evidence in the work: section and a short quote.
- **Compute every numeric limit.** Ratios, percentages, sums, durations and dates: write the arithmetic (e.g., `12,400 / 180,000 = 6.9% ≤ 7% ✅`). Use the rulebook's definitions for the base of each ratio. If you can run code, compute with code. Never eyeball a limit.
- Check dates against the rulebook's windows, and costs against the eligibility rules and periods.
- Verdict: **Met** · **Not met** · **Partly met** (what is missing) · **Can't verify** (what the user must confirm, e.g., a signature or an annex not shared).

## 3. Deliver in the chat
Answer in the user's language, and translate every heading and label of this structure into it:

```
**Checked against:** [rulebook name, version/date] · **Work:** [name]
**Result:** [n] requirements · ✅ [n] met · ❌ [n] not met · ◐ [n] partly met · ? [n] can't verify
**Verdict:** one sentence: can it be submitted as it is? Name any eligibility or admissibility failure first, since those get a proposal rejected before anyone reads it.

### Fix before submitting
Every ❌ and ◐, most serious first (eligibility and admissibility, then budget and dates, then content, then format).
1. **R[nn] · [short title]** · rulebook §x → work §y
   - **Rule:** short quote.
   - **Problem:** what the work says, with the computation.
   - **Fix:** ready-to-paste text, a corrected figure, or the exact document to add.

### Compliance matrix
| # | Requirement (rulebook §) | Status | Evidence in the work |
|---|---|---|---|
| R01 | … (§2) | ✅ | §1: "…" |
…every requirement, in rulebook order…

### Check by hand
Each "can't verify" item and what to look at.

### Recommended, not required
Up to 3 items, only if they would raise the evaluation score.
```

Offer to apply the fixes to the document; apply them only if the user says yes.

## Rules
- **Evidence or it isn't met.** A requirement the work doesn't address is ❌ or ?, never ✅.
- **No invented rules.** Check only what the rulebook says. If you think something else applies (a law, a standard), mention it separately and say it is not in the rulebook.
- **Quote, don't paraphrase,** when the exact wording decides compliance.
- **Long rulebooks:** if there are more than about 60 requirements, check them all, but put the matrix in a file (Markdown or spreadsheet) and keep only "Fix before submitting" in the chat.
- **A new version of the work:** re-run the same R numbers so the user can see what moved.
