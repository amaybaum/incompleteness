# P1: weighted channel application and convention check

**Status:** author-completed paper-only application check, awaiting independent non-author review. No new theorem is needed for the finite-dilation application specified below. This is a conditional mathematical application, not physical recovery or a claim that any native apparatus satisfies its inputs.

**Goal link — #1169:** determine whether the normalized weighted-prior realization already on main fits Main §3.2's channel presentation and its existing P-to-CP implication, without reproving the fixed-prior population identity or assuming total finiteness of nature.

**Authority:** owner `amaybaum`, 2026-11-16, [#1169 comment 6909675524](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-6909675524), records “Ok sounds good, proceed as suggested” and authorizes this bounded paper-only check against main at or after `32322301`, with independent review. A favourable “no new theorem required” outcome requires hypothesis-by-hypothesis review; it gives no physical recovery credit. No further proof attempt, Lean work, scientific computation or manuscript edit is authorized. The continuation is recorded in [comment 6910111269](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-6910111269).

## 1. Pinned sources and exact target

All primary source anchors in this document refer to main `32322301e4b8c54f000560db73201260c63bf7f8`. The accepted planning input is `RECOVERY-PLAN-r1.md` at research commit `708d11a53956cbadb6d67c8476bce7d0954f0f24`, §2; it is provenance for the task, not proof support. The technical application below is supported by the pinned main sources and the displayed finite sums.

Fix a nonempty finite visible set V and hidden set H, one bijection φ of V × H, and one probability mass function μ on H, independent of the prepared visible input. Write ρ_H = diag(μ). For an integer t ≥ 0 define the forward unitary by U|i,k⟩ = |φ(i,k)⟩ and

\[
\Phi_t(\rho)=\operatorname{Tr}_H\bigl[U^t(\rho\otimes\rho_H)U^{t\dagger}\bigr].
\]

The application target is this family at the declared integer times. It is not every CPTP family and is not a new construction on an infinite total carrier. The finite representative is mathematical data; choosing it makes no assertion about the cardinality of nature.

For a finite-horizon stochastic target, Main:520–524 supplies φ, H and a common μ reproducing its full law through K. That existence result is reused. Its φ and H may depend on the law and K. It supplies no single finite model for all horizons or all experimental settings. The law after K is unspecified by that target construction.

## 2. Weighted Kraus application and normalization

Main:282–284 gives the partial-trace channel and the uniform-prior Kraus presentation; Main:534–536 already states the general fixed-prior population identity. Applying the same finite partial-trace expansion to ρ_H = Σ_k μ(k)|k⟩⟨k| gives, with k the initial hidden index and l the final hidden index,

\[
 K^{(t)}_{kl}=\sqrt{\mu(k)}\, (I_V\otimes\langle l|)U^t(I_V\otimes|k\rangle),
 \qquad \Phi_t(\rho)=\sum_{k,l}K^{(t)}_{kl}\rho K^{(t)\dagger}_{kl}.
\]

The normalization check is

\[
\sum_{k,l}K^{(t)\dagger}_{kl}K^{(t)}_{kl}
=\sum_k\mu(k)(I_V\otimes\langle k|)U^{t\dagger}U^t(I_V\otimes|k\rangle)
=\Bigl(\sum_k\mu(k)\Bigr)I_V=I_V.
\]

These are the bounded application checks, using the finite basis resolution of identity and Main:268–270's permutation unitarity. Thus the standard Kraus criterion cited in Main:284 applies: the map is completely positive and trace preserving. The proof uses μ ≥ 0 for the square roots and Σ μ = 1 for trace preservation. Zero weights are permitted. Neither full support, an invariant prior, a maximally mixed prior nor a resetting bath is required. At t = 0 the same formula gives Φ_0 = id.

For μ(k) = 1/|H| this is exactly the displayed §3.2 formula. For the initialized ledger/clock slice of Main:524, zero weights outside the slice remain zero, but l still ranges over all final hidden states. For Main:522's arbitrary-kernel extension, the response-coordinate prior is a finite product of normalized kernels, with point masses on the initial ledger/clock. This satisfies positivity and normalization and is independent of X_0 by that construction; no rationality of μ is required. Arbitrary kernels at zero-probability histories are part of the chosen construction, not observed conditional probabilities there.

A general μ does not license the doubly stochastic or unital conclusions of a uniform-prior realization. No such conclusion is used here.

## 3. Population and matrix conventions

The manuscript's transition convention is **row = initial visible state, column = final visible state**:

\[
T_{ij}(t)=\langle j|\Phi_t(|i\rangle\langle i|)|j\rangle
=\sum_{k,l}\mu(k)|\langle j,l|U^t|i,k\rangle|^2.
\]

This is the existing Main:534–536 identity, with its weighted prior. In the unitary matrix, conversely, the row index is the output ket and the column index is the input ket: U_{p q} = 1[p = φ(q)]. These conventions are consistent and must not be identified merely because both matrices use two indices.

The Lean matrix convention requires an explicit inverse. In `verification/lean-mathlib/OIBridge/EquivalenceChain.lean:233–235`, `permConj_apply` states

`(ψ.permMatrix * M * (ψ⁻¹).permMatrix) p q = M (ψ p) (ψ q)`.

Consequently its `ψ.permMatrix` acts on column kets as the forward permutation ψ⁻¹. To represent the manuscript's forward φ in the definition `OIBridge.Phi` at :242–243, instantiate the Lean permutation parameter with **φ⁻¹**, and the complex weight with the real probability μ embedded in ℂ. Then its `(φ⁻¹)^t.permMatrix` is the manuscript's U^t. The right-hand factor is its inverse/adjoint. This is a dictionary check, not a source or Lean edit.

The direct unitarity witness `permMatrix_mem_unitaryGroup` (:179–185) quantifies over every finite permutation, so this substitution is allowed. `priorState` (:211) is diagonal by definition. `isDiag_Phi` (:253–254) also quantifies over every finite permutation and arbitrary complex weights, hence applies with φ⁻¹ and μ; its conclusion is algebraic diagonality, not positivity or normalization. Those probability conditions were checked separately above. No new Lean verification is claimed.

## 4. Hypothesis-by-hypothesis application table

“Satisfied” below refers only to the expressly specified representative. “Conditional” identifies a premise not supplied by this application. The independent reviewer must check both categories rather than treating the table as evidence of native physical realization.

| Hypothesis / source | Application and disposition |
| --- | --- |
| Finite product V × H and a bijection; Main:268–270 | Satisfied by the chosen data. For the process application, Main:520–524 supplies a finite reversible realization. Its n ≥ 2 and finite K hypotheses are retained when invoking that theorem. Total finiteness of nature is not invoked. |
| One common hidden prior, independent of the visible root; Main:520–524 | Satisfied in that process construction. The same μ is used for all initial basis states and all t; no fitting a separate prior at each root or time. For an arbitrary physical model this remains an input to be established. |
| μ real, nonnegative, normalized; Main:522/:524/:534 | Satisfied for the constructed product/slice probability. Required independently for any supplied μ. Complex weights in the Lean theorem alone would not suffice. |
| Product initial state ρ ⊗ ρ_H; Main:282/:534 | Part of the defined channel application. No channel assignment for arbitrary initial visible–hidden correlations is inferred. The correlated-law kernel `S_imp_D` is not used to establish this hypothesis. |
| Unitarity at compared times; Main:268–272 | Satisfied for integer powers of the one fixed permutation. A continuous interpolation and generator selection are unnecessary and not derived here. |
| Matching population family; Main:534–536 | Satisfied for the family generated by that same φ and μ. Equality to the target process is limited to its declared horizon and specified roots; zero-probability target roots require the construction's chosen extension, not a new empirical claim. |
| Computational diagonality; Main:326–328; `isDiag_Phi` | Satisfied because both the initial basis state and hidden prior are diagonal and the evolution permutes the basis; partial trace preserves diagonality. The inverse dictionary above aligns the formal witness. |
| P-indivisibility at a pair 0 < t₁ < t₂ in scope; Main:330–332 | **Conditional.** P1 supplies no witness for an arbitrary process. If such a pair is already established, the existing proof applies. Memory alone is insufficient; no recurrence premise is silently added. |
| A proposed CPTP intermediate map Λ; Main:332 | The assumption in the existing contradiction argument. Positivity and trace preservation make M_{kj} = ⟨j|Λ(|k⟩⟨k|)|j⟩ row-stochastic. Diagonality gives T(t₂) = T(t₁)M. Thus an established P-indivisible pair excludes such Λ. No converse is claimed. |

Main:332 already proves this implication on the diagonal-preserving family; `book/appendix-b-derivations.md:92–94` contains its uniform-prior presentation. Substituting the normalized weighted channel preserves the exact diagonal-preservation hypothesis consumed by that proof. The particular recurrence-based witness cited in the theorem statement is not required for its algebraic implication, and is not asserted for a finite accessible window without evidence.

## 5. Evidence levels, limits and disposition

**Author conclusion:** no new theorem is required for this normalized finite-dilation application. The Kraus weights and trace normalization are the displayed finite-sum application of Main's existing channel formula; the population identity and P-to-CP argument are already on main. The explicit φ⁻¹ dictionary resolves the matrix-orientation issue. This conclusion awaits independent checking of every row above.

This is a paper-level application with source-inspected formal witnesses for unitarity/diagonal preservation. It does not turn the weighted CPTP claim, the root-independent process construction or the P-to-CP proof into new kernel-certified results. The source's cited numerical/exact probes were read only as provenance and were not run; no new numerical evidence is offered.

The retained boundaries are substantive:

- Main:334's Hadamard example blocks extending the P-to-CP implication to arbitrary CPTP families. Here diagonal preservation is an actual hypothesis, not a generic quantum property.
- `verification/programmes/substratum/continuous-substates/infinite-xor-counterexample.md` records a common normalized infinite-carrier model with history memory and all-time P-divisible rooted maps. Its mathematical countercontrol is reused at its paper-proof scope; this check does not independently certify all infinite-carrier constructions.
- A family Φ_t from the common initial state is not the composition Φ_1^t with a reset environment. Its diagonal two-time maps alone do not give a sequential intervention instrument or reproduce arbitrary measurement protocols. The full passive history law is supplied by Main's particular common deterministic realization, not by multiplying the reduced channels.
- No native preparation, physical hidden-prior principle, quantum operation availability, Born-exponent selection, infinite-carrier extension, finite-bit accuracy theorem or full OI–QM equivalence follows. A1 remains open and unadopted; A4 is unchanged; physical source remains **NOT PASSED**.

The unit stops at the independent review of this application. An actual contradiction in a source hypothesis or dictionary would be reported as a scoped gap; no unapproved source correction, new proof programme or premise would be introduced to repair it.
