# NONDIO-M1: the non-DIO obstruction on uncountable configuration carriers (preregistration)

**WIP / UNVERIFIED. Paper-only research.** This plan is committed before the research record
(`NOTE.md`). It adopts no premise, edits no manuscript, Lean module or reviewed record, runs no
computation and changes no status. No merge is authorized.

- **Authorization.** Owner decision, `amaybaum`, #1169 c.7076731666 (2026-11-22), item 2,
  "Quantum emergence (#1509): M1": "Does the non-DIO obstruction extend to uncountable
  configuration carriers? Keep TB, DEC, KIN-B, LIN and NAT explicit. Distinguish normal from
  non-normal states, and do not generalize the countable-carrier proof without justification."
  Safeguards there: separate branch, preregistered question, explicit assumptions, stop
  conditions, independent non-author review; paper arguments, source analysis, literature review
  and mathematical counterexamples only; no computation, Lean, physical-rule change, manuscript
  edit or merge; no file of the A1 retirement ledger modified.
- **Goal link (§A.47).** Serves #1509 (quantum emergence; OPRES and its successor NATIVE-NONDIO,
  #1544) and, through it, clause I-3 (physical sourcing) of I★. It would decide whether the
  countable-carrier obstruction of NATIVE-NONDIO (no native coherence detector or creator in the
  configuration basis) depends on the countability of the configuration set, that is, whether a
  carrier with uncountably many configurations, such as an infinite lattice with a finite
  alphabet, opens a native route that the countable proof excludes. It does not decide the
  nativeness criterion (M4 of NATIVE-NONDIO), the A1 retirement, or M2.
- **Tracking.** Accountable Issue #1509. Source record NATIVE-NONDIO, draft PR #1544, branch
  `research/native-nondio-20261122`, head `ab8306210445a26863f92daa33cc8233df606d0a`, from which
  this branch is cut; #1544 is not changed.
- **A1 ledger check.** Before the first commit, `origin/research/a1exit-deletion-20261121` was
  fetched read-only at `fef0f1589d66ae6e120b14e73b0ebb70b316e4c7` and
  `verification/audits/foundations/a1exit-deletion-20261121/ledger.json` was read there. It lists
  44 paths. None lies under `verification/programmes/oi-qm/reconstruction/nondio-m1-20261122/`,
  and none is a file this record writes. This record writes only inside that directory.

## 1. Pins

| Source | Pin | Use |
|---|---|---|
| NATIVE-NONDIO (#1544) | `ab830621` | `PLAN.md`, `INVESTIGATION.md` (§0, SHARP, DET, RED, IDLE, N5, N6, M1, M2); reviews #1544 c.7075473914, c.7075888975, c.7075922740 |
| OPRES (#1511) | `24702c1d` | Proposition D, Remark D′, Conjecture D″, U1′; cited at its own standing |
| `main` | `53c6601a10419b6b333cc992474272501ab542af` | `Main:n` lines of `papers/Main.md` (Definition, Lemma 1, Lemma 2, Lemma 3 and status Remark, §3.2 selected update and measurable-carrier corollary, ledger) |
| GATE-A r5.8 (#1503) | `109b9590` | T-SUB′ and the (iv) dilemma, through NATIVE-NONDIO §0 only |

## 2. The question

**Q-M1.** Let the total configuration set be uncountable, the case of interest being
X = A^Λ with A finite, |A| ≥ 2, and Λ countably infinite (for instance Λ = ℤ^d). Does the
non-DIO obstruction of NATIVE-NONDIO (Lemma DET, Corollaries RED and IDLE: every positive
extension, satisfying TB, of a deterministic total-carrier configuration action is DIO-type and
MIO-type, its visible reductions are DIO-type, and native record laws depend only on the
configuration law) hold there, and for which states and which extension maps?

Exactly one outcome is reported, per carrier formulation of §3 where they differ:

- **EXTENDS**, with the exact class of carriers, algebras, states and maps stated;
- **FAILS**, with an explicit counterexample channel inside the stated class;
- **INCONCLUSIVE**, with the missing ingredient named.

A formulation in which the question cannot be typed without a new definition is reported as such,
and any definition introduced is stated before it is used and judged against the circularity test
of §5 (N2).

## 3. Carrier formulations fixed in advance

The configuration algebra 𝒟 is the algebra whose states are configuration laws; "coherence" is
always relative to 𝒟 inside an observable algebra ℬ. The candidates:

- **(F-at) Atomic.** ℬ = B(ℓ²(X)) on the (non-separable) Hilbert space with the configurations as
  an orthonormal basis; 𝒟 = ℓ^∞(X). Normal and non-normal states and maps are distinguished.
  A diffuse law on X is not a normal state here.
- **(F-C\*) C\*-algebraic.** X compact (A^Λ with the product topology), 𝒟 = C(X), and ℬ a unital
  C\*-algebra containing 𝒟, for instance the quasi-local algebra ⊗_{s∈Λ} M_A with its canonical
  diagonal. Every Radon probability on X is a state of 𝒟. There is no normality notion.
- **(F-W\*) Measurable.** 𝒟 = L^∞(X, μ) for a reference probability μ (for instance a Bernoulli
  measure), inside ℬ = B(L²(X, μ)) or inside another von Neumann algebra containing it as a
  maximal abelian subalgebra. Points of X are not normal states.

Which formulation is the faithful one for the framework is not presupposed; each is walked.

## 4. Assumptions, native (N) and imported (I)

| Label | Content | Kind | Source |
|---|---|---|---|
| KIN-B | configurations form an orthonormal basis of a complex Hilbert carrier; probabilities are diagonal entries | (I) | NATIVE-NONDIO §4 |
| KIN-𝒟 | the generalization used in (F-C\*) and (F-W\*): configuration laws are the restrictions of states of ℬ to an abelian subalgebra 𝒟; coherence is relative to 𝒟 | (I) | introduced here; reduces to KIN-B in (F-at) |
| LIN | operations are positive linear maps (normal where stated; CP where stated) | (I) | NATIVE-NONDIO §4 |
| TB | the global trace bound, in Heisenberg form Σ_o Φ_o\*(1) ≤ 1 over every finite set of outcomes, so on all inputs, coherent ones included | (I) | NATIVE-NONDIO §0 (review F1) |
| DEC | adjoined factors whose dynamics is not a configuration map are prepared independently and evolve by product dynamics | (N) | NATIVE-NONDIO §0 (review F2); `Main:60` |
| DEF | S is the total system; the dynamics is a map φ: S → S | (N) | `Main:42` |
| A2 | φ is deterministic | (N) | `Main:54` |
| NAT | every transition is a step of φ on configurations; outcomes and records are functions of configurations at declared times (a reading of T-SUB′ (ii), (iii); not adopted) | (N), reading | NATIVE-NONDIO §3 |
| LAW | preparations and hidden priors are configurations or laws over them | (N) | `Main:58`; ledger posit (iv) |
| FIN-V | the visible configuration set C_V is finite | (N) | `Main:46` (Lemma 1) |
| UNC | the total configuration set is uncountable (scope hypothesis of this record) | scope | — |

Encoded carriers in the sense of T-SUB′ (iv) are outside every statement (NATIVE-NONDIO §0, F3).
M2 of NATIVE-NONDIO (a countably infinite visible carrier with a non-normal hidden state) is kept
separate unless a result here settles it as stated. The A1 retirement is not treated as landed;
the question is mathematical.

## 5. Productivity test (§A.31), fixed before the walk

The investigation is a **gem** iff it yields a fact strictly stronger than the restatement
"NATIVE-NONDIO's DET, RED and IDLE hold on countable carriers, and on measurable diffuse carriers
the two typable readings make DIO-type definitional (its N5)", **and** either (i) decides or
narrows M1 of NATIVE-NONDIO, OPRES U1′, or READOUT-ALG items 11 and 12 on measurable spaces, or
(ii) exposes a hidden assumption in how the countable proof or the measurable question is posed.
Otherwise it is a **non-gem** (coherence relabelling). INCONCLUSIVE is an allowed outcome of the
question and is compatible with either verdict of this test.

## 6. Nodes and decision rules (depth-first; decisive branch first)

- **N1 (decisive). Step audit.** For each step of SHARP, DET, RED and IDLE, identify whether it
  uses countability of X or of the outcome set, the trace-class (predual) setting, normality of
  the map, or normality of a state; check each such use in each formulation of §3. *Rule:* a step
  whose use is removable by a stated argument is marked extendable with that argument; a step
  whose use is load-bearing gets an explicit example, inside or outside the stated class, or is
  recorded MISSING.
- **N2. Definition of a deterministic action.** In each formulation, state what "configuration-
  level action" and "deterministic" mean when points are not normal states or the map is not
  normal. *Circularity test:* a definition is admissible only if it constrains Φ on states whose
  configuration law is sharp (concentrated on one configuration or on one event), and does not
  already fix Φ on states whose configuration law is not; a definition that is equivalent to
  DIO-type by inspection is recorded as definitional, not as a result.
- **N3. Rigidity.** Under each admissible definition, is every positive extension satisfying TB
  DIO-type, and MIO-type where MIO-type is typable? *Rule:* a proof gives YES for the stated
  class; an explicit positive map gives NO and becomes the counterexample of §2.
- **N4. Reduction and record laws.** RED and IDLE in each formulation, with the hidden state
  normal, non-normal, diffuse or coherent. *Rule:* algebra on paper, the slice map stated
  explicitly.
- **N5. Native reading.** Which of the admissible definitions does NAT, read on an uncountable
  carrier, actually deliver? *Rule:* citation and argument only; if NAT does not decide it, the
  gap is named.
- **N6. Drop-one.** For each premise used by a positive answer in N3–N4, an explicit example of
  what fails without it, or the record that it is not used.

Every node is closed by an explicit check with its verdict recorded at the node. Every result is
labelled **ESTABLISHED** (proved on paper in this record, layer X, or cited at its source's
standing; established within this record, not in the §A.46 sense), **ASSUMED** (a named premise)
or **MISSING** (a gap, with the node where the branch stopped). Paper derivation, literature and
conjecture are kept distinct.

## 7. Negatives and scope

A negative (an obstruction) is stated only for the class it covers: the formulation, the
algebras, the states and the maps named at the node, with every premise listed. It is not a
statement about encoded carriers, nonlinear state assignments, a nativeness criterion other than
NAT, or formulations not walked here. A counterexample is stated with the premise it violates.

## 8. Stop conditions

- A node that needs computation: record MISSING and stop that branch.
- A node whose answer needs a change to the physical model or a new premise: name it and stop.
- A node that needs a literature theorem that cannot be checked on paper here: cite it as (I)
  literature at its source's standing, or record INCONCLUSIVE with that theorem named.
- The question is answered in every formulation of §3, or each remaining formulation is reported
  INCONCLUSIVE or untypable with its missing ingredient.
- Fixed point: three consecutive passes over N1 yield no NEW finding.
