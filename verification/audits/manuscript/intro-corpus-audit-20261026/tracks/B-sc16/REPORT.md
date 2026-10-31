# Track B report — SC-16 (saved by coordinator from the agent hand-back; agent could not write files)

Base `6bc2c4af`. Read-only; nothing committed by the agent. Decision rule: `PREREGISTRATION.txt`, written before any
result. Code: `oi_exact.py` (exact simplex with checked certificates), `families.py`, `controls.py`, `run_families.py`,
`enumerate_all.py`, `converse_check.py`, `addendum.py`; outputs in `out/`; edit list `proposed_edits.md` (E1–E23, old
strings checked verbatim at `6bc2c4af`). Scripts import siblings: run from this directory with `python3 -B <script>`.
`out/enum_33.txt` is a partial (3,3) run stopped under §A.40; no verdict rests on it.

## Verdict: refuted
(C1)–(C4) as Main §1.3 states them, with (C4) at an accessible order inside {0..n} (n below the first visible return
r), do not imply that the rooted family is P-indivisible on {0..n}, under all four readings: R1 Main :137 (Γ_t = Γ_s Λ,
Λ stochastic, all s<t≤n); R2 Λ_{s,t} the realized kernel P(X_t|X_s); R3 Main :121 TV-monotonicity for all p, q; R4 the
same for point roots. Exact countermodels exist, including families with gap order and window an arbitrarily small
fraction of the recurrence time. All controls green. What (C1)–(C4) do imply on an accessible window: accessible
non-Markovianity (positive conditional mutual information, Main's readback lemma), as Main §2.3 Scope (:141) states.

## Definitions
Γ_t(a,j) = μ_H{h : π_V φ^t(a,h) = j}, μ_H shared by every root, uniform visible prior; window n < r (r = first t ≥ 1
with Γ_t = I). (C4): some k ≤ n−1 and two positive-probability histories with the same present and different next-step
laws. (C1) literal: successor of some reachable (c,h) depends on h; also C1-hist and "T non-permutation". (C2)
structural: at the gap order the hidden-state laws given the two histories differ; slow form checked only as a static
bath. (C3): log2 n_H ≥ I*, exact integer-power comparison.

## Countermodels (index s = x·n_H + h)
(a) XOR, (2,2), uniform μ_H: φ(x,h) = (h, x⊕h), permutation [0,3,1,2]; X_0 = x, X_1 = h, X_2 = x⊕h, L = r = 3;
Γ_0 = I, Γ_1 = Γ_2 = J/2; P-divisible on {0,1,2} (Λ_{0,t} = Γ_t, Λ_{1,2} = I); (C4) at order 1, gap 1; (C1) X_2 = H_1;
(C2) H_1 = X_0⊕X_1 written at step 1, read at step 2; I* = 1 bit = log2 2.
(b) Static bath, n_V = n_H = p prime: φ(x,h) = (x+h mod p, h); Γ_t = J/p for 1 ≤ t ≤ p−1, Γ_p = I; P-divisible on every
window short of recurrence; gap 1 at order 1; (C2) slow holds literally (τ_B = ∞); I* = log2 p; k/r = 1/p → 0. Main :80
admits it ("a pre-sampled hidden variable revealed by the history satisfies it").
(c) LFSR, (2, 2^m): state (X_t,…,X_{t+m}), primitive recurrence of degree m+1, L = r = 2^{m+1}−1; Γ_t = J/2 for
1 ≤ t < L; no gap below order m, gap 1 at every order m..L−1. Paper proof: X_t is a nonzero linear functional of the
initial state; with no hidden part it equals x, forcing φ^t = id; otherwise uniform given the root. Computed m = 1–5
(several polynomials) and x^7+x+1 (r = 127, gap order 6).

Exhaustive (R1 countermodels / bijections with an accessible C1∧C2s∧C4 window):
| (n_V,n_H) | uniform μ_H | skewed μ_H | point-mass μ_H |
|---|---|---|---|
| (2,2) | 8 / 12 | 4 / 12 | 0 / 4 |
| (2,3) | 576 / 576 | 232 / 576 | 0 / 160 |
| (3,2) | 240 / 616 | 24 / 616 | 0 / 462 |
| (2,4) | 21888 / 36864 | 18376 / 37392 | 0 / 10080 |
| (4,2) | 4224 / 39200 | 480 / 39200 | 0 / 35880 |
Largest r among R1 countermodels: 15 at (2,4). Static-bath countermodels: 6 at (3,2), 24 at (4,2) uniform.

Controls: K1 swap P-indivisible on {0,1,2}, Farkas (1,−3,−3,1,1,1); K2/K3 matrix pairs; K4 LP vs closed-form 2×2 on
2,401 pairs; K5 Main Scope equivalence (gap below L ⇔ some Γ_s non-permutation ⇔ P-indivisible on {0..L}) on every
enumerated model, 0 violations; K6 TV checker; K7 (C3) on every countermodel. Every feasible verdict carries an exactly
verified Λ, every infeasible a verified Farkas vector. R3 exact for n_V ≤ 4; for n_V > 4 decides only the equal-rows case
(covers the static-bath families).

## Established, by kind of evidence
1. Accessible conditional memory from (C4): Main :167, I ≥ p_0δ²/ln 2 — paper proof; XOR value exact.
2. Indivisibility across the recurrence cycle (Main :137, :141): Lean `OIBridge.EquivalenceChain.isPermMatrix_of_stochastic_inverse`
   (hA, hB row-stochastic, A*B = 1 ∨ B*A = 1 ⇒ A permutation); composition with P-divisibility and gap → non-permutation
   Γ_s on paper; K5 exact.
3. Converse (new): under a full-support visible prior, P-indivisibility on {0..n} ⇒ a (C4) gap at some order ≤ n−1.
   Paper proof (no gap ⇒ Markov on {0..n}, Γ_t = Q_0⋯Q_{t−1}, Λ_{s,t} = Q_s⋯Q_{t−1}); exact: 0 violations in 10,612 windows.
4. Special case (new): if the visible trajectory is a function of the root (e.g. point-mass μ_H), a gap at order k ⇒
   P-indivisible on {0..k+1}: the gap is Lean's `C4e (k+1) Γ`; `OIBridge.CausalReadback.c4e_implies_pIndivisible`
   (h : C4e K Γ ⊢ PIndivisibleWithin K Γ); also `c4r_implies_pIndivisible`. Exact: zero countermodels under point-mass
   priors. Caveat: there literal C1 holds but C1-hist fails.

## Missing assumption
P-divisibility on {0..n} depends only on Γ_0..Γ_n; (C1)–(C4) constrain the multi-time law and leave those free (XOR and a
memoryless register share Γ_0, Γ_1, Γ_2). Needed: root-level collision-and-revival (C4e) or distinguishability revival
(C4r) inside the window — kernel-proved sufficient. Not supplied by (C2) slow (static bath), time-homogeneity (every
uniform-prior countermodel is stationary), or (EM) (pushes Γ_t toward rank one, where divisibility holds).

## Coordinator addendum
1. (2,3) [0,3,4,1,5,2], uniform μ_H: reproduced with own code (already the largest-r (2,3) countermodel): L = r = 6;
   Γ_1 = Γ_5 = [[1/3,2/3],[2/3,1/3]], Γ_2..4 = [[2/3,1/3],[1/3,2/3]], Γ_6 = I; P-divisible on {0..5} (Λ_{1,2} = Λ_{4,5} =
   flip, Λ_{2,3} = Λ_{3,4} = I); not on {0..6}, Farkas (1,−5,−5,1,1,1); gap δ = 1 at orders 1–6; literal C1 and C1-hist;
   (C3) saturated; distinguishability monotone on {0..5}; RoutedReadbackAtStorage at K = 2 with witness (0,1,1,1,2,0)
   and three others, fails at K = 1. Confirmed.
2. (c) LFSR confirmed m = 1–5 (two degree-4 polynomials) plus paper proof. (d) HMM (g ~ BSC(1/50), p_0 = 1/5,
   p_1 = 2/5, g_0 uniform): Γ_t = B((1+λ_t)/2), λ_t = E[Π_{i<t}(1−2p_{g_i})], exact t ≤ 9, λ_1..4 = 2/5, 124/625,
   8552/78125, 614896/9765625; exact LP P-divisible on {0..9}; paper proof Λ = B((1+λ_t/λ_s)/2) needs λ positive
   non-increasing, matching Lean `ScalingFamily.pDivisible_below`; gaps at orders 1–5 (order 1: 8/175); routed readback
   at storage already at K = 2 (hence K = 4); the ledger never influences the visible law. Confirmed.
3. Lean (`CausalReadback.lean`): `PDivisible K Γ` = ∀ s<t≤K ∃ row-stochastic Λ, Γ t = Γ s * Λ; `C4e K Γ` = ∃ a≠b,
   s<t≤K, Γ s a = Γ s b ∧ Γ t a ≠ Γ t b; `C4r` the same with tv(Γ s a, Γ s b) < tv(Γ t a, Γ t b). Both no-go theorems
   hold for an arbitrary real family Γ with no other hypothesis. `rootedMap` with `RootedRealization` = Main :137's Γ_t;
   `PDivisible K` = Main's "P-divisible on {0..K}". C4e/C4r are one-time-marginal conditions, not Main's history-level
   (C4); the module says it does not relate them.
4. Definitions: rooted family and P-divisibility identical across Track B, Track D and Lean; point roots vs arbitrary
   initial laws immaterial (same Λ serves all). Gap existence depends only on the support of the visible prior. Shared
   prior vs stationary initial law coincide for uniform μ_H and uniform visible prior; countermodels also under skewed
   non-stationary priors. Lean defines no accessible window; Track B uses n < r. No verdict depends on a definitional
   choice except that point-mass priors give no countermodels (item 4 above).
5. Safeguard: the countermodels refute no formal theorem in Main or the kernel (Main :137 concerns n with Γ_n = I, and
   every countermodel is indivisible at its return; the readback lemma and the characterization theorem concern
   conditional memory; `pdFamily_pDivisible`, `not_c4e_and_not_c4r_of_pDivisible`,
   `routedAtStorage_forces_return_indivisibility` and `PhysicalC4Discharge`'s "not on the same window" remark are all
   consistent). They refute the manuscript reading "C1–C4 (or routed readback) give accessible-window P-indivisibility".

## Sites (replacement text in proposed_edits.md)
E1 Complexity :418; E2 Complexity :461 = ch15 :112 = FULL :4073; E3 Complexity :462 and ch15 :114 = FULL :4075
("exceeding the (C2) threshold yields memory"; Main :76: persistence alone does not supply (C4)); E4 Complexity :478;
E5 Complexity :503; E6 Explainer :294; E7 Explainer :767 (selectors contradicted by SM :226, :228, :236, :240);
E9 ch17 :178 = FULL :4757 (flag: re-audit row B7, appendix-a :151 = FULL :5688); E10–E12 ch01 :121/:127–129/:133 =
FULL :465/:471–473/:477; E13 appendix-b :420 = FULL :6187; E14 appendix-b :92 = FULL :5859; E15 ch18 :72 = FULL :4890;
E16 ch15 :83 = FULL :4044; E17 Computation :144; E18 Explainer :892; E19 Explainer :581; E20 Explainer :619; E21 SM :306
(and :236), borderline; E22 Explainer §3.3→§3.4 numbering (:346, :352, :1009, :1018–:1020) and :352 "unconditional"
needs a full-support visible prior; E23 Main :153 and the :167 lemma title.
Checked and correctly scoped: Main :20, :82, :141, :174, :334, :716; Explainer :351, :373, :411; Medicine :13, :33;
Bioinformatics :14, :44, :80; Complexity :360; Structure :1141, :1147, :1175, :1249; glossary :99, :105, :119; ch00 :53;
ch01 :89; ch15 :67. Substratum :108, :122 borderline but in the true direction (item 3).

## Errors beyond the listed sites
- "Information backflow" in two senses: conditional memory (Main :334) vs distinguishability revival certifying
  P-indivisibility (Main :121, :149; Explainer :143). XOR has 1 bit of the first and none of the second. E23 renames the
  :167 lemma "accessible conditional memory from readback", rewrites :153 (which also cites (C2) as the lemma's
  hypothesis), and reserves "information backflow" for the trace-distance sense.
- ch01 :127 = FULL :471 derives the conditional-memory bound from storage alone; Main :155, :172 require readback (E11).
- Complexity :462 and ch15 :114 = FULL :4075: the "sharp transition" at the (C2) threshold is not derived (E3).
- Explainer cites the characterization theorem as §3.3; it is §3.4 (§3.3 is Bell).
