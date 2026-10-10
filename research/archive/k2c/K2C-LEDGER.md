# K2C-LEDGER — composite cone, universality, orientation (off-repo research ledger)

Status: COMPLETE for this pass. One depth-first pass. The §A.31 fixed point is **not** reached (§7).

## 0. Base, scope, evidence layers

- **Base.** `wt-68b` at `68b6df0651f14b2c8ab082635b8d2051918617a2` (`git rev-parse HEAD`). It is read-only:
  `git status --porcelain` is empty at the end of the pass. No git write was run. Every write is under
  `scratchpad/k2c/`. The `k2d/` bytecode cache was reused, not rewritten (mtime 12:34, before this session). Paths
  are relative to `verification/lean-mathlib/OIBridge/`.
- **Scope.** This is ungoverned, off-repo research. Nothing here is frozen, certified, adopted, or proposed as
  ROADMAP or manuscript wording. Every hypothesis named is a premise, and none is established.
- **Prior research consumed as data, not re-certified unless re-run:** `k2d/K2-LEDGER.md` (T5, T6, T7, A5, H3),
  `threads/E/RESULT.md` (P5–P14: the 32 gates, the parity rule, the 15/105 Lie closures, and the *written* cone
  theorem P12 with LG = a continuous local group and a closed convex cone), `sa/SA-LEDGER.md` §5 (countable operation
  families; question K2-c), and `kg/` (K2-GUARD-1 result).
- **Layers. They are kept distinct and none substitutes for another:**
  - `[K]` a kernel theorem or definition at the base (file:line).
  - `[X]` an exact computation in DIM-1 coordinates that uses kernel definitions only. Tables and maps are parsed or
    transcribed literally from the Lean source.
  - `[M]` an exact computation that uses the matrix model (complex 4×4 matrices, Pauli dictionary). It is evidence
    about QM, not about the kernel.
  - `[W]` a written argument.
  - `[L]` a literature-standard fact, not re-proved here.

## 1. Task 1 — the positive witness (orientation-preserving side)

### Node 1a — the coordinate dictionary, derived from the kernel definitions. Check: P1, 30/30

`W 3` is identified with `Herm(ℂ²⊗ℂ²)` by `ω_{μν} = Tr((σ_μ⊗σ_ν)ρ)`. Index 0 is the unit, and 1, 2, 3 are Bloch x, y, z,
as fixed by `hom x = vecCons 1 x` (`CompositeDimension.lean:100`). The checks are exact and symbolic. The kernel
objects `pc`, `pt`, `sgn`, `nflip` and `reflY` are parsed from the Lean files. `actT` and `actC` are transcribed
literally (`:198`, `:201`, `homMap` `:112`) and compared with their matrix forms (P1.6a–b).

- P1.1: the map is a real-linear bijection `Herm(4) ↔ W 3`.
- P1.2: `q(ρ(x)⊗ρ(y)) = prodState x y`.
- P1.3: `Tr((E_a⊗F_b)ρ) = pairVal a b ω`, so `ehom e` is the Pauli vector of the effect operator.
- P1.4: `E_a ⪰ 0 ⇔ Lor a` (kernel `Lor`, `:869`), from the characteristic polynomial.
- **P1.5b: the parsed kernel `cnot` is exactly the transfer matrix of `Ad(CNOT_{A→B})`** (control = first index).
  - Countercontrols: it is not `Ad(CNOT_{B→A})`, not `Ad(CZ)`, and not `cnot' := actT reflY ∘ cnot ∘ actT reflY`
    (P1.5c–e).
  - Cross-check: identical to k2d's independent parser (`k2lib.kernel_cnot_matrix`, P1.5f).
- **P1.7e–f: for every quaternion `q ≠ 0`, `actT R(q)` is the transfer matrix of `Ad(I⊗U_q)` and `actC R(q)` is that of
  `Ad(U_q⊗I)`.** These are symbolic identities in `q`. `R(q)` is the Bloch action of `U_q` (P1.7a–d: orthogonal,
  `det 1`). Surjectivity of `q ↦ R(q)` onto SO(3) is `[L]` (Euler–Rodrigues).
- P1.8: `actT nflip = Ad(I⊗X)`, `actC nflip = Ad(X⊗I)`.
- **P1.9: `actT reflY` is the partial transpose on copy B, `actC reflY` is the partial transpose on copy A, and
  `actC reflY ∘ actT reflY` is the global transpose.**

Verdict: POSITIVE. DIM-1's `cnot` and local rotations are exactly the Pauli images of CNOT and local SU(2). This agrees
with k2d's P1 (9/9) and extends it to all of SU(2) and to both reflections. Layer `[M]`, with `[X]` for the
literal-definition checks.

### Node 1b/1c — the PSD cone `Q3` is a candidate cone invariant under `cnot` and local SO(3) on both copies. Check: P2, 20/20

The witness is stated **without ℂ**:
`Q3 := {ω | certW ω is PSD}`, where `certW ω := realify(ρ(ω))`. This 8×8 real symmetric matrix has entries that are
integer linear forms in `ω`, divided by 4 (verbatim from `p2_psd_cone.out`):

```
4·certW ω =
 [w00+w03+w30+w33, w01+w31, w10+w13, w11-w22, 0, w02+w32, w20+w23, w12+w21]
 [w01+w31, w00-w03+w30-w33, w11+w22, w10-w13, -w02-w32, 0, -w12+w21, w20-w23]
 [w10+w13, w11+w22, w00+w03-w30-w33, w01-w31, -w20-w23, w12-w21, 0, w02-w32]
 [w11-w22, w10-w13, w01-w31, w00-w03-w30+w33, -w12-w21, -w20+w23, -w02+w32, 0]
 [0, -w02-w32, -w20-w23, -w12-w21, w00+w03+w30+w33, w01+w31, w10+w13, w11-w22]
 [w02+w32, 0, w12-w21, -w20+w23, w01+w31, w00-w03+w30-w33, w11+w22, w10-w13]
 [w20+w23, -w12+w21, 0, -w02+w32, w10+w13, w11+w22, w00+w03-w30-w33, w01-w31]
 [w12+w21, w20-w23, w02-w32, 0, w11-w22, w10-w13, w01-w31, w00-w03-w30+w33]
```

| claim | check | layer |
| --- | --- | --- |
| `v^H ρ(ω) v = [u;v]^T certW ω [u;v]` | P2.1a, symbolic | `[M]` identity; PSD ⇔ PSD is `[L]` |
| products in `Q3` | P2.2a (ρ(x) ⪰ 0 ⇔ \|x\| ≤ 1, symbolic) and 49 rational pairs, exact minors (P2.2b). Kronecker of PSD is PSD: `[L]` | `[M]+[L]` |
| `Q3 ⊆ maxCone (eball 3)` | `pairVal a b ω = Tr((E_a⊗F_b)ρ)` (P1.3b) with `E_a⊗F_b ⪰ 0`; `Tr(PQ) ≥ 0` is `[L]`. 40 random instances (P2.3) | `[M]+[L]`; the instances are not proof |
| `certW (cnot ω) = O_C certW ω O_Cᵀ`, `O_C` a permutation | P2.4a, symbolic in ω | `[X]` statement, `[M]` origin |
| `\|q\|² certW (actT R(q) ω) = O_q certW ω O_qᵀ`, likewise `actC` | P2.4b–c, polynomial identities in (q, ω); `O_qᵀO_q = \|q\|² I` (P2.4e) | same |
| global transpose `actC reflY ∘ actT reflY` preserves `Q3` and commutes with `cnot` | P2.4d (`J certW J`), P2.4f | same |
| **countercontrol**: `actT reflY` and `actC reflY` move the `Q3` point `phiW` to `idW ∉ Q3` | P2.5a–e (singlet value −1/2) | `[X]` + `[M]` |
| strictness `SEP ⊊ Q3 ⊊ maxCone` | `phiW ∈ Q3`, witness `f = ω00−ω11+ω22−ω33 ≥ 0` on products, `f(phiW) = −2`; `idW ∈ maxCone \ Q3` (P2.6a–c, Cauchy–Schwarz `[W]`) | `[X]+[W]` |
| W's Euclidean pairing is 4 × Hilbert–Schmidt, so `Q3` is self-dual for it | P2.7 | `[M]` |

**What is field-neutral and what is not.** The statement of every item is real and lives in DIM-1 coordinates: the
predicate `certW`, the congruence matrices, and the kernel maps. Its **content is the matrix model**: the choice of
`certW` encodes the complex structure, and the proofs of "products ∈ Q3" and "Q3 ⊆ maxCone" are `[L]` matrix facts.
The witness is therefore a **consistency control**: it shows that the hypotheses "candidate, `cnot`-invariant, local
SO(3)-invariant" are jointly satisfiable. It is not a derivation of the composite cone.

### Node 1d — the reflection countercontrol, now on both copies

K2-GUARD-1's countercontrol was `nflip` (one rotation, chain value 0). The witness above upgrades it: an invariant
candidate exists for **all** of SO(3) on each copy, and for the global transpose. It exists for **no** one-copy
reflection.

## 2. Task 2 — the reflection corollary (negative side)

### Node 2a — `actT` and `actC` are monoid homomorphisms. Check: P3.1, symbolic, on the literal definitions

`homMap (A∘B) = homMap A ∘ homMap B` (P3.1a). Hence:
- `actT (A∘B) = actT A ∘ actT B` and `actC (A∘B) = actC A ∘ actC B` (P3.1b–c).
- `actT A` commutes with `actC B` (P3.1d).
- `actT id = id` (P3.1e).

Layer `[X]`. It is a one-line kernel lemma (`funext; Fin.cases; rfl/vecTail_homMap`).

### Node 2b — the corollary. Check: P3.2 symbolic; P3.3 replays the landed chain

For `S ∈ O(3)` with `det S = −1` (P3.2 uses `S = −R(q)`, which is every such `S`):
- `A := reflY Sᵀ` lies in SO(3) and `A S = reflY` (P3.2a–c).
- Hence `actT reflY = actT A ∘ actT S` and `actC reflY = actC A ∘ actC S` (P3.2d–e).

So invariance under `actT S` and under the **single rotation** `actT A` gives invariance under `actT reflY`, which
contradicts `no_candidateCone_cnot_reflY` (`K2Guard.lean:143`). The chain value −1/2 and the `nflip` control value 0
are reproduced by independent code (P3.3).

### Node 2c — the control copy. Check: P3.4

`actC reflY phiW = idW = actT reflY phiW` (P2.5e), so `cnot ∘ actC reflY ∘ cnot` sends `prodState xplus z3` to the
same `chainW`, with value −1/2. The landed obstruction therefore holds verbatim for a reflection of the **control**
copy. It is kernel-cheap: `cnot_prodState_xplus_z3` (`:1222`), a new `actC_reflY_phiW`, `cnot_idW` (`K2Guard:110`),
and `chain_value` (`:134`).

### Node 2d — the simultaneous reflection is compatible. Check: P2.4d, P3.5

The global transpose `τ = actC reflY ∘ actT reflY` commutes with `cnot` (P3.5b) and preserves `Q3` (P2.4d). The
chain through `τ` returns to the product (P3.5a).

So the local symmetry group of `Q3` is `{actC A ∘ actT B : A, B ∈ O(3), det A = det B}`:
- the pairs with `det A ≠ det B` reduce, by Node 2a, to a one-copy reflection and are excluded;
- the pairs with `det A = det B = −1` are `τ` times rotations and are admitted.

**The corollary must therefore say "one-copy", not "orientation-reversing on the composite".** This confirms thread E
(the antiunitary survivors).

### Lean sketches (UNCOMPILED; landed names reused)

```lean
-- Node 2a
theorem homMap_comp (A B : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (v : HVec d) :
    homMap (A ∘ₗ B) v = homMap A (homMap B v) := by
  funext i; refine Fin.cases ?_ (fun j => ?_) i
  · rfl
  · rw [homMap_succ, homMap_succ, vecTail_homMap]; rfl
theorem actT_comp (A B) (ω : W d) : actT (A ∘ₗ B) ω = actT A (actT B ω) := by
  funext μ; exact homMap_comp A B (ω μ)
theorem actC_comp (A B) (ω : W d) : actC (A ∘ₗ B) ω = actC A (actC B ω)   -- same, on columns

-- Node 2b: one rotation suffices
theorem no_candidateCone_cnot_reflection {K : Set (W 3)} (hK : CandidateCone K)
    (hC : ∀ ω ∈ K, cnot ω ∈ K)
    {S : Matrix (Fin 3) (Fin 3) ℝ} (hS : S ∈ Matrix.orthogonalGroup (Fin 3) ℝ) (hdet : S.det = -1)
    (hSK : ∀ ω ∈ K, actT (Matrix.toLin' S) ω ∈ K)
    (hA : ∀ ω ∈ K, actT (Matrix.toLin' (Matrix.diagonal ![1, -1, 1] * Sᵀ)) ω ∈ K) : False :=
  -- toLin' (diag * Sᵀ) ∘ₗ toLin' S = toLin' (diag * (Sᵀ * S)) = reflY ; then actT_comp and
  -- no_candidateCone_cnot_reflY hK hC
  sorry
-- the SO(3) form, as asked
theorem no_candidateCone_cnot_SO3_reflection {K} (hK : CandidateCone K) (hC : ∀ ω ∈ K, cnot ω ∈ K)
    (hR : ∀ R ∈ Matrix.specialOrthogonalGroup (Fin 3) ℝ, ∀ ω ∈ K, actT (Matrix.toLin' (R : Matrix _ _ ℝ)) ω ∈ K)
    {S} (hS : S ∈ Matrix.orthogonalGroup (Fin 3) ℝ) (hdet : S.det = -1)
    (hSK : ∀ ω ∈ K, actT (Matrix.toLin' S) ω ∈ K) : False
    -- from the previous theorem, with diag * Sᵀ ∈ specialOrthogonalGroup (det = (-1)(-1), (diag Sᵀ)ᵀ(diag Sᵀ) = S Sᵀ = 1)
-- Node 2c
theorem actC_reflY_phiW : actC reflY phiW = idW            -- fin_cases, as actT_reflY_phiW
theorem no_candidateCone_cnot_reflY_control {K} (hK : CandidateCone K) (hC : ∀ ω ∈ K, cnot ω ∈ K)
    (hR : ∀ ω ∈ K, actC reflY ω ∈ K) : False                 -- the landed proof with actC_reflY_phiW
```

The orthogonality bookkeeping (`Sᵀ S = 1`) is the only Mathlib cost. A `LinearMap` form needs `det` and inverse lemmas
instead.

## 3. Task 3 — cone uniqueness

Let `G := ⟨cnot, actT R, actC R : R ∈ SO(3)⟩` (as maps of `W 3`).

### Node 3a — what is `G`? Check: P4 (lower bound over GF(p) = upper bound, so each figure is rendered)

- **Case A (local + cnot): Lie algebra of the closure has dimension 15.**
  - Lower bound: GF(p) closure under brackets and `Ad(cnot)`.
  - Upper bound: an explicit 15-dimensional rational subspace, exactly closed under brackets and `Ad(cnot)`, that
    contains the six local generators (P4.1b–d).
  - That subspace is the transfer image of `ad(i·su(4))` (P4.1a, `[M]`), and `Ad(CNOT) ∈ Ad(SU(4))` (P4.5).
  - So `G ⊆ Ad(SU(4)) ≅ PU(4)` inside `SO(15)` on the traceless part. **It is PU(4), not SO(15)** (dimension 15,
    not 105). That `G` *equals* PU(4), i.e. that the group generated by one-parameter subgroups is the analytic
    subgroup of the generated Lie algebra, is `[L]`.
- **Countercontrols (P4.3):** local only gives 6; local + `actT nflip` gives 6, so a finite local gate adds nothing.
- **Case F (local + cnot'):** 15, but a different subspace (A + F spans 24 linearly; P4.2).
- **Cases D (local + cnot + actT reflY) and E (local + T_refl):** 105 = so(15) (P4.4).

These reproduce thread E P10/P11 independently, in kernel coordinates with the parsed `cnot`. Classification:
CONFIRMING.

### Node 3b — `maxCone = block-positive = dual of separable`. Check: `[K]` + `[W]` + P1.3b/P1.4/P2.7

- `[K]`: `ω ∈ maxCone (eball 3) ⇔ ∀ a b, Lor a → Lor b → 0 ≤ pairVal a b ω`.
  - (⇒) is `pairVal_nonneg_of_maxCone` (`:993`).
  - (⇐) uses `lor_ehom` (`:930`): every effect has `Lor` coefficients.
  - This is a two-line kernel corollary.
- `[W]`: since `Lor = ℝ≥0 · hom(eball 3)`, this says `maxCone = SEP*` for the Euclidean pairing of `W 3`, where
  `SEP = cone{prodState x y}`. Under the dictionary (P1.3b, P1.4, P2.7: Euclidean = 4·HS), it is the block-positive
  cone, the HS-dual of the separable cone.
- Strictness: `SEP ⊊ Q3 ⊊ maxCone` (P2.6).

### Node 3c — the uniqueness theorem and its proof skeleton `[W]`, with exact instances

**Claim U.** Let `K ⊆ W 3`.
- **(U↑)** If `K ⊆ maxCone (eball 3)` and `K` is `G`-invariant, then `K ⊆ Q3`. No convexity or closedness is needed.
- **(U↓)** If `K` contains every `prodState x y` (x, y ∈ ball), is `G`-invariant, and is a convex cone (closed under
  `+` and `ℝ≥0`-scaling), then `Q3 ⊆ K`. No closedness is needed.
- Hence **every convex `G`-invariant candidate cone equals `Q3`**.

The proof uses **one** `cnot` and the Schmidt decomposition, and no Lie theory:

1. **Transitivity of G on pure states with one cnot.**
   - The Schmidt state `a|00⟩+b|11⟩` is `cnot (prodState (2ab, 0, a²−b²) z3)` (P5.1a–b, symbolic, `[X]+[M]`).
   - Every pure state is `(U_A⊗U_B)(a|00⟩+b|11⟩)` (`[L]` Schmidt). In W coordinates this reads
     `actC R_A (actT R_B (cnot (prodState x z3)))`. An exact rational instance is P5.1c.
   - Inverting the word (rotations are invertible in SO(3), and `cnot` is an involution) maps any pure state to
     `prodState z3 z3`.
2. **(U↑).** If `ω ∈ K \ Q3`:
   - Take `v` with `v^H ρ(ω) v < 0` (`[L]`), and a word `g ∈ G` sending `v` to `|00⟩` (step 1).
   - Then `prodEffVal (sharpEff z3) (sharpEff z3) (g ω) = v^H ρ v < 0`, so `g ω ∉ maxCone`, which contradicts
     invariance.
   - Exact instances:
     - `idW = cnot⁻¹(chainW)`: `cnot idW` has value −1/2 (P5.2a). This is the K2-GUARD chain.
     - A non-maximally-entangled instance: `α I − P_ψ` with `α = 16/25` (largest Schmidt coefficient squared) is in
       `maxCone` (block-positivity `[L]`; 20 exact instances, P5.2g) and not PSD (−9/25, P5.2c). The explicit word
       `actC R_y ∘ cnot ∘ actC R_Aᵀ ∘ actT R_Bᵀ` maps it to value −9/25 (P5.2e–f).
   - **Answer to "is any strictly larger G-invariant cone inside maxCone possible?": no.** No `G`-invariant
     *subset* of maxCone leaves `Q3`, and this needs no convexity.
3. **(U↓).** For `ω ∈ Q3`, `ρ(ω) = Σ_{i≤4} λ_i P_{v_i}` with `λ_i ≥ 0` (`[L]` spectral). Each `q(P_{v_i}) = g_i (prodState z3 z3)`
   by step 1. A convex cone containing the products and invariant under `G` contains this sum.
4. **The positive witness** (Node 1b) shows that `Q3` itself satisfies every hypothesis.

### Node 3d — where (i) universality, (ii) group closure, (iii) closedness and convexity enter (precise list)

| ingredient | witness `Q3` invariant | (U↑) nothing larger in maxCone | (U↓) nothing smaller | countercontrol showing it is load-bearing |
| --- | --- | --- | --- | --- |
| **(i) universality** (Lie closure = su(4), G = PU(4)) | not used; only `G ⊆ Ad U(4)` (P1.5b, P1.7e–f) | **not used**; only transitivity on pure states, from one `cnot` + Schmidt + local SU(2) | **not used**, same | it is consumed only if the theorem is restated as "invariant under PU(4)". P4 is identification and consistency evidence, not a premise of U |
| **continuous local group** (all of SO(3) on each copy, exactly) | — | used: the rotations `R_A`, `R_B`, `R_y` of step 1 are specific and in general irrational | used, same | finite native group: the interval `C_H ⊊ Q3 ⊊ M_H` (k2d T6) |
| **(ii) topological closure of the group** | — | not used with full SO(3). With a dense `D ⊆ SO(3)`: not used either (the set `{g : gω ∉ maxCone}` is open and nonempty, and `⟨cnot, D⟩` is dense in G) `[W]` | not used with full SO(3). With dense `D`: **replaceable by closedness of K** (Node 3e) | — |
| **(iii-a) convexity of K** | — | not used | **used** (spectral sums) | `K_nc := ℝ≥0·(G·products)` is G-invariant, candidate, `⊆ Q3`, and misses `(I − P00)/3`, whose spectrum {1/3,1/3,1/3,0} has exactly one zero, while every scaled product spectrum with a zero has two (P5.3a–c, `[L]` unitary orbits preserve spectra) |
| **(iii-b) closedness of K** | — | not used | not used with full SO(3); **used** with a countable dense `D` | `K_d` (Node 3e) |
| **cnot** | — | used (entangles) | used | without it the Lie algebra is 6-dimensional (P4.3), and `SEP` and `maxCone` are both local-invariant |

### Node 3e — a dense countable subgroup does not suffice without closedness `[W]+[L]`

Take `D` = the rotations `R(q)` with `q ∈ ℚ⁴ \ 0`. This is a countable group, dense in SO(3) `[L]`, and its W-matrices
are rational (P1.7e). Let `G_D := ⟨cnot, actT R, actC R : R ∈ D⟩` and
`K_d := convex cone generated by G_D · {prodState x y}`.

Properties of `K_d`:
- **Candidate:** `K_d ⊆ Q3 ⊆ maxCone`, because `G_D` preserves `Q3` (P2.4).
- **Invariance:** `K_d` is `G_D`-invariant.
- **`K_d ≠ Q3`:**
  - A pure state `ψ ∈ K_d` is an extreme ray of `Q3`, so every summand of a representation is proportional to `ψ`.
    So `ψ ∈ ℝ₊ · g·prodState x y` with `|x| = |y| = 1`, since `g ∈ Ad PU(4)` preserves rank.
  - The pure states in `K_d` therefore form a countable union of smooth images of `S²×S²` (dimension 4) in `CP³`
    (dimension 6). This set has measure zero `[L]`, so `K_d` misses almost every entangled pure state.
- **Closure:** the closure of `K_d` is `Q3`.

**With `K` closed and `D` dense, `K` is invariant under all of G** (linear maps are continuous), and U applies. So
cone pinning needs **either** exact continuous local actions **or** a closed body plus a dense local family. It does
**not** need the operation family to be closed, nor universality.

No explicit missing pure state is exhibited. A natural one-parameter attempt fails instructively: the Schmidt family
is mapped onto products by the single gate `cnot` (P5.1a). A generic (transcendence-degree-6) point would work but is
not computed.

### Lean sketches (UNCOMPILED)

```lean
def certW (ω : W 3) : Matrix (Fin 8) (Fin 8) ℝ := (1/4 : ℝ) • !![ … ]   -- the table in Node 1b, verbatim
def Q3 : Set (W 3) := {ω | ∀ v : Fin 8 → ℝ, 0 ≤ v ⬝ᵥ (certW ω *ᵥ v)}
def IsRot (R : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) : Prop :=
  (∀ x, ∑ i, R x i ^ 2 = ∑ i, x i ^ 2) ∧ LinearMap.det R = 1
def RotInvariant (K : Set (W 3)) : Prop :=
  (∀ ω ∈ K, cnot ω ∈ K) ∧ ∀ R, IsRot R → ∀ ω ∈ K, actT R ω ∈ K ∧ actC R ω ∈ K
def IsConvexCone (K : Set (W 3)) : Prop :=
  (∀ ω ∈ K, ∀ ω' ∈ K, ω + ω' ∈ K) ∧ ∀ c : ℝ, 0 ≤ c → ∀ ω ∈ K, c • ω ∈ K

-- Task 1 (positive witness)
theorem candidateCone_Q3 : CandidateCone Q3
theorem rotInvariant_Q3 : RotInvariant Q3
theorem transpose_mem_Q3 {ω} (h : ω ∈ Q3) : actC reflY (actT reflY ω) ∈ Q3
-- Task 3 (uniqueness, two directions stated separately, §A.34)
theorem subset_Q3_of_rotInvariant {K} (hK : K ⊆ maxCone (eball 3)) (hG : RotInvariant K) : K ⊆ Q3
theorem Q3_subset_of_rotInvariant {K} (hP : ∀ x ∈ eball 3, ∀ y ∈ eball 3, prodState x y ∈ K)
    (hc : IsConvexCone K) (hG : RotInvariant K) : Q3 ⊆ K
theorem eq_Q3 {K} (hK : CandidateCone K) (hc : IsConvexCone K) (hG : RotInvariant K) : K = Q3
-- dense variant
theorem eq_Q3_of_dense {K} (hK : CandidateCone K) (hc : IsConvexCone K) (hcl : IsClosed K)
    {D : Set ((Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ))} (hD : ∀ R, IsRot R → R ∈ closure D)
    (hDK : (∀ ω ∈ K, cnot ω ∈ K) ∧ ∀ R ∈ D, ∀ ω ∈ K, actT R ω ∈ K ∧ actC R ω ∈ K) : K = Q3
-- countercontrols
theorem exists_nonconvex : ∃ K, CandidateCone K ∧ RotInvariant K ∧ K ≠ Q3          -- K_nc
theorem exists_nonclosed_dense : ∃ D K, (countable D ∧ dense) ∧ CandidateCone K ∧ IsConvexCone K ∧ (D-invariant) ∧ K ≠ Q3
```

The statements are real. Expected kernel cost, ordered by difficulty:
1. **Cheap.** The `cnot` congruence (`certW (cnot ω) = Pᵀ certW ω P`, by `fin_cases`).
2. **Medium.** The rotation case needs a spin lift `R ↦ q` (Euler–Rodrigues inversion, with case splits and
   `Real.sqrt`), then the P2.4b congruence.
3. **High.** `subset_Q3…` and `Q3_subset…` need the spectral theorem and a 2×2 complex SVD (Schmidt). Mathlib has the
   former (`Matrix.IsHermitian.eigenvectorBasis`). Whether a usable SVD exists was not checked. Thread E P12 suggests
   the K3-side complex-matrix vocabulary as the natural home.

## 4. Task 4 — orientation characterization

For a convex cone `K` containing all products:

1. **`K ⊆ maxCone` and invariant under `cnot` + local SO(3)² ⇔ `K = Q3`.**
   - (⇐) by Node 1b `[M]`.
   - (⇒) by U `[W]`.
2. **Invariant under `cnot` + local SO(3)² + any one-copy reflection (either copy) ⇒ `K ⊄ maxCone`.** This follows
   from Node 2b/2c (`[X]`, kernel-cheap). The **Hilbert–Schmidt ball cone** `B3 := {ω | Σ_{(μν)≠(00)} ω_{μν}² ≤ 3 ω00², ω00 ≥ 0}`
   is such a cone:
   - it contains the products (P5.4a);
   - it is invariant under `cnot` (a signed permutation fixing (0,0), P5.4b) and under `actT`/`actC` of all of O(3)
     (P5.4c);
   - it is not in `maxCone`: `2e00 − prodState z3 z3 ∈ B3` has value −1/2 (P5.4d).
   - With the reflection the Lie algebra is so(15) (P4.4), and `B3` is the minimal closed invariant convex cone `[W]`.
   - This confirms thread E P11's Lorentz cones `L_c`.
3. **Simultaneous reflection of both copies** (`τ`, global transpose) is compatible: `Q3` is `τ`-invariant (P2.4d).
4. **The separable cone** is invariant under local O(3) (products go to products, P1.6c–d) and **not** under `cnot`
   (witness −2, P5.5, P2.6b). Likewise `maxCone` is local-O(3)-invariant and not `cnot`-invariant (k2d P3.b). So the
   local group alone selects nothing, and `cnot` is what makes orientation matter.
5. **The branch is fixed by the gate, not by the local group.** `reflY SO(3) reflY = SO(3)` (P3.8d). Three gates
   satisfy DIM-1's frame, `relT` and `relC` exactly:
   - `cnot'` (P3.8a–c). For `cnot'` + SO(3)², the unique convex invariant candidate is `actT reflY '' Q3 = PT_B(Q3)`,
     by conjugating U. `Q3` itself is not `cnot'`-invariant (`cnot' p0 = idW`).
   - `T_refl := actT reflY ∘ cnot` (P3.7a–c, with positivity from P3.7d). **No** candidate cone is invariant under
     `T_refl` alone (`T_refl² p0` has value −1/2, P3.7e).
   - So DIM-1's `NativeGate` admits gates whose invariant candidate cone does not exist. This is thread E P9's "odd
     class", here as a kernel-cheap two-step chain.
6. **Beyond reversible maps, the operative invariant is complete positivity, not the determinant.**
   - For the contracted reflection `c·reflY` (a ball map; `det = −c³ < 0`), the landed chain gives exactly
     `(1−3c)/4` (P3.6a). Its zero is the CP threshold of the corresponding qubit map: the Choi spectrum is
     {(1+c)/4 ×3, (1−3c)/4} (P3.6b, `[M]`).
   - For every `D = diag(d1,d2,d3)`, the chain with `D∘F`, where `F` ranges over `id` and the three π-rotations (`nflip`
     is one), returns **exactly the four Choi eigenvalues** (P5.6a, P3.6c).
   - Consequence:
     - (kernel-only, `[X]`) no candidate cone is invariant under `cnot`, the π-rotations and `actT D` when the unital
       Pauli-diagonal map `D` is not CP;
     - (`[M]+[L]` Choi) `Q3` is invariant when `D` is CP.
   - So orientation-reversing **contractions** can be liftable (`c·reflY`, `0 ≤ c ≤ 1/3`). "Orientation-preserving"
     (k2d A5) is exactly the reversible restriction of complete positivity: for orthogonal `D`, CP ⇔ `det D = +1`.

## 5. Task 5 — the evidence layers, and the circularity audit

| statement | `[K]` | `[X]` | `[M]` | `[W]` | `[L]` |
| --- | --- | --- | --- | --- | --- |
| landed obstruction (reflY on copy B) | K2Guard `:143` | P3.3 replay | — | — | — |
| control-copy obstruction | ingredients | P3.4, P2.5e | — | — | — |
| corollary for every S ∈ O(3)∖SO(3) (one rotation suffices) | ingredients | P3.1, P3.2 | — | — | — |
| `T_refl`: native gate with no invariant candidate | — | P3.7 | — | positivity via P3.7d | — |
| CP face tests (chain = Choi eigenvalue) | — | chain values P3.6a/c, P5.6a | Choi spectra | — | the CP tetrahedron (Fujiwara–Algoet / Ruskai–Szarek–Werner) |
| `maxCone = SEP*` | `:993`, `:930` | — | P1.3b, P1.4 (block-positive reading) | scaling step | — |
| `cnot`, `actT/actC R` = Pauli images of CNOT, local SU(2) | — | literal-definition checks | P1.5b, P1.7e–f | — | SU(2)→SO(3) onto |
| `Q3` candidate and invariant | — | congruence identities P2.4 (statement real) | P2.1–P2.3 | — | Kronecker of PSD, `Tr(PQ) ≥ 0` |
| Lie dimensions 6 / 15 / 105 | — | P4 (lower = upper) | identification with su(4) (P4.1a) | — | analytic-subgroup theorem (G = PU(4)) |
| uniqueness U (both directions) | — | one-cnot Schmidt identity P5.1a | instances P5.1c, P5.2 | assembly | Schmidt, spectral theorem |
| convexity load-bearing | — | — | P5.3 | — | orbits preserve spectra |
| closedness load-bearing (dense case) | — | — | — | Node 3e | measure zero, density of rational quaternions |
| `B3` invariant under cnot + O(3)², not a candidate | — | P5.4 | — | minimality | — |

**Circularity audit (proving K2 by assuming K2).**
- **(a) U is a reduction, not a derivation.** Its hypothesis "K invariant under `actT R` and `actC R` for every
  R ∈ SO(3), and under `cnot`" *is* the composite-level local-reversibility premise (k2d A1 + A6 + LocalExt), which
  is K2's open content. U shows that this premise plus convexity *pins* the cone. It does not source the premise.
- **(b) `Q3` must not be read as "the composite cone because QM says so".** It is used only as a consistency control
  (Node 1b) and as the name of the conclusion. In the kernel `Q3` should be the real predicate `certW`. "`Q3` is the
  image of the PSD cone" belongs to `[M]`.
- **(c) The complex structure is not assumed in U's hypotheses** (`cnot`, `actT`, `actC` are real kernel maps). It
  enters in two places:
  - through `cnot`'s sign table: `cnot` vs `cnot'` selects `Q3` vs `PT_B(Q3)`, Node 4.5;
  - through the proof steps Schmidt and spectral, which are proved over ℂ.
  A kernel proof routed through `Matrix … ℂ` would import the dictionary as a proof device. That is legitimate for a
  statement about the real set `Q3`, provided the dictionary is a theorem (P1-type identities), not a definition of
  the composite.
- **(d) No step here uses LT beyond the carrier `W 3` itself.** k2d D1 records that `W 3` encodes LT plus product data;
  everything here inherits that premise.

## 6. Task 6 — gem-finding: hidden assumptions of the cone-pinning route (depth-first)

Productivity test, fixed before classifying (AGENTS §A.31): a finding is a gem iff it is strictly stronger than
restating thread E / k2d (P9–P12, T5–T7, A5) and it either constrains an obligation or exposes a hidden assumption.

| # | node and check | finding | class |
| --- | --- | --- | --- |
| G1 | Node 4.6; P3.6a–c, P5.6a | **The landed chain is a Choi-eigenvalue test.** For `actT (c·reflY)` it gives `(1−3c)/4`, whose threshold equals the CP threshold `c = 1/3`. With the π-rotations (`nflip` among them) the four chains give all four Choi eigenvalues of every Pauli-diagonal one-copy map. Hidden assumption exposed: k2d's A5 ("the liftable family must be orientation-preserving, `det = 1`") is right only for reversible maps. Orientation-reversing contractions `c·reflY` with `c ≤ 1/3` admit `Q3`. If K∞-Act or K3 ever lifts irreversible local operations, the criterion is the CP faces, not the determinant. **Assumption-watch AW-K2C-1.** Pressure test: the CP tetrahedron itself is `[L]`. The positive direction (CP ⇒ liftable) is matrix-model only. New here: the kernel chain realises each face exactly, so the negative direction is kernel-cheap. | **NEW** (scoped; mathematically the known unital-qubit CP characterisation) |
| G2 | Node 3c–3d; P5.1–P5.3 | **Uniqueness needs neither universality nor group closure nor a closed cone.** With exact local SO(3)², one `cnot` plus Schmidt gives exact transitivity on pure states. (U↑) needs no convexity or closedness; (U↓) needs convexity only. Thread E P12 assumed LG + a closed convex cone and routed through P10 (Lie closure). Here those are shown not load-bearing, with countercontrols for convexity (`K_nc`) and for closedness in the countable case (`K_d`). | ELABORATING (sharpened hypothesis list for P12 / k2d T7; lowers the kernel cost from Lie theory to spectral + 2×2 SVD) |
| G3 | Node 3e | **The closure requirement can live on the body instead of on the operations.** With a countable local family (all that the passive collapse supplies, SA §5 item 3), the cone is pinned iff the body is closed, given density of the family in SO(3), which is a topological property of the family and not an adoption of limit operations. `K_d` shows that without closedness it is not pinned. COMP-1's `PreComposite` has a `convex` field and **no closedness field** (`CompositeInterface.lean:226`). The single-system completion body is closed by definition (`StageCompletion.lean:141`), but no joint tower exists. This answers the cone part of SA question K2-c. **Assumption-watch AW-K2C-2:** "closed composite body" is an unlisted premise of every dense-family route to the cone. Pressure test: the topological step (closed + dense ⇒ invariance under the closure) is elementary. The content is the trade-off and the non-closed countermodel, which is written, not exhibited explicitly. | **BORDERLINE** (programme-relevant relocation; elementary mathematics; countermodel `[W]`) |
| G4 | Node 4.5; P3.7, P3.8 | The cone branch (`Q3` / `PT_B Q3`) is fixed by the native gate's sign table, not by the orientation of the local group (`reflY SO(3) reflY = SO(3)`). DIM-1's `NativeGate` admits `T_refl`, which has no invariant candidate cone (kernel-cheap two-step chain). | CONFIRMING (thread E P9 cone bit / odd classes), with a new kernel-cheap form |
| G5 | Node 2b, 2c | The reflection corollary needs **one** rotation (`reflY Sᵀ`), not all of SO(3). The landed obstruction holds verbatim on the control copy (`actC reflY phiW = idW`). | ELABORATING |
| G6 | Node 2d | The simultaneous both-copy reflection (global transpose) is compatible; the obstruction is a statement about *one-copy* reflections only. The local symmetry group of `Q3` is `{(A,B) ∈ O(3)² : det A = det B}`. | CONFIRMING (thread E antiunitary survivors) |
| G7 | Node 3a; P4 | G's closure is PU(4) (dimension 15), not SO(15). With any one-copy reflection or with `T_refl` it becomes so(15), and the minimal invariant closed convex cone is `B3`, outside `maxCone`. | CONFIRMING (thread E P10, P11), independent code in kernel coordinates |
| G8 | Node 3b | `maxCone = SEP*` for W's Euclidean pairing is a two-line kernel corollary (`:993` + `:930`). It is the block-positive cone under the dictionary. | POSITIVE |
| G9 | Node 1b | The positive witness can be stated without ℂ (`certW`), and its `cnot` invariance is a permutation congruence (kernel-cheap). The rotation invariance needs a spin lift. | POSITIVE |
| G10 | Node 5(a), §5 | **Operational availability of local SO(3) is the open premise.** The kernel's only boundary-transitive witness uses reflections (k2d H3; `boundaryTransitive_fullAut`, `EffectSpace.lean:337`). By G6, reflections must be excluded on one copy. By G3, a countable family suffices only with a closed body. Nothing here sources the lift. | CONFIRMING |
| G11 | — | **Inverse closure.** U uses inverses: `R⁻¹` for un-Schmidting, and `cnot` as an involution. A lifted *semigroup* (forward powers of one irrational rotation) has a group closure (compactness `[L]`), but no exact transitivity, so it falls back to G3's closed-body route. | ELABORATING (minor) |

## 7. Verdict (§A.31)

- **Task 1:** POSITIVE.
  - `Q3`, stated as the real predicate `certW ω ⪰ 0`, is a candidate cone invariant under `cnot` and under `actT R`,
    `actC R` for every R ∈ SO(3), and under the global transpose.
  - The congruence identities are exact (P2). The containments rest on `[M]+[L]`.
  - `cnot` is exactly `Ad(CNOT)` and `actT/actC R(q)` are exactly `Ad(local SU(2))` (P1, cross-checked against k2d).
- **Task 2:** the corollary holds by exact algebra (P3.1–P3.2), from the landed theorem.
  - Only one rotation is needed.
  - The control-copy version is kernel-cheap.
  - Simultaneous reflection of both copies is compatible.
- **Task 3:**
  - The closure of G is PU(4) (dimension 15, not SO(15)).
  - Every convex G-invariant candidate cone equals `Q3`. No G-invariant subset of maxCone is larger. The minimal
    invariant convex cone is `conv(G·products) = Q3`, with no closure needed.
  - Neither universality nor group closure is consumed. Convexity is consumed by the lower bound only. Closedness is
    consumed only with a countable dense family, where it is load-bearing.
  - The argument is written. Its ingredients are exact (P4, P5).
- **Task 4:**
  - With `cnot` fixed, `Q3` is the only convex candidate for local SO(3)².
  - Adding any one-copy reflection leaves none; `B3` is invariant but not a candidate.
  - Separable cones are local-O(3)-invariant and not `cnot`-invariant.
  - The branch is set by the gate.
  - For contractions the criterion is CP, which the landed chain tests face by face.
- **Fixed point:** not reached. This pass produced one NEW (G1) and one BORDERLINE (G3). The next pass should start
  from:
  - G1: state the face theorem for all unital ball maps, reducing to diagonal form by signed SVD with SO(3) factors,
    and check whether a non-unital (affine) one-copy map can be expressed with `homMap` at all. It cannot as defined,
    since `homMap` fixes the unit coordinate, which is itself a scope limit to record.
  - G3: try to exhibit an explicit pure state outside `K_d`, or a closedness-free alternative.
- **Correctness/consistency (§A.23):** consistency-axis work only. Bands unchanged. Nothing is adopted or propagated.

## Probe log

All scripts and outputs are in `scratchpad/k2c/`. Arithmetic is exact: sympy rationals, Gaussian rationals and
symbolic identities, plus GF(p) ranks used only as lower bounds. No float is evidence. Kernel tables and maps are
parsed from the base files.

Command form, from `scratchpad/k2c/`, with `W=../wt-68b/verification/lean-mathlib/OIBridge`:
`python3 -I <probe>.py $W/CompositeDimension.lean $W/K2Guard.lean` (P1 takes `../k2d` as a third argument). Each probe
was run, then rerun into `replay/`. `cmp` reported every output **byte-identical**.

| probe | script md5 | output md5 | result | runtime |
| --- | --- | --- | --- | --- |
| shared helpers `k2clib.py` | `939469d7…` | — | — | — |
| P1 dictionary | `b038000d…` | `f7e0aa70…` | 30 checks, 0 failures; VERDICT DICTIONARY-EXACT | ~6 s |
| P2 PSD cone | `97771b67…` | `3f302686…` | 20 checks, 0 failures; VERDICT POSITIVE-WITNESS-EXACT | ~73 s |
| P3 reflection | `e485eb0e…` | `290db25a…` | 28 checks, 0 failures; VERDICT COROLLARY-ALGEBRA-EXACT | ~4 s |
| P4 group / Lie | `7cc845ef…` | `85374ae5…` | 16 checks, 0 failures; VERDICT LIE-DIMENSIONS-RENDERED | ~4 s |
| P5 uniqueness | `d4c645e5…` | `fef8c3aa…` | 20 checks, 0 failures; VERDICT UNIQUENESS-INGREDIENTS-EXACT | ~5 s |

Run history, recorded rather than kept as files:
- **P1 run 0** crashed at check 1.7d with a Python `TypeError` (`sum` of sympy matrices without a start value). This
  was a script defect, not a result: 20 checks had passed and no verdict was rendered. The start value was fixed and
  nothing else changed.
- **P5:** after the first full run (20/20), a dead duplicate assignment in §5.2 (overwritten on the next line) was
  removed. P5 was rerun and then replayed. The recorded md5s are for the edited script.
- **No draft expectation was refuted in this pass.** The CP-threshold expectation behind G1 (chain value linear in
  `c` and vanishing at `c = 1/3`; Choi eigenvalue `(1−3c)/4`) was worked out by hand before P3 was written. P3.6a–b
  test it, and P3.6c was written alongside them.
- **P5.6a** (all four faces via the π-rotations) was added after reading P3.6c's output. It was derived by hand from
  that output and then checked exactly.
- **Note:** P3.6 was not preregistered in a frozen file. This ledger's decision rules are script docstrings written
  before each first run.

Written steps that the exact checks do not cover (marked `[W]`/`[L]` where used):
- the PSD transfers: realify, Kronecker, `Tr(PQ)`;
- Euler–Rodrigues surjectivity;
- the Schmidt and spectral steps of U;
- block-positivity of `α I − P_ψ` (instances only);
- the analytic-subgroup identification `G = PU(4)`;
- the density and measure-zero argument for `K_d`;
- minimality of `B3`;
- the Choi/CP equivalence.
