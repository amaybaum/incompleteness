# A1-SCOPE Phase 2 — companion papers and book mirrors: dispositions, edit ledger, controls and decision rule

**Amended once (§12), after the independent review of `3b5c937c`. Where §12 differs from an earlier section, §12
governs.**

**Status.** Writer's paper-only preregistration (stage 1 of 2). It fixes, before any manuscript edit, which
companion and book sentences change, their exact text, and the mechanical tests the edit must pass.

- **Not done here:** no edit under `papers/` or `book/`, no Lean, no registry change, no new premise, no merge.
- **Status of A1:** A1 (Main posit ledger item (ii)) remains open and unadopted. Physical measurement sourcing
  remains not passed. No splice adopts a premise; each new label use is "assumed … not adopted".
- **Stage 2 is not authorized by this record.** Applying the ledger needs an independent non-author review of this
  record and a separate owner decision, as for Phase 0 → Phase 1.

**Authorization.** Owner `amaybaum`,
[#1169 comment 7033018172](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7033018172),
2026-11-20T07:12:08Z, "Owner decision record: expanded workstreams": "A1-PHASE2 | paper-only | #1443 merged, so the
prerequisite is met. Same controlled minimal-edit method for the companion papers and book mirrors." The scope is
[#1169 comment 7032429839](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7032429839)
(2026-11-20T06:37:08Z): "Apply the Phase 0/1 method to the companion papers (SM, Substratum, GR, Structure) and their
book mirrors … Include O-A4's SM:222/242, SM:539 and SM:240 findings and its Stage-2 classifications. GR:58 counting
stays conditional (R1)", with decision rule "Every companion consumer states A1 or an explicit sufficient condition;
all controls pass." The same record: "None of these authorizes adopting a new physical assumption."

**Goal link (§A.47).** Item served: #1055 (A1 programme), which serves #1169. What the work decides: for each companion
and book consumer of total finiteness, whether its sentence states A1 or an explicit sufficient condition with the
condition carried into its conclusion, and the exact minimal text where it does not.

**Source pin.** `main` at `b9168ef0408b5f55b935a4df17cb0841877e221a` (merge of #1443, Phase 1).

- Between the Phase 0 pin `d5735bed` and this pin, `papers/SM.md`, `Substratum.md`, `GR.md`, `Structure.md` and the
  in-scope chapters are unchanged (`git diff --stat d5735bed b9168ef0 -- papers book` lists only Main, ch00, ch01,
  appendix-b, appendix-c, glossary, FULL and their generated files). Phase 0 line numbers therefore hold for every
  in-scope paper and chapter. `glossary.md` changed at line 11 only, in place.
- FULL line numbers moved in Phase 1 (corollary insertion in ch01). Phase 2 keys each FULL mirror by its chapter line's
  exact text (the CENSUS §7 recipe), not by the Phase 0 FULL line number.

## 1. Inputs and findings

### 1.1 Inputs (all on `main` at the pin; cited, not re-derived)

| Short name | Path under `verification/audits/foundations/` | Used for |
|---|---|---|
| P0 | `a1-scope-phase0-20261120/PREREG.md`, `sites.json`, `phase0_controls.py` | site map (P2 and OA4 rows), §3.2 companion targets, CTL-1–13 |
| P1 | `a1-scope-phase0-20261120/phase1_ledger.json`; `papers/Main.md` at the pin | Main's (NR) corollary (§2.3), item (ii) wording, (IL), (IP), (REV) |
| O-A4 | `o-a4-20261120/RESULT.md` (#1441, merged after ACCEPT WITH NITS) | step table rows 1–26, §5–§9a, markers W1–W3 |
| REMAINDER | `a1-remainder-20261119/REMAINDER.md` | rows C1–C14, residues R1–R6, §5 (O-INFLOW) |
| FCLASS, ROOTS, NEC, CENSUS | `a1-finiteness-classes-20261117/`, `a1-main-roots-20261118/`, `a1-necessity-20261117/`, `a1-09-dependency-census/` | row keys inherited through `sites.json`; not reclassified |
| P7B | `p7-boundary-count-20261116/P7-BOUNDARY-COUNT.md` | C1/C2 (GR:58, GR:88): stays conditional |

No row of these audits is reclassified. Each site keeps the Phase 0 class and rows.

### 1.2 Findings recorded by this unit

| Id | Finding | Evidence at the pin | Consequence |
|---|---|---|---|
| P2-F1 | Substratum's (A1) declaration carries no status, while Main item (ii) and the book mirror ch02:76 state "open hypothesis, not adopted". The book leads the paper (§A.25 step 2). | Sub:92; ch02:76; Main §4.5 item (ii) | Unit B1 |
| P2-F2 | SM Lemma 1c(ii) is proved by a determinant factorization (SM:254), a finite-dimensional argument, while its statement names no finiteness and (iii) applies it to the translation-invariant realization on ℤ^d. | SM:252–254; O-A4 row 11, §6.1 | Units S7, S8 (narrowed to the proved scope) |
| P2-F3 | Companion sentences restating the P-indivisibility route name only total finiteness, while Main §2.3 now proves the conclusion under (NR) for a hidden space of any cardinality. | SM:44, GR:138, GR:589, Sub:92; Main §2.3 Corollary (near-return), M:724 | Units S1, G1, G2, B1 (additive) |
| P2-F4 | O-A4 §7: the printed finite class of A4 (Sub:98) admits period lattices on which Stage 2 inputs fail (no `O_h` action on skew quotients; no checkerboard on odd tori; fewer than eight corners unless Λ ⊂ 2ℤ³). Only SM:539 is a named finding of the scope; the A4 clause itself is open question Q1. | O-A4 §7.1–§7.2, checks D–E | Unit S6; Q1 |
| P2-F5 | SM:222 declares the carrier Λ = ℤ^d and calls the bijection finite; Theorem 1a assumes S finite (O-A4 §9a). | SM:222, SM:242 | Unit S3 (finite reading stated with A1, A4); Q2 |
| P2-F6 | The CTL-14 scan is lexical. Its condition-token list (§5) can excuse a sentence whose condition word attaches to another clause, and it reads only site lines. | §5 | Reviewer item 4 (§9) |

## 2. Scope

**In scope.** `papers/SM.md`, `papers/Substratum.md`, `papers/GR.md`, `papers/Structure.md`; their book mirrors
`book/ch02-substratum.md`, `ch03-structural-realism.md`, `ch04-methodology.md`, `ch05-gauge-structure.md`,
`ch07-gravity.md`, `ch09-universality.md`, `glossary.md` (the chapters holding Phase 0 P2/OA4 sites keyed to rows of
these four papers); and `book/The-Incompleteness-of-Observation-FULL.md` for every chapter line in scope.

**Sites.** Every Phase 0 site with phase P2 or OA4 in those files, and the FULL line equal to each in-scope chapter
site: 214 sites (122 paper, 46 chapter, 46 FULL).

**Out of scope (recorded, open question Q3).** 77 Phase 0 P2 sites in `papers/Methodology.md` (13),
`Computation.md` (4), `Introduction.md` (2), `Complexity.md` (1), `Medicine.md` (1), `book/ch14-quantum-computing.md`
(5), `book/ch18-beyond.md` (23) and their FULL mirrors (28). They key to Main rows (M1, M10, M13), to C12
(Computation) or to FCLASS U1, not to the four companion papers.

## 3. Dispositions (delta 1)

### 3.1 Method

Each in-scope site receives one disposition in [`dispositions.json`](dispositions.json): `edit` (with the ledger
units that change its line) or `N` (no edit, with the reason). The test applied to each site sentence:

- **(E-a)** It asserts finiteness of `S`, the substratum, the total carrier or the fundamental bijection in the
  framework's own voice, with no condition (A1, a finite representative or model, a named hypothesis, or a theorem's
  stated hypothesis) in the sentence → `edit`, inserting the condition.
- **(E-b)** It restates the P-indivisibility route with total finiteness as its only stated condition, where Main §2.3
  (Phase 1) proves the conclusion under the weaker (NR) → `edit`, additive: the existing sentence is kept and the
  weaker sufficient condition is added, "assumed … not adopted".
- **(E-c)** It is a named O-A4 finding whose statement exceeds its proof or its declared carrier (SM:222, SM:539,
  Lemma 1c(ii)) → `edit`, narrowing to the proved scope or stating the condition.
- **(E-d)** It is an INFLOW site → names the inflow question as open, with its own support (P0 §3.2 row C10).
- Otherwise → `N`. A sentence that already states A1 ("finite under A1", "under the open hypothesis A1", "A1–A6"),
  a finite representative, a finite model or a named hypothesis is not edited (minimum necessary change, §A.25).

### 3.2 Counts

| File | Sites | edit | N | Splices |
|---|---|---|---|---|
| `papers/SM.md` | 26 | 7 | 19 | 8 (S1–S8; S8 is the proof line of S7) |
| `papers/Substratum.md` | 30 | 4 | 26 | 4 (B1–B4) |
| `papers/GR.md` | 15 | 2 | 13 | 2 (G1, G2) |
| `papers/Structure.md` | 51 | 2 | 49 | 2 (T1, T2) |
| `book/ch02-substratum.md` | 17 | 2 | 15 | 2 (K1, K2) |
| `book/ch03-structural-realism.md` | 8 | 0 | 8 | 0 |
| `book/ch04-methodology.md` | 3 | 0 | 3 | 0 |
| `book/ch05-gauge-structure.md` | 9 | 2 | 7 | 2 (K3, K4) |
| `book/ch07-gravity.md` | 2 | 0 | 2 | 0 |
| `book/ch09-universality.md` | 6 | 1 | 5 | 1 (K5) |
| `book/glossary.md` | 1 | 0 | 1 | 0 |
| FULL (mirrors of the above) | 46 | 5 | 41 | 5 (K1–K5-FULL) |
| **Total** | **214** | **25** | **189** | **26** |

### 3.3 O-A4 classifications as applied

| O-A4 row / section | Manuscript site | Phase 2 action |
|---|---|---|
| 1, §7 (A4's finite quotient; `O_h` and parity conditions on Λ) | Sub:98, ch02:82, SM:202, ch05:65 | N; the A4 clause states its class. The period-lattice conditions are Q1 |
| 4–5 (dimension; SM:210 reads verbatim on ℤ^d) | Sub:157, SM:202, SM:210, ch05:65–77 | N (conditional on A4 as printed) |
| 9, §9a (Theorem 1a's unused "S finite"; SM:222 carrier) | SM:222, SM:242 | S3 at SM:222; SM:242 N; dropping the hypothesis is Q2 |
| 10 (Lemma 1c(i), any probability space) | SM:252 | no change to (i) |
| 11–12 (Lemma 1c(ii): determinant proof; H-cont; H-Bloch) | SM:252, SM:254 | S7, S8: (ii) stated on a finite carrier and fibrewise under translation invariance; the infinite-carrier pole reading stated as not established |
| 15, 17 (Proposition 4b; Theorem 5's kinetic clause) | SM:334, SM:336 | N: the counting measure is stated |
| 18, §7.2, §9a (checkerboard; odd tori) | SM:539 | S6 |
| 20–21, §5 (Theorem 19, H-μ(φ,Θ)) | SM:641 | N: the counting-measure prior is stated; the ℤ^d form is Q4 |
| 22 (Stage 3, H-count) | GR:58, GR:88, ch07:42 | N: stays conditional on A1 (scope: R1); preserved by CTL-15 |
| 23–24 (Theorem 24(i) coherent form, (iii)) | Sub:262, Sub:268, ch02:144 | N: finite-factor statements with infinite extensions stated as not established |
| 26 (Theorem 23 lists A1) | Sub:104–133, :189–195, :205–233, ch02:88–122, ch04:10–26, ch05:19, Str:768, glossary:13 | N: A1–A6 stated as hypotheses |
| §9 (SM:240 ring countermodel) | SM:240 | N: correct as stated; a finite countermodel remains one in any class that keeps finite models |

### 3.4 Keep list (CTL-14 residue)

At the base, 28 distinct sentences on paper and chapter site lines match the finiteness pattern of §5 without a
condition token: 9 are edited (S2–S5, T1, B2, B3, K1, K3) and 19 are kept; FULL copies follow their chapter line. The
ledger's `keep` list records the 19 kept sentences by SHA-256 with their reasons: external-theorem scope (GR:20), finite operational carriers (GR:257, :261),
continuation of a sentence that states the finite representative (GR:591), stated hypotheses of cited results (GR:138,
SM:24, ch03:240, ch09:106, Str:1157), mathematical statements about finite sets (SM:1227), other programmes
(Str:339), problem classes (Sub:52 second sentence), the A4 declaration and its mirror (Sub:98, ch02:82), Stage 1's
per-context construction (Sub:125, ch02:90), finite Bell regions (Sub:131) and a quantifier (ch05:77). Each is
checked by the reviewer (§9 item 4).

## 4. Edit plan (delta 2; exact text in `phase2_ledger.json`; not applied)

The ledger is authoritative: 26 splices, each with file, site, exact old string and its SHA-256, new text and its
SHA-256, rows, reason, sufficient condition and source of support. No splice adds or removes a line.

**Marks** (as P0 §3): **status** (A1's status stated), **condition stated** (an existing finite statement gains its
condition, no change of content), **weaker** (a weaker sufficient condition added, proved in Main), **narrowed** (a
statement reduced to its proved scope), **open** (an open question named).

| Unit | Site | Change (summary) | Sufficient condition | Mark | Support |
|---|---|---|---|---|---|
| S1 | SM:44 | adds: "For the P-indivisibility conclusion itself the near-return condition (NR) of [Main §2.3], assumed in place of finiteness as a hypothesis and not adopted, is a weaker sufficient condition." | A1 or (NR) | weaker | Main §2.3 Corollary (near-return) |
| S2 | SM:158 | "on the finite phase space" → "on the phase space, finite under A1" | A1 | condition stated | Substratum §3.1 |
| S3 | SM:222 | "The finite bijection is fundamental" → "The substratum bijection is fundamental (under A1 and A4 [Substratum §3.1] it acts on a finite periodic quotient of Λ)" | A1 with A4 | condition stated | O-A4 §9a |
| S4 | SM:232 | "the finite bijection φ" → "the bijection φ, finite under A1" | A1 | condition stated | — |
| S5 | SM:316 | "the fundamental finite bijection" → "the fundamental bijection (finite under A1)" | A1 | condition stated | — |
| S6 | SM:539 | bipartite on ℤ³ and on periodic quotients with even-sum period vectors, with the parity argument; a quotient with an odd-sum period vector (an odd torus) carries no checkerboard | ℤ³ or even-sum quotient | narrowed | O-A4 §7.2, checks E |
| S7 | SM:252 | Lemma 1c(ii) opens "On a finite carrier, and in each Fourier fibre of a translation-invariant U with finite-dimensional cell data" | finite carrier, or fibrewise finite (O-A4 H-Bloch) | narrowed | SM:254 proof; O-A4 §6.1 |
| S8 | SM:254 | proof: the fibrewise argument; on an infinite carrier without that structure the pole reading assumes a continuation "not established here" | as S7 | narrowed | O-A4 §6.1 |
| B1 | Sub:92 | "A1 remains the finite-carrier premise …" → A1 "an open hypothesis, not adopted ([Main §4.5], item (ii)), and one sufficient condition among those each result names", premise of the recurrence arguments, with (NR) weaker for their P-indivisibility conclusion | A1 or (NR) | status, weaker | Main §1.2, §2.3, §4.5 |
| B2 | Sub:288 | "S is a finite set" → "S is a set (finite under A1)" | A1 | condition stated | — |
| B3 | Sub:52 | "the finite OI configuration" → "the OI configuration (finite under A1)" | A1 | condition stated | — |
| B4 | Sub:56 | adds: without A1 the replacement of the past hypothesis is open; an invariant law on an infinite carrier can carry a low-entropy stream from spatial infinity (every Bernoulli product law is shift-invariant) | A1; without A1 open | open | REMAINDER §5; stated in the splice |
| G1 | GR:138 | adds: the near-return corollary gives P-indivisibility for an infinite deep sector under (NR), "assumed … not adopted" | A1 or (NR) | weaker | Main §2.3; GR App. B prior (D5) is shared by every root |
| G2 | GR:589 | adds ", or the near-return condition (NR) of [Main §2.3], assumed in its place as a hypothesis and not adopted" | A1 or (NR) | weaker | Main M:724 (E11) |
| T1 | Str:224 | "OI's \|S\| < ∞ requirement" → "OI's structural condition A1, \|S\| < ∞" | A1 | condition stated | — |
| T2 | Str:718 | "overall recurrence time" → "the overall recurrence time of a finite representative" | finite representative | condition stated | Main §4.6 Setup |
| K1 | ch02:158 | mirror of B2 | A1 | condition stated | — |
| K2 | ch02:76 | "open hypothesis, not adopted" gains ", and one sufficient condition among those the results name" (Phase 1 B1/B8 wording) | A1 | status | Main §1.2, §4.5 |
| K3 | ch05:83 | "the finite bijection" → "the substratum bijection (finite under A1)" | A1 | condition stated | — |
| K4 | ch05:89 | "the fundamental finite bijection" → "the fundamental bijection (finite under A1)" | A1 | condition stated | — |
| K5 | ch09:189 | "a finite configuration space" → "a configuration space finite under A1" | A1 | condition stated | ch09:183, :193 |
| K1–K5-FULL | FULL | the same splices on the byte-identical FULL lines (§A.14) | | | |

**Not edited, by decision of §3.1:** GR:58 and GR:88 (R1 stays conditional on A1, scope); Theorem 19 (counting-measure
prior stated); Proposition 4b; Theorem 23 and its mirrors (A1–A6 stated); the A4 clause (Q1); Theorem 1a (Q2); SM:240
(correct as stated); SM:20, SM:22, GR:20 (finiteness stated as the setting or the declared input; Q5).

## 5. Controls (§A.41 invariant → checkpoint table)

Implemented in [`phase2_controls.py`](phase2_controls.py) (standard library). It loads the Phase 0 functions from
`../a1-scope-phase0-20261120/phase0_controls.py` unchanged. Base: `git show b9168ef0:<path>`. Head: the working tree,
or with `--dry-run` the base with the ledger applied in memory. Exit status 0 iff no control FAILs (§A.44).

| Id | Invariant | Checkpoint |
|---|---|---|
| CTL-1–5 | Main's frozen statements unchanged | P0 `check_frozen` on Main (Main is not in the ledger) |
| CTL-6 | Lean and registry unchanged; no new kernel identifier | no change under `verification/lean*` or the registry; registry statuses equal; `lean_manuscript_census.py` exits 0; no backticked identifier new to any changed file |
| CTL-7 | no edit presents a law, typicality, recurrence or inflow as derived or physical; every new label carries a status word | P0 `check_added` on added sentences of every changed file |
| CTL-8 | paper register (§A.32, §A.33) | P0 `check_added` on added sentences in `papers/` |
| CTL-9 | generated artifacts current | `tools/staleness_check.py` exits 0 |
| CTL-10 | Main ledger inventory unchanged | P0 item test |
| CTL-11 | the edit is exactly the ledger | every `papers/*.md`, `book/*.md` equals base + ledger splices (P0 `check_ledger_exact`); vacuous when nothing changed |
| CTL-12 | status wording not weakened | in every scope file and Main, the counts of "not adopted", "open" and A1/(ii)/total-finiteness sentences with posit/hypothesis do not decrease |
| CTL-13 | FULL parity | P0 `check_full_parity` |
| CTL-14 | no unconditioned finiteness on in-scope site lines | on each site line (FULL by chapter-line text), every sentence matching `FIN` and no `COND` token is in the ledger `keep` list; every `keep` entry is a base sentence |
| CTL-15 | preserved companion statements | GR:58 (H-count), GR boundary-only lemma, H-BD, GR App. A setup; SM Theorem 1a and proof, Theorem 19, Proposition 4b, SM:210 corollary, SM:240; Substratum (A4), Lemma 23.0, Theorems 23, 24; Structure Proposition 9.5: paragraphs byte-identical. Required text: GR "Under A1, restrict the finite total system …" and "H-count — that the total system is finite (A1)"; "(A1) **Finiteness.** The configuration space $S$ is finite."; Theorem 19's "counting measure" |
| CTL-16 | site lines stable | line counts of the scope files equal the base |

`FIN` and `COND` are printed verbatim in the script. `COND` tokens: A1, A4, posit, hypothes-, assum-, if, Let,
condition, sufficient, (NR), representative, model, realiz-, counterexample, instance, "on a finite", "for (a) finite",
suppose, "finite under".

**Self-test (`--self-test`, on the real base texts).** The compliant head (ledger applied) passes every control and
meets every DR; the base leaves DR-2 unmet. Eleven countercontrols must fail: M1 strip "(finite under A1)" at Sub:389
(CTL-14); M2 revert S3 (CTL-14, CTL-11); M3 GR:58 without "Under A1" (CTL-15); M4 "(NR) holds in nature … recurrence is
derived" (CTL-7); M5 delete "not adopted" in ch02:76 (CTL-12); M6 K1 without its FULL mirror (CTL-13); M7 an inserted
line (CTL-16); M8 S1 without (NR) (DR-3 unmet); M9 a forged keep entry (keep integrity); M10 "The substratum is a
finite set." inserted on GR:591 (CTL-14); M11 Theorem 19's prior changed (CTL-15). The Phase 0 self-test runs first.
A mutation check outside the record disabled each check function in turn; the self-test failed every time.

**Runs at this record's head.**

| Run | Result |
|---|---|
| `--self-test` | PASS (Phase 0 functions PASS; 11 countercontrols FAIL as required) |
| base working tree | CTL-1–13, 15, 16 PASS; CTL-14 FAIL on exactly the 9 edited sentences and the FULL copies of ch02:158 and ch05:83 (the residue the ledger removes); DR-2, DR-3 unmet |
| `--dry-run` | CTL-1–8, 10, 12–16 PASS; CTL-9, CTL-11 N/A in memory; DR-1–DR-4 all met |

## 6. Decision rule (fixed in advance)

Phase 2 succeeds if and only if, on its final head:

1. **DR-1 (completeness).** `dispositions.json` holds exactly one disposition for each of the 214 in-scope sites; every
   `edit` names ledger units whose old text lies on that site's base line; every ledger unit is used, or is the
   declared companion S8.
2. **DR-2 (nothing unconditional).** CTL-14 holds: no unconditioned finiteness sentence on an in-scope site line
   outside the `keep` list, and every `keep` entry is a base sentence.
3. **DR-3 (change rows, diff-based).** Tokens occur in sentences of the file absent from the base:
   SM `(NR)`, `not adopted`, `weaker sufficient condition`; GR `(NR)`, `not adopted`, `near-return corollary`;
   Substratum `open hypothesis, not adopted`, `one sufficient condition`, `(NR)`; ch02 `one sufficient condition`;
   SM `finite periodic`, `quotient of $\Lambda$`; SM `even coordinate sum`, `odd side`; SM `On a finite carrier`,
   `Fourier fibre`, `not established`; Substratum `Without A1 this replacement is open`.
4. **DR-4 (R1 and preserved statements).** CTL-15 holds; GR:58 remains conditional on A1 and H-count.
5. **All controls hold.** CTL-1–16 PASS on the working tree after the rebuild; CTL-11 makes the text the ledger's
   exactly.
6. **Review.** An independent non-author review confirms S6's parity argument, S7–S8's scope against the SM:254
   proof, G1's applicability of Main's corollary to GR's deep-sector prior, and the keep list.

The predicates, token lists, keep list and ledger are not adjusted after Phase 2's text exists, except by an appended,
reviewed ledger amendment made before the edit (or, as in Phase 1, under a recorded owner exception).

## 7. Application, propagation and rebuild (stage 2, after the owner decision)

1. Apply the ledger in order (each old string occurs once).
2. Run `phase2_controls.py --root .` (all CTL, including CTL-11, CTL-13, CTL-14).
3. Re-grep the Phase 0 patterns over the scope files; confirm that only the 25 `edit` sites and SM:254 changed; state
   the surviving counts.
4. Rebuild with `sh ./build.sh SM Substratum GR Structure` and `sh ./build.sh --book`; no dropped glyphs; check page
   count and characters per page.
5. Run CTL-9.

## 8. Open questions for the owner

- **Q1 (O-A4 §7, A4's period lattice).** The A4 clause (Sub:98, mirror ch02:82) admits every finite-index sublattice.
  `O_h` equivariance needs an `O_h`-invariant period lattice and the eight staggered corners need Λ ⊂ 2ℤ³. Options:
  (a) narrow the A4 clause, with propagation to ch02:82 (and a check of Stage 2(d)–(e) and SM:531); (b) a separate
  unit; (c) leave as recorded. Phase 2 edits only SM:539 (named in the scope).
- **Q2 (Theorem 1a).** Its proof uses only `P² = P`, `Q = I − P` and linearity (O-A4 row 9), so "Let S be finite" can be
  dropped (theorem recovery) to cover the ℤ^d carrier; the Attribution paragraph (SM:250) would then need its "FINITE
  deterministic bijection" adjusted. Phase 2 instead states the finite reading at SM:222 (S3).
- **Q3 (scope).** The 77 out-of-scope Phase 2 sites (§2): a further unit, or added here by amendment.
- **Q4 (alternatives on ℤ^d).** Whether the companions should state O-A4's alternative sufficient conditions (A4∞, LF,
  H-μ(φ,Θ), H-μ(sp), H-Bloch) beside A1 for Stage 2 and Theorem 19, rather than only record them here. Not proposed:
  each would be a new manuscript claim resting on a research record.
- **Q5 (prerequisite summaries).** SM:22 and GR:20 summarize Main's result "in a deterministic bijection on a finite
  configuration space". The finiteness is the stated setting, so they are `N`; adding "(finite under A1)" is optional.

## 9. Reviewer checklist

1. The scope (§2) and the disposition test (§3.1); spot-check `N` dispositions in each file, especially Structure's
   C11 class sentences and the INFLOW and DECL rows.
2. Each splice in `phase2_ledger.json` against its site: minimal, correct, register (§A.32/§A.33), "assumed … not
   adopted" for every (NR) use, no premise adopted, no derived law, typicality, recurrence or inflow (§A.29).
3. S6 (parity on quotients), S7–S8 (Lemma 1c(ii) against its determinant proof, fibrewise case for (iii)), G1 (Main's
   corollary hypotheses: finite C_V, one prior shared by every root, measurable update; GR's prior (D5)), B4 (the
   inflow sentence's support).
4. The 19 `keep` entries and their reasons; whether any `COND` token excuses a sentence it should not (P2-F6).
5. That `phase2_controls.py` implements §5 and §6; that the self-test, base run and dry run reproduce; that the
   countercontrols are live.
6. Q1–Q5.

## 10. Off-`main` references (§A.42 item 8)

| Reference | Attached to | Classification |
|---|---|---|
| #1169 comments 7033018172, 7032429839 | authorization and scope | provenance; quoted with author and time |
| #1441 (O-A4) review comments | review status of O-A4 | provenance; O-A4's record and checks are on `main` |
| #1443 | Phase 1 | provenance; its merge `b9168ef0` is the pin |
| #1055, #1169, #1334, #866 | accountability; O-INFLOW | provenance |

## 11. Verification status (§A.46 item 4)

Evidence level: paper reading of the cited sources and mechanical controls (§5). No proof is added beyond the one-line
arguments inside S6, S8 and B4. Missing: independent non-author review of this record; the owner's decision on
application and on Q1–Q5. Accountable Issue: #1055.

## 12. Amendment 1 (2026-11-20, before any manuscript edit)

**Trigger.** The independent non-author review of `3b5c937c` returned REVISE. It verified that the controls are live,
that all 26 splice hashes match the base, that S6, S7–S8 and B4 are mathematically correct, and that all 19 keep
entries are justified. It raised two blocking items and nine nits. The review was relayed by the coordinating session.
This amendment is appended under §6 ("an appended, reviewed ledger amendment made before the edit"). The earlier
splices, keep entries and commits are unchanged.

**Ledger.** Fourteen splices are appended, marked `"amendment": 1`, for 40 in all. Units carrying `amends` act on text
that an earlier unit inserted. Each old string occurs once in the text the earlier splices produce.

| Review item | Unit(s) | Change |
|---|---|---|
| B1 (blocking): G1 omitted the measurability hypothesis of Main's corollary. GR (D5) allows any σ-algebra, and Appendix B gives measurability only for t ≤ n (Lemma B.3). | A-G1 | "gives P-indivisibility **for a measurable update** from a non-permutation rooted map under its near-return condition (NR)". The support line names every hypothesis of the corollary. |
| B2 (blocking): the census read only Phase 0 site lines. | A-C1 SM:30; A-C2 SM:60; A-C3 Str:730; A-C4 Str:732; A-C5 ch02:8 (+FULL); A-C6 ch05:15 (+FULL) | Each names its condition ("finite under A1", or for ch05:15 "finite under the open hypothesis A1", as ch05:23 has it) |
| Nits 3–4: "carrier" is SM's reserved gauge-carrier term. The fibrewise case needs P translation invariant as well as U. | A-S7, A-S8 | "On a finite configuration space, and in each Fourier fibre when $U$ and $P$ are translation invariant …"; "On an infinite configuration space …". The symbol S is avoided because Lemma 1c(i) names a relabelling S. |
| Nit 6 | A-S3 | "it acts on configurations over a finite periodic quotient of Λ". S3 makes the SM:222/SM:242 conflict conditional; the root fix remains Q2. |
| Nit 7 | A-K2 (+FULL) | reordered: "…not adopted, read as the choice of the minimal finite representative and motivated by E3 (…); it is one sufficient condition among those the results name." |
| Nit 10 (optional) | not adopted | S1 keeps the existing sentence with "requires", which is true of the recurrence-cycle result. Changing the verb would make CTL-7 read the whole sentence as added, including "bijectivity guarantees recurrence". |

**Census extension (B2).** CTL-14 and DR-2 now scan every line of the scope papers and chapters, plus the FULL copies of
the Phase 0 site lines. A FULL copy of any other chapter line is covered by CTL-13 and CTL-11. At the base, the whole-file
scan finds 31 lines outside the Phase 0 site map that carry an unconditioned finiteness sentence:

- **6 lines edited:** SM:30, SM:60, Str:730, Str:732, ch02:8 and ch05:15.
- **25 lines kept (26 sentences), each with a reason in the keep list:**
  - mathematical statements: Sub:333, Str:734, Str:1233;
  - a scoped result: Sub:344, which concerns records "from one fixed finite reversible carrier";
  - finite operational carriers (C5): Sub:533, ch04:146, GR:213, :225, :239, :249, :255, :273;
  - the boxed no-go for the finite OI class: GR:219;
  - GR Appendix A and B hypotheses and proofs: GR:132, :761, :879, :880, :895, :901;
  - the finite algebra-channel pair of Structure §10.4: Str:800, :821, :972;
  - ch04:94, keyed K in Phase 0 (C5);
  - a quantifier: ch07:126;
  - a statement of hypotheses: glossary:105.

The reviewer's borderline items are decided as follows: ch02:8 is edited; ch04:94 and Sub:344 are kept. `dispositions.json`
now holds 251 dispositions (214 sites, 31 census lines and 6 FULL copies of census chapter lines). The keep list holds
45 entries.

**Controls.** These changes are made in `phase2_controls.py` (same commit):

- CTL-14 and DR-2 cover the whole scope files (`scan_lines`).
- DR-1 also requires a disposition for each census line (`census_lines`) and for the FULL copy of each census chapter line.
- CTL-7 gains a rule (nit 8): every added sentence that contains "(NR)" also contains "not adopted". The Phase 0
  status test is vacuous for that label, because "(NR)" sits beside "condition".
- DR-3: the Lemma 1c(ii) row reads "On a finite configuration space" and "when $U$ and $P$ are translation invariant".
  The GR row adds "for a measurable update". Four rows cover the census splices.
- Four countercontrols are added:
  - M12: "(NR) … which holds." (CTL-7);
  - M13: "(NR), adopted here," (CTL-7);
  - M14: census splice A-C6 reverted in the chapter and FULL (CTL-14);
  - M15: "The substratum is a finite set." inserted on SM:30, a line outside the Phase 0 map (CTL-14).
- A recipe for the mutation check of §5 (nit 11):
  `python3 -I -B phase2_controls.py --root . --mutation-check` disables each check function in turn and exits 0 only if
  the self-test then fails for every one.

**Dispositions (nit 9).**

- SM:44: its last sentence ("The lattice is one way to implement determinism on a finite set …") passes CTL-14 lexically,
  through "not". It is kept on its merits, because it states one implementation and does not assert that S is finite.
- SM:20: it passes CTL-14 lexically, through "condition". It is kept as the declared structural input.
- ch02:32 and its FULL copy: the reason now reads that finiteness is stated for "the exact OI model here".

**Q1, routed explicitly (nit 5).** Two more sentences belong to Q1:

- SM:539's spin–taste sentence, which identifies the two sublattices with the grades of γ₅ ⊗ ξ₅. It uses the staggered
  corners and so needs Λ ⊂ 2ℤ³ on a finite quotient.
- SM:1536's unqualified "bipartite checkerboard structure" among the substratum's exact discrete symmetries.

Both stay unedited pending the owner's decision on Q1. Q1–Q4 are not acted on.

**Runs at the amended head.**

| Run | Result |
|---|---|
| `--self-test` | PASS (Phase 0 functions PASS; 15 countercontrols FAIL as required) |
| `--mutation-check` | PASS (each of 8 check functions disabled → the self-test fails) |
| base working tree | CTL-1–13, 15, 16 PASS. CTL-14 FAILs on exactly the 15 paper and chapter sentences the ledger edits and on the FULL copies of ch02:158 and ch05:83. DR-2 and DR-3 are unmet. |
| `--dry-run` | CTL-1–8, 10, 12–16 PASS; CTL-9 and CTL-11 N/A in memory; DR-1–DR-4 all met |

**Counts that replace §3.2 and §4.**

| File | Splices |
|---|---|
| SM | 13 |
| Substratum | 4 |
| GR | 3 |
| Structure | 4 |
| ch02 | 4 |
| ch05 | 3 |
| ch09 | 1 |
| FULL | 8 |
| **Total** | **40** |

The `edit` dispositions now number 33: the original 25 and 8 census edits, 6 on paper or chapter lines and 2 on FULL
copies. Each amended line keeps its original disposition with the amendment unit added. §7 step 3 reads "only the `edit`
lines and SM:254 changed".

**Off-`main` reference.** The review of `3b5c937c` is cited as provenance. Each change it prompted is written out in
the ledger and checked by the controls above.
