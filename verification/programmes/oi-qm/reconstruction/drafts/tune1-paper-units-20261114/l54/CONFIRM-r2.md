# Confirmation review of `L54-r2.md` (TUNE-1 gap L5.4, paper derivation r2)

**Reviewer standing.** Same reviewer as `REVIEW-r1.md`; non-author, read-only, paper-only. Hand
reasoning only: no computation on any OI rule or model, nothing edited in the repository or either
worktree, nothing committed, pushed or posted. This is a hand review of a [W] derivation. §6
contains derivations of my own; they are marked reviewer-authored and have had no independent
check.

**Objects.** `l54/L54-r2.md` (521 lines), `l54/RESPONSE-r1.md`. Citation forms as in `L54-r2.md`
(`r2:n` is a line of it). In addition `MS:n` =
`verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/measurement-source.md` on `main`.

***

## 0. Verdict

**ACCEPT WITH CHANGES.** Five small changes, all to wording or scope; exact replacement text is in
§7. None touches a proof.

- F1–F9 are each disposed of as the response says, and each disposition is right at source (§1).
- The replaced control K1 is direct and green in all three cases. I re-derived the C-POS-2 coupling
  bound, including its cell-integration constants; the control is sound and should be kept (§2).
- The new text is supported: Proposition 2's exchange-mode extension and R1 and R3 as written, R2
  after one correction (§3).
- Theorem 1's hypothesis list is complete, and "classes A, B, C fail Q5′, hence T1" is exactly what
  follows (§4).
- The classification ELABORATING is right. One of the three prior statements, C-MEAS, is a precedent
  for the test and not for the mechanism (§5).
- On the rule-free question (§6): the record convention does not by itself make Q5′ fail for every
  rule. I give a non-additive second-order rule that meets Q5′ exactly under complete-history
  records in exchange mode, and a rule-free lemma that constrains every rule and makes Q5′ fail for
  every rule in one corner (initial-condition mode, `τ = 1`). Both are reviewer-authored and
  unchecked. Both Theorem 1 and the lemma depend on the form of the target that AF fixes; that
  dependence has to be stated wherever L5.4–L5.6 are described as decided.

***

## 1. Findings F1–F9: disposition and check

| # | r2 does what the response says | Right at source |
|---|---|---|
| F1 | yes: K1 rebuilt on atom counts and multisets (r2:316–352) | yes; §2 |
| F2 | yes: eight-hypothesis headline (r2:32–52); "closed" no longer occurs; (C) carried at r2:59–60, :155–157, :395 | yes; one nit (C5) |
| F3 | yes (r2:372–378) | yes: Proposition 2 covers FC-1 and FC-2 on `ε < 1/48`; Theorem 1 is silent on `1/96 ≤ ε < 1/48` |
| F4 | yes (r2:245–261) | yes: the exchange-mode line is correct (§3.1) |
| F5 | yes (r2:418–422) | yes |
| F6 | yes (r2:424–449); nothing classified NEW | yes, with the C-MEAS correction (§5; change C4) |
| F7 | yes (r2:216–217, :514–519) | yes |
| F8 | yes (r2:47–49, :105–110, :500–502) | yes: S2:195, :200 |
| F9 | yes (r2:174–178, :303–310) | yes. Reducing Lemma 5 to hypotheses 6–8 is correct: its proof uses neither the rule nor H-μ |

Nothing was declined, and I found no finding applied wrongly.

***

## 2. Control K1, re-derived

The control now uses one fact outside the unit: a bijection preserves the multiset of atom
probabilities of a law. That is independent of Lemmas 2–5 and of Theorem 1.

**C-POS-1.** Checked at HA5:116–120 and :128–135. `μ_n(a·λ > 0) = (1 + a·n)/2` re-derived:
`(n·λ)_+ = (n·λ + |n·λ|)/2`, `∫_{a·λ>0} λ dΩ = πa`, and by evenness half of `∫|n·λ| dΩ = 2π` lies in
any hemisphere, so the probability is `(π a·n + π)/(2π)`. The reset `μ_{sa}` is supported on
`sign(a·λ) = s`. "Read `a`, read `a`" has `m` atoms; "read `a`, read `b`" has `2m`. **(T) fails.**
Confirmed.

**C-POS-2.** I opened `finite-a2-v5/REPORT.md` (lines 1–300) and re-derived every step the control
uses.
- *Support of `ν_n`.* The weight is `⌊2^W g_n(p_i)⌋` with `g_n ∝ (n·p)_+` (FA2:80, :91), so it is
  zero where `n·z_i ≤ 0`. Rounding the cumulative probabilities down (FA2:93–94) gives a label of
  zero weight an empty interval, so it gets no mass. `ν_{−n}` is the antipodal mirror (FA2:95–96).
  So `ν_{sa}` is supported on `s a·z_i > 0`, and a second read of `a` returns `s` exactly.
- *The coupling bound, with its constants.* `|∂_u g_n| ≤ 1 + 2 = 3` because `|n_u|/r⁴ ≤ 1` and
  `4|u||n·p|/r⁶ ≤ 4|u|/r⁵ ≤ 2`. A midpoint differs from a point of its cell by at most `1/M` per
  coordinate, so the integrand differs by at most `6/M`; over six faces of area 4 this is `144/M`.
  Flooring costs less than `2^{-W}` per label, times the cell area `4/M²`, times `6M²` labels:
  `24/2^W`. With `E` their sum, `Σ|q_i/S − J_i/π| ≤ (E + |S − π|)/π ≤ 2E/π ≤ 96/M + 16/2^W` in
  `ℓ¹`, so the total variation is at most `48/M + 8/2^W`. Rounding the `N − 1` interior cut points
  moves at most `2^{-B}` each: `η`. So `τ = 48/M + 8/2^W + η`. The band `|a·λ| ≤ 2/M` has area
  `8π/M`, and `∫_band (n·λ)_+/π = ∫_band |n·λ|/(2π) ≤ 4/M`. So one read differs with probability
  at most `κ = τ + 4/M`. This agrees with FA2:150–164 line by line. One pass, by hand.
- *The two cases.* If `κ < 1/4`, the second sign of "read `a`, read `b`" has probability within `κ`
  of `(1 + s a·b)/2 ∈ [1/4, 3/4]`, so strictly between 0 and 1: `2m` atoms against `m`. If
  `κ ≥ 1/4`, the row's floor is at least `min(1, 2κ) ≥ 1/2` for `h = K ≥ 2`, and failure below
  `1/96` contradicts nothing the row states.

**The control is sound. Keep it.** Its reliance sentence can now say that the constants were
re-derived once by the confirmation review (change C5).

**R-nl.** Both rows of T3 were recomputed in `REVIEW-r1.md` and again by the writer; the multisets
`{27, 90, 126}` and `{51, 51, 141}` differ. Confirmed.

Two line references are off by two (change C5): the definition of "holds for the class" is at
P:705–706 and of "applies" at P:706–709.

***

## 3. New text in r2

### 3.1 Proposition 2 in exchange mode (r2:281–285): supported

Re-derived. Let the witnesses be heralded or adaptive policies, padded with `c(0)`. The test label
`c_u` is written at the start of round `K − 1`, and a test's labels never depend on the
preparation's records (AF:99–100). Let `x` be the world configuration before that exchange. The
round's record is the `O`-history of `Φ^t((I − Π_C)x + ι(c_u))` together with `c_u`. Replacing `c_a`
by `c_b` adds the `O`-history of `Φ^t ι(c_b − c_a)` and `c_b − c_a`: one fixed element `δ`, the same
for every `u`, every prefix policy and both witnesses. The prefix records are unchanged for every
`u`, so the accepted event is the same event. Step 1 holds for such witnesses by Lemma I
(S4:278–281). Steps 3 and 4 are unchanged. The extension is correct.

### 3.2 R1 (r2:459–469): supported

This is the observation of `REVIEW-r1.md` §4 with a correct proof and constant. §6.3 below
strengthens it.

### 3.3 R2 (r2:471–475): supported after one correction

The first sentence is right for every coset-uniform law. The second is not: under a coset-uniform
law a neighbour's value need not be uniform on `V` (a point mass is coset-uniform). It needs the
uniform law. It also needs the mode: in initial-condition mode the shared slice is all of `O`; in
exchange mode it is `O ∖ C` and there is no `P`. With those two qualifications the statement is
correct: `x_o(1) = Σ_nn x_j(0) − y_o(0)` contains one unread, uniform, independent summand.
Replacement text: change C1.

### 3.4 R3 (r2:477–481): supported

In W-nl-2's interface `x_o(1) = h(c + S_5) − y_o(0)` with `c` the current component of the first
block (S4:181–183), and no other block is within distance 1 of `o`. The two largest entries of rows
`a = 0, 1, 2` of T3 sum to 216, 192, 216 out of 243. R1 gives `1 − 2ε ≤ 8/9`. Confirmed, and its
last sentence states its scope correctly.

***

## 4. Theorem 1: statement, hypotheses, consequence

**Every hypothesis the proof uses is listed.** Lemma 1 uses 1, 3, 4, 5. Lemma 3 uses 7 (with
AF:107 for the product form, and rank one for `π(k_2|k_1)`). The comparison uses 6 and 8. I looked
for unlisted inputs and found none: disjoint class supports are in 7 ("two-class split"); the same
instrument at both rounds is in 7 ("label and class only"); free filler is in 3.

**Nothing is listed that the statement does not need.** Hypothesis 2 is not used by the algebra,
which holds on any site set. It states where the schema lives and carries H-∞, which the conclusion
must carry. That is a scope hypothesis and should stay.

**"Classes A, B, C fail Q5′, hence T1" (r2:384–401).** Exactly what follows. Hypotheses 1–7 hold for
every interface of an R-lin family in the schema under a law on the D3 list. With `F` posed for the
empty preparation, Theorem 1 gives failure at `ε < 1/96`, `K ≥ 2`. Otherwise an unheralded prefix of
length 1 with a fixed label always exists at `K ≥ 3` and Corollary 1a gives `ε ≥ 1/128`. T1 requires
Q5′ at every `ε > 0` and every `K ≥ L + 1 ≥ 3`. The sentence is conditional on 6 and 7; see §6.9 and
change C3.

One nit: r2:28 says "under the hypotheses 1–8", but 8 is the assumption being refuted (change C5).

***

## 5. Classification against `main`

- **M1 Corollary A′** (M1:424–427) and **OA-1 N2, N3** (OA1:369–375, :392): quoted exactly in r2.
  They state the mechanism: under an affine rule the joint law of all records does not depend on
  the setting, while the comparator's does.
- **C-MEAS** is not the same mechanism. Its world is a non-disturbing read with a fresh independent
  seed at each use: "The first record conditions q_1 but leaves the point signal z_theta
  unchanged. The fresh q_2 remains independent with law mu" (MS:87). It fails the same two-read test
  (S2:238–244) for a different reason. It is a precedent for the test, not for label translation.
  The wording "the mechanism is stated on `main` in three places" came from my own first review
  and should be corrected (change C4).
- **Nothing in r2 is claimed as new that is on `main`.** No finding is classified NEW.
- **The stated additions are not on `main`.** A search of `main` for "L5.4" finds it only in
  Sessions 3 and 4 and in the OA-1 reports, each time as open (OA1:365–367, :609). No file under
  the TUNE-1 drafts, the OA units or MECH-1 contains the bounds `1/96` or `1/128`, and no record
  read tests R-lin against `F(ε; 𝒯_R)` alone.

ELABORATING is the right class for Theorem 1, Corollary 1a, Proposition 2 and Lemma 5.

***

## 6. Rule-free shared-record question

**Status of this section.** Everything in §§6.3–6.7 is reviewer-authored: one derivation each, by
hand, **not independently checked**. Lemma S and Proposition E are stated with full hypotheses and
self-contained proofs so that a separate checker can test them. No statement elsewhere in this
review, and nothing in r2, depends on them.

### 6.1 What the shared coordinate is

It is a physical state component that the record lists twice. It is not a copy of earlier history
made by the rule, and it is not a newly measured outcome.

- The phase space is "a pair (previous value, current value) at each site" (P:74).
- "The record of the round is the **complete history of `O`**: its configuration at each of the
  `τ` ticks, `h_j ∈ ((V × V)^O)^τ`, together with `c_j`" (P:167–168).
- "`Φ_F` copies each cell's current value into its previous-value component" (P:201).

Round `j` lists the configurations after ticks `(j − 1)τ + 1, …, jτ`. The last of them is
`(x_O(jτ − 1), x_O(jτ))` and the first of round `j + 1` is `(x_O(jτ), x_O(jτ + 1))`. So `x_O(jτ)`
appears as the current component at the last tick of `h_j` and as the previous component at the
first tick of `h_{j+1}`. In exchange mode the exchange replaces the content of `C`, so the overlap
is `x_{O∖C}(jτ)`.

### 6.2 The map from record to outcome, and what Q5′ compares

- **The outcome map.** Each read label "has a two-class split of its records" (AF:88–89). The
  outcome of a round is the class of its record, `κ_u(h_j) ∈ {u1, u0}`. The split is declared by
  the family with the target.
- **What Q5′ compares.** Not outcomes. Credit is "the direct total variation" between "the world's
  law of `(r, records of T)`" and `Σ_r w_r δ_r ⊗ 𝔔*(σ_r · T)` (AF:127–130), where `𝔔*(σ · T)` "is
  the law of `T`'s records when the target instruments act on `σ`" (AF:107) and the instrument is
  `𝓘*_{c_a,h}(σ) = q_a(h|a1) P_a σ P_a` with "fixed conditional record laws" (AF:89–91). D4 says
  the same of the comparator: the class coarse-grainings "are not a readout rule and do not change
  `d_K`, which compares complete records" (P:275–277).
- **The target's joint law of the overlap.** Under AF's target a round's record is drawn from
  `q_v(· | class)`, whatever the earlier records were. Two successive records are independent given
  the two classes. A coordinate common to both is therefore, in the target, two conditionally
  independent draws. AF has no clause that lets a round's record law depend on an earlier record.
  So the target does not represent a persistent classical memory inside a round's record.
- **Is a contradiction forced?** No. The family chooses `q_u`, and can make the shared coordinate
  degenerate (one value). Then the event "the two entries differ" has target probability 0 and
  nothing follows. What the target forces is degeneracy, not a positive error. Lemma S makes this
  exact.
- **The same quantities on both sides.** Pushed through the outcome map, the overlap imposes
  nothing: a class split may ignore the shared coordinate. The constraint exists only in the
  comparison of complete records. It does not come from treating one stored value as two
  measurement outcomes; it comes from the target drawing one physical coordinate twice. It must not
  be extended to other readouts without a further argument (§6.6).

### 6.3 Lemma S (reviewer-authored, not independently checked)

**Hypotheses.**
- (S1) Pair form: a cell's configuration is (previous, current), and after one tick the previous
  component equals the current component before it. No other property of the update is used: any
  map `G` in `(y, x) ↦ (x, G(x) − y)`, any site set, any law (it may even depend on the labels).
- (S2) Records: a round's record lists the configuration of `O` at each of its `τ ≥ 1` ticks (D4).
- (S3) Mode: let `D = O` in initial-condition mode and `D = O ∖ C` in exchange mode. Let
  `X = x_D(τ)`, `f(h_1)` its copy in the last tick of round 1 and `f′(h_2)` its copy in the first
  tick of round 2.
- (S4) Target: for the two-round test `(c_u, c_v)` on a state `σ`, the target law is
  `L_uv = Σ π(k_1, k_2) q_u(·|k_1) ⊗ q_v(·|k_2)` with `π(k_2|k_1) = Tr(P^v_{k_2} P^u_{k_1})`,
  `|a·b| ≤ 1/2`, and `q_v` the same in every test (AF:88–91, :107).
- (S5) Credit: one state `σ` has `TV(W_uv, L_uv) ≤ ε` for the tests `(a, b)` and `(b, a)`, and for
  whichever of `(a, a)`, `(b, b)` the conclusion is wanted. `ε < 1/32`.

**Statement.** For each `v ∈ {a, b}` there is one configuration `x^in_v ∈ V^D`, determined by `q_v`
alone, with `P_W(x_D(τ) = x^in_v) ≥ 1 − 17ε` in every credited test whose second label is `c_v`.

**Proof.** Take `u ≠ v`.
1. In the world `f(h_1) = f′(h_2)` always. So `P_L(f ≠ f′) ≤ ε`.
2. Let `A_{k_1}` be the law of `f` under `q_u(·|k_1)`, `B_{k_2}` the law of `f′` under
   `q_v(·|k_2)`, and `s(k_1, k_2) = Σ_x A_{k_1}(x) B_{k_2}(x)`. By (S4),
   `P_L(f ≠ f′) = Σ π(k_1, k_2)(1 − s(k_1, k_2))`.
3. Let `k*` be a first class with `π(k*) ≥ 1/2`. Since `π(k_2|k*) = (1 ± a·b)/2 ≥ 1/4`,
   `π(k*, k_2) ≥ 1/8` for both `k_2`, so `1 − s(k*, k_2) ≤ 8ε`.
4. Let `x°` maximize `A_{k*}`. From `s ≤ max A` we get `A_{k*}(x°) ≥ 1 − 8ε`. From
   `s ≤ A(x°)B(x°) + (1 − A(x°)) ≤ B(x°) + 8ε` we get `B_{k_2}(x°) ≥ 1 − 16ε` for both `k_2`.
5. As `16ε < 1/2`, `x°` is the unique point carrying more than half of `B_0` and of `B_1`. It
   depends on `q_v` only. Call it `x^in_v`.
6. In any test with second label `c_v` the target's law of `f′(h_2)` is a mixture of `B_0` and
   `B_1`, so it puts at least `1 − 16ε` on `x^in_v`. The world's law is within `ε` of it, and in the
   world `f′(h_2) = x_D(τ)`. ∎

The proof uses no additivity, no property of the law, no herald, no preparation other than the
empty one, and no adaptivity. It does not use the classes of the world's records at all.

**Corollary S1 (initial-condition mode, `τ = 1`).** Under (S1)–(S5) with the four tests credited
for one `σ`, `ε ≥ 1/288`. *Proof.* With `τ = 1`, `h_1 = (x_O(0), x_O(1))` and `x_O(0)` is fixed by
`r_O`, so `h_1` is a function of `X`. By Lemma S, in the tests `(a, b)` and `(b, a)` the first
record is one fixed record with probability at least `1 − 17ε`, so its class is fixed with that
probability, and the target's first class has probability at least `1 − 18ε`:
`min(p_u, 1 − p_u) ≤ 18ε` for `u = a` and `u = b`. Then `|α|, |β| ≥ 1 − 36ε`, so
`α² + β² ≥ 2 − 144ε`, and `α² + β² ≤ 3/2`. ∎

**Remark (R2 at every `τ`; unreviewed).** Under R-lin and the uniform product law in
initial-condition mode, `x(τ) = P_τ(A)x(0) − P_{τ−1}(A)y(0)` with `P_τ` monic of degree `τ`. The
coefficient of `x_{i+τe}(0)` in `x_i(τ)` is 1 for a unit vector `e` (one path of length `τ`; on a
torus of side greater than `2τ`). If that site lies outside `O ∪ P`, `x_i(τ)` is uniform on `V` and
Lemma S gives `1/q ≥ 1 − 17ε`, so `ε ≥ 1/34` for every `q ≥ 2`. This is narrower than Theorem 1 (one
law, one mode, a condition on the layout).

### 6.4 Proposition E: a non-additive rule that meets Q5′ (reviewer-authored, not independently checked)

**Statement.** There is a second-order rule `Φ_G(y, x) = (x, G(x) − y)` over `V = ℤ/2` on a finite
site set, with `G` not additive, and an interface in exchange mode under H-write, with the uniform
law, complete-history records (D4) and `τ = 4`, such that `F(0; 𝒯_R)` holds at every horizon `K`
for a target with `a·b = 0`. So Q5′ holds at `ε = 0`.

**Construction.** Sites: `O = {o, p, κ, κ₂}` with `C = {o}`; unread: two registers `A`, `B` and a
chain `r_1, …, r_N`, `N ≥ 4K + 4`. Law: uniform on the unread cells. Ready configuration:
`p = (0, 0)`, `κ = (1, 0)`, `κ₂ = (0, 0)`. The rule, with `x_s` the current value of site `s`:
- `G_o = 0`, `G_κ = 0`, `G_{κ₂} = 1`;
- `G_p = (1 + x_κ)·[(1 + x_o) x_A + x_o x_B]`;
- `G_A = x_κ (1 + x_{κ₂}) · x_o · x_{r_1}` and `G_B = x_κ (1 + x_{κ₂}) · (1 + x_o) · x_{r_1}`;
- `G_{r_1} = x_{r_2}`, and `G_{r_i} = x_{r_{i+1}} + x_{r_{i−1}}` for `i ≥ 2`.

The products of `x_o` with `x_A`, `x_B` and `x_{r_1}` are what make `G` non-additive. Read labels:
`c_a = (0, 0)` and `c_b = (1, 1)` as (previous, current) of `o`.

**Verification, by time-stepping a round that starts at `T ≡ 0 (mod 4)`.**
1. *Clocks.* `x_κ(t) = t mod 2`. `x_{κ₂}(t) = 0, 1, 1, 0` for `t ≡ 0, 1, 2, 3 (mod 4)`. So the
   factor `1 + x_κ` is 1 at even times, and `x_κ(1 + x_{κ₂})` is 1 only at `t ≡ 3`.
2. *Label cell.* After the exchange `o = (c^y, c^x)`. With `G_o = 0`, `x_o` is `c^x` at `T`, `T + 2`,
   `T + 4` and `c^y` at `T + 1`, `T + 3`.
3. *Registers.* `G_A` and `G_B` vanish except at `t ≡ 3`. So their even-time values `β_A`, `β_B`
   are constant during the round, and at `T + 4` exactly one changes:
   `β_A ← β_A + c^y f`, `β_B ← β_B + (1 + c^y) f`, with `f = x_{r_1}(T + 3)`.
4. *Fresh bit.* By induction `x_{r_i}(t)` contains `x_{r_{i+t}}(0)` with coefficient 1 and no cell
   beyond it. So `x_{r_1}(t)` is uniform and independent of everything that does not depend on
   `x_{r_{1+t}}(0)`, which includes all records and register values up to time `t`.
5. *Pointer.* Assume `x_p(T − 1) = x_p(T) = 0`. Then `x_p(T + 1) = k`, where `k = β_A` if `c^x = 0`
   and `β_B` if `c^x = 1`; `x_p(T + 2) = 0`; `x_p(T + 3) = k + k = 0`, because `x_o(T + 2) = c^x`
   and the registers are unchanged; `x_p(T + 4) = 0`. The assumption holds again at `T + 4`.
6. *Record.* The round's record is a fixed injective function of `(c_j, k)`: `o` shows the label,
   the clocks are deterministic, and `p` shows `(0, k, 0, 0, 0)`. The class is `k`. The conditional
   record laws are point masses.
7. *Classes.* A read `c_a` shows `β_A` and re-randomizes `β_B`; a read `c_b` shows `β_B` and
   re-randomizes `β_A`. Initially both are uniform and independent. So a repeated read repeats its
   class, and a different read returns a fresh uniform bit independent of all earlier records.
   That is the Lüders law for `a·b = 0`.
8. *Every admissible preparation.* The four labels of the menu show one register and re-randomize
   one. Given the complete record of any prefix, adaptive or not, the registers are in one of
   three situations: `β_A` known and `β_B` uniform; `β_B` known and `β_A` uniform; both uniform. I
   checked the twelve transitions; the set is closed, and in each situation the future depends on
   the record only through it. Credit the eigenstate of `a`, the eigenstate of `b`, or `𝟙/2`. The
   world's law of (prefix record, test records) then equals the comparator's exactly, for every
   test in `𝒯_R`. A herald is a set of prefix records, so the conditional law is also exact. ∎

The shared slice is `x_{O∖C}(4j) = (0, 0, 0)`: one configuration, as Lemma S requires. The
round-one and round-two records of `(c_a, c_a)` have 2 atoms and of `(c_a, c_b)` have 4, so
property (T) fails, as Lemma 5 requires.

**What the construction is not.** `G` is designed, site-dependent and not nearest-neighbour; the
site set is not the cubic lattice; the rule is not in 𝓡 and is not R-nl. It is of the kind the
proposal stipulates for control C-PROG (P:687). It has no gates and does not meet Q3′ or Q6′.

**Initial-condition mode (sketch only; not verified end to end; not relied on).** The same logic
with `o` replaced by the first cell of a tape of block cells, held static while it is read, and the
tape shifted by one cell between reads. A content-oblivious swap of two cells' full states is a
product of five alternating linear moves of the two time-layers
(`diag(P, P) = U(P) L(P) U(P + 𝟙) L(𝟙) U(𝟙)` over `𝔽_2`), gated by a clock in `O` with the period
of the round. I checked the three components separately and did not time-step the assembly.

### 6.5 Can the floor be recomputed without additivity?

- **A positive floor for every rule does not survive.** In exchange mode at `τ = 4` Proposition E
  has `ε = 0`.
- **What the non-additive rule does that removes it.** Three things, none available to an additive
  rule: it shows one of two hidden registers according to the label (a product of label and hidden
  value); it re-randomizes the other register according to the label (a product of label and fresh
  bit); and it returns the read region to one fixed configuration before the round ends, so that
  nothing but the class passes between rounds. The first two change the dependence between
  successive complete records with the label, which Lemma 5 demands and Lemma 1 forbids for an
  additive rule.
- **Where a rule-free floor does survive.** Corollary S1: initial-condition mode with `τ = 1`,
  `ε ≥ 1/288`, for every second-order rule, law, layout and carrier. And Lemma S itself, as a
  constraint and not a floor, at every `τ` in both modes.

### 6.6 Heralds, laws, adaptivity; and the form of the target

**Heralds, initial laws, adaptive protocols.** `F` quantifies universally, and the empty
unheralded preparation with the four constant tests is among its required instances (AF:121, :127,
:134–135). Failing one required instance fails Q5′, whatever heralds or adaptive protocols exist
elsewhere. Theorem 1 uses H-μ and nothing else of the law. Lemma S uses nothing of the law. So
within the schema neither conclusion is weakened by heralding, by the choice of law on the D3
list, or by adaptivity.

**The form of the target is load-bearing for both.** This is the qualification that matters.
- Theorem 1's proof compares complete-record laws against a target that is a product given the
  classes (hypothesis 7). It does not survive if the comparison is made on outcomes only. An
  additive world, by hand: label-free bits `g_a, g_b` (shown in round 1) and `t_a, t_b` (fresh in
  round 2); the round-2 record is `(g_a, g_b, t_a, t_b, λ)` with `λ` the first label, an additive
  shift; the class of a `v`-round is `g_v` if `λ = v` and `t_v` otherwise. Its classes follow the
  Lüders law for `a·b = 0` from `𝟙/2` on all four two-round tests, and the second class is fresh
  given the complete first record. Its complete-record laws are shifts of one another, as Lemma 1
  says.
- This world does what M1 Corollary A′ calls "choosing afterwards which record to consult"
  (M1:424) and what OA-1 D7 calls a coarse-graining of one joint record (OA1:204–205). Q5′ as
  defined rejects it: under `(a, b)` the round-2 record still contains `g_a`, the first class,
  which the target's `q_b(·|k_2)` cannot depend on. So the memoryless form of the target is what
  gives Q5′ its force against a declared class split acting as a decoder (D4, P:272–273: "No pointer
  function, response function, threshold or decoder is chosen").
- I did not derive whether an additive rule can meet a class-level or memory-tolerant version on
  all of `𝒯_R`. For a coset-uniform law the two-round case shows the only route: the label history
  must move the record into a different coset of the record group, where the class split is a
  different function. That is open.

### 6.7 Alternative record representations

The constraint of the coordinator's item 6 is applied to each.

| Representation | Information kept? | Same test? | Available in the schema? |
|---|---|---|---|
| Schema as written: list of round records; class of the current record is the outcome; record law fixed by label and class | all | — | yes: D4 (P:272–277), AF:88–91, :107 |
| Drop the duplicated boundary slice from one of the two records | all: the duplicate always agrees, so the map is a bijection on the world's support | not identical, but no weaker in kind: Theorem 1 holds verbatim (the records stay additive images and the target keeps its form); the exact-copy form of Lemma S goes, but the interior of `O` at tick `jτ + 1` is still a function of the previous record | a change to how P:167–168 partitions ticks into rounds; small, but a change |
| Keep complete records; let a round's record law depend on earlier records (persistent classical memory), classes Lüders | all | no: weaker. It readmits the additive world of §6.6 on two-round tests | no: it changes AF:88–91 and :107 (B1.1). An owner decision |
| Class-only or thresholded records | no: discards what the observer reads | no | no: contrary to D4 and D5 (P:272–280) |

**The representation asked about** (full accessible history kept, current outcome distinguished
from it). The schema already has this distinction at the level of rounds: the history is the list
`(h_1, …, h_K)` whose joint law is compared (P:181–182; D4), and the current outcome is the class of
the current round's record (AF:88–89). What the schema does not allow is to declare part of the
*current* round's record to be retained history, so that its law may depend on earlier records.
That needs target instruments indexed by earlier records and is a change to AF B1.1, not a reading
of it. If it is made, it needs its own guard against the decoder of §6.6; I do not have one to
propose, and none is on record.

### 6.8 Class D: what this does and does not imply

**Does imply** (conditional on Lemma S and Proposition E being checked).
- Complete-history records do not by themselves exclude a non-additive rule from Q5′. Class D is
  not decided by the record convention.
- Any R-nl candidate must meet Lemma S: at every read-round boundary `x_O` (initial-condition mode)
  or `x_{O∖C}` (exchange mode) is one fixed configuration up to `17ε`, whatever the class. With
  Lemma 5 this is a second necessary condition, and it does not involve the labels.
- In initial-condition mode an R-nl interface with `τ = 1` fails Q5′ below `1/288` (Corollary S1);
  R3 is an instance with a better constant.

**Does not imply.**
- That R-nl can meet Q5′. Proposition E's rule reads arbitrary cells, differs from site to site and
  multiplies a label by a hidden value directly. R-nl has one fixed map, the rounded neighbour sum,
  in which a cell's own value does not enter. Whether it can do the three things of §6.5 is not
  derived. NL-A and NL-P stand as they were.
- That R-nl cannot. Nothing here is a no-go for class D beyond the `τ = 1` corner.
- Anything about Q3′, Q6′ or T1 for a non-additive rule.
- That non-linear dynamics is refuted, or supported, under any other admissible observer interface.

### 6.9 The four outcomes

- **(i) Fails only for additive dynamics.** Not established as "only". Established, conditional on
  Proposition E: under Q5′ as AF defines it, every additive rule fails (Theorem 1) and the interface
  does not force that failure, since a non-additive second-order rule passes in exchange mode. So
  within the schema the obstruction of Theorem 1 is specific to a property of the dynamics, namely
  (T). In initial-condition mode I have a sketch only.
- **(ii) Fails for every rule under the complete-history interface.** False in exchange mode
  (Proposition E). True in one corner: initial-condition mode with `τ = 1` (Corollary S1). At other
  `τ` in initial-condition mode: open, with a sketch against.
- **(iii) A mismatch between the record encoding and the quantum target.** Present, and it is the
  source of the shared-record constraint: AF's target draws each round's complete record afresh
  given its class, so it cannot represent a random value that persists in the read region. It is a
  constraint on every rule (Lemma S), not a failure of every rule, and it is not a case of one
  value read as two outcomes. Theorem 1 also depends on this form of the target (hypothesis 7).
- **(iv) Survives under a valid alternative representation.** Open. The memory-tolerant alternative
  keeps all information but is a weaker test, readmits post-hoc selection on two-round tests, and is
  a change to AF B1.1. Whether an additive rule passes it on all of `𝒯_R`, and whether a guarded
  version exists, are not derived.

**Consequences for how r2 is stated.**
- The additive theorem stays an elaboration. It should not be credited with separating R-lin from
  R-nl: nothing is known about R-nl. It may be credited with identifying a property, (T), that
  every additive rule has and every passing rule must lack; that statement does not depend on §6.
- L5.4–L5.6 are decided for Q5′ as the governing text defines it. They are not decided "without
  qualification": the qualification is hypotheses 6 and 7, and r2 should say so where it says the
  rows are answered (change C3).

### 6.10 Exact open questions

1. Is there an R-nl interface, with `τ ≥ 2` in initial-condition mode or any `τ` in exchange mode,
   that meets Lemma S and Lemma 5 at small `ε`?
2. Proposition E in initial-condition mode: complete the sketch, or find an obstruction.
3. Exchange mode at `τ ∈ {1, 2, 3}` for a general second-order rule.
4. For an additive rule and a target that tolerates persistent memory, or a class-level test: does
   failure on all of `𝒯_R` survive? (r2:506–508 poses the coarse-record half of this.)
5. A lattice-local, translation-invariant second-order rule in place of Proposition E's designed
   one.

***

## 7. Remaining changes, with replacement text

**C1 (R2).** Replace r2:471–475 by:

> **R2 (consequence for R-lin; derived here once).** Under R-lin and a coset-uniform law, `x_O(τ)`
> is uniform on a coset of a subgroup `M_τ` (Lemma 0, S3:50–54), so R1 requires `|M_τ| ≤ 2` when
> `ε < 1/6`. Under the uniform law (on `ℤ^3` the uniform product law), in initial-condition mode at
> `τ = 1`, `x_o(1) = (A x(0))_o − y_o(0)` is uniform on `V` at every site of `O` with a neighbour
> outside `O ∪ P`. So for `q ≥ 3`, `τ = 1` and such a site, R1 alone gives failure of Q5′ at
> `ε < 1/6`. In exchange mode the same holds for a site of `O ∖ C` with an unread neighbour.
> General `τ`, layouts whose blocks adjoin `O`, and other laws were not derived.

**C2 (§7, assessment 2).** Replace r2:487–490 by:

> 2. *How Theorem 1 is read.* For R-lin part of the failure of Q5′ is obtainable from R1 without
>    the translation form (R2). Theorem 1 says nothing about R-nl, so it is not evidence that
>    additivity separates R-lin from R-nl under Q5′. What it establishes that R1 as derived does
>    not is the failure for every `τ`, layout, region `O`, law and `q`, and that every passing rule
>    must lack property (T) (Lemma 5). Whether the record convention alone forces failure for every
>    rule is examined in `CONFIRM-r2.md` §6; the lemma and the construction there are
>    reviewer-authored and not independently checked, and nothing here relies on them.

**C3 (§6, "Left open").** Insert after r2:410:

> - *The form of the target.* Hypothesis 7 is load-bearing in the same way as D4. The target law of
>   two rounds is a product given the classes: a round's record law depends on its label and class
>   only, with no persistent classical memory. The proof compares complete-record laws (AF:107,
>   :127–130), not class statistics, and does not carry over to a comparison of classes alone or to
>   a target whose later records may repeat earlier ones. L5.4, L5.5 and L5.6 are answered for Q5′
>   as AF defines it.

and in r2:400 replace "because Q5′ alone fails" by "because Q5′, as AF defines it, alone fails".

**C4 (prior art).**
- r2:424: replace "The mechanism is stated on `main` in three places:" by "The mechanism is stated
  on `main` in two places, and a third record fails the same two-read test by a different
  mechanism:".
- r2:430–431: append to the C-MEAS item "; its world is a non-disturbing read with a fresh seed at
  each use (MS:87–127), so it is a precedent for the test, not for label translation".
- r2:102: replace "Prior statements of the mechanism on `main`" by "Prior statements on `main`".
- r2:443: replace "quantitative form of the three statements above" by "quantitative form of the
  two statements of the mechanism above".

**C5 (nits).**
- r2:28: replace "Under the hypotheses 1–8 below" by "Under hypotheses 1–7 below, with `F` posed as
  in 8".
- r2:342: "(P:705–708)" → "(P:706–709)". r2:350: "(P:703–704)" → "(P:705–706)".
- r2:342–344 and :351–352: replace the reliance sentences by "*Reliance:* the coupling bound is the
  source's (FA2:150–164); its hemisphere probability and its cell-integration constants were
  re-derived by hand, once, by the confirmation review."

With C1–C5 applied I have no further change to request. §§4–6 of r2 would then stand as one
hand-reviewed [W] derivation. Whether the S3 §5 rows and 3A §§3.1–3.3 are restated remains the
owner's decision (r2:503–505).

***

## 8. Checked, not checked, disclosure

**Read for this confirmation.** `L54-r2.md` and `RESPONSE-r1.md`, whole.
`finite-a2-v5/REPORT.md` 1–300. `history-architecture-v5/REPORT.md` 96–140.
`TUNE-1-STEP2-PROPOSAL.md` 676, 698–709 (again). `oi-qm-ext-1/measurement-source.md` 87–127. A
search of `main` for "L5.4", "1/96" and "1/128". Sources read for `REVIEW-r1.md` were not re-read
except where cited above.

**Not checked.** Lemma 4 (c)'s identification of OA-2's objects (unchanged from r1). N9. The public
record of C-POS-2 is not itemized in one place in its source; the control takes the sign as the
only random public datum, as r2:334–336 states.

**Reviewer-authored and unchecked.** Lemma S, Corollary S1, the remark on R2 at every `τ`,
Proposition E, the initial-condition sketch, and the two-round additive example of §6.6. Each has
one derivation, by hand.

**Commands.** `ls`, `wc`, `cat`, `sed -n`, `cat -n`, `cut`, `grep`, `find`, `awk` (line lengths), and
one `sed -i` pass on this file itself to correct six line references and one quotation. No
interpreter was run for this confirmation. All arithmetic and all time-stepping in §6.4 were done by hand.
