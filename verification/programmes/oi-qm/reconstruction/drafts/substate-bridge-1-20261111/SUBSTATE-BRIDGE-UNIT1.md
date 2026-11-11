# SUBSTATE-BRIDGE-1, unit 1: can recursive substates supply the missing non-classical component?

**WIP / UNVERIFIED — writer draft r1, pending independent review. Authorizes nothing.** Paper-only unit under the accountable Issue #1169 (owner approval 2026-11-11 in the coordinating session: "Proceed as suggested"). It adopts no physical premise, edits no manuscript or frozen record, runs no OI mechanism and makes no git or GitHub write. Its only computations are the generic exact checks S1–S6 of `probes/generic_substate_checks.py` (run with `python3 -I -B`; 11 lines, all PASS; no OI rule, carrier, coupling or preparation is encoded).

**Corpus pin.** `main` = `cac5d26441dd33e9348151487e4df7b547195481` (2026-11-09). "Main:n" is line n of `papers/Main.md` at that commit (blob `5b73da57…`); "GR:n" likewise (`cd8d16a7…`). "RS/" = `verification/programmes/substratum/recursive-substates/`; "CS/" = `verification/programmes/substratum/continuous-substates/`; "OB/" = `verification/lean-mathlib/OIBridge/`. Lean sources were read; nothing was built.

**Evidence tags.** **[K]** kernel theorem on `main` (statement read, build not rerun). **[P]** paper proof in a manuscript on `main`. **[W]** research record on `main` (author-reported or model review is not verification, §A.46 item 7). **[D]** draft off `main` (§6). **[A]** argument in this file, unreviewed. **[X]** generic exact check in this unit's probe (supports, does not replace, an argument). **[L]** literature recalled, not read first-hand in this unit.

**Inputs under review.** INTERVENE-1 unit 1, draft r2 (PR #1230; its T0–T7, hypotheses P-CONF, H4, H-IND, routes C / E_f / E_r / C-dyn) and Bell-scope unit 1, draft r2 (PR #1231; its class 𝒞_sep, Theorem N/N′, Lemma G, open points O1–O3). Both are [D]. Statements below that depend on them say so.

**Productivity test, fixed before the walk (§A.31).** A result counts only if it is strictly stronger than "an infinite hidden carrier is still classical" and either constrains a route or exposes an assumption that a finite-carrier argument hides. Findings are classified in §4.4.

***

## 0. Verdicts

| Q | Verdict | Status | Decisive lemma or gap |
|---|---|---|---|
| **Q1a** Does T0 (every procedure induces a nonnegative kernel family) survive an infinite, continuum or recursive hidden carrier? | **Yes.** | proved [A] (Lemma E1), conditional on P-CONF∞ (states are probability measures; maps and records measurable), H4, H-IND | E1: the induced object is a Markov kernel `T(s, ·) = κ(s, {r : (f,g)(s,r) ∈ ·})`. No step uses finiteness, bijectivity or an invariant measure. |
| **Q1b** Does the induced class grow? | **No, for a finite identified carrier.** | proved [A; X S1] under the broad preparation form H5 | E1 + saturation: every member of 𝒦 is already induced by a *finite* hidden register, so 𝒦_∞ = 𝒦. T2 and T4 of INTERVENE-1 are statements about 𝒦 on the finite carrier and are unchanged. |
| **Q1c** Does T3 (route E_f) survive? | **Not as an obstruction on the transformation side.** T3's spanning hypothesis forces `|Ω_enc| ≤ d²`, so it has no infinite-carrier instance; without spanning its conclusion is not an obstruction, already for a finite frame. A finiteness-free replacement holds on the measurement side. | counter-structure exact [X S2, S2c]; replacement proved [A] (Lemma E2), conditional on a linear encoding, P-CONF∞, H4, H-IND | E2 (single-POVM lemma): under any linear encoding into laws on any measurable carrier, all native measurements are post-processings of one POVM, hence jointly measurable; two non-commuting sharp measurements are never both native. |
| **Q1d** What changes under trace-out over an infinite hidden factor? | Five named changes (§2.4): no canonical measure; double stochasticity only under an invariant product prior; real, not rational, entries; no forced recurrence; H3 no longer excludes amplitude-valued configuration coordinates. | each proved [A] or sourced [W]; see §2.4 | For profinite towers with continuous dynamics and readouts, every finite-horizon record law equals that of a finite stage (Lemma E3, [A] on the topological lemma of RS/ANALYSIS.md, a paper proof [W]). |
| **Q2a** Do the substate structures defined on `main` supply edges of `G_φ` between distant sites (O1) or within-cone dependence (O2)? | **No.** Every substate construction on `main` is either site-fibred under an unchanged stencil or a single-cell model with no spatial sites. | proved by inspection for the constructions on `main` [A on K, W]; not a statement about every conceivable substate structure | L1 (tower locality): enlarging site alphabets at a fixed stencil adds no edge to `G_φ`; Main's cone lemma uses finiteness of the site set only. |
| **Q2b** What would a native, non-fitted linkage have to be, and which Bell hypothesis would it break? | Four properties N1–N4 (§3.3): a hidden factor that is not site-fibred; a *directed* generator→factor→record path inside the window; masking for a sourced preparation class; a selector for the quantum set. It would break **parameter independence**. A substate used as a common cause of settings and responses would instead break measurement independence; product priors on towers work against that. | N1–N4 each open; none supplied by `main` | L3: a shared factor that both wings read and no setting writes is a common cause and stays Bell-local [A; X S5]. Channel + pad without a selector gives the PR box [X S4]. |
| **Q3** What did F2-1 and the related rounds establish? | F2-1: `INCONCLUSIVE (gap)`, scoped to thirteen screened access rules judged on structure; the gap is the operator condition G★. NATIVE-PADIC-1: no deep-to-low passive backflow for the linear stencil rule under additive alphabet reductions. FIXED-SCALE-1, B1, B2, infinite XOR, solenoid: classical memory or Markov witnesses. None is a no-go; none concerns spatial linkage or Bell. | as recorded on `main` ([K] for the named kernel statements, [W] otherwise; reviews author-reported) | §4.1–4.2 |
| **Q4** Is "substates" (a) unable, (b) a possible carrier with named extra properties, or (c) indeterminate? | **(c) indeterminate for OI itself**, with **(a)** proved on four named classes and **(b)** reduced to seven named properties, none supplied. | see §4.3, §5 | Missing lemma SLL (§4.3): existence, or exclusion by posit (viii), of a native hidden factor that is not site-fibred and carries a directed generator→record path with masked signalling. For the operation component the missing lemma is the already-recorded G★ / L3. |

**What the unit does not show.** It does not show that no extension of OI by substates can source a non-classical operation or a Bell escape. The (a) results cover: single procedures under H-IND on routes C and (linear) E_f; profinite towers with continuous maps at finite horizon; site-fibred towers under a stencil-respecting rule; low-digit readouts under the linear stencil rule. Routes C-dyn and E_r remain undecided, as in INTERVENE-1.

**Favourable-reading check (§A.31).** Two readings favour substates: (i) a continuum carrier can host unitaries as point maps and amplitudes as configuration coordinates; (ii) unresolved depth supplies a natural masking measure. Both are pressure-tested in §2.3, §3.4 and §4.3 and neither survives as a source: (i) is closed on the measurement side by E2 for linear encodings and is "quantum mechanics by fiat" for non-linear ones; (ii) supplies a pad without a channel and, with a channel, over-generates to CHSH = 4.

***

## 1. Definitions and sources: what "substate" means on `main`

No manuscript uses the term: a search of `papers/*.md` and `book/ch*.md` at the pin for `sub-?state` returns one unrelated hit (`papers/Complexity.md:533`, protein conformational substates). Substates exist on `main` only as research records under `verification/`.

| Source | Object | Where | Layer and status on `main` |
|---|---|---|---|
| Main §1.2 | Lemma 1 proves finiteness of the *visible* configuration space; finiteness of the total `S` is a physical posit; the bijective finite representative is a representation choice | Main:48, Main:62; ledger item (ii), Main:726 | [P]; posit |
| GR §3 Step 2 | Deep-sector cardinality is gauge to `O(τ_S/τ_B)` for a slowly coupled deep sector; exact only for a decoupled one; the recurrence proof needs finite `S` | GR:136–142 | [P], conditional on the frozen-deep-sector hypothesis |
| SUBSTATE-1 (Issue #1007) | "each finite site state carries infinitely many internal sub-states below the resolution ε": a **per-site** alphabet extension — real-type (`R/Z` per site value) or p-adic-type (`Z_p` per site value) — under the same lattice wave map, Haar prior | CS/README.md:37–39, :53–56 | [W]; WIP; paper proofs not independently reviewed on `main` (CS/README.md, "Standing of this directory") |
| `ObservableFactorRecurrence` | change event = union of off-diagonal cells, any carrier; identity return + earlier non-permutation ⇒ P-indivisible on that horizon | OB/ObservableFactorRecurrence.lean:48, :68 | [K]; conditional (the measurable realization of Γ is not constructed) |
| `ObservableMeasureReturn` | measured-return matrix = 1 iff visible change has measure zero, any hidden type and measure | OB/ObservableMeasureReturn.lean:63, :83 | [K]; ENNReal ratio matrix only |
| `GradientLinkFlatness` | site-gradient links have zero plaquette curvature; two-slice update is invertible for any `F` | OB/GradientLinkFlatness.lean:27, :39, :47 | [K] |
| SUBSTATE-2 (Issue #1010) | a **nested family of finer internal distinctions**, an inverse limit `K = lim K_n` of finite stages; hypothesis only, "not a statement that physical OI contains fractal internal states" | RS/README.md:3, :7–12 | [W]; hypothesis and preregistered controls |
| Models A, B1, B2, C | odometer on `ℤ_2`; fixed-depth feedback; shift conveyor; four links of one plaquette in `(ℤ_2)^4` | RS/README.md:20–25; RS/ANALYSIS.md:62–175 | [W]; exact finite controls + paper limits |
| Finite-depth theorem | a continuous map from a compact inverse limit of finite sets to a finite alphabet factors through a finite stage; finite-horizon and exact-period corollaries | RS/ANALYSIS.md:14–54 | paper proof [W]; "Lean bridge open" |
| `RecursiveFiniteFactor` | finite-family depth aggregation and the exact-period extension, *assuming* stagewise factorization; hidden-controlled reversible flip | OB/RecursiveFiniteFactor.lean:52, :83, :100 | [K]; conditional by statement |
| FIXED-SCALE-1 | one fixed update `T(a,r,c) = (a⊕r⊕c_0, r, Sc)` on a bi-infinite fair tape; P-divisible two-time law with one bit of three-time memory; "classical"; prior "an explicit physical *candidate prior*, not one OI has selected" | RS/README.md:96–164 | [W]; written infinite proof + finite controls |
| NATIVE-PADIC-1 / `NativePadicReduction` | any additive alphabet homomorphism commutes with the neighbour-sum two-slice step under **one fixed stencil** `neighbors : I → D → I` | OB/NativePadicReduction.lean:32, :56, :66; RS/README.md:167–222 | [K] for coefficient 1; paper for other coefficients [W] |
| F2-1 | preregistered unit on sourcing `rot` and phases from substate access; amendment A★; stage 2 run-2 | RS/f2-1-coherence-sourcing/ | [W], frozen; §4.1 |
| `F2CoherenceControls` | `nonnegClass` is an `Architecture`, `NonnegBounded` and `OnesFixing`; `realClass` has `rot` and not phases; `fullClass` has all three | OB/F2CoherenceControls.lean:123, :173, :182, :306, :317, :343–358 | [K] |
| Infinite-tape XOR; 3-solenoid | P-divisible all-time two-time family with non-Markov three-time law; exactly Markov visible law `Γ_t = P^t` | CS/infinite-xor-counterexample.md; CS/README.md (three-solenoid section) | paper proofs [W], not independently reviewed |

**Reading used below.** A *site-fibred tower* is `S = ∏_{i∈V} S_i` with each `S_i` an inverse limit (or a continuum) and the visible readout a finite-valued function. A *single-cell model* has one visible cell and a hidden tape with no site set. These two shapes exhaust the constructions listed. The corpus sentence closest to this unit's question is CS/equivalence-and-d3-scope.md:137–139: "a hidden continuum alone changes none of Bell's premises" [W].

***

## 2. Q1 — nonnegativity on infinite, continuum and recursive carriers

### 2.1 Which steps of INTERVENE-1 use finiteness

| Step (INTERVENE-1 r2 [D]) | Use of finiteness | Disposition |
|---|---|---|
| H1; definitions of 𝒩 and 𝒦 ("finite Ω") | by definition | replaced by P-CONF∞ below |
| §1.2: "this covers φ⁻¹, since φ has finite order" | **yes** | fails for infinite order. φ⁻¹ becomes a separate generator and must be measurable: automatic for a Borel bijection of a standard Borel space (Lusin–Souslin [L]), a hypothesis otherwise. T0 does not use φ⁻¹. |
| T0: `Σ_r κ(r∣s)…` | sum over a finite `R` | integral against a Markov kernel; needs joint measurability of the maps and records (E1) |
| T0: "the state at the start is the law μ(s)κ(r∣s)" | every finite joint law disintegrates | on general spaces a joint law has a kernel `κ` when the hidden space is standard Borel (disintegration [L]); otherwise `κ` is a hypothesis. Covered by taking `κ` as the datum, as H-IND does. |
| T0: record-dependent stopping time | implicit: the protocol halts | on an infinite carrier a stopping time can be infinite on a set of positive measure. E1 carries a failure outcome ⊥. The same caveat applies to a finite carrier and is not finiteness-specific. |
| T1: generators nonnegative, columns sum to 1 | none | holds for kernels: pushforward by a measurable map, product with a probability measure, restriction to a measurable set, marginalization |
| T2: `w = Σ_s w_s e_s` | finite expansion **on the identified carrier only** | unchanged when the identified carrier is finite (the case in the brief). For an infinite identified carrier the diagonal-matrix formulation does not typecheck (§2.5). |
| T3: `Span(L(states)) = ℝ^{Ω_enc}`; uniqueness of the frame matrix | **yes**: spanning forces `|Ω_enc| ≤ d²` | no infinite-carrier instance; without spanning the conclusion is not an obstruction (§2.3) |
| T4–T7 | the kernel's `FiniteOperationalTheory` is typed over `Fintype` carriers; the hidden carrier does not occur in these statements | unchanged, given faithfulness to 𝒦, which E1 supplies |

### 2.2 Lemma E1 (T0 on an arbitrary measurable hidden carrier) [A]

**P-CONF∞.** `(Ω_S, 𝒮)` and `(R, ℛ)` are measurable spaces; `Ω_S` is the identified carrier (finite with the discrete σ-algebra in the case of the brief), `R` collects every other degree of freedom and may be infinite, a continuum or an inverse limit. `φ : Ω_S × R → Ω_S × R` is measurable for the product σ-algebra. Physical states are probability measures on `Ω_S × R`. Records are measurable coordinates (H4, H6).

**Procedure.** A Markov kernel `κ` from `Ω_S` to `R`, the same for every input law (H-IND); an outcome `a` in a countable alphabet `A`, a stopping time `τ ∈ ℕ ∪ {∞}` and an output configuration, all measurable functions of finitely or countably many records along the trajectory.

**E1.** *Put `g(s,r)` for the outcome, `f(s,r) = π_S(φ^{τ}(s,r))` on `{τ < ∞}`, and ⊥ on `{τ = ∞}`. Then*

`T(s, B × {a}) := κ(s, {r : τ(s,r) < ∞, f(s,r) ∈ B, g(s,r) = a})`

*is a sub-Markov kernel from `Ω_S` to `Ω_S × A`; with the ⊥ outcome added it is Markov. For every input law μ the law of (output, outcome) is `∫ μ(ds) T(s, ·)`.*

*Proof.* `f`, `g`, `τ` are measurable as countable combinations of the measurable maps `φ^t` and coordinate maps, so `E = {τ<∞, f ∈ B, g = a}` lies in `𝒮 ⊗ ℛ`. For a product-measurable set, `s ↦ κ(s, E_s)` is measurable (monotone-class argument, standard). The initial state is `μ ⊗ κ` by H3 and H-IND, the trajectory is a function of `(s,r)`, and the law of `(f,g)` is the pushforward of `μ ⊗ κ`, which is the displayed integral. Values of a measure are nonnegative, and the total mass is `κ(s, R) = 1`. ∎

The proof uses no finiteness, no bijectivity, no invariance of any measure, and no topology. It also holds verbatim for finitely additive states with `κ` a finitely additive kernel, provided the sets involved are in the algebra: positivity does not rest on countable additivity. What it does use: measurability (a non-measurable readout has no law), `κ` independent of the input law (H-IND), and states that are measures (H3).

**Saturation (𝒦_∞ = 𝒦 for a finite identified carrier) [A; X S1].** Let `Ω_S`, `Ω_S'`, `A` be finite. By E1 every procedure with any hidden carrier induces a member of 𝒦. Conversely every member `(T_a)` of 𝒦 is induced with a *finite* hidden register: take `R` = the set of functions `r : Ω_S → Ω_S' × A` with the product prior `ν(r) = ∏_s T(r(s) ∣ s)`, an output register `ℤ_m`, `m = |Ω_S' × A|`, started at 0, and the bijection `(s, r, o) ↦ (s, r, o + r(s))`. The induced kernel is `T` (S1 checks six rational instances exactly, including bijectivity). Hence an infinite hidden carrier adds no single-procedure induced map. With the kernel's narrower preparation (`prepAvail_uniform`, uniform ancillas only) finite registers reach rational entries and an infinite one reaches all real entries; that is the whole difference (§2.4 item 3).

**Consequences for INTERVENE-1 on a finite identified carrier.** T2 (every linear lift of a branch preserves diagonals), T4 (FI-1ᵘ fails in a theory faithful to 𝒦) and the route-C verdict hold with the hidden carrier arbitrary, conditional on P-CONF∞, H4, H-IND. This is a conditional extension of drafts that are themselves [D].

**Relation to F2-1 on `main`.** A★2 item 2 states the operator form of the same fact for a measure-preserving joint process on register × `K`: the induced operator is the compressed Koopman operator or its adjoint transfer operator, "positive and unital Markov operators (standard)", entrywise nonnegative in the computed indicator basis (RS/f2-1-coherence-sourcing/amendments/A-star.md:38–45, frozen [W]); the kernel counterpart for the generated class is `nonnegClass_nonnegBounded` (OB/F2CoherenceControls.lean:173 [K]). E1 is the same statement without measure preservation and for adaptive procedures. So the Q1a answer was already on `main` in operator form for the invariant-measure case.

### 2.3 Route E_f: the spanning hypothesis, two counter-structures, and Lemma E2

**The finiteness-bearing step.** T3 assumes a linear injective `L` with `Span(L(states)) = ℝ^{Ω_enc}`. The states of a `d`-level system span a real space of dimension `d²`, so spanning forces `|Ω_enc| ≤ d²`. T3 therefore cannot be instantiated on an infinite encoded carrier, and its control X5 (a negative entry in the Hadamard's frame matrix) is a property of spanning frames.

**Counter-structure 1 (finite, non-spanning) [X S2c].** Octahedral frame for a qubit: `Ω_enc` = the six axis points, `L(ρ)(k) = (1 + r·n_k)/6`. `L` is linear and injective and does not span `ℝ⁶`. The Hadamard rotation `(x,y,z) ↦ (z,−y,x)` permutes the six points, so it acts on the frame by a permutation matrix, a member of 𝒦, although its conjugation does not preserve diagonal matrices. For comparison the spanning tetrahedral frame gives a frame matrix with minimum entry −2/5 for a rational rotation [X S2b].

**Counter-structure 2 (continuum) [X S2].** Husimi frame for a qubit: `Ω_enc` = the unit sphere, `L(ρ)` has density `1 + r·n` for normalized area. It is linear, injective and nonnegative, and conjugation by any unitary acts by the point map `n ↦ Rn`: `Q_{UρU†}(n) = Q_ρ(Rᵀn)`. Every unitary is then induced by a measurable area-preserving bijection of the carrier.

So on route E_f without spanning, "the induced encoded map has a nonnegative frame representative" does not separate classical from non-classical transformations; the class INTERVENE-1 calls classical on E_f is frame-relative. On a profinite (totally disconnected) carrier counter-structure 2 is not available continuously: a continuous action of a connected group on a totally disconnected space is trivial (compare RS/ANALYSIS.md:169–175 on homomorphisms). It is available measurably, through a Borel isomorphism that respects no finite stage — the readouts excluded by RS/ANALYSIS.md:28–30 from the finite-depth theorem.

**Lemma E2 (single-POVM lemma; finiteness-free) [A].** *Let `L` be a linear map from the density matrices of a `d`-level system into the probability measures on a measurable space `(Ω_enc, Σ)`. Assume P-CONF∞, H4 and H-IND with the encoded carrier as identified carrier (the role of H-LIFT). Then:*

1. *`E(B)` defined by `tr(ρ E(B)) = L(ρ)(B)` is a POVM on `Ω_enc`.*
2. *Every native procedure with outcome alphabet `A` has statistics `p(a∣ρ) = ∫ k_a dL(ρ)` for measurable `k_a : Ω_enc → [0,1]` with `Σ_a k_a = 1`; its effects are `F_a = ∫ k_a dE`.*
3. *Any two native procedures are jointly measurable, with joint POVM `M_{ab} = ∫ k_a k'_b dE`.*
4. *If the effects of two native procedures are all projectors, they commute.*

*Proof.* (1) `ρ ↦ L(ρ)(B)` is linear with values in `[0,1]`, so it is `tr(ρ E(B))` for a unique `0 ≤ E(B) ≤ 1`; σ-additivity of `E` follows from that of `L(ρ)`. (2) E1 with outputs discarded: `k_a(ω) = T(ω, Ω × {a})`. (3) `M_{ab} ≥ 0`, `Σ_b M_{ab} = F_a`, `Σ_a M_{ab} = F'_b`. (4) If `F_a = P_a` is a projector then `0 ≤ M_{ab} ≤ P_a` gives `P_a M_{ab} = M_{ab} = M_{ab} P_a`; summing over `a` after multiplying `Q_b = Σ_{a'} M_{a'b}` by `P_a` gives `P_a Q_b = M_{ab} = Q_b P_a`. ∎

Hence under any linear encoding, on any carrier, two non-commuting sharp measurements (σ_z and σ_x of a qubit) are never both native; in the Husimi frame no native readout is sharp at all (an effect `m(B)·1 + v·σ` with `|v| ≤ 1/4 < 1/2`; S3 checks the tetrahedral analogue exactly). This is the known trade-off that a quasi-probability representation of quantum theory has negativity in states or in effects (Spekkens 2008; Ferrie–Emerson [L]). E2 replaces T3's role without a finiteness or spanning hypothesis: on route E_f the missing component is a pair of incompatible sharp measurements with their update rule, not a transformation.

### 2.4 What changes when the visible law is a trace-out over an infinite hidden factor

1. **No canonical measure.** A finite bijection preserves the counting measure. An infinite one need not have an invariant probability measure (translation of `ℤ`), and when it has one it need not be unique. Lemma 3's selected measure (Main:56) has no general analogue; the hidden prior becomes an irreducible realization datum. The models on `main` pin Haar or product-fair measures by choice (CS/README.md:56; RS/README.md:160–162).
2. **Double stochasticity is conditional.** With `μ_V` uniform on a finite `V` and a hidden law `μ_H`: `Σ_i T_ij = |V| · (μ_V ⊗ μ_H)(φ⁻¹({x_j} × H))`, which equals 1 when `φ` preserves `μ_V ⊗ μ_H` and need not otherwise [A; X S6 for the finite illustration]. The doubly stochastic scope of Main's determinism argument (Main:62) therefore carries the invariance of the product prior as a hypothesis on an infinite carrier.
3. **Real entries.** Under the counting measure every probability is a ratio of counts. With a continuum hidden factor every real value in `[0,1]` occurs, so targets with irrational entries can be met exactly; the aside in Bell-scope §4.4 on rationality then does not apply. No bound in either draft uses rationality.
4. **No forced recurrence; exact Markov laws exist.** `Γ_L = I` is forced on a finite carrier and not on an infinite one: infinite-tape XOR is P-divisible at all times with a non-Markov three-time law, the shift conveyor is iid, the 3-solenoid is exactly Markov ([W], paper proofs not independently reviewed). The all-time classification `finiteRootedRealizable_iff_pper` is a finite-realization statement (F2-1 preregistration, §1 table). The kernel keeps the conditional form: identity return plus an earlier non-permutation gives P-indivisibility on any carrier (OB/ObservableFactorRecurrence.lean:68 [K]). An infinite hidden carrier thus removes a guaranteed source of P-indivisibility; it does not add a non-classical one. H-IND also becomes harder to meet across steps: with unbounded hidden memory the conditional law of the hidden factor given the carrier depends on the history indefinitely (FIXED-SCALE-1: one bit of three-time memory under a P-divisible two-time law), which is route C-dyn. E1 still applies to the protocol as one procedure from its start, and the complete record law is a probability measure on record sequences.
5. **H3 stops excluding amplitude-valued coordinates.** On a continuum carrier a normalized amplitude vector can itself be a configuration coordinate (`Ω` ⊇ projective Hilbert space, `φ` the unitary action — the classical-Hamiltonian formulation of quantum dynamics, Kibble 1979 [L]). "States are probability laws" then no longer implies "no amplitude-bearing state"; on a finite Ω it does, because projective space is uncountable. No fixed finite carrier reproduces "the entire exact continuum operational theory of even a qubit at all preparations/effects and all precisions" (Main:564, the classical-dimension obstruction [P]; the ontological-model form is Hardy 2004 [L]), so an infinite carrier is *necessary* for an exact register encoding over the full menu (route E_r), and a finite carrier gives the bounded-menu, finite-accuracy form Main states there. This is a statement about representability. It supplies no operation: the encoding is non-linear in ρ or unsharp (E2), the composite amplitude space is not a product over sites (it conflicts with ledger (viii), Main:726), and the unitary action and the Born measure are then posits (INTERVENE-1's Q1a/Q1b, scored "QM by fiat").

**Lemma E3 (finite-depth reduction for profinite towers) [A on W and K].** *Let the total space be a compact inverse limit of finite sets, with every map of a protocol (dynamics, register couplings) continuous and every record a continuous finite-valued function. For each finite horizon there is a finite stage `N` such that the complete record is a function of the stage-`N` projection of the initial state; the record law is that of the finite set `K_N` under the projected prior.* By the topological lemma and finite-horizon lemma (RS/ANALYSIS.md:14–38, paper proof) with the aggregation `finite_horizon_depth_bound` (OB/RecursiveFiniteFactor.lean:52 [K], conditional on stagewise factorization). Under a common exact visible period one stage serves all times (`all_time_depth_bound_of_exact_period`, :83 [K]). So for recursive substates in the sense of SUBSTATE-2, with continuous access, Q1 reduces at every finite horizon to the finite-carrier case that INTERVENE-1 treats. Depth can matter only through a non-continuous (threshold-type) readout or coupling, or at infinite horizon.

### 2.5 Infinite identified carrier (outside the brief; stated for scope)

If the identified carrier is itself a continuum, a non-atomic law is not a diagonal density matrix (a trace-class operator commuting with a non-atomic `L^∞` is zero), so route C's formulation has to be restated on the abelian algebra `L^∞(Ω_S, m)`. E1 gives the kernel form: the induced map on measures is positive, and its dual on bounded measurable functions is positive and unital. A lift statement analogous to T2 was not proved here; it would need a continuity (normality) hypothesis on the lift.

***

## 3. Q2 — can substates link separated regions?

### 3.1 What the definitions on `main` give

**L1 (tower locality) [A].** *Let `S = ∏_{i∈V} S_i` with `V` finite and the `S_i` arbitrary sets, and let `(φ(s))_i` depend only on `(s_j)_{j ∈ N(i)}` for a stencil `N`. Then the dependency graph of `φ` is contained in the stencil graph, and `(φ^k(s))_i` depends only on the stencil ball of radius `k`.* Main's cone lemma argues by changing one site component at a time; it states that "finiteness of `V` is used in the first step" (Main:364) and does not use finiteness of the `S_i`. Replacing each finite site alphabet by a tower or a continuum at a fixed stencil therefore adds no edge and leaves the cone unchanged.

Instances on `main`:
- **SUBSTATE-1** refines each site value to `R/Z` or `Z_p` under the same lattice wave map (CS/README.md:53–55). Site-fibred; stencil unchanged.
- **NATIVE-PADIC-1.** `waveStep` is defined for one stencil `neighbors : I → D → I` and any additive alphabet (OB/NativePadicReduction.lean:32); `project_waveStep` (:56) shows every additive reduction commutes with it. The lifted map has the stencil's dependency graph at every level, and, more strongly, a readout that factors through a fixed low quotient evolves autonomously: for such a readout the deeper digits are not even a hidden variable.
- **Models A, B1, B2, FIXED-SCALE-1, infinite XOR, solenoid.** Single-cell: one visible cell and a hidden tape or digit string; no site set, no spatial graph. Their "depth" is not a spatial direction.
- **Model C** and the gauge-pointer toy (CS/shared-gauge-pointer-candidate.md). Links of one plaquette joining adjacent vertices; local. The toy is "an explicit addition to the microscopic model, not an implementation of the OI cubic wave update".

No record on `main` defines a substate shared between non-adjacent sites, a level whose variables belong to a block of sites, or a substate-mediated long edge. The records that mention Bell in this programme decline the claim (RS/fixed-scale-skew/PREREGISTRATION.md:104–107; RS/native-padic-bridge/REPORT.md:186–189; RS/ANALYSIS.md:217–226; CS/equivalence-and-d3-scope.md:137–139). Search performed: `bell|nonlocal|entangl|spacelike|distant|long edge|coupling graph|signal` over RS/ and CS/, and `sub-?state` joined with `bell|wing|remote|shared|two-system|distant|nonlocal|long edge|entangl|pair` over `verification/programmes/oi-qm/` at the pin; the only joint hit is a citation of F2-1 A★ in `oi-qm-ext-1/pair-operation-source.md:48`.

**L2 (Bell ceiling with site-fibred towers) [A on D].** In Theorem N/N′ of Bell-scope, steps 1–2 are pointwise in the pre-setting state and step 4 is pointwise in Ω; step 3 is a mixture over the law of Ω. With each `S_i` a measurable space and the records measurable, the sum becomes an integral and nothing else changes (Bell's theorem for a general measurable λ is standard [L]). By L1 the hypothesis (Sep) is the same condition for the tower as for its finite-alphabet counterpart. So a site-fibred tower under a stencil-respecting rule belongs to 𝒞_sep whenever the finite model does, and the bound `ε ≥ (√2−1)/4` applies to it. This depends on Theorem N, which is [D].

**O1 and O2 for the constructions on `main`.** O1: no edge supplied (L1). O2: the graph cone is a property of the stencil and is unchanged; the long-wavelength speed is a property of the linear rule, which the per-site lifts keep. Whether the native rule yields Bell-relevant dependence in the window between the two speeds is as open as in Bell-scope; substates neither supply nor exclude it. O3 is discussed in §3.5.

### 3.2 L3: a shared factor is harmless unless a setting writes it [A; X S5]

Main's `G_φ` is "symmetrized for the spatial graph" (Main:364), and Bell-scope's (Sep) uses that symmetrized distance. The induction in the cone lemma is directed: output `i` depends on the inputs that have an edge *into* `i`. Let `M` be a hidden factor read by both wings (edges `M → R_A`, `M → R_B`). If there is no directed path from `G_B` to `R_A^t` of length at most `t − t_s`, then step 1 of Theorem N goes through with directed distance, `M`'s content at `t_s` is part of Ω, and the conclusion is unchanged: `M` is a common cause. S5 checks 300 random response tables with a shared mode and correlated priors: `|CHSH| ≤ 2` in each.

Two consequences. (i) A shared, static or autonomously evolving substate — B1's static bit, a conveyor of fresh digits delivered to both wings — cannot produce a Bell violation, however deep. (ii) Bell-scope's statement that a wing–mode–wing path "breaks (Sep) at graph distance ≤ 2" is correct for (Sep) as written, but parameter independence fails only if the path is directed generator → mode → record. (Sep) is sufficient, not sharp; this is a remark for that draft's review, not a correction made here.

### 3.3 What a native, non-fitted linkage would have to be

| # | Property | Why it is needed | Status on `main` |
|---|---|---|---|
| **N1** | A hidden factor `M` that is not site-fibred: one substate object adjacent to both wings, for example a level-`n` variable belonging to a block of `2^n` sites (hierarchical or ultrametric adjacency), or a deep mode common to a prepared pair | L1: site-fibred factors add no edge | not defined anywhere; conflicts with ledger (viii) as stated (Main:726) unless `M` is counted as a site, and then with (x) on the reference class unless it is preparation-indexed, which is H-Bell (i) (`papers/Substratum.md`:131–133), open |
| **N2** | A directed path `G_B → M → R_A` inside the record window: the remote setting *writes* `M` and the near wing *reads* it | L3 | not supplied; the only level-mixing coupling on record is the explicitly non-native mutant (RS/README.md:196–199), and it is single-cell |
| **N3** | Masking: complete-history no-signalling for the physically preparable class 𝒫 | N2 is a signal-capable ontic channel | not supplied. By the preparation-span diagnostic (`oi-qm-ext-1/prepared-pair-source.md` §5 [W], finite Λ), 𝒫 cannot have full affine span; the restriction needs a reason independent of the target table |
| **N4** | A selector: the mechanism yields CHSH in `(2, 2√2]` and not more | channel + pad alone is the PR box [X S4] | not supplied; Main:362 records the same over-generation for the unrestricted construction |

**Which Bell hypothesis.** With N1–N2 and measurement independence kept, the failed hypothesis is parameter independence — Main's adopted option (a) (Main:414). Outcome independence is automatic under determinism. If instead a substate were a common cause of a setting generator and the response-relevant variable, the failed hypothesis would be measurement independence, Main's option (b), "recorded, not adopted" (Main:418), with the necessary cost `I_ont ≥ 0.0309` bits.

### 3.4 Complete-history no-signalling: general argument, and the pad reading

At fixed λ, N2 makes wing A's complete history a function `h_A(λ, a, b)` that depends on `b`. No-signalling requires, for every `a`, `b`, `b'` and history `h`: `μ{λ : h_A(λ,a,b) = h} = μ{λ : h_A(λ,a,b') = h}` for every preparable μ. These are linear constraints on μ. If they hold on a class containing all finitely supported laws they hold at each point mass, so `h_A` does not depend on `b` and N2 is void (the infinite-carrier form of the diagnostic cited at N3; for a class that is only weak-* dense the implication is not automatic, since history indicators are not continuous — not proved here).

**A sufficient native-looking condition (PAD).** For every `b, b'` there is a μ-preserving bijection `σ` of the hidden space with `h_A(σλ, a, b') = h_A(λ, a, b)`: the remote setting acts on the near history only through a measure-preserving relabelling of substates that A cannot resolve. A tower offers a candidate reason: an observer of finite resolution (Lemma 1) cannot prepare digits below its resolution, so its preparable laws are Haar on the unresolved depth. That reason is independent of the Bell table, which is what the diagnostic asks for.

**Pressure test of the pad reading.**
1. (PAD) is sufficient, not necessary, and is a property of the pair (response map, measure). With a biased pad the same channel signals [X S4, countercontrol]; so the claim rests on the Haar prior on unresolved digits, which the records call a candidate prior "not one OI has selected" (RS/README.md:160–162).
2. A pad without a channel is a common cause (L3; [X S4, countercontrol]). Substates on `main` supply pads in abundance and no channel.
3. Channel + fair pad gives CHSH = 4 with exact no-signalling [X S4]. Nothing in the tower structure selects `2√2`; N4 is a separate requirement.
4. The pad must not be readable later by the same wing, or the wing learns the remote setting: a reuse constraint over complete histories and continuations. The shared-parity candidate on `main` is reported by Bell-scope as having reuse signalling (`oi-qm-ext-1/two-system-interface.md` [W], not re-read here).
5. The masking is resolution-relative: an observer resolving one more level reads the pad. That is a definite consequence (signalling at finer resolution), but with an unbounded tower the level at which it appears is a free parameter.
6. GR's deep-sector corollary (GR:136–142) makes a slowly coupled deep sector invisible to the visible transition data up to `O(τ_S/τ_B)`. Substates that carry an `O(1)` Bell-relevant response cannot sit in that frozen deep sector; they would have to belong to the boundary-coupled sector, or the corollary's frozen-sector hypothesis would fail for them.

### 3.5 O3: substates and measurement independence

Under a product prior on a tower, digits at disjoint coordinates are independent, and a conveyor (model B2) delivers fresh fair digits at every step. Setting generators fed by such digits satisfy the conditioning-factorization condition of Bell-scope's Lemma G whenever the conditioning event factorizes across the generator coordinates and the rest. Substates therefore make measurement independence easier to satisfy, which strengthens the obstruction rather than the escape. This is conditional on the product prior (a posit) and inherits Lemma G's open point: an observer's actual record conditioning need not factorize.

***

## 4. Q3 and Q4

### 4.1 What F2-1 and the related rounds established, for which class

| Round | Result | Class it covers | Layer; review status as recorded |
|---|---|---|---|
| **F2-1 stage 1 (A★)** | no admissible `Θ★` among thirteen candidates: Θ-A, Θ-K, Θ-F, Θ-D and N1–N9 (amplitude embedding, √μ with phase digits, level-mixing rule change, generator lift, SU(2) lift, unistochastic lift, polar factor, linear-field lift, holonomy twist). "No `R`, `R†`, `P`, Gate 4 or Gate 5 quantity was computed on any candidate" | the listed candidates, "judged on structure" (A★4 Scope); "It is not a theorem about every conceivable rule" (A★6) | frozen [W]; A★:9, :17, :186–188, :341–343 |
| **A★2** | for a classical `(K, T, μ)` and a coupling that records set membership, the induced-operator rule is the Koopman-indicator baseline: positive, unital, nonnegative in the computed basis. A differing rule needs (i) structure on `K` the measure algebra does not carry, (ii) a non-indicator readout, or (iii) a function of the baseline that no stated process executes | rules of induced-operator form; "decides neither `R` nor `P`" for any theory | paper argument, frozen [W]; A★:29–60 |
| **G★ (A★4)** | the gap as an operator condition, five items; the difference must lie in the coupling `C`, not in structure on one `K`, for the candidate to be transplantable | names what is missing; "This is not a no-go" | frozen [W]. Item 2's necessity claim is refuted in part for the gauged ones-fixing clause (RS/README.md:241–266; `PC1Controls.gauged_rot_mem_onesClass` [K]); the token is unaffected |
| **F2-1 stage 2, run 1** | `INCONCLUSIVE (void)`: build failed | — | RS/README.md:227–234 |
| **F2-1 stage 2, run 2** | `INCONCLUSIVE (gap)`: controls C1–C10 return their reference values, mutations caught, 19 fixed-statement declarations built; "No admissible access rule exists among the 13 candidates screened in stage 1. That is the extent of the result." | controls only; no candidate | [K] for the declarations; token by frozen rule; independent review author-reported, reviewer identity unresolved (run-2/RESULT.md:121–131) |
| `F2CoherenceControls` | `rot` leaves both the nonnegative and the ones-fixing invariant; a class of nonnegative matrices times scalars of modulus ≤ 1 generates a theory with neither `rot` nor phases; real matrices give `rot` without phases | architecture-generated finite theories | [K] |
| **NATIVE-PADIC-1** | "narrow passive low-digit NO-BACKFLOW": reduction mod `2^m` commutes with the linear stencil step and inverse; a deliberately non-native bit-1 kick breaks it | the integer-coefficient cubic stencil rule over compatible `ℤ/2^n` alphabets, passive congruence readouts. Not covered: threshold or non-congruence readouts, level-mixing interactions, the nonlinear native-Y rule, gauge links, the observer-level real lift, Bell, C4 (REPORT.md:177–189) | [K] coefficient 1; paper otherwise; review author-reported |
| **Models A, B1, B2, C; FIXED-SCALE-1; matched control** | classical: permutation readout (A); one bit of memory at a chosen depth (B1); iid without return (B2); non-flat profinite abelian holonomy without action or instrument (C); one fixed rule with unbounded depth access and one bit of three-time memory (FIXED-SCALE-1) | the stated models with their pinned priors | exact finite controls + written limits [W] |
| **PC-1** (physical coupling, related round) | strict token `INCONCLUSIVE (void)`; a scientific finding carried under an owner exception: no admissible candidate among 25 screened, "It is not a no-go" | as its PC★4 states | [W]; header of `physical-coupling-pc1/stage2/run-2/RESULT.md` read only |

**Negative results, at their scope.** (1) Passive congruence readout under the linear stencil rule cannot see deeper digits. (2) Induced-operator rules for classical substate dynamics with indicator readouts are nonnegative. (3) Thirteen named access rules fail the admissibility screen or lack a stated physical justification. Nothing on `main` rules out substates as a class, and each record says so.

### 4.2 What remains untested (from the records and from this unit)

- The nonlinear native-Y rule and any level-mixing interaction on a tower.
- Threshold or other non-continuous readouts of real-type or p-adic substates; an interacting map on real-type substates (CS/README.md, "Reading").
- A non-indicator readout with a stated process; a coupling-level access principle transplantable to any `K` (G★ items 1, 3 and the transplant requirement). N7 (polar factor) passes the numbered screen items and was rejected on justification only; A★6 leaves it to a reviewer.
- Any composite or two-copy property (Gate 5b, local tomography), named and never run.
- Measure selection on an infinite `K` beyond the control measures (Gate 3).
- Routes outside the induced-operator form: memory outside the identified carrier (C-dyn) and non-linear register encodings (E_r); the Kochen–Specker model enters F2-1 only as control C10, whose scope "is recorded, not tested".
- **Everything spatial.** No record tests a substate structure across two sites, a shared or block-level substate, a Bell protocol, or no-signalling for a substate-mediated coupling. Q2 is untouched by F2-1 and its siblings.

### 4.3 Q4: synthesis

**(a) Unable, with reason — four classes.**
1. *Single procedures under H-IND, routes C and linear E_f, any hidden carrier.* E1 and saturation: the induced class is 𝒦, unchanged; E2: under a linear encoding no two incompatible sharp measurements are native. Conditional on P-CONF∞, H4, H-IND.
2. *Profinite towers with continuous dynamics and readouts, any finite horizon.* E3: record laws equal those of a finite stage. Conditional on the topological lemma (paper proof on `main`).
3. *Site-fibred towers under a stencil-respecting rule, for Bell.* L1, L2: no new edge; the restricted obstruction of Bell-scope applies unchanged. Conditional on Theorem N [D] and on that draft's hypotheses (Sep, GI or MI*, MI, every-run outputs).
4. *Low-digit readouts under the linear stencil rule.* `project_waveStep` [K]: deeper digits do not influence them at all.

**(b) Possible carrier only with named extra properties.** For the Bell component: N1–N4 (§3.3). For the operation component: R1 a non-indicator readout or a non-linear encoding on a connected continuum (route E_r; a continuum is necessary for exactness, §2.4 item 5); R2 a sourced state-update consistent across preparations and complete records; R3 a level-mixing rule or non-continuous access, so that E3 does not apply. Each is scored in §5. None is supplied by `main`, and none is adopted here.

**(c) Indeterminate for OI itself.** The classes in (a) do not exhaust "substates": a non-site-fibred factor, a non-linear encoding and a history-dependent hidden memory are each outside them, and nothing on `main` defines or excludes them.

**Missing lemma (SLL, substate linkage lemma).** *Either (existence)* a native rule on a carrier containing a hidden factor `M` that is not site-fibred, such that: (i) some physically separated every-run Bell protocol has a directed path generator → `M` → remote record inside its window; (ii) complete-history no-signalling holds for a preparation class with a stated resolution-based reason; (iii) CHSH exceeds 2 and is bounded by `2√2` by the mechanism; (iv) on the reference class the rule reduces to the stencil rule with its dispersion and area-law controls. *Or (exclusion)* every hidden factor admissible under the ledger is site-fibred — posit (viii) read as covering all hidden degrees of freedom — which with L1 and L2 would extend class (a)3 to all substates and leave Bell-scope's O2 and O3 as the only open points. The text of (viii) ("the configuration space is identified with a product of local configuration spaces over a set of sites", Main:726) reads as the exclusion; Main §3.3(a)'s preparation-indexed long edges are compatible with it only as edges between sites. Whether (viii) is meant to bind a deep hidden sector is an owner question, parallel to Bell-scope's finding F1 on (x).

For the operation component the missing lemma is already recorded on `main` as G★ (A★4) and L3; this unit adds no new one, only that E1 extends its premise beyond measure-preserving processes and E2 states its measurement-side form.

### 4.4 Findings (§A.31 classification)

| # | Finding | Class | Assumption-watch marker |
|---|---|---|---|
| G1 | T3's spanning hypothesis is the step that carries finiteness; on non-spanning frames (finite octahedral, continuum Husimi) non-diagonal-preserving unitaries have nonnegative frame maps, so E_f's "classical class" is frame-relative; the obstruction is on the measurement side (E2) | NEW | any verdict "NX-1 fails/holds on E_f" must state whether the frame spans |
| G2 | `G_φ` is symmetrized, the cone lemma is directed; a shared factor that no setting writes is a common cause (L3). (Sep) is sufficient, not sharp | NEW (for Bell-scope) | "a path through a shared mode" is not by itself a failure of parameter independence |
| G3 | On a continuum carrier, "states are laws" does not imply "no amplitude-bearing state"; what excludes entangled amplitude vectors as configurations is site factorization (viii), not H3 | NEW | P-CONF's H3 clause is cardinality-dependent |
| G4 | 𝒦_∞ = 𝒦: an infinite hidden carrier adds no single-procedure map (E1 + saturation) | ELABORATING (INTERVENE-1 §6 anticipated T1's extension) | — |
| G5 | A★2 on `main` is the invariant-measure operator form of E1 | POSITIVE (validates the inheritance) | — |
| G6 | Profinite + continuous ⇒ finite stage at finite horizon (E3) | ELABORATING (assembles two results on `main`) | "infinite depth" matters only through non-continuous access or infinite horizon |
| G7 | Unresolved depth as masking measure: a pad without a channel; with a channel, PR | BORDERLINE (a candidate reason for N3, nothing more) | masking arguments must exhibit the channel and the selector separately |

Correctness bands unchanged: every result here is on the consistency axis (§A.23).

***

## 5. §A.29 table for the named extra properties (none adopted)

**Controls any revision must preserve, stated in advance.** (c1) `S ⇔ D ⇔ Q_fb` at the finite-law level (Main §3.4; `finite_horizon_equivalence` [K]). (c2) Lemma 1: finite visible configuration space. (c3) Main's Bell ceiling theorem and Corollary at their scope (Main:366–416). (c4) NATIVE-PADIC-1 no-backflow for the linear stencil rule [K]. (c5) The stencil rule's dispersion, isotropy and the area-law derivations on the reference class (SM §3.1, §4.1). (c6) GR's deep-sector corollary at its scope (GR:136–142). (c7) Operational no-signalling over complete histories. (c8) The F2-1 control classifications C1–C10.

**Columns.** *P*: controls preserved. *I*: an independent prediction or postdiction beyond the problem it is built to fix. *V*: can it be adjusted to fit any outcome.

| ID | Property | Status | P | I | V | Score |
|---|---|---|---|---|---|---|
| N1 | hidden factor not site-fibred (block-level or pair-common substate) | open; not defined on `main`; in tension with ledger (viii) as written | (c1), (c2), (c4), (c8) untouched; (c3) leaves its scope by construction; (c5), (c6) at risk: a block-level adjacency changes graph distances (logarithmic in separation for a binary hierarchy) and so the boundary counts and the cone | a hierarchical adjacency would give a definite, direction-independent super-wave cone and scale-indexed correlations; none derived | the hierarchy's branching, depth-to-distance map and membership are free | fails as stated; scorable only once one hierarchy is fixed from native data |
| N2 | directed write–read path generator → `M` → remote record | open; only a non-native single-cell mutant exists | breaks (c3)'s hypothesis (ii)/(iii) by design; (c4) must still hold for the linear rule, so the coupling is necessarily non-linear or non-congruence | none stated | the coupling function is free | fails; it is the Bell channel by fiat until derived from the rule |
| N3 | masking by Haar measure on unresolved depth (PAD), with a single-use constraint | open; candidate reason (finite resolution) is independent of the Bell table | (c7) is its purpose; (c2) is its premise; (c6) requires the masked substates to lie outside the frozen deep sector | yes, one: signalling for an observer of finer resolution, or for non-Haar preparations of the unresolved digits | the resolution level at which signalling appears is unbounded in a tower: adjustable unless the depth scale is fixed independently | the most hard-to-vary of the four; insufficient alone (pad without channel is local; S4, S5) |
| N4 | selector bounding CHSH by `2√2` | open; nothing supplied | (c3) | reproducing Tsirelson's bound is a postdiction (known value), consistency axis only | — | not scorable: no candidate |
| R1 | non-linear (ψ-ontic or ψ-epistemic) register encoding on a connected continuum, or a non-indicator readout with a stated process | open; = INTERVENE-1 route E_r / F2-1 G★ item 3 | (c1) for the laws it represents; (c2) kept if the readout is finite-valued; conflicts with (viii) for composites | none; an infinite carrier is necessary for exactness over the full menu (Main:564) but that is a requirement, not a prediction | the encoding, the group action and the equilibrium measure are free | fails hard-to-vary as stated ("QM by fiat" on a continuum); open only with a selection rule |
| R2 | sourced state-update, reusable across preparations, contexts and complete records | open; INTERVENE-1 Q6's sourcing demand | — | — | — | not scorable: no candidate |
| R3 | level-mixing or non-continuous access, so that E3 and (c4) do not confine depth | open; NATIVE-PADIC-1 option (a)/(b); mutant is non-native | (c4) preserved only if the mixing is not the linear rule; (c5) at risk | discrete-scale (log-periodic) signatures are named as "an explicit falsifiable future target, not a prediction" (RS/README.md:46) | scale `b`, coupling and readout "are precisely the fit freedom" (RS/ANALYSIS.md:196–198) | fails as stated; the records already say so |

No row meets all three §A.29 requirements. N3 is the only one with an independent reason and an own consequence, and it supplies masking only.

***

## 6. Off-`main` references (§A.42 item 8)

Nothing in this file lands. If it ever does, each gap below closes first.

| Reference | Claim it is attached to | Classification |
|---|---|---|
| INTERVENE-1 unit 1 r2, `INTERVENE-UNIT1.md` (blob `06f148e0…`) on `research/intervene-1-20261111` at `e1534b08…`, PR #1230 | the hypotheses P-CONF, H4, H-IND, H5; routes C, E_f, E_r, C-dyn; statements T0–T7; the question Q1 | **support off `main`: gap.** E1 re-proves T0 independently and does not use its proof. The Q1b consequences (T2, T4 unchanged) and G1 (about T3) are statements about that draft and stand or fall with its acceptance (§A.46 item 7). |
| Bell-scope unit 1 r2, `BELL-SCOPE-UNIT1.md` (blob `5814e479…`) on `research/bell-scope-868-20261111` at `ea12fde1…`, PR #1231 | 𝒞_sep, (Sep), Theorem N/N′, Lemma G, O1–O3, the constant `(√2−1)/4`; L2, L3, §3.5 | **support off `main`: gap.** L1 rests on Main:364 [P] alone. L2 depends on Theorem N. L3's common-cause core is the standard Bell argument and is checked generically (S5). |
| Issues #1007, #1010, #1015, #1169; closed PRs #1009, #1011, #1016 (bodies read through the host API, 2026-11-11) | routing; the status of SUBSTATE-1/2; the owner-recorded observer-relative finiteness formulation in #1016's body | **provenance.** No claim uses them: the finiteness split is cited from Main:48, :62, :726 on `main`. |
| Literature [L]: Hardy (2004, ontological excess baggage); Spekkens (2008) and Ferrie–Emerson (negativity in quasi-probability representations); Kibble (1979); Kochen–Specker (1967); Lusin–Souslin; disintegration of measures; Bell's theorem for measurable λ | §2.3 closing remark; §2.4 item 5; §2.1 rows 2–3; L2 | recalled, none read first-hand. **Provenance** for Spekkens / Ferrie–Emerson, Kibble, Kochen–Specker (E2 and S2 are self-contained). Hardy's theorem is cited beside Main:564, which carries the necessity claim on `main`: provenance. **Support off `main`: gap** for the standard measure-theoretic facts in §2.1 (Lusin–Souslin, disintegration) and for Bell's theorem with a measurable λ in L2; each is labelled where used. |
| `probes/generic_substate_checks.py` (sha256 `fbee6ec5…1970`), `probes/generic_substate_checks.out` (sha256 `9fa91e5c…0ff9`), this directory | [X] tags S1–S6 | off `main`: **gap** if this record lands; the probe lands with it. |
| Records on `main` at `cac5d264`: RS/ (README, ANALYSIS, F2-1 preregistration, A★ blob `fb01edcf…`, run-2 RESULT, native-padic REPORT, fixed-scale PREREGISTRATION); CS/ (README, infinite-xor-counterexample, equivalence-and-d3-scope, shared-gauge-pointer-candidate); `oi-qm-ext-1/prepared-pair-source.md` §5; the six OB/ modules; `papers/Main.md`, `papers/GR.md`, `papers/Substratum.md` | §1, §2.2 (relation to F2-1), §2.4, §3, §4.1 | **on `main`.** Their own review status is as they record it: paper proofs in CS/ are "not independently reviewed on `main`"; F2-1 and NATIVE-PADIC-1 reviews are author-reported. They are used here as descriptions of what was constructed and claimed, and E3 alone uses one of them (the topological lemma) as a premise — it is labelled conditional for that reason. |
| `oi-qm-ext-1/two-system-interface.md` (reuse signalling of the shared-parity candidate) | §3.4 item 4 | on `main`, **not re-read here**; cited through Bell-scope's description. Provenance; no verdict depends on it. |

The local checkout was at `b1d782f9…`, an ancestor of the pin. Every file cited from RS/, the six OB/ modules and the CS/ and `oi-qm-ext-1` files named above is byte-identical between the two commits (`git diff --quiet`); CS/README.md and the manuscripts were read at the pin.

***

## 7. Not done

- **No OI mechanism was computed.** In particular: no native rule was run on any tower; no check of whether the native-Y rule mixes levels; no dispersion computation for lifted rules (the O2 statement in §3.1 is by the form of the rule only).
- **No kernel formalization or build.** E1–E3 and L1–L3 are paper arguments. E1 (a kernel pushforward), E2 item 4 and L1 are natural kernel targets.
- **Infinite identified carrier** (§2.5): the lift statement was not proved.
- **Routes C-dyn and E_r** are not decided here either. §2.4 items 4–5 describe how an infinite carrier bears on them; no verdict on whether such a route succeeds.
- **The preparation-span diagnostic on an infinite hidden space** is argued only for classes containing all finitely supported laws.
- **No primary literature read first-hand** (audit Step 4 is done from recall only); the [L] entries need a literature pass before any use as support.
- **Not re-audited:** INTERVENE-1's and Bell-scope's own proofs; the paper proofs in CS/ (infinite XOR, solenoid, Fourier); H-LIFT's relation to H-IND; PC-1 and MR-1 beyond PC-1's result header; `two-system-interface.md`.
- **Issue comment threads** of #1007, #1009, #1011, #1015, #1016 were not read beyond the bodies; a decision recorded only in a comment could bear on the reading of (viii) or on the status of the observer-relative finiteness formulation.
- **No reading of ledger (viii) is chosen**, and no manuscript finding is corrected. G1 and G2 are observations for the reviews of PR #1230 and PR #1231; they are not applied to those drafts.
- **r1 has not been reviewed.** Nothing here is adopted, promoted or proposed for the manuscripts.
