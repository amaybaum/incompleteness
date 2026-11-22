# RECON-INF P2-C Node 1: the relations frozen against the corpus (reading)

**Goal link (§A.47).** Issue #1531 (RECON-INF Phase 1, whose audit records the Stage 1 → Stage 2
identification as open in both settings) and Issue #1535 (P2-C, cross-stage compatibility). This
node decides nothing for either: it fixes the statements, quantifiers and witnesses that Nodes 2–9
of the design use, so that their verdicts can be stated against a frozen object.

**Authorization.** Owner decision on #1169, comment 7074078687, executing the packet at #1535
comment 7074070661: Node 1 only, as the accepted design states it; reading and paper-only analysis.

**Pins.** Design: `verification/audits/foundations/recon-inf-p2c-20261121/DESIGN.md` at
`d1f39ce886c69c0d5bf3dd566f30c55285d0a4c6`, unchanged by this record. Corpus: `main` at
`df6da1c6101e811acdc7952d5748aff57028e8ed`. `Sub:n`, `Main:n`, `SM:n` are lines of
`papers/Substratum.md`, `papers/Main.md`, `papers/SM.md` at that commit; `NR-1:n` are lines of
`verification/audits/foundations/nr1-near-return-20261116/NR-1.md` at that commit; Lean paths are
relative to `verification/lean-mathlib/OIBridge/` at that commit. Design sections are cited as
"design §n".

**What was read.** Sub:121–173, Main:526–562, Main:614–650, SM:64–68, SM:220–244, Main:292–298 and
NR-1 §2 (NR-1:69–121), with the lines those passages cite where a statement below depends on them
(Sub:94, :98; Main:54, :736 items (viii) and (xiii); SM:106; `Equivalence.lean`:150–156, :422;
`SubstratumInterfaceAudit.lean`:87–102, :185–211; `WaveSubstratumUnbounded.lean`:45–58).

**Labels.** Established / Assumed / Missing, as the task requires; (N) native, (I) imported, as
design §0 defines them. A relation not yet proved carries no (N)/(I) label; its entry names what a
proof would import. Lemmas R and P below are paper derivations in this record and have not been
independently reviewed; their "Established" label is conditional on that review (Missing
obligation M1).

**Output class.** Definitions only. No computation was run; the only arithmetic is the hand counts
shown in §3 and the one coefficient in §5.4.

***

## 1. Common notation

These definitions instantiate design §2.3 and are used by every relation in §5.

- **Carrier.** `A = ℤ_q`, `q ≥ 2`. Setting (Z): `Λ = ℤ³`. Setting (F): `Λ = ℤ³/P_lat`, `P_lat` a
  finite-index sublattice with side at least 3 and the wrapping conditions each use states
  (Sub:98; SM:222). For a sublattice that is not cubic, "side at least 3" is read as: every nonzero
  vector of `P_lat` has ℓ¹-norm at least 3. Under this reading the sites `i ± e_j` are distinct from
  `i` and from one another, which the no-self-input reading and the return count of §5.4 use. `Ω = (A²)^Λ`, a site carrying the pair `(p, c)` (previous, current).
- **Dynamics.** `Φ_{q,α}(p, c) = (c, αSc − p)`, `S` the nearest-neighbour sum (Sub:159; SM:224;
  NR-1:75, which also displays `Φ^{-1}(u, v) = (v, αSv − u)` with `u` current, `v` previous).
  Main:296 is the instance `q = 2`, `α = 1`, with `(u, v) = (c, p)`.
- **Window phase group.** For a finite window `W ⊂ Λ`, `G_W = (A²)^W`, `|G_W| = q^{2|W|}`;
  `π_W : Ω → G_W` the restriction.
- **Readout map.** `r = g ∘ π_W : Ω → Y_r`, `Y_r = g(G_W)` its value set. Classes (R-coord),
  (R-lin), (R-nl) as in design §2.3.
- **Time map.** `m ≥ 1` lattice updates per visible step; `m ∈ {1, …, m_max}`, `m_max` fixed by the
  node's amendment before its run (design §2.3).
- **Readout-history law.** For a bijection `F` of `Ω`, time map `m`, readout `r` and initial law
  `λ` on `Ω`: `L(F, m, r, λ)` is the law under `λ` of `(r(F^{mk} ω))_{k=0}^{K}` on `Y_r^{K+1}`.
- **Target.** `P` a law on `C_V^{K+1}`, `C_V` finite and nonempty, horizon `K ≥ 1`, with time-0
  marginal `P_0`.
- **Matching (the alphabet and exactness conventions combined).** For an injective
  `ι : C_V → Y_r` and `e ∈ {(ex), (ε)}`:
  `Match_e(L, P, ι)` holds iff `L(ι(C_V)^{K+1}) = 1` and, writing `ι^{-1}_* L` for the law it
  induces on `C_V^{K+1}`, either `ι^{-1}_* L = P` (ex) or `TV(ι^{-1}_* L, P) ≤ ε` (ε).
  This reads design §2.3's two clauses together: the alphabet convention requires probability zero
  outside `ι(C_V)`, and (ex)/(ε) compare laws on `C_V^{K+1}`.
- **Splits.** Under (R-coord) with coordinate set `X_V`: `Ω = A^{X_V} × A^{X_H}`, `H_r := A^{X_H}`.
  Under (R-lin) with recorded complement `K'` of `ker h`: `Ω ≅ Y_r × H_r` through the isomorphism
  `Θ` of Lemma R, `H_r := ker h × (A²)^{Λ∖W}`.
- **Preparation classes** (design §2.3), stated as sets of laws on `Ω`:
  - (Π-H)(r): `Θ^{-1}_*(ι_* P_0 ⊗ β_H)` (`Θ` the identity under (R-coord)), `β_H` the marginal of
    `Θ_* β` on `H_r`; (Π-prod)(r): the same with `β_H` replaced by any law `ν` on `H_r`. Both are
    defined only for (R-coord) and (R-lin).
  - (Π-β): `β(· | E)`, `E` a cylinder event fixed by finitely many site–time values
    `(F^t ω)(z)` of the rule `F` under test, with `β(E) > 0`; for the time set of `E` see §6, point D1.
  - (Π-W): `λ_W ⊗ ν`, `λ_W` a law on `G_W` with `g_* λ_W = ι_* P_0`, `ν` any law on `(A²)^{Λ∖W}`;
    (Π-W,β): `ν` the marginal of `β` outside `W`.
  - (Π-joint): any law on `Ω` (Borel on the product topology in (Z)).
- **`β`.** On (Z), the uniform Bernoulli (Haar) law; on (F), the uniform (counting) law of `Ω`
  (design §2.2; Main:54, Lemma 3; NR-1:103).

***

## 2. Result (i): the readout classes of the corpus's lattice readouts

Scope: the passages read. No corpus-wide negative claim is made (§A.19); a readout outside these
passages is not classified here.

| Source | Readout as stated | Class | Reason |
|---|---|---|---|
| Main:294–298 | `q = 2`; "the visible sector being the sites of a region `R`", `s = dim V = 2|R|`; blocks `M_HV`, `M_VH` | (R-coord) with `W = R`, `X_V` all phase coordinates of `W`; hence also (R-lin) and (R-nl) | `s = 2|R|` counts both `u` and `v` at every site of `R`; the blocks `M_HV`, `M_VH` are blocks of the coordinate split |
| NR-1:81–83, :104 | `π(u, v) = (u, v)|_W ∈ V = (ℤ_q²)^W`, hidden `H = {x : πx = 0}`, `Ω = V × H`; NR-1:104 records it as the readout on `main` | (R-coord), `X_V` all phase coordinates of `W`; also (R-lin), (R-nl) | Coordinate projection with coordinate split; NR-1:84's rooted maps under (Haar) are (Π-H) with `P_0 = δ_a`, one time, `m = 1` |
| SM:242 (Theorem 1a) | A linear observer projection `P` on real observables of `S`, with `Q = I − P`, commuting with `U` and `R_g` | Not a member of any §2.3 class | §2.3's readouts are maps on configurations; Theorem 1a's `P` is a linear operator on the observable space, not required to be the projection onto functions of a readout map, and no law fixing an orthogonal projection is specified. Whether every such `P` corresponds to a readout map is not stated in the passages read (Missing obligation M6) |
| SM:68 | Normal-mode identification of the four-site ring over `ℤ/3` on `(ℤ/3)^8` | A normal-mode coordinate read alone is an (R-lin) readout of the spatial identification with `W` the whole ring | The adjacency matrix diagonalizes over `ℤ/3` (SM:68), so the change to normal-mode coordinates is a linear isomorphism of `𝔽_3^8`; a coordinate functional is a surjective homomorphism, and over a field its kernel has a complement |
| Sub:125, :137 | Stage 1: `S = C_V × C_H`, `V = C_V`, visible marginal | Not a lattice readout | Coordinate projection on a finite product without site structure (design §2.1). Sub:125 writes "`V ⊂ S` a distinguished subset" while Sub:137 makes `V = C_V` a factor of `S`; the readout is the projection `π_V` in both, so no class question arises |
| Main:292 | `|V| = |H| = 2`, `φ(x, h) = (h, x)` | Not a lattice readout | Finite coordinate example, J0-type |
| Sub:131, :171 | Bell protocol: `±1` outcome at each wing, finite readout regions | (R-nl) at least; finer class not determined | The outcome map is not specified; M1-B is outside Q (design §1) |

**Class nesting (by definition).** As sets of readout maps,
(R-coord) ⊂ (R-lin) ⊂ (R-nl): a projection onto a coordinate set `X_V` is a surjective
homomorphism whose kernel (the other window coordinates) has the coordinate complement, and every
homomorphism is a function. For an (R-coord) map, viewing it in (R-lin) with the coordinate
complement as `K'` gives the same split; another `K'` is a separate run (design §2.3). As sets of
laws, (Π-H) ⊂ (Π-prod) ⊂ (Π-joint), (Π-W,β) ⊂ (Π-W) ⊂ (Π-joint) and (Π-β) ⊂ (Π-joint). (Π-prod)
and (Π-W) coincide when `X_V` is all of `W`'s phase coordinates (then `g` is the identity of `G_W`
and `λ_W = ι_* P_0` is forced). Otherwise, for `P_0` not a point mass and `W ≠ Λ`, neither
contains the other. On (F) with `W = Λ` there are no coordinates outside `W`: (Π-prod) is then
`ι_* P_0 ⊗ ν` on the hidden window coordinates, which lies in (Π-W), and (Π-W) is every law on `Ω`
with readout marginal `ι_* P_0`, so (Π-prod) ⊂ (Π-W), strictly when `P_0` is not a point mass and
some window coordinate is hidden. For `P_0` a point mass, (Π-W) ⊂ (Π-prod), with equality when
`W = Λ` (the window law is then `δ_a` on the visible coordinates
times a law on the rest of the window, and its product with `ν` is a law on `H_r`; under (R-lin)
the same through `Θ`).

**Finding for (i).** Every lattice readout in the passages read that is used for the M1-T temporal
sector is of one kind: (R-coord) with `X_V` the full phase state of the window. No passage read uses
a proper coordinate subset (for example `c|_W` alone), a non-coordinate linear readout of the
spatial lattice, or a genuinely non-linear readout. SM:242's observer projection lies outside the
§2.3 classes. Status: Established (N), by reading.

***

## 3. Result (ii): which readout classes meet `|C_V|`

**Counts.** Let `w = |W|` and `n = |C_V|`. An injective `ι : C_V → Y_r` exists iff `|Y_r| ≥ n`.

| Class | Value count of one map `r` | Maximum over the class at `(q, W)` | Attained by |
|---|---|---|---|
| (R-coord), `|X_V| = k`, `1 ≤ k ≤ 2w` | `q^k` | `q^{2w}` | `X_V` all of `W` |
| (R-lin) | `|im h| = |K'|`, the order of a direct summand of `G_W` | `q^{2w}` | `h` the identity, `ker h = 0`, `K' = G_W` |
| (R-nl) | `|im g| ≤ |G_W| = q^{2w}`; every value `1, …, q^{2w}` occurs | `q^{2w}` | `g` injective |

**Counting rule, applied.** For a target `P` with `n = |C_V|`, at alphabet `q` and window `W`:
- a single readout map is excluded by counting iff its value count is below `n`;
- each class is excluded by counting iff `q^{2w} < n`. The threshold is the same for all three
  classes, since each contains a map with `q^{2w}` values; the classes differ only in which value
  counts below the maximum their maps take (powers `q^k` for (R-coord); orders of direct summands of
  `G_W` for (R-lin), powers of `q` when `q` is a prime power; every count for (R-nl)).
- The least window that no class is excluded on is the least `w` with `q^{2w} ≥ n`; for `n ≤ q²`
  it is a single site.
- Counting is a necessary condition for an injective labelling only. A map or class not excluded by
  counting is not thereby shown to realize the target: meeting the count says nothing about whether
  J2 or any other relation holds.

**Per target family.** The counting depends on a target only through `n = |C_V|`. It therefore
excludes individual targets, never a family as such: for (𝒫-rat), (𝒫-Q) and (𝒫-mem) alike, a target
with `n` outcomes is excluded at `(q, W)` exactly when `q^{2|W|} < n`, and a listed map exactly when
its count is below `n`. (𝒫-mem) needs `n ≥ 2`, since `M_t > 0` requires a non-constant visible
variable; `n = 1` targets are excluded by no class.

**Hand counts for the design's Node 4a families** (a qubit, `n = 2`, and a qutrit, `n = 3`,
observed in a fixed basis; design Node 4a, "Target families"). Observed projectively at every step,
with a fixed unitary `U` between readings, these laws are Markov: after a reading the state is a basis
vector, so `P(x_{k+1} = j | x_{≤k}) = |U_{ji}|²` whatever the past, and `M_t = 0` at every order.
They therefore lie in (𝒫-Q) and not in (𝒫-mem), and are not M1-T inputs of the kind Q concerns;
design Node 4a lists them beside the memory-bearing laws of the Main §3.4 probes. The table checks
only value counts against the listed readouts. It shows that no listed map is excluded by counting
except `c|_W` for the qutrit at `q = 2`; it shows nothing about realization:

| `q` | `w` | `c|_W` alone: `q^w` | Class maximum `q^{2w}` | Qubit (`n = 2`) | Qutrit (`n = 3`) |
|---|---|---|---|---|---|
| 2 | 1 | `2^1 = 2` | `2^2 = 4` | no class excluded (`4 ≥ 2`); `c|_W` not excluded (`2 ≥ 2`) | no class excluded (`4 ≥ 3`); `c|_W` excluded by counting (`2 < 3`) |
| 2 | 2 | `2^2 = 4` | `2^4 = 16` | none excluded | none excluded (`4 ≥ 3`, `16 ≥ 3`) |
| 3 | 1 | `3^1 = 3` | `3^2 = 9` | none excluded | none excluded (`3 ≥ 3`, `9 ≥ 3`) |

The corpus instance Main:294–298 (`q = 2`, full window readout) has `2^{2|R|}` values: 4 at
`|R| = 1`, so neither family is excluded by counting there. At `q = 2` no (R-coord) or (R-lin) map has exactly 3 values
(its counts are powers of 2), so a qutrit target under these classes always leaves readout values
outside `ι(C_V)`, which the realized law must avoid at every time `0, …, K`; that is a constraint
for Nodes 4–5, not an exclusion by counting.

**Composite `q`.** For `q = 4`, the map `ℤ_4 → ℤ_4/2ℤ_4` on one coordinate has kernel `2ℤ_4`,
which has no complement in `ℤ_4` (design §2.3); it is therefore not admitted to (R-lin) and is
counted in (R-nl), with 2 values.

Status of (ii): Established (N), by counting.

***

## 4. Result (iii): the two authorized witnesses

The design's Node 1 text names "§2.5 rows 3 and 4 (the (R-lin) relabelling and the (R-nl) padding
argument)". In the design's §2.5 table the relabelling is the witness the third and fourth rows
name, and the padding argument is the sixth row's. Both are supplied below, and every row of
design §2.5 is then given a witness or "Missing" in §4.3.

### 4.1 Lemma R (the (R-lin) relabelling)

*Statement.* Let `h : G_W → Y` be a surjective group homomorphism and `K'` a subgroup with
`G_W = ker h ⊕ K'`. Put `s = (h|_{K'})^{-1} : Y → K'` and
`θ(g) = (h(g), g − s(h(g)))`. Then `θ : G_W → Y × ker h` is a group isomorphism with
`pr_Y ∘ θ = h`, and `Θ = θ × id : Ω → Y × (ker h × (A²)^{Λ∖W})` is a group isomorphism (in (Z), a
homeomorphism of the product topology) with `pr_Y ∘ Θ = h ∘ π_W`. For every `m`,
`Θ Φ_{q,α}^m Θ^{-1}` is a bijection, conjugate to `Φ_{q,α}^m` with the readout carried to `pr_Y`.

*Proof.* `h|_{K'}` is injective because `K' ∩ ker h = 0`, and surjective because
`h(G_W) = h(ker h + K') = h(K')`; so `s` is a homomorphism. `h(g − s(h(g))) = h(g) − h(g) = 0`, so
`θ` lands in `Y × ker h`, and it is a homomorphism as a composite of homomorphisms. The map
`(y, k) ↦ s(y) + k` inverts it: `θ(s(y) + k) = (y, s(y) + k − s(y)) = (y, k)`, and
`s(h(g)) + (g − s(h(g))) = g`. `pr_Y ∘ θ = h` by construction. `Θ` acts coordinatewise as `θ` on the
window and as the identity outside, so it is an isomorphism, continuous with continuous inverse in
(Z) because it changes finitely many coordinates. Conjugating the bijection `Φ^m` by a bijection
gives a bijection. `□`

*Use.* Under (R-lin) with the recorded `K'`, `Θ` makes the (R-lin) split a product split
`Y × H_r` with the readout as the projection onto the first factor. When `Y ≅ A^j` (always when
`q` is prime, `G_W` then being an `𝔽_q`-vector space), a basis choice makes `pr_Y` a projection onto
`j` coordinates. On (F), `Θ` maps the counting law of `Ω` to the counting law of `Y × H_r`, so the
(R-lin) marginal `β_H` is uniform on `H_r`.

Standing: Established (N), elementary group theory, subject to review (M1).

### 4.2 Lemma P (the (R-nl) padding argument)

*Statement.* Let `Ω_F` be finite, `Ψ` a bijection of `Ω_F`, `r : Ω_F → Y` any map,
`ι : C_V → Y` injective, and `λ` a law on `Ω_F` with `r(Ψ^k ω) ∈ ι(C_V)` for all `0 ≤ k ≤ K`,
`λ`-almost surely. Let `P'` be the law under `λ` of `(ι^{-1} r(Ψ^k ω))_{k=0}^{K}`.

(a) There exist a finite `C_H`, a bijection `ψ` of `C_V × C_H` and an injective
`b : Ω_F → C_V × C_H` with `ψ ∘ b = b ∘ Ψ` and `π_V(b(ω)) = ι^{-1}(r(ω))` whenever
`r(ω) ∈ ι(C_V)`. Under the initial law `b_* λ`, the visible trajectory of `ψ` through `K` has law
`P'`, and every state reachable from the support of `b_* λ` lies in `b(Ω_F)`.

(b) If moreover `Ω_F = Y × H` with `r = pr_Y` and `λ = ι_* P_0 ⊗ ν`, then `b` can be chosen with
`b(ι(x), h) = (x, j(h))` for one injective `j : H → C_H`, and then `b_* λ = P_0 ⊗ j_* ν`: the
hidden prior is independent of the visible initial state. The product form is that of the posited
preparation class (Π-H) or (Π-prod), carried through the bijection `b`: it is inherited from the
hypothesis on `λ`, not produced by the dynamics, and it is not a physically sourced preparation
(Main:648).

*Proof.* (a) Choose `κ : Y → C_V` with `κ ∘ ι = id` (arbitrary on `Y ∖ ι(C_V)`). The fibres
`G_x = (κ ∘ r)^{-1}(x)`, `x ∈ C_V`, partition `Ω_F`; let `a_x = |G_x|` and `c = max_x a_x`, and put
`C_H = {1, …, c}`. Adjoin pairwise disjoint sets `I_x` of `c − a_x` new (inert) states, put
`Ω' = Ω_F ⊔ ⊔_x I_x`, and let `Ψ'` act as `Ψ` on `Ω_F` and as the identity on each `I_x`; `Ψ'` is a
bijection of `Ω'`. Each `G_x ⊔ I_x` has `c` elements, so choose bijections
`b_x : G_x ⊔ I_x → {x} × C_H`; their union `b' : Ω' → C_V × C_H` is a bijection, because the sets
`G_x ⊔ I_x` partition `Ω'` and the sets `{x} × C_H` partition `C_V × C_H`. Set
`ψ = b' Ψ' b'^{-1}` and `b = b'|_{Ω_F}`. Then `ψ` is a bijection, `ψ ∘ b = b ∘ Ψ`, and
`π_V(b(ω)) = κ(r(ω))`. For `λ`-almost every `ω` and `k ≤ K`,
`π_V ψ^k b(ω) = π_V b(Ψ^k ω) = κ(r(Ψ^k ω)) = ι^{-1}(r(Ψ^k ω))`, so the visible trajectory has law
`P'`. `Ψ` preserves `Ω_F`, so `ψ` preserves `b(Ω_F)`, which contains the support of `b_* λ`.
(b) Here `G_x ⊇ {ι(x)} × H` for every `x`, so `c ≥ |H|`; fix an injection `j : H → C_H`. The map
`(ι(x), h) ↦ (x, j(h))` is injective from `{ι(x)} × H` into `{x} × C_H`; a partial injection
between finite sets of equal size `c` extends to a bijection (the counting step of Main:530,
`exists_perm_extending` in `Equivalence.lean`:60, composed with a fixed bijection
`G_x ⊔ I_x → {x} × C_H`), so `b_x` can be chosen extending it. Then
`b_*(ι_* P_0 ⊗ ν)(x, j(h)) = P_0(x) ν(h)`, which is `P_0 ⊗ j_* ν`. `□`

*Consequences used below.* Under (ex), `P' = P`; under (ε), `TV(P', P) ≤ ε`, and the realization is
of `P'`. When every fibre `G_x` already has `c` elements (for example (R-coord) or, through Lemma R,
(R-lin) with `ι` onto `Y`), no inert state is adjoined and `b` is a bijection `Ω_F → C_V × C_H`.

Standing: Established (N), finite combinatorics, subject to review (M1). The padding argument does
not fail, so the decision rule's fallback (the (R-nl) row Missing, (R-nl) verdicts compared with
J0-joint only) is not triggered. Lemma P delivers J0-joint, and J0-ind only in case (b); an (R-nl)
readout with a general preparation is compared with J0-joint.

### 4.3 The implications of design §2.5, row by row

Under (ex) the J1 ⇒ J0 rows below give J0 for `P`. Under (ε) they give J0 for the realized law
`P' = ι^{-1}_* L`, with `TV(P', P) ≤ ε`, not for `P` (§4.2, consequences); since J0 holds for every
finite-horizon law (Main:528; `S_imp_D`), this costs nothing for J0 itself.

| Design §2.5 row | Witness after Node 1 | Standing |
|---|---|---|
| J3 ⇒ J2 ⇒ J1 ⇒ J1⁰ | Class inclusion (§2 nesting; §5 statements) with the same readout and preparation class on both sides. `Φ_{q,α}` satisfies A2 (SM:106; `waveSubstratum_A2`, `SubstratumInterfaceAudit.lean`:190), A3 with degree `2d` (`waveSubstratum_A3`:194), A4's translation clause exactly (`waveSubstratum_A4Exact`:202; `waveZ_A4Exact`:51 in (Z)); these Lean anchors are stated on `Fin d → ZMod L`, that is on cubic tori `P_lat = Lℤ^d` and on `ℤ^d` at `L = 0`, and for a non-cubic `P_lat` the A2–A4 checks rest on SM:106 and the form; and A4's no-self-input clause by its form, the new current at `i` being `αSc(i) − p(i)` with `S` excluding `i` (SM:228; Sub:98; on (F), the ℓ¹ reading of side at least 3 in §1). The Lean predicate `A4Exact` (`SubstratumInterfaceAudit.lean`:94) is the translation clause only; the no-self-input clause rests on the form, not on a kernel theorem. The inclusion J2 ⇒ J1 holds with J1's time-map quantifier as stated in §5.4 | Established (N), by definition, for the quantifier form of §5.4 |
| J1 on (F), (R-coord), (Π-H) or (Π-prod) ⇒ J0-ind | The coordinate split when `ι` is onto `Y_r`; Lemma P(b) when it is not (values outside `ι(C_V)` assigned by `κ`) | Established (N): by definition for `ι` onto, Lemma P(b) otherwise; for `P` under (ex), for `P'` under (ε) |
| J1 on (F), (R-lin), (Π-H) or (Π-prod) ⇒ J0-ind | Lemma R, then the previous row (Lemma P(b) when `ι` is not onto) | Established (N), Lemmas R and P(b); for `P` under (ex), for `P'` under (ε) |
| J1 on (F), (R-lin), (Π-W), (Π-β) or (Π-joint) ⇒ J0-joint | Lemma R, then the next row; or directly Lemma P(a), since (R-lin) ⊂ (R-nl) | Established (N), Lemma R or Lemma P(a); for `P` under (ex), for `P'` under (ε) |
| J1 on (F), (R-coord), (Π-W), (Π-β) or (Π-joint) ⇒ J0-joint | The coordinate split when `ι` is onto; Lemma P(a) otherwise | Established (N); for `P` under (ex), for `P'` under (ε) |
| J1 on (F), (R-nl), any preparation class ⇒ J0-joint | Lemma P(a) with `Ψ = F^m` | Established (N), Lemma P(a); for `P` under (ex), for `P'` under (ε) |
| J2 on (Z) ⇒ J2 on (F), side above the Node 3 bound | Light-cone agreement for multi-time laws (Node 3); NR-1 Prop. 4.1 covers rooted maps under the uniform prior only | Missing (Node 3) |
| J2 on (F), side above the bound ⇒ J2 on (Z) | Lift of the torus preparation (Node 3) | Missing (Node 3) |
| J4-fac ⇒ J2-type law equality | Pushforward under the factor map (Node 6); the law on `S` must be named (§5.7) | Missing (Node 6) |
| J4-emb ⇒ J2 with a preparation supported on the invariant subset | With J4-emb stated as in §5.8: the preparation `b'^{-1}_* μ_R`, supported on `Ω'`, gives readout law `P`; it lies in (Π-joint) | Established (N), by definition |
| J2 on (F), (R-coord) ⇒ J5(T) | Main:632, universality clause, applied to the realization of the J0 rows (`ι` onto; otherwise to the realization `ψ` on `C_V × C_H` of Lemma P(a)); `T(P)` under (ex), `T(P')` under (ε). The (R-lin)/(R-nl) form on the torus states is Node 7a's (§5.9) | Established (N) on (F) with (R-coord), paper-proof layer with exhaustive small-size certification, not kernel-checked; no identification content |
| J2 ⇒ J5(R₁) | None known | Not asserted |
| J0 ⇒ J2 | None known; Node 4 | Not asserted |
| J5(T) ⇒ J4, J5(R₁) ⇒ J4 | None known | Not asserted |

The rows J1 ⇒ J0 carry little content on their own, because J0-ind holds for every finite-horizon
law (Main:528). What they add is that the lattice realization itself, conjugated by the splits or
by Lemma P, is a J0 realization; J5(T) (§5.9) and J4-emb (§5.8) use exactly that.

The design's existing equivalences keep their directional witnesses at the pin:
`S ⇔ D ⇔ Q_fb` (Main:556–562; `Qfb_imp_S` at `Equivalence.lean`:245, `D_imp_Qfb`:294, `S_imp_D`:422,
`finite_horizon_equivalence`:462) and the all-time rooted classification (Main:650). No new
equivalence is displayed here (§A.34).

***

## 5. The relations, with explicit quantifiers

Every relation below is read for a target `P` on `C_V^{K+1}`, a setting `s ∈ {(F), (Z)}` (with
`P_lat` admissible on (F)), and an exactness `e`. A **domain** `𝔇` is the tuple of ranges a node
fixes before its run: a set `𝒬` of pairs `(q, α)`, `m_max`, a readout class with a finite list `𝓜`
of readout maps (design §2.3), a preparation class, and the torus conditions. The core predicate is

`Real(F, m, r, λ; P, ι, e) :⇔ Match_e(L(F, m, r, λ), P, ι)`.

A positive verdict is an instance of the existential; a negative verdict over `𝔇` is the
universal negation `∀ (q, α) ∈ 𝒬 ∀ m ≤ m_max ∀ r ∈ 𝓜 ∀ ι ∀ λ ∈ class(r) : ¬Real(…)`, and holds only
over the listed maps (design §2.3).

### 5.1 J0-ind

`∃ finite C_H ∃ bijection φ of C_V × C_H ∃ law μ_H on C_H` such that the law of
`(π_V φ^k(X_0, H_0))_{k=0}^{K}` under `P_0 ⊗ μ_H` equals `P`. No `(q, α)`, `m` or lattice readout
enters; the readout is `π_V`.

Status: Established (N) for every finite-horizon law: Main:526 (rational kernels, uniform tape) and
Main:528 (arbitrary kernels, response-table form, product prior independent of `X_0`). Layer: paper
derivation with exact probe certification; the independence of `μ_H` from the visible initial state
is not formalized in the kernel (Main:530). The physical origin of `P` is E1 (I) (Sub:123); the
relation itself uses no import.

### 5.2 J0-joint

`∃ finite C_H ∃ bijection φ of C_V × C_H ∃ law μ on C_V × C_H` (its `C_V`-marginal `P_0`, the
coordinates possibly correlated) such that the law of `(π_V φ^k(X_0, H_0))_{k=0}^{K}` under `μ`
equals `P`.

Status: Established (N); kernel-checked, `S_imp_D` (`Equivalence.lean`:422), class (D) as
`Equivalence.lean`:150–156 defines it. J0-ind ⇒ J0-joint trivially. These are the faithful
realizations of Main:614.

### 5.3 J1⁰

`∃ d ≥ 1`, a site set `Λ` (`ℤ^d`, or `ℤ^d/P_lat`), a finite site alphabet `B`, a bijection `F` of
`B^Λ` of finite range (each output coordinate a function of the input coordinates within graph
distance `r_F` of its site), `∃ m ≤ m_max`, `∃` a readout map `r = g ∘ π_W` in the stated readout
class, `∃ ι`, `∃ λ` in the stated preparation class: `Real(F, m, r, λ; P, ι, e)`.

Reading notes. (a) Translation invariance is not required, so the single-active-site form that
design §2.4 cites for J5(T) is a member; its translation-invariant variant (the same bijection at
every site) is also a member. (b) Finite range bounds each site's coupling degree, so "no constraint
from A3–A6" is read as no constraint beyond finite range. (c) (R-coord) and (R-lin) need
coordinates and a group structure on `B`; (R-nl) is always defined. (d) Whether `F^{-1}` must also
have finite range is not fixed by the design; every rule J2 uses has a finite-range inverse
(NR-1:75), so the inclusions of §4.3 hold under either reading; Node 2's vacuity test may turn on
it (§6, D5).

Status: Missing as a stated result; Node 2 tests whether it is vacuous. Imports a proof would need:
none beyond A2.

### 5.4 J1

As J1⁰, with `F` further required to satisfy A2 (bijective), A3 (bounded degree), and both senses of
A4 (Sub:98): commuting with translations of `Λ` up to a site-wise gauge, and no self-input. The
no-self-input clause is defined in the corpus for rules with a designated present value; the
second-order form `x(t+1) = F(x(t)) − x(t−1)` over a finite abelian group per site (Main:736 item
(xiii); Sub:98) is that case, read as: each `F_i` does not depend on `x_i(t)` (SM:228). For other
rule forms the clause is a definitional choice the design does not make (§6, D3). The readout and
preparation classes and `m` are quantified as in J1⁰.

**Time-map quantifier.** J1 quantifies `∃ F ∃ m`, with A2–A4 required of the one-step rule `F`, not
of `F^m`. With this form, J2 ⇒ J1 is class inclusion for every `m`. The other reading, in which
`F^m` must itself satisfy A4's no-self-input clause, does not contain J2 in general, under the
reading of D3 that the new current value at `i` must not depend on `c(i)`: `Φ^2` is not
of the second-order form in the phase coordinates `(p, c)`, and its current component is
`Φ^2(p, c)_c = α² S²c − αSp − c`, in which `c(i)` occurs with coefficient `2dα² − 1` (`S²c(i)` has
`2d` back-and-forth terms returning to `i` on `ℤ^d`, and on a torus under the ℓ¹ reading of §1). That
coefficient is nonzero unless `2dα² ≡ 1 (mod q)`; for `d = 3`, `q = 5`, `α = 1` it is
`6 − 1 = 5 ≡ 0`.

Status: Missing. Imports: A2–A4, (viii) site factorization (Main:736).

### 5.5 J2 (this is Q)

`∃ (q, α) ∈ 𝒬 ∃ m ∈ {1, …, m_max} ∃ r ∈ 𝓜 ∃ ι : C_V ↪ Y_r ∃ λ ∈ class(r)` (on (F), also for the
stated `P_lat`): `Real(Φ_{q,α}, m, r, λ; P, ι, e)`. The pointwise relation `J2_{q,α,m,r}` fixes the
first three quantifiers; node verdicts are recorded pointwise ("for that `(q, α)`, `m`, window and
readout map", design Node 4a). `q` and `α` are not fixed on `main` (NR-1:101; SM:230), so `𝒬` is a
node choice, written into the amendment before the run.

Status: Missing. Imports: A2–A6, the nearest-neighbour premise, (xiii) and (viii) (Main:736;
Sub:159; SM:224).

### 5.6 J3 (this is Q⁺, the design's stronger reading)

J2 with `class(r)` restricted to (Π-β), (Π-H) or (Π-W,β), and `β` as in §1.

Status: Missing. Imports: as J2, plus H-μ(φ,Θ) (design §1) and the choice of `β`, which the corpus
does not make; `β` is Assumed (named) here, not selected. Q⁺ is not the owner's question and is
reported separately (design §1).

### 5.7 J4-fac

`∃ (q, α) ∃ m`, a realization `R = (C_V × C_H, φ_R, μ_R)` of `P` (which `R`: §6, D4), and a map
`π : Ω → C_V × C_H` such that either (measure-theoretic) `π` is measurable with
`π ∘ Φ^m = φ_R ∘ π` `β`-almost everywhere, or (topological) `π` is continuous and surjective with
`π ∘ Φ^m = φ_R ∘ π` everywhere; and the readout factors through it, `π_V ∘ π = ι^{-1} ∘ r` on the
relevant set, for some `r` and `ι`.

Quantifier remark. The law on `C_V × C_H` that a measure-theoretic factor carries is `π_* β`, and
`φ_{R*}(π_* β) = π_*(Φ^m_* β) = π_* β`: it is `φ_R`-invariant (`β` is `Φ`-invariant: on (F) because
`Φ` is a bijection and `β` is the counting law; on (Z) because `Φ` is a continuous automorphism of a
compact group, NR-1:77, :103). J4-fac therefore relates `Ω` to
`(C_V × C_H, φ_R)` with an invariant law; Stage 1's initial law `P_0 ⊗ μ_H` enters the row
"J4-fac ⇒ J2-type law equality" only where it is that law or is obtained from it by a stated
further step. Node 6 must name which (M3).

Status: Missing. Imports: as J3.

### 5.8 J4-emb

For a realization `R = (C_V × C_H, φ_R, μ_R)` of `P`, "realization" meaning Main:614's faithful
realization (the initial law `μ_R` on `C_V × C_H` may correlate the coordinates): `∃ (q, α) ∃ m`, a finite `Φ^m`-invariant set
`Ω' ⊂ Ω`, and a bijection `b' : Ω' → C_V × C_H` with `b' ∘ Φ^m|_{Ω'} = φ_R ∘ b'` and
`π_V ∘ b' = ι^{-1} ∘ r` on `Ω'`, for some readout `r` and injective `ι`. Two quantifier forms:
`J4-emb[R]` for a fixed `R`, and `J4-emb∃ := ∃ R J4-emb[R]`.

Quantifier remark. On (F), J2 for a readout whose fibres `(κ ∘ r)^{-1}(x)` all have the same size
(for example (R-coord), or (R-lin) through Lemma R, with `ι` onto) gives `J4-emb∃` with no further
argument: Lemma P adjoins no inert state, `b` is a bijection `Ω_F → C_V × C_H`, and
`R = (C_V × C_H, b Φ^m b^{-1}, b_* λ)` satisfies `J4-emb[R]` with `Ω' = Ω_F`. Under (ex) `R` realizes
`P`; under (ε) it realizes `P'`, so the implication is J2(ε) ⇒ `J4-emb∃` for `P'`, not for `P`. With
the joint initial law allowed this holds for every preparation class. With a product initial law
required (the J0-ind form, which Stage 1's `R₁` has, Main:526), it holds for (Π-H) and (Π-prod) only,
through Lemma P(b), because otherwise `b_* λ` is not a product. Under (ex), `J4-emb∃` therefore
adds nothing to J2 on (F) for such readouts. Identification content can only come from
`J4-emb[R₁]`, with `R₁` the dilation Stage 1 actually uses (§6, D4).

Status: `J4-emb[R₁]` Missing as a stated identification; `J4-emb∃` on (F) for equal-fibre readouts is
implied by J2 there, for `P` under (ex) and for `P'` under (ε), with the preparation classes stated
above for each initial-law form (Established (N), Lemma P). Imports: as J2.

### 5.9 J5(T)

`∀` faithful realizations `R` of `P` on `C_V × C_H` at horizon `K` (Main:614's definition: joint
initial law allowed): `∃!` morphism of realizations `q_R : R → T(P)` on the prior-supported
reachable part, a morphism being stage-preserving, visible-preserving (`π_V ∘ q = π_V`) and
dynamics-intertwining (`q ∘ φ_R = σ ∘ q`) (Main:632).

Scope. On (F) with (R-coord) and `ι` onto `Y_r`, the realization of §4.3 is such an `R`; with `ι`
not onto, Main:632 applies to the realization `ψ` on `C_V × C_H` of Lemma P(a). Under (ex) the
quotient is `T(P)`; under (ε) the realization is of `P'` and the quotient is `T(P')`. The form on
the torus states for (R-lin) and (R-nl) readouts, and for (R-coord) with `ι` not onto, needs the morphism notion restated with `κ ∘ r` in
place of `π_V`, and is Node 7a's question; composing Lemma P(a) with Main:632 is a route Node 7a may
examine, not established here (M5). On (Z) the statement needs Node 7a's extension.

Status: Established (N) on (F) with (R-coord), at the paper-proof layer with exhaustive exact
certification at small sizes (Main:632); not kernel-checked. It holds for every faithful realization,
J0's dilation and Node 2's range-0 witness included, so it carries no identification content and is
not a criterion for Q or Q⁺ (design §2.4, I12). (R-lin) and (R-nl), and (R-coord) with `ι` not onto, on the
torus states, and (Z): Missing (Node 7a).

### 5.10 J5(R₁)

For a J2 realization (finite form, on (F) or through Node 3) with initial law `λ`, and Stage 1's
dilation `R₁ = (C_V × C_H, φ₁, μ₁)`: `∃` a map `q` from the realization's prior-supported reachable
part onto `R₁`'s that is stage-preserving, visible-preserving (`π_V ∘ q = ι^{-1} ∘ r`) and
intertwining (`q ∘ Φ^m = φ₁ ∘ q`), with or without the clause `q_* λ = μ₁` (§6, D2).

Status: Missing; not implied by Main:632, whose fibres above `T(P)` are not unique
(`fiber_freedom`, Main:632). Imports: Main:632's morphism notion.

***

## 6. Definitional points the design leaves open

Each is recorded with the literal reading used above; none is decided here. Each is routed to the
node that first needs it, or to the owner under design S2 if a verdict turns on it.

- **D1. Time set of the (Π-β) event `E`.** Design §2.3 says "a finite set of sites and times"; design
  Node 3 takes backward cones "back to time 0", which presupposes times at or after 0. The class is
  read with time set `T_E ⊂ {0, 1, 2, …}` finite. If `T_E` meets `(0, mK]`, the preparation
  conditions on the lattice state at times inside the readout horizon; the design does not exclude
  this. First needed by Node 3.
- **D2. Prior clause in J5(R₁).** Design Node 7b requires a visible-preserving, intertwining map onto
  `R₁`'s prior-supported reachable part; it does not say whether the map must carry the realization's
  initial law to `μ₁`. Both forms are stated in §5.10. First needed by Node 7b.
- **D3. No-self-input outside the second-order form.** §5.4. First needed by Node 2, case (b), whose
  example is of second-order form, so the case may not arise.
- **D4. Which dilation is `R₁`.** Stage 1's dilation is fixed by the construction of Main:526–530
  only up to choices: the denominator `D` and the quantile assignment `Q` in the tape form, the
  response-table form of Main:528 as an alternative, and the completion of the bijection off the
  well-formed states (Main:530, "assigned by this completion"). A relation on the prior-supported
  reachable part through `K` (J5(R₁)) does not see the completion; a relation on all of `S`
  (`J4-emb[R₁]`, the restriction being all of `(S, φ)`) does. Which choices `R₁` fixes must be stated
  before Nodes 6–7 run.
- **D5. Finite range of `F^{-1}` in J1⁰.** §5.3, reading note (d): the design does not fix whether
  `F^{-1}` must have finite range. The inclusions of §4.3 hold either way. First needed by Node 2,
  whose vacuity test may turn on it.

***

## 7. Missing obligations

- **M1.** Independent review of Lemma R (§4.1) and Lemma P (§4.2), the two paper derivations this
  record adds. Until reviewed, the rows of §4.3 that rest on them are Established subject to that
  review.
- **M2.** Node 3: both directions of the (Z) ↔ (F) light-cone transfer for multi-time laws and each
  preparation class (design §2.5, rows 7–8). Missing.
- **M3.** Node 6: the witness of "J4-fac ⇒ J2-type law equality", including which law on `S` it uses
  (§5.7). Missing.
- **M4.** The truth of J1⁰, J1, J2, J3, J4-fac, `J4-emb[R₁]` and J5(R₁): statements frozen here,
  decisions Missing (Nodes 2, 4, 5, 6, 7b).
- **M5.** Node 7a: J5(T) on (Z), with the "almost every" restatement for a non-atomic law, and the
  form on the torus states for (R-lin) and (R-nl) readouts, and for (R-coord) with `ι` not onto
  (§5.9). Missing.
- **M6.** The relation between SM:242's linear observer projections and the §2.3 readout classes is
  not stated in the passages read. No row of design §2.5 needs it. Missing (recorded, not pursued).
- **M7.** J0-ind is not formalized in the kernel (Main:530); its support is the paper derivation of
  Main:526–528 with probe certification. Recorded as the existing layer, not a P2-C obligation.
- **M8.** D1–D5 of §6: definitional choices to be fixed before the nodes that use them run.

Nothing in Node 1 required a computation, so no step is recorded as "Missing (needs computation)".
No step required a proof beyond Lemmas R and P; the one coefficient in §5.4 is hand arithmetic
supporting a quantifier choice, not a further result.

***

## 8. Checks on this record

| Design invariant | Check |
|---|---|
| I1, I2 | The commit adds this file only; `DESIGN.md` is unchanged; no code or data file is added |
| I3 | Every `file:line` above was read at `df6da1c6` |
| I10 | The added lines were searched for the excluded vocabulary and for local paths, with no hit |
| I11 | No equivalence is displayed; §4.3 lists each implication one direction at a time |
| I14 | J2 (§5.5) and J3 (§5.6) are stated separately |

***

## 9. No verdict on Q

This record makes no verdict on Q (J2) or on Q⁺ (J3), and none on any relation of §5 other than
J0-ind, J0-joint and J5(T), whose standing is taken from the corpus as cited. It does not freeze
Node 2's reference rule set or its per-rule readout and preparation lists, does not open Nodes 2–9,
and does not run the literature search of design §3.
