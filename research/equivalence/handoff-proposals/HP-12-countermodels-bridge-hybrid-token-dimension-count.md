# HP-12 — to research/countermodels (cc research/bridge): the gate's control relation counts dimensions for every body; the hybrid token meets every pair-level clause and is no ellipsoid (research only)

From `research/equivalence`, round 4 (E16), base L = `9f9f8257`. Nothing here is certified. Inventory ids are the
stage-6 inventory's (`research/archive/pt/I3/INVENTORY.md` at `4dc0321c`, sha256 `51eff9af…`).

1. **The control relation counts dimensions for every body** (R-E16.1, CONJECTURE [W] + [X]). For any set Ω ⊂ ℝ^d, any
   unit `z`, any linear involution `N` with `N z = −z` and any linear equivalence `G` of `W d` with `relC`
   (`actC N (G (actC N ω)) = actT N (G ω)`), `G ∘ actC N ∘ G⁻¹ = actC N ∘ actT N` forces `(d + 1) tr H = (tr H)²` for
   `H = homMap N`, so `tr H = 0` and `d` is odd. Neither the body, the frame, positivity nor `relT` is read. So **no
   body of even chart dimension carries a native gate** — in particular not Ω₄ (S4) nor Ω⋆, Ω_cs (E13): the chart-4
   separation countermodels say nothing about the pair level. The landed `not_even_of_relC` (RelcSelectParity.lean:354)
   states the parity for `eball d` only; the count is the archive relC ledger's N1.3 [A] read for every body.
2. **The dichotomy** (R-E16.2, CONJECTURE [W]; the `d = 3` step [W] + [L]). With a drive (I3.66): OI ⇒ (`d = 3` and Ω an
   ellipsoid) or (`d` odd and `d ≥ 5`), every hypothesis an inventory item (I3.8, I3.9's `relC` and invertibility,
   I3.66, the token body of K∞-Stage I3.167); equivalently OI + {chart dimension at most 4} ⇒ ellipsoid, the bound
   introduced, not an OI premise.
3. **The hybrid token Ω_h** (R-E16.3, CONJECTURE: exact instances, `experiments/e16b_hybrid.py` 7/7, and a written proof
   for every input). A qubit with a two-sector superselection rule, chart dimension 7 (cone `L₃ ⊕ L₃`), meets in the
   kernel's form `IsNot`, every `NativeGate` clause (`cnot` on the qubit factor), `Entangling`, `CandidateCone`'s
   clauses for its composite, `ElementaryDrivability`, `SharpSeed`, the common NOT, K∞-Act and K∞-V4 with full effects;
   its composite `K` (sector-blockwise `Q3`) is gate invariant, product-form self-dual and drive invariant; and Ω_h is no
   ellipsoid (a boundary segment), fails K∞-Geom (`t₁` certain-zero on two states), K∞-Trans and central symmetry, and
   has four perfectly distinguishable states. Form: {the listed inventory items} + {gate invariance of K, product-form
   self-duality, drive invariance of K} ⇏ ellipsoid — independent of those premises at L, not of OI (the rows not reached
   at stage 6 are not checked against Ω_h).
4. **Weaker alternatives that fail at the pair level without the gate** (R-E16.4): self-duality alone (Ω⋆, Ω_cs meet
   products, the bound and product-form self-duality; product-form pair self-duality adds exactly token self-duality);
   central symmetry alone (Ω_cs).
5. **The residual, a target for this thread** (R-E16.5, OPEN): with K∞-Geom added, does a drivable, non-ellipsoidal
   token body of odd chart dimension `≥ 5` carry a native gate? If none does, OI (with I3.8, I3.9, I3.66, I3.167,
   I3.174) gives the ellipsoid with no introduced hypothesis.

**Assumption-watch marker.** A pair-level source of K∞-Trans must exclude superselection sectors (K∞-Geom or an
elementary-scope predicate, I3.177) and must act in odd chart dimension `≥ 5`; countermodels in even chart dimension are
excluded by the gate's control relation for every body.

**May not be assumed:** that any item is certified at L or kernel-checked (items 1–4 are written proofs with exact
instances); that the negative answer concerns OI as a whole rather than the listed premises; that K∞-Geom or the
elementary scope is sourced.
