# EQ4-F — running notes (formalization package; design only; base `bcbc516f`, read-only at `scratchpad/eq/base/`)

Scope: the EQ4-F section of `scratchpad/eq4/PROTOCOL.md` (frozen; not edited). Writes only inside
`scratchpad/eq4/F/`. No Lean toolchain: every Lean text here is UNBUILT. No git writes, branches, pushes, PRs, CI,
freezes, ROADMAP or manuscript edits, premise adoption, or spawned agents.

## N0. Integrity at start (2026-10-09 04:01 UTC)

- `cd scratchpad/eq/base && sha256sum -c --quiet ../base.manifest.sha256`: silent, exit 0.
- `/home/user/incompleteness`: `git status --porcelain` empty (0 lines); HEAD
  `bc3bf9bc846c138de5f5b45f386a75244da4f21f`.
- `scratchpad/eq4/F/` existed and was empty; `.start_marker` created (mtime 2026-10-09 04:01:04 UTC) for the
  end-of-thread write check. `scratchpad/eq4/P/` exists (the sibling thread's directory; not read, not written).

## N1. Reading (all read in full unless noted; nothing modified)

- `eq4/PROTOCOL.md` (EQ4-F section, vocabulary, settled facts, limits).
- `/home/user/incompleteness/AGENTS.md` (§A.34 directional witnesses, §A.35 registry contract, claim/evidence
  boundary, §A.32/§A.33 register, §A.36 placement, §A.39 native rounds, §A.40 where verification runs).
- `eq3/P/RESULT.md`, `eq3/P/NOTES.md`; probe outputs p1–p6 and `run_all.out` (hashes re-computed: equal to RESULT §7).
- `eqreview/EQ3-AUDIT.md`; `eqreview/audit_eq3_n1.py` and its `.out` (29/29; sha `d9b504a45f74c5a5` / `f944cd932a66f149`,
  replay `.out` identical).
- `eqreview/EQ2-SYNTHESIS.md` (Theorem C, Theorem E).
- `eq2/A/EQ2A.candidate.lean`, `eq2/B/TheoremAPrime.candidate.lean` (UNBUILT designs; read for naming alignment:
  `pauliW`, `Q3`, `twin`, `transposeW`, `swapW`, `IsConvexCone`, `NormPres`, `ctrlGate_classification`).
- Base Lean (paths under `verification/lean-mathlib/OIBridge/`), lines verified by reading:
  - CompositeDimension (CD): `HVec` 93, `W` 97, `hom` 100, `homMap` 112, `prodState` 161, `pairVal` 164, `ehom` 167,
    `prodEffVal` 182, `maxCone` 186, `jointStates` 190, `IsProduct` 194, `actT` 198, `actC` 201, `corner` 205,
    `IsNot` 210, `NativeGate` 218 (fields frame/posFwd/posInv/relT/relC 220–225), `Entangling` 229, `toOp` 406,
    `actT_actT` 471, `actC_actC` 476, `sum_univ_four'` 731, `sgn` 741, `pc` 744, `pt` 751, `cnotFun` 758,
    `cnot` 775, `cnot_symm_apply` 790, `z3` 793, `nflip` 797, `actT_apply` 828, `actC_apply` 831,
    `prodState_apply` 834, `isNot_nflip` 838, `cnot_frame` 848, `cnot_relT` 854, `cnot_relC` 860, `Lor` 869,
    `lor_ehom` 930, `cnot_prodState_mem_maxCone` 1152, `nativeGate_cnot` 1160, `xplus` 1213, `phiW` 1220,
    `cnot_prodState_xplus_z3` 1222, `tens` 1450, `lor_eq_zero_of_head` 1576.
  - CompositeInterface (CI): `unitEff` 78, `affine_expand` 130, `BoundedAffine` 139, `exists_effect_rescale` 148,
    `exists_effect_neg` 171, `ProductData` 210 (`prodEff` 216, `prodEff_apply` 217), `PreComposite` 223
    (`convex` 226, `prod_mem` 227, `prodEff_effect` 228–229, `prodEff_unit` 230), `LocallyTomographic` 235,
    `Composite` 243 (`lt` 245), `condA` 259, `prodEff_eq_of_eff_eq` 342, `condA_mem` 431 (hypotheses `IsCompact ΩA`,
    `Convex ℝ ΩA`), `JointReversible` 445, `subset_maxBody` 467, `isEffectOn_maxBody` 545, `Model.Carrier` 579,
    `Model.modelData_ext` 740.
  - KInfFoundations (KF): `IsEffectOn` 116, `fullEffects` 149, `ball3` 311.
  - OrbitGeneration (OG): `seedTransport` 49, `PreservesBody` 69 (both `g x ∈ Ω` and `g.symm x ∈ Ω`),
    `isEffectOn_seedTransport` 94.
  - OrbitNormalization (ON): `words` 53, `driveWords3` 571, `rotX` 581, `euler_apply_pole` 589,
    `exists_euler_angles` 614, `exists_word_pole` 658.
  - K2Guard (K2G): `reflY` 46, `reflY_reflY` 73, `det_reflY` 78, `CandidateCone` 95 (products ⊆ K ⊆ maxCone; no
    convexity), `idW` 101, `chainW` 104, `actT_reflY_phiW` 106, `cnot_idW` 110, `no_candidateCone_cnot_reflY` 143,
    `prodState_mem_maxCone` 165, `actT_prodState` 173.
  - RelcSelectBlock (RSB, namespace `RelcSelect`): `CtrlGate` 45 (frame/posFwd/posInv/relC 47–51),
    `ctrlGate_of_nativeGate` 53, `dim_of_ctrlGate` 739, `three_of_ctrlGate` 753.
  - EffectSpace (ES): `sharpVec` 57, `sharpEff` 65, `sharpFamily` 72, `sharpEff_isEffectOn` 97, `maxConeOf` 411,
    `prodEffVal_sharp` 514, `maxConeOf_sharpFamily` 549, `MixingClosed` 591, `not_fullEffects_of_orbit` 762.
  - TransitiveBody (TB): `eball` 518, `mem_eball` 520. MonoidalCompletion: `tensorOf` 193.
  - SpectatorBridge (SB): `IsSpectatorExtension` 180, `isSpectatorExtension_iff` 188,
    `InertSpectatorCompositionality` 223, `inertSpectator_iff_parallelReferenceExtension` 233.
  - CarrierGeneralOIPlus (CGOP): `ObservationalIndependence` 73, `OIPlus` 185, `oiPlus_iff_qm` 207.
  - Absent at the base (grep, whole `OIBridge/`): `transposeW`, `pauliW`, `coordsW`, `FourCopy*`, any carrier with three
    or more copies. Name collision noted: `Adm` exists (ClosureObstruction:78), so the package uses `PairAdm`.
- Census registry `verification/lean-manuscript-census.json` (read with `python3 -I -B`, json only): every OIBridge
  module must belong to a family with a disposition; the analogous modules (CompositeInterface, CompositeDimension,
  EffectSpace, K2Guard, RelcSelect*) are `kernel-only`.

## N2. Node: exact identity checks for the package (`f1_package_identities.py`)

Written before any run, decision rule in the header (rules, not expected numbers); own code, imports nothing from
`eq2/`, `eq3/` or `eqreview/`; kernel conventions typed by hand and re-parsed from the base text (K0, K1).
- Purpose: give [X] support to the statements the package introduces beyond EQ3/audit evidence:
  - R1–R4: the four target relabellings of the four-copy contraction (used to instantiate one core lemma four
    times); R5 countercontrol (transposes dropped).
  - W1–W4: the cone-level reading of H-KT4 on the 256-entry carrier, both cross-grouping values, token coherence of
    the W4 model, and its countercontrol (a transposed 02 factor breaks it).
  - C1–C4: `cnot'` (twin gate) identities used by the aligned form: involution, orthogonal/symmetric, unit fixed,
    twin Bell table, frame/relT/relC (so `cnot'` satisfies the table identities of `NativeGate`), positivity
    reduction to `cnot`.
  - B1–B2: aligned parity from gate-supplied Bell data only (states `cnot^τ` of the four corner products, effects the
    dual images of the corner sharp products).
  - G0–G3: general charts — orientation rule for the Bell state (det A det B), the Θ-parity bookkeeping over all 16
    determinant patterns × 2 draws, and the pre-local countercontrol.
- Run 1 (2026-10-09 04:25 UTC): 21/21, `VERDICT F1-PACKAGE-IDENTITIES-EXACT`, stderr empty (the `.err` holds only
  the appended `exit=0`). Replay (04:26): byte-identical (`cmp` silent).
  - sha256 (first 16): `.py` `8338e4ec8b1cf258`, `.out` `9d80e6dad860f242`, `.replay.out` `9d80e6dad860f242`.
  - Tools: Python 3.11.15, sympy 1.14.0. Runtime ≈ 13 s.
- Reading of the outputs:
  - B2 minima (table normalization; the log prints `m1/m2` with `/` also inside the fractions, so `-1/8/-1/8`
    means m1 = −1/8, m2 = −1/8): negative exactly at the eight odd patterns, 0 at the eight even ones; the pattern
    list matches audit P1 and EQ3 p2 Z2 in the same pair order (01, 23, 02, 13).
  - G1: post-locals with det A det B = +1 give a Bell state in Q3 and not in Tw; −1 gives Tw and not Q3.
  - G2: consistency of Θ(C23) with C01 holds exactly at even det-parity; G3: pre-locals (N's own dual) give the
    opposite verdict when their determinant product differs on one link pair, so the inverse's dual (post-locals)
    is substantive, as audit G5 found.
- Status: consistency-axis evidence for the package statements; nothing kernel-checked.

## N3. Node: explicit parity witnesses and the chart reduction (`f2_parity_witnesses.py`)

Written after N2, decision rule in the header before its first run; own code (imports nothing from f1 or other
threads). Purpose: concrete data for the cheap aligned-parity lemma of the Lean design.
- X1: a reflection chart at the first token also turns `cnot` into `cnot'` (symbolic); countercontrol with `nflip`.
- X2: every even pattern is a coboundary τ_ij = ε_i + ε_j and the per-token reflection chart conjugates each aligned
  gate to `cnot` (symbolic); no ε for odd patterns (exhaustive). Charts found: 0000→0000, 0011→0011, 0101→0001,
  0110→0010, 1001→0100, 1010→0111, 1100→0101, 1111→0110 (τ in pair order 01,23,02,13; ε in token order 0..3).
- X3: for every odd pattern the first witness in lexicographic order is the same index choice in both families:
  family (i) X = S[0], Y = S[0], E = E[0], F = E[3]; family (ii) e = E[0], f = E[0], L = S[0], L' = S[3]; value −1/8
  in each case; no negative value for even patterns. (S[0] = gate image of prodState(xplus, z3), the Bell table;
  index 3 = the corner (−xplus, −z3), whose `cnot` image is the singlet table diag(1, −1, −1, −1).)
- Run 1 (04:31 UTC): 4/4, `VERDICT F2-PARITY-WITNESSES-EXACT`, stderr empty. Replay byte-identical.
  - sha256 (first 16): `.py` `b29e5f70333171b6`, `.out` `ca728faa79476868`, `.replay.out` `ca728faa79476868`.
- Hand check of one witness (τ = 0001, `cnot'` on 13 only): ⟨Δ, (Δ/4)·Δ·(diag(1,−1,1,−1)/4)ᵀ⟩
  = (1/16)⟨diag(1,1,−1,1), diag(1,−1,1,−1)⟩ = −2/16 = −1/8, agreeing with X3.

## N4. Design decisions, pressure tests and review fixes (FORMAL.md, FourCopyIE1.lean)

- Interface choice: `FourCopyCoherent` states both families in inequality form (no closedness, no bipolar inside the
  predicate). Membership forms (`L·f·L'ᵀ ∈ K01`) are derived later with H-closed or on closures.
- Lemma B2 (cone-level faithfulness) uses the maximal cone {Ω | effA ≥ 0 ∧ effB ≥ 0}; it needs no hull and no
  closure. Each direction has its own witness.
- Favourable observations, pressure-tested before writing them up (§A.31, maximum skepticism on favourable branches):
  - R-LT (four-copy `lt` not read). Walked the bridge route step by step:
    - families = product effects of one grouping evaluated on product states of the other;
    - values via token coherence, bilinearity of `prodEff` (CI:216), `prodEff_apply` (CI:217);
    - effect/table dictionary via boundedness and the vanishing lemma (H-eff).

    No step identifies a state from its product-effect values, so `lt` is not read. Countercheck: could token
    coherence be a consequence of `lt` plus one body? No — a twisted second product structure (one factor read
    transposed) gives two PreComposites (even Composites, since the twist is an isomorphism) on one body without token
    coherence. f1 W4 is the exact ingredient. So token coherence is a separate clause and `lt` does not supply it.
  - R-inv (H-inv on closures from H-gate and orthogonality). Argument:
    - N-CLASS gates are orthogonal for `ipW` (audit G1);
    - `N(cl K) ⊆ cl K` by continuity;
    - on the compact `cl K ∩ {‖ω‖₂ ≤ 1}`, N is an isometric self-map, hence onto, so `N⁻¹(cl K) = cl K`.

    The derivation reads H-inv only through `dualW K = dualW (cl K)`. Second argument (independent): powers of N in
    the compact group O(16) accumulate at the identity, so `N⁻¹` is a limit of positive powers, each preserving the
    closed cone. Mathlib lemma for the first argument not found (N5).

    Kept H-inv as a named hypothesis of A, C, D; recorded as [W] only.
- Scope care: H-pairwise is not read separately once the gate form (aligned) or H-NCLASS (general) is given;
  `kt4_forward` carries `hpair` unread and says so. The usage table in FORMAL §2 states this.
- Name collisions (second check, whole `OIBridge/`): every introduced name in FourCopyIE1.lean was grepped as a
  declaration. Zero hits except `IsRot` (QuarterTurn:233, `OIBridge.QuarterTurn.IsRot`, a permutation predicate),
  hence `IsRot3`. `Adm` (ClosureObstruction:78) was found at N1, hence `PairAdm`.
- Review fixes before finishing:
  - Lean: two wrong `ipW_comm` rewrites removed (in `incl_II` and `incl_II_aligned`);
  - FORMAL:
    - brief corrected to three precision points;
    - cross-reference for the circularity audit fixed (§6);
    - P_u in the remark now lists H-inv, H-NCLASS (general charts) and H-eff;
    - vocabulary list completed (`EvenCycle4`, `FCC`, `orient`, `blochOf`);
    - "R-F1 alone would kernel-check" (future tense: nothing is built).

## N5. Mathlib grep record (snapshot `scratchpad/ml-v433-src/m`, tag v4.33.0; grep only)

- Found (declaration line read in context): every entry of FORMAL §7 "Found". Among them:
  - `Matrix.IsHermitian.spectral_theorem` Analysis/Matrix/Spectrum.lean:141;
  - `Matrix.PosSemidef.kronecker` Analysis/Matrix/Order.lean:213 (same line EQ2-SYNTHESIS recorded);
  - `IsAlgClosed.exists_eq_mul_self` FieldTheory/IsAlgClosed/Basic.lean:90;
  - `geometric_hahn_banach_closed_point` Analysis/LocallyConvex/Separation.lean:231;
  - `ProperCone.hyperplane_separation_point` Analysis/Convex/Cone/Dual.lean:132;
  - `dense_pi` Topology/NhdsWithin.lean:421.
  - `Finset.sum_comm` and `Fin.sum_univ_four` are the `@[to_additive]` forms of `Finset.prod_comm` (Sigma.lean:120–121)
    and `Fin.prod_univ_four` (Fin.lean:123–124). The attribute lines were read.
- Not found (patterns tried):
  - Euler angles (`euler.angle|eulerAngle|euler_angle`, no file);
  - rotation maps in the quaternion files;
  - the compact-isometry surjectivity lemma (`isometry` with `compact` and `surj|onto|bij|range`);
  - a named rank-one form of the spectral theorem;
  - a named closedness lemma for PSD (`isClosed` near `PosSemidef`);
  - `interior_closure_eq_interior` (only `Convex.combo_interior_closure_subset_interior` and relatives exist).
- `ProperCone.innerDual_innerDual` (InnerDual.lean:107) needs an inner product space; `W 3` is a Pi type with the sup
  norm. The design therefore uses `geometric_hahn_banach_closed_point` directly (as CI:174 does) or
  `ProperCone.dual_flip_dual` with a continuous perfect pairing (Dual.lean:137).

## N9. Integrity at the end (2026-10-09 04:46 UTC)

- Base: `cd scratchpad/eq/base && sha256sum -c --quiet ../base.manifest.sha256` silent, exit 0; no `__pycache__`
  under the base.
- `/home/user/incompleteness`: `git status --porcelain` empty; HEAD `bc3bf9bc846c138de5f5b45f386a75244da4f21f`
  (unchanged); `git diff-index --cached --quiet HEAD` exit 0.
- Out-of-directory side effects:
  - No working-tree file is newer than this thread's start marker, and no file inside `.git` is.
  - The `.git` directory mtime moved to 04:46:43, the second of the final `git status --porcelain`. This is the
    transient `index.lock` that a read-only status creates and removes, the same effect EQ3 recorded at its N9.
    `.git/index` is unchanged (mtime 2026-10-07 00:26), and no lock remains.
- Scratchpad: no file outside `eq4/F/` is newer than the start marker. In particular nothing in `eq4/P/`, `eq3/`,
  `eqreview/`, `eq2/` or the base was written. Every file this thread wrote is in `eq4/F/`; no `__pycache__` there
  (all runs `-B`).
- Final hashes (first 16 hex of sha256):
  - 70d454f8873d9cc5  FORMAL.md
  - d548fc7bbda363d5  FourCopyIE1.lean
  - 8338e4ec8b1cf258  f1_package_identities.py
  - 9d80e6dad860f242  f1_package_identities.out
  - b29e5f70333171b6  f2_parity_witnesses.py
  - ca728faa79476868  f2_parity_witnesses.out
- NOTES.md is the last file written (this entry), so it carries no hash of itself.
