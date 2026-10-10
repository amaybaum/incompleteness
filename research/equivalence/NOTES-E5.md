# NOTES-E5 — λ's sourcing and the three-token structure

Base L = `9f9f8257`. λ is the four-token coherence premise of the design-run theorem
`OIBridge.FourCopy.kt4_forward_ie1` (`FourCopyHeadline` at `ff9c3a35`), audited hypothesis by hypothesis by the landed
round KT4-PREM-1 (receipt at L; result note `verification/programmes/oi-qm/reconstruction/round-kt4-prem-1-premise-audit/
result.md`, cited [K-record]); its premise ledger is `research/archive/eq5/F/ASSUMPTIONS.md` and the source audit
`research/archive/eqreview/EQ5-SOURCE-AUDIT.md` [A].

## 1. The statement and what λ is

```lean
kt4_forward_ie1 (K : Pr → Set (W 3)) (N : Pr → W 3 ≃ₗ[ℝ] W 3) (A B A' B' : Pr → E3)
  (hcls : ∀ p, NClass (N p) (A p) (B p) (A' p) (B' p)) (hadm : ∀ p, PairAdm (K p))
  (hcl : ∀ p, IsClosed (K p)) (hgate : ∀ p, ∀ ω ∈ K p, N p ω ∈ K p)
  (H : KT4Core (K .p01) (K .p23) (K .p02) (K .p13) V) :
  (∀ p, IE1 (K p)) ∧ EvenCycle (fun p => orient (A p) (B p))
```

`KT4Core` (FourCopyCore at `ff9c3a35`, archived `research/archive/pt/inputs/fourcopy/FourCopyCore.lean:99`) carries two
product structures on one carrier `V` — `stA`, `effA` for the grouping `01|23` and `stB`, `effB` for `02|13` — with the
evaluation laws, two positivity fields (`posBA`: products of `02|13` effects are nonnegative on `01|23` products of pair
states; `posAB` the converse) and two token fields:

```lean
tokA : ∀ a b c d : Fin 4, ∀ x ∈ pairBody K01, ∀ y ∈ pairBody K23,
  effA (tabCoord a b) (tabCoord c d) (stA x y) = effB (tabCoord a c) (tabCoord b d) (stA x y)
```

(and `tokB` on `stB x y`): **the single-token coordinate table `(a, b, c, d)` of a four-token product state is the same
whichever grouping reads it.** λ is `KT4Core` with `tok`.

## 2. No structure with three or more tokens at L

[K-reading at L] No declaration of the kernel at L takes three or more copies: the search for multi-token carriers,
stage products and iterated composites (`FiniteStage.prod`, `DirectedStages.prod`, any `Fin 4 → Fin 4 → Fin 4`-indexed
table) finds only DIM-1's two-token index tables `pc`, `pt` (CompositeDimension.lean:744, :751); COMP-1's header places
the stage-level product outside its module; the only `DirectedStages` values are the controls `badD`, `bitTower`, `midD`
(KT4-PREM-1 Q2). The S0 census at `bcbc516f` [A, `eq5/SOURCE/s0_census`] applies unchanged: L's
`verification/lean-mathlib` tree is byte-identical to `bcbc516f`'s (`git diff --stat bcbc516f 9f9f8257 --
verification/lean-mathlib` is empty).

## 3. What a three-token carrier would need to be, and whether `tok` can be sourced from it

**The shape (written).** A k-token carrier would need, for every bipartition of the k tokens into two parts, a COMP-1
pre-composite structure on **one** carrier with **one** body whose factors are the bodies of the parts (KT∞, "every
grouping of a finite family of systems into two parts is a valid composite", EQ2 §5 [A]), and the coherence of the
single-token coordinates across groupings — the k-token analogue of `tok`. At three tokens the groupings are `1|23`,
`12|3`, `13|2`; at four, KT4Core uses `01|23` and `02|13`.

**`tok` is a carrier property, `H`'s content is positivity across groupings.** On the multi-index table carrier — the
real functions on `(Fin 4)^k`, the k-token iterate of DIM-1's `W 3`, with each grouping read as a reshape and product
states and effects as tensor products of tables — the token clauses hold **by construction**: reading entry `(a, b, c, d)`
of `x ⊗ y` through `01|23` or through `02|13` reads the same number [W]. That carrier encodes **multi-token local
tomography** exactly as `W 3` encodes two-token local tomography (`W` CompositeDimension.lean:97). So `tok` is sourced
as far as multi-token LT is, which at L is not at all — it is a premise of the carrier. What remains of `H` once the
carrier is fixed is the pair of positivity fields, i.e. the cone-level condition FCC: under `hadm`, `H ⟺ FCC`, one
direction by Lemma B1 of the design modules and the other by an explicit carrier (KT4-PREM-1 Q1-MAP [K-record]). And
`tok` is not a vacuous convention: for the mismatched cones `(Q3, Q3, Q3, twin)` FCC fails at `−1/8`, so **no** carrier
carries `KT4Core` for them (model `M_tok`, KT4-PREM-1 [K-record]).

**Verdict on sourcing λ.** A three- or four-token structure supplying λ would have to supply (i) a joint carrier with
grouping-coherent single-token coordinates — multi-token LT, absent at L and, field-neutrally, the test locality of a
joint tower that no `DirectedStages` value at L provides (k2d D6 [A]) — and (ii) positivity of each grouping's product
effects on the other grouping's product states (FCC), the substantive content, for which no composition principle at L
is a source (KT4-PREM-1 open question 2). Relative to the rest of the theorem `tok` cannot be dropped (`M_tok`) and is not
necessary for given carrier data (`M_tokC`) [K-record]. Label: OPEN (λ unsourced); the reduction "`tok` holds by
construction on the multi-index table carrier, `H ⟺ FCC` there" is CONJECTURE [W] + [K-record].

## 4. Can the KT(4) route be re-derived at L?

**Tree identity [K-reading].** The merge base of `ff9c3a35` and L is `bcbc516f`; L changes nothing under
`verification/lean-mathlib` relative to it, and `ff9c3a35` adds exactly the eleven FourCopy modules and their import
lines. So design run 4 (run 37948419430, [A]) built `kt4_forward_ie1` over a kernel identical to L's.

**Re-derivation in this thread [D].** Branch `dev-equivalence/kt4-at-l` at `288f80ec` = this thread's checkpoint plus the
ten Pauli-free modules (blobs checked equal to `ff9c3a35`'s; `FourCopyPackage`, the sorry-carrying Pauli stage imported
by no headline module, omitted). Run 38084161796: RESULT-PENDING.

**What a certified re-derivation would and would not give.** Certifying `kt4_forward_ie1` at L needs a governed round
(registry family under §A.35; the release gate's `lean-manuscript` step fails on unregistered modules). It would certify
a conditional theorem whose five hypotheses are each unsourced on certified main (KT4-PREM-1 Q3 [K-record]); it would
move no status by itself. The shortest sourcing route the record names: a pair-level completion action (P-STAGE2 +
P-ACT2), which would supply `hcl` and `hgate` together but presupposes K2 (KT4-PREM-1 Q2).

## 5. Classification (§A.31)

ELABORATING: `tok` is located precisely (multi-token LT, carrier-level), the substantive residue is FCC, and the
re-derivation question is answered by tree identity plus a fresh design build. No NEW finding.
