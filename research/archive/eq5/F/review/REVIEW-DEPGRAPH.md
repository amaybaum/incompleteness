# Review of `eq5/F/DEPGRAPH.md` (adversarial; design only)

## 0. Scope, objects and evidence

- **Object reviewed:** `scratchpad/eq5/F/DEPGRAPH.md`, sha256 prefix `78fd34c3ca5c3156` (unchanged at the end).
- **Sources read:**
  - `verification/lean-mathlib/OIBridge/FourCopy{Defs,Parity,Package}.lean` at HEAD `f0d37906`. These are byte-identical
    to `eq5/inputs/`.
  - The certified base `scratchpad/eq/base/…/OIBridge/`: CompositeDimension, CompositeInterface, K2Guard,
    KInfFoundations, OrbitNormalization, EffectSpace, MonoidalCompletion and OperationalRigidity.
  - Background: `eq4/F/FORMAL.md`.
  - The two pre-check scripts and their outputs.
  - The preflight RESULT and LEDGER.
- **Integrity:**
  - The base manifest and the inputs manifest were checked at the start and at the end (`sha256sum -c --quiet`): OK
    both times.
  - The repository HEAD was `f0d37906` throughout, and the working tree is clean.
  - Writes went only to `eq5/F/review/`.
- **Pre-check evidence:**
  - Script and output hashes in DEPGRAPH §9 recomputed. All four match.
  - Both replays are byte-identical.
  - The `.err` files are empty.
- **New exact evidence:** `review/review_checks.py`.
  - Its decision rule was fixed in the header before the first run. Run with `python3 -I -B`, exact arithmetic only.
  - Definitions are implemented literally from the Lean text: `homMap`, `actT` and `actC` entrywise; `rot3`, `rotX`
    and `cyc3` as maps applied to basis vectors; `tensorOf` as `Matrix.of` on index pairs.
  - Complex numbers are Gaussian rationals over `Fraction`. Orthogonal matrices come from integer quaternions, not the
    Cayley transform, and the random seed differs from the note's.
  - Result: **21/21, `VERDICT REVIEW-CHECKS-EXACT`**, first run. Replay byte-identical. Hashes: `.py` `96a147de0eb2ca45`,
    `.out` `8127bfd9e7f239bc`. The `.err` files are empty.
  - The check list is in §6.
- **Not reviewed:**
  - `eq5/F/drafts/`, which DEPGRAPH does not cite.
  - The cited legacy values: `C_H` failing KT(4) at −1/200 [p6 H3], the `K_F` foils [p2 F1, F3] and f2 X3.

Verdict scale: CONFIRMED / ERROR (with correction) / GAP (what is missing).

## 1. Task 1 — the central favourable claim (IE₁-first, §4.1, G1–G15)

**Verdict: CONFIRMED (mathematics).**

IE₁ for all four pair cones, and `EvenCycle (fun p => orient (A p) (B p))`, follow from:
- `FourCopyCoherent`;
- N-CLASS;
- `CandidateCone`;
- `IsConvexCone`;
- `IsClosed`;
- forward gate preservation;
- inverse gate preservation.

The route uses no Pauli dictionary. Two ERRORs in the supporting text (E1, E3) and two GAPs (G1, G2) are listed below.

### (a) The cross relation G5/G6 — CONFIRMED

- **⊇.** `incl_I` [K] is the `famII` reading.
  - Links: the Bell states `bell02 ∈ K02`, `bell13 ∈ K13`. They come from O16, the products clause and `hgate`.
  - For `f ∈ K23*` this gives `Θ f ∈ K01**`.
  - O33 (`hK` from `hadm`, `K01.Nonempty` from the products) and `hcl` give `K01** = K01`. Bipolar is used here
    only, on K01.
- **⊆.** `incl_II` [K] is the `famI` reading.
  - Links: the Bell effects `bell_p ∈ K_p*`. They come from O17, G4a, `dualW_of_inv` [K] (needing O15 and `hinv`)
    and scaling by 4.
  - This gives `0 ≤ ipW X (Θ Y)` for `Y ∈ K23`.
  - Θ is ipW-orthogonal (G2), so `Θ⁻¹X ∈ K23*`.
  - No bipolar and no closedness are used on this side.
- **G6.** Dualize G5 using `(Θ S)* = Θ (S*)` for orthogonal Θ, then apply bipolar to K23.
- Consequence: `hinv` is consumed by IE₁ itself, not only by the parity. The ⊆ half of G5 is what turns
  `actC(…)(Θ f) ∈ K01` into `actC(…) '' K01 ⊆ K01`. §7.1's row for `hinv` (Bell effects, G4) is consistent with this.

### (b) The rotated links are members of K02 and K13 — CONFIRMED

- `N02 (prodState (A02′ᵀ x) (B02′ᵀ y)) = actC A02 (actT B02 (cnot (prodState x y)))` for every unit x, y.
  - Review C3 checks this for general rational points of S², all four determinant classes, and general pre-locals.
  - The note's M10 covered only equatorial x and y in the yz-plane.
- With `x = rot3 a xplus` and `y = rotX b z3`, both unit vectors, `cnot (prodState x y) = actC (rot3 a ∘ rotX b) phiW`
  (review C4).
- Membership reads exactly three things:
  - `CandidateCone.1`, the products clause;
  - `hgate`;
  - `IsOrth3 A′, B′`, which keep `A′ᵀx` a unit vector.

### (c) The four identities of G8 and the direction of the conjugations — CONFIRMED

- **Left link, control side.** With `A02ᵀA02 = I`, `L = Ĥ(A02 M A02ᵀ)·bell02`, so
  `L·g·bell13ᵀ = actC (A02 M A02ᵀ) (Θ g)`.
- **Left link, target side.** By G7(iii) the same L equals `bell02·Ĥ(B02 M′ᵀ B02ᵀ)` with `M′ = rotX b ∘ rot3 a`, so
  `L·g·bell13ᵀ = Θ (actC (B02 M′ᵀ B02ᵀ) g)`.
- **Right link.** The same two identities hold with `actT` and `A13`, `B13`.
- Review C5 builds both links literally as gate images `N02(product)` and `N13(product)` and checks all four
  identities on all units plus random tables.
- Countercontrols fail as required:
  - `A02ᵀ M A02` in place of `A02 M A02ᵀ`;
  - `B02 M′ B02ᵀ` without the transpose.
- The observation behind GAP G2: the "target-side link" needs no separate membership. It is the same gate image as
  the control-side link.

### (d) Every token side is covered — CONFIRMED

The eight instances, by target and link:

| target (reading) | link, side | conclusion | token |
|---|---|---|---|
| 01 (`target01` [K]) | 02, control | `actC(A02 M A02ᵀ) '' K01 ⊆ K01` | 0 |
| 01 | 13, control | `actT(A13 M A13ᵀ) '' K01 ⊆ K01` | 1 |
| 01 | 02, target | `actC(B02 M′ᵀ B02ᵀ) '' K23* ⊆ K23*` (Θ injective, ⊆ half of G5) | 2 |
| 01 | 13, target | `actT(B13 M′ᵀ B13ᵀ) '' K23* ⊆ K23*` | 3 |
| 02 (`target02`, O1, O3) | 01, control | invariance of K02, first index | 0 |
| 02 | 23, control | invariance of K02, second index | 2 |
| 02 | 01, target | invariance of K13*, first index | 1 |
| 02 | 23, target | invariance of K13*, second index | 3 |

- The index bookkeeping of `target02` was checked: `target02.upper` is `famII` and `target02.lower` is `famI` (review
  C6). So `⟨h.upper, h.lower⟩ : FourCopyCoherent K02 K13 K01 K23`, and the target-01 argument applies verbatim with
  `Θ′ = Theta A01 B01 A23 B23`.
- G12 then moves the invariance from K23* and K13* to K23 and K13 (bipolar).
- `target23` and `target13` (O5, O6) are not needed.

### (e) The generated monoid is SO(3) — CONFIRMED

- Mathlib's `AffineEquiv.coe_mul` gives `(e * e') = e ∘ e'`, transcribed in review T0. So
  `(rot3 ψ * rotX θ * rot3 φ).linear = rot3ψ ∘ rotXθ ∘ rot3φ`.
- The base's `euler_apply_pole` formula is reproduced with the literal `rotX` (review C4).
- The link family contains `rot3 a` (b = 0) and `rotX b` (a = 0).
- The invariance set `{R | actC R '' K ⊆ K}` is closed under composition: `homMap` is multiplicative.
- For `R′ ∈ SO(3)`, put `R := Aᵀ R′ A`. Then R is orthogonal with `det R = (det A)² det R′ = 1`, and so3_euler gives
  `R′ = (A rot3ψ Aᵀ)(A rotXθ Aᵀ)(A rot3φ Aᵀ)`.
- Equality of images (G11) follows from `Rᵀ ∈ SO(3)`.

### (f) The parity reduction G14 — CONFIRMED

**The decomposition.**
- `ε_A := reflY` if `det A = −1`, and I otherwise.
- `R_A := A ε_A ∈ SO(3)`, `A = R_A ε_A` and `R_Aᵀ A = ε_A`.
- `orient A B = decide (det A det B = −1) = (ε_A ≠ ε_B)`.

**State witnesses** (pairs 01 and 23):
1. `prodState (A′ᵀ xplus) (B′ᵀ z3)` lies in K_p by the products clause.
2. Under N it becomes `actC A (actT B (cnot (prodState xplus z3)))`, which lies in K_p by `hgate`.
3. IE₁(K_p) with `R_Aᵀ`, `R_Bᵀ` gives `actC ε_A (actT ε_B (cnot P)) ∈ K_p`.
4. This equals `gateOf (orient A B) P`. The four ε cases use O14 or `cnotTw_apply`, together with
   `reflY xplus = xplus` and `reflY z3 = z3`.

**Effect witnesses** (pairs 02 and 13, signs `s = ±1`):
1. `tens (sharpVec (A′ᵀ(s xplus))) (sharpVec (B′ᵀ(s z3)))` lies in `K_p*` by G4a.
2. `dualW_of_inv` (O15 and `hinv`) gives `actC A (actT B (cnot (tens …)))` in `K_p*`.
3. IE₁(K_p*) by G12 gives `actC ε_A (actT ε_B (cnot (tens …)))` in `K_p*`.
4. This equals `gateOf (orient A B) (tens …)`.

**Evidence.**
- Review C7 checks both reductions for all four determinant classes, general pre-locals and `s = ±1`. The
  countercontrol `gateOf (¬orient)` fails as required.
- Review C8 checks the end-to-end value of `famI` on the reduced general-chart witnesses over all 16 patterns. It is
  `0` at even patterns and `−1/8` at odd ones.
- These four memberships are exactly the ones `kt4_parity_aligned`'s proof derives (`hX`, `hY`, `hE`, `hF`), with
  τ_p = orient.

### Skeptical sweep — no defects found

- **Hidden Pauli use:** none. No step uses Q3, the twin, `pauliW` or ℂ.
- **Circularity:** none. IE₁ is derived in G13. G14 uses only the derived IE₁ of K_p and of K_p*.
- **(o)-step:** none. Every gate use is a standalone pair's gate, or its inverse's dual, acting on that pair's product
  states or product effects.
- **Closedness and convexity:** used only for the pair cones' own bipolar. Both are available as `hcl` and `hadm`.
  `isClosed_dualW` (O30) is not needed.

### Defects in the supporting text

- **E3** (step tags) and **E1** (G2's evidence): see §7.
- **G1:** G5 and G6 are stated only at target 01, but the note uses them at target 02 (G9 "the same at target 02", and
  L13 "for every p").
- **G2:** G8's table does not say which link state each identity uses.

## 2. Task 2 — the classification layer (§4.2, L1–L13)

**Verdict: CONFIRMED.** One GAP (G3) and one wrong edge (part of E7).

### L13, the squeeze — CONFIRMED

```
K01 ⊆ Θ(C23*) = Θ(C23)        (G5;  C23 ⊆ K23 by L12;  O28/O29 ⊆ half)
Θ(C23) ⊆ Θ(K23) = K01*        (L12 at 23;  G6)
K01* ⊆ C01* = C01 ⊆ K01       (L12 at 01;  O28/O29 ⊆ half)
```

- Hence `K01 = C01 = twistQ3 (orient A01 B01)`.
- No step uses `chart_rule`, `Q3 ≠ twin` or `ie1_Q3`.
- The other pairs follow in the same way, using G5/G6 at target 02 (GAP G1).
- Both halves of O28 are consumed: the ⊆ half here, the ⊇ half in L10. O34 is therefore needed.

### L12, the lower bound — CONFIRMED

The cases of `(ε_A, ε_B)`:
- `(I, I)`: L10.
- `(I, reflY)`: L10 applied to `actT reflY '' K`, which is a closed convex cone.
- `(reflY, I)`: `actC reflY (pureTab C) = actT reflY (pureTab C̄)` (review P3), and `actC reflY '' Q3 = twin`.
- `(reflY, reflY)`: `actT reflY (actC reflY (pureTab C)) = transposeW (pureTab C) = pureTab C̄` (review P2, P3). Since
  C ↦ C̄ is onto, this lands in Q3, and orient = false.
- Review P3 also checks that `actT reflY` is exactly the partial transpose on the second tensor factor, using an
  index-swap implementation. That gives `twin = PT₂(Q3)`.

### L10, `Q3_subset_of_pure` — CONFIRMED

- L3 gives `K* ⊆ Q3`.
- Hence `Q3 ⊆ Q3* ⊆ K** = K`. Only the ⊇ half of O28 is used.
- O33 needs `K.Nonempty`, which `pureTab 0 = 0 ∈ K` supplies.

### L11(i), `transposeW (pureTab C) = pureTab (C.map star)` — CONFIRMED

- Proof:
  1. Conjugate the trace.
  2. Use `σ̄ = σᵀ` for Hermitian σ.
  3. Use `σ_μᵀ = s_μ σ_μ` with `s = (1, 1, −1, 1)`.
- This gives `pureTab C̄ μν = s_μ s_ν pureTab C μν`.
- Checked directly in review P2, with 6 Gaussian-rational C. The countercontrol `pureTab Cᵀ` fails.
- The note's evidence is indirect (S5 + S2 + injectivity of `pauliW`). That derivation is valid.

### L1, L2, L4, L5, L6, L8 — CONFIRMED

- All six were rechecked with independent arithmetic (review P1, P4, P5).
- L8 was checked with complex `d₀` as well. The note's S1 covered real `d₀` only.

### L9 — GAP G3

- As tabled, its statement omits two things it needs:
  - closure of K under nonnegative scaling (the factor `‖d₀‖²+‖d₁‖²`, and C = 0);
  - the fact `ε R ε ∈ SO(3)`.
- Its cited evidence "[X N8]" is not what L9 uses. N8 concerns `gateOf` on the Lemma P witnesses.
- The edge "L9 reads … the N8 identities" in §3 is wrong. L9 reads G13 (IE₁) instead (E7).

## 3. Task 3 — Lemma B1 (§4.3) — CONFIRMED

Traced against the `ProductData` fields (CI:210–218), the `PreComposite` fields (CI:223–230) and `Composite.lt`
(CI:245–246), and against `KT4`, `TokenCoherent`, `pairBody`, `tabCoord` and `flatW`.

**famI.**
- **Inputs.**
  - The state is `ω = PA.prodState x̂ ŷ`. It lies in `PA.Ω` by `prod_mem` (B1b) and in `PB.Ω` by `one_body`.
  - The effects come from `PB.prodEff_effect`, with `e_E` and `f_F` from O21.
- **Expansion.** Bilinear expansion (B1d), then
  `tok μ κ ν λ ω : PA.prodEff (tabCoord μ κ) (tabCoord ν λ) ω = PB.prodEff (tabCoord μ ν) (tabCoord κ λ) ω`, read
  right to left. Then `PA.prodEff_apply`.
- **Value.** `c c′ Σ E_μν F_κλ X̂_μκ Ŷ_νλ = c c′ · fourVal X̂ Ŷ E F`.

**famII.**
- **Inputs.**
  - The state is `PB.prodState L̂ L̂′`. It lies in `PB.Ω = PA.Ω` by `one_body` in the other direction.
  - The effect is `PA.prodEff e_e f_f`.
- **Expansion.** `tok` read left to right, then `PB.prodEff_apply`.
- **Value.** `c c′ Σ e_μν f_κλ L̂_μκ L̂′_νλ = c c′ · fourVal e f L̂ L̂′`.

**Identification and evidence.**
- O1 identifies both values: `fourVal X Y E F = ipW X (E Y Fᵀ)` and `fourVal e f L L′ = ipW e (L f L′ᵀ)`.
- Review B2 checks both expansions. The countercontrol (no regrouping) fails.
- `one_body` is used in both directions. The `tok` directions are as stated.

**B1a.**
- `|ω μν| ≤ ω 0 0` follows from sums of pairs of sharp products `±eᵢ ⊗ ±e_k` (review B1, symbolic). These are
  `(ω₀₀ ± ω_ik)/2`, `(ω₀₀ ± ω_i0)/2` and `(ω₀₀ ± ω_0k)/2`, each ≥ 0.
- Hence `ω₀₀ = 0 → ω = 0`.

**B1c.** `c = 1/(1 + Σ|E_μν|)` works with the restated bound at `ω₀₀ = 1`.

**Fields.**
- Not read: `convex`, `prodEff_unit`, `prodState_combo_left/right` and `lt`. Confirmed.
- From `PairAdm`, B1 reads only `CandidateCone.2` (the maximal-cone bound) and the scaling half of `IsConvexCone`.

## 4. Task 4 — counts and graph (§2–§3)

### Counts — CONFIRMED

Independent enumeration: an `awk` pass over the `^  sorry$` lines of `FourCopyPackage.lean`.
- It finds 48 obligations.
- The only other occurrence of the word is the header comment at line 5.
- The order is identical to the note's O1–O48 (fourVal_eq_01 … not_fcc_odd).

The partition:
- **A′** = {1, 3, 14, 15, 16, 17, 20, 21, 22, 33, 39}: **11**. IE₁ alone needs 10; O14 enters only through the parity
  route chosen.
- **A** = A′ ∪ {28, 29, 34, 38 (as L10), 44}: **16**.
- **Off-headline: 32.** The ten groups sum to 32, they are pairwise disjoint from A, and the union is {1…48}.
- No obligation is misclassified between A′, A and off-headline.

Observation, not an error: O14 is avoidable. The four ε cases of G14 are concrete tables (review C7 computes them
directly). It is in A′ only because the route chooses it.

### Dependencies — headline rows CONFIRMED; off-headline rows contain errors (E5)

- **O43** lists only O44. With `hinv` in O44 it also needs O12, to supply `hinv` for aligned gates, unless (R) removes
  `hinv`.
- **O46** lists "—". `famI` and `famII` quantify over `dualW Q3`, and `PosSemidef.kronecker` needs those effect
  factors to be PSD. So O46 needs the ⊆ half of O28 (L3 + O34).
- **O47** needs O29, or alternatively O46 + O19 + L11 with charts `ε = (0, 1, 1, 0)`.
- **O48** cites "O24-type facts". `not_fcc_odd` needs membership facts, not O24:
  - either O26, `CandidateCone twin` and the gate preservations `cnot '' Q3 ⊆ Q3` and `cnotTw '' twin ⊆ twin` (each a
    new small lemma), used through `kt4_parity_aligned` [K] at τ = (0, 0, 0, 1);
  - or O23 + O28 + O29 for the direct witness.
- **O32** needs O23 as well as O31.
- **O13**'s consumer "Theorem B" is wrong. `kt4_aligned` reads no `NativeGate`, and O13 has no consumer in the
  package: it is a satisfiability control.
- **O18 and O19** carry the consumer "Theorem B", but they are not read under the O43 route the table itself gives.

### §3 edges (E7)

- **G9** reads G2 (Θ injective, for the target-side instances) and `incl_I` [K]. It does not read G3.
- **G14** reads G7 (state witnesses as gate images), G4a, `dualW_of_inv` [K] and O15 (effect witnesses). None of
  these appears.
- **L9** reads G13 and cone scaling, not "the N8 identities".

### The "30" of the earlier route — GAP G6

The 30 obligations are not listed. One reconstruction gives exactly 30, so the figure is plausible but not checkable
from the note:

> O1–O6, O15–O17, O20–O22, O23–O25, O28–O30, O31–O32, O33, O34, O35–O38, O39–O41, O44

## 5. Task 5 — minimal-assumption claims (§7)

### (a) The recurrence lemma (R) — CONFIRMED

- O(16) is compact, so some subsequence `N^{n_k}` converges. Then `N^{n_{k+1}−n_k} → I`.
- So `N^{m_k−1} → N⁻¹` with `m_k − 1 ≥ 0`, and `N^{m_k−1} ω ∈ K`. Closedness gives `N⁻¹ω ∈ K`.
- Only orthogonality of N and closedness of K are used. Convexity is not.
- `hinv` follows from `hcls ∧ hgate ∧ hcl`: O15 makes N_p orthogonal.
- Conversely, (R) applied to `N.symm` derives `hgate` from `hinv`.
- `tendsto_subseq_of_bounded` exists (Mathlib Topology/MetricSpace/Sequences.lean:38).

### (b) Closedness is redundant for the parity — CONFIRMED

Every hypothesis passes to closures:
- `dualW (cl K) = dualW K`;
- both families are continuous in their state slots;
- `maxCone` is an intersection of closed half-spaces;
- the gates are continuous, both forward and inverse;
- a convex cone's closure is a convex cone.

The parity conclusion mentions only `(A_p, B_p)`.

### (c) The foil rows — logic CONFIRMED, with GAPs G4, G5, G7, G8

**KT(4) row, (A2), C_H.**
- `|H| = 8`.
- `phiW = cnot(prodState xplus z3) ∈ C_H`.
- `ψ₁ = actT R_H phiW`, with `R_H ∈ SO(3)`.
- Review F1 certifies `ψ₁ ∉ C_H` independently of the extreme-ray argument:
  - every `h ∈ H` is ipW-orthogonal and fixes the `(0,0)` entry;
  - every `h(ψ₁)` has zero local parts and an orthogonal correlation block;
  - `ψ₁₀₀ = 1` and `ipW ψ₁ ψ₁ = 4`.
- So the linear witness `W = 2e₀₀ − ψ₁` satisfies `W(h(prodState x y)) = 1 − xᵀ T y ≥ 0` on every generator of C_H,
  while `W(ψ₁) = −2`.
- Countercontrols: the certificate fails for `phiW`, which lies in C_H, and for a product state.

**Convexity row, `R1 ∪ SEP ∪ cnot SEP`.**
- R1 is never defined (GAP G4). Under the reading "R1 = the pure tables `{s • pureTab C}`, the rank-≤1 part of Q3",
  every listed property holds:
  - closed, as a finite union of closed cones;
  - it contains the products;
  - it is `cnot`-invariant (`cnot` is `Ad CNOT`, and `cnot` swaps SEP with `cnot SEP`);
  - it lies inside `maxCone`;
  - its dual is Q3, by L3 and `conv R1 = Q3`.
- The uniform interface holds because the cone is a subset of Q3 with dual Q3, *given O46*. The open obligation is
  not mentioned in the row (GAP G5).
- (A2): `ρ = cnot σ` lies in the set, while `ρ′ = actT R_H ρ` does not (review F2, with an independent partial
  transpose):
  - `ρ′` is PSD with rank 2;
  - both `det PT₂` values are `−135/4096`;
  - the control σ is PPT.

**Closedness row, `int Q3 ∪ conv(SEP ∪ cnot SEP)`.**
- The set is convex: segments from interior points to points of the closure stay in the interior.
- It is not closed.
- `ψ₁` lies outside it:
  - `det pauliW ψ₁ = 0` and its rank is 1 (review F3);
  - `conv(SEP ∪ cnot SEP) ⊆ C_H`, and F1's witness separates `ψ₁` from C_H.
- Its interface also needs O46 (GAP G5).

**Products, maximal-cone bound, N-CLASS and forward-gate rows.** CONFIRMED as [W] arguments.
- `{0}` has `pairBody = ∅`, and the KT4 data exist with `Ω = ∅`.
- `W 3` has dual `{0}`.
- SEP with `N = id`.
- In the forward-gate row, SEP and max also violate `hinv`. They are foils for the hypothesis list *with `hinv`
  removed*, which the row presupposes but does not say (GAP G8).

**Necessity.**
- The note never claims necessity: see §7.6 "Scope" and §1 item 5, "they do not show necessity".
- Every "none known" in (A2) is presented as open (§7.6 "What the table shows"). That is honest.
- The granularity of "every read hypothesis has a foil" is table rows: the KT4Core fields `prod_mem`,
  `prodEff_effect`, `prodEff_apply` and bilinearity have no separate foils (GAP G7).

**§7.2 pre-locals — ERROR E6.**
- The pre-locals' orthogonality is read. O15 needs it (N's ipW-orthogonality, consumed by `dualW_of_inv` and by (R)).
- The ball clause needs it too, to keep `A′ᵀx` a unit vector.

## 6. Task 6 — independent exact checks (`review/review_checks.py`, 21/21)

| id | content | countercontrol (failed as required) |
|---|---|---|
| T0 | 37 Lean definitions found verbatim, including Mathlib `AffineEquiv.coe_mul`; `sgn`, `pc`, `pt` parsed independently | — |
| T1 | literal `actC`/`actT` equal `H(N)·ω` and `ω·H(N)ᵀ` for non-orthogonal N (validates the pre-checks' matrix model) | — |
| C1 | G1 with all four det classes of `(A02, B02)` | no reflY: 143 failures |
| C2 | G2 including the note's N9 (`Θ⁻¹ = actC R02ᵀ ∘ actT R13ᵀ`) | R in place of Rᵀ: 141 |
| C3 | G7(i) for general unit x, y | `A′x` in place of `A′ᵀx`: 60 |
| C4 | G7(ii), G7(iii) and `euler_apply_pole` with literal rot3/rotX/cyc3, 36 angle pairs | same composition order on both sides: 25 |
| C5 | G8, all four identities, with the links built as gate images | 156 and 156 |
| C6 | O1, O3; the `target02` fields are `famII` and `famI` | transposes dropped: 5 |
| C7 | G14 witness reduction, states and effects, s = ±1, all four det classes | `gateOf (¬orient)`: 32 |
| C8 | G14 end to end, 16 patterns: value 0 (even) and −1/8 (odd) | — |
| C9 | G3 adjoints and commutation (non-orthogonal M); O14 on all units | — |
| P1 | L1 (exactly real), L2 | — |
| P2 | L11(i) | `pureTab Cᵀ`: 6 |
| P3 | L11(ii), the L12 cases, `actT reflY` = PT₂ | `idW` has singlet expectation −1 |
| P4 | L8 with complex `d₀`, `d₁` | conjugate phase: 6 |
| P5 | L4, L6 with quaternion SU(2) elements | `R_Uᵀ`: 12 of 16 (the 4 coincident pairs have q₀ = 0) |
| F1 | C_H exclusion by a linear witness | certificate fails for `phiW` and for a product |
| F2 | convexity foil, index-swap partial transpose, dets −135/4096 | control σ is PPT |
| F3 | closedness foil: `ψ₁` singular, rank 1 | — |
| B1 | B1a sharp combinations, symbolic | — |
| B2 | B1e expansions for both families | no regrouping: 4 |

## 7. Findings

### ERRORS (must fix)

**E1. G2's evidence N9 is not certified.**
- `precheck_core.py` computes `ok9` (line 237) but never passes it to `check()`. N9 prints no line, is not among the
  23/23, and does not enter the VERDICT.
- The script's own preregistered decision rule (docstring line 32) lists N9 among "every check below". The rendered
  verdict therefore did not implement its stated rule.
- The identity is true (review C2).
- Fix one of two ways:
  - **(i)** Add `check("N9 Theta inverse …", ok9)` and re-run as run 2. Keep run 1 as `.run1.*` and update §9 (24/24,
    new hashes).
  - **(ii)** Amend the text. Replace line 199's evidence `[X M8, N9]` with
    `[X M8]; inverse [W] from G1 and orthogonality (review C2)`. Replace line 287's
    "- M1–M11 and N1–N9 (rotation links, Θ, reflection charts, witness reduction);" with
    "- M1–M11 and N1–N8 (rotation links, Θ, reflection charts, witness reduction); N9 is computed but not asserted;".

**E2. Line 17 miscounts the checks.**
- Current: "- `precheck_ie1first.py`: 12/12, verdict `IE1FIRST-PRECHECK-EXACT`; its checks are M1–M11."
- The 12 checks include K0. Replace "its checks are M1–M11." with "its checks are K0 and M1–M11.".

**E3. Lines 223–224 mislabel the steps.**
- Current: "Steps (2) and (3) are (2)-type, since the gate acts on product states of its own pair; every other step is
  (s)-type."
- Step 3 performs no operation. Step 1 consumes (2)-supplied Bell states and effects exactly as step 2 consumes link
  states. Under FORMAL's tags this is "(s) on (2) data" (S11).
- Replace with: "Steps 1 and 2 consume (2)-type data: the native gate of a standalone link pair applied to its own
  product states (Bell and rotated links) and the inverse gate's dual action on its own product effects (Bell effects).
  Every inference step, 1–4, is (s)-type ("(s) on (2) data", FORMAL S11). No (o) step occurs."

**E4. Lines 42–43 overclaim.**
- Current: "Every algebraic identity among them is covered by an exact pre-check."
- This is false for:
  - G2's inverse formula (E1);
  - G3's composition and commutation laws;
  - L11(i), which is only derived;
  - the reflection bookkeeping of L9, L12 and G14 (`A = R_A ε_A`, `ε R ε ∈ SO(3)`).
- Replace with: "Every algebraic identity among them is covered by an exact pre-check except G2's inverse formula,
  G3's composition and commutation laws, L11(i) and the reflection bookkeeping of L9, L12 and G14. Those are covered
  by the review checks C2, C7, C9, P2 and P3."

**E5. Off-headline dependency entries in §2 are wrong or missing.** No count changes.

| row | replace | with |
|---|---|---|
| O43 | "O44" | "O44, O12 (to supply `hinv` for aligned gates; not needed once (R) removes `hinv`)" |
| O46 | "—" | "O28 (⊆ half: the effect factors in `dualW Q3` are PSD), O1" |
| O47 | "O46" | "O46, O29 (or O46 + O19 + L11 with charts ε = (0,1,1,0))" |
| O48 | "O24-type facts" | "O26, `CandidateCone twin` and the gate preservations of Q3 (`cnot`) and twin (`cnotTw`), via `kt4_parity_aligned` [K]; or O23 + O28 + O29" |
| O32 | "O31" | "O31, O23" |

The consumer column also needs fixing:
- **O13:** replace "Theorem B" with "none (satisfiability control for `cnotTw`)".
- **O18, O19:** replace "Theorem B" with "an alternative chart-transport route to Theorem B; not read by O43 as routed".

**E6. Lines 337–338 understate what the pre-locals carry.**
- Current: "Pre-locals `A′, B′` are read only through `A′⁻¹x`, `B′⁻¹y` of unit vectors. They reparametrize the product
  states and carry no content."
- Replace with: "Pre-locals `A′, B′` are read only through their orthogonality (O15, used by `dualW_of_inv` and by
  (R); and to keep `A′ᵀx`, `B′ᵀy` in the ball) and through the reparametrized inputs `A′ᵀx`, `B′ᵀy`. No conclusion
  depends on their values."

**E7. §3 edges are wrong or missing.**
- Lines 162–163, "G9 … which reads G5, G6, G7 (link family), G8 (rotated-link identities), O33 and G3 (adjoints)":
  replace "G3 (adjoints)" with "G2 (Θ injective) and `incl_I` [K]".
- Lines 166–169 (G14): add the edges "G7 (state witnesses as gate images), G4a, `dualW_of_inv` [K] and O15 (effect
  witnesses)".
- Line 173, "L9 (pure tables in the cone), which reads L6, L7, L8, G7 and the N8 identities": replace "and the N8
  identities" with ", G13 (IE₁) and cone scaling". Make the same change to L9's evidence cell in §4.2.

**E8. Line 310's "cheap" list contradicts the tables.**
- Current: "Everything else on the headline is cheap: O1, O3, O14, O15–O17, O20, O21, G1–G8, G10–G12, G14–G15, L11 and
  L13."
- The tables rate G10 **m**, which is a direct contradiction, and O15–O17, O21, G7, G14 and L11 c–m.
- Replace with: "Everything else on the headline is cheap: c for O1, O3, O14, O20, G1–G6, G8, G11, G12, G15 and L13;
  c–m for O15–O17, O21, G7, G14 and L11; G10 is m (O39 plus bookkeeping)."

### GAPS (should state)

- **G1. G5 and G6 at target 02.** State them over generic cones, or over `PairLinked`, with nonemptiness supplied by
  the products clause, as O33 requires. They are used at target 02 through
  `FourCopyCoherent K02 K13 K01 K23 := ⟨target02.upper, target02.lower⟩`, with `Θ′ = Theta A01 B01 A23 B23` (G9, G13,
  L13).
- **G2. G8 should name its links.** The left link is `L = actC A02 (actT B02 (actC M phiW))` with
  `M = rot3 a ∘ rotX b`. By G7(iii) it equals `actC A02 (actT B02 (actT M′ phiW))` with `M′ = rotX b ∘ rot3 a`, so the
  target-side identities need no extra membership.
- **G3. L9's hypotheses.** Add `IsConvexCone K` (at least scaling) and the fact `ε R ε ∈ SO(3)` for `ε ∈ {I, reflY}`.
- **G4. Define R1.** In the convexity foil, R1 should be the pure tables `{s • pureTab C | s ≥ 0}`.
- **G5. Name O46 in two foil rows.** The convexity and closedness foils' uniform interface rests on O46
  (`fcc_uniform_Q3`, open). Write "[… + W, given O46]", as the forward-gate (A3) cell already does.
- **G6. List the 30.** List the 30 obligations of the earlier route (one consistent reconstruction is given in §4).
- **G7. Foil granularity.** "Every read hypothesis has a foil" is meant at row granularity. The individual KT4Core
  fields have no separate foils.
- **G8. The `hgate`/`hinv` symmetry.** Under `hcls ∧ hcl`, `hgate` and `hinv` are symmetric: each is redundant given
  the other. The §7.6 foils for "forward gate" are relative to the list with `hinv` removed. Say so in the row.
- **G9. Evidence scope.**
  - S1 covers only real `d₀`, so L8's complex phase is [W] there.
  - M10 covers only restricted (x, y).
  - Both are now covered exactly by review P4 and C3. Cite them, or extend the pre-checks.
- **G10. Round R-A's list (§8).** It names "kt4_forward", which has no `sorry` of its own. Its open content is O44
  (`kt4_general`), and through O22 it already depends on R-A′. Name O44 and O38-as-L10 explicitly, so that R-A's
  obligations read O28, O29, O34, O38 (L10) and O44 — the five that A adds to A′.

### CONFIRMED

**Task 1:**
- IE₁ for all four pairs and the orientation parity follow from the stated hypotheses without the Pauli dictionary.
- Items (a)–(f) are confirmed.
- No hidden Q3, `pauliW` or ℂ; no circularity; no (o) step.
- Closedness and convexity are used only where they are hypotheses.
- `hinv` enters IE₁ through the ⊆ half of G5 as well as the parity effects.

**Task 2:**
- The L13 squeeze needs neither `chart_rule` nor `Q3 ≠ twin`.
- The L12 cases, L10 by duality, and `transposeW (pureTab C) = pureTab (C.map star)` are confirmed.
- L1, L2, L4–L6 and L8 are confirmed, the last including complex `d₀`.

**Task 3:**
- Lemma B1 confirmed: the `tok` directions, `one_body` in both directions, both values equal to `fourVal` through O1.
- `convex`, `prodEff_unit`, `prodState_combo_*` and `lt` are not read.

**Task 4:**
- 48 obligations, numbering as stated; A′ = 11 (IE₁ alone 10), A = 16, off-headline 32.
- Headline dependencies are correct, and no obligation is misclassified.

**Task 5:**
- (R) and both redundancy directions; closedness redundant for the parity.
- The foil logic, including:
  - an independent exact certificate that `ψ₁ ∉ C_H`;
  - an independent partial-transpose recheck of the convexity foil.
- No necessity is claimed, and the "none known" entries are honestly open.

**Bookkeeping:**
- §9 hashes match, replays are byte-identical, `.err` files are empty.
- Every cited Mathlib name exists at the stated paths: `tendsto_subseq_of_bounded`,
  `geometric_hahn_banach_closed_point` (:231), `exists_eigenvalue`, `spectral_theorem` (:141),
  `exists_eq_mul_self` (:90), `trace_kronecker`, `posSemidef_iff_dotProduct_mulVec` (:297) and
  `posSemidef_vecMulVec_self_star` (:412).
- The base anchors exist as cited: OR:917, ON:589 and ON:614.

Consistency-axis work only; bands unchanged.
