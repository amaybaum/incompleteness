# TUNE-1, Step 2, session 4: the R-nl branch (L5/M3 under H-nl)

**WIP / UNVERIFIED research record.** Paper derivation only; no interpreter or numerical
computation was run. No manuscript or Lean file is changed, no premise is adopted, and nothing is
frozen, dispatched or merged. An independent internal review (same model family) returned ACCEPT
WITH CHANGES at `69a92592`; its required and minor items, and the owner decisions below, are
applied here. The record goes to a focused internal re-check and then to ChatGPT review.

**Authorization.** The owner authorized this work on PR #1237, comment 6824440978 (`amaybaum`,
author association `OWNER`, 2026-11-12T13:06:41Z): "R-nl branch: 'Start after review
(Recommended)'. R-nl (choice 1(b), under H-nl) starts as paper-only work once ChatGPT has reviewed
Session 3." The same comment records L5.4 and L5.5 as "Record and leave (Recommended)"; this
session does not work on them. The review gate is met: ChatGPT review 5875006206 of Session 3 at
`53ec4898` (ACCEPT WITH SCOPE QUALIFICATIONS) states that "that independent review gate is now
met, subject to the existing named H-nl and all governance limits."

**Governing text:**
- the proposal at `e676c42a` (sha256 `2a081101…7499fd5`, checked at the start of this session);
- `TUNE-1-STEP2-AMENDMENT-1-final.md`;
- addenda 1 and 2.

Q-conditions are Q1, Q2, Q3′, Q4, Q5′ and Q6′; `F(ε; 𝒯′)`, credited assignments, admissibility,
the separation length `L` and constant `c₀` are as in the final amendment (B1). Labels are [K],
[P], [R] and [W]. Every derivation here is [W] unless tagged otherwise.

**Notation.** `L` always denotes the family's separation length (final B1.3 (ii), `L ≥ 2`). The
side of a torus is written `L_tor`, and the torus is `Λ_{L_tor} = (ℤ/L_tor ℤ)^3` (the proposal's
`Λ_L`, §1.2).

**R-nl and H-nl, as frozen** (proposal §1.1, choice 1(b) recorded at M0 in Session 1):
- **R-nl** is the rounded bijection of SM:294,
  `x(t+1) = ⌊(Σ_nn x(t) + 1)/3⌋ − x(t−1) mod q`, evaluated on the representatives `0, …, q − 1`.
  In the second-order form of proposal §1.1 it is `Φ(y, x) = (x, g(x) − y)` with
  `g(x)_i = h(s_i(x)) mod q`, `s_i(x) = Σ_{j ∈ nn(i)} x_j` (integer sum of representatives over the
  six nearest neighbours) and `h(s) = ⌊(s + 1)/3⌋`. The formula was checked against SM:294 at the
  Step 1 pin `cac5d264`.
- **H-nl** is the named hypothesis "the world's rule is R-nl". It replaces ledger item (vii) for
  this subclass, is carried into every conclusion that uses it, and is not adopted (proposal
  §1.1, §6).

**Controls.** All seventeen M1 controls are green under the governing text (Session 2, and its
C-POS-2 rerun with G1 closed), and the L5 proves-too-much row is green (Session 3 §4). Any new
negative argument of this session gets its own proves-too-much row (§4).

**Effort bound.** Choice 10(a) fixed three writer sessions with reviews; this is the fourth. The
owner extended choice 10(a) to it on PR #1237, comment 6825956102 (`amaybaum`, author association
`OWNER`, 2026-11-12T14:12:24Z):

> 1. Effort bound: "Extend 10(a) to cover it (Recommended)". This extends choice 10(a) to a fourth
> writer session, for R-nl only. H1–H4 are then applied and the session goes to ChatGPT review.

The tokens of §5 are therefore reported within the effort bound as extended. The same comment
records owner decisions 2–4, quoted where they are applied (§1.6, §5.2 and §5.1 respectively).

***

## 0. Productivity test (§A.31), fixed before the node derivations

The R-nl branch is a **gem** iff it yields a fact that is strictly stronger than the restatement

> "Lemma A-T's proof uses R-lin's linearity, so FC-1 and FC-2 do not cover R-nl"

and that fact either
- (a) constrains R-nl families: a `FAIL-CLASS` for a stated subclass, or an explicit necessary
  condition on any family that meets Q3′, Q5′ and Q6′; or
- (b) exposes a hidden assumption in the governing text or in Sessions 1–3.

Otherwise the branch is a non-gem, and its results are recorded only. The propagation bar is
better-than-coherence: a relabelling of an existing statement is recorded and not propagated.

**Node plan (depth-first).**
- NL.1: transfer of Session 3 to R-nl, item by item, with the exact step at which nonlinearity
  breaks Lemma A-T, and whether the conclusion (not only the proof) fails.
- NL.2: the decisive branch. Is there an obstruction for R-nl families? First the R-lin route (an
  exact dichotomy), then its weakenings, then obstructions that do not use the rule at all.
- NL.3: the constructive side (Route P): what a `PASS-DERIVED` on R-nl would need.
- NL.4: the child splits of Session 3 (heralds, adaptivity, laws), read for R-nl.
- Tokens by proposal §2.2, over green controls.

***

## 1. Transfer of Session 3 to R-nl (node NL.1)

### 1.1 Two lemmas used below

**Lemma NA (R-nl is not affine)** [W].
- *Statement.* For every `q ≥ 2`, on `Λ_{L_tor}` with `L_tor ≥ 3` and on `ℤ^3`, the map `g` is
  not additive, and `Φ` is not affine.
- *Proof.* Let `n₁ ≠ n₂` be two neighbours of a site `o`, and let `x = δ_{n₁}`, `x′ = δ_{n₂}` (value
  1 at one site, 0 elsewhere). Then `s_o(x) = s_o(x′) = 1` and `s_o(x + x′) = 2`. Since `h(1) = 0`
  and `h(2) = 1`, `g(x + x′)_o − g(x)_o − g(x′)_o = 1 ≠ 0 mod q`. Also `g(0) = h(0) = 0`, so
  `Φ(0, 0) = (0, 0)`, and an affine `Φ` fixing `0` would be additive, which needs `g` additive. ∎

**Lemma M (one-time pad, every second-order rule)** [W].
- *Statement.* Let `Φ(y, x) = (x, G(x) − y)` for any map `G`. Let `U` be a set of cells whose
  previous components `y_U(0)` are uniform on `V^U` and independent of the rest of the time-0
  configuration. Then `x_U(1)` is uniform on `V^U` and independent of `x(0)` and of `y_{Λ∖U}(0)`.
- *Proof.* `x_U(1) = G(x(0))_U − y_U(0)`. Conditional on `(x(0), y_{Λ∖U}(0))`, this is a fixed
  translate of a uniform variable, hence uniform. ∎
- Under the uniform law (uniform product law on `ℤ^3`) it applies with `U` the unread cells, in
  both modes.

### 1.2 Where nonlinearity breaks Lemma A-T

Lemma A-T's proof step 1 states that `Φ_F` is a group endomorphism. For R-nl this is false by
Lemma NA. Every later part rests on it:
- (a) and (b) need the record to be a homomorphic image of the configuration plus a translation;
- (c) applies Lemma 0 to that homomorphism;
- (d) follows from (c).

Lemma 0 itself holds (it is a statement about finite abelian groups), but for R-nl it has no
input.

**The mechanism.** Take a site `i` and write `x_i(2) = G(x(1))_i − x_i(0)`. By Lemma M, the
unread neighbours of `i` carry fresh uniform values at time 1, so `G(x(1))_i` is a function of a
label-dependent part `a` and a fresh sum `S`.
- For R-lin, `G(x(1))_i = a + S`. This is a homomorphic image of `S` translated by `a`. By Lemma 0
  it is uniform on a coset, and a change of `a` translates the coset.
- For R-nl, `G(x(1))_i = h(a + S) mod q`. Here `h` is not a homomorphism, and the law of
  `h(a + S)` depends on `a` other than by translation (tables T2 and T3 below).

So linearity enters Lemma A-T exactly at the pad. In R-lin, the fresh variables reach the record
through a homomorphism, which leaves two cases: the label is hidden completely, or it shifts the
record. In R-nl, the composite `h ∘ Σ` hides a label only partially.

### 1.3 The conclusion fails, not only the proof

**Hand counts used** (each checked by its total).
- `q = 2`: `S_k`, the sum of `k` independent uniform bits, has counts `(1,4,6,4,1)/16` for `k = 4`,
  `(1,5,10,10,5,1)/32` for `k = 5`, `(1,6,15,20,15,6,1)/64` for `k = 6` and `(1,3,3,1)/8` for
  `k = 3`. For `s ≤ 6`, `h(s)` is odd exactly when `s ∈ {2, 3, 4}`.
- `q = 3`: `S_5`, the sum of five independent uniform values in `{0, 1, 2}`, has the coefficients of
  `(1 + z + z²)^5`: `(1, 5, 15, 30, 45, 51, 45, 30, 15, 5, 1)/243`. For `s ≤ 12`, `h(s) mod 3` is
  `0` on `{0, 1, 8, 9, 10}`, `1` on `{2, 3, 4, 11, 12}` and `2` on `{5, 6, 7}`.

**Table T2** (`q = 2`; probability that `h(a + S_k)` is odd).

| `k` | `a = 0` | `a = 1` | `a = 2` | `a = 3` |
|---|---|---|---|---|
| 3 | 4/8 | 7/8 | 7/8 | 4/8 |
| 4 | 11/16 | 14/16 | 11/16 | — |
| 5 | 25/32 | 25/32 | — | — |
| 6 | 50/64 | — | — | — |

**Table T3** (`q = 3`; counts over 243 of `h(a + S_5) mod 3 = 0, 1, 2`).

| `a` | value 0 | value 1 | value 2 |
|---|---|---|---|
| 0 | 27 | 90 | 126 |
| 1 | 51 | 51 | 141 |
| 2 | 90 | 27 | 126 |

Every entry of T3 is at least `27/243 = 1/9`. In T2, every entry for `k = 3` with `a ≤ 3`, and for
`k = 4` with `a ≤ 2`, lies in `[1/8, 7/8]`.

**W-nl-1 (record laws not coset-uniform)** [W]. Take initial-condition mode, `O = C = {o}`, `τ = 1`,
and blocks at graph distance at least 3 from `o`, on `Λ_{L_tor}` with `L_tor ≥ 5` or on `ℤ^3`, under the
uniform law.
- For `q = 2`: `x_o(1) = h(S_6) − y_o(0)`, and `h(S_6)` is odd with probability `50/64 = 25/32`
  (T2). So `x_o(1)` takes one value with probability `25/32` and the other with `7/32`.
- The cosets of subgroups of `ℤ/q` are, for prime `q`, the points and `ℤ/q` itself, so a
  coset-uniform law is a point mass or uniform. This law is neither, so Lemma A-T (c) fails for
  R-nl at `q = 2`.
- For `q = 3`, in the interface of W-nl-2 below with label current `0`, `x_o(1)` has law
  `(27, 90, 126)/243` up to a shift (row `a = 0` of T3). It is neither a point mass nor uniform,
  so (c) fails at `q = 3` as well.

**W-nl-2 (`q = 3`, initial-condition mode: the dichotomy fails)** [W].
- *Interface.* `Λ_{L_tor}` with `L_tor ≥ 5`, or `ℤ^3`; `O = C = {o}`; `τ = 1`; the uniform law (uniform
  product law on `ℤ^3`); any fixed `r_O = (y_o(0), x_o(0))`. The layout puts `P_1 = {n₁}`, with
  `n₁ = o + e_1`, and `P_2 = {o + 2e_1 + 2e_2}` (graph distance 4 > `τ`), and the later blocks at
  graph distance at least 3 from `o`.
- *Two label sequences.* They agree on every block except `P_1`. There both have previous
  component `y*`, and their current components are `0` and `1`.
- *Claim.* The laws `W⁽¹⁾, W⁽²⁾` of the round-2 record satisfy `13/81 ≤ TV(W⁽¹⁾, W⁽²⁾) ≤ 175/243`.
- *Proof.*
  1. The round-2 record is `O`'s configuration at tick 2, `(x_o(1), x_o(2))`.
  2. `x_o(2)` depends on `x_o(0)` and on `x_j(1)` for `j ∈ nn(o)`. These depend on `x(0)` at
     `nn(j)` and on `y_j(0)`. Every site involved lies within graph distance 2 of `o`, which
     excludes every block but `P_1`. `L_tor ≥ 5` makes these sites distinct.
  3. `x_o(1) = h(c + S) − y_o(0)`, where `c` is `P_1`'s current component and `S` is the sum over
     the five other neighbours of `o`, all unread and uniform, so `S ~ S_5`. By rows `a = 0, 1` of
     T3 the two laws of `x_o(1)` are `(27, 90, 126)/243` and `(51, 51, 141)/243`, up to the common
     shift by `−y_o(0)`. Their total variation is `(24 + 39 + 15)/486 = 39/243 = 13/81`. The record's
     total variation is at least that of this marginal.
  4. Let `J = nn(o) ∖ {n₁}`. For `j ∈ J`, `x_j(1) = h(s_j(0)) − y_j(0)` with `y_j(0)` uniform and
     independent of `x(0)` and of each other (Lemma M). `x_o(1)` and `a = x_{n₁}(1) = h(s_{n₁}(0)) − y*`
     are functions of `x(0)`. So, conditional on `(x_o(1), a) = (v, a)`, the sum
     `S′ = Σ_{j∈J} x_j(1)` has the law of `S_5`, and `x_o(2) = h(a + S′) − x_o(0)`. By T3,
     `P(x_o(2) = w | v, a) ≥ 1/9` for every `w`.
  5. Hence `P⁽ⁱ⁾(v, w) ≥ P⁽ⁱ⁾(v)/9` for every `(v, w)` and `i = 1, 2`. The overlap
     `Σ_{v,w} min(P⁽¹⁾(v, w), P⁽²⁾(v, w))` is at least `3 · (1/9) · (1 − 39/243) = 68/243`. So
     `TV ≤ 175/243`. ∎
- The two sequences coincide from round 2 on, with the same `r_O` and layout. Lemma A-T (d), if it
  held for R-nl, would give total variation `0` or `1`.

**W-nl-3 (`q = 2`, initial-condition mode)** [W].
- *A single label cell is hidden at one step.* By T2 (`k = 5`), `h(a + S_5)` is odd with
  probability `25/32` for both `a = 0` and `a = 1`. The map `S_5 ↦ 5 − S_5` sends `{2, 3, 4}` to
  `{1, 2, 3}`. This round-2 witness uses two label cells next to one read site. Whether one label
  cell suffices at `q = 2` is not decided: its value re-enters as `y_{n₁}(1)` and can reach `o` at
  tick 3.
- *Interface.* `Λ_{L_tor}` with `L_tor ≥ 5`, or `ℤ^3`; `o′ = o − e_1 + e_2`; `O = C = {o, o′}`;
  `τ = 1`; the uniform law. `P_1 = C + e_1 = {o + e_1, o + e_2}`. Both cells are neighbours of `o`, and
  `o + e_2 = o′ + e_1` is also a neighbour of `o′`. The later blocks are at graph distance at least
  3 from `O`.
- *Two label sequences.* They differ only in `P_1`'s current components: `(0, 0)` against
  `(1, 0)`.
- *Claim.* `3/16 ≤ TV ≤ 1 − 13/1024` for the round-2 record
  `(x_o(1), x_{o′}(1), x_o(2), x_{o′}(2))`.
- *Proof.*
  1. *Lower bound.* `x_o(1) = h(t + S_4) − y_o(0)`, where `t ∈ {0, 1}` is the sum of the two label
     currents and `S_4` is the sum over `o − e_1, o − e_2, o ± e_3`, all unread. By T2 (`k = 4`) the
     two laws of `x_o(1)` differ by `|11 − 14|/16 = 3/16`.
  2. *`x_{o′}(1)` given `x_o(1)`.* `x_{o′}(1) = h(x_{o+e_2}(0) + x_{o−e_1}(0) + S″) − y_{o′}(0)`.
     The label current at `o + e_2` is `0` in both sequences. `S″` is the sum over the four other
     neighbours of `o′` (`o − 2e_1 + e_2`, `o − e_1 + 2e_2`, `o′ ± e_3`), which are unread and are
     not neighbours of `o`. Given `x_o(1)` and `x_{o−e_1}(0) ∈ {0, 1}`, T2 (`k = 4`) gives each value
     of `x_{o′}(1)` probability at least `2/16 = 1/8`.
  3. *Tick 2.* Condition on all of `x(0)` and on `x_{o−e_1}(1)`. By Lemma M, the time-1 values of
     the other unread neighbours of `o` and `o′` are independent and uniform. Then
     `s_o(1) = A + S_3`, where `A ∈ {0, …, 3}` comes from the two block cells and `o − e_1`, and
     `S_3` is the sum over `o − e_2, o ± e_3`. Likewise `s_{o′}(1) = A′ + S‴`, where
     `A′ ∈ {0, 1, 2}` comes from `o + e_2` and `o − e_1`, and `S‴` is the sum over the four other
     neighbours of `o′`. `S_3` and `S‴` are independent. By T2, each value of `x_o(2)` and of
     `x_{o′}(2)` has conditional probability at least `1/8`, so each pair has at least `1/64`.
  4. Every record value therefore has probability at least `P(x_o(1) = v)/512` under each
     sequence. Summing over the eight values of `(x_{o′}(1), x_o(2), x_{o′}(2))`, the overlap is at
     least `8 · (1 − 3/16)/512 = 13/1024`. ∎

**W-nl-4 (`q = 3`, exchange mode under H-write)** [W].
- *Interface.* `O = {o, p}` with `p = o + e_1`, `C = {p}`, `τ = 1`, the uniform law on `Λ ∖ O`.
- *Two label sequences.* Round 1 writes `(y*, c)` into `p`, with `c = 0` in one sequence and `c = 1`
  in the other. Round 2 writes the same `c_2 = (y_2, x_2)` in both.
- *The round-2 record.* It is `c_2` together with `O`'s configuration at tick 2: `(x_o(1), x_o(2))`
  at `o` and `(x_2, x_p(2))` at `p`.
- *Proof.*
  1. As in W-nl-2, `x_o(1) = h(c + S_5) − y_o(0)`, which gives a lower bound of `13/81`.
  2. Given `x_o(1)`, set `s_o = x_2 + S′` and `s_p = x_o(1) + S″` at tick 2. `S′` and `S″` are fresh
     sums over the five unread neighbours of `o` other than `p` and of `p` other than `o`. These sets
     are disjoint, since the cubic lattice is bipartite.
  3. By T3, each pair `(x_o(2), x_p(2))` has conditional probability at least `1/81`. The overlap
     is therefore at least `(204/243) · 9/81 = 68/729`, and `13/81 ≤ TV ≤ 661/729`. ∎

**Any larger `C`.** Adjoin to `C` (and `O`) any cells at graph distance at least 6 from the witness
sites, with equal labels in both sequences. In initial-condition mode, the translated block cells
then lie at distance at least 5. The records of the added cells depend on time-0 variables
disjoint from those of the witness. Under a product law their part of the record has the same law
in both sequences and is independent of the witness part, so the total variation is unchanged.
Therefore, on tori large enough to hold them and on `ℤ^3`:
- W-nl-2 holds for every `|C| ≥ 1` at `q = 3`, in initial-condition mode;
- W-nl-4 holds for every `|C| ≥ 1` at `q = 3`, in exchange mode;
- W-nl-3 holds for every `|C| ≥ 2` at `q = 2`, in initial-condition mode only.

**Scope of the witnesses.** No witness was computed at `q = 2` in exchange mode, or at any
`q ≥ 4`. The proof of Lemma A-T fails at every `q ≥ 2` (Lemma NA). Its conclusion (d) is refuted
at `q = 3` in both modes and at `q = 2` in initial-condition mode, and is not decided at `q = 2` in
exchange mode or at `q ≥ 4`.

### 1.4 Lemma I: steps 1–5 of FC-1, without the rule

**Lemma I (intermediate distinguishability)** [W].
- *Statement.* Let an interface satisfy Q3′, Q5′ and Q6′ at `(ε, K)`, with `K ≥ L + 1`, for a
  declared target with reads `a, b` and `a·b ∈ [−½, ½]`. Let `P_1, P_2` be admissible Q6′(i)
  witnesses for `ψ_1 = a` and `ψ_2 = b`. Pad each with rounds of `c(0)` to length `K − 2`, giving
  `P′_1, P′_2`, and let `W′_i` be the world's law of the records of the single round `c_a` after
  `P′_i`, conditional on the herald where there is one. Then

  > `(1 − a·b)/2 − 8ε ≤ TV(W′_1, W′_2) ≤ (1 − a·b)/2 + 12ε`,

  so in particular `¼ − 8ε ≤ TV(W′_1, W′_2) ≤ ¾ + 12ε`.
- *Proof.* This is Session 3's FC-1, steps 1–5. They use the following, and no property of the
  rule, the law or the mode:
  - Q3′, through `F(ε; 𝒯_K)` on `T_a` and on `(c(0)^k, T_a)`;
  - the Lüders structure of `c_a` (Q5′);
  - Q6′(i), whose witnesses have length `≤ K − L ≤ K − 2`.

  For a heralded witness, the padded preparation is an unheralded extension of an admissible
  heralded preparation (final B1.2), so it is admissible with the same herald. Every law in
  steps 2–5 is then the conditional law, which is what credit controls. In exchange mode, an
  adaptive witness changes no step. ∎
- *Witness qualifiers.* None: admissible witnesses of every kind.

For R-lin, FC-1 step 6 contradicts Lemma I through the dichotomy. For R-nl, W-nl-2 to W-nl-4 show
that equal-length preparations followed by a common round can be at intermediate total variation.
Lemma I is therefore a necessary condition that R-nl's structure does not exclude by itself. It is
not shown to be met by any family that also meets the other conditions.

### 1.5 Transfer table

| Session 3 item | Rule property it uses | R-nl | Check |
|---|---|---|---|
| Lemma 0 | none (finite abelian groups) | holds, but has no input | §1.2 |
| Lemma A-T (a), (b) | `Φ_F` is a group endomorphism (proof step 1) | fails at step 1 | Lemma NA |
| Lemma A-T (c) | (a), (b) and Lemma 0 | conclusion false at `q ∈ {2, 3}`, initial-condition mode | W-nl-1, W-nl-2 |
| Lemma A-T (d) | (c) | conclusion false at `q = 3`, both modes, and at `q = 2`, initial-condition mode; not decided at `q = 2`, exchange mode | W-nl-2, -3, -4 |
| FC-1 steps 1–5 | none | hold | Lemma I |
| FC-1 step 6, FC-2 | Lemma A-T (d) | not available | W-nl-2 to W-nl-4 |
| L5.4–L5.6 (children) | defined by where (d) held | no counterpart (§2, NL.4) | — |
| Lemma F, U2(ii) exact | `Φ` a bijection of a finite set | hold on `𝓛_fin` | §3 |
| §4 row (L-1) | — | R-nl is an explicit member of the third class for which (L-1) fails | W-nl-1 |

### 1.6 Finding F-S3-1: the `K₀` of Session 3's tokens presumes `L = 2`

- FC-1 states its tokens at `(ε₀, K₀) = (1/50, 3)`. Its step 1 takes Q6′(i) witnesses of length
  at most `K − 2`.
- By final B3, Q6′ is posed only for `K ≥ L + 1`, and Q6′(i) witnesses have length `≤ K − L`. The
  separation length `L ≥ 2` is the family's own constant (final B1.3 (ii)).
- For a family that declares `L ≥ 3`, Q6′ is not posed at `K = 3` ("entered as 'not posed', and the
  other conditions are reported with that entry"). FC-1 then gives no failure at `K = 3`. Its proof
  does give a failure at every `K ≥ L + 1`.
- A `FAIL-CLASS(𝓢)` needs one `K₀` for all of `𝓢` (proposal §2.1). The four `FAIL-CLASS` tokens of
  Session 3 §5 therefore hold as stated for families with `L = 2` only.
- This does not change Session 3's verdict that no R-lin family of those subclasses meets the
  target: each fails at `K = L + 1`, which a pass requires. The same restriction is built into
  NL-C below.

**Owner decision 2** (comment 6825956102, quoted in the header):

> 2. F-S3-1: "Add L ≤ L₀ at K₀=L₀+1 (Recommended)". Session 3's four FAIL-CLASS tokens are
> restated with the restriction L ≤ L₀ at (1/50, L₀+1), for every L₀ ≥ 2. The correction is
> recorded in the Session 4 record. The Session 3 file is not edited.

**Corrected statement of Session 3's tokens** [W]. This record is the mutable record that carries
the correction; `TUNE-1-STEP2-SESSION3.md` carries only a pointer to this section in its §5
(PR #1237 comment 6828820114, `amaybaum`, 2026-11-12T16:05:24Z), and its §5 tokens, FC-1 and FC-2 are read
as corrected here. Each token keeps its existing qualifiers and adds the restriction `L ≤ L₀`. Each
holds at `(1/50, L₀ + 1)` for every `L₀ ≥ 2`; at `L₀ = 2` this is `(1/50, 3)`.

| Law | Carrier, mode | Corrected token | Hypotheses carried |
|---|---|---|---|
| uniform | `𝓛_fin`, `init` | `FAIL-CLASS(R-lin, 𝓛_fin, uniform law, init, Q6′ witnessed unheralded, L ≤ L₀)` at `(1/50, L₀ + 1)`, for every `L₀ ≥ 2` and every `q ≥ 2` | H-μ |
| uniform product | `𝓛_∞`, `init` | `FAIL-CLASS(R-lin, 𝓛_∞, uniform product law, init, Q6′ witnessed unheralded, L ≤ L₀)` at `(1/50, L₀ + 1)`, for every `L₀ ≥ 2` | H-μ, H-∞ |
| uniform | `𝓛_fin`, `exch` | `FAIL-CLASS(R-lin, 𝓛_fin, uniform law, exch, Q6′ witnessed non-adaptive and unheralded, L ≤ L₀)` at `(1/50, L₀ + 1)`, for every `L₀ ≥ 2` | H-μ, H-write |
| uniform product | `𝓛_∞`, `exch` | `FAIL-CLASS(R-lin, 𝓛_∞, uniform product law, exch, Q6′ witnessed non-adaptive and unheralded, L ≤ L₀)` at `(1/50, L₀ + 1)`, for every `L₀ ≥ 2` | H-μ, H-∞, H-write |

The theorem texts read as follows:
- **FC-1:** no interface of any such family, at any resource, satisfies Q3′, Q5′ and Q6′ together
  at any `ε < 1/48` and `K ≥ L + 1`, when Q6′ is witnessed by unheralded preparations. In its
  proof, "`K ≥ 3`" reads "`K ≥ L + 1`"; step 1's witnesses then have length `≤ K − L ≤ K − 2`, and
  steps 2–6 are unchanged.
- **FC-2:** the same in exchange mode under H-write, with Q6′ witnessed by non-adaptive,
  unheralded preparations, at any `ε < 1/48` and `K ≥ L + 1`.
- **What the tokens establish** (Session 3 §5): each establishes only that its stated subclass,
  restricted to `L ≤ L₀`, does not reach the target at `(1/50, L₀ + 1)`.

`ε₀ = 1/50` is unaffected, and so are the `INCONCLUSIVE` rows of Session 3 §5. The NL-C rows of
§5.2 bear on those rows.

***

## 2. The R-nl node tree

The nodes are decided depth-first by the proposal's decision rule (§2.2), over green controls.

### Node NL.1: transfer

§1. **Verdict: proved [W].** Lemma A-T fails for R-nl at its first proof step. Its conclusion (c)
is false at `q ∈ {2, 3}` in initial-condition mode. Its conclusion (d) is false at `q = 3` in both
modes and at `q = 2` in initial-condition mode. At `q = 2` in exchange mode, and at `q ≥ 4`, the
conclusions are not decided. FC-1 and FC-2 do not transfer. Their rule-free part is Lemma I.
Lemma F and exact U2(ii) transfer on `𝓛_fin`.

### Node NL.2: an obstruction for R-nl families?

**NL.2.1: the exact dichotomy, over all interfaces.** It is refuted at `q = 3` in both modes, for
every `|C| ≥ 1` (W-nl-2, W-nl-4), and at `q = 2` in initial-condition mode, for every `|C| ≥ 2`
(W-nl-3). **Verdict: refuted [W]** in these cases. The route of FC-1 is closed for R-nl there, not
merely unproved. At `q = 2` in exchange mode, and at `q ≥ 4`, the exact dichotomy is not decided.

**NL.2.2: a dichotomy restricted to witness pairs, or an approximate one.** FC-1 step 6 needs the
dichotomy only for the padded witness pairs that a family meeting Q3′, Q5′ and Q6′ supplies.
W-nl-2 to W-nl-4 use arbitrary label pairs. They do not show that such a family's witness pairs
can be at intermediate distance.
- *Reduction* [W]. Fix `q`, the law `λ`, the mode `m` and the carrier `𝓛`. Suppose that for some
  `δ ∈ [0, ¼)` the following holds: for every family of (R-nl, `𝓛`, `λ`, `m`), with its separation
  length `L`, every member, every `ε < (¼ − δ)/12` and every `K ≥ L + 1`, every interface that
  meets Q3′, Q5′ and Q6′ at `(ε, K)` for a declared target with reads `a, b`, `a·b ∈ [−½, ½]`,
  and every pair `P_1, P_2` of admissible Q6′(i) witnesses for `ψ_1 = a` and `ψ_2 = b` (heralded or
  not, adaptive or not), the padded pair `P′_1, P′_2` of Lemma I has `TV(W′_1, W′_2) ∉ (δ, 1 − δ)`.
  For such `ε`, `¼ − 8ε > δ` and `¾ + 12ε < 1 − δ`, so Lemma I places the total variation inside
  `(δ, 1 − δ)`, which is a contradiction. For every `L₀ ≥ 2`, a family with `L ≤ L₀` has
  `K₀ = L₀ + 1 ≥ L + 1`, so this would give
  `FAIL-CLASS(R-nl, 𝓛, λ, m, L ≤ L₀)` at `(ε₀, L₀ + 1)` for every `ε₀ < (¼ − δ)/12`.
- *Constraint on any proof.* The unrestricted form, over all equal-length pairs followed by a
  common round rather than witness pairs only, is false in the following cases, since each witness
  has `min(TV, 1 − TV)` at least the stated constant:

  | `q` | Mode | Witness | `TV` interval | Form false for |
  |---|---|---|---|---|
  | 3 | initial-condition | W-nl-2, every `|C| ≥ 1` | `[39/243, 175/243]` | `δ < 13/81` |
  | 3 | exchange (H-write) | W-nl-4, every `|C| ≥ 1` | `[13/81, 661/729]` | `δ < 68/729` |
  | 2 | initial-condition | W-nl-3, every `|C| ≥ 2` | `[3/16, 1011/1024]` | `δ < 13/1024` |
  | 2 | exchange | none computed | — | not decided |
  | `≥ 4` | either | none computed | — | not decided |

  A proof with `δ` below the stated constant must therefore use the Q-conditions on the pair, not
  R-nl's structure alone.
- A proof must also use a property of R-nl that some reversible rule with an unread uniform
  environment lacks. In particular, it must lack it under the rule `F_U` that C-PROG stipulates in
  second-order form, whose row takes Q0–Q6 from Main:582's controller at the stated `(ε, K)`. A
  property shared by every second-order rule would contradict that row.
- **Verdict: open.** This is gap NL-A (§5).

**NL.2.3: symmetries of R-nl.**

**Lemma S (reflection)** [W].
- *Statement.* For every `q ≥ 2`, `Φ` commutes with `ρ(y, x) = (−1 − y, −1 − x)`, applied sitewise.
- *Proof.*
  1. On representatives, `−1 − x` is `q − 1 − x`, so `s_i(ρx) = 6(q − 1) − s_i(x)`.
  2. Write `h(6(q − 1) − s) = ⌊(6q − 5 − s)/3⌋ = 2q − 2 + ⌊(1 − s)/3⌋`. Then
     `⌊(1 − s)/3⌋ = −⌈(s − 1)/3⌉ = −⌊(s + 1)/3⌋`, so `h(6(q − 1) − s) = 2(q − 1) − h(s)` and
     `g(ρx) = −2 − g(x) mod q`.
  3. Hence `Φ(ρ(y, x)) = (−1 − x, −2 − g(x) + 1 + y) = ρ(Φ(y, x))`. ∎
- *Consequence.* The record law of the interface with `(r_O, labels)` is the `ρ`-image of the one
  with `(ρ r_O, ρ labels)`, under any law invariant under `ρ`. This relates two interfaces. Within
  one interface it gives at most an involution on labels and records. A qubit record theory can
  carry such a symmetry, so no constraint follows.
- **Verdict: no obstruction.** Recorded only (non-gem).

**NL.2.4: obstructions that do not use the rule.**

**Theorem NL-C (bounded control region)** [W].
- *Statement.* Take any rule (in particular R-nl under H-nl), any law, either mode and either
  carrier. Let an interface have `|C| ≤ c` and declare a target with separation length `L`. Then
  Q6′(i) fails at every `ε < ε_C(c) := sin(π/(q^{2c} + 1))/8` and every `K ≥ L + 1`, whatever its
  witnesses (heralded or not, adaptive or not). Hence no member of a family with
  `sup_n |C_n| ≤ c` and `L ≤ L₀` satisfies Q6′ at `(ε₀, L₀ + 1)` for any `ε₀ < ε_C(c)`.
- *Proof.* This is C-CARD (a)'s argument (final B6.1 item 10; Session 2 §2.5), re-derived for a
  control region of bounded size, on any torus side `L_tor`, on `ℤ^3` and at any separation
  length `L`.
  1. The menu `(V × V)^C` has `M = q^{2|C|} ≤ q^{2c}` labels. In both modes every label, gate
     labels included, is an element of it. In initial-condition mode a label is the content of a
     block, which is a translate of `C`.
  2. Among the angles `2πk/(M + 1)`, `k = 0, …, M`, two distinct ones `θ, θ′` have
     `c(θ) = c(θ′)`. Their circular distance is `d ≥ 2π/(M + 1)`.
  3. Take `u ∈ {a, b}` with `|u_⊥| ≥ ½`, where `⊥` denotes the component perpendicular to `n̂`.
     If both `|a_⊥|, |b_⊥| < ½`, then `|a·b| ≥ |a_∥||b_∥| − |a_⊥||b_⊥| > ¾ − ¼ = ½`, a
     contradiction.
  4. Let `Δ = R_θ^{−1}u − R_{θ′}^{−1}u`. Then `|Δ| = 2|u_⊥| sin(d/2) ≥ sin(π/(M + 1))`, since
     `d/2 ∈ [π/(M + 1), π/2]`.
  5. Q6′(i) for the pure state `ψ` with Bloch vector `Δ/|Δ|` gives an admissible `P` of length
     `≤ K − L`, credited on `𝒯_L`, with `|r̄ − ψ| ≤ 2ε` (Bloch).
  6. The tests `(c(θ), c_u)` and `(c(θ′), c_u)` lie in `𝒯_L` and fit. They are the same label
     sequence. An identified test's labels never depend on the preparation's records (final B1.1).
     So the world's laws after `P`, conditional on the herald if there is one, are equal. The
     target's class-`u1` probabilities are `(1 + (R_θ^{−1}u)·r̄)/2` and `(1 + (R_{θ′}^{−1}u)·r̄)/2`,
     since a gate's record law does not depend on the state. Credit gives `|Δ·r̄| ≤ 4ε`.
  7. `|Δ| = Δ·ψ ≤ |Δ·r̄| + |Δ||ψ − r̄| ≤ 4ε + 2 · 2ε = 8ε`. With step 4, this is false for
     `ε < sin(π/(M + 1))/8`. ∎
- *What it uses:*
  - the declared target's gate family over every `θ` and its Lüders reads with `a·b ∈ [−½, ½]`
    (final B1.1);
  - Q6′(i) with its credit on `𝒯_L`;
  - the finite menu;
  - that an identified test's labels do not depend on the preparation's records (final B1.1).
- *What it does not use:* the rule, the law, the carrier, adaptivity, heralds, Q1, Q2, Q3′, Q4,
  Q6′(ii) or the resource count.
- *Relation to C-CARD (a).* C-CARD (a) is stated for one fixed finite world, and is the special case
  `|C| ≤ L_tor³`. NL-C needs only a bounded `C`. It holds at every torus side `L_tor`, at every
  separation length `L` (with `K ≥ L + 1`) and on `𝓛_∞`, so an infinite
  carrier does not remove the obstruction for a bounded control region. No control row changes.

**Corollary NL-C′ (explicit growth of the control region)** [W].
- *Statement.* If an interface meets Q6′ at `(ε, K)`, with `ε < 1/8` and `K ≥ L + 1`, then
  `|C| ≥ ½ log_q(π/arcsin(8ε) − 1) ≥ ½ log_q((1 − 4ε)/(4ε))`. The resource `N` is then at least
  `|C|` in exchange mode, and at least `(K + 1)|C|` in initial-condition mode, since `O ⊇ C` and
  there are `K_n ≥ K` disjoint blocks of size `|C|` outside `O`.
- *Proof.*
  1. By NL-C, `sin(π/(M + 1)) ≤ 8ε < 1`. Since `π/(M + 1) ∈ (0, π/2]`, this gives
     `π/(M + 1) ≤ arcsin(8ε)`, so `q^{2|C|} ≥ π/arcsin(8ε) − 1`.
  2. `arcsin y ≤ πy/2` on `[0, 1]` (convexity), so `π/arcsin(8ε) ≥ 1/(4ε)`. ∎
- *Illustration* (hand values, approximate). At `q = 2` and `ε = 1/50`, `arcsin(0.16) ≈ 0.1607`
  and `π/0.1607 ≈ 19.55`. So `2^{2|C|} ≥ 18.55`, which means `|C| ≥ 3`.

**Verdict NL.2.4: proved [W].** NL-C is the `FAIL-CLASS` of §5, with no witness qualifier.

**Fixed point.** Three further passes after NL-C found no further structural finding:
- a rule-free bound from Q1's upper half (none: Q1 does not involve the gate family);
- the light-cone timing of the blocks in initial-condition mode (a layout constraint, not an
  obstruction);
- the exact hiding of single label cells at `q = 2` (W-nl-3), which is a property of one step and
  is recorded only.

### Node NL.3: the constructive side (Route P)

No R-nl family is exhibited. Any candidate must meet the following [W]:
- NL-C′: `|C_n|` grows at least like `½ log_q(1/(4ε))`;
- L4(a) in exact form on `𝓛_fin` (§3): its encoding is not an injective complete orthogonal frame
  with H-LIFT;
- D6(b) under choice 11(a): each component of the label encoder is `selected` or `parameter`.

R-nl's record laws have no closed form, so a proof of the Q-conditions on paper would go either
through a derivation of the record laws from `Φ`, `r_O` and `μ`, or through a capacity statement
(R-nl reproduces some controller). In the second case, a controller whose specification has a hit
under D6 makes the encoder `content` and a hit, as in C-PROG-P's second presentation. No derivation
of the first kind is known for R-nl. **Verdict: open.** This is gap NL-P (§5).

### Node NL.4: the child splits of Session 3

For R-lin, heralds, adaptivity and the non-coset laws were child nodes because the dichotomy held
in the base case (unheralded, non-adaptive, uniform law). For R-nl the exact dichotomy fails
already in the base case (NL.2.1), so no child node is opened:
- NL-C covers every kind of witness, every law and both modes;
- the family classes are `INCONCLUSIVE(NL-A; NL-P)` under every law.

***

## 3. Lemma F and U2(ii) for R-nl

Session 3 §3 re-derived Lemma F and exact U2(ii) under these hypotheses:
- a fixed bijection `Φ` of a finite configuration set;
- the stated observer operations;
- H-LIFT;
- an injective orthogonal frame identification.

None of these concerns the form of `F`. R-nl is a bijection (proposal §1.1 [W]: `(x, z) ↦ (g(x) − z, x)`
inverts it), and on `Λ_{L_tor}` the configuration set is finite. Hence:
- Lemma F and exact U2(ii) hold for R-nl on `𝓛_fin`;
- L4(a) holds in its exact form for R-nl on `𝓛_fin`.

On `𝓛_∞` the configuration set is infinite, and neither statement was re-derived. The approximate
form of L4(a) stays open, as in Session 3. No token depends on it.

***

## 4. Proves-too-much rows (proposal §3, invariant table)

**NL-C.** The properties it uses:
- (C1) the gate labels are drawn from a menu of at most `M` labels, with `M` bounded on the
  subclass;
- (C2) Q6′(i) credit on gate-then-read tests of the declared target;
- (C3) the declared target has a gate label for every `θ`, and Lüders reads `a, b` with
  `a·b ∈ [−½, ½]` (final B1.1);
- (C4) an identified test's labels do not depend on the preparation's records (final B1.1).

(C3) and (C4) are part of the frozen definitions and hold in every case below; the cases differ in
(C1) and (C2).

| Case | Do (C1) and (C2) hold? | Does the conclusion contradict the stated classification? | Applies? |
|---|---|---|---|
| C-POS-1, on its protocol class at `ε = 0` | (C1) fails: a continuum of rotation settings, not a lattice menu | — | no |
| C-POS-2, separating menus | both hold, with `M` the menu size | no. Its Q6′ is classified at `ε ≥ b + δ_{K−2}`, and `δ_{K−2} ≥ g ≥ π/M_rot ≥ π/M > π/(8(M + 1)) > sin(π/(M + 1))/8`, where `M_rot ≤ M` is the number of menu rotations about `n̂` | no |
| Reversible rules, unread uniform environment, every member, at growing resources | (C1) fails for members whose control region `C_n` grows | — | no |

The row is **green**. Lemma I is not a negative argument and concludes nothing against any case.
W-nl-1 to W-nl-4 are instances. The L5 row of Session 3 §4 is unchanged and green. Its third-case
entry, "(L-1) fails for nonlinear members", has an explicit member: R-nl at `q ∈ {2, 3}`
(W-nl-1).

***

## 5. Tokens and the verdict (proposal §2.2)

**Step 1.** Every control row is green:
- the seventeen M1 controls (Session 2 and its C-POS-2 rerun);
- the L5 row (Session 3 §4);
- the NL-C row (§4).

No row relied on as established has status other than `proved`. H-nl is carried by every R-nl
token below. The session is within choice 10(a) as extended by owner decision 1 (header).

**Step 2.** No `PASS-DERIVED` family is proved.

**Step 3.** `FAIL-CLASS` is proved for proper subclasses only, so each is reported with
`INCONCLUSIVE(gap)` for the rest.

The `FAIL-CLASS` rows have the form
`FAIL-CLASS(R-nl, 𝓛, λ, m, sup_n |C_n| ≤ c, L ≤ L₀)`, at `(ε₀, L₀ + 1)` for every
`ε₀ < sin(π/(q^{2c} + 1))/8`, every `c ≥ 1`, every `L₀ ≥ 2` and every `q ≥ 2`. Q6′ may be witnessed
in any admissible way. The restriction is on the family (its control region and separation length),
not on the witnesses. The rows are written `FC-nl(𝓛, λ, m)` below. Each family with bounded
`|C_n|` lies in one of these subclasses (take `c = sup_n |C_n|` and `L₀ = L`), so the part of each
family class that `INCONCLUSIVE(NL-A; NL-P)` leaves undecided is the families with
`sup_n |C_n| = ∞`.

| Law (choice 6(i)(c)) | Carrier, mode | Tokens | Hypotheses carried |
|---|---|---|---|
| uniform | `𝓛_fin`, `init` | `FC-nl(𝓛_fin, uniform law, init)`; family class `INCONCLUSIVE(NL-A; NL-P)` | H-nl, H-μ |
| uniform product | `𝓛_∞`, `init` | `FC-nl(𝓛_∞, uniform product law, init)`; `INCONCLUSIVE(NL-A; NL-P)` | H-nl, H-μ, H-∞ |
| uniform | `𝓛_fin`, `exch` | `FC-nl(𝓛_fin, uniform law, exch)`; `INCONCLUSIVE(NL-A; NL-P)` | H-nl, H-μ, H-write |
| uniform product | `𝓛_∞`, `exch` | `FC-nl(𝓛_∞, uniform product law, exch)`; `INCONCLUSIVE(NL-A; NL-P)` | H-nl, H-μ, H-∞, H-write |
| level-set law | `𝓛_fin`, `exch` | `FC-nl(𝓛_fin, level-set law, exch)`; `INCONCLUSIVE(NL-A; NL-P)` | H-nl, H-μ, H-write |
| level-set law | `init`; `𝓛_∞` | not defined (choice 6(iii)) | — |
| non-uniform product | `𝓛_fin`, `init` | `FC-nl(𝓛_fin, non-uniform product law, init)`; `INCONCLUSIVE(NL-A; NL-P)` | H-nl, H-μ |
| non-uniform product | `𝓛_∞`, `init` | `FC-nl(𝓛_∞, non-uniform product law, init)`; `INCONCLUSIVE(NL-A; NL-P)` | H-nl, H-μ, H-∞ |
| non-uniform product | `𝓛_fin`, `exch` | `FC-nl(𝓛_fin, non-uniform product law, exch)`; `INCONCLUSIVE(NL-A; NL-P)` | H-nl, H-μ, H-write |
| non-uniform product | `𝓛_∞`, `exch` | `FC-nl(𝓛_∞, non-uniform product law, exch)`; `INCONCLUSIVE(NL-A; NL-P)` | H-nl, H-μ, H-∞, H-write |

NL-C uses neither the law nor the rule. The hypotheses are carried because each token names R-nl
and its law, as proposal §2.1 requires.

### 5.1 The gaps

- **NL-A (obstruction).** "For R-nl at fixed `q`, under the law `λ`, in mode `m`, on `𝓛`: is there
  `δ ∈ [0, ¼)` such that, for every family with separation length `L`, every member, every
  `ε < (¼ − δ)/12` and every `K ≥ L + 1`, every interface meeting Q3′, Q5′ and Q6′ at `(ε, K)`,
  and every pair of admissible Q6′(i) witnesses for `a` and `b` (heralded or not, adaptive or not),
  the padded pair of Lemma I has `TV(W′_1, W′_2) ∉ (δ, 1 − δ)`?" A yes gives, for every `L₀ ≥ 2`,
  `FAIL-CLASS(R-nl, 𝓛, λ, m, L ≤ L₀)` at `(ε₀, L₀ + 1)` for every `ε₀ < (¼ − δ)/12` (NL.2.2).
  The form over all equal-length pairs followed by a common round is false for `δ < 13/81` at
  `q = 3` in initial-condition mode (W-nl-2), for `δ < 68/729` at `q = 3` in exchange mode
  (W-nl-4) and for `δ < 13/1024` at `q = 2` in initial-condition mode (W-nl-3). At `q = 2` in
  exchange mode, and at `q ≥ 4`, it is not decided.
- **NL-P (construction).** "Exhibit an R-nl family in `𝕀_D` with Q0–Q6 (amended) and D1–D7
  proved, with explicit `N(ε, K)` and `G(ε, K)`." Its necessary conditions are listed in NL.3.

**Owner decision 4** (comment 6825956102, quoted in the header):

> 4. NL-A / NL-P: "[No preference]". No further work on these gaps is authorized, so they stay
> `INCONCLUSIVE`.

Both gaps therefore stay open, and the R-nl family classes stay `INCONCLUSIVE(NL-A; NL-P)` for
families with `sup_n |C_n| = ∞`.

**What the tokens establish** (proposal §2.3). Each `FAIL-CLASS` row establishes only that R-nl
families with a bounded control region and bounded separation length do not reach the target at the
stated `(ε₀, K₀)`. The argument is rule-independent, so the rows say nothing specific to R-nl. They
are not a no-go for:
- R-nl families with unbounded `|C_n|`;
- R-lin (its own NL-C rows are the separate tokens of §5.2);
- other rules;
- OI generally.

Every R-nl statement carries H-nl. H-nl is not adopted, and a statement about R-nl is a statement
about a rule `main` does not posit (proposal §6, choice 1(c)). Every result here is a paper
derivation [W] awaiting ChatGPT review; nothing is kernel-checked.

### 5.2 NL-C rows for R-lin

**Owner decision 3** (comment 6825956102, quoted in the header):

> 3. NL-C rows for R-lin: "Enter them (Recommended)". They are added to the R-lin table at this
> record update, under the frozen §2.2 step 3 reporting rule.

NL-C uses no property of the rule or the law, so it applies to R-lin as it stands. The rows below
are **rule-independent**: they say nothing specific to R-lin, and they do not use Lemma A-T. They
extend the R-lin table of Session 3 §5, as corrected in §1.6; they do not replace any row of it.
H-nl is not carried, since the rule is R-lin.

Every row has the form
`FAIL-CLASS(R-lin, 𝓛, λ, m, sup_n |C_n| ≤ c, L ≤ L₀)`, at `(ε₀, L₀ + 1)` for every
`ε₀ < sin(π/(q^{2c} + 1))/8`, every `c ≥ 1`, every `L₀ ≥ 2` and every `q ≥ 2`, written
`FC-lin-C(𝓛, λ, m)` below.
- *Hypotheses of NL-C:* a declared target with a gate label for every `θ` and Lüders reads `a, b`
  with `a·b ∈ [−½, ½]`; Q6′(i) with its credit on `𝒯_L`; the finite menu `(V × V)^C` with
  `|C| ≤ c`; identified tests whose labels do not depend on the preparation's records; `K ≥ L + 1`.
- *Witness types:* any admissible Q6′(i) witness: heralded or unheralded, and in exchange mode
  adaptive or non-adaptive. The restriction is on the family (control region and separation
  length), not on the witnesses.

| Law (choice 6(i)(c)) | Carrier, mode | Token | Session 3 row it bears on | Hypotheses carried |
|---|---|---|---|---|
| uniform | `𝓛_fin`, `init` | `FC-lin-C(𝓛_fin, uniform law, init)` | `INCONCLUSIVE(L5.4)` | H-μ |
| uniform product | `𝓛_∞`, `init` | `FC-lin-C(𝓛_∞, uniform product law, init)` | `INCONCLUSIVE(L5.4)` | H-μ, H-∞ |
| uniform | `𝓛_fin`, `exch` | `FC-lin-C(𝓛_fin, uniform law, exch)` | `INCONCLUSIVE(L5.4; L5.5)` | H-μ, H-write |
| uniform product | `𝓛_∞`, `exch` | `FC-lin-C(𝓛_∞, uniform product law, exch)` | `INCONCLUSIVE(L5.4; L5.5)` | H-μ, H-∞, H-write |
| level-set law | `𝓛_fin`, `exch` | `FC-lin-C(𝓛_fin, level-set law, exch)` | `INCONCLUSIVE(L5.6)` | H-μ, H-write |
| level-set law | `init`; `𝓛_∞` | not defined (choice 6(iii)) | — | — |
| non-uniform product | `𝓛_fin`, `init` | `FC-lin-C(𝓛_fin, non-uniform product law, init)` | `INCONCLUSIVE(L5.6)` | H-μ |
| non-uniform product | `𝓛_∞`, `init` | `FC-lin-C(𝓛_∞, non-uniform product law, init)` | `INCONCLUSIVE(L5.6)` | H-μ, H-∞ |
| non-uniform product | `𝓛_fin`, `exch` | `FC-lin-C(𝓛_fin, non-uniform product law, exch)` | `INCONCLUSIVE(L5.6)` | H-μ, H-write |
| non-uniform product | `𝓛_∞`, `exch` | `FC-lin-C(𝓛_∞, non-uniform product law, exch)` | `INCONCLUSIVE(L5.6)` | H-μ, H-∞, H-write |

The hypotheses are carried because each token names R-lin's law, as in Session 3 §5; NL-C itself
does not use them.

**Effect on the `INCONCLUSIVE` rows.** Each family with bounded `|C_n|` lies in one of these
subclasses (take `c = sup_n |C_n|` and `L₀ = L`). The rows therefore settle the bounded-control-region
part of each family class named in the fourth column, for every kind of witness, including the
heralded witnesses of L5.4, the adaptive witnesses of L5.5 and the non-coset laws of L5.6. They do
not close L5.4, L5.5 or L5.6: those gaps remain open for families with `sup_n |C_n| = ∞`, and
the family classes stay `INCONCLUSIVE(L5.4)`, `INCONCLUSIVE(L5.4; L5.5)` and `INCONCLUSIVE(L5.6)`,
narrowed to those families. No work on L5.4 or L5.5 was done (owner decision of c.6824440978).

***

## 6. Pressure test (§A.31)

- **Favourable branch 1: "R-nl escapes the R-lin obstruction."**
  - Only the exact dichotomy over all interfaces is refuted (NL.2.1), and only at `q = 3` in both
    modes and at `q = 2` in initial-condition mode.
  - The dichotomy restricted to witness pairs is open. So are the approximate forms with `δ` at or
    above the case constants of NL.2.2 (`13/81`, `68/729`, `13/1024`), and every form at `q = 2`
    in exchange mode and at `q ≥ 4` (NL-A).
  - The witnesses are single rounds on regions of one or two cells. They say nothing about Q2–Q6,
    and they are not evidence that any R-nl family meets the target.
  - SM's chaos diagnostics are not used. They are numerical evidence, not premises (proposal §1.1).
- **Favourable branch 2: "Lemma I is compatible with R-nl."** Lemma I is a necessary condition.
  W-nl shows only that the condition is not excluded by an exact property of the rule.
- **NL-C, checked for overreach.**
  - A finite menu makes every gate map non-injective, so the declared target's gates are indexed
    by `θ`. This is the reading under which C-CARD (a) is green.
  - A family cannot enlarge the menu. The menu is every configuration of `C`, and in
    initial-condition mode a label is the content of a block, which is a translate of `C`
    (proposal §1.2).
  - A gate cannot be a sequence of rounds: `c(θ)` is one label, and `𝒯_θ` is one round (final
    B1.1).
  - Heralded witnesses are covered, since credit is at conditional error. Adaptive witnesses are
    covered, since an identified test's labels do not depend on the preparation's records.
  - The NL-C row (§4) is green.
- **F-S3-1, checked.** Final B3 states that for `K < L + 1` "Q6′ is entered as 'not posed', and the
  other conditions are reported with that entry". It does not count "not posed" as failed, and FC-1
  needs Q6′(i) witnesses. The finding stands, and the owner adopted the restatement of §1.6
  (decision 2).
- **Exactness.** Every probability in T2, T3 and W-nl-1 to W-nl-4 is an exact rational count,
  checked against its total (16, 32, 64, 8, 243). The only approximate values are in the
  illustration of NL-C′, marked `≈`, and no claim rests on them.
- **Small tori.** Lemma NA uses `L_tor ≥ 3` and the witnesses use `L_tor ≥ 5`, so that neighbours
  are distinct. Families at growing `L_tor` are not affected. No statement here is made for
  `L_tor ≤ 2`.

**Output classification** (§A.31).
- F-S3-1: NEW. It is a hidden assumption in Session 3's `K₀`. Assumption-watch marker: any
  `FAIL-CLASS` that uses Q6′ has `K₀ ≥ L + 1`.
- NL-C and NL-C′: ELABORATING. They strengthen C-CARD (a) from a fixed world to a bounded control
  region, on both carriers and for every rule. Assumption-watch marker: a control region of bounded
  size fails under every rule.
- W-nl-1 to W-nl-4 and Lemma I: ELABORATING. They show that the conclusion of Lemma A-T fails for
  R-nl, and not only its proof.
- Lemma M: CONFIRMING. It locates where linearity enters.
- Lemma S, and the hiding of a single label cell at `q = 2`: BORDERLINE, recorded only.

**Productivity verdict (§0): gem.** The verdict rests mainly on F-S3-1 (NEW), which exposes a
hidden assumption in Session 3's `K₀` (§0 (b)). NL-C and NL-C′ meet §0 (a) only as a
rule-independent elaboration: they constrain every R-nl family, but they re-read C-CARD (a), whose
constant already depends only on `|C|`. Both are strictly stronger than the restatement fixed in
§0.

***

## 7. Remaining work, and owner questions

**Remaining work:**
- a focused internal re-check of the changes applied after the independent review, then ChatGPT
  review.

No further work on NL-A or NL-P is authorized (decision 4).

**Owner questions: all answered** (comment 6825956102, `amaybaum`, 2026-11-12T14:12:24Z).

| Question | Decision | Applied in |
|---|---|---|
| 1. Effort bound: is choice 10(a) extended to this fourth writer session? | "Extend 10(a) to cover it (Recommended)": extended to a fourth writer session, for R-nl only | header; §5 step 1 |
| 2. F-S3-1: how are Session 3's four `FAIL-CLASS` tokens restated? | "Add L ≤ L₀ at K₀=L₀+1 (Recommended)": the restriction `L ≤ L₀` at `(1/50, L₀ + 1)`, for every `L₀ ≥ 2`, recorded here; Session 3 not edited | §1.6 |
| 3. NL-C rows for R-lin: enter them? | "Enter them (Recommended)" | §5.2 |
| 4. NL-A and NL-P: pursue them? | "[No preference]": no further work is authorized, so they stay `INCONCLUSIVE` | §5.1 |

***

## 8. Disclosure

- **Commands:** `git` (worktree list, branch, status, fetch, log, show, diff, add, commit, push),
  `gh api` (reads of the PR #1237 reviews and of comments 6824440978 and 6825956102), `cat`,
  `sed`, `grep`, `cut`,
  `wc`, `ls`, `df`, `sha256sum`. No interpreter was run, and all arithmetic was done by hand.
- **Read:**
  - the proposal (in full);
  - the final amendment and addenda 1 and 2 (in full);
  - Session 1 §§1, 2.1, 2.2, 2.7 and 4–6;
  - Session 2 §§0–1, 2.5–2.8, 3 and 4;
  - the C-POS-2 rerun §§0–2;
  - Session 3 (in full);
  - ChatGPT reviews 5874583745 and 5875006206;
  - owner comments 6824440978 and 6825956102;
  - the independent internal review of this session at `69a92592`;
  - `papers/SM.md`:294 and :296 at the Step 1 pin `cac5d264`.
