# Answer key: Rulebook test (call vs proposal)

**Materials**
- Call: `kit-materials/rulebook/call-en.md` (Spanish version: `call-es.md`). Meridian Fund for Digital Public Services, Call MF-CFP-2026/02, "Responsible Artificial Intelligence in Citizen Services".
- Proposal: `kit-materials/rulebook/proposal-en.md` (Spanish version: `proposal-es.md`). Larkfield Citizen Services Agency (LCSA), "ATLAS: An AI Assistant for Larkfield Citizen Services".
- The call has **42 requirements** (R01 to R42). The proposal meets 34 and fails **8** (F1 to F8).
- The Spanish versions have the same content, numbers and failures. Section numbers are the same. In Spanish, outcome indicator O4 is labelled **E4**.

**Reference figures (from the proposal's budget table, §10)**

| Item | Value |
|---|---|
| Grant, direct costs | USD 335,000 |
| Co-financing (all in kind) | USD 88,000 |
| Total direct costs | USD 423,000 |
| Indirect costs (grant) | USD 30,200 |
| Requested grant | USD 365,200 |
| Total project cost | USD 453,200 |
| Implementation period | 1 March 2027 – 31 August 2028 (18 months) |

---

## Part A: The 8 failures

### F1. Indirect costs exceed the 7% cap (numeric)
- **Requirement (R10, call §4):** "Indirect costs may be charged as a flat rate of up to 7% of total direct eligible costs."
- **Where it fails:** proposal §10, budget line 8.1 (USD 30,200).
- **Why:** the cap is 7% × 423,000 = **USD 29,610**. The proposal charges USD 30,200, which is 30,200 / 423,000 = **7.14%**, or USD 590 over the cap. The proposal states no rate, so the breach only shows if the ratio is computed. If the ineligible licence share from F4 (USD 7,500) is also removed, direct eligible costs fall to 415,500 and the ratio rises to 7.27%.
- **Counts as found:** says that indirect costs exceed 7% of direct costs, with a correct or approximately correct computation (about 7.1% to 7.3%, or a cap of about USD 29,610 or lower).
- **Partial (0.5):** raises the indirect-cost cap as a concern ("borderline", "verify") without concluding there is a breach, or concludes there is a breach using a wrong base or wrong arithmetic.

### F2. Co-financing below 20% of the total project cost (numeric)
- **Requirement (R08, call §4 and Annex I):** "Applicants must provide co-financing equal to at least 20% of the total project cost". Annex I defines total project cost as direct plus indirect costs, including both the grant and co-financing.
- **Where it fails:** proposal cover table, §10 budget table and the closing sentence of §10 ("roughly one fifth of the total project cost").
- **Why:** 88,000 / 453,200 = **19.42%**. The minimum is 20% × 453,200 = USD 90,640, so the shortfall is USD 2,640. The breach holds even after the F4 adjustment: 88,000 / 445,700 = 19.74%.
- **Counts as found:** concludes that co-financing is below 20% of the total project cost, with a correct or approximately correct computation (about 19.4%).
- **Partial (0.5):** flags co-financing as borderline or unverified ("about 20%, check") without concluding it falls short.
- **Note:** computing against direct costs (20.8%) or against the grant (24.1%) gives "met". That is a miss, not a partial.

### F3. Start date before the earliest permitted start date (contradiction with a date rule)
- **Requirement (R05, call §3):** "the earliest permitted start date of the implementation period is 1 April 2027, and no project activity may begin, and no cost may be incurred, before that date."
- **Where it fails:** proposal cover table ("1 March 2027 – 31 August 2028") and §4 ("Month 1 is March 2027", with the tender, inception work and the subscription payment in M1–M2).
- **Why:** the project starts one month before the earliest allowed date. The 18-month duration and the 31 August 2028 end date are both compliant, which hides the problem.
- **Counts as found:** says that the 1 March 2027 start date comes before the 1 April 2027 earliest start date.
- **Partial (0.5):** notes only a related symptom without citing the 1 April 2027 rule, for example that activities or costs fall before grant signature in March 2027, or that March 2027 costs would be ineligible.

### F4. Licence subscription prepaid beyond the end date (ineligible cost, buried in a long paragraph)
- **Requirement (R13, call §5, long paragraph):** "software licences, subscriptions and cloud services are eligible only for the portion of their term that falls within the implementation period … the share corresponding to any period after the end date of the project is not eligible and must be covered from other sources, even when it is paid during the implementation period."
- **Where it fails:** proposal §10, line 2.2 (USD 30,000) and its budget narrative: "contracted for 24 months from month 1 and paid at contract signature … USD 1,250 per month".
- **Why:** the implementation period is 18 months, but the subscription covers 24 months from M1. The 6 months after 31 August 2028 (6 × 1,250 = **USD 7,500**) are charged to the grant and are ineligible.
- **Counts as found:** says that the 24-month subscription extends beyond the 18-month implementation period, so part of line 2.2 is ineligible. Quantifying the amount (USD 7,500) is not required.
- **Partial (0.5):** notices the 24-month or prepaid subscription and questions it without concluding that part of it is ineligible, or cites the wrong rule (for example procurement) while still pointing at line 2.2's 24-month term.

### F5. Curricula vitae of key personnel not attached (missing annex)
- **Requirement (R22, call §6 annex list and Annex I):** "the curricula vitae of the key personnel". Annex I defines key personnel as, at a minimum, the project lead and the technical lead.
- **Where it fails:** proposal "Annexes" list (Annexes A–F). Annex F contains only an "Organisational chart … and terms of reference of project positions". The two leads appear in the cover table and in §4 with one-line bios, but no CVs are attached.
- **Why:** a mandatory annex is missing. The total number of annexes still looks complete, because Annex F stands in the place where CVs would be.
- **Counts as found:** says that the CVs of key personnel (the project lead and/or the technical lead) are missing from the annexes.
- **Partial (0.5):** says the annex list is incomplete or does not match the call, but does not name the CVs.

### F6. Risk matrix has no risk owner (missing mandatory element)
- **Requirement (R35, call §10):** "The risk matrix must indicate, for each risk identified, its likelihood, its impact, the mitigation measures and the risk owner, meaning the person or unit responsible…"
- **Where it fails:** proposal §8. The risk table has only the columns Risk | Likelihood | Impact | Mitigation. The only line about oversight is a general one ("reviewed quarterly by the steering committee"), which does not assign an owner to each risk.
- **Counts as found:** says that the risk matrix does not assign a risk owner or responsible person or unit to each risk.
- **Partial (0.5):** says the risk matrix is incomplete or lacks "responsibilities" in general terms, without tying this to per-risk owners. Also partial if it says the committee-level review is not enough but never says that owners are missing.

### F7. Outcome indicator without a quantified baseline (missing element)
- **Requirement (R25, call §7 and footnote 2):** "Every outcome indicator must have a quantified baseline value, stating the year to which the value refers and its source." Footnote 2 adds: "Where the applicant plans a survey during the project to refine existing data, the value available at the time of submission should still be reported as the baseline."
- **Where it fails:** proposal §5, outcome indicator **O4** (Spanish: E4), average time from first submission to decision for housing subsidy and disability fee waiver applications. Its baseline reads "Established from case records during inception (M3)" and its target is "30% reduction". §2 explains why the data is not available, which makes the gap look justified.
- **Counts as found:** identifies O4 (E4) as having no quantified baseline at submission.
- **Partial (0.5):** flags O4 only because its target is relative or unquantified, without mentioning the missing baseline, or makes a general remark that "some baselines are pending" without identifying O4.

### F8. Final evaluation budget below 3% of the grant (numeric, buried in a footnote)
- **Requirement (R41, call §14, footnote 3):** "The final evaluation must be budgeted at no less than 3% of the grant requested."
- **Where it fails:** proposal §10, line 6.2 "External final evaluation", USD 9,000.
- **Why:** 9,000 / 365,200 = **2.46%**. The minimum is 3% × 365,200 = USD 10,956, so the shortfall is USD 1,956. The independence of the evaluator (R40) is met, which can draw attention away from the amount.
- **Counts as found:** concludes that the evaluation budget is below 3% of the requested grant (about 2.5%, or below USD 10,956).
- **Partial (0.5):** questions whether the evaluation budget is sufficient without computing it or concluding a breach, or concludes a breach using the wrong base (for example 9,000 / 453,200 = 1.99% of the total cost).

**Mix of failure types:** numeric (F1, F2, F8); missing element (F5, F6, F7); contradiction with a rule (F3 date, F4 ineligible cost). F4 depends on a requirement buried in a long paragraph and F8 on one buried in a footnote. F7 also relies partly on footnote 2.

---

## Part B: Full requirement list

The verdict column uses "Met (proposal §x)" or "Not met → Fk". Proposal "§0" is the cover table; "Annexes" is the closing annex list.

| ID | Requirement (short quote) | Call § | Verdict |
|---|---|---|---|
| R01 | Applicant must be a "public-sector entit[y] at national or subnational level" that delivers services to the public; private companies, civil society organisations and universities are not eligible as applicants | §2 | Met (proposal §0, §2: LCSA, a public agency of the regional government) |
| R02 | "Applicants must have been legally constituted for at least three years on the date of the submission deadline" | §2, footnote 1 | Met (proposal §2: created by regional ordinance in 2015) |
| R03 | AI projects "must be designed as pilots limited in scope … and must define a go/no-go decision point, with explicit and measurable criteria"; the projects must be citizen-facing | §2 | Met (proposal §1, §4, §5: 2 offices + portal, 5 service types, go/no-go in M17 with quantified criteria) |
| R04 | Implementation period "no shorter than 12 months and no longer than 24 months" | §3 | Met (proposal §0: 18 months) |
| R05 | "earliest permitted start date … is 1 April 2027"; no activity or cost before that date | §3 | **Not met → F3** |
| R06 | "All projects must end no later than 31 December 2028" | §3 | Met (proposal §0: 31 August 2028) |
| R07 | Grant "no less than USD 150,000 and no more than USD 400,000" | §4 | Met (proposal §0, §10: USD 365,200) |
| R08 | Co-financing "at least 20% of the total project cost" | §4, Annex I | **Not met → F2** |
| R09 | In-kind contributions "valued at cost, and the valuation method … explained in the budget narrative" | §4 | Met (proposal §10 narrative for lines 1.3, 4.1, 7.1: salary cost × timesheet hours; internal cost rates; depreciated cost) |
| R10 | Indirect costs "up to 7% of total direct eligible costs" | §4 | **Not met → F1** |
| R11 | Permanent staff salaries "not eligible for grant funding"; may count only as in-kind co-financing | §5 | Met (proposal §10: lines 1.1–1.2 are fixed-term hires; permanent staff time, line 1.3, is in the co-financing column only) |
| R12 | "equipment of all kinds may … not exceed 10% of total direct costs" | §5 (long paragraph) | Met (proposal §10: 18,000 / 423,000 = 4.3%; still 6.6% if the in-kind server capacity in line 7.1 is counted) |
| R13 | Licences, subscriptions and cloud services eligible only for the part of their term within the implementation period | §5 (long paragraph) | **Not met → F4** |
| R14 | No ineligible costs from the list (land, buildings or construction, vehicles, debts, fines, interest or exchange losses, costs funded by other donors, contingency or unallocated lines) | §5 | Met (proposal §10: no such lines) |
| R15 | "Proposals must be written in English or Spanish" | §6 | Met (proposal §0; the documents are in English and Spanish) |
| R16 | Narrative "must not exceed 15 A4 pages, in a font size of at least 11 points" | §6 | Met (proposal §0: 13 A4 pages, 11-point font) |
| R17 | Narrative must contain the ten listed sections "in this order", with the content listed for each (for example §4: timeline, management and key personnel, procurement plan, reporting and evaluation; §10: table with separate grant and co-financing columns plus a narrative for each line) | §6 | Met (proposal §1–§10, same titles and order; listed contents present) |
| R18 | Summary "no more than 300 words", stating the problem, solution, results, grant and total cost | §6 | Met (proposal §1: about 213 words in English and 255 in Spanish; all elements present) |
| R19 | Annex: "the logical framework (logframe)" | §6 | Met (proposal Annexes: Annex A) |
| R20 | Annex: "the detailed budget, prepared in the Fund's spreadsheet template" | §6 | Met (proposal Annexes: Annex B; §0: spreadsheet format) |
| R21 | Annex: "a letter committing the co-financing, signed by the applicant's legal representative" | §6, Annex I | Met (proposal Annexes: Annex C, signed by the Director-General, legal representative under the founding ordinance) |
| R22 | Annex: "the curricula vitae of the key personnel" (project lead and technical lead at minimum) | §6, Annex I | **Not met → F5** |
| R23 | Annex: the DPIA, which "must cover the processing carried out in the pilot" | §6, §9 | Met (proposal §7 and Annex D: DPIA of the ATLAS pilot covering all processing) |
| R24 | Annex: "at least one letter of support from an organisation representing the users" | §6 | Met (proposal Annexes: Annex E, Disability Rights Network and Senior Citizens Council) |
| R25 | "Every outcome indicator must have a quantified baseline value, stating the year … and its source" | §7, footnote 2 | **Not met → F7** |
| R26 | Every indicator (outcome and output) "must have a quantified target for the end of the project and a means of verification" | §7 | Met (proposal §5: O1–O5 and P1–P5 all have a target and a means of verification; O4's relative target "30% reduction" is quantified, and O4's baseline problem is F7) |
| R27 | Section 6 "must include a gender and inclusion analysis" identifying groups at risk and the measures to address them | §8 (long paragraph) | Met (proposal §6: five groups, including women caregivers, plus measures) |
| R28 | All digital interfaces "must conform to the applicable national web accessibility standard at its intermediate conformance level or higher" | §8 (long paragraph) | Met (proposal §6: conversational interface, portal, kiosk and tablet interfaces; external audit; P4) |
| R29 | No service only available through the AI channel; in-person and telephone channels "must remain available on equal terms throughout the project" | §8 (long paragraph) | Met (proposal §1, §6: unchanged hours and staffing, during and after the project) |
| R30 | User testing "before and during the pilot, must include persons with disabilities and older persons (aged 65 or over)" | §8 (long paragraph) | Met (proposal §5 P5, §6: 60 users with ≥15 persons with disabilities and ≥15 aged 65+; same quotas in the two rounds during the pilot) |
| R31 | Section 7 "must describe the legal basis for each processing …, the categories of personal data … and the retention periods" | §9 | Met (proposal §7: Legal basis, Categories of data and Retention paragraphs) |
| R32 | Personal data "may not be used to train, fine-tune or otherwise improve AI models", including by providers; "contracts with providers must exclude such use" | §9 | Met (proposal §7: retrieval only; contracts with the platform and integration providers exclude such use) |
| R33 | Decisions on benefits or entitlements "must be taken by a human officer"; AI may only support them (simple transactional operations may be automated) | §9 | Met (proposal §1, §7: pre-check only, a case officer decides; certificates only reproduce existing records) |
| R34 | Users "clearly informed that they are interacting with an AI system" and "able to reach a human agent at any point" | §9 | Met (proposal §7: notice at the start of every conversation; "talk to a person" at every step, by chat or 24-hour phone line) |
| R35 | Risk matrix must give "for each risk … its likelihood, its impact, the mitigation measures and the risk owner" | §10 | **Not met → F6** |
| R36 | Commitment to fund operating costs "for at least 12 months after the end of the implementation period" and to "identify the source of those funds" | §11 | Met (proposal §9: 24 months, regular operating budget programme 03; Annex C) |
| R37 | Contracts above USD 50,000 awarded competitively with "at least three valid offers"; relaunch or Fund approval if fewer | §12 | Met (proposal §4: integration services, USD 96,000, open tender, ≥3 offers, relaunch if fewer; no other contract is above USD 50,000) |
| R38 | Visibility costs as "a separate line … not exceed[ing] 2% of the grant requested"; Fund logo in communication materials, publications and the solution's user interfaces | §13 | Met (proposal §10 line 5.1: 6,000 / 365,200 = 1.64%; narrative 5.1 covers materials, publications, the welcome screen and kiosks) |
| R39 | Progress reports "for every six-month period … within 30 days" and a final narrative and financial report "within 60 days of the end date" | §14 | Met (proposal §4: reports for M1–6, M7–12, M13–18 within 30 days; final report by 30 October 2028) |
| R40 | "an independent external final evaluation" (no contractual or hierarchical relationship with the applicant for project delivery) | §14, footnote 3 | Met (proposal §4: external evaluator selected competitively, no such relationship; line 6.2) |
| R41 | "The final evaluation must be budgeted at no less than 3% of the grant requested" | §14, footnote 3 | **Not met → F8** |
| R42 | Submitted "through the Fund's online portal no later than 15 January 2027 at 17:00 UTC", narrative as a single PDF, budget in spreadsheet format, other annexes as separate PDFs | §15 | Met (proposal §0: portal, 12 January 2027, formats as required) |

**Totals:** 42 requirements: 34 met, 8 not met (R05, R08, R10, R13, R22, R25, R35, R41 → F3, F2, F1, F4, F5, F7, F6, F8).

---

## Scoring notes

- **Compound requirements.** R03, R14, R17, R34, R37, R38, R39 and R42 bundle several conditions. A tool may list their parts separately. For coverage, credit the requirement if all its parts are covered. For false alarms, count at most one per requirement ID.
- **Not requirements.** The following text in the call is descriptive and does not count for coverage: the purpose and envelope (§1); the instalment schedule (§4); the extension policy (§3); the "encourages" or "expects to consider" guidance in §7 and §10 (3–6 outcome indicators, a user-experience indicator, risk categories); the scaling plans the Fund "will value" (§11); the Fund's monitoring visits and its review of evaluation terms of reference; the helpdesk, selection criteria and results date (§15); and the Annex I definitions themselves. The proposal satisfies all of this guidance anyway (5 outcome indicators including O3 and O5; all 5 risk categories appear in §8).
- **Consequences of the failures.** These are not extra failures. Costs incurred in March 2027 being ineligible is a consequence of F3; count it under F3. Indirect costs and co-financing ratios recomputed after removing the F4 amount still fail; count them under F1 and F2.
- **Likely false alarms. These requirements are MET:**
  - Certificates issued automatically: allowed by §9, because they reproduce existing records.
  - Co-financing entirely in kind: allowed by §4.
  - Subscription bought through a request for quotations: allowed, because USD 30,000 is under the USD 50,000 threshold.
  - Kiosks bought under a framework agreement: allowed, at USD 18,000.
  - Equipment cap: met even if the in-kind server capacity counts as equipment (6.6%).
  - Sustainability commitment: unconditional and longer than required (24 months). The go/no-go decision concerns only extension to other offices.
  - Human contact outside chat hours: provided through the 24-hour telephone line.
  - O4's relative target ("30% reduction"): the defect is the missing baseline (F7), not the target.
  - Disaggregation by sex, age and disability: not required by the call, and the proposal offers it anyway.
