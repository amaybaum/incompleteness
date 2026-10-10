# EQ4-F preflight — hypothesis ledger (what the statements carry; what the run can and cannot show)

## Minimal headline `kt4_forward` (FourCopyPackage.lean)
Hypotheses, each explicit in the signature:
- `hcls`  N-CLASS per pair: N p = actC A ∘ actT B ∘ cnot ∘ actC A' ∘ actT B', orthogonal factors.
- `hadm`  PairAdm per pair: CandidateCone (products of ball states inside, K ⊆ maxCone) ∧ convex cone.
- `hcl`   closedness per pair (absent from the closure-level form `kt4_closure`).
- `hgate` gate preservation per pair.
- `hinv`  inverse-gate preservation per pair (inverse-gate duality; in the completed layer it enters only
          through `dualW_of_inv`).
- `H : KT4` two COMP-1 `PreComposite`s of the normalized pair bodies (fields: product data with
          `prodEff_apply`, `convex`, `prod_mem`, `prodEff_effect` over every `IsEffectOn` effect — the
          full-effect reading — and `prodEff_unit`), `one_body`, and `tok : TokenCoherent` (the four-token
          coherence clause, an explicit field).
Not hypotheses:
- four-copy local tomography (`Composite.lt`): absent from `KT4`; the convenience form `kt4_forward_lt`
  takes `Composite`s and is proved from `kt4_forward` by forgetting `lt` (`KT4LT.toKT4`).
- H-pairwise (IsNot/CtrlGate sourcing of N-CLASS): dropped; it was unused once N-CLASS is a hypothesis.
Built into the setting (cannot be dropped inside this formalization):
- two-copy local tomography of each pair: pair cones live in DIM-1's table carrier `W 3`, whose docstring
  states it encodes local tomography (CompositeDimension.lean, `W`).

## What a green build would establish, and what it would not
- Established: the statements elaborate; D and P's proofs check; their axiom reports (if standard)
  contain no `sorryAx`; `kt4_forward`'s proof composes Lemma B1 and Theorem C with every hypothesis
  passed through; `kt4_forward_lt` follows from `kt4_forward` with `lt` unused.
- Not established: KT(4) ⇒ IE₁ (Lemma B1, Theorem C and the heavy layer are open: 48 obligations);
  that any listed hypothesis is used inside the open proofs; that any hypothesis is necessary (P/A/C).
- Planned route for Lemma B1 (written, unchecked): uses prod_mem, prodEff_effect, prodEff_apply,
  bilinearity of prodEff, one_body, tok, PairAdm; not convex(Ω), not prodEff_unit, not lt.

## Lemma P (`kt4_parity_aligned`, FourCopyParity.lean, complete)
Uses: CandidateCone of each pair cone, aligned-gate preservation, `famI` once.
Does not use: convexity, closedness, inverse gate, `famII`, the COMP-1 bridge, local tomography,
complex numbers.
