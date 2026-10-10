# EQ3-P audit (coordinator; research only, base `bcbc516f`)

The audit was run against the frozen protocol (`eq3/PROTOCOL.md`, Amendments 1 and 2) and the owner's checklist
(`EQ3-AUDIT-CHECKLIST.md`). Nothing is adopted, frozen or governed. No round was opened, and no ROADMAP or manuscript
file was edited.

Evidence tags:
- [X] exact computation, replayed byte for byte;
- [W] written argument;
- [L] literature, unverified;
- [K] landed kernel identifier.

## 0. Verdict

**Two copies (IE₁): the thread's positive result stands.**
- At the instance KT(4; 01|23, 02|13), each pair cone is Q3 or the twin in its token charts, so IE₁ is derived and not
  postulated.
- My independent exact code reproduces every identity the route uses, in operator form and with its own conventions
  (29/29).
- I replayed all eight of the thread's scripts; every output is byte-identical.
- The route is [X + W]: exact identities, plus a written assembly (density, spectral theorem, Euler decomposition,
  closure). Nothing is kernel-checked.

**Three copies (IE₂): open, as the thread reports, with one qualification it did not state.**
- The exclusion of `M_bs`, the GHZ dichotomy and the wall's "co-self-dual K₃" form all take both triples of the
  six-copy instance to carry the same cone: uniform composition at the triple level.
- Without that assumption, the families the thread derives do not exclude the non-uniform pair (BS*, BS) (§5b).

**Precision points:**
- one implicit premise in arbitrary charts (§5a);
- one unused lever at six copies, which relocates the wall rather than closing it (§5c);
- one wording fix (§5d).

## 1. What was checked

**Replays.**
- I copied the thread's scripts into `replayEQ3/` and re-ran them with `python3 -I -B`.
- p1–p6 and x1–x2: 8/8 byte-identical, stderr empty. The hashes match RESULT §7.

**Independent exact code.** It imports nothing from `eq3/P`. The kernel tables are typed in by hand and re-parsed from
the base text as a control. All four-copy and six-copy contractions are computed as explicit operators, not in the
thread's table calculus, and the table formulas are then checked against the operator results.

- **`audit_eq3_n1.py`: 29/29, `AUDIT-EQ3-N1-EXACT`, replay identical.**
  - Run 1 (kept as `.run1.*`) scored 28/29. G3 failed from a harness error of mine: `sharpVec` divided Python
    integers, so floats leaked in.
  - Fixed with exact division and an explicit no-Float guard. The decision rules were not changed.
- **`audit_eq3_n2.py`: 13/13, `AUDIT-EQ3-N2-EXACT`, replay identical.**
  - Run 1 (kept) scored 12/13. B1 failed from a harness error of mine: I wrote the Lagrange identity in its sesquilinear
    form, but `⟨GHZ|a ⊗ χ⟩` is bilinear and needs `|a₀χ̄₁₁ − a₁χ̄₀₀|²`.
  - I checked the correction separately before the rerun. The bound under test did not change.

**Integrity.**
- The base manifest holds: 1317/1317 files, exit 0, no `__pycache__`.
- The repository is clean at `bc3bf9bc` and the index is unchanged.
- Every scratchpad file written since the thread started is accounted for: the thread's files in `eq3/P`, mine in
  `eqreview`, plus the coordinator's protocol.
- The only stray artifact was the `__pycache__` my own `py_compile` calls created; I removed it.

## 2. The four checks

1. **Both inclusions, for the whole cone: yes.** Both are linear identities in the cone elements [X I1, I2, symbolic],
   and in arbitrary charts [X G4].
   - (II) `K₀₁ ⊆ Θ(K₂₃*)` needs no closedness.
   - (I) gives `Θ(K₂₃*) ⊆ cl K₀₁` without closedness, and `⊆ K₀₁` with it.
   - So `cl K₀₁ = Θ(K₂₃*)` holds relative to base + KT(4) with no closedness at all.
   - The classification also goes through on closures: `cl K_ij ∈ {Q3, Tw}`.
   - Closedness is used only to pass from the closures to the cones themselves. The foil
     `int Q3 ∪ conv(SEP ∪ cnot SEP)` shows that step cannot be skipped.
2. **Effect availability: settled at the base, in favour of the full dual cone.**
   - COMP-1's `prodEff_effect` [K CI:227] quantifies over `IsEffectOn` functionals [K KF:116]. These are all affine
     maps with values in [0, 1] on the body.
   - The derivation uses only positivity of products of such functionals on the joint body. It never uses that a
     measurement is available.
   - So the quantifier is `K₂*`, not `E₂⁺`, and the route obtains `T(K₂*) ⊆ K₂`. EFF-1's Q-SET conditionality does not
     enter.
   - The full-effect reading is load-bearing: with effects restricted to Q3, `K_F` passes [p2 F3].
   - This makes KT a no-restriction-type principle for regrouped composites. That content belongs to KT/COMP-1, not to
     an added availability assumption.
3. **Four-copy consistency: one coherent K₄.**
   - One carrier and a fixed token order; the regroupings are index reshuffles. I assemble the 16 × 16 operators
     explicitly and recover both table formulas [X O1–O3].
   - Local tomography of the regrouped composites (COMP-1 `lt`) is part of KT. The thread records it as an unsourced
     n-copy transport.
4. **No circularity: confirmed.**
   - Every step is (s) or (2). The (2) steps are the standalone pair gate, and in arbitrary charts its inverse (§5a),
     acting on product states and product effects of standalone pairs.
   - No (o) step occurs, at four copies or at six.

## 3. Level of success and the outcome table

**Milestone 1, co-self-duality: level 2, conditional.**
- **Named assumptions:**
  - KT(4) itself. It is the principle under test and is not at the base, which rules out level 3.
  - Closedness, which enters (I) only.
- **Not used:** uniform composition. The instance gives the cross-pair relation `K₀₁ = Θ(K₂₃*)`, and each pair is
  co-self-dual once classified.
- **No added effect assumption.**
- On closures the result is unconditional relative to base + KT(4).

**Milestones 2 and 3 (selection, IE₁): outcome 1, "coherence alone selects the quantum cone".**
- The twin is the per-pair alternative, fixed by the orientation of that pair's gate.
- **Given:**
  - the transported two-copy premises on every pair: an admissible convex body, the native gate and its inverse as
    standalone operations, and N-CLASS in arbitrary charts;
  - closedness;
  - COMP-1's effect quantifier.
- "Alone" means without uniform composition and without an extra finite symmetry.
- The gate is load-bearing: SEP and max satisfy KT(4).
- I agree with the thread's placement.

**Milestone 4 (IE₂):** none of the five outcomes.

## 4. Sufficiency, insufficiency, necessity (the owner's P/A/C rule)

- **Sufficiency.** `P ∧ KT(4) ⇒` IE₁ ∧ even 4-cycles [X + W, the thread's route].
- **Insufficiency.** Each foil is a model of `P′ ∧ ¬C`, where `P′` drops one premise. Each shows that the premise
  cannot be dropped without a replacement; none shows necessity.
  - `C_H` and `K_F`: the two-copy premises do not imply KT(4). Re-derived in my own code: order 8, max norm² 45/49,
    value −1/200.
  - SEP and max: the gate is load-bearing.
  - The closure foil: closedness is load-bearing.
  - Restricted effects: the full-effect reading is load-bearing.
  - The thread's ledger header "independence / necessity evidence" should read "independence (insufficiency)". The
    thread's text claims no necessity.
- **Necessity of KT(4) relative to the two-copy premises (new in this audit).**
  - **Uniform pair cones (`P_u`):** `P_u ∧ IE₁ ⇒ KT(4)`.
    - IE₁ + gate + admissibility ⇒ K ∈ {Q3, Tw} (EQ2 cone selection [X+W]).
    - Uniform Q3 is realized by PSD₁₆, and uniform twin by `PT_{{0,3}}(PSD₁₆)` [X P2].
    - So relative to `P_u`, **KT(4) ⟺ IE₁**, with a separate witness for each direction (§A.34).
  - **Without uniformity:** KT(4) ⟺ IE₁ ∧ every 4-cycle of twist bits even.
    - IE₁ alone does not imply KT(4). Take Q3 on (01), (23), (02) and the twin on (13). This satisfies P and IE₁ on
      every pair and violates KT(4) (value −2 [X P1]).
    - So KT(4) is strictly stronger than IE₁ by exactly the parity constraint.
- **Answer to the decisive question at two copies.** Given the standalone pair gate, state-level coherence of the two
  groupings is equivalent to single-token idle extension, plus 4-cycle parity when pair cones may differ.

## 5. Findings

**(a) Arbitrary charts: inclusion (II) uses the inverse gate.**
- The thread's §1.3 derives the Bell effect for the aligned gate only, where `cnot` is self-adjoint. Its general-chart
  checks U1–U2 test only the state side.
- In arbitrary charts, the Bell effect that induces the same identification Θ as the Bell state is the dual image under
  `N⁻¹`. N-CLASS gates are Euclidean-orthogonal, so `(N⁻¹)ᵀ = N` [X G1–G3].
- Through `N`'s own dual, the Bell effect is `ℓ₂ᵀ(Δ)/4`, built from the pre-locals. For `N = (reflY ⊗ 1)∘cnot` this has
  `det R′ = −1`, while the Bell state has `det R = +1` [X G5].
- The conclusion is unaffected. The premise used is reversibility of the standalone gate (`posInv`), a (2)-type premise
  already in `CtrlGate`.
- It should be listed in the ledger and the step tags.

**(b) Six copies: triple-level uniformity is presupposed.**
- KT(6) gives the cross-triple relation `K₀₁₂ = T₃(K₃₄₅*)` [X S3, S4].
- The exclusion of `M_bs` (−1/16, reproduced [X B2]), the GHZ dichotomy T6, and the "co-self-dual K₃" form of the wall
  all take both triples to carry one cone in a shared chart.
- The non-uniform pair (BS*, BS) satisfies every family the thread derives, both inclusions in both role orders and the
  filter conditions [W]:
  - BS and BS* are closed under local CP maps and under T₃;
  - BS* is the maximal admissible three-token cone, with Q3 pair marginals.
- The −1/16 witness `½ − GHZ` is then not an effect of the triple (0,1,2): it has eigenvalue −½, so it is not in BS
  [X U1].
- So the exclusions hold for the uniform models `M_bs`, `M_tw`, `M_odd` as defined. A wall stated without uniformity
  must handle cross-related pairs of triple cones.
- This is Amendment 2's uniformity point, appearing at three copies. Two copies avoided it because each pair's own gate
  pins its cone from below; no three-token gate does that for a triple.

**(c) Six copies: an unused lever, which relocates the wall.**
- The thread's six-copy families use only products of link-pair effects. KT(6) also gives the four-token group
  (1,4,2,5) its full effect set.
- If that set contains the CNOT Choi effect `Ad(CNOT₁₂)(Ω₁₄ ⊗ Ω₂₅)`, the instance requires
  `⟨x, Ad(CNOT)(yᵀ)⟩ ≥ 0` for every x in K₀₁₂ and y in K₃₄₅ [X U2, exact identity on three instances].
  - The effect is present whenever that group's cone lies in PSD₁₆.
  - With `K₀₁₂ = T₃(K₃₄₅*)`, that condition is exactly `Ad(CNOT)`-invariance of K₃₄₅ on a pair: **IE₂ for cnot**.
  - It also excludes (BS*, BS), at value −½ [X U2].
- Sourcing the Choi effect needs either an upper bound on the four-token cone or effect-level idle extension at four
  tokens, which is (o)-type. The thread's no-generation lemma rules out building it from pair-level data.
- So the three-copy wall follows from a four-token statement: **it moves up one level and is not closed**. This
  refines the thread's reading that KT∞ could imply IE₂ only "through its fixed point at every level".

**(d) Wording.** In the ledger header, "necessity" should read "insufficiency" (§4).

**(e) T6.**
- The ← direction needs the GHZ class to be one SLOCC orbit, dense among pure states. Density holds because the class
  is the complement of the hyperdeterminant hypersurface. Being a single orbit is the Dür–Vidal–Cirac classification
  [L].
- My code confirms the hyperdeterminant's values and its SLOCC covariance [X Y].
- The upper bound `K₃ ⊆ PSD₈` again uses triple-level uniformity (b).

## 6. Effect on the EQ2 theorem statements (design note; nothing adopted)

- **Theorem C, premise (I):** IE₁ could be replaced by KT(4; 01|23, 02|13) on every four-token family, plus closedness,
  plus the inverse gate as a standalone operation in arbitrary charts. That trades an operation-level premise for a
  state-level one.
- IE₂ and H0 remain named premises. Theorem E is unchanged, since KT is not at the base.

## 7. Evidence log (sha256, first 16 hex digits)

| file | sha | outcome |
|---|---|---|
| `audit_eq3_n1.py` | `d9b504a45f74c5a5` | 29/29 `AUDIT-EQ3-N1-EXACT`; `.out` `f944cd932a66f149`; replay identical |
| `audit_eq3_n1.run1.py` / `.out` | `316876fcf7118a41` / `044007b9641b71a2` | 28/29, harness error (floats), kept |
| `audit_eq3_n2.py` | `e8b116f0ee0602d4` | 13/13 `AUDIT-EQ3-N2-EXACT`; `.out` `ed1439b967ebaa6f`; replay identical |
| `audit_eq3_n2.run1.py` / `.out` | `58b49c90391c5888` / `ecd8a42c49617e0a` | 12/13, harness error (Lagrange form), kept |
| `replayEQ3/replay.log` | — | p1–p6, x1, x2: 8/8 identical; hashes as RESULT §7 |
