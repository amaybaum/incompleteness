# NOTES-E4 — K2's clauses after stages 3–6, and the theorem schema conditional on A_miss

Base L = `9f9f8257`. Sources: ROADMAP K2 (:1001–1006); the pair-cone research stages 3–6 at L
(`research/archive/pt/INTEGRATION-NOTE-STAGE3.md` … `-STAGE6.md`, audited there; cited [A]); k2d/K2-LEDGER, k2c/K2C-LEDGER
[A]; the kernel at L [K]. No new probe was run for this node: every cell below is a citation at its own evidence level,
re-read against the kernel anchors; the schema in §3 is a statement, not a proof.

## 1. The pair-level hypotheses, at their status at L

| name | content (on `K ⊆ W 3`) | status at L |
| --- | --- | --- |
| H1 | `∀ x y ∈ eball 3, prodState x y ∈ K` | the lower bound of every COMP-1 pre-composite body (`minBody_subset` CompositeInterface.lean:461 [K]) — given that the pair is a COMP-1 composite, which is K2(a)'s premise |
| upper bound | `K ⊆ maxCone (eball 3)` | `subset_maxBody` :467 [K], same proviso; `CandidateCone` K2Guard.lean:95 bundles H1 with it |
| H2 | `∀ ω ∈ K, cnot ω ∈ K` | unsourced: gate preservation needs a pair-level operation datum (P-ACT2), which restates it (KT4-PREM-1 Q2, receipt at L [K-record]); `cnot` meets DIM-1's hypotheses (`nativeGate_cnot` CompositeDimension.lean:1160 [K]) |
| H3 | `K = dualW K` (Euclidean self-duality of the table pairing) | an added premise, not in the kernel; stage 3 tested it as a candidate source and found it insufficient [A] |
| (b) / A_miss | the native single-token reversible operations, idle-extended to one token, preserve `K`; minimal native form: `∀ t, ∀ ω ∈ K, actτ R_z(t) ω ∈ K ∧ actτ R_x(t) ω ∈ K` for one token `τ` (ball3Drive's flow `rot3`, KInfFoundations.lean:411/450, and its `J = cyc3`-conjugate) | INDEPENDENT of every item at L that reaches the pair cone (stage 6 [A]: K(Z_F) satisfies all of them; 13 FAILS rows, each a hypothesis) |

## 2. K2's clauses after stages 3–6

| clause (ROADMAP :1003–1005) | status after stages 3–6 | evidence | what remains |
| --- | --- | --- | --- |
| (a) local tomography / product-test structure | unchanged: a premise encoded by the carrier `W 3` (`W` CompositeDimension.lean:97, "Local tomography is the premise this carrier encodes"); the K1 step consumes only product-test compatibility of the gate (PTQ), LT proper only the K3 dictionary | k2d D1–D3 [A]; real-QT countercontrol [A] | a source: LT is "test locality of a joint tower", and no joint tower exists at L (k2d D6 [A]; KT4-PREM-1 Q2: no `DirectedStages` built from two systems) |
| (b) the composite cone | **settled negatively at the pair level**: H1 + H2 (even at level (ii), the order-16 native class) + H3 do not force `K = Q3` — exact cones K(E0), K(Z_F) | stage 3 [A] (Q-SD EXOTIC), stage 6 R6 (K(Z_F) against the 199 applicable items) [A] | a selecting premise; the candidates that pass the disguise test (λ, pair homogeneity H, extreme-ray transitivity T) are not items at L |
| (c) local actions compatible with the cone | **is (b) itself**: no theorem at L concludes a pair cone's invariance under a single-token action (39 theorems mention `actC`/`actT`; the only cone-binding one forbids an operation: `no_candidateCone_cnot_reflY` K2Guard.lean:143 [K]); every principle at L that yields (b) contains it as a spectator clause | stage 5 (α–η, κ, λ) and stage 6 D1–D4 [A] | the spectator clause for the drive and one off-frame partner (A_miss), unsourced; field-neutrally it needs both the operations' availability (K∞-Act/Drive) and their idle extension to the pair (a pair-level `OpDatum`, P-ACT2) |
| (d) the composition theorem | at the pair level **CONDITIONAL on A_miss** (§3); beyond the pair OPEN: three-token parity needs IE₂ or KT∞ (EQ2 §2(b), §3 [A]); four-token coherence λ gives IE₁ in a design run (KT4-PREM-1 [K-record], E5) | stage 4 Y2 [A]; EQ2 [A] | IE₂ (or KT∞) and a three-token structure, absent at L |
| (e) antiunitary / complete-positivity bridge | reversible pair part **settled by the kernel**: no candidate cone is invariant under `cnot` and a one-copy reflection (`no_candidateCone_cnot_reflY` [K]); the twin `PT_B(Q3)` vs `Q3` is a per-token chart convention at two copies (EQ2 §2(b) [A]); the transposed gate class is excluded only at three copies under IE₂ + H0 (EQ2 [A]); for irreversible one-copy maps the operative condition is the CP faces, tested face by face by the landed chain (k2c G1 [A]) | [K] + [A] | the three-copy exclusion (IE₂), a kernel statement of the CP-face chain |
| (f) relation to the K3 machinery | the two-copy dictionary `W 3 ≅ Herm(ℂ² ⊗ ℂ²)` is exact on the DIM-1 objects (k2c P1 [A]); no formal map at L from the matrix, hidden-history or general levels to the pair carrier (NO-MEET, stage 6 §1 [A]); E3: K3's `ContextStable` plays the role of the spectator clause at the matrix level, and the qubit-power carriers K2 reaches suffice for drivability (Kₙ-DESC, CONJECTURE) | [A] + E3 | a k-token dictionary, and a formal map between `ContextStable` and (b) — none exists at L, and none is asserted here |

So, at the pair level, **two clauses are settled** — (b) negatively (the cone is not forced by H1–H3) and (e) in its
reversible part (one-copy reflections excluded) — **(c) is identified with the single missing assumption** (b), and
(a), (d) beyond the pair, (e)'s three-copy part and (f) **remain**.

## 3. The theorem schema conditional on A_miss (pair level)

**Statement (proposal; Lean-style, in kernel vocabulary plus the ℂ-free predicate `Q3 := {ω | certW ω ⪰ 0}` of
k2c Node 1b [A]):**

```lean
theorem pairCone_eq_Q3_of_drive {K : Set (W 3)}
    (hH1 : ∀ x ∈ eball 3, ∀ y ∈ eball 3, prodState x y ∈ K)          -- products
    (hH2 : ∀ ω ∈ K, cnot ω ∈ K)                                        -- gate preservation
    (hH3 : K = dualW K)                                                -- self-duality (closedness follows)
    (hA : (∀ t : ℝ, ∀ ω ∈ K, actT (rotZ t) ω ∈ K ∧ actT (rotX t) ω ∈ K) ∨
          (∀ t : ℝ, ∀ ω ∈ K, actC (rotZ t) ω ∈ K ∧ actC (rotX t) ω ∈ K)) : -- A_miss on one token
    K = Q3
-- rotZ t: the linear part of ball3Drive's flow `rot3 t`; rotX t: its conjugate by `cyc3`.
-- corollaries under the same hypotheses: K is invariant under actT R and actC R for every R ∈ SO(3) (IE₁, (b) for
-- every local rotation), and its image under the dictionary is the two-qubit PSD cone.
```

**Status.** CONDITIONAL on H2, H3 and A_miss, each unsourced at L (H1 and the `maxCone` bound are kernel bounds for a
COMP-1 body). Proof: stage 4's Y2 [A] — written, with exact ingredients, audited twice, not kernel-checked; its group
step uses only the connected subgroup `{U ⊗ P₊ + V ⊗ P₋}` that one token's rotations generate with `cnot`, and H3 is
used because that subgroup is not transitive on pure states. A kernel proof needs `Q3` as a real predicate (`certW`, k2c
[A]) and a spectral argument (Mathlib `Matrix.IsHermitian.eigenvectorBasis`; k2c Node 3 lists the costs).

**Controls the schema must keep** (each cited, none re-run here):
- positive: `Q3` itself meets H1–H3 and A_miss on both tokens (k2c P2, P2.7 [A]);
- without A_miss: K(Z_F) meets H1–H3 and leaves under every one-parameter rotation subgroup of either token,
  `ipW(R_n(t) z_s, R_n(π/2) p_s) = −sin(t)/8` (stage 6 §3 [A]);
- without H2: the twin `PT_B(Q3)` meets H1, H3 and local-rotation invariance; it fails H2 at `idW = actT reflY phiW`
  (`actT_reflY_phiW` K2Guard.lean:106 [K]), since `cnot idW = chainW` (`cnot_idW` :110 [K]) takes `−1/2` on a product of
  sharp effects (`chain_value` :134 [K]), so `chainW ∉ maxCone ⊇ PT_B(Q3)` (the inclusion: `Q3 ⊆ maxCone` [A] and `maxCone` is preserved by `actT reflY`, a ball automorphism — `EqvSeams.actT_mem_maxCone` [D]);
- without H3: the Hilbert–Schmidt ball cone `B3` meets H1, H2 and local O(3) invariance on both tokens and is neither
  self-dual nor inside `maxCone` (k2c P5.4 [A]).

**Minimality, recorded.** Within the native repertoire, the drive alone, `{J}` and `{NOT, J}` leave exotic cones (stage
5 C5 census [A]); outside it, one generic one-parameter rotation subgroup of one token (axis off the native frame's
coordinate axes) or one order-3 rotation about `(5,1,1)` already forces `Q3` (stage 4 S3[n], R1 [A]). So A_miss is the
minimal form **within the native repertoire**, not the minimal invariance overall.

**What the schema does not do.** It sources none of H2, H3, A_miss; it says nothing beyond two tokens; it identifies
no pair-level operation datum; and it does not discharge H-Bell (ROADMAP :1006).

## 4. Classification (§A.31)

ELABORATING: the clause table makes exact which K2 clauses the pair-cone stages settle and which they leave; the schema
restates stage 4's Y2 with each hypothesis's status at L and the kernel facts behind its controls. No NEW finding at
this node.
