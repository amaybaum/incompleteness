# SC-38: probe and evidence statements (PR-F, part)

Base: `main` at `0d917665`. Findings: CON-25 / R-03 / OD-7, CON-24 / R-04 / OD-10 and CON-26 / R-33, from
`FINDINGS.md` on `audit/intro-corpus-20261026` at `16fc745d` and the consolidated audit on
`draft/oi-introductory-paper-20261025` at `9dc2b069`. Line numbers are those of the base.

Every verdict below rests on `sc38_exact.py` in this directory, run as `python3 -I sc38_exact.py`, which
decides each one in exact arithmetic: Fractions for probabilities, and, for information quantities, an exact
vector of rational coefficients on log2 of primes, which is zero iff every coefficient is zero (the logarithms
of distinct primes are linearly independent over Q). A strict sign is decided by mpmath interval arithmetic
on that exact vector, and an undecided interval fails the check. Each section carries a countercontrol. The
retained output is `sc38_exact.out`: 50 PASS lines, `ALL CHECKS PASS`, about 20 s.

## Per claim

### C-1. CON-25 / R-03: the readback lemma's probe (Main:170)

- **Original.** Main:170: "(Certified exactly on gap families, the revival family, and a small-gap parametric
  family, with the coin silent, in `c4_backflow_probes.py`.)"
- **Defect.** The probe builds `Fraction` laws and computes the gap term p₀δ² exactly, but accumulates the
  conditional mutual information as `float(p)*log2(float(...))` (line 23), returns the bound as
  `float(best)/LN2` (line 43) and asserts with tolerances 1e-12 and 1e-9 (lines 52, 63, 97, 129). It covers
  named families, not a class. "Certified exactly" overstates floating-point evidence on instances.
- **Correction.** Main:170 now reads "(Checked on a gap family, the revival family and a small-gap parametric
  family, with the coin silent, in `c4_backflow_probes.py`: the laws and gaps in exact rational arithmetic, the
  information quantities and the inequality in floating point.)" The probe is unchanged. Making it exact was
  possible (section B of `sc38_exact.py` does it), but the lemma is proved on paper. The paper's annotation
  therefore describes the probe it cites, and the exact instance check is retained here as evidence.
- **Evidence level.** The lemma is a paper proof (Pinsker plus the triangle inequality). The instances hold
  exactly: Q1 I = 1 bit, p₀δ² = 1/4; Q2 I = 2/3 bit, p₀δ² = 1/6; Q5 p₀δ² = 1/64 with I irrational and the
  inequality strict; the coin's target product law, checked directly rather than through the dilation, has
  I = 0 and no gap at every order (B1–B4, controls B5–B6).
- **Downstream.** Ledger entry `MAIN:L-accessible-conditional-memory-from-readback` fingerprints the statement
  at Main:167, which is unchanged; its level P is unchanged. No mirror carries the sentence.

### C-2. Other probe claims labelled exact or certified over floating-point evidence (the grep)

| Site | Original | Defect | Now |
|---|---|---|---|
| Main:616 | "(All clauses certified exhaustively — … and the predictive floor $\log_2 \|\mathrm{tails}_t\| \geq I(X_{<t}; X_{>t} \mid X_t)$ — over all 1{,}464 $\varphi$-realizations … under two priors, 2{,}928 instances, exact: `purification_probes.py`.)" | Clause (6) is computed with `float`/`math.log2` and tolerance 1e-9 (`purification_probes.py` lines 139, 146). | "…2{,}928 instances, in exact rational arithmetic except the predictive floor, which is checked in floating point: `purification_probes.py`.)" |
| Main:606 | "(All three certified over every bijection at … under the uniform prior — 1{,}464 cases — in `memory_probes.py`.)" | Clause (c) is floating point with tolerance 1e-12 (`memory_probes.py` lines 78–80). | "(All three checked over every bijection … in `memory_probes.py`, (a) and (b) in exact rational arithmetic and (c) in floating point.)" |
| Main:620 | "…with the bound $\log_2\|\mathcal{C}_H\| \geq I^*$ saturated by realizations that attain it; both are certified by exhaustive enumeration in `primitive_probes.py`." | The (C3) half is floating point (`primitive_probes.py` lines 74, 99). | "…both are checked by exhaustive enumeration in `primitive_probes.py`, the first in exact rational arithmetic and the second in floating point." |
| `papers/main_repro/README.md`:8 | "ALL PASS (exact enumeration)" | `minimal_model.py` uses numpy floats and `allclose`. | "ALL PASS (enumeration of all twelve states, floating point)" |

The conclusions all hold exactly: D1–D5 re-derive them, over the same exhaustive sets.

- **The quantity `primitive_probes.py` computes.** It is the per-order maximum max_k M_k, with
  M_k = I(X_<k; X_{k+1} | X_k), not Main's I* = sup_t I(X_<t; X_>t | X_t). At horizon 3 the two coincide exactly
  on every gap realization at (2,2), (2,3) and (3,2): 16, 648 and 672 realizations (D1i).
- **The (C3) bound.** max_k M_k ≤ log2|C_H| holds on all 16, 648, 672 and 39,168 gap realizations at (2,2),
  (2,3), (3,2) and (2,4). Saturation is attained exactly, at (2,2) on all 16 and at (3,2) on 384 of 672.
- **Gap and memory.** The gap and max_k M_k > 0 agree on every bijection at the three sizes Main:612 names.
- **The memory theorem's clause (c)** holds on 24, 720 and 720 bijections.
- **The predictive floor** holds on all 14, 97 and 149 laws.
- **Must-fail controls (D1c, D4c, D5c).** Each bound, tightened (to 1/2 bit for D1, or by 1/2 bit for D4 and
  D5), is violated at every size. The exact decision therefore detects violations and is not vacuous.

The edits correct the evidence label only, and each claim stands. Main:620's own wording is SC-40's (see
Cross-unit dependencies).

Output strings of the probes, where they claimed certification over a floating-point step:

- `c4_backflow_probes.py`:131 "readback lemma certified" became "checked";
- `primitive_probes.py`:100 "=> certified: … log2|C_H| >= I*" became "=> checked (floating point): … log2|C_H|
  >= max_k M_k";
- `memory_probes.py`'s header "Certifies" became "Checks".

SC-40 edits none of these files. The exact clauses' "certified" strings (`primitive_probes.py`:87, :118) are
left.

Checked and left unchanged, because the label is accurate:

- `tdilate_probes.py`, Main:208: sympy, exact.
- `chirality_grading_probes.py`, at Main:212, SM:535, SM:543, ch05:155 and FULL:1484: the entries are Gaussian integers, so the elimination is exact.
- `c1_cp_scope_probes.py`, Main:324 and :330: Fractions and an exact Q(√2) class.
- `intervention_probes.py`, Main:478: Fractions.
- `lg_comb_probes.py`, Main:480: Fractions.
- `review4_probes.py` P-F and P-G, Main:514, :528 and :728: Fractions.
- `nogo_probes.py`, Main:556: exact Q(√3); floats are used only to print.
- `review3_probes.py`, Main:76, :80 and :172: the product law is asserted exactly first, which gives I = 0.
- `primitive_probes.py` (A), Main:74: exact.
- Main:78 and :612 say "confirms", which does not claim exactness.

Main:516 ("Certified exactly on P-indivisible targets … (full-joint equality in exact rational arithmetic;
permutation control silent)") is also left unchanged. Its parenthetical confines the exactness to the
full-joint equality, which is exact, and the probe's floating-point capacity check (P6) is not what it cites.

### C-3. CON-24 / R-04 / OD-10: "minimal" as a size label

- **Original.**
  - Main:178: "### 2.4 Explicit Construction: A Minimal Model".
  - ch01:273 and FULL:617: "The minimal such game is the coin-and-die model of §1.5 dealt onto a table."
  - The same label on the same six-hidden-state model at ch01:135 and FULL:479 ("**A worked minimal
    model.**"), and at Explainer:725 ("the minimal-model ancestors of antimatter").
  - `papers/main_repro/README.md`:8: "§2.4 minimal model".
- **Defect.** As a size claim, "minimal" is false, and no measure is stated that would make it true.
  - A two-hidden-state model (h = 1 flips x, h = 2 fixes it) already gives T(1,0) = ½J and T(2,0) = I, with no
    stochastic divisor (A3, A3').
  - A three-hidden-state model (h = 1 flips x; h = 2, 3 swap) reproduces every number of Main §2.4: T(1,0),
    T(2,0) = I, Λ(2,1) with entries −1, and the conditionals 1 and 1/3 (A2).
  - With one hidden value every T(k,0) is a permutation matrix (A5).
  - The ch01:273 sentence is also inexact as an identification. The card game swaps the hole card and one burn
    card, so it has two hidden values and T(1,0) = ½J (A4). That is not the coin-and-die model's T(1,0).
- **Correction.** No minimality claim, following OD-10's recommendation.
  - Main:178 is now "### 2.4 Explicit Construction: A Six-Hidden-State Model".
  - ch01:135 and FULL:479 are now "**A worked six-hidden-state model.**".
  - ch01:273 and FULL:617 now read "A small such game deals the write-then-read mechanism of the coin-and-die
    model of §1.5 onto a table, with one burn card in place of the die."
  - Explainer:725 now reads "toy-model ancestors".
  - The `main_repro` README line is now "§2.4 six-hidden-state model". The script name `minimal_model.py` is
    an identifier and is kept.
- **Evidence level.** Exact (A1–A6). The model's own numbers are unchanged.
- **Downstream.** No anchor links to the old Main heading, and no other site carries "minimal model".

### C-4. CON-26 / R-33: the fixed-dimension count (Main:610; FINDINGS cites it as Main:594@eae01647)

- **Original.** Main:610: "At $(n_V, |\mathcal{C}_H|) = (2,3)$ the two agree for one of fifteen distinct
  processes with $M_t > 0$, with residuals up to $0.667$ bits (`memory_probes.py`); the agreeing process is
  the one with $H(X_{<t} \mid X_t, X_{t+1}) = 0$, and each residual equals that entropy by the identity
  above."
- **Defect.**
  - **What the probe groups by.** `memory_probes.py` grouped realizations by the t = 2 next-step conditionals
    alone, not by process. One such group holds two distinct laws of (X₀..X₃) (C4), so "fifteen distinct
    processes" miscounts.
  - **What the sentence leaves out.** It stated neither the prior that generates the processes nor t.
  - **The audit's figure.** B4's "2 of 16 over arbitrary priors" counts by law. A prior does not change the
    count: by the Remark's own identity, I(X_<t;H_t|X_t) − M_t = H(X_<t|X_t,X_{t+1}) for every bijective
    completion. The residual is therefore a function of the law.
- **Correction.**
  - **Source.** `memory_probes.py`'s `signature` now returns the exact law of (X₀..X₃). The probe prints "2
    of 16 laws of (X0..X3)" and still passes. Its float attainment test and its fail condition are unchanged.
  - **Main:610.** It now reads: "At $(n_V, |\mathcal{C}_H|) = (2,3)$ and $t = 2$, the uniform prior on
    $\mathcal{C}_V \times \mathcal{C}_H$ gives sixteen distinct laws of $(X_0,\ldots,X_3)$ with $M_t > 0$, and
    $M_{\mathrm{det}} = M_t$ for two of them, with residuals up to $2/3$ bit (`memory_probes.py`). The agreeing
    laws are those with $H(X_{<t} \mid X_t, X_{t+1}) = 0$, and each residual equals that entropy by the identity
    above, so it is the same under every hidden prior that realizes the law."

    "Process" became "law of $(X_0,\ldots,X_3)$" because the count depends on the horizon (SC-38 review B1).
    It is 16 laws (2 attaining) for (X₀..X₃), and 18 (2 attaining) for every horizon K = 4, …, 12, which
    covers the full process of these periodic permutations (C8).
- **Evidence level.** All exact:
  - the identity on all 720 realizations (C1);
  - 16 processes by law, 2 attaining (C2);
  - the probe's old grouping reproduces 15 and 1 (C3);
  - the merge (C4);
  - the maximal residual is exactly 2/3 bit (C5);
  - the attaining laws are exactly those with H(X_<2|X_2,X_3) = 0 (C6);
  - the horizon dependence, 16/2 at horizon 3 and 18/2 at K = 4..12 (C8);
  - a must-fail control: the identity with H(X_<2|X_2) in place of H(X_<2|X_2,X_3) fails on 648 of 720
    realizations (C7).

  This agrees with the audit's independent exact re-derivation (`evidence/scripts/E2_memory_exact.py` on the
  audit branch), which is credited for priority. The present script shares no code with it. CON-26 is resolved.
- **Downstream.**
  - The Remark's conclusion, that the fixed-dimension identity fails at every hidden dimension, rests on the
    identity and the i.i.d.-coin example. It is unchanged.
  - `verification/lean/hidden_memory_probe.py`:279–280 printed "The variational identity M_det = M_t remains
    OPEN and is FALSE in its fixed-hidden-dimension reading (memory_probes.py)." This contradicted the Remark,
    which shows the identity false in general at every hidden dimension. The two print strings now read "The
    variational identity M_det = M_t is false in general at every hidden dimension: every bijective completion
    has I(X_<t; H_t | X_t) = H(X_<t | X_t) (Main §3.4; memory_probes.py)." Only the strings changed. The
    probe's output before and after differs only in those two lines, and it passes.
  - The Introduction's L185 ("the fixed-dimension form is false") is left to r32. The flat statement is
    supported: R-33's alternative, "keep the flat statement once Main carries an exact certificate", now holds
    through this check, and the cited probe's count is corrected.

## Site table

| Site | Was | Now | Source |
|---|---|---|---|
| Main:170 | Certified exactly … in `c4_backflow_probes.py` | Checked …; laws and gaps exact, information quantities in floating point | CON-25 |
| Main:178 | 2.4 … A Minimal Model | 2.4 … A Six-Hidden-State Model | CON-24 |
| Main:606 | All three certified … | All three checked …, (c) in floating point | grep (C-2) |
| Main:610 | one of fifteen … up to 0.667 bits … the agreeing process is the one | (2,3), t = 2, uniform prior: sixteen distinct laws of (X₀,…,X₃), $M_{\mathrm{det}} = M_t$ for two … up to 2/3 bit … the agreeing laws; prior-independent | CON-26; review B1 |
| Main:616 | … exact: `purification_probes.py` | … exact except the predictive floor, in floating point | grep (C-2) |
| Main:620 | both are certified by exhaustive enumeration | both are checked …, the second in floating point | grep (C-2) |
| ch01:135, FULL:479 | A worked minimal model | A worked six-hidden-state model | CON-24 (propagation) |
| ch01:273, FULL:617 | The minimal such game is the coin-and-die model … dealt onto a table | A small such game deals the write-then-read mechanism … with one burn card in place of the die | CON-24 |
| Explainer:725 | minimal-model ancestors | toy-model ancestors | CON-24 (propagation) |
| main_repro/README:8 | §2.4 minimal model; (exact enumeration) | §2.4 six-hidden-state model; (enumeration of all twelve states, floating point) | CON-24, grep |
| memory_probes.py | grouping by t = 2 conditionals; "1 of 15"; header "Certifies" | grouping by law of (X₀..X₃); "2 of 16 laws of (X0..X3)"; header "Checks" | CON-26 (source); review O7 |
| c4_backflow_probes.py:131, primitive_probes.py:100 | "certified" in output strings over floating-point steps | "checked"; primitive also names max_k M_k | review O7 |
| verification/lean/hidden_memory_probe.py:279–280 | "M_det = M_t remains OPEN and is FALSE in its fixed-hidden-dimension reading" | "is false in general at every hidden dimension: every bijective completion has I(X_<t; H_t \| X_t) = H(X_<t \| X_t)" (strings only) | review O4 |
| LEDGER.json | `MAIN:T-canonical-predictive-quotient-purification-ingredient` fingerprint 8b180e8ae437af19 | 9f4f8626d7c3bc87; same ID, level P and delta unchanged (only the evidence parenthetical changed) | coverage |

Regenerated: `papers/Main.{tex,pdf}` (96 pages), `papers/Explainer.{tex,pdf}` (70 pages) and
`book/The-Incompleteness-of-Observation-FULL.{tex,pdf}` (558 pages). The page counts equal the base's, and the
median characters per page are 3174, 2835 and 2962.

## Re-grep (papers/*.md, book/*.md, papers/main_repro/README.md)

- **Zero remaining.** "Certified exactly on gap" 0, "minimal model" (any case) 0, "minimal-model" 0, "minimal
  such game" 0, "one of fifteen" 0, "0.667" 0, "1 of 15" 0, "exact: `purification" 0.
- **Surviving legitimate uses.** "certified exactly" 13, all over exact probes (listed in C-2: Main:208, :212, :324, :330, :478, :480, :516, :528, :556; SM:535, :543; ch05:155; FULL:1484), and Main:250's "not exactly certified". "exhaustive"
  in its correct senses (Main:74, :286, :320, :774; Methodology; Structure:1256; Substratum:269), and the
  chess "exhaustively analyzable" (ch01:267 and :288, with their FULL mirrors).
- **New labels.** "Six-Hidden-State" 1 (Main); "six-hidden-state" 3 (ch01, FULL, main_repro README).

## Claims made conditional or removed

None is made conditional. Removed: the size claim "minimal", at its four sites and their mirrors, and the
identification of the card game with the coin-and-die model. Every other change corrects an evidence label or
a count, and each underlying claim holds exactly.

## Lean

No Lean statement or proof is affected, and nothing here requires a formal change. The census registry is
untouched.

## Cross-unit dependencies

- **Main:610.** The same line is edited by #961 (SC-29, `corpus/sc29-kernel-scope`), in a different sentence:
  the `C3Necessity.lean` citation. Git reports a textual conflict. The resolution is to keep both: SC-29's
  citation clause and this unit's count sentence.
- **LEDGER.json.** This unit changes one fingerprint, at line 1308. #961 changes the neighbouring hidden-memory
  entry, at lines 1295–1302. The ranges are separate.
- **Shared sentences.** These sentences are changed here and may be relied on by other units:
  - the §2.4 heading (any "§2.4 minimal model" citation in a later unit or in the Introduction's B.1 heading,
    r32);
  - the book §1.11 sentence on the card game;
  - Main:610's count, which the Introduction's L185 / R-33 relies on.
- **Main:620 and SC-40 (`corpus/sc40-c2-c3-statements`).** SC-40 also edits Main:620. Its branch carries the
  combined text: (C3) exact, and the per-order capacity form in floating point. At reconciliation SC-40's line
  is taken. SC-38 makes no further change to Main:620.
- **`verification/lean/hidden_memory_probe.py`.** #961 (SC-29) edits other lines of this file (base lines
  3–9 and 270–275). This unit changes the print strings at 279–280 only.
- **Shared source.** `memory_probes.py`'s grouping and the probe output strings above. No other unit edits
  them.
- **ch01 and FULL.** SC-39 edits ch01:286 and FULL:630 in the same §1.11 paragraph block (separate lines).
- **#968 (SC-33).** It touches neither ch01:135 nor ch01:273.

## Open, for #970

- **Making `c4_backflow_probes.py` exact.** It could be done with the prime-log method of section B, if the
  owner wants the paper to cite an exact instance check.
- **Exactness of the cited probes.** `memory_probes.py` (c), `primitive_probes.py` (B) and
  `purification_probes.py` (6) remain floating point. An exact port would make their annotations "exact"
  again. The conclusions are exactly verified here.
