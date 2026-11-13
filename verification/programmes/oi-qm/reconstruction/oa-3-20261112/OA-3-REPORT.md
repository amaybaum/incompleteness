# OA-3: native gbit or dual-gbit shapes in `G_SM`, and Theorem E(b) without (H4)

**Standing.** WIP / UNVERIFIED author report for unit OA-3 under #1169, ending in independent review.

- **Scope.** Paper-only: reading and hand derivations. No computation on any OI rule (no script,
  numerics, enumeration or LP), no Lean change, no manuscript edit, no premise adopted, no claim
  promoted. Nothing committed, pushed or posted.
- **Authorization.** Owner amaybaum, 2026-11-12, recorded on #1169 (as relayed by the coordinator;
  not re-fetched in this unit). Unit OA-3: one bounded paper-only investigation (OA-2 r3 "next step 1").
- **Commands used.** `git fetch`, `git show`, `git ls-tree`, `git grep`, `grep`, `sed`, `cut`, `fold`,
  `wc`, `cat -n`, `ls`, `mkdir`. No script was written or run. No source copy was written anywhere.

**Snapshots.**

- `main` = `615cc1190ec1bda69093be1eac49c839744008a5` (read with `git show origin/main:`).
- Research branch `research/oa1-w1-1-20261112` = `815d6a8ee110ec713b54549ba70c501eb8f1db59`
  (OA-1 r4, OA-2 r3 and their reviews).

**Citation forms.** `OA2:n` = `.../oa-2-20261112/OA-2-REPORT-r3.md` at `815d6a8e`; `Rv2:n` =
`REVIEW-OA-2.md` there; `OA1:n` = `.../oa-1-20261112/OA-1-REPORT-r4.md` at `815d6a8e`; `SM:n` =
`papers/SM.md`; `Main:n` = `papers/Main.md`; `M2:n` = `mechanism-2-20261108/DESIGN.md`; `MA:n` /
`MAR:n` = `minacc-1-20261108/DESIGN.md` / `RESULT.md`; `AP1:n` = `apparatus-1-20261107/DESIGN.md`;
`L3b:n` = `verification/programmes/oi-qm/interface/round-l3b-orthogonal-rule-controls/`; all of
`M2`, `MA`, `MAR`, `AP1` under `verification/programmes/oi-qm/reconstruction/` at `main@615cc119`.

**Support labels** as in OA2:43–51: [K] Lean statement read, [P] manuscript, [R] research record,
[W] hand derivation here (unreviewed), [L] literature from memory (context only), [O] open.

***

## 0. Plain-language summary

1. minacc-1's gate cancellation transfers to `G_SM` (on the right-hand side only). It *adds* access; it is a refuter of read restriction, not a source of it (N1).
2. In OA-2's E3 setting the observer's own cells are held, so they exert no unknown "kick". The class-N read restriction exists only under the supplied half-known-reader convention P2, which does not count (N1.3).
3. `G_SM`'s left edge is fixed and enters linearly. From that alone, three consecutive observer sites with retained history determine the entire configuration of a finite ring of `L` sites within `2(L−3)` ticks, whatever the settings (Lemma OBS, N2). The proof is measure-free.
4. Hence, for such observers, under μ-G, heralds, and horizon at least `4L − 10`, `G_SM`'s prepare–measure fragment is a simplex: neither the gbit shape nor the dual shape occurs (Theorem S, N3). The same holds for class N and for SM's rule at every `q`.
5. Non-nested reads (AW-OA2-4): OA-2's Lemma 1 needs heralded composites to count as effects. With them, multi-time joint statistics are available, variant (ii) coincides with variant (i), and Theorem E(b) holds without (H4) (N4).
6. Without them, a 3-cell shift with a one-cell observer already shows an exact gbit, and Lemma 1 fails. That "success" is a memory artefact of the convention, rule-independent, and does not count (N4.2).
7. **Verdict: OPEN, narrowed.** Still open: small observers (no three consecutive held sites), horizons shorter than about `4L`, μ other than μ-G, infinite windows. The preregistered computation (OA2:776–833) stays the decisive next step for that regime, with three design amendments (§4).

***

## 1. Definitions (kept from OA-2; nothing redefined)

- **Setup.** `𝔖 = (S, φ, (V, H), μ, A)` (OA2:83–92; OA1:90–105). Procedures `Proc(𝔖)`: waiting under
  `φ`, settings as cell contents (initial, or written by `φ` from records), heralds and discards
  (OA2:95–101). "Held" = a function of present `V` (OA1:107–110). MP-0b retains history (OA1:554–555).
- **Label conventions.** C-PM: a preparation's own label cells (setting, coin, herald records) are
  not effects; effects are post-processings of held records other than those (OA2:103–111). C-PM′:
  the labels are physically out of reach (OA2:112–117).
- **E3 operational class** `[p]`; `W = span(reachable laws)`, `U = ⋃ supp` (OA2:127–132).
  Induced maps; heralded branches subnormalized then renormalized (OA2:136–141). **Lemma 1**
  (closure): every `π ∈ Proc` induces a well-defined `π_E` because `e∘π` is available for every
  available `e` (OA2:224–227).
- **Criteria G0–G3** (OA2:143–152). G3 here is always the prepare–measure criterion (OA2:521–523).
- **H-AR** additive (cell-aligned, full-resolution) observer (OA2:175–186). **(H4)** nested records
  (OA2:486). **(SP)** spanning of reachable record laws (OA2:519–521). **(xiv)** measurement
  independence (Main:724). **Proposition B** (i)–(iv) (OA2:237–278). **Corollary B′**: G3 needs
  preparation or effect equivalences coarser than ontic equality (OA2:301–312).
- **Measures** μ-O (derived), μ-G and μ-R (posited, ledger (iv)) (OA1:96–105, :236–270). Each result
  below states which it uses.
- **The two shapes.** (a) gbit: two switch-selected reads `f₀, f₁` of one carrier, four reachable
  preparations fixing `(f₀, f₁)`, joint read unavailable under every protocol (OA2:767–770;
  𝔊_K, OA2:365–475; AP1 Lemma 4′, AP1:698–712; M2:521–529). (b) dual: complete reads, reachable laws
  confined to `W ⊊ ℝ^U` (OA2:280–299, :771–773).
- **Variant (ii) effect class (made explicit here; N4).** (V-ii-U): effects are post-processings of
  the final present `V` only (the literal reading of OA2:107–108 with "held = present `V`").
  (V-ii-H): in addition, heralded composites `e∘π` (herald at earlier ticks, then read) are
  available subnormalized effects, as Lemma 1's proof uses (OA2:226).

### 1.1 `G_SM`: definition and standing

- **Definition [P].** Ring of `L ≥ 4` sites, alphabet `ℤ/q`; `R(i, x) = i+2` if `x_{i+1} = 0`, else
  `i+1`; `L(i) = i−1` fixed; `x_i(t+1) = x_{L(i)}(t) + x_{R(i,x(t))}(t) − x_i(t−1) mod q` (SM:112).
  Bijective by explicit inverse (SM:106, :112).
- **At `q = 2` [R, hand-checked here].** `f_i(u) = u_{i−1} ⊕ (u_{i+1} ∨ u_{i+2})`, `F(u, v) = (f(u) ⊕ v, u)`
  (M2:157–164). Check: if `u_{i+1} = 1` the selected value is that 1, else `u_{i+2}`; this is
  `u_{i+1} ∨ u_{i+2}`. At `q = 2` the memory sign is immaterial (M2:167–168).
- **Status.** The state-dependent-geometry principle `s(t+1) = φ_{s(t)}(s(t))` is a stated
  hypothesis/principle, distinct from A6 (SM:104). The ring is SM's example of it, "not derived or
  selected by OI" (M2:199–209); its standing is an independently motivated proposal (M2:43–46). Any
  use as OI's rule is a Layer-0 revision under §A.29 (OA2:660–661).
- **Axioms (M2:184–193) [R].** A2, A3 (reach 2), A4 (center-free, translation) kept. **A5 broken**
  by the term `u_{i+1}u_{i+2}`. **Non-reciprocal for `L ≥ 5`**: `i` can read `i+2`, while `i+2`
  reads `i+1` and `i+3` or `i+4`. Lemma Q's argument does not apply.
- **CP status relative to R1 [R].** Joint-CP failure under R1 holds for every coupling rule
  (covariance group `A_4 ≀ S_n`, not Clifford) and does not single out `G_SM` (M2:455–471, :761).
  P★'s C-CP failure is R1-relative. OA-2 treats these as G4-type: they count for nothing either way
  in E3 (OA2:671–672). Nothing below uses R1.
- **The feature used below.** For every state, `f_i` contains `u_{i−1}` with coefficient 1, ungated:
  `G_SM` is permutive in its left edge (for the property's name in the corpus: L3b
  `preregistration.md`:65–66, :105–109; `result.md`:51–53). SM:112's own remark ("the update adds the hidden
  value `x_{L−1}(t)`") is the same edge seen from the visible side.

***

## 2. Depth-first chain

### N1. minacc-1's gate cancellation in `G_SM` (first item: rule in or out)

**N1.1 Source [R].** Under `G_σ = OR(u_{i−1}, u_{i−2}) ⊕ OR(u_{i+1}, u_{i+2})` (MAR:36–40), a reader
whose own `u` is unknown has no backaction when the far cell of the gated pair is 1, because
`OR(α, 1) = 1`; protocol `E_A` determines `u + v` of an active cell in every branch (MAR:201–256).
Resources: P2 half-known ready cells, one known-1 cell (H-PREP), P1 registration with archive-swap
refills (MAR:297–318; MA:294–326, "No cell with both slots known is supplied").

**N1.2 Transfer to `G_SM` [W].** In `G_SM` only the right side is gated, so the mirror image works
with the reader on the right. Sites are relative to target 0, with `(u_0, v_0) = (x, y)`:

- t = 0 (Π_A-type supplies): cell −1 known `u = 0` (P2); reader cell 1 known `v = 0`, unknown
  `u = α` (P2); gate cell 2 known `u = 1` (H-PREP); cell 3 arbitrary.
- Tick 1: `u_1(1) = v_1 ⊕ u_0 ⊕ OR(u_2, u_3) = x ⊕ 1`, so register `r_1 = x ⊕ 1`.
  `u_0(1) = v_0 ⊕ u_{−1} ⊕ OR(u_1, u_2) = y ⊕ OR(α, 1) = y ⊕ 1`, and `v_0(1) = x`. The reader's unknown
  `α` does not reach cell 0.
- Refill cells −1, 1, 2 to the `t = 0` specification (fresh `α₂`).
- Tick 2: `u_1(2) = 0 ⊕ (y ⊕ 1) ⊕ OR(1, ·) = y`, so register `r_2 = y`.
  `u_0(2) = x ⊕ 0 ⊕ OR(α₂, 1) = x ⊕ 1`, and `v_0(2) = y ⊕ 1`.
- **Exposure.** Cell 0 is active, unregistered and sharp at `t = 2`, `(u, v) = (r_1, r_2 ⊕ 1)`. Its
  `u + v` is determined in every branch. This is minacc-1's (B-D), now for `G_SM`.
- **Mechanism-off control (hand).** With `R ≡ i+1` (class N; M2:195–197) the same schedule gives
  `u_0(1) = y ⊕ α`, masked: protection returns, as required.
- **Observation (ELABORATING).** In the other linear limit `R ≡ i+2` (`f_i = u_{i−1} ⊕ u_{i+2}`,
  non-symmetric) cell 1 does not enter `f_0` at all, so this limit does not restore protection. What
  removes the backaction is a coupling that is one-way at that tick. Gate cancellation is one way to
  get it; the non-reciprocity of M2:191 is another. This agrees with "a gate whose influence is
  one-way" (MAR:93–95).

**N1.3 What this means in E3 [W].** OA-2's E3 observer holds its own cells, so their contents are
held records, known to every effect. Hence:

- A `V`-cell reader has no unknown slot. There is no kick to cancel, and no gate cancellation is
  needed (N2 makes this exact).
- The class-N read restriction (Lemma Q protection; native `Z`/`X` reads only, OA2:627–656) rests on
  readers that carry an unknown slot. That is P2 (MA:297–300) together with P1. It is a supplied
  convention, not a property of the rule.

**Verdict N1.** Gate cancellation is **ruled in as a refuter**: it transfers to `G_SM` and defeats
the P2-based restriction even where that convention is imposed. It is **ruled out as a source** of
shape (a): it supplies access, not restriction. Measure-free: determination is a support statement
for any full-support prior on the unknown slots (MAR:255). CONFIRMING (minacc-1), with the
one-way-coupling observation ELABORATING.

### N2. Lemma OBS: a three-site held block observes the whole ring

**Lemma OBS [W].** Take SM's rule (SM:112) at any `q ≥ 2` and either memory sign, on a ring of `L ≥ 4`
sites. Let `V ⊇ {a, a+1, a+2}` with H-AR. Then:

- **(i)** The history of the three `u`-slots over `[0, T]`, together with `v_a(0)`, determines the
  full configuration at time `L − 3` whenever `T ≥ 2(L−3)`. By bijectivity it therefore determines
  the full initial configuration.
- **(ii)** Without `v_a(0)`, the `u`-history over `[1, T_M]` determines the configuration at time 0
  whenever `T_M ≥ 2(L−2)`.
- **(iii)** Both hold for every setting (every content of `V`) and pointwise in the configuration, so
  they are measure-free.

*Proof.* Write `x_j(t)` for the `u`-slot; then `v_j(t) = x_j(t−1)`. The update at site `j`,

  `x_j(t+1) = x_{j−1}(t) + x_{R(j, x(t))}(t) ∓ x_j(t−1)`,

is solved for the left neighbour:

  `x_{j−1}(t) = x_j(t+1) − x_{R(j, x(t))}(t) ± x_j(t−1)`.   (★)

`R(j, x(t))` and `x_R(t)` need only `x_{j+1}(t)` and `x_{j+2}(t)`. For `j = a`, all three of
`x_{a+1}, x_{a+2}` and the history of `x_a` are held. Let `D_k` be the set of times at which
`x_{a−k}` is determined, with `D_0 = D_{−1} = D_{−2} = [0, T]`. For `t = 0`, (★) at `j = a` uses
`v_a(0)`.

- `k = 1`: `D_1 = [0, T−1]`.
- `k ≥ 2`: (★) at `j = a−k+1` needs `x_{a−k+1}` at `t ± 1` and `x_{a−k+2}`, `x_{a−k+3}` at `t`. Those were
  determined at depths `k−1`, `k−2`, `k−3`, or are held. By induction `D_k = [k−1, T−k]`.
- Site `a−k`'s pair `(x(t*), x(t*−1))` is determined at `t* ∈ [k, T−k]`.
- The hidden sites are `a−1, …, a−(L−3)` (going round the ring to `a+3`). They are all determined
  at the common time `t* = L−3` when `T ≥ 2(L−3)`. The held sites are known at `t*` directly.

For (ii), start (★) at `t ≥ 2`: `D_k = [k+1, T_M−k]`, and the common time exists when
`T_M ≥ 2(L−2)`.

No step uses a gate value, a setting, a known ready cell or a measure. Each step is the
left-edge permutivity of (★). ∎

- **Generality.** The proof needs only that the update is bijective in `x_{j−1}` given the right-hand
  arguments, which reach `r` sites. A block of `r + 1` held sites then suffices. Class N (`r = 1`)
  needs a 2-block. `G_σ` has no ungated edge and is **not** covered.
- **Hand check on `L = 4`.** The hidden site is `a+3 = a−1`. (★) at `j = a` gives `x_{a−1}(t)` for
  `t ∈ [0, T−1]`, so its pair is known at `t* = 1` once `T ≥ 2 = 2(L−3)`. ✓
- **Bearing on shape (a).** For any carrier, every functional pair is jointly read by the single
  procedure "wait `2(L−2)`, read the history". The gbit's "joint read unavailable under every
  protocol" fails.
- **Bearing on N-a.** `G_SM`'s setting-gated reads at the right end of `V` (OA2:665: N-a met) are
  real but irrelevant here: completeness comes from the ungated edge, whatever the settings.

**Verdict N2: NO for shape (a)**, for `G_SM`, class N and SM's rule at every `q`. Class: H-AR observer
with three (class N: two) consecutive held sites; retained history (H4), or heralded composites
(N4); horizon at least `2(L−2)` after handoff; finite ring. Measure-free. Candidate NEW (§5).

### N3. Theorem S: the dual shape is closed for the same observers under μ-G

**Theorem S [W].** Assume Lemma OBS's observer, μ-G (uniform on `C_V × C_H`, Main:58), heralds
(OA2:96–97, :800–801), C-PM, and horizon at least `4L − 10`: a preparation stage of at least
`2(L−3)` and a measurement stage of at least `2(L−2)`. Then the prepare–measure fragment of `G_SM`
(likewise class N, and SM's rule at any `q`) is simplex-embeddable, and `E` is a simplex. G1 and G3
fail.

*Proof.*

1. **Point preparations of every configuration.** Run `T₁ ≥ 2(L−3)` ticks. Herald on the full held
   history, including `V(0)`, which is held at `t = 0`.
   - μ-G is invariant and `F` is a bijection, so `ω(T₁)` is uniform on `S`.
   - By Lemma OBS(i), the herald value determines `ω(T₁)`.
   - So every `δ_ω`, `ω ∈ S`, is a heralded preparation, with probability `|S|^{−1} > 0`. This is
     OA-1 D3's cost (OA1:152–156), paid.
   - Hence `W = ℝ^S`.
2. **Complete effects.** By Lemma OBS(ii), the post-handoff history over `[T₁+1, T₁+2(L−2)]`
   determines `ω(T₁)`. It uses no label cell: no `V(T₁)` entry and no `v`-slot copy of it. So every
   function on `S` is an available effect.
   - The read also reveals the label. C-PM′ therefore fails physically, which only refines the
     equivalences.
3. **The model.** Take the ontic state to be the configuration at handoff, each preparation to its
   law, and each effect to its response.
   - Prepare–measure statistics are reproduced, because `F` is deterministic.
   - Proposition B(i): `R` is injective on `W` (step 2), so the model is preparation-noncontextual.
   - Proposition B(ii) (⇐): `W = ℝ^S` (step 1) makes `ρ` injective, so the model is
     measurement-noncontextual.
   - Proposition B(iv): the model is a simplex embedding.
   - `E = R(Δ(S))` with `R` injective is a simplex.
   - Shorter procedures in the same fragment are laws on `S` and responses on `S`, so they are
     covered. ∎

- **Measure.** μ-G is used once, for full support of `ω(T₁)`. Not established under μ-O (orbit
  support; (xiv) may fail, OA1:179–184) or μ-R. Not established with MP-0a declared cells, whose
  law is neither invariant nor of full support (OA1:230–231).
- **Relation to M2 Theorem NC (ELABORATING).** NC needed spanning certification, and at `q = 2` a
  `Y` read not exhibited natively (M2:485–537). In E3 with a held 3-block, spanning on the
  configuration space is supplied natively, by observability plus heralds. This is a different
  object (configuration E3, not R1-encoded cells under P1/P2). It does not decide M2's A6 at the
  native `Z`/`X` level.
- **Classical control.** 𝔊_K passes G3 because its conveyors keep labels and old contents out of
  reach for the horizon, with no return path (OA2:404–426). In `G_SM`, the ungated left edge is a
  native return path of exactly the kind 𝔊_K is designed to lack. The negative is consistent with
  the control.
- **Scope, skeptically.** The horizon `≈ 4L` is of the order of the ring size. Physically relevant
  horizons `T ≪ L` are **not** covered. On a line, or for `T < 2(L−2)`, hidden sites at depth in
  `(T/2, T]` still feed the records through the left chain but are not determined, and the right-hand
  hidden region is read only through OR terms. The question stays open there.

**Verdict N3: NO for shape (b) (and (a))** within Theorem S's class. Scoped to that class; not an
impossibility for `G_SM`. Candidate NEW.

### N4. Theorem E(b) without (H4): the variant-(ii) effect class decides AW-OA2-4

**N4.1 The hidden assumption.** OA-2 treats the non-nested case as "only the marginals are
available statistics" (OA2:549–551; Rv2:115–122). Two of OA-2's own statements bear on this:

- Lemma 1 asserts well-defined `π_E` for every `π ∈ Proc`, heralds included (OA2:136–141, :224–227).
- Its proof uses "`e∘π` is available".

For heralded `π` under "held = present `V`", `e∘π` (herald at `τ₁`, read at `τ₂`) is not a
post-processing of the final present `V`. So it is available only under (V-ii-H), not under
(V-ii-U).

**N4.2 Under (V-ii-U): an exact gbit for a trivial affine rule [W].**

- **Setup.**
  - `Φ` = cyclic shift on 3 cells, `ω(t+1)_i = ω(t)_{i−1}`. It is linear, an additive bijection,
    so (H1) holds as stated in OA2:483.
  - `V` = cell 0 (H-AR). μ-G. No settings, so (xiv) holds trivially; (H3) holds.
  - At `t = 0`: cell 0 holds `p`, cell 2 holds `x`, cell 1 holds `y`. `V` holds `x` at `t ≡ 1`,
    `y` at `t ≡ 2` and `p` at `t ≡ 0 (mod 3)`.
- **Preparations.** Herald `V(1) = a` and `V(2) = b`, with handoff at `t_h = 3`. The configuration
  returns to its initial form, with `(x, y) = (a, b)` sharp. These are four point preparations
  `[ab]`, each with probability ¼. Coin mixtures are taken under C-PM for the coin (as OA2:435–438).
  The herald cells are past `V` contents, so C-PM is met.
- **Effects.** Under (V-ii-U), an effect is a function of `V(t_h + τ′) ∈ {p, x, y}`: one variable at a
  time.
  - `A = ½([00]+[11])` and `B = ½([01]+[10])` have equal `p` and uniform `x`- and `y`-marginals. So
    `A ∼ B`.
  - `X` (`τ′ = 1`) and `Y` (`τ′ = 2`) are sharp on `[ab]`.
- **Contradiction.** OA-2 Claim 2's argument applies verbatim (OA2:427–442): the four supports are
  disjoint, and `½(μ₀₀+μ₁₁) = ½(μ₀₁+μ₁₀)` is impossible. So the fragment is
  preparation-contextual, and G3 passes.
- **Lemma 1 fails here.**
  - Let `π` = herald `V(t_h+1) = 0`.
  - Then `π(A) = [00]` and `π(B) = [01]`, and reading `V(t_h+2)` gives 0 against 1.
  - So `A ∼ B` but `π(A) ≁ π(B)`.
- **Pressure test (favourable branch, maximum skepticism).**
  - Nothing in `Φ` supplies the restriction. It comes from a one-cell memory and from heralds that
    condition at several ticks while effects cannot. The identity on a cell with a rotating register
    does the same.
  - So the access restriction is **imposed by convention, not native**. G3 here does not
    discriminate even trivial dynamics, which fails the classical control more severely than 𝔊_K.
    Non-import is trivially met.
  - **Would establish:** that the narrow variant-(ii) class makes G3 non-discriminating.
  - **Would not establish:** anything about any OI rule, admissibility (§A.29), non-import's bearing
    on OI, unbounded horizons, or a qubit-type fragment.
  - **Prior art:** OA-1 D8(c)'s cyclic permutation `(y, r, h) ↦ (h, y, r)` (OA1:216–223), and the
    ingredient anticipated at Rv2:124–132. The missing piece there ("a counterexample that also
    meets C-PM", OA2:555–556; Rv2:131–132) is supplied here, *for the narrow class only*.

**N4.3 Under (V-ii-H): Theorem E(b) holds without (H4) [W].** Assume (H1), H-AR, (H3), (xiv), C-PM and
**(SP)**, where (SP) is read for the formal joint record `Z = (Z_τ)_{τ ≤ T}`, which is never held at
once.

1. **Records.** By Theorem E(a) (OA2:509–511), `Z_τ = Z₀^τ(ω) + h_τ(c)`, measure-free.
2. **Effects.** Each available effect is either a single-tick read `f(Z_τ)` or a heralded composite
   `Π_i [Z_{τ_i} = r_i] · f(Z_τ)`. Both are functions of `λ = Z₀` after translation by `h(c)`.
3. **Model.** `ι(s)` = law of `Z₀` under `s`; responses as in step 2. It reproduces every statistic.
4. **Preparation NC.** Singleton indicators `[Z = λ + h(c)]` are available, as heralds at every tick
   followed by a final read. So two equivalent preparations have equal laws of `Z₀`.
5. **Measurement NC.** By Proposition B(ii) (⇐) on the `Z₀` model with (SP) (OA2:519–521).
6. **Conclusion.** The model is a simplex embedding of the prepare–measure fragment. Transformation
   noncontextuality is not claimed (as OA2:524–525). ∎

**N4.4 Corollary (variants coincide) [W].** Under (V-ii-H):

- the effect cone is the cone generated by the joint indicators `[Z = z]`, which is variant (i)'s
  cone;
- preparations heralded on a history are the same as sequential single-tick heralds;
- simplex-embeddability is a condition on linear maps that are positive on these cones (OA-2's
  G3 definition, OA2:150 [L: Schmid et al. 2021]), so variants (i) and (ii) give the same verdict.

**Verdict N4.**

- Under (V-ii-H), which Lemma 1 requires, **AW-OA2-4 is not an exit for the affine class**:
  E(b) holds without (H4), under (H1), H-AR, (H3), (xiv) and (SP). The measure row is as OA2:733:
  (xiv) holds for disjoint cells under μ-G and may fail under μ-O and μ-R.
- Under (V-ii-U), an exit exists, but it is convention-imposed and rule-independent, and OA-2's
  Lemma 1 fails there. It does not count.
- The affine class at E3 without (SP) stays open (OA2:762).
- Candidate NEW: a hidden assumption in OA-2's effect class (§5).

### N5. What remains for `G_SM`: small observers and short horizons

**Candidate mechanism (not decided) [W].** With `|V| ≤ 2`, (★) leaves residuals. For
`V = {a, a+1}` at `q = 2`, site `a+1`'s update gives `o(t) = OR(u_{a+2}(t), u_{a+3}(t))`. Site `a`'s
update then determines `u_{a−1}(t)` in three cases out of four:

- when `u_{a+1}(t) = 1`;
- when `u_{a+1}(t) = 0` and `o(t) = 0`;
- in the remaining case (`u_{a+1}(t) = 0`, `o(t) = 1`) only `u_{a−1}(t) ⊕ u_{a+2}(t)` is
  determined.

These residuals are data-dependent and gated by held contents. Separately, the left-end setting
`u_a` gates the hidden–hidden edge `{a−2 ← a−1}`, since `OR(u_{a−1}, u_a)` enters `f_{a−2}`. That is
a genuinely non-translational setting action on `H`.

**What a native gbit would need.** In E3 every influence of `V` on `H` is a function of held data,
so it is a known translation. An unknown disturbance on a carrier can come only from hidden cells
(μ-dependent). A gbit would therefore need held settings to route hidden noise into a hidden carrier
selectively, against the residuals above.

**Verdict N5.** Not derivable by hand without enumerating protocols, which is outside this unit's
authorization. **OPEN.**

***

## 3. Candidates and controls

| Candidate | Passes G3 (prepare–measure)? | Access restriction native? | Classical control (𝔊_K) | Non-import | Verdict |
|---|---|---|---|---|---|
| C1. Lemma-Q / P2 read restriction transplanted into `G_SM` as gbit source | No: class N's native `Z`/`X` fragment is NC (OA2:627–656); in `G_SM`, gate cancellation defeats it (N1.2) | No: P2 is supplied (MA:297–300) | — | met | Ruled out |
| C2. Gate-cancellation reads (minacc-1 mechanism, mirrored) | No: it adds access | Native (rule), but access, not restriction | — | met | Refuter, ruled in |
| C3. One-site or any carrier, observer ⊇ 3 consecutive held sites, history | No (N2, N3) | Rule supplies the opposite: an ungated return path | Consistent: 𝔊_K lacks a return path | met | NO in class of Theorem S |
| C4. Dual shape via restricted preparations, same observer | No: heralds reach every `δ_ω` under μ-G (N3) | — | — | met | NO in class of Theorem S |
| C5. Small observers (`|V| ≤ 2`), setting-gated OR reads; short horizons | Not decided | Possible (non-translational gating, N5) | Not run | met by construction (no quantum structure in the definitions) | OPEN |
| C6. Memory gbit under (V-ii-U) (3-cell shift) | **Yes** | **No**: imposed by the held-record and herald convention; rule-independent | Fails to discriminate (trivial dynamics pass) | met | Does not count |
| C7. Affine class, non-nested reads, (V-ii-H) | No, under (SP), (xiv) (N4.3) | — | — | met | NO; AW-OA2-4 closed as an exit |

**Controls applied in the derivations.**

- *CC-OFF for N1.2.* `R ≡ i+1` must mask: it does (`y ⊕ α`). `R ≡ i+2` does not restore protection,
  as reported.
- *Must-break for Lemma OBS.* `G_σ` has no ungated edge. (★) cannot be solved at `j = a`, since
  `OR(u_{a−1}, u_{a−2})` is not invertible in `u_{a−1}`. So the lemma correctly does not cover it.
  MAR's exposure under `G_σ` uses refills and P2, not observability.
- *Positive control for N4.2.* OA-2's 𝔊_K Claim 2 argument (OA2:427–442) is used verbatim. The shift
  example is checked tick by tick above.
- *Non-vacuity of N4.2.* Two operationally distinct classes exist (`[00]` vs `[11]`), and two
  non-equivalent effects (`X`, `Y`). This is the guard of OA2:809–811.
- *Target-neutrality.* Every object uses only laws on `S`, `[0, 1]` responses and convex structure.
  R1, CP and Hilbert space enter nowhere.

***

## 4. Conclusion

**OPEN, narrowed**, with the following established by hand at [W] level, unreviewed:

1. **Shape (a), gbit:** NO for `G_SM` with H-AR observers holding three consecutive sites, retained
   history or heralded composites, horizon at least `2(L−2)`, finite ring. Measure-free (N2).
2. **Shape (b), dual:** NO for the same class, under μ-G, with horizon at least `4L − 10` (N3).
3. **Gate cancellation:** transfers to `G_SM` and is a refuter of read restriction (N1).
4. **Theorem E(b) without (H4):** holds under (V-ii-H), which Lemma 1 requires. Under (V-ii-U) the
   gbit pattern appears for a 3-cell shift and does not count (N4).

**Precise remaining question.** For `G_SM` at `q = 2`, an H-AR observer with no three consecutive
held sites (for example `V = {0, 1}`), horizon `T < 4L − 10`, μ-G, C-PM, and heralded composites as
effects (so variant (i) = (ii)): is the closure-defined prepare–measure fragment
simplex-embeddable? And for `T ≪ L` with any observer?

**Is the preregistered computation still decisive?** Yes, for exactly that regime. OA-2's `G_SM`
object (`V = {0, 1}`, `Z_5`, `T ≤ 4`, OA2:797) lies outside Lemma OBS (`|V| = 2`; `T < 10`). Three
design amendments are proposed for the future preregistration. Each needs owner authorization before
anything runs.

1. **Variant (ii) effect class.** State it. If heralded composites are effects (Lemma 1), variant (ii)
   equals variant (i) (N4.4), so drop it or keep it only as a pipeline cross-check. If the narrow
   class is kept, add the 3-cell shift with a one-cell `V` (or OA-1 D8(c)'s permutation) as a
   memory-artefact control that must return non-embeddable. A non-embeddable variant-(ii) verdict
   for `N₁` or `G_SM` then carries no rule-specific information without a preregistered
   discriminating criterion. This replaces the "measurement without a prediction" reading of
   OA2:818–819.
2. **Predicted-embeddable `G_SM` control (independent proof: Theorem S).** `G_SM` on `Z_4` (one hidden
   site) with `V` three consecutive sites, μ-G, heralds, horizon at least `4L − 10 = 6`. It must
   return embeddable. A class-N analogue with a 2-block has horizon at least `4L − 6`.
3. **Keep** 𝔊_K (positive), the variant-(ii) single-cell control (OA2:814–817), and the non-vacuity
   guards. The `G_SM` test object stays as preregistered.

***

## 5. Status table

| Item | Status | Support | Measure |
|---|---|---|---|
| `G_SM` definition, bijectivity, `q = 2` OR form | manuscript / research record, re-checked by hand | [P] SM:112, :106; [R] M2:157–164 | — |
| `G_SM` standing: state-dependent-geometry principle stated as a hypothesis; ring an example | as recorded | [P] SM:104; [R] M2:43–46, :199–209 | — |
| A5 broken; non-reciprocal for `L ≥ 5`; CP verdicts relative to R1 only | as recorded | [R] M2:184–193, :455–471 | — |
| N1.2 gate-cancellation exposure `E_A^SM` (Π_A-type supplies) | derived here | [W] on [R] MAR:201–256 | any full-support prior (support statement) |
| N1.2 `R ≡ i+2` limit does not restore protection | derived here | [W] | measure-free |
| Lemma OBS (left-edge observability; any `q`, either sign) | derived here; candidate NEW | [W] | measure-free |
| Shape (a) excluded for ≥3-block held observers | derived here | [W] | measure-free |
| Theorem S (simplex fragment; shapes (a), (b) excluded) | derived here; candidate NEW | [W] + OA-2 Proposition B [W/RW] | μ-G only |
| N4.2 memory gbit under (V-ii-U); Lemma 1 fails there | derived here; does not count | [W]; prior art OA1:216–223, Rv2:124–132 | μ-G (any full-support law on `(x, y)`) |
| N4.3 Theorem E(b) without (H4) under (V-ii-H) | derived here; candidate NEW (hidden-assumption finding) | [W] on OA-2 Theorem E(a) [R/W] | as OA2:733 |
| N4.4 variants (i) and (ii) coincide under (V-ii-H) | derived here | [W]; [L] Schmid et al. 2021 for the cone formulation | as N4.3 |
| `G_SM`, small observers / `T ≪ L` / μ-O, μ-R / infinite windows | open | [O] | — |
| Affine class without (SP) | open | [O] (OA2:762) | — |

**§A.31 classification (one pass; fixed point not reached).** The productivity test is OA-2's
(OA2:866–867).

- **Lemma OBS:** NEW (candidate). It is strictly stronger than "the rule couples `V` to `H`", it
  constrains where non-embeddability can occur, and it exposes that an ungated permutive edge is a
  native return path.
- **Theorem S:** NEW (candidate), scoped negative.
- **N4:** NEW (candidate), hidden assumption in OA-2's variant-(ii) effect class and Lemma 1.
- **N1:** CONFIRMING, with an ELABORATING observation.
- **Tally:** 3 NEW candidates, all unreviewed [W].

**Assumption-watch markers.**

- **AW-OA3-1 (ungated permutive edge).** Any proposed `G(x)` or rule with an edge entering
  bijectively for every state is fully observable from a held block of width (one-sided reach + 1) on
  a finite ring. M-INACC (M2:832–871) therefore needs every return path gateable, as in `G_σ`.
  Cross-propagates to M2 §6.2's "what would derive it" and to any symmetrized `G(x)` proposal.
- **AW-OA3-2 (heralded composites).** Any record-level claim that uses present-`V` reads together with
  heralds must state whether heralded composites are effects. This applies to OA-2 Lemma 1 and
  variant (ii), and to "only the marginals are available" (OA2:550–551). OA-1 D2 (OA1:141–150) is a
  single-time statement and is unaffected as stated. Its reading as a retention no-go should be
  checked against this marker.

***

## 6. Reading inventory

**At `main` `615cc119`.**

- `papers/SM.md`: heading index; :56; :100–169 (§3.1 whole; :104 principle, :106 bijectivity, :112 the
  explicit construction and its visible-sector remark), read via `sed`/`fold`.
- `papers/Main.md`: :42, :54, :58, :60 (spot reads); grep for `G_SM` and "state-dependent".
- `mechanism-2-20261108/DESIGN.md`: :1–330, :360–560, :560–760, :760–880.
- `minacc-1-20261108/RESULT.md`: :1–420. `DESIGN.md`: :294–330 and a grep. Amendments: line
  counts only, not read.
- `apparatus-1-20261107/DESIGN.md`: :694–730.
- L3b round (`interface/round-l3b-orthogonal-rule-controls/`): grep of `result.md` and
  `preregistration.md` for permutivity.
- `git grep` over `verification/programmes/oi-qm/`, `papers/SM.md` and `papers/Main.md` for prior art
  on observability and heralded effects. No prior statement of Lemma OBS or N4 was found; L3b frames
  edge-permutivity as the axis of the masking argument.

**At research branch `815d6a8e`.**

- `OA-2-REPORT-r3.md`: whole.
- `REVIEW-OA-2.md`: :60–140 and grep. `REVIEW-OA-2-r2.md`: grep.
- `OA-1-REPORT-r4.md`: :85–275, :540–575.

**Not read.**

- OA-2 r1 and r2.
- REVIEW-OA-1*.
- minacc-1 amendments (A1–A3) and DESIGN outside :294–330.
- QA, FB, PI (`physical-interface.md`), obsmu, MECH-1, mathcon1, TUNE-1.
- AP1 outside :694–730.
- SM outside the lines above.
- The literature [L].

Negative claims are limited to these sources. "No prior statement found" rests on the grep above.

***

## 7. Limits

- Every [W] item is an unreviewed hand derivation; none is kernel-checked or computed.
- Theorem S needs:
  - a finite ring;
  - μ-G (full support);
  - three consecutive held sites;
  - H-AR;
  - history, or heralded composites;
  - horizon of at least `4L − 10`.

  It says nothing about `T ≪ L`, lattice windows, μ-O, μ-R, MP-0a laws, non-additive observers
  (AW-OA2-1) or unbounded horizons (AW-OA2-2).
- N4.3 needs (SP) for the formal joint record. N4.2's example satisfies (H1) as OA-2 states it,
  but it is not a gauge-derived OI rule. Its role is to show the convention, not OI physics.
- C-PM's treatment of labels that return to `V` in a fixed layout is used as OA-2 uses it. In
  Theorem S the labels are physically readable, which only refines equivalences.
- No manuscript claim is affected. No premise is adopted. Theorem S is not an impossibility result
  for `G_SM`, and N4 does not promote any OI claim.
