# NOTES-C22 — Theorem S′ for compact defect sets as a design module

Round-5 node C22, opened 2026-10-11T07:19Z (session start); S0 written 2026-10-11T07:50:58Z (`date -u`), before any C22 script ran and
before any Lean text of the node was dispatched. Target (the coordinator's words): for a compact family of rank-one
defects `d_h = 1 − c(h) P_h` with unit seeds, `c` continuous into `(1, 2]`, `c < card n`, pairwise nonnegative trace
pairings and (CC) in cap/co-cap form on every pair of positive pairing, the surgery cone `K(Z) = (PSD ∩ Z*) + closed cone Z`
is closed and self-dual under `Re tr(AB)`. The circle cones C13.5, C13.7 and `K_κ` (C16.4) rest on this statement at
[W] (C13-S); the finite form is `CmSprime` (C17.1, [D]).

Conventions as in NOTES-C11, NOTES-C13 and NOTES-C17; the module is `OIBridge/CmSprimeCompact.lean` (namespace
`OIBridge.CmSprime`, importing `OIBridge.CmSprime` unchanged), written against the kernel at L = `9f9f8257` and the
Mathlib the lakefile pins (`v4.33.0`; the local read-only checkout `db584cd6`, grep only); the working copy is kept under
`lean/` once a run has been made.

## Question, design, productivity test (§A.31)

**Question.** Which step of the finite proof needs a new argument over a compact base, and can the compact theorem be
stated with every hypothesis explicit and machine-checked within one or two dispatches?

**Design (fixed before the first run).** The finite engine (`selfDual_of_local`: Farkas by the infimum of ratios, the
least-weight decomposition on a compact feasible set, the local lemma) is reused as a black box through
`theorem_Sprime`, not generalized to a compact family. The compact theorem is reduced to the finite theorem on finite
nets of the compact family:

1. **Definition.** For an index type `κ` and `d : κ → Herm(n)`, `coneOf d` is the set of finite nonnegative
   combinations `Σ_{k ∈ s} t_k d_k` (`s` a finset), and
   `surgeryC d = {q + z : q ⪰ 0, pr q (d k) ≥ 0 for every k, z ∈ closure (coneOf d)}` — the surgery with the **closed**
   conic hull, which is the target statement's own form. (Whether `coneOf d` is already closed for a compact family —
   Carathéodory over a compact base not containing 0, NOTES-C13 C13-S — is left as a written remark [W]; it is what
   identifies `surgeryC` with the thread's `K(Z) = (Q ∩ Z*) + cone Z` and is **not** part of the module's statement.)
2. **`K ⊆ K*`** by the four pairings, each extended to the closure of `coneOf d` by `closure_minimal` (the pairing
   with a fixed matrix is continuous). No new argument.
3. **`K* ⊆ K` — the new argument (approximation).** Let `y ∈ K*`. For `ε > 0`, compactness of `κ` and continuity of
   `d` give a finite `F ⊆ κ` with every `d k` within `ε` (entrywise) of some `d k′`, `k′ ∈ F`. The finite theorem
   applies to the subfamily `F` (every hypothesis restricts). Two estimates make `y + ηI` a member of the finite
   dual cone `(K_F)*`: (a) for `q ⪰ 0` and any `M` with entries `≤ ε` in modulus, `|pr q M| ≤ ε · n · tr q` (through
   the factorization `q = BB†`, `pr q M = Σ_m qf M (B_m)`, and Cauchy–Schwarz `(Σ|v_a|)² ≤ n Σ|v_a|²`); hence for
   `q ∈ Q ∩ F*`, `pr q (d k) ≥ −ε n tr q` for every `k ∈ κ`, so `q + δI ∈ Q ∩ Z*` for `δ = ε n tr(q)/τ`
   (`τ ≤ tr d_k` the uniform trace bound, `τ = n − max c > 0` by compactness), so `pr q y ≥ −δ tr y`; (b) therefore
   `pr X (y + ηI) ≥ (η − ε n tr(y)/τ) tr q ≥ 0` for every `X = q + Σ t_k d_k ∈ K_F` when `η ≥ ε n tr(y)/τ`. The finite
   theorem gives `y + ηI = q_F + z_F` with `q_F ∈ Q ∩ F*`, `z_F ∈ coneOf d`. Along `ε_m → 0` (`η_m → 0`) the
   `q_m` and `z_m` lie in compact entry boxes (PSD entries are bounded by the trace; `z`-entries by
   `3 · tr z/τ`), so subsequences converge: `q_m → q ⪰ 0` with `pr q (d k) ≥ 0` for every `k` (limit of
   `≥ −ε_m n R`), `z_m → z ∈ closure (coneOf d)`, and `y = q + z ∈ K`.
4. **Closedness** of `surgeryC d` from `K = K*` (a dual cone is closed), as in the finite engine.

So the steps that need new arguments over a compact base are exactly: the quantitative pairing estimate (3a), the shift
`y + ηI` into the finite dual cone (3b), and the limit passage (compact entry boxes, subsequences). What the design
does **not** need: Farkas over a compact family, a least-weight decomposition over a compact family, a separation
theorem, and Carathéodory (the last only because the closed conic hull is in the definition).

**Productivity test.** The node is a gem iff it yields a fact strictly stronger than the restatement "S′ holds for
compact Z" — here: the identification of the finite-net approximation as the only new step, with the closedness of the
conic hull separated out as a named [W] remark — and it constrains something: the compact-form statement the circle cones
rest on becomes machine-checked (if the dispatch is green), and its exact hypothesis list fixes what every consumer
(C13.5, C13.7, C16.4; HO-36's tower closure question, C23) must verify. Below that bar: record only.

## Hypothesis classification (standing rule 1; owner's requirement (1))

Pure cone geometry in `Herm(n)`; no OI inventory item is used, no introduced hypothesis (H1–H3, A_miss, claim (D), EBF,
T) appears. Every hypothesis of the compact form is explicit in the module's statement: `[CompactSpace κ]` (the
defect family is the continuous image of a compact space), `Continuous c`, `Continuous h` (the seed map), unit seeds,
`1 < c k ≤ 2`, `c k < card n`, `[Nonempty κ]` (the empty family is the PSD cone, self-dual by the kernel's
JordanClassification.lean:84, not restated), pairwise nonnegative pairings, (CC) in cap/co-cap form on every ordered
pair `j ≠ k` of positive pairing; the closedness the compact base needs enters as the closed conic hull in the
definition of `surgeryC`. Reading of every downstream use: invariance (the cones are pair cones; nothing here is about
availability). Written parts and kernel-checked parts are separated in the RESULTS rows: the module's statements are
[W] until the dispatch is green and [D] after; the Carathéodory remark (closedness of `coneOf d`) stays [W].

## S0 — predictions and decision rules (written before the first run)

### Preflight `experiments/c22_preflight.py` (exact: Fractions, Gaussian rationals; sympy for symbolic identities)

Instance data: the S2 circle cone of C13.7 — `g_w = (3, 3, w, −w)` in the computational basis (`|0+⟩ = (1,1,0,0)/√2`,
`|1−⟩ = (0,0,1,−1)/√2`; `|g_w|² = 20`), `P_w = g_w g_w†/20`, `d_w = I − c P_w`, `c = 21/20`, `|w| = 1`; the net
`F = {±1, ±i, (±3 ± 4i)/5}` (eight rational points) and off-net rational points `w ∈ {(5 + 12i)/13, (−5 + 12i)/13,
(8 + 15i)/17, (7 + 24i)/25, (−7 − 24i)/25, (20 + 21i)/29}`.

1. **Q1 the column identity and the pairing estimate.** For exact PSD `q = BB†` (Gaussian-rational `B`) and Hermitian
   `M`: `pr q M = Σ_m qf M (B_{·m})` exactly, and `|pr q M| ≤ ε n tr q` with `ε² = max_ij |M_ij|²` (compared through
   squares). Countercontrol: the factor `n` is load-bearing — `q = vv†`, `v = (1,1,1,1)`, `M` the all-ones matrix:
   `pr q M = 16 = ε n tr q` while `ε tr q = 4 < 16`. Predicted: identity on every instance; bound on every instance;
   countercontrol as stated.
2. **Q2 the entry bound for PSD matrices.** `4|q_ij|² ≤ (q_ii + q_jj)²` and `|q_ij|² ≤ (tr q)²` on the PSD instances.
   Countercontrol: the Hermitian non-PSD `X ⊕ 0` (`|q_01| = 1 > 0`). Predicted: both hold; countercontrol fails.
3. **Q3 the defect entry bound.** `|d_ij|² ≤ (1 + c)²` for unit seeds (exact instances including `c = 2` on a Bell
   state); countercontrol: a non-unit seed `(2, 0, 0, 0)` at `c = 2` has `|d_00| = 7 > 3`. Predicted: as stated.
4. **Q4 the net mechanism on the circle.** (a) Hypotheses of the finite theorem on `F ∪ {off-net points}`: unit seeds,
   `c ∈ (1, 2]`, pairings `4 − 2c + c²s ≥ 0`, (CC) `c²s ≥ 4(c − 1)` on every pair; the symbolic identity
   `|⟨g_w|g_{w′}⟩|²/400 = |9 + w̄w′|²/100` for `|w| = |w′| = 1`, whose minimum `64/100 = 16/25` is C13-S2's `s_min`.
   (b) `ε²` := the exact maximum over off-net `w` of the minimum over `w′ ∈ F` of `max_ij |(d_w − d_{w′})_ij|²`;
   `τ = 4 − c = 59/20`. (c) For sampled pure `q = P_v ∈ Q ∩ F*` (exact `v` with `|⟨g_{w′}|v⟩|² ≤ 20|v|²/c` for every
   `w′ ∈ F`), and every off-net `w`: `pr q (d_w) ≥ −ε n tr q\) and `pr (q + δI) (d_w) ≥ 0` with `δ = ε n tr(q)/τ`
   (both compared exactly through squares when the left side is negative). (d) The shift on a real instance:
   `y = d_{w₀}`, `w₀ = (5 + 12i)/13` (an element of `K(Z)`, hence of `K(Z)*` by the pairings), is **not** in `K(F)*`
   — an exact pure `v` in the open cap of `w₀` outside every net cap has `pr (d_{w₀}) P_v < 0` — while
   `y + ηI`, `η = ε n tr(y)/τ = 4ε`, pairs `≥ 0` with every sampled `P_v ∈ Q ∩ F*` and with every `d_{w′}`,
   `w′ ∈ F`. Predicted: (a)–(d) as stated (the witness of (d) exists, by the cap-radius count `arccos(1/√c) ≈ 12.6° <`
   the half-spacing of the net `≈ 15.6°` in Fubini–Study distance).
5. **Q5 Bell-circle countercontrol.** On the Bell circle `C2(w)` at `c = 2` two distinct points pair to `4s − 4 < 0`:
   the pairing hypothesis fails (consistent with C7.6, `K(Z_circ)` not self-dual). Predicted: as stated.

Decision rule (fixed now): `VERDICT C22-PREFLIGHT-OK` iff Q1–Q5 give the predicted outcomes, countercontrols included.
Any other outcome voids the preflight and blocks the dispatch until it is understood; a failed run is kept as
`c22_preflight.run1.{py,out,err}`.

### Design run (CI): at most two dispatches for C22 (the round's third is held for C23)

Branch `dev-countermodels/c22-compact` cut from L with two modules — `OIBridge/CmSprime.lean` exactly as at
`5649e641` (sha256 `a10f4790…`) and the new `OIBridge/CmSprimeCompact.lean` — and two import lines in `OIBridge.lean`
(after `import OIBridge.RelcSelectC5`). Dispatched by `workflow_dispatch` through `gh api`, as LOG records for round 4.

Decision rule (fixed now): the run is **BUILT** iff, in the Mathlib bridge job log, (i) the Build step succeeds with
`Built OIBridge.CmSprimeCompact` (and `Built OIBridge.CmSprime`); (ii) every one of the new module's `#print axioms`
lines reports a subset of `{propext, Classical.choice, Quot.sound}`; (iii) no `sorryAx` anywhere and `lean-axioms`
passes. BUILT ⇒ the compact-form statements (`theorem_Sprime_compact`, its inequality and `ℂ⁴` forms, the two
inclusions, the control) are CONJECTURE [D], and the rows conditional on "S′ for compact Z [W]" (C13.1, C13.5, C13.7,
C16.4; C21.1's `Kk`) become conditional on [D] **plus** the [W] Carathéodory remark identifying `surgeryC` with
`K(Z)`. Not BUILT ⇒ the text is kept as `lean/CmSprimeCompact.run<id>.lean`, the error lines recorded, one repair
dispatch may follow; not BUILT after two ⇒ C22 FAILED (design), the compact form stays [W], and the closedness lemma /
two-sided inclusion are recorded at whatever the log shows elaborated (per declaration, by its `#print axioms` line).
Nothing about the compact form is cited as [D] before a green dispatch (owner's requirement (1)).

Predictions (stated plainly): the module builds at the first dispatch with probability about one half; if not, the
likeliest failure sites are the limit bookkeeping (`IsCompact.tendsto_subseq`, `Tendsto.comp` along a strictly monotone
subsequence, `tendsto_nhds_unique`), the subtype-indexed sums of the finite surgery, and `simp` normal forms in the
entry bounds — not the mathematics; every `#print axioms` line within the permitted three; the gate red on
`lean-manuscript` (two modules without census family) and on no other step.

## Runs (written 2026-10-11T10:13:34Z, `date -u`)

### Preflight
Run 1 (07:53:29Z) crashed before any check printed (harness: the square-only `matmul` on a 4×1 factor in Q1's
countercontrol), kept as `c22_preflight.run1.*`. Run 2 (07:53:41Z) 7/8: Q5's prediction refuted — S0 said two
non-antipodal Bell-type defects at `c = 2` pair to "`4s − 4 < 0`"; the pairing is `4 − 2c − 2c + c²s = 4s ≥ 0`, an
arithmetic slip; what excludes the Bell circle is (CC) (`4s ≥ 4` needs `s = 1`), as NOTES-C11 Remark (iii) says; kept as
`c22_preflight.run2.*`. Run 3 (07:54:17Z), Q5 amended to the correct statement and nothing else changed: 8/8,
`VERDICT C22-PREFLIGHT-OK`; replay byte-identical. Measured: `ε² = 3969/850000` for the eight-point net of the S2 circle
(`c = 21/20`); `y = d_{w₀}`, `w₀ = (15 + 8i)/17`, pairs `−1/74` with an exact pure member of `Q ∩ F*` in its own cap (so
`y ∉ K(F)*`), while `η² = 3969/53125 ≥ 1/5476` (the shift restores membership).

### Design runs under S0 (two dispatches)
| dispatch | run | job | head | Build | `CmSprimeCompact` prints | errors |
|---|---|---|---|---|---|---|
| 1 | `38124380741` | `114425574221` | `6cb76f96` | FAILED | 38: 32 standard, 6 `sorryAx` (error recovery; 4 inherited) | 90:42 invalid projection (`zero_mem_coneOf`); 375:79 unsolved goals (`mem_box`); 536:11 expected token (`q∞` is not an identifier) |
| 2 | `38125067948` | `114427630399` | `e4ef2e46` | FAILED | 38: 32 standard, 6 `sorryAx` (`mem_box` and the five declarations that use it) | 377:2 `simp` made no progress (`mem_box`: membership instance at `Matrix n n ℂ` against `Set (n → n → ℂ)`) |

`CmSprime` (the finite module, unchanged) printed all 78 lines on the three permitted axioms in both runs. Dispatched
texts kept: `lean/CmSprimeCompact.run38124380741.lean` (`d24b7ea8…`), `lean/CmSprimeCompact.run38125067948.lean`
(`5b447af0…`). **S0 verdict: not BUILT after two dispatches ⇒ C22's S0 design run is FAILED (design)**; by the S0 rule
the compact form stays [W]. Per declaration (S0's fallback clause), run 2 shows on the standard axioms: `K ⊆ K*`
(`surgeryC_subset_dualH`), the pairing estimate `abs_pr_le` (with `abs_qf_le`), the entry bounds
(`norm_entry_le_pr_one`, `norm_entry_defect_le`, `norm_entry_coneOf_le`), finite nets (`exists_net`), compactness of the
entry boxes (`isCompact_box`), `isClosed_psd`, the pairing lemmas over the closed hull and `continuous_defect_family`;
the engine `dualH_subset_surgeryC_of_finite` reached no error of its own and carries `sorryAx` only through
`mem_box` — which is not a statement about the engine's proof being checked (a declaration that uses a sorried lemma is
not machine-checked), so nothing beyond the listed declarations is [D] from these runs.

## Amendment A1 (written 2026-10-11T10:13:34Z, before the third dispatch)

**Why.** S0 held the round's third dispatch for C23. C23's design (NOTES-C23, S0) is exact arithmetic with a plain
certificate and an independent checker; it uses no Lean module, so the held dispatch is not needed there. The
coordinator's message of 10:06Z authorizes spending it "only on a module whose every error from run 38125067948 is
diagnosed and repaired with the names checked in the pinned sources". The single error is diagnosed (LOG entry 2026-10-11T10:13:10Z):
`mem_box` is repaired by definitional unfolding of the membership and the ball condition through `Metric.mem_closedBall`,
`dist_zero_right`, `Eq.trans_le`, `forall_congr'`, `Iff.trans`, `Set.mem_univ`, each grep-checked in the pinned Mathlib;
no other declaration changes (`diff` against the run-2 text: `mem_box`'s three proof lines replaced by seven).

**What does not change.** The S0 verdict above stands: C22's S0 design run is FAILED (design) and is recorded as such.

**Decision rule for the amendment run (fixed now).** One dispatch (the round's third and last). **BUILT** iff (i) the Build
step succeeds with `Built OIBridge.CmSprimeCompact`; (ii) all 38 of its `#print axioms` lines report a subset of
`{propext, Classical.choice, Quot.sound}`; (iii) no `sorryAx` and `lean-axioms` passes. BUILT ⇒ the compact-form
statements of the module (`theorem_Sprime_compact`, `_ineq`, `_C4`, the two inclusions, `control_compact_single_defect`)
are CONJECTURE [D] **by the amendment run**, recorded in their own row with the amendment named, and the rows that rest on
"S′ for compact Z [W]" become conditional on that [D] statement plus the written Carathéodory remark (which identifies
`surgeryC` with `(Q ∩ Z*) + cone Z`) — the remark stays [W]. Not BUILT ⇒ the compact form stays [W]; the declarations
on the standard axioms in the last run are recorded [D] individually; no further dispatch.

**Prediction (fixed now).** BUILT, with every `CmSprimeCompact` print standard and the gate red only on
`lean-manuscript` (two modules without a census family) — confidence moderate (the repaired lemma is the only changed
declaration and the rest elaborated in run 2; the residual risk is in the elaboration of the membership unfolding).

### Amendment run (written 2026-10-11T10:23:29Z)
| dispatch | run | job | head | Build | `CmSprimeCompact` prints | `lean-axioms` | gate red steps |
|---|---|---|---|---|---|---|---|
| 3 (A1) | `38131214451` | `114445772534` | `a69987bd` | success, `⚠ [3645/3647] Built OIBridge.CmSprimeCompact (4.4s)` (warnings only) | 38/38 `[propext, Classical.choice, Quot.sound]` | PASS (5976 named results, no `sorryAx`) | `lean-manuscript` only (2 problems: `CmSprime`, `CmSprimeCompact` have no registry family — local read-only rerun of the census tool) |

By A1's rule the run is **BUILT**; A1's prediction held.

## Results

### C22-1 — Theorem S′ for compact defect families, design-built [D by Amendment A1]
`theorem_Sprime_compact` (`OIBridge.CmSprime`, `lean/CmSprimeCompact.lean`, sha256 `2f12f6e8…`): for a topological
space `κ` that is **compact** and **nonempty**, a nonempty finite index type `n`, **continuous** `c : κ → ℝ` and
**continuous** seed map `h : κ → ℂⁿ` with **unit** seeds, **`1 < c k ≤ 2`**, **`c k < card n`**, **pairwise nonnegative trace
pairings** `pr (d j) (d k) ≥ 0` (all `j, k`) and **(CC) in cap/co-cap form on every ordered pair `j ≠ k` of positive
pairing**, the surgery with the **closed** conic hull `surgeryC d = (Q ∩ Z*) + closure (cone Z)` is closed and equal to
its dual inside the Hermitian matrices under `Re tr(AB)`. Also: `theorem_Sprime_compact_ineq` ((CC) in the inequality
form `(√(c_j − 1) + √(c_k − 1))² ≤ c_jc_k|⟨h_j|h_k⟩|²`), `theorem_Sprime_compact_C4` (`ℂ⁴`, `c k < 4` automatic), the two
inclusions `surgeryC_subset_dualH` (`K ⊆ K*`, needs only Hermitian members and pairwise nonnegative pairings) and
`dualH_subset_surgeryC_of_finite` (`K* ⊆ K` from the finite self-duality of every finite subfamily, a uniform trace bound
`τ > 0` and a uniform entry bound), the quantitative estimate `abs_pr_le` (`|pr q M| ≤ ε · card n · tr q` for `q ⪰ 0`,
`max |M_ij| ≤ ε`), and the non-vacuity control `control_compact_single_defect`. Machine-checked in a design module built
against L (run `38131214451`), outside the certified chain, no census disposition: **CONJECTURE [D]**.

### C22-2 — which step needed a new argument (the answer to the node's question) [D + W]
The finite engine (Farkas by the infimum of ratios, the least-weight decomposition, the local lemma) survives
unchanged as a black box: it is applied to finite ε-nets of the compact family. The only new arguments are (i) the
pairing estimate `abs_pr_le` (through the factorization `q = BB†` and Cauchy–Schwarz), (ii) the shift: for `y ∈ K*` and
an ε-net `F`, `y + ηI ∈ (K_F)*` once `η ≥ ε · card n · tr(y)/τ` — exact instance in the preflight (Q4d: `y = d_{w₀}` is
outside `(K_F)*` and the shift restores it), and (iii) the limit along `ε → 0` in compact entry boxes with two
subsequences. Farkas over a compact family, a least-weight decomposition over a compact family, a separation theorem and
Carathéodory are **not** needed for the statement with the closed hull. Carathéodory is needed only for C22-3. [D] for
(i)–(iii) as parts of the built module.

### C22-3 — the closedness of the conic hull over a compact base [W + L]
*If `Z ⊂ Herm(n)` is compact and `tr d ≥ τ > 0` on `Z`, then `cone Z` (finite nonnegative combinations) is closed; hence
`surgeryC d = (Q ∩ Z*) + cone Z = K(Z)`, the surgery as NOTES-C11/C13 define it.* Proof: by Carathéodory in `Herm(n)` (real
dimension `n²`) every point of `conv Z` is a convex combination of at most `n² + 1` points of `Z`, so `conv Z` is a
continuous image of `Δ_{n²} × Z^{n²+1}`, compact; `cone Z = {t x : t ≥ 0, x ∈ conv Z}`; if `t_m x_m → y` then
`t_m τ ≤ tr(t_m x_m)` is bounded, so along a subsequence `t_m → t`, `x_m → x ∈ conv Z`, and `y = t x ∈ cone Z`. ∎
[W]; Carathéodory [L: Mathlib `convexHull_eq_union`, Analysis/Convex/Caratheodory.lean:149 at the pinned version, read,
not used in the module]. Not machine-checked (not in the module).

### C22-4 — consumers: the circle cones, with every link's side hypotheses checked (round-4 audit's chain rule)
Chain: link 1 `theorem_Sprime_compact_ineq` [D by A1] — side hypotheses: compact nonempty `κ`, continuous `c` and seed
map, unit seeds, `c ∈ (1, 2]`, `c < 4`, pairwise pairings `4 − 2c + c²s ≥ 0`, (CC) `c²s ≥ 4(c − 1)` on positively paired
pairs (equal `c`; monotone in `s`, so checked at `s_min`); link 2 C22-3 [W] (to read the result for `K(Z) = (Q ∩ Z*) +
cone Z`).

| cone | `κ` (compact, continuous injective parametrization) | `c` | `s_min` (source) | pairings `≥ 0` | (CC) |
|---|---|---|---|---|---|
| C13.7 (S2 circle, level (i)) | `S¹`, `w ↦ (3, 3, w, −w)/√20` | `21/20` | `16/25` (C13 R4 [X]; symbolic `82 + 18 cos t` in C22 Q4a [X]) | `4 − 21/10 + (441/400)(16/25) > 0` | `(441/400)(16/25) = 441/625 ≥ 1/5` ✓ |
| C13.5 (case A, three circles) | three copies of `S¹`, `θ ↦ √p b̂₃ + √(1 − p) e^{iθ} b̂_j` | `251/250` | `(36/49)²` (C13 R2, CC2 [X]; orbit formulas [W]) | positive (C13 CC2) | checked exactly in C13 (R2) |
| C16.4 (`K_κ` = C21's `Kk`, two circles) | `{±1} × S¹`, `(σ, x) ↦ (6, 2σ, x, −σx)/√42` | `103/100` | `256/441` (C16 K2 [X]) | positive (C16 K4) | `c²s_min = 169744/275625 ≥ 3/25` (C16 K4 [X]) |

So the rows that rested on "S′ for compact Z [W]" (C13.1, C13.5, C13.7, C16.4, and C21.1 for `Kk`) rest on C22-1 [D] with the
side hypotheses as tabled, plus C22-3 [W] for the identification with the cones as those rows define them. Their labels
do not change (CONDITIONAL); the condition moves from a written proof of the theorem to a design-built statement plus a
written closedness remark.

### C22-2f — the S0 design run
Two dispatches under S0 did not build (errors as tabled above); by S0's rule **FAILED (design)**, kept with evidence
(`lean/CmSprimeCompact.run38124380741.lean`, `lean/CmSprimeCompact.run38125067948.lean`). C22-1's [D] is the amendment
run's, not S0's.

## Hypothesis classification
Cone geometry: no OI inventory item; no introduced hypothesis (H1–H3, A_miss, claim (D), EBF, T do not appear). Every
hypothesis of the compact form is explicit in the module's statement (owner's requirement (1)). Reading of downstream
uses: invariance (the circle cones are pair cones; nothing here is about availability).

## Gem classification (§A.31)
- NEW: the compact form reduces to the finite engine by finite ε-nets with one quantitative estimate and a shift; the
  closedness of the conic hull (Carathéodory) is needed only to identify the closed-hull form with `(Q ∩ Z*) + cone Z`,
  and is isolated as a written remark. The productivity test is met: a fact strictly stronger than "S′ holds for compact
  Z" (the decomposition of the proof into a machine-checked core and one named written remark), and it constrains the
  circle cones' evidence (C22-4).
- Process: S0's Bell-circle prediction (Q5) carried an arithmetic slip (FAILED, kept); the S0 design run FAILED after two
  dispatches on elaboration details; the amendment run built.

## What is not claimed
No kernel statement and no census disposition; C22-3 is [W] + [L]; necessity of (CC) is not stated; extremality of the
defects (C13-S) is not in the module; nothing about OI's premises.
