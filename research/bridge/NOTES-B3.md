# NOTES-B3 — finite versus continuous

Node B3 of `research/bridge`. Base L = `9f9f8257`. Evidence:
- [X] `experiments/b3_finite.py`: 11/11 PASS, VERDICT B3-FINITE-EXACT. Run 1 is kept as `.run1.*`; its output is
  identical, only its header timestamp was misstated. The final run replays byte-identically.
- [W] written here.
- [A] audited archive record.
- [L] literature, not verified here: Jordan's theorem on finite linear groups.

**Productivity test (fixed before the run).** The node is a gem iff it decides, with an exact obstruction or an exact
reduction, whether finite H-level substrata can supply the composite action that closes the gap. A restatement of
"finite order is not enough" would not count.

## 0. The question sharpened

The charter asks whether embedded observation (EO) together with the K∞ completion can source, on one token, an
off-frame finite rotation or a dense subgroup. If not, it asks for the no-go; if so, it asks for the reduction of (b)
to A_miss.

The audited record already shows that **finiteness of order is not the dividing line**. A single rational rotation of
order 3 about `(5,1,1)`, `R1 = (1/9)[[8,1,4],[4,−4,−7],[1,8,−4]]` [X3], forces `Q3` together with `cnot` and H1–H3
(stage 4, Y7 "UNIQUE" [A], INTEGRATION-NOTE-STAGE4.md:42). K(Z_F) is moved out by `actC R1`:
- my certified witness gives `−79/720` [X7];
- R6/AUDIT-R recorded `−2383/5316` with another witness [A].

The dividing line found here is whether the realized operations, **together with `cnot`**, generate a finite or a
locally finite group (a directed union of finite groups) on the pair.

## 1. One token

- **A fixed finite substratum gives a finite token group [W + X1].** Let `π ↦ O_π` send each readout-respecting
  permutation to its induced map. This is a homomorphism (`O_{π∘σ} = O_π O_σ`, exact on all 48² pairs of the
  octahedral model). Its image is a quotient of a subgroup of `Sym(Λ)`, hence finite.
- **Off-frame finite rotations are H-sourceable on one token [X3].** The 18-point ontic token
  `Λ_R1 = ⟨R1⟩·{±e_i}` consists of unit vectors. `R1` permutes it, and `R_A P_{R1} = Hom(R1) R_A` holds exactly
  (rank 4). The same holds for `cyc3` on the 6-point octahedral token (b1 H1a). The native substratum nevertheless
  yields only frame-monomial operations: the octahedral group, and with continuous phases the group `O(2)` about `z`
  (B2 §2.4). EO's clauses generate no new single-token operation; they transport availability only (B2 §2.1) [W].
- **Directed towers give at most one flow, and never an off-axis `J` [W].** Consider an infinite strictly increasing
  chain of finite subgroups of `SO(3)`. Its members are eventually cyclic or dihedral about one common axis `a`:
  - `T`, `O` and `I` have order at most 60;
  - a cyclic or dihedral group contains no polyhedral group;
  - so once a polyhedral group occurs in the chain, the chain stops growing past 60, which contradicts infinitude.

  So the closure of the union lies in `O(2)_a`. An element of order 3 in it, such as `J = cyc3`, is a rotation about
  `a` and commutes with the flow, so `J_off_axis` fails. Hence `ElementaryDrivability` (KInfFoundations.lean:264) is
  never the closure of a directed union of stage-preserving finite operations. **This confirms and sharpens F-D3**
  (drive/RESULT.md §3.2): there, one stage-preserving operation has finite order; here, even a directed family of them
  cannot produce an off-axis drive. The generator must cross stages.

## 2. The pair: the no-go for finite substrata

**Theorem B3.1 (fixed finite pair substratum).**

*Hypotheses.*
- `Λ` is finite, with a linear readout `R : ℝ^Λ → W 3` whose image spans `W 3`.
- `cnot` and a family of token operations in the pair context are realized as readout-respecting permutations of
  `Λ`, with induced maps `L_π`.

*Conclusions.*
- The group `Ĝ = ⟨L_π⟩` is finite, since `π ↦ L_π` is a homomorphism from a subgroup of `Sym(Λ)`.
- Suppose every `L_π` is a unitary or antiunitary conjugation. (A one-token reflection together with `cnot` is excluded
  for every candidate cone anyway, by `no_candidateCone_cnot_reflY`, K2Guard.lean:143.) Then claim D with its
  dimension corollary (Z/RESULT.md §1.0 [A]) gives a `Ĝ`-invariant self-dual cone `K ⊇ SEP`, `K ≠ Q3`, with H1–H3 at
  level (i).

*Consequence.* **(b) for every operation realized together with `cnot` on a fixed finite pair substratum, even when
granted, never forces `Q3`.*

*Proof.* Finiteness as stated. Claim D applies to any compact group of unitary and antiunitary conjugations fixing
`E00`, and the dimension corollary covers every finite group, because `R(Ĝ)` is a finite union of images of `S²×S²`
[A]. ∎

- **Native instance [X2].** The group generated on `W 3` by `cnot` and the local octahedral rotations (`S`, `cyc3` on
  each token) is finite, of order **11520**, the two-qubit Clifford group modulo phases. It is EXOTIC-E: C5 census,
  seed `d_low = 5/256` [A].
- **`R1` with `cnot` [X4].** The word `cnot · actC R1` has trace `10/9 ∉ ℤ`. A finite-order real matrix has an
  algebraic-integer trace, so this element has infinite order and `⟨cnot, actC R1⟩` is infinite. Control C1: the
  finite-order elements have integer traces. So `R1` and `cnot` are never realized together on a finite pair
  substratum, although each is H-sourceable on its own.

**Theorem B3.2 (directed towers of finite pair substrata) [W + L + X6].**

*Hypotheses.*
- Stage `n` is a finite pair substratum realizing `cnot` and a finite group `Ĝ_n` (Theorem B3.1).
- The system is directed: every operation realized at stage `n` is realized at every later stage with the same
  induced map, so `Ĝ_n ⊆ Ĝ_{n+1}`.
- The realized operations preserve the realized normalized states, a bounded set that affinely spans the slice
  (B1 §2). So `⋃ Ĝ_n` is bounded, and its closure `H` is a compact linear group.

*Conclusion.* The identity component `H₀` is abelian.

*Proof.*
1. Jordan's theorem [L] gives each `Ĝ_n` an abelian normal subgroup `A_n` of index at most `J(16)`.
2. Pass to a subsequence along which `A_n` converges in the Chabauty topology, in the compact space of closed
   subgroups. The limit `A` is an abelian closed subgroup of `H`.
3. Every `h ∈ H` is a limit of elements `g_{n,k} a_n` drawn from at most `J` cosets. Hence `H` is covered by finitely
   many cosets of `A`. So `A` is open in `H` and contains `H₀`. ∎

*Consequence.* Let `A_n` be the generator of the local circle about `n` on one token, and `B_n = cnot A_n cnot`.
- If `H ∋ cnot` and `H` contains an off-frame local circle `exp(t A_n)`, then `H₀` contains both one-parameter groups
  `exp(t A_n)` and `exp(t B_n)`. Exactly, `[A_n, B_n] ≠ 0` for `n = (3/5, 0, 4/5)` on either token [X6]. So `H₀` is
  nonabelian, which is impossible.
- Hence **no directed tower of finite pair substrata realizing `cnot` supplies any of the following:**
  - (b) for an off-frame local circle (stage 4 S3[n], UNIQUE [A]);
  - (b) for the drive together with an off-frame partner (A_miss), since `H₀` would contain circles about two
    different axes;
  - (b_R1) (X4).
- The frame-axis circles commute with their `cnot`-conjugates (`e_x`, `e_z` on either token [X6]). They are exactly
  the axes stage 4 records as EXOTIC-E [A].

### 2.1 Partial results toward Conjecture B3.C [W], added after the node's verdict (20:48Z)

**Setting.**
- `H` is a compact group of unitary and antiunitary conjugations of the pair, with `cnot ∈ H`.
- Its identity component is a torus, `H₀ = T`.
- `R(H) = H·P`, where `P` is the set of pure product states.
- By claim D [A], `H` is EXOTIC as soon as some pure state lies outside `R(H)`.

`T = H₀` is normal in `H`. Hence every `h ∈ H`, unitary or antiunitary, maps joint eigenlines of `T` to joint
eigenlines. For antiunitary `h`: if `tφ = λφ`, then `hφ` is an eigenvector of `h t h⁻¹ ∈ T`.

- **(P1) `dim T ≤ 1` ⇒ EXOTIC.** `R(H)` is a finite union of images of `T × P` under smooth maps, so its dimension is
  at most `1 + 4 < 6 = dim CP³`.
- **(P2) `T` has four distinct eigenlines forming a grid product basis ⇒ EXOTIC.** A grid product basis is, up to a
  local unitary, `{α⊗β, α⊗β⊥, α⊥⊗β, α⊥⊗β⊥}`.
  - A product state has coefficients `(ac, ad, bc, bd)` in such a basis. Its support therefore has size 1, 2 or 4,
    never 3.
  - `T` preserves supports, and every `h ∈ H` permutes the eigenlines, so it preserves support sizes.
  - Hence `R(H)` misses every state of support size 3, for instance `(φ₁ + φ₂ + φ₃)/√3`.

  This covers the following tori, with any finite extension normalizing them:
  - the full diagonal (monomial) torus, i.e. the continuous phase flows on both tokens together with the `ZZ` phase;
  - stage 4's S2 torus `actC R_z ∘ actT R_x` (EXOTIC-E [A], consistent);
  - every torus of commuting local frame-axis flows whose eigenbasis is a grid.
- **(P3) `T` has four distinct eigenlines, none of them a product state ⇒ EXOTIC.** Suppose `h·p = φ_k` with `h ∈ H`
  and `p ∈ P`. Then `p = h⁻¹φ_k` is an eigenline, hence not a product, which is a contradiction. So `φ_k ∉ R(H)`. This
  covers the Bell-diagonal 3-torus, the identity component of K(Z_F)'s own stabilizer (stage 4 Z [A]).

**The wall.** The remaining cases are:
- 2- and 3-dimensional tori whose eigenbasis is a non-grid product basis, such as `{|0β⟩, |0β⊥⟩, |1γ⟩, |1γ⊥⟩}` with
  `β ≠ γ, γ⊥`;
- eigenbases that contain some, but not only, product lines;
- 2-dimensional tori with a 2-dimensional eigenspace.

For these, `μ(P)` (the moment image in the simplex) is 3-dimensional. Whether the finitely many images `σ(μ(P))`,
`σ` in the normalizer's image, cover the simplex needs a case analysis constrained by `cnot ∈ N(T)`. That analysis is
not done here.

**What is left OPEN.** Whether every compact pair group containing `cnot` with abelian identity component leaves an
exotic invariant cone, beyond (P1)–(P3). This holds for finite groups (claim D [A]) and for the torus nodes recorded at stage 4 [A]. In
general it is open (Conjecture B3.C). With it, "no finite or locally finite H-level substratum ever forces `Q3`, even
granted every spectator principle at every stage" would be unconditional. Without it, the statement is proved for the
three sufficient contents listed above.

## 3. The reduction: the completion's flow, and A_miss as two rational matrices

- **Closure lemma [W].** For `K` closed and `gK ⊆ K` for every `g` in a group `G`, also `hK ⊆ K` for every
  `h ∈ cl(G)`: write `hω = lim g_n ω ∈ K`.
- **Infinite order [X5].** `R_z(θ)` with `cos θ = 3/5` has `tr = 11/5 ∉ ℤ`, so it has infinite order. Its powers are
  therefore dense in the circle [W: irrational rotation].
- **Hence (b) for one rational matrix equals (b) for its circle,** and
  **A_miss ⟺ (b) for the two rational matrices `R_z(θ)`, `R_x(θ)` on one token** [W + X5]. Each alone already moves
  K(Z_F) out: `−1/10`. The finite-order phase `S` moves it out with `−1/8` [X5].
- **What the completion contributes.** If the completion supplies a continuous flow on a token (F-D2: the closure of
  an infinite-order stage-crossing datum; K∞-Drive OPEN), then (b) for that flow is exactly A_miss. By the closure
  lemma, it equals (b) for one stage-crossing generator and one off-frame partner. **The continuum adds nothing to
  what is missing. The missing content is the composite action of single operations, which Theorems B3.1 and B3.2
  show no finite or locally finite H-level pair substratum can carry together with the native gate.**

## 4. Verdict of B3

- **FAILED route, exact obstruction (fixed finite substratum).** Realized pair groups are finite; exotic cones survive
  (b) for all of them, even when granted (B3.1 [W + A]; native order 11520 [X2]).
- **FAILED route, exact obstruction (directed towers).** Their closures have abelian identity component, which excludes
  every sufficient (b)-content that contains an off-frame circle or `R1` (B3.2 [W + L + X4, X6]).
- **Reduction recorded.** A_miss ⟺ (b) for `{R_z(θ), R_x(θ)}`, `cos θ = 3/5` [W + X5]. `(b_R1)` also suffices [A].
  K(Z_F) is excluded by each single operation [X5, X7].
- **Gem classification.**
  - **NEW**: the composite action that closes the gap is, structurally, an operation that generates a non-locally-
    finite group together with `cnot`. So it can come from no finite H-level substratum and from no directed tower of
    them, whatever spectator principle is granted. This propagates to every H→P route that sources (b) at finite
    stages: assumption-watch marker.
  - **ELABORATING**: F-D3 sharpened to directed families on one token.
- **Not claimed.** Conjecture B3.C. Anything about stage-crossing (non-permutation) operations, which are not hidden
  permutations of a finite set. Jordan's theorem is cited, not proved [L].
