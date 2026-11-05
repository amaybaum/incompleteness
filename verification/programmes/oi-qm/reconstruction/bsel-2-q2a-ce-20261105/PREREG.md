# BSEL-2 Q2A: verification of the candidate counterexample pair (preregistration)

**Status: WIP / UNVERIFIED. Preregistration, frozen at the commit that adds this file.** Paper-only. Writer:
`writer-bsel2-ce`, the sole writer of this unit. Independent review is pending.
**Base:** `origin/main` `a8ab8dae3e9af7376c9233f4d474d7ccec1ecdb2`. Every line number below is read at this base.
**Method:** reading and hand algebra in exact arithmetic only. No script, CAS, numerical evaluation or search over the
matrices. No Lean work.
**Order of work:** this file is committed and pushed before any control or invariant is evaluated. The results go in
`RESULT.md` in this directory, in a later commit that changes no other file. The pair in §2 is not changed after this
commit. If a control fails, the verdict is VOID (§5).

## §0. Authorization

Owner ruling, #1033 comment 6662765230 (amaybaum, Claude Code session chat, 2026-11-05, shortly before 16:03Z), quoted
verbatim from that comment:

> Release the F §6, line 430 boundary for this specific candidate-counterexample verification only.
>
> The assessment identifies a concrete, testable mathematical claim rather than another open-ended proof search. It is worth checking, even if the result is unfavorable to OI's proposed equivalence.
>
> Authorize one paper-only verification unit with:
> * The two proposed 4×4 unitaries frozen before checking.
> * The five preregistered controls K-a through K-e, including unitarity, equality of the operational data, the positive gauge control, the ancilla countercontrol and an independent derivation of the relevant lemma.
> * Explicit verification of the applicable complete-record laws, including branch masses and failures, rather than relying on a weaker observable.
> * Independent mathematical review and a fixed decision rule.
>
> If every control passes and the Gram invariant differs, record a scoped COUNTEREXAMPLE for the applicable C2-ch, C2-sel and C0 claims at the stated dimensions and within the all-unitary class.
>
> If a required control fails, record VOID and preserve the unresolved status.
>
> Keep the distinction between arbitrary unitary families, `PPer`, native OI-realizable lifts and physically sourced access. No conclusion about the latter classes follows automatically.
>
> This authorization does not permit computational searches, changes to #1125, theorem promotion or manuscript edits. Bring any proposed change to the B4′ matrix back for approval.

The same comment records that the release covers only the candidate pair of the assessment (#1033 c.6662297536).

**Not authorized here:** any other pair; any search; changes to #1125 or its branch; theorem promotion; manuscript
edits; a change to the B4′ matrix (a change is proposed in `RESULT.md` only); merge.

## §1. Definitions used, with their sources on `main`

Abbreviations: TSG `verification/lean-mathlib/OIBridge/TwoSidedGauge.lean`; CLG `CoherentLiftGauge.lean`; DC
`DilationChoice.lean`; CF `CancellationFork.lean`; RC `RootedClassification.lean` (same directory). B4 is
`verification/programmes/oi-qm/reconstruction/bsel-2-b4prime-20261105/B4PRIME.md` and SC is `SCOPE.md` in that
directory.

- **Carrier.** `V = {0,1}`, `A ⊇ {a₀,a₁}`, carrier `V × A`, fixed anchor `a₀`; `e_v := e_{(v,a₀)}`, `𝒜 := span{e_v}`,
  `C := 𝒜^⊥`, fibre projector `P_w := |w⟩⟨w| ⊗ 1_A` (B4 ll. 32–33).
- **Lifts.** `U = (U_t)_{t∈ℕ}`, each `U_t` unitary; ∀U ranges over all such families (B4 l. 34; SC ll. 109–111).
- **Left fibre group.** `LeftFibreGroup L`: `L` unitary and `L p q = 0` whenever `p.1 ≠ q.1` (TSG:78–79).
- **Weak anchor stabilizer.** `WeakAnchorStabilizer a₀ K`: `K` unitary and `K p (j,a₀) = c_j` if `p = (j,a₀)`, else 0
  (CLG:114–116); `|c_j| = 1` (`weak_anchor_coeff_norm_one`, CLG:146).
- **Two-sided relatedness `G`.** `TwoSidedRelated a₀ U U′`: there are `L_t`, `K_t` with `LeftFibreGroup (L_t)`,
  `WeakAnchorStabilizer a₀ (K_t)` and `U′_t = L_t U_t K_t` for every `t` (TSG:84–87).
- **Fibre-Gram data.** `FG^{(i)}(U)(j,k) := FibreGram a₀ U i j k = Σ_a conj(U((i,a),(j,a₀))) · U((i,a),(k,a₀))`
  (TSG:95–97; `fibreGram_apply` TSG:115–116). Diagonal: `fibreGram_diag` (TSG:127–128). Sum over fibres is `1` for unitary
  `U` (`sum_fibreGram`, TSG:153–154). Left invariance: `fibreGram_left_mul` (TSG:207–208).
- **Phase equivalence.** `GramPhaseEquiv G G′`: some `c : V → ℂ` with `|c_j| = 1` and `G′ i j k = conj(c_j) G i j k c_k`
  for all `i, j, k` (TSG:102–103).
- **Kernel theorems used.** `gramPhaseEquiv_of_twoSided` (TSG:263–265, forward); `twoSided_slice_iff` (TSG:826–830,
  both directions); `twoSidedRelated_iff` (TSG:839–843; `mp` and `mpr` named where used).
- **Readback `Γ`.** `Γ_t(w,v) := Σ_a |U_t((w,a),(v,a₀))|² = ‖P_w U_t e_v‖²` (B4 l. 39; DC:86–87, DC:134–136). Rows `w`,
  columns `v`.
- **Anchored moduli.** `α_t(w,j) := |⟨e_w, U_t e_j⟩|²`; `β_{t,s}(w,v) := |⟨e_w, T_{t,s} e_v⟩|²` (B4 l. 43).
- **Relative object and readback.** `T_{t,s} := U_t U_sᴴ`; `𝒪₂(t,s)(w,v) := ‖P_w T_{t,s} e_v‖²` (B4 ll. 40–42; CF:123–129).
- **Gram invariant.** `g(W) := FG^{(0)}(W)(0,1) = Σ_a conj(W((0,a),(0,a₀))) · W((0,a),(1,a₀)) = ⟨P_0We_0, P_0We_1⟩`,
  inner product conjugate-linear in its first argument.
- **Procedures** (SC ll. 112–119, frozen): H-comp (root to first read at `s` by `U_s`; between reads at `s < t` by
  `T_{t,s}`); Acc₂ (any finite increasing read list `t₁ < … < t_k`, `k ≥ 1`, all records kept jointly); P-conf (root
  `|j,a₀⟩`, each `j` separately); Rd (Lüders read by `P_v`, record `v`); Rst-ch (the ancilla is replaced by `|a₀⟩`);
  Rst-sel (an `|a₀⟩⟨a₀|` test after the read; `⊥` kept with its mass and not continued). Readings (r1) (B4 ll. 57–59)
  and (r2), the test follows every read including the last (B4 ll. 60–62).
- **Candidates.** C0 = (P-conf, Acc₁, Rd); C2-ch = (P-conf, Acc₂, Rd, H-comp, Rst-ch); C2-sel = (P-conf, Acc₂, Rd,
  H-comp, Rst-sel) (SC ll. 120–124).
- **Complete-record laws `Λ_C`.** "every branch mass and every failure record `⊥`, unnormalized and unconditioned"
  (SC ll. 24–25). Their general forms on `main` are B4 W0.1 (ll. 70–74), W0.4 (ll. 94–111) and W0.5 (ll. 113–125).
  `O_C(U,U′)` is `Λ_C(U) = Λ_C(U′)` (SC ll. 24–25).
- **The target statement.** `Q[C]`: `∀U,U′: O_C(U,U′) ⇒ G(U,U′)` (SC l. 129; B4 l. 221), restricted to `|V| = 2`,
  `|A| ≥ 2`, for C ∈ {C0, C2-ch, C2-sel}. These are the cells B4 rows 514, 519 and 521 record as "not addressed".
- **Class `PPer`.** `Γ 0 = 1`, row-stochastic at every `t`, and periodic (RC:32–33).

**Status of B4 on `main`.** B4's header (l. 3) reads "WIP / UNVERIFIED (complete draft, not reviewed)"; its reviews are
recorded only in #1033 comments, which are provenance (B4 l. 20). This record therefore takes from B4 and SC only
definitions (the procedures, readings and candidate tuples) and notation. It does not take W0's product formulas as
premises: K-b computes every branch mass of the pair from the procedures, by explicit unnormalized branch states, and
compares the result with W0's formulas as a cross-check only.

**The assessment's reading** (#1033 c.6662297536): `Γ`, `α`, `g` and `TwoSidedRelated` as above. K-e checks each
definition used against its source line. A definition that reads differently from the assessment's reading makes the
verdict VOID (§5).

## §2. The frozen pair

**Basis order** (as in the assessment): `p₀ = (0,a₀)`, `p₁ = (0,a₁)`, `p₂ = (1,a₀)`, `p₃ = (1,a₁)`. Matrices are written
with rows and columns in this order.

**Reading of `e₀` and `e₁`.** The assessment writes `We₀`, `We₁`. Under B4's notation (`e_v := e_{(v,a₀)}`, B4 l. 32),
`e₀ = e_{p₀}` and `e₁ = e_{p₂}`. This reading is fixed here.

**What the assessment leaves open, fixed here.** The assessment fixes the anchored columns `We₀ = W′e₀ = (1,1,1,1)/2`,
`We₁ = (1,1,−1,−1)/2` and `W′e₁ = (1,−1,1,−1)/2`, and says both are column permutations of Sylvester's `H₄/2`. It does
not fix the columns at `p₁` and `p₃`. They are fixed here as follows.

Sylvester's `H₄ = H ⊗ H` with `H = [[1,1],[1,−1]]` has columns `h₀ = (1,1,1,1)`, `h₁ = (1,−1,1,−1)`,
`h₂ = (1,1,−1,−1)`, `h₃ = (1,−1,−1,1)`.

- **`W := H₄/2`** (the identity column permutation): columns `(h₀, h₁, h₂, h₃)/2` at `(p₀, p₁, p₂, p₃)`.

  ```
  W = ½ ·  [ 1   1   1   1 ]     row p₀ = (0,a₀)
           [ 1  −1   1  −1 ]     row p₁ = (0,a₁)
           [ 1   1  −1  −1 ]     row p₂ = (1,a₀)
           [ 1  −1  −1   1 ]     row p₃ = (1,a₁)
  ```

- **`W′`** := `H₄/2` with its columns at `p₁` and `p₂` exchanged: columns `(h₀, h₂, h₁, h₃)/2` at `(p₀, p₁, p₂, p₃)`.

  ```
  W′ = ½ · [ 1   1   1   1 ]     row p₀ = (0,a₀)
           [ 1   1  −1  −1 ]     row p₁ = (0,a₁)
           [ 1  −1   1  −1 ]     row p₂ = (1,a₀)
           [ 1  −1  −1   1 ]     row p₃ = (1,a₁)
  ```

  Entrywise: `W(p_r, p_c) = ½·H₄(r, c)`; `W′(p_r, p_c) = ½·H₄(r, σ(c))` with `σ = (0)(1 2)(3)`.

- **The lifts.** Constant: `U_t := W` and `U′_t := W′` for every `t ∈ ℕ`. `|V| = 2`, `|A| = 2`, anchor `a₀`.
- **Extension to `|A| = m ≥ 3`.** `A = {a₀, a₁, …, a_{m−1}}`; `W ⊕ 1` and `W′ ⊕ 1`, the identity on the `2(m−2)` basis
  vectors `(v,a)`, `a ∉ {a₀,a₁}`; the same constant placement. K-b and the invariant are checked for the extension as
  well.
- **The K-c control element.** `L := 1_V ⊗ H₂` with `H₂ = (1/√2)[[1,1],[1,−1]]` on `{a₀,a₁}` (WE's `L`, B4 l. 324):

  ```
  L = (1/√2) · [ 1   1   0   0 ]
               [ 1  −1   0   0 ]
               [ 0   0   1   1 ]
               [ 0   0   1  −1 ]
  ```

  and `K := diag(1, −1, i, 1)` in the basis order `(p₀, p₁, p₂, p₃)`. The control lift is the constant lift
  `U^c_t := L W K`.

## §3. Controls and their pass criteria

All arithmetic is exact (integers, `½`, `1/√2`, `i`). Each control is written out in full in `RESULT.md`.

- **K-a (unitarity).** Pass iff `WᴴW = 1` and `W′ᴴW′ = 1`, all 16 entries each computed; and `L`, `K` unitary, with
  `LᴴL = 1` and `KᴴK = 1` computed.
- **K-b (equality of the complete-record laws).** Pass iff all of the following hold, each computed from the procedures
  of §1 by explicit unnormalized branch states for both lifts:
  - **C0:** for each root `j ∈ V` and each `t`, every record mass `‖P_v U_t e_j‖²` agrees.
  - **C2-ch:** for each root `j`, every finite read list `t₁ < … < t_k` (`k ≥ 1`) and every record `(v₁, …, v_k)`, the
    branch mass agrees.
  - **C2-sel:** for each root `j`, every finite read list and every record — every all-ok sequence
    `((v₁,ok), …, (v_k,ok))` and every sequence ending in one `(v_m,⊥)`, `1 ≤ m ≤ k` — the unnormalized mass agrees.
    The `⊥` masses are compared, not only the ok masses.
  - **Bookkeeping:** for each lift and root, the masses over all records of a read list sum to 1.
  - **Derived data:** `Γ(W) = Γ(W′)` and `α(W) = α(W′)` entrywise, and the computed masses match W0.1, W0.4 and W0.5
    (cross-check).
  - **Coverage:** all `t ∈ ℕ` and all `k`, by an argument valid for every read list (the lifts are constant), and the
    extension to `|A| ≥ 3`.
- **K-c (positive gauge control).** Pass iff all hold:
  - `L` satisfies `LeftFibreGroup` (TSG:78–79) and `K` satisfies `WeakAnchorStabilizer a₀` (CLG:114–116), with its
    coefficients `c = (c₀, c₁)` stated;
  - `W` and `LWK` are two-sided related by construction (TSG:84–87, constant `L`, `K`);
  - the fibre-Gram data of `LWK`, computed entrywise from the matrix `LWK` in both fibres, satisfy
    `FG^{(i)}(LWK)(j,k) = conj(c_j) FG^{(i)}(W)(j,k) c_k` for all `i, j, k`;
  - hence `Γ(LWK) = Γ(W)` and `|g(LWK)| = |g(W)|`.

  Purpose: on a pair related by construction, the hand Gram computation reports no difference.
- **K-d (ancilla countercontrol).** Pass iff both hold:
  - (i) **the pair uses `|A| = 2`:** for at least one of `W`, `W′`, the vectors `P₀We₀` and `P₀We₁` are not collinear,
    equivalently `|g|² ≠ Γ(0,0)·Γ(0,1)` for that member;
  - (ii) **the `|A| = 1` statement, re-derived:** at `|V| = 2`, `|A| = 1`, every unitary has `|g|² = Γ(0,0)Γ(0,1)`, so
    equal `Γ` forces equal `|g|` and the pair can contradict nothing proved at `|A| = 1` (B4 §3.1, ll. 240–246).

  The assessment's K-d wording ("`P₀We₀` and `P₀We₁` are not collinear") does not say for which member. Criterion (i)
  is fixed as "at least one member" because that is exactly what (ii) requires: two unitaries with equal `Γ` and
  unequal `|g|` cannot both satisfy `|g|² = Γ(0,0)Γ(0,1)`.
- **K-e (independent re-derivation).** Pass iff `RESULT.md` derives the following from `main`'s kernel lines and the
  definitions of §1 only, with every step cited, and every definition used matches its source line and the
  assessment's reading:
  - **Lemma R** (relatedness at `|V| = 2`), each direction separately (§A.34): for unitary slices `W, W′`,
    (a) `∃ L ∈ 𝒢_L, K weak: W′ = LWK` ⇒ (b) `Γ(W) = Γ(W′)` and `|g(W)| = |g(W′)|`; and (b) ⇒ (a). For lifts, `G(U,U′)`
    ⇒ the slice relation at every `t` (TSG:839 `mp`).
  - **Lemma C** (constant lifts): `G` on constant lifts holds exactly when the slices are related; `Λ_C0` is `Γ`;
    `Λ_C2-ch` is a function of `Γ` and determines it; `Λ_C2-sel` is a function of `(Γ, α)` and determines it.

  The lemmas of `Q2A.md` (off `main`, #1125 branch at `f3ef3d3d`) are not used. That file is provenance only.
- **Gram invariant.** `g(W)` and `g(W′)` computed exactly from the matrices of §2.

## §4. Logical use of the controls

If K-a, K-b and K-e pass and `|g(W)| ≠ |g(W′)|`:
- K-b gives `O_C(U,U′)` for C ∈ {C0, C2-ch, C2-sel}.
- Suppose `G(U,U′)`. TSG:839 (`mp`) gives `GramPhaseEquiv` at `t = 0`, and Lemma R (a ⇒ b) gives
  `|g(W)| = |g(W′)|`, a contradiction. So `¬G(U,U′)`.
- Hence `Q[C]` fails at `|V| = 2`, `|A| = 2` for each of the three candidates; the extension gives `|A| ≥ 3`.

K-c and K-d test the method and the scope: K-c that the Gram computation does not produce a spurious difference, K-d
that the pair does not conflict with the `|A| = 1` result.

**Class.** Constant lifts have `Γ_0 = Γ(W)`. If `Γ(W) ≠ 1`, the pair lies outside `PPer` in either orientation
(`Γ 0 = 1` is orientation-free; RC:32). RESULT states `Γ(W)` and the class.

## §5. Decision rule (fixed)

- **COUNTEREXAMPLE** iff K-a, K-b, K-c, K-d and K-e all pass and `|g(W)| ≠ |g(W′)|`. The verdict text is then:
  COUNTEREXAMPLE[C0, C2-ch, C2-sel; `|V| = 2`, `|A| ≥ 2`; constant lifts; equal complete-record laws (same `Γ`, and
  same `α`); all-unitary class; outside `PPer`]. Scope as in §6.
- **VOID** otherwise: any control fails, or is vacuous; a definition reads differently from the assessment's reading;
  or `|g(W)| = |g(W′)|`. On VOID the cells B4 rows 514, 519 and 521 stay "not addressed", and the recommendation
  reverts to the assessment's option G (park with a named gap).
- No other verdict is available. The pair of §2 is not adjusted after this commit, whatever the outcome.
- Either verdict is reported to the owner. Any change to the B4′ matrix is proposed in `RESULT.md` and not applied.

## §6. Scope

- **What a COUNTEREXAMPLE would establish:** that `Q[C0]`, `Q[C2-ch]` and `Q[C2-sel]` (O⇒G) are false at `|V| = 2`,
  `|A| ≥ 2` over the class of all unitary families (∀U), witnessed by constant lifts outside `PPer`.
- **What it would not establish** (kept distinct, per the ruling):
  - anything about the `PPer` subclass, whose O⇒G cells at `|V| = 2`, `|A| ≥ 2` would stay "not addressed";
  - anything about native OI-realizable lifts or restricted lift classes;
  - anything about physically sourced access (P-conf, Acc₂, Rd, H-comp, Rst-ch, Rst-sel remain SOURCING-GAPs, B4
    ll. 556–565);
  - any physical gauge or operational equivalence or inequivalence.
- **Conditional reading.** Every statement is about the stated mathematical objects. Read about OI lifts it is
  CONDITIONAL[the candidate tuple, ∀U, fixed `a₀`, (r1)], with (r2) for C2-sel (B4 ll. 547–553).
- **Not a theorem promotion.** No manuscript edit; no Lean work; the kernel formalization of the pair, if wanted, needs
  separate authorization.

## §7. Invariants and their checkpoints (§A.41)

| Invariant asserted | Checkpoint |
|---|---|
| The pair, controls and rule are frozen before any check | This file's commit is pushed before the RESULT commit; `git diff <this commit> <result commit> --stat` lists `RESULT.md` only |
| No script, CAS or search over the matrices | RESULT states the method; every value is shown as a written hand computation; reviewer checks |
| Exact arithmetic | Every entry in RESULT is an integer, a multiple of `½`, `¼` or `1/√2`, or a Gaussian rational |
| Complete-record laws, `⊥` masses included | K-b, with each record type enumerated |
| No reliance on off-`main` lemmas | K-e; the §A.42 item 8 trace in RESULT |
| Decision rule applied as written | RESULT's verdict section quotes §5 and evaluates each condition |
| Independent review | Pending; recorded on the guiding pull request; merge not authorized |

## §8. Off-`main` references (provenance; traced in RESULT)

- F: `BSEL2-B3-B5.md` at `88c175c3` (branch `research/bsel2-b3-b5-20261104`), l. 430 ("DC's strictness at `|V| = 2`,
  `|A| ≥ 2`"), named by the ruling; ll. 254–261 (the `|A| = 1` case, re-derived on `main` in B4 §3.1).
- `Q2A.md` at `f3ef3d3d` (#1125 branch `research/bsel2-q2a-oeg-20261105`).
- #1033 comments 6662765230 (the ruling) and 6662297536 (the assessment).
