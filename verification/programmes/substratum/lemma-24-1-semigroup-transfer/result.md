# Reconstruction — Substratum Lemma 24.1, the semigroup-transfer step: RESULT

Executed under the frozen control plane in this directory, `preregistration.md`, blob
`b8168df9ed1acff21eb89e84487b43470124f845`, merged into `main` as
`c46e1606d4cafe2720afd69dc06c667eb0f1acff` (PR #594) — the freeze's mandated execution base.

## Start state, and the inputs consumed unmodified

| | |
| --- | --- |
| Mandated execution base | `c46e1606d4cafe2720afd69dc06c667eb0f1acff` (merge of PR #594) |
| This round's frozen control plane | `preregistration.md`, blob `b8168df9ed1acff21eb89e84487b43470124f845` |
| Single-map dilation uniqueness, kernel | `verification/lean-mathlib/OIBridge/StinespringUniqueness.lean`, blob `5bb228363ea8708225fbd7d49a3375fae2c08435` (`stinespringChannel`, `krausOf`, `channel_eq_krausMap`) |
| Kraus-family uniqueness, kernel | `verification/lean-mathlib/OIBridge/KrausUniqueness.lean`, blob `217031c5e394e5c0ccece99ff45fcf9e46525539` (`krausMap`, `krausMap_single`) |
| Equal-environment right-unitary uniqueness, kernel | `verification/lean-mathlib/OIBridge/UhlmannUniqueness.lean`, blob `5b35b10bd7df5fa16ce710ee5285289438afa900` (`rightUnitary_of_gram`) |
| The substratum interface, unmodified | `verification/lean-mathlib/OIBridge/SubstratumInterfaceAudit.lean`, blob `56a0e4800c08e9a015ce4bc7da4d74aa3ea471b8` |
| This round's module | `verification/lean-mathlib/OIBridge/SemigroupTransfer.lean` |

Every blob the freeze's start-state table pins is present at the base with the pinned identity,
with **one recorded discrepancy**: the freeze pins `verification/ROADMAP.md` at blob `3965d930…`
and the base carries `27c29ee5…` — the act 12 propagation, merged between the freeze's authoring
and its merge. The P1 row *Substratum Lemma 24.1 — semigroup transfer* and its section are
byte-identical in the two blobs. The preregistration is not edited; the discrepancy is recorded
here and nowhere repaired. `proposition_9_7b`, `kraus_uniqueness`, `rightUnitary_of_gram` and
`stinespring_scope_probe.py`'s contracts are consumed as they stand and none is revised.

**Track B and Track I are not touched**, in either direction. Nothing from act 11 or act 12 is
consumed as evidence, and act 7's entry formula for a permutation matrix is re-proved locally
(`permMatrix_entry`) so that no Track B module is imported.

## Outcome, in one line

**`ST0`–`ST4` landed; `ST5` necessity landed; `ST5` sufficiency is UNDECIDED.** `ST0`, `ST1` and
`ST1′` positively; `ST2`, `ST3` and `ST4` NEGATIVELY, each by a trace certificate proved in the
kernel; `ST5` exactly at its frozen fallback — necessity at level 2, sufficiency UNDECIDED with the
obstruction named. Every target is at evidence level 2 at the strength the freeze predicted, with
one prediction exceeded in a direction that costs nothing: `ST0(c)` was predicted at high strength
with a possible formal obstruction to record, and it was reached in full — the identification of
GNS cyclicity with trivial hidden commutant is a kernel theorem in both directions. Nothing else
moved from its predicted strength.

**The central result, at the strength jointly reached:** the visible channel family does not
determine the underlying dilation up to a single time-independent hidden conjugation, even under
the frozen GNS-cyclic reading and the frozen decoupled-enlargement control. The present
semigroup-transfer proof route therefore does not establish completeness of `𝒢_sub`. Equality of
all block-word traces is necessary for hidden conjugation, but this round does not establish that
it is sufficient. Consequently the P1 completeness obligation remains OPEN, with stronger
multi-time information or a different proof route required.

The mechanism, in one sentence: **the family carries only the sorted balanced word data and not
the interleaved multi-time data**, and Pair C is a pair of six-element substrata, both with trivial
hidden commutant, with the same family at every time and different interleaved data.

### Three boundaries, stated once and kept everywhere below

1. **Lemma 24.1 is not called false without qualification.** Its proposed transfer from the
   visible channel family to one common hidden conjugation is refuted on the tested readings —
   the literal reachable-cyclic reading, the GNS-cyclic reading, and the reading up to visible
   relabelling and decoupled enlargement; the broader completeness theorem could still have
   another proof.
2. **`ST5` does not repair the lemma.** Since sufficiency is UNDECIDED, full word-trace data is
   currently a candidate strengthened hypothesis, not a certified repair.
3. **The four gauge generators are not called incomplete.** Pair C escapes the frozen treatments
   of generators (i) and (iii), but the round deliberately says nothing about (ii)/(iv), so
   exhaustiveness remains neither proved nor refuted.

## `ST0` — the setting: the substratum family is an instance of the merged idiom

`familyAt`, `visibleBlock`, `familyAt_single`, `amplitude_gram_entry`, `purifiedIsometry_apply`,
`familyAt_eq_stinespringChannel`, `ST0c_cyclic_iff`, with `krausOf_toEuclideanLin`, `krausMap_smul`,
`sqrt_scalar_sq`, `mul_singleKron_apply`, `singleKron_mul_apply`, `eq_oneKron_of_comm`, `slice_comm`,
`hiddenKron_comm_enlarge`, `enlarge_unitary`, `one_kronecker_sub`, `separating_of_hct`,
`hct_of_separating` and `starProjection_comm` as the mechanism.

1. **`ST0(b)`, the block-trace form.** `familyAt U t` is the uniform-prior family
   `Φ_t(ρ) = Tr_H[U^t (ρ ⊗ 𝟙/m) U^{-t}]`, written as the `m²`-member Kraus map with operators
   `(U^t)(·, h)(·, h')` indexed by `H × H` and the scalar `1/m` in front. `familyAt_single` is the
   frozen identity `Φ_t(E_{ab})_{cd} = (1/m) · Tr[(U^t)_{ca} ((U^t)_{db})ᴴ]`, and
   `familyAt_eq_of_blockTraces` records its consequence: **family equality is equality of the
   sorted balanced word traces** `Tr[(U^t)_{ca}((U^t)_{db})ᴴ]`, and nothing more. The Gram entry of
   the amplitude matrix is the same block trace (`amplitude_gram_entry`).
2. **`ST0(a)`, the purification.** On the carrier `V × (H × H')` with `H' = H`, the matrix
   `m^{-1/2} (U^t)(a, h)(b, h')` applied to `ψ` is `U^t ⊗ 𝟙_{H'}` applied to `ψ ⊗ Ω` with
   `Ω = m^{-1/2} Σ_h |h⟩|h⟩` (`purifiedIsometry_apply`), and the uniform-prior family is exactly the
   merged module's `stinespringChannel` of that isometry, for every `t`
   (`familyAt_eq_stinespringChannel`). **The reference state of the substratum is mixed**, and the
   purified environment has dimension `m²`, not `m`.
3. **`ST0(c)`, GNS cyclicity is trivial hidden commutant — at level 2, in both directions.**
   `ST0c_cyclic_iff`: for unitary `U`, `HiddenCommutantTrivial U` holds **iff** every subspace of
   `ℂ^{V × (H × H')}` that contains every `ψ ⊗ Ω` and is invariant under every `X ⊗ 𝟙`, under
   `U ⊗ 𝟙_{H'}` and under `(U ⊗ 𝟙_{H'})ᴴ` is the whole space. The proof is the frozen one and no
   other: the commutant of `B(ℋ_V) ⊗ 𝟙` is `𝟙 ⊗ B(ℋ_H ⊗ ℋ_{H'})` (`eq_oneKron_of_comm`), each primed
   slice of a commuting `𝟙 ⊗ Z` lies in the hidden commutant of `U` (`slice_comm`), so with a
   trivial hidden commutant the reference is separating for the commutant of the generating set
   (`separating_of_hct`), and conversely a non-scalar `Y` in the hidden commutant gives the nonzero
   commutant element `𝟙 ⊗ (Y ⊗ 𝟙 − 𝟙 ⊗ Yᵀ)` that kills every `ψ ⊗ Ω` (`hct_of_separating`). The step
   the freeze flagged as possibly exceeding the round — that a reference is cyclic for a `*`-closed
   set iff it is separating for its commutant — is carried by `starProjection_comm`: the orthogonal
   projection onto a subspace invariant under `A` and `A†` commutes with `A`, so `𝟙 − P` is a
   commutant element vanishing on the reference and hence zero. **The two cyclicity notions are
   different**: `𝒞_B = 𝒞_H` holds on every permutation instance by the definition of the reachable
   span under a full-support prior, and is not a hypothesis of any theorem here; GNS cyclicity is
   `HiddenCommutantTrivial`, and Pair A below satisfies the first and fails the second.

## `ST1` and `ST1′` — Reading A from merged inputs, stated as per-time and no more

`readingA_perTime`, `familyAt_hiddenConjugate`, `hiddenConjugate_family`, with `conj_pow`,
`hiddenKron_unitary`, `krausMap_mix`, `mixing_unitary`, `hiddenKron_mul_apply`,
`mul_hiddenKron_conjTranspose_apply` and `kraus_hiddenConjugate` as the mechanism.

1. **`ST1`.** If `Φ^U_t = Φ^{U'}_t` for every `t`, then **for each `t` separately** there is a unitary
   `W_t` on the purified environment `ℂ^{H × H}` with `X'_t = X_t W_t`, `X_t` the
   `(n × n) × (H × H)` amplitude matrix `m^{-1/2}(U^t)(a, h)(b, h')` of the Kraus family of `Φ_t` —
   by `ST0(b)` and `rightUnitary_of_gram`, with `m ≥ 1`. **The existential is inside the `∀ t`.
   Nothing in Reading A makes `W_t` constant in `t`, nor of the product form `W ⊗ W̄`**, and `ST3`
   exhibits a pair with equal families on which no single hidden `W` exists at all.
2. **`ST1′`, the soundness control.** Hidden conjugation `U' = (𝟙 ⊗ W) U (𝟙 ⊗ W)ᴴ` preserves the
   family at every `t`: on the purified environment it is Kraus mixing by the single,
   time-independent, product unitary `W ⊗ W̄` (`kraus_hiddenConjugate`, `mixing_unitary`), and Kraus
   mixing by a unitary leaves the map unchanged (`krausMap_mix`). This is the direction the
   completeness argument does **not** need; it is recorded as the control the freeze asked for.

## `ST2` — Reading B as literally stated, refuted on Pair A, with the absorption

`ST2_pairA`, with `pairA_blocks`, `adj_literals`, `pow_involution`, `familyAt_involution_eq`,
`familyAt_eq_of_blockTraces`, `trace_visibleBlock_hiddenConjugate` and `visibleBlock_conj` as the
mechanism.

**NEGATIVE, at full strength, as predicted.** Pair A is `φ(v, h) = (v, h ⊕ v)` and
`φ'(v, h) = (v, h ⊕ v ⊕ 1)` on `ℤ₂ × ℤ₂`, pinned inside the statement by `U = φ̂` and `U' = φ̂'`. Both
are involutions, so `familyAt_involution_eq` reduces family equality at every `t` to the sixteen
block traces at `t = 1`, which agree. **No hidden unitary conjugates one to the other on the fixed
carrier**: the `(0,0)` visible block of `φ̂` is `𝟙` and that of `φ̂'` is `X`, hidden conjugation
preserves each block's trace (`trace_visibleBlock_hiddenConjugate`), and `Tr 𝟙 = 2 ≠ 0 = Tr X`.
The theorem's conclusion is `¬ HiddenConjugate U U'` — a universal over `W`, never a failed search.

**The absorption is proved in the same theorem**: `φ̂' = (X ⊗ 𝟙) φ̂ (X ⊗ 𝟙)` is its last conjunct.
So the bounded reading, in the freeze's words: **step (2)'s conclusion, as written, fails on a
two-qubit substratum pair; exhaustiveness is untouched by this pair**, because generator (i)'s
visible part relates it. The `(i)+(iii)` absorption of Pair A is not formalized; nothing rests on
it. Both hidden commutants of Pair A contain `X`, so neither is GNS-cyclic, and Pair A separates
the two cyclicities exactly as the freeze said it would.

## `ST3` — Reading B under GNS cyclicity, refuted on Pair C

`ST3_pairC`, with `pairC_blocks`, `pairC_hct`, `pairC'_hct`, `pairC_family`,
`hiddenKron_mul_permMatrix`, `permMatrix_mul_hiddenKron`, `permMatrix_mul_self` and
`permMatrix_conjTranspose_self` as the mechanism.

**NEGATIVE, at full strength, as predicted.** Pair C on `ℤ₂ × ℤ₃`: `φ` exchanges `(0,2) ↔ (1,0)` and
`(1,1) ↔ (1,2)` and fixes `(0,0)`, `(0,1)`; `φ'` additionally exchanges `(0,0) ↔ (0,1)`. The theorem
carries, as conjuncts of one statement:

1. **both hidden commutants are trivial** — `pairC_hct` and `pairC'_hct` eliminate the `3 × 3`
   unknown `Y` from eight entries of the commutation equation, forcing every off-diagonal entry to
   vanish and the three diagonal entries to agree; so both instances are GNS-cyclic by `ST0(c)`;
2. **the families are equal at every `t`** — both are involutions and the sixteen block traces
   agree at `t = 1` (`pairC_family`);
3. **the visible statistics are non-trivial** — `Φ_1(E_{00}) = diag(2/3, 1/3)`, the classical
   symmetric channel `[[2/3, 1/3], [1/3, 2/3]]` composed with full dephasing, so this is not a pair
   the family fails to see because the family is degenerate;
4. **no unitary whatsoever conjugates one to the other on the fixed carrier** — `Tr φ̂ = 2 ≠ 0 = Tr φ̂'`,
   and the trace is invariant under every unitary conjugation `G U Gᴴ`, so hidden conjugation,
   visible relabelling, their products, and every generator-(i) relabelling of `V × H` are excluded
   at once.

**This is the target that decides the manuscript's expected mechanism**: the GNS-cyclic reading
of step (2) — the reading the argument's own words point to — is refuted on a six-element
substratum with non-trivial visible statistics. The mechanism is a hidden involution acting inside
one visible fibre and commuting with `φ̂`, which the dephasing family cannot see. The secondary
inverse-pair witness on `ℤ₂ × ℤ₂` is not formalized; it is a toy time-reversal pair and nothing
rests on it.

## `ST4` — the (i)+(iii) orbit, refuted on Pair C by a balanced word

`ST4_pairC`, with `wordEval`, `enlarge`, `pairC_wordTraces`, `visibleBlock_enlarge`,
`wordEval_enlarge`, `deltaWord_balanced`, `trace_wordEval_enlarge`, `sandwich_mul`, `wordEval_conj`
and `trace_wordEval_conj` as the mechanism.

**NEGATIVE, at full strength — the freeze predicted high, and the two reasons it gave for
stopping short of full are both discharged in the kernel.** For Pair C: for every finite non-empty
`D`, every pair of unitaries `δ, δ'` on `ℂ^D`, every visible permutation `σ` of `ℤ₂` and every
hidden unitary `W` on `ℂ^{H × D}`,

    U' ⊗ δ' ≠ (P_σ ⊗ W)(U ⊗ δ)(P_σ ⊗ W)ᴴ.

The certificate is the balanced word `w₀ = U₀₀ U₁₀ U₀₁ U₀₀ᴴ U₀₁ᴴ U₁₀ᴴ`, with `Tr[w₀(φ̂)] = 1` and
`Tr[w₀(φ̂')] = 0`, and its swap-relabelling `w₁`, with `Tr[w₁(φ̂')] = 0` (`pairC_wordTraces`). The two
general lemmas the freeze named are theorems here: **the enlargement lemma**
`trace_wordEval_enlarge` — for a balanced word `w` and unitary `δ`, `Tr[w(U ⊗ δ)] = |D| · Tr[w(U)]`,
because the `δ`-letters of a balanced word multiply to `δ^{net} = δ^0 = 1` in the unit group
(`deltaWord_balanced`) — and **the relabelling lemma** `trace_wordEval_conj` — the word value of
`(P_σ ⊗ W) U (P_σ ⊗ W)ᴴ` is `W · w_σ(U) · Wᴴ` with `w_σ` the word relabelled by `σ`, so its trace is
`Tr[w_σ(U)]`. Both visible relabellings are checked: at `σ = id` the word `w₀` gives
`|D| · 0 = |D| · 1`, at `σ = swap` the word `w₁` gives `|D| · 0 = |D| · 1`, and `|D| ≠ 0`.

**The frozen deep-sector model is stated in the theorem and is the only one this round bounds**:
an exact product `U ⊗ δ` with a decoupled factor of equal total size on both sides, re-indexed onto
`V × (H × D)` so that `H × D` is the enlarged hidden factor. Approximate decoupling and unequal
sizes are outside it. Unbalanced words carry `Tr[δ^j]` and are not enlargement-stable; only
balanced words are used. **This is the target that bounds the lemma's "up to
enlargement/reduction of the deep sector" clause**: the clause absorbs Pair A (recorded, `ST2`) and
Pair B (recorded in the freeze, not formalized here) and does not absorb Pair C.

## `ST5` — the positive branch, at its frozen fallback

`trace_wordEval_hiddenConjugate`.

**Necessity, at level 2.** Hidden conjugation preserves every block-word trace — every word,
balanced or not, on every carrier. **Sufficiency is UNDECIDED, and the obstruction is the one the
freeze named**: the statement that equal word traces on the algebra generated by `B(ℋ_V) ⊗ 𝟙` and
`U^{±1}` make `w(U) ↦ w(U')` a trace-preserving `*`-isomorphism of the generated algebras
implemented by a hidden unitary needs the trace-form kernel argument and the unitary
implementation of a trace-preserving `*`-isomorphism between `*`-subalgebras of `M_m(ℂ)`, neither
of which Mathlib or the corpus carries; it was not attempted, and **necessity at level 2 is not
sufficiency and is not promoted**. `ST5` is what a corrected transfer lemma would rest on; its
hypothesis is **strictly stronger than the family**, and `ST3`/`ST4` witness exactly the gap.

## The post-round sentence, at the strength jointly reached

`ST2`, `ST3` and `ST4` landed, so the frozen sentence is asserted at full strength: fixing the
visible channel family fixes the substratum dilation at each time up to a time-dependent
Kraus-mixing unitary, and does **not** fix the dilating unitary up to hidden conjugation — not on
the reachable-cyclic reading, not on the GNS-cyclic reading, and not up to decoupled deep-sector
enlargement — because the family carries only the sorted balanced word data and not the
interleaved multi-time data. **The present completeness proof therefore remains conditional**:
equality of the visible channel family does not supply the semigroup-transfer conclusion as
stated. Repairing this route requires stronger multi-time data — such as `ST5`'s full word-trace
hypothesis — or a different argument. **This round does not prove that stronger data are
necessary for completeness itself**: `ST2`–`ST4` show what the present route needs, not what every
possible completeness proof needs.

## What the outcomes do not license

- **Nothing here says the four families fail to exhaust `𝒢_sub`, and nothing here says they do.**
  A negative `ST2` is absorbed by (i). A negative `ST3`/`ST4` shows the lemma's *route* does not
  deliver completeness and that Pair C escapes (i) and (iii) at the frozen exact-decoupling
  reading; it says **nothing** about (ii) and (iv), which have no meaning on a six-element carrier.
  The permitted sentence is "the present completeness proof remains conditional, and repairing
  its route needs stronger multi-time data or a different argument"; the forbidden sentences are
  "completeness is false", "completeness holds", and "completeness itself requires stronger data
  than the lemma names".
- **Nothing about Bell or H-Bell.** Theorem 23 already keeps Bell-inclusive uniqueness outside the
  lemma's scope; this round does not enter it.
- **Nothing about A6.** The A1–A6 package and its `GAP` row are untouched.
- **Nothing about Track B's `P0`**, in either direction, and nothing imported from acts 11 or 12.
- **No manuscript claim changes in this round.** `papers/` and `book/` are untouched. Whether and
  how to propagate is a separate owner call after the execution; the words "corrected lemma" name
  a possible future object, not a manuscript statement.
- **Nothing about the physical substratum.** The witnesses are toy carriers. Whether the wave rule
  on the cubic lattice has a trivial hidden commutant, and what its family determines, is not
  asked.
- **Nothing about approximate deep sectors.** The exact-decoupling reading is what step (3)
  invokes and what `ST4` bounds.
- **Nothing about time reversal in general.** The secondary inverse-pair witness is not
  formalized; the manuscript's subsumption of `φ → φ^{-1}` under (i) is neither confirmed nor
  refuted.
- **No selection principle is named.** The P1 row's status label stays **OPEN**: a negative on the
  lemma's route is not an impossibility theorem for the obligation.

## Definition budget: **SIX of the frozen six slots fire**

`familyAt` (slot 1), `HiddenCommutantTrivial` (slot 2), `HiddenConjugate` (slot 3), `visibleBlock`
(slot 4), `wordEval` (slot 5, conditional — **fired**, because `ST4`'s statement quantifies over
every enlargement and every relabelling and its certificate is stated on a six-letter word under
two relabellings, which an inline `List.prod` would not keep readable), `enlarge` (slot 6,
conditional — **fired**, because `ST4`'s statement re-indexes `U ⊗ δ` onto `V × (H × D)` and the
`Matrix.reindex` of a `Matrix.kroneckerMap` inline would not be readable). **No seventh definition
was introduced.** The witness permutations of Pairs A and C and the reference vector `ψ ⊗ Ω` are
`local notation` — syntax, not declarations — and each witness is pinned by an equation
`U = φ.permMatrix ℂ` inside the statement that needs it; no witness pair, no `W`, no carrier, no word
and no enlargement is a top-level definition. The merged modules' definitions are reused, not
redefined.

Hypotheses on the carrier sizes, all frozen: `m ≥ 1` (`[Nonempty H]`) in `ST1` and `ST0(c)`, `n ≥ 1`
(`[Nonempty V]`) in `ST0(c)`, and `|D| ≥ 1` (`[Nonempty D]`) in `ST4`, since an empty deep sector
makes both sides the empty matrix.

## Chronology certification

Guard `R7-SGT` in `verification/lean/edge_rigidity_probe.py` pins this file's preregistration by
content — blob `b8168df9ed1acff21eb89e84487b43470124f845` — and certifies act 10's strengthened
ancestry predicate with the real execution head: `pull_request.head.sha` from the Actions event
payload in PR CI and `HEAD` locally, never the synthetic merge commit; `B = c46e1606…` an ancestor
of the head **and every commit of `git rev-list H ^B` itself a descendant of `B`**, recovering
whatever history it needs and failing closed when it cannot. **The property certified is that no
commit reachable from the execution head lies outside the control-plane merge's descendants.**
What it does not certify: that the merged preregistration was authored before the analysis it
records (the freeze itself carries the recorded analysis, by design), that no execution-specific
object existed outside the repository before the freeze, or anything about branches the head does
not reach. The claim is scoped to the repository record; commit SHAs locate, blob SHAs are what is
pinned.

## Axiom table

Sixty-one named results, one `#print axioms` line each at the foot of the module, every one
printing exactly `[propext, Classical.choice, Quot.sound]`; no `sorry`, no `axiom`, no
`native_decide`.

| result | target | axioms |
| --- | --- | --- |
| `enlarge_apply` | mechanism | `[propext, Classical.choice, Quot.sound]` |
| `visibleBlock_apply` | mechanism | `[propext, Classical.choice, Quot.sound]` |
| `visibleBlock_enlarge` | `ST4` | `[propext, Classical.choice, Quot.sound]` |
| `familyAt_single` | `ST0(b)` | `[propext, Classical.choice, Quot.sound]` |
| `amplitude_gram_entry` | `ST0(b)`/`ST1` | `[propext, Classical.choice, Quot.sound]` |
| `krausOf_toEuclideanLin` | `ST0(a)` | `[propext, Classical.choice, Quot.sound]` |
| `krausMap_smul` | `ST0(a)` | `[propext, Classical.choice, Quot.sound]` |
| `sqrt_scalar_sq` | `ST0(a)` | `[propext, Classical.choice, Quot.sound]` |
| `purifiedIsometry_apply` | `ST0(a)` | `[propext, Classical.choice, Quot.sound]` |
| `familyAt_eq_stinespringChannel` | `ST0(a)` | `[propext, Classical.choice, Quot.sound]` |
| `readingA_perTime` | `ST1` | `[propext, Classical.choice, Quot.sound]` |
| `conj_pow` | `ST1′` | `[propext, Classical.choice, Quot.sound]` |
| `hiddenKron_unitary` | `ST1′` | `[propext, Classical.choice, Quot.sound]` |
| `krausMap_mix` | `ST1′` | `[propext, Classical.choice, Quot.sound]` |
| `mixing_unitary` | `ST1′` | `[propext, Classical.choice, Quot.sound]` |
| `hiddenKron_mul_apply` | mechanism | `[propext, Classical.choice, Quot.sound]` |
| `mul_hiddenKron_conjTranspose_apply` | mechanism | `[propext, Classical.choice, Quot.sound]` |
| `kraus_hiddenConjugate` | `ST1′` | `[propext, Classical.choice, Quot.sound]` |
| `familyAt_hiddenConjugate` | `ST1′` | `[propext, Classical.choice, Quot.sound]` |
| `hiddenConjugate_family` | `ST1′` | `[propext, Classical.choice, Quot.sound]` |
| `permMatrix_entry` | mechanism | `[propext, Classical.choice, Quot.sound]` |
| `visibleBlock_conj` | `ST2`/`ST4` | `[propext, Classical.choice, Quot.sound]` |
| `sandwich_mul` | `ST4` | `[propext, Classical.choice, Quot.sound]` |
| `wordEval_conj` | `ST4` | `[propext, Classical.choice, Quot.sound]` |
| `trace_wordEval_conj` | `ST4` | `[propext, Classical.choice, Quot.sound]` |
| `wordEval_enlarge` | `ST4` | `[propext, Classical.choice, Quot.sound]` |
| `deltaWord_balanced` | `ST4` | `[propext, Classical.choice, Quot.sound]` |
| `trace_wordEval_enlarge` | `ST4` | `[propext, Classical.choice, Quot.sound]` |
| `trace_wordEval_hiddenConjugate` | `ST5` necessity | `[propext, Classical.choice, Quot.sound]` |
| `pow_involution` | `ST2`/`ST3` | `[propext, Classical.choice, Quot.sound]` |
| `familyAt_involution_eq` | `ST2`/`ST3` | `[propext, Classical.choice, Quot.sound]` |
| `permMatrix_mul_self` | `ST2`/`ST3` | `[propext, Classical.choice, Quot.sound]` |
| `permMatrix_conjTranspose_self` | `ST2`/`ST3` | `[propext, Classical.choice, Quot.sound]` |
| `krausMap_expand` | `ST0(b)` | `[propext, Classical.choice, Quot.sound]` |
| `familyAt_expand` | `ST0(b)` | `[propext, Classical.choice, Quot.sound]` |
| `familyAt_eq_of_blockTraces` | `ST0(b)` | `[propext, Classical.choice, Quot.sound]` |
| `hiddenKron_mul_permMatrix` | `ST3` | `[propext, Classical.choice, Quot.sound]` |
| `permMatrix_mul_hiddenKron` | `ST3` | `[propext, Classical.choice, Quot.sound]` |
| `trace_visibleBlock_hiddenConjugate` | `ST2` | `[propext, Classical.choice, Quot.sound]` |
| `pairA_blocks` | `ST2` | `[propext, Classical.choice, Quot.sound]` |
| `pairC_blocks` | `ST3`/`ST4` | `[propext, Classical.choice, Quot.sound]` |
| `adj_literals` | `ST2`–`ST4` | `[propext, Classical.choice, Quot.sound]` |
| `ST2_pairA` | `ST2` | `[propext, Classical.choice, Quot.sound]` |
| `pairC_hct` | `ST3` | `[propext, Classical.choice, Quot.sound]` |
| `pairC'_hct` | `ST3` | `[propext, Classical.choice, Quot.sound]` |
| `pairC_family` | `ST3` | `[propext, Classical.choice, Quot.sound]` |
| `ST3_pairC` | `ST3` | `[propext, Classical.choice, Quot.sound]` |
| `pairC_wordTraces` | `ST4` | `[propext, Classical.choice, Quot.sound]` |
| `ST4_pairC` | `ST4` | `[propext, Classical.choice, Quot.sound]` |
| `mul_hiddenKron_apply` | `ST0(c)` | `[propext, Classical.choice, Quot.sound]` |
| `mul_singleKron_apply` | `ST0(c)` | `[propext, Classical.choice, Quot.sound]` |
| `singleKron_mul_apply` | `ST0(c)` | `[propext, Classical.choice, Quot.sound]` |
| `eq_oneKron_of_comm` | `ST0(c)` | `[propext, Classical.choice, Quot.sound]` |
| `slice_comm` | `ST0(c)` | `[propext, Classical.choice, Quot.sound]` |
| `hiddenKron_comm_enlarge` | `ST0(c)` | `[propext, Classical.choice, Quot.sound]` |
| `enlarge_unitary` | `ST0(c)` | `[propext, Classical.choice, Quot.sound]` |
| `separating_of_hct` | `ST0(c)` | `[propext, Classical.choice, Quot.sound]` |
| `one_kronecker_sub` | `ST0(c)` | `[propext, Classical.choice, Quot.sound]` |
| `hct_of_separating` | `ST0(c)` | `[propext, Classical.choice, Quot.sound]` |
| `starProjection_comm` | `ST0(c)` | `[propext, Classical.choice, Quot.sound]` |
| `ST0c_cyclic_iff` | `ST0(c)` | `[propext, Classical.choice, Quot.sound]` |

## Discipline

- **It touches no manuscript.** `papers/Substratum.md`, `papers/Structure.md`,
  `papers/Complexity.md` and every other manuscript are read, not edited.
- **It changes no status label.** The P1 row stays **OPEN**; its section is sharpened.
- **It names no selection principle.**
- **It imports neither act 11 nor act 12**, and consumes `proposition_9_7b` only as the per-map
  input it is; its independence hypothesis is not this round's cyclicity.
- **It says nothing about Track I**, and nothing about (ii) or (iv).
