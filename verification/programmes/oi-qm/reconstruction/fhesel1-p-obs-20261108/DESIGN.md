# FHE-SEL-1 P-OBS: preregistration (Stage 1A)

**Standing.** WIP / UNVERIFIED. Stage 1A preregistration of the P-OBS construction under #1169.
Writer: Claude Code session (P-OBS writer), 2026-11-08. Independent review pending; no reviewer of
this file reviews another construction of the portfolio. Paper only: no result is derived, nothing
is computed, simulated, built in Lean or run under V3, nothing is adopted, and no manuscript is
edited. Stage 1B is not authorized. Every verdict this file provides for is generated in Stage 1B,
if authorized, from the rule fixed here.

**Base and pins.** Branch `research/fhesel1-p-obs-20261108` from main
`9c201475ba6fd8f341591d14dd8e88db2e2aaa90`. `File:N` means line `N` of that file at this commit.
Abbreviations, all under `verification/programmes/oi-qm/reconstruction/` unless stated:

- `Main`, `Sub` = `papers/Main.md`, `papers/Substratum.md`;
- `AP1` = `apparatus-1-20261107/DESIGN.md`; `QA` = `quarter-phase-native-20261107/DESIGN.md`;
- `M2D` = `mechanism-2-20261108/DESIGN.md`; `GA` = `oi-qm-ext-1/endpoints.md`;
- `MR★` = `measurement-record-formation/amendments/MR-star.md`;
- `LEAD` = `o-ret-routes-20261103/classical-retention-20261107/LEAD.md` (#1186, on main);
- `TN` = `o-ret-routes-20261103/phaseB-negative/THEOREM-N.md` (on main).

Off main and provisional:

- `MI` = `minacc-1-20261108/RESULT.md`, `MI-D` = its `DESIGN.md`, `MI-A3` =
  `amendments/A3-post-result-prot-r.md`, all at #1198 head
  `f649b3475c9d69f98cf9a6ecab9c1dd076096834` on `research/oi-qm-minacc-20261108`. Read with
  `git show`, not modified.
- `Q3-A1` = `verification/programmes/substratum/a5-linear-affine-20261104/q3-a6-offsets-20261108/amendments/A1-prereg-review.md`
  at #1202 head `25384b13526dfa23909bbd63a119508091f467c7`. Used only for its classification
  standard (§7), which is restated here in full.
- `S0` = the Stage 0 map, #1169 c.6719708521, with its review c.6719720616 and confirmation
  (ACCEPT; c.6719723538). Its standing line reading "pending" is stale. Its file:line citations are
  to main `f88c1842`; between `f88c1842` and `9c201475` main adds only
  `controller-preparation-1-20261108/SELECTION.md`, so every cited line is unchanged at the pin.

***

## 0. What this file fixes

1. **Question** (§1). What physical mechanism permits registration, retention and reuse of records
   without unintended leakage of information?
2. **Candidates** (§3). Fourteen candidates are recorded with the reason each is selected or
   rejected. One construction is selected, P-OBS-LB (a Landauer–Bennett record cycle). A null
   outcome (no candidate) is preregistered as admissible.
3. **Construction** (§4). P-OBS-LB on a finite ring at `q = 2`. Registration only by copy onto a
   standard blank. Reset and reuse only by export of the spent register into an interacting hidden
   sink. Blanks come from a reservoir whose law is fixed in advance. Rule `N_1` is primary; `N_0`
   and `G_σ` are preserved-result controls.
4. **Source ledger** (§5). Each resource is classed native / supplied / representation / imported.
   Named open inputs: BLANK-SRC, SWAP-EXEC, RECORD-STORE, EXHAUST, TIMING.
5. **Motivation and classification** (§6). The overall motivation is classed **mixed**.
6. **Properties and decision rule** (§8–§9). These cover non-vacuity, the leakage increment
   `LK-R`, `PROT-D/B/R′` on the never-exported domain, and sink use `USE-S`. They also fix the
   outcomes and their mapping to the owner's (a)/(b)/(c), the ladder L0–L3 and the three statuses.
7. **Controls** (§10). Mechanism-off, classical imitation, target import, a target-tuned
   countercontrol and robustness/replication.
8. **Explanatory quality, §A.29** (§11). Preserved results, the variation analysis and its decision
   rule, reach, the assessment ladder and the disclosure of origin.
9. **Report commitment** (§12), the invariant → checkpoint table (§13), the §A.42 item 8 trace
   (§14), concerns (§15) and what is not claimed (§16).

***

## 1. Authority, question and Stage 0 rows

### 1.1 Authority (quoted)

- **#1169 c.6720450946** (amaybaum, 2026-11-08T10:38:44Z), Stage 1A approved, 1B gated. The
  owner's words, as recorded:
  > P-OBS | Can native observation preserve and reuse records without leaking protected
  > information? | #1169, with sourcing under #1032
  >
  > These are research labels, not adopted OI axioms.
  >
  > **Research boundaries.** M-INACC's findings remain applicable. … P-OBS cannot count supplied
  > record access as physically generated access. No computation, V3 execution, new physical
  > axiom, manuscript change or Q-B activation is authorized.

  The same record requires the report to distinguish "An independently predicted positive result.
  A positive result obtained only after selecting among multiple candidates. A result that
  reproduces quantum statistics but admits an equivalent classical imitation", and requires "a
  separate robustness or replication check" before any positive is promoted.
- **#1169 c.6720342295** (amaybaum, 2026-11-08T10:26:34Z), planning clarification. P-OBS scope:
  "What physical mechanism permits registration, retention and reuse without unintended leakage of
  information?" Safeguard: "Must keep M-INACC's leakage findings: registration and refill can expose
  hidden information (#1198). Physical mechanisms are sourced under #1032 (Codex)." Anchors:
  "Apparatus-1 P1/P2; M-INACC; in Stage 0, the measurement-interface rows." Three statuses:
  proposed / mathematically sufficient / derived from native OI. Order: "First, independent
  physical motivation. Second, evaluation of consequences. Third, comparison with the quantum
  completion conditions. The order is never reversed."
- **#1169 c.6719386464** (amaybaum, 2026-11-08T08:41:15Z). The owner's words: "Every candidate
  physical restriction must have an independent physical motivation established before evaluating
  whether it selects quantum behaviour. A restriction that eliminates an unwanted classical model is
  not automatically evidence that nature obeys that restriction." Refinement 1, approved by the
  owner: "A restriction designed to exclude a particular construction is treated as tuned to the
  target."
- **#1169 c.6719192859** (owner guidance on M-INACC tiers). The owner's words: the most important
  part is "the classical-imitation control".

### 1.2 Stage 0 rows targeted

- **Row 9, measurement interface (primary).** Tag R. "P1 and P2 are supplied (AP1:419–420)."
  Column (d): "Native reciprocal backaction, in part (AP1:311–330) … P1 and P2 lack independent
  motivation (AP1:349, 357–363)." Residual freedom: "Which instruments, and which access or
  intervention model." P-OBS-LB proposes a physically motivated access model for the registration,
  reset and supply that P1 and P2 currently supply.
- **Row 16, inaccessible but dynamically used memory (evaluation).** Tag R. "Lemma Q in class N,
  given P1 and P2 (QA:458–479) … Fails for `G_σ` (MI; provisional; §4)." P-OBS-LB is evaluated on
  whether its cycle keeps what row 16 records for class N once P1's decoupled archive is replaced by
  export into an interacting sink.
- **Reach rows** (§11.3). Row 2 (preloaded content and its storage form) and row 15 (hidden dynamics
  between couplings), through the sink-use test `USE-S`. Row 4 (reversibility) is used and not
  targeted.

***

## 2. Constraints carried from the record

| ID | Constraint | Source | How P-OBS-LB meets it |
| --- | --- | --- | --- |
| K-NC | MECH-2 Theorem NC: under an injective identification with H-LIFT and spanning-read certification, the configuration model is noncontextual for any dynamics. A construction must change the identification or the access, not only the dynamics | M2D:65–71, M2D:483–498 | P-OBS-LB changes the access: the registration, reset and supply model. It leaves the rule and the identification unchanged. It claims no nonclassicality. At `q = 2` over native `Z`/`X` reads alone NC does not apply; the configuration model remains a classical imitation in every case (C-NC, §10) |
| K-MI | M-INACC: under `G_σ`, registration and refill expose the `Q* = 1` functional in `Π_A` and `Π_B` (E_A, E_A′, E_B; outcome (B, B), tiers Negative). P-GK is degenerate. PROT-R fails even in the linear limits; PROT-R′ holds in them | MI §0, §3, §4, §6.3; MI-A3 §1, §4 (provisional, off main) | Preserved as control PR-3. No P-OBS-LB clause is chosen to block E_A, E_A′ or E_B; the target-tuned countercontrol TT (§10) checks this |
| K-FIN | Finite carriers: the encoded unitaries of a fixed bijection form a finite group (Theorem U2); AP1 excludes `rot` | M2D:55–64, M2D:404; AP1 §5.3 | P-OBS-LB is finite and claims no encoded operation. Any encoded operation outside `A_4 ≀ S_n` under R1 attributed to it voids the record (PR-1) |
| K-SUP | Supplied access, records, preparation or control does not count as physically generated | c.6720450946 | Every resource is in the §5 ledger. "Derived from native OI" requires every load-bearing entry to be native (§9.4) |
| K-IV | Condition (iv) fails natively (`permTheory_not_control`, `substratumGen_not_control`); the residual is in the access/intervention model | S0 row 9 | P-OBS-LB makes no claim about (iv). The comparison stage only records whether its access model bears on (iv) (§9.5) |
| K-LEAN | No `readWriteSourced_*` citation (#1188) | brief | None cited |
| K-Q | `q = 2`; odd `q` conditional on #1193 | brief | `q = 2` only. No odd-`q` statement |
| K-1032 | Physical mechanisms are sourced under #1032 (Codex) | c.6720342295 | Not duplicated. Needed mechanisms not sourced there are named open inputs (§5.2) |

***

## 3. Candidate record (owner distinction (b))

Each candidate was considered before any consequence was evaluated. "Scope" asks whether it
addresses all three stages (registration, retention, reuse) at the level of access, as K-NC
requires. "Class" is the motivation class of §6.2.

| # | Candidate | Source | Class | Decision and reason |
| --- | --- | --- | --- | --- |
| C-1 | Landauer–Bennett record cycle: registration by reversible copy onto a blank; reset only by exporting the register's content into non-information-bearing degrees of freedom of an environment; blank supply as a consumed resource | Landauer 1961; Bennett 1973, 1982, 2003 (§6.3) | Mixed (§6.2) | **Selected** as P-OBS-LB. It is the only candidate whose motivation is stated without the target and that fixes a form for all three stages, including reset, which is the step where M-INACC's exposure entered (MI §8, "archive-swap refills act as gate settings") |
| C-2 | Barrier-protected metastable memory (Kramers hopping; trapped bead with camera read) | LEAD §2; Bérut et al. 2012; Kramers 1940 | Independent, external | **Rejected as P-OBS's mechanism; carried as a dependency.** It is a retention mechanism and is silent on leakage. Its native sourcing is #1032's open item (LEAD §4: "first missing ingredient … source-level realization of the controlled bead register"). Duplicating it is outside this unit (K-1032) |
| C-3 | Redundant environmental records (quantum Darwinism, objectivity, spectrum broadcast structures) | Zurek 2009; Ollivier, Poulin, Zurek 2004; Horodecki, Korbicz, Horodecki 2015 | Target-defined | **Rejected.** Stated for quantum systems (pointer states, decoherence). Its classical residue, many copies of one record, multiplies access paths and does not address leakage |
| C-4 | Classical repetition / majority redundancy for retention | Standard coding | Independent | **Rejected.** Retention against noise only. Added copies are added read paths; there is no leakage content |
| C-5 | Self-correcting local memory (Toom's rule; reliable cellular automata) | Toom 1980; Gács 2001 | Independent | **Rejected.** Noise-robust retention with dissipative local rules. In a bijective substratum it needs a supplied cold sink, which is the same unsourced resource as C-1's blanks, and it does not address leakage. Recorded for #1032 |
| C-6 | Symplectic reciprocity extended to every coupling, gates included ("full-map reciprocity") | Hamiltonian action–reaction; AP1:313–327 | Independent in motivation, but no definition for nonlinear maps over `F_2` | **Rejected.** Over `F_2` it has no stated meaning for non-affine rules. Adopting it now would act chiefly to exclude `G_σ`, i.e. a particular construction: tuned under refinement 1. Its class-N content is already QA's Lemma Q |
| C-7 | Epistemic restriction (knowledge balance; classical complementarity) | Spekkens 2007, 2014; Bartlett, Rudolph, Spekkens 2012 | Target-adjacent | **Rejected as motivation.** Introduced to reproduce quantum phenomena (Spekkens 2007 abstract). Used only as a comparator (§10, C-NC) |
| C-8 | Conservation-limited measurement (Wigner–Araki–Yanase) | Wigner 1952; Araki, Yanase 1960 | Target-defined | **Rejected.** Stated for quantum observables. Its classical analogue, conservation of `Q`, is tested in MI and does not protect under `G_σ` (MI §6.2) |
| C-9 | Causal-cone locality of records | Main:364 | Independent | **Rejected as mechanism.** Non-discriminating: `G_σ` satisfies it (MI §6.1, C-NS green) |
| C-10 | Information acquisition bounded by negentropy consumed (Szilard–Brillouin–Sagawa–Ueda accounting) | Szilard 1929; Brillouin 1951; Sagawa, Ueda 2009 | Independent | **Not a separate candidate.** A global budget, not a mechanism. Kept inside C-1 as the resource ledger. Whether it constrains per-cell determination is a Stage 1B question; it is not assumed to |
| C-11 | Wake / passing-field reads | MR★ C-2, C-4 | — | **Rejected as out of scope.** It is #1032's route I, recorded `UNDECIDED` in MR★ C-4. Not duplicated |
| C-12 | Non-equilibrium environment as blank supply (observers in a non-equilibrium phase) | Main §4.6 (conditional on EM); MR★ C-3 | Mixed | **Not selected; recorded as candidate source for BLANK-SRC.** MR★ C-3: "No principle in the corpus supplies [a quiet region]". Sourcing is #1032/#1147 territory |
| C-13 | State-dependent geometry as protector | SM:104; M2D §0 item 1 | Independent proposal | **Rejected as P-OBS's mechanism.** Tested within scope by MI and fails there (provisional). Kept as a control rule (`G_σ`) |
| C-0 | Null: no candidate | — | — | **Admissible outcome.** If the §6 entry review reclassifies C-1 as target-defined, P-OBS records a null and stops (§9.1, step E0) |

**Selection is by motivation and scope, not by outcome.** No consequence of any candidate has been
evaluated. The disclosure of origin (§11.5) records how C-1 came to be considered and the
independence risk that follows from it.

***

## 4. The construction P-OBS-LB

### 4.1 Carrier and rule

- **Carrier.** A finite ring `Z_L` at `q = 2`. Each site holds one cell `(u_i, v_i) ∈ F_2²`, with
  `u_i = x_i(t)` and `v_i = x_i(t − 1)` (MI-D §1.2). This is a finite carrier. `L` and the horizon
  `T` satisfy H-NW (no dependency cone winds within `T`). `T` is below the recurrence period of the
  orbits in the support of the initial law (MR★ S-L6, MR★:595).
- **Rules, each evaluated separately; none is selected by outcome.**
  - **`N_1` (primary).** The fixed, always-on, translation-invariant, symmetric, center-free linear
    nearest-neighbour second-order step `u′_i = u_{i−1} + u_{i+1} + v_i`, `v′_i = u_i` (QA's class
    N on the ring; MI's `N_1`). Native under A4/A5 (Sub:98–100), whose posit status is unchanged.
  - **`N_0` (linear control).** MI's other linear limit, with the gated edges always present.
  - **`G_σ` (preserved-result control).** `f_i = OR(u_{i−1}, u_{i−2}) ⊕ OR(u_{i+1}, u_{i+2})`
    (MI §0 item 1). Used to check K-MI, not as a candidate rule.
- **Always on.** No P3 multipliers, no E-iso, no vacancies, no translations. Every cell on the ring
  is updated by the rule at every tick (as in MI's `Π_A`).

### 4.2 Regions and the initial law

- **Carrier region `C`.** Source cells, both slots unknown, uniform and independent (N2 through
  H-PREP; product sources H-PS). These are the cells about which information is registered.
- **Register sites `Rg`.** Fixed by the protocol at `t = 0`, outside `C`. Each holds a standard
  blank (§4.3, LB-B) at `t = 0`.
- **Sink entry sites `Snk`.** For each register site `r`, one fixed hidden site `s(r)` outside `C`
  and `Rg` at ring distance `d_S = 3` from `r`, on the side away from `C` (parameter; §11.2,
  A-dist).
- **Background.** Every other ring site holds a source cell (the hidden sector).
- **Reservoir `Res`.** Decoupled cells outside the ring, each a standard blank, injected only by
  LB-Z. This is MI §6.3's reserve-cell representation, now holding blanks only.
- **Exhaust `Ex`.** Decoupled cells outside the ring, never injected and never read (§4.3, LB-Z).

### 4.3 The access mechanism (the construction proper)

- **LB-W, registration by copy onto a blank.** The observer acquires a record value only by
  registering the `u` slot of a cell at a register site. Carrier cells and background cells are
  never registered directly. Information reaches a register only through the fixed rule's coupling.
- **LB-B, standard blank.** At its injection tick a blank has `u = 0` known and `v` unknown,
  uniform and independent of everything else. No other supplied cell exists: no value 1, no `v`-known
  or `(u + v)`-known supply, and no fully known cell.
- **LB-F, reservoir fixity.** The blank law of LB-B is fixed before any protocol and does not depend
  on the protocol, the records or the carrier. The protocol chooses only when a reset occurs; it
  never chooses blank values.
- **LB-Z, reset by export (atomic with registration).** Immediately after a register site's `u` slot
  is registered, between the same two ticks, the cycle `(Res blank → r; spent register → s(r);
  former occupant of s(r) → Ex)` is executed. The spent register then evolves on the ring at
  `s(r)` under the fixed rule, coupled to its neighbours. Nothing is erased: the cycle is a
  permutation of cells.
- **LB-S, sink inaccessibility.** No register-site rule lets the observer register a cell at a sink
  site or in `Ex`. The sink's content can reach a register only through the fixed rule's dynamics.
- **Adaptivity.** The choice of which register to register, and when, may depend on earlier records.
  Register sites, sink sites, `d_S` and the blank law are fixed per protocol before `t = 0`.
- **Protocol class `Π_LB`.** All finite protocols built from the above on a given rule. Sequential
  composition: the outgoing ring configuration, `Res`, `Ex` and the records are the input of the
  next protocol.

### 4.4 Records, retention and reuse

- **Records.** The joint record is the list of registered values with their sites and ticks.
  Knowledge `K_t` comprises the record, the protocol (sites, schedule, `d_S`) and the blank law
  (MI-D §1.2's definition, adapted).
- **Retention.** A registered value is held in the observer's record store. Its physical retention
  is RECORD-STORE (§5.2), supplied here. The physical register is exported by LB-Z; P-OBS-LB
  provides no persistence mechanism for it. Persistence is #1032's (C-2).
- **Reuse.**
  - *Register sites* are reused after each LB-Z reset.
  - *Carrier continuation:* the carrier keeps evolving and can be registered again through
    registers.
  - *Recombination:* an unregistered register keeps interacting under the rule, so any
    un-copying (AP1 §4.5) happens only by the dynamics.
  - *Record-conditioned preparation* is excluded by LB-F.

### 4.5 What differs from AP1 and MI

| Element | AP1 / MI | P-OBS-LB |
| --- | --- | --- |
| Registered cell after registration | Archived: leaves the ring, couples to nothing (P1; MI-D §3.3) | Exported into the ring at `s(r)`, where it keeps coupling (LB-Z) |
| Supplied cells | Either slot known, value 0 or 1 (H-PREP), chosen by feedback (MI-D §3.1, §3.2) | `u = 0` known at injection only; fixed law (LB-B, LB-F) |
| What may be registered | Any active cell (MI-D §3.3) | Register sites only (LB-W) |
| Isolation, multipliers | `Π_B`: P3, E-iso | None |

Whether MI's protocols E_A, E_A′ and E_B lie in `Π_LB` is a Stage 1B check (§10, PR-3). It is not
assumed in either direction.

***

## 5. Source ledger

### 5.1 Entries

| Resource | Class | Note |
| --- | --- | --- |
| Finite ring, cells in `F_2²` | Native | A1 posit (finiteness) unchanged |
| Rule `N_1` (and `N_0`) | Native | A4/A5 posits; A4's no-self-term clause has open warrant (S0 row 9, §3 A4) |
| Rule `G_σ` | Representation (corpus candidate) | Control only; from SM's state-dependent-geometry hypothesis via MI |
| Bijectivity of every step and of LB-Z's permutation | Native (A2) for the rule; LB-Z's execution is supplied (SWAP-EXEC) | A2's corpus motivation is mixed (S0 row 4); LB-Z uses only its information-conservation prong |
| Observer/hidden partition | Native as OI's definition (Main:44) | The placement of `C`, `Rg`, `Snk` is representation |
| Placement of `C`, `Rg`, `Snk`, `d_S` | Representation | Fixed per protocol before `t = 0` |
| Uniform unknown slots (sources, blanks' `v`) | Native measure through the open hypothesis H-PREP | AP1:416, 418 |
| Standard blanks and the reservoir | Supplied | Named open input BLANK-SRC |
| Execution of LB-Z | Supplied | Named open input SWAP-EXEC (a controller act; #866 territory) |
| Registration act and record store | Supplied | Named open input RECORD-STORE; the later-read bridge is LEAD §4's "separate missing bridge" |
| Exhaust `Ex` (decoupled, never read) | Supplied idealization | Named open input EXHAUST |
| Schedule and clock | Supplied | Named open input TIMING; S0 row 5: no clock source passes CTL's gate |
| R1 encoding | Representation (comparator only) | Used only in C-NC and PR-1 |
| Literature of §6.3 | Imported (motivation only) | Not a premise of any derivation |
| Qubit stabilizer theory, toy theory | Imported (comparator only) | C-NC |

### 5.2 Named open inputs

- **BLANK-SRC.** A physical source of standard blanks under one fixed law. MR★ C-3 records that no
  principle in the corpus supplies a quiet ready region. #1147 and #1032 hold the readiness and
  register obligations. Not sourced here.
- **SWAP-EXEC.** A physical process that executes LB-Z's permutation under the fixed rule. Not
  sourced. Controller sourcing is #866 (CP-PREP-1 at main `9c201475`, source gate not passed).
- **RECORD-STORE.** A physical retention of registered values and the read into a public record. It
  depends on #1032 (LEAD §4; TN §6.2: "not a universal no-go").
- **EXHAUST.** A decoupled, never-read store for displaced sink occupants. Supplied as in MI §6.3's
  reserve-cell representation.
- **TIMING.** A source of the schedule. Not sourced.

**Consequence fixed now.** Because BLANK-SRC, SWAP-EXEC, RECORD-STORE, EXHAUST and TIMING are
supplied, the status "derived from native OI" cannot be reached in Stage 1B unless a recorded
source for each lands first (§9.4). This is stated before any result.

***

## 6. Independent physical motivation

### 6.1 Motivation (stated without the target)

1. **Registration as copying onto a blank.** A logically reversible operation can be carried out by
   a physical mechanism without a necessary entropy cost (Bennett 1973; Bennett 2003, abstract). A
   measurement can be modelled as such an operation: the measured value is copied into a memory
   that starts in a known standard state (Bennett 1982). The memory, not the measured system, then
   holds the record. LB-W states this for the ring. Information about the carrier reaches the
   observer only through a cell that began in a known standard state and was coupled to the carrier
   by the same dynamics that moves everything else.
2. **Reset requires export.** "Any logically irreversible manipulation of information, such as the
   erasure of a bit … must be accompanied by a corresponding entropy increase in non-information
   bearing degrees of freedom of the information processing apparatus or its environment" (Bennett
   2003, abstract, stating Landauer 1961). In a dynamics that conserves information (A2; Liouville's
   theorem in the classical case), a memory cannot be returned to its standard state by destroying
   its content. The content must be moved into other degrees of freedom. LB-Z states this for the
   ring: reuse of a register site is a permutation that moves the spent register into the
   environment and brings in a fresh standard memory.
3. **The environment keeps evolving.** The degrees of freedom that receive exported content are
   part of the world and obey the same dynamics. Main's observer is a proper subsystem coupled to
   its complement through the same `φ` (Main:44). Visible and hidden lattice degrees of freedom obey
   the same local rule (Sub:48). LB-Z therefore places the exported register on the ring, where it
   keeps coupling, rather than in a store that couples to nothing.
4. **The standard state fixes the information-bearing value only.** Landauer's distinction separates
   information-bearing degrees of freedom, which a reset sets to a standard value, from the others,
   which stay thermal. In the second-order cell the present value `u` is the one the observer
   registers. LB-B sets `u` to the standard value 0 and leaves the previous-slice value `v` at the
   maximal-entropy law (Main:56, through H-PREP).
5. **A reservoir is fixed in advance.** A reservoir is a system whose state law is set before, and
   independently of, the process that draws on it. LB-F states this. It matches GA's admission
   contract, which excludes fitted seed laws and record-conditioned loading (GA:75–106).
6. **The environment is not read.** Exported content is outside the observer's registers (LB-S).
   This is the content of "environment" in item 2, and Main's partition of `S` into observer and
   complement (Main:44).

### 6.2 Classification (Q3-A1 §3 C2 standard, restated)

**The standard.** `T` here means quantum behaviour, the Born rule, complete positivity, unitaries,
the completion conditions, and the protection of the `Q* = 1` class (the protected class of QA and
MI, chosen there for the quantum target). Each assumption is judged on its own, without the rest of
the construction. What it yields together with the construction is a consequence (§8), never a
motivation.

- **Independent.** The stated motivation and its support do not presuppose `T` and are not designed
  to exclude a particular construction.
- **Target-adjacent.** Taken on its own, the assumption or its motivation presupposes `T`, is
  equivalent to part of `T` on the class at issue, or is supported only by a consequence of `T`.
- **Target-defined.** The stated reason is to obtain `T` or to exclude a particular construction;
  or, by the functional test, the assumption's statement is a restriction on the protected
  functional itself, with no stated effect outside it.
- **Mixed.** An independent component together with a target-adjacent one, each identified.
- **None found.** No motivation located after a recorded search.

| Clause | Class | Reason |
| --- | --- | --- |
| LB-W | Independent | Bennett's reversible measurement model; no reference to `T` |
| LB-Z | Independent | Landauer's principle with information conservation. A2's corpus motivation is mixed (Main:62, 66); LB-Z uses only the Liouville prong |
| LB-Z, interacting sink (item 3) | Independent | Main:44, Sub:48: one dynamics for observer and complement |
| LB-B | **Mixed** | Independent: Landauer's information-bearing / thermal split. Target-adjacent: the result, one known slot per supplied cell, coincides in form with AP1's P2, whose motivation is "closure plus the E-AR obstruction … a programme-internal reason" (AP1:347–349), and with the knowledge-balance principle (C-7). The choice of `u` as the information-bearing slot is a representation choice |
| LB-F | Independent | Reservoir definition; GA:75–106 |
| LB-S | Independent | Main:44 partition. It is a lack of access, not a supplied access |
| Leakage criterion `LK-R` (§8) | Independent | Defined relative to the single-use reference, without `T` |
| `PROT-D/B/R′_LB` (§8) | Target-adjacent | Inherited from MI to preserve K-MI; used only to record outcomes |

**Overall: mixed.** The target-adjacent component is LB-B's form. Whether that component is
load-bearing is decided by the variation analysis (§11.2, A-B and A-Bslot). If it is load-bearing
and its destroying variants are equally supported by item 4, the positive is recorded as (b)
(§9.3).

### 6.3 Literature

Each item below was checked in this unit, or is marked as not checked. The entry review (E0, §9.1)
must verify the textual support of every item marked "not read here" before that item counts as
motivation. #1186 records that earlier Landauer/Bennett attributions in the corpus "were not
textual literature reads … they do not source this lead" (LEAD:29); the same standard applies here.

| Reference | Checked here | Used for |
| --- | --- | --- |
| C. H. Bennett, *Notes on Landauer's principle, reversible computation, and Maxwell's demon*, Stud. Hist. Phil. Mod. Phys. 34, 501 (2003), arXiv:physics/0210005 | Abstract read | §6.1 items 1, 2, 4 |
| R. Landauer, *Irreversibility and heat generation in the computing process*, IBM J. Res. Dev. 5, 183 (1961) | Not read here | Item 2, item 4 (information-bearing distinction) |
| C. H. Bennett, *Logical reversibility of computation*, IBM J. Res. Dev. 17, 525 (1973) | Not read here | Item 1 |
| C. H. Bennett, *The thermodynamics of computation — a review*, Int. J. Theor. Phys. 21, 905 (1982) | Not read here | Item 1 (measurement as copying into a standard memory) |
| T. Sagawa, M. Ueda, *Minimal energy cost for thermodynamic information processing: measurement and information erasure*, PRL 102, 250602 (2009), arXiv:0809.4098 | Abstract read | C-10 |
| A. Bérut et al., Nature 483, 187 (2012) | Through LEAD §1–§2 only | C-2 |
| H. A. Kramers, Physica 7, 284 (1940) | Not read here | C-2 |
| P. Gács, *Reliable cellular automata with self-organization*, J. Stat. Phys. 103, 45 (2001), arXiv:math/0003117 | Abstract read | C-5 |
| A. L. Toom, *Stable and attractive trajectories in multicomponent systems* (1980) | Not read here | C-5 |
| W. H. Zurek, *Quantum Darwinism*, Nature Phys. 5, 181 (2009), arXiv:0903.5082; H. Ollivier, D. Poulin, W. H. Zurek, PRL 93, 220401 (2004), arXiv:quant-ph/0307229; R. Horodecki, J. K. Korbicz, P. Horodecki, PRA 91, 032122 (2015), arXiv:1312.6588 | Abstracts read | C-3 (rejection) |
| R. W. Spekkens, PRA 75, 032110 (2007), arXiv:quant-ph/0401052; arXiv:1409.5041; S. D. Bartlett, T. Rudolph, R. W. Spekkens, PRA 86, 012103 (2012), arXiv:1111.5057 | Abstracts read (titles for 1111.5057) | C-7 (rejection); comparator |
| E. P. Wigner (1952); H. Araki, M. M. Yanase, Phys. Rev. 120, 622 (1960) | Not read here | C-8 (rejection) |
| L. Szilard (1929); L. Brillouin (1951) | Not read here | C-10 |

***

## 7. Assumptions (hypothesis ledger)

| ID | Statement | Status |
| --- | --- | --- |
| Nq | `q = 2` | Native parameter |
| H-NW | No dependency cone winds within `T` | Modelling condition (as MI) |
| H-PS | Product sources | Modelling condition (as MI-D §3.1) |
| H-PREP | Supplied laws are in-realization conditionals of the stated measure | Open hypothesis (AP1:418), carried, not adopted |
| N2 | Uniform law on unknown slots | Native measure through H-PREP |
| BUD | `T` below recurrence | MR★ S-L6 |
| LB-W, LB-B, LB-F, LB-Z, LB-S | §4.3 | The construction. Proposed, not adopted |
| BLANK-SRC, SWAP-EXEC, RECORD-STORE, EXHAUST, TIMING | §5.2 | Supplied; named open inputs |

***

## 8. Properties evaluated (definitions fixed now)

Determination and bias are judged as in MI-D §1.2: branch by branch, on the entire joint record of
a single run, before any averaging.

- **Domain `D_t`.** The ring sites at tick `t` other than sink sites currently occupied by an
  exported registered register. A registered cell carries the observer's record by design; MI-A3 §1
  records that such a cell can be sharp ("its registered slot and its transported known slot need
  not commute"). The domain therefore separates the record from everything else. The full-ring
  variant is reported as a diagnostic (DG-FULL) and decides nothing.
- **NV, non-vacuity.** `Π_LB` on the given rule contains at least one protocol whose joint record
  is not independent of the carrier region `C`, and at least one protocol with a reset (LB-Z) after
  which the reused site is registered again. If NV fails, the class is vacuous for the question and
  no positive can be recorded (cf. P-GK's degeneracy, MI §4).
- **LK-R, leakage increment (primary, target-free).** For `π ∈ Π_LB`, let `ref(π)` be the same
  protocol with LB-Z's sink replaced by ideal terminality: the spent register goes to a decoupled,
  never-read store, as in AP1 SA-1(b) and MI-D §3.3. LK-R holds iff, for every `π`, every tick and
  every record branch of positive probability:
  - every function of the configuration on `D_t` that is determined given `K_t` under `π` is
    determined under `ref(π)`; and
  - every such function that is biased under `π` is biased under `ref(π)`.

  A violation is unintended leakage: information reaching the observer through export and the
  sink's return, beyond what single-use registration gives.
- **PROT-D_LB, PROT-B_LB (inherited, target-adjacent; recorded).** MI-D §4.1's PROT-D and PROT-B
  with "active cells" replaced by `D_t`: no linear functional on `D_t` with `Q* = 1` is determined
  (respectively, biased).
- **PROT-R′_LB (inherited; recorded).** MI-A3 §4's PROT-R′ with the cells active at `t′` replaced
  by `D_{t′}`.
- **USE-S, sink use (reach; §11.3).** Some function of the exported content changes the law of a
  later registered value. Equivalently: the sink is not dynamically inert on the register sites
  within `T`.

For non-linear rules, "linear functional" in PROT-D_LB/PROT-B_LB keeps MI's meaning: a linear
functional of current slots. LK-R quantifies over all functions.

***

## 9. Decision rule

### 9.1 Order of evaluation (fixed; never reversed)

Each step runs per rule (`N_1`, `N_0`, `G_σ`). The verdict for `N_1` is the construction's verdict.
The others are controls.

- **E0, entry review of motivation.** An independent reviewer classifies each clause of §6.2. The
  reviewer verifies the "not read here" items of §6.3 textually or strikes them. If any of LB-W,
  LB-Z, LB-F or LB-S is reclassified target-defined, or if C-1 is target-defined as a whole, the
  outcome is **C-0 (null)** and evaluation stops. A reclassification of LB-B to target-adjacent
  alone does not stop; it is carried into §9.3.
- **E1, controls before any verdict.** C-IMPORT, C-OFF-1 to C-OFF-4 setup, PR-1 to PR-11 and C-NC
  (§10). A red required control voids every verdict that relies on it.
- **E2, NV.** If it fails, the outcome is **VAC** (vacuous) and the walk stops for that rule.
- **E3, LK-R.** Proof or exhibited violation.
- **E4, PROT-D_LB, PROT-B_LB, PROT-R′_LB.** Proof or exhibited violation. DG-FULL is reported.
- **E5, USE-S.** Proof or exhibited inertness.
- **E6, variation analysis** (§11.2), for every load-bearing assumption.
- **E7, labels.** Outcome (§9.2), owner distinction (§9.3), ladder rung (§11.4), statuses (§9.4).
- **E8, comparison with the completion conditions.** Only after E7, and only as a record (§9.5).

**Standard of proof.** As in MI-D §4.4: paper derivation. A violation is exhibited by an explicit
protocol on a stated instance; a holding property needs a proof over all of `Π_LB` for that rule.
Any instance check by enumeration or program requires that Stage 1B's authorization permits it. This
file authorizes none.

### 9.2 Outcomes (per rule)

| Outcome | Condition |
| --- | --- |
| **POS** | NV holds; required controls green; LK-R, PROT-D_LB, PROT-B_LB and PROT-R′_LB proved; USE-S holds |
| **PART-INERT** | As POS, but USE-S fails: protection by an inert sink |
| **PART-EXTRA** | The properties hold only with a premise not in this file. The premise is reported, not adopted, and classed under §6.2 (CC-RECON if its only role is to block an exposure) |
| **PART-SPLIT** | The properties hold on the chosen values but fail on a variant of a load-bearing assumption that its own motivation supports equally (§11.2, class S-sel) |
| **NEG** | NV holds, required controls green, and an exhibited protocol in `Π_LB` violates LK-R or PROT-D_LB/PROT-B_LB |
| **VAC** | NV fails |
| **INC** | Neither proof nor violation is reached within Stage 1B's scope |
| **VOID** | A required control is red |
| **C-0** | Null at E0 |

Several outcomes may be reported side by side for one rule: for example, LK-R violated (NEG) while
PROT-D_LB holds. The rule-level label is the first applicable row in the order NEG, VAC, VOID, INC,
PART-EXTRA, PART-SPLIT, PART-INERT, POS. That order is fixed here.

### 9.3 Owner distinctions (a), (b), (c)

- **(a) Independently predicted positive.** POS for `N_1` with the configuration fixed in §4, no
  PART-SPLIT entry, E0 passed with LB-B's target-adjacent component found not load-bearing (§11.2),
  and robustness R-1 to R-4 complete (§10).
- **(b) Positive only after selection.** Any positive that needs:
  - a variant other than §4's fixed values (within the construction); or
  - LB-B's target-adjacent component as load-bearing; or
  - a premise reported under PART-EXTRA; or
  - the portfolio coordinator's choice of P-OBS among the three constructions because the others
    failed (across the portfolio).

  The selection among C-0 to C-13 in §3 was made before any evaluation and is disclosed (§11.5). It
  is recorded under (b) if the E0 reviewer finds that the selection used knowledge of consequences.
- **(c) Classical imitation.** P-OBS-LB is a configuration-level classical model. Every outcome is
  classically imitable by the model itself (C-NC). Wherever a comparison at E8 finds statistics that
  match a quantum subtheory (for example, toy-theory or stabilizer statistics in class N), the
  result is recorded under (c). A P-OBS positive is evidence about an access mechanism. It is never
  evidence for quantum selection.

### 9.4 Three statuses (recorded separately)

- **Proposed.** After the Stage 1A review: "proposed" iff the review accepts §6.2 with overall class
  independent or mixed. Otherwise "not proposed" (C-0).
- **Mathematically sufficient.** After Stage 1B: "sufficient for {properties} under {hypotheses}"
  iff POS or PART-INERT is proved for `N_1`, listing every hypothesis of §7 used. Otherwise "not
  established", with the outcome label.
- **Derived from native OI.** "Not derived" unless each of BLANK-SRC, SWAP-EXEC, RECORD-STORE,
  EXHAUST and TIMING that the proof uses has a recorded native source on main when Stage 1B
  reports. Fixed now (§5.2).

### 9.5 Comparison stage (record only)

After E7, Stage 1B records, without changing any label:

- whether the access model of `Π_LB` bears on condition (iv);
- whether class-N outcomes coincide with toy-theory statistics, which goes under (c);
- for every encoded statement, R1's group `A_4 ≀ S_n` (PR-1).

No criterion above refers to the target except to record an outcome (C-IMPORT).

***

## 10. Controls and countercontrols

| ID | Kind | Fixed pass criterion |
| --- | --- | --- |
| C-OFF-1 | Mechanism off: LB-Z | Replace export by in-place reuse: the spent register stays at `r` and is treated as the next blank (no swap). Report LK-R and PROT-*_LB. If the outcome equals the mechanism-on outcome, the mechanism is idle and no positive is attributed to LB-Z |
| C-OFF-2 | Mechanism off: interacting sink | Replace the sink by ideal terminality. By definition this is `ref(π)`; LK-R holds trivially. Must reproduce MI's C-LIN result for the linear limits (refills as reserve cells; MI §6.3). Failure to reproduce is red |
| C-OFF-3 | Mechanism off: LB-B | Fully known blanks. Must break PROT-D_LB on the supplied cell itself (MI §6.1 C-P2, "under any rule"). Not breaking is red |
| C-OFF-4 | Mechanism off: LB-F | Blank values chosen per step from records (MI's refills). Reported. Its outcome under `G_σ` must agree with MI's exhibited exposures where those protocols are admissible; a contradiction is red |
| C-NC | Classical imitation (Theorem NC; exhibited model) | State the configuration model as an exact classical imitation of every `Π_LB` record law. State where NC's hypotheses fail at `q = 2` (no native `Y` read; M2D:65–71). No nonclassicality may be claimed. Any quantum-statistics match is labelled (c) |
| C-IMPORT | Target import | (i) No §4–§8 definition contains a quantum quantity. (ii) PROT-*_LB are recorded, not motivating. (iii) No clause is added to `Π_LB` after Stage 1B begins. (iv) Any blocking premise is reported, not adopted, with CC-RECON. (v) Every verdict is generated from §9 |
| TT | Target-tuned countercontrol, must be rejected | Three premises, classified at E0 and E6 by §6.2's standard. Each must be classed target-defined, and none may enter a positive: **TT-1** P-GK′, "a blank is injected only where every gate that will act on it is known" (MI §4 P-GK); **TT-2** "the known slot of each blank is the slot that keeps the observer's knowledge on `D_t` isotropic"; **TT-3** "no exported register is placed within distance 2 of an unknown cell of `C`" (MI §4 P-NR analogue). If the standard fails to reject one, the classification procedure is defective and E0 is void |
| PR-1 … PR-11 | Preserved results (§11.1) | Each listed result is reproduced or not contradicted, as stated there |
| DG-FULL | Diagnostic | PROT-D on the full ring reported; decides nothing |
| R-1 | Robustness | Independent re-derivation of every holding property by a reviewer who did not author Stage 1B, from this file and the Stage 1B record alone |
| R-2 | Robustness | Both linear limits `N_1` and `N_0`; every `L` admitted by H-NW for the stated `T` (proof, not instance) |
| R-3 | Robustness | The variation analysis E6 complete, with every assumption classified |
| R-4 | Replication | Before promotion, a separately authorized check of each holding property on stated instances (an authorization question for the owner; none is granted here) |

A positive is not promoted, and does not count toward any physical selection principle, before
R-1 to R-4 are complete (c.6720450946).

***

## 11. Explanatory quality (AGENTS.md §A.29)

### 11.1 Preserved results (they become controls)

| ID | Result | Source | Control |
| --- | --- | --- | --- |
| PR-1 | Theorem U2: under R1⊗n the CP ontic permutations are `A_4 ≀ S_n`; no `rot`, `S`, `T` or entangling unitary | M2D:55–64, :404 | No encoded operation outside `A_4 ≀ S_n` is attributed to `Π_LB` |
| PR-2 | Theorem NC | M2D:483 | C-NC |
| PR-3 | M-INACC: exposures E_A, E_A′, E_B under `G_σ` in `Π_A`/`Π_B`; P-GK degenerate; PROT-R fails in the linear limits; PROT-R′ holds there (provisional, off main) | MI §0, §3, §4, §6.3; MI-A3 | Under `G_σ`, Stage 1B states for each of E_A, E_A′, E_B whether it lies in `Π_LB`. If one is excluded, the excluding clause is named and passed to E6. No result may contradict MI within MI's classes |
| PR-4 | AP1 Lemma 3 and controls C4, C9: terminality and half-known supply suffice for isotropy; removing either sharpens | AP1:533–560, :677, :682 | C-OFF-2, C-OFF-3 |
| PR-5 | QA Lemma Q (class N, under P1 and P2) | QA:458–479 | C-OFF-2 in the linear limits |
| PR-6 | Main (C1)–(C4) as diagnostics: (C2-structural) holds by reversibility in every bijective realization; (C3) capacity bound; (C4) readback | Main:74–80, :604, :614 | Any statement about the cycle's visible law must be consistent with them. USE-S is checked against (C4)'s operational form |
| PR-7 | TN and LEAD scoped retention obstructions (PAD, NP, AE, SS-2); "not a universal no-go" | TN §4, §6.2; LEAD §3 | P-OBS-LB claims no physical retention; RECORD-STORE remains supplied |
| PR-8 | S-L6: finite `S` gives `φ^N = id`; irreversibility only relative to a budget below recurrence | MR★:595 | BUD |
| PR-9 | (iv) fails in the access model and the stated-intervention theory | S0 row 9 | No (iv) claim |
| PR-10 | No sourced quiet ready region (MR★ C-3) | MR★:1342 | BLANK-SRC stays supplied |
| PR-11 | Complete passive observation holds exactly when the algebra is commutative | Main:592 | No complete passive-observation claim |

### 11.2 Variation analysis (decision rule only; nothing predicted)

**Claimed consequence.** The verdict of §9.2 for `N_1` (POS, or whichever label applies), together
with the LK-R verdict.

**Rule.** For each assumption `a` with the variant set `V_a` fixed below, Stage 1B evaluates the
claimed consequence on every variant and classifies `a`:

- **H (hard to vary):** every variant destroys the consequence, i.e. changes the §9.2 label or the
  LK-R verdict.
- **E (easy to vary):** every variant preserves it.
- **S (split):** some variants preserve it and some destroy it. Then:
  - **S-mot:** every destroying variant is excluded by `a`'s own §6.1 motivation;
  - **S-sel:** some destroying variant is supported by that motivation as well as the chosen value.
    The construction's choice then selects the consequence: PART-SPLIT, and (b).

**Overall reading.**

- If every assumption is E, the outcome is recorded as **poor explanation**, whatever the match to
  the question.
- If no assumption is H or S-mot, the rung is at most L1 (§11.4).

| Assumption | Variant set `V_a` (fixed) |
| --- | --- |
| A-B (blank form, LB-B) | {one slot known (chosen); both slots known; no slot known} |
| A-Bslot | {`u` known at injection (chosen); `v` known at injection; `u + v` known} |
| A-Bval | {standard value 0 (chosen); 1; either, per protocol} |
| A-F (LB-F) | {fixed law (chosen); per-step choice from records} |
| A-Z (LB-Z) | {export into interacting sink (chosen); export into decoupled store (= `ref`); in-place reuse} |
| A-atom | {registration and export atomic (chosen); export delayed by one tick} |
| A-S (LB-S) | {sink never registrable (chosen); sink registrable once per cell} |
| A-W (LB-W) | {register sites only (chosen); any ring cell registrable} |
| A-dist | {`d_S` = 1; 3 (chosen); `≥ L/2`} |
| A-rule | {`N_1` (primary); `N_0`}. `G_σ` is reported separately and is not a variant of the construction |

### 11.3 Reach

- **RCH-1, sink use (Main (C4); S0 rows 2 and 15; MI clause (a)).** The exported content must remain
  dynamically used (USE-S). A construction that avoids leakage only because exported content never
  influences later records has made its protection trivial. USE-S can fail, and failure gives
  PART-INERT.
- **RCH-2, recombination (AP1 §4.5; the #1169 combination gate, c.6713156200).** An unregistered
  copy can be undone by the reciprocal coupling, and a registered one, once exported, cannot be
  recalled by any register-site operation. Stage 1B states whether `Π_LB` reproduces AP1 §4.5's
  recombination result in `N_1` before export, and whether export makes the record irreversible
  within BUD. A contradiction with AP1 §4.5 is red.
- **No novel independently checkable consequence is identified.** RCH-1 and RCH-2 are
  internal-consistency tests on the consistency axis (§A.23). They can fail, so the cap "useful
  construction" does not apply. L3 (§11.4) has no candidate, so the highest reachable rung is L2.

### 11.4 Assessment ladder (recorded with (a)/(b)/(c))

- **L0.** The construction reproduces the target property: registration, retention and reuse
  without leakage (LK-R and PROT-*_LB hold).
- **L1.** It does so only through assumptions that are E or S-sel, or arbitrary (A-dist chosen
  without motivation and S-sel).
- **L2.** An independently motivated mechanism fixes several features, with at least two of A-B,
  A-Z, A-F and A-S classed H or S-mot. It also excludes the non-target alternatives: C-OFF-1 and
  C-OFF-4 destroy the property.
- **L3.** L2 plus a novel, independently checkable consequence. None is identified (§11.3).

Every outcome, negative ones included, is recorded at a rung or as "below L0".

### 11.5 Origin disclosure

- **Where the conjecture came from.** The writer read AP1's P1 and P2, MI's archive-swap refills and
  #1032/#1186 (Bérut; the Landauer/Bennett remark at LEAD:29) before forming C-1. The observation
  that MI's archive-swap refill has the form of a Landauer reset in a reversible dynamics came from
  reading MI §8, a target-oriented record. The search therefore ran from posits introduced for a
  target-adjacent programme (AP1's Lemma 3, toward the quarter-phase test) back to thermodynamics.
- **What that implies.** LB-Z and LB-B reproduce the structure of P1 (with one change, the
  interacting sink) and of P2 (with value 0 only). The resemblance is a product of the search
  direction, not a discovery. LB-B is the clause most exposed to retrofitting, and it is classed
  mixed for that reason.
- **Knowledge of consequences at drafting.** While fixing LB-B, the writer had read MI's protocols.
  E_A uses a supplied known value 1 (MI §3.2), which LB-B's value 0 excludes. E_A′ uses
  `v`-known and `u`-known cells at `t = 0` (MI §3.3). The slot `u` was fixed by item 4 of §6.1, the
  registered value being the information-bearing one. Whether `Π_LB` contains E_A′ or any other
  exposing protocol is not known to the writer and is a Stage 1B check (PR-3). TT-2 and A-Bslot
  test whether the slot choice is doing protective work.
- **The independence requirement is unchanged.** This disclosure does not relax it (c.6719386464).

***

## 12. Commitment to report

Stage 1B, if authorized, reports for each rule:

- the outcome of §9.2, whatever it is;
- (a)/(b)/(c), the ladder rung and the variation classification of every assumption;
- the three statuses of §9.4;
- every control with its status;
- every premise found to block an exposure, reported and not adopted.

This covers positive, negative, vacuous, inconclusive, void and null outcomes. A negative for
`Π_LB` is a negative for this access model on these rules only (§16). No outcome is withheld or
re-run with changed clauses. A changed clause is a new preregistration.

***

## 13. Invariant → checkpoint table (§A.41)

| Invariant asserted | Checkpoint that measures it |
| --- | --- |
| This commit adds exactly one file, this `DESIGN.md`, in `fhesel1-p-obs-20261108/` | `git show --stat` of the commit lists one added path |
| No result is derived here | Reviewer reading of §4–§11; `grep -n -i 'we find\|it follows that\|holds for every'` matches only this row |
| The decision rule precedes any Stage 1B text | Stage 1B's first commit is a descendant of this commit, and this file is byte-identical there (`git diff` empty for this path) |
| No `readWriteSourced_` identifier is cited | `grep -n readWriteSourced` on this file matches only K-LEAN (§2) and this row, which name the prohibition |
| No odd-`q` statement | `grep -n -i odd` matches only K-Q (§2), §16 and this row |
| §6.1 contains no quantum quantity | Grep of §6.1 for "quantum", "Born", "unitar", "complete positiv", "completion", "Q*" returns nothing |
| Repository citations are to main `9c201475`, or to the stated off-main commits `f649b347` (MI) and `25384b13` (Q3) | Reviewer check of every `File:N`, and of each full SHA, against `git cat-file -e` |
| No file of the other two constructions is cited | `grep -n -i 'p-control\|p-mix'` matches only this row |
| M-INACC is cited as provisional and off main | §14 classifies MI as "support off main: gap"; PR-3 says "provisional, off main" |
| Every candidate considered has a decision and reason | §3 has one row per candidate C-0 to C-13 with a non-empty decision cell |
| The variation sets are fixed before evaluation | §11.2 table is byte-identical at Stage 1B's first commit (first row of this table) |

***

## 14. §A.42 item 8 trace

| Reference | Used for | Class |
| --- | --- | --- |
| #1169 c.6720450946, c.6720342295, c.6719386464, c.6719192859 | Authorization, scope, standard, tiers | Provenance |
| #1169 c.6713156200 (joint synthesis) | RCH-2's combination-gate wording | Provenance |
| S0 (#1169 c.6719708521; review c.6719720616) | Rows 9 and 16; the rows are restated here with their on-main citations | Provenance. The restated row content rests on files on main (AP1, QA, Main, Sub), cited directly |
| #1198 head `f649b347` (MI, MI-D, MI-A3) | K-MI, PR-3, definitions of §8, TT-1, TT-3 | **Support off main: a gap.** MI is provisional (model-reviewed, unmerged). No established claim rests on it. Every use is as a preserved result to be checked or as a definition restated here |
| #1202 head `25384b13` (Q3-A1 §3 C2) | Classification standard | Provenance. The standard is restated in full in §6.2, so the classification does not depend on the off-main text |
| #1032 body and c.6712887557, c.6713169247, c.6567189236 | K-1032; C-2; non-duplication | Provenance. The content used (LEAD) is on main |
| LEAD, TN | C-2, PR-7, RECORD-STORE | Support on main |
| #1188 | K-LEAN | Provenance |
| #1193 | K-Q | Provenance |
| #866, #1147 | SWAP-EXEC, BLANK-SRC ownership | Provenance (Issues) |
| arXiv abstracts and journal references of §6.3 | Motivation and rejections | External literature; "read here" is marked per item; E0 verifies the rest |

***

## 15. Concerns for the coordinator and the reviewer

1. **Independence (main concern).** The search ran backward from target-adjacent posits (§11.5).
   LB-B coincides in form with P2 and with knowledge balance. E0 must decide whether item 4 of §6.1
   is a motivation or a retrofit.
2. **Possible vacuity.** With value-0 blanks only and every non-register site unknown, the class may
   register nothing informative about `C`. That would give VAC, recorded as a finding and not
   repaired by adding supplies.
3. **Domain choice.** `D_t` excludes exported registered cells. The reason is MI-A3 §1's
   record/active distinction. A reviewer may judge that the exclusion hides leakage. DG-FULL is
   reported for that reason.
4. **Supplied load.** Five named open inputs remain supplied. "Derived from native OI" is
   unreachable without them (§9.4), and the most a positive can give is "mathematically sufficient
   under named supplied inputs".
5. **Overlap with #1032 and #866.** BLANK-SRC, RECORD-STORE and SWAP-EXEC fall in Codex's and #866's
   areas. P-OBS does not source them. If #1032 lands a source for any of them, P-OBS cites it and
   does not re-evaluate it.
6. **Classical by construction.** Every P-OBS outcome is classically imitable (§9.3 (c)). Its value
   is to the access-model question of S0 row 9, not to quantum selection.

***

## 16. Not claimed

- Any result about `Π_LB`. Every property of §8 is open until Stage 1B.
- A physical source for blanks, swaps, record storage, exhaust or timing.
- Physical retention of any record (#1032).
- Any statement for rules other than `N_1`, `N_0` and `G_σ`; for access models other than `Π_LB`;
  or for odd `q`.
- Any statement about composites; P-OBS-LB is single-ring.
- Nonclassicality, contextuality, a quantum operation, condition (iv) or OI–QM equivalence.
- That a negative for `Π_LB` excludes every observer-level registration mechanism.
