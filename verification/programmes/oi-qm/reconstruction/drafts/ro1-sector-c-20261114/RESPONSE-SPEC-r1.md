# Response to the independent review of RO1-SPEC-r1

**UNREVIEWED.** These are the writer's dispositions of `REVIEW-SPEC-r1.md`: REVISE at `7156d761`,
file SHA-256 `d7f4380d…a4341`, with three blocking, seven major and twelve minor findings. They also
cover two additions relayed by the coordinator from ChatGPT. The changes are in `RO1-SPEC-r2.md`.
`RO1-SPEC-r1.md` is left unchanged (SHA-256
`d7f4380d2c2786a30f68b2d1776f5212ca11750192778e2fed3e2bde7e6a4341`).

Each finding was checked at source before it was applied. Reading only: no computation, no Lean, no
edit, no post. No finding was found to be wrong. Where the check refined a finding, the row says so.
Line numbers in the first column are r1's.

## Blocking

| Finding | Check at source | Disposition | Where in r2 |
|---|---|---|---|
| **B1.** §7.2's "REFUTED" is unsupported, and contradicts K-acc and §8 | **Confirmed.** SEL-EXCL-1 at `0ecfddeb`: "This interface is **specified, not derived from the native OI/SM dynamics**" (l. 46); "interface itself UNSOURCED" (l. 129); the menu restriction is "**assumed** rather than OI-derived" (l. 150). In the map `T(x,y,r,A,B) = (x,y,r, A⊕r, B⊕r⊕(x∧y))` (SEL-DISC-1 l. 63), `x, y` are unchanged, so `T` executes no setting program. r1 ll. 322 and 328–329 assumed what is open. r1 §8 (ll. 354–355) applies only to a complete C, yet r1 l. 386 applied it to the frame. The classical control was not shown green (r1 ll. 303–305) | **Applied.** "REFUTED" and "cannot yet be sound" are removed. §7 is now a conditional check, not a verdict (§7.1). K-acc is "Open" for the PR model, and the control is UNSOURCED (§7.2). The conclusion is stated conditionally: *if* the single-use test is in `Γ`. The check states its assumptions: class reading (S6), tuple reading (S1). The single-use test's own setting actuation is listed as an availability question (§5.1, first row). §8 step 3 now requires the classical control to be exhibited before it is green | Outcome; §§5.1, 7.1, 7.2, 8 steps 2–3; §10 S3 |
| **B2.** Soundness has no structure-preserving correspondence | **Confirmed.** As r1 wrote it (ll. 280–284), soundness asks only that a law "equals that of some finite quantum experiment". A single quantum device that takes `(x, y)` jointly and reads out a classical register realizes any finite conditional table, PR's included. The sources assume a structured comparison: SEL-EXCL-1 l. 81, "the corresponding bipartite dichotomic Bell scenario"; SEL-DISC-1 D7, local instruments and one classical bit (ll. 129, 190); SEL-ACCESS-1 §1 item 4 | **Applied.** §6.3 defines a correspondence `Θ`, as [P]. It maps wings to separate subsystems with local instruments, composition to composites, sequence and adaptivity to conditioned instruments, and messages to classical channels with the same alphabet, budget and schedule. It also maps records to records and exogenous settings to exogenous settings. `Θ` constrains the comparison class and is not a clause of C. Its adoption is a new owner stop, S8. Coverage now uses the same `Θ`. The claims resting on soundness are re-derived against `Θ`: §7.2's three consequences and §8 steps 5–7 | §§6.3, 7.2, 8; §10 S8 |
| **B3.** The "five kinds" K-X table is unsupported | **Confirmed.** J2 was absent although r1 l. 187 recorded it as untested. Main:78: (C4) is met by "a pre-sampled hidden variable revealed by the history … (the response-table construction, §3.4)". The OI⁺ principles and their primitive-source and substratum-source forms are at Main:584–588. r1 l. 174's ban is stricter than #914 c.6875046763 decision 4 ("Allowed as a conditional mathematical input, not a physical explanation"). Candidate E: SEL-ACCESS-1 l. 81. H-Bell's clauses (Substratum:133) are (i) parameter dependence, (ii) no-signalling and (iii) a metric/Ollivier–Ricci stability condition. The PR model has (i) and (ii). **Refinement:** (iii) is a continuum-geometry condition that no source applies to PR, so "H-Bell does not exclude PR" holds *as stated*, not as a theorem | **Applied.** §7.4 is relabelled [A-inf], over a search stated by file and line. Rows are added for (C1)–(C4) (untested), for OI⁺ and its two refinements (with their posited inputs from Main:588), and for candidate E (untested; support outside the repository). The H-Bell row now reads "No, as stated", with the refinement. The ban is withdrawn and becomes owner stop S9. The outcome paragraph and S2 are restated to match | §§3 (last paragraph), 7.4; Outcome; §10 S2, S9 |

## Major

| Finding | Check at source | Disposition | Where in r2 |
|---|---|---|---|
| **M1.** (C1)–(C4) excluded silently (r1 ll. 98–99) | Confirmed: the sentence read as an exclusion | **Applied.** The sentence is now explicitly notation only. (C1)–(C4) are a candidate ground (J2) and a candidate for K-X (§7.4) | §2.1 |
| **M2.** Typing settled without a stop; J7's §A.29 judgement not shown | Confirmed. r1 l. 160 folded E into `φ`; Main:588 adds "one operation … as an empirical controllability resource", which is not a change of `φ`. K-acc derived `Γ` from `(φ, Obs)`, while SEL-DISC-1 l. 34 lists `Γ` as a component. Owner item 1: "The shared model-identity and typing questions remain open" | **Applied.** New stop S7 covers both typing choices. J7's judgement now reads "§A.29 judgement: not met", with three reasons: (a) preservation of the controls not shown; (b) no independent prediction; (c) open to adjustment until S3. K-acc is marked as not yet applicable | §§2.1, 3 (K-dyn, K-acc), 4 (J7); §10 S7 |
| **M3.** LEDGER and r3 cited as results on `main` | Confirmed. LEDGER is on the records branch at `9ff3b8d9`, not on `main`; its README reads "UNREVIEWED — NOT AUTHORITATIVE". r1 l. 97 labelled a statement about r3 "[R, main]" | **Applied.** `main` lines are cited directly where they exist: Main:724 for posits (ii), (iii) and (xiv); Main:362–389 for J4. LEDGER and r3 are cited as *off-main records* with their review states, in a new block of §9, which states the §A.42 gap for them. The negative claims that rested on LEDGER are now [A-inf] over what was read, or [R, off-main record] (A-QM UO). "No mechanism is stated in the corpus" is removed; §7.4's stated search replaces it | §§2.1, 3, 4, 6.3, 9 |
| **M4.** J1's C0 control is not supported at the cited commit | Confirmed. SEL-ACCESS-1 points to pages outside the repository (l. 26) and lists C0 as "not adopted as main-established evidence" (l. 123). SEL-DISC-1 l. 30 says the original review artifacts were not recovered | **Applied.** The C0 citation is dropped. It is replaced by the swap and visible-flip classical control, which SEL-ACCESS-1 proves in the file (§2, ll. 53–69). Candidate E is marked *outside the repository*, and the gap is recorded in §9 | §§4 (J1), 7.4, 9 |
| **M5.** K-X defined by its control outcomes | Confirmed: r1 l. 166 defined K-X by what it excludes and keeps | **Applied.** K-X is now "a physically justified clause, stated first with its ground". PR exclusion, 2√2 and the classical fragment are tests it must pass under §8. In §7.3 the named restriction `R*` keeps (a)–(b) as the tests it must pass and (c) as §6.1 | §§3, 7.3 |
| **M6.** S-J reading too narrow; depends on S6 | Confirmed. The Bell part of #914 c.6875548603 was omitted, and K-acc holds by definition | **Applied.** §4 states both readings, tied to S6, includes the Bell part as K-X's ground, and records that K-acc explains nothing | §4 |
| **M7.** O11 narrowed without a stop | Confirmed (r1 ll. 138–142) | **Applied.** The menu constraint is moved under S1 as a proposal for the owner, with its effect stated | §2.3; §10 S1 |

## Minor

| Finding | Disposition | Where in r2 |
|---|---|---|
| **m1.** §5 heading not labelled "proposed" | **Applied.** | §5 heading |
| **m2.** §5.1 omits continuations; "Inside C?" should be "In `Γ`?" | **Applied.** Checked at SEL-EXCL-1 ll. 91, 97 and SEL-DISC-1 l. 71. Added rows: the single-use test's setting actuation; a probe of `r` or of an unused cell; arbitrary choice of source index; a unilateral stop or ready request. The column is renamed "In `Γ`?" | §5.1 |
| **m3.** S-A5 against a bank pre-prepared in `μ` | **Applied.** S-A5 and K-res now count cells prepared in `μ` at the start or renewed later. SEL-EXCL-1 l. 87 prepares the bank as "one common source law" | §§3 (K-res), 5 |
| **m4.** Finiteness hypotheses | **Applied.** Checked at Main:758 ("bounded coupling, finiteness of `S`, the canonical-typicality result [31], and … (EM)"), Main:362 ("`V` and each `S_i` finite") and Main:366–376 (hypotheses (i)–(iv)). J3 and J4 now carry them. J3 notes the conflict with a non-finite `S`. K-dyn states its departure from posit (ii) (Main:724) | §§3, 4 |
| **m5.** K-dyn's status overstated | **Applied.** Checked: Main:42 gives `φ: S → S`. Bijectivity is posit (iii), "part-empirical rather than a pure lemma" (Main:724). K-dyn is now [P], adopting posits | §3 |
| **m6.** S4 not needed to state C | **Applied.** K-obs quantifies over each observer. S4 is withdrawn, and ledger Q1 is moved to coverage as a dependency | §§3, 6.3; §10 |
| **m7.** O4 is scientific, not an owner decision; r3 question 6 not carried forward | **Applied.** S2 now names O4 as scientific, homed at #1143. Conditional variants, one per route, are proposed for the next revision | §7.3; §10 S2 |
| **m8.** Labels at r1 ll. 112, 338 and 146 | **Applied.** The alternative reading is now [P]. §7.4 is [A-inf] over a stated search. "One record law has many realizations" is now [A-inf], citing Main:598 | §§2.2, 2.3, 7.4 |
| **m9.** O12 attribution | **Applied.** r2 says the renaming to `Res` goes beyond r3's convention, which is to name the objects in full, and serves the same purpose | §2.1 |
| **m10.** Coverage maps a family to one program | **Applied.** Coverage now maps every experiment of every family | §6.3 |
| **m11.** "clauses the corpus can support today" includes new proposals | **Applied.** The outcome paragraph no longer says this. It says five clauses are met as stated and K-acc is open | Outcome |
| **m12.** The measurement-dependent row does not exclude PR and bears on Q8 | **Applied.** Checked at Main:416–423: the bound min{4, …} allows 4. The row now reads "No" and points to S5 | §7.4 |

## Additions relayed by the coordinator

| Addition | Disposition | Where in r2 |
|---|---|---|
| Test the PR countermodel against each clause, with the closure rules, and name the exact missing restriction without choosing between H-Bell and IC₂ | **Applied.** §7.2 gives a clause-by-clause table: K-dyn, K-obs and K-src are met; K-rec and K-res are met given its programs; K-acc is open. The closure consequences are given for the single-use test, same-seed reuse and the one-bit message. §7.3 names `R*` by conditions (a)–(c). It records that `R*` cannot be pointwise parameter independence, because that gives CHSH ≤ 2 under K-src and determinism (Main:364–389). The route is stop S2 | §§7.2, 7.3 |
| No repair of C by quantum-set membership; any new restriction needs §A.29 justification, else a stop | **Applied.** §6.1 states both rules, and §1 quotes owner item 1 ("introduce a premise merely to reproduce quantum predictions") | §§1, 6.1 |
| Under O11, can physically equivalent descriptions get different membership decisions under each candidate relation? | **Applied.** It takes the corpus's own equivalent representatives (relabelling, decoupled enlargement and alphabet change; Main:724 item (ii)). Answer: yes under (i), with agreement expected for relabelling but unproved; yes in general under (ii), by M-1/Q2A and the failure of G ⇒ O for C2-ch and C2-sel; no under (iii) for record-equivalent descriptions, though K-dyn may then fail invariance (Main:598) | §2.3 |

## Stops after r2

- **Kept:** S1, S2, S3, S5 and S6.
- **New:** S7 (typing), S8 (`Θ`) and S9 (quantum kinematics in clauses).
- **Withdrawn:** S4 (m6).
