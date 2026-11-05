# BSEL-2 follow-up Q2A: O⇒G for C2-ch and C2-sel at `|V| = 2`, `|A| ≥ 2` (paper record)

**Status: WIP / UNVERIFIED; paper-only; not reviewed.**

**Authorization.** amaybaum, Claude Code session chat, 2026-11-05, as relayed by the coordinating session:
> Choose the proof-only direction, without lifting the scope boundary. Correction: the direction is O⇒G, not G⇒O. WE
> already disproves G⇒O for C2-ch and C2-sel. Authorize a narrowly scoped proof attempt for O⇒G at |V| = 2, |A| ≥ 2,
> preserving F §6's unresolved boundary.
> - Do not expand into counterexample searches that would resolve the protected F §6 question.
> - If the proof cannot be established, retain "not addressed"; do not infer a positive result.
> - Preserve the reviewed B4′ matrix and its conditional assumptions.
> - Prefer recording this as a separate follow-up unit rather than modifying the already reviewed #1123 head.
> - No new computation, Lean work, physical interpretation, theorem promotion or merge is authorized.

**Base.** Commit `7fe4cd86bd1ec89ac2711dfbf04466b952592398`, the reviewed head of the B4′ record (#1123). This record
adds one file and changes nothing else.

**Inputs.** The inputs are "B4PRIME" (`verification/programmes/oi-qm/reconstruction/bsel-2-b4prime-20261105/B4PRIME.md`
at `7fe4cd86`), cited by line. No definition, tuple or reading is added. The inputs used are:
- **Notation:** carrier, anchor, readbacks and anchored moduli (B4PRIME ll. 29–44); Facts W and L (ll. 45–47).
- **Candidate tuples:** C2-ch = (P-conf, Acc₂, Rd, H-comp, Rst-ch) and C2-sel = (P-conf, Acc₂, Rd, H-comp, Rst-sel)
  (l. 54).
- **Reading (r2):** the Rst-sel test follows every read (ll. 60–62).
- **Laws:** the factorized C2-ch law (W0.4, ll. 94–112) and the C2-sel ok-chain and `⊥` law (W0.5, ll. 113–126).
- **Conditional readings and sourcing gaps:** ll. 546–547 and 550–558.
- **Matrix cells:** the cells at `|V| = 2`, `|A| ≥ 2` (ll. 513, 515), and the scope note of §3.5 (ll. 349–358).

**Method.** Paper derivation and hand algebra only. [D] marks a step derived here; [K] marks a kernel line under
`verification/lean-mathlib/OIBridge/` at the base (TSG `TwoSidedGauge.lean`).

***

## §1. Targets (stated before any proof)

The two candidates are kept separate throughout. Each target is one direction only.
- **Q2A-ch (O⇒G for C2-ch).** For all lifts `U, U′` at `|V| = 2`, `|A| ≥ 2`: if `Λ_C2-ch(U) = Λ_C2-ch(U′)` on the
  complete record (every branch mass kept), then `TwoSidedRelated a₀ U U′` (`G`).
- **Q2A-sel (O⇒G for C2-sel).** The same statement with `Λ_C2-sel`. Every `(v,ok)` and `(v,⊥)` mass is kept,
  unnormalized.

**Verdicts.** Each target gets PROVED or NOT ESTABLISHED. The converse direction G⇒O is already disproved at this
scope by witness WE (B4PRIME ll. 513, 515). Neither verdict is an equivalence.

**Hard limit.** No counterexample to either target is sought or constructed. A candidate obstruction met along the
way is recorded in one line and not developed.

## §2. Lemmas (common to both targets)

Write `u_j := We_j` for a unitary slice `W` on `ℂ^{V×A}`. Put `g(W) := FG^{(0)}(W)(0,1) = ⟨P_0u_0, P_0u_1⟩`, the
`(0,1)` entry of the fibre-0 Gram matrix [K TSG:95].

### Lemma 1 (two-sided slice relation at `|V| = 2`, any `|A|`) [D from K]
For unitary slices `W, W′` at `|V| = 2`, the following are equivalent:
- (a) some `L ∈ 𝒢_L` and weak `K` give `W′ = LWK`;
- (b) `Γ(W) = Γ(W′)` and `|g(W)| = |g(W′)|`.

Each direction has its own proof (§A.34).
- **(a ⇒ b).** `gramPhaseEquiv_of_twoSided` (TSG:263, forward) gives `FG(W′) = D̄FG(W)D` with `D = diag(c)`, `|c_j| = 1`.
  - The diagonals agree, and they are `Γ` (`fibreGram_diag`, TSG:127).
  - The off-diagonal entry satisfies `g(W′) = c̄_0 g(W) c_1`, so the moduli agree.
- **(b ⇒ a).**
  - `Σ_i FG^{(i)} = 1` (`sum_fibreGram`, TSG:153). So `FG^{(1)}(0,1) = −g` for each slice, and each fibre's
    off-diagonal entries are conjugates.
  - If `g(W) = 0`, then `g(W′) = 0`; take `c ≡ 1`. Otherwise take `c_0 = 1` and `c_1 = g(W′)/g(W)`, which is a phase by
    (b). In both cases `FG(W′) = D̄FG(W)D` in both fibres.
  - That is `GramPhaseEquiv`, and `twoSided_slice_iff` (TSG:826, mpr) gives (a).

For lifts, `twoSidedRelated_iff` (TSG:839, both directions) makes `G(U,U′)` equivalent to (b) at every `t`.

### Lemma 2 (constant lifts) [D]
Let `U_t ≡ W` and `U′_t ≡ W′` for every `t`.
- **(i) `G` on constant lifts.** `G(U,U′)` holds exactly when `W` and `W′` satisfy Lemma 1 (a). By `twoSidedRelated_iff`
  in both directions, `G` is the slice condition at every `t`, and every slice is the same.
- **(ii) The C2-ch law.** `Λ_C2-ch(U)` is a function of `Γ(W)` alone, and determines it.
  - *Function of `Γ(W)`.* `T_{t,s} = WWᴴ = 1`, so `𝒪₂(t,s)(w,v) = ‖P_we_v‖² = δ_{wv}`. W0.4 (B4PRIME ll. 106–108)
    then gives `p(v₁,…,v_k|j) = Γ(W)(v₁,j)` when all the `v_m` are equal, and 0 otherwise.
  - *Determines it.* Single-read lists give `Γ(W)(·,j)` for every `j`.
- **(iii) The C2-sel law.** `Λ_C2-sel(U)` is a function of `(Γ(W), α(W))`, and determines it.
  - *First step* (W0.5, B4PRIME ll. 119–122): the factors are `α(W)(v₁,j)` for ok and `Γ(W)(v₁,j) − α(W)(v₁,j)`
    for `⊥`.
  - *Every later step* starts from `e_v`, with `T = 1`. The ok factor is `|⟨e_w,e_v⟩|² = δ_{wv}` and the `⊥` factor is
    `δ_{wv} − δ_{wv} = 0`.
  - *Determines it.* The single-read records `(v,ok)` and `(v,⊥)` give `α(W)` and `Γ(W) − α(W)`.

Constant families are lifts under ∀U (B4PRIME l. 34), so each target restricts to them.

## §3. Q2A-ch: NOT ESTABLISHED

- **Step 1** [D] (one direction only: Q2A-ch ⇒ S-ch). Restrict Q2A-ch to constant lifts. By Lemma 2 (i) and (ii),
  Q2A-ch implies:
  - **S-ch:** at `|V| = 2`, `|A| ≥ 2`, any two unitary slices with equal readback are two-sided related.
- **Step 2** (where the argument stops). S-ch is slice-wise `Fib ⊆ G` at `|V| = 2`, `|A| ≥ 2`.
  - That inclusion is what F's corollary DC turns on (F l. 243). It is decided at `|A| = 1` (F ll. 254–261), and its
    `|A| ≥ 2` case is the item F l. 430 leaves undecided.
  - A proof of Q2A-ch would therefore prove S-ch, and so decide F l. 430, in the positive direction.
  - The authorization preserves F §6's unresolved boundary. The argument stops here, before any attempt on S-ch.
- **The hypothesis a proof would need:** S-ch, or any statement implying it. It is not among the frozen inputs, and it
  is not added.
- **Verdict: NOT ESTABLISHED.** The B4PRIME matrix cell (l. 513, O⇒G) stays "not addressed".
- **Finding.** B4PRIME l. 356 says the proof direction "could be pursued without touching F l. 430". By Steps 1–2
  this does not hold for C2-ch: any proof of the proof direction decides F l. 430, positively. The reviewed record is
  not modified; the finding is for the owner.

## §4. Q2A-sel: NOT ESTABLISHED

- **Step 1** [D] (one direction only: Q2A-sel ⇒ S-sel). Restrict Q2A-sel to constant lifts. By Lemma 2 (i) and (iii),
  Q2A-sel implies:
  - **S-sel:** at `|V| = 2`, `|A| ≥ 2`, any two unitary slices with `Γ(W) = Γ(W′)` and `α(W) = α(W′)` are two-sided
    related.
- **Step 2** [D] (S-sel and the protected item).
  - S-ch implies S-sel, since S-sel has the stronger hypothesis.
  - So a proof of S-sel does not decide F l. 430. A refutation of S-sel would refute S-ch and decide it negatively.
    That route is outside the authorization and is not taken.
- **Step 3** [D] (proof attempt of S-sel, via Lemma 1).
  - It suffices to show `|g(W)| = |g(W′)|`.
  - *Decomposition.* Split the fibre parts of `u_j`: in fibre 0, `x_j e_{(0,a₀)} + q_j` with `q_j ⊥ e_{(0,a₀)}`; in
    fibre 1, `y_j e_{(1,a₀)} + r_j` with `r_j ⊥ e_{(1,a₀)}`.
    - Then `g = x̄_0x_1 + ⟨q_0,q_1⟩`.
    - Orthogonality of `u_0, u_1` gives `x̄_0x_1 + ⟨q_0,q_1⟩ + ȳ_0y_1 + ⟨r_0,r_1⟩ = 0`.
  - *What the data fix.* `α` fixes `|x_j|²` and `|y_j|²`, and `Γ` then fixes `‖q_j‖²` and `‖r_j‖²`. So the data fix
    `|x̄_0x_1|` and `|ȳ_0y_1|`, and bound `|⟨q_0,q_1⟩| ≤ ‖q_0‖‖q_1‖` and `|⟨r_0,r_1⟩| ≤ ‖r_0‖‖r_1‖`.
  - **Where the argument stops.** `|g|` depends on two things beyond these moduli: the modulus of `⟨q_0,q_1⟩` and its
    phase relative to `x̄_0x_1`. The frozen data constrain them only through the orthogonality relation. That relation
    equates `g` with `−(ȳ_0y_1 + ⟨r_0,r_1⟩)`, which carries the same two unknowns in fibre 1. No step from the frozen
    inputs derives `|g|`.
  - **Candidate obstruction, not developed (outside authorization):** the moduli that `(Γ, α)` fix do not visibly fix
    `|g|`.
- **The hypothesis a proof would need.**
  - The argument closes under the following condition, which is not among the frozen inputs. It is reported here and
    not adopted.
  - **(N):** at every `t` there are a fibre `i` and an input `j` with `Γ_t(i,j) = α_t(i,j)`.
  - (N) is read off the data, so if it holds for `U` it holds for `U′`.
  - *Why (N) suffices* [D]. For an arbitrary lift, single-read records at `t` give `Γ_t` and `α_t` (W0.5). Under (N)
    with `i = 0`, `q_j = 0`, so `|g_t| = |x_0||x_1| = (α_t(0,0)α_t(0,1))^{1/2}`. With `i = 1`, `r_j = 0`, and the
    orthogonality relation gives `|g_t| = |ȳ_0y_1| = (α_t(1,0)α_t(1,1))^{1/2}`. In either case Lemma 1 holds at
    every `t`, and `twoSidedRelated_iff` (mpr) gives `G`.
  - This settles no cell.
- **Verdict: NOT ESTABLISHED.** The B4PRIME matrix cell (l. 515, O⇒G) stays "not addressed".

## §5. Scope notes

- **Class.** Both reductions use constant lifts, which are admitted under ∀U. Constant lifts with `Γ ≠ 1` lie outside
  `PPer`, so neither reduction applies to the `PPer` subclass. That subclass is not attempted separately. The verdicts
  above are for the class of all unitary families, and the `PPer` class is not addressed.
- **Conditional readings.**
  - Every [D] statement here about C2-ch is CONDITIONAL[C2-ch = (P-conf, Acc₂, Rd, H-comp, Rst-ch), ∀U, fixed `a₀`].
  - Every [D] statement about C2-sel is CONDITIONAL[C2-sel = (P-conf, Acc₂, Rd, H-comp, Rst-sel), ∀U, fixed `a₀`,
    (r2)].
  - These are the readings of B4PRIME ll. 546–547.
- **SOURCING-GAP** (B4PRIME ll. 555–558):
  - P-conf;
  - Acc₂ (all records retained jointly);
  - Rd;
  - H-comp (its root clause, and `U_tU_sᴴ` between reads);
  - Rst-ch (the ancilla-replacement channel) for C2-ch, and Rst-sel (the `|a₀⟩⟨a₀|` test, `⊥` retained) for C2-sel;
  - which lift is OI's, the anchor `a₀`, and which candidate, if any, is native.

## §6. Results

| Target | Direction | Verdict | Stopping point | Hypothesis a proof would need |
|---|---|---|---|---|
| Q2A-ch | O⇒G, C2-ch, `\|V\| = 2`, `\|A\| ≥ 2`, all unitary families | NOT ESTABLISHED; cell stays "not addressed" | §3 Step 2: Q2A-ch implies S-ch, which is F l. 430's protected item | S-ch (not adopted) |
| Q2A-sel | O⇒G, C2-sel, `\|V\| = 2`, `\|A\| ≥ 2`, all unitary families | NOT ESTABLISHED; cell stays "not addressed" | §4 Step 3: `\|g\|` is not derived from `(Γ, α)` | (N), or S-sel (neither adopted) |

**Supporting statements** (proved [D], used only to locate the stops):
- Lemma 1, both directions;
- Lemma 2;
- the one-direction reductions Q2A-ch ⇒ S-ch and Q2A-sel ⇒ S-sel;
- the sufficiency of (N) for C2-sel.

**Does NOT establish.**
- Either target.
- Any answer to F l. 430.
- Any counterexample.
- Any `PPer`-class statement.
- Any physical gauge or operational claim.

The B4′ matrix and its conditional assumptions are unchanged. Nothing is promoted.
