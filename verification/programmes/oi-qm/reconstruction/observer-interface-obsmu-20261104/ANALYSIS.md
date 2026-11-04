# O-OBSMU — what `(Obs, μ)` needs, what the corpus supplies, and what is missing

**Status: WIP / UNVERIFIED.** Paper-only analysis by `writer-866`, under the authorization in
#866 c.6642599988. Revised twice, after the independent reviews of `1a796918` (#1110 c.6643202940) and of
`9a34c823` (#1110 c.6643501421). The disposition of each point is in the #1110 checkpoint
comments. The reviews are model-authored records off `main`. This note cites them as provenance,
not as verification of any result (§A.46 item 7). No computation was run.
Nothing here has been independently reviewed at this revision. No statement here is a premise of
an established claim (AGENTS.md §A.46 item 7).

## 0. Conventions

**Anchors.** All anchors are at `D` = `f5c281ae10a913ec68fa41b3b839ad0b164979cd`.

| Anchor | Refers to |
| --- | --- |
| `Main:N`, `SM:N`, `Substratum:N` | lines of `papers/` |
| `FULL:N`, `ch04:N`, `ch18:N`, `appC:N` | lines of `book/The-Incompleteness-of-Observation-FULL.md`, `book/ch04-methodology.md`, `book/ch18-beyond.md`, `book/appendix-c-objections.md` |
| `MR-pre:N` | `../measurement-record-formation/preregistration.md` |
| `MR★:N` | `../measurement-record-formation/amendments/MR-star.md` |
| `PC★:N` | `../physical-coupling-pc1/amendments/PC-star.md` |
| `SOI-audit` | `verification/audits/operational/stochastic-observer-interface-audit.md` |
| `ROF` | `verification/audits/operational/rooted-observer-family-sourcing/result.md` |

**Support layers.**

- **KC:** kernel-checked on `main`.
- **PD:** a paper derivation in a record on `main`, with its review status stated where it
  matters.
- **PD-here:** a paper derivation written in this note, unreviewed at this revision.
- **CJ:** a conjecture or sketch.
- **OP:** open.

A chain takes the layer of its weakest link.

**Sorting rule** (owner guidance, relayed 2026-11-04). Each requirement goes in exactly one
group:

- **(a)** implied by OI's axioms or theorems. The locator and support layer are given.
- **(b-stated)** not implied by the axioms, but stated in a manuscript as a posit, principle,
  idealization, convention, realization datum or solution-specific datum, and labelled there as
  such.
- **(b-new)** not stated anywhere in the corpus as a premise of the result that uses it.

Mathematical validity and physical justification are recorded separately.

**Literature** (§3.8). The owner's arXiv authorization is recorded at #866 c.6643204362. Each
source is marked as read directly or taken from a named secondary source. External results never
establish that something follows from OI's assumptions. An ingredient that only an external
construction supplies is an additional assumption.

**Off-`main` references** are classified one by one in §7 (§A.42 item 8).

## 1. The obligation, by consumer

The obligation, quoted in #866 c.6600176951 from the ROADMAP P1 section frozen at `9613b21c`:
"supply independently motivated structure selecting the physical observation map and ensemble,
or prove that the claims consuming an induced stochastic law are invariant under that residual
choice." Its negative bound is `ensemble_underdetermined` and
`waveSubstratum_stochastic_interface_gap` (KC, `OIBridge/StochasticInterface.lean`).

The consumers were found by searching `papers/Main.md`, `papers/Substratum.md`, `papers/SM.md`
§3.1, the SOI-audit, ROF and the #914 matrix. This is a census of those sources, not of every
downstream paper.

| # | Consumer | Locator | What it needs from `Obs` | What it needs from `μ` | Status under the residual choice |
| --- | --- | --- | --- | --- | --- |
| U1 | Representation equivalence `S ⇔ D ⇔ Q_fb` | Main §1.5, §3.4; KC `finite_horizon_equivalence` (`Equivalence.lean:462`), a biconditional for every `P : Traj V K → ℝ` with no hypothesis on `μ` | a finite outcome alphabet | nothing | **not a residual-choice consumer**: it holds for every finite-horizon law |
| U2 | Unavoidable hidden predictive memory; pushforward identity | Main §1.5, §3.4; KC `pushforward_identity` | finite alphabet | nothing | **not a residual-choice consumer** |
| U3 | Reverse finite realization | Main §1.5 (3) | finite alphabet | nothing | **not a residual-choice consumer** |
| R1 | Recurrence-cycle P-indivisibility of the rooted family | Main:137–145; KC `pIndivisible_of_identity_return_of_overlap` (`RecurrenceHorizon.lean:119`), its rooted form (`:148`), `isPermMatrix_of_stochastic_inverse` | product cut, `π_V` | the hidden laws given each root | **support-invariant**: depends on the hidden laws only through their supports (Theorem SI, §3.2; ELABORATING Main:141). **Not invariant across supports** (CC-1) |
| R2 | A C4 gap at order `k` | Main §1.3 (C4), Main:141 | product cut, `π_V` | the preparation law | **not invariant, even at fixed full support** (CC-2, §3.3). A generic dichotomy holds (Proposition G), and the canonical law can lie in its exceptional set |
| R3 | P-divisibility on an accessible window; the stochastic route's diagnostic | Main:141 scope; SOI-audit stage 3 | product cut, `π_V` | the hidden law | **not invariant in general, even at fixed full support** (CC-2, §3.4). **Open for native K1** |
| R4 | Applying the stochastic–quantum correspondence | Main:526–530 (translation hypothesis (T)); arXiv:2309.03085v2 §3.1 | finite configuration space | a transition map that does not change when the initial distribution is varied (Q9′) | **nothing new relative to Main.** Q9′ is (b-stated) at Main:137 and Main:284 (§3.8) |
| L1 | Partition-relativity lemma | Main:86 | the partition | the canonical measure, by name | **stated relative to a named measure** (Q8) |
| L2 | Baseline matrices; Lemma 3 prong 1; the uniform-prior one-step lemma | Main:60, :62, :276 | product cut | the uniform hidden prior | **stated relative to a named measure** (Q8) |
| L3 | A specific visible law (a Born weight, a correlation, a parameter) | Main:60 | the cut | the prior | **refuted as invariant** by Main:60's own swap example |
| L4 | Setting screening in the Bell analysis | Main:366 ff. | the wings' cuts | setting–hidden independence | **non-invariance argued, not shown here**; it also needs capacity (2) |
| L5 | Readiness and records (O-RDY, O-REC) | #914 rows O-RDY, O-REC; MR★:642 | the cut, its access | a ready resource | **non-invariance argued** (Lemma P-1: H-μ has no ready region), **not shown for every μ** |

**How each consumer fares.**

- **U1–U3:** use nothing from the residual choice. They are non-consumers, and they carry no
  prediction.
- **R1:** reduces the μ leg to a choice of supports.
- **R2 and R3:** depend on the measure itself, not only its support.
- **R4:** needs nothing beyond what Main states.
- **L1 and L2:** carry the named measure Q8 as a hypothesis.
- **L3:** is refuted as invariant.
- **L4 and L5:** non-invariance is argued here, not shown.

## 2. The four capacities: what the corpus establishes

**K1** is MR-1's frozen `K★ = {K1}`: the additive second-order step
`φ(u_prev, u) = (u, A u − u_prev)` on the native cubic graph, with finite or compact value group
`𝐑` (MR★:462–466).

| Capacity | Established (locator, layer) | Conditional (hypotheses) | Open | Physical justification of the hypotheses |
| --- | --- | --- | --- | --- |
| **(1) Preparation** | Main:60: a realization "carries its own fixed hidden prior `μ_H` as part of the realization datum" (stated datum). For finite `𝐑` under H-μ, every region is uniform and disjoint regions are independent at equal times (Lemma P-1, PD-here). | For rooted laws with a full-support visible prior, conditioning on the observed initial value replaces preparation (§3.5, PD-here). | O-RDY (#914 row O-RDY). No process on K1 writes a chosen value into a region (MR★:637). | The structured `μ_H` is supplied, not sourced (ROF Q3(ii)). |
| **(2) Selectable interactions** | The controlled lift `F(x, s) = (T_s x, s)` conserves `s` (MR-pre:115, N7; a frozen record). | On K1, a setting region changes every other region only by an additive offset that does not depend on the carrier's state. This is the identity part of Lemma D (MR★ S-L1, S-C1, :479–509; PD in a frozen record; re-derived here, PD-here). Counting offsets as non-selectable needs premise D-SEL, and O-SET's definition is open. | O-SET, DEFINITION-OPEN (#1009). Non-additive native-type rules are unscreened (MR★:667, σ12). | Additivity is Substratum A5, "partly derived" from amplitude-scale gauge, an "explicit operational principle" (Substratum:100, :272) (b-stated). |
| **(3) Accessible outcomes** | A finite outcome alphabet: Main Definition and Lemma 1 (Main:44, :48; PD with an external holographic input). The readout is configuration-sector (Main:222). Region readout: KC definition `cutRealization` (`PhysicalC4Discharge.lean:582`). | For finite `𝐑`, under H-μ and K1 with a homomorphic readout, conditional next-step laws are flat on cosets of a history-independent subgroup (Proposition C, PD-here). | O-ACC: whether one retained tick is native or a convention (#914 row O-ACC). | The cut exists (a): Main:38–40, :50. The product form is (b-stated): "idealized" (Main:54). A finite readout does not imply a product (§4.1, Q4, PD-here). |
| **(4) Readable, persistent records** | MR-1 stage 1 gives a scoped `GAP` (MR★ §M.1, a frozen record). | On K1, no confined pattern lasts beyond about twice its width (MR★ S-L4, S-C4a, :528–571). PD in a frozen record, not independently reviewed. Hypotheses: `ℤ^d`, or a torus with `N ≥ 5w + 2`, and `a` injective. | O-RET (#1032), O-REC (#866). | Finite recurrence bounds every budget (MR★ S-L6). |

## 3. The routes, depth-first

Each node is closed by the check it names. Productivity test (§A.31), fixed before the walk: a
node is a gem if it is strictly stronger than a restatement and either constrains something or
exposes a hidden assumption.

### 3.0 Node S — the sourcing route

**S.1, the Obs leg.** Checks: Main §1.2, ROF Q1 and Q6, SOI-audit T2.

- **Existence of the cut (a).** It is constitutive of Axiom 1 on Main's adopted perspectival
  reading (Main:38–40), and Lemma 2 states it (Main:50).
- **Which cut.** Not implied. Main §1.4 makes the description partition-relative, so the cut is
  a parameter of every per-cut claim.
- **Product form (b-stated).** Main calls it "idealized" (Main:54).
- **Readout slice.** Main treats the readout as configuration-sector (Main:222), so the slice is
  (b-stated). Whether it is native is O-ACC.
- **The two layers.** The reduced `Substratum` record has no observation map (KC
  `readWriteFamily_exists`). The realization layer declares one (ROF Q6).

**Verdict S.1.** The Obs leg is sourced as a family indexed by the declared cut. The product form
and the readout slice are (b-stated).

**S.2, the μ leg.**

- **S.2.1, invariance alone.** It does not select a measure: KC `ensemble_underdetermined`.
  Closed, negative.
- **S.2.2, Lemma 3's selection (b-stated).** Main:56 reads: "the counting measure is selected
  among invariant measures as the maximal-entropy one — a selection principle, not uniqueness
  from invariance alone".
  - It needs finite total `S`. Main:62 and :268 carry that as a posit. The owner's
    observer-relative finiteness decision (§7) keeps it as a branch premise.
  - On an infinite space the counting measure is not a probability, and Haar measure on a
    compact completion would need its own selection argument (PC★:219–220).
- **S.2.3, what Main states about conditioning, and at what level.** Main §4.6 is quoted in full
  in Appendix A.
  - **What §4.6 states.** Its theorem (Main:748–752) is conditional on (EM) and concerns "the
    coarse-grained description generated by iterating `𝒦_{Σ_loc(V)}`". It assumes bounded
    coupling-graph diameter, canonical typicality for the equilibrium clause, and finite `S`
    (Main:760, Scope). Its past-hypothesis corollary (Main:758) adds the rate condition
    `τ_mix ≪ τ_S` and concludes that, "in that description, with (C2) read in its timescale form
    (C2-slow), the framework's observers therefore exist only in the non-equilibrium phase of
    `(S, φ)`". §4.6 says where observers can exist. It states no measure.
  - **The "structural, not measure-theoretic" sentence** (Main:756) belongs to the
    anti-Boltzmann-brain corollary. The first revision of this note used it to infer that Main
    states no conditioning, and that inference is withdrawn. The sentence says only how the
    Boltzmann-brain exclusion is argued.
  - **What Main does state about the measure** is orbit-level conditioning:
    - Main:62: "the selection among orbits is fixed by maximal entropy compatible with the
      observer's records", with "the atypical short orbits … precisely observer-lacking
      substrata … outside the scope of every theorem below";
    - the posit ledger, Main:726 (iv): "the measure selection is a maximal-entropy principle ('the
      maximal-entropy invariant measure compatible with the observer's records') — a standard but
      substantive epistemic postulate, not derived";
    - book ch01:85, which says the same.
  - **Classification.** The note's earlier single label H-OC is split into two:
    - **H-OC_orb (b-stated):** the measure is the maximal-entropy *invariant* measure compatible
      with the observer's records, which excludes observer-lacking orbits (Main:62,
      :726 (iv); ch01:85).
    - **CR_slice (b-new):** a rule that conditions the measure on an event at a stated time slice.
      No source states one.
- **S.2.4, why orbit-level conditioning cannot give a preparation.**
  - A measure invariant under `φ` gives equal weight to every point of each orbit in its support.
    It therefore assigns a time-slice event `R` the weight of `R` within each orbit, at every time
    alike. That is not a preparation made at a time.
  - Lemma 3's selection is among invariant laws (Main:56, :726 (iv)). The uniform law on a
    time-slice event `R` is invariant only if `φ(R) = R`. So "given `R`, the measure follows from
    Lemma 3" stays withdrawn.
  - A preparation law at a time is obtained in one of two ways:
    - **(i)** supplied directly as a realization datum. Main:60 allows "its own fixed hidden prior
      `μ_H`", and Main:524 gives a structured state-level prior, "uniform on the initialized
      ledger/clock sector times the tape".
    - **(ii)** derived from the canonical measure by a slice-conditioning rule, CR_slice (b-new).
  - Route (i) needs no new rule. Its content, which particular state-level law, is supplied, not
    sourced.
- **S.2.5, related statements in the corpus** (a §A.19 search).
  - **Main:62:** "the selection among orbits is fixed by maximal entropy compatible with the
    observer's records". This is a stated, records-conditioned, orbit-level selection
    (b-stated). It does not name a state-level preparation event.
  - **ch18:210 and FULL:5023–5033:** "The universe starts in a configuration that is far from
    equilibrium relative to the substratum's full state space", and "the universe begins in a
    low-entropy configuration with most degrees of freedom on the hidden side of the cosmological
    horizon". This states a low-entropy initial condition in the book (b-stated).
  - **ch04:170:** "Cosmic initial conditions are solution-specific … The state at any particular
    cosmic time, including the time-zero conditions, is not a framework output."
  - **appC:329:** "Why this initial state rather than another is not addressed by the framework's
    structural content."
  - **Main versus ch18 (checked by hand; the second review agrees).**
    - Main limits its replacement of the past hypothesis to one role, at both places it states
      it:
      - Main:744: "in its role of selecting observer-compatible configurations";
      - Main:758: "The low-entropy initial condition commonly imported as a "past hypothesis" to
        select observer-compatible configurations is replaced here, within that description, by
        a structural selection rule".
    - Main makes no claim about the source of the arrow of time.
    - So no contradiction is recorded **between Main and ch18**. This verdict is limited to that
      pair.
  - **Cross-document finding, tracked as #1112 (ARROW-1).** Each passage below was read directly
    at `D`. The corpus disagrees on whether the arrow of time is derived.
    - **Saying it is derived:**
      - Substratum:401: "every arrow the observer sees descends from this confinement together
        with the horizon growth that the accelerating phase produces";
      - ch02:194–196 (= FULL:837 and the paragraph after it): "it derives a monotonic parameter
        along observer worldlines and four aligned arrows of time";
      - ch03:58;
      - Explainer:930: "You don't need to posit low initial entropy to explain why we see it".
    - **Saying it is inherited:** ch18:210 and :218–222 (= FULL:5023, :5031–5035): "the arrow is
      at the level of partition initial conditions, not at the level of substratum dynamics".
    - This note does not analyze it further, and edits no manuscript.
  - **What is missing.**
    - **Its category is stated.** State-level realization or solution-specific data: Main:60,
      :524; ch01:85; ch04:170.
    - **Its content is not.** No source specifies which state-level preparation event or law is
      realized.
    - **Any principle fixing that content** would be b-new.
- **S.2.6, ordering against O-RDY.**
  - #914 makes O-RDY depend on the μ leg, "or a named prior [C]", and records two further
    routes: "under H-μ, equal-time readiness is absent, so positives go through conditioned
    patches (I2, open) or cross-time routes". It also forbids assuming "a record that supplies
    readiness (Z1)" (#914 c.6563412926, row 1′).
  - Read through CR_slice, the μ leg needs the readiness event that O-RDY supplies. That route is
    circular.
  - The named-prior option, conditioned patches and cross-time routes are not circular. So no
    circularity forces O-OBSMU to come before O-RDY.
  - Status: ELABORATING.

**Verdict S.2.** The μ leg is not sourced from the axioms. Main supplies a measure only through
Q8 and H-OC_orb (b-stated: Main:56, :62, :726 (iv)), which need finite total `S`. Orbit-level
conditioning cannot produce a time-slice preparation. A preparation law at a time is either a
realization datum with supplied content (b-stated category), or the canonical measure conditioned
by CR_slice (b-new).

### 3.1 Node I.1 — non-consumers U1–U3

KC `finite_horizon_equivalence` is a biconditional for every `P : Traj V K → ℝ`, with no
hypothesis on `μ` (`Equivalence.lean:462`). Every induced law with a finite alphabet is in its
scope. So U1–U3 use nothing from the residual choice. They carry no prediction and do not
discharge O-OBSMU for any consumer that does.

### 3.2 Node I.2 — Theorem SI (support invariance), consumer R1

**Setting.**

- `C_V` and `C_H` are finite, and `φ` is a bijection of `C_V × C_H` of order `L`. Finite order
  needs finite total `S` (Main:62, :268).
- `μ_a` is the hidden law given root `a`. It may depend on `a`.
- `Γ_t(a, j) = μ_a{h : π_V φ^t(a, h) = j}`.

**Theorem SI (PD-here).** Whether the family is P-divisible on `{0, …, L}` depends on the `μ_a`
only through their supports `Σ_a`.

*Proof.*

1. **Permutation status depends only on the supports.** `Γ_s(a, ·)` is a point mass iff
   `h ↦ π_V φ^s(a, h)` is constant on `Σ_a`. A square stochastic matrix is a permutation iff its
   rows are point masses at pairwise distinct columns. Both conditions depend only on these maps
   restricted to the `Σ_a`.
2. **All permutations give divisibility.** `Γ_0 = I`, and `Γ_L = I` whatever the `μ_a`, because
   `φ^L = id`. If every `Γ_s` with `1 ≤ s ≤ L − 1` is a permutation, then `Γ_s⁻¹ Γ_t` is a
   stochastic divisor for all `s < t ≤ L`.
3. **One non-permutation gives indivisibility.** Suppose some `Γ_s` is not a permutation.
   - Two distinct rows of `Γ_s` then share positive mass (Main:139).
   - KC `pIndivisible_of_identity_return_of_overlap` (`RecurrenceHorizon.lean:119`) assumes only
     that `Γ_s` is row-stochastic. With `Γ_L = I`, it gives P-indivisibility on `{0, …, L}`.
   - The P-divisibility predicate is `PDivisible` (`CausalReadback.lean:54`). `□`

**Corollary SI-1** (every `Σ_a = C_H`). A point-mass row forces
`φ^s({a} × C_H) = {σ(a)} × C_H`, by counting and injectivity. So the verdict depends on
`(φ, π_V)` alone. It is indivisibility exactly when the hidden state changes the visible value
from some root at some time `1 ≤ s ≤ L − 1`.

**Countercontrol CC-1.** Take `C_V = C_H = {0, 1}` and `φ(v, h) = (v ⊕ h, h)`, so `L = 2`.

- Uniform `μ_H`: `Γ_1 = [[½, ½], [½, ½]]` and `Γ_2 = I`. Not P-divisible.
- `μ_H = δ_1`: `Γ_1` is the swap and `Γ_2 = I`. P-divisible.

**Status: ELABORATING.** Main:141 already carries the shared-prior, full-support form: "With a
full-support visible prior the hypothesis and the conclusion coincide" … "For every visible
prior, a non-deterministic visible step … makes some `Γ_s` a non-permutation". What this note
adds is the root-dependent generalization and the statement that only the supports matter.

**Limits.**

- The consumer is a property of the whole recurrence cycle, which no accessible window reaches
  (Main:141).
- The theorem needs the product form (b-stated) and finite total `S`.

### 3.3 Node I.3 — consumer R2: generic dichotomy, not invariance

**Proposition G (PD-here).** Fix `(φ, π_V)`, an order `k` and a support `Σ ⊆ C_V × C_H`. Among
preparation laws with exactly this support, exactly one of the following holds:

- no law has a C4 gap at order `k`;
- every law has one, except for a closed set of Lebesgue measure zero in the relative open
  simplex `Δ_Σ` of such laws.

*Proof.*

1. **Positivity depends only on the support.** A visible history `p = (x_0, …, x_k)` has positive
   probability iff some `(a, h) ∈ Σ` produces it, that is, iff
   `π_V φ^t(a, h) = x_t` for all `t ≤ k`.
2. **The criterion is polynomial.** Fix two positive-probability histories `p ≠ p′` with
   `x_k = x′_k`, and an outcome `y`.
   - Write `D_p = Σ_{(a,h) ∈ Σ} λ(a, h) 1[(a, h) produces p]`, and `N_p(y)` for the same sum
     with the further condition `π_V φ^{k+1}(a, h) = y`.
   - Both are linear in the law `λ`. Their next-step probabilities are `N_p(y)/D_p` and
     `N_{p′}(y)/D_{p′}`.
   - Since `D_p, D_{p′} > 0` on `Δ_Σ`, the two differ at `y` iff
     `Q_{p,p′,y}(λ) = N_p(y) D_{p′} − N_{p′}(y) D_p ≠ 0`, a polynomial in `λ`.
3. **The dichotomy.** A C4 gap at order `k` exists at `λ` iff `Q_{p,p′,y}(λ) ≠ 0` for some
   triple. The set of triples is finite and, by step 1, the same for every `λ ∈ Δ_Σ`.
   - If every `Q` vanishes identically on `Δ_Σ`, no law has a gap.
   - Otherwise some `Q` is a polynomial that is not identically zero on the open set `Δ_Σ`
     (open in its affine hull). The laws with no gap lie in its zero set. That set is closed, and
     it has measure zero, because a polynomial that does not vanish identically on a connected
     open set has a null zero set. `□`

**Product preparations `λ = ν ⊗ μ_H`** (Main's rooted setting). These form a lower-dimensional
subset of `Δ_Σ`. Here `Σ = Σ_V × Σ_H`, and `D_p` and `N_p(y)` are bilinear in `(ν, μ_H)`. The same
argument therefore gives the same dichotomy on the product of the two relative open simplices.

**The dichotomy is not invariance.** The canonical law can lie in the exceptional set.

**Countercontrol CC-2 (PD-here, checked by hand; construction from the first review).**

- **The construction.** `C_V = {0, 1}`, `C_H = {0, 1}^m` with `m ≥ 2`, and
  `φ(x, h) = (x ⊕ h_0, rot h)`, where `(rot h)_i = h_{i+1 mod m}`.
  - It is a bijection. Its inverse is `(x′, h′) ↦ (x′ ⊕ (rot⁻¹ h′)_0, rot⁻¹ h′)`.
  - `φ^{2m} = id`.
  - Along a trajectory `x_{t+1} = x_t ⊕ h_t`, so `x_t = x_0 ⊕ h_0 ⊕ … ⊕ h_{t−1}`.
- **The preparations.** Take `x_0` uniform and independent of `h`. Let `h_0` and `h_1` have
  uniform marginals and `P(h_0 ≠ h_1) = q ∈ (0, 1)`. Any further coordinates are independent and
  uniform. Every such law has full support.
- **R2 at order 1.**
  - A history `(x_0, x_1)` reveals `h_0 = x_0 ⊕ x_1`, and `x_2 = x_1 ⊕ h_1`.
  - The histories `(0, 0)` and `(1, 0)` both end at `x_1 = 0`. Their next-step probabilities of
    `x_2 = 1` are `P(h_1 = 1 | h_0 = 0) = q` and `P(h_1 = 1 | h_0 = 1) = 1 − q`.
  - So there is a gap iff `q ≠ ½`. The uniform tape (`q = ½`) has no gap at order 1. Every other
    `q` in `(0, 1)` has one.
- **R3 on the window `{0, 1, 2}`.**
  - `Γ_1(a, ·)` is the law of `a ⊕ h_0`, uniform for both roots, so its rows are equal.
    `Γ_2(a, ·)` is the law of `a ⊕ h_0 ⊕ h_1`, with flip probability `q`.
  - `Γ_1 Λ` has equal rows for every `Λ`. So `Γ_2 = Γ_1 Λ` needs `q = ½`.
  - So the family is P-divisible on `{0, 1, 2}` at `q = ½` (take `Λ = Γ_2`), and not P-divisible
    for `q ≠ ½`.

**A related zero-memory uniform-tape instance.** Main:178's §3.4 fair-coin dilation has zero
conditional memory "exactly at every horizon time" under its uniform tape. It is not the same
construction as CC-2. This note does not check whether a correlated tape law in that
construction gives memory.

**Verdict R2.** Not invariant, even at fixed full support. Proposition G still says that the
verdict at the canonical law is non-generic whenever it differs from the generic one.

### 3.4 Node I.4 — consumer R3

**Closedness (PD-here).** Fix a window `{0, …, n}` and the supports `Σ_a` of the hidden laws
given each root. Let `Δ` be the product over roots of the relative open simplices of laws with
those supports. The set `Div ⊆ Δ` of hidden-law families at which the rooted family is
P-divisible on `{0, …, n}` (`PDivisible`, `CausalReadback.lean:54`) is relatively closed in `Δ`.

*Proof.*

1. Each `Γ_t` is linear in the hidden-law family, so `μ ↦ (Γ_t(μ))_{t ≤ n}` is continuous.
2. The set `Stoch` of row-stochastic `|C_V| × |C_V|` matrices is compact.
3. For a pair `s < t`, let `F_{s,t} = {(A, B) : B = A Λ for some Λ ∈ Stoch}`. It is the image of
   the closed set `{(A, Λ) : A ∈ Stoch}` under the continuous map `(A, Λ) ↦ (A, AΛ)`.
   - Restricted to `A` in the compact set `Stoch`, the domain `Stoch × Stoch` is compact, and so
     is its image.
   - So `F_{s,t}` is closed.
4. `Div` is the intersection, over the finitely many pairs `s < t ≤ n`, of the preimages of the
   `F_{s,t}` under the continuous maps `μ ↦ (Γ_s(μ), Γ_t(μ))`. So `Div` is closed in `Δ`. `□`

**Consequences.**

- `Δ` is connected. So the verdict is the same at every point of `Δ` iff `Div` is empty or all of
  `Δ`, that is, iff `Div` is also relatively open.
- CC-2 (§3.3) shows that `Div` can be neither, at full support. So window P-divisibility is
  **not invariant in general**.

**Open for native K1.** Whether some native `(φ, π_V)` has a window verdict that does not depend on
the prior is open. Settling it needs a paper argument or a native two-prior counterexample. The
first version said that finding such a pair "is a computation"; that is withdrawn, since CC-2 was
found by hand.

### 3.5 Node I.5 — consumers L1–L5, and the root convention

- **L3** is refuted as invariant by Main:60's swap example.
- **L1 and L2** are stated relative to a named measure (Main:86, :276). They need Q8 and nothing
  less.
- **L4 and L5:** non-invariance is argued, not shown.
  - L4 needs setting–hidden independence (Main:366 ff.) and capacity (2).
  - L5 needs a ready region, which H-μ lacks (Lemma P-1).

**Root convention (PD-here, restricted).** Let the visible prior `ν` have full support. Then for
every root `a`, conditioning on the observed `X_0 = a` gives `μ_a`. Every row of the rooted family
is then a conditional law given an initial record, and capacity (1) is not needed for R1.

The rooted family keeps rows of roots with visible probability zero (Main:139). If `ν` lacks
full support, those rows cannot be obtained by conditioning. They are then either a preparation
(capacity (1)) or a convention extending `μ_a` to those roots.

### 3.6 Node D — K1's dynamical obstructions, conditionally independent of `(Obs, μ)`

**Lemma D, identity part (PD-here; MR★:479–485 and :491–509).** On K1, `φ^t` is additive. So
`pr_Y φ^t(s) = Σ_X Φ^t_{YX}(s_X)`, with each `Φ^t_{YX}` a fixed homomorphism. This is an
identity in the state `s`, and so it holds under every `μ`.

**Lemma D, conclusion (conditional).** Two premises, both named:

- **D-SEL (definitional).** A selectable interaction is a setting-dependent change of the
  carrier's transformation that is not only an additive offset `T_s = τ_{Bs} ∘ T_0`. It must also
  survive the foils of #866 c.6567167742: precomputed selector, post-processing, XOR relabelling
  and masked kicks, effects of `Z_rest` alone, and decoy cancellation.
  - Under additivity, settings give exactly such offsets.
  - Offsets compose to non-commuting affine maps (`T_s T_{s′} ≠ T_{s′} T_s` in general).
  - So whether they count is a question for O-SET's open definition (#1009), not a fact about
    `μ`.
- **S-L4 (MR★:531–562).** PD in a frozen record, not independently reviewed. Its hypotheses:
  `Λ = ℤ^d` with nearest neighbours, or a torus with `N ≥ 5w + 2`, and `a` injective on `𝐑`.

Under D-SEL, no `(Obs, μ)` on K1 supplies capacity (2). Under S-L4 with its hypotheses, no
`(Obs, μ)` on K1 supplies a confined pointer (capacity (4)). Both statements are scoped to K1.
They are conditional on D-SEL and S-L4 respectively.

**Status: ELABORATING** (a reduction of the MR★ §S lemmas).

### 3.7 Node C — the law H-μ induces on K1 with finite `𝐑` (ELABORATING)

**Scope.** `𝐑 = ℤ/q`, so `S` is a finite abelian group. This excludes the `ℤ_p` and `ℝ/ℤ` cases
of K1.

**Lemma P-1 (PD-here).** Let `S` be a finite abelian group, `φ` an automorphism of `S`, and `μ`
the Haar (uniform) probability on `S`. For a region `X`, let `S_X` be its factor and
`pr_X : S → S_X` the projection. Then:

- the law of `pr_X(φ^t s)` is uniform on `S_X` for every `t`;
- for disjoint `X` and `Y`, `pr_X(φ^t s)` and `pr_Y(φ^t s)` are independent;
- a fixed pattern on `X` has probability `|S_X|⁻¹`.

*Proof.*

1. `φ^t` is a bijection, so it preserves the uniform law.
2. `pr_X` is a surjective homomorphism. Each fibre `pr_X⁻¹(x)` is a coset of `ker pr_X`, so all
   fibres have size `|S|/|S_X|`, and the pushforward is uniform.
3. `pr_{X∪Y} = (pr_X, pr_Y)` is a surjective homomorphism onto `S_X × S_Y`, since the regions are
   disjoint factors. Its pushforward is uniform on the product, which is the product of the
   uniform laws. `□`

**Proposition C (PD-here).** Take `S`, `φ` and `μ` as in Lemma P-1, and a homomorphic readout
`π : S → G` onto a finite abelian group `G`.

*Definitions.*

- `Ψ_k(s) = (π φ^0 s, π φ^1 s, …, π φ^k s) ∈ G^{k+1}`. This is a homomorphism. Its image is
  `I_k ≤ G^{k+1}`.
- `K_{k+1} = {y ∈ G : (0, …, 0, y) ∈ I_{k+1}}`, with `k + 1` zeros. It is a subgroup of `G`.
- `π̂ : G^{k+2} → G^2` keeps the last two coordinates, `(g_0, …, g_k, g_{k+1}) ↦ (g_k, g_{k+1})`.
- `K′_{k+1} = {y ∈ G : (0, y) ∈ π̂(I_{k+1})}`. It is a subgroup of `G` with
  `K_{k+1} ≤ K′_{k+1}`.

*Claims.*

1. The history `X_{≤k} = Ψ_k(s)` is uniform on `I_k`.
2. For every `h ∈ I_k`, the conditional law of `X_{k+1}` given `X_{≤k} = h` is uniform on a coset
   `y_0(h) + K_{k+1}`.
3. `H(X_{k+1} | X_{≤k} = h) = log₂|K_{k+1}|` for every such `h`. The conditional law given `X_k`
   alone is uniform on a coset of `K′_{k+1}`, and
   `M_k = I(X_{<k}; X_{k+1} | X_k) = log₂ [K′_{k+1} : K_{k+1}]`.

*Proof.*

1. By Lemma P-1's step 2 applied to the surjective homomorphism `S → I_k`.
2. `I_{k+1}` is uniform by step 1. Let `ρ : I_{k+1} → I_k` drop the last coordinate. It is a
   surjective homomorphism with kernel `{0}^{k+1} × K_{k+1}`. So the fibre over `h` is
   `{(h, y_0(h) + κ) : κ ∈ K_{k+1}}` for any `y_0(h)` in it, and the uniform law on `I_{k+1}`
   conditions to the uniform law on that coset.
3. The same argument applies to `π̂(I_{k+1})`, which is the image of a homomorphism and so carries
   the uniform pushforward. Its projection to the first coordinate has kernel `{0} × K′_{k+1}`.
   So `H(X_{k+1} | X_k) = log₂|K′_{k+1}|` at every positive-probability value. Then
   `M_k = H(X_{k+1} | X_k) − H(X_{k+1} | X_{≤k}) = log₂|K′_{k+1}| − log₂|K_{k+1}|`. Finally,
   `K_{k+1} ≤ K′_{k+1}`, because `(0, …, 0, y) ∈ I_{k+1}` gives `(0, y) ∈ π̂(I_{k+1})`. `□`

**Status.** ELABORATING. The equal-time part overlaps #914 C-10, which cites an off-`main` record.
That record is classified in §7. The proofs above are complete in this note and do not use it.

### 3.8 Literature

1. **Barandes, arXiv:2309.03085v2, §3.1, pp. 8–10, equations (24)–(35). Read directly.**
   - The tuple is `(C, T, T_0, Γ, p, A)`, with `Γ_ij(t ← t_0) = p(i, t | j, t_0)`.
   - Quoted: "Only the standalone probabilities `p_1(0), …, p_N(0)` at the initial time 0 will be
     taken to be freely adjustable".
   - Quoted: the definition of `Γ` "is independent of the choice of standalone probabilities …
     at the initial time 0".
   - Use here: to identify that R4 needs Q9′.
   - Main already states Q9′: Main:137 draws the hidden state from one prior "whatever the root",
     and Main:284's channel `Φ(ρ_V) = Tr_H[U_φ(ρ_V ⊗ ρ_H)U_φ†]` uses one fixed `ρ_H` for every
     input. So R4 needs nothing new relative to Main.
   - The source's divisibility (35) is imposed only at conditioning times. It is not Main's
     P-divisibility, and ROF records that the two are not identified.
2. **Barandes, arXiv:2302.10778v3. Read directly: abstract page only.** Not used.
3. **'t Hooft, arXiv:1405.1548v3. Read directly: abstract page only.** Not used.
4. **The Past Hypothesis and the record asymmetry. Secondary only:** web-search result summaries,
   2026-11-04. The summaries attribute the record asymmetry to a low-entropy initial macrocondition
   (Albert, Loewer), and report that arXiv:2309.03484 calls the basic Past Hypothesis too vague.
   No passage was read, and nothing here uses them as support.
5. **Additive cellular automata (superposition).** Background only. No source was read. Lemma D's
   identity is derived here directly.

## 4. What is missing

### 4.1 Requirements for `(Obs, μ)`, sorted

| # | Requirement | Group | Locator and layer |
| --- | --- | --- | --- |
| Q1 | A finite outcome alphabet | (a) | Main Definition (Main:44: "finitely many distinguishable internal states") and Lemma 1 (Main:48). PD with an external holographic input. |
| Q2 | An observer cut exists | (a) | Main:44, :50; constitutive of Axiom 1 on the adopted reading (Main:38–40). |
| Q3 | Which cut | (b-stated), as a parameter | Main §1.4, Main:86. |
| Q4 | Product form `S = C_V × C_H` | (b-stated) | "idealized" (Main:54). A finite readout does not imply it. Take `S = {1, 2, 3}` and `π(1) = π(2) = 0`, `π(3) = 1`: the fibres have sizes 2 and 1, so `S` is not `C_V × C_H` with `π` the projection (PD-here). |
| Q5 | Readout slice content | (b-stated), as a model choice | Main:222 projects the flow onto the configuration sector. This is a construction step in the marginalization, not a labelled posit. Whether the slice is native is O-ACC (open). |
| Q6 | `μ` is invariant | (b-stated) | Part of the canonical-measure posit (Main:56; ledger Main:726 (iv)). Realization priors need not be invariant (Main:60, :524). |
| Q7 | `μ` is unique | not available | KC `ensemble_underdetermined`. |
| Q8 | Maximal-entropy selection of the counting measure | (b-stated) | Main:56; ledger Main:726 (iv), "a standard but substantive epistemic postulate, not derived"; KC `counting_maximal_entropy`. Needs finite total `S` (Main:62, :268), a branch premise under the owner's finiteness decision (quoted in §7). |
| Q9 | Root independence `μ = ν ⊗ μ_H` | (b-stated) | Main:60, :137; ROF Q4. |
| Q9′ | The hidden laws given each root do not change when the visible initial distribution is varied | (b-stated) | Main:137, :284. Implied by Q9. "Measurement independence" is an analogy only. |
| Q10 | The supports `Σ_a` of the hidden laws | (b-stated) | Part of the realization datum `μ_H` (Main:60). Full support under Q8. |
| Q12 | The measure beyond its support | (b-stated) | Q8, or a realization datum (Main:60). |

The axioms imply none of Q3–Q12. The conditioning and preparation requirements are sorted
separately below, in the four groups the owner asked to be kept apart.

| Group | Requirement | Classification | Locator |
| --- | --- | --- | --- |
| **(1)** | **H-OC_orb:** the measure is the maximal-entropy *invariant* measure compatible with the observer's records; observer-lacking orbits are outside scope | **b-stated** (orbit level) | Main:62; Main:726 (iv); ch01:85 |
| **(2)** | **CR_slice:** a rule conditioning a reference measure on an event at a stated time slice | **b-new** | Stated nowhere (S.2.3–S.2.4). It drops Q6 unless `φ(R) = R` |
| **(3)** | **Q11′ category:** a state-level preparation event or law, admitted as starting data | **b-stated** (as a category) | Main:60 ("its own fixed hidden prior `μ_H`"); Main:524 (a structured state-level prior); ch01:85; ch04:170 (initial data "solution-specific"); appC:329. The book states a low-entropy initial condition (ch18:210, FULL:5023–5033) |
| **(4)** | **G-PREP:** a physical principle that generates the *content* of those events, saying which state-level preparation is realized | **none identified.** Any such principle would be b-new | No source supplies one (S.2.5, "What is missing") |

### 4.2 By consumer

| Consumer | What it needs |
| --- | --- |
| U1–U3 | Q1 only. They are not residual-choice consumers. |
| R1 | Q1, Q2, Q4, Q10 and finite total `S`. Supports suffice (Theorem SI). Relative to Main nothing new; relative to the axioms Q4 and Q10 are b-stated. |
| R2, R3 | The measure itself (CC-2), so Q12. R3 on native K1 is open. |
| R4 | Q9′, which Main states. Nothing new. |
| L1, L2 | Q8 only. |
| L4 | Setting–hidden independence (Main:366 ff.) and capacity (2). |
| L3, L5 | A measure for a preparation that is actually made. |

**For L3 and L5. A scoped answer, not a minimality result.**

- **Group (1) is not enough.** An invariant measure gives equal weight along each orbit, so it
  cannot produce a preparation made at a time (S.2.4).
- **Two routes reach a time-slice preparation law.** Neither uses more than groups (2) and (3):
  - **Route (i), datum:** take the preparation law directly as group-(3) starting data. No new
    rule is needed. The content is supplied, not sourced, so L3 and L5 outputs are conditional
    on supplied data. Under ch04:170 they are solution-specific.
  - **Route (ii), conditioning:** derive the preparation law from Q8 by CR_slice (group (2),
    b-new) on a group-(3) event whose content is again supplied.
- **The second review's formulation** was "a sourced state-level preparation event, whose
  category is already admitted as data, plus one new slice-conditioning rule". I checked it
  against route (i), and it holds for route (ii) only. Route (i) needs no new rule. So the
  slice-conditioning rule is needed only to obtain the preparation law *from the canonical
  measure*.
- **Either way, group (4) is missing.** No physical principle generating the content of the
  preparation event is identified in the corpus. This note does not supply one.
- **Not shown minimal.** This note does not show that no smaller ingredient serves.

**Which assumptions prevent OI from deriving its own observer and measurement structures.** The
list is scoped to the sources read and conditional where stated.

1. **No principle generates the content of preparations (group (4)).** Without one, every
   preparation-dependent law (L3, L5) is relative to supplied data. This is the crux of O-OBSMU's
   μ leg.
2. **Main's own measure posit works at orbit level** (group (1); Q6, Q8). An invariant,
   records-compatible maximal-entropy measure cannot represent a preparation at a time. Getting
   one from it needs CR_slice, which is b-new.
3. **The observer's cut and product form are parameters and idealizations** (Q3, Q4), and its
   readout slice is a construction step (Q5; O-ACC open). No result derives which subsystem
   observes from `(S, φ)`; this is the separate question #914 row 3′ records as O-OBS.
4. **For the measurement capacities (2) and (4), the native step's additivity** (Substratum A5,
   b-stated through amplitude-scale gauge) blocks selectable interactions and confined records
   for every `(Obs, μ)`. This holds conditionally on D-SEL and S-L4 (Lemma D). It is a dynamical
   assumption, not an interface one. Removing it is the P-SDC question (§4.4).

### 4.3 Proposal P-R (not adopted; awaiting the owner)

**Statement.** For a declared cut `V`, the laws are drawn from the counting measure, or Haar
measure on a compact completion, conditioned by CR_slice on a declared state-level preparation
event `R`. Group (2) is added; group (3) content is supplied. P-R does not supply group (4).

**Failable controls (§A.29).**

- **(i) Lemma 3, prong 1 (Main:62).** Main:62 excludes visible merges "wherever the observed
  statistics are of that doubly stochastic class under the uniform prior". Main:276 and :524
  confine double stochasticity to uniform-prior marginals.
  - **Evaluation (PD-here).** CR_slice on an `R` that constrains hidden sites makes the hidden
    prior non-uniform. The visible marginals are then generically not doubly stochastic, even for
    a bijection. So under P-R, observed departures from double stochasticity no longer witness a
    merge, and prong 1 loses its empirical input.
  - Lemma 3's conclusion (bijectivity) survives through prong 2, which is structural:
    finiteness and recurrence on the eventual image (Main:62).
  - **Verdict:** control (i) **fails as worded**. P-R removes prong 1's empirical input. It does
    not contradict Lemma 3's conclusion.
  - P-R could be scoped away from the control only by restricting its conditioning to visible or
    apparatus sites that leave the hidden prior uniform. That restriction is a further free
    choice.
- **(ii) Main §4.6.** Main:744 replaces the past hypothesis "in its role of selecting
  observer-compatible configurations". P-R must not take over that selection role. It fails if
  `R` is required to select observer-compatible configurations rather than a laboratory
  preparation.
- Theorem SI and Lemma D hold for every measure, so they are not controls.

**Independent consequence: none identified.** Proposition C's coset structure already holds under
unconditioned H-μ.

**Refuting outcome.** None realizable on K1. MR-1 stage 1 sources no native record law there
(scoped `GAP`).

**§A.29.** `R` and CR_slice are free, so P-R fails the hard-to-vary test. Not recommended.

### 4.4 Beyond O-OBSMU: capacities (2) and (4)

Capacities (2) and (4) need a dynamical ingredient. SM §3.1 states a state-dependent coupling
principle. Its explicit construction (SM:112) makes the transfer to site `i` depend on the value
at `i + 1`, so in it the transfer does depend on another region's state. MR★:667 lists it as
outside `K★` and unscreened.

**Proposal P-SDC (not adopted; awaiting the owner).** The native step has SM §3.1-type
state-dependent coupling.

**Failable controls (§A.29).**

- SM's constraints (i)–(iii) (SM:108).
- Substratum's A5-based reconstruction must survive as the reference-class limit (SM:108,
  "the reference derivation chain survives").
- A sourced setting region must pass every foil of #866 c.6567167742.

**Refuting outcome.** The first version's first refuting bullet is withdrawn: SM:112 already
exhibits state-dependent transfer. What remains: if no rule satisfying (i)–(iii) gives a sourced
setting that passes the foils, with a readable record, P-SDC is refuted for that class.

**Independent consequence: none identified.** The gravitational role in SM §3.1 is the
principle's motivation, not a consequence derived from it.

**§A.29.** The switching rule is unconstrained, so P-SDC is easy to vary. Testing it is not
authorized here.

### 4.5 What this note does not establish

- That the architecture is refuted, or that no extension supplies `(Obs, μ)`.
- That O-OBSMU is closed for any consumer.
- That either route of §4.2 is minimal, or that any group-(4) principle exists or cannot exist.
- Anything about window divisibility for native K1.
- That P-R or P-SDC is true, adopted or recommended.
- Any change to a manuscript, ROADMAP, frozen record or Lean module.

## 5. Owner decisions needed

1. **D-OB1, how O-OBSMU is stated.**
   - (a) Split it by consumer:
     - U1–U3 are non-consumers;
     - R1 is support-invariant, pending review;
     - R4 needs nothing beyond Main;
     - L1 and L2 carry Q8;
     - R2, R3, L3, L4 and L5 stay open.
   - (b) Keep it as one open item.
   - (c) Carry it as a named condition `[C: Q8, Q9]` everywhere.
2. **D-OB2, the entry point for O-RDY.**
   - (a) The named-prior option, as #914 already allows.
   - (b) Conditioned patches or cross-time routes, per #914 row 1′.
   - (c) First commission a search for a group-(4) principle, one that generates preparation
     content.
3. **D-OB3, the measure.**
   - (a) Keep Q8 and H-OC_orb as stated, with finite total `S` as a branch premise.
   - (b) Commission a selection argument for Haar measure on compact completions.
   - (c) Ask whether CR_slice (group (2), b-new) should be proposed, with its own §A.29 case. It
     fails control (i) as worded (§4.3).
4. **D-OB4, the arrow of time.** This is tracked as #1112 (ARROW-1). This note records the
   cross-document finding only (S.2.5) and edits no manuscript.
5. **D-OB5, P-R and P-SDC.** Record them unadopted, decline them, or ask for hard-to-vary
   versions. A screen of P-SDC, whether on paper or by computation, is outside the present
   authorization.
6. **D-OB6, review** of Theorem SI, CC-1, CC-2, Proposition G, the §3.4 closedness argument,
   Lemma P-1, Proposition C and Lemma D at the revised head.

## 6. Review packet (revised head)

1. **§1 table:** the U1 description; the R2 and R3 verdicts; the L1 and L2 wording.
2. **CC-2:**
   - the bijection and its inverse;
   - an order-1 gap iff `q ≠ ½`;
   - divisibility on `{0, 1, 2}` iff `q = ½`;
   - full support for every `q ∈ (0, 1)`.
3. **The proofs, which are now complete in this note:**
   - Proposition G, including its product-form paragraph;
   - the §3.4 closedness argument;
   - Lemma P-1;
   - Proposition C, with the definitions of `Ψ_k`, `I_k`, `K_{k+1}`, `π̂` and `K′_{k+1}`.
4. **Theorem SI:** the root-dependent form; the kernel citations (`RecurrenceHorizon.lean:119`,
   `CausalReadback.lean:54`); ELABORATING against Main:141.
5. **§3.5:** the full-support restriction and the null-root convention.
6. **S.2.3–S.2.5:**
   - Appendix A matches Main:746–760 at `D`.
   - Main:756's sentence is attributed to the anti-Boltzmann-brain corollary.
   - H-OC_orb is b-stated (Main:62, :726 (iv), ch01:85).
   - CR_slice is b-new.
   - The Main↔ch18 verdict is limited to that pair.
   - The arrow-of-time finding points to #1112 and quotes its passages accurately.
7. **Lemma D:** D-SEL and S-L4 carried as premises; the scope is K1; Lemma D and S-L4 appear in
   the "Conditional" column of §2.
8. **§4.1:** the Q-table labels, and the four groups kept separate:
   - (1) b-stated;
   - (2) b-new;
   - (3) a b-stated category;
   - (4) none identified.
9. **§4.2:**
   - the two routes, (i) datum and (ii) conditioning;
   - the partial disagreement with the second review's formulation;
   - the list of blocking assumptions.
10. **§4.3–§4.4:**
    - the evaluation of P-R's control (i);
    - "no independent consequence identified";
    - SM:112.
11. **§7:** each reference, individually.

## 7. Off-`main` and non-record references (§A.42 item 8)

Each reference was classified by reading the claim it is attached to.

| Reference | Used where | Classification |
| --- | --- | --- |
| #866 c.6642599988, c.6643204362, c.6643530298 | authorization; owner acceptance of the second review | governance records. They establish no claim |
| #1110 c.6643202940, c.6643501421 (model-authored reviews) | the status line | provenance. They do not verify any result here (§A.46 item 7) |
| #866 c.6600176951 (quoting ROADMAP at `9613b21c`) | §1, the wording of the obligation | provenance. The quoted text is on `main` in `verification/ROADMAP.md` |
| #866 c.6567167742 (the foils) | D-SEL, P-SDC | provenance. The foil list is carried as a named premise (D-SEL); no claim here is supported by it |
| #866 c.6526292899 (controlled lift) | — | replaced by MR-pre:115 (N7), which is on `main` |
| #914 c.6563412926 (rows O-ACC, O-RDY, O-SET, 1′, 3′; C-10) | status labels; S.2.6; §4.2 item 3 | planning record, used for status labels and recorded routes. No mathematical claim here rests on it |
| #914 C-10 (MAP §4, off `main`) | §3.7 | provenance. Proposition C is proved here without it |
| #1007 c.6526897139 | S.2.2, Q8 | governance record. Quoted: "The *principle* is adopted; its infinite-carrier physical adequacy is **not proved**. Finite total-S remains a conditional branch premise where already consumed by recurrence/gauge/reconstruction theorems." (amaybaum, 2026-10-30T15:44:46Z). That Q8 needs finite `S` follows mathematically, independently of the record |
| #1007 c.6527637527, #1017 | — | provenance only. Replaced by the three-state example in Q4 (PD-here) |
| #1009, #1032, #1025, #1112 | status labels (O-SET, O-RET, O-RDY); the arrow-of-time pointer | planning records. They support no claim |
| arXiv sources | §3.8 | external, classified there |

The README lists further #866 comments as reading context: c.6541293037, c.6541615446,
c.6548283392, c.6627392555, c.6631480154 and c.6641545083. They are provenance only, and no claim
here uses them.

No claim here rests on content that exists only off `main`. The proofs this note relies on are
stated in it.

## Appendix A — Main:746–760 at `D`, verbatim

The text below is the exact content of `papers/Main.md` lines 746–760 at `D`, copied with `sed`.

```text
**Setup.** Let $V$ be a partition with hidden sector $B = S \setminus V$. Define the coupling-graph neighborhood $\Sigma_{\text{loc}}(V)$ as the subset of $S$ reached from $V$ by at most $\tau_S / \Delta t$ steps of $\varphi$, where $\Delta t$ is the update step. The exact Koopman operator of $\varphi$ — and of its restriction to any invariant subsystem — is a permutation operator: unitary, with modulus-one spectrum and exact recurrence. It has no dissipative gap; exponential mixing cannot hold for it. Mixing, where it holds, is a property of a *compression*: let $\mathcal{K}_\Sigma := P_\Sigma\, \mathcal{U}_\varphi\, P_\Sigma$ denote the coarse-grained effective channel on the observable algebra of a local region $\Sigma$. **Effective-mixing hypothesis (EM).** *The local effective channel $\mathcal{K}_{\Sigma_{\text{loc}}(V)}$ mixes, with mixing time $\tau_{\text{mix}}(\Sigma_{\text{loc}}(V))$ set by its (dissipative) spectral gap.* (EM) is an explicit physical hypothesis — motivated by local thermalization phenomenology, not derived from $\varphi$ — with the same status as the conditional-mixing curve of (C2).

**Theorem (structural observer selection — conditional on (EM)).** Under the effective-mixing hypothesis, for any partition $V$ of bounded coupling-graph diameter, the hidden-sector memory time of the coarse-grained description generated by iterating $\mathcal{K}_{\Sigma_{\text{loc}}(V)}$ obeys
$$
\tau_B(V) \leq \tau_{\text{mix}}(\Sigma_{\text{loc}}(V)) + O(\varepsilon),
$$
where $\varepsilon$ absorbs typical-set and finite-size corrections. In particular, if $\Sigma_{\text{loc}}(V)$ is in its local equilibrium macrostate in the sense of canonical typicality [31], $\tau_B(V)$ is bounded by the local thermal decorrelation time.

*Proof.* Correlations between a $V$-localized observable $f$ and a $B$-localized observable $g$ at time $t$ require information to propagate from $V$ to $B$ at time $0$ and back to influence the $V$-correlated component of $g$ at time $t$. By the bounded per-step range of $\varphi$ (its causal cone), this round trip stays within $\Sigma_{\text{loc}}(V)$ for $t \leq \tau_S$. In the description generated by iterating $\mathcal{K}_{\Sigma_{\text{loc}}}$ the $n$-step channel is $\mathcal{K}_{\Sigma_{\text{loc}}}^n$, and under (EM) its dissipative gap — which on an equilibrium macrostate sets the local thermal decorrelation rate — bounds the decay of such coarse-grained correlations exponentially at rate $1/\tau_{\text{mix}}$; canonical typicality [31] supplies the local-equilibrium *state*, not the temporal mixing, which is exactly what (EM) posits. Hence $\tau_B(V) \leq \tau_{\text{mix}}(\Sigma_{\text{loc}}) + O(\varepsilon)$. $\square$

**Corollary (anti-Boltzmann-brain).** A Boltzmann brain is by construction a local fluctuation within a neighborhood $\Sigma_{\text{loc}}$ that is itself in local thermal equilibrium — that is what "fluctuation from equilibrium" means. The exclusion is the conditional chain, in the coarse-grained description generated by iterating $\mathcal{K}_{\Sigma_{\text{BB}}}$ (Scope (ii)): (EM) together with $\tau_{\text{mix}}(\Sigma_{\text{BB}}) \ll \tau_S$ implies the candidate partition fails (C2-slow), and hence — by the fast-bath erasure lemma of §2.3, under its uniform-erosion hypothesis — has its order-$k$ readback gap suppressed as $e^{-(k-1)\tau_S/\tau_B}$ for every $k \geq 2$; that gap is what (C4), the condition the characterization actually requires, asserts. For a numeric illustration under a further generic-thermal estimate — (GT): the region's effective-channel correlation time is set by the thermal scale, $\sim \hbar/(k_B T_{\text{local}}) \cdot O(1)$, an estimate that fails for protected slow modes (conserved-quantity bottlenecks, activation barriers, glassy or critical slowing) — the bound is at most $\sim 10^{-12}$ s for temperatures warm enough to support structured matter. The illustration rides (GT); the exclusion itself rides only the chain. Any finite-information observer has $\tau_S$ bounded below by its own internal processing time — for biological or synthetic BBs of any currently-envisioned type, $\tau_S \gtrsim 10^{-6}$ s. The slow form (C2-slow), $\tau_S \ll \tau_B$, therefore fails by at least six orders of magnitude for any BB whose local environment satisfies (GT) — and because (EM) posits genuine mixing rather than mere speed, the record the persistence form (C2-structural) requires is degraded with it: records are scrambled before readback up to a residue suppressed exponentially in $\tau_S/\tau_{\text{mix}}$. The chain bounds the readback gap: by the fast-bath erasure lemma, the failure of (C2-slow) with uniform erosion bounds the order-$k$ gap by $\delta_0\, e^{-(k-1)\tau_S/\tau_B}$ for every $k \geq 2$ — Boltzmann-brain observers so described carry at most exponentially suppressed readback at those orders, and since they fail (C2-slow), within that description they are not observers in the sense of (C1)–(C4) with (C2) read in its timescale form; the fixed-basis quantum representation they trivially possess ($S \iff D \iff Q_{\mathrm{fb}}$) carries no discriminating content. The exclusion is structural, not measure-theoretic — it follows from the incompatibility of (C2-slow) with fast-mixing local equilibrium, not from arguments about the ratio of BBs to "ordinary" observers in an anthropic sample.

**Corollary (past-hypothesis replacement, with its rate condition).** The theorem above bounds $\tau_B(V)\le\tau_{\rm mix}(\Sigma_{\rm loc}(V))+O(\varepsilon)$, while (C2)-slow requires $\tau_S\ll\tau_B$; those do not compose. Contradicting (C2-slow) additionally requires $\tau_{\rm mix}\ll\tau_S$ — the condition the Boltzmann-brain corollary states explicitly. A slowly mixing equilibrium with $\tau_S\ll\tau_{\rm mix}$ is entirely compatible with $\tau_S\ll\tau_B\le\tau_{\rm mix}$, so the valid form is that a sufficiently fast-mixing equilibrium supports no observer satisfying (C2) in its timescale form (C2-slow); for (C2-structural) and (C4) it gives suppression, not exclusion (§2.3). This matters for the de Sitter route, where $\tau_{\rm thermal}\sim\hbar/(k_BT_{\rm GH})=2\pi/H$ is Hubble-order and hence enormously longer than laboratory $\tau_S$: a de Sitter thermal state does not erase observer memory on accessible timescales. Under $\tau_{\rm mix}\ll\tau_S$: For $(S, \varphi)$ in its equilibrium macrostate, canonical typicality [31] implies every local subsystem is also in its local equilibrium. By the theorem — under (EM) for each region's effective channel, in the coarse-grained description it generates — $\tau_B(V)$ is bounded by the local $\tau_{\text{mix}}$ for every bounded-diameter partition $V$. No bounded-diameter partition supports (C2-slow) in that description. That every relevant equilibrium region satisfies (EM) at the required rate is itself a physical hypothesis, to be established model by model; the theorem converts it into the selection rule and does not supply it. In that description, with (C2) read in its timescale form, the framework's observers therefore exist only in the non-equilibrium phase of $(S, \varphi)$. The low-entropy initial condition commonly imported as a "past hypothesis" to select observer-compatible configurations is replaced here, within that description, by a structural selection rule: observers exist where (C1)–(C4), with (C2) read as (C2-slow), are satisfiable, and (C1)–(C4), so read, are not satisfiable in the coarse-grained description of the equilibrium phase.

**Scope.** The theorem uses bounded coupling, finiteness of $S$, the canonical-typicality result [31], and the effective-mixing hypothesis (EM) — the last an additional conditional physical premise, established model by model; it does not follow from isotropy or bounded-coupling regularity. Three scope notes. (i) *Locality of $V$.* The theorem assumes $V$ has bounded coupling-graph diameter. Adversarially non-local partitions — cherry-picking distant subsystems that happen to be correlated — are excluded by that assumption; bounded coupling degree does not by itself bound the diameter of $V$, and the finite response time of a physical observer motivates the assumption. (ii) *Ergodicity.* The gap the argument needs belongs to the coarse-grained effective channel $\mathcal{K}_\Sigma$, not to $\varphi$ itself: the exact Koopman operator of a finite permutation has modulus-one spectrum and cannot mix, so no spectral gap on typical orbits of $\varphi$ is available or assumed. A gap for $\mathcal{K}_\Sigma$ is exactly the content of (EM) and does not follow from statistical isotropy or bounded-coupling regularity. The cycle structure of $\varphi$ does not settle (EM), which concerns the one-step compression: a single cycle does not make the exact compressions relax (below), and orbits of length at most $2$ do not prevent a gap (on four states with cells $\{0,1\}$, $\{2,3\}$, the transposition $(0\,2)$ gives $\mathcal{K}_\Sigma$ with eigenvalues $1$ and $0$). The exact linear rule of [SM §4.2], whose largest energy shell for $d\ge2$ splits into exponentially many cycles, is therefore not excluded by its cycle structure; whether it or the rounded bijection satisfies (EM) is open. The exact $n$-step compressions $P_\Sigma\, \mathcal{U}_\varphi^n\, P_\Sigma$ are compressions of a permutation, recur, and need not equal $\mathcal{K}_\Sigma^n$: for the cyclic shift on five states with a coarse variable marking one of them, they equal $\mathcal{K}_\Sigma$ for $1 \leq n \leq 4$ and the identity at $n = 5$, while $\mathcal{K}_\Sigma^n$ relaxes. The theorem and its two corollaries are therefore statements about the coarse-grained description generated by iterating $\mathcal{K}_\Sigma$; that these iterates govern the exact compressions over the accessible window is not established, and the corollaries do not assert that the exact visible law carries no accessible memory. (iii) *The cosmological realization.* The de Sitter horizon is thermal in the static-patch sense at Hawking temperature, but the globally expanding system is not in equilibrium with respect to any static-observer partition. The horizon's expansion sets $\tau_B \sim H^{-1}$ structurally, not thermally, which is the OI-native mechanism making human-timescale laboratory observation compatible with (C2).
```
