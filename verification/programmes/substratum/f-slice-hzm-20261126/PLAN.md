# F-SLICE-HZM: does the centred label-sector J supply what Theorem 5's Σ and H-PF consume? Plan

**WIP / UNVERIFIED. Model-written research record, paper-only. Committed on its own before any
derivation is recorded. Recorded, not frozen. Nothing here is adopted, proposed for the
manuscripts or authorized beyond the unit scope. No premise is adopted, weakened or changed.
Replacing or narrowing H-ZM, or adding a bridge premise, would be a premise change (§A.29, §A.50
item 6); this unit only traces and derives.**

The writer read the input records of §1 before writing this plan, and began considering the
question while reading. No derivation is recorded before this commit, and the decision rule of §4
names classes and the rule that maps them to an outcome, not expected results.

- **Accountable Issues:** #1217 (COMPLEX-CARRIER-1) and #1049 (linear vs affine microscopic
  dynamics); programme #1169.
- **Work package:** WP-2, scientific research. Its record is #1169 comment 7199704501 (author
  amaybaum, created 2026-11-26T17:49:03Z; owner decision "Proceed as suggested", received
  2026-11-26T17:49Z).
- **Authorization:** #1169 comment 7200549806 (author amaybaum, created 2026-11-26T18:30:55Z;
  owner decision received 2026-11-26T18:30Z, coordinating session), item 4: "Authorize all three
  ranked scientific investigations — SMD sourcing, uniform norm control and F-slice — at
  paper-only level, with independent review and bounded stopping conditions."
- **Question source:** rank 3 of the successor assessment, #1169 comment 7191949320 (author
  amaybaum, created 2026-11-26T12:23:54Z): "Check whether the centered label-sector J supplies the
  inputs actually used by Theorem 5's Sigma and H-PF." and "A test must trace the real-lift
  dependency and check the theorem's consumers before any change to H-ZM."
- **Goal link (§A.47):** #1217 and #1049. The unit decides, for each input of Theorem 5 that
  consumes lane 2's Proposition 5 (the null-sector exclusion at the massless point on the torus),
  whether Unit C's F-slice supplies it, supplies it only under a named further premise, is
  obstructed, or is not consumed. This decides whether lane 2's "exclusion requires the named
  hypothesis H-ZM" can be narrowed for Theorem 5's purposes. It does not decide the outcome, and
  it does not change H-ZM.
- **Not in scope.** SMD sourcing (a parallel investigation, rank 1): the state conditions L-SDS,
  TPC and SMD are carried as Unit A records them and are not investigated here. Carrier Z
  (H-top), the SM:811 energy, the register question O2 of Unit C and the amplitude-scale gauge O1
  of Unit C are not investigated.
- **Pinned main commit [P]:** `a8d4ab969e274dc6ba25cbc6021da909d5aec814`. `papers/` at [P] is
  identical to `papers/` at Unit A's and Unit C's pin `353a066f18766837fed8c7f58507e09ff549b1a4`
  (empty `git diff` for `papers/`), so their SM line numbers hold at [P].
- **Writer:** the designated writer of branch `research/f-slice-hzm-20261126` under WP-2. No push
  and no GitHub write is made by this unit.

## 1. Inputs (all on `main` at [P])

| Label | Source | Content used |
| --- | --- | --- |
| C3 | `verification/programmes/substratum/hzm-energy-sourcing-20261126/REPORT-r3.md` §5.3, §11 O3 | F-slice steps (a)–(d), its pressure test and open node O3 |
| L2 | `verification/programmes/oi-qm/reconstruction/complex-carrier-20261126/REPORT-r2.md` and `PRESERVATION.md` | Lemma 0; Theorem 1; Propositions 2–5, 7, 8, 11; Counterexamples 9, 10; the H-PF definition (§4, §6); the named assumptions table (§5) |
| A | `verification/programmes/oi-qm/reconstruction/theorem5-premise-ledger-20261126/REPORT-r3.md` | The premise ledger of Theorem 5 (§2): H6-Φ, P1, P2a–P2e, L-NZM and their carried premises; Lemma 1; Propositions A–D |
| SM | `papers/SM.md`: SM:222, 230, 232, 240, 290, 292, 298, 312–316, 322, 334–344, 360–364, 374, 505 | Theorem 5, its proof, its scope, the observer-level branch and the lift's status |

The three records are reviewed model-written paper derivations, not independently verified
theorems (§A.46 item 7). A result of them used here is used as a named conditional input, with
its label.

## 2. Question

Q. At the massless point on the torus T (αμ = 1/d, M = μI_6, b = 0, L even or odd), let ρ be an
F-stationary law with finite second moments. Unit C's F-slice replaces lane 2's quotient by the
static subspace L_0 with the label sectors x*(t) + V_rest and a J on each. For each item of Theorem
5's premise ledger (Unit A §2), does the F-slice supply what that item consumes from lane 2's
Proposition 5?

Sub-questions, each answered with its own trace:
- **Q-lift.** The real-lift dependency: every premise between SM:232 and the F-slice output, with
  its status (proved / conditional / posited / open).
- **Q-J.** What object the F-slice supplies: a complex structure on which space, and how it
  relates to Proposition 5's reduced J.
- **Q-cons.** For each consumer of Proposition 5 in Theorem 5 (from Unit A: H6-Φ, P1, P2a with
  H-PF, P2b–P2e, L-NZM; and layer M items P3–P5), the class of §4.
- **Q-dir.** Where a named further premise X is needed, its directional relation to H-ZM, each
  direction separately (§A.34).

## 3. Method

1. Trace Q-lift from SM text and the named assumptions of L2 §5; label each link.
2. Derive Q-J by exact hand algebra [A], or reasoning [W] where an argument is not pure algebra.
3. For each consumer, read Unit A's ledger row and the step of Theorem 5's proof (SM:342) that
   consumes it, identify what it reads from the reduced space, and classify (§4).
4. Apply the controls of §5 before printing any verdict.
5. Depth-first (§A.12, §A.31): resolve each consumer to a class before moving on; apply maximum
   skepticism to any favourable classification.

Labels: [A] exact hand algebra here; [W] reasoning here; [L2], [A-rec], [C3] for results of the
input records, carried as conditional inputs; [P] text quoted at [P]. No computation is run and
no Lean is built (paper-only authorization).

## 4. Decision rule

Each consumer κ of Proposition 5 is assigned exactly one class:

- **NC (not consumed):** κ reads nothing from Proposition 5's output.
- **S (supplied):** the F-slice output provides κ's input, under the premises Proposition 5's route
  already carries other than H-ZM (LIN, LIFT, b = 0, the stationarity that Proposition 4 uses, and
  lane 2's Theorem 1).
- **S|X (supplied under X):** as S, but only under a named further premise X that no stated premise
  supplies. X is recorded and not adopted.
- **OB (obstructed):** a controlled argument or witness shows the F-slice output cannot provide κ's
  input under any reading of κ within the stated scope.

Outcome, generated from the classes:
- **R1, route around H-ZM:** every consumer is NC or S. The record then states that, for Theorem
  5's consumers, H-ZM can be replaced by the F-slice under the carried premises; it proposes
  nothing for the manuscripts.
- **R2, route under a further premise:** no consumer is OB, and at least one is S|X. Each X is
  recorded with its directional relation to H-ZM (Q-dir), and the unit stops (§3 of the stopping
  conditions below).
- **R3, controlled obstruction:** at least one consumer is OB under every reading. The obstruction
  and its witness are recorded.

Where a consumer admits several readings, each reading is classified separately; the consumer's
class is the most favourable class over readings that Theorem 5's text admits, and the reading
that gives it is stated. A consumer is OB only if every admitted reading is OB.

## 5. Controls and countercontrols

| Id | Kind | Requirement | Fails if |
| --- | --- | --- | --- |
| C+1 | positive | Off the massless point (abs(μ) < 1), where there is no null sector, the method must classify every consumer as Unit A's ledger does without H-ZM | any consumer is classified differently from Unit A at abs(μ) < 1 |
| C+2 | positive | Under H-ZM, the method must reproduce lane 2's Proposition 5: every consumer S given H-ZM | a consumer Unit A marks as carrying H-ZM is not supplied under H-ZM |
| C−1 | countercontrol | A reading of Σ that keeps the static labels inside ⟨φφ†⟩ must be tested against P2a by an explicit witness, and must not be classified S unless P2a survives | that reading is classified S without the witness check |
| C−2 | countercontrol | Complex structures excluded by lane 2 (site-local, untamed, or not commuting with F) must not be accepted as supplying H6-Φ | such a structure is accepted |
| C−3 | countercontrol | With b_A1 ≠ 0 at resonance the F-slice must be found empty (no stationary law), not supplying | it is classified as supplying anything |
| C−4 | extraction | Every quote re-read at [P] | a quote does not match |

A verdict prints only over green controls. A failed control voids the verdict, and the record
states which control failed.

## 6. Stopping conditions

1. The decision rule resolves (R1, R2 or R3) with all controls green.
2. Bounded effort: at most four depth-first passes over the consumers. If the rule has not
   resolved, the remaining gap is stated precisely and the unit stops.
3. A new premise would be needed (an S|X class, or an X needed to state the F-slice itself): it is
   recorded, with its directional relation to H-ZM, and the unit ends there (§A.29, §A.50 item 6).

## 7. Productivity test (§A.31)

Gem iff the unit yields a fact strictly stronger than a restatement of C3 O3, and either
constrains how H-ZM may be replaced or exposes a hidden assumption in the F-slice or in a consumer.
Otherwise non-gem (coherence relabelling), record-only.

## 8. Outputs

- `REPORT.md` in this directory: the trace, every premise labelled proved / conditional / posited /
  open, the per-consumer classes, the controls, the outcome against §4, the scope, and the open
  nodes. Committed separately from this plan.
