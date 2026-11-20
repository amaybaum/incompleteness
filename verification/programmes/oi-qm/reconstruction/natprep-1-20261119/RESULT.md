# NATPREP-1: native preparation of delivering components from an untuned source

**Standing.** Author record of a paper-only gem-finding unit (AGENTS.md §A.31, depth-first form).
No independent review yet. It adopts no premise, edits no manuscript, Lean module or registry, and
runs no simulation. Small exact checks are included as controls (§9).

- **Authorization.** Owner `amaybaum`, row P1 of
  [#1169 c.7023834853](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7023834853),
  2026-11-19T22:21:00Z: "**NATPREP-1** (#866): can native dynamics prepare, from an untuned source,
  the active regions that deliver?", boundary "Explicit resource accounting and no imported
  controller. A rigorous obstruction counts as a successful outcome". The same decision states:
  "These are investigation only. None adopts a premise. Each needs independent non-author review,
  and each needs its own merge decision." Scope as assigned to this unit: paper-only; small exact
  checks as controls; no premise adoption; no merge.
- **Goal link (§A.47), from the authorization.** "P1 is the measurement-source bottleneck." The
  work decides, for the declared update U₂, whether an untuned initial law together with the
  native dynamics yields components that later perform a delivery meeting DELIVER-1's task with
  clause (R), and if not, which property of U₂ blocks it. Unchanged, as recorded there: "A1
  OPEN/UNADOPTED; physical measurement sourcing NOT PASSED".
- **Accountable Issues.** #866 (native preparation source), #1169 (OI projection objective).
- **Snapshot.** `main` at `bae5cfdd80758abe86586f47e18cc478c0e1664a`, which contains DELIVER-1
  (merge of #1425; its record is unchanged from `aa64bc99`). Record paths are relative to
  `verification/programmes/oi-qm/reconstruction/`. `DL1` is `deliver-1-20261119/RESULT.md` and
  `DL1 2.3(f)` its item; `PR1` is `prep-regress-1-20261119/RESULT.md`. NSC-1..7 are the clauses
  of PR1 §2, the native-source contract.
- **Productivity test (fixed in advance by the assignment).** The unit is a gem iff it gives either
  (i) an untuned native preparation of delivering components, with its probability and cost, or
  (ii) a scoped obstruction stronger than DL1's, with the blocking property identified.

| Label | Meaning |
|---|---|
| [K] | Lean statement on `main`, cited by its record; nothing built here |
| [R] | research record on `main`, not independently established |
| [W] | derivation in this record; not independently reviewed; not kernel-checked |
| [EC] | exact finite check in `checks/natprep_checks.py` (integer and rational arithmetic; entropies as exact `a + b·log₂3`) |
| [LIT2] | literature cited from memory, not re-read; no result depends on it |

Numbering: results of this record carry an `N` prefix (Lemma N2.1, Theorem N3.1); DL1's results
keep their own numbers (DL1 Theorem 2.2, DL1 Lemma 2.3).

***

## 0. Summary

1. **Node 1 (§1).** An untuned supply is a product law on the non-carrier bits that is invariant
   under lattice translations and the cubic point group, carries no conditioning, and whose positive
   results hold on an open set of single-site laws (U1–U4, from NSC-3 and NSC-5). The family
   `ν_ρ` (each perturbation bit relative to a parity-uniform background β independently 1 with
   probability ρ) is the primary case; ρ = 0 is DL1's pure parity-uniform supply. The designed
   patterns DL1 2.3(f), (i) fail U1 and U2; their random-offset averages fail U2; `ν_ρ` conditioned
   on their environment returns them exactly and fails U3 [EC N1-CC1, N1-CC2]. The delivery task is
   DL1's DT with (R), with the records held at the last refresh time (DT_s); the literal reading,
   with the record held at any later time, admits a 2×2 plaquette whose log equals the ready block
   at every time [EC S2e].
2. **Node 2 (§2) [W, EC].**
   - Lemma N2.1: with a pure parity-uniform supply and single-site carriers, no log disjoint from
     the carriers predicts a carrier with error below `2^{−K}` (K carriers). This settles, for
     such carriers, the open case of DL1 2.3(g).
   - Proposition N2.2: with one carrier, a DT_s delivery (ε = 0) needs at least two environment
     excitation bits.
   - Exhaustive enumeration over lines of 3–6 sites and 2×2, 2×3 boxes: single deliveries occur
     from minimum environment weight 2; double deliveries (N = 2) occur on none of lines of up to 5 sites or the
     2×2 box, and on line 6 and 2×3 from minimum weight 5, the weight of DL1 2.3(i).
   - Under `ν_ρ`, a declared block lies in a delivering configuration with positive probability:
     for the DL1 2.3(f) placement, `π(ρ) ≥ Σ_w c_w ρ^w (1−ρ)^{9−w} · (1−ρ)^{940} ≥ ρ²(1−ρ)^{947}`.
   - Lemma N2.3: in law (no conditioning) the record of a single-site carrier has error at least
     `2^{−K} ν(background on B(L,t) ∖ {j})`, which tends to `2^{−K}` as ρ → 0.
   - So preparation here is the initial law placing delivering configurations. Used in law, the
     delivery is diluted. Used after conditioning on the placement event, the conditional law is
     exactly the designed pattern (Lemma N4.1).
3. **Node 3 (§3) [W, EC].**
   - Theorem N3.1: for finite-support initial data (or on a torus), the partition of
     `cl₂(A_0)` into classes at mutual ℓ1-distance ≥ 3 is invariant, and each class evolves alone
     by a periodic bijection.
   - Corollary N3.2: U₂ never merges, splits or moves a class. The whole history of a block is a
     function of the initial content of its class, so U₂ cannot generate delivery capacity.
   - Theorem N3.3: for arbitrary initial data on ℤ³, including i.i.d. noise, where `cl₂(A_0) = ℤ³`
     almost surely [LIT2], the history of a region R up to T is the isolated evolution of
     `D_T(R)`, the classes of `cl₂(A_0 ∩ B(R,T))` meeting R. `D_T(R)` grows with T only through the
     closure of initial data.
   - The blocking property is (P), `g(0) = g(1)` (equivalently `g(6) = g(5)`), together with the
     second-order form. It fails for every `q ≥ 3`. There `G(2) = 1`, and a single symbol spreads
     without bound [EC T4b].
4. **Node 4 (§4).**
   - The budget is not binding: the designed environment carries `m` bits against the `N+1`
     required by DL1 (2.4).
   - The cost of using a placement is the selection, `log₂(1/π)` bits (PR1 E3). For a pattern `z`,
     `m = log₂(1/ν(z)) + log₂(ν(z)/u(z))` exactly.
5. **Node 5 (§5).** Controls hold; the countercontrols classify the designed patterns as tuned.
6. **Productivity (§6).**
   - Test (ii) is met: Lemma N2.1, Proposition N2.2 and Theorems N3.1, N3.3, with (P) identified as
     the blocking property.
   - Test (i) is not met: positive-probability placement exists, but it is not generated by the
     dynamics and is a delivery in law only after a selection that returns the designed law.
   - Classification: gem, NEW at scope.

***

## 1. Node 1 — the untuned source

**1.1 Definition (fixed before any computation).** Work in perturbation coordinates relative to a
parity-uniform β (DL1 2.1; by DL1 Lemma 2.1 the perturbation dynamics does not depend on which of
the sixteen β is used). Carriers are the measured systems: fair independent bits at declared sites
(DL1 DT; NSC-3 does not constrain where a carrier sits, #1425 c.7023506974 C1 as answered in DL1).
The supply is the law of every other bit. A supply law μ is **untuned** for a delivery at
(H, carriers, w\*) iff:

- **U1 (no reference to the target).** μ is invariant under all lattice translations and the cubic
  point group. Source: NSC-3, "a newly tuned prepared producer state"; a law placing structure
  relative to H or the carriers is specified for the task.
- **U2 (no special distribution).** μ is a product over sites of one single-site law `q` on
  `{0,1}²`. Source: NSC-3, "a special hidden distribution"; NSC-5, an arbitrary candidate law is
  not justified by having been written down. A product law has no structure beyond `q`.
- **U3 (no conditioning).** Statements are about μ itself, not about `μ(·|E)` for an event chosen
  by success. Source: NSC-3 ("postselection", "a herald outside the stated physical model"); DL1
  DT ("no conditioning on success").
- **U4 (no fine-tuned parameter).** A positive result counts only if it holds for an open set of
  single-site laws `q`. Source: NSC-3 ("tuned"); §A.29 (a variant adjustable to fit is rejected).

The budget is stated (NEQ-T with uniform density): for a region R,
`D(μ_R ‖ u_R) = |R| · D(q ‖ u_{{0,1}²})`; for `ν_ρ` (q = Bernoulli(ρ)⊗Bernoulli(ρ)) this is
`2|R|(1 − h₂(ρ))`. `ν_ρ` relative to β equals `ν_{1−ρ}` relative to β⊕1, so ρ ≤ 1/2 loses nothing.
ρ = 0 is DL1's pure parity-uniform supply (deterministic; untuned by U1–U3). ρ = 1/2 is μ₂.

**1.2 What the definition does not decide.** Under U2 with `q` of full support every finite pattern
has positive probability, so the definition admits delivering configurations with positive
probability (§2). Whether a delivery holds in law, and whether the dynamics generates it, is left
to nodes 2 and 3.

**1.3 μ-O and μ-R.** Both are invariant laws, so under them readiness and every fixed-block
statistic are constant in time (PR1 1.3). On a finite torus the class partition and the orbit of
each class's content are constants of the motion (Theorem N3.1), so under μ-O of a state `s₀` the
component geometry is that of `s₀`. Either the orbit is selected (U3; its cost is the PR1 1.5(b)
boundary datum), or `s₀` is drawn from a product law, which is the `ν` case. They are not pursued
separately.

**1.4 The delivery task DT_s.** DL1's DT with clause (R) at ε = 0 for a single-site block H, with
the **retention time equal to the last refresh time**: the records are held at `τ_N`, when H is
ready. Justification: PR1 2.5's per-cycle form counts "N results still held … with the register
re-armed at T", and DL1's examples 2.3(f), (i) hold their records at a refresh time. DL1's text
("At T, each used carrier's bit is ε-predictable", with `τ_N ≤ T`) also admits `T > τ_N`. An
exploratory enumeration under that literal reading preceded this choice. Its finding is recorded
as a countercontrol: on the 2×2 plaquette with one environment excitation diagonal to the carrier,
the literal reading is met (H ready at 0 and 5, record at 7), but the log equals H at every time,
so no record is ever held while H is ready [EC S2e]. Under the literal reading the minimum
environment weight drops from 2 to 1; §2.6 states the effect on the probability.

**1.5 Countercontrol [EC N1-CC1, N1-CC2].** The DL1 2.3(f) pattern as a law has unequal site
marginals (fails U1); its random-offset average on a ring is translation invariant but its adjacent
pair law is not the product of its marginals (fails U2). `ν_ρ` conditioned on the 2.3(f) environment
event is the point mass on that pattern (fails U3; Lemma N4.1).

**Verdict, node 1.** U1–U4 and DT_s are fixed. Designed patterns are classified as tuned.
CONFIRMING relative to NSC-3 and NSC-5.

***

## 2. Node 2 — the positive-probability question

**2.1 Silent branches.** *Lemma N2.1 [W, EC S1a, S1b].* Let the supply be β (ρ = 0), and let
carriers `c_1, …, c_K` sit at single sites `j_k` (on one or both slices), each with `c_k = 0` giving
the background value on its bits. For every block L disjoint from `{j_1, …, j_K}`, every `t ∈ ℤ` and
every estimator `f`, `P(f(W_t(L)) ≠ c_k) ≥ 2^{−K}`.
*Proof.* With every carrier but `c_k` equal to 0, the initial perturbation is supported in `{j_k}`.
A singleton is closed (any other site has at most one neighbour in it), so by DL1 Theorem 2.2 the
perturbation stays in `{j_k}` at every time, and L holds β in both values of `c_k`. That event has
probability `2^{−(K−1)}`, and on it any estimator errs with probability 1/2. ∎
The bound is attained for K ≥ 2 [EC S1b]. Countercontrol: a carrier region `{j, j+2e_1}` with both
bits equal to `c` is not closed, and the site between them depends on `c` [EC S1c]. Scope: carriers
whose region is closed and whose zero value is the background; other carrier forms are open.
DL1 2.3(g) (exhaustive search of small boxes, evidence) is the special case of Lemma N2.1 at ε = 0.

**2.2 One environment excitation is not enough.** *Proposition N2.2 [W, EC S2a].* With one
single-site carrier at `j` and an environment differing from β in exactly one bit, at site `e`,
no DT_s delivery with ε = 0 exists, for any H, w\*, log block or horizon.
*Proof.* If `e = j`, the whole perturbation lies on `{j}` and never leaves it (Lemma N2.1's
argument), so H ≠ j never depends on `c`. If `d(e, j) ≥ 3`, the classes `{e}` and `{j}` are at
distance ≥ 3 in the branch `c = 1` (DL1 Lemma 2.3(c)), so again `c` never reaches H. If
`d(e, j) ∈ {1, 2}`, then in both branches the perturbation stays in the box spanned by `e` and `j`:
a pair, a straight 3-site segment, or a 2×2 square, each closed. Outside it every site holds β at
every time in both branches, so H and the log lie in it. In the pair, the only non-carrier site is
H, which leaves no log block. The 3-site segment and the 2×2 square are covered, in every
orientation by lattice symmetry, by the exhaustive enumeration on line 3 (no delivery at all) and on
2×2 (minimum weight 2) [EC S2a]. ∎

**2.3 Exhaustive enumeration [EC S2a, S2b, S2-full].** All environments on the box, all single-site
carrier positions and modes (current slice, previous slice, both), every H, every w\*, every log
block disjoint from the carriers and H, ε = 0, DT_s with (R). A box is closed in ℤ³ (DL1 Lemma
2.3(a)), so a configuration supported in it evolves exactly as in the box.

| Box | Carriers | N | Delivering configurations | Minimum environment weight |
|---|---|---|---|---|
| line 3 | 1 | 1 | 0 | — |
| line 4 | 1 | 1 | 184 | 2 |
| line 5 | 1 | 1 | 1904 | 2 |
| 2×2 | 1 | 1 | 736 | 2 |
| 2×2 | 2 | 1 | 304 | 2 |
| line 4 | 2 | 1 | 76 | 2 |
| 2×2, line 4, line 5 | 2 | 2 | 0 | — |
| line 6 (`--full`) | 1 | 1 | 19712 | 2 |
| 2×3 (`--full`) | 1 | 1 | 56884 | 2 |
| line 6 (`--full`) | 2 | 2 | 664 | 5 |
| 2×3 (`--full`) | 2 | 2 | 760 | 5 |

Positive controls: DL1 2.3(f) is found as a single delivery (τ = (0, 5), log site 3, w\* = (0,0))
[EC S2c]; DL1 2.3(i) as a double delivery (τ = (0, 4, 16), log site 4 for both carriers,
w\* = (1,1)) [EC S2d]. Its environment has weight 5.

**2.4 Probability under `ν_ρ` [W, EC S3a, S3b].** Fix the 2.3(f) placement: H at a declared site,
the carrier at `H − e_1` (current slice), w\* = background, the segment `{H − e_1, …, H + 3e_1}`.
Of its 512 environments, 20 deliver, by weight `{2: 1, 3: 4, 4: 6, 5: 5, 6: 3, 7: 1}` [EC S3b].
Isolation over the horizon `T = τ₂ = 5`: if every bit in `B(S, T) ∖ S` is background, then, since
`W_t(S)` depends only on `W_0(B(S, t))` (one site per tick), the segment evolves for `t ≤ T` exactly
as in isolation. `|B(S, 5)| = 475` in ℤ³ [EC S3a]. Hence
```text
π(ρ) ≥ Σ_w c_w ρ^w (1−ρ)^{9−w} · (1−ρ)^{940} ≥ ρ² (1−ρ)^{947} > 0   for every ρ ∈ (0, 1),
```
about `7.7·10⁻⁹` at ρ = 1/100 and `3.9·10⁻⁷` at ρ = 1/1000 [EC S3b]. As ρ → 0 the bound is
`ρ²(1 + o(1))`. The isolation factor is crude (it asks for an empty cone), so these are lower
bounds. The same holds for any placement whose delivering environment has finite weight `w`: the
bound is `c ρ^w (1−ρ)^{M}` with `M` fixed by the horizon; for DL1 2.3(i), `w = 5`, `T = 16`,
`|B(S, 16)| = 8742` [EC S3a]. By translation invariance the expected fraction of declared
placements in a box that are in delivering configurations is the same π, so delivering
configurations exist at positive density.

**2.5 Use in law: dilution.** *Lemma N2.3 [W, EC S4].* Let the environment law ν be independent of
the carriers, with K single-site carriers as in Lemma N2.1, L disjoint from the carrier sites, and
`t ≥ 0`. Let `G_k(t)` be the event that every environment bit in `B(L, t) ∖ {j_k}` is background.
Then every estimator of `c_k` from `W_t(L)` errs with probability at least `2^{−K} ν(G_k(t))`; under
`ν_ρ`, `ν(G_k(t)) ≥ (1−ρ)^{2|B(L,t)|}`.
*Proof.* `W_t(L)` depends only on `W_0(B(L, t))`. On `G_k(t)`, with the other carriers 0, that data
is supported in `{j_k}`, which is closed, so `W_t(L)` is β in both values of `c_k`. ∎
On the isolated 2.3(f) segment with `ν_ρ` on its nine environment bits, the exact annealed record
error from the log site at `t = 5` is 0.4964 (ρ = 1/10) and 0.5000 to four places (ρ = 1/100), above
the bound `½(1−ρ)^8`; readiness of H is 0.81 and 0.78 (ρ = 1/10) at `t = 0, 5` [EC S4]. Lemma N2.3
bounds records only. Whether a product law with `ρ|B(L,t)| ≳ 1` can give both reliable records and ε-ready H
in law is not decided here.

**2.6 Assessment.** By Theorems N3.1 and N3.3, what delivers by time T is a function of the
initial content of a closure-determined region. Preparation on U₂ is therefore the initial law
placing a delivering configuration, as the assignment anticipated. Under `ν_ρ` that placement:
- passes U1–U4: it is a typical event of a product law, at rate `π(ρ) ≥ ρ²(1−ρ)^{947}`;
- is not a delivery in law: a fixed apparatus sees records with error near `2^{−K}` at small ρ
  (Lemma N2.3);
- becomes a delivery in law only on conditioning on the placement event, which is excluded by U3
  and NSC-3. The conditional law is exactly the designed pattern (Lemma N4.1), at selection cost
  `log₂(1/π)` bits.

Positive-probability placement plus selection is a relabelling of the designed patterns; without
selection it is a diluted delivery. Under the literal retention reading (§1.4), the plaquette gives
weight 1, so `π ≥ c ρ (1−ρ)^M`. The assessment is unchanged.

**Verdict, node 2.** Positive probability: yes, `π(ρ) ≥ ρ²(1−ρ)^{947}` for the 2.3(f) placement.
Preparation is the initial law's placement. It is a typical event of an untuned law, but usable as a
delivery in law only after a selection that returns the designed law. Lemma N2.1 and Proposition
N2.2 are obstructions [W, EC]; the enumeration is exhaustive within its boxes.

***

## 3. Node 3 — dynamics-generated preparation

For a set A let `Comp(A)` be the classes of `cl₂(A)` under the equivalence generated by
ℓ1-distance ≤ 2.

*Lemma N3.0 [W].* Each class of `Comp(A)` is closed, distinct classes are at ℓ1-distance ≥ 3, and
any union of classes is closed.
*Proof.* A site outside `cl₂(A)` has at most one neighbour in `cl₂(A)`, hence at most one in any
union of classes. A site of `cl₂(A)` outside a class D with two neighbours in D would lie within
distance 1 of D, hence in D's class. Two classes at distance ≤ 2 would be one class. ∎

*Theorem N3.1 (class partition invariant) [W, EC T1].* For U₂ on ℤ³ with `A_0` finite, or on
`(ℤ/n)³`, and β as in DL1 Lemma 2.1:
(a) `Comp(A_t) = Comp(A_0)` for all `t ∈ ℤ`;
(b) for each class D, `W_t|_D = Ψ_D^t(W_0|_D)`, with `Ψ_D` the isolated dynamics of D (perturbation
coordinates), a bijection, periodic when D is finite.
*Proof.* (a) `Comp` depends only on the closure, which is invariant by DL1 Theorem 2.2. (b) Apply
DL1 Lemma 2.3(c) to D and the union of the other classes, closed by Lemma N3.0, with
`A_0 ⊆ cl₂(A_0)`. ∎ [EC T1: six random finite configurations, 24 classes, 30 ticks on n = 14,
invariance and isolated evolution exact.]

*Corollary N3.2 (no assembly) [W].* Under the hypotheses of N3.1, for each value of the carriers:
the class containing H is constant in time; the history of every block in it is a function of
that class's initial content; no class is ever merged, split or moved. Hence a DT_s delivery at H
is an event of the initial content of `D*(H)`, the union over carrier values of the classes meeting
H or the log. A configuration whose classes do not deliver in isolation does not deliver in any
surrounding. Within a class, the dynamics moves the content along a fixed periodic orbit, so
readiness can appear at a later time (DL1 2.3(f), (i)) without new capacity. Every record is
erased by the next multiple of the period (DL1 2.3(c)). [EC T3: in the plaquette `D*(H)` is the
square, with class `{E}` for `c = 0` and the square for `c = 1`.]

*Theorem N3.3 (finite-horizon locality) [W, EC T2].* For any initial data on ℤ³, any finite R and
any T ≥ 0, let `D_T(R)` be the union of the classes of `Comp(A_0 ∩ B(R, T))` meeting R. For
`0 ≤ t ≤ T`, `W_t(R)` equals the isolated evolution of `W_0|_{D_T(R)}` restricted to R, with
`R ∖ D_T(R)` at β. `D_T(R)` is non-decreasing in T.
*Proof.* `W_{t+1}(R)` depends on `W_t(B(R,1))`, so `W_t(R)` depends only on `W_0(B(R, t))`. Replace
the initial perturbation by its restriction to `B(R, T)`; this leaves `W_t(R)` unchanged for
`t ≤ T`, and the restricted perturbation has finite support, so N3.1 applies. Monotonicity: closure
is monotone, and a class of a smaller closure lies in a class of a larger one. ∎
[EC T2: noisy n = 16 torus, ρ = 0.06, eight seeds, T = 0..6. The identity holds, `D_T` grows in some
instance, and after T the isolated evolution can differ from the true one (countercontrol).]

*Remark (infinite volume) [LIT2].* For i.i.d. noise of any density ρ > 0 on ℤ³, 2-neighbour bootstrap
percolation fills the lattice almost surely, so `cl₂(A_0) = ℤ³`. Theorem N3.1 is then empty, and DL1's
hypothesis (I) fails almost surely. Theorem N3.3 still holds, with `D_T(R)` finite for each T. As
T → ∞, `D_T(R)` grows through the closure of initial data alone. Whether the U₂ dynamics carries
readiness or carrier information through such merged regions over long times is open.

**3.4 The blocking property.** U₂ blocks preparation by (P): a site whose previous perturbation is 0
and which has at most one perturbed neighbour stays unperturbed. For β ∈ P the neighbour sum of a
site is 0 or 6, so (P) is `g(0) = g(1)` and `g(6) = g(5)` (equivalent by `g(6−s) = g(s)`), together
with the second-order form, which removes the `x_{t−1}` term. (P) is the step of DL1 Theorem 2.2's
proof; N3.1–N3.3 follow from it. Countercontrol: with `g(1) = 1` a single excitation leaves its site
[EC T4a]. For every `q ≥ 3` the rounded rule has `G(2) = ⌊3/3⌋ = 1`, so one neighbour carrying the
symbol 2 perturbs a vacuum site and (P) fails. A single symbol 2 in the vacuum spreads without
confinement: two-slice support radius 12 (q = 3) and 18 (q = 2^16) at t = 20 [EC T4b].

**Verdict, node 3.** For finite-support or torus laws, dynamics-generated preparation is forbidden
outright on U₂: classes are invariant and autonomous (N3.1, N3.2). For arbitrary laws on ℤ³ it is
forbidden over every finite horizon, beyond what the closure of the initial data within the light
cone already connects (N3.3). The blocking property is (P) with the second-order form. The question
moves to `q ≥ 3`, including the published `q = 2^16`, where (P) fails [EC T4b], and to the long-time
noise interface on U₂.

***

## 4. Node 4 — resource accounting

*Lemma N4.1 [W, EC N1-CC2, A1].* Let ν be a product law and `E_z` the event that the environment on
a finite region R′ equals `z` (m′ bits).
(a) `ν(·|E_z) = δ_z ⊗ ν|_{outside R′}`: conditioning returns the designed law on R′.
(b) `D(ν(·|E_z) ‖ ν) = log₂(1/ν(z))`, PR1 E3.
(c) `m′ = D(δ_z ‖ u_{R′}) = log₂(1/ν(z)) + log₂(ν(z)/u(z))`: the designed budget splits into the
selection cost and the supply's log-likelihood ratio on `z`.
*Proof.* (a) product structure; (b) PR1 E3; (c) `u(z) = 2^{−m′}`. ∎

| Case | Budget required (DL1 (2.4), ε = 0) | Budget of the selected region | Selection cost at ρ = 1/4, segment only [EC A1] |
|---|---|---|---|
| 2.3(f) (N = 1, m = 9, w = 2) | 2 bits | 9 bits | `18 − 7 log₂3 ≈ 6.91` bits (supply term `≈ 2.09`) |
| 2.3(i) (N = 2, m = 10, w = 5) | 3 bits | 10 bits | `20 − 5 log₂3 ≈ 12.08` bits (supply term `≈ −2.08`) |

Including isolation adds `M log₂(1/(1−ρ))` bits of selection. For 2.3(f) at its best ρ
(about `2/949`) the total is about 20.7 bits, matching `π ≈ 6·10⁻⁷`. In the unconditioned law
`ν_ρ`, the cone budget `2|B|(1−h₂(ρ))` exceeds (N+1) by orders of magnitude, so the budget is not
the binding constraint (DL1 node 1: the budget does not discriminate). The binding cost of using an
untuned placement as a delivery is the selection, `log₂(1/π) ≈ w log₂(1/ρ)` as ρ → 0.

**Verdict, node 4.** Accounted: no positive case meets DT_s in law without selection, and the
selected case costs `log₂(1/π)` bits beyond the untuned law.

***

## 5. Node 5 — controls

| Control | Check | Verdict |
|---|---|---|
| S⇔D⇔Q_fb, `finite_horizon_equivalence` [K, as cited in PR1] | Quantifies over supplied finite-horizon laws; nothing here restricts which laws are representable. | untouched |
| DL1 [R] | Theorem 2.2 and Lemma 2.3 are used as stated. 2.3(f) and (i) are reproduced as DT_s deliveries [EC S2c, S2d]. Lemma N2.1 extends 2.3(g) from evidence to proof for its carrier class. N3.1 drops hypothesis (I) for finite support. N3.3 replaces it over finite horizons. DT's retention clause admits the plaquette under the literal reading (S2e); DL1's conclusions use examples that meet DT_s. | consistent; one definitional gap noted (AW-NP1-1) |
| PR1 [R] | E3 is used for the selection cost, and 2.5 enters through DL1 (2.4). | consistent |
| P8 bound (#1400) [R] | Not used. | untouched |
| #1408 fixed-site obstruction, #1412 obstruction [R] | Product-law statements at ρ = 1/2. `ν_{1/2}` is μ₂. Nothing here concerns their fixed-site or moving-frame claims. | preserved at their scope |
| Source screens (DL1 §1 rows) [R] | Their `q = 2^16` cases lie outside (P) [EC T4b]. No screen is promoted or weakened. | each true at its scope |
| Countercontrol (designed pattern tuned) | N1-CC1, N1-CC2 | passes |

***

## 6. Productivity verdict and classification

**Test (i)** is not met. The untuned law `ν_ρ` places delivering configurations with positive
probability (§2.4), but U₂ does not generate them (N3.1–N3.3). In law they are diluted (Lemma
N2.3), and conditioning on them returns the designed pattern (Lemma N4.1), which U3 and NSC-3
exclude.

**Test (ii)** is met, at scope U₂, `q = 2`, parity-uniform backgrounds:
- Lemma N2.1 proves, for single-site carriers, the pure-supply obstruction DL1 left as evidence.
- Proposition N2.2 gives the two-excitation threshold.
- Theorem N3.1 removes DL1's hypothesis (I) for finite-support laws, with Corollary N3.2: U₂
  cannot generate delivery capacity.
- Theorem N3.3 gives the finite-horizon form for arbitrary laws on ℤ³, where (I) fails almost surely.
- (P) with the second-order form is the blocking property.

Verdict: gem.

**Pressure test.**
1. N3.1 and N3.2 follow from DL1 Theorem 2.2 and Lemma 2.3(c) in a few lines. Their content is that
   no extra hypothesis is needed. N3.3 is a light-cone argument.
2. The probability statement is favourable to a positive answer, so it was pressed: the placement
   holds at positive rate, but the use in law fails (N2.3), and the conditioned law equals the
   designed one exactly (N4.1).
3. The retention-time choice in DT_s makes delivery harder. Under the literal reading the
   minimum weight is 1, not 2, and the assessment is unchanged (§2.6).
4. Scope: q = 2 only. For `q ≥ 3`, (P) fails and the question is open. The long-time noise
   interface on U₂ is open, and so are carriers whose region is not closed.

| Item | Class |
|---|---|
| Node 1: U1–U4; DT_s; N1-CC1, N1-CC2 | CONFIRMING (NSC-3, NSC-5) |
| Retention-time gap in DT (S2e) | NEW (definitional) |
| Lemma N2.1; Proposition N2.2 | NEW at scope |
| Enumeration §2.3; probability §2.4 | ELABORATING |
| Lemma N2.3; Lemma N4.1 | ELABORATING (PR1 E3) |
| Theorem N3.1; Corollary N3.2 | ELABORATING (DL1 2.2, 2.3(c)) |
| Theorem N3.3 with the infinite-volume remark; (P) identified | NEW at scope |

- **AW-NP1-1 (retention time).** A delivery task that does not tie the record time to a refresh
  time admits logs that mirror the ready block. A DT used elsewhere should hold its records at a
  time when the block is ready.
- **AW-NP1-2 (placement and selection).** On an update with an invariant class structure, a
  positive-probability delivering configuration under an untuned law is a placement. Its use as a
  delivery in law needs a selection whose conditional law is the designed one (N4.1). A claim of
  native preparation on such an update should state which of the two it uses.
- **AW-NP1-3 (infinite volume).** DL1's hypothesis (I) fails almost surely for i.i.d. supplies on
  ℤ³ [LIT2]. Statements resting on (I) hold there only over finite horizons, through `D_T(R)`.
- **Fixed point.** One pass, with NEW items; the §A.31 fixed point is not reached.

***

## 7. What this decides for #866 and #1169

For U₂ (`q = 2`): native dynamics cannot prepare delivering components (Corollary N3.2, Theorem
N3.3). An untuned product supply places them with positive probability, of order `ρ²` for a single
delivery and `ρ⁵` for the double delivery found. Placement is a delivery in law only after a selection costing
`log₂(1/π)` bits, which returns the designed pattern. A measurement source on U₂ therefore rests on
the initial law or on a selection, not on the dynamics. The blocking property (P) fails for every
`q ≥ 3`. The question of native preparation moves to those rules, including the published
`q = 2^16`, and to the long-time noise interface on U₂. Physical measurement sourcing remains
"NOT PASSED", and A1 remains "OPEN/UNADOPTED", as recorded by the owner.

***

## 8. Limits; what an independent reviewer must check; literature

- U1–U4 and their derivation from NSC-3 and NSC-5. Check that they do not decide the answer:
  every finite pattern has positive probability under U2.
- DT_s's retention time, and the S2e countercontrol (the plaquette's log equals H at every time).
- Lemma N2.1: the closedness of a singleton and the branch argument; the scope (closed carrier
  regions, background zero value).
- Proposition N2.2: the case split on `d(e, j)`; that the closure of `{e, j}` is the spanned box;
  that line 3 and 2×2 cover the cases.
- Lemma N3.0 and Theorem N3.1(b): that the union of the other classes is closed and at distance ≥ 3.
- Theorem N3.3: the light-cone step `W_t(R) ← W_0(B(R, t))`, and the monotonicity of `D_T`.
- Lemma N2.3: the event `G_k(t)` and the truncation argument.
- Lemma N4.1 and the accounting table.
- That each check tests what is claimed (§9). T1 and T2 are exact checks on seeded random
  instances; the general statements rest on the proofs. The `--full` enumerations take about
  17 minutes.
- Not done: no literature re-read; no study of `q ≥ 3` beyond T4b; no long-time study of the noise
  interface; no Lean.

[LIT2] A. C. D. van Enter, J. Stat. Phys. 48 (1987) 943, and R. H. Schonmann, Ann. Probab. 20
(1992) 174, on bootstrap percolation on ℤ^d (critical density 0 for threshold ≤ d); J. Chalupa,
P. L. Leath and G. R. Reich, J. Phys. C 12 (1979) L31. No result here depends on them.

***

## 9. Exact checks

`checks/natprep_checks.py`. Command, from this directory: `python3 -I checks/natprep_checks.py`
(about 20 seconds); `--full` adds the larger enumerations (about 17 minutes). Exit status 0 iff every
check holds.

| Check | Statement tested |
|---|---|
| N1-CC1, N1-CC2 | countercontrols: designed (f) pattern fails U1/U2; conditioning `ν_ρ` returns it (U3, N4.1(a)) |
| S1a | single-site perturbations never leave their site, along whole orbits, on nine boxes |
| S1b | Lemma N2.1: error ≥ 2^{−K} for K = 1..3 on ten box/carrier-count cases; attained for K ≥ 2 |
| S1c | countercontrol: a non-closed carrier region leaks |
| S2a, S2b | exhaustive DT_s enumeration (§2.3 table, default rows); Proposition N2.2's finite part |
| S2c, S2d | positive controls: DL1 2.3(f) and 2.3(i) |
| S2e | countercontrol for the retention time: the plaquette |
| S3a, S3b | ball sizes; delivering environments of the (f) placement by weight; π lower bounds |
| S4 | Lemma N2.3 on the isolated (f) segment; annealed readiness and record error |
| T1 | Theorem N3.1 on random finite configurations |
| T2 | Theorem N3.3 on noisy tori; countercontrol after the horizon |
| T3 | plaquette classes per carrier value |
| T4a, T4b | the blocking property (P); its mutation; q = 3 and q = 2^16 spreading |
| A1 | Lemma N4.1(c) identity and (2.4) slack |
| S2-full | (`--full`) §2.3 table, rows marked `--full` |

Output of `python3 -I checks/natprep_checks.py --full` at this record's commit (exit status 0; the
default run prints the first 20 lines and `19/19 checks hold`, exit status 0):

```text
CHECK N1-CC1 countercontrol: the designed (f) pattern has unequal site marginals (fails U1); its random-offset average is translation invariant but not a product law (fails U2): PASS
CHECK N1-CC2 countercontrol: nu_rho conditioned on the (f) environment event is the point mass on the designed pattern (fails U3; it is the designed law): PASS
CHECK S1a every single-site perturbation stays on its site along its whole orbit, on lines 3..7 and boxes 2x2, 2x3, 3x3, 2x2x2 (a singleton is closed; DL1 Theorem 2.2): PASS
CHECK S1b pure parity-uniform supply with K = 1..3 single-site carriers (lines 4..6, 2x3, 2x2x2): a log disjoint from the carriers never predicts c_k with error < 2^-K (Lemma N2.1); the bound is attained for K >= 2: PASS
CHECK S1c countercontrol: a carrier region {j, j+2} with both bits equal to c is not closed, and the site between them depends on c: PASS
   S2 summary: 3 k=1 N=1: 0 found, min weight None; 4 k=1 N=1: 184 found, min weight 2; 5 k=1 N=1: 1904 found, min weight 2; 2x2 k=1 N=1: 736 found, min weight 2; 2x2 k=2 N=1: 304 found, min weight 2; 4 k=2 N=1: 76 found, min weight 2; 2x2 k=2 N=2: 0 found, min weight None; 4 k=2 N=2: 0 found, min weight None; 5 k=2 N=2: 0 found, min weight None
CHECK S2a strict DT+(R) enumeration (eps = 0, all environments, all single-site carrier positions and modes, all H): single deliveries exist on lines 4, 5 and 2x2 with 1-2 carriers, none with fewer than 2 environment excitations; none on line 3: PASS
CHECK S2b no double delivery (N = 2) on 2x2, line 4 or line 5 with two carriers: PASS
CHECK S2c positive control: DELIVER-1 2.3(f) is a strict single delivery: {'carrier': 0, 'taus': (0, 5), 'T': 5, 'log': (3,), 'w': (0, 0), 'P': 12}: PASS
CHECK S2d positive control: DELIVER-1 2.3(i) is a strict double delivery: {'carriers': (0, 1), 'taus': (0, 4, 16), 'T': 16, 'logs': ((4,), (4,)), 'w': (1, 1), 'P': 60}: PASS
CHECK S2e countercontrol for the retention time: plaquette delivers in the literal reading ({'carrier': 0, 'taus': (0, 5), 'T': 7, 'log': (2,), 'w': (0, 0), 'P': 6}) and not in the strict one; its log mirrors H at every time: PASS
CHECK S3a |B(segment, T)| in Z^3: 475 for (f) (5 sites, T = 5), 8742 for (i) (6 sites, T = 16): PASS
CHECK S3b (f) placement: delivering environments by weight {2: 1, 3: 4, 4: 6, 5: 5, 6: 3, 7: 1}; pi(rho) >= sum_z rho^w (1-rho)^(9-w) * (1-rho)^940 > 0; at rho = 1/10, 1/100, 1/1000: 7.099e-46, 7.656e-09, 3.893e-07: PASS
CHECK S4 dilution on the isolated (f) segment: rho=1/10: P(H ready at 0)=0.8100, at 5=0.7795, record error=0.4964 >= 0.2152; rho=1/100: P(H ready at 0)=0.9801, at 5=0.9753, record error=0.5000 >= 0.4614: PASS
CHECK T1 component partition of cl2(A_0) is invariant and each class evolves alone (6 random finite configurations, 24 classes, n = 14, 30 ticks); classes are closed and pairwise at l1-distance >= 3 (Theorem N3.1): PASS
CHECK T2 finite-horizon locality (noisy n = 16 torus, rho = 0.06, 8 seeds, T = 0..6): the history of the origin up to T equals the isolated evolution of D_T; D_T is non-decreasing and grows in some instance; after T the isolated evolution can differ (countercontrol): PASS
CHECK T3 plaquette: with c = 0 the only class is {E}; with c = 1 it is the 2x2 square containing H and the log (D*(H) is the square): PASS
CHECK T4a blocking property (P): g(0) = g(1) = 0 and g(5) = g(6) = 0; mutation g(1) = 1 lets a single excitation leave its site (countercontrol): PASS
CHECK T4b q = 3 and q = 2^16: G(2) = 1, and the two-slice support of a single symbol 2 in the vacuum reaches l1-radius 12 (q = 3) and 18 (q = 2^16) at t = 20 (n = 45 torus; radii by tick {3: [1, 2, 3, 3, 3, 4, 5, 6, 6, 6, 7, 8, 9, 9, 9, 10, 11, 12, 12, 12], 65536: [1, 2, 3, 3, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]}); no confinement: PASS
CHECK A1 accounting identity m = log2(1/nu(z)) + log2(nu(z)/u(z)) and (2.4) slack: (f): m=9, selection cost 18 + -7*log2(3), supply term -9 + 7*log2(3), (2.4) needs 2; (i): m=10, selection cost 20 + -5*log2(3), supply term -10 + 5*log2(3), (2.4) needs 3: PASS
CHECK S2-full 6 k=1 N=1: 19712 found, min weight 2: PASS
CHECK S2-full 2x3 k=1 N=1: 56884 found, min weight 2: PASS
CHECK S2-full 6 k=2 N=2: 664 found, min weight 5: PASS
CHECK S2-full 2x3 k=2 N=2: 760 found, min weight 5: PASS
23/23 checks hold
```
