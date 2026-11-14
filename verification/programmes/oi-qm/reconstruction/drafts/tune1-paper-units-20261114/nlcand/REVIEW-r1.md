# REVIEW r1 of NLCAND-r1: independent non-author review

**Verdict: REVISE.**

No hand derivation in the document was found wrong (one miscount, R11). The revision is needed because
several headline statements are stronger than the derivations under them: verdict (b) and its H-Bell sentence
(R1), the record convention under which the signalling and the PR-type table are obtained (R2), the joint
statement J1 (R3), the scoring of the kernel no-go as a failure of this candidate and the exact/approximate
split (R4), and the "cheapest decisive check" (R5). Replacement text is supplied for each. The reviewer's own
derivations below are hand derivations, unreviewed, and are offered for the author to re-derive, not to cite.

- **Reviewer.** Non-author; did not write `NLCAND-r1.md` or `NOTES-r1.md`.
- **Method.** Source reading and hand derivation only. No computation on any OI rule or model, no
  enumeration, no simulation, no Lean build. One stored file was opened with a field viewer
  (`stage2/runs/10/results.json` at `a8fff57a`): `verdicts.counts` = 37 / 10 / 70 and headline
  `SIGNALLING-FOUND`, as the document quotes. Read-only: nothing edited, committed, pushed or posted.
- **Pins.** `main` = `c3b5f37a` in `wt-mainread/`; `SM:n`, `Main:n`, `Sub:n` are lines of `papers/*.md`
  there. Lean files are `verification/lean-mathlib/OIBridge/*.lean` there, statements read. `S3`, `S4`, `OA1`,
  `OA2`, `OA3`, `M2`, `PPS`, `PI` as in the document. Off `main`: `3A` = `wt-3a/…/TUNE-1-STEP3A-r3.md`;
  `LP`, `SS` = `wt-tune1plan/…/tune1-landing-20261114/LANDING-PLAN.md`, `STATUS-SOURCING.md`; `LD` =
  `wt-bell/…/bell-ladder-20261113/BELL-LADDER-r3.md`. `NLCAND:n` is a line of the document under review.
- **Tags.** [C] confirmed by my re-derivation or by reading the source; [Rv] reviewer's hand derivation, new
  here, unreviewed.

***

## A. What was re-derived and holds [C]

| Item | Check | Result |
|---|---|---|
| Quotation of the rule (NLCAND:67–69) | compared character by character with SM:112 | verbatim |
| Reading of the rule | `x_{R(i,x)} = sel(x_{i+1}, x_{i+2})`, selector read from the current slice; SM:112 "`R(i,x)` depends only on `x_{i+1}`" | the manuscript's reading; `f_i = u_{i−1} + sel(u_{i+1}, u_{i+2})`; at `q = 2`, `sel = ∨` (M2:157–164) |
| §1.2 bijectivity | `ΨΦ = ΦΨ = id` with `Ψ(a, b) = (b, f(b) − a)`; `σΦσ = Ψ`; SM:112's inverse `u = f(v) − w` is the same map | holds for every `f`, `L`, `q` |
| §1.2 spot check | `f(1,0,0,1) = (1,0,1,1)` on `ℤ₄`, `q = 2` | correct |
| B1 dependency sets | each of `u_{i−1}`, `u_{i+1}`, `u_{i+2}` varied separately, `q = 2` and `q ≥ 3` | correct; `G_φ^{K_nz}` is the nearest-neighbour ring and no larger class has it |
| `K_nz` not closed | `u ≡ 1, v ≡ 2 ↦ 0` for `q ≥ 3`; at `q = 2` the only member that stays is `u = v ≡ 1` | correct (but see R7 for an invariant core at `q ≥ 3`) |
| P8 reflection | `f_{−i}(ρu) = u_{i+1} + sel(u_{i−1}, u_{i−2})`; at `u = δ_{i+2}` the two sides are `0` and `1` | breaks; the undirected selected graph of SM:112 is reflection-covariant, as the document says |
| P10 | `sel(λa, λb) = λ sel(a, b)` for units; shift fails at `u_{i+1} = 0`, `u_{i+2} ≠ 0` | scaling survives, shift breaks |
| B1/B3 directed cone | reads are `i−1`, `i+1`, `i+2`: influence moves `+1` per tick, and `−1` or `−2` | two cells per tick toward decreasing index, one toward increasing |
| B3 corridor lemma | induction re-done for `k = 1, 2` and the general step | correct. The backward cone of `(s−2k, k)` is `[s−3k, s]`, so the hypothesis is used on `3k` cells, both slots |
| B4 (ii) | `P(sel(w, y) = c) = [c ≠ 0]/q + [c = y]/q`; joint law with `x_{a+1}(1)` (which shows `w` when `u_{a+2} = 0`) | total variation exactly `1/q` for the complete history, not only for the one cell |
| B4 (iii) earliest tick | `3 + ⌈(g−1)/2⌉ = 3 + ⌊g/2⌋`; in the window only for `g ≥ 5` | correct; "undecided" is the right label |
| B5 algebra | `β − α = sel(y, x)`; at `q = 2`, `E = (−1)^{x∨y}`, CHSH `= 4`; marginals uniform | correct; PR box up to relabelling |
| B5 one-cell histories, any `T` | `x_j(t+1) = u_{j−1−t}(0) + G` with `G` free of that slot (rightward speed one), triangular | correct: every one-cell history is uniform on `(ℤ/q)^T` under μ-G |
| C1 | bijection preserves the counting law | correct, rule-free |
| C3 erosion | `x_j(1) = 0` guaranteed for `m+1 ≤ j ≤ M−2` | correct, three cells per tick |
| A5 number | `sin(π/17)/8 ≈ 0.0230` | correct |
| Citations spot-checked | OA3:509–511, M2:187–205, OA2:676–682, :794–816, PPS:79, :136–145, :164, PI:288–299, S3:56–76, S4:94–101, :423–474, OA1:103–105, :156–160, :196–200, LD:104, :134, :187–231, :274 | each says what the document attributes to it |

***

## B. Findings

Severity: **major** changes a verdict or headline; **medium** changes a stated scope or status; **minor**
is wording or a slip.

### R1 (major). Verdict (b) is "not established" as argued, and one sentence contradicts B5

- **Location.** NLCAND:49–53 (§0.5), :307–312 (Verdict (b)), :356–358 (§6 "first failure … (b) at B2").
- **Problem.**
  1. Verdict (b) reads "Requirements (i) and (ii) of H-Bell (Sub:133) are not met jointly by this rule". B5
     (NLCAND:269–279) exhibits records for which they are met jointly at one tick: `B`'s record depends on
     `A`'s setting whenever `y = 0`, and both one-cell histories are uniform. The sentence is false for the
     rule and is at most a statement about the member's blocks.
  2. For the member's blocks the support offered is one decided in-window instance (`g = 1`) and an
     undecided family (`g ≥ 5`). One instance plus an undecided case supports "not established", not "not
     supplied" (witness → theorem, in the negative direction).
  3. H-Bell's object is "preparation-indexed adjacency … bounded-degree Bell-relevant long edges" (Sub:131).
     The ring rule has neither (the document's own M3, NLCAND:98–99). Quoting H-Bell's clauses in the
     verdict reads as a test of H-Bell. It is not one.
  4. §6 calls B2 "the first failure on a derivation". B2 is a confinement statement (no dependence for
     `D > 2T`), which Main:414 already states for any graph cone; it fails (b) only for a physical cone at
     least as wide as the rule's own.
- **What can be derived for the member [Rv].** Let `c_L` be the physical speed toward decreasing index,
  which the corpus does not fix (Main:414). If `c_L ≥ 2`, every wing pair outside the physical cone is
  outside the rule's cone and B2 applies. If `c_L < 2`, the record cell at distance two is outside the
  physical cone after one tick, and it signals for the member (B4 (ii) under the complete-history
  convention; R2 item 3 under either convention). So at lattice scale the member has, for every value of
  `c_L`, either no dependence outside the cone or signalling outside it. This uses no undecided case. It
  is a statement about one-tick, two-cell separations; it says nothing about wings separated by many cells
  under μ-G, where B4 (iii) stays undecided and R15 bounds the effect.
- **Proposed replacement for NLCAND:307–312.**
  > **Verdict (b). Member: not supplied at lattice scale; rule: not established.** Outside its own cone
  > the rule gives no parameter dependence and is Bell-local under (xiv) (B2). For the member's blocks,
  > whatever speed `c_L ≤ 2` is taken as physical toward decreasing index, either `c_L = 2` and B2 covers
  > every pair outside the cone, or `c_L < 2` and a record cell two cells from the remote generator signals
  > after one tick (B4 (0), (ii)). For wings many cells apart under μ-G the in-window case is undecided
  > (B4 (iii)). With one-cell records the dependence is present without signalling and the table is of PR
  > type (B5); that is a statement about one record convention and does not select the quantum set. The
  > ring rule has no preparation-indexed long edge (M3), so none of this tests H-Bell (Sub:131–133).
- **Proposed replacement for NLCAND:356–358.** "…In TUNE-1's form (a) is undecided. For (b), B2 confines any
  effect to `T < D ≤ 2T` toward decreasing index, and the decided instances inside that window signal for
  the member (B4)."

### R2 (major). The signalling value `1/q` and the PR-type table both need the record cell's pre-setting slot; Main's Bell conditions do not grant it

- **Location.** NLCAND:114 (readout row), :252–255 (B4 (ii)), :269–279 (B5), :406–407 (F4, F5).
- **Sources.** Main:369–372: wing `A`'s outcome is "a ±1-valued function of the state on a readout region
  `R_A` `k_A` updates after the setting". The state one update later holds `(x(1), x(0))` on `R_A`; it does
  not hold `v(0) = x(−1)`. The document's readout is the complete history from `t = 0`, "imported
  convention" (NLCAND:114; 3A:501; LD:198–200), which does hold `v(0)`. OA-2's own design runs both
  conventions separately (OA2:803–805), and LD:274 lists the record convention as open.
- **Derivations [Rv].**
  1. *B4 (ii) under Main's readout.* `x_{a+2}(1) = u_{a+1} + sel(w, y) − v_{a+2}(0)`. Under μ-G `v_{a+2}(0)`
     is uniform, independent of every other slot, and absent from `A`'s state at tick 1 and from everything
     `B` holds. So `A`'s state at tick 1 has the same law for every `y`: total variation `0`. By Lemma M
     (S4:94–101) with `U = A ∪ B`, the two states at tick 1 are functions of each wing's own `u(0)` content
     and private pads, so the table is a product given the settings, hence Bell-local. The member's ready
     cell (`a+1` at `(0, 0)`) does not change this at `g = 1`: it unmasks `x_{a+1}(1)`, which reads `w`, not
     `y`.
  2. *B5 under Main's readout.* `β = x_i(1) + v_i(0)` uses `v_i(0)`. Without it `x_i(1)` is masked by
     `v_i(0)` and is independent of `α`: no PR-type table.
  3. *An instance that signals under either convention, missed by B4.* Take `g = 0`, so `B`'s generator is
     cell `a+3`, and the member's own ready cell `a+1` at `(0, 0)` (NLCAND:116). Then
     `x_{a+1}(1) = u_a + sel(u_{a+2}, y)`. `A` holds `u_a(0)` and `u_{a+2}(0)` at tick 1 in either convention,
     so when `u_{a+2}(0) = 0` it reads `y` exactly: total variation `1` at that own content, at distance two
     after one tick. This is A1's gated read (NLCAND:165–169) with the remote generator in the place of the
     unread cell.
  4. *General form.* An observer that knows `u_{j−1}(0)` and `v_j(0)` and sees `x_j(1)` learns
     `sel(u_{j+1}, u_{j+2})(0)`. Knowledge of `v_j(0)` is the resource: a held pre-setting record, a ready
     slot, or a label slot. Under μ-G alone with single-time readout it is absent.
- **Consequence.** "For the member's observer blocks it signals" (NLCAND:51–52) is true for the member as
  specified, and the convention on which it rests is the writer's import, not the manuscript's Bell
  condition. F4 and F5 are results under that convention.
- **Proposed addition after NLCAND:262** (a new item B4 (0) and a table):
  > *(0) Adjacent blocks, `g = 0`, with the member's ready cell.* `x_{a+1}(1) = u_a + sel(u_{a+2}, y)`: when
  > `u_{a+2}(0) = 0`, `A` reads `y` exactly. Total variation `1` at that content, under the complete-history
  > readout and under a single-time readout of `A`'s state at tick 1.
  >
  > | Records | Slots known beforehand | `g` | Law of `A`'s record against `y`, `T = 1` |
  > |---|---|---|---|
  > | complete history of the block (member) | none | 1 | total variation `1/q` |
  > | state of the block at tick 1 (Main:369–372) | none, or the member's `r_O` | 1 | `0`; table Bell-local |
  > | either | member's `r_O` | 0 | `1` when `u_{a+2}(0) = 0` |
  > | complete history of one cell | none | any | `0` at every `T`; PR-type table at one tick (B5) |
  > | either | a blank corridor of `3D/2` cells, both slots | any | `1` at tick `D/2` (B3) |
- **Proposed edit to F4 (NLCAND:406).** "One-hop signalling of the three-cell member with complete-history
  records, total variation `1/q` (B4 (ii)); absent for a single-time readout of the block; total variation
  `1` at `g = 0` with the ready cell under either readout (B4 (0))."
- **Proposed edit to F5 (NLCAND:407).** Append: "; the table needs the record cell's pre-setting slot
  `v_i(0)` and is absent for a single-time readout".

### R3 (major). J1 is a conditional statement about a corridor; the stated (b)–(c) exclusion is not derived

- **Location.** NLCAND:58–59 (§0.7), :250–251 (B4 (i) "the resource requirement (c) asks for"), :359–362
  (J1), :408 (F6).
- **Problem.**
  1. What is derived is B3: a contiguous line of `3D/2` cells blank in both slots, from below `A`'s record
     cell up to `B`'s generator and including `A`'s own cells, carries a value at two cells per tick. J1
     states it for "any supply of blank cells … along a line" and then as "(c) and 'no signalling outside
     the reference cone' exclude each other".
  2. Requirement (c) as the records define it is "a native producer … of known-value cells for `r_{O,n}`
     and the program blocks, renewed every run" (LP:245; SS:59–60). It does not ask for a blank line
     spanning the two wings. A supply confined to each observer's own cells meets (c) and builds no
     corridor.
  3. The faster channel is not opened by the supply. It is present under μ-G with no known cell at all
     (B4 (ii), total variation `1/q`). Known cells raise the value; they do not create the channel.
  4. "Twice the reference-class speed" presupposes that the reference class is `K_nz` and that `q ≥ 3`. At
     `q = 2` nothing propagates in `K_nz` (NLCAND:291–292), and under the "vacuum" reading of the reference
     class (all-zero configuration, NLCAND:96–97) the two-cell speed *is* the reference speed (R7).
- **What is derivable [Rv].** The local form: three adjacent known slots suffice for a certain read at
  distance two after one tick (`u_{j−1}(0)`, `v_j(0)` known and `u_{j+1}(0) = 0`; R2 item 4). The member's
  own `r_O` together with a label `u_{a+2} = 0` is such a pattern. So a known-value supply placed at an
  observer's cells gives that observer a two-cell read; whether a supply meeting (c) yields signalling over
  many cells depends on its layout, which no source fixes.
- **Proposed replacement for NLCAND:359–362.**
  > **J1 (conditional) [H].** If a line of `3D/2` consecutive cells is blank in both slots from below `A`'s
  > record cell to `B`'s generator, the two-site edge is a deterministic channel toward decreasing index at
  > two cells per tick (B3, B4 (i)). Locally, an observer that knows `u_{j−1}`, `v_j` and has `u_{j+1} = 0`
  > reads cell `j+2` after one tick; the member's ready cell with label `u_{a+2} = 0` is such a pattern
  > (A1, B4 (0)). Requirement (c) does not by itself ask for a line between the wings, so J1 is a
  > constraint on where a supply may be placed, not an exclusion of (c) by (b). The channel is not created
  > by the supply: under μ-G it is already open with probability `1/q` per hop (B4 (ii)).
- **Proposed replacement for NLCAND:58–59.** "A line of known zero cells between the wings turns the
  two-site edge into a deterministic channel at two cells per tick (J1, conditional on that layout)."
- **Proposed replacement for F6.** "J1: a blank line between the wings is a deterministic two-cell-per-tick
  channel; a known-value supply at an observer's own cells gives a two-cell read | new; conditional on
  layout".
- **Proposed edit to NLCAND:250–251.** Delete "This is the resource requirement (c) asks for (J1)"; write
  "This needs a prepared line of `3D/2` blank cells, which is more than (c) asks for (J1)".
- **Missing link to state.** Requirement (a)'s only supplied ingredient (A1) and the signalling of (b) are
  one mechanism: the gated read at label `0` reads a cell at distance two after one tick. §6 states a
  (b)–(c) relation and omits this (a)–(b) one.

### R4 (major). The kernel no-go does not see the rule; it is not a failure of this candidate, and "exact versus approximate" is the wrong axis

- **Location.** NLCAND:46–48 (§0.4), :56–57 (§0.7), :153 (P17), :185–193 (A3), :212–213 (Verdict (a)),
  :355–356 (§6), :403 (F1), :413–414.
- **Lean statements, as read.**
  - `obsTheory 𝒮 := permTheory 𝒮.Conf` (`SubstratumInterfaceAudit.lean`:770–771), with
    `obsTheory_eq_permTheory … := rfl` (:775) and `obsTheory_rule_independent (R R' : Rule ι V) :
    obsTheory {…, R := R} = obsTheory {…, R := R'} := rfl` (:780–782). Hypotheses: finite sites and
    alphabet, nothing on the rule. The file header: "The observer theory depends on the substratum only
    through its configuration space … configuration-level sourcing consumes nothing of A3–A6" (:34–35).
  - `sourcing_rule_independent … (P : FiniteOperationalTheory (ι → V × V) → Prop) : P (obsTheory R) ↔
    P (obsTheory R') := Iff.rfl` (`FrozenSourcing.lean`:295–298), docstring "under the present interface".
  - `frozen_sourcing_verdict : ¬ PhasesAvailable (permTheory (Fin 2)) ∧ ¬ DenseUnitaryControl
    (permTheory (Fin 2)) ∧ ¬ DerivedOI (permTheory (Fin 2))` (:318–323). No substratum and no rule occur.
    `DenseUnitaryControl` is an approximation property (`DiscreteCompletion.lean`:45–48: every unitary is
    within `ε` of an available one, for every `ε > 0`), and `nonnegBounded_not_denseUnitaryControl`
    (:173–184) with `obsTheory_nonnegBounded` (:84–86, every substratum) is its ceiling.
  - `substratumGen_not_control : ¬ HasCompositeUnitaryControl (genTheory substratumClass
    substratumClass_arch (Fin 2))` (`StructuralClosure.lean`:348–356), `substratumClass` being the monomial
    operators (:180). Two-valued carrier; no substratum, no rule, no region, no measure.
  - `obs_not_layerFlowExecutable {g : Equiv.Perm 𝒮.Conf} (hx : g x ≠ x) : ¬ LayerFlowExecutable
    (obsTheory 𝒮) g` (`ExecSource.lean`:129–134), with "Not claimed: … anything about a richer observer
    architecture than the stated one" (:29–30).
- **What is rule-independent, and where.** The object `obsTheory 𝒮` is built from the configuration set
  alone: the theory generated by the read-write exchanges on the whole phase-space configuration set, its
  operations acting on matrices indexed by configurations. The rule is not an input, so rule independence
  holds by definition (`rfl`), not by a property that rules share. There is no region, no hidden sector, no
  law and no record history in that object. The document's sentence "the kernel result holds for every
  substratum rule within the stated observer architecture" is correct. Its uses of it are not:
  1. **It cannot be a failure "of the candidate".** §0.7 and §6 rank it as the first of the candidate's
     failures. A statement that takes the same value for every rule does not test a rule; scoring it
     against this candidate is a non-discriminating control.
  2. **It gives no information about a rule change at an interface where the rule enters.** "The control
     gap does not trace to linearity" (NLCAND:190–191) is true at the configuration-level interface and
     only there. The same `rfl` equally fails to show that linearity is innocent of the TUNE-1 obstruction;
     the document's own A1 shows that at the record-law interface the rule does matter (Lemma A-T's
     dichotomy holds for R-lin and fails here). F1's "assumption-watch for any plan that expects a rule
     change to supply mixing" is therefore too wide.
  3. **The kernel ceiling is not only exact.** The dense (every-`ε`) ceiling holds at the same interface
     (`permTheory_dense_ceiling`, :187–188). The line between the kernel statement and TUNE-1's T1 is the
     interface, not exactness: T1 is a condition on record laws of a region under a law (3A:783–812:
     "`d_K(I, 𝔔) ≤ ε` over complete multi-time records"), which a classical hidden-variable model can meet
     for one qubit (control C-POS-1, 3A:837). §0.7's "in exact form … in TUNE-1's approximate form" misnames it.
- **Prior art to cite.** 3A:498 already records "the observer theory is rule-independent [K]".
- **Proposed replacement for A3's heading and first sentences (NLCAND:185–191).**
  > **A3. Operator-level mixing at the configuration-level interface. Not a test of the candidate [K].**
  > The kernel's observer theory is `permTheory` on the configuration set, and the rule is not an input to
  > it (`obsTheory_rule_independent`, `SubstratumInterfaceAudit.lean`:780–782, by `rfl`;
  > `sourcing_rule_independent`, `FrozenSourcing.lean`:295–298). At that interface no unitary mixing is
  > available, exactly (`obs_not_layerFlowExecutable`, `ExecSource.lean`:129–134;
  > `substratumGen_not_control`, `StructuralClosure.lean`:348–356, two-valued carrier) or to within every
  > `ε` (`permTheory_dense_ceiling`, `FrozenSourcing.lean`:187–188; `obsTheory_nonnegBounded`, :84–86).
  > The statement has the same value for the linear rule and for this one, so it neither counts against
  > the candidate nor bears on whether a rule change helps at the record-law interface of TUNE-1.
- **Proposed replacement for §0.4 (NLCAND:46–48).** "…Operator-level mixing at the kernel's
  configuration-level interface: unavailable for every rule by construction of that interface [K]; not a
  test of this candidate. TUNE-1's single-qubit target, a condition on record laws: undecided; the gap is
  the ring-rule analogue of NL-P (R6)."
- **Proposed replacement for §0.7 first sentences and §6 "First failure" (NLCAND:56–57, :355–358).**
  "One mechanism does not meet all three. The kernel no-go is rule-blind and is not scored. Of the
  requirements that depend on the rule, (a) is undecided at TUNE-1's interface and (b) is the first with a
  derived defect for the member (R1)."
- **Proposed replacement for F1 (NLCAND:403).** "The kernel's observer theory does not take the rule as
  input, so its control ceiling is the same for every rule; it does not bear on rule changes at the
  record-law interface (A3) | CONFIRMING of Main:588 and 3A:498; assumption-watch for plans that read the
  kernel no-go as evidence for or against a rule".
- **P17 (NLCAND:153).** Replace "survives | rule-independent (A3)" by "unaffected | the statement does not
  take the rule as input (A3)".

### R5 (medium). The "cheapest decisive check" is not about the member, is not decisive for any verdict, and omits a standing owner condition

- **Location.** NLCAND:195–198 (A4), :363–374.
- **Problem.**
  1. The member's observer is three cells with `L ≥ 4T + 8` (NLCAND:111, :113). The check is OA-2's row for
     a two-cell observer on `ℤ₅` with `T ≤ 4` (OA2:814), where `L = 5 < 4T + 8` and paths wrap. A4 itself is
     worded for "observers of at most two cells". Neither is a node about the specified member.
  2. By the document's own account neither outcome moves verdict (a), (b), (c) or the joint verdict
     ("classical at that size, horizon and convention only" / "not T1"). It decides N-b at one size. It is
     not decisive for the question the document was asked.
  3. LP:19–21 quotes the owner: "Do not authorize Step 3B, a new candidate search, or a G_SM computation
     until a physically justified O-RDY resource exists and the relevant candidate class is adequately
     specified." Verdict (c) says the first condition is unmet and NLCAND:122–125 says the second is. "Needs
     its own authorization" understates this: on the document's own findings the stated preconditions fail.
  4. The description drops two frozen items of the OA-2 row: site 0's `v`-slot as preparation label, and
     the two record variants run separately (OA2:803–805, :814). After R2 the second is the variable that
     matters.
  5. For the B4 (iii) computation the control "`R ≡ i+1` must give total variation `0` (Proposition AL)" is
     vacuous: at `D = 6 > T = 5` the nearest-neighbour rule gives `0` by the cone lemma, whatever the
     program does with masking.
- **Proposed replacement for NLCAND:363–374.**
  > - **Undecided nodes.** A4 (small observers, including the member at `T < 4L − 10`; OA3:89–92) and
  >   B4 (iii). No computation is proposed here: the owner's stated conditions for a `G_SM` computation
  >   (LP:19–21) are unmet on this file's own findings (verdict (c); §1.4). For the record, the design that
  >   exists is OA-2's `G_SM` row (OA2:796–814), with both record variants and three amendments
  >   (OA3:91–92); it concerns a two-cell observer on `ℤ₅`, not the member, and either outcome decides
  >   condition N-b at that size only. A B4 (iii) computation would need controls that can fail: the
  >   linear ring inside its cone (`D ≤ T`), where Proposition AL predicts total variation `0` or `1`
  >   (LD:187–231); `g = 1` giving `1/q`; a blank corridor giving `1`; and a single-time readout of the
  >   block giving `0` at `T = 1` (B4 table).

### R6 (medium). Names taken from TUNE-1 are used for a different rule; one negative is false as worded

- **Location.** NLCAND:4–5 (header), :45 (§0.3), :48, :90–93 (M1), :200 (A5), :213, :411 (F9).
- **Sources.** S4:30–39: "R-nl is the rounded bijection of SM:294"; "H-nl is the named hypothesis 'the
  world's rule is R-nl'". S4:605–606: NL-P is "Exhibit an R-nl family in `𝕀_D` …". TUNE-1's carriers are
  `Λ_{L_tor} = (ℤ/L_tor ℤ)^3` and `ℤ^3` (S4:26–28). SM:294 writes the rounded rule, a non-linear rule in
  `d = 3`.
- **Problem.**
  1. The header defines H-nl as "the world's rule is non-linear". That is a wider hypothesis under an
     existing name.
  2. "The gap is NL-P" names a gap that is defined for R-nl families on three-dimensional carriers. The
     ring rule is not R-nl and its carrier is outside TUNE-1's schema, a point A5 does not state.
  3. §0.3 "no `d = 3` rule exists" and F9 "No `d = 3` non-linear rule is written" are false as worded:
     SM:294 writes one. `NOTES-r1.md` §3 has the correct statement; the main file does not.
- **Proposed replacements.**
  - Header: "The hypothesis that the world's rule is this ring rule (written H-ring below; it is not
    TUNE-1's H-nl, which names the rounded rule of SM:294, S4:37–39) is unadopted throughout."
  - §0.3, last sentence: "Every `d = 3` result is undetermined, because no `d = 3` version of the ring rule
    is written."
  - §0.4 and Verdict (a): "the gap is the ring-rule analogue of NL-P (S4:605–606, which is stated for
    R-nl)".
  - A5, add: "TUNE-1's schema is stated on three-dimensional tori and `ℤ^3` (S4:26–28); the ring is outside
    it, so T1 would first have to be restated for a ring."
  - F9: "No `d = 3` rule with a state-dependent graph is written; the `d = 3` non-linear rule that is
    written (the rounded rule, SM:294) is a different rule and is not assessed here".

### R7 (medium). "Reference class only" rests on the writer's choice of `K_nz`; under the manuscript's wording ledger (x) fails for this rule

- **Location.** NLCAND:43–44 (§0.3), :94–97 (M2), :132–133, :141–143 (P5–P7), :405 (F3).
- **Sources.** Main:724 (x): "on the reference vacuum/uniform state class the coupling graph `G_φ^ref` … is
  the simple-cubic graph". SM:124: the mod-`q` proof is "With uniform initial conditions". M2 of the
  document already notes that the all-zero configuration and the support of the uniform law both give the
  two-site graph.
- **Problem.** The two readings the manuscript's words suggest ("vacuum", "uniform") give "breaks" for P5–P7.
  `K_nz` is the one class on which they hold, it is chosen by the writer after computing B1, and §2 then
  labels the outcome "reference class only". That is the favourable reading and should carry the choice in
  the label (§A.31).
- **Addition [Rv].** `K_nz` is not closed, but for `q ≥ 3` it has a non-trivial invariant part: for any
  `b : ℤ/L → {0, 1}`, `x_i(t) = 1 + b(i + t)` takes values in `{1, 2}`, so `sel` returns its first argument
  at every step and `x_{i−1}(t) + x_{i+1}(t) − x_i(t−1) = 1 + b(i + t + 1)`. These `2^L` trajectories obey
  the nearest-neighbour rule for all time and move rigidly toward decreasing index. The statement "the
  dynamics does not preserve [the reference class]" holds for `K_nz` and not for its invariant part, which
  the document does not identify.
- **Also.** SM's `G(x)` is the selected-neighbour graph (it drops the edge `i → i+1` when `x_{i+1} = 0`,
  SM:112 "undirected degree in [2, 4]"); Main:362's `G_φ^K` is the dependency graph, in which `i+1` stays an
  in-neighbour. M2:187 notes the same point. B1 uses Main's; one sentence should say that the two differ.
- **Proposed replacement for NLCAND:132–133.** "'`K_nz` only' means: holds on `K_nz`, the configurations
  whose current slice has no zero (B1). `K_nz` is the writer's choice of the class on which ledger (x) can
  hold; on the all-zero configuration and on the support of μ-G the entry is 'breaks' (M2)."
  Rename the outcome in P5–P7 from "reference class only" to "`K_nz` only; breaks on the vacuum and
  uniform readings", and in §0.3 write "survive only on `K_nz`, a class chosen here, which the dynamics
  does not preserve (for `q ≥ 3` an invariant part exists and is not characterized)".

### R8 (medium). The preserved-results list is drawn from a partial reading and omits results SM names

- **Location.** NLCAND:129–158 (§2), :380–381 (§7).
- **Sources.** SM:110: "Under these constraints, the uniform-class Markov area-law bound holds, center
  independence is preserved, **the gap equation is unchanged**, and the form lemma of §4.1 applies at each
  step." SM:222: "a real/complex wave operator is an observer-level lift". SM §4.2 (:284): factorization
  into Dirac operators, an identity for the linear lattice operator. SM:296 and Sub:135: the conserved
  quadratic invariant of the exact linear rule. `NOTES-r1.md` §2: `papers/GR.md`, `papers/Structure.md` and
  the book were not read.
- **Problem.** §A.29 asks for the preserved results to be stated in advance and to serve as controls. The
  list has no row for the gap equation (which SM:110 claims survives for this class), the observer-level
  linear lift and what is built on it (§4.2 onward, also in `d = 1` form), or the conserved quadratic
  invariant. GR and Structure were not searched (§A.19). The statement that the first column "was fixed
  before §§3–5 were written" cannot be checked by a reader of a single undated draft.
- **Proposed addition to §2** (rows, outcomes to be derived by the author, not asserted here):
  "P19 gap equation (SM:110; GR §3) | to assess"; "P20 observer-level linear lift and the Dirac
  factorization built on it (SM:222, §4.2) | to assess; the lift's premise is a linear rule"; "P21
  conserved quadratic invariant (SM:296; Main:724 (v)) | to assess". And a bound: "The list is drawn from
  SM §3.1, Main §3.3–3.4 and the ledger; `papers/GR.md`, `papers/Structure.md` and the book were not
  searched, so it is not a complete inventory."
- **Proposed edit to NLCAND:131–132.** Delete the sentence on the order of writing, or replace by "The list
  was drawn up from the sources named above; it is not a dated preregistration."

### R9 (medium). Which verdicts depend on the writer's choices

- **Location.** NLCAND:104–125 (§1.4); `NOTES-r1.md` §6.
- **Manuscript's.** The update, ring, alphabet, memory sign, distinguished value, jump length (SM:112); a
  visible sector of "one site's two time slices" and "the uniform hidden prior", both for the
  P-indivisibility remark only (SM:112).
- **Writer's.** Three-cell observer; complete-history readout; control region; ready cell; one-cell
  generators with `u`-slot settings; wing layout; `L ≥ 4T + 8`; `K_nz`; μ-G as the law at the setting
  slice.
- **Sensitivity, by verdict.**

  | Verdict | Depends on | Effect of changing it |
  |---|---|---|
  | A1 supplied | none (pointwise property of `f`) | — |
  | A3 | nothing in the candidate (R4) | — |
  | A5 bound `0.023` | `|C| = 2`, `q = 2` | NL-C′ gives the general form |
  | B2 Bell-local outside the cone | (xiv) | as Main |
  | B4 (ii) signalling `1/q` | complete history, two adjacent held cells | `0` for a single-time readout; `0` for one-cell records (R2) |
  | B5 PR-type table | one-cell records, complete history, interleaved generators | absent for a single-time readout; signals if `B` holds its generator cell (NLCAND:283–286) |
  | C1 | μ-G | undecided under μ-O, μ-R |
  | P5–P7 | `K_nz` | "breaks" on the other readings (R7) |
- **Note.** The one-cell record that §1.4 labels "not the member's observer … chosen to exhibit the gadget"
  is the only visible sector SM:112 itself names for this rule; the three-cell block is the writer's. The
  member also sits in the class OA-3 closes at long horizons (three consecutive held sites), while the open
  case is smaller observers (OA3:89–92). The document should say that the member was chosen where results
  exist, not where the question is open.
- **Proposed addition after NLCAND:125.** The table above, with the sentence: "Verdicts B4 (ii), B5 and
  P5–P7 are properties of these choices; A1, B2, B3 and C1 are not."

### R10 (minor). Verdict (c): "not supplied" should be "no unconditional supply"

- **Location.** NLCAND:54–55, :318–321, :346–347, :409 (F7), :336–337.
- **Sources.** LP:248: "An unconditional supply excluded under μ-G, heralding the only route there"; OA1
  D3 (:156–160).
- **Check against the O-RDY definition.** The argument is right for what it covers: under μ-G every slot is
  uniform at every tick, so no native process leaves a cell at a prescribed value with probability above
  `q^{−1}` per slot, whatever the rule. It does not exclude the heralded route, which C1 itself prices at
  `q^{−M}`, and under the member's complete-history convention cells are known as functions of records
  (C2). "Undecided" under μ-O and μ-R is right; nothing in the sources decides either for this rule.
- **Proposed replacements.** §0.6 and Verdict (c): "No unconditional supply under the uniform counting law,
  for any bijective rule; a heralded supply costs `q^{−M}` for `M` slots. Undecided under …". F7: "Under
  μ-G a bijection preserves the counting law whatever its form, so non-linearity adds no unconditional
  producer…". NLCAND:337: "nothing renews it" → "no renewing process is identified".

### R11 (minor). Slips

- NLCAND:180–181: `f_i = u_{i−1} ⊕ u_{i+1} ⊕ u_{i+2} ⊕ u_{i+1}u_{i+2}` is one doubly-controlled flip with
  **three** singly-controlled ones (or one OR-controlled flip and one singly-controlled), not two.
- NLCAND:146: the identity `f(δ_{i+1} + δ_{i+2}) − f(δ_{i+1}) − f(δ_{i+2}) = −1` holds at component `i`;
  say so.
- NLCAND:186: `ExecSource.lean`:125–134 → :129–134; add the two statements that carry the claim directly,
  `obsTheory_rule_independent` (`SubstratumInterfaceAudit.lean`:780–782) and `sourcing_rule_independent`
  (`FrozenSourcing.lean`:295–298).
- NLCAND:393–395: "It does not meet the requirements; the variants that might are the adjustable ones" →
  "It is not shown to meet the requirements; the variants not examined here are the adjustable ones."
- NLCAND:233–234: "The rule as written therefore cannot serve wings whose separation exceeds twice the
  window" — add "toward decreasing index; toward increasing index the bound is the window itself".

***

## C. Missing analysis before the candidate could be called failed or viable

1. **Record convention (R2).** A statement of every in-cone result under the manuscript's Bell readout
   (Main:369–372) beside the complete-history one, and the `g = 0` instance.
2. **Coarse-scale behaviour under μ-G [Rv, sketch to be re-derived].** A record at distance `D > T` can
   depend on the remote setting only along a dependency chain with at least `D − T` two-cell steps, each
   needing its gate cell to be `0` on the trajectory. The gate cells of one chain lie on a line that
   recedes faster than one cell per tick, so each has its own left-chain pad and their values are jointly
   uniform; one chain is open with probability `q^{−k}`, `k ≥ D − T`. Hence the probability `P(N)` that
   the record depends on the setting is at most the sum of `q^{−k}` over chains, and under (xiv)
   `|S_CHSH| ≤ 2 + 2P(N)` (local on the complement). At `g = 1`, `T = 1` this is exact: `N = {w = 0}`,
   `P(N) = 1/q`, so `|S_CHSH| ≤ 2 + 2/q`, which is below `2√2` for every `q ≥ 3` and at most `3` at `q = 2`,
   whatever the outcome functions. The general count of chains was not carried out; for small `q` the
   bound does not decide B4 (iii). If it holds, in-window dependence and in-window signalling are both
   small for large `q` and large gain `D − T`, which is neither a Bell mechanism nor a signalling defect at
   coarse scale.
3. **The invariant part of `K_nz` (R7)** and, with it, whether any class on which the nearest-neighbour
   graph holds has positive weight under the law used.
4. **Dynamics off `K_nz`.** Typical configurations under μ-G have zeros, so propagation is two cells per
   tick one way and one the other (B3). P7 and P8 then read "breaks for typical states", and SM:108 (iii)
   holds only for the undirected graph. Whether any isotropic long-wavelength behaviour survives is not
   examined; a reader would need it before "viable".
5. **Cycle structure and conserved quantities of the ring rule.** Needed for μ-O (C4), for ledger (v)
   (P18) and for P21 (R8). Only the constant fixed pairs are identified.
6. **The rows R8 adds to the preserved list**, and a search of `papers/GR.md` and `papers/Structure.md`.
7. **A `d = 3` version and a long-edge version.** Without them nothing here bears on the gauge sector (the
   document says so) or on H-Bell (R1 item 3). Both are different candidates with free parameters of the
   kind §7 lists.
8. **The instruction's record.** `NOTES-r1.md` §1 says no Issue or comment id was supplied. S4:608–611
   records "No further work on these gaps [NL-A / NL-P] is authorized" and LP:19–21 excludes a new
   candidate search; the instruction that supersedes them should be quoted with author and time before
   this file is cited anywhere (§A.42 item 7).

***

## D. Answers to the seven review questions

1. **The rule.** Quoted exactly; the reading is the manuscript's; bijectivity and the inverse hold. The
   verdicts that are artefacts of writer's choices are listed in R9: the `1/q` signalling value and the
   PR-type table (record convention and observer size), and "reference class only" (`K_nz`).
2. **Preserved-results list.** Each entry checked holds as a statement; `K_nz` not closed, shift and
   reflection covariance broken are all correct. The label "reference class only" hides a choice (R7), and
   the list is incomplete (R8).
3. **Control.** Rule independence is definitional at the configuration-level interface (`rfl`), covers the
   exact and the every-`ε` operator ceilings alike, and carries no information about a rule change at the
   record-law interface where TUNE-1's target lives. It should not be scored as this candidate's failure
   (R4).
4. **Bell.** Cone, corridor, `1/q` and the PR-type table are all correct. "Not supplied" is justified for
   the member at lattice scale only through the cone dichotomy of R1, which the document does not state;
   as argued it is "not established", and for the rule (as opposed to the member) only "not established".
   B4 (ii) and B5 both assume the complete-history readout; Main:369–372 uses a single-time readout, under
   which both vanish at one tick (R2). The one-cell table is no-signalling because every one-cell history
   is uniform under μ-G whatever happens elsewhere; it shows that the update has the form of the ladder's
   `φ_×`, and nothing about separated wings, realistic records or the quantum bound.
5. **Cell supply.** The argument is right for unconditional supply and is rule-free; "undecided" is right
   for the other two laws. The wording should keep the heralded route (R10).
6. **Joint verdict and scope.** The (b)–(c) conflict is a conditional statement about a corridor layout,
   not a derived exclusion (R3). Sentences that generalize: §0.7 "(a) fails first, for every rule of the
   form (xiii)" and F1 (to the whole class, from a rule-blind statement; R4); Verdict (b) "(i) and (ii) of
   H-Bell … not met jointly by this rule" (to the rule and, by reading, to H-Bell; R1); F7 without "under
   μ-G" (R10); the header's definition of H-nl (R6). The "cheapest decisive check" is well posed for
   OA-2's instance and is neither about the member nor decisive here (R5).
7. **Missing analysis.** Section C.
