# NLCAND r1: the SM ring rule as one non-linear candidate, tested jointly for control, Bell and cell supply

**WIP / unverified. Paper-only writer draft; hand reasoning only; unreviewed. Authorizes nothing, adopts no
premise, proposes no manuscript edit. The hypothesis H-nl ("the world's rule is non-linear") is named and
unadopted throughout, and nothing here recommends adopting it.**

- **Scope.** Owner instruction of 2026-11-14, as relayed to the writer: "Specify one non-linear candidate.
  Start from the SM ring rule and test all three requirements jointly: control, parameter dependence without
  signalling, and cell supply." Paper-only.
- **What was done.** Source reading and hand derivations. No script computed on any OI rule or model; no
  enumeration, simulation, probe replay or Lean build. Stored outputs of earlier runs were read, not rerun
  (`NOTES-r1.md`).
- **Pins.** `main` = `c3b5f37a354bb26437e2e0165c576a347a63c153`. `Main:n`, `SM:n`, `Sub:n` are lines of
  `papers/Main.md`, `papers/SM.md`, `papers/Substratum.md` there. With `R` =
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
  `verification/lean-mathlib/OIBridge/` on `main`, read, not rebuilt.
- **Tags.** [P] manuscript on `main`; [K] Lean statement read; [R] research record on `main` (model-reviewed,
  not verification, §A.46 item 7); [D] draft off `main`; [H] hand derivation in this file, unreviewed.

***

## 0. Answer

1. **The candidate.** SM's ring rule exactly as written (SM:112): second-order update on a ring over `ℤ/q`,
   left neighbour fixed, right neighbour `i+1` or, when cell `i+1` holds `0`, `i+2`. It is a complete bijective
   update (§1.2). The member is completed with the uniform counting law, a three-cell observer block with
   complete history, cell-content labels and one-cell setting generators (§1.4).
2. **Missing from the manuscript.** The update is not missing. What the manuscript does not give for it: any
   version in `d = 3` with six components; the set of configurations that make up its reference class; any
   edge longer than two sites; and every interface datum (law, observer, readout, preparation, generators).
3. **Preserved results (§2).** Bijectivity, the second-order kernel layer, `S ⇔ D ⇔ Q_fb`, the cone lemma and
   the Bell ceiling (both read on the rule's own graph), centre independence and time-reversal symmetry survive.
   The nearest-neighbour graph, the wave-rule form and the dispersion survive on a reference class that the
   dynamics does not preserve. Shift covariance of the alphabet and reflection covariance of the update break.
   Every `d = 3` result is undetermined, because no `d = 3` rule exists.
4. **(a) Control.** A label action that is not a translation: supplied [H; prior art OA3:509–511]. Exact
   continuously tunable mixing: not supplied; the kernel result holds for every substratum rule within the
   stated observer architecture [K]. An approximate single-qubit interface: undecided; the gap is NL-P.
5. **(b) Bell.** Not supplied for the member. Outside the rule's own cone (two sites per tick toward decreasing
   index, one toward increasing) there is no parameter dependence and the member is Bell-local under (xiv).
   Inside it the dependence is real and one-way; for the member's observer blocks it signals (total variation
   `1/q` at one hop under the uniform law, `1` through a corridor of known zero cells). With records cut to one
   cell it is no-signalling and the table is of PR type (CHSH 4 at `q = 2`), with no bound at `2√2`.
6. **(c) Cell supply.** Not supplied under the uniform counting law (a bijection preserves it, whatever its
   form). Undecided under the orbit and record-compatible laws, with the same gaps as for the linear rule.
7. **Joint.** One mechanism does not meet all three. In exact form (a) fails first, for every rule of the form (xiii); in
   TUNE-1's approximate form (a) is undecided and (b) is the first requirement that fails on a derivation.
   (b) and (c) pull against each other: known zero cells turn the two-site edge into a channel at twice the
   reference speed (J1, §6).

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

### 1.2 Bijectivity and reversal, by hand [H]

Put `Ψ(a, b) = (b, f(b) − a)`. Then `Ψ(Φ(u, v)) = Ψ(f(u) − v, u) = (u, f(u) − (f(u) − v)) = (u, v)` and
`Φ(Ψ(a, b)) = Φ(b, f(b) − a) = (f(b) − (f(b) − a), b) = (a, b)`. So `Φ` is a bijection of `(ℤ/q)^{2L}` for
every `L ≥ 4`, every `q ≥ 2` and every map `f`; this agrees with SM:106 and SM:112. With the slot swap
`σ(u, v) = (v, u)`: `σΦσ(u, v) = σ(f(v) − u, v) = (v, f(v) − u) = Ψ(u, v)`, so `Φ⁻¹ = σΦσ` for every `f`.
Spot check, `L = 4`, `q = 2`, `u = (1,0,0,1)`, `v = 0`: `f(u) = (1,0,1,1)`, `Φ(u, v) = ((1,0,1,1),(1,0,0,1))`,
and `Ψ` of that is `((1,0,0,1), f(1,0,0,1) − (1,0,1,1)) = (u, 0)`.

### 1.3 What the manuscript does not define

- **M1. No rule in `d = 3`.** SM:112 is a one-component ring. The statements that follow it quantify over a
  class ("bounded-degree graph G(x) satisfying constraints (i)–(iii)", SM:144) of which no `d = 3`,
  six-component member is written anywhere searched (`NOTES-r1.md`). Which neighbour would be switched, by
  which cell, compatibly with the octahedral symmetry the gauge sector uses, is unspecified.
- **M2. The reference class as a set of configurations.** SM:108 and Main:362, :724 name "the reference
  vacuum/uniform state class" without listing its members. For this rule the readings differ (node B1):
  current slices with no zero give the nearest-neighbour ring; the all-zero configuration, where the selected
  neighbour is `i+2` everywhere, and the support of the uniform law both give the full two-site graph.
- **M3. Long edges.** The only switched edge has length two. Sub:131 speaks of "bounded-degree Bell-relevant
  long edges"; no update containing one is written, nor a process that prepares one (PPS:81).
- **M4. Interface data.** SM:112 fixes a visible sector only for its P-indivisibility remark ("one site's two
  time slices"). Law, observer region, readout, preparations, generators and control region are chosen in
  §1.4. `q` and `L` are left free by SM:112.

### 1.4 Member specification

| Item | Value | Source or choice |
|---|---|---|
| Rule, carrier | `Φ` of §1.1 on a ring of `L` cells, each cell a pair `(u_i, v_i) ∈ (ℤ/q)²` | taken, SM:112 |
| Memory sign, distinguished value `0`, jump length `2` | as written | taken, SM:112 |
| `q` | free. Statements hold for every `q ≥ 2` unless marked; witnesses marked `q = 2` use `sel = ∨` | free parameter (SM:112) |
| `L` | free, taken `≥ 4T + 8` for horizon `T`, so that no dependency path wraps | chosen. Reason: at horizons `≥ 4L − 10` a three-cell observer with held history has a simplex fragment (OA3:306–314); the choice keeps the member outside that proved classical regime. In one fixed finite world it cannot be kept at long horizons |
| Law | μ-G, uniform on `(ℤ/q)^{2L}` (ledger (iv), uniform reading; OA1:103–105) | chosen as the task's default; μ-O and μ-R are treated in §5 |
| Observer region `O` | three consecutive cells `{a, a+1, a+2}`, both slots, read at every tick | chosen. Reason: the smallest block with results on `main` (OA3:225–234); `|O| ≤ 2` is the open case (OA3:498–518) |
| Readout | complete history of `O` (D4-type; an MP-0b-type convention, 3A:501); outcomes are functions of it | imported convention |
| Control region `C` | `{a, a+2} ⊂ O`, both slots; menu of `q⁴` labels | chosen. Reason: `u_{a+2}` gates the read of world cell `a+3` (A1); `u_a` is written into world cell `a−2` on a world condition (A1) |
| Ready configuration `r_O` | cell `a+1` at `(0, 0)` | free; declared initial condition of the MP-0a type, unsourced (3A:493) |
| Round length | one tick | free |
| Preparation prefixes | initial-condition mode: the label is the content of `C` at `t = 0`; a herald is a condition on the held history; nothing writes but `Φ` | TUNE-1 schema (3A:466–470) |
| Two wings | two such blocks, `A = {a..a+2}` on the lower-index side and `B = {b..b+2}`, `g = b − a − 3` unread cells between; generator of each wing: one of its cells, setting = its `u`-slot at `t_s = 0` | chosen; the lower-index wing is the one the two-site edge reaches |
| One-cell variant (B5 only) | records `{i−1}` (A), `{i}` (B); generators `{i+2}` (A), `{i+1}` (B) | chosen to exhibit the gadget; not the member's observer |

**Not supplied, and not readable from the manuscript:** the generating rule for more than one round (layout
of program blocks and how their content reaches `O`), a declared target with its separation length and
constant, and the label encoder (items 1–3 of 3A:913–931). The member is therefore specified for one-round
label actions and for the two-wing protocol, and is not a Step 3B-qualifying family. Gap S (LP:243) stays open.

***

## 2. Results the replacement of ledger (vii) must preserve

The list of results (first column) was fixed before §§3–5 were written. The outcomes use only §1.2 and the
graph facts of node B1, and were not revised after the requirement verdicts. "Reference class only" means:
holds on `K_nz`, the configurations whose current slice has no zero (node B1).

| # | Result | Outcome | Reason |
|---|---|---|---|
| P1 | Bijectivity (ledger (iii)) | survives | §1.2 |
| P2 | Second-order form (xiii) and the kernel layer stated for it (`ruleDynamics`, quasilocal completion, the path of automorphisms; Main:588) | survives | the Lean `Rule` carries an arbitrary finite-range `F` (`SecondOrderLayer.lean`:198–203) [K] |
| P3 | `S ⇔ D ⇔ Q_fb`; characterization theorem of Main §3.4 | survives | no rule and no spatial constitution enters (Main:724, items (viii)–(xiii) "which the characterization theorem of §3.4 does not use") |
| P4 | Cone lemma (Main:362); Bell ceiling (Main:364–389) | survive, read on this rule's graph | they need site factorization and the actual dependency graph only; in-neighbourhood `{i−1, i+1, i+2}` (B1). The Corollary Main:414 is stated for the nearest-neighbour cubic update and no longer describes the rule |
| P5 | Ledger (x), nearest-neighbour graph on the reference class | reference class only | B1: `G^K` is the nearest-neighbour ring for `K = K_nz` and for no larger class; `K_nz` is not closed for `q ≥ 3`, and at `q = 2` only one of its configurations stays in it |
| P6 | Form lemma and wave-rule selection (SM:224; Sub:159) | reference class only, one step at a time | the lemma's hypothesis is linearity; on `K_nz` one step of `Φ` equals the `α = 1` nearest-neighbour rule; the lemma no longer selects the rule |
| P7 | Dispersion `cos ω = cos k` (SM:126) and what rests on it | reference class only; undetermined off it | a statement about trajectories, and trajectories leave `K_nz` |
| P8 | Reflection covariance of the update (isotropy in `d = 1`; ledger (vi)) | breaks | reads are directed: `i` reads `i+2` and never `i−2` (M2:191). SM:108 (iii), a statement about the undirected graph's statistics, holds |
| P9 | Centre independence, both clauses (xi); bounded degree (ix) | survive | `f_i` does not read `u_i`; same rule at every site; three in-neighbours (SM:112; M2:187–189) |
| P10 | Amplitude-scale gauge (SM:96, :240; Sub:100) | scaling survives, shift breaks | `sel(λa, λb) = λ·sel(a, b)` for units `λ`; the shift `x ↦ x + c` turns the test "`= 0`" into "`= c`". The affine lemma's premise fails, as it must for a non-affine rule (`f(δ_{i+1} + δ_{i+2}) − f(δ_{i+1}) − f(δ_{i+2}) = −1`) |
| P11 | Time-reversal symmetry of the update (SM §5.1) | survives | `Φ⁻¹ = σΦσ`, §1.2 |
| P12 | Recurrence-cycle P-indivisibility for a one-site visible sector | survives | asserted for this rule at SM:112 |
| P13 | Mod-`q` boundary bound `I(V; V^c) ≤ |∂V| log₂ q` (SM:122–124) | survives with `∂V` read in the union graph | the Markov argument needs every in-neighbour of an interior cell inside `V`; that holds with a boundary two cells deep. For a boundary read in the configuration's own graph (SM:150) the argument is not re-derived here |
| P14 | Discrete Einstein equation | nothing to preserve | target form with an open curvature step (SM:144–150) |
| P15 | Gauge sector, six-link carrier, generations (`d = 3`) | undetermined | M1: no `d = 3` rule. Theorem 7 (link geometry) does not depend on the rule |
| P16 | Linear-rule spectral results (SM Appendix A; cycle-structure Remark, SM:296) | inapplicable to the candidate | they use the module structure of an additive map; they remain theorems about the linear rule |
| P17 | Kernel no-go on control (Main:588) | survives | rule-independent (A3) |
| P18 | Hidden-sector mixing (ledger (v)) | undetermined | no result for this rule |

Two results about the candidate itself constrain every node: Lemma OBS (a held three-cell block with history
determines the whole finite ring within `2(L−3)` ticks, OA3:225–260 [R]) and Theorem S (simplex fragment at
horizons `≥ 4L − 10`, OA3:296–347 [R]).

***

## 3. Requirement (a): control

**A1. Is there a label action that is not a translation? Supplied [H].**
- *Gated read.* `x_{a+1}(1) = u_a + sel(u_{a+2}, u_{a+3}) − v_{a+1}`, with `u_a`, `v_{a+1}` held. For label
  `ℓ = u_{a+2} ≠ 0` the record is `u_a + ℓ − v_{a+1}`, a point mass. For `ℓ = 0` it is `u_a + w − v_{a+1}` with
  `w = u_{a+3}(0)` an unread cell, uniform under μ-G. Total variation between label `0` and a non-zero label is
  `1 − 1/q`, which lies in `(0, 1)` for every `q ≥ 2`. Lemma A-T (d)'s `0`-or-`1` dichotomy (S3:73–76), which
  holds for R-lin, fails; the functional read depends on the label, unlike the affine case (D5 (ii), OA1:176–183).
- *Controlled write.* `x_{a−2}(1) = u_{a−3} + sel(u_{a−1}, u_a) − v_{a−2}`: the label `u_a` is added into world
  cell `a−2` exactly at world states with `u_{a−1} = 0`. As a map on world configurations this is a translation
  on one part of the world's state space and the identity on the rest.
- *Control off.* With `R ≡ i+1` both reduce to translations, as Lemma A-T requires.
- *Standing.* CONFIRMING: OA3:509–511 records the same non-translational setting action at `q = 2`, and
  OA2:681 records condition N-a as met.

**A2. Which gate family? Characterized [H].** One tick is `v_i ↦ f_i(u) − v_i` at every cell followed by the
slot swap. Each `f_i` adds, into the target slot, `u_{i−1}` and a value selected by a zero test. Label-indexed
actions are therefore compositions of translations and zero-controlled translations: permutations of the
configuration set. At `q = 2`, `f_i = u_{i−1} ⊕ u_{i+1} ⊕ u_{i+2} ⊕ u_{i+1}u_{i+2}` (M2:157–164), a
doubly-controlled bit flip with two singly-controlled ones. Whether these generate every reversible classical
circuit on prepared cells is not shown here. OA-2's reversible computer `𝔊_K` (OA2:381–490) is a designed
map, not this rule, and is not evidence about it.

**A3. Exact tunable mixing. Not supplied; rule-independent [K].** `obs_not_layerFlowExecutable` is stated for
every `Substratum`, whose `Rule` is arbitrary (`ExecSource.lean`:125–134; `SubstratumInterfaceAudit.lean`:60–66;
`SecondOrderLayer.lean`:198–203), and `substratumGen_not_control` (`StructuralClosure.lean`:348–356) rests on
admissible operators being monomial. Main:588 states the result for "finite bijective read-write dynamics".
OA1:196–200 [R] gives the same ceiling for any theory generated from configuration bijections. Replacing
ledger (vii) by any bijective rule leaves this obligation as it is: at the exact level the control gap does
not trace to linearity. Scope of the kernel statement: the stated observer architecture; it does not decide
the observer-level lift or a richer architecture (`ExecSource.lean`:28–30), and Main:588 leaves the site-space
wave-operator formulation unresolved.

**A4. Necessary condition for a non-classical fragment at small size. Undecided.** For observers of at most
two cells and horizons below Theorem S's bound, whether the gated reads give a prepare–measure fragment that is
not simplex-embeddable (condition N-b, OA2:682) is open (OA3:498–518, :531). Exact gap: the reachable laws and
available effects of that fragment have not been enumerated. This is the first undecided node (§6).

**A5. The single-qubit target T1. Undecided; gap NL-P.**
- NL-C uses no property of the rule (S4:423–462). With `|C| = 2`, `q = 2`: `M = 16` labels, so Q6′(i) fails at
  every `ε < sin(π/17)/8 ≈ 0.023` (hand value). A pass at small `ε` needs
  `|C_n| ≥ ½ log_q((1−4ε)/(4ε))` (S4:464–474), and the candidate supplies no mechanism for that growth.
- A1 removes the one proved obstruction specific to the linear rule (labels act by translation, OA1:176–195;
  Lemma A-T). It does not show a composing one-parameter family of gate rounds (Q3′, Q4; 3A:800–801).
- The family that T1 quantifies over (3A:913–931, items 1–3) is not specified (§1.4), so T1 cannot be applied.
- Two constraints already on `main` bound where a pass could live: horizons `T ≪ L` only (Theorem S), and, on
  the lower-index side of `O`, unread cells to depth `T/2` are recoverable from the held history (Lemma OBS,
  OA3:245–252), so persistent incompleteness there is limited to deeper cells and to the higher-index side,
  which is read only through `sel`.

**Verdict (a).** Non-translational label action: supplied. Exact continuously tunable mixing: not supplied, for
every rule. Approximate single-qubit control: undecided, with the gap NL-P and the growth of `|C_n|` unsourced.

***

## 4. Requirement (b): parameter dependence without signalling

**B1. Does the one-step graph differ between states? Supplied, within two sites [H].** `x_i(t+1)` depends on
`u_{i−1}` at every state; on `u_{i+2}` at the states with `u_{i+1} = 0` and at no others; on `u_{i+1}` at every
state for `q ≥ 3`, and at `q = 2` at the states with `u_{i+2} = 0`. So in Main:362's notation: `G_φ` has
in-neighbourhood `{i−1, i+1, i+2}`; `G_φ^K` is the nearest-neighbour ring for `K = K_nz`; for `K` the support of
μ-G, `G_φ^K = G_φ`. `K_nz` is not closed for `q ≥ 3` (`u ≡ 1`, `v ≡ 2` gives next slice `≡ 0`); at `q = 2` it
is the set `u ≡ 1`, whose only member that stays in it is the fixed pair `u = v ≡ 1`, and there the output
depends on neither right neighbour. Under μ-G each two-site edge is active with probability `1/q` per tick.
Directed speeds: at most two cells per tick toward decreasing index, one toward increasing (ELABORATING; the
symmetric envelope "ring distance 2t" is PI:288–291).

**B2. Wings outside the rule's own cone. Not supplied (Bell-local) [P on H].** With `A` on the lower-index
side at separation `D` (generator of one wing to the nearest record cell of the other) and a window of `T`
ticks: if `D > 2T`, no record of either wing depends on the other's generator (cone lemma, Main:362, with B1),
and under (xiv) Main's theorem gives `|S_CHSH| ≤ 2` (Main:364–389; closed form BS:159–178 [D]; directed form
L3:46–50 [D]: `D > 2T` for `B → A`, `D > T` for `A → B`). Already recorded for this rule at PPS:79, :164 and
PI:293–299. The rule as written therefore cannot serve wings whose separation exceeds twice the window.

**B3. Inside the cone: pointwise dependence. Supplied, one-way [H].** *Corridor lemma.* Let both slots be `0`
at every cell below `s`, and `u_s(0) = y`; the content of `v_s` and of the cells above `s` is arbitrary. Then
`x_{s−2k}(k) = y` and `x_j(k) = 0` for `j < s − 2k`, for every `k ≥ 1` (no wrap).
*Proof.* Induction on `k`; the hypothesis at `k−1` and `k−2` gives zeros at all `j < s − 2k + 2` at time `k−1`
except `x_{s−2k+2}(k−1) = y`, and zeros at all `j ≤ s − 2k` at time `k−2`. For `j < s − 2k`:
`x_j(k) = 0 + sel(0, 0) − 0 = 0`. For `j = s − 2k`: `x_j(k) = 0 + sel(x_{s−2k+1}(k−1), x_{s−2k+2}(k−1)) − 0 =
sel(0, y) = y`. Base: `x_{s−2}(1) = 0 + sel(0, y) − 0 = y`, `x_j(1) = 0` for `j < s − 2`. ∎ So in a zero
background a cell value is copied two cells per tick toward decreasing index; on trajectories that stay in
`K_nz` the same influence moves one cell per tick. Toward increasing index the speed is one in every
background (only the left-neighbour read carries it). The window "inside the union cone, outside the
reference-class cone" is `T < D ≤ 2T`, for the lower-index wing only.

**B4. Is the dependence hidden from the member's observers? No [H], with one undecided case.**
- *(i) Prepared corridor.* If the cells below `B`'s generator, `A`'s own included, are blank in both slots, B3
  gives `A` the value `y` exactly at tick `D/2` (`D` even): total variation `1` between any two remote
  settings. This is the resource requirement (c) asks for (J1).
- *(ii) One hop under μ-G, `g = 1`.* `A`'s edge cell: `x_{a+2}(1) = u_{a+1} + sel(w, y) − v_{a+2}`, with `w` the
  one unread cell and `y = u_{a+4}(0)` `B`'s setting; `u_{a+1}`, `v_{a+2}` are held. `P(sel(w, y) = c) =
  [c ≠ 0]/q + [c = y]/q`. For `y ≠ y′` the laws differ at `c = y` and `c = y′` by `1/q` each: total variation
  `1/q` (`½` at `q = 2`). `A`'s complete history signals. Here `D = 2 > T = 1`.
- *(iii) Padded window, `g ≥ 2`.* By Lemma M (S4:94–101) the slice at tick 1 outside `A` is uniform and
  independent of `u(0)`, so `y` first acts through `x_b(2) = f_b(u(1)) − y`, then along the two-site lane.
  `A`'s edge cell can first depend on it at tick `3 + ⌊g/2⌋` (consistent with Lemma S, MP:320–334 [D]). That
  precedes the one-cell-per-tick arrival, tick `g + 1`, only for `g ≥ 5`. First instance: `g = 5`, `D = 6`,
  `T = 5`. Whether `A`'s history law depends on `y` there is **undecided**: the pads on that path (`u`-slots at
  tick 1) are read by several cells and are not single-use, and `sel` outputs are not uniform
  (`P(sel = 0) = 1/q²`), so neither masking nor signalling follows by hand.
- *Stored comparison, not this rule.* The mixed-path Stage 2 run on the rounded rule R-round (small `d = 3`
  tori, `q = 2, 3`) reports headline `SIGNALLING-FOUND`: over its primary instances 37 signalling, 10 masked
  and Bell-local, 70 without dependence, and no non-local table among the no-signalling ones (`MPR`, fields
  `verdicts.counts`, `nonlocal_among_nonsignalling`; [D], WIP, not rerun here). It is context for (iii), not
  evidence about the ring rule.

**B5. One-cell records: a no-signalling table of PR type inside the cone [H; witness, not a mechanism].**
`x_i(1) = u_{i−1} + sel(u_{i+1}, u_{i+2}) − v_i`. Put `α = u_{i−1}(0)` (wing A's record), `y = u_{i+1}(0)`
(B's setting), `x = u_{i+2}(0)` (A's setting), `β = x_i(1) + v_i(0)` (a function of B's one-cell history). Then
`β − α = sel(y, x)`; at `q = 2`, `α ⊕ β = x ∨ y`: `E(0,0) = +1`, `E = −1` otherwise, and
`E_{00} − E_{01} − E_{10} − E_{11} = 4`.
- *No-signalling, complete one-cell histories, μ-G.* `B`'s history `(u_i, v_i, x_i(1))` is uniform given
  `(x, y)` because `α` is uniform and independent of the rest. `A`'s history `(u_{i−1}, v_{i−1}, x_{i−1}(1))` is
  uniform because `x_{i−1}(1)` contains `u_{i−2}(0)`. For longer windows, `x_j(t+1)` contains `u_{j−1−t}(0)` with
  coefficient one through the left-neighbour chain, and nothing earlier in cell `j`'s history contains it, so a
  one-cell history over `T` ticks is uniform on `(ℤ/q)^T` and independent of every initial slot other than
  `u_{j−1}(0), …, u_{j−T}(0)` (`L > T + 3`); the generators lie on the other side.
- *Hypotheses.* (D), (F), (Gen), (Rec) for one-cell regions, (GI) (no record reads a generator's `v`-slot) and
  (MI), (MI\*) hold under μ-G (BS:139–157 [D]). (Sep) fails in `G_φ`: `i+2 → i` is an edge. In the
  nearest-neighbour graph the generators are at distance two from the remote records, with `T = 1`.
- *Pressure (favourable outcome, §A.31).* (1) It is not the member's observer: if `B` also holds cell `i−1`, it
  knows `α` and reads `x` whenever `y = 0`; if `B` holds its generator cell `i+1` with both slots, then
  `x_{i+1}(1) = u_i + sel(x, u_{i+3}) − v_{i+1}` shows it `sel(x, w′)`, total variation `1 − 1/q` between `x = 0`
  and `x ≠ 0`. No-signalling rests on a record region of one cell (the open record-convention item of LD:274).
  (2) `α` is a pre-existing cell value that does not depend on `A`'s setting; the wings interleave over four
  adjacent cells. (3) The table is of PR type; nothing bounds it at `2√2` (ladder stage 7, LD:104: undetermined).
  (4) It needs a hidden, single-use, uniform pad: with `α` fixed by a preparation, `B`'s record shows
  `sel(y, x)`. A preparation family of full span forces locality (PPS:136–145). (5) It does not extend: beyond
  two cells per tick B2 applies, and a relay over the lane is B4. (6) At `q = 2` there is no slower
  reference-class cone to be outside of (B1).
- *What it shows.* The candidate's one-tick update at a cell has the form `r += ρ + sel(g_B, g_A)`, the type of
  the ladder's designed map `φ_×` (LD:134, check 1 at LD:145–149). Proposition AL's affine hypothesis is
  what excludes such tables for R-lin; the ring rule lacks it.

**B6. Hypotheses escaped, and measurement independence.**
- Main's theorem and Theorem N/N′: only separation in the actual `G_φ` (hypothesis (iii), Main:369–372;
  (Sep), BS:150), and only for wings inside the two-site cone. For wings outside it nothing is escaped (B2).
- Proposition AL (LD:187–231): (AL1), the affine update. (AL2) a coset-uniform law, (AL3) cell-valued settings
  and (AL4) fixed regions hold in B5. With (AL4) and no-signalling on the member's three-cell blocks, the
  examined cases give signalling (B4 (i), (ii)) or are undecided (B4 (iii)).
- (xiv) and (MI\*): under μ-G at the setting slice the generator slots are independent of every other slot, so
  both hold. The rule does not obstruct them. Under μ-O or μ-R they are not decided, as for the linear rule
  (OA1:185–188).

**Verdict (b). Not supplied.** The candidate gives ontic parameter dependence only inside its own two-site
cone and only toward decreasing index. Outside that cone it is Bell-local under (xiv) and the protocol
hypotheses of Main:364–389. Inside it, the member's observers either see the remote setting (B4 (i), (ii)) or
the case is undecided (B4 (iii), first instance `(D, T) = (6, 5)`); the one-cell protocol is no-signalling and
of PR type, which is not the quantum set. Requirements (i) and (ii) of H-Bell (Sub:133) are not met jointly by
this rule, and (iii) is not reached.

***

## 5. Requirement (c): cell supply

**C1. Unconditional supply under μ-G. Not supplied [H; rule-free].** `Φ` is a bijection, so μ-G is invariant:
at every tick every slot is uniform and independent of the present content of any disjoint set of cells. No
cell has a known value except by a herald, and fixing `M` slots costs probability `q^{−M}` (OA1:156–160, D3).
The step uses bijectivity alone (NA:92 [D] notes the same), so replacing (vii) cannot change it.

**C2. Knowledge from held history. Supplied as knowledge, not as a ready resource [R].** With the history
held, Lemma OBS gives both slots of cell `a−k` at times in `[k, T−k]` (OA3:245–252), and a gated read gives
`u_{a+3}(t)` whenever `u_{a+2}(t) = 0` (A1). These are values known as functions of records, at whatever values
occur. The same holds for the linear rule with a two-cell block (OA3:262–266). It rests on the convention that
the history is held (MP-0b type).

**C3. What non-linearity changes [H].**
- A bijection preserves the counting law (C1), so no rule of the form (xiii) concentrates probability on blank
  cells; the candidate adds no producer.
- For an affine rule a cell with known content `c` differs from a zero cell by a known translation of every
  later record (OA1:176–183). The candidate distinguishes the value `0` (P10): the gated read and the lane of
  B3 need `u = 0` exactly, so a known non-zero cell does not substitute.
- *Blanks erode.* If cells `m..M` have both slots `0` at `t = 0`, then `x_j(1) = 0` is guaranteed only for
  `m+1 ≤ j ≤ M−2` (the left neighbour and both right neighbours must be blank). A blank interval of `n` cells
  is guaranteed for about `n/3` ticks; nothing renews it.

**C4. μ-O. Undecided.** Only orbit-constant slots are known unconditionally (as SS:63–64 for R-lin). The exact
gap: the cycle structure of `Φ` is unknown; the only orbits identified by hand are the constant fixed pairs
`u = v ≡ c`.

**C5. μ-R. Undecided,** as for the linear rule (SS:65). C2 says what the records fix; whether the
record-compatible law supplies a prescribed ready pattern, renewed per run, is not addressed by any source read.

**Verdict (c).** Not supplied under the uniform counting law; undecided under the orbit and record-compatible
laws. O-RDY (Gap P, LP:243) is unchanged by the candidate; #1278's stop for the binary ring (NA:12) [D] stands.

***

## 6. Joint verdict

- **All three by one mechanism: no.** (a) non-translational control is supplied and nothing more is shown;
  (b) is not supplied; (c) is not supplied under μ-G.
- **First failure.** In exact form, (a) at A3: within the stated observer architecture no substratum rule
  supplies continuously tunable mixing. In TUNE-1's approximate form (a) is undecided, and the first failure
  on a derivation is (b) at B2: a bounded jump length gives a bounded cone, and outside it the Bell ceiling
  applies.
- **J1 (joint constraint) [H].** By B3 and B4 (i), any supply of blank cells (both slots `0`) along a line
  makes the two-site edge a deterministic channel at twice the reference-class speed, toward decreasing index. Within
  this candidate, (c) and "no signalling outside the reference cone" exclude each other. They are compatible
  only if the physical cone is the union cone, and then there is no Bell window (B2).
- **First undecided node: A4.** *Cheapest decisive check (described, not run; needs its own authorization):*
  the `G_SM` row of OA-2's design sketch (OA2:796–814): `q = 2`, ring `ℤ₅` (`2^{10}` configurations), observer
  cells `{0, 1}`, setting `u_0(0)`, ready cell 1 at `(0, 0)`, carrier cell 2, cells 3–4 uniform, horizon
  `T ≤ 4`; exact enumeration of the closure-defined prepare–measure fragment and an exact-rational
  simplex-embedding linear program, with OA-2's controls (`𝔊_K` non-embeddable, the linear ring embeddable,
  non-vacuity) and OA-3's three design amendments (OA3:91–92). Embeddable: classical at that size, horizon and
  convention only. Non-embeddable: the necessary condition N-b at that size; not T1, since a designed classical
  computer also passes it (OA2:381–490).
- **Next undecided node, B4 (iii).** An exact computation of `A`'s five-tick history law at `g = 5`, `q = 2`,
  for the two values of `y`, over the unread cells in `A`'s backward cone. Controls: `R ≡ i+1` must give total
  variation `0` (Proposition AL, LD:187–231); `g = 1` must give `½` (B4 (ii)); a known zero corridor must give
  `1` (B3).

***

## 7. §A.29 accounting

- **Preserved results stated in advance:** §2. Three entries are losses, not preservations (P8, P10 shift
  part, P16), three hold on a class the dynamics leaves (P5–P7), and P15 cannot be assessed.
- **Independent consequences, beyond the three requirements [H].**
  1. Any in-cone Bell effect of this rule is confined to timing margins `D/T ≤ 2` and to one orientation of the
     wing pair. The analogous cut-off `√3` for the cubic reference rule, and its cost against large-margin Bell
     tests, is at MP:68–74 [D], which reads the literature from recall.
  2. A zero background carries signals at two cells per tick in one direction and one in the other (B3); the
     nearest-neighbour speed holds on `K_nz` only.
  3. The alphabet value `0` is physically distinguished (P10).
- **Variants adjustable to any outcome (rejected under §A.29 unless fixed by an independent argument).**
  The jump length (SM:112 writes `2`; a family `R = i + D` has cut-off `D`, which can be set above any observed
  margin); the distinguished value; mirrored or two-sided selectors; a reference class chosen after the result;
  `q`; the record region (B5).
- **Hard to vary?** As written the rule has no free structural parameter apart from `q` and `L`, and its
  consequences 1–3 are definite. It does not meet the requirements; the variants that might are the adjustable
  ones.

***

## 8. Findings (§A.31 classification)

| # | Finding | Class |
|---|---|---|
| F1 | At kernel level, within the stated observer architecture, the control gap holds for every rule; it does not trace to linearity (A3) | CONFIRMING of Main:588; assumption-watch for any plan that expects a rule change to supply mixing |
| F2 | Directed cone of the ring rule, two versus one; corridor lemma (B3) | ELABORATING (PI:288–291; M2:187, :191) |
| F3 | For this rule ledger (x) holds on `K_nz` only, and `K_nz` is not closed; the manuscript does not list the reference class (M2, P5–P7) | new at the level of the records read (`NOTES-r1.md`) |
| F4 | One-hop signalling of the three-cell member, total variation `1/q` (B4 (ii)) | new; exact, by hand |
| F5 | The one-tick update is of the type of the ladder's `φ_×`; a one-cell protocol gives a no-signalling PR-type table inside the cone (B5) | new as a statement about SM's rule; a witness only |
| F6 | J1: cell supply and no-signalling at the reference speed exclude each other in this candidate | new |
| F7 | A bijection preserves the counting law whatever its form, so non-linearity adds no cell producer; blanks erode at three cells per tick (C1, C3) | CONFIRMING (OA1 D3; NA:92), ELABORATING for erosion |
| F8 | Shift covariance breaks; scaling covariance survives (P10) | ELABORATING (Sub:100, :220) |
| F9 | No `d = 3` non-linear rule is written, so H-nl through this rule cannot be assessed against the gauge sector (M1, P15) | new at the level of the records read |

Fixed point not reached: one pass. Cross-propagation markers: F1 and F7 apply to every candidate rule of the
form (xiii), R-round included; F3 applies to any rule whose graph varies with the state.

***

## 9. Reference table (§A.42 item 8 form)

| Reference | Attached to | Classification |
|---|---|---|
| `papers/Main.md`, `papers/SM.md`, `papers/Substratum.md` at `c3b5f37a` | §§1–7 | support on `main` [P] |
| `ExecSource.lean`, `StructuralClosure.lean`, `SecondOrderLayer.lean`, `SubstratumInterfaceAudit.lean` | P2, A3 | support on `main` [K], statements read |
| OA-1 r5, OA-2 r4, OA-3 r4, mechanism-2, prepared-pair-source, physical-interface, TUNE-1 Step 2 sessions 3–4 | A1–A5, B2, C1–C2, §6 | support on `main` [R]; research records, not established (§A.46 item 7) |
| Step 3A r3 (`8228b3c2`); TUNE-1 landing notes (`ea9bff9c`) | §1.4 schema, Gap S, Gap P, C4–C5 | support off `main`: a gap if this file were ever landed before them |
| Bell ladder r3 (`d8e4f80e`), Bell-scope r2 (`e1534b08`), SB L3 extract (`a0fa2502`) | B2, B5, B6 | support off `main`: gap for Proposition AL, Theorem N/N′ and the directed form; the exogenous theorem Main:364–389 is on `main` |
| Mixed-path unit and Stage 2 output (`a8fff57a`) | B4 context, §7 item 1 | provenance; no verdict here rests on it |
| #1278 assessment (`d8b74527`) | C1, verdict (c) | provenance |

No result of this file is reviewed. Every [H] item is a hand derivation that an independent reader should
re-derive; the ones on which a verdict rests are §1.2, B1, B3, B4 (ii) and B5.
