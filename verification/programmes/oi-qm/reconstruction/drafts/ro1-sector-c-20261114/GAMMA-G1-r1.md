# GAMMA-1 unit G1; paper-only; definitions; unreviewed

**What this note does.** It fixes, for one fixed model, one measure `μ` and one access instance
under the accepted U1 criterion, the objects that (γ) at Main:682 is stated in: the six record laws
`L_a`, the correspondence map `κ` onto raw-direct double-slit observables (§A.24), the two directions
(γ→) and (γ←) (§A.34), and the controls. It derives no record law, evaluates no `L_a`, runs no
computation, simulation, enumeration or Lean, edits no manuscript, adopts no premise, extension or
sector condition, and changes no Issue. Each [P] is a proposed definition for review. Each [A-inf] is
an author-side consequence of definitions, by hand, and is not verification.

**Authorization.** Owner decision record #1169 c.6891808569 (`amaybaum`, 2026-11-15T08:39:13Z),
wave 1, item 3: "γ plan, unit G1 (definitions) starts now. Its classifications that depend on U4
stay provisional." Answers binding here (same record): "Q5: the ensemble and orbit-frequency
readings are both carried; neither is adopted"; "Q6: compatibility with classical waves alone does
not establish quantum coverage"; "Q7: γ is reported under each reading of P-vii, and C-1 and OB-b0
stay open under #1234". "No new premise, execution or merge is authorized." Physical source remains
NOT PASSED. Amended target, #1169 c.6891338304 (`amaybaum`, 2026-11-15T07:54:33Z): coverage of
perceived quantum phenomena and agreement with every performed experiment are required; C is
defined with no reference to quantum outcomes; the relation of C to Q is a finding.

**Issue.** #1305 (GAMMA-1). **Writer:** Claude. **Review:** a separate non-author reviewer
(pending); ChatGPT review optional.

**Inputs, at exact objects.**
- RO-1 drafts in `verification/programmes/oi-qm/reconstruction/drafts/ro1-sector-c-20261114/`,
  branch `research/ro1-sector-c-1169-20261114` (PR #1294) at
  `f86dd1f791774f68237c8b82ef810855f14dd6d8`. **Off `main`.**
  - `GAMMA-PLAN-r1.md`, blob `77f1fcd8d32403b26fb87c47cfd572bbf982febb` (cited PLAN-G:N); plan only,
    not reviewed (#1305 body);
  - `S3-U1-r5.md`, blob `68983f8666df0ca6c26ec4b9ec00d0a9e4072f67` (U1:N); accepted, #1169
    c.6891241282;
  - `S3-U2-r3.md`, blob `2711c168a65c0ae4397195593528fcf0ee6a4cba` (U2, by section); accepted with
    its recorded limits, #1169 c.6891710167;
  - `S3-U4-r1.md`, blob `e6d8101a2e8017c9b1d09a0909e66c1faae52df7` (U4:N), and its review
    `REVIEW-S3-U4-r1.md`, blob `63c95b30d66348e063ee7f89e7e457b3dd2506b9` (RU4, by finding);
    verdict REVISE, r2 not written. **Every classification below that rests on U4 is PROVISIONAL.**
  - `LIT-ERASER-r3.md`, blob `2b414173ce862d570aabb56e86c6b76344da0194` (LIT, by item);
    reviewed literature note.
  - `U4-CALC-r1.md`, blob `fb3d50f804becafd292a434be68867f86455f322`: unreviewed; **not used**. G2
    reuses it after its review (c.6891808569, wave 2).
- Corpus at `origin/main` `75cc51009aebcfb17c1bbf76d149760c540aac3b`, read with `git show`:
  - `papers/Main.md`, blob `0db1759754bfaa85d1f5271f03dc6e0ca55d2209` (Main:N);
    `papers/Substratum.md`, blob `da64dc35d9b55a231354bab1fb7e138803e486a2` (Substratum:N);
  - SUBSTATE-1, `verification/programmes/substratum/continuous-substates/observation-context-protocol.md`,
    blob `6ca6f0abb3518242f80bd2a93392feba37875a65` (OCP:N);
  - MR-1, `verification/programmes/oi-qm/reconstruction/measurement-record-formation/preregistration.md`,
    blob `c36fb14bd7761d242049100fde0bbc7fa6c4dcd9` (PREREG:N), and `amendments/MR-star.md`, blob
    `45af1678c401c03ac55938761d8f012a48225743` (MR★:N);
  - K1-RDY-1, `verification/programmes/oi-qm/reconstruction/round-k1-rdy-1/preregistration.md`, blob
    `c7505385d70343189f561ddf747d41592ae4782a` (K1R:N), and `result.md`, blob
    `e494a32b7f5b43e0f4314bb101ab540dd343323b` (K1R-res:N);
  - BORN-SEL (b), `verification/programmes/oi-qm/reconstruction/born-sel-b-measure-20261104/QB3-EVIDENCE.md`,
    blob `9dac27fe5265d6b617937953cdab004e433f5a0f` (QB3:N).
  - OA-1 (`oa-1-20261112/OA-1-REPORT-r5.md`) is cited only through U1's quotations (OA1:N via U1).
- GitHub records read through the REST API on 2026-11-15: #1169 c.6891808569, c.6891338304,
  c.6891710167; #1305 body.

**Labels** (as U1, U2): **[M]** on `main` at its own layer; **[M-r]** verification record on `main`
with its review on `main`; **[NP]** named premise (§A.46 item 7); **[OFF]** off `main`, with its review
state; **[EXT]** external literature, with LIT's read status (FULL, ABSTRACT, SECONDARY, NOT READ);
**[P]** proposed definition; **[A-inf]** author-side inference; **PROVISIONAL** rests on U4 r1.

***

## 0. Scope

G1 fixes PLAN-G §1.2's objects (PLAN-G:86–117) and, for each protocol program, the U1 actions it
needs and their outcomes as already classified on record (PLAN-G:316). It stops where PLAN-G's G1 row
stops (PLAN-G:316): an action with no classification on record, or a definition that would need an
outcome-based choice (K-2). It also stops, per the brief, where a definition would need S7, O11 or a
frequency reading; §9 reports each.

Not done here: G2's K1 detection law (route A, H-1), G3's literature (X-1 to X-3), G4's measure and
frequency note, G5's synthesis. Where a definition below meets one of those, the slot is fixed and
its filling is assigned.

## 1. The fixed instance

[P] An **instance** is the tuple

    I = (rule ρ with its P-vii reading, slice form f, μ, AD-1 instance, geometry 𝒢, budget T, t_c, κ).

- **Rule and reading** (owner Q7). Under the *global* reading of P-vii, `ρ = K1` (MR★:464–483), a
  member of R-lin. Under the *scoped* reading, `ρ` is K1 only for apparatus that OB-b0 places in the
  reference class; otherwise a σ12 rule (MR★:667: native-Y, the SM:104–106 coupling graph that
  varies with the configuration, SM §6.5 dynamical links) or G_SM (U1 §4). Which applies is open
  under #1234; every verdict is reported per reading.
- **Slice form** `f ∈ {A-reg, A-cur}` (U1 AD-1(b), U1:228). Carried, not selected.
- **`μ`**, fixed with the model before any setting (U1 G3, U1:182). It includes the law of the
  setting region (§2.2). Levels as U1:190–197: *derived* only with the counting measure of Main Lemma 3
  (Main:54), otherwise *available relative to the declared `μ`*, with each datum listed.
- **AD-1 instance**: the observer family of §2.1, read only (AD-1(c)), with a fixed read schedule
  (AD-1(e)) and a finite budget (AD-1(f)).
- **Geometry** `𝒢`: a finite declared lattice and region partition, the native graph (MR★:467–472;
  a graph chosen per design is excluded on K1, MR★:471–472 [NP]).
- **`t_c`**: the one comparison tick (U1:156–158).
- **`κ`**: the map of §5, declared with `I`.

Every report carries `I`. Verdicts under different `ρ`, `f`, `μ` or frequency readings are reported
separately and never combined (NC-γ3; U1 G6).

## 2. The program family and the protocols

### 2.1 Regions and observers, declared once for every protocol

[P] One declaration, identical for all six protocols (U1:154–159):
- `Σ`: the source (carrier) region; `P_L`, `P_R`: the two path regions; `D = (D_1, …, D_n)`: the
  screen, `n` declared readout cells (OCP's two-port toy is `n = 2`, a fringe/antifringe pair,
  OCP:15); `A`: the marker region; `Z`: the setting region; `H_e`: herald region; ledgers `L`.
- Observers (AD-1(a)): `V_D ⊇ D`, `V_A ⊇ A`, `V_Z ⊇ Z`, `V_E ⊇ H_e`. **The same four observers are
  declared in every protocol.** A protocol never changes `Obs`.

*Ground.* Under reading (i) of O11 a different `Obs` is a different model, and G6 forbids combining
verdicts across models (U1:243–245, :876–878). Declaring one observer family keeps all six protocols
in one model without resolving O11. A marker that is "not read" is therefore held by `V_A` and
omitted from the compared record (§2.3), not moved into the hidden sector.

### 2.2 How the protocol label enters: three encodings, none selected

[P] The protocol label `a ∈ 𝒜` must enter one fixed program `g` through U1's actions. Three
encodings are defined; each is a different program, reported separately:
- **E-set.** `a` is the content of `Z` at the use tick, a datum of `μ` or written by `φ` from held
  records (U1 C-SET, U1:308–327). The program is one `g`; `L_a` is the restriction of its record law
  to `{held setting record = a}` (§3.2). Where `a` changes what `φ` does to the carrier (blocking a
  path; switching the marker coupling; switching the marker read), the change is a C-INT action of
  class I-sel or I-off (U1 §4.3).
- **E-prep.** `a` changes a preparation law (for example the marker's prepared content), under an
  executed herald with the complementary mass kept (U1 C-PREP, U1:264–272).
- **E-read.** `a` changes only the readout function applied to a held configuration (which partition
  of `V_A`'s configuration is reported). This is a post-processing, not an operation (OCP:49:
  "Passive changes of which column of a fixed probability table is displayed are not operations";
  S-C1(b), MR★:504–507 [NP]).

*Excluded encoding.* **E-decl**: `a` changes only which regions are declared, with `φ`, `μ` and `Obs`
fixed. [A-inf, from AD-1(c)] A declaration changes no region's content, so every record law is the
same for every `a`; E-decl cannot represent any of the six protocols as distinct laws. A change of
graph per protocol is a change of model (§9, O11).

### 2.3 The six protocols as program specifications

[P] SUBSTATE-1's six protocols (OCP:17–24), with one identical incident source and one schedule
(OCP:15). The table states what each protocol *requires*; §4 classifies.

| `a` | Protocol (OCP) | Required of the program | Compared record (subset of §3.1) |
|---|---|---|---|
| a1 | both open, no marker (OCP:19) | carrier from `Σ` through `P_L` and `P_R` to `D`; marker coupling absent or not engaged | screen, setting, herald, loss |
| a2 | left only (OCP:20) | transfer through `P_R` to `D` removed, with that flux booked as loss (subnormalized, OCP:26) | screen, setting, herald, loss |
| a3 | right only (OCP:21) | as a2 with `L` and `R` exchanged | screen, setting, herald, loss |
| a4 | both open, marker stored, not read (OCP:22) | marker coupling engaged; `V_A`'s record omitted from the comparison | screen, setting, herald, loss |
| a5 | both open, marker read in path partition (OCP:23) | as a4; `V_A`'s configuration reported through a declared path partition `π_P` | screen, marker (`π_P`), setting, herald, loss |
| a6 | both open, marker read in complementary partition (OCP:24) | as a4; reported through a declared partition `π_C` | screen, marker (`π_C`), setting, herald, loss |

- `π_P`, `π_C` are declared partitions of `V_A`'s finitely many states, with a null value `∅` kept,
  fixed with `I` and never chosen after any screen record is seen (NC-γ1). A partition chosen because
  it sorts screen records into fringes is a selection effect (OCP:45; H-8).
- **Which-path and complementarity are tested, not defined into `π_P`, `π_C`.** The operational
  predicates of §2.4 are test statistics computed from records.
- **Timing variant.** a6-delayed: the marker read tick is later than the screen record tick. The
  screen record is then retained to `t_c` (C-RET) or the joint law is R-seq (U1:165–167; K-4).
- **Three eraser cases kept apart** (#1169 c.6891710167): a6 is *sorting* on marker outcomes.
  *Physical reversal of the marker interaction* and *recovery of a record after a period of
  inaccessibility* (the parked record) are not among the six protocols; each would be its own
  protocol, and none is defined here (PROVISIONAL on U4 §§4.2, 6).

### 2.4 Auxiliary protocols that the measured quantities require [P, not adopted]

[A-inf, from LIT] The which-path knowledge actually measured in the experiments read first-hand is
obtained from **one-path-blocked runs with the marker read**: Schwindt 1999 obtains `K = 2L − 1` "from
path-blocked counts with the analyzer in place" (LIT 1.12, FULL); Ma 2013 measures "Path
probabilities … by blocking one path" (LIT 1.8, FULL). `D` itself is a maximum over marker
measurements and is not measured (LIT §3). None of the six protocols blocks a path and reads the
marker. So the raw-direct which-path quantity of X-4 is not defined on `𝒜_6`. The extension needed:

| `a` | Protocol | Use |
|---|---|---|
| a2P, a3P | one path blocked, marker read in `π_P` | operational path knowledge `K_P`: the total-variation distance between the marker-record laws of a2P and a3P, each normalized by its own incident mass, with equal priors (Schwindt's `K = 2L − 1`) |
| a2C, a3C | one path blocked, marker read in `π_C` | the same statistic `K_C` for `π_C`; `K_C = 0` is the operational content of "complementary" |

`𝒜_6` is SUBSTATE-1's preregistered set and is kept as the primary family. `𝒜_10 = 𝒜_6 ∪ {a2P,
a3P, a2C, a3C}` is proposed for X-4 only; whether to adopt it is owner question 1 (§12).

## 3. The record laws `L_a`

### 3.1 Record space

[P] For a program `g` of `I`, the complete record at `t_c` is the tuple

    r = (s, m, z, e, ℓ) ∈ 𝓡 = 𝓢 × 𝓜 × 𝓩 × 𝓔 × 𝓛,

- `s ∈ {0,1}^n`: the detection vector, `s_j = 1` when cell `D_j` registers a detection in the sense of
  `κ_det` (§5.2); the full vector is kept, not only its single-click part;
- `m ∈ 𝓜`: the marker report `π_P(V_A)` or `π_C(V_A)`, including `∅`; in a1–a4, `m` is not entered
  (§2.3), and the law with `m` retained is also kept as `L_a^full`;
- `z`: the held setting record (E-set);
- `e ∈ {E, ¬E, ⊥}`: herald executed, herald failed, or no herald process (G5);
- `ℓ`: loss and attempt marks (`⊥`, `∅`; MR★:639, :910–911). A mark with no executing process is
  listed with mass 0 by specification (U1 G5, U1:184).

Every component is a function of an observer's configuration **held at `t_c`** (G4, U1:183). A
component first held at an earlier tick enters only if retained to `t_c` (C-RET) or carried there
(S-A6) (U1:165–167).

### 3.2 The law, with full masses

[P] **`L_a` is the unnormalized measure on `𝓡`**

    L_a(r) = μ( { x ∈ S : rec_{t_c}(φ^{t_c} x) = r, z(x) = a } ),

where `rec_{t_c}` is the declared record map and `z(x) = a` is the held setting record (E-set). For
E-prep, the setting restriction is replaced by the executed herald `E_a`, and `¬E_a` is kept as an
outcome. Consequences of the definition:
- **Total mass** of `L_a` is `μ(z = a)`, with the herald-failed and loss outcomes inside it. Nothing
  is renormalized to the surviving or detected runs (G5; NC-γ4; OCP:15, :26).
- **All six laws are restrictions of one joint law** `L = Σ_a L_a` on `𝓡`, under one `μ` (G3, G6).
  Protocol-wise normalization uses only the incident mass `μ(z = a ∧ E)` (§5.3).
- **Ensemble object.** `L_a` is a law over `μ`, not over the analyst's sequence of configurations
  along one history (R-seq is a representation, U1 G4). The orbit-frequency reading is a separate
  object (§5.6), not a redefinition of `L_a`.
- **Level** of `L_a`: the weakest level of the actions `g_a` uses (U1:676), with every `μ`-datum
  listed.

### 3.3 Two consequences of the definitions alone [A-inf]

- **Read invariance.** Under E-read, a4, a5 and a6 are post-processings of one law `L_{a4}^full`
  (screen with `V_A`'s full configuration retained): `L_{a5} = (id × π_P)_* L_{a4}^full`,
  `L_{a6} = (id × π_C)_* L_{a4}^full`. Their screen marginals are identical, by AD-1(c) (reads change
  no content). Under E-set with a φ-effected read, whether the screen marginal is invariant is a
  property of the model (causal order of the read and the screen record), not of the definition.
- **Sum rule.** For each `a ∈ {a5, a6}`, `Σ_m L_a(s, m, ·) = L_{a4}(s, ·)` holds for full masses,
  `∅` included, identically under E-read. In raw coincidence data it holds only up to the marker
  detector's efficiency and coincidence window (RU4 finding 8), which `κ` carries (§5.4).

These are properties of the bookkeeping, not results about any model. They match the coherent
benchmark's structure (OCP:24: "unconditioned screen remains (1/2,1/2)"), which is not evidence
(NC-γ2).

## 4. U1 actions per protocol, and their outcomes on record

### 4.1 Actions needed

| Action (U1 §4) | Needed by | What it must deliver |
|---|---|---|
| C-PREP | all | the incident carrier preparation, one law for every `a`; a ready screen (for `κ_det`, §5.2); for E-prep, the marker law |
| C-SET | all (E-set) | `Z = a` with positive mass, held to `t_c` |
| C-INT | a2, a3 (blocking); a1 vs a4–a6 (coupling switch, E-set); a5 vs a6 (read switch, E-set only) | a setting-selected change of the carrier's or marker's transfer |
| C-REC | all (screen); a5, a6 (marker); herald | R1, R3, R5 under AD-1 (U1:511–517) |
| C-RET | all | screen, marker, setting and herald records held at `t_c`; a6-delayed |
| C-REN | only for sequential runs (§5.6) | ready screen and marker restored between runs |
| C-COMP | sequential runs; a6-delayed | one program, global schedule, joint hold at `t_c` |

### 4.2 Outcomes from records already classified

Global reading of P-vii (`ρ = K1 ∈` R-lin). U1's four outcomes (U1:205–213); only *not available*
is a negative under SNR-1.

| Step | Outcome on record | Source and standing |
|---|---|---|
| Carrier preparation | **unsourced**: under the counting measure "every region's marginal is uniform, so there is no ready region" | MR★:642 [NP]; U1 C-PREP first missing step (U1:300–304); hidden carriers: Gap 1 disproved at its scope (U1:283 [M-r]); T0 not shown (U4 §3.2, confirmed in RU4) |
| Ready screen for `κ_det` | **unsourced**: same ready-region gap | MR★:642, MR★ C-3 [NP]; U1 C-REC (U1:548–549) |
| Setting `Z = a`, held to `t_c` | value derived under μ-G; held record **unsourced** (reduces to C-REC) | U1 §4.2 (iv), AW-5; MR★:637 [NP] |
| Blocking in a2, a3 (E-set) | **not available** at D5's scope: blocking makes the carrier's transfer through one path depend on the setting, which is setting-selected I-sel on a carrier; on affine rules "the non-translational part of the carrier's map does not depend on `c`" | D5 (OA1:176–193 via U1:487) [M-r]; U1's factor-set reading [A-inf]; counts under SNR-1 only once that reading is verified (U2 §11.1) |
| Blocking by a different graph per protocol | a different model (MR★:471–472 [NP]); not comparable within `I` | §9, O11 |
| Marker coupling switch a1 vs a4 (E-set) | **not available** at D5's scope (same class as blocking) | as above; U4 §2.1: "Marker coupling is not a setting on K1" (PROVISIONAL) |
| Marker coupling a1 vs a4 (E-prep) | a change of the marker's prepared law only; on K1 it changes the screen only through the offset `Φ_{DA} s_A` | S-L5, MR★:584–593 [NP]; U4 §2.1, PK-2 (PROVISIONAL) |
| Read switch a5 vs a6 (E-read) | no operation; both are coarse-grainings of one joint record | S-C1(b), MR★:504–507 [NP]; OCP:49 |
| Read switch a5 vs a6 (E-set, φ-effected) | **not available** on R-lin at D5's scope (I-sel) | D5 [M-r]; U1:487 |
| Marker as which-path record (C-REC for `A`) | native marker: records a class in `S_A/K^t_A`; full masking undecided for `t ≥ 2`, complete at `t = 1` (RU4 finding 12, reviewer's hand check); **unsourced at (β)–(δ)** where masked; quiet marker: assumed apparatus | U4 §3.2, U4-F1 (PROVISIONAL); U4-CALC-r1 not used |
| Screen record R1 | **undecided** on K1 (trace route, C-4), blocked at C-3 | MR★:1373–1380 via U1:532 [NP] |
| Heralds, loss and attempt marks | no executing process on K1; listed with mass 0 | MR★:639 [NP] |
| Retention to `t_c` | **unsourced** (no bounded readable register; O-RET) | U1 C-RET (U1:590–599); S-C4a [NP] |
| Renewal between runs | readiness relocated, never created | Lemma R, PREREG:177–187 [NP]; U1 C-REN |

**Per protocol, global reading** [A-inf, from the table]: a1 and a4–a6 **unsourced** (preparation,
ready screen, retention), with E-set encodings of the coupling and read switches **not available** at
D5's scope; a2, a3 **not available** at D5's scope as settings of one program, and otherwise outside
`I`. No protocol reaches *available*.

**Scoped reading.** For a rule that is not affine, D5 does not apply. G_SM: operational I-sel is in
`φ`, with the request and ready precursor unsourced (U1:491, NIS2 STATUS:25–33 [M-r]); native-Y: "no
isolated available gate was found" (MR★:672–673 [NP]); the SM:104–106 graph and SM §6.5 links: not
screened. Outcome: **unsourced or not classified**, pending #866's σ12 screen (c.6891808569 wave 1,
item 4). Route E (SUBSTATE-1 continuous substates): no model is specified (OCP:58), and OCP's native
test gate (OCP:88–97) precedes any comparison; G1's definitions apply unchanged once a model is.

**Extension operations** (a detector or blocking operation an extension adds): typed into `φ`, the
criterion applies; typed into `Γ`, *requires assumed apparatus*; typed into `Obs`, **S7(a) stop**
(U1 §6.1), inherited, not reached anew (§9).

## 5. The correspondence map `κ`

[P] `κ = (κ_det, κ_mark, κ_norm, κ_freq, κ_tgt, κ_cmp, κ_scale)`, declared with `I` before any `L_a`
is evaluated (NC-γ1), identical for every protocol and for every control law (§7).

### 5.1 What `κ` acts on

`κ` acts on record laws over `𝓡`: native `L_a`, and the control laws of §7, alike. It reads masses of
held records only. It contains no amplitude, wavefunction, `|·|²`, Kraus map, Born probability or
assigned marker overlap (NC-γ2; OCP:11, :41; PREREG:233–237).

### 5.2 `κ_det`: what counts as a detection at a cell

[P] **A detection at cell `D_j` at tick `t` is the event that the held readout of `D_j` differs from
the value to which `D_j` was prepared by the program's screen preparation (C-PREP), read through a
declared finite partition of `D_j`'s states.**
- *Ground.* R1 (U1:514): a record of a property is a dependence of a held value on it; a detection is
  a departure from a ready value. The corpus's null value is a coarse value, "for example the zero
  value" (MR★:639), and the zero configuration is fixed (P-3, MR★:466). The rule names no outcome.
- *Consequence* [A-inf]. Without a prepared screen, `κ_det` is undefined, and (γ→) is *unsourced at
  C-PREP* for the screen, not a miss. This is H-1's dependency (PLAN-G:185–194), expressed in `κ`.
- *Excluded.* A `κ_det` that converts a field value into a click rate or an intensity is a supplied
  detector model and fails G1 unless the conversion is effected by `φ` as a C-REC step (H-2,
  PLAN-G:195–199).
- *Multiplicity.* The whole vector `s` is kept. Runs with no detection and runs with several are kept
  with their masses (NC-γ4). Single-detection observables (X-1 discreteness, X-2 anticorrelation) are
  functionals of the joint law of `s`, not of cell marginals.

### 5.3 `κ_norm`: normalization per incident particle

[P] Counts per incident particle for protocol `a` are `L_a(·) / μ(z = a ∧ E)`, the denominator
being the mass of the executed preparation herald under setting `a`; with no herald process, the
setting mass `μ(z = a)`. Division by the mass of detected runs is excluded (OCP:26: "Compare raw
counts, not separately normalized surviving subsets"). One-open protocols are therefore
subnormalized by construction. On K1, with no executing herald or attempt process (MR★:639 [NP]),
the incident mass is the setting mass, and the herald outcome has mass 0 by specification.

### 5.4 `κ_tgt`: the target observables, singles versus coincidences

[P, from LIT] Each target datum is typed before use.

| Type | Definition | Protocols | Sources read (LIT) |
|---|---|---|---|
| T-sing | counts at a cell over all runs, no condition on any marker or partner detection | a1–a4 | X-1 sources NOT READ (G3); Schwindt 1999 `V` "with the polarization analyzer removed", FULL (LIT 1.12); Dürr 1998 unconditional patterns, SECONDARY, marker read status NOT READ (LIT 1.11) |
| T-coinc | joint counts (cell, marker or partner detector outcome) per fixed integration time | a5, a6 (and a1 in two-photon form) | Kim 2000 `R01`–`R04`, FULL, no visibility numbers or error bars (LIT 1.6); Walborn 2002 Figs. 2–9, FULL, no numbers (LIT 1.7); Ma 2013 counts conditioned on Det 4, FULL, with numbers (LIT 1.8) |
| T-coinc-unsorted | coincidences with the partner detected and no marker analysis | a4 in two-photon form | Walborn 2002 Figs. 3, 7, FULL (LIT C2) |
| T-block | one path blocked, marker read | a2P, a3P (§2.4) | Schwindt 1999, FULL; Ma 2013, FULL |

Rules fixed with the types:
- **No substitution between types.** T-coinc and T-coinc-unsorted data are not compared with a
  T-sing image, and conversely. Unsorted singles at the interfering detector in delayed arrangements
  are reported in none of Kim, Walborn or Ma (LIT C2, C4, C5); κ has **no target** for a4-in-a-delayed-
  arrangement in the sources read, and the statement "the unsorted pattern has no fringes" there is
  a QM prediction, not a raw-direct datum.
- **Coincidence normalization.** T-coinc counts are per integration time, not per incident particle,
  and the incident flux is not reported. `κ` compares them only through quantities independent of
  that flux: shapes and contrasts within one sorted channel, and ratios across channels at equal
  integration times (Walborn's Figs. 4–5 at 800 s against Fig. 3 at 400 s are rescaled by the stated
  times, LIT 1.7).
- **Marker detection efficiency** `η` enters a T-coinc image of `L_a` as a measured apparatus input
  (E), taken from the source when reported (for example Schwindt's efficiency ratio 1.11 ± 0.01,
  LIT 1.12), never fitted. Where `η` is not reported, comparisons that depend on it (the sum rule of
  §3.3 against raw counts) are not made.
- **Background.** Background-subtracted values (Schwindt, 100–400 s⁻¹; Ma's Canary data, LIT 1.8,
  1.12) are inferred quantities; `κ` compares the model's law with background added as stated in the
  source, or does not compare.

### 5.5 Raw-direct, derived and inferred (§A.24)

| Class | Quantities | Use in `κ` |
|---|---|---|
| Raw-direct | cell counts; coincidence counts; path-blocked counts; integration times | compared as-is |
| Derived by a stated formula from raw counts | `V = (max − min)/(max + min)` over cells of one channel; `K = 2L − 1` from T-block counts with the stated efficiency; the additivity defect `Δ_j` (§7.1) | compared, the formula fixed in `κ` |
| Inferred or fitted | `D` (a maximum over marker measurements); background-subtracted values; Ma's corrected curve `V = 0.95√(1 − (I/0.97)²)`; visibility reductions attributed to detector size or pump divergence (Kim) | not compared |

### 5.6 `κ_freq`: probability and frequency, both readings carried (owner Q5)

[P] Performed data are relative frequencies over `N` runs in one laboratory history. Two readings are
carried; neither is adopted; every comparison is reported under both.
- **κ-ens (ensemble reading).** The relative frequency of a record value over runs is compared with
  its mass under `L_a` (§3.2), normalized by `κ_norm`. Each run is one evaluation of `g_a` from `μ`;
  no renewal is required, because runs are not composed.
- **κ-orb (orbit-frequency reading).** The runs are successive segments of one orbit of `φ`: run `k`
  of protocol `a` is program `g_a` started at tick `t_0 + kτ`. The observable is the empirical
  frequency `F_N(x)` of a record value over the `N` runs, a function of the actual configuration `x`.
  This needs, between runs, renewal of the screen and marker (C-REN) and, for a change of protocol, a
  φ-effected setting write (C-SET; U2 CP-4's step class). OI's prediction for `F_N` under κ-orb is
  the per-orbit value, reported as the set of orbits of positive `μ`-mass on which `F_N` agrees with
  the datum, and that set's `μ`-mass. **No threshold on that mass is set, and no orbit is selected:**
  selecting the orbit or the threshold after comparison would choose by outcome (K-2, NC-γ1).

Where the readings differ, for the slots G4 fills [A-inf, for G4 to check]:
- Full-period orbit averages are averages under the uniform law on an orbit, which differs from the
  counting law on records already on `main` (QB3:60–61, CE-8). A full period exceeds the budget of
  AD-1(f) (below recurrence, U1:232; S-L6 [NP]). Within the budget, κ-orb's object is `F_N` for
  `Nτ ≤ T`, not the orbit-uniform law.
- `F_N` is a function of the unknown actual configuration; predicting it needs a law over
  configurations. Both readings therefore consume a measure, `μ` (H-4 cross-propagation,
  PLAN-G:236–238). Which measure κ-orb's per-orbit report weights by is G4's question; G1 fixes
  only that the weight is the model's declared `μ` and that the report is the agreeing mass, not a
  verdict selected from it.
- κ-orb requires C-REN; κ-ens does not. The frequency reading therefore changes which U1 actions a
  protocol needs (§4.1), and so can change its outcome.

### 5.7 `κ_cmp`: the agreement rule

[P] Fixed before evaluation, and the same for every target and control:
- A target with a reported uncertainty: agreement when the `κ`-image lies within the reported
  interval, at the confidence level the source states.
- A target reported only qualitatively (Walborn's "roughly equal"; Kim's plotted curves without
  numbers; LIT 1.6, 1.7): agreement or disagreement **of the qualitative feature only** (fringes
  present or absent; π-shift between sorted channels). Such a target cannot yield a counted miss on a
  quantitative value.
- A counted miss needs an *available* `L_a` with every input derived or disproved (PLAN-G:136–138)
  and a quantitative raw-direct target.

### 5.8 `κ_scale`: lattice cells to physical positions

[P] `κ` separates **scale-free** functionals (visibility, the additivity defect, π-shifts, sum rules,
anticorrelation parameters) from **scale-carrying** ones (fringe spacing, envelope width). The cell
identification `D_j ↦ position` and any length scale are declared in `I`. Scale-carrying comparisons
are conditional on spatial isotropy, empirical input E4 (Main:670), and on the observer-level wave
operator, unresolved (Main:588; #914 row 12) (H-9). A length scale set from the data it is compared
with is a fitted input (R) and is reported as such.

**Phase scans.** Schwindt's `V` is taken by scanning a path length (LIT 1.12), a phase setting. On K1
a phase setting enters additively and a change of arm propagation is a change of geometry (U4 §2.1,
PROVISIONAL). A phase-scan datum therefore corresponds, on K1, to a family of geometries, not to one
program. With an `n`-cell spatial screen, the cell index plays the role of the phase, and one program
suffices. [A-inf] The only FULL-read T-sing datum with an unread marker (Schwindt) is of the
phase-scan kind; the spatial unconditional patterns with a stored marker (Dürr) are SECONDARY.

## 6. The two directions (§A.34)

For one instance `I` (reading, slice form, `μ`, frequency reading included):

**(γ→), derivation and agreement.** For every performed protocol `a ∈ 𝒜` with a typed target:
1. every U1 action of `g_a` has outcome *available*, so `L_a` is available at a stated level, derived
   from `(φ, μ)` under a declared geometry;
2. `κ(L_a)` agrees with every typed raw-direct target of `a` under `κ_cmp`;
3. the controls of §7 are green for that comparison.

*Closed at level X* for protocol `a` when 1–3 hold, X the weakest level of its inputs. *Counted miss*
when 1 holds with every input derived or disproved, 3 holds, and 2 fails on a quantitative target; it
falsifies `(M, κ)` at that scope, not every observer-level extension (Code Review Rules, no-go
scope). *Unsourced* or *requires assumed apparatus* when 1 fails that way; not a negative.
*Undecided* otherwise. **What would close it:** a derivation of `L_a` from `φ` and `μ` for a declared
geometry, with sourced preparation, records and retention, followed by the comparison.

**(γ←), coverage.** For every perceived phenomenon `Φ` in the declared list (§7.3), there is a program
`g ∈ Γ_exe(M)` of the **same** `M`, `μ` and AD-1 instance, with outcome *available*, such that
`κ(L_g)` agrees with the raw-direct target that exhibits `Φ`, and `Φ` lies in the coverage credit set
of §7.2 (owner Q6). **What would close it:** exhibiting such a program per phenomenon. A negative for
`Φ` needs *not available*, at a verified scope, for every program whose `κ`-image would exhibit `Φ`;
otherwise the report is *not shown*.

**Neither gives the other.**
- (γ→) is universal over the fixed family `𝒜`; (γ←) is existential over `Γ_exe(M)`. A covering
  program can disagree with a performed protocol elsewhere, and agreement on `𝒜_6` covers nothing
  outside it: X-2 needs a beam splitter and two detectors, X-3 three paths, X-4 the auxiliary
  protocols of §2.4.
- The intervention dilation (Main:480–482) realizes any action-labelled family with a constructed
  `S`, `φ` and `{𝓘_a}` per family. It supplies neither direction (representable only, K-4; NC-rep,
  §7.1).
- Read invariance (§3.3) is a property of the definitions under E-read; it is not evidence for
  either direction.

## 7. Controls

### 7.1 Positive and negative controls, as laws on `𝓡`

Every control law is passed through the same `κ` (§5.1).

- **C0, fixed-path classical stochastic** (OCP:34–35). A path variable `π ∈ {L, R}` with source law
  `(p_L, p_R)`, a per-path response law `r_π` on `𝓢 × 𝓛`, independent of whether the other path is
  open and of the marker. Blocking `π` sends its runs to loss. Its laws: `L^{C0}_{a2} = p_L r_L`,
  `L^{C0}_{a3} = p_R r_R`, `L^{C0}_{a1} = L^{C0}_{a4} = L^{C0}_{a2} + L^{C0}_{a3}` (subnormalized sum).
  *Test statistic:* the additivity defect per incident particle,
  `Δ_j = c_{a1}(j) − c_{a2}(j) − c_{a3}(j)`, from T-sing data. C0 has `Δ ≡ 0`.
  *Required result:* C0 **fails** the two-open comparison whenever the target's `Δ` differs from 0
  under `κ_cmp`. If the target data do not separate `Δ` from 0, the interference comparison is void
  (control not green). A failure of C0 rules out only this restricted model (OCP:35).
- **PC-wave, classical coherent wave** (C1, OCP:37–38). Classical complex field contributions
  `f_L(j)`, `f_R(j)`, a linear recombiner, intensity `|f_L(j) + f_R(j)|²`, and a supplied square-law
  stochastic detector with click rate proportional to intensity; a marker as classically correlated
  wave and marker modes. The amplitudes and the detector belong to the control, not to `κ`.
  *Required result:* **passes** the fringe statistics (`Δ ≠ 0`) and the fringe-build-up shape of X-1;
  OCP:38: "This control MUST be marked PASS for the interference statistics, not incorrectly used as
  a no-go." Its expected result on X-2 and X-3 is to be taken from G3's first-hand reads, not
  assumed here.
- **NC-rep, representability** (Main:480–482, :582). The anti-complementary family
  `L^{rep}_{a4}` screen marginal `= L_{a1}` screen marginal (fringes kept with a stored, unread
  marker), and `L^{rep}_{a5}(·, m = L) = L_{a2}`, `L^{rep}_{a5}(·, m = R) = L_{a3}` (full which-path
  on reading). *Required result:* realizable by the dilation, which shows that representability
  tests nothing. [A-inf] Whenever `Δ ≠ 0` it has no E-read realization in a bare model: its a4 and a5
  screen marginals differ (`L_{a1}` against `L_{a2} + L_{a3}`), contrary to read invariance (§3.3). It
  is the time-indexed accessibility reading of U4 §6.3 (RU4 finding 6; PROVISIONAL), and it disagrees
  with the T-sing unread-marker data as read (Schwindt; LIT C1, C5).
- **NC-copy, non-invasive classical copy** (PREREG:237–238, CC1). A marker that copies `π` with no
  back-action: fringes intact with `K_P = 1`. *Required result:* reproduced as a law outside
  `D² + V² ≤ 1`; it separates record formation from visibility loss. On K1, by S-L5 [NP], every
  marking is of this kind (MR★:592–593, "marking is non-invasive, which is the CC1 kind")
  (PROVISIONAL, U4 §2.1, PK-2).
- **NC-noise, loss without a record** (CC7 at VER2's scope, "`V = 0` needs uniform `f`"; U4 §4.2). A
  carrier-free additive offset at `D` with no marker correlation: `V` reduced with `K_P = 0`. Under
  S-L5's C-9 wording the offset is from content that is not a function of the carrier's content and
  may be correlated with it under `μ` (RU4 finding 11). *Required result:* distinguished from
  record-tied loss by `K_P` on the auxiliary protocols; on `𝒜_6` alone the two are not separated.
- **Deletion** (PREREG T8). Remove in turn the second path's transfer, the marker, the setting and
  the herald. *Required result:* the attributed effect vanishes. On K1 a removed transfer is a change
  of geometry, hence of model (§4.2); its deletion control is a separate instance, reported
  alongside.

### 7.2 The classical-wave ceiling and the coverage credit set (owner Q6)

[P] For a native result on instance `I`, its **coverage credit set** is the set of typed target
observables on which `κ(L)` agrees with the data and PC-wave, passed through the same `κ`, does not.
Where the credit set is empty and C0 fails while PC-wave and the native law agree, the result is
reported as "interference compatible with classical coherent waves; no quantum completion" (OCP:45),
and it does not count toward the coverage half of AC-1. Agreement on observables that classical
eraser models also reproduce (CC4, CC5 at VER2's scopes; OCP:38) is reported the same way for those
models.

### 7.3 The perceived-phenomena list for (γ←)

[P] PLAN-G §5.3's list (PLAN-G:293–299), typed by §5.4, with read status. G1 adds no item.

| # | Phenomenon | Protocols | Read status |
|---|---|---|---|
| X-1 | fringe build-up from discrete detections | a1 (T-sing) | NOT READ (G3) |
| X-2 | anticorrelation behind a beam splitter | outside `𝒜` | NOT READ (G3) |
| X-3 | `I_3 = 0` | outside `𝒜` | NOT READ (G3) |
| X-4 | complementarity with a stored, unread marker | a4 (T-sing), a2P/a3P (T-block) | Schwindt FULL; Dürr ABSTRACT and SECONDARY |
| X-5 | sorting eraser: conditional fringes and antifringes; none under a path read | a5, a6 (T-coinc) | Kim, Walborn, Ma FULL; unsorted singles not reported |

### 7.4 Noncircularity countercontrols, with checkpoints (§A.41)

| Invariant | Checkpoint |
|---|---|
| NC-γ1: `I` (with `κ`, `π_P`, `π_C`, the encoding E-set/E-prep/E-read, the run convention, `μ`, AD-1) declared before any `L_a` is evaluated; `κ` not justified by matching Born statistics | the instance declaration is a fixed record cited by every evaluation; a reviewer checks that no `κ` component, partition or encoding changed after any law was evaluated |
| NC-γ2: no amplitude, wavefunction, Kraus map, Born probability or assigned marker overlap in `κ` or in a native law | §5.1; the reviewer checks each `κ` component against this list; OCP's benchmark table is used for protocol structure only |
| NC-γ3: one `M`, `μ`, AD-1 instance for all of `𝒜`; no combination across instances | every report carries `I`; §2.1's single observer family |
| NC-γ4: complete masses, no postselection | `L_a`'s total mass equals `μ(z = a)` (§3.2); `κ_norm` divides only by incident mass (§5.3) |
| NC-γ5: no C adjusted after results are known | a change of `I` after evaluation creates a new instance, reported beside the old one and not replacing it |

## 8. Dependencies

| Definition | U4 (PROVISIONAL) | S7 | P-vii reading | Slice form | `μ` | Frequency reading |
|---|---|---|---|---|---|---|
| `𝓡`, `L_a`, masses (§3) | — | — | — | per `f` | per `μ` | κ-ens object only |
| Encodings E-set/E-prep/E-read (§2.2) | marker coupling not a setting on K1 (U4 §2.1) | — | which rule | — | — | — |
| §4.2 outcomes on K1 | (β), masking, PK-2, T0 (U4 §§2.1, 3.2, 6.1) | Obs typing of extension operations | global vs scoped | AD-1(b) per form | μ-G for MR★:642 | C-REN only under κ-orb |
| `κ_det` (§5.2) | — | a detector typed into `Obs` | — | which slice `D_j` reads | ready screen as a `μ`-datum or herald | — |
| `κ_freq` (§5.6) | — | — | — | — | the weight of κ-orb's report | both carried |
| `κ_scale`, phase scans (§5.8) | U4 §2.1 | — | — | — | — | — |
| NC-copy, NC-noise on K1 (§7.1) | S-L5 consequences, PK-2 | — | global | — | — | — |
| Three eraser cases (§2.3) | U4 §§4.2, 6 | — | — | — | — | — |

## 9. Stops

- **S7.** Not chosen. Reached only as inherited from U1 §6.1: an extension's operation (a detector,
  a blocking or a read operation) typed into `Obs` gets no verdict. The `φ` and `Γ` typings are
  classified (§4.2). No G1 definition needs S7 to be chosen.
- **O11.** Not resolved. G1 avoids it by one observer family (§2.1) and by excluding E-decl. It is
  reached **conditionally** for one comparison: on K1, a2 and a3 are expressible only as programs of
  other models (a different graph) once blocking as a setting is not available (§4.2). Comparing
  those programs with a1 within (γ) needs a reading of O11 under which the models are identified, or
  a G6 exception. Neither is supplied; such programs are reported per model, never combined.
- **Frequency reading.** Not adopted (§5.6). κ-orb's per-orbit report fixes no threshold and selects
  no orbit.
- **Outcome-based choice.** None made. The partitions `π_P`, `π_C`, `κ_det` and the encodings are
  fixed by target-neutral grounds and declared with `I`.
- **Actions with no classification on record.** For the scoped reading, the SM:104–106 graph and the
  SM §6.5 links have no recording screen (MR★:667; U4 §4.5). G1 records them *not classified* and
  stops there for those rules.

G1 did not halt: every definition it was asked for is stated.

## 10. Findings and assumption-watch markers (§A.31)

**Productivity test, fixed before the walk:** an item is a gem if it is strictly stronger than the
obvious restatement and either constrains (γ) or exposes an assumption. Favourable readings were
pressure-tested; G1-F2 was re-tested under E-set with a φ-effected read, where it does not hold by
definition.

| # | Finding | Check | Class |
|---|---|---|---|
| G1-F1 | The raw-direct which-path quantity of the experiments read is measured on path-blocked runs with the marker read (Schwindt; Ma), not on any of SUBSTATE-1's six protocols; X-4 is not defined on `𝒜_6` | LIT 1.8, 1.12, §3 | NEW: exposes an omission in the protocol set for X-4; owner question 1 |
| G1-F2 | Under the read-as-post-processing encoding, a4–a6 are images of one law, with equal screen marginals and an exact full-mass sum rule, by AD-1(c) alone | definitions §3.3 | ELABORATING: these are bookkeeping identities, not evidence; NC-rep is the family that breaks them |
| G1-F3 | On R-lin, blocking a path and switching the marker coupling or read, as settings of one program, are setting-selected I-sel, not available at D5's scope; a2, a3 survive only as programs of other models | D5 via U1:487; MR★:471–472 | ELABORATING (H-3 made precise); counts only once U1's factor-set reading is verified |
| G1-F4 | `κ_det` needs a prepared screen; without one (γ→) is unsourced at C-PREP, not a miss | §5.2; MR★:642 | ELABORATING: H-1's dependency located in `κ` |
| G1-F5 | Within AD-1(f)'s budget the orbit-frequency reading's object is a finite-run frequency `F_N`, not the orbit-uniform law; both readings consume a measure; κ-orb needs C-REN and κ-ens does not | §5.6; QB3:60–61; U1:232 | ELABORATING; assumption-watch marker for G4 (sharpens H-4) |
| G1-F6 | The only FULL-read singles datum with an unread marker is a phase-scan datum; on K1 a phase scan is a family of geometries (PROVISIONAL), while a spatial screen needs one program | LIT 1.12; U4 §2.1 | BORDERLINE: it bears on which targets one instance can be compared with |
| G1-F7 | No target in the sources read exists for the unsorted singles of a delayed arrangement; κ may not substitute coincidence data | LIT C2, C4, C5 | CONFIRMING (LIT's finding carried into `κ`) |

**Cross-propagation.** G1-F1 applies to every OI comparison with complementarity data (D-1, AC-1's
coverage half, MR-1's T1). G1-F5 applies to every OI comparison of a law under `μ` with laboratory
frequencies (PLAN-G:236–238).

## 11. Off-`main` references traced (§A.42 item 8)

| Reference | Claim it is attached to here | Classification |
|---|---|---|
| PLAN-G at `f86dd1f7` | the objects G1 fixes, H-1 to H-10, routes, X-list | support off `main` (gap); plan not reviewed |
| U1 at `f86dd1f7` | criterion, AD-1, outcomes, C-INT classes | support off `main` (gap); accepted, c.6891241282 |
| U2 at `f86dd1f7` | counting conditions for the factor-set reading; CP-4 step class | support off `main` (gap); accepted, c.6891710167 |
| U4 r1 and RU4 at `f86dd1f7` | every PROVISIONAL entry | support off `main`, under revision (REVISE) |
| LIT at `f86dd1f7` | target typing, read status, G1-F1, G1-F6, G1-F7 | support off `main` (gap); reviewed |
| U4-CALC-r1 | not used | provenance |
| VER2 (cited through RU4 and U2) | CC7 and S-L5 C-9 scopes | support off `main`; accepted at its scopes, c.6891511297 |
| #1169 c.6891808569, c.6891338304, c.6891710167; #1305 | authorization, target, three cases | provenance and governance |

Every statement resting on an [OFF], [NP] or PROVISIONAL row carries that gap. This note is itself
off `main` and unreviewed.

## 12. Owner questions, and what later units use

**Owner questions.**
1. Is `𝒜_10` (§2.4, one-path-blocked protocols with the marker read) adopted for X-4, or is X-4
   compared on `𝒜_6` only, with its which-path quantity left undefined?
2. Is `κ_det` (§5.2, departure from the prepared value) accepted as the detection rule, on its
   stated ground?
3. Is κ-orb's report as the agreeing `μ`-mass of orbits, with no threshold (§5.6), the intended form
   of the orbit reading, or is that form G4's to fix?
4. Which encodings of §2.2 are admitted for the a1/a4 distinction (E-set, E-prep), given that E-decl
   represents none?

**For G2** (after the 2b review): `κ_det`, `κ_norm`, the record space and the E-set/E-prep
encodings; G1-F3 and G1-F4; C0's `Δ` and PC-wave as its required controls. **For G3:** the target
typing (§5.4), the raw-direct classes (§5.5) and PC-wave's open X-2/X-3 entries. **For G4:** §5.6 and
G1-F5. **For G5:** §6's two directions, §7.2's credit set, §8's dependency table.

Nothing here authorizes G2–G5, a calculation or any change of Issue, plan or manuscript.
