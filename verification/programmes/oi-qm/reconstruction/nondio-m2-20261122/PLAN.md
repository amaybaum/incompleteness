# NONDIO-M2: the non-DIO obstruction with a countably infinite visible carrier and a non-normal hidden state (preregistration)

**WIP / UNVERIFIED. Paper-only research.** This plan is committed before the research record
(`NOTE.md`). It adopts no premise, edits no manuscript, Lean module or reviewed record, runs no
computation and changes no status. No merge is authorized.

- **Authorization.** Owner decision, `amaybaum`, #1169 c.7077598984 (2026-11-22T10:08:36Z),
  item 2, "Quantum emergence (#1509)": "M2 first: non-normal hidden states on a countably infinite
  visible carrier. Requires a precise mathematical construction or a clearly identified
  obstruction, and must not assume that infinite state spaces produce quantum behaviour.
  Distinguish mathematical existence from physical realizability. M1-b needs separate
  authorization." Safeguards there (item 3): paper-only; an isolated branch; no file of the A1
  retirement ledger; negative results and unresolved premises preserved; stop at the stated
  boundaries; no GitHub write through an unvalidated write path; independent review before any
  successor round is proposed.
- **Write path.** Under the owner's write-integrity halt (#1169 c.7076910606 and c.7077598984)
  this record is published by `git push` to its branch only. No pull request, Issue edit or
  comment is made from this session. The branch-only state is provisional (§A.43).
- **Goal link (§A.47).** Serves #1509 (quantum emergence; NATIVE-NONDIO, #1544, and NONDIO-M1,
  #1547) and, through it, clause I-3 (physical sourcing) of I★. It would decide whether the
  non-DIO obstruction of NATIVE-NONDIO and NONDIO-M1 depends on the visible configuration set
  being finite (FIN-V) when the hidden state is not normal, that is, whether a countably infinite
  visible carrier together with a non-normal hidden state opens a route to a native coherence
  detector that the finite-visible proof excludes. It does not decide M1-b, NN M3 (nonlinear
  state assignments), NN M4 (the nativeness criterion), the A1 retirement, or anything about
  encoded carriers.
- **Tracking.** Accountable Issue #1509. Source record NONDIO-M1, draft PR #1547, branch
  `research/nondio-m1-20261122`, head `dac9ca3f2cf416faec1109e6ed9af8a6ba0fd3d7`, from which this
  branch is cut; #1547 is not changed. Owner acceptance of NONDIO-M1 at that head as a completed
  paper-only research record: #1169 c.7077295004, item 3.
- **A1 ledger check.** Before the first commit, `origin/research/a1exit-deletion-20261121` was
  fetched read-only at `ea1029d59b0bc0de7c5e21790d6011d83738e8bd`, and
  `verification/audits/foundations/a1exit-deletion-20261121/ledger.json` was read there. Its
  `files` map lists 44 paths, and they are exactly the files of its 399 splices. None lies under
  `verification/programmes/oi-qm/reconstruction/nondio-m2-20261122/`, and none is a file this
  record writes. This record writes only inside that directory.

## 1. Pins

| Source | Pin | Use |
|---|---|---|
| NONDIO-M1 (#1547) | `dac9ca3f` | `NOTE.md`: §0, §2 (S9, S10), §4 (Lemma P, Corollary P1, Lemma NRM, Corollary NRM-D, DET-at, CX-1′), §5 (RED-∞, IDLE-∞, "M2 kept separate"), §6, §9; reviews #1547 c.7077044631 (n4) and c.7077116712 |
| NATIVE-NONDIO (#1544) | `ab830621` | `INVESTIGATION.md`: §0, RED, IDLE, N5 (M2), N6; reviews #1544 c.7075473914, c.7075888975, c.7075922740 |
| OPRES (#1511) | `24702c1d` | Proposition D, Remark D′ (step 3, the pointwise slice), U1′ (ii) and (iii) with the reviewer sketch it records; cited at its own standing |
| `main` | `53c6601a10419b6b333cc992474272501ab542af` | `Main:46` (Lemma 1, FIN-V), through NONDIO-M1's citation |

## 2. The question

**Q-M2.** Let the total configuration set be C_V × Z, with the visible configuration set C_V
countably infinite and Z a set (countable in NATIVE-NONDIO's setting; any cardinality is
admitted). Let ω be a state of B(ℓ²(Z)) that is not normal. Let (Φ_o) be a positive extension,
satisfying TB, of a deterministic total-carrier configuration action (σ-D of NONDIO-M1). Is every
visible instrument obtained by appending ω, applying Φ_o and discarding the hidden output
DIO-type relative to ℓ^∞(C_V), and is it MIO-type where MIO-type is typable? Do native record
laws then depend only on the configuration law?

Exactly one outcome is reported per typing of §3:

- **EXTENDS**, with the exact class of carriers, append maps, states and extension maps stated;
- **FAILS**, with an explicit counterexample instrument inside the stated class;
- **INCONCLUSIVE**, with the missing ingredient named.

A typing in which the question cannot be posed without a new definition is reported as such; any
definition introduced is stated before it is used and judged against the circularity test of §6
(N1).

## 3. Formulation and slice fixed in advance

- **Formulation: (F-at)** of NONDIO-M1. ℬ = B(ℓ²(C_V × Z)) = B(ℓ²(C_V) ⊗ ℓ²(Z)), with
  𝒟 = ℓ^∞(C_V × Z); the visible algebra is B(ℓ²(C_V)) with 𝒟_V = ℓ^∞(C_V). Coherence is relative
  to the configuration algebra. (F-C\*) is not walked: NONDIO-M1 RED-∞ already covers it for every
  state and every visible carrier through the minimal tensor product, and that is not M2 as posed
  (NONDIO-M1 §5).
- **The slice in question.** The map σ_ω: B(ℓ²(C_V × Z)) → B(ℓ²(C_V)) that "appends ω", in the
  visible instrument Φ^V_o\*(a) := σ_ω(Φ_o\*(a ⊗ 1)) of NATIVE-NONDIO RED and NONDIO-M1 RED-∞. For
  normal ω it is the normal slice id ⊗ ω; for finite C_V it is the pointwise slice of OPRES D′
  step 3. For C_V infinite and ω non-normal it is the object NATIVE-NONDIO N5 records as not
  established (M2) and NONDIO-M1 §5 (review n4) locates off the diagonal.
- **Two typings of the visible instrument.**
  - **(F-H) Heisenberg.** The append is a linear map E: B(ℓ²(C_V × Z)) → B(ℓ²(C_V)), and the
    visible instrument is the Heisenberg map E∘Φ_o\*(· ⊗ 1) on B(ℓ²(C_V′)). This is the parent's
    definition.
  - **(F-S) State space.** The append is an assignment ρ ↦ Ω_ρ of a state of B(ℓ²(C_V × Z)) to
    each visible input state ρ, normal or not, and the visible output is Ω_ρ∘Φ_o\*(· ⊗ 1). Where
    the assignment is affine its linear extension is a map into the bidual B(ℓ²(C_V))\*\*, not
    necessarily into B(ℓ²(C_V)).
- **DIO-type and MIO-type** are taken in NONDIO-M1's Heisenberg form: DIO-type means
  Φ\*(𝒟_out) ⊆ 𝒟_in; MIO-type means Δ_in Φ\* = Δ_in Φ\* Δ_out, with Δ the diagonal conditional
  expectation. In (F-S), DIO-type is read as: the output configuration law (Ω_ρ∘Φ_o\*(· ⊗ 1)
  restricted to ℓ^∞(C_V′)) depends on ρ only through ρ|ℓ^∞(C_V).

## 4. Assumptions, native (N) and imported (I)

| Label | Content | Kind | Source |
|---|---|---|---|
| KIN-B | configurations form an orthonormal basis of a complex Hilbert carrier; probabilities are diagonal entries | (I) | NATIVE-NONDIO §4 |
| LIN | operations are positive linear maps (normal where stated; CP where stated) | (I) | NATIVE-NONDIO §4 |
| TB | the global trace bound, in Heisenberg form Σ_o Φ_o\*(1) ≤ 1 over every finite set of outcomes | (I) | NATIVE-NONDIO §0 |
| DEC | adjoined factors whose dynamics is not a configuration map are prepared independently and evolve by product dynamics | (N) | NATIVE-NONDIO §0; `Main:60` |
| DEF | S is the total system; the dynamics is a map φ: S → S | (N) | `Main:42` |
| A2 | φ is deterministic | (N) | `Main:54` |
| NAT | every transition is a step of φ on configurations; outcomes and records are functions of configurations (a reading of T-SUB′ (ii), (iii); not adopted) | (N), reading | NATIVE-NONDIO §3 |
| σ-D | each configuration input has an output configuration law that is zero or a point mass, σ-additively; NAT delivers it on the total carrier | (N), reading | NONDIO-M1 §3, §6 |
| LAW | preparations and hidden priors are configurations or laws over them. Two readings are kept apart: LAW-σ (σ-additive laws) and LAW-fa (finitely additive laws, that is, states of ℓ^∞). Neither is adopted | (N), readings | `Main:58`; ledger posit (iv) |
| VC | the append leaves the visible configuration observables unchanged: E(g ⊗ 1) = g for g ∈ ℓ^∞(C_V), E unital | (I), definition of an append | introduced here |
| PROD | the appended hidden state is ω, independently of the visible input: E(a ⊗ c) = ω(c)a for a ∈ B(ℓ²(C_V)), c ∈ B(ℓ²(Z)) (in (F-S): Ω_ρ(a ⊗ c) = ρ(a)ω(c)) | (I), definition of "ω appended" | introduced here; implies VC |
| CNT-V | C_V is countably infinite | scope | the question |
| NN-ω | ω is not normal | scope | the question |

FIN-V (`Main:46`) is **not** assumed: dropping it is the question. Encoded carriers in the sense of
T-SUB′ (iv) are outside every statement (NATIVE-NONDIO §0). The A1 retirement is not treated as
landed. RED-∞ is not generalized beyond its stated scope without a proof given here.

## 5. Productivity test (§A.31), fixed before the walk

The investigation is a **gem** iff it yields a fact strictly stronger than the restatement
"NATIVE-NONDIO RED and NONDIO-M1 RED-∞ hold for normal ω with any C_V, and for any ω with C_V
finite; the slice for C_V infinite and ω non-normal is not established (M2)", **and** either
(i) decides or narrows M2 of NATIVE-NONDIO or OPRES U1′ (ii), or (ii) exposes a hidden assumption
in how M2 or the slice was posed. Otherwise it is a **non-gem** (coherence relabelling).
INCONCLUSIVE is an allowed outcome of the question and is compatible with either verdict of this
test.

## 6. Nodes and decision rules (depth-first; decisive branch first)

- **N1 (decisive). The slice.** In (F-H): does a positive E satisfying PROD exist for every state
  ω of B(ℓ²(Z)) when C_V is infinite, and is it unique? *Rule:* a construction with a proof of
  boundedness and positivity gives existence; a proof that PROD and positivity determine E gives
  uniqueness; two distinct maps satisfying PROD give non-uniqueness and are recorded as a choice
  the question depends on. *Circularity test:* PROD and VC are admissible only if they constrain
  E on product elements (or on visible configuration observables) and do not already fix
  E(ℓ^∞(C_V × Z)) ⊆ ℓ^∞(C_V); a definition that is equivalent to DIO-type by inspection is
  recorded as definitional, not as a result.
- **N2. DIO-type of the visible instrument.** Under VC, or under PROD, is E∘Φ_o\*(· ⊗ 1)
  DIO-type for every positive extension Φ_o satisfying TB and σ-D? *Rule:* a proof gives YES for
  the stated class; an explicit positive map gives NO and becomes the counterexample of §2.
- **N3. MIO-type and creation.** For which ω is the visible instrument MIO-type, and does a
  non-diagonal ω give a non-MIO-type instrument? *Rule:* proof for the positive class; an
  explicit instrument for the negative.
- **N4. State-space typing (F-S) and joint states.** For normal visible inputs, is Ω_ρ fixed by
  PROD? For non-normal visible inputs, is it, and is the output configuration law determined by
  ρ|ℓ^∞(C_V)? *Rule:* a uniqueness proof, or two explicit joint states with the same product
  marginals; the residual question stated precisely if it stays open.
- **N5. Mathematical existence and physical realizability.** Which non-normal ω exist, by which
  principle, and which are delivered by NAT with LAW-σ or LAW-fa? *Rule:* proof, citation and
  argument only; if NAT and LAW do not decide it, the gap is named.
- **N6. Drop-one.** For each premise used by a positive answer in N1–N4, an explicit example of
  what fails without it, or the record that it is not used.

Every node is closed by an explicit check with its verdict recorded at the node. Every result is
labelled **ESTABLISHED** (proved on paper in this record, layer X, or cited at its source's
standing; established within this record, not in the §A.46 sense), **ASSUMED** (a named premise)
or **MISSING** (a gap, with the node where the branch stopped). Paper derivation, literature and
conjecture are kept distinct.

## 7. Negatives and scope

A negative (an obstruction) is stated only for the class it covers: the typing, the append maps,
the states and the extension maps named at the node, with every premise listed. It is not a
statement about encoded carriers, nonlinear state assignments, a nativeness criterion other than
NAT, (F-C\*) or (F-W\*), or OPRES's protocol class, which it may bear on but does not settle unless
a node proves it. A counterexample is stated with the premise it violates. Mathematical existence
of a state or a map is not presented as its physical realizability.

## 8. Stop conditions

Each of the following is a sufficient stop condition, and the record names the one under which it
stops:

- A node that needs computation: record MISSING and stop that branch.
- A node whose answer needs a change to the physical model or a new premise: name it and stop.
- A node that needs a literature theorem that cannot be checked on paper here, or that falls
  under M1-b: cite it at its source's standing, or record INCONCLUSIVE with that ingredient
  named, and stop that branch.
- The question is answered in both typings of §3, or each remaining case is reported
  INCONCLUSIVE or untypable with its missing ingredient.
- Fixed point: three consecutive passes over N1–N2 yield no NEW finding.

There is no successor round.
