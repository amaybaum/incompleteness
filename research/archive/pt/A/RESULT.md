# Thread A — PAIR-COMP (composite completion): RESULT

Research only. Base: certified `main` at L = `9f9f8257a980a1819fbbc1dc0019917cf8678626` (`pt/base/`, read-only).
Governing texts: `pt/PROTOCOL.md` (sha256 `239dc123…fa9b23`), amendment 1 (`b41aa0e7…31cf83`), amendment 2
(`2a2f78f3…c530a`). Nothing here is adopted, frozen or governed; no git write, PR, CI or agent was used. Lean text in
`lean/` is UNBUILT (no toolchain) and is not a kernel proof.

Evidence levels, kept separate: **[K]** kernel identifier certified at L (file:line in `pt/base/`); **[D]** kernel-checked
in the design run at `ff9c3a35` (`pt/inputs/fourcopy/`), not certified; **[W]** written argument (given here);
**[X]** exact computation in this directory, stated for the instance it checks; **landed X** = an exact check of the
certified round KT4-PREM-1 (`kt4_prem1_probe.py`, by check id); **[L]** literature not read at the source.

Notation. `SEP` = convex cone of the product states `prodState x y`, `x, y ∈ eball 3`. `K_gen = SEP + cnot SEP`.
`K_E = dualW(K_gen)`. `K_cl = int Q3 ∪ (SEP + cnot SEP)` (the landed closedness foil `M_cl`). `T_ψ = actT R_H phiW`
(landed M_cl.6). `F = E00/2 − T_ψ/4`. A *pair system* is a `DirectedStages` whose labels include product labels `e ⊗ f`
of one-ball effects; its *read-out* `T : CSpace D → W 3` reads the table from 16 product labels whose homogenized
coefficient vectors span (`a1` A1.10); `T` is continuous (finitely many coordinates). **ID**: "the theorem's `K_p` is the
cone over `T(body D)` for a pair system `D` whose completed body has finite rank".

## 0. Answer

**(A-i) completion — DERIVED.** The narrow stage-level product of two one-ball directed systems (product preparations,
product labels, multiplicative table), and its closure under `cnot`, are directed systems of finite stages whose completed
bodies are closed in ℓ^∞ (`body_isClosed` [K], true of every directed system) and — because every label is a product
label, so the completion is locally tomographic by construction (a named use of K2's content) — have finite rank and read
out into `W 3` as compact sets: with factor preparations dense in the ball, the normalized slices of `SEP` and of
`K_gen` ([W]; [X] on the finite instance; UNBUILT Lean).
**(A-ii) correspondence, and with it `hcl` for the theorem's `K_p` — INDEPENDENT of the premises certified at L as stated
(and of `hcls ∧ hadm ∧ hgate ∧ H`):** the landed foil `M_cl` satisfies every certified premise bearing on it (§0.1) and
its cone `K_cl` is the `W 3` read-out of the completed body of a finite-stage pair system with stage consistency and
bi-affine product tables (`D_cl`, infinite rank; [X] skeleton + [W]); `hcl` is not claimed. What closes the gap is finite
rank of the pair completion together with ID (sufficiency proved), and ID is equivalent to `hcl` relative to `hadm` (both
directions proved), so it is recorded as a restatement, not a source; instance `d = 3`, gate `cnot`, identity locals,
one cone at every pair.

- **Sufficiency proved:** (A-i) as stated [K + W]. `FiniteRank ∧ ID ⇒ hcl` [K + W], and `hcl ∧ hadm ⇒ ID` [W; X on
  instances]: ID, and likewise P-STAGE2, is `hcl` restated. Closure form `hcls ∧ hadm ∧ hgate ∧ H ⇒ IE1(cl K_p) ∧
  EvenCycle` [D + W, not kernel-checked]: `hcl` only transfers IE1 from `cl K_p` to `K_p`. At the instance, the models of
  `hcls ∧ hadm ∧ hgate ∧ H` are exactly the `cnot`-invariant convex cones between `K_cl` and `Q3` [D + W + L].
- **Routes refuted** (countermodels of the route's own premises; evidence as marked):
  - completion + bi-affine tables + identification without finite rank (`D_cl`, [X] skeleton + [W]);
  - K2 as "coordinate-model Composite with local tomography" (`K_cl`'s slice, landed Q2: landed X + W);
  - identification with a native closure:
    - `SEP`: `hgate` fails, −2, landed I2;
    - `K_gen`: FCC fails, −1/8 [X], so H fails by Lemma B1 [D];
    - `K_E`: FCC fails, −1/2 [X];
    - closure under `actT reflY ∘ cnot`: no valid stages, −1/2 [X].
- **Survives the countermodels only:** nothing here is asserted on that basis.
- **Local tomography, explicitly:** it is used only by product-labels-only constructions (which give finite rank and LT
  together) and by P-STAGE2's injective chart. The closedness argument does not use it (`D_pad` [X]). It does not give
  `hcl` (landed Q2).

### 0.1 The two verdicts (amendments 1 and 2)

**(A-i) Completion — DERIVED.**
- *Construction.* `DirectedStages.prod` (UNBUILT `lean/PairComp.lean` §1):
  - index: the product preorder;
  - stage `(i, j)`: preparations `P_i × P'_j`, labels `E_i × E'_j`, table `p((e, f), (x, y)) = e(x) f(y)`, unit
    `(1, 1)`;
  - maps: products of the factor maps.
  The laws `directed`, `comp_E`, `comp_P`, `unit_map` and SC∞ hold componentwise ([W]; `scInf_prod`). The cnot closure
  adds to each stage the gate images `cnot(prodState x y)` with table `prodEffVal e f (cnot(prodState x y))`.
- *Closed in which space.*
  - In ℓ^∞ over all labels, for every directed system: `body_isClosed` [K] (CompletionAction.lean:202).
  - For the two constructed systems, the completed body is also `Ψ(S)` with `Ψ : W 3 → CSpace` linear and injective (16
    spanning product labels). `S` is the closed convex hull of the product tables (resp. of these and their `cnot`
    images). It is compact; it is the normalized slice of `SEP` (resp. `K_gen`) when the factor preparations are dense
    in the ball, and the rank is then 15. The read-out is `S`. The argument is [W] (W-A1). [X] on the finite instance
    `a1` (25 checks):
    - the laws (A1.1–A1.4) and SC∞, with a countercontrol (C2);
    - bi-affine tables (A1.5–A1.6);
    - the cnot-closure tables in `[0, 1]` (A1.7; universal by the [W] step from `cnot_prodState_mem_maxCone` [K]);
    - rank 16 (A1.10–A1.11);
    - closing under `actT reflY ∘ cnot` gives the table value −1/2 (A1.9).
- *Premises.* None beyond the construction and [K]. Local tomography holds **by construction** (only product labels;
  K2-LEDGER D6) and is named here as such. It is a property of the constructed systems, not an assumption about a given
  pair system.
- *Scope.* These are constructed systems. No OI-native pair system (for instance a protocol tower for two balls) is
  defined at L, and whether one is such a product is not addressed.

**(A-ii) Correspondence with the theorem's `K_p ⊆ W 3`, hence `hcl` — INDEPENDENT of the premises certified at L as
stated.** Countermodel: `M_cl` (uniform `K_cl`, `N_p = cnot`, identity locals), realized through `D_cl` (§1, N3.3).
`hcl` and IE1 fail (landed M_cl.5–M_cl.11; [X] a2 A2.5–A2.7 gives a PSD-free certificate of `T_ψ ∉ K_gen`).

The certified premises bearing on the target, and the check that the model satisfies each:

| certified at L | how it bears on `hcl` | `M_cl` / `D_cl` satisfies it by |
|---|---|---|
| COMP-1 `ProductData`, `PreComposite` (CompositeInterface.lean:210, :223) | interface of a pair body | landed I1 [X] with I1W [W]; re-checked a4 A4.8 [X] |
| COMP-1 `Composite.lt` (:243) | local tomography of the pair body | landed I1W [W]: the `lt` argument of `minComposite`/`maxComposite` (`prodEff_eq_of_eff_eq` :342 with `modelData_ext` :740) |
| `CandidateCone` (K2Guard.lean:95) | products in `K`, `K ⊆ maxCone` | landed M_cl.2 [W] with D1–D6 [X] |
| `NativeGate (eball 3) z3 nflip cnot` (`nativeGate_cnot`, CompositeDimension.lean:1160) | the gate's hypotheses | a property of `cnot` alone [K]; `cnot` preserves `K_cl` (landed M_cl.3 [W], D1–D2 [X]) |
| `no_candidateCone_cnot_reflY` (K2Guard.lean:143) and the other DIM-1, EFF-1 and K1-BRIDGE-1 theorems | constraints on candidate cones | theorems at L, consistent with any model; `K_cl` is `cnot`-invariant and not `actT reflY`-invariant, which is consistent |
| completion layer (`DirectedStages` :63, `SCInf` :78, `body` :141, `body_isClosed` CA:202, chart lemmas) applied to a pair system | the only certified source of closedness | `D_cl` is a `DirectedStages` of finite stages; SCInf holds (one global table); its body is closed in ℓ^∞ [K]; its read-out is `K_cl` (W-A3; [X] a3 A3.1–A3.10 on the stages `n ≤ 4`) |
| the theorem's other hypotheses `hcls`, `hadm`, `hgate`, `H` (not certified premises) | — | landed Q1-CL (`M_cl` satisfies all four) |

Not satisfied, and not certified at L:
- `FiniteRank` of the pair completion. It is a definition (StageCompletion.lean:299) whose truth is the open K∞-Stage
  obligation (ROADMAP.md:1010; Main.md:542). `D_cl` has infinite rank.
- ID and P-STAGE2.

Scope: `hcl` is independent of the premises certified at L as stated. It is not independent of `FiniteRank ∧ ID` or of
P-STAGE2, each of which implies it (N3.2, N4.2). It is not claimed independent of every extension of the framework.

Further results under (A-ii):
- *The constructed completions do not correspond* (route refuted at the instance, [X]):
  - `SEP` breaks `hgate` (landed I2, −2);
  - `K_gen` breaks FCC (a2 A2.9, −1/8), hence H by Lemma B1 [D];
  - `K_E` breaks FCC (a2 A2.14, −1/2).
- *The forms of correspondence that do give `hcl` are restatements.* ID ⟺ `hcl` and P-STAGE2 ⟺ `hcl`, relative to
  `hadm`, with a separate argument for each direction (N4.2).
- *Uses of local tomography (K2), named.*
  - (i) Product-labels-only constructions. They give finite rank and LT at once (W-A3.3).
  - (ii) P-STAGE2's chart *onto* `W 3`. This is injectivity of the read-out on the completed body, i.e. LT of the
    completed pair system.
  Neither use is needed for closedness (`D_pad`, a4 A4.4–A4.7). LT does not suffice for it (`K_cl`'s slice is an LT
  Composite).

## 1. Routes and countermodels, node by node

**N0 (A0) — what `hcl` does in the theorem.** Read from the design code ([D]): `kt4_general_ie1`
(FourCopyHeadline.lean:102) consumes `hcl` only in `inv_mem_of_orth (hcls p).ipW_map (hcl p) (hgate p)` (Lemma R,
FourCopyBipolar.lean:148) and `bidual_of_adm (hadm p) (hcl p)` (FourCopyBipolar.lean:110). The latter's output `hbi`
feeds `cross_rel`, the four `inv_*` lemmas and `ie1_of_dualW`.

*W-A0 (closure form; sufficiency proved [D + W]; UNBUILT Lean §2).* Assume `hcls ∧ hadm ∧ hgate ∧ H`.
1. Lemma B1 (`fourCopyCoherent_of_kt4Core`, FourCopyBridge.lean:269 [D]) gives FCC(K).
2. Each hypothesis passes to `cl K_p`:
   - products lie in `cl K_p`;
   - `cl K_p ⊆ maxCone`, since `maxCone` is the intersection of the closed half-spaces `{ω | 0 ≤ prodEffVal e f ω}`;
   - `cl K_p` is a convex cone, by continuity of `+` and of scaling;
   - `N_p(cl K_p) ⊆ cl(N_p K_p) ⊆ cl K_p` (a linear map in finite dimension is continuous);
   - `dualW(cl K) = dualW K`;
   - famI and famII are continuous in their state slots, and `cl K01 × cl K23 = cl(K01 × K23)`, so FCC(K) ⇒ FCC(cl K).
3. `kt4_general_ie1` [D], applied to `p ↦ cl K_p` with `hcl` given by `isClosed_closure`, gives
   `cl K01 = Θ(dualW K23)`, `IE1(cl K_p)` for every `p`, and `EvenCycle`.

So `hcl` is consumed only to pass IE1 from `cl K_p` to `K_p`. This fails in `M_cl` (IE1(`K_cl`) fails while
`cl K_cl = Q3`), so `hcl` cannot be dropped: there is no claim that it is inessential.

Verdict: POSITIVE/CONFIRMING. DEPGRAPH §7.2 recorded the parity part and EQ3-AUDIT the cross relation. The design
package's open `kt4_closure` (FourCopyPackage.lean:318, `sorry`) is a stronger closure-level classification that keeps
`hinv` as a hypothesis.

**N1 (A1) — the stage-level product.** Choices the definition must make, with their consequences:

| choice | preparations | labels / tables | status |
|---|---|---|---|
| P1 narrow product | `P_i × P'_j` | product labels; `e(x) f(y)` | valid; SC∞ (W-A1, UNBUILT §1; a1 A1.1–A1.6 [X]) |
| P2 + finite mixtures | adds rational mixtures | same | same completion as P1 |
| P3 + native-gate images | adds `N(prodState x y)` | product labels; the gate's action on `W 3` tables (presupposes the gate acts on product-test tables) | `N = cnot`: valid (a1 A1.7 [X]; [W] from `cnot_prodState_mem_maxCone` [K]); `N = actT reflY ∘ cnot`: invalid, value −1/2 (a1 A1.9 [X]) |
| P4 + local operations on joint preparations | (o)-steps | — | forbidden premise; not used |
| P5 dense subset of a given cone `K` | `K`'s slice | product labels | P-STAGE2 in disguise (`D_K`, N4.2) |
| joint labels | any | non-product labels allowed | completion may have infinite rank (`D_cl`, N3.3) |

*W-A1.*
- Laws: the product preorder is directed, and the maps compose componentwise.
- SC∞: `p_j(f(e), f(x)) = p_i(e, x)` in each factor, so the product of the two tables is carried.
- Read-out: with product labels whose homogenized coefficient vectors span `ℝ⁴`, the 16 basis labels determine a table
  (rank 16). The value map `Ψ(w) = (pairVal(ehom e, ehom f, w))_{labels}` is linear, bounded and injective, hence a
  closed embedding. `prepVec = Ψ ∘ table`, so `body = cl conv Ψ(tables) = Ψ(cl conv tables)`. For P1 this is `Ψ` of the
  normalized `SEP`, which is compact as the convex hull of a compact set in finite dimension.
- For P3 with `cnot`, the body is `Ψ(conv(SEP_n ∪ cnot SEP_n)) = Ψ(K_gen slice)`.

Verdict: CONFIRMING (COMP-1-DESIGN §2.1 anticipated the narrow product) and ELABORATING (gate closure is valid or invalid
by gate; exact at two instances).

**N2 (A2) — the completions at `d = 3`.**
- P1 (factor preparations dense in the ball): the body read-out is the normalized `SEP`, the landed `ball3MinComposite`
  body. It is closed. It is not `cnot`-invariant (landed I2: `w00 − w11 + w22 − w33` is `−2` at `phiW`).
- P3 with `cnot` (same density): `K_gen`. It is closed [W] and admissible (`prodState_mem_maxCone`, `cnot_prodState_mem_maxCone` [K]).
  It is `cnot`-invariant (`cnot` is an involution, A1.8 [X]). It is not `Q3`: `F ∈ dualW K_gen` by exact SOS
  identities (a2 A2.3–A2.4 [X] plus the [W] step that each SOS term is ≥ 0 on the ball), and `ipW(F, T_ψ) = −1/2`
  (A2.5) with `T_ψ ∈ Q3` (A2.7).
- IE1 fails for `K_gen`: `phiW ∈ K_gen` and `actT R_H phiW = T_ψ ∉ K_gen` (A2.6).
- FCC fails for uniform `K_gen`: famI at `(phiW, phiW, T_ψ/4, F)` is `−1/8` (A2.9; countercontrol C2 gives `1/4` with a
  `Q3`-dual effect). By Lemma B1 [D], H fails.
- The maximal native closure `K_E = dualW(K_gen) = maxCone ∩ cnot(maxCone)` (W A2.W6) is the largest admissible
  `cnot`-invariant cone. It is closed (a dual cone, `isClosed_dualW` [D]; or directly [W]) and contains the products
  (A2.15 + [K]).
  - It contains `F ∉ Q3` (A2.10–A2.11).
  - IE1 fails: `ipW(actT R0 F, cnot(prodState(−e2, e2))) = −2/5` (A2.12).
  - FCC fails: famI at `(F, phiW, cnot(prodState(e2, −e3)), cnot(prodState(e2, e2)))` is `−1/2` (A2.14). So H fails
    by B1 [D].
- Every admissible `cnot`-invariant convex cone `K` satisfies `K_gen ⊆ K ⊆ K_E` (W A2.W6). The inclusions
  `K_gen ⊆ Q3 ⊆ K_E` are [W] from the identities A2.16 [X]; both are strict (exact witnesses above).

Verdict: NEW — an exact obstruction for the class "identify the pair cone with the closure that native generation
selects (minimal) or that native no-restriction selects (maximal)" at this instance. Each candidate is closed and fails
H. Scope: the instance (`cnot`, identity locals, uniform cones) only.

**N3 (A3) — from the completion to `W 3`.**
- *N3.1 Read-out and LT.* `T` exists once 16 spanning product labels are labels (A1.10 [X]; countercontrol C6 has rank
  4). `T` is injective on the body exactly when the completed pair system is locally tomographic.
- *N3.2 W-A3.1 (sufficiency proved [K + W]).* If `body D` is nonempty with `FiniteRank`, then `T(body D)` is compact and
  the cone over it is closed:
  1. `body D` is closed and convex (`body_isClosed`, `body_convex` [K]). It lies in the unit ball of ℓ^∞
     (`val_nonneg`, `val_le_one`, `body_subset` [K]).
  2. `exists_completionChart` [K] gives a chart with `isClosedEmbedding_chart` [K]. The chart body is closed (a
     preimage) and bounded (the injective linear part is bounded below in finite dimension), hence compact. The body
     is its image (`mem_range_of_mem_body`, `chart_coordsOf` [K]), hence compact.
  3. `T` is continuous, so `T(body D)` is compact. It lies in `ω00 = 1` (`coord_unit_eq_one` [K]).
  4. A limit of `t_n s_n` with `s_n` in a compact `S ⊆ {ω00 = 1}` has `t_n → ω00` and a convergent subsequence of `s_n`,
     so the cone over `S` is closed.

  Injectivity of `T` and TAB are not used. `D_pad` is the model: on the a4 instance (A4.4–A4.7 [X]) its rank is the
  product-label rank plus 1 (5 = 4 + 1), LT fails, and its preparations read out to their product tables; with dense
  product preparations [W] its rank is 16 + 1.
- *N3.3 Without finite rank: route refuted.* The pair system `D_cl`:
  - preparations: `c_j`, dense in the `K_gen` slice, and `ρ_J`, dense in the `int Q3` slice;
  - labels: product labels with bi-affine tables, joint labels `b_S` (`S` finite) with `b_S(ρ_J) = [J ∈ S]` and
    `b_S(c_j) = 0`;
  - stage maps: inclusions; `ι = ℕ`.

  Its read-out cone is `K_cl` (W-A3). Exact skeleton (a3, 14 checks, stages `n ≤ 4`):
  - valid stages and SC∞ (A3.1–A3.2);
  - TAB read-out (A3.3);
  - rank `2n` (A3.4);
  - the `ρ_J` pairwise at sup-distance ≥ 1 (A3.5), while on product labels `τ_k → T_ψ` at distance `t_k/4` (C3);
  - `τ_k`, `cnot τ_k` positive definite and `T_ψ` rank-deficient (A3.6–A3.7);
  - `T_ψ ∉ K_gen` (A3.8);
  - sample mixtures positive definite (A3.9);
  - the ℓ¹ norming inequality on samples (A3.10).
  The one-line generalizations to all `n` are [W] (A3.W3). The same construction with `C = Q3` slice and `ρ` dense in
  `int maxCone` realizes `M_int`'s cone (A3.11 [X], A3.W2 [W]).

  *W-A3.*
  - Let `Φλ = (Σ_{J∈S} λ_J)_S`. Then `‖Φλ‖_∞ ≥ ½‖λ‖₁`, by taking `S` the support of the positive or of the negative
    part.
  - A sup-norm Cauchy sequence of convex combinations `Σμ_i c_i + Σλ_J ρ_J` therefore has ℓ¹-convergent `λ`. Its
    product-label part converges in the finite-dimensional image of `Ψ`. Since `K_gen`'s slice `C` is compact,
    `body D_cl = {(Ψ((1−|λ|)c + Σλ_J ρ_J), Φλ) : c ∈ C, λ ≥ 0 in ℓ¹, |λ| ≤ 1}`. One inclusion is by truncation and
    density; the other by closedness of this set.
  - So `T(body) = {(1−|λ|)c + Σλ_J ρ_J}`.
  - For `λ ≠ 0` this is positive definite, since `Σλ_J ρ_J ⪰ (Σλ_J λ_min(ρ_J)) I` with a positive coefficient.
    For `λ = 0` it is `c ∈ C`. Every point of the open convex `int Q3` slice is a finite convex combination of the
    dense `ρ_J`.
  - Hence `T(body) = C ∪ int Q3` slice, which is the `K_cl` slice.

  Verdict: NEW — an exposed hidden assumption. The closedness content of P-STAGE2 is finite rank (compactness) of the
  pair completion, not completion as such and not LT. Finite rank of the factors does not give it: `D_cl`'s marginals
  are ball states.
- *N3.4 K2 does not give `hcl`* (route refuted). The slice of `K_cl` is a COMP-1 `Composite` including `lt` (landed Q2,
  I1/I1W; A4.8 [X]). Verdict: CONFIRMING.

**N4 (A4) — the identification.**
- *N4.1 Which feature excludes `K_cl`.* Finite rank of the completion, together with ID (N3.2). The ℓ^∞ closure alone
  does not exclude it (N3.3).
  - For a pair system indexed by a countable preorder, the cone over the finitely preparable tables has countably many
    extreme rays. It therefore cannot contain every pure product, and pure products are extreme rays of `maxCone`
    [W, W-A4.1]. So `hadm` already forces `K_p` to contain limit points.
  - *W-A4.1.* Let `|x| = |y| = 1` and `x̂ŷᵀ = ω1 + ω2` with `ω_i ∈ maxCone = {ω : aᵀωb ≥ 0 ∀ a, b ∈ L}` (landed note
    F.max). Take `a ∈ L`.
    - `u_i = ω_iᵀa` lies in `L* = L` (self-duality of the Lorentz cone, landed F6).
    - `u_1 + u_2 = ŷ (x̂·a)`, and `ŷ` spans an extreme ray of `L`, so `u_i = c_i(a) ŷ` with `c_i` linear.
    - Hence `ω_i = ℓ_i ŷᵀ`. Symmetrically `ω_i = x̂ m_iᵀ`, so `ω_i` is a nonnegative multiple of `x̂ŷᵀ`.
    - An extreme ray of `cone(conv A)` is spanned by an element of `A`.
  - With an uncountable index preorder, every convex set — `K_cl` included — is the set of finitely preparable states.
  - ELABORATING.
- *N4.2 ID ⟺ `hcl` relative to `hadm` (both directions proved).*
  - (⇒) is W-A3.1.
  - (⇐) W-A4.2: for `K` closed and admissible, its slice `S` is compact (closed, and bounded by
    `abs_le_one_of_maxCone` [D] or directly [W]) and convex. Take `Q` countable and dense in `S`. `D_K` has stage `n`
    with preparations `q_1..q_n` and the product labels of a fixed effect list. Its tables lie in `[0, 1]`
    (`S ⊆` normalized `maxCone`). Its body is `Ψ(cl conv Q) = Ψ(S)`, of finite rank, with read-out `S`, and the cone
    over `S` is `K`. [X] instances: `Q3`, `maxCone`, `K_gen` (a4 A4.1–A4.3, countercontrol C1).
  - `D_K`'s read-out is injective, so the same equivalence holds for P-STAGE2: its LT clause constrains the witnessing
    system, not `K_p`.
  - Verdict: NEW. It sharpens the landed reading "P-STAGE2 … presupposes K2". As a condition on the theorem's `K_p`,
    P-STAGE2 and ID are `hcl` restated. LT and finite rank are substantive only for a *given* pair system.
- *N4.3 Instance characterization (sufficiency proved, [D + W + L]; not kernel-checked).* At `cnot`, identity locals and
  uniform cones, the models of `hcls ∧ hadm ∧ hgate ∧ H` are exactly the `cnot`-invariant convex cones `K` with
  `K_cl ⊆ K ⊆ Q3`.
  - (⊆) By W-A0, `cl K` satisfies `hcls ∧ hadm ∧ hgate ∧ IE1`. The landed written classification (result.md Q1-NEC,
    C.W, with its Lie-theory input [L]) gives `cl K = Q3`, by the matched pattern with identity locals. Then
    `int Q3 = int cl K = int K ⊆ K` [L: convex sets in finite dimension]. `hadm ∧ hgate` give `K ⊇ K_gen`.
  - (⊇) `hadm` and `hgate` hold. For H: `cl K = Q3`, so `dualW K = dualW Q3`, and FCC follows from FCC(`Q3`) as in
    landed M_cl.4; the explicit carrier (landed S2, H.W) gives H.
  - So `K_cl` is the smallest model, and `hcl` ⟺ `K = Q3` ⟺ every rank-deficient state of `Q3` lies in `K`.
  - ELABORATING (sharpened gap), conditional on the written classification.

**Pass 2 — other closure principles** (no NEW finding).
- Twisted self-duality `K01 = Θ(K23*)` implies closedness. Relative to the other hypotheses, W-A0 gives
  `cl K01 = Θ(K23*)` [D + W], so it is `hcl` restated.
- No-restriction `K = dualW dualW K` is `hcl` for nonempty convex cones (`dualW_dualW` [D]): a restatement.
- The minimal and maximal gate-invariant admissible cones are `K_gen` and `K_E` (N2): independent principles,
  inconsistent with H at the instance.
- "The closure of what is preparable at finite stages" is ID (N4.2), and it needs finite rank (N3.3).

**Pass 3 — sources of finite rank** (no NEW finding).
- Product labels only (with TAB) give finite rank and LT together (W-A3.3: `prepVec = Ψ ∘ table`). This is K2-LEDGER
  D6's relocation of LT, and using it is a use of K2.
- Finite rank of the factors does not give finite rank of the pair (`D_cl`).
- Open lead, not settled: under an N-CLASS gate of infinite order, Milman's converse of Krein–Milman [L] allows a pure
  state in the closed hull of the orbit of pure products only if it lies in the closed orbit, so an entangled pure
  eigenvector is never reached.

The question is answered; passes 2–3 and the pressure tests yield nothing beyond pass 1. Fixed point.

## 2. Ledger — certified versus added

| premise | class | anchor (in `pt/base/` unless noted) | used by | statement match / note |
|---|---|---|---|---|
| `DirectedStages`, `FiniteStage`, `StageMap`, `SCInf` | [K] | StageCompletion.lean:63, :78, :53; KInfFoundations.lean:63 | A1 construction | exact (definitions) |
| `prepVec`, `body` (closed convex hull), `val_nonneg/le_one`, `body_subset`, `coord_unit_eq_one`, `continuous_coord` | [K] | StageCompletion.lean:135, :141, :102, :105, :171, :204, :164 | W-A3.1, W-A1 | exact |
| `body_isClosed`, `body_convex` | [K] | CompletionAction.lean:202, :200 | (A-i), W-A3.1 | exact |
| `FiniteRank` (definition) | [K] def | StageCompletion.lean:299 | W-A3.1 | definition only; its truth is not certified |
| `exists_completionChart`, `isClosedEmbedding_chart`, `mem_range_of_mem_body`, `chart_coordsOf` | [K] | CompletionAction.lean:154, :189, :171, :175 | W-A3.1 | exact |
| `prodState`, `pairVal`, `ehom`, `prodEffVal`, `maxCone`, `actT`, `cnot`, `phiW`, `W` | [K] | CompositeDimension.lean:161, :164, :167, :182, :186, :198, :775, :1220, :97 | all scripts (transcription re-checked S0) | exact; `W` carries the comment "local tomography is the premise this carrier encodes" (:95–96) |
| `cnot_prodState_mem_maxCone`, `cnot_prodState_xplus_z3`, `nativeGate_cnot`, `lor_ehom`, `isEffectOn_affOf` | [K] | CompositeDimension.lean:1152, :1222, :1160, :930, :916 | P3 validity, `K_gen ⊆ maxCone`, `dualW SEP = maxCone` | exact |
| `CandidateCone`, `prodState_mem_maxCone`, `idW`, `chainW`, `chain_value` | [K] | K2Guard.lean:95, :165, :101, :104, :134 | `hadm` checks, A1.9 | exact |
| COMP-1 `ProductData`, `PreComposite`, `Composite`, `prodEff_eq_of_eff_eq`, `modelData_ext`, `minComposite`, `ball3MinComposite`, `paddedPre` | [K] | CompositeInterface.lean:210, :223, :243, :342, :740, :750, :807, :848 | (A-ii) table, N3.4, `D_pad` analogy | exact |
| `fourCopyCoherent_of_kt4Core` (Lemma B1), `kt4_general_ie1`, `kt4_forward_ie1`, `bidual_of_adm`, `inv_mem_of_orth`, `dualW_dualW`, `isClosed_dualW`, `abs_le_one_of_maxCone` | [D] | `pt/inputs/fourcopy/`: FourCopyBridge.lean:269, :111; FourCopyHeadline.lean:102, :120; FourCopyBipolar.lean:110, :148, :81, :31 | W-A0, H-failure of `K_gen`/`K_E`, N4.3 | design run only, not certified |
| landed result note KT4-PREM-1 (M_cl, M_int, I1/I1W, I2, Q1-NEC classification) | certified round record (exact + written) | `round-kt4-prem-1-premise-audit/result.md`; probe check ids | (A-ii), N4.3 | its written steps stay written |
| `FiniteRank` of the pair completion | [N] (pair-level instance of the open [A] obligation K∞-Stage, ROADMAP.md:1010; Main.md:542) | — | W-A3.1 | independently motivated (finite predictive dimension); not a restatement: it says nothing about any given `K_p` |
| TAB (bi-affine product tables) | [N] | completion form of COMP-1's bilinear `prodEff` field (CompositeInterface.lean:216) | the read-out's meaning | independently motivated (local effects compose bilinearly) [L, unverified for the GPT literature]; not consumed by closedness |
| PAIR-SYS (the pair system is a finite-stage `DirectedStages` with product labels) | [N] | none at L (no pair `DirectedStages` exists: census in the landed note) | ID | independently motivated ("composites are systems") |
| ID (the theorem's `K_p` is the read-out cone of a finite-rank pair completion) | [N] | — | `hcl` | **restatement**: ⟺ `hcl` relative to `hadm` (N4.2) |
| LT / K2 | [N] named (K2 OPEN, ROADMAP.md:1001) | `Composite.lt`; `W` (:95–96) | only product-labels-only constructions and P-STAGE2's injectivity | independent; neither needed for closedness nor sufficient for `hcl` |
| ID-gen (`K_p` = native closure `K_gen`) / NR-gen (`K_p = K_E`) | [N] | — | N2 | independent; inconsistent with H at the instance |

Forbidden premises: none used. `Q3`/PSD enter only as properties of countermodels and of the intended model, never as a
premise of a route. No (o)-step, idle extension, IE1 or IE2 is assumed; IE1 of `cl K` in N4.3 is derived (W-A0). ID is
flagged as `hcl` restated.

## 3. Candidate table

Verdict per model: ✓ the model satisfies the candidate and the target; ✗ the model satisfies the candidate and violates
the target (implication refuted); — the model violates the candidate (not a test).

| candidate | statement | class | tested | `M_Q` | `M_cl` | `M_int` | `M_max` | `D_cl` | other | verdict | independence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| C0 certified layer | everything certified at L bearing on `hcl` | [K] | ⇒ `hcl` | ✓ | ✗ | ✗ | ✓ | ✗ | — | refuted (INDEPENDENT) | — |
| C1 K2/LT | the pair is a coordinate-model Composite (`lt`) | [N] | ⇒ `hcl` | ✓ | ✗ (landed Q2) | — | ✓ | — | `D_pad`: LT fails, closed | route refuted | independent |
| C2 TAB | product tables bi-affine | [N] | ⇒ `hcl` | ✓ | ✗ (via `D_cl`) | ✗ | ✓ | ✗ | — | route refuted | independent |
| C3 FiniteRank (alone) | pair completion of finite rank | [N]/[A] | ⇒ `hcl` | ✓ | ✗ (`M_cl` with any finite-rank system, e.g. `D_K` for `Q3`: no link to `K_p`) | ✗ | ✓ | — | — | route refuted | independent |
| C4 ID⁻ (no finite rank) | `K_p` = read-out cone of a pair completion | [N] | ⇒ `hcl` | ✓ (`D_Q3`) | ✗ (`D_cl`) | ✗ (W A3.W2) | ✓ | ✗ | — | route refuted | — |
| C5 ID | C4 + finite rank | [N] | ⇒ `hcl` | ✓ | — | — | ✓ | — | — | **sufficiency proved** | **restatement** (⟺ `hcl` rel. `hadm`) |
| C6 P-STAGE2 | C5 with injective read-out | [N] (landed) | ⇒ `hcl` | ✓ | — | — | ✓ | — | — | sufficiency proved (landed + W-A3.1) | restatement (N4.2) |
| C7 ID-gen | `K_p` = closure of native preparations (products, mixtures, `cnot`) | [N] | ⇒ `hcl`; ⇒ consistent with H | — (`Q3 ≠ K_gen`) | — | — | — | — | `K_gen`: closed, FCC −1/8 | `hcl` proved; inconsistent with H at the instance (route refuted) | independent |
| C8 NR-gen | `K_p = dualW`(native effects) | [N] | same | — (`F ∈ K_E∖Q3`) | — | — | — | — | `K_E`: closed, FCC −1/2 | same | independent |
| C9 SD | `K01 = Θ(K23*)` | [N] | ⇒ `hcl` | ✓ | — | — | — | — | — | sufficiency proved | restatement relative to H (pass 2) |
| C10 NR | `K = dualW dualW K` | [N] | ⟺ `hcl` | ✓ | — | — | ✓ | — | — | equivalence [D] | restatement |

## 4. Cross-thread notes

- **B (PAIR-ACT).**
  - The narrow product has no `cnot` operation datum: `cnot` leaves its body (landed I2).
  - In the `cnot`-closed product, `τ(x⊗y) := prepVec(cnot(x⊗y))` is an `OpDatum`, its own inverse. Its `AffineRespect`
    follows from `prepVec = Ψ ∘ table` with `Ψ` injective and `cnot` linear [W]. So P-ACT2 holds there, and `hgate`
    holds for `K_gen`, but H fails (FCC −1/8). Sourcing `hgate` this way yields a cone the four-copy hypothesis rejects.
  - For `actT reflY ∘ cnot` there is no valid gate-closed system (−1/2, a1 A1.9).
- **C (FOUR-COMP).**
  - FCC fails exactly for the two native closures: uniform `K_gen` (−1/8) and uniform `K_E` (−1/2) (a2).
  - FCC passes to closures and from them: `FCC(K) ⟺ FCC(cl K)` (W-A0; duals are unchanged by closure). A four-copy
    principle that yields FCC is therefore blind to `hcl`.
  - At the instance, `hcls ∧ hadm ∧ hgate ∧ H` pins `cl K = Q3` (N4.3).
- **D (NCLASS-ADM).**
  - For a countably indexed pair system, `hadm`'s product clause cannot hold for the finitely preparable cone (N4.1).
  - At the instance, `hadm ∧ hgate` place `K` in `[K_gen, K_E]` (N2).
- **Integration (K2).** Local tomography is used only where a given pair system's completed state space is identified
  with a subset of `W 3`. The open obligations that would make a completion route source `hcl` are:
  - a pair system given independently of `K_p`;
  - its finite rank;
  - a proof that its read-out satisfies H.
  Each native construction examined fails the last.

## 5. What is not claimed

- `hcl` for the theorem's `K_p` is not claimed, derived or sourced. INDEPENDENT is relative to the premises certified at
  L as stated. It is not a statement about every extension of the framework: `FiniteRank ∧ ID`, and P-STAGE2, imply
  `hcl`.
- No necessity claim is made: no premise is called "required" without a proof of `P ∧ C ⇒ A`.
- Not kernel-checked:
  - W-A0 is written from [D] lemmas; its Lean text is UNBUILT;
  - N4.3 rests on the landed written classification (one Lie-theory input) and on convex analysis [L].
- [X] results hold for the instances checked:
  - the finite stages `n ≤ 4` of `D_cl`;
  - the sample families of a1 and a4;
  - the effect lists named in each script.

  Universal statements rest on the cited [W] arguments or on symbolic identities.
- The native-closure obstruction (N2) is for the instance `cnot`, identity locals, uniform cones. The infinite-order
  N-CLASS case is open (pass 3).
- No countermodel is a physical theory. `D_cl`'s joint labels are a mathematical device. No OI-native pair system is
  defined at L, and none is claimed here.
- Nothing here edits or proposes edits to `main`, the ROADMAP, manuscripts or Lean results.

## 6. Evidence log

`python3 -I -B`, Python 3.11.15, sympy 1.14.0. Exact arithmetic only. Decision rules sit in each script header and were
fixed before the first run. VERDICT lines print only over green checks and countercontrols. No timing appears in stdout,
and every `.err` file is empty.

| script | sha256 (script) | sha256 (output) | checks | runs | replay |
|---|---|---|---|---|---|
| `a1_stage_product.py` | `981769080d6382ddc8a90cec514ed456bfe7414358a41ac841819e3041bdf526` | `fb03dd86ddbdb1473b481cc11fa9f882430f1f3993cf30cde524f6f420ae47a6` | 25 PASS, 0 FAIL (3 countercontrols) | 1 | byte-identical |
| `a2_native_closures.py` | `8c444c60d5370ee7f4fea1f7c4bc1bd0dca1542abf9418d922ced57be2d79fbe` | `ada90286c117ca3f7fcfa958701ba68c648477e29c01eb5206a2dea8ef826649` | 22 PASS, 0 FAIL (4 countercontrols) | 2 | byte-identical |
| `a3_shadow_countermodel.py` | `ed4ff5d63e0245aa2b421561e4ac187208e5b16ca70482df33f1e0c9d7176455` | `6d2de61ec3c7a2f49a7c20f87638cb773a0941dc7eaa3bf7ea7d6cd5ae49391f` | 14 PASS, 0 FAIL (2 countercontrols) | 2 | byte-identical |
| `a4_identification.py` | `d117f72a79445da97e34b657af5b6a63669a492cfdaeaf7b92c8bc675ac43f1f` | `611dc429e95871c46b5c427daf40d77615285e550d2f531db3a271985b368fa4` | 12 PASS, 0 FAIL (3 countercontrols) | 1 | byte-identical |

Earlier runs, kept:
- `a2_native_closures.run1.py` (`b2fc981f7e9a7a08b64a029d2b5784aeccaa2b849629db3bf2a91f4ec81a2f61`), output
  `5c8e3e4d7f5c5b89939410d4bf77d0bfa111af2371be831cb502dc043a73c3df`: 21/21 PASS.
- `a3_shadow_countermodel.run1.py` (`f3a3a01bc5c2f77e9079fa7c527483220a2ac2f7acb7fa03411f1a7812629f3b`), output
  `e6e227ed588926b8790ca24cfa321bb68ea0e12d6728fa409ba7b57a5985675a`: 14/14 PASS.

Both re-runs were wording corrections of over-broad verdict lines (NOTES.md "Runs and pre-run edits"). Run 2 of a2 adds
check A2.16. Run 2 of a3 has PASS/FAIL lines identical to run 1.

Exploration [E], not evidence:
- `explore/e1_objects.py` / `.out`: `7de9f5c6…4149` / `0ccc82ab…60bb`;
- `e2_fcc_KE.py` / `.out`: `8d2c57c9…3a31` / `b0b2eb53…65e7`;
- `e3_fcc_KE_witness.py` / `.out`: `b9f86fdf…6735` / `6628142e…44ce3`.

UNBUILT Lean: `lean/PairComp.lean` (`633152999c1369d9fc41799fd3a66a10f6d628092a41d0b4e3e8025657c6fb8d`).
Notes: `NOTES.md`.

## 7. Integrity

Start (recorded in `.start_marker` before any work):
- `sha256sum -c --quiet inputs.manifest.sha256`: rc 0;
- `git -C base rev-parse HEAD` = `9f9f8257a980a1819fbbc1dc0019917cf8678626`;
- `git -C base status --porcelain`: empty;
- protocol sha256 `239dc123…fa9b23`.

End (run after all scripts, replays and notes, before this block was written):

```
$ sha256sum -c --quiet inputs.manifest.sha256
rc=0
$ git -C base rev-parse HEAD
9f9f8257a980a1819fbbc1dc0019917cf8678626
$ git -C base status --porcelain
rc=0 (empty output above = clean)
$ sha256sum PROTOCOL.md PROTOCOL-AMENDMENT-1.md PROTOCOL-AMENDMENT-2.md
239dc123b07cb83f354a0f9def3cc39f5fd025fb2f6b4f3c4ba3d3e0ddfa9b23  PROTOCOL.md
b41aa0e735b3ca0bf7fb08c3629dd9a18c6d979039c6ba005fd707330831cf83  PROTOCOL-AMENDMENT-1.md
2a2f78f374e5dfb541854677060481a0e40bda636c1649a850a132f3b27c530a  PROTOCOL-AMENDMENT-2.md
```

Every file in `pt/A/` (39 files: `.start_marker`, `NOTES.md`, `RESULT.md`, four scripts with `.out`/`.err` and replays,
two `.run1` triples, three exploration triples, `lean/PairComp.lean`) was written by this thread. No foreign file
appeared; nothing was quarantined. No write outside `pt/A/`; read-only git only (`rev-parse`, `status`). Integrity
events: none.
