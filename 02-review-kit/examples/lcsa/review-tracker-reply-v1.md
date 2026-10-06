**Project ATLAS · v1 first review** · Score 1.5 / 5

**Verdict:** I would not take this to the Board as it is. The idea is reasonable, but three things would stop an approval: the plan issues benefit decisions without human review, it sends citizens' medical and ID data to a vendor that may reuse it, and its timeline and budget do not add up.

I judged it as the Executive Board would: they approve the plan and USD 780,000, so they expect consistent numbers, an achievable timeline, privacy and automated-decision obligations met, an honest account of who is affected, and measures that prove the objective. The rubric and 18 findings are in the ledger below (6 Critical, 9 Important, 3 Minor).

## Critical (fix before it goes to the Board)

**F-01 · Automated decisions (§5).** ATLAS "will issue the decision automatically" on housing subsidy and disability fee waiver, with no human review and no appeal, while every answer says it "may contain errors". These are benefit decisions for vulnerable people. *Fix:* no decision (at least no denial) is issued without review by a named staff role, and the plan says how a citizen contests it. Consider a rules engine for eligibility, with the LLM only collecting documents and explaining.

**F-02 · Sensitive data export (§6).** 2.3 million case files with national IDs, contact details and medical certificates go to the vendor, with no minimisation, legal basis or privacy impact assessment. *Fix:* remove or de-identify those fields, or name the legal basis and a completed privacy/legal clearance before the export. Please check with your legal counsel which data-protection rules apply to you.

**F-03 · Vendor terms (§8).** The standard terms let the vendor use your case files and interactions to "improve its products and models" and host in its global cloud. This contradicts §6. *Fix:* the contract prohibits that use and states where the data is hosted and why that is allowed.

**F-04 · Timeline (§8 vs §9).** Procurement takes four months, but the rollout approves in month 1, builds in month 2 and goes live in month 3. *Fix:* start build after award and move go-live and the year-1 target accordingly.

**F-05 · Cuts scheduled before results (§9).** Month 4 closes 40% of call-center positions and cuts office hours, two months before the month-6 results report. *Fix:* make the cuts conditional on measured results at a go/no-go gate.

**F-06 · No human fallback (§5, §7, §9).** There is no handoff to a person, while call-center and office capacity shrink. Citizens without a smartphone or digital skills are left without a channel. *Fix:* a human handoff on every channel and a non-digital route for each in-scope procedure, with staffing.

## Important

- **F-07 · Budget (§10, §1).** The lines add to 750,000 (420+180+95+25+30), not 780,000. *Fix:* lines sum to the total and §1 asks for the same amount.
- **F-08 · Years 2–3 "cost-neutral" (§10).** No numbers; the license alone is 420,000 a year and there are no recurring costs or quantified savings. *Fix:* a three-year table with recurring costs and savings, or drop the claim.
- **F-09 · Objective not measured (§3).** The goal is 11 to 4 days, but neither measure tracks resolution time. *Fix:* add resolution time with baseline and method.
- **F-10 · No quality or equity measures (§3, §11).** Nothing on error rate, escalations or who cannot use ATLAS. *Fix:* add a correctness measure (audit sample) and an escalation/abandonment measure with targets.
- **F-11 · Big-bang launch (§9).** Nationwide, all channels, no pilot or rollback. *Fix:* a limited pilot with go/no-go criteria first.
- **F-12 · Staff impact not disclosed (§1, §9).** The summary says staff will "focus on complex cases"; §9 closes positions. *Fix:* say it in §1 and state what happens to affected staff.
- **F-13 · Accessibility (§7).** Text-only, one language, standard design, for an agency that serves people with disabilities. *Fix:* an accessibility requirement and an accessible alternative, checked before launch.
- **F-14 · Risk register (§7).** Three generic risks; a notice and vendor certificates are not mitigations. Missing: data misuse, wrong decisions, exclusion, vendor dependency. *Fix:* add them, each with an acting mitigation and an owner.
- **F-15 · The 4-day target is not derived (§3, §5).** Most of the saving is said to come from the automated decisions that F-01 says need review. *Fix:* show the calculation or pilot evidence consistent with the review you keep.

## Minor
- **F-16 · Unsourced baselines (§2).** 70% repetitive, 11 days, "one call in five", and the strategy is unnamed. *Fix:* state source or method.
- **F-17 · "12 procedures" (§4).** Only 9 are listed. *Fix:* make the number and the list match.
- **F-18 · Dangling reference (§5).** "The CSP selected in section 8": §8 selects none. *Fix:* name it in §8 or say it will be selected in procurement.

## Score (same rubric every version)
Consistency 2 · Evidence 2 · Obligations 1 · People affected 1 · Feasibility and cost 1 · Measures and risk 2 → **1.5 / 5**.

## What to do first
Fix F-01 to F-06 (they change the design), then F-07 and F-08 (the numbers the Board votes on). Several are cheap: F-07, F-17 and F-18 are quick edits.

Keep the file **review-ledger.md** in your project. When you have a v2, share it with that file, and I will check each finding against it, look for anything the edits broke, and score with the same rubric.

---

# Review ledger — Project ATLAS, AI Assistant for Citizen Services (implementation plan)
Judged by: LCSA Executive Board · Standard: consistent numbers, achievable timeline, privacy and automated-decision obligations met before approval, honest account of who is affected, full multi-year cost, measures that prove the objective.

(Full ledger with the rubric, anchors, and each finding's "Fixed when…" and "Could also" is saved in review-ledger.md.)

| Version | Date | Score | Open: C / I / M |
|---|---|---|---|
| v1 | 2026-10-06 | 1.5 / 5 | 6 / 9 / 3 |
