# POSIT-MIN — preregistration: minimality criterion, decision rule and classification schema

**Status.** Writer's paper-only preregistration, committed and pushed before any per-item
classification is written. The classification is `AUDIT.md` in this directory, in a later commit.
Nothing here edits a manuscript, a Lean module or a registry, and no posit is adopted or dropped.
Independent non-author review is required before any use of the audit.

**Authorization.** Owner `amaybaum`,
[#1169 comment 7033247170](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7033247170),
2026-11-20T07:25:20Z, "Owner decision record: POSIT-MIN authorized; minimal-substratum principle".
Quoted limits: "POSIT-MIN: paper-only, authorized. Single writer (Claude), independent non-author
review, its own merge decision." "No manuscript edit. No posit is adopted or dropped; any proposed
change goes to the owner, and a Layer-0 revision is judged by the §A.29 test." "Reuse, don't redo.
The A1 audits: FCLASS, MAIN-ROOTS, A1-09, A1-NECESSITY, A1-REMAINDER and A1-SCOPE."

**Governing principle.** The §A.29 bullet of PR #1447 (branch
`docs/agents-minimal-substratum-20261120`, commit `7e52c8ad51726e30f5ce8764b7a3f12493687f57`, not
yet on `main`): "The substratum follows the most basic rules consistent with observation, and no
more. … A posit is kept only where observation forces it or a stated result needs it; it records
why it was chosen, and a weaker alternative is sought wherever one may exist. What counts as 'most
basic' is fixed by a criterion stated in advance, never chosen once the outcome is known."

**Goal link (§A.47).** Item served: #1169 (OI projection objective), through the owner's question
"which substratum posits are forced by observation and which are revisable". What the work decides:
for each of the fourteen items of Main's posit ledger, its reason, consumers, observational status,
weakest known alternative and standing, and the rule class the criterion below selects. It does not
decide which posits the framework keeps.

**Source pin.** `main` at `b9168ef0408b5f55b935a4df17cb0841877e221a`. `Main:n`, `SM:n`, `Sub:n`,
`GR:n` are line `n` of `papers/Main.md`, `papers/SM.md`, `papers/Substratum.md`, `papers/GR.md` at
the pin. Main's posit ledger is the single paragraph `Main:732`; its items are cited as
`Main:732 (k)`.

**Coordination.** Running units whose questions are cited and not duplicated: G3-W1 (conserved
energy of the `d = 3` rule), A1-PHASE2 (A1 companion ledger), the UNIV-2 revision. A1 (item (ii)) is
classified from the existing A1 audits only.

## 1. Inputs reused, not re-derived

| Short name | Path (all on `main` at the pin) | Used for |
|---|---|---|
| FCLASS | `verification/audits/foundations/a1-finiteness-classes-20261117/CLASSIFICATION.md` | finiteness classes F1–F4/A1 |
| MAIN-ROOTS | `verification/audits/foundations/a1-main-roots-20261118/{ROOTS,AUDIT}.md` | Main's roots and their A1 dependence |
| A1-09 | `verification/audits/foundations/a1-09-dependency-census/CENSUS.md` | corpus census |
| A1-NECESSITY | `verification/audits/foundations/a1-necessity-20261117/ASSESSMENT.md` | five-family table |
| A1-REMAINDER | `verification/audits/foundations/a1-remainder-20261119/REMAINDER.md` | consumer table, residues R1–R6, replacement hypotheses |
| A1-SCOPE | `verification/audits/foundations/a1-scope-phase0-20261120/` | site map and sufficient conditions |
| O-A4 | `verification/audits/foundations/o-a4-20261120/RESULT.md` | A4 without the finite periodic lattice; Theorem 19 on `ℤ^d` |
| NR-1 | `verification/audits/foundations/nr1-near-return-20261116/NR-1.md` | selected update on `ℤ^d` under Haar |
| R1-INF | `verification/audits/foundations/r1-inf-20261119/RESULT.md` | default law on an infinite carrier |
| A5-LA | `verification/programmes/substratum/a5-linear-affine-20261104/A5-LINEAR-AFFINE.md` | A5 dependency inventory D1–D16; selection principles N1–N11 |
| H-A, H-B | `verification/programmes/hydrodynamics/round-h-{a-source-audit,b-reversible-fluid-substratum}/result.md` | linearity gate on coarse closures |
| OA-1 | `verification/programmes/oi-qm/reconstruction/oa-1-20261112/OA-1-REPORT-r5.md` | D5 (Lemma A, affine rules) |
| MR★ | `verification/programmes/oi-qm/reconstruction/measurement-record-formation/amendments/MR-star.md` | S-L1, S-C1, S-L4, AW-MR8, AW-MR9 |
| SEL-SYN | `verification/programmes/oi-qm/reconstruction/selection-discriminator-20261113/support/synthesis/SYNTHESIS-r3.md` | MM-4 |
| UNIV-1 | `verification/programmes/oi-qm/reconstruction/univ-1-20261119/RESULT.md` | Theorem L |
| DL1, NP1, PR1 | `…/deliver-1-20261119/RESULT.md`, `…/natprep-1-20261119/RESULT.md`, `…/prep-regress-1-20261119/RESULT.md` | measurement-sourcing limits |
| C1C4-MIN, MIN-REP | `verification/audits/foundations/{C1C4-MINIMALITY-AUDIT,MINIMAL-REPERTOIRE-AUDIT}.md` | earlier minimality work (different objects) |

Every input is a research record or a manuscript statement. None is treated as established beyond
the layer it states for itself (§A.46 item 7): a [W]/[D] derivation in an input stays [W]/[D] here.

## 2. Classification schema (per ledger item)

Each of the fourteen items receives one row with five fields, each with file:line evidence.

- **(a) Reason chosen.** Quoted from the corpus, then typed: `EMP` (an empirical motivation is
  stated), `CONV` (stated as a choice or selection of a model), `RES` (stated as needed by a named
  result), `REP` (stated as a representation choice), or a combination.
- **(b) Consumers.** The results that use the item, across Main, the companion papers, the Lean
  modules and the verification records, cited from existing audits where a row exists.
- **(c) Forced by observation?** `FORCED` (an observation in §3 implies the item, for the object the
  item is about, with the implication cited at its support layer); `PARTLY` (an observation forces a
  strictly weaker statement, which is named); `PRESUPPOSED` (every observed requirement in §3
  presupposes it, and no observation can bear on it); `NOT FORCED`.
  Ontic and emergent objects are kept apart: an observation of the emergent description forces an
  ontic clause only through a cited implication.
- **(d) Weakest known alternative.** The weakest alternative found in the corpus or in the cited
  literature, with its sufficiency status for the item's consumers: `proved` (cited, with layer),
  `partial` (for some consumers), `none traced`.
- **(e) Standing.** One of:
  - `forced` — (c) is `FORCED` at the item's stated scope, at a reviewed layer;
  - `refuted` — a valid counterexample or a contradiction with an observation in §3 that uses no
    hypothesis beyond those the item's own statement and Main's adopted branches carry;
  - `in tension` — a contradiction with an observation in §3, or with another ledger item or an
    adopted branch of Main, that holds under stated further hypotheses, each named;
  - `open` — none of these.
  An item may carry `open` together with a presupposition label (`PRESUPPOSED`), and `in tension`
  lists every hypothesis under which the contradiction holds.

## 3. The minimality criterion (fixed here, before the classification)

### 3.1 Observed requirements

Each requirement is stated as an observation, with its observational basis, and then as the
rule-level reading the corpus has proved or stated, with the layer. A requirement's rule-level
reading is admitted into the criterion only at the scope the cited implication reaches.

- **O1 — Operational locality.** *Observation:* no signal has been observed to propagate faster than
  a finite maximal speed, and spacelike-separated setting choices do not change remote marginal
  statistics (relativistic-causality tests; the marginals of Bell experiments, `Sub:78` E2).
  *Not part of O1:* ontic locality of the substratum. Main's Bell theorem (`Main:366–391`) shows
  that a deterministic, screened, cone-local completion has `|S_CHSH| ≤ 2`; with observed Bell
  violation (E2), ontic cone locality for Bell-relevant degrees of freedom is not an observed
  requirement and is excluded under measurement independence (`Main:403–412`).
  *Rule-level reading:* none forced. The corpus's sufficient route to the emergent property is the
  coupling-graph cone over finite read sets (`Main:364`), which is a result-needed clause (§3.3).
- **O2 — Reversibility as observed.** *Observation:* isolated-system dynamics is unitary to tested
  precision, with no observed intrinsic collapse (`Sub:76` E1; `Sub:94` A2, matter-wave interference
  at macroscopicity 15.5). *Rule-level reading:* the observation constrains the effective quantum
  dynamics, not ontic bijectivity (A1-REMAINDER M11). Restricting to reversible representatives
  excludes no finite-horizon visible law, since every such law has a finite reversible deterministic
  realization (`Main:80` item (1), `S ⇔ D ⇔ Q_fb`). Reversibility therefore enters as a
  representation clause (§3.3, class `REP`), not as an observation-forced clause.
- **O3 — Stable records.** *Observation:* observers hold registered distinctions in bounded loci,
  and these persist over many update times and remain mutually consistent (memories, written and
  instrumental records; Axiom 1 registration `Main:36`, the finite-capacity locus of the Definition
  `Main:42`, and (C2-structural) retention `Main:74`). *Rule-level reading:* (i) preservation of
  registered distinctions gives injectivity on states with different registered content
  (`Main:36`); (ii) persistence in a bounded locus requires either a confined persistent pattern of
  the configuration or an observer-level carrier; which of the two a rule class supplies is read
  from the cited records.
- **O4 — Interacting signals.** *Observation:* the effect of a local stimulus on a later local
  readout depends on the state of another local system (a detector registers only when armed; a
  collision deflects; a switch gates), and a record so produced can select a later operation on a
  further system (feed-forward control, cascaded logic). *Rule-level reading:* at the configuration
  level, with settings, records and carriers taken as cell content ("inclusion"), an affine update
  excludes this: the effect of a change is the same whatever the other regions hold (MR★ S-C1), and a
  stored setting acts on a carrier only by translation, for every measure (OA-1 D5). Whether O4 read
  at the observer interface excludes affine updates is not settled in the inputs; the audit states
  the scope at which the exclusion holds and does not extend it.

### 3.2 Further observations already cited by Main or the companions

Fixed now, with their sources, so that no observation is added after the classification:
E1 unitarity (`Sub:76`); E2 Bell violation (`Sub:78`); E4 spatial isotropy (`Sub:82`); E6 stable
matter (`Sub:86`); the homogeneity anchor of A4 (`Sub:98`); observed non-Markovian memory as the
necessity anchor of C1 and C4 (`Main:72`, `Main:78`). An inferred quantity (E3, E7) is not used as
an observation (§A.24).

### 3.3 Clause classes and the selected class

A rule class is given by a set Σ of clauses on `(S, φ)` and its interface. Class `R(Σ₁)` is more
basic than `R(Σ₂)` exactly when `R(Σ₁) ⊋ R(Σ₂)` (fewer restrictions). Each clause is typed:

- `PRE` — presupposed by the observed requirements themselves;
- `OBS` — implied by O1–O4 or §3.2 at the cited scope and layer;
- `REP` — a representation choice proved to lose no finite-horizon visible law;
- `RES` — the hypothesis of a named result, kept only because that result needs it;
- `CONV` — stated as a choice of model, with no observation or result requiring it.

The criterion selects two classes, reported separately so that the cost of each result is visible:

- **R_obs** = `R(Σ_PRE ∪ Σ_OBS ∪ Σ_REP)`: the most basic class consistent with observation.
- **R_res** = `R(Σ_PRE ∪ Σ_OBS ∪ Σ_REP ∪ Σ_RES)`: R_obs restricted by the hypotheses of the named
  results the framework retains, each result named beside the clause it costs.

`CONV` clauses belong to neither. A clause in tension with an `OBS` clause cannot be in R_res; it is
reported with the results that consume it.

### 3.4 Decision rule per ledger item

- `KEEP` — the item is a `PRE`, `OBS` or `REP` clause at its stated strength.
- `KEEP-RES` — the item is needed only by named results; it is kept conditional on them and the
  results are named.
- `WEAKEN` — a strictly weaker clause carries what observation forces and what the item's consumers
  need, or most of it; the weaker clause, its sufficiency status and the consumers it does not
  carry are stated.
- `FLAG` — the item is `CONV`, or it is in tension with an `OBS` clause or with an adopted branch
  of Main; the conflict and its hypotheses are stated.

Verdicts can combine (`KEEP-RES + FLAG`). A verdict is a proposal to the owner, not a change.

### 3.5 Controls

- **K1 (no edit).** The diff of this unit touches only this directory.
- **K2 (A1 audits authoritative).** Item (ii)'s row cites A1-REMAINDER §3, A1-NECESSITY §3 and
  A1-SCOPE; its standing must agree with A1-REMAINDER's verdict ("posit (ii) cannot yet be replaced
  by observer-relative finiteness alone"). A disagreement is reported as a finding, not resolved.
- **K3 (discrimination).** If all fourteen items receive the same verdict, the criterion is
  declared non-discriminating and the classification void.
- **K4 (positive control).** Item (xii), which Main states "imposes no restriction on the rule"
  (`Main:732`), must not be classified as an observation-forced restriction; Axiom 1 (indubitable,
  `Main:36`), used as a control outside the fourteen items, must be classified `PRE`.
- **K5 (countercontrol on O4).** The audit must exhibit, or cite, a case showing that O4 read at the
  observer interface without a locality condition on the coarse-grained variables does not exclude
  affine rules, so that the configuration-level scope of O4's reading is checked rather than
  assumed.
- **K6 (pressure on favourable readings, §A.31).** Every `forced` standing and every `KEEP` verdict
  is restated with the strongest objection found, before it is recorded.

### 3.6 A5 and UNIV-1, fixed questions

The audit answers these as separate rows:

1. What Main uses A5 for, with every Main line that cites ledger item (vii).
2. What UNIV-1 Theorem L shows and its scope, at its stated layer and review status.
3. What Theorem L does not imply for observers, records or measurement, checked against DELIVER-1,
   NATPREP-1, PREP-REGRESS-1, OA-1 D5/D6 and MR★.
4. Whether any observation in §3 is contradicted by A5 under named hypotheses.

## 4. Productivity test (§A.31)

The unit is productive iff it records at least one of: an item whose standing in §2's sense differs
from the label Main gives it; a conflict between two ledger items or between an item and an adopted
branch of Main, located with file:line evidence; or a weaker alternative with a proved or cited
sufficiency that the ledger does not name. Otherwise it is a relabelling and is reported as such.

## 5. Off-`main` references (§A.42 item 8)

- PR #1447 and its branch commit `7e52c8ad`: **provenance** for the principle; the criterion above
  is stated in full here and does not use content held only on that branch.
- Running units G3-W1, A1-PHASE2, UNIV-2 revision: **provenance**; nothing here uses their content.
