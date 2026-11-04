# OI observer-relative finiteness — source dependency and minimum-diff audit

## Bounded-REVISE resolution and matrix-extension checkpoint — 2026-11-01

- **Revises** audit head `955a1e39d27d2b20612b2b025844731066121792`. Sources are
  re-verified at current main `07d94f2c618c17237bea5b8bbf914417e598940b` (merge #1024).
  The fixture baseline `f6989a27` is kept as historical provenance; new rows cite `07d94f2c`.
- **Owner direction:** resolve the bounded REVISE (#1017 comment 6528422871, at `955a1e39`)
  and extend the matrix with owner-assigned items 10, 11, 13 and 15 (the owner's 2026-11-01
  disposition of open obligations) before renewed review. **Every
  manuscript correction proposed here remains gated by #1015.** Main:720's sole edit owner
  is #1015; this audit supplies evidence only.
- **No computation:** `scope_controls.py` was neither modified nor run. Fragments were
  re-verified with read-only `git show`/`grep -cF` at `07d94f2c`. The controls the review
  requests are listed below as pending; each needs separate authorization.
- **One verification note changed.** No manuscript, Lean, PDF or main edits; no dispatch,
  F/E, ready or merge.
- **Review independence:** the REVISE was posted through the owner's linked account, so
  distinct-reviewer independence is not established. A separate scientific and
  minimum-diff review of the new head is still required.

| Review item | Request | Resolution here |
| --- | --- | --- |
| 1 H-product | Record that a finite-valued `π:S→V` does not give `S≅V×H` with π the projection, nor a shared root-independent `μ_H`. Do so for Main Lemma 2, ch01 Lemma 2 and the §2.3/§3.4 proofs; keep the finite-product theorems | Dependency row **C-2** in the proof-dependency matrix and row **X-C2** in the matrix extension, with corpus scope. Unequal-fiber argument added to the negative controls. The finite-product theorems are unchanged; applying them to a general observation requires H-product. No wording drafted. Executable control pending (P-1) |
| 2 Lemma 3 orbit measure | Cover Main Lemma 3 as well as ch01:38; shift on ℤ | M4 now covers Main:56. The review's Main:55–61 is the Lemma 3 statement at :56, with Remarks at :58 and :60. A Main:56 substitution reuses the ch01:38 text. Matrix row added. The kernel's `orbit_invariant_unique` (`CanonicalMeasure.lean:178`) is proved under `[Fintype S]` (:54). Propagation sites ch01:85/FULL:429 and Explainer:115 are recorded. Executable control pending (P-2) |
| 3 ch05 triage | Classify each ch05 line REQUIRED / NO-EDIT / UNDECIDED | M8 now classifies ch05:11 NO-EDIT, ch05:15 NO-EDIT and ch05:23 REQUIRED (framing plus the A12 attribution) |
| 4 post-#1005 refresh | Re-verify fixtures on current main; correct stale #1005 status | Header and cross-branch metadata corrected: #1005 merged at `358d03d5`. Table below. The `f6989a27` fixture stays historical, not a perpetual gate |

**Fragment re-verification** (`scope_controls.py` `OLD`). Each fragment occurs exactly once at both
commits, at the same line, and the whole line is byte-identical:

| Fragment (abridged) | File | `f6989a27` | `07d94f2c` | Mirror at `07d94f2c` |
| --- | --- | --- | --- | --- |
| `…that it acts on a *finite* $S$ (Lemma 1);` | Main | :46 | :46 unchanged | — |
| `only finite visible resolution is a theorem (Lemma 1)` | Main | :62 | :62 unchanged | — |
| `Lemma 1 requires $S$ finite for the recurrence proof…` | GR | :142 | :142 unchanged | — |
| `it acts on a *finite* system; finiteness, not the dynamics…` | ch01 | :28 | :28 unchanged | FULL:372 |
| `On each accessible orbit the invariant measure is unique and uniform` | ch01 | :38 | :38 unchanged | FULL:382 |
| `**Axiom 2 (Finiteness).**` | glossary | :11 | :11 unchanged | FULL:6605 |
| `Part I established that any observer embedded in a finite deterministic universe` | ch05 | :11 | :11 unchanged | FULL:1338 |
| `The framework's content rests on a minimal mathematical structure: a finite set $S$` | ch05 | :23 | :23 unchanged | FULL:1350 |

Other cited lines are also byte-identical at both commits: Main:43–62, :113 and :118,
Substratum:92, ch02:76, ch05:15 and ch04:22. #1024 replaced one line each at Main:744,
Explainer:930, Complexity:206, Substratum:56/:407, ch02:194 and FULL:837. None of these is a
cited line, and no `.md` source's line count changed, so no reference here moves. Main:744's
"finite bijective $(S, \varphi)$" stands on both sides of #1024 as an explicit
finite-branch statement; it needs no row here. #918 is still draft at `fa32b043`.

**Pending controls (not run; each needs separate authorization).**
P-1: an exact enumeration of the unequal-fiber H-product control. P-2: an exact statement
check of the shift-on-ℤ orbit control; finite samples cannot certify the infinite case,
which rests on the written argument. P-3: `scope_controls.py --sources .` replayed at
`07d94f2c`. Ordinary exact-head CI on the new head is also required.

**Status:** research-only, independent review required. Not a manuscript correction,
scientific theorem grade, proof of arbitrary-carrier QM, or owner authorization to
merge. Parent: #1015; foundational direction #1007; experimental proofs #1009
and #1016. Created from main at
`f6989a27815c4d715223eebf2859422c1231e3f8`.
The Introduction comparison uses *draft* #918 at
`fa32b043ee1bc23fd78924c5c1c884b9918d2242`.
Publication/surgical audit #1005 at
`5eb7bbc1bb5d1b260aec1bb5fffbe27b8d509488` was the first scoped
snapshot; #1005 merged into main at
`358d03d5e6e5aed5184095bcb1906b1d1e28bcb2` (head `45269ab3d93ba626ec77ea3bba2004cea2ce91ca`)
and changed none of the cited source lines. Exact line references in the
sections below are to these pinned sources; the 2026-11-01 checkpoint
re-verifies them at main `07d94f2c`.

## Reproducible controls (not a certification)

`verification/audits/manuscript/observer-relative-finiteness-20261030/scope_controls.py`
has two deliberately separate modes:

- `python3 -I -B verification/audits/manuscript/observer-relative-finiteness-20261030/scope_controls.py`:
  checks the infinite carrier with a nonconstant invariant quadratic
  function, the single-cycle finite permutation obstruction to a
  nonconstant invariant, and a binary observation of an infinite set.
  Exact integer regressions are a cross-check of the accompanying
  algebraic arguments, not a Lean proof.
- Add `--sources .` at the original main baseline (or on the audit branch
  while those source manuscripts remain unchanged) to verify that eight
  precisely named old-claim fragments occur exactly once across Main,
  GR, ch01, glossary and ch05. This is a **historical-source fixture**:
  an eventual surgical manuscript correction is expected to change
  those fragments, so this command is *not* a perpetual release check.

The writer's initial local standalone probe returned
`PASS INFINITE-CARRIER`, `PASS FINITE-CYCLE` and
`PASS FINITE-OBSERVER`. The source-phrase check is **not claimed
executed locally** and still needs independent verification.
Automatic repository CI on the exact new head must be inspected
separately; none of these controls proves a physical OI energy law.

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
| M4 | `book/ch01-observation.md:38` and `papers/Main.md:56` (Lemma 3), same baseline | The uniform invariant probability on "each accessible orbit" is stated without spelling out **finite cycles**, in both manuscripts. The shift `T(n)=n+1` on ℤ has one infinite orbit and no normalized invariant probability. The "globally … counting measure" clause also presupposes finite `S`. | Explicitly scope both Lemma 3 statements to finite periodic orbits in the selected finite-carrier branch; do not generally replace counting by Haar or imply a unique invariant probability on infinite orbits. The restatements at ch01:85/FULL:429 and Explainer:115 inherit Lemma 3's scope: NO-EDIT if Lemma 3 is scoped, otherwise the same edit (UNDECIDED, decided at review). The "globally … counting measure" clause (Main:56, ch01:38): NO-EDIT if the orbit substitution is adopted, since that substitution names the selected finite reversible model in the same sentence and the counting measure is normalizable there; otherwise it needs the same finite-branch scope. The continuum Liouville clause (ch01:38; Main:58 Remark): NO-EDIT, because it is a continuum-limit reading of the finite counting measure that asserts selection, not uniqueness, and Main:58 and ch01:85 state Liouville's non-uniqueness. Main:62's restatement ("on the orbit of the actual microstate, the uniform measure is the unique $\varphi$-invariant measure"): NO-EDIT, because it follows "On a finite set" in the same passage and so is already finite-branch. |
| M5 | `papers/Substratum.md:92` and `book/ch02-substratum.md:76`, main baseline | A1 literally says "S is finite", correctly as a condition of that reconstruction's *candidate class*; may be misread as the universal OI foundation. | Keep A1 as an explicitly labelled **finite-carrier branch premise**, including restrictions of Theorem 23/24, finite q and nearest-neighbor/selected lattice conditions. Do not delete A1 from those theorems unless the dependency is reproved. |
| M6 | `papers/Introduction.md:17,31,33`, #918 `fa32b043` | Abstract/physical hypothesis use "every physical observer ... finite ... system/world" while `:31` correctly defines an illustrative finite-carrier model. | In abstract and physical-hypothesis paragraph, state finite *observer distinguishability* as the general thesis. Keep `:31` and finite-horizon theorem as an explicitly **restricted** illustrative model. Introduction remains independently gated. |

**M6 source text.** `papers/Introduction.md` at #918's draft commit `fa32b043ee1bc23fd78924c5c1c884b9918d2242` (blob `afedb761084ad8d6b4aa8aaec4b32d86e8090ab8`, branch `draft/oi-introductory-paper-20261025`), lines 17, 31, 33 and 67 in full:

Introduction:17 —

> Could the randomness of quantum measurements arise because observers cannot access all the information in an underlying deterministic reality? Observational incompleteness (OI) is the hypothesis that every physical observer is a proper part of a finite reversible deterministic system and records only the visible marginals of its dynamics. At every finite horizon, three classes of law coincide: all finite stochastic laws, the visible marginals of finite reversible dynamics, and the records of finite unitary systems measured in one fixed basis; the known components (Egri et al.; Barandes) are stated as one machine-checked theorem. Because Markov laws lie in every class, the discriminating content is memory: every faithful realization carries the law's conditional memory in its hidden state. Stochastic, quantum-like records can therefore arise exactly from deterministic dynamics, and any memory they show must be stored in the hidden part. In a finite reversible world whose hidden odds are shared by every visible start and drawn independently of it, the forecasts from every start, starts of probability zero included, are P-indivisible somewhere in the recurrence cycle whenever some table of forecasts from the start is not a permutation, in particular whenever a visible step is not fully predictable from the current observation; with every start of positive probability, this is equivalent to conditional memory at some order below the recurrence time. For an operational theory on a nonempty finite system that assumes complex matrix kinematics and tensor-product composites, the available operations on the system and at every finite ancilla level are exactly the normalized finite Kraus instruments if and only if five completion conditions hold. Neither that kinematics nor those conditions follow from bare OI. Applied to physics, OI places the zero-point sum and the effective cosmological constant at different levels of description, and separates conservation of black-hole information from its accessible recovery. Open are the completion conditions a physical substratum supplies, the Born exponent and the gravitational field equations.

Introduction:31 —

> This is modelled by a triple $(S,\varphi,V)$ [Main §1.2]: a finite total system $S=\mathcal C_V\times\mathcal C_H$ of visible configurations $\mathcal C_V$ and hidden configurations $\mathcal C_H$, a bijection $\varphi$ of $S$, and an observer $V$ that registers $x\in\mathcal C_V$ and not $h\in\mathcal C_H$. The bijection is the reversible representative of the hidden dynamics, motivated by observed near-unitarity, and finiteness of all of $S$ is posited [Main §1.2, Remark (status of the early commitments)]. The finite reversible system $(S,\varphi)$ is the *substratum*.

Introduction:33 —

> Observational incompleteness (OI) is the physical hypothesis that every physical observer is in this situation: a part of a finite, reversible, deterministic world with a specified readout and preparation. The hidden coordinates are not directly read at that instant. Whether they can be inferred depends on the retained history and permitted operations, not on embedding alone. In the known swap game, the first two visible readings already identify both cards, even though the visible process has memory. More generally, a quantity is identified exactly when it is constant on the initial states compatible with the retained record [Substratum, Prop. 24.5]. It is not joint unsharpness of non-commuting observables: the restriction can arise for a single fixed readout, and no uncertainty relation constrains fixed-readout visible laws [Main §3.4].

Introduction:67 —

> **Theorem 1** (finite-horizon stochastic–reversible–unitary equivalence [Main §3.4]). *For every finite visible alphabet and every finite horizon $K$,*

At #918's head `4028e45db1ba520dc6a1bfb44a26b76a112ba575` (blob
`bbf837ffbdf4a33ec9fbb5b02a7c63905ecabb0a`), lines 17 and 33 differ from the
text quoted above; lines 31 and 67 are unchanged. The quotations are of
`fa32b043`, the commit this row cites.

**Cross-branch conflict check:** #1005 (merged at `358d03d5`) changed Complexity §5.1–§5.2, book ch18,
bibliography, regenerated FULL and audit outputs; it did **not** change the
original source sites Main:46, GR:142, ch01:28 or ch02:76. At `07d94f2c` the FULL
mirror still carries the book sites' old wording (FULL:372 for ch01:28, FULL:719 for ch02:76). #918 introduces Introduction.md only
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

**Two exact model countercontrols for the energy clause:**

- Infinite substratum with a nonconstant conserved quantity:
  `S = ℝ²`, `T(x,p)=(p,-x)`, `H(x,p)=x²+p²`; then
  `H(T(x,p))=H(x,p)` exactly, despite `|S|` infinite.
- Finite substratum without a nonconstant conserved energy:
  `S=ℤ/qℤ`, `T(x)=x+1 mod q` (one full cycle). If
  `H(Tx)=H(x)` for every x, then H is constant on all S.

Thus **finite total cardinality is neither necessary nor, by itself,
sufficient to specify a nontrivial conserved-energy function**.
Additional physical structure/dynamical selection is required.
These are mathematical countercontrols for Main:46's causal attribution,
not a claim that OI already derives a physical Hamiltonian.
**Proposed textual substitutions, NOT applied to any manuscript:**

| Source | Exact old subspan | Candidate smallest replacement |
| --- | --- | --- |
| `Main.md:46` | `What distinguishes the present setting is not the existence of such a map but that it acts on a *finite* $S$ (Lemma 1); finiteness, not the dynamics, is the load-bearing commitment, and it is what renders energy and its conservation well defined downstream.` | `What distinguishes the present setting is the finite set of distinctions accessible to an embedded observer (Lemma 1); the finite total-$S$ reversible construction used below is an additional model premise, not a consequence of the lemma.` |
| `GR.md:142` | `Lemma 1 requires $S$ finite for the recurrence proof ([Main, §2.3])` | `The finite-order recurrence proof in [Main §2.3] additionally assumes finite total $S$; Lemma 1 itself requires only finite visible resolution` |
| `ch01-observation.md:28` | `What *is* distinctive here is not that such a map exists, but that it acts on a *finite* system; finiteness, not the dynamics, is the load-bearing commitment.` | `What *is* distinctive here is the finite set of distinctions accessible to the observer; finiteness of the *total* system is a separate premise of the finite reversible models developed below.` |
| `ch01-observation.md:38` | `On each accessible orbit the invariant measure is unique and uniform` | `On each finite cycle of the selected reversible model, the invariant probability measure is unique and uniform` |
| `Main.md:56` (at `07d94f2c`) | `On each accessible orbit the invariant measure is unique (uniform on the cycle)` | `On each finite cycle of the selected reversible model, the invariant probability measure is unique and uniform` (the ch01:38 text, reused) |

**Review risks:** The `Main:46` edit deletes an unsupported dependency
assertion, not an energy proof. If a sound downstream derivation of energy
requires finite microstates, move that hypothesis into its own stated
conditional theorem instead. The `ch01:38` edit must also check the
surrounding global counting/Liouville sentence before treating the whole
paragraph as an unrestricted infinite-carrier statement. In `#918`, amend
only the abstract's and physical-hypothesis paragraph's *universal finite
world* characterization; keep the finite illustrative realization at
Introduction:31 and the finite-horizon correspondence at Introduction:67
(both quoted under M6 above).

**Exact-head review status:** This is a writer-supplied correction to
the audit note, not an independent review. Require a distinct reviewer to
verify source identity, minimum science diff and all proof boundaries.

---
## Further corpus-propagation findings (exact main source, not manuscript edits)

**M7 — `book/glossary.md:11`: a foundational attribution defect.**
The glossary has an entry labelled **“Axiom 2 (Finiteness)”**, describing
finiteness of the *total* substratum as foundational. This contradicts
Main §1.2 even at the historical baseline: Main's second axiom is that
**differentiation recurs**, while the finite-total-carrier requirement
is separately identified as a posit. The owner's revised formulation
makes the discrepancy still clearer. A candidate *one-entry replacement*
for independent editorial review is:

> **Axiom 2 (recurrence of differentiation).** Differentiated content
> recurs across more than one moment; the first observation axiom alone
> does not imply recurrence. Finite observer distinguishability is
> addressed by Lemma 1 under its observational premises; finite total
> substratum cardinality is an additional restriction of the finite
> reversible reconstruction, not Axiom 2. See Main §1.2.

Do not replace the term by a new *axiom of infinite S*: microscopic
cardinality is intentionally **not specified** in the general framework.

**M8 — `book/ch05-gauge-structure.md:11,15,23`: finite branch framed
as universal.** The opening and §5.2 say respectively that Part I
established an observer embedded in a *finite deterministic universe*,
that the section establishes the *minimal mathematical object* as a finite
set, and that the **framework's content rests on** a finite set S.
These are correct descriptions **only of the finite-carrier realization**
that supplies the subsequent factorization and cubic reconstruction.
Per-line triage (review item 3; lines unchanged at `07d94f2c`):

- **ch05:11 — NO-EDIT.** "Part I established that any observer embedded
  in a finite deterministic universe…" already conditions its statement on
  the finite case, and it describes that case correctly. The edit owner of
  ch05:11 for its own correction is #924; this audit proposes no framing there.
- **ch05:15 — NO-EDIT.** This is the chapter roadmap for §5.2, the finite
  reconstruction. It already names the product factorization as "an input
  the dynamics has not been shown to select"; that is site factorization
  (ledger (viii), Main:726), not the V×H readout of C-2. If
  ch05:23 is scoped, :15 inherits that scope. Its decision stays with #1015
  (Substratum A1 / GR §3 / ch05:15 scope).
- **ch05:23 + FULL:1350 — REQUIRED, two clauses on one line.** (a) Framing:
  "The framework's content rests on … a finite set $S$" reads universally.
  The minimum qualifier is “The finite-carrier reconstruction considered in this
  chapter rests on...”. (b) Attribution: "The lemmas of Chapter 1 extracted …
  finiteness" gives total finiteness to Chapter 1's lemmas. This is #1013 row A12 in
  the matrix extension below. It resolves the earlier open check on whether §5.2's
  *finiteness follows from Chapter 1's lemma* claim needs a separate finite-model
  premise: it does.

Preserve the actual finite-q formulas, coupling-graph derivation and A1–A6
hypotheses unchanged.

**Adjacent but separately scoped:** `book/ch04-methodology.md:22`
calls observation the single founding premise, whereas current
Main §1.2 counts two axioms (differentiation and recurrence).
That may merit a **separate** foundational-consistency review, but
it is not authorization to rewrite Chapter 4 in this finite-S patch.

These findings come from a targeted source-text search, not a completed
whole-corpus closure scan. Before any manuscript correction claims
propagation complete, check all source papers, chapter openings, book
glossary, Intro, Explainer and FULL mirrors for synonyms and inherited
finite-total-S premises, classifying each **genuinely** affected location.

---
## Proof-dependency matrix: a non-negotiable review gate

| Result | General observer-relative formulation | Finite-S proof retained |
| --- | --- | --- |
| Finite visible resolution (Main Lemma 1) | Yes for a **specified finite-resolution interface** under its resource premises; no total-S inference | Yes |
| Finite-horizon stochastic ↔ reversible ↔ fixed-basis Born records | Existing **existence of finite representatives** of finite visible laws; not a characterization of the actual infinite substrate | Yes under published horizon, state and measurement conditions |
| Stochastic-inverse rigidity | Works for a finite *visible* matrix, independent of hidden cardinality | Yes |
| Measured exact observable return `Gamma_L=I iff pi(T^L)=pi` a.e. | Conditional, after defining finite positive-mass measurable cells; #1009 Lean candidate | Yes |
| Existence of a global synchronized visible return | **Not automatic**: control 3 below gives a binary readout of a countable union of finite cycles, with full-support invariant probability, pointwise periodicity and Poincaré recurrence, whose measured visible matrix is the identity at no positive step. Whether finite-history representability suffices is unresolved (#1015) | Finite total permutation yields exact common finite order |
| P-indivisibility | Conditional if a nonpermutation rooted step and exact visible return are shown, or another independently justified route is supplied | Finite-cycle route remains |
| Theorem 23 / gauge uniqueness | No unrestricted generalization; fixed branch, H-link/source and completeness obligations still open | Keep explicit A1_finite and other physical hypotheses |
| Deep hidden cardinality being observational "gauge" | Exact only relative to explicitly decoupled interface; slow-coupling estimate is finite-time/leading-order; not absolute cardinality invariance | Retain original qualified claims |
| Finite boundary entropy / hbar gap | Requires a physical finite-mode/boundary state and H-slope/KMS/thermal match hypotheses; not deduced from `|V_O|<infty` alone | Retain established conditional finite-boundary result |
| **C-2 / H-product:** product carrier `S≅C_V×C_H` with the readout as first projection, and a shared root-independent `μ_H` (Main Lemma 2 :50–54; ch01 Lemma 2 :34–36; consumed by §2.3, §3.2 and §3.4) | **Not implied** by a finite-valued `π:S→V` (unequal-fiber control 5 below). It is a named assumption (H-product); root-independence of `μ_H` is a further hypothesis. EDITORIAL: it names an assumption the finite theorems already use; Main:62 already classes all of §1.2 except Lemma 1 as non-theorem, and Main:54 calls the product idealized | Yes: §2.3's finite-order theorem, the §3.2 setup and §3.4's finite realizations are unchanged theorems on `C_V×C_H`, and the ledger's "Proved" is untouched; applying them to a general `(S, φ, V)` requires H-product. Kernel `Realization` (`HiddenMemory.lean:54–55`) and `TrajectoryMemory` take `step : V × H ≃ V × H` over finite types, presupposing the product rather than deriving it |
| Unique uniform invariant probability on each orbit; global counting measure (Main Lemma 3 :56; ch01 Lemma 3 :38) | **Not general:** an infinite orbit can carry no normalized invariant probability (control 6 below), and counting measure on infinite `S` is not normalizable. A separately specified normalized measure is required. EDITORIAL scope | Yes: finite cycles. Kernel `orbit_invariant_unique` (`CanonicalMeasure.lean:178`) is proved under `[Fintype S]` |

## Matrix extension — owner-assigned items 10, 11, 13, 15, C-2 and Main:720 (sites at `07d94f2c`)

Every old span below occurs exactly once in its file at `07d94f2c`, except the probe
sentence, which occurs at its two listed lines. Replacements are proposals, **NOT applied**, and all are gated by #1015.
**Kind:** SCIENTIFIC changes what an anchor claims is established; EDITORIAL changes
attribution, scope wording or labels to match an existing anchor. No row changes a theorem's
status; a row that would is marked SCIENTIFIC and is decided by review, not here.

**Misattribution class (#1013 Group A).** #1013 stays open as the defect record and is
closed by the eventual surgical PR. Rows A1, A3 and A7 are M0, M2 and M3 above and take
this audit's wording, which avoids two diffs on one sentence. Under that choice the
path-scoped re-grep of `\(Lemma 1\)|Lemma 1 requires \$S\$|only Lemma 1 \(finiteness|finite total system \(Lemma 1\)`
over `papers/*.md`, `book/*.md` and `verification/lean-mathlib` has 11 hits at
`07d94f2c` and should leave 5 survivors: Main:46 (M0's replacement keeps a literal "(Lemma 1)"),
Main:62, Main:216, Explainer:427 and GR:160, all legitimate `C_V`/ε uses. It leaves 7 if
#1013's own A7 text is used. Of the thirteen
Group A rows, nine have no earlier #1017 row; A12 was partly covered by M8. The
replacement texts are the reviewed #1013 assessment's (round 2, ACCEPT-WITH-NITS).

| ID | Site(s) | Exact old span | Finding | Proposed replacement (NOT applied) | Kind |
| --- | --- | --- | --- | --- | --- |
| A2 | Main:268 | `$\mathcal{C}_H = \{h_1, \ldots, h_m\}$ (Lemma 1)` | §3.2 Setup gives `C_H`'s finiteness to Lemma 1; Main:113 gives it to the posit | `$\mathcal{C}_H = \{h_1, \ldots, h_m\}$ (Lemma 1 for $\mathcal{C}_V$; $\mathcal{C}_H$ under the total-finiteness posit, §1.2, §4.5)` | EDITORIAL |
| A4 | Explainer:44 | `This means the configuration space is finite, not continuous. This matters because finite systems` | Lemma 1 → whole configuration space finite → exact recurrence | `This means the visible configuration space is finite, not continuous. This matters, given the separate posit that the whole state space is finite [Main §1.2, §4.5], because finite systems` | EDITORIAL |
| A5 | Explainer:145 | `We work on finite sets (Lemma 1).` | Covers `C_V×C_H` | `We work on finite sets (Lemma 1 for the visible sector; the total-finiteness posit [Main §4.5] for the hidden sector).` | EDITORIAL |
| A6 | Explainer:169 | `(the definition and Lemma 1)` | The Definition (Explainer:38) does not make `S` finite | `(the definition, Lemma 1 and the total-finiteness posit)` | EDITORIAL |
| A8 | ch01:119 + FULL:463 | `The proof uses only Lemma 1 (finiteness, hence Step 1's recurrence)` | Step 1 (ch01:111) uses the finite total set | `The proof uses only finiteness of $\mathcal{C}_V \times \mathcal{C}_H$ (Lemma 1 for the visible factor, posit A1 of Chapter 2 for the hidden one; hence Step 1's recurrence)` (names the product, consistent with C-2) | EDITORIAL |
| A11 | Explainer:1005 (+ Explainer.tex) | `\| Definition, Lemma 1, a non-permutation $T$ \|` | The proof needs `φ^N=id`; same omission as A6 | `\| Definition, Lemma 1, the total-finiteness posit, a non-permutation $T$ \|`; the table's section-label fixes are not this audit's | EDITORIAL |
| A12 | ch05:23 + FULL:1350 | `— finiteness, causal partition, determinism —` | Chapter 1's lemmas give visible finiteness only | `— visible finiteness, causal partition, determinism —` (same line as M8's REQUIRED framing) | EDITORIAL |
| A13 (a) | Main:718; mirror GR:589 | `The P-indivisibility proof uses finiteness via the recurrence argument` | The dependency list omits the posit | `The P-indivisibility proof uses total finiteness (the posit of §1.2, §4.5) via the recurrence argument`. GR:589 carries the sentence verbatim: mirroring it is recommended (§A.25 step 3). NO-EDIT is defensible only because GR:589's later clause places recurrence-scale P-indivisibility on a finite representative; decided at review | EDITORIAL |
| A13 (b) = FA D-17 | Main:718 + GR:589 | `and genericity conditions (non-degenerate spectrum, non-vanishing overlaps)` (unique in each file), together with the bridge clause that precedes it in the same sentence ("the stochastic-quantum bridge" alone also occurs at Main:220) | The final audit's slice 1 (`e138ce0b`, D-17) finds that the characterization theorem uses neither the bridge nor genericity, although both sites list them as requirements | **No wording proposed.** Trace the theorem's proof dependencies corpus-wide, including the Lean modules, and decide by independent scientific review before any text changes. The flag stays explicit in this editorial matrix | **SCIENTIFIC** |
| ch03:22 | ch03:22 + FULL:896 | `without additional postulates beyond those identified in Chapter 1's structural lemmas` | "a finite deterministic substratum" omits posit A1 | Candidate: `… beyond those identified in Chapter 1's structural lemmas and posit A1 of Chapter 2`; adoption decided in #1015 triage | EDITORIAL |
| A9 (item 10) | `OIRealization.lean:283` (docstring of `SealedCoreIsFiniteOI`) | `finite total system (Lemma 1);` | Comment attribution only; the kernel model (`Fintype.card Core = 8`) is explicitly finite | `finite total system (the total-finiteness posit, [Main] §1.2/§4.5; Lemma 1 gives the finite visible sector);` | EDITORIAL |
| A10 (item 10) | `OIRealization.lean:31–34` (header box) | `manuscript's finite-observation definition and Lemmas 1–3 (finite total` / `system, proper hidden sector,` | Untagged item, while the box tags "recurrence — Axiom 2 —" | `(finite total system — the total-finiteness posit —, proper hidden sector, …`. The box lines have about 4 characters of slack, so the re-wrap inserts a **fifth box line before the CAPSTONE line (:35)**; the edit ledger lists lines 31–34 and the inserted line | EDITORIAL |
| Probe prose (item 10) | `partition_coupling_probe.py:11, :199`; `bohr_frequency_probe.py:7120` | `uses only Lemma 1 (finiteness, hence recurrence)` (twice); `1-3 invoke (finite total system` | Check-message prose quoting A8 and A10; gates nothing but goes stale with them. :11 also says "[Main] and Chapter 1 both say" the A8 sentence, which Main does not contain | Update with A8 and A10 | EDITORIAL |

A9/A10 change comments only, so §A.35 is not engaged: no theorem is strengthened, and the
census has no byte pin. The frozen records that pin the Lean blob or quote these sentences
(legacy rounds hb-1, c4-2 and c4-3; `C1C4-MINIMALITY-AUDIT.md:36`;
`sc42-integration-result.json:1343`; `HUNKS-BOOK-A.md:66`) are preserved, not edited.

**Owner-assigned items 13 and 15, C-2 and Main:720.**

| ID | Site(s) | Exact old span | Finding | Proposed disposition (NOT applied) | Kind |
| --- | --- | --- | --- | --- | --- |
| O3 (item 13) | Computation:118 (§4.5) | `The framework, however, asserts that $S$ is finite` | Total finiteness is a posit of the finite-carrier branch (Main:62, §4.5), not a framework assertion. The clause's holographic justification is #1002's patch-budget question | `The total-finiteness posit ([Main] §1.2, §4.5), however, takes $S$ finite`. The holographic clause that follows is left to #1002, which stays held | EDITORIAL ⚑: the status word changes from "asserts" to "posit", aligning with Main:62; no theorem status moves |
| Structure:53 (item 15) | Structure:53, Theorem 24(iii) restated | `The hidden sector beyond the boundary layer admits arbitrary cardinality.` | Theorem 24(iii)'s exact identity covers independently prepared, normalized, exactly decoupled **finite** factors at a fixed interface (Substratum:50, :54, :92, :249, and the theorem statement at :257: finite factor `A`, `Tr σ_A = 1`, product dynamics `U⊗W`, fixed interface `V×H`). Infinite extensions need specified measures (Substratum:92). GR §3's coupled deep-sector statement is leading-order only (GR:142) | `The hidden sector beyond the boundary layer admits enlargement or reduction by independently prepared, normalized, exactly decoupled finite factors at a fixed interface.` Propagation check: Substratum:201's "deep-sector enlargement of arbitrary size — see §4" is consistent if read as arbitrary finite size (UNDECIDED, decided at review). Generator completeness and the older generator names stay with #979 | EDITORIAL: narrows a restatement to its anchor's proved scope; Theorem 24(iii) is unchanged |
| X-C2 (H-product) | Attribution sites, where the product is said to follow from embedding: Main:50–54; ch01:34 (Lemma 2 statement) and :36 + FULL:378/:380; Explainer:46–48; GR:591; `OIRealization.lean:284–285` (comment; the product clause's "(Lemma 2)" is at :285, while :284's is the legitimate proper-subsystem use); header box :32 "explicit product partition", in the item-list that A10 re-wraps | `follows, with cross-partition correlations entering only through $H_{\text{int}}$.` (Main:54); `The decomposition is not a modeling choice but the very definition of embedded observation` (ch01:36); `Lemma 2's product decomposition` (GR:591) | The partition `V⊊S` is definitional; the product form is not (control 5). **Preserve unchanged; their application to a general `(S, φ, V)` requires H-product:** Main:113/:131 (§2.3), Main:268 (§3.2), Main:60 (the §3.4 realization datum), Explainer:145, the `Realization` and `TrajectoryMemory` kernel statements, Theorem 24(iii) (Substratum:257 fixes the interface `V×H`), and GR:348 / ch07:181 / FULL:2056 (definiteness of a specific product partition). SM:68 and ch05:15 concern site factorization (ledger (viii), Main:726), not the `V×H` readout; they bear on C-2 only if `V` is a union of sites. Main:518's dilation theorem constructs a product representative, so the product is in its conclusion, not its premises. The shared uniform hidden prior is already an explicit hypothesis at Main:131 and ch01:93/:119 | Name H-product as an explicit assumption at the attribution sites, and at two Lean module docstrings that presuppose the `V × H` product without naming it as an assumption: `HiddenMemory.lean:48–53` ("Nothing else is assumed") and the `TrajectoryMemory.lean:1–8` module header ("No independent history/present/hidden joint law is assumed"); docstring text only, no statement or proof change. **No wording drafted here.** The text is set after review under #1015's gate, using Main:54's "idealized" and Main:62's anchor. The map side stays with #914 | EDITORIAL: no theorem status moves, since the finite-product theorems already assume the product; only their application scope is named |
| Main:720 | Main:720 (§4.5, Falsifiability); companion Main:722 (`its deterministic finite ontology`) | `a finite set with a deterministic bijection.` | The falsifiable structural claim makes the finite-carrier posit (Main:62; ledger (ii) at Main:726) the framework's claim | **Sole edit owner: #1015,** for Main:720 and Main:722 as one unit. This audit supplies evidence only: Main:62, M0–M1 and the rows above. SC-41's swap-half content (#972) is not part of this evidence | SCIENTIFIC: Main:720 contradicts no current anchor, since Main:62 and ledger (ii) also posit finite total `S`; rescoping therefore changes the declared falsifiable ontology rather than aligning it to an anchor. The owner's 2026-11-01 disposition tags this site's triage ED; #1015 confirms the kind |

## Specific negative controls to preserve

1. #1016 shows one finite instantaneous observer bit on an uncountable
   microscopic product can carry unbounded cumulative public history.
   A finite cyclic surrogate agrees through any pinned horizon `n ≤ q` and
   first differs at `n = q+1`; do not upgrade finite-horizon equivalence to all-time.
2. #1009's solenoid control is a fully reversible infinite carrier with
   Markov visible process and no exact common visible identity return.
3. #872's countably infinite union of finite cycles has full-support
   invariant normalized atomic measure and pointwise periodicity, but
   no single positive identity return time for the specified finite readout.
   The construction, verbatim from
   [#872 comment 6526240419](https://github.com/amaybaum/incompleteness/issues/872#issuecomment-6526240419)
   (posted from the author's account, 2026-10-30; its stated research gate is
   "independent mathematical review, exact premise scope, and explicit positive
   comparison with #1009's observable-return lemma", none of which is recorded
   on `main`):

   > **Construction.** Let `X = ⊔_{m≥2} ({m}×Z/mZ)`, `T(m,k)=(m,k+1 mod m)`, and assign each state `μ(m,k)=2^{-(m−1)}/m`. Since `Σ_{m≥2} 2^{-(m−1)}=1`, μ is a full-support invariant probability; each state has finite orbit length m. Define the *binary* readout `π(m,k)=1` iff `k=0`, otherwise 0. Both visible cells have positive μ measure.
   >
   > For **every** `L≥1`, choose the cycle `m=L+1`. The two states `(m,0)` and `(m,m−L)` change visible labels after L steps, each with positive weight `2^{−L}/(L+1)`. Hence
   >
   > `μ{π(T^L x) ≠ π(x)} ≥ 2^{1−L}/(L+1) > 0`,
   >
   > so the measured rooted visible matrix `Γ_L` is **never** the identity at any positive L. This is fully compatible with pointwise state periodicity and Poincaré recurrence. It does **not** say that a different finite visible factor cannot return, or that infinite X forbids P-indivisibility by other routes.

   Written argument; the comment's bounded `fractions.Fraction` regression
   (cycle lengths m = 2…16, L = 1…10) is not retained.
4. #1003's gauge-invariant squared-action countercontrol shows that, for
   one oriented square plaquette with compact gauge group `SU(2)` in
   ambient lattice gauge theory, local gauge covariance alone does not
   uniquely select the Wilson/Yang–Mills plaquette action. It is not a native OI
   result and says nothing about continuous internal states or
   cardinality. Whether continuous internal states or cardinality bear
   on the choice of action is unresolved (#1015).

   The #1009 pure-gradient link control establishes trivial plaquette
   holonomy for the tested construction. Its sourcing controls do not
   establish a native mechanism for selectable quantum measurement
   interactions. These results do not establish a general impossibility
   for continuous internal states, nor do they derive such measurement
   controls from continuity or cardinality alone. The broader question
   is unresolved (#1015).

   #1003's countercontrol, verbatim from
   `verification/programmes/oi-qm/constructive-qcd-bridge/README.md:60–92` at
   `0efd67a630fc80ac55fde1ca49fe8c5cbdbf10c3` (blob `948c7ee84dba205da2590a787b06f6020f707c9b`,
   branch `research/oi-constructive-qcd-bridge-20261029`):

   > **Claim (ambient lattice gauge-theory countercontrol, not a native OI
   > substratum theorem).** For one oriented square plaquette with compact gauge
   > group `SU(2)`, local gauge covariance permits distinct gauge-invariant
   > plaquette functionals. Therefore that covariance alone cannot uniquely
   > select Wilson/Yang–Mills dynamics.
   >
   > **Derivation.** Give an oriented link `x → y` a variable
   > `U_xy ∈ SU(2)` with transformation
   > `U_xy ↦ g_x U_xy g_y^{-1}`. The holonomy around a based plaquette obeys
   > `U_p ↦ g_x U_p g_x^{-1}`. Hence
   > `w(U_p) = 1 − (1/2) Re Tr(U_p)` is invariant, and so are both
   > `S_1 = ∑_p w(U_p)` (Wilson plaquette functional, up to normalization)
   > and `S_2 = ∑_p w(U_p)^2`. These are *different* gauge-invariant
   > functionals, not merely different normalizations: on a one-plaquette
   > configuration take `U_p = diag(e^{iθ}, e^{-iθ})`, attainable with three
   > identity links and one such link. Then `w = 1 − cos θ`:
   >
   > | Holonomy | `w` | `w²` |
   > | --- | ---: | ---: |
   > | `θ = π/3` | `1/2` | `1/4` |
   > | `θ = π` | `2` | `4` |
   >
   > The ratio `S_2/S_1` changes from `1/2` to `2`. Both actions pass the
   > same gauge-transformation check, but cannot be proportional across all
   > configurations. This establishes only **non-uniqueness from covariance
   > alone**. It does not show that both actions have the same continuum
   > universality class, that either is generated by the actual OI bijection,
   > or that OI's other premises fail to select one.
   >
   > **Control and countercontrol:** conjugating the plaquette by arbitrary
   > `g_x ∈ SU(2)` preserves both traces; the two explicitly evaluated
   > holonomies demonstrate unequal action ratios. The proof is exact
   > algebra (not a Lean certificate or numerical simulation).

   The source note is "research-only / preliminary mathematical finding" (:3) and lists,
   as its next independent check, whether the countercontrol is framed correctly (:158–159).
5. **Unequal fibers (H-product).** `S={a,b,c}`, `V={0,1}`, `π(a)=0`,
   `π(b)=π(c)=1`. If `π` were the first projection of a bijection
   `S≅V×H`, every fiber would have `|H|` elements; here the fibers have
   sizes 1 and 2, so no such `H` exists (here also `|S| = 3` is odd, a separate and weaker obstruction: fibers of sizes 1 and 3 also admit no product). A finite-valued
   readout therefore does not give a product carrier, whatever the dynamics.
   On an infinite measured carrier, conditional measures must be specified,
   and a root-independent `μ_H` is a further hypothesis. Written argument;
   executable control pending (P-1).
6. **Infinite orbit, no normalized invariant probability.** `S=ℤ`,
   `T(n)=n+1`. An invariant probability `p` satisfies `p(n+1)=p(n)` for
   all `n`, so `p` is constant on ℤ. Its total mass is then 0 or ∞,
   never 1. Lemma 3's unique uniform orbit measure is therefore a
   finite-cycle statement. Written argument; executable statement check pending (P-2).

## Conditions for actual surgical manuscript changes

1. Independent scientific reviewer checks the exact old clauses and the
   theorem-to-premise classification at these **exact SHAs**.
2. Produce an exact per-site proposed replacement diff with no unrelated
   editing. Re-check old finite-case proof hypotheses, including the
   distinction between finite **visible** matrices and finite total carriers.
3. Compare all affected source papers, ch01/ch02, Explainer, Introduction
   draft and FULL book mirror against current main (post-#1005 `358d03d5`;
   re-verified at `07d94f2c`); do not copy a draft Introduction body onto main.
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
