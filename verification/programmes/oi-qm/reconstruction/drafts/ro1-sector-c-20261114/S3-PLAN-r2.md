# S3: physical executability of operations by an embedded observer — plan, r2

**UNREVIEWED. Plan only, for owner decision.** This document plans paper-only work on stop S3. It
does no scientific work: no candidate is derived or evaluated, no premise is adopted, no
computation, Lean, manuscript edit or merge is made, and no Issue's scope, authorization or writer
changes. Nothing in it starts until the owner authorizes a unit.

**Authority.** Owner decision record, #1169 c.6884568026 (`amaybaum`, 2026-11-14T21:36:37Z, "Yes I
confirm, proceed as suggested"), item 4:
- "The next item to investigate is the physical executability of operations by an embedded
  observer."
- "The work is accountable to #866 and #913. It does not duplicate their obligations or change
  their current authorizations."
- "The first unit will be a bounded, paper-only **plan**, presented for owner authorization before
  any new scientific work starts."

The same record accepts RO1-DEPS-r4 at `549b1056` with verdict UNDETERMINED, and keeps S1–S3, S5–S12
and X1–X5. Its item 5 keeps C-1 under #1234.

**Revision.** r2 applies the independent review of r1 (`REVIEW-S3-PLAN-r1.md`, REVISE at `38b5a460`):
- F1: route M is no longer closed early, and a decisive test is named (§§8.4, 8.6);
- F2: the negative controls are split into those on record and those needing an MR-1 stage-2
  authorization (§8.5);
- F3: U2 and U3 are narrowed, and their dependencies on #866 and #913/#914 are stated (§§2.3, 9);
- F4–F9: the remaining findings.

Dispositions are in `RESPONSE-S3-PLAN-r1.md`. r1 (SHA-256
`582cb1413f683bfbabda523eaaa49707020f0629b6b3f55ce31037e9d6c19ac4`) is left unchanged.

**Owner's additional requirements** ("Confirmed, proceed as suggested", `amaybaum`, 2026-11-14) are
built into this revision: the four-way separation, three explicit points and outcome tiers for route
M (§8), and, for U4, the tier it can reach (§9). C-1 stays independently open under #1234.

**Writer:** Claude Code. **Base:** `origin/main` `dfeec843`. GitHub records were read through the
REST API on 2026-11-14: #866 (body and 71 comments), #913 (body and 3 comments), #1169
c.6884568026, and #1023 c.6555169983.

**Labels**, as in RO1-DEPS-r4:
- **[R]** existing result, with its evidence state:
  - *main*: a manuscript statement;
  - *kernel*: a Lean statement, read and not built;
  - *record on main*: a paper-level verification record on `main`, not established (§A.46 items 1
    and 7);
  - *reviewed, not merged*;
  - *off-main record*.
- **[P]** proposed obligation or definition.
- **[A]** unproved assumption. **[A-inf]** marks an inference drawn here, unreviewed.
- **[STOP]** a point that needs an owner decision.

***

## 1. Target question

**Ultimate goal (not a step).** For one fixed OI model `M = (S, φ, μ, Obs, Γ, R, Res)` (RO1-SPEC-r3
§2.1), determine the set `Γ_exe(M)`: the experiments an embedded observer can physically execute
using only `M`'s own dynamics and resources. Decide whether, on that one set, quantum coverage and
quantum-set soundness can both hold (RO1-DEPS-r4 §7.7, X4, X5).

**What S3 asks of the plan.** RO1-SPEC-r3 S3 asks two questions:
- "Are the programs of §5.1, the single-use test included, executable in any OI model (O10)?"
- "What criterion gives 'executes through `Obs`'?"

RO1-DEPS-r4 makes S3 the first open step of track (d), "A definition of 'executable'", and part of
track (c)'s step 2.

**Three levels, never conflated.** [R, record on main] They are taken from MR-1
(`verification/programmes/oi-qm/reconstruction/measurement-record-formation/preregistration.md` §1):
- **Representable.** "a mathematical representation exists".
- **Available.** "an executing physical process exists in the declared interface: every operation,
  setting change, readout, reset and inverse is a composition of native steps under the declared
  access, with its resources accounted".
- **Derived.** "available from the OI premises at `D` … with no added resource".

[P] S3 uses these levels and does not invent new ones. `Γ_exe(M)` is the set of *available*
programs. A program in `Γ_exe(M)` that needs no added resource is *derived*. D-real and D-glue
(RO1-DEPS-r4 §1.2) are *representable* results, and do not place a program in `Γ_exe`.

## 2. What #866 and #913 already own, have established, and authorize

The plan builds on these records and does not restate their work. Each item below is cited at its
source.

### 2.1 #866: "P0: physical observable carrier and evolution selection"

**Owned obligations (body planning table).**
- **NATIVE-PREP-SRC-1** and **NATIVE-INT-SRC-2**, the source-first preparation producer and native
  observer–apparatus interaction.
- **CP-PREP-1**, the physical controller lead.
- **P0**, **O-OBSMU** (`(Obs, μ)`), **O-REC** ("how an interaction produces a readable, persistent
  record") and **O-SET** (setting-dependent interaction, NC-1).
- The 2026-11-06/07 bounded units: preparation/control/readout, record-to-control,
  hidden-correlation recombination, the native recombination no-signalling screen, the common
  physical interface, and T1 preparation/loading.
- MR-1 (measurement as record formation) is held under row O-REC (#866 c.6631480154).

**Established or refuted, at scope:**

| Item | Result at scope | Evidence state |
|---|---|---|
| CP-PREP-1 | "Native interaction source gate: NOT PASSED". The first missing link is "an executing interaction under the selected fixed OI rule, together with accounted incoming preparation/control resources, timing and setting source" (#866 c.6719027303) | Merged as `9c201475` (#1197); record on main |
| Controller lead | "No controller passes the physical source gate"; the missing ingredient is "an accounted native producer of that complete ready/request law" (#866 c.6713088252) | Merged (#1185); record on main |
| O-OBSMU | Reviewed record integrated; "physical premise decisions remain open" (body) | Merged as `52542985` (#1110); record on main |
| MR-1 stage 1 | Scoped GAP. On the K1 rule: "Superposition excludes setting-dependent transfer", "Marking cannot destroy interference; only added independent noise can (S-L5)", "The inverse is representable but not available (S-L3)"; classical record formation G for "the **absence of a physically sourced quiet, ready region**"; the trace route UNDECIDED (#1023 c.6555169983). The token is provisional: "It stands only if a controls-only stage 2 … returns every reference result … otherwise it is `VOID`" (README) | Record on main (`measurement-record-formation/`); stage 2 not authorized |
| PC-1 | Scoped gap; on main (#866 c.6627392555) | Record on main |
| NATIVE-INT-SRC-2 | "STOPPED / UNSOURCED; physical source NOT PASSED. Stage B not entered" (body) | Reviewed, not merged (#1223 at `862a493d`) |
| NATIVE-PREP-SRC-1 | "No producer of the proposed ordered bank/common incoming law and selectable request is sourced". The supplied bank needs 13/15/17 additional fixed hidden coordinates for L = 9/10/≥11, "for that chosen bank, not a universal physical cost or minimum" (#866 c.6765674746) | Reviewed, not merged (#1225 at `dbb57b6d`) |
| 2026-11-06/07 units | All conditional, all stopped at the physical preparation/setting/access map: receiver law (`813b7263`); recombination (`9d24914c`); no-signalling screen, "STOP … no physical no-signalling PASS or FAIL" (`d3754dfc`); common interface, "a conditional source-based local component, **not a complete physical Bell interface**" (`235305e2`); T1 (`ba777f85`); observer-interface source, "no physically motivated candidate" (`35aaa4c8`) | Reviewed, not merged (draft #1173) |

**Current authorization.**
- No #866 unit is running under an authorization recorded in its body.
- NATIVE-PREP-SRC-1's one-unit authorization is completed ("not permission for another source
  screen", c.6765674746).
- NATIVE-INT-SRC-2 is "blocked: native ready/request producer and persistent-record source".
- O-REC is blocked on O-RET and O-ACC, and MR-1 stage 2 is not authorized.
- O-SET's gate existence is "ready", paper-only under PO-1102 workstream C.
- P0 is "not authorized".
- A Codex native apparatus source screen was handed off on 2026-11-13 (c.6863601327: "Codex task
  dispatch/execution itself is not established by this GitHub comment").
- Standing writer ownership was reset on 2026-11-14 (c.6880247299).
- Physical source: NOT PASSED.

### 2.2 #913: "OI reconstruction: remaining foundations, generalization and A2 gates"

**Owned obligation.** **O-REUSE**, "Reusable instruments, composition and freshness". Tier
Foundational; prerequisite O-INS (#914); readiness "blocked: O-INS"; authorization "not authorized"
(#913 body; owner decision recorded at c.6628909432). #913 also holds the work loci of #885
obligations 5 and 6, whose accountable home stays #914 (c.6628909432):
- "Native preparation, settings and clock";
- "Observer-access closure";
- "Arbitrary depth and measurement menu";
- "Composites and Bell structure".

**Established or refuted, at scope:**
- [R, record on main] The conditional finite-depth composition theorem: "a sufficient contract, not a
  characterization". Its fresh-resources route: "An independent initial seed bank supplies this
  condition only when earlier dynamics and access have not used it or conditioned on it in a way that
  changes the relevant joint law" (`composition-access-20261024/REPORT.md`:57–69).
  - #913's status-source cell names this file "branch … only, not `main`". It has since landed on
    `main` (commit `86cd47e5`, an evidence landing). The cell is stale, and correcting it is #913
    maintenance, not this plan's.
- [R, off-main record] #912's packages (branch `draft/oi-composition-access-20261024` at
  `2af1d5d5`), as indexed in c.6628909432:
  - "Reuse of the unchanged carrier leaves the decoder cone" (`native-x-v2/`);
  - "Gates, storage, clock and isolation are supplied, not derived" (`composition_flag_v6/`).
- [R, off-main record] #911's "exact fixed-vector reset-reuse audit finds a public-record error";
  "supplied independent-pair renewal keeps continuous-resource costs explicit" (#913 body).

**Current authorization:** none; O-REUSE is "not authorized".

### 2.3 Related homes, not to be duplicated

| Home | What it holds |
|---|---|
| #1032 (O-RET) | Retention, including cross-read coherence retention (#1143 c.6692765618) |
| #1147 (O-RDY) | Readiness (#866 c.6665471504) |
| #865 | The drive |
| #1007 | Carrier foundations. The owner's working definition of Q1: "A common refinement that is genuinely available through the declared native access interface, under the same preparation, should withhold the setting-controlled-interaction label … This is a working definition, not a proof that such a refinement physically exists" (quoted in #866 c.6719811801) |
| #1143 | The discriminators and countermodels: SEL-ACCESS-1, SEL-EXCL-1, SEL-DISC-1 |
| #1060, #868 | Bell soundness and coverage |
| #914, row O-INS | The accountable home of #885 obligations 5 and 6: native preparation, clock and settings, access closure, unrestricted depth and menu, composites and Bell. Their work loci are #913's gates "Native preparation, settings and clock" and "Observer-access closure" (#913 c.6628909432) |
| #866, Codex's native apparatus source screen | Allocated 2026-11-13 (#866 c.6863601327). It classifies "(i) a ready configuration, (ii) a selected setting/intervention, (iii) a held readout and failure history, and (iv) resources for repeated runs" as "**derived / assumed / absent**" for one candidate. Whether it is running is not established on the record. Under the ownership reset, work in flight "keeps its existing writer" (#1169 c.6880239486) |
| #1234 | C-1 |

[P] **Demarcation.**
- **U1** fixes a criterion that RO-1 uses as a definition only, for S3 and the sector-C frame. It does
  not discharge #913's or #914's access-closure or preparation obligations, or #866's sourcing.
- **U2** classifies only RO-1's own control programs, and reads the Codex screen's result for native
  candidates rather than classifying them anew.
- **U3** states closure as a definition for RO-1. Any closure or renewal finding is routed to
  #913/#914 (O-REUSE, O-INS) without being discharged there.

## 3. The native criterion for each action (to be specified in unit U1)

[P] For each action, unit U1 states what counts as "executable through `Obs`" (the *available*
level of §1). It keeps an **assumed apparatus capability** separate from an operation **sourced in
the native dynamics**.

The verdict vocabulary is #866's existing source matrix: "*derived / assumed / unsourced /
disproved*" (#866 c.6763916830, Stage A item 5). Two owner rules also apply:
- NATIVE-INT-SRC-2's rule: "An assumed inverse image, conditional event, prepared state or
  adjustable control label is **not** a producer".
- The Q1 working definition (§2.3).

| Action | Candidate criterion for U1 to fix (proposed, not adopted) | Assumed capability, if not met | Existing source of the requirement |
|---|---|---|---|
| Preparation | A native process, started from `μ` with accounted ready cells, that brings a region to the prepared configuration law. Conditioning on an outcome is not a preparation | A supplied ready region or bank | MR-1 GAP ("quiet, ready region"); NATIVE-PREP-SRC-1; RO1-DEPS-r4 D-A8, P-super |
| Setting choice | A native process that writes a setting value, with its producer named. **Independence of the setting's law from the unused source is not part of the criterion.** It is a property each classified record must decide, as a property of `μ` (MR-1 AW-MR7; preregistration §5.6: "Setting independence is decided as a property of `μ` … never assumed"). It is conditional on S5 (ledger Q8) | An exogenous label `I_a` (Main:482); a stipulated controller | SEL-EXCL-1 l. 46 ("specified, not derived"); MR-1 AW-MR7; CP-PREP-1 |
| Intervention | A composition of native steps whose *operation* is selected by the written setting, with no declared operator outside `φ`. [P] An additive offset that depends on the setting is recorded separately, as a setting-dependent *output*, and does not count as a setting-selected intervention. MR-1: "Setting-dependent outputs remain possible as offsets" (#1023 c.6555169983), while on K1 the setting "selects no operation" (S-C1(a)) | A declared operator (P-mix, P-phase) | MR-1 S-C1; D-iv, D-nonneg |
| Complete-record writing | A native process that leaves a persistent, readable record in `V`'s configuration, with failures, heralds and timing, and with no discarded mass | A supplied pointer or blank marker | O-REC; MR-1 §3.1–§3.2; K-rec (RO1-SPEC-r3) |
| Retention | The record persists to the readback that uses it, within the declared access | Supplied storage | C2-structural (Main:74, :80); O-RET (#1032) |
| Renewal | A native process that supplies fresh source cells, ready regions or blank markers, with resources counted | A supplied fresh bank | §4; O-REUSE (#913) |
| Composition | The executable set is closed under the compositions in §5, each itself executable | Supplied gates, clock, isolation | `composition_flag_v6/` ("supplied, not derived"); `REPORT.md`:57–69 |

[P] **The access declaration (F5).** MR-1's *available* level is relative to "the declared access",
and the access is a free choice that can decide outcomes.
- [R, record on main] Whether the native access is an epistemic restriction depends on which slices it
  reads: "An access that reads the current slice at a single time is an epistemic restriction …
  Which slices the access reads is not fixed by the sources" (S-L7, `amendments/MR-star.md`:603–618).
- S-L7 cites SM:252 for the visible/hidden slice assignment. At `main` `dfeec843`, SM:252 is Lemma 1c,
  so the citation has drifted.
- U1 therefore **freezes the access declaration**, with its source re-pinned, before any
  classification. K-2 covers it.

[P] **Constraint on U1.** The criterion and the access declaration are stated without reference to
quantum outcomes (§6, K-2). Both are preregistered before U2 classifies any record. **[STOP]** If fixing it
requires the typing choice S7 (where an operation lives) or the identity relation O11 (S1), U1 stops
and asks the owner.

## 4. Renewal and resources

What is on record:
- [R, reviewed, not merged] **Same-seed reuse** with a retained first record makes the PR
  implementation signal in complete local histories. A **fresh-cell** supply restores no-signalling
  (SEL-EXCL-1 §§3, 7 at `0ecfddeb`). RO1-DEPS-r4 §5.1 records this as the one partial discriminator.
  Its scope: it rejects only the same-seed implementation, and only if that continuation is
  executable.
- [R, reviewed, not merged] "Scarcity alone is not a separator". A closed finite world bounds output
  entropy (SEL-DISC-1 P5, l. 53; §4, l. 79).
- [R, reviewed, not merged] A supplied bank meeting the precursor constraints needs 13/15/17 extra
  hidden coordinates for L = 9/10/≥11, and that is "not a universal physical cost or minimum"
  (NATIVE-PREP-SRC-1).
- [R, record on main] A seed bank is fresh only if "earlier dynamics and access have not used it or
  conditioned on it" (`REPORT.md`:57–69).
- [R, off-main record] Reuse of an unchanged carrier leaves the decoder cone (#912 `native-x-v2/`).
  A reset-reuse audit finds a public-record error (#911).

**What the plan would establish** [P], in unit U3, on paper:
- whether the criterion of §3 makes fresh-cell renewal *available* in any fixed model on record, or
  only *assumed*;
- what the X-PR mechanism needs, per use, in renewal and ready resources under that criterion;
- whether a native limit on renewal exists, or the question is unsourced.

U3 does not search for a renewal mechanism. That is #866 and #913 work, and it is not authorized
(O-REUSE: "not authorized"). U3 states its findings as definitions and requirements for RO-1 and
routes them to #913 (O-REUSE) and #914 (O-INS) without discharging those obligations (§2.3,
demarcation). It reads the Codex screen's item (iv), "resources for repeated runs", if that result
exists, and does not repeat it.

## 5. Closure of the executable set

[P] `Γ_exe(M)` is closed under sequence, adaptivity, parallel composition, reuse, renewal, classical
communication and later joint readout (RO1-SPEC-r3 §5, S-A1 to S-A7). This holds only where each
composite is itself executable under the criterion of §3. Access closure is required by the target:
"every physically performable experiment within C" (#1169 c.6876591512, answer 4).

**One interface** (RO1-DEPS-r4 §7.7):
- *X4.* An operation that supplies coverage enlarges `Γ_exe`, and with it the composites that
  soundness must control.
- *X5.* Track (b)'s remote-setting dependence is the PR mechanism.
- *Consequence.* [P] Every unit of this plan states its findings for coverage and for soundness *on
  the same `Γ_exe`*. A criterion assessed for one without the other is reported as incomplete.

## 6. Countercontrols

Each is fixed before U1 and applies to every unit.

| # | Countercontrol | What it guards against | Source |
|---|---|---|---|
| K-1 | **PR must not vanish by declaration.** The criterion may not exclude a program only by declaring it unavailable. If the PR program is excluded, U1 must name the native fact that excludes it, with its source | Defining the executable set narrowly to win soundness | RO1-SPEC-r3 §§6.1, 7.2; X-MENU (a passive selector cannot force a repertoire) |
| K-2 | **Not chosen for quantum outcomes.** The criterion *and the access declaration* must be stated and justified before any control is applied. A criterion or access whose only justification is that it yields quantum statistics is rejected | Fitting the criterion, or tuning it through the access, to the target | #1060 BELL-QSET rule; #914 c.6883249235 item 1; §A.29 |
| K-3 | **Coverage kept or reported.** The criterion must keep the coherent operations, incompatible measurements and Bell experiments the target needs, or state that it does not | Winning soundness by losing coverage, as global P-vii does (track (b)) | RO1-DEPS-r4 §§6, 7.3 |
| K-4 | **Representable is not available.** No program enters `Γ_exe` because a realization theorem represents it | D-real, D-glue (Main:582: "the same reversible machinery can realize non-quantum finite instrument families") | MR-1 §1 levels |
| K-5 | **No transfer without argument.** Finite-carrier results stay at their carriers | RO1-DEPS-r4 §7 rule 3 | — |
| K-6 | **Complete histories.** Full unnormalized branch masses, failures and residual state; no postselection | Hiding signalling or failure | #866 c.6548283392; SEL-DISC-1 §2 |

## 7. Existing evidence, labelled

| Evidence | Label | Bearing on S3 |
|---|---|---|
| Main:682: "coupling a which-path record is an intervention that changes it"; "a derivation of the two-slit interference pattern from the substratum dynamics is open" | [R, main] | §8 |
| Main:326–328: diagonal preservation; permutation-dilation channels "map computational-diagonal states to computational-diagonal states" | [R, main] | §8 |
| D-iv, D-nonneg (F₂); D-A8 (F); D-ceil (F, global P-vii) | [R, kernel] / [R, main] (RO1-DEPS-r4 §1.2) | §§3, 8 |
| MR-1 preregistration and stage-1 amendments | [R, record on main]; GAP provisional | §§2.1, 8 |
| CP-PREP-1, controller lead, O-OBSMU | [R, record on main] | §2.1 |
| Composition-access `REPORT.md` | [R, record on main] | §§2.2, 4 |
| NATIVE-INT-SRC-2 (#1223), NATIVE-PREP-SRC-1 (#1225), #1173 units | [R, reviewed, not merged] | §2.1 |
| SEL-ACCESS-1, SEL-EXCL-1, SEL-DISC-1 | [R, reviewed, not merged] | §§4, 6 |
| #912 packages, #911 audit | [R, off-main record] | §§2.2, 4 |
| RO1-SPEC-r3, RO1-DEPS-r4 (accepted, PR #1294) | [R, reviewed, not merged] | throughout |

## 8. Owner-suggested route M: measurement and which-path recording

**The owner's words:** "Perhaps the missing physical operation is somehow related to the act of
taking a measurement itself? For example when using a which-path detector in the double slit
experiment?" **Status: an owner-suggested hypothesis, not an adopted premise.** The owner's further
requirements for this route ("Confirmed, proceed as suggested", `amaybaum`, 2026-11-14) are built in
below: a four-way separation (§8.2), three explicit points (§8.3) and outcome tiers (§8.6).

### 8.1 What the corpus already says (§A.19 search)

Searched: `papers/` (Main, Substratum, GR, Structure, SM), `book/ch18-beyond.md`,
`book/ch19-open-problems.md` and `verification/programmes/oi-qm/reconstruction/`, for "which-path",
"which-way", "eraser", "double-slit" and "two-slit", and for measurement as record formation.

- [R, main] Main:682: in the double-slit experiment, "a which-path record coupled" is one of "a finite
  set of apparatus settings". "Coupling a which-path record is an intervention that changes" the
  setting-indexed visible law. "The detection statistics are an input of that construction, and a
  derivation of the two-slit interference pattern from the substratum dynamics is open."
- [R, main] `papers/Substratum.md`:463: "the measurement problem receives an observer-relative account
  at the fixed-basis level"; "In the double-slit experiment, the substratum occupies a single
  configuration at every step, and a derivation of the interference pattern from its dynamics is
  open."
- [R, main] `papers/GR.md`:350: "environmental decoherence, in which which-path records pass to
  unobserved degrees of freedom such as emitted radiation while the total evolution remains
  unitary".
- [R, main] Main:326–328: under a permutation unitary, the visible channels map diagonal states to
  diagonal states.
- [R, record on main] **MR-1 already studies this question**: "On one fixed interface generated by
  OI's native reversible dynamics, which microscopic interaction forms a record while preserving,
  modifying or eliminating the possibility of coherent recombination; and is any resource beyond the
  present OI premises necessary for it?" (`preregistration.md` §1). Its relevant content:
  - **Proposition A1:** records are functions of the complete state.
  - **Proposition A2:** a model with non-functional records "abandons at least one of" P-bij, P-obs,
    P-set.
  - **Proposition S:** "loss of interference is not evidence of record formation, a record is not
    evidence of irreversibility" (§3.5).
  - **The complementarity benchmark**, with visibility `V = |⟨d_L|d_R⟩|` (§3.5).
  - **T0:** "Coherence before marking (T0, an obligation)", and T4, "eraser" (§§5.4–5.5).
  - **AW-MR5:** the native step is symplectic, and Catani et al.'s classical toy theory "reproduces
    Mach–Zehnder, which-way, eraser, delayed-choice and bomb-tester phenomenology and is
    generalized-noncontextual" (§4.5).
  - **Countercontrol CC5:** "a classical eraser".
  - **Stage-1 GAP on K1:** "Superposition excludes setting-dependent transfer"; "Marking cannot
    destroy interference; only added independent noise can (S-L5)"; "The inverse is representable but
    not available (S-L3)"; the classical record route has G for the absence of a sourced ready region;
    the trace route is UNDECIDED (#1023 c.6555169983; `amendments/MR-star.md`:491–648).
  - **AW-MR8, as rescoped by MR★ C-6:** "The K1 step is additive and supplies no conditional dynamics
    (S-C1). MR-1's question (frozen §1) presupposes an interaction that the K1 step does not have.
    Operation-selecting settings, adaptive operations and subsystem undo therefore need a non-additive
    step, or structure beyond the K1 step. Whether the K1 step supplies records, through wakes, is
    undecided (C-4)" (`amendments/MR-star.md`:1401–1412). C-6 withdraws the substratum-level reading.
  - **The GAP's scope and caveats** are carried in §8.6: `K★ = {K1}` only; σ12, the non-additive
    rules, not screened. The GAP is provisional, and stage 2 is not authorized (README).

[A-inf] **Route M is, in substance, MR-1's question under O-REC (#866).** The plan must not duplicate
it. Route M adds the following: the question is posed under S3's criterion and RO-1's four tracks,
with the separation and tiers below.

### 8.2 Four-way separation

[P] Every statement unit U4 makes about route M carries exactly one class. A statement that would
need two is split.

| Class | Meaning | What may enter it | What may not |
|---|---|---|---|
| **(i) Native mechanism** | What the reversible dynamics and the observer's resources actually implement | The fixed `φ`, `μ`, `Obs`, `Res`; operations meeting the §3 criterion (*available*), with sources | Superposition, phases, a Born dictionary, quantum instruments, any supplied operation |
| **(ii) Conditional quantum interpretation** | What follows only after importing superposition, phases, a Born-rule dictionary or quantum instruments | The imported structure, named each time (P-super, P-phase, P-mix, P-CK, P-Born; RO1-DEPS-r4 §1.1) | Any claim that the import is native, or that a class-(ii) result is a class-(i) result |
| **(iii) Discriminating prediction** | An experimentally distinguishable restriction that follows without being chosen to match quantum results | A restriction derived from class-(i) facts, stated before comparison with QM, with its distinguishing experiment | A restriction justified by its agreement with QM (K-2); a single fringe (M-4) |
| **(iv) Negative control** | A fully specified model in which recording works but coherent quantum operations, or PR exclusion, fail | Complete models with full branch masses and residual state | Partial or schematic models; separately built countermodels combined |

Examples of how existing statements fall:
- *Class (i).* MR-1's S-L5 and S-L3 on K1; Main:328; the stage-1 G for the ready region.
- *Class (ii).* The complementarity benchmark `V = |⟨d_L|d_R⟩|` (MR-1 §3.5, which itself marks it as
  standard and imported); GR:350's account of environmental decoherence "while the total evolution
  remains unitary".
- *Class (iv), fully specified on record:* the PR model with complete records (M-7) and PC-1's
  screened rules (M-8).
- *Class (iv), once specified:* the Catani et al. classical model (M-1) and the classical eraser CC5
  (M-2). They are specified at class level in MR-1, and their full specification needs an MR-1 stage-2
  authorization (§8.5).

### 8.3 Three points the plan must address

**Point 1: a reversible copy alone is not quantum measurement.**
- [R, record on main] Classical reversible systems copy bits: MR-1 Proposition A1, and the
  tape-and-ledger realization that meets (C1)–(C3) (Main:78).
- [P] U4 keeps two questions apart.
  - **(a) Acquisition.** How does the observer *acquire* the coherent operations the target needs:
    completion condition (iv), the phases, and coherent preparation (RO1-DEPS-r4 track (a))?
  - **(b) Loss.** Given an *existing* superposition, how does visible interference drop once a record
    exists?

  (b) presupposes (a): MR-1's T0 makes coherence before marking an obligation. A class-(ii) account
  of (b) (decoherence by entanglement with a marker) answers nothing about (a).
- A native copy is a bijection of configurations: P-L3 is a premise (Main:54). Its conjugation is a
  permutation. [R, main] The diagonal-preservation lemma is a paper proof (Main:326–328). [A-inf]
  The conclusion is exact at configuration level: such a copy cannot contribute to (a) there. It holds
  by the definition of *available* together with P-L3, so it is not a finding. It does not reach the
  observer-level lift (§8.4, check 3) or the σ12 rules (§8.4, check 2).
- [R, record on main] On K1, interference of the additive field is native (S-L1). So (b) is not purely
  class (ii): its class-(i) form is D-1 (§8.4, check 1).

**Point 2: erasure must be physical uncomputation, not deletion by assumption.**
- [P] U4 tests, in class (i), whether the native dynamics can implement all four of:
  - **R** — recording;
  - **U** — reversible uncomputation of the record by an executable inverse;
  - **I** — the interference experiment, including the coherent preparation it needs;
  - **P** — that preparation itself.

  Deleting the record by declaration, or discarding it from the comparison, does not count.
- [P] Whether interference returns depends on three things, each stated explicitly: the joint state;
  how which-path information becomes inaccessible (uncomputation, transfer to unread degrees of
  freedom as in GR:350, or added noise as in S-L5); and which correlations are examined. Under K-6,
  full branch masses are compared.
- [R, record on main] On K1, the inverse is "representable but not available" (S-L3), and the record
  route has G at the ready region. [A-inf] So on the record, U and P are not shown available, and I
  waits on P (track (a), OB-a3).

**Point 3: records alone may allow fresh-cell PR.**
- [R, reviewed, not merged] A retained record of the first use exposes same-seed reuse (SEL-EXCL-1 §7).
  This is already the partial discriminator (RO1-DEPS-r4 §5.1). A fresh-cell supply defeats it, and
  the records it produces are complete and classical (SEL-EXCL-1 §3).
- [P] So recording, by itself, is not taken as a restriction. A genuine restriction must come from one
  of three places:
  - **physical renewal**: whether fresh cells or blank markers are executable, and at what cost (§4);
  - **accessibility across the wings**: which records each wing can read, under the declared access
    and the Q1 working definition;
  - **the allowed interventions**: the §3 criterion for setting writes and interventions.
- [P] Each candidate restriction is checked against K-3: it must not also exclude quantum Bell
  behaviour, as D-ceil under global P-vii does (RO1-DEPS-r4 track (b)).

### 8.4 What U4 checks, on paper and from the corpus only

Each check is tagged with the classes its statements may take. **Configuration-level copy** and the
**full measurement process** are kept apart throughout. The full process comprises preparation, an
accessible outcome, a retained record, and possibly uncomputation.

1. **D-1, the decisive test: S-L5 against observed which-path complementarity.**
   - [R, record on main] S-L5 is a class-(i) result, derived without reference to QM. On K1, "A
     record (R1) never causes (ii): marking is non-invasive" (`amendments/MR-star.md`:584–594). In
     #1023 c.6555169983's words, "Marking cannot destroy interference".
   - Observed which-path complementarity is a raw-direct observable (§A.24): with a which-path marker
     coupled, fringe visibility drops.
   - The two conflict on their face. [P] U4 treats this as a candidate class-(iii) confrontation,
     conditional on three identifications, each stated and decided from the sources:
     - (α) the K1 reading of the step, which is P-vii read globally, so it depends on C-1 (#1234);
     - (β) MR-1's marker region, `Φ_{AΣ} s_Σ ≠ 0`, is a which-path detector;
     - (γ) the additive-field interference of S-L1 corresponds to the observed detection statistics.
   - *Either outcome is decisive at its scope.*
     - If (α)–(γ) hold, native K1 recording misses observed complementarity. That is a raw-direct miss
       for the K1 reading, and it bears on P-vii and C-1 (RO1-DEPS-r4 track (b)).
     - If (β) or (γ) fails, the K1 marker is not a which-path detector, and route M is empty on K1. It
       then lies only on the rules MR-1 did not screen (check 2) or on the observer-level lift
       (check 3).
   - U4 decides the identifications on paper. It does not run any experiment or computation.
2. **The rules MR-1 did not screen.** Class (i).
   - [R, record on main] σ12, "Non-additive native-type rules", covers native-Y's rule, SM:104–106's
     state-varying coupling graph and SM §6.5's dynamical links: "outside `K★ = {K1}` … not screened
     for R or Q here". "These are the rules on which conditional dynamics, and so pointers and
     settings, are not excluded" (`amendments/MR-star.md`:667, :680).
   - The state-varying coupling graph is track (b)'s Bell route, so this check is indexed by the
     reading of P-vii (C-1, #1234; X2).
   - U4 records which of these rules any record on file has screened for recording. It does not screen
     them: that is #866 work (O-REC).
3. **The observer-level lift.** Class (i), with its route recorded as open.
   - [R, main] Main:588: "the observer-level lift, in every formulation stated that lands in the
     operational interface, derives neither a non-monomial admissible operator nor the layer flow, the
     site-space wave-operator formulation being unresolved rather than excluded" (kernel
     `obs_not_layerFlowExecutable`, `OIBridge/ExecSource.lean`).
   - [R, main] SM:224 states the rule "at either the substratum-symbolic level or an observer-level
     linear lift".
   - [A-inf] On that lift, the native linear step acts on field amplitudes by a non-monomial matrix.
     So the configuration-level argument of Point 1 does not reach it.
   - U4 records whether route M depends on this lift. It does not investigate the lift: that is track
     (a)'s OB-a1 (#866; #1169).
4. **Is writing a which-path record natively executable?** Class (i). Use the §3 criterion with MR-1's
   RFI definition and stage-1 results.
   - MR-1's GAP names the first missing ingredient: a sourced ready region (a blank marker).
   - At configuration level, an available recording operation is a composition of native bijections by
     definition (§1, *available*; P-L3), so its conjugation is a permutation. That is a property of the
     definition, not a finding (Point 1).
5. **R, U, I, P together** (Point 2). Class (i) for availability; class (ii) for any interpretation of
   a returned fringe beyond what M-1 and M-2 reproduce.
6. **Renewal, accessibility and interventions as restrictions** (Point 3).
   - Class (i) for what is executable.
   - Class (iii) only if a restriction follows from class-(i) facts without reference to QM, and comes
     with its distinguishing experiment.
7. **Negative controls.** U4 uses the class-(iv) controls already fully specified on record (§8.5).
   It specifies the others at class level, as MR-1 does, and does not construct them (F2; §8.5).

### 8.5 Route M's negative controls and countercontrols

**Fully specified on record, usable without construction:**

| # | Control | Class | Source |
|---|---|---|---|
| M-7 | The reversible PR model with complete local records. Recording works; PR exclusion fails. Coherent operations fail too, since `T` is a permutation | (iv) | SEL-EXCL-1 §§2–3 at `0ecfddeb` (reviewed, not merged) |
| M-8 | PC-1's screened rules: "classical measurable bijections with function-valued records". None of the 25 qualifies, and the obstruction is G★ item 3 | (iv) | `physical-coupling-pc1/` on `main` (#866 c.6627392555) |

**Specified at class level in MR-1; executing them needs an MR-1 stage-2 authorization** (README: "a
controls-only stage 2 … returns every reference result"). They are not U4 deliverables.

| # | Control | Class | Source |
|---|---|---|---|
| M-1 | Classical which-way and eraser phenomenology: the Catani et al. epistemically restricted model reproduces them | (iv) once specified | MR-1 AW-MR5; CC4 |
| M-2 | A classical eraser with full branch masses | (iv) once specified | MR-1 CC5 |
| M-3 | Loss of interference without any record (classical random dephasing) | (iv) once specified; shows that loss is not evidence of a record | MR-1 §3.5, Proposition S |

**Countercontrols:**

| # | Countercontrol | Source |
|---|---|---|
| M-4 | "A single quantum-eraser fringe alone is not a success criterion"; compare whole joint laws, outgoing carrier included | #866 c.6548283392 |
| M-5 | Coherence before marking (T0) must be shown first | MR-1 §5.4 |
| M-6 | The criterion, and the access declaration, are not chosen because recording yields quantum statistics (K-2) | §6 |

### 8.6 Outcome tiers, and what would close route M

**Route M stays open, conditional and unclosed until a decisive test runs.** Its tiers:
- **Strongest tier.** One native observer–record mechanism, in class (i), that both:
  - supplies coherent measurement operations (track (a): (iv), the phases, coherent preparation);
  - restricts executable non-quantum correlations (track (c)) without excluding quantum Bell
    behaviour.

  This needs a class-(i) result on Point 1(a), which the configuration level cannot give (check 4).
  So it would have to come from the observer-level lift (check 3) or from a σ12 rule (check 2), with a
  class-(iii) restriction on Point 3.
- **Weaker tier, still useful.** Recording explains memory and some measurement behaviour, in class
  (i): record formation, retention, the role of the retained record in exposing same-seed reuse, and
  which accounts of interference loss stay conditional. Quantum coherence (track (a)) and Bell
  soundness (track (c)) stay open separately.

**What would close route M negatively, at its scope.** All of the following:
- (a′) **D-1 is decided.** If (α)–(γ) hold, route M on K1 ends in a raw-direct miss for the K1
  reading. If they do not, route M is empty on K1.
- (b′) **The observer-level lift (check 3)** is shown to give no non-monomial admissible operator
  executable through `Obs`. Main:588 records this as "unresolved rather than excluded". It is
  track (a)'s question (OB-a1), not U4's.
- (c′) **The σ12 rules (check 2)** are screened for recording. MR-1 did not screen them. This is #866
  work.
- (d′) **Bearing on soundness** reduces wholly to renewal, accessibility and the allowed interventions,
  which are §§3–4's questions (Point 3).
- (e′) **Returned interference.** Class-(i) interference that a generalized-noncontextual model (M-1,
  M-2) reproduces supplies no quantum coherent operation.
  - [R, record on main] On K1, interference of the additive field is native (S-L1).
  - [R, record on main] Classical erasers reproduce returned interference without any class-(ii)
    import (CC5; AW-MR5).
  - Only interference beyond such models (MR-1's W1 witness, §5.7) needs class (ii), or a U or P that
    is not available.

U4 can settle (a′), and record (d′) and (e′). Settling (b′) and (c′) lies outside U4. So **U4 alone
cannot close route M negatively**. It can reach the weaker tier, decide D-1, and state exactly what
closure still needs.

**Scope of the MR-1 GAP, carried.**
- [R, record on main] The GAP is for `K★ = {K1}`, sources σ1–σ13, and a budget below recurrence
  (#1023 c.6555169983).
- σ12 is not screened.
- Its caveats, quoted: "This is not a no-go, and it makes no claim against classical explanations";
  "the absence of a proved ready supply is an open sourcing problem, not a proof that no ready supply
  can exist".
- The token is provisional pending a controls-only stage 2 (README).

**Stop.** If route M can proceed only through a non-functional record relation, it changes P-bij,
P-obs or P-set (MR-1 Proposition A2). That is a new premise, and it stops for owner decision under
§A.29.

## 9. Units, in order

The units are proposed; each needs its own owner authorization. All are paper-only.

The outcome tiers of §8.6 are defined for route M only. U1–U3 produce definitions and ledgers, and
their output type is given in place of a tier (F7).

| Unit | Content | Home | Output type / tier | Depends on | Stops when |
|---|---|---|---|---|---|
| **U0** | This plan | #1169 (RO-1) | Plan | — | — |
| **U1** | Specify the per-action criterion (§3), the frozen access declaration and the countercontrols (§6), preregistered. Reuse MR-1's levels, #866's source-matrix vocabulary and the Q1 working definition. No candidate is evaluated. Used by RO-1 as a definition only | #1169 (RO-1, S3 as an RO-1 stop) | Definition (`S3-CRIT`); tiers not applicable | Owner answers on S7 (question 3) | The criterion needs S7 or O11; or it cannot be stated without reference to quantum outcomes (K-2) |
| **U2** | Classify, against the U1 criterion, **only RO-1's own control programs**: the PR single-use test, fresh-cell use, same-seed reuse, the one-bit message, the further #1143 continuations (RO1-SPEC-r3 §5.1), and the closure rules S-A1 to S-A7. Native candidates are not classified anew; for them U2 reads the Codex screen's result (#866 c.6863601327) and the existing #866 stops | #1169 | Ledger; tiers not applicable | U1. Owner answer on the Codex screen (question 4); if the screen is running, U2 waits for its result | A verdict would need a new derivation or candidate: route it to #866 and stop that row |
| **U3** | Closure and renewal (§§4–5) as **definitions and requirements for RO-1**: what `Γ_exe` must contain under the criterion; the renewal requirements of the X-PR mechanism; coverage and soundness on the same `Γ_exe`. Findings routed to #913 (O-REUSE) and #914 (O-INS) without discharging them | #1169 | Requirements note; tiers not applicable | U1, U2; the Codex screen's item (iv), if available | A renewal mechanism or access-closure result would have to be proposed: that is #866, #913 or #914 work, not authorized |
| **U4** | Route M (§8) from the corpus only: decide D-1's identifications; record the σ12 and observer-level-lift dependencies; R, U, I, P from the records; restrictions under Point 3; use the on-record controls M-7 and M-8 | #1169, with findings routed to #866 (O-REC, MR-1) | Route-M note. Tier: the weaker tier at most, plus D-1 decided. It cannot close route M negatively alone (§8.6) | U1 | MR-1 stage 2, a σ12 screen, an observer-level-lift derivation, a construction, or a premise change would be needed |
| — | Report to the owner: the effect on RO1-DEPS-r4's track (c) and (d) first steps, and D-1's bearing on track (b) | #1169 | Summary | U1–U4 | — |

**Order.** U1 first. U2 after U1 and after the owner's answer on the Codex screen. U3 after U2. U4 after
U1, in parallel with U2 and U3. One writer per unit. No unit edits #866, #913, #914 or #1143 records or
branches.

**Stopping conditions, general.** Stop at any of the following:
- a new premise (§A.29);
- choosing Q7 (#1060), resolving O11 or S7, or changing the target;
- a computation or a construction, including the full specification of M-1 to M-3;
- any step that would duplicate an #866, #913 or #914 obligation, or alter its authorization.

C-1 stays under #1234, and X1–X5 stay open.

## 10. Owner questions

1. **Authorization.** Authorize U1, U2, U3 and U4 as paper-only units under #1169, with which writer
   and reviewer?
2. **Home of U4.** Should route M run as an RO-1 unit (U4) reading MR-1, or as an #866 O-REC unit?
   MR-1 stage 2 stays unauthorized either way unless the owner decides otherwise. Executing M-1 to M-3
   needs that stage-2 authorization.
3. **S7 first?** U1 may need the typing choice S7. Decide it before U1, or let U1 stop at it?
4. **Codex's apparatus screen.** Is the 2026-11-13 handoff (#866 c.6863601327) running? U2 depends on
   the answer. If the screen is running, U2 waits for its result and classifies only RO-1's control
   programs.
5. **O-REUSE and O-INS.** U3's findings would be routed to #913 (O-REUSE, blocked on O-INS, "not
   authorized") and #914 (O-INS) without discharging them. Is that routing acceptable without
   changing their status?
6. **D-1's consequence.** If D-1's identifications hold, the K1 reading misses observed which-path
   complementarity. That bears on P-vii and C-1, which stays under #1234. Should U4 report that
   consequence to #1234, or only to RO-1?
7. **#913 maintenance.** O-REUSE's status-source cell reads "branch only", while the composition-access
   REPORT is now on `main` (`86cd47e5`). Correcting it is #913 maintenance, outside this plan.
