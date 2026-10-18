# Substratum round WT2-1 — is `WT1_transfer` unitarily implemented on general pairs?: PREREGISTRATION (draft for owner review)

**Status: candidate control plane, native V3 draft for owner review. Not an F candidate.** Drafted on a pull request
from `D`, revised under the owner's decision on PR #828 (comment 6254706890: route (A), induction on minimal
projections). It is built from 24.1A's records (`programmes/substratum/lemma-24-1a-word-trace-sufficiency/`,
`OIBridge/WordTraceSufficiency.lean`); a grep of every `origin/research/*` head for `WT2`, `Specht`, `Wiegmann`,
`Pearcy`, `hiddenConjugate` finds only copies of landed records, guard sources and logs. No design module, probe or
`controls.py` exists for it yet; the statement surface below is proposed and is fixed exactly only by the
statement-surface design run before `F`. Nothing is executed. Only the owner designates `F` and `E` under AGENTS §A.39;
an instruction to proceed is not a designation.

```v3-round
round WT2-1
kind non-sealing
record-directory verification/programmes/substratum/round-wt2-1-general-unitary-implementation/
```

```v3-governed-paths
record AM verification/programmes/substratum/round-wt2-1-general-unitary-implementation/
record AM verification/receipts/WT2-1.json
execution A verification/lean-mathlib/OIBridge/WordTraceGeneral.lean
execution M verification/lean-mathlib/OIBridge.lean
execution M verification/lean-manuscript-census.json
```

D: dee3b5ae6fd3fb20fa1bad3337963e5af947f3a4. Delta(D, F) is this preregistration and any amendments in the round's
`amendments/` directory; **no manuscript, built artifact, workflow, `verification/ROADMAP.md`, landed kernel module or
other round's record changes under any outcome.** Every citation below is a coordinate at `main`
`501331f58e856019173d7246a8c4de7d4aec752d`. Of the files cited, `SemigroupTransfer.lean` (blob `5ee55b5c`),
`WordTraceSufficiency.lean` (blob `ea8e9692`), 24.1A/B/C's records and `tools/legacy_records_check.py` are identical at
`D` and at `main`; `ROADMAP.md` gained line 69 after `D`, so its lines cited below past :68 are one higher than at
`D`; `OIBridge.lean` and
`lean-manuscript-census.json` each gained one entry at their tails after `D` (below, "Reconciliation").

## What the round is

24.1A froze `WT2` as "For `U, U'` on the same carrier with `Uᴴ U = 1`, `U'ᴴ U' = 1` and `WordTracesEqual U U'`,
`HiddenConjugate U U'`." (its preregistration.md:324–325) and recorded "**UNDECIDED, and the obstruction is named
among the freeze's (a)–(f).**" (result.md:174), naming "(b) together with (e)" (:176–179); ROADMAP.md:702 states it as
"the spatial structure theory of `*`-subalgebras of `M_m(ℂ)`". `WT1_transfer` (WordTraceSufficiency.lean:420) gives,
under `WordTracesEqual U U'` (:98) alone, an injective, unital, multiplicative, `*`- and trace-preserving linear
`φ : wordSpan U → M_m(ℂ)` (:94), `w(U) ↦ w(U')`; `WT2gen_hiddenConjugate` (:599) gives `HiddenConjugate`
(SemigroupTransfer.lean:106) only on the spanning class (`BlockSpanning` WordTraceSufficiency.lean:102), via
`exists_unitary_of_starMul` (WordTraceSufficiency.lean:459).

- **Q-CORE (kernel).** Is every linear map `φ` from a unital `*`-subalgebra `A` of `M_m(ℂ)` into `M_m(ℂ)` that is
  multiplicative, `*`-preserving and trace-preserving on `A` conjugation by a unitary? The hypotheses are stated
  exactly in the next section.
- **Q-GEN (kernel).** With no spanning or unitarity hypothesis, does `WordTracesEqual U U'` give `HiddenConjugate U U'`?
  `wordEval` (SemigroupTransfer.lean:112) takes all words in blocks and adjoints; the classical statement is the
  simultaneous unitary similarity theorem of Specht–Wiegmann–Pearcy (external). Q-GEN drops both of 24.1A's
  unitarity hypotheses `Uᴴ U = 1`, `U'ᴴ U' = 1` and both spanning hypotheses of `WT2gen_hiddenConjugate`, so it is
  strictly stronger than the frozen `WT2` and than `WT2-gen`: its hypothesis is one of theirs, and X4 below exhibits
  pairs satisfying it that satisfy neither `WT2`'s nor `WT2-gen`'s hypotheses.
- **Q-IFF (kernel, assembly).** Is `HiddenConjugate U U' ↔ WordTracesEqual U U'` on all pairs, with one witness per
  direction (§A.34)? The forward direction is landed (`trace_wordEval_hiddenConjugate`); the iff's content beyond it
  is exactly Q-GEN's, so its token credits an assembly and no novel result.
- **Q-EXACT (exact layer).** Off the spanning class, do spans, conjugations and multiplicities behave as the general
  statement requires, and does each hypothesis of Q-CORE and Q-GEN that admits a countermodel have one?

**Placement.** A sibling of `lemma-24-1a-word-trace-sufficiency/`, a closed namespace of `legacy-records.json` where
`tools/legacy_records_check.py:118` refuses added files, in the native `round-<id>-<slug>/` form (§A.36). 24.1B (:23–26)
and 24.1C (:637–640), frozen and never executed, put `WT2` outside their scope; 24.1C's `SC6` (:529, :538) leaves it
unchosen.

## The algebraic hypotheses, exactly

The ambient algebra is `Matrix H H ℂ` (`M_m(ℂ)`, `m = card H`), with matrix multiplication, `star` = `conjTranspose`
and the unnormalised `Matrix.trace`; `H` carries `[Fintype H] [DecidableEq H]` as at WordTraceSufficiency.lean:84.

- **Domain.** `A : Submodule ℂ (Matrix H H ℂ)` with three separate closure hypotheses: `h1 : 1 ∈ A`,
  `hmulA : ∀ x y, x ∈ A → y ∈ A → x * y ∈ A`, `hstarA : ∀ x, x ∈ A → xᴴ ∈ A`. Together they say that `A` is a unital
  `*`-subalgebra of the ambient algebra. A `*`-closed linear subspace is not assumed to be closed under
  multiplication: `hmulA` is its own hypothesis, and N3 below shows the conclusion fails without it. `A` is a
  `Submodule`, not a `StarSubalgebra`, because `wordSpan U` is a `Submodule` (:94) and `WT1_transfer`'s map is a linear
  map on its subtype, so `A := wordSpan U` is an instance with no coercion.
- **Codomain.** The whole ambient algebra on the same index type `H`. Nothing is assumed of the image; that it is a
  unital `*`-subalgebra follows.
- **The map.** `φ : A →ₗ[ℂ] Matrix H H ℂ`; `hmul` (multiplicative on `A`), `hstar` (`*`-preserving on `A`) and `htr`
  (`trace (φ x) = trace x` on `A`), each in the membership-carrying form of `WT1_transfer`'s conjuncts (:427–431).
  Neither unitality nor injectivity of `φ` is assumed: `φ 1` is a self-adjoint idempotent of trace `m`, hence `1`;
  `trace (φ xᴴ φ x) = trace (xᴴ x)` gives injectivity.

**How the landed theorems consume them.** At `A = wordSpan U`, `h1`, `hmulA`, `hstarA` are `one_mem_wordSpan` (:143),
`mul_mem_wordSpan` (:164), `conjTranspose_mem_wordSpan` (:175), and `hmul`, `hstar`, `htr` are `WT1_transfer`'s fifth
to seventh conjuncts (:427–431), passed verbatim. `WT2gen_hiddenConjugate` (:599) reaches its unitary through
`exists_unitary_of_starMul` (:459), whose domain is all of `M_m(ℂ)` and whose third hypothesis is injectivity, not
trace preservation. The core replaces "domain all of `M_m(ℂ)`, injective" by "domain a unital `*`-subalgebra,
trace-preserving". Injectivity cannot do the work once `A` is proper: X2's map is injective, unital, multiplicative and
`*`-preserving on a two-dimensional `A`, and is not conjugation by a unitary.

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

The countermodel surface is admissible only in place of the other three. `WT2_hiddenConjugate` applies the core at
`A = wordSpan U` to `WT1_transfer`'s map; blocks pass to `U` as in `WT2gen_oneSided` (:562), by `visibleBlock_conj`
(SemigroupTransfer.lean:371) at `σ = 1`. Witnesses (§A.34), as in `WT3_spanning_iff` (:624): (→)
`trace_wordEval_hiddenConjugate` (SemigroupTransfer.lean:468); (←) `WT2_hiddenConjugate`. Helpers and a budget (two
`def`s, no witness a `def`) are fixed by the statement-surface design run; one `#print axioms` line per named result.
Census family "word-trace sufficiency on general pairs (round WT2-1, substratum)", `modules: ["WordTraceGeneral"]`,
`status: "kernel-only"`, `manuscript: []`; the import line follows the last import of `OIBridge.lean`.

**Mathlib at the pin** (tag `v4.33.0`, commit `db584cd6`) carries abstract Wedderburn–Artin (`RingTheory/SimpleModule/
IsAlgClosed.lean:33`), the algebraic double centralizer for semisimple modules (`jacobson_density`, `RingTheory/
SimpleModule/Basic.lean:568`; `Module.Finite.toModuleEnd_moduleEnd_surjective` :581), `orthogonal_mem_invtSubmodule`
(`Analysis/InnerProductSpace/Adjoint.lean:486`) and `cfc_mem_elemental` (`Analysis/CStarAlgebra/
ContinuousFunctionalCalculus/Range.lean:89`); a bounded grep finds no Specht, Wiegmann, Pearcy or Skolem–Noether
statement and no semisimplicity of `*`-closed subalgebras. 24.1A's freeze records no Jacobson-density statement "for
matrix algebras" (:168–170); the module-level one is an algebraic form of its piece (f)'s double commutant, given (a).

## The route, frozen: (A) induction on minimal projections

The round proves the core by route (A) and by no other route. For projections `P` commuting with `A` and `P'`
commuting with `φ(A)`, with `trace (P a) = trace (P' φ a)` for all `a ∈ A` (at the start `P = P' = 1`, which is `htr`),
it builds a partial isometry `W` with `Wᴴ W = P`, `W Wᴴ = P'` and `W a = φ(a) W` on `A`, by induction on `trace P`. The
pieces, frozen as the list the result note names its stopping point from:

- **(A1) invariant complements.** For an `A`-invariant subspace of `ℂ^H`, its orthogonal complement is `A`-invariant
  (`A` is `*`-closed), and its orthogonal projection commutes with `A`.
- **(A2) a minimal projection.** For `P ≠ 0`, a nonzero projection `q` of least trace in `P A` exists and satisfies
  `q A q = ℂ q` (spectral projections of a Hermitian element of `q A q` are polynomials in it, hence in `q A q`).
- **(A3) the compressed transfer.** `P a ↦ P' φ(a)` is well defined (by the trace form) and carries `q` to a
  projection `q'` with `trace q' = trace q`.
- **(A4) Gram data to a partial isometry.** For unit `ξ = q ξ`, `η = q' η`, the families `a ξ` and `φ(a) η` have equal
  Gram data, giving a partial isometry from `A ξ` onto `φ(A) η` that intertwines `A` and `φ`.
- **(A5) the induction.** `P₁ ≤ P` the projection onto `A ξ`, `P₁'` onto `φ(A) η`, the trace condition passing to
  `P − P₁`, `P' − P₁'`, `trace (P − P₁) < trace P`, and the assembly into a unitary at `P = P' = 1`.
- **(A6) the transfer.** Core and `WT1_transfer` give `HiddenConjugate U U'`.
- **other**, named in words.

**Route change.** If a piece of (A1)–(A5) cannot be completed without the decomposition of `A` into simple summands
(24.1A's route, its pieces (a)–(e) at preregistration.md:248–255), the result note reports that obstruction against
the piece, as an obstruction to route (A) within this budget. The round does not switch to route (B) (24.1A's route
:230–258 with `jacobson_density`); a route (B) attempt is a separately frozen round.

## The exact layer (proposed probe `wt2_1_probe.py` in the record directory)

Standard library, exact arithmetic (`fractions.Fraction`; every matrix below is rational), `python3 -I`, run by
`controls.py`; `𝒲(U)` is grown from `1` until closed under left multiplication by every letter, which determines it
exactly. Output `checks: 10, failures: 0` and `VERDICT WT2-INSTANCES-EXACT`. Each "not conjugation by a unitary" is
certified by an exact invariant of unitary conjugation (trace, `tr x²`, `tr xᴴx`, multiplicativity, `*`), never
numerically.

- **K0**: the nine matrix units of `M_3` have rank 9, `{1}` rank 1. **K1**: the Pair-C blocks (`pairC_blocks`,
  SemigroupTransfer.lean:603) span `M_3`, as 24.1A's analysis records (preregistration.md:172–177).
- **X1**: `U_R`, the permutation matrix of `(v, h) ↦ (1 − v, h)` for `h ∈ {0, 1}`, fixing `(v, 2)`, on `Fin 2 × Fin 3`,
  and `U_R' = (1 ⊗ P₍₀ ₂₎) U_R (1 ⊗ P₍₀ ₂₎)ᴴ ≠ U_R` have word spans of dimension 2 < 9: not spanning.
- **X2**: `U_S`, the same with the swap only at `h = 0`: `U_R,vw ↦ U_S,vw` extends to an injective unital
  `*`-isomorphism of the two-dimensional word spans (checked on every product of blocks), while
  `Tr U_R,01 = 2 ≠ 1 = Tr U_S,01`.
- **X3**: `U_T = enlarge U_C 1₂` (SemigroupTransfer.lean:117): `dim 𝒲(U_T) = 9 < 36`; with `e_{ij} = E_{ij} ⊗ 1₂`,
  `Tr e₀₀ = 2`; a unit `ξ` with `e₀₀ ξ = ξ` gives three orthonormal `e_{j0} ξ`, two orthonormal such `ξ_r` a basis.
- **X4**: `2 U_R` and `(1 ⊗ P₍₀ ₂₎)(2 U_R)(1 ⊗ P₍₀ ₂₎)ᴴ`: `(2U_R)ᴴ(2U_R) = 4 ≠ 1`, word span of dimension 2 < 9, and the
  word traces agree (necessity): a pair in Q-GEN's domain outside `WT2`'s and `WT2-gen`'s.
- **N1** (`hmul` dropped): `A = M_2`, `φ(x) = xᵀ`: linear, `*`-preserving, trace-preserving, unital;
  `φ(E₀₁E₁₀) = E₀₀ ≠ E₁₁ = φ(E₀₁)φ(E₁₀)`.
- **N2** (`hstar` dropped): `A = M_2`, `φ = Ad S`, `S = [[1,1],[0,1]]`: multiplicative, trace-preserving, unital;
  `φ(E₀₀) = [[1,−1],[0,0]]` is not Hermitian while `E₀₀` is.
- **N3** (`hmulA` dropped): `A = span{1, X}`, `X = diag(0,1,2)`: unital, `*`-closed, `{1, X, X²}` of rank 3 so
  `X² ∉ A`, and `x y ∈ A` for `x, y ∈ A` only when one is scalar; `φ(1) = 1`, `φ(X) = 1`: linear, `*`- and
  trace-preserving (`tr X = 3`), multiplicative on every pair with product in `A`; `tr φ(X)² = 3 ≠ 5 = tr X²`.
- **N4** (`hstarA` dropped): `A` the upper-triangular `2 × 2` matrices (unital, multiplicatively closed,
  `E₀₁ᴴ ∉ A`), `φ = Ad diag(2,1)`: multiplicative, trace-preserving, the identity on `A ∩ Aᴴ` (the diagonal), so `hstar`
  holds wherever it applies; `tr φ(E₀₁)ᴴφ(E₀₁) = 4 ≠ 1 = tr E₀₁ᴴE₀₁`.

## The decision rules (implemented by `controls.py verdict`)

| Cell | Token | Rule |
|---|---|---|
| Q-CORE | `WT2-1-CORE-PROVED`; else `WT2-1-CORE-UNDECIDED` | the module is present at `E`, its statements are exactly the frozen ones (S1), resolve to the landed objects (S2), and the exact-head run at `E` builds the module with the core's print within `[propext, Classical.choice, Quot.sound]` |
| Q-GEN | `WT2-1-GENERAL-PROVED` | the positive surface is present; `WT2_hiddenConjugate` has exactly the frozen signature and its print is within the three axioms at `E` |
| Q-GEN | `WT2-1-GENERAL-COUNTERMODEL` | the countermodel surface is present in place of the positive one; `WT2_countermodel` has exactly the frozen signature and its print is within the three axioms at `E` |
| Q-GEN | `WT2-1-GENERAL-UNDECIDED` | neither surface is present at `E` |
| Q-IFF | `WT2-1-IFF-PROVED`; else `WT2-1-IFF-NOT-ESTABLISHED` | the iff has the frozen signature, its print is within the three axioms, and its proof term names the two witnesses, one per direction (S3) |
| Q-EXACT | `WT2-1-INSTANCES-EXACT`; else `WT2-1-INSTANCES-NOT-ESTABLISHED` | the probe blob at `E`, run by `controls.py` with `python3 -I`, prints `PASS` for K0, K1, X1–X4, N1–N4, no `FAIL`, `checks: 10, failures: 0` and the verdict line |

No rule reads another cell's outcome. Tokens are printed by `controls.py verdict E` from the measurements at `E`. Both
surfaces present fails S1; a verdict over a failed control is void and the round halts (`S12`). Under
`WT2-1-GENERAL-UNDECIDED` the landing is record-only (below), so no module is present at `E`, and Q-CORE reads
`WT2-1-CORE-UNDECIDED` and Q-IFF `WT2-1-IFF-NOT-ESTABLISHED` by their own rules.

## What each positive token credits, and its countercontrol

| Token | Credited hypothesis | What it contributes | Countercontrol (conclusion fails without it) |
|---|---|---|---|
| `CORE-PROVED` | `htr` | fixes the multiplicities: the conclusion implies trace preservation | X2 (map injective, unital, multiplicative, `*`-preserving; trace differs) |
| | `hmul` | the conclusion implies multiplicativity | N1 |
| | `hstar` | the conclusion implies `*`-preservation | N2 |
| | `hmulA` | `A` an algebra, not only a `*`-closed subspace | N3 |
| | `hstarA` | invariant complements (A1) | N4 |
| | `h1` | nothing: carried because `WT1_transfer` supplies it | none exists: for a non-unital `*`-subalgebra, `φ` extends to `A + ℂ1` by `1 ↦ 1`, which satisfies every other hypothesis |
| `GENERAL-PROVED` | `WordTracesEqual U U'` | the trace form behind `WT1`'s map and the core's `htr` | X2's pair `U_R, U_S`: every word relation agrees (the letter map is a unital `*`-isomorphism of the word spans), the traces differ, and by necessity the pair is not hidden-conjugate; Pair C (`WT0b_pairC_not_wordTracesEqual`) is the landed one |
| | dropped: `BlockSpanning`, unitarity | non-vacuity of the strengthening | X1, X3 (non-spanning), X4 (non-unitary and non-spanning) are in its domain |
| `IFF-PROVED` | — | assembly; no novel result beyond `GENERAL-PROVED` | its directions' |
| `INSTANCES-EXACT` | — | control layer; the countercontrols above | each check's own mutation in `controls.py --self-test` |

`GENERAL-COUNTERMODEL` and the undecided tokens are not positive tokens. The result note counts `CORE-PROVED` and
`GENERAL-PROVED` as the round's novel results and no other token.

## The earned reading and the non-inference rule

> Earned reading (only when Q-CORE, Q-GEN and Q-IFF are positive and Q-EXACT is exact): on every finite carrier
> V × H, for all pairs, with no spanning and no unitarity hypothesis, equal block-word traces imply hidden
> conjugation (WT2_hiddenConjugate) and hidden conjugation implies equal block-word traces
> (trace_wordEval_hiddenConjugate), assembled as hiddenConjugate_iff_wordTracesEqual; every linear map of a unital
> *-subalgebra of M_m(ℂ) into M_m(ℂ) that is multiplicative, *-preserving and trace-preserving on it is conjugation
> by a unitary (exists_unitary_of_traceStarMul).

> Countermodel reading: the statement renders a classical theorem over ℂ, so a kernel countermodel is read as the
> statement or a landed definition (wordEval, WordTracesEqual, HiddenConjugate) not rendering the classical question,
> named in the result note for owner review; no failure of word-trace sufficiency, label move or ROADMAP wording
> follows. Undecided reading: WT2 stays at 24.1A's strength; the result note names the stopping piece from (A1)–(A6)
> or "other", whether the route-change obstruction was met, and the last kernel-checked lemma.

> Non-inference rule: under no outcome does the round show that the reconstruction framework supplies the block-word
> trace data (24.1B's question) or decide how BlockSpanning and HiddenCommutantTrivial stand to each other (24.1C's).
> Nothing about completeness of 𝒢_sub, generators (ii) and (iv) or the physical wave rule follows. Lemma 24.1 is not
> repaired, the generators are neither called complete nor called incomplete, the manuscripts' route is not restored,
> the P1 label stays OPEN, and the probe is an exact computation, not a kernel proof. An exhausted budget or an
> undecided cell supports no negative mathematical conclusion: not that WT2 is false, not that route (A) fails, not
> that the structure theorem is necessary.

**Premises this round does not source:** the word-trace data (`WordTracesEqual U U'` is a hypothesis; whether the
framework fixes it is 24.1B's question); any spanning, commutant or unitarity property of substratum dilation data.

## The ROADMAP wording the round would license (P1 row :64, section :687–707; not applied by the round)

With Q-CORE, Q-GEN and Q-IFF positive, the row's "sufficiency on general pairs UNDECIDED at the unitary-implementation
step" may become "WT2-1: on every pair, equal block-word traces imply hidden conjugation (`WT2_hiddenConjugate`) and
conversely (`trace_wordEval_hiddenConjugate`), assembled as `hiddenConjugate_iff_wordTracesEqual`", and the section may
gain a paragraph after 24.1A's, which stays (`R7-WTS` pins it, edge_rigidity_probe.py:10164–10179; the README ledger
and census family it pins are at :10182–10198). The row stays `OPEN` under every outcome; under any other outcome no
wording is licensed. A later propagation edits text that `R7-WTS`'s W24 reads (README "sufficiency on general pairs is
UNDECIDED", the census note "WT2 UNDECIDED"), so it amends that guard in the same change.

## The controls (in `controls.py`)

- **S1 surface**: preamble, frozen declaration list, one print per named result, exactly one surface. Mutations, each
  failing with its code: `BlockSpanning U` or `Uᴴ * U = 1` added to `WT2_hiddenConjugate`; `htr`, `hmulA` or `hstarA`
  dropped from the core; `A` retyped to a `StarSubalgebra`; the core's conclusion weakened to an intertwiner;
  `WT2_countermodel` beside `WT2_hiddenConjugate`; a print removed; a `sorry`; an `axiom`.
- **S2 resolution**: every landed object cited above resolves to its declaration at `D`; SemigroupTransfer.lean (blob
  `5ee55b5c`) and WordTraceSufficiency.lean (blob `ea8e9692`) are unchanged at `E`.
- **S3 load-bearing**: (i) the iff names `trace_wordEval_hiddenConjugate` forward and `WT2_hiddenConjugate` backward
  (a forward term not naming it fails S3 alone); (ii) `WT2_hiddenConjugate` names `WT1_transfer` and the core;
  (iii) X2, X4 and N1–N4 as countercontrols, each mutated in `--self-test` into a non-countermodel (`U_S := U_R`;
  `φ := id` for N1; `S := 1`; `X := diag(0,1,1)`, whose `A` is an algebra; `diag(2,1) := 1`; X4 rescaled to `U_R`),
  which must fail its check; (iv) `R7-WTS` green at `E` (its W17, edge_rigidity_probe.py:10125–10135, reads only
  WordTraceSufficiency.lean). **V**: four tokens, each reading exactly when its rule holds. **G**: `D → E` governed.
- **S4 phrases**: "Lemma 24.1 is repaired", "completeness holds", "completeness fails", "the generators are complete",
  "the generators are incomplete", "the manuscripts' route is restored", "the framework supplies", "24.1B is
  answered", "the classes coincide", "word-trace sufficiency fails", "WT2 is false", "route (A) fails", "kernel proof
  of" (for the probe), "design module".

## Budget, stopping and the undecided landing

- **Budget.** Proof development runs after `F`, on linear execution commits. An attempt is one exact-head
  `workflow_dispatch` run of `verify.yml` on an execution commit whose tree carries the module, its import line and
  its census family. At most six attempts, numbered in the result note; no automatic extension, and no seventh attempt
  in this round. A failure counts as an attempt unless it is a verified infrastructure failure: a job that fails
  before the bridge build starts or through the runner or the cache service, recorded with run, job, failing step
  and the digest of the log excerpt read. The statement-surface design run before `F` and the run at a candidate `E`
  are not attempts.
- **Stopping.** The owner designates `E`. An exhausted budget designates nothing and licenses no token.
- **Undecided landing.** If Q-GEN would read UNDECIDED, the candidate `E` is record-only: its tree differs from `D`
  only in the record directory. Commits after the last attempt remove the module, its import line and its census
  family, so no unfinished kernel declaration is registered; a useful intermediate theorem needs its own separately
  frozen round. The result note names the stopping piece and the last kernel-checked lemma: the last lemma in the
  last attempt whose bridge job was green with that lemma's print within the three axioms, cited by attempt, commit
  and retained expected result, or "none".
- **Certification.** `WT2-1-GENERAL-UNDECIDED` and `WT2-1-CORE-UNDECIDED` are bounded outcomes only with every control
  green, S2's blobs unchanged, no `sorry` and no new axiom, and every required job of the exact-head run at `E` green.
  Otherwise the round halts (`S12`).

## Evidence retention (§A.42)

Every retained item is an expected-result JSON (deterministic outputs only, naming its commit, recipe, run, job and
the digest of the text read), under `evidence/` in the record directory, outside `amendments/`. No raw log is
committed.

- `evidence/design-surface.json` — the statement-surface design run (a disposable branch from `D`; the frozen
  statements elaborated as `def … : Prop` with no proofs, the probe and `controls.py --self-test`), pinned by sha256 in
  this file before `F`, committed by the first execution commit.
- `evidence/run-F.json` — `F`'s exact-head run, committed by the first execution commit.
- `evidence/attempt-<k>.json` — attempt `k`'s bridge result and the module's axiom reports, committed by a later
  execution commit, at the latest the result-note commit.
- `evidence/probe.json` — the probe's ten check lines and verdict, regenerated by `python3 -I wt2_1_probe.py`.
- `evidence/run-E.json` — `E`'s exact-head run, added by an evidence-retention pull request to `main` before the
  reconciliation; the reconciliation takes a base containing it and the receipt's candidate entry for `E` names its
  digest. Nothing writes to the record directory after `Q`.

## Invariants and their checkpoints (§A.41)

| invariant | checkpoint |
| --- | --- |
| execution begins from the frozen control plane; controls and probe are the frozen ones | `C1`: this file's blob at `F`; `C2`: blobs at stage 1 and at `E`, `controls.py --self-test` OK at `E` |
| the design evidence pinned here is the evidence retained | `C8`: sha256 of `evidence/design-surface.json` at the first execution commit equals the pin |
| at most six attempts; each counted or excused with its evidence | `C9`: one `attempt-<k>.json` per attempt, `k ≤ 6`, each excused failure with its job and step |
| under a module-landing outcome every frozen declaration elaborates within the three axioms; exactly one surface; the iff's two witnesses | `C3`: the dispatch run at exactly `E`, every job `success`, bridge build and prints; `C5`: S1, S3(i) in `controls.py check E --freeze F` |
| landed modules untouched; `R7-WTS` green; the exact layer replays | `C5` (S2 blobs); `C3`: the guard step at `E`; `C5`: the probe's verdict line at `E` |
| under `GENERAL-PROVED` or `GENERAL-COUNTERMODEL` the module is registered; under `GENERAL-UNDECIDED` nothing outside the record directory changes | `C4`: the release gate at `E` passing every step; `C6`: `git diff --no-renames --name-status D E`, record paths only under `GENERAL-UNDECIDED`; `C5` (G) |
| `E`'s run is retained on `main` before the reconciliation | `C10`: `evidence/run-E.json` reachable from the reconciliation's first parent, its digest in the receipt's candidate entry |
| the native receipts hold; legacy records untouched | `C7`: `v3_verifier --verify-round Q`; `legacy_records_check.py` at every stage commit and `Q` |

## Design work required before F

1. Write the probe and `controls.py` in the record directory; run the probe three times and compare outputs.
2. On a disposable branch from `D`, build the statement surface as `def … : Prop` and confirm it elaborates; fix S1
   (declarations, helpers, budget) and check that `cfc_mem_elemental`, `orthogonal_mem_invtSubmodule` (via
   `Matrix.toEuclideanCLM`) or a direct matrix argument serve (A1) and (A2) for `Matrix H H ℂ`. Retain the run as
   `evidence/design-surface.json` and pin its sha256 here.
3. Owner choices: the module name and the directory slug.

## Reconciliation

After `D`, `main` appended `import OIBridge.TurnpikePremiseOrientation` (OIBridge.lean:269) and a BG-2 census family
at the tail of `lean-manuscript-census.json`. Under a module-landing outcome the round appends at the same two tails,
so the reconciliation conflicts there; it keeps both sides' entries (§A.39). Under the record-only landing it touches
neither file.

## Stages and outcomes

Stages: C1 `controls.py`, the probe and the design evidence; attempts 1–6, each a stage commit; the record-only
reversion if Q-GEN is undecided; the result note = candidate `E`; the evidence-retention pull request for `E`'s run;
the reconciliation; `Q`. **`WT2-1-READ`**: `controls.py check E --freeze F` OK, four tokens printed, the exact-head run at
`E` green on every job. **`WT2-1-HALTED`**: otherwise (`S12`). No outcome moves the P1 label or edits the ROADMAP, the
README, a manuscript or a landed module; correctness bands unchanged (consistency axis).
