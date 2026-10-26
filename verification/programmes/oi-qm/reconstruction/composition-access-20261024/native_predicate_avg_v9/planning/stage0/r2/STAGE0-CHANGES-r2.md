# Stage 0: changes from `STAGE0-PLAN.md` (r1) to `STAGE0-PLAN-r2.md`

`STAGE0-PLAN.md` (SHA-256 `4720ac77…71429`) is unchanged and remains the reviewed
object. The review is `review/STAGE0-REVIEW.md` (SHA-256 `3392ca66…fc19`).
Section numbers below are r2's.

## Required changes

| item | where | how |
| --- | --- | --- |
| R1, exact soundness (C15) | §6 C15; §5a; §9 | The production closure is dimension-parametric. C15 checks it on exhaustive 1D (2^21 worlds) and 2D (2^18 worlds) windows, under A geometry and under G geometry with a frame, against `s0native.py`, an independent native evaluator. Every rule mutant runs through it, and wrong far tip fails it (C15 in the toy runs). |
| R2, mutant list | §6 mutant table | Parity-dropped is removed as equivalent; the run is kept as evidence (it fails nothing). Wrong far tip, B-only off-axis, un-applied elimination and skip-record are added. Every rule mutant runs under A and G; B-only off-axis does not apply under G. |
| R3, planted families and code-level C1, C2, C7 | §6 C1, C2, C3, C7 | Families {q} ∪ all near and far tips are planted for every convention, type and depth. G plants sit outside the frame, with in-frame vacuity contrasts. C1 and C2 test the production `in_cone` and `tips`. C7 uses `s0ref.py`, which has its own context, cone and tip code and a different algorithm. |
| R4, parity re-run | §9; `stage0-design-r2/` | The toys are re-run at L = 4 with Φ even, and the r1 parity error is stated. One artifact is new: r1's "symmetric" variant actually deleted the far cone, and with correct parity, symmetric radii are equivalent (see the comments below). |
| R5, symmetry | §1 E4; §6 C8; §12 S4 | C8 compares only C4v-invariant attributes. Source-dependent attributes are per record. Equivariance of retained sets is checked. Orbit-weighted counts must equal the full counts (owner's S4 condition). |
| R6, distinguishability | §3 (a)–(c) | Replaces "observer interface" with: observer-equivalence classes; the private dependence set (J cells, other Φ cells, sources); and the stated limit that operational distinguishability is Stage 1. |
| R7, COLLAPSE_ALL wording | §5 | Collapse is established by the exact closure computation (C0–C18 green) and turned into law failure by the proved C_A and C_G. P_A and P_G play no part in it. |
| R8, base precondition | §3; §5 BASE_RESIDUE; §6 C6 | The base context is hand-derived under A and G (the reviewer's derivation, restated), checked in C6 before its computed value is read. If it fails, the labels are base-relative. |
| R9, §A.41 table | §7 | Adds rows for exactness (C15), the audit (C18), completeness (C17, C13), non-vacuity, orbit attributes (C8), the base precondition, design parity, mutant non-equivalence, distinguishability, the minimal witness (C16, order defined) and evidence retention (C13: `result.json`, `expected-controls.json`, recipe). |

## Owner decisions folded in (2026-10-26)

| decision | where |
| --- | --- |
| S6 approved and run as a labelled proof-check | header; §9; §12 |
| S1a included; S1b and S1c deferred (decided by S1a's result, never by available resources) | §12 |
| S4 approved, with count preservation | §6 C8; §12 |
| S9: every listed work checked first-hand before any novelty claim | §8; §12 |
| Three independent safeguards: soundness, completeness, non-vacuity | §5a; C15, C17, C18, C13, C3 |
| Three-way observer classification kept | §3 (a)–(c) |
| Execution steps 1–2 done; 3–5 pending | header; §9 |

## Optional items

| item | status |
| --- | --- |
| P_A-dir in C11 (reviewer's O-c) | stated as P_A-dir (§4); open item S11, recommended |
| Literature additions (finding 6) | added to §8 |

## Points not adopted as stated, with reasons

1. **The symmetric-radius countercontrol** (owner's original list; RECHECK §3.2)
   is replaced. On even-class contexts every far-slice cell lies at distance
   ≡ d − 1 (mod 2), so radius d and radius d − 1 select the same cells.
   Symmetric radii therefore cannot change any closure. It is removed as
   equivalent. Its run (`symmetric_blind`) fails no closure-level control; C1's
   radius-attainment check detects it at the definition level only. Three
   mutants are added in its place, each caught by a named control:
   parity-preserving radius −2 and radius +2, and "far cone deleted".
   - r1's 160-of-400 "symmetric" difference was an artifact. The parity
     mismatch caused it, together with an implementation that emptied the far
     cone instead of widening it.
2. **B-only off-axis under G** does not apply: convention G has no B-type
   quantity at depth ≥ 1. It runs under A only. The full-convention off-axis
   mutant runs under both.
3. **C15 does not test the off-axis mutants.** They need depth ≥ 2 in two or
   more dimensions, which is beyond the exhaustive windows. C2, C3 and C18 catch
   them.
4. **C7 does not catch the near-only mutant on the toy class**: production and
   reference agree on all 1,400 toy records. C3's centre-removed block catches
   it. This is recorded as an observation about the toy class, not a defect.
5. Nothing else is declined.
