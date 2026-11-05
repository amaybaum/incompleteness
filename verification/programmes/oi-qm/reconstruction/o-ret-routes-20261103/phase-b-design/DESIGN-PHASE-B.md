# O-RET Phase B: native-retention design

**Status: WIP / UNVERIFIED.** A paper-only design under #1032 comment 6649418760, revised after
two independent reviews: of `fdacce54` (#1115 c.6649925951) and of `5839e064` (#1115
c.6650383732), both ACCEPT WITH CHANGES. The work continues under the owner's decision #1032
c.6649977592. This revision is not re-reviewed. The design is not frozen and not authorized to run. It adopts no premise and selects no candidate. No computation, enumeration,
simulation, script or Lean build was run for it; every value below is a hand derivation, marked as
such.

**Governing principle for the test.** Owner, #1032 c.6649977592 (amaybaum, 2026-11-05T04:49:59Z):
"a test must be able to fail even when all its declared assumptions hold. A positive result that a
decoder guarantees by construction cannot establish independent retention. This guides G-4 and
G-5." §1.3 (Observation D2-T1 and Proposition IP′) and §6.4 (the counting rule) apply it.

**Support labels.**
- **[PA]** Phase A evidence on `main`: the frozen inputs at `F = 49f0bd41` and `phaseA/run-1/`.
- **[R]** `ROUTES.md` at `F`. It is in `main`'s history, but no review record of it is on `main`,
  so its lemmas are used here as design motivation, never as premises (programme `README.md:30–35`;
  AGENTS.md §A.46 item 7).
- **[DP]** `DESIGN-PULSE.md` r6, frozen at `F`. Its reviews are on PR #1078, off `main`; the same
  restriction applies.
- **[MR]** the frozen MR-1 record `../measurement-record-formation/amendments/MR-star.md`.
- **[O]** an owner decision recorded on #1032 or #914, quoted with its comment id.
- **[D]** a paper derivation made here. Unreviewed. None is an established result.
- **[L]** literature. Section 9 says which items were read directly.

`D:n`, `P:n`, `R:n`, `MR:n` are line numbers of `DESIGN-PULSE.md`, `PREREG-PHASE-A.md`, `ROUTES.md`
at `F`, and `MR-star.md`, all at `D` = `f5c281ae`.

***

## 1. Starting point (a)

### 1.1 What Phase A established

The owner's note to this unit (#1032 c.6649418760): "O-RET Phase A passed 49/49 frozen calibration
cases. That result validates the calibration implementation, not physical retention in native OI."

**The count is verified against the record.**
- `phaseA/run-1/phase-a/summary.json` has `tuples_frozen` 49, 49 entries in `tuples_evaluated`,
  `verdict` `PASS`, `exit` 0 and `first_failure` null. It was read, not regenerated.
- `phaseA/run-1/RESULT.md:42–43`: "`summary.json` has `verdict` PASS, `exit` 0, `first_failure` null,
  and 49 of 49 frozen tuples evaluated in the frozen order."
- `RESULT.md:49`: "The rows assigned were 2b ×14, 5 ×7, 1 ×6, 2a ×6, I-9 ×5, 6 ×4, 8 ×3, I-3 ×2, 3 ×1
  and 7 ×1." These sum to 49, and the per-tuple `row` fields of `summary.json` give the same tally.
- `phaseA/run-1/REVIEW.md:9–11`: "CONFIRMED PASS … an independent re-application of the frozen
  rule found 0 mismatches across 49/49 tuples."

**What the pass shows, in the record's own words.**
- PREREG §1 (P:41–43): "On these toy instances, under the conventions of §2, exact enumeration
  reproduces the hand derivations of DESIGN §3 and §6 and of §3 below, and the implemented §4
  precedence assigns the hand-assigned rows. This is a result on the consistency axis (§A.23)."
- Owner (RESULT.md:55–57): "The verified PASS establishes that the implementation agrees with its
  49 frozen calibration expectations. It does not establish physical retention in native OI
  dynamics or validate the classifier outside this test set."
- RESULT.md:59: "The agreement holds under the frozen conventions: `ε* = 1/20`, and conditioning on
  the declared preparation set `P`."

So Phase A shows that one implementation of the §4 classifier agrees with hand algebra on 49 toy
cases. The classifier itself (rows, precedence, DIL∃, J-1, the `G`-rule) is calibrated on those
cases and nowhere else.

### 1.2 What Phase A did not establish

- **Any retention mechanism, native or otherwise** (P:45). Every storage control imposes its law
  ("Every storage control imposes its preparation (quiet bits and ready registers)", P:696).
- **O1, O3, O4** (P:45–46): physical source of the preparation, accessible readback, observer
  formation.
- **Validity outside the control set.** P:666–668: "The controls are toy rules designed with known
  answers, and the expected values come from the same design. A pass shows that the implementation
  and the hand algebra agree. It does not show that the criteria separate storage from transport
  on cases outside the set."
- **Coverage** (RESULT.md:64–70; P:669–682): row 4 (I-8) is a declared constant; evidence rows I-1,
  I-2 and I-5 are not exercised; CX-4 is absent; row 3 is reached only through `ε_max > ε*`; no
  tuple has a J-1 failure in `H_{T′} ∖ H_T`; exit 4 is exercised only in the self-test.
- **Reproducibility.** `REPLAY.json`: "Not replayed … byte-for-byte reproduction outside that run
  has not been established." Python hash-seed independence is "Not established" (`REPLAY.json:105`;
  #1032 c.6629059049). The reviewer's re-check script is not retained (RESULT.md:51–53).
- **Decisions left open for Phase B.**
  - The decoder rule off the write-tick support (owner, #1032 c.6622434587: "a separate decision, to
    be made before Phase B"). PREREG §2.8 shows that those values decide rows: with the minimal
    tie-break, HC-SW becomes TR, and HC-TS becomes TR on `W₁` itself (P:212–215).
  - `w*` and `T*` (P:223, "unset and unused").
  - The nonlinear rule and its instance (D:559).
- **Conventions that decide verdicts** (P:689–692): the support conditioning `μ(·|σ∈P)`, the cell
  decomposition and the choice of `A` (I-5 not evaluated).
- **Known blind spots** (P:683–688): J-1 admits advection inside `A` and outflow; DIL∃ over-rejects
  through pooling (CX-4) and joint support (CX-4b); the siding of CX-7 is undecided.
- **The paper lemmas are not premises.** Lemmas S, S′, Q, C, L, H and P [R, DP] have no review
  record on `main` (programme `README.md:30–35`). Lemmas H and P sit on the verdict path of §6
  and need a review record before any freeze (G-13).

### 1.3 Paper observations that bear on Phase B [D]

All are hand derivations, unreviewed, stated in one direction only. None is an established result
or obstruction. Each is used in §6 as a control or a gate, never as a premise of a verdict.

**Setting common to all.** A copy-form bijection `φ(x, y) = (y, G(y) − x)` on cells with values in
a finite abelian group `𝐑`, where `G_i` depends on the current slice `y` only and not on `y_i`
(centre-free). K1 (`MR:464–465`), the SM:112 ring rule and rule h
(`../native-y-continuation-20261024/shared_v12/INTERFACE-CONTRACT.md:35–36`) have this form
(SM:106: "x_i(t+1) = f(neighbors of i at time t) − x_i(t−1)"). The carrier `Σ` is site 0, both
slices; `A` is a set of sites disjoint from `Σ`; the law at `t₀` is a product `μ_Σ ⊗ ν`; `P` is all
carrier values `σ = (x₀, y₀)(t₀)`.

**Lemma PAD (the register's own previous slice is a one-time pad at the write tick).**
- *Hypotheses.* Under `μ`, `x_A(t₀)` is uniform on `𝐑^A` and independent of
  `W := (y(t₀), x_{Λ∖A}(t₀))`. The carrier variable `κ` is a function of `W`.
- *Claim.* `y_A(t₀+1)` is uniform and independent of `W`, hence of `κ`: `TV_{t₀+1} = 0`, and every
  decoder has `ε_max(t₀+1) ≥ 1 − 1/m`, the blind bound of D-MET.
- *Proof.* Given `W`, `y_A(t₀+1) = G_A(y(t₀)) − x_A(t₀)` is a fixed translate of a uniform variable
  independent of `W`. ∎
- *Consequence.* Under `π₀`, nothing is written into a current-slice register of a copy-form rule,
  exactly or approximately, whatever the rule's nonlinearity.
- *Classification (§A.31).* CONFIRMING. It extends to every copy-form rule:
  - the CN control (#1032 c.6567189236);
  - the remark "K1's `y′_V = drive − x_V`, with `x_V` as the one-time pad" (R:314–315);
  - DESIGN-PULSE Observation K, (K-1) (D:151–155): "DIL∃ fails at the first hold tick unless the
    register's own content at `t₀` is restricted";
  - P2-G's necessary condition that every `y`-section `X_y` be proper (#914 c.6563955678 §2).

**Lemma NP (no pad at the carrier's site means re-supply).**
- *Claim.* If a tuple is written (`TV_{t₀+1}(σ, σ′) > 0` for some pair), then:
  - `y₀ ∈ Q := Par(R) ∖ R`;
  - J-i fails at the hold tick `t₀+1` unless `G₀(y(t₀))` is uniform under `ν`.
  - So the tuple is row 1 (RS) unless the current slices of site 0's neighbours pad it.
- *Proof.*
  1. The readout at `t₀+1` is a function of `(y(t₀), x_A(t₀))` and depends on `κ` only through
     `y₀(t₀)`. So a write needs `y₀` in the parent set of some read cell, and `y₀ ∉ R`, since
     `A ∩ Σ = ∅`.
  2. `y₀(t₀+1) = G₀(y(t₀)) − x₀(t₀)`, where `G₀` does not read `y₀`, and the law `L_G` of
     `G₀(y(t₀))` given `σ` does not depend on `σ` (product law).
  3. So `L(y₀(t₀+1) | σ)` is `L_G` translated by `−x₀`. It is the same for every `x₀ ∈ 𝐑` iff `L_G`
     is translation invariant, that is, uniform. ∎
- *Consequences.*
  - Under `δ₀` (`r = ∞`), and under `r = 2` at `N = 5` (which is `δ₀` there; §6.2), every written
    tuple is row 1 and every other tuple is row 3w.
  - For K1 at `N = 8` with `r = 2`, every written register contains site 1 or site 7 and none
    contains both. The other neighbour of site 0 is at distance 2 from `A`, so it is ready,
    `G₀ = y₇ + y₁` is constant, and the tuple is row 1 or 3w.
  - For SMR at `N = 8`, `r = 2` is not settled by NP in general.
- *Classification.* ELABORATING: it is the "carrier has left" clause of D-TRN (T-2) applied to the
  carrier's own site.

**Observation D2-T1 (the one-tick test under D2 is non-discriminating by construction).**
- Decoder D2 (§6.2) extends the write-tick decoder along the equivalence `~₁` generated by
  `ℓ ~ f_R(ℓ, q)` for `q ∈ supp Q_{t₀+1}`. That support is `𝒬_{W₁}`, the very input set DIL∃ uses on
  `W₁`.
- *Claim.* If `d2_status = consistent`, then DIL∃ holds on `W₁` and `τ = ∞` on `W₁`.
- *Proof.*
  - Every configuration in `supp R_{t₀+2}` is `f_R(ℓ, q)` with `ℓ ∈ supp R_{t₀+1}` and
    `q ∈ supp Q_{t₀+1}`. So every member of `𝓛_{W₁}` lies in the `~₁`-class of a write-supported
    configuration.
  - Consistent D2 makes `g∘ρ` constant on each such class. So no class holds two members of `𝓛_{W₁}`
    that decode differently, and no hit exists. ∎
- *Consequence.* Under D2, a one-tick window (`T = 1`) cannot produce TR or EX. The pulse criterion
  is vacuous there, and a `T = 1` pass is guaranteed by the decoder's construction. Such a pass is
  never evidence of storage (§6.4).

**Proposition IP′ (when a longer window is still guaranteed).**
- *Definitions.*
  - `~₁` is D2's relation, generated by `f_R(·, q)` for `q ∈ supp Q_{t₀+1}`.
  - `~_W` is the relation generated by `f_R(·, q)` for `q ∈ 𝒬_{W_T}`. Since `t₀+1 ∈ H_T`, every
    `~_W`-class is a union of `~₁`-classes.
  - `IP′ := every ~_W-class that meets 𝓛_{W_T} is a single ~₁-class`.
- *Claim.* If `d2_status = consistent` and `IP′` holds, then:
  - DIL∃ holds on `W_T`;
  - `τ = ∞`;
  - `ε_max(t) = ε_max(t₀+1)` for every `t ∈ W_T`.

  So the storage step is reached iff J-1, (R-a), (R-b) and `ε_max(t₀+1) ≤ ε*` hold, and the
  retention part of the verdict is guaranteed by the decoder.
- *Proof.*
  - By induction, `R_{t+1} = f_R(R_t, Q_t)` with `Q_t ∈ 𝒬_{W_T}`, so every supported `R_t` is
    `~_W`-equivalent to a write-supported configuration.
  - Under `IP′`, the `~_W`-class of a supported configuration is one `~₁`-class. So every supported
    `R_t` is `~₁`-equivalent to a write-supported configuration.
  - Consistent D2 makes `g∘ρ` constant on that class. So no `~_W`-class meeting `𝓛_{W_T}` decodes two
    ways, and no hit exists.
  - Constant `ε` follows from Lemma H's direction (D:110–115). ∎
- *Why the syntactic form was wrong.* The checkpoint-3 flag `IP := (𝒬_{W_T} ⊆ supp Q_{t₀+1})`
  compared input values. New input values that generate no new relation (for example, inputs that
  act as the identity, like an earlier one) leave `~_W = ~₁`. The pass is then still guaranteed
  while `IP` reads `false`. DT-S1q is such a case (second review, c.6650383732 §3).
- *Where a `T ≥ 2` test can fail under D2.* `IP′ = false` means that some `~_W`-class meeting
  `𝓛_{W_T}` merges two or more `~₁`-classes, through inputs D2 never read. Those classes carry D2's
  values independently, so DIL∃ on `W_T` and the observed window `W_{T′}` are not implied. They can
  fail with every declared assumption holding.
- *A concrete failing configuration (control DT-S13, §6.3).* `M_F` (route III's toy, E-reg) with
  `L = 3`, under its frozen S1 law (uniform on `{p₂ = 0}`), `P` the two fired preparations,
  `T = 2`:
  - At `t₀+1` the arriving cell is old cell 2, with `p = 0`. So `supp Q_{t₀+1} = {(0, 0), (0, 1)}`,
    `f_R(·; (0, v)) = id`, `~₁` is the identity relation, and D2 is consistent with `g = r`.
  - At `t₀+2` the arriving cell is old cell 1, `(p₁, v₁)`, uniform. With probability 1/2, `p₁ = 1`
    and the Fredkin gate swaps a uniform `v` into `r`.
  - The input `p = 1` merges the `~₁`-classes `{0}` and `{1}`, so `IP′ = false`.
  - `ε_max(t₀+3) = 1/4 > ε*` and `TV_{t₀+3} = 1/2`. `τ = 1`. J-1 holds at both hold ticks, because
    the arriving cells are independent of `(κ, r)`. `G*_{W₂} = {p = 0}` is consistent.
  - The row is 2b (EX). The design's laws, access and D2 all hold, and the tuple still fails.
- *A concrete passing configuration that could have failed (control DT-S2s, §6.3).* A two-bit
  variant of `M_F` in which the later input acts on an unread register bit, so the merged
  `~₁`-classes decode alike. The hand values are in §6.3. `IP′ = false`, and the row is 5.
- *A guaranteed pass (control DT-S1q, §6.3).* The later input `(0, 1)` acts as the identity, like
  `(0, 0)`. So `~_W = ~₁`, `IP′ = true`, and its row 5 never counts.

**Observation W1 (the Phase A classifier on a K1 wavefront).**
- *Instance.*
  - K1 at K-18(b): `ℤ/5`, `q = 2`, `a = 1`, background `δ₀`, register `A` = sites 1–4, two-slice locus.
  - The carrier's previous slice is restricted to 0 (`P = {(0,0), (0,1)}`), which is HC-K4's
    pattern (R:163–168).
  - Decoder `g = OR(y₁, …, y₄)`, which coincides on `𝓛_{W₂}` with D1′.
- *Values* (with `c = y₀(t₀)`):
  - `y(t₀+1) = (0, c, 0, 0, c)`, `y(t₀+2) = (c, 0, c, c, 0)`, `y(t₀+3) = (0, c, c, c, c)`.
  - With input `y₀ = 0`, the two-slice orbit is
    `(0000,1001) → (1001,0110) → (0110,0110) → (0110,1001) → (1001,0000) → (0000,1001)`, of period 5.
    It never meets the supported blank `(0000, 0000)`.
- *Rows under the Phase A classifier.*
  - `T = 1`: DIL∃ holds, `τ = ∞`, and SCH fails at `t₀+1` (`Par(y₂) ∩ C_{t₀+1} ∋ y₁`), so the row is
    6. The locality gate turns it into I-10 (§6.2, B-4).
  - `T = 2`: `y₀(t₀+2) = c`, so J-i fails and the row is 1.
  - Under D1 (`g(0110) = 0`) the row at `T = 1` is 2a (TR). D2 is undetermined (the orbit passes
    `(1001, 0000)`, whose read value is the blank's) and falls back to D1.
- *Classification.* ELABORATING, as the review corrected it: an instance of the Phase A classifier
  under D1′ and a restricted carrier. It is not a blind spot of the default Phase B configuration,
  which takes `P` as all carrier values. It is used as control NK-Wq.

**Proposition K1-NS (no K1 register of this family reaches storage).**
- *Provenance.* The first review's argument (#1115 c.6649925951, item 9c), re-derived here. It is
  restated, as the second review (#1115 c.6650383732 §2) showed, without the independence
  hypothesis of checkpoint 3: that hypothesis follows from KN-2 and J-1, and the bound needs
  neither.
- *Status.* The second review verified it on paper and by its own exact check (not retained, and not
  a Phase B result). No review record of it is on `main`. It is not an established obstruction and
  is not adopted (owner, #1032 c.6649977592). K1 stays in the planned tuples and controls (G-14).
- *Hypotheses.* They are named KN-1 to KN-4, so as not to clash with Main's A1–A6.
  - (KN-1) K1 over `𝔽₂` (`q = 2`), `a = 1`, on any finite graph. So `y′ = Adj y + B q − x` is linear,
    and `y₀` enters the register's update additively, with the fixed coefficient vector
    `b := B e_{y₀}`, the indicator of `A`'s neighbours of site 0.
  - (KN-2) `Σ` = site 0 (both slices); `A ∩ Σ = ∅`; `μ = μ_Σ ⊗ ν` for any `ν`; `P` = all four carrier
    values; `f = y₀(t₀)`.
  - (KN-3) Two-slice locus `R = (x_A, y_A)`, current-slice read, `Q = Par(R) ∖ R` = the current slice
    of `A`'s outside neighbours (B-1).
  - (KN-4) The decoder's values on the write-tick support depend on `c`. Otherwise the decoded value
    has the same law for `c = 0` and `c = 1`, so `ε_max(t₀+1) ≥ 1/2` and (R-c) fails.
- *Write structure.* `y_A(t₀+1) = c·b + n`, where `n = Adj_A y_A(t₀) + B_rest y_rest(t₀) − x_A(t₀)`.
  `n` and the x-part `n_x = y_A(t₀)` have a joint law independent of `σ` (KN-2). So
  write-supported configurations come in pairs, `(n_x, n)` with label 0 and `(n_x, n + b)` with
  label 1. By KN-4, `g∘ρ` differs on some such pair.
- *The join.*
  - The register update is `f_R((x, y); q) = (y, Adj_A y + B q − x)`.
  - For any `q` and `ℓ* := (Adj_A n_x + B q − n, n_x)`: `f_R(ℓ*; q) = (n_x, n)` and
    `f_R(ℓ*; q + e_{y₀}) = (n_x, n + b)`.
  - So any relation containing both `q` and `q + e_{y₀}` joins the two differently decoded members of
    the pair. This is the first review's `((q − c)b, 0)` construction, with general `n_x, n`.
- *The bound.*
  - Fix `c`, and let `σ₀ = (x₀ = 0, c)` and `σ₁ = (x₀ = 1, c)`. Both are in `P` (KN-2).
  - `y₀(t₀+1) = G₀(y_{≠0}(t₀)) − x₀`. The other components of `Q_{t₀+1}` are `G_j(y(t₀)) − x_j(t₀)` for
    `j ≠ 0`, which do not involve `x₀`. So `L(Q_{t₀+1} | σ₁)` is `L(Q_{t₀+1} | σ₀)` translated by
    `e_{y₀}`.
  - The supports of the two laws together contain pairs `{q, q + e_{y₀}}`. So exact DIL∃ fails on
    every `W_T`, by the join.
  - A `G` with `~_G` consistent contains no such pair. Then
    `μ(Q ∈ G | σ₀) + μ(Q ∈ G | σ₁) = Σ_q μ(Q = q | σ₀)[1_G(q) + 1_G(q + e_{y₀})] ≤ 1`, so
    `η_{t₀+1} = max_σ μ(Q_{t₀+1} ∉ G | σ) ≥ 1/2`.
  - The Lemma H bound is therefore `≥ 1/2 > ε*`.
- *Conclusion.*
  - Under KN-1 to KN-3, every K1 tuple either fails (R-c) at `t₀+1` (KN-4 false), or has exact DIL∃
    failing and no consistent `G` meeting the ST bound.
  - So no K1 tuple of the NRR-1 family reaches ST, for any `T ≥ 1` and under every decoder rule (D1,
    D1′, D2). Its row lies in {3w, 1, 2a, 2b, 3, 7, 8}. Under `π₀` it is row 3w (Lemma PAD).
  - J-1 is not needed for the conclusion. It only decides which non-storage row the tuple takes.
- *Two further consequences.*
  - **D2 is undetermined on every written K1 tuple satisfying KN-4.** `supp Q_{t₀+1}` contains a pair
    `{q, q + e_{y₀}}`, so the join lies inside `~₁` and merges two write-supported configurations
    that decode differently. Such tuples are decoded by D1's fallback, which reads no hold-tick data.
    The second review reports the same, by its own unretained check, for every written tuple of
    both rules on the stated instances (§4.4).
  - **K1-NS does not decide `G_status`.** A K1 tuple *may* reach PREREG §4 step 6 with
    `G_status_{W_T} = inconsistent` and exact DIL∃ failing, which under the frozen rule halts with
    exit 4. The second review reports that, on the instances it checked, every J-1-passing written
    K1 tuple has `G_status = empty`, which never halts. B-6 guards the halt case either way (G-15).
- *Limitations.*
  - `q = 2` only.
  - Laws that are not products are not covered.
  - Registers containing `Σ` are excluded by (R-a).
  - Rule h is not covered.
  - **SMR.**
    - The proof needs `y₀` to enter the register's update additively with a state-independent
      coefficient, and no switch of `A` to read `y₀`.
    - SMR registers that contain site `N−1` do not meet this: site `N−1` reads `y₀` through its
      switch. Nor do registers that contain site `N−2`, which reads `y₀` as its conditional target
      when `y_{N−1} = 0`. These are not covered.
    - *A claim to verify, not adopted.* The second review states, as its own unreviewed hand
      derivation, that K1-NS extends to SMR registers that contain site 1 and not site `N−1`
      (`y′₁ = y₀ + y_{R(1,y)} − x₁`, and no switch of `A` reads `y₀`). The writer's outline check of
      the join in that scope agrees, provided `A` also excludes site `N−2`. It is unreviewed and is
      not used by any control or verdict.

***

## 2. The candidate mechanism (b)

### 2.1 What the reviewed routes leave

From `ROUTES.md` [R] and DESIGN-PULSE [DP]:
- **Route I** (state-selected access) is blocked for exact retention under every law with
  φ-invariant support (Lemma S′), and undecided outside (R:233–240).
- **Route II** (a restricted prior on an existing rule):
  - on linear K1 at K-18(b): blocked under RET-st, undecided under D-RET (R:317–327);
  - on nonlinear copy-form rules: undecided, ceiling CONDITIONAL[H-sel, H-cur (declared)]
    (R:328–335).
  - The Comparison names it "Open native route with no added interaction" (R:462–463).
- **Route III** (`M_F`, `M_T`): CONDITIONAL on a new, unjustified F2 extension E-reg, designed for
  the purpose; "not a candidate while E-reg is unjustified (§A.29)" (R:421–426).
- **The resource every exact route needs** (annotation, #914 c.6612951653): a law whose support is
  not φ-invariant and excludes overwrites at the hold tick. It is unsourced (MR★ C-3).
- **Lemmas PAD and NP** (§1.3) add, for copy-form current-slice registers:
  - readiness of the register's own previous slice is needed for a write at all;
  - a free pad next to the carrier is needed for J-1 to pass.

So no route offers a sourced mechanism. The candidate with the least added structure that uses an
in-corpus step and adds no interaction is route II, with a register, a write, a law family and a
decoder all fixed in advance.

### 2.2 The candidate: NRR-1, native ready-register retention

**Definition.** NRR-1 is the following family of tuples, fixed before any evaluation.

| Element | Specification | Status |
|---|---|---|
| Dynamics | an in-corpus copy-form bijection `φ(x, y) = (y, G(y) − x)`: K1, or the SM:112 ring rule (§2.3) | K1: the native step form (posit (vii)) on a 1-D toy graph. SM:112 ring: in-corpus construction; as physics, F2 extension E-SDC |
| Carrier | `Σ` = one site, both slices, at `t₀`; `μ_Σ` uniform; `P` = all carrier values; `f(σ) = y_Σ(t₀)` | declared preparation |
| Register | a fixed set `A` of sites disjoint from `Σ`; locus `R` = both slices of `A`; read cells = the current slice of `A` | declared (H-cur), as in D-ACC |
| Write | the step `t₀ → t₀+1`. No gate is added. | as the dynamics row |
| Hold | the same step at every hold tick | as the dynamics row |
| Law | `μ = μ_Σ ⊗ ν_r`, with `ν_r` from the ready-region family of §6.2 (`r = −1` is `π₀`) | `π₀`: conditional on H-μ. `r ≥ 0`: imposed, H-sel |
| Decoder | fixed at the write tick by the rule chosen at G-4; never by later outcomes | imposed rule |
| Criteria | the Phase A classifier with amendments B-1 to B-6 (§6.2) | imposed rule, calibrated by controls |

**Why it is proposed as the smallest native candidate (argued from added structure, not proved
minimal).** D-SML does not use a scalar minimum: "use a resource comparison rather than one scalar
minimum" (DEFINITIONS:215–218, owner OQ-8).
- It adds no interaction to the step (route III adds E-reg).
- It adds no access mechanism beyond the declared baseline H-cur (route I would need one).
- It places all imposed structure in the starting law, in one parameter: the radius `r` of the
  ready region around `A`. The ledger `D(ν_r)` is the number of constrained bits, and the
  probability that `π₀` produces the ready region spontaneously is `2^{−D(ν_r)}`. That is OQ-8's
  preparation column, and the write probability of the same event (§6.6).
- It adopts DESIGN-PULSE's §8 Phase B target (D:576–582): K1 at K-18(b) with every nonempty
  `A ⊆` sites 1–4 and the laws `π₀`, `δ₀` and `δ_b`; a nonlinear copy-form rule at `|S| ≤ 2¹⁶`;
  `T = 1, 2`. It refines it with the locus, the law family and `T = 3`.

**What NRR-1 is not.**
- Not a SOURCE-CANDIDATE: `ν_r` for `r ≥ 0` is imposed, and access is declared.
- Not selected: K1 and the SM:112 ring rule are evaluated under one preregistered rule, and neither
  is preferred in advance (#1032: "tested without choosing the winner post hoc").
- Not a claim that native retention exists. It is the object Phase B would test.

### 2.3 OI-native parts and F2 extensions

- **K1** (`φ(x, y) = (y, Ay − x)`, `(Ay)_i = Σ_{j∼i} y_j`, `a = 1`, `ℤ/q`).
  - Its step form is posit (vii), "linearity of the substratum update (A5)" (Main:726). That this
    is the physics is a posit (MR★ C-1, MR:1309–1320).
  - The native coupling graph is the simple-cubic graph, posit (x) (Main:726; MR:467–468). The rings
    used here are 1-D toy graphs, so a K1 tuple tests the native step form on a toy graph, not native
    `d = 3` dynamics.
  - If Lemma L [R] and S-C1 [MR] hold as stated, the transfer to any region on K1 does not depend on
    any other region's state, so a prior can supply offsets but cannot gate the write. Lemma L has no
    review record on `main`. S-C1 is in the frozen MR-1 record.
- **The SM:112 ring rule.**
  - The rule: `x_i(t+1) = x_{i−1}(t) + x_{R(i,x(t))}(t) − x_i(t−1)` mod `q`, with `R(i, x) = i+2` if
    `x_{i+1} = 0` and `i+1` otherwise (SM:112).
  - It is an in-corpus construction meeting SM §3.1's constraints (i)–(iii). SM §3.1 states
    state-dependent geometry as a principle (SM:104). The transfer to site `i` depends on the value
    at `i+1`, which is what K1 lacks.
  - It is nonlinear, so taking it as the physical update departs from posit (vii).
  - **F2 extension E-SDC (unadopted):** "the step has SM §3.1-type state-dependent coupling,
    realized by the SM:112 ring rule's switching rule".
    - The principle itself is SM:104's. What E-SDC adds is this particular switching rule as the
      physics.
    - No independent consequence of the switching rule is identified, and the rule is not
      constrained by anything beyond (i)–(iii). So E-SDC fails §A.29's hard-to-vary test as it
      stands.
    - The O-OBSMU record states the same idea as proposal P-SDC (branch `research/o-obsmu-20261104`
      at `f67b9f0c`, `ANALYSIS.md` §4.4, provenance only).
  - **Departure from `ROUTES.md`.** R:462 calls route II on "a nonlinear copy-form rule already in
    the corpus" the "Open native route with no added interaction". The rule adds no interaction to
    the copy form, but it is not the update that posit (vii) fixes. This design therefore labels it
    E-SDC when it is read as physics, and a positive under it is CONDITIONAL[E-SDC].
- **Rule h.** `U_{t+1}(v) = U_{t−1}(v) ⊕ h(⊕_{w∼v} U_t(w))`, `h(A,B,D) = (B, D, A ⊕ BD)` on `𝔽₂³` per
  site, six neighbours (`INTERFACE-CONTRACT.md:35–36`). It is also outside posit (vii). Its smallest
  torus has `|S| ≥ 2⁴⁸`, beyond exhaustive enumeration; it is not in the instance set (G-1).
- **Not native, and not used in NRR-1 tuples:** E-reg (`M_F`, `M_T`), any clock register, any
  adaptive or moving readout, any decoder chosen after the write tick. E-reg models appear only as
  calibration controls (DT-S13, DT-S2s, DT-S1q).

***

## 3. Discrimination (c)

Each failure mode has an operational criterion, evaluated by the classifier on structured fields,
and at least one countercontrol whose expected row is fixed in advance. The criteria are Phase A's
(DESIGN-PULSE §2.3–§4; PREREG §4) unless marked as a Phase B amendment.

### 3.1 Travelling pulse

**Criterion TP.** A tuple counts as storage only if all of the following hold:
- DIL∃ on `W_T` exactly, or DIL∃-η with the Lemma H bound `≤ ε*` on `W_T` (ST, D:170–173);
- no observed `ε_max > ε*` on the gap-free extension window `W_{T′}`, `T′ = max(T, τ)`. Otherwise
  the case is TR (no consistent `G`) or EX (some consistent `G`) (P:468–469);
- for copy-form rules, DIL∃ on the two-slice locus (B-1), so the register's own previous slice is
  part of `R` and not a quiet input;
- the locality gate LOC (B-4);
- `T ≥ T*` (B-5);
- under D2, the retention part is not implied by the decoder: `IP′ = false` (§1.3, §6.4). Some
  class of the window's relation that meets `𝓛_{W_T}` must merge two or more `~₁`-classes.

**Why each part is needed.**
- DIL∃ is the only Phase A criterion that separates HC-TS from HC-SW on `W₁` (D:507–525, L1).
- The observed failure prevents DIL∃'s over-rejections (CX-4, CX-4b) from being read as transport
  (P:125).
- Observation D2-T1: under D2 the one-tick test cannot fail, so `T = 1` is non-discriminating by
  construction.
- Proposition IP′: under D2, a longer window is also guaranteed when the later hold ticks merge no
  `~₁`-classes that meet `𝓛_{W_T}`. When `IP′ = false`, the classes merged by inputs D2 never read
  carry D2's values independently, so DIL∃ on `W_T` and the observed window can fail. When
  `IP′ = true`, they cannot fail through the decoder.
- DT-S13 is a concrete case in which the `T = 2` test fails under D2, with every declared assumption
  holding. DT-S2s is a case in which it could fail and passes. DT-S1q is a guaranteed pass
  (`IP′ = true`) that does not count.

**Countercontrols.**
- HC-TS and HC-TM [PA] (expected TR, P:341–346) and MB [PA] (TR). They are cited; their roles are
  carried by NK-Wq and DT-S13.
- NK-W and NK-Wq (native step form on K1).
- DT-S13 (fails at `T = 2` under D2, `IP′ = false`), DT-S2s (passes at `T = 2`, `IP′ = false`) and
  DT-S1q (guaranteed pass, `IP′ = true`, does not count).

### 3.2 Recurrence

**Criterion RC.**
- Every window is gap-free: `ε_max` and J-1 are evaluated at every tick of `W_{T′}`.
- A readback success at a tick after an observed failure is flagged and never supports rows 5 or 6
  (the recurrence rule, P:456–463).
- Phase B adds a reported field `n_supp`, the period of `φ` on the support of `μ`. By Lemma P [DP]
  (D:141–145), exact retention over `W_T` needs `T ≤ n_supp − 2`. A storage row with
  `T′ ≥ n_supp − 1` is impossible if the implementation and Lemma P are right, and it halts the run
  (exit 6, §6.10).

**Countercontrols.** HC-R1 and HC-R3 [PA]: a single late readback passes, while the gap-free
window gives RS (P:354, :359). They are cited, not re-run; their role in Phase B is carried by the
recurrence-flag field and the exit-6 check.

### 3.3 Continual re-supply

**Criterion RS.**
- J-1 with `B_t := Q = Par(R) ∖ R`, computed from `φ` on all of `S` (P:81–86), at every hold tick of
  `H_{T′}`: (J-i) `Q_t ⫫ κ` jointly, and (J-ii) `κ ⫫ Q_t | R_t`. A failure is row 1 and takes
  precedence over every storage row.
- With the two-slice locus (B-1), `Q` is the current slice of `A`'s outside neighbours, including
  the state-dependent neighbours of the SM:112 rule. For a written register, `Q` contains the
  carrier's current slice (Lemma NP), so J-1 tests D-TRN (T-2)'s requirement that the hold ticks
  come after "the incoming carrier has left".
- J-1 is an inflow screen only (P:164–166). Advection inside `A` and outflow are left to TP.

**Countercontrols.**
- HC-R2 and SC [PA] (RS; SC through J-ii alone, the joint-information case the owner asked for).
- NK-W: on K1 under `δ₀`, J-i fails at `t₀+1`, because `y₀(t₀+1) = x₀`.
- NK-K3: HC-K3, countercontrol (g). Its planted-marker decoder holds `y₀` while J-i fails at `t₀+1`.
- C-NP-ALL: Lemma NP checked on every tuple whose law makes `G₀(y(t₀))` non-uniform (§6.3).

### 3.4 What the criteria cannot separate, and where the test is weak

- **The one-tick test under D2.** It is non-discriminating by construction (D2-T1). The same holds
  for any window whose later hold ticks merge no `~₁`-classes that meet `𝓛_{W_T}` (Proposition IP′).
  Such tuples are reported and never counted.
- **On the NRR-1 family, D2 is undetermined on every written tuple that is not blind** (§4.4). So
  the decoder that classifies NRR-1 tuples is D1's fallback, and the circulation D2 is meant to keep
  testable is exercised only by the controls.
- **Near-global ready regions.** At `N = 5`, `r = 2` is `δ₀` for every register. At `N = 8`, `r = 2`
  constrains four to seven of the seven non-carrier sites (`Z₂({1}) = {1, 2, 3, 7}`).
  - By Lemma NP, every written tuple at `r = ∞`, at `r = 2` with `N = 5`, and at `r = 2` with K1 and
    `N = 8` is RS. So these law values test re-supply only.
  - They are excluded from robustness (§6.4).
- **Robustness is unreachable under the current family.** No matched pattern can count, for either
  rule (§6.4, reachability note). Under the present definitions, STORAGE-ROBUST cannot pass. Its
  repair is the owner's (G-9).
- **A dwell in a closed locus** (CX-7, the siding). Storage here means "a dwell at a closed locus
  covering `W_T`" (D:489–490). Phase B inherits that reading.
- **Information carried jointly by `Q` and cells beyond it.** J-1 tests `Q` only. Uniform cells
  outside the ready region can pad the carrier's influence so that `Q` looks independent of it. The
  case is then decided by DIL∃ and the observed window, not by J-1.
- **Coordinates.** Every verdict is relative to the cell decomposition and to `A` (CX-3, I-5). The
  robustness criterion (§6.4) varies `N` and `T`, not the coordinates.
- **Finite rings.** On `ℤ` the K1 wake fills the light cone (MR★ C-2). On a ring of 5 or 8 sites the
  cone wraps within a few ticks, so a ring result does not settle the infinite-line or `d = 3`
  question.

***

## 4. Assumptions (d)

Label key: **S** physically sourced (locator given); **C[h]** conditional on the named hypothesis
`h`; **I** imposed.

### 4.1 Starting law

| Assumption | Label | Locator or reason |
|---|---|---|
| Finite `S` | C[posit (ii)] | Main:726 item (ii) |
| One time-homogeneous bijection | S, given the update | SM:106: bijectivity "is automatic for any second-order reversible dynamics" |
| Product form `μ = μ_Σ ⊗ ν` (carrier independent of background) | I | requirement 3 of #1032; DEFINITIONS preamble |
| `μ_Σ` uniform, `P` = all carrier values | I | a declared preparation; requirement 2 asks for "at least two independently available incoming carrier preparations" and gives no source for them |
| `ν_{−1} = π₀` | C[H-μ] | Main:56: "a selection principle, not uniqueness from invariance alone"; #914 c.6563412926 §0 code H-μ |
| `ν_r`, `r ≥ 0` (ready register and collar) | I, C[H-sel] | MR★ C-3: no physically sourced quiet, ready region in the sources read (as scoped by C.1-1) |
| `δ_b` (NK-K3 only) | I | HC-K3's planted marker; a countercontrol, never a candidate law |

### 4.2 Write

| Assumption | Label | Locator or reason |
|---|---|---|
| K1 as the update | C[posit (vii)], on a 1-D toy graph rather than the simple-cubic graph of posit (x) | Main:726 items (vii), (x); SM:296; MR★ C-1 |
| The SM:112 ring rule as the update | C[E-SDC], an unadopted F2 extension | SM:104 (principle), SM:112 (construction); §2.3 |
| Write tick `t₀ → t₀+1`, preparation at `t₀` | I | declared timing (DEFINITIONS preamble) |
| The carrier's value enters only through the step | S under the update's label | no gate is added |
| `f = y_Σ(t₀)` | I, forced by the form | a copy-form step can imprint only the carrier's current slice on a disjoint register at `t₀+1`, since `y_A(t₀+1) = G_A(y(t₀)) − x_A(t₀)` [D] |

### 4.3 Readback

| Assumption | Label | Locator or reason |
|---|---|---|
| H-cur (declared): the current slice of `A` is readable | C[H-cur] | #914 c.6566997020 K-8 ("H-cur is declared, not native"); D-ACC (#1032 c.6611966162, OQ-3). Physical sourcing of access outstanding |
| Identity of `A` across ticks (a fixed declared region) | I | Main:88 ("the partition is fixed"); requirement 1 says identity across time "does not count" as a derived register |
| Two-slice locus `R` with current-slice read | I (amendment B-1) | the register's previous slice is physically part of its sites' state (SM:106); it is not read |
| Reading across ticks | evaluated by the analyst, not an embedded read | D-SEN: a path-law comparison "must not silently supply physical access across time" (#1032 c.6611966162) |
| No clock register | I | row 4 stays a declared constant (§6.2) |

### 4.4 Decoder

| Assumption | Label | Locator or reason |
|---|---|---|
| A deterministic decoder of the read cells, fixed at the write tick | I | Q8 (#1032 c.6621961326): "**Frozen at the write tick.** A deterministic decoder minimizing worst-case write-time error over the two preparations, with a fixed lexicographic tie-break. Never optimized using later retention outcomes." |
| The lexicographic tie-break, exactly (D1) | I | §6.2. It applies on and off the write-tick support. Off the support it gives the least value, as #1032 c.6622434587 reads it ("It sets the decoder's values on configurations that are unsupported at the write tick") |
| Values off the write-tick support by the rule chosen at G-4 | I | #1032 c.6622434587 leaves this rule to be decided before Phase B |
| `ε* = 1/20` | I | owner, #1032 c.6612956983: "a preregistered engineering criterion, not a derived physical constant" |

**D2 and Q8.**
- D2 reads no `ε` and no tick after `t₀+1`, so it is not "optimized using later retention outcomes".
- But it reads `supp Q_{t₀+1}`, the input support of the first hold tick, which is exactly the
  data DIL∃ uses on `W₁`. A consistent D2 therefore guarantees DIL∃ and `τ = ∞` on `W₁`
  (Observation D2-T1).
- This goes beyond the reading of c.6622434587, under which the off-support rule fixes values but
  does not decide rows by construction. It is the reason for `T* ≥ 2` and for the `IP′ = false`
  counting condition (§6.4). It is put to the owner at G-4 and G-5.
- **On this family D2 decides no written tuple.**
  - `P` contains both values of `x₀`. So `supp Q_{t₀+1}` contains pairs `{q, q + e_{y₀}}` (Proposition
    K1-NS, the bound).
  - Wherever `y₀` enters the register's update additively, the join then merges, inside `~₁`, two
    write-supported configurations that decode differently. So D2 is `undetermined`. This is shown
    on paper for K1 (every written tuple satisfying KN-4).
  - The second review (#1115 c.6650383732 §2) reports, by its own unretained check (not a Phase B
    result), zero D2-consistent written tuples for both rules at both `N`.
  - Consequence: under G-4 (a), every written NRR-1 tuple is decoded by D1's fallback, with
    `IP′ := false`. G-4 (a) then coincides with G-4 (c) on this family. The choice between them
    matters only for the controls and for any later family.

***

## 5. Sourced versus imposed under NRR-1 (e)

The five requirements of #1032's "Precisely missing" list.

| # | Requirement | Status under NRR-1 | Why |
|---|---|---|---|
| 1 | Physical rule, not access by declaration | **Imposed.** The dynamics is the native step form on a toy graph (K1) or conditional (E-SDC). The register, its identity and its readable σ-algebra are declared. | H-cur is the declared baseline; requirement 1 is not met by it (D-ACC). No state-selected or derived register is tested. |
| 2 | Nontrivial transfer | **Tested, not sourced.** The write is the step; carrier sensitivity is NB-1 at `t₀+1` (the write gate, B-2); simple advection is rejected by TP and re-supply by RS. | The outcome depends on the computation. A positive shows transfer for the declared register and law only. |
| 3 | Availability and independence | **Imposed** for `r ≥ 0` (H-sel); **conditional** on H-μ for `π₀`. The full joint prior is stated: `μ_Σ ⊗ ν_r`. | Under `π₀`, Lemma PAD predicts no write. No source for `ν_r` exists in the sources read (MR★ C-3, C.1-1). The ready state is never inferred from the record. |
| 4 | Retention | **Tested** over gap-free windows `T ∈ {1, 2, 3}`, with `ε* = 1/20`, the `W_{T′}` extension, the recurrence rule and Lemma P's bound. A tuple counts only at `T ≥ T*` with a test that could fail. Persistence, renewal and reusable supply are **not addressed**. | One-step retention is reported; counting uses at least two hold ticks; multi-tick persistence beyond `T = 3` is not tested. |
| 5 | No circularity | **Not circular as stated, and not met.** No observer, instrument, noncommutative algebra or Born rule is assumed. The ready region is assumed, labelled, and never claimed to arise from the record. | A ready reservoir that generates itself is excluded by construction; one that is supplied is the open premise. |

***

## 6. The proposed Phase B test (f)

### 6.1 Objective and non-objectives

**Objective.** For the NRR-1 family on two in-corpus copy-form rules, decide by exhaustive exact
enumeration which tuples, if any, the Phase A classifier (amended by B-1 to B-6 and calibrated by
the controls of §6.3) assigns a storage row whose retention part is not guaranteed by the decoder,
and report the preparation resource each one needs.

**Non-objectives.** Sourcing any law (O1); access (O3); observers (O4); rule h; `d = 3`; clocks;
moving or adaptive registers; a D-SML ranking while `w*` is unset; any premise adoption,
SOURCE-CANDIDATE promotion, merge or publication; any change to Phase A's frozen files or rows.

### 6.2 Fixed instances and parameters

**Rules.**
- `K1`: `φ(x, y) = (y, Ay − x)`, `(Ay)_i = y_{i−1} + y_{i+1}`, over `𝔽₂`, on `ℤ/N`.
- `SMR`: `y′_i = y_{i−1} + y_{R(i,y)} − x_i`, `R(i, y) = i+2` if `y_{i+1} = 0` and `i+1` otherwise,
  over `𝔽₂`, on `ℤ/N`.
- Ring sizes `N ∈ {5, 8}`, so `|S| = 2¹⁰` and `2¹⁶`. `N = 5` with K1 is K-18(b).
- Injectivity of `φ` on `S` is checked for every instance before any tuple (exit 5).

**Carrier.** `Σ` = site 0, both slices. `μ_Σ` uniform on `𝔽₂²`. `P` = all four values. `f = y₀(t₀)`,
so `m = 2` and the blind bound is `1/2 > ε*`.

**Registers.**
- `N = 5`: all 15 nonempty `A ⊆ {1, 2, 3, 4}`.
- `N = 8`: all arcs `{a, …, a+w−1} ⊆ {1, …, 7}` with `w ∈ {1, 2, 3}`, which is 18 registers.

**Ready regions (`r`).** For `r ∈ {−1, 0, 1, 2, ∞}`:
- `ν_{−1} = π₀` on the non-carrier cells;
- for `0 ≤ r < ∞`, `ν_r` is uniform on the non-carrier cells conditioned on: both slices of every
  site at ring distance `≤ r` from `A`, other than site 0, are 0. The constrained site set is
  `Z_r(A) := {i ≠ 0 : dist(i, A) ≤ r}`; `Z_0(A) = A`.
- `ν_∞ = δ₀` on all non-carrier cells.
- Laws with the same constrained set are evaluated once and listed under every `r` that gives them.
  At `N = 5`, `r = 2` gives `Z = {1, 2, 3, 4}` for every `A`, so it equals `ν_∞`.
- `D(ν_r) = 2 |Z_r(A)|` bits.
- One additional law, `δ_b` of HC-K3, is used only in control NK-K3.

**Signed-offset patterns (used by robustness, §6.4).**
- Write each site as its signed offset from site 0 in `(−N/2, N/2]`.
- The pattern of a tuple is the smallest interval `I` of offsets containing `0`, `A` and `Z_r(A)`,
  with each offset labelled carrier, register, ready or free.
- The tuple is *local* iff `|I| ≤ N − 2`. Then `I` is flanked on both sides by at least one free
  site and does not wrap.
- At `N = 5`, the local patterns with `r ∈ {0, 1}` are nine:
  - `A = {1}` with `r = 0` or `r = 1`; `A = {2}` with `r = 0`; `A = {1, 2}` with `r = 0`;
  - their mirror images (sites 4, 3 and {3, 4});
  - `A = {1, 4}` with `r = 0` (pattern register, carrier, register).

  Every other `N = 5` tuple, and every tuple with `r = 2` or `r = ∞`, is non-local at `N = 5`.
- Two tuples at `N = 5` and `N = 8` are *matched* iff both are local and their labelled patterns are
  equal.
  - Eight of the nine local `N = 5` patterns have exactly one matched `N = 8` tuple: the arcs {1},
    {2}, {1, 2}, {7}, {6}, {6, 7} at the same `r`.
  - `A = {1, 4}` has none, because {1, 7} is not an arc of the `N = 8` family. So it cannot be part
    of a robust verdict.
- For K1, mirror patterns are equivalent by reflection. SMR is chiral, so they are not.

**Windows.** `T ∈ {1, 2, 3}`, window mode only (the extension `W_{T′}` is always computed).

**Decoders.** Read configurations are listed in increasing order of their integer encoding, with
the read cells in the frozen cell order and the first read cell as the most significant bit. A
decoder is the tuple of its values in that order, and values are ordered `0 < 1`.
- *D1* (Q8 exactly): among all decoders that minimize the worst-case write-tick error
  `max_{σ∈P} μ(g(ρ(R_{t₀+1})) ≠ f(σ) | σ)`, the lexicographically least. This fixes the values on
  the write-tick support by the tie-break, and gives the least value, 0, everywhere off it.
- *D1′*: D1's values on the write-tick support, and 1 off it. It is a sensitivity variant, not Q8.
- *D2*: D1's values on the write-tick support.
  - Let `~₁` be the equivalence on `config(R)` generated by `ℓ ~ f_R(ℓ, q)` for
    `q ∈ supp Q_{t₀+1}`. Give each read configuration in the `~₁`-class of a write-supported `ℓ` the
    value `g(ρ(ℓ))`.
  - If two values would be assigned to one read configuration, D2 is `undetermined` for the tuple,
    and D1's values are used off the support.
  - The remaining read configurations take D1's value.
- The rule used to classify each NRR-1 tuple is the one chosen at G-4. The rows under the other two
  are recorded as sensitivity (`row_D1`, `row_D1p`, `row_D2`), and a tuple whose rows differ
  carries `decoder_sensitive = true`.

**Amendments to the Phase A decision rule.** These apply to Phase B tuples only. Phase A's frozen
files, rows and decision rule are unchanged.
- **B-1, locus.** For copy-form rules, `R` = both slices of `A`, the read cells = the current slice
  of `A`, and `Q = Par(R) ∖ R` from `φ` on all of `S`. SCH ranges over the read cells.
- **B-2, write gate.** Before PREREG §4 step 2, the tuple takes row **3w (no write)** if
  `TV_{t₀+1}(σ, σ′) = 0` for every pair in `P`. Rows 2a and 2b presuppose a record; without the gate
  a blind register with a failing DIL∃ would be labelled TR or EX.
- **B-3, decoder.** The rule chosen at G-4, for every NRR-1 tuple. Controls keep the decoders their
  definitions fix.
- **B-4, locality.** At PREREG §4 step 6, a storage row (5 or 6) whose environment
  `E := Λ ∖ (Σ ∪ sites(R) ∪ sites(Q))` is empty becomes row **I-10 (global register: not a local
  record)**. For the toy controls, `E` is counted in cells. The code I-10 continues the evidence
  rows I-1 to I-9 and is distinct from the qualifier I-5.
- **B-5, `T*` and `w*` stay outside the per-tuple rule.** As in PREREG §2.10, the ST clause
  "`w ≥ w*` and `T ≥ T*`" (D:170–171) and row 8's second clause (D:411) stay inactive in the
  per-tuple rule. `T*` is applied only in the per-rule counting rule (§6.4). So a storage row at
  `T = 1` stays row 5 or 6 (or I-10); it is not turned into row 8, and it does not count.
- **B-6, an undetermined `G` at the storage step (G-15).** Where PREREG §4 step 6 would halt with
  exit 4 (`G_status_{W_T} = inconsistent` and exact DIL∃ failing), the tuple is recorded with
  `G_undetermined = true`, ST is not certified, and evaluation continues at step 7. It is a guard:
  K1 tuples *may* reach that step, since K1-NS shows exact DIL∃ failing but does not decide
  `G_status`. On the instances the second review checked, the J-1-passing written K1 tuples have
  `G_status = empty`, which never halts.
- Unchanged:
  - `ε* = 1/20`;
  - independence and support conditioning under `μ(·|σ∈P)`, which is `μ` itself when `P` is all
    values;
  - J-1 in the Q7-narrowed wording (P:159–166);
  - the `G`-rule (P:440–452);
  - `W_T` for storage and `W_{T′}` for TR/EX;
  - the recurrence rule;
  - row 4 as the declared constant `false`.

**Phase A rows are unchanged, and coverage still holds [D, by inspection of the frozen tables].**
- B-2: every Phase A tuple has `TV_{t₀+1} ∈ {1, 9/10}` (P:341–365, :383).
- B-4: every Phase A storage tuple (S1, R3 at `T = 1`, HC-SW, MC, HC-SK at `k ≥ 5`) has a nonempty
  environment in cells. For example, MC(3) has `u₄, u₅` outside `Σ ∪ R ∪ Q`.
- B-1 and B-3 do not apply to Phase A models: none is copy-form, and their decoders are part of
  their definitions.
- B-5 restates PREREG §2.10, under which Phase A ran.
- B-6 changes no Phase A row: no frozen tuple reached exit 4 (RESULT.md:68).
- **This is an inspection, not a measured invariant.** The second review confirmed it. Whether a run
  also measures it depends on G-10: only G-10 (b), a named regression test, gives it a §A.41
  checkpoint. Under G-10 (c) no checkpoint exists, and the statement stays a reviewed inspection.
  It is not asserted as a run invariant (§6.9).
- **Coverage** (D:391–399).
  - The write gate is a new first-match step; when it does not match, PREREG's steps follow unchanged.
  - B-4 maps a storage outcome to one row.
  - B-5 changes no step.
  - B-6 replaces a halt by continuing to steps 7–8, where the existing argument already assigns
    exactly one row to every case in which ST fails.
  - So every tuple still takes exactly one row.

**Tuple count.** Per rule, at most `15 × 5 × 3 = 225` tuples at `N = 5` and `18 × 5 × 3 = 270` at
`N = 8`, before laws are deduplicated. At most 990 NRR-1 tuples, plus the controls of §6.3.

### 6.3 Controls

All controls run first, in a fixed order, and the run halts at the first mismatch (exit 1). Their
expected values are hand derivations [D] that the reviewer re-derives. No mechanism verdict is
rendered unless every control is green.

| Id | Instance | Decoder | Expected (compared fields) | Tests |
|---|---|---|---|---|
| C-INJ | every rule instance | — | `φ` injective on `S` | the rules as specified (exit 5) |
| C-PAD-K1 | K1, `N = 5`, `π₀`, `A = {1}`, `T = 1` | D1 = identity on `y₁` (`{0:0, 1:1}`, the lexicographically least of the two worst-case minimizers, identity and negation) | `ε_max(t₀+1) = 1/2`; `TV_{t₀+1} = 0` for all pairs; row 3w; `Q_cells = {y₀, y₂}` | Lemma PAD; B-2; B-1's `Q` |
| C-PAD-SMR | SMR, `N = 5`, `π₀`, `A = {1}`, `T = 1` | D1 = identity on `y₁`, as above | `ε_max(t₀+1) = 1/2`; `TV_{t₀+1} = 0`; row 3w; `Q_cells = {y₀, y₂, y₃}` | Lemma PAD on the nonlinear rule; state-dependent `Par` |
| C-PAD-ALL | every NRR-1 tuple with `r = −1` | as classified | `TV_{t₀+1} = 0` for all pairs, and row 3w | Lemma PAD over all such tuples |
| C-NP-ALL | every NRR-1 tuple whose law makes `G₀(y(t₀))` non-uniform (computed field `G0_uniform = false`). This includes every law equal to `δ₀` on the non-carrier cells under any label (for example `N = 5`, `r = 1`, `A = {2, 3}`), every `N = 5` tuple with `r = 2`, and every K1 `N = 8` tuple with `r = 2` | as classified | row 1 if written, row 3w otherwise | Lemma NP over all such tuples |
| NK-W | K1, `N = 5`, `δ₀`, `P` all values, `A = {1,2,3,4}`, `T = 1` and `T = 2` | D1 (any write-tick minimizer gives the same rows) | `Q_cells = {y₀}`; J-i fails at `t₀+1`; row 1 at both `T`; `ε_max(t₀+1) = 0`; `TV_{t₀+1}(σ, σ′) = 1` if `y₀ ≠ y₀′` and 0 otherwise | RS on the native step form; the carrier's previous-slice channel (`y₀(t₀+1) = x₀`) |
| NK-Wq | K1, `N = 5`, `δ₀`, `P = {(0,0), (0,1)}`, `A = {1,2,3,4}`, `T = 1` and `T = 2` | fixed by the control: `OR(y₁, …, y₄)` | `T = 1`: DIL∃ holds, `τ = ∞`, SCH fails at `t₀+1`, `row_pre_loc` 6, row I-10, `ε = 0, 0`. `T = 2`: J-i fails at `t₀+2`, row 1, `ε = 0, 0, 0` | B-4; Observation W1 |
| NK-K3 | K1, `N = 5`, `δ_b`, `P` all values, `A = {1,2,3,4}`, `T = 1` | fixed by the control: `g(u) = u₁` if `u₂ ≠ u₃`, else `u₂`, with `u = (y₁, y₂, y₃, y₄)` (R:158) | `ε_max = 0, 0`; J-i fails at `t₀+1`; row 1 | countercontrol (g) (R:154–161, :325–326) |
| DT-S13 | `M_F`, `L = 3`, law uniform on `{p₂ = 0}`, `P` the two fired preparations, `T = 2` | D2 (consistent; `g = r`) | `IP′ = false` (`p = 1` merges the `~₁`-classes `{0}`, `{1}`); `ε = 0, 0, 1/4`; `TV = 1, 1, 1/2`; `τ = 1`; J-1 holds at both hold ticks; `G*_{W₂} = {p = 0}`, consistent; row 2b | a `T = 2` test that fails under D2 with every declared assumption holding |
| DT-S2s | `M_F` with two presence bits per channel cell `(p, p′, v)` and register `(r, s)`, read cell `r`. Each tick: if `p = 1`, swap `v ↔ r`; otherwise, if `p′ = 1`, swap `v ↔ s`; then shift. `L = 3`; law uniform on `{p₂ = p′₂ = 0, p₁ = 0}`; `P = {(1,0,0), (1,0,1)}`, `f = v₀`; `T = 2` | D2 (consistent; `g = r`) | `IP′ = false` (`(0,1,v)` at `t₀+2` merges the `~₁`-singletons `(c,0)` and `(c,1)`); DIL∃ holds on `W₂`; `τ = ∞`; `T′ = 2`; `ε = 0, 0, 0`; `TV = 1, 1, 1`; J-1 holds at both hold ticks; SCH holds; `E` = channel cells 1, 2; `D = 3`; row 5; `counts = true` | a `T = 2` pass that could have failed: the positive path for a counting row |
| DT-S1q | `M_F`, `L = 3`, law uniform on `{p₂ = 0, v₂ = 0, p₁ = 0}`, `P` the two fired preparations, `T = 2` | D2 (consistent; `g = r`) | `IP′ = true` (`f_R(·; (0,1)) = f_R(·; (0,0)) = id`, so the window's relation equals `~₁`); DIL∃ holds on `W₂`; `τ = ∞`; `ε = 0, 0, 0`; SCH holds; row 5; `counts = false` | a decoder-guaranteed pass, which must not count: a control of the `IP′` flag |
| DEC-SW | HC-SW model (PREREG §3.1, `T = 1`) | D2 derivation only | D2 table `{00:0, 01:1, 10:1, 11:0}`; `d2_status = consistent`. No retention is evaluated | D2 recovers a circulating decoder |
| DEC-TS | HC-TS(4) model | D2 derivation only | D2 `undetermined`; table `{00:0, 10:1, 01:0, 11:0}` (D1). No retention is evaluated | D2 falls back on transport |

DT-S13, DT-S2s and DT-S1q are new instances of route III's toy `M_F` (E-reg), used only as
calibration controls. They are not Phase A tuples: Phase A evaluated S1(3) only at `T = 1`, under
S1's law, and had no two-presence-bit model. DEC-SW and DEC-TS derive decoders and evaluate no
retention.

**Positive-path coverage.**
- DT-S2s reaches row 5 with `IP′ = false` and counts.
- DT-S1q reaches row 5 with `IP′ = true` and must not count.
- NK-Wq at `T = 1` reaches the storage step (row 6 before B-4) on the native step form.
- DEC-SW shows D2 reproducing the decoder that gives HC-SW its row 6 in Phase A.
- Row 6 with `IP′ = false` has no Phase B control.

**Hand derivations behind the controls [D].**
- *NK-W.*
  - Under `δ₀`, HC-K1 gives `y(t₀+1) = (x₀, y₀, 0, 0, y₀)`.
  - With the two-slice locus on sites 1–4, `Q = {y₀}`: site 0 is the only outside neighbour of the
    arc 1–4 on `ℤ/5`.
  - `Q_{t₀+1} = x₀` varies with `κ`, so J-i fails at `t₀+1 ∈ H_T` for every `T ≥ 1`, and step 2
    assigns row 1.
  - On the write-tick support `{0000, 1001}`, any write-tick minimizer gives `ε_max(t₀+1) = 0`.
- *NK-Wq.* §1.3, Observation W1.
- *NK-K3.* The support, restated and re-derived from R:155–157:
  - `δ_b` has `x₂ = x₄ = 1` and every other non-carrier cell 0.
  - The background alone gives `y(t₀+1) = (0, 0, 1, 0, 1)` and `y(t₀+2) = (1, 1, 0, 0, 0)`.
  - With the carrier imprint of HC-K1, `y|_{1..4}(t₀+1) = (y₀, 1, 0, y₀+1)` and
    `y|_{1..4}(t₀+2) = (x₀+1, y₀, y₀, x₀)`.
  - The decoder returns `u₁ = y₀` at `t₀+1` (since `u₂ = 1 ≠ u₃ = 0`) and `u₂ = y₀` at `t₀+2`, so
    `ε = 0, 0`.
  - `y₀(t₀+1) = y₄(t₀) + y₁(t₀) + x₀(t₀) = x₀`, so J-i fails at `t₀+1`.
- *C-PAD-SMR's `Q`.* `y′₁ = y₀ + y₃ − x₁` if `y₂ = 0`, and `y₀ + y₂ − x₁` otherwise; `x′₁ = y₁`. So
  `Par(R) = {y₀, y₁, y₂, y₃, x₁}` and `Q = {y₀, y₂, y₃}`.
- *DT-S13.* §1.3, Proposition IP′.
  - Under the S1 law, `r(t₀)` and the channel cells other than cell 2 are uniform. The write gives
    `r(t₀+1) = c`, a clean write.
  - At `t₀+2` the arriving `(p₁, v₁)` has `p₁ = 1` with probability 1/2 and then sets `r = v₁`, which
    is uniform. So `P(r(t₀+3) ≠ c | σ) = 1/4`, and `P(r(t₀+3) = c | σ) = 3/4` gives `TV = 1/2`.
  - The singleton `{(1, v)}` is inconsistent (it maps `r = 0` and `r = 1` to `v`), and `{(0, v)}` is
    consistent. So `G* = {p = 0}`, the status is consistent, and with the observed failure at `t₀+3`
    and `τ = 1` the row is 2b.
- *DT-S2s.*
  - The write: at `t₀`, cell 0 is `(1, 0, c)`, so `v ↔ r` gives `r(t₀+1) = c`, a clean write. `r(t₀)`
    is uniform under the law, so (R-b) holds.
  - First hold tick: the arriving cell is old cell 2, `(0, 0, v₂)`, so the register is unchanged.
    `supp Q_{t₀+1} = {(0,0,0), (0,0,1)}`, `f_R = id` there, and `~₁` is the identity relation. D2 is
    consistent, with `g(0) = 0`, `g(1) = 1`; both read values are write-supported.
  - Second hold tick: the arriving cell is old cell 1, `(0, p′₁, v₁)` with `p′₁, v₁` uniform. When
    `p′₁ = 1`, `v ↔ s`, so `r` is unchanged.
  - `𝒬_{W₂} = {(0,0,v), (0,1,v)}`. `f_R((r, s); (0,1,v)) = (r, v)` merges `(r, 0)` with `(r, 1)`.
    These are distinct `~₁`-classes, both meeting `𝓛_{W₂}`, so `IP′ = false`. The merged
    configurations have the same `r`, so DIL∃ holds and `τ = ∞`.
  - `r = c` at `t₀+1`, `t₀+2` and `t₀+3`, so `ε = 0, 0, 0` and `TV = 1, 1, 1`.
  - J-1 holds at both hold ticks: the arriving cells are old cells 2 and 1, independent of `κ` and of
    `R`.
  - SCH holds: `Par(r) = {p, v, r}` at position 0, and only `r` is carrier-dependent there.
  - The carrier's own cell returns to position 0 at hold tick `t₀+3`, outside `H₂`. `D = 3` bits
    (`p₂`, `p′₂`, `p₁`). `E` is channel cells 1 and 2.
  - Row 5, and `counts = true`, since `T = 2 ≥ T*`, `IP′ = false` and `E` is nonempty.
  - Had the second presence bit swapped `v` into `r` instead of `s`, the same structure would merge
    `{0}` and `{1}` and fail, as DT-S13 does. So the pass is not guaranteed by the decoder.
- *DT-S1q.*
  - The arriving cells are `(0, 0)` at `t₀+1` and `(0, v₁)` at `t₀+2`, with `v₁` uniform. Both leave
    `r` fixed.
  - J-1 holds, because the arriving cells are independent of `(κ, r)`.
  - `𝒬_{W₂} = {(0,0), (0,1)}`, and both inputs act as the identity. So the window's relation is
    `~₁`, and `IP′ = true`.
  - DIL∃ holds; `ε = 0` throughout; SCH holds.
  - The environment is channel cells 1 and 2, so it is nonempty.
  - Row 5, with `counts = false`.
- *DEC-SW and DEC-TS.*
  - HC-SW: the write-tick support of `(r₁, r₂)` is `{00, 01}` and `f_R(·; p = 0, v) = swap`, so the
    classes are `{00}`, `{01, 10}`, `{11}`.
  - HC-TS: the support is `{00, 10}`, `f_R(·; 0) = (0, ℓ₁)`, and there is a single class.

**Countercontrols (a)–(f) of #1032, and (g), (h).**

| Countercontrol | How Phase B meets it |
|---|---|
| (a) bare previous-slice copy / H-2s | Read cells are the current slice only. The previous slice is in `R` (B-1) but never read. |
| (b) static declarative decoder | The decoder is fixed by the G-4 rule from `φ` and write-tick data. Its sensitivity to the other rules is recorded per tuple. A pass that the decoder guarantees (D2-T1, IP) never counts. NK-K3 shows that a declared decoder reading a planted clock is rejected by RS. |
| (c) quiet background imported through the prior | Not avoided: `ν_r` is that import, labelled H-sel. Its size is reported as `D(ν_r)` and `2^{−D}`. A positive at radius `r` is conditional on it. |
| (d) moving readout fixed in advance | Not used: `A` is fixed, and there is no clock. |
| (e) passive wave or wake | TP and RS. NK-W and NK-Wq are native-form wake controls. |
| (f) conditioning that makes the carrier indistinguishable | `P` is all carrier values and `f = y_Σ(t₀)`. The write gate B-2 reports a blind register as row 3w. Lemma PAD predicts it for `π₀`, and C-PAD-ALL checks it. |
| (g) fixed decoder that reads a tick marker | NK-K3. |
| (h) a duplicated passing pulse | HCP-h [PA] (row 1, P:349). Under B-1 the analogous native-form case is NK-W. |

### 6.4 Decision rule (preregistered: rules, not numbers)

**Per tuple.** PREREG §4's steps with amendments B-1 to B-6, in this order:
0. recurrence flags. Readback mode and PREREG's noext step 1 are not used: every tuple is in window
   mode.
1. B-2 write gate (row 3w).
2. RS (row 1) if J-1 fails at a hold tick of `H_{T′}`.
3. TR (2a) or EX (2b) if `τ < ∞` and `ε_max > ε*` at some tick of `W_{T′}`.
4. No retention (row 3).
5. Row 4 (declared `false`).
6. Storage if ST holds, then B-4 (I-10) and SCH (row 5 or 6). With B-6, an undetermined `G` is
   recorded and evaluation continues at step 7.
7. TI (row 7) if `ε_max = 0` on `W_T`.
8. I-6 (row 8).

**The implied-pass flag.** For each tuple decoded by D2 with `d2_status = consistent`, `IP′` is
computed as in §1.3: every class of the relation generated by `𝒬_{W_T}` that meets `𝓛_{W_T}` is a
single `~₁`-class.
- By D2-T1 and Proposition IP′, `IP′ = true` means the retention part of a storage row is
  guaranteed by the decoder.
- `IP′ = true` always at `T = 1`, since the two relations coincide.
- For tuples decoded by D1, D1′ or D2's fallback, `IP′ := false`: those decoders read no hold-tick
  data, so no pass is decoder-guaranteed.

**Per rule (the mechanism verdict).** Computed from `summary.json` fields only.
- **VOID** if any control mismatches, any exit is nonzero, or C-PAD-ALL or C-NP-ALL fails anywhere.
  No mechanism verdict is rendered.
- A tuple **counts** iff all of the following hold:
  - its row under the G-4 rule is 5 or 6;
  - `T ≥ T*`;
  - `IP′ = false`;
  - B-4's environment is nonempty.
- **STORAGE-ROBUST[rule]** iff there is a matched pair of local tuples, one at `N = 5` and one at
  `N = 8` with the same labelled pattern and the same `r ∈ {0, 1}`, such that both count at
  `T = 2` and at `T = 3`. A tuple that is not local at `N = 5` cannot be part of a robust verdict,
  so no shape counts as robust on one ring size alone.
  - **Reachability note [D].** Under the current family, no matched pattern can count, for either
    rule, so STORAGE-ROBUST is unreachable. The checks are write-tick facts: they hold for every
    `T`, every decoder rule and every later dynamics, and one failing size suffices.
  - **K1.** Proposition K1-NS excludes every K1 tuple, matched ones included. For the record:
    - `{1}`, `r = 0` is blind, since `y₂` pads `y₁(t₀+1) = c + y₂`;
    - `{2}`, `r = 0` is unwritten;
    - `{1}`, `r = 1` and `{1, 2}`, `r = 0` are written exactly and pass J-1 at `t₀+1`, and K1-NS
      excludes them;
    - the mirror patterns behave the same by reflection.
  - **SMR, at `N = 5`** (`y′_i = y_{i−1} + y_{R(i,y)} − x_i`; patterns with `r ∈ {0, 1}`):
    - `{1}`, `r = 0`: `y₁(t₀+1) = c + 1` if `y₂ = 1`, and `c + y₃` if `y₂ = 0`, with `y₂, y₃` free. The
      least worst-case write-tick error is 1/4.
    - `{1}`, `r = 1`: `y₂ = 0`, so `y₁(t₀+1) = c + y₃`, with `y₃` free. The register is blind.
    - `{2}`, `r = 0`: `y′₂` does not read `y₀`. The register is unwritten.
    - `{1, 2}`, `r = 0`: `y_A(t₀+1)` is `(c+1, 1)` if `y₃ = 1`, and `(c, y₄)` if `y₃ = 0`. The least
      worst-case error is 1/4.
    - `{4}`, `r = 0`: `y₄(t₀+1) = y₃ + (1` if `c = 1`, else `y₁)`, padded by the free `y₃`. Blind.
    - `{4}`, `r = 1`: `y₃ = 0`, so `y₄(t₀+1) = 1` if `c = 1` and `y₁` (free) if `c = 0`. The least
      worst-case error is 1/2.
    - `{3}`, `r = 0`: `y₃(t₀+1)` is padded by the free `y₂`. Blind.
    - `{3, 4}`, `r = 0`: `y₃(t₀+1) = y₂ + c` is padded, and `y₄(t₀+1)` is as for `{4}`, `r = 1`. The
      least worst-case error is 1/2.
    - So every matched SMR pattern is unwritten, or blind, or fails (R-c) at `t₀+1` (`1/4` and
      `1/2 > ε*`).
  - This agrees with the second review (c.6650383732 §4), derived here by hand without its script.
    Repairs are the owner's (G-9).
- **STORAGE-ISOLATED[rule]** iff some tuple counts and none is robust.
- **NO-STORAGE[rule]** iff no tuple counts.
- Every verdict also reports, separately:
  - tuples with storage rows that do not count, by reason (`T < T*`, `IP′ = true`, I-10);
  - decoder-sensitive tuples;
  - `G_undetermined` tuples;
  - the full row tally by (rule, `N`, `r`, `T`).

**Verdict text.** Rendered from `summary.json` by fixed templates, for example "Phase B, `<rule>`:
`<verdict>`; `<k>` of `<n>` tuples count; smallest ready radius among counting tuples `<r>`
(`D` = `<bits>` bits)." The templates are frozen with the preregistration, and a check step
regenerates the text and compares it byte for byte (§A.44).

**Interpretation, fixed in advance.**
- STORAGE-ROBUST: unreachable under the current family (reachability note). If a G-9 repair makes
  it reachable and it is reached on SMR: a conditional witness of one-step register-level retention
  on a toy ring, CONDITIONAL[E-SDC, H-sel (`ν_r`, `D` bits), H-cur (declared), the G-4 decoder rule,
  J-1 and DIL∃ as calibrated]. Not a SOURCE-CANDIDATE.
- STORAGE-ISOLATED on SMR: a reported conditional witness, carrying the same conditions, whose
  dependence on `N` or `T` is itself the finding. No mechanism claim.
- Any storage row on K1, counting or not: predicted impossible by Proposition K1-NS. If one
  occurs, it is a counterexample to K1-NS as stated, or an implementation error, resolved off-run
  as G-14 provides.
- NO-STORAGE: a scoped negative (§6.7).

### 6.5 Positive and negative controls, summarized

- *Negative (must reject):*
  - C-PAD-K1, C-PAD-SMR, C-PAD-ALL (no write);
  - C-NP-ALL, NK-W, NK-K3 (re-supply);
  - NK-Wq at `T = 2` (re-supply after a one-tick pass) and at `T = 1` (global register);
  - DT-S13 (exported at `T = 2` under D2, `IP′ = false`).
- *Positive path (must reach storage):* DT-S2s (row 5, `IP′ = false`, counts); NK-Wq at `T = 1` before
  B-4.
- *Guaranteed pass (must not count):* DT-S1q (row 5, `IP′ = true`).
- *Decoder rule:* DEC-SW (D2 consistent), DEC-TS (D2 undetermined).
- *Phase A material:* G-10.

### 6.6 Resource reporting (D-SML)

For every counting tuple, the record carries one row of OQ-8's table:
- added dynamical assumptions: none beyond posit (vii) on a toy graph (K1), or E-SDC (SMR);
- access and clock: H-cur (declared) on the current slice of `A`; no clock;
- preparation restriction: `ν_r`, `r`, `Z_r(A)`, `D(ν_r)` in bits, and `2^{−D(ν_r)}`;
- register and interaction size: `|A|`, `|Q|`, the rule's range;
- write probability: under the conditioned law the write occurs with probability 1, since there is
  no trigger; the probability that `π₀` produces the ready region is `2^{−D(ν_r)}`;
- retention duration `T` and `T′`; `ε_max` and `TV` at every tick; failures (D-MET item 4).

No ranking is issued while `w*` is unset (P:223). For NRR-1 the write probability under `π₀` and
the ledger are one quantity, so OQ-8's rule that "a vanishing write probability must not win
merely by reducing the preparation ledger" is met by reporting both and ranking by neither.

### 6.7 Possible outcomes and what each would and would not establish

| Outcome | Would establish | Would not establish |
|---|---|---|
| VOID (a control red, C-PAD-ALL or C-NP-ALL fails, or an exit) | that the implementation, the hand algebra, Lemma PAD or NP, or a convention is wrong | anything about native retention |
| NO-STORAGE on both rules | for K1 and SMR on rings `N ∈ {5, 8}`, `q = 2`, one-site carrier, these registers, these laws, `T ≤ 3`, `ε* = 1/20`, H-cur, the G-4 decoder and the amended classifier: no tuple counts | a no-go for native retention; anything at `d = 3`, other `N`, `q` or `a`; non-arc registers at `N = 8`; moving, derived or clocked registers; other laws; rule h; observers |
| STORAGE-ROBUST on either rule | **unreachable under the current family** (§6.4 reachability note). It can occur only after a G-9 repair; then, on SMR, a conditional witness on a toy ring, conditional on E-SDC and H-sel | that E-SDC is the physics (§A.29: no independent consequence of its switching rule); a source for `ν_r`; access |
| STORAGE-ISOLATED on SMR | a reported conditional witness on a toy ring, conditional on E-SDC and H-sel, whose dependence on `N` or `T` is itself the finding | a mechanism; robustness; sourcing; access |
| Any storage row on K1 (STORAGE-ISOLATED on K1, or a non-counting storage row) | predicted impossible by Proposition K1-NS; if it occurs, a counterexample to K1-NS as stated or an implementation error (G-14) | a K1 retention mechanism, until resolved |
| Storage rows only at `T = 1`, or only with `IP′ = true` | nothing beyond the decoder's construction (D2-T1, IP′); no counting tuple | retention |
| Every `r = −1` tuple row 3w, and every tuple covered by C-NP-ALL row 1 or 3w, as predicted | Lemmas PAD and NP hold on these instances (a consistency check) | anything about laws that restrict `x_A` and pad `y₀` |
| All storage decoder-sensitive | that the verdict depends on the off-support decoder rule | storage |

A negative or inconclusive result is acceptable if its scope is precise (owner, #1032
c.6610742427). No outcome moves a correctness band: every outcome sits on the consistency axis
until a counting tuple is confronted with something independent of its construction (§A.23).

### 6.8 Skepticism on a favourable outcome (§A.31)

Fixed before any run, for any counting tuple:
1. Re-derive the tuple by hand from its recorded classes, `Q` supports and `ε` values, and check
   Lemma H's direction (F-2, D:496–497).
2. Check that `Q` at every hold tick is the current slice of outside neighbours only, and that no
   previous-slice cell of `A` is read.
3. Check decoder sensitivity: report the rows under the other two decoder rules.
4. Check that the environment `E` exceeds one site, and report `|E| / N`.
5. Report `𝒬_{W_T}` by tick, and name the `~₁`-classes merged by inputs absent at `t₀+1`; these are
   what the test actually tested (`IP′ = false`).
6. Check whether a φ-invariant global functional is being read (S-C4b [MR]): a register covering
   the support of an invariant functional is not a local record.
7. For K1, any storage row contradicts Proposition K1-NS, since KN-1 to KN-3 hold for every K1 tuple
   by construction. Re-derive K1-NS's join and bound for that tuple, and report where they fail.
8. Report the result as CONDITIONAL with every hypothesis in §4 carried into it.

### 6.9 Invariant → checkpoint (§A.41)

| Invariant | Checkpoint |
|---|---|
| exact rationals; no floating point in a verdict | schema check on every probability field (regex as P:529); exit 2 |
| the frozen Phase B inputs are those reviewed at `F_B` | git blob ids at `F_B` compared with loaded bytes at start; exit 3; recorded in every output |
| Phase A's frozen files are read only | the tool opens them read only, and the job's final step checks their blob ids at the run commit against `F`; exit 3 |
| outputs do not depend on Python's hash seed (`REPLAY.json:105`: "Not established" for Phase A) | the job runs in two matrix legs with distinct fixed `PYTHONHASHSEED` values; a final job compares every per-tuple record and `summary.json` byte for byte and exits 7 on any difference; both legs' conclusions are read from the host |
| every rule instance is a bijection | C-INJ; exit 5; `injective` per tuple |
| the tuple family is fixed in advance | the family is generated from the frozen parameter file; its canonical list's hash is in the freeze and in `summary.json`; `tuples_evaluated` equals the list |
| controls first, halt on first red | controls carry the first orders; `first_failure`; exit 1 |
| Lemmas PAD and NP checked on every covered tuple | per-tuple assertions `pad_ok` and `np_ok` (NP keyed by the computed `G0_uniform`, not by the label `r`); exit 1 on failure |
| decoder fixed at the write tick | each decoder is computed by a function whose recorded inputs are `φ`'s id, `supp R_{t₀+1}` and (for D2) `supp Q_{t₀+1}`; their hash and the decoder table's hash are in each record |
| no decoder reads a later tick | the self-test runs each decoder rule on a tuple whose later ticks are altered and checks the table is unchanged |
| the D1 tie-break is Q8's | the self-test checks C-PAD's D1 table (`{0:0, 1:1}`) and DEC-TS's |
| a decoder-guaranteed pass never counts | `IP_prime` per tuple, computed from the two relations; DT-S1q (`IP′ = true`, must not count) and DT-S2s (`IP′ = false`, counts) compare it; the regeneration step recomputes `counts` from `IP_prime`, `T`, `row` and `E_sites` |
| Phase A rows unchanged by B-1 to B-6 | only under G-10 (b): a named regression step compares the chosen Phase A tuples with `PHASEA-EXPECTED.json` at `F`, exit 1. Under G-10 (c) there is no checkpoint, and the statement is not asserted as a run invariant; it remains the reviewed inspection of §6.2 |
| B-1 locus | `Q_cells` per tuple; NK-W and C-PAD controls compare it |
| B-2 write gate | `TV_t0p1` per pair and `write_gate` per tuple; C-PAD controls |
| B-4 LOC | `E_sites` per tuple and `row_pre_loc`; NK-Wq compares it |
| B-5 | `T_star` is in `summary.json` only; per-tuple rows are recomputed without it |
| B-6 | `G_undetermined` per tuple; exit 4 is never raised for Phase B tuples |
| Lemma P consistency | `n_supp` per tuple; a storage row with `T′ ≥ n_supp − 1` exits 6 |
| robustness from matched patterns only | `pattern`, `local` per tuple; the regeneration step recomputes the verdict from them |
| decoder sensitivity recorded | `row_D1`, `row_D1p`, `row_D2`, `decoder_sensitive` per tuple |
| mechanism verdict from structured data | a check step recomputes the verdict and its text from per-tuple JSON and compares byte for byte |
| one pass, no adaptive extension | host run record `run_attempt = 1`; no tuple outside the frozen list |
| resource limits | each shard's `timeout-minutes`; its conclusion read from the host |

### 6.10 Output schema (§A.44)

**Per tuple:** `phase-b/<tuple_id>.json`, schema `oret-phase-b/1`, with:
- identity: `tuple_id`, `order`, `rule` (`K1` or `SMR`), `N`, `q`, `Sigma`, `A`, `pattern`, `local`,
  `locus` (`two-slice`), `read_cells`, `Q_cells`, `r_values`, `Z_sites`, `law`, `D_bits`, `p_ready`
  (`2^−D`), `P`, `f`, `T`, `T_prime`, `ticks`;
- decoder: `decoder_rule`, `d2_status`, `decoder_table`, `decoder_inputs_hash`, `row_D1`, `row_D1p`,
  `row_D2`, `decoder_sensitive`;
- metrics: `eps` and `TV` per tick (rational strings); `TV_t0p1` per pair; `failures`;
- criteria: `Ra`, `Rb`, `write_gate`, `J1` per hold tick, `SCH` per hold tick, `DIL`, `tau`,
  `classes_T`, `Q_supp_by_tick`, `IP_prime`, `G_star_T`, `G_star_Tprime`, `G_status`, `G_undetermined`,
  `eta`, `lemma_h_bound`, `recurrence_flags`, `n_supp`, `E_sites`, `pad_ok` (for `r = −1`), `np_ok`
  and `G0_uniform` (for C-NP-ALL tuples);
- result: `row_pre_loc`, `row`, `counts` (Boolean);
- `expected` and `comparisons` for control tuples only;
- `frozen_inputs`, `run`.

**`summary.json`:**
- `schema`, `tuples_frozen`, `family_hash`, `tuples_evaluated`, `first_failure`, `controls_green`,
  `exit`, `eps_star` (`"1/20"`), `T_star`, `w_star` (`null`), `decoder_rule`;
- a row tally per (rule, `N`, `r`, `T`);
- the per-rule mechanism verdict, the lists named in §6.4, and `verdict_text`.

**Exits.**
- 0 complete;
- 1 control mismatch, or `pad_ok` or `np_ok` false;
- 2 schema or floating point;
- 3 a frozen input differs from its blob id;
- 4 not raised for Phase B tuples (B-6);
- 5 injectivity or method check;
- 6 Lemma P inconsistency;
- 7 hash-seed legs differ;
- other nonzero: error.

A verdict reads exit statuses, the host's job and step conclusions, and `summary.json`; never log
text.

### 6.11 Budget and execution form (for a later authorization)

- CI only (§A.40), sharded by (rule, `N`), with the controls in every shard's prefix, in two
  hash-seed legs. One pass; no adaptive extension; halt on first red.
- The largest state space is `2¹⁶`, as in Phase A. The run time is not estimated here: nothing was
  run. A later implementation unit states a measured bound from its self-test before any dispatch
  request.
- Implementation reuse: `phaseA/phasea.py` provides exact enumeration, J-1, DIL∃, `τ`, the
  `G`-rule and §4 row assignment (IMPLEMENTATION-NOTES §1). What may be reused, and how, is G-10.

### 6.12 Hard-to-vary checks (§A.29)

- **Nothing new is adopted.** The F2 items are E-SDC (unadopted, tested only as a named
  hypothesis) and `ν_r` (imposed, H-sel). Neither is presented as established, and a positive
  under either is conditional on it.
- **Results the amendments preserve, stated in advance.** Every Phase A row and value, and Phase A's
  frozen files (§6.2, by inspection). The reviewer confirms this from `PHASEA-EXPECTED.json`.
- **Independent prediction.** The amendments are methodological; they are not a Layer-0 revision
  and do not carry an independent prediction in §A.29's sense.
  - C-PAD-ALL and C-NP-ALL are controls: preregistered checks of hand lemmas on tuples the lemmas
    were not built from. They are not independent predictions.
  - NRR-1 makes no independent prediction. So even a robust positive could not be adopted; it would
    be a conditional witness.
- **No variant fits any outcome.** The rules, rings, registers, laws, windows, decoder rule, `T*`,
  `ε*`, counting rule, matching rule and verdict templates are frozen before any evaluation. The law
  family has one parameter, `r`, and every value is reported. Adding a law, register, rule, ring size
  or decoder after results is a new freeze.
- **The test can fail with its assumptions holding.** DT-S13 fails at `T = 2` under D2 with every
  declared assumption holding, and DT-S2s passes where it could have failed. A decoder-guaranteed
  pass (`IP′ = true`) never counts, and DT-S1q checks this.
- **Refuting outcomes for the design.** Each of the following refutes the named lemma or the
  implementation, and halts the run:
  - C-PAD-ALL failing on any tuple (Lemma PAD);
  - C-NP-ALL failing on any tuple (Lemma NP);
  - NK-Wq at `T = 1` assigned anything other than I-10 (Observation W1);
  - DT-S13 assigned anything other than 2b, DT-S2s anything other than a counting row 5, or DT-S1q
    anything other than a non-counting row 5 (Proposition IP′).

***

## 7. Gate items for the owner (g)

Each item gives the exact alternatives, their scientific consequences, whether an alternative can
make a test tautological or non-discriminating, any new assumption it introduces, and the writer's
recommendation. **The recommendations are recommendations only; no alternative is chosen here.**
The test of §6 is decision-complete once every item is decided.

**Gate classes (review c.6649925951).**
- Scientific: G-2, G-3, G-4, G-5, G-6, G-8, G-9, G-14, G-15.
- Partly scientific: G-1, G-7, G-13, G-16.
- Administrative: G-10, G-11, G-12.

### G-1. Which rules are evaluated (K1 stays in every alternative)

- **Alternatives.** (a) K1 and SMR. (b) K1 only. (c) K1 and SMR, plus rule h through a
  non-exhaustive method in a separate design.
- **Consequences.**
  - (a) tests the in-corpus rule with state-dependent coupling beside the native step form.
  - (b) restricts Phase B to the native step form. Given Proposition K1-NS, no K1 tuple is predicted
    to reach storage, so (b) tests K1-NS and the classifier rather than a candidate.
  - (c) reaches `d = 3` but needs a different method and its own validation.
  - Under (a), SMR registers that contain site 1 and not sites `N−1` and `N−2` fall under the second
    review's unreviewed extension of K1-NS. SMR is open on paper only for registers on the other
    side of the carrier.
- **Tautology risk.** None by itself. Under (b), the K1 half is predicted (G-14).
- **New assumptions.** (a) and (c): E-SDC as a named, unadopted hypothesis for SMR. (c): rule h as
  physics, outside posit (vii).
- **Recommendation: (a).** SMR is the only in-corpus rule whose transfer depends on another region's
  state at a size that can be enumerated, and K1 is kept.

### G-2. SMR's status

- **Alternatives.** (a) Test SMR under the named, unadopted extension E-SDC. (b) Exclude SMR until
  E-SDC has a hard-to-vary form.
- **Consequences.**
  - (a) a positive on SMR is CONDITIONAL[E-SDC] and cannot be adopted (§A.29).
  - (b) Phase B reduces to G-1 (b).
- **Tautology risk.** None.
- **New assumptions.** (a) E-SDC, named and unadopted.
- **Recommendation: (a).** Testing a named hypothesis is not adopting it, and its conditional status
  is carried into every verdict.

### G-3. Register locus for copy-form rules

- **Alternatives.** (a) Two-slice locus with current-slice read (B-1). (b) Phase A's convention: `R`
  = the read set, with the register's previous slice in `Q`. (c) Both, reported side by side, with
  the verdict under (a).
- **Consequences.**
  - (a) treats the register's previous slice as part of its state, unread.
  - (b) treats `x_A` as an outside input. From the second hold tick, `x_A(t) = y_A(t−1)` carries the
    record, so J-i fails at `t₀+2` for every written register. Every `T ≥ 2` tuple is then RS,
    whatever the dynamics.
- **Tautology risk.** (b) makes `T ≥ 2` non-discriminating in the rejecting direction: it can never
  pass.
- **New assumptions.** (a) the locus convention, imposed.
- **Recommendation: (a)**, with (c) as an affordable addition.

### G-4. Decoder rule off the write-tick support (Q8's deferred rule)

- **Alternatives.**
  - (a) D2, with D1 and D1′ recorded, and the counting condition `IP′ = false` (§6.4).
  - (b) D2 without the `IP′` condition.
  - (c) D1 only (Q8 exactly).
  - (d) D1′ only.
  - (e) Count a tuple only if its rows under D1, D1′ and D2 agree.
- **Consequences.**
  - (a) can count circulating storage of the HC-SW kind, but only on tuples whose later hold ticks
    merge `~₁`-classes through inputs D2 never read (DT-S2s), so the check could have failed.
  - (b) counts tuples whose retention D2 guarantees: every consistent-D2 tuple at `T = 1`, and every
    one with `IP′ = true` (D2-T1, IP′; DT-S1q).
  - (c) reads no hold-tick data, so every DIL∃ check is a genuine test. It false-rejects circulating
    storage whose invariant decoder differs from the lexicographic one (HC-SW becomes TR; P:213).
  - (d) is the mirror image of (c), with different false rejections.
  - (e) is conservative. It rejects HC-SW-type circulation, because D1 does.
  - **On the NRR-1 family the choice between (a) and (c) does not matter.** D2 is undetermined on
    every written tuple that is not blind (§4.4): on paper for K1, and by the second review's
    unretained check for both rules. So (a) falls back to D1 there and coincides with (c), and the
    circulation (a) keeps testable is exercised only by the controls (DEC-SW, DT-S2s). The choice
    matters for the controls and for any later family.
- **Tautology risk.**
  - (b) is non-discriminating by construction on `IP′ = true` tuples. It would present guaranteed
    passes as storage, against the governing principle.
  - (a) removes those passes from counting.
  - (c), (d) and (e) carry no decoder-guaranteed pass.
- **New assumptions.** (a) and (b): that the input support at `t₀+1` may be used to build the decoder.
  This goes beyond the reading of c.6622434587 (§4.4).
- **Recommendation: (a).** It keeps the owner's Q1 ruling on circulation testable where a family
  allows it, and never counts a pass the decoder guarantees. On this family it acts as (c). (c) is
  the alternative if the owner prefers a decoder that reads no hold-tick data at all, at the cost of
  false-rejecting circulation.

### G-5. `T*` and `w*` (B-5)

- **Alternatives.**
  - (a) `T* = 2`; `T = 1` reported only; `w*` unset, with `2^{−D}` reported.
  - (b) `T* = 1`, the owner's one-step reading.
  - (c) `T* = 3`.
  - (d) Any of these with a `w*` set by the owner.
- **Consequences.**
  - (a): the counted test always includes a hold tick after the first.
  - (b) with G-4 (a):
    - D2-consistent `T = 1` tuples have `IP′ = true` (D2-T1) and do not count.
    - Tuples decoded by D2's fallback carry `IP′ := false` and can count at `T = 1`. On the NRR-1
      family that is every written tuple (§4.4), so (b) with G-4 (a) acts there as (b) with G-4 (c).
    - The one-tick test is then genuine, since D1 reads no hold-tick data, but it is weak. On a
      copy-form register, the carrier's previous-slice channel and the register's own previous slice
      act only from the second hold tick (Observation W1; G-3).
  - (b) with G-4 (b): every D2-consistent `T = 1` pass counts.
  - (c) requires more and is cleaner, at the cost of fewer counting tuples.
  - (d): a native write has `w = 1` under the conditioned law, so `w*` would act only through
    `2^{−D}`. That is the ledger, which OQ-8 does not allow to win alone.
- **Tautology risk.**
  - (b) with G-4 (b) is non-discriminating by construction.
  - (b) with G-4 (a) is not tautological: no counted pass is decoder-guaranteed. It is weak, as above.
- **New assumptions.** None.
- **Recommendation: (a).** It is the smallest window that holds a hold tick D2 did not read, and the
  first at which the copy-form previous-slice channels act.

### G-6. Laws and preparations

- **Alternatives.**
  - (a) `ν_r`, `r ∈ {−1, 0, 1, 2, ∞}`; `P` = all carrier values; `δ_b` in NK-K3 only.
  - (b) Add the restricted-carrier family `x₀ = 0` (HC-K4's pattern, R:163–168) as a separate,
    labelled family.
  - (c) Add one-sided ready regions, defined by a pattern and two radii so that they can enter
    robustness:
    - for an arc `A` on one side of the carrier, `Z^{(r_far, r_opp)}(A) := A ∪ {sites beyond A's far
      end within distance r_far} ∪ {sites on the other side of the carrier within distance r_opp of
      site 0}`, with `r_far, r_opp ∈ {0, 1, 2}`;
    - sites between the carrier and `A`'s near end, and all other sites, are free;
    - patterns, locality and matching are as in §6.2, with the labels of `I` read from `Z^{(r_far,
      r_opp)}(A)`.
- **Consequences.**
  - (b) fixes the carrier's previous slice, so Lemma NP no longer forces RS under `δ₀`. Observation
    W1 shows such tuples reaching the storage step at `T = 1`. Requirement 2 asks for independently
    available preparations, and this family restricts them.
  - (c) lets a register be ready on its far side while the carrier keeps a free pad (Lemma NP), and
    lets the opposite side of the carrier be ready where a switch needs it (SMR's left-side
    registers read `y₁` when `y₀ = 0`).
    - **For K1**, Proposition K1-NS covers every product law, so (c) cannot produce a K1 storage row.
      It would test K1-NS rather than open a route.
    - **For SMR**, left-side registers (containing site `N−1` or `N−2`) are not covered by any paper
      result here. (c) is the shape they need.
  - (c) also bears on G-9: one-sided patterns are what G-9's repairs (b) and (c) refer to.
- **Tautology risk.**
  - (b) at `T = 1` under D2 is non-discriminating (D2-T1). Under G-4 (a) it never counts.
  - `r = ∞` and `r = 2` at `N = 5` test re-supply only (Lemma NP): they cannot pass, so they do not
    discriminate storage.
  - (c) for K1 is predicted negative (K1-NS). That is a check of K1-NS, not a test of a candidate.
- **New assumptions.** (b): a restriction on the carrier. (c): a further imposed shape, H-sel, with
  two radii.
- **Recommendation: (a), with (c) added for SMR**, and for K1 only as a check of K1-NS if G-14 (b) is
  chosen. (b) is not recommended, because it restricts the preparations requirement 2 asks to be
  independently available.

### G-7. Write gate (B-2)

- **Alternatives.** (a) Adopt B-2. (b) Keep Phase A's precedence.
- **Consequences.** Under (b), an unwritten register can be labelled TR or EX (Lemma PAD's tuples
  under `π₀`).
- **Tautology risk.** None.
- **New assumptions.** None. It reads NB-1, which is already adopted.
- **Recommendation: (a).** It changes no Phase A row and prevents mislabelling.

### G-8. Locality gate (B-4)

- **Alternatives.** (a) A nonempty environment. (b) An environment of at least `|A|` sites, for NRR-1
  tuples only. (c) No gate.
- **Consequences.**
  - (a) excludes only registers whose neighbourhood is the whole system (NK-Wq).
  - (b) is stricter.
  - (c) lets a near-global register count; owner principle: "globally preserved information is not
    locally recoverable information" (#914 c.6562546850).
- **Tautology risk.** None.
- **New assumptions.** The margin (imposed).
- **Recommendation: (a)**, with robustness (G-9) carrying the remaining locality burden. Both (a) and
  (b) leave every Phase A row unchanged.

### G-9. Robustness

**Robustness is unreachable under the current family.** By the reachability note of §6.4,
re-derived by hand:
- no matched local pattern can count for SMR (each is unwritten, blind, or has least write-tick error
  1/4 or 1/2);
- K1-NS excludes every K1 tuple.

So the present criterion (matched local patterns at `N = 5` and `N = 8`, `r ∈ {0, 1}`) cannot pass,
and as it stands it is non-discriminating in the rejecting direction. The repair is the owner's.
No repair is chosen here, and none is shown to make the criterion reachable.

**Part 1: repair.**
- **Alternatives.**
  - (a) Pair `N = 8` with `N = 6` or `N = 7` instead of `N = 5` (`|S| = 2¹²` or `2¹⁴`) for robustness.
    Local patterns then allow `|I| ≤ 4` or `|I| ≤ 5`. `N = 5` (K-18(b)) stays in the instance set.
  - (b) Define patterns for G-6 (c)'s one-sided regions and admit them to robustness, keeping
    `N = 5` and `N = 8`.
  - (c) Both.
  - (d) None: keep the criterion as defined, and state in the preregistration that STORAGE-ROBUST is
    unreachable under this family. The strongest positive verdict is then STORAGE-ISOLATED.
- **Consequences.**
  - (a): shapes such as an SMR register `{1, 2}` with readiness one step beyond (`C A A Z`,
    `|I| = 4`) become local.
    - On the right side of the carrier, the second review's unreviewed extension of K1-NS predicts
      that they do not count.
    - The left-side SMR shapes the writer could construct need readiness on both sides of the
      carrier. With an exact write and a pad for Lemma NP, these have `|I| = 5`, so they are local
      only at `N = 7`, and the symmetric `ν_r` supplies them only at `r = 2`, which robustness
      excludes.
    - So (a) alone is not shown to make the criterion reachable.
  - (b): one-sided regions supply the left-side readiness. But every one-sided SMR shape the writer
    could construct with an exact write that passes Lemma NP has `|I| ≥ 4`, so it is not local at
    `N = 5`. (b) alone is not shown to make the criterion reachable. The writer has not shown that no
    such shape exists.
  - (c): the writer found no paper argument here that excludes every matched pattern under (a) and
    (b) together. Whether STORAGE-ROBUST is then reachable is what a run would show. This is not a
    proof of reachability.
  - (d): the per-rule verdict can only be STORAGE-ISOLATED, NO-STORAGE or VOID. §6.4 and §6.7 already
    record STORAGE-ROBUST as unreachable under the current family.
- **Tautology risk.**
  - (d) keeps a criterion that cannot pass, so it is non-discriminating, and it must be reported as
    such.
  - (a) or (b) alone may also leave it unreachable (not shown either way).
  - (c) has no known tautology.
- **New assumptions.** (a): the pairing of ring sizes and the locality bound. (b), (c): G-6 (c)'s
  one-sided shape and radii (H-sel).
- **Recommendation: (c), with N = 7 for the pairing.** It is the only alternative under which no
  argument here predicts the criterion unreachable. If the owner prefers not to enlarge the instance
  set, (d), with the criterion reported as unreachable.

**Part 2: windows.**
- **Alternatives.** (a) Both `T ∈ {2, 3}`. (b) `T = 2` only.
- **Consequences.** (a) asks a matched pair to hold over two windows. (b) is weaker.
- **Tautology risk.** None beyond Part 1.
- **New assumptions.** None.
- **Recommendation: (a).**

**Part 3: single-size counting.** Letting a shape count as robust on one ring size alone is not
offered. Both reviews block it, because it would let a finite-size or wrap artifact count.

### G-10. Phase A material

- **Alternatives.**
  - (a) Replay: re-evaluate Phase A tuples with `phaseA/phasea.py` (`3d5edd97`). This is a partial
    replay under D9 (#1032 c.6629059049). It needs its own authorization, which c.6649977592 does
    not give, and it is never a Phase A result.
  - (b) Regression test: a new Phase B tool is checked against `PHASEA-EXPECTED.json` at `F` on named
    Phase A tuples, authorized by name. It is not a replay of Phase A and not a Phase A result.
  - (c) Import only: the Phase B tool imports functions from `phasea.py` at its landed blob and runs
    no Phase A tuple.
- **Consequences.**
  - (a) adds Phase A rows to Phase B's evidence and needs the separate authorization.
  - (b) validates a new implementation against frozen expectations, and gives "Phase A rows unchanged
    by B-1 to B-6" a §A.41 checkpoint (§6.9).
  - (c) relies on the Phase A tool's calibration only through the shared code. It inherits the tool's
    unestablished hash-seed determinism, which the invariant in §6.9 checks. It leaves "Phase A rows
    unchanged" as a reviewed inspection with no checkpoint.
- **Tautology risk.** None.
- **New assumptions.** (c): that the imported functions behave as in run 1.
- **Recommendation: (b), authorized by name**, because §A.41 asks every asserted invariant to have a
  checkpoint, and (b) is the only alternative that gives one without a replay. DT-S13, DT-S2s,
  DT-S1q, DEC-SW and DEC-TS supply the remaining coverage.

### G-11. Scope extensions (each a separate design)

- **Alternatives.**
  - (a) None.
  - (b) K1 on a `d = 3` torus by exact linear algebra over `𝔽₂`. Each `ν_r` is uniform on a subspace,
    so supports and J-1 reduce to rank computations. It would be validated against full enumeration
    at `N = 5, 8`.
  - (c) Larger rings, `q > 2`.
- **Consequences.** (b) reaches the native graph's dimension for K1, where Proposition K1-NS (if
  right) still applies.
- **Tautology risk.** None.
- **New assumptions.** (b): the linear-algebra method's equivalence to enumeration, to be validated.
- **Recommendation: (a) for this phase.**

### G-12. Governance form

- **Alternatives.** (a) A research run on a disposable branch with an owner-designated freeze `F_B`,
  as for Phase A. (b) A native V3 round under §A.39.
- **Consequences.** Different record forms. No scientific difference.
- **Tautology risk.** None.
- **New assumptions.** None.
- **Recommendation: (a)**, as for Phase A.

### G-13. Review record before freeze

- **Alternatives.**
  - (a) One review record, landed with the freeze, covering the verdict-path premises:
    - Lemma H (ST);
    - Lemma P (exit 6);
    - Lemmas PAD and NP (C-PAD-ALL, C-NP-ALL, B-2);
    - Observation D2-T1 and Proposition IP′ (the counting rule);
    - the reachability note of §6.4;
    - the coverage argument;
    - every control's hand values, DT-S2s included;
    - Proposition K1-NS as restated (KN-1 to KN-4, without the old independence hypothesis), if G-14
      (a) is chosen.

    Lemmas S′, Q and L stay motivation only. The second review's SMR extension of K1-NS enters only
    if a later design uses it.
  - (b) Review only §1.3 and §6.3's derivations.
  - (c) No review record.
- **Consequences.** (c) would put unreviewed premises on the verdict path, against §A.46 item 7.
- **Tautology risk.** None.
- **New assumptions.** None.
- **Recommendation: (a).**

### G-14. Proposition K1-NS: adopt as a predicted control, or run K1 as a measurement (K1 is run under both)

- **Alternatives.**
  - (a) After review (G-13 (a)), adopt K1-NS as a predicted control. Every K1 tuple is still run, and
    every one must take a non-storage row. KN-1 to KN-3 hold for every K1 tuple by construction, and
    a tuple with KN-4 false fails (R-c). A K1 storage row is a control failure: exit 1, VOID.
  - (b) Run K1 as a measurement. K1-NS is recorded as a preregistered expectation. A K1 storage row is
    reported, and is read as a counterexample to K1-NS as stated, or as an implementation error, to be
    resolved off-run.
- **Consequences.**
  - (a): the K1 half is settled on paper for this family, and the K1 tuples become a check of K1-NS
    and of the implementation. The K1 verdict is predicted NO-STORAGE, with no exceptions within
    the family. G-6 (c) for K1 adds further checks of the same prediction.
  - (b): K1 stays an open measurement, and a K1 storage row does not void the run. G-6 (c) for K1
    probes the same prediction without halting on it.
- **Tautology risk.**
  - Under (a), K1's NO-STORAGE is predicted, not discovered, so it does not discriminate as a
    measurement of retention. It still discriminates as a check of K1-NS.
  - Under (b), the K1 measurement can fail either way.
- **New assumptions.** (a) promotes a hand result with no review record on `main` to a halting
  control. Its review is required first (G-13).
- **Recommendation: (b).** K1-NS has no review record on `main`. A measurement can refute it without
  voiding the SMR half. (a) is appropriate only after the G-13 review accepts it.

### G-15. An undetermined `G` at the storage step (B-6)

- **Alternatives.** (a) B-6: record `G_undetermined`, treat ST as not certified, continue at step 7.
  (b) Keep PREREG's exit 4, which halts the run.
- **Consequences.**
  - Under (b), any tuple that *may* reach step 6 with `G_status = inconsistent` halts the whole run.
    K1-NS shows exact DIL∃ failing but does not decide `G_status`. On the instances the second review
    checked, the J-1-passing written K1 tuples have `G_status = empty`, which never halts.
  - Under (a), such a tuple takes row 7 or 8. A storage witness that needs a non-maximal consistent
    `G` would be missed: a false negative, flagged by `G_undetermined`.
- **Tautology risk.** None. (a) can only withhold storage.
- **New assumptions.** None.
- **Recommendation: (a).** It is a guard against a halt that the paper results do not exclude.

### G-16. Lemmas PAD and NP as halting controls

- **Alternatives.** (a) C-PAD-ALL and C-NP-ALL halt the run on failure (exit 1). (b) They are
  reported predictions only.
- **Consequences.**
  - Under (a), an error in either lemma voids the run.
  - Under (b), the run continues, and a failure is reported as a refutation of the lemma.
- **Tautology risk.** None. Both predict rejections.
- **New assumptions.** (a) relies on the lemmas being reviewed (G-13).
- **Recommendation: (a)**, conditional on G-13 (a). The lemmas are short and their failure would
  indicate an implementation error as likely as a lemma error.

***

## 8. Review packet

The independent reviewer is asked to check, at the exact head:

1. **§1.1–§1.2.** The 49/49 count, each quotation verbatim, and the locators (RESULT.md:42–43;
   `REPLAY.json:105`).
2. **Lemma PAD.** The proof, the copy-form claims for K1, SMR and rule h, and the citations
   (D:151–155; #914 c.6563955678).
3. **Lemma NP.** The proof, and its consequences at `r = ∞`, at `r = 2` with `N = 5`, and for K1 at
   `r = 2` with `N = 8`. That C-NP-ALL, keyed by the computed `G0_uniform`, covers every `δ₀`-equal
   law.
4. **Observation D2-T1 and Proposition IP′.**
   - Both proofs.
   - That `IP′ = true` at every `T = 1`.
   - That `IP′ = false` is necessary for the check to be able to fail under D2.
   - The account of why the syntactic flag was wrong.
5. **DT-S13, DT-S2s and DT-S1q.**
   - Every expected value and row.
   - That DT-S13 and DT-S2s have `IP′ = false` and DT-S1q has `IP′ = true`.
   - That DT-S2s could have failed.
   - That none is a Phase A tuple.
6. **Proposition K1-NS, as restated.**
   - The join, and that `B e_{y₀} = b`.
   - The translation argument for `η ≥ 1/2` without J-1 or the old independence hypothesis.
   - The conclusion for every K1 tuple.
   - The `G_status` correction.
   - The SMR limitation (sites `N−1`, `N−2`).
   - That the second review's SMR extension is recorded as unverified and is not used.
7. **Observation W1 and NK-Wq.** Unchanged values; the ELABORATING classification; the D1 and D2
   rows.
8. **NK-W, NK-K3, C-PAD-K1, C-PAD-SMR, DEC-SW, DEC-TS.** Each expected value, row, decoder and
   `Q_cells`.
9. **D1.** That it is Q8's tie-break exactly, and that the C-PAD decoder is the identity.
10. **Patterns, robustness and reachability (§6.2, §6.4).**
    - That the nine local `N = 5` patterns are exactly those listed, that eight have one matched
      `N = 8` tuple each, and that `A = {1, 4}` has none.
    - The hand reachability note, pattern by pattern.
    - That §6.7 lists no outcome that cannot occur.
11. **B-1 to B-6.** That no Phase A row changes, that coverage holds, and how the "Phase A rows
    unchanged" statement is (or is not) measured, under G-10.
12. **§4.4.** That D2 is undetermined on every written K1 tuple satisfying KN-4, and the consequence
    for G-4.
13. **§7.** That every gate item gives alternatives, consequences, tautology risk, new assumptions
    and a labelled recommendation, and that no alternative is chosen. In particular G-9's four
    repairs and G-5 (b) with G-4 (a).
14. **Claim/evidence boundary.**
    - No statement presents NRR-1, E-SDC, `ν_r` or any §1.3 result as established.
    - Every negative is scoped.
    - "Smallest" is argued, not proved.
    - K1 is described as the native step form on a toy graph.
15. **§9.** Each off-`main` reference and its classification.

***

## 9. References off `main`, and literature (§A.42 item 8)

| Reference | Used for | Classification |
|---|---|---|
| #1032 comments (6610742427, 6611966162, 6612956983, 6614257383, 6621961326, 6622018720, 6622434587, 6623962802, 6628404473, 6629059049, 6649418760) | owner decisions and authorization, quoted | provenance; owner records quoted with their comment ids |
| #1032 c.6649977592 (amaybaum, 2026-11-05T04:49:59Z) | the owner's decision on the revisions, and the governing principle quoted at the head of this file | provenance; an owner record quoted with author and time (§A.42 item 7) |
| #914 c.6563412926, c.6563955678, c.6566997020, c.6612951653, c.6562546850, c.6563417740, c.6561476122 | matrix rows, P2-G, K-8, H-μ, the annotation, the persistence principle, K1-PERS-1 scope, rule h's statement | provenance. Rule h's definition used here is the one on `main` (`INTERFACE-CONTRACT.md:35–36`) |
| #1115 c.6649925951 | the independent review of `fdacce54`, and the reviewer's argument re-derived as Proposition K1-NS | provenance. K1-NS is re-derived in full here; no claim rests on the comment |
| #1115 c.6650383732 | the second independent review, of `5839e064`: `IP′`, the restated K1-NS, the unreachability of STORAGE-ROBUST, the SMR extension of K1-NS, and its own counts | provenance. `IP′`, K1-NS and the reachability note are re-derived by hand here. The review's counts come from its own unretained check and support no claim. The SMR extension is recorded as unverified |
| PR #1078 (closed) and its reviews | the review history of `ROUTES.md` and DESIGN-PULSE | provenance. The texts used are on `main` at `F`; their reviews are not, so they are labelled [R] and [DP] and used as motivation only |
| PR #1093 (merged) | how Phase A's evidence reached `main` | provenance; the evidence itself is on `main` |
| `research/o-obsmu-20261104` at `f67b9f0c`, `ANALYSIS.md` §4.4 and §4.6.2 | the name P-SDC; the reading that retained records on K1 are tied to O-RDY | provenance. No claim here uses its content as support: E-SDC is stated from SM:104 and SM:112 on `main`, and the readiness point rests on MR★ C-3 on `main` |
| #1110, #1112 | the O-OBSMU review status; the arrow-of-time pointer | provenance |
| `REVIEW-Q7.md` | cited by PREREG for the J-1 wording | not located (programme `README.md:37–43`); the wording used is the one frozen in PREREG §2.7 on `main` |

**Literature.**
- J. T. Lizier, M. Prokopenko, A. Y. Zomaya, "A framework for the local information dynamics of
  distributed computation in complex systems", arXiv:0811.2690v2 (v1 2008-11-17, v2 2013-10-10).
  **Read directly: abstract page only.**
  - It states that "blinkers embody information storage" and "particles are information transfer
    agents" in cellular automata.
  - Its measures are statistical and per cell; they are closest to SCH and ICH here. They do not
    separate a blinker held by a quiet neighbourhood from one re-supplied by it.
  - Not used as support.
- Landauer 1961, Bennett 1982 (as in `SOURCES.md`); Fredkin and Toffoli 1982; Toffoli and Margolus,
  *Cellular Automata Machines* (1987), on second-order reversible rules; Margolus's billiard-ball
  model, on memory by circulation: **cited from memory, not re-read.** None is used as support.
