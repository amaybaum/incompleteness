# TUNE-1, Step 2, session 4: the R-nl branch (L5/M3 under H-nl)

**WIP / UNVERIFIED research record.** Paper derivation only; no interpreter or numerical
computation was run. No manuscript or Lean file is changed, no premise is adopted, and nothing is
frozen, dispatched or merged. The results go to independent review and then ChatGPT review.

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

**Effort bound.** Choice 10(a) fixed three writer sessions with reviews. This is the fourth. It
runs under the owner's decision above, which authorized the R-nl branch after Session 3; the
relation of that decision to choice 10(a) is listed for the owner in §7.

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
- *Statement.* For every `q ≥ 2`, on `Λ_L` with `L ≥ 3` and on `ℤ^3`, the map `g` is not additive,
  and `Φ` is not affine.
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
and blocks at graph distance at least 3 from `o`, on `Λ_L` with `L ≥ 5` or on `ℤ^3`, under the
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
- *Interface.* `Λ_L` with `L ≥ 5`, or `ℤ^3`; `O = C = {o}`; `τ = 1`; the uniform law (uniform
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
     excludes every block but `P_1`. `L ≥ 5` makes these sites distinct.
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
  `{1, 2, 3}`. A witness at `q = 2` needs two label cells next to one read site.
- *Interface.* `Λ_L` with `L ≥ 5`, or `ℤ^3`; `o′ = o − e_1 + e_2`; `O = C = {o, o′}`; `τ = 1`; the
  uniform law. `P_1 = C + e_1 = {o + e_1, o + e_2}`. Both cells are neighbours of `o`, and
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
W-nl-2 and W-nl-4 therefore hold for every `|C| ≥ 1` at `q = 3`, and W-nl-3 for every `|C| ≥ 2` at
`q = 2`, on tori large enough to hold them.

**For `q ≥ 4`** no witness was computed. The proof of Lemma A-T fails at every `q ≥ 2` (Lemma NA).
Its conclusion is refuted at `q ∈ {2, 3}`, and is not decided for `q ≥ 4`.

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
| Lemma A-T (c) | (a), (b) and Lemma 0 | conclusion false at `q ∈ {2, 3}` | W-nl-1, W-nl-2 |
| Lemma A-T (d) | (c) | conclusion false at `q ∈ {2, 3}`, both modes | W-nl-2, -3, -4 |
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
  Session 3 §5 therefore hold as stated for families with `L = 2`. For every `L₀ ≥ 2` they hold
  with the further restriction `L ≤ L₀`, at `(1/50, L₀ + 1)`. `ε₀` is unaffected.
- This does not change Session 3's verdict that no R-lin family of those subclasses meets the
  target: each fails at `K = L + 1`, which a pass requires. It is listed for the owner (§7), and
  Session 3's file is not edited. The same restriction is built into NL-C below.

***

## 2. The R-nl node tree

The nodes are decided depth-first by the proposal's decision rule (§2.2), over green controls.

### Node NL.1: transfer

§1. **Verdict: proved [W].** Lemma A-T fails for R-nl at its first proof step, and its conclusions
(c) and (d) are false at `q ∈ {2, 3}` in both modes. FC-1 and FC-2 do not transfer. Their
rule-free part is Lemma I. Lemma F and exact U2(ii) transfer on `𝓛_fin`.

### Node NL.2: an obstruction for R-nl families?

**NL.2.1: the exact dichotomy, over all interfaces.** It is refuted at `q ∈ {2, 3}` in both modes,
for every `|C| ≥ 1` at `q = 3` and every `|C| ≥ 2` at `q = 2` (W-nl-2 to W-nl-4). **Verdict:
refuted [W].** The route of FC-1 is closed for R-nl at these `q`, not merely unproved.

**NL.2.2: a dichotomy restricted to witness pairs, or an approximate one.** FC-1 step 6 needs the
dichotomy only for the padded witness pairs that a family meeting Q3′, Q5′ and Q6′ supplies.
W-nl-2 to W-nl-4 use arbitrary label pairs. They do not show that such a family's witness pairs
can be at intermediate distance.
- *Reduction* [W]. Suppose that for some `δ < ¼`, every pair `P′_1, P′_2` of Lemma I has
  `TV(W′_1, W′_2) ∉ (δ, 1 − δ)`. Then Lemma I's interval `[¼ − 8ε, ¾ + 12ε]` lies inside
  `(δ, 1 − δ)` for `ε < (¼ − δ)/12`, which is a contradiction. That would give a `FAIL-CLASS` at
  every `ε₀ < (¼ − δ)/12`.
- *Constraint on any proof.* The unrestricted form, over all equal-length pairs followed by a
  common round, is false at `q = 3` for `δ < 13/81`. W-nl-2 has
  `min(TV, 1 − TV) ≥ min(39, 68)/243 = 13/81`, and holds at every `|C| ≥ 1`. A proof with
  `δ < 13/81` must therefore use the Q-conditions on the pair, not R-nl's structure alone.
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
- *Proof.* This is C-CARD (a)'s argument (final B6.1 item 10; Session 2 §2.5), re-derived without
  fixing `L`.
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
  - the finite menu.
- *What it does not use:* the rule, the law, the carrier, adaptivity, heralds, Q1, Q2, Q3′, Q4,
  Q6′(ii) or the resource count.
- *Relation to C-CARD (a).* C-CARD (a) is stated for one fixed finite world, and is the special case
  `|C| ≤ L³`. NL-C needs only a bounded `C`. It holds at every `L` and on `𝓛_∞`, so an infinite
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
inverts it), and on `Λ_L` the configuration set is finite. Hence:
- Lemma F and exact U2(ii) hold for R-nl on `𝓛_fin`;
- L4(a) holds in its exact form for R-nl on `𝓛_fin`.

On `𝓛_∞` the configuration set is infinite, and neither statement was re-derived. The approximate
form of L4(a) stays open, as in Session 3. No token depends on it.

***

## 4. Proves-too-much rows (proposal §3, invariant table)

**NL-C.** The properties it uses:
- (C1) the gate labels are drawn from a menu of at most `M` labels, with `M` bounded on the
  subclass;
- (C2) Q6′(i) credit on gate-then-read tests of the declared target.

| Case | Do (C1) and (C2) hold? | Does the conclusion contradict the stated classification? | Applies? |
|---|---|---|---|
| C-POS-1, on its protocol class at `ε = 0` | (C1) fails: a continuum of rotation settings, not a lattice menu | — | no |
| C-POS-2, separating menus | both hold, with `M` the menu size | no. Its Q6′ is classified at `ε ≥ b + δ_{K−2}`, and `δ_{K−2} ≥ g ≥ π/M_rot ≥ π/M > π/(8(M + 1)) > sin(π/(M + 1))/8`, where `M_rot ≤ M` is the number of menu rotations about `n̂` | no |
| Reversible rules, unread uniform environment, every member, at growing resources | (C1) fails for members whose control region `C_n` grows | — | no |

The row is **green**. Lemma I is not a negative argument and concludes nothing against any case.
W-nl-1 to W-nl-4 are instances. The L5 row of Session 3 §4 is unchanged and green. Its third-case
entry, "(L-1) fails for nonlinear members", now has an explicit member: R-nl at `q ∈ {2, 3}`
(W-nl-1).

***

## 5. Tokens and the verdict (proposal §2.2)

**Step 1.** Every control row is green:
- the seventeen M1 controls (Session 2 and its C-POS-2 rerun);
- the L5 row (Session 3 §4);
- the NL-C row (§4).

No row relied on as established has status other than `proved`. H-nl is carried by every token
below.

**Step 2.** No `PASS-DERIVED` family is proved.

**Step 3.** `FAIL-CLASS` is proved for proper subclasses only, so each is reported with
`INCONCLUSIVE(gap)` for the rest.

The `FAIL-CLASS` rows have the form
`FAIL-CLASS(R-nl, 𝓛, λ, m, sup_n |C_n| ≤ c, L ≤ L₀)`, at `(ε₀, L₀ + 1)` for every
`ε₀ < sin(π/(q^{2c} + 1))/8`, every `c ≥ 1`, every `L₀ ≥ 2` and every `q ≥ 2`. Q6′ may be witnessed
in any admissible way. The restriction is on the family (its control region and separation length),
not on the witnesses. The rows are written `FC-nl(𝓛, λ, m)` below.

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

**The gaps.**
- **NL-A (obstruction).** "For R-nl at fixed `q`, under the law `λ`, in mode `m`, on `𝓛`: is there
  `δ < ¼` such that, for every interface meeting Q3′, Q5′ and Q6′ at `ε`, the padded witness pairs
  of Lemma I have `TV(W′_1, W′_2) ∉ (δ, 1 − δ)`?" A yes gives `FAIL-CLASS` at every
  `ε₀ < (¼ − δ)/12` (NL.2.2). At `q = 3` the form over all pairs is false for `δ < 13/81`. At
  `q ≥ 4` the exact form is not decided.
- **NL-P (construction).** "Exhibit an R-nl family in `𝕀_D` with Q0–Q6 (amended) and D1–D7
  proved, with explicit `N(ε, K)` and `G(ε, K)`." Its necessary conditions are listed in NL.3.

**What the tokens establish** (proposal §2.3). Each `FAIL-CLASS` row establishes only that R-nl
families with a bounded control region and bounded separation length do not reach the target at the
stated `(ε₀, K₀)`. The argument is rule-independent, so the rows say nothing specific to R-nl. They
are not a no-go for:
- R-nl families with growing `|C_n|`;
- R-lin;
- other rules;
- OI generally.

Every R-nl statement carries H-nl. H-nl is not adopted, and a statement about R-nl is a statement
about a rule `main` does not posit (proposal §6, choice 1(c)). Every result here is a paper
derivation [W] awaiting review; nothing is kernel-checked.

***

## 6. Pressure test (§A.31)

- **Favourable branch 1: "R-nl escapes the R-lin obstruction."**
  - Only the exact dichotomy over all interfaces is refuted (NL.2.1).
  - The dichotomy restricted to witness pairs, and approximate forms with `δ ≥ 13/81`, are open
    (NL-A).
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
  needs Q6′(i) witnesses. The finding stands unless the owner reads B3 otherwise.
- **Exactness.** Every probability in T2, T3 and W-nl-1 to W-nl-4 is an exact rational count,
  checked against its total (16, 32, 64, 8, 243). The only approximate values are in the
  illustration of NL-C′, marked `≈`, and no claim rests on them.
- **Small tori.** Lemma NA uses `L ≥ 3` and the witnesses use `L ≥ 5`, so that neighbours are
  distinct. Families at growing `L` are not affected. No statement here is made for `L ≤ 2`.

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

**Productivity verdict (§0): gem.** NL-C and NL-C′ constrain every R-nl family (§0 (a)). F-S3-1
exposes a hidden assumption (§0 (b)). Both are strictly stronger than the restatement fixed in §0.

***

## 7. Remaining work, and owner questions

**Remaining work:**
- independent review of §§1–6, then ChatGPT review;
- gaps NL-A and NL-P, if the owner wants them pursued.

**Owner questions:**
1. **Effort bound.** This is the fourth writer session. Choice 10(a) fixed three. The owner's
   decision of c.6824440978 authorized it. Should that decision be recorded as extending choice
   10(a) for R-nl? And after review, should NL-A and NL-P be pursued, on paper or by the separately
   authorized exact computation named in proposal §4 (last paragraph), or left as
   `INCONCLUSIVE`?
2. **F-S3-1.** Session 3's four `FAIL-CLASS` tokens state `K₀ = 3`, which holds for `L = 2` only.
   Options:
   - (a) restate each with the further restriction `L ≤ L₀`, at `(1/50, L₀ + 1)`, for every
     `L₀ ≥ 2`, matching NL-C's form here (Recommended);
   - (b) restrict each to `L = 2`, at `(1/50, 3)`;
   - (c) read "not posed" as failed, which would be a definition change.
3. **NL-C for R-lin.** NL-C is rule-independent. It gives `FAIL-CLASS` rows for R-lin's subclasses
   with bounded `|C_n|` and `L`, under every law and for every kind of witness. These rows bear on
   R-lin family classes that Session 3 left `INCONCLUSIVE(L5.4)`, `(L5.5)` and `(L5.6)`, and they
   need no work on L5.4 or L5.5. Proposal §2.2 step 3 reports every `FAIL-CLASS` proved for a
   proper subclass. Options:
   - (a) enter them in the R-lin table at the next record update (Recommended);
   - (b) leave the R-lin table as it is.

***

## 8. Disclosure

- **Commands:** `git` (worktree list, branch, status, fetch, log, show, diff, add, commit, push),
  `gh api` (reads of the PR #1237 reviews and of comment 6824440978), `cat`, `sed`, `grep`, `cut`,
  `wc`, `ls`, `df`, `sha256sum`. No interpreter was run, and all arithmetic was done by hand.
- **Read:**
  - the proposal (in full);
  - the final amendment and addenda 1 and 2 (in full);
  - Session 1 §§1, 2.1, 2.2, 2.7 and 4–6;
  - Session 2 §§0–1, 2.5–2.8, 3 and 4;
  - the C-POS-2 rerun §§0–2;
  - Session 3 (in full);
  - ChatGPT reviews 5874583745 and 5875006206;
  - owner comment 6824440978;
  - `papers/SM.md`:294 and :296 at the Step 1 pin `cac5d264`.
