# Phase 1 report: post-A1 obstruction reassessment

**WIP / UNVERIFIED. Paper-only. Awaits independent non-author review.** Author: Claude Code
session, designated writer of this unit, 2026-11-27. Plan: `PLAN.md`, committed before this
analysis at `569940b5`. Drafting snapshot `D`: `main` at `13c05b4fe`. No computation was run; no
premise is adopted; no manuscript, Lean module, registry, record or Issue is edited.

**Authorization.** Owner decision quoted at #1169 comment 7209026471 (amaybaum, received
2026-11-27, coordinating session): "Approved: Phase 1 post-A1 obstruction reassessment as scoped
above, paper-only under WP-2, accountable to #1169 with #914." The same decision: "No premise
adoption, scientific computation or Phase 2–4 execution is authorized by this decision."

**Goal link (§A.47).** As in `PLAN.md`: the #914 central bottleneck (representation equivalence
without a physical mechanism) under A1 retirement (#1169). This report decides which obstructions
survive without A1, which A1 retirement reopens, and which candidate to test first. It does not
decide whether a mechanism exists.

**Conditionality.** Everything below is conditional on A1's retirement, not a presumption of it.
"Without A1" means: the site set may be infinite (ℤ^d) and the configuration space uncountable,
while local finiteness is kept: finite site alphabet (F1), finite reading sets / finite coupling
range, finite visible capacity (Lemma 1, Main:46), finite measurement horizons. Linearity (A5,
ledger item vii) and the second-order form (item xiii) are kept unless a candidate says otherwise.

Support labels: **K** kernel theorem on `main` (cited, not rebuilt); **X** exact algebra on paper in
a cited record; **P** paper argument in a cited record; **P-here** an argument written in this
report, unreviewed; **R-off** a record not on `main`.

## 0. Outcome

1. **The coherent-control obstructions survive A1 retirement.** Every established obstruction to
   native coherent control (interference beyond the configuration basis, continuous mixing,
   noncommuting non-monomial transformations) traced here rests on the *interface*: bijection-level
   dynamics read through configuration-algebra effects on a finite visible carrier. Its load-bearing
   step is positivity / monomiality / diagonal preservation of bijection channels, or finiteness
   of the *visible* carrier from Lemma 1. None uses total finiteness. The kernel statements are
   `Fintype`-scoped, so their A1-free form is a paper-level transfer (P-here, §2.1), not a kernel
   result.
2. **The setting-selection, magic and universality obstructions depend on A5, not A1.** MECH-1
   Lemma A, Theorem T, Proposition AS and Proposition C, and UNIV-1 Theorem L, use affinity of the
   rule. Their finite-carrier form is windowed and transfers to ℤ^d (P-here). The posit whose
   relaxation bears on them is A5.
3. **What A1 retirement reopens** is the global-finiteness layer: exact global return and the
   record erasure it forces, the finite-reservoir bound on preparation (no fresh resources without a
   supply), all-time finite realizability (`PPer`), the all-precision fixed-finite-carrier
   obstruction (Main:784, E-AR), the counting-measure selection (ledger item iv) and the
   eventual-image injectivity step (Lemma 3). These are obstructions to **preparation, persistent
   records and readiness**, not to coherent control.
4. **Removing an obstruction is not establishing a mechanism.** Every reopened item is reopened as
   *no longer proved*, not as escaped, except where a cited counterexample exists (`PPer`: the
   infinite-XOR construction; recurrence: REC-1 and NR-1). A bare infinite carrier supplies nothing
   (SUBSTATE-1 identity countercontrol).
5. **A1 retirement also removes resources.** The finite-return route to rooted P-indivisibility
   (Main §2.3) loses its support, and for the linear prime-q rule on ℤ^d with Haar law NR-1 proves
   no P-indivisibility at any horizon (A1-FCLASS row 13). The counting-measure selection has no
   permutation-invariant normal analogue on an infinite hidden set (BIDUAL-DIO, PERM; R-off).
6. **Windowed finiteness (assumption-watch AW-P1-1).** F1 with finite reading sets and a finite
   horizon gives every fixed experiment a finite backward cone (A1-FCLASS row 05; Main §3.3). Every
   obstruction whose finiteness enters only at a fixed window therefore survives in windowed form.
   Only statements quantified over all times, all precisions or the whole configuration space
   reopen.
7. **Ranked candidates (§3):** (1) C-ENV, an infinite low-entropy environment acting as entropy
   sink and supply of terminal meters; (2) C-ENV×MON, environment-monitored controllers, which
   targets MECH-1's residual premises and needs a non-affine controller coupling; (3) C-SEL, an
   A1-free measure selection (enabling, not a mechanism); (4) C-NL, a nonlinear reversible rule
   (A5 relaxation, already held as #1461/PM-D5); (5) C-ONT, unbounded ontic resolution for
   all-precision single-system statistics. Six routes are rejected (§3.6).
8. **Phase 2 recommendation (§4):** test C-ENV first, by two preregistered exact-algebra tests on
   the native linear rule on ℤ^d: windowed revival of a finite excitation over the vacuum, and
   existence of a rule-invariant translation-invariant far-field law. A pressure test written here
   (§3.1, P-here) suggests that linear F_p rules may revive windowed content infinitely often by
   self-similarity, which would eliminate C-ENV under A5 and route it to C-NL.

Productivity (§A.31): gem by the plan's test. Item 1 exposes that the coherent-control bottleneck is
insensitive to the posit being retired (POSITIVE for the obstructions, unfavourable to the hope that
A1 retirement helps coherent control); item 2 is NEW as a cross-propagation (the relevant posit is
A5); item 6 is ELABORATING on A1-FCLASS row 05.

## 1. Inventory method as executed

Read: #914 body (dependency index, obligation matrix rows 1–21, §4), #866 body, #1507, #1509 body
and comments (BIDUAL-DIO, NONDIO-M2 reviews), #1461, #1062, #1210, #1169 body; owner decision
c.7209026471. Records read on `main`: A1-FCLASS (`verification/audits/foundations/
a1-finiteness-classes-20261117/CLASSIFICATION.md`), A1-09 census (frozen-sourcing paragraph),
`FrozenSourcing.lean`, `LiftAudit.lean` (Q2), `LiftSource.lean` (T1), `FlowEndpoint.lean`,
`StochasticInterface.lean`, `RouteB.lean`, `OrbitGeneration.lean` (N1), `PhysicalC4Discharge.lean`
(RD1-a), `SubstratumInterfaceAudit.lean` (`obsTheory`, `permTheory`, `a1_of_finite`), Main §1.2,
§3.2–§3.4, §4.5 ledger (Main:736), Main:784; SUBSTATE-1 README and `equivalence-and-d3-scope.md`;
SUBSTATE-2 README, NATIVE-PADIC-1 REPORT, F2-1 stage-2 RESULT; MECH-1 DESIGN; MR-1 MR-star S-L7;
MEAS-Q RESULT (MQ1–MQ4); UNIV-1 RESULT; OBS-EMERGE REPORT-r5. Records read off `main`
(read-only): BIDUAL-DIO NOTE at `e8976f11`, OPRES NOTE at `24702c1d`, I3-SOURCE NOTE at `df520f3b`.

Grep passes over `papers/`, `book/`, `verification/` for the plan's terms, and a second pass for
symplectic / Wigner / Spekkens / stabilizer / epistemic restriction / excess baggage / Landauer /
entropy sink / past hypothesis, found the MECH-1, apparatus-1, MR-1 and Q-A records, which are
reused below rather than re-derived. A third pass surfaced no new admissible result within the
bound. **Not traced (bounded out):** Proposition U (#1504), BQ1 (#1498), QOPS (#1501), GATE-A
(#1503), the #866 single-lead screens' internal proofs, O-ACC's internals. They are listed in §2.4
and carry no classification.

## 2. Classification

Rule (PLAN §Classification): **S** surviving; **R** A1-dependent (reopened), with the step where
A1 enters, sub-labelled *escaped* (cited counterexample) or *unproved*; **U** unclear. Scope column:
P = preparation, O = persistent observation / records, C = coherent control.

### 2.1 Coherent-control obstructions

| ID | Result (source) | Scope | Load-bearing step | A1 use | Class |
|---|---|---|---|---|---|
| P1-01 | Phase ceiling `permTheory_phase_ceiling`, `nonnegBounded_not_phasesAvailable` (FrozenSourcing, K) | C | every available composite one-outcome branch of a bijection-level class preserves nonnegative entries (`preservesNonneg_of_realized`); a quarter phase does not | `Fintype A` only to form matrices; `obsTheory_nonnegBounded` is stated "at every substratum satisfying the finiteness A1 supplies" | **S** (P-here transfer: the transfer and Koopman operators of a measurable bijection are positivity-preserving on any carrier) |
| P1-02 | Dense-control ceiling `permTheory_dense_ceiling` (K) | C | nonnegativity passes to operator-norm limits (`preservesNonneg_of_approx`, entry ≤ norm) | as P1-01 | **S** (P-here: the positive cone is closed in the weak operator topology) |
| P1-03 | Rule independence `obsTheory_rule_independent`, `sourcing_rule_independent` (K) | C | `obsTheory 𝒮 = permTheory 𝒮.Conf` by definition (`Iff.rfl`) | none beyond P1-01 | **S** (definitional) |
| P1-04 | `substratumTheory_not_layerFlowExecutable`, `configurationLevel_not_layerFlowExecutable` (LiftAudit, K); T1 `not_layerFlowExecutable_of_preservesDiag` (LiftSource, K) | C | monomial Kraus operators preserve diagonal states; the half-time gate flow does not | finite carrier for matrices | **S** (P-here: a bijection's Koopman unitary normalizes L^∞(μ), so the diagonal conditional expectation commutes with it) |
| P1-05 | OPRES Theorem C and Lemma C: a non-monomial unitary needs a coherence creator (non-MIO) and a coherence detector (non-DIO) (X; R-off `24702c1d`) | C | closure of CM/RM/MIO/DIO classes under the native operations | proved on **countable** carriers of any size; Prop D and Remark D′ extend detection to measurable carriers for a **nonsingular** bijection with C_V finite | **S** for countable carriers and for nonsingular measurable carriers; see P1-07 |
| P1-06 | BIDUAL-DIO Proposition FV: with C_V finite, every PROD assignment, for every hidden state ω normal or not, is DIO-type (X; R-off `e8976f11`, review CONFIRMED) | C | C_V finite ⇒ every state of B(H_V) normal | uses Lemma 1 (visible finiteness, Main:46), **not** A1 | **S**. It covers the non-normal hidden priors that A1 retirement admits |
| P1-07 | OPRES Conjecture D″: detection half for a **singular** measurable bijection (R-off) | C | not proved | A1 retirement makes uncountable configuration spaces the natural carrier | **U**. Undecided step: Prop D's nonsingularity. P-here note: a Haar-preserving linear rule is nonsingular, so the native linear rule with Haar law falls under Prop D; the open case needs a non-quasi-invariant law |
| P1-08 | I3-SOURCE Lemma S1 and Proposition S2: permutation dilation realizes Ad_W only for monomial W; one-step channels have root-of-unity spectra under same-basis encodings (X; R-off `df520f3b`) | C | assumption (e), countable hidden carrier | countable, not finite | **S** for countable carriers; dropping (e) needs "an uncountable hidden carrier with a non-classical hidden state" (S2), which is imported structure (§3.6, J-2) or, for a diagonal non-normal state, falls under P1-06 |
| P1-09 | Flow endpoint refuted `flow_endpoint_refuted` (K); Route B separation `routeB_target`, `derivedOICore_not_phaseFree` (K); Drive ⇏ Trans `not_boundaryTransitive_flow` (K) | C | explicit countertheories on `Fin 2` / the ball | none: separations by counterexample | **S** (a counterexample stays a counterexample) |
| P1-10 | F2-1 control C6: Koopman eigenvalue ratios of the native wave map are non-real, classified representation-only (F2-1 RESULT, controls on `main`) | C | configuration readouts do not access character-basis phases | none | **S** as a classification; it bounds candidate J-1 (§3.6) |

### 2.2 A5-dependent obstructions (not A1)

| ID | Result (source) | Scope | Load-bearing step | A1 use | Class |
|---|---|---|---|---|---|
| P1-11 | MECH-1 Lemma A: under one fixed affine bijection, a setting only translates slot values (P, `mechanism-1-20261107/DESIGN.md`:404) | P, C | `Φ^t(x,c) = L_t(x,c) + a_t` | stated on F_q^N; the proof is linear algebra and on ℤ^d with finite range each slot at time t involves a finite cone | **S** (windowed, P-here); depends on **A5** |
| P1-12 | MECH-1 Theorem T, Proposition AS (CP ⇔ affine symplectic in Gross's frame, odd q), Proposition C (no quarter phase, infinite-order encoded unitary or Wigner-negative state, odd q) (P) | C | affine symplectic action and Gross's frame on a finite encoded carrier | finite encoded carrier per experiment | **S** (windowed); depends on **A5** and the frame |
| P1-13 | UNIV-1 Theorem L: linear members not universal (P, reviewed) | C (control capacity) | linearity | stated on ℤ^d | **S**; depends on **A5** |
| P1-14 | MR-1 S-L7: single-time current-slice reads are isotropic (an epistemic restriction); two-slice or retained reads are not (P) | O, C | symplectic bracket `MᵀJM = J` | none | **S**; conditional on the declared access |

### 2.3 Preparation, observation and record obstructions

| ID | Result (source) | Scope | Step where A1 enters | Class |
|---|---|---|---|---|
| P1-15 | Exact return Γ_N = I from the finite permutation, and its consequences (Main §2.3; A1-FCLASS rows 03, 07, 14) | O | the cycle decomposition of a bijection of a finite total configuration space | **R, unproved** (and the positive P-indivisibility route loses support; REC-1 and NR-1 give only a.e. or windowed returns) |
| P1-16 | Record erasure in a closed finite system: every record recurs or is erased at the period (Main §2.3 recurrence; MQ4 global reading) | O | the same cycle decomposition, applied to the whole universe | **R, unproved**, for the global form. Two forms survive: MQ4 for a finite **confined** class (finite class, not A1; S), and Poincaré recurrence a.e. under any normalized invariant law (REC-1, A1-FCLASS row 11; S). Escape needs a non-stationary or non-normalizable state class (§3.1) |
| P1-17 | Finite-reservoir preparation bound: a bijection of a finite total space cannot compress the whole state, so readiness and fresh independent resources must be supplied (#885 "supplied, not derived"; NATIVE-PREP-SRC-1, NATIVE-INT-SRC-2 stops) | P | finiteness of the total reservoir available to a reset | **R, unproved**. The bounded screens on a fixed finite two-site ring remain valid for that ring and are not impossibility theorems (§2.4) |
| P1-18 | All-time finite realizability ⇔ `PPer` (`finiteRootedRealizable_iff_pper`, K; A1-FCLASS row 03) | O | one fixed finite carrier for all t | **R, escaped** for nonperiodic all-time laws on infinite carriers (infinite-XOR, `continuous-substates/infinite-xor-counterexample.md`, P) |
| P1-19 | Fixed-finite-carrier obstruction: a single fixed finite carrier cannot equal the continuum operational theory at all precisions (Main:784; #914 row 17b); E-AR (unboundedly many perfectly distinguishable preparations exclude a fixed C²) | C, P | one fixed finite carrier at all precisions | **R, unproved** at all precisions; its windowed form survives by AW-P1-1. SUBSTATE-1: removing it "removes the applicability of that theorem, not the underlying scientific challenge" |
| P1-20 | Counting-measure selection (ledger item iv) and eventual-image injectivity (Lemma 3; ledger item iii) | P, O | uniform probability and eventual image on a finite representative | **R, unproved**. PERM (R-off): no permutation-invariant state on an infinite hidden set; REV is the stated alternative for bijectivity |
| P1-21 | Ensemble underdetermined `ensemble_underdetermined` (StochasticInterface, K) | P | a linear rule fixes zero, so two disjoint invariant sets exist | none essential; without A1 more invariant laws exist | **S** (strengthened) |
| P1-22 | Partition not selected; exact closure fails C1; selected regions of U₂/Q isolated (OBS-EMERGE G4, PP-here in that record) | O | definitional and model-specific | none | **S** |
| P1-23 | MQ1–MQ3 confinement and class isolation for the rounded rule (MEAS-Q, P) | O | local windowed induction | none | **S** |
| P1-24 | NATIVE-PADIC-1: under the unchanged integer rule, deeper p-adic digits cannot affect a low-digit readout (P + K `NativePadicReduction`) | O, C | reduction mod 2^m commutes with the step | none (an F1-relaxation negative) | **S** |
| P1-25 | Finite-depth factorization: a continuous finite-valued readout of a profinite carrier factors through a finite stage (SUBSTATE-2, standard compactness; P) | O, C | compactness | none | **S** |
| P1-26 | NR-1: prime q, α ≠ 0, convex W, Haar: no C4r/C4e and no P-indivisibility at any horizon on ℤ^d (A1-FCLASS row 13) | O | none: an A1-free negative | — | **S** (it applies *because* the setting is infinite) |
| P1-27 | `core_not_routedReadback` (PhysicalC4Discharge, K) | O | a computed certificate for one sealed core | finite model, not an A1 premise | **S** for its model |
| P1-28 | C4r ⇒ rooted P-indivisibility `c4r_implies_pIndivisible` (K; A1-FCLASS row 08) | O | matrix implication | none | **S** |

### 2.4 Composites and Bell

| ID | Result (source) | Scope | Step | Class |
|---|---|---|---|---|
| P1-29 | Bell ceiling for a screened local completion (Main §3.3) | C (composites) | finite reading sets, determinism, measurement independence (xiv) | **S**: the cone is stated "on a site set V of any cardinality" (Main §3.3). Any Bell violation requires dropping (xiv) or locality, with or without A1 |
| P1-30 | Tsirelson not selected: the finite response-table construction realizes PR boxes (Main §3.3; #914 row 16) | C | finite law ⇒ finite reversible dilation | **S** (A1-free conditional) |

**Listed, not classified (outside the bound or not impossibility results):** the #866 single-lead
preparation screens and CP-PREP-1 (bounded screens with "no qualifying candidate"); O-ACC
("unsourced, not passed"); the QPHEN acceptance matrix (#1210; no experiment run); Proposition U,
BQ1, QOPS, GATE-A (not traced).

### 2.5 Summary counts

30 rows: 23 surviving (P1-01 to P1-06, P1-08 to P1-14, P1-21 to P1-30, with P1-16 carrying two
surviving forms), 6 reopened (P1-15 to P1-20; one escaped, five unproved), 1 unclear (P1-07). The
coherent-control column contains no reopened row.

## 3. Candidates

Ranking criteria in the plan's order: physical motivation, additional premises (candidates only,
none adopted), explanatory power, dependent Issues, cheapest eliminating test. §A.31 skepticism is
applied hardest to C-ENV, the candidate most favourable to the programme.

### 3.1 Rank 1: C-ENV, an infinite low-entropy environment as entropy sink and meter supply

- **Physical motivation.** Every laboratory preparation and record dumps entropy into an unbounded
  cold environment (radiation to a cold sky, a cold reservoir). Landauer: a reversible reset needs a
  supply of known states and a place to put the old ones. In a closed finite bijective universe
  (A1) neither exists: records recur (P1-15, P1-16) and fresh resources are bounded (P1-17). This
  is the obstruction set A1 retirement reopens.
- **Additional premises (candidates).** (E1) an infinite site set; (E2) an initial-state class with
  a low-entropy far field: the reference vacuum with finitely many excitations, or a
  translation-invariant maximal-knowledge law (uniform on a Lagrangian subgroup of the two-slice
  phase space, the infinite analogue of a stabilizer state, compatible with S-L7). (E2) is an
  initial-condition posit of past-hypothesis type and is judged under §A.29; it must be fixed by a
  criterion stated before any test. (E3) dispersal: the rule carries finite-support content out of
  every bounded window without revival. (E3) is a property of the rule, decidable, not a posit.
- **Explanatory power.** Preparation and re-arm by export to the far field; persistence of records
  (terminality of whatever has left); conditional freshness of inflowing resources (#885's
  independence requirement); approximate observer closure with bounded leakage (OBS-EMERGE G4 says
  only approximate closure can select a partition). It supplies exactly MECH-1's residual "meter
  supply; terminality of unregistered meters; per-tick meter delivery and arming" in CTRL-MON
  (§6.2 there), which are what a finite closed universe cannot supply. **It does not touch coherent
  control**: P1-01 to P1-08 survive.
- **Dependent Issues.** #866 (native preparation/request source, O-REC, O-SET display), #914 rows
  15 and 20 (C4, instrument), O-RET (#1032), O-ACC, #1062, #1169.
- **Pressure test (P-here, unverified).** Linear rules over F_p are self-similar under Frobenius.
  Illustration, not the native rule: for rule 90, `x(t+1)_i = x(t)_{i−1} + x(t)_{i+1}` over F_2 from
  a single excitation at 0, the value at site 1 at time t is `C(t, (t+1)/2) mod 2`, which by Lucas's
  theorem is 1 at every `t = 2^k − 1`. The excitation's content returns to the window infinitely
  often, at density zero. If the native second-order rule over Z_q behaves alike, a register
  exported to the far field is recovered at sparse times, terminality fails in the information
  sense, and C-ENV is eliminated for linear rules. NR-1's Haar-prior negatives do not apply here,
  because a sink needs a low-entropy far field and Haar is maximal-entropy.
- **Cheapest eliminating test (T-ENV).** Exact algebra on the native linear rule
  `x(t+1) = F x(t) − x(t−1)` over Z_q on ℤ^d (q = 2 and an odd prime; F the nearest-neighbour sum):
  (a) for a single-site excitation over the zero vacuum, is the windowed content at a fixed finite
  window nonzero for infinitely many t, and with what density? Generating-function method:
  `M(z)^t` with `M² = F M − I` gives Chebyshev-type entries `U_{t−1}(F)`, reduced mod p.
  (b) Does a translation-invariant law on the two-slice phase space exist that is invariant under
  the rule and uniform on a Lagrangian subgroup? Eliminates C-ENV under A5 if (a) yields revivals
  at positive density or with full information recovery infinitely often in every window, or if
  (b) has no solution.

### 3.2 Rank 2: C-ENV×MON, environment-monitored controllers (MECH-1 M1 with a native meter supply)

- **Physical motivation.** Controllers in real apparatus are classical because their environment
  monitors them continuously (environment-induced superselection). MECH-1 found that quantum
  compatibility of in-world setting selection holds at odd q if "every S(s) is symplectic and, given
  u_c, the controller's v_c is uniform and independent of all other cells", and that a monitoring
  form (CTRL-MON) relocates the premise to a meter supply and terminal meters. Under the native
  symplectic bracket (S-L7), monitoring `u_c` through a symplectic coupling with a meter whose
  conjugate is uniform randomizes `v_c`: the compatibility condition would be produced by the
  coupling, not stipulated (P-here, unverified).
- **Additional premises (candidates).** C-ENV's (E1)–(E3); a non-affine coupling coefficient set by
  the controller slot (MECH-1's M1; an A5 relaxation, a Layer-0 revision under §A.29); a far field
  half-known in the monitored quadrature (an instance of (E2)). MECH-1 also lists a gauge-violating
  coefficient and a static controller slot or parity clock; whether monitoring removes them is part
  of the test.
- **Explanatory power.** O-SET (in-world settings), Clifford-complete encoded control with in-world
  settings at odd q (Theorem W, Lemmas N and M), and the controller side of QPHEN QX-0 to QX-4. It
  stays inside the classically reproducible fragment (MECH-1 Proposition C(d)): **no** non-Clifford
  resource, contextuality (QX-5) or Bell violation (QX-6, P1-29).
- **Dependent Issues.** #866 (O-SET), #914 rows 8, 9, 11, 12, 20, #1210 (QX-0, QX-1, QX-4, QX-7
  Clifford part).
- **Cheapest eliminating test (T-MON).** On MECH-1's Proposition T′ configuration (odd q, stabilizer
  input, X-type controller): with the controller monitored each tick by inflowing far-field meters
  under one fixed rule, is C-CP met on every reachable input without a supplied schedule? Eliminated
  if any reachable input gives a non-quantum encoded state, or if monitoring needs a supplied meter
  schedule. Run only if T-ENV passes.

### 3.3 Rank 3: C-SEL, an A1-free measure selection (enabling)

- **Motivation.** The counting-measure selection (P1-20) has no infinite analogue that is
  permutation-invariant and normal; ensemble underdetermination survives and strengthens (P1-21);
  #914 row 14 needs a principled `(Obs, μ)`.
- **Premises (candidates).** A maximal entropy-density criterion among translation- and
  rule-invariant laws (Haar for surjective linear rules), stated before outcomes.
- **Power.** #914 row 14, P8 (§4.6, IL condition), the far-field law of C-ENV. Not a mechanism.
- **Eliminating test.** Uniqueness of the maximal entropy-density invariant law for the native rule.
  Non-uniqueness leaves the selection open. Ranked below C-ENV because it explains no repertoire
  item by itself; C-ENV's (E2) is a *low*-entropy far field, so C-SEL and C-ENV pull in opposite
  directions, which the test must face.

### 3.4 Rank 4: C-NL, a nonlinear reversible rule (A5 relaxation)

- **Motivation.** P1-11 to P1-13 show the setting, magic and universality obstructions are A5's;
  POSIT-MIN: observation forces interacting signals at some level; persistent localized structures
  coupled to an exterior are absent in every linear record (OBS-EMERGE Q2).
- **Premises.** A Layer-0 rule change (§A.29: preserved controls, an independent prediction,
  resistance to fitting). The rounded q = 2^16 rule is the corpus's candidate.
- **Power.** #1461, #1062, C-ENV's dispersal and localized apparatus if the linear rule fails T-ENV.
  Proposition AS warns: non-affine ontic bijections are non-CP in Gross's frame, so nonlinearity
  alone yields non-quantum encoded operations.
- **Eliminating test.** Already scoped and held: UNIV-2 / MEAS-Q controlled turn or interaction
  (#1461; owner hold, #1169 c.7079945577). Not recommended for Phase 2 here.

### 3.5 Rank 5: C-ONT, unbounded ontic resolution for all-precision single-system statistics

- **Motivation.** P1-19 reopened at all precisions; ontological models of a qubit need infinitely
  many ontic states (Hardy's excess-baggage theorem; literature, not re-read here). A1 retirement
  permits them.
- **Premises.** Ontic resolution that grows with the experiment's spatial or temporal extent, or a
  continuum per-site alphabet (F1 relaxed), and a native response law.
- **Power.** Single-system all-precision preparation and measurement statistics (#914 rows 17b, 18).
- **Risk.** AW-P1-1: with F1 and finite range, a fixed-horizon experiment sees finitely many ontic
  states, so exactness at fixed horizon needs F1 relaxed, not A1. P1-24 and P1-25 then decouple
  deeper digits under the unchanged rule. The known continuous models (Kochen–Specker 1967) are
  designed simulations (F2-1 C10, a classical counterexample), so the route is close to J-3.
- **Eliminating test.** Under the native integer wave rule with ℝ/ℤ sub-states (SUBSTATE-1
  real-type), does a fixed-window two-cell readout depend on unboundedly many sub-state digits?
  If it factors through finite depth, eliminated for that rule.

### 3.6 Rejected

| ID | Route | Criterion failed | Reason |
|---|---|---|---|
| J-1 | Koopman / character-basis phases of the native map as coherence | imported quantum structure | representation-only (P1-10); using them needs non-configuration observables posited at the interface |
| J-2 | Coherent hidden states on an uncountable carrier (dropping I3-SOURCE assumption (e)) | imported quantum structure | a coherent hidden state is a quantum state posited in the substratum; a diagonal non-normal state is covered by FV (P1-06) |
| J-3 | Response tables, D-W, Kochen–Specker-type simulators | encoded predetermined outcomes; classical simulation encoded | they reproduce statistics by construction and serve as countercontrols (F2-1 C10; I3-SOURCE Lemma O) |
| J-4 | A future or global boundary condition supplying Bell measurement dependence | encoded predetermined outcomes; no eliminating test | a boundary chosen to yield Bell statistics stores them; it can be adjusted to any statistics. A1 retirement also removes the one native global constraint (the closed cycle of a finite bijective universe) |
| J-5 | Bare infinite cardinality | no mechanism | SUBSTATE-1 identity countercontrol: infinitely many hidden states and Γ_L = I with no nonclassical step |
| J-6 | Infinite p-adic digit stacks under the unchanged rule | eliminated already | NATIVE-PADIC-1 (P1-24) |

Candidate generation stopped at five ranked candidates (PLAN bound: six) after J-1 to J-6.

## 4. Phase 2 recommendation

**Test C-ENV first (T-ENV), then C-ENV×MON (T-MON) only if T-ENV passes.** Reasons: C-ENV is the
only candidate drawn directly from the reopened set; it bears on the most dependencies (preparation,
records, readiness, freshness, approximate closure, MECH-1's residual meter premises); its test is
cheap, exact and decisive; and the §3.1 pressure test gives a concrete way for it to fail.

Proposed shape (for owner decision; nothing here is authorized):
1. A preregistration fixing T-ENV (a) and (b), the decision rule as a rule (not expected numbers),
   and the terminality criterion stated in advance: windowed mutual information between the
   initial register value and the window content, with "terminal" meaning eventually zero and
   "revival" meaning full recovery at infinitely many t.
2. Controls, each able to fail: a finite torus must show revival (positive control, A1-FCLASS row
   14); NR-1 composite-q nilpotent α must show revival (row 15); the identity map must show no
   dispersal; rule 90 must reproduce the §3.1 revival times; NR-1 rows 12–13 must be reproduced
   under Haar to check the generating-function machinery.
3. Method: exact generating-function algebra over F_p[z^±] (paper first; any computation is a small
   exact check needing its own authorization).
4. Outcomes. Pass: C-ENV survives under A5; proceed to T-MON. Fail: C-ENV is eliminated under A5;
   record the negative for the class tested only, and route the sink question to C-NL (held under
   #1461).

**What Phase 2 would not show.** A pass establishes a sink and meter supply for preparation and
records under named premises (E1)–(E3). It establishes no coherent-control mechanism: the
coherent-control obstructions of §2.1 survive A1 retirement, and moving them needs a change at the
interface (R-READ, KIN) or in A5, not in A1.

**Gap report (§A.47 item 4).** No candidate here addresses non-Clifford resources, contextuality or
Bell violation; P1-29 forces any account of Bell violations to drop measurement independence or
locality. No active item serves that gap.

## 5. Verification table (§A.46 item 4)

| Claim | Evidence level | Missing verification | Accountable Issue | What resolves it |
|---|---|---|---|---|
| §2 classification (30 rows) | author reading of cited proofs; P-here for transfers | independent non-author review of every row | #1169, #914 | review at this record's head |
| P1-01, P1-02, P1-04 A1-free transfer (positivity, cone closure, Koopman normalizes L^∞) | P-here, standard operator theory | written proof and review; a kernel version is absent | #914 rows 8, 9, 11 | a reviewed paper proof, optionally a Lean statement over a measurable carrier |
| P1-05, P1-07, P1-08 (OPRES, I3-SOURCE) | X in records not on `main`; OPRES Prop D and D′ reviewed (#1509 c.7067531252 per OPRES) | records not on `main` | #1509, #1507 | landing those records, or narrowing these rows |
| P1-06 FV | X, review CONFIRMED (#1509 c.7080291521), not on `main` | record not on `main` | #1509 | landing BIDUAL-DIO |
| P1-11 to P1-13 windowed transfer to ℤ^d | P-here | written proof and review | #1169 | reviewed proof |
| AW-P1-1 windowed finiteness | ELABORATING on A1-FCLASS row 05 (on `main`) | review of its application to each row | #1169 | review |
| §3.1 rule-90 revival illustration | P-here (Lucas's theorem) | check | #1169 | reviewer check |
| Native-rule revival behaviour | conjecture | T-ENV | #1169, #866 | Phase 2 T-ENV |
| C-ENV×MON monitoring produces uniform `v_c` | conjecture (P-here sketch) | T-MON | #866, #914 | Phase 2 T-MON |
| Candidate premises (E1)–(E3), M1, C-SEL criterion | candidates, not adopted | §A.29 tests; owner decision | #1169 | owner decision after Phase 2 |

## 6. Reference tracing (§A.42 item 8)

| Reference | Attached claim | Classification |
|---|---|---|
| #1169 c.7209026471 | authorization | provenance (quoted above) |
| #914 body (obligation matrix, §4) | inventory scope | provenance; each result's support is the kernel or record cited in §2, on `main` |
| #866, #1461, #1062, #1210, #1507, #1509 bodies | inventory scope, Issue mapping | provenance |
| BIDUAL-DIO NOTE, `research/bidual-dio-20261122` at `e8976f11` | P1-06 (FV), P1-20 (PERM), P1-08 rebuttal | **support off `main`: gap** |
| #1509 c.7080237134, c.7080291521 | P1-06 review status | provenance for review status; the content gap is the row above |
| OPRES NOTE, `research/opres-20261121` at `24702c1d` | P1-05, P1-07 | **support off `main`: gap** |
| I3-SOURCE NOTE, `research/i3-source-20261121` at `df520f3b` | P1-08, J-2, J-3 (Lemma O) | **support off `main`: gap** |
| NONDIO-M2 (`7102e6af`) | not used | provenance (cited by #1509 comments only) |
| Kernel modules, Main, A1-FCLASS, SUBSTATE-1/2, F2-1, MECH-1, MR-1, MEAS-Q, UNIV-1, OBS-EMERGE | the rows citing them | support on `main` at `13c05b4fe` |
| #1169 c.7079945577 | C-NL hold | provenance |

The three gaps stay open in this local record. Before any landing they close by landing the three
records or by narrowing P1-05 to P1-08, J-2 and J-3 to "reported in records not on `main`".

## 7. Assumption-watch markers

- **AW-P1-1 (windowed finiteness).** F1 + finite reading sets + finite horizon recover a finite
  carrier per experiment. Only all-time, all-precision or whole-space statements depend on A1.
- **AW-P1-2 (interface, not cardinality).** The coherent-control bottleneck is set by the interface
  premises R-READ and KIN together with Lemma 1, not by A1. Any proposal crediting A1 retirement with
  coherent control must name the interface premise it changes.
- **AW-P1-3 (A5, not A1).** Setting selection, magic and universality obstructions are A5's.
- **AW-P1-4 (retirement removes resources).** Exact return, counting-measure selection and the
  closed-cycle global constraint go with A1.
- **AW-P1-5 (Frobenius revival).** Linear F_p rules may revive finite excitations infinitely often
  over a vacuum, so a low-entropy far field and a linear rule may not jointly give a sink.

## 8. Stop

The plan's stopping conditions are met: every item cited by the named Issues within the bound is
classified or listed as not traced, two further grep passes found no new admissible result,
candidate generation stopped at five, and no computation was run. Independent non-author review is
required before any use of these results (§A.46 item 7).
