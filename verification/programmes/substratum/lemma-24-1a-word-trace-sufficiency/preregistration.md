# Reconstruction — Lemma 24.1A, ST5 sufficiency: do equal block-word traces force a single hidden conjugation? CONTROL PLANE

**This file is a preregistration and nothing else.** It carries no Lean, no probe guard, no
`ROADMAP` edit, no census edit, no manuscript edit, and no outcome label. It **does** carry,
deliberately, the frozen analysis and predictions below — that is what a preregistration is for,
and recording them before merge is what makes them auditable rather than retrospective. Every
*execution-specific* object is excluded. It is merged **alone**, before any execution begins, and
the execution PR descends from the commit that merges it, under the ancestry certificate frozen
below. **Blob identity is authoritative.** The execution guard pins this file by content.

This round **continues** the Lemma 24.1 round in
`verification/programmes/substratum/lemma-24-1-semigroup-transfer/` (control plane blob
`b8168df9ed1acff21eb89e84487b43470124f845`, executed as PR #598). That round left exactly one
target at its frozen fallback: `ST5` sufficiency, UNDECIDED with the obstruction named. This round
is **`ST5` sufficiency only**. It is a **positive-expectation round with a formalization risk**:
the mathematics is expected to be true, and the predictions below are made at the strength the
recorded analysis supports and no higher.

## The owner's framing, quoted as the authority for this round's scope

> Reconstruction / Lemma 24.1 is now a separate repair problem. #598 established that the
> existing visible-channel-family → one hidden conjugation route fails on the tested readings.
> The reconstruction completeness theorem itself was not disproved; the proof route was. The
> ROADMAP therefore correctly keeps Lemma 24.1 OPEN. The next clean round here should be ST5
> sufficiency: equality of all relevant block-word traces ⟹? single hidden unitary conjugacy. We
> already have necessity. If sufficiency is proved, then a second question follows: does the
> actual reconstruction framework give that stronger information? If sufficiency fails, we need a
> genuinely different invariant/completeness argument.

So this round is **24.1A — sufficiency only**. The follow-on question — *does the reconstruction
framework supply the block-word trace data?* — is **round 24.1B**, a separate round this file
names, scopes in one paragraph below, and **does not begin**.

## Start state

| | |
| --- | --- |
| Merged `main` | `2706a3aa7b87e481df17e3ceab88cd3244ce780d` (PR #603) |
| The round this one continues — control plane | `verification/programmes/substratum/lemma-24-1-semigroup-transfer/preregistration.md`, blob `b8168df9ed1acff21eb89e84487b43470124f845` (PR #594; merge `c46e1606d4cafe2720afd69dc06c667eb0f1acff`) |
| The round this one continues — result | `verification/programmes/substratum/lemma-24-1-semigroup-transfer/result.md`, blob `b5822febb2626af48c29f6198fd6d74637ef9896` (PR #598; sealed execution head `57103e9ddf430c538094fed48358c4d1b050ce4d`, merge `11a8a59d22793a10182f853fe3c05edf5415d724`) |
| The merged module, **consumed unmodified** | `verification/lean-mathlib/OIBridge/SemigroupTransfer.lean`, blob `5ee55b5c7d3dcc45fac2a4b62c135a06d4010ea8` (`visibleBlock`, `familyAt`, `HiddenCommutantTrivial`, `HiddenConjugate`, `wordEval`, `enlarge`, `visibleBlock_conj`, `wordEval_conj`, `trace_wordEval_conj`, `trace_wordEval_enlarge`, `trace_wordEval_hiddenConjugate`, `trace_visibleBlock_hiddenConjugate`, `eq_oneKron_of_comm`, `pairC_blocks`, `pairC_hct`, `pairC'_hct`, `pairC_family`, `pairC_wordTraces`, `ST3_pairC`, `ST4_pairC`, `permMatrix_entry`, `permMatrix_mul_self`, `permMatrix_conjTranspose_self`) |
| The module index that imports it | `verification/lean-mathlib/OIBridge.lean`, blob `6dd7f58f7e9879a961809ece37702d6712171cdc` (line `import OIBridge.SemigroupTransfer`) |
| The toolchain and the Mathlib pin | `verification/lean-mathlib/lean-toolchain`, blob `025e59548e48cf71f2744154e2890beefe30a258` (`leanprover/lean4:v4.33.0`); `verification/lean-mathlib/lakefile.toml`, blob `5935a5aed3ed1bf4c5a7224049464d18ed4a8600` (Mathlib `rev = "v4.33.0"`) |
| The queue row and its section | `verification/ROADMAP.md` — **pinned by quotation below**, not by file blob; the file blob at the base, `5aa4235bf895b7c114feff406cc156d117bdb755`, is **informational only** |
| The existing guard, and the archive-mode mechanism this round adopts | `verification/lean/edge_rigidity_probe.py`, blob `da037c584da485e7ac5a550102a6b394b2a0628f` (`R7-SGT`, in archive mode with `_SGT_SEALED_HEAD = 57103e9d…`, `_SGT_MERGE = 11a8a59d…`; the helper `_rbr_archive_ancestry`) — **informational**: other rounds move this file's blob; this round adds its own region and edits no existing contract |
| The archive-mode rule, as written into a control plane | `verification/audits/foundations/act12-scope-propagation-audit.md`, blob `1d471eddde3bc0df8b7dbf26ddf642c4af6783b5` (PR #600, "The chronology control", the archive-mode clause of 2026-09-13 / PR #599) |
| The control-plane model | `verification/programmes/oi-qm/track-b/act-12-two-sided-gauge/preregistration.md`, blob `5850238f290f0424ff677ff6d5cc2c039b1f58c2`; act 10's strengthened chronology mechanism, `verification/programmes/oi-qm/track-b/act-10-anchor-robustness/preregistration.md`, blob `2e92464dca3809558959d240314dbaf9eaa1c500` |
| The README ledger paragraph of the continued round | `verification/README.md`, blob `ea2c1172ad95c29bab1cc1d7da71ea52bb4ec3d1` — **informational**; the execution adds a paragraph immediately after the Lemma 24.1 paragraph and edits nothing else there |
| The census entry of the continued round | `verification/lean-manuscript-census.json`, blob `30277ad60101f512fe3c353460aa324c99b57199` — **informational**; the execution adds its own entry and edits no other |
| The lemma, read for context and **not consumed** | `papers/Substratum.md`, blob `0ada99357ffd6f475beb1fab4adaa597dc4eae9d` (Theorem 24, Lemma 24.1); `papers/Structure.md`, blob `dd5432d70b2a4ab2238a08ea0f30a5101d6ac898`; `papers/Complexity.md`, blob `dd38c5b39797433b6f5de469f5711fd38b116441` |

**The `ROADMAP` row, pinned by quotation.** The P1 row of the queue table at the base reads,
byte for byte:

> `| **P1** | Substratum Lemma 24.1 — semigroup transfer | Reconstruction | **OPEN** — the semigroup-transfer route is refuted on the tested readings (`ST2`–`ST4`); the obligation itself is untouched | unconditional `𝒢_sub` completeness |`

and the section `### P1 — Substratum Lemma 24.1, the semigroup-transfer step` opens with the
paragraph beginning "**Executed** — `programmes/substratum/lemma-24-1-semigroup-transfer/`" and
containing the sentence "**The label stays OPEN**: a negative on the lemma's route is not an
impossibility theorem for the obligation, Lemma 24.1 is not called false without qualification,
`ST5`'s hypothesis is a candidate strengthened hypothesis and not a certified repair, and the four
generators are not called incomplete — the round says nothing about (ii)/(iv)." **This row text
and this section text are what the execution's start-state check compares against.** Other rounds
— the Track B propagation, the A6 propagation, the hydrodynamics rounds — move
`verification/ROADMAP.md`'s file blob without moving this text; the Lemma 24.1 round recorded
exactly such a discrepancy, and this round avoids it by construction: the file blob above is
informational, the quotation is the pin.

**Sequencing.** This round is independent of every Track B round, of the act 12 scope
propagation, of the A6 propagation and of the hydrodynamics rounds. Its execution touches
`verification/ROADMAP.md` (the P1 section, one appended paragraph, and the P1 row's status text
with the label unchanged), `verification/README.md` (one appended paragraph),
`verification/lean-manuscript-census.json` (one new entry) and
`verification/lean/edge_rigidity_probe.py` (one new contract region) **in its own regions only**,
and adds one Lean module plus one import line. Nothing else moves.

## Why this round exists

The Lemma 24.1 round established, at evidence level 2, that the visible channel family does not
determine the dilating unitary up to a single hidden conjugation on any of the tested readings
(`ST2`–`ST4`), and that equality of **all** block-word traces is **necessary** for hidden
conjugation (`trace_wordEval_hiddenConjugate`). It left **sufficiency** — that equal block-word
traces force a hidden conjugation — UNDECIDED, naming the obstruction: the trace-form kernel step
and the unitary implementation of a trace-preserving `*`-isomorphism between `*`-subalgebras of
`M_m(ℂ)`, neither carried by Mathlib nor by the corpus.

Sufficiency is the hinge of the repair problem. If it holds, the block-word trace functional is
**exactly** the invariant that classifies dilation data up to hidden conjugation, and the repair
question becomes whether the reconstruction framework supplies that functional (24.1B). If it
fails, the invariant is wrong and a different completeness argument is needed. Either way the
answer is a theorem about finite matrices, and this Lean programme exists to settle such theorems
rather than cite them.

The classical mathematics is known: Specht's theorem for one matrix, generalized by Wiegmann and
by Pearcy to tuples — two tuples of matrices with equal traces of all words in the letters and
their adjoints are simultaneously unitarily similar. **What this round adds is the kernel**, and
the honest prediction is that the difficulty is formalization, not truth.

## The objects, FROZEN

Throughout, `V` and `H` are finite types with `|V| = n ≥ 1`, `|H| = m ≥ 1`; the carrier is
`V × H`; a **dilation datum** is a matrix `U` on `ℂ^{V × H}` with `Uᴴ U = 1`. Every statement is
finite-dimensional matrix algebra in the coordinate idiom of `SemigroupTransfer.lean`, whose
definitions are **reused, not redefined**.

**The visible block.** `visibleBlock U v w : Matrix H H ℂ`, the `m × m` block
`U_{vw} = (⟨v| ⊗ 𝟙) U (|w⟩ ⊗ 𝟙)`, entrywise `U (v, h) (w, h')`.

**The block word and its value — the exact merged definition.** A word is a
`List (V × V × Bool)`; a letter `(v, w, true)` is the *plain* block `U_{vw}` and a letter
`(v, w, false)` is the *adjoint* block `U_{vw}ᴴ`; the value is the ordered product in `M_m(ℂ)`:

    wordEval U w = (w.map fun l => if l.2.2 then visibleBlock U l.1 l.2.1
                                            else (visibleBlock U l.1 l.2.1)ᴴ).prod

so `wordEval U [] = 1`, `wordEval U (w₁ ++ w₂) = wordEval U w₁ * wordEval U w₂`
(`List.prod_append`), and the trace is `Matrix.trace` on `M_m(ℂ)`, **unnormalised**. This is the
alphabet and the trace that `trace_wordEval_hiddenConjugate` is stated on, and this round changes
neither.

**Why the block alphabet is the right one, recorded as analysis and not as a target.** The
lemma's data are words in `U`, `U⁻¹ = Uᴴ` and the visible operators `B ⊗ 𝟙` on `ℂ^{V × H}`.
Since `(E_{ab} ⊗ 𝟙) U (E_{cd} ⊗ 𝟙) = E_{ad} ⊗ U_{bc}`, `(Uᴴ)_{vw} = (U_{wv})ᴴ`, and
`Tr_{V × H}[E_{ad} ⊗ X] = δ_{ad} Tr_H[X]`, every trace of a word in `U^{±1}` and the visible
matrix units is a sum of block-word traces, and conversely every block-word trace is such a trace
(insert `E_{vv} ⊗ 𝟙` between letters and sum). Equality of all block-word traces is therefore
equality of the full hidden-tracial functional on the algebra the lemma names. Likewise the
conjugating unitary is **of hidden form by construction**: conjugating every block by one `W` is
conjugating `U` by `𝟙 ⊗ W` (`visibleBlock_conj` at `σ = 1`), and the merged
`eq_oneKron_of_comm` — the commutant of `B(ℋ_V) ⊗ 𝟙` is `𝟙 ⊗ B(ℋ_H)` — is the reason a unitary
on `ℂ^{V × H}` fixing the visible algebra pointwise is of that form. **Neither identification is a
target of this round**; both are recorded so the execution cannot substitute another alphabet.

**The adjoint word.** For `w : List (V × V × Bool)`, `w*` is `w` reversed with every flag flipped,
so that `wordEval U w* = (wordEval U w)ᴴ` (`conjTranspose_mul` reverses order, and
`conjTranspose_conjTranspose` returns an adjoint letter to a plain one).

**The word span.** `𝒲(U) := span_ℂ { wordEval U w : w }`, a subspace of `M_m(ℂ)`. It contains
`1` (the empty word), is closed under multiplication (concatenation, extended bilinearly) and
under `ᴴ` (the adjoint word, extended antilinearly): it is the unital `*`-subalgebra of `M_m(ℂ)`
generated by the blocks `{U_{vw}}`. **The round's algebra is `𝒲(U)`**, and it is a span of word
values, never an abstract `StarSubalgebra.adjoin`, so that every element has a word
representation the trace argument can act on.

**The trace form.** `⟨A, B⟩ := Tr[Aᴴ B]` on `M_m(ℂ)`; positive definite,
`Tr[Aᴴ A] = 0 ↔ A = 0` (Mathlib `Matrix.trace_conjTranspose_mul_self_eq_zero_iff`). On word
values it is a word trace: `⟨w₁(U), w₂(U)⟩ = Tr[(w₁* ++ w₂)(U)]`.

**Word-trace equality — the hypothesis of sufficiency.**

    WordTracesEqual U U'  :⟺  ∀ w, Tr[wordEval U w] = Tr[wordEval U' w].

It is symmetric, it includes the empty word (`Tr 1 = m` on both sides, trivially), and it is
**strictly stronger than family equality**: `ST3_pairC` has equal families and, by
`pairC_wordTraces`, a length-six word with traces `1` and `0`.

**Hidden conjugation — the conclusion.** `HiddenConjugate U U'`, the merged predicate:
`∃ W, Wᴴ W = 1 ∧ U' = (𝟙 ⊗ W) U (𝟙 ⊗ W)ᴴ`.

**The spanning hypothesis — the reduced-strength class.**

    BlockSpanning U  :⟺  𝒲(U) = M_m(ℂ)   (as subspaces: `wordSpan U = ⊤`).

**Frozen relation to `HiddenCommutantTrivial`, recorded so that the two are not conflated:**
`BlockSpanning U → HiddenCommutantTrivial U` is immediate (anything commuting with every block
commutes with all of `M_m(ℂ)` and is scalar). The converse is the finite-dimensional double
commutant theorem (equivalently Burnside's theorem on irreducible matrix algebras), which Mathlib
at the pinned revision does **not** carry — `Mathlib/Analysis/VonNeumannAlgebra/Basic.lean`
records the double commutant theorem as work still to be done, and no Burnside or Jacobson-density
statement for matrix algebras is present. **The round's reduced-strength hypothesis is therefore
`BlockSpanning`, stated as spanning, and never `HiddenCommutantTrivial`.** The `ST3` pair's
`pairC_hct` is not a proof of `BlockSpanning`; if the execution wants spanning for Pair C's `φ̂`
it proves it directly (its four blocks generate all nine matrix units of `M_3(ℂ)`:
`U_{01} = E_{31}`, `U_{10} = E_{13}`, `U_{00} = E_{11} + E_{22}`, `U_{11} = E_{23} + E_{32}`, hence
`E_{11} = U_{10} U_{01}`, `E_{33} = U_{01} U_{10}`, `E_{22} = U_{00} − E_{11}`, `E_{23} = E_{22} U_{11}`,
`E_{32} = U_{11} E_{22}`, `E_{12} = E_{13} E_{32}`, `E_{21} = E_{23} E_{31}` — recorded analysis,
not a target).

## The quantifier direction, FROZEN

Every target is stated in the completeness-relevant direction, from equal traces to a conjugating
`W`:

    ∀ U U', [hypotheses on U, U'] → WordTracesEqual U U' → HiddenConjugate U U'

with `HiddenConjugate` an existential over `W` **inside** the statement, discharged by an
exhibited construction, never by a search. The necessity direction is merged
(`trace_wordEval_hiddenConjugate`) and is **consumed, not re-proved**. On any class where
sufficiency lands, the round states the biconditional
`HiddenConjugate U U' ↔ WordTracesEqual U U'` as a corollary at the same strength.

## The recorded analysis — the route in steps, computed before this freeze was written

**Step 1, the trace-form kernel argument.** Suppose `WordTracesEqual U U'`. Let
`Σ_i c_i w_i(U) = 0` for finitely many words and scalars. Then

    Tr[(Σ_i c_i w_i(U'))ᴴ (Σ_j c_j w_j(U'))] = Σ_{i,j} c̄_i c_j Tr[(w_i* ++ w_j)(U')]
                                          = Σ_{i,j} c̄_i c_j Tr[(w_i* ++ w_j)(U)]
                                          = Tr[(Σ_i c_i w_i(U))ᴴ (Σ_j c_j w_j(U))] = 0,

so `Σ_i c_i w_i(U') = 0` by positive definiteness. Hence `w(U) ↦ w(U')` extends to a well-defined
linear map `φ : 𝒲(U) → M_m(ℂ)` with range `𝒲(U')`; by the symmetric argument it is injective;
concatenation makes it multiplicative, the adjoint word makes it `*`-preserving, the empty word
makes it unital, and `Tr[φ(w(U))] = Tr[w(U')] = Tr[w(U)]` makes it trace-preserving. This is
`WT1`. **Mathlib pieces present:** `Submodule.span`, `Submodule.span_induction`,
`mem_span_range_iff_exists_fun` / `Finsupp.linearCombination` for finite representations,
`Matrix.trace_conjTranspose_mul_self_eq_zero_iff`, `Matrix.trace_mul_cycle`,
`Matrix.trace_mul_comm`, `Matrix.traceLinearMap`, `List.prod_append`, `List.prod_reverse`-style
lemmas for the adjoint word. **Absent:** nothing structural; the cost is the bookkeeping of a
linear map defined on a span by its values on a spanning set.

**Step 2, unitary implementation, the spanning case (`WT2-gen`).** If `BlockSpanning U` and
`BlockSpanning U'`, `φ` is a unital `*`-automorphism of `M_m(ℂ)`. Set `e_{ij} := φ(E_{ij})`: these
are matrix units (`e_{ij} e_{kl} = δ_{jk} e_{il}`, `e_{ij}ᴴ = e_{ji}`, `Σ_i e_{ii} = 1`), and
`e_{11} ≠ 0` because `φ` is injective. Choose a unit vector `ξ` with `e_{11} ξ = ξ` (any nonzero
column of `e_{11}`, normalised; `e_{11}` is a nonzero orthogonal projection). Define `W` by its
columns, `W e_j := e_{j1} ξ`. Then `⟨e_{i1} ξ, e_{j1} ξ⟩ = ⟨ξ, e_{1i} e_{j1} ξ⟩ = δ_{ij} ⟨ξ, e_{11} ξ⟩
= δ_{ij}`, so `Wᴴ W = 1`, and `W E_{ij} Wᴴ (e_{k1} ξ) = δ_{jk} e_{i1} ξ = e_{ij} (e_{k1} ξ)` on the
orthonormal basis `{e_{k1} ξ}`, so `W E_{ij} Wᴴ = e_{ij}` for all `i, j` and, by linearity,
`φ = Ad W` on all of `M_m(ℂ)`. In particular `U'_{vw} = φ(U_{vw}) = W U_{vw} Wᴴ` for every block,
which is `U' = (𝟙 ⊗ W) U (𝟙 ⊗ W)ᴴ` entrywise (`visibleBlock_conj` at `σ = 1`). **This uses
finite matrix algebra only**: no Wedderburn, no Skolem–Noether, no double commutant. **Mathlib
pieces present:** `Matrix.single` (the matrix units `E_{ij}`), `Matrix.of`, `Matrix.mulVec`,
`Matrix.conjTranspose`, `Matrix.mem_unitaryGroup_iff'`, `Matrix.IsHermitian`, `EuclideanSpace`
inner products, `Matrix.toEuclideanLin`. The two-sided hypothesis is frozen; one-sidedness —
`BlockSpanning U'` follows from `BlockSpanning U` because `φ` is an injective linear map from an
`m²`-dimensional space into `M_m(ℂ)` — is a permitted strengthening the execution reports as such
if reached.

**Step 2, unitary implementation, the general case (`WT2`).** `𝒲(U)` is a unital `*`-subalgebra
of `M_m(ℂ)`, hence a finite-dimensional C*-algebra: `𝒲(U) ≅ ⊕_i M_{k_i}(ℂ)`, with central
projections `p_i` and `ℂ^m ≅ ⊕_i ℂ^{k_i} ⊗ ℂ^{μ_i}` (no null summand, since `𝒲(U)` is unital), so
`Tr p_i = k_i μ_i`. A trace-preserving `*`-isomorphism `φ : 𝒲(U) → 𝒲(U')` carries `p_i` to the
central projection `p'_i` of the isomorphic summand, with `k'_i = k_i` (intrinsic to the abstract
summand) and `Tr p'_i = Tr p_i`, hence `μ'_i = μ_i`. Two unital `*`-representations of
`⊕_i M_{k_i}(ℂ)` with equal multiplicities are unitarily equivalent — the matrix-unit
construction of the spanning case, run once per summand with `μ_i` orthonormal choices of `ξ` —
and the implementing `W` satisfies `W x Wᴴ = φ(x)` on `𝒲(U)`, in particular on every block. **This
is where trace preservation on the whole algebra is what fixes the multiplicities**, which is why
the hypothesis is the full word-trace functional and not the family. **Mathlib pieces present:**
Wedderburn–Artin in abstract form (`IsSimpleRing.exists_algEquiv_matrix_divisionRing`,
`IsSemisimpleRing.exists_algEquiv_pi_matrix_divisionRing`, and over an algebraically closed field
`IsSemisimpleRing.exists_algEquiv_pi_matrix_of_isAlgClosed` in
`Mathlib/RingTheory/SimpleModule/`), `IsSimpleRing (Matrix ι ι A)`, `Algebra.IsCentral` and
`Subalgebra.center` for matrix algebras (`Mathlib/Algebra/Central/Matrix.lean`), Schur's lemma
(`LinearMap.bijective_or_eq_zero`), `StarSubalgebra`, `StarSubalgebra.centralizer`, `StarAlgEquiv`,
`Submodule.starProjection`, `Matrix.IsHermitian.spectral_theorem`. **Absent, and each a piece the
execution would have to prove or route around:** (a) that a `*`-closed subalgebra of `M_m(ℂ)` is
semisimple (every left ideal is complemented, via the trace form) so that Wedderburn–Artin
applies; (b) the **spatial** form — a unitary block decomposition of `ℂ^m` adapted to the summands
— which the abstract `AlgEquiv` does not give; (c) `*`-compatibility of the Wedderburn
isomorphism; (d) the multiplicity count through traces of central projections; (e) the unitary
equivalence of equal-multiplicity representations; (f) Skolem–Noether (no occurrence in Mathlib
at the pin) and the finite-dimensional double commutant theorem (recorded as to be done in
Mathlib's own von Neumann algebra file). This is why `WT2` is predicted at **medium** strength and
`WT2-gen` is frozen as its fallback. An execution that finds an elementary route to the general
case (for instance, induction on `m` by splitting off one irreducible summand with the trace
form) is free to take it: **the freeze fixes statements, not proofs.**

**Step 3, assembly.** `WT1` and `WT2` (or `WT2-gen`) give `WT3` on the class reached; with the
merged necessity, the biconditional on that class.

**Step 4, finite generation.** `𝒲(U)` is a subspace of the `m²`-dimensional `M_m(ℂ)`, so some
finite family of words spans it (`Submodule.FG` of every submodule of a finite-dimensional space,
and extraction of a finite sub-family of the spanning range). The literature's uniform bounds —
Pearcy's bound on word length for pairs, and the general bounds that followed — are **external,
cited, and not claimed**; no explicit bound is a target.

## The targets, FROZEN

### `WT0` — sanity controls, both directions, cheap and certain

(a) **Necessity, re-cited.** `trace_wordEval_hiddenConjugate` is consumed as the necessity
direction; it is not re-proved and not restated under a new name.

(b) **The hypothesis genuinely excludes the `ST3` pair.** `¬ WordTracesEqual φ̂_C φ̂_C'`, from
`pairC_wordTraces` (the length-six word `U₀₀ U₁₀ U₀₁ U₀₀ᴴ U₀₁ᴴ U₁₀ᴴ` has trace `1` on `φ̂_C` and
`0` on `φ̂_C'`), with the pair pinned inside the statement by `U = φ̂_C`, `U' = φ̂_C'` exactly as
`ST3_pairC` pins it. This records that sufficiency is not vacuous in the direction that matters:
the pair the family cannot see, the word traces do see.

(c) **A positive control with the conjugation exhibited.** With `U = φ̂_C` on `ℤ₂ × ℤ₃`,
`W = P_{(1 2)}` the permutation unitary of the hidden transposition `1 ↔ 2` of `ℤ₃`, and
`U' = (𝟙 ⊗ W) U (𝟙 ⊗ W)ᴴ`, all three pinned by equations in the statement: `Wᴴ W = 1`,
`HiddenConjugate U U'`, `U' ≠ U` (the control is not the identity: `U'` exchanges `(0,1) ↔ (1,0)`
where `U` exchanges `(0,2) ↔ (1,0)`), and `WordTracesEqual U U'` (by necessity). This is the
direction sufficiency must reproduce, on an instance where the answer is known.

**Predicted POSITIVE, at full strength**, all three parts.

### `WT1` — the trace-form kernel step

> For `U, U'` on the same carrier with `WordTracesEqual U U'`, there is a linear map
> `φ : 𝒲(U) →ₗ[ℂ] M_m(ℂ)` with `φ ⟨w(U)⟩ = w(U')` for every word `w`, whose range is `𝒲(U')`,
> which is injective, unital (`φ 1 = 1`), multiplicative (`φ(xy) = φ(x) φ(y)` for `x, y ∈ 𝒲(U)`),
> `*`-preserving (`φ(xᴴ) = φ(x)ᴴ`), and trace-preserving (`Tr φ(x) = Tr x`).

The execution may state this existentially, as written, or through a named induced map (budget
slot 5); the seven properties are the target either way, and each is a conjunct of one statement
or a separately named result consumed by `WT2`. **No unitarity hypothesis is needed** and none is
to be added. **Predicted POSITIVE, at high strength.** High rather than full only for the
formal cost of a map defined on a span by its values on a spanning set; there is no mathematical
risk.

### `WT2-gen` — unitary implementation on the spanning class (**the reduced-strength kernel target**)

> For `U, U'` on the same carrier with `BlockSpanning U`, `BlockSpanning U'` and
> `WordTracesEqual U U'`, `HiddenConjugate U U'`.

By the matrix-unit construction of the recorded analysis, and nothing else needed. **Predicted
POSITIVE, at high strength.** This is the target the round is built to reach whatever happens to
`WT2`, and it is chosen over the other candidates for the fallback for recorded reasons: over
`HiddenCommutantTrivial` on both sides, because that hypothesis reaches spanning only through the
double commutant theorem, which is absent; over "`ℋ_H` of dimension at most two", because that
needs a classification of the `*`-subalgebras of `M_2(ℂ)` that is a detour from the route and is
also absent; over "the `ST3` pair", because sufficiency is vacuous on that pair (`WT0(b)`) and
sufficiency *from* `φ̂_C` to an arbitrary `U'` is an instance of the spanning case that is no
easier than the spanning case itself. **One-sided form permitted:** if the execution derives
`BlockSpanning U'` from `BlockSpanning U` and `WT1`, it reports the one-sided statement as a
strengthening; the two-sided statement is what is frozen and what the label attaches to.

### `WT2` — unitary implementation in general

> For `U, U'` on the same carrier with `Uᴴ U = 1`, `U'ᴴ U' = 1` and `WordTracesEqual U U'`,
> `HiddenConjugate U U'`.

**Predicted POSITIVE as mathematics, at medium strength at kernel level.** The recorded analysis
names six absent pieces; the execution attempts the route, or an elementary alternative, and
reports the strength reached. **Frozen fallback:** if `WT2` is not reached, the execution reports
`WT2-gen` at its strength and `WT2` **UNDECIDED with the obstruction named** — which piece, of
(a)–(f) or another, stopped it — and does not promote. The unitarity hypotheses are carried
because the carrier class is dilation data; if the proof does not use them, the execution drops
them and says so.

### `WT3` — the assembled sufficiency statement, at the strength jointly reached

> `(∀ w, Tr[wordEval U w] = Tr[wordEval U' w]) → HiddenConjugate U U'`, on the frozen carrier
> class: **all** unitary pairs on every finite `V × H` if `WT2` lands; the **spanning** pairs if
> only `WT2-gen` lands; together with the biconditional
> `HiddenConjugate U U' ↔ WordTracesEqual U U'` on the same class, its reverse direction being the
> consumed `trace_wordEval_hiddenConjugate`.

**Predicted at `WT2`'s strength**, exactly. `WT3` is `WT1` composed with whichever of `WT2` /
`WT2-gen` lands; it introduces no new mathematics and no new risk. It is stated once, on the
class reached, and never at a class above the one reached.

### `WT4` — finite generation and bounded word length: analysis, with one optional cheap kernel statement

The kernel statement, if made: `∃ S : Finset (List (V × V × Bool)), span { wordEval U w : w ∈ S }
= 𝒲(U)` — the existence of a finite spanning family of words, from finite-dimensionality.
**Predicted POSITIVE, at full strength if attempted**; it may be left as analysis without any
label. **No explicit length bound is claimed, in either case.** Whether a *uniform* finite family
of words — depending on `m` alone — suffices for the hypothesis of `WT3` is the Pearcy-type
question; it is recorded as analysis, with the literature cited as external, and it is **not** a
target. Nothing in `WT3` depends on `WT4`.

## The preregistered predictions, and their strengths

| target | prediction | strength | what would falsify it | frozen fallback |
| --- | --- | --- | --- | --- |
| `WT0(a)` | positive | full | nothing; a citation | — |
| `WT0(b)` | positive | full | an error in `pairC_wordTraces`, which is merged at level 2 | — |
| `WT0(c)` | positive | full | an error in the recorded permutation arithmetic (`U' ≠ U`) | drop the `U' ≠ U` conjunct and say so |
| `WT1` | positive | high | the span bookkeeping exceeding the round formally | UNDECIDED with the obstruction named; `WT2`, `WT3` then UNDECIDED too |
| `WT2-gen` | positive | high | the matrix-unit construction exceeding the round formally | UNDECIDED with the obstruction named |
| `WT2` | positive | **medium at kernel level** | one of the six absent pieces, or another, not reached | `WT2-gen` at its strength; `WT2` UNDECIDED with the obstruction named |
| `WT3` | positive | `WT2`'s strength | — assembly | stated on the class reached |
| `WT4` | positive | full, if attempted | — finite-dimensionality | analysis only, no label |

**UNDECIDED remains a permitted label for every target**, reported with the obstruction. **No
target may be reported at a strength above the one reached.** A positive target is earned by an
exhibited `W` pinned by an equation, never by a search. A negative on any target — a pair with
equal word traces and no hidden conjugation — is **not predicted** and would contradict the
Specht–Wiegmann–Pearcy theorem; if the execution believes it has one, it reports the pair with its
certificate as a *finding requiring owner review* and does not label sufficiency negative without
an append-only amendment.

## The post-round sentence, frozen now, one per outcome

- **If `WT3` lands on all unitary pairs:** *On every finite carrier `V × H`, equality of all
  block-word traces is necessary and sufficient for hidden conjugation of two unitary dilation
  data. Whether the reconstruction framework supplies that data is round 24.1B and is OPEN. The
  P1 row stays OPEN.*
- **If only `WT2-gen` lands, so `WT3` lands on the spanning class:** *On every finite carrier
  `V × H`, for pairs of dilation data whose visible blocks each span all of `M_m(ℂ)`, equality of
  all block-word traces is necessary and sufficient for hidden conjugation; on general pairs
  necessity holds and sufficiency is reached at [the strength stated]. Whether the reconstruction
  framework supplies that data is round 24.1B and is OPEN. The P1 row stays OPEN.*
- **If `WT2-gen` is not reached:** *Necessity of block-word trace equality for hidden conjugation
  holds at level 2; sufficiency is UNDECIDED, the obstruction being [named]. Round 24.1B is not
  begun. The P1 row stays OPEN.*

**In every case the `ROADMAP` row `P1 — Substratum Lemma 24.1` stays OPEN.** Sufficiency of
`ST5` is a statement about an invariant on finite matrices; it is not completeness of `𝒢_sub`,
which needs 24.1B and possibly more. **Nothing may say Lemma 24.1 is repaired; nothing may say
the four generators are complete or incomplete; nothing may say the manuscripts' route is
restored.**

## Round 24.1B, named and not begun

24.1B asks whether the reconstruction framework's data — what Theorem 24's
"observables-preserving" hypothesis actually fixes — determine every block-word trace. `ST3`/`ST4`
show the uniform-prior channel family alone does not; the interleaved balanced words are
multi-time visible correlation data, and whether the framework's notion of observables includes
them is a question about the manuscripts' definitions, not about matrices. This file names 24.1B,
records that it is OPEN, and freezes nothing about it: no target, no prediction, no reading of the
manuscripts. It cannot begin before 24.1A's execution has merged, and it needs its own control
plane.

## What none of these outcomes licenses

- **Nothing about the completeness of `𝒢_sub`.** A positive `WT3` says the word-trace functional
  is a complete invariant for hidden conjugation on the class reached; it does not say the
  framework supplies that functional, and it does not say the four families exhaust `𝒢_sub`. A
  negative or UNDECIDED `WT3` says nothing about `𝒢_sub` either. The forbidden sentences are
  "Lemma 24.1 is repaired", "completeness holds", "completeness is false", "the generators are
  complete", "the generators are incomplete", and "the manuscripts' route is restored".
- **Nothing about generators (ii) and (iv)**, in either direction; they have no meaning on a
  finite carrier.
- **Nothing about Bell or H-Bell**, nothing about A6, nothing about hydrodynamics, nothing about
  Track B or `P0`, nothing about the fibre-Gram classification. The substratum programme and the
  OI→QM programme share the repository and nothing else in this round.
- **No manuscript claim changes in this round.** `papers/` and `book/` are read, not edited;
  whether and how to propagate a positive `WT3` is an owner call after 24.1B, not after 24.1A.
- **Nothing about the physical substratum.** Whether the wave rule on the cubic lattice satisfies
  `BlockSpanning`, or what its word traces are, is not asked.
- **Nothing about approximate deep sectors, time reversal, or enlargement.** `ST4`'s enlargement
  lemma is not consumed; this round is on a fixed carrier.
- **No selection principle is named**, and no sentence beginning "the selection principle is" is
  written.

## Immutable inputs

Cited and consumed **unmodified**: from `SemigroupTransfer.lean`, `visibleBlock`, `familyAt`,
`HiddenCommutantTrivial`, `HiddenConjugate`, `wordEval`, `enlarge`, `visibleBlock_apply`,
`visibleBlock_conj`, `wordEval_conj`, `trace_wordEval_conj`, `trace_wordEval_enlarge`,
`trace_wordEval_hiddenConjugate`, `trace_visibleBlock_hiddenConjugate`, `eq_oneKron_of_comm`,
`hiddenKron_unitary`, `permMatrix_entry`, `permMatrix_mul_self`, `permMatrix_conjTranspose_self`,
`pairC_blocks`, `adj_literals`, `pairC_hct`, `pairC'_hct`, `pairC_family`, `pairC_wordTraces`,
`ST3_pairC`, `ST4_pairC`; the merged single-map modules `StinespringUniqueness.lean`,
`KrausUniqueness.lean`, `UhlmannUniqueness.lean`, `FactorUniqueness.lean` as the merged module's
imports, none consumed directly here; the `Substratum` structure of
`SubstratumInterfaceAudit.lean`; every merged label of every programme; the `R7-SGT` guard and
its archive-mode pins. **`SemigroupTransfer.lean` is not edited**: its blob
`5ee55b5c7d3dcc45fac2a4b62c135a06d4010ea8` is what the execution imports. The manuscripts are
read, not edited.

## The chronology control — act 10's STRENGTHENED mechanism, carried forward by name, with archive mode

1. **This preregistration blob is merged into `main` before any execution-specific object of this
   round enters the repository tree** — any Lean definition or proof about word spans, adjoint
   words, the trace form, induced maps, matrix-unit constructions or spanning classes, any probe
   guard, any result artifact. **The single permitted exception is the analysis recorded inside
   this control-plane blob itself**, merged *as* the freeze.
2. **The execution PR's base must be exactly the merge commit of this control-plane PR**, and the
   execution branch is never updated from later `main`.
3. **The execution guard pins both**: this file's blob SHA by content, and the execution ancestry,
   **fail-closed**.
4. **The ancestry question is asked of the real execution head** — `pull_request.head.sha` from
   the Actions event payload, **never** the synthetic merge commit `refs/pull/<n>/merge`. An
   unresolvable head **fails closed**, with no fallback.
5. **The check excludes pre-freeze side history.** With `B` this control plane's merge commit and
   `H` the real execution head: `B` ancestor-of `H`, **and every commit in `git rev-list H ^B`
   itself a descendant of `B`**, fail-closed. A guard that checks only the head does not
   discharge this clause.
6. **The guard recovers whatever history it needs itself** — deepening a shallow clone, fetching
   an absent commit — and **fails** if recovery fails, for `B`, for `H`, and for every enumerated
   commit alike.
7. **Archive mode — the rule of 2026-09-13, PR #599.** Once the execution PR has merged, neither
   `HEAD` on `main` nor the head of a later pull request is the execution head, and clause 5 run
   against either would refuse sibling rounds it should not refuse. So after the merge the guard
   **re-runs the same strong check of clauses 4–6 against the sealed execution head pinned by
   SHA, together with its merge commit**: the pinned merge commit's **second parent must equal
   the sealed head**; the sealed head must pass clause 5 against `B` exactly as it did in its own
   PR run; and **both the sealed head and the merge commit must be reachable from the current
   target** — the real `pull_request.head.sha` in PR CI, `HEAD` otherwise — so that a rewritten
   or vanished history fails rather than passes; **fail-closed** at each of the three. Nothing
   about `B` or the preregistration pin changes. The pins are added in a follow-up that records
   the sealed head after exact-head review and merge; until then the guard runs in execution
   mode. The mechanism is the merged `_rbr_archive_ancestry`, reused, not re-implemented; the
   new contract is its own region of `verification/lean/edge_rigidity_probe.py` (tag proposed
   `R7-WTS`; the execution fixes the tag), and `R7-SGT` is untouched.

**The claim is scoped to the repository record.** Commit SHAs locate; **blob SHAs are what is
pinned**, and the two are named as such wherever both appear.

## Definition budget

The execution introduces **at most six** top-level definitions, in one new module
`verification/lean-mathlib/OIBridge/WordTraceSufficiency.lean` importing
`OIBridge.SemigroupTransfer`, and these are the six:

1. **`wordStar`** — the adjoint word: reverse, every flag flipped, with the lemma
   `wordEval U (wordStar w) = (wordEval U w)ᴴ`. *Needed.*
2. **`wordSpan`** — `𝒲(U) = Submodule.span ℂ (Set.range (wordEval U))`. *Needed.*
3. **`WordTracesEqual`** — `∀ w, trace (wordEval U w) = trace (wordEval U' w)`, *if* the inline
   quantifier is not readable in every statement that carries it. *Conditional.*
4. **`BlockSpanning`** — `wordSpan U = ⊤`, *if* the inline equation is not readable in `WT2-gen`
   and `WT3`. *Conditional.*
5. **An induced-map definition** (`transferMap` or similar) for `WT1`'s `φ`, *if* `WT1` is not
   stated existentially. *Conditional.*
6. **An implementing-unitary abbreviation** for the matrix `W` with columns `e_{j1} ξ`, *if* the
   inline `Matrix.of` is not readable in `WT2-gen`'s proof-carrying statement. *Conditional.*

**A seventh definition requires its own append-only amendment.** **No witness is a top-level
definition**: the positive control's `U`, `W` and `U'`, the `ST3` pair, the separating word, the
vector `ξ` and every `W` an existential produces are bound variables pinned by equations inside
the statements that need them, exactly as `ST2_pairA`, `ST3_pairC` and `ST4_pairC` pin theirs;
Pair C's permutations are restated as local notation for the same products of transpositions, or
written out, and are not declarations. The merged module's definitions are **reused, not
redefined**; in particular no second word-evaluation, block, or hidden-conjugation predicate is
introduced under any name.

## Evidence level

**Evidence level 2** — kernel-checked, every named result with its own `#print axioms` line at
the foot of the module printing exactly `[propext, Classical.choice, Quot.sound]`; no `sorry`, no
`axiom`, no `native_decide`; `decide` permitted on finite types — for every target at the strength
reached, with the preregistered fallbacks for `WT2` and, if needed, `WT2-gen` and `WT1`. Every
certificate is an exact rational identity; no floating-point evidence enters any label.

## Named hazards

1. **Reading a positive `WT3` as a repair of Lemma 24.1.** It is a theorem about an invariant on
   finite matrices; the repair needs 24.1B and possibly more; the P1 row stays OPEN.
2. **Substituting the `M_{nm}` word alphabet for the block alphabet mid-round.** The block
   alphabet — `wordEval`'s letters, `Matrix.trace` on `M_m(ℂ)` unnormalised — is frozen; the
   equivalence with words in `U^{±1}` and `B ⊗ 𝟙` is recorded analysis, not a target and not a
   licence to restate the hypothesis.
3. **Using `HiddenCommutantTrivial` as the spanning hypothesis.** The two agree only through the
   double commutant theorem, which is absent; the reduced-strength class is `BlockSpanning`, and
   `pairC_hct` is not a proof of spanning for Pair C.
4. **Promoting `WT2-gen` to `WT2`.** The spanning class is a proper subclass; the label attaches
   to the statement proved.
5. **Promoting a one-sided `WT2-gen` above its strength**, or reporting the two-sided form when
   the one-sided form was proved without saying which.
6. **Silently dropping or adding hypotheses.** Unitarity of `U, U'` is carried in `WT2`/`WT3`; if
   unused, dropped and said; `WT1` carries none and must not acquire any.
7. **A search over `W`.** Every `W` is constructed and pinned; a positive is never "no
   counterexample found".
8. **Reporting a negative without amendment.** A same-trace non-conjugate pair contradicts the
   literature theorem; it is reported as a finding for owner review, not as a label.
9. **Conflating the trace form with the family's Gram form.** `familyAt`'s Gram entries are
   sorted balanced words; the trace form on `𝒲(U)` ranges over all words. The family is not
   consumed here.
10. **Importing Track B acts 11/12, A6, or hydrodynamics** as evidence or analogy. Nothing there
    is an input.
11. **Writing a manuscript sentence.** No manuscript is edited; the result note and the `ROADMAP`
    paragraph describe, they do not restate the lemma.
12. **Any status label other than OPEN for the P1 row**, in any outcome, without owner direction.
13. **Any sentence beginning "the selection principle is", or naming one.** None is named.
14. **Editing `SemigroupTransfer.lean`, `R7-SGT`, or any merged label.** The new module imports;
    the new guard region is its own; nothing merged moves.
15. **Beginning 24.1B.** Not one target, not one reading of the manuscripts' notion of
    observables, enters this round.

## Non-doings

The round does not: run any part of the execution before this file is merged; introduce any
execution-specific object before then (the frozen analysis inside this blob is the permitted
exception, per chronology clause 1); edit `papers/Substratum.md`, `papers/Structure.md`,
`papers/Complexity.md` or any manuscript; change the P1 row's status label; say anything about
completeness of `𝒢_sub`, generators (ii) or (iv), Bell, H-Bell, A6, hydrodynamics, Track B, `P0`,
the fibre-Gram classification, the physical wave rule, approximate deep sectors, enlargement or
time reversal; import acts 11/12; edit `SemigroupTransfer.lean`, the `R7-SGT` contract, or any
merged label; claim an explicit word-length bound; adopt or propose a selection principle; begin
24.1B.

## Execution discipline

- Freeze by exact commit SHA **and blob SHA** before any execution. **Blob identity is
  authoritative.**
- Once frozen, immutable; execution-affecting corrections are append-only amendments, separately
  frozen and merged before the work they affect.
- **This PR carries this file alone.** No Lean, no probe, no manuscript edit, no `ROADMAP`, README
  or census edit.
- **Then exactly one execution PR**, based on the merge commit of this one and never updated from
  later `main`, carrying: the Lean module `OIBridge/WordTraceSufficiency.lean` and its import
  line in `OIBridge.lean`; the result note `result.md` in this directory; the probe guard region
  (pinning this blob by content, resolving the real `pull_request.head.sha`, certifying clause
  5's side-history-excluding ancestry, and carrying the archive-mode pins as `None` until the
  post-merge follow-up sets them); the `ROADMAP` P1 section refresh (one appended paragraph; the
  row's status text may be refreshed; **the label OPEN unchanged**); one README paragraph; one
  census entry. **No manuscript changes.** Each of the shared files is touched in this round's
  own region only.
- Exact-head review after execution is complete, with full CI green.
- **No merge without an explicit owner direction after exact-head review, naming the exact head
  SHA.**
- **After the merge**, one follow-up sets the archive-mode pins — the sealed execution head and
  its merge commit — in the new guard region only, under clause 7.

## Allowed final report

1. **`WT0`** — necessity cited, the `ST3` pair excluded from the hypothesis by the merged word
   certificate, and the positive control with its `W` exhibited;
2. **`WT1`** — the induced map with its seven properties, existentially or by name;
3. **`WT2-gen`** — hidden conjugation on the spanning class, with the matrix-unit construction
   named and the two-sided or one-sided form stated as proved;
4. **`WT2`** — hidden conjugation on all unitary pairs at level 2, or UNDECIDED with the
   obstruction named among (a)–(f) or otherwise;
5. **`WT3`** — the assembled sufficiency and the biconditional, on the class reached and no
   higher;
6. **`WT4`** — the finite spanning family at level 2, or "analysis only", with no bound claimed;
7. the post-round sentence for the outcome reached, in this file's wording;
8. what the outcomes do **not** license, in this file's wording — nothing about `𝒢_sub`
   completeness, (ii)/(iv), Bell/H-Bell, A6, hydrodynamics, Track B/`P0`, the physical substratum,
   and no manuscript change; 24.1B named and not begun;
9. the definition count against the six-slot budget, with conditional slots marked fired or
   unused;
10. the chronology certification, naming the property certified — no commit reachable from the
    execution head lies outside the control-plane merge's descendants — what it does not certify,
    and that archive mode is armed by the post-merge follow-up;
11. the start-state check: every pinned blob present at the base with the pinned identity, and the
    `ROADMAP` row and section byte-identical to the quotation above;
12. the axiom table, one line per named result.

## Points at which this freeze chose a reading, recorded rather than resolved

1. **Block alphabet versus `M_{nm}` alphabet.** The block alphabet is frozen because it is what
   the merged `wordEval` and `trace_wordEval_hiddenConjugate` are stated on; the equivalence is
   recorded analysis. A reader who wants the `M_{nm}` form must say so in terms, in 24.1B or an
   amendment.
2. **Unnormalised trace.** `Matrix.trace` on `M_m(ℂ)`; a normalised trace would change nothing
   mathematically and everything in the merged statements, so it is not used.
3. **Spanning versus trivial hidden commutant.** Spanning is frozen as the reduced-strength
   hypothesis because the equivalence is exactly the absent theorem.
4. **Two-sided versus one-sided spanning.** Two-sided is frozen; one-sided is a permitted
   strengthening.
5. **Unitarity of the data.** Carried in `WT2`/`WT3` as the carrier class; absent from `WT1`;
   dropped where unused and said.
6. **What "the framework supplies the data" means.** Not read here; it is 24.1B's whole content.
