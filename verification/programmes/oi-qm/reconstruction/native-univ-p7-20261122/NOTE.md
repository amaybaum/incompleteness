# NATIVE-UNIV, round 7: the NU9 breather is decoupled unless a piece touches it

**Standing.** Writer's research record, paper only. It follows `PLAN.md` (`2ed611a`), committed
first. Independent non-author review at `5aec000` (relayed by the coordinating session, not posted):
REVISE, with two blockers. This revision answers blockers 1–2, items 3–6 and nits (a)–(e): the
lemmas and theorems are stated with clusters of all parts, class (b) carries PLAN's definition, and
the matched-cluster form of L11 is withdrawn (its counterexample is in §2). No computation was run,
no script is added and no exact check was replayed. Every statement below is derived by hand or
follows from a stated lemma. Every result that uses NU9 is conditional on A-NU9: NU9 is hand
re-derived (R4's review, R5's and R6's reviews), and its exact re-run NU9-CHECK is pending and not
authorized.

Inputs and their standing are listed in `PLAN.md`: `R6` (round 6: L6–L10, T-IND′, Theorem H and
its branch tables), `R5` (L1–L5, T-IND), `R4` (NU9), `PT`, `P2N`, `F1` are reviewed or
preregistered records not on `main`; `U1`, `U2` and `MQ` are on `main`.

**Layer.** Every statement concerns the configuration dynamics of Q. None concerns effects,
instruments, accessible algebras or readouts.

***

## 0. Summary

1. **Definitions (§1).** The gadgets are the bare NU9 breather on `C = {−1,0,1}³` plus finitely
   many straight W2 pieces (R6 §1). Two parts are in *contact* when a site of one is adjacent to a
   site of the other. The *clusters* are the connected components of the contact graph on all
   parts, matched and unmatched. The *clamped orbit* of a set `K` is its orbit with every site off
   `K` held at `c`. Class (a): some contact exists. Class (b) (PLAN): no piece touches `C`, and
   every coupling site touches at least two matched pieces.
2. **L11 (clamped clusters) [W, (N)].** In a run that does not leak, each cluster follows its own
   clamped orbit, in both components, whatever the other clusters carry. No confinement hypothesis
   is needed. The form with clusters of `C` and the matched pieces only is false: an unmatched
   piece in contact with matched parts can carry breather-component values without a leak (§2).
3. **L12 (leak transfer) [W, (N)].** If the clamped orbit of a union of clusters gives a site
   outside the allowed region an allowed-neighbour sum of absolute value ≥ 2 at `T − 1`, and that
   site touches no other part (or the other clusters' clamped values do not reduce the sum below
   2), the gadget leaks by `T`.
4. **Theorem D (§3), conditional on A-NU9 for (i).** Class 𝒩: no piece touches `C`. It contains
   class (b) and the members of class (a) whose contacts are between pieces only, among them the
   thick J1 analogue with adjacent arms that do not touch the cube. In every leak-free run:
   - (i) the breather is NU9 at the phase fixed by its initial state;
   - (ii) the pieces follow their clamped orbit, the same for every breather phase.

   So no input is written into the breather, the signal's orbit does not depend on the breather, and
   a controlled turn needs the output piece in the input piece's cluster. In class (b′), class (b)
   with all parts pairwise not in contact, there is no controlled turn. A leak-free signal orbit
   there equals the free superposition, except possibly by *absorption*: the signal piece follows
   its clamped orbit after its own free orbit leaves the line sector (U1 E6), with the breather and
   the other pieces unchanged. Whether any (b′) gadget absorbs is MISSING.
5. **L13 and Example E (§2–3), conditional on A-NU9.** In class 𝒮 (parts pairwise not in contact,
   R6 Corollary R2's setting) the no-input free superposition leaks within 20 ticks unless the
   matched pieces' values cancel at every coupling site of the cube; when they cancel, and every
   other outside sum stays in `{−1, 0, 1}`, the orbit is admissible. Example E, three rays at the
   corner `(1,1,1)`, is in class (b′) ⊂ 𝒮 and is admissible. So class (b) is not empty; the
   breather is decoupled in it (Theorem D).
6. **Theorem HO (§4), conditional on A-NU9.** Let one matched head-on W2 piece touch the cube
   (R6's `H00`, `H10`, `H11`, at least two sites), and let no further piece touch the cube or that
   piece (class (a2)). Then no controlled turn involves that piece or the breather (L11). If, for
   every start, one of the sites listed in §4 touches no further piece, every
   f-cycle start leaks by R6's leak tick, and no initial state has an admissible no-input orbit.
   For one further straight piece the conclusion of (b)–(c) holds in every placement, except at
   `H00` for a matched piece through `(−3,0,0)`; there 16 of the 20 f-starts leak for every background of that
   piece, and the other 4 leak for two of its four backgrounds and are not decided for the others.
7. **Necessary condition AW-NU-7 (§5).** For the breather to take part in a leak-free orbit other
   than through the leak condition at its coupling sites, a piece must touch the cube. For a
   controlled turn around the breather, the input and output pieces, which are distinct, must both
   lie in the breather's cluster, so that cluster holds at least two pieces. Theorem HO adds that a
   cluster `{C, P_in}` with a head-on `P_in` has no admissible no-input orbit under its condition,
   and so no signal interaction. This is a condition on designs. A gadget meeting it would still not
   show that R_q is universal.
8. **MISSING (§6).** Not settled:
   - class (a3): a cluster of the cube with two or more pieces (two pieces touching the cube, or a
     piece touching a piece that touches it), including the thick J1 analogue at the cube, every
     head-on input arm whose output arm touches the cube or the input arm, and every gadget with an
     unmatched piece touching the cube or `P_in`. Beyond hand scale; an exact check is described,
     not run;
   - absorption in class (b′), and the clamped orbits of piece clusters in 𝒩 (turns of the pieces'
     own dynamics in (b) ∖ (b′) and (a1));
   - the `H00` sub-case of item 6;
   - R6's open cases, which this round does not take up;
   - NU9-CHECK.

   No claim is made that R_q is non-universal.
9. **Excluded classes (§5), in one statement.** Class (b′): no controlled turn, no write, and no
   signal interaction other than absorption. Class 𝒩 (containing (b) and (a1)): the breather is
   decoupled. Class (a2): no turn involving `P_in` or the breather; under Theorem HO's condition no
   admissible no-input orbit.
10. **Productivity (§7):** gem by (ii), for Theorems D and HO, and by (iii), for L11 and L12.

***

## 1. Definitions

Notation as in R5 §1 and R6 §1: RZ, `y = x − c`, `y_{t+1}(i) = G(S_t(i)) − y_{t−1}(i)` with
`G(s) = ⌊(s+1)/3⌋`, `S_t(i)` the sum over the six neighbours, `p(i) = i₁ + i₂ + i₃ mod 2`. NU9
occupies the component `p(i) + t` even, with the breather at phase `t mod 10`, and its nonzero
phases are `O` at 0, 8 (`±2`), `E1` at 1, 7, `E2` at 2, 6, `C3` at 3, 5 (`±1`). A site's update
from `t` to `t + 1` reads slots `(j, t)`, `j` a neighbour, which lie in the component of `(i, t+1)`.
So a sum that decides a breather-component slot never contains a value of the other component
(NU1).

**Gadgets.** A *gadget* is the bare breather on `C` at some phase plus finitely many straight W2
pieces `P_1, …, P_m` (rays, finite segments of `n ≥ 1` sites, or lines; R6 §1), pairwise disjoint
and disjoint from `C`, at a uniform background `c` with `3 ≤ c ≤ q − 4`, `q ≥ 7`. The pieces carry
the restriction of a W2 background, the ends included (R6 §1); a piece may also carry a W2 signal
(U1 E2, U2 K0) launched at distance ≥ 8 from every other part. The *parts* are `C` and the pieces.
The allowed region is `A = C ∪ ⋃ P_k`. *Leak*, *matched*, *coupling site*, *contact site*,
*free superposition*, *admissible no-input orbit*, *controlled turn* and *signal interaction* are as
in R5 §1–2 and R6 §1. A *coupling site* of the cube is a site outside `A` adjacent to `C` and to a
matched piece.

**Contact, clusters.** Two parts are in *contact* when a site of one is adjacent to a site of the
other. The *contact graph* has as vertices all parts, `C` and every piece, matched or unmatched,
with an edge for each contact. Its connected components are the *clusters*; the cluster containing
`C` is the *breather's cluster*.

**Clamped orbit.** For a set `K` and an initial state on `K`, the *clamped orbit* `Ȳ^K` is the
sequence on `K` with
```text
Ȳ_{t+1}(i) = G( Σ_{j ∈ N(i) ∩ K} Ȳ_t(j) ) − Ȳ_{t−1}(i),   i ∈ K,
```
that is, the update with every site off `K` held at `c`. If the free orbit of `K`'s initial state
alone (allowed region `K`) does not leak on an interval, it satisfies this recursion there and so
equals `Ȳ^K` there. In particular:
- the clamped orbit of `C` from an NU9 state is NU9 (A-NU9: NU9 alone is confined to `C`);
- the clamped orbit of a W2 piece without a signal is its frozen background (L6);
- R6's branch computations assume every outside site is at `c` up to the leak tick (R6 §5), so they
  compute the clamped orbit of `C ∪ P` up to the tick before the leak.

**Classes.**
- *Class (a), direct contact:* the contact graph has an edge. Within it:
  - *(a1):* no piece is in contact with `C`;
  - *(a2):* the breather's cluster is `{C, P_in}`, with `P_in` a matched piece head-on at
    ℓ1-distance 1 with at least two sites (R6 placements `H00`, `H10`, `H11`). So no other piece,
    matched or unmatched, is in contact with `C` or with `P_in`;
  - *(a3):* the remaining members of (a): the breather's cluster holds two or more pieces, or one
    piece that is unmatched, alongside or a single site.

  The three are disjoint and cover (a); (a1) is (a) ∩ 𝒩, with 𝒩 as below.
- *Class (b), fully shared coupling sites (PLAN):* no piece is in contact with `C`; some matched
  piece lies within ℓ1-distance 2 of `C`; and every coupling site of the cube is adjacent to at
  least two matched pieces. *Class (b′):* the members of (b) whose parts are pairwise not in
  contact.
- *Class 𝒩:* no piece is in contact with `C`. It contains (a1) and (b).
- *Class 𝒮:* the parts are pairwise not in contact (R6 Corollary R2's setting). It contains
  (b′).

The *thick J1 analogue* is a gadget with two pieces on perpendicular axes, both ending within
ℓ1-distance 2 of `C`, with at least one pair of adjacent sites ("adjacent arms"). It lies in (a1)
when neither arm touches `C`, and in (a3) otherwise. A head-on input arm with an output arm lies in
(a2) when the output arm touches neither `C` nor the input arm, and in (a3) otherwise.

**Breather decoupled.** In a run, the breather is *decoupled* when its values are NU9 at the phase
fixed by its initial state (and 0 in the other component) and the pieces' values are their clamped
orbit. A decoupled breather can still decide whether a run leaks, through L1 at its coupling sites.

**Starts.** As in R6 §5: for a placement of `P_in` and a free cycle of `C ∪ P_in`, the start `τ₀`
is the state `(Y(τ₀ − 1), Y(τ₀))` of that cycle on `C ∪ P_in`. Ticks are counted in the cycle clock
modulo 20, as in R6's tables; for a start after its event tick, add 20.

***

## 2. General lemmas

R5's L1–L5 and R6's L6–L10 are used as proved there, with their hypotheses checked where used.

**L11 (clamped clusters) [W, (N)].** Let a gadget run not leak at the ticks `t₀, …, t₁`. Then, for
each cluster `K`, the values on `K`, in both components, satisfy the clamped recursion of `K` for
every update `t → t + 1` with `t₀ ≤ t ≤ t₁`. They are therefore determined on `[t₀ − 1, t₁ + 1]` by
their values at `t₀ − 1` and `t₀`, independently of every other cluster.

*Proof.* Let `i ∈ K`. A neighbour of `i` lies in `K`, in another part, or outside `A`.
- A neighbour in a part outside `K` would put that part in contact with `K`, so it does not exist.
- A neighbour outside `A` is at `c` at `t`, since the run does not leak at `t`.

So `S_t(i) = Σ_{j ∈ N(i) ∩ K} y_t(j)`, and the update is the clamped one. ∎

*Remark.* L11 uses only the neighbourhood of the update and the definition of a leak. It holds for
any local second-order rule of this form, and for any finite `K`, not only for W2 pieces and NU9.
It is stronger than R5's L5(b): L5(b) gives the free superposition up to the first departure, for
confined parts that are not in contact, while L11 needs no confinement and holds after departures
inside `A`. It does not contain L5(a), which concerns parts in contact.

*The matched-cluster form fails.* Restricting the contact graph to `C` and the matched pieces, and
claiming L11 for its components in the breather's component, is false. An unmatched piece's
breather-component slots lie in `A`, so they can depart without a leak. Example: `C`; the matched
ray `P = {(x, 1, 1) : x ≥ 3}` with background `w_t(x) = (−1)^x (−1)^{(x+t)/2}` (on `x + t` even);
the unmatched ray `U = {(2, 1, z) : z ≥ 1}`; start `τ₀ = 1`.
- At `t = 3`, `u = (2,1,1)` reads `(1,1,1)` (C3, phase 3: `+1`) and `w_3(3) = +1`, and its other
  neighbours are 0 in the breather's component. So `y_4(u) = G(2) − 0 = 1`, a value inside `A`.
- At `t = 4`, `(1,1,1)` reads `S_b = 3·E2 = 0` plus `y_4(u) = 1`, so it keeps its NU9 value. The
  outside neighbours of `u` read `1` plus an E2 value 0, so nothing leaks at 5.
- At `t = 4`, `P`'s end `(3,1,1)` reads `y_4(u) + w_4(4) = 1 + 1 = 2`, so
  `y_5(3,1,1) = G(2) − w_3(3) = 0`, against the clamped value `−1` of `P` alone.

`P` is not in contact with `C`, so `C` and `P` are separate matched clusters, and `P` departs from
its clamped orbit in a run that is leak-free through tick 5. With clusters of all parts, `C`, `U`
and `P` form one cluster, and L11 holds.

**L12 (leak transfer) [W, (N)].** Let `K` be a union of clusters of a gadget, and `Ȳ` the clamped
orbit of `K` from the gadget's initial state on `K`. Let `s ∉ A` and `T − 1 ≥ τ₀`, and let the
other clusters adjacent to `s` be `K_1, …, K_r`, with clamped orbits `Ȳ^k`. If
```text
| Σ_{j ∈ N(s) ∩ K} Ȳ_{T−1}(j) + Σ_k Σ_{j ∈ N(s) ∩ K_k} Ȳ^k_{T−1}(j) | ≥ 2,
```
then the gadget leaks at some tick `≤ T`. In particular this holds when `s` is adjacent to no part
outside `K` and the first sum alone has absolute value ≥ 2. The hypothesis `s ∉ A` is needed: a
site of a part in another cluster carries no leak.

*Proof.* Suppose the run does not leak up to `T − 1`. By L11 every cluster follows its clamped
orbit through `T − 1`. At `T − 1`, `s`'s sum is the displayed one, since its neighbours outside `A`
are at `c`. Its value at `T − 2` is 0. So `y_T(s) = G(S) ≠ 0`, and `s ∉ A`: a leak at `T`. ∎

*Remark.* L12 needs no claim that `T` is the first leak of `K` alone. It needs only the clamped
values at `T − 1`, which R6's branch tables give.

**L13 (cancellation criterion in class 𝒮) [W, (N), conditional on A-NU9].** Let the gadget be in
class 𝒮 (parts pairwise not in contact, none in contact with `C`). For a coupling site `o` of the
cube, let `g` be its cube neighbour and `W_t(o) = Σ w_t(l)` over the matched piece sites `l`
adjacent to `o`. Then:
- (a) if `W(o) ≢ 0` at some coupling site `o`, the no-input orbit leaks within 20 ticks, from every
  initial state;
- (b) if `W(o) ≡ 0` at every coupling site, and every other site outside `A` has an
  allowed-neighbour sum in `{−1, 0, 1}` in the free superposition at every tick, the no-input
  orbit is the free superposition, never leaks and has period dividing 20. It is admissible.

*Proof.* The parts are closed and confined (A-NU9; L6) and pairwise non-adjacent, so L5(b) applies:
the orbit is the free superposition until the first tick at which an outside site has
`|S| ≥ 2`, and that tick is followed by a leak.
- `C` is closed, so `o` has the one cube neighbour `g`, and `g ∈ C ∖ O`. Each piece has at most one
  site adjacent to `o`: a site off a line has at most one neighbour on it, and a site on the line
  outside an interval is adjacent to at most one of its ends.
- `g` and every `l` adjacent to `o` have the parity of `o` plus 1, so at a tick at which `g` is
  active, every matched `l` is active, and `W_{t+2} = −W_t` (L6(c)).
- Let `t*` be a tick in `[τ₀, τ₀ + 9]` at which `v = y_{t*}(g) ≠ 0`; `v = ±1`, since `g` is a
  boundary site. Then `y_{t*+10}(g) = v` and `W_{t*+10} = −W_{t*}`. If `W_{t*} ≠ 0`, one of
  `|v + W_{t*}|` and `|v − W_{t*}|` equals `1 + |W_{t*}| ≥ 2`, at `t*` or `t* + 10 ≤ τ₀ + 19`.
  This gives (a), since `W_{t*} = 0` forces `W ≡ 0` by the sign alternation.
- Under (b) every coupling-site sum equals `y_t(g) ∈ {−1, 0, 1}`, and every other outside sum is in
  `{−1, 0, 1}`, so no outside site departs. NU9 has period 10 and each piece period 4. ∎

*Consistency with R6.* T-IND′ is the case of class 𝒮 in which some coupling site touches exactly
one matched piece: then `W(o) = ±1 ≢ 0`, and (a) gives T-IND′'s leak within 20 ticks.

***

## 3. Class 𝒩: the breather is decoupled

**Theorem D [W, (N); (i) conditional on A-NU9].** Let the gadget lie in class 𝒩, and let a run of
it, with or without a signal, not leak at the ticks `τ₀, …, t₁`. Then on `[τ₀ − 1, t₁ + 1]`:
- (i) the breather's values are NU9 at the phase fixed by the initial state, and 0 in the other
  component;
- (ii) the pieces' values are their clamped orbit from their initial state; each cluster of pieces
  follows its own clamped orbit;
- (iii) two leak-free runs whose initial states agree on the pieces agree on the pieces, whatever
  the breather's phase.

Hence, in class 𝒩:
- (D1) *no write:* in every leak-free signal orbit the breather is NU9 at its initial phase;
- (D2) *no dependence on the breather:* the signal's orbit is the clamped orbit of its piece's
  cluster, the same for every breather phase;
- (D3) *turns:* in a leak-free signal orbit, a piece outside the input piece's cluster follows its
  clamped orbit from its no-input initial state, so it carries its no-input values. A controlled
  turn therefore needs the output piece in the input piece's cluster, and in class (b′), where each
  piece is its own cluster, there is no controlled turn;
- (D4) *signal interaction in (b′):* let `N` be an admissible no-input orbit, `F` the signal's free
  orbit on its piece alone, and `F̄` the clamped orbit of the signal piece. A leak-free signal orbit
  is `S = N + (F̄ − background)` on the signal piece and equals `N` elsewhere. It equals
  `N + (F − background)` exactly when `F` does not leave the piece's line sector in the window.
  - On a full line, `F` never leaves it (R5 L3(b); U1 E2), so `S = N + (F − background)`: no
    interaction.
  - A signal that reaches a piece end leaves the line sector (U1 E6, A-E6), and then `F ≠ F̄`.
    The only signal interaction not excluded is *absorption*: a leak-free `S` in which the cube and
    the other pieces, with unchanged values, keep every outside sum in `{−1, 0, 1}` after the
    signal reaches its end. Whether any (b′) gadget absorbs is MISSING.

*Proof.* (i) and (ii) are L11: the breather's cluster is `{C}`, and the clamped orbit of `C` from an
NU9 state is NU9 (A-NU9, §1), with the other component's slots, which read only `C`'s
other-component values, at 0. (iii) follows from (ii), since the pieces' clamped orbit does not
refer to `C`. (D1)–(D3) follow, with the input signal launched on the input piece only. For (D4),
each piece of (b′) is its own cluster, and a W2 piece without a signal has its background as clamped
orbit (L6). If `F` stays in the line sector on the window, it satisfies the clamped recursion there
and equals `F̄`. If it leaves, `F` is nonzero off the piece and `F̄` is not. ∎

**Reading.** In class 𝒩 the breather constrains which runs are leak-free, through L1 at its
coupling sites, and does nothing else. A turn in class 𝒩 would be a turn of the pieces' clamped
dynamics, a question about the pieces (PT's kind) in which the breather does not take part. In
class (b′) every signal interaction is excluded except absorption.

**Example E (class (b′) has admissible no-input orbits) [W, (N), conditional on A-NU9].** Take the
three matched rays
```text
P1 = {(x, 1, 1) : x ≥ 3},   P2 = {(2, 2, z) : z ≥ 1},   P3 = {(1, y, 1) : y ≥ 3}.
```
- *Distances.* Each end, `(3,1,1)`, `(2,2,1)`, `(1,3,1)`, is at ℓ1-distance 2 from `C`; every other
  piece site is at distance ≥ 3. No piece is adjacent to `C`.
- *No contacts.* `d(P1, P2) = |x − 2| + 1 + |z − 1| ≥ 2`, `d(P2, P3) = 1 + |y − 2| + |z − 1| ≥ 2`,
  `d(P1, P3) ≥ 4`.
- *Coupling sites of the cube.* The distance-1 neighbours of the three ends are `(2,1,1)` (of
  `(3,1,1)` and `(2,2,1)`) and `(1,2,1)` (of `(2,2,1)` and `(1,3,1)`). Both have cube neighbour
  `g = (1,1,1)` (C3). `(2,1,1)` touches P1 and P2, and `(1,2,1)` touches P2 and P3; their other
  neighbours `(2,0,1)`, `(2,1,0)`, `(2,1,2)`, `(0,2,1)`, `(1,2,0)`, `(1,2,2)` are outside `A`. So
  the gadget is in class (b′).
- *Other shared sites.* The only other outside sites adjacent to two pieces are `(3,2,1)` (P1's and
  P2's ends) and `(2,3,1)` (P2's and P3's ends): a pair of sites of different pieces at distance 2
  occurs only for these two pairs of ends.
- *Parity.* The three ends and `g` have odd parity, so they are active at the same ticks.
- *Backgrounds.* Choose any phase, any background of P2, and backgrounds of P1 and P3 whose values
  at their ends are opposite to P2's end value at one active tick. By `w_{t+2} = −w_t` this holds at
  every active tick: `w(3,1,1) = w(1,3,1) = −w(2,2,1)`. Once that end sign is fixed, two of the
  four backgrounds of P1, and two of P3, qualify.

Then `W ≡ 0` at `(2,1,1)` and `(1,2,1)`, and the sums at `(3,2,1)` and `(2,3,1)` are 0. Every other
outside site is adjacent to at most one part, whose values are ternary (A-NU9; L6). Example E is in
class 𝒮, so L13(b) applies: the no-input orbit is NU9 plus the three backgrounds, admissible, of
period 20. By Theorem D the breather is decoupled in it and in every leak-free signal orbit of the
gadget, and by (D3) the gadget has no controlled turn.

**Skepticism (§A.31).** Example E is an admissible no-input orbit with matched pieces within
distance 2 of NU9. Its admissibility comes from the decoupling: the pieces cancel each other at the
coupling sites, so the breather is read at them only through `y(g)`, which is ternary. Whether a W2
signal on P1, P2 or P3 is absorbed (D4) is not derived: the signal reaches the end of its ray,
where its free orbit leaves the line sector (U1 E6), and the clamped orbit of a ray end after the
signal's arrival is not written out here.

***

## 4. Class (a2): one head-on arm and decoupled further parts

Let `P_in = {(x, a, b) : 2 ≤ x ≤ x₁}`, `x₁ ≥ 3` or `∞`, `(a, b) ∈ {(0,0), (1,0), (1,1)}`, be a
matched W2 piece, with `e = (2, a, b)` and the free cycles of R6 §1, and let `K = C ∪ P_in` be the
breather's cluster (class (a2)). The *further parts* are all other pieces, matched or unmatched;
none touches `C` or `P_in`. *Allowed* sites for a further piece are the sites outside `C ∪ P_in`
and adjacent to neither.

**Leak sites of the f-starts.** For each placement and each f-cycle start, the table lists a set
`Λ(τ₀)` of sites outside `C ∪ P_in`, each with an allowed-neighbour sum of absolute value ≥ 2 at
`T − 1` in the clamped orbit of `K`, and so a leak site at `T` in R6's run. Each such site is
adjacent to `K`, so in class (a2) it lies in no further part, and so outside `A`: a further part
containing it would be in contact with `K`.

| Placement | `τ₀` | `T` | `Λ(τ₀)` | sum at `T − 1` | from |
|---|---|---|---|---|---|
| `H11` | 17–19, 0–2 | 3 | `(2,1,0)`, `(2,0,1)` | `1 + 1` | R6 O-event at 2 |
| `H11` | 3–13 | 15 | `(2,1,0)`, `(2,0,1)` | `0 + 2` | R6 F1; checked below |
| `H11` | 14, 15 | 17 | `(2,1,0)`, `(2,0,1)` | `−1 − 2` | R6 F2; checked below |
| `H11` | 16 | 17 | `(2,1,0)`, `(2,0,1)` | `−1 − 1` | R6 O-event at 16 |
| `H10` | 18, 19, 0, 1 | 2 | `(2,0,0)` | `1 + 1` | R6 O-event at 1 |
| `H10` | 2, 3 | 8 | `(2,0,0)` | `−1 − 1` | R6 P1 |
| `H10` | 4, 5 | 8 | `(2,0,0)` | `−1 − 1` | R6 P2 |
| `H10` | 6 | 8 | `(2,0,0)` | `−1 − 2` | R6 P3; checked below |
| `H10` | 7 | 8 | `(2,0,0)` | `−1 − 1` | R6 O-event at 7 |
| `H10` | 8–11 | 14 | `(2,1,1)`, `(2,1,−1)` | `1 + 1` | R6 P4 |
| `H10` | 12 | 14 | `(2,0,0)` | `0 + 2` | R6 P5; checked below |
| `H10` | 13 | 14 | `(2,1,±1)` | `1 + 1` | R6 O-event at 13 |
| `H10` | 14, 15 | 16 | `(2,1,±1)` | `−1 − 1` | R6 O-event at 15 |
| `H10` | 16, 17 | 26 | the caps of `(−1,−1,±1)`: `(−2,−1,±1)`, `(−1,−2,±1)`, `(−1,−1,±2)` | `−2` | R6 P6; checked below |
| `H00` | 19, 0 | 8 | `(−2,0,0)` | `−2` | R6 H1 |
| `H00` | 1 | 3 | `(2,±1,0)`, `(2,0,±1)` | `1 + 2` | R6 H2 |
| `H00` | 2 | 3 | `(2,±1,0)`, `(2,0,±1)` | `1 + 1` | R6 O-event at 2 |
| `H00` | 3–7 | 9 | `(2,±1,0)`, `(2,0,±1)` | `0 − 2` | R6 H3 |
| `H00` | 8–16 | 17 | `(2,±1,0)`, `(2,0,±1)` | `−1 − 1` | R6 O-event at 16 |
| `H00` | 17, 18 | 28 | `(−2,0,0)` | `−2` | R6 H4 |

Each placement's rows cover its 20 f-starts. The sums at coupling sites are (cube value) + (value of
`e`); the others are the value of the one allowed neighbour.

*Checks of the rows that add sites to R6's.* In the first four, R6's branch has only `e` departing
before `T − 1` among the sites that decide the sum (R6 §5.1: only `e` and `r_3` depart up to each
leak; §5.2: P3 and P5 have one departure before the leak), so the cube site read is at its NU9
value.
- `H11`, F1: `y_{14}(e) = G(2) − y_{12}(e) = 2`. `(2,1,0)` reads `(1,1,0)` (E2, phase 4: 0) and
  `e`, so its sum is 2. `(2,0,1)` is its image under exchanging the second and third coordinates,
  which fixes `C`, `P_in` and NU9.
- `H11`, F2: `y_{16}(e) = G(−2) − y_{14}(e) = −2`; E2 at phase 6 is −1; the sum is −3.
- `H10`, P3: `y_7(e) = G(−2) − y_5(e) = −2`; `(2,0,0)` reads `(1,0,0)` (E1, phase 7: −1) and
  `e`; the sum is −3.
- `H10`, P5: `y_{13}(e) = G(2) − y_{11}(e) = 2`; E1 at phase 3 is 0; the sum is 2.
- `H10`, P6: R6 gives `y_{25}(−1,−1,±1) = G(−3) − 1 = −2`. Each listed cap has `(−1,−1,±1)` as its
  only neighbour in `C ∪ P_in`: its other neighbours have a coordinate of absolute value ≥ 2, so
  lie outside `C`, and first coordinate ≤ 0, so lie outside `P_in`. Its sum is −2.

*Segments.* For `3 ≤ x₁ < ∞`, R6's proof of Theorem H(a) applies L7 with the cut end at
`r_{x₁}`; L7's hypotheses were checked there. Its induction, read for clamped orbits (every outside
site at `c`), shows that the clamped orbit of `C ∪ P_in` agrees with that of `C` plus the ray at
every site outside the removed sites up to `T − 1`. Every site of the table has first coordinate
≤ 2 and is not adjacent to a removed site (first coordinate ≥ 4). So the table holds for segments.

**Allowed neighbours of the table's sites.** For each site used in Lemma G, its neighbours are
listed with the reason each is not allowed; the remaining ones are allowed. Of the six `H10` P6
caps only `(−1,−1,±2)` are listed, which is all Lemma G uses.

| Placement | site | allowed neighbours | the others |
|---|---|---|---|
| `H11` | `(2,1,0)` | `(2,2,0)` | `(1,1,0)` ∈ `C`; `(3,1,0)` touches `(3,1,1)` ∈ `P_in`; `(2,0,0)`, `(2,1,−1)` touch `C`; `(2,1,1) = e` |
| `H11` | `(2,0,1)` | `(2,0,2)` | the image of the row above |
| `H10` | `(2,0,0)` | none | `(1,0,0)` ∈ `C`; `(3,0,0)` touches `(3,1,0)` ∈ `P_in`; `(2,−1,0)`, `(2,0,±1)` touch `C`; `(2,1,0) = e` |
| `H10` | `(2,1,±1)` | `(2,2,±1)`, `(2,1,±2)` | `(1,1,±1)` ∈ `C`; `(3,1,±1)` touches `P_in`; `(2,0,±1)` touches `C`; `e` |
| `H10` | `(−1,−1,±2)` | `(−2,−1,±2)`, `(−1,−2,±2)`, `(−1,−1,±3)` | `(−1,−1,±1)` ∈ `C`; `(0,−1,±2)`, `(−1,0,±2)` touch `C` |
| `H00` | `(2,±1,0)` | `(2,±2,0)` | `(1,±1,0)` ∈ `C`; `(3,±1,0)` touches `(3,0,0)` ∈ `P_in`; `(2,±1,±1)` touch `C`; `e` |
| `H00` | `(2,0,±1)` | `(2,0,±2)` | the same, with the second and third coordinates exchanged |
| `H00` | `(−2,0,0)` | `(−3,0,0)` | `(−1,0,0)` ∈ `C`; `(−2,±1,0)`, `(−2,0,±1)` touch `C` |

**Lemma G (one straight further piece) [W, (N)].** Let `D` be one straight piece whose sites are
allowed. Then for every f-start some site of `Λ(τ₀)` is not adjacent to `D`, except at
`H00` for the starts `τ₀ ∈ {17, 18, 19, 0}` when `(−3,0,0) ∈ D`.

*Proof.* A straight piece adjacent to two sites contains an allowed neighbour of each, and so the
axis segment between them.
- `H11`: `(2,2,0)` and `(2,0,2)` differ in two coordinates.
- `H10`, `(2,0,0)`: no allowed neighbour. `(2,1,1)` and `(2,1,−1)`: the pairs on one axis line
  are `(2,2,1)`, `(2,2,−1)`, whose segment contains `(2,2,0)`, adjacent to `e`, and `(2,1,2)`,
  `(2,1,−2)`, whose segment contains `e`. The caps: `D` is not adjacent to both `(−1,−1,2)` and
  `(−1,−1,−2)`. An allowed neighbour of each on a common axis line is one of the pairs `(−2,−1,±2)`,
  `(−1,−2,±2)`, `(−1,−1,±3)`; the first two segments contain `(−2,−1,1)` or `(−1,−2,1)`, which
  touch `C`, and the third passes through `C`.
- `H00`, coupling sites: the pairs on one axis line are `(2,±2,0)` and `(2,0,±2)`, whose segments
  contain `e`. So `D` is adjacent to at most one of the four. `(−2,0,0)`: its only allowed neighbour
  is `(−3,0,0)`. ∎

**Theorem HO [W, (N), conditional on A-NU9].** Let the gadget be in class (a2), at a uniform
background `3 ≤ c ≤ q − 4`, with further parts in any state (any pieces, either component, with or
without signals, in contact with each other or not, none touching `C` or `P_in`).
- (a) No leak-free run carries a signal from `P_in` to another piece, or from another piece to
  `P_in`, and no input reaches the breather from a further piece. A controlled turn between
  further pieces would lie in their own cluster, with `K` following its clamped orbit. This part
  uses L11 only.
- (b) For each f-cycle start `τ₀` of `C ∪ P_in` at which some site of `Λ(τ₀)` is adjacent to no
  further piece, the run leaks by `T(τ₀) ≤ τ₀ + 12`.
- (c) If (b)'s condition holds at every f-start, no initial state of the gadget, with `C ∪ P_in` in
  either free cycle and the further parts in any state, has an admissible no-input orbit. So the
  gadget realizes no signal interaction.
- (d) For one further straight piece `D` without a signal (Lemma G), (b) and (c) hold in every
  placement except at `H00` with `D` matched and `(−3,0,0) ∈ D`. In that sub-case the 16 f-starts
  `τ₀ ∈ {1, …, 16}` leak by `T`, for every background of `D`. The starts `τ₀ ∈ {17, 18, 19, 0}` leak
  by `T` when `w^D_t(−3,0,0) = −1` at the ticks `t ≡ 3 (mod 4)`, and are not decided otherwise. If
  `D` is unmatched, (b) and (c) hold.

*Proof.*
- (a) By L11, in a leak-free run every further cluster follows its clamped orbit from its initial
  state, which is the same with and without a signal on `P_in`; and `K` follows its clamped orbit
  whatever the further parts carry.
- (b) L12 with `K = C ∪ P_in` and `s ∈ Λ(τ₀)` adjacent to no further piece; `s ∉ A` by the remark
  above the table. The clamped
  orbit of `K` up to `T − 1` is R6's branch (§1), and the table gives `|S| ≥ 2` at `T − 1`. R6's
  leak ticks give `T − τ₀ ≤ 12` (Theorem H(a)).
- (c) An f-state has no admissible orbit by (b). Let `y` be an admissible orbit from a g-state.
  By L8's general part, `ỹ_s = −y_{T′−s}` (`T′` even) is an orbit of the same gadget, leak-free on
  `ℤ` and periodic. By its breather and piece clauses, at the ticks `(T′ − τ₀, T′ − τ₀ + 1)` it
  carries on `C ∪ P_in` a free f-cycle state. On the further parts it carries some state. Its
  forward orbit from there leaks by (b), whose condition is geometric and holds for every state of
  the further parts. This contradicts its leak-freeness.
- (d) Lemma G gives (b)'s condition except in the stated sub-case. There, by L11, a leak-free run
  up to `T − 1` has `D` at its background, so the sum at `(−2,0,0)` at `T − 1` is
  `−2 + w^D_{T−1}(−3,0,0)`. `(−3,0,0)` is active at `T − 1 ≡ 7 (mod 20)`, `w^D_{t+4} = w^D_t`, and
  L12 gives a leak by `T` when this sum is −3. If `D` is unmatched, its clamped orbit keeps its
  breather-component slots at 0, since they read only `D`'s own breather-component values, so the
  sum is −2, and (c)'s argument applies to every state of `D` whose breather-component slots are 0,
  signals in its own component included. ∎

*Values.* Every clamped value of `K` used lies in `{−2, …, 3}` (R6 Theorem H), so RZ equals Q
there (U1 Lemma 2.1).

*Use of the periodicity requirement.* (c) excludes the g-states, and in (d) every state, only
through periodicity, by L8, as in R6 Theorem H(b). Under R5's forward-only requirement the g-states
of (c) would be open.

***

## 5. Necessary condition AW-NU-7

**Proposition (any bare-breather gadget with W2 pieces) [W, (N); conditional on A-NU9 where NU9 is
named].**
- (N5) If no piece is in contact with `C`, the breather is decoupled in every leak-free run
  (Theorem D). Its only effect is the leak condition at its coupling sites.
- (N6) A controlled turn needs the input and output pieces in one cluster (L11). For the breather to
  take part in it, they must lie in the breather's cluster. They are distinct pieces, so that
  cluster holds at least two pieces: two pieces in contact with `C`, or a piece in contact with a
  piece in contact with `C`. That is part of class (a3).
- (N7) Theorem HO adds, for the cluster `{C, P_in}` with `P_in` head-on at distance 1 and the
  further pieces satisfying its condition (b): no admissible no-input orbit, and so no signal
  interaction of any kind, not only no turn.

This sharpens R6's (N3), which allowed "a direct contact or no coupling site exclusive to one
matched piece": fully shared coupling sites without a contact to `C` leave the breather decoupled
(N5), and contacts between pieces only do the same. A gadget with an unmatched piece in contact
with `C` is not covered by (N5) (§2's example shows such a piece can carry breather-component
values). AW-NU-6 (L9's end locking) still applies to
every end in (a3) that touches a gadget site.

**Excluded classes, in one statement.** Conditional on A-NU9, at a uniform background `c` with
`3 ≤ c ≤ q − 4`, any `q ≥ 7`, W2 pieces as in R6 §1 and the W2 signal:
- (i) class 𝒩 (no piece in contact with `C`; it contains (b) and (a1)): in every leak-free run the
  breather is NU9 at its initial phase and the pieces follow their clamped orbit, the same for every
  breather phase; no input is written into the breather;
- (ii) class (b′): no controlled turn, and no signal interaction other than absorption (Theorem D
  (D4));
- (iii) class (a2) (breather's cluster `{C, P_in}`, `P_in` matched and head-on at distance 1 with
  at least two sites): no controlled turn involving `P_in` or the breather; and, when some site of
  each `Λ(τ₀)` touches no further piece, no admissible no-input orbit, hence no signal interaction.
  For one further straight piece without a signal the conclusion of (b)–(c) holds except at `H00`
  for a matched piece through `(−3,0,0)` (Theorem HO(d)).

These are conditions on designs and scoped exclusions. Meeting the conditions would not establish a
controlled turn, and a controlled turn would not establish that R_q is universal in Definition U,
which also needs gates, fan-out, composition and an encoding with a correctness proof (U1 §3).

***

## 6. Established / Assumed / Missing; (N)/(I)

| Result | Label | Status | ESTABLISHED | ASSUMED (where it enters) | MISSING |
|---|---|---|---|---|---|
| L11 (clamped clusters) | (N) | writer's; elementary | as stated, clusters of all parts, any finite parts; the matched-cluster form refuted (§2) | — | — |
| L12 (leak transfer) | (N) | writer's | as stated | L11 | — |
| L13 (cancellation) | (N) | writer's; conditional on A-NU9 | (a) and (b) in class 𝒮 | L5 (R5); L6 (R6); NU9 (R4) | — |
| Theorem D | (N) | writer's; (i) conditional on A-NU9 | (i)–(iii), (D1)–(D3); (D4) for full lines | L11; NU9 confined (R4); L6; U1 E2, E6 (`main`) | absorption in (b′) (D4); the clamped dynamics of piece clusters in (b) ∖ (b′) and (a1) |
| Example E | (N) | writer's; conditional on A-NU9 | admissible no-input orbit, period 20; no controlled turn | L13; NU9 | its signal orbits |
| Lemma G | (N) | writer's; elementary geometry | as stated | — | several further pieces (checked per gadget against the table) |
| Theorem HO | (N) | writer's; conditional on A-NU9 | (a); (b), (c) under the stated condition; (d) | R6's branch tables as clamped orbits (R6, reviewed); R6 L7, L8; NU9 | the `H00` sub-case of (d): 4 starts for half of `D`'s backgrounds, and (c) there |
| AW-NU-7 | (N) | writer's; a condition on designs | (N5)–(N7) | as above | whether any (a3) design is admissible; gadgets with an unmatched piece in contact with `C` |

No quantum, operational or measurement assumption is used. The breather and the pieces are designed
initial patterns, a scope condition, not a claim about native preparation.

**MISSING (not excluded; mathematics unless stated):**
- *Class (a3).* Every gadget whose breather's cluster holds two or more pieces: two pieces in
  contact with the cube (for example two head-on arms, or a head-on and an alongside arm); a
  head-on input arm with an output arm in contact with it; the thick J1 analogue with a junction at
  the cube. L12 does not reuse R6's branches here, because the second piece lies in the breather's
  cluster and changes its clamped orbit. Each geometry has 10 × 4 × 4 = 160 matched initial states
  in 8 free cycles, and R6's single-contact branches already run to 28–33 ticks with departures
  across the cube. This is beyond hand scale under PLAN's stop rule.
- *Unmatched contacts.* Gadgets with an unmatched piece in contact with `C` or with `P_in` (in
  (a3) by §1's partition). §2's example shows
  that such a piece can carry breather-component values without a leak, so neither Theorem D nor
  Theorem HO covers them.
- *Absorption in class (b′)* (Theorem D (D4)): whether a W2 signal reaching a piece end can be
  kept leak-free by the cube and the other pieces. It needs the clamped orbit of a ray end after the
  signal's arrival.
- *Clamped dynamics of piece clusters in classes (b) ∖ (b′) and (a1),* including the thick J1
  analogue away from the cube: whether it has a turn, and whether NU9 can keep its outside sums in
  `{−1, 0, 1}`. In either case the breather is decoupled (Theorem D).
- *The `H00` sub-case of Theorem HO(d):* the starts `τ₀ ∈ {17, 18, 19, 0}` when
  `w^D_t(−3,0,0) = +1` at `t ≡ 3 (mod 4)`, and admissibility for a matched `D ∋ (−3,0,0)`.
- *Several further pieces in class (a2)* that together are adjacent to every site of some
  `Λ(τ₀)`: Theorem HO(b) does not apply to those starts.
- R6's open cases, not taken up here: alongside pieces ending next to the cube, single-site
  segments, the K2 starts beyond tick 30, the forward orbits of segment g-states.
- The exact re-run of NU9 (NU9-CHECK), on which every NU9 result here is conditional (a
  computation; not authorized).
- Whether R_q is universal in Definition U: not addressed.

**An exact check (described, not preregistered, not run).** For each class-(a3) geometry with two
pieces of length at least 80 in the breather's cluster, run the 160 matched initial states to the
first leak or tick 200, and record the admissible ones. This is a computation and needs separate
authorization. It is not part of this round.

***

## 7. Productivity, classification, skepticism

**Productivity (PLAN test).**
- (ii) is met. Theorem D shows that the breather is decoupled in every leak-free run in class 𝒩,
  which contains (b) and (a1): no write, and no dependence of the pieces' orbit on the breather. In
  class (b′) it also excludes every controlled turn and every signal interaction other than
  absorption. Theorem HO excludes class (a2) under its stated condition. No earlier record excludes
  these: R5 and R6 cover gadgets in which some coupling site is exclusive to one matched piece, and
  single pieces.
- (iii) is met. L11 holds for every gadget and every finite set of parts, needs no confinement
  hypothesis, and holds after departures inside the allowed region; R5's L5(b) gives the free
  superposition only up to the first departure, for confined parts not in contact. L12 is its
  leak-transfer form.
- (i) is not met: no gadget is found.

| Item | Class (§A.31) |
|---|---|
| L11 (clamped clusters) and Theorem D | NEW: the breather is decoupled whenever no piece touches it, which removes class (b) and class (a1) from AW-NU-6's alternatives as mechanisms in which the breather takes part |
| Theorem HO, Lemma G | NEW (negative, scoped) |
| Example E | NEW: an admissible no-input orbit with matched pieces within distance 2 of NU9; POSITIVE for L13(b), not for a mechanism |
| AW-NU-7 | NEW, minor: R6's (N3) sharpened |
| L12 | ELABORATING (L5 and L11) |
| L13 | ELABORATING (T-IND′, made into a criterion) |

**Skepticism (§A.31).**
1. *L11 is elementary.* It uses the locality of the update and the definition of a leak only.
   Countercontrols: it is consistent with R5 Theorem T(a) (a line at distance ≥ 3 is its own
   cluster and evolves independently) and with R6's K2 table (the cluster `C ∪ P_in` follows a
   clamped orbit in which `e` and `r_3, …, r_6` depart without a leak). L13(a) reproduces T-IND′.
2. *Favourable reading of Example E.* Every outside site with two or more allowed neighbours is
   listed and its sum computed; the others have one ternary neighbour. Its admissibility rests on
   the decoupling, and it is recorded as a positive result for L13(b) only.
3. *What Theorem D does not exclude.* Absorption in class (b′), and a turn of the pieces' own
   clamped dynamics in classes (b) ∖ (b′) and (a1), are not excluded; both are listed in §6. In both
   the breather's state is NU9 at its initial phase.
4. *Reuse of R6.* Theorem HO uses R6's branch values only up to `T − 1`, as clamped orbits, and
   needs no first-leak claim (L12's remark). The five rows that add sites to R6's are checked in §4.
   R6's L7 is used for segments as in R6 Theorem H(a), applied to `K` alone, with its hypotheses
   as checked there; the further parts do not enter `K`'s clamped orbit.
5. *R6's L8.* It is used only for the two-sided property (admissibility), with the further parts
   carried along as arbitrary states. (b)'s condition is geometric, so the reversed state's
   further parts need no description.
6. *Completeness of the table.* `H11`: 6 + 11 + 2 + 1 = 20 starts; `H10`:
   4 + 2 + 2 + 1 + 1 + 4 + 1 + 1 + 2 + 2 = 20; `H00`: 2 + 1 + 1 + 5 + 9 + 2 = 20.
7. *Window.* Every value used lies in `{−2, …, 3}`.
8. *Cluster definition.* Clusters are taken over all parts. Restricted to `C` and the matched
   pieces, L11 fails (§2's example, followed by hand through tick 5), because an unmatched piece's
   breather-component slots lie in the allowed region. Every statement here uses clusters of all
   parts; class (b) and class 𝒩 exclude unmatched pieces in contact with `C`, as PLAN's class (b)
   does.

**Fixed point.** One pass, with NEW items; the §A.31 fixed point is not reached. Under PLAN's stop
rule the round stops here: the question is answered for classes (b), (a1) and (a2) as stated, and
class (a3) is beyond hand scale, with the exact check described above.
