# NATIVE-UNIV, round 6: W2 rays and segments ending at the bare NU9 breather leak or are inadmissible

**Standing.** Writer's research record, paper only, unreviewed. It follows `PLAN.md` (`0f4d23e`),
committed first. No computation was run, no script is added and no exact check was replayed. Every
orbit below is derived by hand, tick by tick, or follows from a stated lemma. Every result that
uses NU9 is conditional on A-NU9: NU9 is hand re-derived (R4's review, R5's review), and its exact
re-run NU9-CHECK is pending and not authorized.

Inputs and their standing are listed in `PLAN.md`: `R5` (round 5: L1–L5, T-IND, Theorem T),
`R4` (NU9), `PT` (PLANAR-TURN), `P2N`, `F1` are reviewed or preregistered records not on `main`;
`U1`, `U2` and `MQ` are on `main`.

**Layer.** Every statement concerns the configuration dynamics of Q. None concerns effects,
instruments, accessible algebras or readouts.

***

## 0. Summary

1. **Definitions (§1).** A *W2 piece* is a straight ray, finite segment or line carrying the
   restriction of a W2 background; its end sites keep that restriction, and the background
   elsewhere is `c`. An end is *next to the cube* when it lies at ℓ1-distance 1 or 2 from it.
   An *admissible no-input orbit* is a no-input orbit that never leaks and is periodic (U2 R1;
   PT §3(a)). A controlled turn and a signal interaction both need one.
2. **General lemmas (§2), (N).** None uses NU9 except L8's clause on the breather.
   - L6: a W2 piece is closed, its free orbit is confined and frozen, and (W) holds at every one of
     its sites, the ends included.
   - L7 (*truncation*): shortening a piece changes nothing up to a leak as long as the sites at and
     next to the cut stay at their free values.
   - L8 (*time reversal*): `y_s ↦ −y_{T−s}` (`T` even) maps orbits to orbits, leaks to leaks and
     periodic orbits to periodic orbits, and exchanges the two background types of a piece.
   - L9 (*end locking*): if a piece end `e` has exactly two allowed neighbours, a gadget site `g`
     and its piece neighbour `r`, and `e`, `r` keep their free values, then
     `y_t(g)·w_t(r) ≤ 0`. A value of `g` that recurs after `P ≡ 2 (mod 4)` ticks vanishes at
     `r`'s active ticks. This is R5's L4 with the end in place of the coupling site.
3. **T-IND′ (§4), (N), conditional on A-NU9.** R5's T-IND holds verbatim with lines replaced by
   W2 pieces. Every matched piece at ℓ1-distance exactly 2 from the cube leaks within 20 ticks.
4. **Theorem H (§5–6), (N), conditional on A-NU9.** Let one matched W2 ray, or segment of at least
   two sites, end head-on at a face of the cube: `{(x, a, b) : 2 ≤ x ≤ x₁}`, `x₁ ≥ 3` or `∞`, with
   `(a, b) ∈ {(0,0), (1,0), (1,1)}` up to symmetry (end next to a face centre, edge midpoint or
   corner). At a uniform background `3 ≤ c ≤ q − 4`:
   - (a) for each placement, every one of the 20 starts of one background type (the f-cycle) leaks,
     within 12 ticks;
   - (b) none of the 40 initial states has an admissible no-input orbit (by (a) and L8);
   - (c) for rays, the starts of the other type (the g-cycle) also leak forward, within 23 ticks,
     except 9 starts at the face-centre placement. These do not leak through tick 30 by hand, and
     their forward fate is MISSING. They are not admissible, by (b).
5. **Lemma L10 (§5.0), conditional on A-NU9.** At a head-on end, when the end site is driven to 0
   (*erased*), the configuration is NU9 plus the piece shortened by one site, and the erased site
   is driven back to `±1` within 20 ticks by the period mismatch.
6. **Excluded class (§7), conditional on A-NU9.** The bare breather plus one straight matched W2
   piece, either at ℓ1-distance 2 from the cube in any placement or head-on at distance 1 with at
   least two sites, has no admissible no-input orbit. So it carries no controlled turn and no signal interaction. With
   several pieces, every arrangement without direct contact and with one coupling site exclusive to
   one matched piece leaks (T-IND′). This covers the thick J2 analogue with both arms at distance 2.
7. **Necessary condition, not universality (§7).** In an admissible no-input orbit of any gadget, a
   gadget site carrying a nonzero value of period ≡ 2 (mod 4) cannot stay for 20 ticks at a corner
   or end contact whose piece sites keep their free W2 values (L4, L9). This is a condition on designs. A gadget meeting it would still not show that
   R_q is universal.
8. **MISSING (§8).** Not settled:
   - pieces alongside a face that end next to the cube;
   - single-site segments;
   - two or more pieces with a direct contact, including the thick J1 analogue;
   - the forward fate of the 9 starts of item 4(c);
   - NU9-CHECK.

   No claim is made that R_q is non-universal.
9. **Productivity (§9):** gem by (ii), for the class of item 6, and by (iii), for L9.

***

## 1. Definitions

Notation as in R5 §1: RZ, `y = x − c`, `y_{t+1}(i) = G(S_t(i)) − y_{t−1}(i)` with
`G(s) = ⌊(s+1)/3⌋`, `S_t(i)` the sum over the six neighbours, `p(i) = i₁ + i₂ + i₃ mod 2`. The
slots `(i, t)` with `p(i) + t` even form one component (NU1). The NU9 cube is `C = {−1,0,1}³` with
the classes `O, E1, E2, C3` and the orbit of R5 §1. Its nonzero phases are: `O` at 0 (`+2`), 8
(`−2`); `E1` at 1 (`+1`), 7 (`−1`); `E2` at 2 (`+1`), 6 (`−1`); `C3` at 3 (`+1`), 5 (`−1`). With
the breather at phase `t mod 10`, NU9 occupies the component `p(i) + t` even. The breather sums used
below are `S_b(i)`, the sum over the cube neighbours of `i`.

**W2 piece.** Let `ℓ` be an axis line, and let `P ⊂ ℓ` be a ray, a finite segment of `n ≥ 1`
consecutive sites, or `ℓ` itself. A *W2 piece* on `P` is the restriction to `P` of a W2 background
on `ℓ` (U1 E2; R5 §1): the values on `P` are those of the background, the piece's configuration is
0 off `P` (the background `c` in Q), and nothing else is added. In particular:
- each site of `P` carries `±1` at the ticks at which its slot lies in the piece's component and 0
  at the others;
- along `P`, the nonzero values of one tick alternate in sign over every second site;
- an end site keeps exactly its restricted value. No other filling of a finite segment
  (U1 E6 stores an arbitrary trit per site) is in this class.

A piece is *matched* when its nonzero slots lie in the breather's component. Its *ends* are its
sites with one piece neighbour.

**Placements.** By the cube's symmetry group, which fixes NU9 and maps axis pieces to axis pieces,
every axis piece lies along `e₁` at `{(x, a, b) : x ∈ I}` with `a ≥ b ≥ 0` and `I` an interval. With
`δ(a, b) = max(a−1, 0) + max(b−1, 0)` as in R5 §3, the piece's ℓ1-distance from `C` is
`δ(a, b) + dist(I, [−1, 1])`.
- *Head-on:* `δ(a, b) = 0`, that is `(a, b) ∈ {(0,0), (1,0), (1,1)}`. Then `I ⊂ [2, ∞)` up to
  `x ↦ −x`, and the end `(min I, a, b)` faces a cube site of class `E1`, `E2` or `C3`. Write `H00`,
  `H10`, `H11` for `min I = 2` (distance 1).
- *Alongside:* `δ(a, b) = 1`, `(a, b) ∈ {(2,0), (2,1)}`. The piece runs parallel to a face.
- *Indirect:* any placement at distance exactly 2.
- *Independent:* distance ≥ 3, or unmatched (L3).

An end is *next to the cube* when its ℓ1-distance from `C` is 1 or 2.

**Background cycles of a head-on piece.** Let `κ = a + b`. A matched piece's active slots are those
with `x + κ + t` even. For each placement the four backgrounds fall into two 20-tick free cycles
(R5 §3), each containing one background type with both signs ((W)):
- *f-cycle:* `H00` and `H11`: `w_t(x) = (−1)^{(x+t)/2}`; `H10`: `w_t(x) = (−1)^{(x+1+t)/2}`;
- *g-cycle:* `g_t(x) = (−1)^{x+κ} w_t(x)`, the f-cycle with the sign reversed on the sites with
  `x + κ` odd.

Both are W2 backgrounds: `w_{t+2} = −w_t`, and the nonzero values alternate along the line. For a
ray, R5's mirror `x ↦ −x` does not map the piece to itself, so the g-cycle is not reduced to the
f-cycle by a reflection. L8 relates them instead.

**Leak; no-input orbit.** As in R5 §1: the allowed region is `A = C ∪ pieces`, and a run *leaks* at
`t` when some site outside `A` differs from `c` at `t`. The *no-input orbit* of an initial state is
its orbit with no signal launched. *Free superposition*, *coupling site*, *contact site*, *event*,
*I-event*, *O-event* are as in R5 §2 (L5) and §5.

**Admissible no-input orbit.** A no-input orbit is *admissible* when it never leaks and is
periodic. Periodicity is PT §3(a)'s return requirement, which T and T-STATEFUL presuppose (PT §2),
and U2 R1's quiescence (`N(4) = N(0)`). A periodic orbit is defined at every tick of `ℤ`, so an
admissible orbit is leak-free at every tick of `ℤ`.

**Controlled turn; signal interaction.** As in R5 §1, with pieces in place of full lines and with
the no-input orbit required to be admissible. For a controlled turn this is PT's requirement. For a
signal interaction it is stronger than R5's, which asked only for a forward leak-free no-input
orbit. The difference matters only for the 9 starts of Theorem H(c), and §8 lists it.

**Relation to Definition U.** Turns and signal interactions are building blocks (U1 §3). A negative
result here concerns the stated class only. A positive gadget would be a building block only.

***

## 2. General lemmas

R5's L1–L5 are used as proved there. L1 (outside sums) and L5 (first deviation) hold for any
allowed region and any parts confined to closed sets; L4 holds for any line site carrying (W).

**L6 (W2 pieces) [W, (N)].** Let `P` be a W2 piece. Then:
- (a) `P` is closed: a site off `P` has at most one neighbour in `P`;
- (b) run alone, the piece is frozen: `y_{t+1} = −y_{t−1}` at every site of `P`, every site off
  `P` stays at 0, and every value is ternary;
- (c) (W) holds at every site `l` of `P`, ends included: `w_{t+2}(l) = −w_t(l)`,
  `w_{t+10}(l) = −w_t(l)`, and `w_t(l) = ±1` at every active slot.

*Proof.* (a) `P` lies on one axis line, and a site off that line has at most one neighbour on it.
A site of the line outside `P` is adjacent to at most one site of `P`, an end. (b) At a tick at
which a site `k` of `P` updates, its `P`-neighbours `k ± 1` lie in the class active at that tick.
In the interior they carry opposite values (alternation), so the sum is 0. At an end there is one
`P`-neighbour, so the sum is in `{−1, 0, 1}`. In both cases `G = 0` and `y_{t+1}(k) = −y_{t−1}(k)`.
This map preserves the alternation, so the argument repeats at every tick. A site off `P` has sum in
`{−1, 0, 1}` and previous value 0, so it stays 0 (U1 Lemma 2.2; MQ1). (c) follows from (b). ∎

*Consequence.* R5's L3, L4 and L5 apply to W2 pieces exactly as to full lines: each piece is a
closed set whose free orbit is confined, with ternary boundary, and each of its sites satisfies
(W). L3(b) is MQ2(b) for closed sets at distance ≥ 3.

**L7 (truncation) [W, (N)].** Let `P ⊂ P̂` be two W2 pieces on the same line, the values on `P`
being the restriction of those on `P̂`, and let a gadget `K` be given. Let `Ŷ` be the orbit with
`P̂` and `Y` the orbit with `P`, from the restricted initial state. Suppose that `Ŷ` does not leak
up to `T − 1`, and that at every tick `≤ T − 2`, for each end `e` of `P` with outward neighbour
`e⁺ ∈ P̂ ∖ P` and inward neighbour `e⁻ ∈ P`, the sites `e⁻`, `e`, `e⁺` carry their free W2 values
in `Ŷ`. Then:
- `Y` equals `Ŷ` at every site outside `P̂ ∖ P`, and is 0 on `P̂ ∖ P`, at every tick `≤ T − 1`;
- a leak of `Ŷ` at `T` at a site not adjacent to `P̂ ∖ P` is a leak of `Y` at `T`.

*Proof.* By induction over `t ≤ T − 2`, for the step `t → t + 1`.
- A site whose closed neighbourhood avoids `P̂ ∖ P` reads the same values in both runs.
- The end `e` reads `e⁻` in `Y`, and `e⁻ + e⁺` in `Ŷ`. Both carry free values, so the first sum is
  in `{−1, 0, 1}` and the second is 0 (alternation). Both give `G = 0`, so `e` updates to
  `−y_{t−1}(e)` in both runs.
- `e⁺` is outside the allowed region of `Y`. Its sum there is `y_t(e)`, ternary since `e` is free,
  so it stays 0. The other sites of `P̂ ∖ P` read only 0s and sites outside both allowed regions,
  so they stay 0 in `Y`.
- A site off the line adjacent to `P̂ ∖ P` is outside both allowed regions, so it is 0 in `Ŷ` (no
  leak up to `T − 1`). In `Y` its sum is 0, so it stays 0.

At `T`, a leaking site `o` of `Ŷ` not adjacent to `P̂ ∖ P` reads, at `T − 1`, only sites at which the
two runs agree, and its previous value is 0 in both. It lies outside both allowed regions. ∎

**L8 (time reversal) [W, (N)].** For any orbit `y` of RZ on `ℤ³` and any even `T`,
`ỹ_s := −y_{T−s}` is an orbit. It occupies the same component as `y`. It leaks at `s` if and only if
`y` leaks at `T − s`, and it is periodic if and only if `y` is. For a head-on piece, it maps the set
of free superpositions (NU9 at some phase, f-cycle piece) onto the set (NU9 at some phase, g-cycle
piece), and conversely.

*Proof.* The update is `y_{t+1} + y_{t−1} = G(S_t(y))`, symmetric under `t ± 1`. So
`ỹ_{s+1} + ỹ_{s−1} = −(y_{T−s−1} + y_{T−s+1}) = −G(S(y_{T−s})) = G(S(ỹ_s))`, because `G` is odd and
`S` linear. A slot `(i, s)` of `ỹ` is nonzero only if `(i, T − s)` is for `y`, and `T` is even, so
the component is the same. The statements on leaks and periods follow, since the allowed region
is the same and `−0 = 0`.
- *NU9:* NU9 satisfies `y_s = −y_{8−s}` (R4 §1). So `−NU9_{φ+T−s} = NU9_{s+(8−T−φ)}`, which is NU9
  at another phase.
- *Piece:* each f-cycle formula of §1 has the form `w_t(x) = ε (−1)^{(x+κ+t)/2}` with a fixed sign
  `ε`, and on active slots `(−1)^s = (−1)^{x+κ}`. Since `(x+κ−s)/2 = (x+κ+s)/2 − s`,
  `−w_{T−s}(x) = −ε (−1)^{T/2} (−1)^{(x+κ+s)/2} (−1)^{s} = ∓ (−1)^{x+κ} w_s(x)`. That is a g-cycle
  background. The converse is the same computation. ∎

*Use.* If every f-cycle start of a placement leaks forward, no g-cycle orbit is admissible.
Suppose a g-cycle orbit `y` were periodic and never leaked. Then `y` is leak-free on `ℤ`, and so is
`ỹ`. But `ỹ` passes, at the ticks `(T − τ₀, T − τ₀ + 1)`, through the state
`(−y_{τ₀}, −y_{τ₀−1})`, which is a free f-cycle state, and from there it leaks. L8 says nothing about
the forward orbit of a g-cycle state, which may avoid a leak for a while (Theorem H(c)).

**L9 (end locking) [W, (N)].** In a run that does not leak up to tick `t`, let `e` be an end of a
matched W2 piece, `r` its piece neighbour, and suppose the allowed neighbours of `e` are exactly
`r` and one gadget site `g`. If `e` has its free value at `t − 1` and `t + 1`, and `r` at `t`, then
`|y_t(g) + w_t(r)| ≤ 1`. Hence:
- (a) at a tick at which `r` is active, `y_t(g)` is 0 or of sign `−w_t(r)`, and `|y_t(g)| ≤ 2`;
- (b) if `y_{t+P}(g) = y_t(g)` with `P ≡ 2 (mod 4)`, and the hypothesis holds at `t` and `t + P`
  with `r` active, then `y_t(g) = 0`.

*Proof.* `S_t(e) = y_t(g) + y_t(r)`, since the other neighbours of `e` are outside `A` and 0.
Free values at `t ± 1` mean `y_{t+1}(e) = −y_{t−1}(e)`, so `G(S_t(e)) = 0` and `|S_t(e)| ≤ 1`. The
rest is R5's L4 proof with `e` in place of the outside site. ∎

*Reading.* An end that keeps its W2 values is a coupling site that happens to lie inside `A`. When
the inequality fails, `e` departs from W2. That is an I-event at `e`, not a leak.

***

## 3. Single pieces with an end next to the cube

Up to symmetry, a single straight piece disjoint from `C` with an end next to the cube is one of:

| Case | Placement | Where treated |
|---|---|---|
| unmatched, any distance | — | L3(a): independent |
| matched, distance 2 | any `(a, b)`, `I` | T-IND′ (§4): leaks |
| matched, head-on, distance 1 | `H00`, `H10`, `H11`, `|I| ≥ 2` | Theorem H (§5–6) |
| matched, head-on, single site | `I = {2}` | MISSING |
| matched, alongside, distance 1 | `(2,0)` or `(2,1)` with `I ∩ [−1, 1] ≠ ∅` and an end at `|x| ≤ 2` | MISSING |

A head-on piece with `min I = 3` has distance 2. An alongside piece whose interval misses `[−1, 1]`
and ends at `x = ±2` has distance 2. A placement with `δ(a, b) = 2` whose interval meets `[−1, 1]`
has distance 2. All of these fall under T-IND′.

***

## 4. Indirect contact: T-IND′

**Proposition T-IND′ [W, (N), conditional on A-NU9].** Let a bare breather and W2 pieces
`P_1, …, P_m` be given, in either component and at any distance. The cube and the pieces are
pairwise disjoint, and no site of one is adjacent to a site of another. The allowed region is their
union. Suppose some coupling site `o` is adjacent to a cube site `g` and to a site `l` of a matched
piece, and to no site of any other matched piece. Then, from every initial phase and background,
the configuration leaks within 20 ticks.

*Proof.* R5's proof of T-IND, word for word. Its inputs are:
- L5(b), which needs closed confined parts: L6(a), (b);
- (W) at `l`, with `w = ±1` at `l`'s active slots, ends included: L6(c);
- NU9's values at `g ∈ C ∖ O`.

Nothing in it uses the infiniteness of a line. ∎

**Corollary (single piece at distance 2).** Every matched W2 piece at ℓ1-distance exactly 2 from
the cube leaks within 20 ticks, from all 40 initial states.
*Proof.* Take `g ∈ C` and a piece site `l` at distance 2, and `o` a common neighbour. `o` is not in
`C`, since `l` is at distance 2. It is not in the piece, since the piece is at distance 2. `o` has
at most one neighbour in each of the closed sets `C` and `P`, so it has exactly the two allowed
neighbours `g` and `l`. `g` is a boundary site, so `g ∈ C ∖ O`. T-IND′ applies with `m = 1`. ∎

For example, the head-on ray with end `(3, a, b)` has the single coupling site `(2, a, b)`.

***

## 5. Head-on direct contact (`H00`, `H10`, `H11`)

Let `e = (2, a, b)` be the end, `g = (1, a, b)` the cube site it touches, and `r_x = (x, a, b)` the
piece sites (`e = r_2`). Free values are written `w_t(x)` (§1).

**Geometry, common to the three placements.**
- `g` is the only cube site adjacent to the piece, and `e` the only piece site adjacent to the
  cube. These are the contact sites.
- The outside sites adjacent to `e` are its four transverse neighbours `(2, a', b')`. Such a site is
  a coupling site, with cube neighbour `(1, a', b')`, when `|a'|, |b'| ≤ 1`. Otherwise it is a
  *cap* of `e`: its only allowed neighbour is `e`.
- No other outside site has neighbours in both the cube and the piece. A site with first coordinate
  ≥ 3 is not adjacent to `C`.
- Every piece site `r_x`, `x ≥ 3`, has four caps. By L1, every piece site with a cap is ternary in a
  run without a leak, and a value `±2` there leaks at the next tick.
- In the free cycle only `g` and `e` can deviate. Every `r_x`, `x ≥ 3`, has free piece neighbours
  and no cube neighbour.
- In the g-branches below, `w_t` denotes the g-cycle values.

**Starts.** For each placement and cycle, the 20 starts `τ₀ ∈ {0, …, 19}` are the states
`(Y(τ₀ − 1), Y(τ₀))` of the free cycle `Y`. A start whose first event, at a tick `≥ τ₀`, is an
O-event leaks one tick later (L5(a)). The others are followed tick by tick. In each branch below,
every site whose value differs from `Y` is listed, together with the sites that decide the outcome.
Sites not mentioned at a step read only free values and keep their free values. Where a step finds
a value `±2` at a site with a cap, or a sum `|S| ≥ 2` at a coupling site, the run leaks at the next
tick. The conclusion "leaks by `T`" does not depend on whether an earlier leak was missed: up to the
first leak every outside site is 0, which is what each step assumes.

### 5.0 The erased end

**Lemma L10 (erased end) [W, (N), conditional on A-NU9].** In a head-on placement, suppose that at
ticks `(s − 1, s)` the configuration is NU9 at some phase, plus the W2 values of a piece of the
same cycle on `P' = {r_x : x ≥ 3}` (or `3 ≤ x ≤ x₁`), with `y(e) = 0` at both ticks. Then it is
this free superposition, with `y(e) = 0`, up to the first tick `u ≥ s` at which
`|y_u(g) + w_u(r_3)| = 2`. Such a tick exists with `u ≤ s + 19`. At `u + 1`, `y(e) = ±1` with the
sign of that sum, and every other site has its value in the free superposition.

*Proof.* `C` and `P'` are closed, at distance 2, and their only common neighbour is `e`, which is
an allowed site. With `y(e) = 0`, the coupling sites of `e` read a cube value and 0, and the caps
read 0. `g` reads NU9's own sum, since `y(e) = 0`, and `r_3` reads only `r_4`, so it stays frozen.
By L5(a), the only site that can depart is `e`. It reads `y_u(g) + w_u(r_3)`, with previous value 0,
so it stays 0 exactly while that sum is in `{−1, 0, 1}`. The bound `u ≤ s + 19` is T-IND's
argument with `e` in place of `o`: `g` and `r_3` have the same parity, `g`'s class is nonzero at
some phase in every 10 ticks, and `w(r_3)` changes sign over 10 ticks while `y(g)` does not. ∎

### 5.1 Placement `H11` (end next to the corner `(1,1,1)`)

- `e = (2,1,1)`, active at even `t`.
- `g = (1,1,1)` (C3), active at odd `t`.
- Coupling sites: `(2,1,0)` and `(2,0,1)`, with cube neighbours `(1,1,0)` and `(1,0,1)` (E2).
- Caps of `e`: `(2,2,1)` and `(2,1,2)`.
- Breather sum at `g`: `S_b(g) = 3·E2`, which is `3` at phase 2 and `−3` at phase 6.

**Free values.** f-cycle:
- `w_t(2) = (−1)^{(t+2)/2}`, which at `t = 0, 2, …, 18` is `−, +, −, +, −, +, −, +, −, +`;
- `w_t(3) = (−1)^{(t+3)/2}`, which at `t = 1, 3, …, 19` is `+, −, +, −, +, −, +, −, +, −`.

g-cycle: `w_t(2)` is the same, and `w_t(3)` has the opposite sign.

**Events (f-cycle).**
- *O at the coupling sites* (even `t`; E2 value plus `w_t(2)`). At `t = 2, 6, 12, 16` the sums are
  `1+1, −1+1, 1−1, −1−1`. So O-events occur at 2 and 16.
- *I at `g`* (even `t`). The sums are `3 ± 1` and `−3 ± 1` at the E2 phases, and `±1` otherwise.
  `G` is unchanged in every case (L2). So `g` never deviates.
- *I at `e`* (odd `t`; `y_t(g) + w_t(3)`). At `t = 3, 5, 13, 15` the sums are `1−1, −1+1, 1+1, −1−1`.
  So I-events occur at 13 and 15.

| `τ₀` | first event | outcome |
|---|---|---|
| 17–19, 0–2 | 2 (O) | leak at 3, `(2,1,0)` and `(2,0,1)` |
| 3–13 | 13 (I at `e`) | F1: leak at 15 |
| 14, 15 | 15 (I at `e`) | F2: leak at 17 |
| 16 | 16 (O) | leak at 17 |

- **F1.** At `13 → 14`, `e`: `G(2) − y_{12}(e) = 1 − (−1) = 2`. At `14 → 15`, the cap `(2,2,1)` has
  sum 2: **leak at 15**.
- **F2.** At `15 → 16`, `e`: `G(−2) − y_{14}(e) = −1 − 1 = −2`. The cap has sum −2: **leak at 17**.

**Events (g-cycle).** O-events at 2 and 16, as before, and none at `g`. At `e` the sums at
`t = 3, 5, 13, 15` are `1+1, −1−1, 1−1, −1+1`. So I-events occur at 3 and 5.

| `τ₀` | outcome |
|---|---|
| 17–19, 0–2 | leak at 3 |
| 3 | G1: leak at 7 |
| 4, 5 | G2: leak at 27 |
| 6–16 | leak at 17 |

- **G1.**
  - `3 → 4`: `e`: `G(2) − y_2(e) = 1 − 1 = 0` (free −1).
  - `4 → 5`: the cube is 0 at phase 4, and `e` reads `y_4(g) + y_4(r_3) = 0`. Every neighbour of
    `e` keeps its free value. The only difference is `y_4(e)`.
  - `5 → 6`: `e`: `G(−1 − 1) − y_4(e) = −1 − 0 = −1` (free +1).
  - `6 → 7`: `(2,1,0)` has sum `y_6(1,1,0) + y_6(e) = −1 − 1 = −2`: **leak at 7**.
- **G2.**
  - `5 → 6`: `e`: `G(−2) − y_4(e) = −1 + 1 = 0`.
  - `6 → 7`: `g`: `G(−3 + 0) − y_5(g) = −1 + 1 = 0`, the NU9 value. `r_3`: `G(0 + w_6(4)) = 0`,
    free.
  - `7 → 8`: `e`: `G(y_7(g) + w_7(3)) − y_6(e) = G(0 + 1) − 0 = 0`.
  - The state at `(7, 8)` is erased (L10). The first `u ≥ 8` with `|y_u(g) + w_u(3)| = 2` is
    `u = 23` (C3 `+1`, `w_{23}(3) = +1`). At 13 and 15 the sums are 0.
  - `23 → 24`: `e = 1`.
  - `24 → 25`: `r_3`: `G(1 + w_{24}(4)) − w_{23}(3) = G(2) − 1 = 0` (free −1). `g`, `e`'s caps and
    the coupling sites read sums in `{0, 1}`.
  - `25 → 26`: `e`: `G(y_{25}(g) + y_{25}(r_3)) − y_{24}(e) = G(−1 + 0) − 1 = −1`. `r_4` reads
    `0 + w_{25}(5) = 1` and stays free.
  - `26 → 27`: `(2,1,0)` has sum `y_{26}(1,1,0) + y_{26}(e) = −1 − 1 = −2`: **leak at 27**.

Up to each leak, only `e` and `r_3` depart from the free cycle. Every value lies in `{−2, …, 2}`.

### 5.2 Placement `H10` (end next to the edge midpoint `(1,1,0)`)

- `e = (2,1,0)`, active at odd `t`.
- `g = (1,1,0)` (E2), active at even `t`.
- Coupling sites: `(2,0,0)`, with cube neighbour `(1,0,0)` (E1); and `(2,1,±1)`, with cube
  neighbours `(1,1,±1)` (C3).
- Cap of `e`: `(2,2,0)`.
- Breather sum at `g` (odd `t`): `S_b(g) = 2·E1 + 2·C3`, which is `2, 2, −2, −2, 0` at phases
  1, 3, 5, 7, 9.

**Free values.** f-cycle:
- `w_t(2) = (−1)^{(t+3)/2}`, which at `t = 1, 3, …, 19` is `+, −, +, −, +, −, +, −, +, −`;
- `w_t(3) = (−1)^{(t+4)/2}`, which at `t = 0, 2, …, 18` is `+, −, +, −, +, −, +, −, +, −`.

g-cycle: `w_t(2)` has the opposite sign, and `w_t(3)` is the same.

**Events (f-cycle).**
- *O at `(2,0,0)`.* The sums at `t = 1, 7, 11, 17` are `1+1, −1−1, 1−1, −1+1`, so O-events occur at
  1 and 7.
- *O at `(2,1,±1)`.* The sums at `t = 3, 5, 13, 15` are `1−1, −1+1, 1+1, −1−1`, so O-events occur
  at 13 and 15.
- *I at `g`* (odd `t`, `S_b + w_t(2)`). The sums at `t = 1, 3, 5, 7, 11, 13, 15, 17` are
  `3, 1, −1, −3, 1, 3, −3, −1`. By L2, I-events occur at 3, 5, 11 and 17.
- *I at `e`* (even `t`, `y_t(g) + w_t(3)`). The sums at `t = 2, 6, 12, 16` are
  `1−1, −1−1, 1+1, −1+1`, so I-events occur at 6 and 12.

| `τ₀` | first event | outcome |
|---|---|---|
| 18, 19, 0, 1 | 1 (O) | leak at 2, `(2,0,0)` |
| 2, 3 | 3 (I at `g`) | P1: leak at 8 |
| 4, 5 | 5 (I at `g`) | P2: leak at 8 |
| 6 | 6 (I at `e`) | P3: leak at 8 |
| 7 | 7 (O) | leak at 8, `(2,0,0)` |
| 8–11 | 11 (I at `g`) | P4: leak at 14 |
| 12 | 12 (I at `e`) | P5: leak at 14 |
| 13 | 13 (O) | leak at 14, `(2,1,±1)` |
| 14, 15 | 15 (O) | leak at 16, `(2,1,±1)` |
| 16, 17 | 17 (I at `g`) | P6: leak at 26 |

- **P1.**
  - `3 → 4`: `g`: `G(1) − y_2(g) = −1` (free 0).
  - `4 → 5`: `(0,1,0)` and `(1,0,0)` read −1, so 0, free. `(1,1,±1)` read −1, so
    `0 − y_3 = −1`, free. `e` reads `−1 + w_4(3) = 0`, so free.
  - `5 → 6`: `g`: `G(−2 + w_5(2)) − y_4(g) = G(−1) + 1 = 1` (free −1).
  - `6 → 7`: `(1,1,±1)` read `1 − 1 − 1 = −1`, so `0 − y_5 = 1` (free 0). `(1,0,0)` reads
    `1 − 1 − 1 − 1 = −2`, so −1, free. `e` reads `1 + w_6(3) = 0`, so −1, free.
  - `7 → 8`: `(2,0,0)` has sum `y_7(1,0,0) + y_7(e) = −1 − 1 = −2`: **leak at 8**.
- **P2.**
  - `5 → 6`: `g`: `G(−1) − y_4(g) = 0` (free −1).
  - `6 → 7`: every neighbour of `g` takes its free value. The E1 sums are −3, the C3 sums −2, and
    `e` reads `0 + w_6(3) = −1`.
  - `7 → 8`: the free O-event at `(2,0,0)` reads `−1 − 1 = −2`: **leak at 8**.
- **P3.** `6 → 7`: `e`: `G(−2) − y_5(e) = −1 − 1 = −2`. The cap `(2,2,0)` then has sum −2:
  **leak at 8**.
- **P4.**
  - `11 → 12`: `g`: `G(1) − y_{10}(g) = 0` (free 1).
  - `12 → 13`: the E1 neighbours read 3, so `1 − 1 = 0`, free. The C3 neighbours read 2, so 1,
    free. `e` reads `0 + w_{12}(3) = 1`, so free.
  - `13 → 14`: `(2,1,±1)` has sum `1 + 1 = 2`: **leak at 14**.
- **P5.** `12 → 13`: `e`: `G(2) − y_{11}(e) = 1 + 1 = 2`. The cap has sum 2: **leak at 14**.
- **P6** (the longest f-branch).
  - `17 → 18`: `g`: `G(−1) − y_{16}(g) = 1` (NU9 phase 8: 0). Tick 18: `O = −2`, `g = 1`.
  - `18 → 19`: `(0,1,0)` and `(1,0,0)`: `G(−1) + 1 = 1`. Every other site is free. `e` reads
    `1 + w_{18}(3) = 0`, so free.
  - `19 → 20`:
    - `O`: `G(2) + 2 = 3`;
    - `g`: `G(1 + 1 + w_{19}(2)) − 1 = G(1) − 1 = −1`;
    - the other E2 read 1, so 0, free.
  - `20 → 21`:
    - `(0,1,0)` and `(1,0,0)`: `G(3 − 1) − 1 = 0`;
    - the other E1: `G(3) = 1`, free;
    - `e` reads `−1 + w_{20}(3) = 0`, so free.
  - `21 → 22`:
    - `O`: `G(4) − 3 = −2`;
    - `g`: `G(0 + 0 + w_{21}(2)) + 1 = 1`;
    - the E2 sites other than `g` with a neighbour among `(0,1,0)`, `(1,0,0)`, namely `(−1,1,0)`,
      `(1,−1,0)`, `(0,1,±1)` and `(1,0,±1)`: sum 1, so 0;
    - the remaining E2 `(−1,−1,0)`, `(−1,0,±1)`, `(0,−1,±1)`: 1.
  - `22 → 23`:
    - `(1,0,0)` and `(0,1,0)`: `G(−1) − 0 = 0`;
    - `(−1,0,0)`, `(0,−1,0)`, `(0,0,±1)`: `G(1)` or `G(0)`, minus 1, giving −1;
    - `(−1,−1,±1)`: `G(3) = 1`;
    - every other C3: `G(1) = 0`;
    - `e` reads `1 + w_{22}(3) = 0`, so free.
  - `23 → 24`:
    - `O`: `G(−4) + 2 = 1`;
    - `g`: `G(w_{23}(2)) − 1 = −1`;
    - `(−1,−1,0)`, `(−1,0,±1)`, `(0,−1,±1)`: sums 0 or −1, so −1;
    - every other E2: 0.
  - `24 → 25`: `(−1,−1,±1)`: E2 neighbours `−1, −1, −1`, so `G(−3) − 1 = −2`.
  - `25 → 26`: the cap `(−2,−1,1)` has sum −2: **leak at 26**.

  Throughout P6, `e`'s sum `y_t(g) + w_t(3)` is 0 at `t = 18, 20, 22, 24`, so the piece stays
  free.

**Events (g-cycle).**
- *O at `(2,0,0)`:* at 11 and 17.
- *O at `(2,1,±1)`:* at 3 and 5.
- *I at `g`:* the sums at `t = 1, 7, 13, 15` are `1, −1, 1, −1`, so I-events occur at 1, 7, 13
  and 15.
- *I at `e`:* at 6 and 12, as before.

| `τ₀` | outcome |
|---|---|
| 18, 19, 0, 1 | Q1: leak at 4 |
| 2, 3 | leak at 4 |
| 4, 5 | leak at 6 |
| 6 | Q2: leak at 14 |
| 7 | Q3: leak at 16 |
| 8–11 | leak at 12 |
| 12 | Q4: leak at 28 |
| 13 | Q5: leak at 22 |
| 14, 15 | Q6: leak at 18 |
| 16, 17 | leak at 18 |

- **Q1.**
  - `1 → 2`: `g = 0` (free 1).
  - `2 → 3`: every neighbour of `g` takes its free value, as in P4. `e` reads `0 + w_2(3) = −1`.
  - `3 → 4`: `(2,1,±1)`: `1 + w_3(2) = 1 + 1 = 2`: **leak at 4**.
- **Q2.**
  - `6 → 7`: `e`: `G(−2) − y_5(e) = −1 + 1 = 0`.
  - `7 → 8`: `g`: `G(−2 + 0) − y_6(g) = 0`, the NU9 value. The state at `(7, 8)` is erased (L10).
  - The first `u` is 12 (`g = +1`, `w_{12}(3) = +1`), so `e = 1` at 13.
  - `13 → 14`: `(2,1,±1)`: `1 + 1 = 2`: **leak at 14**.
- **Q3.**
  - `7 → 8`: `g`: `G(−2 + 1) + 1 = 1`.
  - `8 → 9`: `(0,1,0)` and `(1,0,0)`: `G(−1) + 1 = 1`. `e`: `G(1 + w_8(3)) − y_7(e) = 1 − 1 = 0`.
  - `9 → 10`: `O`: `G(2) + 2 = 3`. `g`: `G(2) − 1 = 0`. `r_3`: `G(0 + w_9(4)) − w_8(3) = −1`, free.
  - `10 → 11`: `(0,1,0)` and `(1,0,0)`: `G(3) − 1 = 0`; the other E1: 1. `e`: `G(0 − 1) − 0 = 0`.
  - `11 → 12`: `O`: `G(4) − 3 = −2`. `(−1,−1,0)`, `(−1,0,±1)`, `(0,−1,±1)`: 1; the other E2,
    `g` included, 0.
  - `12 → 13`: every E1 is −1. `(−1,−1,±1)`: 1; the other C3: 0. `e`: `G(0 + 1) − 0 = 0`.
  - `13 → 14`: `O`: `G(−6) + 2 = 0`. Every E2 is −1.
  - `14 → 15`: `(−1,−1,±1)`: `G(−3) − 1 = −2`.
  - `15 → 16`: their caps have sum −2: **leak at 16**.
- **Q4.**
  - `12 → 13`: `e`: `G(2) − y_{11}(e) = 1 − 1 = 0`.
  - `13 → 14`: `g`: `G(2 + 0) − y_{12}(g) = 0`, the NU9 value. The state is erased (L10).
  - At 16 and 22 the sums are 0. The first `u` is 26 (`g = −1`, `w_{26}(3) = −1`), so `e = −1`
    at 27.
  - `27 → 28`: `(2,0,0)`: `y_{27}(1,0,0) + y_{27}(e) = −1 − 1 = −2`: **leak at 28**.
- **Q5.**
  - `13 → 14`: `g`: `G(1) − y_{12}(g) = −1`.
  - `14 → 15`: `e`: `G(−1 + w_{14}(3)) − y_{13}(e) = G(−2) + 1 = 0`.
  - `15 → 16`: `g`: `G(−2 + 0) + 1 = 0`. `r_3`: `G(0 + w_{15}(4)) − w_{14}(3) = 1`, free.
  - `16 → 17`: the neighbours of `g` are free. `e`: `G(0 + 1) − 0 = 0`.
  - `17 → 18`: `g`: `G(−2) − 0 = −1`.
  - `18 → 19`: every cube site takes its NU9 value (phase 9: 0). `e`: `G(−1 + w_{18}(3)) − 0 = −1`.
  - `19 → 20`: `O = 2`. `g`: `G(−1) + 1 = 1`. `r_3`: `G(−1 + w_{19}(4)) − w_{18}(3) = G(−2) + 1 = 0`.
  - `20 → 21`: every E1 is 1. `e`: `G(1 + 0) + 1 = 1`.
  - `21 → 22`: `(2,0,0)`: `1 + 1 = 2`: **leak at 22**.
- **Q6.**
  - `15 → 16`: `g = 0`.
  - `16 → 17`: everything is free.
  - `17 → 18`: the free O-event at `(2,0,0)`, `−1 − 1`: **leak at 18**.

Every value lies in `{−2, …, 3}` (`O = 3` in P6 and Q3).

### 5.3 Placement `H00` (end next to the face centre `(1,0,0)`)

- `e = (2,0,0)`, active at even `t`.
- `g = (1,0,0)` (E1), active at odd `t`.
- Coupling sites: all four transverse neighbours `(2,±1,0)` and `(2,0,±1)`, with cube neighbours
  the E2 sites `(1,±1,0)` and `(1,0,±1)`. `e` has no cap.
- Breather sum at `g` (even `t`): `S_b(g) = O + 4·E2`, which is `2, 4, 0, −4, −2` at phases 0, 2, 4,
  6, 8.

**Free values.** f-cycle:
- `w_t(2) = (−1)^{(t+2)/2}`, which at `t = 0, 2, …, 18` is `−, +, −, +, −, +, −, +, −, +`;
- `w_t(3) = (−1)^{(t+3)/2}`, which at `t = 1, 3, …, 19` is `+, −, +, −, +, −, +, −, +, −`.

g-cycle: `w_t(2)` is the same, and `w_t(3)` has the opposite sign.

**Events (f-cycle).**
- *O at the coupling sites:* the sums at `t = 2, 6, 12, 16` are `1+1, −1+1, 1−1, −1−1`, so
  O-events occur at 2 and 16.
- *I at `g`* (even `t`): the sums at `t = 0, 2, 6, 8, 10, 12, 16, 18` are
  `1, 5, −3, −3, 3, 3, −5, −1`. Against `G(S_b) = 1, 1, −1, −1, 1, 1, −1, −1`, I-events occur at 0,
  2, 16 and 18.
- *I at `e`* (odd `t`): the sums at `t = 1, 7, 11, 17` are `1+1, −1−1, 1−1, −1+1`, so I-events
  occur at 1 and 7.

| `τ₀` | first event | outcome |
|---|---|---|
| 19, 0 | 0 (I at `g`) | H1: leak at 8 |
| 1 | 1 (I at `e`) | H2: leak at 3 |
| 2 | 2 (O) | leak at 3 |
| 3–7 | 7 (I at `e`) | H3: leak at 9 |
| 8–16 | 16 (O) | leak at 17 |
| 17, 18 | 18 (I at `g`) | H4: leak at 28 |

- **H1.**
  - `0 → 1`: `g`: `G(1) − 0 = 0` (free 1).
  - `1 → 2`: `O`: `G(5) − 2 = 0`, free. The E2 sites `(1,·)` adjacent to `g` read 1, so 0
    (free 1). The other E2 read 2, so 1. `e` reads `0 + w_1(3) = 1`, so free.
  - `2 → 3`: `g`: `G(0 + 0 + 1) − 0 = 0`, free. The other E1 read 4 or 3, so 0, free. The C3 sites
    `(1,±1,±1)` read 1, so 0 (free 1); `(−1,±1,±1)` read 3, so 1.
  - `3 → 4`: `(0,±1,±1)`: C3 neighbours `0` and `1`, so `G(1) − 1 = −1`. Every other E2 is 0, free.
    `e` reads `0 + w_3(3) = −1`, so free.
  - `4 → 5`: `(0,±1,0)` and `(0,0,±1)`: two E2 neighbours −1, so −1. `g` reads
    `0 + 0 + y_4(e) = −1`, so 0, free. `(−1,0,0)`: 0. `(−1,±1,±1)`: `G(−1) − 1 = −1`, free;
    `(1,±1,±1)`: 0.
  - `5 → 6`: `O`: `G(−4) − 0 = −1`. `(−1,±1,0)` and `(−1,0,±1)`: `G(−3) = −1`. `(0,±1,±1)`:
    `G(−3) + 1 = 0`. `(1,·)`: `G(−1) = 0`. `e` reads `0 + w_5(3) = 1`, so free.
  - `6 → 7`: `(−1,0,0)`: `G(−1 − 4) − 0 = G(−5) = −2`.
  - `7 → 8`: the cap `(−2,0,0)` of `(−1,0,0)` has sum −2: **leak at 8**.
- **H2.** `1 → 2`: `e`: `G(2) − y_0(e) = 1 + 1 = 2`. Then `(2,±1,0)` has sum `1 + 2 = 3`:
  **leak at 3**.
- **H3.** `7 → 8`: `e`: `G(−2) − y_6(e) = −1 − 1 = −2`. Then `(2,±1,0)` has sum `0 − 2`:
  **leak at 9**.
- **H4.**
  - `18 → 19`: `g`: `G(−1) + 1 = 1` (free 0).
  - `19 → 20`: `O = 2` and the E2 are 0, both free. `e` reads `1 + w_{19}(3) = 0`, so free.
  - `20 → 21`: `g`: `G(2 + 0 − 1) − 1 = −1`. The other E1: 1.
  - `21 → 22`: `O`: `G(4) − 2 = −1`. `(1,·)` E2: 0; the other E2: 1. `e` reads `−1 + w_{21}(3) = 0`,
    so free.
  - `22 → 23`: `g`: `G(−1 + 0 + 1) + 1 = 1`. The other E1: 0. `(1,±1,±1)`: 0; `(−1,±1,±1)`: 1.
  - `23 → 24`: `O`: `G(1) + 1 = 1`. `(0,±1,±1)`: `G(1) − 1 = −1`; the other E2: 0. `e` reads
    `1 + w_{23}(3) = 0`, so free.
  - `24 → 25`: `g`: `G(1 + 0 − 1) − 1 = −1`. The other E1: 0. `(−1,±1,±1)`: `G(−1) − 1 = −1`;
    `(1,±1,±1)`: 0.
  - `25 → 26`: `O`: `G(−1) − 1 = −1`. `(−1,±1,0)` and `(−1,0,±1)`: `G(−2) = −1`. `(0,±1,±1)`:
    `G(−1) + 1 = 1`. `(1,·)`: 0. `e` reads `−1 + w_{25}(3) = 0`, so free.
  - `26 → 27`: `(−1,0,0)`: `G(−1 − 4) − 0 = −2`.
  - `27 → 28`: the cap `(−2,0,0)` has sum −2: **leak at 28**.

**Events (g-cycle).** O-events at 2 and 16, and I-events at `g` at 0, 2, 16, 18, as before (they use
`w(2)` only). I at `e`: the sums at `t = 1, 7, 11, 17` are `1−1, −1+1, 1+1, −1−1`, so I-events occur
at 11 and 17.

| `τ₀` | outcome |
|---|---|
| 19, 0 | K1: leak at 8 |
| 1, 2 | leak at 3 |
| 3–11 | K2: no leak through tick 30 (§6) |
| 12–16 | leak at 17 |
| 17 | K3: leak at 33 |
| 18 | K4: leak at 28 |

- **K1.** The same as H1. The cube does not read `r_3`, and `e` reads `0 ± 1` at 1, 3 and 5, so it
  stays free. **Leak at 8.**
- **K3.**
  - `17 → 18`: `e`: `G(−2) − y_{16}(e) = −1 + 1 = 0`.
  - `18 → 19`: `g`: `G(−2 + 0) + 1 = 0`, the NU9 value. The state is erased (L10).
  - At 21 and 27 the sums are 0. The first `u` is 31 (`g = +1`, `w_{31}(3) = +1`), so `e = 1` at 32.
  - `32 → 33`: `(2,±1,0)`: `1 + 1 = 2`: **leak at 33**.
- **K4.**
  - `18 → 19`: `g = 1`, as in H4.
  - `19 → 20`: `e`: `G(1 + w_{19}(3)) − y_{18}(e) = G(2) − 1 = 0` (free −1).
  - `20 → 21`: `g`: `G(2 + 0 + 0) − 1 = 0`. Tick 21 is NU9 phase 1 with `g = 0` and `e` erased.
  - The cube at `(20, 21)` equals H1's at `(0, 1)`, and it runs as in H1. `g`'s sums differ from
    H1's only by `e`'s value (0 here, `±1` there), and `G` is the same: 0 at 22 and at 24. `e`
    reads `0 + w_{21}(3) = −1`, `0 + w_{23}(3) = 1` and `0 + w_{25}(3) = −1`, and stays 0.
  - `26 → 27`: `(−1,0,0)`: `G(−5) = −2`.
  - `27 → 28`: its cap `(−2,0,0)` has sum −2: **leak at 28**.

In every f-branch the piece sites `r_x`, `x ≥ 3`, keep their free values up to the leak, and `e`
keeps its free value up to the tick before it.

***

## 6. Theorem H

**Theorem H [W, (N), conditional on A-NU9].** Let the gadget be the bare breather and one matched
W2 piece `P = {(x, a, b) : 2 ≤ x ≤ x₁}`, `x₁ ≥ 3` or `x₁ = ∞`, with `(a, b) ∈ {(0,0), (1,0), (1,1)}`,
at a uniform background `c` with `3 ≤ c ≤ q − 4`. Then:
- (a) every f-cycle start leaks, within 12 ticks (§5, f-tables; the longest are F1, 12 ticks, and
  H4, 11);
- (b) no initial state of the 40 has an admissible no-input orbit;
- (c) for `x₁ = ∞`, every g-cycle start of `H11` and `H10` leaks, within 23 ticks. Every g-cycle
  start of `H00` leaks within 16 ticks, except `τ₀ ∈ {3, …, 11}`.

*Proof.*
- (a) For a ray, this is §5's f-tables and branches. For a segment with `x₁ ≥ 3`, apply L7 with
  `P̂` the ray and `e = r_{x₁}`. In every f-branch, `r_x` for `x ≥ 3` keeps its free value up to
  the leak, and `r_2 = e` up to the tick before it. So `e⁻`, `e`, `e⁺` are free at every tick
  `≤ T − 2`. Every leak site of §5 has first coordinate ≤ 2, so it is not adjacent to `P̂ ∖ P`.
- (b) The f-cycle states have no admissible orbit by (a). The g-cycle states have none by L8 and
  (a), for rays and segments alike.
- (c) This is §5's g-tables and branches.
- Values: every value before a leak lies in `{−2, …, 3}`, so RZ equals Q in this window
  (U1 Lemma 2.1). ∎

**Proposition K2 (observation) [W, (N), conditional on A-NU9].** For `H00` with a ray, the g-cycle
starts `τ₀ ∈ {3, …, 11}` do not leak through tick 30.

*Derivation.* Write `W(x, t)` for the g-cycle values:
- `W(2, t) = (−1)^{(t+2)/2}`;
- `W(3, t) = −(−1)^{(t+3)/2}`;
- in general `W(x, t) = (−1)^x (−1)^{(x+t)/2}`.

The first event is at 11: `e` reads `1 + 1 = 2`, so `y_{12}(e) = 1 − 1 = 0`. By L10 the state is
erased from `(12, 13)` (`g` is the NU9 value at 13). The first `u ≥ 13` is 17 (`g = −1`,
`W(3, 17) = −1`), so `y_{18}(e) = −1`. From there, `e` and `r_x` update by the line rule, with `e`
reading `y(g) + y(r_3)`:

| `t` | `e` | `r_3` | `r_4` | `r_5` | `r_6` | `r_7` | `r_8` |
|---|---|---|---|---|---|---|---|
| 18 | **−1** | · | −1 | · | 1 | · | −1 |
| 19 | · | **0** | · | −1 | · | 1 | · |
| 20 | **1** | · | 1 | · | −1 | · | 1 |
| 21 | · | **1** | · | 1 | · | −1 | · |
| 22 | **0** | · | **0** | · | 1 | · | −1 |
| 23 | · | **−1** | · | −1 | · | 1 | · |
| 24 | **0** | · | **−1** | · | −1 | · | 1 |
| 25 | · | **1** | · | **0** | · | −1 | · |
| 26 | **0** | · | **1** | · | 1 | · | −1 |
| 27 | · | **−1** | · | **1** | · | 1 | · |
| 28 | −1 | · | **−1** | · | **0** | · | 1 |
| 29 | · | **0** | · | **−1** | · | −1 | · |
| 30 | 1 | · | **1** | · | **−1** | · | −1 |

Bold entries differ from `W`; `·` is an inactive slot (0).

Each entry is `G(sum of its two line neighbours at the previous tick) − (its value two ticks
earlier)`. For `e`, the sum is `y(g) + y(r_3)`. At the odd ticks 19, 21, …, 29, `g` takes
`0, 1, 0, 0, −1, 0`.

The checks are:
- *Cube.* `g`'s sums are `S_b + y(e) = −3, 3, 4, 0, −4, −3, 3` at 18, 20, …, 30. Each gives
  `G(S_b)`, so the cube is NU9 throughout.
- *Coupling sites.* An E2 value plus `y(e)`: `+1 + 0` at 22, `−1 + 0` at 26, and `|y(e)| ≤ 1` with
  E2 = 0 at the other even ticks.
- *Caps.* Every piece value is ternary.

So no outside site leaves `c` through tick 30.

**Skepticism (§A.31).**
- *What it is not.* This is the only branch in which no leak is found by its stop tick. It is not
  an admissible no-input orbit: by L8 its two-sided orbit leaks at some tick before `τ₀`, so it is
  not periodic.
- *What the table shows.* At tick 30 the piece differs from `W` at `r_3`–`r_6`, a disturbance moving
  away from the cube. At `(29, 30)` the values of `e`, `r_3`, …, `r_6` equal those at `(19, 20)`,
  while `W` has changed sign. Relative to the sign-reversed background, the pattern near the cube
  therefore repeats after 10 ticks.
- *What it does not show.* Whether this continues, whether the disturbance is a W2 signal, and
  whether the forward orbit leaks later are not derived. The sites beyond `r_6` influence the
  pattern near the cube within a few ticks, so no extrapolation is made.

***

## 7. Excluded class, necessary conditions and what is not shown

**Corollary R1 (one piece) [conditional on A-NU9].** Let the gadget be the bare breather and one
straight W2 piece, disjoint from the cube, with an end next to it. Suppose it is not alongside at
distance 1 and is not a single site. Then it has no admissible no-input orbit, or it is independent
of the breather:
- unmatched: L3(a);
- distance 2: T-IND′;
- head-on at distance 1: Theorem H(b).

Hence it realizes no controlled turn and no signal interaction. This holds for rays and for
segments of at least two sites, at every phase and background, for `3 ≤ c ≤ q − 4`.

**Corollary R2 (several pieces, no direct contact) [conditional on A-NU9].** Let the gadget be the
bare breather and finitely many W2 pieces (lines, rays, segments), pairwise disjoint and
non-adjacent, none adjacent to the cube. Suppose some coupling site of the cube touches exactly one
matched piece. Then every initial state leaks within 20 ticks (T-IND′). This contains the thick
analogue of PT's J2: an input arm and an output arm that end at distance 2 from the cube, on the same
or different faces, without touching each other.

**Corollary R3 (long alongside pieces) [conditional on A-NU9].** R5's leaks at the full-line
placements `(2,0)` and `(2,1)` persist for a piece `{(x, 2, b) : x₀ ≤ x ≤ x₁}`, `b ∈ {0, 1}`, with
`x₀ ≤ −6` and `x₁ ≥ 6`, for all 40 starts.
*Proof.*
- R5 §5 leaks every start of the full line within 6 ticks (f-type directly, g-type by the line's
  mirror).
- Events occur only at contact sites (L5(a)). A site departs at `t + 1` only if a site of its
  closed neighbourhood departed at `t`, or the site itself departed at `t − 1`. So a line site
  `(x, 2, b)` that departs at `τ₀ + k` has `|x| ≤ k`.
- Up to `T − 2 ≤ τ₀ + 4`, the departed line sites have `|x| ≤ 4`. L7 then applies at both ends, and
  R5's leak sites have `|x| ≤ 2`. ∎

Alongside pieces with an end at `|x| ≤ 5` are not covered (§8).

**Excluded class, in one statement.** Conditional on A-NU9, at a uniform background `c` with
`3 ≤ c ≤ q − 4`, any `q ≥ 7`, W2 pieces as defined in §1 and the W2 signal:
- (i) the bare NU9 breather plus one straight W2 ray or segment of at least two sites, either
  head-on at ℓ1-distance 1 or at ℓ1-distance 2 in any placement, has no admissible no-input orbit,
  and so no controlled turn and no signal interaction;
- (ii) the bare breather plus finitely many W2 pieces with no direct contact and one exclusive
  coupling site leaks from every initial state.

**Necessary geometric conditions (any gadget; conditional on A-NU9 where NU9 is named).** For an
admissible no-input orbit of a gadget with W2 pieces:
- (N1) at every corner contact (L4) and every end contact (L9) with a W2 piece site that keeps its
  free value, the contact gadget site is sign-locked to period 4 at the piece's active ticks. A
  gadget site carrying a nonzero value with period ≡ 2 (mod 4), such as an NU9 boundary site, cannot
  sit at such a contact for 20 ticks with the piece undisturbed;
- (N2) consequently, in a bare-breather gadget, some contact must have its piece site depart from
  W2 in the no-input orbit, or the cube must depart from NU9;
- (N3) without a direct contact, and with a coupling site exclusive to one matched piece, such a
  departure first appears at a coupling site, which is a leak (R2). So an admissible bare-breather
  gadget needs a direct contact (a piece at distance 1 from the cube or adjacent to another piece),
  or no coupling site exclusive to one matched piece;
- (N4) one head-on piece alone does not suffice (Theorem H).

These are conditions on candidate designs. Meeting them would not establish a controlled turn, and
a controlled turn would not establish that R_q is universal in Definition U, which also needs gates,
fan-out, composition and an encoding with a correctness proof (U1 §3).

**What the mechanism is.** Every leak traces to the period mismatch of R5's AW-NU-5, NU9's period 10
against W2's negation over 10 ticks, acting at one of three kinds of site:
- a coupling site: T-IND′, the O-events;
- an end, which is driven to `±2` and leaks through its cap or a coupling site (F1, F2, P3, P5, H2,
  H3), is driven to the sign opposite its free value (G1), or is erased and driven back (L10: G2,
  Q2, Q4, K3);
- the cube, which is driven off NU9 at `g` until a boundary site reaches `±2` (H1, H4, K1, K4, P6,
  Q3), or until a free O-event is reached (P1, P2, P4, Q1, Q5, Q6).

***

## 8. Established / Assumed / Missing; (N)/(I)

| Result | Label | Status | ESTABLISHED | ASSUMED (where it enters) | MISSING |
|---|---|---|---|---|---|
| L6 | (N) | writer's; elementary | as stated | U1 Lemma 2.2, MQ1 (`main`) | — |
| L7 (truncation) | (N) | writer's | as stated | L6; no leak up to `T − 1` | — |
| L8 (time reversal) | (N) | writer's | orbits, leaks, periods; f ↔ g for head-on pieces | NU9's symmetry (R4) for the breather part | — |
| L9 (end locking) | (N) | writer's | for any gadget site at an end with two allowed neighbours | L1 (R5); (W) by L6 | — |
| L10 (erased end) | (N) | writer's; conditional on A-NU9 | as stated, `u ≤ s + 19` | NU9 (R4; hand re-derived; exact re-run pending); L5 (R5) | — |
| T-IND′ | (N) | writer's; conditional on A-NU9 | R5's T-IND for pieces | T-IND (R5, reviewed); L6; NU9 | arrangements in which every coupling site is shared |
| Theorem H (a), (b) | (N) | writer's hand derivation; conditional on A-NU9 | 60 f-starts followed to a leak (3 placements × 20); 60 g-states inadmissible; segments `x₁ ≥ 3` | NU9; L2, L5 (R5); L7, L8 | an exact re-run (a computation; not authorized, not run) |
| Theorem H (c) | (N) | writer's hand derivation; conditional on A-NU9 | 51 g-starts of rays followed to a leak | as above | the 9 `H00` starts of K2 beyond tick 30; g-forward for segments |
| Proposition K2 | (N) | writer's hand derivation; conditional on A-NU9 | no leak through tick 30; the table | as above | the orbit beyond tick 30 |
| Corollaries R1–R3 | (N) | writer's; conditional on A-NU9 | the class of §7 | as above; R5 §5 for R3 | everything below |

No quantum, operational or measurement assumption is used. The breather and the pieces are designed
initial patterns, a scope condition, not a claim about native preparation.

**MISSING (not excluded; mathematics unless stated):**
- alongside pieces at distance 1 that end next to the cube, and alongside pieces with an end at
  `|x| ≤ 5`;
- single-site segments next to the cube, and segments filled other than by a W2 restriction
  (U1 E6 trits);
- two or more pieces with at least one direct contact, to the cube or to each other. This includes
  the thick analogue of PT's J1, whose arms are adjacent, and an input arm head-on with any output
  arm;
- arrangements in which every coupling site is shared between matched pieces;
- the forward orbit of the K2 starts beyond tick 30: whether it leaks, and whether the disturbance
  it sends along the ray is a W2 signal;
- allowed regions larger than the cube (absorbers, spacers, period converters), non-W2 pieces and
  signals, non-uniform backgrounds and other breathers;
- the exact re-run of NU9 (NU9-CHECK), on which every NU9 result here is conditional (a
  computation; not authorized);
- whether R_q is universal in Definition U: not addressed.

***

## 9. Productivity, classification, skepticism

**Productivity (PLAN test).**
- (ii) is met: Corollaries R1–R2 exclude a stated class of NU9 gadgets with rays and segments. No
  earlier record excludes it: R5's class has full lines only, and PT's class is planar.
- (iii) is met, at a smaller scale. L9 holds for every gadget site at a W2 piece end, and is not
  contained in R5's L1–L5, which concern outside sites. L7 and L8 are general tools.
- (i) is not met: no gadget is found.

| Item | Class (§A.31) |
|---|---|
| Theorem H, R1, R2 (bare breather + rays/segments) | NEW (negative, scoped) |
| L9 (end locking) | NEW, minor (R5's L4 transferred to an allowed site); an assumption-watch for every design with piece ends |
| L10 (erased end) | NEW, minor; explains four branches by one mechanism |
| Proposition K2 | NEW (observation, scope stated): a forward orbit with no leak through 30 ticks and a disturbance moving out along the ray |
| T-IND′, R3 | ELABORATING (R5 for pieces) |
| L6, L7, L8 | CONFIRMING (elementary; U1 E6, MQ's backward form) |

**Skepticism (§A.31).** The checks target the ways the result could be wrong in either direction.
1. *Completeness of the placements.* Every axis piece reduces to `e₁` with `a ≥ b ≥ 0` by
   symmetries that fix NU9. A head-on ray reduces to `x ≥ 2` by `x ↦ −x`. §3 lists every case with
   an end within distance 2.
2. *Completeness of the phases.* Each placement has 10 × 4 matched initial states, the two 20-tick
   cycles of §1. Every start of the f-cycle is treated forward, and every start of the g-cycle is
   treated by L8, and forward for rays (§5).
3. *Completeness of the event tables.* The contact and coupling sites are listed from the neighbours
   of `e` (§5, geometry). No site with first coordinate ≥ 3 is adjacent to the cube.
4. *Branches.* The decisive sum in each branch is written out. A slip in a branch could change that
   start's outcome. The branches most exposed are the long ones: P6, Q3, H1, H4, K4 and the K2
   table. Each is for the reviewer to recheck.
5. *Favourable branch.* K2 is the only branch without a leak by its stop tick. Its standing is
   stated without extrapolation, and its exclusion from admissibility rests on L8, not on the table.
6. *Time reversal.* L8 is used only for admissibility, a two-sided property. It is not used to
   claim a forward leak.
7. *Countercontrols on paper.* Under the constant rule `F ≡ 2c` (P3-K1) no outside site ever moves,
   so none of the leaks of §4–5 occurs. For an unmatched piece, L3(a) gives no coupling. Both
   confirm that the leaks use `G`'s rounding and the shared component. L8 applied to NU9 alone
   returns NU9 (its symmetry `y_s = −y_{8−s}`), a consistency check of the reversal map.
8. *Window.* Every value in §5–6 before a leak lies in `{−2, …, 3}`.

**An exact check (described, not preregistered, not run).** Run the 40 matched initial states of
each head-on placement, with a ray of length at least 80 (or a torus of side at least 90 along it),
to the first leak or tick 200. This would confirm §5's tables and decide the K2 starts. It is a
computation and needs separate authorization. It is not part of this round.

**Assumption-watch.** *AW-NU-6 (end locking).* A W2 piece end touching a gadget site behaves as a
coupling site inside the allowed region (L9). An undisturbed end forces period-4 sign locking at
its contact. A design that uses a piece end next to a period-≡ 2 (mod 4) orbit must state how the
end departs from W2 without leaking. In this class, the end is driven to `±2`, erased, or drives
the orbit off its cycle.

**Fixed point.** One pass, with NEW items; the §A.31 fixed point is not reached. Under PLAN's stop
rule the round stops here. The question is answered for the class of §7. The next classes (alongside
ends, direct-contact pairs, K2 beyond tick 30) need branch analyses beyond hand scale or a
computation.
