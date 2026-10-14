# Thread D: readiness of five draft control planes at M

M = `5bfdaba61b535e2fff83d8ba68e73a1b9dbc5dc5` (main after #843, #842, #844). D = `dee3b5ae` (main after #818),
the drafting snapshot of all five drafts. L = `9f9f8257`, the research base the design evidence was measured on.
Read-only work: `git show` on fetched refs plus read-only GitHub Actions queries. Lean was not compiled.

Evidence labels: **[K]** kernel text at M (file:line under `verification/lean-mathlib/OIBridge/`); **[D]** design
evidence (branch, commit, run or job id, verified through the Actions API); **[W]** a written argument made here, not
compiled; **[X]** an exact computation on the research branch that I did not rerun; **[U]** unverified or open.

***

## 0. Findings that apply to all five drafts

**Base movement from D to M.** [K]
- D lies on M's first-parent chain (`git rev-list --first-parent M` contains D). Reconciling onto M therefore
  satisfies `K3`. The movement is three first-parent merges: #843, #842 and #844.
- `verification/lean-mathlib/` is byte-identical between D and M (`git diff --quiet`). Every kernel file:line cited
  in the five drafts resolves at M. I checked each cited line for #821, #822, #824, #825 and #830.
- The `verification/ROADMAP.md` diff from D to M has two hunks. One is the one-for-one replacement of the P2 table row
  at :71. The other is the P2 section at :1113 onward. The K block (:972–:1110) is unchanged in both text and line
  numbers, so every quoted ROADMAP sentence and every `:10xx` reference still holds at M. That includes :1030–1034,
  :1035–1036, :1039–1042 and :70.
- The last import line of `OIBridge.lean` is still `import OIBridge.EqvK2MaxCone` (:268). `.github/workflows/verify.yml`
  is unchanged between D and M.
- `verification/lean-manuscript-census.json` did change. One family, the GR §3.3 Hamiltonian-reconstruction family,
  moved from `current` to `scope-consistent` and got a new note. The last family is the same, so "append at the end of
  `families`" still holds.
- M adds `.github/workflows/bg2-orientation-design.yml`. It is path-filtered to its own directory, so it does not
  trigger on these rounds' paths.
- Receipt count: 43 at L, 46 at both D and M. Legacy records: 303 at L, D and M.

**Landing consequence (S9 condition 2).** Suppose a round keeps D = `dee3b5ae` and reconciles onto LB = M. Then the
census at Λ is M's census plus the round's family, which differs from the census at E. The census path must therefore
be listed in `landing.resolved_paths`. `OIBridge.lean` and `verify.yml` need no resolution against M itself.

The alternative is an owner choice: redraft from D′ = M on a fresh pull request. Rewriting the draft's base on the
existing branch would conflict with `G9`'s "every earlier state stays in F's history".

**Nothing pre-F has been built at D or M.** [D]
- No `workflow_dispatch` of `verify.yml` exists on any of the five draft branches. The latest dispatches in the run
  list date from 2026-10-13T11:02Z and are on other branches.
- The only runs on the drafts are pull-request runs on the control-plane-only heads, all green. Examples:
  - #821: 38406400225 on `9fd622dd`;
  - #822: 38406405523 on `90c72640`;
  - #824: 38406444619 on `72db07ca`.
- These are synthetic-merge runs of a tree with no module. They are neither design evidence for a module nor a `check-run`
  attestation (§A.39).
- No `controls.py` for any of the five rounds exists on any ref. I searched the draft branches,
  `research/equivalence`, `dev-equivalence/split-l3`, `dev-equivalence/omega4` and `dev-equivalence/kinf-seams`.

**The measured blobs are not the predicted execution text.** [D]
- Each measured design module opens its header with "design module of the research thread …". The blobs are
  `b6369153` (StageSeed), `fb9c73fe` (CopyCovariance), `9030f471` (EqvOmega4) and `dc89d735` (EqvLevel3).
- "design module" is a forbidden S4 phrase in #821, #822 and #824, and in #825 too. The execution header must therefore
  be rewritten. For #824 the namespace and the print lines must also be renamed (`EqvOmega4` → `TransSeparation`).
- So the predicted-tree build is necessary, not a formality. It is the first measurement of the text that would
  actually be frozen.

**Collision surface between parallel rounds.**
- #821, #822, #824 and #825 all insert one import line directly after `import OIBridge.EqvK2MaxCone` and append one
  census family at the tail.
- #822, #824 and #830 all make the four-place edit to the aggregate `Numerical probes` job in `verify.yml`. That is
  the `needs` list, the env block, the echo line and the result check.
- Other open drafts (#823 KN-DESC-1, #826 BG-2, #827 PT-STAGE-1, #829 KTOKEN-MAXCONE-1) may touch the same files.
- Each `E` is checked against its own D, which is fine. Every landing after the first must reconcile these paths by
  merits and list them in `resolved_paths`. Serializing the landings, or batching shard edits, is an owner choice.

**The chain these drafts act on.** [K]
- `dim_of_nativeGateOf` / `three_of_nativeGateOf` (K1Bridge.lean:128, :138) take `0 < d`, `EffectsOn (eball d) avail`,
  `PreservesBody (eball d) G`, `SharpSeed (eball d) r` (K∞-Seed), `BoundaryTransitive (eball d) G` (K∞-Trans),
  `SeedOrbitAvailable G r avail` (K∞-V4), `IsNot`, `NativeGateOf` (one NOT, positivity on `maxConeOf avail`) and
  `EntanglingOf`.
- TRB-1 separately consumes K∞-Trans on the chart body: `chartBody_eq_eball` (TransitiveBody.lean:651) for the ball
  identification.

**A finding that bears on #821 and on the K∞ obligation list.**
- [K] On the ball the bare K∞-Seed predicate is free. `sharpEff_sharpSeed (axisVec_sq hd) : SharpSeed (eball d)
  (sharpEff (axisVec hd))` (EffectSpace.lean:118, :429, :431) is used exactly this way in `not_fullEffects_of_orbit`
  (:762).
- [K] `maxConeOf_avail_eq` (EffectSpace.lean:572) uses its four OG-1 hypotheses only through `sharpFamily d ⊆ avail`
  (`sharpFamily_subset_avail`, :374), followed by `maxConeOf_anti`, `maxConeOf_sharp_subset_maxCone` and
  `maxConeOf_fullEffects`.
- [W] For `0 < d`, the conjunction ∃ G r, PreservesBody ∧ SharpSeed ∧ BoundaryTransitive ∧ SeedOrbitAvailable on
  `eball d` is equivalent to `sharpFamily d ⊆ avail`. Each direction has its own witness:
  - forward: `sharpFamily_subset_avail` (:374);
  - backward: take G = `fullAut d` and r = `sharpEff (axisVec hd)`, then use `preservesBody_fullAut` (:230),
    `boundaryTransitive_fullAut` (:337) and `seedTransport_mem_sharpFamily` (:362), as in :762–770.
- At the cone step, then, K∞-Seed has no content separate from K∞-V4. Their joint content is "every sharp directional
  effect of the ball is available". K∞-Trans is still needed upstream by TRB-1.
- This is an observation for the owner (assumption-watch), not a proposed ROADMAP change. No landed lemma states the
  cone equality from `sharpFamily d ⊆ avail` alone.

***

## 1. #821 KINF-SEED-1 (`origin/draft/kinf-seed-1`, head `9fd622dd`)

### (a) Simplification of the target

**What the round would prove.**
- `sharpSeed_eball_of_stage` (theorem 1) relocates K∞-Seed onto three things:
  - K∞-Stage: `SCInf`, plus a `CompletionChart`, which needs finite rank;
  - a finite-stage *sharp stage test*: one stage effect with value 1 at one stage preparation and 0 at another;
  - an affine identification `A '' chartBody C = eball C.d`, which is TRB-1's or KTRANS-DENSE-1's output and so comes
    from K∞-Trans on the chart body.
- The seed it yields is explicit: `effTr A (effR C.L C.p0 (coord D ⟨i, e⟩))`.
- The step from the stage test to the completion is already landed and already stated in the ROADMAP
  (`sharpSeed_completion`, StageCompletion.lean:224; ROADMAP :1035–1036). The round adds only the chart restriction
  (`sharpSeed_restrict`, OrbitNormalization.lean:427) and the transport (`sharpSeed_tr`, :242). Both are landed one-line
  steps [D: blob `b6369153`, proof of theorem 1].

**Material effect: small.**
- Because the bare seed is free on the ball (§0), replacing `hP1` by the stage test removes nothing from K1's
  hypothesis list.
- Theorem 1's real value is that the seed V4 must quantify over becomes a transported stage effect. K∞-Seed ∧ K∞-V4
  would then read "the G-orbit of the transported sharp stage test is available".
- That composite (into `maxConeOf_avail_eq` or `dim_of_nativeGateOf`, with G transported by `conjTr A`) is not in the
  frozen surface. The round therefore does not change the target statement.

**Theorems 2 and 3 do not use their hypotheses.** [W from K]
- `exists_sharpSeed_eball_of_stage` and `exists_sharpSeed_eball_of_stage_dense` conclude `∃ r, SharpSeed (eball C.d) r`.
  That follows from `hd : 0 < C.d` alone, via `sharpEff_sharpSeed (axisVec_sq hd)`.
- So `hSC`, `h1`, `h0`, `hG` and `hT` are idle in both.
- The S3 load-bearing controls (`not_scInf_bad`, `not_sharpSeed_unsharp`) are load-bearing for theorem 1's specific seed
  only.
- The earned reading ("carried to the ball … from one finite-stage fact") is accurate for theorem 1 and vacuous for
  theorems 2–3. Under the claim/evidence rule (control reproducing a free fact), theorems 2–3 should be dropped, or
  reframed as explicit countercontrols showing the existential is free.

### (b) What is still missing for a complete native package

| item | status |
|---|---|
| Module built from the chosen base (D or M) | **missing.** Measured at L only, as blob `b6369153` in run 38091534622. Two discrepancies: the header contains the forbidden S4 phrase "design module", and the built preamble (two `open` lines adding `CompositeDimension K2Guard`, plus `noncomputable section`) differs from the frozen preamble in the prereg (one `open` line without them), which S1 checks. One of the two must be changed and rebuilt. |
| Probe | none required (no exact layer) |
| `controls.py` with `--self-test` and mutations | **missing** (S1–S4, V, I, C, R, G; six S1 mutations; one S2 mutation; V self-tests). Template: KTRANS-DENSE-1's at M. |
| Workflow edit | none (no shard) |
| Import line, census family | specified; to be applied in the S1 commit. The census needs re-derivation if D moves to M. |
| S2 resolution table | **gap:** lists 11 names but only 10 file:lines; `coord` has none (StageCompletion.lean:157). |
| Predicted-tree dispatch at the base | **not done** [D] |
| `F` check-run (exact head) | not done |
| Owner choices open | (1) Keep D or redraft from M; with D kept, census goes in `resolved_paths`. (2) Drop or reframe theorems 2–3. (3) Whether to add the V4 composite that would make the round change K1's hypothesis list. (4) Whether to combine with #822, which comes from the same design module `EqvSeams`. |

### (c) D-scoped references stale at M

- "D … This is main after #818" and the commit's "from current main": D is still valid as a base (it is on M's
  first-parent chain), but main is three merges ahead.
- "the workflow and the census registry changed, so … the census family [is] re-derived at D": the census changed again
  between D and M (GR family status and note). The I/C control "the census is D's with the one family" holds at E but
  forces census resolution at landing.
- Design-evidence prose ("`claims` and `duplicate` PASS on an L-based tree"; release-gate results) is L-scoped. Papers,
  `LEDGER.json` and the census changed between D and M, so it must be re-measured at the chosen base.
- Still valid at M: the 45-commit L→D drift count (L→M is 64); "no landed module cited here changed"; every
  kernel file:line; ROADMAP :1035–1036 and its quoted text; the import anchor `EqvK2MaxCone`.

### (d) Design evidence status

| run | branch @ commit | event / conclusion | verified |
|---|---|---|---|
| 38083220991 | `dev-equivalence/kinf-seams` @ `0578b13d` | dispatch / failure | [D] exists; build failed at `sum_mul_ehom` per the next commit's message |
| 38083519826 | `dev-equivalence/kinf-seams` @ `f5367a7a` | dispatch / failure | [D] Mathlib bridge job 114305141530: Build **success**, Release gate failure |
| 38091534622 | `dev-equivalence/split-l3` @ `8c92343e` (based on L) | dispatch / failure | [D] job 114328799399: `Built OIBridge.StageSeed`; three prints `[propext, Classical.choice, Quot.sound]`; `Build completed successfully (3646 jobs)`; gate: every step PASS except `lean-manuscript` (3 problems: the three unregistered modules) |

***

## 2. #822 KINF-COPY-1 (`origin/draft/kinf-copy-1`, head `90c72640`)

### (a) Simplification of the target

**It weakens K∞-Copy.**
- Copy naturality, as the ROADMAP reads it (:1039, "identical copies' NOTs agree", so `NC = NT` in DIM-1's one-NOT
  `NativeGate`), is replaced by type covariance:
  - ∃ a linear ball automorphism g, g z = z or g z = −z;
  - with `NT ∘ g = g ∘ NC`.
- Then `dim_of_nativeGate2_conj` gives d ∈ {1, 3}, and `three_of_nativeGate2_conj_of_two_le` gives d = 3.
- [D: blob `fb9c73fe`] This is strictly weaker on the data: g = id recovers `NC = NT`, and Q-POS's swapped d = 3 gate
  has `NT ≠ NC`.
- It does not change the selector's conclusion. The non-inference rule correctly records that the control gate is also
  a one-NOT gate with `NT`.
- [X] The J/K two-NOT countermodels at d = 5 and 7 violate it, by unequal eigen-splits. This is an exact layer
  (`e2_copy_conj`, 13/13); positivity of the J/K maps is not re-checked.

**Two hidden-assumption points for owner review.**
1. **Which form of the selector the weakening reaches.** [W]
   - The reduction is proved for DIM-1's absolute `NativeGate` (positivity on `maxCone`). It goes through
     `actT_mem_maxCone`, which needs only ball preservation.
   - The chain's K1 statement is K1-BRIDGE's relative `NativeGateOf` (positivity on `maxConeOf avail`). Conjugating
     before the cone equality would need `avail` to be g-invariant, which is not assumed.
   - Composing therefore needs a two-NOT relative structure plus a cone-equality transport (the analogue of
     `nativeGate_of_cone_eq`, K1Bridge.lean:73). It is short, but it is absent from the frozen surface.
   - Without it, the weakening reaches DIM-1's selector but not `dim_of_nativeGateOf`.
2. **The predicate already exists in the kernel.** [K]
   - Landed `CopyNatural N_A N_B e` (KInfFoundations.lean:284) is already conjugation by a copy identification e.
     `copyNatural_iff_apply` (:294) is the pointwise `N_B (e x) = e (N_A x)`, exactly the round's `hcov`, with an
     affine e instead of a linear g.
   - `copyNatural_refl_iff` (:288) is the ROADMAP's "NOTs agree".
   - Type covariance is therefore CopyNatural with a corner-fixing ball automorphism as the identification. The draft
     neither cites nor resolves `CopyNatural` in S2.
   - If left unconnected, the ROADMAP would carry two names for one notion after the round.

**Net.** This is the one draft that actually weakens a premise of the chain. Its reach is currently DIM-1's absolute
form.

### (b) What is still missing for a complete native package

| item | status |
|---|---|
| Module built from base | **missing.** Measured at L as `fb9c73fe` (run 38091534622, 12 prints standard). The header carries the forbidden S4 phrase "design module". Linter warnings at :110, :188 and :191 (unused or unreachable `first` alternatives) are proof-only hygiene and optional. |
| Probe `verification/lean/kinf_copy1_probe.py` | **not created.** Source `e2_copy_conj.py`, sha256 `c28e1b97…` [X], matches the prereg. Its `KERNEL` path is cwd-relative (`'../../../verification/lean-mathlib/…'`) and must become `'../lean-mathlib/OIBridge/CompositeDimension.lean'` under the shard's `working-directory: verification/lean`. `controls.py` must invoke it from the same cwd. The frozen blob hash is not yet fixed. The header cites `research/archive/threads/B/…` (provenance prose in a public file; owner's call). |
| `controls.py` | **missing** (S1 six mutations, S2, S3 via Q-EXACT, S4, P, W, V three-cell self-tests, I, C, R, G) |
| Workflow edit | **not made.** Shard `probes_kinfcopy1` plus the four-place aggregate edit. `verify.yml` is unchanged between D and M, but the edit collides with #824 and #830. |
| Import line, census family | specified; census re-derivation if D moves |
| Predicted-tree dispatch | **not done** [D] |
| Owner choices open | (1) Add the relative (`NativeGateOf`) form so the weakening reaches the chain's K1. (2) State `hcov` through `CopyNatural`, or record the correspondence. (3) Linter hygiene. (4) The base. (5) Landing order against #824 and #830 for `verify.yml`. |

### (c) D-scoped references stale at M

The same common block as #821: "main after #818", the census re-derivation, and the L-scoped gate prose.

Still valid at M:
- the S2 kernel modules (CompositeDimension, TransitiveBody, K2Guard): `three_of_nativeGate_of_two_le` at
  K2Guard.lean:234 and `dim_of_nativeGate` at CompositeDimension.lean:2723;
- ROADMAP :1039–1042 and its quoted text;
- the W control "workflow at E is D's with exactly that edit", since `verify.yml` is unchanged between D and M.

### (d) Design evidence status

| run | branch @ commit | verified |
|---|---|---|
| 38083220991 / 38083519826 | `dev-equivalence/kinf-seams` @ `0578b13d` / `f5367a7a` | as in #821 [D] |
| 38091534622 | `dev-equivalence/split-l3` @ `8c92343e` | [D] job 114328799399: `Built OIBridge.CopyCovariance`; all twelve prints (:347–:358) standard; linter warnings only; gate fails `lean-manuscript` only |
| exact | `research/equivalence` (`e2_copy_conj.out`) | [X] `checks: 13, failures: 0`, `VERDICT TYPE-COVARIANCE-CONSISTENT`; not rerun here |

***

## 3. #824 KTRANS-SEP-1 (`origin/draft/ktrans-sep-1`, head `72db07ca`)

### (a) Simplification of the target

**It removes nothing; it separates K∞-Trans.**
- The kernel would prove that on Ω₄ = {‖x‖⁴ + s⁴ ≤ 1} ⊂ ℝ⁴ the following all hold:
  - compact, convex, with interior;
  - `ElementaryDrivability` (K∞-Drive);
  - `SharpSeed` (K∞-Seed);
  - `RelStrictConvex`, hence `SingletonFaces` (K∞-Geom);
  - centrally symmetric;
  - no affine image of `eball 4`, by a 16-point `linarith` certificate;
  - and no body-preserving family is `BoundaryTransitive` or has a `DenseBoundaryOrbit`.
- [D: run 38096511360, all 15 prints standard.] This upgrades ROADMAP :1033–1034 from "no theorem derives …" (an
  absence) to a kernel negative result. Since the conclusion quantifies over every body-preserving family, it also covers
  any K∞-Act data.

**Scope.** The separation is single-system and at chart dimension 4. It says nothing about the native gate or d = 3.
- The draft's research context has its own conjecture R-E16.1 [U, written proof only]: `relC` with an invertible gate
  and a NOT forces odd d on any body. The kernel proves this only for `eball` (`not_even_of_relC`,
  RelcSelectParity.lean:354).
- So Ω₄ would likely carry no native gate. Whether {Drive, Seed, Geom, native gate} jointly imply transitivity is open
  (this is #830's residual).
- The round shows K∞-Trans cannot be dropped at the ball step of the present route order. It does not show K∞-Trans is
  independent of the chain's full premise set.
- The non-inference rule states this scope correctly ("nothing about chart dimension 3, and nothing about the
  composite").
- [U] Ω₄ is not shown to be the chart body of any `DirectedStages`. K∞-Stage realizability is not claimed.

### (b) What is still missing for a complete native package

| item | status |
|---|---|
| Module built from base | **missing under its predicted name.** `C0` is met on `9030f471` as `EqvOmega4` (run 38096511360). `TransSeparation` needs a namespace rename (`OIBridge.EqvOmega4` → `OIBridge.TransSeparation`), 15 renamed prints and a header rewrite (the current one contains "design module"). Optional: the deprecations `Set.mem_setOf_eq` and `push_neg`, and the `unnecessarySeqFocus` warning at :244. |
| Probe `verification/lean/ktrans_sep1_probe.py` | **not created.** It would be `e8_ktrans_probe.py` byte for byte; sha256 `c32afda9…` [X] matches. It imports `sympy`, but the prereg pins no version; other shards pin `sympy==1.14.0`, and the research run's version is not recorded. The header reads "E8 design probe for draft S4" (provenance prose; S4 scans only the module header and result note). |
| `controls.py` | **missing** (S1 five mutations including the exponent-2 body, S2 13 names, S3, S4, P, W, V, I, C, R, G) |
| Workflow edit | **not made.** Shard `probes_ktranssep1` with a pip line, plus the four-place aggregate edit. Collides with #822 and #830. |
| Import line, census family | specified |
| Predicted-tree dispatch | **not done** [D] |
| Owner choices open | (1) sympy pin. (2) Deprecation cleanup. (3) Probe header prose. (4) The base. (5) `verify.yml` landing order. |

### (c) D-scoped references stale at M

The same common block. In addition, the `C0` row's "303 legacy records intact, 43 receipts hold" and "`lean-axioms`
5875" are L-tree numbers; D and M have 46 receipts. Every kernel reference holds at M, as do ROADMAP :1030–1034 and the
import anchor.

### (d) Design evidence status

| run | branch @ commit | verified |
|---|---|---|
| 38090924005 | `dev-equivalence/omega4` @ `195dfbee` (blob `ee870649`) | [D] dispatch / failure; build failed, per the repair commit's message (two terms at :157, :215) |
| 38096511360 | `dev-equivalence/omega4` @ `95beab2b` (blob `9030f471`) | [D] job 114343410536: `Built OIBridge.EqvOmega4`; all fifteen prints (:530–:544) standard; `Build completed successfully (3644 jobs)`; gate: every step PASS except `lean-manuscript` (1 problem). The run's head commit message says "not dispatched"; it predates the dispatch, and the run exists. |
| exact | `research/equivalence` | [X] `e8_ktrans_probe.out`: `checks: 12, failures: 0`, both countercontrols "fail as stated", `VERDICT DRIVE-SEED-GEOM-SEC-CAP2-NOT-TRANS`; `e2_drive_trans.py` sha `394850c8…` matches |

***

## 4. #825 L3-CONV-1: short qualification

- **Simplification:** none of the finite K chain. The round bounds the converse direction of Level III (quasilocal,
  H-∞ row :70) relative to `QuasilocalSystem`, whose definition already contains the complex matrix stages. It is
  off-route.
- **Built** [D: run 38091534622, job 114328799399]: `phase_not_oiInduced`, `not_naiveConverseDyn`, `not_comm_of_system`
  and `kraus_iff_of_member`, all with standard prints and one unused-simp warning (blob `dc89d735`, which imports only
  `QuasilocalCharacterization`).
- **Unbuilt:**
  - `MemberFiniteSupport` and `finiteSupport_iff_kraus_of_member`;
  - `regionAvail` (used, but not in the code block) and `regionTheory`;
  - `regionTheory_exactSystem`, `regionTheory_oiPlus` and `regionAvail_indep`;
  - the four §A.34 directional witnesses;
  - the controls `targetA_conclusion` and `stage_comm_of_subsingleton`.
- **§A.34 shape change:** the built `kraus_iff_of_member` is a single iff; the prereg requires it split into named
  directions, so the built evidence does not cover the frozen form.
- **Unresolved composite interface (owner item 3)** [K]:
  - `oiPlus_of_qm` (CarrierGeneralOIPlus.lean:198) consumes `ExactAllFiniteEndomorphicQuantumOps`
    (LevelOneSeam.lean:186), which is `Exact… ∧ ExactCompositeQuantumOps` (AncillaClosure.lean:364).
  - `regionTheory_exactSystem` supplies only the first conjunct.
  - The OIPLUS cell is undefined until the owner picks option (a), (b) or (c).
  - `LevelOneSeam.lean:186` is missing from the draft's landed-object list.
- **Still missing for a native package:** everything except the D-scoped text. That means the port to `Level3Converse`
  with its new import set, `controls.py`, the optional exact layer (which would add a probe and workflow to the governed
  paths) and the predicted-tree dispatch.
- **Stale references at M:** none beyond the common block. "`QuasilocalSystem` occurs in no other kernel module" still
  holds at M (all occurrences are in QuasilocalCharacterization.lean). OIBridge.lean:268 and ROADMAP :70 hold.

***

## 5. #830 GEOM-ODD-1: short qualification

- **Simplification:** none by any outcome. The round is an exact-layer search with no kernel module.
  - A HIT is positivity on finite pools: a candidate, not a gate or a countermodel.
  - EXCLUDED concerns one body with one (z, N), and no exclusion method exists, so that token is to be struck.
  - A finite search cannot decide the universal question: do K∞-Geom, a drive and a native gate force an ellipsoid at
    odd d ≥ 5?
  - Its relevance to the target is indirect. A positive general theorem would be needed to reorder the route so that
    K∞-Geom, Drive and the gate replace K∞-Trans.
- **Prior positive control failed** [X: research branch]. Both `e20_odd_bodies` runs end `VERDICT NOT RENDERED --
  failing: ['C4']` with `eball 3: UNDECIDED(iterations)`.
- **Still missing:**
  - probe, generator and verifier (rebuilt from `ec95a697…`, adding `posInv`, the holdout pool, VE, VD and VN);
  - a generator that couples G and G⁻¹;
  - frozen search set, seeds, pools and pinned `numpy`/`scipy`;
  - `controls.py`, the shard and `verify.yml` edit, the predicted-tree dispatch;
  - verification of the determinant observation [U].
- **Stale references at M:** none beyond "main after #818". The kernel lines hold, `verify.yml` is unchanged and the
  RELC-SELECT-1 record is unchanged between D and M.

***

## 6. Ranked recommendation

1. **#822 KINF-COPY-1: advance first.**
   - It is the only draft whose positive outcome weakens a premise of the target: token-equal NOTs become type-conjugate
     NOTs.
   - The module and probe are measured, the latter as [X].
   - Before F, the owner should decide two things, each one design run or less: whether to add the relative
     `NativeGateOf` form so the weakening reaches K1-BRIDGE's selector (not only DIM-1's), and whether to tie `hcov`
     to landed `CopyNatural`.
   - Then: fix the probe's cwd-relative kernel path, write `controls.py`, and build and dispatch the predicted tree.
2. **#824 KTRANS-SEP-1: second; it is the closest to F.**
   - `C0` is met, the probe hash matches, and the mathematics is non-trivial.
   - It separates rather than simplifies: it certifies that K∞-Trans cannot be dropped at the ball step in favour of
     the single-system seams (d = 4). That is useful for deciding where sourcing effort should not go.
   - Remaining work is mechanical: rename, header, sympy pin, `controls.py`, shard, dispatch.
   - It shares the `verify.yml` edit with #822, so serialize the landings or coordinate the shard edit.
3. **#821 KINF-SEED-1: third, and revise before F.**
   - It is the cheapest package (no probe, no workflow), but its yield is the smallest.
   - The bare seed is free on the ball, and theorems 2–3 hold without their hypotheses. The round leaves K1's
     hypothesis list unchanged unless it gains the V4 composite.
   - A higher-yield variant would state the cone step (and K1's selectors) from `sharpFamily d ⊆ avail` [W, §0],
     exposing that K∞-Seed and K∞-V4 are one obligation at the cone step. Theorem 1 would then supply the natural base
     point (a transported sharp stage test).
4. **#825 L3-CONV-1:** off the finite K chain, with unbuilt declarations and an open composite interface. Not ready.
5. **#830 GEOM-ODD-1:** exploratory, with a failed prior positive control and no outcome that changes the target. Last.

**Common precondition for all.** Choose the base: keep D = `dee3b5ae` and resolve the census at landing, or redraft
from M. Then build and dispatch each predicted tree. No such run exists yet.
