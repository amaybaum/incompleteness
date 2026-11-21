# A1-EXIT Step 2, unit S2-B (R6 corrections): result

**Status.** Writer's record of a manuscript correction unit, not yet independently reviewed. Draft PR
[#1473](https://github.com/amaybaum/incompleteness/pull/1473), branch `research/a1exit-s2b-20261121`.
Authorization: owner `amaybaum`, 2026-11-21,
[#1169 comment 7056875845](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7056875845).
Goal link (§A.47): the A1-exit objective (#1169); this unit decides whether the R6 §7 sites can be made
true without A1. Not merged; no workflow dispatched.

**Base and commits.** Base `main` at `1c7eedc40`. `PREREG.md` at `3541e2ea3` (pushed before any
manuscript edit); manuscript edits, rebuilt artifacts and coverage ledger at `6c31a9c5f`; this file
after it.

## 1. Outcome

All 28 preregistered edits applied verbatim (32 file sites; the edit script checks each old string is
unique in each file before replacing it). Every R6 §7 item in scope is made true without A1 as a proved
weaker condition:

| R6 item | Ledger row | Form after the edit |
|---|---|---|
| #1, #2, #3, #4 (CP), #5, #6, #18 | X-50 | CP-indivisibility apparatus on a measurable hidden carrier (R6 Theorem 6, INF); its P witness under (NR), printed as a hypothesis assumed and not adopted, with the return qualification (WEAK). The finite Lemma states its diagonal prior |
| #4 (physical memory), #7, #8 | X-51 | Both §3.4 theorems on any measurable hidden space with any reference probability, (M1) in integrated form (R6 Theorem 7, INF) |
| #10, #11, #12, #13, #14, #15, #19 | X-53 | Decoupled factors of any cardinality in normalized states or laws, unitary or isometric (classical: measurable) dynamics (R6 T9(a), (b), (d), INF); unnormalizable factors and coupled deep sectors outside |

**X-50 criterion 3.** Edit E2 (Main:336) prints the ledger's queued wording for X-50 verbatim: "(NR),
assumed as a hypothesis of this result and not adopted; (NR) concerns a time that need not be accessible
and then has no finite-window test; for the selected update on ℤ^d the only laws known to satisfy it
are supported on periodic configurations". This discharges X-50's criterion-3 item; S2-C skips it.

**Main item (ii).** Only the list inside it changed (E5a, E5b, E6a, E6b). Item (ii), its identifier and
its pointers are unchanged; A1 is not deleted.

**Not claimed.** No Koopman constant-vector form (R6 T6-K (α), refuted); nothing for Koopman (β) on
diffuse carriers or (γ). (RIG) is not printed: Main names (NR), one of R6's two sufficient conditions.
T9(c) (ρ-preserving relabelling, item #17) is not applied.

## 2. Edits as applied (ledger sites with new line numbers)

Old and new strings are in `PREREG.md`; the applied text is identical to them.

| Edit | R6 item | Row | Site at base | Site after |
|---|---|---|---|---|
| E1a | #1 | X-50 | M:328 | M:328 |
| E1b | #1 | X-50 | M:330 | M:330 |
| E2 | #2 | X-50 | M:334 (insertion after) | M:336 (Corollary), M:338 (proof) |
| E3 | #3 | X-50 | M:60 | M:60 |
| E4 | #10 | X-53 | M:60 | M:60 |
| E5a | #4 | X-50 | M:732 | M:736 |
| E5b | #4 | X-50, X-51 | M:732 | M:736 |
| E6a | #11 | X-53 | M:732 | M:736 |
| E6b | #11 | X-53 | M:732 | M:736 |
| E7 | #5 | X-50 | M:742 | M:746 |
| E8a | #7 | X-51 | M:459 | M:463 |
| E8b | #7 | X-51 | M:467 | M:471 |
| E8c | #7 | X-51 | M:469 | M:473 |
| E9a | #8 | X-51 | M:473 | M:477 |
| E9b | #8 | X-51 | M:473 | M:477 |
| E10 | #18 | X-50 | M:336 | M:340 |
| E11a | #6 | X-50 | AppB:92, FULL:5769 | AppB:92, FULL:5769 |
| E11b | #6 | X-50 | AppB:94, FULL:5771 | AppB:94, FULL:5771 |
| E12a | #12 | X-53 | Sub:257 | Sub:257 |
| E12b | #12 | X-53 | Sub:262 | Sub:262 |
| E12c | #12 | X-53 | Sub:266 | Sub:266 |
| E12d | #12 (consequence) | X-53 | Sub:249 | Sub:249 |
| E13a | #13 | X-53 | Sub:268 | Sub:268 |
| E13b | #13 | X-53 | Sub:268 | Sub:268 |
| E14 | #14 | X-53 | Sub:92 | Sub:92 |
| E15a | #15 | X-53 | ch02:144, FULL:774 | ch02:144, FULL:774 |
| E15b | #15 | X-53 | ch02:144, FULL:774 | ch02:144, FULL:774 |
| E16 | #19 | X-53 | Str:53 | Str:53 |

Main lines after M:334 move by +4 (the inserted Corollary and proof, two paragraphs). Units editing Main
below line 334 (S2-C at :766, S2-D in §4.6) should expect that offset when they merge.

## 3. Propagation (§A.25, §A.14)

Mirror pairs edited together: AppB:92/94 ↔ FULL:5769/5771; ch02:144 ↔ FULL:774. Str:53 restates
Theorem 24(iii) (E16). No book mirror exists for Main §3.2's Lemma and Corollary, the §3.4 theorems,
M:60 or M:732 (grep of "diagonal preservation", "permutation-dilation", "reference prior defining",
"H_k = h", "uniform-prior bijection marginal": hits only in Main and in AppB/FULL Lemma B.2.2, which is
the reverse-direction lemma and is unaffected).

R6 §11 item 9 grep over `papers/*.md` and `book/*.md` ("CP-indivisib", "physical-memory", "physical
memory", "finite factor", "finite decoupled", "decoupled finite", "Infinite extensions", "Infinite
factors"): 75 file-line-term hits at the base, 63 after. Removed: FULL:774 and ch02:144 "Infinite
factors"; M:60 "finite factor"; M:732 "finite decoupled", "finite factor", "physical-memory"; Str:53
"finite factor"; Sub:257 "finite factor"; Sub:268 "Infinite extensions", "finite decoupled"; Sub:92
"Infinite extensions", "finite decoupled". Every survivor, with its reason:

| Hits | Reason |
|---|---|
| Sub:50, Sub:60, Sub:201; Str:154; Meth:467; Complexity:206; ch02:28, ch02:134; ch03:80, ch03:142; ch04:172; appendix-c:106; FULL:658, 764, 941, 1003, 1276, 6261 ("finite decoupled"/"decoupled finite") | R6 #16 (O): true as written; skipped by owner decision |
| ch02:44, FULL:674 ("Infinite extensions", "finite factor") | R6 #20 (O): true as written; skipped |
| ch03:220, FULL:1081 ("finite factor") | R6 #21 (O): true as written; skipped |
| ch02:144, FULL:774 ("finite factor") | Substring of E15b's "an infinite factor under uniform counting", the excluded unnormalizable case |
| M:60 ("CP-indivisib") | E3's own text: the CP theorem uses the finite representative only through its P witness |
| M:736 ("CP-indivisib") | E5a's own text: (NR) named for the CP theorem's P-indivisibility input |
| M:332, M:342; AppB:12, AppB:96; FULL:5689, FULL:5773 ("CP-indivisib") | The finite theorem (true as stated), the ancilla-witness paragraph and the Appendix B overview: no finiteness clause |
| AppB:92, FULL:5769 ("CP-indivisib") | E11a's own theorem, generalized |
| M:746 ("CP-indivisib") | E7's own row |
| Intro:111 ("CP-indivisib") | R6 §7: already states the diagonal premise ("definite probabilities") |
| M:74, 97, 169, 182, 467, 477, 486, 506, 546, 640, 668, 748; Sub:129, Sub:137; SM:1380; glossary:27, 39 = FULL:6518, 6530 ("physical-memory"/"physical memory") | Citations of the theorem, or the theorem itself (M:477), with no finiteness clause (R6 §7 "sites checked and needing no change", line numbers shifted) |
| GR:565, 641, 705; ch07:20 = FULL:1885 ("physical memory-bearing application") | Different phrase ("memory-bearing"), not the theorem |
| Medicine:49 ("physical memory register") | Different subject (enzyme phosphorylation) |

Observation, not edited (outside scope, no A1 content): M:74 and M:748 paraphrase the coupling-step model
as "next visible state determined by the current visible and hidden states"; the model's kernel
`K(x_k, h; ·)` need not be deterministic, before and after this unit. Recorded for the ledger
reconciliation.

## 4. Build and coverage

`sh ./build.sh Main Substratum Structure`: `build: OK`; `sh ./build.sh --book`: `build: OK`; no
dropped glyphs reported.

| Artifact | Pages (base → after) | Median characters per page (base → after) |
|---|---|---|
| papers/Main.pdf | 106 → 108 | 3338 → 3313 |
| papers/Substratum.pdf | 53 → 54 | 3240 → 3236 |
| papers/Structure.pdf | 94 → 94 | 2908 → 2908 |
| book FULL.pdf | 489 → 489 | 2998 → 2990 |

`python3 tools/coverage_check.py` before the ledger update: FAIL (4 stale fingerprints:
MAIN:L-diagonal-preservation, MAIN:T-c2-necessity-quantitative-mixing-form,
MAIN:T-physical-memory-c2-process-form, SUBSTRATUM:C-effective-finiteness-gauge-class-transfer).
Each was re-read and re-affirmed in `verification/coverage/LEDGER.json`: fingerprints updated; the
`assumptions` fields of the first three updated to the statements' hypotheses; levels unchanged. The
diagonal-preservation entry stays K3 with empty delta: its Lean statement already takes the hidden prior
as `Matrix.diagonal mu`, which the Lemma states. The two §3.4 entries stay P (the probe covers finite
instances; the measurable form is a paper proof, R6 Theorem 7). After: `coverage_check: OK (132
canonical statements, 20 unattached checkers)`. The new Corollary is italic-headed, like the near-return
corollary of §2.3, and is not a census statement.

Other local checks (§A.40): `lean_manuscript_census.py` OK; `artifact_placement_check.py` OK;
`legacy_records_check.py 6c31a9c5f…` self-test OK, verdict UNDECIDABLE (shallow local repository;
decided in CI); `py_compile tools/*.py` OK.

**Register scan (§A.32, §A.33)** of every added string: no hits for "now", "no longer", "corrected",
"formerly", "withdrawn", "should not be read", "the reader"; capitals of four or more letters: CPTP
only (acronym).

## 5. Deviations from PREREG

None in the applied text. E12d (Sub:249 preamble, "finite normalized-product form" → "normalized
Hilbert-space product form") is not in R6 §7's site list; it was preregistered as a necessary
consequence of #12, since the preamble otherwise describes the coherent form of (iii) as finite only.

## 6. Off-`main` references (§A.42 item 8)

| Reference | Attached claim | Classification |
|---|---|---|
| #1169 comment 7056875845 | authorization | provenance (owner record) |
| #1169, #1473 | planning, tracking | provenance |
| `3541e2ea3` | that PREREG preceded the manuscript edits | support: depends on commit order; on `main` only if this PR lands by a merge commit keeping it reachable |

Every manuscript statement edited here rests on R6 (`verification/audits/foundations/a1exit-r6-20261120/`,
on `main`) and on proofs printed in the edited text itself. No support off `main`.

## 7. Verification status (§A.46 item 4)

- **Evidence level.** The new and generalized statements are paper derivations ([W], R6, reviewed on
  PR #1467), reproduced in Main's own proofs (Corollary, Lemma converse, §3.4 proof edits) and Substratum's
  Theorem 24(iii) proof. Not kernel-checked; the finite Lemma remains K3.
- **Missing verification.** Independent non-author review of this unit's text, in particular: E2's
  statement and proof against R6 Theorem 6; E1b's construction against R6 Prop. 6.9; E8 and E9 against
  R6 Theorem 7 (the role of (M0) and (M1)); E12–E16 against R6 T9.
- **Accountable Issue.** #1169 (A1-exit).
- **Resolution.** A review recorded on PR #1473, then an owner merge decision.

## 8. Round 1 (review of `91e1052d3`, REVISE; answered by amendment A1)

The review confirmed the mathematics and raised B1, B2 and nits N1–N6. The coordinator's instructions
were to fix B1, B2, N1, N2, N3 and N6, skip N4 and N5, and align the return form with S2-C (#1474).
Amendment `amendments/A1-round1.md` was pushed at `7f2e94c8e` before any edit. Its edits were applied
verbatim at `00b1ca1a6`.

| Item | Edit | Site after | Answer |
|---|---|---|---|
| B1 | R1 | M:224 | The measurable-carrier corollary of §3.2 and the two coupling-step theorems of §3.4 join the list of results that take a measurable hidden space |
| B2 | R2a, R2b | Sub:262, Sub:266 | Theorem 24(iii)'s classical sentence states the hidden-prior channel family identity of [Main §3.2], with its proof line (R6 T9(b)). This supports Main item (ii) (E6a), which is kept as written |
| B2 | R2c | Sub:268 | Corollary (iii): for a classical factor, the channel family read as the hidden-prior family |
| B2 | R2d | ch02:144, FULL:774 | Mirror of R2a. Str:53 does not restate the classical case and is unchanged |
| N1 | R3 | M:60 | "because the product dynamics factorizes and the added state or law keeps total mass one" |
| N2 | R4 | M:336 | F measurable for 2^{C_V} ⊗ 𝓗 |
| N3 | R5 | M:336 | "If some Γ_s with s ≥ 1 is not a permutation matrix … with r = n, under (NR) of that corollary" |
| S2-C alignment | R5 | M:336 | "for the selected update of §3.2 on ℤ^d …" |
| S2-C alignment | R6 | AppB:92, FULL:5769 | Full return form, both clauses, "of Main §3.2" |
| N6 | — | LEDGER.json | Both §3.4 entries: delta "no Lean statement; measurable form: paper proof only" |
| N4 | — | — | Skipped (acceptable per the review) |
| N5 | — | — | Out of scope. M:74, M:748 and glossary:27 paraphrase the coupling step as deterministic; this predates the PR and carries no A1 content (see §3) |

**Effects on the X-50 criterion-3 wording.** It stays printed at M:336, with "of §3.2" added, which is
S2-C's form. **Possible overlap:** R1 edits the final clause of M:224, inside S2-C's range
(:131–:224), as the coordinator assigned. A merge conflict at that line is possible.

**Grep (R6 §11 item 9).** 63 → 64 hits: R1 adds a "physical-memory" citation at M:224. It has no
finiteness clause.

**Build and coverage.** Main has 108 pages, median 3322 characters per page. Substratum has 54 pages,
median 3230. The book has 489 pages, median 2991. No dropped glyphs. `coverage_check` reported one
stale fingerprint, SUBSTRATUM:C-effective-finiteness-gauge-class-transfer (R2c); it was re-affirmed,
level GAP unchanged, and the check then reported `OK (132 canonical statements, 20 unattached checkers)`.

**Deviation.** The amendment's preamble says "Ten manuscript edits". The amendment actually
preregisters nine edits (R1, R2a–R2d, R3, R4, R5, R6) at 11 file sites. The edits themselves are as
preregistered.
