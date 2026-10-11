# NOTES-E18 — the power cone of Ω⋆ is self-dual: a design module in polynomial form

Base L = `9f9f8257`. Node E18 of round 4 (owner's priority 4; "if budget"). Source: R-E13.1 and NOTES-E13 §1: Ω⋆'s
state cone, in the coordinates `u = T + S`, `v = T − S`, is the power cone `P = {u, v ≥ 0, u^{1/3} v^{2/3} ≥ ‖X‖}`, self-dual
for `⟨z, w⟩ = TT' + SS' − (1/3)(TS' + ST') + X·X'` — a written proof (weighted AM–GM; explicit converse witnesses) with
exact checks (`e13_selfdual_body`, [X]). The node asks for a design module: the identities, the nonnegative pairing and
the converse witnesses.

## S0 (written 2026-10-11T04:38Z, before the probe's first run and before the module is written)

**What E18 is (§A.31).** Closure-mode formalization. It counts if the self-duality of `P` for that form — both
inclusions — is a Lean theorem built in a design run with the standard axioms, with exact instances agreeing first.

**The polynomial form (fixed now).** With `S = Σ X_i²`, `P = {(u, v, X) : 0 ≤ u, 0 ≤ v, S³ ≤ u² v⁴}` (for `u, v ≥ 0`,
`‖X‖ ≤ u^{1/3} v^{2/3} ⟺ ‖X‖³ ≤ u v² ⟺ S³ ≤ u² v⁴`): no real powers, no square roots. The form in `(u, v)` coordinates is
`B(z, z') = u u'/3 + 2 v v'/3 + X·X'` (ring identity from `T = (u + v)/2`, `S = (u − v)/2`).
- *Self-positivity* (`z, z' ∈ P ⇒ B ≥ 0`): with `a = uu'`, `b = vv'`, `m = (a + 2b)/3 ≥ 0`, AM–GM is the polynomial
  identity `(a + 2b)³ − 27 a b² = (a − b)²(a + 8b)`, so `m³ ≥ a b²` and `m⁶ ≥ (u²v⁴)(u'²v'⁴) ≥ (S S')³ ≥ D⁶` with
  `D = X·X'` (Cauchy–Schwarz in Lagrange form, `D² ≤ S S'`); cube monotonicity on `[0, ∞)` gives `D² ≤ m²`, hence
  `m + D ≥ 0`.
- *The converse* (`B(z, z') ≥ 0` for every `z ∈ P` ⇒ `z' ∈ P`): `(1, 0, 0)` and `(0, 1, 0)` lie in `P` and give `u' ≥ 0`,
  `v' ≥ 0`. If `S'³ > u'² v'⁴`, an explicit point of `P` pairs negatively: for `u', v' > 0`, with `ρ = u'² v'⁴ / S'³ < 1`,
  `θ = (5 + ρ)/6` and `s = θ S'/(u' v')`, the point `(v' s, u' s, −X')` (membership by Bernoulli,
  `θ⁶ = (1 − (1 − ρ)/6)⁶ ≥ ρ`; pairing `(θ − 1) S' < 0`); for `u' = 0`, the point
  `((v' + 1)² (S' + 1)/S', S'/(v' + 1), −X')` (pairing `2 S' v'/(3(v' + 1)) − S' < 0`); for `v' = 0`, `u' > 0`, the point
  `(S'/(u' + 1), (S' + 1)(u' + 1), −X')` (pairing `S' u'/(3(u' + 1)) − S' < 0`). All witnesses are rational in the data.
- *Hypotheses (rule 1).* None: the statements are about an explicit cone and form, with no OI content and no
  introduced hypothesis. Their bearing is R-E13.1's: Ω⋆ is a self-dual, drivable, non-ellipsoidal token, so token
  self-duality is not a source of K∞-Trans; the module would move the self-duality step of R-E13.1 from [W] + [X] to [D].

**The probe `experiments/e18_powercone.py` (decision rule in its header).** Exact rational arithmetic. Predictions
(sign, strength, reason):
- W1 PASS, certain: the form identity at 50 random rational points (a ring identity).
- W2 PASS, certain: AM–GM's factorization at 200 random rational `(a, b)`, and `B ≥ 0` on 400 pairs of exact rational
  points of `P` (points built on its boundary and inside it).
- W3 PASS, very high: for 300 random rational `z'` with `u', v' > 0` and `S'³ > u'² v'⁴`, the interior witness lies in `P`
  and pairs negatively; Bernoulli `θ⁶ ≥ ρ` at each.
- W4 PASS, very high: the two boundary witnesses on 100 random rational `z'` each.
- W5 PASS, certain: the poles `(1, 0, 0)`, `(0, 1, 0)` lie in `P`, and a `z'` with `u' < 0` or `v' < 0` pairs negatively
  with one of them.
- Countercontrols, each failing as stated, certain: XW1 "the witness with `θ = (1 + ρ)/2` lies in `P`" (fails at
  `ρ = 99/100`: `(199/200)⁶ < 99/100`); XW2 "AM–GM with weights `½, ½`: `((a + b)/2)³ ≥ a b²`" (fails at `(1, 4)`).

**Prediction for the node.** The probe renders its verdict; the module states and proves the form identity,
self-positivity and the converse with these witnesses; the build risk is in the division algebra of the witnesses
(`le_of_mul_le_mul_right` rather than `le_div_iff`, whose name has moved) and in Bernoulli (`one_add_mul_le_pow`, with an
`nlinarith` fallback), moderate. It rides in dispatch 2 (the budget plan of the LOG entry of 04:33Z). Label after a green design run:
CONJECTURE [D] for the self-duality of `P` in polynomial form.

## 1. The probe (measured)

`experiments/e18_powercone.py` run 1 (started 04:38:20Z, after commit `8f3baf2e`; decision rule unchanged): 5/5,
`COUNTER XW1/XW2 fails as stated`, `VERDICT E18-POWERCONE-SELFDUAL-EXACT`; replay byte-identical (py `402f9e88…`, out
`aa53f144…`). Measured: the form identity at 50 points; AM–GM's factorization at 200 points; 40 exact points of `P`
(boundary points `u = p³/q²`, `v = q`, `X = p · (3, 4, 12)/13` up to signs and order, and inner scalings), minimum `B`
over 400 pairs `1238533/4542720 > 0`; the interior witness in `P` with negative pairing at 300 exterior points, Bernoulli
at each; both boundary witnesses at 100 points each; the poles; XW1 fails at `ρ = 99/100` (`0.9704 < 0.99`), XW2 at
`(1, 4)` (`125/8 < 16`). Every S0 prediction held.

## 2. The design module (reading rule and prediction, written 2026-10-11T04:48Z, before dispatch 2)

`lean/EqvPowerCone.lean` (blob `e7d7a286`, sha256 `477a9f1f…`, 319 lines, 7 prints), namespace
`OIBridge.EqvPowerCone`, importing only Mathlib: `sq3`, `dot3`, `PC`, `B`; `form_eq`; `dot3_sq_le` (Lagrange);
`cube_le_cube`, `le_of_cube_le`; `amgm`; `B_nonneg` (self-positivity); `pole_u_mem`, `pole_v_mem`; `bernoulli6` (through
`θ⁶ − (6θ − 5) = (θ − 1)²(θ⁴ + 2θ³ + 3θ² + 4θ + 5)`, no library lemma); `mem_PC_of_dual` (the converse, three cases);
`PC_selfDual`. Two changes from S0's plan: Bernoulli is proved by that factorization instead of `one_add_mul_le_pow`;
the `v' = 0` witness has second coordinate `S' + (u' + 1)² + 1` (so that `b⁴ ≥ b² ≥ S'(u' + 1)²` is elementary) instead
of `(S' + 1)(u' + 1)` — both points pair negatively and lie in `P` (the probe's W4 checked the S0 witness; the module's
is checked by its proof).

**Reading rule (fixed now).** As NOTES-E15 §5, for `EqvPowerCone`'s seven prints: BUILT / PARTIAL / NOT BUILT. BUILT
moves R-E13.1's self-duality step (in polynomial form) to CONJECTURE [D].

**Prediction.** BUILT, moderate (about 0.5): the risk is in the `field_simp` identities of the witnesses, the
`nlinarith` certificates of `B_nonneg` and `le_of_cube_le`, and the destructuring of set-builder membership.
