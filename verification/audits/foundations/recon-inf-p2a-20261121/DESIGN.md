# RECON-INF P2-A: Stage 1 of Theorem 23 without exact return (research design)

**Status.** Research design only, for independent review before any investigation. It contains no
proof, no computation and no new result. It changes no manuscript, Lean file, ledger row, registry
file, Theorem 23 text or #1477 file. Every relation marked ESTABLISHED below is cited from a record
or a kernel statement already on `main`, at the scope that source states.

**Authorization.** Owner decision on #1169,
[comment 7068325638](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7068325638)
(`amaybaum`, 2026-11-21T19:51:15Z), row "RECON-INF Phase 2": "Research planning authorized | Plan
Stage 1, Stage 3 and the cross-stage bridge separately; no proof execution yet". The P2-A line of the
same comment, verbatim: "**P2-A (Stage 1).** Can a weaker finite-observation or history-readback
condition replace exact global return? NU9 orbits, a.e. recurrence and global return stay distinct."
The Phase 2 investigations need a reviewed plan and a separate authorization (same comment, "Order",
item 5).

**Accountability.** Thread #1169; Issue #1531. Input: the Phase 1 audit, PR #1532 at exact head
`0bc9628ab3ee4e6955df8980815ecead869578ee`, files `PLAN.md` and `AUDIT.md` under
`verification/audits/foundations/recon-inf-p1-20261121/` on `research/recon-inf-p1-20261121`
(reviews on #1532: c.7068213461, c.7068281368, c.7068298957). P2-B and P2-C are prepared
independently; this design neither reads nor depends on them.

**Pins.** `main` at `df6da1c6101e811acdc7952d5748aff57028e8ed` (this branch's base and the Phase 1
baseline B1). `Sub:n`, `Main:n`, `GR:n`, `SM:n` are lines of `papers/Substratum.md`, `Main.md`, `GR.md`,
`SM.md` at that commit. Lean paths are relative to `verification/lean-mathlib/OIBridge/`. "P1 row n"
and "P1 §n" refer to the Phase 1 audit at `0bc9628a`. The B2 tree (T0 `5b6d48b5`) is cited only
where P1 cites it.

## 1. Goal and the exact question

**Goal.** Within RECON-INF (#1531, parent thread #1169), determine what Stage 1 of Theorem 23 needs
in place of the finite carrier's exact global return, so that the Stage 1 part of a Phase 3
replacement theorem, if one is ever authorized, rests on a hypothesis whose status is known.

**Question Q-A.** Fix the intended conclusion of Stage 1 at node N1 (§4). Is there a hypothesis
strictly weaker than global exact return `φ^N = id` — in particular one that is testable on a
finite observation window, or one stated in history-readback terms — that suffices for that
conclusion on a carrier of any cardinality? Or does every sufficient hypothesis available on `main`
require a common late-time return property ((R-d), (NR), (RIG) or (CMP) of §2.2), none of which has
a finite-window test?

Each outcome is possible, and so is a third: that the intended conclusion of Theorem 23 consumes no
return property at all, in which case Q-A is answered for Theorem 23 and becomes a question about
the separate corpus statements that do consume one. The design fixes which of these the
investigation will report, and by what rule, before any of it is run.

## 2. What is being replaced, and the candidate hypotheses

### 2.1 Candidate readings of "the intended conclusion"

The phrase is not fixed by any single sentence; four readings occur in the corpus. N1 selects
among them by a consumer trace.

| Code | Reading | Where stated |
|---|---|---|
| IC-O | Stage 1's printed Output: a triple `(S, φ, V)`, `S` finite, whose visible marginal reproduces the supplied law on the finite context, alphabet and horizon, and which satisfies C1–C4 for the M1-T temporal sector | Sub:125–127; status Sub:141 ("Theorem for the scoped finite dilation datum") |
| IC-R | Recurrence-cycle P-indivisibility of the rooted family of a finite representative | Sub:137 ("On a finite representative, a non-permutation rooted map and finite return also give recurrence-cycle P-indivisibility [Main §2.3]"); Main:121–127 (Steps 1–3); Main:137 (history readback + finite recurrence); Sub:44; GR:90 |
| IC-H | The index-free form: the rooted family is not P-divisible on `{0, …, n}` for some `n` | Main:141 ("Without a finite representative the index-free form holds under … (FS) … and … (NR)"); Main:131 (near-return corollary) |
| IC-A | P-indivisibility on an accessible window | Not claimed: Main:141 states that C4 does not force it (XOR control) and Main:638 states that the accessible-timescale claim is non-Markovianity (ii). Listed as a boundary, not a target |

IC-O's output list (Sub:125–127) does not name P-indivisibility; the recurrence sentence at Sub:137
sits in the Derivation. Whether anything downstream consumes IC-R or IC-H is node N1, not an
assumption of this design.

### 2.2 Hypotheses

| Code | Statement | Object it constrains |
|---|---|---|
| (R-c) | Global exact return `φ^N = id` (P1 §3) | Microscopic carrier |
| (PER) | Common a.e. period: `F^N x = x` for μ-a.e. `x` (REC-1 table §2) | Microscopic carrier, under a law |
| (R-d) | Rooted exact return `Γ_N = I` for some `N` (P1 §3; REC-1's (RET)) | Rooted visible family |
| (CMP) | The joint forward orbit of the visible-cell indicators has compact closure in `L²(μ)` (`ObservableRigidity` hypothesis `hcompact`, :275; A1-RIGID-1 Theorem) | Visible partition under an invariant law |
| (RIG) | Visible-partition rigidity: `μ(C_a △ F^{-n_k} C_a) → 0` along some `n_k → ∞` (REC-1 §2) | Visible partition under an invariant law |
| (NR) | One common near-return with margin after an overlap (Main:131; PREMISE-LADDER F11) | Rooted family at one, possibly inaccessible, time |
| (C4r) | A strict increase of row total-variation distance `d_t(a,b) > d_s(a,b)`, `s < t` (`CausalReadback.C4r`, :67) | Rooted family |
| (FO) | **Finite observation.** The observed root-conditional family `P(X_t = · ∣ X_0 = a)`, `t ≤ n`, on an accessible horizon `n`, has no stochastic divisor for some `s < t ≤ n` | Observed law on a finite window |
| (FO-r) | (FO) witnessed by (C4r) at accessible times | Observed law on a finite window |
| (HR) | **History readback.** A readback gap at an accessible order `k`: two positive-probability visible histories with a common endpoint and different next-step laws (C4, Main:78; M1-T, Sub:123) | Observed law on a finite window |
| (ND) | Some visible step is non-deterministic | Observed law |
| (R-a) | Almost-everywhere (Poincaré) recurrence under an invariant probability (P1 §3) | Microscopic carrier, under a law |
| (R-b) | NU9: for the rule `R_q` on `ℤ³`, a single-site seed on a uniform background `c`, `2 ≤ c ≤ q−3`, has an orbit of exact period 10 supported in `{−1,0,1}³` (#1523 at `b9d8ce76`; P1 §3, status C) | Particular configurations |
| (FS) | Full-support visible prior, root drawn independently of the hidden prior (Main:141) | Preparation |
| (P) | Root-shared product prior `μ = ν ⊗ ρ`, `ν(a) > 0` (REC-1 §2; Main:137 "a hidden prior shared by every root") | Preparation |

(R-a), (R-b) and (R-c) are three different properties (owner requirement, P1 §3). No row of §2.3
asserts an implication among them other than the trivial ones from (R-c) that P1 §3 lists.

### 2.3 Logical relations

Labels: **(N)** native — uses only OI's definitions (Main:42–58) and mathematics; **(I)** imported —
uses an empirical or external-physics input, which is named. Standard mathematics (Poincaré, Kac,
Dirichlet) does not make a relation (I). Layer: K = Lean kernel on `main`; P = paper proof in a
reviewed record or a paper on `main`.

**ESTABLISHED**

| # | Relation | Label | Layer and source | Stated limits |
|---|---|---|---|---|
| E1 | (R-c) ⇒ (PER) ⇒ (R-d), the last under domination (D) | (N) | P: REC-1 Prop. 3.6; Main:121 | (D) is implied by (P) (REC-1 Lemma 2.4) |
| E2 | (R-d) at `N`, with `Γ_s` row-stochastic non-permutation, `s < N` ⇒ IC-H on `{0,…,N}` | (N) | K: `ObservableFactorRecurrence.pIndivisible_of_visible_identity_return_nonperm`:68 | Matrix level; the measurable rooted law is not constructed (docstring) |
| E3 | (R-d) ⇔ visible label returns a.e. after `N` | (N) | K: `ObservableMeasureReturn.measuredGamma_eq_one_iff`:83 (both directions in one proof) | ENNReal ratio matrix; positive, finite visible-cell masses; not composed with E2 |
| E4 | (R-d) ⇒ (RIG) under invariance and (P) | (N) | P: REC-1 Prop. 3.6′ | — |
| E5 | (CMP) ⇒ bounded-gap common near-return ⇒ (RIG); with a non-permutation `Γ_s`, ⇒ C4r ⇒ IC-H | (N) | K: `ObservableRigidity.exists_bounded_gap_nearReturn`:280, `exists_pIndivisibleWithin_of_nonPermutation`:358; P: A1-RIGID-1 (review ACCEPT) | Invariant probability; positive cell masses |
| E6 | (RIG) + non-permutation `Γ_s` ⇒ (NR) at large `n_k` ⇒ IC-H | (N) | P: REC-1 Prop. 3.4 | — |
| E7 | (NR) + non-permutation `Γ_s` ⇒ C4r ⇒ IC-H | (N) | P: Main:131; K: `ObservableRigidity.tv_revives_of_nearReturn`:88, `CausalReadback.c4r_implies_pIndivisible`:134 | Normalized root-shared prior |
| E8 | C4r ⇒ IC-H on that horizon | (N) | K: `CausalReadback.c4r_implies_pIndivisible`:134 | Finite `V`, real matrices; no carrier, prior or reversibility |
| E9 | (HR) at order `k` ⇒ some `Γ_s`, `1 ≤ s ≤ k`, non-permutation; (ND) ⇒ the same | (N) | P: REC-1 Prop. 6.1; Main:139 first half | No recurrence, no invariant law |
| E10 | On a finite bijective representative: (ND) ⇒ IC-R | (N) | P: Main:141 ("For every visible prior, a non-deterministic visible step … makes some Γ_s a non-permutation, so the recurrence-cycle indivisibility holds") | Finite representative only |
| E11 | Under (RIG) and (FS): (HR) ⇔ non-permutation `Γ_s` ⇔ IC-H | (N) | P: REC-1 Prop. 6.2, one direction at a time | (b)⇒(c) is the only direction using (RIG) |

**ESTABLISHED negatives (countermodels; each rules out only the class it is built in)**

| # | Non-implication | Label | Source | Class of the countermodel |
|---|---|---|---|---|
| X1 | (R-a) ⇏ (R-d); (R-a) + non-permutation `Γ_1` ⇏ IC-H | (N) | REC-1 node 3 summary, node 4; PREMISE-LADDER F8 | Bilateral Bernoulli shift; infinite-XOR model (normalized invariant law, (P)) |
| X2 | (HR) ⇏ IC-H on a measurable carrier | (N) | REC-1 Prop. 6.2 remark and node 4 | Infinite-XOR model |
| X3 | (HR) ⇏ IC-A, also on finite carriers | (N) | Main:141 (XOR control); Main:638 | Finite XOR family |
| X4 | IC-H ⇏ (R-d); IC-H ⇏ (RIG) | (N) | REC-1 Prop. 3.3 (rotation, IC-H with no identity return); Prop. 3.5 (IC-H, not rigid) | Irrational rotation; shift with majority readout |
| X5 | Every point periodic with unbounded periods ⇏ (R-d) | (N) | PREMISE-LADDER F7 (C−2) | Infinite normalized invariant example C−2 |
| X6 | For the selected update (q prime, α ≠ 0, Haar prior, window readout): (NR), (RIG), (R-d) fail; with lattice-convex windows IC-H fails at every horizon | (N) | NR-1 Prop. 2.3; Thm 3.3 | That update, that prior, those windows; non-convex windows and composite `q` with unit components are open (NR-1 node table) |
| X7 | On a finite carrier no accessible bound on the first identity time or the first IC-R witness | (N) | REC-1 Prop. 5.1 | Finite model, every `K` |

**ASSUMED** (hypotheses of the results above, not adopted by the corpus): (NR) (Main:131 "assumed
… and not adopted"); (FS) (Main:141); the normalized invariant law and (P) of REC-1 (its "contract",
posited); (CMP) (posited where used); the selection of any law on an infinite carrier (REMAINDER R1,
open per P1 §5).

**MISSING** (the targets of §4)

| # | Relation | Node |
|---|---|---|
| M1 | Whether any step of Theorem 23's chain takes IC-R or IC-H as a premise | N1 |
| M2 | On which object Stage 1's return is required: the constructed finite dilation, nature's carrier, or the observed law | N2 |
| M3 | (FO) on the observed law ⇒ IC-H on every faithful realization of any cardinality, and the hypotheses that transfer needs | N3 |
| M4 | Whether E1, read through Stage 1's identification of the supplied law, supplies (FO), or (NR) through almost-periodicity of a finite-dimensional unitary family — (I), importing E1 | N3b |
| M5 | A history-readback strengthening, stated in multi-time terms, that implies (FO-r) | N4 |
| M6 | Whether (R-b) yields (R-d) for some root-shared law: a set `V × supp ρ` of periodic points with a common period bound | N5 |
| M7 | A witness for "(R-d) for the observed law does not give (R-c)" with a non-permutation `Γ_s` (Sub:268 (iii) states it without one; P1 §3) | N6 |
| M8 | A native source of (R-d), (NR), (RIG) or (CMP) for the selected update (LEDGER X-21, status O) | Not a P2-A node; recorded only |

## 3. Literature search (audit Step 4; plan only)

To be done at the start of the investigation, before any node that attempts closure. Each item
records: the exact statement used, its hypotheses, and whether it is (N)-usable mathematics or an
(I) physical import. No result below is claimed for OI here.

1. **Recurrence under a finite invariant measure.** Poincaré recurrence; Kac's lemma (Kac 1947);
   Halmos recurrence and conservativity. Already used at REC-1 §2; recheck only what N3–N6 add.
2. **Infinite-measure ergodic theory** (Aaronson, *An Introduction to Infinite Ergodic Theory*,
   1997; Krengel): conservativity without an invariant probability; whether any return statement
   survives for rooted laws when no invariant probability exists (P7-B Lemma 5.1's setting).
3. **Rigidity and its relatives.** Rigidity sequences and non-recurrence along sequences
   (Bergelson, del Junco, Lemańczyk, Rosenblatt 2014); mild mixing (Furstenberg–Weiss 1978);
   partial rigidity (Friedman); compact vectors and the Kronecker factor (Halmos–von Neumann). Target:
   the exact relation of (CMP), (RIG) and (NR) for a finite partition, and which mixing notions
   exclude each.
4. **Reversible cellular automata on `ℤ^d`.** Curtis–Hedlund–Lyndon (Hedlund 1969); Kari on
   reversibility and its undecidability for `d ≥ 2`; Toffoli–Margolus on invertible CA; Martin,
   Odlyzko and Wolfram (1984) on cycle structure of linear CA; Schmidt, *Dynamical Systems of
   Algebraic Origin* (1995), on Haar-measure mixing of algebraic `ℤ^d` actions. Target: periodic-point
   sets, their measures, and invariant laws supported on them.
5. **Quantum recurrence.** Bocchieri–Loinger (1957); Percival (1961); Hogg–Huberman (1982):
   almost-periodicity of finite-dimensional unitary evolution. Target: N3b, and the exact horizon on
   which E1 is supplied.
6. **Divisibility.** Wolf–Cirac (2008) on dividing channels; Buscemi–Datta (2016) on divisibility
   and monotone distinguishability; Rivas–Huelga–Plenio (2014) review; Breuer–Laine–Piilo (2009);
   Milz et al. (2019); Bengtsson et al. (2005) on unistochastic matrices; Barandes (2023, 2025) on the
   stochastic–quantum correspondence. Target: an exact finite-window test for (FO) and whether a
   unistochastic family can be P-divisible on every window.

**Output of the step.** A table, one row per item: statement, hypotheses, whether it closes or
obstructs a node, and (N)/(I). A node that a literature result settles is closed by citation, and
the result is credited.

## 4. Branch nodes (depth-first, §A.31)

Order: N1 first, because its outcome decides whether Q-A is a question about Theorem 23 or about
separate corpus statements. At each level the decisive branch is taken; the others are recorded as
not entered, with the reason. A node whose outcome favours the framework gets the pressure test
named in it before its verdict is recorded.

### N1 — Consumer trace of IC-R and IC-H (decisive branch; reading)

**Check.** For each step of the chain, record whether IC-R or IC-H (or the CP-indivisibility that
Main:332 derives from P-indivisibility) appears as a premise: Theorem 23 statement Sub:193 and proof
Sub:195; Lemma 23.0 Sub:189–191; Stage 1 Output Sub:125–127 and Derivation Sub:137; Stage 2
Sub:143–173; Stage 3 Sub:175–185 and GR §3 (GR:58–156), including GR:90's "by either route of
[Main, §3], admits a fixed-basis unitary quantum representation"; the Critical-dependencies list
Sub:106–117; and Main §3.4's characterization theorem as Stage 1 cites it. Book mirrors are searched
for the same sentences (§A.19), read only.

**Decision rule.**
- If no step takes IC-R, IC-H or CP-indivisibility as a premise: record "Theorem 23's conclusion does
  not consume a return property; Stage 1's return enters only the statements S1…Sk", listing them
  with `file:line`. Q-A is then answered for Theorem 23 at IC-O, and N2–N6 run on those statements.
- If some step takes one as a premise: record the step and the reading it uses, set the intended
  conclusion to that reading, and run N2–N6 on it.
- If a step's text is ambiguous between the two, record both readings and run N2–N6 on the
  stronger one.

**Pressure test (the first outcome favours a shorter scope).** Before recording it: (a) check that
GR:90's representation route is the universal one of Main §3.4 (Sub:137, "The representation step is
universal"), and not one that needs indivisibility; (b) check that C4 and C2 (Main:72–78) are not
defined through P-indivisibility; (c) check whether the B2 scope sentence (T0 Sub:216, D026, "used by
Stage 1's exact return") names a consumer or only a location; the owner's D026 decision ("Keep the
finite scope for now; name Stage 1's return … explicitly as finite-dependent") is reported against,
not changed.

**Outputs.** NEW if the first outcome survives the pressure test and no record on `main` (P1, REC-1,
PREMISE-LADDER, LEDGER X-20/X-21) states it; otherwise CONFIRMING.

### N2 — Which object carries the return (algebra and reading)

**Check.** Three objects: (O1) the finite dilation that Main §3.4 constructs per horizon
(`Equivalence.finite_horizon_equivalence`:462; Main:60 "a finite hidden space is constructed, not
assumed"); (O2) nature's carrier, with `A^{ℤ³}` as the reference frame of P1 §0; (O3) the observed
law on its finite horizon. For the statements fixed at N1, record which object each quantifies over.

**Decision rule.**
- If a statement concerns O1: (R-c) holds there by construction (E1, finite carrier), so the
  statement needs no hypothesis on O2. Record, from E10, whether it holds for every dilation of every
  law with a non-deterministic step; if so, record that it carries no information about the supplied
  law beyond (ND), and that its witness times may lie beyond the horizon on which the dilation is
  matched to data (X7).
- If it concerns O2: record it as a question about nature's carrier, and hand the identification of
  O1 with O2 to P2-C (P1 row 53) without deciding it here. Only E-, X- and M-rows run on O2.
- If it concerns O3: carry it to N3.

**Control.** On a finite carrier with the uniform law, each conclusion must reduce to Main:121–127
and Main:137 (the A1-preserved control of REC-1 §3, K1–K5).

### N3 — Finite observation (FO) (algebra; decisive for "finite-observation")

**Check.** State and prove or refute on paper, in a later authorized phase: under (FS) and a hidden
prior independent of the root, the rooted rows `Γ_t(a, ·)` of every faithful realization, of any
carrier cardinality, equal the observed conditionals `P(X_t = · ∣ X_0 = a)` for `t ≤ n`; hence (FO)
on the observed law gives IC-H for every such realization (via E8 when (FO-r) holds, or directly
from the definition of P-divisibility).

**Decision rule.**
- If the equality holds under exactly (FS) and root independence: record (FO) ⇒ IC-H, (N), carrier
  free, and record (FS) and root independence as the transfer's hypotheses (assumption-watch AW-1
  below).
- If it fails when the hidden prior is correlated with the root (Main:52, "a joint preparation may
  already correlate the two sectors"): record the countermodel and the hypothesis it shows to be
  load-bearing.
- If (FO) is shown to be equivalent to IC-H on the window (both directions, §A.34: two separate
  witnesses), record that (FO) is a restatement and credit it as CONFIRMING, not as a weaker
  hypothesis.

**Productivity guard.** (FO) ⇒ IC-H on the same window is close to the definition. The node counts
toward the productivity test (§6) only through the transfer hypotheses it exposes, not through the
implication.

### N3b — Does E1 supply (FO) or (NR)? (citation and algebra; (I))

**Check.** Read Sub:137 and Main §3.4 for how the supplied law relates to unitary data: whether the
rooted family is the unistochastic family `Γ_t(a,b) = |⟨b|U^t|a⟩|²` of one finite-dimensional
unitary `U`, or a sequentially measured multi-time law. If the former, apply the almost-periodicity
of `t ↦ U^t` (§3 item 5): for every ε, infinitely many `t` have `‖U^t − I‖ < ε`.

**Decision rule.**
- If the identification is the unistochastic one and E1 is supplied at the times used: record
  (NR) for the observed family, hence IC-H with a non-permutation `Γ_s`, as (I), importing E1
  (unitary evolution of a finite-dimensional visible system) at those times.
- If E1 is supplied only on a finite horizon shorter than the near-identity times: record that the
  route needs E1 beyond the observed horizon, an extrapolation, and credit nothing.
- If the identification is the sequentially measured law: record that this route does not apply.

**Pressure test (favourable outcome).** Before crediting the first outcome: check whether the
near-identity times are bounded independently of the eigenphases (they are not in general; Dirichlet
gives only existence), and whether Stage 1's horizon is fixed before or after the law is supplied.

### N4 — History readback (HR) and its strengthening (algebra, then a future computation)

**Established at entry.** E9 (HR gives a non-permutation map), X2 (HR does not give IC-H on a
measurable carrier), X3 (HR does not give IC-A). So (HR) alone does not suffice for IC-H or IC-A;
this is not re-tested.

**Check.** Define a root-level readback (RR): for roots `a ≠ b` and accessible `s < t`, the visible
law at `s` does not separate `a` from `b` as well as the law at `t` does, the separation being
carried by the hidden sector. Determine whether (RR) is (C4r) at accessible times, and whether any
condition stated in multi-time (C4-type) terms implies it.

**Decision rule.**
- If (RR) coincides with (C4r) at accessible times: record (RR) ⇒ (FO-r) ⇒ IC-H on the window (E8),
  (N), and record (RR) as the readback condition that suffices; state it as strictly stronger than
  (HR) (X3).
- If a multi-time condition implying (C4r) is found: record it with its proof layer.
- If an exact countermodel is found to every candidate condition tried: record the countermodels;
  do not state that no readback condition suffices.

**Future computation (bounded; only after authorization).** Exhaustive exact enumeration over
bijections of `C_V × C_H` at `(|C_V|, |C_H|) ∈ {(2,2), (2,3), (3,2)}`, uniform and point-mass hidden
priors, horizons `n ≤ 4`, classifying each law by (HR) order, (C4r), and P-divisibility on
`{0,…,n}`.
- *Exactness.* Rational arithmetic throughout. P-divisibility is decided by an exact rational
  divisor `Λ` with `Γ_t = Γ_s Λ` verified entrywise, or, for indivisibility, by an exact witness: a
  (C4r) pair, or a rational Farkas certificate for the infeasibility of the divisor's linear system,
  verified exactly. No floating-point verdict.
- *Control (positive).* The swap `φ(v,h) = (h,v)` at `(2,2)`, uniform prior: `Γ_1 = J/2`,
  `Γ_2 = I`, (C4r) at `(1,2)`; must classify as IC-H.
- *Countercontrol.* The XOR family of Main:638 (X3): must classify as (HR) at order 2 with no
  indivisibility on its window. The uncoupled realizations of the C1/C4 minimality audit must
  classify as P-divisible.
- *Control of the classifier itself.* Main:119's monotone-but-indivisible pairs (`translation_probes.py`)
  must classify as P-indivisible without (C4r); this checks that the divisor test, not the
  monotonicity test, decides.
- *Rule.* A verdict is printed only when all controls pass, and its text is generated from the
  counts. A counterexample found is a universal negative for the implication it refutes; no
  counterexample is reported as "none at the sizes tested", not as a theorem.

### N5 — NU9 periodic orbits (R-b) and rooted return (future computation; conditional on #1523)

**Dependency.** #1523's result is status C (P1 §3, (R-b): hand re-derivation and delta check
confirmed; exact re-run pending; not owner-accepted). N5 runs only after #1523's status is settled,
and its verdict carries that status.

**Check.** The rooted convention needs, for one hidden prior ρ shared by every root, that every
`(a, h)` with `a ∈ V` and `h ∈ supp ρ` is periodic, with a common period bound `B` (PREMISE-LADDER
F6; F7 shows that unbounded periods do not suffice). NU9 asserts one orbit per background, from one
seed. Determine, for a window `W` and a finite set of hidden configurations near the NU9 seed, whether
all `|V|` window fillings are periodic with bounded period.

**Decision rule.**
- If a product set `V × supp ρ` of periodic points with a common bound `B` exists: record that a
  root-shared law with (R-d) at `N = lcm(periods)` exists for `R_q`, and, if some `Γ_s`, `s < N`, is
  not a permutation, that IC-H holds for that law (E2). Status C, inheriting #1523. Record that the
  selection of this law is open (REMAINDER R1) and that its relation to the Haar-type laws of Lemma U
  is not addressed.
- If some window filling leaves the periodic set or has no period within the search bound: record
  "no such product set found for `R_q` at the windows and backgrounds tested", for that construction
  only.

**Future computation (bounded).** Exact integer simulation of `R_q` from finitely supported
perturbations of a uniform background on `ℤ³`, with exact configuration comparison and a bound on
support radius and time.
- *Positive control.* Reproduce NU9's period-10 orbit with support in `{−1,0,1}³` at one admissible
  `(q, c)`.
- *Countercontrol.* The selected linear update with `q` prime, `α ≠ 0`: no nonzero finitely
  supported state has a finite orbit (R1-INF Lemma 4 (a), delta review outstanding). The tool must
  report no period for every such start within the bound.
- *Exactness control.* Run each orbit forward `N` steps and backward `N` steps with the inverse
  rule; the start must be recovered exactly (§A.21: the simulated operation preserves reversibility).
- *Rule.* As N4. A period is reported only when exact equality is observed.

### N6 — Separation of (R-c) from (R-d) and of both from IC-H (algebra)

**Check.** Take a finite system with a non-permutation `Γ_1` and `Γ_N = I` (the `(2,2)` swap) and
adjoin a decoupled, independently prepared factor with no periodic point of positive measure (an
irrational rotation or a Bernoulli shift with its invariant law). By the product-dynamics statement
of Main:60 and Theorem 24 (iii), the rooted family is unchanged.

**Decision rule.**
- If the computation confirms that the rooted family is unchanged and (R-c) fails: record the
  witness for "(R-d) ⇏ (R-c), with a non-permutation `Γ_s`" (fills M7), (N), ELABORATING.
- Together with X4 (IC-H without (R-d)), record the chain "(R-c) ⇒ (R-d) ⇒ IC-H, neither converse",
  each direction with its own witness (§A.34).
- If the adjoined factor changes the rooted family: record where the product-dynamics statement
  fails and stop the node.

### Nodes not entered at design time

- (R-a) as a route to IC-H: closed by X1. It is not re-tested; it stays a separate row.
- A native source of (R-d), (NR), (RIG) or (CMP) for the selected update (M8, X-21): X6 rules these
  out for prime `q`, `α ≠ 0`, Haar prior and (for IC-H) lattice-convex windows. Non-convex windows
  and composite `q` (NR-1 node table: (C4r) "holds at a lattice-independent time when α is a nonzero
  nilpotent in some primary component", with witnesses "not credited") are listed as a possible
  later node if N1 makes IC-H the intended conclusion and N2 places it on O2. Entering it needs its
  own preregistration.

## 5. Invariant→checkpoint table (§A.41)

| # | Invariant asserted of the execution | Checkpoint that measures it |
|---|---|---|
| V1 | Read-only on manuscripts, Lean, ledger, registry, Theorem 23 and #1477 files | `git diff --stat origin/main` at every commit lists only files under `verification/audits/foundations/recon-inf-p2a-20261121/` |
| V2 | Decision rules fixed before execution | The commit adding this file precedes every execution commit; each verdict cites the rule by node number at that commit |
| V3 | (R-a), (R-b), (R-c) kept distinct | A review pass lists every sentence naming two of them and checks that each implication between them cites a source (P1 §3 lists the only trivial ones) |
| V4 | Each ESTABLISHED row matches its source's scope | Every row's `file:line` is read at `df6da1c6`; each limit in the "Stated limits" column is quoted from the source |
| V5 | Computational verdicts only over green controls | Each computational node writes its control results before its verdict; a failed or vacuous control voids the verdict |
| V6 | Exact claims certified exactly | Every P-divisibility or periodicity verdict carries an exact rational divisor, an exact certificate, or an exact configuration equality |
| V7 | Directional witnesses for each equivalence (§A.34) | Each "⇔" recorded has two named witnesses, one per direction |
| V8 | Negative results scoped to the construction ruled out | Each negative sentence names its class (carrier, law, prior, window, rule, sizes); reviewer check |
| V9 | Status of off-main inputs carried | Every citation of R1-INF carries "delta review outstanding"; #1504 and #1523 carry status C; grep before each commit |
| V10 | No (I) input recorded as (N) | Each relation row carries its label, and each (I) row names the import (E1, etc.) |
| V11 | Productivity test applied as fixed | §6 is quoted unchanged in the result; each node's class is assigned against it |
| V12 | Bounded local work (§A.40) | N4 and N5 computations run only after authorization, with stated size bounds; any run beyond those bounds moves to CI or stops with the partial state published |

## 6. Productivity test (fixed before any node is run)

A node's outcome is a **gem** iff it yields a fact strictly stronger than the obvious restatement
**and** either constrains something (the scope of a step of Theorem 23, the D026 sentence, or a
corpus statement carrying IC-R or IC-H) or exposes a hidden assumption.

Obvious restatements, which do not count: that (R-c) is sufficient and not necessary for (R-d)
(P1 §3); any row E1–E11 or X1–X7; that (FO) on a window gives IC-H on that window; that (HR) gives a
non-permutation map. The propagation bar is better-than-coherence; below it, record only.

Output classes (§A.31): NEW / POSITIVE / ELABORATING / CONFIRMING / BORDERLINE.

**Assumption-watch markers opened by this design.**
- **AW-1 (root-shared prior).** The rooted family is defined with one hidden prior shared by every
  root (Main:137). Its identification with observed conditionals needs that convention and (FS).
  Any claim transferring a rooted-family property to observed data inherits AW-1. To be checked at
  N3 and carried to P2-C if it bears on O2.
- **AW-2 (horizon of the supplied law).** Stage 1 takes the law on a finite horizon (Sub:137). Any
  route that uses the law at later times (N3b) extrapolates E1 beyond the observed horizon.

## 7. Stop conditions

1. **N1 settles the scope.** If N1's first outcome survives its pressure test, Q-A is answered for
   Theorem 23; N2–N6 run only on the statements N1 lists, and the result says so.
2. **Fixed point.** Stop when 3–4 consecutive passes over the open nodes yield no NEW finding.
3. **Beyond planning scope.** Any node that needs a proof beyond elementary algebra and citation, a
   Lean change, or a computation beyond the bounds of N4/N5 stops with its partial state and a
   request for authorization.
4. **Missing dependency.** If #1523's status, R1-INF's delta review or a cited record changes, the
   dependent node is parked with the named gap.
5. **Provenance.** Any unaccounted file in the work area halts work under §A.26 until swept.

## 8. What counts as a negative result

Stated only for the construction ruled out:
- "For [carrier, law, prior, readout], hypothesis H does not give [IC-x]": a countermodel in that
  class, verified exactly. It does not rule out other laws, readouts or observer-level extensions.
- "No product set of periodic points with a common bound was found for `R_q` at [windows,
  backgrounds, bounds]": a finite search, not an impossibility statement.
- "Theorem 23 consumes [IC-x] at [step]": a reading at `df6da1c6`, which does not determine whether
  a replacement theorem must.

A negative result is progress of the same kind as a positive one (§A.29) and is recorded with the
same care. No negative result here bears on nature's carrier unless the node states O2 and cites
the construction.

## 9. Out of scope

- No proof is executed and no computation is run under this design; N4 and N5 describe future
  computations that need separate authorization.
- No change to any manuscript, to Theorem 23, to the #1477 plan or its frozen files, to any LEDGER
  row, to any Lean module or to the census registry.
- No decision on D022 or D026; N1's outcome is reported for the owner's review of D026.
- Stage 3 (P2-B) and the identification of Stage 1's process with the lattice dynamics (P2-C).
- Physical selection of a law on an infinite carrier (REMAINDER R1) and a native source of a return
  condition (LEDGER X-21).

## 10. References outside `main` (§A.42 item 8)

| Reference | Used for | Classification |
|---|---|---|
| PR #1532 at `0bc9628a` (`PLAN.md`, `AUDIT.md`) | Phase 1 input | Provenance; read only; confirmed draft |
| #1523 at `b9d8ce76` | (R-b), N5 | Provenance; status C |
| T0 `5b6d48b5`, ledger edit D026 | N1 pressure test (c), as P1 cites it | Provenance; read only |
| #1169 c.7068325638 | Authorization | Quoted with author and time |
