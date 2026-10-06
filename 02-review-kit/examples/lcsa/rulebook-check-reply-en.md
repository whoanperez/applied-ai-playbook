**Checked against:** Meridian Fund Call for Proposals MF-CFP-2026/02 (published 1 October 2026) · **Work:** ATLAS proposal, LCSA (narrative, budget and annex list)
**Result:** 62 requirements · ✅ 46 met · ❌ 8 not met · ◐ 1 partly met · ? 7 can't verify
**Verdict:** Not as it stands. Two eligibility failures come first: the implementation period starts on 1 March 2027, before the earliest permitted date of 1 April 2027, and co-financing is 19.4%, below the 20% minimum. The CVs of the key personnel are also missing from the annexes (admissibility). The budget has three further errors, all fixable in one pass: indirect costs over the cap, 6 months of subscription charged beyond the project end, and an evaluation line under 3%. The rest of the proposal is in good shape. Your inclusion, data protection and human-decision sections meet the call's strict conditions.

I checked every figure with code. Dates and money below are computed, not estimated.

### Fix before submitting

1. **R07 · Start date before the permitted date** · call §3 → proposal cover table, §4, §9
   - **Rule:** "the earliest permitted start date of the implementation period is 1 April 2027, and no project activity may begin, and no cost may be incurred, before that date."
   - **Problem:** The cover table says "18 months, 1 March 2027 – 31 August 2028" and §4 says "Month 1 is March 2027". The call allows no earlier start.
   - **Fix:** Keep 18 months and shift everything by one month. Cover table: "Implementation period: 18 months, 1 April 2027 – 30 September 2028". §4: "Month 1 is April 2027." Dates that follow from this:
     - The final report is due within 60 days of 30 September 2028, that is **by 29 November 2028**. §4 currently says 30 October 2028.
     - §9: "at least 24 months after **30 September 2028**".
     - The end date is still before the 31 December 2028 limit (R08).
     - Re-check Annex B and the Annex C letter for the old dates.
     - The month numbers (M1–M18) and the work plan do not change.

2. **R10 · Co-financing below 20%** · call §4 → proposal §10
   - **Rule:** "co-financing equal to at least 20% of the total project cost (as defined in Annex I)."
   - **Problem:** 88,000 / 453,200 = **19.4%** < 20% (the minimum is 90,640). The sentence "roughly one fifth" does not hold. Raising the in-kind amount also raises the total, so the gap is larger than the 2,640 it looks like. With the other budget corrections below, you need at least about USD 1,850 more.
   - **Fix:** Use the corrected budget table under R12. It adds 100 hours of permanent staff time on line 1.3 (2,500 h × USD 22.50 = 56,250), which gives 90,250 / 449,650 = **20.07%**. Add the hours only if they are real and will be in timesheets. Any other documented in-kind cost works too. Replace "roughly one fifth" with: "LCSA's contribution of USD 90,250, entirely in kind, represents 20.1% of the total project cost." Update the cover table and the Annex C letter to USD 90,250.

3. **R30 · CVs of key personnel missing** · call §6 and Annex I → proposal Annexes
   - **Rule:** "the curricula vitae of the key personnel (see Annex I)", meaning at least the project lead and the technical lead.
   - **Problem:** Annex F contains only an organisational chart and the terms of reference of project positions. No annex has CVs.
   - **Fix:** Add to the annex list: "**Annex G** — Curricula vitae of the key personnel: Mr. Tomas Rivell (project lead) and Ms. Amara Okafor (technical lead)". Submit it as a separate PDF.

4. **R12 · Indirect costs over the 7% cap** · call §4, Annex I → proposal §10, line 8.1
   - **Rule:** "a flat rate of up to 7% of total direct eligible costs." Annex I defines direct eligible costs as those "financed by the grant or by co-financing".
   - **Problem:** 30,200 / 423,000 = **7.14%** > 7%. The cap on that base was 29,610, so you are 590 over.
   - **Fix:** Recompute on the corrected direct costs of 420,250 (see the table below). The cap is 7% × 420,250 = 29,417.50, so use **USD 29,400**.

5. **R15 · Subscription charged beyond the project end** · call §5 → proposal §10, line 2.2
   - **Rule:** "the share corresponding to any period after the end date of the project is not eligible and must be covered from other sources, even when it is paid during the implementation period."
   - **Problem:** The subscription is "contracted for 24 months from month 1" at 1,250 a month, so 30,000 is charged to the grant. Only 18 months fall inside the project: 18 × 1,250 = 22,500. The other 7,500 is ineligible.
   - **Fix:** Set line 2.2 to USD 22,500. Replace the 2.2 narrative with: "Subscription to the language model and cloud platform, contracted for 24 months from month 1 at USD 1,250 per month. The grant finances the 18 months within the implementation period (USD 22,500). The remaining six months (USD 7,500) are paid by LCSA from programme 03 and are not counted as co-financing." The extra 7,500 cannot count as co-financing either.

6. **R60 · Final evaluation budget under 3% of the grant** · call §14, footnote 3 → proposal §10, line 6.2
   - **Rule:** "The final evaluation must be budgeted at no less than 3% of the grant requested."
   - **Problem:** 9,000 / 365,200 = **2.46%** < 3% (the minimum was 10,956).
   - **Fix:** Set line 6.2 to USD 11,500. On the corrected grant of 359,400 that is 3.20% (the minimum is 10,782).

   **Corrected budget, covering R10, R12, R15 and R60 together:**

   | Line | Grant | Co-financing | Total |
   |---|---:|---:|---:|
   | 1.3 Permanent staff time, in kind (2,500 h × 22.50) | – | 56,250 | 56,250 |
   | 2.2 Platform subscription (18 × 1,250) | 22,500 | – | 22,500 |
   | 6.2 External final evaluation | 11,500 | – | 11,500 |
   | Total direct costs | 330,000 | 90,250 | 420,250 |
   | 8.1 Indirect costs (≤ 7% × 420,250 = 29,417.50) | 29,400 | – | 29,400 |
   | **Total project cost** | **359,400** | **90,250** | **449,650** |

   Other lines are unchanged. After the changes:
   - The grant is USD 359,400, within the 150,000–400,000 range.
   - Co-financing is 20.07% of the total.
   - Visibility is 6,000 / 359,400 = 1.67% (≤ 2%).
   - Equipment is 18,000 / 420,250 = 4.3% (≤ 10%).
   - Update the grant and total figures in the cover table, in the §1 Summary ("USD 359,400; the total project cost is USD 449,650"), in Annex B and in the Annex C letter.

7. **R33 · Outcome indicator O4 has no quantified baseline** · call §7 and footnote 2 → proposal §5, O4
   - **Rule:** "Every outcome indicator must have a quantified baseline value, stating the year to which the value refers and its source." Footnote 2: where a survey is planned to refine existing data, "the value available at the time of submission should still be reported as the baseline."
   - **Problem:** O4's baseline reads "Established from case records during inception (M3)". That is not a value. Only output indicators that measure new products may start from zero.
   - **Fix:** Report the best value you have today, even if imperfect. Suggested wording: "[X] days (2026, LCSA case management system; measured per registered file, so it understates the true time because resubmissions open a new file; to be refined from case records in M3)". Take X from an extract before 12 January. Because SO2 has no indicator that can be baselined now, also add a sixth outcome indicator. That keeps you within the 3–6 the call suggests:
     > O6. Share of housing subsidy and disability fee waiver applications returned as incomplete | 31% (2026, LCSA case management system) | 20% | Case management system extracts
     The 20% target is a placeholder for you to confirm. Questions to the Fund's helpdesk are open until 15 December 2026 if you want its view on O4.

8. **R50 · Risk matrix has no risk owner** · call §10 → proposal §8
   - **Rule:** the matrix "must indicate, for each risk identified, its likelihood, its impact, the mitigation measures and the risk owner".
   - **Problem:** The table has Likelihood, Impact and Mitigation columns but no owner column.
   - **Fix:** Add a "Risk owner" column. Suggested owners, for you to confirm:

     | Risk | Risk owner |
     |---|---|
     | Incorrect or invented answers | Technical lead (A. Okafor) |
     | Personal data breach | Data Protection Officer |
     | Low adoption by staff | Project lead (T. Rivell) |
     | Exclusion of older users and persons with disabilities | Project coordinator |
     | Integration tender delay | Project lead, with LCSA procurement |
     | Change in institutional priorities | Director-General |

9. **R41 · Legal basis stated once for all processing** · call §9 → proposal §7
   - **Rule:** Section 7 "must describe the legal basis for each processing of personal data".
   - **Problem:** §7 gives one basis for "all processing" plus one for health data. Conversation logs kept for quality sampling and uploaded documents are different processing, and an evaluator can read the text as a blanket statement.
   - **Fix:** Replace "Legal basis" with a short table. Check the basis for each row with your Data Protection Officer:

     | Processing | Legal basis |
     |---|---|
     | Identification, appointments and request status | Performance of LCSA's public-service tasks under its founding ordinance |
     | Document pre-check, including health data in disability certificates | Public-service tasks under the ordinance, and [article] of the applicable data protection law for social benefits |
     | Conversation logs (90 days, quality sampling) | [basis, e.g. the same public task of ensuring service quality] |

### Compliance matrix

| # | Requirement (call §) | Status | Evidence in the work |
|---|---|---|---|
| R01 | Applicant is a national or subnational public entity delivering services (§2) | ✅ | Cover: "public agency of the Larkfield regional government" |
| R02 | Applicant legally constituted at least 3 years at the deadline (fn 1) | ✅ | §2: "created by regional ordinance in 2015", about 11 years |
| R03 | Project introduces AI tools in a listed citizen service (§2) | ✅ | §1: appointments, request status, certificates, document pre-check |
| R04 | Designed as a pilot limited in scope (§2) | ✅ | §1: "two service offices... and on the LCSA web portal" |
| R05 | Go/no-go point with explicit, measurable criteria (§2) | ✅ | §5: month 17; accuracy ≥ 95%, O1 down ≥ 30%, O3 ≥ 3.9, no serious incident |
| R06 | Duration 12–24 months (§3) | ✅ | 1 Mar 2027 – 31 Aug 2028 = 18 months |
| R07 | Start not before 1 Apr 2027; no activity or cost earlier (§3) | ❌ | Cover: "1 March 2027"; §4: "Month 1 is March 2027" |
| R08 | End no later than 31 Dec 2028 (§3) | ✅ | 31 Aug 2028 (30 Sep 2028 after the fix) |
| R09 | Grant between USD 150,000 and 400,000 (§4) | ✅ | USD 365,200 (359,400 after the fix) |
| R10 | Co-financing at least 20% of total project cost (§4) | ❌ | 88,000 / 453,200 = 19.4% |
| R11 | In-kind valued at cost, method explained (§4) | ✅ | 1.3: 2,400 h × 22.50 = 54,000; 4.1: 24 × 250 = 6,000; 7.1: 18 × 1,000 + 10,000 = 28,000 |
| R12 | Indirect costs at most 7% of total direct eligible costs (§4, Annex I) | ❌ | 30,200 / 423,000 = 7.14% > 7% |
| R13 | Permanent staff salaries not charged to the grant (§5) | ✅ | 1.1–1.2 fixed-term; 1.3 "counted only as in-kind co-financing" |
| R14 | Equipment of all kinds at most 10% of total direct costs (§5) | ✅ | 18,000 / 335,000 = 5.4%; with existing equipment, 28,000 / 423,000 = 6.6% |
| R15 | Licences and cloud eligible only for the portion within the project (§5) | ❌ | 2.2: 24 months × 1,250 = 30,000; only 18 × 1,250 = 22,500 is eligible |
| R16 | No land, vehicles, debts or fines, or contingency lines (§5) | ✅ | None among budget lines 1.1–8.1 |
| R17 | No cost already financed by another donor or Fund grant (§5) | ? | No statement in the proposal |
| R18 | Written in English or Spanish (§6) | ✅ | English |
| R19 | Narrative at most 15 A4 pages, at least 11 pt (§6) | ? | Cover states "13 A4 pages in 11-point font"; the PDF was not shared |
| R20 | Ten sections, in the required order (§6) | ✅ | Sections 1–10 in order, with the required titles |
| R21 | Summary of at most 300 words (§6) | ✅ | 213 words |
| R22 | Summary states problem, solution, results, grant, total cost (§6) | ✅ | §1 covers all five |
| R23 | Section 4 has activities, timeline, management and key personnel, procurement plan, reporting and evaluation (§6) | ✅ | §4: A1–A5, quarterly Gantt, management paragraph, procurement plan, reporting paragraph |
| R24 | Summary budget table by line, separate grant and co-financing columns (§6) | ✅ | §10 table |
| R25 | Narrative justifying each line (§6) | ✅ | §10 narrative covers lines 1.1 to 8.1 |
| R26 | Annex: logframe, reproducing the §5 framework (§6, §7) | ? | Listed as Annex A; not shared |
| R27 | Annex: detailed budget in the Fund's spreadsheet template (§6) | ? | Listed as Annex B; not shared |
| R28 | Annex: co-financing letter signed by the legal representative (§6, Annex I) | ? | Annex C "signed by the Director-General", who is the legal representative; the letter was not shared |
| R29 | Annex: DPIA covering the processing in the pilot (§6, §9) | ? | §7: "completed in November 2026"; Annex D not shared |
| R30 | Annex: CVs of key personnel (§6, Annex I) | ❌ | Annexes A–F include no CVs |
| R31 | Annex: at least one letter of support from a users' organisation (§6) | ? | Annex E lists two; the letters were not shared |
| R32 | Results framework in Section 5 separates outcomes and outputs (§7) | ✅ | §5: outcome table O1–O5, output table P1–P5 |
| R33 | Each outcome indicator has a quantified baseline, with year and source (§7) | ❌ | O4: "Established from case records during inception (M3)"; O1–O3 and O5 comply |
| R34 | Every indicator has a quantified end-of-project target (§7) | ✅ | O1–O5 and P1–P5 all have targets |
| R35 | Every indicator has a means of verification (§7) | ✅ | Present for all ten |
| R36 | Gender and inclusion analysis, groups at risk and measures, in Section 6 (§8) | ✅ | §6: five at-risk groups, measures listed |
| R37 | All interfaces meet the national accessibility standard at intermediate level or higher (§8) | ✅ | §6: conversational, portal, kiosk and tablet interfaces; external audit before go-live and in month 12 |
| R38 | No service available only through the AI channel (§8) | ✅ | §6: all pilot services "remain available in person and by telephone" |
| R39 | In-person and phone channels on equal terms throughout (§8) | ✅ | §6: "unchanged opening hours and staffing, during and after the project" |
| R40 | User testing before and during the pilot includes persons with disabilities and people 65+ (§8) | ✅ | §6: 60 users with ≥ 15 each before go-live; same quotas in the two pilot rounds (M8, M13) |
| R41 | Legal basis described for each processing (§9) | ◐ | §7: one blanket basis for "All processing" |
| R42 | Categories of personal data described (§9) | ✅ | §7: identification, request references, uploaded documents, logs |
| R43 | Retention periods described (§9) | ✅ | §7: logs 90 days, case file 5 years, appointments 2 years |
| R44 | No training of AI on personal data; provider contracts exclude it (§9) | ✅ | §7: retrieval only; contracts "will exclude any use of LCSA data to train or improve" |
| R45 | Entitlement decisions taken by a human officer (§9) | ✅ | §7: ATLAS "cannot approve, reject or modify an application" |
| R46 | Users told they are talking to an AI (§9) | ✅ | §7: notice at the start of every conversation, portal and kiosks |
| R47 | Human agent reachable at any point (§9) | ✅ | §7: "talk to a person" option at every step |
| R48 | Risk matrix in Section 8 (§10) | ✅ | §8 table |
| R49 | Each risk has likelihood, impact, mitigation (§10) | ✅ | Three columns filled for all six risks |
| R50 | Each risk has a risk owner (§10) | ❌ | No owner column |
| R51 | Section 9 explains how the solution is run after the grant (§11) | ✅ | §9: USD 52,000 a year, what it covers |
| R52 | Commit to fund operations at least 12 months after the end (§11) | ✅ | §9: "at least 24 months" |
| R53 | Source of the operating funds identified (§11) | ✅ | §9: "programme 03, 'Digital channels'" |
| R54 | Contracts above USD 50,000 awarded by competition with at least 3 valid offers (§12) | ✅ | Only 2.1 (96,000) exceeds 50,000: open tender, "at least three valid offers", relaunch if fewer |
| R55 | Visibility a separate line, at most 2% of the grant (§13) | ✅ | 5.1: 6,000 / 365,200 = 1.64% (limit 7,304) |
| R56 | Fund support and logo shown on materials, publications and interfaces (§13) | ✅ | 5.1: "all communication materials, publications, the ATLAS welcome screen and the kiosks" |
| R57 | Progress reports every six months, within 30 days (§14) | ✅ | §4: months 1–6, 7–12, 13–18, each within 30 days |
| R58 | Final report within 60 days of the end date (§14) | ✅ | 31 Aug 2028 + 60 days = 30 Oct 2028; becomes 29 Nov 2028 after R07 |
| R59 | Independent external final evaluation (§14, fn 3) | ✅ | §4: external evaluator, selected competitively, no contractual or hierarchical relationship |
| R60 | Evaluation budgeted at no less than 3% of the grant (fn 3) | ❌ | 9,000 / 365,200 = 2.46% < 3% |
| R61 | Submitted via the portal by 15 Jan 2027, 17:00 UTC (§15) | ✅ | Cover: 12 January 2027 |
| R62 | Narrative as one PDF, budget as the original spreadsheet, other annexes as separate PDFs (§15) | ✅ | Cover states exactly this |

### Check by hand

- **R19 · Page count:** confirm the final PDF is 15 A4 pages or fewer at 11 pt. After adding the risk-owner column, the legal-basis table and the O6 row, check the count again.
- **R26–R29, R31 · Annexes:** open each annex and confirm:
  - Annex A repeats the §5 indicators, including the new O4 baseline and O6.
  - Annex B is on the Fund's template and matches the corrected budget.
  - Annex C is signed by Ms. Varga, states USD 90,250, and uses the new dates.
  - Annex D covers every processing in §7.
  - Annex E contains actual signed letters.
- **R29 · DPIA date:** §7 says the DPIA "was completed in November 2026". Today is 6 October 2026, so that is still ahead. Make sure it is really finished before 12 January 2027, or reword the sentence to match its true status.
- **R17 · Double funding:** confirm that none of the lines (the staff time, the server capacity, the kiosks) is already paid for by another grant or donor.
- **R07 · Start date in practice:** nothing may be spent or started before 1 April 2027. That includes paying the subscription and issuing the tender. The risk table says tender documents are "prepared in advance", so check that this preparation has no costs or project activity before that date.

### Recommended, not required

1. **Add a technological risk to §8.** The call lists "technological risks" among those it expects. Your table has none, for example integration with the legacy systems failing or a platform outage. It would also help the design and methodology score.
2. **Say what follows a "no-go" in §5.** The call frames the decision as whether to "scale, adjust or discontinue". Add: "If the criteria are not met, LCSA will adjust ATLAS or discontinue it, and report the reasons."
3. **Align the O1 baseline wording.** §2 says 38 minutes is the average wait at the two busiest offices, while O1 calls it the wait for "low-risk procedures". Use one definition in both places so an evaluator cannot question the 38-to-22 target.

Would you like me to apply all of these fixes to the proposal text? I would also put the corrected budget table into §10, with its narrative and the figures in the cover table and §1.
