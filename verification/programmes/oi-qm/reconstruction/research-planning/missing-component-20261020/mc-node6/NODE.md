# Node 6 (A2 track, node 1): the quantum appearance in an observer's records

Research only, consistency axis (§A.23). No premise adopted, no status changed, nothing written to `main`. This is the
first node of the A2 track (PLAN, "A2 track"), run under the owner's guiding principle of 2026-10-20 and the owner's
node-6 guidance of the same day (three outcomes kept apart; record statistics first; no-go theorems applied with their
exact assumptions; derivation from observational limits preferred over building quantum structure in).

**Base.** Thread records at `research/missing-component-20261020` = `649027c9` (PLAN = `../PLAN.md`, N1 =
`../oa-node1/NODE.md`, MC1–MC5 = `../mc-node{1..5}/NODE.md`, each with its review outcome). `main` = `55a0e80a`;
`papers/` and `verification/lean-mathlib/` are identical to `df9e601e` (`git diff --quiet`), so paper and Lean lines
hold at both. Lean paths are under `verification/lean-mathlib/OIBridge/`; every [AT] name was confirmed by `git grep` of
its declaration at `55a0e80a`.

**Tags.** [AT] adopted kernel theorem; [W] written argument here; [EC] exact computation here (`probe/p6.py`, SymPy
1.14.0, Python 3.13.16, `-I -B`, two runs byte-identical); [NUM] floating-point evidence, never evidence of exactness
(one comparison, B3); [UP] unsourced premise; [L] literature, cited from memory unless stated; [rec] recorded in the
cited record, not re-derived.

**Productivity test (fixed before the node, from the brief).** Gem iff the node yields a fact strictly stronger than
"A2 needs M and R", and either identifies which structural feature of the deeper reality or of the observational
limitation is necessary for the quantum appearance, or exposes a hidden assumption in how the thread has framed the
problem. The owner's node-6 guidance arrived after the test was fixed and before any probe was run; it governs the
classification (§5) and the no-go analysis (§3); the test was not changed.

**Three outcomes (owner, 2026-10-20), used throughout and kept apart.**
- *Emergence*: quantum statistics follow from the deeper dynamics plus limited observation, without assuming the answer.
- *Reproduction*: a model matches QM experimentally but introduces quantum-like structure as an independent assumption.
- *Failure*: the model cannot reproduce a measurable quantum phenomenon.

***

## 0. Headline

1. **The thread's A2 track measures the wrong rung for the guiding principle [W, EC A1–A4; corpus].** There are three
   observables for "the world looks quantum":
   - R0, per-menu representability of record laws (Main §3.4, S ⟺ D ⟺ Q_fb). Every finite law is in it, PR boxes
     included (A4; Main:356), so R0 cannot be the target.
   - R1, the observer's record statistics over one realization, with fixed labelled instruments and their composites,
     agreeing with QM within ε on every finite test. This is the owner's "quantum behaviour in the statistics of an
     observer's records".
   - R2, availability under G3 on the visible carriers (F2's `DenseFiniteQM`). The quantum system is the visible
     configuration register itself.

   MC3's cone lemma and MC5's clauses M and R are R2 statements. They do not bind R1: a κ1–κ4 construction (bijections,
   configuration readout, mixed hidden prior) keeps every visible map in the cone 𝒞(C) (A2), yet its records equal the
   qubit's sequential Pauli statistics on all 234 tested protocols (A1). At R1 the corpus already proves Reproduction:
   one finite reversible realization is mutually ε-dense with operational QM at fixed dimension, outcome bound and
   horizon (Main:576–578, the quantum-shadow realizations). Main:578 and the book (appendix-c:230) name the remaining
   question as **selection**. PLAN's A2 track (PLAN:207–209) omits both and frames the track at R2.
2. **Classification of the A2 question at this node's scope: (c) undetermined.** Reproduction at R1 is established
   (corpus) and is not Emergence, because the shadow realizations code quantum instruments into the hidden tables.
   Failure is established for two constructions: the finite-range, measurement-independent deterministic completion
   for Bell (Main §3.3; B1) and every preparation-noncontextual incompleteness for parity-oblivious multiplexing (C1–C3).
   No Emergence of quantum statistics was found. The decisive open question is the corpus's selection problem, sharpened
   in item 3.
3. **What Emergence at R1 would need (necessary, not jointly sufficient) [EC, W, L]:**
   - *N1, preparation contextuality through operationally invisible, response-relevant memory.* POM success above 3/4
     needs it (C3, [L] Spekkens et al. 2009), and QM gives (1+1/√2)/2 ≈ 0.854, a gap that survives finite precision.
     History readback (C4) does not supply it: a C4-satisfying delay line is preparation noncontextual (C1). Nor does
     knowledge-balance restriction (C2). Bijectivity does not force it (§3.3).
   - *N2, for Bell, a relaxed assumption together with nonlinearity.* Under determinism, either ontic parameter dependence
     or measurement dependence of at least 0.0309 bits is needed (Main §3.3; B2, B3). The level of description is not
     an escape (B1). Remote dependence is not enough either: affine (GF(2)-linear) dynamics with bit readouts stays at
     |S| = 2 across cones (B1m, B1a), so the relaxed structure must be nonaffine.
   - *N3, a magnitude-fixing principle.* Every nonclassicality mechanism found here spans the whole range from the
     classical ceiling to the no-signalling or GPT maximum, with a free weight: S = 2 + 2w for one long edge (B2b), and
     POM success (1+w)/2 for destructive complementary readouts (C5). The quantum values 2√2 and (1+1/√2)/2 sit inside
     that range and are selected by nothing examined. Restriction can overshoot QM (C5 at w = 1 gives POM = 1) as well
     as fall short of it (the toy theory has no Bell violation; book appendix-c:232).
   - *N4, unbounded response-relevant capacity in the precision* (Main:580 item (3); Hardy's excess baggage [L]).
4. **Emergent features found are classical-compatible.** These follow from OI's limits without assuming QM:
   - double stochasticity of uniform-prior one-step laws (D1, a replay of Main §3.1), necessary for unistochasticity;
   - operational no-signalling from graph cones (Main §3.3);
   - C4 memory.

   Each also holds in classical local, noncontextual theories, so none separates quantum from classical record
   statistics.
5. **G6: none.** The preregistered rule (§4) rejects each candidate.

***

## 1. Branch node L1 (B1): which observable is "the world looks quantum"?

### 1.1 What the corpus already claims (§A.19)

- **R0 is universal.** S ⟺ D ⟺ Q_fb on every finite horizon (Main:82, :532; `finite_horizon_equivalence`,
  `Equivalence.lean`). Main:534 says representability is not the discriminating content. Main:356 says bare finite OI
  representability realizes PR-box behaviour.
- **R1 Reproduction is a corpus theorem.** The uniform continuum realization (Main:576) gives one finite reversible
  realization R, mutually ε-dense with the operational quantum theory at fixed d, m and K. The finite-test density
  corollary (Main:578) states: "As classes this is density, not identity: D_finite is strictly larger — the
  response-table construction realizes arbitrary finite stochastic behavior, quantum or not … the remaining question
  (route (ii)) is the operational-lifting problem". The single-dynamics corollary (Main:560) makes it one map with a
  program register.
- **The selection problem is named.** Book appendix-c:230 ("Whether embedded observation selects the non-commutative
  structure is the framework's open selection problem"); appendix-c:232 ("restricted access does not by itself single
  out quantum theory").
- **The kernel's emergence result is R2-shaped and is a uniqueness.** `QuasilocalCharacterization.lean`:
  - the region completion is the unique member, up to canonical isomorphism, of the class of quasilocal systems with the
    substratum's configuration matrix algebras as stages (`systemEquiv_unique` :385, `canon_unique` :359);
  - with dynamics, two OI systems with the same substratum dynamics are canonically isomorphic (`systemEquiv_dyn` :497);
  - the induced dynamics has real transported entries, and a one-site phase is induced by no reversible finite-range
    substratum dynamics (`phaseQ_ne_heisQ` :792).

  Per §A.34 this is uniqueness given those stages. It does not derive quantum statistics, and its quantum system is the
  configuration algebra: G3 on visible carriers, which is R2.

### 1.2 The checks [EC]

- **A0–A1.** A Spekkens-type toy bit as an OI construction:
  - hidden ontic pair (a, b), fresh hidden disturbance bits r_t, visible pointers p_t;
  - measurement Z: p ^= a, then b ^= r; X: p ^= b, then a ^= r; Y: p ^= a⊕b, then a ^= r and b ^= r. Every step is a
    bijection of the 2^8 states (A0);
  - preparations are mixed priors on a pair of ontic states.

  Records equal sequential Lüders records of the six qubit Pauli eigenstates for all 39 sequences of length ≤ 3, 234/234
  exact (A1), with complementarity and order dependence (A1b).
- **A2.** The pointer's induced map for one measurement has four 0/1 partial-permutation Kraus operators. Its Kraus
  channel equals Ad_U followed by the partial trace on all four matrix units. This is the cone lemma on the visible
  carrier.
- **A3.** The same carrier admits non-disturbing bijections (p ^= a without r). They are bijective (A0), and their
  records leave QM: an X repeat survives an intervening Z. The qubit-like restriction is a choice of accessible
  bijections, not a consequence of κ1–κ4.
- **A4.** A response table with global setting dependence gives S = 4. R0 contains non-quantum laws.

### 1.3 Verdict at L1

The thread's A2 track is framed at R2. The cone lemma (MC3) and clauses M and R (MC5) concern operations available on
visible configuration registers under G3. At R1, interference-type and non-real-basis (Y) record statistics are met by
κ1–κ4 constructions (A1; Main:576), as Reproduction. The obstruction that remains at R1 is not M or R. It is the gap
between Reproduction and Emergence: κ1–κ4 is universal at R0 and dense at R1 (Main:578), so it constrains nothing until
a selection principle is added.

**Hidden assumption HA-6.1.** The A2 track (PLAN:205–212) equates "agree with QM to arbitrary accessible precision"
with `DenseFiniteQM` under G3, so that M and R become requirements "at every precision". Under the guiding principle
these are R2 requirements. At R1 the corpus already has Reproduction, and the open item is selection (Emergence).
Class: ELABORATING (Main:578 and appendix-c:230 state the selection problem; the A2 track omitted it).

**Decisive branch for L2.** A selection principle has to meet the no-go theorems at R1. These are the constraints that
bind record statistics whatever the observable rung, so L2 applies them with their exact assumptions.

***

## 2. Branch node L2 (B2/B3): necessary features, with each theorem's exact assumptions

Owner safeguard: no conclusion that OI needs a quantum or nonlocal substratum. For each theorem, the table states which
assumption an observationally incomplete model satisfies or relaxes, and then tests whether the observed statistics can
still be reproduced.

### 2.1 Assumption table

| theorem [L] | assumptions | OI's κ1–κ4 class | relaxation available | reproduces? (check) | outcome |
|---|---|---|---|---|---|
| Bell / CHSH, Main's ceiling (i)–(iv) | determinism; settings as interventions; readout before cones meet; one setting-independent pre-setting ensemble; response-complete Ω. In Jarrett's split, outcome independence is automatic under determinism, so the burden falls on parameter independence | determinism constitutional; graph cones exact for finite-range φ; measurement independence a property of the prior, retained by the corpus (Main:82) | ontic parameter dependence (Main's adopted branch (a)); measurement dependence (branch (b), recorded); readout after cone crossing | local and measurement-independent: no (B1, \|S\| ≤ 2 exhaustively). One long edge: yes, S = 4 with operational no-signalling (B2), and S = 2 + 2w for any rational w (B2b). Measurement-dependent local: yes, any S, within Main's bound (B3 [NUM]) | Failure (local, measurement-independent). Reproduction (either relaxation), with S a free weight |
| level of description (is the trace-out an escape?) | records are averages of pointwise boxes | — | — | no: B1 computes the records after the trace-out, with hidden memory present | not an escape (Methodology:385 agrees) |
| Bell with nonlinearity | — | 2-bit reversible blocks are all affine (B1m); SM's reference update is linear over ℤ/qℤ (SM.md:296) | nonaffine gates or state-dependent adjacency (SM.md:112, Main §3.3 preparation-indexed edges) | affine dynamics with bit readouts: \|S\| = 2 at every Ω even with remote dependence (B1a, 48 remote-dependent boxes); a Toffoli-class long edge reaches 4 (B2) | remote dependence is necessary but not sufficient; nonaffinity is needed as well [EC for GF(2); W beyond] |
| Kochen–Specker | outcome determinism; measurement noncontextuality (an observable's value independent of the commuting context) | outcome-deterministic; the response is a function of the whole measurement bijection, i.e. of the context | context-dependent responses, automatic | yes: Peres–Mermin has no noncontextual assignment (0/512) and has context-indexed ones (K1). Main:550 keeps implementation fixedness of labelled instruments and contextual outcome values | no constraint at R1 beyond the corpus's conditional statement |
| preparation contextuality (Spekkens 2005; POM, Spekkens et al. 2009) | ontological-model framework (Λ, μ_P, ξ_M); preparation noncontextuality (operationally equivalent procedures have equal μ) | OI induces an ontological model: Λ the response-relevant microstate, μ_P from the prior and bijections, ξ deterministic. The framework applies. The observer's description is the operational class of a procedure; the epistemic object is μ_P | PNC is neither implied nor excluded by κ1–κ4 (C1, C2 noncontextual; C4, C5 contextual) | PNC models: POM ≤ 3/4 (C3, exact LP). Contextual: up to 1 (C5), and 17/20 at N = 100 for a hidden-label model (C4) | Failure for any PNC incompleteness (knowledge balance, C4-type readback alone). Reproduction (C4); Emergence of contextuality with a free magnitude (C5) |
| PBR | framework; preparation independence (product preparations give product μ); quantum predictions for an entangled measurement | the canonical uniform prior is a product, so PI holds when the systems' response-relevant hidden data are disjoint blocks [W]; it fails when they share hidden data (co-embedding, Methodology:389) | shared hidden sector | not computed. With PI, R1 Reproduction needs ψ-ontic response-relevant data [L]; the shadow realizations store state and instrument labels, so they are ψ-ontic [W] | constrains Emergence accounts with disjoint hidden partners to ψ-ontic data. With a shared sector, PBR does not bind |
| ψ-epistemic overlap bounds (Barrett–Cavalcanti–Lal–Maroney 2014; Leifer 2014) | framework only, d ≥ 3, exact QM; robust forms exist [L, not read] | framework applies | — | not computed | a ψ-epistemic Emergence account cannot attribute most nonorthogonal indistinguishability to ontic overlap at large d [L] |
| Hardy excess baggage | framework, exact qubit statistics | finite Λ at any fixed stage | — | Main:580 item (3): no fixed finite classical carrier reproduces full qubit behaviour | response-relevant capacity must grow without bound in the precision (N4) |

Whether an observer's description counts as an epistemic state in PBR's sense [W]: PBR's ψ labels a preparation's
operational statistics. At R1, a tomographically complete quantum-appearing theory fixes ψ from the statistics. The
non-uniqueness of the fixed-basis dilation Θ (Main:212 (i)) concerns the R0 representation, not the operational state.
So the framework applies to OI at the level of procedures. The assumption OI can relax is PI, not the framework.

### 2.2 Verdicts at L2

- **Bell (CONFIRMING with exact OI-native instances; one narrow addition).** Main §3.3 and Methodology:393 already
  state the ceiling, the two relaxations and that "no-signaling, hidden memory, and indivisibility are all insufficient
  by themselves to select the quantum correlation set". The addition is narrow: remote dependence through affine
  dynamics with bit readouts cannot exceed 2. The relaxed structure must be nonaffine. The reference SM update is linear
  over ℤ/qℤ, and the state-dependent graph is not (SM.md:112, :296). This is [EC] for GF(2) and [W] for ℤ/qℤ with
  homomorphic readouts. With a non-homomorphic readout on ℤ_q, q ≥ 3, the readout itself is a nonlinearity, and that
  case was not checked.
- **Preparation contextuality (the decisive sub-branch: absent from the papers).** `git grep -i "preparation
  contextual"` over `papers/` returns nothing; Main:550 disclaims Spekkens noncontextuality without using it.
  - **C1.** A delay line (x, h) ↦ (h, x) satisfies C4 exactly: P(x₂ = 0 | x₁ = 0, x₀ = 0) = 1 and
    P(x₂ = 0 | x₁ = 0, x₀ = 1) = 0. Its record map on hidden distributions has rank 4/4, so operationally equivalent
    preparations have identical ontic distributions: it is preparation noncontextual.
  - **C2.** The toy bit's single-measurement statistics already determine the ontic distribution (rank 4/4).
  - **C3.** Exact LP over all models on four ontic states with every deterministic response function: under PNC with
    parity obliviousness, the maximum POM success is exactly 3/4, and with the toy's decodings also 3/4. Without
    parity obliviousness it is 1 (countercontrol).
  - **C4.** A hidden-label construction stores which of the four Bloch vectors was prepared and a uniform u ∈ {0,…,N−1},
    and writes [u < N·round_N(p)] into a pointer, which is a bijection. It is parity-oblivious exactly, on 16 XZ-plane
    axes and ±Y. Its success is 3/4, 7/8 and 17/20 at N = 4, 8 and 100. Its parity mixtures have disjoint hidden-label
    supports. Reproduction: the Born weights are coded into the table. At N = 8 it overshoots QM (7/8 > 0.854), as an
    ε-approximant may.
  - **C5.** On a classical 2-bit ontology, the accessible readouts are destructive and complementary: reading bit y
    XORs fresh hidden randomness into the other bit. The construction is a bijection, is parity-oblivious on all 14
    sequences of length ≤ 3 (and so on adaptive ones of that length), and its parity mixtures differ ontically. With
    weight w on the deterministic preparation, success is exactly (1 + w)/2: 1 at w = 1, 17/20 at w = 7/10, and 3/4
    at w = 1/2. Contextuality emerges from a limit on observation, with a free magnitude that reaches the GPT maximum
    (this is the gbit; Barrett 2007 [L]).

  **Necessary feature N1 [EC; L].** An incompleteness that reproduces the quantum POM value at any precision better than
  0.104 must be preparation contextual. The hidden sector must retain response-relevant preparation information that no
  accessible protocol reveals. C4 concerns memory that is read back; N1 concerns memory that is never read back. C1
  shows C4 does not imply N1, and C2 shows the toy bit's knowledge balance does not either.
- **Magnitude (N3).** B2b and C5 have the same structure. A mechanism that produces the nonclassical feature at all
  produces every value from the classical ceiling (2; 3/4) to the maximum (4; 1), set by a prior weight. The quantum
  values (2√2; (1+1/√2)/2) are interior and unselected. This is §A.29's adjustable-to-any-outcome pattern, in two
  independent settings. Observed Bell values are not above 2√2 beyond error [L]; under §A.24 that is a raw-direct
  datum, which these mechanisms accommodate only by tuning w.

### 2.3 Pressure test of the favourable readings (§A.31)

- *C5 as Emergence.* The destruction is a hidden-randomness coupling. A non-destructive bijection on the same carrier
  exists (the A3 analogue), so the restriction is a posit about which bijections the observer can implement. It is a
  limit on observation and assumes no QM, so the label Emergence (of contextuality) holds. But at w = 1 it predicts POM
  = 1, which QM forbids and which a finite-precision experiment separates. As a model of QM it is Failure at w = 1 and
  Reproduction only when w is tuned to 1/√2.
- *B2/B2b as support for branch (a).* B2 shows the adopted branch can reproduce quantum S values. B2b shows it fits
  every S in [2, 4] equally well. That is support for Reproduction, not for Emergence.
- *A1 as a derivation.* The 234/234 match is guaranteed by the toy theory's construction (the stabilizer fragment).
  It shows that R1 is not bound by the cone lemma. It is no evidence for Emergence (A3).

### 2.4 Node L3: does bijectivity supply N1? [W]

Reversibility forbids erasing the difference between two preparation procedures, so the difference persists somewhere in
the global microstate. In the toy construction it persists in the preparer's record register, while the system's
response-relevant marginals of operationally equivalent mixtures are identical (C2: noncontextual). So bijectivity
places the information but does not put it into the response-relevant hidden data. **Verdict: N1 is not supplied by
bijectivity or by C4. It is an additional requirement on the trace-out.** [W, with the C2 instance.]

***

## 3. Branch node L4 (B4): G6 at A2

**Decision rule, fixed before this section (MC5 §7 control 5):** a candidate counts iff it gives a finite-precision
statistic that differs from QMfin on some protocol, its size is fixed by OI quantities without free parameters, and both
outcomes are possible.

| candidate | verdict |
|---|---|
| finite-N discretization of Born weights (C4, Main:576 nets) | size set by N, a free stage parameter: rejected |
| super-quantum POM or CHSH at untuned weights (C5, B2b) | size set by w: rejected; the observed values constrain w (accommodation) |
| a capacity limit on generic entanglement: response-relevant memory or computation exponential in the number of entangled qubits, against C3's ~10^122 (Main:78) | threshold logarithmic in the capacity (n ~ 400 for memory) but construction-dependent: the shadow nets cost O(m·16^n·log 1/δ) record bits (Main:576), the lower bounds rest on complexity conjectures and Markovian-model theorems [L: Montina 2008; Regev–Klartag 2011; Davies 2007, not read], and the deviation's form is unspecified. Size not fixed: rejected. Recorded as a direction only |

**Verdict: no G6.**

***

## 4. Controls (§A.29)

| # | control | type | outcome |
|---|---|---|---|
| 1 | cone lemma reproduced on the toy construction's visible carrier (A2): Kraus channel against the Ad_U and partial-trace route | must-hold, two code paths | holds |
| 2 | non-disturbing bijections on the same carrier leave QM (A3) | can-fail: would fail if κ1–κ4 forced the restriction | QM fails as predicted |
| 3 | Bell ceiling under OI's actual readout, local automaton (B1) | must-hold | \|S\| ≤ 2 on 576 rule pairs × 64 microstates. Deterministic local boxes give ±2 at every point, so attainment is automatic; the can-fail element is the cone check |
| 4 | cone check sensitivity (B1m): four steps on the same ring | can-fail countercontrol | remote dependence detected at 23 552 points |
| 5 | PR negative control (Main:407 calls it mandatory): one nonaffine long edge (B2) | must-fail for locality | S = 4, operational no-signalling |
| 6 | PNC POM ceiling (C3) | must-hold; theorem instance [L], not independent | 3/4 |
| 7 | POM without parity obliviousness (C3) | can-fail countercontrol | 1 |
| 8 | KS operator identities computed (K1) | must-hold | hold |
| 9 | Main §3.1 replay (D1): 21 matrices, 6 failing the necessary condition | replay of a recorded count | matches |
| 10 | PLAN controls: `permTheory_not_qm`, `substratum_residual`, rooted law and M1, K_B/K(Z_F)/Γ(Q3), no E0 positing | — | not engaged: no candidate is proposed at R2. At R1 the analogue of "representability does not stand in for availability" is control 2 together with A4 (R0 does not stand in for R1) |
| 11 | G6 with preregistered rule | — | fails (§3) |

***

## 5. The three outcomes, classified

| result | outcome | why |
|---|---|---|
| toy-bit construction (A1) | Reproduction of the stabilizer fragment; Failure for POM > 3/4, Bell and continuous interference | the knowledge-balance restriction is an independent posit (A3); PNC (C2) |
| quantum-shadow realizations (Main:576–578), hidden-label model (C4) | Reproduction | quantum instruments and Born weights are coded in the hidden tables |
| local, measurement-independent deterministic completion (B1; Main §3.3) | Failure | \|S\| ≤ 2 |
| long edge (B2, B2b), measurement dependence (B3) | Reproduction possible; over-generates | S is a free weight in [2, 4] |
| destructive complementary readouts (C5) | Emergence of preparation contextuality; Failure at w = 1 (POM = 1); Reproduction only at tuned w | the restriction assumes no QM, but its magnitude is free |
| double stochasticity under the uniform prior (D1), operational no-signalling (Main §3.3), C4 memory | Emergence of classical-compatible features | each holds in classical theories; none separates |
| Emergence of quantum statistics proper | none found | — |

***

## 6. Re-reading node 5's headline under the guiding principle

Each sentence below attributes to OI, or to the empirical question, what was shown for operations under G3 on visible
carriers (R2) or for the listed constructions. Proposed scoping in brackets.

1. MC5:298–300, "What is empirically at stake … M and R are needed at every precision, so their realization question
   cannot be avoided by relaxing exactness." [Add: "as available operations under G3 on visible carriers (R2)". At the
   level of record statistics (R1), interference and non-real-basis statistics are reproduced by κ1–κ4 constructions
   (Main:576; mc-node6 A1). The empirical question at R1 is selection, not M and R.]
2. MC5:52–56 (§0 item 3) and :293–294, "No construction examined supplies M by substratum dynamics while keeping
   κ2 … and supervenience". [True at R2. Add "as an available operation". At R1, κ2 and supervenience are kept by the
   toy bit and the shadow realizations, which supply M-type record statistics as Reproduction.]
3. MC5:40, "and no source exists in OI for the constructions examined". [The clause joins an unscoped "no source exists
   in OI" to a scope. Proposed: "no construction examined supplies a source".]
4. MC5:48 and :275, "(i) is ruled out …", "(i) Can it emerge from OI? Ruled out for these constructions". [Scoped
   correctly as written. Under the guiding principle, "emerge" should read "emerge as available operations (R2)". The
   owner's Emergence question at R1 is open (mc-node6 §0 item 2).]
5. PLAN:207–209, "M and R are needed at every precision … The track therefore has to address interference (M), complex
   phases (R), and entanglement with multi-system compatibility (O-B) directly". [Same scoping as item 1. At R1 the
   track's task is Emergence: a selection principle meeting N1–N4.]

MC5's §4 list of excluded constructions, its "not a claim about every observer-level extension" and its §9 scope note
are correctly scoped and need no change.

***

## 7. Hidden-assumption markers

| # | assumption | where | finding | class |
|---|---|---|---|---|
| HA-6.1 | A2 means `DenseFiniteQM` under G3, so M and R bind "at every precision" | PLAN:205–212; MC5:298–300 | R2 framing. At R1 the corpus has Reproduction (Main:576–578), and the open item is selection | ELABORATING (Main:578; appendix-c:230) |
| HA-6.2 | C4 (history readback), OI's discriminating content, carries the hidden memory the quantum appearance needs | Main:534 reads C4 as discriminating against Markov, not against classical; the A2 track is silent | C4 does not imply preparation contextuality (C1). The needed memory is response-relevant and never read back (N1) | BORDERLINE: no paper claims C4 suffices, but N1 is absent from the papers and from the thread |
| HA-6.3 | an access restriction can only under-generate relative to QM (the toy-theory lesson, appendix-c:232) | appendix-c:232 | restriction can also overshoot: destructive complementary readouts give POM = 1 (C5). Restriction bounds nonclassicality from neither side | ELABORATING (gbit/boxworld standard in GPT literature [L]) |
| HA-6.4 | ontic parameter dependence suffices for S > 2 under measurement independence | Main §3.3 phrasing "reproducing them requires ontic parameter dependence" (necessity, correctly stated) | necessary, not sufficient: affine remote dependence stays at 2 (B1a). Nonaffinity is needed; SM's reference update is linear | ELABORATING (narrow; Main states necessity only) |
| HA-6.5 | Bell is the sole place where the magnitude of nonclassicality is unselected | Methodology:393 | the same free-weight pattern appears in single-system preparation contextuality (C5) | ELABORATING |

Assumption-watch markers:
- **AW-MC6-1.** A claimed A2 result names its rung: R0 (representability), R1 (records under one realization with fixed
  labelled instruments and composites) or R2 (G3 availability). The cone lemma and clauses M and R are R2.
- **AW-MC6-2.** A positive-looking result is classified as Emergence, Reproduction or Failure. Matching QM by coding
  instruments, Born weights or a tuned weight into the hidden sector is Reproduction.
- **AW-MC6-3.** Emergence at R1 must meet N1 (invisible response-relevant preparation memory), N2 (a relaxed Bell
  assumption with nonaffine structure), N3 (a magnitude-fixing principle that excludes PR and gbit values and permits the
  quantum ones) and N4 (capacity unbounded in precision).
- **AW-MC6-4.** No-go theorems are applied with their exact assumptions. The OI-induced ontological model satisfies the
  framework; what it can relax is measurement independence, parameter independence, PNC, measurement noncontextuality
  and PI. None of these relaxations by itself makes the substratum quantum, and none selects the quantum magnitude.

***

## 8. Literature (Step 4)

Cited from memory. Bibliographic data not re-verified, texts not read in this node, except the corpus's own citations
as they appear in Main.
- J. S. Bell, Physics 1, 195 (1964); S. Kochen, E. P. Specker, J. Math. Mech. 17, 59 (1967); A. Peres, Phys. Lett. A
  151, 107 (1990); N. D. Mermin, Phys. Rev. Lett. 65, 3373 (1990); J. P. Jarrett, Noûs 18, 569 (1984).
- R. W. Spekkens, Phys. Rev. A 71, 052108 (2005) (preparation contextuality); R. W. Spekkens, D. H. Buzacott, A. J.
  Keehn, B. Toner, G. J. Pryde, Phys. Rev. Lett. 102, 010401 (2009) (parity-oblivious multiplexing); R. W. Spekkens,
  Phys. Rev. A 75, 032110 (2007) (toy theory); S. D. Bartlett, T. Rudolph, R. W. Spekkens, Phys. Rev. A 86, 012103
  (2012) (epistemically restricted Liouville mechanics); D. Schmid, J. H. Selby, E. Wolfe, R. Kunjwal, R. W. Spekkens,
  PRX Quantum 2, 010331 (2021) (noncontextuality iff simplex embeddability).
- M. F. Pusey, J. Barrett, T. Rudolph, Nat. Phys. 8, 475 (2012); P. G. Lewis, D. Jennings, J. Barrett, T. Rudolph,
  Phys. Rev. Lett. 109, 150404 (2012); J. Barrett, E. G. Cavalcanti, R. Lal, O. J. E. Maroney, Phys. Rev. Lett. 112,
  250403 (2014); M. S. Leifer, Quanta 3, 67 (2014); L. Hardy, Stud. Hist. Phil. Mod. Phys. 35, 267 (2004).
- B. S. Tsirelson (Cirel'son), Lett. Math. Phys. 4, 93 (1980); S. Popescu, D. Rohrlich, Found. Phys. 24, 379 (1994);
  J. Barrett, Phys. Rev. A 75, 032304 (2007) (GPTs, gbit); M. Pawłowski et al., Nature 461, 1101 (2009); M. Navascués,
  Y. Guryanova, M. J. Hoban, A. Acín, Nat. Commun. 6, 6288 (2015).
- A. Montina, Phys. Rev. A 77, 022104 (2008); O. Regev, B. Klartag, STOC 2011; P. C. W. Davies, Fluct. Noise Lett. 7,
  C37 (2007).
- Corpus citations used as cited there: Barandes–Hasan–Kagan, arXiv:2512.18105 (Main ref. [24]); Hall–Branciard (Main
  ref. [57]).

***

## 9. Not verified

- R1 is defined here in words (§0 item 1). No formal definition, kernel or otherwise, is given. Whether R2 with the
  domain premises implies R1 is [W].
- A1 covers the six Pauli eigenstates and sequences of length ≤ 3. Mixed preparations and longer sequences are not
  checked. The match is guaranteed by construction and is not evidence for Emergence.
- B1 is a ring of 8 with 2-cell blocks, two steps, exhaustive over rules. The automaton is affine (B1m), so B1 tests the
  cone path, not nonaffine local dynamics. The general local ceiling is Main's theorem [rec], certified in the corpus
  (`equivalence_recovery_probes.py` check 11 [rec]). A nonaffine local exhaustive check was not run.
- The nonaffinity claim (N2) is [EC] for GF(2)-affine dynamics with bit readouts. For linear dynamics over ℤ/qℤ with
  homomorphic readouts it is [W]; non-homomorphic readouts were not examined.
- B3's bound comparison is [NUM] (50 digits). The mutual informations are exact symbolic expressions.
- The C3 LP is restricted to four ontic states. The 3/4 ceiling for general PNC models is the cited theorem [L].
- C4 and C5 check parity obliviousness over their stated accessible sets (18 axes; sequences of length ≤ 3, adaptive
  ones following from these) and not over a closure of those sets.
- §2.4 (bijectivity does not supply N1) rests on one instance (C2) and a written argument.
- PBR and the ψ-epistemic bounds were not computed. The PI analysis is [W].
- Literature in §8 is from memory. The capacity direction in §3 rests on unread literature and complexity conjectures.
- [rec] rows (Main, Methodology, book appendix-c, SM, MC1–MC5) were taken as recorded. No independent review has been
  run on this node.

***

## 10. Files (`probe/`)

| file | role |
|---|---|
| `p6.py` | blocks A (observable ladder), B (Bell under OI readout), C and C5 (preparation contextuality), K (Peres–Mermin), D (double stochasticity replay); 19 checks |
| `p6.run1.out`, `p6.run2.out` | 19 PASS, 0 FAIL; byte-identical |
| `SHA256SUMS` | `p6.py` `069a77fd…2c10`; both outputs `bbfff6b9…2c7b` |

Run: `python3 -I -B p6.py` (with SymPy) from `probe/` (about one minute).

***

## 11. Productivity verdict

**Gem: yes, narrow.** Facts strictly stronger than "A2 needs M and R":
- *Hidden assumption.* M and R bind at R2 only. At R1 the corpus already proves Reproduction, and the open question is
  selection (HA-6.1).
- *Necessary features of the incompleteness:*
  - N1: preparation contextuality through invisible response-relevant memory, which C4, knowledge balance and
    bijectivity do not supply (C1–C3, §2.4);
  - N2: nonaffinity beyond remote dependence (B1a);
  - N3: a magnitude-fixing principle. Every mechanism found spans classical to maximal with a free weight, in both
    the Bell and the POM setting (B2b, C5).

**Classification: ELABORATING overall, with one BORDERLINE item (HA-6.2) and a CONFIRMING core (Bell).** No item is
claimed NEW:
- R1 Reproduction and the selection problem are in Main:576–578 and appendix-c:230;
- the Bell analysis is Main §3.3 and Methodology:393;
- the PNC ceiling is Spekkens et al. [L];
- over-generation by restriction is standard in GPT literature [L];
- the nonaffinity remark is narrow.

**Answer to the node question.** Observational incompleteness, in the κ1–κ4 class, can make a non-quantum reality's
records agree with QM to any accessible precision, but so far only as Reproduction (corpus). Whether it can do so as
Emergence is undetermined. The deeper reality would need N1–N4: hidden, response-relevant preparation memory that is
never read back; a nonaffine relaxation of parameter or measurement independence for composites; capacity unbounded in
the precision; and a principle fixing the size of the nonclassicality at the quantum values. The incompleteness
mechanism must supply N1 and N3, which no mechanism examined does.

***

## 12. Proposed PLAN text

**Status bullet (after `mc-node5/`):**

> - **`mc-node6/`, A2 track node 1, the quantum appearance in an observer's records: ELABORATING, one BORDERLINE item,
>   [W/EC].**
>   - Three rungs: R0, per-menu representability (universal, PR included); R1, record statistics under one realization
>     with fixed labelled instruments and composites; R2, availability under G3 on visible carriers (`DenseFiniteQM`).
>     The cone lemma and clauses M and R are R2 statements. A κ1–κ4 toy-bit construction keeps every visible map in the
>     cone and reproduces the qubit's sequential Pauli records exactly. At R1 the corpus already proves Reproduction
>     (Main's uniform continuum realization, Main:576–578) and names the open question as selection.
>   - Outcomes: Reproduction at R1 (corpus). Failure for the finite-range, measurement-independent completion (Bell)
>     and for every preparation-noncontextual incompleteness (parity-oblivious multiplexing ≤ 3/4 against QM's
>     (1+1/√2)/2). No Emergence of quantum statistics found. The emergent features found (double stochasticity,
>     operational no-signalling, C4 memory) are classical-compatible.
>   - Necessary for Emergence at R1 (not jointly sufficient):
>     - N1: preparation contextuality through response-relevant memory that is never read back; C4 does not imply it,
>       nor do knowledge balance or bijectivity;
>     - N2: for Bell, a relaxed parameter or measurement independence, with nonaffine structure (affine remote
>       dependence stays at 2);
>     - N3: a principle fixing the magnitude. One long edge gives S = 2 + 2w, and destructive complementary readouts
>       give POM success (1+w)/2, with w free; restriction overshoots QM as well as falls short;
>     - N4: capacity unbounded in the precision.
>   - G6: none under the preregistered rule.

**Replacement for PLAN:205–212 (A2 track paragraph), proposed:**

> A separate track, alongside the A1 benchmark. Question: can observational limitations make a deeper, non-quantum
> reality's record statistics agree with QM to arbitrary accessible precision, without QM at the fundamental level?
> Results are classed as Emergence, Reproduction or Failure. At the level of availability under G3 (R2, `DenseFiniteQM`),
> U and O are not needed and M and R are, and the cone lemma (`mc-node3`) keeps the present construction's available
> maps in the monomial cone. At the level of record statistics (R1), M and R are not obstructions: κ1–κ4 constructions
> reproduce them, and the corpus proves Reproduction at fixed dimension, outcome bound and horizon (Main:576–578). The
> track's question at R1 is Emergence, the corpus's selection problem, under the necessary features N1–N4 of
> `mc-node6`. It inherits this thread's method, its controls and G6. Negative results are acceptable outcomes and are
> scoped to the construction examined.

**Next node for the A2 track (proposed): a magnitude-selection test of OI's own principles.**
- *Question.* Does any selection principle already stated in OI's own terms, applied to the κ1–κ4 class, bound the free
  weights of `mc-node6`'s two benchmark families at the quantum values? The families are the long edge (S = 2 + 2w) and
  destructive complementary readouts (POM (1+w)/2). Candidates, stated without Hilbert-space structure:
  - Lemma 3's maximal-entropy selection of hidden priors conditioned on the observer's records;
  - partition covariance of reduced descriptions (Main's Wigner's-friend treatment, observer identity as partition
    gauge);
  - finite-range locality with preparation-indexed edges (H-Bell);
  - capacity balance (C3).
- *Decision rule, preregistered.* A principle passes iff, fixed before any computation, it:
  - excludes the PR value (S = 4) and the gbit value (POM = 1);
  - permits values within ε of 2√2 and (1+1/√2)/2;
  - keeps every classical model.

  It fails if it permits w = 1 in either family or forbids the quantum value.
- *Controls.* PR and gbit must be excluded (must-fail). The classical delay line and the toy bit must be kept
  (must-hold). One family where the principle is vacuous must be shown (countercontrol).
- *Productivity test.* Gem iff a principle passes or fails for an identified structural reason that propagates to
  N1–N3.

***

## Review outcome

Not yet reviewed. To be applied in place after an independent skeptical review, per PLAN's method.
