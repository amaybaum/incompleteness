# OA-2: can deterministic dynamics induce operations on emergent observer states richer than permutations, with one common preparation and readout?

**Standing.** WIP / UNVERIFIED author report for unit OA-2 under #1169. Paper-only: reading and
hand derivations. No computation on any OI rule, no script, no Lean change, no manuscript edit, no
premise adopted, no claim promoted. Nothing committed, pushed or posted. Ends in independent
review.

- **Authorization.** Owner amaybaum, 2026-11-12, #1169 comment 6831588323 (as relayed in the task
  brief; not re-fetched here).
- **Question (owner, verbatim).** "Can deterministic physical dynamics induce operations on
  emergent observer states that are genuinely richer than permutations of configurations, while
  still providing a common physical preparation and readout process?"

**Snapshots and citation forms.**

- `main` = `fb733b4a58558ef64bd7c3585712c76e9f2dfb42`, read with `git show`.
- OA-1 = branch `research/oa1-w1-1-20261112` at `066be3b1d321d1a325c3b0a577973102f7d0fbb7`
  (draft PR #1265), cited `OA1r4:n` for `.../oa-1-20261112/OA-1-REPORT-r4.md`. Research only
  (§A.46 item 7): used as the starting point, not as established premises.
- `Main:n` = `papers/Main.md`. `OB/File:n` = `verification/lean-mathlib/OIBridge/File`. Other
  record paths are relative to `verification/programmes/oi-qm/reconstruction/`.

**Support labels.** [K] Lean statement on `main` (statement read, nothing built). [P] manuscript
statement. [R] research record, not independently established. [W] derived here by hand, not
reviewed, not kernel-checked. [L] external literature cited from memory, not read in this unit;
context only, no verdict rests on it. [O] open.

**Disclosure.** Commands used: `git fetch`, `git show`, `git ls-tree`, `git grep`, `grep`, `sed`,
`wc`, `cut`, `mkdir`. Early in the session I wrote a byte copy of `Main.md` (from `git show` at
`fb733b4a`) into the working root and created a local ref `refs/oa2/oa1`; both were removed,
and every Main line cited below was re-read with `git show fb733b4a:papers/Main.md`. No script was
written or run.

***

## 0. Plain-language summary

1. On laws over configurations, a bijection acts stochastically, and reversibly only by permutations (N0).
2. Hidden memory alone does not escape; the target-neutral emergent state is the operational class (N1).
3. On operational classes, escape is possible exactly through non-injectivity: preparations that
   are physically equivalent but ontically different (N2.1).
4. A designed reversible classical computer escapes exactly; its observer sees a contextual "gbit" (N2.3).
   Each target-neutral criterion G0, G1 and G3 is therefore passed by some classical computer, and
   G2 is passed with growing carriers. Richness measures access structure, not quantumness.
5. At a fixed finite carrier, reversible emergent operations form a finite group, for every rule (N2.2).
6. **For OI's own (gauge-derived affine) rule class the answer is NO.** Every protocol is one fixed
   measurement shifted by the settings: the emergent theory is classical, and settable operations are
   translations after one fixed noise map, for every measure and carrier size (N2.4).
7. So the gap-2 repair (or supplied P3/E-iso) is necessary for gap 3. Sufficiency is OPEN (N2.6).

***

## 1. Definitions, in OI's own terms

### 1.0 One physical setup and its procedures

`𝔖 = (S, φ, (V, H), μ, A)` as in OA1r4:90–117:

- `S` finite (Main:60; ledger (ii), Main:724), or a finite-horizon window of a lattice;
- `φ` a bijection fixed before any target;
- `V ⊊ S` the observer, `H` the hidden sector (Main:42);
- `A` the apparatus layout, fixed once;
- `μ` one of μ-O (per-orbit, derived, Main:54), μ-G (global counting, posited selection,
  Main:54, :58) or μ-R (record-compatible maximal entropy, posited, ledger (iv), Main:724). These
  are not interchangeable (OA1r4:236–270).

**Procedures `Proc(𝔖)`.** A protocol is a finite schedule of waiting under `φ` in which the observer's
settings are cell contents, either initial or written by `φ` from records (feedback), with optional
heralds (conditioning on held records) and discards (ignoring cells). `Proc(𝔖)` is closed under
sequential composition. Its available effects are **all** post-processings of held records: none is
removed by fiat. Reachable preparations are the laws produced by procedures, conditioned on heralds.
A preparation followed by a procedure is again a preparation. "Held" follows OA1r4:107–110; the
visible-history convention MP-0b is allowed and stated where used.

### 1.1 (a) Emergent observer states: three candidates

All three are laws, or classes of laws, on `S`. None posits a Hilbert space.

| | Definition | Measure dependence |
|---|---|---|
| **E1** record law | The law of the observer's present record class (visible configuration, or a coarse readout of it) | Its value depends on μ |
| **E2** posterior state | The conditional law of the full configuration given the observer's held records, under the stated μ (Main:97's history posterior; H-PREP reads it as a preparation, obsmu `ANALYSIS.md`:893–901) | Its value depends on μ, and it is a different object under μ-O, μ-G and μ-R |
| **E3** operational class | `[p] := {p′ : e(p′) = e(p) for every available effect e}`, with `p` a reachable E2-type law. `R(p) := (e(p))_e` is the read map, and `E := R(reachable)` | The definition is measure-free. The set `E` depends on μ through the reachable laws |

E3 is the predictive state: the coarsest description that fixes all future available statistics.
Every result below that holds "for every law" is measure-free. Where a result needs a particular μ,
that is stated.

### 1.2 (b) Induced operation

For `π ∈ Proc(𝔖)` with settings recorded, the induced operation is the map `[p] ↦ [π(p)]` on E3 (or
`p ↦ π(p)` on E1/E2 when it is well-defined).

- *Trace-preserving* means no herald.
- *Heralded branches* are `[p] ↦ [π_k(p)]` with `π_k` subnormalized and then renormalized.
- An operation is *reversible on emergent states* if it maps `E` onto `E` bijectively.

### 1.3 (c) "Genuinely richer than permutations": criteria and their neutrality

"Permutations of configurations" are the maps on `Δ(S)` induced by `σ ∈ Sym(S)`, and their
quotients.

| Criterion | Operational content | Target-neutral? | Discriminates a reversible classical computer? (§3) |
|---|---|---|---|
| **G0** | Some induced operation is not induced by a configuration permutation | yes | **no**: any noise or erasure passes |
| **G1** | `E` is not a simplex | yes | **no**: restricted-access classical models pass (§3) |
| **G2** | Exact reversible trace-preserving emergent operations of infinite order, e.g. dense control on a 2-level emergent system | yes | **no**: fails at every fixed finite `S` for every rule (N2.2); a classical rotor with growing carriers passes; heralded classical Bayesian filters pass at fixed `S` |
| **G3** | The emergent theory (states, operations, effects) has no noncontextual ontological model, equivalently is not simplex-embeddable [L: Spekkens PRA 71, 052108 (2005); PRL 101, 020401 (2008); Schmid et al. PRX Quantum 2, 010331 (2021)] | yes: only laws and convex structure | **only against full access**: a classical computer with a physically restricted interface passes exactly (N2.3) |
| **G4** | Phases, coherent mixing, or dense `Fin 2` unitary control | **no**: it presupposes an identification of emergent states with operators on `ℂⁿ`, which is the target's structure | the configuration-level interface fails it [K]; this interface is not the emergent level |
| **G5** | A quantum-specific fragment (e.g. OA1r4:479–486 T-P to T-R) | no, target-specific by design | ε-versions are passed by designed reversible maps (Main:580) and caught only by non-import |

The **kernel ceiling** is `NonnegBounded`: every available one-outcome composite preserves
entrywise nonnegativity of matrices on `ℂ^{Conf × Fin n}` (OB/FrozenSourcing.lean:65–67;
`PreservesNonneg`, OB/SubstratumInterfaceAudit.lean:505–506). It has no phases (:99), no dense `Fin 2`
control (:173) and is not `DerivedOI` (:111), with `nonnegBounded_verdict` at :327 [K]. It is stated
for the configuration identification (`obsTheory = permTheory Conf`, OB/SubstratumInterfaceAudit.lean:770–782). It is G4 at the
configuration level. **G3 is the representation-invariant analogue for E3:** a theory is simplex-embeddable
exactly when some classical ontic space carries all its states, effects and operations as
nonnegative objects.

### 1.4 (d) Common physical preparation and readout

1. **One `𝔖` for all settings.** Settings are cell contents. There are no per-setting tables and no
   writes outside `φ`.
2. **Closure.** The effects, procedures and preparations are all of `Proc(𝔖)`, with no omissions by fiat.
3. **Admissibility.** `φ` is from the corpus's rule class (the gauge-derived affine class, ledger
   (vii), with R-lin (xiii), Main:724), or is a declared Layer-0 revision subject to §A.29.
4. **Non-import.** The supplied elements cannot be re-tuned, with `φ` and the partition fixed, to a
   non-quantum target just as easily (OA1r4:119–120).

Items 3–4 decide whether a construction bears on OI. Items 1–2 decide whether it is a common
realization at all.

***

## 2. Depth-first chain

### N0. Emergent state = law over configurations, or over record classes with a fixed lift

**Lemma 0 (stochasticity) [W].** Fix a protocol and condition on its settings and heralds. It acts
on `Δ(S)` as a nonnegative matrix:
- `φ` is a permutation matrix;
- attaching a cell in a fixed law is a tensor product;
- a discard is a marginal sum;
- a herald is a 0/1 diagonal;
- feedback is a record-indexed sum of these.

Without heralds the matrix is column-stochastic. This is MECH-2 Lemma F's proof without the frame
(`mechanism-2-20261108/DESIGN.md`:333–344) [R], and the diagonal reading of the kernel's invariant [K].

Let `κ` be a partition of `S` (record classes). The induced map on `Δ(κ)` is a function of the
coarse law exactly when, for every class, the conditional law inside the class at input (the lift) is fixed.
It is then the stochastic matrix `Σ_{s∈j} λ_j(s) M(i|s)`.

**Proposition A (reversible ⇒ permutation) [W].** A linear map taking the simplex `Δ_n` onto
itself bijectively permutes its vertices, so it is a permutation matrix. ∎ This is the special case
of Theorem C below, with `E` a simplex.

**Verdict N0: NO, for this class.** For every φ and every μ, the trace-preserving induced operations
on E1/E2 with a fixed lift are stochastic matrices, and the reversible ones are permutations of
classes. Irreversible stochastic maps pass G0, but G0 does not discriminate.

### N1. Option (ii): the induced map is not a function of the emergent state (hidden memory)

When the lift is not fixed, which is H-LIFT failing (MECH-2 :319–321, :346–347), the coarse
law's future depends on the hidden conditional law. The "operation" is then a set of stochastic
matrices indexed by the lift. It is not a map on E1.

**Lemma 1 (closure) [W].** On E3 every `π ∈ Proc(𝔖)` induces a well-defined linear map `π_E`.

*Proof.* If `p ∼ p′`, then for every available `e`, `e ∘ π` is available by closure, so
`e(πp) = (e∘π)(p) = (e∘π)(p′) = e(πp′)`. Linearity follows because `π` is linear on laws and `R`
is linear. ∎

**Verdict N1: not an independent escape.** Inaccessibility or hidden memory does one of two things.
It makes maps on cruder spaces (E1) ill-defined, or, refined to the predictive class, it reappears as
the shape of the quotient `R` (N2). Each lift-indexed branch is stochastic (Lemma 0), so option (ii)
alone stays inside the ceiling.

### N2. Option (i): emergent state = operational class (E3)

#### N2.1 Injectivity is the whole ceiling

**Proposition B [W].** Let `W = span(reachable laws)`. Suppose `R` is injective on `W`. Then:

- the substratum's own model is preparation- and transformation-noncontextual: `p` is a function
  of `[p]`, and `π|_W` is fixed by `π_E` through `R π = π_E R`;
- if, in addition, the effects restricted to `W` span `W*`, it is measurement-noncontextual, so
  `E` is simplex-embedded by `R⁻¹`;
- every induced operation is the restriction of a stochastic matrix (Lemma 0).

*Proof.* This is Theorem NC's proof (MECH-2 :500–507 [R]) with the frame replaced by `R` itself.
No orthogonal frame and no `q = 2` structure enter. ∎

**Corollary B′.** G3 requires two reachable laws with the same emergent state, used non-trivially.
This is the inaccessibility clause (b) of M-INACC (MECH-2 :834–840 [R]), now **necessary in E3 for
every rule**, with no frame. It is not sufficient: a decoupled hidden coin makes `R` non-injective
while the quotient is still a simplex.

#### N2.2 Fixed finite carriers: reversible emergent control is always finite

**Theorem C [W].** Fix finite `S`, any φ, any μ, any interface. Let `π` be trace-preserving with
`π_E(E) = E`. Then `π_E` is an affine automorphism of the polytope `P_W := R(Δ(S) ∩ W)`. The set of
all such `π_E` lies in a finite group of vertex permutations of `P_W`. Under H-SPAN (`W = ℝ^S`),
the vertices of `P_W` are among the images `R(δ_s)` of configurations.

*Proof.*
1. Reachable laws are closed under available procedures, so `π(W) ⊆ W`. Then
   `π_E(P_W) = R(π(Δ ∩ W)) ⊆ P_W`.
2. `aff(E) = R(W ∩ {mass 1}) ⊇ P_W ⊇ E`, so `E` and `P_W` are full-dimensional in one affine
   space.
3. `π_E(E) = E` forces `|det π_E| = 1` on that space.
4. So `π_E(P_W)` is a closed convex subset of `P_W` with equal volume, hence equal to `P_W`.
5. An affine automorphism of a polytope permutes its vertices and is fixed by that permutation.
   The group is finite, so every inverse is a power, and inverses are themselves induced. ∎

**Consequences.**

- **G2 fails at every fixed finite `S`,** for every rule and every interface, with no
  nonnegative-rank import. Example: a setting-selected rotation at `cos θ = 3/5` has infinite
  order, since `(3+4i)/5` is not an algebraic integer, so exact T-C (OA1r4:484) needs growing
  carriers.
- This is a self-contained derivation, for operations, of the carrier-growth necessity that OA-1
  R7 took half-imported from Main:558.
- **Confirming instance.** In op-quotient v3, a stochastic implementation of a rotation must preserve
  the sign cube, which leaves the 24 Cliffords
  (`states-dynamics-audit-20261024/operational-quotient-v3/REPORT.md`:17–24) [R].

**Scope and pressure tests.**

- **Heralds break the theorem, classically.** Renormalized branches `p ↦ Dp/|Dp|` with `D` a
  positive diagonal (a Bayesian likelihood filter) are reversible on the open simplex. They form a
  continuous group at fixed `S`. G2 for heralded maps is therefore non-discriminating.
- **Growing carriers are not sufficient.** A classical rotor discretized to `N` points, read through
  the response `(1 + cos(λ − α))/2` (apparatus noise supplies the randomness), has `E` equal to an
  `N`-gon. Its rotations by `2π/N` become dense in the rebit disk's `SO(2)` as `N` grows.
- G2 therefore tests carrier growth, not quantumness.

#### N2.3 Existence: a designed reversible classical computer passes G3 exactly

**Universe `𝔊_K` [W].**

| Part | Content |
|---|---|
| `H` | carrier `(x, y) ∈ F₂²`; a bath conveyor `b_1 … b_M` of uniform independent bits with `M > K`; a ready conveyor of known-0 cells |
| `V` | setting cells; record cells, blank (MP-0a, OA1r4:547–552) or under MP-0b |
| Ready cells and blanks | declared in the initial law, as MP-0a |
| Bath | uniform: native under μ-G (Main:58); not established under μ-O or μ-R |

One fixed bijection `Φ` applies a gadget selected by setting cells (a controlled bijection is a
bijection):

- **PREP(p_x, p_y).** Swap `(x, y)` with two ready cells, which leaves `(x, y) = (0, 0)` with the old
  contents out of reach. Then `x ⊕= p_x` and `y ⊕= p_y`.
- **FLIP(f).** `x ⊕= f`.
- **SWAP(w).** A Fredkin gate: if `w = 1`, `x ↔ y`.
- **MEAS(m).** If `m = 0`: `r ⊕= x` into the next blank, `y ↔ b_1`, rotate the bath conveyor. If
  `m = 1`, the same with `x` and `y` exchanged.

No other coupling joins `V` to `(x, y)`. Protocols contain at most `K` MEAS steps.

**How the mixtures are prepared.** The mixtures `P_A` and `P_B` used below are prepared by a variant,
PREP(A/B). It zeroes the carrier as PREP does, then copies a fresh bath bit `b` into both cells:
`(b, b)` for A and `(b, b ⊕ 1)` for B. The bath bit then rotates out of reach. The observer
therefore holds only the label A or B, never the coin. This avoids the label being readable from
the held `p` cells.

**Claim 1 (exact operational equivalence) [W].** Let `P_A = ½[00] + ½[11]` and
`P_B = ½[01] + ½[10]`. Then `P_A ∼ P_B` under all of `Proc(𝔊_K)`.

- Before the first MEAS, no held cell depends on `(x, y)`. PREP sends the old contents to the ready
  conveyor, and settings or feedback cannot depend on the carrier. FLIP and SWAP map
  `{P_A, P_B}` to itself.
- At the first MEAS (say `m = 0`), the joint law of (records, carrier, every cell within reach) is
  the same under both preparations: record `x`, carrier `(x, b_fresh)`, with `x` and `b_fresh`
  uniform and independent.
- The two cases differ only in the bath cell holding the old `y`. It comes back within reach after
  `M > K` measurements, so never within the protocol.
- So all later statistics agree. ∎

**Claim 2 (contextuality) [W].** No preparation-noncontextual ontological model reproduces `𝔊_K`'s
statistics.

1. The point preparations `[ab]` are reachable through PREP. The reads `X` and `Y` are sharp on them.
2. Let `ξ_{X0}` and `ξ_{Y0}` be any response functions with values in `[0, 1]`. Since `e([ab]) ∈ {0, 1}`,
   `ξ_{X0} = 1 − a` and `ξ_{Y0} = 1 − b` hold μ_{ab}-almost everywhere.
3. So the four supports are pairwise disjoint.
4. PREP(A) is operationally equivalent to the explicit mixture `½[00] + ½[11]`, and PREP(B) to
   `½[01] + ½[10]`. With Claim 1, preparation noncontextuality and convex-linearity then require
   `½(μ₀₀ + μ₁₁) = μ_A = μ_B = ½(μ₀₁ + μ₁₀)`. The left side is a
   probability measure on `supp₀₀ ∪ supp₁₁`, the right side one on `supp₀₁ ∪ supp₁₀`, and these are
   disjoint. Contradiction. ∎

The emergent theory is the square ("gbit") with its four facet effects. It passes **G1 and G3
exactly**.

- **G0:** passed by MEAS-and-discard, `(p, q) ↦ (p, ½)`. As part of a non-simplex-embeddable theory,
  this map has no stochastic representation on any classical simplex that is consistent with the
  states and effects.
- **G2:** not passed. The reversible operations are the dihedral group of order 8 (Theorem C).
- **G4 and G5:** not passed. A gbit is not a qubit.

**Pressure test.**

- *Recurrence.* With unbounded protocols on a finite `S`, the bath returns the old `y` and the
  equivalence fails. Exactness holds for each `K` with `M > K`, a growing-carrier family. Whether a
  *used* functional can stay inaccessible to unbounded protocols on a finite bijection is
  not settled here (marker AW-OA2-2).
- *Closure.* PREP was designed so that it does not leak. A swap of the carrier into held cells would
  read both bits and destroy the equivalence. The restriction is a property of `Φ`, not an omission.
- *Admissibility and non-import.* `Φ` is designed (Toffoli/Fredkin, not affine). It fails (d)3 and
  (d)4 by construction. It is a control, not an OI result.
- *Novelty.* The gbit, contextuality with compatible reads and classical Kochen–Specker-type models
  are known [L: Selby et al., PRL 130, 230201 (2023); Kochen–Specker 1967]. What is new here is
  only the exact deterministic-reversible implementation with a closure-defined interface, proved by
  hand.
- *Quantum targets.* Main's gluing (Main:564–582 [P]) gives a single reversible map whose E3 states
  are ε-quantum, "Quantum mechanics enters as the instrument data and as the state held in the
  hidden register" (Main:580). It is non-injective, as Corollary B′ requires: a mixture of register
  values and the register holding the mixed state are operationally equivalent.

**Verdict N2.3: YES, for deterministic reversible dynamics in general.** It is non-discriminating:
the richness sits in an access structure that a classical computer can supply.

#### N2.4 OI's native rule class: the single-measurement collapse

**Hypotheses.**

| Label | Content |
|---|---|
| (H1) | `Φ(ω) = Aω + k`, with `A` an additive bijection of the finite abelian configuration group: the gauge-derived affine class, ledger (vii), Main:724; R-lin included. For a lattice, use a finite-horizon window |
| (H2) H-AR | The held record is an additive function of the configuration: cells read at full resolution, a set of visible cells, or MP-0b's visible history |
| (H3) | Fixed layout and schedule. No supplied per-tick or per-edge control (P3, E-iso) and no supplied timing selection. Natively these are not available (OA1r4:198–204, D7) |

**Theorem E [W, on D5 (OA1r4:172–190, [R]+[W])].** Under (H1)–(H3), write the initial configuration
`ω₀ = (σ, c, α)`: carrier, settings, rest.

- **(a) Measure-free.** For every protocol the held record is `Z = H_σσ + H_c c + H_αα + k′`, with
  `H_•` fixed homomorphisms that do not depend on `c`. Feedback is written by `Φ`, so it is affine
  too, and every setting value only translates `Z` by `H_c c`.
- **(b) Classical E3.** Assume (xiv) (Main:724), so settings are independent of `(σ, α)`. Define
  - `Λ = values of Z₀ := H_σσ + H_αα + k′`;
  - `ι(s) = law of Z₀ under s`;
  - for the effect `(c, f)`, the response `λ ↦ f(λ + H_c c)`.

  This model reproduces every statistic. It is preparation-noncontextual: take `c = 0` and singleton
  indicators, which are available, so the class fixes the law of `Z₀`. Any transformation segment acts
  in it as a marginalization followed by a translation, both stochastic. If the reachable laws of
  `Z₀` span the functions on their support, it is simplex-embeddable.
- **(c) Induced operations.** On carrier laws, setting `c` induces
  `σ ↦ A_σσσ + A_σαα + k + A_σc c`: one fixed, setting-independent stochastic map (the pushforward
  averaged over `α`) followed by the translation `A_σc c`, which is a permutation of configurations. ∎

**Verdict N2.4: NO, for exactly this class.**

- Under (H1)–(H3), for every μ (for (a)) and under (xiv) (for (b)), and at every carrier size, the
  emergent theory on E1, E2 or E3 fails G3.
- Its settable operations are translations composed with one fixed noise map.
- It can pass G0 and G1, both of which are non-discriminating.

The class ruled out is affine rule, additive readout and no supplied non-translational control. The
verdict says nothing about non-affine rules, about supplied P3/E-iso, or about non-additive observer
partitions.

**Corollaries.**

- **E1 (gap 2 is necessary for gap 3 in E3) [W].** Given H-AR, any G3 escape needs a setting
  dependence of the read functionals that is not a translation: MP-1 (OA1r4:556–572), or supplied
  P3/E-iso. This refines OA-1's "independent of the gap-2 repair" (OA1r4:515). The repair is
  **necessary but not sufficient**: insufficiency follows from D6 at configuration level, and in E3
  sufficiency is open (N2.6).
- **E2 (Bell, `q = 2`) [W].** Under (H1)–(H2) at `q = 2` with (xiv), take outcome bits that are parities of held cells.
  1. `E(a, b) = K·(−1)^{(α+γ)a + (β+δ)b}` with `|K| ≤ 1`. This factorizes, so CHSH `≤ 2`.
  2. The bound holds even though additive remote-setting dependence is allowed and no spatial
     separation is assumed. It extends Main's Bell–lattice corollary (Main:414) in this one
     direction, for the whole affine class.
  3. For `q > 2` with a `±1` coarse-graining, H-AR fails and the bound fails: a counterexample over
     `Z₄` reaches 4, but it signals.
  4. No manuscript edit is proposed.

**Pressure tests on Theorem E (all hand-checked).**

1. **Routing a carrier to one of two apparatuses by setting** is a controlled swap, which is
   non-affine, so it is excluded. Placing the carrier at preparation couples the measurement choice
   to the preparation. That is not an independent read.
2. **Time selection** needs conditional copying, which is non-affine (D7). MP-0b's whole history is
   still one `Z`.
3. **Infinite lattices** have a finite cone at a finite horizon (Main:364), so the window is finite
   and (a) applies.
4. **Heralds** are conditionings on components of `Z`, which are preparation labels. (b) is
   unchanged.
5. **Non-additive observer partitions (the H-AR exit).** Take the readout `g(Z + c)` with `g` not
   additive, e.g. `g = 1[Z ∈ {0, 1}]` on `Z₄`. Then `g(Z)` and `g(Z+1)` are two compatible reads
   whose joint `Z` need not be available: the gbit pattern. The exit closes whenever two copies of the same
   functional with known shifts are available, which affine copying permits given blanks. It stays
   open otherwise (marker AW-OA2-1). Main's partition is the projection `π_V` (Main:82–92), which is
   cell-aligned in the lattice model, so H-AR holds there.
6. **Encoded subtheories** (QA's `U′`, P-8, op-quotient v3) restrict reads by an identification, not by
   closure. They are 5c/5d with supplied access and lie outside E3 (§N3).

#### N2.5 Affine rule with supplied control (P1–P3, E-iso): the epistricted class

- **Prior result [R].** With P3 arming, `Z`/`X` reads become selectable. Under H-LIFT with spanning
  reads, Theorem NC gives a noncontextual model for every bijection (MECH-2 :485–507; mathcon1
  `DESIGN.md`:597–627). MECH-2 itself states that Lemma Q's protection is the linear class's native
  instance of the M-INACC pattern (MECH-2 :853–854); the knowledge-balance restriction is symmetric
  between preparation and read.
- **New, conditional [W on R].** Single carrier cell, native `Z`/`X` reads only, class N.
  - *Premises.* H-LIFT. Reachable carrier laws are the uniform, `z`-pair and `x`-pair laws and
    their mixtures. Point laws and `(z+x)`-determined laws are excluded by Lemma Q(iii) under P1–P2
    and by AP1's type grading (MECH-2 :530–534; minacc-1 (s5), `RESULT.md`:118).
  - *Derivation.* The four pair laws span a 3-dimensional `W`, on which `(1, ⟨Z⟩, ⟨X⟩)` is
    injective (checked by hand on the points `(z, x)`). The effects span `W*`. Proposition B then gives
    a simplex-embedded, noncontextual fragment.
  - *Consequence.* This narrows the "undecided at native `Z`/`X`" of OA-1 R6 (OA1r4:439–441) for the
    linear class at one cell. For `G_SM` (P★ reachable) and for multi-cell product reads it stays
    undecided.

#### N2.6 Admissible non-affine rules: open

Candidates: `G_SM` at `q = 2` (MECH-2 :37–47; an SM hypothesis that breaks A5 and the affine form,
a Layer-0 revision under §A.29), and `G_σ` (minacc-1).

| Necessary condition | Source | Status for `G_SM` |
|---|---|---|
| N-a. Non-translational setting dependence of reads | Theorem E | met: the state-dependent graph switches natively ("the selection is ontically in-world", MECH-2 :102–103 [R]) |
| N-b. Non-injective E3 quotient whose identifications are used | Proposition B, Corollary B′ | not shown |
| N-c. Growing carriers, for any exact infinite-order reversible control | Theorem C | — |

**Skeptical reading of the favourable evidence.**

- P★'s "non-stabilizer, non-CP" labels (MECH-2 :80–91) are relative to the frame R1, which is a
  G4-type identification. In E3 they show nothing either way, and they are not counted as evidence of
  richness.
- minacc-1's negative points the other way. Under `G_σ` the gate lets a protocol determine `u + v`
  of an unregistered cell without backaction (`minacc-1-20261108/RESULT.md`:44–63). More access
  pushes `R` toward injectivity.
- ARP-1-MARC's survival concerns the linear rule `N₁` in a finite model with supplied registration and
  P2 (`round-arp1-marc-20261108/result.md`:36–38) [R]. It is not evidence for G3.

**Verdict N2.6: OPEN.**

### N3. Option (iii): other state spaces

- **5c, encoded frames.** These posit a linear identification with operators, a G4-type step.
  - Within their hypotheses, Lemma F, U2 and NC cap them (mathcon1 :597–627 [R]).
  - Not target-neutral unless the identification is derived. An identification that is non-injective
    and restricts reads, such as `U′`, is a supplied version of N2.3's mechanism.
- **5e, amplitude spaces.** Imported (OA1r4:422; `oi-qm-ext-1/two-mode-drive.md`:25–40 [R]).
  Koopman–von Neumann makes G2/G4-style tests non-discriminating (OA1r4:422).
- **5f, infinite lattice.** Not sufficient (OB/QuasilocalCharacterization.lean:792 [K]). For exact G2,
  Theorem C makes growth necessary. For affine rules growth does not help (Theorem E, test 3).

**Verdict N3:** no target-neutral escape beyond N2.

***

## 3. Controls

### 3.1 Classical control: reversible computers with the same kind of interface

| Criterion | Affine classical computer (linear CA) | Fredkin/Toffoli computer, full-access (configuration) interface | Fredkin/Toffoli computer, its own physically restricted interface (`𝔊_K`) | Discriminating? |
|---|---|---|---|---|
| G0 | pass (noise) | pass | pass | **no** |
| G1 | can pass (restricted reachable laws) | fail (simplex) | pass (square) | **no** |
| G2 at fixed `S` | fail | fail | fail (Theorem C) | — (everything fails) |
| G2 with growing carriers | translations only (Theorem E) | — | classical rotor passes | **no** |
| G3 | **fail** (Theorem E) | **fail** (Proposition B; [K] OB/CentralObservation.lean:620, full passive access ⇔ commutative) | **pass** (Claim 2) | discriminates access structures, **not** classical versus quantum dynamics |
| G4 (configuration identification) | fail [K] | fail [K] | fail [K] | not target-neutral |
| G5 (ε) | — | — | the gluing map passes (Main:580), failing non-import (Main:582) | caught only by (d)3–4 |

**Reading.** No target-neutral criterion of single-system richness separates a reversible classical
computer from a quantum-like one, because the computer's `φ` can be designed to supply the access
restriction. This extends OA-1's remark that "the qubit tier tests sourcing, not quantumness"
(OA1r4:466–470) from the qubit tier to G1–G3 [W]. What remains decisive for OI is **sourcing**:
whether OI's own admissible rule produces the restriction, which is items (d)3–4.

### 3.2 Target-neutrality of the definitions

- E1–E3, Lemma 1, Proposition B, Theorem C, Theorem E and G0–G3 use only laws on `S`, response
  functions in `[0, 1]` and convex structure. They use no Hilbert space, no complex amplitude and no
  frame.
- G4 and G5 are listed only to locate the kernel ceiling and the quantum target. No verdict above
  uses them as a criterion for "richer".
- **Countercheck: what if the definitions encoded quantum structure?** Replace E3 by an operator
  identification, as in 5c. "Richer" then becomes frame-relative, and P★ would count. That is the
  representation-versus-mechanism failure the Code Review Rules name; it is avoided here.

***

## 4. Conclusion

| Reading of the question | Verdict | Exact scope |
|---|---|---|
| Deterministic dynamics in general, E3 states, common preparation and readout ((d)1–2 only) | **YES** | `𝔊_K` (exact G1 + G3; premises: designed non-affine `φ` [posit]; uniform bath [native under μ-G, posited otherwise]; ready cells and blanks [MP-0a, resource]; bath longer than horizon [growing carrier]). Main gluing gives ε-G5 with imported data [P]. **Non-discriminating**: a classical computer |
| E1 or E2 with a fixed lift, any rule, any μ | **NO** | Stochastic; reversible ⇒ permutation (Lemma 0, Proposition A) |
| Exact infinite-order reversible emergent control at fixed finite `S` | **NO** | Any rule, interface and μ; trace-preserving only (Theorem C) |
| OI's native rule class | **NO** | (H1) affine, (H2) additive readout, (H3) no supplied non-translational control; every μ for (a), (xiv) for (b); every carrier size (Theorem E) |
| OI-admissible non-affine rules (a Layer-0 revision), or the affine class with supplied P3/E-iso beyond NC's hypotheses | **OPEN** | See below |

**The precise open question.** Does some OI-admissible non-affine rule (e.g. `G_SM` at `q = 2`), with
fixed partition, layout and stated μ, have a closure-defined emergent theory E3 that is not
simplex-embeddable (G3)? If so, does it contain a qubit-type fragment (G5) rather than a gbit, and
does it pass non-import? Necessary: N-a (met by `G_SM`), N-b (unknown), and N-c for exact G2.

**Cheapest decisive next steps.**

1. **Paper-only, within this kind of authorization.** Try to instantiate the `𝔊_K` square witness
   natively in `G_SM`. That means:
   - two switch-selected read functionals `f₀, f₁` of one carrier;
   - four reachable preparations fixing `(f₀, f₁)`;
   - a disturbance making the joint read unavailable under every `G_SM` protocol.

   A single protocol with joint access refutes that shape. minacc-1's gate-cancellation mechanism
   (`RESULT.md`:54–58) is the template to test first.
2. **Computation (needs separate owner authorization).** Exact finite enumeration of the
   closure-defined accessible fragment of a small `G_SM` ring (`L = 5`, `q = 2`, bounded horizon),
   followed by an exact rational simplex-embedding linear program [L: Selby et al., PRL 132, 050202
   (2024)].
   - *Controls, preregistered:* the affine ring `N₁` must return embeddable (Theorem E), and `𝔊_K`
     must return non-embeddable (Claim 2).
   - *Rule:* a verdict prints only over green controls.

***

## 5. Status table

| Item | Status | Support |
|---|---|---|
| Configuration-level ceiling (no phases, not `DerivedOI`, no dense `Fin 2` control; rule-independent) | proved | [K] OB/FrozenSourcing.lean:84, :99, :111, :173, :295, :327; OB/SubstratumInterfaceAudit.lean:780 |
| Full passive access ⇔ commutative | proved | [K] OB/CentralObservation.lean:620 |
| ε-quantum single reversible realization with imported data; finite-carrier obstruction | proved on paper | [P] Main:564–582; Main:558 (half imported) |
| Lemma F, Theorem NC, U2 (frame-relative) | paper records | [R] MECH-2 :307–347, :483–541 |
| Lemma 0, Proposition A (E1/E2 stochastic; reversible ⇒ permutation) | derived here | [W] |
| Lemma 1 (closure ⇒ well-defined E3 operations) | derived here | [W] |
| Proposition B and Corollary B′ (injective ⇒ noncontextual; G3 needs non-injectivity) | derived here | [W], generalizes [R] NC |
| Theorem C (fixed finite `S` ⇒ finite reversible group; G2 needs growing carriers) | derived here | [W]; confirmed by [R] op-quotient v3 |
| `𝔊_K`: exact operational equivalence and preparation contextuality (G1, G3) | derived here | [W]; known pattern [L] |
| Theorem E (affine + H-AR + no supplied control ⇒ single measurement; classical E3; translations) | derived here | [W] on D5 ([R]+[W]) |
| Corollary E1 (non-translational read dependence necessary for G3, given H-AR) | derived here | [W] |
| Corollary E2 (affine, `q = 2`, parity outcomes, (xiv) ⇒ CHSH ≤ 2) | derived here | [W] |
| Class N, one cell, native `Z`/`X`: noncontextual | conditional | [W] on [R] (H-LIFT, Lemma Q(iii), grading) |
| G3 for admissible non-affine rules; qubit-type fragment; non-import | open | [O] |
| Inaccessibility of a used functional under unbounded protocols on a finite bijection (AW-OA2-2) | open | [O] |
| H-AR exit through non-additive partitions (AW-OA2-1) | open | [O] |

***

## 6. §A.31 classification and markers

- **Productivity test, fixed before the chain.** A gem needs a fact strictly stronger than a
  restatement that either constrains something or exposes a hidden assumption.
- **Theorem E: NEW.**
  - It closes OA-1's open row 5d (OA1r4:421) for the native affine class.
  - It shows the gap-2 repair is necessary for gap 3 in E3.
  - It holds under every measure for (a) and at every carrier size.
- **Theorem C: ELABORATING.**
  - It derives carrier-growth necessity for reversible emergent control without Main:558's import.
  - It covers every rule and interface.
- **Universality of `𝔊_K` and §3.1: ELABORATING** of OA1r4:466–470, extended to G1–G3.
- **Proposition B: ELABORATING** of NC: frame-free, and the necessity of non-injectivity holds in E3
  for every rule.
- **Proposition A, Lemmas 0–1: CONFIRMING.**
- **Class-N single-cell result: ELABORATING,** conditional.
- **AW-OA2-1 (H-AR).** Theorem E and Corollary E2 need additive readout. A non-additive observer
  partition is the one native-looking exit. It closes when duplicate copies of a functional are
  available. Watch it in any claim that uses a coarse readout `Y` (e.g. OA-1 D8).
- **AW-OA2-2 (recurrence against permanent inaccessibility).** In `𝔊_K`, exactness needed bath
  length greater than the horizon. M-INACC's "every permitted reuse" clause (MECH-2 :837–838)
  interacts with recurrence (Main:60). Check it before any claim of permanent inaccessibility on a
  finite carrier.
- **AW-OA2-3 (richness is not quantumness).** A G1–G3 success is a statement about access structure.
  Any OI claim of "nonclassical emergent operations" must also pass (d)3–4.
- **Favourable-branch pressure tests.**
  - The YES of N2.3 was tested for leaks (PREP design) and recurrence, and narrowed to bounded horizons.
  - P★ was excluded as evidence, being frame-relative.
  - The N2.6 openness is reported with minacc-1's contrary evidence.
- **Tally:** one NEW (Theorem E). The fixed point has not been reached; this is one pass.

***

## 7. Reading inventory

**At `main` `fb733b4a58558ef64bd7c3585712c76e9f2dfb42`:**

- `papers/Main.md`: :42, :54, :58, :60, :82–92, :97, :147, :358–416 (§3.3, Bell ceiling :364ff., corollary
  :414), :480–482, :552, :558, :564–582, :596, :724 (ledger (ii), (iv), (vii), (xiii), (xiv)).
- Lean statements under `verification/lean-mathlib/OIBridge/`:
  - `FrozenSourcing.lean`: :1–130 and :290–340;
  - `SubstratumInterfaceAudit.lean`: :495–520 and :700–830;
  - `RouteB.lean`: :125–160;
  - `DiscreteCompletion.lean`: :35–60;
  - `CentralObservation.lean`: :605–625;
  - the definition sites from `git grep` (`OperationalAssembly.lean`:594).
- Records under `verification/programmes/oi-qm/reconstruction/`:
  - `mechanism-2-20261108/DESIGN.md`: :1–200, :300–360, :483–545, :700–745, :828–860, and grep of the rest;
  - `mathcon1-polc-20261108/DESIGN.md`: :540–640;
  - `minacc-1-20261108/RESULT.md`: :1–140, and grep of `DESIGN.md`;
  - `round-arp1-marc-20261108/result.md`: :1–111;
  - `observer-interface-obsmu-20261104/ANALYSIS.md`: :885–920;
  - `states-dynamics-audit-20261024/operational-quotient-v3/REPORT.md`: :1–60;
  - `quarter-phase-native-20261107/DESIGN.md`: grep only, for P3 use and the scope of contextuality.

**At OA-1 `066be3b1d321d1a325c3b0a577973102f7d0fbb7`:**

- `OA-1-REPORT-r4.md` (whole);
- `REVIEW-OA-1-r3.md` (whole);
- `REVIEW-OA-1.md` (grep and :205–230);
- `REVIEW-OA-1-r2.md` (grep).

**Not read:**

- MECH-1, apparatus-1, QA bodies, TUNE-1, `two-mode-drive.md` and `whole-model-bridge.md`; these are
  cited only through OA-1 or MECH-2;
- the external literature [L].

Negative claims are limited to these sources.

## 8. Limits

- Every [W] item is an unreviewed hand derivation by one model. None is kernel-checked.
  - Theorem E's (b) carries a spanning qualifier for full simplex-embeddability; preparation
    noncontextuality holds without it.
  - Theorem C is for trace-preserving operations only.
- Theorem E's class is exactly (H1)–(H3), with (xiv) for the operational reading. It does not cover
  non-affine rules, supplied P3/E-iso, non-additive partitions or encoded identifications.
- `𝔊_K` is a designed control. It is not an OI construction and has no bearing on any manuscript
  claim. Its exactness is per horizon.
- The class-N single-cell result rests on [R] premises (Lemma Q(iii), AP1's grading, (s5)) and on
  H-LIFT.
- The external literature is cited from memory as context. Every proof here is self-contained.
- No manuscript claim is affected. Corollary E2 overlaps Main:414's scope and proposes no edit.
- The authorization comment was not re-fetched. Its text is as relayed by the coordinator.
