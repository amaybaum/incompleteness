# COMPLEX-CARRIER-1, lane 2: can the real lift source the complex structure J? Plan

**WIP / UNVERIFIED. Model-written research record, paper-only. Nothing here is adopted, proposed
for the manuscripts or authorized beyond the lane scope.**

- **Accountable Issue:** #1217 (COMPLEX-CARRIER-1); parent #1211; programme #1169.
- **Authorization:** owner decision of 2026-11-26, quoted in #1169 comment 7184425769 (author
  amaybaum, owner timestamp 2026-11-26T06:25:53Z): "Approve all three execution scopes as written
  [...] | 2 | #1217 | Determine whether the complex structure J can be sourced from the real lift
  and its compatibility conditions." and "The existing restrictions remain: paper-only research,
  no computational experiments, no manuscript changes, no adoption of new premises and no
  automatic merges." and "NQ-1059 remains a conditional successor within #1217, not an
  automatically authorized second unit." and "A rigorous negative result or counterexample is as
  valuable as a positive derivation. Do not favor conclusions merely because they support OI."
- **Goal link (§A.47):** serves #1217 (tier foundational): decides whether Theorem 5's complex
  structure on the six-link carrier is supplied by the real lift's own compatibility data, is a
  separate bridge premise, or is open under a named hypothesis. Not the outcome expected.
- **Pinned main commit [P]:** `b6c6b80bbd4a878452e54759cc85f16c9ffb72da`. All SM line numbers
  below are at [P].
- **Writer:** lane 2 designated writer; local branch `research/i1217-complex-carrier-20261126`.
  No push, no GitHub writes, no dispatch.

## 1. Inputs

| Label | Source at [P] | Content used |
| --- | --- | --- |
| P-224 | SM:224, SM:228 | Form lemma of the center-free isotropic linear rule, stated "at either the substratum-symbolic level or an observer-level linear lift" |
| P-240 | SM:240 | Linearity (A5) is a further restriction beyond the affine condition |
| P-292 | SM:292 | Real lift: E positive definite for abs(alpha) below 1/d, semidefinite at 1/d with constant and (even L) staggered null modes, indefinite at alpha = 1 for d at least 2 |
| P-296 | SM:296 | Notation F(u,v) = (v, Av - u); conserved E, Q_B, P_C |
| P-312 | SM:312–316 | K-component second-order update; observer-level branch; matrix M |
| P-334 | SM:334–338 | Proposition 4b (symmetric point M = mu I_6; signed-permutation equivariance) |
| P-340 | SM:340–344 | Theorem 5 (stabilizer in U(6); Sigma = expectation of phi phi-dagger) |
| P-360 | SM:360–364 | H-link, V_phys = V_link tensor C^m |
| P-374 | SM:374 | Theorem 7, 6 = T_1 + E + A_1 under the cubic rotation group |
| P-505 | SM:505 | Carrier "equipped after-the-fact with the complex inner-product structure" |
| P-809 | SM:809 | "the real-to-complex step" named as an open joint |
| P-130 | SM:130 | "The custodial U(6) of the real lift (Theorem 5, §4.6)" |
| U1 | #1211 unit 1, BRIDGE-UNIT1.md r5, commit `820519cf` (off main, handoff branch), finding F4 and NQ1 | Provenance only. Every statement used here is re-derived on paper in REPORT.md. |

## 2. Questions (NQ1 of #1211, as scoped by the owner)

Setting: the real lift of the second-order linear update, phase space of pairs (u, v), with the
symplectic pairing, the conserved energy E and the cubic action on the six-link index.

- **(i) Canonicity.** Off the null modes, is the positive-frequency J the unique complex
  structure that commutes with the update and the cubic action, is compatible with the symplectic
  form and makes E positive? Which of these conditions does uniqueness need?
- **(ii) Null modes at alpha = 1/d.** Are they excluded on independent grounds, constrained, or
  the place where J fails?
- **(iii) Sigma.** Is SM's Sigma = expectation of phi phi-dagger J-Hermitian beyond a stationary
  product covariance on one mode, so that its stabilizer is U(3) x U(2) x U(1)?

## 3. Carriers

- **T:** the finite torus (Z/L)^d, N = L^d sites; null modes are discrete, normalizable modes.
- **Z:** l^2(Z^d); k = 0 is a measure-zero spectral point and J = (f - cos omega)/sin omega is
  unbounded near it, so J is a question of its domain.
- No result may rely on finite L unless stated for T only. The fundamental Z/q alphabet is out
  of scope; nothing here is claimed for it.

## 4. Named assumptions to carry

- **LIN:** the lift's linearity is itself conditional: on A5, or on the lift-level linearity of
  POSIT-MIN D1(b). Every result is stated conditional on the lift being the linear real lift.
- **b = 0:** for each result, state whether it needs the affine offset b to vanish.
- **LIFT:** the existence of the real lift itself (unit 1 B12) is not claimed.
- Any further hidden assumption found is named where it enters.

## 5. Method

Hand algebra only: Fourier reduction to 2x2 mode maps; Schur commutants for real-type
irreducibles; symplectic linear algebra; spectral theory for the unbounded case on Z. No
computation is run. Unit 1's exact checks C1 and C2 are listed as post-hold controls in
REPORT.md and are not run.

## 6. Productivity test (fixed before work)

The result is a gem iff it settles at least one of (i)–(iii) on a stated carrier, by proof or
counterexample (strictly stronger than unit 1's "candidate off the null modes"), **and** either
sources J for Theorem 5, shows J is a separate bridge, or exposes a hidden assumption (for
example degeneracy, energy positivity, or the domain issue on Z). Anything less is record-only.

## 7. Stopping rule

Stop when each of (ii) and (iii) reaches proved, disproved or a precise named gap on both
carriers; or when 3–4 consecutive passes yield no NEW finding.

## 8. Acceptance criteria

- (ii) and (iii) each reach proved, disproved or a named gap on both carriers.
- The conclusion states which holds: J sourced for Theorem 5 (conditional on the lift), J a
  separate bridge premise, or a named open hypothesis.

## 9. Exclusions

No manuscript edit; no adoption of a complex structure; no change to H-link; no claim that a
real-lift J sources the fundamental Z/q level; no claim of the lift itself; no computation; NQ-1059
is not started.

## 10. Deliverables

This PLAN.md (first commit), then REPORT.md in this directory: each question and its result per
carrier with status and proof or counterexample; the named assumptions; the conclusion; the
productivity verdict; open nodes; post-hold controls.
