# BIDUAL-REL: the relative commutant of the diagonal in the bidual of B(ℓ²) (preregistration)

**WIP / UNVERIFIED. Paper-only research.** This plan is committed before the research record
(`NOTE.md`). It adopts no premise, edits no manuscript, Lean module or reviewed record, runs no
computation and changes no status. No merge is authorized.

- **Authorization.** Owner decision, `amaybaum`, #1169 c.7078857457 (2026-11-22T12:04:30Z), the
  "Quantum emergence (#1509)" row: "BIDUAL-REL: is ℓ^∞(C_V)\*\* maximal abelian in
  B(ℓ²(C_V))\*\*? The answer decides the state-space typing of the non-DIO obstruction", building on
  NONDIO-M2 at `7102e6af`. The safeguards there apply: paper-only; a preregistered plan with
  explicit assumptions and a stop condition; a negative result names the exact class it excludes;
  no change to `papers/`, `book/` or any file in the A1 retirement ledger; no computation, pull
  request, merge, comment, description edit or other automated GitHub write; independent review
  in a separate session; a positive result does not authorize its implementation.
- **Write path.** Under the owner's write-integrity halt (#1169 c.7076910606 and c.7078857457)
  this record is published by `git push` to its branch only, with a byte-for-byte check of every
  pushed file against the remote after each push. The branch-only state is provisional (§A.43).
- **Goal link (§A.47).** Serves #1509 (quantum emergence; the NONDIO line). It would decide the
  state-space typing (F-S) of NONDIO-M2 on non-normal visible inputs: whether Proposition BID's
  sufficient condition holds, and, if it fails, whether an affine assignment satisfying PROD and
  failing DIO-type exists. It does not decide NN M3 (nonlinear assignments), NN M4 (the nativeness
  criterion), M1-b, the A1 retirement, OPRES U1′, or anything about encoded carriers.
- **Tracking.** Accountable Issue #1509. Source record NONDIO-M2, branch
  `research/nondio-m2-20261122`, head `7102e6af`, from which this branch is cut; that branch is
  not changed. NONDIO-M2's reviews on #1509: c.7077843705, c.7077898374, c.7077922491.
- **A1 ledger check.** Before the first commit, `origin/research/a1exit-deletion-20261121` was
  fetched read-only at `b1b0522dc8bfab5b4972a4b0d46b328e2a7545a7`, and
  `verification/audits/foundations/a1exit-deletion-20261121/ledger.json` was read there. Its
  `files` map lists 44 paths, carrying 399 splices. The only one under
  `verification/programmes/oi-qm/reconstruction/` is
  `native-y-continuation-20261024/README.md`. None lies under
  `verification/programmes/oi-qm/reconstruction/bidual-rel-20261122/`, and none is a file this
  record writes. This record writes only inside that directory.

## 1. Pins

| Source | Pin | Use |
|---|---|---|
| NONDIO-M2 | `7102e6af` | `NOTE.md` §3 (Lemma CMP, RED-M2), §5 (Lemma JU, CX-F, CX-F′, CX-F″, both slice orders, Proposition BID, BIDUAL-REL), §6, review n5 (equivalence with maximality) |
| NONDIO-M1 | `dac9ca3f` | Lemma NRM (a), DET-at, through NONDIO-M2's citations |
| Reviews of NONDIO-M2 | #1509 c.7077843705, c.7077898374, c.7077922491 | n5 (the maximality equivalence), and the CX-F′/CX-F″ checks |

## 2. The question

Let C_V be countably infinite, H_V = ℓ²(C_V), A := B(H_V), D := ℓ^∞(C_V) ⊆ A the diagonal MASA,
and A\*\* the bidual with its von Neumann algebra structure. D\*\* is identified with the σ-weak
closure of D in A\*\*.

**BIDUAL-REL.** Does D′ ∩ A\*\* = D\*\* hold? (Equivalently, by NONDIO-M2 review n5: is D\*\*
maximal abelian in A\*\*?)

Exactly one outcome is reported:
- **PROVED**: a proof, or a cited theorem checked to apply exactly as stated. Then (F-S) is
  DIO-type for every affine assignment with PROD, by Proposition BID.
- **REFUTED**: an element of D′ ∩ A\*\* outside D\*\*, given as explicitly as the construction
  allows, with the choice principles it uses named. The consequence for (F-S) is then worked out:
  either an affine assignment with PROD that is not DIO-type, with its σ-D instrument, or the
  reason none follows, or INCONCLUSIVE on that sub-question with the missing ingredient named.
- **INCONCLUSIVE**: the missing ingredient named.

## 3. Assumptions, native (N) and imported (I)

| Label | Content | Kind | Source |
|---|---|---|---|
| KIN-B | configurations form an orthonormal basis of a complex Hilbert carrier; probabilities are diagonal entries | (I) | NONDIO-M2 §4 of its PLAN |
| LIN | operations are positive linear maps | (I) | as above |
| TB | the trace bound Σ_o Φ_o\*(1) ≤ 1 over finite sets of outcomes | (I) | as above |
| DEC | adjoined factors with non-configuration dynamics are prepared independently and evolve by product dynamics | (N) | as above |
| KIN-𝒟 | coherence and DIO-type are taken relative to the configuration algebra 𝒟 = ℓ^∞ | (I) | NONDIO-M2 (F-at) |
| σ-D | the total configuration action is deterministic, σ-additively | (N), reading | NONDIO-M1 §3 |
| PROD | the assignment appends ω: Ω_ρ(a ⊗ c) = ρ(a)ω(c) | (I), definition | NONDIO-M2 |
| (F-S) affine | ρ ↦ Ω_ρ is affine on all states of A | (I), the typing of Proposition BID | NONDIO-M2 §5 |
| NAT | every transition is a step of φ on configurations (a reading; **named, not adopted**) | (N), reading | NONDIO-M2 |
| LAW-σ, LAW-fa | readings of what native preparations are; neither adopted | (N), readings | NONDIO-M2 §6 |
| CNT-V | C_V countably infinite | scope | the question |

Literature theorems used in a proof are cited at their source's standing and checked against
their exact hypotheses before use. Constructions that use a free ultrafilter, Hahn–Banach or
another choice principle are marked as such. Mathematical existence of a state or a map is not
presented as its physical realizability. Infinite state spaces are not assumed to produce
quantum behaviour.

## 4. Productivity test (§A.31), fixed before the walk

The investigation is a **gem** iff it yields a fact strictly stronger than the restatement
"BIDUAL-REL is open and is a sufficient condition for (F-S) DIO-type on non-normal inputs", **and**
either (i) decides BIDUAL-REL or the (F-S) DIO question for affine PROD assignments, or narrows
the latter to a strictly smaller class with proof, or (ii) exposes a hidden assumption in how
(F-S) or Proposition BID is posed. Otherwise it is a **non-gem** (coherence relabelling).
INCONCLUSIVE is an allowed outcome and is compatible with either verdict of this test.

## 5. Nodes and decision rules (depth-first; decisive branch first)

- **B0. Literature.** Search for: Kadison–Singer and Marcus–Spielman–Srivastava; the extension
  property of MASAs (Archbold–Bunce–Gregson, Anderson); Akemann–Anderson–Pedersen; the bidual as
  the enveloping von Neumann algebra; maximality of D\*\* in A\*\* for a MASA D ⊆ A; ℓ^∞\*\* inside
  B(ℓ²)\*\*. *Rule:* a theorem that settles BIDUAL-REL is used only after its hypotheses are checked
  against D ⊆ B(ℓ²); otherwise record what was found and proceed on paper.
- **B1 (decisive). BIDUAL-REL.** *Rule:* a proof gives PROVED; an element of D′ ∩ A\*\* with a
  proof that it is not in D\*\* gives REFUTED.
- **B2. Consequence for (F-S).** If B1 is REFUTED: does some affine assignment with PROD and some
  σ-D instrument give two visible inputs with the same configuration law and different output
  configuration laws? *Rule:* an explicit assignment and instrument gives a non-DIO assignment;
  a proof that every affine PROD assignment is DIO-type despite B1 gives the opposite; otherwise
  INCONCLUSIVE with the missing ingredient named. Partial results (classes of ω or ρ for which
  DIO-type holds) are recorded with proof.
- **B3. Existence and realizability.** Which choice principles the constructions use, and where
  the inputs and hidden states stand under LAW-σ and LAW-fa.

Every node is closed by an explicit check with its verdict recorded at the node. Every result is
labelled **ESTABLISHED** (proved on paper here, layer X, or cited at its source's standing;
established within this record, not in the §A.46 sense), **ASSUMED** (a named premise) or
**MISSING** (a gap, with the node where the branch stopped).

## 6. Negatives and scope

A negative is stated only for the class it covers: the typing (F-S) with affine assignments
satisfying PROD, the instruments of NONDIO-M2's RED-M2 class, and the states named at the node.
It is not a statement about (F-H), which NONDIO-M2 settles, about NAT preparations, nonlinear
assignments, encoded carriers or OPRES's protocol class.

## 7. Stop conditions

Each is sufficient, and the record names the one under which it stops:
- B1 and B2 are decided, or each is reported INCONCLUSIVE with its missing ingredient.
- A node that needs computation, a change to the physical model or a new premise: name it and
  stop that branch.
- A node that needs a literature theorem that cannot be checked here: cite it at its source's
  standing, record INCONCLUSIVE with it named, and stop that branch.

There is no successor round.
