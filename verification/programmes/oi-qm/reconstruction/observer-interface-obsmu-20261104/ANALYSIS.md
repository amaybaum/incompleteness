# O-OBSMU — what `(Obs, μ)` needs, what the corpus supplies, and the smallest missing ingredient

**Status: WIP / UNVERIFIED.** Paper-only analysis by `writer-866` under #866 c.6642599988. No
computation was run. Nothing here is independently reviewed, and no statement here is a premise
of an established claim (AGENTS.md §A.46 item 7).

Line anchors `Main:N`, `SM:N` and `Substratum:N` are lines of `papers/` at
`D` = `f5c281ae10a913ec68fa41b3b839ad0b164979cd`. All of the following paths are at `D`:

- `MR★:N` is `../measurement-record-formation/amendments/MR-star.md`;
- `PC★:N` is `../physical-coupling-pc1/amendments/PC-star.md`;
- `SOI-audit` is `verification/audits/operational/stochastic-observer-interface-audit.md`;
- `ROF` is `verification/audits/operational/rooted-observer-family-sourcing/result.md`.

## 0. Conventions

**Support layers.** These are the Code Review Rules' layers, abbreviated as #914 §0 does:

- **KC:** kernel-checked on `main`;
- **PD:** a paper derivation in a record on `main`, with its review status stated where it
  matters;
- **PD-here:** a paper derivation written in this note, not reviewed;
- **CJ:** a conjecture or sketch;
- **OP:** open.

A chain takes the layer of its weakest link.

**Sorting rule** (owner guidance relayed 2026-11-04). Each requirement for deriving `(Obs, μ)`
goes in exactly one group:

- **(a) implied** by OI's existing axioms or theorems, with locator and layer.
- **(b) additional**, meaning not implied by the axioms. Group (b) has two parts, so that nothing
  in it passes as (a):
  - **(b-stated):** a manuscript already states it as a posit, principle, idealization or model
    choice, and labels it as such;
  - **(b-new):** the corpus states it nowhere as a premise of the relevant result.

Two questions are recorded separately for each hypothesis:

- **mathematical validity:** is the statement true under its hypotheses?
- **physical justification:** is the hypothesis derived for native OI, posited, or open?

**Literature.** The owner authorized arXiv searches on 2026-11-04 (relayed by the coordinator),
under AGENTS.md audit step 4. Each source is marked direct or secondary (§3.8). Downloads are kept
outside the repository.

## 1. The obligation, by consumer

The obligation as recorded is quoted in #866 c.6600176951 from the ROADMAP P1 section, frozen at
`9613b21c`: "supply independently motivated structure selecting the physical observation map and
ensemble, or prove that the claims consuming an induced stochastic law are invariant under that
residual choice." Its negative bound is `ensemble_underdetermined` and
`waveSubstratum_stochastic_interface_gap` (KC, `OIBridge/StochasticInterface.lean`; #914 P-7).

This is several obligations, one for each kind of consumer, because the consumers use different
parts of the induced law. The table lists the consumers found in these sources (§A.19):

- `papers/Main.md` and `papers/Substratum.md`;
- `papers/SM.md` §3.1;
- the SOI-audit and ROF;
- the #914 matrix.

It is a census of those sources only, not of every downstream paper.

| # | Consumer | Locator | What it needs from `Obs` | What it needs from `μ` | Invariant under the residual choice? |
| --- | --- | --- | --- | --- | --- |
| U1 | Representation equivalence `S ⇔ D ⇔ Q_fb` on finite horizons | Main §1.5, §3.4; KC `finite_horizon_equivalence` (`Equivalence.lean:462`), `S_imp_D` | a finite outcome alphabet | nothing: it quantifies over all finite-horizon laws | **yes, trivially**: every induced law with a finite alphabet is in its domain (§3.1) |
| U2 | Unavoidable hidden predictive memory; the pushforward identity | Main §1.5, §3.4; KC `pushforward_identity` | a finite alphabet | nothing: it holds in every faithful realization | **yes, trivially** |
| U3 | Reverse finite realization | Main §1.5 (3) | a finite alphabet | nothing | **yes, trivially** |
| R1 | Recurrence-cycle P-indivisibility of the rooted family | Main:137–141; KC `pIndivisible_of_rooted_identity_return_of_overlap` (`RecurrenceHorizon.lean:148`), `isPermMatrix_of_stochastic_inverse` | a product cut `S = C_V × C_H` and the projection `π_V` | the hidden law given each root | **yes, through supports only** (Theorem SI, §3.2, PD-here). **No** when the supports change (countercontrol CC-1) |
| R2 | A C4 gap at a given order `k` | Main §1.3 (C4), Main:141 | product cut, `π_V` | the preparation law | **generically, for fixed supports** (Proposition G, §3.3, PD-here) |
| R3 | P-divisibility on an accessible window; the stochastic route's diagnostic | Main:141 scope; SOI-audit stage 3 | product cut, `π_V` | the hidden law | **open.** The divisible set is closed in the prior (§3.4) |
| R4 | Applying the stochastic–quantum correspondence | Main:526–530 (translation hypothesis (T)); Barandes's tuple (§3.8) | a finite configuration space | a transition map that does not change when the initial distribution is varied | **conditional**: it needs Q9′ (§4.1) |
| L1 | The partition-relativity lemma | Main §1.4 | the partition | the canonical measure, by name | **no**: stated relative to that measure ("the prior is a third datum", Main:86) |
| L2 | Baseline transition matrices; prong 1 of Lemma 3 (doubly stochastic marginals) | Main:60, :62, :276 | product cut | the uniform hidden prior | **no**: the doubly stochastic scope belongs to the uniform prior |
| L3 | Any specific visible law (a Born weight, a correlation, a parameter) | Main:60 remark | the cut | the prior | **refuted as invariant** by Main's own example: "the same bijection and partition under different priors generally yield different visible laws (trivially: the two-state swap under uniform versus point-mass hidden priors)" (Main:60) |
| L4 | Setting screening in the Bell analysis | Main:366 ff. | the wings' cuts | the pre-setting ensemble and its independence from the settings | **no**: the statement is about the ensemble itself |
| L5 | Readiness and records (O-RDY, O-REC) | #914 rows O-RDY and O-REC; MR★:642 | the cut and its access | a ready resource, which is a property of `μ` | **no**: the H-μ measure has no ready region (Lemma P-1) |

**Reading.** The invariance route settles each group differently:

- **U1–U3:** it discharges O-OBSMU outright.
- **R1, R2:** it reduces the μ leg to a choice of support.
- **L1–L5:** it fails, by the manuscript's own counterexample.
- **R3:** it is open.
- **R4:** it is conditional on a preparation-independence assumption.

## 2. The four capacities: what the corpus establishes

"K1" is MR-1's frozen `K★ = {K1}`: the additive second-order step `φ(u_prev, u) = (u, A u − u_prev)`
on the native cubic graph (MR★:461–466). Each row keeps mathematical validity apart from physical
justification.

| Capacity | Established (locator, layer) | Conditional (hypotheses) | Open | Physical justification of the hypotheses |
| --- | --- | --- | --- | --- |
| **(1) Preparation** | Main:60: a realization "carries its own fixed hidden prior `μ_H` as part of the realization datum". This is a stated model datum. Under H-μ, at equal times every region's marginal is uniform and every pair of disjoint regions is independent: Lemma P-1 (PD-here; MR★:642 states it; #914 C-10 cites an off-`main` record). | Rooted laws need conditioning on the observed initial value, not physical preparation (§3.5, PD-here). | O-RDY (#914; RR-1 STAGE-VOID). On K1, no executing process writes a chosen value into a region (MR★:637; S-C1). | A structured `μ_H` is supplied, not sourced (ROF Q3(ii)). Preparation independence is in group (b) (§4.1, Q9′). |
| **(2) Selectable interactions** | On K1, a setting region changes every other region only by an additive offset that does not depend on the carrier's state (MR★ S-L1, S-C1, :491–509; PD in a frozen record; re-derived in Lemma D, PD-here). The controlled lift `F(x, s) = (T_s x, s)` conserves `s` (#866 c.6526292899; PD in a comment, provenance). | — | O-SET is DEFINITION-OPEN (#1009). Non-additive native-type rules are not screened (MR★ σ12, :667). | K1's additivity is Substratum A5. A5 is "partly derived" from amplitude-scale gauge, which Substratum treats as "an explicit operational principle" (Substratum:100, :272): (b-stated). |
| **(3) Accessible outcomes** | A finite outcome alphabet: Main Lemma 1, and Main states that "only finite visible resolution is a theorem" (Main:52, :62; PD with an external holographic input). The owner's principle of observer-relative finiteness (#1007 c.6526897139; planning record, provenance). The region readout is the lattice-cut realization `cutRealization` (KC definition, `PhysicalC4Discharge.lean:582`). | Under H-μ and K1, with a homomorphic readout, every conditional next-step law is uniform on a coset of a subgroup that does not depend on the history (Proposition C, §3.7, PD-here). | O-ACC: is one retained tick of access native, or a convention? (#914 row O-ACC) | The cut exists: this is constitutive of Axiom 1 on the perspectival reading Main adopts (Main:38–40), so it is in group (a). The product form: Main Lemma 2 calls it "idealized" (Main:54), so it is (b-stated). A finite `π : S → V` does not by itself give a product (#1007 c.6527637527; off-`main` #1017; provenance). |
| **(4) Readable, persistent records** | On K1, no confined pattern lasts longer than about twice its width (MR★ S-L4, S-C4a, :531–571; PD in a frozen record, re-read here, not independently reviewed). MR-1 stage 1 ended in a scoped `GAP`; the missing element is `S_A`, an apparatus pointer (MR★ §M.1, :844–870). | P2: no exact two-tick recovery for nontrivial partitions [C: H-μ, K1, H-cur] (#914 P-16; reviewed off `main`). | O-RET (#1032), O-REC (#866). | Finite recurrence bounds every budget (MR★ S-L6). On K1, a record would need an apparatus process that the step does not have (MR★ AW-MR8). |

**Two kinds of capacity.** Capacities (2) and (4) are properties of the dynamics: each holds or
fails at each individual state. Capacities (1) and (3) involve the ensemble and the cut.
Section 3.6 shows that on K1 the obstructions to (2) and (4) are the same for every `(Obs, μ)`.

## 3. The routes, depth-first

Each node closes with the check it names. Productivity test (§A.31), fixed before the walk: a node
counts as a gem if it gives a fact strictly stronger than a restatement and either constrains
something or exposes a hidden assumption.

### 3.0 Node S — the sourcing route

**S.1, the Obs leg.** Checks: Main §1.2; ROF Q1 and Q6; SOI-audit T2.

- **That a cut exists** is in group (a). The observer cut `V ⊊ S` is constitutive of Axiom 1 on
  the perspectival reading Main adopts (Main:38–40), and Lemma 2 states it (Main:52).
- **Which cut** is not implied. Main makes the emergent description a function of the partition
  (Main §1.4), so the cut is a parameter of every law-level claim. A claim stated per declared cut
  does not need the cut selected. A claim about "the" law of our observations does.
- **The product form** `Γ_V × Γ_H` is stated and labelled idealized (Main:54), so it is
  (b-stated).
- **The readout's slice content** (one slice, H-cur, or two, H-2s) is the open question of O-ACC.
- **The two layers.** The reduced `Substratum` record has no observation map (SOI-audit T2; KC
  `readWriteFamily_exists`). The maintained realization layer declares one (ROF Q6). Both
  statements hold, each at its own layer (ROF, "Exact relation to #537").

**Verdict S.1.** The Obs leg is sourced as a family indexed by the declared cut. Within it, the
product form is (b-stated) and the slice content is open. Claims stated per cut need nothing more.

**S.2, the μ leg.** Checks: Main Lemma 3, CanonicalMeasure, SOI-audit T3, #1007.

- **S.2.1, invariance alone.** Invariance does not select a measure. KC
  `ensemble_underdetermined` shows this for every additive substratum with more than one
  configuration. Closed, negative.
- **S.2.2, Lemma 3's selection principle.**
  - Main Lemma 3 states that "the counting measure is selected among invariant measures as the
    maximal-entropy one — a selection principle, not uniqueness from invariance alone" (Main:56).
    This is a posit Main already makes, so it is (b-stated). Kernel support:
    `counting_invariant`, `counting_maximal_entropy` (KC).
  - The principle needs finite total `S`. The owner's principle of observer-relative finiteness
    no longer assumes finite total `S`, which is kept as a conditional branch premise (#1007
    c.6526897139).
  - On an infinite configuration space the counting measure is not a probability measure, and
    entropy maximization is undefined. Haar measure on a compact completion is a candidate
    (PC★:219), but a selection argument for it is still owed (PC★:220).
- **S.2.3, the tension with preparation (gem, NEW as a stated dependency).**
  - Under H-μ, every region is uniform and independent of every other region at equal times
    (Lemma P-1). A ready region, meaning a fixed pattern on `X`, has probability `|S_X|⁻¹`.
  - Main's own observer-selection theorem places observers "only in the non-equilibrium phase of
    `(S, φ)`" [C: EM, finite `S`, bounded diameter, `τ_mix ≪ τ_S`] (Main:748–760).
  - So, on Main's own premises, the observed laws are not drawn from unconditioned H-μ. They are
    drawn from H-μ conditioned on an event in which an observer is present.
  - Main:62 says this in words: "the selection among orbits is fixed by maximal entropy
    compatible with the observer's records".
- **S.2.4, conditional maximum entropy.** Suppose Lemma 3's principle is read as "the counting
  measure conditioned on an event `R`". Then it sources `μ` once `R` is given.
  - **Wall W1:** the corpus has no state-level definition of `R`. C1–C4 are law-level
    diagnostics (Main §1.3). Main's selection theorem concerns the mixing of the coarse-grained
    channel, not a set of microstates.
  - Defining `R` means saying which microstates hold a ready observer and its records. That is
    the object of O-RDY and O-REC.
- **S.2.5, a dependency loop (gem, NEW).**
  - #914 lists O-RDY as depending on the μ leg of O-OBSMU, "or a named prior [C]" (#914 rows
    O-RDY and §0.5 step 1′).
  - By S.2.4, the μ leg, read through Lemma 3's stated principle, needs a readiness event `R`.
    That event is the object of O-RDY.
  - So neither item can come first, unless one of them is carried as a named condition. The only
    non-circular entry point recorded is #914's alternative, "a named prior carried as [C]".

**Verdict S.2.** The axioms do not source the μ leg. Main supplies it only through a posit it
already states (S.2.2). That posit has three limits:

- it needs finite total `S`;
- it conflicts with preparation unless the measure is conditioned;
- it avoids circularity only when a readiness event is named as a condition.

### 3.1 Node I.1 — the invariance route, universal consumers

**I.1.** Consumers U1–U3 quantify over every finite-horizon law on a finite alphabet, or over every
faithful realization. Take any `μ` and any finite readout alphabet: the induced law of
`π_V ∘ φ^t` lies in their domain. Check: Main:99 and the KC `finite_horizon_equivalence`, whose
hypotheses are a finite trajectory space and a stochastic `P`.

These consumers are therefore **invariant**, trivially. They need only a finite outcome alphabet,
which is in group (a): it follows from Lemma 1, or from the owner's principle of observer-relative
finiteness.

**Skepticism.** This branch favours the framework, so the content is stated exactly. This is
invariance by universality: these consumers do not care which law is induced. That says nothing
about which law is physical, and it yields no prediction.

### 3.2 Node I.2 — Theorem SI (support invariance), consumer R1

**Theorem SI (PD-here).** Setting:

- `C_V` and `C_H` are finite sets.
- `φ` is a bijection of `C_V × C_H`, of order `L`.
- For each root `a`, `μ_a` is a probability on `C_H`, the hidden law given the root. Main:137
  takes one `μ_H` shared by every root; here the laws may differ from root to root.
- The rooted maps are `Γ_t(a, j) = μ_a{h : π_V φ^t(a, h) = j}`.

Claim: whether the rooted family is P-divisible on `{0, …, L}` depends on the laws `μ_a` only
through their supports `Σ_a = supp μ_a`.

*Proof.*

1. `Γ_s(a, ·)` is a point mass iff the map `h ↦ π_V φ^s(a, h)` is constant on `Σ_a`. A square
   stochastic matrix is a permutation iff its rows are point masses at pairwise distinct columns.
   Both conditions depend only on the maps `h ↦ π_V φ^s(a, h)` restricted to `Σ_a`.
2. *If every `Γ_s` with `1 ≤ s ≤ L − 1` is a permutation, the family is divisible.* Here
   `Γ_0 = I`, and `Γ_L = I` because `φ^L = id`. So `Λ_{s,t} = Γ_s⁻¹ Γ_t` is a permutation matrix
   for all `s < t ≤ L`, and hence stochastic.
3. *If some `Γ_s` with `1 ≤ s ≤ L − 1` is not a permutation, the family is indivisible.*
   - A square stochastic matrix whose rows have pairwise disjoint supports is a permutation
     (Main:139, paper step). So two distinct rows of `Γ_s` share positive mass at some `x`.
   - Two rows of `Γ_L = I` are at total-variation distance 1. Two rows of `Γ_s` that share mass
     are at distance less than 1.
   - Right multiplication by a stochastic matrix does not increase total-variation distance, so
     no stochastic `Λ` gives `Γ_L = Γ_s Λ`.
   - Kernel support: `pIndivisible_of_identity_return_of_overlap`, cited at Main:145, which
     assumes only that `Γ_s` is row-stochastic. With one shared prior, the rooted form
     `pIndivisible_of_rooted_identity_return_of_overlap` applies directly.
4. By steps 1–3, the verdict is a function of `φ`, `π_V` and the supports `(Σ_a)_a`. `□`

**Corollary SI-1** (full support). Let every `Σ_a = C_H`. Then a row that is a point mass forces
`φ^s({a} × C_H) = {σ(a)} × C_H`, by cardinality and the injectivity of `φ^s`, and distinct roots
then go to distinct columns. So the cycle-level verdict is a property of `(φ, π_V)` alone. The
family is P-indivisible exactly when, at some time within the cycle, the hidden state changes the
visible value from some root. The visible prior plays no role, because the rooted family keeps
every row.

**Countercontrol CC-1 (the support matters; PD-here, worked by hand).** Take
`C_V = C_H = {0, 1}`, `φ(v, h) = (v ⊕ h, h)` and `L = 2`.

- With `μ_H` uniform: `Γ_1 = [[½, ½], [½, ½]]` and `Γ_2 = I`, so the family is not P-divisible.
- With `μ_H = δ_1`: `Γ_1` is the swap permutation and `Γ_2 = I`, so the family is P-divisible,
  with `Λ_{1,2} = Γ_1⁻¹`.

The verdict changes with the support, as Theorem SI allows.

**Skepticism** (the branch favours the framework).

- The consumer is a property of the whole recurrence cycle. Main:141 states that it is not a
  statement about accessible windows, and `L` is far beyond any accessible horizon. So Theorem SI
  discharges the μ leg for a consumer that an observer cannot test.
- The theorem needs the product cut, which is (b-stated).
- It needs finite total `S`, so that `Γ_L = I`. Under the owner's principle of observer-relative
  finiteness, this is a branch premise. #1007's lanes record infinite-`S` constructions without
  synchronized return (#1007 c.6526336447; provenance).
- Gem test: passed. "The verdict depends only on the supports" is stronger than a restatement of
  Main:137. It also constrains the μ leg: for R1, a family of supports is enough, not a measure,
  and the hidden law may even depend on the root.

### 3.3 Node I.3 — Proposition G (generic dichotomy), consumer R2

**Proposition G (PD-here).** Fix `(φ, π_V)`, an order `k`, and a support `Σ ⊆ C_V × C_H` for the
joint preparation law. Consider preparation laws with exactly that support. Then exactly one of
these holds:

- no such law has a C4 gap at order `k`;
- every such law has one, except on a closed set of Lebesgue measure zero in the relative open
  simplex.

*Proof.*

1. A visible history `p = (x_0, …, x_k)` has positive probability iff some point of `Σ` produces
   it. This depends only on the support.
2. Fix two positive-probability histories `p` and `p′` with `x_k = x′_k`, and an outcome `y`.
   Write `N_p(y)` for the probability of `p` followed by `y`, and `D_p` for the probability of
   `p`. Both are linear in the law.
3. The next-step laws after `p` and `p′` differ at `y` iff
   `Q = N_p(y) D_{p′} − N_{p′}(y) D_p ≠ 0`. `Q` is a polynomial in the law.
4. A gap exists iff at least one `Q`, over the finitely many triples `(p, p′, y)`, is nonzero.
   - If every `Q` vanishes identically on the relative open simplex, no law has a gap.
   - Otherwise, the laws with no gap lie in the zero set of a polynomial that is not identically
     zero. That set is closed and has measure zero. `□`

**The product form.** Main's rooted setting uses product preparations `ν ⊗ μ_H`, which form a
lower-dimensional subset of that simplex, so a null set of the simplex need not be null within
them. The same argument works there: `N_p(y)` and `D_p` are bilinear in `(ν, μ_H)`, each `Q` is a
polynomial on the product of the two relative open simplices, and the same dichotomy holds on that
product.

**Skepticism.**

- The dichotomy is generic, not exact: on the exceptional set the verdict differs.
- It does not say whether a gap occurs at an accessible order, which (C4) asks for (Main:80).

### 3.4 Node I.4 — window P-divisibility, consumer R3 (open)

On a finite window `{0, …, n}`, P-divisibility asks for stochastic matrices `Λ_{s,t}` with
`Γ_t = Γ_s Λ_{s,t}`.

1. The set `{(A, AΛ) : A and Λ stochastic}` is compact.
2. The maps `Γ_t` are linear in the hidden law.
3. So, among laws with a given support, the set at which the family is P-divisible is relatively
   closed (PD-here).
4. The relative open simplex is connected. So the verdict is invariant over laws with that support
   iff the divisible set is also relatively open, that is, iff it is empty or everything.

Neither alternative has been shown for any native `(φ, π_V)`, so this node is **open**. Settling
it needs one of two things:

- an argument of the form in step 4;
- two priors with different verdicts on a stated `(φ, π_V)`. Finding such a pair is a
  computation, and computations are not authorized here.

### 3.5 Node I.5 — law-specific consumers L1–L5 (refuted as invariant)

Each law-specific consumer fails invariance:

- **L3:** Main:60's swap example refutes invariance of "the visible law" under the prior.
- **L1, L2:** each names its measure.
- **L4:** it is a statement about the ensemble itself.
- **L5:** it needs a ready region, which H-μ lacks (Lemma P-1).

For these consumers invariance is not available. The μ leg must be sourced, or carried as a named
condition. **Closed: the invariance route does not discharge L1–L5.**

**What survives (PD-here).** For rooted consumers, a visible root need not be physically prepared.
For `ν(a) > 0`, conditioning the preparation law on the observed `X_0 = a` gives the root-`a`
hidden law `μ_a`. So the rooted laws of R1 and R2 are conditional laws given an initial record:
capacity (1) is not needed to obtain them. Preparation independence is needed only where the
initial distribution is varied counterfactually with the transition map held fixed (R4, Q9′).

### 3.6 Node D — the K1 obstructions do not depend on `(Obs, μ)`

**Lemma D (PD-here; the content of MR★ S-L1 and S-C1, re-derived).**

- On K1, `φ^t` is additive. For any partition into regions,
  `pr_Y φ^t(s) = Σ_X Φ^t_{YX}(s_X)`, where each `Φ^t_{YX}` is a fixed homomorphism.
- So the transfer from the carrier region `Σ` to any region is `Φ^t_{·Σ}`, whatever every other
  region holds.
- These are identities in the state `s`. They hold at every state, hence under every `μ`, and
  every readout that is a function of region configurations inherits them.

**Consequence (gem, NEW as a stated reduction).** On K1, no choice of `(Obs, μ)` supplies either
of the dynamical capacities:

- a setting that selects the carrier's transformation (capacity (2));
- a confined pointer (capacity (4)). This also uses S-L4, which is likewise a pointwise statement
  about solutions.

So on K1, O-OBSMU is not the bottleneck for capacities (2) and (4); it bears on (1) and (3) only.
A route to (2) and (4) has to change the dynamics or move to the observer level (MR★ AW-MR8,
:773–785).

This is the superposition principle of additive cellular automata. No source was read for it
(§3.8 item 5).

### 3.7 Node C — the law H-μ induces on K1 (ELABORATING)

**Lemma P-1 (PD-here).** Let `S` be a finite abelian group, `φ` an automorphism of it, and `μ` the
Haar (uniform) measure.

- For any region `X`, `pr_X ∘ φ^t` is a surjective homomorphism onto `S_X`. So the region's law is
  uniform at every time.
- For disjoint regions `X` and `Y`, the equal-time joint law is the product of the two uniform
  laws.
- So a fixed pattern on `X` has probability `|S_X|⁻¹`.

**Proposition C (PD-here).** Take `S`, `φ` and `μ` as in Lemma P-1, and a homomorphic readout `π`.
Let `Ψ_k(s) = (π φ^t s)_{t ≤ k}`. This is a homomorphism; call its image `I_k`. Then:

1. The law of the history is uniform on `I_k`.
2. Define `K_{k+1} = {y : (0, …, 0, y) ∈ I_{k+1}}`. It does not depend on the history. Given any
   positive-probability history `h`, the next value is uniform on a coset `y_0(h) + K_{k+1}`.
3. So `H(X_{k+1} | X_{≤k} = h) = log₂|K_{k+1}|` for every such `h`. Let `π̂` keep the last two
   coordinates, and `K′_{k+1} = {y : (0, y) ∈ π̂(I_{k+1})}`. Then the conditional memory is
   `M_k = log₂ [K′_{k+1} : K_{k+1}]`.

*Proof.*

1. A surjective homomorphism pushes Haar measure to Haar measure.
2. Each fibre of `I_{k+1}` over a point of its projection is a coset of `K_{k+1}`, and all fibres
   have the same size.
3. Hence `M_k = H(X_{k+1} | X_k) − H(X_{k+1} | X_{≤k}) = log₂|K′| − log₂|K|`, with `K ≤ K′`. `□`

**Reading.** Under H-μ and K1, with a homomorphic readout, readback memory is offset memory:

- the past shifts the next-step law but does not change its shape;
- `M_k` is the logarithm of a subgroup index, so for `𝐑 = ℤ/p` it is a multiple of `log₂ p`.

Status: ELABORATING. The equal-time part is #914 C-10 ("R1 as a coset test" [C: H-μ]), which
cites an off-`main` record (MAP §4). The history-independence and the index formula are stated
here. Non-homomorphic coarse-grainings are post-processings of `π`, and their laws need not be
flat.

### 3.8 Literature (AGENTS.md audit step 4)

Each entry records how it was read: **direct** (arXiv ID, exact version, and the section or
page read) or **secondary** (with the secondary source named). External results enter only as
support or challenge. None establishes that a result follows from OI's own assumptions. Where an
external construction supplies part of `(Obs, μ)` or a record mechanism, it counts here only as an
additional assumption in group (b), unless its premises are shown to follow from OI. No such
showing is made in this note.

1. **Barandes, "The Stochastic-Quantum Theorem", arXiv:2309.03085v2.** Read **directly**:
   §3.1, "Indivisible Stochastic Processes", pp. 8–10, equations (24)–(35).
   - The process is the tuple `(C, T, T_0, Γ, p, A)`, with `Γ_ij(t ← t_0) = p(i, t | j, t_0)`, a
     conditional law.
   - The text states: "Only the standalone probabilities `p_1(0), …, p_N(0)` at the initial time
     0 will be taken to be freely adjustable".
   - It states that the definition of `Γ` "is independent of the choice of standalone
     probabilities … at the initial time 0".
   - Use here: to identify what R4 consumes. Instantiating the tuple with an OI realization
     requires the hidden laws `μ_a` given each root to stay fixed while the visible initial
     distribution varies. That is Q9′, which is in group (b). Nothing in the paper supplies Q9′
     for OI.
   - Its divisibility condition (35) is imposed only at conditioning times ("division events").
     It is not the predicate of Main's P-divisibility, which asks for a stochastic `Λ`. ROF
     already records that the two are not identified.
2. **Barandes, "The Stochastic-Quantum Correspondence", arXiv:2302.10778v3.** Read
   **directly**: the abstract page only. Nothing from it is used.
3. **'t Hooft, "The Cellular Automaton Interpretation of Quantum Mechanics", arXiv:1405.1548v3.**
   Read **directly**: the abstract page only. Nothing from it is used.
4. **The Past Hypothesis and the asymmetry of records.** **Secondary** only: the result summaries
   of a web search run on 2026-11-04. Neither the papers nor their passages were read.
   - The summaries attribute an account of the asymmetry of records to a low-entropy initial
     macrocondition (Albert and Loewer).
   - They report that arXiv:2309.03484 ("Laws of Physics") argues the basic Past Hypothesis is
     too vague and proposes a sharper version that picks a particular macrostate.
   - Use here: none as support. It is noted only as the external counterpart of P-R (§4.3),
     which would be a group-(b) assumption, and of P-R's hard-to-vary problem.
   - The passages are to be read before any further use.
5. **Additive cellular automata and the superposition principle** (Lemma D). Standard background.
   No source was read for this note, and Lemma D is derived here directly.

## 4. The smallest missing ingredient

### 4.1 Requirements for `(Obs, μ)`, sorted

| # | Requirement | Group | Locator and layer |
| --- | --- | --- | --- |
| Q1 | A finite outcome alphabet | (a) | Main Lemma 1: "only finite visible resolution is a theorem" (Main:52, :62); PD with an external holographic input. Also the owner's principle of observer-relative finiteness (#1007). |
| Q2 | An observer cut `V ⊊ S` exists | (a) | Main's Definition and Lemma 2 (Main:44, :52). Constitutive of Axiom 1 on the reading Main adopts (Main:38–40). |
| Q3 | Which cut | (b-stated), as a parameter | Main §1.4: laws are relative to the partition. This is a datum of every per-cut claim, not a posit about nature. |
| Q4 | Product form `S = C_V × C_H` | (b-stated) | Main Lemma 2 calls it "idealized" (Main:54). A finite readout does not imply it (#1007 c.6527637527; provenance). |
| Q5 | Slice content of the readout (H-cur or H-2s) | (b), undecided | #914 row O-ACC: native or convention is open. |
| Q6 | `μ` is invariant | (a) | Main Lemma 3; KC `counting_invariant`. |
| Q7 | `μ` is unique | not available | KC `ensemble_underdetermined` (P-7). |
| Q8 | Selection of the counting measure by maximal entropy | (b-stated) | Main Lemma 3: "a selection principle" (Main:56); KC `counting_maximal_entropy`. Needs finite total `S`, which is a branch premise under #1007. |
| Q9 | Root independence: `μ = ν ⊗ μ_H` | (b-stated), at the realization layer | Main:60 ("its own fixed hidden prior"); the hypothesis of Main:137; ROF Q4 (Q8 implies it on a finite product). |
| Q9′ | Preparation independence: the hidden laws `μ_a` given each root stay fixed when the visible initial distribution changes | (b) | Needed by R4 (§3.8). Weaker than Q9, and implied by Q9. Physically, this is a measurement-independence assumption (Main:366 ff.). |
| Q10 | The supports of the hidden laws given each root | (b) | Implied by Q8 (full support). Otherwise not stated. By Theorem SI, this is all R1 needs. |
| Q11 | A ready region: an event of low probability under H-μ | **(b-new)** | Main:748–760 [C: EM] places observers in the non-equilibrium phase but supplies no such event. MR★:642 and Lemma P-1: H-μ has none. |
| Q12 | The measure itself, beyond its support | (b) | Needed by L1–L5 only (§3.5). Q8 gives one measure; conditioning it on Q11 gives another. |

The axioms imply none of Q3–Q5 or Q8–Q12:

- Q3, Q4, Q8 and Q9 are stated in Main, together with their status.
- Q11 is stated nowhere as a premise.

### 4.2 Conclusion by consumer

- **U1–U3:** nothing is missing beyond Q1. This holds at theorem level, by universality.
- **R1 (P-indivisibility over the recurrence cycle):**
  - Needs Q1, Q2, Q4, Q10 and finite total `S`.
  - It needs neither the measure nor root independence: the supports are enough (Theorem SI,
    PD-here).
  - Relative to Main, nothing new is needed.
  - Relative to the axioms, Q4 and Q10 are in group (b).
- **R2 (a C4 gap at order `k`):** the same as R1, holding generically (Proposition G).
- **R3 (divisibility on accessible windows):** open (§3.4).
- **R4 (applying the stochastic–quantum correspondence):** needs Q9′ as well.
- **L1–L5 (specific laws, Bell screening, readiness):**
  - These need a measure. Under Main's own observer-selection theorem, that measure is not the
    unconditioned counting measure (S.2.3).
  - **The smallest missing ingredient is Q11: a readiness event `R` defined at the level of
    states.** Given `R`, the measure follows from Lemma 3's stated principle as the counting
    measure conditioned on `R` (S.2.4).
  - Q11 is (b-new). It is the object of O-RDY, which is why the μ leg of O-OBSMU and O-RDY are
    not ordered (S.2.5).

### 4.3 Proposal P-R (not adopted; awaiting the owner)

**P-R (posited; a proposal only).** For a declared cut `V`, the observer's laws are drawn from
the counting measure, or from Haar measure on a compact completion, conditioned on a declared
readiness event `R ⊆ S`. `R` is a fixed configuration of a declared apparatus region at the time
of preparation.

**Existing results P-R must preserve** (its controls under §A.29):

- U1–U3, unchanged, since they hold for every law.
- Theorem SI and Proposition G, applied with the supports that `R` leaves.
- KC `ensemble_underdetermined` and `invariance_does_not_select`. P-R adds conditioning; it does
  not claim that invariance makes the measure unique.
- Main Lemma 3's statement that maximal entropy is a selection principle, which P-R uses.
- MR-1's scoped `GAP`, and Lemma D. P-R changes no dynamical fact about K1, so it must not be
  reported as supplying capacity (2) or (4) on K1.
- Main:748–760's conditional observer-selection theorem: `R` must lie in the non-equilibrium
  phase, not contradict it.

**Independent consequence, beyond the gap it fills** (PD-here). Take K1, a homomorphic readout
of `V`, and an `R` that is a coset condition (a fixed linear pattern). Then the conditioned
measure is uniform on a coset of a subgroup, and Proposition C still holds:

- every conditional next-step law of the readout is flat on a coset of a subgroup that does not
  depend on the history;
- `M_k` is the logarithm of a subgroup index.

So P-R on K1 predicts that, for every linear readout, the conditional entropy does not depend on
the history.

**Refuting outcome.** Consider a native record law that has been sourced, on a K1 linear readout
from a ready region of coset type. If its conditional next-step entropy depends on the history at
some fixed order, the conjunction (K1, P-R, linear readout) is refuted.

**§A.29 assessment, stated against the proposal.** As it stands, P-R fails the hard-to-vary
test:

- The region and the pattern that define `R` are free. Varying them changes every L-consumer's
  prediction, and nothing in the corpus fixes them.
- Its independent consequence is a theorem of its hypotheses on K1, not a confrontation with
  independent data.
- Secondary reports describe the same vagueness problem for the Past Hypothesis (§3.8 item 4).

**This note does not recommend P-R as a Layer-0 revision.** P-R is the form #914 already allows,
"a named prior carried as [C]", written out with its controls.

### 4.4 Beyond O-OBSMU: the ingredient that capacities (2) and (4) need

By Lemma D, no `(Obs, μ)` supplies capacity (2) or (4) on K1. The ingredient they need is
dynamical: a step in which the state of one region selects the transformation applied to another
(conditional dynamics).

The corpus already contains a principle of that form: SM §3.1's state-dependent coupling graph,
`s(t+1) = φ_{s(t)}(s(t))`. SM gives an explicit bijective construction in which a neighbour's
value selects which site couples (SM:104–110). SM states that this principle is distinct from A6
(SM:104). MR★ σ12 lists it, together with native-Y's rule `h`, as outside `K★` and not screened
(MR★:667).

**Proposal P-SDC (not adopted; awaiting the owner).** The native step has state-dependent
coupling of SM §3.1's form, and such a step can supply a setting that selects operations.

**Controls (§A.29).** P-SDC must preserve, or pass, the following:

- SM's constraints (i)–(iii): graph dependence that is local, centre-independent and
  statistically isotropic (SM:108);
- bijectivity, which is automatic for second-order rules (SM:106);
- finite propagation speed (Main's cone theorem);
- the reference derivation chain, which SM:108 says survives;
- Substratum's reconstruction, which uses A5 on the reference class and must survive as the linear
  reference limit;
- the foils of #866 c.6567167742, which must not pass as setting-dependent interaction:
  - a precomputed selector;
  - post-processing;
  - XOR relabelling;
  - effects that come from `Z_rest` alone;
  - decoy cancellation.

**Independent consequence.** SM introduces state-dependent geometry for background independence,
not for measurement. Suppose one ingredient served both the geometric role (SM §3.1) and the role
of a setting that selects operations. Then the second role would be a consequence beyond the
measurement gap. Whether it serves that role has not been tested.

**Refuting outcome.** P-SDC is refuted for a class of rules if either holds:

- every rule satisfying SM's (i)–(iii) still makes the carrier's transfer independent of an
  embedded region's state, in the sense of #866 c.6567167742;
- its conditional coupling cannot be confined to a bounded setting region without breaking
  (i)–(iii).

**§A.29 assessment.** SM's constraints leave the switching rule unconstrained: the explicit
construction is one choice among many. So P-SDC as stated is easy to vary. It becomes hard to vary
only if an independent requirement fixes the switching rule, such as the gravitational role SM
assigns to it. Testing it is a computation, which is not authorized here.

### 4.5 What this note does not establish

- That the architecture is refuted, or that no extension supplies `(Obs, μ)`.
- That O-OBSMU is closed. Its status here:
  - for U1–U3 it is discharged, by universality;
  - for R1 and R2 it is reduced to a choice of supports, at PD-here level and not reviewed;
  - for R3 and L1–L5 it is open;
  - for R4 it is conditional on Q9′.
- Anything about divisibility on accessible windows (§3.4).
- That P-R or P-SDC is true, adopted, or recommended for adoption.
- Any change to a manuscript, the ROADMAP, a frozen record or a Lean module.

## 5. Owner decisions needed

1. **D-OB1: how O-OBSMU is stated from here.** Options:
   - (a) Split it by consumer:
     - U1–U3: recorded as discharged;
     - R1 and R2: reduced to a choice of supports, once Theorem SI and Proposition G have been
       reviewed independently;
     - R4: conditional on Q9′;
     - R3 and L1–L5: open.
   - (b) Keep it as one open item.
   - (c) Close it as "carried as a named condition [C: Q8, Q9]" for every consumer.
2. **D-OB2: the loop between O-OBSMU and O-RDY (S.2.5).** Options:
   - (a) Record #914's named-prior option as the entry point. O-RDY then proceeds under a named
     readiness event `R` [C], and the μ leg of O-OBSMU is not a prerequisite of O-RDY.
   - (b) Keep O-RDY blocked on O-OBSMU.
   - (c) Commission a definition of readiness at the level of states first.
3. **D-OB3: Lemma 3's measure under observer-relative finiteness.** Options:
   - (a) Keep the counting measure as a branch premise for finite `S`.
   - (b) Commission a selection argument for Haar measure on compact completions.
   - (c) Restate the canonical measure as conditioned on an event in which an observer is
     present, as Main:62 words it. This makes Q11 the open item.
4. **D-OB4: P-R.** Options:
   - (a) Record it, unadopted, as the explicit form of "a named prior [C]".
   - (b) Decline it.
   - (c) Ask first for a hard-to-vary version, with an independent requirement that fixes `R`.
5. **D-OB5: P-SDC and the dynamical gap.** Options:
   - (a) Authorize a paper-only screen of SM §3.1's state-dependent coupling against the foils of
     #866 c.6567167742 and SM's constraints (i)–(iii).
   - (b) Authorize the same screen as a computation, under a preregistration.
   - (c) Defer.

   Options (a) and (b) are outside this workstream's present authorization.
6. **D-OB6: review.** Whether Theorem SI, Proposition G, Lemma P-1, Proposition C and Lemma D go to
   independent read-only review as one packet (§6), before any use beyond this note.

## 6. Review packet

At this note's exact commit, a reviewer checks the following.

1. **The §1 table.** Each consumer's locator and each invariance verdict. In particular, check that
   the kernel statement behind U1 has no hypothesis on `μ` (`Equivalence.lean:462`).
2. **Theorem SI.**
   - Step 1, for root-dependent hidden laws.
   - That the matrix form of the overlap-and-return theorem (Main:145) assumes only a
     row-stochastic `Γ_s`.
   - That `Γ_L = I` holds whatever the hidden laws are.
3. **Corollary SI-1:** the cardinality argument.
4. **CC-1:** `Γ_1` and `Γ_2`, under the uniform prior and under the point-mass prior.
5. **Proposition G.**
   - That `N_p(y)` and `D_p` are linear in the law.
   - That the zero set of a polynomial that is not identically zero on a relative open simplex is
     closed and has measure zero.
6. **§3.4:** that the divisible set is closed.
7. **Lemma P-1 and Proposition C:** the fibre–coset argument and the formula for `M_k`.
8. **Lemma D.**
   - That S-L1 and S-C1 are pointwise identities, so that the reduction "no `(Obs, μ)` supplies
     capacity (2) or (4) on K1" holds.
   - That the scope is K1 only.
9. **S.2.3–S.2.5.**
   - That Main:748–760 is quoted with its conditions: EM, finite `S`, bounded diameter, and the
     rate condition.
   - That the loop with #914's O-RDY row is stated accurately.
10. **§3.8:** the quotations from arXiv:2309.03085v2, §3.1, and the Q9′ reading drawn from them.
11. **§4.1:** that nothing in group (b) is presented as (a). Check Q4, Q8, Q9 and Q9′ in
    particular.
12. **§4.3–§4.4.** That P-R and P-SDC are stated as proposals only, each with:
    - its controls;
    - an independent consequence;
    - a refuting outcome;
    - a §A.29 assessment.

    Check also that neither is adopted.
