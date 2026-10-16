# Finite algebra and reachability design

This record accompanies the five research Lean modules in this directory.
They are design sources outside the adopted `OIBridge` population. They change
neither the mathematical hypotheses of the written cone theorem nor a native
round's control plane. No F is designated. This directory is on a research
branch and is not on main; until it lands there, its files and the runs below
are working evidence, not authoritative references. Every file this record
relies on is in this directory or adopted on main, and each reference that is
not is marked as off main.

Compilation status: all five modules compile against the adopted library at D
`dee3b5ae6fd3fb20fa1bad3337963e5af947f3a4`, which is on main; the design branch
leaves `verification/lean-mathlib` unchanged from D. The exact design head is
`924dc9184c47e69f03beef0828f57edac668f3d7`; GitHub Actions
[run 38885086040](https://github.com/amaybaum/incompleteness/actions/runs/38885086040),
job `116920768112`, is all green (GitHub Actions runs are host records outside the
repository). The run checks this directory's `SHA256SUMS` before it compiles,
so the compiled bytes are those listed. The source hashes are:

| Module | SHA256 |
| --- | --- |
| `FinitePauli.lean` | `4af38e2e151390edf8ca23cdec94be06b7b4b1f9c72c57292a5374b7ca195b8e` |
| `FiniteWalsh.lean` | `d4815ec809fa37fefabe786886efb860f1da02788cea4f7e048e34726da8a5f0` |
| `FiniteCircuit.lean` | `70ce411d9cd830b8d73a5eee3e1eed758da4633802b9734961a6a0021ecc9763` |
| `FiniteReach.lean` | `5112671f1317d60e23b2fcb4a20953f38771e9c1f2f03b2c553f1360947985b4` |
| `FiniteReachTable.lean` | `a71fcb33477cfce4200643f967c2fd4382dc942749fe304b08135748af294f08` |

The modules contain 236 theorems: 14 Pauli/tensor/dictionary theorems, six
Walsh theorems, three circuit theorems, 77 gate, word, multiplexor,
reachability and matrix-cone theorems, and 136 table, carrier, coordinate-action
and transport theorems. All 74 requested main axiom reports (8, 3, 3, 13 and 47
in module order) list only `propext`, `Classical.choice` and `Quot.sound`. The
successful log contains no `sorryAx` and no errors, and it contains the line
`OIBridge.EqvK2MaxCone.pairCone_eq_Q3_of_drive_maxCone is not in the
environment` (see the k = 2 recovery below). No `sorry`, additional axiom or
admitted synthesis hypothesis appears in these sources.

That same run replays the 242 finite controls and five mutations, the historical
descent probe and the independent descent controls, checks the saved hashes,
and compiles the historical KN-DESC design. The descent probe, its independent
controls and the KN-DESC design source are in the sibling research directory
`carrier-descent-design`, which is off main. The run also passes the 303-record
legacy check, all 46 receipts and artifact placement. This is research design
evidence; it is not an F attestation or a native execution. Documentation added
after this exact head reports its build and does not change these source bytes.

The build uses this branch's design workflow,
`.github/workflows/finite-reconstruction-design.yml` (off main), changed here to
build `OIBridge.EqvK2Generation` and to compile `FiniteReach.lean` and
`FiniteReachTable.lean`; its commands for the earlier modules are unchanged.
The owner approved that change on 2026-10-16 as a one-time exception to the
rule against workflow changes in this research track, because Lean cannot be
compiled in the research session. A further workflow change needs separate
approval, and this design workflow is not incorporated into a native
certification pull request without review. Neither `verify.yml` nor any
adopted module is changed. Every declaration listed below is in one of the
five modules the workflow already compiles.

Earlier development builds rejected type transparency, finite-sum ordering,
delta-case simplification and division-normalization steps in the proof sources,
an equality-instance mismatch in the reachability module, described below, and
an unclosed zero-product goal in the unit-table CNOT lemma. Those failed builds
supplied no certification. The corrections retain the mathematical statements
and the all-k argument's stated hypotheses.

## Pauli coordinates and spectators

`FinitePauli.lean` imports the adopted `EqvK2Schema` and uses its one-token
Pauli matrices and entrywise completeness theorem. Its recursive carriers are
`Bits 0 = Fin 1`, `Bits (n+1) = Bits n × Fin 2` and, correspondingly, Pauli
labels with `Fin 4`. This retains the scalar empty tensor and avoids an
enumeration or fixed-dimensional case split for n.

The generic tensor lemmas establish multiplication, trace, conjugate transpose
and conjugation intertwining for arbitrary finite spectator carriers. The
recursive Pauli proofs establish Hermiticity, trace orthogonality and entrywise
completeness for every n. Completeness and orthogonality give separately named
dictionary inverse directions:

- `coordinates_dictionary_real` reads every real table back after mapping it
  into Hermitian matrices.
- `dictionary_coordinates_real` reconstructs every Hermitian matrix from its
  real Pauli coordinates.

The complex-coordinate versions prove the full matrix expansion before the
Hermitian restriction. These are mathematical carrier identities. Identifying
this carrier with the framework's physical n-token states remains a premise.
The reindexing to `Fin n → Fin 2` and `Fin n → Fin 4`, and the five transports
to the existing two-token carrier, are proved in `FiniteReachTable.lean`
(sections below).

## Walsh inversion and finite circuit algebra

`FiniteWalsh.lean` uses the recursive binary carrier. The base Hadamard matrix
is `[[1,1],[1,-1]]`; tensor recursion proves exact row orthogonality for every
number of controls. `walsh_permuted_orthogonal` accepts any bijective column
ordering. `multiplexorAngles_recover` proves the prescribed real branch angles
are recovered from the finite inverse Walsh transform. No density, closure,
rational-angle restriction or asymptotic approximation occurs.

A Gray ordering is only one permissible permutation in that theorem. It is
not assumed to be an already synthesized circuit. `FiniteCircuit.lean` proves
the separate group identity for a chronological list of rotation-then-flip
steps: a one-parameter rotation law, an involutive flip and the exact crossing
law give a normal form with accumulated signed angle and flip parity. A closed
parity word is exactly its accumulated rotation. These hypotheses are explicit
algebraic laws, rather than a physical compatibility postulate. The cone
theorems below do not use these two modules.

## Gates, words and exact multiplexors

`FiniteReach.lean` imports `FinitePauli` and the adopted `EqvK2Generation`.
`cnotM k i j` and `localM k j V` are defined by recursion on the token count: a
gate on the last token is a block-diagonal family over the earlier tokens
(`blockFam`), and a gate on an earlier token is tensored with the identity on
the last. `IsWord k` is the closure under products of unit scalars, `cnotM k i j`
with `i < j < k`, and the third-axis flow `phaseMat (cos t) (sin t)` and the
cyclic matrix `cycMat` at each token `j` with `0 < j < k`. Unit scalars
conjugate every matrix to itself (`pres_scalar`), so every word preserves any
set that the named generators preserve (`pres_of_isWord`). They are needed
because `phaseMat` has determinant `cis t`: a unit scalar times the flow gives
each diagonal special unitary on a token (`isWord_local_dUnit`). The conjugate
transpose of a word is a word (`isWord_conjTranspose`), which supplies the
inverse-word step of argument section 2.

The multiplexor of argument section 3 is proved without the Gray schedule.
`sign_induction` shows that a predicate on real functions of n bits holds for
every function when it is closed under addition, holds for constants and is
stable under multiplication by the sign of each bit; zero controls are the
constant case. For families of diagonal rotations, addition is block
multiplication, a constant is the local flow on the target, and multiplication
by the sign of bit `i` is conjugation by `cnotM (n+1) i n` (`flipX_rz`). Hence
`isWord_rzFam`: every family of diagonal rotations on a target other than the
first token, controlled by all earlier tokens, is a word. Real rotation
families are the cyclic conjugates of diagonal families on the target
(`rotRe_eq`, `isWord_rotReFam`). `isWord_suFam` applies the adopted exact
Euler factorization `su_euler` branchwise and composes the three multiplexors in
the factor order. Spectators are qubit tokens: `isWord_lift` adds a later token
with the identity. Arbitrary finite spectator carriers are not needed for the
cone theorem and are not treated in this module.

`FinitePauli` declares its carrier equality instance classically. An instance
synthesized at an explicit successor carrier `Bits (n+1)` is the product
instance, and at `Bits 0` the `Fin 1` instance; neither is definitionally equal
to the classical one, so an identity matrix written at such a carrier does not
unify with one elaborated generically. `FiniteReach` declares the structural
instance `bitsDecEq` at high priority, and the two added modules elaborate
their matrices with it.

## Reachability and the matrix-form cone theorem

`reach_prod` proves that every vector x on k + 1 tokens is `U` applied to
`a ⊗ |0⟩ ⊗ … ⊗ |0⟩` for a word `U` and a first-token vector `a`. Each step
applies the multiplexor of the inverse blocks `(suTo v_b)†` of argument section
4 to the lifted word for the vector of block norms; a zero block uses the
identity, which is the adopted value of `suTo` at zero. The first token is never
driven. `reach_norm` rescales to unit one-token vectors with a nonnegative
factor, and uses a unit-scalar word for the scalar empty tensor at k = 0.

For a set C of k-token matrices, with preservation by the named generators
written `drive`:

- `subset_psd_of_maxCone_drive`: Hermitian members, nonnegative expectation on
  every product vector and `drive` give C ⊆ PSD. Products in C and cone
  closure are not hypotheses.
- `psd_subset_of_products_cone_drive`: every product of trace-one PSD one-token
  matrices in C, closure under addition and nonnegative real scaling, and
  `drive` give PSD ⊆ C. The product-test bound is not a hypothesis. A PSD
  matrix is a finite sum of rank-one terms by the adopted
  `psdFactorization_discharged`.
- `kCone_eq_psd_of_drive_maxCone` combines the two inclusions.
- `driveInvariant_of_eq_psd`: C = PSD gives `drive`, by PSD conjugation.
- `kCone_eq_psd_iff_drive_maxCone`: under the Hermitian, product, cone and
  product-test hypotheses, C = PSD if and only if `drive`, with
  `driveInvariant_of_eq_psd` and `kCone_eq_psd_of_drive_maxCone` as the two
  directional witnesses.

## Table form

`FiniteReachTable.lean` §1–§5 carry these statements to real Pauli tables on
the recursive label carrier. `dictionary_prodTab` identifies the dictionary
image of a product table with the product of one-token matrices, and
`trace_dictionary_mul` gives the trace pairing of two dictionary images as their
table pairing divided by `2^n`. `blochH u` is the homogeneous Bloch vector of a
one-token vector; `tokMat_blochH` identifies its matrix with `u u†`, and
`lor_blochH` places it in the forward cone. `quad_dictionary_prodVec` writes the
expectation on a product vector as a forward-cone product pairing. The generator
actions on tables are conjugation through the dictionary,
`tabAct k U w = coordinates k (U · dictionary k w · U†)`.

- `tableCone_eq_psd_of_drive_maxCone`: a set K of tables that contains the
  product tables of ball states, is closed under addition and nonnegative
  scaling, is nonnegative on every product of forward-cone vectors and is
  carried into itself by the actions of the named generators is the set of
  tables with PSD dictionary image. Its lower inclusion uses only pure products
  (`psd_subset_of_pure_cone_drive`).
- `maxConeTab k` is the set of tables nonnegative on every product of effects
  of the ball. `lorPair_nonneg_of_maxConeTab` scales each forward-cone vector to
  an effect (`isEffectOn_lorScale`, through the adopted `affOf`), so the effect
  form of the bound implies the forward-cone form. The table theorem uses this
  direction only; the converse is the product-vector section below.
- `tableCone_eq_psd_of_drive_maxConeTab` is the table theorem with
  `K ⊆ maxConeTab k`.
- `tableDrive_of_eq_psd` gives the actions from equality, and
  `tableCone_eq_psd_iff_drive_maxConeTab` states the equivalence with these two
  directional witnesses.

## Fin-indexed carriers and the coordinate actions

`FiniteReachTable.lean` §6–§9 connect the recursive carriers with the carrier
proposed in #829 and prove the coordinate formulas of the table actions for
every k. #829 is an open pull request; its preregistration
`verification/programmes/oi-qm/reconstruction/round-ktoken-maxcone-1/preregistration.md`
at `625f853ff70546f6e8d56d22fad15e968ad48354` (SHA256
`739dc162215771cf7bfe50b716825984df3408ec8013e6a9dcd4f90dc705cb5d`) is off main.
Its definitions are restated in the module below, so the compiled statements do
not depend on that file.

- **Carriers.** `toTup n : Carrier d n → (Fin n → Fin d)` reads the tokens of a
  recursive word (token `n` of `Carrier d (n+1)` is the last component), and
  `ofTup` builds the word of a tuple. The two inverse laws `ofTup_toTup` and
  `toTup_ofTup` give `carrierEquiv d n : Carrier d n ≃ (Fin n → Fin d)`
  (FiniteReachTable.lean:471); `bitAt_eq_toTup` identifies the bits read by the
  gates. `pauliWord_apply` writes each Pauli word as the product over tokens,
  and `prodTab_eq_prod` does the same for product tables.
- **The proposed objects.** `WK k`, `prodStateK`, `maxConeK`, `dictK`, `QK`,
  `cnotK` and `actK` (lines 522–550) are the definitions of the preregistration's
  statement surface (its lines 56–66), with the adopted `hom`, `ehom`, `homMap`,
  `pauli`, `sgn`, `pc`, `pt` and `IsEffectOn`. `tabOf k ω = ω ∘ toTup k` and
  `tupOf k w = w ∘ ofTup k` are inverse (`tupOf_tabOf`, `tabOf_tupOf`).
- **Dictionary, products and product tests.** `dictionary_tabOf` (line 581)
  states that the recursive dictionary of `tabOf k ω` is `dictK ω` reindexed by
  `carrierEquiv 2 k`. `mem_QK_iff` (line 586) is the iff
  `ω ∈ QK k ↔ (dictionary k (tabOf k ω)).PosSemidef`; both directions come from
  Mathlib's `Matrix.posSemidef_submatrix_equiv` applied to that reindexing.
  `tupOf_prodTab` carries the product tables of ball states to `prodStateK`, and
  `sum_prodTab_tupOf` carries every product-test pairing to the pairing in
  `maxConeK`.
- **CNOT.** `cnotM_apply` (line 638) shows that `cnotM k i j` is the permutation
  matrix of the bit map `cnotPerm k i j`, which flips bit `j` by bit `i`;
  `toTup_cnotPerm` identifies it, for `i < j < k`, with `cflip` on token tuples.
  `conj_perm_apply` evaluates conjugation by a permutation matrix entrywise.
  The two-token identity `pauli_cnot_pair` (line 841),
  `σ_m(x₁,y₁) σ_n(x₂+x₁, y₂+y₁) = sgn(pc m n, pt m n) σ_{pc m n}(x₁,y₁) σ_{pt m n}(x₂,y₂)`,
  is read off the adopted `dict_cnot_block` (EqvK2Generation.lean:204) at the
  unit tables `pairUnit m n`; it is not re-derived by case enumeration.
  `dictK_cflip` reindexes the dictionary sum by the involution `cnotLab` of the
  labels, splitting each product at the two tokens (`prod_two_index`).
- **One-token actions.** `localM_conj_dictionary` (line 946) proves, by
  recursion on the token count and the two splittings `dictionary_succ_tok` and
  `dictionary_succ_pref`, that conjugating the dictionary by `localM k j V` is
  the recursive slot action `slotAct N k j` whenever
  `tokMat (homMap N v) = V · tokMat v · Vᴴ`; `slotAct_toTup` identifies the slot
  action with `actK`.

The compiled coordinate formulas:

| Theorem | Statement |
| --- | --- |
| `tabAct_cnotM` (line 873) | `tabAct k (cnotM k i j) (tabOf k ω) = tabOf k (cnotK ⟨i,_⟩ ⟨j,_⟩ ω)` for `i < j < k` |
| `tabAct_cnotM_eq` (line 886) | `tabAct k (cnotM k i j) w = tabOf k (cnotK ⟨i,_⟩ ⟨j,_⟩ (tupOf k w))` for every recursive table `w` |
| `tabAct_localM` (line 984) | `tabAct k (localM k j V) (tabOf k ω) = tabOf k (actK ⟨j,_⟩ N ω)` for `j < k`, given the one-token intertwining |
| `tabAct_localM_eq` (line 993) | the same for every recursive table `w` |

They are used with the adopted `tokMat_rot t` (N = `rotLin t`, V = the phase
flow) and `tokMat_cyc` (N = `cycEquiv`, V = `cycMat`); `tabAct_cnotK` and
`tabAct_localK` state the same identities with `Fin k` token indices.
`tabAct_localK` keeps the intertwining hypothesis. Its instances for `rotLin t`
and `cycEquiv` are the named corollaries `tabAct_rotK` (line 1006) and
`tabAct_cycK` (line 1012); inside `tabSet_local` and `driveInvariantK_of_eq_QK`
the same instances are discharged inline.

## The statement surface proposed in #829

`FiniteReachTable.lean` §10 first separates the table theorem into its two
inclusions on the recursive carrier
(`tableCone_subset_psd_of_maxCone_drive`, line 1081, which uses neither products
nor cone closure, and `psd_subset_tableCone_of_products_cone_drive`, line 1097,
which does not use the product bound), then transports a set `K : Set (WK k)`
to its recursive tables `tabSet k K` (`tabSet_products`, `tabSet_add`,
`tabSet_smul`, `tabSet_maxCone`, `tabSet_cnot`, `tabSet_local`). Each transport
carries one hypothesis to the corresponding table hypothesis; none is absorbed
into a definition, and every theorem below lists its hypotheses explicitly.

With H1, H2 and A written out as in the preregistration's lines 67–69:

- `subset_QK_of_maxCone_drive (hmax : K ⊆ maxConeK (eball 3)) (hH2) (hA) : K ⊆ QK k`
  (line 1168).
- `QK_subset_of_products_cone_drive (hH1) (hadd) (hsmul) (hH2) (hA) : QK k ⊆ K`
  (line 1181).
- `kCone_eq_QK_of_drive_maxCone (hH1) (hadd) (hsmul) (hmax) (hH2) (hA) : K = QK k`
  (line 1198), the antisymmetry of the two inclusions.
- `driveInvariantK_of_eq_QK (h : K = QK k) : H2 ∧ A` (line 1214), by positive
  semidefinite conjugation through `tabAct_cnotK`, `tabAct_localK` and
  `tabAct_psd`.
- `kCone_eq_QK_iff_drive_maxCone (hH1) (hadd) (hsmul) (hmax) : K = QK k ↔ H2 ∧ A`
  (line 1234), with `driveInvariantK_of_eq_QK` as the forward witness and
  `kCone_eq_QK_of_drive_maxCone` as the reverse witness.

The declarations live in the research namespace `FiniteReconstructionDesign`,
not in the proposed `OIBridge/KTokenMaxCone.lean`, and refer to the adopted
objects by their full names (`OIBridge.TransitiveBody.eball`,
`OIBridge.KInfFoundations.rotLin`, `OIBridge.KInfFoundations.cycEquiv`). The
hypotheses and conclusions are the preregistration's. Its proposed module
imports `OIBridge.EqvK2MaxCone`; this module does not. The module text is not
the preregistration's S1 surface, and none of its controls (S1–S4 and the
probe of its Q-EXACT question) has been run on it.

## The k = 2 recovery

`pairCarrierEquiv : W 3 ≃ₗ[ℝ] WK 2` (line 1249) sends `ω` to
`μ ↦ ω (μ 0) (μ 1)`. The five transports of argument section 5 are:

| Object | Theorem |
| --- | --- |
| products | `pairCarrierEquiv_prodState : pairCarrierEquiv (prodState (x 0) (x 1)) = prodStateK x` (line 1261) |
| product tests | `pairCarrierEquiv_maxCone` (maxCone → maxConeK, line 1277) and `maxCone_of_pairCarrierEquiv` (maxConeK → maxCone, line 1283), both through `sum_pairCarrier_eq` |
| dictionary | `mem_Q3_iff_pairCarrier : ω ∈ Q3 ↔ pairCarrierEquiv ω ∈ QK 2` (line 1301); both directions from `dictK_pairCarrier` and Mathlib's `Matrix.posSemidef_submatrix_equiv` |
| gate | `pairCarrierEquiv_cnot : pairCarrierEquiv (cnot ω) = cnotK 0 1 (pairCarrierEquiv ω)` (line 1312) |
| target actions | `pairCarrierEquiv_actT : pairCarrierEquiv (actT N ω) = actK 1 N (pairCarrierEquiv ω)` (line 1320) |

`pairCone_eq_Q3_of_kToken` (line 1336) has the hypotheses and conclusion of the
adopted `pairCone_eq_Q3_of_drive_maxCone` (EqvK2MaxCone.lean:153–160, unchanged
from D on main), with each of H1, hadd, hsmul, hmax, H2 and A an explicit
hypothesis, and is proved by applying `kCone_eq_QK_of_drive_maxCone` at `k = 2`
to the transported set `pairSet K`. At `k = 2` the guard `i < j` leaves only
`CNOT(0 → 1)` and the guard `j ≠ 0` only token 1 (`fin2_lt`, `fin2_ne_zero`).

The proof does not use the adopted two-token theorem or anything proved from
it. This was checked in two ways. `OIBridge.EqvK2MaxCone` is not in the import
closure of the design modules: FinitePauli imports `OIBridge.EqvK2Schema`,
FiniteReach imports `OIBridge.EqvK2Generation`, and `EqvK2MaxCone` imports
`EqvK2Generation`, not the reverse. Every declaration in the environment comes
from a module in that closure, and a declaration proved from the two-token
theorem would have to come from a module importing `EqvK2MaxCone`. The module
also checks this when it is compiled: an `#eval` after the recovery (line 1390)
fails the build if `OIBridge.EqvK2MaxCone.pairCone_eq_Q3_of_drive_maxCone` is in
the environment, and otherwise logs that it is not; run 38885086040 logs the second
outcome. The check excludes the adopted theorem and everything proved from it.
It does not exclude the ingredients of that theorem's proof or sibling
two-token theorems present in the environment
(`EqvK2Generation.blockInvariant_of_drive`, `pairCone_eq_Q3_of_drive_exact`,
`EqvK2Block.pairCone_eq_Q3_of_block`, `EqvK2Schema.pairCone_eq_Q3_of_drive`);
the design sources cite none of them. Under #829's proposed
`import OIBridge.EqvK2MaxCone` this check would fail by construction.

## The product-vector form of the product bound

Argument section 1, item 3, states the product bound in two forms. §12 of
`FiniteReachTable.lean` proves each direction separately, for a Hermitian
matrix `A` on k tokens:

- `prodVec_nonneg_of_maxConeTab` (line 1579), effect form to product-vector
  form: `coordinates k A ∈ maxConeTab k` gives
  `0 ≤ star (prodVec k a) ⬝ᵥ (A *ᵥ prodVec k a)` for every family `a` of
  one-token vectors, through `lorPair_nonneg_of_maxConeTab`, `lor_blochH` and
  `quad_dictionary_prodVec`.
- `maxConeTab_of_prodVec_nonneg` (line 1564), product-vector form to effect
  form. `lor_blochH_decomp` (line 1442) writes every forward-cone vector as a
  nonnegative combination of two Bloch vectors, with an explicit formula and
  no square root (the boundary case `v₀ + v₃ = 0` separately).
  `lorTests_of_blochTests` (line 1527) replaces the forward-cone vectors one
  token at a time by recursion on the token count, slicing a table along its
  last token (`tokSlice`, `sum_prodTab_succ`). `maxConeTab_of_blochTests`
  (line 1556) applies it to the homogenized coefficients of ball effects
  (the adopted `lor_ehom`).
- `maxConeTab_iff_prodVec_nonneg` (line 1594) states the equivalence with
  these two witnesses, one per direction.

No positive semidefinite hypothesis on `A` is used in either direction. The
cone theorems above use only the first direction.

## The finite control of the coordinate formulas

`tabact_vs_829.py` re-implements, with standard-library exact Gaussian-rational
arithmetic, the recursive definitions of `FiniteReach.lean` and
`FiniteReachTable.lean` and the preregistration's `cnotK` and `actK`, and
compares `tabAct` of every named generator with them for k = 1 to 4. Reversed
CNOT direction (`NEG-REV`), reversed rotation sign and the inverse cyclic map
are countercontrols, each detected as a mismatch. `NEG-SWAPDEF` is a degenerate
CNOT whose control reads past the end of the prefix and so acts as the identity.
`tabact_vs_829-output.txt` is its saved run: 89 checks, no failures and
`VERDICT TABACT-MATCHES-829-FORMULAS-k1..4`; two local `python3 -I -B` replays
of the script as listed in `SHA256SUMS` reproduced it byte for byte, with empty
standard error. The design workflow does not replay this script.
It is an independent finite control of the coordinate formulas, and the
compiled theorems do not use it.

## Remaining obligations

The steps between the compiled finite theorem and the statement proposed in
#829 are established in the form above: the coordinate formulas of the named
actions for every k, the transport to `Fin k → Fin 2` and `Fin k → Fin 4`,
the statement surface with its two inclusions and both directions of the
equivalence, and the k = 2 recovery. The following remain:

1. Adoption. The declarations are research sources. An adopted
   `OIBridge/KTokenMaxCone.lean`, the preregistration's S1–S4 controls, its
   k = 3 probe and its Q-EXACT question belong to a native round, which this
   record does not execute.
2. An owner decision before F, open: how the independence check of the k = 2
   recovery is kept at adoption. Either the proposed module imports
   `OIBridge.EqvK2Generation` instead of `OIBridge.EqvK2MaxCone` and keeps the
   `#eval`, or it keeps that import and replaces the `#eval` by a transitive
   used-constants check from `pairCone_eq_Q3_of_kToken` that fails on any
   constant with prefix `OIBridge.EqvK2MaxCone.` and on the sibling theorems
   listed above. The preregistration's S3, which checks direct names only, is
   weaker than either.
3. Optionally, construct the cyclic Gray schedule and prove the prefix-parity
   and Walsh correspondence, including zero controls. This identifies the
   compiled multiplexor with the Gray-ordered word of argument section 3; the
   cone theorems do not need it.

In particular, these modules do not prove arbitrary unitary universality. The
target remains exact pure-state reachability from a product preparation. They
also supply no implementation-class membership for KN-DESC and discharge no
physical source or state/operation compatibility premise. Identifying the
named generators with physical operations, the Pauli carrier with physical
k-token states, and the cone with a physical state space remains a premise.

The existing exact three-token checker remains a finite design comparison; it
does not certify the declarations above.
Productivity classification: ELABORATING, on the consistency axis.
