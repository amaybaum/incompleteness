# NATIVE-UNIV, round 5: the bare NU9 breather cannot be attached to a W2 line without leaking

**Standing.** Writer's research record, paper only. It follows `PLAN.md` (`8931f03`), committed
first. No computation was run, no script is added and no exact check was replayed. Every orbit
below is derived by hand, tick by tick, or follows from a stated lemma. Independent non-author
review at `17d81a3`: REVISE on status and scope
([#1549 c.7077076211](https://github.com/amaybaum/incompleteness/pull/1549#issuecomment-7077076211)).
The reviewer re-derived NU9, the event tables and all eight branches by hand, and the mathematics
holds. This revision answers R1, R2 and n1–n8. For n9: the A1 retirement ledger, re-read at the
ledger branch's head `c176d35`, still lists no `native-univ-*` path.

Inputs and their standing are listed in `PLAN.md`: `R4` (NU9), `PT` (PLANAR-TURN), `P2N` (NU3–NU6),
`F1` (NU1, NU2) are reviewed records not on `main`; `U1`, `U2` and `MQ` are on `main`.

**Layer.** Every statement concerns the configuration dynamics of Q. None concerns effects,
instruments, accessible algebras or readouts.

***

## 0. Summary

1. **Definitions (§1).** A *thick gadget* is a finite allowed set `K` with an interior site of
   `K ∪ lines`; the *bare breather* is `K` = the NU9 cube, carrying NU9 at some phase and nothing
   else. *Controlled turn* is PT's outcome T or T-STATEFUL (not R6-NULL); *signal interaction* is any
   leak-free signal orbit that is not the sum of the no-input orbit and the free signal. Both require
   a leak-free no-input orbit (U2 R1; PT excludes Q-LEAK).
2. **General lemmas (§2), (N).**
   - L1: in a leak-free run, every site outside the allowed region sees an allowed-neighbour sum in
     `{−1, 0, 1}` at every tick.
   - L4 (*period-4 locking*): if an outside site has exactly two allowed neighbours, a gadget site
     `g` and an undisturbed W2 line site `l`, then `y_t(g)·w_t(l) ≤ 0` at every tick. If `y(g)`
     repeats after `P ≡ 2 (mod 4)` ticks over a stretch where `l` is undisturbed, then `y(g) = 0`
     at every tick of that stretch at which `l` is active (every tick of it, when `g` lies in `l`'s
     component).
   - L5 (*first deviation*): for parts confined to pairwise non-adjacent closed sets, with the
     allowed region their union, the first departure from free superposition is a leak.
3. **Theorem T (§3–§5), (N), conditional on A-NU9.** The NU9 orbit is ASSUMED: it is hand
   re-derived (R4's review and this round's review), and its exact re-run NU9-CHECK is pending and
   not authorized. Given A-NU9, the proof below is a paper derivation. Let a bare NU9 breather and
   one straight W2 line be given, disjoint, at any placement and any relative phase, at a uniform
   background `c` with `3 ≤ c ≤ q − 4`. The allowed region is the cube plus the line. Then exactly
   one of the following holds:
   - (a) the line lies in the other parity component, or at ℓ1-distance ≥ 3 from the cube. Breather
     and line then evolve independently for all time, with or without a W2 signal. There is no
     interaction of any kind;
   - (b) the line is in the breather's component at ℓ1-distance 1 or 2. Then the no-input
     configuration leaks: some site outside the cube and the line leaves `c`, within 6 ticks at
     distance 1 and within 20 ticks at distance 2.

   Up to the cube's symmetry there are five placements in (b), each with 40 initial configurations;
   all 200 leak.
4. **Corollary (§6), conditional on A-NU9.** No bare-breather gadget with one W2 line realizes a
   leak-free signal interaction: not a write, a read, a delay or a reflection. No bare-breather
   gadget realizes a leak-free controlled turn or signal interaction when its lines are pairwise
   disjoint, none is adjacent to the cube or to another line, and some breather–line coupling site
   touches only one matched line. The mechanism is the period mismatch:
   - NU9 has period 10 ≡ 2 (mod 4);
   - a W2 line is negated after 10 ticks;
   - so every corner contact is driven to `|S| = 2` within 20 ticks, two breather periods (L4,
     T-IND).
5. **MISSING (§7).** Not settled:
   - two or more lines with at least one in direct contact;
   - lines through the cube;
   - allowed regions larger than the cube (absorbers, spacers, period converters);
   - non-W2 signals and other backgrounds;
   - other breathers.

   No claim is made that R_q is non-universal.
6. **Productivity (§8):** gem by (ii), for the class of item 3, and by (iii), for L4 and L5.

***

## 1. Definitions

Notation as in R4 §1: RZ, `y = x − c`, `y_{t+1}(i) = G(S_t(i)) − y_{t−1}(i)` with
`G(s) = ⌊(s+1)/3⌋` and `S_t(i)` the sum over the six neighbours. `p(i) = i₁ + i₂ + i₃ mod 2`. By
NU1 the slots `(i, t)` with `p(i) + t` even form one component, those with `p(i) + t` odd the
other, and the two evolve independently. Every configuration below lies in one component, so a
slot of the other component is 0 and stays 0.

**NU9 (R4).** On the cube `C = {−1,0,1}³`, with the site classes `O, E1, E2, C3` of R4, the orbit at
phase `t mod 10`:

| phase | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|---|
| `y` | `2·1_O` | `1_{E1}` | `1_{E2}` | `1_{C3}` | 0 | `−1_{C3}` | `−1_{E2}` | `−1_{E1}` | `−2·1_O` | 0 |

The cube is closed, and its boundary layer `C ∖ O` stays in `{−1, 0, 1}` (R4 §2 item 2). Each class
is nonzero at two phases per period: `O` at 0, 8; `E1` at 1, 7; `E2` at 2, 6; `C3` at 3, 5.

**W2 line.** `ℓ(a, b) = {(x, a, b) : x ∈ ℤ}` and its images under axis permutations. A *W2
background* on a line (U1 E2) is a configuration on the line, zero off it, whose current slice is
`±(−1)^k` at the `k`-th site of one parity class along the line, and whose previous slice is
`±(−1)^k` at the `k`-th site of the other. Every line site then has line-neighbour sum 0, so
`y_{t+1} = −y_{t−1}` on the line: the background has period 4, and
```text
w_{t+2}(l) = −w_t(l),   w_{t+10}(l) = −w_t(l),                                  (W)
```
for every line site `l`, with `w_t(l) ∈ {±1}` at every tick at which `l`'s slot lies in the line's
component. A line is *matched* to a breather when its nonzero slots lie in the breather's component.
For a matched line, fixing the breather's phase leaves four backgrounds, one sign for each slice.
In the free cycles of §4 the backgrounds are, with the breather at phase `t mod 10`:
- *f-type:* `w_t(x) = (−1)^{(x+t+κ)/2}` on the sites with `x + t + κ` even;
- *g-type:* `(−1)^t` times the f-type.

Here `κ` is fixed by the placement. The other sign of each type is the same free cycle shifted by
10 ticks, by (W). The mirror image of the f-type under `x ↦ −x`, which fixes the cube and the line,
is `(−1)^κ` times the g-type. So it is the g-type when `κ` is even, and the g-type shifted by 10
ticks when `κ` is odd, as at placement `(2,1)`. Either way the g-type free cycle is the mirror of
the f-type free cycle, which is what §3 uses.

**W2 signal.** U2 K0's defect, launched at distance ≥ 8 on a line toward the gadget (U2 §1, PT §1).
It is ternary at every tick.

**Definition (thick gadget).** A *gadget* is a finite set `K ⊂ ℤ³` with initial two-slice values,
together with finitely many W2 lines, disjoint from `K`. Its *allowed region* is
`A = K ∪ lines`. The gadget is *thick* when `A` has an interior site, one whose six neighbours all
lie in `A`. A gadget is *built around NU9* when `K` contains a 3 × 3 × 3 cube (a translate of `C`)
carrying NU9 at some phase.
It is the *bare breather* when `K` is exactly that cube, with every other site of `K` absent.
Every gadget built around NU9 is thick, since the cube's centre is interior. A planar `A` has no
interior site, so PT's class contains no thick gadget.

**Definition (leak).** A run *leaks* at tick `t` when some site outside `A` differs from `c` at `t`
(PT §1, U2 R3). A *no-input leak* is PT's Q-LEAK.

**Definition (controlled turn).** PT §2's outcome T or T-STATEFUL, not R6-NULL, for a signal
entering on line `A_1` and leaving on a line `B` not collinear with it. This is U2's R1–R6 in PT's
exact form. Here every line is a full straight line `ℓ(a, b)`. PT's geometries J1 and J2 use rays
that end at the junction instead; a gadget with rays or finite segments is outside this record's
class (§7). It requires a no-input orbit that does not leak (R1) and does not emit along a line
(Q-EMIT).

**Definition (signal interaction).** Let the no-input orbit `N` not leak, and let `F` be the
signal's free orbit on its line with no gadget present. A *signal interaction* is a signal orbit
`S` that does not leak and differs at some tick from `N + (F − background)`. It covers a signal that
is delayed, reflected, absorbed or changed in sign or type, and a gadget left in another no-input
orbit or another phase, that is, a write. A controlled turn is a signal interaction. Both need a
no-input orbit that does not leak.

**Relation to Definition U.** Turns and signal interactions are building blocks, as in U1 §3.
Definition U needs, beyond them, gates, fan-out, composition and an encoding with a correctness
proof. A negative result here concerns the stated gadget class only.

***

## 2. General lemmas (any gadget, any `K`)

**L1 (outside sums) [W, (N)].** In a run that does not leak, every site `o ∉ A` has
`Σ_{j ∈ N(o) ∩ A} y_t(j) ∈ {−1, 0, 1}` at every tick.
*Proof.* `y_{t−1}(o) = y_{t+1}(o) = 0` and `y_{t+1}(o) = G(S_t(o)) − y_{t−1}(o)`, so
`G(S_t(o)) = 0`, and `G(s) = 0` iff `|s| ≤ 1`. The neighbours of `o` outside `A` are 0. ∎
*Consequence.* A site of `A` that is the only `A`-neighbour of some outside site is ternary at every
tick. This is NU6(b) for an allowed region that is not closed. The extension rests on MQ1's converse
(ELABORATING).

**L2 (rounding windows) [W, (N)].** `G(s) = k` for `s ∈ {3k − 1, 3k, 3k + 1}`. So `G(s + δ) = G(s)`
for all `δ ∈ {−1, 0, 1}` iff `s ≡ 0 (mod 3)`. For `s = 3k + 1`, only `δ = +1` changes `G`; for
`s = 3k − 1`, only `δ = −1`.
*Proof.* `⌊(3k)/3⌋ = ⌊(3k+1)/3⌋ = ⌊(3k+2)/3⌋ = k`. ∎

**L3 (components and separation) [W, (N)].**
- (a) A line in the other component from `K`'s configuration evolves independently of it, with or
  without a signal, by NU1.
- (b) A matched line at ℓ1-distance ≥ 3 from a closed set `D ⊃ K` also evolves independently of it,
  provided `∂D` stays in `[c−1, c+1]` and the line stays ternary. This is MQ2(b): the line is
  closed, and a W2 line with a W2 signal is ternary at every tick.

**L4 (period-4 locking) [W, (N)].** In a run that does not leak, let `o ∉ A` have exactly two
`A`-neighbours, `g ∈ K` and a line site `l`, and let `l` carry its W2 background value `w_t(l)` at
tick `t`. Then `y_t(g)·w_t(l) ≤ 0` and `|y_t(g)| ≤ 2`.
- (a) At every tick at which `l`'s slot is active and `l` is undisturbed, the sign of `y_t(g)` is
  0 or `−w_t(l)`. Over such ticks it has period 4, up to zeros.
- (b) If moreover `y_{t+P}(g) = y_t(g)` with `P ≡ 2 (mod 4)`, and `l` is undisturbed and active at
  `t` and `t + P`, then `y_t(g) = 0`.

*Proof.* By L1, `|y_t(g) + w_t(l)| ≤ 1`, with `w_t(l) = ±1` when `l`'s slot is active and 0
otherwise. This gives both inequalities. (b): `P` is even, so `l` is active at `t + P` when it is
active at `t`, and by (W), `w_{t+P}(l) = (−1)^{P/2} w_t(l) = −w_t(l)`. So `y_t(g) w_t(l) ≤ 0` and
`−y_t(g) w_t(l) ≤ 0`, which gives `y_t(g) w_t(l) = 0` and hence `y_t(g) = 0`. ∎ When `g`'s
configuration lies in `l`'s component, which is the case in §3–5, `g`'s slot is active exactly when
`l`'s is.

*Reading.* At the ticks where `l` is active, a gadget site at a corner contact with an undisturbed
W2 line cannot carry any nonzero value that recurs after 2, 6, 10, … ticks. NU9's sites recur
after 10.

**L5 (first deviation is a leak) [W, (N)].** Let `X¹, …, Xⁿ` be orbits, each confined alone to a
closed set `D_k` (support in `D_k` at every tick, `∂D_k` in range), with the `D_k` pairwise
disjoint. Let `Y = c + Σ_k y^k` be their *free superposition*, and suppose the true orbit `y` equals
`Y` at `t − 1` and `t`.
- (a) Then `y_{t+1}(i) = Y_{t+1}(i)` at every site `i` except possibly the following:
  - *coupling sites:* sites outside every `D_k` with neighbours in two or more `D_k`;
  - *contact sites:* sites of some `D_k` with a neighbour in another `D_j`.
- (b) If no site of one `D_k` is adjacent to a site of another, there are no contact sites. If, in
  addition, the allowed region is `∪ D_k`, then the first tick at which `y` departs from `Y` is a
  leak. It occurs at a coupling site `o` with `|Σ_k S^k_t(o)| ≥ 2`.

*Proof.* (a) At any other site `i`, at most one `D_k` meets `N(i) ∪ {i}`. So `S_t(i) = S^k_t(i)`,
`y_{t−1}(i) = y^k_{t−1}(i)`, and the update gives `y^k_{t+1}(i)`. Every `y^j` with `j ≠ k` is 0 at
`i` at `t + 1`, since `i ∉ D_j` and `X^j` is confined. (b) A coupling site `o` has at most one
neighbour in each closed `D_k`. Each `X^k` alone keeps `o` at `c`, so `|S^k_t(o)| ≤ 1`. The true
value is `G(Σ_k S^k_t(o)) − 0`, which differs from 0 iff `|Σ_k S^k_t(o)| ≥ 2`. Such an `o` is
outside the allowed region. ∎

***

## 3. Placements of one line

By the cube's symmetry group, which fixes NU9 (its values depend on the site class only) and maps
W2 lines to W2 lines, every axis line reduces to `ℓ(a, b)` along `e₁` with `a ≥ b ≥ 0`. Its
ℓ1-distance from `C` is `δ(a,b) = max(a−1, 0) + max(b−1, 0)`.

| `δ` | placements `(a, b)` | case |
|---|---|---|
| 0 | `(0,0), (1,0), (1,1)` | the line meets the cube: not a disjoint gadget; outside the class (§7) |
| 1 | `(2,0), (2,1)` | *direct contact*: some line site is adjacent to a cube site (§5) |
| 2 | `(3,0), (3,1), (2,2)` | *indirect contact*: coupling sites only (§4) |
| ≥ 3 | all others | L3(b): independent |

**Count.** For a matched line there are 10 breather phases and 4 backgrounds, so 40 initial
two-slice states per placement. The f-type states with both signs form one free cycle of 20 ticks:
the period is `lcm(10, 4) = 20`, and the two signs differ by a 10-tick shift by (W). The g-type
states form the mirror cycle. So it suffices to start the f-type free cycle `Y(t)` at each of its 20
ticks `τ₀`, taking `(Y(τ₀ − 1), Y(τ₀))` as the initial state, and to apply the mirror.

***

## 4. Indirect contact (`δ = 2`): every matched configuration leaks within 20 ticks

**Proposition T-IND [W, (N)].** Let a bare breather and W2 lines `ℓ_1, …, ℓ_m` be given, in either
component and at any distance. The cube and the lines are pairwise disjoint, and no site of one is
adjacent to a site of another. The allowed region is their union. Suppose some coupling site `o` is
adjacent to a cube site `g` and to a site `l` of a matched line, and to no site of any other matched
line. Then, from every initial phase, the configuration leaks within 20 ticks.

*Proof.* By L5(b), the orbit is the free superposition until the first leak. Every class of
`C ∖ O` is nonzero at some phase. Let `s` be such a phase for `g`, and let `t` be the tick in
`[τ₀, τ₀ + 9]` with breather phase `s`. Both `t` and `t + 10` lie in `[τ₀, τ₀ + 19]`. At `o` the
free sum is `y_t(g) + w_t(l)`: `o` has one neighbour in the closed cube and one on `l`'s line. A
neighbour of `o` on an unmatched line has the parity of `g` and is 0 at `t`, since its active slots
lie in the other component. `l`'s slot is active at `t`, since `g` and `l` have the same parity and the line is
matched. By (W), `w_{t+10}(l) = −w_t(l)`, while `y_{t+10}(g) = y_t(g) ≠ 0`. So at `t` or at `t + 10`
the sum has absolute value `|y_t(g)| + 1 ≥ 2`. If no leak has occurred earlier, the orbit is still
the free superposition there (L5(b)), and `o` leaves `c` one tick later. ∎

For one line, every `δ = 2` placement satisfies the hypothesis:

| `(a,b)` | coupling sites | cube neighbour, line neighbour |
|---|---|---|
| `(3,0)` | `(x,2,0)`, `|x| ≤ 1` | `(x,1,0)` (E1 or E2), `(x,3,0)` |
| `(3,1)` | `(x,2,1)`, `|x| ≤ 1` | `(x,1,1)` (E2 or C3), `(x,3,1)` |
| `(2,2)` | `(x,1,2)` and `(x,2,1)`, `|x| ≤ 1` | `(x,1,1)` (E2 or C3), `(x,2,2)` |

In each case the coupling site has no other non-background neighbour. So 3 × 40 = 120 configurations
leak.

*Values.* Up to the first leak, every value is that of NU9 or of a line, so `|y| ≤ 2`. RZ equals Q
there for `2 ≤ c ≤ q − 3` (U1 Lemma 2.1).

***

## 5. Direct contact (`δ = 1`): every matched configuration leaks within 6 ticks

Here L5(a) allows deviations at contact sites, so each start is followed tick by tick. In each
geometry:
1. The contact sites and the coupling sites are listed.
2. The free cycle's *events* are tabulated. An event at tick `t` is a site at which one step from
   `(Y(t−1), Y(t))` departs from `Y(t+1)`. It is an I-event at a contact site, or an O-event at a
   coupling site.
3. Every start whose first event includes an O-event leaks one tick later, since all sites are free
   up to that tick.
4. The other starts are followed tick by tick.

**Line sites never deviate in the free cycle.** A line site's line-neighbour sum is 0, and its cube
neighbour carries a value in `{−1, 0, 1}`. So `G = 0`, as on the free line.

### 5.1 Placement `(2, 0)`

The line is `(x, 2, 0)`. Its matched slots are those with `x ≡ t (mod 2)`. Free cycle:
`w_t(x) = (−1)^{(x+t)/2}`. The values used are:
- `w_t(0) = (−1)^{t/2}`;
- `w_t(1) = (−1)^{(t+1)/2}`;
- `w_t(−1) = −w_t(1)`;
- `w_t(±2) = −(−1)^{t/2}`.

**Contact sites.**
- `(0,1,0)` (E1), with line neighbour `(0,2,0)`.
- `(±1,1,0)` (E2), with line neighbour `(±1,2,0)`.

**Coupling sites.**
- `(0,2,±1)`: cube neighbour E2 `(0,1,±1)`, line neighbour `(0,2,0)`.
- `(±1,2,±1)`: cube neighbour C3 `(±1,1,±1)`, line neighbour `(±1,2,0)`.
- `(±2,1,0)`: cube neighbour E2 `(±1,1,0)`, line neighbour `(±2,2,0)`.

No other site has neighbours in both.

**I-events.** The breather sums, by phase:
- at E1: `S_b = 2, 4, −4, −2` at phases `0, 2, 6, 8`, and 0 otherwise;
- at E2: `S_b = 2, 2, −2, −2` at phases `1, 3, 5, 7`, and 0 otherwise.

By L2, a sum of 2 or −4 changes `G` under `w = −1`, and a sum of 4 or −2 changes it under `w = +1`.

| `t` | 0 | 2 | 6 | 8 | 10 | 12 | 16 | 18 |
|---|---|---|---|---|---|---|---|---|
| E1 `(0,1,0)`: `S_b`, `w`, `G(S_b+w)` vs `G(S_b)` | 2,+1: 1=1 | 4,−1: 1=1 | −4,−1: **−2≠−1** | −2,+1: **0≠−1** | 2,−1: **0≠1** | 4,+1: **2≠1** | −4,+1: −1=−1 | −2,−1: −1=−1 |

| `t` | 1 | 3 | 5 | 7 | 11 | 13 | 15 | 17 |
|---|---|---|---|---|---|---|---|---|
| `S_b` at E2 | 2 | 2 | −2 | −2 | 2 | 2 | −2 | −2 |
| `w_t(1)`, `w_t(−1)` | −1,+1 | +1,−1 | −1,+1 | +1,−1 | +1,−1 | −1,+1 | +1,−1 | −1,+1 |
| deviating E2 site | `(1,1,0)` | `(−1,1,0)` | `(−1,1,0)` | `(1,1,0)` | `(−1,1,0)` | `(1,1,0)` | `(1,1,0)` | `(−1,1,0)` |

At phases 9 (E2) and 4 (E1) the sum is 0, so there is no event. I-events occur at
`t ∈ {1, 3, 5, 6, 7, 8, 10, 11, 12, 13, 15, 17}`.

**O-events.** The sum at a coupling site is the cube value plus the line value.

| site | ticks with cube value ≠ 0 | free sums | O-events |
|---|---|---|---|
| `(0,2,±1)` | E2 at 2, 6, 12, 16 (`+,−,+,−`) | `1−1, −1−1, 1+1, −1+1` | 6, 12 |
| `(1,2,±1)` | C3 at 3, 5, 13, 15 (`+,−,+,−`) | `1+1, −1−1, 1−1, −1+1` | 3, 5 |
| `(−1,2,±1)` | the same | `1−1, −1+1, 1+1, −1−1` | 13, 15 |
| `(±2,1,0)` | E2 at 2, 6, 12, 16 | `1+1, −1+1, 1−1, −1−1` | 2, 16 |

**Starts.** The start is `τ₀`, and the leak is stated as (tick, site).

| `τ₀` | first event | outcome |
|---|---|---|
| 2 | 2 (O) | leak at 3, `(±2,1,0)` |
| 3 | 3 (I+O) | leak at 4, `(1,2,±1)` |
| 4, 5 | 5 (I+O) | leak at 6, `(1,2,±1)` |
| 6 | 6 (I+O) | leak at 7, `(0,2,±1)` |
| 12 | 12 (I+O) | leak at 13, `(0,2,±1)` |
| 13 | 13 (I+O) | leak at 14, `(−1,2,±1)` |
| 14, 15 | 15 (I+O) | leak at 16, `(−1,2,±1)` |
| 16 | 16 (O) | leak at 17, `(±2,1,0)` |
| 18, 19, 0, 1 | 1 (I) | branch B1: leak at 3 (of the next cycle), `(−2,1,0)` |
| 7 | 7 (I) | branch B2: leak at 11, `(−2,1,0)` |
| 8 | 8 (I) | branch B3: leak at 11, `(−2,1,0)` |
| 9, 10 | 10 (I) | branch B4: leak at 15, `(−2,1,0)` |
| 11 | 11 (I) | branch B5: leak at 13, `(0,2,±1)` |
| 17 | 17 (I) | branch B6: leak at 19, `(−2,1,0)` |

In every branch, a site's value at `t + 1` is `G(S_t) − y_{t−1}`. Each step below lists every site
whose value differs from the free cycle, and every site that decides the outcome.

**B1** (`τ₀ ∈ {18, 19, 0, 1}`; no event at 18, 19 or 0).
- `t = 1 → 2`. The only event: `(1,1,0)`. `S = 2 + w_1(1) = 1`, so `y_2 = 0 − y_0 = 0`; the free
  value is 1.
- `t = 2 → 3`. At `(2,1,0)` the sum is `0 + w_2(2) = 1`: no leak. At `(−2,1,0)` it is
  `y_2(−1,1,0) + w_2(−2) = 1 + 1 = 2`, and `(−1,1,0)` is free at `t = 2`. So `y_3(−2,1,0) = 1`:
  **leak at 3**.

**B2** (`τ₀ = 7`).
- `7 → 8`. `(1,1,0)`: `S = −2 + w_7(1) = −2 + 1 = −1`, so `y_8 = 0 − y_6 = 0 − (−1) = 1` (free 0).
  `(−1,1,0)`: `S = −2 − 1 = −3`, so `G = −1 = G(−2)`, as free.
- `8 → 9`. `y_8`: `O = −2`, `(1,1,0) = 1`, line.
  - `(0,1,0)`: `−2 + 1 + w_8(0) = −2 + 1 + 1 = 0`, so `y_9 = 0 − y_7 = 1` (free 0).
  - `(1,0,0)`: `−2 + 1 = −1`, so `y_9 = 1` (free 0).
  - The other E1 sites: `−2`, so `y_9 = −1 + 1 = 0`.
  - `(1,1,±1)`: sum 1, so 0.
  - `(2,1,0)`: `1 + w_8(2) = 1 − 1 = 0`.
  - `(1,2,0)`: `(+1) + (−1) + 1 = 1`, so `G = 0` and the line value is free.
- `9 → 10`.
  - `O`: sum `1 + 1 = 2`, so `y_10 = 1 − (−2) = 3`.
  - `(1,1,0)`: `1 + 1 + w_9(1) = 1 + 1 − 1 = 1`, so `y_10 = 0 − 1 = −1`.
  - `(−1,1,0)`: `y_9(0,1,0) + w_9(−1) = 1 + 1 = 2`, so `y_10 = 1 − 0 = 1`.
  - Every other site of `C` and every outside site: sum in `{−1, 0, 1}` with previous value 0, or
    free.
- `10 → 11`. At `(−2,1,0)` the sum is `y_10(−1,1,0) + w_10(−2) = 1 + 1 = 2`: **leak at 11**.

**B3** (`τ₀ = 8`).
- `8 → 9`. `(0,1,0)`: `S = −2 + w_8(0) = −1`, so `y_9 = 0 − y_7 = 1` (free 0). This is the only
  event.
- `9 → 10`.
  - `O`: sum 1, so `y_10 = 0 − (−2) = 2`, as free.
  - `(1,1,0)`: `1 + w_9(1) = 1 − 1 = 0`, so 0, as free.
  - `(−1,1,0)`: `1 + w_9(−1) = 1 + 1 = 2`, so `y_10 = 1` (free 0).
  - `(0,1,±1)`: sum 1, so 0.
- `10 → 11`. At `(−2,1,0)`: `1 + w_10(−2) = 1 + 1 = 2`: **leak at 11**.

**B4** (`τ₀ ∈ {9, 10}`; no event at 9).
- `10 → 11`. `(0,1,0)`: `S = 2 + w_10(0) = 1`, so `y_11 = 0` (free 1).
- `11 → 12`.
  - `O`: sum 5, so `G = 2` and `y_12 = 0`, as free.
  - `(1,1,0)`: `0 + 1 + w_11(1) = 2`, so 1, as free.
  - `(−1,1,0)`: `0 + 1 + w_11(−1) = 0`, so 0 (free 1).
  - `(0,1,±1)`: `0 + 1 = 1`, so 0 (free 1).
  - The other E2 sites: 2, so 1.
- `12 → 13` (`y_12` = E2 except `(−1,1,0), (0,1,±1)`, which are 0).
  - `(0,1,0)`: `1 + w_12(0) = 1 + 1 = 2`, so `y_13 = 1 − 0 = 1` (free 0).
  - `(−1,1,±1)`: `0 + 1 + 0 = 1`, so 0 (free 1).
  - `(1,1,±1)`: `0 + 1 + 1 = 2`, so 1.
  - The other C3: 3, so 1.
  - E1 other than `(0,1,0)`: sum 4 or 3, so `G = 1`; against previous value 1 this gives 0, as free.
  - `(0,2,±1)`: `0 + 1 = 1`: no leak.
  - `(±2,1,0)`: `1 − 1` and `0 − 1`: no leak.
- `13 → 14` (`y_13` = C3 except `(−1,1,±1)`, plus `(0,1,0) = 1`).
  - `(−1,1,0)`: `1 + 0 + w_13(−1) = 1 + 1 = 2`, so `y_14 = 1 − 0 = 1`.
  - `(0,1,±1)`: `1 + 1 = 2`, so `y_14 = 1`.
  - `(−1,0,±1)`: `0 + 1 = 1`, so `y_14 = 0 − 1 = −1`.
  - `(1,1,0)`: `1 + 2 + w_13(1) = 2`, so 0.
  - The other E2: 2 against previous value 1, so 0.
  - `(±1,2,±1)`: `1 + w_13(1) = 0` and `0 + w_13(−1) = 1`: no leak.
- `14 → 15`. At `(−2,1,0)`: `y_14(−1,1,0) + w_14(−2) = 1 + 1 = 2`. Its other neighbours
  `(−2,0,0)` and `(−2,1,±1)` are 0 at 14. **Leak at 15.**

**B5** (`τ₀ = 11`).
- `11 → 12`. `(−1,1,0)`: `2 + w_11(−1) = 1`, so 0 (free 1). This is the only event.
- `12 → 13`. The O-event at `(0,2,±1)` reads `y_12(0,1,±1)` and `w_12(0)`. Both are free, since
  `(0,1,±1)` reads E1 values at 11, which are unaffected. The sum is `1 + 1 = 2`: **leak at 13**.

**B6** (`τ₀ = 17`).
- `17 → 18`. `(−1,1,0)`: `−2 + w_17(−1) = −1`, so `y_18 = 0 − y_16 = 1` (free 0).
- `18 → 19`. At `(−2,1,0)`: `1 + w_18(−2) = 1 + 1 = 2`: **leak at 19**.

All 20 f-type starts leak, each within 6 ticks of its start. By the mirror, so do the 20 g-type
starts. The largest value in any branch before its leak is `|y| = 3` (B2, `O` at 10). So RZ equals
Q for `3 ≤ c ≤ q − 4`.

### 5.2 Placement `(2, 1)`

The line is `(x, 2, 1)`, matched at `x ≡ t + 1`. Free cycle: `w_t(x) = (−1)^{(x+t+3)/2}`. The values
used are:
- `w_t(0) = (−1)^{(t+3)/2}`;
- `w_t(1) = (−1)^{t/2}`;
- `w_t(−1) = −(−1)^{t/2}`;
- `w_t(±2)`: `(−1)^{(t+5)/2}` and `(−1)^{(t+1)/2}`, which are equal.

**Contact sites.**
- `(0,1,1)` (E2), with line neighbour `(0,2,1)`.
- `(±1,1,1)` (C3), with line neighbour `(±1,2,1)`.

**Coupling sites.**
- `(x,2,0)` for `|x| ≤ 1`: cube neighbour `(x,1,0)`, line neighbour `(x,2,1)`.
- `(±2,1,1)`: cube neighbour C3 `(±1,1,1)`, line neighbour `(±2,2,1)`.

**I-events.** The C3 breather sums at phases 0, 2, 4, 6, 8 are `0, 3, 0, −3, 0`, all ≡ 0 (mod 3).
So by L2 the C3 contact sites never deviate. At `(0,1,1)` the sums are `S_b = 2, 2, −2, −2` at phases
1, 3, 5, 7. The line values `w_t(0)` at `t = 1, 3, …, 19` are `+, −, +, −, +, −, +, −, +, −`. This
gives events at `t = 3` (`2 − 1`), `5` (`−2 + 1`), `11` (`2 − 1`) and `17` (`−2 + 1`).

**O-events.**

| site | cube values | free sums | O-events |
|---|---|---|---|
| `(0,2,0)` | E1 at 1, 7, 11, 17 (`+,−,+,−`) | `1+1, −1−1, 1−1, −1+1` | 1, 7 |
| `(1,2,0)` | E2 at 2, 6, 12, 16 | `1−1, −1−1, 1+1, −1+1` | 6, 12 |
| `(−1,2,0)` | E2 at 2, 6, 12, 16 | `1+1, −1+1, 1−1, −1−1` | 2, 16 |
| `(±2,1,1)` | C3 at 3, 5, 13, 15 | `1+1, −1−1, 1−1, −1+1` | 3, 5 |

**Starts.**

| `τ₀` | outcome |
|---|---|
| 18, 19, 0, 1 | leak at 2, `(0,2,0)` |
| 2 | leak at 3, `(−1,2,0)` |
| 3 | leak at 4, `(±2,1,1)` |
| 4, 5 | leak at 6, `(±2,1,1)` |
| 6 | leak at 7, `(1,2,0)` |
| 7 | leak at 8, `(0,2,0)` |
| 12 | leak at 13, `(1,2,0)` |
| 13–16 | leak at 17, `(−1,2,0)` |
| 8–11 | branch C1: leak at 13, `(1,2,0)` |
| 17 | branch C2: leak at 20, `(−2,1,1)` |

**C1** (`τ₀ ∈ {8, …, 11}`).
- `11 → 12`. `(0,1,1)`: `2 + w_11(0) = 1`, so 0 (free 1). This is the only event.
- `12 → 13`. The O-event at `(1,2,0)` reads `y_12(1,1,0)` and `y_12(1,2,1)`.
  - `(1,1,0)` reads E1 values at 11, which are free, so it is free (1).
  - `(1,2,1)`: line neighbours `w_11(0) + w_11(2) = −1 + 1 = 0`, and its cube neighbour `(1,1,1)`
    is 0 at phase 1. So it is free: `w_12(1) = 1`.
  - The sum is 2: **leak at 13**.

**C2** (`τ₀ = 17`).
- `17 → 18`. `(0,1,1)`: `−2 + w_17(0) = −1`, so `y_18 = 0 − y_16 = 0 − (−1) = 1` (free 0).
- `18 → 19` (`y_18`: `O = −2`, `(0,1,1) = 1`, line).
  - `(−1,1,1)`: `1 + w_18(−1) = 1 + 1 = 2`, so `y_19 = 1` (free 0).
  - `(1,1,1)`: `1 + w_18(1) = 1 − 1 = 0`, so 0.
  - `(0,0,1)` and `(0,1,0)`: `−2 + 1 = −1`, so `y_19 = 0 − (−1) = 1` (free 0).
  - The other E1: `−2`, so 0.
  - `(0,1,2)`: sum 1, so 0.
  - `(0,2,1)`: `0 + 1 = 1`, so the line value is free.
  - `(±1,2,0)`: E2 values at phase 8 are 0, so no leak.
- `19 → 20`. At `(−2,1,1)`: `y_19(−1,1,1) + w_19(−2) = 1 + 1 = 2`: **leak at 20**. (At the same
  update, `O` becomes 3, and `(−1,1,0)`, `(−1,0,1)` become 1.)

All 20 f-type starts leak, each within 5 ticks; by the mirror, so do the g-type starts. Values stay
in `{−2, …, 3}`.

### 5.3 Count

Direct contact gives 2 × 40 = 80 configurations, and indirect contact gives 120 (§4). All 200
matched configurations within distance 2 leak without input.

***

## 6. Theorem T and its corollaries

**Theorem T [W, (N), conditional on A-NU9].** It is stated in §0 item 3. Every case of the proof
uses NU9's values, which are ASSUMED (hand re-derived; exact re-run pending). Its proof:
- unmatched lines: L3(a);
- `δ ≥ 3`: L3(b), with the cube's boundary ternary (R4) and the line ternary with or without a
  signal;
- `δ = 2`: T-IND (§4);
- `δ = 1`: §5.1–5.2, with the mirror (§3).

**Corollary T1 (no signal interaction with a bare breather on one line; conditional on A-NU9).** In
case (a), `S = N + (F − background)` exactly, so there is no interaction. In case (b), the no-input
orbit leaks, and a signal interaction, like a controlled turn, requires a no-input orbit that does
not leak (§1). So no bare-breather gadget with one W2 line, at any placement, phase or component,
realizes a leak-free signal interaction.

**Corollary T2 (bare breather with several lines, none in direct contact; conditional on A-NU9).**
Let the gadget be the bare breather with finitely many W2 lines, in either component, such that
the cube and the lines are pairwise disjoint and non-adjacent (so every line has `δ ≥ 2`). Let some coupling site of the cube
touch exactly one matched line. Then the no-input orbit leaks (T-IND), and the gadget realizes no
leak-free controlled turn or signal interaction. A turn through the breather needs at least two
lines that interact with it, which by L3 are matched with `δ ≤ 2`. T2 therefore leaves open exactly
the arrangements with a line in direct contact (`δ = 1`), with two lines adjacent to each other, or
in which every coupling site of the cube is shared between matched lines (§7).

**What the obstruction rests on.** The leaks come from the period mismatch of L4:
- NU9 recurs after 10 ticks, while a W2 line is negated after 10;
- every coupling site therefore reaches `|S| = 2` within 20 ticks, two breather periods, unless the
  breather is perturbed first. One period does not suffice in general: at an E1 or C3 site the two
  nonzero phases are 6 or 2 ticks apart, both `y` and `w` change sign between them, and `y·w` keeps
  its sign (at an E2 site they are 4 apart, and `y·w` changes sign);
- at direct contact the perturbation occurs first, and §5 shows that it reaches a coupling site
  within 6 ticks.

L4 is the general form: any gadget site at a corner contact with an undisturbed W2 line must have
period 4 in sign, up to zeros.

**Excluded class.** Conditional on A-NU9, the following are excluded:
- (i) every gadget whose allowed region is a 3 × 3 × 3 cube carrying NU9 at some phase plus one
  straight W2 line, disjoint from it: no leak-free controlled turn and no leak-free signal interaction;
- (ii) every gadget whose allowed region is that cube plus finitely many straight W2 lines, in
  either component, pairwise disjoint, none adjacent to the cube or to another line, with one
  coupling site of the cube touching exactly one matched line: no leak-free no-input orbit, hence
  no turn and no interaction.

Both hold at every uniform background `c` with `3 ≤ c ≤ q − 4`, for any `q ≥ 7`, for full straight
lines only (not rays or segments), and for the W2 signal and background only.

***

## 7. Established / Assumed / Missing; (N)/(I)

| Result | Label | Status | ESTABLISHED | ASSUMED (where it enters) | MISSING |
|---|---|---|---|---|---|
| L1, L2 | (N) | writer's; elementary | as stated | MQ1's converse (`main`) | — |
| L3 | (N) | writer's | (a) from NU1; (b) from MQ2(b) | NU1 (F1, reviewed, not on `main`); MQ2 (`main`) | — |
| L4 (period-4 locking) | (N) | writer's; unreviewed | for any `K`, corner contact with an undisturbed W2 site | L1; (W) for W2 backgrounds (U1 E2, on `main`) | how often the "undisturbed" hypothesis holds in a gadget's no-input orbit |
| L5 (first deviation) | (N) | writer's; unreviewed | for disjoint confined parts; leak at the first departure when they are non-adjacent | MQ1 | — |
| T-IND | (N) | writer's; unreviewed | all matched indirect placements of one line (120 configurations); the multi-line version under its stated hypothesis | NU9 (R4; hand re-derived in review; exact re-run pending, not on `main`); L5; (W) | multi-line arrangements without a single-line coupling site |
| §5 direct contact | (N) | writer's hand derivation; unreviewed | 80 configurations, each followed to its leak | NU9; L2; the f/g reduction of §3 (mirror symmetry of Q) | an exact re-run (a computation; not authorized, not run) |
| Theorem T, T1, T2 | (N) | writer's; conditional on A-NU9; mathematics confirmed in review (#1549 c.7077076211) | given A-NU9, the class of §6 | A-NU9 in every case (R4; hand re-derived; exact re-run pending, not on `main`); as above; the definitions of §1 (PT, U2) | NU9-CHECK; everything listed below |

No quantum, operational or measurement assumption is used. The W2 lines and the breather are
designed initial patterns, a scope condition, not a claim about native preparation.

**MISSING (not excluded; mathematics unless stated):**
- two or more interacting lines with at least one in direct contact, or with coupling sites shared
  between lines (the first event can then be an I-event whose branch depends on the other lines);
- two lines adjacent to each other (a line–line contact), with the breather nearby;
- rays or finite segments that end next to the cube, as in PT's turn geometries J1 and J2. The class
  of §6 uses full straight lines only, and a line end is a contact of its own (U1 E6);
- lines that meet the cube (`δ = 0`), where the initial configuration is not a sum of parts;
- allowed regions `K ⊋` cube, including any gadget that places absorbers, spacers or a period
  converter at the coupling sites. L4 still applies at every corner contact of such a gadget;
- W1 lines and signals (period 6; L4's sign argument uses period 4), non-uniform backgrounds, and
  breathers other than NU9 (none other is derived in the corpus);
- a turn or interaction that uses a breather only as a timing element, away from the lines;
- the exact re-run of NU9 (NU9-CHECK), on which Theorem T, T1 and T2 are conditional (a computation;
  not authorized);
- whether R_q is universal in Definition U: not addressed.

***

## 8. Productivity, classification, skepticism

**Productivity (PLAN test).**
- (ii) is met: Theorem T and Corollaries T1–T2 exclude a stated class of thick gadgets built around
  NU9. No earlier record excludes that class:
  - PT's class is planar and contains no thick gadget;
  - U2's families have at most 6 sites, and NU9 needs 27;
  - R4 states only the design inference.
- (iii) is met, at a smaller scale: L4 and L5 hold for every gadget attached to W2 lines.
- (i) is not met.

| Item | Class (§A.31) |
|---|---|
| Theorem T, T1, T2 (bare breather + W2 lines) | NEW (negative, scoped) |
| L4 (period-4 locking at corner contacts) | NEW, minor (MQ1's converse with (W)); an assumption-watch for every breather-based design |
| L5 (first deviation is a leak, for non-adjacent parts) | NEW, minor (MQ2 made exact at coupling sites) |
| L1 | ELABORATING (NU6(b) for non-closed regions) |
| L2, L3 | CONFIRMING (elementary; NU1, MQ2(b)) |

**Skepticism (§A.31).** The checks target the ways the result could be wrong in either direction.
1. *Completeness of the placements.* Every axis line reduces to `ℓ(a,b)`, `a ≥ b ≥ 0`, by symmetries
   that fix NU9. NU9's values depend only on the site class (R4 §1), and Q commutes with the cube
   group.
2. *Completeness of the phases.* For each placement there are 10 × 4 matched initial states. These
   are the two 20-tick free cycles (f-type, and g-type by mirror). Every start of the f-type cycle is
   treated.
3. *Completeness of the event tables.* The coupling and contact sites were found by listing every
   neighbour of every line site near the cube. The coupling sites of one closed set and one line
   are exactly the outside sites with one neighbour in each.
4. *Branches.* The decisive sum in each branch is written out with every term. The immediate
   starts use only the free cycle and the event tables. A slip in one of the eight branches
   B1–B6, C1–C2 could change that start's outcome, so each is for the reviewer to recheck.
5. *Countercontrol on paper.* Under the constant rule `F ≡ 2c` (P3-K1) no outside site ever moves,
   so none of the leaks of §4–5 occurs. For a line in the other component, L3(a) gives no coupling.
   Both confirm that the leaks use `G`'s rounding and the shared component.
6. *Window.* Every value in §4–5 before the leak lies in `{−2, …, 3}`.

**An exact check (described, not preregistered, not run).** Running the 40 matched initial states
of each of the five placements on a torus of side at least 16, to the first leak, would confirm the
tables of §4–5. It is a computation and needs separate authorization. It is not part of this round.

**Assumption-watch.** *AW-NU-5 (period mismatch).* A finite periodic structure attached to W2 lines
through corner contacts must have its contact values sign-locked to period 4 (L4). Any proposal to
use NU9, or any period-≡ 2 (mod 4) orbit, as a gadget part must say how the contact sites avoid it:
direct contact only, a converter, or zero values at contact ticks.

**Fixed point.** One pass, with NEW items; the §A.31 fixed point is not reached. Under PLAN's stop
rule the round stops here: the question is answered for the stated class, and the next classes
(§7) need either branch analyses beyond hand scale or a computation.
