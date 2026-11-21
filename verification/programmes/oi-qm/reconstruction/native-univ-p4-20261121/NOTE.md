# NATIVE-UNIV, round 4: a non-spreading excursion in Q (P3 stage S1 refuted)

**Standing.** Writer's research record, paper only. Not independently reviewed. It follows
`PLAN.md` (`05c24ddb`), committed first. No computation was run. Every orbit below is derived by
hand, tick by tick.

Base and input heads are as in `PLAN.md`:
- `P2N`: NU3–NU7 and the corrected NU5 reading, #1499 at `36fef943`; NU3 and NU4 confirmed in
  review; not on `main`;
- `F1`: NU1, NU2 and P3's preregistration, #1489, reviewed, not on `main`;
- `PT`: PLANAR-TURN, #1515 at `81bb20bc`;
- U1 and MQ: UNIV-1 and MEAS-Q, on `main`.

**Layer.** Every statement concerns the configuration dynamics of the rounded rule. None is a
statement about effects, instruments, accessible algebras or readouts.

***

## 0. Summary

1. **Proposition NU9 [W, (N)].** In RZ (`y = x − c`) the single-site seed
   `(y_{−1}(0), y_0(0)) = (0, 2)` has a periodic orbit of exact period 10:
   - the support is contained in the cube `{−1, 0, 1}³` at every tick;
   - every value lies in `{−2, …, 2}`;
   - the hull `{0}` is breached at `t = 0`.

   For Q = `R_q` on `ℤ³` this holds at every uniform background `c` with `2 ≤ c ≤ q − 3`, any
   `q ≥ 5`, by U1 Lemma 2.1. Hence:
   - P3 stage S1 is **refuted**;
   - Conjecture S(c) of F1 `plans/P3-PREREG.md` is false at every such `c`;
   - non-spreading excursions ("bounded breaches", P2N NU3) exist in Q, for a single site.

   The seeds `(0, −2)`, `(2, 0)` and `(−2, 0)` have the same property: their orbits are images of
   this one under negation and the shift by 9 ticks.
2. **Structure [W, (N)].** The orbit is a *breather*.
   - The excess at the cube's centre is emitted as a shell: the six face centres at `t = 1`, the
     twelve edge midpoints at `t = 2`, the eight corners at `t = 3`.
   - The rule's symmetry `x_s ↦ −x_{8−s}` (time reversal composed with negation) returns the shell
     to the centre with the opposite sign.
   - The only value outside `[c−1, c+1]` ever is at the cube's centre, which is its only interior
     site. This is as NU3 and NU6(b) require.
3. **Consequence for the decisive question [W].** PT's class (planar, ternary by NU6(c)) excludes
   by construction the mechanism NU9 exhibits. NU9's mechanism is an out-of-range value at an
   interior site of a thick (non-planar) region, which shell-emits and reabsorbs without leaking.
   - A PT result of H0 would therefore not bear on gadgets built from breathers.
   - The next decisive class is thick gadgets with interior excursions. This is a change of which
     class a decisive test must cover (PLAN gem (iii)).
4. **Productivity:** gem by (ii), since S1 is refuted by an explicit orbit, and by (iii).

***

## 1. The orbit

Notation: RZ, `y_{t+1}(i) = G(S_t(i)) − y_{t−1}(i)` with `G(s) = ⌊(s+1)/3⌋` and `S_t(i)` the
sum of `y_t` over the six neighbours of `i`. The site classes, with `e_k` the unit vectors:
- `O = {0}`;
- `E1 = {±e_k}` (6 sites);
- `E2 = {σ_j e_j + σ_k e_k : j < k, σ = ±1}` (12 sites);
- `C3 = {(±1, ±1, ±1)}` (8 sites).

`1_X` is the indicator of `X`.

Values of `G` used: `G(0) = G(1) = 0`, `G(2) = G(3) = G(4) = 1`, `G(6) = 2`, and `G(−s) = −G(s)`
(G is odd: `⌊(1−s)/3⌋ = −⌊(s+1)/3⌋` for every integer `s`, checked on residues mod 3).

**Initial state:** `y_{−1} = 0`, `y_0 = 2·1_O`.

| `t` | `y_t` | derivation (each site class; all other sites have `S = 0` and previous value 0) |
|---|---|---|
| −1 | `0` | given |
| 0 | `2·1_O` | given |
| 1 | `1_{E1}` | `O`: `S_0 = 0`, so `0 − 0 = 0`. `E1`: `S_0 = 2`, so `G(2) − 0 = 1`. Others `S_0 = 0` |
| 2 | `1_{E2}` | `O`: `S_1 = 6`, so `G(6) − y_0 = 2 − 2 = 0`. `E1`: the neighbours of `e_k` are `0`, `2e_k` and `e_k ± e_j`, none in `E1`, so `S_1 = 0` and `0 − 0 = 0`. `E2`: the neighbours `σ_j e_j` and `σ_k e_k` are in `E1`, so `S_1 = 2` and `1`. `2e_k`: `S_1 = 1`, so `0` |
| 3 | `1_{C3}` | `O`: `S_2 = 0` and `y_1(0) = 0`, so `0`. `E1`: `e_k` has four `E2` neighbours `e_k ± e_j` (`j ≠ k`), so `S_2 = 4` and `G(4) − y_1 = 1 − 1 = 0`. `E2`: no neighbour lies in `E2`, so `S_2 = 0` and `0 − y_1 = 0`. `C3`: three `E2` neighbours, so `S_2 = 3` and `G(3) − 0 = 1`. Sites with one coordinate `±2` and one `±1`: one `E2` neighbour, so `S_2 = 1` and `0` |
| 4 | `0` | `E2`: two `C3` neighbours, so `S_3 = 2` and `G(2) − y_2 = 1 − 1 = 0`. `C3`: no `C3` neighbour, so `0 − y_2 = 0`. Sites with one coordinate `±2` and two `±1`: one `C3` neighbour, so `S_3 = 1` and `0`. `O`, `E1`: `S_3 = 0`, `y_2 = 0` |
| 5 | `−1_{C3}` | `S_4 = 0` everywhere, so `y_5 = −y_3` |

**Symmetry.** If `y` is an RZ orbit, so is `w_s := −y_{8−s}`.
*Proof.* By the RZ step at time `8 − s`,
`w_{s+1} = −y_{7−s} = −(G(S(y_{8−s})) − y_{9−s}) = G(S(w_s)) − w_{s−1}`, since `G` is odd and `S`
is linear. ∎

Here `w_3 = −y_5 = 1_{C3} = y_3` and `w_4 = −y_4 = 0 = y_4`. An RZ orbit is determined by two
consecutive slices, forward and backward, so `w = y`, that is, `y_s = −y_{8−s}` for every `s`.
Hence:
- `y_6 = −y_2 = −1_{E2}`;
- `y_7 = −y_1 = −1_{E1}`;
- `y_8 = −y_0 = −2·1_O`;
- `y_9 = −y_{−1} = 0`.

**Period.**
- *A return at `t = 10`.* `y_{10} = G(S(y_9)) − y_8 = 0 + 2·1_O = y_0`. With `y_9 = y_{−1}`, the
  state at `t = 10` equals the state at `t = 0`, so `y_{s+10} = y_s` for every `s`.
- *The period is exactly 10.* It is not 1, 2 or 5, since `y_1 ≠ y_{−1}` and `y_5 = −1_{C3} ≠ y_0`.

**Embedding in Q.** Every value lies in `{−2, …, 2}`. For `2 ≤ c ≤ q − 3` all of `c + y` lie in
`[0, q − 1]`, so U1 Lemma 2.1 (one direction: `3 | 6c`) makes `x = c + y` the orbit of `R_q` from
the seed `(x_{−1}(0), x_0(0)) = (c, c + 2)` on the uniform background `c`. ∎ (Proposition NU9)

**Excursion.**
- *At `t = 0`.* The instantaneous hull is `D_0 = cl₂({0}) = {0}`, a singleton, which is closed. Its
  boundary layer is `{0}`, whose current value `c + 2` is outside `[c−1, c+1]`. This is a breach
  of `D_0` at `t = 0`. By NU4 it radiates out of `D_0` at `t = 1`: the six face centres become
  `c + 1`.
- *At `t = 8`.* There is a breach again, with `c − 2`.

**Negated and shifted seeds.** `−y` is an orbit (G is odd), so the seed `(0, −2)` is periodic too.
The state at `t = 9` is `(y_8, y_9) = (−2·1_O, 0)`, which is the seed `(−2, 0)`. Its negation
gives the seed `(2, 0)`. All four have period 10.

## 2. Skepticism checks (§A.31, PLAN)

1. **Every site that can change is covered at every tick.** A site can be nonzero at `t + 1` only
   if it has a nonzero neighbour at `t` or is nonzero at `t − 1`. The table treats exactly those
   sites:
   - `t + 1 = 1`: `O` and its neighbours `E1`;
   - `t + 1 = 2`: `E1`'s neighbours `O`, `2e_k` and `E2`, and `O`;
   - `t + 1 = 3`: `E2`'s neighbours `E1`, `C3` and the sites with one coordinate `±2` and one
     `±1`, and `E1`;
   - `t + 1 = 4`: `C3`'s neighbours `E2` and the sites with one coordinate `±2` and two `±1`, and
     `E2`.

   Every other site stays 0. From `t = 5` on, the orbit follows from the symmetry.
2. **Consistency with NU3.** The union of supports is the cube `{−1,0,1}³`, which is closed: a
   site outside it has at most one neighbour in it.
   - Its boundary layer consists of every site except the centre. The values there are `±1` and 0,
     all in range, at every tick.
   - The centre is the cube's only interior site and the only site with `|y| = 2`. This is as
     NU3 (a ⇒ c) and NU6(b) require.
3. **Window and representatives.** `|y| ≤ 2` throughout, so no wrap-around enters. The `c` range
   `[2, q − 3]` is what U1 Lemma 2.1 needs for these values.
4. **The proof uses the rule's specific `G` at every step.** The constant rule `F ≡ 2c` of P3-K1
   also has periodic excursions, but by isolation. NU9's orbit uses `G(2) = G(3) = G(4) = 1` and
   `G(6) = 2` to emit and reabsorb.
5. **Consistency with the records on `main`.**
   - MEAS-Q's X2 observations ("every breach observed so far grows") concern the stored S-B
     configurations, and P2N NU7 concerns the axis tips. Neither excludes NU9: the axis tips here
     are `t e_k` with value 0 from `t = 2` on, consistent with NU7.
   - F1's P2 preregistration (`k = 1` shapes, values `{−2,…,2}`) would classify this seed as
     P-exc. That plan is unchanged and unrun.
6. **Remaining risk.** A slip in one table entry would break the symmetry match at `t = 3, 4`. The
   match itself is a check: `w_3 = y_3` and `w_4 = y_4` hold only if `y_3`, `y_4` and `y_5` are as
   computed. An exact run is preregistered (§5) and not run.

## 3. What follows for the decisive question

The decisive question for Q, in P2N's corrected reading (#1499 at `36fef943`), asks for a
leak-free controlled transfer relative to a finite allowed region `lines ∪ R`.
- **PT's class cannot contain NU9's mechanism.** PT restricts to planar regions, where every value
  is ternary (NU6(c)). NU9's mechanism needs an interior site, one whose six neighbours all lie in
  the allowed region, carrying a value of size 2. A planar region has no such site.
- **What NU9 supplies.** A native, bounded, periodic object that disturbs its whole ℓ∞ unit ball
  and returns. Its shell reaches the corners at `t = 3` and `t = 5` (values `±1`) and is otherwise
  inside the cube.
  - Whether a breather placed near a line junction can be triggered by a W2 signal, and can emit
    into a different line, is open. It is a construction question.
  - Under the owner's standard (#1169 c.7066602480 item 4), only an explicit implementation under
    the native rule with encoding, dynamics and correctness would count as a construction. NU9 is
    not one.
- **Reading for test selection, at the level established.** PT's expected H0 concerns planar
  gadgets only, and NU9 shows that native bounded excursions live off the plane. So PT's H0 would
  leave the most promising native mechanism untouched. A next decisive test should cover thick
  gadgets: allowed regions with interior sites, values beyond ternary at interior sites, and
  breathers as candidate parts. This narrows the value of running PT stage 1. It does not by
  itself make PT stage 1 uninformative.

## 4. (N)/(I) and Established / Assumed / Missing

| Result | Label | Status | Established | Assumed (where it enters) | Missing |
|---|---|---|---|---|---|
| NU9: the period-10 orbit of the seed `(c, c+2)`, for `2 ≤ c ≤ q − 3`, `q ≥ 5`, on `ℤ³` | (N) | writer's hand derivation, unreviewed; no off-`main` dependency | the orbit, tick by tick to `t = 5`; the symmetry `y_s = −y_{8−s}`; exact period 10; the excursion at `t = 0` and `t = 8` | native only: `R_q`'s update and U1 Lemma 2.1 (on `main`) | an exact re-run (preregistered, gated) |
| S1 refuted, and S(c) false | (N) | as NU9 | P3's decision rule for refutation (an explicit periodic orbit plus an excursion tick) is met on paper | as NU9; P3's definitions (F1, reviewed) | review |
| §3 reading: PT's class excludes NU9's mechanism | (N) | writer's, unreviewed | NU6(c) (P2N, confirmed in review) applied to PT's planar class | NU6 (not on `main`) | whether breathers can couple to lines (mathematics; a construction question) |

## 5. Preregistered check (not run)

**NU9-CHECK.** Run R_q from the seed `(c, c + 2)` on a periodic `9³` torus. The torus exceeds the
cube plus one site of margin on every side, and the support never leaves the cube, so nothing
wraps.
- **Instances:** `q = 2^16` with `c ∈ {2, 2^15, q − 3}`, and `q = 64` and `q = 256` with
  `c = q/2`.
- **Run length:** 30 ticks.
- **Pass:** the state at `t = 10` and at `t = 20` equals the state at `t = 0` bitwise; `y_t` matches
  the table of §1 for `t ≤ 9`; and no state at `1 ≤ t ≤ 9` equals the state at `t = 0`.
- **Countercontrol (must fail the pass condition):** `c = 1` with `q = 2^16`. At `t = 8` the RZ
  value `−1` at the centre is the representative `q − 1`. At `t = 9` each face centre then has
  neighbour sum `q + 4`, so its value `⌊(q + 5)/3⌋ mod q` differs from `c`. The Q orbit is required
  to differ from `c + y` at `t = 9`, and to fail the return at `t = 10`.
- **Informative:** the linear member `L_{q, 3^{−1}}` from the same seed; no requirement.
- **Cost:** bounded local, under a second. It is a computation, so it needs separate
  authorization.

**Would establish:** an exact run confirming NU9 on the sampled instances. **Would not:** anything
beyond NU9.
