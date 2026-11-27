# Phase 1 report, r2: post-A1 obstruction reassessment

**WIP / UNVERIFIED. Paper-only. r2 awaits a delta review.** Writer: Claude Code session,
designated writer of this unit, 2026-11-27. Plan: `PLAN.md` (`569940b5`, committed before r1). r1:
`REPORT.md` at `ccafee2a`, kept unchanged. Changes from r1: `CHANGES-r2.md`. Drafting snapshot `D`:
`main` at `13c05b4fe`. No computation was run, no premise is adopted, and nothing on `main` or in
an Issue is edited.

**Authorization.** Owner decision quoted at #1169 comment 7209026471 (amaybaum, received
2026-11-27, coordinating session): "Approved: Phase 1 post-A1 obstruction reassessment as scoped
above, paper-only under WP-2, accountable to #1169 with #914." "No premise adoption, scientific
computation or Phase 2–4 execution is authorized by this decision." The owner's routing of the
SMD-CL-1, FSLICE-PS-1 and UN-1 findings into Phase 1 is #1169 comment 7209325168 (amaybaum,
2026-11-27T03:51:22Z): "feed these findings into the authorized post-A1 obstruction reassessment,
specifically examining whether the obstruction survives A1 retirement. Our scientific priority
should be finding a physical mechanism that generates the required states, symmetries and
operations, rather than deriving further consequences from independently assumed states." The
four-class test of §3.0 and the contribution matrix of §3.7 follow the owner's further direction,
which the coordinating session relayed for r2.

**Goal link (§A.47).** As in `PLAN.md`: the #914 central bottleneck under A1 retirement (#1169),
with #1217 for the SMD findings. This report decides which obstructions survive without A1, whether
any candidate generates or selects the required states natively, and what Phase 2 should address.
It does not decide whether a mechanism exists.

**Conditionality.** Everything is conditional on A1's retirement, not a presumption of it. "Without
A1" means: the site set may be infinite (ℤ^d) and the configuration space uncountable, while local
finiteness is kept. That covers a finite site alphabet (F1), finite reading sets, finite visible
capacity (Lemma 1, Main:46) and finite measurement horizons. A5 (linearity) and the second-order
form (ledger item xiii) are kept unless a candidate says otherwise.

Support labels: **K** kernel theorem on `main`; **X** exact algebra in a cited record; **P** paper
argument in a cited record; **P-here** an argument written here, unreviewed; **R-off** a record not
on `main` (with its PR).

## 0. Outcome

1. **Coherent control, representational scope.** These results concern the Born form on the
   configuration basis (KIN) with native readouts in the configuration algebra (R-READ, an assumed
   reading of READ, #1501). Their kernel forms are **A1-scoped**: `obsTheory 𝒮 = permTheory 𝒮.Conf`
   with `A1 := Finite 𝒮.Conf` (`SubstratumInterfaceAudit`, `obs_a1`). In this report they survive
   A1 retirement only **conditionally on a P-here transfer (unreviewed)**. The transfer needs (a) a
   countable carrier, or a nonsingular bijection, and (b) a diagonal (entrywise-positive) hidden
   state. The singular or non-diagonal case is unclear (P1-07). Operationally (record laws), OPRES
   shows no non-classical resource to be necessary (D-W, sketch), so this is no operational no-go.
2. **Setting selection, non-Clifford operations and universality depend on A5, not A1** (MECH-1
   Lemma A, Theorem T, Propositions AS and C; UNIV-1 Theorem L). Their finite-carrier proofs are
   windowed, and the transfer to ℤ^d is P-here.
3. **What A1 retirement reopens** is the global-finiteness layer:
   - exact global return (escaped: NR-1 row 12) and the record erasure it forces;
   - all-time finite realizability ⇔ `PPer` (escaped: infinite-XOR);
   - the all-precision fixed-finite-carrier obstruction (Main:784, E-AR);
   - the counting-measure selection and the eventual-image step.

   These bear on preparation, persistent records and readiness. The finite-reservoir preparation
   bound has no located proof and is U.
4. **Removing an obstruction is not establishing a mechanism.** Two reopened rows are escaped by a
   cited counterexample: P1-15 (NR-1 row 12) and P1-18 (infinite-XOR). The others are unproved.
   REC-1 proves a.e. Poincaré recurrence and is no counterexample.
5. **A1 retirement also removes resources.**
   - The finite-return route to rooted P-indivisibility loses its support. NR-1 proves no
     P-indivisibility at any horizon for prime q, α ≠ 0, a lattice-convex window W, two-slice
     readout and Haar law on ℤ^d (A1-FCLASS row 13).
   - No state, normal or not, is invariant under every permutation of an infinite hidden set
     (BIDUAL-DIO PERM, R-off #1509). PERM says nothing about translation- or rule-invariant laws.
6. **The three new records (§2.6).**
   - **SMD-CL-1:** the Q1 obstruction does not rest on the finite counting measure. It is proved
     for the infinite-volume product Haar law, the natural A1-free maximal-entropy law. It
     therefore survives A1 retirement, conditional on (B) and (H) as in the source. Lemma N
     (finite t), the K0 witness ρ_Q (constructed on ℤ^d) and the open K1 question are A1-free.
     S-3 and S-2′ use finite representatives and are reopened as unproved.
   - **FSLICE-PS-1:** no row moves to "derived" without A1. Dropping a premise adds models and
     cannot turn an independent premise into a derived one; the witnesses' transfer to ℤ^d is not
     constructed (U). The NAT-C route uses `R_π = 1 − 2P_π`, which needs an even-L torus, and it
     has no ℓ²(ℤ^d) counterpart.
   - **UN-1:** concerns finite-dimensional operational levels and is unaffected.
7. **No candidate reaches class (i) or (ii) for the required states** (§3.0, §3.7). Nothing here
   generates or selects, from independently justified principles, any of:
   - the condensate state with distinct block values;
   - SMD;
   - a native complex structure;
   - native non-Clifford operations.

   Each candidate either assumes the state (iii) or falls under a named impossibility result (iv).
   Under the owner's bar (at least one fundamental gap resolved without assuming it), no candidate
   resolves a gap non-circularly at present. C-ENV would do so conditionally, for all-time record
   persistence (O-RET), if T-ENV passes for (E2L) and (E2) is justified independently.
   **A1 retirement does not supply one common mechanism for these gaps.** The gaps share a
   structural cause: every required item lies outside the class of B6-equivariant, affine dynamics
   read through configuration-algebra effects under a symmetric maximal-entropy law. That class is
   fixed by the present posits, not by A1. §4 states the minimal missing principle as precisely as
   the records allow, and makes Phase 2 about it.
8. **Vacuum revival decided on paper (§3.1, P-here).** Take the native linear rule over F_p on ℤ^d
   with x(0) = 0 and x(1) = aδ. The value at the origin at t = p^k is exactly a·c^k, where
   c = [(α²S² − 4)^{(p−1)/2}]₀ mod p (odd p). For q = 2 the value at e_1 is a at every t = 2^k.
   The vacuum variant of C-ENV therefore fails terminality for q = 2 (every α ≠ 0 and d), and for
   odd p wherever c ≠ 0. The live variant is a random Lagrangian far field, for which T-ENV is
   redesigned.

Productivity (§A.31): gem by the plan's test. Item 2 is NEW as a cross-propagation. Item 7 is NEW:
it names a common structural cause and the classification shows no generator. Item 8 is NEW (P-here,
unreviewed): a decided negative for the vacuum variant. Item 1 is CONFIRMING, scoped as above.

## 1. Inventory method as executed

As in r1 §1, plus the three new records, read read-only at their pinned heads:
- SMD-CL-1 `REPORT.md` (r2) at `b7e29ea7`, PR #1623;
- FSLICE-PS-1 `REPORT-r2.md` at `f4bd7b2f`, PR #1624 (r3 pending);
- UN-1 `REPORT-r2.md` at `4e84b2f2`, PR #1622.

For UN-1 I read §0–§2 only.

Bounded out: Proposition U (#1504), BQ1 (#1498), GATE-A (#1503), the #866 screens' internals and
O-ACC's internals. Proposition U and BQ1 enter OPRES only through its operational results, which
this report does not use. QOPS (#1501) is not bounded out: R-READ, which OPRES lists as an assumed
reading of READ in #1501, is used here as a named premise of every §2.1 row, and its status is
QOPS's.

## 2. Classification

Rule (PLAN): **S** surviving; **R** A1-dependent (reopened), with the step where A1 enters,
*escaped* (cited counterexample) or *unproved*; **U** unclear. Scope: P preparation, O observation /
records, C coherent control.

### 2.1 Coherent-control obstructions (representational: KIN and R-READ throughout)

| ID | Result (source) | Scope | Load-bearing step and hypotheses | A1 use | Class |
|---|---|---|---|---|---|
| P1-01 | Phase ceiling `permTheory_phase_ceiling`, `nonnegBounded_not_phasesAvailable` (FrozenSourcing, K) | C | bijection-level branches preserve nonnegative entries (`preservesNonneg_of_realized`); the prior is diagonal in the finite kernel | kernel form A1-scoped: `obsTheory 𝒮 = permTheory 𝒮.Conf`, `A1 := Finite 𝒮.Conf`; docstring "at every substratum satisfying the finiteness A1 supplies" | **S conditional on the P-here transfer (unreviewed)**, for countable carriers, or nonsingular bijections with a diagonal hidden state. **U** otherwise, with P1-07's undecided step. FV does not rescue this row: the quarter-phase gate is DIO |
| P1-02 | Dense-control ceiling `permTheory_dense_ceiling` (K) | C | nonnegativity passes to norm limits (`preservesNonneg_of_approx`) | as P1-01 | as P1-01. Alternative support: FV plausibly covers it (DIO is closed and excludes non-DIO targets), but only through BIDUAL-DIO (R-off #1509) |
| P1-03 | Rule independence `obsTheory_rule_independent` (K) | C | `obsTheory 𝒮 = permTheory 𝒮.Conf` by definition | kernel form A1-scoped | **S conditional on the P-here transfer** (it is definitional for any carrier on which `permTheory` is defined) |
| P1-04 | `substratumTheory_not_layerFlowExecutable` (LiftAudit Q2, K); `not_layerFlowExecutable_of_preservesDiag` (LiftSource T1, K) | C | monomial Kraus operators preserve diagonal states | finite region carriers | as P1-01. The transfer: a nonsingular bijection's Koopman unitary normalizes L^∞(μ). It needs nonsingularity, and diagonality of the hidden state for the visible coefficients ω(K) |
| P1-05 | OPRES Lemma C and Theorem C: a non-monomial unitary needs a non-MIO creator and a non-DIO detector (X; R-off #1511/#1509, `24702c1d`) | C | KIN; R-READ; for Theorems B and C, imported fixed coherent resource states | Theorem C on **countable** carriers of any size; on measurable carriers only the **detection half**, under Proposition D (nonsingular bijection, C_V finite, normal ω) or Remark D′ (one possibly non-normal ω, appended with no diffuse hidden factor present, later appends normal) | **S** (countable). Detection half **S** under D/D′'s premises. Otherwise **U** |
| P1-06 | BIDUAL-DIO Proposition FV: C_V finite ⇒ every PROD assignment is DIO-type for every hidden state ω (X; R-off #1509, `e8976f11`, delta review CONFIRMED) | C | C_V finite ⇒ every state of B(H_V) normal | Lemma 1, not A1 | **S** for DIO-type configuration-readout statistics. It does not concern realizing Ad_W |
| P1-07 | OPRES Conjecture D″: the detection half for a singular bijection, and the non-diagonal hidden states of P1-01, P1-02 and P1-04 | C | not proved | uncountable carriers become natural without A1 | **U**. Undecided step: nonsingularity, or diagonality of ω. P-here: a Haar-preserving linear rule is nonsingular |
| P1-08 | I3-SOURCE Lemma S1, Proposition S2 (X; R-off #1508, `df520f3b`) | C | assumptions (a)–(e); (e) is a countable hidden carrier | countable, not finite | **S** for countable carriers. With (e) dropped (an uncountable carrier with a non-classical hidden state) the source leaves the case "not treated": **U** |
| P1-09 | Separations: `flow_endpoint_refuted`, `routeB_target`, `not_boundaryTransitive_flow` (K) | C | explicit countertheories | none | **S** |
| P1-10 | F2-1 control C6: Koopman phases representation-only | C | configuration readouts | none | **S** |

### 2.2 A5-dependent obstructions (not A1)

| ID | Result | Class |
|---|---|---|
| P1-11 | MECH-1 Lemma A (`mechanism-1-20261107/DESIGN.md`:404): a setting under one fixed affine rule only translates slot values | **S** (windowed transfer P-here); depends on **A5** |
| P1-12 | MECH-1 Theorem T; Proposition AS (CP ⇔ affine symplectic in Gross's frame, odd q); Proposition C (no quarter phase, infinite-order encoded unitary or Wigner-negative state, odd q) | **S** (windowed); depends on **A5** and the frame |
| P1-13 | UNIV-1 Theorem L: linear members not universal | **S**; **A5** |
| P1-14 | MR-1 S-L7: single-time current-slice reads are isotropic | **S**; conditional on the declared access |

### 2.3 Preparation, observation and records

| ID | Result | Step where A1 enters | Class |
|---|---|---|---|
| P1-15 | Exact return Γ_N = I (Main §2.3; A1-FCLASS rows 03, 07, 14) | cycle decomposition of a bijection of a finite total space | **R, escaped**: NR-1 row 12 (Haar, nonnilpotent α) gives no exact return on ℤ^d |
| P1-16 | Global record erasure in a closed finite system | the same cycle decomposition, applied to the universe | **R, unproved** in its global form. Two forms survive: MQ4 for a finite confined class (S), and a.e. Poincaré recurrence under any normalized invariant law (REC-1; S) |
| P1-17 | Finite-reservoir preparation bound (#885 "supplied, not derived"; the NATIVE-PREP-SRC-1 and NATIVE-INT-SRC-2 stops) | proof not located | **U** (PLAN step 5). The screens remain valid for their ring and are not impossibility theorems |
| P1-18 | All-time finite realizability ⇔ `PPer` (K; A1-FCLASS row 03) | one fixed finite carrier for all t | **R, escaped**: infinite-XOR (Γ_0 = I, Γ_t = J_2 for t ≥ 1) |
| P1-19 | Fixed-finite-carrier obstruction at all precisions (Main:784; E-AR) | one fixed finite carrier at all precisions | **R, unproved**; the windowed form survives (AW-P1-1) |
| P1-20 | Counting-measure selection (item iv); eventual-image injectivity (item iii) | uniform law and eventual image on a finite representative | **R, unproved**. PERM (R-off #1509): no state is invariant under every permutation of an infinite set; it is silent on translation- or rule-invariant laws |
| P1-21 | `ensemble_underdetermined` (K) | — | **S** (strengthened) |
| P1-22 | OBS-EMERGE G4 and partition non-selection | — | **S** |
| P1-23 | MQ1–MQ3 | — | **S** |
| P1-24 | NATIVE-PADIC-1 | — | **S** |
| P1-25 | Finite-depth factorization (SUBSTATE-2) | — | **S** |
| P1-26 | NR-1: prime q, α ≠ 0, lattice-convex W, two-slice readout, Haar: no C4r/C4e and no P-indivisibility at any horizon on ℤ^d | — | **S** (an A1-free negative) |
| P1-27 | `core_not_routedReadback` (K) | — | **S** for its model |
| P1-28 | `c4r_implies_pIndivisible` (K) | — | **S** |

### 2.4 Composites and Bell

| ID | Result | Class |
|---|---|---|
| P1-29 | Bell ceiling for a screened local completion (Main §3.3; the cone stated on a site set of any cardinality) | **S**. Any Bell violation needs measurement independence (xiv) or locality dropped |
| P1-30 | Tsirelson not selected (PR boxes realizable) | **S** |

### 2.5 Counts for §2.1 to §2.4

30 rows:
- 23 **S**. Of these, P1-01 to P1-04 are S conditional on the unreviewed P-here transfer, and
  P1-01, P1-02, P1-04 and P1-05 carry U residuals in their measurable-carrier cases.
- 5 **R**: two escaped (P1-15, P1-18) and three unproved (P1-16, P1-19, P1-20).
- 2 **U**: P1-07 and P1-17. P1-08's dropped-(e) case is a U residual inside an S row.

### 2.6 New rows: SMD-CL-1, FSLICE-PS-1, UN-1 (R-off; their limitations quoted exactly)

The **criterion** is the plan's rule. A row survives if no step of its proof needs a finite total
configuration space or a finite torus that the A1-free setting removes. It is reopened if such a
step is named. It is unclear if the transfer needs a construction not given.

**SMD-CL-1** (#1623, `b7e29ea7`; source status: "WIP / UNVERIFIED … Pending independent non-author
review").

| ID | Result as stated | Step and A1 use | Class | Constrains candidates? |
|---|---|---|---|---|
| P1-31 | Q1, S-1 and S-2: "under (B) and (H), the selected measure supplies no state that meets the fixed set. Its observer image is a single mixing phase … with scalar Σ … What is missing is distinct block values, not clustering." | S-2 is proved for "the product Haar probability on ((Z/q)²)^{Z^d}", Bernoulli hence mixing. The finite counting measure is not used. Conditional on (B), a reading of the unproved bridge (SM:232), and on (H) | **S** (conditional on (B) and (H)). It does **not** rely on the counting-measure selection that A1 retirement reopens: it holds for that selection's A1-free replacement | **Yes**: it eliminates C-SEL's Haar form as a generator of the condensate (§3.5) |
| P1-32 | S-2′: the energy-shell ensemble is "NOT SOURCED under (H′)"; "its extremality is a separate question … and is not needed" | "the shell is a finite object, and S-2′ concerns its observer image on the finite representative" | **R, unproved**. Without A1 the shell law has no finite form. An infinite-volume B6-symmetric law with conserved densities (Lemma N) need not be extremal, and its ergodic components may carry unequal component energies. P-here: nothing selects the T_1/E/A_1 block pattern among such components, and choosing it would be target-motivated (CC-RECON) | Only negatively: A1 retirement opens a decomposition, not a selection |
| P1-33 | S-3: "On every finite representative the exact rule has finite order L … so the spreading step of Theorem P … has no substratum counterpart" | finite order L on a finite representative | **R, unproved**. On ℤ^d the rule has no finite order. Literature (not re-read): affine CA over F_p asymptotically randomize toward Haar (Pivato–Yassawi). That drives toward the symmetric phase of P1-31 | Yes: asymptotics without A1 point toward the symmetric phase, not the condensate |
| P1-34 | Lemma N: a conserved Ē; "no F^t_*ρ_0 (t finite) is translation-ergodic" if Ē is non-degenerate; "whether … survives t → ∞ limits … is not shown" | stated on ℤ^d | **S** at finite t; t → ∞ open (an open question that exists only without A1) | Yes: at finite t linear evolution only transports the preparation's ergodic and clustering properties |
| P1-35 | K0 witness ρ_Q: translation-ergodic, F-stationary, every premise of the fixed set, Stab(ρ_Q) = U(3)×U(2)×Z_4 ⊊ Stab(C), "every d ≥ 1, every 0 < abs(μ) < 1"; "not O-invariant as a law" | constructed on ℤ^d with wave vectors rationally independent of π, which do not exist on a finite torus | **S** (A1-free; the construction needs an infinite lattice) | Yes: stationarity and clustering do not force SMD, with or without A1 |
| P1-36 | K1: "OPEN, with a sharpened gap" (Lemmas A and R) | stated on ℤ^d | **S** (open stays open) | No candidate addresses it |

**FSLICE-PS-1** (#1624, `f4bd7b2f`, r3 pending; source status: "WIP / UNVERIFIED … pending a delta
review"). Setting: "the carrier is T = (Z/L)^d with d = 3", "V_π present for even L".

| ID | Result as stated | Step and A1 use | Class | Constrains candidates? |
|---|---|---|---|---|
| P1-37 | N-2 class R (reduces to H-PF's positive-frequency clause); N-8 class R under O-1b (Lemma PF); I under the other readings | J_F = D(−D²)^{−1/2} on V_rest is a symbol calculus. P-here: on ℤ^d it is defined off the null set where sin θ = 0 | **S conditional on the P-here transfer** for the reductions; the label-sector part is **U** | No |
| P1-38 | N-9 independent: ρ_P (every even L ≥ 2), ρ_T (L ≥ 7), ρ_T′; class O for odd L ∈ {3, 5} | the witnesses use V_π (even L) and generic lattice momenta on a finite torus | **U** for the transfer: no ℤ^d witness is constructed. **Not D in any case**: dropping A1 enlarges the model class, so it cannot derive an independent premise. The small-L class O has no ℤ^d analogue | Yes: no candidate derives N-9 |
| P1-39 | NAT-C: LI follows from naturality under the whole linear commutant of F, via R_π = 1 − 2P_π (not adopted) | R_π needs V_π ≠ 0, a subspace of the even-L torus. P-here: on ℓ²(ℤ^d) the projection onto one momentum is 0, so R_π = id there | **R, unproved**: the route has no ℓ²(ℤ^d) counterpart. A state-level formulation with spectral atoms at π is not constructed | No |
| P1-40 | "No N_k is class D" | follows from P1-37 to P1-39 | **S** | No |

**UN-1** (#1622, `4e84b2f2`; source status: "reviewed paper derivations, not independently verified"
for its inputs; its own results are "[A]: this unit's paper argument, unreviewed").

| ID | Result as stated | Step and A1 use | Class | Constrains candidates? |
|---|---|---|---|---|
| P1-41 | D2 "controlled on a reduced scope" (τ_min = 0, φ ≤ 184ε; inherited); Theorem D and Corollary D1 in class(η) | finite operational levels (`FiniteOperationalTheory`) of the observable description; no substratum-cardinality step found in §0–§2 | **S** | No |
| P1-42 | "The large branch ν ≥ ν_+ … is not excluded"; the idle step stays "a candidate premise, not adopted" | as above | **S** (open stays open) | No candidate supplies an idle step |

## 3. Candidates

### 3.0 The four-class test

For each required state, symmetry or operation, a candidate is classed as:
- (i) generates it;
- (ii) selects it from physically justified alternatives;
- (iii) assumes it;
- (iv) remains subject to a named impossibility result.

Only (i) and (ii) advance, and only with independently justified principles. **The bar**
(owner clarification, relayed by the coordinating session): a candidate qualifies if it genuinely
resolves at least one fundamental gap without assuming the result it is meant to derive. Resolving
several gaps makes it stronger; it need not resolve all of them. For each candidate the line
"**Gaps resolved non-circularly**" names those gaps, or says none.

The required items are:
- the condensate state with distinct block values (D-BV);
- SMD (stabilizer exactly Stab(C));
- a complex structure (CS: H-PF / J_F, N-2);
- ready and prepared states (READY);
- non-Clifford operations (NC);
- a persistent observer partition (OBS).

### 3.1 C-ENV: an infinite low-entropy environment as entropy sink and meter supply

- **Scope of the A1-specific claim.** By AW-P1-1, a finite universe with a large enough low-entropy
  reservoir supplies meters, ready states and dispersal for any fixed horizon. C-ENV's advantage
  over a finite model is confined to **all-time** terminality of exported content and all-time
  freshness of inflow. The fixed-horizon ingredients are (E2) and (E3), which need no A1
  retirement.
- **Premises (candidates).** (E1) an infinite site set. (E2) a far-field state class in one of two
  variants:
  - (E2v) the zero vacuum with finitely many excitations. It supplies known ready states, and no
    independent randomness;
  - (E2L) a random translation-invariant law, uniform on a Lagrangian subgroup of the two-slice
    phase space. Only this variant can meet #885's independence requirement.

  (E3) dispersal. "Decidable" is dropped. Christol's theorem (automatic sequences for linear rules
  over F_p) is a plausible source, not checked.
- **CC-RECON risk.** Choosing (E2L) as "the infinite analogue of a stabilizer state" is
  target-motivated unless a criterion fixed before outcomes selects it. MECH-1 already flags the
  same risk for terminality of meters.
- **Would address, not "exactly" supplies.** For each item, the variant that delivers it:
  - re-arm by export: (E2v) or (E2L);
  - conditionally fresh random inputs: (E2L) only;
  - all-time terminality of records: both, if (E3) holds for that variant;
  - MECH-1's CTRL-MON residuals (meter supply, terminality of unregistered meters): (E2L).
- **Vacuum revival, decided on paper (P-here, unreviewed).** Take the rule
  x(t+1) = αS x(t) − x(t−1) over F_p on ℤ^d, where S is the nearest-neighbour sum and α ∈ F_p^×,
  with x(0) = 0 and x(1) = aδ.
  1. x(t) = a·E_{t−1}(αS)δ, with E the Dickson polynomial of the second kind
     (E_n = yE_{n−1} − E_{n−2}, E_0 = 1, E_{−1} = 0; equivalently U_n(y/2)).
  2. The polynomial identity E_{mn−1}(y) = E_{m−1}(D_n(y))·E_{n−1}(y) holds over ℤ, where
     D_n(u + u⁻¹) = u^n + u^{−n}.
  3. Mod p: D_p(y) ≡ y^p. Frobenius on commuting translations gives S^p ≡ S_{(p)} (S dilated by
     p), and α^p = α. So D_p(αS) ≡ αS_{(p)}.
  4. E_{p−1}(u + u⁻¹) = (u^p − u^{−p})/(u − u⁻¹) ≡ (u − u⁻¹)^{p−1}. Hence
     P := E_{p−1}(αS) ≡ (α²S² − 4)^{(p−1)/2} for odd p, and P = αS for p = 2. P has range ≤ p − 1.
  5. Iterating step 2, x(p^k) = a·Π_{i<k} P_{(p^i)} δ, a product of dilated copies of P.
  6. The origin's coefficient sums over v_i ∈ supp P with Σ_i p^i v_i = 0. Coordinatewise,
     v_0 ≡ 0 mod p and |v_0| ≤ p − 1 force v_0 = 0, and recursively every v_i = 0. So
     [x(p^k)]_0 = a·c^k with c = [P]_0.
  7. For p = 2 the same digit argument gives [x(2^k)]_{e_1} = a for every k ≥ 1 and every d (the
     unique signed-binary path is v_0 = … = v_{k−2} = −e_1, v_{k−1} = e_1).

  Consequences:
  - For q = 2, any d ≥ 1, α = 1: the register value returns exactly at e_1 at every t = 2^k.
  - For odd prime p with c ≠ 0 (for example p = 3, α = 1, d = 1, c = 1): it returns at the origin at
    every t = p^k.
  - In these cases the vacuum variant fails all-time terminality in the information sense: full
    recovery infinitely often. The negative is scoped to (E2v), these (q, α, d), the single-site
    current-slice excitation and windows containing the stated site.
  - For odd p with c = 0, the vacuum case is undecided by this argument.
  - The r1 illustration used rule 90, which is not injective and so lies outside the bijective
    class. It is superseded by this argument.
- **Redesigned T-ENV (for (E2L)).**
  - *Fixed parameters:* q ∈ {2, 3}, α = 1, d ∈ {1, 3}, the nearest-neighbour S, and a single-site
    register of current-slice value a uniform on F_q.
  - *Far field:* a law uniform on a translation-invariant, rule-invariant Lagrangian subgroup L,
    with L fixed by a criterion stated before outcomes.
  - *Window statistic:* the window content at time t is w_t = a·g_t + h_t, with g_t computed by the
    Dickson algebra above and h_t uniform on a subgroup H_t (the image of L).
  - *Mutual information:* I(a; w_t) = 0 iff g_t ∈ H_t.
  - *Decision:* terminal iff, for every fixed finite window, g_t ∈ H_t for all large t. Revival iff
    g_t ∉ H_t for infinitely many t.
  - *First step:* whether any such L exists.
  - *Elimination scope:* an elimination is scoped to the variant and the (q, α, d) tested.
  - *Controls, each able to fail:*
    - the shift x_i(t+1) = x_{i−1}(t) (two-slice form (x(t−1), x(t)) ↦ (x(t), x(t) shifted)), which
      must report **terminal**: this is the terminal-outcome control;
    - a finite torus, which must report revival (A1-FCLASS row 14);
    - NR-1's nilpotent composite-q case, which must report revival (row 15);
    - the identity map, which must report no dispersal;
    - the §3.1 vacuum result, to be reproduced at q = 2 and at q = 3, α = 1, d = 1;
    - NR-1 rows 12–13 under Haar, which check the generating-function machinery.
- **Classification (§3.0).**
  - D-BV: (iv). The vacuum has Σ = 0 under the B6 action. (E2L) would have to be chosen
    non-symmetric to give distinct block values, which is (iii) with CC-RECON. P1-34 (Lemma N):
    linear evolution transports the far field's symmetry and clustering, and does not create them.
  - SMD: (iv), P1-35 (stationarity and clustering do not force it).
  - CS: none.
  - READY: (iii) globally. Local re-arm would be generated, but only given an assumed low-entropy
    far field (E2), a past-hypothesis-type premise.
  - NC: (iv), P1-12 (Proposition C, odd q) and P1-01 to P1-05.
  - OBS: none directly. Approximate closure with leakage is a possible contribution if a persistent
    localized structure exists, which no linear record shows (OBS-EMERGE Q2).
  - **No item reaches (i) or (ii).**
- **Gaps resolved non-circularly.** None at present.
  - **Conditional:** all-time persistence of records (O-RET; P1-16's reopened form), if (E3) holds
    for (E2L) under T-ENV and (E2) is justified independently. Terminality would then be derived
    from the dynamics rather than assumed: class (ii) for that one gap.
  - The vacuum variant fails this gap in the cases of §3.1.
  - Ready states are not resolved non-circularly: (E2) is itself a supply of known states.
- **What would justify it.** An independent reason for (E2), such as a cosmological low-entropy
  initial condition with its own prediction, plus (E3) proved for the rule. Neither is in the
  corpus.

### 3.2 C-ENV×MON: environment-monitored controllers (MECH-1 M1 with an (E2L) meter supply)

- **Premises.** C-ENV's (E1), (E2L) and (E3), plus MECH-1's M1: a non-affine controller coupling,
  an A5 relaxation, with MECH-1's listed residuals.
- **Classification.**
  - Diagonal controller laws: (ii) **only if** symplectic monitoring by (E2L) meters forces them on
    every reachable input. That is untested, and the principle behind (E2L) is not independently
    justified, so it does not advance.
  - D-BV: none. SMD: none. CS: none.
  - NC: (iv), MECH-1 Proposition C(d): it stays in the classically reproducible stabilizer fragment.
  - OBS: none.
- **Gaps resolved non-circularly.** None at present. Conditional: in-world setting selection
  (O-SET) at Clifford level, if T-MON passes. M1 is then still a posited non-affine coupling,
  judged under §A.29.
- **Eliminating test.** T-MON on MECH-1's Proposition T′ configuration, run only after T-ENV passes.

### 3.3 C-NL: a nonlinear reversible rule (A5 relaxation)

- **Classification.**
  - D-BV and SMD: (iii) or (iv). P-here: a B6-equivariant rule maps B6-invariant laws to
    B6-invariant laws (if g commutes with Φ and ρ is g-invariant, Φ_*ρ is g-invariant). Starting
    from a symmetric law it cannot generate D-BV dynamically. A non-equivariant rule assumes the
    breaking.
  - NC: (iv), MECH-1 Proposition AS (non-affine ontic bijections are non-CP in Gross's frame, odd
    q).
  - OBS: a possible contribution through persistent localized structures (MQ1–MQ3), which are so
    far isolated (P1-22).
  - CS: none.
- **Gaps resolved non-circularly.** None. The rule is a choice, so whatever it supplies is
  assumed unless a §A.29 prediction justifies it.
- **Eliminating test:** UNIV-2 / MEAS-Q, held under #1461.

### 3.4 C-ONT: unbounded ontic resolution

- NC and the all-precision single-system statistics: (iv) under the unchanged rule (P1-24 and P1-25
  decouple deeper digits). With F1 relaxed and a designed response, it is (iii) and close to J-3.
- D-BV: none. SMD: none. CS: none. OBS: none.
- Gaps resolved non-circularly: none.
- Eliminating test as in r1.

### 3.5 C-SEL: an A1-free measure selection (ranked last)

- **Eliminating outcomes.**
  - As a selection principle: non-uniqueness of the maximal entropy-density translation- and
    rule-invariant law **eliminates** it, because it then selects nothing.
  - As a generator of the condensate: **eliminated already**. Its natural form is product Haar,
    whose observer image under (B) and (H) is a single mixing phase with scalar Σ (P1-31). That
    means no distinct block values and no broken ergodic component. P1-33's literature points the
    same way.
- **Classification.** D-BV: (iv), P1-31 (scope (B) and (H)). SMD: (iv), P1-31 and P1-35. CS: none.
  READY: none (Haar is maximal-entropy). NC: none. OBS: none.
- **Gaps resolved non-circularly.** None.

### 3.6 Rejected

| ID | Route | Criterion | Reason |
|---|---|---|---|
| J-1 | Koopman / character-basis phases | imported quantum structure | representation-only (P1-10) |
| J-2 | Hidden states whose off-diagonal values are posited | imported quantum structure | a posited coherent hidden state is quantum structure in the substratum. The residual is a non-atomic carrier with states neither posited coherent nor diagonal. That residual is **open** (P1-07, P1-08), not covered by FV, whose target (DIO-type readout statistics) differs from realizing Ad_W |
| J-3 | Response tables, D-W, Kochen–Specker-type simulators | encoded outcomes or simulation | countercontrols (F2-1 C10; I3-SOURCE Lemma O) |
| J-4 | A future or global boundary condition for Bell measurement dependence | encoded outcomes; no eliminating test | adjustable to any statistics |
| J-5 | Bare infinite cardinality | no mechanism | SUBSTATE-1 identity countercontrol |
| J-6 | p-adic digit stacks under the unchanged rule | eliminated | NATIVE-PADIC-1 |

### 3.7 Ranking, and contributions of the candidates that are not rejected

No candidate advances under §3.0. The ranking orders them as tests, not as sourcing candidates:
1. C-ENV (preparation and records, all-time only);
2. C-ENV×MON;
3. C-NL;
4. C-ONT;
5. C-SEL.

C-SEL moves to last: it is eliminated as a generator, and its selection test eliminates only by
non-uniqueness. C-NL moves above C-ONT: it is the only route not blocked under the unchanged rule
for observer structures, though not for D-BV or NC.

| Candidate | SMD (condensate, distinct block values) | Complex structure | Native quantum ops incl. non-Clifford | Observer emergence | Gravitational coupling |
|---|---|---|---|---|---|
| C-ENV | none ((iv) P1-34 and P1-35; (iii) if (E2L) is chosen non-symmetric) | none | none (re-arm only; NC (iv)) | possible: approximate closure, if localized structures exist | none |
| C-ENV×MON | none | none | Clifford-level in-world settings, if T-MON passes; NC none | none | none |
| C-NL | none ((iii) or (iv)) | none | NC none (Proposition AS) | possible: persistent localized structures | none |
| C-ONT | none | none | none under the unchanged rule | none | none |
| C-SEL | none (P1-31) | none | none | none | none |

## 4. The minimal missing principle, and Phase 2

**Statement, as precisely as the records allow.** Every required item fails at a premise of the
present posit set, not at A1:
- **D-BV and SMD.** Needed: a native rule that selects, among translation-invariant, F-stationary
  observer laws, one with distinct block values and stabilizer exactly Stab(C). Excluded so far:
  - the maximal-entropy selection, in finite and A1-free form (P1-31, under (B) and (H));
  - stationarity plus clustering at K0 (P1-35; K1 open, P1-36);
  - B6-equivariant dynamics from a symmetric law (§3.3, P-here).

  So the principle must either break the custodial symmetry explicitly (in the rule, the coupling
  M ≠ μI, or the selected law) or select one ergodic component by a non-symmetric criterion. The
  first is a parameter choice and must not fit any outcome. The second is the "record-selected
  orbit measure" row that SMD-CL-1 records as REDUCED and open.
- **NC and coherent detection.** Needed: an operation whose Heisenberg dual takes a configuration
  effect outside the configuration algebra, together with a coherence source (OPRES "Missing").
  Excluded so far:
  - any ontic bijection read through R-READ (P1-01 to P1-05, representational scope);
  - in Gross's frame at odd q, any non-affine ontic bijection, because its encoded action is not CP
    (P1-12).

  So the principle must change the interface premise R-READ/KIN, or supply a non-classical resource
  natively.
- **In-world settings.** Needed: a non-affine controller coupling and a non-stipulated reason for
  diagonal controller laws (MECH-1 M1; P1-11).
- **Common cause.** Each gap lies outside the class 𝒞 of B6-equivariant, affine dynamics with
  configuration-algebra readout under a symmetric maximal-entropy law. A1 retirement leaves 𝒞
  unchanged. No record identifies one principle that leaves 𝒞 in all three directions at once.

**Phase 2 proposal (for owner decision; nothing authorized).**

*P2-MIN: the minimal exit from 𝒞.*
- **Question.** Does any single premise that takes the theory out of 𝒞 resolve at least one of the
  fundamental gaps non-circularly, without fitting to the target? The gaps are D-BV/SMD,
  non-Clifford operations (NC) and in-world settings (SET). The exits are:
  - (x1) explicit custodial breaking fixed by a stated criterion;
  - (x2) non-symmetric ergodic-component selection by records;
  - (x3) a non-affine reversible rule (A5 relaxed);
  - (x4) a readout outside R-READ.

  If no exit does, which premise is the minimal one that must be added, and with what proof?
- **Preregisterable decision rule** (fixed in PLAN before any derivation, outcome-neutral). For
  each exit x and gap g, one class:
  - **RESOLVES** if a proof (paper; kernel where cheap) derives g from x and the stated posits,
    where x neither contains g as a clause nor is parametrized so that it can be tuned to g. The
    test for tuning: some admissible value of x's parameter yields ¬g;
  - **BLOCKED** if a cited or new impossibility result covers (x, g);
  - **ASSUMES** if g enters x's statement;
  - **OPEN** otherwise, with the step named.

  Outcome A: some x RESOLVES some g. Outcome B: every (x, g) is BLOCKED or ASSUMES. Outcome C:
  otherwise.
- **Controls, each able to fail.**
  - Inside 𝒞 the rule must return BLOCKED for D-BV (P1-31), NC (P1-12) and SET (P1-11).
  - A deliberately circular exit, "posit the condensate state", must return ASSUMES.
  - A tunable exit, "M an arbitrary symmetric-breaking matrix", must fail the tuning test.
  - The K0 witness ρ_Q (P1-35) must not be credited to any exit that only adds stationarity or
    clustering.
  - MECH-1 Proposition AS must classify (x3) × NC at odd q as BLOCKED in Gross's frame.
- **Cost.** One writer session and one independent review, paper-only, of the size of this unit.
  No computation is needed, except optional small exact checks of the (x1)/(x3) algebra, which
  would need their own authorization. (x1) and (x2) touch SMD; whether they fall under "no SMD
  successor investigation yet" is for the owner. Without them the unit runs on (x3) and (x4).
- **What each outcome decides.**
  - A: names the first non-circular physical sourcing candidate, with its gap, for a §A.29 test.
  - B: a proof that the present posit set plus any one of (x1)–(x4) cannot source these gaps. That
    is the rigorous demonstration of the missing principle: at least two premises are needed, or a
    premise outside the four.
  - C: the named open steps become the next bounded units.

*Secondary: T-ENV (§3.1).*
- **Question:** is an (E2L) far field an all-time sink for the native linear rule at the fixed
  (q, α, d)?
- **Rule and controls:** as in §3.1.
- **Cost:** paper algebra, one session.
- **What it decides:** pass makes C-ENV a conditional (ii) candidate for O-RET; fail eliminates
  (E2L) for those (q, α, d). It decides no required state.

**Gap report (§A.47 item 4).** Nothing active serves D-BV/SMD generation, NC, contextuality or Bell
violation from a native principle. P1-29 forces any account of Bell violations to drop
measurement independence or locality.

## 5. Verification table (§A.46 item 4)

| Claim | Evidence level | Missing verification | Accountable Issue | What resolves it |
|---|---|---|---|---|
| §2 classification (42 rows) | author reading; P-here transfers | delta review | #1169, #914, #1217 | review |
| P1-01 to P1-04 transfer, with (a) and (b) | P-here | written proof and review; the kernel form is A1-scoped | #914 | reviewed proof; optionally Lean over a measurable carrier |
| P1-05, P1-07, P1-08; R-READ, KIN | X in records not on `main`; R-READ an assumed reading of #1501 | landing; QOPS status | #1509, #1507, #1501 | land records or narrow rows |
| P1-06 FV; P1-20 PERM | X, review CONFIRMED, not on `main` | landing | #1509 | land BIDUAL-DIO |
| P1-31 to P1-36 | X/A in SMD-CL-1, pending review there | that review; landing | #1217, #1623 | review and preservation decision |
| P1-37 to P1-40 | A in FSLICE-PS-1, r3 pending | delta review; landing | #1217, #1624 | same |
| P1-41, P1-42 | A in UN-1, inputs model-reviewed | review; landing | #1622 | same |
| §3.1 vacuum-revival argument | P-here (standard Dickson and Frobenius identities) | independent check | #1169 | reviewer check |
| §3.3 equivariance remark | P-here, elementary | check | #1169 | reviewer check |
| §4 class 𝒞 statement | P-here synthesis of cited results | review; P2-MIN | #1169, #914 | Phase 2 |
| Candidate premises (E1)–(E3), M1, (x1)–(x4) | candidates, not adopted | §A.29 tests; owner decision | #1169 | owner decision |

## 6. Reference tracing (§A.42 item 8)

| Reference | Attached claims | Classification |
|---|---|---|
| #1169 c.7209026471, c.7209325168 | authorization, routing | provenance (quoted) |
| Issue bodies #914, #866, #1461, #1062, #1210, #1507, #1509 | scope | provenance |
| BIDUAL-DIO, `research/bidual-dio-20261122` `e8976f11` (#1509) | P1-06; P1-20 (PERM); §0 item 5; C-SEL motivation; P1-02's alternative support; J-2 | **support off `main`: gap** |
| OPRES, `research/opres-20261121` `24702c1d` (#1511, Issue #1509) | P1-05, P1-07; KIN and R-READ used in §0 item 1, §2.1, §4 | **support off `main`: gap** |
| QOPS (#1501) | R-READ's status | **support off `main`: gap** (assumed premise, untraced) |
| I3-SOURCE, `research/i3-source-20261121` `df520f3b` (#1508, Issue #1507) | P1-08, J-2, J-3 | **support off `main`: gap** |
| SMD-CL-1, `research/smd-clustering-20261127` `b7e29ea7` (#1623) | P1-31 to P1-36; §3.1 to §3.5 D-BV/SMD classes; §4 | **support off `main`: gap** |
| FSLICE-PS-1, `research/fslice-premise-sourcing-20261127` `f4bd7b2f` (#1624) | P1-37 to P1-40 | **support off `main`: gap** |
| UN-1, `research/un1-identity-partner-20261127` `4e84b2f2` (#1622) | P1-41, P1-42 | **support off `main`: gap** |
| Kernel modules, Main, A1-FCLASS, SUBSTATE-1/2, F2-1, MECH-1, MR-1, MEAS-Q, UNIV-1, OBS-EMERGE | rows citing them | support on `main` at `13c05b4fe` |
| #1169 c.7079945577 | C-NL hold | provenance |

Before any landing the gaps close in one of two ways. Either the records land: #1622, #1623 and #1624
are prepared for one preservation decision (#1169 c.7209325168), and #1508, #1511 and BIDUAL-DIO
remain off `main`. Or these rows and claims are narrowed to "reported in records not on `main`":
P1-02 (alternative support), P1-05 to P1-08, P1-20, P1-31 to P1-42, §0 items 1, 5, 6 and 7, AW-P1-2,
§3.0 to §3.7, §4, J-2 and J-3.

## 7. Assumption-watch markers

- **AW-P1-1 (windowed finiteness).** As in r1.
- **AW-P1-2 (interface, not cardinality).** Conditional on R-READ and on the P-here transfer of
  §2.1: the representational coherent-control bottleneck is set by R-READ, KIN and Lemma 1, not by
  A1.
- **AW-P1-3 (A5, not A1).** As in r1.
- **AW-P1-4 (retirement removes resources).** As in r1, with PERM restated.
- **AW-P1-5 (vacuum revival).** Linear F_p rules revive a single excitation over the vacuum at
  t = p^k (§3.1, P-here). A low-entropy vacuum and a linear rule do not jointly give an all-time
  sink in the stated cases.
- **AW-P1-6 (law symmetry is conserved).** Equivariant dynamics preserves the symmetry of a law.
  Distinct block values need explicit breaking or a non-symmetric selection, never dynamics alone.

## 8. Stop

The plan's stopping conditions hold for r2. No computation was run. r2 is limited to the review
fixes, the three new records and the four-class classification. Independent delta review is required
before use (§A.46 item 7).
