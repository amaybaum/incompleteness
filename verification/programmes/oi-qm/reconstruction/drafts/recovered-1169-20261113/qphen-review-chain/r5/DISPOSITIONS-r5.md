# QPHEN Phase 1 r5: dispositions of `review/REVIEW-PHASE1-r4.md` (`755c3af0…`)

## Scope and standing

- Paper only and model-written. There are no repository, git or GitHub writes.
- No computation is run on any OI mechanism. The one new check, `review/probes/p9_r5_symplectic_detector.py`, is an
  exact check of a paper claim on generic objects ("Allowed: generic checks", #1210 c.6739250392, owner, 2026-11-09).
  It imports no earlier probe.
- Q-C2-1's D19–D23 remain separate. No freeze, dispatch, construction or implementation approval follows from this
  revision.
- **Inputs.**
  - The r4 review, sha256 `755c3af0ae603b0ebeb06d5853c80357aba50a3634d152c66456e62e2f86a987` (verified before
    reading), verdict REVISE (narrow), and its probe `p8_r4rev_membership.py` (`810131733cd34180…`), whose output
    `p8_r4rev_membership.out` (`a511a94c…`) was read.
  - The owner's summary-scope instruction (every conclusion in a summary or dependency table carries the scope and
    status of its supporting proof or counterexample), as relayed in `R4-REVIEW-ADDENDA.txt` and in the r4 review.
  - The owner rules still in force (last section).
- **The r4 texts** are copied unchanged into `r4/`:

  | file | sha256 |
  | --- | --- |
  | `QX3-ANTIBUNCHING.md` | `f372cef7d3baad57cb4cddd72a710bb1077a1235299fd34283fb5ca29b6c5282` |
  | `QX4-INCOMPATIBILITY-LG.md` | `2765e6f7cb06e4d6bbd60645616abd70588ca8b739235181845fed3cde6f97c4` |
  | `QX6-BELL-CHSH.md` | `5c7ab0cb6efce8e33b23daad29fd20076e6cceeb1fe83d54e11b68c6d6ef774a` |
  | `SHARED-MECHANISM.md` | `23ec1ef19be8b2dd4aa77d59926853fd00a125ee552746db14d83203b366fd11` |
  | `DISPOSITIONS-r4.md` | `a886e40d0311849b19480ef954e17cc1b50b2b0e804486af8c44ee95f1c67c5d` |

  These match the hashes the r4 review lists. `DISPOSITIONS-r4.md` is a record and is not edited.

## The new check

`p9_r5_symplectic_detector.py` (pure Python, integers mod 2; run with `python3 -I` from a separate directory; exit 0;
13 of 13 checks pass; output in `p9_r5_symplectic_detector.out`). Coordinates `(c, x, m, m′)` of `F_2⁴`, symplectic
pairs `(c, x)` and `(m, m′)`. "Interacts only when occupied" is formalized as: the identity on the branch `c = 0`.
"Records occupation" is: some point with `c = 1` has a meter slot changed. Exhaustive results:
- `|GL(4, F_2)| = 20,160`; `|Sp(4, F_2)| = 720`; affine-symplectic maps `720 × 16 = 11,520`; affine bijections
  322,560.
- Affine-symplectic maps that are the identity on `c = 0` and record occupation: **0**. Affine bijections (not
  necessarily symplectic) that do both: **6**, exactly the maps `M = I + d e_cᵀ` with `d_c = 0` and a meter
  component in `d`. This reproduces p8 (6) independently.
- The structure of the hand proof: identity on `c = 0` forces `b = 0`, and with symplecticity `d ∈ {0, e_x}`.
- The copy coupling is a linear bijection, not symplectic, the identity on `c = 0`, and records occupation. The
  reciprocal coupling is symplectic, records occupation, and is not the identity on `c = 0`.

The three-line argument was also checked by hand: `ω(d, e_x) = d_c`, `ω(d, e_m) = d_m′`, `ω(d, e_m′) = d_m`.

## Blockers

| finding | change made (r5) |
| --- | --- |
| **B1** (Q4-D3: affine but not symplectic) | **SHARED Q4-D3** is restated: "… lies outside the class of affine maps of `F_2⁴` (not necessarily symplectic)". Its membership line adds "The copy coupling is not symplectic for the pairs `(c, x)` and `(m, m′)`" (p8 (6); p9), and a line "The claim's affine-symplectic form holds (Q4-P19)". **New entry SHARED Q4-P19, proved** [A: the review's three-line argument, checked by hand; X: p8 (6) and p9, two separately written probes, exhaustive over the 720 × 16 affine-symplectic maps]: an affine-symplectic map of `F_2⁴` that is the identity on `c = 0` changes no meter slot on `c = 1`, so every affine-symplectic coupling that records occupation acts on its silent branch. The 0 / 11,520 and 6 counts are verified independently (above). **At QX-4's body site** where "affine" is read in A4.1's affine-symplectic sense, **QX-4 R4.9** reads "the copy coupling … is affine but not symplectic, and the reciprocal coupling … is affine and symplectic (SHARED Q4-P15)" and adds "Every affine-symplectic coupling that records occupation acts on its silent branch (SHARED Q4-P19)". **SHARED Q4-P15**, which supports R4.9, states the same symplecticity facts, cited to p8 (6) and p9. **SHARED §7** gains rows for the r4 review with p8, and for p9 (§A.42 item 8) |
| **B2** (QX-3 §7 item 5 necessity) | **QX-3 §7 item 5**: "therefore need non-uniform laws, mixtures, or non-affine detector functionals", matching A3.1(a)'s two hypotheses. Q3-P11 is unchanged |

## Must-fix nits

| finding | change made (r5) |
| --- | --- |
| **N1** (§8 membership rule reversed) | **SHARED §8 rules**: "Where membership cannot be shown, the refuted claim is restated over a class the counterexample belongs to, and the original, narrower claim is listed as open." **Q4-D1**'s header reads "*Claim, as restated:*", and its sub-bullet label "*Narrowing.*" reads "*Restatement.*" (the same inversion). DISPOSITIONS-r4 N6's wording is in a record and is not edited |
| **N2** (`K₃ ≤ 1` "only at (a) and (b)") | **QX-4 A4.1(c)**: the first bullet adds "In the Clifford class, integrality and the Lüders bound (§2) give `K₃ ≤ 1` at any number of modes", so the mixture bullet's "still holds" has its antecedent; the sentence in question reads "In the affine-symplectic class with A4.1's read model, the bound `K₃ ≤ 1` itself is established only at the scopes in (a) and (b)". **QX-4 §7 item 2** is qualified the same way and adds "in the Clifford class with pure stabilizer preparations, or mixtures of them, and Lüders `Z` reads it holds at any number of modes (A4.1(c))". Both now agree with Q4-P3 |
| **N3** ("not sufficient" without its condition) | **QX-6 A6.2's title** adds "(under A6.1's hypotheses, including the design assumptions (L′) and (R))". **SHARED §2, M12 × QX-6** reads "r (QM-matching settings with stabilizer pairs; not sufficient under A6.1's hypotheses, including the design assumptions (L′) and (R); A6.2)" |
| **N4** (§3 "Counting") | **SHARED §3 "Counting"** reads "needs the following, each under the condition stated (§8.4)", and each item carries its condition: M12 for QX-4c with stabilizer preparations (A4.1(c)) and QX-6 with stabilizer pair states (A6.2), open for QX-1, QX-5 and QX-7, whose support is D; the cross-wing response (M19) with the no-signalling mask (M20), from A6.1 [A] in contrapositive (under (D) and (MI), `|S| > 2` needs a failure of (L′) or (R)) together with QX-6 §3.2 (the design excludes failures of (L′) and insufficient separation, leaving a short cross-wing coupling path, for which H-Bell is the candidate), and complete-history no-signalling from QX-6's Level-2 witness; M18 and M14 by the protocols' definitions. **SHARED §8.4** gains a proved entry (the conditional necessity statements, with Q4-P3, Q6-P4, Q6-P2) and an open entry (M12's necessity for QX-1, QX-5 and QX-7) |
| **N5** (W2's class in summaries) | **QX-3 §2 "Consequence"**, **QX-3 §7 item 7** and **SHARED §5's QX-3 row** state W2's class as the row does: classical fields under square-law, independent detection, and particle models with no wave-like phase variable. Further sites found in the own pass are listed below |
| **N6** ("must keep an outcome-independent kick") | **SHARED T2**: "The routing coupling must act on its silent branch (`K_null ≠ id`), for example by keeping the reciprocal, outcome-independent kick". **QX-4 A4.4 "Consequence", last bullet**: "… with a coupling that acts on its silent branch (`K_null ≠ id`), for example by keeping the reciprocal, outcome-independent kick that A3.2's control requires from QX-3's side". The old closing sentence "This is the constraint A3.2 states from QX-3's side" equated the weaker requirement with A3.2's reciprocity control and is replaced by that clause. No §8 entry carries the stronger form. Within the affine-symplectic class the stronger form is Q4-P19 (B1) |
| **N7** (`A_4` arm) | **QX-4 §5, `A_4`**: "`K₃ ≤ 1` is not expected" becomes "`A_4`'s value is open (Q4-O6)" |
| **N8** (D labels on probes) | Relabelled X, with "computation-supported" where the ledger entry is: **QX-3 A3.1** heading "P2 (X)"; **QX-4 A4.1(b)** "[X: the reviewer's exhaustive finite scan, P3, reproduced by `p6_r3rev_lg.py` (5b); computation-supported]", and its closing line "not a theorem beyond that scope", so that its status matches Q4-P2 (proved, computation-supported); **QX-4 A4.1(c)** "(P5-LG, X, exact; computation-supported)"; **QX-6 §2** "P1 (X)" and "[X, exact: reviewer P1 and P4(3); writer's probe P5-GHZ; computation-supported]"; **QX-6 A6.1 checks** "(probe P5-A61, X, reproduced by `p6_r3rev_a61.py`; exact, the random-construction check a finite sample; …)". "Off `main` (D)" stays in the reference tables as provenance |

## Precision nits

| finding | change made (r5) |
| --- | --- |
| **N9** ("probes P1–P6") | Applied per file, so that each §0 names the probes that file cites. **QX-4 §0**: "P1–P7". **SHARED §0**: "P1–P9", since SHARED cites P7, p8 and p9. **QX-3 §0 and QX-6 §0** keep "P1–P6": QX-3 cites P2, P5 and P6, and QX-6 cites P1, P4, P5 and P6. **SHARED §8's X rule** names the authors of P8 (reviewer) and P9 (writer) |
| **N10** (`⊥ ↦ ±1` "keep (R)") | **SHARED Q6-P10**: "A6.1 holds with `⊥ ↦ +1` in (R) replaced by any fixed local rule: the proof is unchanged, since steps 5–6 use only that each outcome is a function of its readout region." **QX-6 ABL-BOT** says the same for its two rules |
| **N11** (R6.4 type) | **QX-6 R6.4's type column** begins "design assumption of the Bell test (A6.1 (L′)), not a consequence of OI;", as R6.2's does for (R) |
| **N12** (single-probe X entries) | **SHARED Q3-P6a** cites `p8_r4rev_membership.py` (8); **Q4-P7** and **Q4-D1**'s counterexample cite `p8_r4rev_membership.py` (5). The §7 row for p8 records these reproductions |

## Optional nits

- **Unwrapped §0 lines** (QX-4 §0, QX-6 §0): rewrapped. In QX-4 the sentence was edited for N9 in any case.
- **§A.31 method notes** ("because that reading favours the framework"): no change, as the review allows; they are
  outside §A.32's `papers/` scope.
- **DISPOSITIONS-r4 line 24**: that file is a record and is not edited. The summary-scope check of this revision
  covers every summary site (next section).

## The summary-scope pass over all four specifications

After N2–N8, every summary-level statement was compared with its supporting entry: the §0 standing blocks, the
witness tables and their "Consequence" paragraphs, the requirement tables' status and type columns, the derivation
titles, the arm and ablation tables, the decision trees, the obstacle lists, the ladder mappings, the owner
questions, SHARED §§1–5 (capabilities, the matrix, the minimal set, the tensions and controls, the dependency
proposals) and SHARED §8.4. Mismatches found beyond the review's list, each a site of the same kind as N2, N3, N5 or
N8, are fixed:

| site | as stated (r4) | supporting entry | change (r5) |
| --- | --- | --- | --- |
| QX-3 §6, `C-SURVIVAL` branch | "informative at classical-field scope" | W2 row: also phaseless particle models (N5) | "informative at W2's scope (§2)" |
| QX-3 §8 Level 2 | "if the owner accepts the classical-field class (Q3-1)" | as N5 | "if the owner accepts W2's class (Q3-1)" |
| QX-3 §9 Q3-1 | "excluding classical fields under square-law detection (W1/W2)" | as N5 | "excluding W2's class (classical fields under square-law, independent detection, and particle models with no wave-like phase variable; §2)" |
| QX-4 §5 ABL-G | "`≤ 1` within A4.1's scopes" | after N2, A4.1(c) also gives a Clifford-class Lüders bound at any number of modes, which is not construction B's read model | "`≤ 1` at A4.1(a)–(b)'s scopes with A4.1's read model" |
| QX-6 §6 ABL-NL | "`|S| ≤ 2` (A6.1)" | Q6-P10: conditional on (L′) and (R) (as N3; owner requirement 1) | "(A6.1, under its hypotheses, including the design assumptions (L′) and (R))" |

Checked and left unchanged, because scope and status already match:
- QX-3: §2's witness table; A3.1(a)–(d) and its Scope line; A3.2; the coherent-mixing paragraph; §5's arms and
  ablations (open, Q3-O6, except ABL-ROUTE's values, Q3-P7); §6's other branches (`P-VOID` and `P-NO-FRINGES` speak
  of W1 alone, correctly); §7 items 1–4, 6 and 8; §8 Levels 1, 3 and 4.
- QX-4: §2's predictions and witness table; R4.3–R4.10; A4.1(a); AW-QX4-1 (affine scope, record only); A4.2; A4.3;
  A4.4's hypotheses; §5's `B_4-nat`, `B_4-C`, ABL-SA1c, ABL-NULL and ABL-T1 rows; §6; §7 items 1 and 3–8; §8.
- QX-6: §2's witness table and the stabilizer statement; §3.2; A6.1's header, Scope and "Consequence for the
  ablations"; A6.2's body; A6.3; A6.4; §6's `A_6` and `B_6-loc` (whose definition carries A6.1's hypotheses);
  ABL-C; §7 (the review found it consistent; `B_6-loc` is defined under A6.1's hypotheses); §8 items 2 and 6; §9.
- SHARED: §1 (M2, M3, M14, M15, M16, M19, M20); the §2 cells other than M12 × QX-6; §3's "Epistemic restriction"
  (AW-QX4-1 described as a record, which is its status) and "Cross-wing dynamics"; H-SDC; §4 T1, T3–T9 and the
  controls list (its `K₃ ≤ 1` item is stated under SA-1(c) or environment supplies, which is the affine read model);
  §5's QX-4 and QX-6 rows; §8.4's other entries; §9.

A register scan of every added line (§A.32, §A.33) finds no history phrase, reader instruction or caps emphasis; the
all-caps tokens are identifiers (file names, `NCONS`, `MECH-OPEN`, CHSH).

## The owner rules still in force

| rule | status in r5 |
| --- | --- |
| The three-column restrictions table; column (iii) never supports column (ii) | SHARED §9 unchanged |
| A6.1 is conditional on (L′)/(R), which are design assumptions | kept at every A6.1 citation; added at A6.2's title, M12 × QX-6, R6.4's type column, ABL-NL, and §3 "Counting" |
| Every disproved entry carries a membership line | all 11 do; Q4-D3's adds non-symplecticity (B1) |
| Exact checks on generic objects are labelled; a probe-only result is marked computation-supported | N8, N12; Q4-P19 has a paper proof and two probes, so it is X without that tag |
| No computation on an OI mechanism | p9 runs on generic affine maps of `F_2⁴` only |
| No implied D19–D23 decisions, freeze, dispatch or construction | none added; all rules remain outlines |

## Changes not traced to a review finding

No substantive change. The following housekeeping follows from the instruction to revise the specifications in place
as r5 and to keep r4 under `r4/`:
1. Titles change from "(draft r4)" to "(draft r5)"; the cross-references "§0 (r4)" and "(r4) specifications" change
   to r5.
2. The §0 "Revisions" pointers name `r4/` and `DISPOSITIONS-r5.md`.

The own-pass changes above are traced to the owner's summary-scope instruction, and the §7 reference rows to B1 and
N12 under §A.42 item 8.

## Refusals and deviations

- **None refused.**
- **B1.** The affine-symplectic form is entered as proved (Q4-P19), not open, since the argument was verified by hand
  and by an independent exhaustive probe.
- **N9.** Applied per file rather than as one range, for the reason given.
- **N6.** The QX-4 A4.4 closing sentence referring to A3.2 is reworded with the fix, since it equated the weakened
  requirement with A3.2's reciprocity control.

## r5 file hashes (sha256)

| file | sha256 |
| --- | --- |
| `QX3-ANTIBUNCHING.md` | `e231a795508769cec7645f05931b1ce04e418bbd69acd8802f794a0bec8add71` |
| `QX4-INCOMPATIBILITY-LG.md` | `7f4cd21d02a0dbf7946c4d481c6140f7e3c6df053a5096b8fd589de123a7b5a5` |
| `QX6-BELL-CHSH.md` | `9e9c0d02c48dfc748baa7fade7a271c938e8ae817457ec635a3076cec774e4ea` |
| `SHARED-MECHANISM.md` | `a72067015789371a087517d92f71a5fcc654770d1d3f105e217eda6fcba2cc4d` |
| `review/probes/p9_r5_symplectic_detector.py` | `47cd22cc6cdd490430147f109a756caf4b0c4ab5da9ac0b2df4b7539dbfbc53f` |
| `review/probes/p9_r5_symplectic_detector.out` | `de508afb37f5de6f7c3e2ae3451090a105a205a7792559e32f86feecc7caa96d` |
