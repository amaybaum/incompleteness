# Substratum round WT2-1 — is `WT1_transfer` unitarily implemented on general pairs?: PREREGISTRATION (draft for owner review)

**Status: candidate control plane, native V3 draft for owner review. Not an F candidate.** Drafted on a pull request
from `D`. It is built from 24.1A's records at `D` (`programmes/substratum/lemma-24-1a-word-trace-sufficiency/`,
`OIBridge/WordTraceSufficiency.lean`); a grep of every `origin/research/*` head for `WT2`, `Specht`, `Wiegmann`,
`Pearcy`, `hiddenConjugate` finds only copies of landed records, guard sources and logs. No design module, probe or
`controls.py` exists for it yet; the statement surface below is proposed and is fixed only by design runs before `F`.
Nothing is executed. Only the owner designates `F` under AGENTS §A.39; an instruction to proceed is not a designation.

```v3-round
round WT2-1
kind non-sealing
record-directory verification/programmes/substratum/round-wt2-1-general-unitary-implementation/
```

```v3-governed-paths
record AM verification/programmes/substratum/round-wt2-1-general-unitary-implementation/
record AM verification/receipts/WT2-1.json
execution A verification/lean-mathlib/OIBridge/WordTraceGeneral.lean
execution A verification/lean/wt2_1_probe.py
execution M verification/lean-mathlib/OIBridge.lean
execution M verification/lean-manuscript-census.json
execution M .github/workflows/verify.yml
```

D: dee3b5ae6fd3fb20fa1bad3337963e5af947f3a4. Delta(D, F) is this preregistration and any amendments in the round's
`amendments/` directory; **no manuscript, built artifact, `verification/ROADMAP.md`, landed kernel module or other
round's record changes under any outcome.**

## What the round is

24.1A froze `WT2` as "For `U, U'` on the same carrier with `Uᴴ U = 1`, `U'ᴴ U' = 1` and `WordTracesEqual U U'`,
`HiddenConjugate U U'`." (its preregistration.md:324–325) and recorded "**UNDECIDED, and the obstruction is named
among the freeze's (a)–(f).**" (result.md:174), naming "(b) together with (e)" (:176–179); ROADMAP.md:701 states it as
"the spatial structure theory of `*`-subalgebras of `M_m(ℂ)`". `WT1_transfer` (WordTraceSufficiency.lean:420) gives,
under `WordTracesEqual U U'` (:98) alone, an injective, unital, multiplicative, `*`- and trace-preserving linear
`φ : wordSpan U → M_m(ℂ)` (:94), `w(U) ↦ w(U')`; `WT2gen_hiddenConjugate` (:599) gives `HiddenConjugate`
(SemigroupTransfer.lean:106) only on the spanning class (`BlockSpanning` WordTraceSufficiency.lean:102), via
`exists_unitary_of_starMul` (WordTraceSufficiency.lean:459).

- **Q-CORE (kernel).** Is every trace-preserving, multiplicative, `*`-preserving linear map from a unital `*`-closed
  subspace of `M_m(ℂ)` into `M_m(ℂ)` conjugation by a unitary?
- **Q-GEN (kernel).** With no spanning or unitarity hypothesis, does `WordTracesEqual U U'` give `HiddenConjugate U U'`?
  `wordEval` (SemigroupTransfer.lean:112) takes all words in blocks and adjoints: Specht–Wiegmann–Pearcy (external).
- **Q-IFF (kernel).** Is `HiddenConjugate U U' ↔ WordTracesEqual U U'` on all pairs, one witness per direction?
- **Q-EXACT (exact layer).** Off the spanning class, do spans, conjugations and multiplicities behave as the general
  statement requires, and is trace preservation load-bearing?

**Placement.** A sibling of `lemma-24-1a-word-trace-sufficiency/`, a closed namespace of `legacy-records.json` where
`tools/legacy_records_check.py:118` refuses added files, in the native `round-<id>-<slug>/` form (§A.36). 24.1B (:23–26)
and 24.1C (:637–640), frozen and never executed, put `WT2` outside their scope; 24.1C's `SC6` (:538) leaves it unchosen.

## The proposed statement surface

Module `OIBridge/WordTraceGeneral.lean` (name: owner's choice), importing `OIBridge.WordTraceSufficiency`, namespace
`OIBridge.WordTraceGeneral`, section variables as WordTraceSufficiency.lean:84.

```lean
theorem exists_unitary_of_traceStarMul (A : Submodule ℂ (Matrix H H ℂ)) (h1 : (1 : Matrix H H ℂ) ∈ A)
    (hmulA : ∀ x y, x ∈ A → y ∈ A → x * y ∈ A) (hstarA : ∀ x, x ∈ A → xᴴ ∈ A) (φ : A →ₗ[ℂ] Matrix H H ℂ)
    (hmul : ∀ (x y : Matrix H H ℂ) (hx : x ∈ A) (hy : y ∈ A) (hxy : x * y ∈ A),
      φ ⟨x * y, hxy⟩ = φ ⟨x, hx⟩ * φ ⟨y, hy⟩)
    (hstar : ∀ (x : Matrix H H ℂ) (hx : x ∈ A) (hx' : xᴴ ∈ A), φ ⟨xᴴ, hx'⟩ = (φ ⟨x, hx⟩)ᴴ)
    (htr : ∀ x : A, trace (φ x) = trace (x : Matrix H H ℂ)) :
    ∃ W : Matrix H H ℂ, Wᴴ * W = 1 ∧ ∀ (x : Matrix H H ℂ) (hx : x ∈ A), φ ⟨x, hx⟩ = W * x * Wᴴ
theorem WT2_hiddenConjugate (U U' : Matrix (V × H) (V × H) ℂ) (h : WordTracesEqual U U') : HiddenConjugate U U'
theorem hiddenConjugate_iff_wordTracesEqual (U U' : Matrix (V × H) (V × H) ℂ) :
    HiddenConjugate U U' ↔ WordTracesEqual U U'
theorem WT2_countermodel : ∃ (a b : ℕ) (U U' : Matrix (Fin a × Fin b) (Fin a × Fin b) ℂ),
    WordTracesEqual U U' ∧ ¬ HiddenConjugate U U'
```

The countermodel surface is admissible only in place of the other three. In WordTraceSufficiency.lean the core mirrors
`WT1_transfer`'s conjuncts (:427–431) at `A = wordSpan U` (closure :143, :164, :175); injectivity follows as in
`transferMap_injective` (:403), unitality from `htr`; blocks pass to `U` as in `WT2gen_oneSided` (:562), by
`visibleBlock_conj` (SemigroupTransfer.lean:371) at `σ = 1`. Witnesses (§A.34), as in `WT3_spanning_iff` (:624): (→)
`trace_wordEval_hiddenConjugate` (SemigroupTransfer.lean:468); (←) `WT2_hiddenConjugate`. Helpers and a budget (two
`def`s, no witness a `def`) are fixed by design; one `#print axioms` line per named result. Census family "word-trace
sufficiency on general pairs (round WT2-1, substratum)", `modules: ["WordTraceGeneral"]`, `status: "kernel-only"`,
`manuscript: []`; import line after `import OIBridge.EqvK2MaxCone` (OIBridge.lean:268).

**Mathlib at the pin** (tag `v4.33.0`, commit `db584cd6`) carries abstract Wedderburn–Artin (`RingTheory/SimpleModule/
IsAlgClosed.lean:33`), the algebraic double centralizer for semisimple modules (`jacobson_density`, `RingTheory/
SimpleModule/Basic.lean:568`; `Module.Finite.toModuleEnd_moduleEnd_surjective` :581), `orthogonal_mem_invtSubmodule`
(`Analysis/InnerProductSpace/Adjoint.lean:486`) and `cfc_mem_elemental` (`Analysis/CStarAlgebra/
ContinuousFunctionalCalculus/Range.lean:89`); a bounded grep finds no Specht, Wiegmann, Pearcy or Skolem–Noether
statement and no semisimplicity of `*`-closed subalgebras. 24.1A's freeze records no Jacobson-density statement "for
matrix algebras" (:168–170); the module-level one is an algebraic form of its piece (f)'s double commutant, given (a).

## The exact layer (proposed probe `verification/lean/wt2_1_probe.py`)

Standard library, exact arithmetic, `python3 -I`, shard `probes_wt21`; `𝒲(U)` is grown from `1` until closed under
left multiplication by every letter, which determines it exactly. Output `checks: 5, failures: 0` and
`VERDICT WT2-INSTANCES-EXACT`.

- **K0**: the nine matrix units of `M_3` have rank 9, `{1}` rank 1. **K1**: the Pair-C blocks (`pairC_blocks`,
  SemigroupTransfer.lean:603) span `M_3`, as 24.1A's analysis records (preregistration.md:172–177).
- **X1**: `U_R`, the permutation matrix of `(v, h) ↦ (1 − v, h)` for `h ∈ {0, 1}`, fixing `(v, 2)`, on `Fin 2 × Fin 3`,
  and `U_R' = (1 ⊗ P₍₀ ₂₎) U_R (1 ⊗ P₍₀ ₂₎)ᴴ ≠ U_R` have word spans of dimension 2 < 9: not spanning.
- **X2**: `U_S`, the same with the swap only at `h = 0`: `U_R,vw ↦ U_S,vw` extends to a unital `*`-isomorphism of the
  two-dimensional word spans (checked on a basis), while `Tr U_R,01 = 2 ≠ 1 = Tr U_S,01`.
- **X3**: `U_T = enlarge U_C 1₂` (SemigroupTransfer.lean:117): `dim 𝒲(U_T) = 9 < 36`; with `e_{ij} = E_{ij} ⊗ 1₂`,
  `Tr e₀₀ = 2`; a unit `ξ` with `e₀₀ ξ = ξ` gives three orthonormal `e_{j0} ξ`, two orthonormal such `ξ_r` a basis.

## The decision rules (implemented by `controls.py verdict`)

| Cell | Token | Rule |
|---|---|---|
| Q-CORE | `WT2-1-CORE-PROVED`; else `WT2-1-CORE-UNDECIDED` | the statements are exactly the frozen ones (S1), resolve to the landed objects (S2), and the exact-head run at `E` builds the module with the core's print within `[propext, Classical.choice, Quot.sound]` |
| Q-GEN | `WT2-1-GENERAL-PROVED` | the positive surface is present; `WT2_hiddenConjugate` has exactly the frozen signature and its print is within the three axioms at `E` |
| Q-GEN | `WT2-1-GENERAL-COUNTERMODEL` | the countermodel surface is present in place of the positive one; `WT2_countermodel` has exactly the frozen signature and its print is within the three axioms at `E` |
| Q-GEN | `WT2-1-GENERAL-UNDECIDED` | neither surface is present and building at `E` |
| Q-IFF | `WT2-1-IFF-PROVED`; else `WT2-1-IFF-NOT-ESTABLISHED` | the iff has the frozen signature, its print is within the three axioms, and its proof term names the two witnesses, one per direction (S3) |
| Q-EXACT | `WT2-1-INSTANCES-EXACT`; else `WT2-1-INSTANCES-NOT-ESTABLISHED` | the probe blob at `E`, run by `controls.py` with `python3 -I`, prints `PASS` for K0, K1, X1, X2, X3, no `FAIL`, `checks: 5, failures: 0` and the verdict line |

No rule reads another cell's outcome. Tokens are printed by `controls.py verdict E` from the measurements at `E`. Both
surfaces present fails S1; a verdict over a failed control is void and the round halts.

## The earned reading and the non-inference rule

> Earned reading (only when Q-CORE, Q-GEN and Q-IFF are positive and Q-EXACT is exact): on every finite carrier
> V × H, equality of all block-word traces is necessary and sufficient for hidden conjugation of two matrices, with no
> spanning and no unitarity hypothesis; every trace-preserving, multiplicative, *-preserving linear map of a unital
> *-closed subspace of M_m(ℂ) into M_m(ℂ) is conjugation by a unitary.

> Countermodel reading: the statement renders a classical theorem over ℂ, so a kernel countermodel is read as the
> statement or a landed definition (wordEval, WordTracesEqual, HiddenConjugate) not rendering the classical question,
> named in the result note for owner review; no failure of word-trace sufficiency, label move or ROADMAP wording
> follows. Undecided reading: WT2 stays at 24.1A's strength, the stopping piece named ((a)–(f), :248–255, or another).

> Non-inference rule: under no outcome does the round show that the reconstruction framework supplies the block-word
> trace data (24.1B's question) or decide how BlockSpanning and HiddenCommutantTrivial stand to each other (24.1C's).
> Nothing about completeness of 𝒢_sub, generators (ii) and (iv) or the physical wave rule follows. Lemma 24.1 is not
> repaired, the generators are neither called complete nor called incomplete, the manuscripts' route is not restored,
> the P1 label stays OPEN, and the probe is an exact computation, not a kernel proof.

**Premises this round does not source:** the word-trace data (`WordTracesEqual U U'` is a hypothesis; whether the
framework fixes it is 24.1B's question); any spanning, commutant or unitarity property of substratum dilation data.

## The ROADMAP wording the round would license (P1 row :64, section :686–706; not applied by the round)

With Q-CORE, Q-GEN and Q-IFF positive, the row's "sufficiency on general pairs UNDECIDED at the unitary-implementation
step" may become "WT2-1: necessary and sufficient on every pair (`hiddenConjugate_iff_wordTracesEqual`)", and the
section may gain a paragraph after 24.1A's, which stays (`R7-WTS` pins it, edge_rigidity_probe.py:10164–10199). The
row stays `OPEN` under every outcome; under any other outcome no wording is licensed.

## The controls (in `controls.py`)

- **S1 surface**: preamble, frozen declaration list, one print per named result, exactly one surface. Mutations, each
  failing with its code: `BlockSpanning U` or `Uᴴ * U = 1` added to `WT2_hiddenConjugate`; `htr` dropped; the core's
  conclusion weakened to an intertwiner; `WT2_countermodel` beside `WT2_hiddenConjugate`; a print removed; a `sorry`.
- **S2 resolution**: every landed object cited above resolves to its declaration at `D`; SemigroupTransfer.lean (blob
  `5ee55b5c`) and WordTraceSufficiency.lean (blob `ea8e9692`) are unchanged at `E`.
- **S3 load-bearing**: (i) the iff names `trace_wordEval_hiddenConjugate` forward and `WT2_hiddenConjugate` backward
  (a forward term not naming it fails S3 alone); (ii) `WT2_hiddenConjugate` names `WT1_transfer` and the core;
  (iii) X2, X3 as countercontrols; (iv) `R7-WTS` green at `E` (edge_rigidity_probe.py:10125–10136 reads only
  WordTraceSufficiency.lean). **V**: four tokens, each reading exactly when its tokens hold. **G**: `D → E` governed.
- **S4 phrases**: "Lemma 24.1 is repaired", "completeness holds", "completeness fails", "the generators are complete",
  "the generators are incomplete", "the manuscripts' route is restored", "the framework supplies", "24.1B is
  answered", "the classes coincide", "word-trace sufficiency fails", "kernel proof of" (for the probe), "design module".

## Invariants and their checkpoints (§A.41)

| invariant | checkpoint |
| --- | --- |
| execution begins from the frozen control plane; controls and probe are the frozen ones | `C1`: this file's blob at `F`; `C2`: blobs at stage 1 and at `E`, `controls.py --self-test` OK at `E` |
| every frozen declaration elaborates within the three axioms; exactly one surface; the iff's two witnesses | `C3`: the dispatch run at exactly `E`, every job `success`, bridge build and prints; `C5`: S1, S3(i) in `controls.py check E --freeze F` |
| landed modules untouched; `R7-WTS` green; the exact layer replays | `C5` (S2 blobs); `C3`: the guard step and shard `probes_wt21` with the verdict line at `E` |
| the module is registered; the change stays inside the governed paths (no manuscript, ROADMAP or README) | `C4`: the release gate at `E` passing every step; `C6`: `git diff --no-renames --name-status D E`; `C5` (G) |
| the native receipts hold; legacy records untouched | `C7`: `v3_verifier --verify-round Q`; `legacy_records_check.py` at every stage commit and `Q` |

## Design work required before F

1. No design module exists at `D`. Build one on a disposable branch from `D`, choose a route, record the runs. Neither
   is built: (A) induction on the rank of an `A`-invariant projection pair `(P, P')` with `tr (P a) = tr (P' φ a)`: a
   projection `q` of least nonzero trace in `PA` has `qAq = ℂq`; with its image under `Pa ↦ P'φ(a)` (well defined by
   the trace form) it gives vectors `x ξₛ`, `φ(x) ηₛ` with equal Gram data, hence a partial isometry intertwiner;
   complements are invariant as `A` is `*`-closed; recurse. (B) 24.1A's route (:230–258) with `jacobson_density`.
2. Fix S1 (declarations, helpers, budget; `Submodule` or `StarSubalgebra`) and check that `cfc_mem_elemental`,
   `orthogonal_mem_invtSubmodule` (via `Matrix.toEuclideanCLM`) and `jacobson_density` apply to `Matrix H H ℂ`.
3. Write the probe and `controls.py`; replay the probe three times; add the shard, the aggregate `needs` and result
   check, the family and the import line; dispatch the predicted execution tree at `D` and record the run.
4. Owner choices: under `WT2-1-GENERAL-UNDECIDED`, whether an intermediate surface (for instance semisimplicity of
   `ℂ^m` over a `*`-closed `A`) is frozen to land, or nothing lands; the module name and the directory slug.

## Stages and outcomes

Stages: C1 `controls.py`; S1 module, probe, workflow edit, import line, family; proof repairs only; S2 the result note
= candidate `E`. **`WT2-1-READ`**: `controls.py check E --freeze F` OK, four tokens printed, the exact-head run at `E`
green on every job. **`WT2-1-HALTED`**: otherwise (`S12`). No outcome moves the P1 label or edits the ROADMAP, the
README, a manuscript or a landed module; correctness bands unchanged (consistency axis).
