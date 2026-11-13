# OA-2 (r3): can deterministic dynamics induce operations on emergent observer states richer than permutations, with one common preparation and readout?

**Standing (r3).** WIP / UNVERIFIED author report for unit OA-2 under #1169, revision r3.

- It applies nits N1–N7 of the re-check `REVIEW-OA-2-r2.md` (verdict ACCEPT WITH NITS).
- No verdict moves. Section 10 lists the r3 changes.
- r1 (`OA-2-REPORT.md`) and r2 (`OA-2-REPORT-r2.md`) are unchanged.

**Standing (r2, retained).** r2 applied F1–F9 and the item 8/9 notes of `REVIEW-OA-2.md` (verdict
REVISE). Section 9 maps each finding to its change.

- **Scope.** Paper-only: reading and hand derivations. No computation on any OI rule, no script, no
  Lean change, no manuscript edit, no premise adopted, no claim promoted. Nothing committed, pushed or
  posted.
- **Authorization.** Owner amaybaum, 2026-11-12, #1169 comment 6831588323. The reviewer re-fetched it
  read-only (`REVIEW-OA-2.md`:7–10). It records the owner's question verbatim and authorizes a
  paper-only unit with "no computation, no Lean or manuscript changes, and no premise adoption".
- **Question (owner, verbatim).** "Can deterministic physical dynamics induce operations on
  emergent observer states that are genuinely richer than permutations of configurations, while
  still providing a common physical preparation and readout process?"

**Snapshots and citation forms.**

- `main` is now `615cc1190ec1bda69093be1eac49c839744008a5`, read with `git show origin/main:`.
  - Earlier pins: r1 at `fb733b4a58558ef64bd7c3585712c76e9f2dfb42`, r2 at
    `ec257beee0df9bb1c7b47900c97c42fb356563eb`.
  - `git diff --stat fb733b4a ec257bee` is empty on `papers/Main.md`, `verification/programmes/oi-qm/`
    and `verification/lean-mathlib/`.
  - `git diff --stat ec257bee 615cc119` on those paths only adds the TUNE-1 drafts under
    `reconstruction/drafts/tune-1-20261111/` (#1237). Every earlier citation still holds.
- `T1/n` = `verification/programmes/oi-qm/reconstruction/drafts/tune-1-20261111/TUNE-1-STEP2-SESSION3.md`
  at `615cc119`. It is a research draft [R].
- OA-1: branch `research/oa1-w1-1-20261112` at `066be3b1d321d1a325c3b0a577973102f7d0fbb7`. `OA1r4:n`
  means `.../oa-1-20261112/OA-1-REPORT-r4.md`. It is research only (§A.46 item 7).
- `Main:n` = `papers/Main.md`; `OB/File:n` = `verification/lean-mathlib/OIBridge/File`.
- `MECH-1:n` = `mechanism-1-20261107/DESIGN.md`; `MECH-2:n` = `mechanism-2-20261108/DESIGN.md`;
  `AP1:n` = `apparatus-1-20261107/DESIGN.md`; `obsmu:n` = `observer-interface-obsmu-20261104/ANALYSIS.md`.
  All four are relative to `verification/programmes/oi-qm/reconstruction/`.
- `Rev:n` = line `n` of `REVIEW-OA-2.md`; `Rev2:n` = line `n` of `REVIEW-OA-2-r2.md`.

**Support labels.**

| Label | Meaning |
|---|---|
| [K] | Lean statement on `main`; statement read, nothing built |
| [P] | Manuscript statement |
| [R] | Research record, not independently established |
| [W] | Derived here by hand; unreviewed |
| [RW] | Reviewer's hand derivation, re-derived here before use |
| [L] | Literature cited from memory, not read in this unit; context only, no verdict rests on it |
| [O] | Open |

**Disclosure.**

- **Commands.** `git fetch`, `git show`, `git diff --stat`, `git ls-tree`, `git grep`, `grep`, `sed`,
  `wc`, `cut`, `ls`, `cat -n`.
- **No script.** No script was written or run.
- **No copies.** No copy of any source was written at the working root in r2. r1's disclosure of a
  temporary copy and local ref, both removed, stands.

***

## 0. Plain-language summary

1. On laws over configurations, a bijection acts stochastically; its reversible actions are permutations (N0).
2. Hidden memory alone does not escape. The target-neutral emergent state is the operational class (N1).
3. On operational classes, escape needs equivalences coarser than ontic equality, on the side of
   preparations **or** of reads (N2.1). This is MECH-2's M-INACC rationale, here without a frame.
4. A designed reversible classical computer escapes exactly at every bounded horizon: its observer
   sees a contextual gbit (N2.3). At bounded horizons, G0, G1 and G3 do not separate classical from quantum.
5. At a fixed finite carrier, reversible emergent operations form a finite group, for every rule (N2.2).
6. **Affine class: NO** under (H3) no supplied control, (H4) nested records, H-AR cell-aligned observers,
   (xiv) and spanning. The prepare–measure theory is then classical. Otherwise it is narrowed, not closed (N2.4).
7. Under (H4), spanning and (xiv), G3 needs settings that do more than translate the joint held record,
   for any rule. This is compatible with OA-1's insufficiency statement. Non-affine rules: OPEN (N2.6).

***

## 1. Definitions, in OI's own terms

### 1.0 One physical setup and its procedures

`𝔖 = (S, φ, (V, H), μ, A)`, as in OA1r4:90–117:

- `S` finite (Main:60; ledger (ii), Main:724), or a finite-horizon window of a lattice;
- `φ` a bijection fixed before any target;
- `V ⊊ S` the observer, `H` the hidden sector (Main:42);
- `A` the apparatus layout, fixed once;
- `μ` is μ-O (per-orbit, derived, Main:54), μ-G (global counting, a posited selection, Main:54, :58)
  or μ-R (record-compatible maximal entropy, posited, ledger (iv), Main:724). The three are not
  interchangeable (OA1r4:236–270).

**Procedures `Proc(𝔖)`.**

- A protocol is a finite schedule of waiting under `φ`, of any duration. Its settings are cell
  contents, either initial or written by `φ` from records (feedback). It may include heralds
  (conditioning on held records) and discards.
- `Proc(𝔖)` is closed under sequential composition, so "prepare, wait `τ`, read" is a procedure for
  every `τ` (Rev:112–114).
- "Held" follows OA1r4:107–110: a function of the present configuration of `V`. The visible-history
  convention MP-0b is stated where it is used.

**Prepare-measure convention (C-PM) (F4).**

- A preparation procedure's own label cells are not effects on what it prepares. These are the
  setting and coin cells that select which preparation ran.
- Effects are all post-processings of held records **other than those label cells**. No read of the
  prepared configuration is removed.
- This is the standard identification of a preparation procedure [L: Spekkens, PRA 71, 052108 (2005)].
  It reconciles with "none removed by fiat" because the label is a property of the procedure, not of
  the system it prepared.
- **Physical form (C-PM′).** C-PM holds physically when the preparation gadget moves its label cells
  out of reach of every procedure within the horizon.
  - 𝔊_K below uses C-PM′ for its `p`, `ℓ` and bath-coin cells.
  - It still uses C-PM for the gadget-selector cells, and for the coin that selects between point
    preparations in an explicit mixture (N3).
  - Theorem E uses C-PM.

### 1.1 (a) Emergent observer states: three candidates

All three are laws, or classes of laws, on `S`. None posits a Hilbert space.

| | Definition | Measure |
|---|---|---|
| **E1** record law | The law of the present record class (visible configuration, or a coarse readout of it) | Its value depends on μ |
| **E2** posterior state | The conditional law of the full configuration given held records, under μ (Main:97; H-PREP reads it as a preparation, obsmu:893–901) | Its value depends on μ |
| **E3** operational class | `[p] := {p′ : e(p′) = e(p) for every available effect e}` (C-PM), for `p` a reachable E2-type law. `R(p) := (e(p))_e`, and `E := R(reachable)` | The definition is measure-free. The set `E` depends on μ through the reachable laws |

Notation for N2:

- `W := span(reachable laws)`;
- `U := ⋃ supp(reachable laws)`.

### 1.2 (b) Induced operation

For `π ∈ Proc(𝔖)`, the induced operation is `[p] ↦ [π(p)]` on E3. On E1 or E2 it is `p ↦ π(p)`,
where that map is well defined.

- **Trace-preserving** means no herald.
- **Heralded branches** are subnormalized and then renormalized.
- **Reversible on emergent states** means the map takes `E` onto `E` bijectively.

### 1.3 (c) "Genuinely richer than permutations": criteria

| Criterion | Content | Target-neutral? | Discriminates a reversible classical computer? (§3) |
|---|---|---|---|
| **G0** | Some induced operation is not induced by a configuration permutation | yes | **no** (noise, erasure) |
| **G1** | `E` is not a simplex | yes | **no** |
| **G2** | Exact reversible trace-preserving emergent operations of infinite order (e.g. dense control on a 2-level emergent system) | yes | **no**. It fails at every fixed finite `S` (N2.2). It passes with growing carriers (a classical rotor). Heralded injective maps of infinite order exist at fixed `S` (F9) |
| **G3** | The emergent theory has no noncontextual ontological model; equivalently, its accessible fragment is not simplex-embeddable [L: Spekkens, PRL 101, 020401 (2008); Schmid et al., PRX Quantum 2, 010331 (2021)] | yes | **no at bounded horizon**: 𝔊_K passes (N2.3). Unbounded horizons on a finite bijection are AW-OA2-2 (open) |
| **G4** | Phases, coherent mixing, dense `Fin 2` unitary control | **no**: presupposes an identification with operators | the configuration-level interface fails it [K] |
| **G5** | A quantum-specific fragment (OA1r4:479–486) | no (target-specific) | ε-versions pass with designed maps (Main:580); caught only by non-import |

**The kernel ceiling.**

- `NonnegBounded` (OB/FrozenSourcing.lean:65–67) is stated with `PreservesNonneg`
  (OB/SubstratumInterfaceAudit.lean:505–506).
- It entails no phases (:99), no dense `Fin 2` control (:173) and not `DerivedOI` (:111). The
  combined form is :327 [K].
- It concerns the configuration identification `obsTheory = permTheory Conf`
  (OB/SubstratumInterfaceAudit.lean:770–782). That is G4 at configuration level.
- G3 is its representation-invariant analogue for E3.

### 1.4 (d) Common physical preparation and readout

1. One `𝔖` for all settings: settings are cell contents, with no per-setting tables and no writes
   outside `φ`.
2. Closure: `Proc(𝔖)`, under C-PM, with no read of the prepared configuration omitted by fiat.
3. Admissibility: `φ` is from the corpus's rule class (gauge-derived affine, ledger (vii); R-lin
   (xiii), Main:724), or is a declared Layer-0 revision subject to §A.29.
4. Non-import (OA1r4:119–120).

Items 3–4 decide bearing on OI.

### 1.5 Observer restriction H-AR (F7)

**H-AR (additive readout).** The held record is an additive function of the configuration: a set of
cells read at full resolution, or MP-0b's history of such cells.

- It is a **named restriction on the class of observers**, not a technicality. Main's Definition
  requires only "finitely many distinguishable internal states" (Main:42).
- Site-region observers are suggested at Main:260 ("an observer-centered partition maps boundary
  visible sites to hidden") and at Main:650 ("spatially separated visible regions `V_A, V_B ⊂ V`").
- Main also uses an observation map with an induced coarse-graining `T` (Main:664).
- Main:82–92 (partition-relativity) does not fix cell alignment.
- A thresholded or detector-click readout is not additive.

***

## 2. Depth-first chain

### N0. Emergent state = law over configurations, or over record classes with a fixed lift

**Lemma 0 [W].** A protocol, conditioned on its settings and heralds, acts on `Δ(S)` as a nonnegative
matrix:

- `φ` acts as a permutation matrix;
- attaching cells in fixed laws is a tensor product;
- a discard is a marginal sum;
- a herald is a 0/1 diagonal;
- feedback is a record-indexed sum of these.

Without heralds the matrix is column-stochastic. This is MECH-2 Lemma F's proof without its frame
(MECH-2:333–344) [R], and it is the diagonal reading of the kernel invariant [K].

For a partition `κ` of `S` into record classes, the induced map on `Δ(κ)` is well defined **when**
the conditional law within each class at input (the lift) is fixed. A fixed lift is sufficient, not
necessary: strong lumpability, with `M(i|s)` constant on classes, also suffices (F9; §A.34). It is then
a stochastic matrix.

**Proposition A [W].** A linear map taking `Δ_n` onto itself bijectively permutes its vertices, so it
is a permutation matrix. ∎ This is Theorem C below with `E` a simplex.

**Verdict N0: NO, for this class.** Take E1 or E2, a fixed lift (or strong lumpability), every φ and
every μ. Trace-preserving induced operations are stochastic, and the reversible ones are permutations
of classes. G0 alone is passed, and G0 does not discriminate.

### N1. Option (ii): hidden memory makes the map not a function of the emergent state

Without a fixed lift (H-LIFT failing, MECH-2:319–321, :346–347), the coarse law's future depends on
the hidden conditional law. The "operation" is then a family of stochastic matrices indexed by the
lift, not a map on E1.

**Lemma 1 (closure) [W].** On E3, every `π ∈ Proc(𝔖)` induces a well-defined linear map `π_E`.

*Proof.* Suppose `p ∼ p′`. For every available `e`, the composite `e ∘ π` is available (closure,
under C-PM). So `e(πp) = (e∘π)(p) = (e∘π)(p′) = e(πp′)`. ∎

**Verdict N1: not an independent escape.** Hidden memory makes maps on cruder spaces ill-defined.
Refined to E3, it reappears as the shape of the quotient `R` (N2). Each lift-indexed branch is
stochastic (Lemma 0).

### N2. Option (i): emergent state = operational class (E3)

#### N2.1 What the ceiling needs: preparation **and** effect equivalences equal to ontic equalities (F1)

**Proposition B (corrected; [RW] re-derived here) [W].** Let `R` be injective on `W`.

- **(i) Preparation noncontextuality.** The substratum's configuration model is
  preparation-noncontextual: `p` is a function of `[p]`.
- **(ii) Measurement noncontextuality.** The model is measurement-noncontextual **iff** the
  restriction map `ρ : span(available effects, as functions on U) → W*` is injective. A sufficient
  condition is `W = ℝ^U`; this is Theorem NC's actual hypothesis, that the states span (MECH-2:489,
  :506).
- **(iii) Transformation noncontextuality.** The model is transformation-noncontextual when each `π`
  is fixed on `ℝ^U` by its operational action. "`π|_W` fixed by `π_E`" does not give this
  (Rev:82–83).
- **(iv) Simplex embedding.** When (i)–(iii) hold, the configuration model is a simplex embedding of
  the fragment.

*Proof of (ii).*

- (⇐) If `ρ` is injective, two operationally equivalent effects have equal response functions on `U`.
- (⇐) In detail: two available effects that agree on `W` have a difference in the effect span that
  vanishes on `W`. By injectivity of `ρ` that difference vanishes on `U`, so the two response
  functions are equal on `U`.
- (⇒) Proved in general [RW, re-derived here] (N1).
  1. Suppose `ρ` is not injective. Then some `d = Σ_i c_i e_i`, with available effects `e_i` taken as
     functions on `U`, vanishes on `W` and is nonzero on `U`.
  2. Split by sign: `P = {i : c_i > 0}` and `N = {i : c_i < 0}`. Then
     `Σ_P c_i e_i = Σ_N |c_i| e_i` on `W`.
  3. Let `λ := max(Σ_P c_i, Σ_N |c_i|)`. It is positive, since `d ≠ 0`.
  4. Define, with `0` the null effect (an outcome never registered, which is available by
     post-processing):
     - `A := Σ_P (c_i/λ) e_i + (1 − Σ_P c_i/λ)·0`;
     - `B := Σ_N (|c_i|/λ) e_i + (1 − Σ_N |c_i|/λ)·0`.

     Both are convex mixtures of available effects, so both are available effects with responses in
     `[0, 1]`.
  5. `A = B` on `W`, which contains every reachable law, so `A` and `B` are operationally
     equivalent.
  6. Their ontic response functions differ, because `A − B = d/λ ≠ 0` on `U`.
  7. In the configuration model the response of a mixture is the mixture of the responses. So that
     model gives two operationally equivalent effects different responses: it is
     measurement-contextual. ∎
- **What (⇒) does not give.** It is a statement about the configuration model only. A non-injective
  `ρ` does not imply that the fragment fails to be simplex-embeddable, since another model may
  exist. The G3 claim therefore rests on the counterexample below, separately (Rev2:51–53).

**Counterexample to r1's version [RW, re-derived by hand here].**

1. *Setup.*
   - Ontic space: `(x, y) ∈ F₂²`.
   - Reachable laws: all laws with `P(x = y) = ½`. So `W = {w : w₀₀ + w₁₁ = w₀₁ + w₁₀}`, of
     dimension 3, and `U = F₂²`.
   - `Δ ∩ W` is the square with vertices `σ_{x0} = ½[00]+½[01]`, `σ_{x1}`, `σ_{y0}`, `σ_{y1}`.
   - Effects: every classical read of `(x, y)`. `R` is injective on `W`.
2. *Equivalences on `W`.* `w₀₀ = ½X0 + ½Y0 − ¼`, checked on all four vertices. Then
   `w₁₀ = ½Y0 − ½X0 + ¼` and `w₁₁ = ¾ − ½X0 − ½Y0`.
3. *Pinning `ξ_{Y0}` on the `x`-supports.*
   - On `supp μ_{x0}` we have `ξ_{X0} = 1`.
   - `ξ_{E10} ≥ 0` then gives `ξ_{Y0} ≥ ½`, and `ξ_{E11} ≥ 0` gives `ξ_{Y0} ≤ ½`.
   - The same holds on `supp μ_{x1}`.
4. *Contradiction.* Preparation noncontextuality gives `μ_{y0} + μ_{y1} = μ_{x0} + μ_{x1}`, since both
   sides are the uniform law with mass 2. So `ξ_{Y0} = ½` holds `μ_{y0}`-a.e., which contradicts
   `Y0(σ_{y0}) = 1`.
5. *Conclusion.* The fragment is measurement-contextual, so G3 holds, with `R` injective. Its
   accessible fragment is the gbit square with its four facet effects, as in N2.3: the gbit's dual
   form, with reads complete and preparations restricted.

**Corollary B′ (corrected; CONFIRMING).**

- G3 requires the configuration model's **preparation equivalences or its effect equivalences** to be
  coarser than ontic equality.
- This is MECH-2's M-INACC rationale, "a contextual observer-level theory needs operational
  equivalences coarser than ontic equalities" (MECH-2:842), stated here without a frame. MECH-2:521–529
  gives the read-restriction instance (the gbit) and its caveat: "not a nonclassicality witness unless
  the missing reads are absent for a physical reason".
- Not sufficient: a decoupled hidden coin makes `R` non-injective while the fragment stays a simplex.
- Whether closure excludes the dual (preparation-restriction) route is not shown in general. A
  designed read that records `(x, y)` and then re-randomizes the parity keeps reachable laws in `W`
  (Rev:71–74).

#### N2.2 Fixed finite carriers: reversible emergent control is always finite

**Theorem C [W; step 3 patched per F8].** Fix finite `S`, any φ, μ and interface. Let `π` be
trace-preserving with `π_E(E) = E`. Then `π_E` is an affine automorphism of the polytope
`P_W := R(Δ(S) ∩ W)`, and all such `π_E` lie in a finite group of vertex permutations of `P_W`. Under
H-SPAN (`W = ℝ^S`), the vertices are among the configuration images `R(δ_s)`.

*Proof.*

1. Reachable laws are closed under `Proc`, so `π(W) ⊆ W`. Hence `π_E(P_W) = R(π(Δ ∩ W)) ⊆ P_W`.
2. `aff(E) = R(W ∩ {mass 1})`. Write `K := cl conv(E)`. Then `K ⊆ P_W ⊆ aff(E)`, and `K` is a convex body
   in `aff(E)`.
3. `π_E` is affine and `π_E(E) = E`, so `π_E(conv E) = conv E`, and by continuity `π_E(K) = K`. `K` has
   nonempty relative interior and positive volume in `aff(E)`. So `π_E` is invertible on `aff(E)` and
   `|det π_E| = 1`. (r1 argued this on `E` itself, which need not be convex and may be finite.)
4. `π_E(P_W)` is a closed convex subset of `P_W` of equal volume, so `π_E(P_W) = P_W`.
5. Affine automorphisms of a polytope permute its vertices and are fixed by that permutation, so they
   form a finite group. Inverses are powers, hence induced. ∎

**Consequences and prior art (F8).**

- **G2 fails at every fixed finite `S`,** for every rule and interface. A setting-selected rotation at
  `cos θ = 3/5` has infinite order: `(3+4i)/5` has minimal polynomial `5x² − 6x + 5`, so it is not an
  algebraic integer. Exact T-C (OA1r4:484) therefore needs growing carriers.
- **In-corpus prior art.** AP1 §5.3 (AP1:955–979) already derives in-corpus, with no import, that "no
  finite carrier induces `rot` with exact statistics". It uses Perron–Frobenius power-boundedness and
  Niven's theorem, for any stochastic matrix on a finite ontic set. Theorem C is an operations-level,
  every-interface companion to it. OA-1's R7 framing ("half imported", via Main:558) is superseded by
  AP1 §5.3 for `rot`, not by Theorem C.
- **Main:558** concerns prepare-and-measure behaviours (nonnegative rank), not operations. Theorem C
  is an operations analogue, not a replacement for it.
- **Literature.** Finiteness of the reversible transformation group of a polytopic state space is
  standard in the GPT literature [L: e.g. Gross, Müller, Colbeck, Dahlsten, PRL 104, 080402 (2010)].
- **Confirming instance.** op-quotient v3: rotations preserve the sign cube, giving 24 Cliffords
  (`states-dynamics-audit-20261024/operational-quotient-v3/REPORT.md`:17–24) [R].

**Scope (F9).**

- *Heralds.* Renormalized branches `p ↦ Dp/|Dp|` with `D` a positive diagonal (a Bayesian likelihood
  filter) are injective maps of infinite order at fixed `S`. Finitely many likelihood vectors per
  protocol generate a countable family. Such maps are reversible on `E` when the inverse likelihoods
  are reachable. So G2 for heralded maps is non-discriminating (classical Bayesian).
- *Growing carriers.* A rotor discretized to `N` points, with response `(1 + cos(λ − α))/2`, has `E` an
  `N`-gon, and its rotations by `2π/N` become dense in `SO(2)`. G2 tests carrier growth, not
  quantumness.

**Verdict N2.2:** NO for exact infinite-order trace-preserving reversible control at fixed finite `S`.
ELABORATING.

#### N2.3 Existence: a designed reversible classical computer passes G3 exactly, per horizon

**Universe `𝔊_K` [W; repaired per F4].**

- **Cells.**
  - In `H`: the carrier `(x, y) ∈ F₂²`; a bath conveyor `b_1 … b_{M_b}` of uniform independent bits;
    and a ready conveyor `z_1 … z_{M_r}` of known-0 cells.
  - In `V`: setting cells, and record cells that start blank. The record cells use MP-0a
    (OA1r4:547–552) or MP-0b.
- **Initial law.** Ready cells and blanks are declared in the joint initial law, as MP-0a. The bath is
  uniform: native under μ-G (Main:58), not established under μ-O or μ-R.
- **Conveyors.** `ROT_b` and `ROT_r` cyclically shift the bath and ready conveyors by one position.
  Gadgets work on a window at the front of each conveyor: bath position 1, and ready positions 1–4.
  The horizon bounds below are justified by a window argument (N3).
- **One fixed bijection `Φ`.** It applies a gadget selected by setting cells. A controlled bijection is
  a bijection.

| Gadget | Action (each step a bijection) | Bath shifts | Ready shifts |
|---|---|---|---|
| **PREP(p_x, p_y)** | 1. swap `(x, y) ↔ (z_1, z_2)`, so the carrier is `(0, 0)`<br>2. `x ⊕= p_x`, `y ⊕= p_y`<br>3. swap `(p_x, p_y) ↔ (z_3, z_4)`, which moves the label out of reach and resets the setting cells<br>4. `ROT_r⁴` | 0 | 4 |
| **PREP(ℓ)**, `ℓ ∈ {A = 0, B = 1}` | 1. swap `(x, y) ↔ (z_1, z_2)`<br>2. `x ⊕= b_1`, `y ⊕= b_1`, `y ⊕= ℓ`<br>3. swap `ℓ ↔ z_3`<br>4. `ROT_b`, `ROT_r³` | 1 | 3 |
| **FLIP(f)** | `x ⊕= f` | 0 | 0 |
| **SWAP(w)** | Fredkin: if `w = 1`, `x ↔ y` | 0 | 0 |
| **MEAS(m)** | if `m = 0`: `r ⊕= x` into the next blank, then `y ↔ b_1`, then `ROT_b`; for `m = 1`, the same with `x` and `y` exchanged | 1 | 0 |

- **Coupling.** No other coupling joins `V` to the carrier or to either conveyor.
- **Horizon `K` and resources (N3).** At most `K` gadgets per protocol, with three resource bounds:
  `M_b > K`, `M_r > 4K`, and at least `K` blank record cells (one per MEAS).
  - *Bath.* A gadget leaves its used bath cell at position `M_b`. To re-enter the window at position 1
    it needs `M_b − 1` further shifts. At most `K − 1` gadgets follow, each shifting at most once, and
    `K − 1 < M_b − 1`.
  - *Ready conveyor.* After a PREP its used cells sit at positions `M_r − 3 … M_r`, or `M_r − 2 … M_r`
    for PREP(ℓ).
    - The earliest of these reaches the window (positions 1–4) only after `M_r − 7` further shifts.
      Cells taken from positions 2–4 pass through position 1 inside the PREP's own `ROT_r⁴`; that is
      within the gadget, not a re-entry.
    - At most `K − 2` intermediate PREPs come before any later PREP starts, shifting at most `4(K − 2)`
      in total.
    - `4(K − 2) < M_r − 7` holds whenever `M_r ≥ 4K`. Supplying fresh known-0 cells to up to `K` PREPs
      needs `M_r ≥ 4K` as well.
    - So `M_r > 4K` suffices (Rev2:117–127).
- **Rotation repair (F4).** After `PREP(ℓ)`, the coin `b_1` has moved to position `M_b`. The next MEAS
  uses a fresh bit. This repairs r1's gap: "no gadget rotates the bath except MEAS" (Rev:191–193).

**Claim 1 (exact operational equivalence) [W].** PREP(A) and PREP(B) use the same gadget-selector
cells, so the held selector does not distinguish them. The `ℓ` and coin cells are out of reach, so
C-PM′ is physical for this claim (Rev2:135). Let `P_A` and `P_B` be the
laws prepared by PREP(A) and PREP(B). These are `½[00] + ½[11]` and `½[01] + ½[10]` on the carrier.
Then `P_A ∼ P_B` under every procedure in `Proc(𝔊_K)`.

1. **After preparation.** No held cell depends on the carrier or on `ℓ`: the label and coin are out of
   reach, and the old carrier contents went to the ready conveyor. Feedback cannot depend on the
   carrier.
2. **FLIP and SWAP** map `{P_A, P_B}` to itself.
3. **First MEAS (`m = 0`).**
   - The record is `x`, uniform.
   - The carrier becomes `(x, b_fresh)`, with `b_fresh` uniform and independent.
   - The old `y` is at the bath's end.
   - So the joint law of everything in reach is the same under A and B. The reviewer re-derived this
     step (Rev:185–187).
   - `m = 1` is symmetric.
4. **Afterwards.** The two cases differ only in out-of-reach cells, which do not return within `K`
   gadgets. ∎

**Claim 2 (preparation contextuality) [W].** No preparation-noncontextual ontological model reproduces
`𝔊_K`.

1. The point preparations `[ab]` are reachable through PREP(a, b), and the reads `X` and `Y` are sharp on them.
2. Any response functions satisfy `ξ_{X0} = 1 − a` and `ξ_{Y0} = 1 − b` holding `μ_{ab}`-a.e. So the four
   supports are pairwise disjoint.
3. PREP(A) is operationally equivalent to the coin mixture of PREP(0,0) and PREP(1,1). Both give
   `½[00] + ½[11]` with the `p`, `ℓ` and bath-coin cells out of reach. Similarly for B.
   - **This step uses C-PM, not only C-PM′ (N3).** The two procedures use different gadget-selector
     cells, which stay held. The mixture's selecting coin may also stay held unless it is placed in
     the `p` cells.
   - The convention excludes the selector and coin cells as labels of the preparation procedure.
   - Alternatively, a PREP variant that also swaps its selector and coin cells into the ready conveyor
     makes it physical, with the ready count raised accordingly. Either way the verdict is unchanged.
4. Convex-linearity and preparation noncontextuality give `½(μ₀₀+μ₁₁) = μ_A = μ_B = ½(μ₀₁+μ₁₀)`. The
   two sides are supported on disjoint sets. ∎

**Prior art (F9).**

- Claim 2 is the maximal violation of AP1 Lemma 4′'s preparation-noncontextuality bound for one
  4-point cell (AP1:698–712; average signed `P + V` at most 1).
- AP1's scope note (AP1:714–729) and MECH-2:521–529 explain why a `Z`/`X`-only violation is
  artefactual. The reads are omitted, not physically absent.
- In `𝔊_K` the joint read is physically absent within the horizon, and the equivalence holds under
  every procedure. `𝔊_K` is therefore a designed classical, per-horizon instance of M-INACC (a)–(c)
  (MECH-2:834–840). Known literature pattern [L: Selby et al., PRL 130, 230201 (2023);
  Kochen–Specker 1967].

**Status per criterion.**

- G0 passes: MEAS-and-discard is `(p, q) ↦ (p, ½)`.
- G1 and G3 pass exactly at horizon `K`.
- G2 fails: the reversible operations are the order-8 dihedral group (Theorem C).
- G4 and G5 fail: a gbit is not a qubit.

**Pressure tests.**

- *Recurrence.* Exactness holds per horizon, with `M_b > K` and `M_r > 4K`. Unbounded protocols on a
  finite `S` are AW-OA2-2, open.
- *Leaks.* Every gadget that touches labels or old carrier contents sends them out of reach.
- *Admissibility and non-import.* `Φ` is designed and non-affine, so it fails (d)3–4 by construction.
  It is a control, not an OI result.
- *Quantum analogue.* Main's gluing (Main:564–582 [P]) gives ε-quantum E3 states with imported data:
  "Quantum mechanics enters as the instrument data and as the state held in the hidden register"
  (Main:580). It satisfies Corollary B′ on the preparation side: register mixtures are equivalent to
  the mixed register.

**Verdict N2.3: YES at every bounded horizon, for deterministic reversible dynamics in general.** It
does not discriminate: the richness sits in a designed access structure.

#### N2.4 OI's native rule class: the affine collapse (reclassified ELABORATING; F2, F3, F5, F7)

**Hypotheses.**

| Label | Content |
|---|---|
| **(H1)** | `Φ(ω) = Aω + k`, with `A` an additive bijection of a finite abelian configuration group: the gauge-derived affine class, ledger (vii), Main:724. R-lin is included. A lattice is taken on a finite-horizon window |
| **(H-AR)** | §1.5, a named observer restriction |
| **(H3)** | Fixed layout. No supplied per-tick or per-edge control (P3, E-iso). Durations are part of `Proc` (closure) and are not excluded |
| **(H4) nested records (F2)** | Within the horizon, the held record at the latest read determines every earlier available read. Example: MP-0b with the history retained. Retention is open on `main` ("O-RET, O-REC and O-ACC, all open", obsmu:917) |
| **(xiv)** | Main:724 |
| **(SP) spanning** | Defined in (b) below |

**Prior results this builds on (F5).**

- MECH-1 Lemma A (i)–(iii) (MECH-1:404–418): under one fixed affine rule, every slot is
  `ℓ(x) + β·c + const`. The registered functional does not depend on `c`. The setting changes branches
  only by translations and relabelling.
- MECH-1 Corollary A′ (MECH-1:424–425): "Choosing afterwards which record to consult does not escape
  Lemma A. The physical joint law of all records does not depend on the setting."
- OA-1 D5 (OA1r4:172–190) and D7 (OA1r4:198–204): "every 'selectable' read is a coarse-graining of one
  joint record".
- obsmu Proposition C (obsmu:546–578): coset structure of homomorphic-readout record laws under the
  uniform measure.
- TUNE-1 Lemma A-T (T1:56–98) [R], a research draft on `main` at `615cc119` (N7). It re-derives
  Lemma A for every `q ≥ 2`, for R-lin's second-order rule and for exchange mode. It gives
  coset-uniform record laws and the 0-or-1 dichotomy in total variation. It is prior art for
  Theorem E's coset structure. No verdict depends on it.

**Theorem E [W; ELABORATING of the above].** Write `ω₀ = (σ, c, α)` for carrier, measurement settings
and rest, and use C-PM.

- **(a) Measure-free; MECH-1 Lemma A restated.** Assume (H1) and H-AR. For every protocol, each held
  record is `Z_τ = H_σ^τ σ + H_c^τ c + H_α^τ α + k_τ`, with the `H^τ` fixed homomorphisms independent of
  `c`. Settings act only by translation.
- **(b) E3-level classical model of the prepare–measure fragment.** Assume (H1), H-AR, (H3), (H4) and (xiv).
  1. By (H4), every available effect is a post-processing of the one joint record
     `Z = (Z_τ)_{τ ≤ T}` held at the latest read. This is Corollary A′ and D7 at the E3 level.
  2. Let `Λ` be the set of values of `Z₀ := Z − H_c c`.
  3. The model `ι(s) = law of Z₀ under s`, with response `λ ↦ f(λ + H_c c)` for the effect `(c, f)`,
     reproduces every statistic.
  4. It is preparation-noncontextual, because singleton indicators are available.
  5. Under **(SP)** — the reachable laws of `Z₀` span `ℝ^{U_Z}`, where `U_Z` is the union of their
     supports — the model is also measurement-noncontextual, by Proposition B(ii) (⇐) applied to the
     `Z₀` model. It is then a simplex embedding of the prepare–measure fragment, so G3 fails.
     - **G3 here is the prepare–measure criterion** (N2). Every procedure is folded into a
       preparation, or into a measurement "procedure, then read" [L: Schmid et al. 2021].
     - Transformation noncontextuality of the `Z₀` model, in the sense of Proposition B(iii), is not
       claimed: r2's "and transformation-" is withdrawn.
  6. Without (SP), only preparation noncontextuality is shown. The counterexample of N2.1 is a
     single-`Z` readout with every singleton indicator available and non-spanning reachable laws, and
     it is measurement-contextual.
- **(c) Induced operations.** Assume (H1) and H-AR, and **H-LIFT**: a fixed conditional law of `α`
  given `σ` (MECH-2:319–321) (F9). On carrier laws, setting `c` induces one fixed stochastic map (the
  pushforward of `σ ↦ A_σσσ + A_σαα + k`) followed by the translation `A_σc c`, which is a permutation of
  configurations. Without H-LIFT, the measure-free statement (a) still holds.

**Verdict N2.4 (F3, F6, F7).**

- **NO, with every condition stated.** Under (H1), H-AR, (H3), (H4), (xiv) and (SP), the emergent
  prepare–measure fragment is simplex-embeddable (fails G3), at every carrier size. Under H-LIFT, its settable operations are
  translations composed with one fixed noise map. It can still pass G0 and G1, which do not
  discriminate.
- **Narrowed, not closed, otherwise.** Without (H4) or (SP), classicality of the affine class at E3 is
  not established.
- **Ruled-out class:** affine rule, additive (cell-aligned) observer, nested records, spanning
  reachable record laws, and measurement independence. The verdict says nothing about non-affine
  rules, supplied P3/E-iso, non-additive observers, non-nested reads or non-spanning preparations.

**The non-nested case is a gap, not a refutation (F2).**

- **Reads at all durations are native.** `Proc` contains "prepare, wait `τ`, read" for every `τ`. Under
  the default "held = present `V`", `Z_τ` and `Z_τ′` are generally not jointly held.
- **What (b) then needs.** It needs the joint law of `(Z₀^{(τ)})_τ`, and only the marginals are
  available statistics.
- **Why the gbit ingredient is not excluded** (MECH-2:523; Rev:124–132). A pre-reference herald could
  read `ℓ₁ + ℓ₂` while post-reference reads within the horizon read `ℓ₁` and `ℓ₂` separately, never
  jointly. (H1)–(H3) do not exclude this per-horizon asymmetry.
- **Not shown either way.** Neither a proof for non-nested multi-time families nor a counterexample
  that also meets C-PM is given here. This is marker AW-OA2-4.
- **(H3) consistency.** r1's (H3) excluded "timing selection" and so conflicted with closure, on which
  Lemma 1 and Theorem C rely (Rev:134–137). (H3) now excludes only supplied control. Multi-time reads
  are native and are handled by (H4) or by this gap.

**Corollary E1 (restated as the contrapositive of E(b); F6, N4) [W].**

- **Generalized form of E(b) (N4).** The proof of (b) uses only three things:
  - (H4): one joint held record `Z`;
  - every measurement setting acts on it by translation, `Z = Z₀(ω) + h(c)` with `Z₀` independent of
    `c`;
  - (SP) and (xiv).

  So for **any rule, affine or not**, and any observer: if settings translate the joint held record,
  and (H4), (SP) and (xiv) hold, then the prepare–measure fragment is simplex-embeddable.
- **Statement (the contrapositive).** Within E3, G3 read as the prepare–measure criterion, keep (H4),
  (SP) and (xiv). Then a G3 escape requires settings that do **not** merely translate the joint held
  record.
  - For the gauge-derived affine class under H-AR, (H1) and (H3) give translation (Theorem E(a)). An
    escape therefore requires leaving (H1) ∧ (H3): through MP-1 (OA1r4:556–572), a non-affine rule, or
    through supplied P3/E-iso.
  - r2's wording ("under (H1), …, (H3) a G3 escape needs …") was vacuous: under (H1) and (H3) there is no
    non-translational dependence at all (Rev2:160–170).
- **Failure of (xiv).** It gives preparation correlation, not control (OA1r4:198–204, D7).
- **Relation to OA-1.** This is a necessity statement, compatible with OA-1's insufficiency statement
  (OA1r4:515: dropping A5 "does not by itself bear on gap 3"; D6 at configuration level).
- **Scope of "gap 3".** It does not say the gap-2 repair is necessary for OA-1's gap 3 outright. That
  gap is the broader "sourced operation beyond the configuration-level ceiling".
- **Open exits that need no non-translational setting dependence.**
  - non-additive observers (AW-OA2-1);
  - non-nested multi-time reads (AW-OA2-4);
  - non-spanning reachable laws (N2.1's dual route).

**Corollary E2 (`q = 2`, parity outcomes, (xiv)) [W; confirmed by the reviewer, Rev:322–327].**

- **Result.** Under (H1) and H-AR, `E(a, b) = K s(a) t(b)` with `s, t = ±1`, so `|CHSH| ≤ 2|K| ≤ 2`. This
  holds with additive remote-setting dependence and no spatial separation.
- **Relation to Main:414.** It **complements** Main:414's Bell–lattice corollary: it trades the
  graph-cone locality hypothesis for parity outcomes and the affine class.
- **Counterexample beyond scope.** For `q > 2` with a `±1` coarse-graining, H-AR fails. Over `Z₄` with
  `g(0) = g(1) = 0`, `g(2) = 1` one gets `B = ab` and CHSH = 4, which signals.
- No manuscript edit is proposed.

**Pressure tests on Theorem E.**

1. **Routing by setting.** Routing a carrier to one of two apparatuses by a setting is a controlled swap,
   which is non-affine. Placement at preparation time is a preparation label, excluded under C-PM.
2. **Time (rewritten; F2).** Reads at different durations are native. With (H4) they are
   coarse-grainings of the latest held record, and (b) applies. Without (H4) they are a non-nested
   family, which is the gap above. Selecting a duration by a setting, rather than by protocol length,
   needs conditional copying, which is non-affine (D7).
3. **Infinite lattices.** A finite cone at a finite horizon (Main:364) leaves a finite window.
4. **Heralds.** These are conditionings on components of `Z`, so they act as preparation labels.
5. **Non-additive observers (AW-OA2-1).**
   - With a readout `g(Z + c)` for non-additive `g`, two shifts give compatible reads whose joint
     need not be available: the gbit pattern.
   - The exit closes when two copies of the same functional with known shifts are available.
   - H-AR is a named observer restriction (§1.5), not a consequence of Main.
6. **Encoded subtheories** (QA's `U′`, P-8, op-quotient v3) restrict reads by an identification. They
   are 5c/5d with supplied access, outside E3.

#### N2.5 Affine rule with supplied control (P1–P3, E-iso)

- **Prior results [R].**
  - With P3, `Z`/`X` reads are selectable. Under H-LIFT with spanning reads, Theorem NC applies
    (MECH-2:485–507; mathcon1 `DESIGN.md`:597–627).
  - At odd `q`, MECH-1 Proposition C(d) places the reachable class inside the epistricted theory,
    which is a noncontextual model (MECH-1:763–766).
  - At `q = 2`, every ontological model of the full single-qubit stabilizer subtheory is contextual
    (LWE Theorem 1, as read in MECH-1:788–789). The `Y` read and `Y` states are what is missing
    natively (MECH-2:530–537).
- **Single cell, native `Z`/`X` reads only, class N: noncontextual, conditional [W on R; re-derived
  per F1].**
  - *Premises.*
    - H-LIFT.
    - The reachable carrier laws are the uniform, `z`-pair and `x`-pair laws and their mixtures.
    - Point laws and `(z+x)`-determined laws are excluded by Lemma Q(iii) under P1–P2 and by AP1's
      type grading (MECH-2:530–534; minacc-1 `RESULT.md`:118).
  - *The algebra, at general `q` (N6).*
    - Read "`z`-pair" and "`x`-pair" as the `z`-level and `x`-level laws: uniform on
      `{z = a}` and on `{x = b}` in `F_q²`, with `U = F_q²`. At `q = 2` these are the four pair laws.
    - *Effect side [RW].* The span of the available effects is `{f(z) + g(x)}`, of dimension `2q − 1`.
      Suppose `f(z) + g(x)` vanishes on every level law. Then `f(a) + mean(g) = 0` for all `a`, and
      `mean(f) + g(b) = 0` for all `b`. So `f` and `g` are constants summing to zero, and
      `f(z) + g(x) ≡ 0` on `F_q²`. The restriction `ρ` is injective.
    - *Preparation side [RW].* `W` is spanned by the `q` row and `q` column indicators of `F_q²`, with
      the single relation `Σ rows = Σ columns`, so `dim W = 2q − 1`. `ρ` is an injective linear map
      between spaces of equal dimension `2q − 1`, so it is bijective and the pairing between `W` and
      the effect span is nondegenerate. Hence `R` is injective on `W`. At `q = 2` this is the hand check
      of `(1, ⟨Z⟩, ⟨X⟩)` on the four points.
  - *Premises by `q`.*
    - The reachable-law premises (Lemma Q(iii), the type grading) are established in their [R]
      sources at `q = 2` only.
    - At odd `q`, MECH-1 Proposition C(d) (MECH-1:763–766) independently places the reachable class
      in the noncontextual epistricted theory.
    - So the conclusion is stated at `q = 2` on these premises, and at odd `q` on MECH-1's. The algebra
      above holds for every `q`.
  - *Conclusion.* The prepare–measure fragment is preparation- and measurement-noncontextual. r1's
    reason ("effects span `W*`") was insufficient. The conclusion survives on this reason.
  - *Scope.* This narrows OA-1 R6's "undecided" (OA1r4:439–441) for class N at one cell. It stays
    undecided for `G_SM` (P★ reachable) and for multi-cell product reads.

#### N2.6 Admissible non-affine rules: open

Candidates: `G_SM` at `q = 2` (MECH-2:37–47) and `G_σ` (minacc-1). Each is a Layer-0 revision of
ledger (vii) and A5 (Main:724), under §A.29.

| Necessary condition | Source | Status for `G_SM` |
|---|---|---|
| N-a. Non-translational setting dependence of reads, needed under E1's conditions | Theorem E | met: "the selection is ontically in-world" (MECH-2:102–103) [R] |
| N-b. Preparation **or** effect equivalences coarser than ontic, used non-trivially, under the full closure | Corollary B′ | not shown, by either route |
| N-c. Growing carriers, for exact infinite-order reversible control | Theorem C, AP1 §5.3 | — |

**Skeptical reading of the evidence.**

- P★'s labels (MECH-2:80–91) are relative to the frame R1. That is G4-type, so they count for nothing
  either way in E3.
- Under `G_σ`, the gate cancellation determines `u + v` without backaction
  (`minacc-1-20261108/RESULT.md`:44–63). More access pushes toward injectivity on the read side.
- ARP-1-MARC concerns `N₁` in a finite model with supplied registration
  (`round-arp1-marc-20261108/result.md`:36–38) [R].

**Verdict N2.6: OPEN.**

### N3. Option (iii): other state spaces

- **5c, encoded frames.** These posit an operator identification (G4-type). Within their hypotheses,
  Lemma F, U2 and NC constrain them (mathcon1 :597–627 [R]). A non-injective identification that
  restricts reads (`U′`) is a supplied form of N2.3's mechanism.
- **5e, amplitude spaces.** Imported (OA1r4:422; `oi-qm-ext-1/two-mode-drive.md`:25–40 [R]).
  Koopman–von Neumann makes G2/G4-style tests non-discriminating.
- **5f, infinite lattice.** Not sufficient (OB/QuasilocalCharacterization.lean:792 [K]). Growth is
  necessary for exact G2 (Theorem C; AP1 §5.3).

**Verdict N3:** no target-neutral escape beyond N2.

***

## 3. Controls

### 3.1 Classical control

| Criterion | Affine classical computer (linear CA) | Fredkin/Toffoli computer, full-access interface | Fredkin/Toffoli computer, its physically restricted interface (`𝔊_K`) | Discriminating? |
|---|---|---|---|---|
| G0 | pass | pass | pass | **no** |
| G1 | can pass (restricted reachable laws) | fail (simplex) | pass (square) | **no** |
| G2, fixed `S` | fail | fail | fail (Theorem C) | — |
| G2, growing carriers | translations only (Theorem E(c)) | — | classical rotor passes | **no** |
| G3 | **fails under (H4), H-AR, (SP), (xiv)** (Theorem E(b)); otherwise not established | fail: Proposition B with `W = ℝ^U` (full access makes every point law reachable). Context only [K]: OB/CentralObservation.lean:620 (passive instruments on matrix algebras) | **pass at horizon `K`** (Claim 2) | discriminates access structures at bounded horizon, **not** classical from quantum dynamics |
| G4 (configuration identification) | fail [K] | fail [K] | fail [K] | not target-neutral |
| G5 (ε) | — | — | the gluing map passes (Main:580); fails non-import (Main:582) | only via (d)3–4 |

**Reading.**

- At bounded horizons, no target-neutral single-system criterion separates a reversible classical
  computer from a quantum-like one, because `φ` can be designed to supply the access restriction.
- MECH-2:521–529 anticipates this for omitted reads. `𝔊_K` shows it also holds when the joint read is
  physically absent.
- This extends OA1r4:466–470 ("the qubit tier tests sourcing, not quantumness") to G1–G3 [W].
- Whether any G3 success survives unbounded protocols on a finite bijection is AW-OA2-2.
- The decisive question for OI is sourcing, items (d)3–4.

### 3.2 Target-neutrality

- E1–E3, C-PM, Lemma 1, Propositions A and B, Theorem C, Theorem E and G0–G3 use only laws on `S`,
  `[0, 1]` responses and convex structure. They use no Hilbert space, amplitude or frame.
- G4 and G5 only locate the kernel ceiling and the target.
- **Countercheck.** An operator identification (5c) would make "richer" frame-relative (P★). That is
  avoided here.

### 3.3 Measure dependence

| Result | μ-G | μ-R | μ-O |
|---|---|---|---|
| Lemma 0, Proposition A, Lemma 1, Propositions B and C | hold (statements about every law) | hold | hold |
| `𝔊_K` (uniform bath) | holds | not established | not established |
| Theorem E(a) | holds (measure-free) | holds | holds |
| Theorem E(b) | needs (xiv): holds for disjoint setting cells | (xiv) may fail on the support | (xiv) may fail on the orbit (OA1r4 §2A) |
| Theorem E(c) | needs H-LIFT | needs H-LIFT | needs H-LIFT |
| Corollary E2 | needs (xiv) | needs (xiv) | needs (xiv) |
| Class N single cell | as in its [R] sources (uniform law in (s5)) | not established | not established |

***

## 4. Conclusion

| Reading of the question | Verdict | Exact scope |
|---|---|---|
| Deterministic dynamics in general, E3 states, (d)1–2 only | **YES, per bounded horizon** | `𝔊_K`: exact G1 and G3 at every horizon `K`. Its typed premises are listed below the table. Main's gluing gives ε-G5 with imported data [P]. **Non-discriminating** |
| E1 or E2 with a fixed lift (or strong lumpability), any rule, any μ | **NO** | Lemma 0, Proposition A |
| Exact infinite-order trace-preserving reversible emergent control at fixed finite `S` | **NO** | Theorem C; for `rot`, also AP1 §5.3 |
| Gauge-derived affine class (OI's native rule) | **NO for the prepare–measure fragment under (H1), H-AR (cell-aligned observers), (H3), (H4) nested records, (SP) and (xiv); otherwise narrowed, not closed** | Theorem E, ELABORATING of MECH-1 Lemma A and Corollary A′, OA-1 D5 and D7, obsmu Proposition C and TUNE-1 Lemma A-T. Gaps: non-nested multi-time reads (AW-OA2-4), non-spanning preparations (N2.1), non-additive observers (AW-OA2-1) |
| Admissible non-affine rules (Layer-0 revision), or supplied control beyond NC's hypotheses | **OPEN** | N2.6 |

`𝔊_K`'s premises, typed:

- designed non-affine `φ` (posit);
- uniform bath (native under μ-G, posited otherwise);
- ready cells and blanks (MP-0a, a resource);
- conveyors longer than the horizon (growing carrier);
- C-PM′ for the label and coin cells, and C-PM for the selector cells (N3).

**The precise open question.** Does some OI-admissible non-affine rule, with fixed partition, layout and
stated μ, have a closure-defined E3, under C-PM, that is not simplex-embeddable? Either route of
Corollary B′ would do. If so, is it qubit-like rather than gbit-like, and does it pass non-import?

A second, independent question: is the affine class itself classical at E3 without (H4) or (SP)?

**Cheapest decisive next steps.**

1. **Paper-only; both shapes (item 8).**
   - *(a) Gbit shape (read restriction).* In `G_SM`, look for two switch-selected read functionals
     `f₀, f₁` of one carrier, four reachable preparations fixing `(f₀, f₁)`, and a disturbance that
     makes the joint read unavailable under every protocol. Test minacc-1's gate-cancellation
     mechanism (`RESULT.md`:54–58) first as a refuter.
   - *(b) Dual shape (preparation restriction, N2.1).* Look for complete reads with reachable laws
     confined to a proper subspace `W ⊊ ℝ^U`, for example a parity re-randomized by every joint read,
     with the facet equivalences of the square.
   - *(c) For the affine class,* attempt (H4)-free Theorem E(b), or the AW-OA2-4 counterexample under
     C-PM.
2. **Computation (needs separate owner authorization).** Exact finite enumeration of the
   closure-defined accessible fragment, then an exact-rational simplex-embedding linear program
   [L: Selby et al., PRL 132, 050202 (2024)].
   This is a design sketch for a future preregistration (N5). It needs owner authorization before
   anything runs.

   **Common settings.**
   - μ = μ-G on all non-ready cells. MP-0a ready cells and blanks are declared in the joint initial law.
   - Label convention: C-PM. Preparation-label, selector and coin cells are excluded from effects, and
     in 𝔊_K the label and coin cells are moved out of reach as well (C-PM′).
   - Two record variants, each run separately:
     - (i) MP-0b nested (H4): the held record is the `V` history up to the horizon;
     - (ii) held = present `V`: reads at different durations are separate procedures.
   - Exact rational arithmetic throughout.

   **Per-object partitions.**

   | Object | `V` (H-AR, cell-aligned, both slots) | Setting cells | Ready cells | Carrier, rest | Horizon |
   |---|---|---|---|---|---|
   | `𝔊_K` | setting cells and record cells (at least `K` blanks) | gadget selector, `p`, `ℓ`, `f`, `w`, `m` | ready conveyor, `M_r > 4K` | carrier `(x, y)`; bath `M_b > K` | gadget budget `K` |
   | `N₁` (R-lin, `q = 2`, ring `Z₇`) | sites `{0, 1, 2}` | `v`-slot of site 0 at `t = 0` (measurement setting); site 1's slots at `t = 0` as preparation label (C-PM) | site 2, both slots known 0 (MP-0a); a P2 half-known variant reported separately | carrier site 3; sites 4–6 uniform | tick horizon `T ≤ 4` |
   | `G_SM` (`q = 2`, ring `Z₅`) | sites `{0, 1}` | `u`-slot of site 0 at `t = 0` (it gates the graph); site 0's `v`-slot as preparation label (C-PM) | site 1, both slots known 0 (MP-0a) | carrier site 2; sites 3–4 uniform | tick horizon `T ≤ 4` |
   | Variant-(ii) negative control | the record cell | read selector | blank record cell | one `F₂²` cell under identity dynamics; each read copies `(x, y)` into one record cell, which the next read overwrites | `K` reads |

   - **Heralds.** For every object, a herald is conditioning on the value of a stated `V` cell at a
     stated tick. Heralded preparations are listed in the preregistration.

   **Controls, preregistered.**
   - **Positive control:** `𝔊_K` must return non-embeddable, in both variants. Its record cells are
     written once and never overwritten, so the variants coincide and validate both pipelines.
   - **Negative control, variant (i):** `N₁` must return embeddable (Theorem E). It counts green only if
     both of these hold first:
     - **(SP)** on its reachable record laws;
     - **a non-vacuity check:** at least two operationally distinct reachable classes and at least two
       non-equivalent available effects. This guards against `E` collapsing to a point or a segment,
       for example by equal-time blindness, OA-1 D2.

     If either check fails, the control is void, not green.
   - **Negative control, variant (ii):** the single-cell object must return embeddable. Its classicality
     is proved independently: `W = ℝ^U` from the point preparations, and `ρ` is injective, so
     Proposition B(i) and B(ii) (⇐) give a noncontextual configuration model. It is subject to the same
     non-vacuity check.
   - **Measurement without a prediction:** `N₁` in variant (ii). It bears on AW-OA2-4 and counts only
     over green variant-(ii) controls.
   - **Test object:** `G_SM` in both variants.

   **Decision rule, stated in advance.**
   - Verdicts print only over green, non-vacuous controls.
   - **A non-embeddable `G_SM` result would establish** G3 (prepare–measure) for that object, at the
     stated μ, partition, horizon, label convention and record variant.
   - **It would not establish:**
     - non-import, item (d)4;
     - admissibility under §A.29, since `G_SM` remains a Layer-0 revision needing advance-stated
       preserved results and an independent prediction;
     - anything at unbounded horizons (AW-OA2-2), or under other partitions or μ;
     - a qubit-type fragment (G5).
   - **An embeddable `G_SM` result would establish** classicality at that size, horizon and
     convention only. It is not an impossibility result for `G_SM`.

***

## 5. Status table

| Item | Status | Support |
|---|---|---|
| Configuration-level ceiling (no phases, not `DerivedOI`, no dense `Fin 2` control; rule-independent) | proved | [K] OB/FrozenSourcing.lean:84, :99, :111, :173, :295, :327; OB/SubstratumInterfaceAudit.lean:780 |
| No finite carrier induces `rot` exactly | derived in-corpus | [R] AP1:955–979 |
| ε-quantum single reversible realization (imported data); finite-carrier prepare–measure obstruction | proved on paper | [P] Main:564–582; Main:558 (half imported) |
| MECH-1 Lemma A and Corollary A′; OA-1 D5 and D7 | paper records | [R] MECH-1:404–425; OA1r4:172–204 |
| Lemma F, Theorem NC (states spanning), U2 | paper records | [R] MECH-2:307–347, :483–541 |
| Lemma 0 (well-definedness "when", not "exactly when"), Proposition A | derived here | [W] |
| Lemma 1 (closure, under C-PM) | derived here | [W] |
| Proposition B (corrected: preparation NC from injectivity; configuration-model measurement NC iff `ρ` injective, both directions proved; transformation NC on `ℝ^U`) | derived | [W] + [RW] |
| Counterexample: injective `R`, measurement-contextual (dual gbit) | derived | [RW], re-derived [W] |
| Corollary B′ (preparation **or** effect equivalences coarser than ontic) | CONFIRMING | MECH-2:842, :521–529 [R]; [W] |
| Theorem C (finite reversible group; step 3 on `cl conv E`) | derived here | [W]; prior art AP1 §5.3 [R]; [L] |
| `𝔊_K`: exact equivalence and preparation contextuality, per horizon, under C-PM′ and C-PM (selector cells) | derived here | [W]; maximal violation of AP1 Lemma 4′ [R]; [L] |
| Theorem E(a), (c) | restatement | [R] MECH-1 Lemma A, OA-1 D5; (c) needs H-LIFT |
| Theorem E(b): prepare–measure fragment simplex-embeddable under (H1), H-AR, (H3), (H4), (SP), (xiv) | derived here, ELABORATING | [W] on [R]; prior art MECH-1 Lemma A and Corollary A′, OA-1 D5 and D7, obsmu Proposition C, TUNE-1 Lemma A-T |
| Affine class at E3 without (H4) or (SP) | open | [O] AW-OA2-4; N2.1 |
| Corollary E1 (contrapositive of generalized E(b): under (H4), (SP), (xiv), G3 needs settings that do not merely translate the joint record, for any rule; compatible with OA-1's insufficiency) | derived | [W] + [RW] |
| Corollary E2 (affine, `q = 2`, parity, (xiv): CHSH ≤ 2) | derived | [W], confirmed [RW] |
| Class N, one cell, native `Z`/`X`: preparation- and measurement-NC (algebra for every `q`; premises at `q = 2`, and at odd `q` via MECH-1 Proposition C(d)) | conditional | [W] + [RW] on [R] |
| G3 for admissible non-affine rules; qubit-type fragment; non-import | open | [O] |
| AW-OA2-1, -2, -4 | open | [O] |

***

## 6. §A.31 classification and markers

- **Productivity test, fixed in r1.** A gem needs a fact strictly stronger than a restatement that
  either constrains something or exposes a hidden assumption.
- **Theorem E: ELABORATING** (r1 said NEW; F5). It is the E3-level, simplex-embedding corollary of
  MECH-1 Lemma A and Corollary A′ and OA-1 D5 and D7, using obsmu Proposition C's coset structure. It
  is conditional on (H1), H-AR, (H3), (H4), (SP) and (xiv). It closes 5d (OA1r4:421) only for that
  class.
- **Theorem C: ELABORATING.** It is an operations analogue of AP1 §5.3 and Main:558 and covers every
  interface.
- **Corollary B′: CONFIRMING** of MECH-2:842.
- **Proposition B (corrected): ELABORATING** of NC: frame-free, with the effect-side condition explicit.
- **`𝔊_K` and §3.1: ELABORATING** of MECH-2:521–529 and OA1r4:466–470. It is a physically absent
  read, and the maximal violation of AP1 Lemma 4′.
- **Proposition A, Lemmas 0 and 1: CONFIRMING.**
- **Class N single cell: ELABORATING,** conditional.
- **Assumption-watch markers.**
  - **AW-OA2-1 (H-AR).** A non-additive observer is a possible exit from Theorem E and Corollary E2.
    Detector-click readouts are of this kind. Watch it wherever a coarse readout `Y` is used (OA-1 D8).
  - **AW-OA2-2 (recurrence against permanent inaccessibility).** M-INACC's "every permitted reuse"
    (MECH-2:837–838) interacts with recurrence (Main:60).
  - **AW-OA2-3 (richness is not quantumness).** G1–G3 at bounded horizon are statements about access.
  - **AW-OA2-4 (new; non-nested multi-time reads).** Under "held = present `V`", reads at different
    durations are not jointly held. Whether the affine class can then exhibit the gbit pattern is
    open. The same hazard applies to any record-level (5d) claim that treats "one joint record" as
    available without retention (obsmu:917).
- **Favourable-branch pressure tests.**
  - The YES of N2.3 is narrowed to bounded horizons and C-PM′, with C-PM for the selector cells.
  - P★ is excluded as evidence.
  - The openness of N2.6 is reported together with minacc-1's contrary evidence.
- **Tally: no NEW findings.** This is one pass; the fixed point has not been reached.

***

## 7. Reading inventory

**At `main`.** Sources were read at three snapshots:
- r1's at `fb733b4a`;
- r2's additions at `ec257bee`;
- r3's additions at `615cc119`.

The cited paths are unchanged across the three. The only change on them is the TUNE-1 drafts added at
`615cc119`.

- **`papers/Main.md`** (r1 lines plus r2 additions):
  - :42, :54, :58, :60, :82–92, :97, :147;
  - **:260**;
  - :358–416 (Bell ceiling :364ff., corollary :414);
  - :480–482, :552, :558, :564–582, :596;
  - **:650**, **:664**;
  - :724 (ledger (ii), (iv), (vii), (xiii), (xiv)).
- **Lean statements** in `OIBridge/`:
  - `FrozenSourcing.lean`: :1–130, :290–340;
  - `SubstratumInterfaceAudit.lean`: :495–520, :700–830;
  - `RouteB.lean`: :125–160;
  - `DiscreteCompletion.lean`: :35–60;
  - `CentralObservation.lean`: :605–625;
  - `OperationalAssembly.lean`: :594, via `git grep`.
- **Records:**
  - **`mechanism-1-20261107/DESIGN.md`** (new in r2; §A.19):
    - :1–137 (standing and result);
    - :390–440 (Lemma A, Corollary A′);
    - :749–830 (Proposition C, Observation E, Theorem T, Proposition T′);
    - heading grep of the rest.
  - **`apparatus-1-20261107/DESIGN.md`** (new in r2): :694–730 (Lemma 4′ and scope) and :950–985 (§5.3).
  - `mechanism-2-20261108/DESIGN.md`: :1–200, :300–360, :483–545, :519–530, :700–745, :828–860, plus grep.
  - `mathcon1-polc-20261108/DESIGN.md`: :540–640.
  - `minacc-1-20261108/RESULT.md`: :1–140; `DESIGN.md` grep.
  - `round-arp1-marc-20261108/result.md`: :1–111.
  - `observer-interface-obsmu-20261104/ANALYSIS.md`: :544–582 (Proposition C, new in r2) and :885–920.
  - `states-dynamics-audit-20261024/operational-quotient-v3/REPORT.md`: :1–60.
  - `quarter-phase-native-20261107/DESIGN.md`: grep only.

**At OA-1 `066be3b1`.** `OA-1-REPORT-r4.md` (whole); `REVIEW-OA-1-r3.md` (whole); `REVIEW-OA-1.md`
(grep and :205–230); `REVIEW-OA-1-r2.md` (grep).

**Review.** `working/oa2/REVIEW-OA-2.md` (whole); `working/oa2/REVIEW-OA-2-r2.md` (whole).

**At `main` `615cc119` (r3).** `reconstruction/drafts/tune-1-20261111/TUNE-1-STEP2-SESSION3.md`:28–100
(Lemma 0, Lemma A-T). Directory listing of `drafts/tune-1-20261111/`. `git diff --stat ec257bee 615cc119`
on the cited paths.

**Not read.** TUNE-1 outside `TUNE-1-STEP2-SESSION3.md`:28–100; AP1 outside the lines above; MECH-1 outside the lines above; the QA body;
`two-mode-drive.md`; `whole-model-bridge.md`; the literature [L]. Negative claims are limited to these
sources.

***

## 8. Limits

- Every [W] and [RW] item is an unreviewed hand derivation. None is kernel-checked.
- Theorem E's NO needs (H1), H-AR, (H3), (H4), (SP) and (xiv). (c) needs H-LIFT. Without (H4) or (SP),
  the affine class is narrowed, not closed.
- Theorem C covers trace-preserving operations only.
- Proposition B(ii) is proved in both directions for the configuration model (N1). Neither direction
  decides simplex-embeddability of the fragment: that needs a separate argument, such as the
  counterexample.
- `𝔊_K` is a designed control, exact per horizon. It uses C-PM′ for its label and coin cells and C-PM
  for its selector cells (N3). It is not an OI construction.
- The class-N single-cell result rests on [R] premises and on H-LIFT.
- The literature is context only. Every proof here is self-contained.
- No manuscript claim is affected. Corollary E2 complements Main:414 and proposes no edit.

***

## 9. Changes from r1 (finding → change; verdicts moved)

| Finding | Change | Verdict moved? |
|---|---|---|
| **F1** | Proposition B restated: preparation NC from injectivity; measurement NC iff `ρ` injective (sufficient: `W = ℝ^U`, NC's hypothesis, MECH-2:489, :506); transformation NC on `ℝ^U`. Reviewer's `F₂²` counterexample added and re-derived by hand. Corollary B′ becomes two-route, credited to MECH-2:842 and :521–529. Class-N single cell re-justified by the injectivity check. Propagated to §0.3, N-b, next step 1, §5 and §6 | **Yes.** B′ "non-injectivity necessary for every rule" becomes "preparation or effect equivalences coarser than ontic", CONFIRMING. The class-N conclusion survives on a corrected reason |
| **F2** | Added (H4) nested records. (H3) now excludes only supplied control, and durations are native. The non-nested case is stated as gap AW-OA2-4, with the gbit ingredient not excluded. Pressure test 2 rewritten. Theorem E, E1 and the headline restated under (H4) | **Yes.** The affine-class NO becomes conditional on (H4); without it, narrowed, not closed |
| **F3** | (SP) and (xiv) carried into Verdict N2.4, §0.6, the conclusion row, the status table and §3.1. A measure table was added (§3.3) | **Yes.** "Fails G3", "classical E3" and "for every measure" are now conditional |
| **F4** | C-PM stated in §1.0 and reconciled with "none removed by fiat". 𝔊_K uses the physical form C-PM′: PREP moves label and coin cells out of reach. Rotation gadgets `ROT_b` and `ROT_r` specified, PREP(ℓ) rotates the bath, and the horizon recounted as `M_b > K`, `M_r > 4K`. C-PM applied to Theorem E | No. The 𝔊_K verdict holds per horizon, under C-PM′ |
| **F5** | MECH-1 read. Theorem E reclassified ELABORATING, with credit to MECH-1 Lemma A, Corollary A′ (MECH-1:424–425), OA-1 D5 and D7, and obsmu Proposition C. Tally changed to no NEW | **Yes.** NEW becomes ELABORATING; tally 1 becomes 0 |
| **F6** | Corollary E1 restated conditionally. It is a necessity statement compatible with OA-1's insufficiency (OA1r4:515), with three open exits; "non-translational setting dependence of reads (MP-1 or P3/E-iso)" replaces "the gap-2 repair" | **Yes.** It no longer claims the repair is necessary for gap 3 outright |
| **F7** | H-AR stated as a named observer restriction (§1.5), with Main:42, :82–92, :260, :650, :664. Named in §0.6 and the conclusion row | Scope only |
| **F8** | Theorem C step 3 argued on `K = cl conv(E)`. AP1 §5.3 credited, the Main:558 relation restated, and literature added | No. Still ELABORATING; the verdict stands |
| **F9** | Lemma 0 "exactly when" becomes "when", with strong lumpability. Heralds: "continuous group" becomes "injective maps of infinite order, a countable family, reversible when inverse likelihoods are reachable". E(c) needs H-LIFT. `CentralObservation.lean:620` marked as context. E2 "complements" Main:414. "Non-discriminating" scoped to bounded horizon (§0.4, §1.3, §3.1). MECH-2:521–529 and AP1 Lemma 4′ credited for 𝔊_K | No |
| **Item 8** | Next step 1 adds the dual shape and an affine (H4)-free attempt. Next step 2 fixes μ, partition, horizon and label convention; `N₁` is a valid negative control only with MP-0b nested records, H-AR and a passing spanning check (void otherwise); a non-nested `N₁` variant is a prediction-free measurement | — |
| **Item 9** | Overreach removed: §0 items 3, 6 and 7; Verdict N2.4; the conclusion row; status entries for B′ and E; the NEW label; "for every rule" on B′; "continuous group" | as above |

**Net verdict movement.**

- YES (general deterministic dynamics, bounded horizon, non-discriminating): unchanged.
- NO (E1/E2 with a fixed lift): unchanged.
- NO (exact infinite-order control at fixed `S`): unchanged.
- **OI's native affine class: from NO to NO under (H1), H-AR, (H3), (H4), (SP), (xiv), and otherwise narrowed, not closed.**
- Non-affine: OPEN, unchanged.
- No finding is now NEW.

***

## 10. Changes from r2 (nits of `REVIEW-OA-2-r2.md`; no verdict moved)

| Nit | Change |
|---|---|
| **N1** | Proposition B(ii) (⇒) now has the general convex-split proof: split by sign, rescale, pad with the null effect, giving two operationally equivalent effects with different ontic responses. The proof is for the configuration model, and the text notes it does not decide simplex-embeddability. (⇐) is spelled out. The Limits line is corrected |
| **N2** | Theorem E(b) step 5 drops the transformation-noncontextuality claim. G3 is stated as the prepare–measure criterion in E(b), Verdict N2.4 and the status table |
| **N3** | C-PM′ is now scoped to the `p`, `ℓ` and coin cells. Claim 1 is noted as unaffected (same selector). Claim 2 step 3 is stated to use C-PM for the selector and coin cells, with the physical alternative. The conveyor justification is replaced by the window argument (`M_b > K`; `M_r > 4K` via `4(K − 2) < M_r − 7`), and at least `K` blanks are stated. Limits, §4 and §6 are adjusted |
| **N4** | Corollary E1 is restated as the contrapositive of a generalized E(b): under (H4), (SP) and (xiv), G3 needs settings that do not merely translate the joint held record, for any rule. For the affine class under H-AR this means leaving (H1) ∧ (H3). r2's vacuous wording is withdrawn. Failure of (xiv) gives correlation, not control (D7). §0.7 is updated |
| **N5** | Next step 2 gains: per-object partitions (`𝔊_K`, `N₁` on `Z₇`, `G_SM` on `Z₅`, plus a single-cell control); tick horizons for `N₁` and `G_SM`; a herald recording rule; a non-vacuity check for the `N₁` control; 𝔊_K as positive control in both variants; a provably classical variant-(ii) negative control; and a preregistered statement of what a `G_SM` result would and would not establish |
| **N6** | The class-N preparation side is generalized to every `q`: `dim W = dim effect span = 2q − 1` with `ρ` injective, so `R` is injective on `W`. The premises are stated by `q`: `q = 2` per the [R] sources, odd `q` via MECH-1 Proposition C(d) |
| **N7** | (H3) named in §0.6. MECH-1:404–422 changed to :404–418. Snapshot updated to `615cc119`. TUNE-1 Lemma A-T (T1:56–98) credited as research-draft prior art for Theorem E's coset structure. "Not read: TUNE-1" narrowed. Reading inventory updated |

**Verdicts.** No verdict moved:
- YES for designed deterministic dynamics (per bounded horizon; non-discriminating);
- NO for E1/E2 with a fixed lift;
- NO for exact infinite-order control at fixed `S`;
- the affine class: NO under (H1), H-AR, (H3), (H4), (SP) and (xiv), now stated for the prepare–measure fragment, and otherwise narrowed, not closed;
- OPEN for admissible non-affine rules.

**Tally.** No NEW finding.
