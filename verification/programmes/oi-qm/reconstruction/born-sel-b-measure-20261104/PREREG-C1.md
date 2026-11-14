# BORN-SEL C-1 preregistration: single-orbit frequencies against the Born-form weights on small wave substrata (#1059, part (b))

**Status.** WIP / UNVERIFIED preregistration, draft r9.
- r6 (`cde5ecbc`) was accepted as a draft after the independent review of `3be25e7f` and the delta reviews of
  `c610b2b8`, `1962c378`, `2f59aad7` and `df723247` (#1082 c.6625738542).
- r7 (`5ea9e4ca`) wrote in the owner's rulings on OQ-1 to OQ-15 (#1059 c.6650820790; quoted in §8.2) and the
  expected-value and schema amendments they require. Its independent review (#1082 c.6651181144, model-authored) is
  ACCEPT WITH CHANGES (minor). It recomputed exactly every expected value r7 added, CC-ORDER's included, and every
  expected field of the eleven r6 toys, and found them correct.
- r8 (`500b3177`) applied that review's changes C1–C10. None changes a verdict rule or an expected value. Its
  recheck (#1082 c.6651778560, model-authored) is ACCEPT WITH CHANGES (minor).
- r9 (`2217142c`) applies the recheck's changes that bear on this file (R2, R7). Neither changes a verdict rule or an expected
  value. The independent r9 delta check (#1082 c.6651925573, model-authored) is ACCEPT; it is not a fresh full C-1 expected-answer review.
- Paper only. Nothing has been run or written as code, and no native instance has been enumerated.

**Not a candidate freeze yet.** The freeze sequence is in §7. The independent r9 delta check is ACCEPT (#1082 c.6651925573).
Before `F`, verify the OQ-14 API-field semantics against a real job record and put CC-ORDER's gating interpretation to the owner;
designation of `F` confirms that interpretation, while a contrary ruling must first be incorporated and reviewed (§3.1, §4.3, §7).
**Unfrozen and not authorized to run.** A run still needs the owner's `F` designation and go, the tool, its review and separate dispatch approval (§7).

- **Frozen inputs at `F`.** All four are in `verification/programmes/oi-qm/reconstruction/born-sel-b-measure-20261104/`,
  beside the assessment (§A.36):
  - this file, `PREREG-C1.md`;
  - `C1-INSTANCES.json`, which holds the instance list, the order, the encodings, the explicit toy maps, the unit-control
    inputs, the wave rule's parameters and the recorded OQ-13 answer;
  - `C1-CONTROLS-EXPECTED.json`, the hand-derived expected values of every control and mutation;
  - `C1-OUTPUT-SCHEMA.json`, the machine-readable schema of every output file and of the expected file.
- **Source.** `BORNSEL-B-MEASURE.md` r3, accepted at `7b46d36c` (review #1082 c.6622587957: ACCEPT). Its §7 C-1 sketch
  (lines 404–416 of that file) is the specification frozen here. Base for every corpus citation: `origin/main`
  `1609dc440f5a12d05b750f6d894bb91d09a099a3`.
- **Authorization.** Owner, chat 2026-11-04, #1059 c.6624262539: draft, but do not run, a frozen preregistration for
  C-1. The run is a separate later decision.
- **Owner decisions consumed.** QB-1 and QB-2 (§2.6), and the rulings on OQ-1 to OQ-15 (§8.2; #1059 c.6650820790,
  amaybaum, 2026-11-05).

**Support labels.**
- **[P]** a quotation of, or citation to, a source at the base. This covers a manuscript line (`Main:N`, `SM:N`,
  `Substratum:N`), a Lean declaration with file:line, or a line of the assessment (`BSB:N`, the line in
  `BORNSEL-B-MEASURE.md` at `7b46d36c`). The assessment labels its own derivations [D]; they are cited here as accepted
  at `7b46d36c`, not as kernel-checked.
- **[D]** a derivation or a specification choice made in this file. Unreviewed.
- **[O]** an owner decision.

**Notation.**
- The Lean wave rule's coupling coefficient is named `α` (`SubstratumInterfaceAudit.lean:160`), and the assessment's
  measure branch is also α. In this file the **coupling coefficient is written `a`**, and α always means the measure
  branch "uniform on the actual orbit" [D].
- `F` and `E` keep their §A.39 meanings: the frozen commit, and the certified execution head. The set of evaluated
  native instances is written `Ev` (§4.2).
- The four verdict variants are R0, S1, S2 and S3 (§4.1). R0 is the sketch's rule (BSB:406–410). The OQ-13 answer
  `13b` selects **S1** (§4.2); R0, S2 and S3 are diagnostic comparisons, computed and recorded, that do not qualify
  the C-1 verdict.
- Every native instance is evaluated under two **readouts**, `pc` and `cur` (§2.1; OQ-2). Its verdicts are per
  readout, and there is no combined verdict across readouts.
- The native labels N1–N12 are identifiers, not ordinals. N12 (W-q2-L7-r2) runs between N8 and N9 (§2.2).

***

## 1. Objective and non-objectives

**Objective.** By exhaustive exact enumeration over ℚ, on small instances of the manuscripts' wave substratum, decide
for each instance and readout whether "β's one-step numbers are single-orbit frequencies" (BSB:406). The owner states
the objective as: "test whether the numerical probabilities carried by OI's representation agree with frequencies of
the underlying dynamics, without assuming that agreement" (#1059 c.6650820790).
- **The two objects, kept distinct.** `T^β` is the representation's declared law: the one-step matrix of the
  Born-form theorem with the declared uniform hidden input (Main:282–290). `T^{α,O}` is a frequency of the dynamics:
  the cycle-horizon transition frequency on an orbit `O` taken as actual (Lemma A, BSB:239–241). Their agreement is
  the proposition under test, not a premise.
- **The selected comparison (OQ-13 = `13b`, variant S1).** For every candidate orbit `O ∈ Long′` (long, and with
  `T^{α,O}` not a permutation matrix), does `T^{α,O}` equal the global-prior `T^β` on every visible row `O` visits?
- **Diagnostics.** The other three combinations of candidates and prior support are frozen variants R0, S2 and S3
  (§4.1). They are computed and recorded, and do not qualify the C-1 verdict.

On the same instances, the run also records per orbit whether the α-rooted family is P-divisible on `{0, …, |O|}`
(BSB:411, B4).

**What the question is, in the owner's terms [D].**
- **Credence side (QB-2).** Under QB-2, the embedded observer's assignment given the present visible value `x₀ = a` is
  an invariant maximal-entropy prior conditioned on that record. With the prior over all of `S`, this is
  `unif({a} × 𝒞_H)` (BSB:206–208, γ-c with a present-visible record). Its one-step numbers are `T^β` (Main:117,
  Main:288–290). With the prior restricted to a union `U` of orbits, it is `unif(U ∩ ({a} × 𝒞_H))`.
- **Frequency side (QB-1).** Under QB-1 the physical target is operational frequencies. By BSB:239–241 (Lemma A), the
  transition frequencies along the actual trajectory over a whole cycle of the actual orbit `O*` are `T^{α,O*}`.
- **The comparison.** C-1 asks, on native instances, whether these two coincide for every orbit admitted as a candidate
  `O*`. Agreement at the cycle horizon says nothing about agreement over accessible windows, which C-1 does not
  test.

**Non-objectives.** The run does not cover:
- accessible-window frequencies (C-3, deferred until after QB-1; BSB:424);
- any Lean work (C-2);
- `d ≥ 2`, `d = 3`, the rounded (nonlinear) rule, or a coupling other than `a = 1`;
- record-constrained measures beyond the present-visible record;
- any selection of a measure, a new premise, a manuscript edit, a status change, merge or publication.

**What a completed run establishes.** For each evaluated native instance and each readout, at the frozen sizes and
conventions, it records four verdicts: R0, S1, S2 and S3. Each verdict is one of:
- FREQ: every candidate orbit matches, and at least one comparison is not automatic;
- FREQ_VACUOUS: every candidate matches, but only by construction, because `shared_rows = 0` (§4.1);
- NOT: some candidate does not match;
- VOID_NO_ORBIT: there is no candidate.

It also records the per-orbit P-divisibility. The reported C-1 verdicts are the selected variant S1's overall verdicts,
one per readout (§4.2). This is a result on the consistency axis (§A.23): it compares objects the framework itself
defines and confronts no external measurement.

**What it does not establish.** See §9. In particular, it does not select a measure, does not bear on accessible
windows (agreement there is untested), and does not extend beyond the frozen instances and readouts.

***

## 2. Frozen preconditions

### 2.0 Conventions common to every instance

- **Arithmetic.** All counts are exact integers. A probability is a pair of integers reduced to lowest terms. Equality
  of two probabilities `x/y` and `u/v` is decided by `x·v = u·y` on integers. No floating-point value enters the
  computation, the comparison or the verdict path. One appearing in an output probability field is a schema violation
  (exit 2) [D].
- **Configurations.** Every toy or native instance is a finite set `S = 𝒞_V × 𝒞_H`, with `n = |𝒞_V|` and
  `m = |𝒞_H|`. A state is an integer `s ∈ {0, …, nm − 1}` [D].
  - On a toy, the visible value is `π_V(s) = s mod n` and the hidden value is `s div n`, so `s = v + n·h`.
  - On a native instance, `s` is the state index of §2.1 under both readouts. The visible value is the readout's
    `π_V(s)` (§2.1), and every count over the hidden factor is a count over the states with that visible value. Each
    readout is a product split of the same `S`, so the definitions of §2.3–§2.7 apply to it unchanged.
- **Map.** `φ` is given as an array `φ[s]` over all of `S`: by an explicit table for toy instances
  (`C1-INSTANCES.json`), and by the wave rule of §2.1 for native instances.
- **Enumeration method.** Full: every state of `S`, for every instance. No sampling, no sequential method.
- **Budget check.** Before any enumeration, the tool checks `state_count = n·m ≤ 2¹⁶` from the frozen parameters, and
  exits 7 otherwise.
- **Bijectivity check.** For every toy and native instance, the tool first checks that `φ` is injective on `S`. A failure
  exits 5 before any other field of that instance is computed. For mutation M-INJ, which is expected to be
  non-injective, the detection is the compared field (§3.3).
- **Orbits.** The orbits are the cycles of `φ`. An orbit's representative `rep(O)` is its least state index, and orbits
  are listed in increasing `rep`.
  - **Closure check (OQ-7).** On every toy and native instance, each recorded orbit must be a list of distinct states
    with `φ(s_k) = s_{k+1}` and `φ(s_last) = s_0`, and the recorded orbits must partition `S`. Together these make the
    recorded orbits exactly the cycle decomposition [D]. A failure exits 4. Mutation M-FRAG (§3.3) exercises the check
    as a compared field.
  - The orbits do not depend on the readout. `|O|` is the cycle length, and `ord(φ)` is the least common multiple of
    the cycle lengths.
- **Permutation-matrix test [D].** A matrix `M`, with rows indexed by `W` and columns by `𝒞_V`, is a **permutation
  matrix on `W`** iff all three of the following hold:
  - every entry `M(a, j)` with `a, j ∈ W` is `0` or `1`;
  - every row sum over `j ∈ W` is `1`, and every column sum over `a ∈ W` is `1`;
  - `M(a, j) = 0` for every `a ∈ W` and `j ∉ W`.

  For `T^β`, `W = 𝒞_V`. For `T^{α,O}`, `W = V_O` (§2.3).

### 2.1 The native wave substratum [P, with file:line]

- **Structure.** A substratum is a site type `ι` with translations, an additive alphabet `V`, and a second-order rule
  `R` (`SubstratumInterfaceAudit.lean:60`). Its configuration space is the phase-space form `ι → V × V`
  (`SubstratumInterfaceAudit.lean:78`). Its dynamics is `φ := leapEquiv R.F` (`SubstratumInterfaceAudit.lean:81`).
- **The step.**
  - `leapEquiv F x = leap F x` (`SecondOrderCircuit.lean:117–118`).
  - `leap F x i = ((x i).2, F (curOf x) i − (x i).1)` (`SecondOrderCircuit.lean:67–68`), with `prevOf x i = (x i).1`
    and `curOf x i = (x i).2` (`SecondOrderCircuit.lean:48, 51`).
  - So the per-site pair is `(prev, cur)`, and the step is `(p, c) ↦ (c, F(c) − p)`. This is the manuscripts'
    second-order form `x_i(t+1) = f(neighbours of i at t) − x_i(t−1) mod q` (SM:106, SM:228).
- **The rule.**
  - `waveF α c i = α * ∑_{p : Fin d × Bool} c (i + dir p)` (`SubstratumInterfaceAudit.lean:160–161`), with
    `dir (k, true) = +e_k` and `dir (k, false) = −e_k` (`SubstratumInterfaceAudit.lean:142–143`).
  - The manuscript form is `f = α(x₁ + ⋯ + x_{2d}) mod q` (SM:228).
  - SM Appendix A writes the `d = 1` ring with coefficient 1:
    `x(n, t+1) = x(n−1, t) + x(n+1, t) − x(n, t−1) (mod q)` (SM:1602).
- **The lattice and the boundary.** Sites are `Fin d → ZMod L`, the periodic torus, and the alphabet is `ZMod q`
  (`SubstratumInterfaceAudit.lean:177–180`, with the docstring at :175–176: "the manuscripts' rule on a finite cubic
  torus with alphabet ℤ/qℤ"). Boundary conditions are therefore periodic.
- **Kernel facts used as controls.**
  - `φ` is a bijection (`waveSubstratum_A2`, `SubstratumInterfaceAudit.lean:190`).
  - The rule commutes with translations (`waveSubstratum_A4Exact`, :202).
  - The rule is additive (`waveSubstratum_A5`, :211).
  - `φ` fixes the zero configuration (`waveSubstratum_phi_fixes_zero`, `StochasticInterface.lean:101`).
  - The wave substratum is not transitive (`waveSubstratum_stochastic_interface_gap`, `StochasticInterface.lean:191`).
- **The frozen instance of the rule [D, from the above].** Take `d = 1`, `a = 1`, a ring of `L` sites, and
  `q ∈ {2, 3}`. At site `i`, with indices mod `L`:
  - `p′_i = c_i`;
  - `c′_i = (c_{i−1} + c_{i+1} − p_i) mod q`.

  The Lean sum ranges over `p : Fin 1 × Bool`, so both terms are always present. `L ≥ 3` is required so that
  `i − 1 ≠ i + 1`, making the two neighbours distinct sites. At `L = 2` the sum is `2c_{i+1}`. At `L = 1` it is a
  self-coupling, which center independence excludes (SM:228) [D].
- **How the `d = 1` instance relates to the manuscript instance.**
  - The kernel names the manuscript instance as "`α = 1`, `d = 3`" (`PhysicalC4Discharge.lean:570–571`). C-1 does not
    run that instance [D].
  - The kernel's `waveSubstratum d L q α` is one definition, uniform in `d`. The `d = 1` instances are members of the
    same family with the same coefficient `a = 1`, and the kernel facts above hold for every `d`.
  - The manuscript instance is out of budget. At `d = 3` the neighbours along an axis are distinct only for `L ≥ 3`,
    which gives `|S| = q^{2·27} ≥ 2^{54}`. At `L = 2` they coincide, and at `q = 2` the rule degenerates to `c′ = −p`
    [D].
  - **The coefficient.**
    - SM:222–224 states that the form conditions fix the form of the rule "not the observer-level normalization of
      α", and that a real wave operator "is an observer-level lift whose derivation must be stated separately".
    - SM:230 shows that `α = 1/d` is the coefficient that makes the real harmonic lift gapless.
    - At `d = 1`, SM:1602 writes the ring with coefficient 1, and `1/d = 1`. So at `d = 1` the substratum coefficient
      and that observer-level normalisation coincide.
    - At `d = 3` they do not (`1` against `1/3`). The `d = 1` instances therefore do not stand in for the `d = 3`
      instance's coefficient reading [D].
- **The visible/hidden split [P].**
  - The kernel's cut realization takes "the visible carrier [as] the region's phase-space data, the hidden carrier the
    complement's, and the step is `𝒮.φ` transported along the split" (`PhysicalC4Discharge.lean:578–581`; def
    `cutRealization` at :582).
  - The region `Vs` is a parameter, and "[SM] Theorem 22 quantifies over connected regions with `|V| ≤ N/3`"
    (`PhysicalC4Discharge.lean:561`; SM:1376).
- **The frozen region [D].**
  - `R = {0, 1, …, r−1}`, a contiguous block of `r` sites, with `r ≤ L/3`.
  - Because the rule commutes with translations (A4Exact), every contiguous block of `r` sites gives the same instance
    up to relabelling. The block at the origin is chosen.
- **The two readouts (OQ-2 = C) [P, with readings D].** Every native instance is evaluated under both.
  - **`pc`: the `(prev, cur)` pairs on `R`.** This is the kernel's `cutRealization`
    (`PhysicalC4Discharge.lean:578–590`): the visible configuration is the pair at each site of `R`, so `n = q^{2r}`;
    the hidden configuration is the pair at each site outside `R`, so `m = q^{2(L−r)}`. The kernel definition encodes
    this choice; it does not exclude another split.
  - **`cur`: the current values on `R`.** This is Main:222's configuration-sector readout: "The transition
    probabilities `T_ij` are projections of the full phase-space flow onto the configuration sector of `Γ_V`, with
    momenta and hidden-sector degrees of freedom absorbed into the Liouville marginalization". Read on the
    second-order rule, the configuration is `cur` and `prev` is absorbed into the hidden side [D]. So `n = q^r` and
    `m = q^{2L−r}`.
  - Main:288's theorem holds for every product split, so it does not choose between the readouts. Which one is native
    is the open planning item O-ACC (#914). Every C-1 verdict is stated for its readout only.
- **The state encoding [D].**
  - Site digit `δ_i = p_i·q + c_i ∈ {0, …, q²−1}`; state index `s = Σ_i δ_i·(q²)^i`. The index is the same under both
    readouts.
  - `pc`: `π_V(s) = s mod q^{2r}`, and the hidden value is `s div q^{2r}`, consistent with §2.0's `s = v + n·h`.
  - `cur`: `π_V(s) = Σ_{i<r} (δ_i mod q)·q^i`, where `δ_i = (s div q^{2i}) mod q²`; that is, the current values on `R`
    read as base-`q` digits.
- **Two implementations [D].** The tool computes `φ` twice:
  - (i) by the site loop above;
  - (ii) as the linear map `F = [[0, I], [−I, A]]` on `(p, c) ∈ (ℤ/q)^{2L}`, with `A` the circulant ring adjacency
    (SM:1602), applied to the digit vector.

  The two arrays must be identical on all of `S`, and the tool exits 4 otherwise.

### 2.2 Native instances and sizes [D]

Native instances run in this order: increasing `|S|`, with ties broken by `q` and then by `r`. `|S| = q^{2L}`. There
are twelve (OQ-4 = B). The labels are identifiers, not ordinals: N12 runs between N8 and N9.

| Run order | Label | id | q | L | r | `pc`: `n = q^{2r}`, `m`, `ℓ_min` | `cur`: `n = q^r`, `m`, `ℓ_min` | `|S|` | `gcd(L, q)` |
|---|---|---|---|---|---|---|---|---|---|
| 1 | N1 | W-q2-L3-r1 | 2 | 3 | 1 | 4, 16, 5 | 2, 32, 3 | 64 | 1 |
| 2 | N2 | W-q2-L4-r1 | 2 | 4 | 1 | 4, 64, 5 | 2, 128, 3 | 256 | 2 |
| 3 | N3 | W-q3-L3-r1 | 3 | 3 | 1 | 9, 81, 10 | 3, 243, 4 | 729 | 3 |
| 4 | N4 | W-q2-L5-r1 | 2 | 5 | 1 | 4, 256, 5 | 2, 512, 3 | 1,024 | 1 |
| 5 | N5 | W-q2-L6-r1 | 2 | 6 | 1 | 4, 1,024, 5 | 2, 2,048, 3 | 4,096 | 2 |
| 6 | N6 | W-q2-L6-r2 | 2 | 6 | 2 | 16, 256, 17 | 4, 1,024, 5 | 4,096 | 2 |
| 7 | N7 | W-q3-L4-r1 | 3 | 4 | 1 | 9, 729, 10 | 3, 2,187, 4 | 6,561 | 1 |
| 8 | N8 | W-q2-L7-r1 | 2 | 7 | 1 | 4, 4,096, 5 | 2, 8,192, 3 | 16,384 | 1 |
| 9 | N12 | W-q2-L7-r2 | 2 | 7 | 2 | 16, 1,024, 17 | 4, 4,096, 5 | 16,384 | 1 |
| 10 | N9 | W-q3-L5-r1 | 3 | 5 | 1 | 9, 6,561, 10 | 3, 19,683, 4 | 59,049 | 1 |
| 11 | N10 | W-q2-L8-r1 | 2 | 8 | 1 | 4, 16,384, 5 | 2, 32,768, 3 | 65,536 | 2 |
| 12 | N11 | W-q2-L8-r2 | 2 | 8 | 2 | 16, 4,096, 17 | 4, 16,384, 5 | 65,536 | 2 |

- **Budget.** Every instance has `|S| ≤ 2¹⁶`. `q = 2` reaches `2¹⁶` at `L = 8`. `q = 3` stays below it through `L = 5`
  (`3^{10} = 59,049`), so `L = 6` (`3^{12} = 531,441`) is excluded.
- **Region sizes.** `r ≤ L/3` gives `r = 1` for `L ≤ 5` and `r ∈ {1, 2}` for `L ∈ {6, 7, 8}`.
- **Twin classes (§2.7).** These are intrinsic: orbits with the same primitive cyclic visible word, computed per
  readout. The frozen cross-check generators are `⟨σ⟩` (reflection about site 0) for the nine `r = 1` instances (N1–N5
  and N7–N10) and the trivial group for the three `r = 2` instances (N6, N11 and N12).
- **W-q2-L7-r2 (N12) is included (OQ-4 = B), and counts in each readout's aggregation, on every variant where it is
  non-void (§4.2 unchanged).**
  - Under `pc` it is expected to be void, by the statement of SM Theorem A.1 only (SM:1604–1606: "For q prime with
    gcd(L, q) = 1 — q = 2 included: ord(F mod q) = qL"): every orbit length would divide `qL = 14 < 17 = ℓ_min`.
  - Under `cur`, `ℓ_min = 5`, and the same statement gives an orbit of length 7 or 14, so `Long ≠ ∅` there. `Long′ ≠ ∅`
    is not shown.
  - Both readings use the theorem's statement only; no orbit of any instance was computed [D]. The rule does not
    depend on them.
- **Coprime and non-coprime.** N1, N4, N7, N8, N9 and N12 satisfy `gcd(L, q) = 1`, inside Theorem A.1's scope. The
  others have `q | L`, where the parabolic Jordan blocks of SM Appendix A are present. Both kinds are included.
- **Theorem 22's hypotheses [P, SM:1376]** are "connected bounded-degree coupling graph with diameter D ≥ 4 … any
  connected subgraph V with |V| ≤ N/3".
  - Every frozen `R` is connected and has `|R| ≤ N/3`. These are checked from the frozen parameters, and the tool exits
    2 if they are violated.
  - The ring's diameter `⌊L/2⌋` is at least 4 only at `L = 8` (N10, N11). It is recorded per instance as
    `diameter_ge_4`, a secondary diagnostic only (OQ-4): it gates nothing and selects no instance for counting.
  - C-1 asserts nothing about (C1) on these instances. Theorem 22's own proof step for (C1) uses only `∂V ≠ ∅`
    (SM:1378); that is SM's statement, not a C-1 result.
  - `beta_is_permutation = false` is only a sufficient witness of (C1) (Main:74). It is recorded, and it is not a
    checkpoint for (C1).

### 2.3 The compared objects [D, from the cited definitions]

For an instance with map `φ` on `S = 𝒞_V × 𝒞_H`:

- **Counts.** `c(a, j) := #{h ∈ 𝒞_H : π_V φ(a, h) = j}`. For an orbit `O`:
  - `c_O(a, j) := #{h : (a, h) ∈ O, π_V φ(a, h) = j}`;
  - `n_a(O) := #{h : (a, h) ∈ O}`.
- **`T^β`, the Born-form matrix.** `T^β(a, j) := c(a, j)/m` for every `a, j ∈ 𝒞_V`. This is Main:117's `T_ij`, the
  matrix of the Born-form theorem (Main:288–290), and `Γ^κ_1` with `κ_a` uniform on `𝒞_H` (BSB:126).
- **Rows an orbit visits.** `V_O := {a ∈ 𝒞_V : n_a(O) > 0}`. The rows in `𝒞_V ∖ V_O` are the orbit's **unvisited
  rows**. They are recorded and excluded from that orbit's comparison (BSB:407–408).
- **`T^{α,O}`, the single-orbit frequencies.** For `a ∈ V_O` and every `j ∈ 𝒞_V`:
  `T^{α,O}(a, j) := c_O(a, j)/n_a(O)`.
  - This is `Γ^κ_1` with `κ_a` uniform on `{h : (a, h) ∈ O}`, which is α conditioned on the root `a` (BSB:134–136).
  - By BSB:240–241 (Lemma A), take any `s* ∈ O` and any positive multiple `N` of `|O|`. Along
    `s*, φ(s*), …, φ^{N−1}(s*)`, the empirical frequency of the transition `a → j` among visits to `a` is exactly
    `T^{α,O}(a, j)`.
  - Since `φ` maps `O` into `O`, `T^{α,O}(a, j) = 0` for `j ∉ V_O`. The comparison still runs over every column `j`.
- **Long orbits.** `long(O)` iff `|O| ≥ ℓ_min` (§2.5). `Long := {O : long(O)}`.
- **The orbit-level C4 predicate.** `long_c4(O)` iff `long(O)` holds and `T^{α,O}` is not a permutation matrix on `V_O`.
  `Long′ := {O : long_c4(O)}`.
  - By Lemma PD (§2.4), `long_c4(O)` is `long(O) ∧ ¬pdiv_alpha(O)`.
  - A long orbit with a permutation `T^{α,O}` has a deterministic visible process on the orbit, with no readback gap
    below `|O|`. This follows from Main:74 and Main:141, transported to the root-dependent κ by BSB:147–154 [D].
- **Restricted credences.** For a set `X` of orbits, let `U_X := ⋃_{O ∈ X} O` and `W_X := ⋃_{O ∈ X} V_O`. For
  `a ∈ W_X` and every `j`:
  `T^{β|X}(a, j) := Σ_{O ∈ X} c_O(a, j) / Σ_{O ∈ X} n_a(O)`.
  - These are the one-step numbers of `unif(U_X)` conditioned on `x₀ = a`. This is the same construction as γ-c
    (BSB:206–208), with the prior's support restricted to `U_X` [D].
  - It is the empty map when `X = ∅`.
  - Two are used: `T^{β_long} := T^{β|Long}` and `T^{β_c4} := T^{β|Long′}`.
- **Orbit equality.**
  - `eq(O)` holds iff `T^{α,O}(a, j) = T^β(a, j)` for every `a ∈ V_O` and every `j ∈ 𝒞_V`, that is, iff
    `c_O(a, j)·m = c(a, j)·n_a(O)` for all such `(a, j)`.
  - `eq_beta_long(O)` is defined for `O ∈ Long`, and `eq_beta_c4(O)` for `O ∈ Long′`. Each is the same comparison with
    `T^{β_long}`, respectively `T^{β_c4}`, in place of `T^β`. Each is `null` outside its set.
  - A failed comparison's **first mismatch** is the lexicographically least `(a, j)` with inequality (`a`-major),
    reported with both values.
- **Mixture identity (an internal check, not a hypothesis) [D].**
  - Because the orbits partition `S`, `Σ_O c_O(a, j) = c(a, j)` and `Σ_O n_a(O) = m` for every `a, j`.
  - Hence `T^β(a, ·) = Σ_{O ∋ a} (n_a(O)/m)·T^{α,O}(a, ·)`.
  - The tool computes `c` directly over the `(a, h)` grid and separately as the orbit sum. The two must agree exactly,
    and the tool exits 4 otherwise.
- **Double stochasticity [P, Main:62].** "the marginal of a bijection under the uniform prior is doubly stochastic,
  since each set `{x_j} × 𝒞_H` has exactly `|𝒞_H|` preimages". So `Σ_j c(a, j) = m` and `Σ_a c(a, j) = m`. This is
  checked, and a failure exits 4.

### 2.4 P-divisibility (B4)

- **The kernel definitions [P].**
  - `PDivisible K Γ := ∀ s t, s < t → t ≤ K → ∃ Λ, IsRowStochastic Λ ∧ Γ t = Γ s * Λ` (`CausalReadback.lean:54`).
  - `IsRowStochastic` is at `CausalReadback.lean:48`.
  - The rooted maps with a shared prior are `rootedMap R t a j = Σ_h [π_V(step^t(a, h)) = j]·prior h`
    (`CausalReadback.lean:190`).
- **The α-rooted family on an orbit [D].** For `t ≥ 0` and `a, j ∈ V_O`:
  `Γ^{α,O}_t(a, j) := #{h : (a, h) ∈ O, π_V φ^t(a, h) = j} / n_a(O)`.
  - It is square on `V_O` and row-stochastic.
  - `Γ^{α,O}_0 = I`, and `Γ^{α,O}_1` is `T^{α,O}` restricted to `V_O`.
  - `Γ^{α,O}_{|O|} = I`, because `φ^{|O|}` is the identity on `O`.
  - Its rows are indexed by `V_O` only, because α gives no hidden conditional on an unvisited root. BSB:147 lets `κ_a`
    be arbitrary there for the implication (any probability law, as corrected in BSB r4:149), which would make a
    full-`𝒞_V` record depend on an arbitrary choice.
  - The restriction to `V_O` is the OQ-5 answer (A).
- **The recorded quantity.** `pdiv_alpha(O) := PDivisible |O| Γ^{α,O}`, on `V_O`, with horizon `{0, …, |O|}` (BSB:411).
- **The β family [D].**
  - `Γ^β_t(a, j) := #{h : π_V φ^t(a, h) = j}/m` on `𝒞_V`. Under the `pc` readout this is the kernel's `rootedMap` for
    the cut realization with the uniform prior. Under `cur` it is the same construction on the `cur` split, which is
    not the kernel's `cutRealization` [D].
  - `pdiv_beta := PDivisible ord(φ) Γ^β`, with horizon `{0, …, ord(φ)}`, where `Γ^β_{ord(φ)} = I`.
  - It is required on CE-8. It is recorded on native instances (OQ-6 = A). By Lemma PD it is a function of
    `beta_is_permutation`, so it is not an independent scientific result.
- **Lemma PD [D].** Let `Γ_t` be either family above, on its row set `W` (`V_O` or `𝒞_V`), with return time `N`
  (`|O|` or `ord(φ)`), so that `Γ_N = I`. Then `PDivisible N Γ` holds iff `Γ_1` is a permutation matrix on `W`.
  - **(PDivisible ⇒ Γ₁ permutation), by contraposition.** Suppose `Γ_1` is not a permutation matrix.
    - Then `N ≥ 2`, since `Γ_1 = I` when `N = 1`.
    - A row-stochastic `Λ` with `Γ_N = Γ_1 Λ = I` would be a stochastic right inverse of `Γ_1`. Main:133 forbids this:
      "If a finite square stochastic matrix has a stochastic left or right inverse, then it is a permutation matrix"
      (kernel `isPermMatrix_of_stochastic_inverse`, `EquivalenceChain.lean:110`). So the pair `(1, N)` fails.
    - For β, the general statement of this direction is a kernel-checked theorem: `pIndivisible_of_return_nonperm`
      (`RootedRecurrenceBridge.lean:93`). For a `RootedRealization` whose step returns to the identity at `n` and whose
      `rootedMap` at `s < n` is not a permutation, it concludes `PIndivisibleWithin n (rootedMap R)`.
    - The theorem is kernel-checked. **Its application to these instances is not.** The application takes `s = 1`,
      `n = ord(φ)`, `R` the cut realization with the uniform prior, and `hreturn` the identity `φ^{ord(φ)} = id` on
      `S`. That instantiation is [D], and no Lean term for it is built in C-1.
    - For α, the family has a root-dependent κ and is not a kernel `rootedMap`. That case rests on the matrix lemma
      plus this paragraph [D].
  - **(Γ₁ permutation ⇒ PDivisible).** Suppose `Γ_1` is a permutation matrix `P_f`, with `f` a bijection of `W`.
    - For α, every `(a, h) ∈ O` has `π_V φ(a, h) = f(a)`. So along the cycle `x_{k+1} = f(x_k)`, hence
      `π_V φ^t(a, h) = f^t(a)` and `Γ_t = P_{f^t}`.
    - For β, `π_V φ(b, h′) = f(b)` for every `b, h′`. By induction on `t`, `π_V φ^t(a, h) = f^t(a)`, and again
      `Γ_t = P_{f^t}`.
    - Then `Λ_{s,t} := P_{f^s}^{T} P_{f^t} = P_{f^{t−s}}` is a permutation matrix, hence row-stochastic, and
      `Γ_s Λ_{s,t} = Γ_t` for every `s < t ≤ N`.
  - **Γ₁ deterministic on `V_O` is equivalent to Γ₁ being a permutation matrix on `V_O`.**
    - Every `b ∈ V_O` has a predecessor on the cycle `O`. So if `Γ_1^{α,O}` is deterministic, with
      `π_V φ(a, h) = f(a)` on `O`, then `f : V_O → V_O` is onto, hence bijective, and `Γ_1^{α,O} = P_f`.
    - Therefore, on these horizons, `pdiv_alpha(O)` holds iff `T^{α,O}` is a 0/1 matrix on `V_O`, and `pdiv_beta`
      holds iff `T^β` is a permutation matrix.
  - The B4 record is therefore a function of the comparison data. It is recorded because BSB:411 asks for it, and it
    carries no independent verdict.
- **How the tool computes it.**
  - On every toy and native instance, the tool uses Lemma PD, with witness `(s, t) = (1, N)` when it fails.
  - On every toy control, it also uses the definition, through the certified method below. The two methods must agree,
    and both must match the hand-derived values. A mismatch with an expected value exits 1, and a disagreement between
    the two methods exits 4. This is the countercontrol for Lemma PD.
- **The definitional method, frozen, with certificates [D].**
  - **Indexing.** For a pair `s < t ≤ N` on the row set `W = (w_0, …, w_{k−1})` (ascending), the unknown is
    `x ∈ ℚ^{k²}`, with `x_{i·k+j} = Λ(w_i, w_j)`. The constraints are `A x = b`, `x ≥ 0`, with `k² + k` rows in this
    order:
    - row `ai·k + j` (`ai, j < k`): `Σ_i Γ_s(w_ai, w_i)·x_{i·k+j} = Γ_t(w_ai, w_j)`;
    - row `k² + i` (`i < k`): `Σ_j x_{i·k+j} = 1`.
  - **Pair order.** Pairs are taken in lexicographic order of `(s, t)`. The family is declared P-divisible iff every
    pair is feasible. The search stops at the first infeasible pair.
  - **Search.** Any exact rational method may produce a candidate, for example exact phase-I simplex with Bland's rule,
    or `Λ = Γ_s^{−1}Γ_t` when `Γ_s` is invertible. **No candidate is trusted.** A pair's result counts only through its
    certificate, which the tool's independent checker verifies.
  - **The checker.**
    - (i) It rebuilds `A` and `b` itself, from the `Γ_s` and `Γ_t` the tool computed. For EX-CERT it uses the frozen
      `Γ_s` and `Γ_t` of the case. It never reads `A` or `b` from a certificate.
    - (ii) It checks shapes first. A `lambda` certificate must have exactly the rows `w_0, …, w_{k−1}`, each with
      exactly `k` entries. A `farkas` certificate must have exactly `k² + k` entries. A certificate of the wrong shape
      fails clause `shape`, and no other clause is evaluated for it.
    - (iii) It evaluates **every** remaining clause of the certificate's kind in exact rational arithmetic and records
      each one that fails. A certificate is valid iff no clause fails. The clauses are:
      - for `kind = "lambda"`: `nonnegative` (every entry `≥ 0`); `row_sums` (every row of `Λ` sums to 1, i.e. rows
        `k²…k²+k−1` of `A x = b`); `equality` (`Γ_s Λ = Γ_t`, i.e. rows `0…k²−1` of `A x = b`);
      - for `kind = "farkas"`: `ATy_nonnegative` (`(Aᵀ y)_v ≥ 0` for every `v < k²`); `bTy_negative` (`bᵀ y < 0`).
    - (iv) Coverage. For each family, the certificate entries cover exactly the pairs in lexicographic order up to and
      including the first infeasible pair, or every pair when none is infeasible. Those before the first infeasible
      pair are `lambda`; the first infeasible pair is `farkas`. No entry is missing or extra.
  - **The certificate file.** Every certificate is written to `c1/<id>.pdiv-certs.json` (schema
    `#/$defs/pdiv_certs`). `pdiv_certs_verified` is true iff (i)–(iv) hold for every entry and every family.
  - **Failures.** A certificate that fails, or a coverage failure, exits 4.
  - **Soundness [D].** A valid `Λ` (`x ≥ 0`, `Ax = b`) and a valid `y` (`Aᵀy ≥ 0`, `bᵀy < 0`) cannot coexist, since
    `bᵀy = (Aᵀy)ᵀx ≥ 0`. A correct checker on correctly computed `Γ` therefore admits neither a false "feasible" nor a
    false "infeasible".
  - **Example [D, a valid certificate, not a compared value].** Take CE-8, orbit `O_B`, pair `(1, 4)`: `Γ_1 = J/2`,
    `Γ_4 = I` and `k = 2`. Then `y = (−1, 0, 1, 0, 0, 0)` has `Aᵀy = 0` and `bᵀy = −1`. This is EX-CERT case 1 (§3.3).

### 2.5 `ℓ_min` (fixed before any result) [D; OQ-1 = A]

- **What the corpus says [P].**
  - Main:62: "the atypical short orbits of the idealized linear dynamics (fixed points, low-period cycles) are precisely
    observer-lacking substrata — an orbit of period `p` makes at most `p` states dynamically accessible, so for small
    `p` no partition of it can satisfy the high-capacity condition C3".
  - C3 is `log₂|𝒞_H| ≥ I*` (Main:78). The corpus does not quantify "small `p`".
- **The rule [O, OQ-1 = A].** `ℓ_min(I) := n_I + 1`, where `n_I = |𝒞_V|` of instance `I` under the readout in use
  (§2.2). It depends only on the declared parameters, so it is fixed before any result. The owner's ruling sets it
  "as an explicitly selected test criterion, not a physical threshold derived from OI" (#1059 c.6650820790).
- **Justification [D].**
  - By pigeonhole, an orbit with `|O| ≥ n + 1` revisits some visible value, so `n_a(O) ≥ 2` for some `a`: some root
    carries at least two hidden states on the orbit.
  - An orbit with `|O| ≤ n` can have `n_a(O) = 1` at every visited root. Then `T^{α,O}` is deterministic, and no
    hidden state on the orbit mediates anything. This is the weakest form of the C3 failure Main:62 describes: the
    orbit-restricted hidden capacity `log₂ max_a n_a(O)` is 0.
  - `n + 1` is the least length at which that capacity is guaranteed positive at some root by length alone. It is a
    necessary condition for an orbit to be observer-bearing, not a sufficient one.
  - It is consistent with the assessment's control. In CE-8, `n = 2` and `ℓ_min = 3`, so both orbits (length 4) count,
    as BSB:137 requires ("no period-based or C3-based exclusion … separates them").
- **Inclusive comparison.** An orbit is long iff `|O| ≥ ℓ_min`. Control CC-UNVIS has an orbit of length exactly
  `ℓ_min`.
- **Two choices that `ℓ_min` alone does not make.**
  - `ℓ_min` removes short orbits from the candidates for `O*`, which is the orbit side. It does not by itself say
    whether the credence prior ranges over them.
  - By the mixture identity, if every long orbit equals `T^β` on its visited rows, then on each row the short orbits'
    `n_a`-weighted aggregate must also equal `T^β`. That aggregate includes the kernel-forced fixed point at state 0
    (`waveSubstratum_phi_fixes_zero`), whose row is `δ₀`.
  - A long orbit whose `T^{α,O}` is a permutation matrix differs from every non-deterministic credence row.
  - The OQ-13 answer `13b` makes both choices for the comparison: the candidates are `Long′`, and the credence
    compared is `T^β`, whose prior ranges over all orbits. This fixes the credence C-1 compares, the representation's
    declared law with the declared uniform hidden input (Main:282). It does not select a physical prior (§1). All
    four combinations stay frozen as variants (§4.1), so that none can be chosen after the result; R0, S2 and S3 are
    diagnostics.
- **No other threshold yields a verdict.** Every orbit's `eq(O)` and `|O|` are recorded, so the record would support
  other thresholds. This run issues verdicts only at the frozen `ℓ_min`. Any other threshold or variant needs a new
  freeze.

### 2.6 Owner decisions, and how this preregistration reads them [O, with readings D]

- **QB-1 [O].** "Operational frequencies are the physical target; observer credences cannot by themselves establish a
  Born law."
  - Reading [D]: the frequency side of C-1's comparison is `T^{α,O}`, the cycle frequencies (Lemma A, BSB:240–241).
  - A FREQ verdict would show that the credence numbers coincide with that target for every candidate orbit on the
    instance. It does not establish a Born law (§9).
- **QB-2 [O].** "γ is read as an invariant prior followed by conditioning, with the prior's physical source left open."
  - Reading [D]: with the present-visible record `x₀ = a` and the prior over all of `S`, γ read this way is `unif(U_r)`
    conditioned on `A_r`. That is `unif({a} × 𝒞_H)` (BSB:209–216), whose one-step numbers are row `a` of `T^β`.
  - QB-2 does not fix which orbits the invariant prior ranges over. Every invariant law is a law on orbits (BSB:183–187),
    so restricting the support to a union of orbits keeps it invariant.
  - OQ-13 = `13b` fixes the credence compared in C-1 as `T^β`: the declared law, with the declared uniform hidden input,
    whose prior ranges over all orbits. It fixes what C-1 compares and does not select the physical prior. C-1 is
    silent on the prior's physical source.
- **OQ-11 = A [O].** The variant's credence is the QB-2 credence, and `T^{α,O}` is the QB-1 target at the cycle horizon
  only. The frequency/credence distinction and the cycle-horizon limitation are kept wherever a verdict is reported.
- **Main:62 and Main:282, as the owner reads them for this workstream [O] (#1059 c.6650820790).**
  - Main:62's exclusion of observer-lacking orbits constrains candidate observer histories. It does not by itself
    remove those orbits from the global β prior.
  - Main:282's uniform hidden-sector input remains a declared assumption.
  - An observer's posterior comes from conditioning the selected prior on an identified record.
  - So `T^β`, with all orbits in the prior, is the representation's declared law, and `Long′` restricts only which
    orbits are taken as candidates for the actual one.

### 2.7 Twin classes: the intrinsic word relation, with a frozen group as cross-check [D; OQ-15 = A]

- **The visible word of an orbit.** For an orbit `O` with cycle `(s_0, s_1, …, s_{k−1})`, where `s_0 = rep(O)` and
  `s_{t+1} = φ(s_t)`, its visible word is `w(O) := (π_V s_0, …, π_V s_{k−1})`, read cyclically. The word depends on
  `π_V`, so on a native instance the words and twin classes are computed separately for each readout.
- **`T^{α,O}` depends only on the primitive cyclic word.**
  - From the definitions of §2.3, `c_O(a, j) = #{t : w_t = a, w_{t+1 mod k} = j}` and `n_a(O) = #{t : w_t = a}`.
  - Both counts are unchanged under rotation of `w`.
  - If `w = u^e` with `u` primitive (not itself a power), both counts are `e` times those of `u`, so their ratio is
    unchanged.
  - Hence `T^{α,O}` depends only on the primitive root of `w(O)`, up to rotation.
- **The intrinsic relation.**
  - Let `root(O)` be the primitive root of `w(O)` (the shortest prefix `u` with `w = u^e`), and `e = word_power(O)`.
  - Let `primitive_word(O)` be the lexicographically least rotation of `root(O)`, compared elementwise as integers.
    This is its necklace (Lyndon) representative.
  - Two orbits are **twins** iff they have the same `primitive_word`. Twins have identical `T^{α,·}` rows on every row
    they visit, and their agreement is guaranteed by construction (reviews of `2f59aad7`, N6, and `df723247`, N7).
  - The **twin class** of an orbit is its class under this relation, and `class_rep(O)` is the least `rep` in the class.
  - `primitive_word`, `word_power` and `class_rep` are recorded per orbit. EX-WORD (§3.3) checks the primitive-root
    computation.
- **Every symmetry twin is a word twin [D].** Let `g` be a permutation of `S` that commutes with `φ` and fixes every
  visible value. Then `π_V(φ^t(g s)) = π_V(g(φ^t s)) = π_V(φ^t s)` for all `t`. So the orbit of `g s` has the same
  visible word as the orbit of `s`, read from `g s` and `s` respectively. Hence `gO` and `O` have the same
  `primitive_word`.
- **No frozen group can be complete.**
  - Any two orbits with the same cyclic visible word are exchanged by some visible-fixing bijection that commutes with
    `φ`: map the cycles onto each other state by state, aligned on matching visible values (review of `df723247`, N7(b)).
  - A concrete family, derived here by hand from the rule, is missing from `⟨σ⟩`:
    - **Translations.** By additivity (A5, `SubstratumInterfaceAudit.lean:211`), the phase-space map is additive. So
      `τ_z : x ↦ x + z` commutes with `φ` iff `φ(z) = z`.
    - **Fixed points.** `φ(p, c) = (c, Fc − p)` equals `(p, c)` iff `p = c` and `Fc = 2c`, i.e.
      `c_{i−1} + c_{i+1} = 2c_i` on the ring.
    - **Solving the recurrence.** The second difference vanishes, so `c_i = α + βi`. This closes around the ring iff
      `βL ≡ 0 (mod q)`. At `q = 2` the recurrence is `c_{i+1} = c_{i−1}`, with the same solution space.
    - **Hidden support.** `τ_z` fixes visible values iff `z` vanishes on `R`. At `r = 1` that forces `α = 0`, giving
      `z = (βi, βi)_i`, which is nonzero iff `q | L` (`q` prime). At `r = 2` it also forces `β = 0`.
    - **Where it applies.** A nonzero hidden-supported φ-fixed `z` exists exactly at the `r = 1` instances with
      `q | L`: N2 (`q = 2`, `L = 4`), N3 (`q = 3`, `L = 3`), N5 (`q = 2`, `L = 6`) and N10 (`q = 2`, `L = 8`). At `q = 2`
      with `L` even, `z` has `c = (0, 1, 0, 1, …)`.
    - **Further maps.** Maps of the form `x ↦ x + ℓ(x) z`, with `ℓ` a conserved linear functional, give more.

    None of these is in `⟨σ⟩`. No native orbit was computed for this.
  - So the twin relation is defined intrinsically by the word, not by a group.
- **The frozen groups, as a cross-check only.**
  - For each instance, `C1-INSTANCES.json` lists generators `symmetry_generators`, and `G` is the group they generate.
  - Before orbits are compared, the tool checks each generator `g` on all of `S`, and exits 4 if any of the following
    fails:
    - `bijective`: `g` is a bijection;
    - `commutes`: `g(φ(s)) = φ(g(s))` for every `s`;
    - `visible`: `π_V(g(s)) = π_V(s)` for every `s`.
  - **Cross-check.** For every orbit `O` and generator `g`, the orbit `gO` must have the same `primitive_word` as `O`.
    A violation exits 4. By the lemma above this cannot happen for a valid generator, so a violation exposes an error in
    the generator, the orbit decomposition or the word computation.
  - `symmetry_generators_ok` and `group_cross_check_ok` are recorded. EX-SYM (§3.3) exercises each generator clause.
  - The group does not define the classes. It only tests the tool.
- **Native instances: the reflection `σ` about site 0.**
  - **Definition.** `(σx)_i := x_{−i mod L}`, applied to both components of each site's `(prev, cur)` pair. On digits,
    `δ_i ↦ δ_{−i}`.
  - **`σ` commutes with `φ`.** Using the §2.1 step:
    - `prev′(σx)_i = cur(σx)_i = c_{−i} = prev′(x)_{−i}`;
    - `cur′(σx)_i = cur(σx)_{i−1} + cur(σx)_{i+1} − prev(σx)_i = c_{−i+1} + c_{−i−1} − p_{−i} = cur′(x)_{−i}`.

    So `φ(σx) = σ(φ(x))`. This uses only that the neighbour set `{i−1, i+1}` is mapped onto itself by `i ↦ −i`.
  - **`σ` fixes visible values exactly when `r = 1`.**
    - `σ` fixes site 0. At `r = 1`, `R = {0}`, so `σ` fixes `R` sitewise and changes only hidden sites.
    - At `r = 2`, `R = {0, 1}`, and `σ` sends site 1 to site `L − 1 ∉ R`, since `L ≥ 6`. It therefore changes the
      visible value of any state whose sites 1 and `L−1` differ, and fails `visible`. It is not a generator there.
    - The same holds under both readouts [D]: at `r = 1`, `σ` fixes site 0 and so fixes both `(prev_0, cur_0)` and
      `cur_0`; at `r = 2`, it changes `cur_1` whenever `cur_1 ≠ cur_{L−1}`. The `visible` clause is checked under the
      readout in use.
  - **Other candidate symmetries, and why they are not frozen.**
    - The reflection `i ↦ 1 − i` preserves `R = {0, 1}` as a set, but it swaps sites 0 and 1, so it changes visible
      values.
    - Translations move `R`.
    - Negation `x ↦ −x` and, at `q = 3`, multiplication by 2 both commute with `φ` by linearity. They change visible
      values when `q = 3`. At `q = 2` negation is the identity.
    - **Frozen as cross-check generators:** `⟨σ⟩` for `r = 1`, and the trivial group for `r = 2`. The translations
      `τ_z` above are not listed. The word relation already covers every twin they create, under either readout (under
      `cur`, `z` need vanish only on `cur` over `R`, so there can be more such translations; none is listed).
  - **WF-SIGMA** (§3.2) checks the implemented `σ` against a hand-computed image, so that a `σ` implemented as the
    identity, which would pass the generator check, is caught.
- **Toys [D, derived by hand].**

  | Toy | rep : `primitive_word` (power) | Word classes |
  |---|---|---|
  | CE-8 | 0: `01` (2); 4: `0011` (1) | `{0}`, `{4}` |
  | TT-4 | 0: `0011` (1) | `{0}` |
  | TT-6 | 0: `011202` (1) | `{0}` |
  | CC-TWIN | 0: `0011` (1); 4: `0011` (1) | `{0, 4}` |
  | CC-SHORT | 0: `0011` (1); 4: `0` (1); 5: `01` (1); 7: `1` (1) | four singletons |
  | CC-UNVIS | 0: `01` (2); 2: `2` (2) | `{0}`, `{2}` |
  | CC-VOID | 0: `01` (1) | `{0}` |
  | CC-SKEW | 0: `0011` (1); 4: `0` (1); 5: `1` (1) | three singletons |
  | CC-PERM | 0: `01` (2); 4: `0011` (1); 8, 10: `0` (1); 9, 11: `1` (1) | `{0}`, `{4}`, `{8, 10}`, `{9, 11}` |
  | CC-S3NOT | 0: `0011` (1); 4: `001` (1); 7: `1` (1) | three singletons |
  | CC-AGREE2 | 0: `0011` (1); 4: `00011101` (1) | `{0}`, `{4}` |
  | CC-ORDER | 0: `0102` (1); 4: `012` (1); 7: `1` (1); 8: `2` (1) | four singletons |

  - **The frozen cross-check generators.**
    - CC-TWIN: `s ↦ s+4 mod 8`, which maps rep 0 to rep 4. Both have word `0110`, so the generator stays inside one word
      class.
    - CC-PERM: the fixed-point swaps `8 ↔ 10` and `9 ↔ 11`, which stay inside `{8, 10}` and `{9, 11}`.
    - Every other toy: the identity.
  - **Agreement with r5.** The word classes coincide with the r5 group classes on every toy except the former
    CC-AGREE. There, words `0011` and `00110011 = (0011)²` form one word class. CC-AGREE is therefore replaced by
    CC-AGREE2 (§3.1).
- **How classes enter.** The pool and `shared_rows` of §4.1 count word classes, not orbits.

***

## 3. The frozen control set

The expected values are hand derivations of constructed toys, frozen in `C1-CONTROLS-EXPECTED.json`. §A.29's "rule, not
numbers" applies to the native decision rule of §4, which is frozen without reference to any native value. **No expected
value is given for any native instance.**

**Execution order.**
- The 25 controls and mutations run first, in the order of `C1-INSTANCES.json` (orders 1–25):
  - orders 1–11: the eleven r6 toys of §3.1;
  - orders 12–17: M-INJ, EX-ARITH, EX-SCHEMA, EX-CERT, EX-SYM and EX-WORD;
  - orders 18–21: WF-q2-L5, WF-q3-L4, WF-SIGMA and WF-0;
  - orders 22–25, added by the OQ-7 and OQ-10 rulings: the diagnostic toy CC-ORDER (§3.1), the mutation M-FRAG
    (§3.3), and WF-q2-L6-r2 and WF-CUR (§3.2).
- The 12 native instances follow (orders 26–37), in §2.2's run order, each evaluated under both readouts.
- The controls are shared by both readouts. One mismatch halts the whole run (OQ-2 = C).
- Native instances run only if every control and mutation has matched. A mismatch halts the run before any native
  instance is evaluated, so no native verdict is ever printed over a failed control (§A.29).

### 3.1 Toy controls (explicit maps; `s = v + n·h`)

In the table, `FREQ_V` abbreviates FREQ_VACUOUS. `sr` gives `shared_rows` for R0 / S1 / S2 / S3 (§4.1).

| id | `n`, `m` | `φ` as an array over `s = 0, 1, …` | R0 / S1 / S2 / S3 | `sr` | Purpose |
|---|---|---|---|---|---|
| CE-8 | 2, 4 | `[1, 2, 3, 0, 6, 7, 5, 4]` | NOT / NOT / NOT / FREQ_V | 2/2/2/0 | the assessment's counterexample (BSB:129–138) |
| TT-4 | 2, 2 | `[1, 3, 0, 2]` | FREQ_V ×4 | 0/0/0/0 | transitive toy, A2 (BSB:246): equality by construction |
| TT-6 | 3, 2 | `[1, 4, 3, 5, 2, 0]` | FREQ_V ×4 | 0/0/0/0 | transitive toy with unequal rows and `n = 3` |
| CC-TWIN | 2, 4 | `[1, 3, 0, 2, 5, 7, 4, 6]` | FREQ_V ×4 | 0/0/0/0 | two twin orbits (same word `0110`): agreement guaranteed by construction |
| CC-SHORT | 2, 4 | `[1, 3, 0, 2, 4, 6, 5, 7]` | FREQ / FREQ / FREQ_V / FREQ_V | 2/2/0/0 | short orbits that balance, excluded by `ℓ_min` |
| CC-UNVIS | 3, 2 | `[1, 3, 5, 4, 0, 2]` | FREQ_V / VOID / FREQ_V / VOID | 0/0/0/0 | unvisited row; orbit length exactly `ℓ_min`; `Long′ = ∅` |
| CC-VOID | 2, 1 | `[1, 0]` | VOID ×4 | 0/0/0/0 | no orbit reaches `ℓ_min`; void takes precedence over equality |
| CC-SKEW | 2, 3 | `[1, 3, 0, 2, 4, 5]` | NOT / NOT / FREQ_V / FREQ_V | 2/2/0/0 | short orbits that skew `T^β` |
| CC-PERM | 2, 6 | `[1, 2, 3, 0, 5, 7, 4, 6, 8, 9, 10, 11]` | NOT / FREQ / NOT / FREQ_V | 2/2/2/0 | a long orbit with a permutation `T^{α,O}` |
| CC-S3NOT | 2, 4 | `[2, 3, 1, 0, 6, 4, 5, 7]` | NOT ×4 | 2/2/2/2 | two C4-bearing long orbits that disagree: S3 reaches NOT |
| CC-AGREE2 | 2, 6 | `[2, 3, 1, 0, 6, 7, 8, 9, 5, 10, 11, 4]` | FREQ ×4 | 2/2/2/2 | two long orbits with different primitive words (`0011`, `00011101`) that agree: non-vacuous FREQ under every variant |
| CC-ORDER | 3, 3 | `[1, 3, 0, 2, 5, 6, 4, 7, 8]` | NOT / NOT / FREQ_V / FREQ_V | 3/3/0/0 | diagnostic of the `first_mismatch` order (OQ-10), gating: the `a`-major order of `first_mismatch` differs from the `j`-major order |

Each outcome reached per variant:

| Variant | Non-vacuous FREQ | FREQ_VACUOUS | NOT | VOID_NO_ORBIT |
|---|---|---|---|---|
| R0 | CC-SHORT, CC-AGREE2 | TT-4, TT-6, CC-TWIN, CC-UNVIS | CE-8, CC-SKEW, CC-PERM, CC-S3NOT, CC-ORDER | CC-VOID |
| S1 | CC-SHORT, CC-PERM, CC-AGREE2 | TT-4, TT-6, CC-TWIN | CE-8, CC-SKEW, CC-S3NOT, CC-ORDER | CC-UNVIS, CC-VOID |
| S2 | CC-AGREE2 | TT-4, TT-6, CC-TWIN, CC-SHORT, CC-UNVIS, CC-SKEW, CC-ORDER | CE-8, CC-PERM, CC-S3NOT | CC-VOID |
| S3 | CC-AGREE2 | TT-4, TT-6, CE-8, CC-TWIN, CC-SHORT, CC-SKEW, CC-PERM, CC-ORDER | CC-S3NOT | CC-UNVIS, CC-VOID |

CC-TWIN and CC-AGREE2 give the same verdict under all four variants, so neither enters the separation table. CC-ORDER
has CC-SKEW's verdict pattern; it is a diagnostic of the `first_mismatch` order and adds no separation.

**CC-ORDER gates like every control [D].** It is one of the 25 controls, and a mismatch in any of its compared fields
exits 1 and halts the run (§3). "Diagnostic" names the field it targets, the order of `first_mismatch`. It does not
make CC-ORDER a non-gating record like RX-ORD (§3.4). The owner's ruling calls it a "diagnostic toy" (OQ-10) and uses
"diagnostic record" for RX-ORD (OQ-7); the gating reading, which matches the ruling's total of 25, is put to the owner
before `F`: the owner's designation of `F` confirms it, and a contrary ruling is written in under §7 steps 2–3 before
`F`.

Every pair of variants is separated by at least one control:

| Pair | Separating controls |
|---|---|
| R0 / S1 | CC-UNVIS, CC-PERM |
| R0 / S2 | CC-SHORT (FREQ against FREQ_VACUOUS), CC-SKEW (NOT against FREQ_VACUOUS) |
| R0 / S3 | CE-8, CC-SHORT, CC-UNVIS, CC-SKEW, CC-PERM |
| S1 / S2 | CC-SHORT, CC-UNVIS, CC-SKEW, CC-PERM |
| S1 / S3 | CE-8, CC-SHORT, CC-SKEW, CC-PERM |
| S2 / S3 | CE-8, CC-UNVIS, CC-PERM |

**Hand derivations [D].** In each toy, `ℓ_min = n + 1`.

- **CE-8.** The states are `(0,0)=0, (1,0)=1, (0,1)=2, (1,1)=3, (0,2)=4, (1,2)=5, (0,3)=6, (1,3)=7`.
  - Orbits:
    - `O_A` (rep 0): `0→1→2→3→0`, that is `(0,0)→(1,0)→(0,1)→(1,1)`, with visible sequence `0101`;
    - `O_B` (rep 4): `4→6→5→7→4`, that is `(0,2)→(0,3)→(1,2)→(1,3)`, with visible sequence `0011`.
  - Next visible values over `h = 0..3`: from root 0 they are `1, 1, 0, 1`, and from root 1 they are `0, 0, 1, 0`. So
    `T^β = [[1/4, 3/4], [3/4, 1/4]]` (BSB:133).
  - `T^{α,O_A} = [[0, 1], [1, 0]]` and `T^{α,O_B} = J/2` (BSB:135–136).
  - The sketch's check: `T^β(0, 1) = 3/4` against `T^{α,O_A}(0, 1) = 1` and `T^{α,O_B}(0, 1) = 1/2` (BSB:414).
  - `ℓ_min = 3`, so both orbits are long.
  - Verdicts:
    - R0: both orbits fail, each with first mismatch `(0, 0)` (`0` against `1/4`, and `1/2` against `1/4`). R0 is NOT.
    - S1: `O_A` is a permutation, so `Long′ = {O_B}`. `O_B` against `T^β` gives NOT, with mismatch `(0, 0)`, `1/2`
      against `1/4`.
    - S2: `U_long = S`, so `T^{β_long} = T^β`. S2 is NOT.
    - S3: `T^{β_c4} = T^{α,O_B} = J/2`. Every comparison matches, but `Long′ = {O_B}` is a single orbit, so each row's
      credence pools one orbit and `shared_rows = 0`. S3 is FREQ_VACUOUS.
    - `shared_rows`: R0, S1 and S2 have 2, since both orbits visit rows 0 and 1 and each credence pools both; S3 has 0.
  - P-divisibility (BSB:153–154): `O_A` is divisible (`Γ₁` = swap, `Γ₂ = I`). `O_B` is not (`Γ₁ = J/2`, `Γ₄ = I`). β is
    not, with `ord(φ) = 4`.
- **TT-4.** One orbit, `0→1→3→2→0`, that is `(0,0)→(1,0)→(1,1)→(0,1)`.
  - `T^β = T^{α,S} = J/2`, and every restricted credence is `J/2`.
  - There is one orbit, so every credence pools that orbit alone and `shared_rows = 0` under every variant. All four
    verdicts are FREQ_VACUOUS, which is the A2 equality holding by construction.
  - α and β are both indivisible, and `ord(φ) = 4`.
- **TT-6.** The states are `(v,h) = v + 3h`. One orbit, `0→1→4→2→3→5→0`, that is
  `(0,0)→(1,0)→(1,1)→(2,0)→(0,1)→(2,1)`, with visible sequence `011202`.
  - `T^β = T^{α,S} = [[0, 1/2, 1/2], [0, 1/2, 1/2], [1, 0, 0]]`, and every restricted credence equals it.
  - There is one orbit, so `shared_rows = 0` under every variant. All four verdicts are FREQ_VACUOUS.
  - α and β are indivisible, and `ord(φ) = 6`.
- **CC-TWIN.** The orbits are rep 0 (`0→1→3→2→0`) and rep 4 (`4→5→7→6→4`); rep 4 is the TT-4 pattern on `h ∈ {2, 3}`.
  - Every credence is `J/2`, and both orbits give `J/2`.
  - Every comparison matches. But both orbits have visible word `0110`, whose primitive word is `0011` (§2.7), so they
    form one twin class. Each row's pool is that one class, so `shared_rows = 0` under every variant, and all four
    verdicts are FREQ_VACUOUS. The agreement is guaranteed by construction; the comparison does not find it.
  - The frozen cross-check generator `s ↦ s+4 mod 8` (the hidden shift `h ↦ h + 2`) maps rep 0 to rep 4, which lies in
    the same word class.
  - `orbit_class_count = 1`, and `class_rep = 0` for both orbits.
  - Every family is indivisible, and `ord(φ) = 4`.
- **CC-SHORT.** The orbits are:
  - rep 0, of length 4 (TT-4 on `h ∈ {0, 1}`);
  - rep 4, the fixed point `(0,2)`;
  - rep 5, the 2-cycle `(1,2) ↔ (0,3)`;
  - rep 7, the fixed point `(1,3)`.

  Then:
  - `T^β = J/2`: root 0 over `h = 0..3` gives `1, 0, 0, 1`, and so does root 1.
  - Only rep 0 is long. It is `J/2` and not a permutation, so `Long = Long′ = {rep 0}`, and
    `T^{β_long} = T^{β_c4} = J/2`.
  - R0 and S1 are FREQ, with `shared_rows = 2`: `T^β` pools rep 0 with rep 4 and rep 5 on row 0, and with reps 5 and 7
    on row 1.
  - S2 and S3 are FREQ_VACUOUS, with `shared_rows = 0`: their credence pools rep 0 alone.
  - The short orbits do not match, but on each row they balance to `J/2`:
    - rep 4: `V_O = {0}`, row `[1, 0]`, unvisited rows `{1}`;
    - rep 5: rows `[[0, 1], [1, 0]]`;
    - rep 7: `V_O = {1}`, row `[0, 1]`, unvisited rows `{0}`.
  - P-divisibility: rep 0 is not divisible; reps 4, 5 and 7 are; β is not. `ord(φ) = 4`.
- **CC-UNVIS.** The states are `v + 3h`. The orbits are:
  - rep 0: `0→1→3→4→0`, that is `(0,0)→(1,0)→(0,1)→(1,1)`, visiting rows `{0, 1}` only;
  - rep 2: the 2-cycle `(2,0) ↔ (2,1)`.

  Then:
  - `T^β = [[0, 1, 0], [1, 0, 0], [0, 0, 1]]`.
  - `ℓ_min = 4 = |O|` for rep 0, the inclusive boundary. Row 2 is unvisited and excluded. On rows 0 and 1, `eq = true`.
    Rows 0 and 1 are visited by rep 0 alone, so `T^β` there is rep 0's own rows, and `shared_rows = 0`. R0 is
    FREQ_VACUOUS.
  - `T^{β_long}` has rows `{0, 1}`, `[0, 1, 0]` and `[1, 0, 0]`. With `shared_rows = 0`, S2 is FREQ_VACUOUS.
  - `T^{α,rep 0}` is a permutation matrix on `{0, 1}`, so `Long′ = ∅`. S1 and S3 are VOID_NO_ORBIT, and `T^{β_c4}` is the
    empty map.
  - A tool that compared the unvisited row, or failed on `n_2(O) = 0`, would return NOT or error, and the control would
    fail.
  - P-divisibility: both orbits are divisible, and β is divisible (`T^β` is a permutation). `ord(φ) = 4`.
- **CC-VOID.** One orbit, `(0,0) ↔ (1,0)`, of length `2 < ℓ_min = 3`.
  - The map is transitive and `eq = true`, but all four verdicts are VOID_NO_ORBIT, and both restricted credences are
    the empty map.
  - α and β are P-divisible, and `ord(φ) = 2`.
- **CC-SKEW.** The states are `(0,0)=0, (1,0)=1, (0,1)=2, (1,1)=3, (0,2)=4, (1,2)=5`.
  - The orbits are:
    - rep 0, `0→1→3→2→0`, with `T^α = J/2`, not a permutation;
    - rep 4, the fixed point `(0,2)`;
    - rep 5, the fixed point `(1,2)`.
  - `T^β`: root 0 over `h = 0, 1, 2` gives `1, 0, 0`, and root 1 gives `1, 0, 1`. So `T^β = [[2/3, 1/3], [1/3, 2/3]]`.
  - `ℓ_min = 3`, so `Long = Long′ = {rep 0}` and `T^{β_long} = T^{β_c4} = J/2`.
  - Verdicts:
    - R0 and S1 are NOT, with mismatch `(0, 0)`, `1/2` against `2/3`, and `shared_rows = 2`.
    - S2 and S3 match, but their credence pools rep 0 alone, so `shared_rows = 0` and both are FREQ_VACUOUS.
  - Short orbits: rep 4 has row `[1, 0]` (mismatch `1` against `2/3`), and rep 5 has row `[0, 1]` (mismatch at
    `(1, 0)`, `0` against `1/3`). Both are P-divisible.
  - rep 0 and β are indivisible, and `ord(φ) = 4`.
- **CC-PERM.** The states are `v + 2h`, `h = 0..5`.
  - The orbits are:
    - rep 0, `0→1→2→3→0`, the CE-8 `O_A` pattern on `h ∈ {0, 1}`, with `T^α = [[0, 1], [1, 0]]`;
    - rep 4, `4→5→7→6→4`, the TT-4 pattern on `h ∈ {2, 3}`, with `T^α = J/2`;
    - reps 8, 9, 10 and 11, the fixed points `(0,4)`, `(1,4)`, `(0,5)`, `(1,5)`.
  - `T^β`: root 0 over `h = 0..5` gives `1, 1, 1, 0, 0, 0`, and root 1 gives `0, 0, 1, 0, 1, 1`. So `T^β = J/2`.
  - Reps 0 and 4 are long, and `Long′ = {rep 4}`.
  - Verdicts:
    - R0: rep 4 has `eq = true`. Rep 0 fails at `(0, 0)`, `0` against `1/2`. R0 is NOT.
    - S1: rep 4 against `T^β`. `T^β` pools rep 4 with rep 0 and the fixed points on both rows, so `shared_rows = 2`.
      S1 is FREQ.
    - S2: `T^{β_long}` has row 0 counts `[0, 2] + [1, 1] = [1, 3]`, giving `[1/4, 3/4]`, and row 1 counts
      `[2, 0] + [1, 1] = [3, 1]`, giving `[3/4, 1/4]`. Both long orbits fail at `(0, 0)` (`0` against `1/4`, and `1/2`
      against `1/4`), so S2 is NOT.
    - S3: `T^{β_c4} = J/2`, and rep 4 matches. `Long′ = {rep 4}` is a single orbit, so `shared_rows = 0` and S3 is
      FREQ_VACUOUS.
    - `shared_rows` is 2 for R0, S1 and S2, and 0 for S3.
    - The word classes (§2.7) are `{0}` (`01`, power 2), `{4}` (`0011`), `{8, 10}` (`0`) and `{9, 11}` (`1`), so
      `orbit_class_count = 4`. The cross-check generator `8 ↔ 10, 9 ↔ 11` stays inside them.
    - On row 0 the R0/S1 pool is the classes `{0}`, `{4}` and `{8, 10}`. On row 1 it is `{0}`, `{4}` and `{9, 11}`.
      Each row still pools at least two classes, so the `shared_rows` values above are unchanged. `class_rep` is 8 for
      reps 8 and 10, and 9 for reps 9 and 11.
  - The fixed points do not match `T^β`, and each is P-divisible.
  - Rep 0 is P-divisible; rep 4 and β are not. `ord(φ) = 4`.
- **CC-S3NOT** (proposed in the review of `1962c378`; values derived here by hand). The states are
  `(0,0)=0, (1,0)=1, (0,1)=2, (1,1)=3, (0,2)=4, (1,2)=5, (0,3)=6, (1,3)=7`. `φ`: `0→2, 1→3, 2→1, 3→0, 4→6, 5→4, 6→5,
  7→7`.
  - The orbits are:
    - rep 0, `0→2→1→3→0`, visible `0011`. Row 0: `(0,0)→(0,1)` gives 0 and `(0,1)→(1,0)` gives 1. Row 1:
      `(1,0)→(1,1)` gives 1 and `(1,1)→(0,0)` gives 0. So `T^α = J/2`, which is not a permutation.
    - rep 4, `4→6→5→4`, visible `001`. Row 0: `(0,2)→(0,3)` gives 0 and `(0,3)→(1,2)` gives 1. Row 1: `(1,2)→(0,2)`
      gives 0. So `T^α = [[1/2, 1/2], [1, 0]]`, with `n_a = {0: 2, 1: 1}`, which is not a permutation.
    - rep 7, the fixed point `(1,3)`, with row 1 `[0, 1]`.
  - `T^β`: root 0 over `h = 0..3` gives `0, 1, 0, 1`, and root 1 gives `1, 0, 0, 1`. So `T^β = J/2`.
  - `ℓ_min = 3`, so `Long = Long′ = {rep 0, rep 4}`. Both visit rows 0 and 1, so `shared_rows = 2` under every variant.
  - Verdicts:
    - R0 and S1: rep 0 matches `J/2`. Rep 4 fails at `(1, 0)`, `1` against `1/2`. Both are NOT, with the first
      mismatch at rep 4.
    - S2 and S3: since `Long = Long′`, `T^{β_long} = T^{β_c4}`. Row 0 is `([1, 1] + [1, 1])/4 = [1/2, 1/2]`. Row 1 is
      `([1, 1] + [1, 0])/3 = [2/3, 1/3]`. Rep 0 fails at `(1, 0)`, `1/2` against `2/3`, and rep 4 fails at `(1, 0)`, `1`
      against `2/3`. Both variants are NOT, with the first mismatch at rep 0, failing on row 1.
  - P-divisibility: reps 0 and 4 are indivisible (witnesses `[1, 4]` and `[1, 3]`). Rep 7 is divisible. β is
    indivisible. `ord(φ) = lcm(4, 3, 1) = 12`.
- **CC-AGREE2** (proposed in the review of `df723247`; values derived here by hand). It replaces r5's CC-AGREE, whose
  words `0011` and `(0011)²` were one word class.
  - The states are `v + 2h`, `h = 0..5`. `φ`: `0→2, 1→3, 2→1, 3→0, 4→6, 5→7, 6→8, 7→9, 8→5, 9→10, 10→11, 11→4`.
  - The orbits are:
    - rep 0, `[0, 2, 1, 3]`, visible `0011`. Row 0: `0→2` gives 0 and `2→1` gives 1. Row 1: `1→3` gives 1 and `3→0`
      gives 0. So `T^α = J/2`, with `n_a = {0: 2, 1: 2}`.
    - rep 4, `[4, 6, 8, 5, 7, 9, 10, 11]`, visible `00011101`.
      - Row 0: `4→6` gives 0, `6→8` gives 0, `8→5` gives 1, and `10→11` gives 1.
      - Row 1: `5→7` gives 1, `7→9` gives 1, `9→10` gives 0, and `11→4` gives 0.
      - So `T^α = J/2`, with `n_a = {0: 4, 1: 4}`.
  - Every state is covered, `orbit_count = 2` and `ord(φ) = lcm(4, 8) = 8`.
  - `T^β`:
    - root 0 over `h = 0..5` (states `0, 2, 4, 6, 8, 10`) gives `0, 1, 0, 0, 1, 1`;
    - root 1 (states `1, 3, 5, 7, 9, 11`) gives `1, 0, 1, 1, 0, 0`;
    - so `T^β = J/2`, which is doubly stochastic.
  - `ℓ_min = 3`, so both orbits are long. Neither `T^α` is a permutation, so `Long = Long′ = {0, 4}` and
    `T^{β_long} = T^{β_c4} = T^β = J/2`.
  - **No twins.**
    - `0011` is primitive, and its least rotation is `0011`.
    - `00011101` is primitive: it has no period 1, 2 or 4, since `0001 ≠ 1101`. Its rotations are `00011101`,
      `00111010`, `01110100`, `11101000`, `11010001`, `10100011`, `01000111` and `10001110`, and the least is
      `00011101`.
    - The two primitive words differ, so there are two classes.
  - `shared_rows = 2` under every variant, and every comparison matches. All four verdicts are FREQ: two orbits with
    different primitive words that agree.
  - P-divisibility: both orbits and β are indivisible (witnesses `[1, 4]` and `[1, 8]`; β horizon 8).
- **CC-ORDER** (the `n = 3` first-mismatch diagnostic toy of OQ-10; map constructed and values derived here by hand
  [D] in r7; every value recomputed exactly by the independent review of r7, #1082 c.6651181144).
  - **Its purpose.** PREREG r6 §8.2 item 10 recorded the C-1 reviewers' unadded suggestion: "an `n = 3` toy that
    discriminates the order of `first_mismatch`". The frozen order is `a`-major (§2.3). With `n = 2`, every row that
    mismatches does so at both `j = 0` and `j = 1`, since rows sum to 1, so the `a`-major and `j`-major least mismatches
    coincide. With `n = 3` they can differ, and CC-ORDER makes them differ.
  - **The states.** `s = v + 3h`, `h = 0, 1, 2`: `(0,0)=0, (1,0)=1, (2,0)=2, (0,1)=3, (1,1)=4, (2,1)=5, (0,2)=6, (1,2)=7,
    (2,2)=8`. `φ`: `0→1, 1→3, 2→0, 3→2, 4→5, 5→6, 6→4, 7→7, 8→8`. Every value occurs once, so `φ` is a bijection.
  - **The orbits.**
    - rep 0, `[0, 1, 3, 2]`, visible `0102`, which is primitive; its least rotation is `0102`.
      - Row 0: `0→1` gives 1, and `3→2` gives 2. Row 1: `1→3` gives 0. Row 2: `2→0` gives 0.
      - So `n_a = {0: 2, 1: 1, 2: 1}` and `T^α = [[0, 1/2, 1/2], [1, 0, 0], [1, 0, 0]]`, which is not a permutation.
    - rep 4, `[4, 5, 6]`, visible `120`; its least rotation is `012`. Rows: `6→4` gives `0→1`, `4→5` gives `1→2`, and
      `5→6` gives `2→0`. So `T^α` is the cyclic permutation `0→1→2→0`.
    - rep 7, the fixed point `(1,2)`, with row 1 `[0, 1, 0]`.
    - rep 8, the fixed point `(2,2)`, with row 2 `[0, 0, 1]`.
    - Four orbits with four distinct primitive words, so `orbit_class_count = 4`. `ord(φ) = lcm(4, 3, 1, 1) = 12`.
  - **`T^β`.**
    - root 0 (states 0, 3, 6) gives `1, 2, 1`, so row 0 is `[0, 2/3, 1/3]`;
    - root 1 (states 1, 4, 7) gives `0, 2, 1`, so row 1 is `[1/3, 1/3, 1/3]`;
    - root 2 (states 2, 5, 8) gives `0, 0, 2`, so row 2 is `[2/3, 0, 1/3]`.
    - The column sums are `3, 3, 3`, so `T^β` is doubly stochastic. The mixture identity holds on every row: for row 0,
      `2·[0, 1/2, 1/2] + 1·[0, 1, 0] = [0, 2, 1]`.
  - **Long orbits.** `ℓ_min = 4`, so `Long = Long′ = {rep 0}`, and `T^{β_long} = T^{β_c4} = T^{α,rep 0}`.
  - **Verdicts.**
    - R0 and S1: rep 0 against `T^β`. Row 0 agrees at `j = 0` (`0` against `0`) and first differs at `(0, 1)`, `1/2`
      against `2/3`. Row 1 differs at `(1, 0)`, `1` against `1/3`, and row 2 at `(2, 0)`, `1` against `2/3`.
      - The `a`-major first mismatch is `(0, 1)`. A `j`-major order would give `(1, 0)`, and a descending-`j` order
        would give `(0, 2)`. So a wrong order is caught by the compared `first_mismatch`.
      - Every row's pool contains rep 0 and rep 4, and rows 1 and 2 also a fixed point: at least two word classes on
        each of the three rows, so `shared_rows = 3`. Both are NOT.
    - S2 and S3: the credence is rep 0's own rows and the pool is rep 0 alone, so every comparison matches and
      `shared_rows = 0`. Both are FREQ_VACUOUS.
  - **Short orbits.** rep 4 first differs from `T^β` at `(0, 1)`, `1` against `2/3`; rep 7 at `(1, 0)`, `0` against
    `1/3`; rep 8 at `(2, 0)`, `0` against `2/3`. All three are P-divisible (their rows are permutations).
  - **P-divisibility.** rep 0 is indivisible (witness `[1, 4]`), and β is indivisible (horizon 12).

### 3.2 Native-faithfulness controls (hand-derived, [D])

These check that the implemented `φ` is the §2.1 rule.
- They run in the control phase, before any native instance, and compute `φ` on the listed states only, with both
  implementations of §2.1.
- A mismatch, or a disagreement between the two implementations, exits 1 and halts.
- WF-0 is a sanity check only: `φ(0) = 0` holds for every additive map, so it is not a faithfulness checkpoint.

The controls:
- **WF-0** (for the parameters of each of N1–N12): `φ[0] = 0` (`waveSubstratum_phi_fixes_zero`,
  `StochasticInterface.lean:101`).
- The visible values listed for WF-q3-L4, WF-q2-L5 and WF-q2-L6-r2 are under the `pc` readout; WF-CUR lists them under
  `cur`.
- **WF-q3-L4** (the parameters of N7), starting from `p = (0,0,0,0)`, `c = (1,0,0,0)`:
  - step 1: `p′ = (1,0,0,0)`, `c′ = (0,1,0,1)`;
  - step 2: `p″ = (0,1,0,1)`, `c″ = (1,0,2,0)`;
  - as state indices: `1 → 741 → 2377`; visible values (`n = 9`): `1 → 3 → 1`.
- **WF-SIGMA** (the parameters of N7: `q = 3`, `L = 4`, `r = 1`). The tool checks the implemented `σ` (§2.7) on one
  state, `x`: `p = (0,0,0,0)`, `c = (0,1,0,0)`, state index 9.
  - `σx` has `c = (0,0,0,1)`, state index 729, with visible value `9 mod 9 = 729 mod 9 = 0`.
  - `φ(x)` has `p′ = (0,1,0,0)` and `c′ = (c₃+c₁, c₀+c₂, c₁+c₃, c₂+c₀) = (1,0,1,0)`, state index
    `1 + 3·9 + 1·81 = 109`.
  - `σ(φ(x))` has `p = (0,0,0,1)` and `c = (1,0,1,0)`, state index `1 + 81 + 3·729 = 2269`.
  - `φ(σx)` has `p′ = (0,0,0,1)` and `c′ = (1,0,1,0)`, state index 2269. So `φ(σx) = σ(φ(x))` on this state.
  - The visible values of `φ(x)` and `σ(φ(x))` are both `1`.
  - Expected: `σ(9) = 729 ≠ 9`, so `σ` is not the identity; `σ(109) = 2269`; and `φ(729) = 2269`.
- **WF-q2-L5** (the parameters of N4), starting from `p = 0`, `c = (1,0,0,0,0)`:
  - step 1: `p′ = (1,0,0,0,0)`, `c′ = (0,1,0,0,1)`;
  - step 2: `p″ = (0,1,0,0,1)`, `c″ = (1,0,1,1,0)`;
  - as state indices: `1 → 262 → 601`; visible values (`n = 4`): `1 → 2 → 1`.
- **WF-q2-L6-r2** (the parameters of N6: `q = 2`, `L = 6`, `r = 2`, readout `pc`, `n = 16`; added by OQ-10 = C). It
  checks the `r = 2` visible projection `π_V(s) = s mod 16 = δ_0 + 4δ_1`, which no other hand-derived value checks.
  Starting from `p = 0`, `c = (1,0,0,0,0,0)`:
  - step 1: `p′ = (1,0,0,0,0,0)`; `c′_1 = c_0 + c_2 = 1`, `c′_5 = c_4 + c_0 = 1`, and the rest are 0, so
    `c′ = (0,1,0,0,0,1)`;
  - step 2: `p″ = (0,1,0,0,0,1)`; `c″_0 = c′_5 + c′_1 − p′_0 = 1 + 1 − 1 = 1`, `c″_2 = c′_1 + c′_3 = 1`,
    `c″_4 = c′_3 + c′_5 = 1`, and `c″_1 = c″_3 = c″_5 = 0`, so `c″ = (1,0,1,0,1,0)`;
  - digits `δ = (1,0,0,0,0,0)`, `(2,1,0,0,0,1)` and `(1,2,1,0,1,2)`; state indices `1 → 1030 → 2329`; visible values
    `1 → 6 → 9`. A projection that read site 0 only would give `1 → 2 → 1`.
- **WF-CUR** (the parameters of N6, readout `cur`, `n = 4`; added by OQ-2 = C and OQ-10 = C). It checks
  `π_V(s) = Σ_{i<r} (δ_i mod q)·q^i = c_0 + 2c_1`. Starting from `p = 0`, `c = (0,1,0,0,0,0)`:
  - step 1: `p′ = (0,1,0,0,0,0)`; `c′_0 = c_5 + c_1 = 1`, `c′_2 = c_1 + c_3 = 1`, and the rest are 0, so
    `c′ = (1,0,1,0,0,0)`;
  - step 2: `p″ = (1,0,1,0,0,0)`; `c″_1 = c′_0 + c′_2 − p′_1 = 1 + 1 − 1 = 1`, `c″_3 = c′_2 + c′_4 = 1`,
    `c″_5 = c′_4 + c′_0 = 1`, and `c″_0 = c″_2 = c″_4 = 0`, so `c″ = (0,1,0,1,0,1)`;
  - digits `δ = (0,1,0,0,0,0)`, `(1,2,1,0,0,0)` and `(2,1,2,1,0,1)`; state indices `4 → 25 → 1126`; `cur` visible
    values `2 → 1 → 2`.
  - Wrong projections are caught at step 0: the low index digit `s mod 4 = δ_0` gives 0, the reversed order
    `2c_0 + c_1` gives 1, and the `pc` value `s mod 16` gives 4.

### 3.3 Mutations and unit controls

- **M-INJ (bijectivity check).**
  - The rule is the §2.1 rule with the `−p` term deleted, `(p, c) ↦ (c, A c)`, at `q = 2`, `L = 3`, `r = 1`. It is
    computed by both implementations: the site loop without `−p_i`, and the linear map `[[0, I], [0, A]]`.
  - Two states with the same `c` and different `p` collide, so `φ` is not injective [D].
  - Expected: `phi_impls_agree = true`, `injective = false` and `evaluated_beyond_injectivity = false`. If the tool
    reports `injective = true`, the run exits 1.
- **M-FRAG (closure check; OQ-7 = C).** The closure and partition checks of §2.0 are applied to two frozen candidate
  orbit decompositions of TT-4's `φ = [1, 3, 0, 2]`:
  - case 1, `[[0, 1, 3, 2]]`: `φ(0) = 1`, `φ(1) = 3`, `φ(3) = 2` and `φ(2) = 0`, so the list is closed, and it covers
    `S`. Closure holds and the partition holds;
  - case 2, `[[0, 1], [3, 2]]`: `φ(1) = 3 ≠ 0` and `φ(2) = 0 ≠ 3`, so neither list is closed, while the two lists still
    partition `S`. Closure fails and the partition holds. This is the fragmented decomposition that the mixture
    identity and `Σ|O| = |S|` cannot detect.
  - Expected: `closure_ok = [true, false]`, `partition_ok = [true, true]` and `evaluated_beyond_closure = false` (no orbit
    analysis runs on a decomposition that fails closure). `evaluated_beyond_closure` is one boolean over both cases: it
    is `true` iff any orbit analysis ran on a case whose closure check failed. A case that passes closure does not set
    it. The detection is a compared field, as for M-INJ. A different outcome exits 1.
- **EX-ARITH (exact comparison).** The comparator of §2.3 is applied to these frozen pairs:
  - `("1/3", "6004799503160661/18014398509481984")` → unequal. The second value is the IEEE-754 double nearest `1/3`,
    `(2⁵⁴ − 1)/(3·2⁵⁴)`, so a floating-point comparison would report equality;
  - `("2/6", "1/3")` → equal, after reduction to lowest terms;
  - `("3/4", "3/4")` → equal;
  - `("0", "0/5")` → equal.
- **EX-SCHEMA (two-sided).** The output validator of §5 is applied to frozen fragments, each against a named subschema
  of `C1-OUTPUT-SCHEMA.json`. The expected result gives `schema_valid` and, for a rejection, `violation_path`: the
  RFC 6901 JSON Pointer of the single violating value, relative to the fragment's root. Each rejected fragment has
  exactly one violating value.
  1. `probability`, `"1/2"` → valid.
  2. `probability`, `"2/4"` → invalid at `""` (not in lowest terms).
  3. `matrix`, `{"0": ["1/4", "3/4"], "1": ["3/4", "1/4"]}` → valid.
  4. `matrix` (`T_beta`-shaped), `{"0": [0.75, "1/4"]}` → invalid at `/0/0`.
  5. `matrix` (`T_alpha`-shaped), `{"1": ["0", 1]}` → invalid at `/1/1`.
  6. `mismatch`, `{"a": 0, "j": 0, "alpha": "0", "beta": "1/4"}` → valid.
  7. `mismatch` (`first_mismatch`-shaped), `{"a": 0, "j": 0, "alpha": 0.5, "beta": "1/4"}` → invalid at `/alpha`.
- **EX-CERT (the checker of §2.4).** The checker is applied to frozen certificates, with `W = {0, 1}`, `k = 2` and the
  constraint order of §2.4. It rebuilds `A` and `b` from each case's `Γ_s` and `Γ_t`. The expected result per case is
  `valid` or `invalid`, plus the list of failed clauses. Hand derivations [D]:

  | # | `Γ_s` → `Γ_t` | Certificate | Hand check | Result | Failed clauses |
  |---|---|---|---|---|---|
  | 1 | `J/2 → I` | Farkas `y = (−1, 0, 1, 0, 0, 0)` | `Aᵀy = 0`; `bᵀy = −1` | valid | none |
  | 2 | `J/2 → I` | Farkas `y = 0` | `Aᵀy = 0`; `bᵀy = 0` | invalid | `bTy_negative` |
  | 3 | `J/2 → I` | `Λ = I` | `≥ 0`; rows sum to 1; `Γ_sΛ = J/2 ≠ I` (the false "feasible" an unchecked solver returned in review) | invalid | `equality` |
  | 4 | swap → `I` | `Λ` = swap | `≥ 0`; rows sum to 1; `Γ_sΛ = I` | valid | none |
  | 5 | `J/2 → J/2` | `Λ = [[2, −1], [−1, 2]]` | negative entries; rows sum to 1; `Γ_sΛ = J/2` | invalid | `nonnegative` |
  | 6 | `J/2 → I` | Farkas `y = (−1, 0, 0, 0, 0, 0)` | `Aᵀy = (−1/2, 0, −1/2, 0)`; `bᵀy = −1` | invalid | `ATy_nonnegative` |
  | 7 | `J/2 → J/2` | `Λ = [[1, 1], [0, 0]]` | `≥ 0`; rows sum to 2 and 0; `Γ_sΛ = (1/2, 1/2)` per row `= J/2` | invalid | `row_sums` |
  | 8 | `J/2 → I` | Farkas `y = (−1, 0, 1, 0, 0)`, length 5 | `k² + k = 6` | invalid | `shape` |
  | 9 | swap → `I` | `Λ` with row 0 only, `[0, 1]` | row 1 missing | invalid | `shape` |

  Derivation for case 6. `y` selects constraint row 0, `(a = w_0, j = w_0)`, whose coefficients are
  `Γ_s(w_0, w_i) = 1/2` on `x_{0}` and `x_{2}`. So `Aᵀy` has `−1/2` at `v = 0` and `v = 2`, and `0` elsewhere, and
  `bᵀy = −b_0 = −I(0, 0) = −1`.

  Each clause has a case in which it is the only failure: `bTy_negative` (2), `equality` (3), `nonnegative` (5),
  `ATy_nonnegative` (6), `row_sums` (7) and `shape` (8, 9).
- **EX-SYM (the generator check of §2.7).** The check is applied to frozen candidate generators on CC-TWIN's `φ`
  (`n = 2`, `|S| = 8`). It evaluates `bijective` first; if that fails, nothing else is evaluated. Otherwise it evaluates
  `commutes` and `visible`, and records each one that fails. Hand derivations [D]:

  | # | Candidate `g` (array over `s = 0..7`) | Hand check | Result | Failed clauses |
  |---|---|---|---|---|
  | 1 | `[4, 5, 6, 7, 0, 1, 2, 3]` (`s ↦ s+4`) | commutes (§2.7); adds 4, so `v` is kept | valid | none |
  | 2 | `[1, 3, 0, 2, 5, 7, 4, 6]` (`g = φ`) | commutes with `φ`; `π_V(g(0)) = 1 ≠ 0` | invalid | `visible` |
  | 3 | `[2, 1, 0, 3, 4, 5, 6, 7]` (swap `0 ↔ 2`) | `v` kept (both even); `g(φ(0)) = g(1) = 1`, `φ(g(0)) = φ(2) = 0` | invalid | `commutes` |
  | 4 | `[0, 1, 0, 3, 4, 5, 6, 7]` | `g(0) = g(2)` | invalid | `bijective` |

- **EX-WORD (the primitive-word computation of §2.7).** The tool's word routine is applied to frozen visible words.
  Its expected output is the primitive word (least rotation of the primitive root, compared elementwise as integers)
  and the power. Hand derivations [D]:

  | # | Input word | Case | `primitive_word` | `word_power` |
  |---|---|---|---|---|
  | 1 | `[0, 1, 1, 0]` | rotation | `[0, 0, 1, 1]` | 1 |
  | 2 | `[0, 1, 0, 1]` | power | `[0, 1]` | 2 |
  | 3 | `[1, 1, 0, 1, 1, 0]` | rotation and power: `(110)²` | `[0, 1, 1]` | 2 |
  | 4 | `[1, 1, 0, 0, 1, 1, 0, 0]` | `(1100)²`, same class as case 1 | `[0, 0, 1, 1]` | 2 |
  | 5 | `[0, 0, 0, 1, 1, 1, 0, 1]` | primitive, already least | `[0, 0, 0, 1, 1, 1, 0, 1]` | 1 |
  | 6 | `[1, 0, 0, 1, 0, 0]` | `(100)²` | `[0, 0, 1]` | 2 |
  | 7 | `[3, 3, 3]` | constant | `[3]` | 3 |
  | 8 | `[2]` | single letter | `[2]` | 1 |
  | 9 | `[10, 2]` | numeric, not string, order | `[2, 10]` | 1 |

- For EX-ARITH, EX-SCHEMA, EX-CERT, EX-SYM and EX-WORD, the comparator, validator, checkers and word routine are called
  as units on the frozen inputs. The expected outcome is a compared field and does not exit; a different outcome
  exits 1.
- **Countercontrols built into §3.1.**
  - CC-AGREE2: a non-vacuous FREQ is reachable on a non-transitive map whose two orbits have different primitive words.
  - CC-TWIN: a twin pair is classed as FREQ_VACUOUS, not FREQ.
  - CE-8: NOT is reachable.
  - CC-SHORT: `ℓ_min` excludes short orbits.
  - CC-UNVIS: unvisited rows are excluded, and `Long′ = ∅` is handled.
  - CC-VOID: the void rule takes precedence over equality.
  - CE-8, CC-SHORT, CC-SKEW, CC-PERM and CC-UNVIS together separate every pair of variants.
  - Every variant reaches NOT; CC-S3NOT is the only control in which S3 does.
  - Every variant reaches a non-vacuous FREQ (CC-AGREE2) and FREQ_VACUOUS (TT-4, CC-TWIN).
  - The definitional check on every toy is the countercontrol for Lemma PD (§2.4).
  - CC-ORDER: the frozen `a`-major order of `first_mismatch` is checked on a case where it differs from the `j`-major
    order.
  - M-FRAG: the closure check detects a fragmented decomposition that still partitions `S`.

### 3.4 Recorded cross-checks (OQ-7 = C: RX-ORD is a diagnostic record)

- **RX-ORD.** For N1, N4, N7, N8, N9 and N12 (`gcd(L, q) = 1`), SM Theorem A.1 states `ord(φ) = qL` (SM:1604–1606;
  SM:1610: "Verified computationally for q = 2, 3, 5, 7, 11, 13 and L ≤ 12").
  - The tool records `ord(φ)` and the boolean `ord_phi_eq_qL`.
  - A disagreement does not void C-1. It would be a finding about SM Appendix A or the tool, diagnosed after the run.
  - The fragmentation hazard that motivated making RX-ORD gating is covered by the gating closure check (§2.0) and
    M-FRAG (§3.3).

***

## 4. Decision rule

### 4.1 Per native instance: the four frozen variants

On a native instance everything in this section is computed separately for each readout, from that readout's
per-orbit record. Each variant is a deterministic map from the per-orbit record. A variant is given by its candidate set `C` (the orbits
admitted as `O*`) and its credence `K`:

| Variant | Candidates `C` | Credence `K` | Fields |
|---|---|---|---|
| R0 (the sketch's rule, BSB:406–410) | `Long` | `T^β` (prior over all of `S`) | `verdict`, `first_mismatch` |
| S1 | `Long′` | `T^β` (prior over all of `S`) | `s1_verdict`, `s1_first_mismatch` |
| S2 | `Long` | `T^{β_long}` (prior over `U_Long`) | `s2_verdict`, `s2_first_mismatch` |
| S3 | `Long′` | `T^{β_c4}` (prior over `U_Long′`) | `s3_verdict`, `s3_first_mismatch` |

**The credence pool and `shared_rows` [D].**
- The **pool** of a variant at row `a` is the set of orbits whose counts enter `K(a, ·)`:
  - for R0 and S1, every orbit of `S` that visits `a`, since `K = T^β` pools all of `S`;
  - for S2 and S3, the candidates that visit `a`, since `K = T^{β|C}`.
- `K(a, ·)` is the `n_a`-weighted mixture of the pool's `T^{α,O}(a, ·)`. This follows from the mixture identity of §2.3,
  applied to the pool.
- The twin classes are the word classes of §2.7: orbits with the same primitive cyclic visible word. A class can
  contain orbits of different lengths, for example a word and its square, so a class need not lie wholly inside a
  candidate set. The pool is counted by the distinct classes of its member orbits.
- `shared_rows := #{a ∈ W_C : the orbits in the pool at a belong to at least two twin classes}`, where
  `W_C = ⋃_{O ∈ C} V_O`.
  - For S2 and S3 this is the number of rows visited by candidates from two or more twin classes.
- **Lemma V (vacuity, modulo the word relation).** Suppose `shared_rows = 0`. Then on every row a candidate `O` visits,
  every pooled orbit has `O`'s primitive word. By §2.7 it therefore has the same row `T^{α,O}(a, ·)`. So
  `K(a, ·) = T^{α,O}(a, ·)` there, and every candidate matches by construction. Consequently:
  - FREQ with `shared_rows = 0` carries no information;
  - NOT with `shared_rows = 0` is impossible.
- **Lemma V′ (for S2 and S3) [D].** Under S2 and S3, FREQ holds iff, on every row, all candidates that visit that row
  have identical `T^{α,O}(a, ·)`. So S2 and S3 test whether the candidate orbits agree with one another.
  - (⇐) If they agree, every positive-weight mixture of the identical rows equals each of them.
  - (⇒) Suppose two candidates differ on a row. A positive-weight mixture of distinct vectors cannot equal every one
    of them, so at least one candidate mismatches.

**The rule.** For each variant, with its `C` and `K`:
1. If `C = ∅`, the verdict is `VOID_NO_ORBIT`.
2. Otherwise, if `T^{α,O}` equals `K` on `V_O × 𝒞_V` for every `O ∈ C`:
   - the verdict is `FREQ` if `shared_rows ≥ 1`;
   - the verdict is `FREQ_VACUOUS` if `shared_rows = 0`.
3. Otherwise the verdict is `NOT`. The first mismatch reported is the least-`rep` failing orbit's first mismatch
   against `K`. A `NOT` with `shared_rows = 0` contradicts Lemma V and exits 4.

All four verdicts, and each variant's `shared_rows`, are computed and recorded on every instance.

Also recorded with every instance:
- `|Long|` and `|Long′|`;
- the number of orbits in `C` that match `K`, for each variant;
- the orbit-length histogram and `ord(φ)`;
- `#{O ∈ Long : pdiv_alpha(O)}`, `pdiv_beta` and `diameter_ge_4`.

The P-divisibility counts are descriptive and carry no verdict.

### 4.2 Overall verdicts, and the OQ-13 selection rule

**Aggregation (OQ-8 = A).** The same map is applied separately to each variant and each readout. For a variant and a
readout, let `Ev` be the set of native instances whose verdict under that variant and readout is FREQ or NOT.
FREQ_VACUOUS and VOID_NO_ORBIT instances are excluded from `Ev` and listed separately. The variant's overall verdict is:
- `FREQ_ALL` if `Ev ≠ ∅` and every instance in `Ev` is FREQ;
- `NOT_ALL` if `Ev ≠ ∅` and every instance in `Ev` is NOT;
- `MIXED` if `Ev` contains both;
- `VACUOUS_ALL` if `Ev = ∅` and at least one instance is FREQ_VACUOUS;
- `VOID_ALL` if every instance is VOID_NO_ORBIT.

These five cases are exhaustive and mutually exclusive.

Every native instance enters each readout's aggregation, W-q2-L7-r2 (N12) included, and counts wherever it is
non-void (OQ-4 = B). These are recorded per readout as `c1_r0_verdict_pc`, `c1_s1_verdict_pc`, `c1_s2_verdict_pc`,
`c1_s3_verdict_pc`, and the same four with suffix `_cur`.

**The selection rule.** OQ-13 has two parts:
- (i) which orbits are the candidates for `O*`: the long orbits, or the long orbits that carry history readback;
- (ii) whether the credence prior ranges over all orbits or over the candidate orbits only.

Its answer is recorded as the constant `oq13_answer` in `C1-INSTANCES.json`: **`13b`** (owner ruling, #1059
c.6650820790). One answer applies to both readouts. For each readout, the C-1 verdict (`c1_verdict_pc`,
`c1_verdict_cur`) is the overall verdict of the variant this table assigns to that answer:

| `oq13_answer` | (i) candidates | (ii) prior support | Selected variant | `c1_verdict_<readout>` = |
|---|---|---|---|---|
| `13a` | long orbits (`Long`) | all orbits | R0 | `c1_r0_verdict_<readout>` |
| `13b` | long C4-bearing orbits (`Long′`) | all orbits | S1 | `c1_s1_verdict_<readout>` |
| `13c` | long orbits (`Long`) | the candidates only | S2 | `c1_s2_verdict_<readout>` |
| `13d` | long C4-bearing orbits (`Long′`) | the candidates only | S3 | `c1_s3_verdict_<readout>` |

With the recorded answer, the selected variant is S1: `Long′` compared against the global-prior `T^β`. The owner's
reason: it "directly tests the relation between the representation's numerical probabilities and the actual-orbit
frequencies, without changing the prior to make the comparison easier" (#1059 c.6650820790).

- The table covers every combination of the two binary choices, so it has no gaps on its option space.
- An answer outside it, such as a different candidate predicate or a different prior support, is written into the text
  as a new frozen variant and a new table row before the review that precedes `F` (§7).
- If `oq13_answer` is not one of the four codes at run time, the tool exits 2 before any instance.
- The three variants not selected (R0, S2, S3) are diagnostic comparisons. They are recorded and do not qualify the C-1
  verdicts.
- There is no combined verdict across readouts. Each readout's C-1 verdict is stated for that readout only.

### 4.3 Run validity

- **The job's steps.** Three steps bear on validity:
  - (a) the check step, which is the tool, exiting 0–5 or 7;
  - (b) the re-application step, exiting 0 or 6;
  - (c) the verdict-text step, exiting 0 or 8.
- **The run is complete** iff all three of the following hold.
  - **Step (a) exits 0.** This requires:
    - every control and mutation matches its frozen expected values (§3);
    - every invariant of §2 and §4.1 holds on every instance:
      - the budget, injectivity and agreement of the two implementations of `φ`;
      - the mixture identity and double stochasticity, under each readout;
      - the orbit closure check and the partition `Σ_O |O| = |S|` (§2.0);
      - agreement of the two P-divisibility methods, and every certificate verifying under (i)–(iv);
      - every frozen symmetry generator passing `bijective`, `commutes` and `visible` (§2.7);
      - no NOT with `shared_rows = 0`;
    - the frozen-input check passes, and `oq13_answer` is valid;
    - every output validates against `C1-OUTPUT-SCHEMA.json`.
  - **Step (b) exits 0.** The step recomputes, from the orbits files and `T_beta`, for each readout:
    - every `eq`, `long_c4`, `eq_beta_long`, `eq_beta_c4`, `T_beta_long` and `T_beta_c4`, and each variant's
      `shared_rows`, every `primitive_word`, `word_power` and `class_rep`, and the word classes;
    - each instance's four verdicts and the four overall verdicts;
    - `c1_verdict_pc` and `c1_verdict_cur`, from `oq13_answer` and the table of §4.2;
    - every `orbits_sha256`.

    It compares them with the stored values, and any difference exits 6.
  - **Step (c) exits 0.** It regenerates `verdict_text` from `summary.json` and compares the two byte for byte. A
    difference exits 8.
- **Otherwise the run halts at the first failure.**
  - `summary.json` then has `run_status = HALT`, and every `c1_*_verdict_pc` and `c1_*_verdict_cur` is `null`. A halt
    under either readout halts the whole run (OQ-2 = C).
  - The `native_*_verdicts_pc` and `native_*_verdicts_cur` maps are empty whenever `run_status = HALT`.
  - A native instance's file written before a halt carries no verdict of the run.
  - A failure in step (b) or (c) is read from that step's exit status and conclusion. `summary.json` is written by step
    (a) and does not record it.
- Under §A.29, a halted run establishes nothing about the wave substratum. There is no partial verdict, no rerun within
  a freeze other than the OQ-14 dispatch below, and no amendment after `F`.
- **A runner failure before step (a) starts (OQ-14 = B).** One additional dispatch on `F` is admissible only if both
  hold:
  - **a qualifying pre-step failure.** The host's API job record of the failed dispatch shows the step entry for step
    (a) either absent, or with `started_at` null and conclusion `skipped` or null. It is read from the API, never from
    logs. **These field semantics are to be verified against a real job record before `F`**, and the predicate frozen
    at `F` names the fields as the host actually returns them;
  - **new explicit owner approval** of that dispatch, recorded with the failed run's id.

  The API predicate is necessary, not sufficient. It does not separate a host infrastructure failure from a failure of
  the workflow's own pre-step code, such as a setup error; whether the failure is an infrastructure failure is judged
  by the owner in that approval. If the verification of the field semantics before `F` identifies fields that make the
  separation, the predicate frozen at `F` uses them [D].

  No other rerun is admissible. The run-validity invariant is "the check step ran in exactly one attempt": across the
  API job records of every dispatch on `F`, exactly one must show step (a) started (§6).
- **PASS (the result reviewer's test).** All five of these hold:
  - the host's conclusion for the C-1 job is `success`, read from its API;
  - step (a) exits 0;
  - step (b) exits 0;
  - step (c) exits 0;
  - `summary.json` has `run_status = COMPLETE`.

  Only under PASS are `summary.json`'s `c1_verdict_pc` and `c1_verdict_cur` read as the result, each for its readout.
  The other three variants' overall verdicts are recorded with them.

***

## 5. Outputs (§A.44)

**The schema.**
- `C1-OUTPUT-SCHEMA.json` (JSON Schema draft 2020-12) is frozen and authoritative for every output file; the tables
  below transcribe it.
- The format `c1-reduced-rational` is asserted. A string satisfies it iff it matches
  `^-?(0|[1-9][0-9]*)(/[1-9][0-9]*)?$`, is not `-0`, and, when a denominator is present, has a denominator that is at
  least 2 and coprime to the numerator. Probabilities additionally match the unsigned pattern.
- At start, the tool validates `C1-CONTROLS-EXPECTED.json` against `#/$defs/expected_file`, and exits 2 if it fails.
  That schema has a `required` list for every control. Every expected field is therefore a schema field, and a missing
  expected key fails validation instead of silently dropping a check.

**Output root.** Every output is written under `c1/` at the root of the job's checkout. The directory is uploaded as
one workflow artifact named `bornsel-c1`.

| File | Schema (`$defs`) | Contents |
|---|---|---|
| `c1/<id>.json`, toy control | `toy_record` | the analysis fields below, plus `pdiv_beta_definitional`, `pdiv_certs_file`, `pdiv_certs_sha256`, `pdiv_certs_verified`, `sketch_check` (CE-8 only; `null` elsewhere), `expected`, `comparisons` and `match` |
| `c1/<id>.json`, native instance | `native_record` | `params` (instance parameters), `injective`, `closure_ok`, `phi_impls_agree`, `phi_zero_fixed`, `ord_phi_eq_qL` (`null` outside RX-ORD), `diameter_ge_4` (a secondary diagnostic), and `readouts`: `{pc, cur}`, each a `readout_analysis` object carrying the analysis fields below for that readout; the schema binds each object's `params.readout` to its key and its `orbits_file` to that readout's `.pc` or `.cur` suffix |
| `c1/<id>.json`, unit control or mutation | `unit_record` | `params` (M-INJ, WF); `phi_impls_agree` (M-INJ, WF); `injective` and `evaluated_beyond_injectivity` (M-INJ); `closure_ok`, `partition_ok` and `evaluated_beyond_closure` (M-FRAG); `results` and `reduced` (EX-ARITH); `schema_results` (EX-SCHEMA); `cert_results` and `cert_failed_clauses` (EX-CERT); `sym_results` and `sym_failed_clauses` (EX-SYM); `word_results` (EX-WORD, items `{primitive_word, word_power}`); `hand_steps` (WF-q2-L5, WF-q3-L4, WF-q2-L6-r2 and WF-CUR, items `{step, prev, cur, state, visible}`, the visible value under the control's readout); `sigma_check` (WF-SIGMA: `{x, sigma_x, phi_x, sigma_phi_x, phi_sigma_x, visible_x, visible_sigma_x, visible_phi_x, visible_sigma_phi_x}`); `phi_of_zero` (WF-0); `expected`, `comparisons`, `match` |
| `c1/<id>.orbits.jsonl` (toys) and `c1/<id>.<readout>.orbits.jsonl` (natives, one per readout) | `orbit_record`, one per line | `rep`, `class_rep`, `primitive_word`, `word_power`, `length`, `cycle`, `visited_rows`, `unvisited_rows`, `n_a`, `T_alpha`, `long`, `eq`, `first_mismatch`, `pdiv_alpha`, `pdiv_witness`, `long_c4`, `eq_beta_long`, `first_mismatch_beta_long`, `eq_beta_c4`, `first_mismatch_beta_c4`, `pdiv_alpha_definitional` (`null` on natives) |
| `c1/<id>.pdiv-certs.json`, toys | `pdiv_certs` | `schema`, `id`, `entries`: `{family, rep, rows, pair, kind, lambda, farkas_y}` |
| `c1/summary.json` | `summary` | `schema`, `oq13_answer`, `selected_variant`, `controls_frozen` (25), `controls_matched`, `natives_frozen` (12), `natives_evaluated`; for each readout `<r>` in `pc`, `cur`: `native_verdicts_<r>` (R0), `native_s1_verdicts_<r>`, `native_s2_verdicts_<r>`, `native_s3_verdicts_<r>`, `c1_verdict_<r>`, `c1_r0_verdict_<r>`, `c1_s1_verdict_<r>`, `c1_s2_verdict_<r>`, `c1_s3_verdict_<r>`; then `run_status`, `first_failure`, `verdict_text` |

On a halt, `oq13_answer` and `selected_variant` may be `null`, which covers the exit-2 halt on an unset answer. On a
complete run both must be set; the schema enforces this through a conditional on `run_status`.

**Analysis fields** (toy records, and each readout object of a native record):
- `params` (on a native readout object it also carries `readout`, `pc` or `cur`, and that readout's `n` and `m`);
- `injective`;
- `ell_min`, `ell_min_rule` (`"n+1"`);
- `orbit_count`, `orbit_length_histogram`, `ord_phi`;
- `T_beta`;
- `doubly_stochastic`, `mixture_identity`;
- `beta_is_permutation`, `pdiv_beta`, `pdiv_beta_horizon`;
- `long_orbit_count`, `long_orbits_equal`, `long_orbits_pdiv_alpha`, `first_mismatch`, `shared_rows`, `verdict` (R0);
- `s1_long_count`, `s1_long_equal`, `s1_first_mismatch`, `s1_shared_rows`, `s1_verdict`;
- `T_beta_long`, `s2_long_equal`, `s2_first_mismatch`, `s2_shared_rows`, `s2_verdict`;
- `T_beta_c4`, `s3_long_equal`, `s3_first_mismatch`, `s3_shared_rows`, `s3_verdict`;
- `symmetry_generators_ok`, `group_cross_check_ok`, `orbit_class_count`;

Each verdict field takes one of `FREQ`, `FREQ_VACUOUS`, `NOT` and `VOID_NO_ORBIT`. Each overall verdict takes one of
`FREQ_ALL`, `NOT_ALL`, `MIXED`, `VACUOUS_ALL` and `VOID_ALL`, or `null` on a halt.
- `orbits_file`, `orbits_sha256`.

Every record also carries the common fields `schema`, `id`, `order`, `kind`, `frozen_inputs` and `run`.

**Canonical orbits file.** The file is UTF-8, with one JSON object per line. Keys are sorted, there is no insignificant
whitespace, lines are in increasing `rep`, and each line ends with `\n`. `orbits_sha256` is the SHA-256 of these bytes.

**Comparison rules (controls).**
- The compared fields of a control are exactly the keys of its object in `C1-CONTROLS-EXPECTED.json`. That key set is
  fixed by the schema's `required` lists. A key missing from the computed record is a mismatch. Computed fields that are
  not expected are recorded and not compared.
- **Scalars.** Booleans, integers, `null` and strings must be equal and of the same JSON type. Probability strings are
  compared as strings, which is exact because the format admits one reduced form per rational.
- **Objects.** The key sets are equal, and the values are equal under these rules.
- **Arrays.** The lengths are equal, and the elements are equal in order. The orders are fixed:
  - `visited_rows` and `unvisited_rows` are ascending;
  - `cycle` starts at `rep` and follows `φ`;
  - case lists follow the frozen case order;
  - each `cert_failed_clauses` entry lists its clauses in the order `shape`, `nonnegative`, `row_sums`, `equality`,
    `ATy_nonnegative`, `bTy_negative`.
- **`orbits`.** The expected key `orbits` is compared with the orbits file, read as an array of its lines in file order.
  Each element must have the expected element's exact key set.

**Verdict text.** It is rendered from the summary fields only. On a COMPLETE run it has two paragraphs, `pc` then
`cur`, each rendered from that readout's fields with the templates below and introduced by "Readout <r>:". There is
no combined sentence across readouts.
- **Layout [D].** Each paragraph is the string `Readout <r>: ` (one space after the colon) followed by the rendered
  template, with no line break inside it. The two paragraphs are joined by exactly two line feeds (`\n\n`).
  `verdict_text` has no leading or trailing whitespace and no final line feed. On a halted run it is the one rendered
  halt sentence, with no prefix.
- **Placeholders.**
  - `<k>` is `controls_frozen` (25).
  - `<ids>` is a comma-separated list in run order, or `none`.
  - `<r>` is the paragraph's readout (`pc` or `cur`); `<V>` is `selected_variant`, and `<A>` is `oq13_answer`. The
    `<ids>` lists, `<P>`, `<N>` and `<X>` refer to that readout's verdicts.
  - `<P>` is the frozen phrase of the selected variant:
    - R0: "T^{α,O} = T^β on visited rows for every orbit with |O| ≥ ℓ_min";
    - S1: "T^{α,O} = T^β on visited rows for every orbit with |O| ≥ ℓ_min whose T^{α,O} is not a permutation matrix";
    - S2: "T^{α,O} = T^{β_long} on visited rows for every orbit with |O| ≥ ℓ_min";
    - S3: "T^{α,O} = T^{β_c4} on visited rows for every orbit with |O| ≥ ℓ_min whose T^{α,O} is not a permutation
      matrix".
  - `<N>` is the negation of `<P>`: "for some candidate orbit, T^{α,O} differs from the variant's credence on a visited
    row".
  - `<R>` is "Recorded: R0 <c1_r0_verdict_r>; S1 <c1_s1_verdict_r>; S2 <c1_s2_verdict_r>; S3 <c1_s3_verdict_r>.", with
    `_r` the paragraph's readout.
  - `<X>` is "Vacuous instances (every candidate matched by construction, shared_rows = 0): <ids>. Void instances:
    <ids>."
- **COMPLETE runs.**
  - FREQ_ALL: "C-1 (readout <r>, variant <V>, OQ-13 answer <A>): all <k> controls matched. On every native instance with a
    non-vacuous verdict (<ids>), <P>. <X> <R>"
  - NOT_ALL: "C-1 (readout <r>, variant <V>, OQ-13 answer <A>): all <k> controls matched. On every native instance with a
    non-vacuous verdict (<ids>), <N>. <X> <R>"
  - MIXED: "C-1 (readout <r>, variant <V>, OQ-13 answer <A>): all <k> controls matched. FREQ on <ids>; NOT on <ids>. <X> <R>"
  - VACUOUS_ALL: "C-1 (readout <r>, variant <V>, OQ-13 answer <A>): all <k> controls matched. No native instance has a non-vacuous
    verdict under variant <V>: every candidate matched only by construction, or there was no candidate. The C-1 verdict
    carries no information. <X> <R>"
  - VOID_ALL: "C-1 (readout <r>, variant <V>, OQ-13 answer <A>): all <k> controls matched. No native instance has a candidate orbit
    under variant <V>; the C-1 verdict is void. <R>"
- **Halted runs** (the run is void in every case).
  - Exit 1: "C-1 halted at <id>: <field> expected <expected>, computed <computed>. The run is void."
  - Exit 2: "C-1 halted at <id or 'start'>: schema violation in <field>. The run is void."
  - Exit 3: "C-1 halted at start: frozen input <detail> does not match its git blob id at F. The run is void."
  - Exit 4: "C-1 halted at <id>: invariant <detail> failed. The run is void."
  - Exit 5: "C-1 halted at <id>: φ is not injective. The run is void."
  - Exit 7: "C-1 halted at <id>: state count exceeds 2^16. The run is void."
  - Any other exit: "C-1 halted with exit <exit>. The run is void."

**Exit status.**

| Code | Step | Meaning |
|---|---|---|
| 0 | (a), (b), (c) | complete |
| 1 | (a) | a control, mutation or WF value mismatch |
| 2 | (a) | a schema violation, in an output or in the expected file against `expected_file`; a frozen parameter inconsistent with §2.2's formulas (either readout) or with Theorem 22's region conditions; an invalid `oq13_answer`; or a floating-point value in a probability field |
| 3 | (a) | a frozen input does not match its git blob id at `F`, or `F` is not in the checkout |
| 4 | (a) | an invariant failure: the `φ` implementations disagree; the mixture identity or double stochasticity fails under either readout; a recorded orbit is not a closed `φ`-cycle, or the orbits do not partition `S` (§2.0); the two P-divisibility methods disagree; a certificate or its coverage fails; a NOT has `shared_rows = 0` (Lemma V); a frozen symmetry generator fails `bijective`, `commutes` or `visible`; or a generator maps an orbit to one with a different primitive word (§2.7) |
| 5 | (a) | `φ` is not injective on a toy or native instance |
| 6 | (b) | the re-application step found a stored field that differs from its recomputation |
| 7 | (a) | `state_count > 2¹⁶` |
| 8 | (c) | the regenerated `verdict_text` differs from the stored one |
| other nonzero | any | error |

**Where the verdict is read from.** It is read from the exit statuses of steps (a), (b) and (c), from the host's job and
step conclusions (via its API), and from `summary.json`. Never from log text.

***

## 6. Invariant → checkpoint (§A.41)

| Invariant asserted in this file | Checkpoint |
|---|---|
| exact rationals; no floating point in the verdict path | EX-ARITH and EX-SCHEMA (compared); the schema's `c1-reduced-rational` format on every probability field (exit 2); the tool review (§7 step 6) checks that the comparison and verdict path use integer arithmetic only |
| every expected field is a schema field, and no expected key is missing | `C1-CONTROLS-EXPECTED.json` is validated against `#/$defs/expected_file`, with its `required` lists, at start (exit 2) |
| every output has the frozen schema | each output is validated against `C1-OUTPUT-SCHEMA.json` before it is written (exit 2) |
| the four frozen inputs exist at `F` and are unchanged | at start, the git blob ids at `F` are compared with the loaded bytes (exit 3); `frozen_inputs` appears in every output |
| `F` is the reviewed constant, present in the checkout | `F` is fixed in the reviewed workflow; its absence exits 3; `run.F` appears in every output |
| no frozen item awaits an answer at `F` | `oq13_answer` must be one of `13a`–`13d` (exit 2), and is frozen as `13b`; the review of the revised text (§7 step 3) checks that §8.2 records every answer and carries no open item |
| the C-1 verdict is the variant the OQ-13 answer selects, per readout | step (b) recomputes `c1_verdict_pc` and `c1_verdict_cur` from `oq13_answer` and the §4.2 table (exit 6); `selected_variant` is recorded |
| both readouts are evaluated on the same orbits, under shared controls and one halt; no combined verdict | every native record carries `readouts.pc` and `readouts.cur`, each with its own `params.readout` and orbits-file suffix (schema, exit 2); the controls run once before any native instance (§3); `summary.json` has per-readout fields only (schema) |
| the `cur` projection is the §2.1 formula | WF-CUR (compared); the two readouts' frozen `n`, `m` and `ℓ_min` are checked against §2.2's formulas (exit 2) |
| the `r = 2` `pc` projection is the §2.1 formula | WF-q2-L6-r2 (compared) |
| the recorded orbits are exactly the cycles of `φ` | the closure and partition checks on every toy and native instance (exit 4); M-FRAG detects a fragmented decomposition that still partitions `S` (`closure_ok`, `partition_ok`, `evaluated_beyond_closure` compared) |
| `first_mismatch` is the `a`-major least `(a, j)` | `first_mismatch` and `s1_first_mismatch` compared on CC-ORDER, where the `a`-major and `j`-major orders differ, and on every other toy |
| budget (§A.40) | `state_count ≤ 2¹⁶` before enumeration (exit 7); the job's `timeout-minutes`, with its conclusion read from the host |
| frozen parameters satisfy §2.2 (`pc`: `n = q^{2r}`, `m = q^{2(L−r)}`; `cur`: `n = q^r`, `m = q^{2L−r}`; `ℓ_min = n+1` per readout; `r ≤ L/3`; `R` contiguous) | checked from `C1-INSTANCES.json` before enumeration (exit 2) |
| `φ` is a bijection on every toy and native instance | the injectivity check (exit 5); `injective` is recorded |
| the bijectivity check detects a non-bijection | M-INJ, with `injective = false` compared; exit 1 if it is not detected |
| the implemented `φ` is the §2.1 rule | WF-q3-L4, WF-q2-L5, WF-q2-L6-r2 and WF-CUR (compared); the two implementations agree on all of `S` for every native instance (exit 4). WF-0 is a sanity check only |
| `T^β` is Main:117's matrix | the mixture identity and double stochasticity (exit 4); `T_beta` compared on every toy control |
| `T^{α,O}` on visited rows only; unvisited rows excluded and recorded | CC-UNVIS (compared, including `unvisited_rows`); `unvisited_rows` recorded per orbit |
| `ℓ_min = n + 1`, inclusive, fixed by parameters, per readout | `ell_min` compared on every toy and checked against the formula on every native instance and readout (exit 2); CC-UNVIS exercises `|O| = ℓ_min`, and CC-SHORT exercises exclusion |
| the void rule takes precedence | CC-VOID (compared) |
| the frozen symmetry generators are valid, and the implemented `σ` is the §2.7 reflection | the generator check and the word cross-check on every instance (exit 4); `symmetry_generators_ok` and `group_cross_check_ok` recorded; EX-SYM has a case for each clause (`sym_failed_clauses` compared); WF-SIGMA compares `σ` and `φσ = σφ` with hand values on N7's parameters |
| twin orbits (same primitive cyclic visible word) are not counted as independent agreement | `primitive_word`, `word_power`, `class_rep` and `orbit_class_count` compared on every toy; EX-WORD checks the primitive-word routine on rotation, power, combined, numeric-order and single-letter cases; CC-TWIN (twins, FREQ_VACUOUS), CE-8, CC-UNVIS and CC-PERM (power words) compared; step (b) recomputes the words and classes (exit 6) |
| FREQ (non-vacuous) and NOT are both reachable under every variant | CC-AGREE2 (FREQ under all four, with two distinct primitive words); CE-8, CC-PERM and CC-S3NOT (NOT under each variant, with CC-S3NOT the only S3 NOT); see the §3.1 outcome table |
| a FREQ that holds by construction is not reported as FREQ | `shared_rows` and `s1_shared_rows`, `s2_shared_rows`, `s3_shared_rows` compared on every toy; FREQ_VACUOUS reached under every variant (TT-4) and separated from FREQ (CC-SHORT under S2 and S3); step (b) recomputes them (exit 6); a NOT with `shared_rows = 0` exits 4 |
| A2: a transitive map gives equality, by construction | TT-4 and TT-6 (compared; FREQ_VACUOUS) |
| CE-8 gives `3/4` against `{1, 1/2}`; α on `O_A` is divisible; β is indivisible | `sketch_check`, `T_beta`, `orbits` (`T_alpha`, `pdiv_alpha`) and `pdiv_beta` compared on CE-8 |
| the four variants are computed as frozen, and each pair is separated | CE-8, CC-SHORT, CC-SKEW, CC-PERM, CC-UNVIS and CC-S3NOT (§3.1); every `s1_*`, `s2_*`, `s3_*`, `T_beta_long` and `T_beta_c4` field, and every per-orbit `long_c4`, `eq_beta_long`, `first_mismatch_beta_long`, `eq_beta_c4` and `first_mismatch_beta_c4`, compared on every toy |
| the permutation-matrix test is as frozen | `beta_is_permutation`, `pdiv_alpha` and `long_c4` compared on every toy, including the partial row set of CC-UNVIS |
| Lemma PD agrees with the definition | the definitional check on every toy, compared with the Lemma PD value and the expected value; exit 4 on disagreement |
| definitional results are certified; the checker rebuilds `A` and `b`, checks shapes and evaluates every clause | every certificate is verified under (i)–(iv) (exit 4); `pdiv_certs_verified` is compared; EX-CERT has a case in which each clause is the only failure (`cert_failed_clauses` compared) |
| the verdicts are deterministic functions of the per-orbit record | step (b) recomputes them from the orbits files (exit 6) |
| per-orbit records are those the summary describes | `orbits_sha256` is recomputed in step (b) (exit 6) |
| no native verdict over a failed control | controls run first; the run halts on the first mismatch; `natives_evaluated` is empty whenever `first_failure` is a control |
| frozen order; no adaptive extension | `order` is compared with `C1-INSTANCES.json`; `natives_evaluated` is a prefix of the frozen order |
| the check step ran in exactly one attempt (OQ-14 = B) | the result reviewer reads the API job records of every dispatch on `F`: exactly one shows step (a) started; any second dispatch has a recorded owner approval citing a failed run whose record satisfies the §4.3 pre-step predicate, with the owner's approval judging that the failure is an infrastructure failure. The predicate's field semantics are verified against a real job record before `F` |
| PASS combines five signals | the job emits the exit statuses of steps (a), (b) and (c), and `summary.json`; the result reviewer reads the job conclusion from the host's API (§4.3) |
| verdict text is generated only from structured output | step (c) regenerates `verdict_text` from `summary.json` and compares it byte for byte (exit 8) |

***

## 7. Execution boundary and governance

- **CI only (§A.40).** Locally, only cheap static checks of the tool may run. The instance set runs only in CI.
- **One pass**, halting on the first red. A void run is not repaired by re-running. The only exception is OQ-14's: one
  further dispatch after a qualifying pre-step infrastructure failure and new explicit owner approval (§4.3).
- **Order of steps.**
  1. **Owner answers.** Done: #1059 c.6650820790 (amaybaum, 2026-11-05), recorded in §8.2.
  2. **Revision.** The text and the data files are revised to carry the answers. Each answer is written in place as the
     frozen choice: `oq13_answer` is set in `C1-INSTANCES.json`, and any instance, control or exit code an answer adds
     or removes is written in. §8.2 is replaced by a record of the answers, quoted with author and time (§A.42 item 7).
     This is done in r7, and no item remains open. The review of r7 (#1082 c.6651181144) required changes C1–C10;
     r8 applied them. The recheck of r8 (#1082 c.6651778560) required R1–R10; r9 applies them. The independent r9
     delta check (#1082 c.6651925573, model-authored) is ACCEPT; it does not designate `F` or resolve the pre-`F` items.
  3. **Review.** An independent reviewer reviews the exact revised commit carrying the four frozen files. The review
     covers their agreement with each other, with the answers and with BSB:402–416, and the hand derivations of §3. If
     the review requires changes, steps 2 and 3 repeat.
  4. **Freeze.** The owner designates that reviewed commit as `F`. No text after `F` changes, and nothing in it awaits
     an answer.
  5. **Owner go.** The owner gives the go on `F`. The go authorizes writing the tool; it does not amend `F`.
  6. **Tool.** Only then does the designated writer write the tool, the certificate checker and the workflow, on a
     disposable research branch. The workflow carries `F` as a constant.
  7. **Tool review.** An independent reviewer reviews the tool, the checker and the workflow at their exact commit,
     including `F`'s value, before any dispatch. The push-triggered workflows are inspected before any push (§A.43
     item 4).
  8. **Dispatch approval.** Dispatch is a separate owner approval (§A.43). Any `workflow_dispatch` launch is a special
     launch.
  9. **Result review.** The independent reviewer applies the five-signal PASS of §4.3, using the host's API record.
- **Governance form (OQ-12 = A): the research-run lifecycle.**
  - This run is not a §A.39 native V3 round. It carries no `v3-round` or `v3-governed-paths` block and has no receipt,
    and it is not protocol-valid under §A.39.
  - It "cannot independently support a correctness-band or status promotion" (owner ruling, OQ-12). It changes no
    status, label or classification by itself.
  - Any later V3 use needs separate authorization.
- **Budget (an estimate, not measured).** The largest instances have `2¹⁶` states. The work per instance is:
  - two computations of `φ`, each `O(L·|S|)`;
  - a cycle decomposition with its closure check, `O(|S|)`;
  - the counts, `O(|S|)` per readout;
  - the comparisons, `O(n²)` per orbit for each variant and readout.

  P-divisibility uses Lemma PD on native instances, so no linear program runs there. The certified method runs on toys
  only, with `k ≤ 3`. Minutes are expected. The job timeout is 30 minutes; a timeout is red, and there is no extension.
- **Evidence (§A.42).**
  - The result note states the commit, the command, `summary.json` (small, with its digest), and the owner's answers,
    designations and approvals, quoted with author and time (§A.42 item 7).
  - The tool, the checker and the workflow land on `main` with the result note, so that the command can be rerun from
    `main` (§A.42 item 1).
  - Before the result is an enduring claim, `F` and the run commit must be reachable from `main` (§A.42 items 1, 2 and
    8). A verdict that depends on those commits uses them, and copying their files to `main` does not make them
    reachable. The result note lands with the branch that contains them. That landing is a merge, which needs
    separate owner authorization; no ruling authorizes it.
  - The per-orbit and certificate files can be regenerated by the command and need not land on `main`.
  - A run on a disposable branch is provenance only until its record lands on `main`.
- **Exclusions.** No C-2, no C-3, no Lean, no manuscript edit, no status change, no merge or publication.

***

## 8. Owner answers (record)

### 8.1 Status at this revision

Every OQ is answered (§7 step 1). This section records the answers. No item of this text awaits an answer; the
revised commit awaits independent review (§7 step 3).

### 8.2 The owner's rulings on OQ-1 to OQ-15

Recorded on #1059 c.6650820790: "Owner rulings on BORN-SEL (b) (amaybaum, 2026-11-05, given to the coordinating
session and recorded here)", posted 2026-11-05T05:49:40Z. Basis: the reviewed decision table `OQ-DECISIONS.md` r6
(`9364fdcb`; review #1082 c.6650140256). The objective is quoted in §1. Each row quotes the ruling and its conditions,
and says where this text carries it.

| OQ | Ruling (quoted) | Conditions (quoted) | Where carried |
|---|---|---|---|
| 1 | A | "`ℓ_min = n + 1`, as an explicitly selected test criterion, not a physical threshold derived from OI" | §2.5 |
| 2 | C | "Both `(prev, cur)` and `cur`; one selected variant; independent per-readout verdicts; shared controls; one halt" | §2.1, §2.2, §3, §4.2, §4.3, §5, WF-CUR |
| 3 | A | "`a = 1`; keep the odd-length `q = 3` limitation" | §2.1, §9 |
| 4 | B | "Include W-q2-L7-r2; count every non-void instance; N10/N11 a secondary diagnostic only" | §2.2, §4.2 |
| 5 | A | "Visited roots `V_O` only" | §2.4 |
| 6 | A | "Record β's P-divisibility; the redundant field is not an independent scientific result" | §2.4, §9 |
| 7 | C | "Gating closure check and the M-FRAG mutation; RX-ORD a diagnostic record" | §2.0, §3.3, §3.4, §4.3 |
| 8 | A | "The stated aggregation, separately per readout" | §4.2 |
| 9 | A | "Lemma PD, keeping its toy countercontrol" | §2.4 |
| 10 | C | "The required controls, including the `r = 2` and `cur` projections and M-FRAG, **plus the optional `n = 3` first-mismatch diagnostic toy**. Expected total 25 rather than 24. CC-S4 is not required under OQ-13 = 13b. Update all counts, expectations and schema constraints, and independently review the added diagnostic before any freeze." | §3 (25 controls: CC-ORDER, M-FRAG, WF-q2-L6-r2, WF-CUR added), the JSON files |
| 11 | A | "Keep QB-1 and QB-2, including the cycle-horizon limitation and the frequency/credence distinction" | §1, §2.6, §9 |
| 12 | A | "Research-run lifecycle. It cannot independently support a correctness-band or status promotion; any later V3 use needs separate authorization" | §7 |
| 13 | **13b** | "S1: candidates `Long′`, compared against the global-prior `T^β`. R0, S2 and S3 are diagnostic comparisons" | §1, §4.2, `oq13_answer` |
| 14 | B | "One additional dispatch only after a qualifying pre-step infrastructure failure **and** new explicit owner approval. Verify the API-field semantics before any freeze" | §4.3, §6, §7 |
| 15 | A | "Intrinsic visible-word twin classes, with the group cross-check" | §2.7 |

- **The OQ-10 diagnostic toy.** The "optional `n = 3` first-mismatch diagnostic toy" is the item r6 recorded in this
  section as an unadded reviewer suggestion: "add an `n = 3` toy that discriminates the order of `first_mismatch` (not
  added)". r6 gave its purpose but no map. r7 constructs it as CC-ORDER (§3.1). It is not the S1/S4 witness toy that
  the review c.6649892041 (F5) dropped from `OQ-DECISIONS.md`.
- **The question texts and the reviewers' recommendations** that this section held at r6 are in `PREREG-C1.md` at
  `cde5ecbc` and, with the options and recommended answers, in `OQ-DECISIONS.md` r6 (`9364fdcb`).

### 8.3 Points in the source sketch that cannot be frozen as stated

These are the points of BSB:404–416 that needed a choice, with the choice this draft makes.

1. **"`ℓ_min` fixed in advance."** No source fixes a value, and Main:62's "small p" is unquantified. The draft uses
   `n + 1` (§2.5, OQ-1). The sketch's rule is also one-sided: it restricts the candidates but not the credence. The
   draft therefore freezes four variants; the OQ-13 answer `13b` selects S1.
2. **"A declared region R" and "small L".** The sketch fixes neither the visible content of a site nor the sizes. At
   `d = 1`, `L ≥ 3` is needed for distinct neighbours, and Theorem 22's hypotheses fit the budget only at `L = 8`. The
   choices are in §2.1–§2.2 (OQ-2 = C: both readouts; OQ-4 = B).
3. **The B4 record "per orbit".** Γ^α is undefined on unvisited roots, so a row set must be chosen; the draft uses `V_O`
   (OQ-5). By Lemma PD the record is a function of the comparison data and adds no independent information.
4. **"β indivisible" in the CE-8 control.** No horizon is given. The draft uses `{0, …, ord(φ)}`, which is
   `{0, …, 4}` for CE-8.
5. **"An exact-arithmetic check."** As written it has no expected value. The draft makes it concrete as EX-ARITH and
   EX-SCHEMA.
6. **"A transitive toy, which must return equality."** Equality holds by construction (A2), so the toy is non-vacuous
   only with a non-permutation `T`. TT-4 and TT-6 are chosen accordingly.
7. **The verdict rule.** The sketch gives no rule for combining instances into an overall verdict, and none for
   choosing among the variants. The draft uses §4.2's map (OQ-8) and the OQ-13 selection table.
8. **The coefficient.** The wave rule's coefficient is named `α` in Lean, which clashes with the branch α, and the
   sketch does not fix its value. The draft writes it `a` and fixes `a = 1` (OQ-3).

***

## 9. Limitations: what C-1 can and cannot show

- **Scope of the comparison.**
  - The assessment's B3 and CE-8 already show that on generic finite bijections β's numbers need not be single-orbit
    frequencies (BSB:129–142, BSB:248).
  - C-1 asks only whether the native wave dynamics behaves like that at the twelve frozen sizes: `d = 1`, `a = 1`,
    `q ∈ {2, 3}`, `L ≤ 8`, one contiguous region, and the two readouts `pc` and `cur`.
  - Each verdict holds for its readout only. Neither extends to larger `L`, to `d ≥ 2`, to the manuscript instance
    `d = 3` (§2.1), to other couplings, to the rounded rule, or to other regions or splits.
  - **The coupling (OQ-3 = A).** Only `a = 1` is run. On a ring with even `L`, the staggered negation
    `g(p, c)_i = (−1)^i (p_i, c_i)` satisfies `g ∘ φ_a = φ_{−a} ∘ g` [D, `OQ-DECISIONS.md` OQ-3], so at `q = 3` the
    coupling `a = 2 ≡ −1` is isomorphic to `a = 1` at even `L`. At odd `L` (N3, N9) it is not covered, and could add
    information.
  - At `d = 1` the instances are outside posit (v)'s splitting clause (`d ≥ 2`, BSB:225; Main:726).
- **Two objects, and the horizon.** `T^β` is the representation's declared law; `T^{α,O}` is the cycle-horizon
  frequency on an orbit taken as actual. Their agreement is what C-1 tests, not a premise. By Lemma A, the frequencies
  compared are those over a whole cycle of the orbit. A cycle is of order up to the recurrence time, which no
  accessible window reaches (BSB:259; Main:141). Agreement over accessible windows is untested by C-1; it is C-3's
  subject.
- **No selection.**
  - A FREQ verdict would show that, on those instances, the credence numbers coincide with every candidate orbit's cycle
    frequencies. The identity of the actual orbit then does not matter for one-step numbers there.
  - It would not derive any credence, select a measure, or supply a premise. That is the (Q-sel) question
    (BSB:77–79), which C-1 leaves where BSB:181 left it.
- **What the variants separate.** A disagreement between `T^{α,O}` and a credence can arise in three ways:
  - (i) short, observer-lacking orbits carry weight in the credence. On every native instance, the fixed point at
    state 0, with row `δ₀` (`waveSubstratum_phi_fixes_zero`), is such an orbit.
  - (ii) a candidate orbit is C4-lacking: its `T^{α,O}` is a permutation matrix, which differs from every
    non-deterministic credence row.
  - (iii) observer-bearing orbits' frequencies genuinely differ from one another, or from the credence over them.

  Each variant excludes a different subset:
  - R0 excludes none of (i)–(iii) from the credence and excludes short orbits from the candidates.
  - S1 removes (ii).
  - S2 removes (i).
  - S3 removes both, so a NOT under S3 locates (iii).

  Comparing the recorded variants on one instance therefore shows which mechanism a disagreement comes from.
- **What S2 and S3 test, and vacuity.**
  - Under S2 and S3, the credence is a positive-weight mixture of the candidates' own rows. By Lemma V′ (§4.1), these
    variants test whether the candidate orbits agree with one another on the rows they share. They do not compare the
    candidates with an independent credence.
  - A row visited by one candidate only can never mismatch. When no row is shared, `shared_rows = 0` and the FREQ is
    automatic.
  - Such a FREQ is reported as FREQ_VACUOUS under every variant (Lemma V) and is excluded from the overall verdict.
    When no instance has a non-vacuous verdict and at least one is vacuous, the overall verdict is VACUOUS_ALL, which
    carries no information.
  - A FREQ with `shared_rows ≥ 1` shows that at least one row's credence pools two or more twin classes and the
    candidates still match. It does not show that every row was a non-trivial comparison. `shared_rows` is recorded for
    that reason.
  - **Non-vacuity is certified modulo the word relation (§2.7).** Orbits with the same primitive cyclic visible word are
    merged into one class, and their agreement is not counted.
    - The relation contains every twin pair that any visible-fixing symmetry commuting with `φ` can produce, since such
      a symmetry preserves visible words. It also contains every power relation.
    - So, with respect to symmetry, the certificate is exact. It does not depend on listing symmetries in advance.
    - This is why the frozen groups are only a cross-check. A group cannot be complete: at the `r = 1` instances with
      `q | L`, translations by hidden-supported φ-fixed configurations are further symmetries (§2.7).
  - **What the relation does not cover.** Two orbits with different primitive words can still have equal `T^{α,·}` rows,
    because the rows depend only on the counts of letter pairs. Such agreement counts as non-vacuous. It is a coincidence
    of counts, not a consequence of symmetry. CC-AGREE2 is an example.
- **The variants are frozen.**
  - Which variant answers C-1's question is a question about the prior and the candidates, not a computation. The
    owner answered it: `13b`, variant S1.
  - The four variants are frozen before the result. The C-1 verdicts are S1's, one per readout; R0, S2 and S3 are
    diagnostics, and no variant outside the four can be adopted from this run.
- **Under QB-1.** A NOT in the selected variant means that its credence numbers are not the operational target on that
  instance without a further premise, such as a typicality hypothesis or a selection of the actual orbit. No verdict
  says which orbit is actual.
- **Interaction with QB-1.**
  - QB-1 makes operational frequencies the target, and denies that credences establish a Born law by themselves.
  - C-1 compares a credence with the frequency side at the cycle horizon only. So FREQ cannot establish a Born law under
    QB-1 either: it establishes a coincidence of numbers at a horizon no observer reaches.
  - The one-step numbers are not the Born exponent. The native Born weights `|U_φ|²` lie in `{0, 1}` under every branch
    (BSB:117–121), and C-1 does not touch interface (a).
- **`ℓ_min` and `Long′` are proxies.** The rule `n + 1` is a necessary condition for an orbit to carry hidden capacity,
  not a characterization of observer-bearing orbits. `Long′` adds a necessary condition for history readback. Other
  predicates can change the verdict (CC-SHORT, CC-PERM). The verdicts hold only for the frozen predicates.
- **Present-visible records only.** The credence side is conditioned on `x₀`. Records of longer histories change both
  sides (BSB:250–256, Lemma A3) and are not tested.
- **P-divisibility record.** By Lemma PD the record is a function of whether `T^{α,O}` is a 0/1 matrix, and
  `pdiv_beta` of whether `T^β` is a permutation matrix. It adds no information independent of the comparison data,
  carries no verdict, and is not an independent scientific result (OQ-6).
- **Calibration of the tool.** The controls are constructed toys with hand-derived values. A complete run shows that
  the implementation reproduces them, and that the native `φ` matches the hand-derived steps. It does not show that the
  rule behaves as intended on inputs unlike the controls. The gating closure check (§2.0) catches an
  orbit-fragmenting bug that still partitions `S` on every native instance; RX-ORD is a diagnostic record only
  (OQ-7). The added controls CC-ORDER, M-FRAG, WF-q2-L6-r2 and WF-CUR are hand-derived in r7, and the independent
  review of r7 recomputed their values exactly (#1082 c.6651181144; OQ-10).
- **Consistency axis.** Whatever the verdict, it moves no correctness band (§A.23). A halted run establishes nothing
  about the wave substratum.
