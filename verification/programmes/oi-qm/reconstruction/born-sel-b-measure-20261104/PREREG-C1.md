# BORN-SEL C-1 preregistration: single-orbit frequencies against the Born-form weights on small wave substrata (#1059, part (b))

**Status.** WIP / UNVERIFIED preregistration, draft r4. Revised after the independent review of `3be25e7f` (ACCEPT WITH
CHANGES) and the delta reviews of `c610b2b8` and `1962c378` (each ACCEPT WITH CHANGES); not re-reviewed. Paper only. Nothing has been run or
written as code, and no native instance has been enumerated.

**Not a candidate freeze yet.** The freeze sequence is in §7. First, the owner answers OQ-1 to OQ-14 (§8.2). This text
is then revised to carry the answers, and the revised commit is independently reviewed. Only then does the owner
designate `F`. At `F` no item of this text may still await an answer. **Not authorized to run.** A run needs, after `F`,
the owner's go, the tool, its review, and a separate dispatch approval (§7).

- **Frozen inputs at `F`.** All four are in `verification/programmes/oi-qm/reconstruction/born-sel-b-measure-20261104/`,
  beside the assessment (§A.36):
  - this file, `PREREG-C1.md`;
  - `C1-INSTANCES.json`, which holds the instance list, the order, the encodings, the explicit toy maps, the unit-control
    inputs, the wave rule's parameters and the recorded OQ-13 answer;
  - `C1-CONTROLS-EXPECTED.json`, the hand-derived expected values of every control and mutation;
  - `C1-OUTPUT-SCHEMA.json`, the machine-readable schema of every output file and of the expected file.
- **Source.** `BORNSEL-B-MEASURE.md` r3, accepted at `7b46d36c` (review `REVIEW-7b46d36c.md`: ACCEPT). Its §7 C-1 sketch
  (lines 404–416 of that file) is the specification frozen here. Base for every corpus citation: `origin/main`
  `1609dc440f5a12d05b750f6d894bb91d09a099a3`.
- **Authorization.** Owner, chat 2026-11-04, #1059 c.6624262539: draft, but do not run, a frozen preregistration for
  C-1. The run is a separate later decision.
- **Owner decisions consumed.** QB-1 and QB-2 (§2.6). OQ-1 to OQ-14 are open (§8.2).

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
- The four verdict variants are R0, S1, S2 and S3 (§4.1). R0 is the sketch's rule (BSB:406–410). No variant takes
  precedence until OQ-13 is answered; the frozen rule of §4.2 then selects one.

***

## 1. Objective and non-objectives

**Objective.** By exhaustive exact enumeration over ℚ, on small instances of the manuscripts' wave substratum, decide
for each instance whether "β's one-step numbers are single-orbit frequencies" (BSB:406). The question is whether, for
every candidate orbit `O` of `φ`, the orbit's cycle transition frequencies `T^{α,O}` equal the observer's one-step
credence on every visible row the orbit visits. Two things are left to OQ-13 (§4.2):
- which orbits are the candidates for `O*`: the long orbits, or the long orbits that carry history readback;
- which orbits the credence prior ranges over: all orbits, or the candidates only.

Each of the four combinations is a frozen verdict variant (§4.1). The C-1 verdict is the one the OQ-13 answer selects,
and all four are recorded. On the same instances, the run also records per orbit whether the α-rooted family is
P-divisible on `{0, …, |O|}` (BSB:411, B4).

**What the question is, in the owner's terms [D].**
- **Credence side (QB-2).** Under QB-2, the embedded observer's assignment given the present visible value `x₀ = a` is
  an invariant maximal-entropy prior conditioned on that record. With the prior over all of `S`, this is
  `unif({a} × 𝒞_H)` (BSB:206–208, γ-c with a present-visible record). Its one-step numbers are `T^β` (Main:117,
  Main:288–290). With the prior restricted to a union `U` of orbits, it is `unif(U ∩ ({a} × 𝒞_H))`.
- **Frequency side (QB-1).** Under QB-1 the physical target is operational frequencies. By BSB:239–241 (Lemma A), the
  transition frequencies along the actual trajectory over a whole cycle of the actual orbit `O*` are `T^{α,O*}`.
- **The comparison.** C-1 asks, on native instances, whether these two coincide for every orbit admitted as a candidate
  `O*`.

**Non-objectives.** The run does not cover:
- accessible-window frequencies (C-3, deferred until after QB-1; BSB:424);
- any Lean work (C-2);
- `d ≥ 2`, `d = 3`, the rounded (nonlinear) rule, or a coupling other than `a = 1`;
- record-constrained measures beyond the present-visible record;
- any selection of a measure, a new premise, a manuscript edit, a status change, merge or publication.

**What a completed run establishes.** For each evaluated native instance, at the frozen sizes and conventions, it
records four verdicts: R0, S1, S2 and S3. Each verdict is one of:
- FREQ: every candidate orbit matches, and at least one comparison is not automatic;
- FREQ_VACUOUS: every candidate matches, but only by construction, because `shared_rows = 0` (§4.1);
- NOT: some candidate does not match;
- VOID_NO_ORBIT: there is no candidate. It also records the per-orbit P-divisibility. The reported C-1 verdict is the variant
that the OQ-13 answer selects (§4.2). This is a result on the consistency axis (§A.23): it compares objects the
framework itself defines and confronts no external measurement.

**What it does not establish.** See §9. In particular, it does not select a measure, does not bear on accessible
windows, and does not extend beyond the frozen instances.

***

## 2. Frozen preconditions

### 2.0 Conventions common to every instance

- **Arithmetic.** All counts are exact integers. A probability is a pair of integers reduced to lowest terms. Equality
  of two probabilities `x/y` and `u/v` is decided by `x·v = u·y` on integers. No floating-point value enters the
  computation, the comparison or the verdict path. One appearing in an output probability field is a schema violation
  (exit 2) [D].
- **Configurations.** Every toy or native instance is a finite set `S = 𝒞_V × 𝒞_H`, with `n = |𝒞_V|` and
  `m = |𝒞_H|`. A state is an integer `s ∈ {0, …, nm − 1}`, with visible value `π_V(s) = s mod n` and hidden value
  `s div n`, so `s = v + n·h` [D].
- **Map.** `φ` is given as an array `φ[s]` over all of `S`: by an explicit table for toy instances
  (`C1-INSTANCES.json`), and by the wave rule of §2.1 for native instances.
- **Enumeration method.** Full: every state of `S`, for every instance. No sampling, no sequential method.
- **Budget check.** Before any enumeration, the tool checks `state_count = n·m ≤ 2¹⁶` from the frozen parameters, and
  exits 7 otherwise.
- **Bijectivity check.** For every toy and native instance, the tool first checks that `φ` is injective on `S`. A failure
  exits 5 before any other field of that instance is computed. For mutation M-INJ, which is expected to be
  non-injective, the detection is the compared field (§3.3).
- **Orbits.** The orbits are the cycles of `φ`. An orbit's representative `rep(O)` is its least state index, and orbits
  are listed in increasing `rep`. `|O|` is the cycle length, and `ord(φ)` is the least common multiple of the cycle
  lengths.
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
  - The visible configuration is the `(prev, cur)` pair at each site of `R`, so `n = q^{2r}`. The hidden configuration
    is the pair at each site outside `R`, so `m = q^{2(L−r)}`.
  - Because the rule commutes with translations (A4Exact), every contiguous block of `r` sites gives the same instance
    up to relabelling. The block at the origin is chosen.
- **The state encoding [D].**
  - Site digit `δ_i = p_i·q + c_i ∈ {0, …, q²−1}`; state index `s = Σ_i δ_i·(q²)^i`.
  - Then `π_V(s) = s mod q^{2r}` and the hidden value is `s div q^{2r}`, consistent with §2.0's `s = v + n·h`.
- **Two implementations [D].** The tool computes `φ` twice:
  - (i) by the site loop above;
  - (ii) as the linear map `F = [[0, I], [−I, A]]` on `(p, c) ∈ (ℤ/q)^{2L}`, with `A` the circulant ring adjacency
    (SM:1602), applied to the digit vector.

  The two arrays must be identical on all of `S`, and the tool exits 4 otherwise.

### 2.2 Native instances and sizes [D]

Native instances run in this order: increasing `|S|`, with ties broken by `q` and then by `r`. `|S| = q^{2L}`.

| Order | id | q | L | r | `n = q^{2r}` | `m = q^{2(L−r)}` | `|S|` | `ℓ_min = n+1` | `gcd(L, q)` |
|---|---|---|---|---|---|---|---|---|---|
| N1 | W-q2-L3-r1 | 2 | 3 | 1 | 4 | 16 | 64 | 5 | 1 |
| N2 | W-q2-L4-r1 | 2 | 4 | 1 | 4 | 64 | 256 | 5 | 2 |
| N3 | W-q3-L3-r1 | 3 | 3 | 1 | 9 | 81 | 729 | 10 | 3 |
| N4 | W-q2-L5-r1 | 2 | 5 | 1 | 4 | 256 | 1,024 | 5 | 1 |
| N5 | W-q2-L6-r1 | 2 | 6 | 1 | 4 | 1,024 | 4,096 | 5 | 2 |
| N6 | W-q2-L6-r2 | 2 | 6 | 2 | 16 | 256 | 4,096 | 17 | 2 |
| N7 | W-q3-L4-r1 | 3 | 4 | 1 | 9 | 729 | 6,561 | 10 | 1 |
| N8 | W-q2-L7-r1 | 2 | 7 | 1 | 4 | 4,096 | 16,384 | 5 | 1 |
| N9 | W-q3-L5-r1 | 3 | 5 | 1 | 9 | 6,561 | 59,049 | 10 | 1 |
| N10 | W-q2-L8-r1 | 2 | 8 | 1 | 4 | 16,384 | 65,536 | 5 | 2 |
| N11 | W-q2-L8-r2 | 2 | 8 | 2 | 16 | 4,096 | 65,536 | 17 | 2 |

- **Budget.** Every instance has `|S| ≤ 2¹⁶`. `q = 2` reaches `2¹⁶` at `L = 8`. `q = 3` stays below it through `L = 5`
  (`3^{10} = 59,049`), so `L = 6` (`3^{12} = 531,441`) is excluded.
- **Region sizes.** `r ≤ L/3` gives `r = 1` for `L ≤ 5` and `r ∈ {1, 2}` for `L ∈ {6, 7, 8}`.
- **W-q2-L7-r2 is excluded in this draft.**
  - By SM Theorem A.1 (SM:1604–1606: "For q prime with gcd(L, q) = 1 — q = 2 included: ord(F mod q) = qL"), every orbit
    length divides `qL = 14 < 17 = ℓ_min`. That instance would therefore be void by construction.
  - This uses the theorem's statement only; no orbit of any instance was computed [D].
  - The exclusion is open as OQ-4.
- **Coprime and non-coprime.** N1, N4, N7, N8 and N9 satisfy `gcd(L, q) = 1`, inside Theorem A.1's scope. The others
  have `q | L`, where the parabolic Jordan blocks of SM Appendix A are present. Both kinds are included.
- **Theorem 22's hypotheses [P, SM:1376]** are "connected bounded-degree coupling graph with diameter D ≥ 4 … any
  connected subgraph V with |V| ≤ N/3".
  - Every frozen `R` is connected and has `|R| ≤ N/3`. These are checked from the frozen parameters, and the tool exits
    2 if they are violated.
  - The ring's diameter `⌊L/2⌋` is at least 4 only at `L = 8` (N10, N11). It is recorded per instance as
    `diameter_ge_4`.
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
    be arbitrary there for the implication, which would make a full-`𝒞_V` record depend on an arbitrary choice.
  - The restriction to `V_O` is OQ-5.
- **The recorded quantity.** `pdiv_alpha(O) := PDivisible |O| Γ^{α,O}`, on `V_O`, with horizon `{0, …, |O|}` (BSB:411).
- **The β family [D].**
  - `Γ^β_t(a, j) := #{h : π_V φ^t(a, h) = j}/m` on `𝒞_V`. This is the kernel's `rootedMap` for the cut realization
    with the uniform prior.
  - `pdiv_beta := PDivisible ord(φ) Γ^β`, with horizon `{0, …, ord(φ)}`, where `Γ^β_{ord(φ)} = I`.
  - It is required on CE-8. Recording it on native instances is OQ-6.
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

### 2.5 `ℓ_min` (fixed before any result) [D; owner item OQ-1]

- **What the corpus says [P].**
  - Main:62: "the atypical short orbits of the idealized linear dynamics (fixed points, low-period cycles) are precisely
    observer-lacking substrata — an orbit of period `p` makes at most `p` states dynamically accessible, so for small
    `p` no partition of it can satisfy the high-capacity condition C3".
  - C3 is `log₂|𝒞_H| ≥ I*` (Main:78). The corpus does not quantify "small `p`".
- **The draft rule [D].** `ℓ_min(I) := n_I + 1`, where `n_I = |𝒞_V|` of instance `I`. It depends only on the instance's
  declared parameters, so it is fixed before any result.
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
  - Both choices, which candidates and which prior support, are OQ-13. Each combination is a frozen variant (§4.1),
    and §4.2's rule selects one by the answer. All four are frozen now, so that none can be chosen after the result.
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
  - The support is OQ-13. C-1 is silent on the prior's physical source.

***

## 3. The frozen control set

The expected values are hand derivations of constructed toys, frozen in `C1-CONTROLS-EXPECTED.json`. §A.29's "rule, not
numbers" applies to the native decision rule of §4, which is frozen without reference to any native value. **No expected
value is given for any native instance.**

**Execution order.**
- The 17 controls and mutations run first, in the order of `C1-INSTANCES.json` (orders 1–17):
  - the ten toys of §3.1;
  - M-INJ, EX-ARITH, EX-SCHEMA and EX-CERT;
  - WF-q2-L5, WF-q3-L4 and WF-0.
- The 11 native instances follow (orders 18–28), in §2.2's order.
- Native instances run only if every control and mutation has matched. A mismatch halts the run before any native
  instance is evaluated, so no native verdict is ever printed over a failed control (§A.29).

### 3.1 Toy controls (explicit maps; `s = v + n·h`)

In the table, `FREQ_V` abbreviates FREQ_VACUOUS. `sr` gives `shared_rows` for R0 / S1 / S2 / S3 (§4.1).

| id | `n`, `m` | `φ` as an array over `s = 0, 1, …` | R0 / S1 / S2 / S3 | `sr` | Purpose |
|---|---|---|---|---|---|
| CE-8 | 2, 4 | `[1, 2, 3, 0, 6, 7, 5, 4]` | NOT / NOT / NOT / FREQ_V | 2/2/2/0 | the assessment's counterexample (BSB:129–138) |
| TT-4 | 2, 2 | `[1, 3, 0, 2]` | FREQ_V ×4 | 0/0/0/0 | transitive toy, A2 (BSB:246): equality by construction |
| TT-6 | 3, 2 | `[1, 4, 3, 5, 2, 0]` | FREQ_V ×4 | 0/0/0/0 | transitive toy with unequal rows and `n = 3` |
| CC-TWIN | 2, 4 | `[1, 3, 0, 2, 5, 7, 4, 6]` | FREQ ×4 | 2/2/2/2 | non-transitive, two matching orbits: non-vacuous FREQ under every variant |
| CC-SHORT | 2, 4 | `[1, 3, 0, 2, 4, 6, 5, 7]` | FREQ / FREQ / FREQ_V / FREQ_V | 2/2/0/0 | short orbits that balance, excluded by `ℓ_min` |
| CC-UNVIS | 3, 2 | `[1, 3, 5, 4, 0, 2]` | FREQ_V / VOID / FREQ_V / VOID | 0/0/0/0 | unvisited row; orbit length exactly `ℓ_min`; `Long′ = ∅` |
| CC-VOID | 2, 1 | `[1, 0]` | VOID ×4 | 0/0/0/0 | no orbit reaches `ℓ_min`; void takes precedence over equality |
| CC-SKEW | 2, 3 | `[1, 3, 0, 2, 4, 5]` | NOT / NOT / FREQ_V / FREQ_V | 2/2/0/0 | short orbits that skew `T^β` |
| CC-PERM | 2, 6 | `[1, 2, 3, 0, 5, 7, 4, 6, 8, 9, 10, 11]` | NOT / FREQ / NOT / FREQ_V | 2/2/2/0 | a long orbit with a permutation `T^{α,O}` |
| CC-S3NOT | 2, 4 | `[2, 3, 1, 0, 6, 4, 5, 7]` | NOT ×4 | 2/2/2/2 | two C4-bearing long orbits that disagree: S3 reaches NOT |

Each outcome reached per variant:

| Variant | Non-vacuous FREQ | FREQ_VACUOUS | NOT | VOID_NO_ORBIT |
|---|---|---|---|---|
| R0 | CC-TWIN, CC-SHORT | TT-4, TT-6, CC-UNVIS | CE-8, CC-SKEW, CC-PERM, CC-S3NOT | CC-VOID |
| S1 | CC-TWIN, CC-SHORT, CC-PERM | TT-4, TT-6 | CE-8, CC-SKEW, CC-S3NOT | CC-UNVIS, CC-VOID |
| S2 | CC-TWIN | TT-4, TT-6, CC-SHORT, CC-UNVIS, CC-SKEW | CE-8, CC-PERM, CC-S3NOT | CC-VOID |
| S3 | CC-TWIN | TT-4, TT-6, CE-8, CC-SHORT, CC-SKEW, CC-PERM | CC-S3NOT | CC-UNVIS, CC-VOID |

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
  - All four verdicts are FREQ, on a non-transitive map. Both orbits visit both rows and are both candidates under
    every variant, so `shared_rows = 2` throughout and no FREQ is vacuous.
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

### 3.2 Native-faithfulness controls (hand-derived, [D])

These check that the implemented `φ` is the §2.1 rule.
- They run in the control phase, before any native instance, and compute `φ` on the listed states only, with both
  implementations of §2.1.
- A mismatch, or a disagreement between the two implementations, exits 1 and halts.
- WF-0 is a sanity check only: `φ(0) = 0` holds for every additive map, so it is not a faithfulness checkpoint.

The controls:
- **WF-0** (for the parameters of each of N1–N11): `φ[0] = 0` (`waveSubstratum_phi_fixes_zero`,
  `StochasticInterface.lean:101`).
- **WF-q3-L4** (the parameters of N7), starting from `p = (0,0,0,0)`, `c = (1,0,0,0)`:
  - step 1: `p′ = (1,0,0,0)`, `c′ = (0,1,0,1)`;
  - step 2: `p″ = (0,1,0,1)`, `c″ = (1,0,2,0)`;
  - as state indices: `1 → 741 → 2377`; visible values (`n = 9`): `1 → 3 → 1`.
- **WF-q2-L5** (the parameters of N4), starting from `p = 0`, `c = (1,0,0,0,0)`:
  - step 1: `p′ = (1,0,0,0,0)`, `c′ = (0,1,0,0,1)`;
  - step 2: `p″ = (0,1,0,0,1)`, `c″ = (1,0,1,1,0)`;
  - as state indices: `1 → 262 → 601`; visible values (`n = 4`): `1 → 2 → 1`.

### 3.3 Mutations and unit controls

- **M-INJ (bijectivity check).**
  - The rule is the §2.1 rule with the `−p` term deleted, `(p, c) ↦ (c, A c)`, at `q = 2`, `L = 3`, `r = 1`. It is
    computed by both implementations: the site loop without `−p_i`, and the linear map `[[0, I], [0, A]]`.
  - Two states with the same `c` and different `p` collide, so `φ` is not injective [D].
  - Expected: `phi_impls_agree = true`, `injective = false` and `evaluated_beyond_injectivity = false`. If the tool
    reports `injective = true`, the run exits 1.
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
- For EX-ARITH, EX-SCHEMA and EX-CERT, the comparator, validator and checker are called as units on the frozen inputs.
  The expected outcome is a compared field and does not exit; a different outcome exits 1.
- **Countercontrols built into §3.1.**
  - CC-TWIN: FREQ is reachable on a non-transitive map.
  - CE-8: NOT is reachable.
  - CC-SHORT: `ℓ_min` excludes short orbits.
  - CC-UNVIS: unvisited rows are excluded, and `Long′ = ∅` is handled.
  - CC-VOID: the void rule takes precedence over equality.
  - CE-8, CC-SHORT, CC-SKEW, CC-PERM and CC-UNVIS together separate every pair of variants.
  - Every variant reaches NOT; CC-S3NOT is the only control in which S3 does.
  - Every variant reaches a non-vacuous FREQ (CC-TWIN) and FREQ_VACUOUS (TT-4).
  - The definitional check on every toy is the countercontrol for Lemma PD (§2.4).

### 3.4 Recorded cross-checks (recorded only in this draft; owner item OQ-7)

- **RX-ORD.** For N1, N4, N7, N8 and N9 (`gcd(L, q) = 1`), SM Theorem A.1 states `ord(φ) = qL` (SM:1604–1606; SM:1610:
  "Verified computationally for q = 2, 3, 5, 7, 11, 13 and L ≤ 12").
  - The tool records `ord(φ)` and the boolean `ord_phi_eq_qL`.
  - In this draft a disagreement does not void C-1. It would be a finding about SM Appendix A or the tool, diagnosed
    after the run.
  - Making RX-ORD gating would need its own exit code. That choice is OQ-7.

***

## 4. Decision rule

### 4.1 Per native instance: the four frozen variants

Each variant is a deterministic map from the per-orbit record. A variant is given by its candidate set `C` (the orbits
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
- `shared_rows := #{a ∈ W_C : the pool at a has at least two orbits}`, where `W_C = ⋃_{O ∈ C} V_O`.
  - For S2 and S3 this is the number of rows visited by two or more candidates.
- **Lemma V (vacuity).** If `shared_rows = 0`, every row a candidate visits has that candidate as its only pooled orbit.
  Then `K(a, ·) = T^{α,O}(a, ·)` there, and every candidate matches by construction. Consequently:
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

**Aggregation.** The same map is applied separately to each variant. For a variant, let `Ev` be the set of native
instances whose verdict under that variant is FREQ or NOT. FREQ_VACUOUS and VOID_NO_ORBIT instances are excluded from
`Ev` and listed separately. The variant's overall verdict is:
- `FREQ_ALL` if `Ev ≠ ∅` and every instance in `Ev` is FREQ;
- `NOT_ALL` if `Ev ≠ ∅` and every instance in `Ev` is NOT;
- `MIXED` if `Ev` contains both;
- `VACUOUS_ALL` if `Ev = ∅` and at least one instance is FREQ_VACUOUS;
- `VOID_ALL` if every instance is VOID_NO_ORBIT.

These five cases are exhaustive and mutually exclusive.

These are recorded as `c1_r0_verdict`, `c1_s1_verdict`, `c1_s2_verdict` and `c1_s3_verdict`.

**The selection rule.** OQ-13 has two parts:
- (i) which orbits are the candidates for `O*`: the long orbits, or the long orbits that carry history readback;
- (ii) whether the credence prior ranges over all orbits or over the candidate orbits only.

Its answer is recorded before `F` as the constant `oq13_answer` in `C1-INSTANCES.json`. The C-1 verdict (`c1_verdict`)
is the overall verdict of the variant this table assigns to that answer:

| `oq13_answer` | (i) candidates | (ii) prior support | Selected variant | `c1_verdict` = |
|---|---|---|---|---|
| `13a` | long orbits (`Long`) | all orbits | R0 | `c1_r0_verdict` |
| `13b` | long C4-bearing orbits (`Long′`) | all orbits | S1 | `c1_s1_verdict` |
| `13c` | long orbits (`Long`) | the candidates only | S2 | `c1_s2_verdict` |
| `13d` | long C4-bearing orbits (`Long′`) | the candidates only | S3 | `c1_s3_verdict` |

- The table covers every combination of the two binary choices, so it has no gaps on its option space.
- An answer outside it, such as a different candidate predicate or a different prior support, is written into the text
  as a new frozen variant and a new table row before the review that precedes `F` (§7).
- If `oq13_answer` is not one of the four codes at run time, the tool exits 2 before any instance.
- The three variants not selected are recorded and do not qualify the C-1 verdict.

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
      - the mixture identity, double stochasticity and the partition `Σ_O |O| = |S|`;
      - agreement of the two P-divisibility methods, and every certificate verifying under (i)–(iv);
      - no NOT with `shared_rows = 0`;
    - the frozen-input check passes, and `oq13_answer` is valid;
    - every output validates against `C1-OUTPUT-SCHEMA.json`.
  - **Step (b) exits 0.** The step recomputes, from the orbits files and `T_beta`:
    - every `eq`, `long_c4`, `eq_beta_long`, `eq_beta_c4`, `T_beta_long` and `T_beta_c4`, and each variant's
      `shared_rows`;
    - each instance's four verdicts and the four overall verdicts;
    - `c1_verdict`, from `oq13_answer` and the table of §4.2;
    - every `orbits_sha256`.

    It compares them with the stored values, and any difference exits 6.
  - **Step (c) exits 0.** It regenerates `verdict_text` from `summary.json` and compares the two byte for byte. A
    difference exits 8.
- **Otherwise the run halts at the first failure.**
  - `summary.json` then has `run_status = HALT`, and every `c1_*_verdict` is `null`.
  - The `native_*_verdicts` maps are empty whenever `run_status = HALT`.
  - A native instance's file written before a halt carries no verdict of the run.
  - A failure in step (b) or (c) is read from that step's exit status and conclusion. `summary.json` is written by step
    (a) and does not record it.
- Under §A.29, a halted run establishes nothing about the wave substratum. There is no partial verdict, no rerun within
  a freeze, and no amendment after `F`. A runner failure before step (a) starts is governed by the OQ-14 answer, which
  is written into this text before `F`.
- **PASS (the result reviewer's test).** All five of these hold:
  - the host's conclusion for the C-1 job is `success`, read from its API;
  - step (a) exits 0;
  - step (b) exits 0;
  - step (c) exits 0;
  - `summary.json` has `run_status = COMPLETE`.

  Only under PASS is `summary.json`'s `c1_verdict` read as the result. The other three variants' overall verdicts are
  recorded with it.

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
| `c1/<id>.json`, native instance | `native_record` | the analysis fields below, plus `phi_impls_agree`, `phi_zero_fixed`, `ord_phi_eq_qL` (`null` outside RX-ORD) and `diameter_ge_4` |
| `c1/<id>.json`, unit control or mutation | `unit_record` | `params` (M-INJ, WF); `phi_impls_agree` (M-INJ, WF); `injective` and `evaluated_beyond_injectivity` (M-INJ); `results` and `reduced` (EX-ARITH); `schema_results` (EX-SCHEMA); `cert_results` and `cert_failed_clauses` (EX-CERT); `hand_steps` (WF-q*, items `{step, prev, cur, state, visible}`); `phi_of_zero` (WF-0); `expected`, `comparisons`, `match` |
| `c1/<id>.orbits.jsonl`, toys and natives | `orbit_record`, one per line | `rep`, `length`, `cycle`, `visited_rows`, `unvisited_rows`, `n_a`, `T_alpha`, `long`, `eq`, `first_mismatch`, `pdiv_alpha`, `pdiv_witness`, `long_c4`, `eq_beta_long`, `first_mismatch_beta_long`, `eq_beta_c4`, `first_mismatch_beta_c4`, `pdiv_alpha_definitional` (`null` on natives) |
| `c1/<id>.pdiv-certs.json`, toys | `pdiv_certs` | `schema`, `id`, `entries`: `{family, rep, rows, pair, kind, lambda, farkas_y}` |
| `c1/summary.json` | `summary` | `schema`, `oq13_answer`, `selected_variant`, `controls_frozen` (17), `controls_matched`, `natives_frozen` (11), `natives_evaluated`, `native_verdicts` (R0), `native_s1_verdicts`, `native_s2_verdicts`, `native_s3_verdicts`, `c1_verdict`, `c1_r0_verdict`, `c1_s1_verdict`, `c1_s2_verdict`, `c1_s3_verdict`, `run_status`, `first_failure`, `verdict_text` |

On a halt, `oq13_answer` and `selected_variant` may be `null`, which covers the exit-2 halt on an unset answer. On a
complete run both must be set; the schema enforces this through a conditional on `run_status`.

**Analysis fields** (toy and native records):
- `params`;
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

**Verdict text.** It is rendered from the summary fields only.
- **Placeholders.**
  - `<ids>` is a comma-separated list in run order, or `none`.
  - `<V>` is `selected_variant`, and `<A>` is `oq13_answer`.
  - `<P>` is the frozen phrase of the selected variant:
    - R0: "T^{α,O} = T^β on visited rows for every orbit with |O| ≥ ℓ_min";
    - S1: "T^{α,O} = T^β on visited rows for every orbit with |O| ≥ ℓ_min whose T^{α,O} is not a permutation matrix";
    - S2: "T^{α,O} = T^{β_long} on visited rows for every orbit with |O| ≥ ℓ_min";
    - S3: "T^{α,O} = T^{β_c4} on visited rows for every orbit with |O| ≥ ℓ_min whose T^{α,O} is not a permutation
      matrix".
  - `<N>` is the negation of `<P>`: "for some candidate orbit, T^{α,O} differs from the variant's credence on a visited
    row".
  - `<R>` is "Recorded: R0 <c1_r0_verdict>; S1 <c1_s1_verdict>; S2 <c1_s2_verdict>; S3 <c1_s3_verdict>."
  - `<X>` is "Vacuous instances (every candidate matched by construction, shared_rows = 0): <ids>. Void instances:
    <ids>."
- **COMPLETE runs.**
  - FREQ_ALL: "C-1 (variant <V>, OQ-13 answer <A>): all <k> controls matched. On every native instance with a
    non-vacuous verdict (<ids>), <P>. <X> <R>"
  - NOT_ALL: "C-1 (variant <V>, OQ-13 answer <A>): all <k> controls matched. On every native instance with a
    non-vacuous verdict (<ids>), <N>. <X> <R>"
  - MIXED: "C-1 (variant <V>, OQ-13 answer <A>): all <k> controls matched. FREQ on <ids>; NOT on <ids>. <X> <R>"
  - VACUOUS_ALL: "C-1 (variant <V>, OQ-13 answer <A>): all <k> controls matched. No native instance has a non-vacuous
    verdict under variant <V>: every candidate matched only by construction, or there was no candidate. The C-1 verdict
    carries no information. <X> <R>"
  - VOID_ALL: "C-1 (variant <V>, OQ-13 answer <A>): all <k> controls matched. No native instance has a candidate orbit
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
| 2 | (a) | a schema violation, in an output or in the expected file against `expected_file`; a frozen parameter inconsistent with §2.2's formulas or with Theorem 22's region conditions; an invalid `oq13_answer`; or a floating-point value in a probability field |
| 3 | (a) | a frozen input does not match its git blob id at `F`, or `F` is not in the checkout |
| 4 | (a) | an invariant failure: the `φ` implementations disagree; the mixture identity or double stochasticity fails; the orbits do not partition `S`; the two P-divisibility methods disagree; a certificate or its coverage fails; or a NOT has `shared_rows = 0` (Lemma V) |
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
| no frozen item awaits an answer at `F` | `oq13_answer` must be one of `13a`–`13d` (exit 2); the review of the revised text (§7 step 3) checks that §8.2 carries no open item |
| the C-1 verdict is the variant the OQ-13 answer selects | step (b) recomputes `c1_verdict` from `oq13_answer` and the §4.2 table (exit 6); `selected_variant` is recorded |
| budget (§A.40) | `state_count ≤ 2¹⁶` before enumeration (exit 7); the job's `timeout-minutes`, with its conclusion read from the host |
| frozen parameters satisfy §2.2 (`n = q^{2r}`, `m = q^{2(L−r)}`, `ℓ_min = n+1`, `r ≤ L/3`, `R` contiguous) | checked from `C1-INSTANCES.json` before enumeration (exit 2) |
| `φ` is a bijection on every toy and native instance | the injectivity check (exit 5); `injective` is recorded |
| the bijectivity check detects a non-bijection | M-INJ, with `injective = false` compared; exit 1 if it is not detected |
| the implemented `φ` is the §2.1 rule | WF-q3-L4 and WF-q2-L5 (compared); the two implementations agree on all of `S` for every native instance (exit 4). WF-0 is a sanity check only |
| `T^β` is Main:117's matrix | the mixture identity and double stochasticity (exit 4); `T_beta` compared on every toy control |
| `T^{α,O}` on visited rows only; unvisited rows excluded and recorded | CC-UNVIS (compared, including `unvisited_rows`); `unvisited_rows` recorded per orbit |
| `ℓ_min = n + 1`, inclusive, fixed by parameters | `ell_min` compared on every toy and checked against the formula on every native instance (exit 2); CC-UNVIS exercises `|O| = ℓ_min`, and CC-SHORT exercises exclusion |
| the void rule takes precedence | CC-VOID (compared) |
| FREQ (non-vacuous) and NOT are both reachable under every variant | CC-TWIN (FREQ under all four); CE-8, CC-PERM and CC-S3NOT (NOT under each variant, with CC-S3NOT the only S3 NOT); see the §3.1 outcome table |
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
| one pass | the host run record shows `run_attempt = 1`, or whatever OQ-14's answer, written into this text before `F`, prescribes |
| PASS combines five signals | the job emits the exit statuses of steps (a), (b) and (c), and `summary.json`; the result reviewer reads the job conclusion from the host's API (§4.3) |
| verdict text is generated only from structured output | step (c) regenerates `verdict_text` from `summary.json` and compares it byte for byte (exit 8) |

***

## 7. Execution boundary and governance

- **CI only (§A.40).** Locally, only cheap static checks of the tool may run. The instance set runs only in CI.
- **One pass**, halting on the first red. A void run is not repaired by re-running.
- **Order of steps.**
  1. **Owner answers.** The owner answers OQ-1 to OQ-14 (§8.2).
  2. **Revision.** The text and the data files are revised to carry the answers. Each answer is written in place as the
     frozen choice: `oq13_answer` is set in `C1-INSTANCES.json`, and any instance, control or exit code an answer adds
     or removes is written in. §8.2 is then replaced by a record of the answers, quoted with author and time
     (§A.42 item 7). After the revision no item remains open.
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
- **Governance form (conditional on OQ-12).** If the OQ-12 answer chooses the research-run form, then:
  - this run is not a §A.39 native V3 round;
  - it carries no `v3-round` or `v3-governed-paths` block and has no receipt;
  - it is not protocol-valid under §A.39;
  - it changes no status, label or classification by itself.

  If the answer chooses a native V3 round, step 2 rewrites this section to the §A.39 lifecycle before review.
- **Budget (an estimate, not measured).** The largest instances have `2¹⁶` states. The work per instance is:
  - two computations of `φ`, each `O(L·|S|)`;
  - a cycle decomposition, `O(|S|)`;
  - the counts, `O(|S|)`;
  - the comparisons, `O(n²)` per orbit for each variant.

  P-divisibility uses Lemma PD on native instances, so no linear program runs there. The certified method runs on toys
  only, with `k ≤ 3`. Minutes are expected. The job timeout is 30 minutes; a timeout is red, and there is no extension.
- **Evidence (§A.42).**
  - The result note states the commit, the command, `summary.json` (small, with its digest), and the owner's answers,
    designations and approvals, quoted with author and time (§A.42 item 7).
  - The tool, the checker and the workflow land on `main` with the result note, so that the command can be rerun from
    `main` (§A.42 item 1).
  - The per-orbit and certificate files can be regenerated by the command and need not land on `main`.
  - A run on a disposable branch is provenance only until its record lands on `main`.
- **Exclusions.** No C-2, no C-3, no Lean, no manuscript edit, no status change, no merge or publication.

***

## 8. Open items

### 8.1 Before `F`

Per §7, steps 1–3 come before `F`: every OQ of §8.2 is answered, the text is revised to carry the answers, and the
revised commit is reviewed. This section and §8.2 do not survive into `F` as open items.

### 8.2 Owner questions (all open)

Each item below is open for the owner. Each states the draft's default, followed by the recommendation from the reviews
of `3be25e7f` and `c610b2b8`.

1. **OQ-1, `ℓ_min`.** The draft uses `ℓ_min = n + 1` (§2.5). The corpus leaves "small p" unquantified (Main:62).
   - Alternatives: `ℓ_min = 2`, which excludes fixed points only; or a fixed number common to all instances.
   - The orbit-level C4 predicate is covered by OQ-13 part (i).
   - *Reviewer recommends:* accept `n+1` as the length threshold, with the secondaries of B1. This draft freezes those
     as variants S1–S3, selected by OQ-13.
2. **OQ-2, the visible content of a site.** The draft uses the full `(prev, cur)` pair at each site of `R`, following
   `cutRealization` (`PhysicalC4Discharge.lean:578–582`), with the block `R = {0, …, r−1}` and `r ≤ L/3`. The
   alternative is the current value only.
   - *Reviewer recommends:* accept the `(prev, cur)` pairs. The corpus answers this, and the current-value split would
     be a surrogate.
   - *Reviewer: corpus answers* — forced by the kernel's `cutRealization` (`PhysicalC4Discharge.lean:578–582`), which
     takes the region's phase-space data, the `(prev, cur)` pairs, as the visible carrier. (Review of `1962c378`;
     the item stays open.)
3. **OQ-3, the coupling.** The draft uses `a = 1` only (SM:1602; SM:222–224, :230; §2.1). At `q = 3`, `a = 2 ≡ −1` is
   not covered.
   - *Reviewer recommends:* accept `a = 1`. The corpus answers this, and `a = 2` is not a manuscript instance.
   - *Reviewer: corpus answers* — forced by SM:1602, which gives the `d = 1` ring with coefficient 1, and by
     SM:222–230, which give the observer-level `α = 1/d`, equal to 1 at `d = 1`. (Review of `1962c378`; the item stays
     open.)
4. **OQ-4, the instance list.** The draft has eleven instances, including the non-coprime ones, and excludes
   W-q2-L7-r2. Theorem 22's diameter hypothesis holds only at `L = 8`. The question is also which instances count toward
   the overall verdicts.
   - *Reviewer recommends:*
     - accept all eleven, all counting;
     - reinstate W-q2-L7-r2 as recorded. It costs nothing, VOID does not count, and it gives an RX-ORD point at `r = 2`;
     - add a recorded secondary over N10 and N11 for the diameter hypothesis.
5. **OQ-5, the α-rooted family's row set.** The draft uses `V_O` only, with horizon `{0, …, |O|}` (§2.4).
   - *Reviewer recommends:* accept `V_O`.
   - *Reviewer: corpus answers* — forced, because α defines no hidden conditional on an unvisited row. Any other row
     set adds an arbitrary datum (BSB:147). (Review of `1962c378`; the item stays open.)
6. **OQ-6, β's P-divisibility on native instances.** The draft records it.
   - *Reviewer recommends:* record it. It is free, and the theorem covering its (⇒) direction is kernel-checked
     (`RootedRecurrenceBridge.lean:93`).
7. **OQ-7, RX-ORD.** The draft records it only.
   - *Reviewer recommends:* make it gating, expecting `ord = qL` from SM:1606. It is the only whole-map control of the
     native `φ`. A cycle-detection bug that fragments orbits while still partitioning `S` would push instances toward
     VOID_NO_ORBIT, and the WF spot checks cannot see that.
   - Gating needs its own exit code and halt text.
8. **OQ-8, the aggregation.** The draft applies §4.2's map, in which void instances do not count, to each variant.
   - *Reviewer recommends:* accept, after the rename of `E` (done: `Ev`).
9. **OQ-9, Lemma PD.** The draft adopts the reduction to "`Γ₁` is a permutation matrix", with the certified definitional
   method on toys (§2.4).
   - *Reviewer recommends:* accept, with the surjectivity line and a certified definitional method. Both are added, and
     the checker requirements are frozen in §2.4 (i)–(iv).
   - *Reviewer: corpus answers* — this is a proof, not a choice. The reviewer checked it in both directions. (Review of
     `1962c378`; the item stays open.)
10. **OQ-10, the controls.** The draft has the 17 gating controls of §3.
    - *Reviewer recommends:*
      - accept all as gating;
      - add CC-SKEW and an S1 toy (added: CC-SKEW, CC-PERM);
      - make EX-SCHEMA two-sided (done);
      - give EX-CERT a case for each clause (done: cases 6–9);
      - add CC-S3NOT, so that S3 reaches NOT (done);
      - add an `n = 3` toy that discriminates the order of `first_mismatch` (not added);
      - add a WF step at `r = 2` at N6's parameters (not added).
11. **OQ-11, the QB readings.** The draft identifies the variant's credence as the QB-2 credence, and `T^{α,O}` as the
    QB-1 target at the cycle horizon (§2.6).
    - *Reviewer recommends:* accept, conditional on B1. The open question is which orbits the invariant prior ranges
      over (OQ-13).
12. **OQ-12, the governance form.** One option is a research run on a disposable branch, not a §A.39 native V3 round:
    no `v3-round` or `v3-governed-paths` block, `F` the owner-designated exact commit, and the files placed as listed
    in the header. The other is a native V3 round. §7 states the consequences of each.
    - *Reviewer recommends:*
      - accept the research-run form if the result is for the record only;
      - use a native V3 round if the result is to support the O-OBSMU μ-number proposal (BSB §5.2);
      - under the research-run form, state that the run is not §A.39-protocol-valid and supports no status change by
        itself. This draft now states it in §7.
13. **OQ-13, the candidates and the support of the credence prior.**
    - (i) Are the candidates for `O*` the long orbits, or the long orbits that carry history readback (`Long′`)?
    - (ii) Does QB-2's invariant prior range over all orbits, or over the candidate orbits only?
    - The answer is one of `13a`–`13d`. It selects the C-1 verdict by the table of §4.2, and the other three variants are
      recorded.
    - An answer outside the table is written in as a new variant before `F` (§4.2).
    - *Reviewer recommends:* that the owner decide it. The review's B1 shows that the R0 verdict alone does not settle
      it.
    - *Reviewer: corpus answers* — the corpus leans but does not force. (Review of `1962c378`; the item stays open.)
      - On part (ii): Main:56 (Lemma 3, clause 2) and posit (iv) state the global counting prior, which favours 13a or
        13b. But BSB N4 shows that clauses 1 and 2 conflict for non-transitive `φ`, and QB-2 left the prior's source
        open.
      - On part (i): Main:74 makes (C1) the hidden-influence diagnostic, and a permutation orbit has no hidden influence,
        which supports `Long′`. Nothing in the corpus excludes such orbits outright.
    - Under 13c or 13d, Lemma V′ applies: the selected variant tests whether the candidate orbits agree with one another
      (§4.1, §9).
14. **OQ-14, the rerun policy for a runner failure before step (a) starts.** For example, provisioning, checkout or
    environment set-up fails, and no output exists. `run_attempt = 1`, with no exception, would let such a failure
    spend the freeze.
    - Options: no rerun, so the freeze is spent; or a second dispatch, recorded with the failed run's id under a new
      owner approval, with the invariant restated as "the check step ran in exactly one attempt".
    - *Reviewer recommends:* add the policy, as an owner decision, never a silent rerun.

### 8.3 Points in the source sketch that cannot be frozen as stated

These are the points of BSB:404–416 that needed a choice, with the choice this draft makes.

1. **"`ℓ_min` fixed in advance."** No source fixes a value, and Main:62's "small p" is unquantified. The draft uses
   `n + 1` (§2.5, OQ-1). The sketch's rule is also one-sided: it restricts the candidates but not the credence. The
   draft therefore freezes four variants and leaves the choice to OQ-13.
2. **"A declared region R" and "small L".** The sketch fixes neither the visible content of a site nor the sizes. At
   `d = 1`, `L ≥ 3` is needed for distinct neighbours, and Theorem 22's hypotheses fit the budget only at `L = 8`. The
   draft's choices are in §2.1–§2.2 (OQ-2, OQ-4).
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
  - C-1 asks only whether the native wave dynamics behaves like that at the eleven frozen sizes: `d = 1`, `a = 1`,
    `q ∈ {2, 3}`, `L ≤ 8`, one contiguous region, and the visible content fixed by OQ-2.
  - Neither verdict extends to larger `L`, to `d ≥ 2`, to the manuscript instance `d = 3` (§2.1), to other couplings,
    to the rounded rule, or to other regions or splits.
  - At `d = 1` the instances are outside posit (v)'s splitting clause (`d ≥ 2`, BSB:225; Main:726).
- **Cycle horizon only.** By Lemma A, the frequencies compared are those over a whole cycle of the orbit. A cycle is of
  order up to the recurrence time, which no accessible window reaches (BSB:259; Main:141). C-1 says nothing about
  accessible-window frequencies, which are C-3's subject.
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
  - A FREQ with `shared_rows ≥ 1` shows that at least one row's credence pools two or more orbits and the candidates
    still match. It does not show that every row was a non-trivial comparison. `shared_rows` is recorded for that
    reason.
- **The variants are frozen.**
  - Which variant answers C-1's question is a question about the prior and the candidates, not a computation (OQ-13).
  - The four variants are frozen before the result. The C-1 verdict is the one the OQ-13 answer selects, and no variant
    outside the four can be adopted from this run.
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
- **P-divisibility record.** By Lemma PD the record is a function of whether `T^{α,O}` is a 0/1 matrix. It adds no
  information independent of the comparison data and carries no verdict.
- **Calibration of the tool.** The controls are constructed toys with hand-derived values. A complete run shows that
  the implementation reproduces them, and that the native `φ` matches the hand-derived steps. It does not show that the
  rule behaves as intended on inputs unlike the controls. Without RX-ORD gating (OQ-7), an orbit-fragmenting bug that
  still partitions `S` is not caught on native instances.
- **Consistency axis.** Whatever the verdict, it moves no correctness band (§A.23). A halted run establishes nothing
  about the wave substratum.
