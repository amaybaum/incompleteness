# Thread TWO-LE — sourcing `2 ≤ d` (read-only, from 8daf2bc0)

Status: scoping only. No branch, no round, no ROADMAP wording, no premise adopted.
Nothing below is kernel-checked; the Lean in `TwoSharpTests.sketch.lean` is uncompiled.

## Target

On `eball d`: `2 ≤ d` iff there exist two sharp binary tests inequivalent modulo complementation.

## T0 — the predicate, stated on states (gem-check result)

The predicate is stated by values on Ω, not by equality of affine maps:

    TwoSharpTests Ω :=
      ∃ e f, SharpSeed Ω e ∧ SharpSeed Ω f ∧ (∃ x ∈ Ω, f x ≠ e x) ∧ (∃ x ∈ Ω, f x ≠ 1 - e x)

Hidden assumption exposed: if the test were identified with the affine map (`f ≠ e` as maps),
a body Ω whose affine span is not the whole carrier would count as distinct two effects that
agree on every state, so the count of tests would be inflated by functionals no observation
separates. On `eball d` the two readings coincide (the ball has nonempty interior), so the ball
theorem does not depend on the choice, but any later sourcing on a general Ω does. Recorded as an
assumption-watch marker: **operational identity of tests is agreement on Ω.**

`SharpSeed` is OG-1's (OrbitGeneration:65): an effect on Ω with a certain state and a zero
state. So the predicate is field-neutral as stated; only the theorem is about `eball d`.

## Proof plan (all steps from landed lemmas)

- **T1 complement identity.** `sharpEff (-b) x = 1 - sharpEff b x` for all `x` (from
  `sharpEff_apply`; the sums negate). Map form: `sharpEff (-b) = const 1 - sharpEff b`.
- **T2 sharp seeds are sharp directional effects.** `SharpSeed (eball d) e →
  ∃ u, ∑ u_j² = 1 ∧ e = sharpEff u`: unpack the seed and apply `sharp_eq_of_certain`
  (EffectSpace:181). Landed; no new mathematics.
- **T3 d = 0.** `eball 0` is a single point, so no effect is certain at one state and zero at
  another: `¬ SharpSeed (eball 0) e`. Hence no tests at all.
- **T4 d = 1.** A unit `u : Fin 1 → ℝ` is `z1` or `-z1` (`u 0 ^ 2 = 1`). So any two seeds are
  `sharpEff (±z1)`; either `f = e` or, by T1, `f x = 1 - e x` on every `x`. Both disjuncts of
  the predicate fail. The countermodel is the classical bit of `two_le_load_bearing`.
- **T5 d ≥ 2 witness.** `e = sharpEff (Pi.single 0 1)`, `f = sharpEff (Pi.single 1 1)`, both
  seeds by `sharpEff_sharpSeed`; at `x = Pi.single 0 1 ∈ eball d`: `e x = 1`, `f x = 1/2`,
  `1 - e x = 0`, so one state separates `f` from `e` and from `1 - e`.
- **T6 equivalence.** `TwoSharpTests (eball d) ↔ 2 ≤ d`: (→) by T3/T4 on `d ≤ 1`;
  (←) by T5. Both directions have their own witnesses (§A.34): T3+T4 for →, T5 for ←.

Corollary chain (each link a separate theorem, no equivalence claimed beyond T6):
`TwoSharpTests (eball d)` → `2 ≤ d` → (with K1-BRIDGE-1's relative hypotheses, IsNot,
NativeGateOf) `d = 3` via `three_of_nativeGateOf_of_two_le`.

## Gem-finding pass

- **G1 (NEW, assumption-watch):** test identity must be agreement on Ω (T0). POSITIVE for the
  ball, binding for any general-Ω sourcing.
- **G2 (POSITIVE):** nothing already in the selector chain implies `2 ≤ d`: at `d = 1`
  `SharpSeed`, `BoundaryTransitive (fullAut 1)` and the classical gate all hold. Consistent with
  `two_le_load_bearing`. So the predicate is a genuine new input, not a restatement.
- **G3 (gap in the landed controls, ELABORATING):** `two_le_load_bearing` shows `2 ≤ d` is
  load-bearing for the **absolute** selector only. For the **relative** selector, the d = 1
  instance needs K1-BRIDGE-1's hypotheses at `d = 1`: avail = `fullEffects (eball 1)` (sound),
  `G = fullAut 1`, `r = sharpEff z1`, `boundaryTransitive_fullAut`, V4 from seed transports
  being effects, and `NativeGateOf` from `NativeGate` through `maxConeOf_fullEffects`. Every
  ingredient is landed; the instance is not. Short lemma; should precede any manuscript
  statement that `2 ≤ d` is "the" remaining premise of the relative selector.
- **G4 (BORDERLINE, alternative predicate):** a preparation-side form — some state has two
  distinct decompositions into boundary states — is also expected equivalent to `2 ≤ d` on the
  ball (d = 1: the interval decomposes uniquely; d ≥ 2: the centre is the midpoint of two
  different antipodal pairs). Not proved. Neither form is sourced by trace-out alone: a classical
  joint distribution traced out gives a simplex, where both fail. Whichever is sourced, the
  sourcing step is a non-classicality input, and must be named as such.

## Boundary of the earned statement (if T6 lands)

On the derived elementary ball, `2 ≤ d` is equivalent to the existence of two sharp binary tests
inequivalent modulo complementation. It does not show that OI supplies two such tests.

## Correction (after thread P, base 06b6f94e)

G4's claim that "a classical joint distribution traced out gives a simplex, where both fail" is
wrong for simplices with three or more vertices. The trit (triangle) has two sharp tests distinct
modulo complementation: the barycentric coordinates lambda_A and lambda_B, separated from each
other at A and from 1 - lambda_A at C (exact check). On any compact convex body HasTwoSharpTests
is equivalent to affine dimension >= 2 (thread P, written proof plus six exact bodies). The
classical failure holds only for the two-vertex simplex (the bit). The landed K1-SHARP-TESTS-1
records make no classical claim (their non-inference rule states none); the error is confined to
this ledger and to chat messages.
