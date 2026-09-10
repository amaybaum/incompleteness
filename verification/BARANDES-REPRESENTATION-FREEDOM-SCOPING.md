# Track B — representation-freedom scoping pass

Base: `main` at `55826721797780855ccb9f8157a0f96225b35012` (post-PR #562, act 2 closed at RT1).

**This is a scoping pass, not a round.** It adjudicates nothing, proves nothing, and preregisters
nothing. It exists because a proposed act 3 was about to be frozen around a construction the corpus
may not contain, and a frozen round that fails for want of a construction cannot distinguish *"we
cannot exhibit non-invariance"* from *"it is invariant"* — the same conflation that was removed from
that draft's `RU2` in review.

Nothing here is a theorem claim. Every entry records **what is proved, what is merely plausible, and
which**.

## The question being scoped

Act 3 was to ask whether the interference discrepancy of arXiv:2302.10778v3 §3.5 — the gap between
a rooted family and its would-be division through a candidate propagator — is a property of the
**stochastic family** or only of a **chosen quantum representation**.

Testing that adversarially needs two representations of *one* rooted family that differ in a way a
candidate extraction can see. So the prior question is: **what same-family freedoms does the merged
corpus actually prove?**

## 1. Inventory of merged same-family constructions

A "same-family freedom" here means a merged theorem supplying a **parameterized alternative
representation that preserves the family** — a construction taking a lawful `Q` and a parameter to a
lawful representation `Q'` with `∀ a t j, Q.rooted t a j = Q'.rooted t a j`, and exhibiting
representation-level variation for some choices of the parameter.

That is deliberately not "a theorem yielding `Q ≠ Q'`". `padData_rooted` proves the *family
equality*; it does not prove record inequality for every parameter, and at the trivial parameter the
padded record is a relabelling of the original. What makes padding a freedom is that some choices of
`W` do change operator content, which Arc D establishes separately.

| construction | location | same-family status | relates two representations? |
|---|---|---|---|
| **Ancilla padding** `padData Q Anc W w` | `OperationalSourcing.lean`, `padData_rooted` | **Proved**, for every finite ancilla, every unitary `W` on it, every weight `w` | **Yes** — this is the one genuine freedom |
| `permData R` | `QuantumRepresentationT3.lean`, `permData_rooted` | **Proved** equal to `rootedMap R` | **No** — constructs *one* representation from a realization |
| `hadData` | `QuantumRepresentationT2.lean`, `hadData_rooted` | **Proved** for the specific `pdFamily` | **No** — a single named witness |
| `unitData` | `OperationalSourcing.lean`, `unitData_rooted` | **Proved**, trivial carrier | **No** — a single named witness |
| `QfbData.condReal a K` | `QuantumRepresentation.lean` | `condReal_Bas`, `condReal_U`, `condReal_read` are `rfl` | **No** — same `Bas`, same `U`, same `read`; only `init` re-conditioned |
| `rootTraj_marginal` | `QuantumRepresentation.lean` | **Proved** | **No** — two descriptions of one `Q`, not two `Q`s |
| Carrier relabelling | `reindex_padUnit` (Arc D, internal step) | a reindexing lemma, used inside consequence 3 | **Not stated** as a same-family freedom on `QfbData` |
| Diagonal phase / gauge | — | **Not merged.** Hits for "phase", "gauge", "diagonal unitary" are in `CoherentLift`, `AntiunitaryInvariance`, `CongruentReconstruction`, `ControlLie` and others, none of which produce two `QfbData` with equal rooted families | **No** |
| `LabelInvariant` | `ImplementationLocality.lean` | a property of **implementation classes** | **No** — not about representations |

**Finding 1 (inventory).** Ancilla padding is the **only** merged theorem exhibiting a same-family
freedom with a free parameter. Everything else is either a single named witness, a re-description of
one representation, or a statement about a different kind of object.

This matches how Arc D's own preregistration frames it: padding is the construction proving that
operator content is not a function of the represented family.

## 2. Is padding inert at the candidate level?

Two natural extractions of a visible candidate propagator from a representation `Q` at `s < t`. Both
are Born-derived: `born b b' = ‖U b' b‖²`, and `bornPow`, `jointMass` and `rooted` are all built
from it. `QfbData` does expose `U` directly, so this is a property of the two rules examined here and
not a claim about every function definable from the structure.

**(a) Init-weighted.** Marginalize `bornPow (t−s)` over visible fibres using `Q.init`. This *is*
`Q.rooted (t−s)`. For two representations of the same family `Γ` it equals `Γ (t−s)` on both sides,
so it is **invariant by construction** — and therefore answers the invariance question by definition
rather than by discovery. An act 3 built on this extraction would be vacuous.

**(b) Uniform-on-fibre.** Weight each basis point over a visible value equally. This *looks*
representation-dependent: `padData` sets `read b = Q.read b.1`, so every fibre is multiplied by
`Anc`. But the padded weight is a product, `born` factorizes (`padData_born`:
`Q.born b b' * ‖W x' x‖²`), and the merged `sum_ancBorn` gives `∑_{x'} ancPow W t x x' = 1` from
unitarity of `W`. The ancilla marginalizes away to 1 regardless of the weighting.

**Finding 2 (provisional, evidence: reading of merged statements, not a proof).** Padding appears
**inert** at the candidate level for both natural extractions, and for the same structural reason in
each case: it preserves the family by preserving Born weights up to a factor that unitarity forces
to marginalize to one.

This is recorded as *provisional* deliberately. Establishing it is a proof obligation, not a scoping
observation, and the distinction is the point of this pass.

**Finding 3 (structural, and the reason Finding 2 is unlikely to be an accident).** Every visible
stochastic candidate extraction **identified in this scoping pass** is a function of Born weights.
`QfbData` exposes `U`, so this is not an exhaustive theorem about all definable extractions; the
unrestricted question stays at S3 below. A freedom that preserves the
rooted family does so either by preserving Born weights or by contributing a factor that
marginalizes. Diagonal-phase freedom illustrates the first case: `born` is `‖·‖²` and hence
phase-blind, so a phase freedom would be inert at the candidate level **even if it were merged**.
So adding more same-family freedoms of the merged kinds would not, by itself, make the invariance
question adversarial.

## 3. Search for a non-padding same-family pair

The useful object is not "another unitary exists" but a lawful alternative representation of the
*same* family whose difference a candidate extraction can see.

**None found in the merged corpus.** The named witnesses (`permData`, `hadData`, `unitData`) each
represent a *different* family from the others, so no two of them form a same-family pair. Padding is
the only parameterised construction, and §2 records it as apparently inert. No merged theorem
supplies a relabelling, gauge, phase, or alternate-dilation freedom on `QfbData` at all.

**This is an absence in the corpus, and no inference is drawn from it.** It does not show that no
such freedom exists mathematically, and it is not evidence for invariance.

## 4. Classification

Against the three scoping outcomes:

- **S1 — a usable non-padding freedom exists.** **Not supported.** None is merged.
- **S2 — all currently proved freedoms collapse at the candidate level.** **Supported, provisionally
  and for the merged freedoms only.** Padding is the sole proved freedom, and §2 finds it inert for
  both natural extractions, with §3's structural reason suggesting this is not accidental. The word
  "provably" in S2 is **not** earned here: that requires the theorems, which is a proof round.
- **S3 — the corpus has no theorem sufficient to decide.** **Partly true and worth stating
  separately**: the corpus decides nothing about freedoms it does not contain, so any claim of the
  form "the discrepancy is invariant under *all* representation freedom" is out of reach regardless
  of what a proof round establishes about padding.

**The classification is S2 for the merged freedoms, with S3 standing for the general question.**

## 5. What this implies for act 3, stated as implications and not as decisions

1. **Act 3 should not be an "invariance under representations" round.** Both of its outcomes would be
   reachable only through padding, and padding looks inert. `RU1` would fail for want of a
   construction, which is precisely the uninterpretable null this pass was run to avoid.
2. **A positive invariance theorem over the merged freedoms is within reach**, and would be an honest
   result: *the candidate discrepancy is unchanged under every same-family freedom this corpus
   proves.* It must be stated at exactly that scope, since §4's S3 half is permanent until more
   freedoms are merged.
3. **The live question moves one level earlier.** Extraction (a) is invariant by construction and
   extraction (b) by unitarity, but nothing in the corpus says which — if either — is the physically
   meaningful candidate. The rooted family does not determine that choice. So the missing ingredient
   on this route is a **candidate-selection principle**, and that can be established directly rather
   than inferred from a failed search.
4. **If a genuinely adversarial invariance round is wanted later**, it needs a same-family freedom
   that is not Born-preserving and not marginalizing. Whether one exists is open, and constructing
   one would itself be a round.

## What this pass does not do

- It proves nothing and preregisters nothing.
- It draws **no** inference from the absence of a construction to the truth of invariance.
- It does not claim padding is inert; it records that as provisional, with the proof obligation
  named.
- It does not decide what act 3 becomes. §5 states implications; the decision is the owner's.
- It touches no manuscript, adjudicates no deferred resource, reopens no merged result, and makes no
  sourcing claim.
