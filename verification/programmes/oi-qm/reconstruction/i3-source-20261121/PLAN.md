# I3-SOURCE: what counts as a genuine physical source (plan, fixed before derivation)

**WIP / UNVERIFIED. Research plan only.** This file fixes the question, the test classes, the
productivity test and the node order of the D5 research unit before any derivation is recorded.
It adopts no criterion, premise or extension E, and changes no status. Physical source remains
NOT PASSED.

Tracking: Issue #1507. Governing owner decision: #1169 c.7065620072 (D5 option (c), D6 staging).
Authority: paper research, counterexamples, literature analysis and preregistration, with an
independent reviewer. No computation, implementation, premise adoption or merge.

## 1. Inputs (read-only, reviewed)

- GATE-A r5.6, #1503 at `fd3cb064`, `verification/programmes/oi-qm/reconstruction/gate-a-r5-20261121/PROPOSAL.md`
  (cited `GA:§`): §2 (I★), §2.2 (D-W, the I-3 options, the (iv) dilemma), §2.4 (I★_st-coh,
  I★_st-pop), §4 (L-H, L-H′), §9 (D5, D6).
- #1506 at `66d1b8e9` (D-W corrected stepwise form, §4.3 of its DESIGN).
- #1498 at `3269772a` (BQ1: under H1–H5 native runs are in BPP; the separating hypothesis is an
  available coherent operation).
- #1501 at `cd3672fa` (QOPS phase 2: KIN, FLOW, RES; earliest O1 and O3 links; Lemma P5).
- #1504 at `31594967` (Proposition U, (I) via (xiv)).
- Corpus on `main` at `df6da1c6`: `papers/Substratum.md`:249 (single-time interface),
  `papers/Main.md`:328 (diagonal preservation and its measurable-carrier corollary), `:568`,
  `:650`; `papers/Methodology.md`:403–405 (PBR and PIP); `OIBridge/SemigroupTransfer.lean`:93
  (`familyAt`).

## 2. The question

D-W meets I★'s mathematical clauses at trivial E. A criterion is sought that separates a genuine
physical source of the quantum operations from a classical simulator of their predictions,
without presupposing the quantum operations to be derived.

## 3. The three test classes (fixed now)

- **C1, classical simulation.** D-W stepwise (#1506 §4.3); D-W-enc (register stored under a fixed
  bijective re-encoding: encrypted, compressed or spread over sites); D-W-lazy (stores preparation
  parameters and instrument history, computes the state on demand); D-W-tot (simulates system and
  apparatus together, with a single fixed global step).
- **C2, genuine quantum models.** The target's own unitary dilation; quantum lattice models with
  finite local Hilbert dimension; ψ-ontic interpretations (de Broglie–Bohm, Everett, GRW);
  ψ-epistemic models of prepare-and-measure scope (Lewis–Jennings–Barrett–Rudolph).
- **C3, native OI.** Permutation dilations of a substratum bijection with a classical (diagonal)
  hidden prior (`Sub:249`, `familyAt`, `Main:328`); the same with a non-diagonal hidden state;
  native runs under H1–H5 (#1498); a hypothetical native exact model with an executable
  non-monomial operation (FLOW of #1501), none being known.

## 4. Productivity test (fixed before the attempt)

The unit is a **gem** iff it yields a fact strictly stronger than the restatement "D-W meets
I★'s mathematical clauses at trivial E, and the GATE-A options fail or meet the (iv) dilemma",
**and** at least one of:

- (a) a criterion that is independently justified (stated and motivated without reference to
  D-W or to `Q_exact`), excludes every C1 variant, admits at least one C2 model, and does not
  exclude C3 by its own terms, with a mathematically decisive test;
- (b) a proof, for a stated class of criteria, that no member separates C1 from C2, or that every
  member separating C1 from C2 also excludes a stated part of C3;
- (c) a hidden assumption exposed in the D5 analysis of GA §2.2 or §2.4.

Below that bar the outcome is recorded only (CONFIRMING or ELABORATING). A negative result is
stated only for the class actually treated.

**Decision rule for each criterion (fixed now).** A criterion is recorded as *passing* only if all
four cells hold: justification independent of D-W; C1 excluded in every listed variant; some C2
model admitted; C3 not excluded by the criterion's own terms (C3 may still fail exactness for a
separate reason, which is recorded separately). Any empty or failed cell gives *fails* or
*conditional*, with the failing cell named. The verdict text is written from the cells.

**Skepticism rule.** Any branch whose outcome is favourable to the framework (a criterion that
excludes D-W and admits native OI) is pressure-tested in the same node before acceptance: by a
redescription of D-W, by a genuine quantum model it might exclude, and by the question whether the
criterion was shaped by D-W.

## 5. Nodes, depth-first

- **N1 (Stage 1 lead).** Under I★_st-coh, does a T-SUB′-type criterion with (iv)-recoverable
  exclude D-W while admitting a legitimate exact model, native or at least non-native, of the
  single-time data? Sub-nodes: N1.1 the coherent variant over the corpus's interface; N1.2 the
  population variant.
- **N2 (independent criteria).** For each, independent justification and the three-class test:
  (a) resource or complexity separation (BQ1); (b) counterfactual or interventional structure;
  (c) locality and causal structure; (d) thermodynamic cost (Landauer, QOPS P5); (e) the
  ψ-ontology literature (PBR with PIP named; Hardy; Colbeck–Renner; Leifer); (f) T-HTV′ applied
  symmetrically.
- **N3 (well-posedness).** Is the distinction undecidable or ill-posed in principle, and for which
  class of criteria?

Order: N1.1 first (decisive, cheapest), then N1.2, N2 in the listed order, N3 last.

## 6. Literature (audit Step 4), searched first

Ontological models (Harrigan–Spekkens; Spekkens contextuality); ψ-ontology theorems and their
assumptions (PBR and PIP; Lewis et al.; Schlosshauer–Fine; Colbeck–Renner; Hardy; Barrett et al.;
Leifer's review); simulation, implementation and emulation (Feynman; Putnam; Chalmers); Deutsch's
universal quantum computer argument and its critics; complexity of classical simulation and of
ontological models (Montina; Aaronson); constructor theory; nonlinear dynamics and signalling
(Gisin; Polchinski); quantum non-equilibrium (Valentini). Precise citations in NOTE.md.

## 7. Outputs

`NOTE.md` in this directory: every result labelled (N) or (I) with its imports, its layer (P paper,
X exact algebra on paper, K kernel citation) and its §A.31 classification; the three questions
answered; owner decisions listed. Nothing else is added.
