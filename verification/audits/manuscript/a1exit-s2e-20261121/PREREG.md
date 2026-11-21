# A1-EXIT Step 2, unit S2-E — Q3 propagation of the 81 remaining sites: preregistration

**Status.** Writer's preregistration, WIP / UNVERIFIED, pushed before any manuscript edit.
Independent non-author review is required; merge is a separate owner decision. Consistency work only
(§A.23): no premise is added and no claim is strengthened; bands unchanged.

**Authorization.** Owner `amaybaum`, #1169 comment 7056875845 (2026-11-21), unit S2-E, the last
Step-2 unit. Limits as recorded there: manuscript corrections in this unit's scope only; A1 and Main
posit-ledger item (ii) are not deleted; the pointer sites are not rewritten (they belong to the final
deletion edit, which is not authorized); no merge; no workflow dispatch.

**Goal link (§A.47).** The A1-exit objective (#1169). This unit decides, for each of the 81 Q3 sites of
the A1-EXIT ledger, whether it can be made true without A1, in one of three forms: a proved weaker
condition, an explicit finite-only scope, or an open statement.

**Base.** `main` at `1c7eedc40`. The ledger pin is `e837e3db`; `git diff e837e3db 1c7eedc40` is empty
for `papers/Computation.md`, `papers/Complexity.md`, `papers/Introduction.md`, `papers/Medicine.md`,
`papers/Methodology.md` and `book/`, so every pin line number is the base line number. No edit adds or
removes a line.

## 1. Sources

- **Ledger.** `verification/audits/foundations/a1exit-ledger-20261120/` (LEDGER.md §4, rows.json rows
  X-01, X-10, X-20, X-24, X-26, X-30, X-45, X-55, X-63, X-80, X-82; sitemap.json).
- **S2-C** (PR #1474, branch `research/a1exit-s2c-20261121` at `cb6d1b87e`), RESULT §2: the return
  form, its book parenthesis form ("of Main §3.2"), "assumed as a hypothesis and not adopted", and the
  finite-only scope "on a finite representative". Copied verbatim.
- **S2-D** (PR #1472, branch `research/a1exit-s2d-20261121` at `c5aaeb73f`), RESULT §3: the two Cx:212
  wordings, copied verbatim; ch18:40 takes no change (the sentence does not use finiteness to exclude an
  inflow; reviewer finding relayed by the coordinator).
- **S2-A** (PR #1470, branch `research/a1exit-s2a-20261121` at `dd95fcd0b`): A4 on $\mathbb{Z}^d$ as
  "the standard construction, distinct from a continuous space", a finite periodic quotient
  $\mathbb{Z}^d/P$ "admitted as a qualified case, under the conditions on $P$ stated with each result
  that uses it"; no approximation wording. Owner A4 decision #1169 c.7048255658.
- **Routed sites** (coordinator, from the S2-A review): ch18:22, ch18:226 and ch18:230 with FULL
  mirrors (discrete lattice beside a continuous $\mathbb{R}^3$; "Klein-bottle quotient" is not a
  translation quotient $\mathbb{Z}^d/P$).

## 2. Decision rules (fixed before editing)

1. **Pointer (row X-01).** A site whose only A1 content is a pointer to the posit ("A1", "the
   total-finiteness posit", "posit ledger") is left unchanged and recorded "deferred to the deletion
   edit".
2. **F rows (X-10, X-24, X-26, X-55, X-80; X-45 is F).** The statement stays and becomes explicitly
   finite-scoped ("for a finite substratum", "on a finite representative", "a finite model"); A1 is not
   presented as a framework hypothesis. A site already finite-scoped takes no change.
3. **J rows (X-20, X-30).** Where a site states the result without its weaker condition, the weaker
   condition is printed in its source wording ((NR) with S2-C's return parenthesis; (REV) with
   M:732 (iii)'s wording), or the site is finite-scoped.
4. **O rows (X-63, X-82).** Stay visibly open (S2-D's Cx:212 wording).
5. **Lattice sites.** $\mathbb{Z}^3$ is stated as the discrete lattice, distinct from a continuous
   $\mathbb{R}^3$; a translation quotient $\mathbb{Z}^3/P$ is A4's qualified case; a Klein-bottle-type
   identification is stated as not a quotient by translations alone.
6. **Register.** Book and papers: no revision-history words, meta-commentary, reader instructions or
   caps emphasis in added text (§A.32, §A.33).

## 3. Disposition of the 81 sites

Line numbers are base = pin. FULL line = ch14 line + 3600, ch18 line + 4731, glossary line + 6491.

| Site | Row | Disposition | Edit / reason |
|---|---|---|---|
| Comp:120 | X-01 | deferred to the deletion edit | only A1 content is the pointer "the total-finiteness posit ([Main] §1.2, §4.5) remains open and unadopted" |
| Comp:122 | X-10 | no change | already "the substratum measure of a finite representative" |
| Comp:178 | X-55 | edited | E01 |
| Comp:182 | X-55 | edited | E02 (ledger wording) |
| Cx:212 | X-82 | edited | E03a, E03b (S2-D wording) |
| Intro:12 | X-20 | no change | finite-scoped: "In finite reversible models … finite recurrence also forces"; no (NR) restatement |
| Intro:93 | X-20 | no change | finite-scoped: "In a finite reversible world" |
| Med:25 | X-24 | no change | "on one fixed finite reversible representative"; row correction none |
| Med:35 | X-20 | edited | E04 |
| Meth:106 | X-30 | no change | the ladder lists bijectivity as a claim of the definition; its status is stated at :146–:148 |
| Meth:146 | X-30 | edited | E05a–c |
| Meth:148 | X-30 | edited | E06 |
| Meth:156 | X-01 | deferred to the deletion edit | only A1 content is the pointer "the structural assumption A1 … counted as such in the companion paper's posit ledger" |
| Meth:158 | X-01 | deferred to the deletion edit | only A1 content is the pointer "which is A1"; the sentence is scoped "on the finite total representative" |
| Meth:283 | X-63 | no change | S2-D RESULT §3: region-level exclusion, finite bijective model, no phase conclusion |
| Meth:339 | X-45 | edited | E07 |
| Meth:345 | X-45 | edited | E08a, E08b |
| Meth:357 | X-45 | edited | E09a, E09b |
| Meth:367 | X-45 | edited | E10 |
| Meth:369 | X-45 | edited | E11 |
| Meth:441 | X-63 | no change | S2-D RESULT §3: "The proved exclusion uses a finite bijective model" |
| Meth:517 | X-01 | edited | E12 (not a pointer: asserts a finite substrate) |
| ch14:160 = FULL:3760 | X-55 | edited | B01 |
| ch14:164 = FULL:3764 | X-55 | edited | B02 |
| ch14:184 = FULL:3784 | X-55 | edited | B03a, B03b |
| ch14:262 = FULL:3862 | X-55 | edited | B04 |
| ch14:272 = FULL:3872 | X-10 | no change | already "the maximal-entropy measure of a finite representative" |
| ch18:20 = FULL:4751 | X-26 | edited | B05 |
| ch18:36 = FULL:4767 | X-10 | edited | B09 |
| ch18:40 = FULL:4771 | X-82 | no change | does not use finiteness to exclude an inflow (S2-D reviewer); its "recurrent under A1 (§18.7)" is a pointer left for the deletion edit |
| ch18:162 = FULL:4893 | X-26 | edited | B10 |
| ch18:164 = FULL:4895 | X-26 | no change | section heading; the section is finite-scoped by B11 |
| ch18:166 = FULL:4897 | X-26 | edited | B11a–c |
| ch18:168 = FULL:4899 | X-26 | edited | B12 |
| ch18:170 = FULL:4901 | X-26 | edited | B13a, B13b |
| ch18:172 = FULL:4903 | X-26 | edited | B14a–c |
| ch18:174 = FULL:4905 | X-26 | no change | mathematics of a bijection of a finite set |
| ch18:176 = FULL:4907 | X-26 | no change | permutation-order bounds for finite $S$ |
| ch18:178 = FULL:4909 | X-26 | no change | "For illustration only, if $\lvert S\rvert$ were …"; cardinality "not fixed by visible data" |
| ch18:179 = FULL:4910 | X-26 | no change | displayed bound under the same illustration |
| ch18:180 = FULL:4911 | X-26 | no change | as :179 |
| ch18:183 = FULL:4914 | X-26 | no change | bound for an invertible linear map of finite $S$ |
| ch18:184 = FULL:4915 | X-26 | no change | as :183, with the named nonlinear bijections |
| ch18:186 = FULL:4917 | X-26 | no change | "a finite model returns …" |
| ch18:188 = FULL:4919 | X-26 | no change | "A finite model is periodic …" |
| ch18:190 = FULL:4921 | X-26 | edited | B15 |
| ch18:192 = FULL:4923 | X-26 | edited | B16a, B16b |
| ch18:242 = FULL:4973 | X-80 | edited | B17 |
| ch18:244 = FULL:4975 | X-80 | edited | B18 |
| ch18:260 = FULL:4991 | X-80 | edited | B19 |
| ch18:288 = FULL:5019 | X-80 | edited | B20 |
| gloss:105 (= FULL:6596, mirror) | X-20 | edited | G01 |

Counts: 47 ledger sites edited (30 sources, 17 FULL mirrors), 3 deferred to the deletion edit, 31 no
change. Routed sites outside the ledger: ch18:22 = FULL:4753 (B06), ch18:226 = FULL:4957 (B07),
ch18:230 = FULL:4961 (B08). The glossary mirror FULL:6596 is edited with G01.

## 4. Mirrors (§A.14, §A.25)

Every book edit (B01–B20, G01) is applied to the chapter or glossary and to FULL.md, byte-identically.
No companion paper restates the Comp, Cx, Med or Meth sentences edited here (distinctive-phrase grep at
the base). Main is not edited.

## 5. Edit list

The exact strings are in `checks/s2e_edits.json`, from which the list below is generated.
`checks/s2e_check.py base` checks that each old string occurs exactly once in its file (and in FULL.md
for a book edit) on the stated line; `apply` applies them; `applied` (default) checks the result and
the book ↔ FULL identity of each edited line. At the base: `base check PASS (45 edits)`.

### E01 — `papers/Computation.md:178`

- **Ledger row:** X-55. **Source:** X-55 correction (restate as conditional statements about finite substrata).
- **Finding:** A1 presented as a framework hypothesis; the statement is true for a finite substratum.
- **Old** (unique in its file):

  > The framework's axiomatic content concerns, under A1, finite physical structures

- **New:**

  > For a finite substratum, the framework's axiomatic content concerns finite physical structures

### E02 — `papers/Computation.md:182`

- **Ledger row:** X-55. **Source:** X-55 correction, verbatim head ("The framework's finiteness hypothesis (A1)" -> "A finite substratum"); appositive adjusted for grammar.
- **Finding:** A1 presented as the framework's hypothesis.
- **Old** (unique in its file):

  > The framework's finiteness hypothesis (A1) — that the substratum has finitely many tokens at any moment — sits naturally

- **New:**

  > A finite substratum — one with finitely many tokens at any moment — sits naturally

### E03a — `papers/Complexity.md:212`

- **Ledger row:** X-82 (T17b). **Source:** S2-D RESULT §3, Cx:212 item 1 (verbatim).
- **Finding:** global equilibrium-phase conclusion (X-63 T17b) not supported; region-level form W*.
- **Old** (unique in its file):

  > that C1–C4-satisfying observers, with C2 read in its timescale form, cannot exist in the equilibrium phase of $(S, \varphi)$:

- **New:**

  > that C1–C4-satisfying observers, with C2 read in its timescale form, cannot exist in regions whose effective channel mixes in a time short compared with $\tau_S$:

### E03b — `papers/Complexity.md:212`

- **Ledger row:** X-82; X-63 (T17b). **Source:** S2-D RESULT §3, Cx:212 item 2 (verbatim).
- **Finding:** past-hypothesis replacement asserted from a global-phase claim; the inflow endpoint (O-INFLOW) open without finiteness.
- **Old** (unique in its file):

  > The "past hypothesis" of low initial entropy — usually imported as a separate axiom to explain why we observe a low-entropy universe — is replaced, in its role of selecting observer-compatible configurations, by the same theorem, since, in that description and with C2 read in its timescale form, observers exist only in the non-equilibrium phase.

- **New:**

  > Whether the same theorem replaces the "past hypothesis" of low initial entropy — usually imported as a separate axiom to explain why we observe a low-entropy universe — in its role of selecting observer-compatible configurations is open, since the theorem selects regions rather than global configurations; on an infinite carrier an invariant law can also carry a low-entropy stream entering from spatial infinity, and whether such an incoming supply is excluded is not settled.

### E04 — `papers/Medicine.md:35`

- **Ledger row:** X-20. **Source:** S2-C finite-only scope of a recurrence-cycle statement ("on a finite representative").
- **Finding:** finiteness used as an unscoped premise of the recurrence-scale result.
- **Old** (unique in its file):

  > which holds at the recurrence scale from a non-permutation rooted map and finiteness,

- **New:**

  > which holds at the recurrence scale from a non-permutation rooted map on a finite representative,

### E05a — `papers/Methodology.md:146`

- **Ledger row:** X-30. **Source:** X-30 exit (eventual-image recovery stays a finite statement, M:60).
- **Finding:** eventual-image restriction is a finite-set argument, stated without finite scope.
- **Old** (unique in its file):

  > it is removable for registered histories whose states lie in the eventual image

- **New:**

  > it is removable, on a finite representative, for registered histories whose states lie in the eventual image

### E05b — `papers/Methodology.md:146`

- **Ledger row:** X-30. **Source:** as E05a.
- **Finding:** as E05a.
- **Old** (unique in its file):

  > the second for registered states in the eventual image

- **New:**

  > the second, on a finite representative, for registered states in the eventual image

### E05c — `papers/Methodology.md:146`

- **Ledger row:** X-30. **Source:** as E05a.
- **Finding:** as E05a.
- **Old** (unique in its file):

  > or, for registered states in the eventual image, by the eventual-image restriction

- **New:**

  > or, for registered states in the eventual image of a finite representative, by the eventual-image restriction

### E06 — `papers/Methodology.md:148`

- **Ledger row:** X-30. **Source:** X-30 weaker condition (REV), M:732 (iii), and exit (bijectivity posited as (REV), not recovered).
- **Finding:** surjectivity presented as awaiting total finiteness (A1); without A1 it is the posit (REV).
- **Old** (unique in its file):

  > Reversibility therefore is not established here — it waits on finiteness of the total space (Section 4.5).

- **New:**

  > Reversibility therefore is not established here: on a finite total space it follows from injectivity (Section 4.5); otherwise it is posited as reversibility (REV), $\varphi$ a bimeasurable bijection of a measurable carrier ([Main §4.5]).

### E07 — `papers/Methodology.md:339`

- **Ledger row:** X-45. **Source:** X-45 correction ("under E1–E7 and A1–A6" -> "for a finite substratum — A4's finite periodic ... qualified case — satisfying E1–E7 and A2–A6"), with S2-A's A4 qualified-case wording.
- **Finding:** A1 listed among the reconstruction's hypotheses.
- **Old** (unique in its file):

  > Given E1–E7, A1–A6, the M1-T temporal

- **New:**

  > For a finite substratum — A4's finite periodic quotient $\mathbb{Z}^d/P$, a qualified case under the conditions on $P$ stated with each result that uses it [SM §4.1] — given E1–E7, A2–A6, the M1-T temporal

### E08a — `papers/Methodology.md:345`

- **Ledger row:** X-45. **Source:** X-45 correction ("the structural class A1–A6" -> "the class of such finite substrata").
- **Finding:** A1 listed among the structural assumptions.
- **Old** (unique in its file):

  > The structural assumptions A1–A6 are not claimed as derived

- **New:**

  > The structural assumptions A2–A6 and the restriction to finite substrata are not claimed as derived

### E08b — `papers/Methodology.md:345`

- **Ledger row:** X-45. **Source:** as E08a.
- **Finding:** as E08a.
- **Old** (unique in its file):

  > A reader who rejects an assumption in A1–A6

- **New:**

  > A reader who rejects an assumption in A2–A6, or the restriction to finite substrata,

### E09a — `papers/Methodology.md:357`

- **Ledger row:** X-45. **Source:** X-45 correction (finite-only statement of the theorem's setting).
- **Finding:** the framework's setting asserted finite.
- **Old** (unique in its file):

  > The framework's setting is finite, and the gauge-classification theorem is what the finiteness buys

- **New:**

  > The gauge-classification theorem concerns a finite substratum, and it is what the finiteness buys

### E09b — `papers/Methodology.md:357`

- **Ledger row:** X-45. **Source:** as E09a.
- **Finding:** A1 presented as the framework's hypothesis.
- **Old** (unique in its file):

  > it is a statement of what the framework's finiteness hypothesis A1 makes available

- **New:**

  > it is a statement of what a finite substratum makes available

### E10 — `papers/Methodology.md:367`

- **Ledger row:** X-45. **Source:** X-45 correction ("the structural class A1–A6" -> "the class of such finite substrata"), applied to the constructive-OSR claim.
- **Finding:** A1 listed among the structural assumptions.
- **Old** (unique in its file):

  > the constructive-OSR claim is conditional on the structural assumptions A1–A6 and the nearest-neighbor premise, which are not themselves derived; the claim is "constructive OSR within the nearest-neighbor A1–A6 class,"

- **New:**

  > the constructive-OSR claim is conditional on a finite substratum, the structural assumptions A2–A6 and the nearest-neighbor premise, which are not themselves derived; the claim is "constructive OSR within the nearest-neighbor class of finite substrata satisfying A2–A6,"

### E11 — `papers/Methodology.md:369`

- **Ledger row:** X-45. **Source:** as E10.
- **Finding:** A1 listed in the class qualifier.
- **Old** (unique in its file):

  > which is why the A1–A6 qualifier is load-bearing

- **New:**

  > which is why the qualifier to finite substrata satisfying A2–A6 is load-bearing

### E12 — `papers/Methodology.md:517`

- **Ledger row:** X-01 (site owner Q3; not a pointer). **Source:** Methodology §3.1 definition (S, φ, V); no finiteness asserted.
- **Finding:** finiteness of the substratum asserted without scope; the type-level argument does not use it.
- **Old** (unique in its file):

  > The framework's substrate is the bijection on a finite set;

- **New:**

  > The framework's substrate is the bijection $\varphi$ on the total system $S$;

### B01 — `book/ch14-quantum-computing.md:160` = FULL:3760

- **Ledger row:** X-55. **Source:** X-55 correction (conditional statement about a finite substratum).
- **Finding:** A1 presented as a framework hypothesis.
- **Old** (unique in its file and in FULL.md):

  > (the bijection $\varphi$ acts on a state space, finite under A1, with classical probability

- **New:**

  > (the bijection $\varphi$ acts on a state space, which is finite for a finite substratum, with classical probability

### B02 — `book/ch14-quantum-computing.md:164` = FULL:3764

- **Ledger row:** X-55. **Source:** as B01.
- **Finding:** as B01.
- **Old** (unique in its file and in FULL.md):

  > the universe is, under A1, a deterministic finite system at the substratum level

- **New:**

  > the universe is a deterministic system at the substratum level, finite for a finite substratum

### B03a — `book/ch14-quantum-computing.md:184` = FULL:3784

- **Ledger row:** X-55. **Source:** as B01.
- **Finding:** as B01.
- **Old** (unique in its file and in FULL.md):

  > bijection and finite structures when A1 is posited

- **New:**

  > bijection, and finite structures for a finite substratum

### B03b — `book/ch14-quantum-computing.md:184` = FULL:3784

- **Ledger row:** X-55. **Source:** as B01 (parallel to E01).
- **Finding:** as B01.
- **Old** (unique in its file and in FULL.md):

  > the framework's axiomatic content concerns, under A1, finite physical structures

- **New:**

  > for a finite substratum, the framework's axiomatic content concerns finite physical structures

### B04 — `book/ch14-quantum-computing.md:262` = FULL:3862

- **Ledger row:** X-55. **Source:** as B01.
- **Finding:** as B01.
- **Old** (unique in its file and in FULL.md):

  > A1 would limit the total number of configurations.

- **New:**

  > A finite substratum would limit the total number of configurations.

### B05 — `book/ch18-beyond.md:20` = FULL:4751

- **Ledger row:** X-26. **Source:** X-26 correction (§18.7 finite-only, "for a finite substratum").
- **Finding:** A1 presented as a framework hypothesis.
- **Old** (unique in its file and in FULL.md):

  > Section 18.7 develops, under A1, the finite-information character

- **New:**

  > Section 18.7 develops, for a finite substratum, the finite-information character

### B06 — `book/ch18-beyond.md:22` = FULL:4753

- **Ledger row:** routed (S2-A review). **Source:** owner A4 decision (discrete lattice distinct from continuous space); S2-A A4 wording.
- **Finding:** the discrete lattice's global options listed as a continuous R^3; Klein-bottle identification not a translation quotient.
- **Old** (unique in its file and in FULL.md):

  > (whether the universe is topologically trivial $\mathbb{R}^3$, a 3-torus, a Klein-bottle quotient, or some other compact identification)

- **New:**

  > (whether the lattice is the infinite discrete lattice $\mathbb{Z}^3$, which is distinct from a continuous $\mathbb{R}^3$; a 3-torus quotient $\mathbb{Z}^3/P$; a Klein-bottle-type identification, which is not a quotient by translations alone; or some other compact identification)

### B07 — `book/ch18-beyond.md:226` = FULL:4957

- **Ledger row:** routed (S2-A review). **Source:** as B06.
- **Finding:** as B06.
- **Old** (unique in its file and in FULL.md):

  > But whether the lattice extends globally as $\mathbb{R}^3$, identifies as a 3-torus, has a Klein-bottle quotient, or admits some other global identification structure

- **New:**

  > But whether the lattice extends globally as the infinite discrete lattice $\mathbb{Z}^3$, the standard construction of A4, which is distinct from a continuous $\mathbb{R}^3$; identifies as a 3-torus $\mathbb{Z}^3/P$, a finite periodic quotient that A4 admits as a qualified case; has a Klein-bottle-type identification, which is not a quotient by translations alone and is not among the cases A4 admits; or admits some other global identification structure

### B08 — `book/ch18-beyond.md:230` = FULL:4961

- **Ledger row:** routed (S2-A review). **Source:** as B06.
- **Finding:** Klein-bottle quotient not a translation quotient.
- **Old** (unique in its file and in FULL.md):

  > (a 3-torus, a Klein-bottle quotient, or other compact identifications)

- **New:**

  > (a 3-torus, a Klein-bottle quotient, whose identification includes a parity-reversing map and so is not a quotient by translations alone, or other compact identifications)

### B09 — `book/ch18-beyond.md:36` = FULL:4767

- **Ledger row:** X-10. **Source:** X-10 (counting/maximal-entropy measure exists only on a finite carrier; finite scope as at ch14:272, Comp:122).
- **Finding:** maximal-entropy (counting) measure stated without finite scope.
- **Old** (unique in its file and in FULL.md):

  > the account reduces to the maximal-entropy measure posited in [Main §4.5]

- **New:**

  > the account reduces to the maximal-entropy measure of a finite representative posited in [Main §4.5]

### B10 — `book/ch18-beyond.md:162` = FULL:4893

- **Ledger row:** X-26. **Source:** as B05.
- **Finding:** as B05.
- **Old** (unique in its file and in FULL.md):

  > finite information under A1, the arrow of time

- **New:**

  > finite information for a finite substratum, the arrow of time

### B11a — `book/ch18-beyond.md:166` = FULL:4897

- **Ledger row:** X-26. **Source:** as B05 (removes "the hypothesis A1 of a finite substratum").
- **Finding:** A1 presented as a framework hypothesis.
- **Old** (unique in its file and in FULL.md):

  > The hypothesis A1 of a finite substratum has structural consequences

- **New:**

  > A finite substratum has structural consequences

### B11b — `book/ch18-beyond.md:166` = FULL:4897

- **Ledger row:** X-26. **Source:** as B05.
- **Finding:** as B11a.
- **Old** (unique in its file and in FULL.md):

  > Under A1 the universe is described by a finite configuration space $S$ with bijection dynamics $\varphi: S \to S$. Finiteness is not a calculational convenience but load-bearing under A1:

- **New:**

  > It is described by a finite configuration space $S$ with bijection dynamics $\varphi: S \to S$. Finiteness is then not a calculational convenience but load-bearing:

### B11c — `book/ch18-beyond.md:166` = FULL:4897

- **Ledger row:** X-26; X-20. **Source:** X-20 (NR) weaker sufficient condition; S2-C book parenthesis form (appC:104) verbatim.
- **Finding:** route stated to require finite S; Main §2.3 corollary (near-return) gives the conclusion under (NR).
- **Old** (unique in its file and in FULL.md):

  > The recurrence route in the framework's logic chain requires finite $S$.

- **New:**

  > In this exact-return form the recurrence route in the framework's logic chain uses finite $S$; the near-return condition of Chapter 1 §1.5, assumed in its place and not adopted, also gives the indivisibility conclusion (it concerns a time that need not be accessible and then has no finite-window test; for the selected update of Main §3.2 on $\mathbb{Z}^d$ no law that is not supported on periodic configurations is known to satisfy it).

### B12 — `book/ch18-beyond.md:168` = FULL:4899

- **Ledger row:** X-26. **Source:** as B05.
- **Finding:** A1 presented as a framework posit.
- **Old** (unique in its file and in FULL.md):

  > and under the finiteness posit A1 (Chapter 2 §2.4) it is finite.

- **New:**

  > and for a finite substratum it is finite.

### B13a — `book/ch18-beyond.md:170` = FULL:4901

- **Ledger row:** X-26; X-20. **Source:** as B11c.
- **Finding:** route stated to close without finiteness; the same paragraph and Main §2.3 give it under a revival (NR).
- **Old** (unique in its file and in FULL.md):

  > is load-bearing. Infinite hidden sectors would break the recurrence argument that drives recurrence-scale P-indivisibility; that route would close.

- **New:**

  > is load-bearing for that route's exact-return form. Infinite hidden sectors would break the finite-order argument that drives that form.

### B13b — `book/ch18-beyond.md:170` = FULL:4901

- **Ledger row:** X-26. **Source:** as B13a (scope to the update and prior named in the preceding sentence).
- **Finding:** as B13a.
- **Old** (unique in its file and in FULL.md):

  > so an infinite substratum removes this route rather than the framework's quantum representation.

- **New:**

  > so for that update and prior an infinite substratum removes this route rather than the framework's quantum representation.

### B14a — `book/ch18-beyond.md:172` = FULL:4903

- **Ledger row:** X-26. **Source:** as B05.
- **Finding:** A1 presented as a framework hypothesis.
- **Old** (unique in its file and in FULL.md):

  > The hypothesis of finite information (A1) is therefore neither a quantitative claim

- **New:**

  > Finite information is therefore neither a quantitative claim

### B14b — `book/ch18-beyond.md:172` = FULL:4903

- **Ledger row:** X-26; X-20. **Source:** as B11c.
- **Finding:** finiteness stated as a requirement; it is a sufficient condition.
- **Old** (unique in its file and in FULL.md):

  > It is a structural requirement for one particular route — the recurrence-based P-indivisibility result,

- **New:**

  > For a finite substratum it is a sufficient condition for one particular route — the recurrence-based P-indivisibility result in its exact-return form,

### B14c — `book/ch18-beyond.md:172` = FULL:4903

- **Ledger row:** X-26. **Source:** as B05.
- **Finding:** as B14a.
- **Old** (unique in its file and in FULL.md):

  > The substratum's finiteness is what makes this particular route to P-indivisibility available.

- **New:**

  > For a finite substratum, finiteness is what makes this form of the route to P-indivisibility available.

### B15 — `book/ch18-beyond.md:190` = FULL:4921

- **Ledger row:** X-26. **Source:** as B05.
- **Finding:** A1 presented as a framework hypothesis.
- **Old** (unique in its file and in FULL.md):

  > The recurrence theorem connects three structural features of the framework: substratum finiteness (the hypothesis A1, $|S| < \infty$),

- **New:**

  > The recurrence theorem connects three structural features of a finite model: substratum finiteness ($|S| < \infty$),

### B16a — `book/ch18-beyond.md:192` = FULL:4923

- **Ledger row:** X-26. **Source:** as B05.
- **Finding:** as B14a.
- **Old** (unique in its file and in FULL.md):

  > The hypothesis of finite information (A1) is therefore load-bearing for the recurrence route specifically,

- **New:**

  > Finite information is therefore load-bearing for the exact-return form of the recurrence route specifically,

### B16b — `book/ch18-beyond.md:192` = FULL:4923

- **Ledger row:** X-26; X-20. **Source:** as B11c.
- **Finding:** as B13a.
- **Old** (unique in its file and in FULL.md):

  > would remove the recurrence route rather than the framework's quantum representation.

- **New:**

  > would remove that exact-return form rather than the framework's quantum representation; the route then needs the near-return condition of Chapter 1 §1.5, assumed as a hypothesis and not adopted.

### B17 — `book/ch18-beyond.md:242` = FULL:4973

- **Ledger row:** X-80. **Source:** X-80 (finite-only); S2-A A4 qualified-case wording; Klein-bottle routed (S2-A review).
- **Finding:** realizing A1 presented as a framework aim; finite lattice not qualified per A4.
- **Old** (unique in its file and in FULL.md):

  > First, a compact identification can give a finite periodic lattice. With finitely many states per site and the specified finite-carrier dynamics, this is one way to realize A1 in a model.

- **New:**

  > First, a compact identification by translations can give a finite periodic quotient $\mathbb{Z}^3/P$, which A4 admits as a qualified case under the conditions on $P$ stated with each result that uses it; a Klein-bottle-type identification is not a quotient by translations alone and is not among the cases A4 admits. With finitely many states per site and the specified finite-carrier dynamics, a finite periodic quotient is one way to obtain a finite substratum in a model.

### B18 — `book/ch18-beyond.md:244` = FULL:4975

- **Ledger row:** X-80. **Source:** X-80 (finite-only).
- **Finding:** A1 presented as a framework hypothesis.
- **Old** (unique in its file and in FULL.md):

  > Second, A1 can also hold on a finite lattice region

- **New:**

  > Second, a finite substratum can also be obtained on a finite lattice region

### B19 — `book/ch18-beyond.md:260` = FULL:4991

- **Ledger row:** X-80. **Source:** X-80 (finite-only).
- **Finding:** as B18.
- **Old** (unique in its file and in FULL.md):

  > illustrate one way to model A1 under the conditions above

- **New:**

  > illustrate one way to model a finite substratum under the conditions above

### B20 — `book/ch18-beyond.md:288` = FULL:5019

- **Ledger row:** X-80. **Source:** X-80 (finite-only).
- **Finding:** as B18.
- **Old** (unique in its file and in FULL.md):

  > *The substratum is finite under A1.* Under A1 the framework's finite substratum (§18.7) would constrain

- **New:**

  > *A finite substratum bounds information content.* A finite substratum (§18.7) would constrain

### G01 — `book/glossary.md:105` = FULL:6596

- **Ledger row:** X-20. **Source:** X-20 ("or (NR)", as M:131); S2-C book parenthesis form verbatim; "assumed as a hypothesis and not adopted" as S2-C ch01:179.
- **Finding:** glossary lags M:131 "or (NR)" (owner Q3, #1169 c.7035888700).
- **Old** (unique in its file and in FULL.md):

  > uses a non-permutation rooted map and a finite return ([Main §3.4])

- **New:**

  > uses a non-permutation rooted map and a finite return or the near-return condition (NR), assumed as a hypothesis and not adopted (it concerns a time that need not be accessible and then has no finite-window test; for the selected update of Main §3.2 on $\mathbb{Z}^d$ no law that is not supported on periodic configurations is known to satisfy it) ([Main §3.4])
