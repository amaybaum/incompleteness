# Response to the independent review of S3-PLAN-r1

**UNREVIEWED.** These are the writer's dispositions of `REVIEW-S3-PLAN-r1.md` (REVISE at `38b5a460`).
The changes are in `S3-PLAN-r2.md`. `S3-PLAN-r1.md` is left unchanged (SHA-256
`582cb1413f683bfbabda523eaaa49707020f0629b6b3f55ce31037e9d6c19ac4`).

Each finding was checked at source before it was applied. No finding was found to be wrong.

Unchanged:
- the plan is paper-only, with no new premise;
- no authorization changes for #866 or #913;
- C-1 stays under #1234, and X1–X5 stay open;
- the owner's confirmed requirements A, B1–B3 and C still apply.

## Major findings

| Finding | Check at source | Disposition | Where in r2 |
|---|---|---|---|
| **F1(a).** Condition (a) holds by definition; the observer-level lift is open | **Confirmed.** *Available* is "a composition of native steps" (MR-1 preregistration §1), and P-L3 makes each step a bijection. Main:588: "the site-space wave-operator formulation being unresolved rather than excluded". SM:224: "at either the substratum-symbolic level or an observer-level linear lift" | **Applied.** Point 1 now says that the configuration-level conclusion holds by definition together with P-L3, so it is not a finding, and that it does not reach the observer-level lift or the σ12 rules. A new check (§8.4, check 3) records the lift route as open, with its home at track (a), OB-a1. The closure conditions no longer contain the definitional condition (a). They require (b′), the lift shown to give no non-monomial admissible operator, which can fail | §§8.3, 8.4, 8.6 |
| **F1(b).** Condition (c) is false: classical interference returns natively | **Confirmed.** S-L1 gives native additive-field interference on K1. CC5 and AW-MR5 reproduce returned interference without any class-(ii) import | **Applied.** Restated as (e′): class-(i) interference that a generalized-noncontextual model reproduces supplies no quantum coherent operation, and only interference beyond such models (MR-1's W1) needs class (ii) or an unavailable U or P. Point 1 notes that (b) has a class-(i) form | §§8.3, 8.6 |
| **F1(c).** A decisive test is missing | **Confirmed.** S-L5: "A record (R1) never causes (ii): marking is non-invasive" (`amendments/MR-star.md`:584–594). Observed which-path complementarity is a raw-direct observable (§A.24) | **Applied.** D-1 is now U4's first check, as a candidate class-(iii) confrontation conditional on three identifications: (α) the K1 reading (P-vii global, so it depends on C-1); (β) MR-1's marker is a which-path detector; (γ) additive-field interference corresponds to the observed detection statistics. Both outcomes are stated: a raw-direct miss for the K1 reading, or route M empty on K1. Owner question 6 asks where to report the first outcome | §8.4, check 1; §8.6 (a′); §10 question 6 |
| **F1(d).** The GAP's scope and caveats are not carried | **Confirmed.** `K★ = {K1}`, σ1–σ13, a budget below recurrence (#1023 c.6555169983). σ12: "outside `K★ = {K1}` … not screened for R or Q here"; "These are the rules on which conditional dynamics, and so pointers and settings, are not excluded" (`MR-star.md`:667, :680). The caveats are quoted in c.6555169983 | **Applied.** The scope and both caveats are carried in §8.6. σ12 becomes check 2, indexed by the reading of P-vii (C-1; X2), with screening routed to #866 | §§8.1, 8.4, 8.6 |
| **F1, overall.** The route must stay open; copy and full process kept apart | Confirmed | **Applied.** §8.6 opens with "Route M stays open, conditional and unclosed until a decisive test runs", and states that U4 alone cannot close route M negatively. §8.4 keeps a configuration-level copy apart from the full measurement process (preparation, accessible outcome, retained record, possible uncomputation) | §§8.4, 8.6 |
| **F2.** The negative controls need construction | **Confirmed.** Full specification of M-1 to M-3 is construction, and is the content of MR-1's controls-only stage 2 (README), which is not authorized | **Applied.** §8.5 now separates two groups. The controls fully specified on record and usable without construction are M-7 (the PR model with complete records) and a new M-8 (PC-1's screened rules, "classical measurable bijections with function-valued records", #866 c.6627392555). M-1 to M-3 are specified at class level in MR-1 and executed only under an MR-1 stage-2 authorization. The U4 deliverable "specified completely" is removed, and the full specification of M-1 to M-3 is listed as a stop | §§8.2, 8.4 check 7, 8.5, 9 |
| **F3.** U2 and U3 overlap other work | **Confirmed.** #866 c.6863601327 classifies (i)–(iv) as "derived / assumed / absent". #913's gates are the work loci of #914 O-INS (c.6628909432) | **Applied.** §2.3 adds #914 O-INS and the Codex screen, with a demarcation. U1 is a definition for RO-1 only. U2 is narrowed to RO-1's own control programs, reads the Codex screen's result for native candidates, and waits on owner question 4. U3 is narrowed to definitions and requirements for RO-1, routed to #913 and #914 without discharging them. The dependencies are stated in §9 | §§2.3, 4, 9, 10 |

## Medium findings

| Finding | Check at source | Disposition | Where in r2 |
|---|---|---|---|
| **F4.** The setting criterion builds in measurement independence | Confirmed. Preregistration §5.6: "Setting independence is decided as a property of `μ` … never assumed"; AW-MR7 | **Applied.** The independence clause is dropped. Independence is recorded as a property each record must decide, conditional on S5 | §3 |
| **F5.** The access declaration is a free choice | Confirmed. S-L7 (`MR-star.md`:603–618): "Which slices the access reads is not fixed by the sources". SM:252 is now Lemma 1c, so S-L7's citation has drifted | **Applied.** U1 freezes the access declaration, with its source re-pinned, before classification. K-2 now covers the access | §§3, 6, 9 |
| **F6.** AW-MR8 quoted in superseded wording | Confirmed (`MR-star.md`:1401–1412, C-6) | **Applied.** The rescoped C-6 text is quoted, and the withdrawal of the substratum-level reading is noted | §8.1 |
| **F7.** Route-M tiers applied to U1–U3 | Confirmed | **Applied.** The tiers are stated as route M's only. U1–U3 show their output type, with "tiers not applicable". U4 keeps its tier | §9 |

## Minor findings

| Finding | Disposition | Where in r2 |
|---|---|---|
| **F8.** Setting-dependent offsets | **Applied.** An additive offset that depends on the setting is recorded as a setting-dependent output, not as a setting-selected intervention. Quoted: "Setting-dependent outputs remain possible as offsets" (#1023 c.6555169983); the setting "selects no operation" (S-C1(a)) | §3 |
| **F9.** Labels on Point 1's premises | **Applied.** P-L3 is marked a premise, and the diagonal-preservation lemma a paper proof on `main`. The conclusion is stated as exact at configuration level and scoped per F1(a) | §8.3 |
