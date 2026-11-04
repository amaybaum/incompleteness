# LA-GAP: proof attempt and counterexample for LA-EQUAL

**Status: WIP / UNVERIFIED. Model-authored by `writer-1007` and not independently reviewed.** No
computation was run. Every step below is either hand algebra on the 8-element table of `H` or integer
arithmetic on coordinates, or it cites a recorded exact check that was read and not re-run. Each such
citation is marked *(recorded, not re-run)*. Paths are relative to
`verification/programmes/substratum/continuous-substates/` unless stated otherwise. `NY/` stands for
`verification/programmes/oi-qm/reconstruction/native-y-continuation-20261024/`. All inputs are on `main`
at `f5c281ae`.

Two kinds of verdict are kept apart throughout:

- **Mathematics:** a statement *proved under H1…Hn*, a *counterexample*, or *open*, with the remaining
  gap stated.
- **Physics:** for each hypothesis, whether native OI *derives* it, *posits* it, or leaves it *open*
  (Q4).

A proof under hypotheses does not derive them.

## Summary of verdicts

| Question | Verdict |
| --- | --- |
| Q0 Statement | Stated exactly below. The displayed hypotheses leave the law of `D′` free. |
| Q1 Pre-cut equality | **Proved under H-pre** (Theorem 1), plus H-rule, H-torus and H-access with its record dictionary. **Counterexample** to the implication from the displayed hypotheses (Theorem 2): with `D′` a point mass, which displayed H-prior permits, a pre-cut public record determines the setting (TV 1). **Open:** whether the specific source-programme law of `D′` gives equality without H-pre. |
| Q2 Forward kernel | **Proved under the parent's 42-key prior** (implied by H-prior), given the parent's recorded geometry. No step is wrong. Three steps are unwritten in the parent and are supplied here (K4′, K6′, K7′). |
| Q3 Composition | **Proved under H-prior⁺** (Theorem 3): `μ_0^{k0} = μ_1^{k0}` for every `k0`, `⊥` included. One direction only. Under the five displayed hypotheses it fails (Theorem 2). |
| Q4 Physics | No hypothesis is derived for native OI. H-pre, H-prior, H-inventory, H-access and H-rule are posited; H-torus is a construction parameter, measured. H-rule is the native-Y rule, not the corpus's selected linear rule. |

***

## Q0. Statement of LA-EQUAL

### Probability space and dynamics

- **Lattice.** The torus `(Z/nZ)^3` with side `n = 256L+64T+1`. The constants are
  `T = 185`, `P = 12·840^185`, `S = P+T`, `R = S+68`, `L = R+9 = S+77`
  (`NY/native_vread_v15/checks.py:27–33`). `dist` is the lattice L1 distance.
- **Sample space.** `Ω` is the set of initial configurations `(U_{-1}, U_0)`, each a map from the torus
  to `{0,1}^3`. Every variable named below is a deterministic function of `ω ∈ Ω`. `P` is a probability
  measure on `Ω`.
- **Rule (H-rule).** `U_{t+1}(v) = U_{t-1}(v) ⊕ H(⊕_{w∼v} U_t(w))`, with
  `H(A,B,D) = (B, D, A ⊕ BD)` (`later-access-preregistration.md:164`).
- **Light cone.** `U_t(v)` depends only on `U_0(x)` with `dist(x,v) ≤ t`, `dist(x,v) ≡ t (mod 2)`,
  and on `U_{-1}(x)` with `dist(x,v) ≤ t-1`, `dist(x,v) ≡ t-1 (mod 2)`. This follows by induction on
  `t` from the rule.

### Variables

- **Ports.** `p_0 … p_7` with frontier cells `f_i(t)`, as in `NY/history_v11/REPORT.md:34–43`. Port 5:
  `p5 = (0,S,0)` and `f_5(t) = (0,S+t,0)`.
- **Setting.** `R = U_{S+4}(p5)`. The setting is `c = R.A`. Its source is the bank cell
  `b5 = f_5(S+4) = (0,2S+4,0)` (`native-random-setting-test.md:40`).
- **Cut.** `τ = L+3` is the use cut. The **pre-cut history** `W_τ` is the public record through `τ`
  under H-access and the probe's record dictionary:
  - every public port's raw triple at every tick `≤ L+3`, including `R`;
  - the old q9 record `U_L(Q9)`, with `Q9 = (0,S,77)`;
  - the V read `U_{L+2}(Q9)`;
  - the herald `U_L(p7)`;
  - the flag and timing cells `U_{R+k}((0,S,68+k))` for `k = 0…9`.

  These are the records of `native_later_access_probe.py:221–224`. The flag dictionary is an
  implementation choice disclosed at `later-access-result.md:105–108`.
- **Incoming packet.** `K0 = K_{L+3}`: fourteen triples, the current (`L+3`) and previous (`L+2`)
  slices on the footprint `Q10 + {0, ±e_x, ±e_y, ±e_z}`, with `Q10 = (0,S,78)`. `K0 = ⊥` in the 16
  terminal source contexts.
- **Future.** `Fut = (K1, K2, ΔW1, ΔW2)`, at `L+4` and `L+5`.
- **Tail.** `Tail` is the raw triple of every port at every tick `L+6 ≤ t ≤ 2L`.
- **Window object.** `X = (R.B, R.D, W_τ∖R, K0, Fut, Tail)`. `A(X)` is `X` without `K0`, `K1` and
  `K2`. Write `W_pre = (R.B, R.D, W_τ∖R)`.
- **Initial-variable blocks** (pairwise disjoint sets of cells of `U_0`):
  - `η`: the 42 parent keys (`native_random_setting_probe.py:60–69`): `b5`; 13 incoming keys; 12
    boundary keys; and the 16 public-bank keys `f_i(L+4)`, `f_i(L+5)`.
  - `β`: the tail bank `f_i(t)`, `L+6 ≤ t ≤ 2L`.
  - `V5`: the pre-cut port-5 bank `f_5(t)`, `S+5 ≤ t ≤ L+3`. These are 76 triples; together with
    `b5` they make 77.
  - `D′`: every initial variable outside `η ∪ β`, so `V5 ⊂ D′`. `D‴ := D′ ∖ V5`.
  - `E := (D‴, η∖{b5}, β)`.

### Hypotheses

- **H-prior** (displayed, `later-access-preregistration.md:151`): `P(η=z, β=b | D′=d) = 8^-(42+|β|)`.
- **H-bank** (named by H-prior's sourcing sentence, `:153–154`; source `NY/history_v11/REPORT.md:23–27`):
  the history_v11 bank `{f_i(t) : a_i < t ≤ 2L}` is uniform conditional on its complement.
- **H-free:** the 25 FREE keys of `η` are uniform conditional on the rest of the complement. This is
  the "inherited independent-uniform complement" of `:153`.
- **H-prior⁺:** `P(η=z, β=b, V5=v | D‴=d) = 8^-(42+|β|+76)`. H-bank and H-free together imply it (chain
  rule). H-prior⁺ implies H-prior, and H-prior implies the parent's prior `P(η | D) = 8^-42`.
- **H-pre** (the weakest form used in Theorem 1): `(b5, V5)` is uniform conditional on `E`. H-prior⁺
  implies it.
- **H-inventory, H-access, H-torus:** as in `later-access-preregistration.md:161–168`.
- **P1–P5, P6a:** the recorded exact preconditions (`later-access-result.md:41–49`) *(recorded, not
  re-run)*. P6b is a sampled mechanism check and is not used below.

### LA-EQUAL

For `c ∈ {0,1}`, `μ_c(x) = P(X=x | R.A=c)`. This is defined because `P(R.A=c) = 1/2` under H-prior:
`R` is a bijective image of `b5` for fixed other variables (Lemma 1), and `b5` is uniform.
`μ_c^{k0}` is `μ_c` restricted to `{K0=k0}`, unnormalized.

> **LA-EQUAL:** for every `k0` in the incoming-packet values and `⊥`, `μ_0^{k0} = μ_1^{k0}`.
> Equivalently, `TV_win(k0) = 0` for every `k0`. Then also `TV_acc(k0) = 0`, and every stop rule on
> `A(X)`-prefixes gives equal laws.

**Verdict Q0.** The statement is fixed as above. The displayed H-prior constrains the law of `(η, β)`
given `D′` and leaves the law of `D′` arbitrary, `V5` included. H-bank is not in the displayed
hypothesis list. The parent's "D" (`native-random-setting-test.md:86`) is `D′ ∪ β`.

***

## Q1. Pre-cut equality

The pre-cut factor is `ν_c^{k0}(w) := P(W_pre = w, K0 = k0 | R.A = c)`. The question is whether
`ν_0^{k0} = ν_1^{k0}`.

### Lemma 1 (port-5 word is a bijective image of its bank)

For every fixed value of `E`, the map `(b5, V5) ↦ P5 := (U_t(p5))_{S+4 ≤ t ≤ L+3}` is a bijection
of `({0,1}^3)^77`.

*Proof.*

1. **Triangular.** `dist(f_5(t′), p5) = t′`. By the light cone, `U_t(p5)` does not depend on
   `f_5(t′)` for `t′ > t`. So `U_t(p5)` is a function of `E` and of `f_5(t′)` for `t′ ≤ t`.
2. **Diagonal.** Fix `E` and `f_5(t′)` for `t′ < t`, and let `u = U_0(f_5(t))`. Take the axial path
   `x_s = f_5(t) − s·e_y`, `s = 0…t`, so `x_0 = f_5(t)` and `x_t = p5`. For `s ≥ 1`,

       U_s(x_s) = α_s ⊕ H(U_{s-1}(x_{s-1}) ⊕ β_s),

   where `α_s = U_{s-2}(x_s)` and `β_s = ⊕_{y∼x_s, y≠x_{s-1}} U_{s-1}(y)`. Neither depends on `u`:
   - `dist(x_s, x_0) = s > s−2`. At `s = 1`, `α_1 = U_{-1}(x_1)` is an initial variable other than `u`.
   - Every neighbour `y ≠ x_{s-1}` of `x_s`, whether `x_{s+1}` or one of the four transverse ones, has
     `dist(y, x_0) = s+1 > s−1`.

   With `H` bijective (P6a), each step `v ↦ α_s ⊕ H(v ⊕ β_s)` is a permutation. So `U_t(p5)` is a
   composition of permutations applied to `u`. Distances are the unwrapped lattice distances by H-torus
   (P5), since `2(L+3)` is less than the side.
3. **Conclusion.** A triangular map with bijective diagonal is a bijection: invert in increasing `t`. ∎

This is the history_v11 inversion (`NY/history_v11/REPORT.md:98–108`), restricted to port 5's ticks
`S+4 … L+3`. The equal-time edges `2→5` and `3→5` bring `f_2(t)` and `f_3(t)` into `U_t(p5)`, but
those triples are in `E` and are fixed.

### Lemma 2 (exclusion, hand arithmetic on coordinates)

`b5` and `V5` reach no pre-cut record other than port 5's own ticks `≥ S+4`. That is, for every
`S+4 ≤ t ≤ L+3` and every record `(y, s)` of `W_τ` or `K0`, other than `(p5, s ≥ S+4)`,
`dist(f_5(t), y) > s`.

*Proof.* Write `f_5(t) = (0,S+t,0)` with `t ≥ S+4`, and recall `L+3 = S+80 = P+265`.

| Record `(y, s)` | `dist(f_5(t), y)` | Comparison |
| --- | --- | --- |
| `p5`, `s ≤ S+3` | `t` | `t ≥ S+4 > s` |
| `p0 = (0,T,0)`, `s ≤ L+3` | `S+t−T = P+t` | `> P+265` |
| `p1 = (0,0,−8T)` | `S+t+8T` | `> L+3` |
| `p2 = (T,P,0)`, and `p3` likewise | `T+(S+t−P) = 2T+t = 370+t` | `> S+80` |
| `p4 = (4T,P,0)` | `5T+t` | `> L+3` |
| `p6 = (12R,0,0)`, `p7 = (48L,0,0)` (herald included) | `≥ S+t` | `> L+3` |
| `Q9 = (0,S,77)` at `L` and `L+2` | `t+77 ≥ S+81` | `> L+2 = S+79` |
| flag `(0,S,68+k)` at `R+k = S+68+k` | `t+68+k` | `> S+68+k` |
| `K0` footprint at `L+3` and `L+2` | `min = t+77 ≥ S+81` | `> L+3` |

The footprint minimum is attained at `(0,S+1,78)` and `(0,S,77)`. At `t = S+4` the margins 1 (`K0`)
and 2 (`Q9`) agree with the recorded CP-PRECUT values `b5_to_K0_slices_minus_tau = 1` and
`b5_to_q9_minus_L2 = 2` (`later-access-result.json`). The `⊥` label is the terminal source context. It
is a function of source cells, and `b5` and `V5` are not source cells: for `b5` this is the parent's
check (`native_random_setting_probe.py:73`); for `V5`, it is history_v11's bank/source distinctness
(`NY/history_v11/REPORT.md:67–81`) *(recorded, not re-run)*. ∎

### Theorem 1 (pre-cut equality; proved under H-pre)

Assume H-pre, H-rule with P6a, H-torus with P5, and H-access with the record dictionary of Q0. Then for
every `w` and every `k0`, `⊥` included, `ν_0^{k0}(w) = ν_1^{k0}(w)`.

*Proof.*

1. By Lemma 2, `Rest := (W_τ ∖ (U_t(p5))_{t ≥ S+4}, K0)` is a function of `E`.
2. By H-pre and Lemma 1, `P5` is uniform on `8^77` values conditional on `E`, and hence independent of
   `(E, Rest)`.
3. For every value `c` of `R.A`, every value `p′` of `P5` with `R.A` deleted, and every `ρ`:
   `P(R.A=c, P5′=p′, Rest=ρ) = 8^-77·P(Rest=ρ)`.
4. Therefore `P(R.A=c) = 1/2` and `P(P5′=p′, Rest=ρ | R.A=c) = 2·8^-77·P(Rest=ρ)`, which does not
   depend on `c`.
5. `(W_pre, K0)` is a function of `(P5′, Rest)`, so the pushforwards agree. ∎

Theorem 1 uses neither the parent kernel nor P1–P4. Its only probabilistic input is H-pre.

### Theorem 2 (counterexample to the implication from the displayed hypotheses)

Let `D′` be the point mass at the all-zero configuration: `U_{-1} ≡ 0`, and `U_0 = 0` on every cell
outside `η ∪ β`. Let `η` and `β` be uniform and independent of `D′`, so H-prior holds as displayed.
H-rule, H-torus, P1–P5 and P6a do not involve the law of `D′` and hold as recorded. H-inventory and H-access concern the declared inventory and the read convention, not the law of
`D′`; whether "the original preparation" requires the source-programme law is the question this
theorem isolates (see below). Let
`Y = (R.B, R.D, U_{S+6}(p5))`. `Y` is a coordinate function of `A(X)`, since port 5's raw triple at
`S+6 ≤ L+3` is in `W_τ`. Then the laws of `Y` given `c = 0` and `c = 1` have disjoint supports:

| `(R.B,R.D)` | `c=0`: `R` | `U_{S+6}(p5)` | `c=1`: `R` | `U_{S+6}(p5)` |
| --- | --- | --- | --- | --- |
| `(0,0)` | `000` | `000` | `100` | `001` |
| `(0,1)` | `001` | `010` | `101` | `101` |
| `(1,0)` | `010` | `110` | `110` | `001` |
| `(1,1)` | `011` | `100` | `111` | `111` |

Triples are written `ABD`. Given `c`, `R` is uniform on its four rows. In particular
`P(Y = (0,0,000) | c=0) = 1/4` and `P(Y = (0,0,000) | c=1) = 0`, and `TV(Law(Y|c=0), Law(Y|c=1)) = 1`.
Since `Y` is a function of `A(X)` and the `K0`-classes partition `Ω`,
`Σ_{k0} TV_acc(k0) = Σ_{k0} TV_win(k0) = 1`. So LA-EQUAL fails for this law of `D′`.

*Proof.*

**(a) Only `b5` is non-zero in the relevant ball.** `U_{S+4}(p5)` and `U_{S+6}(p5)` depend only on
initial cells in the ball `B(p5, S+6)`. Every `η` key other than `b5`, and every `β` triple, lies
outside it. Write `t′` for the key's own first-arrival time.

- 13 incoming keys and 12 boundary keys (coordinates from `native_random_setting_probe.py:60–68`):
  `dist(key, p5) ≥ t′+77 ≥ L+79`. The incoming value 152 is recorded as
  `incoming_keys_to_R_minus_S4`.
- 16 public-bank keys `f_i(t′)`, `t′ ∈ {L+4, L+5}`: `dist ≥ t′`. Port 5 is axial, ports 2 and 3 give
  exactly `t′`, and the other ports are farther, by the table of Lemma 2.
- `β`: `dist ≥ t′ ≥ L+6`, by the same table. P1 is recorded as well.

So inside the ball, the configuration is the single seed `x = U_0(b5)` on a zero background. The ball
does not wrap (H-torus), so the values equal those of the single-seed world on `Z^3`.

**(b) Single-seed recursions.** Place the seed at the origin and look along the `−e_y` axis. Outside the
light cone, and at the wrong parity, the values are `0`, since `H(000) = 000`.

- *Front.* At axial distance `t` and time `t`, the only non-zero neighbour at `t−1` is the preceding
  axial vertex, so `F_t = H(F_{t-1}) = H^t(x)`.
- *Two behind the front.* At axial distance `t−2` and time `t`, the value is

      B_t = F_{t-2} ⊕ H(F_{t-1} ⊕ B_{t-1}),   t ≥ 3,   B_2 = x.

  The neighbours at `t−1` are the outer axial vertex (`F_{t-1}`), the inner axial vertex (`B_{t-1}`),
  and four transverse vertices on the front. The four transverse vertices are equal by the lattice
  symmetries fixing the axis, which commute with the rule, so their XOR is `0`. `B_2 = x`, because
  the six neighbours of the seed each equal `H(x)` at `t = 1`, and six equal terms XOR to `0`.

`p5` lies at axial distance `S+4` from `b5`. So `R = F_{S+4}` and `U_{S+6}(p5) = B_{S+6}`.

**(c) Reduction to `t = 9, 11`.** `H` has cycles `(000)`, `(001 010 100)` and
`(011 111 110 101)`, so its order is 12. For each `x` with `H`-cycle length `m`:

- the state `(t mod m, B_t)` evolves by a permutation, because `B_{t-1} ↦ B_t` is bijective for each
  `t`;
- so the sequence is purely periodic. Its period is 15 for `x` in the 3-cycle (`(2,100)` recurs at
  `t = 17`) and 12 for `x` in the 4-cycle (`(2,011)` and `(2,110)` recur at `t = 14`).

Since `60 | 840`, `P ≡ 0 (mod 60)` and `S ≡ 185 ≡ 5 (mod 60)`. So `S+4 ≡ 9` and `S+6 ≡ 11 (mod 60)`,
which gives `R = F_9 = H^9(x)` and `U_{S+6}(p5) = B_11`.

**(d) Hand table.** These values are read from the 8-entry table of `H`:

| `x` | `B_2 … B_11` | `R = H^9(x)` | `B_11` |
| --- | --- | --- | --- |
| `000` | all `000` | `000` | `000` |
| `001` | 001 001 100 100 010 011 011 100 111 010 | `001` | `010` |
| `010` | 010 011 011 100 111 010 111 001 110 110 | `010` | `110` |
| `100` | 100 100 010 011 011 100 111 010 111 001 | `100` | `001` |
| `011` | 011 100 100 011 010 110 001 001 110 111 | `111` | `111` |
| `111` | 111 010 111 011 100 100 011 010 110 001 | `110` | `001` |
| `110` | 110 110 001 001 111 100 100 011 011 101 | `101` | `101` |
| `101` | 101 111 101 110 110 001 001 111 100 100 | `011` | `100` |

The periods used in (c) come from continuing these rows. For `x = 100`, `B_12 … B_17` is
`110 110 010 001 001 100`. For `x = 011` and `x = 110`, `B_12 … B_14` is `010 111 011` and
`111 101 110`.

Each entry was cross-checked against `B_11 = R ⊕ H(F_10 ⊕ B_10)`. Re-indexing by `R` gives the table
in the statement. ∎

**What Theorem 2 shows, and what it does not.**

- It refutes the implication "displayed H-prior, H-rule, H-torus, H-access and P1–P6a imply LA-EQUAL".
  The step that needs more is the pre-cut equality.
- The steps S3–S6 of the LA argument (tail uniformity and `EMPTY`) hold for every fixed value of `D′`.
  The pre-cut equality does not.
- The point mass is not the original preparation: it zeros the source programme inside `B(p5, S+6)`.
  Theorem 2 is therefore not a counterexample to LA-EQUAL under H-prior⁺ (Theorem 3), nor under the
  original source-programme law of `D′`.
- The setting enters `U_{S+6}(p5)` in all three components, not only through
  `A = R.A ⊕ Σ.B`. The `A` bit alone gives TV `1/2` here: the rows `(0,0)` and `(1,1)` agree on it.

### Remaining gap in Q1

Equality for the specific original law of `D′`, the source programme with `V5` not uniform, is
**open**. It depends on the background inside `B(p5, S+6)`, which is astronomical. No bounded exact
computation decides it, and none is proposed.

**Verdict Q1.**

- **Proved under H-pre** (Theorem 1), with H-rule (P6a), H-torus (P5) and H-access with its record
  dictionary.
- **Counterexample** to sufficiency of the displayed hypotheses (Theorem 2, TV 1).
- **Open** for the unmodified source-programme law without H-pre.

***

## Q2. Audit of the parent forward-kernel proof (`native-random-setting-test.md:67–127`)

The claim (`:109–110`) is
`P(K1,K2,ΔW1,ΔW2 | K0=k0, W_τ=w, R=r) = 8^-28·S(k0,k1)·S(k1,k2)` in every positive-mass continuing
branch.

**K1 (`:69–84`). 42 keys; own uniquely axial paths; triangular graph; bijective diagonals.**
Valid, given the recorded geometry.

- The probe checks, for each row, that the distance equals `t` and that the key differs from its site
  in one coordinate. It checks that no key reaches an earlier label (`min(affected) == i`, using the
  conservative `dist ≤ t` without parity). It also checks distinctness, the class, and exclusion from
  `Q`. See `native_random_setting_probe.py:69–78` *(recorded, not re-run)*.
- The diagonal argument is the one in Lemma 1(2). It needs only that the off-path neighbours are
  farther, which holds for any axial path.
- Hand-checked here: the key coordinates (`:59–64`), and that the K0 centre at `L+3` is fixed by `Q`.

**K2 (`:86–93`). Prior `P(η | D) = 8^-42`.** A hypothesis. It is implied by H-prior, and hence by
H-prior⁺.

**K3 (`:95–102`). Joint law.** Valid.

- For fixed `d`, the label map from `η` is injective by K1.
- Its image lies in the compatible set `{π(k0) = Q(d), S(k0,k1), S(k1,k2)}`:
  - `π(K0) = U_{L+3}(Q10) ⊕ H(⊕ U_{L+2}(Q10+e)) = U_{L+1}(Q10) = Q`, which no key reaches (`native_random_setting_probe.py:78`).
  - The `K1` previous slice is the `K0` current slice.
  - The `K1` centre is `U_{L+2}(Q10) ⊕ H(⊕ U_{L+3}(Q10+e))`, a function of `K0`.
- The compatible set has `8·8^13·8^14·8^14 = 8^42` elements. That is 6 boundary and 8 port triples free
  per step, and 13 free `K0` coordinates.
- An injective map between sets of equal size is a bijection, so the uniform prior gives the displayed
  mass. The parent leaves the cardinality step implicit.

**K4 (`:104–110`). Conditioning on `(K0, R, D)`.** Valid. Marginalizing gives
`P(R=r, K0=k0 | d) = 8^-14·1[π(k0)=Q(d)]`, and dividing gives `8^-28·S·S` for every `d`.

**K4′ (unwritten in the parent; supplied here). From `D` to `W_τ`.** Valid, under one recorded
exclusion.

- The kernel is stated conditional on `W_τ`, not on `D`. This passage is valid because
  `W_τ ∈ σ(D, R, K0)`:
  - the 28 future keys reach no pre-cut record: footprint, ports and `Q9` are checked at
    `native_random_setting_probe.py:96–100` *(recorded)*; the flags follow by hand, since
    `dist(key, Q10) ≥ L+4` and `dist(Q10, (0,S,68+k)) = 10−k` give `dist ≥ R+3+k > R+k`;
  - for fixed `d`, `(b5, incoming keys) ↦ (R, K0)` is a bijection (K3).
- The kernel given `(K0, R, D)` does not depend on `d`, so averaging over `d` given
  `(K0=k0, W_τ=w, R=r)` leaves it unchanged.
- Hand-checked: the incoming keys reach no flag cell. `dist(key, (0,S,68+k)) ≥ dist(key, Q9) − (9−k) > R+k`,
  using the recorded `dist(key, Q9) > L` (`native_random_setting_probe.py:90–93`).

**K5 (`:112`). "The same for every r, hence for both c".** Valid as a statement about the kernel. It
does not imply equality of the setting-conditioned history masses, and the parent does not claim that
it does. The LA preregistration bars that substitution (`later-access-preregistration.md:139–140`).

**K6 (`:120–127`). The pre-cut history is a function of `r` and `V` for fixed `D`.** Valid given the
recorded exclusions. `V = U_{L+2}(Q9)` is the label `B2:4`, a coordinate of `K0`
(`native_random_setting_probe.py:94–95`).

**K6′ (supplied here).** K6 is the source of the LA gap: "for fixed `D`" makes the pre-cut history a
function of `r`. Its law given `c` then depends on the law of `D`, which K2 leaves free (Theorem 2).

**K7′ (unwritten in the parent; supplied here). Terminal contexts.** Valid. The joint formula covers
continuing branches only.

- For `k0 = ⊥` the 16 public-bank keys still determine `ΔW1` and `ΔW2` through the same triangular
  rows, since the geometry does not depend on the context.
- So `P(ΔW1, ΔW2 | W_τ, K0=⊥, R) = 8^-16`, with `K1` and `K2` absent.

**Verdict Q2.** **Proved under the parent's prior** (implied by H-prior), H-rule (P6a) and H-torus, given
the recorded 42-row geometry *(recorded, not re-run)*. No step is in error. Steps K4′, K6′ and K7′ are
written here for the first time. The kernel does not need H-pre.

***

## Q3. Composition

### Theorem 3 (LA-EQUAL; proved under H-prior⁺)

Assume H-prior⁺, H-rule with P6a, H-torus with P5, H-access with the record dictionary of Q0, the
recorded P1–P4, and the parent's recorded 42-row geometry. Then `μ_0^{k0} = μ_1^{k0}` for every `k0`,
`⊥` included.

*Proof.* By the chain rule, for each `(w′, k0, f, y)`:

    μ_c^{k0}(w′, f, y) = ν_c^{k0}(w′) · P(Fut=f | W_pre=w′, K0=k0, R.A=c) · P(Tail=y | W=w, R.A=c)

The second factor is defined when the first is positive, and the third when the product of the first
two is positive. Each factor in turn:

1. **Pre-cut factor.** `ν_c^{k0}(w′)` does not depend on `c`, by Theorem 1. H-prior⁺ implies H-pre.
   Positivity of the conditioning event therefore does not depend on `c` either.
2. **Future factor.** The event `{W_pre=w′, K0=k0, R.A=c}` equals `{W_τ=w, K0=k0, R=r}` with
   `r = (c, w′.B, w′.D)`. By Q2 (K3, K4, K4′) it equals `8^-28·S(k0,k1)·S(k1,k2)` for `k0 ≠ ⊥`, and by
   K7′ it equals `8^-16` for `k0 = ⊥`. Neither depends on `c`.
3. **Tail factor.** By S3 and S4 of the review reconstruction (`LA-EQUAL-REVIEW.md:299–308`):
   - P1, P4 and the Lemma 1 argument make `β ↦ Tail` triangular with bijective diagonal, for fixed
     `(D′, η)`;
   - H-prior (implied by H-prior⁺) gives `P(Tail=y | D′, η) = 8^-|β|`;
   - by P2, `W` and `R.A` are functions of `(D′, η)`.

   So the factor equals `8^-|β|`.

Hence `μ_c^{k0}(w′, f, y) = ν^{k0}(w′)·κ_{k0}(f)·8^-|β|` whenever both conditioning events are
positive, and both sides are `0` otherwise. The expression does not depend on `c`. ∎

### Directionality (§A.34) and scope

- Theorem 3 is one implication: the hypotheses imply equality.
- No converse is claimed. The token rule "LA-EQUAL iff P1–P6b" (`later-access-preregistration.md:205`)
  defines when a token is printed; it is not a mathematical equivalence.
- Theorem 2 shows that the implication fails when H-prior⁺ is weakened to the displayed H-prior.
- P6b is not used.
- `EMPTY` uses only H-prior and is unaffected.
- The sentence that the equality "has the same cause as its emptiness" (`:257–259`;
  `later-access-result.md:32–33`) holds for the tail factor only. The cause of the pre-cut factor is
  the port-5 bank masking under H-pre.

**Verdict Q3.**

- **Proved under H-prior⁺** (Theorem 3), together with H-rule, H-torus, H-access and its dictionary,
  the recorded P1–P5 and P6a, and the parent's recorded geometry.
- Under the five displayed hypotheses: **counterexample** (Theorem 2).
- No conditioning event of zero probability is used.

***

## Q4. Mathematics versus physics

| Hypothesis | Mathematical role | Physical standing in native OI |
| --- | --- | --- |
| **H-pre / H-prior⁺** (contains H-bank on `b5` and `V5`) | Load-bearing for the pre-cut factor: Theorem 2 fails it and Theorem 1 uses it. | **Posited.** history_v11 supplies its bank as "an explicit resource extension … supplied assumptions rather than derived physical laws" (`NY/history_v11/REPORT.md:23–27`). Not derived; whether native OI supplies it is open. |
| **H-prior** (displayed) | Tail factor, `EMPTY` and the parent kernel. | **Posited**, from the same source. It is load-bearing: CP-PRIOR gives TV `1/8` when the prior is correlated. |
| **H-free** (with H-bank, implies H-prior⁺) | Covers the FREE keys' uniformity. | **Posited** ("inherited independent-uniform complement"). |
| **H-inventory** | Not used in any proof step here. It underwrites that the record set and source inventory are as listed. | **Posited:** a declared completeness condition of the construction. |
| **H-access** and the record dictionary | Defines `W_τ`, `A(X)` and the passive no-write read. Lemma 2 is relative to this dictionary. | **Posited:** a retained candidate convention, not adopted (`later-access-preregistration.md:68–75`). A different flag or timing set could change Lemma 2. |
| **H-rule** | Bijectivity of `H` (P6a) in Lemma 1, the parent kernel and the tail. The specific `H` is used in Theorem 2. | **Posited model rule of native-Y.** It is not the corpus's selected dynamics: center independence, isotropy and linearity give the linear rule `x_i(t+1) = α Σ_{j∼i} x_j(t) − x_i(t−1)` (`papers/SM.md:224`), and `H` is nonlinear. Theorems 1 and 3 use only bijectivity of the update. Theorem 2's table is specific to this `H`. No statement here transfers to OI's selected rule without a new argument. |
| **H-torus** | No wrap; the distances are lattice distances. | A construction parameter, measured exactly by P5 *(recorded)*. Finiteness of the substratum is posited. |
| **P1–P5, P6a** and the parent's 42-row geometry | Geometric premises. | Exact finite computations *(recorded, not re-run, not independently reviewed)*. Parts used here were re-derived by hand: Lemma 2, Theorem 2(a), and the K0, Q9 and flag distances. |

**Verdict Q4.** None of the hypotheses is derived for native OI. Theorem 3 is a conditional
mathematical theorem about the native-Y model under posited resources. It is not a physical derivation,
and it says nothing about OI's selected linear dynamics.

***

## Proposed computations (not run; each needs separate owner authorization)

### PC-1: exact replay of Theorem 2 on a small native world

Theorem 2(c) reduces the actual scale to distance 9 exactly, so this world reproduces the
actual-scale values.

- **Inputs.**
  - The pinned rule `H` (`native_random_setting_probe.py:27–29`).
  - A cubic lattice region containing `B(p, 12)`, with `p = (0,0,0)` and seed cell `s = (0,9,0)`.
  - Zero background in both slices, and seed value `x ∈ {0,1}^3`.
- **Enumerates.** The 8 seed values, with direct six-neighbour evolution to `t = 11`. This uses no
  recursion formula.
- **Records.** `R = U_9(p)` and `Y = (R.B, R.D, U_11(p))`.
- **Decision rule.** Pass if the 8 rows equal the table in Theorem 2, and the exact Fraction TV between
  the classes `R.A = 0` and `R.A = 1` equals `1`. Otherwise report the mismatch.
- **Controls.**
  - **C1 (masking countercontrol).** Add independent uniform triples at `(0,10,0)` and `(0,11,0)`, the
    analogues of `f_5(S+5)` and `f_5(S+6)`, and enumerate `8^3`. The TV of `Y` must be exactly `0`.
    This is Theorem 1's mechanism.
  - **C2.** Direct evolution must equal the `F_t` and `B_t` recursions for all `t ≤ 40` and all `x`.
  - **C3.** Iterating the state maps must give periods 15, 12 and 12, and exact integer arithmetic must
    give `S mod 60 = 5`.
  - **C4 (null).** Two identical laws must give TV `0`.
  - **C5 (mutant).** With `H` replaced by the identity, the table must change. This shows the check is
    not vacuous.
- **Arithmetic and cost.** Exact integers and Fractions only. Seconds-scale, standard library.
- **Not decided by it.** The original-preparation law (Q1, remaining gap).

### PC-2: exact recheck of Theorem 2(a) and Lemma 2

- **Computes.** Integer distances from every `η∖{b5}` and `β` cell to `p5` (minimum over the `β` rays
  at endpoints and breakpoints), and from `f_5(t)`, `S+4 ≤ t ≤ L+3`, to every pre-cut record.
- **Decision rule.** The strict inequalities above.
- **Control.** A ray placed at distance exactly `s` must fail.

***

## Literature

No external result is used. The steps are a triangular map with bijective diagonal (inverted
sequentially), the fact that a bijection pushes the uniform law to the uniform law, and the chain rule
for discrete conditional probability. No literature search was needed or made.

## For review

The exact head SHA is given in the PR description. A reviewer should check:

1. Lemma 1(2): that `α_s` and `β_s` do not depend on `u`.
2. Lemma 2: the coordinate table, against `NY/native_vread_v15/checks.py:27–33` and `:377–381`.
3. Theorem 1, steps 1–5: that `Rest` is `E`-measurable, including the `⊥` context.
4. Theorem 2:
   - (a) the key coordinates against `native_random_setting_probe.py:60–68`;
   - (b) the `B_t` recursion and the transverse-symmetry step;
   - (c) the permutation and periodicity argument, and `S mod 60 = 5`;
   - (d) every table entry, against `H`'s 8-entry table.
5. Q2, K3: the cardinality step. K4′: `W_τ ∈ σ(D, R, K0)`.
6. Theorem 3: the factor order and the positivity conditions.
7. Q4: each standing, against the cited sources.
