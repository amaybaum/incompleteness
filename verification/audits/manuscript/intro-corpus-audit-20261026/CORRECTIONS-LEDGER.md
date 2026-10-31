# Corrections ledger: introduction-corpus audit (#942), source-correction gate #946

Draft, 2026-10-27. Read against `main` at `0d917665d32287e5d0ce649012175f2c7bf75b09`, the audit branch
`audit/intro-corpus-20261026` at `42bbd33c`, and the remote heads of the `corpus/sc*` branches as listed by
`git ls-remote` at about 20:58Z. Audit records cited by path are under
`verification/audits/manuscript/intro-corpus-audit-20261026/` on the audit branch unless another branch is named. That
directory is abbreviated `AUD/` below.

## Conventions

**Evidence levels.** Each unit lists one level per claim component. The levels are not interchangeable.

| Code | Level | What it requires here |
|---|---|---|
| K | Lean kernel-checked | a named theorem, its `#print axioms` line in the source, and the release gate's `lean-axioms` step (`tools/lean_axiom_check.py`, permitted set `propext`, `Classical.choice`, `Quot.sound`; the gate passes `--require-lake`) |
| X | exact algebra or exhaustive finite computation | an exact-arithmetic script and its output, with controls |
| P | mathematical argument in prose | a paper proof, with no kernel or exhaustive check of the step |
| N | numerical evidence | floating-point or sampled computation |
| C | conditional result | proved under a named hypothesis that is not established |
| O | open | stated as open in the corrected text |

Where a source does not fix the level, the weaker level is recorded and marked *(flag)*.

**Provenance and evidence.** CI runs, job ids, PR bodies and PR comments are provenance (AGENTS.md §A.42 item 2), not the
support of a claim. Review records retained on the audit branch, which is not on `main`, are identified by path. A
reviewer verdict quoted from a PR body or comment is marked "(PR record)".

**CI.** "CI x/y" is the tally of check-run conclusions on that exact commit, read from the checks API while this ledger
was drafted. Every listed `main` merge commit reads 25 success and 1 skipped (the matrix placeholder).

**Lines.** `File :n` means line n of that file at the unit's base commit, unless stated otherwise.

## Summary

| Unit | PR | State | Head | Merge commit |
|---|---|---|---|---|
| SC-1 | #947 | merged | `4cef4200` | `024a2126` |
| SC-2 | #948 | merged | `a66ee170` | `9020bfa0` |
| SC-4 | #950 | merged | `7b8bccdd` | `0585dd0d` |
| SC-3 | #949 | merged | `fb3eecce` | `6bc2c4af` |
| SC-3 propagation and A6 | #951 | merged | `e042cfad` | `a5168789` |
| SC-18 | #952 | merged | `7d55572b` | `1a60e06b` |
| SC-20 | #953 | merged | `64281543` | `d66bb70e` |
| SC-21 | #954 | merged | `0474dad3` | `9d975c11` |
| SC-16 | #955 | merged | `1b6a4dbc` | `55e3217b` |
| SC-27 | #958 | merged | `75a7aa2c` | `4449b0d9` |
| SC-24 | #956 | merged | `652afa09` | `f92279af` |
| SC-25 | #957 | merged | `25c2903d` | `7a7a654d` |
| SC-26 | #959 | merged | `2b90a684` | `0d917665` |
| SC-17 (Explainer part) | #963 | open, draft | `03f8b6ad` | — |
| SC-22 | #964 | open, draft | `621fbf2c` | — |
| SC-28 | #962 | open, draft | `51ba6652` | — |
| SC-29 | #961 | open, draft | `823d6a80` | — |
| SC-31 | #967 | open, draft, stacked on #962 | `71c96578` | — |
| SC-32 | no PR found | drafting | `97d5b37c` | — |
| SC-33 | #968 | open, draft | `6b200f67` | — |
| SC-23 | no PR | investigation only | — | — |

For every merged unit the merge commit is a normal two-parent merge whose second parent is the approved head. Its tree
equals the head's tree, checked with `git rev-parse <commit>^{tree}` for all thirteen. The approval at the exact head is
recorded in `AUD/PLAN.md`, section *Merged source corrections*. For #947, #948, #950 and #951 it is also recorded in the
PR's merge comment, as provenance.

***

## Merged units

### SC-1: ε-realization at finite precision (#947)

- **Flaw.** Main §3.4 (base `14804075`) extended the clipping-and-normalization Corollary to digitized branches that are
  Hermitian but not positive. Normalization multiplies blocks by s/Q, which can exceed 1, so negative mass can grow.
  Main :546: "so both regimes are unconditional, the exact-ring one additionally probe-certified end-to-end". Main :560:
  "the substratum ontology stated as a theorem at finite resolution". Further sites: :550, :554, :556, :558, :576, :580.
  Findings S9-M1, S9-M2, S9-A9, S9-D4, S9-I5.
- **Corrected claim.** The exact-ring bound K(|O_max|−1)/G is proved. The finite-b bound on the realized outcome law is
  open (Main :562 at `0d917665`: "a bound on the realized outcome law of the clipped and normalized simulator at finite
  $b$ is open"). The instrument-level Rounding Lemma is proved, and its extension to Hermitian inputs is open. The
  Kochen–Specker conclusion is scoped to d ≥ 3, a Kochen–Specker set and exact statistics. :560 states compatibility of
  finite-accuracy quantum statistics with one reversible law, with quantum mechanics as an input. A hidden-state
  capacity independent of |N| is obtained with fixed-point registers, whose finite-b bound is open (:592).
- **Evidence.**
  - Exact-ring bound: P, with X instance checks (`AUD/proofs/eps-realization/exact_regime.py`: 1980 runs, 0 violations,
    `Fraction` arithmetic).
  - Counterexample to the per-parent bound 4ηs + 8ν: X (`AUD/proofs/eps-realization/neg_parent4.py`, `Fraction`; d=3,
    R=9: 5.0007 > 4.0002; d=4, R=16: 8.0022 > 4.0016).
  - Finite-b bound: O.
  - Ledger: `MAIN:T-uniform-continuum-realization-mutual-density` at level P ("no Lean statement"), re-affirmed.
- **Manuscripts.** papers/Main; `papers/oi_lattice_code/architecture_check.py` and `foundations/opglue_probes.py`
  (descriptions); LEDGER. No book or FULL site: a corpus grep found none.
- **Introduction (#918).** R-40, which revises R-07. #918's r16 record (`CHANGES-r16.md`, item I-12) states that the paper
  carries no ε-realization text. Introduction-side closure: unverified.
- **Verification.**
  - Step-9 review: `AUD/proofs/eps-realization/REVIEW.md`.
  - PR review (PR record): ACCEPT WITH CHANGES at `7c6ceaaa` (RC-1 to RC-5, RR-1 to RR-4); ACCEPT at `4cef4200`.
  - CI at the head: 25/26 success, 1 skipped. Main CI at the merge commit: green.
  - Repair research: #945.
- **Merge.** Approved head `4cef420039b49dbfb707030a2389df8b45b39580`; merge commit
  `024a212699f7c76e6aff80173c607ecb2f34bebd` (parents `14804075`, `4cef4200`).

### SC-2: the independent-prior realization (#948)

- **Flaw.** Main :496 (base `14804075`): "so the equivalence is between rational laws and finite realizations with
  rational priors". This is false when the prior is μ_H: a rational point-mass μ_H with an irrational visible initial law
  is a counterexample. The parenthetical "(t ≪ t_R)" was not delivered by the construction. Further items: proof gaps
  G1, G2, G5 and G6; the (ii) ⇒ (iii) ledger row's "C2 leg conditional". Findings S9-M3, S9-A6, S9-I7, S9-D8.
- **Corrected claim.** Main :512 at `0d917665`: "for a finite realization whose prior $\mu_H$ is rational and independent
  of the visible initial state, … the conditional kernels at positive-probability histories are rational; conversely
  every law with rational conditional kernels is real[ized]". The initial law enters only through P₀ and may be
  irrational. "(t ≪ t_R)" is removed. (C2) is not part of (iii). The Extension is retitled "arbitrary kernels".
- **Evidence.**
  - Theorem and converse: P.
  - Counterexample: P (an argument).
  - The reviewer's exact re-implementation (78 checks) is a PR record; its script is not identified in a retained
    record *(flag)*.
  - Step-9 probes: X (`AUD/proofs/independent-prior/*.py` with outputs).
  - Ledger: `MAIN:T-finite-horizon-process-dilation` at level P, re-affirmed.
- **Manuscripts.** papers/Main, papers/Structure (:1255–:1256), LEDGER.
- **Introduction (#918).** R-08. r16 item D2 rewrites L56 from Main :512–514. Closure: unverified.
- **Verification.**
  - Step-9 review: `AUD/proofs/independent-prior/REVIEW.md`.
  - PR review (PR record): ACCEPT WITH CHANGES at `2995ef93` (RC-1 to RC-4); ACCEPT WITH CHANGES at `e5c09aec` (RC-5);
    ACCEPT at `801fc221`. `a66ee170` is `801fc221` with main `024a2126` merged.
  - CI at the head: 25/26 success, 1 skipped.
- **Merge.** Approved head `a66ee170ed1e34d02faada52d8898f314ef1a059`; merge commit
  `9020bfa01bd3042af8a84c289290b56b26433973`.

### SC-4: signal-cone speed versus c, and the Bell hypotheses (#950)

- **Flaw.**
  - Main :389 (base `14804075`): "Determinism is constitutional here, so exactly two hypotheses remain available and the
    framework must choose between them".
  - Main :394 (Corollary): "with maximum lattice propagation speed identified with $c$".
  - The hypotheses were loose enough to reach CHSH = 4 (CE2 sequential interventions, CE3 a remote-reading readout, CE4
    no-click post-selection). "Screened" was undefined.
  - Check 11 was described as "Certified".
  - Findings S9-I3, S9-A8, S9-D2.
- **Corrected claim.**
  - The theorem states (ii) own-wing interventions u_a × u_b × id, (iii) ±1 readouts on regions outside the other
    wing's cone, (iv) a definition of "screened", and outcomes recorded in every run.
  - The cone lemma states that V is finite.
  - An inclusive either/or: a completion reproducing quantum Bell correlations gives up ontic parameter independence or
    measurement independence, and the framework gives up the first.
  - Main :410 at `0d917665`: "which of the two, if either, is the physical $c$ depends on which propagation sets the
    emergent light cone and is not derived here".
- **Evidence.**
  - Bell ceiling: P (Bell's theorem under the stated hypotheses). It has no coverage-ledger entry; that gap is assigned
    to SC-14.
  - Countermodels CE1–CE4, and the positive tests on reversible nearest-neighbour automata: X
    (`AUD/proofs/bell-ceiling/bell_review_probes.py`, `.out`).
  - Lift speed 1/√3: X (sympy, per the review record).
  - Cone speed versus c: O.
  - Check 11 is an exhaustive pointwise bound over 16 deterministic tables, but its controls (b), (c) and
    `withdrawn_would_allow` are vacuous. That is SC-13, open, and no verdict here rests on that check.
  - Ledger: `MAIN:C-bell-lattice-obstruction-state-dependent` at GAP, re-affirmed.
- **Manuscripts.** papers/Main, Substratum (:48, :130), SM (:230), Methodology (:391); book ch00, ch02, ch04 and FULL;
  LEDGER.
- **Introduction (#918).** R-39. r16 item D6 states the theorem with (i)–(iv), ±1 in every run, and the either/or.
  Closure: unverified.
- **Verification.**
  - Step-9 review: `AUD/proofs/bell-ceiling/REVIEW.md`.
  - PR review (PR record): ACCEPT WITH CHANGES at `74302d0c` (RC-1 to RC-7); ACCEPT WITH CHANGES at `fa1d835b` (RC-8,
    RC-9); ACCEPT at `e99df4a0`.
  - `7b8bccdd` is `e99df4a0` with main merged twice. Its source-line changes equal `e99df4a0`'s across 19 files (PR
    record).
  - CI at the head: 25/26 success, 1 skipped.
- **Merge.** Approved head `7b8bccddfe84bf4219d938c4d870b3f080635dd4`; merge commit
  `0585dd0dfc31dbb4ba542f310748273c68f142cf`.

### SC-3: recurrence and memory interpretation (#949)

- **Flaw.**
  - Main :30 (base `14804075`): "History readback then identifies the nontrivial sector by forcing hidden predictive
    memory and, on a fixed finite recurrent representative, global indivisibility".
  - Main :82: "C4 forces … global indivisibility somewhere in the recurrence cycle".
  - Main :594: "Remark (a variational identity, open — and false in its naive form)". The identity M_det = M_t fails at
    every hidden dimension.
  - The §2.3 theorem without a root-independent shared hidden prior is false: 152,808 counterexamples at (2,4).
  - Findings S9-A1, S9-I1, S9-D6, S9-M4, S9-A4, S9-A5, S9-I2, S9-D7.
- **Corrected claim.**
  - Under a full-support prior, recurrence-cycle indivisibility is equivalent to M_k > 0 at some order below the
    recurrence time. Every non-deterministic visible step supplies it, laws Markov on every accessible window included
    (Main :141 at `0d917665`). Observational access needs the obstruction at an accessible order, which is (C4).
  - Γ_t is defined for every root under one shared, root-independent hidden prior.
  - The memory statements are kept.
  - §1.5 predictive infimum: over completions without bijectivity it is I(X_<t; X_>t | X_t), attained by the canonical
    predictive quotient; over bijective realizations it is H(X_<t | X_t) (Main :610).
  - (C3) is unconditional (`c3_necessity`).
  - Owner framing decision R-37: memory, readback (C4) and predictive information are three distinct claims.
- **Evidence.**
  - Stochastic-inverse lemma: K (`isPermMatrix_of_stochastic_inverse`, `#print axioms` at
    `OIBridge/EquivalenceChain.lean:391`).
  - Overlap plus total-variation route: K (`pIndivisible_of_rooted_identity_return_of_overlap`, `#print axioms` at
    `OIBridge/RecurrenceHorizon.lean:190`).
  - History step: P. The theorem's ledger entry `MAIN:T-history-readback-finite-recurrence-implies` is at P.
  - Scope equivalence: X (exhaustive at (2,2), (2,3), (3,2), PR record); the reviewer's 33,408 cases with an exact LP
    for P-divisibility (PR record).
  - Memory theorem: K (`unavoidable_hidden_predictive_memory`, `#print axioms` at `OIBridge/HiddenMemory.lean:202`), for a
    joint law. The time-t reading is P; SC-29 proposes K3 → K2.
  - Reversibility identity: P, with X checks (11,712 cases, PR record).
  - Step-9 probes: X (`AUD/proofs/readback-recurrence/*`, `AUD/proofs/hidden-memory-theorem2/*`).
  - Axiom reports for the four names above: `[propext, Classical.choice, Quot.sound]` in the Mathlib bridge job log of
    run 40553921940 (provenance). These Lean files are unchanged between `0d917665` and that run's head, apart from
    comments in `HiddenMemory.lean`.
- **Manuscripts.** papers/Main (abstract :20, :30, :82, §1.5, §2.3, §3.4, :411, :534, :752, :758), Substratum,
  Explainer, Structure; book ch00, ch01, ch02, glossary, README, readers-guide, FULL; LEDGER.
- **Introduction (#918).** R-36, R-37. r16 items D1 (abstract) and D4 (L90–L96). Closure: unverified.
- **Verification.**
  - Step-9 reviews: `AUD/proofs/readback-recurrence/REVIEW.md`, `AUD/proofs/hidden-memory-theorem2/REVIEW.md`.
  - PR review (PR record): ACCEPT WITH CHANGES at `50a40e1c`; ACCEPT WITH CHANGES (RC-R1) at `0c249f57`; ACCEPT at
    `da14b171`. Framing commit `00183e9e`. ACCEPT WITH CHANGES at `d6df1d78`; ACCEPT at `3b17567f`.
  - Reconciliation review of `fb3eecce`: recorded in `AUD/PLAN.md`; verdict text not located in a retained record
    *(unverified)*.
  - CI at the head: 25/26 success, 1 skipped.
- **Merge.** Approved head `fb3eeccea7771293e568fcf4b15e3e58f84cc211`; merge commit
  `6bc2c4af10863c2cdfd9f5c1b88abdc8b64f9ed0`.

### SC-3 propagation and A6 (#951)

- **Flaw.**
  - Residual sites presenting recurrence-cycle indivisibility as identifying the memory-bearing sector. ch01 :193 (base
    `6bc2c4af`): "the memory-bearing indivisible sector characteristic of OI". Methodology :13:
    "memory-bearing/indivisible sector".
  - List A: Substratum :52, glossary :99, ch18 :193, ch09 :110 and :265, Medicine :13, Bioinformatics :14, Main :141.
  - A6: the M1-T premise "history-readback/P-indivisible sector" at Substratum :108 and :122, ch02 :90 and appendix-c
    :108, each with its FULL mirror.
  - RC-A6-1: the Substratum Stage-1 step (:136) had no antecedent and overstated the reverse-direction lemma.
- **Corrected claim.** "memory-bearing sector". Recurrence P-indivisibility holds on every finite reversible
  representative with a non-deterministic visible step. The M1-T premise names the history-readback sector. Stage 1
  cites the finite-horizon equivalence (S ⇒ D), and cites the lemma only for one doubly stochastic matrix.
- **Evidence.** P (wording alignment to Main §2.3). S ⇒ D: K (`S_imp_D`, `#print axioms` at
  `OIBridge/Equivalence.lean:479`).
- **Manuscripts.** papers/Main, Substratum, Medicine, Bioinformatics, Methodology; book ch01, ch02, ch09, ch18,
  appendix-c, glossary, FULL.
- **Introduction (#918).** R-36, R-37 (as SC-3).
- **Verification.**
  - Review (PR record and #946): ACCEPT WITH CHANGES at `0ecc8ec6` (list A); ACCEPT at `bf8066e5`; A6 owner-approved; ACCEPT
    at `e042cfad` after RC-A6-1.
  - CI at the head: 25/26 success, 1 skipped.
- **Merge.** Approved head `e042cfad1a2ae264b226ae5ae72371dbbb50a703`; merge commit
  `a5168789196788ca13f3f33c067be52f0f4d82ab`.

### SC-18: reverse-direction lemma scope (#952)

- **Flaw.** Structure :1274 (base `a5168789`): "[Main]'s reverse-direction lemma (every P-indivisible process on a finite
  configuration space admits a deterministic dilation)". The lemma (Main :270) covers one doubly stochastic matrix with a
  uniform hidden prior. Related sites: Substratum :110, Main :274, appendix-b :44 and :46 (FULL :5811, :5813).
- **Corrected claim.** Structure :1274 cites the §3.4 finite-horizon process dilation, with the response-table extension
  ("a finite deterministic bijection, depending on K"), and the all-time impossibility. The other sites give the
  one-step uniform-prior correspondence (exact for rational entries, approximate otherwise) and point to §3.4 for the
  process level.
- **Evidence.** P (citation scoping; the new content rests on the paper proofs of Main §3.4). No Lean identifier is
  claimed.
- **Manuscripts.** papers/Structure, Substratum, Main; book appendix-b, FULL.
- **Introduction (#918).** None: #918 cites only the §3.4 process-level result.
- **Verification.**
  - Track C classification: `AUD/tracks/C-consistency/REVIEW.md` (rows STR-1274, SUB-110) and
    `AUD/tracks/C-consistency/STRUCTURE-1274.md`.
  - PR review (PR record): ACCEPT WITH CHANGES at `48dfb8f7` (F1 blocking, N1–N5); ACCEPT at `7d55572b`.
  - CI at the head: 25/26 success, 1 skipped.
- **Merge.** Approved head `7d55572b5ecf2235f014e1f09b8bc2c434b2548a`; merge commit
  `1a60e06b27ff5e41833dcd1e013ddb1c3aab1947`.

### SC-20: C2 necessity in two forms (#953)

- **Flaw.** The corpus called C2 necessity "conditional" without separating a persistence form that needs no mixing
  hypothesis (Track D finding D4). (C2-structural) was presented as a nontrivial condition on bijective realizations
  (D1). Main :76 (base `1a60e06b`): "satisfying (C2-structural) while violating (C2-slow)".
- **Corrected claim.**
  - Persistence form, in the coupling-step model of §3.4: observed memory I* > 0 places some realized hidden conditional
    at least ε_min(I*, n_V) from π_H, with no mixing hypothesis.
  - Timescale (slow-bath) form: conditional on the mixing hypothesis.
  - (C2-structural) holds by reversibility in every bijective realization and constrains coarse-grained descriptions.
  - Main :76 at `0d917665`: "so that (C4) holds while (C2-slow) fails".
- **Evidence.**
  - Persistence form: P (the physical-memory theorem's own proof). The reviewer's exact probe found 0 violations over
    3,000 models (PR record). That is a finite sample, not exhaustive *(flag)*.
  - Reversible retention: P (Main :608), with X (`AUD/tracks/D-c2-sc16/c2_bijective_checks.py`, `out_c2_bijective.txt`,
    exhaustive at (2,2), (2,3), (3,2), (2,4)).
  - Slow-bath form: C.
  - Ledger: `MAIN:T-physical-memory-c2-process-form` at P, re-affirmed (`4c4f0d29`).
- **Manuscripts.** papers/Main, Substratum, Structure, GR, Explainer, SM (:296); book glossary, ch01, ch02, ch04, ch07,
  ch19, appendix-b, appendix-c, FULL; LEDGER.
- **Introduction (#918).** #918 :185 to name the slow-bath form. r16 items D3 (L86) and D5 (L185). Closure: unverified.
- **Verification.**
  - Track D: `AUD/tracks/D-c2-sc16/REPORT.md`.
  - PR review (PR record): ACCEPT WITH CHANGES at `f6e4ba55` (B1, B2, N1–N6); ACCEPT WITH CHANGES at `c9969d89` (Main
    :624); ACCEPT at `64281543`.
  - Open item N3 (the τ_B reading in the shift-register example) is not resolved here.
  - CI at the head: 25/26 success, 1 skipped.
- **Merge.** Approved head `64281543957ff1d88276abe8ae8e280a209c8c39`; merge commit
  `d66bb70efacf5070c052c1184d1cf9db84122a3b`.

### SC-21: (EM) results scoped to the coarse-grained description (#954)

- **Flaw.** Main :746 (base `d66bb70e`): "Theorem (structural observer selection — conditional on (EM))", stated for the
  exact τ_B(V). Its proof (:752) uses 𝒦_Σⁿ. Main :754: "¬(C2-structural) ⇒ ¬(C4) by the fast-bath erasure lemma ⇒ $M_t
  = 0$ on accessible windows". The past-hypothesis corollary is at :756. Nothing establishes PUⁿP = 𝒦ⁿ (Track D D6).
- **Corrected claim.** The theorem and both corollaries hold for "the coarse-grained description generated by iterating"
  the one-step effective channel (Main :742 at `0d917665`). Scope (ii) states that the exact n-step compressions recur
  and need not equal 𝒦ⁿ, and that the corollaries do not assert that the exact visible law carries no accessible memory.
- **Evidence.**
  - Counterexample (φ(z) = z+1 on ℤ₅): X (`AUD/tracks/D-c2-sc16/compression_check.py`, `out_compression.txt`: PUⁿP = 𝒦
    for 1 ≤ n ≤ 4, PU⁵P = I). The reviewer reproduced it with a fine-partition countercontrol (PR record).
  - Theorem and corollaries: C (on (EM), within the scoped description).
  - Ledger entries `MAIN:T-structural-observer-selection-conditional-em`, `MAIN:C-anti-boltzmann-brain`,
    `MAIN:C-past-hypothesis-replacement-rate-condition`: GAP, re-affirmed.
  - The exact-vanishing reading at :161, :165, :754 is not corrected here (SC-23).
- **Manuscripts.** papers/Main, Substratum, Complexity, Explainer, Structure; book ch01, ch02, ch03, ch04, FULL; LEDGER.
- **Introduction (#918).** None: #918 makes no (EM)-based claim.
- **Verification.**
  - PR review (PR record): ACCEPT WITH CHANGES at `c4ca72c4`; ACCEPT at `9e01e9fb`, `36ef284d` and `b7b67508` (owner
    safeguards checked at `6c2bfb8e`); re-validated ACCEPT at `0474dad3` after merging main `d66bb70e`.
  - CI at the head: 25/26 success, 1 skipped.
- **Merge.** Approved head `0474dad38fedb2614bf52baad780d62f16e6026f`; merge commit
  `9d975c11e119950dba6f90b1ae1af8f2a2dd7bb0`.

### SC-16: accessible-window P-indivisibility attributed to C1–C4, with the SC-5 terminology (scheme A) (#955)

- **Flaw.**
  - Sites read the readback lemma, or C1–C4, as giving P-indivisibility or a revival of distinguishability within
    accessible windows. Explainer :892 (base `9d975c11`): "the accessible-timescale backflow lemma (Main, §2.3)
    establishes P-indivisibility without recurrence".
  - A second premise error: appendix-b :420: "so C1 and finiteness establish P-indivisibility only *in principle*". The
    same error at Bioinformatics :14, Medicine :13, Main :151, :733 and Explainer :272.
  - The full site union is in #946 (*Items assigned to units*) and `AUD/tracks/RECONCILIATION.md` §3.
- **Corrected claim.**
  - C1–C4 give accessible conditional memory. "C1–C4 ⇒ accessible-window P-indivisibility" is a refuted implication.
  - An in-window revival of distinguishability is a sufficient, not necessary, extra condition.
  - (C1) supplies the non-permutation rooted map under the uniform hidden prior that defines T.
  - "Backflow" is reserved for distinguishability revival. The readback lemma is retitled "Lemma (accessible conditional
    memory from readback)" (Main :167 at `0d917665`).
- **Evidence.**
  - Refutation: X. Exact countermodels from Track B (`AUD/tracks/B-sc16/`) and Track D (`AUD/tracks/D-c2-sc16/`): XOR, a
    static bath, an LFSR family, the 6-state permutation [0,3,4,1,5,2], and an (EM) plus C2-slow hidden-Markov family,
    with exhaustive enumeration. Coordinator re-checks are in `AUD/tracks/xcheck/` (`six.py`, `sixgap.py`, `c1perm.py`).
    No formal theorem is contradicted.
  - Sufficient condition: K (`c4e_implies_pIndivisible`, `c4r_implies_pIndivisible`, `#print axioms` at
    `OIBridge/CausalReadback.lean:331` and `:330`; reported `[propext, Classical.choice, Quot.sound]` in the run
    40553921940 log, provenance). The manuscript states it in words only.
  - Readback lemma: P (`MAIN:L-accessible-conditional-memory-from-readback` at P, "no Lean statement").
- **Manuscripts.** papers/Main, GR, Explainer, Complexity, SM, Substratum, Structure, Medicine, Bioinformatics,
  Computation; book ch00, ch01, ch04, ch05, ch15, ch16, ch17, ch18, appendix-a, appendix-b, appendix-c, glossary, README,
  FULL; LEDGER; `verification/lean/c3_necessity_probe.py` (message text only).
- **Identifier transition.** `MAIN:L-accessible-backflow-from-readback` is retired, not reused, and succeeded by
  `MAIN:L-accessible-conditional-memory-from-readback`. This is an owner-authorized exception to claim-ID immutability,
  recorded in `AUD/PLAN.md`, *Identifier transitions*.
- **Introduction (#918).** None needed for scheme A. r16 adds one sentence: an in-window revival makes the family
  P-indivisible on that window (Main :153).
- **Verification.**
  - PR review (PR record): ACCEPT WITH CHANGES at `2d3067aa` (B1, B2, N1–N17); ACCEPT at `1165b068`; re-validated ACCEPT
    at `1b6a4dbc` after the reconciliation merge `338932dd`.
  - Regression grep: recorded in the PR body (provenance).
  - CI at the head: 25/26 success, 1 skipped.
- **Merge.** Approved head `1b6a4dbc9f2f82d53d91ed887138845c850720cb`; merge commit
  `55e3217b16a75d8533cb12c2a650f4ca1068ff71`.

### SC-27: C2 in its two forms and C3 unconditional at the stale sites (#958)

- **Flaw.**
  - Substratum :137 (base `55e3217b`): "establishes that the resulting dynamics, conditional on the hidden-sector mixing
    hypothesis …, necessarily satisfies C2 … and C3", which makes mixing a condition for C3.
  - Substratum :129: "the divisibility deficit obeys an explicit bound $(k-1)\varepsilon$; without it, the necessity
    direction (P-indivisibility on accessible timescales forces $\tau_S \ll \tau_B$)".
  - Further sites: Main :99, :109, :336, :652; GR :20 and :565 ("ETH holds"); SM :296; the glossary :27 heading;
    appendix-b :98.
- **Corrected claim.**
  - C3 (log₂|C_H| ≥ I*) holds in every faithful realization, with no mixing hypothesis.
  - (C2-structural) holds by reversibility.
  - The persistence form needs no hypothesis.
  - The slow-bath form, under mixing, gives a lower bound on the bath's conditional mixing time, not τ_S ≪ τ_B. The
    benchmark bound ‖T^(k) − T^k‖ ≤ (k−1)ε is optimal at k = 2.
  - ETH is "the standard assumption" for the horizon complement.
- **Evidence.**
  - C3: K for the joint-law form (`c3_necessity`, `#print axioms` at `OIBridge/C3Necessity.lean:140`), with the time-t
    reading P. The ledger shows `MAIN:T-c3-necessity` at K3 on main; SC-29 proposes K2.
  - Capacity corollary: `card_hidden_ge_two_pow_Istar` has `#print axioms` at `C3Necessity.lean:143`. Its ledger level is
    P on main; SC-29 proposes K2.
  - C2 forms: P and C as in SC-20. No fingerprinted statement changed.
- **Manuscripts.** papers/Substratum, Main, GR, SM; book ch07, glossary, appendix-b, FULL.
- **Introduction (#918).** None per `AUD/PLAN.md`; the Introduction's (C2)/(C3) statements are revised in r17 against main.
- **Verification.**
  - Reviews retained on the audit branch: `AUD/tracks/FINAL-AUDIT/reviews/958-REVIEW-7e9cf451.md` (BLOCK, three
    findings), `958-RECHECK-838918bd.md` (ACCEPT), `958-CONFIRM-75a7aa2c.md` (CONFIRM).
  - CI at the head: 25/26 success, 1 skipped.
- **Merge.** Approved head `75a7aa2cf21da69cae755ef324d10b7eb2ee1c11`; merge commit
  `4449b0d9bfa5042869b22b7eb0a298e5f994e388`.

### SC-24: Medicine :25, Markov laws realizable and the fixed-basis representation internal (#956)

- **Flaw.** Medicine :25 (base `55e3217b`): "where it proves that the description of any embedded observer with partial
  access to a deterministic system is necessarily non-Markovian — quantum for processes in the correspondence's class,
  under the translation hypothesis (T)". This contradicts Main :172, :612–614 and :548/:652 (finding D-0, high).
- **Corrected claim.** Medicine :25 at `0d917665`: "The representation is universal, Markov laws included, so
  representability alone does not distinguish memory-bearing laws; history readback does." (C4) holds exactly when M_t
  > 0 at some accessible time. Recurrence-cycle P-indivisibility is stated with its hypotheses (Main :137, :141).
  Distinguishability backflow is not asserted.
- **Evidence.** P (prose/status correction). Every clause restates a Main result at Main's scope; no new computation. The
  representation clause rests on Main §3.4, whose S ⇒ D leg is K (`S_imp_D`).
- **Manuscripts.** papers/Medicine, Explainer (:294, :707, :709, :856, :948), Methodology (:110), Complexity (:27); book
  ch00, ch05, ch14, ch19, FULL.
- **Introduction (#918).** Per `AUD/PLAN.md`, the Introduction's recurrence and representation statements match Medicine
  :25 (r17/r18 scientific confirmations).
- **Verification.**
  - Reviews retained on the audit branch: `AUD/tracks/FINAL-AUDIT/reviews/956-REVIEW-533cdeb2.md` (ACCEPT WITH CHANGES),
    `956-RECHECK-3715cc33.md` (ACCEPT), `956-CONFIRM-b7632485.md` (CONFIRM).
  - `652afa09` is `b7632485` with main `4449b0d9` merged. The landing equals the PR's own diff (`AUD/PLAN.md`).
  - CI at the head: 25/26 success, 1 skipped.
- **Merge.** Approved head `652afa09a057403a7010c444214536d2aa6553aa`; merge commit
  `f92279afded306fc9e8b276a68c5128b14fedf5c`.

### SC-25: Main §3.5 rest-frame lemma stated as the proved inclusion (#957)

- **Flaw.** Main :660 (base `55e3217b`): "Then the invariance group of $T$ within the local frame transformations $O(3,1)$
  is the stabilizer of $n$". Main :668 (boxed): "$T$ selects a unique preferred timelike direction $n$ **if and only if**
  its invariance group … is a maximal compact subgroup $O(3)$". Only G_T ⊆ Stab(n) is proved. "Rotations fix n, so are
  invariances" took a necessary condition as sufficient (finding D-1). Substratum :329 depends on it.
- **Corrected claim.** Main :660 at `0d917665`: G_T "is contained in the stabilizer of the timelike line $\mathbb{R}n$,
  which is isomorphic to $O(3)\times O(1)$, and its orthochronous part … is contained in the stabilizer of $n$ …
  Consequently, under this hypothesis, boosts, which move $n$, are not invariances of $T$". The hypothesis that T
  determines the horizon foliation is explicit. The converse is one-way in O⁺(3,1), under its own hypothesis, which is
  not established for T. The box is removed. Which rotations are invariances is open, and spatial isotropy is empirical
  input E4.
- **Evidence.**
  - Inclusion and boost exclusion: C (on the foliation hypothesis), P.
  - Equality refuted: X, one witness (`AUD/tracks/SC25-rest-frame/cubic_counterexample.py`, `.out`: |G| = 48 = |O_h|, and
    96 with time-symmetric data; "ALL CONTROLS GREEN"). The script is on the audit branch, not on `main`.
  - Converse hypothesis for T: O.
  - Ledger: `MAIN:L-rest-frame-selection` and `MAIN:C-boost-rotation-inequivalence` at GAP, re-affirmed.
- **Manuscripts.** papers/Main (:256, :660–:670), SM (:134, :136, :1418), Substratum (:329); book ch19 (:240–:248),
  FULL; LEDGER. GR is unchanged, which the review accepted.
- **Introduction (#918).** None: the Introduction does not cite Main §3.5.
- **Verification.**
  - Reviews retained on the audit branch: `AUD/tracks/FINAL-AUDIT/reviews/957-REVIEW-b25dcfc4.md` (ACCEPT WITH CHANGES),
    `957-RECHECK-806b57dc.md` (ACCEPT WITH CHANGES), `957-CONFIRM-9eff10d3.md` and `957-CONFIRM-683ca7f1.md` (CONFIRM).
  - `25c2903d` is `683ca7f1` with main `4449b0d9` and `f92279af` merged (reconciliation CONFIRM per `AUD/PLAN.md`).
  - CI at the head: 25/26 success, 1 skipped.
- **Merge.** Approved head `25c2903d7b7036c06864c7c08e509c0c15b580f4`; merge commit
  `7a7a654d13ebb21d426ccb3a02daa2a5b126cdac`.

### SC-26: residual memory/divisibility scope, SC-16 and SC-3 classes (#959)

- **Flaw.** Residual sites stated P-indivisibility, backflow, a Bell mechanism, numerical gains or an unconditional
  ceiling beyond what the corpus proves. Examples at `55e3217b`:
  - Structure :903: "Non-Markovian marginal (P-indivisibility) | Confirmed".
  - Main :730: "The converse is retired".
  - Complexity :484–:490: a 10³ × sensitivity gain.
  - Bioinformatics and ch17: a "no-go theorem".
  - GR :591, SM :112, ch15 revival-as-prediction.
  - The full list is in #946 (comment of 12:13Z) and the PR's site table.
- **Corrected claim.** Three notions are kept apart: conditional memory (supplied by (C4)), recurrence-cycle
  P-indivisibility (wherever a rooted visible map is not a permutation), and backflow (a revival of distinguishability,
  which C1–C4 do not supply). Structure :903 at `0d917665`: "memory; P-indivisibility not tested by these experiments |
  Observed". Gains are "not quantified". The Bioinformatics ceiling is a conditional theorem.
- **Evidence.**
  - Mostly P (narrowing).
  - GR :591: P, using the K lemma `isPermMatrix_of_stochastic_inverse`.
  - SM :112: X per the PR body ((4,2), (4,3), (5,2), with two countercontrols). The script is not committed; only its
    sha256 is recorded, so the computation is not retained *(flag)*.
- **Manuscripts.** papers/Structure, Complexity, Bioinformatics, Main, SM, GR, Computation, Explainer; book preface,
  ch01, ch02, ch03, ch12, ch13, ch15, ch17, ch18, appendix-c, README, FULL.
- **Introduction (#918).** Reconciled against this main in #918's final reconciliation (`AUD/PLAN.md`). r16 states that
  none of the listed sites is a source of an Introduction statement.
- **Verification.**
  - Reviews retained on the audit branch: `AUD/tracks/FINAL-AUDIT/reviews/959-REVIEW-7c117827.md` and
    `959-RECHECK-8d8ca8c6.md` (both ACCEPT WITH CHANGES).
  - Confirmation rounds, retained in the same directory: `959-CONFIRM-72eece11.md` (ACCEPT WITH CHANGES),
    `959-CONFIRM-e71371dd.md`, `959-CONFIRM-f3b42a7b.md` and `959-CONFIRM-2b90a684.md` (CONFIRM).
  - CI at the head: 25/26 success, 1 skipped.
- **Merge.** Approved head `2b90a684e1afe7dcebcafe6cddebcfe0e1f2095c`; merge commit
  `0d917665d32287e5d0ce649012175f2c7bf75b09`.

***

## Open units

### SC-29: kernel scope (#961)

- **Flaw.**
  - Main :268 (base `0d917665`): "an exact norm-continuous path of local $*$-automorphisms of the quasilocal algebra".
    The same wording is at Main :584, GR :292, Explainer :381, FULL :509 and :5286, ch01 :165 and ch19 :126.
    `driveQ_isContinuousPath` proves only strong (pointwise) continuity, and no theorem states locality of `driveQ R t`
    at general t.
  - Main :510, :608 and :610 cited the memory and C3 theorems with no scope, although `Realization`
    (`HiddenMemory.lean:54`) carries an arbitrary joint law that is not tied to the bijection's time-t law.
  - The ledger's capacity bound was at P ("no Lean statement").
- **Corrected claim (branch).** Main :268: "an exact strongly continuous path of $*$-automorphisms …". Main :510 adds:
  "for joint laws of history, present and hidden state, with $I^*$ the maximum over a finite family of such laws on one
  hidden alphabet; reading a realization's time-$t$ laws as those joint laws is a step not formalized".
- **Evidence.**
  - Strong continuity: K (`driveQ_isContinuousPath`, `#print axioms` at `SecondOrderDrive.lean:859`; with
    `driveQ_one_eq_heisQ` at `:893`).
  - Locality at general t: no kernel statement (O5 follow-up).
  - Capacity bound, upgraded P → K2:
    - Theorem `card_hidden_ge_two_pow_Istar` (`C3Necessity.lean:117`): for every finite nonempty family of
      `Realization`s on one history type, one visible and one hidden alphabet H, 2^(Istar) ≤ |H|.
    - Axiom evidence: `#print axioms card_hidden_ge_two_pow_Istar` at `C3Necessity.lean:143`, checked by the release
      gate's `lean-axioms` step against `PERMITTED` (`tools/lean_axiom_check.py:47`). The gate runs in CI as the
      Mathlib bridge job, and `OIBridge.lean:59` imports the module.
    - Run 40553921940 (event `pull_request`, head_sha `823d6a80`): conclusion success. Mathlib bridge job 122364744513:
      Build success, Release gate success. The job log (provenance) reports `'OIBridge.C3.card_hidden_ge_two_pow_Istar'
      depends on axioms: [propext, Classical.choice, Quot.sound]` and `PASS lean-axioms … lean_axiom_check: OK (6082
      named result(s) reported …)`, with no `sorryAx` token. The same log reports the permitted three for
      `c3_necessity_and_capacity`, `c3_necessity`, `unavoidable_hidden_predictive_memory` and
      `driveQ_isContinuousPath`. The run tests a synthetic merge with `main` `0d917665`, which `823d6a80` already
      contains.
    - K2, not K3, for two named ancillary steps that are not formalized: the time-t reading, and reading sup_t as the
      finite maximum, with histories in one history type.
  - K3 → K2 downgrades:
    - `MAIN:T-unavoidable-hidden-predictive-memory`: the time-t reading of the law is not formalized.
    - `MAIN:T-c3-necessity`: the same step.
    - Totals: K3 23 → 21, K2 6 → 9, P 28 → 27; kernel coverage 30/116 → 31/116. No fingerprint moves and no ID is retired.
  - Probe evidence for the remaining clauses: X (`c3_dilation_probes.py`; C5 and C6 of
    `verification/lean/c3_necessity_probe.py`).
- **Lean edits are comment-only.** The changes are in `C3Necessity.lean`, `HiddenMemory.lean` and `SecondOrderDrive.lean`.
  Re-checked for this ledger: with `--` and `/- … -/` comments, docstrings included, stripped, each file is identical to
  `0d917665`, and the line counts are unchanged (148, 206, 895).
- **Manuscripts.** papers/Main, GR, Explainer; book ch01, ch19, FULL; LEDGER; the census JSON and its note;
  `verification/README.md`; `verification/lean/edge_rigidity_probe.py` (R7-CTN guard, mutation-tested), plus the
  `c3_necessity_probe.py`, `hidden_memory_probe.py` and `static_generator_probe.py` docstrings.
- **Introduction (#918).** None (PR body): #918 already states Theorem 2's machine-checked core in joint-law form.
- **Verification.**
  - Track record: `AUD/tracks/SC29-kernel-scope/README.md` on the branch.
  - Reviews retained at `AUD/tracks/FINAL-AUDIT/reviews/`: `961-REVIEW-8c5d2751.md` (ACCEPT WITH CHANGES: R1,
    comment-only; O1–O9) and `961-CONFIRM-823d6a80.md` (ACCEPT). `823d6a80` applies R1, O1–O4 and O7.
  - CI at `823d6a80`: 25/26 success, 1 skipped.
- **Status.** PR #961, open, draft, head `823d6a80`. Merge after #918 by owner decision, at an exact SHA.

### SC-28: generalizations stated without their assumptions (#962)

- **Flaw.**
  - Main :151 (base `0d917665`): "By Poincaré recurrence, $\exists t_R$: the set of hidden states with … has measure $> 1
    - \delta$ for any $\delta > 0$".
  - Main :176: the §3.4 necessity proof for (C2) "establishes" P-divisibility.
  - Main :706: "with the type II structure as a consequence rather than a postulate", with GR §6.3 :368 and ch07 :199.
  - SM :1211: "by P-indivisibility (Main Theorem 4), the stationary distribution is unique, hence $\rho \circ T = \rho$".
  - SM :294: "empirically demonstrated", "closed at chat-track numerical scale".
  - Also ch18 §18.7 (finite-measure and single-cycle claims), SM §8.5 and Explainer :679.
- **Corrected claim (branch).**
  - Main :151: common-time near-total return would give P-indivisibility. "Poincaré recurrence does not supply it for a
    general Hamiltonian flow … for a mixing flow $T_{ii}(t)$ tends to the normalized Liouville measure of the cell". The
    general case is open.
  - SM :1211: the whole of gap (ii) is conditional on cycle ergodicity of the realized bijection on a T-invariant set
    carrying ρ. TφT = φ⁻¹ holds for every update (a,b) ↦ (R(a) − b, a).
  - SM :294: chaos is demonstrated numerically within the sampled sizes, ensembles and protocols. Breaking the linear
    rule's integrability is needed for full-shell sampling, and chaos does not establish it.
  - Type II, CLPW's algebra and entropy, and the dS cancellation are open.
- **Evidence.**
  - Mixing-flow failure: P.
  - Gap (ii): C (cycle ergodicity).
  - TφT = φ⁻¹: P. The "symbolic and random-state" check named in the track README is not retained as a file *(flag)*.
  - SM chaos diagnostics: N.
  - Type II and dS claims: O.
  - Self-assessment sentences are removed.
- **Manuscripts.** papers/Main, GR, SM, Structure, Explainer; book ch01, ch02, ch07, ch09, ch18, FULL.
- **Introduction (#918).** None (PR body).
- **Verification.**
  - Track record: `AUD/tracks/SC28-assumption-scope/README.md` on the branch. The GR §6 heading no-change decision is at
    `AUD/tracks/FINAL-AUDIT/GR6-heading-decision.md`.
  - Reviews retained at `AUD/tracks/FINAL-AUDIT/reviews/`: `962-REVIEW-42bc4050.md` (ACCEPT WITH CHANGES, R1–R4),
    `962-CONFIRM-df061d64.md` (ACCEPT WITH CHANGES, Q1–Q3) and `962-CONFIRM-c43347f4.md` (ACCEPT). The single commit
    `51ba6652` (SM :294 wording, owner decision 6a) has no verdict yet; its delta confirmation is pending.
  - CI at `51ba6652`: 25/26 success, 1 skipped.
- **Status.** PR #962, open, draft, head `51ba6652`. The PR body still names `c43347f4`. Merge after #918 by owner
  decision.

### SC-31: recurrence-period growth (#967, stacked on #962)

- **Flaw.** ch18 :184 (base `0d917665`): "For a generic permutation on $|S|$ elements, the order is bounded by
  $\mathrm{lcm}(1, 2, \ldots, |S|)$ (Landau's function), which grows as approximately $e^{|S|}$". It presented
  e^{e^{10^122}} as the period.
- **Corrected claim (branch).** Three quantities are kept distinct: ord | lcm(1..n), with ln lcm = ψ(n) ~ n; Landau's
  g(n), with ln g ~ √(n ln n); and the Erdős–Turán typical order ½(ln n)², valid only for σ uniform on S_n. None is an
  OI recurrence time, and the corpus adopts no model of φ. For the exactly linear fixed-graph rule (A5), N ≤ q^D − 1. |S|
  is not fixed by visible data. No finite observation falsifies the framework as a whole.
- **Evidence.**
  - (1)–(3): cited theorems (PNT; Landau 1903; Erdős–Turán 1965, 1967), not re-proved.
  - (R): P (elementary proof).
  - X: `AUD/tracks/SC31-period-growth/period_growth_check.py`, `.out` on the branch (exact integers, fixed seed, 10
    controls; exhaustive 2×2 orders for the listed q).
  - The E[ln ord] samplers: N (a sanity check only).
- **Manuscripts (own diff).** book ch18, ch01, appendix-a (F8), appendix-b (:420), appendix-c, README, bibliography,
  FULL; papers/Explainer (:175).
- **Introduction (#918).** Unverified: #946 says "to verify", and the PR body does not state it.
- **Verification.**
  - Reviews retained at `AUD/tracks/FINAL-AUDIT/reviews/`: `967-REVIEW-2430948d.md` (ACCEPT WITH CHANGES, R1–R4) and
    `967-CONFIRM-beb24b35.md` (ACCEPT, with the record fix that `71c96578` applies: the control count is 10, not 11).
  - CI at `71c96578`: 25/26 success, 1 skipped.
- **Status.** PR #967, open, draft, head `71c96578`. It merges after #962.

### SC-22: the 𝒩-regime vocabulary (#964)

- **Flaw.** ch18 :74 (base `0d917665`): "The P-indivisibility measure $\mathcal{N}$ — quantifying the degree of
  non-Markovianity in the emergent dynamics — provides a continuous parameter interpolating between memoryless …". There
  were 43 occurrences across ch13, ch15, ch18 and the glossary (+ FULL), conflating revival, capacity and timescales. The
  ch18 :82–:88 table placed 𝒩 by τS/τB, which is not derived.
- **Corrected claim (branch).** On a window W, 𝒩 is the peak revival, max over preparation pairs and s < t of [d_t −
  d_s]⁺, with d the total variation of the visible population laws, and 𝒩 ∈ [0, 1]. The cumulative (BLP) backflow is
  named apart; it is unbounded on a finite bijection since Γ_{t+L} = Γ_t. 𝒩 > 0 certifies P-indivisibility, and the
  converse fails. Memory does not fix 𝒩. "Partially-quantum" becomes "restricted quantum-statistical regime" at 57
  sites. The table is removed, and the candidate systems are labelled as the proposal's conjecture.
- **Evidence.**
  - Definitions and relabel: P.
  - Memory without revival: X (`AUD/tracks/SC22-N-regime/regime_exact.py`, `blp_unbounded.py`, `enum_window.py` with
    `.out`, landed on the branch byte-identical to the audit-branch blobs). `enum_window` is exhaustive at (2,2), (2,3),
    (3,2), with controls K1–K3.
  - Candidate-system placement: O (conjecture).
- **Manuscripts.** book ch18, ch13, ch15, ch09, ch01, ch19, appendix-a, appendix-c, glossary, readers-guide, FULL. No
  paper is touched.
- **Introduction (#918).** None (PR body).
- **Verification.**
  - Track records: `AUD/tracks/SC22-N-regime/REPORT.md` (audit) and `tracks/SC22-N-regime-fix/README.md` (branch).
  - Reviews retained at `AUD/tracks/FINAL-AUDIT/reviews/`: `964-REVIEW-eaeed819.md` (ACCEPT WITH CHANGES, R1–R4) and
    `964-CONFIRM-621fbf2c.md` (ACCEPT).
  - Owner decisions (i)–(iii) are incorporated.
  - CI at `621fbf2c`: 25/26 success, 1 skipped.
- **Status.** PR #964, open, draft, head `621fbf2c`. Exclusions remain: ch01 :225 and appendix-c :62 keep the old label.

### SC-17: compressed Bell-ceiling summaries, Explainer part (#963)

- **Flaw.**
  - Explainer :709 (base `0d917665`): "Entanglement is the algorithm's encoding of correlations that were written into
    the hidden sector during preparation and haven't been read back yet".
  - Explainer :767: "The dynamics is unique" and selectors.
  - Explainer :771: "**No free parameters.** The wave equation is selected, not chosen".
  - Explainer :826: "The Higgs mechanism from one condition".
  - ch05 :95 and ch03 :186 (+ FULL).
  - Compressed ceilings at Explainer :58, :300, :338, :563, :665, :1017.
- **Corrected claim (branch).**
  - Bell is stated at Main §3.3's scope: under determinism and a ±1 outcome in every run, ontic parameter independence
    plus measurement independence gives |S_CHSH| ≤ 2. The framework gives up ontic parameter independence. H-Bell is the
    open compatibility hypothesis.
  - The form is fixed up to one coefficient α, and nearest-neighbour range is assumed.
  - Center independence carries neither memory nor P-indivisibility.
  - Explainer :771 now reads "**Few free parameters.**": one free geometric parameter ε, with σ undetermined.
- **Evidence.** P (alignment to Main §3.3, SM §4.1, SM §4.3, GR §4–§5). H-Bell and the descent of center independence:
  O.
- **Manuscripts.** papers/Explainer; book ch03, ch05, FULL.
- **Introduction (#918).** None (PR body); the track README checked the Introduction at `bace5ef8`.
- **Verification.**
  - Track record: `AUD/tracks/SC17-explainer-bell/README.md` on the branch.
  - Reviews retained at `AUD/tracks/FINAL-AUDIT/reviews/`: `963-REVIEW-2619c94b.md` (ACCEPT WITH CHANGES: R1, R2;
    O1–O6), `963-CONFIRM-81654257.md` (ACCEPT), `963-RECHECK-183c1a74.md` (REVISE: conditions on the gap equation and
    the 1/4 at :771; GR-selection framing at :974; self-assessment at :773), `963-RECHECK-e8b5d80c.md` (REVISE: "not
    consequences of" at :974 stronger than SM §4.1) and `963-CONFIRM-03f8b6ad.md` (ACCEPT).
  - CI at `81654257`: 25/26 success, 1 skipped. At `e8b5d80c`: 24 success, 1 skipped, 1 in progress (`Numerical probes /
    A41 independent`). At `03f8b6ad`: in progress when read.
- **Status.** PR #963, open, draft. The remote head is `03f8b6ad`, one commit after the `e8b5d80c` named for re-review.
  #966 (the SM Theorem 3 source-repair draft) is stacked on `81654257`.

### SC-33: Bell placement in Main and the book (#968)

- **Flaw.**
  - Main :700 (base `0d917665`): "Bell placement (outcome independence violation vs. superdeterminism)".
  - Main :766: "Reproducing quantum correlations therefore requires ontic parameter dependence, which … the specific
    SM/GR target implements through preparation-indexed state-dependent adjacency".
  - Main :558: "The Bell side is now separate rather than analogous" (§A.33).
  - Compressed ceilings at Main :22, :646 and ch00 :55, ch01 :16, :169, :183, ch02 :188, ch03 :162, :164, :180, ch04 :90,
    :92, ch18 :110, appendix-c :32, :34, glossary :19 (+ FULL).
- **Corrected claim (branch).** Main :700: "Bell placement (ontic parameter dependence with measurement independence
  retained vs. superdeterminism)". Main :766 states the either/or, with preparation-indexed adjacency as the proposed
  implementation under the open hypothesis H-Bell. Each compressed ceiling carries own-wing interventions and/or ±1 in
  every run.
- **Evidence.** P (alignment to Main §3.3; a deterministic completion satisfies ontic outcome independence
  automatically). H-Bell: O.
- **Manuscripts.** papers/Main; book ch00, ch01, ch02, ch03, ch04, ch18, appendix-c, glossary, FULL.
- **Introduction (#918).** None (PR body; the track README checked the Introduction at `3e600003`).
- **Verification.** Track record: `AUD/tracks/SC33-bell-main-book/README.md` on the branch. Independent review retained at
  `AUD/tracks/FINAL-AUDIT/reviews/968-REVIEW-6b200f67.md`: REVISE (B1, graph separation missing at four book ceilings;
  B2, H-Bell's no-signaling requirement stated as fact at ch03 :180 and ch18 :110). The revisions are in progress.
  CI at `6b200f67`: in progress when read.
- **Status.** PR #968, open, draft, head `6b200f67`. Drafting status was given as "branch
  corpus/sc33-bell-main-book"; the PR was opened at 20:52Z.

### SC-32: SM Theorem 3 displayed as an equivalence (branch `corpus/sc32-sm-theorem3`)

- **Flaw.** SM :300 (base `0d917665`): "**Theorem 3.** *Center independence of the lattice dynamics is equivalent to
  exact chiral symmetry of the emergent staggered fermions.*" Both proof lines prove one direction. The Remark (:304)
  exhibits C = 2(1−d) with exact chiral symmetry (§A.34).
- **Corrected claim (branch).**
  - Theorem 3 is stated at α = 1/d as one direction: C = 0 gives the square of the massless staggered operator, and a
    mass m ≠ 0 gives C = ±m².
  - New Lemma 3a: K(C,α) = B² − μ, with μ = C − 2(1 − dα).
  - New Proposition 3b: at fixed α = 1/d, chiral ⇒ C = 0.
  - The display carries no "iff". The converse as displayed is false (α = 1, C = 2(1−d)).
  - Open: anisotropic or next-nearest-neighbour rules, and operator-valued on-site masses.
- **Evidence.**
  - Proved direction and Lemma 3a: P, with X (`AUD/tracks/SC32-sm-theorem3/theorem3_exact.py`, `.out` on the branch;
    `Fraction`; countercontrols rejected; "VERDICT all controls green").
  - Converse refuted as displayed: X (rows RM and H).
  - Proposition 3b: P, using the kernel identity `Chiral.center_anticommutator` (`verification/lean/OI_Structural_Core.lean`).
    No `#print axioms` line for it was found, so its axiom evidence is unverified.
  - Ledger on the branch: `SM:T-3` K2 → K1; `SM:L-3a` and `SM:P-3b` added at K1. None of the converses is
    kernel-certified.
  - The related author proof and bounded exact checks in #965 (first-order on-site converse) are unreviewed and not
    adopted.
- **Manuscripts.** papers/SM; LEDGER; `verification/lean/ROADMAP.md`. Explainer :826 and ch05 :95 (+ FULL :1424) are left
  to SC-17. The `OI_Structural_Core.lean` docstring and `structural_chain_probe.py` are left to #966.
- **Introduction (#918).** #946: "dependency to assess, not an automatic new #918 blocker". The SC-32 record finds no use
  of Theorem 3 outside SM. Introduction check: unverified.
- **Verification.** Track record `AUD/tracks/SC32-sm-theorem3/README.md` on the branch (sourced from SC-17's two
  independent reviews). Independent review of SC-32: none located. CI at `97d5b37c`: no check runs returned.
- **Status.** Drafting. Branch head `97d5b37c` (one commit on `0d917665`). No PR found for the branch. Related drafts:
  #965 (head `d2e01a3a`), #966 (head `f522e62f`, a patch generator only, no applied source edits).

***

## SC-23 (not a unit with a PR)

- **Finding F1.** Main :159–161 (fast-bath lemma) reads an exponential bound as exact vanishing: "(C4) fails",
  "$M_t = 0$". Sites: Main :161, :165, :742, :754, :756; Complexity :204; Explainer :926–:932; Substratum :56, :351,
  :492; ch03 :58, ch04 :178, :182, ch01 :227, glossary :27, ch02 :194 (+ FULL), at `1a60e06b`.
- **Finding F2.** One-step thermalization is read as window-wide Markovianity, T^(k) = T^k. Sites: Main :439, :445,
  :447, :494; Explainer :357–361; Substratum :129; ch01 :51, :225, :227; glossary :27 (+ FULL). Also Medicine :35
  ("controlled by τS/τB"), and Main :439 (≪) against :447 (≲).
- **Evidence (WIP, unreviewed).**
  - `AUD/tracks/SC23-fastbath-closure/`: `PREREG.txt` and `PREREG2.txt` frozen before computation. `f1.py` is void (a
    failed positive control). `f1b.py` and `f2.py` report "ALL CONTROLS GREEN", and the coordinator replayed both byte
    for byte.
  - F1 counterexample model G: X.
  - F2 counterexamples M1–M4: X, exhaustive over Z2×Z2 and Z2×Z3.
  - No Lean statement is involved.
- **Status.** The proposed lemma text and the Main :445 text are unreviewed drafts. No source PR exists.

## Open findings recorded on #946 that are not yet units

| Finding | Sites (at `0d917665` unless stated) | Recorded where | Status |
|---|---|---|---|
| SM cycle-ergodicity tension | SM :294–:296 (the linear rule is integrable; full-shell sampling relies on the threshold nonlinearity, which :296 says "vanishes in the continuum/large-$q$ limit"); SM :1211 (gap (ii), made conditional on cycle ergodicity by SC-28) | Named in this ledger's brief. #962 and `AUD/tracks/FINAL-AUDIT/slice1-main-companions.md` (D-11) record the SM :1211 non-sequitur, which SC-28 corrects. No record stating the :294–:296/:1211 tension as a separate finding was located | statement of the finding *unverified*; no unit |
| Main :766 and :558 | Main :766 (either/or dropped; "implements"); Main :558 ("is now separate") | #946 comment of 17:46Z | addressed by the SC-33 draft #968, unreviewed |
| Explainer section labels | Explainer Bell section and :1017 cite "§3.2" (Main's Bell section is §3.3); Explainer "§3.3" for Main §3.4 at :346, :352, :1009, :1018–:1020 (#955 deferred list) | #946 comment of 17:46Z; #963 follow-ups | deferred. The owner's deferral is given in the brief; no retained record of it was located *(unverified)* |
| Selector residuals | Substratum :48, :159, :323; SM :110, :296 (review numbering :291); Complexity :27 | #963 follow-ups; `tracks/SC17-explainer-bell/README.md` | open; no unit |
| 𝒩 symbol collision | SM §7.2 and ch06 :179 taste-loop 𝒩 = 1/9, against the revival measure 𝒩 | #964 exclusions; `tracks/SC22-N-regime-fix/README.md` | open; not renamed |
| SC-29 review follow-ups | O5 `driveQ_localityPreserving`; O6 cite `driveQ_smul`, `driveQ_one` (Main :268, :584; GR :292); O8 census note for the joint-law reading; O9 possible stale P on `MAIN:T-finite-horizon-process-dilation` | #946 comment of 17:46Z | open |
| SC-32 follow-ups | ch05 :95 (+ FULL :1424) to name α = 1/d; `OI_Structural_Core.lean` docstring "zero iff the center terms vanish" | `tracks/SC32-sm-theorem3/README.md` | open; left to SC-17 and #966 |
| Explainer :340 caps | "FAILS" (§A.33) | #946 comment of 17:46Z | open |
| Main :82 and other compressed ceilings | Main :82 omits ±1 in every run; glossary :49, appendix-c :42, ch03 :40 (+ FULL); "That condition is now downstream of a harder one" at ch01 :171, ch03 :180, Main §3.3, Explainer :340, Methodology :339 | `tracks/SC33-bell-main-book/README.md` | left for #946 |

Units on #946 with no source-fix PR yet (listed for completeness, not ledgered here):
- SC-5 residue (S9-A3 Pinsker hypotheses; S9-D1 "certified exactly");
- SC-6 (CP-indivisibility);
- SC-7 (BH-01 record);
- SC-8 to SC-15 (FINDINGS (d) PR-A to PR-H, including the SC-11 Main §3.4 imprecisions, SC-13 probe statements and SC-14
  coverage gaps);
- SC-19 (C3 presented as following from C4, Main :78);
- SC-30 (low items);
- the SC-20 shift-register τ_B tension;
- the SC-21 follow-up at ch04 :178.

## Cells marked unverified or flagged

1. Introduction-side closure on #918 for SC-1, SC-2, SC-3, #951, SC-4 and SC-20. The r16 mapping was read; review of the
   applied changes was not checked. #918 is open, draft, head `3e600003`.
2. SC-2: the script behind the reviewer's 78 exact checks.
3. SC-3: the reconciliation-review verdict at `fb3eecce`.
4. SC-20: the 3,000-model probe is a sample, not exhaustive.
5. SC-26: the SM :112 enumeration is not committed.
6. SC-28: the verdict on `51ba6652` (delta confirmation pending); the TφT = φ⁻¹ check file.
7. SC-31: the Introduction dependency.
8. SC-32: the axiom evidence for `Chiral.center_anticommutator`; the Introduction check; any review.
9. Open findings: the SM cycle-ergodicity finding statement; the owner deferral of the Explainer section labels.
