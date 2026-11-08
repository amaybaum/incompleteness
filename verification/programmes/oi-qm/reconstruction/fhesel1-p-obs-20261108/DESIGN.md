# FHE-SEL-1 P-OBS: preregistration (Stage 1A)

**Standing.** WIP / UNVERIFIED. Stage 1A preregistration of the P-OBS construction under #1169,
revision r3. r2 applied the independent review of `7878a7fd`, and r3 applies its re-review at
`40f42bd9` (both verdicts REVISE; review texts relayed by the coordinator, not on `main`). Writer: Claude Code session (P-OBS writer), 2026-11-08. Each review
of this file is by a reviewer who reviews no other construction of the portfolio. Paper only: no
result is derived, nothing is computed, simulated, built in Lean or run under V3, nothing is
adopted, and no manuscript is edited. Stage 1B is not authorized. Every verdict this file provides
for is generated in Stage 1B, if authorized, from the rule fixed here.

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
  at #1202 head `25384b13526dfa23909bbd63a119508091f467c7`. Only its classification standard is
  used: §3 Block C, C2 at Q3-A1:185, with C3 (search record) at Q3-A1:206. The standard is restated
  in full in §6.2.
- `S0` = the Stage 0 map, #1169 c.6719708521, with its review c.6719720616 and confirmation
  (ACCEPT; c.6719723538). Its standing line reading "pending" is stale. Its file:line citations are
  to main `f88c1842`; between `f88c1842` and `9c201475` main adds only
  `controller-preparation-1-20261108/SELECTION.md`, so every cited line is unchanged at the pin.

**Symbols.** `T` is the time horizon. `𝒯` is the target (§6.2).

***

## 0. What this file fixes

1. **Question** (§1). What physical mechanism permits registration, retention and reuse of records
   without unintended leakage of information?
2. **Candidates** (§3). Fourteen candidates are recorded, C-0 to C-13, with the reason each is
   selected or rejected. One construction is selected, P-OBS-LB (a Landauer–Bennett record cycle).
   A null outcome is preregistered as admissible.
3. **Construction** (§4). P-OBS-LB on a finite ring at `q = 2`.
   - Registration only by copy onto a standard blank.
   - Reset and reuse only by export of the spent register into an interacting hidden sink.
   - Blanks come from a reservoir whose law is fixed in advance.
   - Rule `N_1` is primary; `N_0` and `G_σ` are controls.
4. **Source ledger** (§5). Each resource is classed native / supplied / representation / imported.
   The named open inputs are BLANK-SRC, SWAP-EXEC, RECORD-STORE, EXHAUST and TIMING.
5. **Motivation and classification** (§6). Overall: **mixed**. Components pending the entry review
   E0 are marked.
6. **Properties** (§8). Each is defined without further choice:
   - non-vacuity NV (conjunctive);
   - the reference `ref(π)`, fully specified;
   - the target-free leakage test LK-R is the conjunction of a matched-history comparison and a
     sink-only-history test;
   - `PROT-D/B/R′_LB` on M-INACC's own active domain (every cell on the ring), with a discount
     that removes, as a summand, only exported content already determined at export, checked by
     the definitional control C-DISC;
   - sink use USE-S, defined comparatively against `ref(π)`.
7. **Decision rule** (§9). A fixed entry review E0 with stated exits, and a total, ordered outcome
   table, including LIMIT when a decisive test fails its countercontrols. It also fixes one rule for
   (a)/(b), the ladder L0–L3, the three statuses and a rule against adjustment (§9.7).
   Justifications for the leak test and the discount are recorded before any result (§8.6).
8. **Controls** (§10). Mechanism-off, classical imitation (attributed to the exhibited model), target
   import, the owner's two decisive countercontrols CC-ACCEPT and CC-REJECT with the discount
   control C-DISC, an external positive calibration, four target-tuned
   countercontrols (one disguised), preserved results and robustness.
9. **Explanatory quality, §A.29** (§11). Preserved results, the variation analysis and its decision
   rule, reach, the assessment ladder and the disclosure of origin.
10. **Report commitment** (§12), the invariant → checkpoint table (§13), the §A.42 item 8 trace
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
- **#1169 c.6720342295** (amaybaum, 2026-11-08T10:26:34Z), planning clarification.
  - P-OBS scope: "What physical mechanism permits registration, retention and reuse without
    unintended leakage of information?"
  - Safeguard: "Must keep M-INACC's leakage findings: registration and refill can expose hidden
    information (#1198). Physical mechanisms are sourced under #1032 (Codex)."
  - Anchors: "Apparatus-1 P1/P2; M-INACC; in Stage 0, the measurement-interface rows."
  - Three statuses: proposed / mathematically sufficient / derived from native OI.
  - Order: "First, independent physical motivation. Second, evaluation of consequences. Third,
    comparison with the quantum completion conditions. The order is never reversed."
- **#1169 c.6719386464** (amaybaum, 2026-11-08T08:41:15Z). The owner's words: "Every candidate
  physical restriction must have an independent physical motivation established before evaluating
  whether it selects quantum behaviour. A restriction that eliminates an unwanted classical model is
  not automatically evidence that nature obeys that restriction." Refinement 1, approved by the
  owner: "A restriction designed to exclude a particular construction is treated as tuned to the
  target."
- **#1169 c.6719192859** (owner guidance on M-INACC tiers). The owner's words: the most important
  part is "the classical-imitation control".
- **#1169 c.6720678942** (amaybaum, 2026-11-08T11:03:23Z), two workstreams.
  - P-OBS belongs to the **physical-selection** workstream. Its question is "why should OI or nature
    select a given extension?" Its success criterion is "independent motivation, physical sourcing,
    explanatory necessity and critical tests". Its standards are c.6720450946 and §A.29.
  - Owner refinement 2, in the owner's words as recorded:
    - "Theorem NC supplies a noncontextual model under its identification and spanning-read
      conditions."
    - "Theorem U2 restricts the available encoded unitaries under its finite-frame and
      operation-set assumptions. It does not exclude every finite-order non-Clifford operation in a
      different extension."

    §2 (K-NC, K-FIN), §10 (C-NC) and PR-1 apply this refinement.
  - "None may influence another construction's frozen rule without a documented amendment."
  - "No derivation, computation, V3 execution, new physical premise, manuscript promotion or merge
    is authorized by this decision."

- **Owner decision on P-OBS** (chat, 2026-11-08, relayed by the coordinator; binding for r3, not
  yet posted on #1169 at this commit):
  1. "Two decisive countercontrols": "an ordinary exported record that is correctly accepted" and
     "a deliberately planted information leak that is correctly rejected", evaluated "against
     adaptive strategies and complete accessible histories". "If no definition passes both, the
     correct outcome is to report the limitation and stop."
  2. The discount rule and the leak test must each be justified as meaningful definitions,
     independently of whether the candidate passes them. The owner's words: "A technically
     non-vacuous test is necessary, but not sufficient, if its definition is still tailored to the
     candidate."
  3. No adjustment made solely to obtain a positive result.

  §8.6 (justifications), §10 (CC-ACCEPT, CC-REJECT), §9.3 (LIMIT) and §9.7 (no adjustment) apply it.

### 1.2 Stage 0 rows targeted

- **Row 9, measurement interface (primary).** Tag R. "P1 and P2 are supplied (AP1:419–420)."
  Column (d): "Native reciprocal backaction, in part (AP1:311–330) … P1 and P2 lack independent
  motivation (AP1:349, 357–363)." Residual freedom: "Which instruments, and which access or
  intervention model." P-OBS-LB proposes a physically motivated access model for the registration,
  reset and supply that P1 and P2 currently supply.
- **Row 16, inaccessible but dynamically used memory (evaluation).** Tag R. "Lemma Q in class N,
  given P1 and P2 (QA:458–479) … Fails for `G_σ` (MI; provisional; §4)."
  - P-OBS-LB is evaluated on whether its cycle keeps what row 16 records for class N once P1's
    decoupled archive for registered cells is replaced by export into an interacting sink.
  - The construction does not remove the decoupled-store idealization. It relocates it to the
    displaced former sink occupants, which go to the decoupled exhaust `Ex` (EXHAUST, §5).
- **Reach rows** (§11.3). Row 2 (preloaded content and its storage form) and row 15 (hidden dynamics
  between couplings), through USE-S. Row 4 (reversibility) is used and not targeted.

***

## 2. Constraints carried from the record

| ID | Constraint | Source | How P-OBS-LB meets it |
| --- | --- | --- | --- |
| K-NC | MECH-2 Theorem NC, within its exact hypotheses: under an injective identification with H-LIFT and spanning-read certification, the configuration model is a noncontextual model of the encoded theory, for any dynamics. Hence a construction must change the identification or the access, not only the dynamics | M2D:65–71, M2D:483–498; c.6720678942 refinement 2 | P-OBS-LB changes the access (registration, reset, supply). It leaves the rule and the identification unchanged and claims no nonclassicality. At `q = 2` over native `Z`/`X` reads alone NC does not apply. Classical imitability of P-OBS's configuration-level record laws rests on the exhibited model itself, not on NC (C-NC, §10) |
| K-MI | M-INACC: under `G_σ`, registration and refill expose the `Q* = 1` functional in `Π_A` and `Π_B` (E_A, E_A′, E_B; outcome (B, B), tiers Negative). P-GK is degenerate. PROT-R fails even in the linear limits; PROT-R′ holds in them | MI §0, §3, §4, §6.3; MI-A3 §1, §4 (provisional, off main; model-reviewed) | Preserved as PR-3, with its off-main status (§11.1). No clause of P-OBS-LB is chosen to block E_A, E_A′ or E_B. TT-1 to TT-4 check this (§10) |
| K-FIN | Finite carriers. Theorem U2 within its exact hypotheses: (i) under R1⊗n the CP ontic permutations are `A_4 ≀ S_n`; (ii) under Lemma F's operation set ("attach cells in fixed laws, apply the rule, feedback, discard, condition on configuration records") and H-LIFT, any branch acting on the encoded carrier as `p · Ad U` with input-independent `p > 0` has `Ad U = T_π`, `π ∈ A_4 ≀ S_n`. AP1 excludes `rot` on finite carriers | M2D:48–64, :404–413; AP1 §5.3; c.6720678942 refinement 2 | P-OBS-LB is finite and claims no encoded operation. PR-1 (§11.1) applies U2 only within its hypotheses. Stage 1B first states whether `Π_LB`'s operations are in Lemma F's set and satisfy H-LIFT. U2 says nothing about non-unitary encoded maps or about operations outside that set |
| K-SUP | Supplied access, records, preparation or control does not count as physically generated | c.6720450946 | Every resource is in the §5 ledger. "Derived from native OI" requires all five named inputs to be native, each sourced by an established claim on `main` (§9.5) |
| K-IV | Condition (iv) fails natively (`permTheory_not_control`, `substratumGen_not_control`); the residual is in the access/intervention model | S0 row 9 | P-OBS-LB makes no claim about (iv). The comparison stage only records whether its access model bears on (iv) (§9.6) |
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
| C-1 | Landauer–Bennett record cycle: registration by reversible copy onto a blank; reset only by exporting the register's content into other degrees of freedom of an environment; blank supply as a consumed resource | Landauer 1961; Bennett 1973, 1982, 2003 (§6.3) | Mixed (§6.2), components pending E0 | **Selected** as P-OBS-LB. It is the only candidate whose motivation is stated without the target and that fixes a form for all three stages, including reset, which is the step where M-INACC's exposure entered (MI §8, "archive-swap refills act as gate settings") |
| C-2 | Barrier-protected metastable memory (Kramers hopping; trapped bead with camera read) | LEAD §2; Bérut et al. 2012; Kramers 1940 | Independent, external | **Rejected as P-OBS's mechanism; carried as a dependency.** It is a retention mechanism and is silent on leakage. Its native sourcing is #1032's open item (LEAD:95, "First missing ingredient"). Duplicating it is outside this unit (K-1032) |
| C-3 | Redundant environmental records (quantum Darwinism, objectivity, spectrum broadcast structures) | Zurek 2009; Ollivier, Poulin, Zurek 2004; Horodecki, Korbicz, Horodecki 2015 | Target-defined | **Rejected.** Stated for quantum systems (pointer states, decoherence). Its classical residue, many copies of one record, multiplies access paths and does not address leakage |
| C-4 | Classical repetition / majority redundancy for retention | Standard coding | Independent | **Rejected.** Retention against noise only. Added copies are added read paths; there is no leakage content |
| C-5 | Self-correcting local memory (Toom's rule; reliable cellular automata) | Toom 1980; Gács 2001 | Independent | **Rejected.** Noise-robust retention with dissipative local rules. In a bijective substratum it needs a supplied cold sink, which is the same unsourced resource as C-1's blanks, and it does not address leakage. Recorded for #1032 |
| C-6 | Symplectic reciprocity extended to every coupling, gates included ("full-map reciprocity") | Hamiltonian action–reaction; AP1:313–327 | Independent in motivation, but no definition for nonlinear maps over `F_2` | **Rejected.** Over `F_2` it has no stated meaning for non-affine rules. Adopting it now would act chiefly to exclude `G_σ`, a particular construction: tuned under refinement 1. Its class-N content is already QA's Lemma Q |
| C-7 | Epistemic restriction (knowledge balance; classical complementarity) | Spekkens 2007, 2014; Bartlett, Rudolph, Spekkens 2012 | Target-adjacent | **Rejected as motivation.** Introduced to reproduce quantum phenomena (Spekkens 2007 abstract). Used only as a comparator (§9.6) |
| C-8 | Conservation-limited measurement (Wigner–Araki–Yanase) | Wigner 1952; Araki, Yanase 1960 | Target-defined | **Rejected.** Stated for quantum observables. Its classical analogue, conservation of `Q`, is tested in MI and does not protect under `G_σ` (MI §6.2) |
| C-9 | Causal-cone locality of records | Main:364 | Independent | **Rejected as mechanism.** Non-discriminating: `G_σ` satisfies it (MI §6.1, C-NS green) |
| C-10 | Information acquisition bounded by negentropy consumed (Szilard–Brillouin–Sagawa–Ueda accounting) | Szilard 1929; Brillouin 1951; Sagawa, Ueda 2009 | Independent | **Not a separate candidate.** A global budget, not a mechanism. Kept inside C-1 as the resource ledger. Whether it constrains per-cell determination is a Stage 1B question; it is not assumed to |
| C-11 | Wake / passing-field reads | MR★ C-2, C-4 | — | **Rejected as out of scope.** It is #1032's route I, recorded `UNDECIDED` in MR★ C-4. Not duplicated |
| C-12 | Non-equilibrium environment as blank supply (observers in a non-equilibrium phase) | Main §4.6 (conditional on EM); MR★ C-3 | Mixed | **Not selected; recorded as candidate source for BLANK-SRC.** MR★:1353: "No principle in the corpus supplies one." Sourcing is #1032/#1147 territory |
| C-13 | State-dependent geometry as protector | SM:104; M2D §0 item 1 | Independent proposal | **Rejected as P-OBS's mechanism.** Tested within scope by MI and fails there (provisional). Kept as a control rule (`G_σ`) |
| C-0 | Null: no candidate | — | — | **Admissible outcome.** E0's exits give C-0 (§9.1) |

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
- **Sink entry sites.** For each register site `r`, one fixed site `s(r)` outside `C` and `Rg`, at
  ring distance `d_S = 3` from `r` and on the side of `r` away from `C`. Both are parameters
  (§11.2, A-dist and A-side). They are fixed per protocol before `t = 0`.
- **Background.** Every other ring site holds a source cell (the hidden sector).
- **Reservoir `Res`.** Decoupled cells outside the ring, each a standard blank, injected only by
  LB-Z. This is MI §6.3's reserve-cell representation, holding blanks only.
- **Exhaust `Ex`.** Decoupled cells outside the ring, never injected and never read (§4.3, LB-Z).

### 4.3 The access mechanism (the construction proper)

- **LB-W, registration by copy onto a blank.** The observer acquires a record value only by
  registering the `u` slot of the cell at a register site. Carrier cells and background cells are
  never registered directly. Information reaches a register only through the fixed rule's coupling.
- **LB-B, standard blank.** At its injection tick a blank has `u = 0` known and `v` unknown,
  uniform and independent of everything else. No other supplied cell exists: no value 1, no
  `v`-known or `(u + v)`-known supply, and no fully known cell.
- **LB-F, reservoir fixity.** The blank law of LB-B is fixed before any protocol and does not depend
  on the protocol, the records or the carrier. The protocol chooses only when a registration (and
  with it a reset) occurs. It never chooses blank values.
- **LB-Z, reset by export (atomic with registration).** Immediately after the `u` slot at register
  site `r` is registered, between the same two ticks, a cyclic permutation of three cells is
  executed:
  1. a blank from `Res` goes to `r`;
  2. the spent register goes to `s(r)`;
  3. the former occupant of `s(r)` goes to `Ex`.

  The spent register then evolves on the ring at `s(r)` under the fixed rule, coupled to its
  neighbours. Nothing is erased: the cycle is a permutation of cells.
- **LB-S, sink inaccessibility.** No cell at a site outside `Rg`, and no cell in `Ex`, can be
  registered. Content at sink sites can reach a register only through the fixed rule's dynamics.
- **Strategy.** A protocol is a strategy `π`: the fixed data (`C`, `Rg`, `s(·)`, `d_S`, side) together
  with a map from record histories to the set of register sites registered between ticks `t` and
  `t + 1`. The map may depend on earlier records (adaptivity).
- **Protocol class `Π_LB`.** All such strategies on a given rule, with horizon `≤ T`. Sequential
  composition: the outgoing ring configuration, `Res`, `Ex` and the records are the input of the
  next protocol.

### 4.4 Records, retention and reuse

- **Records and knowledge.** The joint record is the list of registered values with their sites and
  ticks. Knowledge `K_t` is the record up to `t`, the strategy `π`, and the blank law.
- **Retention.** A registered value is held in the observer's record store. Its physical retention
  is RECORD-STORE (§5.2), supplied. The physical register is exported by LB-Z, and P-OBS-LB
  provides no persistence mechanism for it. Persistence belongs to #1032 (C-2).
- **Reuse.**
  - *Register sites* are reused after each LB-Z reset.
  - *Carrier continuation:* the carrier keeps evolving and can be registered again through
    registers.
  - *Recombination:* an unregistered register keeps interacting under the rule, so any un-copying
    (AP1 §4.5) happens only through the dynamics.
  - *Record-conditioned preparation:* excluded by LB-F.

### 4.5 What differs from AP1 and MI

| Element | AP1 / MI | P-OBS-LB |
| --- | --- | --- |
| Registered cell after registration | Archived: leaves the ring, couples to nothing (P1; MI-D §3.3) | Exported into the ring at `s(r)`, where it keeps coupling (LB-Z) |
| Decoupled stores | The archive holds registered cells | `Ex` holds the displaced former occupants of sink sites, which are never registered. The decoupled-store idealization is relocated, not removed (EXHAUST) |
| Supplied cells | Either slot known, value 0 or 1 (H-PREP), chosen by feedback (MI-D §3.1, §3.2) | `u = 0` known at injection only; fixed law (LB-B, LB-F) |
| What may be registered | Any active cell (MI-D §3.3) | Register sites only (LB-W) |
| Isolation, multipliers | `Π_B`: P3, E-iso | None |

Whether MI's protocols E_A, E_A′ and E_B, or AP1's C9 protocol, lie in `Π_LB` is a Stage 1B check
(PR-3, PR-4). It is not assumed in either direction.

***

## 5. Source ledger

### 5.1 Entries

| Resource | Class | Note |
| --- | --- | --- |
| Finite ring, cells in `F_2²` | Native | A1 posit (finiteness) unchanged |
| Rule `N_1` (and `N_0`) | Native | A4/A5 posits; A4's no-self-term clause has open warrant (S0 row 9, §3 A4) |
| Rule `G_σ` | Representation (corpus candidate) | Control only; from SM's state-dependent-geometry hypothesis via MI |
| Bijectivity of every step and of LB-Z's permutation | Native (A2) for the rule; LB-Z's execution is supplied (SWAP-EXEC) | A2's corpus motivation is mixed (S0 row 4); LB-Z uses only its information-conservation prong |
| Observer/hidden partition | Native as OI's definition (Main:44) | The placement of `C`, `Rg` and the sink sites is representation |
| Placement of `C`, `Rg`, `s(·)`, `d_S`, side | Representation | Fixed per protocol before `t = 0` |
| Uniform unknown slots (sources, blanks' `v`) | Native measure through the open hypothesis H-PREP | AP1:416, 418 |
| Standard blanks and the reservoir | Supplied | Named open input BLANK-SRC |
| Execution of LB-Z | Supplied | Named open input SWAP-EXEC (a controller act; #866 territory) |
| Registration act and record store | Supplied | Named open input RECORD-STORE. LEAD:101: "The later read has its own missing bridge" |
| Exhaust `Ex` (decoupled, never read) | Supplied idealization | Named open input EXHAUST |
| Schedule and clock | Supplied | Named open input TIMING; S0 row 5: no clock source passes CTL's gate |
| Reference devices of §8 (`ref(π)`'s archive `Arc` and fresh source cells) | Representation (comparison device only) | Not part of P-OBS-LB; used only to define LK-R |
| R1 encoding | Representation (comparator only) | Used only in C-NC and PR-1 |
| Literature of §6.3 | Imported (motivation only) | Not a premise of any derivation |
| Qubit stabilizer theory, toy theory | Imported (comparator only) | §9.6 |

### 5.2 Named open inputs

- **BLANK-SRC.** A physical source of standard blanks under one fixed law. MR★:1353 records that no
  principle in the corpus supplies a quiet ready region. #1147 and #1032 hold the readiness and
  register obligations. Not sourced here.
- **SWAP-EXEC.** A physical process that executes LB-Z's permutation under the fixed rule. Not
  sourced. Controller sourcing is #866 (CP-PREP-1 at main `9c201475`, source gate not passed).
- **RECORD-STORE.** A physical registration act, a physical retention of registered values, and the
  read into a public record. It depends on #1032 (LEAD §4; TN §6.2: "not a universal no-go").
- **EXHAUST.** A decoupled, never-read store for displaced sink occupants. Supplied, as in MI §6.3's
  reserve-cell representation.
- **TIMING.** A source of the schedule. Not sourced.

**Consequence fixed now.** All five are supplied. "Derived from native OI" therefore cannot be
reached unless each of the five is first sourced by an established claim on `main` (§9.5). This is
stated before any result.

***

## 6. Independent physical motivation

### 6.1 Motivation (stated without the target)

Each item states what is supported by a source read in this unit and what is the writer's reading.
Items or parts marked **[pending E0]** rest on sources not read here. They do not count as support
until E0 verifies them in the text (§9.1).

1. **Registration as copying onto a blank.**
   - *Read here:* "any logically reversible transformation of information can in principle be
     accomplished by an appropriate physical mechanism operating in a thermodynamically reversible
     fashion" (Bennett 2003, abstract).
   - **[pending E0]** A measurement can be modelled as such an operation: the measured value is
     copied into a memory that starts in a known standard state, and the memory then holds the
     record (Bennett 1982; also Bennett 1973).
   - LB-W states this for the ring. Information about the carrier reaches the observer only through
     a cell that began in a known standard state and was coupled to the carrier by the same dynamics
     that moves everything else.
2. **Reset requires export.**
   - *Read here:* "any logically irreversible manipulation of information, such as the erasure of a
     bit … must be accompanied by a corresponding entropy increase in non-information bearing
     degrees of freedom of the information processing apparatus or its environment" (Bennett 2003,
     abstract, stating Landauer's principle).
   - *Without literature:* in a dynamics that conserves information (A2), a memory cannot be
     returned to its standard state by destroying its content; the content must be moved into other
     degrees of freedom.
   - LB-Z states this for the ring. Reuse of a register site is a permutation that moves the spent
     register into the environment and brings in a fresh standard memory.
3. **The environment keeps evolving.** The degrees of freedom that receive exported content obey
   the same dynamics as everything else. Main's observer is a proper subsystem coupled to its
   complement through the same `φ` (Main:44). Visible and hidden lattice degrees of freedom obey the
   same local rule (Sub:48). LB-Z therefore places the exported register on the ring, where it keeps
   coupling, rather than in a store that couples to nothing.
4. **The standard state of a blank.**
   - *Read here:* the abstract quoted in item 2 distinguishes information-bearing from
     non-information-bearing degrees of freedom only to say where erasure deposits entropy.
   - **[pending E0]** *Writer's reading, not a statement of any source read here:* a reset fixes the
     information-bearing value of the memory and leaves its other degrees of freedom of the same
     memory at the thermal law (Landauer 1961, not read here). Applied to a second-order cell, the
     registered present value `u` is taken as the information-bearing value. The previous-slice
     value `v` is left at the maximal-entropy law (Main:56, through H-PREP). The mapping to the
     `(u, v)` cell is the writer's.
   - *A second reading, for E0 to weigh* (raised by the review): position reset, velocity thermal,
     as for a reset bead. With `u` known, the discrete velocity `u + v` is uniform exactly when `v`
     is uniform, so this reading gives the same supply law. It is not textually verified either.
   - *A reading that would give a different law:* a quiescent memory, `u = v = 0`, is an equally
     natural reset of a second-order cell when AP1/P2 are not in view (review's judgement). It is
     variant "both slots known" of A-B (§11.2).
5. **A reservoir is fixed in advance.** A reservoir is a system whose state law is set before, and
   independently of, the process that draws on it. LB-F states this. It matches GA's admission
   contract, which excludes fitted seed laws and record-conditioned loading (GA:75–106).
6. **The environment is not read.** Exported content is outside the observer's registers (LB-S).
   This is what "environment" means in item 2, and Main's partition of `S` into observer and
   complement (Main:44).

### 6.2 Classification (Q3-A1 §3 Block C, C2–C3, restated)

**The standard.** `𝒯` means quantum behaviour, the Born rule, complete positivity, unitaries, the
completion conditions, and the protection of the `Q* = 1` class (the protected class of QA and MI,
chosen there for the quantum target). Each assumption is judged on its own, without the rest of the
construction. What it yields together with the construction is a consequence (§8), never a
motivation. No clause counts deriving `𝒯` (or its negation) as a merit or as a demerit.

- **Independent.** The stated motivation and its support do not presuppose `𝒯` and are not designed
  to exclude a particular construction.
- **Target-adjacent.** Taken on its own, the assumption or its motivation presupposes `𝒯`, is
  equivalent to part of `𝒯` on the class at issue, or is supported only by a consequence of `𝒯`.
- **Target-defined.** The stated reason is to obtain `𝒯` or to exclude a particular construction.
  Or, by the functional test, the assumption's statement is a restriction on the protected
  functional itself, with no stated effect outside it.
- **Mixed.** An independent component together with a target-adjacent one, each identified.
- **None found.** No motivation located after a search. Every "none found" carries its search
  record (C3): the corpus locations and literature searched, so that it is backed by a corpus-wide
  search (§A.19).

**Extensional check (added for TT-4, §10).**

- **Rule.** Two premises are extensionally equal if they admit the same strategies of `Π_LB`. A
  premise extensionally equal to another recorded premise takes the more target-ward of the two
  classes, in the order independent, mixed, target-adjacent, target-defined. A premise equal to one
  with a recorded blocking reason (MI §4's P-GK, P-NR, P-1) is at least target-adjacent.
- **Exemption.** The rule does not apply if the premise has an independent reason **recorded
  before** the other premise.
- **"Recorded before".** This is judged on the reason **as applied to the premise**, not on the date
  of the source the reason cites. The date is that of the earliest commit or recorded comment that
  states the application, here the mapping onto the premise's own terms. It must precede the
  earliest commit or comment that states the other premise.
- **Consequence for LB-B.** LB-B's application of item 4 (the mapping onto the `(u, v)` cell) was
  first recorded at `7878a7fd`, after AP1 recorded P2 and after MI. The exemption therefore does not
  apply to LB-B against P2 restricted to `u`-known value 0. E0 classifies P2's recorded reason
  (§9.1, item 3), and the exits of §9.1 then fix LB-B's consequence.

| Clause | Class | Reason |
| --- | --- | --- |
| LB-W | Independent **[pending E0]** for its measurement-as-copy component | Bennett 2003 abstract read; Bennett 1982 not read here. If E0 strikes Bennett 1982, LB-W's class is re-decided on the remainder |
| LB-Z | Independent | A2 with information conservation; no literature needed. Subject to E0's ordinary classification and exits |
| LB-Z, interacting sink (item 3) | Independent | Main:44, Sub:48 |
| LB-B | **Mixed**, independent component **[pending E0]** | Independent component: item 4's information-bearing/thermal reading (not read here). Target-adjacent component: the resulting one known slot per supplied cell coincides with AP1's P2, whose motivation is "closure plus the E-AR obstruction … a programme-internal reason" (AP1:347–349), and with the knowledge-balance principle (C-7). The choice of `u` as the information-bearing slot is the writer's mapping |
| LB-F | Independent | Reservoir definition; GA:75–106 |
| LB-S | Independent | Main:44 partition. It is a lack of access, not a supplied access |
| Record discount `Disc_t` in `PROT-*_LB` (§8.3) | **Mixed** | Independent component: the question's own distinction between intended (registered) and unintended information; the discount removes only exported content determined at export. Target-adjacent component: the discount was shaped with knowledge of MI-A3 §1's archived-cell countercase, of E-SHARP and of the r2 re-review's counterexample (§8.3), and its effect is on the protected class |
| Leakage increment LK-R (§8.2) | Independent | Defined relative to `ref(π)` and functions of world variables, without `𝒯` |
| `PROT-D/B/R′_LB` (§8.3) | Target-adjacent | Modified from MI; recorded to preserve K-MI |

**Overall: mixed.** The target-adjacent components are LB-B's form and the record discount. The
single rule for target-informed components (§9.4) governs both: an H or S-mot class of LB-B's or the
discount's variation counts toward (a) only if E0 classes that component **independent** (for LB-B,
also textually verified and uniquely selecting). Otherwise every positive is (b). A component classed
mixed does not support (a).

### 6.3 Literature

Each item below was either checked in this unit or is marked as not checked. #1186 records that
earlier Landauer/Bennett attributions in the corpus "were not textual literature reads … they do not
source this lead" (LEAD:29). The same standard applies here: an unread item supports nothing until
E0 verifies it.

| Reference | Checked here | Used for |
| --- | --- | --- |
| C. H. Bennett, *Notes on Landauer's principle, reversible computation, and Maxwell's demon*, Stud. Hist. Phil. Mod. Phys. 34, 501 (2003), arXiv:physics/0210005 | Abstract read | Item 1, first quotation; item 2, quotation. It does **not** support item 4's mapping |
| R. Landauer, *Irreversibility and heat generation in the computing process*, IBM J. Res. Dev. 5, 183 (1961) | Not read here | Item 4 [pending E0] |
| C. H. Bennett, *Logical reversibility of computation*, IBM J. Res. Dev. 17, 525 (1973) | Not read here | Item 1 [pending E0] |
| C. H. Bennett, *The thermodynamics of computation — a review*, Int. J. Theor. Phys. 21, 905 (1982) | Not read here | Item 1 [pending E0] (measurement as copying into a standard memory) |
| T. Sagawa, M. Ueda, *Minimal energy cost for thermodynamic information processing: measurement and information erasure*, PRL 102, 250602 (2009), arXiv:0809.4098 | Abstract read | C-10 |
| A. Bérut et al., Nature 483, 187 (2012) | Through LEAD §1–§2 only | C-2 |
| H. A. Kramers, Physica 7, 284 (1940) | Not read here | C-2 (rejected; nothing depends on it) |
| P. Gács, *Reliable cellular automata with self-organization*, J. Stat. Phys. 103, 45 (2001), arXiv:math/0003117 | Abstract read | C-5 |
| A. L. Toom, *Stable and attractive trajectories in multicomponent systems* (1980) | Not read here | C-5 (rejected; nothing depends on it) |
| W. H. Zurek, *Quantum Darwinism*, Nature Phys. 5, 181 (2009), arXiv:0903.5082; H. Ollivier, D. Poulin, W. H. Zurek, PRL 93, 220401 (2004), arXiv:quant-ph/0307229; R. Horodecki, J. K. Korbicz, P. Horodecki, PRA 91, 032122 (2015), arXiv:1312.6588 | Abstracts read | C-3 (rejection) |
| R. W. Spekkens, PRA 75, 032110 (2007), arXiv:quant-ph/0401052; arXiv:1409.5041; S. D. Bartlett, T. Rudolph, R. W. Spekkens, PRA 86, 012103 (2012), arXiv:1111.5057 | Abstracts read (title only for 1111.5057) | C-7 (rejection); comparator |
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

### 8.1 Common terms

- **Ticks.** The configuration at tick `t` is the configuration after the `t`-th application of the
  rule. A registration made between ticks `t` and `t + 1` reads the configuration at `t`, and its
  value enters `K_t`. The LB-Z permutation it triggers is executed in the same interval, after the
  registration. Determination and bias "at `t`" are evaluated on the configuration at `t` after
  every LB-Z permutation of that interval, given `K_t`. The next application of the rule produces
  the configuration at `t + 1`. This is MI-A3's convention (a registration at tick `t` enters the
  knowledge at `t`). Decoupled cells (`Res`, `Ex`, `Arc`) take free ticks `(u, v) ↦ (v, u)`.
- **Branches.** A record branch is a record history of positive probability under the stated run.
  Determination and bias are judged branch by branch, on the entire joint record of a single run,
  before any averaging (MI-D §1.2).
- **World variables `W`.** The initial (`t = 0`) slot values of every cell of `C` and of the
  background, including every cell that LB-Z later displaces to `Ex`. Blanks' unknown slots, and the
  fresh source cells of `ref(π)`, are apparatus variables and not in `W`.
- **Determined, biased (functions of `W`).** A function `g` of `W` is determined in a branch if it
  is constant on the support of the conditional law of `W` given that branch's knowledge. It is
  biased in a branch if its conditional law given that knowledge differs from its prior law.
- **Linear functionals, `ω`, `Q*`.** As in MI-D §1.2: `f = Σ_i (a_i u_i + b_i v_i)` over a finite
  set of cells, `Q*(f) = Σ_i a_i b_i`, `ω(f, f′) = Σ_i (a_i b′_i + b_i a′_i)`. Here the cells range
  over the ring, `Ex` and `Res` together (the space `V_t`). `f` is determined in a branch if it is
  constant on the support of the conditional law of the configuration given that branch's
  knowledge, and biased if that conditional law is not uniform on `F_2`. In the linear rules every
  step, every free tick and every LB-Z permutation is linear and symplectic for `ω` and preserves
  `Q*`. A functional at `t_e` is therefore transported to a unique functional at any `t > t_e`.

### 8.2 LK-R, the leakage increment (primary, target-free)

**The reference `ref(π)`.** It uses the same strategy `π`: the same fixed data and the same map from
record histories to registrations. It differs from `π` only in the cell placed at `s(r)` at each
LB-Z event:

| Step at an LB-Z event at `r` | `π` | `ref(π)` |
| --- | --- | --- |
| Blank from `Res` | to `r` | to `r` |
| Former occupant of `s(r)` | to `Ex` | to `Ex` |
| Placed at `s(r)` | the spent register | a fresh source cell (both slots uniform, independent of everything) |
| Spent register | on the ring at `s(r)` | to `Arc`, a decoupled, never-read store |

`ref(π)` is therefore AP1/MI's P1 configuration (registered cells go to a decoupled store that
nothing reads), plus fresh-source-cell injections at the sink sites. P1 itself has no sink site and
makes no injection. The injections are added so that the two runs differ only in what is placed at
`s(r)`: both runs displace the same former occupant to `Ex`, and both inject a cell there. C-OFF-2
requires Stage 1B to extend the linear-limit lemmas to these injections.

**The comparison.** For a run `X ∈ {π, ref(π)}` and a record history `h` at tick `t` of positive
probability under `X`, let `Det_X(h)` be the set of functions of `W` determined given `h` under `X`,
and `Bias_X(h)` the set biased given `h` under `X`. LK-R holds iff both of the following hold for
every strategy `π ∈ Π_LB` and every `t ≤ T`.

- **(i) Matched histories.** For every history `h` of positive probability under both runs:
  - `Det_π(h) ⊆ Det_ref(h)`;
  - `Bias_π(h) ⊆ Bias_ref(h)`.

  The strategy is the same, so the two runs take the same actions on `h`.
- **(ii) Sink-only histories.** For every history `h` of positive probability under `π` and
  probability 0 under `ref(π)`:
  - let `h_0` be the longest prefix of `h` of positive probability under `ref(π)`;
  - let `H_ref(h)` be the set of `ref(π)` histories at tick `t` that extend `h_0` and have positive
    probability.

  Then:
  - every function of `W` determined given `h` under `π` is determined given some `h′ ∈ H_ref(h)`
    under `ref(π)`;
  - every function of `W` biased given `h` under `π` is biased given some `h′ ∈ H_ref(h)`.

A violation of (i) or (ii) is unintended leakage: information about the world reaching the observer
through export and the sink's return, beyond what the same strategy gives with ideal terminality.
Both runs quantify over the same variables `W`.

**Diagnostic LK-R-U** (decides nothing): the union-over-branches containment of r2, that is
`∪_h Det_π(h) ⊆ ∪_h Det_ref(h)` and the same for bias, at each `t`.

### 8.3 PROT-D_LB, PROT-B_LB, PROT-R′_LB (modified from MI; target-adjacent; recorded)

**Domain.** The domain is M-INACC's own active domain: every cell on the ring at `t`, exported
registers included (MI-D §1.2, "a cell that is on the ring and not archived … Hidden cells are
active").

**Definitional fact used to fix the discount (E-SHARP).** It follows from the definitions alone and
is not a derived result:

- A blank at `r` in the configuration at `t_0` has `u(t_0) = 0` known.
- Under every second-order rule `v(t_0 + 1) = u(t_0)`, so `v(t_0 + 1) = 0` is known.
- Its `u` slot is registered between ticks `t_0 + 1` and `t_0 + 2`, so the value enters
  `K_{t_0 + 1}` (§8.1). The cell is then fully determined at `t_0 + 1`. After LB-Z in the same
  interval it is on the ring at `s(r)`.

On the undiscounted ring, MI's PROT-D therefore fails for every rule through this strategy. This is
the A3-type case: the record's own content is sharp (MI-A3 §1, where the cell was archived). Because
E-SHARP strategies are admissible, A3-type determinations occur in every linear-rule evaluation.
This is a standing fact, not an annotation.

**The discount (linear rules `N_1`, `N_0` only).** Fixed in formulas. It removes, as a summand, only
content of exported cells that was already determined at export.

1. **Export content.** At each export event `e`, at tick `t_e`, in a given branch, let
   `Disc_e = span{u_e, v_e} ∩ Det(t_e)` in that branch. This is the exported cell's own content
   that is determined at export, in the configuration at `t_e` after LB-Z. It is either `0`,
   `span{u_e}` (registered slot only), or `span{u_e, v_e}` (sharp, as in E-SHARP).
2. **Transport.** `Disc_e(t)` is its transport to tick `t`, as functionals on `V_t` (the ring, `Ex`
   and `Res`). Later LB-Z events may move part of it into `Ex`.
3. **Sum.** `Disc_t = Σ_e Disc_e(t)` over the exports before `t`, in that branch. Distinct exports
   lie on distinct cells at export, and transport preserves `ω`, so `ω(Disc_e(t), Disc_{e′}(t)) = 0`
   for `e ≠ e′`.
4. **Split.** Let `I_t = Disc_t ∩ Disc_t^⊥` (the isotropic radical; for example a registered `u_e`
   whose partner was unknown at export). Let `N_t` be any complement of `I_t` in `Disc_t`. `ω` is
   nondegenerate on `N_t`, so `V_t = N_t ⊕ N_t^⊥`. Let `p_N` be the projection onto `N_t^⊥` along
   `N_t`.
5. **Action on ring functionals.** For a linear functional `f` on the ring at `t`, its
   record-discounted part is `p_N(f) = f − d`, with `d` the unique element of `N_t` such that
   `f − d ∈ N_t^⊥`. Since `N_t ⊆ Det`, `f` and `p_N(f)` are determined (respectively biased)
   together.
6. **The isotropic part is not discounted.** `I_t ⊆ N_t^⊥` for every `N_t`, so content in `I_t`
   stays in `p_N(f)`. A determined functional that pairs with a registered `u_e ∈ I_t` (`ω = 1`, the
   AP1 C9 sharpening) therefore stays a violation.
7. **No dependence on a choice.** The properties below quantify over **every** complement `N_t`,
   so no choice of complement can hide a violation.

**Properties.**

- **PROT-D_LB.** For every strategy, tick, branch and complement `N_t`: no determined linear
  functional `f` on the ring has `Q*(p_N(f)) = 1`.
- **PROT-B_LB.** For the same quantifiers: no biased linear functional `f` on the ring has
  `Q*(p_N(f)) = 1`.
- **PROT-R′_LB.** MI-A3 §4's PROT-R′, read on the ring. For `t ≤ t′` and a linear functional `f` on
  the ring at `t` whose value equals that of a linear functional `f′` on the ring at `t′`: if
  `Q*(p_{N_{t′}}(f′)) = 1` for some complement `N_{t′}`, then `f(t)` is neither determined nor
  biased given `K_{t′}`.

**Decisive rule.** An exhibited violation of any of the three gives NEG (§9.3).

**C-DISC** (§10) checks this discount on paper at E1, before any verdict, as part of CC-ACCEPT and
CC-REJECT. If the discount fails any case, the outcome is LIMIT (§9.3): the limitation is reported,
evaluation stops, and the discount is not tuned to pass (§9.7).

**`G_σ`.** The discount is inapplicable, because transport is nonlinear. Under `G_σ`, PROT-*_LB are
reported as diagnostics on the undiscounted ring and on `D_t` (the A-dom variants, §11.2), for PR-3
only. `G_σ`'s label is computed from the decisive set `{LK-R}` (§9.3).

### 8.4 USE-S, sink use (reach; comparative)

USE-S holds iff there exist all of the following:

- a strategy `π ∈ Π_LB`;
- an export event `e` at tick `t_e`;
- a later registration at tick `t > t_e`;
- a function `g` of the initial variables (world and apparatus) that equals a function of the
  exported cell's two slots at `t_e` under `π`;

such that:

- (i) `g` is not determined given `K_{t_e}` in that branch; and
- (ii) there is a record history `h`, up to just before the registration at `t`, of positive
  probability under both `π` and `ref(π)`, and a value of `g` of positive probability given `h`
  under both runs, for which the conditional law of the value registered at `t`, given `h` and `g`,
  differs between `π` and `ref(π)`.

`g` is the same function of the initial variables in both runs. Under `ref(π)` the cell carrying
that content is in `Arc`, so a difference in (ii) is a difference made by what LB-Z places at
`s(r)`. A dependence on `g` through common causes (world variables that feed both the exported cell
and the later record) appears in both runs alike, and does not satisfy (ii).

### 8.5 NV, non-vacuity (conjunctive)

NV holds iff some `π ∈ Π_LB` contains all of the following:

- an LB-Z reset at a register site `r`;
- followed by a later registration at the same `r`;
- whose value, in some branch, is not conditionally independent of the initial configuration of `C`
  given the knowledge just before that registration.

**Diagnostic NV-D** (decides nothing). Two separate facts are reported:

- some protocol has a record that is not independent of `C`;
- some protocol re-registers a site after a reset.

### 8.6 Justification of the two definitions (recorded before any result)

These justifications are recorded in this commit, before any property of `Π_LB` is evaluated. None
of them refers to whether P-OBS-LB passes or fails, and none uses a clause specific to LB (the blank
law, `d_S`, the side, the rule).

**J-LK, the leak test LK-R.**

1. *What "leakage through a mechanism" means.* Information is acquired through a mechanism if the
   observer would not have it had that mechanism's distinctive element been absent, with everything
   else held fixed. This is the counterfactual-difference reading of "acquired through a channel":
   cut one path, keep the rest, compare what is known.
2. *Why `ref(π)` is the right counterfactual.* The distinctive element of an export-type reset is
   that the spent record re-enters the dynamics. `ref(π)` replaces exactly that element by the
   ideal it is meant to replace (P1's decoupled store, the corpus's existing standard for retention
   without leakage, AP1:292–296, :533–560). The re-entering cell is replaced by an independent
   maximal-entropy cell, which carries no information. Everything else is kept equal: the strategy,
   the blank supply and the displacement of the former occupant.
3. *Why world variables.* "Unintended information" is information about the world the observer did
   not register. Measuring knowledge as functions of the initial world variables `W` gives one fixed
   set of questions for both runs. It does not presuppose any protected class or any structure of
   the cells.
4. *Why both matched and sink-only histories.* Matched histories compare like with like, which an
   adaptive strategy needs (the same record history gives the same actions). Sink-only histories
   exist only because of the mechanism. They are compared against what the reference could know
   after the last point the two runs share.
5. *Scope, stated in advance.* The test is general. It applies unchanged to any reset variant
   (C-OFF-1, A-Z's variants) and to any rule, `G_σ` included. It detects only the increment over
   ideal terminality. Leakage already present under ideal terminality is the job of PROT-*_LB and
   of AP1/QA's existing results.

**J-DISC, the record discount.**

1. *A record's own content is intended information.* A registration exists to make the observer know
   the registered value. At the moment of export the exported cell is the physical record. Knowledge
   of its content determined at that moment is what the observer acquired by registering, and is not
   leakage of anything else.
2. *Consistency with the corpus's existing treatment.* MI-A3's PROT-R′ leaves information held only
   by an archived cell outside protection from the moment of archiving (MI-A3 §4). The discount
   treats the exported cell's content at the moment of export in the same way. The exported cell
   differs from an archived one only after export, and everything acquired after export stays
   protected.
3. *Minimality.*
   - The discount removes only content determined at export, and removes it as a summand, not by
     membership, so that combining a record with other legitimate knowledge is not a violation
     (C-DISC case 1).
   - It removes only the nondegenerate part. A registered slot whose partner was unknown at export is
     kept, so that AP1's existing criterion of leakage, sharpening by pairing with a retained record
     (C9, AP1:682), stays a violation (C-DISC case 3).
4. *Generality.* It is stated for any export mechanism and any linear rule. It applies unchanged to
   C-OFF-1 and to `ref(π)`, where it is empty.

**Origin, disclosed.** The r3 form of the discount was written after the re-review of `40f42bd9`
gave a counterexample to r2's form (§11.5). Reasons J-DISC 1–4 are what makes the form meaningful.
The counterexample showed only that r2's form failed reason 3. Whether the r3 form makes P-OBS-LB
pass is unknown to the writer.

***

## 9. Decision rule

### 9.1 E0, the entry review (fixed)

**Who and when.** E0 is a recorded step by a reviewer who wrote neither this file nor any Stage 1B
record. It is completed and recorded before any Stage 1B derivation commit. The status "proposed"
is recorded only after E0 (§9.5). This file's Stage 1A review is not E0.

**What E0 does.**

1. It verifies in the text every **[pending E0]** item of §6.1 and §6.3, or strikes it.
2. It classifies every clause of §6.2 under the standard there, with C3 search records for any
   "none found". This includes LB-Z, through its ordinary classification and exits.
3. It classifies P2's recorded reason, "closure plus the E-AR obstruction … a programme-internal
   reason" (AP1:347–349), under the same standard.
4. It runs C-CAL and TT-1 to TT-4 (§10).
5. It answers in writing whether item 4, without AP1/P2 in view, selects LB-B's law (`u = 0` known,
   `v` uniform) uniquely among the variants of A-B × A-Bslot × A-Bval (§11.2). It names every
   variant that item 4, or the second reading in item 4, admits equally.
6. It runs the extensional check of §6.2 on LB-B against MI §4's blocking premises, TT-1 to TT-4,
   and "P2 restricted to `u`-known value 0".
   - Within `Π_LB`, LB-B equals the last of these, because LB-B is exactly the supply P2 permits
     there.
   - LB-B's independent reason as applied to LB-B (item 4's mapping onto the `(u, v)` cell) was
     first recorded at `7878a7fd`, after AP1 recorded P2.
   - The exemption of §6.2 therefore does not apply. LB-B takes the more target-ward of its own
     class and the class of P2's recorded reason.
7. It classifies the record discount (§6.2).

**Exits.**

| E0 finding | Consequence |
| --- | --- |
| C-CAL fails, or any of TT-1 to TT-4 is classed independent or mixed | The classification is defective. E0 is void and is repeated once by a different reviewer, with the failing item recorded. If the second E0 is also defective, the outcome is **VOID** until a documented amendment repairs the standard |
| Any of LB-W, LB-Z, LB-F, LB-S classed target-defined, or "none found" with its C3 record | **C-0** (null). Evaluation stops |
| LB-B classed target-defined, on its own or through the extensional check (P2's recorded reason classed target-defined, no exemption) | **C-0** |
| LB-B classed target-adjacent, on its own or through the extensional check, or its independent component "none found" (item 4 struck and no other source) | LB-B is carried as target-adjacent. Every positive is (b) (§9.4) |
| The record discount classed target-defined | PROT-*_LB become diagnostics. The decisive set is `{LK-R}` (§9.3), and every positive is (b) |
| Otherwise | Proceed to E1 |

### 9.2 Order of evaluation (fixed; never reversed)

Each step runs per rule (`N_1`, `N_0`, `G_σ`). The verdict for `N_1` is the construction's verdict.
The others are controls.

- **E0.** §9.1.
- **E1, controls before any verdict.** First CC-ACCEPT and CC-REJECT for every decisive test, with
  C-DISC (§10). These are evaluated before any property of `Π_LB` itself. Then C-IMPORT, C-OFF-1 to
  C-OFF-4, C-NC and PR-1 to PR-11 (§10, §11.1). A red required control voids every verdict that
  relies on it.
- **E2, NV.**
- **E3, LK-R.** A proof, or an exhibited violation of (i) or (ii).
- **E4, PROT-D_LB, PROT-B_LB, PROT-R′_LB** (linear rules, unless E0 made them diagnostics). A proof,
  or an exhibited violation. Diagnostics are reported.
- **E5, USE-S.** A proof, or a proof of its negation.
- **E6, variation analysis** (§11.2), for every assumption.
- **E7, labels.** Outcome (§9.3), owner distinction (§9.4), ladder rung (§11.4) and statuses (§9.5).
- **E8, comparison with the completion conditions.** Only after E7, and only as a record (§9.6).

**Standard of proof.** As in MI-D §4.4: paper derivation.

- A violation is exhibited by an explicit strategy on a stated instance.
- A holding property needs a proof over all of `Π_LB` for that rule.
- Any instance check by enumeration or program requires that Stage 1B's authorization permits it.
  This file authorizes none.

### 9.3 Outcomes (per rule; total and ordered)

**The decisive set `P`.** For `N_1` and `N_0`: `{LK-R, PROT-D_LB, PROT-B_LB, PROT-R′_LB}`. For
`G_σ`, and for every rule after the E0 exit "discount target-defined": `{LK-R}`, with PROT-*
reported as diagnostics.

The rule-level label is the **first** row whose condition holds, in this order.

| Order | Outcome | Condition |
| --- | --- | --- |
| 1 | **C-0** | An E0 exit to null (§9.1) |
| 2 | **LIMIT** | A decisive test of `P` fails CC-ACCEPT or CC-REJECT. The limitation is reported and evaluation stops for that rule. No definition is repaired within this preregistration (§9.7) |
| 3 | **VOID** | Another required control is red, or the second E0 is defective (§9.1) |
| 4 | **VAC** | NV fails (proved) |
| 5 | **NEG** | An exhibited strategy in `Π_LB` violates a member of `P` |
| 6 | **INC** | No violation is exhibited, and NV, a member of `P` or USE-S is undecided within Stage 1B's scope |
| 7 | **PART-SPLIT** | Every member of `P` is proved and USE-S is decided, but E6 classes some assumption S-sel (§11.2) |
| 8 | **PART-INERT** | Every member of `P` is proved, USE-S fails, and no assumption is S-sel |
| 9 | **POS** | Every member of `P` is proved, USE-S holds, and no assumption is S-sel |
| 10 | **INC** | No row above applies. The reason is stated |

**Annotations** (reported with the label; they never replace it):

- **+EXTRA.** When the label is NEG or INC and a premise, reported and not adopted, would make the
  failing or undecided members provable. The premise is classed under §6.2, with CC-RECON if its
  only role is to block an exposure.
- **+LEAK.** When the label is VAC or LIMIT and a violation of a member of `P` was nevertheless
  exhibited. The violation is reported in full.
- **+POOR.** When E6 classes every assumption E (§11.2).

No row is decided by the definitions alone, provided CC-ACCEPT, CC-REJECT and C-DISC are green.
C-DISC's first case is the case that would otherwise decide NEG in advance (§10).

### 9.4 Owner distinctions (a), (b), (c)

**"Load-bearing".** An assumption is load-bearing iff its §11.2 class is H, S-mot or S-sel, i.e. not
E.

**Known now.** A-B and A-Bslot are load-bearing before Stage 1B, for definitional reasons:

- a supplied cell with a known `Q* = 1` functional has that functional determined on the ring at
  injection;
- that cell comes from `Res` and carries no exported content, so the discount does not touch it;
- this covers the variants "both slots known" and "`u + v` known";
- hence PROT-D_LB fails on them (C-OFF-3; MI §6.1 C-P2, "under any rule").

Their variation test is therefore decided by E0's reading of item 4, not by a Stage 1B derivation.

**The single rule for target-informed components.** It governs LB-B and the record discount, and is
stated identically in §6.2, this section, §11.4 and §15.

- **LB-B.** An H or S-mot class of A-B, A-Bslot or A-Bval counts toward (a) and toward L2 only if
  both of the following hold:
  - E0 classes LB-B **independent**, after the extensional check, with item 4's source verified in
    the text;
  - E0 finds that item 4 selects LB-B's law uniquely, or that every variant it admits equally gives
    the same §9.3 label.
- **The record discount.** An H or S-mot class of A-dom counts toward (a) only if E0 classes the
  discount **independent** (for example, as the definition of "unintended" fixed by the question
  itself) and C-DISC is green.
- **Otherwise.** If either condition fails, every positive is (b), and L2 needs its two credits from
  A-Z, A-F and A-S. A component classed mixed does not support (a).

- **(a) Independently predicted positive.** All of the following:
  - POS for `N_1` with the configuration fixed in §4;
  - no S-sel;
  - the single rule above satisfied for both LB-B and the discount;
  - E0 passed;
  - R-1 to R-4 complete (§10).
- **(b) Positive only after selection.** Any POS, PART-INERT or PART-SPLIT that is not (a). That
  includes a positive that needs:
  - a variant other than §4's fixed values;
  - LB-B or the discount without the single rule satisfied;
  - a premise reported under +EXTRA;
  - the portfolio coordinator's choice of P-OBS among the three constructions because the others
    failed.

  The selection among C-0 to C-13 in §3 was made before any evaluation and is disclosed (§11.5). If
  E0 finds that the selection used knowledge of consequences, it is also recorded under (b).
- **(c) Classical imitation.**
  - P-OBS-LB is itself a classical stochastic model on configurations. Its configuration-level
    record laws are therefore classically imitated by the exhibited model. This does not rest on
    Theorem NC.
  - Wherever E8 finds statistics that match a quantum subtheory, the result is recorded under (c).
  - For an *encoded* statistic, E8 also records whether the imitation is noncontextual. That holds
    only under NC's injective identification, H-LIFT and spanning-read hypotheses. Otherwise the
    imitation is only an ontological model, which always exists and on its own gives no
    information.
  - A P-OBS positive is evidence about an access mechanism, never evidence for quantum selection.

### 9.5 Three statuses (recorded separately)

- **Proposed.** Recorded only after E0. "Proposed" iff E0 gives no exit to C-0. The status line names
  every target-adjacent component that E0 records, at least LB-B's form and the record discount
  where they are classed mixed or target-adjacent. Otherwise "not proposed" (C-0).
- **Mathematically sufficient.** After Stage 1B: "sufficient for {properties} under {hypotheses}" iff
  POS or PART-INERT is proved for `N_1`, listing every hypothesis of §7 used. Otherwise "not
  established", with the outcome label.
- **Derived from native OI.** "Not derived" unless all of BLANK-SRC, SWAP-EXEC, RECORD-STORE,
  EXHAUST and TIMING are sourced, without exception for any input a proof is said not to use. Each
  source must be an established claim on `main` under §A.46 item 1. P-OBS's reviewer checks each
  under §A.46 item 7 before the status changes. Presence on `main`, or a citation, is not enough.

### 9.6 Comparison stage (record only)

After E7, Stage 1B records, without changing any label:

- whether the access model of `Π_LB` bears on condition (iv);
- whether class-N outcomes coincide with toy-theory statistics, which goes under (c) with the NC
  scope note of §9.4;
- for every encoded statement, its scope with respect to U2 (PR-1).

No criterion above refers to the target except to record an outcome (C-IMPORT).

### 9.7 No adjustment to obtain a positive (owner decision, item 3)

- No definition, control, variant set or clause of this file changes after r3, except by a
  documented amendment that is independently reviewed before any property of `Π_LB` is evaluated.
- An amendment states its reason. A reason that refers to an outcome, or whose only stated effect is
  to change an outcome, is rejected (CC-RECON).
- After LIMIT, or after any property of `Π_LB` has been evaluated, a change is a new preregistration.
  It cites this one, and it is classed under §6.2 with this file's results known.

***


## 10. Controls and countercontrols

| ID | Kind | Fixed pass criterion |
| --- | --- | --- |
| C-OFF-1 | Mechanism off: LB-Z | Replace export by in-place reuse: the spent register stays at `r` and is treated as the next blank, with no swap. Report LK-R and PROT-*_LB. If the outcome equals the mechanism-on outcome, the mechanism is idle and no positive is attributed to LB-Z |
| C-OFF-2 | Mechanism off: interacting sink | Under `ref(π)` in `N_1` and `N_0`, Stage 1B proves PROT-D_LB and PROT-B_LB in its own record. It may cite QA Lemma Q(iii) and AP1 Lemma 3 (on main) and must extend them to `ref`'s injections; MI §6.3's extension is off main and is a cross-check only. Failure is red |
| C-OFF-3 | Mechanism off: LB-B | Fully known blanks. By definition PROT-D_LB fails on the supplied cell itself (§9.4). Not failing is red: a definitional sanity check |
| C-OFF-4 | Mechanism off: LB-F | Blank values chosen per step from records (MI's refills). Reported. Its relation to MI is handled as in PR-3 |
| C-NC | Classical imitation | State the exhibited configuration model as an exact classical imitation of every `Π_LB` record law. State where NC's hypotheses hold or fail (at `q = 2` with native `Z`/`X` reads, NC does not apply; M2D:65–71). Claim no nonclassicality. Label (c) as in §9.4 |
| C-IMPORT | Target import | (i) No §4–§8 definition contains a quantum quantity, other than `Q*` in the target-adjacent PROT-*_LB. (ii) PROT-*_LB are recorded, not motivating. (iii) No clause is added to `Π_LB` after Stage 1B begins. (iv) Any blocking premise is reported, not adopted, with CC-RECON. (v) Every verdict is generated from §9 |
| C-DISC | Definitional control of the discount, checked on paper at E1 | Under `N_1` and `N_0`, three cases, each decidable from §8.3's definitions. **Case 1 (must not be a violation):** the E-SHARP strategy with `d = u_s + v_s` of the exported cell (`Q*(d) = 1`, `Disc_e = span{u_s, v_s}`), and `b` the known `u = 0` slot of the fresh blank placed at `r` (`Q*(b) = 0`, `ω(d, b) = 0`, `b ∉ Disc_t`). The functional `f = d + b` is determined and has `Q*(f) = 1`. Its discounted part `p_N(f)` must have `Q* = 0`. **Case 2 (must be a violation):** a planted determined `c` on the ring with `Q*(c) = 1` and `ω(c, Disc_t) = 0`. **Case 3 (must be a violation):** a planted determined `c` with `ω(c, u_e) = 1` against a registered `u_e ∈ I_t` whose partner was unknown at export (the AP1 C9 sharpening). Failing any case gives LIMIT (§9.3). The discount is not tuned to pass (§9.7) |
| CC-ACCEPT | Decisive countercontrol (owner decision, item 1): an ordinary exported record is correctly accepted | Evaluated against adaptive strategies and complete accessible histories: every branch, judged on the whole `K_t` (all records, the strategy, the blank law and every supplied known value), with no averaging and no discarding. **For PROT-*_LB** (linear rules): the E-SHARP export, embedded in an adaptive strategy whose later registrations depend on that record, with blanks continuing to be supplied. No branch may show a violation whose discounted part comes only from that record's content combined with supplied known slots (C-DISC case 1, extended to every later tick and every branch). **For LK-R:** the same adaptive strategy with `s(r)` chosen so that, by Main's coupling-graph cone (Main:364), no exported content can reach any register site before `T`. LK-R must hold for it. Failing either is LIMIT (§9.3) |
| CC-REJECT | Decisive countercontrol (owner decision, item 1): a deliberately planted leak is correctly rejected | Planted operations used only in this control, outside `Π_LB`, each embedded in an adaptive strategy and judged on complete accessible histories as above. **PL-1 (direct):** a planted record of a `Q* = 1` functional of a cell of `C` that never passed through a register. PROT-D_LB must reject it. **PL-2 (sink return):** a planted coupling that, at a later tick, adds the exported cell's undetermined slot into a fresh blank, which is then registered. LK-R must reject it, by (i) or (ii); under `ref(π)` the same planted coupling reads the fresh cell at `s(r)`. **PL-4 (post-export pairing):** a planted record, after export, of the exported cell's slot that was undetermined at export. PROT-D_LB must reject it (C-DISC case 3). For each, Stage 1B states one instance at E1, before any property of `Π_LB` is evaluated, and does not revise it afterwards. Failing any is LIMIT (§9.3) |
| C-CAL | Positive calibration of the classifier, on an item external to P-OBS-LB | Q3-A1 §5.1's C-CAL item, verbatim: "A4's translation clause applied to the affine rule including its offset, 'F commutes with lattice translations'", with its source Substratum:98's anchor, "the homogeneity of physical law — no experiment has found a preferred location in the laws". Under §6.2's standard it must be classed independent. Otherwise the classification is defective (§9.1: one repetition, then VOID) |
| TT-1 | Target-tuned, must be rejected | "A blank is injected only where every gate that will act on it is fixed by `K` when it acts." Design reason: **to block E_A, E_A′ and E_B** (MI §4, P-GK) |
| TT-2 | Target-tuned, must be rejected | "Each blank's known slot is the slot that keeps the observer's knowledge isotropic." Design reason: **to keep the knowledge isotropic** |
| TT-3 | Target-tuned, must be rejected | "No exported register is placed within distance 2 of a cell of `C` with an unknown slot." Design reason: **to block E_A, E_A′ and E_B** (MI §4, P-NR analogue) |
| TT-4 | Disguised, must be rejected | "After `t = 0`, no blank is injected at a site within distance 2 of a ring cell with an unknown slot. A memory reset in thermal contact with a hot neighbour does not reach its standard state, so a standard reset requires thermal isolation." The stated reason sounds independent. Within `Π_LB` its extension equals that of MI's P-NR (MI §4, row 2: no refill within distance 2 of an active cell with an unknown slot), whose role is to block exposures. It was written after P-NR was known |
| TT pass criterion | Decisive | TT-1 to TT-4 are each classed target-defined, or target-adjacent with the reason identified. TT-4 must be caught by the extensional check of §6.2. Any TT classed independent or mixed: E0 is void and is repeated once; a second defective E0 gives VOID (§9.1) |
| PR-1 … PR-11 | Preserved results (§11.1) | As stated there |
| DG-FULL | Diagnostic | PROT-D on the undiscounted ring, and on `D_t` (§11.2), reported. Decides nothing; the decisive form is PROT-D_LB |
| Diagnostics | Reported | LK-R-U (§8.2), NV-D (§8.5), and for `G_σ` the PROT-* diagnostics (§8.3) |
| R-1 | Robustness | Independent re-derivation of every holding property, from this file and the Stage 1B record alone, by a reviewer who did not author Stage 1B |
| R-2 | Robustness | Both linear limits `N_1` and `N_0`; every `L` admitted by H-NW for the stated `T` (proof, not instance) |
| R-3 | Robustness | Variation analysis E6 complete, with every assumption classified |
| R-4 | Replication | Before promotion, a separately authorized check of each holding property on stated instances (an authorization question for the owner; none is granted here) |

A positive is not promoted, and does not count toward any physical selection principle, before
R-1 to R-4 are complete (c.6720450946).

***

## 11. Explanatory quality (AGENTS.md §A.29)

### 11.1 Preserved results (they become controls)

| ID | Result | Source | Control |
| --- | --- | --- | --- |
| PR-1 | Theorem U2 within its hypotheses (K-FIN) | M2D:48–64, :404–413 | Stage 1B first states whether `Π_LB`'s operations lie in Lemma F's operation set and satisfy H-LIFT, including for exported cells correlated with the carrier. If they do, an encoded branch acting as `p · Ad U` (input-independent `p > 0`) with `Ad U` outside `A_4 ≀ S_n` is red. If they do not, U2 is recorded as not applicable and any encoded operation found is reported with that scope. Non-unitary encoded maps never trigger PR-1 |
| PR-2 | Theorem NC within its hypotheses | M2D:483 | C-NC |
| PR-3 | M-INACC: exposures E_A, E_A′, E_B under `G_σ` in `Π_A`/`Π_B`; P-GK degenerate; PROT-R fails in the linear limits; PROT-R′ holds there | MI §0, §3, §4, §6.3; MI-A3 (provisional, off main, model-reviewed) | Under `G_σ`, Stage 1B states for each of E_A, E_A′, E_B whether it lies in `Π_LB`. If one is excluded, the excluding clause is named and passed to E6. An MI exposure is used as a control only after Stage 1B re-derives it in its own record. A contradiction between P-OBS and MI is recorded as a finding against one of the two records and adjudicated under §A.46 item 7. It does not turn a control red automatically, and verdicts that depend on the contested item are marked contested until it is adjudicated |
| PR-4 | AP1 Lemma 3 and controls C4, C9: terminality and half-known supply suffice for isotropy; without terminality a re-coupled registered meter lets a second read sharpen the partner (C9) | AP1:533–560, :677, :682 | C-OFF-2, C-OFF-3. Stage 1B states whether C9's protocol, or its dynamical analogue through a register site, lies in `Π_LB`. If excluded, it names the excluding clause (LB-W or LB-S) and passes it to E6 |
| PR-5 | QA Lemma Q (class N, under P1 and P2) | QA:458–479 | C-OFF-2 |
| PR-6 | Main (C1)–(C4) as diagnostics: (C2-structural) holds by reversibility in every bijective realization; (C3) capacity bound; (C4) readback | Main:74–80, :604, :614 | Any statement about the cycle's visible law must be consistent with them. USE-S is checked against (C4)'s operational form |
| PR-7 | TN and LEAD scoped retention obstructions (PAD, NP, AE, SS-2); "not a universal no-go" | TN §4, §6.2; LEAD §3 | P-OBS-LB claims no physical retention; RECORD-STORE stays supplied |
| PR-8 | S-L6: finite `S` gives `φ^N = id`; irreversibility only relative to a budget below recurrence | MR★:595 | BUD |
| PR-9 | (iv) fails in the access model and the stated-intervention theory | S0 row 9 | No (iv) claim |
| PR-10 | No sourced quiet ready region | MR★:1342, :1353 | BLANK-SRC stays supplied |
| PR-11 | Complete passive observation holds exactly when the algebra is commutative | Main:592 | No complete passive-observation claim |

### 11.2 Variation analysis (decision rule only; nothing predicted)

**Claimed consequence.** The §9.3 label for `N_1`, together with the LK-R verdict.

**Rule.** For each assumption `a` with the variant set `V_a` fixed below, Stage 1B evaluates the
claimed consequence on every variant and classifies `a`:

- **H (hard to vary):** every variant destroys the consequence (changes the §9.3 label or the LK-R
  verdict).
- **E (easy to vary):** every variant preserves it.
- **S (split):** some variants preserve it and some destroy it. Then:
  - **S-mot:** every destroying variant is excluded by `a`'s own §6.1 motivation, as upheld at E0;
  - **S-sel:** some destroying variant is supported by that motivation as well as the chosen value.
    The construction's choice then selects the consequence: PART-SPLIT and (b).

**Overall reading.**

- If every assumption is E, the annotation +POOR ("poor explanation") is recorded, whatever the
  match to the question.
- If no assumption is H or S-mot, the rung is at most L1 (§11.4).
- For A-B, A-Bslot and A-Bval, and for A-dom, the classes H and S-mot count only under the single
  rule for target-informed components (§9.4).

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
| A-dom (protected domain and discount) | {full ring with the §8.3 discount (chosen); full ring without discount (MI's exact domain); `D_t`}. `D_t` is defined exactly: every ring site except a sink site `s(r)` from the tick of an export into it until the tick at which a later LB-Z displaces that occupant to `Ex`. For `G_σ` only the last two apply |
| A-dist | {`d_S` = 1; 3 (chosen); `≥ L/2`} |
| A-side | {away from `C` (chosen); toward `C`} |
| A-rule | {`N_1` (primary); `N_0`}. `G_σ` is reported separately and is not a variant of the construction |

Before any derivation it is recorded, by definition, that the variant "full ring without discount"
of A-dom changes the label by E-SHARP (§8.3), provided the chosen value is not itself NEG. This
statement is definitional. Its H or S-mot class counts only under the single rule of §9.4, so with
the discount classed mixed it does not support (a).

### 11.3 Reach

- **RCH-1, sink use (Main (C4); S0 rows 2 and 15; MI clause (a)).** The exported content must stay
  dynamically used, in the conditioned sense of USE-S (§8.4). Protection that holds only because
  undetermined exported content never affects later records is protection by inertness. USE-S can
  fail, and failure gives PART-INERT.
- **RCH-2, recombination (AP1 §4.5; #1169 c.6713156200).** Stage 1B states two things:
  - whether `Π_LB` in `N_1` reproduces AP1 §4.5's recombination result for an unregistered register
    (un-copying through the reciprocal coupling);
  - whether export makes a registered copy irreversible within BUD by every register-site operation.

  A contradiction with AP1 §4.5 is red.
- **No novel independently checkable consequence is identified.** RCH-1 and RCH-2 are
  internal-consistency tests on the consistency axis (§A.23). They can fail, so the cap "useful
  construction" does not apply. L3 has no candidate, and the highest reachable rung is L2.

### 11.4 Assessment ladder (recorded with (a)/(b)/(c))

- **L0.** The construction reproduces the target property: registration, retention and reuse
  without leakage (LK-R and PROT-*_LB hold).
- **L1.** It does so only through assumptions that are E or S-sel, or arbitrary (A-dist or A-side
  chosen without motivation and S-sel).
- **L2.** An independently motivated mechanism fixes several features, and it excludes the
  non-target alternatives.
  - At least two of A-Z, A-F, A-S, and (under the LB-B rule) A-B, are classed H or S-mot.
  - C-OFF-1 and C-OFF-4 destroy the property.
- **L3.** L2 plus a novel, independently checkable consequence. None is identified (§11.3).

Every outcome, negative ones included, is recorded at a rung or as "below L0".

### 11.5 Origin disclosure

- **Where the conjecture came from.**
  - The writer read AP1's P1 and P2, MI's archive-swap refills and #1032/#1186 (Bérut; the
    Landauer/Bennett remark at LEAD:29) before forming C-1.
  - The observation that MI's archive-swap refill has the form of a Landauer reset in a reversible
    dynamics came from reading MI §8, a target-oriented record.
  - The search therefore ran from posits introduced for a target-adjacent programme (AP1's Lemma 3,
    toward the quarter-phase test) back to thermodynamics.
- **What that implies.**
  - LB-Z and LB-B reproduce the structure of P1 (with one change, the interacting sink) and of P2
    (with value 0 only). The resemblance is a product of the search direction, not a discovery.
  - LB-B is the clause most exposed to retrofitting. A quiescent blank (`u = v = 0`) is an equally
    natural reset when AP1/P2 are not in view. The single rule of §9.4 makes LB-B count toward (a)
    or L2 only if E0 classes it independent, with a verified, selecting reading of item 4.
- **Knowledge of consequences at drafting.**
  - While fixing LB-B, the writer had read MI's protocols. E_A uses a supplied known value 1
    (MI §3.2), which LB-B's value 0 excludes. E_A′ uses `v`-known and `u`-known cells at `t = 0`
    (MI §3.3). Whether `Π_LB` contains E_A′ or any other exposing protocol is not known to the
    writer and is a Stage 1B check (PR-3).
  - In r1, the protected domain `D_t` was fixed with knowledge of MI-A3 §1's archived-cell
    countercase. In r2 the record discount `Disc_t` was fixed with knowledge of E-SHARP, which the
    independent review of `7878a7fd` pointed out (finding B1). In r3 the discount was restated as
    a summand projection after the re-review of `40f42bd9` showed that r2's membership test makes
    PROT-D_LB fail by definition (its finding R2-1). r3's form was chosen to meet the three C-DISC
    cases stated by that re-review, not to pass any derivation. Both domain choices are classed
    mixed, and both are varied under A-dom.
- **The independence requirement is unchanged.** This disclosure does not relax it (c.6719386464).

***

## 12. Commitment to report

Stage 1B, if authorized, reports for each rule:

- the §9.3 label and annotations, whatever they are;
- (a)/(b)/(c), the ladder rung and the variation class of every assumption;
- the three statuses of §9.5 and every E0 finding;
- every control with its status;
- CC-ACCEPT and CC-REJECT, with their instances, and LIMIT if it occurs;
- every diagnostic (LK-R-U, NV-D, DG-FULL);
- every premise found to block an exposure, reported and not adopted.

This covers positive, negative, vacuous, inconclusive, void and null outcomes. A negative for
`Π_LB` is a negative for this access model on these rules only (§16). No outcome is withheld or
re-run with changed clauses. A changed clause is a new preregistration or a documented amendment
(c.6720678942).

***

## 13. Invariant → checkpoint table (§A.41)

| Invariant asserted | Checkpoint that measures it |
| --- | --- |
| r3 changes only this `DESIGN.md`, in one commit whose single parent is `40f42bd9` | `git show --stat` of the r3 commit lists only this path; `git rev-parse <r3>^` is `40f42bd9…` |
| No result is derived here | Reviewer reading of §4–§11; `grep -n -i 'we find\|it follows that\|holds for every\|is protected\|leaks\|POS holds'` matches only this row |
| The only consequences stated before Stage 1B are definitional: E-SHARP and the A3 standing fact (§8.3), the C-DISC cases (§10), C-OFF-3 and "Known now" (§9.4), and the A-dom note (§11.2) | Reviewer reading. Each of those passages says "definitional", "by definition" or "decidable from the definitions", and uses only the second-order step `v′ = u`, a supplied known value, or the definitions of `ω`, `Q*` and the discount |
| The decision rule precedes any Stage 1B text | Stage 1B's first commit is a descendant of the r3 commit, and this file is byte-identical there (`git diff` empty for this path) |
| J-LK and J-DISC (§8.6) are recorded before any result | They are in the r3 commit, which precedes every Stage 1B commit (fourth row of this table) |
| CC-ACCEPT and CC-REJECT, with their stated instances, precede every evaluation of a property of `Π_LB` | Stage 1B's E1 record carries a commit time earlier than its first E2–E5 text |
| E0 precedes every Stage 1B derivation commit | E0's record carries a commit or comment time earlier than the first Stage 1B derivation commit |
| No `readWriteSourced_` identifier is cited | `grep -n readWriteSourced` on this file matches only K-LEAN (§2) and this row, which name the prohibition |
| No odd-`q` statement | `grep -n -i odd` matches only K-Q (§2), §16 and this row |
| §6.1 contains no quantum quantity | Grep of §6.1 for "quantum", "Born", "unitar", "complete positiv", "completion", "Q\*" returns nothing |
| Repository citations are to main `9c201475`, or to the stated off-main commits `f649b347` (MI) and `25384b13` (Q3) | Reviewer check of every `File:N`, and `git cat-file -e` on each full SHA |
| No file of the other two constructions is cited | `grep -n -i 'p-control\|p-mix'` matches only this row |
| M-INACC is cited as provisional and off main | §14 classifies MI as "support off main: gap"; PR-3 says "provisional, off main" |
| Every candidate considered has a decision and reason | §3 has one row per candidate C-0 to C-13 with a non-empty decision cell |
| The variation sets are fixed before evaluation | The §11.2 table is byte-identical at Stage 1B's first commit (fourth row of this table) |

***

## 14. §A.42 item 8 trace

| Reference | Used for | Class |
| --- | --- | --- |
| #1169 c.6720450946, c.6720342295, c.6719386464, c.6719192859, c.6720678942 | Authorization, scope, standard, tiers, workstreams, NC/U2 reading | Provenance |
| #1169 c.6713156200 (joint synthesis) | RCH-2 | Provenance |
| S0 (#1169 c.6719708521; review c.6719720616) | Rows 9 and 16; restated here with their on-main citations | Provenance. The restated row content rests on files on main (AP1, QA, Main, Sub), cited directly |
| #1198 head `f649b347` (MI, MI-D, MI-A3) | K-MI, PR-3, the definitions of §8, TT-1, TT-3, TT-4 | **Support off main: a gap.** MI is provisional (model-reviewed, unmerged). No established claim rests on it. Each use is either a preserved result, which Stage 1B re-derives before using it as a control (PR-3), or a definition restated here |
| #1202 head `25384b13` (Q3-A1 §3 Block C) | Classification standard | Provenance. The standard is restated in full in §6.2 |
| Independent review of `7878a7fd` and re-review of `40f42bd9` (relayed by the coordinator; not on main) | The r2 and r3 changes; the second reading in item 4; E-SHARP; the C-DISC cases | Provenance. E-SHARP and the C-DISC cases are restated here from the definitions |
| Q3-A1 §5.1 C-CAL item (at `25384b13`) | C-CAL | Provenance. The item is quoted verbatim in §10, with its on-main source Substratum:98 |
| #1032 body and c.6712887557, c.6713169247, c.6567189236 | K-1032; C-2; non-duplication | Provenance. The content used (LEAD) is on main |
| LEAD, TN | C-2, PR-7, RECORD-STORE | Support on main |
| #1188 | K-LEAN | Provenance |
| #1193 | K-Q | Provenance |
| #866, #1147 | SWAP-EXEC, BLANK-SRC ownership | Provenance (Issues) |
| arXiv abstracts and journal references of §6.3 | Motivation and rejections | External literature. "Read here" is marked per item; E0 verifies the rest |

***

## 15. Concerns for the coordinator and the reviewer

1. **Independence (main concern).** The search ran backward from target-adjacent posits (§11.5).
   LB-B coincides in form with P2 and with knowledge balance, and its independent component rests
   on an unread source. E0 decides it under the single rule for target-informed components (§9.4).
   Through the extensional check, LB-B's consequence follows E0's class of P2's recorded reason.
2. **The record discount.** The discount is fixed knowing E-SHARP and the re-review's
   counterexample. It is classed mixed and varied under A-dom. Under the single rule for
   target-informed components (§9.4), its variation counts toward (a) only if E0 classes it
   **independent**; otherwise every positive is (b). A component classed mixed does not support
   (a). C-DISC checks that it neither decides NEG by definition nor hides the C9 sharpening.
3. **Possible vacuity.** With value-0 blanks only and every non-register site unknown, the class may
   register nothing informative about `C` after a reset. NV is conjunctive, so that case gives VAC.
   It is recorded as a finding and not repaired by adding supplies.
4. **Supplied load.** Five named open inputs stay supplied. "Derived from native OI" requires all
   five to be sourced by established claims on `main` (§9.5). The most a positive can give is
   "mathematically sufficient under named supplied inputs".
5. **Overlap with #1032 and #866.** BLANK-SRC, RECORD-STORE and SWAP-EXEC fall in Codex's and #866's
   areas. P-OBS does not source them. If a source for any of them lands, P-OBS's reviewer checks it
   under §A.46 items 1 and 7 before any status changes.
6. **Countercontrols may stop the unit.** If the leak test or the discount fails CC-ACCEPT or
   CC-REJECT, the outcome is LIMIT: the limitation is reported and evaluation stops (§9.3, §9.7).
7. **Classical by construction.** Every configuration-level P-OBS outcome is classically imitated by
   the exhibited model (§9.4 (c)). Its value is to the access-model question of S0 row 9, not to
   quantum selection.

***

## 16. Not claimed

- Any result about `Π_LB`, beyond the definitional facts marked as such. Every property of §8 is
  open until Stage 1B.
- A physical source for blanks, swaps, record storage, exhaust or timing.
- Physical retention of any record (#1032).
- Any statement for rules other than `N_1`, `N_0` and `G_σ`; for access models other than `Π_LB`;
  or for odd `q`.
- Any statement about composites; P-OBS-LB is single-ring.
- Nonclassicality, contextuality, a quantum operation, condition (iv) or OI–QM equivalence.
- That a negative for `Π_LB` excludes every observer-level registration mechanism.
