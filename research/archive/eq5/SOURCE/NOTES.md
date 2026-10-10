# EQ4-SOURCE — running notes (research only; nothing adopted, frozen or governed)

Thread directory: `scratchpad/eq5/SOURCE/` (the only place this thread writes). Protocol: `scratchpad/eq5/PROTOCOL.md`,
section "EQ4-SOURCE" (read in full; not edited). Base: certified main `bcbc516f`, snapshot `scratchpad/eq/base/`.
Inputs: `scratchpad/eq5/inputs/` (the preflight package at `f0d37906`). No Lean toolchain: every Lean text is UNBUILT.

## N0. Start (integrity)

- `cd scratchpad/eq/base && sha256sum -c --quiet ../base.manifest.sha256`: silent, exit 0 (1317 entries).
- `cd scratchpad/eq5/inputs && sha256sum -c --quiet ../inputs.manifest.sha256`: silent, exit 0 (6 entries).
- Repository HEAD (read-only git): `f0d37906a83585efdaca8e3ee3404410e869c43e` on `claude/network-tool-access-8jtdhm`;
  `git status --porcelain` empty. Reflog top: `f0d37906 HEAD@{0}: commit: EQ4-F preflight (design only, not for merge)`.
- `.start_marker` written (UTC timestamp, HEAD, both manifest results).

## N1. Reading log (what was read, and why)

- Protocol (whole file); AGENTS.md RULE sections, §A.19, §A.31, §A.34 (in the session context).
- Inputs: `FourCopyPackage.lean` (whole), `FourCopyDefs.lean` (whole), `FourCopyParity.lean` (whole),
  `PREFLIGHT-LEDGER.md`, `PREFLIGHT-RESULT.md`.
- `eq4/F/FORMAL.md` (whole; §2 ledger, §3 B1 route, §6 skeleton), `eq4/F/NOTES.md` N4 (R-tok), `eq4/F/f1_*.py` header and
  output (W1–W4 are functional identities; W4 is a countercontrol on a functional, not a model).
- Base kernel: `CompositeInterface.lean` (whole), `CompositeDimension.lean` §A–§B, §K (cnot tables), `K2Guard.lean`
  §A–§D, `RelcSelectBlock.lean` §A, `KInfFoundations.lean` §B (`IsEffectOn`) and `CopyNatural`, `StageCompletion`
  (`body` = closed convex hull, SC:141–142), `RegionTower` declarations (complex-matrix types).
- Base records: ROADMAP P1-K (lines 971–1102, incl. K1, K2, K∞, Kₙ); round results COMP-1, ORD-1, EFF-1, K1-BRIDGE-1,
  K2-GUARD-1, K1-SHARP-TESTS-1, KTRANS-DENSE-1, NB-1, RELC-SELECT-1, PARITY-NOT-1, ODD-CHAR-1; audit
  `audits/foundations/kn-elementary-carrier-census.md`; `papers/Main.md` (axiom statement, posit ledger, §3.4
  operational-lifting passages, conclusion).
- Scratchpad records: `kn/KN-CENSUS-RESULT.md`, `k-infinity/K-INF-DESIGN.md` (grep), `k2d/K2-LEDGER.md` (whole),
  `sa/SA-LEDGER.md` (§0, §1, §5), `eqreview/EQ2-SYNTHESIS.md`, `eqreview/EQ3-AUDIT.md`, `eqreview/EQ4-AUDIT.md`,
  `eq2/B/RESULT.md` (N-CLASS rows), `eq3/PROTOCOL.md` (KT∞ statement, Amendments 1–2), `eq4/P/RESULT.md` §0.

## N2. Search log (§A.19: before any "not supplied" claim)

All searches read-only over `scratchpad/eq/base/` (paths below relative to `verification/lean-mathlib/OIBridge/` unless
stated); the exact ones are re-done inside `s0_census.py` and `s2_pair_premises.py`.

- `PreComposite|ProductData|LocallyTomographic|SharpReadout`: only `CompositeInterface.lean` (s0 Q1b). Other hits of
  "Composite" (`exactComposite`, `fullComposite`) are matrix-world `FiniteOperationalTheory` objects.
- COMP-1 values: `minPre`, `maxPre`, `minComposite`, `maxComposite`, `bitComposite`, `ball3MinComposite`,
  `ball3MaxComposite`, `paddedPre`, `paddedBall3` — all with one-copy factor bodies (s0 Q1d).
- Carriers with >= 3 chained `Fin` binders: none on the field-neutral side (18 modules); `HydroSourceAudit` has
  `Fin 3 → Fin 3 → Fin 3 → Fin 3 → ℝ` tensors (hydrodynamics, unrelated, not judged) (s0 Q1c).
- `FiniteStage.prod`, `DirectedStages.prod`, `stageProd`, `LocalExt`, `JointTower`, `TokenCoherent`,
  `FourCopyCoherent`, `NClass`, `ctrlGate_classification`, `PairAdm`: absent (s0 Q1e). `DirectedStages` values: only
  the controls `badD`, `bitTower` (StageCompletion), `midD` (CompletionAction) (s0 Q2a).
- Import graph: no path in either direction between the field-neutral composite core and the complex region /
  operational core; no module other than the aggregator reaches both (s0 Q1a). Region tower types are
  `Matrix (Conf Λ Q) (Conf Λ Q) ℂ` (RT:123, RT:128; s0 Q2b).
- `associat|braid|monoidal`: hits are matrix-world (`ReferenceExtension` reindexing `R × (A × Fin n) ≃ A × Fin m`;
  `LieRing.ofAssociativeRing`; `ProjectiveAction` cocycle; `MonoidalCompletion`, whose `tensorOf` is on
  `Matrix A A ℂ`, MC:193, and whose H_comp / H-tensor is the matrix-world spectator principle).
- `token`: Main.md Axiom 1 ("tokened differentiation", a concrete particular of registered content, Main.md:38) and
  ROADMAP:1029, :1078 (K∞-Copy's "type covariance of native inversion ... rather than by token"). No composite-level
  token identity anywhere. `KInfFoundations.CopyNatural` (KF:284) identifies two copies' NOTs only.
- Manuscript status of composition: Main.md:82 ("(4) Full operational extension ... requires the additional
  operational-lifting and composition hypotheses stated in §3.4"), :212 and :628 (kinematic locality does not prove
  local tomography, statistical product structure, or one common tensor-product instrument category), :534
  ("exact coherent/composite compatibility is the residual operational-lifting problem"). Posit ledger (Main.md:706)
  lists no composition posit.
- Records: COMP-1 result:53 ("constructs no composite larger than the minimal body from any source"), :102–106 (open:
  "the stage-level product of two towers and its completion"); CompositeInterface header CI:5 ("a structure over V,
  not a construction"), CI:54–55 (stage product and the bridge from product towers "not part of this module");
  K2Guard header K2G:27 ("Nothing here sources a cone"); K2-GUARD-1 result:39; KTRANS-DENSE-1 result:59 ("does not
  concern whether the composite cone is closed"); ROADMAP K1 :984–1000, K2 :1001–1006, K∞ :1007–1057, Kₙ :1058–1069,
  route :1081–1093; landed audit `audits/foundations/kn-elementary-carrier-census.md` §1–§2.
- Mathlib checkout `/home/user/leanprover-community/mathlib4` is at `db584cd6`, tagged `v4.33.0` (read-only
  `git rev-parse`); anchors: `Matrix.vecCons` Data/Fin/VecNotation.lean:59–60, `finProdFinEquiv`
  Logic/Equiv/Fin/Basic.lean:334, `Matrix.PosSemidef.kronecker` Analysis/Matrix/Order.lean:213,
  `PosSemidef.conjTranspose_mul_mul_same` LinearAlgebra/Matrix/PosDef.lean:313; base `psd_trace_mul_nonneg`
  OperationalRigidity.lean:917.

## N3. Scripts, pre-run edits and runs (all `python3 -I -B`, run from `scratchpad/eq5/SOURCE/`)

- `s0_census.py <base>/…/OIBridge <eq5>/inputs`.
  - Pre-run edits (before run 1): Q1c restricted to the field-neutral side (the draft would have judged unrelated
    three-index tensors elsewhere); Q1d's signature parser rewritten to work declaration by declaration.
  - Run 1 (kept: `s0_census.run1.{py,out,err}`): 12/12 and verdict rendered, but the Q1d listing wrongly included the
    predicate `LocallyTomographic` (its binder `(P : PreComposite ΩA ΩB V)` matched). No check changed by it.
  - Fix: the declared type is the text after the last colon at bracket depth 0; the field-neutral module list is
    printed. Run 2: 12/12, `VERDICT S0-CENSUS-NO-MULTICOPY-STRUCTURE`, 9 COMP-1 values.
- `s1_kt4_models.py <base>/…/OIBridge`.
  - Pre-run edits: an explicit Kronecker product replaced `sympy.kronecker_product` (may stay unevaluated); R5's last
    clause (vacuous as drafted) replaced by the explicit witness values E = phiW/4, F = dg(1,−1,1,−1)/4 (header text
    updated accordingly); the countercontrol comparison made explicit, and `nsimplify(rational=True)` replaced by
    `sympify` so that the no-float guard cannot be bypassed.
  - Run 1: 35/35, `VERDICT S1-KT4-WITHOUT-TOK-MODELS-EXACT`.
- `s2_pair_premises.py <base>/…/OIBridge <mathlib4 root>`.
  - Run 1 (kept: `s2_pair_premises.run1.{py,out,err}`): harness error after 8 passing checks — `skron` assumed square
    matrices and was applied to column vectors (IndexError); no verdict printed.
  - Fix: rectangular Kronecker. Run 2: 11/11, `VERDICT S2-PAIR-PREMISE-CORES-EXACT`.
- `e1_stmc_twist.py` (exploration, a lead): run 1: controls c1–c3 pass, value −1/4, `LEAD STMC-TWIST-EXCLUDED`.

## N4. Productivity test (§A.31) and the depth-first walk

Productivity test (fixed before the branch walk below; the scripts' rules were fixed earlier in their headers): a
finding is a gem iff it is strictly stronger than "premise X is unsourced" and either decides a premise's class with an
exact route or countermodel, or exposes an assumption hidden in how a premise or the setting is stated. Otherwise it is
record-only. Favourable branches (those that would let the architecture supply something) get maximum skepticism.

- B1 (Q1) any carrier/composite with >= 3 copies at the base? Check: s0 (12/12). Verdict: none. CONFIRMING (ROADMAP
  K2/Kₙ OPEN; Kₙ census).
- B2 (Q2) is TokenCoherent supplied?
  - B2.1 composition coherence: COMP-1 is two-factor, no composite-as-factor value, no associator or symmetry (s0
    Q1b, Q1d). Absent. CONFIRMING.
  - B2.2 token/site identity: present only in the complex region tower (complex-matrix types; disconnected from the
    ball side, s0 Q1a, Q2b); `CopyNatural` concerns NOTs. A route through either imports `Matrix _ _ ℂ` (the quantum
    cone) and, for H_comp, an operation-level spectator principle ((o)-type). Absent in field-neutral form. CONFIRMING.
  - B2.3 protocol tower: no product or joint tower; only three control towers (s0 Q1e, Q2a). Absent. CONFIRMING.
  - B2.4 is KT4 without `tok` a model of the stated premises, and does the headline survive? Check: s1 R1–R6, T1–T5,
    P1–P7, A1–A3. Verdict: M_rho and M_tw satisfy every other hypothesis of `kt4_forward` (and `lt`), and its
    conclusion fails (forced odd twist pattern; −1/8). The minimal-form KT4 minus `tok` is satisfiable for every
    quadruple of nonempty pair bodies (anchor sum). **NEW** (EQ4-F R-tok had: tok is a separate clause; it did not
    show that the remaining fields carry no four-token content or that the headline fails without it).
  - B2.5 favourable-branch pressure test: could four-copy `lt` (both groupings) supply tok? No: M_rho, M_tw have `lt`
    for both groupings [W from CI:750/753 + bijection]. CONFIRMING (EQ4-F N4).
  - B2.6 what exactly is tok's content? Routes [W]: FCC ⟺ ∃ KT4 (for PairAdm cones), each direction with its own
    witness; tok ⟺ TokProdState relative to KT4-without-tok + `lt` of PA + CandidateCone.1, each direction with its
    own witness; `lt` load-bearing for (⇐) (padding countercontrol [W]). **NEW** (reduction of an effect-level clause
    to a state-level clause, and identification of KT4's content with the inequalities).
  - B2.7 STMC (single-token marginal coherence): implied by tok; excludes M_tw and every local twist [W]; the simplest
    STMC-respecting nonlocal twist fails family (i) at −1/4 [E e1]. Sufficiency: OPEN. ELABORATING.
- B3 (Q3) given KT4: Lemma B1's route re-derived step by step; exact endpoints in M_sigma (s1 S2, S3) with the M_rho
  countercontrol; precise USES: CandidateCone.2 and positive scaling only (not CandidateCone.1, not cone addition);
  full-effect reading = COMP-1's field (EFF-1's Q-SET not consumed); one body vacuous without tok. ELABORATING.
- B4 (Q4) pair premises: hadm [T] (COMP-1 bounds, definitional match s2 D1–D3); hcls [U] route (EQ2-B, landed
  ingredients present s2 N, no classification theorem); hgate and hinv [U] countermodel from landed objects
  (ball3MaxComposite / ball3MinComposite bodies with cnot; s2 G1–G2); hcl [U] countermodel (closure foil; s2 C1–C3).
  The gate and inverse labels correct EQ4-F's "transported": no base premise implies them. ELABORATING (correction).
- B5 (Q5) circularity: every route above is (s) or (2); none uses IE₁, IE₂, the quantum cone or an (o) step. The
  countermodels use Q3 / PSD16 as models only. CONFIRMING.

Passes after the first (B2.5, B2.7, B3, B4 re-read; the search sweep of N2; the setting items re-examined: pairBody
normalization = H0 at four tokens built into the typing, per-token charts = tok's content) produced no further NEW
finding in four consecutive passes: fixed point reached.

## N5. Replays, hashes and corrections after the runs

- Replays (all `python3 -I -B`, same arguments): `s0_census`, `s1_kt4_models`, `s2_pair_premises`, `e1_stmc_twist` —
  each `.replay.out` byte-identical to `.out` (`cmp`), each `.replay.err` = `exit=0`. Hashes in RESULT §10.
- Cited evidence re-hashed and matching its own record: EQ3 `p6_cheap_foils` (`0a162d37…`/`d6263e18…`, EQ3
  RESULT:354), EQ3 `p2_audit_twists_foils` (`b8cff894…`/`401efe5c…`, :350), EQ2-B `b1_native_class`
  (`03c24172…`/`a9ccaf0a…`, EQ2-B RESULT:233), `b7_certificates` (`50916f3c…`/`e3a07ef5…`, :239).
- RESULT corrections before finalizing (reading against the base): `NativeGate.posFwd/posInv` are CD:222–223 (a draft
  said CD:213–214, which is inside `IsNot`); §3.7's injectivity of T_A rests on the coordinate expansion (CI:130,
  CI:290), not on `prodEff_eq_of_eff_eq`; §3.6's `lt` step now names `prodEff_eq_of_eff_eq` (CI:342), which it does use.

## N6. End (integrity)

- `cd scratchpad/eq/base && sha256sum -c --quiet ../base.manifest.sha256`: silent, exit 0; no `__pycache__` under the
  base.
- `cd scratchpad/eq5/inputs && sha256sum -c --quiet ../inputs.manifest.sha256`: silent, exit 0.
- Repository (read-only git): HEAD `f0d37906a83585efdaca8e3ee3404410e869c43e` on `claude/network-tool-access-8jtdhm`,
  unchanged; `git status --porcelain` empty; reflog top three entries unchanged from N0.
- Write audit: every file in `scratchpad/eq5/SOURCE/` is this thread's (listing in RESULT §10 plus `.start_marker`,
  `NOTES.md`, `RESULT.md`, the `.err`/`.replay.*` files). Files newer than `.start_marker` elsewhere in the scratchpad
  are all under `scratchpad/eq5/SIX/` and `scratchpad/eq5/F/`, the concurrent SIX thread's and the coordinator's own
  directories under the protocol; this thread wrote none of them and read none of them.
