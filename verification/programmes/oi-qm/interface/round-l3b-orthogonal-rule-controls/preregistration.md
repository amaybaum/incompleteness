# Interface round L3B — orthogonal substrate-rule controls under the fixed interface I₃, and the hidden-law block: PREREGISTRATION

**Status: control plane of a native round.** This round runs under `AGENTS.md` §A.39: one pull request from `D`,
with the control plane drafted on it; execution after the owner designates `F`; as the round's protocol record, a
receipt on which `tools/v3_verifier.py --verify-round` must print `VERDICT  HOLDS`. The design is the held Level-3B
draft (`PREREG-3B-DRAFT.md`, sha256 `4ef4c775…`, written 2026-10-03 before any Level-3 computation and sealed with
the 3A package) with the owner's decisions D1–D4 of that date carried unchanged; this file fixes its anchors on `D`,
its κ sets, horizons, validation gates and cost evidence. No factor, protocol, horizon, variable or verdict rule of
the draft changes here.

## The declarations

```v3-round
round L3B
kind non-sealing
record-directory verification/programmes/oi-qm/interface/round-l3b-orthogonal-rule-controls/
```

```v3-governed-paths
record AM verification/programmes/oi-qm/interface/round-l3b-orthogonal-rule-controls/
record AM verification/receipts/L3B.json
```

The round has no execution path. Everything it produces lives in the record directory: this preregistration; the
frozen controls `controls.py` (stage C1); the instrument under `code/` (the sealed modules copied verbatim, §7.1,
and the round's own modules, §7.2); the result artifacts under `results/` and the validation and replay logs under
`logs/`; the result note. The receipt path is `verification/receipts/L3B.json`. **No manuscript, no built artifact,
no Lean module, no tool under `tools/`, no probe under `verification/lean/`, the workflow and `verification/ROADMAP.md`
change under any outcome.** Checkpoints of the resumable driver stay outside the repository.

## The objects

- **`D`** = `b7af4852b79fa3bfa90e9b5c2eca3aca6890395a`, the head of `main` after round CC-2 landed (push run
  37153338826, every job green). The corrected manuscripts at `D` are not read by this round; its inputs are the
  sealed off-repository artifacts of §0 and the exact arithmetic of its instrument.
- **`F`** — the commit carrying this file, which the owner designates; `delta(D, F)` is this file.
- **`E`** — the certified execution head, which the owner designates.
- **`Λ`**, **`Q`** — the reconciliation (if any) and the receipt commit, as §A.39 defines them.

## 0. Provenance and anchors

All inputs are sealed, off-repository artifacts of the Level-2 and Level-3A programme, cited by sha256 (first eight
hex digits) and never modified by this round:

| Artifact | sha256 | Role here |
|---|---|---|
| `record/FREEZE.md`, `record/RESULT.md`, `record/SEAL.md` (RECORD, Level 2) | `b66b1a69`, `dc759199`, `e4153402` | the frozen definitions "as RECORD": κ class IC, OBS-R, r, R4(r; G), evidence classes, certification |
| `record/fast_stageA_L2.json` | `580d4721` | Level-2 Stage A: certified table rank > 4 for every κ under RECORD's nonlinear (min 7) and majority (min 11) rules |
| `level3/PREREG-3A.md`, `RESULT-3A.md`, `LEMMA-3A.md`, `SEAL-3A.md` | `9fe88a1a`, `a7a0e870`, `6206f1aa`, `0f223781` | the interface I₃ as frozen and run; the Stage horizons; the R_LL cell's results |
| `level3/fast3_stageA_linear.json`, `fast3_stageB_linear.json`, `fast3_stageC_linear.json` | `9b88a7cc`, `48296b18`, `ceb33dc9` | R_LL: 76 ADVANCE / 67 NOT-INVASIVE at Stage A; 76/76 AT-RANK at Stage B; 3/3 C-CONSISTENT |
| `level3/layers3_linear.json`, `cc3_census.json` | `fee05255`, `729bdd5b` | G identities 143/143 and the countercontrol census for I₃ (not repeated here) |
| `level3/PREREG-3B-DRAFT.md` | `4ef4c775` | the design this file freezes |
| `ledger/SUMMARY.md`, `ledger/SUMMARY-2.md` (premise ledger, checkpoints 1 and 2) | `19f4bfad`, `407fae0b` | the axes A5, A4-S, H, interface, r |

What this round does not do: it does not bank 3A as a verification round (3A's label EXPOSED and its post-result
theorem are cited, not reinterpreted and not promoted); it does not touch any manuscript, the five deferred
correction items (R3, R9, R10, T-HT1-1, T-E-3) or any CC-2 decision; it does not open the architectural questions
(representation versus selection, the SELECT composition, LIMCLOSE-C, EO, G-layer sourcing), which belong to the
round after this one.

## 1. The question

With the interface I₃, the observer OBS-R, the measured effect r, the hidden-law class H₀ and the evidence rules
held identical across every cell, what in the substrate rule governs the rank behaviour found at Levels 2 and 3A:
linearity (A5), the absence of self-coupling (A4-S), both, or **edge-permutivity**, the property the 3A masking
argument actually uses? Edge-permutivity is a named factor of the design (D1), not an explanation offered after the
fact. Block 2 then varies the hidden law under the same interface, separately.

## 2. Held identical across every cell (every item as RECORD and 3A unless stated)

| Variable | Value | Axis |
|---|---|---|
| Rule class | second-order leaps v^{t+1} = F(v^t) + v^{t−1} mod 2, translation-invariant, radius 1; bijective for every F (A2 holds in every cell); F varies by cell (§3) | A5, A4-S, permutivity |
| Hidden-law class | Block 1: uniform product measure H₀ on (u_i, v_i), i ∈ ℤ; Block 2: H₀, H₁, H₂ of §6 | H |
| Observer | OBS-R: site-0 pair (u_0, v_0) visible, all else hidden, record external and never read by the dynamics | OBS-1 |
| Interface | I₃ = IC × {f, s, c} exactly as PREREG-3A §3: 143 κ (passive excluded) in RECORD's frozen order; letters o, i, m, f, s, c with c: (u, v) ↦ (u ⊕ v, v); alphabets: preparations {o, i, f, s, c}, effects {o, i, m, f, s, c}, generators G₃ = {i, m, f, s, c}; horizons in the word metric of {f, s, c} | interface |
| Measured effect | r = (o, outcome 1); not searched | r |
| Setting | field-neutral: exact integer count tables, probabilities in ℚ | setting |
| Preparation and effect family rules | as PREREG-3A §2 (protocols of length ≤ L_p conditioned on their record, positive weight; effects of length ≤ L_e with a singleton record event; record bits never system effects) | G-SPLIT |
| R4 definitions, certification, WELLDEF guard, evidence classes | as PREREG-3A §2 and §5: rank-basis certification (greedy mod p, exact ℚ independence and spanning); UNDER-RANK (< 4, nonterminal), AT-RANK (= 4, nonterminal), OVER-RANK (certified > 4, terminal for that κ), R4-CLOSED only by a structural theorem about the true orbit | R4-MEASURED-EFFECT |
| Horizons | Stage A (3, 3), Stage B (4, 4), Stage C (4, 5) with the Stage-C selection rule of 3A | — |

## 3. Block 1 — the rule matrix

| Cell | F | A5 | A4-S | Edge-permutive | Status under I₃ |
|---|---|---|---|---|---|
| R_LL | v_{i−1} + v_{i+1} | kept | kept | yes (both edges) | from 3A (§0); not rerun; instrument replay only (§7.3) |
| R_LS | v_{i−1} + v_i + v_{i+1} | kept | violated | yes (both edges; also centre) | **run**, Stages A, B, C |
| R_NL | v_{i−1} v_{i+1} | violated | kept | no (necessarily, §3.1) | **run**, Stages A, B, C |
| R_NS-n | v_{i−1} v_{i+1} + v_i (RECORD's nonlinear) | violated | violated | centre only | OVER-RANK at every κ by monotonicity (iii) from Level 2; positive control at three κ (§7.3) |
| R_NS-m | maj(v_{i−1}, v_i, v_{i+1}) (RECORD's majority) | violated | violated | no | as R_NS-n |
| R_5 | v_{i−1} + v_i v_{i+1} | violated | violated | yes (left edge only) | **run**, Stages A, B, C (D1) |

The permutivity column is exact (enumeration of the eight inputs; the census is validation gate V2). R_NS-n and
R_NS-m need no new sweep: G₂ ⊆ G₃ with the same κ and the same code for o, i, m, so the Level-2 table is a
sub-table of the Level-3 table at every κ and its certified rank > 4 (min 7 and 11, §0) is a lower bound that
excludes R4(r; G₃) there already.

### 3.1 Design finding, fixed before any run: the 2 × 2 is confounded with edge-permutivity

The mechanism of PREREG-3A §8 and LEMMA-3A for the linear rule's ceiling uses that F has coefficient 1 in an edge
variable v_{i±1}: every leap adds a cone-edge initial variable independent of everything observable, and hidden
correlation is masked. Linearity is sufficient for it but not what the argument uses. In the radius-1 binary class:

- a rule without the self variable is a Boolean function of two bits; permutive in one argument, it is x ⊕ h(y)
  and hence affine. So (A5 violated, A4-S kept) forces non-permutive: R_NL cannot be edge-permutive;
- a nonlinear edge-permutive rule must use the self variable, F = v_{i−1} ⊕ h(v_i, v_{i+1}) with h nonlinear; so the
  only place edge-permutivity separates from A5 is the (A5 violated, A4-S violated) cell, which the 2 × 2 fills
  with two non-edge-permutive rules. R_5 is that separation (D1).

### 3.2 The decision table (criterion once frozen; read at Stage B, cell labels of §5)

| Outcome pattern | Reading |
|---|---|
| R_LS no κ OVER-RANK, R_NL ≥ 1 κ OVER-RANK, R_5 no κ OVER-RANK | rank behaviour tracks edge-permutivity; neither A5 nor A4-S is the operative axis |
| R_LS no κ OVER-RANK, R_NL ≥ 1 κ OVER-RANK, R_5 ≥ 1 κ OVER-RANK | A5 (linearity proper) or an A5 × A4-S interaction; permutivity alone insufficient |
| R_LS ≥ 1 κ OVER-RANK | A4-S matters even for a linear, edge-permutive rule; the masking argument is wrong in its stated generality |
| R_NL no κ OVER-RANK | the masking mechanism is not necessary for a rank ceiling; new finding |

A cell with ≥ 1 κ OVER-RANK carries the label OVER (§5) whatever its other κ; "no κ OVER-RANK" is the label EXPOSED
or NOT-EXPOSED. A cell INCONCLUSIVE where a row depends on it leaves that row undecided (outcome L3B-PARTIAL, §9).
Rows are read in the order listed; the first row whose condition holds is the reading.

**Predictions (not criteria):** R_LS no κ OVER-RANK and R_5 no κ OVER-RANK (masking holds for both; left-edge
permutivity suffices); R_NL ≥ 1 κ OVER-RANK (no fresh variable; the product of the edges carries hidden correlation
into every reading, as RECORD found for its non-permutive controls). If these hold the first row is the reading.

## 4. Stages, horizons and the per-cell procedure (as PREREG-3A §4)

| Stage | κ set | L_p, L_e | Protocols per κ | Purpose |
|---|---|---|---|---|
| A | all 143 | 3, 3 | 156 × 259 = 40,404 | filter: NOT-INVASIVE and OVER-RANK |
| B | every κ advancing from A | 4, 4 | 781 × 1,555 = 1,214,455 | verdict stage |
| C | first three AT-RANK κ and the first UNDER-RANK κ (if any) in frozen order after B | 4, 5 | 781 × 9,331 | depth probe on the Stage-B preparation set |

**Advance rule A → B (criterion):** a κ advances iff it is operationally invasive at Stage A and its certified
dim C_2 ≤ 4. **Guard handling (criterion):** rank, WELLDEF, invasiveness and the dims C_k are computed for every κ at
every stage; a WELLDEF failure is recorded and gates only positive claims (AT-RANK); it never removes an OVER-RANK
lower bound and never stops a job early. The procedure is applied to each run cell of §3 independently, with the
unchanged analysis code of 3A (`analysis3.analyze`, §7.1) and the rule as the job's parameter.

## 5. Verdicts (criteria; PREREG-3A §5 verbatim in content)

**Per κ, at Stage B** (Stage C can only add an OVER-RANK, by monotonicity (ii)): NOT-INVASIVE (no domain effect e
with m·e ≠ i·e on any preparation; reported with its rank; excluded from the capacity question) · OVER-RANK
(certified table rank > 4, or certified dim C_k > 4 for some k; terminal for R4(r; G₃) at that κ) · AT-RANK (not
OVER-RANK, certified table rank = 4, dim C_3 = dim C_2 = 4, WELLDEF holds; nonterminal) · AT-RANK (unequal) (dim
C_3 = 4 but C_3 ≠ C_2) · UNDER-RANK (not OVER-RANK, dim C_3 < 4) · INCONCLUSIVE (rank certification fails, or WELLDEF
fails where an AT-RANK claim depends on it).

**Cell label** (over the 143 κ of one rule): EXPOSED (≥ 1 κ AT-RANK and 0 κ OVER-RANK) · NOT-EXPOSED (0 κ AT-RANK of
either kind and 0 κ OVER-RANK) · OVER (≥ 1 κ OVER-RANK, whatever the others) · INCONCLUSIVE (none of the above
decided, and some κ INCONCLUSIVE where the label depends on it).

No label is R4-CLOSED. R4-CLOSED for a (rule, κ) requires a written structural theorem about the true orbit
C(r; G₃) with the computation as its control; none is claimed by this round for any new cell. The 3A statement for
R_LL is cited (§0), not re-derived.

## 6. Block 2 — the hidden-law factor H (D3, D4)

Design (rule cell) × H, with the rule cells R_LL, R_LS, R_NL, R_5 and H varied as a separate factor, so that what
the rule does, what the hidden law does, and whether they interact are answered separately.

| H | Initial measure | Weight (integer) | Role |
|---|---|---|---|
| H₀ | uniform product on (u_i, v_i) | 1 | baseline; the enumerator's built-in control (V4, §7.3) |
| H₁ | v^0 a stationary two-state Markov chain along the lattice with P(v^0_{i+1} = v^0_i) = 3/4; u^0 uniform product, independent | 3^(number of equal adjacent v-pairs) | the informative variation |
| H₂ | u^0_i = v^0_i (equal time slices); v^0 uniform product | 1 on u^0 = v^0, 0 otherwise | null control |

**Scope (D4, criterion):** every (rule, H) cell with rule ∈ {R_LL, R_LS, R_NL, R_5} and H ∈ {H₁, H₂} runs all 143 κ at
Stage A (3, 3) only. There is no Stage B in Block 2.

**Per-κ labels in Block 2 (criteria):** OVER-RANK (certified table rank > 4, or certified dim C_k > 4 for some k;
informative and terminal for R4(r; G₃) under that hidden law) · NO-OVER-RANK-AT-A (invasive, not OVER-RANK: certified
rank ≤ 4 and all dims ≤ 4 at this horizon) · NOT-INVASIVE (reported with its rank and its over-rank flag) ·
INCONCLUSIVE (rank certification fails). **Conservative semantics (D4):** NO-OVER-RANK-AT-A means exactly "no
OVER-RANK detected at Stage A" for that (rule, H, κ) — never preservation of the ceiling, never AT-RANK, never a
null interaction. The cell summary is the tally of labels; no cell label of §5 is assigned in Block 2.

**Instrument.** The window simulator's exactness rests on the product measure's invariance under the leap, which
H₁ and H₂ lack. Block 2 therefore uses an exact cone enumerator (`hsim3b.py`, §7.2): with `left` leaps remaining
the state is the exact joint distribution over (u on |i| ≤ left − 1, v on |i| ≤ left) and the record string; the
first leap materializes the initial measure on that cone (2^24 configurations for the 216 Stage-A protocols with six
leaps, fewer for the rest) and every later leap only shrinks it; pair maps act on (u_0, v_0) as in RECORD; weights
are integers and every total mass is a power of two, so the common-denominator step of `analysis3.analyze` applies
unchanged. On H₀ the enumerator must equal the window simulator (V4).

**Predictions (not criteria):** under H₁ the edge variable v^0_{t+1} is correlated with v^0_t inside the observed
cone, so masking fails and certified rank may exceed 4 even for R_LL; under H₂ the edge variable still enters with
coefficient 1 and is independent, so no OVER-RANK is expected in the edge-permutive cells. Interaction reading (not a
criterion): rule × H is real for edge-permutive cells (H₁ produces OVER-RANK where H₀ did not) and absent for R_NL
(already OVER-RANK under H₀). Both are statements about these classes at this horizon only.

## 7. Instrument, validation and replay plan (criteria)

### 7.1 Sealed modules, copied verbatim

The import closure of the 3A analysis is copied into `code/` with its directory layout preserved (the sealed modules
locate each other by relative paths), and `controls.py` checks each file's sha256 against this table at every
stage:

| Path under `code/` | sha256 (first eight) | Origin |
|---|---|---|
| `record/record_sim.py` | `e499a081` | RECORD reference window simulator |
| `record/record_fast.py` | `c2c94a68` | RECORD fast evaluator |
| `quotient/rankbasis.py` | `e82e2ab9` | QUOTIENT rank-basis certification |
| `quotient/quotient.py` | `068f93ab` | QUOTIENT (imported by rankbasis) |
| `rank/lattice_rank.py` | `39173d18` | RANK (imported by quotient) |
| `rank/protocol_rank.py` | `e57e68ba` | RANK (imported by quotient) |
| `level3/record3_sim.py` | `ac812fbb` | 3A reference simulator with the letter c |
| `level3/record3_fast.py` | `455c74af` | 3A fast evaluator with the letter c |
| `level3/analysis3.py` | `efe53458` | 3A analysis: the criteria of §4–§5 as code |
| `level3/layers3.py` | `5fa200e2` | 3A G-identity checker (rule-generic) |

None of these files is modified. The 3A orchestration and replay scripts (`driver3.py`, `replay3.py`,
`replay3B_ref.py`) are not copied: they fix the rule to `linear` and the artifact names; their rule-parameterized
equivalents are written at C1 (§7.2) and call the unchanged `analysis3.analyze` with `RUN_ALL` swapped exactly as
they do.

### 7.2 The round's own modules (written at C1; sha256 recorded in the result note)

- `code/level3b/rules3b.py` — installs the extended rule function F3B into the sealed modules' namespaces at call
  time (the sealed files are not edited): `LS`, `NL`, `R5` added; `linear`, `nonlinear`, `majority` delegated to the
  sealed function. Exact permutivity, affineness and centre-use census (V2).
- `code/level3b/hsim3b.py` — the cone enumerator of §6, with `run_H` (one protocol) and `run_all_H` (prefix-shared trie,
  as `record_fast.run_all`).
- `code/level3b/analysis3b.py` — job lists per cell and stage (the advance and Stage-C rules of §4 applied to the cell's
  own artifacts), the Block-2 label mapping of §6 on `analysis3.analyze`'s record, artifact assembly in frozen job
  order with the 3A serialization.
- `code/level3b/driver3b.py` — resumable orchestration (per-κ checkpoints outside the repository; `imap_unordered`;
  assembly when every job has a checkpoint), as `driver3.py`.
- `code/level3b/replay3b.py` — the replays of §7.3 on the reference simulator (`record3_sim.run3`) and, for Block 2, on
  `run_H` and on the independent brute force, each compared field by field with the artifact record.
- `code/level3b/validate3b.py` — gates V2–V5 and V7, with the brute-force cone reference used by V5 and V7.
- `controls.py` — §7.1 hashes; the presence and `OK` lines of every gate's log; artifact completeness (143 records per
  Stage-A and Block-2 cell, label strings in the frozen sets); the Stage-B job list equal to the advance rule applied
  to the cell's Stage-A artifact and the Stage-C selection equal to §4's rule applied to its Stage-B artifact; the
  decision-table row recomputed from the artifacts; the Block-2 tallies recomputed. `--check E` must pass at `E`.

### 7.3 Gates (each a criterion; its log is a record file; a failed gate halts the dependent item)

| Gate | Content | Required result |
|---|---|---|
| V1 | §7.1 hashes | all ten equal |
| V2 | rule census: A5 (affineness), A4-S (centre use) and permutivity for the six rules equal the columns of §3; the two-variable lemma of §3.1 (every two-variable Boolean function permutive in some argument is affine, 6 of 16) | equal |
| V3 | `record3_fast` = `record3_sim` on LS, NL, R5: 180 random protocols (seed 3, lengths ≤ 3 + 3), four κ | 0 mismatches |
| V4 | `hsim3b` on H₀ = `record3_sim` on 150 random protocols over the six rules (seed 3), and = `record3_fast` on the full Stage-A protocol set (40,404) for κ ((0,1),(0,1)), ((1,3),(0,2)), ((2,0),(3,1)) under `linear` and `R5` | 0 mismatches |
| V5 | `hsim3b` on H₀, H₁, H₂ = independent brute-force cone enumeration (explicit initial configurations, explicit time stepping; `validate3b.brute`) on 54 random protocols with ≤ 3 leaps (seed 3), rules `linear`, `R5`, `NL` | 0 mismatches |
| V6 | R_LL instrument replay: Stage-A records for the κ at positions 0, 18, 36, 54, 72, 90, 108, 126, 142 of the frozen order and for ((0,1),(0,1)) recomputed with the copied instrument equal the sealed 3A entries (`9b88a7cc`) field by field | 10/10 MATCH |
| V7 | OVER-RANK controls: R_NS-n and R_NS-m at positions 0, 71, 142, Stage A | each certified rank > 4 (OVER-RANK) |
| V8 | per run cell (R_LS, R_NL, R_5): Stage-A replay on the reference simulator for the nine positions 0, 18, …, 142 plus, after the output exists, the first κ in frozen order of each verdict class not yet covered | all MATCH |
| V9 | per run cell: Stage-B replay for κ ((0,1),(0,1)) if it advanced, else the first advancing κ in frozen order, reference table in resumable chunks, then the unchanged `analyze` | MATCH (skipped only if no κ advances, recorded) |
| V10 | per run cell: G identities (G2 forgetful sum, G3 normalization, G3 trailing idle) on all 143 κ at the Stage-A horizon | 143/143, 143/143, 143/143 |
| V11 | per Block-2 cell: at positions 0, 71, 142, the trie path `run_all_H` equals the per-protocol path `run_H` on the full Stage-A set, and equals the brute force on the 40 Stage-A protocols with ≤ 3 leaps that come first in lexicographic order; the H₀ record of the same κ under the enumerator equals the window-simulator record (3A's for R_LL, the Block-1 artifact for the other cells) | all MATCH |
| V12 | byte-identical rerun: Stage A of R_5 rerun after every other stage; the artifact's sha256 unchanged | equal |

V1–V5 run at C1 before any result run. V6 and V7 run at the start of S1. V8–V10 run in S1 after the cell's
artifacts exist. V11 runs in S2. V12 runs last in S2.

## 8. Execution order and stages

The order is fixed: **fixed interface → orthogonal rule controls → hidden-law block.** Every execution commit is a
single-parent child of its predecessor from `F`.

- **C1** — `code/` (§7.1 copies, §7.2 modules), `controls.py`, and `logs/` with V1–V5. No result artifact.
- **S1 (Block 1)** — in this order: V6, V7; Stage A for R_LS, R_NL, R_5 (all 143 κ each); Stage B for each cell's
  advancing κ; Stage C for each cell per §4; V8, V9, V10; artifacts `results/stage{A,B,C}_<cell>.json`,
  `results/layers_<cell>.json`, `results/controls_RNS.json`, logs. One or more commits; a commit that completes a
  stage carries that stage's artifacts and logs only.
- **S2 (Block 2)** — Stage A for the eight (rule, H) cells of §6, all 143 κ each; V11; V12; artifacts
  `results/H_<rule>_<H>.json`, logs.
- **S3** — the result note: every tally, the decision-table row, the Block-2 tallies, the gate results, artifact
  sha256s, module sha256s, timings. Candidate `E`.
- Repairs between stages may touch only orchestration (the driver's checkpointing and assembly, the logs' format) or
  `controls.py`'s reporting; no criterion, horizon, κ set, label rule or sealed module changes. A gate that fails is
  not repaired: the dependent item is halted and the round records it (§9). Any failure of the release gate at `E`
  is a halt, not a repair.

## 9. Outcomes

- **`L3B-READ`** — every run cell of Block 1 carries a label of §5 that is not INCONCLUSIVE, the decision table has a
  determined row, every Block-2 cell is complete with its tally, and every gate V1–V12 passed.
- **`L3B-PARTIAL`** — one or more items halted under §8 (a gate failed, a cell INCONCLUSIVE where a row or a tally
  depends on it); the completed cells, the gates that passed, the row if determined, and each halted item with its
  reason are listed.
- **`L3B-HALTED`** — anything else; the round halts under the specification's `S12`.

No outcome changes correctness bands: Block 1 attributes a finite-horizon rank behaviour to rule properties within
the radius-1 binary second-order class under I₃ and H₀; Block 2 measures the hidden-law factor at Stage A. The
result note states "bands unchanged".

## 10. Interpretation limits (stated in advance)

- Not evidence about any other interface, observer (OBS-M, OBS-C), measured effect or hidden-law class than those
  run; Block 2's negative results are stated for H₁ and H₂ as defined, at Stage A, only.
- Not a QM test: no cell outcome bears on strict convexity, continuous reversible transitivity, composites or any
  Q-layer premise; a 4-dimensional sector is a pair-marginal space whose reachable states under I₃ form a finite set.
- Not a search for r; not a search for a rule: the six F of §3 are the whole class run.
- R4-CLOSED is not a label of this round for any cell; the 3A theorem for R_LL is cited as 3A states it.
- Edge-permutivity is a property of F as a Boolean function; the decision table attributes rank behaviour to it within
  this class and says nothing about rules of larger radius or alphabet.

## 11. Hazards and design evidence (measured before this freeze, on the sealed instrument and the prototype modules)

- **Instrument identity.** The copied closure is exactly the ten files `analysis3` and `layers3` import from the
  sealed directories (measured by import tracing); their hashes are those of §7.1.
- **Prototype validation** (`rules3b.py` sha256 `a47f91de…`, `hsim3b.py` `a587b8c5…`, `validate3b.py` `11f09619…`,
  2026-10-04): V2 census equals §3 (6 of 16 two-variable functions permutive in some argument, all affine); V3 180/0;
  V4 150/0 random and 40,404/0 on the full Stage-A set for κ ((0,1),(0,1)) under `linear`; V5 54/0 over H₀, H₁, H₂.
  The C1 modules are these files or revisions that pass the same gates; their final hashes go in the result note.
- **Cost.** Window simulator, Stage-A set, one κ: 5 s; enumerator, same set, one κ: 32 s (H₀), 22 s (H₁); rank
  certification per Stage-A κ ≈ 10 s (3A: 143 κ in 6 min on 4 cores). Block 1: Stage A ≈ 6 min per cell; Stage B
  ≈ 1.5 h per cell on 3 workers if 76 κ advance (3A measurement); Stage C ≈ 1 h per cell for 3 κ. Block 2: 8 cells ×
  143 κ × ≈ 40 s ≈ 13 core-hours, ≈ 3.5 h on 4 cores. V10: ≈ 1 h per cell (3A). Total ≈ 12 h wall, run in resumable
  checkpointed stages; the Stage-A protocol multiset by leap count is 1600 / 6800 / 12136 / 11600 / 6252 / 1800 / 216
  for T = 0 … 6, so the 2^24 materialization occurs for 216 protocols per κ and is shared through the trie.
- **Harness limit.** Background jobs stop at 2 h; every sweep is checkpointed per κ (as 3A amendment 2) and resumes
  without loss; the result note records the number of resumptions.
- **Memory.** Measured peak RSS of the prototype enumerator on the 216 six-leap protocols of one κ: 4.55 GB (the
  per-site bit arrays of the 2^24-row cone are materialized at once in the first leap); the machine has 15 GB and
  4 cores, so the driver runs Block 2 with at most 2 workers unless the C1 revision of `hsim3b.py` lowers the peak
  (then with at most 3), and Block 2 takes ≈ 6.5 h on 2 workers; the total becomes ≈ 15 h wall.
- **Monotonicity (iii) for the controls.** Level-2 certified table rank is > 4 at every κ for both R_NS rules (§0), so
  V7 is a positive control of the pipeline, not a measurement.
- **Gate steps.** The round adds files only under its record directory: no manuscript-reading step, the coverage
  ledger, the census registry, the workflow and the probes are untouched; `duplicate_check` reads this file and the
  result note, so neither repeats a paragraph within itself.
