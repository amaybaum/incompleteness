# The typed completion audit (OI_Q, Level II)

Level I closed the substratum-source programme with one statement, frozen in the manuscripts:
on every nonempty finite carrier, the current OI substratum together with continuous
off-diagonal controllability is equivalent to exact finite **endomorphic** operational quantum
mechanics. Every operation in that statement acts from a finite carrier back to the same carrier:
`FiniteOperationalTheory` has `avail` on `A` and `availExt n` on `A × Fin n`, and nothing else.
Full finite-dimensional quantum mechanics also has operations `M_S → M_{S'}` between different
carriers — preparations, isometric embeddings, partial traces, instruments whose input and output
dimensions differ.

This audit asks whether "endomorphic" is a physical limitation or an artifact of the typing. It
asks the question as a **redundancy test**, not by postulate: define a typed interface with
independent operational meaning, and prove or refute that the frozen endomorphic theory determines
it. Bare OI and the frozen Level I statements are untouched; the thread is a new one and its
object is called OI_Q.

## The discipline

Two rules were fixed before the first theorem.

- The typed layer must **not** be defined by "there exists an endomorphic dilation". That would
  make the determination theorem nearly definitional. The typed interface states what typed
  operations are available in its own terms; the lint checks that the structure region names no
  dilation, no Kraus form, no shadow, and no exactness.
- The conditions that relate carriers must carry **no quantum content**. The test is a typed
  theory that satisfies every rule of the interface and is not quantum.

The possible outcomes were named in advance: (A) full redundancy — the endomorphic theory already
determines the typed one; (B) a preparation gap — fresh chosen-state preparation is missing; (C) a
coherence gap — the carrier theories are quantum separately but not coherently linked; (D) another
missing operation, exposed by a countermodel.

## First entry: the typed interface, its shadow, and the determination theorem

**The interface.** A typed finite operational theory (`TypedCompletion.TypedOperationalTheory`)
has an availability predicate `availT S S' O F` on finite outcome families of maps
`M_S → M_{S'}` for every pair of finite carriers, with exactly the closure rules the endomorphic
structure already has, stated at their carrier-general type:

| Rule | Content |
|---|---|
| identity | doing nothing is available on every carrier |
| coarse-graining | classical coarse-graining of the outcome label |
| feed-forward composition | run `F : S → S'`, then an outcome-dependent `G : S' → S''` |
| relabelling | availability transported along bijections of both carriers |
| uniform attachment | attaching a uniformly mixed fresh factor — the only preparation assumed, as in the endomorphic structure |
| discard | discarding a factor (the partial trace) |
| readout | a native factor readout exists and is spectator-independent; its form is derived, as in the endomorphic structure |

No clause mentions a dilation. At a level `Fin n` the typed attachment is the endomorphic
structure's `uniformAttach` and the typed discard is its partial trace (`attachUniform_fin`,
`discardR_fin`).

**The shadow.** Restricting a typed theory to maps from a carrier to itself, with `A × Fin n` as
the levels, yields a `FiniteOperationalTheory` on every carrier (`shadow`); every field of the
endomorphic structure is discharged by a typed rule. The shadow family is regrouping-invariant by
definition and relabelling-invariant by the typed relabelling rule, so every shadow is an
embedded-observation theory (`shadow_embeddedObservation`). This settles the first coherence
question: the product-type cross-carrier coherence that embedded observation asks for is automatic
for a typed theory.

**The hypothesis.** `ShadowQuantum`: the shadow is exact finite endomorphic quantum mechanics on
every nonempty carrier. This is what Level I supplies from the OI⁺ package on each carrier, and
`typed_determined_of_oiPlusElem` states the result in that vocabulary.

**The determination theorem** (`typed_determined`). Under the shadow hypothesis, between any two
nonempty finite carriers a family is typed-available if and only if it is a finite typed Kraus
instrument (`IsTypedKrausInstrument`: rectangular Kraus operators `M_{S'×S}`, normalized on `S`,
grouped by outcome).

- *Soundness* (`typedKraus_of_availT`). A typed-available family is wrapped, by discard, attach
  and relabelling, into an endomorphic family on the register `S × S'` (`wrap`, `wrap_availT`).
  By exactness the wrapper is a square Kraus instrument, and the typed family is recovered from it
  by slice embeddings (`recover_of_wrap`): its Kraus operators are the compressions
  `|S'|^{-1/2} · P_s L_k V_t`, normalized on `S` because the slice projectors sum to the identity
  and the slice embeddings are isometries.
- *Completeness* (`availT_of_typedKraus`). A typed Kraus instrument is realized by attaching a
  uniform ancilla `S' × Fin (n+1)`, relabelling to the register `S' × (S × Fin (n+1))`, running the
  square Kraus instrument whose operators place `K_k` on the output factor and record `k` on the
  ancilla (`regOp`, `regOp_normalized`), and discarding the second factor
  (`discardR_regOp_conj`). Every step is a typed closure rule or an endomorphic availability
  supplied by exactness on the register (`availT_of_krausFamily`).

**The converse.** A typed theory whose available families between nonempty carriers are
exactly the typed Kraus instruments has a quantum shadow, by restriction to one carrier, where a
typed Kraus instrument is exactly an endomorphic one (`typedKraus_iff_endomorphic`,
`shadowQuantum_of_typed`). The determination therefore holds both ways: the shadow is quantum on
every nonempty carrier exactly when the typed theory is the finite typed quantum theory
(`typed_determined_iff`).

**No quantum content in the interface.** The typed diagonal theory (`typedDiag`), in which a
family is available exactly when every branch preserves diagonal matrices, satisfies every rule
of the interface; its qubit shadow has no composite unitary control and is not quantum mechanics
(`typedDiag_shadow_not_control`, `typedDiag_shadow_not_qm`, `typed_interface_not_quantum`). The
quantum content of the determination theorem lies entirely in the shadow hypothesis.

## The fork, decided for this interface

Outcome **A**, full redundancy. No fresh chosen-state preparation is needed: the uniform attachment
the endomorphic structure already assumes, together with exactness on a register, realizes every
typed Kraus instrument. No cross-carrier coherence beyond the typed closure rules is needed: the
shadow family is coherent by construction. For this interface, "endomorphic" is a typing artifact
of `FiniteOperationalTheory`, not a physical limitation of the Level I conclusion.

| Outcome | Status |
|---|---|
| A. Full redundancy | Holds (`typed_determined`) |
| B. Preparation gap | Does not arise: uniform attachment plus exactness suffices (`availT_of_typedKraus`) |
| C. Coherence gap | Does not arise: the shadow family is regrouping- and relabelling-invariant by construction (`shadow_embeddedObservation`) |
| D. Other missing operation | None exposed |

## What is not claimed

- That this typed interface is the only reasonable one. It is the carrier-general form of the
  closure rules the endomorphic structure already assumed; a differently typed interface would need
  its own determination test.
- Anything about infinite-dimensional quantum mechanics. Level III is a different programme: an
  inductive limit of finite matrix algebras is an AF algebra, not `B(L²(ℝ³))`, and the standard
  representation requires a specified directed system, which for OI would be the spatial lattice
  refinement of the substratum. It is not begun here.
- Anything about bare OI, which is untouched, or about the frozen Level I statements, which this
  audit does not modify.

## Freeze

Level II is frozen at this entry. Its statement, propagated to GR §3.3 with cross-references in
Main §3.4, the Explainer, and book chapters 1 and 19:

> Under the carrier-general typed operational interface — identity, composition, coarse-graining,
> relabelling, uniform finite attachment, discard, and factor readout — the current OI substratum
> together with continuous off-diagonal controllability is equivalent to exact finite-dimensional
> typed operational quantum mechanics, for nonempty finite input and output carriers.

Within the natural carrier-general extension of the operational rules already used at Level I,
"endomorphic" is a typing artifact rather than an additional physical restriction. The
qualification is stated beside it in every mirror: uniform attachment and discard are not derived
from the endomorphic formulation, which cannot express a map between different carriers; they are
the carrier-general counterparts of the ancilla attachment and discard rules already present in the
finite operational framework, and the determination theorem shows that adding them introduces no
specifically quantum content. The Level I theorem references keep the word "endomorphic", since that
is what those theorems prove; the typed theorem follows them and removes the qualifier at the typed
operational level. No pure-preparation axiom, no carrier-coherence axiom, and no
all-completely-positive-maps axiom entered; the quantum content lies entirely in the frozen Level I
shadow. The remaining qualifier is finite-dimensional. Whether to open Level III, where the new
physics is the continuum completion rather than another finite operational axiom, is a separate
decision.
