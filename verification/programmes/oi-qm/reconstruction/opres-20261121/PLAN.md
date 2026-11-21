# OPRES: necessary resources for non-monomial transformations (plan, fixed before derivation)

**WIP / UNVERIFIED. Research plan only.** This file fixes the question, the definitions to be
used, the productivity test and the node order before any derivation is recorded. It adopts no
premise or criterion and changes no status. Physical source remains NOT PASSED.

Tracking: Issue #1509. Authorization: #1169, following I3-SOURCE (#1508, confirmed at
`df520f3b`). Paper research, counterexamples, literature and preregistration only; no
computation.

## 1. Question

What additional physical operations or resources are **necessary** for OI's native dynamics to
generate genuinely non-monomial quantum transformations?

## 2. Distinctions kept explicit in every result

- **Necessary vs possible.** A necessity claim is a theorem over a stated class of protocols. An
  example of a route is recorded as a possible route only.
- **Native vs imported.** Native: operations OI's stated dynamics and interface supply. Imported:
  every operation or state outside them, named.
- **Exact vs approximate.** Each no-go states whether it bounds approximations, and how.
- **Single step vs protocol.** Results are stated for one autonomous step and, separately, for
  protocols with preparation, control, measurement, feedforward and discard.
- **Representational vs operational.** "Non-monomial" is a property of a transformation's Born-form
  matrix in the configuration basis (KIN, decision 4). Operational record laws are a separate
  target. D-W shows they can be met classically (#1508 §0), so every result says which one it
  concerns.

## 3. Inputs (reviewed, read-only)

- S1, S2 and CM-1 to CM-5 (#1508 at `df520f3b`); S2-sub stays a conjecture and is used only where it
  is a necessary input, labelled as such.
- BQ1 and its separating hypothesis (#1498, `3269772a`).
- QOPS phase 2: KIN, FLOW, RES, READ, P5, J1 (#1501, `cd3672fa`).
- Proposition U (#1504, `31594967`).
- Lean interface designs (#1506, `66d1b8e9`).
- Kernel: `substratumGen_not_control` (StructuralClosure.lean:330),
  `substratumTheory_not_layerFlowExecutable` (LiftAudit.lean:200), and the diagonal lemmas they use.

## 4. Productivity test and outcomes (fixed before the attempt)

The unit's outcome is exactly one of the following, decided by what is proved, not by preference:

- **CONSTRUCTION.** A native mechanism (only native operations, each named) realizing a
  non-monomial transformation, exact or with a stated error, on a stated scope.
- **OBSTRUCTION.** A theorem: over a stated class 𝒞 of native protocols (any size and depth), no
  member realizes a non-monomial transformation exactly, with a stated approximation bound or the
  statement that none is given; **and** a proof that every protocol that does realize one contains a
  named element outside 𝒞. The named element is then the necessary additional premise, for that
  class.
- **INCONCLUSIVE** (a legitimate, preregistered outcome). Neither is proved. The record then names
  the exact missing premise or lemma whose proof would decide it.

A result is a **gem** (§A.31) iff it is strictly stronger than S1/S2 restated, namely it covers
protocols with preparation, control and measurement, or approximation, or it identifies the
necessary element sharper than "FLOW". Below that it is recorded only. Negative results are stated
for the class actually treated. Any favourable branch, one that yields a native mechanism, is
pressure-tested in the same node against a hidden import: a coherent state, a non-configuration
readout, a non-bijective step or a fitted parameter.

## 5. Nodes, depth-first

- **N1.** Fix the native protocol class 𝒩 in Born form: permutation steps, configuration
  preparations and ready cells, configuration-basis readout, classical feedforward, discard. Does
  𝒩 generate any coherence, exactly or approximately?
- **N2.** Extend 𝒩 by arbitrary fixed coherent ancilla or hidden states (𝒩⁺). Can a protocol realize
  a non-monomial unitary branch, exactly or approximately?
- **N3.** Necessity: characterize the element any realizing protocol must contain beyond 𝒩⁺, and
  check each candidate route (non-monomial step, non-configuration readout, preparation-dependent
  coherent hidden states, change of logical basis, uncountable carrier) as necessary or merely
  possible.
- **N4.** The operational layer: what is necessary for exact operational laws (L-H′, records, RES,
  Proposition U) and for efficient hosting (BQ1), as distinct from N1–N3.
- **N5.** Native status: does OI's stated dynamics supply any element found necessary in N3?

## 6. Literature (searched first)

Resource theories of coherence and their free operations (Baumgratz–Cramer–Plenio; Winter–Yang;
Chitambar–Gour's physically incoherent operations; Marvian–Spekkens; the Streltsov–Adesso–Plenio
review); measurement-based computation and its classical limits; Gottesman–Knill. Precise
citations in NOTE.md.

## 7. Output

`NOTE.md` in this directory, with (N)/(I) labels, layers (X exact algebra on paper, P paper,
K kernel citation), the outcome from §4, and Established / Assumed / Missing for each result.
