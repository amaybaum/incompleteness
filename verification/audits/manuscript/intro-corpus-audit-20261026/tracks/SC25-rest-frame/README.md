# SC-25: the rest-frame "iff" of Main §3.5 (main `55e3217b`)

`cubic_counterexample.py` is an exact `Fraction` computation. Run it from this directory with
`python3 -I -B cubic_counterexample.py`; its output is `cubic_counterexample.out`, and it exits 0 only when every check
passes.

## The kernel
Take n = (1,0,0,0) and the metric diag(1,−1,−1,−1). T is the nearest-neighbour step kernel on ℤ³ with increments
S = {n ± e_i}, each with weight 1/6. A Lorentz Λ is an invariance of T when ΛS = S. S spans ℝ⁴, so the script finds
every invariance by trying all 360 basis images.

## Results
- G_T has 48 elements. All of them fix n, and their spatial blocks are the signed permutations, O_h. This is strictly
  smaller than Stab(n) ≅ O(3).
- n is still selected: parity lies in G_T, so the subspace G_T fixes is ℝn.
- Control: the rational rotation (3/5, 4/5) about z fixes n but is not an invariance.
- Countercontrol: the boost with cosh = 5/4 moves n and is not an invariance.
- With time-symmetric data S ∪ (−S), the group has 96 elements, O_h × O(1). It preserves ℝn but not n.

## What this shows
The lemma's hypotheses give only the inclusion of G_T (its orthochronous part, in Stab(n)). They do not give equality,
so the boxed biconditional and the "same fact" sentence rest on the unproved direction.

The computation does not determine G_T for the framework's own horizon map. Spatial isotropy remains an empirical input
(Main, posit (vi), E4).

## Replay
The coordinator replayed the script independently, and the output matched.
