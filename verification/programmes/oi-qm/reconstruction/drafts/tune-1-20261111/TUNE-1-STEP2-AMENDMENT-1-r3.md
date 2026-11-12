# TUNE-1, Step 2: amendment 1, revision r3

**WIP / UNVERIFIED draft amendment, for independent review.** This is the third draft of
amendment 1. It replaces r2 (`TUNE-1-STEP2-AMENDMENT-1-r2.md` at `39a61e9e`), and r1
(`TUNE-1-STEP2-AMENDMENT-1.md` at `9bba40d3`) before it. Both are left unchanged as reviewed
objects. r3 applies the re-review of r2 (verdict ACCEPT WITH CHANGES, items S1–S4), as set out in
section B0. Apart from those changes, r3 is r2.

It implements the owner's decisions 1–8, recorded at PR #1237 comment 6821448213: `amaybaum`,
2026-11-12T10:44:37Z, author association `OWNER`, posted through the `claude` GitHub app, "Adopt as
proposed (Recommended)". That decision "authorizes paper-only definition repair and review only.
It authorizes no computation and adopts no premise." This file reruns no control, adopts no premise
and changes no manuscript or Lean file. It does not narrow any preserved control: where a principled
definition cannot preserve one, an owner question is raised (section B8).

**Amends** `TUNE-1-STEP2-PROPOSAL.md` at `e676c42a`, sha256
`2a081101efae469b39b747ef8f3641f259e55892705bc0f7759adf3ac7499fd5`. That file is not edited.
Where this amendment and the proposal differ, the amendment governs. Everything not amended stands.
The findings it implements are those of `TUNE-1-STEP2-SESSION1.md` at `498ec02f` (RC-1, RC-2,
Rd-1 to Rd-8).

**Conventions.** Trace distance is `‖σ − σ′‖_tr = ½‖σ − σ′‖₁`. For qubit states it equals half the
Euclidean distance of the Bloch vectors. `TV` is total variation, half the `ℓ¹` distance. Labels
[K], [P], [R] and [W] are as in the proposal. Every argument below is [W], unreviewed.

***

## B0. Plain summary and changes from r1

**Summary.** Session 1 found that the "whole Bloch ball" test, and the gate and read tests with it,
were checked on a freely chosen quantum model of the records. The owner decided to restate those
tests on what the observer can actually record. This draft states them on the observer's records:
- gates and reads are tested by sequences of rounds after each preparation;
- reads must behave like ideal repeatable measurements;
- the Bloch-ball test counts only states that the family's declared operations can tell apart, with
  a separating strength that does not shrink as the apparatus grows.

A hand argument shows that a world obeying real quantum theory then fails the Bloch-ball test,
while a genuine qubit can pass it. Three preserved controls are affected:
- one positive control cannot keep part of its scope under any definition that follows the owner's
  principle;
- two others change their constants.

These points go to the owner as questions, and are not settled here. Composition (Q4) is not
obtained from a general lemma, since none is available under the amended gate test; it is proved
row by row at the rerun.

**Changes from r2.** Every item of the re-review was checked by hand before being applied.

| Re-review item | Check | Applied in r3 |
|---|---|---|
| S1: declared labels must be unitary gates or Lüders reads, so a qubit whose third component is measured only unsharply fails | Confirmed. Take `z`-rotations, Lüders `X` and `Y`, and an unsharp `Z` with effects `(𝟙 ± ηZ)/2`: no declarable test reaches `z`. B1.4's exclusion uses only that the world's test laws are affine on a 2-dimensional state set, together with the target's lower bound `c₀`, so it holds for any fixed target instrument | B1.1: a declared label may carry any fixed target qubit instrument. Its separation contribution enters `c*_n` through the linear part of its test laws (B1.3 (ii)). With the unsharp `Z`, the test reaches `z` with strength `η/2`, and `c₀ > 0` for fixed `η`. Real QT stays excluded (B1.4). |
| S2: `𝒯_0` is the empty family, but B1.3 and the C-ISO-2 row use it for the gate `c(0)` | Confirmed | `𝒯_{θ=0}` in B1.3 and B6.3 |
| S3: the reason given for a uniform `c₀` overstates; it should read "every `n` in the range of `n(ε, K)`" | Confirmed. `ε/c*_{n(ε,K)} → 0` also excludes real QT, because B1.4 bites once `ε < c*/12` | B1.3 (ii): the condition is restricted to the members the family uses, and the uniform `c₀` is stated as a principled, checkable sufficient form, not a necessary one |
| S4: Q1 is strengthened without saying so | Confirmed. A heralded Q1 witness must carry target credit | B1.3: recorded as a change to Q1, with credit on `𝒯_K`. B1.2 names `𝒯_K`. |

C-POS-2's narrowing stays an owner question (B8.1) and is not applied.

**Changes from r1 to r2.** Every point of the review of r1 was checked by hand before being
applied.

| Review point | Check | Applied in r2 |
|---|---|---|
| R1 (blocker): the target may vary with `n`, so `c*_n → 0` lets real QT pass | Confirmed: with `n̂ = y`, `a = x cos α + y sin α`, `b = z`, `c* = ½ sin α`, and real QT meets every condition at `ε ≈ ½ sin α + O(Kα²)` | B1.3 (ii): `c*_n ≥ c₀ > 0` for every `n`, with `c₀` stated by the family. B1.4 re-derives the exclusion uniformly. |
| R2: separation by gates then reads only fails an exact qubit whose third component is reached by another label | Confirmed: `z`-rotations, reads `X` and `Y`, and a Hadamard. Then `Z = HXH` is available but not counted | B1.1: the target may declare further gates and reads. B1.3 (ii): separating tests of length up to `L` declared by the family. |
| R3: "admissible" is undefined | Confirmed | B1.2 defines admissibility and the scope of `F` |
| R4: preserved constants of C-POS-2 and C-CARD (a) change under Q3′; C-SUP-1 to be checked | Confirmed for C-POS-2 (`K`-dependent floor) and for C-CARD (a) (new constant). C-SUP-1 is unaffected (`Kδ = ε/2`) | B6.1; owner questions B8.2–B8.3 |
| R5: Q3′ and Q5′ coincide | Confirmed | B1.3: `F(ε; 𝒯′)` with named sub-families; rows cite them |
| R6: L3 is needed by the rerun and may fail under Q3′ | Confirmed: Q4's continuation uses labels that `F` does not constrain | B7: L3 is not used; Q4 is proved directly per row at the rerun, as a gate |
| Minor | — | Trace-norm convention (above); `ε_N ≥ 1/6` (B6.2); "is to be confirmed" (B1.4); C-REP's change recorded as a change to a control (B6.4) |

***

## B1. Decision 1: Q3, Q5 and Q6 on record laws

### B1.1 Declared target and identified tests

A family declares, as part of its specification (D1: a function of `n` alone), a **target** `𝔔*`.
It consists of:
- a rotation axis `n̂` and, for each `θ ∈ [0, 2π)`, a gate label `c(θ)`, with target instrument
  `𝓘*_{c(θ),h} = p_h(θ) · Ad(e^{−iθ n̂·σ/2})`;
- two read labels `c_a, c_b`, with unit Bloch vectors satisfying `a·b ∈ [−1/2, 1/2]`. Each has a
  two-class split of its records and fixed conditional record laws, with Lüders target instrument
  `𝓘*_{c_a,h}(σ) = q_a(h|a1) P_a σ P_a` for `h ∈ a1` and
  `q_a(h|a0) (𝟙 − P_a) σ (𝟙 − P_a)` for `h ∈ a0`, likewise for `c_b`;
- optionally, finitely many further declared labels. Each carries a fixed target qubit instrument
  `{𝓘*_{g,h}}_h`, stated in full: a unitary gate `p_h(g) · Ad(V_g)`, a Lüders read along a stated
  direction, an unsharp read whose effects are not projections, or any other fixed instrument. Its
  contribution to separation is stated through the linear part of its test laws (B1.3 (ii)). For
  example, a read with effects `(𝟙 ± η m·σ)/2` contributes `(η/2)|m·x|`.

The **identified labels** `ℒ_id` are all of these. An **identified test** is a protocol whose
labels are in `ℒ_id`. Its labels may depend on its own records, never on the records of the
preparation it follows.

Named sub-families:
- `𝒯_m`: every identified test of length at most `m`;
- `𝒯_R`: tests using only the two read labels `c_a, c_b`;
- `𝒯_θ`: the single round `c(θ)`. For example, `𝒯_{θ=0}` is the single round `c(0)`.

`𝔔*(σ · T)` is the law of `T`'s records when the target instruments act on `σ`.

The declared labels are the family's own operations, each tested by `F` below against its stated
target. Decision 1 credits components fixed by "available preparation, measurement or
continuation". Declaring a label makes it available as a test, with its behaviour checked, and
leaves nothing untested.

### B1.2 Admissible preparations and credited assignments

- An **unheralded preparation** is any prefix of a protocol of `Π_K`.
- A **heralded preparation** is such a prefix with an event of positive probability on its records.
- A heralded preparation is **admissible** for a given proof if the proof uses it to witness Q1 or
  Q6′(i), it carries an assignment credited at conditional error `ε` on `𝒯_K` (below), and its `p_acc` and
  trial cost `1/p_acc` are reported (B4). No other heralded preparation is quantified over.
- An unheralded preparation is always admissible.
- An unheralded extension of an admissible heralded preparation, by further rounds with no further
  herald, is admissible with the same herald.

**Credited assignment.** Let `P` be an admissible preparation of length `ℓ` with world weights `w_r`
on its prefix records, conditional on the herald if there is one. An assignment `r ↦ σ_r` of qubit
states is **credited at error `ε` on `𝒯′`** if, for every `T ∈ 𝒯′` with `ℓ + |T| ≤ K`, the direct
total variation between the following two laws is at most `ε`:
- the world's law of `(r, records of T)`, conditional on the herald;
- `Σ_r w_r δ_r ⊗ 𝔔*(σ_r · T)`.

The mean is `σ̄_P = Σ_r w_r σ_r`.

**Condition `F(ε; 𝒯′)`.** Every admissible preparation of length `ℓ ≤ K − 1` has an assignment
credited at error `ε` on `𝒯′`.

Universality runs over the unheralded preparations and their admissible extensions. Rare heralds
enter only when a proof uses them, and then with their conditional error and their cost stated.
`F(ε; 𝒯′)` is a property of the world's record laws and the declared target. No freely chosen model
enters it.

### B1.3 The restated conditions

These replace Q3, Q5 and Q6 of proposal section 1.4, and change Q1 as follows. Q0, Q2 and Q4 are
unchanged, and Q2 keeps its existential qubit model and `d_K`.

- **Q1 (changed).** Q1's statement is kept. A heralded preparation may witness Q1 only if it is
  admissible (B1.2): its conditional error is at most `ε` against the model `𝔔` of Q2 (B4), and
  it carries an assignment credited at conditional error `ε` on `𝒯_K` against the declared target.
  Q1 therefore depends on the declared target through its heralded witnesses. Unheralded witnesses
  are as before. The C-ISO-2 argument uses this credit (B6.3).

- **Q5′ (incompatible sharp reads, Lüders).** `F(ε; 𝒯_R)` holds for the declared target. This is
  decision 3.
  - *Operational consequence:* tests of two reads check the post-measurement state through
    complete sequential records. An immediately repeated read reproduces its class within `ε`, and
    `b` after `a` has class frequencies `Tr(P_b P_{a·})`.
  - *Supplement:* where the qubit instrument is operationally identified, a diamond-norm bound on
    the coarse-grained read instrument may be stated in addition. It does not replace the record
    test.
- **Q3′ (dense coherent family).** `F(ε; 𝒯_K)` holds: every identified test, gates included.
  - *Operational consequence:* after every admissible preparation, a gate round's record has the
    law `p(θ)` whatever was prepared, within `ε`. Its effect on later identified rounds is that of
    the rotation by `θ` about `n̂` on the credited states, over tests of up to `K − ℓ` rounds.
    Errors of repeated gates therefore accumulate within the bound.
  - Q3′ contains Q5′. A row that uses only part of it names the sub-family (for example
    `F(ε; 𝒯_{θ=0})`).
- **Q6′ (the whole Bloch ball, record-certified).** Q6′ consists of (i) and (ii).
  - (i) For every pure `ψ` there is an admissible preparation `P` of length `ℓ ≤ K − L` with an
    assignment credited at error `ε` on `𝒯_L`, whose mean satisfies `‖σ̄_P − ψ‖_tr ≤ ε`.
  - (ii) Separation, uniform in `n`. Let `V_n` be the target's map from Bloch vectors to laws of
    the tests in `𝒯_L`, with linear part `Λ_n`. Its **separation constant** is
    `c*_n = min_{|x|=1} sup_{T ∈ 𝒯_L} TV-norm(Λ_n x)`. The family states a separation length
    `L ≥ 2` and a constant `c₀ > 0`, both independent of `n`, and `c*_n ≥ c₀` for every `n` in
    the range of `n(ε, K)`.
  - In general `c*_n > 0` exactly when the target's test map on `𝒯_L` is injective on Bloch
    vectors.
    - A gate (declared or `c(θ)`) followed by a Lüders read along `u` gives `Λ x` a class
      component `½ (R_g^{−1} u)·x`, where `R_g` is the gate's Bloch rotation.
    - A declared read with effects `(𝟙 ± η m·σ)/2` gives `½ η (m·x)`.
    - Tests of these kinds give `c*_n > 0` exactly when the directions they reach, each weighted by
      its strength, span `ℝ³`.
  - *Operational consequence:* two qubit states at Bloch distance `|x|` have test laws at least
    `c₀|x|` apart. A credited mean state is fixed by the records to Bloch distance `2ε/c₀`, which
    tends to 0 with `ε`.
  - *Reason for the uniform form.* Decision 1 requires that the available tests fix a credited
    component. With separation `c*`, a credited mean state is fixed to Bloch distance `2ε/c*`.
    - Decision 1 therefore requires at least that `ε / c*_{n(ε,K)} → 0` as `ε → 0`.
    - Without some such condition, review R1 shows that real QT passes through targets tilted by
      `α_n → 0`.
    - That weaker condition already excludes real QT: B1.4's argument bites once `ε < c*/12`, since
      `c*/(12c* + 6) ≥ c*/12` for `c* ≤ ½`.
    - The uniform bound `c*_n ≥ c₀` is a principled choice that is simpler and can be checked at
      each member the family uses. It is sufficient for decision 1, not necessary.
    - It contains no number fitted to a control: `c₀` is the family's own constant.
    - Admitting the weaker condition instead would be an owner decision. It would not change any
      expected classification in B6, since B1.4 and the C-NULL bound (`ε_N ≥ 1/6`) hold under it.

### B1.4 Check: real quantum theory fails Q6′, and a genuine qubit can meet it

**Claim (exclusion).** Let the world be real quantum theory of one system: every state of the
disk is preparable, and operations are real instruments. For any declared target meeting (ii) with
constant `c₀`, Q6′(i) fails at every `ε < c₀/(12 c₀ + 6)`. This holds uniformly in `n`, so no family
with a rebit record theory has Q6′ at all `ε`.

**Proof.**
1. Each admissible preparation leaves a real state `ρ_P` in the disk `D`, an affine set of
   dimension 2.
2. The world's test laws on `𝒯_L` depend affinely on `ρ_P`: `W(ρ)`.
3. The target's laws are `V(σ)`, with `‖Λ x‖ ≥ c₀ |x|` by (ii).
4. Take `ψ_1, …, ψ_4`, the vertices of a regular tetrahedron in the Bloch sphere. Q6′(i) gives
   `P_i` with `|r̄_i − ψ_i| ≤ 2ε` (Bloch) and `‖W(ρ_{P_i}) − V(σ̄_i)‖ ≤ ε`.
5. Four points of `D` are affinely dependent. So there is `μ ≠ 0` with `Σ μ_i = 0`,
   `Σ μ_i ρ_{P_i} = 0` and `max|μ_i| = 1`, and then `‖Λ(Σ μ_i r̄_i)‖ ≤ 4ε`, so
   `|Σ μ_i r̄_i| ≤ 4ε/c₀`.
6. The tetrahedron's edge vectors from `ψ_4` have Gram matrix `(4/3)(I + J)`, with least
   eigenvalue `4/3`, and `|(μ_1, μ_2, μ_3)| ≥ 1/√3`. So `|Σ μ_i ψ_i| ≥ 2/3` and
   `|Σ μ_i r̄_i| ≥ 2/3 − 8ε`.
7. Hence `2/3 − 8ε ≤ 4ε/c₀`, which is false for `ε < c₀/(12c₀ + 6)`. ∎

The independent review checked steps 1–7 for r1. r2 changes only the constant from `c*` to `c₀`.
r3 lets a declared label carry any fixed target instrument (B1.1); the proof is unchanged by this.
- Step 2 uses only that the world's laws for each test are affine in the world's state. This holds
  for every operation of real QT, whatever target it is declared against.
- Step 3 uses only the lower bound on the target's linear part, whatever instruments define it.
- Which instrument a declared label carries enters neither step.

**Review R1's attack is excluded.** The tilted targets have `c*_n = ½ sin α_n → 0`. This violates
(ii), so Q6′ fails for that family by definition. A family with fixed tilt `α` meets (ii) with
`c₀ = ½ sin α`, and Q6′(i) then fails below `c₀/(12c₀+6)`.

**Genuine qubits.**
- An exact qubit world can declare `n̂ = z`, `a = (x + z)/√2`, `b = (x − z)/√2` (`a·b = 0`), with
  `L = 2`. For a unit `x = (sin φ cos χ, sin φ sin χ, cos φ)`, the gate-then-read directions reach
  `|u·x|` up to `(|sin φ| + |cos φ|)/√2 ≥ 1/√2`. So `c₀ = 1/(2√2)` for every `n`. With every pure
  state preparable and exact instruments, Q6′ holds at `ε = 0`.
- Review R2's world (`z`-rotations, reads `X` and `Y`, a Hadamard) declares the Hadamard as a
  further gate. "Hadamard then read `X`" reaches `z`, so (ii) holds with a positive constant.
- The re-review's world (`z`-rotations, Lüders `X` and `Y`, and an unsharp `Z` read with effects
  `(𝟙 ± ηZ)/2` for a fixed `η > 0`) declares the unsharp read (B1.1) [W].
  - A unit `x = (x_1, x_2, x_3)` meets the gate-then-read tests with strength
    `½ (x_1² + x_2²)^{1/2}` (rotating the `X` direction about `z`), and the unsharp read with
    strength `½ η |x_3|`.
  - So `c* ≥ ½ min_{|x|=1} max((x_1² + x_2²)^{1/2}, η|x_3|) = ½ η/(1 + η²)^{1/2} > 0`, constant in
    `n`, and (ii) holds.
  - With every pure state preparable and exact instruments, Q6′ holds at `ε = 0`.
- C-POS-1 (all rotations and directions) meets (i) and (ii) at `ε = 0` with the first target above.
  This is to be confirmed at the rerun.

***

## B2. Decision 2: the M0 statement

The owner's decision record states that the approval carries this sentence verbatim:

> "A `PASS-DERIVED` would be a consistency-axis result (§A.23); it would move no correctness
> assessment."

It is entered as part of the approval record of the amended text. It answers the Session 1
record's open item (section 1, question 5).

## B3. Decision 5: preparations for Q6′, and short horizons

- A preparation counts for Q6′ only if at least `L ≥ 2` later rounds follow it: `ℓ ≤ K − L`. Two
  rounds suffice for gate-then-read and read-then-read tests. A family whose separation needs
  longer tests states that larger `L` (B1.3 (ii)).
- Q1's preparations keep their length (`ℓ ≤ K − 1`, with Session 1's Rd-2 for the continuation).
  Its heralded witnesses need target credit (B1.3, Q1 changed).
- **Short horizons.** Q6′ is posed only for `K ≥ L + 1`.
  - For smaller `K`, Q6′ is entered as "not posed", and the other conditions are reported with
    that entry.
  - A `PASS-DERIVED` requires every `K`, so Q6′ is required at every `K ≥ L + 1`.
  - `PARTIAL-FIXEDK` is reported only for a fixed `K ≥ L + 1`.
  - `F` is posed at every `K ≥ 1`, over the tests that fit.

## B4. Decision 4: conditional error and acceptance

- **Definition.** The conditional error of a heralded preparation is the direct total variation
  between the world's law of the complete record conditional on the herald and the comparator's
  conditional law. The comparator is `𝔔` of Q2 for Q1, and the target with the credited assignment
  for `F` and Q6′. It is taken over every protocol of `Π_K`, or every identified test, that extends
  the prefix.
- `2 d_K / p_acc ≤ ε` is a sufficient bound for it, not its definition.
- **Acceptance reporting.** Each admissible heralded preparation states its `p_acc > 0` and its
  expected trial count `1/p_acc`. The resource claim (Q0) states, beside `N(ε, K)` and `G(ε, K)`,
  the trial cost `R(ε, K) = max 1/p_acc` over the heralded preparations used at `I_{n(ε,K)}`, as an
  explicit function. A rare herald appears as a cost and cannot produce a success without one.

## B5. Decision 6: D3 for the compiled controllers

In C-PROG and C-PROG-P, the D3 entry is "not met":
- under choice 6(i)(c) the non-uniform product law is on the list in its own right;
- the rows draw fair bits directly from the environment;
- the controller's record law is not stated under that law;
- fair bits are not assumed.

Every other entry and the token (`OPERATIONAL-ONLY` under choice 11(a)) are unchanged. The same
rule applies wherever Q-conditions rest on fair bits whose law the robustness clause does not cover.

## B6. Decision 7: controls

### B6.1 Results the amendment must preserve (§A.29)

The twelve controls green in Session 1 are named in advance, with the classification each must
keep under the amended definitions. Where a constant or form changes, the change is stated and
goes to the owner (B8). No scope is narrowed here.

1. **C-SUP-1.** Q1, Q2, Q3′, Q5′ and Q6′ hold at the stated `(ε, K)`. Q4 is proved directly (B7).
   D1, D2, D6 and D7 fail. `OPERATIONAL-ONLY`.
   - *Check (R4).* Main:598's net has `δ = ε/(2K)`. A gate used up to `K` times in a test contributes
     at most `Kδ = ε/2` in diamond norm (Main:596 telescoping [P]), so `F` holds within the stated
     `ε`.
   - The net contains Lüders reads and every rotation, so the target of B1.4 is available
     (`c₀ = 1/(2√2)`).
   - The constant is unchanged.
2. **C-SUP-2.** D1 fails; Q4 not applicable; supplied.
3. **C-POS-1.** Q1–Q6′ at `ε = 0` on its protocol class, with the target of B1.4. D3, D5, D6 and D7
   fail. `OPERATIONAL-ONLY`.
4. **C-POS-2.** Preserved as its row states, for every menu the row admits. Two consequences of the
   amended definitions bear on it; neither is applied here, and both are owner questions.
   - (a) Menus whose operations do not separate states fail Q6′. Example: every menu rotation about
     one axis and both reads perpendicular to it. B8.1.
   - (b) Q3′ holds at a `K`-dependent floor `ε ≥ b + K g`, where `g` is the largest gap between a
     requested angle and the nearest menu angle about `n̂`. A test may repeat a gate up to `K`
     times, and each use contributes at most its diamond distance `g` to the total variation (Main:596 [P]). The row's floor is
     `ε ≥ b + δ`. B8.2.
5. **C-ISO-1.** Q1 fails (affine dichotomy, deterministic reading); D7 fails.
6. **C-ISO-2.** Amended row, B6.3.
7. **C-FIN.** Q2 with Q3′ fails below `1/15` at the record's scope (fixed decoder); D fails. Not
   `PASS-DERIVED`.
8. **C-TAB.** Q2 only with `d = N`; Q1 and Q2 at `d = 2` fail for three pairwise distinguishable
   preparations.
9. **C-B1.** Q1 fails; D2 and D7 fail.
10. **C-CARD.** Preserved in the proposal's form.
    - (a) For fixed `L`, there is `ε₀(L) > 0` below which Q3′ and Q6′ cannot both hold. Session 1's
      constant `π/(2q^{2|C|})` was derived for the unamended Q3; the re-derived constant is below,
      and the change goes to the owner as B8.3.
    - (b) Well-defined on `ℤ^3` except the level-set law.
    - (c) Verdicts are indexed by `K`.

    *Re-derived constant for (a)* [W].
    - The menu has `M ≤ q^{2|C|}` labels. Among the `M + 1` angles `2πk/(M+1)`, two, `θ` and `θ′`,
      share a label, with `|θ − θ′| ≥ 2π/(M+1)`. The world's laws of "`c(θ)` then read `u`" and
      "`c(θ′)` then read `u`" are then equal.
    - Take `u ∈ {a, b}` with `|u_⊥| ≥ ½`. This exists because `|a·b| ≤ ½` forces
      `max(|a_⊥|, |b_⊥|) ≥ ½`.
    - Credited states must satisfy `|(R_θ^{−1}u − R_{θ′}^{−1}u)·r| ≤ 4ε`.
    - Q6′(i) supplies `r` within `2ε` of the pure state that maximizes the left side, where it
      equals `2|u_⊥| sin(|θ − θ′|/2) ≥ sin(π/(M+1))`.
    - So `sin(π/(M+1)) − 4ε ≤ 4ε`, giving `ε₀(L) = sin(π/(M+1))/8`.
11. **C-MEAS.** The one-read match holds under the uniform law and fails under `μ′` (D3 supplied).
    Q2 fails on the two-read law, and Q5′, `F(ε; 𝒯_R)`, fails on the same two-read test. D4 and D7
    fail.
12. **C-EXACT.** C-POS-1 at `ε = 0`; C-ISO-2 fails at every `ε` below its constant.

The proves-too-much check and the two-way check of the encoder test are rerun with these rows.

### B6.2 New controls: C-REBIT and C-NULL

Their expected classifications are stated now and are not revised after the rerun.

- **C-REBIT.** Real quantum theory of one system, every disk state preparable.
  - Q1, Q2, Q4 and Q5′ hold for a target with reads in the disk. Q3′ holds for `n̂` normal to the
    disk.
  - Q6′ fails for every declared target: by (ii) when no declared test reaches outside the disk
    plane, and otherwise at every `ε < c₀/(12c₀ + 6)` (B1.4).
  - This is the `PARTIAL-REBIT` pattern. Never `PASS-DERIVED`.
  - The proposal's proves-too-much text for C-REBIT ("Q6 fails below `1/2`") is replaced by this.
    The properties the argument uses are: the preparation set has affine dimension 2, and the test
    laws are affine in the state.
- **C-NULL, in both modes.** Labels act on nothing in the world.
  - Expected: `F(ε; 𝒯_2)` and Q6′ cannot hold together at `ε < ε_N = s/(2 + 2s)`, where
    `s = max(|a_⊥|, |b_⊥|) ≥ ½`. So `ε_N ≥ 1/6` for every target. Not `PASS-DERIVED`.
  - *Sketch* [W]. After any admissible preparation of length `≤ K − 2`, the world's class
    probability of "read `a` after `c(θ)`" does not depend on `θ`. So the credited mean satisfies
    `|a_⊥||r_⊥| ≤ 2ε`, and likewise for `b`, giving `|r_⊥| ≤ 2ε/s`. Q6′(i) for a pure `ψ`
    perpendicular to `n̂` needs `|r_⊥| ≥ 1 − 2ε`.
  - The rerun derives this separately in exchange mode and in initial-condition mode. In exchange
    mode it also checks whether the label content in a read round's own records affects the step
    "does not depend on `θ`".

### B6.3 Amended C-ISO-2 row

| ID | Construction | Expected classification | Source |
|---|---|---|---|
| C-ISO-2 | As in the proposal (one lazy random walker; labels permute `C`; records are the position or a blank at each tick, with no label) | Q1, Q2, `F(ε; 𝒯_{θ=0})` (the gate `c(0)` alone) and `F(ε; 𝒯_R)` with `a·b ∈ [−½, ½]` cannot hold together at `ε < ε_D = 7 × 10^{-4}`, for every `K`, interface, `O`, `C`, `τ` and `μ`. D7 fails. Not `PASS-DERIVED`. Properties used: W1 (the whole state is read whenever it lies in `O`; labels act only on read states), W2 (laziness), W3 (start outside `O`). Depends on Rd-2, and on B1.2's admissibility of the heralded preparations a Q1 proof uses. | Session 1 record, section 2.5 [W] |

**Marked for independent check (scope and constants).**
- Step A under the credited form of `F(ε; 𝒯_{θ=0})`, which gives `Σ_r w_r TV(L_r, p(0)) ≤ ε` directly.
- Step B under `F(ε; 𝒯_R)`, the first read after the empty preparation.
- Step C's hybrid over "`P_i` followed by `j − 1` rounds", which B1.2 admits as unheralded
  extensions of admissible preparations, of length `≤ K − 1`.
- The side conditions `ε ≤ 1/30` and `ε ≤ 10^{-3}`, and `γ ≥ 0.0624`.
- That no property beyond W1–W3 is used.

Whether the constant holds or improves is to be checked, not assumed.

### B6.4 Other rows

- **C-PROG and C-PROG-P:** D3 per B5.
- **C-REP: changed control.** Its first clause is replaced by: "Every Q-condition is a property of
  the record laws and the declared target. Q2 is existential over qubit models. For Q3′, Q5′ and
  Q6′, a credited assignment's existence is fixed by the records. Q6′ also requires separating
  identified tests with a uniform constant. Padding cannot move `d_K`. Not `PASS-DERIVED`."
  This is recorded as a change to a control.

## B7. Q4 and L3 (gate for the rerun)

L3 ("Q2 and Q3 imply Q4 with error `4ε`") used Q3 on the model `𝔔`'s channels. Under Q3′ that step
is not available: `F` constrains identified tests only, while Q4's continuation may use any labels.
A general L3′ (Q2, Q3′ and Q6′ imply Q4) is open and may be false. It is not used.

- **Gate.** Every row that asserts Q4 proves it directly at the rerun. These are C-SUP-1, C-POS-1
  and C-POS-2, and any candidate family.
  - For a control whose construction supplies a fixed quantum comparison, L3's argument may be
    applied to that supplied model. Such controls are Main:598's net model and C-POS-2's exact
    menu model, each within its record's bound.
  - The supplied model is part of the construction, not chosen for the condition.
- A row whose Q4 cannot be proved this way is red at the rerun.
- The error budget of a pass (proposal section 3, invariant table) is restated with Q4 proved
  directly.

## B8. Owner questions raised by r2

1. **C-POS-2 at menus whose operations do not separate states** (B6.1 item 4(a)).
   - At such menus no declared operation, alone or composed, detects one Bloch component. An
     example is a menu whose rotations share one axis, with reads perpendicular to it. Q6 held there
     under the unamended definitions only through components that no record fixes (RC-1).
   - No definition that follows decision 1 credits those components, so C-POS-2 cannot be preserved
     there unnarrowed.
   - Options:
     - (a) approve narrowing C-POS-2's preserved scope to menus whose declared operations separate
       states (B1.3 (ii)), as a consequence of decision 1;
     - (b) keep the scope, in which case the rerun finds C-POS-2 red at those menus and the
       definitions return to the owner;
     - (c) another resolution.
2. **C-POS-2's Q3′ floor** (B6.1 item 4(b)). Options: (a) accept `ε ≥ b + K g`, which depends on
   `K`, as the preserved form; (b) keep `b + δ`, which the amended Q3′ does not give.
3. **C-CARD (a)'s constant** (B6.1 item 10). Options: (a) accept `ε₀(L) = sin(π/(M+1))/8`,
   `M ≤ q^{2|C|}`, keeping the row's statement that an `ε₀(L) > 0` exists; (b) other.

## B9. Gate (decision 8)

L5/M3, its child nodes, the re-derivations of MECH-1 Lemma A and MECH-2 Lemma F (choice 9(a)), and
the R-nl branch do not start until all of the following hold:
- this amendment has been reviewed;
- the owner has answered B8;
- the amended controls have been rerun (B6, with B7's direct Q4 proofs);
- that rerun has passed independent review.

## B10. Disclosure

- **Commands:** `git` (rev-parse, status, add, commit, push), `cat`, `cp`, `grep`, `sed`, `head`, `wc`,
  `sha256sum`. No interpreter was run. All arithmetic was done by hand.
- **Read:** the review of r1 and its r2 section (in full), r1, r2, comment 6821448213 (read for r1), and the proposal.
- **Not done:** any control rerun; any work after M1.
