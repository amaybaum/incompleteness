# TUNE-1, Step 2: amendment 1 to the definitions and controls

**WIP / UNVERIFIED draft amendment, for independent review.** It implements the owner's
decisions 1–8 recorded at PR #1237, comment 6821448213. The comment is from `amaybaum`,
2026-11-12T10:44:37Z, author association `OWNER`, and was posted through the `claude` GitHub app;
it reads "Adopt as proposed (Recommended)". The decision "authorizes paper-only definition repair
and review only. It authorizes no computation and adopts no premise." This file reruns no control,
adopts no premise and changes no manuscript or Lean file.

**Amends.** `TUNE-1-STEP2-PROPOSAL.md` in this directory, at `e676c42a`, sha256
`2a081101efae469b39b747ef8f3641f259e55892705bc0f7759adf3ac7499fd5`. That file is not edited.
Where this amendment and the proposal differ, the amendment governs. Everything not amended stands.
The Session 1 record, `TUNE-1-STEP2-SESSION1.md` at `498ec02f`, is the source of the findings
implemented here (RC-1, RC-2, Rd-1 to Rd-8).

**Labels.** As in the proposal: [K], [P], [R], [W]. Every argument below is [W], unreviewed.

***

## A0. Plain summary

Session 1 found that the "whole Bloch ball" test, and the gate and read tests with it, were checked
on a freely chosen quantum model of the records. Parts of that model are not fixed by any record. The
owner decided to restate those tests on what the observer can actually record. This amendment
writes that restatement:
- gates and reads are tested by sequences of rounds after every preparation;
- reads must behave like ideal repeatable measurements, which is tested by reading twice;
- the Bloch-ball test counts only states that the available tests can tell apart.

It also fixes three readings: how errors after a herald are measured, how many rounds must follow a
preparation, and how the compiled-simulator controls are scored. It names in advance the twelve
controls the change must preserve, and adds the two that exposed the defect as new controls. A hand
check shows that the real-quantum-theory model of Session 1 is now excluded. The controls are
rerun only after this amendment is reviewed, and the linear-rule analysis waits until that rerun
has itself been reviewed.

***

## A1. Decision 1: Q3, Q5 and Q6 on record laws

### A1.1 Declared target and identified tests

A family declares, as part of its specification (D1: a function of `n` alone), a **target**
`𝔔* = (n̂, a, b, p, q_a, q_b)`:
- a rotation axis `n̂`;
- two unit Bloch vectors `a, b` with `a·b ∈ [−1/2, 1/2]` (equivalently `Tr(P_a P_b) ∈ [1/4, 3/4]`);
- for each `θ`, a probability vector `p(θ)` on gate-round records;
- for each read, the two classes of its records, with fixed conditional record laws `q_a(·|a1)`,
  `q_a(·|a0)`, and likewise for `b`.

The target's instruments are fixed by these data, not chosen:

- gate `c(θ)`: `𝓘*_{c(θ),h} = p_h(θ) · Ad(e^{−iθ n̂·σ/2})`;
- read `c_a` (Lüders): `𝓘*_{c_a,h}(σ) = q_a(h|a1) P_a σ P_a` for `h ∈ a1`, and
  `q_a(h|a0) (𝟙 − P_a) σ (𝟙 − P_a)` for `h ∈ a0`; likewise for `c_b`.

The **identified labels** `ℒ_id` are the gate labels `c(θ)`, `θ ∈ [0, 2π)`, and the two read
labels. An **identified test** of length `m` is a protocol of `m` rounds whose labels are in
`ℒ_id`. Its labels may depend on its own records, never on the records of the preparation it
follows. `𝒯_m` is the set of identified tests of length at most `m`.

**Credited assignment.** Let `P` be an admissible preparation: a protocol prefix of length `ℓ`,
unheralded or heralded (A4). Let `w_r` be the world's weights on its prefix records `r`,
conditional on the herald if there is one. An assignment `r ↦ σ_r` of qubit states is **credited
at error `ε`** if, for every `T ∈ 𝒯_{K−ℓ}`,

> `TV( law of (r, records of T) in the world ,  Σ_r w_r δ_r ⊗ 𝔔*(σ_r · T) ) ≤ ε`,

where `𝔔*(σ · T)` is the law of `T`'s records when the target's instruments act on `σ`. The mean
credited state is `σ̄_P = Σ_r w_r σ_r`.

Whether a credited assignment exists is a property of the world's record laws and the declared
target. No freely chosen comparator enters it.

**Condition F(ε).** Every admissible preparation of length `ℓ ≤ K − 1` has an assignment credited
at error `ε`.

### A1.2 The restated conditions

These replace Q3, Q5 and Q6 of proposal section 1.4. Q0, Q1, Q2 and Q4 are unchanged. Q2 keeps
its existential qubit model `𝔔` and the distance `d_K`.

- **Q3′ (dense coherent family, on records).** F(ε) holds for the declared target, with `ℒ_id`
  containing a gate label for every `θ ∈ [0, 2π)`.
  - *Operational consequence:* after every admissible preparation and in every identified test, a
    gate round's record has the law `p(θ)` whatever was prepared, within `ε`. Its action on later
    rounds is that of the rotation by `θ` about `n̂` on the credited states.
- **Q5′ (incompatible sharp reads, Lüders, on records).** This is decision 3. F(ε) holds with the
  two read labels in `ℒ_id`. The identified tests include two consecutive reads, so the
  post-measurement state of the Lüders instrument is tested through complete sequential records,
  not only its effects.
  - *Operational consequence:* a read repeated at once reproduces its class within `ε`, and a read
    of `b` after a read of `a` has the class frequencies `Tr(P_b P_{a·})`.
  - *Supplement:* where the qubit instrument is operationally identified, a diamond-norm bound
    `‖𝓘^{(2)}_{c_a} − 𝓘*^{(2)}_{c_a}‖_⋄ ≤ ε` on the coarse-grained instrument may be stated in
    addition. It does not replace the record-level test.
- **Q6′ (the whole Bloch ball, record-certified).** Q6′ consists of (i) and (ii); A3 fixes which
  preparations count (decision 5).
  - (i) For every pure state `ψ` there is an admissible preparation `P` of length `ℓ ≤ K − 2` with
    a credited assignment whose mean state satisfies `‖σ̄_P − ψ‖_tr ≤ ε`.
  - (ii) The identified tests separate states. The read directions they reach,
    `U = {R_θ^{−1} a, R_θ^{−1} b : θ}`, span `ℝ³`, where `R_θ` is the Bloch rotation about `n̂` by
    `θ`. Equivalently: `a` or `b` is neither parallel nor perpendicular to `n̂`, or one of them is
    perpendicular and the other parallel to `n̂`.
  - The **completeness constant** `c* = ½ min_{|x|=1} max_{u ∈ U} |u·x|` is stated with the family.
    By (ii) it is positive.
  - *Operational consequence:* two qubit states at trace distance `t` have identified-test laws at
    sup-TV distance at least `c* · 2t`. Each state that (i) credits is therefore fixed by the
    records to within `ε/c*`.
  - *Why (ii) is needed.* Rotations about `n̂` acting on reads in the plane perpendicular to `n̂`
    give real quantum theory of one system, as proposal section 1.4 states. Their test laws do not
    see the third Bloch component. Without (ii), (i) could be met through a component that no
    available test fixes, which decision 1 excludes.

`PARTIAL-REBIT` (proposal section 2.1) reads: Q0–Q5′ with Q3′, without Q6′.

### A1.3 Check: C-REBIT's real-quantum-theory model is excluded

This is the check required before committing, by hand [W]. It uses no comparator model.

**Claim.** Let the world be real quantum theory of one system: every state of the disk is
preparable, and operations are real instruments. Take any declared target. If (ii) fails, Q6′
fails. If (ii) holds with constant `c*`, Q6′(i) fails at every `ε < c* / (12 c* + 6)`.

**Proof.**
1. Every admissible preparation of the world, heralded or not, leaves a real density matrix
   `ρ_P`. These form the disk `D`, an affine set of dimension 2.
2. For each identified test `T`, the world's law of `T`'s records depends only on `ρ_P`, and
   affinely. Write `W(ρ)` for the vector of these laws over `𝒯_2`.
3. Write `V(σ)` for the target's test-law vector. It is affine in the Bloch vector `r` of `σ`. By
   the gate-then-read tests and (ii), its linear part `L` satisfies `‖L x‖ ≥ c* |x|`, where `‖·‖`
   is the sup over tests of total variation.
4. Let `ψ_1, …, ψ_4` be the vertices of a regular tetrahedron inscribed in the Bloch sphere.
   Suppose Q6′(i) holds at error `ε`. It gives preparations `P_i` whose mean credited states `σ̄_i`
   have Bloch vectors within `2ε` of `ψ_i`, and `‖W(ρ_{P_i}) − V(σ̄_i)‖ ≤ ε`. (The marginal over
   prefix records of a credited joint law is within `ε`, and `V` is affine.)
5. Four points of the 2-dimensional set `D` are affinely dependent. So there is `μ ≠ 0` with
   `Σ μ_i = 0`, `Σ μ_i ρ_{P_i} = 0` and `max |μ_i| = 1`. Then `Σ μ_i W(ρ_{P_i}) = 0`, hence
   `‖L(Σ μ_i r̄_i)‖ ≤ 4ε` and `|Σ μ_i r̄_i| ≤ 4ε / c*`.
6. For the tetrahedron, the edge vectors `e_i = ψ_i − ψ_4` (`i ≤ 3`) have Gram matrix
   `(4/3)(I + J)`, whose least eigenvalue is `4/3`. Any `μ` as in step 5 has `|(μ_1, μ_2, μ_3)| ≥
   1/√3`. Hence `|Σ μ_i ψ_i| = |Σ_{i≤3} μ_i e_i| ≥ (2/√3)(1/√3) = 2/3`, and
   `|Σ μ_i r̄_i| ≥ 2/3 − 8ε`.
7. Together, `2/3 − 8ε ≤ 4ε/c*`, which is false for `ε < c*/(12 c* + 6)`. ∎

Both alternatives exclude Session 1's model `𝔔_Y`.
- *Targets that real QT itself realizes* (`n̂` normal to the disk, reads in the disk): `U` spans
  only the disk plane. So (ii) fails, and Q6′ fails at every `ε`.
- *Any target meeting (ii):* Q6′(i) fails below `c*/(12c* + 6)`.

The imaginary parts that made Q6 hold in Session 1 enter neither `W` nor any credited test law.
The argument uses only the dimension of the world's preparation set. It applies to any world whose
admissible preparations have identified-test laws in an affine family of dimension at most 2,
which is the operational sense of "a disk is not a ball".

**Positive cases.** Qubit states form an affine set of dimension 3, so the argument does not bear
on a world whose preparations realize the Bloch ball. C-POS-1, with a target meeting (ii) (its
model realizes every direction), meets (i) and (ii) at `ε = 0`. The rerun confirms this (A7).

***

## A2. Decision 2: the M0 statement

The owner's decision record states that the approval carries this sentence verbatim:

> "A `PASS-DERIVED` would be a consistency-axis result (§A.23); it would move no correctness
> assessment."

It is entered here as part of the approval record of the amended text. The Session 1 record's open
item on it (its section 1 and question 5) is answered by decision 2 of comment 6821448213.

## A3. Decision 5: preparations for Q6′, and short horizons

- A preparation counts for Q6′ only if at least two later rounds follow it: `ℓ ≤ K − 2`. Two is the
  length of the gate-then-read and read-then-read tests. A preparation of length `K − 1` or `K` is
  not a Q6′ preparation.
- Q1's preparations are unchanged: any length `ℓ ≤ K − 1` with a common continuation, read with
  Session 1's Rd-2 (the continuation's labels depend only on its own records).
- **Short horizons.** Q6′ needs a non-empty set of preparations followed by two rounds, so it is
  posed only for `K ≥ 3`.
  - For `K ≤ 2`, Q6′ is entered as "not posed". The other conditions at those `K` are reported
    with that entry.
  - A `PASS-DERIVED` requires every `K`, so Q6′ is required at every `K ≥ 3`.
  - `PARTIAL-FIXEDK` is reported only for a fixed `K ≥ 3`.
  - F(ε) (Q3′, Q5′) is posed at every `K ≥ 1`, over the identified tests that fit.

## A4. Decision 4: conditional error and acceptance

- **Definition.** The conditional error of a heralded preparation is the direct total variation
  between the world's law of the complete record conditional on the herald and the comparator's
  conditional law. The comparator is `𝔔` of Q2 for Q1, and the target with the credited assignment
  for Q3′, Q5′ and Q6′. It is taken over every protocol of `Π_K`, or every identified test, that
  extends the prefix.
- `2 d_K / p_acc ≤ ε` is kept as a sufficient bound for it, not as its definition (proposal
  section 1.2).
- **Acceptance reporting.** Each heralded preparation used in a proof of Q1, Q3′, Q5′ or Q6′
  states its acceptance probability `p_acc`, which must be positive, and its expected number of
  trials `1/p_acc`. The resource claim (Q0) states, beside `N(ε, K)` and `G(ε, K)`, the trial cost
  `R(ε, K) = max 1/p_acc` over the heralded preparations used at `I_{n(ε,K)}`, as an explicit
  function. A rare herald therefore appears as a cost and cannot produce a success without one.

## A5. Decision 6: D3 for the compiled controllers

In C-PROG and C-PROG-P, the D3 entry is "not met":
- under choice 6(i)(c) the non-uniform product law is on the list in its own right;
- the rows draw fair bits directly from the environment;
- the controller's record law is not stated under that law;
- fair bits are not assumed.

Every other entry and the token (`OPERATIONAL-ONLY` under choice 11(a)) are unchanged. The test of
D6(b) that the rows exercise is unaffected. The same rule applies wherever a control's or family's
Q-conditions rest on fair bits whose law the robustness clause does not cover.

## A6. Decision 7: controls

### A6.1 Results the amendment must preserve (§A.29)

The twelve controls that were green in Session 1 are named in advance. Each must keep the
classification Session 1 obtained, re-derived under the amended definitions. Where the amendment
changes a clause a row is stated in, the preserved form is given.

1. **C-SUP-1.** Q1, Q2, Q3′, Q4, Q5′ and Q6′ hold at the stated `(ε, K)`. Main:598's net contains
   rotations and Lüders reads, and a target meeting (ii) is declared. Q0 holds in the finite-size
   form. D1, D2, D6 and D7 fail. `OPERATIONAL-ONLY`.
2. **C-SUP-2.** D1 fails; Q4 not applicable; supplied.
3. **C-POS-1.** Q1–Q6′ at `ε = 0` on its protocol class, with a target meeting (ii). D3, D5, D6
   and D7 fail. `OPERATIONAL-ONLY`.
4. **C-POS-2.** As its row states, for menus containing a non-Clifford rotation and two rank-one
   reads with `Tr(P_a P_b) ∈ [1/4, 3/4]`. The amendment adds the requirement that the menu's
   rotations and reads meet (ii).
   - For a menu that does not meet (ii), Q6′ fails, by the argument of A1.3 applied to the
     identified tests. That is not a preserved result.
   - The narrowing is declared here, before the rerun.
   - Q4's entry depends on L3, which is re-derived under Q3′ (A8).
5. **C-ISO-1.** Q1 fails (affine dichotomy, deterministic reading); D7 fails.
6. **C-ISO-2.** Amended row, A6.3.
7. **C-FIN.** Q2 with Q3′ fails below `1/15` at the record's scope (fixed decoder); D fails. Not
   `PASS-DERIVED`.
8. **C-TAB.** Q2 only with `d = N`; Q1 and Q2 at `d = 2` fail for three pairwise distinguishable
   preparations.
9. **C-B1.** Q1 fails; D2 and D7 fail.
10. **C-CARD.** (a) Q3′ fails below `π/(2 q^{2|C|})` at fixed `L` (finite menu). (b) Well-defined on
    `ℤ^3` except the level-set law. (c) Verdicts are indexed by `K`.
11. **C-MEAS.** The one-read match holds under the uniform law and fails under `μ′` (D3 supplied).
    Q2 fails on the two-read law, and Q5′ fails with it. D4 and D7 fail.
12. **C-EXACT.** C-POS-1 at `ε = 0`; C-ISO-2 fails at every `ε` below its constant.

The proves-too-much check and the two-way check of the encoder test are rerun with these rows. Both
were green in Session 1.

### A6.2 New controls: C-REBIT and C-NULL

The two rows that exposed RC-1 are the amendment's new controls. Their expected classifications
are stated now and are not revised after the rerun.

- **C-REBIT (amended expectation).** Real quantum theory of one system, with every state of the
  disk preparable.
  - Q1, Q2, Q3′, Q4 and Q5′ hold for the target with `n̂` normal to the disk and reads in the disk.
  - Q6′ fails for every declared target: by (ii) when the target is realized by real operations,
    and by A1.3 at every `ε < c*/(12c* + 6)` otherwise.
  - This is the pattern `PARTIAL-REBIT` reports for a family in `𝕀_D`. Never `PASS-DERIVED`.
  - The proposal's proves-too-much text for C-REBIT ("its conclusion is that Q6 fails below `1/2`")
    is replaced by this statement. The properties the argument uses are: the world's preparation
    set has affine dimension 2, and its test laws are affine in the state.
- **C-NULL (amended expectation), in both modes.** Labels act on nothing in the world.
  - Expected: Q3′, Q5′ and Q6′ cannot hold together at `ε < ε_N = s/(2 + 2s)`, where
    `s = max(|a_⊥|, |b_⊥|)` (the components perpendicular to `n̂`, `s > 0` by (ii)). Not
    `PASS-DERIVED`.
  - *Sketch* [W]. After any admissible preparation of length `≤ K − 2`, the world's class
    probability of `read a` after `gate c(θ)` does not depend on `θ`. Under F(ε) the mean credited
    Bloch vector `r` therefore satisfies `|a_⊥| |r_⊥| ≤ 2ε`, and likewise for `b`, so `|r_⊥| ≤ 2ε/s`.
    Q6′(i) for a pure `ψ` perpendicular to `n̂` needs `|r_⊥| ≥ 1 − 2ε`.
  - The rerun derives this in exchange mode and in initial-condition mode separately (decision 7),
    including whether the label content of a read round's own records (exchange mode) affects the
    step "does not depend on `θ`".

### A6.3 Amended C-ISO-2 row

The C-ISO-2 row of proposal section 3 is replaced by the following.

| ID | Construction | Expected classification | Source |
|---|---|---|---|
| C-ISO-2 | As in the proposal (one lazy random walker; labels permute `C`; records are the position or a blank at each tick, with no label) | Q1, Q2, Q3′ (at `θ = 0`) and Q5′ cannot hold together at `ε < ε_D = 7 × 10^{-4}`, for every `K`, interface, `O`, `C`, `τ` and `μ`. D7 fails. Not `PASS-DERIVED`. Properties used: W1 (the whole state is read whenever it lies in `O`; labels act only on read states), W2 (laziness), W3 (start outside `O`). Depends on Rd-2, and on the conditional-error requirement for Q1's heralded preparations (A4). | Session 1 record, section 2.5 [W] |

**Marked for independent check (scope and constants).** Session 1's argument was written for the
unamended Q3 (state-independent gate records of the model `𝔔`) and for Q5 read through effects. The
rerun checks the following:
- Step A's bound (\*) under the credited form of F(ε). Under that form it reads
  `Σ_r w_r TV(L_r, p(0)) ≤ ε`, not `2.5ε`. Whether the constant holds or improves is to be
  checked, not assumed.
- Step B under Q5′, where the class probabilities are those of the credited states.
- Step C's use of preparations of length up to `K − 1`, which F(ε) covers (A1.1).
- The side conditions `ε ≤ 1/30` and `ε ≤ 10^{-3}`, and the constant `γ ≥ 0.0624`.
- That no property beyond W1–W3 is used.

## A7. Rerun

All controls are rerun under this amendment by paper derivation (decision 7):
- the twelve rows of A6.1, each against its preserved classification;
- C-REBIT and C-NULL against A6.2, C-NULL in exchange mode and in initial-condition mode;
- C-REP, with its first clause replaced by: "Every Q-condition is a property of the record laws
  and the declared target. Q2 is existential over qubit models. For Q3′, Q5′ and Q6′, a credited
  assignment's existence is fixed by the records, and Q6′ in addition requires identified tests
  that separate states. Padding cannot move `d_K`. Not `PASS-DERIVED`.";
- C-PROG and C-PROG-P, with A5's D3 entry.

The stop rule of the proposal (sections 3, 4 M1, 7) applies unchanged. A red row voids the rerun
and returns the definitions to the owner. A definition is not adjusted after a rerun to make a row
green (§A.29).

## A8. Consequences elsewhere in the proposal

- **L3 (proposal M2).** "Q2 and Q3 imply Q4 with error `4ε`" used the unamended Q3 on `𝔔`. It is to
  be re-derived under Q3′ at M2, or Q4 proved directly. The error budget of a pass (proposal
  section 3, invariant table) applies once L3 is re-established.
- **L2.** It uses Q2 only and is unaffected.
- **M3's sketch, step 4.** It uses states near `|a+⟩`, `|b+⟩` of Q5. Under the amendment these are
  credited states of Q6′ preparations.
- **Condition and control tables.** Their schema (proposal section 2.2) is unchanged. Rows Q3, Q5
  and Q6 are entered as Q3′, Q5′ and Q6′.

## A9. Decision 8: gate

L5/M3 (the R-lin node), its child nodes, the re-derivations of MECH-1 Lemma A and MECH-2 Lemma F
(choice 9(a)), and the R-nl branch do not start until the amended controls have been rerun (A7) and
that rerun has passed independent review. Before the rerun, this amendment itself goes to
independent review.

***

## A10. Disclosure

- **Commands:** `git` (rev-parse, status, fetch, add, commit, push), `curl` (one GET of comment
  6821448213 from the GitHub API, as the coordinator instructed), `grep`, `sed`, `wc`, `sha256sum`.
  No interpreter was run. The arithmetic of A1.3 and A6.2 was done by hand.
- **Read:** comment 6821448213 (in full); the proposal and the Session 1 record (as in session 1).
- **Not done:** any control rerun; any work after M1.
