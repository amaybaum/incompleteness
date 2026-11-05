# OI-QM-SEL M-1: verification of the alternating-W candidate (preregistration)

**Status: WIP / UNVERIFIED. Preregistration, frozen at the commit that adds this file.** Paper-only. Writer: `writer-m1`,
the sole writer of this unit. Independent review is pending; merge is not authorized.
**Base:** `origin/main` `f051916a113c9412b3efbb1ff813ec57c2ed265d`. Every path:line below is read at this base.
**Method:** reading and hand algebra in exact arithmetic only (integers, `½`, `¼`, `1/√2`, `i`). No script, CAS,
numerical evaluation, enumeration or search over matrices. No Lean work.
**Order of work:** this file is committed and pushed before any law, relative object, Gram datum of the alternating
lifts or target-QM mass is written out. The results go in `RESULT.md` in this directory, in a later commit that changes
no other file. Nothing in §§2–6 is changed after this commit. If a control fails, the verdict is VOID (§6). If the
candidate fails, no other pair is substituted.

## §0. Authorization

Owner ruling, #1031 comment 6665461411 (amaybaum, Claude Code session chat, 2026-11-05, about 18:45Z by the ruling's own
header; comment posted 18:05:55Z), pointer on #1143 comment 6665466217 (18:06:10Z). Quoted verbatim:

> **#1143 M-1.** Authorize one paper-only verification of the alternating-W candidate: U=(I,W,I,W,…), U′=(I,W′,I,W′,…). Freeze the pair, mathematical definitions, controls and outcome rules before checking. The record must determine whether C0 laws agree, whether the lifts are gauge-related, whether the target quantum procedures distinguish them, and what C2-ch and C2-sel actually observe. A positive result may establish a scoped PPer mathematical counterexample. It does not establish physical availability or native OI realizability. No numerical search, Lean work or manuscript promotion is authorized.

and, from the M-2 paragraph of the same ruling:

> If M-1 fails, do not silently substitute another pair. Independent review is required for each result.

**Not authorized here:** any other pair; any search; Lean work; manuscript edits or theorem promotion; a change to the
B4′ matrix (a change is proposed in `RESULT.md` only); M-2's evaluation (C-pers is not evaluated here); merge.

## §1. Definitions used, with their sources on `main`

Abbreviations (kernel files under `verification/lean-mathlib/OIBridge/`): TSG `TwoSidedGauge.lean`; CLG
`CoherentLiftGauge.lean`; DC `DilationChoice.lean`; RC `RootedClassification.lean`; RCAT
`RootedClassificationAllTime.lean`; CR `CausalReadback.lean`; TB `TransposeBridge.lean`. Paper records under
`verification/programmes/oi-qm/reconstruction/`: B4 `bsel-2-b4prime-20261105/B4PRIME.md`; SC
`bsel-2-b4prime-20261105/SCOPE.md`; QP `bsel-2-q2a-ce-20261105/PREREG.md`; RES `bsel-2-q2a-ce-20261105/RESULT.md`.

**Carrier and lifts.**
- `V = {0,1}`, `A ⊇ {a₀,a₁}`, carrier `V × A`, fixed anchor `a₀`; `e_v := e_{(v,a₀)}`, `𝒜 := span{e_v}`, `C := 𝒜^⊥`;
  fibre projector `P_w := |w⟩⟨w| ⊗ 1_A` (B4 ll. 33–34; SC l. 102).
- A lift is `U = (U_t)_{t∈ℕ}` with every `U_t` unitary on `ℂ^{V×A}`; ∀U ranges over all such families (B4 l. 35; SC
  ll. 109–111).

**Gauge.**
- `LeftFibreGroup L`: `L` unitary and `L p q = 0` whenever `p.1 ≠ q.1` (TSG:78–79).
- `WeakAnchorStabilizer a₀ K`: `K` unitary and `K p (j,a₀) = c_j` if `p = (j,a₀)`, else 0 (CLG:114–116); `|c_j| = 1`
  (`weak_anchor_coeff_norm_one`, CLG:146).
- `G(U,U′)` := `TwoSidedRelated a₀ U U′`: there are `L_t`, `K_t` with `LeftFibreGroup (L_t)`, `WeakAnchorStabilizer a₀
  (K_t)` and `U′_t = L_t U_t K_t` for **every** `t` (TSG:84–87).

**Fibre-Gram data and phase equivalence.**
- `FG^{(i)}(X)(j,k) := FibreGram a₀ X i j k = Σ_a conj(X((i,a),(j,a₀))) · X((i,a),(k,a₀))` (TSG:95–97; `fibreGram_apply`
  TSG:115–116). Diagonal `fibreGram_diag` (TSG:127–128); `Σ_i FG^{(i)} = 1` for unitary `X` (`sum_fibreGram`,
  TSG:153–154); rank `≤ |A|` (`fibreGram_rank_le`, TSG:146).
- `GramPhaseEquiv G G′`: some `c : V → ℂ`, `|c_j| = 1`, with `G′ i j k = conj(c_j) G i j k c_k` for all `i, j, k`
  (TSG:102–103).
- Gram invariant of a slice: `g(X) := FG^{(0)}(X)(0,1) = ⟨P₀Xe₀, P₀Xe₁⟩`, conjugate-linear in the first slot (QP l. 66).
- Kernel theorems used: `gramPhaseEquiv_of_twoSided` (TSG:263–265, forward); `twoSided_slice_iff` (TSG:826–830, `mpr`
  named if used); `twoSidedRelated_iff` (TSG:839–843, direction named where used).

**Readback and visible family.**
- `Γ_t(w,v) := Σ_a |U_t((w,a),(v,a₀))|² = ‖P_w U_t e_v‖²`; rows `w` (record), columns `v` (root) (B4 l. 40; DC:86–87,
  DC:134–136). `AdmissibleDilationAt (Γ t) a₀ (U t)` fixes `Γ t` entrywise from `U t` (DC:134–136), so the visible family
  of a coherent lift (`CoherentLift`, CLG:124) is this `Γ`.
- Anchored moduli `α_t(w,j) := |⟨e_w, U_t e_j⟩|²`; relative object `T_{t,s} := U_t U_sᴴ`; relative readback
  `𝒪₂(t,s)(w,v) := ‖P_w T_{t,s} e_v‖²`; `β_{t,s}(w,v) := |⟨e_w, T_{t,s} e_v⟩|²` (B4 ll. 42–44).

**Class `PPer`** (RC:32–33): `Γ 0 = 1`, `IsRowStochastic (Γ t)` for every `t`, and `PeriodicFamily Γ` (some `M > 0`
with `Γ (t+M) = Γ t` for all `t`, RC:27–28). `IsRowStochastic M`: nonnegative entries and every row sums to 1
(CR:48–49). Orientation: the kernel's realization maps `rootedMap R t a j` have the root `a` as row index (CR:190–192),
while `Γ_t` above has the root as column index. Per SC l. 135 and B4 l. 496 (W9), membership is checked for the family `Γ` and for
the transposed family `(Γ_tᵀ)_t`, so that it holds in either orientation.

**Procedures** (SC ll. 112–119, frozen; readings B4 ll. 57–62).
- H-comp: root to the first read at `t₁` by `U_{t₁}`; between reads at `s < t` by `T_{t,s}`.
- Acc₁: one read at one time. Acc₂: any finite increasing read list `t₁ < … < t_k`, `k ≥ 1`, `t_m ∈ ℕ`, all records kept
  jointly.
- P-conf: root `|j,a₀⟩ = e_j`, each `j ∈ V` separately, laws indexed by `j`.
- Rd: Lüders read by `P_v`, record `v`.
- Rst-ch: after each read the ancilla is replaced by `|a₀⟩`. Rst-sel: after each read (reading (r2): the last read
  included) an `|a₀⟩⟨a₀|` test `Π := 1_V ⊗ |a₀⟩⟨a₀|`; `⊥` is kept with its mass and not continued.
- (r1): for one-time candidates, the state at a read at `t` is `U_t` applied to the root (B4 ll. 57–59).
- Candidates (SC ll. 120–124): C0 = (P-conf, Acc₁, Rd); C2-ch = (P-conf, Acc₂, Rd, H-comp, Rst-ch); C2-sel = (P-conf,
  Acc₂, Rd, H-comp, Rst-sel).

**Complete-record laws.** `Λ_C`: "every branch mass and every failure record `⊥`, unnormalized and unconditioned"
(SC ll. 24–25). `O_C(U,U′)` is `Λ_C(U) = Λ_C(U′)`. The target statement `Q[C]`:
`∀U,U′: O_C(U,U′) ⇒ G(U,U′)` (SC l. 129), here in the `PPer` class at `|V| = 2`, `|A| ≥ 2` (B4 rows l. 517, l. 523,
l. 526, all "not addressed").

**Target-QM procedures** (from the reviewed #1143 specification, c.6665278924 §1.4; restated in full here, and used
in this restated form only).
- **T-V (primary).** QM on `V`, with `A` an inaccessible environment in `|a₀⟩` at the root. Preparations: every
  `ρ ⊗ |a₀⟩⟨a₀|`, `ρ` a density matrix on `V`. Readouts: every finite instrument on `V`, acting as (Kraus operator)
  `⊗ 1_A`. Dynamics: the lift, composed by H-comp. `A` persists between reads (no reset). Every branch mass is kept,
  unnormalized.
- **T-V+R.** T-V together with a declared ancilla reset (Rst-ch or Rst-sel) after reads. It is used only where C2-ch or
  C2-sel is compared with QM. Every T-V procedure is a T-V+R procedure.
- T-full (arbitrary procedures on `V ⊗ A`) is excluded: a separation that only T-full achieves does not count.
- **Lifts T-V-distinct:** some T-V procedure gives some record unequal masses for the two lifts.

**Status of the sources.** B4's header (l. 3) reads "WIP / UNVERIFIED (complete draft, not reviewed)", and RES's
reads "Independent review pending"; the reviews of both are recorded only in GitHub comments (provenance, §A.42 item 2).
This record therefore takes from B4, SC, QP and RES only **definitions, notation and the frozen matrices** `W`, `W′`,
`L`, `K`. It takes no derived result of B4 or RES as a premise (§A.46 item 7): every law, Lemma R, the witnesses WB and
WE used as controls, and the T-V separation are re-derived in `RESULT.md` from the procedures and kernel lines above.
B4's W0 formulas (ll. 71–127) are a cross-check only.

## §2. The frozen pair

**Basis order** (QP ll. 94–95): `p₀ = (0,a₀)`, `p₁ = (0,a₁)`, `p₂ = (1,a₀)`, `p₃ = (1,a₁)`. Rows and columns of every
matrix are in this order. `e₀ = e_{p₀}` and `e₁ = e_{p₂}` (QP ll. 97–98).

**The slices** (exactly QP ll. 107–125; `W = H₄/2`, and `W′` is `H₄/2` with its columns at `p₁` and `p₂` exchanged):

```
I = [ 1  0  0  0 ]      W = ½ · [ 1   1   1   1 ]      W′ = ½ · [ 1   1   1   1 ]
    [ 0  1  0  0 ]              [ 1  −1   1  −1 ]               [ 1   1  −1  −1 ]
    [ 0  0  1  0 ]              [ 1   1  −1  −1 ]               [ 1  −1   1  −1 ]
    [ 0  0  0  1 ]              [ 1  −1  −1   1 ]               [ 1  −1  −1   1 ]
```

**The lifts.** Defined for every `t ∈ ℕ` (no finite horizon; every finite read list is covered):
- `U_t := I` for even `t` and `U_t := W` for odd `t`: `U = (I, W, I, W, …)`;
- `U′_t := I` for even `t` and `U′_t := W′` for odd `t`: `U′ = (I, W′, I, W′, …)`.

This is B4's alternating placement (B4 ll. 229–230) with `M = W` and `M = W′`. `|V| = 2`, `|A| = 2`, anchor `a₀`.

**Extension to `|A| = m ≥ 3`** (as QP l. 128): `A = {a₀, …, a_{m−1}}`; slices `I`, `W ⊕ 1`, `W′ ⊕ 1`, the identity on
the `2(m−2)` added basis vectors `(v,a)`, `a ∉ {a₀,a₁}`; the same alternating placement.

**Control elements** (fixed now).
- `L := 1_V ⊗ H₂`, `H₂ = (1/√2)[[1,1],[1,−1]]` on `{a₀,a₁}` (QP ll. 131–138), and `K := diag(1, −1, i, 1)` (QP l. 140).
- Gauge-control lift `U^c`: `U^c_t := I` for even `t`, `U^c_t := L W K` for odd `t`. Witnessed `G(U,U^c)` by
  `L_t = L, K_t = K` at odd `t` and `L_t = K_t = I` at even `t`.
- T-V gauge-control lift `U^M`: `U^M_t := L U_t` for every `t` (so `U^M_0 = L`, `U^M_1 = LW`). Witnessed `G(U,U^M)` by
  `L_t ≡ L`, `K_t ≡ I`.
- Sensitivity witnesses, restated from their definitions (their laws are re-derived in RESULT, not cited):
  - **WE** (B4 ll. 332–333): `U^E_0 = I`, `U^E_t = P := swap(p₁, p₃)` for `t ≥ 1`; its gauge image `L·U^E` (`L_t ≡ L`,
    `K_t ≡ I`).
  - **WB** (B4 l. 285): on `|V| = 2`, `|A| = 2`, `U^B` = alternating `H₂ ⊕ 1_C` (`H₂` on `span{e₀,e₁}`, identity on
    `p₁, p₃`); its gauge image with `L_t ≡ I`, `K_t = Z := diag(1,1,−1,1)` (`−1` at `p₂ = (1,a₀)`) at odd `t`, `I` at
    even `t`.

## §3. The T-V separating procedure (stated now)

- **T-sep₁.** Root `ρ₊ ⊗ |a₀⟩⟨a₀|` with `|+⟩ = (e₀ + e₁)/√2 = (e_{p₀} + e_{p₂})/√2`; evolve by `U_1` (H-comp root clause);
  one Lüders read by `P_v` at `t = 1`, record `v ∈ {0,1}`. Masses `‖P_v U_1 |+⟩‖²` for both lifts.
- **T-sep₂ (frozen fallback; used iff T-sep₁ gives equal masses).** As T-sep₁ with `|+i⟩ = (e_{p₀} + i e_{p₂})/√2`.
- **T-sep₃ (frozen second fallback; used iff T-sep₁ and T-sep₂ give equal masses).** If `FG^{(i)}(W) ≠ FG^{(i)}(W′)` for
  some `i`, the root `|x⟩⟨x| ⊗ |a₀⟩⟨a₀|` for an explicit unit `x ∈ ℂ^V` with `⟨x, (FG^{(i)}(W) − FG^{(i)}(W′)) x⟩ ≠ 0`,
  one read at `t = 1`; `x` is exhibited and both masses are written out.
- If none applies (`FG^{(i)}(W) = FG^{(i)}(W′)` for both `i`), the T-V question is reported **NOT-DETERMINED** by this
  record: multi-time T-V procedures with a persisting ancilla are M-2's object and are not evaluated here.

All three are T-V procedures by the definition of §1 (a T-V preparation, one Lüders instrument on `V`, the lift's
dynamics, no reset). They are also T-V+R procedures.

## §4. Controls and pass criteria

All arithmetic exact; every control written out in full in `RESULT.md`. Mapping to the #1143 specification's controls:
K-c ↔ spec K1 (gauge, mathematical form); K-d ↔ spec K2; K-g ↔ spec K5's T-V re-derivation with spec K1's T-V form and
K11's sensitivity form; K-h ↔ spec K5; spec K7 (unnormalized, `⊥` kept) is part of K-e.

- **K-a (unitarity).** Pass iff `WᴴW = 1` and `W′ᴴW′ = 1` (all 16 entries each), `LᴴL = 1`, `KᴴK = 1`, `(LWK)` unitary
  as a product, `P` and `H₂ ⊕ 1_C` unitary, and `X ⊕ 1` unitary for the extension.
- **K-b (`PPer` membership of the visible family, from the kernel definitions).** Pass iff, for the visible family `Γ`
  of `U` (and of `U′`), computed entrywise from the slices by DC:134–136:
  - `Γ_0 = 1` (RC:33);
  - for every `t`, `Γ_t` and `Γ_tᵀ` have nonnegative entries and every row sums to 1 (CR:48–49);
  - `Γ_{t+2} = Γ_t` for every `t` (RC:27–28, `M = 2`).

  The same is reported for `U^c` and `U^M`.
- **K-c (positive gauge control).** Pass iff all hold:
  - `L` satisfies `LeftFibreGroup` (TSG:78–79) and `K` satisfies `WeakAnchorStabilizer a₀` (CLG:114–116), with
    `c = (c₀, c₁)` stated; `G(U, U^c)` by the witnesses of §2 (TSG:84–87);
  - `FG^{(i)}(LWK)(j,k)`, computed entrywise from the matrix `LWK`, equals `conj(c_j) FG^{(i)}(W)(j,k) c_k` for all
    eight `(i,j,k)`;
  - hence `Γ_t(U^c) = Γ_t(U)` and `|g(U^c_t)| = |g(U_t)|` for every `t`, and `Λ_C0(U^c) = Λ_C0(U)`.

  Purpose: on a pair related by construction, the hand Gram and C0 computations report no difference.
- **K-d (`|A| = 1` countercontrol).** Pass iff (i) for at least one of `W`, `W′`, `P₀Xe₀` and `P₀Xe₁` are not
  collinear, i.e. `|g|² ≠ Γ(0,0)·Γ(0,1)` for that member (the pair uses `|A| = 2`); and (ii) at `|V| = 2`, `|A| = 1` every
  unitary has `|g|² = Γ(0,0)Γ(0,1)`, re-derived, so equal `Γ` forces equal `|g|` there and the pair contradicts nothing
  proved at `|A| = 1`.
- **K-e (complete-record laws: computation and coverage).** Pass iff `RESULT.md` computes, for both lifts, from the
  procedures of §1 by explicit unnormalized branch states (not from B4's W0 formulas):
  - **C0:** for each root `j` and each `t ∈ ℕ`, every record mass;
  - **C2-ch:** for each root `j`, every finite read list `t₁ < … < t_k` (`k ≥ 1`, any times in ℕ, so every pattern of
    parities of consecutive read times, including reads at `t = 0`) and every record `(v₁,…,v_k)`, the branch mass;
  - **C2-sel:** for each root, every read list and every record — every all-ok record and every record ending in one
    `(v_m,⊥)`, `1 ≤ m ≤ k` — the unnormalized mass; the `⊥` masses are computed, not only the ok masses;
  - **bookkeeping:** for each lift, root and read list, the masses over all records sum to 1;
  - **cross-check:** the computed masses agree with B4 W0.1, W0.4 and W0.5 (a disagreement fails K-e);
  - **coverage:** an argument valid for every `k` and every read list, stated, not sampled.

  K-e passes or fails on completeness and bookkeeping. Whether the laws are equal is a result, used by §6.
- **K-f (sensitivity of the law computation).** Pass iff the per-step rules used in K-e, applied to the WE pair
  `(U^E, L·U^E)`, give: under Rst-ch, root `j = 0`, reads `(0,1)`, records `(0,0)` and `(0,1)` with masses `(1, 0)` for
  `U^E` and `(½, ½)` for `L·U^E`; under Rst-sel, root `0`, one read at `0`, `(0,ok)` mass `1` against `½` and `(0,⊥)` mass
  `0` against `½`; and, for C0, the pair `(U, I)` (the identity lift) gives `Γ_1 = Γ(W)` against `1`, with the
  difference reported. The expected WE values are those stated at B4 ll. 335–347 and are re-derived, not assumed.
- **K-g (T-V: separation, gauge control, sensitivity).** Pass iff all hold:
  - **(g1) computation:** T-sep₁ (and, if triggered, T-sep₂, T-sep₃ in order) is computed for both lifts, both records,
    with the unnormalized branch states written out;
  - **(g2) T-V gauge negative control:** T-sep₁ gives equal masses for `U` and `U^M`; and a general argument, re-derived,
    shows that every T-V procedure (any preparation, any finite instrument sequence on `V`, any read list, persisting
    `A`) gives `U` and `U^M` equal laws;
  - **(g3) T-V sensitivity:** T-sep₁ applied to WB (`U^B` against its gauge image) gives the masses `(1,0)` against
    `(0,1)` (B4 ll. 286–288), re-derived.
- **K-h (independent re-derivation; definitions).** Pass iff `RESULT.md` derives from the kernel lines and definitions of
  §1 only, every step cited:
  - **Lemma R (a ⇒ b)**, for unitary slices `X, X′` at `|V| = 2`: `X′ = L X K` with `L ∈ LeftFibreGroup`, `K` weak ⇒
    `Γ(X) = Γ(X′)` and `|g(X)| = |g(X′)|` (via TSG:263–265 and the definition TSG:102–103);
  - **Lemma R (b ⇒ a)**, written out only if §6's branch (P2-eq) is reached (via `sum_fibreGram`, TSG:153, and
    `twoSided_slice_iff` `mpr`, TSG:826–830);
  - every definition used matches its source line; no off-`main` content and no B4 or RES derived result is a premise.
- **K-i (extension, scope only).** For `|A| = m ≥ 3`, every quantity of K-b, K-e, K-g (g1) and the Gram invariant is
  shown unchanged. A failure of K-i does not void the verdict; it restricts the verdict's scope to `|A| = 2`.

**Gauge determination.** `g(W)` and `g(W′)` (the odd slices; the even slices are both `I`) are computed exactly.
- If `|g(W)| ≠ |g(W′)|`: `G(U,U′)` would require `W′ = L_1 W K_1` (TSG:84 at `t = 1`), hence by Lemma R (a ⇒ b)
  `|g(W)| = |g(W′)|`; so **¬G** (branch P2-neq).
- If `|g(W)| = |g(W′)|` and `Γ(W) = Γ(W′)`: Lemma R (b ⇒ a) relates the odd slices, the even slices are related by
  `L = K = I`, and `G` holds (branch P2-eq).

## §5. What is reported regardless of the verdict

- **C0:** LAWS-EQUAL or LAWS-DIFFER, with a separating root, time and record if they differ.
- **Gauge:** `|g(W)|`, `|g(W′)|`, and G or ¬G.
- **T-V:** T-V-DISTINCT[the first procedure of §3 that separates, with its masses] or NOT-DETERMINED. T-V+R inherits
  T-V-DISTINCT, since every T-V procedure is a T-V+R procedure.
- **C2-ch and C2-sel (what they observe):** for each, LAWS-EQUAL or LAWS-DIFFER (with the first separating root, read
  list and record, and both masses, `⊥` included), and a closed-form statement of which data of the lift the law is a
  function of on this pair (for example `Γ`, `𝒪₂`, `α`, `β` at the relevant time pairs), and which data of the pair
  that distinguish the lifts (the fibre-Gram off-diagonals, the T-sep masses) do not enter it.
- The K-b visible family, with orientation, and the K-i scope.

## §6. Decision rule (fixed)

Conditions:
- **(P1)** `Λ_C0(U) = Λ_C0(U′)` (K-e).
- **(P2)** ¬G(U,U′) (branch P2-neq of §4).

Verdicts:
- **VOID** iff any of K-a, K-b, K-c, K-d, K-e, K-f, K-g or K-h fails or is vacuous, or a definition reads differently
  from its source line, or an entry is not exact. On VOID the B4 cells ll. 517, 523, 526 stay "not addressed".
- **COUNTEREXAMPLE** iff no VOID condition holds and (P1) and (P2) hold. The verdict text is
  COUNTEREXAMPLE[`𝒞`; `PPer`; `|V| = 2`, `|A| ≥ 2` (or `|A| = 2` if K-i fails); alternating lifts `U = (I,W,I,W,…)`,
  `U′ = (I,W′,I,W′,…)`; equal complete-record laws; not two-sided related; T-V: `τ`], where
  - `𝒞` = C0, followed by each of C2-ch and C2-sel whose laws are LAWS-EQUAL (K-e);
  - `τ` = DISTINCT[procedure] or NOT-DETERMINED (§3).

  For each `C ∈ 𝒞`, `Q[C]` (O⇒G) is then false at the stated scope in the class `PPer`.
- **NOT-A-COUNTEREXAMPLE** iff no VOID condition holds and (P1) or (P2) fails. The verdict names which failed. The C2
  and T-V reports of §5 are still given. No other pair is examined or proposed in this record.
- No other verdict is available. Nothing in §§2–6 is adjusted after this commit.

## §7. Scope

- **A COUNTEREXAMPLE would establish** a paper-level mathematical counterexample to `Q[C]` for the `C ∈ 𝒞`, at
  `|V| = 2`, `|A| ≥ 2`, for lifts whose visible family lies in `PPer`.
- **It would not establish:**
  - physical availability of any procedure: P-conf, Acc₂, Rd, H-comp, Rst-ch, Rst-sel and the T-sep preparation
    remain SOURCING-GAPs (B4 ll. 562–572; #1143 spec §4.4 S-0–S-8);
  - native OI realizability of `U` or `U′`: `PPer` membership is not nativeness. No native class of BSEL-2 dilation
    lifts and no native-realization→lift correspondence (spec S-0) is defined on `main`; the inclusion
    `L_native ⊆ L_PPer` is an unverified inference under a hypothesis (spec F3);
  - any physical OI–QM difference, gauge equivalence or inequivalence; a T-V-DISTINCT report is a statement about the
    stated mathematical procedures only;
  - anything about C-pers (M-2) or about T-full;
  - a theorem promotion, a Lean statement or a manuscript claim.
- **Conditional reading.** Read about OI lifts, every statement is CONDITIONAL[the candidate tuple, ∀U, fixed `a₀`,
  (r1)], with (r2) for C2-sel (B4 ll. 548–559).

## §8. Invariants and their checkpoints (§A.41)

| Invariant asserted | Checkpoint |
|---|---|
| Pair, definitions, controls and rule frozen before checking | This commit is pushed before the RESULT commit; `git diff <this commit> <result commit> --stat` lists `RESULT.md` only |
| No script, CAS, numerical evaluation or search | RESULT states the method; every value shown as a written hand computation; reviewer checks |
| Exact arithmetic | Every entry in RESULT is an integer, a multiple of `½`, `¼` or `1/√2`, or a Gaussian rational |
| Complete-record laws with `⊥` masses | K-e, each record type enumerated, bookkeeping sums |
| `PPer` from the kernel definition, both orientations | K-b |
| Law computation can detect a difference | K-f |
| T-V separation re-derived, gauge-safe and sensitive | K-g (g1)–(g3) |
| No off-`main` or unverified premise | K-h; the §A.42 item 8 trace in RESULT |
| Decision rule applied as written | RESULT's verdict section quotes §6 and evaluates each condition |
| No substitute pair | RESULT examines only the pair of §2 and the control lifts fixed there |
| Independent review | Pending; recorded on the guiding pull request; merge not authorized |

**Drafting disclosure.** The slice data of `W` and `W′` (`Γ`, `α`, fibre-Gram data, `g`) are on `main` in RES §2 and
were read before this file was written; they are re-derived in RESULT, not cited. Every entry of `W` and `W′` is `±½`,
which is visible from §2. While fixing what must be computed, the writer formed an expectation about the
moduli-only factors; no law, relative object or target-QM mass of the alternating lifts was written out before this
commit. The rule of §6 is stated without reference to any expected value.

## §9. Off-`main` references (provenance; traced in RESULT)

- #1031 c.6665461411 and #1143 c.6665466217: the authorization (owner designation, quoted with author and time,
  §A.42 item 7).
- #1143 c.6665278924 (the reviewed specification: F4, §1.4 T-V / T-V+R, §4.2 M-1, §4.6 controls) and c.6665288579 (its
  review record): source of the candidate and of the T-V definition, restated in full in §1 and §3.
- Reviews of B4 and RES recorded in #1033 and #1139 comments: not used as support.
