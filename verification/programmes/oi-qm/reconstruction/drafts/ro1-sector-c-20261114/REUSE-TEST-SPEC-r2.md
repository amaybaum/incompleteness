# REUSE-TEST-SPEC, r2: a two-sided reuse test with one wing held and the remote wing varied

**Scope of r2.** r1 (`REUSE-TEST-SPEC-r1.md`, blob `07a6e9f768236586a590439435089fa4c3c5f115`, at
`bf809e3b`) is left unchanged. r2 differs from r1 only by the required changes R-1 to R-7 and the
optional items O-1 to O-8 of its independent review (`REVIEW-REUSE-TEST-SPEC-r1.md`, blob
`aed9d8ca6fc03279a06c4d88ff830e6ffb016759`, retained at `45517959`; cited REV), and their necessary
consequences. Dispositions, one per finding, are in `RESPONSE-REUSE-TEST-SPEC-r1.md`. The design's
core (source, schedule S-R, records, both RR-1 forms) is unchanged.
- **R-1 (M-2).** Arm W is outside L-2: a program that `Θ` identifies with it applies different
  instruments at its two uses, so its responses are tick-indexed, case (N). DR-3 and §10.1's L-2
  bullet are restricted to arm P (§§5, 7.2, 8.2, 10.1).
- **R-2 (M-1).** r1's [A-inf] on the `⊥` rule was false for a fresh fair coin. The coin is drawn once
  per wing per event; exclusions are claimed only under rules that keep the source structure (§6.3).
- **R-3.** Strict (U) is excluded by any repeat failure at a fully repeated joint policy, without
  L-2. This baseline is DR-3a; DR-3 adds information only where every such cell is consistent with
  zero (§§7.1, 8.2, 10.1).
- **R-4.** A countercontrol for DR-3a, DR-3 and DR-4 (CC-1); C-5 as a separate calibration block;
  pass criteria for C-6 and C-10; the T-C common subensemble (§§8.4, 9, 11).
- **R-5, R-6.** An exhaustive outcome map with a precedence order (§8.3); one pinned CHSH orientation
  (§§7.1, 8.1, Appendix A).
- **R-7.** Mao's per-acquisition settings are labelled as LIT's writer's reading; the arm P first uses
  of P-1 and P-2 move to "Additions"; P-1's detection expectation is marked [DES] (§3).
- **O-1.** Q-3 uses no repeatability, no `Θ` and no (k5′). It is stated at that scope, and DR-4 then
  applies to arm W, where at ideal QM it can exclude for `η ≳ 0.94` (§§5, 8.2, Appendix A).
- **O-2 to O-8.** One martingale bound per linear test statistic; a declared setting-bias bound; an
  applied-setting fidelity monitor; the (F)/(R) coincidence of the DR-3 and DR-4 statistics; `F_W`
  in arm P only; the header's list of OI sources; the general locality condition.

**Status: paper-only design specification; r2 unreviewed.** It specifies a performed experiment that
would supply the raw-direct data (§A.24) that U3's agreement half asks for (`S3-U3-r3.md` §10.3,
owner question 4). It is a design document only. It adopts no premise, extension E or sector
condition C, chooses no apparatus, authorizes no execution and runs no computation. Nothing in it is
evidence.

**Sources of OI-attributed statements.** Every statement attributed to OI rests on one or more of:
- the lemmas L-2 and L-3 of U3 §5 ("proved as stated, at their stated hypotheses", #1169
  c.6893058127), conditional on those hypotheses;
- the design aids Q-2 and Q-3 (Appendix A), author-side hand derivations [A-inf], re-derived and
  found correct at their stated hypotheses by REV §1, with no owner decision and no literature check;
- the elementary baseline step of DR-3a (§8.2), an author-side hand step [A-inf] that REV §2.3 states;
- two results off `main`, each marked where used: SEL-EXCL-1's fresh-cell lemma [OFF] and LREV R3's
  designed readback realization [OFF].

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

On the same branch at `45517959`: r1 and REV, blobs above.

On `main` (the branch head contains `main` at `7ac74a4b`): TSI,
`verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/two-system-interface.md`, blob
`65db5a7caf70091cffc1478001badf5f12be8313`, at [NP] standing as in U3 §9; `papers/Main.md` at the
lines U3 cites.

**Method.** Reading and hand reasoning only. The quantum predictions of §7 are standard Lüders
calculations for local instruments on `|Φ⁺⟩`, re-checked by hand [A-inf] and by REV §3; the
projective case is TSI (1) and (9). The arm W threshold `η ≈ 0.9385` is REV's evaluation (REV §1.2),
re-checked here by hand. Appendix B is an order-of-magnitude hand estimate. No literature beyond LIT
was read for this note; every apparatus statement attributed to a paper is LIT's record of it.

**Labels.** As in U3: **[M]**, **[M-r]**, **[NP]**, **[OFF]**, **[A-inf]**. **[DES]** marks a design
choice or expectation stated here, open to review. OI-attributed statements carry "conditional on
L-2", "conditional on L-3", "conditional on Q-2" or "conditional on Q-3" with the hypotheses named.

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
  axes are at the CHSH angles in one plane (TSI (1)), labelled so that the pinned orientation of §7.1
  gives `+2√2` at ideal QM.
- **Arm P (required):** both first uses projective and nondestructive, second uses projective.
- **Arm W (secondary):** first uses unsharp, of declared sharpness `η_A, η_B`, second uses projective.
- Per event, each wing records both outcomes as separate records (fresh-output form, RR-1(F)), with
  `⊥` for any failure, plus settings, applied-setting readbacks, timestamps, one assignment coin and
  raw detector data. The same-register record of RR-1(R) is computed from them.
- The complete per-event dataset, all attempts included, is published.

## 3. Source and platform options

Each option is assembled from apparatus LIT records. Each needs elements that no paper read combines;
those are listed as additions. No option is chosen here. [DES]

| | P-1: trapped ions | P-2: time-tagged photonics | P-3: superconducting qubits |
|---|---|---|---|
| Apparatus on record (LIT) | Leupold et al. 2018: one ⁴⁰Ca⁺ ion, 53 million sequential QND projective measurements, settings "chosen in real time by a quantum random number generator, latency below 50 µs", repeatability "above 99.6 %", raw dataset public (LIT §1.12). Kirchmair et al. 2009: two ⁴⁰Ca⁺ ions in one trap, sequential QND measurements of two-qubit observables by mapping and fluorescence detection, each outcome recorded per run | Mao et al. 2022: per event, "one of the four single-photon detectors per pulse corresponds to exactly one of the four outcome combinations (b_k,1, b_k,2)"; "All photon detection events are time-tagged"; first use an unsharp Sagnac CNOT with a path meter of strength `η` (LIT §1.8). Zhu et al. 2022: both wings of one singlet pair used twice (LIT §1.9) | White et al. 2016: two transmons in the singlet state, each with an ancilla; ancilla measurement of strength `φ ∈ [0, π/2]`, projective at `φ = π/2`; per-shot readout of all four qubits (LIT §1.10) |
| Pair source | entangled pair of ions: in one trap (P-1a, Kirchmair's geometry) or in two traps (P-1b). A two-trap source is not among the papers read; its availability is not established here | SPDC polarization pairs (all photonic papers read) | the White chip |
| First use, arm P | see Additions | see Additions | ancilla measurement at `φ = π/2` (White) |
| First use, arm W | see Additions | Mao's coupling at `η < 1` | White's ancilla at `φ < π/2` |
| When the first record is held | P-1 as designed: before the second use (classical fluorescence record) [DES] | at the end (deferred readout) | at the end ("all four qubits are read out") |
| Additions not in the papers read | (i) local nondestructive fluorescence detection of **one** ion of an entangled pair, with the partner's qubit preserved (Leupold detects a single ion; Kirchmair maps two-qubit observables), as arm P's first use; (ii) an ancilla-mediated partial measurement, as arm W's first use; (iii) the two-wing, two-use schedule with per-use random settings on both ions; (iv) for P-1b, the two-trap source | (i) Mao's coupling at full strength, a projective path meter, as arm P's first use (Mao ran it unsharp); (ii) the coupling and four-detector readout on **both** wings; (iii) per-pulse fast setting switching on both uses. How Mao changed settings is not stated in the version LIT read; "fixed per acquisition" is LIT's *[writer's reading]* (LIT §1.8) | (i) per-shot random settings on both uses (White ran one fixed configuration); (ii) raw binary readouts without calibration rescaling (White's ancilla correlators were rescaled) |
| Detection loophole | none expected for fluorescence detection [DES]; measured, C-9 | open unless detection efficiency is high; fair sampling otherwise (T-C, §8.4) | none stated by White ("near unit detection efficiency"); readout assignment error is part of the record |
| Locality | P-1a: open. P-1b: open unless the condition of §9 holds | can be enforced at laboratory separations if the windows are short (§9) | open ("such an interaction cannot be ruled out here", White) |
| Reachable tier (§8.4) | T-B (P-1a, P-1b); T-A only if P-1b also enforces locality | T-C with fair sampling; T-A with high efficiency and enforced locality | T-B |

[A-inf] The order of first-record holding differs across platforms. The decision rule (§8) uses only
the records at the comparison tick and does not depend on it. It is reported (§6) because U3's C-RET
against R2 table (U3 §7) and LREV R3's readback realization concern a first record that exists before
the second use; P-1 as designed would supply that as a raw-direct fact, P-2 and P-3 do not.

## 4. Setting schedules

### 4.1 Primary schedule S-R: full factorial, per event, per use [DES]

- At each event `e`, Alice draws `x₁, x₂` and Bob draws `y₁, y₂`, four fair bits, independent of each
  other, of the event marker, of the event index and of all earlier records.
- Each draw uses its own local random source and is recorded raw (§6). The applied setting is read
  back at each use and recorded (fidelity monitor, C-13).
- The second setting of each wing is drawn after that wing's first use is complete. The lemmas allow
  a preloaded second setting ((k3): "a preloaded per-use slot … serves equally"); drawing it later
  removes the prefix route TSI uses (TSI §2: "the program slots may be loaded initially") and makes
  control C-2 meaningful.
- Every joint policy `(x₁x₂, y₁y₂)` has nominal probability 1/16. Every holding policy of each wing,
  `(s, s)`, meets all four remote policies.

### 4.2 Fixed constants, declared before data

- The CHSH orientation of §7.1.
- The family-wise error level `α`, its Bonferroni weights over the bounds of §8.2, and the martingale
  bound used (§8.1).
- A declared bound `β` on the deviation of each setting probability from 1/2 (§8.1).
- The structure-keeping `⊥`-assignment set (§6.3).
- The event-marker rule (herald, or trial clock with its period).
- For arm W, the declared Kraus pair and sharpnesses (§5).
- The countercontrol's synthetic records and expected verdicts (CC-1, §9).

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
  and (k3′) need, at one fixed remote second setting, are eleven of the sixteen [A-inf; recounted in
  REV §2.1]. Running only those, or running them in blocks, removes five policies and introduces
  setting drift across blocks, the failure LIT R-4 records for per-acquisition designs ("we are
  effectively using different states for each measurement", Padovan et al.). S-R is kept, and Λ
  (§7.1) uses all four remote policies.

## 5. First-use strength

| Arm | First use | Second use | What it serves | Coverage by the lemmas and aids |
|---|---|---|---|---|
| P (required) | projective, nondestructive | projective | L-3's repeatability; L-2's comparison; the full two-use law (1)×(9) | DR-3a (baseline); DR-3: L-2 with (k1)–(k5) and Q-2; DR-4: L-3 with (k1) or its dilation, (k3′), (k4′), (k5′) and `Θ`, and Q-3, Q-2 at finite repeatability |
| W (secondary) | unsharp, sharpness `η_W ∈ (0, 1)` per wing, declared | projective | DR-2's setting-independence at a different instrument; DR-4 by Q-3; a strength scan as a countercontrol for crosstalk (C-6) | DR-3a (baseline); DR-4 by Q-3 and Q-2 only. **Not L-2:** see below. **Not L-3:** L-3 "says nothing about non-repeatable instruments" (U3 §5.2, Scope) |

- **Arm W is outside L-2** (REV M-2). (k2) requires that "the second use applies the same response
  functions" (U3 §5.1). A program that `Θ` identifies with arm W applies an unsharp instrument at its
  first use and a projective one at its second, so its responses are tick-indexed (`A₂ ≠ A₁`), which
  U3 §2.2 places in case (N). REV gives a countermodel meeting (k1), (k3), (k4), (k5) and the
  unchanged-`λ` half of (k2) with `S₁ = 2√2` and blind local histories: `a₁ = R`,
  `b₁ = R ⊕ x₁y₁ ⊕ C`, `a₂ = f_A`, `b₂ = f_B`. DR-3 is therefore not evaluated in arm W.
- **Arm W is inside Q-3** (REV §1.2, O-1). Q-3 uses neither repeatability, nor `Θ`'s identification
  with the Lüders law, nor (k5′); the repeat-failure rates enter only as measured rates. With
  `η_A = η_B = η` at ideal QM, `Λ = 4(1 − η)` and the margin `(S₁ − 2)/2` is `√2 η² − 1`, so DR-4 can
  exclude when `η > (−4 + √(16 + 20√2))/(2√2) ≈ 0.9385` (REV §1.2; re-checked by hand). Q-3 is used
  at that scope only; it does not extend L-3.
- In arm W the first-use CHSH value is `2√2 η_A η_B` for unsharp Lüders instruments (§7.2); DR-1
  needs `η_A η_B > 1/√2`. A scan that includes points below that threshold serves as a countercontrol
  only (C-6).
- The unsharp instrument is declared by its Kraus pair before data, for example
  `K_± = √((I ± η σ_n)/2)`. The predictions of §7.2 for arm W are for that pair.

## 6. Per-event records

### 6.1 Schema (fresh-output form) [DES]

One row per event marker, kept whether or not anything is detected.

| Field | Content |
|---|---|
| `e` | event index, consecutive, with no gaps |
| `t_e` | event-marker time; herald value `h_e ∈ {0, 1}` and the herald's raw signal where the source is heralded |
| per wing `W ∈ {A, B}`, per use `i ∈ {1, 2}` | raw random-source output; intended setting `s_{W,i}`; applied-setting readback; time the setting was chosen; time it was applied |
| per wing, per use | outcome `w_{W,i} ∈ {0, 1, ⊥}`; registration time; raw detector data (photon counts and threshold for P-1; channel and time tag for P-2; readout signal and threshold for P-3) |
| per wing | one assignment coin `c_{W,e}`, drawn by a local random source at the event, independent of the settings (§6.3) |
| per wing | instrument arm (P or W) and declared sharpness; calibration identifier; block type (production or calibration, C-5) |
| flags | every abort, purge, timeout or exclusion, with its trigger, at the event where it happened |

### 6.2 The two register forms

- **RR-1(F):** each wing's complete two-use history is the pair `(w_{W,1}, w_{W,2})`, with its
  settings, held at the comparison tick.
- **RR-1(R):** each wing's register is `w_{W,1} ⊕ w_{W,2}`, set to `⊥` if either entry is `⊥`. It is
  computed from the (F) record and is assessed separately, as the owner decision requires.
- [A-inf] No outcome of this experiment can favour one form over the other as a claim about nature
  (BRIEF §4). Each form's statistics are reported in their own rows. The repeat-failure statistics
  (`B`, `Δ`, `Λ`) are the same number in both forms, since `w₁ ≠ w₂` exactly when the register is 1;
  they are reported in both rows with that stated. Only `H_W` differs between the forms (REV O-5).

### 6.3 Completeness, assignment and publication

- **Every attempt is kept** with its mass (U1 G5; K-6). No coincidence filter, outcome-triggered purge
  or real-time exclusion is applied to the dataset. An apparatus that must abort a sequence logs the
  abort as `⊥` at the event, with its trigger. Leupold's dataset "does not include the data purged in
  real time … due to long sequences of dark measurements" (LIT §1.12); that practice is excluded here.
- **`⊥`-assignment.** The tests that need binary outcomes (S₁, B, Δ, Λ) use an assignment rule from
  the **structure-keeping set**, declared before data:
  - `⊥ ↦ 0` on each wing;
  - `⊥ ↦ 1` on each wing;
  - `⊥ ↦ c_{W,e}`: the wing's one coin for the event, applied to every `⊥` of that wing in that event.

  [A-inf] Each rule makes the assigned outcome a fixed function of the wing's raw outcome and of
  `c_{W,e}`. The coin is drawn once per event, independently of the policies, so it can be placed in
  the source `λ`; then a realization of the raw records induces one of the assigned records with the
  same source structure, (U), (N) or (S), and the lemmas and aids apply to the assigned records with
  their hypotheses unchanged.

  A coin drawn **afresh for each `⊥`** is not in the set. It is fresh noise per use, case (N), and it
  can break DR-3: REV M-1 gives a (U) model with `S₁ = 3` and `ΣΔ = 0` under it.
- **Exclusions under the set.** DR-3a, DR-3 and DR-4 claim an exclusion only if it holds under every
  rule of the structure-keeping set (C-12). DR-2 is run on unassigned records as well.
- **Publication.** The complete dataset in the schema above, its checksum, the frozen analysis code
  and the declared constants, deposited before the analysis is run; the checksum is recorded before
  unblinding (C-8).

## 7. Statistics, and what each account implies

### 7.1 Statistics

All are computed from the per-event records, conditioned only on the settings, over production events
(and, in tier T-C, over the subensemble of §8.4). Estimators weight each event by the inverse of its
nominal setting probability, so that they remain valid under inter-event memory (C-10); the declared
bias bound `β` enters the confidence bounds (§8.1).

- **S₁:** the first-use CHSH value, `S₁ := E₀₀ + E₀₁ + E₁₀ − E₁₁`, with `E_xy` the correlator of
  `(w_{A,1}, w_{B,1})` given `(x₁, y₁) = (x, y)`, summed over the second settings, with assigned
  outcomes. This orientation is pinned at freeze; no other orientation is used in any rule.
- **ε_W(s; π):** the repeat-failure rate of wing `W` holding `(s, s)` while the remote policy is `π`:
  `P(w_{W,1} ≠ w_{W,2} | W holds (s, s), remote π)`.
- **B_W(s; r) := ε_W(s; (r, r))**: the baseline at a fully repeated joint policy, eight cells.
- **Δ_A(x) := ε_A(x; (0, 1)) − ε_A(x; (0, 0))** and **Δ_B(y) := ε_B(y; (0, 1)) − ε_B(y; (0, 0))**:
  L-2's witnesses for (k3)'s pairs. **ΣΔ := Σ_x Δ_A(x) + Σ_y Δ_B(y).**
- **H_W(π_W; π, π′):** the total-variation distance between wing `W`'s (F)-form history laws under
  remote policies `π` and `π′`, at own policy `π_W`, over all four own policies and all six remote
  pairs. This includes TSI's witness (10) (Bob `(0, 1)`, Alice varying `x₂`).
- **Λ := ½ Σ_x Σ_{y₁, y₂} ε_A(x; (y₁, y₂)) + ½ Σ_y Σ_{x₁, x₂} ε_B(y; (x₁, x₂))**: L-3's comparison
  (k3′) on both wings, averaged over the fixed remote second setting (REV O-1). Q-3 holds for each
  fixed remote second setting, so it holds for the average.
- **F_W (arm P only):** at a changed own policy `(s, s′)`, `s′ ≠ s`, the largest frequency with which
  `w_{W,2}` equals any function of `(x₁, y₁, w_{A,1}, w_{B,1}, x₂, y₂)`.
- **P₁₂:** the dependence of the first-use law on the second settings, for control C-2.
- **φ_W(s; r):** the applied-setting mismatch rate in cell `B_W(s; r)`, from the readbacks (C-13).

### 7.2 Predictions

| Statistic | QM, ideal local instruments on `\|Φ⁺⟩` [A-inf, standard; REV §3] | Unchanged source, case (U) | Setting-independent renewal, case (N) | Source update, case (S) |
|---|---|---|---|---|
| S₁ | arm P: `2√2`; arm W: `2√2 η_A η_B` (TSI (1); correlators scale by the sharpnesses) | any value; the rows below assume `S₁ > 2` | as (U) | as (U) |
| B_W(s; r) | arm P: 0; arm W: `(1 − η_W)/2` | exactly 0, by the baseline step of DR-3a [A-inf], under (k1) or a dilation with its noise in the unchanged source, (k2) and (k5); no Bell violation and no lemma needed | not constrained | not excluded; LREV R3's realization gives 0 [OFF] |
| ε_W(s; π), dependence on π | none: each wing's two-use local law does not depend on the remote policy (local instruments, no message), in both arms | arm P, conditional on L-2 and (k1)–(k5): with `S₁ > 2`, some `Δ_A(x)` or `Δ_B(y)` is nonzero. Conditional on Q-2 as well: `ΣΔ ≥ (S₁ − 2)/2`. Arm W: L-2 does not apply (§5) | L-2 does not apply ((k2) fails); no-signalling can hold (fresh-cell lemma, SEL-EXCL-1 §3 [OFF]) | not excluded; LREV R3's designed realization gives no dependence [OFF] |
| ε_W(s; π), level | arm P: 0 for every π; arm W: `(1 − η_W)/2` for every π | as above | arm P, conditional on L-3 and (k3′), (k4′), (k5′) with `Θ` (S8): repeatability fails on the remote-dependent wing for some remote first setting | not excluded; LREV R3's realization gives `ε = 0` at repeated settings [OFF] |
| H_W | 0 | arm P, conditional on L-2: positive for some wing, own policy and remote pair (the (F)-form TV is at least the matching `Δ`, Appendix A) | as for ε | as for ε |
| Λ | arm P: 0; arm W: `4(1 − η)` at `η_A = η_B = η` | both arms, conditional on Q-3 and Q-2 with (k1) or its dilation, (k3′), (k4′): `Λ ≥ (S₁ − 2)/2` when neither wing's second-use content depends on the first outputs or the remote first setting | the same, conditional on Q-3 and Q-2 | not excluded |
| F_W (arm P) | 1/2: at a changed setting the second outcome is fair and independent of the first records (TSI (9)). In arm W the QM value is not 1/2 (REV §3); F_W is not used there | L-3 (c) can be met by (U) as well; F_W does not discriminate | (N) with content determined by the first records is excluded, conditional on L-3 (c) | the update must also carry content not determined by the first records, conditional on L-3 (c) |
| P₁₂ | none | none, under the S-R timing | none | none |

**Reading of the table.**
- The (U), (N) and (S) columns describe OI realizations: programs that `Θ` (S8) identifies with this
  experiment. Nature's source is not classified by them.
- **The baseline dominates L-2 for strict (U)** (REV §2.3). Under strict (U), the outputs at a fully
  repeated joint policy are identical, so `B_W(s; r) = 0` exactly. An apparatus with any measurable
  repeat failure therefore excludes strict (U) by DR-3a, without L-2 or Q-2. DR-3 subtracts exactly
  that baseline. It adds an exclusion only where every `B_W(s; r)` is consistent with zero. The class
  of unchanged `λ` with fresh local noise per use is case (N); L-2 does not reach it, and DR-4 does
  (Q-3, Q-2).
- L-2 and L-3 are existence statements (U3 §5). Exclusion at finite statistics through them needs
  the quantitative aids Q-2 and Q-3 (Appendix A), marked wherever used.
- Case (S) predicts the quantum record law exactly in LREV R3's designed realization [OFF]. The
  experiment cannot separate case (S) from QM. It can exclude strict (U) and, through Q-3, realizations
  in which neither wing's second-use content depends on the first outputs or the remote first setting.
- Neither the lemmas nor the aids cover realizations without (k4) or (k4′): the measurement-dependent
  route (Main:416–423 [M]). Nor do they cover extension operations typed into `Obs`, which are stop
  S7(a) (U1 §6.1).

## 8. Decision rule, fixed before data

### 8.1 Constants and form

- One family-wise level `α`, fixed at freeze and split over the bounds of §8.2 by declared
  Bonferroni weights.
- Each exclusion test is a one-sided bound on one linear statistic of the per-event
  inverse-probability-weighted terms (REV O-2):
  - DR-3: `T₃ := (S₁ − 2)/2 − ΣΔ`;
  - DR-4: `T₄ := (S₁ − 2)/2 − Λ`;
  - DR-3a: `B_W(s; r) − φ_W(s; r)` per cell.

  The bound is martingale-valid (Azuma–Hoeffding, or a declared Bernstein-type bound) with the
  per-event range stated at freeze, and it is widened by the declared setting-bias bound `β`
  (REV O-3). **LCB** and **UCB** denote the one-sided bounds at the allocated weight.
- The rule is stated in terms of measured quantities only. The inequalities it tests are fixed in
  advance; their thresholds are functions of the measured statistics, not expected values (REV §4.1).
  Verdict text is generated from the measurements by the frozen analysis code.

### 8.2 Steps, per arm

- **DR-0 (controls).** If any control of §9 marked *required* fails its stated criterion, or is
  vacuous, the verdict is `void` for every test of that arm.
- **DR-1 (precondition).** If `LCB(S₁) ≤ 2`, the verdict is `no-bearing` for DR-3a, DR-3 and DR-4:
  a Bell-local realization meets the data with no update. DR-2 is still reported, as a QM check.
- **DR-2 (setting-independence, QM check).** For each wing, own policy and remote pair, test
  `H_W = 0` and `ε_W(s; π) = ε_W(s; π′)`, on assigned and unassigned records, in both register forms.
  If any test rejects at its weight, the verdict is `ns-disagree`, with the rejecting cells listed.
  Otherwise `ns-consistent`, with the largest UCB of `H_W` reported.
- **DR-3a (baseline; both arms; elementary step [A-inf], no lemma).** If, for some wing and cell,
  `LCB(B_W(s; r) − φ_W(s; r)) > 0` under every rule of the structure-keeping set, the verdict is
  `u-excluded-baseline`, with the cells listed: strict (U), under (k1) or a dilation with its noise in
  the unchanged source, (k2) and (k5), is excluded. Otherwise `baseline-null`.
- **DR-3 (the L-2 margin; arm P only; conditional on L-2 and Q-2).** If `LCB(T₃) > 0` under every rule
  of the structure-keeping set, the verdict is `ns-excludes-U`. Otherwise `ns-unresolved`. Reported
  for RR-1(F) and RR-1(R), with the statement that the statistic is the same number in both forms
  (§6.2). It adds an exclusion beyond DR-3a only when DR-3a returns `baseline-null`.
- **DR-4 (the Q-3 margin; both arms; conditional on Q-3 and Q-2; in arm P also an instance of
  L-3).** If `LCB(T₄) > 0` under every rule of the structure-keeping set, the verdict is
  `rep-excludes-UN`: realizations in which neither wing's second-use content depends on the first
  outputs or the remote first setting are excluded. Otherwise `rep-unresolved`.
- **DR-5 (repeatability, QM check; both arms).** Each `ε_W(s; π)` is compared with the same wing's
  single-system repeat-failure rate from C-3, for the same instrument. If the entangled-wing rate
  exceeds it with `LCB` of the difference above 0, the verdict is `rep-disagree`, with the cells
  listed. Otherwise `rep-consistent`.
- **DR-6 (fresh outcome; arm P only).** If `UCB(F_W) < 1` on both wings, `fresh-consistent`;
  otherwise `fresh-unresolved`. This test is nearly automatic at any useful sample size and adds
  little (REV O-6); it is kept because it is L-3's part (c).

If Q-2 or Q-3 is rejected at owner decision before freeze (§11), DR-3 or DR-4 is removed from the rule
before freeze; DR-3a does not depend on them.

### 8.3 Outcome map: precedence and exhaustive rows

The summary for each arm is the first row whose condition holds. Every verdict of §8.2 is reported in
full beside the summary.

| # | Condition | Summary |
|---|---|---|
| 1 | DR-0 `void` | void |
| 2 | DR-1 `no-bearing` | no bearing on L-2, L-3, Q-2, Q-3 or the baseline; DR-2 reported as a QM check |
| 3 | DR-2 `ns-disagree` | negative outcome for QM's no-signalling of local instruments at this tier (§10.2); diagnosis by C-5, C-6 and C-10 first; no exclusion is summarized |
| 4 | DR-5 `rep-disagree` | the apparatus does not realize QM's repeat law on an entangled wing; DR-4 has no bearing; DR-3a's and DR-3's verdicts are summarized beside it, read as in rows 5–8 |
| 5 | arm P; strict (U) excluded (DR-3a `u-excluded-baseline` or DR-3 `ns-excludes-U`); DR-4 `rep-excludes-UN` | U3 §10.3's agreement condition met at tier T, both halves, with the strict-(U) route named |
| 6 | arm P; strict (U) excluded; DR-4 `rep-unresolved` | first half met (setting-independence and strict (U) excluded, route named); second half unresolved |
| 7 | arm P; DR-3a `baseline-null` and DR-3 `ns-unresolved`; DR-4 `rep-excludes-UN` | second half met; strict (U) not excluded by either route (an apparatus repeating perfectly within its bounds, with DR-3 short of its margin) |
| 8 | arm P; DR-3a `baseline-null`, DR-3 `ns-unresolved`, DR-4 `rep-unresolved` | inconclusive at this sample |
| 9 | arm W; DR-3a `u-excluded-baseline` | first half met at arm W (setting-independence; strict (U) excluded by the baseline); DR-4's verdict reported as a Q-3 statement; L-3's repeatability half not addressed by arm W |
| 10 | arm W; DR-3a `baseline-null` | arm W gives setting-independence only; DR-4's verdict reported as a Q-3 statement |

Rows 5–8 cover every combination of the strict-(U) route (excluded or not) and DR-4 (excluded or
unresolved) in arm P, and rows 9–10 every DR-3a value in arm W, so the map is a function of the
verdicts [A-inf]. 
### 8.4 Tiers

Each verdict carries the loopholes left open, as conditions (§9).
- **T-A:** locality enforced (C-11), setting draws outside the future light cone of the pair's
  emission or herald (freedom of choice, C-11), no detection loophole (assigned outcomes, no fair
  sampling), per-event local random settings, complete records.
- **T-B:** as T-A with locality open (P-1a, P-3, P-1b without the condition of §9). Verdicts are
  conditional on the absence of an uncontrolled coupling between the wings; C-5, C-6 and C-10 probe
  specific couplings and do not bound unknown ones.
- **T-C:** as T-A or T-B with fair sampling for the binary-outcome tests. DR-1, DR-3a, DR-3 and DR-4
  are computed on one common subensemble, `E₄`: the events with all four uses detected (no `⊥` on
  either wing). The fair-sampling assumption is stated in model terms: the probability of `E₄` given
  `λ` does not depend on the policies (the review's form, detection independent of `λ` and of the
  policies, is a stronger version). [A-inf] Under it the law of `λ` on `E₄` does not depend on the
  policies, so (k4) and (k4′) hold there and the aids apply on `E₄`. DR-2 and C-9 are computed on the
  full `⊥`-kept records. A coincidence-conditioned S₁ is never combined with `⊥`-kept rates.

## 9. Loopholes and controls

| Item | Hazard | Measure | Control and pass criterion | Required |
|---|---|---|---|---|
| Postselection | conditioning on joint detection makes one wing's retained events depend on the remote wing's records, and can produce or hide setting dependence | no coincidence filter; events defined by a setting-independent marker; `⊥` kept in local histories (§6.3); T-C's common subensemble only as §8.4 states | C-7: event count equals marker count, and every flag is logged | yes |
| Detection | low efficiency lets a local model reach `S₁ > 2` under fair sampling | assigned outcomes for S₁; tier T-C otherwise | C-9: per-wing, per-setting detection rates reported; pass iff their setting-independence is not rejected at its weight | yes |
| Locality and timing | a light-speed influence from a remote choice to a local record would give a spurious DR-2 signal or a spurious S₁ | for every cross-wing pair of a setting-choice event and an outcome-registration event, the choice lies outside the causal past of the registration: `t_reg − t_choice < L/c` in the laboratory frame (REV O-8) | C-11: timing audit per event from the recorded times; pass iff every pair meets the condition. For T-A also: every setting draw outside the future light cone of the emission or herald | for T-A |
| Measurement independence | settings correlated with the source would void (k4) and (k4′) | local random sources; second settings drawn after the first use | C-1: settings uniform within `β` and mutually independent, and independent of the marker, the event index and earlier records; pass iff no χ² test rejects at its weight. [A-inf] C-1 is necessary for (k4), not sufficient; (k4) remains a hypothesis | yes |
| Memory between events | the apparatus or source carries information from earlier events | martingale-valid bounds (§8.1) | C-10: homogeneity of each wing's record law at `e` across the remote settings at `e − 1` and at `e − 2`; pass iff no test rejects at its weight. A rejection diagnoses a classical coupling between the wings | yes |
| Memory within an event | the second use reads the first use's post-measurement record or system | none: this is what the experiment probes; QM's post-measurement update and LREV R3's readback realization both use it | reported attribute: when the first record is held (§3) | — |
| Prefix | the first use depends on a second setting already fixed | second settings drawn after the first use (§4.1) | C-2: pass iff `P₁₂ = 0` is not rejected at its weight | yes |
| Crosstalk between the wings | a shared mode, a scatter path or a control line carries a remote setting into a local record | locality where reachable | C-5 (positive control, **separate calibration block**, never in production events): a known classical coupling from Bob's `y₂` to Alice's second-use setting injected with a declared probability `p_inj`, fixed at freeze below the planning margin of DR-3; pass iff DR-2 rejects in that block at its weight and the block's estimate of the injected dependence has a confidence interval containing `p_inj`. C-6: DR-2's statistics regressed on first-use strength (arm W scan) and on inter-wing delay; pass iff no slope rejects zero at its weight | yes (C-5); yes for T-B (C-6) |
| Source quality | a weak or mixed source makes DR-1 fail, not the lemmas | — | C-4: countercontrol with a separable source of the same marginals; pass iff `UCB(S₁) ≤ 2` and DR-2 gives `ns-consistent` | yes |
| Instrument repeatability | an imperfect instrument raises ε for reasons unrelated to the remote wing | — | C-3: each wing's repeat-failure rate on a local maximally mixed input (a fair mixture of the setting's eigenstates), with the remote wing idle, for each arm's instrument; it is QM's comparison for DR-5 (REV §3: each wing's reduced input is maximally mixed under every remote policy) | yes |
| Setting fidelity | a misapplied second setting raises ε at a held cell and could fake DR-3a | applied-setting readback per use (§6.1) | C-13: mismatch rates `φ_W` reported per cell; DR-3a subtracts them (§8.2) | yes |
| Analysis | choice of analysis after seeing data | analysis code and constants frozen; data checksum recorded before unblinding | C-8 | yes |
| `⊥` assignment | the assignment rule changes a verdict | the structure-keeping set (§6.3) | C-12: verdicts under each rule of the set reported; an exclusion is claimed only if it holds under all of them | yes |
| Exclusion tests | DR-3a, DR-3 or DR-4 return an exclusion whatever the realization | — | **CC-1 (countercontrol, freeze precondition; specified here, not run):** the frozen analysis code is run on synthetic per-event records, in the §6.1 schema with S-R settings, generated from (i) TSI's (U) candidate at `η*`, `h = 1`; (ii) its fresh replacement of `(R, C)` at each use, case (N); (iii) LREV R3's (S) realization [OFF]; (iv) REV M-1's (U) model. Expected, by hand [A-inf]: (i) DR-1 pass, DR-2 `ns-disagree`, DR-3a `baseline-null`, DR-3 `ns-unresolved` (`ΣΔ = 1`), DR-4 `rep-unresolved`; (ii) DR-2 `ns-consistent`, DR-3a `u-excluded-baseline` (`B = ½`), DR-3 `ns-excludes-U` (`ΣΔ = 0`; correct, since (ii) is not (U)), DR-4 `rep-unresolved` (`Λ = 4`); (iii) DR-2 `ns-consistent`, DR-3a `baseline-null`, DR-3 `ns-excludes-U`, DR-4 `rep-excludes-UN`; (iv) DR-3 `ns-unresolved` under every rule of the structure-keeping set (`ΣΔ = (S₁ − 2)/2` there). Pass iff every expected verdict is returned. Optional: a laboratory emulator with a deliberate classical channel between the wings | yes, before freeze |

[A-inf] The expected values in CC-1. (i) TSI (7): at Bob `(1, 1)`, `b₁ ⊕ b₂ = x₁ ⊕ x₂`, so `Δ_B(1) = 1`
and `Λ ≥ 1`; at fully repeated joint policies `b₂ = b₁` and `a₂ = a₁`, so `B = 0`. (ii) Independent
`(R, C)` per use gives `P(w₂ ≠ w₁) = ½` at every held cell, so `B = ½`, `ΣΔ = 0` and `Λ = 4`; each
wing's two-use history is uniform whatever the remote policy. (iii) `ε = 0` at every held cell and no remote
dependence. (iv) Under `⊥ ↦ c_{A,e}`: `S₁ = 3`, `Δ_A(1) = ½`, `ΣΔ = ½ = (S₁ − 2)/2`, so `LCB(T₃) ≤ 0` in
expectation; under `⊥ ↦ 0` and `⊥ ↦ 1`, REV M-1 gives `ΣΔ = ½`.

## 10. What the outcomes would and would not show for sector C

### 10.1 A positive outcome (row 5 or 6 of §8.3)

Would show, at tier T and with its open loopholes as conditions:
- The agreement condition of U3 §10.3 is met, in whole (row 5) or in its first half (row 6), by a
  performed experiment with raw complete local-history records, which LIT finds absent from the
  papers read.
- **Strict (U), arm P.** A program that `Θ` (S8) identifies with arm P and that reuses an unchanged
  source with the same response functions, meeting (k1) or its dilation, (k2) and (k5), disagrees
  with the data, a raw-direct miss (§A.24). Where DR-3a returns `u-excluded-baseline`, this rests on
  the baseline step alone. Where DR-3a returns `baseline-null` and DR-3 returns `ns-excludes-U`, it is
  conditional on L-2 with (k1)–(k5), on `Θ` (S8) and on Q-2, and it then holds for Bell-violating
  sources specifically. It holds for both RR-1(F) and RR-1(R).
- **Q-3's class.** Conditional on Q-3 and Q-2 with (k1) or its dilation, (k3′), (k4′), and `Θ` (S8):
  a realization in which neither wing's second-use content depends on the first use's outputs or the
  remote first setting disagrees with the data. In arm P this is L-3's (a) and (b) at finite
  repeatability, and RQ-UPD-2's source update is then backed by agreement with a performed
  experiment, in addition to coverage (U3 §10.3, first row). In arm W it is a Q-3 statement only.
- RQ-UPD-1 is then an agreement requirement as well as a coverage one, in arm P: reuse with
  no-signalling complete local histories, for realizations meeting (k1), (k3), (k4), (k5), is case
  (S) or (N), not (U) (conditional on L-2, `Θ` (S8) and, at finite statistics, Q-2).

Would not show:
- that any OI model executes a source update; RQ-UPD's first missing step, "a `φ`-effected source
  update meeting (2)" (U3 §10.1), is unchanged, and no native or executed realization is on record;
- that sector C covers any perceived phenomenon; coverage is shown on no model (U2 §6.1);
- anything about the C/Q relation beyond CQ-2's conditional statement (U3 §10.4);
- a discrimination between PR and quantum statistics: PR has no two-use target law (U3 §4.4), and
  H-RR stays undetermined in all three cases (U3 §10.2);
- anything about realizations without (k4) or (k4′), or about extension operations typed into `Obs`
  (S7(a));
- a separation of case (S) from QM: LREV R3's designed (S) realization [OFF] predicts the same
  records.

Classification [A-inf]. The experiment confronts QM's predictions for local instruments. For OI it is
an agreement check of requirements that the lemmas derive from QM's two-use law; it is not a test of a
prediction OI makes independently of that law. It sits on the consistency axis for sector C's
requirements (§A.23) and is not a correctness result for OI.

### 10.2 A negative outcome

- **`ns-disagree` with every control green (row 3).** One wing's two-use local record law depends on
  the remote policy beyond the bounds. At tier T-A this contradicts QM's no-signalling of local
  instruments, a result whose bearing reaches far beyond sector C. At tiers T-B and T-C the first
  reading is an uncontrolled coupling, which C-5, C-6 and C-10 probe.
  - For sector C it would not confirm case (U) or any OI realization: L-2 states what (U) requires,
    not that nature is a (U) realization. If `ΣΔ` is at or above `(S₁ − 2)/2`, the data are
    compatible with that bound (conditional on Q-2); that compatibility singles out no model.
  - It would remove the agreement ground for RQ-UPD-1 at that tier. RQ-UPD-1's coverage ground (U3
    §10.3) concerns QM's law and would then be in question at the same time.
- **`rep-disagree` (row 4).** The apparatus does not realize QM's repeat law on an entangled wing while
  it does on a single system (C-3). DR-4 then has no bearing. It is a finding about the apparatus or
  about QM's update on entangled wings; it is not evidence for case (U) or (N).

### 10.3 No bearing, unresolved, void

Rows 1, 2, 7, 8 and 10 leave U3's agreement half open in the part not met. None is a negative under
SNR-1.

## 11. Freeze preconditions and open items

Before any adoption of this design as a preregistration (not authorized):
1. **Q-2 and Q-3** (Appendix A) were re-derived and found correct at their stated hypotheses by REV
   §1, with Q-3's scope widened as stated. An owner decision on them and a literature check are owed.
   REV's pointer, marked unverified there, is to bounds on CHSH under relaxed parameter independence.
   If either aid is rejected, §8.2's fallback applies.
2. **`α`, the Bonferroni weights, the martingale bound and its per-event ranges, `β`, the
   structure-keeping `⊥` set, `p_inj`, the CHSH orientation and the arm W Kraus pair and sharpnesses**
   are fixed (§§4.2, 8.1, 9).
3. **CC-1** is run on the frozen code and passes (§9).
4. **Sample size** is fixed from the declared bound and the margin at a conservative S₁; Appendix B
   gives an order of magnitude only.
5. **An apparatus** is identified that combines the additions of §3. LIT does not establish that any
   existing apparatus does; Choi et al. 2020 was read in abstract only.
6. **The invariant-to-checkpoint table** (§A.41) is written: every control of §9 names the record
   field or statistic that measures it and its pass criterion.

Owner questions:
1. Should Q-2 and Q-3 be adopted for DR-3 and DR-4, at the scopes stated in Appendix A, or should
   DR-3 and DR-4 be dropped and DR-3a, DR-2 and DR-5 kept?
2. Is arm W in scope, now that it serves DR-2, DR-3a and DR-4 (by Q-3) but not L-2 or L-3, or should
   the specification be reduced to arm P?
3. Which tier is the target for U3 §10.3's agreement half: T-A only, or T-B and T-C with their
   conditions carried?

## 12. Off-`main` references traced (§A.42 item 8)

| Reference | Claim it supports here | Classification |
|---|---|---|
| U3, BRIEF, U1, U2, LREV on branch `research/ro1-sector-c-1169-20261114` at `6ab9515d` | L-2, L-3 and their hypotheses; RQ-UPD; the register forms; G5; LREV R3's readback realization | **Support off `main`** (gap); U3 r3 and the RR-1 reading owner-accepted (#1169 c.6893058127) |
| LIT on the same branch | the apparatus records of §3; the absence of a qualifying experiment (§1) | **Support off `main`** (gap); owner-accepted (#1169 c.6893058127) |
| r1 and REV on the same branch at `45517959` | r1's text, revised here; REV's countermodels M-1, M-2, the baseline finding, the arm W threshold and its re-derivations of Q-2 and Q-3 | **Support off `main`** (gap) for the countermodels and the threshold, each also re-checked here by hand; provenance otherwise |
| SEL-EXCL-1 (cited through U3) | `T`'s responses (§4.3); the fresh-cell lemma (§7.2) | **Support off `main`** (gap), as in U3 §9 |
| TSI on `main`, blob `65db5a7c` | the first-use law (1), the two-use law (7) and (9), the witness (10), the prefix property, CC-1's (U) and (N) records | **Support on `main`**, at [NP] standing |
| Main:389 and Main:416–423 on `main` | the local CHSH bound; the measurement-dependent route | **Support on `main`** [M] |
| #1169 comments 6892563291, 6893058127, 6893331779 | authorization; accepted scopes; the RR-1 reading | Provenance and governance |

Every statement built on a row marked support off `main` carries that gap (§A.46 item 1).

***

## Appendix A. Design aids Q-2 and Q-3 (author-side hand derivations [A-inf])

Re-derived and found correct at the hypotheses below by REV §1; no owner decision and no literature
check. DR-3 and DR-4 use them only as §11 item 1 states.

**Setting.** (k1) and (k4) of U3 §5.1: deterministic binary first-use responses `A₁(x, y, λ)`,
`B₁(x, y, λ)`, with a law of `λ` that does not depend on the policies. Write
`δ_A(x) := P(A₁(x, 0, λ) ≠ A₁(x, 1, λ))` and `δ_B(y) := P(B₁(0, y, λ) ≠ B₁(1, y, λ))`. `S₁` is the
pinned orientation of §7.1.

**Q-2.** `S₁ ≤ |S₁| ≤ 2 + 2[δ_A(0) + δ_A(1) + δ_B(0) + δ_B(1)]`.

*Derivation.* Set `a′(x, λ) := A₁(x, 0, λ)` and `b′(y, λ) := B₁(0, y, λ)`, local responses, so their
CHSH value `S′` satisfies `|S′| ≤ 2` (Main:389 [M]). For each `(x, y)`, the correlators satisfy
`|E_xy − E′_xy| ≤ 2 P(A₁ ⊕ B₁ ≠ a′ ⊕ b′) ≤ 2[P(A₁(x, y) ≠ a′(x)) + P(B₁(x, y) ≠ b′(y))]`. The four
terms are: `(0, 0)`: 0; `(0, 1)`: `δ_A(0)`; `(1, 0)`: `δ_B(0)`; `(1, 1)`: `δ_A(1) + δ_B(1)`. Sum. The
bound does not depend on which term carries the minus sign (REV §1.1). ∎ REV §1.1 shows it is tight on
a mixture of the PR table with a local table.

*Use in DR-3 (arm P only).* Under case (U) with (k2), (k3), (k5), the proof of L-2 gives, in the (R)
form, Alice's register 0 under Bob `(0, 0)` and `A₁(x, 0, λ) ⊕ A₁(x, 1, λ)` under Bob `(0, 1)`, so
`Δ_A(x) = δ_A(x)`; likewise `Δ_B(y) = δ_B(y)`. Hence `ΣΔ ≥ (S₁ − 2)/2`, that is `T₃ ≤ 0`. In the (F)
form, the TV distance between the two history laws is at least `δ_A(x)`, since the law under Bob
`(0, 1)` puts mass `δ_A(x)` off the diagonal and the law under Bob `(0, 0)` puts none there. In arm W,
(k2) fails (§5) and this use does not apply.

**Q-3.** Let wing A's second-use content not depend on `y₁`, `a₁` or `b₁`: `κ_A = G(λ, ν, x₁)` with
the law of `(λ, ν)` independent of the policies ((k4′)). Then for each `x` and each fixed `y₂`,
`δ_A(x) ≤ ε_A(x; (0, y₂)) + ε_A(x; (1, y₂))`, and likewise for wing B.

*Derivation.* Under Alice `(x, x)` and Bob `(y₁, y₂)`, `a₂ = g(λ, ν)` with
`g := A₂(x, y₂, G(λ, ν, x))`, which does not depend on `y₁`; by (k4′) the law of `(λ, ν)` is the same
for `y₁ = 0` and `y₁ = 1`. Then `P(A₁(x, 0, λ) ≠ A₁(x, 1, λ)) ≤ P(A₁(x, 0, λ) ≠ g) + P(g ≠ A₁(x, 1, λ))`,
and the two terms are `ε_A(x; (0, y₂))` and `ε_A(x; (1, y₂))`. ∎

*Scope (REV §1.2).*
- It uses neither repeatability, nor `Θ`'s identification with the Lüders law, nor (k5′); the ε's are
  measured rates. It holds for any first-use instrument, arm W included.
- Policy-independent noise is dilated: first-use noise into `λ′ = (λ, μ₁)`, second-use noise into
  `ν`; `G(λ′, ν, x₁)` still cannot compute `a₁` without `y₁`.
- It covers unchanged `λ` with fresh local noise per use, which is case (N).
- It is not L-3: it does not state which wing updates, and it says nothing about realizations that
  meet its premise for one wing only.

*Use in DR-4.* Averaging Q-3 over the two values of `y₂` (and of `x₂`) and summing over both wings
gives `Λ ≥ δ_A(0) + δ_A(1) + δ_B(0) + δ_B(1)`. With Q-2: if neither wing's second-use content depends
on the first outputs or the remote first setting, `Λ ≥ (S₁ − 2)/2`, that is `T₄ ≤ 0`. In arm P at
`ε = 0` this reduces to L-3 (a) and (b).

**Shared scope.** No atomic source law is used; a setting-independent herald restricts the argument
to the success branch without changing it; realizations without (k4) or (k4′) are not covered.

## Appendix B. Order of magnitude of the sample size (hand estimate, illustrative)

[A-inf] Each `ε_W(s; π)` term is a conditional rate on joint policies of probability 1/16, so its
inverse-probability-weighted estimator takes values in `[0, 16]`. An Azuma–Hoeffding bound at
per-term level `10⁻⁴` gives a half-width of about `16 · √(ln(10⁴)/(2N)) ≈ 34/√N`. Summing eight such
per-term bounds gives about `270/√N`. With an illustrative `S₁ ≈ 2.55` (visibility 0.9), the DR-4
margin is about 0.27, which needs `N` of order `10⁶` events under this bound. The joint per-event
estimator of the summed statistic has a smaller range than the sum of the per-term ranges, so a single
bound on it is narrower by about a factor of 4 in half-width (REV §6, O-2), and a variance-adaptive
bound narrows it further when the true rates are small, as single-system repeatability of "above
99.6 %" (Leupold) suggests for P-1. These figures are for planning only; they are not predictions and
do not enter the rule.
