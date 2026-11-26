# OI-QM-APPROX-1, unit 3 (O2): approximate structure rules

Plan, fixed before any bound is written. Status of every question at this commit: **open**.

- **Accountable home:** #1216 (OI-QM-APPROX-1). Parent programme #1169. Open node O2 of unit 2
  (`../unit2/REPORT-r3.md` §8: "Approximate structure rules (readout, feed-forward,
  preparations)", open) and assumption-watch marker W2 (§7 there: the exact Lüders readout and
  exact feed-forward are inputs of Theorem 3 outside the five conditions; the exact trace
  preservation of the coarse-grained readout is an input of Lemma 7's padding).
- **Authorization.** Owner decision at #1169 comment 7189139613 (posted from the account
  `amaybaum` 2026-11-26T10:16:17Z, quoting the owner's decision received 2026-11-26T10:16Z),
  item 2, lane 2: "Approximate composition (#1216) — Determine whether the stability results
  survive approximate preparation, readout and feed-forward." Acceptance criterion, lane 2:
  "Obtain an explicit stability bound, a counterexample or a precisely identified obstruction.
  Preserve the distinction between the history and correspondence metrics." The same decision
  states: "Use separate writers and independent reviewers", and, in item 3, "Do not authorize
  computation or adopt additional premises through the new research units."
- **Writer:** `writer-approx-comp` (Claude Code agent), designated writer of unit B in the same
  comment. Record directory `verification/programmes/oi-qm/approximation/unit3/`, branch
  `research/i1216-approx-composition-20261126`. Independent non-author review follows the report
  (§10); no acceptance is claimed here.
- **Pinned source.** `main` = `353a066f18766837fed8c7f58507e09ff549b1a4`
  (2026-11-26 11:55:50 +0200). "Main" = `papers/Main.md` at that commit (SHA-256 prefix
  `1b8310e921bd6ece`); "OB/" = `verification/lean-mathlib/OIBridge/`, unchanged between unit 2's
  pin `b6c6b80b` and this pin. Main's four changed lines between the two pins (692, 716, 720,
  724) lie outside the passages used here. All `path:line` citations are at the pinned commit.
- **Goal link (§A.47).** Serves #1216 (Foundational). The unit decides whether unit 2's stability
  results (the Direction 1 bound, Theorem 4; the converse under M_C, Lemma 7 and Theorem 8) keep
  a bound that tends to 0 when the six structure rules of Main:572 hold only to a stated accuracy
  η, under M_H and under M_C separately. It closes or sharpens O2 and W2. It does not decide
  whether OI or any finite mechanism supplies the structure rules or the δ-conditions (unit 2
  O5), and it does not bear on the derivation of the complex matrix kinematics (O6, W3).

## 1. Setting (inherited, unchanged)

The following are unit 2's, fixed in `../unit2/PLAN.md` (commit `d2fd361e`) and used here
unchanged:
- the carrier A with |A| = d;
- the levels n ≥ 1 with N = d·n, and the system;
- the complex matrix kinematics, taken as given (Main:572, W3);
- the history class: adaptive protocols of horizon exactly K and outcome bound m on input
  densities ρ, with laws computed by exact composition of the families the protocol applies and
  with exact classical control;
- TV;
- the metrics M_H and M_C;
- the norms ‖·‖ (the trace-norm induced norm of a family, X ↦ ⊕_a F_a(X), on all complex
  matrices) and ‖·‖_{1→1};
- the δ-forms V_δ, L_δ, I_δ, U_δ, C_δ, and the notation C_δ[M, Λ].

The kinematic operations inside the δ-forms (uniform attachment and partial trace in C_δ,
`withSpectator` in I_δ, transport in L_δ, conjugation in U_δ) stay exact. Relaxing them would
change the δ-forms, which this unit does not do.

**Finite dimension is finite accessible resolution, not A1** (as in unit 2 §1).

## 2. The approximate-structure-rule model (declared in advance)

**Rules relaxed.** All six structure rules of Main:572 are relaxed, each with its own parameter.
The lane names three of them: preparation (d), readout (e) and feed-forward (c). Relaxing all six
keeps the model from leaving any rule exact for convenience. The lane's case is the special case
η_a = η_b = η_f = 0. The kernel fields are those of `FiniteOperationalTheory`
(OB/OperationalAssembly.lean:594).

**Form of every relaxation.** An exact rule declares a specified object X available. Its η-form
declares instead that some available Y, with the same outcome set and at the same level, has
‖Y − X‖ ≤ η_r. X and Y are families, or preparations from the system into a level. The norm is
the family norm ‖·‖ of §1 for families. For a preparation P from the system into level n it is
‖P‖_{1→1}, the trace-norm induced norm on all complex matrices.

The errors are absolute: they do not scale with the norm of X. Each η_r is uniform over all
instances of its rule at a given level, and it may depend on the level, η_r = η_r(n). Every bound
names the levels at which it reads each η_r. Write η = (η_a, η_b, η_c, η_d, η_e, η_f), with
|η| = max_r η_r.

| Rule | Kernel field(s) | Exact object X | η-form |
| --- | --- | --- | --- |
| (a) identity | `avail_id` | id on the system | some available single-outcome system family I′ with ‖I′ − id‖ ≤ η_a |
| (b) coarse-graining | `avail_coarse`, `availExt_coarse` | the coarse-graining of an available F along f : O → O′ | some available G with outcome set O′ and ‖G − coarse_f(F)‖ ≤ η_b |
| (c) feed-forward | `availExt_bind` | at level n, F followed by G(a) chosen by the outcome a, with outcome set O × O′ | some available H at level n with ‖H − bind(F, G)‖ ≤ η_c |
| (d) preparation | `prepAvail_uniform`, `prepAvail_post` | (d1) uniformAttach(r), r ≥ 1; (d2) Φ ∘ P for an available preparation P and an available single-outcome Φ at its level | (d1) some available P_r with ‖P_r − uniformAttach(r)‖_{1→1} ≤ η_d; (d2) some available P′ with ‖P′ − Φ ∘ P‖_{1→1} ≤ η_d |
| (e) readout | `readout`, `readout_avail`, `readout_local` | at level n, the n-outcome family `localLuders` (the form `readout_is_localLuders`, OB/OperationalAssembly.lean:658, derives from spectator independence) | some available n-outcome family R_n at level n with ‖R_n − localLuders_n‖ ≤ η_e(n) |
| (f) discard | `prepAvail_discard` | discardWith(P, F) for an available preparation P and an available family F at its level | some available system family G with ‖G − discardWith(P, F)‖ ≤ η_f |

**Rule (e), alternative form.** The kernel's premise for (e) is spectator independence on
products, not the Lüders form. The faithful relaxation of that premise is (e′):
‖R_{n,k}(X ⊗ Y) − X ⊗ P_k Y P_k‖₁ ≤ η′ ‖X‖₁ ‖Y‖₁ for products, summed over k. Node 1 derives the
dimension-dependent constant c with which (e′) implies (e_η) at η_e = c·η′. This is a
norm-conversion step of the kind unit 2 §1.1 describes. Results are stated in η_e.

**Properties fixed with the model, verified at node 0:**
- (M1) at η = 0, each η-form is the exact rule, so the η = 0 class is exactly
  `FiniteOperationalTheory`;
- (M2) the classes are monotone: η ≤ η′ componentwise gives class(η) ⊆ class(η′);
- (M3) no η-form refers to the quantum instrument set (`IsFiniteEndomorphicKrausInstrument`,
  OB/KrausSoundness.lean:112). Each one refers only to kinematic maps.

**Parameters are independent.** δ (the conditions) and η (the rules) are independent parameters.
Neither is a function of the other in the model. A bound is stated as a function of
(δ, η, d, n, m, K) at fixed (d, m, K) and level n. For Direction 2 it is stated as a function of
(ε, η, d, N_Λ, m, K).

**Out of scope, with reasons fixed now.**
- Noise in the protocol's classical control (a wrong next family chosen with some probability).
  It changes the history laws of T and Q alike, so it alters the comparison rather than the
  theory. It would change the history class and the metrics, which unit 2 fixed and this unit
  keeps.
- Approximate input states. The history class takes the supremum over all input densities.
- Relaxing the kinematic operations inside the δ-forms (§1).

**Status of the model.** The η-model is a class of hypothetical operational theories studied
mathematically. It is not a premise of the framework, it changes no posit of Main's ledger, and it
alters neither unit 2's exact characterization nor #1169's exact conditions (§A.29, §A.50 item 6).

## 3. Preregistered questions

| ID | Question | Metric | Status field |
| --- | --- | --- | --- |
| Q0η | Do (M1)–(M3) hold? Do unit 2's counterexample theories T_alg, T_dec and T^{(L)} lie in every η-class (control C1)? Does the countercontrol theory T_triv have the properties stated in §5.3? | none | open |
| Q1-C (Direction 1) | At fixed (d, m, K) and level n: do C_δ[M, Λ] for suitable M, Λ, together with the η-rules, imply M_C ≤ ε(δ, η, d, n, m, K) with an explicit ε, and ε → 0 as (δ, η) → 0? Which η_r enter, at which levels, and in what form? | M_C | open |
| Q1-H (Direction 1) | The same question under M_H. A proved M_C bound gives the same M_H bound through M_H ≤ M_C. Q1-H additionally asks whether some η_r that enters the M_C bound can be removed from the M_H bound. That sub-question is answered or recorded open. | M_H | open |
| Q2-L7 (Lemma 7) | At a level n, with m ≥ 2, K ≥ 2 and M_C(T, Q) < ε for T in class(η): are there correspondences c, c′ with ‖F − c(F)‖ and ‖c′(J) − J‖ at most an explicit κ(ε, η, …), with κ → 0 as (ε, η) → 0? | M_C | open |
| Q2-T8 (Theorem 8's converse) | On a level set Λ containing every level the δ-forms reference: does T in class(η) with M_C < ε satisfy C_{δ(ε, η, N_Λ)}[m, Λ] with an explicit δ(·) → 0 as (ε, η) → 0? Do the conditions m ≥ 2, K ≥ 2 and the level-set condition stay sufficient? | M_C | open |
| Q2-H | Direction 2 under M_H. Unit 2's disproof (Theorem 5) transfers to every η-class if C1 holds. Recorded at node 0 with no new derivation. | M_H | open |
| Q3 (secondary) | The analogue of Corollary 10 when δ and η tend to 0 together. Each direction is a separate question (§A.34). Not required by the stopping rule. | M_C | open |

Every question is answered separately for M_H and for M_C. M_H ≤ M_C is the only relation used
between them, and only in its valid directions: an M_C upper bound gives an M_H upper bound, and
an M_H lower bound gives an M_C lower bound. A result under one metric is not used as evidence
for the other in any other way. Direction 1 and Direction 2 are separate questions with separate
statuses (§A.34).

## 4. Decision rule (fixed now)

Each of Q1-C, Q1-H, Q2-L7 and Q2-T8 ends in exactly one of the following branches. Verdict text
is generated from what is derived, and only over green controls (§5).

- **B1, survives.** An explicit bound, proved, that tends to 0 as (δ, η) → 0 (Direction 1) or as
  (ε, η) → 0 (Direction 2). The report states every hypothesis, the levels at which each η_r is
  read, and which η_r enter. Status: proved (paper derivation, [A]).
- **B2, survives non-uniformly.** A proved bound that tends to 0 only under an extra condition on
  how η → 0, for example η_r(n) → 0 faster than a stated function of the dimension or the depth,
  or only on a reduced set of levels or outcome bounds. Status: proved on the stated scope; the
  extra condition is named as a finding.
- **B3, broken.** A theory in class(η) satisfying the hypotheses of the unit 2 statement for
  arbitrarily small (δ, η) or (ε, η), or at δ = 0 (respectively ε = 0) and every η > 0, whose
  metric (Direction 1) or δ-forms (Direction 2) stay bounded away from the unit 2 conclusion.
  Status: disproved, for the stated metric and scope only. A negative result is stated only for
  the class it rules out.
- **B4, obstruction.** A named step of the unit 2 proof that uses an exact rule, where no
  η-continuous replacement is obtained. The report states the step, the estimate that fails and
  what would close it. Status: open, with the named obstruction. Failure to find a bound is not a
  disproof of the statement.
- For Q2-H, the branch is the one C1 decides: disproved in every η-class if C1 is green.

**Inputs from unit 2.** Unit 2's results are reviewed paper derivations, not independently
verified theorems (owner decision, item 3; §A.46 item 8). A unit 3 result that reuses an
unchanged unit 2 step is stated relative to that step, labelled [U2]. Every step whose argument
the η-model changes is re-derived here (§A.46 item 7).

## 5. Controls (fixed now)

### 5.1 C0: reproduction at η = 0

At η = 0, every bound derived under Q1 and Q2 must coincide with unit 2's bound, in its
expression and in its hypotheses:
- Theorem 2: ε_s = δ(4N(m+1) + 3) under δ(N(m+1) + 1) < 1, and
  ε_s^{sys} = δ + δ(4d(m+1) + 3).
- Theorem 3: ε_c = (1+δ)^{3k+1} − 1 + δ, with k = ⌈log₂(m N²)⌉ and L = n·2^k.
- Theorem 4: M_H ≤ M_C ≤ ½((1+ε₁)^K − 1), with ε₁ = max(ε_s, ε_c), under
  C_δ[max(m, 2), Λ₁(n, m)].
- Lemma 7: ‖F − c(F)‖ ≤ 160ε and ‖c′(J) − J‖ ≤ 184ε, for M_C < ε ≤ 1/48 with m, K ≥ 2.
- Theorem 8: V_κ, U_κ, I_{(N_Λ+1)κ}, C_{2κ} and L_{2κ}, with κ = 184ε and
  δ(ε) = 184(N_Λ + 1)ε.

The check is symbol by symbol. A bound that is weaker at η = 0 than unit 2's, or that needs a
hypothesis unit 2 does not, fails C0. Its verdict is void until it is repaired.

### 5.2 C1: transfer of unit 2's negative results

By (M1) and (M2), every theory satisfying the exact rules lies in every class(η). So the following
hold in every η-class:
- Proposition 1 (T_alg);
- Theorem 5 (T_dec: the M_H converse fails);
- Proposition 11 (T_dec: the M_C converse fails at m = 1 and at K = 1);
- Proposition 9 (T^{(L)}: a metric that omits a level does not bound U_δ there).

Node 0 checks (M1) and (M2). Any η-result that contradicts one of these statements is void. In
particular, no Q2-T8 verdict may drop m ≥ 2, K ≥ 2 or the level-set condition.

### 5.3 CC: countercontrol, a relaxation that breaks Direction 1 (candidate)

**T_triv**, on any carrier, defined as follows:
- *Available families,* on the system and at every level: exactly the outcome-independent
  instruments F_a = p_a Φ_a, with (p_a) a probability vector and each Φ_a completely positive and
  trace preserving.
- *Available preparations:* the completely positive, trace-preserving maps from the system into a
  level.

**Claimed properties,** verified on paper at node 0:
- rules (a), (b), (c), (d) and (f) hold exactly;
- V, L, I, U and C hold exactly (δ = 0);
- rule (e) fails at every level n ≥ 2, and (e_η) holds with η_e(n) = 2, since both families have
  norm 1;
- every T_triv law is independent of the input state, so M_H(T_triv, Q) ≥ 1/2, on the system and
  at every level, for m = 2 and every K ≥ 1. Hence M_C ≥ 1/2 as well.

**Rule.** Any Direction 1 bound must satisfy ε(0, η) ≥ 1/2 at η_e(n) = 2 for n ≥ 2, η_e(1) = 0 and
every other η_r = 0, for m = 2. A bound that falls below 1/2 there is void. This tests that η_e is
not dropped from the bound; it is a weak test of the size of η_e's coefficient. If node 0 does
not verify the claimed properties, the report records that no Direction 1 countercontrol is
fixed, and why.

**Direction 2.** No countercontrol beyond C1 is fixed in advance. No theory is known in which
relaxing the rules alone breaks Lemma 7 or Theorem 8 at m, K ≥ 2. Finding one is branch B3 of
Q2, and fixing a candidate now would presuppose that outcome. The same reason applies to rules
other than (e) in Direction 1.

## 6. Order of work

0. Node 0: Q0η, that is (M1)–(M3), C1, CC and the (e′) to (e) conversion constant. If C1 or (M1)
   fails, the model is repaired before any further node, and the repair is recorded.
1. Node 1: a census of every use of an exact structure rule in unit 2's Theorems 2–4, Lemma 7 and
   Theorem 8, including the uses through `avail_of_availExt_one` (OB/LevelOneSeam.lean:107), which
   rests on rules (d1) and (f). Each use records its rule, the level, and the property the proof
   takes from it.
2. Q1-C, one rule at a time in the order (e), (c), (d), (f), (b), (a); then all six jointly.
3. Q1-H.
4. Q2-L7, then Q2-T8.
5. Q3, only if Q1 and Q2 have reached a status.
6. Pressure test of every favourable branch (§A.31): hidden exact inputs, level bookkeeping, and
   the uniformity of η_r over instances.

## 7. Productivity test (fixed now)

**The baseline restatement S.** S is the bound obtained from unit 2's text by changing nothing
except one thing: at each use of an exact rule, insert an additive term η_r multiplied by a
coefficient read from unit 2's existing norm estimates (the norms of the maps composed after that
use). S uses no new construction or lemma and changes no hypothesis.

**Gem** iff the unit yields, with proof, at least one of the following:
- (G1) an explicit bound for Q1-C, Q1-H, Q2-L7 or Q2-T8 whose proof needs something beyond S: a
  new construction or lemma, a changed level set, or a changed threshold on m, K or the range of
  ε. This applies in particular where a unit 2 step uses an exact rule for a property other than
  a norm estimate, such as an exact identity, exact trace preservation used to normalize a law,
  or exact membership used structurally;
- (G2) a counterexample (branch B3) in which approximate rules break a transfer;
- (G3) a precisely identified obstruction (branch B4);
- (G4) a lower bound showing that an η_r enters a bound necessarily, or a proof that an η_r which
  S would include does not enter.

**Non-gem (record-only):**
- a result that is S, verified valid;
- a bound that only adds constants to unit 2's bounds;
- the countercontrol at fixed η_e = 2 alone.

The independent reviewer decides whether a step goes beyond S.

## 8. Stopping rule (fixed now)

Stop when each of Q1-C, Q1-H, Q2-L7 and Q2-T8 reaches a status at fixed (d, m, K): B1, B2, B3 or
B4. Also stop when 3–4 consecutive passes yield no NEW finding (§A.31). Q3 is not required. Any
branch favourable to the framework is pressure-tested before it is accepted.

## 9. Inputs and their labels

- [K] kernel-checked on `main` at the pin:
  - `FiniteOperationalTheory` and its fields (OB/OperationalAssembly.lean:594);
  - `readout_is_localLuders` (:658), `HasCompositeUnitaryControl` (:665) and
    `pureSeedPrep_available_of_swap` (:675);
  - `avail_of_availExt_one` (OB/LevelOneSeam.lean:107), `SystemToLevelOne` (:117) and
    `ExactAllFiniteEndomorphicQuantumOps` (:186);
  - `availExt_relativeReadout` (OB/AncillaClosure.lean:231) and `IteratedAncillaClosure` (:247);
  - `CompositeOperationalValidity` (OB/OperationalValidity.lean:88) and `cp_of_valid_inert` (:105);
  - `InertSpectatorCompositionality` (OB/SpectatorBridge.lean:223);
  - `IsFiniteEndomorphicKrausInstrument` (OB/KrausSoundness.lean:112);
  - `exactAll_iff_physical_general` and `general_characterization` (OB/GeneralCarrier.lean:100,
    :107).
- [P] Main §3.4 at the pin: Main:572 (the six rules, the five conditions, the kinematics taken as
  given), :604, :606 and :610.
- [U2] unit 2 (`../unit2/REPORT-r3.md`, commit `b10379335d8c36207f10cff476991a8daaa3210e`;
  `../unit2/PLAN.md`; `../unit2/PRESERVATION.md`): reviewed paper derivations, not independently
  verified (§A.46 item 8). They are used under §4's rule for inputs from unit 2.
- Partially verified: unit 1 (`../unit1/`), used for labels only.
- [L] standard literature, recalled.
- [A] this unit's own arguments, unreviewed until §10's review.
- Provenance only, with no claim using their content: the owner decisions cited above; the
  consolidated synthesis at #1169 comment 7189143747; the unit 2 reviews on PR #1584.
- No content off `main` is used as support (§A.42 item 8). The report traces every reference
  again before it lands.

## 10. Review

- An independent non-author reviewer reviews the report before any acceptance. The reviewer is an
  agent other than `writer-approx-comp` and is given this plan.
- The reviewer checks:
  - C0 symbol by symbol;
  - C1 and CC;
  - each η-rule use against the node 1 census;
  - the separation of M_H from M_C, and of Direction 1 from Direction 2;
  - the gem verdict against §7.
- A model's review is evidence of review, not independent mathematical verification (§A.46
  item 8).
- Acceptance and preservation are owner decisions.

## 11. Boundaries

- Paper-only; no computation and no Lean build.
- No manuscript change.
- No premise adopted, weakened or changed; no premise chosen because it reproduces QM (§A.29).
- Unit 1 and unit 2 records are not edited.
- No GitHub write by the writer; the coordinator commits this record.
