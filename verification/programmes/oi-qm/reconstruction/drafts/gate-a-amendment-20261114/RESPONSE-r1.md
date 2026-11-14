# Response to REVIEW-r1.md

Dispositions of the findings in `REVIEW-r1.md` on `GATE-A-AMEND-r1.md`. `r2:n` is line n of
`GATE-A-AMEND-r2.md`; `TR` is `GATE-A-AMEND-r2-TRACE.md`; `EP:n` is line n of `endpoints.md`, blob
`d9d92e038a8022e854586101067ce4de9789fdf6` on `main` at `c3b5f37a`. r1 is unchanged.

I checked every finding at its source before applying it. I read again: EP in full; on `main`,
`whole-model-bridge.md`:236–249, `composition-source-map.md`:90, `two-system-interface.md`:187 and
:325–327, `observer-access-20261106/ASSESSMENT.md`:284–286 and
`states-dynamics-audit-20261024/REPORT.md`:75; `papers/Main.md`:558, :580, :588 and :600 by grep for
the quoted phrases; `OIBridge/StructuralClosure.lean`:346–430 and `OIBridge/TypedCompletion.lean`:848–852;
`TARGET-THEOREM-r3.md`:34 (off `main`). Through the public API: #1169 c.6763928950 (`amaybaum`,
2026-11-10T09:34:24Z), the #1143 body (updated 2026-11-13T20:07:02Z) and the #1169 body. Every
quotation the review gives from these sources matched. The review's header says fourteen should-fix
findings, but its table lists sixteen (F1–F16); all sixteen are answered below.

| ID | Disposition | Where in r2 | Check and reason |
| --- | --- | --- | --- |
| B1 | applied, extended | r2:75–78 (residual clause); r2:84–119 (§3.1, rows added and amended); TR §1 (every nonblank EP line) | Confirmed: in r1, EP:110 and EP:21–29 were untraced, the listed clauses of EP:40, 43, 45, 47, 75–77, 79, 92, 104, 112, 164, 172 and 177 were dropped, and there was no residual clause. All the review's rows and amendments are applied; row "79–88" is split into 79 and 81–88. TR §1 assigns each of the 113 nonblank lines exactly one disposition (kept, record, superseded, partly superseded). One addition beyond the review: EP:51 ("The primary proposed model-level target is:") is marked partly superseded, since the target it introduces is now r2 §5 (r2:142–144). |
| F1 | applied | r2:19–28; r2:121–129 (§3.2) | Confirmed: the r1 quotation came from the target-theorem sentence that c.6875548603 replaces. The c.6875548603 list of standing requirements, the c.6875046763 sentences and the c.6703342848 clarification match the API text. Exactness and the Bell track are added as a §3.2 row as well, since c.6875548603 lists them. |
| F2 | applied, modified | r2:80–82 | Confirmed: r1's "applies to every part" contradicts r1's §5.3. The review's text is applied, and B is added to the list of parts outside `J_exact(A)` because F12 makes Bell its own obligation. |
| F3 | applied | r2:146–151 | Confirmed: the two lists in r1 differed. The review's text is used, with B added (F12). r2 §6.1 repeats the same list. |
| F4 | applied | r2:159–167; TR §2 | All eight added quotations were checked at source and match. The fourteen-row table is in TR §2 to keep r2 short; r2 summarizes it, says the list comes from a search, and names #1143 with the PROGRAMME paragraph. |
| F5 | applied | r2:195–199; r2:356–358 (R7) | Confirmed: I ranges over `J_exact(A)`, which excludes changes of system type (EP:41, EP:110) and has no wing structure. The remainder is named as open and untyped, so the contract is not widened. |
| F6 | applied | r2:180–185 | Confirmed that r1's I-2 allowed declared but fitted T-dependence. The review's text is used verbatim. |
| F7 | applied | r2:186–189 | Confirmed against "physically sourced" (#1169 c.6875724719, item 1) and "Physical source remains **NOT PASSED**". |
| F8 | applied, modified | r2:203–212 (type table); r2:228–230 (C-4); r2:360–365 (§8) | Confirmed that the type of C cannot be fixed from the records: "experiment families" (#914 c.6875548603) against "OI models outside C" (#1169 c.6875724719), and #1143 lists further filter targets. As F8 says, "or physical regimes" is deleted from C-4. Modification: the owner question lists three options with what each commits to. The regime option is kept only when it is stated as a law-level or model-level predicate, and a regime that restricts the procedures compared becomes a named restricted target under EP:43. |
| F9 | applied | r2:215–222 | Confirmed: in r1, C-1 did not exclude a C defined by I's construction or with later-fixed parameters. The review's text is used verbatim. |
| F10 | applied | r2:231–232 | Confirmed: in r1, admissibility depended on the open target. The review's text is used. |
| F11 | applied | r2:237–259 | All four defects were confirmed. The review's text for S⇒, S⇐ and S⇐ᴺ is used, and I checked its two logical claims by hand. First, with I, S⇐ᴺ implies S⇐: the I witness is quantum, so C holds of it. Second, for a C that is a function of the history law, S⇐ implies S⇐ᴺ: any M′ ≡ T has the same law as the S⇐ witness. One added sentence states that necessity is a distinct question only if C depends on data beyond the history law. |
| F12 | applied, modified | r2:223–225 (C-2); r2:261–278 (S-J and B) | Confirmed: S-J combined three kinds of obligation, and C-2 repeated the confinement clause. S-J now states confinement alone and B has two directions, as the review asks. Modification: B⇐ and B⇒ are stated for instances of 𝔄 that satisfy C and are typed for `J_Bell`, rather than for "members of `M_C(E, A)`". `M_C(E, A)` is a subclass of `M(E, J_exact(A))`, which is defined over `J_exact(A)`, while `J_Bell` is a separate interface. |
| F13 | applied | r2:324–330 | Confirmed: the owner question is the type of C. The review's text is used verbatim. |
| R2 addition | applied | r2:331–339 | The two owner-record quotations and `TARGET-THEOREM-r3.md`:34 were checked. The single-model reading is recorded as an owner question (r2 §8, item 3). |
| F14 | applied | r2:345–351 | Confirmed: in `whole-model-bridge.md`, lines 238–240 give the narrower scope, and 247–248 the retained-subinterface clause. |
| F15 | applied | r2:307–308 | Confirmed at source: "proved in exact arithmetic … the bound on the realized law is open" (Main:600, item 4), "check 13, `opglue_probes.py`" (Main:580), and "The factorization interface assumed is the ordinary preparation $\to$ finite ontic system $\to$ measurement one" (Main:558). The numerical-probe qualifier for :580 is added. |
| F16 | applied | r2:310–311, r2:316, and a row for #1143 | Confirmed: `substratumGen_not_control` :348, `substratum_plus_control_qm` :414, `fullClass_extendsSubstratum` :419–420 (`fun _ _ _ _ _ => trivial`), `qm_generated_by_substratum_extension` :423 (witness `fullClass`), `typed_determined_iff` :850, and "an empirical controllability resource" (Main:588). The typed-form row says the statement was read through its location, docstring and the manuscript only. |
| N1 | applied | r2:285 | "the regime of the sector" is replaced by "the scope of C". |
| N2 | applied | r2:49–51 | The review's sentence is added. |
| N3 | resolved | r2:252–259, r2:324–330 | "strictly stronger" no longer appears unqualified. |
| N4 | applied | r2 §3.1 | Under B1. |

No finding is declined.

## What was not checked

- The #1143 body and #1169 c.6763928950 were read only around the quoted passages.
- `typed_determined_iff` was read only through its docstring and opening lines. Its full statement and hypotheses were not read.
- The review's further reading was not repeated, namely `prepared-pair-source.md`, `composition-source-map.md`:18, :87–91, :168, and `two-system-interface.md`:183–188, :322–330 beyond the quoted lines.
- r2 is 376 lines, somewhat over the 360-line guide. The long tables were moved to TR; what remains is the §3.1 trace of kept requirements and the §6.2 status table, which the authorization and the deliverable require in the amendment itself.

## Confirmation review (CONFIRM-r2.md)

Dispositions of the changes in `CONFIRM-r2.md` on r2. `r3:n` is line n of `GATE-A-AMEND-r3.md`;
`TR3` is `GATE-A-AMEND-r3-TRACE.md`. r2 and its trace are unchanged. Each change was checked at its
source first. Main:427 ("Removing the screened local-intervention restrictions admits the
unrestricted OI behavior class, including the PR negative control"), Main:580 ("all steps
injective, laws exact"), EP:75 ("the candidate's stated admissible preparation procedures") and
#1169 c.6703342848 (owner approval "after the explanation that … “We do not need the hidden
machinery itself to be quantum.”"; "Deterministic hidden dynamics … are admissible" is the
comment's own sentence) all match.

| ID | Disposition | Where in r3 | Check and reason |
| --- | --- | --- | --- |
| K1 | applied | r3:248–260 (S-A); r3:265–268; r3:364–368 (R5); r3:388–394 (§8 item 4); S-A added to the obligation lists at r3:82, r3:154, r3:236, r3:279, r3:307 and r3:399, and to TR3 row 170 | Confirmed. S⇒ and S⇐ compare only the label-interpreted protocols of `J_exact(A)` (EP:43, EP:47). No line of EP constrains what a member's other admissible procedures produce: EP:102 requires that every protocol of J be realized, and EP:104 treats missing procedures, not extra ones. The PR-type class is on record (Main:427). The reviewer's texts are used verbatim. One sentence is added to S-A pointing to owner question 4. Three further propagations: C-5 names S-A (r3:235–236); §4.2's sector form reads "S⇒ and S-A" (r3:166–167); TR3 §2's introduction matches. Item 4 of §8 also records the c.6703342848 passages bearing on the question. |
| K2 | applied, modified | r3:283–298 | Confirmed: "satisfies C" was undefined on `J_Bell`, B⇒ named no class, and B⇐ was not tied to S⇐. The reviewer's text is used, except for B⇐'s quantifier. It reads "for every T in `Q_exact(A₁ × A₂)` there exists an S⇐ witness M for T … reproduces exactly T's law for every quantum two-wing protocol and preparation", where the review had "there exists an M meeting S⇐". S⇐ is quantified per T, so "an M meeting S⇐" is not well typed, and the witness must match a given T. |
| K3 | applied | r3:208–209, r3:213, r3:215 | The reviewer's texts are used. The type sentence also states that the admissible types are C-law and C-model. |
| K4 | applied | r3:375–387 | The reviewer's items 1–3 are used verbatim. |
| K5 | applied | r3:145–148; TR3 row 51 | The reviewer's text is used. TR3 row 51 states the same disposition; no other disposition changed. Rows 69 and 112 refer to "the amendment" instead of "r2". |
| N1 | applied | r3:53, r3:131 | This corrects the attribution introduced in r2 under REVIEW-r1 F1. |
| N2 | applied | TR3 §3, row for Main:596/:580 | It now reads "is checked computationally (:580, check 13, `opglue_probes.py`)". This corrects the F15 row above, which called it a numerical probe. |
| N3 | applied | r3:163 | It now reads "Fourteen entries". |
| N4 | applied | r3:325–332; TR3 §3 | The §6.2 status table is moved to TR3 §3 unchanged except for N2 and the added S-A in the Bell row. r3 keeps a summary of the statuses. r3 is 406 lines; the obligations were not shortened. |

No change is declined.
