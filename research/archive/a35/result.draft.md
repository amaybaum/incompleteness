# Track B act 35 — the Diţă hulls of the product-embedded stratum: RESULT

Run under `AGENTS.md` §A.39 as a native round, in one pull request, #755. This note is part of `E`,
so it records what was measured up to `E`. The attestations for `F` and `E`, the reconciliation, the
verdict on the receipt commit and the gate's check of this round's own receipt are recorded in the
receipt, `verification/receipts/A35.json`, and on the pull request.

- **`D`** — `100bb1e86931fa769a200e9b117f4f9fb0a745b9`, the head of `main` after act 34's landing.
- **`F`** — `a58d39ae569e6117ae0095aad464c2a3a7f625eb`, which adds amendment 1, blob `f0ced0ab64a85c4636ad29be6b47a6e7dd408e53`, to its parent
  `62479b5780c1c3e3809e5d49cf7e1cf3684ced80`, the child of `D` that adds the preregistration alone, blob
  `ca6c531bd28c0485f25a433ac3c344ae9cb973db`. The parent was designated by comment 5854712207 and held
  on the owner's review before any execution commit; the amendment carries the review's four
  corrections. `F`'s `check-run` attestation is run 36313785069; the owner's designation is comment
  @@FCOMMENT@@ on #755.
- **Shape** — non-sealing: no seal record, guard clause, manifest record or certificate.

**Outcome:** `A35-DITA-STRATIFIED`

| target | outcome at `E` | predicted |
| --- | --- | --- |
| `A35` | `A35-DITA-STRATIFIED`, theorem `a35_dita_stratified` | the same, very high |

The verdict theorem has the frozen statement `P_R` verbatim, compared after collapsing whitespace,
and so do the corollary `a35_c_exclusive` and the thirteen statements required under this label:
- `A35-1`: `a35_shared_hull`, `a35_shared_hull_t` and `a35_shared_hull_sub`;
- `A35-2`: `a35_shared_sigma_hull`;
- `A35-3`: `a35_shared_cross` and `a35_control_witness`;
- `A35-4`: `a35_control_twist`;
- `A35-5`: `a35_control_real`;
- `A35-6`: `a35_control_relabel`;
- `A35-7`: `a35_shared_extend`, `a35_shared_modulus` and `a35_shared_infinite`;
- the control `a35_control_untwisted`.

***

## The frozen post-round sentence

> @@SENTENCE@@

***

## What was proved, and how

The proofs follow the freeze's route. Throughout, `dita X Y D` is the column construction
`(a,b),(c,d) ↦ X[a,c]·D[c,b]·Y_c[b,d]`, `ditaT X Y E` the row construction
`(a,b),(c,d) ↦ X[a,c]·E[a,d]·Y_a[b,d]`, `gram H` the tuple `i ↦ (j,k) ↦ star (H i j) · H i k` of a
flat unitary `H`, `fl X` flatness of a `4 × 4` unitary with entries of modulus `1/2`, `Δc` and `Δr`
the two hulls, `S` act 34's stratum and `N` the product normalized set.

**`A35-1`, `a35_shared_hull`, `a35_shared_hull_t`, `a35_shared_hull_sub`.** The column construction
is unitary: a row-times-row entry of `H · star H` splits through `Fintype.sum_prod_type` into
`∑_c X[a,c]·star X[a',c]·D[c,b]·star D[c,b']·(Y_c · star Y_c)[b,b']`; the inner factor is `δ_{bb'}`
by the unitarity of `Y_c`, then `|D[c,b]|² = 1` and the outer sum is `δ_{aa'}` by the unitarity of
`X` (`a35_shared_dita_unitary`). Every entry has modulus `1/2 · 1 · 1/2` (`a35_shared_dita_norm`).
A flat unitary `H` of the product carrier pads to the dilation `U (p,_) (q,_) = H p q` over the
one-element ancilla, unitary because the ancilla sum is one term (`a35_shared_pad_unitary`), with
readback `‖H i j‖² = 1/16`, the product visible family; act 12's `sh1_necessity` makes its
fibre-Gram tuple, which is `gram H` by `fibreGram_apply`, realizable (`a35_shared_gram_realizable`).
The row construction is the transpose of the column construction at `Xᵀ`, `(Y a)ᵀ`
(`a35_shared_ditaT_eq`), so its unitarity is act 25's `transpose_unitary` applied to the former
(`a35_shared_hull_t_core`). Both hulls therefore lie in `N` (`a35_shared_hull_sub`).

**`A35-2`, `a35_shared_sigma_hull`.** A stratum point is `featureVec (X ⊠ Y)` with `X`, `Y`
realizable; act 12's `sh1_sufficiency` gives dilations `U_X`, `U_Y` over `Fin 4 × Fin 1`, whose
visible parts are unitary by act 21's `vpart_unitary` and flat by the readback
(`a35_shared_vpart_flat`); every entry of `X` is `star U_X (a,0) (j,0) · U_X (a,0) (k,0)`
(`a35_shared_gram_of_dilation`), so `X ⊠ Y` is `gram (dita X' (fun _ => Y') 1)` entrywise, and
also `gram (ditaT X' (fun _ => Y') 1)` (`a35_shared_sigma_core`).

**`A35-3`, `a35_shared_cross` and `a35_control_witness`.** For a product tuple the product of the
two entries is `X a c c' · X a c' c · Y b d d · Y b' d d`; the `Y` factors are the diagonal `1/4`
(act 12's fourth realizability condition), and `X a c' c = star (X a c c')` by act 34's
`a34_shared_hermitian`, so the `X` factors give `‖X a c c'‖² = 1/16` by act 34's
`a34_shared_entry_norm` (`a35_shared_cross_core`); the diagonal entry of a product tuple is `1/16`
(`a35_shared_diag_core`). Act 34's witness matrix equals the column construction at `F₄(i)` with
the column blocks `F₄(±i)` and no twist, entrywise by `ring` (`a35_shared_wit_eq`); the Fourier
factors are flat unitaries by act 23's `hadamard_z_admissible` and act 21's `vpart_unitary`
(`a35_shared_f4_flat`), which places the witness in the column hull (`a35_shared_wit_mem`); its
non-membership in the stratum is act 34's `a34_control_proper` (`a35_shared_wit_notin`); the value
`−1/256` at `(0,1,0,0,1,1)` is a direct evaluation (`a35_shared_wit_val`); and the witness is
entrywise `F₄(i) ⊗ F₄(i)` with the columns relabelled by `ρ`, the sixty-four cases over the column
block, the row within the block and the column within the block decided by `simp` and `ring`
(`a35_shared_wit_rel`), from which the feature-vector identity follows by unfolding `gram` and
`submatrix` (`a35_shared_wit_feat`); the six parts assemble into `a35_shared_wit_core`.

**`A35-4`, `A35-5`, `A35-6`, the points off the stratum.** A point of the hull is off the stratum
when one coordinate of its feature vector differs from the value every product tuple carries: at
the coordinate `((a,b),(a,b'),(a,b')), ((c,d),(c',d),(c,d))` a product tuple has the value
`1/256 · 1/16 = 1/4096` by the cross-ratio identity and the diagonal, while the twisted point `Hw`
has `−i/4096` at `(0,0,1,0,1,0)` and the second real class `Hr` has `−1/4096` at `(0,0,3,0,3,0)`,
both by direct evaluation, and act 34's `a34_shared_feature_ext` turns the feature-vector
equality into the coordinate equality (`a35_shared_twist_notin`, `a35_shared_real_notin`). The
four-row sums `i/32` and `1/32` are direct evaluations over the sixteen columns, and the entries
of `Hr` are real because each of the three factors is (`a35_shared_real_im`). The relabelled point `Pσ`: its
realizability is act 25's `relabel2_realizable` at the constant product family applied to
`F₄(i) ⊗ F₄(i)`'s tuple, itself realizable through act 21's `product_realizable` and act 12's
`sh1_necessity`; the exact isometry is act 25's `relabel2_isometry` read through act 26's
`dist_featureVec`; the stratum point is `tup 0 i ⊠ tup 0 i` by act 34's `a34_shared_tup_real`;
and `Pσ` is off the stratum by the same coordinate argument at `(0,0,1,0,1,2)`, where it takes
`−i/4096`, its cross-ratio entry `−i/256` by direct evaluation (`a35_shared_relab_core`). The
untwisted point is on the stratum by act 34's `a34_control_product` and the entrywise identity
`a35_shared_untw_eq` (`a35_shared_untw_core`).

**`A35-7`, `a35_shared_extend`, `a35_shared_modulus`, `a35_shared_infinite`.** The relabelling
by `(π₁ × π₂, τ₁ × τ₂)` of `gram (dita X Y D)` is `gram (dita X' Y' D')` entrywise with
`X' = X.submatrix π₁ τ₁`, `Y'_c = (Y (τ₁ c)).submatrix π₂ τ₂` and `D' c b = D (τ₁ c) (π₂ b)`, and a
permutation submatrix of a unitary is unitary (`a35_shared_perm_unitary`); the entrywise
conjugate is the construction at the conjugate factors, unitary because each entry of
`conj A · star (conj A)` is the conjugate of the corresponding entry of `A · star A`
(`a35_shared_conj_unitary`); the transpose is the row construction at `Xᵀ`, `(Y a)ᵀ`, `D`
(`a35_shared_ext_core`). At fixed factors, the coordinate
`((0,b),(0,0),(0,0)), ((c,0),(0,0),(c,0))` of the feature vector is a nonzero product of factor
entries times `star D[c,b]·D[0,b]·star D[0,0]·D[c,0]·|D[c,0]|²`; equal feature vectors give equal
such products, the factor entries cancel (`mul_left_cancel₀`), and the unit-modulus algebra
(`a35_shared_unit_solve`, a `linear_combination` over the eight unit relations) yields
`D' c b = u c · v b · D c b` with `u c = D' c 0 · star D c 0` and
`v b = D' 0 b · star D 0 b · D 0 0 · star D' 0 0` (`a35_shared_mod_core`). The family through
`F₄(i) ⊗ F₄(i)` is infinite: the twists `t_n = (n + i)/(n − i)` at the entry `(1,1)` are unit
(`a35_shared_zn`) and pairwise distinct (`a35_shared_zn_inj`), and equal feature vectors force,
through the modulus statement at the four entries `(0,0)`, `(0,1)`, `(1,0)`, `(1,1)`, equal twists
(`Set.infinite_of_injective_forall_mem`); a finite set of maps applied to a finite set is a finite
set, which an infinite family is not contained in (`a35_shared_inf_core`).

**`a35_c_exclusive`**: each disjunct of `P_N` contradicts the corresponding conjunct of `P_R`.

**Zero definitions.** The module carries @@NTHM@@ theorems, each followed by its `#print axioms`
line.

### The route-authorization matrix — deviations recorded

Every theorem keeps to its row: no `a35_shared_…`, `a35_c_…` other than `a35_c_exclusive`, or
`a35_control_…` consumes a verdict theorem or `a35_c_exclusive`, and `a35_c_exclusive` consumes
neither verdict theorem. The frozen matrix authorizes, beside Mathlib and this round's own shared
lemmas, the declarations and theorems listed under Provenance — the whole of act 33's and act 34's
modules among them — and it records a helper absent from that list as a deviation against the row
it departs from, not repaired. @@DEVIATIONS@@

***

## The exact-computation layer

The frozen probe `verification/lean/dita_defect_probe.py`, blob
`99f98ca79b0089d15cf9babb9ca965e88598cfa6` as amendment 1 fixes it, is added at stage 1 and wired
into the `Numerical probes` job by the one frozen token. Its run at the stage commits reports
43 `PASS` and no `FAIL` and ends with the line

```text
@@PROBELINE@@
```

These are exact arithmetic replayed, not kernel-certified: the defect strata 105, 73, 57 at the
fourth-root stratum points, 49 at the rational stratum point and at the twisted point, 17 on the
generic hull, 105 at both real classes; the two fixed-pairing hulls' tangent rank 26 against the
defect 49 at the certified rational stratum point, each of the 65 tangent and gauge vectors tested
against each of the 240 defect equations, the frozen countercontrol of the open modulus; the twenty
census points with the
preregistered defects, pairwise distinct and off the three Kronecker triples; act 34's witness
entrywise a column relabelling of `F₄ ⊗ F₄` with its invariant triple; the profile of the twisted
point and of the second real class against `F₄ ⊗ F₄`'s and Sylvester's; the matrix-induced part
of act 33's group of order 2304, image 72 and kernel 32, index 16; and the stabilizers 8192 at `F₄ ⊗ F₄` and 128 at the twisted point, counted in exact
exponent arithmetic, with their orbits 324 and 20736 under `G_ext` by breadth-first search as the
control (orbit times stabilizer is 2 654 208 at each).

**Open modulus**, recorded and not decided: whether every realizable class of the product
normalized set sufficiently near the stratum lies in some relabelled Diţă hull. Its frozen
countercontrol holds as computed: at the certified rational stratum point the defect, the dimension
of the solution space of the linearized unitarity constraints modulo phases and an upper bound on
the dimension of any family of realizable classes through the point, is 49, while the tangent span
of the two fixed-pairing hulls has rank 26, so those two tangent spaces do not exhaust the defect
space. Whether the twenty-three residual directions integrate to realizable classes, and whether
the hulls at other pairings or relabellings reach the classes near the stratum, is not measured.

***

## The `P0` cell and the guard

On `A35-DITA-STRATIFIED` this round's sentence and its standing clause are appended once after act
34's standing clause in the `P0` cell of `verification/ROADMAP.md`. The file's blob at `E` is
`243e9b973e5afe115014ffa0a807fe185727be6e`, the blob rehearsed for this case in amendment 1.

The guard is not changed by this round: at `E` it is byte for byte `D`'s, blob
`d28e9b3cf2093984a1c453892204b9932a685b2e`. The workflow at `E` is `D`'s with the one token
inserted.

***

## Checks up to `E`

- **`C1`:** the preregistration at `F` has blob `ca6c531bd28c0485f25a433ac3c344ae9cb973db` and
  amendment 1 has blob `f0ced0ab64a85c4636ad29be6b47a6e7dd408e53`, verified before the first execution commit.
- **`C2`:**
  - `controls.py` has blob `4834dd888cc87ae914c5d2a517d61d083f4daf23` at stage 1, as amendment 1 fixes it.
  - Run beside the preregistration and amendment 1, `controls.py --self-test` prints `controls: the two verdict
    propositions are duals and every shared text has one source; 8 duality mutations fail as
    required`, `controls: 3 rows hold as frozen, 74 mutation controls fail as required` and
    `controls: self-test OK`.
  - At each stage commit the module passes every one of `controls.py`'s module checks. The only
    finding is at stage 1, the corollary that stage 2 adds.
- **`C3`:** the probe has blob `99f98ca79b0089d15cf9babb9ca965e88598cfa6` at stage 1; its run is
  green at the stage commits with the line above.
- **`C6`:** at each stage commit, `tools/v3_verifier.py --receipts` holds on ten receipts and
  `tools/legacy_records_check.py` reports 303 records intact.
- **`C7`:** `git diff --no-renames --name-status D <stage 3>` lists the frozen set for
  `A35-DITA-STRATIFIED`, less this note:
  - added: the preregistration, amendment 1, `controls.py`, the module and the probe;
  - modified: `OIBridge.lean`, the census, the workflow and `ROADMAP.md`.

The guard, run locally at stage 3, reports 91 PASS and 0 FAIL in `D`'s order. That run is evidence
for the executor and not an attestation.

@@RUNS@@

`C8`, the dispatch run at `E`; `C9`, `controls.py check E`; and `C10`, the receipt commit, follow this
note.

## Discrepancies

@@DISCREPANCIES@@

@@CLAUSE@@
