# Coordinator's audit of thread S2 — PAIR-CONS (stage 2)

Audited: `pt/S2/RESULT.md`, sha256 `b1139809e61dd4526108e7e2a9aafe038909eb042de40980d77c265fef5bbe89`. `pt/S2/` holds 38 entries and no subdirectory.

## Integrity
- **Coordinator's check, 08:37Z.**
  - The `inputs`, `stage1` and `inputs2` manifests are OK.
  - Base HEAD is `9f9f8257…`; status is clean; there is no bytecode.
  - The four protocol files are unchanged.
  - No file outside `pt/S2/` and `pt/S3/` is newer than the start markers.
- **The start marker** was written at 07:26:56Z into an empty directory. It records green start checks.
- **Hashes.** Every script and output hash in RESULT §6 matches the files.
- **Notes.** `NOTES.md` records only pre-run edits and one wording correction: the frame-covariance rotations are by −2φ. It records no anomaly.

## Replays
Run as `python3 -I -B` from `pt/auditS2-replay/`, with the OIBridge path argument, plus `../inputs/fourcopy` for `s2_6`. All seven reproduce stdout and `.err` byte for byte:

| script | checks |
|---|---|
| `s2_1_native` | 42 |
| `s2_2_beyond` | 38 |
| `s2_3_lt` | 35 |
| `s2_4_rank` | 15 |
| `s2_5_tower` | 17 |
| `s2_6_effects` | 22 |
| `s2_7_supp` | 13 |

The total is 182. Afterwards the base status is empty and there is no bytecode.

## Independent check (no thread code)
`indep_checkS2.py`: sha256 `c1c6badf…`; output `951bad14…`; the replay is identical. **26/26 CONFIRMED**, verdict `INDEP-S2-CONFIRMED`.

**Run 1** (kept as `indep_checkS2.run1.*`) printed 25/26. The one MISMATCH was my own countercontrol C1c, which was badly designed. It tested "cnot ∘ C(Rx, I) is not local" on a single product whose target is an x-eigenstate, and CNOT leaves that input unentangled. Run 2 scans the 36 axis products instead: 16 of 36 give entangled images. All other lines of the two runs are identical. No claim of the thread was in question.

The landed predicates were re-implemented from `CompositeDimension.lean:210–224` (`IsNot`, `NativeGate`: frame, relT and relC with `z3` and `nflip`). Then:

- **Theorem N (exact, N1–N6).**
  - Of the 4096 signed-diagonal dressings of `cnot`, those meeting frame, relT and relC are **exactly 32 distinct gates**, `cnot` among them.
  - Each gate has one orientation pair over all its dressings, and there are 8 gates per pair.
  - **Absorption:** `cnot ∘ L ∘ cnot` is local exactly for the 32 orientation-even locals among the 64.
  - Over all 1024 ordered pairs, `G_i ∘ G_j` has a negative product-effect value on axis data **exactly** when `orient_pre(G_i) ≠ orient_post(G_j)`. That happens for 512 pairs.
  - The (even, even) class generates a group of order 16, each element a local or `cnot ∘ local`. Hence its generated cone is `SEP + cnot SEP = K_gen`.
  - `σ = actT reflY` conjugates the (even, even) class onto the (odd, odd) class.
  - posFwd and posInv hold for every dressing by orthogonality of the locals and [K] `cnot_prodState_mem_maxCone` [W].
- **Carrier models (R1–R7).**
  - Register model: N² = cnot ⊕ cnot, N⁴ = I and N² ≠ I. The product action holds, and every generated table is p or cnot p. `N(pxz,0)` and `N²(pxz,0)` share a table but are separated by N, so the model is not LT.
  - Block lemma, symbolic, with one hidden coordinate: the defect is B C v, and the W3-block of N∘N is I + BC.
  - Hidden-parameter model, my own instance (Δ = E11 − E10, cnot Δ = −Δ): N² = I; the ungenerated states (E00, ±1/4) share a table and are separated by N; their images are valid.
  - Rebit control: Ad(CNOT) sends X⊗Z to −Y⊗Y, so the induced product-table action kills X⊗Z. (I + Y⊗Y)/4, a CNOT image of a mixture of real products, and I/4 share tables, and CNOT tests separate them.
  - A model with LT on the generated system and N² ≠ I on the carrier: cnot ⊕ D, with D³ = I and no coupling.
  - **Clock model:** the parity sequence has run lengths 1, 3, 5, … from j = 1. Its L×L Hankel sections have exact ranks **8, 16, 32, 48, 64** at L = 8, 16, 32, 48, 64, matching the thread's reported ranks. A period-4 control has rank 3.
- **Monomial and finite groups (M1–M3).**
  - No arrangement of ψ_w's modulus pattern (9, 16, 0, 25)/50 is rank one.
  - ψ_w's reduced Bloch length² is 16/25, equal to that of CNOT(|a⟩|0⟩) with Bloch(a) = (3/5, 0, 4/5).
  - ⟨CNOT, SWAP⟩ has order 6, and no element maps ψ_w to a product vector.
- **Effects (E1–E5).**
  - `cnot` is a symmetric orthogonal involution, so generated effects equal generated states.
  - `T_ψ = actT R_H phiW` is pure. R_H is the landed probe's matrix, `kt4_prem1_probe.py:119`.
  - `F = E00/2 − T_ψ/4` takes the value `1/4 + xᵀMy` with |M| ≤ 1/4 on products and on cnot images, so F ∈ dualW K_gen. This route is independent of the thread's.
  - `tr ρ(F) ρ(T_ψ) = −1/8`, so F ∉ Q3.
  - **famI(phiW, phiW, T_ψ/4, F) = −1/8** uses two non-generated effects. The countercontrol with generated effects gives 1/4.
- **Frame covariance (C1, C2, C1c).**
  - `cnot ∘ C(Rx,I) ∘ C(I,Zπ) ∘ C(Rx,Zπ) = actC(rotation about x by −2φ)` holds symbolically modulo c² + s² = 1.
  - `cnot ∘ C(I,Rz) ∘ C(Xπ,I) ∘ C(Xπ,Rz) = actT(rotation about z by −2φ)` likewise. Both signs agree with the thread's corrected wording.
  - `cnot ∘ C(Rx,I)` alone is not local.

## Design-source check of the effect-consumption table (EFF)
In the S3 audit I read the FCC consumption sites (FourCopyIE1:166, :171, :315, :329, :343, :363, :448; FourCopyParity:237). They match S2's table:
- `cross_rel ⊆` (upper) reads only generated effects.
- `cross_rel ⊇` and the four invariance lemmas (lower) read **free effects over the full duals**.
- The parity lemma reads only generated arguments.

The two threads agree: FCC's force against the native construction lies in its free full-dual effect slots.

## Written steps reviewed
- **INV2 ⇒ LT** (block lemma plus "LT ⟺ PTQ for test-generated towers").
  - Correct. The (⇐) induction on words and the (⇒) restriction are both sound.
  - The four models each remove one ingredient, as stated.
  - **Renaming test:** passed. INV2 says one operation composed with itself is the identity; LT says product tests separate states. They are equivalent only relative to generation and the product action.
- **Finite rank.**
  - The finite-group bound (rank ≤ 16·|G| − 1) is immediate from bi-affinity [W].
  - The clock model's infinite rank uses Kronecker's theorem on Hankel matrices [L, standard], plus the pigeonhole step on the run lengths [W]. Both are sound.
  - The clock model meets the product action because the clock starts at 0, which is a square.
- **Theorem N** is now confirmed exactly here as well. Completeness beyond signed-diagonal dressings rests on Thread D's D1.4 [W + X, audited], as the thread states.
- **Theorems M and F** are [W + L], with Milman's converse and the dimensions of CP³ and S²×S². The exact witnesses are confirmed.
- **FC ⟺ IE1 given hgate.**
  - (⇒) The confirmed words give one-parameter local rotations about x on the control and about z on the target. Conjugation reaches every rotation [W].
  - (⇐) is immediate.
  - Being a restatement of IE1 given hgate, FC stays flagged.

## Label qualifications for integration (no change of substance)
1. **GC "DERIVED for the constructed system"** is DERIVED *relative to the construction rules*: generation (C6, C7) and the table rule (C5), which are the adopted meaning of "from data", plus [K] facts.
   - L defines no pair system, so relative to certified L the gate premise keeps its stage-1 status: INDEPENDENT.
   - For the generated cone, gate invariance holds by construction. The substantive content is validity (C10), which rests on [K] `cnot_prodState_mem_maxCone` and `cnotFun_cnotFun`.
2. **LT under the table rule is built in, not derived.** The thread says so. The non-trivial LT result is the abstract-carrier one, CONDITIONAL on INV2.
3. **"S2 ∧ S3 unsatisfiable"** is scoped to the construction classes examined: `𝒞_nat`, `𝒞_mono`, `𝒞_fin` and the dual completion. The thread records that scope.

## Verdict for integration
- **The framework's data construct a consistent pair system, K_gen**, for a consistent native set: (even, even), or σ K_gen for (odd, odd).
  - It has finite rank and LT, CONDITIONAL on INV2 (abstract carrier) or built in (table rule).
  - It is gate-compatible by construction.
  - All of its generated states and tests lie in Q3, and four-copy coherence holds on all of them [W].
- **The required state space (Q3, IE1, FCC) is INDEPENDENT of L**, witnessed by the K_gen system.
  - It is unreachable by every construction class examined that excludes frame-moving local operations on entangled states: exact for `𝒞_nat`; [W + L] for `𝒞_mono` and `𝒞_fin`.
  - A non-flagged source in general is UNRESOLVED.
- **Exposed, and shared with S3:** what separates K_gen from Q3 is no-restriction. The full dual `K_E = dualW K_gen` (= S3's `K_gen*`) contains effects such as F and E0 that no data generate. FCC excludes K_gen only through them.
- **Evidence levels.**
  - [K]: `cnot`, its frame, relT, relC and positivity; `NativeGate`; `IsNot.invol`; COMP-1 and StageCompletion.
  - [D]: the theorem and the consumption sites.
  - [W] and [W + L]: Theorems M and F, the clock pigeonhole step, FC.
  - [X]: instance-scoped.
  - The Lean in §1 is UNBUILT.
- **Bands:** unchanged. This is consistency-axis work.
