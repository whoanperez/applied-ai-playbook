**Project ATLAS implementation plan · v2.0 vs v1.0** · Score 1.5 → 3.0 / 5
**Verdict:** Much better: all four of the original Critical findings on data, contract, timeline and cuts are resolved. It is not ready for the Board yet, because two Critical findings are only partly fixed (no way to contest a decision; no handoff from the chat to a person) and the edits introduced three new inconsistencies.

One note on the change log: it says "Eligibility decisions are now reviewed by a caseworker." In the text, only denials are reviewed. Approvals are still issued automatically.

### Status of the open findings
| ID | Finding | v1 | v2 | Evidence |
|---|---|---|---|---|
| F-01 | Automated benefit decisions, no review or appeal | Open | **Partly fixed** | §5: "When the rules point to a denial, a caseworker reviews the case…". Missing: how a citizen contests a decision. |
| F-02 | Fine-tuning on 2.3M case files sent to the vendor | Open | **Fixed** | §6: "ATLAS will **not** be fine-tuned on case files… No case data is exported to the vendor." DPIA and legal basis before the pilot. |
| F-03 | Vendor standard terms (data use, global cloud) | Open | **Fixed** | §8: in-country hosting, "no use of agency data or interactions to train or improve the vendor's products or models", certified deletion at exit. |
| F-04 | Go-live before procurement ends | Open | **Fixed** | §9: procurement months 1–4, build 5–7, pilot 8–10, go/no-go 11; §3 target moved to end of year 2. |
| F-05 | Closures fixed on the calendar | Open | **Fixed** | §9: "The call center and the 14 offices keep their current hours throughout." |
| F-06 | No human fallback | Open | **Partly fixed** | Non-digital channels kept (§9). Missing: a handoff from the ATLAS chat to a person. |
| F-07 | Budget lines do not add to the total | Open | **Fixed** | 420+180+40+35+25+30 = 730,000 = §10 total = §1 request. |
| F-08 | Years 2–3 "cost-neutral", no numbers | Open | **Not fixed** | §10: "From year 2, ATLAS is expected to pay for itself" is a rewording. No table, no recurring costs, no savings figures. |
| F-09 | Objective not measured | Open | **Fixed** | §3: "Average resolution time for in-scope procedures, from the case management system." |
| F-10 | No quality or equity measures | Open | **Partly fixed** | Accuracy measure added (95%, monthly sample). Missing: a measure of escalation or abandonment. |
| F-11 | Big-bang nationwide launch | Open | **Partly fixed** | Two-district pilot and go/no-go at month 11. Missing: the go/no-go criteria. |
| F-12 | Summary hides job and hours impact | Open | **Fixed (watch)** | No closures or hours cut remain. Reopens if the §10 savings are meant to come from staff reductions (see R-03). |
| F-13 | No accessibility | Open | **Not fixed** | §7 unchanged: "text-only chat. The interface follows the vendor's standard design." |
| F-14 | Token risk register | Open | **Partly fixed** | "Misuse of personal data" added and better mitigations for two risks. Missing: wrong decisions, exclusion, vendor dependency; no owners. |
| F-15 | 4-day target not derived | Open | **Not fixed** | Target moved to year 2 with a 7-day interim, but no calculation. "This is where most of the time savings come from" is unchanged. |
| F-16 | Baselines unsourced | Open | **Not fixed** | Only "About 70%" was added; no source or period. |
| F-17 | "12 procedures", 9 listed | Open | **Fixed** | §4 lists 12 (but see R-01). |
| F-18 | §5 refers to a CSP that §8 never selects | Open | **Fixed** | §5: "the cloud provider selected through the procurement in section 8". |

### Regressions (broke in this version)
1. **R-01 · Tax item inside the tax exclusion** · §4. To reach 12 procedures, item 11 "Property tax payment plans" was added, but the section still says "Out of scope for year 1: tax matters". Fix: remove or rename the item, or state the exception in the exclusion. Also show the volumes that make the three added procedures "highest-volume".
2. **R-02 · Evaluation date no longer fits the timeline** · §11 vs §9. §11 still has the report on the success measures "at month 6", but months 5–7 are build and testing and the pilot runs in months 8–10. No results can exist at month 6. Fix: report on the pilot at the month-11 go/no-go, then after each rollout phase.
3. **R-03 · Savings with no mechanism** · §10 vs §9. §10 says efficiency gains "in the call center and the offices" will cover the platform. v2 removed the closures and keeps all hours, so nothing produces the saving. If the plan means staff reductions later, the Board is not being told. Fix: name a mechanism consistent with §9, or drop the claim. Resolve it together with F-08.

### New findings
- **F-19 · Important · §7.** The go/no-go is decided by a committee that includes the vendor's delivery lead, on "the vendor's pilot evaluation". The vendor grades its own pilot and votes on its own rollout. Fixed when the agency (or an independent party) prepares or validates the evaluation, and the vendor does not vote. Also consider adding the Data Protection Officer and a caseworker.
- **F-20 · Minor · §6.** "No case data is exported to the vendor" is true for fine-tuning, but the vendor-hosted platform still reads individual records, receives uploaded medical certificates and holds the conversation logs. Fixed when §6 describes this runtime data flow (what, where, how long) and ties it to the DPIA and the §8 clauses.

### Score, with the same rubric
| Criterion | v1 | v2 | What moved it |
|---|---|---|---|
| Consistency | 2 | 3 | F-04, F-07, F-17 and F-18 fixed; R-01 to R-03 keep it from going higher |
| Evidence | 2 | 2 | F-15 and F-16 unmoved |
| Obligations | 1 | 4 | F-02 and F-03 fixed, F-01 partly; no appeal route and no audit rights or SLA yet |
| People affected | 1 | 3 | F-05 and F-12 fixed; F-06 partly, F-13 open |
| Feasibility and full cost | 1 | 3 | F-04 and F-07 fixed; F-08 and R-03 mean no multi-year cost |
| Measures and risk | 2 | 3 | F-09 fixed; F-10, F-11 and F-14 partly |

Open findings: 2 Critical, 9 Important, 3 Minor (was 6 / 9 / 3).

### Still to do before the Board
1. **F-01 (Critical):** add how a citizen contests a decision, with the role and deadline. Consider a sample audit of automatic approvals.
2. **F-06 (Critical):** define the handoff from the chat to a person on web and WhatsApp, with the staffing for it.
3. **R-02:** move the evaluation to the month-11 go/no-go and the post-rollout phases.
4. **F-08 and R-03:** add a three-year cost table with recurring costs, review costs and a real source of savings, or remove the "pays for itself" claim.
5. **F-11 and F-19:** write the go/no-go criteria (accuracy, resolution time, escalations, complaints) and take the vendor out of the vote.
6. **F-10, F-14:** add an escalation or abandonment measure. Add risks for wrong decisions, exclusion and vendor dependency, each with an owner.
7. **F-13:** set an accessibility requirement and an alternative to text chat, checked before the pilot.
8. **F-15, F-16, R-01, F-20:** derive the target by procedure (or commit to deriving it from the pilot), source the baselines, fix the tax item and describe the runtime data flow.

The updated ledger is attached (`review-ledger.md`). Keep it in the project as `review-ledger.md`, or paste it next to v3. Same rubric and anchors, so v3 will be comparable.
