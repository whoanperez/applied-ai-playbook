# Answer key — Project ATLAS v1.0 → v2.0 (progress tracking)

Files: `atlas-v1.md` (12 seeded flaws, see `atlas-v1-key.md`) and `atlas-v2.md`.

**Summary of v2 state**

| Flaw | Status in v2 |
|---|---|
| C1 Sensitive data for fine-tuning | FIXED |
| C2 Automated eligibility decisions | **PARTIAL** |
| C3 Big-bang launch / channel removal | FIXED |
| C4 Vendor data-use contract | FIXED |
| I1 KPIs don't measure objective | FIXED |
| I2 Recurring costs / cost-neutral years 2–3 | **NOT FIXED** |
| I3 No accessibility / inclusion testing | **NOT FIXED** |
| I4 Timeline vs procurement | FIXED |
| M1 Budget total doesn't add up | FIXED |
| M2 Undefined acronyms | FIXED |
| M3 Unsourced 70% figure | **NOT FIXED** |
| M4 12 procedures vs 9 listed | FIXED |

Counts: 8 FIXED, 3 NOT FIXED, 1 PARTIAL. Plus 2 regressions (R1, R2) and 1 new flaw (N1).

**Note on the change log.** v2 has a "Changes since v1.0" box. It is deliberately imperfect: it **overstates C2** ("Eligibility decisions are now reviewed by a caseworker" — the body only reviews denials), and it **omits** the acronym fix (M2), the scope-list change (M4, which causes R2), the objective's move from "end of year 1" to "end of year 2", and the new steering committee (N1). A review that takes the change log at face value will tend to mark C2 as fixed and miss R2/N1.

**Grading of status.** For each C/I/M item, a review "gets it right" (1) if it states the status below or clearly equivalent wording. It gets 0 if it states a different status, or says nothing about that flaw. No half credit on status unless stated in the item.

---

## Status of the 12 v1 flaws

### C1 — Sensitive personal data used for fine-tuning — **FIXED**
Evidence (section 6): "ATLAS will **not** be fine-tuned on case files; RAG over the manuals and FAQ is enough." / "No case data is exported to the vendor." / "Uploaded documents, including medical certificates, go straight into the case management system, and conversation logs are pseudonymized. Before the pilot, the Data Protection Officer will complete a data protection impact assessment and confirm the legal basis for the processing." The 95,000 fine-tuning line is gone from the budget (section 10).
Counts as correct: "fixed", "resolved", "addressed" — the export and fine-tuning on 2.3M case files with IDs and medical data are removed, with minimization, DPIA and legal basis. A note that the DPIA is still to be done (future) is fine as long as the status is fixed.
Counts as wrong: "not fixed" or "partial" on the grounds that ATLAS still processes medical certificates for the fee waiver (that is the procedure itself, now under DPIA, in-country hosting and no-training clauses), or confusing this with C2.

### C2 — Fully automated eligibility decisions — **PARTIAL**
Evidence (section 5): "Approvals are issued automatically and reach the citizen by WhatsApp or email within minutes. When the rules point to a denial, a caseworker reviews the case and issues the decision within five working days."
What was fixed: denials now get human review before they are issued.
What remains: (a) approvals of the housing subsidy and the disability fee waiver are still fully automated, with no human check (a wrong automatic approval commits public funds); (b) there is still no explanation of reasons and no way for a citizen to contest or appeal a decision. The change log claims "Eligibility decisions are now reviewed by a caseworker", which overstates the fix.
Counts as correct: "partial", "partly fixed", "improved but incomplete" — or "fixed for denials only / approvals still automatic", or "human review added but no appeal/explanation". Naming at least one of (a) or (b) as what remains is required.
Counts as wrong: "fixed" / "resolved" (including echoing the change log); "not fixed" with no acknowledgment that denials are now reviewed.

### C3 — Big-bang launch, no pilot, removal of human channels — **FIXED**
Evidence (section 9): "| 8–10 | **Pilot in two districts**, web portal and WhatsApp |", "| 11 | Pilot evaluation and go/no-go (section 7) |", "| 12 onward | Phased rollout, region by region |" and "The call center and the 14 offices keep their current hours throughout." The v1 milestone "Close 40% of call-center positions and reduce office opening hours to three days a week" is deleted.
Counts as correct: "fixed" — pilot + phased rollout and the human channels are kept. A reviewer may add a caveat about the pilot's go/no-go governance (that is N1) without changing this status.
Counts as wrong: "not fixed" or "partial". Note: if the review says "partial" only because the go/no-go decision is made by a conflicted committee, give 0 for C3 status but credit N1 if the conflict is correctly described.

### C4 — Vendor may use citizen data; no data control — **FIXED**
Evidence (section 8): "Instead of the vendor's standard terms, the contract must provide for: hosting in data centers in the country; agency ownership of all data; no use of agency data or interactions to train or improve the vendor's products or models; and, at exit, return of all data and certified deletion within 30 days."
Counts as correct: "fixed" — data-use clause removed and residency, ownership and exit terms added.
Counts as wrong: "not fixed" / "partial". (Observing that these are requirements still to be negotiated is fine as a caveat; it does not change the status.)

### I1 — Success measures don't measure the objective — **FIXED**
Evidence (section 3): "- Average resolution time for in-scope procedures, from the case management system." and "- Accuracy: share of answers judged correct in a monthly staff review of sampled conversations (target: 95%)." The conversation-volume KPI (600,000) is removed.
Counts as correct: "fixed" — a resolution-time KPI (and an accuracy KPI) now track the objective.
Counts as wrong: "not fixed" / "partial". (Noting that the resolution-time KPI has no separate numeric target is acceptable as a minor remark — the target is in the objective line — but not as a "partial" status.)

### I2 — Recurring costs missing; years 2–3 assumed cost-neutral — **NOT FIXED**
Evidence (section 10): "The program runs for three years. From year 2, ATLAS is expected to pay for itself, as efficiency gains in the call center and the offices cover the platform." Reworded from v1 ("expected to be cost-neutral, because savings…"), same substance. The budget is still year 1 only; no license renewal, usage/inference, maintenance or monitoring costs for years 2–3.
Extra (still part of I2, not a separate item): v2 removed the 40% call-center cut (C3 fix), so the "efficiency gains" claim now has even less basis than in v1. A review that points this out is right about I2.
Counts as correct: "not fixed", "unchanged", "only reworded".
Counts as wrong: "fixed" or "partial" (e.g., treating the rewording or the new budget lines as addressing recurring costs; the new lines are year-1 one-offs).

### I3 — No accessibility or inclusion testing — **NOT FIXED**
Evidence (section 7): "ATLAS will launch in the national language, as a text-only chat. The interface follows the vendor's standard design." — identical to v1. No accessibility standard, no testing with older adults, people with disabilities or low digital literacy, no other languages; the disability fee waiver is still in scope.
Counts as correct: "not fixed" / "unchanged".
Counts as wrong: "fixed" or "partial" because the call center and offices remain open (that is the C3 fix; it does not provide accessibility of ATLAS itself), or because a pilot is now planned.

### I4 — Timeline contradicts the four-month procurement — **FIXED**
Evidence (section 9): "| 1–4 | Board approval, then procurement |" and "| 5–7 | Build, integration, security testing and impact assessment |", consistent with section 8 "takes about **four months**".
Counts as correct: "fixed". A review may also note that section 11 still says "month 6" — that is R1 and does not make I4 partial (the procurement/build conflict is resolved).
Counts as wrong: "not fixed" / "partial" (including "partial because of the month-6 report": give 0 for I4 status, but credit R1 if described).

### M1 — Budget total doesn't add up — **FIXED**
Evidence (section 10): items 420,000 + 180,000 + 40,000 + 35,000 + 25,000 + 30,000 = 730,000, and "| **Total** | **730,000** |". Section 1 also says "a year-1 budget of USD 730,000" (consistent).
Counts as correct: "fixed" — the table now adds up (and matches the summary).
Counts as wrong: "not fixed" / "partial", or a claim that the totals still don't match.

### M2 — Undefined acronyms — **FIXED**
Evidence (section 5): "a large language model with retrieval-augmented generation (RAG): it looks up the relevant passages in the procedure manuals and FAQ before answering. It will run on the cloud provider selected through the procurement in section 8". "CSP" no longer appears.
Counts as correct: "fixed" — RAG defined, CSP replaced by plain words.
Counts as wrong: "not fixed" / "partial". (Not in the change log, so a review that only reads the change log will miss it.)

### M3 — Unsourced 70% figure — **NOT FIXED**
Evidence (section 2): "About 70% of all inquiries are repetitive and could be answered automatically." Only "About" was added; still no source or method.
Counts as correct: "not fixed" / "unchanged" / "still unsourced".
Counts as wrong: "fixed" or "partial" (the hedge "About" is not a source).

### M4 — Scope says 12 procedures, lists 9 — **FIXED**
Evidence (section 4): the list now has 12 items, adding "10. Resident parking permits", "11. Property tax payment plans", "12. Pet registration".
Counts as correct: "fixed" — the count now matches. A review may add that item 11 contradicts the out-of-scope line (that is R2); the count mismatch itself is fixed.
Counts as wrong: "not fixed" / "partial" (including "partial because item 11 is out of scope": give 0 for M4 status, but credit R2 if described).

---

## Regressions and new flaw

Scoring: **FOUND (1)** if the review meets "Counts as found"; **PARTIAL (0.5)** per the item; **MISSED (0)** otherwise. For R1/R2 the review does not need to use the word "regression"; it must identify the inconsistency. Explicitly attributing it to the v2 edit is a plus but not required.

### R1 — Evaluation still at month 6, now before ATLAS exists (sections 11 vs 9 and 3)
Description: section 11 is unchanged from v1: "At month 6 the Digital Transformation Office will report to the Board on the success measures in section 3 and propose the procedures for phase 2." In v2, month 6 falls inside the build phase ("| 5–7 | Build, integration…"); the pilot only starts in month 8, the evaluation is in month 11 ("| 11 | Pilot evaluation and go/no-go (section 7) |"), and section 3's interim target is "at month 11". There are no results to report at month 6.
Why it is a regression: in v1, section 11 (month 6) matched the rollout table ("| 6 | Results report to the Board |"). The I4 fix moved the timeline and dropped the month-6 report from the table but did not update section 11, so a consistent element became inconsistent.
Counts as found: identifies that the month-6 report/evaluation in section 11 conflicts with the new timeline (pilot in months 8–10, evaluation in month 11) or that nothing will be live at month 6.
Partial (0.5): says the "evaluation timing is unclear/inconsistent" or "section 11 wasn't updated" without naming month 6 vs the new pilot/evaluation months; or mentions it only as a caveat to I4 without saying the two sections now conflict.

### R2 — Property tax added to scope, contradicting "tax matters" out of scope (section 4)
Description: to fix M4 the author added three procedures, including "11. Property tax payment plans", but the line below still reads "Out of scope for year 1: tax matters and procedures that require a notary." The pilot (months 8–10) and the early rollout fall in year 1, so the scope list and the exclusion contradict each other.
Why it is a regression: in v1 the 9 listed procedures were consistent with the out-of-scope line (no tax procedure). The M4 fix introduced the contradiction; it was not in v1.
Counts as found: points out that property tax payment plans (item 11) are a tax matter and conflict with the out-of-scope exclusion.
Partial (0.5): says the newly added procedures are questionable/unjustified or "check the new items against the out-of-scope list" without naming the tax conflict; or names item 11 as odd without linking it to the exclusion.

### N1 — Go/no-go decided by a conflicted steering committee on the vendor's own evaluation (section 7, referenced in section 9)
Description: new paragraph in section 7: "A steering committee, chaired by the project director with the vendor's delivery lead and the head of the call center, will review the vendor's pilot evaluation and take the go/no-go decision on the rollout." The decision to scale to the whole population is taken by the people delivering the project plus the vendor, which has a commercial interest in the rollout, on an evaluation the vendor itself prepares. There is no independent evaluation, no independent member (e.g., Data Protection Officer, legal, audit, citizen representative) and no Board approval of the rollout. The rollout table points to it: "| 11 | Pilot evaluation and go/no-go (section 7) |".
Why it is new: v1 had no pilot and no steering committee; this governance flaw comes entirely from content added in v2 and is not one of the 12 v1 flaws (it is not about data use (C1/C4), automated decisions (C2) or the existence of a pilot (C3)). It is not mentioned in the change log.
Counts as found: flags the conflict of interest / lack of independence — the vendor (and/or the project team) evaluating the pilot and deciding go/no-go — or that the Board/an independent body does not decide the rollout.
Partial (0.5): comments that the pilot needs "clear success criteria" or "more governance" for go/no-go without identifying the vendor/self-assessment conflict or the missing independent/Board decision.

---

## Not to be scored (acceptable observations)

These are not seeded and should neither earn nor lose points if a review mentions them:
- The year-1 platform license (420,000) is unchanged although the platform is only used from month 5.
- The resolution-time KPI has no separate numeric target (the target sits in the objective line).
- The change log's omissions and the C2 overstatement (credit goes through the C2 status, R2 and N1 items above).
- The DPIA and contract clauses are commitments still to be carried out.
