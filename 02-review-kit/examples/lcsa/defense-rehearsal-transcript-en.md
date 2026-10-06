# defense-rehearsal — demo transcript

> Simulated: the presenter is an AI agent playing the head of the Digital Transformation Office (fictional LCSA). The panel is Claude Sonnet running the defense-rehearsal skill.

**User:** defense-rehearsal: I present the ATLAS plan (v2, attached) to the Executive Board next month. Let's rehearse.

**Claude:** Here is the setup. You are presenting ATLAS v2 to the LCSA Executive Board, which will decide whether to approve the plan and the USD 730,000 year-1 budget. Your panel:

- **Finance Director:** guards the money. Worried about what the Board is really committing to over three years, and whether the numbers behind the savings hold up.
- **Risk and Legal Counsel:** answers for rules, oversight and data. Worried about what happens when the system is wrong, who is accountable, and what the agency is exposed to.
- **Head of Citizen Operations:** speaks for the call center, the offices and the citizens who use them. Worried about whether this works for real people and real staff on the ground.

Three quick settings, all optional:
1. **Length:** default is 8 questions, about 15 minutes.
2. **Tone:** supportive, realistic or tough. Default is realistic.
3. **Feedback:** a short note after each answer, or only at the end. Default is only at the end.

Reply with your choices, or just say "go" and I'll use the defaults. Answer as you would in the room, and write "pause", "skip", "hint" or "end" at any point if you need them.

**User:** Defaults are fine, let's go.

**Claude:** Defaults it is: 8 questions, realistic tone, my full assessment at the end. We begin.

**Question 1 of 8**

**Finance Director:** Section 10 gives me a year-1 budget of USD 730,000, and section 10 also says the program runs for three years and the contract term is three years. The plan doesn't say what years 2 and 3 cost. What is the total three-year cost the Board is committing to, and what is in it?

**User:** That's a fair point, and I'll be straight with you: the plan only gives the year-1 figure, and I don't have a Board-ready three-year total to put in front of you today. What I can say is how it breaks down. The platform license, the 420,000, is the recurring piece, while integration, the impact assessment and security testing, and most of the training and campaign spend are largely one-off in year 1. But the real license price comes out of the procurement, and I don't want to quote a multiplied number that the tender could change. I'd rather come back to the Board with a three-year cost model, including run costs, before you vote on the full commitment.

**Claude:** **Finance Director:** I appreciate the candor, but the vote is next month, not after the tender. Two things the plan doesn't say. Where does the 420,000 license figure come from, if the price only comes out of procurement, and does it cover a full twelve months when the system won't exist until month 5 and the pilot only starts in month 8? And if you can't give me a number, what ceiling are you asking the Board to approve for years 2 and 3?

**User:** The 420,000 is an estimate we built from the framework agreement's indicative price list, so it's a planning figure, not a quote. As for the twelve months, you're right to push: the platform won't be live until month 8, so on paper we're budgeting a full year of license for roughly the pilot period, and I can't tell you today how much of that the vendor would actually bill in year 1. That could leave some room in year 1, but I wouldn't count on it until the tender is in. On a ceiling for years 2 and 3, I don't have one I can defend yet, so what I'd propose is that the Board approves year 1 only, and that years 2 and 3 are released after the month 11 go/no-go, against a costed three-year model that I bring back.

**Claude:** **Question 2 of 8**

**Risk and Legal Counsel:** The change summary on page one says "Eligibility decisions are now reviewed by a caseworker." Section 5 says something narrower: approvals for the housing subsidy and the disability fee waiver are issued automatically within minutes, and a caseworker only reviews cases where the rules point to a denial. Which is it? And when ATLAS approves someone who turns out not to be eligible, who is accountable for that decision, and where in the plan would the agency ever find out?

**User:** You're right, the summary line on page one overstates it, and section 5 is the accurate description: approvals go out automatically, and a caseworker only sees the cases where the rules point to a denial. I should have worded the change note that way, and I'll fix it. On accountability, formally the agency issues the decision, so it sits with the director of the service that owns those two procedures, but I'll be honest that the plan doesn't spell out that line of responsibility. And on how we'd find out about a wrong approval, the monthly accuracy review samples conversations, not approval decisions, so today the plan has no real check on that. What I'd want to add is a regular caseworker audit of a sample of automatic approvals, but that's a proposal, not something that's in the plan yet.

**Claude:** **Risk and Legal Counsel:** Thank you, that is a clear answer on the gap. But an audit that isn't in the plan doesn't help me vote. The housing subsidy is a benefit people will start relying on within minutes. Suppose the audit finds that ATLAS wrongly approved a share of cases. What error rate would you consider acceptable, what happens to a citizen who has already received a wrongly approved subsidy, and what would make you switch off automatic approvals?

**User:** Fair, and I don't have a number for you that I could defend. The 95% in the plan is an accuracy target for answers in conversations, and for a subsidy decision that's clearly not the right standard; the acceptable rate there should be far lower, but I'd want the Data Protection Officer and your office to help me set it rather than pick it in this room. On the citizen who was wrongly approved, that's really a legal question for you: my instinct is that someone who acted in good faith on an agency decision shouldn't be left worse off, but I can't tell you what the law allows us to do about recovering the benefit. As for switching off, I'd expect us to be able to route those two procedures back to caseworkers quickly, and I'd want that as a condition for the pilot, but I need to confirm with the vendor and the integration team that it's a simple switch and not a change request.

**Claude:** **Question 3 of 8**

**Head of Citizen Operations:** Let me turn to the people at my counters. Section 5 says ATLAS will handle the fee waiver for people with disabilities, and section 7 says it launches as a text-only chat, in the national language only, with the vendor's standard design. Walk me through how a citizen who is blind, who has an intellectual disability, or who doesn't speak the national language well actually gets through that procedure. And for anyone without a smartphone or WhatsApp, what changes for them?

**User:** Honestly, that's thin in the plan and I won't pretend otherwise. The one thing I can stand behind is that the call center and all 14 offices keep their current hours throughout, so nobody is forced onto ATLAS and a person who can't use the chat still has the counter and the phone. But I can't tell you today whether the vendor's standard interface works with screen readers, and a text-only chat in one language clearly isn't enough for someone with an intellectual disability or someone who doesn't speak the national language well. I'd need to ask the vendor for their accessibility conformance information and test it with disability organizations before the pilot, and I'd want your staff involved in that. For people without a smartphone, nothing changes for now, they keep using the channels they use today, though I realize that means the benefits of ATLAS reach them last.

**Claude:** **Head of Citizen Operations:** Keeping the counters open is good, but you've just told me the main users of the fee waiver are the people the chat serves worst. Section 8 lists the contract terms you will require, and accessibility isn't among them. Will it be? And if the vendor can't show accessible access by the pilot, do you keep the disability fee waiver in ATLAS's scope or take it out?

**User:** Yes, it should be, and I'll add accessibility to the contract requirements in section 8, with the vendor's conformance to a recognized accessibility standard as a condition, not a nice-to-have. I'd need legal and procurement to tell me how to word it in the framework agreement, so I won't promise the exact clause today. On the fee waiver, my answer is that if the vendor can't show accessible access by the pilot, that procedure shouldn't go live through ATLAS for those citizens. What I can't settle alone is the consequence, because the housing subsidy and the fee waiver are 38% of the backlog and most of our time savings, so taking the waiver out would hurt the case for the 4-day target, and I'd rather tell the Board that now than hide it.

**Claude:** **Question 4 of 8**

**Finance Director:** Section 10 closes with "From year 2, ATLAS is expected to pay for itself, as efficiency gains in the call center and the offices cover the platform." I can't find a single savings figure behind that sentence. And section 9 says the call center and all 14 offices keep their current hours throughout. Where does the claim come from, and which actual cost line goes down, by how much, and when?

**User:** The logic comes from the volumes: we handle about 1.2 million contacts a year and roughly 70% of them are repetitive, so if ATLAS takes a meaningful share of those, the call center and the offices free up a lot of capacity. And I'd say the value of this project isn't only in cutting a budget line; faster resolution, fewer missed calls at peak and staff working on the complex cases are real returns for the agency too. The pay-for-itself sentence is the expectation of the team, and we'll firm it up with the pilot data, because that's when we'll see how many contacts ATLAS really resolves. I wouldn't want to commit to a line item and a date before we have that.

**Claude:** **Finance Director:** Freed capacity is not a saving unless someone spends less. You've said the counters keep their hours, and I don't see a headcount or overtime change anywhere in the plan. Your three success measures in section 3 are resolution time, accuracy and satisfaction, and none of them measures cost or the share of contacts ATLAS resolves. So should the Board read this as a service investment that needs about USD 420,000 a year of ongoing budget, rather than something that pays for itself? If not, what is the mechanism, in one sentence?

**User:** I think that's a fairer reading than my sentence in section 10, so I'll say it plainly: until we have pilot data, the Board should treat this as a service investment. If there is a mechanism for savings, it's that the call center and offices absorb demand with what they have, so we avoid overtime and backfilling vacancies, rather than cutting posts, but I can't put a number on that today and I won't pretend the plan does. You're also right about the measures, and I'd add the share of contacts ATLAS resolves without a person and a cost per resolved request to section 3, so the month 11 evaluation can show whether the cost side is real. I'd then rewrite that sentence to say the case for self-funding will be assessed at that point.

**Claude:** **Question 5 of 8**

**Risk and Legal Counsel:** Section 6 says "no case data is exported to the vendor," and section 5 says ATLAS runs on the cloud provider selected in the procurement. Yet to check a housing subsidy, ATLAS has to read the citizen's record, including medical certificates for the fee waiver, and the language model has to process that content to produce an answer. Walk me through where that record physically goes when ATLAS reads it, who can see it there, and where the pseudonymized conversation logs are stored.

**User:** Let me be precise, because the wording matters. The records stay in the case management system, and ATLAS only reads the single record of the citizen who has identified themselves, through the existing API; there's no bulk copy, no extract and no training set. Uploaded documents, medical certificates included, go straight into the case management system, so the language model isn't a storage place for them. When the model processes a record to answer, that happens in the provider's environment, and section 8 is what governs it: data centers in the country, the agency owns all data, no use of our data or interactions to train or improve their products, and at exit everything is returned and certified as deleted within 30 days. The conversation logs are pseudonymized and sit under those same terms. Who exactly at the vendor can technically access them, and the retention period for the logs, are things I expect the security design and the data protection impact assessment to pin down before the pilot, and I'm happy to bring you that.

**Claude:** **Question 6 of 8**

**Head of Citizen Operations:** Let's talk about the pilot, because that's where my staff will live it. Section 9 runs the pilot in two districts in months 8 to 10, and section 3 promises an average of 7 working days in those districts by month 11. Today the average is 11 working days. The plan doesn't say which two districts, why those, or what their baseline is. How do you measure a drop to 7 days from a pilot that lasts three months, when many requests started in month 10 won't have closed by the evaluation? And what do you show the Board if the pilot districts come out at 9?

**User:** The districts aren't chosen yet, and I'd pick them with your operations team, ideally one busier and one smaller so we don't test only the easy case. On measurement, the case management system gives us resolution times for in-scope procedures, so I'd compare the pilot districts against their own baseline and against districts that aren't in the pilot over the same months. You're right that requests opened late in the pilot won't have closed, so we'd report on requests that were opened early enough to be resolved by month 11 and show the still-open ones separately, rather than flatter the average. If we come out at 9, the steering committee decides with the data in front of it, and I'd rather present a 9 honestly, with what's driving it, than stretch the pilot to hit 7. I'll admit the plan doesn't set go/no-go thresholds, and I'd bring those to the committee before the pilot starts.

**Claude:** **Question 7 of 8**

**Finance Director:** You told me the 420,000 comes from the framework agreement's indicative price list. Section 8 then says the contract will not use the vendor's standard terms: in-country hosting, no use of our data to improve their models, and certified deletion at exit. Those are exactly the terms that tend to cost more or that some vendors refuse. What evidence do you have that a vendor under the framework will accept them at or near that price, and what happens to the four-month procurement and to the budget if none does?

**User:** I don't have written evidence that a vendor will accept those terms at that price, and I'd be misleading you if I said I did. What I'd say is that in-country hosting and a no-training clause are not unusual requests for a public body, and the framework agreement exists precisely so we can tailor terms, so I'm cautiously confident we'll get bidders. But whether the price holds is a different matter, and the 420,000 should be read as a planning figure that could move once vendors price those clauses. If nobody bids, the plan has no fallback today: the four months would stretch, the pilot would slip with it, and I'd have to return to the Board with a revised timeline and budget rather than loosen the data terms. I'd propose a quick market sounding with the framework's suppliers before the call for offers, so we know where we stand.

**Claude:** **Question 8 of 8**

**Risk and Legal Counsel:** My last question is about who decides. Section 7 says the steering committee that takes the go/no-go decision on the rollout is chaired by the project director and includes the vendor's delivery lead, and that it reviews the vendor's own pilot evaluation. So the vendor helps judge its own pilot. Who on that committee can stop the rollout, and what would a "no-go" look like in practice, given that the contract has already been signed for three years?

**User:** I'd defend the design: the vendor's delivery lead is there because they know what the system did and didn't do in the pilot, and the head of the call center is on the same committee, so the people who live with the results are in the room and can challenge the vendor's numbers. The project director chairs it and is accountable to the Board for the go/no-go, and the committee's decision is a recommendation the Board can overrule. That said, I take your point that the vendor shouldn't be the one writing the evaluation it's judged on, so I'd have the agency's own team produce the evaluation from our case management data, and the vendor would contribute but not vote. In practice a no-go means we don't extend beyond the two pilot districts, we route the procedures back to staff, and we pay for the license until we work out the way out. I'd need procurement and legal to tell me what the contract's termination terms allow, because section 8 only covers data return and deletion at exit.

**Claude:** That was the last question. I'm stepping out of role now.

### Likely outcome: Approve with conditions

If the Board votes on the document as it stands, a Defer is a real possibility. What keeps it at "approve with conditions" is that you offered, unprompted, the narrowing the panel wants: approve year 1 only.

- **Finance Director:** Approves year 1 only, with years 2 and 3 released after the month 11 evaluation against a costed three-year model. Would change to Defer if the "pays for itself" sentence stays; would firm up with a market sounding on the 420,000 and a clear license billing start date.
- **Risk and Legal Counsel:** Approves only if automatic approvals have a named accountable owner, a sample audit with a set error threshold, and a tested way to route both procedures back to caseworkers. Would move to Defer if the DPIA still comes after the contract award, and would be reassured by an agency-written pilot evaluation with the vendor non-voting.
- **Head of Citizen Operations:** Supports the pilot if the districts are chosen with operations, accessibility is a contract requirement, and the fee waiver does not go live through ATLAS until accessible access is shown. Would turn against it if the pilot is judged only on the 7-day average.

### How you answered

| # | Member | Question (short) | Answer | Why |
|---|---|---|---|---|
| 1 | Finance | Three-year total cost | adequate | Honest and a sound proposal (approve year 1, release the rest later), but no figure, and the basis of the 420,000 and its 12-month coverage came only under pressure. |
| 2 | Risk and Legal | Page-1 claim vs section 5; accountability for wrong approvals | weak | You conceded the inconsistency cleanly, but after a follow-up there was still no accountable owner in the plan, no error threshold, no legal answer on a wrongly granted subsidy, and an unconfirmed switch-off. |
| 3 | Operations | Access for blind, disabled, non-national-language and offline citizens | adequate | Candid and the counters-stay-open point is real; after the follow-up you committed to an accessibility requirement and named the 38% trade-off honestly. The clause and the fallback for the fee waiver are still open. |
| 4 | Finance | "Pays for itself" from year 2 | adequate | First answer reframed instead of answering; after the follow-up you gave the right reading (service investment), a plausible mechanism, and better measures. No numbers behind any of it. |
| 5 | Risk and Legal | Where the record goes; where logs live | adequate | Clear on the architecture and on what section 8 covers, and the processing-in-provider's-environment point corrects the "no export" wording. Vendor access and log retention were deferred. |
| 6 | Operations | Measuring 7 days in a 3-month pilot | strong | Concrete method (own baseline, non-pilot comparison, only requests opened early enough, open ones shown separately), an honest answer on a result of 9, and you named the missing thresholds. |
| 7 | Finance | Will vendors accept the section 8 terms at that price | adequate | Honest that there is no evidence, and a sensible fallback (return to the Board, don't loosen data terms) plus a market sounding. "Cautiously confident" has nothing behind it yet. |
| 8 | Risk and Legal | Vendor on the committee that judges its pilot | adequate | You defended the design, then conceded the key point and fixed it (agency writes the evaluation, vendor non-voting). The no-go consequences depend on termination terms you haven't seen. |

### Prepare these three answers

**1. Question 1 and 4: "What is the total cost the Board is committing to, and does it pay for itself?"**
Missing: any figure beyond year 1, and any cost-side evidence.
- Year 1 is USD 730,000: 420,000 license (a planning figure from the framework's indicative price list, not a quote) and 310,000 of mostly one-off items.
- Years 2 and 3: state as an assumption, clearly labeled, that the license alone is about 420,000 a year if the price held (about 1.26 million over three years), and that run costs beyond the license are not yet estimated. Say what you will bring and when: a costed three-year model before the month 11 go/no-go.
- Ask for what you can defend: approve year 1 only, release years 2 and 3 after month 11.
- Position it as a service investment. The self-funding case will be tested at month 11 with two new measures. Missing fact: current overtime and backfill spend, which is the only saving mechanism you named.

**2. Question 2: "ATLAS approves someone who isn't eligible. Who answers for it, and how do we find out?"**
Missing: a named owner, an error threshold, a recovery rule, a tested stop.
- Open with the correction: approvals are automatic, denials are reviewed by a caseworker; the page-1 line was wrong.
- Name the accountable role (the director of the service that owns the two procedures) and put it in section 7.
- Commit to a caseworker audit of a sample of automatic approvals each month, with the acceptable error rate set with the DPO and Legal before the pilot (the 95% answer-accuracy target is not that standard).
- Make "route both procedures back to caseworkers" a pilot condition, confirmed with the vendor. Missing fact: the legal position on recovering a wrongly granted benefit. Say who you will ask and by when.

**3. Question 7 and 8: "What if the contract terms don't survive procurement, and what does a no-go really cost?"**
Missing: market evidence and termination terms.
- State the dependency plainly: in-country hosting, no training on agency data and certified deletion are non-negotiable; price and timeline are what can move.
- If no vendor bids, you return to the Board with a revised timeline and budget rather than loosen the data terms.
- Propose a market sounding with the framework's suppliers before the call for offers.
- On a no-go: no extension beyond the pilot districts, procedures return to staff, the agency writes the evaluation and the vendor does not vote. Missing fact: what the contract allows on early termination and what you would still owe. Section 8 only covers data return and deletion.

### Change the document

1. **Changes box and section 5.** Replace "Eligibility decisions are now reviewed by a caseworker" with: "Approvals for the housing subsidy and the disability fee waiver are issued automatically. A caseworker reviews every case where the rules point to a denial and audits a monthly sample of approvals. The accountable owner is the Director of [service]. The acceptable error rate and the audit sample size will be set with the DPO and Legal before the pilot. ATLAS can be switched off for these two procedures and the cases routed back to caseworkers."
2. **Section 10.** Replace the last paragraph with: "Year 1 costs USD 730,000. Years 2 and 3 are not yet costed. The Board is asked to approve year 1 only. Release of years 2 and 3 depends on the month 11 evaluation and a costed three-year model, including license, run and support costs. Whether ATLAS pays for itself will be assessed at that evaluation." Add one line stating that the 420,000 is a planning figure from the framework's indicative price list and when license billing starts.
3. **Section 3.** Add two measures: "share of contacts resolved without a person" and "cost per resolved request"; add "accuracy of automatic approvals (audited sample)". Add: "Pilot go/no-go thresholds will be fixed before the pilot starts. The 7-day result counts requests opened early enough to be resolved by month 11, with open requests reported separately."
4. **Section 7.** Change the committee: "The Digital Transformation Office produces the pilot evaluation from case management data. The vendor's delivery lead contributes and does not vote." Add three rows to the risk table: wrong automatic approval; no bidder accepts the section 8 terms (fallback: revised timeline and budget); inaccessible interface for people with disabilities.
5. **Sections 7 and 8.** Add to the contract requirements: "vendor conformance to a recognized accessibility standard" and the early-termination terms. Add: "The disability fee waiver will not go live through ATLAS until accessible access is demonstrated." Section 6: add where the model processes records, who at the vendor can access them, and the retention period for conversation logs.

### Questions we didn't get to

1. **Risk and Legal Counsel:** The DPIA and legal basis come in months 5 to 7, after the award in month 4 and a three-year contract. What happens if the DPIA concludes the processing can't go ahead as designed?
2. **Finance Director / Operations:** Where does the "70% of inquiries are repetitive" figure come from, and what share of those is in the 12 procedures? The plan also says the housing subsidy and fee waiver are 38% of the backlog. How was that measured?
3. **Head of Citizen Operations:** Every denial goes to a caseworker within five working days, and the plan budgets USD 25,000 for staff training without saying how many people that covers. How many caseworker hours does that review take, and does it fit the 4-day target?

