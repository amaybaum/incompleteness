# Thread J — running notes (read-only; certified main 6d0abf6b)

Worktree: threads/J/wt at 6d0abf6ba5467e0b0c1f5437a03ae6bd22f9c28a. KF = KInfFoundations.lean.

## Tree facts verified
- KF:63 `FiniteStage` (P, E finite, table p in [0,1], unit). KF:81 `vec`, KF:84 `states` = convexHull of range vec
  in `S.E → ℝ`. KF:149 `fullEffects`, KF:154 `PerfectlyDistinguishable` (needs only effects on Ω summing to 1, each
  certain on its state; no `avail`). KF:899 `response_eq_one_forces`, KF:924 `exists_zero_of_classicallyExposed`.
- `FiniteStage` is used in no other module (grep: no hit outside KF). There are no stage maps, no directed system,
  no completion object in the field-neutral vocabulary. KF header: "It sources nothing".
- No identifier containing predictive rank / predictive dimension anywhere in OIBridge.
- Main.md:352: "stagewise finiteness does not prove that this completion retains finite predictive rank".
  Main.md:542: an exact-completion reconstruction "must additionally show that its chosen completion retains finite
  predictive dimension". Main.md:538 fixes one realization; Main.md:540 the SIC embedding, sharp |0><0| extends to
  1/2 + √3/2 at an ontic vertex.
- Matrix regime only: RegionLimit `inclObs` RL:102 (X ↦ X ⊗ 1), `tensorOf_mul` RL:116, `trace_inclObs_mul` RL:125;
  RegionTower `inclObs` RT:123, `inclObs_trans` RT:152, `trace_inclObs_mul_restrict` RT:190, `restrict_trans` RT:233,
  `Consistent` RT:319, `consistent_mix` RT:341. Header: "no infinite-volume algebra ... is constructed".
- Ontic conditioning: `quotMeasure_branch` PQ:410; DomainGlue header: the classical branch domain is closed under
  reversible evolution and visible branch selection (ontic, simplex-valued).
- The completion definition Ω∞ = cl conv{p(·|s)} ⊂ [0,1]^{E∞} (product topology) is in the scratchpad design note
  k-infinity/K-INF-DESIGN.md §2 — not in the repo, not governed. It presupposes "maps carrying readbacks and
  preparations forward consistently", which is never stated as a condition.

## Reasoning log
1. Under the design-note completion, e_v ∈ E_σ ⊂ E∞ gives the coordinate π_{e_v}. It is linear on ℝ^{E∞},
   continuous in the product topology, [0,1]-valued on the whole cube, and its value at the carried preparation
   x_v is the table entry. So the extension question collapses to: is the carried table entry still 1 (resp. 0)?
   That is exactly stage consistency (SC). Nothing about rank, compactness or dynamics enters.
2. Typing in KF: ℝ^{E∞} for infinite E∞ has no norm instance; KF's V needs one. ℓ^∞(E∞) works: every point of the
   cube is bounded, evaluation is a norm-1 continuous linear functional. PD (KF:154) does not ask compactness.
   So the KF-typed statement needs no finite predictive rank either. (Compactness in KF's norm topology would fail
   in general; not needed for PD.)
3. Pressure test (favourable reading): the partner effect. With e₂ = 1 − π_{e_v} the PD sum is automatic. If the
   partner must be the other *visible readback* e_{v'} (availability-minded reading, Thread H), then
   π_{e_v} + π_{e_{v'}} = π_unit must hold on preparations that first appear at later stages; SC on carried
   preparations does not give that. Second premise TP: forward maps carry tests (outcome families summing to the
   unit) to tests. Only needed for the available-partner reading.
4. Loss of sharpness in a limit occurs for a *limit of stage seeds* (pointwise), not for a fixed-stage seed.
   Countable-simplex tower: e_n = π_n sharp on (δ_n, δ_0) at stage n, e_n → 0 pointwise on Ω∞; δ_n → 𝟘 (unit 1,
   every visible coordinate 0) in the product topology; 𝟘 ∈ Ω∞ violates the infinite visible partition of unity.
5. SIC: the seed hypothesis itself (a sharp visible pair) is unsatisfiable by response effects on the SIC ball, and
   conditioning on a visible cell leaves the ball image; closing under it gives Δ₃.
6. Double dissociation for rank: C1a (two-stage inconsistent tower, finite rank) fails; countable simplex (infinite
   affine dimension) passes for a fixed-stage seed. Rank is neither necessary nor sufficient; SC is load-bearing.
