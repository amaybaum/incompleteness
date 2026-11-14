# NLCAND r3: the SM ring rule as one non-linear candidate, tested jointly for control, Bell and cell supply

**WIP / unverified. Paper-only writer draft r3; hand reasoning only. r1 received an independent non-author
review (`REVIEW-r1.md`, REVISE); r2 received the same reviewer's confirmation (`CONFIRM-r2.md`, ACCEPT WITH
CHANGES, N1–N5); r3 is r2 with those five wording edits and no change of verdict. Dispositions are in
`RESPONSE-r1.md`. Both reviews are model reviews, not independent verification (§A.46 item 7). Authorizes
nothing, adopts no premise, proposes no manuscript edit. The hypothesis that the world's rule is this ring
rule, written H-ring below, is unadopted throughout and nothing here recommends adopting it. H-ring is not
TUNE-1's H-nl, which names the rounded rule of SM:294 (S4:37–39).**

- **Scope.** Owner instruction of 2026-11-14, as relayed to the writer: "Specify one non-linear candidate.
  Start from the SM ring rule and test all three requirements jointly: control, parameter dependence without
  signalling, and cell supply." Paper-only. Every verdict below is about the one member specified in §1.4.
- **What was done.** Source reading and hand derivations. No script computed on any OI rule or model; no
  enumeration, simulation, probe replay or Lean build. Stored outputs of earlier runs were read, not rerun.
- **Pins.** `main` = `c3b5f37a354bb26437e2e0165c576a347a63c153`. `Main:n`, `SM:n`, `Sub:n`, `GR:n` are lines
  of `papers/Main.md`, `papers/SM.md`, `papers/Substratum.md`, `papers/GR.md` there. With `R` =
  `verification/programmes/oi-qm/reconstruction`, on `main`: `OA1:n` = `R/oa-1-20261112/OA-1-REPORT-r5.md`;
  `OA2:n` = `R/oa-2-20261112/OA-2-REPORT-r4.md`; `OA3:n` = `R/oa-3-20261112/OA-3-REPORT-r4.md`; `M2:n` =
  `R/mechanism-2-20261108/DESIGN.md`; `PPS:n` = `R/oi-qm-ext-1/prepared-pair-source.md`; `PI:n` =
  `R/oi-qm-ext-1/physical-interface.md`; `S3:n`, `S4:n` = `R/drafts/tune-1-20261111/TUNE-1-STEP2-SESSION3.md`,
  `…SESSION4.md`. Off `main`, read at the stated heads: `3A:n` = `R/drafts/tune-1-20261111/TUNE-1-STEP3A-r3.md`
  at `8228b3c2`; `SS:n`, `LP:n` = `R/tune1-landing-20261114/STATUS-SOURCING.md`, `LANDING-PLAN.md` at `ea9bff9c`;
  `LD:n` = `R/drafts/bell-ladder-20261113/BELL-LADDER-r3.md` at `d8e4f80e`; `BS:n` =
  `R/drafts/bell-scope-868-20261111/BELL-SCOPE-UNIT1.md` at `e1534b08`; `L3:n` =
  `R/bell-landing-20261114/SB-L3.md` at `a0fa2502`; `MP:n` = `R/drafts/mixed-path-868-20261111/MIXED-PATH-UNIT1.md`
  and `MPR` = its `stage2/runs/10/results.json`, at `a8fff57a`; `NA:n` =
  `R/native-apparatus-source-20261113/ASSESSMENT.md` at `d8b74527`. Lean files are under
  `verification/lean-mathlib/OIBridge/` on `main`, statements read, not rebuilt.
- **Tags.** [P] manuscript on `main`; [K] Lean statement read; [R] research record on `main` (model-reviewed,
  not verification, §A.46 item 7); [D] draft off `main`; [H] hand derivation in this file; [H, Rc] hand
  derivation that the reviewer of r1 re-derived and confirmed (`REVIEW-r1.md` §A), which is a model review and
  not verification.
- **Record conventions, kept apart.** **H**: a wing's record is the complete history of its region from the
  setting slice `t_s = 0`, the content of both slots at `t = 0` included (D4-type; 3A:501; LD:198–200).
  **S**: the single-time readout of Main's Bell theorem, "a ±1-valued function of the state on a readout
  region `R_A` `k_A` updates after the setting" (Main:369–372); the state at tick `k` holds `x(k)` and `x(k−1)`
  on the region and not earlier slices. Under both, values fixed by declaration (ready cells, labels) are
  known. OA-2's design runs the two as separate variants (OA2:803–805), and the choice is an open item of the
  ladder (LD:274).

***

## 0. Answer

1. **The candidate.** SM's ring rule exactly as written (SM:112): second-order update on a ring over `ℤ/q`,
   left neighbour fixed, right neighbour `i+1` or, when cell `i+1` holds `0`, `i+2`. It is a complete bijective
   update (§1.2). The member adds the uniform counting law, a three-cell observer block, cell-content labels, one
   declared ready cell and one-cell setting generators (§1.4); these are the writer's choices.
2. **Missing from the manuscript.** The update is not missing. Not given for it: a `d = 3` six-component
   version; the reference class as a set of configurations; any switched edge longer than two sites; every
   interface datum.
3. **Preserved results (§2).** Bijectivity, the second-order kernel layer, `S ⇔ D ⇔ Q_fb`, the cone lemma and
   the Bell ceiling (read on the rule's own graph), centre independence and time reversal survive. The
   nearest-neighbour graph, the wave-rule form and the dispersion hold only on `K_nz`, a class chosen here; on
   the vacuum and uniform readings of the reference class they break. Shift covariance, reflection covariance
   and the linear rule's quadratic invariant break. Every `d = 3` result is undetermined, because no `d = 3`
   version of the ring rule is written. The list is not a complete inventory.
4. **(a) Control.** A label action that is not a translation: supplied (pointwise, both conventions).
   Operator-level mixing at the kernel's configuration-level interface: unavailable for every rule by the
   construction of that interface, so not a test of this candidate. TUNE-1's single-qubit target, a condition on
   record laws: undecided.
5. **(b) Bell.** Member: not supplied at lattice scale. Rule: not established. Outside its own cone the rule
   gives no dependence and is Bell-local under (xiv), under both conventions. Inside it: with adjacent blocks
   the member reads the remote setting at distance two after one tick (total variation 1 at label `0`, both
   conventions); with one unread cell between, total variation `1/q` under H and `0` under S. A cone dichotomy
   (B7) covers every choice of physical speed. One-cell records under H are no-signalling with a PR-type table
   at one tick; under S that table is absent.
6. **(c) Cell supply.** No unconditional supply under the uniform counting law, for any bijective rule; a
   herald that fixes `M` slots is accepted with probability at most `q^{−M}`. Undecided under the orbit and
   record-compatible laws.
7. **Joint.** The member is not shown to meet the three requirements, and for (b) it has a derived defect at
   lattice scale. The kernel no-go is rule-blind and is not scored. The one supplied ingredient of (a) and the
   signalling of (b) are the same gated read (J2).

***

## 1. The candidate

### 1.1 The manuscript's definition

SM:112, verbatim: "On a ring of L ≥ 4 sites with alphabet ℤ/qℤ, define the right-neighbor assignment
$R(i, x) = i+2 \bmod L$ if $x_{(i+1) \bmod L} = 0$, and $R(i, x) = i+1 \bmod L$ otherwise, with left neighbor
$L(i) = i - 1 \bmod L$ fixed. The dynamics is $x_i(t+1) = (x_{L(i)}(t) + x_{R(i,x(t))}(t) - x_i(t-1)) \bmod q$."

Notation used below (mine): `u = x(t)`, `v = x(t−1)`; `sel(a, b) = a` if `a ≠ 0` and `= b` if `a = 0`;
`f_i(u) = u_{i−1} + sel(u_{i+1}, u_{i+2})`; `Φ(u, v) = (f(u) − v, u)`. Then `x_{R(i,x)} = sel(x_{i+1}, x_{i+2})`
and `Φ` is SM's update. At `q = 2`, `sel(a, b) = a ∨ b` (M2:157–164; OA3:135–137).

Standing in the corpus: an example of the state-varying-graph principle, "not derived or selected by OI"
(M2:205); outside ledger (vii), since under a linear update the graph is the same at every state (Main:362;
SM:104); any use as the world's rule is a Layer-0 revision (OA2:676–677).

### 1.2 Bijectivity and reversal, by hand [H, Rc]

Put `Ψ(a, b) = (b, f(b) − a)`. Then `Ψ(Φ(u, v)) = Ψ(f(u) − v, u) = (u, f(u) − (f(u) − v)) = (u, v)` and
`Φ(Ψ(a, b)) = Φ(b, f(b) − a) = (f(b) − (f(b) − a), b) = (a, b)`. So `Φ` is a bijection of `(ℤ/q)^{2L}` for
every `L ≥ 4`, every `q ≥ 2` and every map `f`; this agrees with SM:106 and SM:112. With the slot swap
`σ(u, v) = (v, u)`: `σΦσ(u, v) = σ(f(v) − u, v) = (v, f(v) − u) = Ψ(u, v)`, so `Φ⁻¹ = σΦσ` for every `f`.
Spot check, `L = 4`, `q = 2`, `u = (1,0,0,1)`, `v = 0`: `f(u) = (1,0,1,1)`, `Φ(u, v) = ((1,0,1,1),(1,0,0,1))`,
and `Ψ` of that is `((1,0,0,1), f(1,0,0,1) − (1,0,1,1)) = (u, 0)`.

### 1.3 What the manuscript does not define

- **M1. No `d = 3` version of this rule.** SM:112 is a one-component ring. The statements that follow it
  quantify over a class ("bounded-degree graph G(x) satisfying constraints (i)–(iii)", SM:144) of which no
  `d = 3`, six-component switched-neighbour member is written in the sources searched. The `d = 3` non-linear
  rule that is written, the rounded rule of SM:294, is a different rule and is not assessed here.
- **M2. The reference class as a set of configurations.** SM:108 and Main:362, :724 name "the reference
  vacuum/uniform state class" without listing its members. For this rule the readings differ (B1): the
  all-zero configuration and the support of the uniform law both give the full two-site graph; only current
  slices with no zero give the nearest-neighbour ring.
- **M3. Long edges.** The only switched edge has length two. Sub:131 speaks of "bounded-degree Bell-relevant
  long edges"; no update containing one is written, nor a process that prepares one (PPS:81). Nothing in this
  file therefore tests H-Bell (Sub:131–133).
- **M4. Interface data.** SM:112 names one visible sector, "one site's two time slices", and "the uniform
  hidden prior", both for its P-indivisibility remark. Everything else in §1.4 is chosen.

### 1.4 Member specification

| Item | Value | Source or choice |
|---|---|---|
| Rule, carrier | `Φ` of §1.1 on a ring of `L` cells, each cell a pair `(u_i, v_i) ∈ (ℤ/q)²` | taken, SM:112 |
| Memory sign, distinguished value `0`, jump length `2` | as written | taken, SM:112 |
| `q` | free. Statements hold for every `q ≥ 2` unless marked | free parameter (SM:112) |
| `L` | free, taken `≥ 4T + 8` for horizon `T`, so that no dependency path wraps | chosen. At horizons `≥ 4L − 10` a three-cell observer with held history has a simplex fragment (OA3:306–314); in one fixed finite world the member cannot be kept outside that regime |
| Law | μ-G, uniform on `(ℤ/q)^{2L}` (ledger (iv), uniform reading; OA1:103–105) | chosen as the task's default; μ-O and μ-R in §5 |
| Observer region `O` | three consecutive cells `{a, a+1, a+2}`, both slots | chosen where results exist (OA3:225–234), not where the question is open: `|O| ≤ 2` is the open case (OA3:89–92, :498–518) |
| Readout | convention H or convention S, stated at each node | H is an imported convention (3A:501); S is Main:369–372 |
| Control region `C` | `{a, a+2} ⊂ O`, both slots; menu of `q⁴` labels | chosen (A1) |
| Ready configuration `r_O` | cell `a+1` at `(0, 0)` | free; a declared initial condition of the MP-0a type, unsourced (3A:493) |
| Round length | one tick | free |
| Preparation prefixes | initial-condition mode: the label is the content of `C` at `t = 0`; a herald is a condition on the record; nothing writes but `Φ` | TUNE-1 schema (3A:466–470) |
| Two wings | two such blocks, `A = {a..a+2}` on the lower-index side and `B = {b..b+2}`, `g = b − a − 3` unread cells between; `B`'s generator is cell `b`, setting `y = u_b(0)`; `A`'s generator is any cell of `A` | chosen; the lower-index wing is the one the two-site edge reaches |
| One-cell variant (B5 only) | records `{i−1}` (A), `{i}` (B); generators `{i+2}` (A), `{i+1}` (B) | the one-cell record is the only visible sector SM:112 itself names; the generator placement is chosen |

**Not supplied, and not readable from the manuscript:** the generating rule for more than one round, a
declared target with its separation length and constant, and the label encoder (items 1–3 of 3A:913–931). The
member is specified for one-round label actions and for the two-wing protocol, and is not a Step 3B-qualifying
family. Gap S (LP:243–245) stays open.

**Which verdicts depend on these choices.**

| Result | Depends on | If changed |
|---|---|---|
| A1, B1, B2, B3 | nothing chosen (pointwise properties of `f`); B2 also (xiv) | — |
| A3 | nothing in the candidate | — |
| A5 bound `0.023` | `|C| = 2`, `q = 2` | NL-C′ gives the general form |
| B4 (0), total variation 1 | adjacent blocks; `r_O`; label `0`. Under H, `r_O` is not needed | under S without `r_O`: `0` at `T = 1` |
| B4 (ii), total variation `1/q` | convention H; two adjacent held cells | `0` under S; `0` for one-cell records |
| B5 PR-type table | one-cell records; convention H; interleaved generators | absent under S; signals if `B` holds its generator cell or cell `i−1` |
| C1 | μ-G | undecided under μ-O, μ-R |
| P5–P7 | `K_nz` | "breaks" on the other readings |

***

## 2. Results the replacement of ledger (vii) must preserve

The list was drawn up from SM §3.1, Main §3.3–3.4, the ledger (Main:724) and Sub §3; it is not a dated
preregistration and not a complete inventory. `papers/Structure.md`, the book and `papers/GR.md` beyond the
lines cited were not read. "`K_nz` only" means: holds on `K_nz`, the configurations whose current slice has no
zero (B1). `K_nz` is the writer's choice of the class on which ledger (x) can hold; on the all-zero
configuration and on the support of μ-G those entries read "breaks" (M2).

| # | Result | Outcome | Reason |
|---|---|---|---|
| P1 | Bijectivity (ledger (iii)) | survives | §1.2 |
| P2 | Second-order form (xiii) and the kernel layer stated for it (`ruleDynamics`, quasilocal completion, the path of automorphisms; Main:588) | survives | the Lean `Rule` carries an arbitrary finite-range `F` (`SecondOrderLayer.lean`:198–203) [K] |
| P3 | `S ⇔ D ⇔ Q_fb`; characterization theorem of Main §3.4 | survives | no rule and no spatial constitution enters (Main:724, "which the characterization theorem of §3.4 does not use") |
| P4 | Cone lemma (Main:362); Bell ceiling (Main:364–389) | survive, read on this rule's graph | they need site factorization and the actual dependency graph only (B1). The Corollary Main:414 is stated for the nearest-neighbour cubic update and does not describe this rule |
| P5 | Ledger (x), nearest-neighbour graph on the reference class | `K_nz` only; breaks on the vacuum and uniform readings | B1 |
| P6 | Form lemma and wave-rule selection (SM:224; Sub:159) | `K_nz` only, one step at a time; breaks on the other readings | the lemma's hypothesis is linearity; on `K_nz` one step of `Φ` equals the `α = 1` nearest-neighbour rule; the lemma does not select this rule |
| P7 | Dispersion `cos ω = cos k` (SM:126) and what rests on it | `K_nz` only; breaks for typical configurations under μ-G | a statement about trajectories; `K_nz` is not closed for `q ≥ 3`, though it has an invariant part that is not characterized (B1) |
| P8 | Reflection covariance of the update (isotropy in `d = 1`; ledger (vi)) | breaks | reads are directed: `i` reads `i+2` and never `i−2` (M2:191). SM:108 (iii) concerns the undirected selected graph and holds for it |
| P9 | Centre independence, both clauses (xi); bounded degree (ix) | survive | `f_i` does not read `u_i`; same rule at every site; three in-neighbours (SM:112; M2:187–189) |
| P10 | Amplitude-scale gauge (SM:96, :240; Sub:100) | scaling survives, shift breaks | `sel(λa, λb) = λ·sel(a, b)` for units `λ`; the shift `x ↦ x + c` turns the test "`= 0`" into "`= c`". The affine lemma's premise fails: at component `i`, `f(δ_{i+1} + δ_{i+2}) − f(δ_{i+1}) − f(δ_{i+2}) = −1` |
| P11 | Time-reversal symmetry of the update (SM §5.1) | survives | `Φ⁻¹ = σΦσ`, §1.2 |
| P12 | Recurrence-cycle P-indivisibility for a one-site visible sector | survives | asserted for this rule at SM:112; not re-derived |
| P13 | Mod-`q` boundary bound `I(V; V^c) ≤ |∂V| log₂ q` (SM:122–124) | survives with `∂V` read in the union graph | the Markov argument needs every in-neighbour of an interior cell inside `V`. For a boundary read in the configuration's own graph (SM:150) it is not re-derived |
| P14 | Discrete Einstein equation | nothing to preserve | target form with an open curvature step (SM:144–150) |
| P15 | Gauge sector, six-link carrier, generations (`d = 3`) | undetermined | M1. Theorem 7 (link geometry) does not depend on the rule |
| P16 | Linear-rule spectral results (SM Appendix A; cycle-structure Remark, SM:296) | inapplicable to the candidate | they use the module structure of an additive map |
| P17 | Kernel sourcing negatives on control (Main:588) | unaffected | the statements do not take the rule as input (A3) |
| P18 | Hidden-sector mixing (ledger (v)) | undetermined | no result for this rule |
| P19 | Gap equation (SM:110 asserts it "is unchanged" for this class; GR §3) | not assessed | GR §3 was read only at GR:78, :144, :154; SM:110's assertion is not re-derived |
| P20 | Observer-level linear lift and the Dirac factorization (SM:222, :284) | operator identities unaffected; their attachment to the candidate undetermined | the identities concern the lattice operator. The map from the bijection to that operator is recorded as not proved for the linear rule (SM:232); off `K_nz` one step of `Φ` is not the nearest-neighbour operator |
| P21 | Conserved quadratic invariant `E` of the linear rule (SM:296; Sub:135) | breaks for `E` [H] | from `x(−1) = 0`, `x(0) = y·δ_s` on a blank ring: `x(1) = y` at `s−2, s−1, s+1`, so `E = y²` at `t = 0` and `y² + 3y² − 2y² = 2y²` at `t = 1`; the linear rule gives `y²` at both. The two values differ whenever `y² ≢ 0 (mod q)`. Whether `Φ` has another invariant is unknown |

Two results about the candidate itself constrain every node: Lemma OBS (a held three-cell block with history
determines the whole finite ring within `2(L−3)` ticks, OA3:225–260 [R]) and Theorem S (simplex fragment at
horizons `≥ 4L − 10`, OA3:296–347 [R]). Both are stated for held histories (convention H).

***

## 3. Requirement (a): control

**A1. Is there a label action that is not a translation? Supplied [H, Rc].**
- *Gated read.* `x_{a+1}(1) = u_a + sel(u_{a+2}, u_{a+3}) − v_{a+1}`. For label `ℓ = u_{a+2} ≠ 0` the cell reads
  `ℓ`; for `ℓ = 0` it reads the unread cell `w = u_{a+3}(0)`, at distance two, after one tick. With `u_a` and
  `v_{a+1}` known (held under H; `v_{a+1}(0) = 0` by `r_O` and `u_a(0)` in the tick-1 state under S), the record
  is a point mass for `ℓ ≠ 0` and uniform for `ℓ = 0` under μ-G: total variation `1 − 1/q`, in `(0, 1)` for
  every `q ≥ 2`. Lemma A-T (d)'s `0`-or-`1` dichotomy (S3:73–76), which holds for R-lin, fails; the functional
  read depends on the label, unlike the affine case (D5 (ii), OA1:176–183).
- *Controlled write.* `x_{a−2}(1) = u_{a−3} + sel(u_{a−1}, u_a) − v_{a−2}`: the label `u_a` is added into world
  cell `a−2` exactly at world states with `u_{a−1} = 0`.
- *Control off.* With `R ≡ i+1` both reduce to translations, as Lemma A-T requires.
- *Standing.* CONFIRMING: OA3:509–511 records the same non-translational setting action at `q = 2`, and
  OA2:681 records condition N-a as met.

**A2. Which gate family? Characterized [H].** One tick is `v_i ↦ f_i(u) − v_i` at every cell followed by the
slot swap. Label-indexed actions are compositions of translations and zero-controlled translations:
permutations of the configuration set. At `q = 2`, `f_i = u_{i−1} ⊕ u_{i+1} ⊕ u_{i+2} ⊕ u_{i+1}u_{i+2}`
(M2:157–164): one doubly-controlled flip with three singly-controlled ones. Whether these generate every
reversible classical circuit on prepared cells is not shown here.

**A3. Operator-level mixing at the configuration-level interface. Not a test of the candidate [K].**
- *What the Lean statements say.* The kernel's observer theory is `obsTheory 𝒮 := permTheory 𝒮.Conf`
  (`SubstratumInterfaceAudit.lean`:770–771). The rule is not an input: `obsTheory_rule_independent` (:780–782)
  and `sourcing_rule_independent` (`FrozenSourcing.lean`:295–298) hold by `rfl` and `Iff.rfl`
  respectively, the latter with the docstring
  "under the present interface". The negatives are stated on the two-valued carrier with no substratum and no
  rule: `frozen_sourcing_verdict` (`FrozenSourcing.lean`:318–323) for `permTheory (Fin 2)`;
  `substratumGen_not_control` (`StructuralClosure.lean`:348–356) for the monomial class (:180) on `Fin 2`.
  `DenseUnitaryControl` asks that every unitary be within `ε` of an available one for every `ε > 0`
  (`DiscreteCompletion.lean`:45–48), and its ceiling `permTheory_dense_ceiling` (`FrozenSourcing.lean`:187–188)
  holds at the same interface, with `obsTheory_nonnegBounded` (:84–86) for every substratum.
  `obs_not_layerFlowExecutable` (`ExecSource.lean`:129–134) is stated for every substratum and does not claim
  "anything about a richer observer architecture than the stated one" (:28–30).
- *What follows.* That object contains no region, no hidden sector, no law and no record history. Its
  negatives take the same value for the linear rule and for this one, by definition of the object and not by
  a property the rules share. They neither count against the candidate nor bear on whether a change of rule
  helps at an interface where the rule enters. A1 shows that at the record-law interface the rule does matter.
- *The divide.* The kernel statements and TUNE-1's T1 differ in the observer interface: operators on the
  configuration set, against record laws of a region under a law (3A:783–805), which a classical
  hidden-variable model can meet for one qubit (3A:837). The divide is not between rules, and not between
  exact and approximate: the every-`ε` ceiling, stated on the two-valued carrier, holds at the kernel's
  interface.
- *Prior art.* 3A:498 records that the observer theory is rule-independent [K].

**A4. Small observers and short horizons. Undecided.** Whether gated reads give a prepare–measure fragment that
is not simplex-embeddable (condition N-b, OA2:682) is open for observers of at most two cells (OA3:498–518,
:531) and for the member itself at horizons below `4L − 10` (OA3:89–92). Exact gap: the reachable laws and
available effects of those fragments have not been enumerated.

**A5. The single-qubit target T1. Undecided.**
- T1 is stated for TUNE-1's carriers, three-dimensional tori and `ℤ³` (S4:26–28). The ring is outside that
  schema, so T1 would first have to be restated for a ring. NL-P is defined for families of the rounded rule
  (S4:605–606); the gap here is its ring-rule analogue.
- NL-C uses no property of the rule (S4:423–462). With `|C| = 2`, `q = 2`: `M = 16` labels, so Q6′(i) fails at
  every `ε < sin(π/17)/8 ≈ 0.023` (hand value). A pass at small `ε` needs `|C_n| ≥ ½ log_q((1−4ε)/(4ε))`
  (S4:464–474), and the candidate supplies no mechanism for that growth.
- A1 removes the one proved obstruction specific to the linear rule (labels act by translation, OA1:176–195;
  Lemma A-T). It does not show a composing one-parameter family of gate rounds (Q3′, Q4; 3A:800–801).
- The family that T1 quantifies over (3A:913–931, items 1–3) is not specified (§1.4), so T1 cannot be applied.
- Under H, horizons `T ≪ L` only (Theorem S), and unread cells on the lower-index side to depth `T/2` are
  recoverable from the held history (OA3:245–252).

**Verdict (a).** Non-translational label action: supplied, as a pointwise property of the rule. The kernel
negatives: not scored, since they do not see the rule. Single-qubit control at the record-law interface:
undecided; the gap is the ring-rule analogue of NL-P, and the growth of `|C_n|` is unsourced.

***

## 4. Requirement (b): parameter dependence without signalling

Nodes B1–B3 are pointwise and hold under both record conventions. B4–B5 are stated under each convention
separately. B7 is the dichotomy on which the member's verdict rests.

**B1. Does the one-step graph differ between states? Supplied, within two sites [H, Rc].** `x_i(t+1)` depends
on `u_{i−1}` at every state; on `u_{i+2}` at the states with `u_{i+1} = 0` and at no others; on `u_{i+1}` at
every state for `q ≥ 3`, and at `q = 2` at the states with `u_{i+2} = 0`. In Main:362's notation `G_φ` has
in-neighbourhood `{i−1, i+1, i+2}`; `G_φ^K` is the nearest-neighbour ring for `K = K_nz` and for no larger
class; for `K` the all-zero configuration or the support of μ-G, `G_φ^K = G_φ`. Main's graph is the dependency
graph; SM's `G(x)` is the selected-neighbour graph, which drops `i+1` when `x_{i+1} = 0` (SM:112, "undirected
degree in [2, 3] … [2, 4]"; M2:187). This file uses Main's. `K_nz` is not closed for `q ≥ 3` (`u ≡ 1`, `v ≡ 2`
gives next slice `≡ 0`). It has an invariant part: for any profile `h` with no zero value, `x_i(t) = h(i + t)`
and `x_i(t) = h(i − t)` solve the rule for all time, since `sel` then returns its first argument and
`h(i−1+t) + h(i+1+t) − h(i+t−1) = h(i+t+1)`, likewise for `h(i − t)` [H]. That part is not characterized
further. At `q = 2`, `K_nz` is the set `u ≡ 1`, whose only member that stays in it is `u = v ≡ 1`. Under μ-G
each two-site edge is active with probability `1/q` per tick. Directed speeds: at most two cells per tick
toward decreasing index, one toward increasing (ELABORATING; the symmetric envelope is PI:288–291).

**B2. Wings outside the rule's own cone. No dependence; Bell-local [P on H].** With `A` on the lower-index
side, a generator at distance `D` from the nearest record cell of the other wing and a window of `T` ticks: if
`D > 2T`, no record of either wing depends on the other's generator (cone lemma, Main:362, with B1), and under
(xiv) and the protocol hypotheses of Main:364–389, `|S_CHSH| ≤ 2` (closed form BS:159–178 [D]; directed form
L3:46–50 [D]). Toward decreasing index the bound is `D > 2T`; toward increasing index it is `D > T`. Recorded
for this rule at PPS:79, :164 and PI:293–299. This is a confinement statement of the kind Main:414 makes for
any graph cone. It decides (b) only if the physical cone is at least as wide as the rule's own (B7).

**B3. Inside the cone: pointwise dependence. Supplied, one-way [H, Rc].** *Corridor lemma.* Let both slots be
`0` at every cell below `s`, and `u_s(0) = y`; the content of `v_s` and of the cells above `s` is arbitrary.
Then `x_{s−2k}(k) = y` and `x_j(k) = 0` for `j < s − 2k`, for every `k ≥ 1` (no wrap). *Proof.* Induction on
`k`; the hypothesis at `k−1` and `k−2` gives zeros at all `j < s − 2k + 2` at time `k−1` except
`x_{s−2k+2}(k−1) = y`, and zeros at all `j ≤ s − 2k` at time `k−2`. For `j < s − 2k`:
`x_j(k) = 0 + sel(0, 0) − 0 = 0`. For `j = s − 2k`: `x_j(k) = 0 + sel(x_{s−2k+1}(k−1), x_{s−2k+2}(k−1)) − 0 =
sel(0, y) = y`. Base: `x_{s−2}(1) = 0 + sel(0, y) − 0 = y`, `x_j(1) = 0` for `j < s − 2`. ∎ The backward cone of
`(s − 2k, k)` is `[s − 3k, s]`, so the hypothesis is used on `3k` cells, both slots. In a zero background a
cell value is copied two cells per tick toward decreasing index; on trajectories that stay in `K_nz` the same
influence moves one cell per tick. Toward increasing index the speed is one in every background. The window
"inside the rule's cone, outside the nearest-neighbour cone" is `T < D ≤ 2T`, for the lower-index wing only.

**B4. What the member's blocks see inside the window, by convention [H].**
- *(0) Adjacent blocks, `g = 0`.* `B`'s generator is cell `a+3`. With `r_O` (`v_{a+1}(0) = 0`):
  `x_{a+1}(1) = u_a + sel(u_{a+2}, y)`. When `u_{a+2}(0) = 0`, the value `x_{a+1}(1) − u_a(0)` is `y` exactly.
  This holds **under S and under H**: the state on `{a, a+1}` at tick 1 holds `x_{a+1}(1)` and `u_a(0)`, and
  `u_{a+2}(0)` is the label, known by declaration (or read from the block's tick-1 state). Total variation `1`
  between any two remote settings at label `0`; with the label left to μ-G, `1/q`. Under H the ready cell is
  not needed, since `v_{a+1}(0)` is held. The dependence enters through cell `a+1`, at nearest-neighbour
  distance two from the generator; the readout region `{a, a+1}` satisfies Main's condition (iii) in the
  nearest-neighbour graph (`d = 2 > 1`) and fails it in `G_φ`. **This is the gated read of A1 with the remote
  generator in the place of the unread cell.**
- *(i) Blank corridor.* If `3D/2` consecutive cells below `B`'s generator are blank in both slots, `A`'s own
  included, B3 gives `A` the value `y` at tick `D/2` (`D` even): total variation `1`, **under S and under H**.
  This is a prepared line, which is more than requirement (c) asks for (J1).
- *(ii) One unread cell, `g = 1`, `T = 1`.* `x_{a+2}(1) = u_{a+1} + sel(w, y) − v_{a+2}`, `w` the unread cell,
  `y = u_{a+4}(0)`.
  - **Under H** [H, Rc]: `u_{a+1}`, `v_{a+2}` are held, and `P(sel(w, y) = c) = [c ≠ 0]/q + [c = y]/q`. For
    `y ≠ y′` the laws differ at `c = y` and `c = y′` by `1/q` each: total variation `1/q`. `A`'s complete
    history signals, with `D = 2 > T = 1`. The dependence occurs only on the event `N = {w = 0}`, of
    probability `1/q` and independent of the settings; off `N` neither wing's one-tick history depends on the
    other's setting. So for any ±1 functions of the histories, `|S_CHSH| ≤ 2(1 − 1/q) + 4/q = 2 + 2/q`: below
    `2√2` for every `q ≥ 3`, at most `3` at `q = 2` [H].
  - **Under S** [H]: `v_{a+2}(0)` is not in `A`'s state at tick 1, is uniform and enters nothing else, so
    `x_{a+2}(1)` is uniform and independent of `y`. With `r_O`, `x_{a+1}(1)` reads `w`, not `y`. Total variation
    `0`. Each wing's tick-1 state is a function of its own `u(0)`, unread cells that the other wing's setting
    does not enter, and private pads, so the one-tick table is Bell-local.
- *(iii) Padded window, `g ≥ 2`.* **Under H:** by Lemma M (S4:94–101) the slice at tick 1 outside `A` is
  uniform and independent of `u(0)`, so `y` first acts through `x_b(2) = f_b(u(1)) − y`. `A`'s edge cell can
  first depend on it at tick `3 + ⌊g/2⌋` (consistent with Lemma S, MP:320–334 [D]), which precedes tick `g + 1`
  only for `g ≥ 5`. First instance `g = 5`, `D = 6`, `T = 5`: whether `A`'s history law depends on `y` there is
  **undecided**. **Under S:** a state readout is a function of the history, so its total variation is at most
  the value under H; also undecided. Under S with no declared cell, at `T = 1` and every `g`, each `x_j(1)` on
  a block is masked by its own `v_j(0)`: total variation `0` and a Bell-local one-tick table.
- *Stored comparison, not this rule.* The mixed-path Stage 2 run on the rounded rule (small `d = 3` tori,
  `q = 2, 3`) reports headline `SIGNALLING-FOUND`: 37 signalling, 10 masked and Bell-local, 70 without
  dependence, and no non-local table among the no-signalling ones (`MPR`; [D], WIP, not rerun). Context only.

| Records | Declared cells | Instance | `A`'s record law against `y` |
|---|---|---|---|
| H, block | none | `g = 1`, `T = 1` | total variation `1/q`; `|S_CHSH| ≤ 2 + 2/q` |
| S, block | none or `r_O` | `g = 1`, `T = 1` | `0`; table Bell-local |
| H or S, block | `r_O` (S), label `0` | `g = 0`, `T = 1` | `1` |
| H or S | blank line of `3D/2` cells | any `D` even, `T = D/2` | `1` |
| H, one cell | none | B5 | `0` at every `T`; PR-type table at one tick |
| S, one cell | none | B5 | `0`; product table |
| H or S, block | none | `g ≥ 5` in the window | undecided |

**B5. One-cell records [H, Rc under H].** `x_i(1) = u_{i−1} + sel(u_{i+1}, u_{i+2}) − v_i`. Put `α = u_{i−1}(0)`
(wing A's record), `y = u_{i+1}(0)` (B's setting), `x = u_{i+2}(0)` (A's setting).
- **Under H.** `β = x_i(1) + v_i(0)` is a function of `B`'s one-cell history and `β − α = sel(y, x)`. At
  `q = 2`, `α ⊕ β = x ∨ y`: `E(0,0) = +1`, `E = −1` otherwise, `E_{00} − E_{01} − E_{10} − E_{11} = 4`.
  No-signalling: `x_j(t+1)` contains `u_{j−1−t}(0)` with coefficient one through the left-neighbour chain, and
  nothing earlier in cell `j`'s history contains it, so a one-cell history over `T` ticks is uniform on
  `(ℤ/q)^T` and independent of every initial slot other than `u_{j−1}(0), …, u_{j−T}(0)` (`L > T + 3`); the
  generators lie on the other side. (D), (F), (Gen), (Rec) for one-cell regions, (GI) and (MI), (MI\*) hold
  under μ-G (BS:139–157 [D]); (Sep) fails in `G_φ`, where `i+2 → i` is an edge.
- **Under S.** `B`'s state at tick 1 is `(x_i(1), u_i(0))`; `v_i(0)` is absent and masks `x_i(1)`, which is
  then independent of `α`. No PR-type table: the one-tick table is a product. At one tick the table returns under
  S if the record cell's pre-setting slot is known by declaration (a ready record cell).
- *General form.* An observer that knows `u_{j−1}(0)` and `v_j(0)` and sees `x_j(1)` learns
  `sel(u_{j+1}, u_{j+2})(0)`. Knowledge of `v_j(0)` is the resource: a held pre-setting record, a ready slot or
  a label slot.
- *Pressure (favourable outcome, §A.31).* (1) If `B` also holds cell `i−1`, it knows `α` and reads `x` whenever
  `y = 0`; if `B` holds its generator cell `i+1` with both slots, `x_{i+1}(1) = u_i + sel(x, u_{i+3}) − v_{i+1}`
  shows it `sel(x, w′)`, total variation `1 − 1/q` between `x = 0` and `x ≠ 0`. (2) `α` is a pre-existing value
  that does not depend on `A`'s setting; the wings interleave over four adjacent cells. (3) The table is of PR
  type; nothing bounds it at `2√2` (ladder stage 7, LD:104). (4) It needs a hidden, single-use, uniform pad; a
  preparation family of full span forces locality (PPS:136–145). (5) It does not extend beyond two cells per
  tick (B2). (6) At `q = 2` there is no slower nearest-neighbour class to be outside of (B1).
- *What it shows.* Under H the one-tick update at a cell has the form `r += ρ + sel(g_B, g_A)`, the type of
  the ladder's designed map `φ_×` (LD:134, check 1 at LD:145–149). It says nothing about separated wings,
  realistic records or the quantum bound.

**B6. Hypotheses escaped, and measurement independence.**
- Main's theorem and Theorem N/N′: only separation in the actual `G_φ` (hypothesis (iii), Main:369–372;
  (Sep), BS:150), and only inside the two-site cone. Outside it nothing is escaped (B2).
- Proposition AL (LD:187–231): (AL1), the affine update. (AL2)–(AL4) hold in B5 under H.
- (xiv) and (MI\*): under μ-G at the setting slice the generator slots are independent of every other slot, so
  both hold. Under μ-O or μ-R they are not decided, as for the linear rule (OA1:185–188).

**B7. Cone dichotomy for the member [H; proposed by the reviewer of r1, re-derived here].** Let `c_L` be the
physical speed toward decreasing index, in cells per tick. The corpus does not fix it (Main:414: which
propagation sets the light cone "is not derived here").
- *Case `c_L ≥ 2`.* A pair outside the physical cone has `D > c_L·T ≥ 2T`, so B2 applies: no record depends on
  the remote generator, under either convention.
- *Case `c_L < 2`.* Take B4 (0): generator `a+3`, readout region `{a, a+1}`, `T = 1`. The region is at distance
  `2 > c_L·1`, so it is outside the physical cone, and the member's record there equals `y` at label `0`.
  Check of each ingredient: `x_{a+1}(1) = u_a(0) + sel(u_{a+2}(0), u_{a+3}(0)) − v_{a+1}(0)` by §1.1;
  `v_{a+1}(0) = 0` by `r_O` (S) or held (H); `u_a(0)` is in the tick-1 state of cell `a`; at `u_{a+2}(0) = 0`,
  `sel = u_{a+3}(0) = y`. The member's observer then distinguishes remote settings with certainty outside the
  physical cone.
- *Conclusion.* For every value of `c_L` the member has either no dependence outside the physical cone or a
  record that signals outside it. No undecided case is used.
- *Limits.* (1) Lattice scale: two cells, one tick, adjacent blocks. It says nothing about wings many cells
  apart under μ-G with no declared cells between them, where B4 (iii) is undecided and B4 (ii) bounds the
  one-hop effect by `1/q`. (2) Under S the second case uses the declared `r_O`, a writer's choice; without any
  declared cell S gives total variation `0` at one tick (B4 (iii)). (3) It treats the physical cone as sharp
  at the scale of one tick. (4) Toward increasing index the rule behaves as the nearest-neighbour rule (speed
  one) and adds nothing.

**Verdict (b). Member: not supplied at lattice scale. Rule: not established.** Outside its own cone the rule
gives no parameter dependence and is Bell-local under (xiv) (B2). For the member's blocks, whatever speed is
taken as physical toward decreasing index, either B2 covers every pair outside the cone or a record two cells
from the remote generator signals after one tick (B7, with B4 (0) under both conventions). For wings many
cells apart under μ-G the in-window case is undecided (B4 (iii)). With one-cell records under H the dependence
is present without signalling and the table is of PR type (B5); that is a statement about one record
convention, is absent under S, and does not select the quantum set. So for the rule, as opposed to the member,
neither "supplied" nor "not supplied" is established. The ring rule has no preparation-indexed long edge (M3),
so none of this tests H-Bell.

***

## 5. Requirement (c): cell supply

**C1. Unconditional supply under μ-G. None, for any bijective rule [H, Rc].** `Φ` is a bijection, so μ-G is
invariant: at every tick every slot is uniform and independent of the present content of any disjoint set of
cells. No native process leaves a cell at a prescribed value with probability above `1/q` per slot. A heralded
supply remains: a herald that fixes `M` slots is accepted with probability at most `q^{−M}`, with equality
when it reads those slots directly (OA1:156–160, D3; LP:248). The step uses
bijectivity alone (NA:92 [D]).

**C2. Knowledge from held history. Supplied as knowledge, under H [R].** Lemma OBS gives both slots of cell
`a−k` at times in `[k, T−k]` (OA3:245–252), and a gated read gives `u_{a+3}(t)` whenever `u_{a+2}(t) = 0` (A1).
These are values known as functions of records, at whatever values occur; the same holds for the linear rule
with a two-cell block (OA3:262–266).

**C3. What non-linearity changes [H].**
- Under μ-G a bijection preserves the counting law whatever its form, so the candidate adds no unconditional
  producer.
- For an affine rule a cell with known content `c` differs from a zero cell by a known translation of every
  later record (OA1:176–183). The candidate distinguishes the value `0` (P10): the gated read and the lane of
  B3 need `u = 0` exactly.
- *Blanks erode* [H, Rc]. If cells `m..M` have both slots `0` at `t = 0`, then `x_j(1) = 0` is guaranteed only
  for `m+1 ≤ j ≤ M−2`. A blank interval of `n` cells is guaranteed for about `n/3` ticks; no renewing process
  is identified.

**C4. μ-O. Undecided.** Only orbit-constant slots are known unconditionally (as SS:63–64 for R-lin). Gap: the
cycle structure of `Φ` is unknown; by hand only the constant fixed pairs and the travelling solutions of B1
are identified.

**C5. μ-R. Undecided,** as for the linear rule (SS:65).

**Verdict (c).** No unconditional supply under the uniform counting law, for any bijective rule; a herald that
fixes `M` slots is accepted with probability at most `q^{−M}`. Undecided under the orbit and
record-compatible laws. O-RDY (Gap P,
LP:243–248) is unchanged by the candidate; #1278's stop for the binary ring (NA:12) [D] stands.

***

## 6. Joint verdict

- **For this member.** (a): one ingredient supplied (A1), the target undecided. (b): not supplied at lattice
  scale (B7); undecided for wings many cells apart under μ-G. (c): no unconditional supply under μ-G;
  undecided under the other two laws. The member is not shown to meet the three requirements. It is not shown
  that no completion of the ring rule can meet them.
- **Order.** The kernel no-go is rule-blind and is not scored. Of the requirements that depend on the rule,
  (a) is undecided at TUNE-1's interface, and (b) is the first with a derived defect for the member: B2
  confines any effect to `T < D ≤ 2T` toward decreasing index, and inside that window the member's record at
  cell `a+1` signals at `g = 0` under both conventions (B4 (0), readout region `{a, a+1}`) and its block
  signals at `g = 1` under H (B4 (ii)). Under S the `g = 1` instance is decided and does not signal.
- **J1 (conditional) [H].** If a line of `3D/2` consecutive cells is blank in both slots from below `A`'s
  record cell to `B`'s generator, the two-site edge is a deterministic channel toward decreasing index at two
  cells per tick (B3, B4 (i)). Locally, an observer that knows `u_{j−1}`, `v_j` and has `u_{j+1} = 0` reads cell
  `j+2` after one tick; the member's ready cell with label `u_{a+2} = 0` is such a pattern. Requirement (c)
  asks for known-value cells for the ready configuration and the program blocks (LP:245; SS:59–61), not for a
  line between the wings, so J1 constrains where a supply may be placed and is not an exclusion of (c) by (b).
  The channel is not created by the supply: under μ-G and convention H it is already open with probability
  `1/q` per hop (B4 (ii)). "Twice the nearest-neighbour speed" presupposes `K_nz` and `q ≥ 3`; on the vacuum
  reading the two-cell speed is the reference speed.
- **J2 (one mechanism) [H].** The supplied ingredient of (a) and the lattice-scale signalling of (b) are the
  same operation: the gated read at label `0` reads a cell at distance two after one tick (A1, B4 (0)).
- **Undecided nodes.** A4 (small observers, and the member at horizons below `4L − 10`), A5, B4 (iii), C4, C5.
- **No computation is proposed.** The owner's stated condition is "Do not authorize Step 3B, a new candidate
  search, or a G_SM computation until a physically justified O-RDY resource exists and the relevant candidate
  class is adequately specified" (quoted at LP:19–21). On this file's own findings neither condition is met
  (verdict (c); §1.4). For the record only: the design that exists is OA-2's `G_SM` row (OA2:796–814), with two
  record variants and three amendments (OA3:91–92); it concerns a two-cell observer on `ℤ₅`, not the member,
  and either outcome decides condition N-b at that size only. A B4 (iii) computation, were one ever
  authorized, would need controls that can fail: the linear ring inside its cone (`D ≤ T`), where Proposition
  AL predicts total variation `0` or `1` (LD:187–231); `g = 1` under H giving `1/q`; a blank corridor giving
  `1`; and a state readout of the block giving `0` at `T = 1`.

***

## 7. §A.29 accounting

- **Preserved results:** §2, with its stated bound. Losses: P8, P10 (shift part), P16, P21. Holding only on a
  class chosen here: P5–P7. Not assessable or not assessed: P15, P19, P20.
- **Independent consequences, beyond the three requirements [H].**
  1. Any in-cone Bell effect of this rule is confined to timing margins `D/T ≤ 2` and to one orientation of the
     wing pair. The analogous cut-off `√3` for the cubic reference rule, and its cost against large-margin Bell
     tests, is at MP:68–74 [D], which reads the literature from recall.
  2. A zero background carries signals at two cells per tick in one direction and one in the other (B3).
  3. The alphabet value `0` is physically distinguished (P10).
- **Variants adjustable to any outcome (rejected under §A.29 unless fixed by an independent argument).**
  The jump length (SM:112 writes `2`; a family `R = i + D` has cut-off `D`); the distinguished value; mirrored
  or two-sided selectors; a reference class chosen after the result; `q`; the record region and the record
  convention.
- **Hard to vary?** As written the rule has no free structural parameter apart from `q` and `L`, and
  consequences 1–3 are definite. The member is not shown to meet the requirements; the variants not examined
  here are the adjustable ones.

***

## 8. Findings (§A.31 classification)

| # | Finding | Class |
|---|---|---|
| F1 | The kernel's observer theory does not take the rule as input, so its control ceiling is the same for every rule; it does not bear on rule changes at the record-law interface (A3) | CONFIRMING of Main:588 and 3A:498; assumption-watch for plans that read the kernel no-go as evidence for or against a rule |
| F2 | Directed cone of the ring rule, two versus one; corridor lemma on `3k` cells (B3) | ELABORATING (PI:288–291; M2:187, :191) |
| F3 | Ledger (x) holds for this rule on `K_nz` only, a class chosen here; it fails on the vacuum and uniform readings; `K_nz` is not closed but contains travelling solutions (B1, P5–P7) | new at the level of the records read |
| F4 | One-hop signalling of the three-cell member under H, total variation `1/q`, with `|S_CHSH| ≤ 2 + 2/q`; absent under S; total variation `1` at `g = 0` with the ready cell and label `0` under both (B4) | new; by hand |
| F5 | Under H the one-tick update is of the type of the ladder's `φ_×`, and a one-cell protocol gives a no-signalling PR-type table inside the cone; the table needs the record cell's pre-setting slot and is absent under S (B5) | new as a statement about SM's rule; a witness only |
| F6 | J1: a blank line between the wings is a deterministic two-cell-per-tick channel; a known-value supply at an observer's own cells gives a two-cell read | new; conditional on layout |
| F7 | Under μ-G a bijection preserves the counting law whatever its form, so non-linearity adds no unconditional producer; blanks erode at three cells per tick (C1, C3) | CONFIRMING (OA1 D3; NA:92), ELABORATING for erosion |
| F8 | Shift covariance breaks; scaling covariance survives (P10); the linear rule's invariant `E` is not conserved (P21) | ELABORATING (Sub:100, :220); P21 new |
| F9 | No `d = 3` version of the ring rule is written; the `d = 3` non-linear rule that is written (SM:294) is a different rule and is not assessed here (M1, P15) | new at the level of the records read |
| F10 | J2: control ingredient A1 and the lattice-scale signalling of B4 (0) are one operation | new |
| F11 | Every in-cone Bell result here depends on the record convention, H or S (B4 table) | assumption-watch for any two-wing analysis that imports complete histories |

Fixed point not reached: two passes, the second prompted by review; r3 adds wording edits only. Cross-propagation markers: F1, F7 and F11.

***

## 9. What this does and does not show about the non-linear class

**Shows, for the one member of §1.4.**
- SM's ring update is a complete bijection whose labels act other than by translation (A1).
- Its dependence on remote cells is confined to two cells per tick toward decreasing index and one toward
  increasing (B1, B2).
- At lattice scale the member's three-cell blocks, with the declared ready cell, do not give parameter
  dependence without signalling for any choice of physical speed (B7).
- Under the uniform counting law it has no unconditional supply of known-value cells (C1).

**Does not show.**
- That the ring rule with other observers, other declared cells, another law or another record convention
  fails (b): for one-cell records under H the dependence is present without signalling (B5), and for wings
  many cells apart under μ-G the question is undecided (B4 (iii)).
- Whether any isotropic long-wavelength propagation survives for typical configurations, which have zeros
  and so leave `K_nz`: not examined (P7, P8).
- Anything about the rounded rule of SM:294, about a rule with a longer switched edge, or about a `d = 3`
  switched-neighbour rule. None was analysed. A longer edge is a different candidate with a free parameter.
- Anything about H-Bell: its object is preparation-indexed long edges (Sub:131–133), which this rule lacks.
- That a non-linear rule can or cannot meet TUNE-1's single-qubit target: T1 was not applied (A5).
- That no non-linear rule supplies cells: C1 is a statement about the uniform counting law and holds there
  for every bijection by its own argument; under the orbit and record-compatible laws nothing is decided.
- Any property of non-linear rules as a class. The three rule-free statements used (the kernel's `rfl`, NL-C
  and the invariance of the counting law) hold for every rule by their own proofs and are not findings of
  this analysis.

***

## 10. Reference table (§A.42 item 8 form)

| Reference | Attached to | Classification |
|---|---|---|
| `papers/Main.md`, `papers/SM.md`, `papers/Substratum.md`, `papers/GR.md` at `c3b5f37a` | §§1–7 | support on `main` [P] |
| `SubstratumInterfaceAudit.lean`, `FrozenSourcing.lean`, `DiscreteCompletion.lean`, `StructuralClosure.lean`, `ExecSource.lean`, `SecondOrderLayer.lean` | P2, A3 | support on `main` [K], statements read |
| OA-1 r5, OA-2 r4, OA-3 r4, mechanism-2, prepared-pair-source, physical-interface, TUNE-1 Step 2 sessions 3–4 | A1–A5, B2, C1–C2, §6 | support on `main` [R]; research records, not established (§A.46 item 7) |
| Step 3A r3 (`8228b3c2`); TUNE-1 landing notes (`ea9bff9c`) | §1.4 schema, A3 prior art, Gap S, Gap P, C4–C5, the owner condition quoted in §6 | support off `main`: a gap if this file were ever landed before them. The owner condition is quoted from the landing plan, not from the host record |
| Bell ladder r3 (`d8e4f80e`), Bell-scope r2 (`e1534b08`), SB L3 extract (`a0fa2502`) | B2, B5, B6 | support off `main`: gap for Proposition AL, Theorem N/N′ and the directed form; the exogenous theorem Main:364–389 is on `main` |
| Mixed-path unit and Stage 2 output (`a8fff57a`) | B4 context, §7 item 1 | provenance; no verdict here rests on it |
| #1278 assessment (`d8b74527`) | C1, verdict (c) | provenance |
| `REVIEW-r1.md`, `CONFIRM-r2.md`, `RESPONSE-r1.md` (beside this file) | [H, Rc] tags; B7; B4 (0); the S-convention derivations; the wording edits N1–N5 | review provenance; each derivation adopted from the review was re-derived here |

The owner instruction in the header is quoted as relayed; its host record (Issue, comment id, author, time)
was not available to the writer and must be quoted before this file is cited anywhere (§A.42 item 7). S4:608–611
records that no further work on NL-A / NL-P was authorized at that time; the present instruction is the
record that would supersede it for this unit.

**Not included.** The confirmation review offers an optional refinement, O1 (`CONFIRM-r2.md` §8): a reviewer's
sketch that under S with no declared cell the in-window case is decidable. It is not re-derived or used here,
and by its own statement it does not cover the member, whose ready cell is declared, nor convention H.
