# NATIVE-NONDIO: a native route to non-MIO or non-DIO elements (preregistration)

**WIP / UNVERIFIED. Paper-only research.** This plan is committed before the investigation
(`INVESTIGATION.md`). It adopts no premise, edits no manuscript, Lean module, accepted design or
reviewed record, runs no computation and changes no status. No merge is authorized.

- **Authorization.** Owner decision, `amaybaum`, #1169 c.7075274142 (2026-11-22T06:20:58Z), row
  "Native mechanisms": "A bounded, paper-only investigation of the leading missing mechanism: the
  physical route to non-MIO / non-DIO resources, building on OPRES (#1511) and READOUT-ALG
  (#1513), on a new branch with a fresh writer". Excluded there: "Computation; the held
  H-F1/H-RC/T-WP tests (#1518); changes to the physical model; theorem-strengthening claims".
  Conditions: own branch, writer and draft PR; an independent reviewer in a separate session; no
  merges; no automatic successor tasks.
- **Goal link (§A.47).** The work serves the owner's P1 workstream "Native quantum mechanisms"
  (#1169 c.7069936226, parallel plan) and, through it, clause I-3 (physical sourcing, NOT PASSED)
  of I★ as adopted under D1-A. It would decide, for the framework's stated substratum and observer
  interface, whether the earliest missing mechanism named by OPRES (a native coherence detector
  and a native coherence source) can be supplied without a new posit, and if not, which premise
  blocks it.
- **Tracking.** This record's draft PR. Related Issues: #1509 (OPRES), #1512 (READOUT-ALG), #1490
  (QOPS). The accountable Issue for any open item this record leaves is proposed as #1509, for
  owner confirmation (§A.45 rule 6); no Issue is edited.

## 1. Pins

| Source | Pin | Use |
|---|---|---|
| `main` | `53c6601a10419b6b333cc992474272501ab542af` | `Main:n`, `Sub:n`, `GR:n` are lines of `papers/Main.md`, `papers/Substratum.md`, `papers/GR.md`; Lean `file:line` under `verification/lean-mathlib/OIBridge/` |
| OPRES (#1511) | `24702c1d` | Lemma C, Theorems A′, B, C, Proposition D, Remark D′, CC-1, U1′, U2; cited at its own standing (WIP / UNVERIFIED; D′ independently reviewed) |
| READOUT-ALG (#1513) | `4554dd63` | the three levels; items 1–26; RA-1, RA-1′, RA-2; IMPL-R5, ACC-R5, UPD-C; provisional |
| QOPS-P4 (#1524) | `f9e564ea` | read under §A.19 before any novelty claim: Proposition RIG, Corollary RIG′, CPX, COH-REC; provisional, unreviewed beyond its first review |
| GATE-A r5.8 (#1503) | `109b9590` | I★, clause I-3, T-SUB′ and its definition of observer-access procedure (an option, not adopted) |
| QOPS-P3 (#1518) | `46240053` | context only; its H-F1/H-RC/T-WP tests are held and are not run, redesigned or ranked here |
| endpoints (`EP:n`) | blob `d9d92e03` | `verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/endpoints.md` |

## 2. The question (either answer counts)

**Q.** Within the framework's stated substratum and observer interface, with no new posit, does
any native mechanism supply a **non-DIO** element (an instrument whose output diagonal depends on
an off-diagonal entry of its input) or a **non-MIO** element (an operation mapping some
configuration state to a non-diagonal output)? If not, which premise or missing ingredient blocks
it? Each candidate is assessed separately for:

- **(a)** existence of such an element in some admissible model;
- **(b)** its derivation from the actual selected dynamics and observer interface;
- **(c)** its operational accessibility to an embedded observer.

A positive answer at (a) does not imply (b) or (c), and a negative answer is stated only for the
class actually ruled out.

## 3. Definitions fixed in advance

- **Born-form carrier.** For a countable configuration set X, ℓ²(X) with the configurations as an
  orthonormal basis; ℓ^∞(X) its configuration algebra (OPRES §2; READOUT-ALG §1).
- **Configuration-level action** of a family (Φ_o) of normal positive linear maps on trace-class
  operators, with Σ_o Tr Φ_o(ρ) ≤ Tr ρ for ρ ≥ 0: p(o, y | x) := ⟨y|Φ_o(|x⟩⟨x|)|y⟩.
- **Extension.** (Φ_o) is a positive (respectively CP) extension of a given configuration-level
  rule p if its configuration-level action is p. Nothing is assumed about its action on
  non-diagonal inputs.
- **Deterministic action.** p(o, y | x) ∈ {0, 1} for all o, y, x.
- **MIO-type, DIO-type** as in OPRES §2; on measurable carriers, DIO in its Heisenberg form
  (OPRES Proposition D).
- **Native class NAT.** Operations of the total carrier S satisfying clauses (ii) and (iii) of
  GATE-A r5.8's definition of observer-access procedure: every transition is a step of the
  substratum update on configurations, and outcomes and records are functions of configurations
  at declared times. NAT is used as a named premise; T-SUB′ is an option under D5, not adopted.

## 4. Assumptions, imported (I) and native (N)

| Label | Content | Kind | Source |
|---|---|---|---|
| KIN-B | configurations form an orthonormal basis of a complex Hilbert carrier; probabilities are diagonal entries | (I) | decision 4; OPRES §0 (KIN) |
| LIN | operations are represented by normal positive linear maps (CP where stated) | (I) | complex matrix kinematics (GR:213 setting) |
| DEF | S is the total system, and the dynamics is a map φ: S → S | (N) | `Main:42` |
| A2 | φ is deterministic (and, in the selected model, a bijection) | (N) | `Main:54` (Lemma 3); `Sub:94` |
| NAT | as in §3 | (N) as a reading; not adopted | GATE-A r5.8 §2.2, T-SUB′ (ii), (iii) |
| LAW | native preparations and hidden priors are configurations or laws over them | (N) | `Main:58`; ledger posit (iv) (`Main:736`); `EP:77` |
| CNT | carriers countable, unless a node states otherwise | scope hypothesis | — |

Everything quantum (complex amplitudes, CP maps, coherence) enters only through KIN-B and LIN.

## 5. Productivity test (§A.31), fixed before the walk

The investigation is a **gem** iff it yields a fact strictly stronger than the restatement
"conditional on R-READ, OI's stated operations lie in 𝒩 ⊆ MIO ∩ DIO" (OPRES §5) and than QOPS-P4's
RIG′ for the injective lift, **and** either (i) constrains a named open item of OPRES, READOUT-ALG
or QOPS-P4, or (ii) exposes a hidden assumption in how the native question has been posed.
Otherwise it is a non-gem (coherence relabelling). Below the propagation bar the result is
record-only.

## 6. Nodes and decision rules (depth-first; the decisive branch first)

- **N1 (decisive). Rigidity.** Does a deterministic configuration-level action fix MIO-type and
  DIO-type for every positive extension, without injectivity? *Rule:* a proof gives YES; an
  explicit positive extension of a deterministic action that is non-MIO or non-DIO gives NO, and
  that extension becomes the first candidate of N4. Also: state the sharpest necessary condition
  on p for an extension to be non-DIO, and for it to be non-MIO.
- **N2. Native operations at the total carrier.** Is every NAT operation, read on the total
  carrier, an extension of a deterministic action? Checked source by source (dynamics, readouts,
  records, controls, preparations, discards, the EP schema). *Rule:* any native operation found
  with a non-deterministic total-carrier action is a candidate for N4; otherwise the node closes.
- **N3. Reduction and record laws.** Do the visible instruments obtained from N2's operations by
  appending any hidden state and tracing out keep DIO, and on which inputs do native record laws
  depend? *Rule:* algebra on paper.
- **N4. Candidates, with maximum skepticism.** Each candidate the corpus contains or the reviews
  have named is assessed at (a), (b), (c). A candidate that re-imports quantum structure, a unitary
  dilation, an interpolation chosen rather than derived, or an ancilla in a coherent state is
  recorded as a representation, not a derivation. Candidates fixed in advance: 4a the continuous
  gate path (`GR:290`, `gateFlow`); 4b the unitary of the stochastic-quantum correspondence
  (`Main` §3.1); 4c the declared full observable algebra (READOUT-ALG items 24, 25); 4d a coherent
  hidden state, or a non-diagonal representative of a law; 4e the decoupled deep sector (`Main:736`
  item (ii)); 4f emergent visible stochasticity and P-indivisibility; 4g READOUT-ALG items 11 and
  12 under QOPS-P4's COH-REC.
- **N5. Carrier scope.** Measurable hidden carriers and non-normal states. *Rule:* if the notion
  of extension is not typable there without a new definition, record Missing and stop the branch.
- **N6. The blocking premise.** For each premise used by a negative in N1–N3, give an explicit
  paper example showing what fails when it is dropped, or record that it is not used.

Every node is closed by an explicit check (algebra, citation, or "needs computation: Missing,
stop") with its verdict recorded at the node. Claims are labelled **Established** (proved or
checked on paper in this note, or cited at the source's own standing; not established in the
§A.46 sense), **Assumed** or **Missing**, and (N) or (I).

## 7. Negatives and their scope

A negative is stated only for the class it rules out: operations in NAT, on countable carriers,
under KIN-B and LIN, with the premises listed at the node. It is not a statement about every
observer-level extension, about measurable carriers unless N5 closes them, or about models with
a non-trivial extension E. Failure to find a native mechanism is not shown to be impossibility of
one outside that class.

## 8. Stop conditions

- A node that needs computation: record Missing and stop that branch.
- A node whose answer would require a change to the physical model: name the premise and stop.
- Fixed point: stop when three consecutive passes over N4 yield no NEW finding.
- Nothing here runs, redesigns or ranks H-F1, H-RC or T-WP.
