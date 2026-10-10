# NOTES-B1 — the hidden-level composite

Node B1 of `research/bridge` (charter `README.md`). Base L = `9f9f8257`; checkpoint `1c6852c3`. Evidence levels
[K] certified at L (file:line, paths under `verification/lean-mathlib/OIBridge/`; CD = CompositeDimension.lean),
[W] written argument given here, [X] exact computation (`experiments/b1_hidden.py`, check id), [A] audited archive
record. Exact arithmetic only; `Q3` and the dictionary `M(ω) = Σ ω_μν σ_μ⊗σ_ν` appear only as comparison tools (check
H2d), never as premises.

**Productivity test (§A.31), fixed before the first computation.** The node is a gem iff it yields a fact strictly
stronger than "the hidden level needs a composite premise" and that fact either constrains the composite route or
exposes a hidden assumption. Otherwise it is recorded as coherence relabelling.

## 1. The hidden pair model

A **hidden pair model** consists of the following data.

- `Λ` is a finite set, the pair's hidden configuration space.
- `𝒫 ⊆ Δ(Λ)` is convex: the hidden distributions the pair can be in, prepared or reached by available interventions.
- `R : ℝ^Λ → W 3` is linear: the pair readout. For each `μ ∈ 𝒫`, `pairVal (ehom e) (ehom f) (Rμ)` is the realized
  probability of the product effect `(e, f)` (CD:164, :182), so `R(𝒫)` consists of joint states.
- `K_H := cone R(𝒫)` is the **hidden composite cone**. It is always a well-defined convex cone in `W 3`. It lies in
  `maxCone (eball 3)` whenever the realized statistics are valid probabilities.
- A token operation `O`, a linear map of the ball, is realized in the pair context by a hidden bijection `Π` of `Λ`.

**Locality of registers (L-REG).** The model is L-REG when four conditions hold:
1. `Λ = Λ_A × Λ_B`;
2. the readout is local, `R = R_A ⊗ R_B`, i.e. the response to a product effect is the product of local response
   functions on the local registers;
3. a token operation acts on its own register only, `Π = π × id`;
4. preparations are measurement-independent: `𝒫` does not depend on the effects measured later.

## 2. Theorem B1.1 — when (b_H) is a theorem

**Hypotheses.**
- **(W) RESPECT.** For `μ, ν ∈ 𝒫`, `Rμ = Rν` implies `R Π_*μ = R Π_*ν`.
- **(A) Availability in context.** `Π_*(𝒫) ⊆ 𝒫`.
- **(P) Product behaviour.** If `μ ∈ 𝒫` and `Rμ = prodState x y`, then `R Π_*μ = prodState (O x) y`.
- `R(𝒫)` contains `prodState x y` for every `x, y` in the ball (H1 of the pair).

**Conclusion.** `actC O (K_H) ⊆ K_H`. The same holds for the target with `actT`.

**Proof [W].**
1. By (W), `L(Rμ) := R Π_*μ` is a well-defined map on `R(𝒫)`.
2. `L` is affine on the convex set `R(𝒫)`. Pushforward is linear on measures and `R` is linear, so for `μ, ν ∈ 𝒫`,
   `L(p Rμ + (1−p) Rν) = R Π_*(pμ + (1−p)ν) = p L(Rμ) + (1−p) L(Rν)`.
3. By (P), `L` agrees with `actC O` on the product states. These affinely span the normalized slice `{ω₀₀ = 1}` of
   `W 3` (local tomography on the carrier; [X H3]: already the 36 octahedral products have rank 16). An affine map on
   a convex set is determined by its values on an affinely spanning subset, so `L = actC O` on `R(𝒫)`.
4. By (A), `actC O (R(𝒫)) = R(Π_*(𝒫)) ⊆ R(𝒫)`. Pass to cones by homogeneity. ∎

**Under L-REG, (W) and (P) follow from RESPECT of `π` for the token alone [W].**
`(R_A ⊗ R_B)(P_π ⊗ I) = (R_A P_π) ⊗ R_B = (Hom N_π · R_A) ⊗ R_B = actC N_π ∘ (R_A ⊗ R_B)`.

**Exact instance [X H1].** Take the octahedral ontic token `Λ_A = {±e_x, ±e_y, ±e_z}` with `R_A δ_a = hom v_a`.
- 48 of the 720 permutations respect `ker R_A`. They induce a closed group of 48 signed permutation matrices,
  containing `nflip`, `rot3 π`, `S = R_z(π/2)` and `cyc3` (H1a).
- For all 48, `R (P_π ⊗ I) = actC(N_π) R` and `R (I ⊗ P_π) = actT(N_π) R` hold as 16 × 36 matrices (H1b).
- Countercontrol CC1: the transposition `+x ↔ +y` does not respect `ker R_A`.

(A) holds under L-REG if every hidden distribution is available, or if the agent's local interventions can be applied
in every context. So under L-REG, (b_H) is a theorem for every token operation realized by a readout-respecting
local permutation.

## 3. Theorem B1.2 — L-REG hosts no candidate pair (the obstruction)

**(i) Bell.** Assume L-REG with measurement-independent preparations and local response functions for the four sharp
effects of a CHSH test.
- Every realized pair state then has `|S| ≤ 2`: the 16 deterministic local strategies give `max S = 2`,
  `min S = −2` (H2b), and every Bell-local model is a mixture of them [W].
- `phiW = cnot (prodState xplus z3)` holds at L (CD:1222). So `phiW` lies in every candidate cone: H1 puts the products
  in `K`, and H2 makes `K` invariant under `cnot` [W].
- With the exact unit settings `a0 = e_x`, `a1 = e_z`, `b0 = (4/5, 0, 3/5)`, `b1 = (4/5, 0, −3/5)`, `phiW` has valid
  statistics and `S = 14/5 > 2` (H2a).
- Each Bell-type defect `z_s` of K(Z_F) likewise reaches `S = 14/5`, with valid statistics (H2c).
- `phiW ∈ K(Z_F)`: its pairings with the defects are `0, 1/2, 0, 1/2`, and `M(phiW)` is PSD as a comparison (H2d).

Hence no L-REG realization reproduces the CHSH experiment on `phiW`. **L-REG excludes every candidate cone, `Q3`
included.**

Controls:
- CC2: a product state stays inside the bound (`S = 0`).
- CC3: the PR table reaches `S = 4`, so the bound is not vacuous.

**(ii) No gate.** Suppose in addition that every hidden distribution is available (`𝒫 = Δ(Λ)`) and that the local
readouts are valid, i.e. ontic points lie in the ball.
- `K_H` is generated by the products `R δ_(a,b)`.
- `K_H` lies in the half-space `⟨w, ·⟩ ≥ 0`, with `w = E00 − E11 + E22 − E33`. [W]: on products,
  `⟨w, prodState x y⟩ = 1 − x·Dy ≥ 1 − |x||y| ≥ 0` with `D = diag(1, −1, 1)`. [X H1c]: the 36 octahedral values have
  minimum 0.
- `⟨w, phiW⟩ = −2` (H1c).
- Every hidden permutation of `Λ` permutes the point masses, so it preserves `K_H`. `cnot` does not preserve it,
  because it maps `prodState xplus z3 = R δ_(+x,+z)` to `phiW`.

So the native gate is realized by no hidden permutation.

**Reading.** L-REG makes (b_H) a theorem exactly where the native gate cannot act on the hidden state, or where the
gate's output cannot be Bell-tested with sharp effects. This holds for every candidate pair, not only for the exotic
ones.

## 4. The framework's own Bell branch, and what remains of (b_H)

The hypotheses of B1.2(i) are the hypotheses (i)–(iv) of the framework's Bell-ceiling theorem: determinism; setting
interventions supported in their regions; readout before the cones meet; one common pre-setting ensemble
(Main.md:360–370, with the pointwise graph cone of Main.md:358). Its conclusion is `|S_CHSH| ≤ 2` (Main.md:371). The framework adopts **branch (a), ontic parameter
dependence** (Main.md:392): at the microstate level, one wing's response depends on the remote setting, through
preparation-indexed long edges. It records branch (b), measurement dependence, without adopting it (Main.md:396). So
**the framework itself gives up L-REG** for Bell-prepared pairs.

In branch (a):
- (P) and (W) can still hold operationally. No-signalling is an identity of the carrier for `actC` (CD:112–113,
  :201–202), and local tomography is the premise field `lt` of `Composite` (CompositeInterface.lean:245), encoded by the
  carrier `W 3` (CD:96).
- By Theorem B1.1, (b_H) then reduces exactly to **(A), availability in context**: the token's intervention, applied
  with the other token present, leaves the pair in a hidden distribution the pair can be in.
- At level H, (A) is "an available operation remains available when an untouched system is adjoined". That is the
  spectator clause of OI⁺-1 (GR.md:228) read at the hidden level.

## 5. Is the assumption an existing named hypothesis?

- **GR.md:326**: "The tensor product structure follows from the spatial product structure of the classical
  configuration space `C_V = C_1 × ⋯ × C_N`".
  - As a carrier statement at level M it is correct: the Hilbert space over a product set is the tensor product.
  - Read as a statement about the operational composite reached by local interventions on measurement-independent
    preparations, it is L-REG, and B1.2 shows that its pair statistics are Bell-local.
  - The manuscript's own §3.3 says the same in its Bell-ceiling theorem.
  - **Assumption-watch marker**: the product configuration space does not yield the entangled composite. The
    entangled sector needs the branch-(a) nonlocal response. Recorded, not applied: manuscript hold.
- **H-local-lift** (GR.md:328) concerns the locality of the selected continuous observer generator. It mentions
  neither registers nor a pair cone, so it is not L-REG.
- **H-observer-bundle** (SM.md:791, inside one long paragraph: "the trace-out produces a local observer-state bundle
  with nonzero projective curvature in the hypercharge channel"; also cited at SM.md:683 and :1294) belongs to the
  gauge sector, not to L-REG.
- **Conclusion.** L-REG is not a named hypothesis of the composite route. Its content is the hypothesis set of
  Main.md's Bell ceiling, whose conclusion the framework avoids by adopting branch (a).

## 6. Disguise test and the K(Z_F) test

| principle | restates (b) / I3.150–153 / I3.165 / OI⁺-1 spectator? | transcription vs K(Z_F) | verdict |
|---|---|---|---|
| L-REG (product registers, local readout, `π × id`, measurement independence) | no: it is stated on configurations and maps | satisfiable by **no** candidate cone (B1.2), so it cannot discriminate `K(Z_F)` from `Q3` | not a bridge (excludes the target) |
| (A) in branch (a), for the drive and one off-frame partner | **yes**: it is the H-level spectator clause of OI⁺-1 | excludes `K(Z_F)` (B4: exact witnesses) | fails the disguise test |

## 7. Verdict of B1

- **FAILED route, exact obstruction.** The charter's expected route ("a locality-of-registers assumption does the
  work") does do the work for (b_H) (B1.1 with L-REG). But its hypotheses are those of the framework's Bell ceiling,
  and every candidate cone contains `phiW` with `S = 14/5 > 2`. So it excludes `Q3` together with `K(Z_F)`
  ([W] + [X] H2a–H2d, H1c; [K] CD:1222).
- **Exact content of (b_H) in the adopted branch.** (b_H) for `O` is equivalent to availability in context (A), given
  (W), (P) and LT. That is CONDITIONAL on (A), the H-level OI⁺-1 spectator clause. Status: assumed, a do-not-assume
  item when transcribed to the pair (I3.165's clause).
- **Gem classification.** **NEW**: the locality-of-registers route is self-defeating at level H. The assumption that
  would make the composite action a theorem is the one the framework's own Bell analysis rejects, and it rejects the
  quantum composite too. The fact is strictly stronger than "a premise is needed", and it exposes an assumption at
  GR.md:326. It applies to every H→P route that would derive (b) from product registers: assumption-watch marker.
- **What is not claimed.** No statement about measurement-dependent models (branch (b), not adopted). No claim that
  (A) is false; it is unsourced. The Bell bound for stochastic local models is the standard mixture argument, [W].
