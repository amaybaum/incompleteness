# Reconstruction — Lemma 24.1A, `ST5` sufficiency: do equal block-word traces force a single hidden conjugation? RESULT

Executed under the frozen control plane in this directory, `preregistration.md`, blob
`98cfcfdc0e74ffe0186c502517a842bfeb25d351`, merged into `main` as
`baadea2638019b335d96c892590491a6fb420936` (PR #606) — the freeze's mandated execution base.

## Start state, and the inputs consumed unmodified

| | |
| --- | --- |
| Mandated execution base | `baadea2638019b335d96c892590491a6fb420936` (merge of PR #606; second parent `f049838e4ea17c1991845121fc94f61ab408deb5`) |
| This round's frozen control plane | `preregistration.md`, blob `98cfcfdc0e74ffe0186c502517a842bfeb25d351` |
| The round this one continues — control plane | `verification/programmes/substratum/lemma-24-1-semigroup-transfer/preregistration.md`, blob `b8168df9ed1acff21eb89e84487b43470124f845` |
| The round this one continues — result | `verification/programmes/substratum/lemma-24-1-semigroup-transfer/result.md`, blob `b5822febb2626af48c29f6198fd6d74637ef9896` |
| The merged module, consumed unmodified | `verification/lean-mathlib/OIBridge/SemigroupTransfer.lean`, blob `5ee55b5c7d3dcc45fac2a4b62c135a06d4010ea8` (`visibleBlock`, `wordEval`, `HiddenConjugate`, `visibleBlock_conj`, `trace_wordEval_hiddenConjugate`, `pairC_blocks`, `pairC_wordTraces`, `ST3_pairC`, `permMatrix_entry`, `permMatrix_mul_self`, `permMatrix_conjTranspose_self`) |
| The module index | `verification/lean-mathlib/OIBridge.lean`, blob `6dd7f58f7e9879a961809ece37702d6712171cdc` |
| The toolchain and the Mathlib pin | `verification/lean-mathlib/lean-toolchain`, blob `025e59548e48cf71f2744154e2890beefe30a258`; `verification/lean-mathlib/lakefile.toml`, blob `5935a5aed3ed1bf4c5a7224049464d18ed4a8600` |
| The archive-mode rule | `verification/audits/foundations/act12-scope-propagation-audit.md`, blob `1d471eddde3bc0df8b7dbf26ddf642c4af6783b5` |
| The control-plane model, and act 10's mechanism | `verification/programmes/oi-qm/track-b/act-12-two-sided-gauge/preregistration.md`, blob `5850238f290f0424ff677ff6d5cc2c039b1f58c2`; `verification/programmes/oi-qm/track-b/act-10-anchor-robustness/preregistration.md`, blob `2e92464dca3809558959d240314dbaf9eaa1c500` |
| The README ledger and the census | `verification/README.md`, blob `ea2c1172ad95c29bab1cc1d7da71ea52bb4ec3d1`; `verification/lean-manuscript-census.json`, blob `30277ad60101f512fe3c353460aa324c99b57199` |
| The manuscripts, read and not consumed | `papers/Substratum.md`, blob `0ada99357ffd6f475beb1fab4adaa597dc4eae9d`; `papers/Structure.md`, blob `dd5432d70b2a4ab2238a08ea0f30a5101d6ac898`; `papers/Complexity.md`, blob `dd38c5b39797433b6f5de469f5711fd38b116441` |
| This round's module | `verification/lean-mathlib/OIBridge/WordTraceSufficiency.lean` |

Every blob the freeze's start-state table pins as consumed is present at the base with the
pinned identity. The two rows the freeze marks **informational** differ, and both are **recorded
discrepancies**, not repaired: the freeze cites `verification/ROADMAP.md` at blob `5aa4235b…` and
the base carries `397b06be…`; the freeze cites `verification/lean/edge_rigidity_probe.py` at blob
`da037c58…` and the base carries `921a7a24…` — in both cases sibling rounds merged between the
freeze's authoring and its merge (PR #607's control plane among them), exactly the movement the
freeze anticipated by pinning the `ROADMAP` row **by quotation**. The P1 row *Substratum Lemma
24.1 — semigroup transfer* and the opening paragraph of its section are byte-identical to the
freeze's quotation at the base. The preregistration is not edited; the discrepancies are recorded
here and nowhere repaired. One further placement note: the freeze's informational README row says
the round's paragraph goes immediately after the Lemma 24.1 paragraph; the ledger's chronological
order puts a later round's paragraph there, so this round's paragraph is appended at the ledger's
end, immediately before the CI paragraph, and edits nothing else.

**Track B, A6 and the hydrodynamics rounds are not touched**, in either direction. Nothing from
act 11 or act 12 is consumed as evidence; the only kernel imports beyond Mathlib are
`OIBridge.SemigroupTransfer` and its own imports.

## Outcome, in one line

**`WT0`, `WT1`, `WT2-gen`, `WT3` on the spanning class and `WT4` landed; `WT2` is UNDECIDED.**
`WT0` at full strength in all three parts; `WT1` in full — the induced map is a named definition
with its seven properties each a kernel theorem; `WT2-gen` in full, two-sided as frozen, with the
one-sided form proved as the permitted strengthening; `WT2` exactly at its frozen fallback —
UNDECIDED with the obstruction named — so `WT3` is stated on the spanning class and no higher, as
the biconditional; `WT4` at full strength with no length bound claimed. Two predictions were
exceeded in directions that cost nothing: `WT1` and `WT2-gen` were predicted at high strength for
formal cost and were reached in full. Nothing was reached above its predicted strength in a
direction that would move a label, and **the spanning-class result is not the general one**.

**The central result, at the strength jointly reached:** on the class of dilation data whose
visible blocks span all of `M_m(ℂ)`, the block-word trace functional is a complete invariant for
hidden conjugation — equal word traces give an exhibited hidden unitary `W` with
`U' = (𝟙 ⊗ W) U (𝟙 ⊗ W)ᴴ`, and conversely. On general pairs the same hypothesis gives a
trace-preserving `*`-isomorphism of the word spans; that it is implemented by a unitary is the
step not reached. `ST5`'s hypothesis is therefore certified sufficient on the spanning class and
remains a candidate on the rest, and the P1 completeness obligation remains OPEN.

### Three boundaries, stated once and kept everywhere below

1. **Lemma 24.1 is not repaired.** A theorem about an invariant on finite matrices is not
   completeness of `𝒢_sub`; whether the reconstruction framework supplies the block-word trace
   data is round 24.1B, which is named here and not begun.
2. **The four gauge generators are neither called complete nor called incomplete.** Nothing here
   is about generators (ii)/(iv), which have no meaning on a finite carrier, and nothing here
   exhausts `𝒢_sub`.
3. **The manuscripts' route is not restored.** The semigroup-transfer route stays refuted on the
   tested readings (`ST2`–`ST4`); a sufficiency theorem for a stronger hypothesis does not revive
   the route from the weaker one. **No negative is reported**: no pair with equal word traces and
   no hidden conjugation was found or sought, and none would be labelled without an append-only
   amendment.

## `WT0` — the controls: necessity cited, the `ST3` pair excluded, the positive control

`WT0b_pairC_not_wordTracesEqual`, `WT0c_positive_control`, with `tau_permMatrix` as the
mechanism; the merged `trace_wordEval_hiddenConjugate`, `pairC_wordTraces`, `pairC_blocks`,
`visibleBlock_conj`, `permMatrix_mul_self` and `permMatrix_conjTranspose_self` consumed.

**POSITIVE, at full strength, as predicted, all three parts.**

1. **`WT0(a)`, necessity re-cited.** `trace_wordEval_hiddenConjugate` is consumed as the
   necessity direction wherever it is needed — the reverse half of `WT3_spanning_iff` and the last
   conjunct of the positive control — and is **not re-proved and not restated under a new name**.
2. **`WT0(b)`, the hypothesis genuinely excludes the `ST3` pair.** With `U = φ̂_C` and `U' = φ̂_C'`
   pinned by equations exactly as `ST3_pairC` pins them, `¬ WordTracesEqual U U'`: the merged
   length-six word `U₀₀ U₁₀ U₀₁ U₀₀ᴴ U₀₁ᴴ U₁₀ᴴ` has trace `1` on `φ̂_C` and `0` on `φ̂_C'`
   (`pairC_wordTraces`), so `1 = 0` would follow. The pair the family cannot see, the word traces
   do see; sufficiency is not vacuous in the direction that matters.
3. **`WT0(c)`, the positive control with the conjugation exhibited.** `U = φ̂_C` on `ℤ₂ × ℤ₃`,
   `W = P_{(1 2)}` the permutation unitary of the hidden transposition `1 ↔ 2` of `ℤ₃`, and
   `U' = (𝟙 ⊗ W) U (𝟙 ⊗ W)ᴴ`, all three pinned by equations in the statement; the conjuncts are
   `Wᴴ W = 1`, `HiddenConjugate U U'`, `U' ≠ U` and `WordTracesEqual U U'`. **The `U' ≠ U`
   conjunct is kept**, not dropped: the `(0,1)` block of `U` is `E_{31}` and that of `U'` is
   `W E_{31} Wᴴ = E_{21}`, so the entry `(1,0)` of the block is `0` on one side and `1` on the
   other. The last conjunct is the consumed necessity, applied to the exhibited `W`.

## `WT1` — the trace-form kernel step

`WT1_transfer`, with `wordStar`, `wordSpan`, `WordTracesEqual`, `transferMap`, `wordEval_nil`,
`wordEval_append`, `visibleBlock_eq_wordEval`, `wordStar_cons`, `wordEval_wordStar`,
`wordEval_mem_wordSpan`, `one_mem_wordSpan`, `visibleBlock_mem_wordSpan`,
`wordEval_mul_mem_wordSpan`, `mul_mem_wordSpan`, `conjTranspose_mem_wordSpan`,
`exists_linearCombination`, `linearCombination_mem_wordSpan`, `trace_linearCombination_gram`,
`gram_eq_of_wordTracesEqual`, `linearCombination_eq_zero_of_wordTracesEqual`,
`ker_linearCombination_le`, `transferMap_linearCombination`, `transferMap_apply_of_eq`,
`transferMap_wordEval`, `transferMap_range`, `transferMap_one`, `transferMap_trace`,
`transferMap_wordEval_mul`, `transferMap_mul`, `transferMap_conjTranspose` and
`transferMap_injective` as the mechanism.

**POSITIVE, in full — the freeze predicted high strength for the formal cost of a map defined on
a span by its values on a spanning set, and that cost was paid.** The induced map is the named
definition `transferMap U U' h` (budget slot 5, fired), `𝒲(U) →ₗ[ℂ] M_m(ℂ)`: the word combination
of `U'` factored through the quotient of the coefficient space `List (V × V × Bool) →₀ ℂ` by the
kernel of the word combination of `U`, which is legitimate exactly because of the kernel step.
**The kernel step is the trace form.** `Tr[(Σᵢ cᵢ wᵢ(U))ᴴ (Σⱼ dⱼ wⱼ(U))]` expands into the word
traces `Tr[(wᵢ* ++ wⱼ)(U)]` (`trace_linearCombination_gram`, with `wordEval_wordStar` supplying
`w*(U) = w(U)ᴴ`), so **equal word traces make the two Gram forms agree**
(`gram_eq_of_wordTracesEqual`), and `Tr[Aᴴ A] = 0` forces `A = 0`
(`Matrix.trace_conjTranspose_mul_self_eq_zero_iff`, under `ComplexOrder`): a vanishing word
combination for `U` vanishes for `U'` (`linearCombination_eq_zero_of_wordTracesEqual`). **The
seven frozen properties, each its own theorem and all conjuncts of `WT1_transfer`:**

1. `φ ⟨w(U)⟩ = w(U')` for every word (`transferMap_wordEval`);
2. the range is `𝒲(U')` (`transferMap_range`);
3. injective (`transferMap_injective`): `Tr[xᴴ x] = Tr[φ(x)ᴴ φ(x)]` by properties 5–7, so
   `φ(x) = 0` forces `x = 0` by positive definiteness;
4. unital, `φ 1 = 1` (`transferMap_one`, the empty word);
5. multiplicative on `𝒲(U)` (`transferMap_mul`, concatenation extended bilinearly by
   `Submodule.span_induction` twice);
6. `*`-preserving (`transferMap_conjTranspose`, the adjoint word extended antilinearly);
7. trace-preserving (`transferMap_trace`).

**No unitarity hypothesis is carried and none was added**; `WordTracesEqual U U'` is the only
hypothesis. `𝒲(U)` is a span of word values and never an abstract `StarSubalgebra.adjoin`; it
contains `1` and every block and is closed under products and adjoints (`one_mem_wordSpan`,
`visibleBlock_mem_wordSpan`, `mul_mem_wordSpan`, `conjTranspose_mem_wordSpan`).

## `WT2-gen` — unitary implementation on the spanning class

`WT2gen_hiddenConjugate` (two-sided, as frozen), `WT2gen_oneSided` (the permitted strengthening),
with `exists_unitary_of_starMul`, `single_mul_single_ite`, `conjTranspose_single_one` and
`blockSpanning_of_wordTracesEqual` as the mechanism.

**POSITIVE, in full — the freeze predicted high strength for the formal cost of the matrix-unit
construction, and that cost was paid.** `BlockSpanning U` is `wordSpan U = ⊤` (budget slot 4,
fired), spanning and never `HiddenCommutantTrivial`. **The matrix-unit construction is the frozen
one and no other** (`exists_unitary_of_starMul`, finite matrix algebra only): for a linear map
`ψ` of `M_m(ℂ)` that is multiplicative, `*`-preserving and injective, `e_{ij} := ψ(E_{ij})` are
matrix units (`e_{ij} e_{kl} = δ_{jk} e_{il}`, `e_{ij}ᴴ = e_{ji}`); `e_{oo}` is nonzero by
injectivity, so some column `ξ` of it is nonzero and `e_{oo} ξ = ξ`; `W₀` has columns `e_{jo} ξ`
and `W₀ᴴ W₀ = ‖ξ‖² 𝟙` (the Gram entry `⟨e_{io} ξ, e_{jo} ξ⟩ = ⟨ξ, e_{oi} e_{jo} ξ⟩ = δ_{ij} ‖ξ‖²`);
`W := ‖ξ‖⁻¹ W₀` has `Wᴴ W = 1`; `W E_{ij} = e_{ij} W` columnwise, hence `W E_{ij} Wᴴ = e_{ij}`
since a square isometry is unitary; and `ψ = Ad W` on all of `M_m(ℂ)` by linearity. No
Wedderburn, no Skolem–Noether, no double commutant. Applied to `WT1`'s map on `𝒲(U) = M_m(ℂ)`,
every block satisfies `U'_{vw} = W U_{vw} Wᴴ`, which is `U' = (𝟙 ⊗ W) U (𝟙 ⊗ W)ᴴ` entrywise
(`visibleBlock_conj` at `σ = 1`). The empty hidden factor is handled by the subsingleton case,
so no `m ≥ 1` hypothesis appears.

**The two-sided form is the label; the one-sided form is proved and reported as the
strengthening.** The construction consumes `BlockSpanning U` alone — once `𝒲(U) = M_m(ℂ)`, `φ`
is a multiplicative, `*`-preserving, injective map of all of `M_m(ℂ)`, which is all the
construction needs — so `WT2gen_oneSided` is proved directly, and `WT2gen_hiddenConjugate`, the
frozen two-sided statement, is derived from it with its second spanning hypothesis carried and
**unused, which is said here and in the module**. Independently,
`blockSpanning_of_wordTracesEqual` derives `BlockSpanning U'` from `BlockSpanning U` by
injectivity and dimension (`LinearMap.finrank_range_of_inj`, `Submodule.eq_top_of_finrank_eq`),
as the freeze's recorded analysis foresaw. No unitarity hypothesis on `U, U'` is carried.

## `WT2` — unitary implementation in general: UNDECIDED, at the frozen fallback

**UNDECIDED, and the obstruction is named among the freeze's (a)–(f).** `WT1` supplies the input
the general route needs — a trace-preserving `*`-isomorphism `φ : 𝒲(U) → 𝒲(U')` of unital
`*`-subalgebras of `M_m(ℂ)` — and there the round stops. **The obstruction is (b) together with
(e)**: the **spatial** form of the decomposition — a unitary block decomposition
`ℂ^m ≅ ⊕ᵢ ℂ^{kᵢ} ⊗ ℂ^{μᵢ}` adapted to the simple summands of `𝒲(U)`, with `Tr pᵢ = kᵢ μᵢ` — and
the unitary equivalence of two `*`-representations of `⊕ᵢ M_{kᵢ}(ℂ)` with equal multiplicities;
pieces (a) (semisimplicity of a `*`-closed subalgebra), (c) (`*`-compatibility of the Wedderburn
isomorphism) and (d) (the multiplicity count through traces of central projections) are needed on
the way to them. Mathlib at the pin carries Wedderburn–Artin in abstract form and Schur's lemma
and carries none of (a)–(f); the corpus carries none; and none was built here — they are the
structure theory of finite-dimensional C*-algebras in spatial form, which exceeds this round.
The elementary alternative the freeze permitted — induction on `m` by splitting off one
irreducible summand with the trace form — needs an invariant-subspace statement for the
`*`-subalgebra that is (f)-adjacent and equally absent. **`WT2-gen` is reported at its strength
and `WT2` is not promoted.** The unitarity hypotheses `Uᴴ U = 1`, `U'ᴴ U' = 1` of `WT2`'s frozen
statement were never consumed, because the statement was never reached.

## `WT3` — the assembled sufficiency, on the spanning class and no higher

`WT3_spanning`, `WT3_spanning_iff`.

**At `WT2-gen`'s strength, exactly as the freeze fixes it.** `WT3_spanning` is the frozen sentence
with the inline quantifier: for `U, U'` with `BlockSpanning U` and `BlockSpanning U'`,
`(∀ w, Tr[wordEval U w] = Tr[wordEval U' w]) → HiddenConjugate U U'`. `WT3_spanning_iff` is the
biconditional `HiddenConjugate U U' ↔ WordTracesEqual U U'` on the same class, its reverse
direction the consumed `trace_wordEval_hiddenConjugate`. **Stated once, on the class reached, and
never at a class above the one reached.** The unitarity hypotheses of the frozen carrier class are
**dropped because the proof does not use them**, and this is said: nothing in `WT1` or the
matrix-unit construction consults `Uᴴ U`.

## `WT4` — a finite spanning family of words

`WT4_finite_spanning_family`.

**POSITIVE, at full strength.** For every `U` there is a `Finset` of words `S` with
`span { wordEval U w : w ∈ S } = 𝒲(U)`: a linearly independent subfamily of the word values
spanning the same subspace is finite because `M_m(ℂ)` is finite-dimensional
(`exists_linearIndependent`, `LinearIndependent.set_finite_of_isNoetherian`), and a finite subset
of the image of `wordEval U` is the image of a finite set of words. **No explicit length bound is
claimed.** Whether a uniform family depending on `m` alone suffices — Pearcy's bound for pairs and
the bounds that followed — is external, cited, and not a target; nothing in `WT3` depends on
`WT4`.

## The post-round sentence, at the strength jointly reached

Only `WT2-gen` landed, so `WT3` lands on the spanning class, and the frozen sentence for that case
is asserted: *On every finite carrier `V × H`, for pairs of dilation data whose visible blocks
each span all of `M_m(ℂ)`, equality of all block-word traces is necessary and sufficient for
hidden conjugation; on general pairs necessity holds and sufficiency is reached at the strength
of `WT1` — the trace-preserving `*`-isomorphism of the word spans at level 2, its unitary
implementation UNDECIDED. Whether the reconstruction framework supplies that data is round 24.1B
and is OPEN. The P1 row stays OPEN.*

## What the outcomes do not license

- **Nothing about the completeness of `𝒢_sub`.** A positive `WT3` says the word-trace functional
  is a complete invariant for hidden conjugation on the class reached; it does not say the
  framework supplies that functional, and it does not say the four families exhaust `𝒢_sub`. The
  forbidden sentences are "Lemma 24.1 is repaired", "completeness holds", "completeness is
  false", "the generators are complete", "the generators are incomplete", and "the manuscripts'
  route is restored". **Nothing may say Lemma 24.1 is repaired; nothing may say the four
  generators are complete or incomplete; nothing may say the manuscripts' route is restored.**
- **Nothing about generators (ii) and (iv)**, in either direction; they have no meaning on a
  finite carrier.
- **Nothing about Bell or H-Bell**, nothing about A6, nothing about hydrodynamics, nothing about
  Track B or `P0`, nothing about the fibre-Gram classification.
- **No manuscript claim changes in this round.** `papers/` and `book/` are read, not edited;
  whether and how to propagate a positive `WT3` is an owner call after 24.1B, not after 24.1A.
- **Nothing about the physical substratum.** Whether the wave rule on the cubic lattice satisfies
  `BlockSpanning`, or what its word traces are, is not asked.
- **Nothing about approximate deep sectors, time reversal, or enlargement.** `ST4`'s enlargement
  lemma is not consumed; this round is on a fixed carrier.
- **No selection principle is named.** The P1 row's status label stays **OPEN**.
- **Round 24.1B is named and not begun.** Not one target, not one reading of the manuscripts'
  notion of observables, enters this round; 24.1B needs its own control plane.

## Definition budget: **FIVE of the frozen six slots fire**

`wordStar` (slot 1, needed), `wordSpan` (slot 2, needed — a `def` marked reducible so that the
span-induction arguments see through it), `WordTracesEqual` (slot 3, conditional — **fired**,
because the hypothesis appears in eleven statements and the biconditional reads as a predicate),
`BlockSpanning` (slot 4, conditional — **fired**, because `WT2-gen`, `WT3` and the one-sided
strengthening each carry it), `transferMap` (slot 5, conditional — **fired**, because the seven
properties of `WT1` are stated as separate theorems consumed by `WT2-gen` and then assembled).
**Slot 6 is unused**: no implementing-unitary abbreviation; the matrix `W` with columns `e_{jo} ξ`
is a bound variable inside the proof of `exists_unitary_of_starMul`, and every `W` an existential
produces is bound by the statement that produces it. **No seventh definition was introduced.**
Pair C's permutations and the hidden transposition are `local notation` — syntax, not
declarations — and each witness is pinned by an equation inside the statement that needs it; no
witness pair, no `W`, no `ξ`, no carrier and no word is a top-level definition. The merged
module's definitions are reused, not redefined: no second word-evaluation, block or
hidden-conjugation predicate exists under any name.

No hypothesis on the carrier sizes is carried anywhere: the empty hidden factor is handled by the
subsingleton case inside the matrix-unit construction.

## Chronology certification

Guard `R7-WTS` in `verification/lean/edge_rigidity_probe.py` pins this file's preregistration by
content — blob `98cfcfdc0e74ffe0186c502517a842bfeb25d351` — and certifies act 10's strengthened
ancestry predicate with the real execution head: `pull_request.head.sha` from the Actions event
payload in PR CI and `HEAD` locally, never the synthetic merge commit; `B = baadea26…` an ancestor
of the head **and every commit of `git rev-list H ^B` itself a descendant of `B`**, recovering
whatever history it needs and failing closed when it cannot. **The property certified is that no
commit reachable from the execution head lies outside the control-plane merge's descendants.**
What it does not certify: that the merged preregistration was authored before the analysis it
records (the freeze itself carries the recorded analysis, by design), that no execution-specific
object existed outside the repository before the freeze, or anything about branches the head does
not reach. **Archive mode is armed by the post-merge follow-up**: the guard carries
`_WTS_SEALED_HEAD = None` and `_WTS_MERGE = None` until exact-head review and merge, when one
follow-up sets the sealed head and its merge commit in the new region only, under clause 7, and
the merged `_rbr_archive_ancestry` re-runs the same strong check against them. The claim is
scoped to the repository record; commit SHAs locate, blob SHAs are what is pinned.

## Axiom table

Forty named results, one `#print axioms` line each at the foot of the module, every one printing
exactly `[propext, Classical.choice, Quot.sound]`; no unproved declaration, no added postulate,
no kernel-bypassing decision procedure.

| result | target | axioms |
| --- | --- | --- |
| `wordEval_nil` | `WT1` | `[propext, Classical.choice, Quot.sound]` |
| `wordEval_append` | `WT1` | `[propext, Classical.choice, Quot.sound]` |
| `visibleBlock_eq_wordEval` | `WT2-gen` | `[propext, Classical.choice, Quot.sound]` |
| `wordStar_cons` | `WT1` | `[propext, Classical.choice, Quot.sound]` |
| `wordEval_wordStar` | `WT1` | `[propext, Classical.choice, Quot.sound]` |
| `wordEval_mem_wordSpan` | `WT1` | `[propext, Classical.choice, Quot.sound]` |
| `one_mem_wordSpan` | `WT1` | `[propext, Classical.choice, Quot.sound]` |
| `visibleBlock_mem_wordSpan` | `WT1` | `[propext, Classical.choice, Quot.sound]` |
| `wordEval_mul_mem_wordSpan` | `WT1` | `[propext, Classical.choice, Quot.sound]` |
| `mul_mem_wordSpan` | `WT1` | `[propext, Classical.choice, Quot.sound]` |
| `conjTranspose_mem_wordSpan` | `WT1` | `[propext, Classical.choice, Quot.sound]` |
| `exists_linearCombination` | `WT1` | `[propext, Classical.choice, Quot.sound]` |
| `linearCombination_mem_wordSpan` | `WT1` | `[propext, Classical.choice, Quot.sound]` |
| `trace_linearCombination_gram` | `WT1` | `[propext, Classical.choice, Quot.sound]` |
| `gram_eq_of_wordTracesEqual` | `WT1` | `[propext, Classical.choice, Quot.sound]` |
| `linearCombination_eq_zero_of_wordTracesEqual` | `WT1` | `[propext, Classical.choice, Quot.sound]` |
| `ker_linearCombination_le` | `WT1` | `[propext, Classical.choice, Quot.sound]` |
| `transferMap_linearCombination` | `WT1` | `[propext, Classical.choice, Quot.sound]` |
| `transferMap_apply_of_eq` | `WT1` | `[propext, Classical.choice, Quot.sound]` |
| `transferMap_wordEval` | `WT1` | `[propext, Classical.choice, Quot.sound]` |
| `transferMap_range` | `WT1` | `[propext, Classical.choice, Quot.sound]` |
| `transferMap_one` | `WT1` | `[propext, Classical.choice, Quot.sound]` |
| `transferMap_trace` | `WT1` | `[propext, Classical.choice, Quot.sound]` |
| `transferMap_wordEval_mul` | `WT1` | `[propext, Classical.choice, Quot.sound]` |
| `transferMap_mul` | `WT1` | `[propext, Classical.choice, Quot.sound]` |
| `transferMap_conjTranspose` | `WT1` | `[propext, Classical.choice, Quot.sound]` |
| `transferMap_injective` | `WT1` | `[propext, Classical.choice, Quot.sound]` |
| `WT1_transfer` | `WT1` | `[propext, Classical.choice, Quot.sound]` |
| `single_mul_single_ite` | `WT2-gen` | `[propext, Classical.choice, Quot.sound]` |
| `conjTranspose_single_one` | `WT2-gen` | `[propext, Classical.choice, Quot.sound]` |
| `exists_unitary_of_starMul` | `WT2-gen` | `[propext, Classical.choice, Quot.sound]` |
| `WT2gen_oneSided` | `WT2-gen` (one-sided) | `[propext, Classical.choice, Quot.sound]` |
| `WT2gen_hiddenConjugate` | `WT2-gen` | `[propext, Classical.choice, Quot.sound]` |
| `blockSpanning_of_wordTracesEqual` | `WT2-gen` (one-sided) | `[propext, Classical.choice, Quot.sound]` |
| `WT3_spanning` | `WT3` | `[propext, Classical.choice, Quot.sound]` |
| `WT3_spanning_iff` | `WT3` | `[propext, Classical.choice, Quot.sound]` |
| `WT4_finite_spanning_family` | `WT4` | `[propext, Classical.choice, Quot.sound]` |
| `WT0b_pairC_not_wordTracesEqual` | `WT0(b)` | `[propext, Classical.choice, Quot.sound]` |
| `tau_permMatrix` | `WT0(c)` | `[propext, Classical.choice, Quot.sound]` |
| `WT0c_positive_control` | `WT0(c)` | `[propext, Classical.choice, Quot.sound]` |

## Discipline

- **It touches no manuscript.** `papers/Substratum.md`, `papers/Structure.md`,
  `papers/Complexity.md` and every other manuscript are read, not edited.
- **It changes no status label.** The P1 row stays **OPEN**; its section gains one paragraph and
  its row text gains the 24.1A outcome.
- **It names no selection principle.**
- **It edits neither `SemigroupTransfer.lean` nor `R7-SGT` nor any merged label**; the new module
  imports, the new guard region is its own.
- **It imports neither act 11 nor act 12**, and consumes nothing from Track B, A6 or
  hydrodynamics.
- **It begins no part of 24.1B.**
