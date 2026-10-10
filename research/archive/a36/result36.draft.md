# Track B act 36 — the Diţă factorization hierarchy at the product-embedded stratum: RESULT

Run under `AGENTS.md` §A.39 as a native round, in one pull request, #757. This note is part of `E`,
so it records what was measured up to `E`. The attestations for `F` and `E`, the reconciliation, the
verdict on the receipt commit and the gate's check of this round's own receipt are recorded in the
receipt, `verification/receipts/A36.json`, and on the pull request.

- **`D`** — `8b33e25fcb7e5b464cbfc605f61f7d40e5825784`, the head of `main` after the documentation
  landing of #756, itself after act 35's landing.
- **`F`** — `1f86b690352248789b95d79606cda52a43a70465`, the child of `D` that adds the
  preregistration alone, blob `e6c17bd04bf52c96657efc25b788107ed5af8543`. `F`'s `check-run`
  attestation is run 36335286607; the owner's designation is comment 5857996731 on #757.
- **Shape** — non-sealing: no seal record, guard clause, manifest record or certificate.

**Outcome:** `A36-HIERARCHY`

| target | outcome at `E` | predicted |
| --- | --- | --- |
| `A36` | `A36-HIERARCHY`, theorem `a36_hierarchy` | the same, very high |

The verdict theorem has the frozen statement `P_R` verbatim, compared after collapsing whitespace,
and so do the corollary `a36_c_exclusive` and the seven statements required under this label:
- `A36-1`: `a36_shared_hull_g` and `a36_shared_hull_gt`;
- the `A36-1` instances: `a36_control_hull28` and `a36_control_hull82`;
- `A36-2`: `a36_shared_line`;
- `A36-3`: `a36_shared_point`;
- the control `a36_control_stratum`.

***

## The frozen post-round sentence

> @@SENTENCE@@

***

## What was proved, and how

The proofs follow the freeze's route. Throughout, `dg X Y D` is Diţă's column construction over
any index types `α`, `β`, `(a,b),(c,d) ↦ X[a,c]·D[c,b]·Y_c[b,d]`, `dgT X Y E` the row construction
`(a,b),(c,d) ↦ X[a,c]·E[a,d]·Y_a[b,d]`, `flg X` flatness of a unitary on a finite type with every
entry of squared modulus one over the cardinality, `gram H` the tuple `i ↦ (j,k) ↦ star (H i j) · H i k`
of a flat unitary `H` of the product carrier, `r28`, `c28`, `r82`, `c82` the frozen index maps,
`Pu u = SIG ∘ u^W` the family, `P = Pu u₆₀` the named point, `S` act 34's stratum and `N` the
product normalized set.

**`A36-1`, `a36_shared_hull_g`, `a36_shared_hull_gt`.** The column construction over any finite
index types is unitary by act 35's block computation at general types: a row-times-row entry of
`H · star H` splits through `Fintype.sum_prod_type` into
`∑_c X[a,c]·star X[a',c]·D[c,b]·star D[c,b']·(Y_c · star Y_c)[b,b']`, the inner factor is
`δ_{bb'}` by the unitarity of `Y_c`, then `|D[c,b]|² = 1` and the outer sum is `δ_{aa'}` by the
unitarity of `X` (`a36_shared_dg_unitary`). Reindexing a unitary matrix by two bijections keeps it
unitary, the row sum being transported along the column bijection by
`Function.Bijective.sum_comp` and the Kronecker delta along the row bijection by its injectivity
(`a36_shared_reindex_unitary`). The bijections `eR`, `eC` of `α × β` with the product carrier give
`card α · card β = 16` (`Fintype.card_congr`, `Fintype.card_prod`), so every entry has squared
modulus `1/(card α · card β) = 1/16` (`a36_shared_dg_norm_sq`) and modulus `1/4`
(`a36_shared_sq_quarter`); act 35's `a35_shared_gram_realizable` then makes the tuple realizable
(`a36_shared_hullg_core`). The row construction is the transpose of the column construction at
`Xᵀ`, `(Y a)ᵀ` (`a36_shared_dgT_eq`), so its unitarity is act 25's `transpose_unitary` applied to
the former (`a36_shared_dgT_unitary`), with the same norm and realizability steps
(`a36_shared_dgT_norm_sq`, `a36_shared_hullgt_core`).

**The `A36-1` instances, `a36_control_hull28`, `a36_control_hull82`.** Each is `A36-1` at explicit
equivalences: for the `2 × 8` instance, `Fin 4 × Fin 4 ≃ Fin 2 × Fin 8` built from
`finProdFinEquiv.symm` on the first factor, the product associator, and `finProdFinEquiv` on the
second, with the product commutator on the column side, whose inverse is definitionally `r28`,
respectively `c28`; for the `8 × 2` instance likewise with `r82 = c82` (`a36_shared_hull28_core`,
`a36_shared_hull82_core`).

**`A36-2`, `a36_shared_line`.** The witnesses are those of the nested form: the outer factor
`X = ((1 + i)/2) · [[1, 1], [1, −1]]`, a flat unitary on `Fin 2` (`a36_shared_xo_flat`); the inner
factors `Y_c` on `Fin 8`, each the reindexing along `finProdFinEquiv.symm` of the row construction
over `Fin 2 × Fin 4` with the outer factor `((1 − i)/2) · [[1, 1], [1, −1]]`
(`a36_shared_xi_flat`), the twist `E_c[a_lo, d] = u^{[d = 1]}` when `c = 0` and `a_lo = 0` and `1`
otherwise, and the inner factors `Z_{c,a_lo} = s · p_b · F₄(w)` with the unit scalar
`s = z^{[c = 1][a_lo = 1]}` and the unit row phases `p_b = u^{[c = 0][a_lo = 0][b = 1]}`, flat
unitaries because a unit scalar and unit row phases preserve unitarity (`a36_shared_phase_unitary`,
`a36_shared_zp_flat`), so that each `Y_c` is a flat unitary on `Fin 8` by the row construction's
unitarity and the reindexing lemma (`a36_shared_y8_flat`); and the twist `D ≡ 1`. The identity
`Pu u = dita28 X Y D` holds entrywise: after the outer indices `a`, `c` are split into their
sixteen cases and the frozen index maps evaluated (`a36_shared_div`, `a36_shared_mod`, by
`decide`), each entry is a polynomial identity in `z`, `w`, `u`, `i` and the Fourier entries, closed
by `ring` after `i² = −1` (`a36_shared_nested_eq`); the scalar product `((1 + i)/2)·((1 − i)/2)·(1/2)`
is `1/4`. Realizability and membership in `N` are the `2 × 8` instance at these witnesses
(`a36_shared_line_core`).

**`A36-3`, `a36_shared_point`.** `star u₆₀ · u₆₀ = 1` by `3599² + 120² = 3601²`
(`a36_shared_u60_unit`); realizability and membership in `N` are `A36-2` at `u₆₀`; the
cross-ratio value `u₆₀/256` is a direct evaluation of the four entries, each `1/4` times a power of
`u₆₀` with the exponents `0, 0, 1, 0` (`a36_shared_p_val`); and `P` is off the stratum because on
every stratum point the closed-walk coordinate at `(((0,0),(0,1),(0,1)), ((0,0),(1,0),(0,0)))` is
`1/4096` by act 35's `a35_shared_cross_core` and `a35_shared_diag_core`, while on `P` it is
`u₆₀/4096`, and equal feature vectors have equal coordinates by act 34's `a34_shared_feature_ext`
(`a36_shared_p_notin`, `a36_shared_point_core`).

**The control, `a36_control_stratum`.** `Pu 1 = SIG` by `one_pow`; `featureVec (gram SIG) ∈ S`
with the fibre-Gram tuples of the Fourier dilations at `z` and at `w`, realizable by act 23's
`hadamard_z_admissible` with act 12's `sh1_necessity`, whose product tuple is `gram SIG` entrywise
by `fibreGram_apply` (`a36_shared_one_core`).

**`a36_hierarchy`** is the conjunction of the four cores over the frozen head; **`a36_c_exclusive`**:
each disjunct of `P_N` contradicts the corresponding conjunct of `P_R`.

**Zero definitions.** The module carries @@NTHM@@ theorems, each followed by its `#print axioms`
line.

### The route-authorization matrix — deviations recorded

Every theorem keeps to its row: no `a36_shared_…`, `a36_c_…` other than `a36_c_exclusive`, or
`a36_control_…` consumes a verdict theorem or `a36_c_exclusive`, and `a36_c_exclusive` consumes
neither verdict theorem. The frozen matrix authorizes, beside Mathlib and this round's own shared
lemmas, the declarations and theorems listed under Provenance — the whole of act 33's, act 34's
and act 35's modules among them — and it records a helper absent from that list as a deviation
against the row it departs from, not repaired. @@DEVIATIONS@@

***

## The exact-computation layer

The frozen probe `verification/lean/dita_hierarchy_probe.py`, blob
`b3d144988a9678deac69a738b6459f32230371b0`, is added at stage 1 and wired into the
`Numerical probes` job by the one frozen token. Its run at the stage commits reports 57 `PASS` and
no `FAIL` and ends with the line

```text
@@PROBELINE@@
```

These are exact arithmetic replayed, not kernel-certified: the defect 49 at the certified rational
stratum point and 37 at the named point `P` and at the second point `Pu u₅`, `u₅ = (3+4i)/5`, of the
frozen line; `W` an exact straight line in `ker DF`, with a one-entry perturbation failing the test;
the family at `u = 1` equal to `SIG` entrywise; the exhaustive block-structure searches, which find
at `P` and at `Pu u₅` no `4 × 4` and no `8 × 2` Diţă factorization of either orientation and
exactly one `2 × 8` factorization of each orientation, at the frozen blocks and row classes, while
finding at `SIG = Pu 1` its four `4 × 4`, two `8 × 2` and three `2 × 8` factorizations per form;
the first-order census `80 / 31 / 14, 14, 26 / 23 / 64`; the 492 `4 × 4` Diţă hulls through `SIG`,
each of tangent dimension 14 with `D²F` vanishing exactly, spanning the 49-dimensional defect; the
stabilizer of order 1024 with 112 classes and the residual sectors `8 + 8 + 4 + 2 + 1`; the
second-order form of rank 47; the two 8-dimensional sectors obstructed at three seeded generic
directions each by the exact certificate `B(v, v) ∉ span{B(v, T), B(T, T)}`, which fails at all 8 of 8
structured basis vectors of each; and the 4-, 2- and 1-dimensional sectors extended at three
seeded directions each by an explicit row-hull correction.

By the probe, and not by the kernel: **the `4 × 4` Diţă hierarchy is locally insufficient at the
certified stratum point** — a continuous `2 × 8` Diţă deformation passes through the product point
and, at its named point and at a second point, lies in no `4 × 4` hull — and the first escaping
family belongs to the `2 × 8` construction.

**Open**, recorded and not decided: whether every realizable class of the product normalized set
sufficiently near the stratum lies in some Diţă hull of some factorization of the sixteen-point
carrier. Act 35's open modulus is answered in the negative for the `4 × 4` hulls by the named point
and re-posed at this level; nothing here says the hierarchy exhausts anything.

***

## The `P0` cell and the guard

On `A36-HIERARCHY` this round's sentence and its standing clause are appended once after act 35's
standing clause in the `P0` cell of `verification/ROADMAP.md`. The file's blob at `E` is
`a02be0964a982abe2b9fd5082e2844927d3ab690`, the blob rehearsed for this case in the
preregistration.

The guard is not changed by this round: at `E` it is byte for byte `D`'s, blob
`d28e9b3cf2093984a1c453892204b9932a685b2e`. The workflow at `E` is `D`'s with the one token
inserted.

***

## Checks up to `E`

- **`C1`:** the preregistration at `F` has blob `e6c17bd04bf52c96657efc25b788107ed5af8543`,
  verified before the first execution commit.
- **`C2`:**
  - `controls.py` has blob `292faff95a9e082b4fae8fb193db34ef7745d665` at stage 1, as frozen.
  - Run beside the preregistration, `controls.py --self-test` prints `controls: the two verdict
    propositions are duals and every shared text has one source; 8 duality mutations fail as
    required`, `controls: 3 rows hold as frozen, 62 mutation controls fail as required` and
    `controls: self-test OK`.
  - At each stage commit the module passes every one of `controls.py`'s module checks. The only
    finding is at stage 1, the corollary that stage 2 adds.
- **`C3`:** the probe has blob `b3d144988a9678deac69a738b6459f32230371b0` at stage 1; its run is
  green at the stage commits with the line above.
- **`C6`:** at each stage commit, `tools/v3_verifier.py --receipts` holds on eleven receipts and
  `tools/legacy_records_check.py` reports 303 records intact.
- **`C7`:** `git diff --no-renames --name-status D <stage 3>` lists the frozen set for
  `A36-HIERARCHY`, less this note:
  - added: the preregistration, `controls.py`, the module and the probe;
  - modified: `OIBridge.lean`, the census, the workflow and `ROADMAP.md`.

The guard, run locally at stage 3, reports 91 PASS and 0 FAIL in `D`'s order. That run is evidence
for the executor and not an attestation.

@@RUNS@@

`C8`, the dispatch run at `E`; `C9`, `controls.py check E`; and `C10`, the receipt commit, follow this
note.

## Discrepancies

@@DISCREPANCIES@@

@@CLAUSE@@
