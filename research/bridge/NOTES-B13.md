# NOTES-B13 — the reachability theorem B7-1 as a design-module statement, with its finite case proved

Node B13 of `research/bridge` (round 3). Base L = `9f9f8257`. The module is
`verification/lean-mathlib/OIBridge/BridgeReach.lean` on the disposable branch `dev-bridge/r3-reach`, cut from
`research/bridge`. Its verbatim copy is `research/bridge/lean/BridgeReach.lean`. Evidence levels: [D] design module
built in CI; [X] exact computation (`experiments/b13_preflight.py`); [W] written here; [A] audited record.

## S0. Success criterion and predictions (written 2026-10-11T01:09:22Z, before the preflight run and the dispatch)

**Success criterion (round-3 directive).** A design-module statement of the reachability theorem B7-1 (RESULTS B7-1:
every compact group `H` of unitary and antiunitary conjugations of the pair whose identity component is abelian misses
some pure state with `H·P`), with its finite cases proved. One dispatch at most.

**Reading of "finite cases".** The case of a finite group `H`. Its identity component is trivial, so it is abelian.
The cases of B7-1 with `dim H₀ ≥ 1` (NOTES-B7 §1, §2, §4) are not attempted.

**Design.**
- **Carrier.** Pure vectors are `PVec = Fin 2 × Fin 2 → ℂ`, `ψ (a, b)` with `a` the first token. A vector is a
  product iff the determinant of its coefficient matrix, `prodDet ψ = ψ₀₀ψ₁₁ − ψ₀₁ψ₁₀`, vanishes. Only the direction
  "product ⟹ `prodDet = 0`" is used.
- **The statement.** Two definitions, `ReachUnitary` and `ReachAnti`, quantify over closed subgroups `H` of
  `Matrix.unitaryGroup (Fin 2 × Fin 2) ℂ` whose identity component is commutative.
  - `ReachAnti` adds an antiunitary coset `H·κ`, `κ = K ∘ conj`, with the two conditions that make `H ∪ Hκ` a group:
    `K · conj(h) · K* ∈ H` and `K · conj(K) ∈ H`.
  - The conclusion: some `v ≠ 0` such that no element of the group carries `v` to a product. Since `H` is a group,
    this says `[v] ∉ H·P`.
  - Working in `U(4)` rather than `PU(4)` loses nothing [W]. The preimage of a compact projective group is compact,
    and its identity component is abelian iff the projective one is (NOTES-B7 §1).
- **The finite case** is an avoidance lemma: finitely many functions, each nonzero somewhere and quadratic along every
  line `v + n·w` (`n ∈ ℕ`), have a common non-root.
  - The proof is by induction. Given `v` avoiding the earlier functions and `w` with `f_j w ≠ 0`, among the
    `2·|s| + 1` points `v + n·w` one avoids all of them. A quadratic with three distinct roots vanishes (pigeonhole).
  - For a unitary `U`, `v ↦ prodDet (U v)` qualifies, and so does `v ↦ prodDet (U v̄)` for the antiunitary
    `U ∘ conj` (a natural-number parameter is fixed by `conj`). `U U* = 1` gives a non-root through `|00⟩ + |11⟩`.
- **Controls.**
  - Positive control: an explicit `ψ = (1, 2, 3, 5)` avoids products under the identity and under `CNOT`
    (`prodDet = −1`, `−7`).
  - Two countercontrols:
    - the zero matrix is quadratic along lines but has no non-root, so the unitarity hypothesis is load-bearing;
    - two complementary step functions, each nonzero somewhere, have no common non-root, so the quadratic hypothesis
      is load-bearing.
- **Toolchain.** No local Lean (as in B11). Every Mathlib name used is checked against the pinned sources (`v4.33.0`,
  raw.githubusercontent.com, read into the session scratchpad). In this tag:
  - the unitary lemmas live in the namespace `Unitary`;
  - `Finset.induction_on` is `@[elab_as_elim]` with explicit insert binders;
  - the pigeonhole lemma is `Finset.exists_lt_card_fiber_of_mul_lt_card_of_maps_to`.

**Productivity test (§A.31), fixed now.** B13 is a gem iff writing the statement precisely, or proving the finite
case, yields a fact strictly stronger than the obvious restatement of B7-1 that constrains something or exposes a
hidden assumption. Examples: a hypothesis of B7-1 that the written proof uses without stating it, or a reduction of
the antiunitary case. Otherwise B13 is ELABORATING: a formalization.

**Predictions.**

| id | prediction | check |
|---|---|---|
| S0-1 | Every algebraic identity the module relies on holds exactly: the expansion of `prodDet` along a line; `prodDet (a ⊗ b) = 0`; the three-root lemma for quadratics; conjugation fixes natural-number parameters; `prodDet (|00⟩ + |11⟩) = 1`; the control values `−1`, `−7` (with `CNOT` as the map `(a, b) ↦ (a, b ⊕ a)`). The sufficiency `2·|s| + 1` holds: on `2·|s| + 1` points, `|s|` nonzero quadratics leave a common non-root | `b13_preflight.py` P1–P6 |
| S0-2 | The CI build of the module succeeds: Build green; every `#print axioms` line of the module on `[propext, Classical.choice, Quot.sound]`; `lean-axioms` PASS; the gate red only on `claims`, `duplicate`, `lean-manuscript` | dispatch, job log |
| S0-3 | If the build fails, the most likely failure points are, in order: (i) elaboration of the statement definitions (topology on the nested subtype for `connectedComponent`, the coerced subgroup in `IsClosed`); (ii) `prodDet_bellV` and the controls (deciding `Fin 2` literals); (iii) the induction in `exists_avoid` (motive, `choose`, pigeonhole) | job log |
| S0-4 | Gem classification ELABORATING. NEW only if the formal statement exposes a hidden assumption of B7-1 | §3 |
