# K1-RDY pre-freeze items: paper proofs and an analysis of the P1 class rule

**Status of every proof in this file: written proof, not independently reviewed.** Each is a hand derivation. No
enumeration, model computation, Lean run or workflow was used. The file changes no statement of the K1-RDY text and
decides no gate, token or owner question.

## 0. Sources, scope and conventions

"The text" and "line N" are as in `verification/programmes/oi-qm/reconstruction/k1-rdy-proofs-20261105/LEMMAS.md`
§0.1 (on `main` at `4f016afd`): the K1-RDY preregistration accepted on 2026-11-02, 313 lines, recorded sha256
`a93f3f33f0c5a6e8b2467312d184fa2d2e915296490948938c4dd7832c64bb63`. The definitions D1–D10 of `LEMMAS.md` §0.2 are used
as stated there, and its Lemma P1, blindness lemma and L-O are cited by section. The statements below are reproduced
from the text; that they are the text's is checkable against the recorded sha256 once lines 1–313 are on `main`.

`LEMMAS.md` §5 item 3 lists what the text uses and that file does not prove. This file treats each item:

| `LEMMAS.md` §5 item 3 | Here |
|---|---|
| the cycle decomposition of `φ` at the instance | §2, proved |
| P3's explicit image (line 89) | §3, proved |
| TA (c4) | §4, proved in the form lines 206, 234 and 243 use |
| the conservation of ℰ behind lines 74–75 | §5, proved, with the shell count CC-LEDGER uses |
| §5.3's class rule (Q4) | §6, analysed: one direction proved, the converse not established, and the clause shown unreachable at the instance |
| (not in that list) the ledger bounds (c1)/(c2), lines 60–62 | §7, proved |
| the gates that precede G4 for a P1 member row | not a premise: decided by the round's own gates at execution (§6.4 records what the class-rule analysis needs from them) |

Notation: `𝟙 ∈ 𝐑^Λ` is the vector with every entry 1, and `⟨u, v⟩ = Σ_i u_i v_i` in `ℤ/2`. Over `ℤ/2`, `−1 = 1`.

## 1. The region `E` at the instance

**Statement** (line 198). "At the fixed instance, §2's rule gives `E = {x_1, y_1, y_2}`, `W_eq = {x_1, y_1}`."

**Proof.** By D2, `V_{t_0} = y_1(t_0)` and `V_{t_0+1} = y_1(t_0 + 1)`, and the second component of `φ` gives
`y_1(t_0 + 1) = (Ay)_1 − x_1 = y_0 + y_2 − x_1` in the state at `t_0`. The cells with a nonzero coefficient for some
offset `0 ≤ t ≤ T = 1` are `y_1` (offset 0) and `y_0, y_2, x_1` (offset 1). Removing `Σ = {x_0, y_0}` (D4) leaves
`E = {x_1, y_1, y_2}`. `W_eq` is `V`'s site set, both slices (line 43): site 1, `{x_1, y_1}`. ∎

## 2. The cycle decomposition of `φ` at the instance

### 2.1 Statement

**Proposition CYC.** At the instance of D1, `φ^{10}` is the identity, and `φ` has 156 cycles: two fixed points, the
zero state `0` and the state `(𝟙, 𝟙)`; one 2-cycle, `{(0, 𝟙), (𝟙, 0)}`; 102 cycles of length 5; and 51 cycles of
length 10. The lengths sum to `2 + 2 + 510 + 510 = 1024 = |S|`.

Uses: line 191 assigns the decomposition to execution; line 270's checkpoint requires one P1 member row per cycle
and cycle sizes summing to `|S|`; by Lemma P1(a) the members `u_c` of `𝓘` are indexed by these cycles.

### 2.2 Proof of Proposition CYC

*Ring form.* Identify `u ∈ 𝐑^Λ` with `Σ_i u_i X^i` in `R := 𝔽_2[X]/(X^5 − 1)`. Then `(Xu)_i = u_{i−1}` and, since
`X^{−1} = X^4`, `(X^4 u)_i = u_{i+1}`. So `A` is multiplication by `a := X + X^4`, and `φ(x, y) = (y, a y − x)` is an
`R`-linear map of `S = R × R`.

*Splitting `R`.* Over `𝔽_2`, `X^5 − 1 = (X + 1) Φ` with `Φ := X^4 + X^3 + X^2 + X + 1`. `Φ` is irreducible: it has no
root in `𝔽_2` (`Φ(0) = Φ(1) = 1`), so a factorization would be a product of two irreducible quadratics; the only
irreducible quadratic over `𝔽_2` is `X^2 + X + 1`, and `(X^2 + X + 1)^2 = X^4 + X^2 + 1 ≠ Φ`. `X + 1` and `Φ` are coprime
(`Φ(1) = 1`). By the Chinese remainder theorem, `u ↦ (u(1), u mod Φ)` is a ring isomorphism
`R → 𝔽_2 × K` with `K := 𝔽_2[X]/(Φ)`, a field of 16 elements. Let `ζ ∈ K` be the class of `X`: `ζ^5 = 1` and `ζ ≠ 1`, so
`ζ` has order 5, and `ζ^{−1} = ζ^4`. The isomorphism carries `S = R^2` to `𝔽_2^2 × K^2`, and `φ` acts factorwise by
`(u, v) ↦ (v, a′v − u)`, where `a′` is the image of `a`: `a′ = 1 + 1 = 0` in `𝔽_2`, and `a′ = ζ + ζ^{−1}` in `K`.

*The `𝔽_2` factor* (4 states). The map is `(u, v) ↦ (v, u)`. Its fixed points are `(0, 0)` and `(1, 1)`, and `(1, 0)`,
`(0, 1)` form a 2-cycle. So two states have period 1 and two have period 2.

*The `K` factor* (256 states). The map is the matrix `M` with `M(u, v) = (v, u + (ζ + ζ^{−1}) v)`. For `λ ∈ K`,
`M(1, λ) = (λ, 1 + (ζ + ζ^{−1}) λ)`, which equals `λ (1, λ)` iff `λ^2 + (ζ + ζ^{−1}) λ + 1 = 0`, that is
`(λ + ζ)(λ + ζ^{−1}) = 0`. So `e_1 = (1, ζ)` and `e_2 = (1, ζ^{−1})` are eigenvectors with eigenvalues `ζ` and `ζ^{−1}`,
which differ because `ζ^2 ≠ 1`; hence `e_1, e_2` form a basis of `K^2`. For `b = β_1 e_1 + β_2 e_2`,
`M^k b = ζ^k β_1 e_1 + ζ^{−k} β_2 e_2`, which equals `b` iff `(ζ^k − 1) β_1 = 0` and `(ζ^{−k} − 1) β_2 = 0`. For `b ≠ 0`
one of `β_1, β_2` is nonzero, so `M^k b = b` iff `5 | k`. The zero vector has period 1 and the other 255 states have
period 5.

*Combining.* A state is a pair `(α, b)`, with `φ^k(α, b) = (α, b)` iff both factors return, so its period is the least
common multiple of the factor periods. Counting pairs: period 1, `2 · 1 = 2` states; period 2, `2 · 1 = 2` states (one
cycle); period 5, `2 · 255 = 510` states (102 cycles); period 10, `2 · 255 = 510` states (51 cycles). Every period
divides 10, so `φ^{10}` is the identity.

*Naming the short cycles.* The states with `K`-component `0` are those with `x ≡ y ≡ 0 mod Φ`. The multiples of `Φ` in
`R` are `0` and `Φ` itself: for `g ∈ R`, `g − g(1)` is divisible by `X + 1` and `(X + 1) Φ = 0` in `R`, so
`g Φ = g(1) Φ`. Hence `x, y ∈ {0, 𝟙}` (`Φ` is the vector `𝟙`). Their
`𝔽_2`-components are `(x(1), y(1))` with `𝟙(1) = 5 = 1`: `(0, 0) ↦ (0, 0)`, `(𝟙, 𝟙) ↦ (1, 1)`, and `(0, 𝟙)`, `(𝟙, 0)` give
the 2-cycle. Directly: `A𝟙 = 2 · 𝟙 = 0`, so `φ(𝟙, 𝟙) = (𝟙, 0 − 𝟙) = (𝟙, 𝟙)` and `φ(0, 𝟙) = (𝟙, 0)`. ∎

### 2.3 Scope

The decomposition is of the instance only. It lists the members of `𝓘` (Lemma P1(a)) and fixes the counts behind
line 270's checkpoint. It evaluates no member row.

## 3. P3's image at `t_0`

### 3.1 Statement

Lines 86–90: "As functions of the state at `t_0`, `x(t−1) = Ax(t) − y(t)` gives `y_1(t_0 − k)` for `k = 0, 1, 2, 3` as
`y_1`, `x_1`, `x_0 + x_2 − y_1` and `x_1 + x_3 + x_4 − y_0 − y_2`. Since `W(t) = (y_1(t − 1), y_1(t))`, `O` holds iff these
four values are equal. Mod 2 that is `Im_O = {x_1 + y_1 = 0, x_0 + x_2 = 0, x_3 + x_4 + y_0 + y_2 = 0}`, a subgroup of
index 8, so `π_0(O) = 1/8` and `D(μ_O) = 3 log 2` (TA (c5))." `O` is "`W`'s configuration is identical at each tick of
`[t_u − 2, t_u]`", `W = W_eq`, `t_u = t_0` (lines 78–80).

### 3.2 Proof

*Backward step.* `φ^{−1}(x, y) = (Ax − y, x)` (D1), so `x(t − 1) = A x(t) − y(t)` and `y(t − 1) = x(t)`. Also, from
`s(t) = φ(s(t − 1))`, `x(t) = y(t − 1)`; hence `W(t) = (x_1(t), y_1(t)) = (y_1(t − 1), y_1(t))`.

*The four values*, all in the state at `t_0`:
- `y_1(t_0) = y_1`;
- `y_1(t_0 − 1) = x_1(t_0) = x_1`;
- `y_1(t_0 − 2) = x_1(t_0 − 1) = (Ax)_1 − y_1 = x_0 + x_2 − y_1`;
- `y_1(t_0 − 3) = x_1(t_0 − 2) = x_0(t_0 − 1) + x_2(t_0 − 1) − y_1(t_0 − 1)`, with `x_0(t_0 − 1) = x_4 + x_1 − y_0` and
  `x_2(t_0 − 1) = x_1 + x_3 − y_2`; so `y_1(t_0 − 3) = x_1 + x_3 + x_4 − y_0 − y_2`.

*The event.* `W(t_0 − 2), W(t_0 − 1), W(t_0)` are `(y_1(t_0 − 3), y_1(t_0 − 2))`, `(y_1(t_0 − 2), y_1(t_0 − 1))` and
`(y_1(t_0 − 1), y_1(t_0))`. They are all equal iff `y_1(t_0 − 3) = y_1(t_0 − 2) = y_1(t_0 − 1) = y_1(t_0)`. Mod 2, with the
values above: `y_1(t_0 − 1) = y_1(t_0)` is `x_1 + y_1 = 0`; given it, `y_1(t_0 − 2) = y_1(t_0)` is `x_0 + x_2 = 0`; given
both, `y_1(t_0 − 3) = y_1(t_0)` is `x_1 + x_3 + x_4 + y_0 + y_2 = y_1`, that is `x_3 + x_4 + y_0 + y_2 = 0`. Conversely the
three equations give the three equalities in the same order. So `O = Im_O`.

*Index and ledger.* The three equations are linear, so `Im_O` is a subgroup. Each contains a variable absent from the
other two (`y_1`, `x_0`, `x_3`), so they are independent, and `Im_O` is the kernel of a surjection `S → 𝔽_2^3`: index 8,
`|Im_O| = 128`. Hence `π_0(O) = 1/8`, `μ_O` is uniform on 128 states, `H(μ_O) = log 128`, and
`D(μ_O) = log 1024 − log 128 = 3 log 2`. ∎

### 3.3 Scope

This proves the stated image, the value the declaration predicts for G2(b)'s T2 comparison (lines 131–133). It does
not evaluate P3's rows (line 235), which execution derives from the image and `E`.

## 4. TA (c4): equal-time independence of disjoint cells under `π_0`

### 4.1 Statement

The text cites TA (c4) as "`π_0`'s equal-time independence of disjoint cells" (line 243) and uses it at line 206
(CC-ABS) and line 234 (P0's B-eq row). The statement proved, for a finite `S = 𝐑^Γ` on a finite cell set `Γ` with
`|𝐑| = q`, any bijection `φ`, and `π_0` uniform:

**Proposition IND.** For every tick `t` and every pair of disjoint cell sets `X, Y`, under `π_0` the variables `X_t` and
`Y_t` are independent and each is uniform. Hence, for cell sets `W` and `E` and `w ∈ 𝐑^W`,
`π_0(E_t = 0 | W_t = w) = q^{−|E∖W|}` if `w` is `0` on `W ∩ E`, and `0` otherwise. In particular it is `q^{−|E|}` for every
`w` when `W ∩ E = ∅`.

### 4.2 Proof

`π_0` is φ-invariant (Lemma P1(a)), so the law of `s(t)` is `π_0` at every tick (Lemma P1(b)); it suffices to take
`t = t_0`. For disjoint `X, Y` and values `a, b`, the states with `s_X = a` and `s_Y = b` are fixed on `|X| + |Y|` cells
and free on the rest, so there are `q^{|Γ| − |X| − |Y|}` of them, and `π_0(s_X = a, s_Y = b) = q^{−|X|} q^{−|Y|}`. Summing
over `b` gives `π_0(s_X = a) = q^{−|X|}`, and likewise for `Y`; so the joint law is the product of two uniform laws.
For the conditional: `{s_W = w, s_E = 0}` is empty if `w` is nonzero on `W ∩ E`; otherwise it fixes the `|W| + |E∖W|`
cells of `W ∪ E` and has `q^{|Γ| − |W| − |E∖W|}` states, against `q^{|Γ| − |W|}` states in `{s_W = w}`. ∎

### 4.3 Uses at the instance (`q = 2`, `E = {x_1, y_1, y_2}`, §1)

- CC-ABS (line 206): `W = {x_3, y_3}` is disjoint from `E`, so `r(w) = 2^{−3} = 1/8` for every `w`; no `w` is sharp.
- P0's B-eq row (line 234): `W_eq = {x_1, y_1} ⊆ E`, so `r(0) = 2^{−1} = 1/2` and `r(w) = 0` for `w ≠ 0`; no `w` is
  sharp.
- P0's B-pl row (line 233): `π_0(E_{t_0} = 0) = 1/8 < 1`; not sharp.

## 5. ℰ: conservation and the shell count

### 5.1 Statement

`ℰ(x, y) = ⟨x, x⟩ + ⟨y, y⟩ − ⟨x, Ay⟩ mod q` (the form of SM:296 at `07d94f2c`, with `(u, v) = (x, y)`;
SM:294–296 are unchanged on `main` at `4f016afd`). Line 74 states
"P2's energy-shell measures (SM:294–296) are members" of `𝓘`, and CC-LEDGER (line 209) uses "both shells have 512
states, `D = log 2`".

**Proposition EN.** (a) If `A` is symmetric, `ℰ ∘ φ = ℰ`. (b) For each value `e`, the set `{ℰ = e}` is a union of cycles,
and `μ_e := π_0(· | ℰ = e)`, when defined, is a member of `𝓘`. (c) At the instance, `{ℰ = 0}` and `{ℰ = 1}` have 512
states each, so `D(μ_0) = D(μ_1) = log 2`.

### 5.2 Proof

(a) `ℰ(φ(x, y)) = ℰ(y, Ay − x) = ⟨y, y⟩ + ⟨Ay − x, Ay − x⟩ − ⟨y, A(Ay − x)⟩`
`= ⟨y, y⟩ + ⟨Ay, Ay⟩ − 2⟨Ay, x⟩ + ⟨x, x⟩ − ⟨y, A^2 y⟩ + ⟨y, Ax⟩`. For symmetric `A`, `⟨Ay, Ay⟩ = ⟨y, A^2 y⟩` and
`⟨y, Ax⟩ = ⟨Ay, x⟩`, so the sum is `⟨x, x⟩ + ⟨y, y⟩ − ⟨x, Ay⟩ = ℰ(x, y)`. At the instance `A_{ij} = 1` iff
`j = i ± 1`, which is symmetric.

(b) By (a), `ℰ` is constant along each orbit, so each cycle lies in one set `{ℰ = e}`, and that set is a union of
cycles `c`. `μ_e` is uniform on it, so `μ_e = Σ_{c ⊆ {ℰ = e}} (|c| / |{ℰ = e}|) u_c`, a member of `𝓘` by Lemma P1(a)
("if" direction).

(c) Over `ℤ/2`, translation by `(𝟙, 0)` changes `ℰ` by
`ℰ(x + 𝟙, y) − ℰ(x, y) = 2⟨x, 𝟙⟩ + ⟨𝟙, 𝟙⟩ − ⟨𝟙, Ay⟩ = 0 + 5 − ⟨A𝟙, y⟩ = 1`, using symmetry and `A𝟙 = 2 · 𝟙 = 0`. So
`(x, y) ↦ (x + 𝟙, y)` is a bijection of `S` that maps `{ℰ = 0}` onto `{ℰ = 1}`; each has `1024/2 = 512` states. Then
`H(μ_e) = log 512` and `D(μ_e) = log 1024 − log 512 = log 2`. ∎

### 5.3 Scope

(a) and (b) hold for every symmetric `A` over `ℤ/q`; (c) is the instance. CC-LEDGER's pass condition then reads
`|E| log 2 = 3 log 2 > log 2` with `|E| = 3` (§1).

## 6. The P1 class rule (§5.3, review question Q4)

### 6.1 The rule and what it is compared with

Lines 156–163, verbatim:

> **5.3 P1 class rule** (K-17(a); no post-selection). Member rows are evaluated for `π_0` and for every cycle-uniform
> `u_c`, in increasing order of each cycle's lexicographically least state, and every member row is reported. Per
> branch, if any member row is not a positive, the class token is the first of VOID[row], Z1-VOID, UNDECIDED(Gk), ABSENT,
> BLIND attained by a member row, scoped as "not every member of `𝓘`". If every member row is positive, the class
> token is positive iff every nonempty union `C` of cycles admits a `w` with `∅ ≠ C ∩ {W_{t_u} = w} ⊆ {E_{t_0} = 0}`
> at which `NB` holds under every weighting supported on `C`. It is ABSENT if some `C` admits no such `w`, BLIND if each `C`
> admits one but `NB` fails there for some weighting, and UNDECIDED(G4) if this is not decided. In B-pl a member row is ABSENT
> if the member is not sharply ready, and BLIND by the blindness lemma if it is.

The proposal's review called the union-of-cycles test "the finite decision of 'all invariant measures'" (REV-pre,
#1031 comment 6567537517, Q4; provenance). The comparison here is with K-17(a)'s class read as "every member of `𝓘`
passes G4 with a positive outcome": for every `μ ∈ 𝓘` there is a sharp `w` at which `NB(μ(· | W_{t_u} = w))` holds.

Fix a branch, with its `W`, `t_u` and `B_w = {W_{t_u} = w}`, and `Z = {E_{t_0} = 0}` (D5). For a nonempty union `C` of
cycles let `Sh(C) := {w : ∅ ≠ C ∩ B_w ⊆ Z}`, and let `Λ(C)` be the set of weightings `λ` (probability vectors on the
cycles) whose positive entries are exactly the cycles in `C`; write `μ_λ = Σ_c λ_c u_c`. **Reading:** "every weighting
supported on `C`" is read as every `λ ∈ Λ(C)`. Under the wider reading `{c : λ_c > 0} ⊆ C`, a weighting carried by a
smaller union `C′` can give `μ_λ(B_w) = 0` at a `w ∈ Sh(C)`, and `NB` under `μ_λ(· | B_w)` is then undefined.

### 6.2 Statements

- **CR-1** (support and weighting). Every `μ ∈ 𝓘` equals `μ_λ` for exactly one nonempty union `C` of cycles, namely
  `C = supp μ`, and exactly one `λ ∈ Λ(C)`, namely `λ_c = μ(c)`; and every such `μ_λ` is in `𝓘`.
- **CR-2** (sharpness depends only on the support). For `μ ∈ 𝓘` with support `C` and any `w`: `w` is sharp for `μ`
  (D7) iff `w ∈ Sh(C)`.
- **CR-3** (the positive clause is sufficient). If every nonempty union `C` admits `w ∈ Sh(C)` such that `NB` holds under
  `μ_λ(· | B_w)` for every `λ ∈ Λ(C)`, then every `μ ∈ 𝓘` has a sharp `w` with `NB(μ(· | B_w))`.
- **CR-4** (the ABSENT clause is exact). Some nonempty union `C` has `Sh(C) = ∅` iff some `μ ∈ 𝓘` has no sharp `w`.
- **CR-5** (the converse of CR-3 is not established). "Every `μ ∈ 𝓘` has a sharp `w` with `NB`" is, by CR-1 and CR-2,
  `∀C ∀λ ∈ Λ(C) ∃w ∈ Sh(C) : NB(μ_λ(· | B_w))`, while the rule's positive clause is
  `∀C ∃w ∈ Sh(C) ∀λ ∈ Λ(C) : NB(μ_λ(· | B_w))`. The two coincide for every `C` with `|Sh(C)| ≤ 1`. When `Sh(C)` has two or
  more elements, the rule's BLIND clause ("each `C` admits one but `NB` fails there for some weighting") does not by
  itself establish that some member of `𝓘` fails `NB` at every sharp `w`. No counterexample is claimed; none was sought by
  computation.
- **CR-6** (unreachability at the instance). At the fixed instance, in each of B-pl, B-eq and B-ct, the member row of
  `δ_0` is not a positive. Hence the union clause (from "If every member row is positive" to "if this is not decided")
  is not evaluated at the instance, and in every branch the class token is the first of VOID[row], Z1-VOID,
  UNDECIDED(Gk), ABSENT, BLIND attained by a member row.

### 6.3 Proofs

*CR-1.* Lemma P1(a) gives `μ = Σ_c μ(c) u_c` with unique weights; P1(c) gives `supp μ = ⋃{c : μ(c) > 0}`, so the
positive weights are exactly the cycles in `C = supp μ`. Conversely each `μ_λ` is a convex combination of the `u_c`,
hence in `𝓘` (P1(a), "if").

*CR-2.* For `s ∈ c`, `μ({s}) = μ(c)/|c|`, which is positive iff `s ∈ C`. So `μ(B_w) > 0` iff `C ∩ B_w ≠ ∅`, and
`μ(B_w ∖ Z) = 0` iff `C ∩ B_w ∖ Z = ∅`, that is `C ∩ B_w ⊆ Z`. When `μ(B_w) > 0`, `μ(Z | B_w) = 1` iff
`μ(B_w ∖ Z) = 0`. Both directions follow.

*CR-3.* Let `μ ∈ 𝓘`. By CR-1, `μ = μ_λ` with `C = supp μ` and `λ ∈ Λ(C)`. The hypothesis gives `w ∈ Sh(C)` with
`NB(μ_λ(· | B_w))`; by CR-2, `w` is sharp for `μ`.

*CR-4.* "If": let `μ ∈ 𝓘` have no sharp `w`, and `C = supp μ`; by CR-2, `Sh(C) = ∅`. "Only if": let `Sh(C) = ∅`, and take
any `λ ∈ Λ(C)` (for example uniform on the cycles of `C`); by CR-1 `μ_λ ∈ 𝓘` with support `C`, and by CR-2 it has no
sharp `w`.

*CR-5.* The two displayed forms follow from CR-1 and CR-2 by substituting the description of `𝓘` and of sharpness. The
rule's form implies the other (choose its `w` for every `λ`). If `|Sh(C)| ≤ 1`: when `Sh(C) = ∅` both forms fail at `C`;
when `Sh(C) = {w_0}`, both reduce to `∀λ : NB(μ_λ(· | B_{w_0}))`. With two or more sharp `w`, the order of the quantifiers
is the difference, and nothing in the text or in this file excludes a `C` at which each `λ` has its own `w`.

*CR-6.* `δ_0 = u_{{0}}` is a member of `𝓘` (Lemma P1(a); `{0}` is a cycle, §2). Positive tokens are issued only when
"G1–G6 pass" (lines 177–178), and G4 passes only if some sharp `w` has `NB`: otherwise it issues ABSENT (no sharp `w`) or
BLIND (`NB` fails at each), with VOID[row] before BLIND (lines 140–143, 173–174). Under `δ_0` the state is `0` at every
tick (`φ(0) = 0`), so in each branch only `w = 0` has positive mass, it is sharp, and `δ_0(· | B_0) = δ_0`. `NB(δ_0)` fails
by the blindness lemma (`LEMMAS.md` §2.2, applied as in §2.3, CC-SCOPE). So G4, if reached, issues VOID[row] or BLIND,
and if an earlier gate issues a token, that token (UNDECIDED(Gk), Z1-VOID or VOID[stage]) is not a positive either; UNDECIDED(G6)
arises only on rows reaching a positive. In every branch some member row is not a positive, and line 158's first
sentence decides the class token. ∎

### 6.4 Scope

- CR-1 to CR-5 concern G4's sharpness and `NB` only. Whether a mixture's row passes G1–G3, G5 and G6 is not treated; the
  rule evaluates member rows for `π_0` and the `u_c` only.
- CR-5 is a gap in the claimed equivalence, not a counterexample. CR-6 shows it cannot change any token at the fixed
  instance. Whether the rule should be restated (for example in the `∀λ ∃w` form) is an owner decision; this file
  changes no statement of the text.
- The parameter fields of the class token ("first ... attained by a member row") are the subject of PF-1 and are not
  treated here.

## 7. The equal-time ledger bounds (c1) and (c2)

**Status: written proof, not independently reviewed.**

### 7.1 Statement

Lines 60–62: "`D(μ) = log|S| − H(μ) = D_KL(μ ‖ π_0)`. Equal-time bounds: B-pl sharp readiness needs
`|E| log q ≤ D(μ)` (c1); B-eq sharp readiness on `w` of mass `p` needs `p·|E∖W| log q ≤ D(μ)` (c2, the chain rule with
overlap cells counted in `W`)." G3 writes the bound for each row and G4 voids an equal-time sharp positive that breaks it
(lines 139–142).

**Proposition LEDGER.** Let `S` be finite with `|𝐑| = q`, `π_0` uniform and `μ` a probability measure on `S`.
(a) `log|S| − H(μ) = D_KL(μ ‖ π_0)`. (b) (c1): if `μ(E_{t_0} = 0) = 1`, then `D(μ) ≥ |E| log q`. (c) (c2): if `W` is read at
`t_u = t_0`, `p = μ(W_{t_0} = w) > 0` and `μ(E_{t_0} = 0 | W_{t_0} = w) = 1`, then `D(μ) ≥ p · |E∖W| log q`.

### 7.2 Proof

(a) `D_KL(μ ‖ π_0) = Σ_s μ(s) log(μ(s) |S|) = log|S| − H(μ)`.

(b) As in `LEMMAS.md` §2.3: `supp μ ⊆ Z`, `|Z| = |S| q^{−|E|}`, and `H(μ) ≤ log|supp μ|`, so
`D(μ) = log|S| − H(μ) ≥ log|S| − log|Z| = |E| log q`.

(c) By the chain rule for relative entropy over the partition `{B_v}` of `S` by the value `v` of `W_{t_0}`,
`D_KL(μ ‖ π_0) = D_KL(μ_W ‖ π_{0,W}) + Σ_v μ(B_v) D_KL(μ(· | B_v) ‖ π_0(· | B_v))`, where `μ_W` and `π_{0,W}` are the
laws of `W_{t_0}` and the sum runs over `v` with `μ(B_v) > 0`. Every term is nonnegative, so
`D(μ) ≥ p · D_KL(μ(· | B_w) ‖ π_0(· | B_w))`. Sharpness puts `ν := μ(· | B_w)` on `A := B_w ∩ Z`, which is then nonempty,
so `w` is `0` on `W ∩ E`. `π_0(· | B_w)` is uniform on `B_w`, so
`D_KL(ν ‖ π_0(· | B_w)) = log|B_w| − H(ν) ≥ log(|B_w| / |A|)`. By Proposition IND (§4),
`|A| / |B_w| = π_0(Z | B_w) = q^{−|E∖W|}`. Hence `D(μ) ≥ p · |E∖W| log q`. ∎

### 7.3 Scope

Equal time only: (c) uses `W` and `E` at the same tick, through IND. Cross-time readiness is not bounded by `D(μ)`
(line 62), and nothing here bounds it. (b) is (c) with `W` trivial (`p = 1`, `E∖W = E`). Consequence: an equal-time row
whose sharp readiness holds satisfies its G3 bound, so G4's VOID[row] is reached only by a row whose asserted readiness
does not hold, as in CC-LEDGER, whose assertion is injected (line 209).
