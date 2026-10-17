## Fin-indexed carriers and the coordinate actions

`FiniteReachTable.lean` §6–§9 connect the recursive carriers with the carrier
proposed in #829 and prove the coordinate formulas of the table actions for
every k.

- **Carriers.** `toTup n : Carrier d n → (Fin n → Fin d)` reads the tokens of a
  recursive word (token `n` of `Carrier d (n+1)` is the last component), and
  `ofTup` builds the word of a tuple. `ofTup_toTup` and `toTup_ofTup` give
  `carrierEquiv d n : Carrier d n ≃ (Fin n → Fin d)`; `bitAt_eq_toTup` identifies
  the bits read by the gates. `pauliWord_apply` writes each Pauli word as the
  product over tokens, and `prodTab_eq_prod` does the same for product tables.
- **#829's objects.** `WK k`, `prodStateK`, `maxConeK`, `dictK`, `QK`, `cnotK`
  and `actK` are #829's definitions (preregistration lines 56–66), with the
  landed `hom`, `ehom`, `homMap`, `pauli`, `sgn`, `pc`, `pt` and `IsEffectOn`.
  `tabOf k ω = ω ∘ toTup k` and `tupOf k w = w ∘ ofTup k` are inverse
  (`tupOf_tabOf`, `tabOf_tupOf`).
- **Dictionary, products and product tests.** `dictionary_tabOf` states that the
  recursive dictionary of `tabOf k ω` is `dictK ω` reindexed by `carrierEquiv 2 k`,
  and `mem_QK_iff` follows from `Matrix.posSemidef_submatrix_equiv`.
  `tupOf_prodTab` carries the product tables of ball states to `prodStateK`, and
  `sum_prodTab_tupOf` carries every product-test pairing to the pairing in
  `maxConeK`.
- **CNOT.** `cnotM_apply` shows that `cnotM k i j` is the permutation matrix of
  the bit map `cnotPerm k i j`, which flips bit `j` by bit `i`; `toTup_cnotPerm`
  identifies it, for `i < j < k`, with `cflip` on token tuples.
  `conj_perm_apply` evaluates conjugation by a permutation matrix entrywise.
  The two-token identity `pauli_cnot_pair`,
  `σ_m(x₁,y₁) σ_n(x₂+x₁, y₂+y₁) = sgn(pc m n, pt m n) σ_{pc m n}(x₁,y₁) σ_{pt m n}(x₂,y₂)`,
  is read off the landed `dict_cnot_block` (EqvK2Generation.lean:204) at the
  unit tables `pairUnit m n`; it is not re-derived by case enumeration.
  `dictK_cflip` reindexes the dictionary sum by the involution `cnotLab` of the
  labels, splitting each product at the two tokens (`prod_two_index`).
- **One-token actions.** `localM_conj_dictionary` proves, by recursion on the
  token count and the two splittings `dictionary_succ_tok` and
  `dictionary_succ_pref`, that conjugating the dictionary by `localM k j V` is the
  recursive slot action `slotAct N k j` whenever
  `tokMat (homMap N v) = V · tokMat v · Vᴴ`; `slotAct_toTup` identifies the slot
  action with `actK`.

The compiled coordinate formulas (obligation 1, transported by obligation 2):

| Theorem | Statement |
| --- | --- |
| `tabAct_cnotM` | `tabAct k (cnotM k i j) (tabOf k ω) = tabOf k (cnotK ⟨i,_⟩ ⟨j,_⟩ ω)` for `i < j < k` |
| `tabAct_cnotM_eq` | `tabAct k (cnotM k i j) w = tabOf k (cnotK ⟨i,_⟩ ⟨j,_⟩ (tupOf k w))` for every recursive table `w` |
| `tabAct_localM` | `tabAct k (localM k j V) (tabOf k ω) = tabOf k (actK ⟨j,_⟩ N ω)` for `j < k`, given the one-token intertwining |
| `tabAct_localM_eq` | the same for every recursive table `w` |

They are used with the landed `tokMat_rot t` (N = `rotLin t`, V = the phase
flow) and `tokMat_cyc` (N = `cycEquiv`, V = `cycMat`).

## The statement surface proposed in #829

`FiniteReachTable.lean` §10 first separates the table theorem into its two
inclusions on the recursive carrier
(`tableCone_subset_psd_of_maxCone_drive`, which uses neither products nor cone
closure, and `psd_subset_tableCone_of_products_cone_drive`, which does not use
the product bound), then transports a set `K : Set (WK k)` to its recursive
tables `tabSet k K` (`tabSet_products`, `tabSet_add`, `tabSet_smul`,
`tabSet_maxCone`, `tabSet_cnot`, `tabSet_local`). Each transport carries one
hypothesis of #829 to the corresponding table hypothesis; none is absorbed into
a definition, and every theorem below lists its hypotheses explicitly.

With H1, H2 and A written out as in the preregistration (lines 67–69):

- `subset_QK_of_maxCone_drive (hmax : K ⊆ maxConeK (eball 3)) (hH2) (hA) : K ⊆ QK k`.
- `QK_subset_of_products_cone_drive (hH1) (hadd) (hsmul) (hH2) (hA) : QK k ⊆ K`.
- `kCone_eq_QK_of_drive_maxCone (hH1) (hadd) (hsmul) (hmax) (hH2) (hA) : K = QK k`,
  the antisymmetry of the two inclusions.
- `driveInvariantK_of_eq_QK (h : K = QK k) : H2 ∧ A`, by positive semidefinite
  conjugation through `tabAct_cnotK`, `tabAct_localK` and `tabAct_psd`.
- `kCone_eq_QK_iff_drive_maxCone (hH1) (hadd) (hsmul) (hmax) : K = QK k ↔ H2 ∧ A`,
  with `driveInvariantK_of_eq_QK` as the forward witness and
  `kCone_eq_QK_of_drive_maxCone` as the reverse witness (AGENTS §A.34).

The declarations live in the research namespace `FiniteReconstructionDesign`,
not in the proposed `OIBridge/KTokenMaxCone.lean`, and refer to the landed
objects by their full names (`OIBridge.TransitiveBody.eball`,
`OIBridge.KInfFoundations.rotLin`, `OIBridge.KInfFoundations.cycEquiv`). The
hypotheses and conclusions are #829's; the module text is not #829's S1
surface, and no control of #829 (S1–S4, P, W, V, I, C, R, G) has been run on it.

## The k = 2 recovery

`pairCarrierEquiv : W 3 ≃ₗ[ℝ] WK 2` sends `ω` to `μ ↦ ω (μ 0) (μ 1)`. The five
transports of argument section 5 are:

| Object | Theorem |
| --- | --- |
| products | `pairCarrierEquiv_prodState : pairCarrierEquiv (prodState (x 0) (x 1)) = prodStateK x` |
| product tests | `pairCarrierEquiv_maxCone` (maxCone → maxConeK) and `maxCone_of_pairCarrierEquiv` (maxConeK → maxCone), both through `sum_pairCarrier_eq` |
| dictionary | `mem_Q3_iff_pairCarrier : ω ∈ Q3 ↔ pairCarrierEquiv ω ∈ QK 2`, from `dictK_pairCarrier` |
| gate | `pairCarrierEquiv_cnot : pairCarrierEquiv (cnot ω) = cnotK 0 1 (pairCarrierEquiv ω)` |
| target actions | `pairCarrierEquiv_actT : pairCarrierEquiv (actT N ω) = actK 1 N (pairCarrierEquiv ω)` |

`pairCone_eq_Q3_of_kToken` has the hypotheses and conclusion of the landed
`pairCone_eq_Q3_of_drive_maxCone` (EqvK2MaxCone.lean:153–160 at D) and is proved
by applying `kCone_eq_QK_of_drive_maxCone` at `k = 2` to the transported set
`pairSet K`. At `k = 2` the guard `i < j` leaves only `CNOT(0 → 1)` and the guard
`j ≠ 0` only token 1 (`fin2_lt`, `fin2_ne_zero`).

The proof does not use the landed two-token theorem or anything proved from it.
`OIBridge.EqvK2MaxCone` is not in the import closure of the design modules
(FinitePauli imports `OIBridge.EqvK2Schema`, FiniteReach imports
`OIBridge.EqvK2Generation`, and neither imports it), so no declaration of that
module is in the environment. The module checks this when it is compiled: an
`#eval` after the recovery fails the build if
`OIBridge.EqvK2MaxCone.pairCone_eq_Q3_of_drive_maxCone` is in the environment,
and otherwise logs that it is not. A theorem proved from it would have to be in
the same environment, so none is used either.
