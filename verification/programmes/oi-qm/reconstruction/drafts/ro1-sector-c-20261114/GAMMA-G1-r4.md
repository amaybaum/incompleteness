# GAMMA-1 unit G1, r4; paper-only; definitions; unreviewed

**What this note does.** It fixes, for one fixed model, one measure `μ` and one access instance
under the accepted U1 criterion, the objects that (γ) at Main:682 is stated in: the record laws `L_a`
of the ten protocols of `𝒜_10`, with their masses under each encoding, the correspondence map `κ` onto raw-direct double-slit
observables (§A.24), the two directions (γ→) and (γ←) (§A.34), and the controls. It derives no record
law, evaluates no `L_a`, runs no computation, simulation, enumeration or Lean, edits no manuscript,
adopts no premise, extension or sector condition, and changes no Issue. Each [P] is a proposed
definition for review. Each [A-inf] is an author-side consequence of definitions, by hand, and is not
verification.

**Revision r4.** G1 r3 (`GAMMA-G1-r3.md`, blob `20166317`, at PR #1294 commit `b3c79f60`) is accepted
by the owner, #1169 c.6892563291 (`amaybaum`, 2026-11-15T09:49:19Z): "The definitions are accepted.
Results that depend on U4, and credit by scope alone, stay conditional." r4 applies that record's six
answers to r3's owner questions, and their necessary consequences, and changes nothing else. r3 is
kept unchanged. The answers, cited here as **G1-A1** to **G1-A6** (to keep them apart from the plan's
Q5–Q7 answers below), and where each is applied are listed in `RESPONSE-G1-r3-OWNER.md` and in §12.
The review history of r1–r3 is in `RESPONSE-GAMMA-G1-r1.md` and `RESPONSE-GAMMA-G1-r2.md`.

**Authorization.** Owner decision record #1169 c.6891808569 (`amaybaum`, 2026-11-15T08:39:13Z),
wave 1, item 3: "γ plan, unit G1 (definitions) starts now. Its classifications that depend on U4
stay provisional." Answers binding here (same record): "Q5: the ensemble and orbit-frequency
readings are both carried; neither is adopted"; "Q6: compatibility with classical waves alone does
not establish quantum coverage"; "Q7: γ is reported under each reading of P-vii, and C-1 and OB-b0
stay open under #1234". "No new premise, execution or merge is authorized." Physical source remains
NOT PASSED. Amended target, #1169 c.6891338304 (`amaybaum`, 2026-11-15T07:54:33Z): coverage of
perceived quantum phenomena and agreement with every performed experiment are required; C is
defined with no reference to quantum outcomes; the relation of C to Q is a finding.
Acceptance and answers, #1169 c.6892563291 (`amaybaum`, 2026-11-15T09:49:19Z): "Acceptance records the
reviewed work and its stated limits. It does not establish quantum coverage, and it adopts no new
physical premise." G1-A1: "all four auxiliary protocols are added"; G1-A2: "both detection-rule
variants are kept, separately"; G1-A3: "the orbit-frequency report is accepted, with no weights chosen
before G4"; G1-A4: "'no marker' means the coupling is absent"; G1-A5: "the comparison constants are
fixed, and a sensitivity analysis over a declared set is added"; G1-A6: "separation by scope alone is
not sufficient, so the CC4/CC5 credit stays conditional". "Not authorized: merges, CI dispatches, new
premises."

**Issue.** #1305 (GAMMA-1). **Writer:** Claude. **Review:** a separate non-author reviewer
(pending); ChatGPT review optional.

**Inputs, at exact objects.**
- RO-1 drafts in `verification/programmes/oi-qm/reconstruction/drafts/ro1-sector-c-20261114/`,
  branch `research/ro1-sector-c-1169-20261114` (PR #1294) at `20cdb9e5d` (the review of r1), and
  at `0300c8437` for the review of r2 (`REVIEW-GAMMA-G1-r2.md`, blob
  `20d8bbc5a7ae33022a71e36b44e555b203795921`, cited RG2). **Off `main`.**
  - `GAMMA-G1-r1.md`, blob `46697d9c76892914cd2719f768373c836b952d17` (G1r1:N), and its review
    `REVIEW-GAMMA-G1-r1.md`, blob `17431953280e20618d484f48fe87b65dd8ba48ea` (RG1, by finding);
  - `GAMMA-PLAN-r1.md`, blob `77f1fcd8d32403b26fb87c47cfd572bbf982febb` (PLAN-G:N); plan only, not
    reviewed (#1305 body);
  - `S3-U1-r5.md`, blob `68983f8666df0ca6c26ec4b9ec00d0a9e4072f67` (U1:N); accepted, #1169
    c.6891241282;
  - `S3-U2-r3.md`, blob `2711c168a65c0ae4397195593528fcf0ee6a4cba` (U2, by section); accepted with
    its recorded limits, #1169 c.6891710167;
  - `S3-U4-r3.md`, blob `54ee962919ab17d04f430b2847ab677cbc444829` (U4, by section), at `c3353dc5`;
    accepted by the owner, #1169 c.6892563291: "D-1 stays undecided at γ. No experimental
    contradiction is established". **Every classification below that rests on U4 is PROVISIONAL**
    ("Results that depend on U4 … stay conditional", same record). r1–r3 of this note cited U4 r2
    (blob `d8cced4c`); the section numbers are the same in r3;
  - `U4-CALC-r2.md`, blob `bef634e2100979d499b87f7139440dd6cff4fc64` (CALC, by theorem), reviewed
    ACCEPT in `REVIEW-U4-CALC-r2.md`, blob `70eddf2dad303b31c9691ad8ac1dcd3ee4576f8f`; accepted by
    the owner, #1169 c.6892224647 (`amaybaum`, 2026-11-15T09:17:55Z): "2b r2 (`U4-CALC-r2.md`, blob
    `bef634e2` at `9d5b2169`) is accepted as a bounded paper-only calculation"; "It upgrades no named
    premise and establishes no physical source";
  - `LIT-ERASER-r3.md`, blob `2b414173ce862d570aabb56e86c6b76344da0194` (LIT, by item); reviewed;
  - `VERIFY-SL3-CC-r2.md`, blob `9f81ad0ea5b517c6d3758a328ee2c16de5bb4fc7` (VER2); accepted at its
    stated scopes, #1169 c.6891511297 item 1;
  - `S3-PLAN-r9.md`, blob `46ebc72d866e24a6ea5a0050f7afca3f18c8fffb` (PLAN); accepted,
    c.6890079967.
- Corpus at `origin/main` `75cc51009aebcfb17c1bbf76d149760c540aac3b`, read with `git show`:
  - `papers/Main.md`, blob `0db1759754bfaa85d1f5271f03dc6e0ca55d2209` (Main:N);
  - SUBSTATE-1, `verification/programmes/substratum/continuous-substates/observation-context-protocol.md`,
    blob `6ca6f0abb3518242f80bd2a93392feba37875a65` (OCP:N);
  - MR-1, `verification/programmes/oi-qm/reconstruction/measurement-record-formation/preregistration.md`,
    blob `c36fb14bd7761d242049100fde0bbc7fa6c4dcd9` (PREREG:N), and `amendments/MR-star.md`, blob
    `45af1678c401c03ac55938761d8f012a48225743` (MR★:N);
  - BORN-SEL (b), `verification/programmes/oi-qm/reconstruction/born-sel-b-measure-20261104/QB3-EVIDENCE.md`,
    blob `9dac27fe5265d6b617937953cdab004e433f5a0f` (QB3:N).
  - OA-1 (`oa-1-20261112/OA-1-REPORT-r5.md`) is cited only through U1's quotations (OA1:N via U1).
- `GAMMA-G1-r3.md`, blob `201663175173274de45077f38463f63c27e91ae7`, and its review
  `REVIEW-GAMMA-G1-r3.md`, blob `a6836a0cc78193d5495bbd43032dc2d4a475b907`, at `b3c79f60`.
- GitHub records read through the API on 2026-11-15: #1169 c.6891808569, c.6891338304,
  c.6891710167, c.6892224647, c.6892563291; #1305 body.
- External literature only through LIT, at LIT's read status. No external source was read for r2.

**Labels** (as U1, U2): **[M]** on `main` at its own layer; **[M-r]** verification record on `main`
with its review on `main`; **[NP]** named premise (§A.46 item 7); **[OFF]** off `main`, with its review
state; **[EXT]** external literature, with LIT's read status (FULL, ABSTRACT, SECONDARY, NOT READ);
**[P]** proposed definition; **[A-inf]** author-side inference; **PROVISIONAL** rests on U4 r3. The U4 citations
point to U4 r3, section for section. Where r3's text differs from r2's in a cited section, the item
says so: U4 r3 §2.1 adds a "Beyond H-μ" extension (§4.2, E-prep row); U4 r3 §3.2 adds that masking is
pair-relative (§4.2, marker row, which rests on CALC directly); U4 r3 §6.1 and §6.3 restrict PK-2 to
"fixed geometry, tick and background" (§7.1, §8); U4 r3 §5.4 makes the Case Pk typing of the
delayed-choice erasers conditional (§2.3).

***

## 0. Scope

G1 fixes PLAN-G §1.2's objects (PLAN-G:86–117) and, for each protocol program, the U1 actions it
needs and their outcomes as already classified on record (PLAN-G:316). It stops where PLAN-G's G1 row
stops (PLAN-G:316): an action with no classification on record, or a definition that would need an
outcome-based choice (K-2). It also stops where a definition would need S7, O11 or a frequency
reading; §9 reports each.

Not done here: G2's K1 detection law (route A, H-1), G3's literature (X-1 to X-3), G4's measure and
frequency note, G5's synthesis. Where a definition below meets one of those, the slot is fixed and
its filling is assigned.

## 1. The fixed instance

[P] An **instance** is the tuple

    I = (rule ρ with its P-vii reading, slice form f, μ, AD-1 instance, geometry 𝒢, budget T, t_c,
         encoding per protocol, incident events, κ).

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
- **Protocol family** `𝒜_10 = 𝒜_6 ∪ {a2P, a3P, a2C, a3C}` (G1-A1; §2.4).
- **Encoding per protocol and incident events**: §2.2 and §3.2.
- **`κ`**: the map of §5, declared with `I`.

Every report carries `I`. Verdicts under different `ρ`, `f`, `μ`, `κ_det` instances (G1-A2, §5.2) or
frequency readings are reported separately and never combined (NC-γ3; U1 G6).

## 2. The program family and the protocols

### 2.1 Regions and observers, declared once for every protocol

[P] One declaration, identical for all protocols (U1:154–159):
- `Σ`: the source (carrier) region; `P_L`, `P_R`: the two path regions; `D = (D_1, …, D_n)`: the
  screen, `n` declared readout cells (OCP's two-port toy is `n = 2`, a fringe/antifringe pair,
  OCP:15); `A`: the marker region; `Z`: the setting region; `H_e`: herald region; ledgers `L`.
- Observers (AD-1(a)): `V_D ⊇ D`, `V_A ⊇ A`, `V_Z ⊇ Z`, `V_E ⊇ H_e ∪ L`. **The same four observers
  are declared in every protocol.** A protocol never changes `Obs`. The ledgers are held by `V_E`, so
  every record component of §3.1 is a function of an observer's configuration.

*Ground.* Under reading (i) of O11 a different `Obs` is a different model, and G6 forbids combining
verdicts across models (U1:243–245, :876–878). Declaring one observer family keeps all protocols in
one model without resolving O11. A marker that is "not read" is therefore held by `V_A` and omitted
from the compared record (§2.3), not moved into the hidden sector.

### 2.2 How the protocol label enters: three encodings, none selected

[P] The protocol label `a ∈ 𝒜` must enter one fixed program `g` through U1's actions. Three
encodings are defined; each is a different program, reported separately. Each has its own incident
event (§3.2).
- **E-set.** `a` is the content of `Z` at the use tick, a datum of `μ` or written by `φ` from held
  records (U1 C-SET, U1:308–327), held to `t_c`. Where `a` changes what `φ` does to the carrier
  (blocking a path; switching the marker coupling; switching the marker read), the change is a C-INT
  action of class I-sel or I-off (U1 §4.3).
- **E-prep.** `a` changes only a preparation law (for example the marker's prepared content). Each
  `a` has a declared preparation attempt, executed under a herald whose outcome is a record
  component, with the failed mass kept (U1 C-PREP, U1:264–272).
- **E-read.** `a` changes only the readout function applied to a held configuration (which partition
  of `V_A`'s configuration is reported). The protocols so encoded share one program run and one
  incident event. This is a post-processing, not an operation (OCP:49: "Passive changes of which
  column of a fixed probability table is displayed are not operations"; S-C1(b), MR★:504–507 [NP]).

*Excluded encoding.* **E-decl**: `a` changes only which regions are declared, with `φ`, `μ`, `Obs` and
the record map fixed. [A-inf, from AD-1(c)] A declaration changes no region's content, so with the
record map fixed every record law is the same for every `a`; E-decl cannot represent the protocols as
distinct laws. Two cases are not E-decl:
- a declaration that changes which cells are reported changes the record map. The laws then differ,
  but they are post-processings of one configuration law: that case is E-read;
- a declaration that changes `Obs` is a change of model under reading (i) of O11 (§2.1; §9).

A change of graph per protocol is a change of model (§9, O11).

### 2.3 The six protocols as program specifications

[P] SUBSTATE-1's six protocols (OCP:17–24), with one identical incident source and one schedule
(OCP:15). The table states what each protocol *requires*; §4 classifies.

| `a` | Protocol (OCP) | Required of the program | Compared record (subset of §3.1) |
|---|---|---|---|
| a1 | both open, no marker (OCP:19) | carrier from `Σ` through `P_L` and `P_R` to `D`; marker coupling absent (G1-A4: "'no marker' means the coupling is absent") | screen, setting, herald, loss |
| a2 | left only (OCP:20) | transfer through `P_R` to `D` removed, with that flux booked as loss (subnormalized, OCP:26) | screen, setting, herald, loss |
| a3 | right only (OCP:21) | as a2 with `L` and `R` exchanged | screen, setting, herald, loss |
| a4 | both open, marker stored, not read (OCP:22) | marker coupling engaged; `V_A`'s record omitted from the comparison | screen, setting, herald, loss |
| a5 | both open, marker read in path partition (OCP:23) | as a4; `V_A`'s configuration reported through a declared path partition `π_P` | screen, marker (`π_P`), setting, herald, loss |
| a6 | both open, marker read in complementary partition (OCP:24) | as a4; reported through a declared partition `π_C` | screen, marker (`π_C`), setting, herald, loss |

- `π_P`, `π_C` are declared partitions of `V_A`'s finitely many states, with a null value `∅` kept,
  fixed with `I` and never chosen after any screen record is seen (NC-γ1). A partition chosen because
  it sorts screen records into fringes is an outcome-based choice (K-2; NC-γ1), and, where the sorted
  subset is then treated as the incident ensemble, a selection effect (OCP:45; H-8).
- **Which-path and complementarity are tested, not defined into `π_P`, `π_C`.** The operational
  statistics of §2.4 are computed from records.
- **Timing variant.** a6-delayed: the marker read tick is later than the screen record tick. The
  screen record is then retained to `t_c` (C-RET) or the joint law is R-seq (U1:165–167; K-4).
- **Three eraser cases kept apart** (#1169 c.6891710167): a6 is *sorting* on marker outcomes.
  *Physical reversal of the marker interaction* and *recovery of a record after a period of
  inaccessibility* (the parked record) are not among the six protocols; each would be its own
  protocol, and none is defined here (PROVISIONAL on U4 §§4.2, 5.3–5.4, 6). U4 r3 §5.4 makes the
  typing of the delayed-choice erasers as Case Pk conditional on how an unread in-flight photon is
  classified under U1 G4; this note defines none of the three cases, so its content is unchanged.

### 2.4 Auxiliary protocols that the measured quantities require, adopted (G1-A1)

[A-inf, from LIT] The which-path knowledge reported in the experiments read first-hand is obtained
from **one-path-blocked runs with the marker coupling engaged and the marker read**: Schwindt 1999
obtains `K = 2L − 1` "from path-blocked counts with the analyzer in place, detector-efficiency ratio
1.11 ± 0.01, Wootters–Zurek betting strategy, optimized basis" (LIT 1.12, FULL); Ma 2013 measures
"Path probabilities … by blocking one path" (LIT 1.8, FULL). `D` is defined as a maximum of `K` over
marker measurements (`D = max{K}`, LIT 1.12, §3); the FULL-read sources report `K` for a chosen
measurement, which can lie below `D` (LIT §3). Dürr 1998's PRL abstract states "We have measured D and
V independently" (LIT 1.11, ABSTRACT; method NOT READ). OCP's a2 and a3 transmit one alternative with
no marker specified (OCP:20–21, :15), and a4–a6 block no path. So the raw-direct which-path quantity
of X-4 is not defined on `𝒜_6`. The extension needed:

| `a` | Protocol | Use |
|---|---|---|
| a2P, a3P | one path blocked, marker coupling as in a4, marker read in `π_P` | path knowledge `K_P` (below) |
| a2C, a3C | the same, marker read in `π_C` | the same statistic `K_C` for `π_C` |

Under E-read, a2P and a2C are two readouts of one marker-engaged one-path program, and so are a3P and
a3C; the extension then adds two programs, not four.

**The statistic** [P]. Fix a detected event `𝔇` in the record space: a screen detection in a declared
cell set (§5.2), together with a marker report `m ≠ ∅`. For `π ∈ {L, R}` let `b(π)` be the protocol
with only `π` open (a2P for `L`, a3P for `R`), and

    c_π(m) := L_{b(π)}(𝔇 ∧ marker report m) / (incident mass of b(π))      (κ_norm, §5.3)

for each value `m ≠ ∅` of the declared partition. Then

    K_P := Σ_m |c_L(m) − c_R(m)| / Σ_{π, m} c_π(m)        (defined when the denominator is > 0).

- *It is `2L − 1`.* With the priors `w_π := Σ_m c_π(m) / Σ_{π′,m} c_{π′}(m)`, taken from the detected
  masses of a2P and a3P at equal incident flux, and Wootters–Zurek betting (guess the path with the
  larger `c_π(m)`), `L = Σ_m max_π c_π(m) / Σ_{π,m} c_π(m)`. Since `2 max(u, v) − u − v = |u − v|`,
  `2L − 1 = K_P`. With `w_L = w_R` it is the total-variation distance between the two conditional
  marker laws. It includes the a-priori predictability: for a marker with the same conditional law on
  both paths, `K_P = |w_L − w_R| = P`.
- *Full masses kept.* `K_P` is a ratio of masses of declared events of full-mass laws (§3.2); no law
  is renormalized, and the null-report fraction `f_∅(b) := L_b(screen detection ∧ m = ∅) /
  L_b(screen detection)` and the undetected mass are reported beside it (NC-γ4). Beside `K_P` is
  also reported `K_P^∅`, the same formula with `∅` kept as a marker value (the event `𝔇` without its
  clause `m ≠ ∅`), so that a null report that depends on the path is not discarded. In check 4 below,
  with one efficiency `η` on both paths and equal detected masses, `K_P^∅ = η`.
- *Efficiency.* In raw counts, `c_π(m)` is the count at marker outcome `m` divided by that outcome's
  detection efficiency `η_m`, at equal incident flux and integration time (§5.4). `K_P` is unchanged
  by a common factor on all `η_m`, so only efficiency ratios enter, as in Schwindt's 1.11 ± 0.01. A
  model's `K_P` is computed from its own masses, with no `η`.
- *`K_C`* is the same formula with `π_C`. `K_C = P` (no knowledge beyond predictability) is necessary
  for `π_C` to be complementary; it is not sufficient: the trivial partition meets it and reads
  nothing. Sufficiency would need a statistic on a6 (conditional visibility per `π_C` cell), which G1
  does not adopt as a definition of "complementary".

**Hand checks** [A-inf, by hand].
1. *Perfect marker.* In a2P every detected run reports `m = L`, in a3P `m = R`: `c_L = (L: d_L)`,
   `c_R = (R: d_R)`, zero elsewhere. `K_P = (d_L + d_R)/(d_L + d_R) = 1`, for every `d_L, d_R > 0`.
2. *Position of the block.* Blocked runs reach no screen cell, so they lie outside `𝔇` whether the
   block sits before the marker (blocked runs carry the blocked path's mark) or after it (blocked runs
   carry `∅`). Both give `K_P = 1` in check 1. r1's statistic, normalized by incident mass with the
   blocked runs inside, gave `1/2` and `0` in these two cases (RG1 finding 2); that dependence is gone.
3. *Uninformative marker.* `c_π(m) = d_π q(m)` with one law `q`: `K_P = |d_L − d_R|/(d_L + d_R)`, which
   is 0 at equal detected masses.
4. *Inefficient perfect marker.* A fraction `1 − η` of detected runs reports `∅` on each path. Those
   runs lie outside `𝔇`; `K_P = 1` and `f_∅ = 1 − η` is reported beside it. A per-outcome efficiency
   difference enters only through the ratio correction above.
5. *NC-copy.* A marker that copies the path with no back-action has the conditional laws of check 1,
   so `K_P = 1` is reached (§7.1).

**The four added protocols, adopted** (G1-A1). `𝒜_6` is SUBSTATE-1's preregistered set. G1's protocol
family is `𝒜_10 = 𝒜_6 ∪ {a2P, a3P, a2C, a3C}`, and (γ→) and (γ←) range over it (§6). [P] Program
specifications, as in §2.3:

| `a` | Required of the program | Compared record (§3.1) |
|---|---|---|
| a2P | transfer through `P_R` to `D` removed, with that flux booked as loss (as a2); marker coupling engaged as in a4; `V_A`'s configuration reported through `π_P` | screen, marker (`π_P`), setting, herald, loss |
| a3P | as a2P with `L` and `R` exchanged | as a2P |
| a2C | as a2P, reported through `π_C` | screen, marker (`π_C`), setting, herald, loss |
| a3C | as a2C with `L` and `R` exchanged | as a2C |

[P] **Record laws and masses, in two encodings** (§3.2's definitions, unchanged).
- *All four by E-set.* Four setting values with disjoint incident events
  `𝔈_a = {the held setting record at t_c is a}`. `L_a = (ρ_a)_* L_a^full`, with `ρ_{a2P}`, `ρ_{a3P}`
  mapping `𝓒_A` by `π_P` and `ρ_{a2C}`, `ρ_{a3C}` by `π_C`. Total mass `μ(z = a)`, with the blocked
  flux, undetected runs and herald failures inside it. Four disjoint parts of `L^full`. The sum rule
  holds for each protocol against its own unread marginal (§3.3); equality of `Σ_m L_{a2P}` and
  `Σ_m L_{a2C}` is a property of the model.
- *Blocking by E-set, the read by E-read.* Two setting values, `b_L` (only `L` open, marker coupling
  engaged) and `b_R`, with disjoint incident events `𝔈_{b_L}`, `𝔈_{b_R}`. Then
  `L_{a2P} = (ρ_P)_* L^full|_{𝔈_{b_L}}`, `L_{a2C} = (ρ_C)_* L^full|_{𝔈_{b_L}}`, and likewise for a3P,
  a3C with `b_R`. Each has total mass `μ(𝔈_{b_π})`. The runs of `𝔈_{b_π}` enter `L^full` once.
  [A-inf, by hand, as in §3.3] `Σ_m L_{a2P}(s, m, ·) = Σ_m L_{a2C}(s, m, ·)` = the unread marginal of
  `L^full|_{𝔈_{b_L}}`, identically, since `π_P` and `π_C` are total on `𝓒_A`.
- E-prep does not encode blocking (§4.2: blocking by a prepared content is not classified).
- Normalization per incident particle by `μ(𝔈_a ∧ e = (a, E))`, or `μ(𝔈_a)` with no herald process
  (§5.3); in the second encoding, `μ(𝔈_{b_π})` for both reads.

[P] **`K_P` and `K_C` on them.** `c_π(m)` above is taken from `L_{b(π)}`, `b(L) = a2P`, `b(R) = a3P`,
for `K_P`, and from a2C, a3C for `K_C`, each divided by its own incident mass. In the second encoding,
`K_P` and `K_C` for path `π` are read from one full law, `L^full|_{𝔈_{b_π}}`, through `π_P` and
`π_C`, and the undetected mass beside them is the same for both. `𝔇` uses a screen detection, so
`K_P`, `K_C`, `K_P^∅` and `f_∅` are computed per `κ_det` instance (§5.2). With `𝒜_10`, `π_P` and
`π_C` have an operational test: `K_P` and `K_C` on these protocols (and `K_C = P` remains necessary,
not sufficient, for "complementary").

**On K1, the O11 stop** (§9). Blocking as a setting of one program is not available at D5's scope,
on the condition that U1's factor-set reading is verified (U2 §11.1; §4.2). A blocked transfer is
then a change of graph, hence of model (MR★:471–472 [NP]). So on K1, under the global reading, a2P,
a3P, a2C and a3C are programs of other geometries. They are compared with a4–a6 within one instance
only through the O11 stop, which is not resolved; they are reported per model and never combined.
Under the all-E-set encoding, the switch between a2P and a2C (and between a3P and a3C) is also an
E-set read switch, which on R-lin is not available at D5's scope on the same factor-set condition, as
for a5 and a6 (§4.2); the second encoding, with the read by E-read, avoids it.
`K_P` itself combines the laws of the `L`-blocked and `R`-blocked programs, two geometries, so on K1
it too is defined within one instance only through that stop. "Marker coupling as in a4" on K1 is a
property of the declared region and the fixed graph (U4 §2.1, PROVISIONAL). Under the scoped reading
these protocols take a2's and a3's standing per rule (§4.2): unsourced or not classified.

## 3. The record laws `L_a`

### 3.1 Record space

[P] For a program `g` of `I`, the complete record at `t_c` is the tuple

    r = (s, m, z, e, ℓ) ∈ 𝓡 = 𝓢 × 𝓜 × 𝓩 × 𝓔 × 𝓛,

- `s ∈ {0,1}^n`: the detection vector, `s_j = 1` when cell `D_j` registers a detection at `t_c` in the
  sense of the declared `κ_det` variant (§5.2); the full vector is kept, not only its single-click part;
- `m ∈ 𝓜`: the marker report `π_P(V_A)` or `π_C(V_A)`, including `∅`; in a1–a4, `m` is not entered
  (§2.3);
- `z`: the held setting record (E-set);
- `e`: the herald record: `⊥` (no herald process), or `(a, E)`, `(a, ¬E)` (herald for the preparation
  attempt of `a` executed or failed);
- `ℓ`: loss and attempt marks (`⊥`, `∅`; MR★:639, :910–911). A mark with no executing process is
  listed with mass 0 by specification (U1 G5, U1:184).

**The full record space** is `𝓡^full = 𝓢 × 𝓒_A × 𝓩 × 𝓔 × 𝓛`, with `𝓒_A` the finite configuration
space of `V_A` at `t_c` (AD-1(a)). It refines `𝓡` for both `π_P` and `π_C`. Each protocol `a` has a
**record projection** `ρ_a : 𝓡^full → 𝓡`: for a1–a4, `𝓒_A` is dropped; for a5, `𝓒_A` is mapped by
`π_P`; for a6, by `π_C`. `π_P` and `π_C` are total on `𝓒_A`, with `∅` among their values.

Every component is a function of an observer's configuration **held at `t_c`** (G4, U1:183). A
component first held at an earlier tick enters only if retained to `t_c` (C-RET) or carried there
(S-A6) (U1:165–167).

### 3.2 Incident events, laws and masses, per encoding

[P] Each protocol `a` has an **incident event** `𝔈_a ⊆ S`, declared with `I`:

| Encoding | `𝔈_a` | Shared by |
|---|---|---|
| E-set | `{x : the held setting record at t_c is a}` | `a` only |
| E-prep | `𝔄_a`, the declared preparation attempt for `a`: a `μ`-event of the preparation region's content at the preparation tick; the attempt label is carried in `e` and held at `t_c` | `a` only |
| E-read | `𝔈_*`, the incident event of the one program whose record is read through several projections (for a4–a6, `𝔈_* = {z = z*}` with `z*` its setting value, or `S` if there is no setting) | every protocol it encodes |

Distinct incident events are pairwise disjoint (a declared property of `I`, checked at NC-γ4).

[P] **The full law** of protocol `a` is the unnormalized measure on `𝓡^full`

    L_a^full(r) = μ( { x ∈ 𝔈_a : rec^full_{t_c}(φ^{t_c} x) = r } ),

with `rec^full_{t_c}` the declared record map onto `𝓡^full`, and **the compared law** is
`L_a := (ρ_a)_* L_a^full` on `𝓡`. Consequences:
- **Total mass** of `L_a` and of `L_a^full` is `μ(𝔈_a)`: `μ(z = a)` under E-set; `μ(𝔄_a)` under
  E-prep, with the outcomes `e = (a, ¬E)` inside it; `μ(𝔈_*)` for each protocol E-read encodes.
  Herald-failed, undetected and loss outcomes are inside it. Nothing is renormalized to the surviving
  or detected runs (G5; NC-γ4; OCP:15, :26).
- **One joint law.** `L^full := Σ_{𝔈} L^full|_𝔈`, summed over the distinct incident events of `I`,
  each once; its total mass is `μ(∪_a 𝔈_a)`. Under E-read the protocols sharing `𝔈_*` are images of
  one restriction, not disjoint parts: `L^full ≠ Σ_a L_a^full` whenever E-read encodes more than one
  protocol, and no run is counted twice.
- **Incident mass for normalization** (§5.3): `μ(𝔈_a ∧ e = (a, E))` where a preparation herald
  process exists; otherwise `μ(𝔈_a)`.
- **Ensemble object.** `L_a` is a law over `μ`, not over the analyst's sequence of configurations
  along one history (R-seq is a representation, U1 G4). The orbit-frequency reading is a separate
  object (§5.6), not a redefinition of `L_a`.
- **Level** of `L_a`: the weakest level of the actions `g_a` uses (U1:676), with every `μ`-datum
  listed.

### 3.3 Two consequences of the definitions alone [A-inf, by hand]

- **Sum rule, every encoding.** For `a ∈ {a5, a6}`,
  `Σ_m L_a(s, m, z, e, ℓ) = (ρ_{a4})_* L_a^full (s, z, e, ℓ)`, the sum over every value of `𝓜`, `∅`
  included. *Check:* `ρ_a` maps `𝓒_A` by a total function `π`, so summing over `m` recovers the
  marginal of `L_a^full` with `𝓒_A` dropped, which is `(ρ_{a4})_* L_a^full`. Both sides have total
  mass `μ(𝔈_a)`.
- **Equal marginals under E-read.** If a4, a5, a6 share `𝔈_*`, then `L_{a4}^full = L_{a5}^full =
  L_{a6}^full`, so the right side above is `L_{a4}`, and the screen marginals of `L_{a4}`, `L_{a5}`,
  `L_{a6}` are equal, each of total mass `μ(𝔈_*)`. Reads change no content (AD-1(c)).
- **Under E-set** the three protocols have disjoint incident events. The sum rule holds for each
  protocol against its own unread marginal; whether that marginal equals `L_{a4}`'s on the components
  other than `z` is a property of the model (causal order of a φ-effected read and the screen record),
  not of the definition. **Under E-prep** only the a1/a4 distinction is encoded (§4.2); the sum rule
  is the per-protocol identity above, and no equality across protocols follows.
- **Raw data.** In coincidence data the sum rule holds only up to the marker detector's efficiency and
  coincidence window (U4 §5.4; RU4 finding 8), which `κ` carries (§5.4).

These are identities of the pushforward, not results about any model. They match the coherent
benchmark's structure (OCP:24: "unconditioned screen remains (1/2,1/2)"), which is not evidence
(NC-γ2).

## 4. U1 actions per protocol, and their outcomes on record

### 4.1 Actions needed

| Action (U1 §4) | Needed by | What it must deliver |
|---|---|---|
| C-PREP | all | the incident carrier preparation, one law for every `a`; a ready screen (for `κ_det^rdy`, §5.2); for E-prep, the marker law under each attempt |
| C-SET | all (E-set) | `Z = a` with positive mass, held to `t_c` |
| C-INT | a2, a3, and the auxiliary protocols (blocking); a1 vs a4–a6 (coupling switch, E-set); a5 vs a6 (read switch, E-set only) | a setting-selected change of the carrier's or marker's transfer |
| C-REC | all (screen); a5, a6 and the auxiliary protocols (marker); herald | R1, R3, R5 under AD-1 (U1:511–517) |
| C-RET | all | screen, marker, setting and herald records held at `t_c`; a6-delayed |
| C-REN | only for sequential runs (§5.6) | ready screen and marker restored between runs |
| C-COMP | sequential runs; a6-delayed | one program, global schedule, joint hold at `t_c` |

### 4.2 Outcomes from records already classified

Global reading of P-vii (`ρ = K1 ∈` R-lin). U1's four outcomes (U1:205–213); only *not available*
is a negative under SNR-1.

| Step | Outcome on record | Source and standing |
|---|---|---|
| Carrier preparation | **unsourced** under the counting measure: "every region's marginal is uniform, so there is no ready region" | MR★:642 [NP]; U1 C-PREP first missing step (U1:300–304); hidden carriers: Gap 1 disproved at its scope (U1:283 [M-r]); visible carriers native at the D3 cost (U1:284 [M-r]); T0 not shown (U4 §3.2, PROVISIONAL) |
| Ready screen, counting-measure route (`κ_det^rdy`) | **unsourced**: same ready-region gap | MR★:642, MR★ C-3 [NP]; U1 C-REC (U1:548–549) |
| Ready screen, visible-herald route (`κ_det^rdy`) | preparation native: `D ⊆ V_D` is visible, and visible cells are prepared "Native, by a visible herald, at the D3 cost", `P(E) ≤ q^{−M}` for `M` point-prepared `q`-ary cells, exactly that under μ-G; the herald is a component of the compared record (§3.1), so it must be held at `t_c`: **unsourced at C-RET** | OA1:328, :156–160 via U1:284–285 [M-r]; U1:300–304 (first missing step: "an executed herald together with a retention process that holds it"); U1 C-RET (U1:590–599) |
| Setting `Z = a`, held to `t_c` | value derived under μ-G; held record **unsourced** (reduces to C-REC) | U1 §4.2 (iv), AW-5; MR★:637 [NP] |
| Blocking in a2, a3 and the auxiliary protocols (E-set) | **not available** at D5's scope: blocking makes the carrier's transfer through one path depend on the setting, which is setting-selected I-sel on a carrier; on affine rules "the non-translational part of the carrier's map does not depend on `c`" | D5 (OA1:176–193 via U1:487) [M-r]; U1's factor-set reading [A-inf]; counts under SNR-1 only once that reading is verified (U2 §11.1) |
| Blocking by a different graph per protocol | a different model (MR★:471–472 [NP]); not comparable within `I` | §9, O11 |
| Blocking by a prepared content (E-prep) | a prepared content enters the screen only through an offset (S-L5); an offset correlated with the carrier under `μ` is not excluded by S-L5's C-9 wording (MR★:1433–1437). Whether such a correlation, as a datum of the one `μ` of `I` conditioned on an attempt, could stand in for blocking: **not classified** | S-L5 [NP]; U4 §2.1 (PROVISIONAL); no ground on record to exclude it without reference to outcomes |
| Marker coupling switch a1 vs a4 (E-set) | **not available** at D5's scope (same class as blocking: the linear part `Φ_{AΣ}` would depend on the setting). The verdict rests on D5 and U1's factor-set reading alone | as for blocking; U4 §2.1 adds that on K1 a region "records" whenever `Φ_{AΣ} ≠ 0`, "a property of the declared region and the fixed graph" (PROVISIONAL), which bears on §9's O11 stop, not on this verdict |
| Marker preparation a1 vs a4 (E-prep) | changes the marker's prepared law only; the marker still records (`Φ_{AΣ} s_Σ` does not depend on `s_A`), so E-prep realizes a4 with another marker preparation, **not a1** "no marker" (OCP:19); the screen changes only through the offset `Φ_{DA} s_A` | S-L5, MR★:584–593 [NP]; U4 §2.1 (PROVISIONAL); CALC Theorem 1′: a marker law `ν` with `ν_t` invariant under translation by `M_t δ` masks the path completely, so such an attempt gives `K_P = P` with the coupling present, which under G1-A4 is still a4, not a1. U4 r3 §2.1 ("Beyond H-μ", [A-inf]) adds that a change of marker preparation changes `D`'s law through the background, while a declaration does not; this supports the row and changes none of it |
| Read switch a5 vs a6 (E-read) | no operation; both are projections of one full law | S-C1(b), MR★:504–507 [NP]; OCP:49 |
| Read switch a5 vs a6 (E-set, φ-effected) | **not available** on R-lin at D5's scope (I-sel) | D5 [M-r]; U1:487; factor-set condition as above |
| Marker as which-path record (C-REC for `A`) | under K1 and μ-G the native marker holds exactly the class `q_t(s_Σ) ∈ R_A/K_t`; masking complete for every path variable iff `K_t = R_A`; complete at `t ≤ 1` in every geometry; at `t = 2` it fails on a ring (A-reg) and on the native cubic torus with `5 \| q`; where it fails, a single-tick R1 record for the partition by `q_t`, with persistence, R3 and R4 open; **unsourced at (β)–(δ)** only where the declared point-path pair is masked, `M_t(x_L − x_R) ∈ K_t` (CALC Theorem 1(b); always when `K_t = R_A`, and possible with `K_t ≠ R_A`, as U4 r3 §3.2 records for Instance 1.2's mirror-related pairs); quiet marker: assumed apparatus | CALC Theorem 1, Prop. 1.4, Instances 1.1–1.2, §1.7, R-7 ([OFF], reviewed ACCEPT); U4 §3.2 (PROVISIONAL) |
| Screen record R1 | the screen's law given carrier `x` is uniform on `M^D_t x + K^D_t` under μ-G and does not depend on any marker declaration; a single-tick dependence on the carrier exists where `K^D_t ≠ R_D`; whether it does for a declared two-path geometry is G2's (H-1); persistence and the trace route **undecided** (C-4), blocked at C-3 | CALC Prop. 2.8(i) ([OFF], reviewed ACCEPT); MR★:1373–1380 via U1:532 [NP] |
| Process-produced marks (`⊥`, attempt and failure marks) | no executing process on K1; listed with mass 0 | MR★:639 [NP] |
| Retention to `t_c` | **unsourced** (no bounded readable register; O-RET) | U1 C-RET (U1:590–599); S-C4a [NP] |
| Renewal between runs | readiness relocated, never created | Lemma R, PREREG:177–187 [NP]; U1 C-REN |

*MR★:639 and OA1:328 reconciled* [A-inf]. MR★:639 states that no heralding, failure or rejection
*process* exists on K1: nothing in `φ` writes `⊥` or an attempt mark. OA1:328's visible herald is a
read of a visible configuration held at the preparation tick, and the rejected mass is its
complement; no write is involved. The two statements concern different objects and do not conflict.
What OA-1's route leaves open is the herald's retention to `t_c`.

**Per protocol, global reading** [A-inf, from the table]. Under the counting measure μ-G:
- a1 and a4–a6: **unsourced** (carrier preparation; ready screen, at C-PREP on the counting-measure
  route and at the herald's C-RET on the visible-herald route; retention). Their E-set coupling and
  read switches are **not available** at D5's scope, conditionally on U1's factor-set reading being
  verified (U2 §11.1). a1 under E-prep is not realized on K1 (PROVISIONAL, U4 §2.1).
- a2, a3 and the auxiliary protocols: **not available** at D5's scope as settings of one program, on
  the same condition; as programs of other geometries they lie outside `I` (§9); blocking by a
  prepared content is not classified (PROVISIONAL).
- **No protocol reaches *available*.**

Under a declared `μ` that supplies ready cells or a register as `μ`-data, C-PREP, C-REC and C-RET are
*available relative to `μ`* (U1:275, :524–525, :576–577). The remaining blocker for the screen is then
R1's persistence on K1, which is *undecided* (C-4; U1:532), not *unsourced*. The headline holds there
too: no protocol reaches *available*. The reason differs by `μ` and is reported with it.

**Scoped reading.** For a rule that is not affine, D5 does not apply. G_SM: operational I-sel is in
`φ`, with the request and ready precursor unsourced (U1:491, NIS2 STATUS:25–33 [M-r]); native-Y: "no
isolated available gate was found" (MR★:672–673 [NP]); the SM:104–106 graph and SM §6.5 links: not
screened here. Outcome: **unsourced or not classified**, pending #866's σ12 screen (c.6891808569 wave
1, item 4). Route E (SUBSTATE-1 continuous substates): no model is specified (OCP:58), and OCP's
native test gate (OCP:88–97) precedes any comparison; G1's definitions apply unchanged once a model is.

**Extension operations** (a detector or blocking operation an extension adds): typed into `φ`, the
criterion applies; typed into `Γ`, *requires assumed apparatus*; typed into `Obs`, **S7(a) stop**
(U1 §6.1), inherited, not reached anew (§9).

## 5. The correspondence map `κ`

[P] `κ = (κ_det, κ_mark, κ_norm, κ_freq, κ_tgt, κ_cmp, κ_scale)`, declared with `I` before any `L_a`
is evaluated (NC-γ1), identical for every protocol and for every control law (§7).

### 5.1 What `κ` acts on

`κ` acts on record laws over `𝓡` and `𝓡^full`: native `L_a`, and the control laws of §7, alike. It
reads masses of held records only. It contains no amplitude, wavefunction, `|·|²`, Kraus map, Born
probability or assigned marker overlap (NC-γ2; OCP:11, :41; PREREG:233–237).

### 5.2 `κ_det`: what counts as a detection at a cell

`κ_det` is an **explicit choice** with a verdict-level effect. Two variants are declared; each is
carried as a separate instance and reported separately, as the slice forms are (assumption-watch
marker AW-det, §10).

[P] **`κ_det^rdy` (departure from a ready value).** A detection at cell `D_j` is the event that the
readout of `D_j` held at `t_c`, read through a declared finite partition of `D_j`'s states, differs
from the class of the value to which `D_j` was prepared by the program's screen preparation (C-PREP).
A departure first held at an earlier read tick enters only if retained to `t_c` (C-RET).
- *Ground.* "The ready state the write needs is an input under C-PREP" (U1:519); MR★ C-3 (the quiet
  ready region, via U1:548). It is G1's [P] that a detection is a departure from such a ready value;
  R1 (U1:514) itself requires only that "under `μ`, the law of the held value depends on the `P`-cell
  at `t₀`". The rule names no outcome and presupposes no agreement.
- *Consequence* [A-inf]. Without a prepared screen, `κ_det^rdy` is undefined and (γ→) is *unsourced*
  for the screen, not a miss: at C-PREP on the counting-measure route, at the herald's C-RET on the
  visible-herald route (§4.2). This is H-1's dependency (PLAN-G:185–194), expressed in `κ`.

[P] **`κ_det^part` (readout partition, no ready reference).** A detection at `D_j` is the event that
the readout of `D_j` held at `t_c` lies in a declared "click" class `C_j` of a declared finite
partition of `D_j`'s states. It also meets R1 wherever the held value's law depends on the carrier.
- *Consequence* [A-inf]. It needs no ready screen. Under μ-G with no carrier dependence, the click
  mass at `D_j` is `|C_j|/|states of D_j|` (MR★:642, uniform marginals): the declared partition fixes
  a dark law. A G2 outcome "uniform screen law" is then a comparable law with setting-independent
  clicks, where under `κ_det^rdy` it is *unsourced*.
- *Both are carried* (G1-A2), as two instances `I^rdy` and `I^part` that are identical in every other
  component of `I`. Each instance is evaluated, reported and counted on its own; their verdicts are
  never combined, and neither is selected after evaluation (NC-γ3, NC-γ5). Every quantity defined
  through a detection (`s`, `𝔇`, `K_P`, `K_C`, `Δ`, the §5.7 statistics) is computed per instance.

[P] For both variants:
- *Partition.* On K1 a departure fires on any nonzero contribution, so detections are support events
  and the declared partition of `D_j`'s states carries weight. The partition, and `C_j` under
  `κ_det^part`, are part of `I` under NC-γ1.
- *Excluded.* A `κ_det` that converts a field value into a click rate or an intensity is a supplied
  detector model and fails G1 unless the conversion is effected by `φ` as a C-REC step (H-2,
  PLAN-G:195–199).
- *Multiplicity.* The whole vector `s` is kept. Runs with no detection and runs with several are kept
  with their masses (NC-γ4). Single-detection observables (X-1 discreteness, X-2 anticorrelation) are
  functionals of the joint law of `s`, not of cell marginals.

### 5.3 `κ_norm`: normalization per incident particle

[P] Counts per incident particle for protocol `a` are `L_a(· ∧ e = (a, E)) / μ(𝔈_a ∧ e = (a, E))`
where a preparation herald process exists, with the failed mass `μ(𝔈_a ∧ e = (a, ¬E))` reported
beside; with no herald process, `L_a(·) / μ(𝔈_a)`. Under E-read the denominator is `μ(𝔈_*)` (or its
herald-executed part) for every protocol so encoded. Division by the mass of detected runs is excluded
(OCP:26: "Compare raw counts, not separately normalized surviving subsets"); ratios of masses of
declared events under a stated formula (`K_P`, §2.4; `V`, §5.5) are derived quantities, not
renormalized laws. One-open protocols are subnormalized by construction. On K1, with no
process-produced herald (MR★:639 [NP]), the incident mass is `μ(𝔈_a)` unless the visible-herald route
of §4.2 is used.

### 5.4 `κ_tgt`: the target observables, singles versus coincidences

[P, from LIT] Each target datum is typed before use.

| Type | Definition | Protocols | Sources read (LIT) |
|---|---|---|---|
| T-sing | counts at a cell over all runs, no condition on any marker or partner detection | a1–a4 | X-1 sources NOT READ (G3); Schwindt 1999 `V` "with the polarization analyzer removed", background subtracted, FULL (LIT 1.12); Dürr 1998 unconditional patterns, SECONDARY, marker read status NOT READ (LIT 1.11) |
| T-coinc | joint counts (cell, marker or partner detector outcome) per fixed integration time | a5, a6 (and a1 in two-photon form) | Kim 2000 `R01`–`R04`, FULL, no visibility numbers or error bars (LIT 1.6); Walborn 2002 Figs. 2–9, FULL, no numbers (LIT 1.7); Ma 2013 counts conditioned on Det 4, FULL, with numbers (LIT 1.8) |
| T-coinc-unsorted | coincidences with the partner detected and no marker analysis | a4 in two-photon form | Walborn 2002 Figs. 3, 7, FULL (LIT C2) |
| T-block | one path blocked, marker read | a2P, a3P, a2C, a3C (§2.4) | Schwindt 1999, FULL; Ma 2013, FULL |

Rules fixed with the types:
- **No substitution between types.** T-coinc and T-coinc-unsorted data are not compared with a
  T-sing image, and conversely. Unsorted singles at the interfering detector in delayed arrangements
  are reported in none of Kim, Walborn or Ma (LIT C2, C4, C5); `κ` has **no target** for a4 in a
  delayed arrangement in the sources read, and the statement "the unsorted pattern has no fringes"
  there is a QM prediction, not a raw-direct datum.
- **Coincidence normalization.** T-coinc counts are per integration time, not per incident particle,
  and the incident flux is not reported. `κ` compares them only through quantities independent of
  that flux: shapes and contrasts within one sorted channel, and ratios across channels at equal
  integration times (Walborn's Figs. 4–5 at 800 s against Fig. 3 at 400 s are rescaled by the stated
  times, LIT 1.7).
- **Marker detection efficiency** `η` enters a T-coinc or T-block image of `L_a` as a measured
  apparatus input (E), taken from the source when reported (Schwindt's efficiency ratio 1.11 ± 0.01,
  LIT 1.12), never fitted. Where `η` is not reported, comparisons that depend on it (the sum rule of
  §3.3 against raw counts) are not made. `K_P` needs only efficiency ratios (§2.4).
- **T-block conditions.** The priors in `K_P` need the two blocked runs at equal incident flux and
  integration time. Where the source's `K` is compared, that condition is the source's; LIT 1.12 does
  not record it separately, and G3 or G5 checks it at source before a counted comparison.
- **Background.** Background-subtracted values (Schwindt, 100–400 s⁻¹; Ma's Canary data, LIT 1.8,
  1.12) are inferred quantities; `κ` compares the model's law with the background added as stated in
  the source, or does not compare. Where only the background range is stated and the signal rate is
  not, the background cannot be added at a stated value, and the comparison is not made.

### 5.5 Raw-direct, derived and inferred (§A.24)

| Class | Quantities | Use in `κ` |
|---|---|---|
| Raw-direct | cell counts; coincidence counts; path-blocked counts; integration times; a feature of plotted raw counts stated by the source (§5.7) | compared as-is |
| Derived by a stated formula from raw counts | `V` by the source's own formula over the source's own scan variable (Schwindt: maximum and minimum counts at detector 1 over a path-length scan, LIT 1.12; Ma: `V = (C_max − C_min)/(C_max + C_min)` on counts conditioned on Det 4 over a phase scan, LIT 1.8); `K = 2L − 1` from T-block counts by §2.4's formula, with the stated efficiency ratio; the additivity defect `Δ_j` (§7.1) | compared, the formula fixed in `κ`; a model image goes through the same formula over the same scan variable, and a spatial-screen image is not compared with a phase-scan `V` unless `κ_scale` declares the cell-to-phase identification (§5.8) |
| Inferred or fitted | `D` as a maximum over marker measurements (not a functional of one declared measurement's counts); background-subtracted values; Ma's corrected curve `V = 0.95√(1 − (I/0.97)²)`; visibility reductions attributed to detector size or pump divergence (Kim) | not compared |

### 5.6 `κ_freq`: probability and frequency, both readings carried (owner Q5)

[P] Performed data are relative frequencies over `N` runs in one laboratory history. Two readings are
carried; neither is adopted; every comparison is reported under both.
- **κ-ens (ensemble reading).** The relative frequency of a record value over runs is compared with
  its mass under `L_a` (§3.2), normalized by `κ_norm`. It rests on a hypothesis:
  **H-ens.** The `N` sequential runs of one history are treated as `N` independent evaluations of
  `g_a`, each from `μ`. This identifies a run sequence in one history with independent draws from
  `μ` (in effect, exchangeability across runs). κ-ens does not represent the run sequence, and the
  renewal requirement that a run sequence carries is inside H-ens, not absent (assumption-watch
  marker, sharpening H-4).
- **κ-orb (orbit-frequency reading).** The runs are successive segments of one orbit of `φ`: run `k`
  of protocol `a` is program `g_a` started at tick `t_0 + kτ`. The observable is the empirical
  frequency `F_N(x)` of a record value over the `N` runs, a function of the actual configuration `x`.
  This needs, between runs, renewal of the screen and marker (C-REN) and, for a change of protocol, a
  φ-effected setting write (C-SET; U2 CP-4's step class). OI's report under κ-orb is the **agreeing
  set** `𝒪_agree`, the set of orbits in the support of `μ` on which `F_N` agrees with the datum under
  `κ_cmp`, stated as *all*, *some* or *none* of the orbits in the support, with its `μ`-mass given
  beside it. The `μ`-mass is reported, not used as the reading's weight. **No threshold is set, no
  orbit is selected, and no weight is fixed:** this report form is accepted, with no weights chosen
  before G4 (G1-A3); the weight is G4's question.
  Selecting the orbit, threshold or weight after comparison would choose by outcome (K-2, NC-γ1).

Where the readings differ, for the slots G4 fills [A-inf, for G4 to check]:
- Full-period orbit averages are averages under the uniform law on an orbit, which differs from the
  counting law on records already on `main` (QB3:60–61, CE-8). A full period exceeds the budget of
  AD-1(f) (below recurrence, U1:232; S-L6 [NP]). Within the budget, κ-orb's object is `F_N` for
  `Nτ ≤ T`, not the orbit-uniform law.
- `F_N` is a function of the unknown actual configuration. A verdict *all* or *none* needs no measure;
  a verdict *some* is informative only with a law over configurations. So κ-orb consumes a measure
  where its verdict is *some*, and κ-ens consumes `μ` through H-ens (H-4 cross-propagation,
  PLAN-G:236–238).
- κ-orb requires C-REN explicitly; κ-ens requires none as an action, because H-ens takes the runs as
  independent draws. The frequency reading therefore changes which U1 actions a protocol needs
  (§4.1), and so can change its outcome; under κ-ens that change is carried by H-ens.

### 5.7 `κ_cmp`: the agreement rule

[P] Fixed before evaluation, and the same for every target and control. The constants below are
explicit choices of `I`, declared with it, and are fixed (G1-A5). The sensitivity set over which they
are varied is declared below, before any evaluation.

**Quantitative targets.** With `σ` the source's stated standard uncertainty: agreement iff the
`κ`-image lies within `k·σ` of the reported value, with **`k = 3`**. A source that states an interval
at another confidence level is converted to `σ` under the source's own stated error model; if it
cannot be, the target is used qualitatively only. Every comparison reports its deviation in units of
`σ`, and every report states the number of comparisons made (the trial count). A visibility is
computed by the source's own formula over the source's own scan (§5.5).

**Qualitative targets** (a feature stated in the source's text or plotted in its raw counts, with no
number; Kim's plotted curves, Walborn's figures; LIT 1.6, 1.7). The target side is the source's stated
feature. The model side is the `κ`-image, a law, classified by **local ratio statistics** in which any
envelope common to numerator and denominator cancels cell by cell.
- *Normalizers*, declared with `I` for each target channel `c`:
  - **pair normalizer**: if `c = c₁` is one channel of a declared pair `(c₁, c₂)` sorted by one marker
    read (a5's `m = L`, `m = R`; a6's two `π_C` values; Kim's `R01`, `R02`, or `R03`, `R04`),
    `n := c₁ + c₂`;
  - **one-path normalizer**: if `c` is an unsorted channel (a1, a4, or the total of a sorted pair),
    `n := c_{a2} + c_{a3}`, the subnormalized one-path sum of the same instance. For `c = c_{a1}`,
    `c/n − 1 = Δ_j/n_j`: the ratio is the local form of C0's test statistic (§7.1);
  - where no normalizer is declared within `I` (on K1 the one-path protocols lie in other models,
    §9), the qualitative feature of that channel is **not tested** in that instance, and the report
    lists it as untested.
- *Ratio and support.* `u_j := c(j)/n(j)` on the support `J := {j : n(j) ≥ ν · max n}`, with
  **`ν = 0.1`**, and `V_u := (max_J u − min_J u)/(max_J u + min_J u)`. For a pair whose channels are
  `n(1 ± v cos θ_j)/2`, `V_u = v`, the channels' own visibility.
- *Fringes present* iff `V_u ≥ v_+` and `u` has an interior strict local extremum on some maximal
  run of consecutive cells of `J`. *Fringes absent* iff `V_u ≤ v_−` or `u` is monotone on every such
  run. Neither, otherwise. **`v_+ = 0.5`, `v_− = 0.2`.** For a screen of at most two cells declared
  as a fringe/antifringe pair (OCP:15), the cells are a maximum and a minimum by declaration and the
  monotonicity clause is omitted. The image's `V_u` is reported beside every classification.
- *Fringes and antifringes* (Kim's "π phase shift"; Walborn's fringes and antifringes whose sum is
  "roughly equal" to the unsorted pattern; LIT 1.6, 1.7): the pair ratio `c₁/(c₁ + c₂)` has fringes
  present, **and** the pair total `c₁ + c₂` has fringes absent under the one-path normalizer. Where the
  one-path normalizer is not declared, only the first clause is tested, and the report says so.
- A **qualitative miss** is a classification opposite to the source's stated feature. A
  classification of "neither" yields no agreement and no miss.

**Hand checks of the qualitative rules** [A-inf, by hand]. They are used for the structure of the
rules only (NC-γ2).
1. *The review's counterexample* (RG2 N2(b)). Sixteen cells; `c₁ = (0 ×12, 4, 2, 0, 2)`,
   `c₂ = (0 ×12, 0, 2, 4, 2)`, exactly complementary. The pair normalizer is
   `n = (0 ×12, 4, 4, 4, 4)`, so `J` is cells 13–16, one run, and `u₁ = (1, 1/2, 0, 1/2)`.
   `V_u = (1 − 0)/(1 + 0) = 1 ≥ 0.5`, and cell 15 is an interior strict local minimum: fringes
   present. The total `c₁ + c₂` is constant on `J`, so against any one-path normalizer proportional to
   the envelope its ratio is constant, `V_u = 0`: absent. The pair is classified fringes and
   antifringes. r2's covariance test read it as in phase (covariance `4 > 0`).
2. *An envelope without fringes* (RG2 N2(a); Kim's `R03`, "an absence of interference", with `R04`
   showing "no significant difference ... except the small shift of the center", LIT 1.6). With
   `c₃ = c₄ = e` for any envelope `e`, `u = 1/2` on `J`: `V_u = 0`, absent. With a shifted partner
   `c₄(j) = e(j − δ)` and `e` log-concave on `J`, `e(j)/e(j − δ)` is monotone in `j`, so `u` is
   monotone: absent. For a shift small against the lobe width this applies to a `sinc²` envelope, which is log-concave on its main lobe, since
   `(log (sin x/x)²)″ = 2(1/x² − 1/sin² x) < 0` for `0 < |x| < π`, and its first side lobe peaks at
   about `0.047` of the maximum, below `ν = 0.1`, so `J` lies in the main lobe. r2's rule, `V ≥ 0.5`
   over the whole channel, read this envelope as fringes present.
3. *OCP's benchmark* (OCP:19–24, two ports). a6: `c₊ = (1/2, 0)`, `c₋ = (0, 1/2)`, `u₊ = (1, 0)`,
   `V_u = 1`: present; the total `(1/2, 1/2)` against `c_{a2} + c_{a3} = (1/2, 1/2)` gives
   `u = (1, 1)`: absent; so fringes and antifringes, as OCP:24 states. a5: `c_L = c_R = (1/4, 1/4)`,
   `u = (1/2, 1/2)`: absent. a1: `(1, 0)` against `(1/2, 1/2)`, `u = (2, 0)`, `V_u = 1`: present. a4:
   `(1/2, 1/2)`, `u = (1, 1)`: absent.
4. *The standard two-slit law*, equal slits, fringe phase `θ_j`, envelope `e`. a1 `= 2e(1 + cos θ_j)`
   against `c_{a2} + c_{a3} = 2e`: `u = 1 + cos θ_j`; with four cells per fringe period, `u` takes
   `2, 1, 0, 1`, so `V_u = 1` with interior extrema: present. a4 at full marking `= 2e`: `u ≡ 1`,
   absent. `R01 ∝ e cos²(θ_j/2)`, `R02 ∝ e sin²(θ_j/2)`: pair ratio `cos²(θ_j/2)`, present; total
   `∝ e`, absent; fringes and antifringes. Path-sorted `R03 = R04 ∝ e/2`: absent.
5. *The rules can return a miss* (countercontrol against vacuity). C0's a1 image `= c_{a2} + c_{a3}`
   gives `u ≡ 1`: absent, a qualitative miss against a source that shows fringes. An in-phase pair
   `c₁ = c₂ ∝ e cos²(θ_j/2)` gives pair ratio `1/2`: absent, a miss against a stated fringe/antifringe
   pair. A pair shifted by a quarter period, `c₁ ∝ e(1 + cos θ_j)`, `c₂ ∝ e(1 + sin θ_j)`, has pair
   ratio fringes present, but its total `∝ e(2 + cos θ_j + sin θ_j)` gives `u = 1 + (cos θ_j + sin θ_j)/2`,
   ranging over `1 ± √2/2`, so `V_u = √2/2 ≥ 0.5`, present: it is not classified fringes and
   antifringes.

**Counted misses.** A quantitative or qualitative miss is counted only for an *available* `L_a` with
every input derived, with the controls of §7 green for that comparison. Quantitative and qualitative
misses are reported separately. A disagreement of an `L_a` available only relative to a declared `μ`
is reported as a disagreement relative to that `μ`, at that scope.

*Ground.* The constants are fixed before any evaluation and use no source value. The ratio statistics
read the relative modulation that defines a fringe (OCP:28's non-additivity, in local form), so an
envelope, a single-slit diffraction lobe or a detector response common to both sides cannot stand in
for one. The gap between `v_−` and `v_+` keeps a qualitative miss to gross disagreements, and `k` with
the trial count makes the per-comparison and family-wise error assessable. None is tuned to any
target.

**Sensitivity analysis** (G1-A5) [P]. Declared now, before any evaluation; a stated set, not fitted.
- *The set.* `𝒮 = {2, 3, 4} × {0.4, 0.5, 0.6} × {0.1, 0.2, 0.3} × {0.05, 0.1, 0.2}` for
  `(k, v_+, v_−, ν)`: 81 points, each with `v_− < v_+`. The primary point is `(3, 0.5, 0.2, 0.1)`. The
  steps are equal and lie on both sides of each primary value, and no source value enters. The lower
  end of `ν` stays above the `sinc²` first side-lobe height, about `0.047` of the maximum, which
  §5.7 check 2 uses.
- *What varies.* `k` acts on quantitative comparisons only; `(v_+, v_−, ν)` act on qualitative ones
  only. So a quantitative comparison has three distinct settings and a qualitative one 27.
- *How results are reported.* Every comparison reports its **primary verdict** (at the primary
  point) and its verdict at each point of `𝒮`. It is **stable** if the verdict is the same at every
  point; otherwise the report lists the points where it differs. The quantities reported anyway, the
  deviation in units of `σ` and, for qualitative targets, `V_u`, `J` and the monotonicity of `u`, are
  enough to read every point's verdict by hand: a quantitative verdict changes with `k` exactly where
  the deviation crosses `k`.
- *What the analysis does not do.* It never replaces the primary verdict, selects no point and counts
  no miss at a point other than the primary. A counted miss (above) is a primary-verdict miss, reported
  with its stability. Every report states the size of `𝒮` beside the trial count (NC-γ5).
- *The hand checks over `𝒮`* [A-inf, by hand], with two stated conditions. Checks 1 and 3 have
  `V_u ∈ {0, 1}` and a support that does not change with `ν`: stable. Check 4 has `V_u = 1`; at
  `ν = 0.2` its support is where `sinc² ≥ 0.2`, `|x| ≤ 2.02` on the slit scale, a width of about
  `1.29 λf/a`, against a fringe period `λf/d`. So it holds `1.29 d/a` periods, enough for an interior
  extremum, **when the slit separation is at least the slit width**, `d ≥ a`: stable under that
  condition, with four cells per fringe period. Check 2: `u = 1/2` gives `V_u = 0`, absent at every
  `v_−`. For the shifted partner, `u` stays monotone only while the support lies inside both main
  lobes, which holds for a shift `δ < π − x_ν` in the sinc argument, with `sinc²(x_ν) = 2ν`: about
  `0.81` rad at `ν = 0.05`, `1.12` at `0.1` and `1.54` at `0.2`. So check 2 is stable over `𝒮`
  **for a shift of at most about 0.8 rad**. Check 5:
  the quarter-period total has `V_u = √2/2 ≈ 0.71 ≥ 0.6`, present at every `v_+`, and the C0 and
  in-phase images have `V_u = 0`, absent at every `v_−`: stable. So every hand check keeps its
  classification over `𝒮`, under the two conditions stated for checks 4 and 2.

### 5.8 `κ_scale`: lattice cells to physical positions

[P] `κ` separates **scale-free** functionals (visibility, the additivity defect, π-shifts, sum rules,
anticorrelation parameters, `K_P`) from **scale-carrying** ones (fringe spacing, envelope width). The
cell identification `D_j ↦ position` and any length scale are declared in `I`. Scale-carrying
comparisons are conditional on spatial isotropy, empirical input E4 (Main:670), and on the
observer-level wave operator, unresolved (Main:588; #914 row 12) (H-9). A length scale set from the
data it is compared with is a fitted input (R) and is reported as such.

**Phase scans.** Schwindt's `V` is taken by scanning a path length (LIT 1.12), a phase setting. On K1
a phase setting enters additively and a change of arm propagation is a change of geometry (U4 §2.1,
PROVISIONAL). A phase-scan datum therefore corresponds, on K1, to a family of geometries, not to one
program. With an `n`-cell spatial screen, the cell index plays the role of the phase, and one program
suffices. [A-inf] The only FULL-read T-sing datum with an unread marker (Schwindt) is of the
phase-scan kind; the spatial unconditional patterns with a stored marker (Dürr) are SECONDARY.

## 6. The two directions (§A.34)

For one instance `I` (reading, slice form, `μ`, `κ_det` variant and frequency reading included):

**(γ→), derivation and agreement.** For every performed protocol `a ∈ 𝒜` with a typed target:
1. every U1 action of `g_a` has outcome *available*, so `L_a` is available at a stated level, derived
   from `(φ, μ)` under a declared geometry;
2. `κ(L_a)` agrees with every typed raw-direct target of `a` under `κ_cmp`;
3. the controls of §7 are green for that comparison.

*Closed at level X* for protocol `a` when 1–3 hold, X the weakest level of its inputs. *Counted miss*
when 1 holds with every input derived, 3 holds, and 2 fails on a quantitative or qualitative target
(§5.7); it falsifies `(M, κ)` at that scope, not every observer-level extension (Code Review Rules,
no-go scope). *Unsourced* or *requires assumed apparatus* when 1 fails that way; not a negative.
*Undecided* otherwise. **What would close it:** a derivation of `L_a` from `φ` and `μ` for a declared
geometry, with sourced preparation, records and retention, followed by the comparison.

**(γ←), coverage.** For every perceived phenomenon `Φ` in the declared list (§7.3), there is a program
`g ∈ Γ_exe(M)` of the **same** `M`, `μ` and AD-1 instance, with outcome *available*, such that
`κ(L_g)` agrees under `κ_cmp` with the raw-direct target that exhibits `Φ`. **What would close it:**
exhibiting such a program per phenomenon. A negative for `Φ` needs *not available*, at a verified
scope, for every program whose `κ`-image would exhibit `Φ`; otherwise the report is *not shown*.

**Condition on the coverage result** (owner Q6). A (γ←) result counts toward AC-1's coverage half
only if its coverage credit (§7.2) is nonempty: every classical control of the declared ceiling is
separated by some listed observable. This is a condition on the result as a whole, not on each
phenomenon; where some control is not separated, the result is reported as §7.2 states.

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

Every control law is passed through the same `κ` (§5.1). Per incident particle throughout.

- **C0, fixed-path classical stochastic** (OCP:34–35). A path variable `π ∈ {L, R}` with source law
  `(p_L, p_R)`, a per-path response law `r_π` on `𝓢 × 𝓛` of total mass 1, independent of whether the
  other path is open and of the marker. Blocking `π` sends its runs to loss: a point mass `δ_blk` at
  "no detection, blocked loss". Its full laws:
  `L^{C0}_{a2} = p_L r_L + p_R δ_blk`, `L^{C0}_{a3} = p_R r_R + p_L δ_blk`,
  `L^{C0}_{a1} = L^{C0}_{a4} = p_L r_L + p_R r_R`, each of total mass 1. On the screen part (runs with
  a detection), `L^{C0}_{a1} = L^{C0}_{a2} + L^{C0}_{a3}`; the full laws do not add, since the sum has
  mass 2.
  *Test statistic:* the additivity defect per incident particle,
  `Δ_j = c_{a1}(j) − c_{a2}(j) − c_{a3}(j)`, with `c_a(j)` the mass of `{s_j = 1}` per incident
  particle, from T-sing data. C0 has `Δ ≡ 0`, since `δ_blk` has no detection. The coherent benchmark
  gives `(+1/2, −1/2)` (OCP:28).
  *Required result:* C0 **fails** the two-open comparison whenever the target's `Δ` differs from 0
  under `κ_cmp`. If the target data do not separate `Δ` from 0, the interference comparison is void
  (control not green). A failure of C0 rules out only this restricted model (OCP:35).
- **PC-wave, classical coherent wave** (C1, OCP:37–38). Classical complex field contributions
  `f_L(j)`, `f_R(j)`, a linear recombiner, intensity `|f_L(j) + f_R(j)|²`, and a supplied square-law
  stochastic detector with click rate proportional to intensity; a marker as classically correlated
  wave and marker modes. The amplitudes and the detector belong to the control, not to `κ`.
  *Required result:* **passes** the fringe statistics (`Δ ≠ 0`) and the fringe-build-up shape of X-1;
  OCP:38: "This control MUST be marked PASS for the interference statistics, not incorrectly used as
  a no-go." Its results on X-2 to X-5 are taken from G3's first-hand reads and from a stated
  construction through the same `κ`, not assumed here (§7.2).
- **NC-rep, representability** (Main:480–482, :582). The anti-complementary family: on the screen
  part, `L^{rep}_{a4} = L_{a1}` (fringes kept with a stored, unread marker), and
  `L^{rep}_{a5}(·, m = L) = L_{a2}`, `L^{rep}_{a5}(·, m = R) = L_{a3}` (full which-path on reading).
  *Required result:* realizable by the dilation with per-family actions, which shows that
  representability tests nothing.
  - [A-inf] Whenever `Δ ≠ 0` it has no E-read realization, in any model: E-read forces equal a4 and a5
    screen marginals (§3.3), while NC-rep requires `L_{a1}` against `L_{a2} + L_{a3}` on the screen
    part, which differ by `Δ`.
  - As a law family it disagrees with the T-sing unread-marker data as read: Schwindt's `V` measured
    with the analyzer removed is small at full marking (LIT 1.12, C1, FULL), where NC-rep keeps the
    a1 fringes. That `V` is background subtracted. Subtracting a constant `b ≥ 0` from both maximum and
    minimum raises `(max − min)/(max + min)` when `max + min > 2b`, so the raw visibility lies at or
    below the subtracted value. Under §5.4 the comparison at the raw level needs the background added
    to NC-rep's image at a stated value, which needs the signal rate; LIT records only the bound
    "below 5×10⁴ s⁻¹". The raw-level comparison is therefore not made in G1 (G3 reads the raw maximum
    and minimum counts).
  - NC-rep is **not** the time-indexed accessibility reading AV-t of U4 §6.3 under G1's conventions.
    AV-t ties `V` at the recombination tick to whether an observer holds the record then (U4 §6.3;
    RU4 finding 6). G1 holds a stored unread marker in `V_A` (§2.1), so AV-t predicts no fringes for
    G1's a4, the opposite of NC-rep's a4. NC-rep's a4 would correspond to AV-t only for a marker held by
    no observer at that tick, a parked-record protocol that G1 does not define (§2.3; PROVISIONAL).
    U4 §6.3 classifies Schwindt's unanalysed polarization as unheld; whether a physical unread marker
    corresponds to G1's held-and-omitted marker or to an unheld one is a correspondence question that
    LIT C5 leaves open and G1 does not decide.
- **NC-copy, non-invasive classical copy** (PREREG:237–238, CC1). A marker that copies `π` with no
  back-action: a4's screen law equals a1's (fringes intact), and in a2P/a3P every detected run reports
  its own path, so `K_P = 1` (§2.4, check 5). *Required result:* reproduced as a law with `K_P² + V² >
  1`, hence outside `D² + V² ≤ 1` (since `K ≤ D`); it separates record formation from visibility loss.
  On K1, by S-L5 [NP], every marking is of this kind (MR★:592–593, "marking is non-invasive, which is
  the CC1 kind") (PROVISIONAL, U4 §2.1; PK-2, which U4 r3 §6.1 states at fixed geometry, tick and background, so the
  statement carries that scope). [A-inf, for G2] For two point-prepared paths the K1
  marker's marginal is all-or-nothing (CALC Theorem 1(c)); whether `K_P` on K1 is then 1 or `P` also
  depends on the conditioning on a screen detection, which couples the background images at `A` and
  at `D`, and is G2's.
- **NC-noise, loss without a record** (CC7 at VER2's scope, "`V = 0` needs uniform `f`"; U4 §4.2). A
  carrier-free additive offset at `D` with no marker correlation: `V` reduced with `K_P = P` (0 at
  equal detected masses, §2.4 check 3). Under S-L5's C-9 wording the offset is from content that is
  not a function of the carrier's content and may be correlated with it under `μ` (MR★:1433–1437; RU4
  finding 11). *Required result:* distinguished from record-tied loss by `K_P` on the auxiliary
  protocols; on `𝒜_6` alone the two are not separated. (PROVISIONAL, U4 §4.2; PK-2 at fixed geometry,
  tick and background, U4 r3 §6.1.)
- **Deletion** (PREREG T8). Remove in turn the second path's transfer, the marker, the setting and
  the herald. *Required result:* the attributed effect vanishes. On K1 a removed transfer or a removed
  marker coupling is a change of geometry, hence of model (§4.2; PROVISIONAL on U4 §2.1); its deletion
  control is a separate instance, reported alongside, and comparable within `I` only through §9's O11
  stop.

### 7.2 The classical ceiling and the coverage credit set (owner Q6)

[P] **The ceiling.** `𝒦 = {C0, PC-wave, CC4, CC5}`. Each member `K` has a **scope** `dom(K)`: the
typed listed observables for which `K`'s stated construction gives a law through `κ`.
- C0 and PC-wave: every observable of §7.3, by the constructions of §7.1 and those below for X-2.
- CC4 and CC5: the marker-protocol observables within VER2's stated scopes (CC4's T1–T4 laws, CC5's
  T4 law; VER2 §§3.4, 4.4), that is, X-4- and X-5-type observables; not X-1 to X-3. G1 does not extend
  them.

On `o ∈ dom(K)`, `K`'s result is *agrees*, *established to disagree* (through the same `κ`, under
`κ_cmp`), or *unknown* (a law exists and has not been established, for example PC-wave on X-4 and
X-5, OCP:38).

[P] **Separation.** For a native result `L`, a listed observable `o` **separates** `K` when `κ(L)`
agrees with the data on `o` and either
- (s1) `o ∈ dom(K)` and `K` is established to disagree on `o`; or
- (s2) `o ∉ dom(K)`: `K`'s construction gives no law for `o`, so `K` does not reproduce it
  (separation by scope, reported as such).

An unknown result does not separate. `S(K)` is the set of observables that separate `K`.

[P] **Credit.** `L` has nonempty coverage credit iff `S(K) ≠ ∅` for **every** `K ∈ 𝒦`: for each
classical control, some listed observable separates it. The observables may differ from member to
member. Every report lists `S(K)` for each member, with each element's kind (s1 or s2). Whether
Separation by scope alone is not sufficient (G1-A6). A result whose credit needs (s2) for some member
is reported as **credit conditional on the separation of that member**, not as credited. It does not
count toward AC-1's coverage half until each such member is separated by (s1).

**Constructions for X-2** [P; A-inf, by hand]. The anticorrelation parameter is
`α := P(both outputs) / (P(transmitted) · P(reflected))`.
- *C0 at a beam splitter.* One particle per run is routed to one output by a run variable with law
  `(t, r)`, independent of everything else, and registered by that output's response law. No run has
  detections at both outputs (no dark process), so `P(both) = 0` and `α = 0`.
- *PC-wave at a beam splitter.* A field of intensity `I` per run, with any law, is split into `tI`
  and `rI`; square-law stochastic detectors, conditionally independent given the field, click with
  probabilities `ηtI` and `ηrI` (low-click regime). Then
  `P(both) = η² t r E[I²] ≥ η² t r E[I]² = P(transmitted) P(reflected)`, so `α ≥ 1`, with equality
  iff `I` is constant. The bound does not need the low-click regime: for any click probabilities
  `f(I)`, `g(I)` both increasing in `I` (for example `1 − e^{−ηtI}`, `1 − e^{−ηrI}`), Chebyshev's
  inequality for comonotone functions of one variable gives `E[fg] ≥ E[f] E[g]`, so `α ≥ 1`.

**X-3 separates no member** [A-inf, by hand]. C0's three-path probability is the sum of the
subnormalized one-path terms, so `I_3 = P_ABC − P_AB − P_AC − P_BC + P_A + P_B + P_C = 0`;
`|f_A + f_B + f_C|²` has only pairwise cross terms, so PC-wave's `I_3 = 0` when its click probability
is linear in intensity (the low-click regime); with saturating detection, for example
`1 − e^{−ηI}`, `I_3 ≠ 0` in general, and the statement is made in the linear regime only. The Born
reference also has `I_3 = 0`. X-3 bears on the exponent (#1059), not on the ceiling.

[P] **Reporting.** If `S(PC-wave) = ∅`: "interference compatible with classical coherent waves; no
quantum completion" (OCP:45). If `S(C0) = ∅`: compatible with fixed-path classical particles. If
`S(CC4) = ∅` or `S(CC5) = ∅`: compatible with that model at VER2's scope. In each case the result
does not count toward the coverage half of AC-1 (§6).

**Limitation** (assumption-watch marker AW-hyb). The rule is relative to the declared members. A
classical model outside `𝒦` that behaves like C0 on X-2 and like PC-wave on the fringe observables
would be credited. A rule stated member by member cannot exclude it without excluding the quantum
reference, since that combination is the reference's own pattern on the list. Excluding it needs a
further member or a joint observable (OCP:51), and G1 adds neither.

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
| NC-γ1: `I` (with `κ`, both `κ_det` variants and their screen partitions and click classes, `π_P`, `π_C`, `𝔇`, the encoding and incident event of each protocol, the run convention, `κ_cmp`'s constants and the sensitivity set `𝒮`, `μ`, AD-1) declared before any `L_a` is evaluated; `κ` not justified by matching Born statistics | the instance declaration is a committed file with its blob hash, and every evaluation record cites that hash and lies later in commit order; a reviewer checks that no item listed here changed after any law was evaluated |
| NC-γ2: no amplitude, wavefunction, Kraus map, Born probability or assigned marker overlap in `κ` or in a native law | §5.1; the reviewer checks each `κ` component against this list; OCP's benchmark table is used for protocol structure only |
| NC-γ3: one `M`, `μ`, AD-1 instance for all of `𝒜`; no combination across instances | every report carries `I`; §2.1's single observer family |
| NC-γ4: complete masses, no postselection | per encoding: `L_a`'s total mass equals `μ(z = a)` (E-set), `μ(𝔄_a)` with the `(a, ¬E)` mass inside (E-prep), `μ(𝔈_*)` for each protocol E-read encodes, with the shared runs entered once in `L^full`; distinct incident events are disjoint; `κ_norm` divides only by incident mass (§5.3); `K_P` is reported with `f_∅` and the undetected mass |
| NC-γ5: no C adjusted after results are known | a change of `I` after evaluation creates a new instance, committed and reported beside the old one and not replacing it; every report states how many instances were declared after the first evaluation, so that a search over `π_C`, `κ_det` or `κ` variants is visible as a trial count |
| NC-γ6: the definition of (γ←), with §7.2, is satisfiable by quantum mechanics, and no ceiling member is credited | the declared quantum reference below, used for the structure of the definition only (NC-γ2), is put in place of `Γ_exe(M)`, and each member of `𝒦` in turn; a reviewer checks each clause of (γ←) and §7.2 against them. **Status at G1: open.** Met for (γ←)'s clauses; for §7.2 at the level of the reference and control laws, conditional, since CC4 and CC5 are separated by scope only, which does not suffice (G1-A6, below); not met on the data side until G3 reads the sources for C0's separation (`Δ` or X-1) and for X-2 |

**The declared quantum reference** [EXT, standard theory, structure only]. For `𝒜_6` and X-1: OCP's
benchmark table (OCP:17–24) and the standard two-slit law. For X-2: a single excitation at a beam
splitter has zero mass of detections at both outputs, `α = 0` (PLAN-G §5.3 names Grangier–Roger–Aspect
1986: NOT READ, G3). For X-3: the Born rule gives `I_3 = 0` (PLAN-G §5.3 names Sorkin 1994 and Sinha
et al. 2010: NOT READ, G3). For X-4: Schwindt's theory curve `V² + D² = 2 Tr(ρ²) − 1` and the
pure-marker equality (LIT 1.12, §3, FULL). For X-5: OCP:23–24.

**NC-γ6 at G1** [A-inf, by hand].
- *(γ←)'s clauses* are agreement with a typed raw target under `κ_cmp` and one `M`, `μ`, AD-1
  instance. Neither fails for the reference by construction.
- *§7.2 for the reference, at the level of laws.*
  - C0: separated (s1) by the two-port fringes and X-1: the reference has `Δ = (+1/2, −1/2)` and C0
    has `Δ ≡ 0` (OCP:28, :35; §7.1); under §5.7, C0's a1 image is "fringes absent" (§5.7 check 5).
    X-4 is not counted for C0: "no fringes at any marking setting" needs C0's per-path response `r_π`
    to be independent of the phase setting of a phase scan, which C0's definition (§7.1; OCP:35, "Fix
    the screen response per path") does not state, and G1 does not add that clause (see the data side
    below). X-2 does not separate C0 (`α = 0` for both), nor does X-3.
  - PC-wave: separated (s1) by X-2, `α ≥ 1` against `0`. X-1 and X-3 do not separate it; X-4 and X-5
    are unknown.
  - CC4, CC5: within their scopes they reproduce the reference's marker-protocol laws at VER2's
    scopes, so there is no (s1); X-1 and X-2 lie outside their scopes, so they are separated by scope
    (s2).
  - So `S(K) ≠ ∅` for every member, with CC4 and CC5 separated by scope only: at the level of laws
    the reference's credit is **conditional** (G1-A6). Under (s1) alone the reference is not
    creditable on the present list.
- *The data side.* Each separating observable also needs the reference's agreement with the data.
  - C0: its data-side separation **waits on G3**. The observable C0 is defined to fail is the
    additivity defect `Δ`, which needs one-path counts at the same settings as the two-path counts;
    LIT records none for Schwindt's phase scan, and the X-1 sources are NOT READ. A clause making
    `r_π` independent of the phase setting would let Schwindt's `V` separate C0, but it would do so
    by narrowing the control's own definition beyond OCP:35, not by the test OCP fixes for C0; an
    additive C0 whose per-path response varies with arm length gives `V > 0` in a phase scan and is
    separated only by `Δ`. G1 therefore does not add the clause.
  - PC-wave: its only separating observable is X-2, whose source is NOT READ (G3).
  - So credit for the reference on the declared list waits on G3's reads for C0 (`Δ` or X-1) and for
    PC-wave (X-2), and stays conditional for CC4 and CC5 (G1-A6).
- *No member is credited.* Put any `K ∈ 𝒦` in place of `L`. On `o ∈ dom(K)`, `K` agrees with itself,
  so there is no (s1) for `K`; on `o ∉ dom(K)`, `K` gives no law, so it cannot agree with the data, and
  there is no (s2). Hence `S(K) = ∅` and `K` is not credited. For example, C0 in place of `L` separates
  PC-wave by X-2 (`α = 0` agrees with the reference's value), but `S(C0) = ∅`. The dilation family
  (NC-rep) is representable only, not available, so (γ←) excludes it before §7.2 applies.
- r2's quantifier, one observable on which every member fails, admitted none: C0 reproduces X-2, and
  PC-wave reproduces X-1 and the fringes; both have `I_3 = 0` (RG2 N1).

## 8. Dependencies

| Definition | U4 (PROVISIONAL) | S7 | P-vii reading | Slice form | `μ` | Frequency reading |
|---|---|---|---|---|---|---|
| `𝓡`, `𝓡^full`, `L_a`, incident events, masses (§3) | — | — | — | per `f` | per `μ` | κ-ens object only |
| Encodings E-set/E-prep/E-read (§2.2) | marker coupling not a setting on K1 (U4 §2.1) | — | which rule | — | — | — |
| `K_P`, `K_C` (§2.4) | — | — | — | — | — | per reading |
| §4.2 outcomes on K1 | (β), PK-2 at fixed geometry, tick and background, T0 (U4 §§2.1, 3.2, 6.1); CALC Theorem 1, Prop. 2.8 ([OFF], reviewed ACCEPT) | Obs typing of extension operations | global vs scoped | AD-1(b) per form | μ-G, or declared `μ`-data (§4.2) | C-REN only under κ-orb |
| `κ_det` (§5.2) | — | a detector typed into `Obs` | — | which slice `D_j` reads | ready screen as a `μ`-datum or visible herald | — |
| `κ_freq` (§5.6) | — | — | — | — | H-ens; the weight of κ-orb's verdict *some* | both carried |
| `κ_cmp` constants (§5.7) | — | — | — | — | — | per reading |
| `κ_scale`, phase scans (§5.8) | U4 §2.1 | — | — | — | — | — |
| NC-rep, NC-copy, NC-noise, Deletion on K1 (§7.1) | §6.3, S-L5 consequences, PK-2 (at fixed geometry, tick and background), §4.2, §2.1 | — | global | — | — | — |
| Three eraser cases (§2.3) | U4 §§4.2, 5.3–5.4, 6 | — | — | — | — | — |

## 9. Stops

- **S7.** Not chosen. Reached only as inherited from U1 §6.1: an extension's operation (a detector,
  a blocking or a read operation) typed into `Obs` gets no verdict. The `φ` and `Γ` typings are
  classified (§4.2). No G1 definition needs S7 to be chosen.
- **O11.** Not resolved. G1 avoids it by one observer family (§2.1) and by excluding E-decl. It is
  reached **conditionally** for these comparisons on K1:
  - a2 and a3 against a1, once blocking as a setting is not available (§4.2): expressible only as
    programs of other models (a different graph);
  - a1 against a4 (PROVISIONAL, U4 §2.1): with the E-set coupling switch not available and E-prep
    realizing a4 with another marker preparation, a1's "no marker", the coupling absent (G1-A4), is
    expressible only in another geometry;
  - the four added protocols `𝒜_10 ∖ 𝒜_6` (G1-A1; §2.4), which block a path, against a4–a6, and `K_P`,
    `K_C` themselves, which combine the `L`-blocked and `R`-blocked programs; and the Deletion
    control's removed transfer and removed marker (§7.1).

  Comparing those programs within (γ) needs a reading of O11 under which the models are identified,
  or a G6 exception. Neither is supplied; such programs are reported per model, never combined.
- **Frequency reading.** Not adopted (§5.6). κ-orb's report fixes no threshold, selects no orbit and
  fixes no weight; κ-ens carries H-ens.
- **Outcome-based choice.** None made. The partitions `π_P`, `π_C`, the detected event `𝔇`, both
  `κ_det` instances, `κ_cmp`'s constants, the sensitivity set `𝒮` and the encodings are fixed by target-neutral grounds and
  declared with `I`.
- **Actions with no classification on record.** For the scoped reading, the SM:104–106 graph and the
  SM §6.5 links have no recording screen here (MR★:667; U4 §4.5). Blocking by a prepared content
  correlated with the carrier under `μ` (§4.2) has no classification on record. G1 records them *not
  classified* and stops there.

G1 did not halt: every definition it was asked for is stated.

## 10. Findings and assumption-watch markers (§A.31)

**Productivity test, fixed before the walk:** an item is a gem if it is strictly stronger than the
obvious restatement and either constrains (γ) or exposes an assumption. Favourable readings were
pressure-tested: G1-F2 was re-tested under E-set and E-prep, where it does not hold across protocols
by definition, and G1-F5 was re-tested for κ-ens's hidden premise (H-ens).

| # | Finding | Check | Class |
|---|---|---|---|
| G1-F1 | The which-path quantity reported in the experiments read first-hand, `K = 2L − 1` for a chosen marker measurement, is formed from one-path-blocked runs with the marker coupling engaged and the marker read (Schwindt; Ma). None of SUBSTATE-1's six protocols has that form (a2, a3 specify no marker; a4–a6 block no path), so X-4's which-path quantity is not defined on `𝒜_6`, and `π_P`, `π_C` have no operational test there | LIT 1.8, 1.11, 1.12, §3; OCP:15, :19–24; re-verified with §2.4's statistic | NEW: an omission in the protocol set for X-4; the four protocols are added (G1-A1) |
| G1-F2 | Per encoding, the sum rule holds identically for each marker-read protocol against its own unread marginal, with total mass `μ(𝔈_a)`; under E-read, a4–a6 are projections of one full law on one incident event, entered once, with equal screen marginals | §3.3, by hand | ELABORATING: bookkeeping identities, not evidence; NC-rep is the family that breaks them |
| G1-F3 | On R-lin, blocking a path and switching the marker coupling or read, as settings of one program, are setting-selected I-sel, not available at D5's scope; a2, a3 and the auxiliary protocols survive only as programs of other models | D5 via U1:487; MR★:471–472 | ELABORATING (H-3 made precise); counts only once U1's factor-set reading is verified |
| G1-F4 | `κ_det^rdy` needs a prepared screen. On the counting-measure route (γ→) is unsourced at C-PREP; on the visible-herald route the preparation is native at the D3 cost and the first missing step is the herald's retention to `t_c` (C-RET). Either way it is unsourced, not a miss. Under `κ_det^part` no ready screen is needed, and a uniform screen law becomes a comparable law | §4.2, §5.2; MR★:642; OA1:328 via U1:284 | ELABORATING: H-1's dependency located in `κ`, with the location corrected |
| G1-F5 | Within AD-1(f)'s budget the orbit-frequency reading's object is a finite-run frequency `F_N`, not the orbit-uniform law. κ-orb needs C-REN explicitly; κ-ens needs no renewal action only because H-ens identifies the runs of one history with independent draws from `μ`. A κ-orb verdict *some* needs a law over configurations | §5.6; QB3:60–61; U1:232 | ELABORATING; assumption-watch markers H-ens and κ-orb's weight, for G4 (sharpens H-4) |
| G1-F6 | The only FULL-read singles datum with an unread marker is a phase-scan datum, background subtracted; on K1 a phase scan is a family of geometries (PROVISIONAL), while a spatial screen needs one program | LIT 1.12; U4 §2.1 | BORDERLINE: it bears on which targets one instance can be compared with |
| G1-F7 | No target in the sources read exists for the unsorted singles of a delayed arrangement; `κ` may not substitute coincidence data | LIT C2, C4, C5 | CONFIRMING (LIT's finding carried into `κ`) |
| G1-F8 | Credit is a conjunction across observables: under the member-by-member rule the quantum reference's credit at the level of laws is conditional (G1-A6), with C0 separated by the additivity defect, PC-wave only by X-2's anticorrelation (`α ≥ 1` against 0, by hand), and CC4, CC5 by scope only; X-3 separates no member in the linear detection regime; no member is credited. On the data side the credit waits on G3's reads for C0 (`Δ` or X-1) and PC-wave (X-2) | §7.2; §7.4 NC-γ6; OCP:28, :38, :51; VER2; RG2 N1 | ELABORATING: fixes which single observable on the list carries the separation from classical waves |
| AW-hyb | The ceiling rule does not exclude a classical model outside `𝒦` that is particle-like on X-2 and wave-like on the fringes; no member-by-member rule can, without excluding the quantum reference | §7.2 | assumption-watch marker; bears on AC-1's coverage half and on any C/Q finding |
| AW-det | `κ_det` is a choice with a verdict-level effect: under `κ_det^rdy` a uniform screen law is unsourced; under `κ_det^part` it is comparable, with a dark law fixed by the declared partition | §5.2 | assumption-watch marker; both carried as separate instances (G1-A2) |
| AW-ens | H-ens, the hypothesis of κ-ens | §5.6 | assumption-watch marker (H-4) |

**G1-F1 re-verified after the `K_P` fix** [A-inf]. §2.4's statistic needs the conditional marker laws
`c_π(·)` per path and the priors from the detected masses of the two one-path runs. On a4–a6 no path
is blocked, so the records carry no path label from which `c_π` could be formed; on a2 and a3 no
marker is specified (OCP:20–21) and `m` is not in the compared record. So `K` as Schwindt defines it is
not a functional of any law on `𝒜_6`, and the finding stands. Two refinements: the omission is the
marker-engaged one-path program, and under E-read the reads are bookkeeping, so the extension is two
programs (§2.4); and the corrected `D` wording (§2.4) leaves the finding about `K`, which is what the
FULL-read sources report. Dürr's "We have measured D and V independently" (ABSTRACT; method NOT READ)
is outside its scope.

**Cross-propagation.** G1-F1 applies to every OI comparison with complementarity data (D-1, AC-1's
coverage half, MR-1's T1), and its corollary that `π_P`, `π_C` lack an operational test on `𝒜_6`
applies to every X-5 comparison; on `𝒜_10` they have one (§2.4). G1-F5 and AW-ens apply to every OI comparison of a law under `μ` with
laboratory frequencies (PLAN-G:236–238). AW-det applies to every K1 detection law (G2; MR-1's screen).
For G5 [A-inf, unchecked]: under E-read every model holds one joint law of `(s, π_P(V_A), π_C(V_A))`,
so a5 and a6 are jointly representable reads, the classical-eraser class; whether X-5 under E-read is
then bounded by CC4/CC5's reach is a candidate check.

## 11. Off-`main` references traced (§A.42 item 8)

| Reference | Claim it is attached to here | Classification |
|---|---|---|
| PLAN-G at `20cdb9e5` | the objects G1 fixes, H-1 to H-10, routes, X-list | support off `main` (gap); plan not reviewed |
| U1 at `20cdb9e5` | criterion, AD-1, outcomes, C-INT classes, levels under declared `μ` | support off `main` (gap); accepted, c.6891241282 |
| U2 at `20cdb9e5` | counting conditions for the factor-set reading; CP-4 step class | support off `main` (gap); accepted, c.6891710167 |
| U4 r3 at `c3353dc5` | every PROVISIONAL entry | support off `main` (gap); accepted, c.6892563291; U4-dependent results stay conditional |
| U4-CALC r2 and its review at `20cdb9e5` | marker masking condition; the screen's coset law (§4.2); NC-copy's G2 slot; E-prep masking remark | support off `main` (gap); reviewed ACCEPT; accepted by the owner, c.6892224647 |
| LIT at `20cdb9e5` | target typing, read status, `K` and `D` definitions, G1-F1, G1-F6, G1-F7 | support off `main` (gap); reviewed |
| VER2 at `20cdb9e5` | CC4, CC5, CC7 scopes; ceiling set (§7.2) | support off `main`; accepted at its scopes, c.6891511297 |
| G1 r1 and its review at `20cdb9e5`; G1 r2 and its review at `0300c8437`; G1 r3 and its review at `b3c79f60` | the findings r2 and r3 apply; the text r4 revises | provenance |
| U4 r2 (cited by r1–r3 of this note) and the reviews of U4 r2 and r3 | superseded citations; not used | provenance |
| #1169 c.6891808569, c.6891338304, c.6891710167, c.6892224647, c.6892563291; #1305 | authorization, target, three cases, CALC's acceptance, G1 r3's acceptance and answers G1-A1 to G1-A6 | provenance and governance |

Every statement resting on an [OFF], [NP] or PROVISIONAL row carries that gap. This note is itself
off `main` and unreviewed.

## 12. Owner questions, answered, and what later units use

**Answered** by #1169 c.6892563291 (`amaybaum`, 2026-11-15T09:49:19Z). No question of r3 remains open.
1. *Auxiliary protocols.* G1-A1: "all four auxiliary protocols are added". Applied in §1 (the family
   `𝒜_10`), §2.4 (specifications, record laws and masses under both encodings, `K_P` and `K_C`, the
   O11 stop on K1), §9 and §10 (G1-F1).
2. *Detection rule.* G1-A2: "both detection-rule variants are kept, separately". Applied in §1 and
   §5.2 (instances `I^rdy`, `I^part`), §2.4 (`K_P` per instance), §9 and §10 (AW-det).
3. *Orbit-frequency report.* G1-A3: "the orbit-frequency report is accepted, with no weights chosen
   before G4". Applied in §5.6.
4. *"No marker".* G1-A4: "'no marker' means the coupling is absent". Applied in §2.3 (a1), §4.2 (the
   E-prep row: a masking marker preparation is a4, not a1) and §9. The encodings of §2.2 are
   unchanged and none is selected; E-prep cannot realize a1 under this reading.
5. *Comparison constants.* G1-A5: "the comparison constants are fixed, and a sensitivity analysis over
   a declared set is added". Applied in §5.7 (the set `𝒮`, its reporting rule and the hand checks over
   it) and §9.
6. *Separation by scope.* G1-A6: "separation by scope alone is not sufficient, so the CC4/CC5 credit
   stays conditional". Applied in §7.2, §7.4 (NC-γ6) and §10 (G1-F8). Crediting coverage
   unconditionally would need an (s1) separation of CC4 and CC5, which no observable on the present
   list supplies.

**For G2** (after the 2b review): both `κ_det` variants, `κ_norm`, the record spaces, the incident
events and the E-set/E-prep encodings; G1-F3 and G1-F4; the screen's coset law (§4.2) and NC-copy's
slot (§7.1); C0's `Δ` and PC-wave as required controls. **For G3:** the target typing (§5.4), the
raw-direct classes (§5.5), Schwindt's raw maximum and minimum counts and T-block conditions, the X-2
and X-3 sources of the declared quantum reference (§7.4), the data side of the separations in §7.2,
and PC-wave's open X-4 and X-5 entries. **For G4:** §5.6, G1-F5, H-ens. **For G5:** §6's two
directions, §7.2's ceiling and credit set, NC-γ6, §8's dependency table, and §10's E-read candidate.

Nothing here authorizes G2–G5, a calculation or any change of Issue, plan or manuscript.
