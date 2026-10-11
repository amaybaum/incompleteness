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

**S0 outcome.**
- S0-1 held: `b13_preflight.py` run 1 (01:10:34Z) gave 7/7 PASS, VERDICT B13-PREFLIGHT-OK; the replay is
  byte-identical.
- S0-2 held: the build succeeded on the single dispatch (§2), with 21/21 `#print axioms` lines standard and
  `lean-axioms` PASS.
- S0-3 did not arise. The fallback branches show which first alternative closed each goal (§2).
- S0-4 held: ELABORATING (§3).

## 1. What the module states

`lean/BridgeReach.lean` (sha256 a6e055e4…; dev blob 7a279393). The section numbers are those of the module.

| declaration | content |
|---|---|
| `PVec`, `M4`, `U4` | pair vectors `Fin 2 × Fin 2 → ℂ`; pair matrices; `Matrix.unitaryGroup (Fin 2 × Fin 2) ℂ` |
| `prodDet`, `prodCross`, `kron2`, `conjV`, `bellV` | `ψ₀₀ψ₁₁ − ψ₀₁ψ₁₀` and its polarization; `a ⊗ b`; entrywise conjugation; `|00⟩ + |11⟩` |
| `AvoidsProducts v g` | `g v` is no product `a ⊗ b` |
| `prodDet_kron2`, `avoids_of_prodDet` | products have `prodDet = 0`, so `prodDet (g v) ≠ 0` gives `AvoidsProducts v g` (only this direction is used) |
| `prodDet_add_smul`, `conjV_add_natSmul`, `conjV_conjV`, `prodDet_bellV`, `prodDet_zero` | `prodDet` is quadratic along lines; conjugation fixes natural-number parameters and is an involution; `prodDet (|00⟩ + |11⟩) = 1` |
| `IdCompComm H` | the identity component `connectedComponent (1 : H)` of a subgroup of `U4` is commutative |
| **`ReachUnitary`** (definition) | B7-1 for unitary groups: every closed `H ≤ U4` with `IdCompComm H` has some `v ≠ 0` that no `h ∈ H` carries to a product |
| **`ReachAnti`** (definition) | B7-1 with an antiunitary coset `H κ`, `κ = K ∘ conj`. The hypotheses: `K conj(h) K* ∈ H` for `h ∈ H`, and `K conj(K) ∈ H`, which make `H ∪ H κ` a group (preflight P7). The conclusion: some `v ≠ 0` with neither `h v` nor `h K conj(v)` a product |
| `QuadAlong`, `quad_eq_zero_of_three`, **`exists_avoid`** | the avoidance lemma (S0 design) |
| `quadAlong_mulVec`, `quadAlong_mulVec_conj`, `exists_ne_zero_of_mul_star`, `exists_ne_zero_of_mul_star_conj` | unitary and antiunitary conjugations qualify |
| **`reachUnitary_finite`**, **`reachAnti_finite`** | the conclusions of both statements for every finite subgroup `H`, with no hypothesis on the identity component and none on `K` |
| **`reachUnitary_of_infinite`**, **`reachAnti_of_infinite`** | each statement follows from its restriction to infinite closed subgroups: the finite case is discharged |
| `ctl_cnot_witness`, `ctl_avoids` | positive control: `(1, 2, 3, 5)` has `prodDet = −1`, and its `CNOT` image has `−7` |
| `ctl_counter_zero`, `ctl_counter_step` | countercontrols: the zero matrix (quadratic, no non-root); two complementary step functions (each nonzero somewhere, no common non-root) |

## 2. CI record (dispatch 2 of 3; the only dispatch of B13)

- **Run.** 38101591388: `verify.yml`, `workflow_dispatch` on `dev-bridge/r3-reach` @ 747bcf94, created 01:22:01Z. The
  dev commit's parent is research/bridge 7266e30b. It adds the module and one root import line.
  - The run waited in the queue behind run 38101580750 of another thread until the job started at 01:33:55Z. Nothing
    was cancelled.
- **Mathlib bridge job 114358450003.**
  - **Build: success**, 01:34:13–01:36:15Z: "⚠ [3644/3646] Built OIBridge.BridgeReach (1.7s)", warnings only,
    then "Build completed successfully (3646 jobs)".
  - **`#print axioms`: 21/21 on `[propext, Classical.choice, Quot.sound]`** (module lines 355–375). The declarations
    are `prodDet_kron2`, `avoids_of_prodDet`, `prodDet_add_smul`, `conjV_add_natSmul`, `conjV_conjV`,
    `prodDet_bellV`, `prodDet_zero`, `quad_eq_zero_of_three`, `exists_avoid`, `quadAlong_mulVec`,
    `quadAlong_mulVec_conj`, `exists_ne_zero_of_mul_star`, `exists_ne_zero_of_mul_star_conj`,
    `reachUnitary_finite`, `reachAnti_finite`, `reachUnitary_of_infinite`, `reachAnti_of_infinite`,
    `ctl_cnot_witness`, `ctl_avoids`, `ctl_counter_zero` and `ctl_counter_step`.
  - **Release gate** (01:36:15–01:36:47Z). `lean-axioms` **PASS** ("OK (5881 named result(s) reported, no sorr…").
    This is consistent with the module's 21 named results. B11's run, whose dev tree carried the dictionary's 20
    instead, reported 5880.
  - The gate fails only on `claims`, `duplicate` and `lean-manuscript`. All three are red by construction on research
    branches.
  - The `lean-manuscript` problem is the one expected. A local run of `tools/lean_manuscript_census.py` on the
    exported dev tree (evidence for this thread only, not an attestation, §A.40) reports exactly "UNCLASSIFIED module
    BridgeReach has no registry family".
  - Job conclusion: "failure", from the gate only.
- **The warnings.**
  - Unused `done` and never-executed fallbacks in `conjV_add_natSmul` (100, 101), `conjV_conjV` (106, 107) and
    `prodDet_bellV` (111–113). In each, the first alternative closed the goal: `simp only` with the named lemmas, and
    `simp [prodDet, bellV]`.
  - `push_neg` is deprecated in favour of `push Not` (line 171), a warning only.

## 3. Reading and verdict

- **B7-1 now has a precise formal statement** in two parts. `ReachUnitary` covers unitary groups; `ReachAnti` covers
  groups with an antiunitary coset. The finite case of each is a design statement built in CI ([D]).
  `reachUnitary_of_infinite` and `reachAnti_of_infinite` state formally that what remains of B7-1 is its infinite
  closed subgroups, i.e. the cases `dim H₀ ≥ 1` of NOTES-B7 §1, §2 and §4.
- **What writing the statement fixed** [W]:
  - **The antiunitary coset needs two explicit conditions.** `K conj(h) K* ∈ H` and `K conj(K) ∈ H` are what make
    `H ∪ Hκ` a group (preflight P7). B7-1's written proof uses them through the group structure: the group permutes
    the eigenspaces of its identity component and normalizes the maximal torus (NOTES-B7 §1). The finite case needs
    neither.
  - **Conjugation preserves products.** So an antiunitary coset contributes the set `H K·P`, a unitary coset applied
    to the products.
  - **Working in `U(4)`.** Projective groups are covered by their preimages in `U(4)`.
- **The finite case is elementary and needs no group structure.** The avoidance lemma, with `quadAlong_mulVec`,
  `quadAlong_mulVec_conj` and the two non-root lemmas, covers any finite family of unitary and antiunitary
  conjugations; the two theorems state it for finite subgroups. Invertibility alone would suffice [W]. The proof
  avoids finitely many quadratics along a line.
- **Propagation.** B7-4's fixed-finite-substratum case uses B7-1 only for finite groups. That reachability step is
  now [D] (row B13-2). The tower case is unchanged: it still needs Jordan [L] and the written proof of B7-1 for tori.
- **Gem classification: ELABORATING**, as predicted (S0-4). The productivity test is not met: the formal statement
  exposes no hypothesis that B7-1's written proof uses without stating, and the finite case is the expected
  nowhere-density fact.
- **Not claimed.**
  - B7-1 for subgroups of positive dimension.
  - Formal non-vacuity of `IdCompComm` [W]: `U(4)` itself is excluded, its identity component being non-commutative.
  - The identification of table-level pair groups (on `W 3`) with groups of conjugations beyond the dictionary
    statements of B11 [D].
  - Certification or any census disposition.
