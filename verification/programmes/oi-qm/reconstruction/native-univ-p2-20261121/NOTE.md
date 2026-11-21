# NATIVE-UNIV, phase 2: the bounded-breach question, P3 stage S1, and the P1-Q2 design

**Standing.** Writer's research record. Paper only. Independent non-author review at `d2ddb3cb`:
REVISE ([#1499 c.7064953331](https://github.com/amaybaum/incompleteness/pull/1499#issuecomment-7064953331)),
mathematics confirmed apart from NU8's tick count. Its items R1, R2 and n1–n4 are answered in an
appended commit, not yet re-reviewed. It follows
`PLAN.md`, which was committed (`960977eb`) before this file. No computation was run. No
manuscript, Lean or registry edit and no premise adoption. Authorization, scope and the
productivity test are in `PLAN.md`.

- **Base.** Stacked on `2572854b`, the reviewed head of #1489. `F1` is that record,
  `verification/programmes/oi-qm/reconstruction/native-univ-feasibility-20261121/`, which is
  unchanged here; `F1 §n` is its `NOTE.md`.
- **Predecessors.** MQ is MEAS-Q `RESULT.md` §2 (MQ1, MQ2, closed sets, `cl₂`, the boundary layer
  `∂D`); U1 is UNIV-1; U2 is UNIV-2.
- **Object.** Q = `R_{2^16}` on `ℤ³`, the working reference implementation
  ([#1169 c.7064226074](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7064226074)
  item 3.2), at a uniform background `c`.
- **Window.** Results for Q at general `c` are stated on representatives, as in MQ. Where RZ
  (`y = x − c`) is used, it is used inside U1 Lemma 2.1's window.

| Label | Meaning |
|---|---|
| [W] | derivation in this record; not independently reviewed; not kernel-checked |
| [W-rev] | derivation in F1, confirmed by #1489's non-author reviews |
| [R] | research record on `main`, at its stated standing |
| [LIT-R] | literature whose cited passage was read in the source (F1 §2) |

**Dependencies, stated and not assumed.**
- MQ1 and MQ2 [R].
- F1's NU1 and NU2 [W-rev].
- U1 Lemma 2.1 [R].
- Morita–Ueno 1992 [LIT-R], including its universality claim at the standing of that paper's
  construction.

Nothing here assumes PM-D5 (#1454), which stays paused, or any other unresolved prerequisite.

***

## 0. Summary

1. **The bounded-breach question (F1 §4) dissolves into a confinement question [W].**
   - *Theorem NU4.* For any closed region `D` (finite or infinite) whose complement is at `c`:
     a boundary-layer value of `D` outside `[c−1, c+1]` at tick `t` puts a non-background value
     outside `D` at tick `t + 1`. Conversely, MQ1 keeps the complement at `c` while every boundary
     value is in range. So, relative to any closed region, a breach is radiation one tick later.
     "A bounded breach that heals without radiation" relative to the region in which the
     disturbance is allowed does not exist.
   - *Proposition NU3.* For finite configurations: periodic ⇔ bounded support ⇔ confined, at every
     tick, in one finite closed set with in-range boundary. Every excursion of a periodic orbit
     lies inside its own permanently confined closed hull.
   - *Consequence: the decisive question for Q, restated.* Does Q admit a controlled transfer
     whose whole transit is confined in one closed region `D = cl₂(lines ∪ R)`, with `R` finite?
     That means `∂D` in range at every tick; values outside `[c−1, c+1]` are allowed only at
     interior sites of `D`.
   - *Corollary NU6.* If `D` lies in one lattice plane, every site of `D` is a boundary site.
     A planar radiation-free transit is then ternary at every tick.
   - This corrects F1 §4's framing: F1 listed a healing breach as a possibility distinct from
     confinement, which it is not.
2. **P3, stage S1: open [W].**
   - *Proved, Lemma NU7.* The light-cone tip of a single-site seed dies within
     `⌈log₃|b|⌉ + 1` ticks, so no proof of S1 can run through a front moving at light speed along
     an axis.
   - *Proved by NU3.* S1 is equivalent to the statement that no single-site seed with an excursion
     is confined forever in a finite closed set.
   - *Stopped at* a sub-luminal growth mechanism. Stage S2 is not started (P3's stage order).
     F1's P2 (k = 1 shapes) is the preregistered computation that would test S1. It stays gated.
3. **P1-Q2: a proposed comparison construction, on paper only [W]. Not a construction under the native rule (§3, Classification).**
   - *Theorem NU8.* For every 16-state 2-D reversible partitioned CA `P` (Morita–Ueno Def. 2.1)
     there is a narrow-class rule `R_P`. Its update is `x(t+1) = F(x(t)) − x(t−1) mod 8995` on `ℤ²`,
     and `F` reads only the four nearest neighbours: no self-term, translation-commuting.
   - `R_P` comes with an injective encoding `E` such that six ticks of `R_P` act on `E(c)`
     exactly as one step of `P` acts on `c`. Each tick updates one sublattice.
   - Applied to Morita–Ueno Model 1, it gives a narrow-class comparison rule that is universal at
     the standing of Morita–Ueno's construction. The design embeds in `ℤ³`.
   - *What the comparison rule is not.* It is neither isotropic nor totalistic, and it needs a
     designed periodic background of role tags and clocks. It is a comparison model only and does
     not bear on `R_q`.
4. **Productivity (PLAN test).** Met by (iii), whose wording, fixed in PLAN, is "a complete paper design": NU8. That is a productivity criterion only. Under the owner's construction standard (§3, Classification) NU8 is not a completed construction. Not counted toward (i): NU4 and NU5 correct
   F1 §4's framing, but they apply MQ1's converse at a closed set's boundary and are ELABORATING
   (§5). They do not settle Q, because the region `D` is still free and excursions inside a
   never-breached `D` remain possible. Not met by (ii): S1 is open.
5. **(N)/(I) and Established / Assumed / Missing** for each result: §4a.

***

## 1. Question B: bounded breach, healing and radiation in Q

Conventions. `c` is a uniform background, which is a fixed point at `d = 3` (F1 NU2). A set `D` is
*closed* when every site outside `D` has at most one neighbour in `D` (MQ, DL1 §2.2). `∂D` is the
set of sites of `D` with a neighbour outside `D`. A *breach of `D` at `t`* is a site `j ∈ ∂D` with
`x_t(j) ∉ [c−1, c+1]` (current slice, as in MQ2's hypothesis).

**Theorem NU4 (breach of a closed region is radiation) [W].** Let `D ⊂ ℤ³` be closed, finite or
infinite, and suppose `x_{t−1}(p) = x_t(p) = c` for every `p ∉ D`. Then
`x_{t+1}(p) = c` for every `p ∉ D` if and only if `D` has no breach at `t`.

*Proof.*
- (⇐) This is MQ1.
- (⇒) Let `j ∈ ∂D` with `x_t(j) ∉ [c−1, c+1]`, and let `p ∉ D` be a neighbour of `j`.
  - Since `D` is closed, `j` is the only neighbour of `p` in `D`.
  - Every other neighbour of `p` is outside `D`, so it holds `c` at `t`, and `x_{t−1}(p) = c`.
  - By MQ1's converse, `x_{t+1}(p) ≠ c`. ∎

*Corollary NU4′ (windows).* Suppose `x_{t₀−1}` and `x_{t₀}` equal `c` off the closed set `D`. Then
the support stays in `D` at every tick of `[t₀ − 1, t₁ + 1]` if and only if `D` has no breach at any
`t ∈ [t₀, t₁]`. (⇐) is MQ2(a). (⇒) is NU4, applied at the first breach tick.

**Proposition NU3 (finite configurations) [W].** For a finite perturbation of `(c, c)` under Q, the
following are equivalent:
- (a) the orbit is periodic;
- (b) the support over `t ≥ 0` is bounded;
- (c) there is a finite closed `D` with no breach at any `t ∈ ℤ` and with `x_t = c` off `D` for all
  `t`.

*Proof.*
- (a ⇒ c). Let `B` be the union of the supports of all slices over one period. It is finite and
  equals the union over all `t`. Put `D = cl₂(B)`, which is finite and closed.
  - Let `j ∈ ∂D` and let `p ∉ D` be a neighbour of `j`. Then `p ∉ B`, so `x_s(p) = c` for every
    `s`.
  - Since `D` is closed, `j` is `p`'s only neighbour in `D`, and `p`'s other neighbours hold `c`.
  - MQ1's converse, from `x_{t−1}(p) = x_{t+1}(p) = c`, gives `x_t(j) ∈ [c−1, c+1]` for every `t`.
- (c ⇒ b). Immediate.
- (b ⇒ a). This is F1 NU2. ∎

*Reading.* An *excursion* (F1 `plans/P2-PREREG.md` §1) is a breach of the instantaneous hull
`D_t = cl₂(supp x_{t−1} ∪ supp x_t)`. By NU3, an excursion in a periodic orbit is a breach of a
smaller set inside the hull `D`, and `D` itself is never breached. By NU4, an excursion at `t` puts
non-background values outside `D_t` at `t + 1`, and those values stay inside `D`.

**Theorem NU5 (no healing relative to the allowed region) [W].** Fix a closed region `D`, for
example `D = cl₂(L ∪ R)` with `L` a set of axis lines and `R` a finite junction set. Fix a transit
window. Suppose the initial slices equal `c` off `D`.
- (a) The transit is radiation-free relative to `D` (support in `D` at every tick) if and only if
  `D` is never breached in the window (NU4′).
- (b) A breach of `∂D` at `t` is radiation outside `D` at `t + 1` (NU4). So no orbit has a breach
  of `D` that "heals without radiation" relative to `D`.

What remains possible:
- (i) Excursions relative to smaller sets inside a never-breached `D`. These are transients of
  MQ2's confined dynamics on `D`, during which the interior values of `D` are unrestricted.
- (ii) Radiation outside `D` that later returns. This is confinement relative to a larger region,
  and U2's R3 counts it as a failure.

*The decisive question for Q, restated.* Is there a closed `D = cl₂(L ∪ R)`, with `R` finite, and
an initial pattern such that a W-type signal enters along one line and leaves along another? The
transit must be confined in `D` throughout, with no breach of `∂D` at any tick, and the line
sector must be restored. By NU5 this subsumes F1 §4's "bounded breach" alternative. The breach
mechanism of U2 D1 (AW-UNIV-3) is exactly a breach of `∂D` for `D` the junction's closed set.

**Corollary NU6 (necessary conditions on a confined transit) [W].** In a transit confined in `D`:
- (a) every `j ∈ ∂D` has `x_t(j) ∈ [c−1, c+1]` at every tick. For `j ∈ ∂D`, `G(S_t(j)) − y_{t−1}(j)`
  must lie in `{−1, 0, 1}` (RZ, inside the window), so `|S_t(j)| ≤ 7`.
- (b) values outside `[c−1, c+1]` occur only at interior sites `Int D = {j ∈ D : N(j) ⊂ D}`;
- (c) *planar regions:* if `D` lies in a plane `z = z₀`, then `cl₂` keeps it there, since an
  off-plane site has only one neighbour in the plane. Every site of `D` has its `±z` neighbours
  outside `D`, so `∂D = D` and the transit is ternary (`|y| ≤ 1`) at every site and tick.
  A planar radiation-free turn is therefore a problem in the ternary sector of RZ on a planar set:
  - in-plane sums satisfy `|S| ≤ 4`, so `G(S) ∈ {−1, 0, 1}`;
  - the constraint is that `G(S) − y_{t−1}` never reaches `±2`.

*Proof.* (a) is NU5(a) with RZ; (b) restates (a); (c) is as given. ∎

**Skepticism (§A.31).** The results above are restrictive, not favourable. The favourable reading,
"healing breaches are now irrelevant, so a turn is easier to find", does not follow: NU5 removes an
alternative, and the confined-transfer question is at least as hard. Three checks:
- *The proofs use MQ1's converse.* MQ1's converse holds only when the outside site has one
  non-background neighbour. Closedness of `D` supplies exactly that.
- *NU4 does not need `D` finite.* So it covers configurations with infinite lines.
- *P3-K1 countercontrol.* For `F ≡ 2c` (no neighbour coupling) NU4's (⇒) fails: an out-of-range
  boundary value kicks nothing. NU4, and with it NU3 and NU5, therefore use the property
  "`G(s) = 0` iff `|s| ≤ 1`" of the rounded rule.

***

## 2. P3, stage S1 (single-site seeds at `c = 2^15`)

Statement (F1 `plans/P3-PREREG.md`): a seed `(a, b)` at the origin, with `max(|a|, |b|) ≥ 2` in RZ,
has unbounded support over `t ≥ 0`.

**Reformulation [W, by NU3].** S1 holds if and only if no such seed has an orbit confined in a
finite closed set at every tick. Every such seed has an excursion at `t = 0` or `t = 1`:
- if `|b| ≥ 2`, the hull `{0}` is breached at `t = 0`;
- if `|b| ≤ 1` and `|a| ≥ 2`, then `y_1(0) = −a` breaches `{0}` at `t = 1`.

**Lemma NU7 (the axis tips of the light cone die) [W].** For a seed at the origin, `y_t(i) = 0`
whenever `|i|₁ > t` (light cone, by induction). On an axis tip `i = t e_k`, the only neighbour
inside the cone at `t − 1` is `(t−1) e_k`, and the subtracted term `y_{t−2}(t e_k)` is 0 (as is
`y_{t−1}(t e_k)`). So `u_t := y_t(t e_k)` satisfies `u_t = G(u_{t−1})` with `u_0 = b`.
- If `|u| ≤ 3^m` then `|G(u)| ≤ 3^{m−1}`, and `G(u) = 0` for `|u| ≤ 1`. So for `|b| ≥ 2`,
  `u_t = 0` for `t ≥ ⌈log₃ |b|⌉ + 1`. For `|b| ≤ 1` the tip is 0 from `t = 1`.
- The recursion is exact on representatives and needs no window bound. The bound `|u_t| ≤ |b|`
  holds for the tip values only: off the axis values can exceed `|b|`, and `y_1(0) = −a` already
  does when `|a| > |b|`. ∎

*Consequence.* The support does not grow at speed 1 along the axes beyond a finite time. A proof
of S1 that follows the outermost front at light speed fails at the axis tips. The rest of the
light-cone surface is not shown to die, so a proof following an off-axis light-speed front is not
excluded.

**Where the attempt stopped.**
- *What a proof needs.* A sub-luminal growth mechanism: a quantity forcing the support's radius to
  infinity at some speed below 1.
- *Candidates tried on paper.* The light-cone surface recursion. On the surface,
  `y_t(i) = G(Σ_{inner neighbours} y_{t−1})`, with at most three inner neighbours. Its maximum is
  non-increasing (`G(3M) = M`), which gives no growth.
- *No conserved or monotone quantity.* None is known for Q (U2 A2 excludes one template).
- *Verdict.* S1 is open. Under P3's stage order, S2 is not started.
- *The decisive computation* is F1's preregistered P2 restricted to `k = 1`. Its `P` certificates
  would refute S1 for the seeds they cover; its `G` class would be evidence only. It stays gated.
  No new preregistration is needed.

***

## 3. P1-Q2: a narrow-class rule simulating any 16-state 2RPCA(4)

**Target.** Morita–Ueno Def. 2.1 (p. 142): `P = (ℤ², U, R, D, L, f_P)` with
`U = R = D = L = {0, 1}` and `f_P : D × L × U × R → U × R × D × L` a bijection, and
`F_P(c)(i, j) = f_P(DOWN(c(i, j+1)), LEFT(c(i+1, j)), UP(c(i, j−1)), RIGHT(c(i−1, j)))`.
Model 1 is one such `P` (p. 144), stated universal by the realization of a Fredkin gate [LIT-R].

**Alphabet.** `q = 8995 = 5 · 7 · 257`. By the Chinese remainder theorem,
`ℤ/8995 ≅ ℤ/5 × ℤ/7 × ℤ/257`, and subtraction acts componentwise with no carries. Each value is a
triple `(τ, κ, δ)`:
- the tag `τ ∈ ℤ/5`: 0 inactive, 1 cell, 2 plaquette, 3 horizontal edge, 4 vertical edge;
- the clock `κ ∈ ℤ/7`: phase indices `0,…,5`;
- the data `δ ∈ ℤ/257`.

**Geometry (one component of NU1).** On `ℤ²` let the even sublattice `A` hold cells at `(2u, 2v)`
and plaquettes at `(2u+1, 2v+1)`. Let the odd sublattice `B` hold horizontal edges `(2u+1, 2v)`
and vertical edges `(2u, 2v+1)`. Roles are read from the neighbours' tags, by position
`(N, E, S, W)`:

| Role | E/W neighbours | N/S neighbours |
|---|---|---|
| cell | horizontal edges | vertical edges |
| plaquette | vertical edges | horizontal edges |
| horizontal edge | cells | plaquettes |
| vertical edge | plaquettes | cells |

The four patterns are distinct, so `F`, which reads only the ordered neighbour tuple, knows the
role of the site it updates.

**Encoding `E(c)`.** The tags are as above; every A site has `κ = 4` and every B site `κ = 5`; cells
and plaquettes have `δ = 0`.
- A horizontal edge between cells `(u, v)` [W] and `(u+1, v)` [E] has
  `δ = −enc₂(RIGHT(c(u,v)), LEFT(c(u+1,v)))`.
- A vertical edge between `(u, v)` [S] and `(u, v+1)` [N] has
  `δ = −enc₂(UP(c(u,v)), DOWN(c(u,v+1)))`.
- Here `enc_k` is the binary encoding of `k` bits into `{0,…,2^k − 1} ⊂ ℤ/257`.

Every part of `c` sits on exactly one edge, so `E` is injective. The other component of the
second-order rule is held at 0.

**Update.** Half-step `h` updates `A` for even `h` and `B` for odd `h`, with phase `k = h mod 6`.
An updated site reads its neighbours' clocks (all equal to `k − 1`) and knows its own (`k − 2`). It
sets each field by `y′ = F − y`, with:
- `F_τ = 2τ`, so the tag is kept;
- `F_κ = k + (k − 2 mod 6)` in `ℤ/7`, so the clock becomes `k`;
- `F_δ` as in the table, in `ℤ/257`.

Sites with all-zero neighbour tags, and tuples outside the image of the encoding, get `F = 0`.
That choice is arbitrary: reversibility holds for every `F` (second-order form). The table lists
each phase's data invariant before the step, with `X = enc₄` of `f_P`'s input tuple at the cell and
`Y = enc₄(F_P(c)(cell))`.

| `k` | Sites | Data before | `F_δ` read from neighbours | Data after |
|---|---|---|---|---|
| 0 | cells | `0` | `X`, read from the four edges' (negated) parts: D from N, L from E, U from S, R from W | `X` |
| 0 | plaquettes | `0` | `0` | `0` |
| 1 | edges | `−e` (`e` = the edge's two parts) | `enc₈(X_W, X_E) − e`; for a vertical edge, `(X_S, X_N)`. Here `e` is read from the two cells: RIGHT of W is a component of `X_E`, LEFT of E is a component of `X_W` | `enc₈(X_W, X_E)` |
| 2 | cells | `X` | `X + Y`: `X` from any edge's copy, `Y = enc₄(f_P(X))` | `Y` |
| 2 | plaquettes | `0` | `0` | `0` |
| 3 | edges | `enc₈(X_W, X_E)` (vertical: `enc₈(X_S, X_N)`) | horizontal: `enc₈(X_W, X_E) + enc₂(RIGHT(Y_W), LEFT(Y_E))`; vertical: `enc₈(X_S, X_N) + enc₂(UP(Y_S), DOWN(Y_N))`; `X = f_P^{−1}(Y)`, read from the cells | `e′` (the new parts) |
| 4 | cells | `Y` | `Y`, read from the four edges' new parts: UP on N, RIGHT on E, DOWN on S, LEFT on W | `0` |
| 4 | plaquettes | `0` | `0` | `0` |
| 5 | edges | `e′` | `0` (cells and plaquettes hold 0) | `−e′` |

**Theorem NU8 [W].** For every 16-state `2RPCA(4)` `P`, the rule `R_P` above has these properties:
- *Class.* It lies in the narrow class: `x(t+1) = F(x(t)) − x(t−1) mod 8995` on `ℤ²`, with `F`
  reading only the four nearest neighbours, no self-term and one `F` at every site.
- *Simulation.* Let `Ψ` be one tick of the second-order rule. By NU1(b), one tick is one
  half-step of the staggered component, which updates one sublattice. Then
  `Ψ⁶ ∘ E = E ∘ F_P`: six ticks per PCA step.

*Proof.* Induction over the six phases, using the table's invariants.
- *Phase 0.* Each cell's four incoming parts are on its four edges, negated, so the cell obtains
  `f_P`'s argument `X`.
- *Phase 1.* Each edge's own value `−e` is recoverable from the adjacent cells' `X`, so `F − y`
  replaces it by `enc₈` of both cells' `X`. Eight bits is at most 255 < 257.
- *Phase 2.* The cell reads `X` from an edge copy and gets `F − X = Y = enc₄(F_P(c))`.
- *Phase 3.* Each edge recovers its copy from `Y` by `f_P^{−1}`, which exists because `f_P` is a
  bijection, and replaces it by the new parts.
- *Phase 4.* The cell reads `Y` back from its four edges and is cleared.
- *Phase 5.* The edges negate.
- *Bookkeeping.* Tags are fixed and clocks return to `(4, 5)`, so the state is `E(F_P(c))`. The
  components do not interact (NU1), and the other component stays at 0 because `F(0,0,0,0) = 0`. ∎

*Universality, at the source's standing.* Morita–Ueno realize a Fredkin gate in Model 1 and infer
computation universality (p. 141, §4) [LIT-R]. NU8 embeds every Model-1 orbit step for step, so a
Model-1 universal configuration maps to an `R_{Model 1}` configuration that carries out the same
computation.
- `E` maps a configuration that is quiescent outside a finite set (`f_P(0) = 0`, by
  conservativity) to a periodic tag-and-clock background with a finite change. So finite Model-1
  configurations become ultimately periodic ones.
- Not checked here: whether Morita–Ueno's universal constructions need non-ultimately-periodic
  configurations; and the transfer to U1's Definition U, which is F1 §3.1 consequence 1's caveat.
- *Three dimensions.* Let `F` depend only on the four in-plane neighbours, with the planes
  `z ≠ 0` at 0. Off-plane sites see zero in-plane tags and get `F = 0`. This gives a rule on `ℤ³`
  that reads nearest neighbours only, with no self-term. Its `F` does not depend on the `±z`
  neighbours, so its coupling graph is the planar square lattice in each plane, not ledger (x)'s
  simple-cubic graph on the reference class. A variant whose `F` reads the `±z` neighbours is not
  treated here: NU8 is not extended until the owner rules on §6 item 1.

**Classification under the owner's construction standard.** [#1169 c.7066602480](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7066602480) item 4: "A universal
computational capability, an existence theorem or a simulation design does not by itself constitute a
construction. A construction requires an explicit admissible implementation under the native rule,
with its encoding, dynamics and correctness established." NU8 is a simulation design for a rule that
is not the native rule. It is therefore **not a construction under the native rule**. It is classed
as a **proposed comparison construction** (conditional), not a completed one.
- *Established on paper [W, confirmed in review at `ef25e3bf`]:*
  - the rule `R_P` (alphabet, role table, six-phase `F`) and the encoding `E`;
  - the narrow-class membership;
  - the written correctness proof of `Ψ⁶ ∘ E = E ∘ F_P` for every 16-state 2RPCA(4) `P`.
- *At Morita–Ueno's standing only [LIT-R]:* the universality of Model 1, and hence of
  `R_{Model 1}`, in their sense.
- *Not established:*
  - any execution: NU8-CHECK is preregistered with amendment A01 and has not been run;
  - the transfer to U1's Definition U;
  - anything about `R_q`, OI's native rule, at any `q`;
  - any implementation under the native rule.

**Skepticism (the favourable branch, §A.31).**
1. *It is a comparison model.* `F` depends on neighbour positions (not isotropic), on whole values
   (not totalistic) and on a designed periodic background of tags and clocks. `R_q` is totalistic,
   cubic-symmetric and has no tags. NU8 says nothing about `R_q` at any `q`. The owner's
   distinction in #1169 c.7064226074 applies in full.
2. *Every part is a writer's derivation.* NU8 is [W]. No simulation was run: a check would be a
   computation, preregistered in `plans/NU8-CHECK-PREREG.md` and not run. The proof needs `f_P` to
   be a bijection, and `f_P(0) = 0` for the ultimately-periodic remark.
3. *The universality conclusion inherits Morita–Ueno's notion and standing.* Their argument is a
   construction shown in figures (Fredkin gate from I-gates and switch gates). The Fredkin-gate
   universality it relies on is Fredkin–Toffoli's (cited there).
4. *The alphabet is large.* `q = 8995` uses three coprime fields. Whether a small alphabet, an
   isotropic `F` or a totalistic `F` suffices in the narrow class is open.

***

## 4. Updated verdicts (at the level established)

| Question | Before (F1 §4) | Now |
|---|---|---|
| Goal A, broad class | answered at sketch level (Margolus 1984, App. A) | unchanged |
| Goal A, narrow class | open | a proposed comparison construction on paper (NU8, [W]; universality at Morita–Ueno's standing) for a non-isotropic, non-totalistic rule at `q = 8995`; not executed; not a construction under the native rule; open for isotropic or totalistic members |
| Goal B, Q | open; decisive question "bounded breach or growth" | open; decisive question restated as a controlled transfer confined in a closed region `D = cl₂(lines ∪ R)` (NU5). A healing breach relative to `D` is excluded (NU4). Planar confined transits are ternary at every tick (NU6) |
| P3 S1 | preregistered | open; axis tips die (NU7); reformulated by NU3 |

The native rule is not settled by NU8 or by any comparison model.

***

## 4a. (N)/(I) classification and Established / Assumed / Missing

**Definition** (owner, [#1169 c.7064843184](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7064843184) and [#1169 c.7064859041](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7064859041)). The label records the assumptions a result rests on, not
where the result is stored.
- **(N):** a theorem proved from OI's native assumptions.
- **(I):** a conditional theorem that requires imported quantum or operational assumptions. Each
  imported assumption is named.

Review and `main` status are recorded separately in the Status column.

Native assumptions used below:
- the published rounded rule `R_q` (SM:294) at the working reference `q = 2^16` on `ℤ³`;
- its second-order reversible form (Main ledger (xiii));
- its finite alphabet.

"Uniform background `c`" and "finite perturbation" are scope conditions on the configurations
treated, not assumptions about nature.

| Result | Label | Status | Established | Assumed (where it enters) | Missing (earliest unsupported step; kind) |
|---|---|---|---|---|---|
| NU3 | (N) | this record: confirmed in review at `ef25e3bf` (#1499), not on `main`. It depends on F1 NU2, which is reviewed on #1489 and not on `main` until #1489 lands, and on MQ1's converse, which is on `main` (MEAS-Q, reviewed) | For finite perturbations of a uniform background of Q: periodic ⇔ bounded support over `t ≥ 0` ⇔ confined at every tick in one finite closed set with in-range boundary. Written proof, cycle (a)⇒(c)⇒(b)⇒(a) | native only. MQ1's converse in (a)⇒(c); NU2 in (b)⇒(a), which uses reversibility, the finite alphabet and the fixed-point property of `c` | none within the statement |
| NU4, NU4′ | (N) | this record: confirmed in review at `ef25e3bf`, not on `main`; depends on MQ1 (on `main`) | For any closed `D`, finite or infinite, with the complement at `c`: no breach at `t` ⇔ the complement is still at `c` at `t + 1` | native only. MQ1 and its converse at the closed set's boundary; current-slice breach as in MQ2 | none within the statement |
| NU5 | (N) | as NU4 | Relative to the allowed closed region `D`, no breach heals without radiation; a radiation-free transit is exactly a never-breached `D` | native only (NU4′) | it does not settle Q: whether a controlled transfer exists inside some never-breached `D = cl₂(lines ∪ R)` (mathematics) |
| NU6 | (N) | as NU4; (a) also uses U1 Lemma 2.1 (on `main`) | In a confined transit, `∂D` stays in range and `|S| ≤ 7` on `∂D`; a planar confined transit is ternary at every tick | native only (NU5; RZ inside Lemma 2.1's window for (a)) | whether a planar ternary turn exists (mathematics; a search would be a gated computation) |
| NU7 | (N) | as NU4; no off-`main` dependency | For a single-site seed, the six axis tips of the light cone are 0 from `t = ⌈log₃|b|⌉ + 1` (from `t = 1` when `|b| ≤ 1`) | native only (radius-1 light cone; contraction of `G`) | the rest of the light-cone surface (mathematics) |
| S1 (P3 stage 1) | (N) target, open | not established | reformulated by NU3; not proved or refuted | native only, as NU3 and NU7 | a sub-luminal growth mechanism, or an exact periodic counterexample (mathematics; P2 at `k = 1` would test it, gated) |
| NU8 | not an (N)/(I) statement about OI | confirmed in review at `ef25e3bf` as a paper design, not on `main`; classed as a proposed comparison construction, not a construction under the native rule (#1169 c.7066602480 item 4); not executed | For every 16-state 2RPCA(4) `P`, a narrow-class rule `R_P` on `ℤ²`, `q = 8995`, with injective `E` and `Ψ⁶ ∘ E = E ∘ F_P`. Written proof by phase invariants | no quantum or operational assumption. The object is a non-native comparison rule (neither isotropic nor totalistic, with a designed tag-and-clock background), so the result is not proved from OI's native assumptions and does not concern `R_q`. Within the proof: `f_P` bijective (Morita–Ueno Lemma 2.1) in phase 3, and `f_P(0) = 0` for the ultimately-periodic remark. Universality imports Morita–Ueno's Fredkin-gate construction and Fredkin–Toffoli's gate universality [LIT-R, at the source's standing] | the transfer to U1's Definition U, including whether Morita–Ueno's universal configurations are ultimately periodic (mathematics) |

***

## 5. Classification (§A.31) and assumption-watch

| Item | Class |
|---|---|
| NU4, NU4′, NU5: relative to a closed region, breach is radiation one tick later; the bounded-breach alternative of F1 §4 is not distinct from confinement | ELABORATING (MQ1's sharp converse at a closed set's boundary; corrects F1 §4's framing; does not settle Q, since `D` is free) |
| NU3: periodic ⇔ bounded ⇔ confined in a finite closed set at all ticks | ELABORATING (NU2, MQ2) |
| NU6(c): planar confined transits are ternary at every tick | NEW, minor |
| NU7: axis tips die | NEW, minor (closes one proof route for S1) |
| NU8: narrow-class simulation design for every 16-state 2RPCA(4) | NEW at design level; a proposed comparison construction, not a construction under the native rule (owner standard, #1169 c.7066602480 item 4) |
| S1 | open |

**AW-NU-2 (healing versus confinement).** For Q on a uniform background, statements of the form
"a breach that heals without radiation" must name the region. Relative to the region in which the
disturbance is allowed, such a breach does not exist (NU4). Relative to a smaller region it is a
transient inside confined dynamics. This bears on U2's AW-UNIV-3 and on MEAS-Q's breach language.

**AW-NU-3 (narrow class versus native constraints).** The narrow-class comparison rule needs
position-dependent reads and a designed tag-and-clock background. The open distance to `R_q` is
isotropy, totalisticity and the absence of such a background, not the neighbourhood.

**Fixed point.** One pass, with NEW items; the §A.31 fixed point is not reached.

***

## 6. Owner decision points

1. **NU8 and item 3(b): ruled.** [#1169 c.7066602480](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7066602480) item 4 sets the standard quoted in §3. Under it, NU8 is a
   proposed comparison construction and not a construction under the native rule. It was carried
   out as proof exploration under
   [c.7064767045](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7064767045),
   and has not been tested or run. NU8 is not extended further.
2. **The NU8 check** (`plans/NU8-CHECK-PREREG.md`, with amendment
   `plans/amendments/A01-NU8-CHECK-six-ticks.md`): a bounded exact comparison of `Ψ⁶ ∘ E` with
   `E ∘ F_P`, preregistered and not run. It needs authorization.
3. **Next step for Q.** The confined-transfer question of NU5, starting with the planar ternary
   case of NU6(c). Any search there is a computation and stays gated.

***

## 7. Replay

The base branch's exact checks were replayed and match their committed output (F1 `results.json`).
No other computation was run.
