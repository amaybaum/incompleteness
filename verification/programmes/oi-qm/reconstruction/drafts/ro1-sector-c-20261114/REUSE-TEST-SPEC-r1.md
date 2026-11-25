# REUSE-TEST-SPEC, r1: a two-sided reuse test with one wing held and the remote wing varied

**Status: paper-only design specification; r1 unreviewed.** It specifies a performed experiment that
would supply the raw-direct data (§A.24) that U3's agreement half asks for (`S3-U3-r3.md` §10.3,
owner question 4). It is a design document only. It adopts no premise, extension E or sector
condition C, chooses no apparatus, authorizes no execution and runs no computation. Nothing in it is
evidence. Every statement attributed to OI is a consequence of the lemmas L-2 or L-3 of U3 §5 ("proved
as stated, at their stated hypotheses", #1169 c.6893058127), conditional on those hypotheses, or of the design aids Q-2 and Q-3 of Appendix A, which are
unreviewed hand derivations [A-inf] and are marked wherever they are used.

**Authorization.** #1169 c.6893331779 (`amaybaum`, 2026-11-15T11:00:45Z), "Proceed as suggested",
item 2: "**Reuse test design:** a paper-only specification of the missing two-sided reuse test. In
it, one wing holds its setting while the remote wing varies, and per-event records are kept so both
RR-1 forms can be evaluated. It is a design document only, with no execution." Same record: "Each
unit gets an independent review before it is presented." "**Not authorized:** execution,
computation, merges, manuscript edits and new premises. Physical source remains **NOT PASSED**."

**Owner records this note builds on.**
- #1169 c.6892563291 (`amaybaum`, 2026-11-15T09:49:19Z): U3 r2 accepted, "L-2 and L-3 stay proposed
  lemmas that need a dedicated review"; U3 Q1: "the coverage target is the perceived quantum
  phenomena, with one fixed finite observer family per model"; U3 Q3: "side channels are counted
  operationally"; U3 Q4: "the performed experiments that use one source twice are read first-hand".
- #1169 c.6893058127 (`amaybaum`, 2026-11-15T10:35:17Z): U3 r3 accepted ("L-2 and L-3 are proved as
  stated, at their stated hypotheses"; "Every use of L-2 or L-3 in sector-C work stays conditional on
  their hypotheses"); reuse literature r2 accepted ("no single performed experiment meets U3 §10.3's
  agreement condition. None varies the remote setting while one wing holds its own, with records
  published"; "U3's agreement half, owner question 4, therefore stays open"); RR-1 reading: "both
  register forms are kept, RR-1(F) (fresh-output) and RR-1(R) (same-register). Each is assessed
  separately".

**Writer:** Claude. **Review:** an independent non-author review before the note is presented.

**Inputs, at exact objects.** Branch `research/ro1-sector-c-1169-20261114` at
`6ab9515dec3d54ad90058bfec0d24c49c0e78d73`, directory
`verification/programmes/oi-qm/reconstruction/drafts/ro1-sector-c-20261114/`, **off `main`**:
- `S3-U3-r3.md`, blob `77b815b4cffd0c2d11e62c8a654d13a04e35a97c` (owner-accepted); cited U3;
- `LIT-REUSE-r2.md`, blob `291abebffe6693c14407848215c3d1a62361860f` (owner-accepted); cited LIT;
- `RR1-REGISTER-BRIEF-r1.md`, blob `953c6f58a499698d695b9b973a103f9fa1bffc50` (recommendation
  adopted by owner decision); cited BRIEF;
- `S3-U1-r5.md`, blob `68983f8666df0ca6c26ec4b9ec00d0a9e4072f67`; cited U1;
- `S3-U2-r4.md`, blob `1bcb9e1727cda229f8d6edd3c913ad7b520218e1`; cited U2;
- `REVIEW-U3-L2-L3.md`, blob `3a81d18dbaaeb77e32be46948723f469d2f7f864`; cited LREV.

On `main` (the branch head contains `main` at `7ac74a4b`): TSI,
`verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/two-system-interface.md`, blob
`65db5a7caf70091cffc1478001badf5f12be8313`, at [NP] standing as in U3 §9; `papers/Main.md` at the
lines U3 cites.

**Method.** Reading and hand reasoning only. The quantum predictions of §7 are standard Lüders
calculations for local instruments on `|Φ⁺⟩`, re-checked by hand [A-inf]; the projective case is
TSI (1) and (9). Appendix A gives two hand derivations, Q-2 and Q-3, used only as marked. The
sample-size figure of Appendix B is an order-of-magnitude hand estimate. No literature beyond LIT
was read for this note; every apparatus statement attributed to a paper is LIT's record of it.

**Labels.** As in U3: **[M]**, **[M-r]**, **[NP]**, **[OFF]**, **[A-inf]**. **[DES]** marks a design
choice made here, open to review. OI-attributed statements carry "conditional on L-2", "conditional
on L-3", "conditional on Q-2" or "conditional on Q-3" with the hypotheses named.

***

## 1. The question, and why no performed experiment answers it

U3 §10.3 states its agreement half as conditional on "a performed experiment that measures one
entangled source twice per wing, with a setting change between the uses, and whose raw complete
local-history records show setting-independence", and, for L-3, "repeatability at repeated settings
on both wings". The two lemmas compare specific policy patterns, where a policy `(s₁, s₂)` is one
wing's settings at its first and second use (LIT G3, G4):
- **L-2's comparison, (k3).** Alice holds `(x, x)` while Bob's policy is `(0, 0)` or `(0, 1)`; and
  the mirror pairs, Alice `(0, 0)` or `(0, 1)` while Bob holds `(y, y)`. What is compared is the law
  of the holding wing's complete two-use history across the remote policies.
- **L-3's comparison, (k3′).** Alice holds `(x, x)` while Bob's first setting varies, `(0, y₂)`
  against `(1, y₂)` for one fixed `y₂`; and the mirror pairs. With a projective first use, the
  holding wing's outcome repeats.

LIT's findings at the papers-read scope: two experiments measure both wings twice, Zhu et al. 2022
(photons; the two wings' setting indices matched) and White et al. 2016 (transmons; one fixed
configuration) (LIT R-1); none realizes (k3)'s or (k3′)'s pattern (R-2, R-3); per-event records of
both uses exist on one reused wing in Mao et al. 2022 and per shot in White et al. 2016 (R-4); the
only published raw dataset is single-system (Leupold et al. 2018), with stated exclusions (R-5); the
agreement condition is met by no single experiment read (R-6). Choi et al. 2020 was read in abstract
only.

The experiment below is the smallest one, in apparatus and in setting choices, that realizes both
patterns on both wings with per-event fresh-output records (§4.3 gives the reasons it cannot be made
smaller).

## 2. The design in brief

- One entangled pair per event, ideally `|Φ⁺⟩`, from a source whose event marker (herald or trial
  clock) does not depend on the settings.
- Two wings, Alice and Bob. Each measures its own system **twice**, with a binary setting at each use,
  chosen per event by a local random source: four random bits per event, `(x₁, x₂, y₁, y₂)`, each fair
  and independent. All sixteen joint policies occur, so every holding wing meets every remote policy.
- Settings are the CHSH settings: on each wing the two axes are Bloch-orthogonal, and the two wings'
  axes are at the CHSH angles (TSI (1)).
- **Arm P (required):** both first uses projective and nondestructive, second uses projective.
- **Arm W (secondary):** first uses unsharp, of declared sharpness `η_A, η_B`, second uses projective.
- Per event, each wing records both outcomes as separate records (fresh-output form, RR-1(F)), with
  `⊥` for any failure, plus settings, timestamps and raw detector data. The same-register record of
  RR-1(R) is computed from them.
- The complete per-event dataset, all attempts included, is published.

## 3. Source and platform options

Each option is assembled from apparatus LIT records. Each needs elements that no paper read combines;
those are listed as additions. No option is chosen here. [DES]

| | P-1: trapped ions | P-2: time-tagged photonics | P-3: superconducting qubits |
|---|---|---|---|
| Apparatus on record (LIT) | Leupold et al. 2018: one ⁴⁰Ca⁺ ion, 53 million sequential QND projective measurements, settings "chosen in real time by a quantum random number generator, latency below 50 µs", repeatability "above 99.6 %", raw dataset public (LIT §1.12). Kirchmair et al. 2009: two ⁴⁰Ca⁺ ions in one trap, sequential QND measurements by mapping and fluorescence detection, each outcome recorded per run | Mao et al. 2022: per event, "one of the four single-photon detectors per pulse corresponds to exactly one of the four outcome combinations (b_k,1, b_k,2)"; "All photon detection events are time-tagged"; first use an unsharp Sagnac CNOT with a path meter of strength `η` (LIT §1.8). Zhu et al. 2022: both wings of one singlet pair used twice (LIT §1.9) | White et al. 2016: two transmons in the singlet state, each with an ancilla; ancilla measurement of strength `φ ∈ [0, π/2]`, projective at `φ = π/2`; per-shot readout of all four qubits (LIT §1.10) |
| Pair source | entangled pair of ions: in one trap (P-1a, Kirchmair's geometry) or in two traps (P-1b). A two-trap source is not among the papers read; its availability is not established here | SPDC polarization pairs (all photonic papers read) | the White chip |
| First use, arm P | fluorescence detection, nondestructive and repeatable as in Leupold; the outcome is a classical record before the second use | the path-meter coupling at full strength; the outcome is the path, read at the final detection | ancilla measurement at `φ = π/2` |
| First use, arm W | an ancilla-mediated partial measurement (a variant of Kirchmair's mapping); not among the papers read | Mao's coupling at `η < 1` | White's ancilla at `φ < π/2` |
| When the first record is held | before the second use (classical fluorescence record) | at the end (deferred readout) | at the end ("all four qubits are read out") |
| Additions not in the papers read | the two-wing, two-use schedule with per-use random settings on both ions; for P-1b, the two-trap source | the coupling and four-detector readout on **both** wings; per-pulse fast setting switching on both uses (Mao set wave plates per acquisition) | per-shot random settings on both uses (White ran one fixed configuration); raw binary readouts without calibration rescaling (White's ancilla correlators were rescaled) |
| Detection loophole | none expected for fluorescence detection (stated as an attribute to be measured, C-9) | open unless detection efficiency is high; fair sampling otherwise | none stated by White ("near unit detection efficiency"); readout assignment error is part of the record |
| Locality | P-1a: open. P-1b: open unless the separation exceeds `c` times the measurement window (§9) | can be enforced at laboratory separations if the window is short (§9) | open ("such an interaction cannot be ruled out here", White) |
| Reachable tier (§8.4) | T-B (P-1a, P-1b); T-A only if P-1b also enforces locality | T-C with fair sampling; T-A with high efficiency and enforced locality | T-B |

[A-inf] The order of first-record holding differs across platforms. The decision rule (§8) uses only
the records at the comparison tick and does not depend on it. It is reported (§6) because U3's C-RET
against R2 table (U3 §7) and LREV R3's readback realization concern a first record that exists before
the second use; P-1 supplies that as a raw-direct fact, P-2 and P-3 do not.

## 4. Setting schedules

### 4.1 Primary schedule S-R: full factorial, per event, per use [DES]

- At each event `e`, Alice draws `x₁, x₂` and Bob draws `y₁, y₂`, four fair bits, independent of each
  other, of the event marker, of the event index and of all earlier records.
- Each draw uses its own local random source and is recorded raw (§6).
- The second setting of each wing is drawn after that wing's first use is complete. The lemmas allow
  a preloaded second setting ((k3): "a preloaded per-use slot … serves equally"); drawing it later
  removes the prefix route TSI uses (TSI §2: "the program slots may be loaded initially") and makes
  control C-2 meaningful.
- Every joint policy `(x₁x₂, y₁y₂)` has probability 1/16. Every holding policy of each wing, `(s, s)`,
  meets all four remote policies.

### 4.2 Fixed constants, declared before data

- `y₂* = 0` and `x₂* = 0`: the fixed remote second setting of L-3's (k3′) comparison. The full
  factorial also supplies `y₂* = 1` and `x₂* = 1`; they are reported, not used in the rule. [DES]
- The family-wise error level `α` and its split between tests (§8.1).
- The `⊥`-assignment rule (§6.3) and its declared alternatives.
- The event-marker rule (herald, or trial clock with its period).

### 4.3 Why the experiment cannot be smaller

- **One-sided reuse does not suffice.** Which wing carries the remote dependence is
  realization-specific. In SEL-EXCL-1's `T`, `a = r` does not depend on `y` and `b = r ⊕ xy` depends
  on `x` (U3 §5.1, checks against the instances), so the signal appears only when Bob holds and Alice
  varies. L-2's conclusion and L-3's (b) bound the two wings together (Appendix A), so both wings must
  hold in some events and vary in others.
- **Two uses per wing suffice.** L-2 and L-3 are two-use statements.
- **One binary setting per use suffices.** The CHSH precondition needs two settings per wing; both
  comparisons use the same two.
- **The same-register form does not need its own register.** BRIEF §4: "the (R) record is a function
  of the (F) record", so an (F)-form experiment "checks the agreement half for both forms".
- **A blocked schedule saves little and costs measurement independence.** The joint policies (k3)
  and (k3′) need are eleven of the sixteen [A-inf]. Running only those, or running them in blocks,
  removes five policies and introduces setting drift across blocks, the failure LIT R-4 records for
  per-acquisition designs ("we are effectively using different states for each measurement",
  Padovan et al.). S-R is kept.

## 5. First-use strength

| Arm | First use | Second use | What it serves | Lemma coverage |
|---|---|---|---|---|
| P (required) | projective, nondestructive | projective | L-3's repeatability; L-2's comparison; the full two-use law (1)×(9) | L-2 (k1)–(k5); L-3 (k1) or its dilation, (k3′), (k4′), (k5′), with `Θ` identifying the program with the two-use Lüders experiment |
| W (secondary) | unsharp, sharpness `η_W ∈ (0, 1)` per wing, declared | projective | L-2's comparison at a different instrument; a strength scan as a countercontrol for crosstalk (C-6) | L-2 only. L-3 "says nothing about non-repeatable instruments, which impose (c) without the repeatability part" (U3 §5.2, Scope) |

- In arm W the first-use CHSH value is `2√2 η_A η_B` for unsharp Lüders instruments (§7.1); the L-2
  comparison needs it above 2, so `η_A η_B > 1/√2`. A scan that includes points below that threshold
  serves as a countercontrol only (C-6).
- The unsharp instrument is declared by its Kraus pair before data, for example
  `K_± = √((I ± η σ_n)/2)`. The predictions of §7.1 for arm W are for that pair.

## 6. Per-event records

### 6.1 Schema (fresh-output form) [DES]

One row per event marker, kept whether or not anything is detected.

| Field | Content |
|---|---|
| `e` | event index, consecutive, with no gaps |
| `t_e` | event-marker time; herald value `h_e ∈ {0, 1}` and the herald's raw signal where the source is heralded |
| per wing `W ∈ {A, B}`, per use `i ∈ {1, 2}` | raw random-source output; setting `s_{W,i}`; time the setting was chosen; time it was applied |
| per wing, per use | outcome `w_{W,i} ∈ {0, 1, ⊥}`; registration time; raw detector data (photon counts and threshold for P-1; channel and time tag for P-2; readout signal and threshold for P-3) |
| per wing | instrument arm (P or W) and declared sharpness; calibration identifier |
| flags | every abort, purge, timeout or exclusion, with its trigger, at the event where it happened |

### 6.2 The two register forms

- **RR-1(F):** each wing's complete two-use history is the pair `(w_{W,1}, w_{W,2})`, with its
  settings, held at the comparison tick.
- **RR-1(R):** each wing's register is `w_{W,1} ⊕ w_{W,2}`, set to `⊥` if either entry is `⊥`. It is
  computed from the (F) record and is assessed separately, as the owner decision requires.
- [A-inf] No outcome of this experiment can favour one form over the other as a claim about nature
  (BRIEF §4). Each form's statistics are reported in their own rows.

### 6.3 Completeness, assignment and publication

- **Every attempt is kept** with its mass (U1 G5; K-6). No coincidence filter, outcome-triggered purge
  or real-time exclusion is applied to the dataset. An apparatus that must abort a sequence logs the
  abort as `⊥` at the event, with its trigger. Leupold's dataset "does not include the data purged in
  real time … due to long sequences of dark measurements" (LIT §1.12); that practice is excluded here.
- **`⊥`-assignment.** For the tests that need binary outcomes (S₁, Δ, Λ), a fixed local rule maps
  `⊥ ↦ 0` on each wing, declared before data, with `⊥ ↦ 1` and `⊥ ↦ fair local coin` as the declared
  sensitivity set. [A-inf] An assigned outcome is a fixed function of that wing's own raw record, so a
  realization of the raw records induces one of the assigned records with the same source structure,
  (U), (N) or (S); the lemmas apply to the assigned records with their hypotheses unchanged.
- **Publication.** The complete dataset in the schema above, its checksum, the frozen analysis code
  and the declared constants, deposited before the analysis is run; the checksum is recorded before
  unblinding (C-8).

## 7. Statistics, and what each account implies

### 7.1 Statistics

All are computed from the per-event records, over all events, conditioned only on the settings.
Estimators weight each event by the inverse of its known setting probability, so that they remain
valid under inter-event memory (C-10).

- **S₁:** the first-use CHSH value, from `(w_{A,1}, w_{B,1})` given `(x₁, y₁)`, summed over the
  second settings, with assigned outcomes.
- **ε_W(s; π):** the repeat-failure rate of wing `W` holding `(s, s)` while the remote policy is `π`:
  `P(w_{W,1} ≠ w_{W,2} | W holds (s, s), remote π)`. In the (R) form it is the rate of register value 1.
- **Δ_A(x) := ε_A(x; (0, 1)) − ε_A(x; (0, 0))** and **Δ_B(y) := ε_B(y; (0, 1)) − ε_B(y; (0, 0))**:
  L-2's witnesses in the (R) form, for (k3)'s pairs (Bob `(0, 0)` against `(0, 1)` while Alice holds;
  Alice `(0, 0)` against `(0, 1)` while Bob holds). **ΣΔ := Σ_x Δ_A(x) + Σ_y Δ_B(y).**
- **H_W(π_W; π, π′):** the total-variation distance between wing `W`'s (F)-form history laws under
  remote policies `π` and `π′`, at own policy `π_W`, over all four own policies and all six remote
  pairs. This includes TSI's witness (10) (Bob `(0, 1)`, Alice varying `x₂`).
- **Λ := Σ_x Σ_{y₁} ε_A(x; (y₁, y₂*)) + Σ_y Σ_{x₁} ε_B(y; (x₁, x₂*))**: eight repeat-failure terms,
  L-3's comparison (k3′) on both wings (arm P).
- **F_W:** at a changed own policy `(s, s′)`, `s′ ≠ s`, the largest frequency with which `w_{W,2}` equals
  any function of `(x₁, y₁, w_{A,1}, w_{B,1}, x₂, y₂)`. L-3's part (c) concerns this.
- **P₁₂:** the dependence of the first-use law on the second settings, for control C-2.

### 7.2 Predictions

| Statistic | QM, ideal local instruments on `\|Φ⁺⟩` [A-inf, standard] | Unchanged source, case (U) | Setting-independent renewal, case (N) | Source update, case (S) |
|---|---|---|---|---|
| S₁ | arm P: `2√2`; arm W: `2√2 η_A η_B` (TSI (1); correlators scale by the sharpnesses) | any value; the rows below assume `\|S₁\| > 2` | as (U) | as (U) |
| ε_W(s; π), dependence on π | none: each wing's two-use local law does not depend on the remote policy (local instruments, no message) | conditional on L-2 and (k1)–(k5): with `\|S₁\| > 2`, some `Δ_A(x)` or `Δ_B(y)` is nonzero; under (U), `ε_W(s; (r, r)) = 0` exactly and `ε_W(s; (r, r′))` is the dependence of the wing's first-use response on the remote setting. Conditional on Q-2 as well: `ΣΔ ≥ (\|S₁\| − 2)/2` | L-2 does not apply ((k2) fails); no-signalling can hold (fresh-cell lemma, SEL-EXCL-1 §3 [OFF]) | not excluded; LREV R3's designed realization (wing-local readback) gives no dependence [OFF] |
| ε_W(s; π), level | arm P: 0 for every π; arm W: `(1 − η_W)/2` for every π | as above | conditional on L-3 and (k3′), (k4′), (k5′) with `Θ` (S8): repeatability fails on the remote-dependent wing for some remote first setting; conditional on Q-3 and Q-2 as well: `Λ ≥ (\|S₁\| − 2)/2` | not excluded; LREV R3's realization gives `ε = 0` at repeated settings [OFF] |
| H_W | 0 | conditional on L-2: positive for some wing, own policy and remote pair (the (F)-form TV is at least the (R)-form Δ, Appendix A) | as for ε | as for ε |
| Λ (arm P) | 0 | conditional on L-3 (case (U)) and Q-3, Q-2: `Λ ≥ (\|S₁\| − 2)/2` | the same, conditional on L-3, Q-3, Q-2 | not excluded |
| F_W (arm P) | 1/2: at a changed setting the second outcome is fair and independent of the first records (TSI (9)) | L-3 (c) can be met by (U) as well; F_W does not discriminate | (N) with content determined by the first records is excluded, conditional on L-3 (c) | the update must also carry content not determined by the first records, conditional on L-3 (c) |
| P₁₂ | none | none, under the S-R timing | none | none |

**Reading of the table.**
- The (U), (N) and (S) columns describe OI realizations: programs that `Θ` (S8) identifies with this
  experiment. Nature's source is not classified by them.
- L-2 and L-3 are existence statements (U3 §5). Exclusion at finite statistics needs the quantitative
  bounds Q-2 and Q-3 (Appendix A). Every entry that uses them is marked.
- Case (S) predicts the quantum record law exactly in LREV R3's designed realization [OFF]. The
  experiment cannot separate case (S) from QM. It can exclude cases (U) and (N) for realizations
  meeting the lemmas' hypotheses.
- Neither lemma covers realizations without (k4) or (k4′): the measurement-dependent route
  (Main:416–423 [M]). Nor do they cover extension operations typed into `Obs`, which are stop S7(a)
  (U1 §6.1).

## 8. Decision rule, fixed before data

### 8.1 Constants and form

- One family-wise level `α`, fixed at freeze and split over the tests below by a stated
  Holm–Bonferroni allocation. Confidence bounds are martingale-valid (Azuma–Hoeffding or a stated
  Bernstein-type bound) for the inverse-probability-weighted estimators of §7.1. **LCB** and **UCB**
  denote the lower and upper one-sided bounds at the allocated level.
- The rule is stated in terms of measured quantities only. Its margins are functions of the measured
  S₁, not expected values. Verdict text is generated from the measurements by the frozen analysis
  code.

### 8.2 Steps

- **DR-0 (controls).** If any control of §9 marked *required* fails, or is vacuous, the verdict is
  `void` for every test. No other step is reported as a verdict.
- **DR-1 (precondition).** If `LCB(S₁) ≤ 2`, the verdict is `no-bearing` for DR-3 and DR-4: a
  Bell-local realization meets the data with no update, so the lemmas say nothing. DR-2's homogeneity
  test is still reported, as a QM check.
- **DR-2 (setting-independence, QM check).** For each wing, own policy and remote pair, test
  `H_W = 0` and `ε_W(s; π) = ε_W(s; π′)`, with assigned and unassigned outcomes, in both register
  forms. If any test rejects at its allocated level, the verdict is `ns-disagree`, with the rejecting
  cells listed. Otherwise `ns-consistent`, with the largest UCB of `H_W` reported.
- **DR-3 (the L-2 margin; conditional on Q-2).** If `UCB(ΣΔ) < (LCB(S₁) − 2)/2`, the verdict is
  `ns-excludes-U`, reported separately for RR-1(F) and RR-1(R). [A-inf] Under (U), each `Δ` equals
  `P(w_{W,1} ≠ w_{W,2})` under the changed remote policy, in both forms; the (F)-form verdict is
  reported because the (F)-form history determines the (R)-form register. Otherwise `ns-unresolved`.
- **DR-4 (the L-3 margin; arm P only; conditional on Q-3 and Q-2).** If
  `UCB(Λ) < (LCB(S₁) − 2)/2`, the verdict is `rep-excludes-UN`. Otherwise `rep-unresolved`.
- **DR-5 (repeatability, QM check; arm P).** Each `ε_W(s; π)` is compared with the same wing's
  single-system repeat-failure rate from control C-3. If the entangled-wing rate exceeds it with
  `LCB` of the difference above 0, the verdict is `rep-disagree`, with the cells listed. Otherwise
  `rep-consistent`.
- **DR-6 (fresh outcome; arm P).** If `UCB(F_W) < 1` on both wings, `fresh-consistent`; otherwise
  `fresh-unresolved`.
- **DR-7 (U3 §10.3).** The agreement condition of U3 §10.3 is reported **met at tier T** (§8.4) when
  DR-1 passes, DR-2 gives `ns-consistent`, DR-3 gives `ns-excludes-U`, and, for its L-3 half, DR-4
  gives `rep-excludes-UN` and DR-5 gives `rep-consistent`. It is reported **not met** with the
  failing step named otherwise.

If Q-2 or Q-3 fails its review before freeze (§11), DR-3 or DR-4 is removed from the rule before
freeze, and DR-7 is restated qualitatively: setting-independence and repeatability are reported with
their bounds, and no exclusion of (U) or (N) at finite statistics is claimed.

### 8.3 Outcome map

| DR-2 | DR-3 | DR-4 | DR-5 | Report |
|---|---|---|---|---|
| ns-consistent | ns-excludes-U | rep-excludes-UN | rep-consistent | §10.3 condition met at tier T; positive outcome (§10.1) |
| ns-consistent | ns-excludes-U | rep-unresolved | rep-consistent | L-2 half met; L-3 half unresolved (statistics or instrument quality) |
| ns-consistent | ns-unresolved | any | any | inconclusive at this sample: no exclusion claimed |
| ns-disagree | any | any | any | negative outcome for QM's no-signalling of local instruments at this tier (§10.2); diagnosis by C-5, C-6, C-10 first |
| ns-consistent | any | any | rep-disagree | the apparatus does not realize (9) on an entangled wing; L-3's target law fails for this instrument, so DR-4 has no bearing |
| any, with DR-1 `no-bearing` | — | — | — | no bearing on L-2 or L-3 |
| any, with DR-0 `void` | — | — | — | void |

### 8.4 Tiers

Each verdict carries the loopholes left open, as conditions (§9).
- **T-A:** locality enforced, no detection loophole (assigned outcomes, no fair sampling), per-event
  local random settings, complete records.
- **T-B:** as T-A with locality open (P-1a, P-3, P-1b without enforced separation). Verdicts are
  conditional on the absence of uncontrolled coupling between the wings, bounded by C-5 and C-6.
- **T-C:** as T-A or T-B with fair sampling assumed for S₁ (P-2 at low efficiency). DR-1 and the
  margins of DR-3 and DR-4 are then conditional on fair sampling; DR-2 is not, since it uses
  unconditioned local records with `⊥` kept.

## 9. Loopholes and controls

| Item | Hazard | Measure | Control | Required |
|---|---|---|---|---|
| Postselection | conditioning on joint detection makes one wing's retained events depend on the remote wing's records, and can produce or hide setting dependence | no coincidence filter; events defined by a setting-independent marker; `⊥` kept in local histories (§6.3) | C-7: event count equals marker count; every flag logged | yes |
| Detection | low efficiency lets a local model reach `S₁ > 2` under fair sampling | assigned outcomes for S₁; tier T-C otherwise | C-9: per-wing, per-setting detection rates reported; their setting-independence tested | yes |
| Locality and timing | a light-speed influence from a remote choice to a local record would give a spurious DR-2 signal or a spurious S₁ | each remote choice event outside the causal past of each local outcome registration: with window `τ_W` from a wing's first choice to its last registration, a separation `L > c · (τ_A + τ_B)` suffices for windows that start together [A-inf]; timestamps recorded (§6.1) | C-11: timing audit from the recorded times, per event | for T-A |
| Measurement independence | settings correlated with the source would void (k4) and (k4′) | local random sources; second settings drawn after the first use | C-1: settings uniform and mutually independent, and independent of the marker, the event index and earlier records (χ² at its allocated level). [A-inf] C-1 is necessary for (k4), not sufficient; (k4) remains a hypothesis of the lemmas | yes |
| Memory between events | the apparatus or source carries information from earlier events | martingale-valid bounds (§8.1) | C-10: dependence of each wing's records at `e` on the remote settings at `e − 1`, `e − 2` reported; a nonzero value diagnoses a classical coupling between the wings | yes |
| Memory within an event | the second use reads the first use's post-measurement record or state | none: this is what the experiment probes; QM's post-measurement state and LREV R3's readback realization both use it | reported attribute: when the first record is held (§3) | — |
| Prefix | the first use depends on a second setting already fixed | second settings drawn after the first use (§4.1) | C-2: P₁₂ = 0 within bounds | yes |
| Crosstalk between the wings | a shared mode, a scatter path or a control line carries a remote setting into a local record | locality where reachable | C-5: positive control, a known classical coupling from Bob's `y₂` to Alice's second-use setting injected with probability below the DR-3 margin, shown detected by DR-2 (a null not detected at that size makes DR-2 vacuous). C-6: DR-2 statistics against first-use strength (arm W scan) and against inter-wing delay; no trend | yes (C-5); yes for T-B (C-6) |
| Source quality | a weak or mixed source makes DR-1 fail, not the lemmas | — | C-4: countercontrol with a separable source of the same marginals: `UCB(S₁) ≤ 2` and DR-2 consistent | yes |
| Instrument repeatability | an imperfect instrument raises ε for reasons unrelated to the remote wing | — | C-3: each wing's repeat-failure rate on a local maximally mixed input (a fair mixture of the setting's eigenstates), with the remote wing idle; it is QM's comparison for DR-5 | yes (arm P) |
| Analysis | choice of analysis after seeing data | analysis code and constants frozen; data checksum recorded before unblinding | C-8 | yes |
| `⊥` assignment | the assignment rule changes a verdict | declared sensitivity set (§6.3) | C-12: verdicts under each declared rule reported; a verdict that changes under the set is reported as such | yes |

## 10. What the outcomes would and would not show for sector C

### 10.1 A positive outcome (§10.3 condition met at tier T)

Would show, at tier T and with its open loopholes as conditions:
- The agreement condition of U3 §10.3 is met by a performed experiment with raw complete
  local-history records, which LIT finds absent from the papers read.
- Conditional on L-2, (k1)–(k5), `Θ` (S8) and Q-2: a program that `Θ` identifies with this
  experiment, that reuses an unchanged Bell-violating source, and that meets (k1)–(k5) disagrees with
  it, a raw-direct miss (§A.24). This holds for both RR-1(F) and RR-1(R).
- Conditional on L-3, (k3′), (k4′), (k5′), `Θ` (S8), Q-3 and Q-2 (arm P): a realization in which
  neither wing's second-use content depends on the first use's outputs or the remote first setting
  disagrees with it. So RQ-UPD-2's source update is backed by agreement with a performed experiment,
  in addition to coverage (U3 §10.3, first row).
- RQ-UPD-1 is then an agreement requirement as well as a coverage one: reuse with no-signalling
  complete local histories, for realizations meeting (k1), (k3), (k4), (k5), is case (S) or (N), not
  (U) (conditional on L-2).

Would not show:
- that any OI model executes a source update; RQ-UPD's first missing step, "a `φ`-effected source
  update meeting (2)" (U3 §10.1), is unchanged, and no native or executed realization is on record;
- that sector C covers any perceived phenomenon; coverage is shown on no model (U2 §6.1);
- anything about the C/Q relation beyond CQ-2's conditional statement (U3 §10.4);
- a discrimination between PR and quantum statistics: PR has no two-use target law (U3 §4.4), and
  H-RR stays undetermined in all three cases (U3 §10.2);
- anything about realizations without (k4) or (k4′), or about extension operations typed into `Obs`
  (S7(a));
- a separation of case (S) from QM: LREV R3's designed (S) realization predicts the same records.

Classification [A-inf]. The experiment confronts QM's predictions for local instruments. For OI it is
an agreement check of requirements that the lemmas derive from QM's two-use law; it is not a test of a
prediction OI makes independently of that law. It sits on the consistency axis for sector C's
requirements (§A.23) and is not a correctness result for OI.

### 10.2 A negative outcome

- **`ns-disagree` with every control green.** One wing's two-use local record law depends on the
  remote policy beyond the bounds. At tier T-A this contradicts QM's no-signalling of local
  instruments, a result whose bearing reaches far beyond sector C. At tiers T-B and T-C the first
  reading is an uncontrolled coupling, which C-5, C-6 and C-10 bound.
  - For sector C it would not confirm case (U) or any OI realization: L-2 states what (U) requires,
    not that nature is a (U) realization. If `ΣΔ` is at or above `(|S₁| − 2)/2`, the data are
    compatible with that bound (conditional on Q-2); that compatibility singles out no model.
  - It would remove the agreement ground for RQ-UPD-1 at that tier. RQ-UPD-1's coverage ground (U3
    §10.3) concerns QM's law and would then be in question at the same time.
- **`rep-disagree`.** The apparatus does not realize (9) on an entangled wing while it does on a single
  system (C-3). L-3's target law fails for this instrument, so DR-4 has no bearing. It is a finding
  about the apparatus or about QM's Lüders update on entangled wings; it is not evidence for case (U)
  or (N).

### 10.3 No bearing, unresolved, void

`no-bearing` (DR-1), `ns-unresolved`, `rep-unresolved` and `void` change nothing: U3's agreement half
stays open, as now. None is a negative under SNR-1.

## 11. Freeze preconditions and open items

Before any adoption of this design as a preregistration (not authorized):
1. **Q-2 and Q-3** (Appendix A) need an independent review. If either fails, §8.2's fallback applies.
   A literature check for prior statements of them is not done here.
2. **`α`, the martingale bound, `y₂*`, `x₂*`, the `⊥` sensitivity set and the arm W sharpnesses** are
   fixed (§§4.2, 8.1).
3. **Sample size** is fixed from the declared bound and the margin at a conservative S₁; Appendix B
   gives an order of magnitude only.
4. **An apparatus** is identified that combines the additions of §3. LIT does not establish that any
   existing apparatus does; Choi et al. 2020 was read in abstract only.
5. **The invariant-to-checkpoint table** (§A.41) is written: every control of §9 names the record field
   or statistic that measures it.

Owner questions:
1. Should Q-2 and Q-3 be reviewed as additions to L-2 and L-3, or should DR-3 and DR-4 be dropped and
   the rule kept qualitative?
2. Is arm W in scope, or should the specification be reduced to arm P?
3. Which tier is the target for U3 §10.3's agreement half: T-A only, or T-B and T-C with their
   conditions carried?

## 12. Off-`main` references traced (§A.42 item 8)

| Reference | Claim it supports here | Classification |
|---|---|---|
| U3, BRIEF, U1, U2, LREV on branch `research/ro1-sector-c-1169-20261114` at `6ab9515d` | L-2, L-3 and their hypotheses; RQ-UPD; the register forms; G5; LREV R3's readback realization | **Support off `main`** (gap); U3 r3 and the RR-1 reading owner-accepted (#1169 c.6893058127) |
| LIT on the same branch | the apparatus records of §3; the absence of a qualifying experiment (§1) | **Support off `main`** (gap); owner-accepted (#1169 c.6893058127) |
| SEL-EXCL-1 (cited through U3) | `T`'s responses (§4.3); the fresh-cell lemma (§7.2) | **Support off `main`** (gap), as in U3 §9 |
| TSI on `main`, blob `65db5a7c` | the first-use law (1), the two-use law (9), the witness (10), the prefix property | **Support on `main`**, at [NP] standing |
| Main:416–423 on `main` | the measurement-dependent route | **Support on `main`** [M] |
| #1169 comments 6892563291, 6893058127, 6893331779 | authorization; accepted scopes; the RR-1 reading | Provenance and governance |

Every statement built on a row marked support off `main` carries that gap (§A.46 item 1).

***

## Appendix A. Design aids Q-2 and Q-3 (author-side hand derivations [A-inf], unreviewed)

These are not results of this note. They are stated so that a reviewer can check them; DR-3 and DR-4
use them only if they pass review (§11).

**Setting.** (k1) and (k4) of U3 §5.1: deterministic binary first-use responses `A₁(x, y, λ)`,
`B₁(x, y, λ)`, with a law of `λ` that does not depend on the policies. Write
`δ_A(x) := P(A₁(x, 0, λ) ≠ A₁(x, 1, λ))` and `δ_B(y) := P(B₁(0, y, λ) ≠ B₁(1, y, λ))`.

**Q-2.** `|S₁| ≤ 2 + 2[δ_A(0) + δ_A(1) + δ_B(0) + δ_B(1)]`.

*Derivation.* Set `a′(x, λ) := A₁(x, 0, λ)` and `b′(y, λ) := B₁(0, y, λ)`, local responses, so their
CHSH value `S′` satisfies `|S′| ≤ 2` (Main:389 [M]). For each `(x, y)`, the correlators satisfy
`|E_xy − E′_xy| ≤ 2 P(A₁ ⊕ B₁ ≠ a′ ⊕ b′) ≤ 2[P(A₁(x, y) ≠ a′(x)) + P(B₁(x, y) ≠ b′(y))]`. The four
terms are: `(0, 0)`: 0; `(0, 1)`: `δ_A(0)`; `(1, 0)`: `δ_B(0)`; `(1, 1)`: `δ_A(1) + δ_B(1)`. Sum. ∎

*Use in DR-3.* Under case (U) with (k2), (k3), (k5), the proof of L-2 gives, in the (R) form, Alice's
register 0 under Bob `(0, 0)` and `A₁(x, 0, λ) ⊕ A₁(x, 1, λ)` under Bob `(0, 1)`, so `Δ_A(x) = δ_A(x)`;
likewise `Δ_B(y) = δ_B(y)`. Hence `ΣΔ ≥ (|S₁| − 2)/2`. In the (F) form, the TV distance between the two
history laws is at least `δ_A(x)`, since the law under Bob `(0, 1)` puts mass `δ_A(x)` off the diagonal
and the law under Bob `(0, 0)` puts none there.

**Q-3.** Under L-3's setting, if wing A's second-use content does not depend on `y₁`, `a₁` or `b₁`,
then for each `x` and fixed `y₂`,
`δ_A(x) ≤ ε_A(x; (0, y₂)) + ε_A(x; (1, y₂))`, and likewise for wing B.

*Derivation.* As in L-3's proof, under Alice `(x, x)` and Bob `(y₁, y₂)`, `a₂ = g(λ, ν)` with
`g := A₂(x, y₂, G(λ, ν, x))`, which does not depend on `y₁`; by (k4′) the law of `(λ, ν)` is the same
for `y₁ = 0` and `y₁ = 1`. Then `P(A₁(x, 0, λ) ≠ A₁(x, 1, λ)) ≤ P(A₁(x, 0, λ) ≠ g) + P(g ≠ A₁(x, 1, λ))`,
and the two terms are `ε_A(x; (0, y₂))` and `ε_A(x; (1, y₂))`. ∎

*Use in DR-4.* If neither wing's second-use content depends on the first outputs or the remote first
setting, Q-3 on both wings and Q-2 give `Λ ≥ (|S₁| − 2)/2`. This is L-3's (a) and (b) in quantitative
form at finite repeatability. It does not identify which wing updates, as L-3 (a) does not without the
realization. At `ε = 0` it reduces to L-3.

**Scope.** As L-2 and L-3: no atomic source law is used; a setting-independent herald restricts the
argument to the success branch without changing it; realizations without (k4) or (k4′) are not
covered. Q-3 is stated for deterministic responses; L-3's dilation of policy-independent noise
(U3 §5.2, Scope) is assumed to carry over and is part of what review checks.

## Appendix B. Order of magnitude of the sample size (hand estimate, illustrative)

[A-inf] Each `ε_W(s; π)` term is a conditional rate on joint policies of probability 1/16, so its
inverse-probability-weighted estimator takes values in `[0, 16]`. An Azuma–Hoeffding bound at
per-term level `10⁻⁴` gives a half-width of about `16 · √(ln(10⁴)/(2N)) ≈ 34/√N`. Λ has eight terms,
so its bound is about `270/√N` above its estimate. With an illustrative `S₁ ≈ 2.55` (visibility 0.9),
the DR-4 margin is about 0.27, which needs `N` of order `10⁶` events under this bound. A
variance-adaptive bound reduces this when the true rates are small, as single-system repeatability of
"above 99.6 %" (Leupold) suggests for P-1. These figures are for planning only; they are not
predictions and do not enter the rule.
