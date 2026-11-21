# BQP-P4: the decisive sub-question for efficient native quantum computation, and its proof plan

**Status: WIP / UNVERIFIED.**
- Design and paper research only: #1169 c.7067281228, round 4.
- Awaiting an independent non-author review.
- This note walks `PLAN.md`, which was committed first at `b534c5c3`.
- Nothing is run. No manuscript, Lean or registry file is edited. No premise is adopted.
- No imported quantum operation is counted as native.

**Inputs.**
- #1514 at `c7a16eb1` (reviewed);
- BQ1, #1498 at `3269772a`;
- OPRES, #1511 at `7669e511`;
- Proposition U, #1504 at `31594967`;
- READOUT-ALG, #1513, a constraint under review and never a theorem here.

Corpus lines are at `main` `df6da1c6`.

**Labels.**
- [R] a reviewed record; [P] a manuscript statement; [W] a derivation here, unreviewed.
- (N) and (I) follow the owner standard.

**Layers.** Each result names its layer on three axes:
- effect, instrument or accessible algebra (E / In / A);
- ontic or Born-form (O / B);
- typing, soundness or operational (T / S / Op).

## 0. Summary

- **Decisive sub-question (DQ-L).** Take a run of poly(n) native steps under OI's own route to
  non-classical correlations: option (a), preparation-indexed adjacency with bounded-degree long
  edges (Main:418; SM:108–110). Is the number L(n) of distinct long edges that the run's
  dependency set can reach polynomial in n? This counts ambient edges, those supplied by the
  environment's own entangling history, as well as edges created by the protocol.
- **Why this one** (P1, §1).
  - BQ1 is a statement at the ontic, operational layer.
  - Of its five hypotheses, four are fixed by named posits or imports, each at the scope stated
    in §1.1. H5 is the exception.
  - H5, a polynomial dependency set, is the only one whose native status is left open by a
    mechanism the corpus actually proposes.
  - Q1, Q2-via-Proposition-U and Q3 fail the selection criterion: each misses S1, S2 or S3.
- **Proof plan** (P2, §2).
  - **Lemma LE.** This is (N) as combinatorics, at [W; O, Op], with a proof given here. Its use
    for H5 is (I) on option (a). Let L count long edges reachable within T steps, and let the
    sites that select which edges exist lie within bounded reference range r_s of the endpoints
    of those edges. Then the dependency set satisfies
    |D| ≤ (|R₀| + 2L)·|B_ref(T + r_s)|, where B_ref(·) is a nearest-neighbour ball.
  - **If L(n) = poly(n):** H5 holds. With BQ1-D, efficient native BQP on the native reading
    would imply BQP ⊆ BPP. Outcome: **OBSTRUCTION**, (I).
  - **If the dynamics can generate long edges, so that L grows superpolynomially:** **ESCAPE**,
    through configuration-indexed adjacency.
  - **Present outcome: INCONCLUSIVE.** The corpus states neither of the two clauses needed:
    - an edge-generation rule;
    - a bound on the long edges reachable from a finite region in T steps (isolation),
      ambient edges included.

    A fixed bounded-degree web of ambient long edges already breaks H5 without generating any
    edge (§2.3).
- **Layer correction to #1514** (P3, §1.2). #1514 §2.2 says "¬R-READ breaks H4 by definition".
  The two hypotheses sit at different layers:
  - H4 is ontic: the outcome is a function of configurations;
  - R-READ is a Born-form effect statement.

  With permutation dynamics and a diagonal prior, ontic configuration readouts have diagonal
  Born-form effects. Main:328 gives the output (MIO) half; the effect (DIO) half is a one-line
  Heisenberg extension [W], below. So ¬R-READ requires a failure of H1 or H2 at the ontic layer, or
  outcomes that are not configuration functions (H4). The correct statement is that ¬R-READ
  breaks at least one of H1, H2 or H4.

## 1. Selection (criterion S1–S3, PLAN §3)

### 1.1 The native reading NR and BQ1's hypotheses

| BQ1 hypothesis | Native status on NR | Label |
|---|---|---|
| H1, second-order rule with polynomial-time F | plain R_q (SM:294; `lyapunov_v3.py:16–19`) holds only on the reference graph. Under option (a) the update reads G(x) neighbours, long edges included, so it is no longer bare R_q. Its second-order form is posit (xiii) of a selected lattice model | (N) for R_q on the reference graph; otherwise (I), posit (xiii) plus polynomial-time F under G(x) |
| H2, input-independent prior samplable in polynomial time | posit (iv): the counting measure, on a finite representative only (Main:54, Main:736). On ℤ^d, product uniform is an added hypothesis. The corpus's other priors are not shown samplable (#1498 B3(c): GR:883, SM:292–296, Main:744) | (I), posit, on finite representatives; an added hypothesis otherwise |
| H3, (xiv) for inputs | (xiv) retained as a posit (Main:410–416), extended beyond its Bell scope | (I), posit |
| H4, polynomial-time configuration readout, charged conditioning | records are configurations. Native repetitions are one longer run under BQ1, so conditioning is charged by that run's length, and no run independence is used | (N) as ontic readout |
| H5, polynomial dependency set | native for the nearest-neighbour rule and polynomial T (Main:368, Main:420). **Open under option (a) long edges** | (N) for the reference graph; open under H-Bell (a) |

"Polynomial T" is the definition of efficiency in native units (AW-2 of #1498).

So on NR, H1–H4 are fixed by named posits or imports, each at the scope in the table. H5 is the
exception: the mechanism the corpus proposes (Main:418) leaves it open.

### 1.2 Why Q1 is not decisive for efficiency (fails S1; layer correction)

- BQ1 is an ontic, operational statement (O, Op). Native output laws are pushforwards of the
  ontic prior under ontic dynamics, whatever Born-form description they receive.
- Theorem C, R-READ and non-DIO are Born-form statements, at the effect or instrument layer
  (B, E/In).
- A native instrument that is non-DIO or non-MIO in Born form, and is realized by configuration
  dynamics with configuration records and an H2 prior, leaves H1–H5 intact. BQ1 then still
  binds.
- Such an instrument cannot in fact be non-MIO or non-DIO in Born form: its visible outputs and
  effects are diagonal.
  - **Outputs (MIO):** Main:328 [P], diagonal preservation under permutation dilations with
    diagonal hidden states.
  - **Effects (DIO) [W]:** a one-line Heisenberg extension, not stated at Main:328. For a
    permutation U, a diagonal μ_H and a diagonal effect f on V × H, the visible effect
    E = Tr_H[(1 ⊗ μ_H) U†(f)U] is diagonal, because U†fU is diagonal.
- So a Born-form native creator or detector requires an ontic ingredient outside H1, H2 or H4,
  and BQ1's hypotheses already track it.
- A positive Q1 answer therefore does not by itself change the efficiency classification. It
  matters only through the ontic hypothesis it breaks. [W; O/B, Op]
- This also corrects #1514 §2.2 at the layer: ¬R-READ breaks at least one of H1, H2 or H4. It
  does not break H4 by definition.

### 1.3 Why the readout-cone n-scaling of Q2 is not decisive (fails S1)

- Proposition U bounds |R| ≥ log rank₊(B) / log|Q|, with B the prepare-and-measure behaviour
  matrix.
- For a fragment with |P| preparations and |M| measurements, rank₊(B) ≤ min(|P|, |M|·k), with
  k outcomes. So for polynomial fragments the bound is at most O(log n). [W; O, Op]
  - These are the trivial factorizations of the plain nonnegative rank, which is what
    Proposition U's lower bound uses.
  - The k|M| factorization is not an ontological-model factorization, since Ξ would then have
    entries indexed by the measurements. The argument needs only the upper bound on rank₊.
- Exponential ontic-state results, such as Montina and Hardy's excess baggage [LIT2], concern
  exact reproduction of *all* states and measurements. Those are exponential fragments, not
  efficient computations.
- Efficiency is therefore a time and dependency-set question, H5, and not a cone-width question.
  Q2 as posed reduces to DQ-L.

### 1.4 Why Q3 is not decisive (fails S3)

Amplification across runs (Main:764 against (C2)/(C4)) bears on efficiency only once a
bounded-error native protocol exists, so it presupposes the answer to DQ-L. It stays
INCONCLUSIVE as #1514 §3.3 left it.

### 1.5 DQ-L meets S1–S3

- **S1.** Each answer gives a different classification: OBSTRUCTION, ESCAPE or INCONCLUSIVE (§2).
- **S2.** DQ-L is stated at the ontic, operational layer, as a property of the dependency graph.
  It makes no Born-form claim.
- **S3.** It needs neither R-READ nor Q1, nor any amplification result.

## 2. Proof plan for DQ-L

### 2.1 Lemma LE (dependency set with long edges)

(N) as combinatorics, [W; O, Op], with a proof given. Its use for H5 is (I) on option (a).

**Setting.**
- Sites ℤ^d, with the reference nearest-neighbour graph G_ref.
- At each step t, the update of site i reads its neighbours in G_t = G_ref ∪ E_t. Here E_t is a
  set of long edges and may depend on the state; G_t has bounded degree.
- **Edge-selection locality (premise).** The configuration values that determine whether an
  edge belongs to E_t lie within reference distance r_s of that edge's endpoints. This is
  constraint (i) of SM:108 in the reference class. For preparation-indexed long edges the
  corpus does not say where the index is stored, so the premise is (I) there.
- Let E* = ⋃_{t<T} E_t restricted to the edges reachable by a dependency path, and L = |E*|.

**Claim.** For a readout region R₀ and T steps, the dependency set, which now includes the
edge-selection sites, satisfies
D ⊆ B_ref(R₀, T + r_s) ∪ ⋃_{u endpoint of E*} B_ref(u, T + r_s). Hence
|D| ≤ (|R₀| + 2L)·c_d·(T + r_s + 1)^d.

**Proof.**
- A site in D is joined to R₀ by a backward dependency path of at most T edges, each edge in
  some G_t.
- If the path uses no long edge, the site lies in B_ref(R₀, T).
- Otherwise, cut the path at its last long edge, nearest the site. The remainder is a G_ref path
  of at most T edges from an endpoint u of an edge in E*, so the site lies in B_ref(u, T).
- The output also depends on the sites that select E_t at each step. By edge-selection locality,
  a selection site for a reference edge is within r_s of a site already in D, and one for a long
  edge is within r_s of an endpoint in E*. Enlarging each radius by r_s covers both. The
  second-order dependence on x(t−1) is a same-site step and changes nothing. ∎

**Scope.**
- The bound is in terms of L, and L may itself depend on the run.
- It does not cover the "equivalent nonlocal response map" variant of Main:418. That variant is
  not a graph. Within ledger item (xiii), each F_i reads finitely many sites (Main:736), but the
  number need not be uniformly bounded (§2.3, item 3).

### 2.2 Combination with BQ1 (plan for Proposition BQ2)

**BQ2 (to be stated and reviewed; (I)).**
- *Hypotheses:* NR, i.e. H1–H4 at the scopes of §1.1, together with option (a),
  edge-selection locality, and L(n) = poly(n) for the **reachable** long edges, ambient edges
  included.
- *Conclusion:* the native run's output law is classically samplable in poly(n). If such runs
  host BQP, then BQP ⊆ BPP.
- *Proof:* Lemma LE gives H5, and BQ1-D applies.
- *Imports:* posits (iv) and (xiv), the latter beyond its Bell scope; H-Bell option (a) as the
  mechanism; polynomial T as the unit of efficiency.
- *Layer:* ontic, operational. Not Born-form, not typing.

### 2.3 The decisive paper step: can L(n) grow superpolynomially?

1. **Preparation-fixed edges.** Main:418 says the long edges are "supplied by a Bell
   preparation", and SM:110 says "prepared states may carry additional bounded-degree,
   preparation-indexed edges".
   - Fixing the edges at preparation does **not** by itself give a polynomial L. The protocol's
     own preparations contribute at most Δ·poly(n) edges. But ambient long edges, supplied by
     the environment's own entangling history, also enter D whenever they are reachable.
   - A fixed bounded-degree web of ambient edges, such as an expander-like chain, gives
     |D| ~ (Δ·|B_ref(T)|)^{#hops} with no edge ever generated. H5 then fails.
   - OBSTRUCTION in this case therefore needs an **isolation premise**: the reachable edge count,
     ambient edges included, is poly(n).
2. **Dynamically regenerated edges.** G(x) is recomputed from the state at every step (SM:106,
   inverse "uses x(t) to determine which graph to apply").
   - In the reference class, constraint (i) keeps graph-dependence local within a bounded range
     (SM:108). Constraint (i) is stated for the reference class only.
   - In prepared states, nothing in the corpus says whether long edges can be created or
     re-attached by the dynamics.
   - If they can, a bounded-degree time-varying graph can have dependency balls of size Δ^T.
     L(n) can then be superpolynomial, and the outcome is **ESCAPE**, through configuration-indexed
     adjacency.
3. **The nonlocal response-map variant.** If it reads a bounded number of remote sites per step,
   it reduces to case 1 or case 2. If the number is unbounded, BQ1's H1 needs re-examination:
   finite reading is preserved but bounded reading is not.

**Cheapest decisive step (paper).** Determine which of cases 1–3 the corpus's G(x) construction
permits:
- from SM §3.1, constraints (i)–(iii) and the prepared-state clause;
- from Main:418's realization of option (a);
- from the H-Bell statement in Substratum §3.2.

The decision rule is fixed now:

| What the corpus fixes | Outcome |
|---|---|
| No dynamic edge generation, **and** the reachable long-edge count from a poly(n) region in poly(n) steps is poly(n), ambient edges included (isolation) | OBSTRUCTION, via BQ2, (I) |
| Dynamic edge generation, or an ambient long-edge web with superpolynomial reachability | ESCAPE, with the generation rule or the ambient connectivity as the named route |
| Either clause unstated | INCONCLUSIVE, naming the missing clauses |

**Present status: INCONCLUSIVE, narrowed.**
- **Substratum:131–133 (H-Bell).** "an entangling preparation supplies bounded-degree
  Bell-relevant long edges (or an equivalent ontically nonlocal response map)". H-Bell's three
  conditions are parameter dependence, no-signaling and curvature stability. None of them states
  whether supplied edges persist, move or multiply under the dynamics.
- **SM §3.1's sparse local-contamination estimate** L_N m_N / N → 0 (Substratum:133) bounds a
  density of long-edge contamination for the curvature step.
  - It does not bound reachability. It expects contamination in typical states, and once
    ρ·|B_ref(T)| > 1, multi-hop reachability can grow superpolynomially.
  - It does not bound the per-run count L(n), and it does not fix an edge-generation rule.
- **Sharpening [W].** Case 1 includes edges supplied by *every* entangling step of a protocol,
  not only an initial preparation. If each entangling step supplies at most a bounded number of
  edges, the protocol's own contribution is O(Δ · #entangling steps) = poly(n). That bounds the
  protocol's edges only, not the ambient edges reachable from its region.
- **Missing premise, stated exactly.** Neither H-Bell nor SM §3.1 states the following two
  clauses:
  - **(M1) Edge generation.** Whether G(x) can create or re-attach long edges outside entangling
    preparations, and if so at what rate per step.
  - **(M2) Isolation (reachability).** A bound, polynomial in n, on the number of long edges
    reachable within T = poly(n) steps from a region of poly(n) sites, including ambient edges
    from the environment's entangling history. It must constrain the connectivity of the ambient
    long-edge graph, not only its density.

  OBSTRUCTION needs both (M1) excluding generation, or bounding it polynomially, and (M2).
  Failure of either is an ESCAPE route.

### 2.4 Preregistered computation (design only; not run; needs its own authorization)

**C-2: exact check of Lemma LE's bound on small instances.**
- **Instances.**
  - A 2D torus of side ℓ ∈ {8, 12, 16}, with k ∈ {0, 1, 2, 4} long edges placed by a fixed seed
    list recorded in advance, and T ∈ {1, …, ℓ/2}.
  - **Amended: chained instances.** For each ℓ, also k ∈ {2, 4, 8} long edges laid as a chain,
    each edge's far endpoint within reference distance ≤ T of the next edge's near endpoint, so
    that multi-hop paths are exercised.
  - Dependency sets are computed exactly by backward breadth-first search. Edge selection is
    static (r_s = 0) in every instance.
- **Decision rule.** Any instance with |D| > (|R₀| + 2k)·|B_ref(T)| refutes the proof of Lemma LE
  as written, and the lemma is withdrawn until repaired. Otherwise the check is evidence about
  those instances only.
- **Relevance.** Low: it checks a proved union bound by enumeration. It is kept as a cheap guard
  on the multi-hop counting.
- **Controls.**
  - k = 0 must give |D| = |B_ref(R₀, T)| exactly.
  - Countercontrol: a graph whose long edges are re-attached each step to fresh sites at
    distance > 2T must exceed every (|R₀| + 2k₀)·|B_ref(T)| for the static edge count k₀. This
    shows that the static count, not the degree, is what the bound uses.
- **Not covered.** Infinite lattices; the response-map variant; any physical claim.

## 3. Established / Assumed / Missing

- **Established** [W, unreviewed]:
  - Lemma LE: (N) as combinatorics (O, Op); its use for H5 is (I) on option (a);
  - the selection argument (§1.2–1.5), including the layer correction to #1514 §2.2 (O/B, Op);
  - the rank₊ ≤ min(|P|, k|M|) observation (§1.3).
- **Assumed:**
  - posits (iv) and (xiv), with (xiv) beyond its Bell scope;
  - KIN, only where Born-form statements are compared (§1.2);
  - option (a) as the mechanism for Bell correlations (H-Bell, open);
  - polynomial T as the unit (AW-2);
  - Main:328 for diagonal preservation of outputs, and its effect-side extension [W];
  - **edge-selection locality** (§2.1), which is (I) for preparation-indexed edges;
  - **isolation (M2)**, a bound on reachable long edges with ambient edges included, which BQ2
    would need and the corpus does not state.
- **Missing.** The earliest unsupported step is the pair of clauses (M1) edge generation and
  (M2) isolation of reachable long edges, ambient edges included (§2.3).
  - Both need a specification of the physical mechanism, H-Bell option (a), not mathematics.
  - Given them, BQ2 is a short derivation.

## 4. What this record does not claim

- It does not claim that efficient native QC is impossible. BQ2 is a plan, and its decisive
  premise is open.
- It does not claim that long edges exist. Option (a) is the corpus's proposed route, and
  H-Bell is open.
- It does not claim a native non-MIO or non-DIO element in either direction, and it does not
  use the abstract full matrix algebra as a supply of operations.
- It uses no BQ1 hypothesis as an established native fact. Each hypothesis is labelled in §1.1.
