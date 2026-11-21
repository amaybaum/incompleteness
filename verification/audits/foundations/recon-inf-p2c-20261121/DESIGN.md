# RECON-INF P2-C: cross-stage compatibility in Theorem 23 (research design)

**Status.** Research design only. It executes no proof, runs no computation, and changes no
manuscript, Theorem 23, #1477 file or plan, ledger, registry or Lean file. Every node below is a
planned investigation with a preregistered decision rule; none has been run. The design needs an
independent review before any node is authorized.

**Authorization.** Owner decision on #1169,
[comment 7068325638](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7068325638)
(`amaybaum`, 2026-11-21T19:51:15Z): "RECON-INF Phase 2 | Research planning authorized | Plan Stage 1,
Stage 3 and the cross-stage bridge separately; no proof execution yet", with "**P2-C (cross-stage).**
Can Stage 1's observable process arise from the same infinite lattice dynamics that Stage 2
selects?", and the order "the Phase 2 designs, prepared independently", then "Phase 2
investigations, only after their plans are reviewed". The owner's scope for this unit: "Determine
whether the observable process in Stage 1 can arise from the same infinite lattice dynamics selected
in Stage 2, rather than from a separately constructed reversible system."

**Goal link.** Thread #1169 (RECON-INF); Issue #1531 (Phase 1); Phase 1 audit PR #1532, confirmed at
`0bc9628ab3ee4e6955df8980815ecead869578ee` (reviews #1532 c.7068213461, c.7068281368, c.7068298957).
This design takes up the seam that audit records as open in both settings: AUDIT row 53 (the
Stage 1 → Stage 2 identification), row 52 (SM:66), §4.2 "The seam", §5 (O), and O-A4 row 2.

## 0. Sources and notation

**Pin.** `main` at `df6da1c6101e811acdc7952d5748aff57028e8ed` (B1 of the Phase 1 audit). `Sub:n`,
`Main:n`, `SM:n`, `GR:n`, `Str:n` are lines of `papers/Substratum.md`, `Main.md`, `SM.md`, `GR.md`,
`Structure.md` at the pin. The retirement plan P* of #1477 shifts `Main:45` onward by `+2` and leaves
`Sub:94` onward, SM, GR and Structure unchanged (Phase 1 AUDIT §0); this design cites B1 only and
assumes no P* edit has landed. Lean paths are relative to `verification/lean-mathlib/OIBridge/`.

**Records cited** (paths under `verification/audits/foundations/`, standing as each record states it):

| Short name | Path | Standing |
|---|---|---|
| P1-AUDIT | `recon-inf-p1-20261121/AUDIT.md` at `0bc9628a` (PR #1532, not on `main`) | Confirmed by delta check (#1532 c.7068298957); kept as a reviewed draft by owner decision |
| O-A4 | `o-a4-20261120/RESULT.md` | Merged in #1441; accepted (P1-AUDIT §0) |
| NR-1 | `nr1-near-return-20261116/NR-1.md` | Review ACCEPT WITH CHANGES; delta CONFIRMED WITH NITS |
| A1-01 | `a1-free-p12b-observer/TRACE.md` | Trace record; its first row and row 2b are cited for the open seam only |
| R1-INF | `r1-inf-20261119/RESULT.md` | Delta review outstanding; cited only as O-A4 row 3 cites it, each time marked "(delta review outstanding)" |

**(N)/(I).** A relation or result is (N) when it is proved inside the corpus from OI's own definitions,
and (I) when it imports a result or a premise from outside; imported items are named. A relation not
yet proved carries neither label; its row names what a proof would import.

## 1. The question

**Q.** Let `P` be a law Stage 1 takes as input: a finite-horizon visible law on a finite alphabet for
one finite experimental context, in the M1-T temporal sector (Sub:123, :137). Does `P` arise as the
law of a finite readout of the lattice dynamics that Stage 2 selects (Sub:157–159; SM:224), under a
preparation law that is itself part of that same system, or does Stage 1's output exist only as the
separately constructed finite dilation of Main §3.4?

Either answer is a result. A positive answer would supply the identification that P1-AUDIT row 53
records as missing, at the stated scope. A negative answer for a stated class of dynamics,
readouts and preparations would show that Theorem 23's Stage 1 and Stage 2 describe different
systems in that class, and would bound what a replacement theorem can claim. Neither outcome is
preferred, and none of the decision rules below encodes an expected outcome.

The M1-B Bell sector is outside Q. Its one-object compatibility is the open hypothesis H-Bell
(Sub:131–133, :171–173), and the Bell–lattice obstruction (Main:420) already excludes realizing it
on the reference cone. P2-C addresses the M1-T temporal data only.

## 2. The objects and the relations to be decided

### 2.1 What Stage 1 constructs

- **Input.** A law `P = P_K` on visible trajectories `C_V^{K+1}` for one context, finite `C_V`, finite
  horizon `K` (Sub:137). Its empirical source is E1 (I).
- **Output.** A triple `R₁ = (S, φ, V)` with `S = C_V × C_H` finite, `φ` a bijection, and a hidden prior
  `μ_H` independent of the visible initial state, whose visible marginal from `P₀ ⊗ μ_H` is `P`
  (Sub:125, :137; Main:526, process dilation; Main:528, response-table form for arbitrary kernels).
  The Lean form `Equivalence.S_imp_D`:422 uses a joint initial law on `V × Hid` (its docstring, and
  A1-01 first row); the independent-prior form is the paper theorem. Both are (N).
- **Non-uniqueness.** `R₁` is one realization among many. The Stage-1 gauge statement (Sub:139) is
  scoped to "the finite channel/dilation datum actually used"; equal channel families need not have
  conjugate dilations (Sub:139; Str:669–683, Proposition 9.7b and Corollary 9.8). The canonical
  predictive quotient `T(P)` (Main:632) is the terminal object of the category of faithful
  realizations: every faithful realization `R` of `P` carries a unique visible-preserving,
  dynamics-intertwining morphism `q_R : R → T(P)` on its prior-supported reachable part, and the
  hidden fibres above `T(P)` are not unique (`fiber_freedom`). Stated there for realizations on
  `C_V × C_H`, certified exhaustively at small finite sizes. (N)
- **Site structure.** `R₁` carries no product decomposition into sites. Site factorization is posit
  (viii) (Main:736): the dynamics has not been shown to select it, and the coupling graph is read
  relative to it; SM:68 gives a normal-mode identification of the four-site ring over ℤ/3 with
  coupling-graph degree 1 against 3 for the spatial identification.

### 2.2 What Stage 2 selects

- **Dynamics.** Within A3–A6, the nearest-neighbour premise and the second-order form (xiii)
  (Main:736), the update `Φ_{q,α}: (p, c) ↦ (c, αSc − p)` on `Ω = (ℤ_q × ℤ_q)^Λ`, `S` the
  nearest-neighbour sum (Sub:159; SM:224, form lemma). `q` and `α` are not fixed on `main` (NR-1:101; SM:230).
- **Carrier.** Setting (Z): `Λ = ℤ³` (SM:222; A4 at Sub:98 as the standard construction). Setting (F):
  a finite periodic quotient `ℤ³/P` under the wrapping conditions on `P` (Sub:98; SM:222; O-A4 §7).
- **Reference law.** H-μ(φ,Θ): a normalized law invariant under the update and the reversal, with
  product form `u_V ⊗ ν` at the visible window (O-A4 §2). On (Z) the uniform Bernoulli (Haar) law
  `β` satisfies it for every second-order rule over a finite abelian group (O-A4 Lemma U). On (F)
  the counting law (Main:54, Lemma 3).
- **Readout.** The corpus readouts of the lattice model are window readouts: "the visible sector
  being the sites of a region R" (Main:297), and NR-1's (R), `π = (u, v)|_W` (NR-1:104). SM's
  observer branch uses linear projections on Koopman observables (SM:242, Theorem 1a).

### 2.3 Classes the nodes range over (frozen here)

- **Readout classes.** (R-win) the full window phase state `(p, c)|_W`; (R-win-c) the current
  component `c|_W` only; (R-lin) any group homomorphism of the window phase state; (R-nl) any function
  `g` of the window phase state. Each is a finite readout region (FR).
- **Preparation classes.** (Π-β) the reference law conditioned on a finite apparatus record: `β(· | E)`
  with `E` a cylinder event at some finite set of sites and times; (Π-H) `P₀ ⊗ (hidden marginal of β)`,
  the visible initial law times the reference law on the hidden coordinates; (Π-prod) `P₀ ⊗ ν` with `ν`
  any law on hidden coordinates; (Π-joint) any law on `Ω`.
- **Target classes.** (𝒫-rat) laws with rational conditional kernels; (𝒫-Q) finite-horizon laws of
  fixed-basis sequential measurements of a finite-dimensional unitary system (the class `Q_fb`,
  Main:556); (𝒫-mem) laws in (𝒫-Q) with `M_t > 0` at an accessible order (the M1-T sector).
- **Exactness.** (ex) equality of the laws on `C_V^{K+1}`; (ε) total-variation distance at most `ε`.

### 2.4 Relations

Each relation is stated for a target `P` at horizon `K` and is read in setting (F) or (Z).

| Id | Relation | Status | (N)/(I) | Imported or named assumptions |
|---|---|---|---|---|
| J0 | `P` is the visible marginal of some finite reversible realization with independent hidden prior | Established | (N) | E1 for the input law; Main:526–528 |
| J1⁰ | `P` is the readout law of some reversible finite-range cellular automaton on a lattice, with no constraint from A3–A6 | Missing as a stated result; Node 2 tests whether it is vacuous | — | — |
| J1 | As J1⁰, for a translation-invariant, centre-free, reversible finite-range rule (A2, A3, A4), with a readout and preparation in stated classes | Missing | — | A2–A4, (viii) |
| J2 | `P` is the readout law of `Φ_{q,α}` for some `q, α`, some readout class and some preparation class | Missing | — | A2–A6, nearest-neighbour premise, (xiii), (viii) |
| J3 | J2 with the preparation in (Π-β) or (Π-H): the preparation is generated by the reference law Stage 2 uses | Missing | — | As J2, plus H-μ(φ,Θ), and the Stage 3 measure (interface to P2-B, §6) |
| J4-fac | Stage 1's finite `(S, φ)` is a measure-theoretic or topological factor of `(Ω, Φ_{q,α}, β)`, with the window readout factoring through it | Missing | — | As J3 |
| J4-emb | Stage 1's finite `(S, φ)` is the restriction of `Φ_{q,α}` to a finite invariant subset of `Ω` (for example the `P`-periodic configurations), with `V` the window | Missing as a stated identification | — | As J2 |
| J5 | A realization of `P` by `Φ_{q,α}` (J2) carries a morphism of realizations in the sense of Main:632 onto Stage 1's datum | Missing; Node 7 | — | Main:632; its extension to an infinite measurable carrier |

**"One and the same system".** For this design the identification Q asks for is J3 at the stated
exactness, together with the transfer of Stage 1's conclusions to the realizing lattice system
(Node 8). J2 without J3 gives a lattice realization that uses a preparation unrelated to the law
Stage 2 and Stage 3 use; J4 is a stronger, dynamical identification. J0 alone is the separately
constructed system the owner's question contrasts with. A shared ingredient (for example that both
Stage 1's dilation and Stage 2's lattice are reversible, or both carry a finite visible window) is not
an identification; only an explicit relation of the table counts.

### 2.5 Implications between the relations and their witnesses (§A.34)

No equivalence between the relations is asserted. Each implication is listed one direction at a
time with the witness it needs.

| Direction | Witness needed | Standing |
|---|---|---|
| J3 ⇒ J2 ⇒ J1 ⇒ J1⁰ | Class inclusion; `Φ_{q,α}` satisfies A2–A4 (SM:224; Lean `WaveSubstratumUnbounded.waveZ_A2`–`waveZ_A5`:45–70 for the wave rule on `Fin d → ℤ`) | Inclusions by definition; the Lean anchors cover A2–A5 for the wave rule, to be checked against the readout and preparation classes in Node 1 |
| J1 on (F) ⇒ J0 | A torus realization with a product preparation is a finite reversible realization with independent hidden prior | By definition for (Π-H), (Π-prod); (Π-β) and (Π-joint) need the independence form checked (Node 1) |
| J2 on (Z) ⇒ J2 on (F), side `L` large | Light-cone agreement for multi-time laws under the preparation class (Node 3) | Missing. NR-1 Prop. 4.1 proves it for the rooted maps under the uniform prior only |
| J2 on (F), side `L` large ⇒ J2 on (Z) | Lift of the torus preparation to a law on `Ω` with the same light-cone marginal (Node 3) | Missing; a separate witness from the previous row |
| J4-fac ⇒ J2-type law equality | Pushforward of `β` under the factor map with the readout compatibility `π_V ∘ π = readout` (Node 6) | Missing |
| J4-emb ⇒ J2 with a preparation supported on the invariant subset | Restriction | By definition, once J4-emb is stated |
| J2 on (F) ⇒ J5 onto `T(P)` | Main:632, universality clause, for finite carriers | Established on (F) for the morphism to `T(P)` (N); its extension to (Z) is Node 7 |
| J0 ⇒ J2 | None known; Nodes 4 and 5 test it | Not asserted |
| J5 ⇒ J4 | None known | Not asserted |

The existing equivalences the design leans on keep their directional witnesses: `S ⇔ D ⇔ Q_fb`
(Main:556; `S_imp_D`:422, `D_imp_Qfb`:294, `Qfb_imp_S`:245, assembled in
`finite_horizon_equivalence`:462), and the all-time rooted classification (Main:650;
`pper_of_finiteRootedRealizable` forward, `pper_has_responseRealization` converse).

## 3. Literature search (plan only; run before any closure attempt, Step 4)

Each query records: the source, the exact statement found, its hypotheses, and whether it decides a
node, bears on it, or shows the node to be known hard. A node closed by citation states the scope
of the cited theorem and checks that the cited hypotheses hold for `Φ_{q,α}` and the classes of §2.3.

| # | Topic | Target node | Starting points to check |
|---|---|---|---|
| L1 | Factor maps, conjugacy and simulation between cellular automata and subshifts; intrinsic universality of reversible CA | 2, 6 | Hedlund (1969); Lind and Marcus, *An Introduction to Symbolic Dynamics and Coding*; Kůrka, *Topological and Symbolic Dynamics*; Toffoli (1977) and Morita on universality of reversible CA; Durand-Lose on intrinsic universality of reversible CA; Kari's block-permutation representation of reversible CA; Delorme, Mazoyer, Ollinger and Theyssier on bulking |
| L2 | Ergodic properties of linear (additive) CA over `ℤ_q`: invariance of Haar measure, ergodicity, mixing, spectrum | 4, 6 | Hedlund (1969); Willson (1975); Cattaneo, Formenti, Manzini and Margara on ergodicity of linear CA; Pivato's survey of the ergodic theory of CA; R1-INF Prop. 5 (delta review outstanding) |
| L3 | Finite factors of weakly mixing systems; eigenfunctions; Rokhlin lemma; generator and model theorems | 6 | Standard texts (Walters; Petersen); Krieger's generator theorem; Jewett–Krieger; Sinai's factor theorem and Ornstein theory, for factor relations onto finite-alphabet processes |
| L4 | Stinespring and dilation uniqueness; classical dilations of stochastic processes | 7 | Stinespring (1955); Paulsen's text; Str:660–683 (Propositions 9.7a, 9.7b, Corollary 9.8) |
| L5 | Minimal predictive models and their universality (causal states, ε-machines, generative models) | 7 | Crutchfield and Young (1989); Shalizi and Crutchfield (2001); Löhr and Ay on generative complexity; Upper on hidden Markov models; compare with Main:632 |
| L6 | Stochastic processes as readouts of deterministic or reversible CA with random initial data; probabilistic CA as factors of deterministic CA with noise | 2, 5 | Mairesse and Marcovici's survey on probabilistic CA; Egri et al. (Main reference [64]) for system–ancilla realizations |
| L7 | Embeddings of finite reversible systems into reversible CA on `ℤ^d`; embedding theorems for subshifts | 2, 6 | Krieger's embedding theorem; Boyle's lower entropy factor theorem; block (Margolus) constructions |
| L8 | Locality and light-cone reductions; quasilocal completions and automorphisms | 3, 7 | GR:279–286 (region completion, kernel `QuasilocalCharacterization`); Schumacher and Werner on reversible quantum CA |

**Decision rule for §3.** A node whose question a located theorem decides is closed by citation, at
the theorem's scope, before any proof or computation is planned for it. A node that the literature
shows to be open or known hard is parked with the named gap. A node with no located source proceeds
as planned. The search result is recorded per query, including null results.

## 4. Branch nodes (depth-first, §A.31)

The walk is depth-first. Each node is closed by its decisive check and records its verdict before
the next node opens. The order selects first the branches that decide which relation is the target
(Nodes 1–2), then the branch closest to the owner's question, the reference law Stage 2 uses
(Node 4), and only then the wider preparation classes. A branch outcome favourable to the
identification receives the pressure test of §A.31 before acceptance.

**Common rules for every computational node.**
- Verdicts are generated from the measurements and printed only over green controls; a verdict over
  a failed, vacuous or self-reproducing control is void (§A.29).
- Exact claims (equality of laws, zero distance, feasibility or infeasibility, rank) are certified in
  exact rational or finite-field arithmetic. Floating point never certifies them.
- Each run is deterministic and replayable: parameters, seeds and outputs are recorded in full
  precision and a replay must match elementwise (§A.26 item 3).
- Cost is classified before the run (§A.40): small exact enumerations run locally; anything larger
  is planned for CI and run only after authorization.
- Each negative verdict states its full scope: dynamics `(q, α)`, readout class, preparation class,
  target class, setting (F) or (Z), and exactness (ex) or (ε).

### Node 1 — Freeze the relations against the corpus (reading)

- **Check.** Re-read Sub:121–173, Main:526–562, :614–650, SM:64–68, :220–244, Main:292–297 and NR-1 §2
  against the classes of §2.3. Determine: (i) which readout classes the corpus's lattice readouts
  belong to; (ii) whether the visible alphabet size of each readout class can match the target's
  `|C_V|` (for (R-win) it is `q^{2|W|}`, for (R-win-c) `q^{|W|}`); (iii) whether each preparation class
  has the independence form Stage 1 uses (Main:526) or only the joint form of `S_imp_D`.
- **Decision rule.** Node 1 is complete when every relation J0–J5 has a statement with explicit
  quantifiers over `(q, α)`, readout, preparation and target, and every implication of §2.5 has a
  named witness or the entry "Missing". A class that cannot meet the target alphabet size is
  recorded as excluded for that target by counting, with the count shown, and is not carried
  further for that target.
- **Output class.** Definitions only; no verdict on Q.

### Node 2 — Is lattice realization without the Stage 2 constraints vacuous? (J1⁰, J1)

- **Hypothesis under test.** Every finite-horizon law is J1⁰-realizable by a construction that carries
  no Stage 2 content, so J1⁰ cannot by itself identify the systems.
- **Check.** Paper construction, one per class: (a) J1⁰: a range-0 rule acting as `φ` on a site
  alphabet `C_V × C_H`, identity elsewhere; (b) J1: the same question inside A2–A4, including A4's
  no-self-input clause (Sub:98), for example a second-order rule `x(t+1) = F(x(t)) − x(t−1)` with a
  non-linear `F` (reversible for every `F`, SM:106) whose hidden coordinates feed a window like a
  tape. Each construction is checked against the classes of §2.3 and against L1, L6, L7.
- **Decision rule.** If a construction realizes every target of a class exactly inside a given set
  of premises, the relation at that premise set is recorded as uninformative for Q, and Q is carried
  by the next stronger relation. If no construction is found inside A2–A4, J1 is carried as Missing
  and the obstruction found, if any, is recorded at its scope.
- **Countercontrol.** The range-0 construction is the vacuity witness: any identification criterion
  that it satisfies is too weak to answer Q and is not used.

### Node 3 — Finite versus infinite carrier at finite horizon (light-cone reduction)

- **Hypothesis under test.** For `Φ_{q,α}`, readout region `W`, horizon `K` and a preparation whose
  restriction to the backward light cone `W + B_K` is fixed, the window-history law on `ℤ³` equals
  the law on the torus `(ℤ/L)³` once `ext_j(W) + 2K < L`, in both directions (§2.5 rows 3 and 4).
- **Check.** Paper proof extending NR-1 Prop. 4.1 (rooted maps, uniform prior) to the full
  multi-time law and to each preparation class of §2.3. The (Z) → (F) direction and the (F) → (Z)
  direction (lifting the torus preparation) are proved separately.
- **Decision rule.** For each preparation class: if both directions are proved, questions about J2
  and J3 at horizon `K` for that class are decided on tori, and Nodes 4–5 may compute on tori. If
  only one direction is proved, only that transfer is used. If a class fails (for example a
  (Π-β) event `E` outside the light cone that correlates with it, or a (Π-joint) law with no
  torus counterpart), that class keeps a separate (Z) status.
- **Controls for any computation here.** Replay control: reproduce NR-1 §7 part B (`dim K_t`,
  `dim N_t` agree between torus and `ℤ^d` for `t ≤ (L−1)/2`) before any new run. Countercontrol: a
  torus below the bound must show a disagreement in at least one recorded instance, so the
  comparison detects wrap-around.
- **Scope.** This node bears on finite-horizon laws only. Global return (R-c), recurrence and every
  property at unbounded times differ between (F) and (Z) (P1-AUDIT §3) and are not transferred by it.

### Node 4 — The Stage 2 reference law: J3 under (Π-β) and (Π-H)

This is the branch closest to Q: the preparation is generated by the reference law `β` Stage 2 uses.
It splits into three sub-branches, taken in this order.

**4a. Arithmetic of the kernels (exact).**
- **Hypothesis under test.** Under (Π-H) or (Π-β), with any readout class, every conditional kernel
  of the window-history law at a positive-probability history is rational, as a ratio of counts on
  the finite light cone (through Node 3 and the rationality statement of Main:526 for finite
  realizations with rational prior). Then a target with an irrational conditional kernel has no
  exact J3 realization in these classes.
- **Check.** Paper proof. Literature check of L2 for the Haar marginals.
- **Decision rule.** If the proof passes review, record the negative for (ex), targets with an
  irrational kernel, preparations (Π-H) and (Π-β), every readout class and every `(q, α)`, in both
  settings to the extent Node 3 transfers. It does not cover rational targets, (ε) realization,
  (Π-prod) or (Π-joint), and it bears on any finite-alphabet rule with uniform hidden prior, not on
  `Φ_{q,α}` specifically; the record states that last point. If the proof fails, 4a is parked with
  the gap named.
- **Pressure test.** Exact equality with an irrational empirical law is not an observable
  requirement: data fix a law to finite precision. A negative at (ex) alone is therefore recorded
  as an arithmetic fact about the classes and is not reported as an answer to Q; 4c carries the
  (ε) question.

**4b. Coset and translation structure (exact, linear readouts).**
- **Hypothesis under test.** For an affine update, a readout in (R-lin) and a preparation `P₀ ⊗ ν`,
  the conditional window-history law given the visible initial state `x₀` is the translate by an
  affine function of `x₀` of one fixed law (the pushforward of `ν`). Under (Π-H), and under (Π-β)
  with `E` an affine event, that law is uniform on a coset of a subgroup. This extends NR-1
  Lemma 2.2, which proves the one-time rooted case under Haar and window readout.
- **Check.** Paper proof of the multi-time statement; then an exact finite test on tori allowed by
  Node 3: for each target, compute the distance functional
  `δ_tr(P) = min over labellings of outcomes by readout values, laws λ and affine maps A of
  max_{x₀} TV(P(· | x₀), τ_{A x₀} λ)` (for 4b under (Π-prod)), and the coset-uniform distance
  `δ_cos(P)` (for (Π-H), (Π-β)), each by exact enumeration over the finite candidate set.
- **Decision rule.** If the lemma passes review, then for (R-lin): `δ_tr(P) > ε` excludes (ε)
  realization under (Π-prod), and `δ_cos(P) > ε` excludes it under (Π-H) and (Π-β), for that target,
  `(q, α)` and window size; `δ = 0` admits the exact realization and is followed by an explicit
  realization checked in exact arithmetic. Each verdict is recorded per target family; no
  statement about all targets is made from a finite test.
- **Controls.** Positive control: a target generated by `Φ_{q,α}` itself under (Π-H) must give
  `δ_cos = 0`. Countercontrol: a target realized by the response-table construction (Main:528), which
  is not affine, with conditional laws that are not translates, must give `δ_tr > 0`; and the same
  test applied to a second-order rule `x(t+1) = F(x(t)) − x(t−1)` with a non-affine `F` (reversible
  for every `F`, SM:106), fixed before the run, must not report a coset structure it does not have,
  so the test is not vacuous.
  Symmetry control: relabelling the visible alphabet by a group automorphism leaves `δ_tr` unchanged.
- **Target families.** Small instances of (𝒫-Q) and (𝒫-mem) fixed before the run: a qubit and a
  qutrit observed in a fixed basis with a stated unitary between readings, horizons 2 and 3, and
  memory-bearing laws taken from the corpus's certified examples (Main §3.4 probes), each listed
  with its exact data in the node's preregistration amendment.

**4c. Non-linear readouts (ε).**
- **Hypothesis under test.** Under (Π-H) or (Π-β) with (R-nl), the targets of (𝒫-Q) and (𝒫-mem) are
  (ε)-realizable for every `ε > 0` with a window and horizon budget that can be stated.
- **Check.** Paper construction or obstruction, then exact enumeration on small tori: the set of
  realizable laws is the set of pushforwards of coset-uniform laws under functions `g`, so for fixed
  `(q, α, W, K)` the minimal TV distance to the target is a finite minimization computed exactly.
- **Decision rule.** If a construction with a stated budget `|W|(ε)` is proved, record the positive
  at (ε) for the stated targets, with the budget, and pass to the pressure test. If the exact
  minimum stays above a stated `ε₀` for every window up to the computed size, record only that
  finite fact; it is not extrapolated to larger windows.
- **Pressure test (favourable branch).** A positive here is examined for three ways it could carry
  no Stage 2 content: (i) whether the same budget is met by every finite-range reversible rule with
  a mixing hidden inflow, so the result says nothing about `Φ_{q,α}` in particular; (ii) whether `g`
  must encode the target's structure, so the readout, not the dynamics, carries the law; (iii)
  whether the construction violates the observer premises (Lemma 1's finite capacity; SM:242's
  linear projection on Koopman observables; A1-01 row 2b's scalar-kernel bridge). Each is answered
  before the positive is accepted, and the record states which of them hold.

### Node 5 — Preparations not generated by the reference law: J2 under (Π-prod) and (Π-joint)

Opened only if Node 4 leaves Q undecided for the target class, or decides it negatively.
- **Hypothesis under test.** Every target of (𝒫-Q) is exactly J2-realizable under (Π-prod) with
  (R-nl), the hidden inflow into `W` serving as a tape.
- **Check.** Paper construction; for small instances an exact linear-feasibility problem: by
  linearity the window history depends on hidden coordinates only through `M h ∈ im M`, so a law `λ`
  on `im M` replaces `ν`; feasibility is certified by an exact rational feasible point, and
  infeasibility by an exact Farkas certificate.
- **Decision rule.** Feasible with a verified point: J2 holds for that target and class, and the
  record states that the preparation is not generated by the reference law, so J3 is not
  established by it. Infeasible with a verified certificate: J2 fails for that target, readout,
  window and horizon. No other output is a verdict.
- **Controls.** Positive control: a law generated by `Φ_{q,α}` under a random rational `ν` must be
  feasible. Negative control: a law with support outside `L x₀ + im M` must be infeasible with a
  certificate. Replay: rerun from the recorded rational data must reproduce the certificate.
- **Interface.** A positive here moves the question to the measure: whether a preparation law of
  this kind is the law Stage 2 and Stage 3 use. That question belongs to P2-B's measure and is
  recorded as the interface of §6, not decided here.

### Node 6 — Dynamical identification: J4-fac and J4-emb

- **6a. Factor.**
  - *Hypothesis under test.* For `α` a unit, `(Ω, Φ_{q,α}, β)` on (Z) has no factor onto a finite
    `(S, φ)` on which `φ` acts non-trivially on the support of the pushed-forward law.
  - *Check.* Citation: mixing for unit `α` (R1-INF Prop. 5, delta review outstanding; L2) and the
    standard fact that a weakly mixing system has no non-constant eigenfunction (L3), applied to the
    eigenfunctions a factor onto a finite cycle would carry.
  - *Decision rule.* If R1-INF Prop. 5 passes its delta review and L3 supplies the eigenfunction
    statement with hypotheses met, record the negative for J4-fac: measurable factors, unit `α`, the
    law `β`, setting (Z). It does not cover non-unit `α`, other invariant laws, topological factors,
    or J2 and J3, which are not factor relations. If either input fails, 6a is parked with the gap.
  - *Pressure test.* Check that the factor notion matches what Stage 1 needs: Stage 1's visible
    process is a readout, not a factor, of `R₁` (the visible process of a non-Markovian law is not a
    factor of `φ`), so a negative for J4-fac does not by itself bear on J3.
- **6b. Invariant finite subsystem.**
  - *Hypothesis under test.* For translation-invariant `Φ_{q,α}`, the `P`-periodic configurations of
    `ℤ³` form a finite invariant subset on which `Φ_{q,α}` is the torus update (setting (F) inside
    (Z)), and the union over sublattices `P` is `β`-null.
  - *Check.* Paper argument; L7.
  - *Decision rule.* If both parts hold, record that the finite representatives of setting (F) embed
    in (Z) as invariant subsystems carried by a `β`-null set; then every property Stage 1 proves on a
    finite representative (for example global return, P1-AUDIT §3 (R-c)) holds on that null set and
    transfers to `β`-typical configurations only through a further argument, which is P2-A's
    interface (§6). If either part fails, record the failure at its scope.

### Node 7 — The morphism to Stage 1's datum and the coupling-graph seam (J5)

- **7a. Hypothesis under test.** The canonical predictive quotient of Main:632, with its unique
  morphism `q_R`, extends from finite carriers to a realization of `P` by `Φ_{q,α}` on (Z) at
  horizon `K` with a finite readout.
  - *Check.* Paper proof: well-definedness and measurability of the visible-future-tail map (it
    depends on the finite light cone), the pushforward clause and the uniqueness clause on the
    prior-supported reachable part, which for a non-atomic law must be restated with "almost
    every". Compare with L5.
  - *Decision rule.* If the extension is proved, record that every lattice realization of `P`
    (J2 or J3) carries the morphism onto `T(P)`, so Stage 1's datum can be taken as `T(P)` and the
    identification reduces to J2 or J3. If it fails, record the failing clause.
- **7b. Hypothesis under test.** The coupling graph Stage 2 reads (Sub:157, "inherited from Stage 1")
  is not a function of Stage 1's datum `R₁` or `T(P)`, which carry no site factorization; it is read
  off a lattice realization under posit (viii).
  - *Check.* Reading of SM:66–68 and Main:736 (viii); the SM:68 normal-mode example is the witness
    that one dynamics carries coupling graphs of different degree under two identifications.
  - *Decision rule.* If confirmed, record that the direction of inheritance at Sub:157 needs the
    lattice realization of Node 4 or 5 as an input, and that this is an assumption of Stage 2, not
    an output of Stage 1. This node proposes no manuscript wording.
  - *Countercontrol.* Apply the reading to a realization that does carry a site factorization (the
    torus realization of a J2 instance, if Node 4 or 5 supplies one): there the coupling graph is
    defined and equals the lattice graph, so the reading distinguishes the two cases.

### Node 8 — Transfer of Stage 1's conclusions to a lattice realization

For a lattice realization produced by Nodes 4–5, determine which Stage 1 conclusions hold of it.

| Conclusion | Source | Check | Decision rule |
|---|---|---|---|
| C1, C3, C4 necessity; unavoidable hidden predictive memory | Main:614, :624, :736 status rows | Whether the universal theorems, stated for realizations on `C_V × C_H`, hold for a measurable infinite hidden carrier at finite horizon (via Node 3, or directly) | Holds: the conclusion transfers to every J2 realization. Fails or unproved: recorded per conclusion |
| C2 persistence and slow-bath forms | Sub:129; Main:463, :477 | The theorems are stated on a measurable `H` (P1-AUDIT rows 16, 22); check the coupling-step model fits `Φ_{q,α}` with the readout | Fit shown: transfers, the slow-bath form keeping the open mixing hypothesis. Not shown: recorded |
| Recurrence-cycle P-indivisibility | Sub:137; P1-AUDIT row 21 | Consumed as an interface from P2-A (§6); NR-1 Prop. 2.3 and Thm 3.3 already decide it negatively under Haar with window readout at their stated hypotheses | P2-C records only whether the preparation class Node 4 or 5 requires is one under which P2-A's replacement condition can hold |
| Stage-1 gauge statement | Sub:139 | Scoped to the finite datum actually used | Not transferred by P2-C; recorded as finite-datum-only unless Node 7a supplies a lattice-level form |

### Node 9 — One system for every context

- **Hypothesis under test.** One `(q, α)` and one reference law serve every experimental context,
  the contexts differing only in readout region and preparation.
- **Check.** Compare the constraints Nodes 1, 4 and 5 place on `(q, α)` per target (alphabet counts,
  denominators, coset structure). For composite `q`, use the primary decomposition (NR-1 node 5
  item (4)).
- **Decision rule.** If two target families of the stated classes impose incompatible conditions on
  `(q, α)`, record the incompatibility at its scope. If every constraint found is met by one
  `(q, α)`, record that, for the families tested only.

## 5. Productivity test, stop conditions and output classes (fixed before any node runs)

**Productivity test (§A.31).** P2-C is a gem iff it yields a fact strictly stronger than the
restatement "the Stage 1 → Stage 2 identification is open in both settings" (P1-AUDIT row 53;
O-A4 row 2), and that fact either constrains something or exposes a hidden assumption. Qualifying
outcomes:
- (a) a decision, proved or closed by citation, of J2 or J3 for a stated target class, readout
  class, preparation class, setting and exactness, positive or negative;
- (b) a reduction of Q to a precisely stated finite problem with both directions witnessed (for
  example Node 3 with Node 7a);
- (c) an exposed hidden assumption with a witness: for example that the identification requires a
  preparation not generated by the reference law of Stages 2 and 3, or that Sub:157's inheritance
  needs a lattice realization as an input.

Non-gems: renaming the relations without a decided instance; restating ledger or Phase 1 rows;
any outcome Node 2 shows to be vacuous. The propagation bar is better than coherence; below it, the
outcome is recorded only.

**Output classes.** Each node's verdict is classified NEW, POSITIVE, ELABORATING, CONFIRMING or
BORDERLINE (§A.31), with the reason.

**Stop conditions.**
- **S1 (fixed point).** Three consecutive closed nodes without a NEW finding.
- **S2 (posit required).** A node's decision turns on a physical choice the corpus does not make (for
  example which preparation class is physical); the node stops and the choice is routed to the
  owner, with the alternatives and their consequences.
- **S3 (control failure).** A failed, vacuous or self-reproducing control voids that node's verdict;
  the node halts until the control is repaired.
- **S4 (cost).** A computation exceeding the bounded local budget stops; the partial state and a CI
  plan are published instead (§A.40).
- **S5 (measure interface).** If Node 4 decides J3 negatively for a target class at both (ex) and
  (ε) for every readout class, and Node 5 decides J2 positively, the remaining question is which law
  the system carries; P2-C stops and reports that interface to P2-B.
- **S6 (provenance).** Any unaccounted file in the work area triggers the §A.26 sweep and halts
  substantive work.

**Scope of negative results.** A negative verdict is stated for the dynamics, readout class,
preparation class, target class, setting and exactness of the node that produced it. It is not
stated as a failure of every observer-level extension, of every lattice dynamics, or of every
preparation law.

## 6. Interfaces with P2-A and P2-B

These are stated as interfaces only. This design was prepared without reading the P2-A or P2-B
drafts, and it fixes nothing in them.

| Interface | P2-C consumes | P2-C supplies |
|---|---|---|
| P2-A (Stage 1 return) | The condition P2-A proposes in place of exact global return, stated as a property of a dynamics, readout and law | The preparation and readout classes under which J2 or J3 holds (Nodes 4–5), and Node 6b's record of where finite representatives sit in (Z); P2-C checks whether P2-A's condition can hold in those classes (Node 8, third row) |
| P2-B (Stage 3 measure) | The normalized law P2-B justifies on the infinite configuration space for the entropy and boundary calculation | J3 is evaluated with `β` taken to be that law when it differs from Stage 2's H-μ(φ,Θ) instance; P2-C reports whether Stage 1's laws arise from it (Node 4) or need a preparation outside it (Node 5) |

Known constraints at the interfaces, already on record: under Haar with window readout and `α`
non-nilpotent, rooted exact return and (NR) fail (NR-1 Prop. 2.3), and for `q` prime, `α ≠ 0` and
lattice-convex windows the rooted family is P-divisible at every horizon (NR-1 Thm 3.3). A
generic normalized invariant law leaves the Stage 3 slope undetermined (P1-AUDIT §2.2).

## 7. Invariant → checkpoint table (§A.41)

| # | Invariant asserted of this design or of a future execution | Checkpoint that measures it |
|---|---|---|
| I1 | This design changes only its own directory | `git diff --stat origin/main...HEAD` lists only `DESIGN.md` here, checked before each push |
| I2 | No proof executed and no computation run in this design | The commit adds one Markdown file and no code or data file; checked with the diff above |
| I3 | Every corpus citation reads as cited at the pin | Each `file:line` re-read at `df6da1c6` before commit; the reviewer re-reads a sample of them |
| I4 | No relation carries a status stronger than its source | §2.4 and §2.5 status cells checked against P1-AUDIT, O-A4, NR-1 and Main:632 by the reviewer |
| I5 | Decision rules are fixed before any node runs | Nodes run only from a reviewed head of this file; any change is an additive amendment commit, with the reviewed SHA cited in the node's record |
| I6 | Computational verdicts print only over green controls | Each node's result record prints the control table before the verdict; a verdict line without a preceding green control table is void |
| I7 | Exact claims are certified exactly | Each exact verdict names its certificate (rational feasible point, Farkas vector, exact count) and the replay that reproduced it |
| I8 | Negative results carry their full scope | Each negative verdict line names the six scope fields of §4's common rules; the reviewer checks each |
| I9 | Independence from P2-A and P2-B drafts | The design cites only the owner's statement of their scope (#1169 c.7068325638); no reference to their branches or commits appears in it |
| I10 | Repository-text constraints | A grep of the added lines for the excluded vocabulary and for local paths returns nothing |
| I11 | Every displayed equivalence has a witness per direction | §2.5 lists each direction separately with its witness or "Missing"; no new equivalence is displayed |

## 8. Out of scope

- No proof is executed and no computation is run under this design; each node waits for review of
  this design and a separate authorization.
- No change to any manuscript, to Theorem 23 or its proof, to #1477 or its frozen plan P*, to the
  A1-EXIT ledger, to the Lean-to-manuscript census registry, or to any Lean file.
- No wording is proposed for Sub:157, Sub:195 or SM:66; D022 and D026 remain with the #1477
  reviewers.
- The M1-B Bell sector and H-Bell; the continuum step; the observer-kernel bridge of A1-01 row 2b,
  which P2-C uses only as a constraint in the pressure test of Node 4c.
- No post on #1169 or #1477.
