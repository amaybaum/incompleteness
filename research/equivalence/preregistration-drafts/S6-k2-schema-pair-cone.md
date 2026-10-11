# Reconstruction round K2-SCHEMA-1 — the pair cone under products, the gate, self-duality and one copy's rotations: PREREGISTRATION (draft for owner review)

**Status: research draft, not a control plane.** Written by the research thread `research/equivalence` (node E15,
round 4) and held on that branch under `research/equivalence/preregistration-drafts/` for owner review. No round is
opened, no pull request exists, nothing under `verification/` is written, no `D` is designated and no `F` exists. If
the owner opens the round, this text moves to the record directory below on a pull request from the designated `D`;
every measurement marked *(at L)* is re-taken at `D`; `controls.py` is generated; the predicted execution tree is built
and dispatched; and this file may change before `F` (`G9`). Measurements were taken at
L = `9f9f8257a980a1819fbbc1dc0019917cf8678626`.

**Readiness (round 4).** The statement surface is a built design module: `EqvK2Schema` (copy
`research/equivalence/lean/EqvK2Schema.lean`, blob `659ae36c`) built over L in design run 38101580750 with all 22 prints
`[propext, Classical.choice, Quot.sound]`, so the analogue of draft S4's checkpoint `C0` is met before drafting. The
exact layer the round would freeze was run this round (`e15_k2s6_probe`, 12/12, replay byte-identical). Every
predicted output below is generated from those measurements. Unmeasured, as in every draft: the predicted execution
tree at a designated `D` (the module under its predicted name `K2Schema`, a rename of the measured text; the census
family; `controls.py`; the probe shard). One optional pre-`F` hygiene item, warnings only: the unused `simp` arguments
the linter reports in run 38101580750. **§G**, the necessity direction of the equivalence (the invariance of `Q3` under
one copy's local unitary conjugations and the assembled `iff`), added after the coordinator's round-4 framing, is a
built design module too: `EqvK2Converse` (copy `research/equivalence/lean/EqvK2Converse.lean`, blob `4add9b8d`) built
over L in design run 38112803530 with all nine prints standard, so checkpoint `C0′` is met.

**Readiness (round 5).** Two further design modules over L, both built on the dev branch `dev-equivalence/r5-design`:
`EqvK2Block` (§H; copy `research/equivalence/lean/EqvK2Block.lean`, blob `23d0db23`; run 38132266383, 11/11 prints
standard; its first text failed to build in run 38124464622 and is kept as `lean/EqvK2Block.run38124464622.lean`) and
`EqvK2Generation` (§H.6; copy `lean/EqvK2Generation.lean`, blob `682f187e`; run 38134245361, 12/12 prints standard).
With them the schema needs no reachability hypothesis: `ReachPure` is a theorem (`reachPure`); sufficiency is
`pairCone_eq_Q3_of_drive_exact` (H1, H2, H3, `hA`); the equivalence is `pairCone_eq_Q3_iff_drive_exact` (given H1 and
H3, `K = Q3` iff H2 and `hA`), each direction a separate theorem; the block form (`pairCone_eq_Q3_of_block`,
`Q3_blockInvariant`, `pairCone_eq_Q3_iff_block`) states the forcing for invariance under the block-diagonal
`SU(2) × SU(2)`. Checkpoints `C0″` (§H) and `C0‴` (§H.6) are met in those runs. The countercontrol family enters the
controls with its self-duality on the countermodels thread's design-built `CmSprime.theorem_Sprime_ineq` (handoff
HO-30), every hypothesis of which this thread checked exactly for `K384`, `K768` and `KC`
(`experiments/e19_s6_controls.py`). The text below is revised to that surface; the round-4 statement
`pairCone_eq_Q3_of_drive` (with `hreach : ReachPure`) stays built and is now the instance
`pairCone_eq_Q3_of_drive hH1 hH2 hH3 hA reachPure`.

```v3-round
round K2-SCHEMA-1
kind non-sealing
record-directory verification/programmes/oi-qm/reconstruction/round-k2-schema-1-pair-cone/
```

```v3-governed-paths
record AM verification/programmes/oi-qm/reconstruction/round-k2-schema-1-pair-cone/
record AM verification/receipts/K2-SCHEMA-1.json
execution A verification/lean-mathlib/OIBridge/K2Schema.lean
execution A verification/lean/k2_schema1_probe.py
execution M verification/lean-mathlib/OIBridge.lean
execution M verification/lean-manuscript-census.json
execution M .github/workflows/verify.yml
```

The record directory would hold this preregistration, `controls.py` and the result note. **No manuscript, no built
artifact, `verification/ROADMAP.md`, no landed kernel module and no other round's record change under any outcome.**

## The objects

- **`D`** — to be designated by the owner. Drafting measurements: L. **`F`**, **`E`**, **`Λ`**, **`Q`** as §A.39.

## What the round is

K2 (ROADMAP :1001–1006) is OPEN: "no governed round records the classification or the cone theorem", and its
obligations include the composite cone and local actions compatible with it. At L the pair carrier is DIM-1's `W 3`
(CompositeDimension.lean:97) with the gate `cnot` (:775); the candidate-cone family and the reversible part of the
local-action clause are settled by K2-GUARD-1 (`CandidateCone`, K2Guard.lean:95; `no_candidateCone_cnot_reflY`, :143).
The audited stage records show that products, the gate and self-duality do not force the two-qubit positive cone:
exotic self-dual cones exist. The research record proposes that one further invariance does: invariance under one
copy's rotations about the third axis and its cyclic permutation (A_miss, in handoff HO-5's form). The round states the
schema as an equivalence: **given H1 and H3, `K = Q3` iff H2 and A_miss, where A_miss is the invariance of `K` under
the flow and `cycEquiv`** — each direction separately witnessed (§A.34): sufficiency by `pairCone_eq_Q3_of_drive_exact`
(§H.6: the gate and the clause's two operations generate, by exact finite words, the block-diagonal `SU(2) × SU(2)`,
under which the products reach every pure state, so `ReachPure` is the theorem `reachPure`), necessity by `Q3_cnot`
and `Q3_aMiss` (§G, §H.6: `Q3` is invariant under the gate and under one copy's local unitary conjugations).

**Scope: the equivalence is between cone-level statements.** A_miss is cone-preserving admissibility — the invariance
of `K` under `actT (rotLin t)` for every `t` and under `actT cycEquiv` — an introduced hypothesis, not a premise at L:
the equivalence does not source it and adopts nothing; it says that, given H1 and H3, the pair cone is `Q3` exactly
when it has that invariance together with the gate invariance H2. The necessity direction proves A_miss in this invariance reading only: `Q3`'s
invariance under every local unitary gives `Q3 ⇒ A_miss` and says nothing about whether those operations are available
through the kernel's protocols. That availability is the H-level premise (A)/H-OI_g — for this repertoire, H-OI_g at
`{R_z(θ₀), J}` (handoff HO-20 item 4, CONDITIONAL), the hidden-history premise of the two-rotation invariance clause
below — a separate question S6 does not decide; a quantum cone with a restricted set of available transformations has the invariance
without the availability. With A the transferred pair-level premises at L (the 118 rows stage 6 transferred) and (b)
the composite action, the stage-6 record has a cone meeting A and not (b) (K(Z_F) [A]): (b) is independent of the
transferred pair-level premises at L; the 68 rows not reached at stage 6 have not been shown irrelevant, so the record
does not make (b) or A_miss independent of OI. A_miss is a form of (b) (I3.150, I3.153). A failure of `Q3` (`K ≠ Q3`) is
not a failure of any particular instance of A_miss; a failure of an instance is a failure of `Q3` only through `Q3`'s
invariance under that operation (§G).

The round asks:

- **Q-CONE (kernel).** Is the two-token Pauli dictionary a real-linear equivalence
  `W 3 ≃ₗ[ℝ] selfAdjoint (Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ)` carrying product states to Kronecker products and
  the table pairing to four times the trace pairing, and do the two cone lemmas hold — LOWER (a set closed under
  addition that contains a table of every rank-one positive matrix contains `Q3`), UPPER (such a set lying in its own
  dual lies in `Q3`) — with `Q3 = dualW Q3` as the positive control for self-duality?
- **Q-SUFF (kernel, the sufficiency direction).** Does `pairCone_eq_Q3_of_drive_exact` hold with exactly its four
  hypotheses H1, H2, H3, `hA` (below), with no reachability hypothesis?
- **Q-GEN (kernel, the generation step).** Do the gate and the clause's two operations give invariance under the
  block-diagonal `SU(2) × SU(2)` (`blockInvariant_of_drive`, exact finite words, no closure), and is `ReachPure` a
  theorem (`reachPure`)?
- **Q-NEC (kernel, the necessity direction).** Is `Q3` invariant under the gate (`Q3_cnot`) and under `actT (rotLin t)`
  for every `t` and `actT cycEquiv` (`Q3_aMiss`: A_miss in its invariance reading), so that, given H1 and H3,
  `K = Q3 ↔ (H2 ∧ A_miss)` (`pairCone_eq_Q3_iff_drive_exact`)?
- **Q-BLOCK (kernel, the block form).** Given H1 and H3, is `K = Q3` equivalent to invariance under the block-diagonal
  `SU(2) × SU(2)` (`pairCone_eq_Q3_of_block`, `Q3_blockInvariant`, `pairCone_eq_Q3_iff_block`)?
- **Q-EXACT (exact layer).** Do the exact checks hold — the lifts of the generators, the positive control `Q3`, the
  reachability lemma on exact instances — and does the countercontrol behave as stated: under the native octahedral
  repertoire on one copy in place of the rotations, an explicit invariant cone with the products differs from `Q3` and
  is not preserved by the rotation with `cos t = 3/5`?

## The kernel declarations the round would add (frozen surface, module `OIBridge/K2Schema.lean`)

Imports `OIBridge.CompositeDimension`, `OIBridge.BoundaryAudit`, `Mathlib.LinearAlgebra.Matrix.PosDef`; namespace
`OIBridge.K2Schema`. The statement surface is the design module `EqvK2Schema` as built in run 38101580750, renamed, no
statement changed. The definitions `pauli`, `tokMat` and `dict` are the bridge thread's draft definitions verbatim
(handoffs HO-18, HO-21), so one dictionary serves both threads. Its declarations, in order:

- §A the Pauli matrices: `pauli`, `pauli_conjTranspose`, `trace_pauli_mul`, `pauli_complete`;
- §B the kernel tensor on one-token matrices: `tensorOf_mul`, `trace_tensorOf`, `tensorOf_conjTranspose`,
  `trace_T_mul_T`;
- §C the dictionary: `tokMat`, `dict` (`dict ω = ¼ Σ ω_μν σ_μ ⊗ σ_ν`, control first), `dict_tens`, `dict_prodState`,
  `dict_add`, `dict_smul`, `dictLin`, `dict_sum`, `star_ofReal_div_four`, `dict_conjTranspose`, `dict_isHermitian`,
  `trace_T_mul_dict`, `dict_mul_left`, `ipW` (the Euclidean table pairing), `trace_dict_mul`, `ipW_eq_trace`,
  `coordOf`, `coordOf_dict`, `dict_injective`;
- §D completeness and the equivalence: `sum_T_entry`, `dict_complete4`, `trace_T_mul_real`, `dict_coordOf`,
  `dictEquiv`, `dictEquiv_apply`;
- §E the cone step: `dualW`, `mem_dualW`, `Q3` (`{ω | (dict ω).PosSemidef}`), `mem_Q3`, `ipW_add_right`,
  `ipW_smul_right`, `trace_vecMulVec_mul`, `posSemidef_dict_of_pure`, `subset_Q3_of_pure_dual` (UPPER),
  `Q3_subset_of_pure` (LOWER, through `psdFactorization_discharged`, BoundaryAudit.lean:100), `Q3_subset_dualW`,
  `dualW_Q3_subset`, `Q3_selfDual`;
- §F the drive words and the assembly: `actTLin`, `driveGens` (`cnot`, every `actTLin (rotLin t)`,
  `actTLin cycEquiv`; `rotLin` KInfFoundations.lean:386, `cycEquiv` :416), `driveWords` (the submonoid they generate),
  `driveWords_preserve`, `ReachPure`, `pairCone_eq_Q3_of_drive`.

The two §F statements a round reads, quoted from the built module:

```lean
def ReachPure : Prop :=
  ∀ x : Fin 2 × Fin 2 → ℂ, ∃ g ∈ driveWords, ∃ x₀ ∈ TransitiveBody.eball 3,
    ∃ y₀ ∈ TransitiveBody.eball 3, ∃ c : ℝ, 0 ≤ c ∧
      dict (c • g (prodState x₀ y₀)) = Matrix.vecMulVec x (star x)

theorem pairCone_eq_Q3_of_drive {K : Set (W 3)}
    (hH1 : ∀ x ∈ TransitiveBody.eball 3, ∀ y ∈ TransitiveBody.eball 3, prodState x y ∈ K)
    (hH2 : ∀ ω ∈ K, cnot ω ∈ K)
    (hH3 : K = dualW K)
    (hA : ∀ t : ℝ, ∀ ω ∈ K, actT (KInfFoundations.rotLin t) ω ∈ K ∧
      actT (KInfFoundations.cycEquiv : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) ω ∈ K)
    (hreach : ReachPure) :
    K = Q3
```

**§G, the necessity direction (a design module of its own, `EqvK2Converse`, copy
`research/equivalence/lean/EqvK2Converse.lean`, blob `4add9b8d`, measured before `F` — checkpoint `C0′`).** Its
declarations, appended in order to the module and renamed into `K2Schema`, no statement changed: `dict_eq_sum_tensorOf`
(the split `dict ω = Σ_μ (½σ_μ) ⊗ tokMat (ω μ)`), `dict_actT`, `tensorOf_conj`, `tokMat_eq`, `mat2_ext`, `phaseMat`,
`phaseMat_conjTranspose`, `homMap_rotLin`, `tokMat_rot`, `cycMat`, `cycMatH`, `cycMat_conjTranspose`, `homMap_cyc`,
`tokMat_cyc`, the two intertwining lemmas — `dict_actT_rotLin` (the dictionary carries `actT (rotLin t)` to conjugation
by `1 ⊗ diag(1, cos t + i sin t)` for every real `t`) and `dict_actT_cyc` (`actT cycEquiv` to conjugation by
`1 ⊗ (I − i(X + Y + Z))/2`) — the identities also checked exactly by `e15_k2s6_probe` D1 at `cos t = 3/5` and `t = π/2`
and by `e10_k2_schema` L2 at `cos t = 5/13` (the monomial case is also the bridge thread's `BridgeDictionary` [D],
handoff HO-21) — and

```lean
theorem Q3_aMiss : ∀ t : ℝ, ∀ ω ∈ Q3, actT (KInfFoundations.rotLin t) ω ∈ Q3 ∧
    actT (KInfFoundations.cycEquiv : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) ω ∈ Q3

theorem pairCone_eq_Q3_iff_drive {K : Set (W 3)}
    (hH1 : ∀ x ∈ TransitiveBody.eball 3, ∀ y ∈ TransitiveBody.eball 3, prodState x y ∈ K)
    (hH2 : ∀ ω ∈ K, cnot ω ∈ K) (hH3 : K = dualW K) (hreach : ReachPure) :
    K = Q3 ↔ ∀ t : ℝ, ∀ ω ∈ K, actT (KInfFoundations.rotLin t) ω ∈ K ∧
      actT (KInfFoundations.cycEquiv : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) ω ∈ K
```

The direction `→` is `Q3_aMiss` after substituting `K = Q3` (unitary conjugation preserves positive semidefiniteness,
Mathlib's `PosSemidef.mul_mul_conjTranspose_same`); the direction `←` is `pairCone_eq_Q3_of_drive`. The two directions
are witnessed by different declarations; neither is an extension, uniqueness or density theorem standing in for the
other. Both sides of the `iff` are statements about the cone: `→` yields the invariance of `Q3`, not the availability of
the operations (the H-level premise (A)/H-OI_g, not in S6). §G is [D] (design run 38112803530), not certified.

**§H, the block form (design module `EqvK2Block`, blob `23d0db23`, run 38132266383 — checkpoint `C0″`).** Its
declarations, appended in order and renamed into `K2Schema`, no statement changed: `P0`, `P1`, `blockMat`
(`P₀ ⊗ U₀ + P₁ ⊗ U₁`), `blockAct` (its action on tables through the dictionary), `IsSU`, `BlockInvariant`,
`dict_blockAct`, `blockVec`, `blockVec_eq`, `blockMat_mulVec`, `conj_vecMulVec`, the one-token lemmas `nrm2`, `nrm`,
`rotTo`, `suTo` and their facts, `bloch`, `tensVec`, `tokMat_hom_bloch`, `dict_prod_bloch`, **`reach_block`** (every
rank-one positive matrix is a block conjugate, by a pair of special unitaries, of the dictionary image of a nonnegative
multiple of a product state — Theorem C19-1 (a) of handoff HO-31), and

```lean
theorem pairCone_eq_Q3_of_block {K : Set (W 3)}
    (hH1 : ∀ x ∈ TransitiveBody.eball 3, ∀ y ∈ TransitiveBody.eball 3, prodState x y ∈ K)
    (hH3 : K = dualW K) (hB : BlockInvariant K) : K = Q3

theorem Q3_blockInvariant : BlockInvariant Q3

theorem pairCone_eq_Q3_iff_block {K : Set (W 3)} (hH1 …) (hH3 : K = dualW K) : K = Q3 ↔ BlockInvariant K
```

with `aMiss_of_blockInvariant` (block invariance gives the full-flow form of A_miss; it does not give H2, the gate
having determinant ratio `−1`). The block form has neither the gate nor a reachability statement among its hypotheses.

**§H.6, the generation step (design module `EqvK2Generation`, blob `682f187e`, run 38134245361 — checkpoint `C0‴`).**
Conjugation invariance `ConjInv K M` is closed under products and unit scalars; the generators are the flow at every
point of the unit circle, the cyclic lift and its inverse (`cycMatᴴ = −cycMat²`), and the gate as the block pair
`(1, X)`; every special unitary is `diag(a, ā) · R(c, s) · diag(b, b̄)` (`su_euler`, exact, no angles), the real rotation
is `cycMatᴴ · diag(c − is, c + is) · cycMat` (`rotRe_eq`), and the controlled diagonal pair is the word
`gate · (1 ⊗ diag(r, r̄)) · gate · (1 ⊗ diag(r̄, r))` (`rtrick`). Then

```lean
theorem blockInvariant_of_drive {K : Set (W 3)} (hH2 : ∀ ω ∈ K, cnot ω ∈ K)
    (hA : ∀ t : ℝ, ∀ ω ∈ K, actT (KInfFoundations.rotLin t) ω ∈ K ∧
      actT (KInfFoundations.cycEquiv : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) ω ∈ K) : BlockInvariant K

theorem reachPure : ReachPure

theorem pairCone_eq_Q3_of_drive_exact {K : Set (W 3)} (hH1 …) (hH2 : ∀ ω ∈ K, cnot ω ∈ K)
    (hH3 : K = dualW K) (hA …) : K = Q3

theorem Q3_cnot : ∀ ω ∈ Q3, cnot ω ∈ Q3

theorem pairCone_eq_Q3_iff_drive_exact {K : Set (W 3)} (hH1 …) (hH3 : K = dualW K) :
    K = Q3 ↔ ((∀ ω ∈ K, cnot ω ∈ K) ∧ ∀ t : ℝ, ∀ ω ∈ K, actT (KInfFoundations.rotLin t) ω ∈ K ∧
      actT (KInfFoundations.cycEquiv : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) ω ∈ K)
```

(`hH1` and `hA` as in §F). The direction `→` of the last is `Q3_cnot` with `Q3_aMiss`; the direction `←` is
`pairCone_eq_Q3_of_drive_exact` = `pairCone_eq_Q3_of_block ∘ blockInvariant_of_drive`. `reachPure` is proved by
applying `blockInvariant_of_drive` to the set of scaled drive images of products (which satisfies H2 and A_miss by
construction) and `reach_block`. No closure, density or continuity enters §H.6: every element of the block group acts
as a finite composition of the generators' actions.

`#print axioms` lines: the 22 of the built module (EqvK2Schema.lean:453–474), in the built order, §G's nine
(EqvK2Converse.lean:226–234): `dict_eq_sum_tensorOf`, `tensorOf_conj`, `tokMat_eq`, `tokMat_rot`, `tokMat_cyc`,
`dict_actT_rotLin`, `dict_actT_cyc`, `Q3_aMiss`, `pairCone_eq_Q3_iff_drive`, §H's eleven (`dict_blockAct`,
`blockMat_mulVec`, `conj_vecMulVec`, `suTo_isSU`, `suTo_mulVec`, `dict_prod_bloch`, `reach_block`,
`pairCone_eq_Q3_of_block`, `Q3_blockInvariant`, `pairCone_eq_Q3_iff_block`, `aMiss_of_blockInvariant`) and §H.6's twelve
(`blockMat_mul`, `cycMat_conjTranspose_eq`, `rotRe_eq`, `su_euler`, `conjInv_idle`, `rtrick`, `conjInv_ctrl`,
`blockInvariant_of_drive`, `reachPure`, `pairCone_eq_Q3_of_drive_exact`, `Q3_cnot`, `pairCone_eq_Q3_iff_drive_exact`):
54 prints. §H.6 imports the bridge thread's `BridgeDictionary` and `BridgeConverge` (for `dict_cnot` on the one
dictionary, handoff HO-34); a round would carry their two declarations it uses (`cnotMat`, `dict_cnot`) or land them
first — a surface decision for the owner. **Census family:**
"the pair-level composite cone, conditionally: products of ball states, invariance under DIM-1's gate and under one
copy's rotations about the third axis and its cyclic permutation, and self-duality under the table pairing give the
two-qubit positive cone through the Pauli dictionary, and conversely (round K2-SCHEMA-1, reconstruction)", `modules: ["K2Schema"]`, `status: "kernel-only"`, `manuscript: []`. **Import line** after
`import OIBridge.RelcSelectC5`.

## The A_miss hypothesis, exactly; `ReachPure` a theorem

- **A_miss is the full-flow form.** `hA` is invariance under `actT (rotLin t)` for **every** `t : ℝ` together with
  `actT cycEquiv` — the form of handoff HO-5. With the gate (H2) it generates, by exact finite words, the block-diagonal
  `SU(2) × SU(2)` (§H.6): no closure, no density, no continuity and no closedness of `K` enter the sufficiency
  direction.
- **The two-rotation clause (dense-control form) is the stronger theorem this round does not freeze.** HO-13 item 2:
  invariance under `actT (rotLin θ₀)`, `cos θ₀ = 3/5`, and `actT cycEquiv`. Its passage to the flow needs, as premises
  named before C19-1 (a) gives `ReachPure`: (i) `K` closed — a consequence of H3 (`isClosed_of_selfDual`; the one-sided
  `K ⊆ dualW K` does not suffice); (ii) the action of a one-token matrix on tables continuous
  (`continuous_transferMap`); (iii) the closure identification — its density half DENSE(θ₀) (every phase of the flow
  lies in the closure of the one rotation's powers: Niven and Kronecker [L], a fact about the circle with no physical
  content, an explicit hypothesis of `flow_of_dense`), its generation half `blockInvariant_of_drive` (§H.6); (iv) the
  closure lemma (`invariant_of_closure`, `flow_of_dense`). (i), (ii), (iv) are [D] in the research thread's design
  module `EqvOneDictionary` (run 38132266383, not part of this round's surface); so the two-rotation form gives `Q3`
  from H1, H2, H3 and the one-angle clause modulo DENSE(θ₀) [L] and the iteration of one rotation to its powers [W].
  Its premise at the hidden-history level is H-OI_g at `{R_z(θ₀), J}`, nothing weaker (handoff HO-20 item 4,
  CONDITIONAL); an exact token model of the clause exists only under a re-preparation law the stated access refutes
  (handoff HO-17 item 4).
- **`ReachPure` is a theorem, not a hypothesis** (`reachPure`, §H.6). It is a statement about the drive words and the
  dictionary only — every rank-one positive two-qubit matrix is, up to a nonnegative scale, the dictionary image of a
  drive word applied to a product of ball states — and it holds outright: the drive words realize every element of
  the block-diagonal `SU(2) × SU(2)` on tables, under which the products reach every pure state (`reach_block`). Its
  finite-group analogue fails: no element of the order-384 group of the finite clause carries
  `φ₀ = (1, 2, 3i, −1+i)/4` to a product (X7 below; for every finite subgroup of `U(4)` by the bridge thread's
  `reachUnitary_finite`, a design-run statement, handoff HO-23).

## The hypotheses, classified against the premise inventory (owner's rule: derive, do not introduce)

The sufficiency theorem's form is **OI + {H2, H3, A_miss (full flow)} ⇒ K = Q3**: three of its hypotheses are
introduced, so it is not of the form "OI ⇒ X". The equivalence of §H.6 has the form **OI + {H3} ⇒ (K = Q3 ↔ (H2 ∧
A_miss))**, H2 ∧ A_miss (invariance form) being on one side of it, not premises; the block form has the form
**OI + {H3} ⇒ (K = Q3 ↔ BlockInvariant)**. `ReachPure` is no hypothesis of either: it is the theorem `reachPure`. Inventory ids are the stage-6 premise inventory's (`research/archive/pt/I3/INVENTORY.md`
at `research/archive` @ `4dc0321c`, sha256 `51eff9af…`), with the status each record fixes at L.

| hypothesis or setting item | kind | inventory id and status at L |
|---|---|---|
| the pair carrier `W 3` (local tomography encoded) | (i) inventory item | I3.1 `W d`: assumed (the premise the carrier encodes; K2 OPEN) |
| `hH1`: every product of `eball 3` states lies in `K` | (i) inventory item | the products clause of I3.43 `CandidateCone`: assumed (also the PT-record H1, I3.147) |
| the token body is `eball 3` | (i) inventory items | the output of TRB-1 (I3.89, proved [K]) from K∞-Trans (I3.170) and the other K∞ seams (I3.166–I3.174), each open, unsourced |
| `hH2`: `cnot`-invariance of `K` | (ii) **introduced, not an OI premise** | PT-record H2 (I3.148); `cnot` itself is I3.11, but no kernel statement at L asserts `cnot K ⊆ K` of any cone (I3.9's bridge note) |
| `hH3`: `K = dualW K` | (ii) **introduced, not an OI premise** | PT-record H3 (I3.149); `ipW` and `dualW` are not at L (I3.143) |
| A_miss (invariance form, introduced) — `hA` in §F, one side of the equivalence in §G: the invariance of `K` under `actT (rotLin t)` for every `t` and under `actT cycEquiv` | (ii) **introduced, not an OI premise** | the open bridge: K2's clause "local actions compatible with the composite cone" (I3.165, open), in a form of (b) (I3.150 (b_S4), I3.153 (b_DJ)): PT-record open, flagged do not assume |
| (A)/H-OI_g (availability, H-level, not in S6) — the operational availability of those operations through the kernel's protocols | not a hypothesis of any statement of the round | the H-level premise; for this repertoire H-OI_g at `{R_z(θ₀), J}` (handoff HO-20 item 4, CONDITIONAL); neither assumed nor decided by S6, and not implied by A_miss |
| `ReachPure` | **not a hypothesis: a theorem** (`reachPure`, §H.6, [D] run 38134245361) | not an inventory record; pure-state reachability is flagged do not assume (I3.144) — it is not assumed: it is proved, as a statement about the drive words and the dictionary only |
| BlockInvariant (the block form's hypothesis): invariance under `blockAct U₀ U₁` for every pair of special unitaries | (ii) **introduced, not an OI premise** in the block form; in the generator form not a hypothesis (it follows from H2 and A_miss, `blockInvariant_of_drive`) | a form of (b) for the operations of the block-diagonal `SU(2) × SU(2)` (I3.165; I3.150, I3.153) |
| DENSE(θ₀) (the two-rotation form only, not frozen) | a mathematical statement [L] (Niven; Kronecker), carried as an explicit hypothesis of `flow_of_dense` | not an inventory record; no physical content |

The objects `dict`, `Q3`, `ipW`, `dualW`, `driveWords` are definitions of the module (the comparison objects of I3.144 at
L only in a design preflight), not hypotheses. Using the four introduced hypotheses in this theorem does not make any of
them an OI premise. The countercontrol family below satisfies H1, H2 and H3 and differs from `Q3`, so the continuous part
of A_miss is load-bearing; H1, H2 and H3 are load-bearing by the witnesses of control S3.

## The cited inputs and their evidence layers (owner's rule: layers kept separate)

| input | layer |
|---|---|
| the 22 declarations of `EqvK2Schema` (the frozen surface) | [D] design run 38101580750, not certified |
| §G, the declarations of `EqvK2Converse` (the frozen surface's necessity direction) | [D] design run 38112803530, not certified |
| `cnot` and its relations (CompositeDimension.lean:775, :854, :860), `rotLin` (KInfFoundations.lean:386), `cycEquiv` (:416), `psdFactorization_discharged` (BoundaryAudit.lean:100), `CandidateCone` (K2Guard.lean:95), `actT_reflY_phiW` (:106), `cnot_idW` (:110), `chain_value` (:134), `no_candidateCone_cnot_reflY` (:143) | [K] kernel at L |
| the verdicts of DIM-1 and K2-GUARD-1 on those declarations | CERTIFIED (landed rounds) |
| the exact layer `e15_k2s6_probe` | [X] |
| §H (`EqvK2Block`) and §H.6 (`EqvK2Generation`): the block form, the generation step, `reachPure`, the full-flow equivalence | [D] design runs 38132266383 and 38134245361, not certified |
| (i), (ii), (iv) of the two-rotation form (`isClosed_of_selfDual`, `continuous_transferMap`, `invariant_of_closure`, `flow_of_dense`; research module `EqvOneDictionary`) | [D] design run 38132266383, not part of the frozen surface |
| the countercontrol family's self-duality: `CmSprime.theorem_Sprime_ineq` (the countermodels thread, handoff HO-30), with every hypothesis checked exactly for `K384` (`K*`), `K768` and `KC` | [D] (countermodels design run) + [X] (`e19_s6_controls` K1–K3, this thread) |
| the compact-defect cone `Kk` (HO-31 item 3, HO-32) | on Theorem S′ for compact defect sets: [W] |
| the group generated: the determinant-ratio invariant, the two-reflection and Euler words on exact instances | [X] (`e19_s6_controls` K4, `e19b_block_controls` B4, B6, B7) |
| the two-rotation clause (HO-13 item 2) | [W] + [X] + [L] Niven |
| claim (D) and K(Z_F) (stage records) | [A] |
| `BridgeDictionary` (HO-21) and `reachUnitary_finite` (HO-23) | [D] bridge-thread design runs |
| HO-17 item 4, HO-20 item 4, HO-22 items 1 and 3, HO-25 items 1–2 | at their handoff labels (CONJECTURE or CONDITIONAL; [W], [X], [A]) |

## The exact layer (frozen probe `verification/lean/k2_schema1_probe.py`)

The probe is `research/equivalence/experiments/e15_k2s6_probe.py` (sha256
`78cd7c592e9dde0febc585758a215a447b857beeb58bf6f914eb82cd1e48c319`; exact Gaussian-rational arithmetic, sympy 1.14.0 in R1
only), with its two kernel paths set to `CompositeDimension.lean` and `KInfFoundations.lean` beside it in the tree and
nothing else changed. It parses the kernel's `cnot`, `rotFun` and `cycEquiv`. Its checks:

- **D1** through the dictionary, on all sixteen basis tables: the parsed `cnot` is `Ad(CNOT)`; `actT R_z(π/2)` is
  `Ad(1 ⊗ diag(1, i))`; `actT cyc3` is `Ad(1 ⊗ (I − i(X + Y + Z))/2)`; `actT R_z(θ₀)` is `Ad(1 ⊗ diag(1, (3 + 4i)/5))`;
  each lift unitary. **D2** the table group `G₃₈₄ = ⟨cnot, actT R_z(π/2), actT cyc3⟩` has order 384.
- **P1, P2** positive control `Q3`: products of 36 pairs of rational ball points have positive semidefinite Kronecker
  images (exact principal minors); a non-positive table pairs negatively with a pure state.
- **X1–X6** the countercontrol, handoff HO-24 item 4 recomputed: the defect `d* = I − c* P_{h*}`,
  `h* = (10, 2 − 2i, −1 − 3i, 3 − i)/√128`, `c* = 401/400`, has a `G₃₈₄`-orbit `Z` of 192 rays closed under the three
  lifts (X1); the 18336 pairwise squared overlaps lie in `[25/2048, 13/16]` (X2); every defect admits the products (H1:
  `c* λ_max ≤ 1`, minimum normalized `|det Ψ|²` `85/2048`) (X3); condition (CC) `c*² s ≥ 4(c* − 1)` holds on every pair
  (X4); `d*` is not positive semidefinite, `⟨h*|d*|h*⟩ = −1/400`, and HO-24's table `z* = E00/2 − (c*/8) T_{h*}` has
  dictionary image `d*/8` (X5); with `R = 1 ⊗ diag(1, (3 + 4i)/5)`, `R h*` has squared overlap at most `1949/2048 < 400/401`
  with every ray of `Z`, so its projector is positive and lies in `Z*`, pairs nonnegatively with every element of
  `K* = (PSD ∩ Z*) + cone Z`, and pairs `−1/400` with `R d* R*`: the rotation with `cos t = 3/5` does not preserve `K*`
  although every element of `G₃₈₄` does (X6).
- **X7** the orbit of `φ₀` under `G₃₈₄` has 384 rays, none a product (minimum normalized `|det Ψ|²` `5/256`).
- **R1** lemma L4 on five exact states (NOTES-E10's code, unchanged).
- **XC1, XC2, XC3** (countercontrols, each must fail as stated): (CC) at `c′ = 301/300` holds on every pair (it fails on
  the minimal-overlap pair); `K*` is invariant under `actT R_z(θ₀)` (X6's witness); `d*` is positive semidefinite.

Read together: `K*` contains the products (X3), is invariant under the gate and the finite clause (X1 with D1, and
unitary conjugation preserves positive semidefiniteness), differs from `Q3` (X5) and violates the full-flow `hA` at
`t = θ₀` (X6). Its self-duality is Theorem S′ of the countermodels thread (handoff HO-24 item 3; hypothesis (CC) on every
pair, checked by X4; a written proof read by the coordinator and found sound, not kernel-checked and not checked by
this round). So the full-flow hypothesis is load-bearing in the sense the round can state: the module's theorem with
`hA` weakened to the finite clause fails on `K*` given Theorem S′. Handoff HO-25 records the same on the cone side for
each half of A_miss alone (the Clifford half by an explicit cone through S′, the continuous half through claim (D) of
the audited record); the round asserts neither.

## The decision rules (frozen; implemented by `controls.py verdict`)

| Cell | Outcome | Rule |
|---|---|---|
| Q-CONE | `K2-SCHEMA-CONE-STEP-PROVED` | `dictEquiv`, `dict_prodState`, `ipW_eq_trace`, `subset_Q3_of_pure_dual`, `Q3_subset_of_pure`, `Q3_selfDual` and every declaration of the module they depend on have their frozen statements, resolve to the landed objects (S2), and are built at `E` with their `#print axioms` lines within `[propext, Classical.choice, Quot.sound]` |
| Q-CONE | `K2-SCHEMA-CONE-STEP-NOT-ESTABLISHED` | otherwise |
| Q-SUFF | `K2-SCHEMA-SUFFICIENCY-PROVED` | `pairCone_eq_Q3_of_drive_exact` has its frozen statement — exactly the four hypotheses H1, H2, H3, `hA` (the full-flow form), no reachability hypothesis — resolves to the landed objects, and is built at `E` with its print within the three axioms |
| Q-SUFF | `K2-SCHEMA-SUFFICIENCY-NOT-ESTABLISHED` | otherwise |
| Q-GEN | `K2-SCHEMA-GENERATION-PROVED` | `blockInvariant_of_drive` (exactly the hypotheses `hH2`, `hA`) and `reachPure` (no hypothesis; `ReachPure` the frozen definition) have their frozen statements, resolve to the landed objects, and are built at `E` with their prints within the three axioms |
| Q-GEN | `K2-SCHEMA-GENERATION-NOT-ESTABLISHED` | otherwise |
| Q-NEC | `K2-SCHEMA-NECESSITY-PROVED` | `Q3_aMiss`, `Q3_cnot` and `pairCone_eq_Q3_iff_drive_exact` (exactly the hypotheses `hH1`, `hH3`; its `→` citing `Q3_cnot` and `Q3_aMiss`, its `←` citing `pairCone_eq_Q3_of_drive_exact`) have their frozen statements, resolve to the landed objects, and are built at `E` with their prints within the three axioms |
| Q-NEC | `K2-SCHEMA-NECESSITY-NOT-ESTABLISHED` | otherwise |
| Q-BLOCK | `K2-SCHEMA-BLOCK-FORM-PROVED` | `pairCone_eq_Q3_of_block` (exactly `hH1`, `hH3`, `hB`), `Q3_blockInvariant` and `pairCone_eq_Q3_iff_block` have their frozen statements, resolve to the landed objects, and are built at `E` with their prints within the three axioms |
| Q-BLOCK | `K2-SCHEMA-BLOCK-FORM-NOT-ESTABLISHED` | otherwise |
| Q-EXACT | `K2-SCHEMA-INSTANCES-EXACT` | the probe blob at `E`, run by `controls.py` with `python3 -I`, prints `PASS` for D1, D2, P1, P2, X1–X7 and R1, no `FAIL`, `COUNTER XC1 fails as stated`, `COUNTER XC2 fails as stated`, `COUNTER XC3 fails as stated`, `checks: 12, failures: 0` and `VERDICT E15-S6-EXACT-LAYER-CONSISTENT` |
| Q-EXACT | `K2-SCHEMA-INSTANCES-NOT-ESTABLISHED` | otherwise |

No rule reads another cell's outcome. `K2-SCHEMA-1-READ` when the six cells are assigned; tokens printed by
`controls.py verdict E` from the measurements at `E`.

## The earned reading and the non-inference rule (frozen)

> Earned reading (only when all six cells are positive): on the pair carrier of two copies of the Euclidean 3-ball,
> a set of joint vectors that contains every product of ball states, is invariant under DIM-1's gate and under one
> copy's rotations about the third axis and its cyclic permutation, and equals its own dual under the table pairing is
> the two-qubit positive cone read through the Pauli dictionary. The gate and those operations generate, by finite
> compositions, every block-diagonal pair of special unitaries, and under these the products reach every pure state,
> so every pure two-qubit state is reachable from a product by the drive words (ReachPure holds). Conversely the
> two-qubit positive cone is invariant under the gate, those rotations and that permutation, so, given the products and
> self-duality, the pair cone is the two-qubit positive cone exactly when it has the gate invariance and the rotation
> invariance, properties of the cone; equivalently, exactly when it is invariant under every block-diagonal pair of
> special unitaries. With the octahedral repertoire on that copy in place of the rotations, an explicit set with the
> products, invariant under the gate and that repertoire, differs from the two-qubit positive cone and is not invariant
> under the rotation with cosine 3/5. The gate invariance and self-duality are introduced hypotheses, not OI premises,
> and the rotation invariance is the open bridge, not a premise: the results have the forms OI + {H2, H3, A_miss} ⇒
> K = Q3, OI + {H3} ⇒ (K = Q3 ↔ (H2 ∧ A_miss)) and OI + {H3} ⇒ (K = Q3 ↔ BlockInvariant).

> Non-inference rule: this round does not show that OI supplies the composite cone, the gate, self-duality or the
> rotations; the products clause, the gate invariance, self-duality and the rotation invariance are premises. The
> reachability statement it proves concerns the operations, not the cone, and sources none of them. The equivalence
> does not source the gate or the rotation invariance: it says only that, given the products and self-duality, those
> invariances and the conclusion stand or fall together; a failure of the conclusion is not a failure of any particular
> operation's invariance. It does not show that the gate, the rotations or the permutation are available operations:
> their invariance is a property of the cone, and availability is a separate premise the round does not address. It does
> not formalize invariance under one rotation of irrational angle and the cyclic permutation in place of the rotations.
> It says nothing about more than two copies, local tomography as a source, the antiunitary or complete-positivity
> bridge, the relation to K3, or H-Bell. The countercontrol set's self-duality rests on another research thread's
> design-built theorem, whose hypotheses the exact layer checks; that theorem is not certified by this round. The probe
> is an exact computation, not a Lean kernel proof.

**Premises this round does NOT source:** H2 (`cnot`-invariance), H3 (`K = dualW K`), A_miss (the invariance of `K`
under the full flow with `cycEquiv`) and H1 as a property of a composite. H2, H3 and A_miss are introduced hypotheses,
not OI premises; H1 is the products clause of the inventory item I3.43 (assumed at L); `ReachPure` is a theorem of the
round, not a premise. The availability of the operations ((A)/H-OI_g) is not a premise of any statement of the round
and is not decided by it.

## The ROADMAP wording the round would license (row K2; not applied by the round)

At L, ROADMAP :1001–1003 reads: "**K2 — the composite. OPEN.** Read-only research has mapped a candidate `d = 3`
composition route, but no governed round records the classification or the cone theorem." Under `K2-SCHEMA-1-READ` with
all six cells positive the second sentence may be replaced by: "A governed round records the pair-level cone theorem
conditionally (`pairCone_eq_Q3_of_drive_exact`): products, invariance under the gate and under one copy's rotations
about the third axis and its cyclic permutation, and self-duality under the table pairing give the two-qubit positive
cone through the Pauli dictionary, and conversely that cone has the gate and rotation invariance
(`pairCone_eq_Q3_iff_drive_exact`); the gate invariance and self-duality are introduced hypotheses, not OI premises,
and the rotation invariance of the cone is the open bridge; no governed round records the classification." The
obligations sentence ("… all are open") stands: every hypothesis of the theorem is unsourced. K2 stays OPEN under every outcome.

## The controls (in `controls.py`)

- **S1 surface**: preamble, every declaration in order and by kind, every theorem's signature, every definition whole
  (`pauli`, `tokMat`, `dict`, `dictLin`, `ipW`, `coordOf`, `dictEquiv`, `dualW`, `Q3`, `actTLin`, `driveGens`,
  `driveWords`, `ReachPure`; §G's `phaseMat`, `cycMat`, `cycMatH`; §H's `P0`, `P1`, `blockMat`, `blockAct`, `IsSU`,
  `BlockInvariant`; §H.6's `ConjInv`, `dUnit`, `rotRe`, `Xm`, `driveOrbit`), 54 prints (22, §G's nine, §H's eleven,
  §H.6's twelve). Mutations, each failing with its code: the two sides of `pairCone_eq_Q3_iff_drive_exact` exchanged
  with `hH2` and `hA` added as hypotheses (the equivalence turned into an implication); `hA` weakened to the finite
  clause (`t = Real.pi / 2` only) in `pairCone_eq_Q3_of_drive_exact` (the frozen statement check fails; the
  countercontrol shows the weakened statement false given Theorem S′); `hH2` dropped from `blockInvariant_of_drive`
  (the frozen statement check fails; without the gate the clause's operations generate only the diagonal subgroup,
  which fixes `|det Ψ|`, `e19b_block_controls` B5); a hypothesis added to `reachPure`; `hH3` weakened to
  `K ⊆ dualW K`; the factor `1/4` of `dict` replaced by `1/2`; `0 ≤ c` dropped from `ReachPure`; a fifty-fifth print.
- **S2 resolution**: `W`, `HVec`, `hom`, `prodState`, `tens`, `actT`, `cnot`, `tensorOf`, `eball`, `rotLin`,
  `cycEquiv`, `psdFactorization_discharged` resolve to the landed declarations at `D`. Mutation: a local `cnot`.
- **S3 positive control and hypothesis load-bearing**: positive — `Q3` meets H1 (P1), H2 and A_miss (D1: each generator
  is a unitary conjugation; in the kernel layer `Q3_cnot` and §G's `Q3_aMiss`, the necessity direction), H3
  (`Q3_selfDual`) and BlockInvariant (`Q3_blockInvariant`); H2 load-bearing — the partial transpose `actT reflY (Q3)`
  meets H1, H3 and A_miss (written: `actT reflY` is an involutive signed permutation of the table coordinates that
  carries products of ball states to products of ball states, and `reflY R reflY` is a rotation for every rotation
  `R`), and it is not `cnot`-invariant: it contains `idW = actT reflY phiW` (K2Guard.lean:106; `phiW`, the table of a
  Bell state, lies in `Q3`), while `cnot idW = chainW`
  (:110) takes the value `−1/2` on a product of effects (:134) and so lies outside `maxCone (eball 3)`, which contains
  `actT reflY (Q3)` (written); H3 load-bearing — the half-space `{ω | 0 ≤ ω 0 0}` meets H1, H2 and A_miss
  and is not `Q3` (written; `e19b_block_controls` B2 exact); H1 load-bearing — `−Q3` meets H2, H3 and A_miss and
  contains no product (written; B1 exact); the continuous part of A_miss load-bearing — **the countercontrol family**:

  | cone | invariant under | H3 | differs from `Q3`; moved by | label |
  |---|---|---|---|---|
  | `K*` = `K384` (HO-24) | `G₃₈₄ = ⟨cnot, 1 ⊗ S, 1 ⊗ U_J⟩` (the finite clause) | `theorem_Sprime_ineq` [D], every hypothesis checked exactly (`e19_s6_controls` K1, `c = 401/400`) | Q-EXACT X1–X6, XC1–XC3; `1 ⊗ diag(1, (3+4i)/5)` (E15 X6, `e19b` B3) | CONJECTURE [D] + [X] |
  | `K768` (HO-31 item 2) | `G₇₆₈ = ⟨G₃₈₄, actC nflip⟩` | the same, K2 (`c = 10001/10000`) | K7: `R h*` overlaps `≤ 1949/2048 < 10000/10001`, pairing `−8/625` | CONJECTURE [D] + [X] |
  | `KC` (HO-31 item 2) | the two-qubit Clifford group `C₂` (11520) | the same, K3 (`c = 100001/100000`) | HO-32 item 3 (non-Clifford rotations) | CONJECTURE [D] + [X] |
  | `Kk` (HO-32) | G16 with κ's gate flow and the drive flow without `J` | Theorem S′ for compact defect sets [W] | HO-32 item 4 | at HO-32's label |

  Each cone refutes only the bridge candidate HO-32 item 4 names (every finite Clifford clause; the drive flow without
  its cyclic permutation) and is no countermodel to OI's quantum conclusion; each fails exactly at the closure
  identification (iii): its group is finite (or lacks `J`), equal to its own closure, and contains no infinite-order
  rotation of the full clause (`e19b` B7). The defeated alternatives at their labels: "the transfer clause for the
  stated access" and "a finite group" (HO-34 item 4, FAILED, the second CONDITIONAL on claim (D)), "a group of
  identity-component dimension at most one" (HO-35 item 3, FAILED, CONDITIONAL on claim (D)), "a finite stage" of the
  tower (HO-36 item 2, FAILED). `ReachPure` on the finite side — X7: for the finite clause's group the reachability
  statement fails; for the round's drive words it is the theorem `reachPure`.
- **S4 phrases** (module header, result note): "OI supplies", "derived from OI", "K2 is discharged", "the composite
  is forced", "two rotations suffice" (for the kernel layer), "ReachPure is proved", "self-dual" for the countercontrol
  without "written", "kernel proof of" (for the probe), "design module", "not for merge".
- **P, W**: the probe at S1 and `E` is the frozen blob; the workflow is `D`'s with the frozen edit — a shard
  `probes_k2schema1` installing `sympy==1.14.0` and running the probe, and the aggregate `Numerical probes` job's
  four-place edit (as KT4-PREM-1); `controls.py` checks the workflow at `E` is `D`'s with exactly that edit.
- **V**: each cell one token by its rule; the note contains exactly the six computed tokens; the earned reading
  exactly when all six are positive; the non-inference rule under every outcome. Self-test mutations: a broken
  signature of `dict_coordOf` fails only Q-CONE; a broken signature of `pairCone_eq_Q3_of_drive_exact` fails only
  Q-SUFF; a broken signature of `reachPure` fails only Q-GEN; a broken signature of `Q3_cnot` fails only Q-NEC; a broken
  signature of `Q3_blockInvariant` fails only Q-BLOCK; a probe with one witness value changed (for example
  `c* = 301/300`) fails only Q-EXACT.
- **I, C, R, G** as in KTRANS-DENSE-1 (one import line; one family; record directory exactly three files; `delta(D, E)`
  exactly the record paths and the five execution paths).

## Invariants and their checkpoints (§A.41)

| invariant | checkpoint |
| --- | --- |
| execution begins from the frozen control plane | `C1`: this file's blob at `F` |
| the module's text was built before `F` | `C0`: a design run of the module text, green at the Mathlib bridge build with all 22 prints standard, recorded in this file before `F` — **measured: run 38101580750 (job 114358419270), met**; the predicted tree's run at `D` remains with every draft's unmeasured items |
| the controls and the probe are the frozen ones | `C2`: blobs of `controls.py` and the probe at stage 1 and at `E`; `controls.py --self-test` OK at `E` |
| every frozen declaration elaborates within the three axioms | `C3`: the dispatch run at exactly `E`, every job `success`; the Mathlib bridge build and the 54 prints, none with `sorryAx` |
| the exact layer replays and renders | `C3`: shard `probes_k2schema1` green with `VERDICT E15-S6-EXACT-LAYER-CONSISTENT`; the aggregate job green |
| `hA` is the full-flow form and `ReachPure` the frozen definition | `C5`: `controls.py check E --freeze F` (S1 surface, with the mutation "`hA` weakened to the finite clause") |
| §G was built before `F` | `C0′`: a design run of §G (a design module importing the built `EqvK2Schema`), green at the Mathlib bridge build with §G's nine prints standard, recorded in this file before `F` — **measured: run 38112803530 (job 114391691368), met** |
| §H was built before `F` | `C0″`: a design run of §H, green at the Mathlib bridge build with §H's eleven prints standard — **measured: run 38132266383 (job 114448854872), met** (its first text failed in run 38124464622, job 114425828153; kept as `lean/EqvK2Block.run38124464622.lean`) |
| §H.6 was built before `F` | `C0‴`: a design run of §H.6, green at the Mathlib bridge build with §H.6's twelve prints standard — **measured: run 38134245361 (job 114454742595), met** |
| the equivalences' two directions are witnessed by different declarations | `C5` (S1 surface: `pairCone_eq_Q3_iff_drive_exact`'s `→` cites `Q3_cnot` and `Q3_aMiss`, its `←` cites `pairCone_eq_Q3_of_drive_exact`; `pairCone_eq_Q3_iff_block`'s `→` cites `Q3_blockInvariant`, its `←` cites `pairCone_eq_Q3_of_block`) |
| no reachability hypothesis enters the sufficiency direction | `C5` (S1 surface: `pairCone_eq_Q3_of_drive_exact` has exactly `hH1`, `hH2`, `hH3`, `hA`; `reachPure` has no hypothesis) |
| the module is registered; no manuscript changes | `C4`: the release gate at `E` passing every step |
| the statements, the workflow edit and the note are the frozen ones | `C5`: `controls.py check E --freeze F` |
| the change stays inside the governed paths | `C6`: `git diff --no-renames --name-status D E`; `C5` (G) |
| the native receipts hold; the legacy records are untouched | `C7`: `v3_verifier --verify-round Q`; `legacy_records_check.py` at every stage commit and at `Q` |

## Design evidence and the predicted outputs

| run | commit | workflow run | measured |
|---|---|---|---|
| 1 | `472835c5` (`dev-equivalence/k2-schema`, based on L; module `EqvK2Schema`, blob `3edcf9b0`) | 38099025197 | Mathlib bridge job 114350890660: **build failed** at four proofs (`dict_tens` 105:87, `dict_smul` 122:67, `trace_dict_mul` 167:64, `dict_coordOf` 235:2), one rewriting-order defect of the one-list `simp only` rendering; prints standard for 10 of 22, `sorryAx` for the 12 that are or use those four; no statement failed |
| 2 | `aabc649e` (proof-only repair: four `simp only` lists gain `Matrix.add_apply` or `Matrix.trace_add`; blob `659ae36c`) | 38101580750 | Mathlib bridge job 114358419270: `Build completed successfully (3644 jobs)`; **all 22 prints** (`EqvK2Schema.lean:453–474`) `[propext, Classical.choice, Quot.sound]`; warnings only (unused `simp` arguments); release gate every step PASS except `lean-manuscript` (1 problem: the unregistered module), `lean-axioms` 5882, no sorry, 303 legacy records intact, 43 receipts hold |
| 3 (§G) | `2d978412` (`dev-equivalence/r4-design`, based on L; `EqvK2Schema` unchanged, `EqvK2Converse` blob `4add9b8d`, with another design module) | 38112020014 | Mathlib bridge job 114389373318: Build failed at the other module (`EqvTransport`); `EqvK2Converse` built with warnings only, 9/9 prints standard |
| 4 (§G) | `20c207f1` (same branch; `EqvK2Converse` byte-identical) | 38112803530 | Mathlib bridge job 114391691368: `Build completed successfully (3647 jobs)`; §G's nine prints (EqvK2Converse.lean:226–234) and the 22 standard; release gate PASS except `lean-manuscript` (4 problems: the four unregistered design modules), `lean-axioms` 5907, no sorry, 303 legacy records intact, 43 receipts hold |
| exact (round 2) | `research/equivalence` | `e10_k2_schema` run 2 (replayed by the coordinator) | 9 checks, 0 failures, `VERDICT K2-SCHEMA-SKELETON-CONSISTENT` |
| exact (round 3) | `research/equivalence` | `e11_k2_dict` run 2 (replayed by the coordinator) | 18 checks, 0 failures, `VERDICT E11-DICT-STATEMENTS-EXACT` |
| exact (the probe to freeze) | `research/equivalence` | `e15_k2s6_probe` run 1 (local, `python3 -I -B`; replay byte-identical; py `78cd7c59…`, out `3ee625fe…`) | 12 checks, 0 failures; `COUNTER XC1/XC2/XC3 fails as stated`; `VERDICT E15-S6-EXACT-LAYER-CONSISTENT` |
| 5 (§H, §H.6's first) | `7dd71a7e` (`dev-equivalence/r5-design`, based on L; `EqvK2Schema`, `EqvK2Converse` unchanged; `EqvK2Block` blob `d339c6c5`; the research module `EqvOneDictionary`; the bridge thread's `BridgeDictionary`, `BridgeConverge` carried verbatim) | 38124464622 | Mathlib bridge job 114425828153: Build failed in `EqvK2Block` (a rewrite order; `unitary.star_mem` renamed `Unitary.star_mem` at the pin; `simp` normal forms of rank-one literals and of real half-angle cosines; `ring` inside `first` falling back to `ring_nf`); 5 of its 11 prints standard; no statement failed |
| 6 (§H) | `f67da967` (proof-only repair; `EqvK2Block` blob `23d0db23`) | 38132266383 | Mathlib bridge job 114448854872: Build success; §H's eleven prints and every other print standard; release gate red only at `lean-manuscript` (6 unregistered design modules), `lean-axioms` 5949, no sorry, 303 legacy records intact, 43 receipts hold |
| 7 (§H.6) | `f0c36cf9` (adds `EqvK2Generation`, blob `682f187e`) | 38134245361 | Mathlib bridge job 114454742595: `Build completed successfully (3650 jobs)`; §H.6's twelve prints and every other print standard; release gate red only at `lean-manuscript` (7 unregistered design modules), `lean-axioms` 5961, no sorry, 303 legacy records intact, 43 receipts hold |
| exact (round 5) | `research/equivalence` | `e19_s6_controls` run 2; `e19b_block_controls` run 3 (local; replays byte-identical) | 8/8 `VERDICT E19-S6-CONTROLS-EXACT`; 7/7 `VERDICT E19B-BLOCK-CONTROLS-EXACT` (the countercontrol family's hypotheses of `theorem_Sprime_ineq`, the determinant-ratio invariant, the Euler and two-reflection words, the load-bearing witnesses) |

**Predicted outputs, generated from those measurements by the rules:** Q-CONE `K2-SCHEMA-CONE-STEP-PROVED` (run 2: the
six named declarations and their dependants built with standard prints; in run 1 four of them printed `sorryAx`).
Q-SUFF `K2-SCHEMA-SUFFICIENCY-PROVED` (run 38134245361: `pairCone_eq_Q3_of_drive_exact` standard). Q-GEN
`K2-SCHEMA-GENERATION-PROVED` (run 38134245361: `blockInvariant_of_drive` and `reachPure` standard). Q-NEC
`K2-SCHEMA-NECESSITY-PROVED` (run 38134245361: `Q3_cnot` and `pairCone_eq_Q3_iff_drive_exact` standard; `Q3_aMiss`
standard there and in run 38112803530). Q-BLOCK `K2-SCHEMA-BLOCK-FORM-PROVED` (runs 38132266383 and 38134245361:
`pairCone_eq_Q3_of_block`, `Q3_blockInvariant`, `pairCone_eq_Q3_iff_block` standard).
Q-EXACT `K2-SCHEMA-INSTANCES-EXACT` (the run of `e15_k2s6_probe`: `checks: 12, failures: 0`, the three countercontrols
failing as stated, the verdict token), the frozen probe being that blob with its two path lines changed (checkpoint
`C2`). The rules, not this reading, are what a frozen file would fix; the predicted execution tree at `D` is not yet
measured.

**Convergence remark (not part of the frozen surface).** The bridge thread's design module `BridgeDictionary` (handoff
HO-21) proves, on the same definitions, the gate's matrix form `dict (cnot ω) = cnotMat * dict ω * cnotMat`, the
monomial images and `rotZ (cos t) (sin t) = rotLin t`, which this module does not state (its exact layer checks those
conjugations instead, D1). A converged dictionary module would be a separate round's surface.

## Stages and outcomes

Stages as KT4-PREM-1 (C1 `controls.py`; S1 the module, probe, workflow edit, import line and family in one commit; proof
repairs only; S2 the result note = candidate `E`), preceded by `C0` (met in design run 38101580750), `C0′` (met in
design run 38112803530), `C0″` (met in design run 38132266383) and `C0‴` (met in design run 38134245361).
**`K2-SCHEMA-1-READ`**: `controls.py check E --freeze F` OK, six tokens printed, the exact-head run at `E` green on
every job. **`K2-SCHEMA-1-HALTED`**: anything else (`S12`). No outcome sources a premise, discharges K2, or edits the
ROADMAP or a manuscript; correctness bands unchanged (consistency axis).
