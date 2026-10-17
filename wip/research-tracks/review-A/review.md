Review A: the k-token cone theorem on research/finite-reconstruction-design-20261013 (@29857749, source head 11fbcd59)

Bottom line: no item is refuted and none has a gap. The compiled theorems match #829's premise set in substance. None of their hypotheses is stronger than #829's: there is no closedness or self-duality assumption, no extra gates, and no assumed inverse invariance. Every countermodel violates exactly the hypothesis it was built to fail. The scope fixes needed are in wording, mainly the report's headline. What compiles is a research-carrier form of #829's theorem, not #829's proposed statement surface.

Method: read-only, in a detached worktree at 29857749. The worktree was clean and has been removed. Lean was not compiled; the CI logs were read through the GitHub MCP tools.

**1. Statement fidelity: CONFIRMED-WITH-SCOPE-FIX**

The definitions the statements use (FiniteReach.lean / FiniteReachTable.lean):
- **Carrier:** `Mat k = Matrix (Bits k) (Bits k) ℂ`, with `Bits 0 = Fin 1` and `Bits (n+1) = Bits n × Fin 2`. Token i is component i (`bitAt`, :185–187).
- **Products:** `prodVec k a = ∏_{i<k} a i (b_i)` (:629–631); `prodMat k ρ = ρ0 ⊗ … ⊗ ρ(k−1)` (:757–759).
- **Gates:** `cnotM k i j = Σ_b |b⟩⟨b| ⊗ X^{b_i}` on token j (:221–225, `blockFam` :115). `localM k j V` is V on token j (:228–231). `phaseMat c s = diag(1, c+is)`; `cycMat` is (I − i(X+Y+Z))/2.
- **Preservation:** `Pres C U :≡ ∀ A ∈ C, U A Uᴴ ∈ C` (:345). `psdSet k = {A | A.PosSemidef}` (:784).
- **Table objects:** `dictionary k w = Σ (w μ/2^k) P_μ` and `coordinates k H μ = Re Tr(P_μ H)` (FinitePauli:177–181). `tabAct k U w = coordinates k (U · dictionary k w · Uᴴ)` (Table:209). `prodTab k v μ = ∏_{i<k} v i μ_i` (Table:20).
- **Effects:** `maxConeTab k = {w | ∀ e, (∀ i<k, IsEffectOn (eball 3) (e i)) → 0 ≤ Σ_μ prodTab k (ehom∘e) μ · w μ}` (Table:337). `IsEffectOn Ω e ≡ ∀ x∈Ω, 0 ≤ e x ≤ 1` (KInfFoundations:116). `Lor v ≡ 0 ≤ v0 ∧ Σ v_{j+1}² ≤ v0²` (CompositeDimension:869).

Below, H2 stands for `∀ i j, i<j → j<k → Pres C (cnotM k i j)`. A stands for `∀ j, 0<j → j<k → ∀ t, Pres C (localM k j (phaseMat (cos t) (sin t))) ∧ Pres C (localM k j cycMat)`. H2tab and Atab are the same with `∀ w ∈ K, tabAct … w ∈ K` in place of `Pres`.

The statements:
- `subset_psd_of_maxCone_drive` (Reach:789–795):
  - (hherm: ∀A∈C, A.IsHermitian)
  - (hmax: ∀A∈C, ∀a : ℕ→Fin 2→ℂ, 0 ≤ star(prodVec k a) ⬝ᵥ (A *ᵥ prodVec k a))
  - (H2) (A)
  - gives C ⊆ psdSet k.
- `psd_subset_of_products_cone_drive` (:809–817):
  - (hprod: ∀ρ, (∀i<k, ρ i PSD ∧ trace 1) → prodMat k ρ ∈ C)
  - (hadd) (hsmul: ∀c≥0, ∀A∈C, c•A∈C)
  - (H2) (A)
  - gives psdSet k ⊆ C.
- `kCone_eq_psd_of_drive_maxCone` (:844–856): all seven hypotheses give C = psdSet k.
- `driveInvariant_of_eq_psd` (:862–867): C = psdSet k gives H2 ∧ A.
- `kCone_eq_psd_iff_drive_maxCone` (:872–883): under hherm, hprod, hadd, hsmul and hmax, C = psdSet k ↔ H2 ∧ A.
- `tableCone_eq_psd_of_drive_maxConeTab` (Table:364–376):
  - (hH1: ∀x : ℕ→Fin 3→ℝ, (∀i<k, x i ∈ eball 3) → prodTab k (hom∘x) ∈ K)
  - (hadd) (hsmul)
  - (hmax: K ⊆ maxConeTab k)
  - (H2tab) (Atab)
  - gives K = {w | (dictionary k w).PosSemidef}.
  - The forward-cone variant `tableCone_eq_psd_of_drive_maxCone` (:224–235) is the same with "∀v, (∀i<k, Lor(v i)) → 0 ≤ Σ prodTab k v μ · w μ" in place of hmax.
- `tableDrive_of_eq_psd` (:386–394): K = {PSD dictionary image} gives H2tab ∧ Atab.
- `tableCone_eq_psd_iff_drive_maxConeTab` (:399–411): under hH1, hadd, hsmul and hmax, K = {…} ↔ H2tab ∧ Atab.
- `lorPair_nonneg_of_maxConeTab` (:343–361): w ∈ maxConeTab k and (∀i<k, Lor (v i)) give 0 ≤ Σ_μ prodTab k v μ · w μ.

Premise by premise against #829 (preregistration at 625f853f, :56–75):
- **Carrier:** different type. The recursive `Labels k → ℝ` is isomorphic to `WK k = (Fin k → Fin 4) → ℝ`, but the transport is not compiled. The matrix form's hherm is the chart.
- **H1:** same. The ℕ-indexed form with an i<k guard is equivalent; matrix hprod is H1 through the dictionary.
- **hadd, hsmul:** same.
- **hmax:** `maxConeTab` has the same quantifier structure as `maxConeK`. The Lor form and the matrix product-vector form are equivalent to it, but are not compiled as equivalences.
- **H2:** the gate set is the same (every i<j). The action, however, is defined by conjugation through the dictionary, not by #829's `cnotK` sign-and-label formula.
- **A:** the token set is the same (j ≠ 0, with every t and the cyclic map). The action is again defined by conjugation, not by `actK`/`homMap`.
- **Conclusion:** same, up to the carrier.
- **Nothing makes the theorem easier:**
  - `Pres` is forward-only, as in #829. Inverse invariance is derived, not assumed: `isWord_conjTranspose` (:384–410) builds cyc⁻¹ as −cyc² from the adopted `cycMat_conjTranspose_eq`.
  - Unit scalars are discharged by `pres_scalar` (:361).
  - No closedness assumption is made. The upper inclusion uses neither products nor cone closure.
  - The upper inclusion uses hmax only on padSeq seeds (`reach_norm`, :719–752), which matches Track B's Corollary 1.

Exact check of the remaining definitional gap (formalization.md item 1):
- `scripts/tabact_vs_829.py` re-implements the design definitions literally on one side and #829's `cnotK`/`actK` on the other. The latter use the landed `sgn`/`pc`/`pt` (CompositeDimension:741–757), `homMap`, `rotLin` and `cycEquiv`.
- It compares the two exhaustively over basis tables at k = 1..4, for every i<j and every token j>0, at three rational angles.
- Result: all match.
- Countercontrols that were correctly rejected:
  - reversed CNOT direction;
  - flipped rotation sign;
  - cycEquiv⁻¹;
  - a degenerate CNOT that reads its control past the end of the carrier and so acts as the identity. It is labelled NEG-SWAPDEF, but it is weaker than "swapped definition" suggests; NEG-REV is the real direction control.
- At k = 2 these agree with the kernel anchors `dict_cnot` (BridgeDictionary:71), `tokMat_rot` and `tokMat_cyc` (EqvK2Converse:87, :133).
- This is finite exact evidence, not a proof for all k.
- Files and hashes:
  - script: /tmp/claude-0/-home-user-incompleteness/ce7104bc-8508-557b-9490-8c1ce0f7a1ca/scratchpad/research/review-A/scripts/tabact_vs_829.py, sha256 `3fb354bbc276fc58d5fe5044d1846eb2b48fad006eca43dff7e6187d7ffa1c6e`
  - output: /tmp/claude-0/-home-user-incompleteness/ce7104bc-8508-557b-9490-8c1ce0f7a1ca/scratchpad/research/review-A/tabact_vs_829-output.txt, sha256 `d20f1d086acf3ada67788b5bee93f00a1b8df47c0379418b1d61357bbfcc7dbe`
  - 89 checks, 0 failures, empty stderr, run with python3 -I.

The names also differ from #829's frozen S1 names (`subset_QK_of_maxCone_drive`, `kCone_eq_QK_…`, `driveInvariantK_of_eq_QK`). As written, the modules would not pass #829's S1 control. That is expected before F.

**2. Non-vacuity: CONFIRMED**
- PSD satisfies every hypothesis at every k. Hermitian, tensor-product PSD, cone and quadratic-form positivity are elementary [W]; the drive part is the compiled `pres_psd` (:858).
- The conclusion is not trivial. At k = 3, ZERO3, SCALE3, ADD3, SHIFT3, SEP3/CUT3 and ORBIT3 each drop exactly one hypothesis and differ from PSD.
- No compiled lemma states that PSD meets hherm, hprod, hadd, hsmul and hmax. It would be cheap to add.

**3. §A.34 directional witnesses: CONFIRMED-WITH-SCOPE-FIX**
- Matrix iff:
  - → is `driveInvariant_of_eq_psd` (subst, then PSD conjugation);
  - ← is `kCone_eq_psd_of_drive_maxCone`, the antisymmetry of two genuine inclusions.
- Table iff:
  - → is `tableDrive_of_eq_psd` (via `tabAct_psd`);
  - ← is `tableCone_eq_psd_of_drive_maxConeTab`.
- None of these is an extension, uniqueness or density theorem.
- argument.md:33–34 ("equivalently"):
  - The compiled direction is effect form ⇒ product-vector form. It exists only as `lorPair_nonneg_of_maxConeTab` together with the internal step `hmaxC` (Table:251–261); there is no standalone named theorem.
  - The converse is written only. formalization.md:178–179 says so, but argument.md does not.
  - Fix at argument.md:39–40: "scaled rank-one local projectors give one direction (compiled for tables: `lorPair_nonneg_of_maxConeTab`, used in `tableCone_eq_psd_of_drive_maxCone`). Conversely (written argument, not compiled), …".
- No prose claims the "equivalently" is compiled.

**4. Kernel hygiene: CONFIRMED**
- The five .lean files contain none of: sorry, admit, axiom, native_decide, unsafe, implemented_by, extern, opaque, set_option or macros. The only instance changes are FinitePauli:49 and :56 and the `attribute [instance high]` at Reach:34.
- `sha256sum -c SHA256SUMS` passes.
- Job 116860178759 ran at head_sha 11fbcd59 and every step succeeded. Docs job 116861771680 ran at 29857749 and succeeded.
- All 38 prints read exactly [propext, Classical.choice, Quot.sound] (8 + 3 + 3 + 13 + 11), and every name the report lists appears.
- The log has no error and no sorry. The warnings are linter-only, plus one "bitsDecEq of class type is semireducible".
- Theorem counts are 14/6/3/77/29, total 129, as stated.
- Four print lines are wrapped across lines in the log, not printed verbatim on one line as the report says: `psd_subset_of_products_cone_drive` and three `tableCone_*`. Any print control at adoption must normalize whitespace.
- From the certifying log I read the last 400 of its 6,966 lines, which hold the whole design-compile segment from "Build completed" on. That the hash check and replays passed rests on the step conclusions.

**5. bitsDecEq: CONFIRMED**
- The fix cannot change what any statement means. `DecidableEq α` is a subsingleton, so `1` or `diagonal` built with different instances are provably equal, and `PosSemidef`, `IsHermitian` and `Pres` do not depend on the instance.
- At explicit sizes it unfolds to the Prod and Fin instances the adopted modules synthesize.
- Labels still uses the classical `carrierDecidableEq` (FinitePauli:56), harmlessly.
- At adoption: make the instance structural at its source (FinitePauli:56), and mark it reducible to silence the semireducible warning.

**6. Countermodels: CONFIRMED (none satisfies every hypothesis)**

| Countermodel | Hypothesis it violates |
| --- | --- |
| ZERO3 | hprod / hH1 |
| SCALE3 | hsmul |
| ADD3 | hadd |
| SHIFT3 | hmax: value −1 at \|000⟩ [X] |
| SEP3 | H2 at (0,1): partial-transpose minor −1/4 under the literal `cnotM` [X] |
| CUT3 | H2 at (1,2): GHZ, minor −1/4 [X] |
| ORBIT3 | A: cyclic map on tokens 1 and 2 |
| Track B CM1–CM5 (H = S⊗I₄) | hmax: −1/25 at (3,4)⊗\|00⟩, a seed vector [X] |
| Track C ΓQ3 at k = 2 | H2 only: Bell state, singlet value −1/2 [X]; it satisfies A by the intertwining [X] |

**7. Workflow: CONFIRMED**
- The diff 8b431a18→29857749 only adds `OIBridge.EqvK2Generation` to the lake build, two copy lines, and the compile of FiniteReach (with -o) and FiniteReachTable.
- The earlier modules' commands are unchanged. `verification/lean-mathlib` is identical to D. FinitePauli, FiniteWalsh and FiniteCircuit are unchanged.
- Between pushes: 0edc62db→11fbcd59 changes comments only; FiniteReach statements have been stable since 45c05e31.

**8. Claim/evidence boundary: CONFIRMED-WITH-SCOPE-FIX**

The modules, formalization.md (:192–203) and argument.md (:250–253) keep "research", "conditional" and "not adopted". The fixes are in the report and one line of argument.md:
- **Report headline.** Replace "The conditional k-token cone theorem from #829 now compiles for every k" with: "A research-carrier form of #829's conditional k-token theorem compiles for every k (recursive `Bits k`/`Labels k`; table actions defined by dictionary conjugation). #829's statement surface (`WK k`, `cnotK`/`actK`, its names, Q-PAIR) is not yet reached."
- **"Items 2–4: done".** Change to "done in the form the theorem uses (qubit spectators only)". The original item 2 named arbitrary spectator carriers. These are the remaining obligations of formalization.md at 8b431a18, not "#829 items".
- **"Earlier green runs on the same statements".** Change to "on the subsets present then". 45c05e31 had FiniteReach only; 03cd311d lacked the effect-form theorems.
- **argument.md:249–250.** Optionally, "table forms" → "a dictionary-conjugation table form".

No witness→theorem, conditional→unconditional or design→adopted overreach was found.