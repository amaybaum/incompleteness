# NOTES-C8 — non-orthogonal Bell-type sets with three or more members

Node C8 (round 2; C4.4's first open item). Bell-type defects in matrix normalization: `d_g = I − 2gg†` (`= 8 pauliW(z_g)`),
`g` maximally entangled; `K(Z) = (Q3 ∩ Z*) + cone Z`; `⟨d_g, d_h⟩ = 4|⟨g|h⟩|² ≥ 0`. Cap vectors are written in the
`ψ` basis of NOTES-C2; real combinations of `ψ_1, ψ_3` (and of `ψ_2, ψ_4`) are maximally entangled, as is
`(3ψ_1 + 4iψ_2)/5`. A **Bell circle** is the set of maximally entangled states in a 2-dimensional subspace spanned by two
independent ones (a great circle of its Bloch sphere). Evidence levels as in NOTES-C1.

## S0 — predictions written before the first run of `c8_bell_sets.py` (2026-10-10T23:04Z)

Scratchpad exploration (numerical, not evidence): minimizing `⟨y₁, y₂⟩` over pairs in `K(Z)*` gave negative values for
line triples (`c = 0.2, 0.4, 0.6`), the regular triangle, square and pentagon on a Bell circle; `0` for an orthogonal
triple (control) and `−0.093` for a pair at `c = 1/2` (control). Random sampling of `K(Z)*` had missed every one of these
witnesses, so it is not used.

1. **Witness lemma (C8-L).** If `v, x ∈ ℂ⁴` and `λ ≥ 0` on the defects non-orthogonal to `d₁` satisfy (L1)
   `⟨vv† + Σλ_k d_k, d₁⟩ = 0`, (L2) `⟨vv†, d_k⟩ ≥ 0` for every `k ≠ 1`, (L3) `x†(vv† + Σλ_k d_k)x < 0`, (L4) `x†d_j x ≥ 0`
   for every `j ≠ 1` with `g_j ⊥ g₁`, then `y = vv† + Σλ_k d_k ∈ K(Z)* \ K(Z)`.
2. **Construction.** For a non-orthogonal pair `g₁, g₂` (`c = |⟨g₁|g₂⟩|² ∈ (0, 1)`), `W = span(g₁, g₂)`, a unit `e ∈ W^⊥`,
   `v = g₁ + εe`, `λ = (1 − ε²)/(4c)` on `g₂`, `x = g₂ − (⟨g₁|g₂⟩/ε)e`: (L1) holds, (L3) holds iff `ε² > c`, (L2) holds for
   every cap vector in `W` iff `ε² ≥ 2c_k − 1`, and for one outside `W` when `e ⊥ Π_{W^⊥}g_k`. Predicted: every Bell
   **triple** with a non-orthogonal pair and every finite set on one Bell circle with a non-orthogonal pair is not
   self-dual; exact instances: line triples at `c = 16/25` and `9/25`, the regular triangle (trine), the square, the
   regular hexagon, a triple with its third vector outside `W` non-orthogonal to `g₁`, and one with it outside `W`
   orthogonal to `g₁`.
3. Countercontrols: below the window (`ε² < 2c − 1`) (L2) fails for the line triple at `c = 16/25`; for `Z_F`
   (orthogonal) (L1) is unsatisfiable (`⟨d_k, d₁⟩ = 0` for all `k ≠ 1`).
4. Predicted OPEN: sets of four or more members not on one Bell circle whose `W^⊥`-projections are not parallel
   (conjecture: still not self-dual); the full Bell circle (a continuum) is handled separately (C7 prediction 5).

**Provenance note (added 2026-10-10T23:01Z, `date -u`).** The time in the S0 heading above is an estimate; by file
modification time this section was last written at 22:55:46 UTC, before `c8_bell_sets.py` (22:56:56) and its run 1
(22:57:10). The header time inside `c8_bell_sets.py` ("23:08Z") is likewise an estimate (LOG, correction entry).

## Runs
`c8_bell_sets.py`: run 1 12/12, `VERDICT C8-BELL-SETS-EXACT`, replay identical (out `d219d502…`). No pre-run edits.

## Results

### C8-L — the witness lemma [W]
Let `Z` be a finite set of Bell-type defects `d_k = I − 2g_k g_k†`, `d₁ ∈ Z`, `N₁ = {k ≠ 1 : ⟨g_k|g₁⟩ ≠ 0}`,
`O₁ = {k ≠ 1 : g_k ⊥ g₁}`. If `v, x ∈ ℂ⁴` and `λ_k ≥ 0` (`k ∈ N₁`) satisfy (L1) `⟨vv† + Σλ_k d_k, d₁⟩ = 0`,
(L2) `⟨vv†, d_k⟩ ≥ 0` for all `k ≠ 1`, (L3) `x†(vv† + Σλ_k d_k)x < 0`, (L4) `x†d_j x ≥ 0` for all `j ∈ O₁`, then
`y = vv† + Σλ_k d_k ∈ K(Z)* \ K(Z)`.
Proof. `y ∈ Q3 + cone Z`; `⟨y, d_k⟩ = ⟨vv†, d_k⟩ + Σ_j λ_j·4|⟨g_j|g_k⟩|² ≥ 0` for `k ≠ 1` and `= 0` for `k = 1`; so
`y ∈ (Q3 + cone Z) ∩ Z* ⊆ K(Z)*`. If `y = q + Σμ_k d_k` with `q ∈ Q3 ∩ Z*`, then `0 ≤ ⟨q, d₁⟩ = −Σμ_k·4|⟨g_k|g₁⟩|²`
forces `μ_k = 0` for `k ∈ N₁ ∪ {1}`, so `q = y − Σ_{O₁} μ_j d_j` and `x†qx ≤ x†yx < 0` by (L4). ∎

### The construction [W + X]
For `g₁, g₂` with `c = |⟨g₁|g₂⟩|² ∈ (0, 1)`, `W = span(g₁, g₂)`, a unit `e ∈ W^⊥`, `0 < ε < 1`: `v = g₁ + εe`,
`λ = (1 − ε²)/(4c)` on `g₂`, `x = g₂ − (⟨g₁|g₂⟩/ε)e`. Then `v†x = 0` and:
- (L1) `⟨vv†, d₁⟩ = ε² − 1`, `⟨d₂, d₁⟩ = 4c`: holds.
- (L3) `x†yx = λ(|x|² − 2|⟨g₂|x⟩|²) = λ(c/ε² − 1) < 0` iff `ε² > c`.
- (L2) `⟨vv†, d_k⟩ = 1 + ε² − 2|⟨g_k|g₁⟩ + ε⟨g_k|e⟩|²`: for `g_k ⊥ g₁` it is `≥ 1 − ε² > 0` always; for `⟨g_k|e⟩ = 0`
  (in particular `g_k ∈ W`) it is `≥ 0` iff `ε² ≥ 2c_k − 1`, `c_k = |⟨g_k|g₁⟩|²`.
- (L4) for `g_j ⊥ g₁`: if `⟨g_j|e⟩ = 0` (in particular `g_j ∈ W`), `|⟨g_j|x⟩|² = |⟨g_j|g₂⟩|² ≤ 1 − c` and (L4) holds when
  `1 + c/ε² ≥ 2(1 − c)` — automatic for `c ≥ 1/2`, else `ε² ≤ c/(1 − 2c)`; if `g_j ∈ W^⊥`, `⟨g_j|g₂⟩ = 0` and (L4) holds
  for every `ε² ≥ c`.
Choosing `g₂` a partner of `g₁` of maximal overlap `c` makes `2c_k − 1 < c` for every `k`, so the window
`ε² ∈ (c, 1)` (intersected with `ε² ≤ c/(1 − 2c)` when `c < 1/2`) is nonempty.

### Theorem C8 [W + X]
*Let `Z` be a finite set of Bell-type defects containing a non-orthogonal pair. Suppose some `g₁` with a non-orthogonal
partner, and a partner `g₂` of maximal overlap, admit a unit `e ∈ W^⊥` (`W = span(g₁, g₂)`) orthogonal to the
`W^⊥`-projection of every cap vector outside `W ∪ W^⊥` that is non-orthogonal to `g₁` or orthogonal to `g₁`. Then `K(Z)`
is not self-dual.* In particular:
- (a) **every Bell triple with a non-orthogonal pair** (at most one vector lies outside `W`; take `e` orthogonal to its
  projection);
- (b) **every finite set on one Bell circle with a non-orthogonal pair** (all cap vectors in `W`; any `e`);
- (c) every set whose cap vectors outside `W` lie in `W^⊥` (e.g. `Z_F ∪ {g}`, `g ∉ Z_F`).
This extends the pair theorem C4.1 ("only if") to these classes by a second, independent witness. Exact instances
[X]: line triples at `c = 16/25` (`x†yx = −323/20736`) and `9/25` (`−7/64`); the trine, pairwise `c = 1/4` (`−35/144`);
the square `{ψ_1, ψ_3, (ψ_1 ± ψ_3)/√2}` (`−7/288`); the regular hexagon (`−19/4050`); a triple with its third vector
outside `W` and non-orthogonal to `g₁` (`−323/20736`); one with it in `W^⊥` (`−323/20736`); the five-member
`Z_F ∪ {(4ψ_1 + 3ψ_3)/5}` (`−323/20736`). Countercontrols: below the window the construction fails (`⟨vv†, d₂⟩ = −3/100`
at `ε = 1/2` for `c = 16/25`); for `Z_F` (L1) is unsatisfiable, as Theorem S requires.
Together with W5 of NOTES-C7 (the full Bell circle, a continuum, by a different exact certificate), **no non-orthogonal
Bell-type configuration examined here has a self-dual surgery cone.**

## OPEN
- Finite Bell sets with two or more cap vectors outside `W`, with independent `W^⊥`-projections, for every admissible
  `(g₁, g₂)` (the smallest open case has four members). Conjecture C8-C: for every closed set `Z` of Bell-type defects,
  `K(Z)` is self-dual iff `Z` is pairwise orthogonal (then `|Z| ≤ 4`).
- Non-Bell defect sets with two or more members (C4.4's second item) were not attempted.

## Gem classification (§A.31)
- NEW: the witness lemma C8-L and Theorem C8 (all triples, all finite sets on a Bell circle, the `W^⊥` class): C4.4's
  first open item is settled for triples in the negative direction ("find a non-orthogonal triple with a self-dual
  surgery" — none exists).
- Process lesson (kept with the exploration record in LOG): random sampling of `K(Z)*` missed every witness here; the
  decisive numerical test was minimizing the pairing of two members of `K(Z)*` (`K` is self-dual iff `K*` is
  self-positive).
