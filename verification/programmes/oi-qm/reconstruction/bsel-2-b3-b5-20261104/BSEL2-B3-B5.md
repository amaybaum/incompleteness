# BSEL-2: the one-time (⇒) gap, B3 and B5 (paper units)

**Status: WIP / UNVERIFIED.** Paper-only. Not independently reviewed.
**Authorization:** owner, 2026-11-04, #1033 c.6622106693. Its scope is the one-time (⇒) gap and units B3 and B5,
under the paper-only authorization #914 c.6567372732 (H.2). B6 is out of scope (blocked on O-REC, O-SET).
**Base:** `origin/main` `1609dc440f5a12d05b750f6d894bb91d09a099a3`; Lean read with `git show` only.
**Method:** reading and hand algebra. No code, script, enumeration, Lean build or probe. No repository or GitHub write.

**What this is.** Paper derivations that decide, or bound, three questions, with every step labelled.
**What this is not.** It is not a native operational claim, not a statement about which preparations, devices or reads
OI physically supplies, and not a gauge classification. It promotes nothing, changes no record, and adopts no reading;
§5 lists proposals only.

**Support labels.** [K] kernel-checked at the base (identifier, file:line under `verification/lean-mathlib/OIBridge/`);
[P] reviewed paper result (cited); [D] derived here, unreviewed; [L] literature or standard fact from memory, not
re-read; [O] owner decision.

**Sources read.** `AGENTS.md`; #1033 body and all six comments (c.6567681563 status; c.6567694252/6567701387 B1(c)
note and review; c.6567713723/6567723333 B4′ note and review; c.6622106693 start); #914 c.6558834119 (BSEL-1),
c.6563412926 (master matrix rev 2, "MM"), c.6567372732 (H.2); #866 comments; #1074; `TwoSidedGauge.lean` (TSG),
`CoherentLiftGauge.lean` (CLG), `DilationChoice.lean`, `RootedClassification.lean`, `RootedClassificationAllTime.lean`;
`papers/Main.md` :95–99, :205–216.
**Off-repo working records** (provenance only, §A.42; found in this session's scratchpad, not written by this writer):
- PL-BSEL2 rev 1, `resume/BSEL2-PLAN.md`, sha256 `f0e8ce7e…85192`. Authenticated only by agreement with the
  verbatim quotation of its ll. 48–58, 69 and 176 in the B1(c) note (#1033 c.6567694252). Its review RV-BSEL2 is
  `resume/BSEL2-REVIEW.md` (`56d284e3…70c26`).
- Thread E, `p0five/E/THREAD-E.md` (`00d6bfa0…40ddb`), with reviews `REVIEW.md` (`f624e42b…e93e0`) and
  `REVIEW-r2.md` (`546ca50e…e1787`).

The definitions of B3 and B5 exist only in PL-BSEL2. No public source states them (searched: #1033, #914, #866, #1074;
`git grep` over all remote branches for `BSEL`, `Γ_W`, `Thread E`, `H-fac`). The label "B5" in #914 c.6567870091
(BORN-SRC-1) is an unrelated row.

**Disclosure.** Not blind. The reviewer's lead (B1(c) note §4; review F7) was known before §2 was written, and the
routes of §3.1 and §3.2 were sketched while reading.

***

## §1. The exact questions

### 1.0 Objects (common)
- `V`, `A` finite; anchor `a₀`; `N = |V||A|`; `e_v := e_{(v,a₀)}`; anchored span `𝒜 = span{e_v}`; `C = 𝒜^⊥`, with
  projector `P_C`; `P_w = |w⟩⟨w| ⊗ 1_A`.
- `𝒢_L` = `LeftFibreGroup` [K TSG:78]: unitaries block-diagonal across fibres, `≅ Π_w U(ℂ^A)` [K `left_block_unitary`
  TSG:188]. `𝒲` = `WeakAnchorStabilizer a₀` [K CLG:114]: unitaries with `Ke_v = c_ve_v`.
- Readback (visible slice) `Γ(U)_{wv} = Σ_a |U_{(w,a),(v,a₀)}|² = ‖P_wUe_v‖²` [K `AdmissibleDilationAt`, DilationChoice:134].
- **Interface** (frozen, PL-BSEL2 ll. 48–58 as quoted in #1033 c.6567694252; "proposed, not adopted"): `I = (π, G, ψ, 𝒫)`.
  Under H-fac its law is `p_c(U) = tr(A_c UρU†)` with `A_c = X†P_cX` and `X = G(1⊗|ψ⟩)`. Here `ρ` is `π`'s density
  operator; mixtures enter by convex-linear extension (B1(c) review F3). The effects `A_c` are `U`-independent,
  `0 ≤ A_c`, and `Σ_c A_c = 1`.
- **GR(I)**, "respects the gauge" (frozen): `∀U ∈ U(N)`, `∀L ∈ 𝒢_L`, `∀K ∈ 𝒲`, `∀c`: `p_c(LUK) = p_c(U)`.
- **NI** (frozen): `⟨P_cG(|v⟩⊗ψ), P_cG(|v′⟩⊗ψ)⟩ = 0` for `v ≠ v′`. At `|A| = 1` this says exactly that every `A_c` is diagonal.

### 1.1 The one-time (⇒) gap
Sources, verbatim:
- PL-BSEL2 ll. 70–73: "**The one-time equivalence.** (⇐) fibre-identifying (equivalently SH-respecting) ⇒
  OI-gauge-respecting: **VERIFIED**, trivially, since at `|A| = 1` two-sided orbits lie inside visible fibres (BSEL-1
  §5). (⇒) OI-gauge-respecting ⇒ fibre-identifying: **GAP** […] The clause "⇔ configuration preparation ∧ NI" holds
  (⇐) via (a) and is **refuted** (⇒) by blind reads and RHC5. It is withdrawn."
- MM §4c: "**One-time equivalence**: (⇐) VERIFIED, trivially; (⇒) GAP."
- B1(c) note §4: "(ii) "fibre-identifying" must be fixed: which `U, U′` with `|U|² = |U′|²`, at which `π`."

Not pinned by the sources: the meaning of "fibre-identifying", and the `|A|` scope. PL-BSEL2 l. 60 heads B1 "at
`|A| = 1`, one time".

**Readings of "fibre-identifying" (fixed here).**
- **FI (operative):** `∀U, U′ ∈ U(N)`: `Γ(U) = Γ(U′) ⇒ p_c(U) = p_c(U′)` for every `c`, at the interface's own `π`.
- **FI_c:** the same with entrywise `|U|² = |U′|²` on `V × A` in place of `Γ(U) = Γ(U′)`.

At `|A| = 1` the two coincide, since `Γ(U) = |U|²`. FI is operative because the sources' gloss is "visible fibres"
(BSEL-1: "SH orbits are exactly the visible fibres"), and because §3.1 shows that the recorded (⇐) verdict holds
under FI at every `|A|` but under FI_c only at `|A| = 1`.

**Questions.**
- **Q1⇒:** for every interface `I` under H-fac at one time, GR(I) ⇒ FI(I).
- **Q1⇐:** FI(I) ⇒ GR(I).
- **Q1c (my addition):** an exact characterization of GR, to stand in place of the withdrawn clause. It is posed as
  two directions.
- **Scope:** any finite `V`, `A`; `|A| = 1` is reported separately.

### 1.2 B3
Sources, verbatim:
- #1033: "Decide whether the reviewed Thread E / Γ_W candidate and B5 belong in a separate mathematical lane. A
  candidate torus formula or one finite witness is not a general theorem."
- PL-BSEL2 l. 106 ff.: "**B3. Thread E's decisive question, reduced** […] the condition holds iff `Re c_r = Im c_r`
  for every row. […] **Still open:** the torus form (right phases free, so feasibility on some dephased lift reduces
  to collinearity of `c_0, c_1, c_2` through `0`; [P], unproved), feasibility for any non-monomial `Γ_W`, and the
  winding argument on 3+1 blocks (`J₃/3 ⊕ 1`, four placements)."
- Thread E §5 asks the question itself: "Is there a 4×4 unistochastic `Γ_W` […] with no lift `W'` satisfying
  `|W'H(1)|² = |W'H(i)|²`?"
- MM D-36: "B3: pursue as pure mathematics or park (choose)". D-37: "B3's exact certification, after D-33 reports".

**Precise form.**
- `H(z) = ½[[1,1,1,1],[1,z,−1,−z],[1,−1,1,−1],[1,−z,−1,z]]`.
- A *lift* of a 4×4 unistochastic `Γ_W` is a unitary `W` with `|W|² = Γ_W` entrywise. The orientation is my reading.
  The question quantifies over all unistochastic `Γ_W`, a set closed under transposition, so its answer does not
  depend on the orientation.
- `Feas(Γ_W)`: some lift `W` has `|WH(1)|² = |WH(i)|²` entrywise.
- **Q3:** is `Feas(Γ_W)` true for every 4×4 unistochastic `Γ_W`? Thread E's "Yes" is the negation.
- **Sub-questions:**
  - Q3a: the torus/collinearity reduction, both directions;
  - Q3b: 3+1 blocks;
  - Q3c: general `Γ_W`;
  - Q3-lane: the lane question.

### 1.3 B5
Source, verbatim. PL-BSEL2 l. 125: "**B5. `PPer` transfer** (kernel). TG3 on `1, J/4, 1, J/4, …` is in `PPer`; lift
theorems, B1 and B4′ need re-proof; GL2 needs a re-placed gauge time (Thread E §3.3)." MM D-38: "B5's lane: Track B or
K∞ (choose)". D-39: "B5's Lean work (yes/no)". MM R2-3: the `PPer` membership is [P].

**Precise form.** Let `Γ^alt_t = 1` for even `t` and `J/4` for odd `t`. Let `U^alt_t = 1` (even), `H(1)` (odd), and
`U′^alt_t = 1` (even), `H(i)` (odd).
- **Q5a:** `PPer Γ^alt` [`PPer`, RootedClassification:32].
- **Q5b:** `U^alt` and `U′^alt` are coherent lifts of `Γ^alt` that are not `TwoSidedRelated`, and their relative
  objects differ.
- **Q5c:** do B1/Q1 and B4′'s verdicts transfer to `Γ^alt`?
- **Q5d:** GL2's re-placed version.
- **Q5-lane:** the lane question. The kernel (Lean) part is out of scope.

## §2. Decision criteria (stated before §3)

- **PROVED (MATHEMATICAL):**
  - a complete paper proof under the stated quantifiers;
  - each step is [K], [P] or elementary algebra;
  - the controls below behave as required.
- **REFUTED / COUNTEREXAMPLE[scope]:** an explicit instance meeting the hypothesis and failing the conclusion,
  checked by hand in exact arithmetic.
- **CONDITIONAL[…]:** proved only with a named extra hypothesis.
- **OPEN:** neither of the above; the unproved step is named.
- **VOID:** a control fails, or a reading cannot be fixed.
- **Lane questions:** an owner choice [O]. They are not decided here. §5 states the facts that bear on them.
- **Equivalences:** each direction is a separate question (§A.34).

**Controls for Q1.** Each was fixed before §3 was written:
- **K1:** at `|A| = 1`, B1(c)'s S must be recovered as a special case.
- **K2:** C0's interface (configuration preparation, configuration read) must satisfy GR.
- **K3:** B4′'s C1 counterexample must fail GR.
- **K4:** the RHC5 interface must fail GR under ∀U.
- **K5:** non-vacuity. A same-`Γ` pair that is not two-sided related must exist, so that FI is strictly stronger than
  orbit invariance.
- **K6:** at `|A| = 2`, a positive instance must pass and a perturbed instance must fail.
- **K7:** B1(c)'s R2 countermodel must be classified as GR.

**Controls for Q3.** Thread E's controls must come out feasible: monomial `Γ_W`, `J/4`, and 2+2 blocks. A fixed
`W = H(1)` must separate the pair before right phases are applied.

## §3. Work

### 3.1 Q1⇐ (FI ⇒ GR)
`Γ(LUK) = Γ(U)` for every `L ∈ 𝒢_L` and `K ∈ 𝒲`.

[K]: `left_preserves_admissible` (TSG:217) and `weak_preserves_admissible` (CLG:273). Each sends an admissible
dilation of `Γ` to an admissible dilation of the same `Γ`. Hence FI ⇒ GR. **PROVED** at every `|A|` [D from K].

Under FI_c, (⇐) fails at `|A| ≥ 2`. **CE-3** [D]:
- the setting: `V = {0,1}`, `A = {a₀,a₁}`, `π = e_{(0,a₁)}`, `G = 1`, cells `{P_{(0,a₁)}, 1 − P_{(0,a₁)}}`;
- the law `p(U) = |U_{(0,a₁),(0,a₁)}|²` is a function of `|U|²`;
- `K` swaps `e_{(0,a₁)} ↔ e_{(1,a₁)}` and lies in `𝒲`;
- `p(1) = 1` and `p(K) = 0`.

### 3.2 Q1⇒ (GR ⇒ FI), any `|A|`
**Lemma HS** [P: B1(c) note §2 Step 2, review-confirmed]. If `B` is Hermitian and non-scalar, `Δ` is Hermitian and
traceless, and `tr(U†BUΔ) = 0` for every unitary `U`, then `Δ = 0`.

**Lemma CM** [D; uses Schur's lemma for `U(n)` on `ℂⁿ`, L].
- (a) `𝒲′ = {Σ_v x_v e_ve_v† + μP_C}`. Proof: `K ∈ 𝒲` iff `K = D ⊕ W`, with `D` a diagonal unitary on `𝒜` and
  `W ∈ U(C)`. Commuting with `1_𝒜 ⊕ (−1_C)` makes `X` block-diagonal. Distinct anchored phases make the `𝒜` block
  diagonal, and `U(C)` makes the `C` block scalar. The converse is immediate.
- (b) `𝒢_L′ = {Σ_w α_wP_w}`, by the same argument with `−1` on one fibre.

**Proof of Q1⇒** [D]. Assume GR.
1. *(Right part.)* Put `L = 1`. Then `tr(U†A_cU·Δ_K) = 0` with `Δ_K = KρK† − ρ`, for all `U` and all `K ∈ 𝒲`. If every
   `A_c` is scalar, the law is constant and FI holds. Otherwise Lemma HS gives `Δ_K = 0` for all `K ∈ 𝒲`, so
   `ρ ∈ 𝒲′`, that is, `ρ = Σ_v r_ve_ve_v† + μP_C`. (At `|A| = 1`, `C = 0`; set `μ = 0`.)
2. Write `ρ = μ1 + Q`, with `Q = Σ_v (r_v − μ)e_ve_v†`. Then `p_c(U) = μ tr A_c + tr(A_cUQU†)`.
3. *(Left part.)* Put `K = 1` and `B = L†A_cL − A_c`, which is Hermitian and traceless. Put `Δ = Q − (tr Q/N)1`. Then
   `tr(U†BU·Δ) = 0` for all `U`.
   - If `Δ = 0`, then `Q` is scalar. At `|A| ≥ 2` this forces `Q = 0`, because `Q` vanishes on `C ≠ 0`. Either way
     `ρ = 1/N` and the law is constant.
   - Otherwise Lemma HS (contrapositive) makes `B` scalar, and since `tr B = 0`, `B = 0`. So `A_c ∈ 𝒢_L′` for every
     `c`: `A_c = Σ_w a_c(w)P_w`.
4. Then
   `p_c(U) = μ tr A_c + Σ_{v,w} (r_v − μ) a_c(w) ‖P_wUe_v‖² = μ tr A_c + Σ_{v,w} (r_v − μ) a_c(w) Γ(U)_{wv}`.
   This is a function of `Γ(U)`, so FI holds. ∎

Neither configuration-diagonality of the cells nor any property of `G` or `ψ` is used.

**Q1c, characterization** [D, both directions]. GR(I) holds iff at least one of the following does:
- **(D1)** every `A_c` is scalar;
- **(D2)** `ρ = 1/N`;
- **(D3)** `ρ ∈ 𝒲′` and every `A_c ∈ 𝒢_L′`.

(⇒) is steps 1–3. (⇐): each disjunct makes the law a function of `Γ(U)` (constant for D1 and D2; step 4 for D3), and
§3.1 applies.

**At `|A| = 1`.** Here `𝒲′` is the configuration-diagonal matrices and `𝒢_L′` the diagonal ones, so "`A_c ∈ 𝒢_L′` for
all `c`" is NI. Hence:

> GR ⇔ every cell is blind (B1(c)'s R1) ∨ `ρ = 1/|V|` ∨ (`ρ` is a mixture of configuration preparations ∧ NI).

The withdrawn clause "⇔ configuration preparation ∧ NI" lacks the first two disjuncts. **CE-1** [D]:
- `V = {0,1}`, `ρ = ½·1`, `G = H₂ ⊗ 1`, configuration cells, so `A_c = |±⟩⟨±|`;
- the law is `(½,½)` for every `U`, so GR holds;
- `⟨P_0Ge_0, P_0Ge_1⟩ = ½`, so NI fails, and the cells are not blind.

**Consequence for B1(c)'s S at `|A| ≥ 2`** [D]. Step 1 gives S′: right-respect ∀U implies `ρ ∈ 𝒲′` or every cell is
scalar. S itself, "`ρ` is a mixture of configuration preparations", fails for mixed `ρ`. **CE-2**:
- `V = {0,1}`, `A = {a₀,a₁}`, `ρ = ½e_{(0,a₀)}e_{(0,a₀)}† + ¼P_C`, `G = 1`, cells `P_0, P_1`;
- the law is `p_0 = ½ + ¼Γ_{00} − ¼Γ_{01}`, using `Σ_q ‖P_0Ue_q‖² = 2`;
- so GR holds (D3), with non-blind cells and `ρ` not a mixture of configuration preparations.

For pure `π` and `|V| ≥ 2`, `ρ ∈ 𝒲′` has rank 1, so `μ = 0` and `ρ = e_ve_v†`: S holds. `|A| = 1` is load-bearing
in B1(c) only for mixed preparations.

**Corollary DC (one-time candidates)** [D from K]. Let a one-time candidate `C` be a set of H-fac interfaces, with
lifts ranging over all unitary families (B4′'s convention). Then `R[C]` (every member is GR) gives `O_C ⊇ Fib`, where
`Fib` is equality of `Γ` slice by slice. Hence `R[C] ∧ Q[C]` would give `Fib ⊆ G`. That inclusion is false:
- **at `|A| = 1`, `|V| = 4`:** TG3 [K `hadamard_slices_not_twoSided` TSG:907].
- **at `|V| ≥ 3`, any `|A|`:** `F₃` against `F̄₃` (`F₃ = [ω^{jk}]/√3`), placed on the anchored lines with `1` on `C`
  and `⊕1` on further configurations.
  - Both have readback `J/3` (`⊕ 1` on further configurations).
  - The `∼_D`-invariant `G⁽⁰⁾₁₀G⁽¹⁾₀₁` is `ω/9` against `ω̄/9`, so the two are not `GramPhaseEquiv`
    [K `gramPhaseEquiv_cross_invariant` TSG:870] and not two-sided related [K `gramPhaseEquiv_of_twoSided` TSG:263].

So no one-time H-fac candidate both respects the gauge and refines `G`. B4′'s C0/C1/C1′ rows are instances. At
`|A| = 1` the quotient a GR one-time interface can see is `Fib`, which equals BSEL-1's SH orbits per slice [P #914
c.6558834119 §5].

**Controls** (all by hand, exact).

| Control | Requirement | Result |
|---|---|---|
| K1 | Recover S at `\|A\| = 1` | Step 1 is S with `𝒲′` = diagonal: **pass** |
| K2 | C0 interface (`ρ = e_j`, configuration cells) satisfies GR | It is D3: **pass** |
| K3 | B4′'s C1 counterexample fails GR | `ρ = \|+⟩⟨+\|` on `{0,1}` lies outside `𝒲′`, and the cells are not scalar, so CH predicts failure; B4′ HC-A gives `(½,½,0,0)` against `(0,0,½,½)` [P]: **fails as required** |
| K4 | The RHC5 interface fails GR under ∀U | Not in D1–D3; B1(c) HC-A at `U = R` gives `(1/50,49/50)` against `(49/50,1/50)` [P]: **fails as required** |
| K5 | Non-vacuity | The `F₃` pair and TG3 above: **pass** |
| K6 | Positive and perturbed instances at `\|A\| = 2` | CE-2 passes, also checked directly at `K = swap((0,a₁),(1,a₁))`, where both laws are `¾`. With `ρ′ = ½(e_{(0,a₀)}e† + e_{(0,a₁)}e†)` the same `K` gives `1` against `½`: **pass / fails as required** |
| K7 | B1(c)'s R2 countermodel is GR | `A_0 = A_1 = ½·1` is D1: **pass** |

**Skepticism (§A.31).** The result is strictly stronger than its obvious restatement: invariance on orbits yields
invariance on the strictly larger fibres (K5). It constrains one-time candidates (DC). Its content still comes from
two places:
- **the ∀U quantifier.** Lemma HS is applied at unitaries built from `A_c` and `ρ`.
- **the H-fac form.** The law is a fixed linear functional of `UρU†`.

It says nothing about a restricted class of `U`, such as one process's lift slices or OI-realizable lifts; that case
is OPEN. It says nothing about `U`-dependent devices, two times (B4′'s C2 fails GR), physical availability of any
ingredient, or an identification of OI's gauge with SH's. The last would be a bridge without a formal map.

### 3.3 B3
**Q3a, reduction (torus form)** [D, both directions]. Fix a lift `W` with columns `w_k`, and put
`a = ½(w₀ − w₂)`, `b = ½(w₁ − w₃)`. Then `W·col₁H(1) = a+b`, `W·col₁H(i) = a+ib`, `W·col₃H(1) = a−b`,
`W·col₃H(i) = a−ib`, and columns 0 and 2 of `H(1)` and `H(i)` agree.

For each row, `|a+b|² − |a+ib|² = 2(Re c − Im c)` with `c = a b̄`, and the column-3 condition is the same. This
reproduces PL-BSEL2/RHC7's `Re c_r = Im c_r` [P]. Also `Σ_r c_r = ⟨b,a⟩ = 0`. The following are equivalent:
- (i) `Feas(Γ_W)`;
- (ii) some lift has `c_0, c_1, c_2` collinear through `0`;
- (iii) some lift has `w₀ − w₂ ∈ ℝ⁴` and `w₁ − w₃ ∈ ℝ⁴`.

Proof:
- (i)⇒(ii): immediate.
- (ii)⇒(iii): right phases `d₁ = d₃ = e^{iθ}` rotate `c` and make it real. Then left phases `l_r` make each `a_r`
  real, and `b_r` with it, or make `b_r` real where `a_r = 0`. Both steps keep `|W|²`.
- (iii)⇒(i): `d₁ = d₃ = e^{−iπ/4}` puts every real `c_r` on `e^{iπ/4}ℝ`.

The torus form [P] is (ii) restricted to one two-sided orbit. Over the whole fibre the existential runs over every
orbit in it.

**Sufficient condition** [D]. If `Γ_W` is orthostochastic, then `Feas` holds: take `W = O` real in (iii). This covers
every Thread E control: monomial `Γ_W`, `J/4 = |H(1)|²`, and every 2+2 sum, since 2×2 doubly stochastic matrices are
orthostochastic [L]. Countercontrol: the fixed `W = H(1)` gives `c = (0,¼,0,−¼)`, with `Re ≠ Im`, so it separates
before right phases: **as required**.

**Q3b, 3+1 blocks** [D]. Let `Γ_W = P(B₃ ⊕ 1)Q`, with `P`, `Q` permutations and `B₃` any 3×3 unistochastic
matrix. Then `Feas` holds.
- *Reduction.* Row permutations preserve (iii). The column permutations `(0 2)`, `(1 3)` and `(0 1)(2 3)` send
  `(a,b)` to `(−a,b)`, `(a,−b)` and `(b,a)`, which preserve (iii). They generate a group transitive on `{0,1,2,3}`, so
  the singleton column may be taken at index 3.
- *Construction.* Take `W = V ⊕ 1`, with `V` a lift of `B₃`, left-phased so that `u := v₁ ∈ ℝ³`. Then `b` is real
  (its row-3 entry is `−½`). It remains to find phases with `d₀v₀ − d₂v₂ ∈ ℝ³`.
- *The real plane.* Let `R = u^⊥ ∩ ℝ³`, whose complex span is `span{v₀,v₂}`. A vector `r ∈ R` with
  `|⟨v₀,r⟩| = |⟨v₂,r⟩| = 1` is such a combination. Set `h(r) = |⟨v₀,r⟩|² − |⟨v₂,r⟩|² = rᵀSr`, with
  `S = Re(v₀v₀† − v₂v₂†)`.
- *Tracelessness.* `v₀v₀† + v₂v₂† = 1 − uuᵀ =: P_R`, which is real, so `S = P_R − 2Re(v₂v₂†)` and
  `tr_R S = 2 − 2‖v₂‖² = 0`.
- *Conclusion.* A traceless quadratic form on a real 2-plane vanishes at some `r̂` with `‖r̂‖ = 1`. Take `r = √2r̂`. ∎

Exact instance: `B₃ = J₃/3`, `V = [[1,1,1],[ω,1,ω²],[ω²,1,ω]]/√3`, `d₀ = d₂ = i`. Then `a = (0,−½,½,0)` and
`b = ½(1/√3,1/√3,1/√3,−1)`. After `d₁ = d₃ = e^{−iπ/4}`, column 1 of `|WH(1)|²` and of `|WH(i)|²` is the same,
`(1/12, 1/3 − 1/(2√6), 1/3 + 1/(2√6), 1/4)`, and so is column 3. `J₃/3` is not orthostochastic, so Q3b goes beyond the sufficient condition.

**Q3c, general `Γ_W`: OPEN.** Counting gives 2 phase parameters, `d₂/d₀` and `d₃/d₁`, against 2 real collinearity
conditions per orbit. Generic fibres are finite unions of two-sided orbits [L], so existence is a global question. No
proof of general feasibility and no infeasible `Γ_W` was found. A leading-order check near the identity, in one regime
`|X₀₁| ≫ |X₁₂|, |X₀₃| ≫ |X₂₃|`, found the leading-order equations solvable: their obstruction phase is
`≡ 0 (mod π)` by anti-Hermiticity. That is a heuristic only, unverified, with no non-degeneracy or higher-order
control.

**B3's relevance (unchanged).** By PL-BSEL2 B1-C(ii) [P], with ancilla-carrying device lifts the process-fixed
relation identifies TG3 for every `Γ_W`. Q3 bears only on `V`-only lifts, which "under a reading of Main:99's class
[…] are absent" (PL-BSEL2 l. 85). B3 is pure mathematics with representational relevance only.

### 3.4 B5
- **Q5a: MATHEMATICAL** [D].
  - `Γ^alt_0 = 1`; `1` and `J/4` are row-stochastic; the period is 2.
  - Both slices are symmetric, so `PPer`'s transpose orientation (Thread E §3.3(d)) changes nothing.
  - With `pper_has_responseRealization` [K RootedClassificationAllTime:162], `Γ^alt` has a finite reversible
    realization (Thread E §3.3(e)).
  - This confirms MM R2-3's [P] on paper.
- **Q5b: MATHEMATICAL** [D from K].
  - Each slice is admissible: `Γ(1) = 1` and `Γ(H(z)) = J/4`.
  - The slices at `t = 1` are not two-sided related [K TSG:907]. `TwoSidedRelated` needs every slice [K TSG:84], so
    the lifts are not related.
  - `U′_1U′_0ᴴ = H(i) ≠ H(1) = U_1U_0ᴴ`.
  - No Lean proof exists (D-39 not authorized).
- **Q5c.**
  - *Per-slice statements* (B1(a)–(c), Q1, Q1c, DC, and B4′'s C0/C1/C1′ rows) quantify over unitaries slice by
    slice and carry over unchanged [D].
  - *C2, R fails* [D]: with `g` given by `K_1 = diag(1,1,1,−1)` and `K_t = 1` otherwise, the procedure reading at
    `(1,3)` gives `𝒪₂(3,1) = |H(1)H(1)ᴴ|² = 1` for `U^alt` and `|H(1)KH(1)ᴴ|² = J/4` for `gU^alt`. The second equality
    follows from `1 − 2h₃h₃ᵀ`, entries `±½`. The factorized law is B4′ D4 [P], under `Rst-auto`.
  - *C2, Q fails* [D]: `U^alt` and `U′^alt` have equal C2 laws on every read list from every root `j`. Every factor
    is the same for both lifts: root `Γ_{t₁} ∈ {1, J/4}`, and `𝒪₂(t,s)` is `1` (same parity) or `J/4` (mixed
    parity), since `H(z)H(z)ᴴ = 1` and `|H(z)|² = J/4`. Yet the lifts are not `G`-related (Q5b). So
    COUNTEREXAMPLE[Q[C2], `Γ^alt ∈ PPer`, `|A| = 1`, `Rst-auto`]. It needs no gauge image. Unlike the constant TG3
    pair, C2 does not separate this pair even raw.
- **Q5d (GL2 re-placed): OPEN, not attempted.** It needs act 7's `U_B` and a reviewed choice of gauge time.

## §4. Results

| Question | Dir. | Verdict | Hypotheses | Support | Does NOT establish |
|---|---|---|---|---|---|
| Q1 | ⇐ | MATHEMATICAL (FI); fails under FI_c at `\|A\|≥2` (CE-3) | H-fac, one time, fixed `a₀` | [K] TSG:217, CLG:273; [D] | anything native |
| Q1 | ⇒ | MATHEMATICAL, any `\|A\|` | H-fac, one time, ∀U on `ℂ^{V×A}` | [P] Lemma HS; [D] CM, steps 1–4 | restricted `U` classes (OPEN); two times; `U`-dependent devices; physical availability |
| Q1c | ⇒, ⇐ | MATHEMATICAL: GR ⇔ D1 ∨ D2 ∨ D3 | as Q1⇒ | [D] | that any disjunct is physically supplied |
| B1(c) S, extended to `\|A\|≥2` | — | COUNTEREXAMPLE[mixed `ρ`] (CE-2); holds for pure `π`, `\|V\|≥2` | as Q1⇒ | [D] | nothing about S at `\|A\| = 1`, which stands |
| DC | — | MATHEMATICAL: `¬(R[C] ∧ Q[C])` at `\|V\|≥3` | one-time H-fac candidates, ∀U | [D]; [K] TSG:263, :870, :907 | native separation or identification; `\|V\| = 2` |
| Q3a | ⇔ | MATHEMATICAL ((i)⇔(ii)⇔(iii)) | 4×4, `\|W\|² = Γ_W` | [D]; reproduces [P] RHC7 | Q3 itself |
| Q3 suff. | ⇒ | orthostochastic ⇒ Feas: MATHEMATICAL | — | [D], [L] | the converse |
| Q3b | — | MATHEMATICAL: every `P(B₃⊕1)Q` feasible | — | [D] | general `Γ_W` |
| Q3c | — | OPEN | — | — | Yes or No |
| Q5a | — | MATHEMATICAL | — | [D]; [K] RCAT:162 | any native realization of the lifts |
| Q5b | — | MATHEMATICAL | — | [D from K] TSG:84, :907 | a kernel statement |
| Q5c | R[C2], Q[C2] | COUNTEREXAMPLE both, at `Γ^alt` | `\|A\|=1`, H-comp, Rst-auto, P-conf | [D], [P] B4′ D4 | `\|A\|≥2` |
| Q5d | — | OPEN (not attempted) | — | — | — |
| B3/B5 lanes | — | not decided | — | [O] D-36, D-38, D-39 | — |

Controls K1–K7 and the Q3 controls behaved as required.

## §5. Consequences for #914 (proposals only; nothing applied)

1. **MM §4c, one-time equivalence.** Proposed: "(⇒) PD, once independently reviewed, under ∀U, H-fac and reading FI. (⇐) holds
   under FI at every `|A|`, and under FI_c only at `|A| = 1`." This applies only after independent review.
2. **MM §4c, the withdrawn clause.** Q1c (D1 ∨ D2 ∨ D3) is a candidate replacement, with CE-1 recorded.
3. **B1(c) row.** Add the scope note: `|A| = 1` is load-bearing for mixed preparations (CE-2); S′ holds at `|A| ≥ 2`.
4. **New R-edges (not L-edges).**
   - DC informs B6 and #1064 (BSEL-3). A one-time H-fac interface that separates two-sided classes cannot be
     gauge-respecting, so any native separation route is two-time or outside H-fac.
   - DC also bears on P-22. At `|A| = 1` the GR one-time quotient is the SH/fibre quotient, and no gauge identification
     follows.
5. **MM Thread E row (table above §4c).**
   - "torus form CJ [P]" → reduction PD [D].
   - Add "3+1 blocks feasible (PD [D]); orthostochastic feasible; general Q3 OP".
   - "Stays a candidate" is unchanged.
6. **MM R2-3.** `PPer` membership of `Γ^alt`: [P] → PD [D], pending review. Add the `Γ^alt` C2 pair as a `PPer`
   witness for B4′'s C2 rows.
7. **Unchanged:** B6 ← O-REC, O-SET; O-BSEL's "gauge = operational (Z7)" prohibition; all holds and grades.

## §6. Open items and owner questions

**Open.**
- Q1⇒ for restricted `U` classes (one process's slices, OI-realizable lifts).
- Q3c (general `Γ_W`; fibres enumerated beyond phase orbits).
- Q5d (GL2).
- The `|A| ≥ 2` analogue of DC's strictness at `|V| = 2`.
- B2 (`|A| ≥ 2`, PL-BSEL2 l. 102) is partly addressed by Q1c. Its kernel controls (GI2's `A`-read, GL2's off-anchor
  read, `pq1b`) were not run through CH here.

**Owner questions.**
1. Is FI the intended reading of "fibre-identifying"?
2. Is ∀U the intended quantifier of the one-time equivalence?
3. Should Q1c replace the withdrawn clause, after review?
4. D-36: B3 as pure mathematics, or park? Q3b removes the 3+1 sub-item.
5. D-38 and D-39: B5's lane, and its Lean work.
6. May PL-BSEL2 and Thread E, which exist only off-repo, be quoted as sources? Their B3/B5 text is posted nowhere
   public.
7. Who reviews this note independently?

## §7. Proposed computation (for separate authorization only; none run)

1. **Exact controls for Q1c.** Gaussian-rational unitaries (Cayley transforms) at `|V| = |A| = 2` and at `|V| = 3`,
   `|A| = 1`:
   - D1–D3 instances must be GR;
   - single-entry perturbations must fail;
   - a scalar countercontrol.
2. **Q3c.** Exact fibre enumeration and feasibility for a generic non-block 4-level `Γ_W`, under Thread E's
   preregistered rule, which can certify Yes only. Q3b's family and orthostochastic `Γ_W` serve as positive
   controls.
3. **Q5c control.** A complete-record comparison of `U^alt` against `U′^alt` and against `gU^alt`, under `Rst-auto`,
   to horizon 4.
4. **Lean (D-39).** `PPer Γ^alt`; non-relatedness of the `Γ^alt` lifts; Lemma HS, Lemma CM, Q1 and Q1c. This needs a
   preregistration and the §A.35 registry contract.
