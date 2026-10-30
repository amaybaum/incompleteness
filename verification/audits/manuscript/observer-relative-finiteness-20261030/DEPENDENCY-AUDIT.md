# OI observer-relative finiteness — source dependency and minimum-diff audit

**Status:** research-only, independent review required. Not a manuscript correction,
scientific theorem grade, proof of arbitrary-carrier QM, or owner authorization to
merge. Parent: #1015; foundational direction #1007; experimental proofs #1009
and #1016. Created from main at
`f6989a27815c4d715223eebf2859422c1231e3f8`.
The Introduction comparison uses *draft* #918 at
`fa32b043ee1bc23fd78924c5c1c884b9918d2242`.
Publication/surgical audit #1005 at
`5eb7bbc1bb5d1b260aec1bb5fffbe27b8d509488` was the first scoped
snapshot; its later `ecec14ac644eaf33927113c92d3f39284e79b974` head
still changes no Main/GR/ch01/ch02 source files. #1005 stays separately
gated. Exact line references below are to these pinned sources, not moving main.

## Owner direction — foundation versus implementation

**General OI principle (choice of framework):** for a specified bounded embedded
observer/interface O there is a finite set of *distinguishable accessible
configurations* V_O, with a readout `pi_O:S -> V_O` (or a probabilistic
observer interaction with finitely many registered outcomes). Do **not** infer
that total microscopic S is finite. Infinite, countable, continuous and
finite carriers are all admissible for investigation when their states,
dynamics and observation interfaces are actually specified.

**Hypothesis boundary:** finite observable resolution does not follow from
embeddedness *alone*. A finite resource/boundary/information assumption is
needed for the specific observable interface; if an observer can accumulate
records forever the set of possible *histories* need not be finite. A physical
normalized state or probability measure, a measurable readout, and a specified
dynamical law are still necessary for computed transition probabilities.

**Old finite branch stays valid:** finite total-S assumptions (A1_finite)
may continue as explicit premises in finite reversible-permutation theorems
and candidate local lattice reconstructions. Their existing Lean proof objects,
finite-horizon equivalences, recurrence theorems and negative countermodels
are not invalidated by removing total finiteness from OI's **general** axioms.
No general carrier-independent physics follows merely by relabelling A1.

## Exact-source candidate correction sites

| ID | Pinned source and line | Existing problem | Minimum proposed disposition (NOT applied) |
| --- | --- | --- | --- |
| M0 | `papers/Main.md:46`, main `f6989a27` | Says dynamics acts on "*finite* S (Lemma 1)" and describes finiteness of total S as the distinguishing commitment. This is inconsistent with the very next finite-*visible* Lemma 1 and Main:62 status note. | Replace only the clause attributing finite S to Lemma 1, explicitly distinguishing finite resolved observer states from a separately selected finite-carrier representative. Check remainder of the same paragraph for dependent "energy" overreach before approval. |
| M1 | `papers/Main.md:48` and `:62`, same baseline | Lemma 1 is about finite visible configurations. The status remark honestly calls finite total S a posit, but presents the physical reading via a selected finite representative. | Preserve Lemma 1 and the finite-branch proof. Re-scope the remark only to distinguish the *general* framework from the original finite-total realization; do not invent a new infinite-carrier dynamics theorem. |
| M2 | `papers/GR.md:142`, same baseline | Says "Lemma 1 requires S finite for the recurrence proof". It is the **finite-order recurrence argument**, not Lemma 1, that requires total S finite. | Single-clause correction: finite-order recurrence in Main §2.3 assumes finite *total* S; Lemma 1 itself only establishes finite observable resolution. Keep exact decoupled and approximate slow-coupled deep-sector distinctions. |
| M3 | `book/ch01-observation.md:28`, same baseline | Claims the map acts on a "*finite* system" immediately before the finite-*visible* Lemma 1. | Change the sentence only: observer resolves finitely many states; the physically selected finite-total model is a separate restricted choice. Avoid rewriting the surrounding explanation. |
| M4 | `book/ch01-observation.md:38`, same baseline | The uniform invariant probability on "each accessible orbit" is stated without spelling out **finite cycles**. | Explicitly scope this statement to finite periodic orbits in the selected finite-carrier branch; do not generally replace counting by Haar or imply a unique invariant probability on infinite orbits. |
| M5 | `papers/Substratum.md:92` and `book/ch02-substratum.md:76`, main baseline | A1 literally says "S is finite", correctly as a condition of that reconstruction's *candidate class*; may be misread as the universal OI foundation. | Keep A1 as an explicitly labelled **finite-carrier branch premise**, including restrictions of Theorem 23/24, finite q and nearest-neighbor/selected lattice conditions. Do not delete A1 from those theorems unless the dependency is reproved. |
| M6 | `papers/Introduction.md:17,31,33`, #918 `fa32b043` | Abstract/physical hypothesis use "every physical observer ... finite ... system/world" while `:31` correctly defines an illustrative finite-carrier model. | In abstract and physical-hypothesis paragraph, state finite *observer distinguishability* as the general thesis. Keep `:31` and finite-horizon theorem as an explicitly **restricted** illustrative model. Introduction remains independently gated. |

**Cross-branch conflict check:** #1005 changes Complexity §5.1–§5.2, book ch18,
bibliography, regenerated FULL and audit outputs; it does **not** change the
original source sites Main:46, GR:142, ch01:28 or ch02:76. Its FULL artifact
may still mirror their old wording. #918 introduces Introduction.md only
on its own draft branch. Keep these life cycles independent.

## Additional dependency and proposed smallest edits (review-only)

**M0 energy dependency is *not* disposed of by fixing a parenthesis.** The
last sentence of `papers/Main.md:46` attributes well-defined energy and
energy conservation downstream to finite total `S`. The neighboring
finite-visible Lemma 1 does not prove this. The correct repair must either
(i) cite a specific theorem and retain its exact physical hypotheses, or
(ii) remove that extra causal attribution from the foundational sentence.
Do **not** claim energy conservation follows just from a finite observable
alphabet, or conversely that an infinite carrier cannot have conserved energy.

**Proposed textual substitutions, NOT applied to any manuscript:**

| Source | Exact old subspan | Candidate smallest replacement |
| --- | --- | --- |
| `Main.md:46` | `What distinguishes the present setting is not the existence of such a map but that it acts on a *finite* $S$ (Lemma 1); finiteness, not the dynamics, is the load-bearing commitment, and it is what renders energy and its conservation well defined downstream.` | `What distinguishes the present setting is the finite set of distinctions accessible to an embedded observer (Lemma 1); the finite total-$S$ reversible construction used below is an additional model premise, not a consequence of the lemma.` |
| `GR.md:142` | `Lemma 1 requires $S$ finite for the recurrence proof ([Main, §2.3])` | `The finite-order recurrence proof in [Main §2.3] additionally assumes finite total $S$; Lemma 1 itself requires only finite visible resolution` |
| `ch01-observation.md:28` | `What *is* distinctive here is not that such a map exists, but that it acts on a *finite* system; finiteness, not the dynamics, is the load-bearing commitment.` | `What *is* distinctive here is the finite set of distinctions accessible to the observer; finiteness of the *total* system is a separate premise of the finite reversible models developed below.` |
| `ch01-observation.md:38` | `On each accessible orbit the invariant measure is unique and uniform` | `On each finite cycle of the selected reversible model, the invariant probability measure is unique and uniform` |

**Review risks:** The `Main:46` edit deletes an unsupported dependency
assertion, not an energy proof. If a sound downstream derivation of energy
requires finite microstates, move that hypothesis into its own stated
conditional theorem instead. The `ch01:38` edit must also check the
surrounding global counting/Liouville sentence before treating the whole
paragraph as an unrestricted infinite-carrier statement. In `#918`, amend
only the abstract's and physical-hypothesis paragraph's *universal finite
world* characterization; keep the finite illustrative realization at
Introduction:31 and the finite-horizon correspondence at Introduction:67.

**Exact-head review status:** This is a writer-supplied correction to
the audit note, not an independent review. Require a distinct reviewer to
verify source identity, minimum science diff and all proof boundaries.

---
## Proof-dependency matrix: a non-negotiable review gate

| Result | General observer-relative formulation | Finite-S proof retained |
| --- | --- | --- |
| Finite visible resolution (Main Lemma 1) | Yes for a **specified finite-resolution interface** under its resource premises; no total-S inference | Yes |
| Finite-horizon stochastic ↔ reversible ↔ fixed-basis Born records | Existing **existence of finite representatives** of finite visible laws; not a characterization of the actual infinite substrate | Yes under published horizon, state and measurement conditions |
| Stochastic-inverse rigidity | Works for a finite *visible* matrix, independent of hidden cardinality | Yes |
| Measured exact observable return `Gamma_L=I iff pi(T^L)=pi` a.e. | Conditional, after defining finite positive-mass measurable cells; #1009 Lean candidate | Yes |
| Existence of a global synchronized visible return | **Not automatic**; finite visible alphabet, pointwise/Poincaré return and finite-history representability do not suffice | Finite total permutation yields exact common finite order |
| P-indivisibility | Conditional if a nonpermutation rooted step and exact visible return are shown, or another independently justified route is supplied | Finite-cycle route remains |
| Theorem 23 / gauge uniqueness | No unrestricted generalization; fixed branch, H-link/source and completeness obligations still open | Keep explicit A1_finite and other physical hypotheses |
| Deep hidden cardinality being observational "gauge" | Exact only relative to explicitly decoupled interface; slow-coupling estimate is finite-time/leading-order; not absolute cardinality invariance | Retain original qualified claims |
| Finite boundary entropy / hbar gap | Requires a physical finite-mode/boundary state and H-slope/KMS/thermal match hypotheses; not deduced from `|V_O|<infty` alone | Retain established conditional finite-boundary result |

## Specific negative controls to preserve

1. #1016 shows one finite instantaneous observer bit on an uncountable
   microscopic product can carry unbounded cumulative public history.
   A finite cyclic surrogate agrees on any pinned horizon `n<q` but
   diverges at `2q`; do not upgrade finite-horizon equivalence to all-time.
2. #1009's solenoid control is a fully reversible infinite carrier with
   Markov visible process and no exact common visible identity return.
3. #872's countably infinite union of finite cycles has full-support
   invariant normalized atomic measure and pointwise periodicity, but
   no single positive identity return time for the specified finite readout.
4. #1003's gauge-invariant squared-action countercontrol and #1009's
   pure-gradient flatness/source failure remain: continuous internal
   states cannot choose Wilson/Yang–Mills action or generate quantum
   measurement controls by cardinality alone.

## Conditions for actual surgical manuscript changes

1. Independent scientific reviewer checks the exact old clauses and the
   theorem-to-premise classification at these **exact SHAs**.
2. Produce an exact per-site proposed replacement diff with no unrelated
   editing. Re-check old finite-case proof hypotheses, including the
   distinction between finite **visible** matrices and finite total carriers.
3. Compare all affected source papers, ch01/ch02, Explainer, Introduction
   draft and FULL book mirror **after** the #1005 publication baseline is
   reconciled; do not copy a draft Introduction body onto main.
4. Obtain separate independent minimum-diff/editorial acceptance and
   exact-head ordinary CI where relevant; regenerate publication artifacts
   only with authorized canonical pipeline.
5. No theorem-grade elevation, F/E, workflow dispatch, readiness change,
   PR merge or main modification on the strength of this report.

**Current verdict:** observer-relative finiteness is the owner-selected
general foundation; the finite total-carrier property is no longer a
universal requirement. The original finite-S theorem family remains a
conditional, mathematically useful **special case**. All claims requiring
actual infinite-carrier dynamics, a consistent long-time observer, physical
readback or quantum/YM/GR sourcing remain OPEN until separately proved.
