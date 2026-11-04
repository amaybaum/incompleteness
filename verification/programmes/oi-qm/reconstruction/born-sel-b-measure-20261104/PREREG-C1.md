# BORN-SEL C-1 preregistration: single-orbit frequencies against the Born-form weights on small wave substrata (#1059, part (b))

**Status.** WIP / UNVERIFIED preregistration, draft r2. Revised after the independent review of `3be25e7f` (ACCEPT WITH
CHANGES); not re-reviewed. Paper only; nothing has been run or written as code, and no native instance has been
enumerated. Candidate freeze: it becomes frozen when the owner designates an exact commit `F` that carries this file
and its three data files. **Not authorized to run.** A run needs the owner's go on the reviewed `F`, then the tool, then
its review, then a separate dispatch approval (§7).

- **Frozen inputs at `F`**, all in `verification/programmes/oi-qm/reconstruction/born-sel-b-measure-20261104/`, beside
  the assessment (§A.36):
  - this file, `PREREG-C1.md`;
  - `C1-INSTANCES.json`, the instance list, order, encodings, explicit toy maps, unit-control inputs and the wave rule's
    parameters;
  - `C1-CONTROLS-EXPECTED.json`, the hand-derived expected values of every control and mutation;
  - `C1-OUTPUT-SCHEMA.json`, the machine-readable schema of every output file and of the expected file.
- **Source.** `BORNSEL-B-MEASURE.md` r3, accepted at `7b46d36c` (review `REVIEW-7b46d36c.md`: ACCEPT). Its §7 C-1 sketch
  (lines 404–416 of that file) is the specification frozen here. Base for every corpus citation: `origin/main`
  `1609dc440f5a12d05b750f6d894bb91d09a099a3`.
- **Authorization.** Owner, chat 2026-11-04, #1059 c.6624262539: draft, but do not run, a frozen preregistration for
  C-1. The run is a separate later decision.
- **Owner decisions consumed.** QB-1 and QB-2 (§2.6).

**Support labels.**
- **[P]** a quotation of, or citation to, a source at the base: a manuscript line (`Main:N`, `SM:N`, `Substratum:N`),
  a Lean declaration with file:line, or a line of the assessment (`BSB:N`, the line in `BORNSEL-B-MEASURE.md` at
  `7b46d36c`). The assessment labels its own derivations [D]; they are cited here as accepted at `7b46d36c`, not as
  kernel-checked.
- **[D]** a derivation or a specification choice made in this file. Unreviewed.
- **[O]** an owner decision.

**Notation.**
- The Lean wave rule's coupling coefficient is named `α` (`SubstratumInterfaceAudit.lean:160`), and the assessment's
  measure branch is also α. In this file the **coupling coefficient is written `a`**, and α always means the measure
  branch "uniform on the actual orbit" [D].
- `F` and `E` keep their §A.39 meanings (the frozen commit; the certified execution head). The set of evaluated native
  instances is written `Ev` (§4.2).

***

## 1. Objective and non-objectives

**Objective.** By exhaustive exact enumeration over ℚ, on small instances of the manuscripts' wave substratum, decide
for each instance whether "β's one-step numbers are single-orbit frequencies" (BSB:406). That is, decide whether, for
every orbit `O` of `φ` with `|O| ≥ ℓ_min`, the orbit's cycle transition frequencies `T^{α,O}` equal the Born-form matrix
`T^β` on every visible row the orbit visits. On the same instances:
- record per orbit whether the α-rooted family is P-divisible on `{0, …, |O|}` (BSB:411, B4);
- record two secondary verdicts, S1 and S2 (§4.1), each fixed here as a deterministic function of the per-orbit record.

**What the question is, in the owner's terms [D].**
- Under QB-2, the embedded observer's assignment given the present visible value `x₀ = a` is the invariant
  maximal-entropy prior conditioned on that record, which is `unif({a} × 𝒞_H)` (BSB:206–208: γ-c with a present-visible
  record). Its one-step numbers are `T^β` (Main:117, Main:288–290).
- Under QB-1 the physical target is operational frequencies. By BSB:239–241 (Lemma A), the transition frequencies along
  the actual trajectory over a whole cycle of the actual orbit `O*` are `T^{α,O*}`.
- C-1 asks, on native instances, whether these two coincide for every orbit that the corpus admits as a candidate `O*`.

**Non-objectives.** The run does not cover:
- accessible-window frequencies (C-3, deferred until after QB-1; BSB:424);
- any Lean work (C-2);
- `d ≥ 2`, `d = 3`, the rounded (nonlinear) rule, or a coupling other than `a = 1`;
- record-constrained measures beyond the present-visible record;
- any selection of a measure, a new premise, a manuscript edit, a status change, merge or publication.

**What a completed run establishes.** For each evaluated native instance, at the frozen sizes and conventions, the
primary verdict is one of:
- FREQ: every long orbit's cycle frequencies equal `T^β` on its visited rows;
- NOT: some long orbit's do not;
- VOID_NO_ORBIT: no orbit is long.

The run also records S1 and S2 and the per-orbit P-divisibility. This is a result on the consistency axis (§A.23): it
compares objects the framework itself defines and confronts no external measurement.

**What it does not establish.** See §9. In particular, it does not select a measure, does not bear on accessible
windows, and does not extend beyond the frozen instances.

***

## 2. Frozen preconditions

### 2.0 Conventions common to every instance

- **Arithmetic.** All counts are exact integers. A probability is a pair of integers reduced to lowest terms. Equality
  of two probabilities `x/y` and `u/v` is decided by `x·v = u·y` on integers. No floating-point value enters the
  computation, the comparison or the verdict path. One appearing in an output probability field is a schema violation
  (exit 2) [D].
- **Configurations.** Every toy or native instance is a finite set `S = 𝒞_V × 𝒞_H` with `n = |𝒞_V|` and `m = |𝒞_H|`. A
  state is an integer `s ∈ {0, …, nm − 1}`, with visible value `π_V(s) = s mod n` and hidden value `s div n`, so
  `s = v + n·h` [D].
- **Map.** `φ` is given as an array `φ[s]` over all of `S`: by an explicit table for toy instances
  (`C1-INSTANCES.json`), and by the wave rule of §2.1 for native instances.
- **Enumeration method.** Full: every state of `S`, for every instance. No sampling, no sequential method.
- **Budget check.** Before any enumeration, the tool checks `state_count = n·m ≤ 2¹⁶` from the frozen parameters
  (exit 7 otherwise).
- **Bijectivity check.** For every toy and native instance the tool first checks that `φ` is injective on `S`. A failure
  exits 5 before any other field of that instance is computed. For mutation M-INJ, which is expected non-injective, the
  detection is the compared field (§3.3).
- **Orbits.** The orbits are the cycles of `φ`. An orbit's representative `rep(O)` is its least state index, and orbits
  are listed in increasing `rep`. `|O|` is the cycle length. `ord(φ)` is the least common multiple of the cycle lengths.
- **Permutation-matrix test [D].** A matrix `M` with rows indexed by `W` and columns by `𝒞_V` is a **permutation matrix
  on `W`** iff:
  - every entry `M(a, j)` with `a, j ∈ W` is `0` or `1`;
  - every row sum over `j ∈ W` is `1`, and every column sum over `a ∈ W` is `1`;
  - `M(a, j) = 0` for every `a ∈ W` and `j ∉ W`.

  For `T^β`, `W = 𝒞_V`. For `T^{α,O}`, `W = V_O` (§2.3).

### 2.1 The native wave substratum [P, with file:line]

- **Structure.** A substratum is a site type `ι` with translations, an additive alphabet `V`, and a second-order rule
  `R` (`SubstratumInterfaceAudit.lean:60`). Its configuration space is the phase-space form `ι → V × V`
  (`SubstratumInterfaceAudit.lean:78`), and its dynamics is `φ := leapEquiv R.F` (`SubstratumInterfaceAudit.lean:81`).
- **The step.**
  - `leapEquiv F x = leap F x` (`SecondOrderCircuit.lean:117–118`).
  - `leap F x i = ((x i).2, F (curOf x) i − (x i).1)` (`SecondOrderCircuit.lean:67–68`), with `prevOf x i = (x i).1`
    and `curOf x i = (x i).2` (`SecondOrderCircuit.lean:48, 51`).
  - So the per-site pair is `(prev, cur)` and the step is `(p, c) ↦ (c, F(c) − p)`. This is the manuscripts'
    second-order form `x_i(t+1) = f(neighbours of i at t) − x_i(t−1) mod q` (SM:106, SM:228).
- **The rule.**
  - `waveF α c i = α * ∑_{p : Fin d × Bool} c (i + dir p)` (`SubstratumInterfaceAudit.lean:160–161`), with
    `dir (k, true) = +e_k` and `dir (k, false) = −e_k` (`SubstratumInterfaceAudit.lean:142–143`).
  - The manuscript form is `f = α(x₁ + ⋯ + x_{2d}) mod q` (SM:228).
  - SM Appendix A writes the `d = 1` ring with coefficient 1:
    `x(n, t+1) = x(n−1, t) + x(n+1, t) − x(n, t−1) (mod q)` (SM:1602).
- **The lattice and the boundary.** Sites `Fin d → ZMod L`, the periodic torus; alphabet `ZMod q`
  (`SubstratumInterfaceAudit.lean:177–180`, with the docstring at :175–176: "the manuscripts' rule on a finite cubic
  torus with alphabet ℤ/qℤ"). Boundary conditions are therefore periodic.
- **Kernel facts used as controls.**
  - `φ` is a bijection (`waveSubstratum_A2`, `SubstratumInterfaceAudit.lean:190`).
  - The rule commutes with translations (`waveSubstratum_A4Exact`, :202).
  - The rule is additive (`waveSubstratum_A5`, :211).
  - `φ` fixes the zero configuration (`waveSubstratum_phi_fixes_zero`, `StochasticInterface.lean:101`).
  - The wave substratum is not transitive (`waveSubstratum_stochastic_interface_gap`, `StochasticInterface.lean:191`).
- **The frozen instance of the rule [D, from the above].** `d = 1`, `a = 1`, ring of `L` sites, `q ∈ {2, 3}`. At site
  `i`, with indices mod `L`:
  - `p′_i = c_i`;
  - `c′_i = (c_{i−1} + c_{i+1} − p_i) mod q`.

  The Lean sum ranges over `p : Fin 1 × Bool`, so both terms are always present. `L ≥ 3` is required so that
  `i − 1 ≠ i + 1` and the two neighbours are distinct sites. At `L = 2` the sum is `2c_{i+1}`, and at `L = 1` it is a
  self-coupling, which center independence excludes (SM:228) [D].
- **How the `d = 1` instance relates to the manuscript instance.**
  - The kernel names the manuscript instance as "`α = 1`, `d = 3`" (`PhysicalC4Discharge.lean:570–571`). C-1 does not
    run that instance [D].
  - The kernel's `waveSubstratum d L q α` is one definition, uniform in `d`. The `d = 1` instances are members of the
    same family with the same coefficient `a = 1`, and the kernel facts above hold for every `d`.
  - The manuscript instance is out of budget. At `d = 3` the neighbours along an axis are distinct only for `L ≥ 3`,
    which gives `|S| = q^{2·27} ≥ 2^{54}`. At `L = 2` they coincide, and at `q = 2` the rule degenerates to
    `c′ = −p` [D].
  - **The coefficient.** At `d = 1`, SM:1602 writes the ring with coefficient 1. SM:230 shows that `α = 1/d` is the
    coefficient that makes the real harmonic lift gapless, and places that normalisation at observer level rather than
    in the substratum update. At `d = 1`, `1/d = 1`, so the substratum coefficient and the observer-level normalisation
    coincide. At `d = 3` they do not (`1` against `1/3`). The `d = 1` instances therefore do not stand in for the
    `d = 3` instance's coefficient reading [D].
- **The visible/hidden split [P].**
  - The kernel's cut realization takes "the visible carrier [as] the region's phase-space data, the hidden carrier the
    complement's, and the step is `𝒮.φ` transported along the split" (`PhysicalC4Discharge.lean:578–581`, def
    `cutRealization` at :582).
  - The region `Vs` is a parameter, and "[SM] Theorem 22 quantifies over connected regions with `|V| ≤ N/3`"
    (`PhysicalC4Discharge.lean:561`; SM:1376).
- **The frozen region [D].**
  - `R = {0, 1, …, r−1}`, a contiguous block of `r` sites, with `r ≤ L/3`.
  - The visible configuration is the `(prev, cur)` pair at each site of `R`, so `n = q^{2r}`. The hidden configuration
    is the pair at each site outside `R`, so `m = q^{2(L−r)}`.
  - Because the rule commutes with translations (A4Exact), every contiguous block of `r` sites gives the same instance
    up to relabelling. The block at the origin is chosen.
- **The state encoding [D].** Site digit `δ_i = p_i·q + c_i ∈ {0, …, q²−1}`; state index `s = Σ_i δ_i·(q²)^i`. Then
  `π_V(s) = s mod q^{2r}` and the hidden value is `s div q^{2r}`, consistent with §2.0's `s = v + n·h`.
- **Two implementations [D].** The tool computes `φ` twice:
  - (i) by the site loop above;
  - (ii) as the linear map `F = [[0, I], [−I, A]]` on `(p, c) ∈ (ℤ/q)^{2L}`, with `A` the circulant ring adjacency
    (SM:1602), applied to the digit vector.

  The two arrays must be identical on all of `S` (exit 4 otherwise).

### 2.2 Native instances and sizes [D]

Native instances run in this order (increasing `|S|`, ties by `q`, then `r`). `|S| = q^{2L}`.

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
  (`3^{10} = 59,049`); `L = 6` (`3^{12} = 531,441`) is excluded.
- **Region sizes.** `r ≤ L/3` gives `r = 1` for `L ≤ 5` and `r ∈ {1, 2}` for `L ∈ {6, 7, 8}`.
- **W-q2-L7-r2 is excluded in this draft.**
  - By SM Theorem A.1 (SM:1604–1606, "For q prime with gcd(L, q) = 1 — q = 2 included: ord(F mod q) = qL"), every orbit
    length divides `qL = 14 < 17 = ℓ_min`, so that instance would be void by construction.
  - This uses the theorem's statement only; no orbit of any instance was computed [D].
  - The exclusion is open as OQ-4, where the reviewer recommends reinstating the instance.
- **Coprime and non-coprime.** N1, N4, N7, N8 and N9 satisfy `gcd(L, q) = 1`, inside Theorem A.1's scope. The others
  have `q | L`, where the parabolic Jordan blocks of SM Appendix A are present. Both kinds are included.
- **Theorem 22's hypotheses [P, SM:1376].**
  - The hypotheses are "connected bounded-degree coupling graph with diameter D ≥ 4 … any connected subgraph V with
    |V| ≤ N/3".
  - Every frozen `R` is connected and has `|R| ≤ N/3`. These two properties are checked from the frozen parameters
    (exit 2 if violated).
  - The ring's diameter `⌊L/2⌋` is at least 4 only at `L = 8` (N10, N11). It is recorded per instance as
    `diameter_ge_4`.
  - C-1 asserts nothing about (C1) on these instances. Theorem 22's own proof step for (C1) uses only `∂V ≠ ∅`
    (SM:1378), and that is SM's statement, not a C-1 result.
  - `beta_is_permutation = false` is a sufficient witness of (C1) only (Main:74). It is recorded, and it is not a
    checkpoint for (C1).

### 2.3 The compared objects [D, from the cited definitions]

For an instance with map `φ` on `S = 𝒞_V × 𝒞_H`:

- **Counts.** `c(a, j) := #{h ∈ 𝒞_H : π_V φ(a, h) = j}`. For an orbit `O`:
  - `c_O(a, j) := #{h : (a, h) ∈ O, π_V φ(a, h) = j}`;
  - `n_a(O) := #{h : (a, h) ∈ O}`.
- **`T^β`, the Born-form matrix.** `T^β(a, j) := c(a, j)/m` for every `a, j ∈ 𝒞_V`. This is:
  - Main:117's `T_ij`;
  - the matrix of the Born-form theorem (Main:288–290);
  - `Γ^κ_1` with `κ_a` uniform on `𝒞_H` (BSB:126).
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
- **Orbit equality.** `eq(O)` holds iff `T^{α,O}(a, j) = T^β(a, j)` for every `a ∈ V_O` and every `j ∈ 𝒞_V`, i.e. iff
  `c_O(a, j)·m = c(a, j)·n_a(O)` for all such `(a, j)`. If `eq(O)` fails, its **first mismatch** is the
  lexicographically least `(a, j)` (`a`-major) with inequality, reported with both values.
- **The orbit-level C4 predicate (for S1).** `long_c4(O)` iff `long(O)` and `T^{α,O}` is not a permutation matrix on
  `V_O`.
  - By Lemma PD (§2.4), this is `long(O) ∧ ¬pdiv_alpha(O)`.
  - A long orbit with a permutation `T^{α,O}` has a deterministic visible process on the orbit, with no readback gap
    below `|O|` (Main:74; Main:141, transported to the root-dependent κ by BSB:147–154) [D].
- **`T^{β_long}`, the credence restricted to the long orbits (for S2).**
  - `U_long := ⋃_{O ∈ Long} O`, and `W_long := ⋃_{O ∈ Long} V_O`.
  - For `a ∈ W_long` and every `j`: `T^{β_long}(a, j) := Σ_{O ∈ Long} c_O(a, j) / Σ_{O ∈ Long} n_a(O)`.
  - These are the one-step numbers of `unif(U_long)` conditioned on `x₀ = a`, the same construction as γ-c
    (BSB:206–208) with the prior's support restricted to `U_long` [D].
  - When `Long = ∅`, `T^{β_long}` is the empty map.
  - `eq_beta_long(O)` is defined for `O ∈ Long`, as for `eq(O)` with `T^{β_long}` in place of `T^β`. Its first mismatch is
    defined in the same way.
- **Mixture identity (an internal check, not a hypothesis) [D].**
  - Because the orbits partition `S`, `Σ_O c_O(a, j) = c(a, j)` and `Σ_O n_a(O) = m` for every `a, j`.
  - Hence `T^β(a, ·) = Σ_{O ∋ a} (n_a(O)/m)·T^{α,O}(a, ·)`.
  - The tool computes `c` directly over the `(a, h)` grid and separately as the orbit sum. The two must agree exactly
    (exit 4 otherwise).
- **Double stochasticity [P, Main:62].**
  - Main:62: "the marginal of a bijection under the uniform prior is doubly stochastic, since each set `{x_j} × 𝒞_H`
    has exactly `|𝒞_H|` preimages".
  - So `Σ_j c(a, j) = m` and `Σ_a c(a, j) = m`. This is checked, and a failure exits 4.

### 2.4 P-divisibility (B4)

- **The kernel definitions [P].**
  - `PDivisible K Γ := ∀ s t, s < t → t ≤ K → ∃ Λ, IsRowStochastic Λ ∧ Γ t = Γ s * Λ` (`CausalReadback.lean:54`).
  - `IsRowStochastic` is defined at `CausalReadback.lean:48`.
  - The rooted maps with a shared prior are `rootedMap R t a j = Σ_h [π_V(step^t(a, h)) = j]·prior h`
    (`CausalReadback.lean:190`).
- **The α-rooted family on an orbit [D].** For `t ≥ 0` and `a, j ∈ V_O`:
  `Γ^{α,O}_t(a, j) := #{h : (a, h) ∈ O, π_V φ^t(a, h) = j} / n_a(O)`.
  - It is square on `V_O` and row-stochastic.
  - `Γ^{α,O}_0 = I`, and `Γ^{α,O}_1` is `T^{α,O}` restricted to `V_O`.
  - `Γ^{α,O}_{|O|} = I`, because `φ^{|O|}` is the identity on `O`.
  - Its rows are indexed by `V_O` only, because α gives no hidden conditional on an unvisited root. BSB:147 lets `κ_a`
    be arbitrary there for the implication, which would make a full-`𝒞_V` record depend on an arbitrary choice.
  - The restriction to `V_O` is open as OQ-5.
- **The recorded quantity.** `pdiv_alpha(O) := PDivisible |O| Γ^{α,O}`, on `V_O`, horizon `{0, …, |O|}` (BSB:411).
- **The β family [D].**
  - `Γ^β_t(a, j) := #{h : π_V φ^t(a, h) = j}/m` on `𝒞_V`. This is the kernel's `rootedMap` for the cut realization
    with the uniform prior.
  - `pdiv_beta := PDivisible ord(φ) Γ^β`, horizon `{0, …, ord(φ)}`, where `Γ^β_{ord(φ)} = I`.
  - It is required on CE-8. On native instances it is recorded, and whether to record it there is open as OQ-6.
- **Lemma PD [D; one direction kernel-checked for β].** Let `Γ_t` be either family above, on its row set `W` (`V_O` or
  `𝒞_V`), with return time `N` (`|O|` or `ord(φ)`), so `Γ_N = I`. Then `PDivisible N Γ` holds iff `Γ_1` is a
  permutation matrix on `W`.
  - **(PDivisible ⇒ Γ₁ permutation), by contraposition.** Suppose `Γ_1` is not a permutation matrix.
    - Then `N ≥ 2`, since `Γ_1 = I` when `N = 1`.
    - A row-stochastic `Λ` with `Γ_N = Γ_1 Λ = I` would be a stochastic right inverse of `Γ_1`. Main:133 forbids this:
      "If a finite square stochastic matrix has a stochastic left or right inverse, then it is a permutation matrix"
      (kernel `isPermMatrix_of_stochastic_inverse`, `EquivalenceChain.lean:110`). So the pair `(1, N)` fails.
    - **For β the whole direction is kernel-checked:** `pIndivisible_of_return_nonperm`
      (`RootedRecurrenceBridge.lean:93`), with `s = 1`, `n = ord(φ)`, `hreturn` the identity `φ^{ord(φ)} = id` on `S`
      and `R` the cut realization with the uniform prior, concludes `PIndivisibleWithin (ord φ) (rootedMap R)`.
    - For α the family has a root-dependent κ and is not a kernel `rootedMap`. That case rests on the matrix lemma
      plus this paragraph [D].
  - **(Γ₁ permutation ⇒ PDivisible).** Suppose `Γ_1` is a permutation matrix `P_f`, with `f` a bijection of `W`.
    - For α: every `(a, h) ∈ O` has `π_V φ(a, h) = f(a)`. So along the cycle `x_{k+1} = f(x_k)`, hence
      `π_V φ^t(a, h) = f^t(a)` and `Γ_t = P_{f^t}`.
    - For β: `π_V φ(b, h′) = f(b)` for every `b, h′`. So by induction on `t`, `π_V φ^t(a, h) = f^t(a)`, and again
      `Γ_t = P_{f^t}`.
    - Then `Λ_{s,t} := P_{f^s}^{T} P_{f^t} = P_{f^{t−s}}` is a permutation matrix, so row-stochastic, and
      `Γ_s Λ_{s,t} = Γ_t` for every `s < t ≤ N`.
  - **Γ₁ deterministic on `V_O` is equivalent to Γ₁ being a permutation matrix on `V_O`.**
    - Every `b ∈ V_O` has a predecessor on the cycle `O`. So if `Γ_1^{α,O}` is deterministic, with
      `π_V φ(a, h) = f(a)` on `O`, then `f : V_O → V_O` is onto, hence bijective, and `Γ_1^{α,O} = P_f`.
    - Therefore, on these horizons, `pdiv_alpha(O)` holds iff `T^{α,O}` is a 0/1 matrix on `V_O`, and `pdiv_beta` holds
      iff `T^β` is a permutation matrix.
  - The B4 record is therefore a function of the comparison data. It is recorded because BSB:411 asks for it, and it
    carries no independent verdict.
- **How the tool computes it.**
  - On every toy and native instance, by Lemma PD, with witness `(s, t) = (1, N)` when it fails.
  - On every toy control, also by the definition, through the certified method below. The two methods must agree, and
    both must match the hand-derived values (exit 1 on a mismatch with the expected value, exit 4 on disagreement
    between the methods). This is the countercontrol for Lemma PD.
- **The definitional method, frozen, with certificates [D].**
  - **Indexing.** For a pair `s < t ≤ N` on the row set `W = (w_0, …, w_{k−1})` (ascending), the unknown is
    `x ∈ ℚ^{k²}` with `x_{i·k+j} = Λ(w_i, w_j)`. The constraints are `A x = b`, `x ≥ 0`, with `k² + k` rows in this
    order:
    - row `ai·k + j` (`ai, j < k`): `Σ_i Γ_s(w_ai, w_i)·x_{i·k+j} = Γ_t(w_ai, w_j)`;
    - row `k² + i` (`i < k`): `Σ_j x_{i·k+j} = 1`.
  - **Pair order.** Pairs are taken in lexicographic order of `(s, t)`. The family is declared P-divisible iff every pair
    is feasible. The search stops at the first infeasible pair.
  - **Search.** Any exact rational method may produce the candidate: exact phase-I simplex with Bland's rule, or
    `Λ = Γ_s^{−1}Γ_t` when `Γ_s` is invertible. **No candidate is trusted.** A pair's result counts only through its
    certificate, which the tool's independent checker verifies with exact rational arithmetic:
    - **feasible:** the certificate is `Λ` (`kind = "lambda"`). The checker verifies that every entry is `≥ 0`, that
      every row of `Λ` sums to 1 and that `Γ_s Λ = Γ_t` entrywise;
    - **infeasible:** the certificate is a Farkas vector `y ∈ ℚ^{k²+k}` (`kind = "farkas"`). The checker verifies that
      `(Aᵀ y)_v ≥ 0` for every `v < k²` and that `bᵀ y < 0`.
  - **Emitted certificates.** For a P-divisible family, the certificates are the `Λ` for every pair. Otherwise they are
    the `Λ` for every pair before the first infeasible pair, and the Farkas vector for that pair.
  - **The certificate file.** Every certificate is written to `c1/<id>.pdiv-certs.json` (schema
    `#/$defs/pdiv_certs`).
  - **Failures.** A certificate that fails verification, or a pair with no certificate, exits 4.
  - **Example [D, a valid certificate, not a compared value].** CE-8, `O_B`, pair `(1, 4)`: `Γ_1 = J/2`, `Γ_4 = I`,
    `k = 2`. The vector `y = (−1, 0, 1, 0, 0, 0)` has `Aᵀy = 0` and `bᵀy = −1`. This is control EX-CERT case 1 (§3.3).

### 2.5 `ℓ_min` (fixed before any result) [D; owner item OQ-1]

- **What the corpus says [P].**
  - Main:62: "the atypical short orbits of the idealized linear dynamics (fixed points, low-period cycles) are precisely
    observer-lacking substrata — an orbit of period `p` makes at most `p` states dynamically accessible, so for small `p`
    no partition of it can satisfy the high-capacity condition C3".
  - C3 is `log₂|𝒞_H| ≥ I*` (Main:78).
  - The corpus does not quantify "small `p`".
- **The frozen rule [D].** `ℓ_min(I) := n_I + 1`, where `n_I = |𝒞_V|` of instance `I`. It depends only on the instance's
  declared parameters, so it is fixed before any result.
- **Justification [D].**
  - By pigeonhole, an orbit with `|O| ≥ n + 1` revisits some visible value, so `n_a(O) ≥ 2` for some `a`: some root
    carries at least two hidden states on the orbit.
  - An orbit with `|O| ≤ n` can have `n_a(O) = 1` at every visited root. Then `T^{α,O}` is deterministic and no hidden
    state on the orbit mediates anything. That is the weakest form of the C3 failure Main:62 describes: the
    orbit-restricted hidden capacity `log₂ max_a n_a(O)` is 0.
  - `n + 1` is the least length at which that capacity is guaranteed positive at some root by length alone. It is a
    necessary condition, not a sufficient one, for an orbit to be observer-bearing.
  - It is consistent with the assessment's control. In CE-8, `n = 2` and `ℓ_min = 3`, so both orbits (length 4) count,
    as BSB:137 requires: "no period-based or C3-based exclusion … separates them".
- **Comparison is `|O| ≥ ℓ_min`**, inclusive. Control CC-UNVIS has an orbit of length exactly `ℓ_min`.
- **One-sidedness, and the two frozen secondaries.**
  - `ℓ_min` removes short orbits from the candidates for `O*`, the orbit side, but `T^β` still averages over them, the
    credence side.
  - By the mixture identity, if every long orbit equals `T^β` on its visited rows, then on each row the short orbits'
    `n_a`-weighted aggregate must also equal `T^β`. That includes the kernel-forced fixed point at state 0
    (`waveSubstratum_phi_fixes_zero`), whose row is `δ₀`.
  - Separately, a long orbit whose `T^{α,O}` is a permutation matrix forces NOT wherever `T^β` is not deterministic.
  - S1 and S2 (§4.1) separate these two mechanisms. They are frozen now, so that neither can be chosen after the result.
  - Whether the credence prior should range over all orbits or over observer-bearing ones only is open as OQ-13.
- **No other threshold yields a verdict.** Every orbit's `eq(O)` and `|O|` are recorded, so the record would support
  other thresholds. This run issues verdicts only at the frozen `ℓ_min`, for the primary verdict and for S1 and S2. Any
  other threshold or variant needs a new freeze.

### 2.6 Owner decisions, and how this preregistration reads them [O, with readings D]

- **QB-1 [O].** "Operational frequencies are the physical target; observer credences cannot by themselves establish a
  Born law."
  - Reading [D]: the target of C-1's comparison is `T^{α,O}`, the cycle frequencies (Lemma A, BSB:240–241).
  - A FREQ verdict would show that the Born-form numbers coincide with that target for every long orbit on the instance.
    It does not establish a Born law (§9).
- **QB-2 [O].** "γ is read as an invariant prior followed by conditioning, with the prior's physical source left open."
  - Reading [D]: with the present-visible record `x₀ = a`, γ read this way is `unif(U_r)` conditioned on `A_r`. That is
    `unif({a} × 𝒞_H)` (BSB:209–216), whose one-step numbers are row `a` of `T^β`.
  - C-1 takes `T^β` as the credence side and is silent on the prior's physical source.
  - Which orbits the invariant prior ranges over is not fixed by QB-2. S2 records the restriction to long orbits, and
    the choice is open as OQ-13.

***

## 3. The frozen control set

The expected values are hand derivations of constructed toys, frozen in `C1-CONTROLS-EXPECTED.json`. §A.29's "rule, not
numbers" applies to the native decision rule of §4, which is frozen without reference to any native value. **No expected
value is given for any native instance.**

**Execution order.**
- The 16 controls and mutations run first, in the order of `C1-INSTANCES.json` (orders 1–16):
  - the nine toys of §3.1;
  - M-INJ, EX-ARITH, EX-SCHEMA and EX-CERT;
  - WF-q2-L5, WF-q3-L4 and WF-0.
- The 11 native instances follow (orders 17–27, in §2.2's order).
- Native instances run only if every control and mutation has matched. A mismatch halts the run before any native
  instance is evaluated, so no native verdict is ever printed over a failed control (§A.29).

### 3.1 Toy controls (explicit maps; `s = v + n·h`)

| id | `n`, `m` | `φ` as an array over `s = 0, 1, …` | Purpose |
|---|---|---|---|
| CE-8 | 2, 4 | `[1, 2, 3, 0, 6, 7, 5, 4]` | the assessment's counterexample (BSB:129–138); must give NOT |
| TT-4 | 2, 2 | `[1, 3, 0, 2]` | transitive toy, A2 (BSB:246); must give equality |
| TT-6 | 3, 2 | `[1, 4, 3, 5, 2, 0]` | transitive toy with unequal rows and `n = 3` |
| CC-TWIN | 2, 4 | `[1, 3, 0, 2, 5, 7, 4, 6]` | non-transitive, two matching orbits; FREQ must be reachable |
| CC-SHORT | 2, 4 | `[1, 3, 0, 2, 4, 6, 5, 7]` | short orbits that balance, excluded by `ℓ_min` |
| CC-UNVIS | 3, 2 | `[1, 3, 5, 4, 0, 2]` | a long orbit with an unvisited row; orbit length exactly `ℓ_min`; S1 void |
| CC-VOID | 2, 1 | `[1, 0]` | no orbit reaches `ℓ_min`; void takes precedence over equality |
| CC-SKEW | 2, 3 | `[1, 3, 0, 2, 4, 5]` | short orbits that skew `T^β`: primary NOT, S2 FREQ (B1) |
| CC-PERM | 2, 6 | `[1, 2, 3, 0, 5, 7, 4, 6, 8, 9, 10, 11]` | a long orbit with a permutation `T^{α,O}`: primary NOT, S1 FREQ, S2 NOT (B1) |

**Hand derivations [D].** In each toy, `ℓ_min = n + 1`.

- **CE-8.** States: `(0,0)=0, (1,0)=1, (0,1)=2, (1,1)=3, (0,2)=4, (1,2)=5, (0,3)=6, (1,3)=7`.
  - Orbits:
    - `O_A` (rep 0): `0→1→2→3→0`, i.e. `(0,0)→(1,0)→(0,1)→(1,1)`, visible `0101`;
    - `O_B` (rep 4): `4→6→5→7→4`, i.e. `(0,2)→(0,3)→(1,2)→(1,3)`, visible `0011`.
  - Next visible values over `h = 0..3`: from root 0, `1, 1, 0, 1`; from root 1, `0, 0, 1, 0`. So
    `T^β = [[1/4, 3/4], [3/4, 1/4]]`, as at BSB:133.
  - `T^{α,O_A} = [[0, 1], [1, 0]]` and `T^{α,O_B} = [[1/2, 1/2], [1/2, 1/2]]`, as at BSB:135–136.
  - The sketch's check: `T^β(0, 1) = 3/4` against `T^{α,O_A}(0, 1) = 1` and `T^{α,O_B}(0, 1) = 1/2` (BSB:414).
  - Primary verdict:
    - `ℓ_min = 3`, so both orbits are long.
    - Both have `eq = false`, with first mismatch `(0, 0)`: `0` against `1/4` for `O_A`, and `1/2` against `1/4` for
      `O_B`. Verdict NOT.
  - Secondaries:
    - S1: `O_A` is a permutation, so `Long′ = {O_B}`. S1 is NOT.
    - S2: `U_long = S`, so `T^{β_long} = T^β`. S2 is NOT.
  - P-divisibility (BSB:153–154):
    - `O_A` is divisible (`Γ₁` = swap, `Γ₂ = I`);
    - `O_B` is not (`Γ₁ = J/2`, `Γ₄ = I`);
    - β is not, with `ord(φ) = 4`.
- **TT-4.** One orbit, `0→1→3→2→0`, i.e. `(0,0)→(1,0)→(1,1)→(0,1)`.
  - `T^β = T^{α,S} = J/2`.
  - Primary, S1 and S2 are all FREQ.
  - α and β are both indivisible. `ord(φ) = 4`.
- **TT-6.** States `(v,h) = v + 3h`. One orbit, `0→1→4→2→3→5→0`, i.e. `(0,0)→(1,0)→(1,1)→(2,0)→(0,1)→(2,1)`, visible
  `011202`.
  - `T^β = T^{α,S} = [[0, 1/2, 1/2], [0, 1/2, 1/2], [1, 0, 0]]`.
  - `ℓ_min = 4 ≤ 6`. Primary, S1 and S2 are all FREQ.
  - α and β are indivisible. `ord(φ) = 6`.
- **CC-TWIN.** Orbits: rep 0, `0→1→3→2→0`; rep 4, `4→5→7→6→4` (the TT-4 pattern on `h ∈ {2, 3}`).
  - `T^β = J/2`, and both orbits give `J/2`.
  - Primary, S1 and S2 are all FREQ, on a non-transitive map.
  - All families are indivisible. `ord(φ) = 4`.
- **CC-SHORT.** Orbits: rep 0, length 4 (TT-4 on `h ∈ {0, 1}`); rep 4, the fixed point `(0,2)`; rep 5, the 2-cycle
  `(1,2) ↔ (0,3)`; rep 7, the fixed point `(1,3)`.
  - `T^β = J/2`: root 0 over `h = 0..3` gives `1, 0, 0, 1`, and root 1 gives `1, 0, 0, 1`.
  - `ℓ_min = 3`, so only rep 0 is long, and it has `eq = true`. Primary FREQ.
  - The short orbits do not match, but they balance (their aggregate on each row is `J/2`):
    - rep 4: `V_O = {0}`, row `[1, 0]`, unvisited `{1}`;
    - rep 5: rows `[[0, 1], [1, 0]]`;
    - rep 7: `V_O = {1}`, row `[0, 1]`, unvisited `{0}`.
  - S1 is FREQ, with `Long′ = {rep 0}`. S2 is FREQ, with `T^{β_long} = J/2`.
  - P-divisibility: rep 0 no; reps 4, 5 and 7 yes; β no. `ord(φ) = 4`.
- **CC-UNVIS.** States `v + 3h`. Orbits: rep 0, `0→1→3→4→0`, i.e. `(0,0)→(1,0)→(0,1)→(1,1)`, visiting rows `{0, 1}`
  only; rep 2, the 2-cycle `(2,0) ↔ (2,1)`.
  - `T^β = [[0, 1, 0], [1, 0, 0], [0, 0, 1]]`.
  - `ℓ_min = 4 = |O|` for rep 0 (the inclusive boundary). Row 2 is unvisited and excluded. On rows 0 and 1, `eq = true`.
    Primary FREQ.
  - A tool that compared the unvisited row, or failed on `n_2(O) = 0`, returns NOT or errors, and the control fails.
  - Secondaries:
    - `T^{α,rep 0}` is a permutation matrix on `{0, 1}`, so `Long′ = ∅` and S1 is VOID_NO_ORBIT.
    - `T^{β_long}` has rows `{0, 1}`: `[0, 1, 0]` and `[1, 0, 0]`. S2 is FREQ.
  - P-divisibility: both orbits yes; β yes (`T^β` is a permutation). `ord(φ) = 4`.
- **CC-VOID.** One orbit, `(0,0) ↔ (1,0)`, of length 2 < `ℓ_min = 3`.
  - The map is transitive and `eq = true`, but the primary verdict is VOID_NO_ORBIT. S1 and S2 are VOID_NO_ORBIT, and
    `T^{β_long}` is the empty map.
  - α and β are P-divisible. `ord(φ) = 2`.
- **CC-SKEW.** States `(0,0)=0, (1,0)=1, (0,1)=2, (1,1)=3, (0,2)=4, (1,2)=5`.
  - Orbits: rep 0, `0→1→3→2→0`, the TT-4 pattern on `h ∈ {0, 1}`, with `T^{α} = J/2`; rep 4, the fixed point `(0,2)`;
    rep 5, the fixed point `(1,2)`.
  - `T^β`: root 0 over `h = 0, 1, 2` gives `1, 0, 0`, and root 1 gives `1, 0, 1`. So `T^β = [[2/3, 1/3], [1/3, 2/3]]`.
  - `ℓ_min = 3`, so only rep 0 is long. `eq = false`, with first mismatch `(0, 0)`: `1/2` against `2/3`. Primary NOT.
  - S1: rep 0 is not a permutation, so S1 is NOT, with the same mismatch.
  - S2: `T^{β_long} = J/2`, so S2 is FREQ. The short orbits skew `T^β`; this is the mechanism of B1.
  - Short orbits: rep 4, row `[1, 0]`, first mismatch `(0, 0)` `1` against `2/3`; rep 5, row `[0, 1]`, first mismatch
    `(1, 0)` `0` against `1/3`. Both are P-divisible.
  - rep 0 and β are indivisible. `ord(φ) = 4`.
- **CC-PERM.** States `v + 2h`, `h = 0..5`.
  - Orbits:
    - rep 0, `0→1→2→3→0`, the CE-8 `O_A` pattern on `h ∈ {0, 1}`, with `T^α = [[0, 1], [1, 0]]`;
    - rep 4, `4→5→7→6→4`, the TT-4 pattern on `h ∈ {2, 3}`, with `T^α = J/2`;
    - reps 8, 9, 10 and 11, the fixed points `(0,4), (1,4), (0,5), (1,5)`.
  - `T^β`: root 0 over `h = 0..5` gives `1, 1, 1, 0, 0, 0`, and root 1 gives `0, 0, 1, 0, 1, 1`. So `T^β = J/2`.
  - `ℓ_min = 3`, so reps 0 and 4 are long. Rep 4 has `eq = true`. Rep 0 has `eq = false`, with first mismatch `(0, 0)`:
    `0` against `1/2`. Primary NOT.
  - S1: rep 0 is a permutation, so `Long′ = {rep 4}`, and S1 is FREQ.
  - S2:
    - `T^{β_long}`: row 0 counts `[0, 2] + [1, 1] = [1, 3]`, giving `[1/4, 3/4]`; row 1 counts `[2, 0] + [1, 1] = [3, 1]`,
      giving `[3/4, 1/4]`.
    - Both long orbits mismatch at `(0, 0)` (`0` against `1/4`; `1/2` against `1/4`), so S2 is NOT.
  - The fixed points do not match `T^β`. Each is P-divisible.
  - Rep 0 is P-divisible; rep 4 and β are not. `ord(φ) = 4`.

### 3.2 Native-faithfulness controls (hand-derived, [D])

These check that the implemented `φ` is the §2.1 rule.
- They run in the control phase, before any native instance, and compute `φ` on the listed states only, with both
  implementations of §2.1.
- A mismatch, or a disagreement between the two implementations, exits 1 and halts.
- WF-0 is a sanity check only: `φ(0) = 0` holds for every additive map, so it is not a faithfulness checkpoint.

The controls:
- **WF-0** (for the parameters of each of N1–N11): `φ[0] = 0` (`waveSubstratum_phi_fixes_zero`,
  `StochasticInterface.lean:101`).
- **WF-q3-L4** (the parameters of N7), from `p = (0,0,0,0)`, `c = (1,0,0,0)`:
  - step 1: `p′ = (1,0,0,0)`, `c′ = (0,1,0,1)`;
  - step 2: `p″ = (0,1,0,1)`, `c″ = (1,0,2,0)`;
  - as state indices: `1 → 741 → 2377`; visible values (`n = 9`): `1 → 3 → 1`.
- **WF-q2-L5** (the parameters of N4), from `p = 0`, `c = (1,0,0,0,0)`:
  - step 1: `p′ = (1,0,0,0,0)`, `c′ = (0,1,0,0,1)`;
  - step 2: `p″ = (0,1,0,0,1)`, `c″ = (1,0,1,1,0)`;
  - as state indices: `1 → 262 → 601`; visible values (`n = 4`): `1 → 2 → 1`.

### 3.3 Mutations and unit controls

- **M-INJ (bijectivity check).**
  - The rule is the §2.1 rule with the `−p` term deleted, `(p, c) ↦ (c, A c)`, at `q = 2`, `L = 3`, `r = 1`. It is
    computed by both implementations: the site loop without `−p_i`, and the linear map `[[0, I], [0, A]]`.
  - Two states with the same `c` and different `p` collide, so `φ` is not injective [D].
  - Expected: `phi_impls_agree = true`, `injective = false`, and `evaluated_beyond_injectivity = false`. If the tool
    reports `injective = true`, the run exits 1.
- **EX-ARITH (exact comparison).** The comparator of §2.3 is applied to frozen pairs:
  - `("1/3", "6004799503160661/18014398509481984")` → unequal. The second value is the IEEE-754 double nearest `1/3`,
    `(2⁵⁴ − 1)/(3·2⁵⁴)`, so a floating-point comparison would report equality;
  - `("2/6", "1/3")` → equal, after reduction to lowest terms;
  - `("3/4", "3/4")` → equal;
  - `("0", "0/5")` → equal.
- **EX-SCHEMA (two-sided).** The output validator of §5 is applied to frozen fragments, each against a named subschema
  of `C1-OUTPUT-SCHEMA.json`. The expected result is `schema_valid` and, for a rejection, `violation_path`, the RFC 6901
  JSON Pointer of the single violating value relative to the fragment's root. Each rejected fragment has exactly one
  violating value.
  1. `probability`, `"1/2"` → valid.
  2. `probability`, `"2/4"` → invalid at `""` (not in lowest terms).
  3. `matrix`, `{"0": ["1/4", "3/4"], "1": ["3/4", "1/4"]}` → valid.
  4. `matrix` (`T_beta`-shaped), `{"0": [0.75, "1/4"]}` → invalid at `/0/0`.
  5. `matrix` (`T_alpha`-shaped), `{"1": ["0", 1]}` → invalid at `/1/1`.
  6. `mismatch`, `{"a": 0, "j": 0, "alpha": "0", "beta": "1/4"}` → valid.
  7. `mismatch` (`first_mismatch`-shaped), `{"a": 0, "j": 0, "alpha": 0.5, "beta": "1/4"}` → invalid at `/alpha`.
- **EX-CERT (the certificate checker of §2.4).** The checker is applied to frozen certificates, with
  `W = {0, 1}`, `k = 2`, and the constraint order of §2.4:
  1. `Γ_s = J/2`, `Γ_t = I`, Farkas `y = (−1, 0, 1, 0, 0, 0)`: `Aᵀy = 0`, `bᵀy = −1`. Valid.
  2. The same pair, `y = 0`: `bᵀy = 0`. Invalid.
  3. The same pair, `Λ = I`: `Γ_s Λ = J/2 ≠ I`. Invalid. This is the false "feasible" that an unchecked solver returned
     in review.
  4. `Γ_s = [[0, 1], [1, 0]]`, `Γ_t = I`, `Λ = [[0, 1], [1, 0]]`: `Γ_s Λ = I`, row-stochastic. Valid.
  5. `Γ_s = J/2`, `Γ_t = J/2`, `Λ = [[2, −1], [−1, 2]]`: `Γ_s Λ = J/2` and the rows sum to 1, but entries are negative.
     Invalid.
- For EX-ARITH, EX-SCHEMA and EX-CERT the comparator, validator and checker are called as units on the frozen inputs.
  The expected outcome is a compared field and does not exit. A different outcome exits 1.
- **The countercontrols built into §3.1.**
  - CC-TWIN: FREQ is reachable on a non-transitive map.
  - CE-8: NOT is reachable.
  - CC-SHORT: `ℓ_min` excludes short orbits.
  - CC-UNVIS: unvisited rows are excluded, and S1 can be void while the primary verdict is not.
  - CC-VOID: the void rule takes precedence over equality.
  - CC-SKEW: S2 separates skewing short orbits from the primary verdict.
  - CC-PERM: S1 separates permutation long orbits, and S1 and S2 differ.
  - The definitional P-divisibility check on every toy is the countercontrol for Lemma PD (§2.4).

### 3.4 Recorded cross-checks (recorded only; not gating, owner item OQ-7)

- **RX-ORD.** For N1, N4, N7, N8 and N9 (`gcd(L, q) = 1`), SM Theorem A.1 states `ord(φ) = qL` (SM:1604–1606; "Verified
  computationally for q = 2, 3, 5, 7, 11, 13 and L ≤ 12", SM:1610).
  - The tool records `ord(φ)` and the boolean `ord_phi_eq_qL`.
  - In this draft a disagreement does not void C-1. It would be a finding about SM Appendix A or the tool, diagnosed
    after the run.
  - Making it gating, which would give it an exit code, is open as OQ-7.

***

## 4. Decision rule

### 4.1 Per native instance (a deterministic map from the computed data)

**Primary verdict (the sketch's rule, BSB:406–410).**
1. If `Long(I) = ∅`: `verdict(I) = VOID_NO_ORBIT`.
2. Otherwise, if `eq(O)` holds for every `O ∈ Long(I)`: `verdict(I) = FREQ`, meaning "β's one-step numbers are
   single-orbit frequencies on I".
3. Otherwise: `verdict(I) = NOT`. The first mismatching long orbit (least `rep`) and its first mismatch are reported
   as `first_mismatch`.

**S1 (recorded secondary): observer-bearing orbits on the orbit side.** `Long′(I) := {O : long_c4(O)}`.
1. If `Long′(I) = ∅`: `s1_verdict = VOID_NO_ORBIT`.
2. Otherwise, if `eq(O)` holds for every `O ∈ Long′(I)`: `s1_verdict = FREQ`.
3. Otherwise: `s1_verdict = NOT`, with `s1_first_mismatch` the least-`rep` failing orbit's first mismatch against `T^β`.

**S2 (recorded secondary): long orbits on both sides.**
1. If `Long(I) = ∅`: `s2_verdict = VOID_NO_ORBIT`.
2. Otherwise, if `eq_beta_long(O)` holds for every `O ∈ Long(I)`: `s2_verdict = FREQ`.
3. Otherwise: `s2_verdict = NOT`, with `s2_first_mismatch` the least-`rep` failing orbit's first mismatch against
   `T^{β_long}`.

S1 and S2 are recorded verdicts. They do not replace or qualify the primary verdict, and no other variant is computed,
including the restriction to `Long′` on both sides.

Recorded with every instance:
- `|Long|`, `#{O ∈ Long : eq(O)}`, `|Long′|`, `#{O ∈ Long′ : eq(O)}` and `#{O ∈ Long : eq_beta_long(O)}`;
- the orbit-length histogram and `ord(φ)`;
- `#{O ∈ Long : pdiv_alpha(O)}`, `pdiv_beta` and `diameter_ge_4`.

The P-divisibility counts are descriptive and carry no verdict.

### 4.2 Overall verdicts

The same map is applied separately to the primary, S1 and S2 verdicts. For each, let `Ev` be the set of native instances
whose verdict of that kind is not VOID_NO_ORBIT. The overall verdict is:
- `FREQ_ALL` if `Ev ≠ ∅` and every instance in `Ev` is FREQ;
- `NOT_ALL` if `Ev ≠ ∅` and every instance in `Ev` is NOT;
- `MIXED` if `Ev` contains both;
- `VOID_ALL` if `Ev = ∅`.

The overall primary verdict is **the C-1 verdict** (`c1_verdict`). `c1_s1_verdict` and `c1_s2_verdict` are recorded.

### 4.3 Run validity

- **The job's steps.** The job has three steps that bear on validity:
  - (a) the check step: the tool, exiting 0–5 or 7;
  - (b) the re-application step, exiting 0 or 6;
  - (c) the verdict-text step, which regenerates `verdict_text` from `summary.json` and compares it byte for byte.
- **The run is complete** iff all of these hold:
  - step (a) exits 0. This requires that every control and mutation matches its frozen expected values (§3), that every
    invariant of §2 holds on every instance (budget, injectivity, the two implementations of `φ`, the mixture identity,
    double stochasticity, the partition `Σ_O |O| = |S|`, the agreement of the two P-divisibility methods, and every
    certificate verifying), that the frozen-input check passes, and that every output validates against
    `C1-OUTPUT-SCHEMA.json`;
  - step (b) exits 0. The step recomputes, from the orbits files and `T_beta`, every `eq`, `long_c4`, `eq_beta_long`,
    `T_beta_long`, each instance's three verdicts, the three overall verdicts and every `orbits_sha256`, and compares
    them with the stored values. Any difference exits 6;
  - step (c) matches.
- **Otherwise the run halts** at the first failure.
  - `summary.json` then has `run_status = HALT`, and the C-1 verdict is `null`.
  - `native_verdicts`, `native_s1_verdicts` and `native_s2_verdicts` are empty whenever `run_status = HALT`.
  - A native instance's file written before a halt carries no verdict of the run.
  - A failure in step (b) is read from that step's exit status and conclusion: `summary.json`, written by step (a), does
    not record it.
- Under §A.29 a halted run establishes nothing about the wave substratum. There is no partial verdict, no rerun within a
  freeze and no amendment after `F`. A runner failure before step (a) starts is open as OQ-14.
- **PASS (the result reviewer's test).** All five of these hold:
  - the host's conclusion for the C-1 job is `success`, read from its API;
  - step (a) exits 0;
  - step (b) exits 0;
  - `summary.json` has `run_status = COMPLETE`;
  - step (c) matches.

  Only under PASS is `summary.json`'s `c1_verdict` read as the result, together with the recorded `c1_s1_verdict` and
  `c1_s2_verdict`.

***

## 5. Outputs (§A.44)

**The schema.**
- `C1-OUTPUT-SCHEMA.json` (JSON Schema draft 2020-12) is frozen and authoritative for every output file. The tables below
  transcribe it.
- The format `c1-reduced-rational` is asserted. A string has that format iff:
  - it matches `^-?(0|[1-9][0-9]*)(/[1-9][0-9]*)?$`;
  - it is not `-0`;
  - when a denominator is present, the denominator is at least 2 and is coprime to the numerator.

  Probabilities additionally match the unsigned pattern, which leaves no sign.
- At start, the tool validates `C1-CONTROLS-EXPECTED.json` against `#/$defs/expected_file`. That check makes every
  expected field a schema field, and a failure exits 2.

**Output root.** Every output is written under `c1/` at the root of the job's checkout. The directory is uploaded as one
workflow artifact named `bornsel-c1`.

| File | Schema (`$defs`) | Contents |
|---|---|---|
| `c1/<id>.json` for a toy control | `toy_record` | the analysis fields below, plus `pdiv_beta_definitional`, `pdiv_certs_file`, `pdiv_certs_sha256`, `pdiv_certs_verified`, `sketch_check` (CE-8 only; `null` elsewhere), `expected`, `comparisons` and `match` |
| `c1/<id>.json` for a native instance | `native_record` | the analysis fields below, plus `phi_impls_agree`, `phi_zero_fixed`, `ord_phi_eq_qL` (`null` outside RX-ORD) and `diameter_ge_4` |
| `c1/<id>.json` for a unit control or mutation | `unit_record` | `params` (M-INJ, WF), `phi_impls_agree` (M-INJ, WF), `injective` and `evaluated_beyond_injectivity` (M-INJ), `results` and `reduced` (EX-ARITH), `schema_results` (EX-SCHEMA), `cert_results` (EX-CERT), `hand_steps` (WF-q*, items `{step, prev, cur, state, visible}`), `phi_of_zero` (WF-0), `expected`, `comparisons`, `match` |
| `c1/<id>.orbits.jsonl` (toys and natives) | `orbit_record`, one per line | `rep`, `length`, `cycle`, `visited_rows`, `unvisited_rows`, `n_a`, `T_alpha`, `long`, `eq`, `first_mismatch`, `pdiv_alpha`, `pdiv_witness`, `long_c4`, `eq_beta_long`, `first_mismatch_beta_long`, `pdiv_alpha_definitional` (`null` on natives) |
| `c1/<id>.pdiv-certs.json` (toys) | `pdiv_certs` | `schema`, `id`, `entries`: `{family, rep, rows, pair, kind, lambda, farkas_y}` |
| `c1/summary.json` | `summary` | `schema`, `controls_frozen` (16), `controls_matched`, `natives_frozen` (11), `natives_evaluated`, `native_verdicts`, `native_s1_verdicts`, `native_s2_verdicts`, `c1_verdict`, `c1_s1_verdict`, `c1_s2_verdict`, `run_status`, `first_failure`, `verdict_text` |

**Analysis fields** (toy and native records):
- `params`;
- `injective`;
- `ell_min`, `ell_min_rule` (`"n+1"`);
- `orbit_count`, `orbit_length_histogram`, `ord_phi`;
- `T_beta`;
- `doubly_stochastic`, `mixture_identity`;
- `beta_is_permutation`, `pdiv_beta`, `pdiv_beta_horizon`;
- `long_orbit_count`, `long_orbits_equal`, `long_orbits_pdiv_alpha`, `first_mismatch`, `verdict`;
- `s1_long_count`, `s1_long_equal`, `s1_first_mismatch`, `s1_verdict`;
- `T_beta_long`, `s2_long_equal`, `s2_first_mismatch`, `s2_verdict`;
- `orbits_file`, `orbits_sha256`.

Every record also carries the common fields `schema`, `id`, `order`, `kind`, `frozen_inputs` and `run`.

**Canonical orbits file.** UTF-8. One JSON object per line, with keys sorted and no insignificant whitespace. Lines are
in increasing `rep`, and each line ends with `\n`. `orbits_sha256` is the SHA-256 of these bytes.

**Comparison rules (controls).**
- The compared fields of a control are exactly the keys of its object in `C1-CONTROLS-EXPECTED.json`. A key missing from
  the computed record is a mismatch. Computed fields that are not expected are recorded and not compared.
- **Scalars.** Booleans, integers, `null` and strings must be equal and of the same JSON type. Probability strings are
  compared as strings, which is exact because the format admits one reduced form per rational.
- **Objects.** The key sets are equal and the values are equal under these rules.
- **Arrays.** The lengths are equal and the elements are equal in order. The orders are fixed: `visited_rows` and
  `unvisited_rows` are ascending; `cycle` starts at `rep` in `φ` order; and case lists follow the frozen case order.
- **`orbits`.** The expected key `orbits` is compared with the orbits file read as an array of its lines in file order.
  Each element must have the expected element's exact key set.

**Verdict text**, rendered from the summary fields only. `<ids>` is a comma-separated list in run order, or `none`.
`<S>` is the sentence "Recorded secondaries: S1 <c1_s1_verdict>; S2 <c1_s2_verdict>."
- COMPLETE, FREQ_ALL: "C-1: all <k> controls matched. On every evaluated native instance (<ids>), T^{α,O} = T^β exactly
  on visited rows for every orbit with |O| ≥ ℓ_min. Void instances: <ids>. <S>"
- COMPLETE, NOT_ALL: "C-1: all <k> controls matched. On every evaluated native instance (<ids>), some orbit with
  |O| ≥ ℓ_min has T^{α,O} ≠ T^β on a visited row. Void instances: <ids>. <S>"
- COMPLETE, MIXED: "C-1: all <k> controls matched. FREQ on <ids>; NOT on <ids>; void on <ids>. <S>"
- COMPLETE, VOID_ALL: "C-1: all <k> controls matched. No native instance has an orbit with |O| ≥ ℓ_min; the C-1
  verdict is void. <S>"
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
| 0 | (a), (b) | complete |
| 1 | (a) | a control, mutation or WF value mismatch |
| 2 | (a) | schema violation (an output, the expected file against `expected_file`, or a frozen parameter inconsistent with §2.2's formulas or Theorem 22's region conditions), or a floating-point value in a probability field |
| 3 | (a) | a frozen input does not match its git blob id at `F`, or `F` is not in the checkout |
| 4 | (a) | an invariant failure: the `φ` implementations disagree; the mixture identity or double stochasticity fails; the orbits do not partition `S`; the two P-divisibility methods disagree; or a certificate fails or is missing |
| 5 | (a) | `φ` is not injective on a toy or native instance |
| 6 | (b) | the re-application step found a stored field that differs from its recomputation |
| 7 | (a) | `state_count > 2¹⁶` |
| other nonzero | any | error |

**Where the verdict is read from.** The exit statuses of steps (a) and (b); the host's job and step conclusions, from its
API; and `summary.json`. Never log text.

***

## 6. Invariant → checkpoint (§A.41)

| Invariant asserted in this file | Checkpoint |
|---|---|
| exact rationals; no floating point in the verdict path | EX-ARITH and EX-SCHEMA (compared); the schema's `c1-reduced-rational` format on every probability field, exit 2; the tool review (§7 step 4) checks that the comparison and verdict path use integer arithmetic only |
| every expected field is a schema field | `C1-CONTROLS-EXPECTED.json` validated against `#/$defs/expected_file` at start; exit 2 |
| every output has the frozen schema | each output validated against `C1-OUTPUT-SCHEMA.json` before it is written; exit 2 |
| the four frozen inputs exist at `F` and are unchanged | git blob ids at `F` against the loaded bytes, at start; exit 3; `frozen_inputs` in every output |
| `F` is the reviewed constant and present in the checkout | `F` fixed in the reviewed workflow; its absence exits 3; `run.F` in every output |
| budget (§A.40) | `state_count ≤ 2¹⁶` before enumeration, exit 7; the job's `timeout-minutes`, its conclusion read from the host |
| frozen parameters satisfy §2.2 (`n = q^{2r}`, `m = q^{2(L−r)}`, `ℓ_min = n+1`, `r ≤ L/3`, `R` contiguous) | checked from `C1-INSTANCES.json` before enumeration; exit 2 |
| `φ` is a bijection on every toy and native instance | the injectivity check; exit 5; `injective` recorded |
| the bijectivity check detects a non-bijection | M-INJ, `injective = false` compared; exit 1 if not detected |
| the implemented `φ` is the §2.1 rule | WF-q3-L4 and WF-q2-L5 compared; the two implementations agree on all of `S` for every native instance (exit 4). WF-0 is a sanity check only |
| `T^β` is Main:117's matrix | the mixture identity and double stochasticity (exit 4); `T_beta` compared on every toy control |
| `T^{α,O}` on visited rows only; unvisited rows excluded and recorded | CC-UNVIS (compared, including `unvisited_rows`); `unvisited_rows` recorded per orbit |
| `ℓ_min = n + 1`, inclusive, fixed by parameters | `ell_min` compared on every toy; checked against the formula on every native instance (exit 2); CC-UNVIS exercises `|O| = ℓ_min`; CC-SHORT exercises exclusion |
| the void rule takes precedence | CC-VOID (compared) |
| FREQ and NOT are both reachable on non-transitive maps | CC-TWIN and CE-8 (compared) |
| A2: transitive gives equality | TT-4 and TT-6 (compared) |
| CE-8 gives `3/4` against `{1, 1/2}`; α on `O_A` divisible; β indivisible | `sketch_check`, `T_beta`, `orbits` (`T_alpha`, `pdiv_alpha`) and `pdiv_beta` compared on CE-8 |
| S1 and S2 are computed as frozen, and each separates its mechanism | CC-SKEW (S2 differs from the primary verdict); CC-PERM (S1 differs from the primary verdict, and S1 from S2); CC-UNVIS (S1 void); all `s1_*`, `s2_*`, `T_beta_long`, `long_c4`, `eq_beta_long` and `first_mismatch_beta_long` fields compared on every toy |
| the permutation-matrix test is as frozen | `beta_is_permutation`, `pdiv_alpha` and `long_c4` compared on every toy, including the partial row set of CC-UNVIS |
| Lemma PD agrees with the definition | the definitional check on every toy, compared with the Lemma PD value and the expected value; exit 4 on disagreement |
| definitional results are certified | every certificate verified by the independent checker (exit 4); `pdiv_certs_verified` compared; EX-CERT exercises the checker on valid and invalid certificates, including a false "feasible" `Λ` and a negative `Λ` |
| the verdicts are deterministic functions of the per-orbit record | step (b) recomputes them from the orbits files; exit 6 |
| per-orbit records are those the summary describes | `orbits_sha256` recomputed in step (b); exit 6 |
| no native verdict over a failed control | controls first; halt on the first mismatch; `natives_evaluated` is empty whenever `first_failure` is a control |
| frozen order; no adaptive extension | `order` compared with `C1-INSTANCES.json`; `natives_evaluated` is a prefix of the frozen order |
| one pass | the host run record shows `run_attempt = 1` (subject to OQ-14) |
| PASS combines five signals | the job emits the exit statuses of steps (a) and (b), `summary.json` and the step (c) comparison; the result reviewer reads the job conclusion from the host's API (§4.3) |
| verdict text generated only from structured output | step (c) regenerates `verdict_text` from `summary.json` and compares it byte for byte |

***

## 7. Execution boundary and governance

- **CI only (§A.40).** Locally, only cheap static checks of the tool may run. The instance set runs only in CI.
- **One pass**, halting on the first red. A void run is not repaired by re-running.
- **Order of steps.**
  1. **Freeze.** An independent reviewer reviews the exact candidate commit carrying the four frozen files. The owner
     then designates `F` (§8).
  2. **Owner go.** The owner gives the go on that reviewed `F`. The go explicitly accepts or replaces each open item of
     §8.2.
  3. **Tool.** Only then does the designated writer write the tool, the certificate checker and the workflow, on a
     disposable research branch. The workflow carries `F` as a constant.
  4. **Review.** An independent reviewer reviews the tool, the checker and the workflow at their exact commit, `F`'s
     value included, before any dispatch. The push-triggered workflows are inspected before any push (§A.43 item 4).
  5. **Dispatch approval.** Dispatch is a separate owner approval (§A.43). Any `workflow_dispatch` launch is a special
     launch.
  6. **Result review.** The independent reviewer applies the five-signal PASS of §4.3 from the host's API record.
- **Budget (an estimate, not measured).** The largest instances have `2¹⁶` states. The per-instance work is:
  - two computations of `φ`, each `O(L·|S|)`;
  - a cycle decomposition, `O(|S|)`;
  - the counts, `O(|S|)`;
  - the comparisons, `O(n²)` per orbit.

  P-divisibility uses Lemma PD on native instances, so no linear program runs there; the certified method runs on toys
  only, with `k ≤ 3`. Minutes are expected. The job timeout is 30 minutes; a timeout is red, and there is no extension.
- **Evidence (§A.42).**
  - The result note states the commit, the command, `summary.json` (small, with its digest), and the owner's designations
    and approvals, quoted with author and time (§A.42 item 7).
  - The tool, the checker and the workflow land on `main` with the result note, so that the command can be rerun from
    `main` (§A.42 item 1).
  - The per-orbit and certificate files can be regenerated by the command and need not land on `main`.
  - A run on a disposable branch is provenance only until its record lands on `main`.
- **Exclusions.** No C-2, no C-3, no Lean, no manuscript edit, no status change, no merge or publication.

***

## 8. Open items

### 8.1 Before a candidate `F`

- **Independent review** of the exact candidate `F`: this file, the three data files, their agreement with each other
  and with BSB:402–416, and the hand derivations of §3.

### 8.2 Owner questions (all open)

Each item below is open for the owner. The draft's default is stated, followed by the recommendation from the review of
`3be25e7f`.

1. **OQ-1, `ℓ_min`.** The draft uses `ℓ_min = n + 1` (§2.5). The corpus leaves "small p" unquantified (Main:62).
   - Alternatives:
     - `ℓ_min = 2`, which excludes fixed points only;
     - a fixed number common to all instances;
     - an orbit-level predicate in place of a length.
   - *Reviewer recommends:* accept `n+1` as the primary, with the S1 and S2 secondaries. The draft now freezes both as
     recorded verdicts (§4.1).
2. **OQ-2, the visible content of a site.** The draft uses the full `(prev, cur)` pair at each site of `R`, following
   `cutRealization` (`PhysicalC4Discharge.lean:578–582`), with the block `R = {0, …, r−1}` and `r ≤ L/3`. The
   alternative is the current value only.
   - *Reviewer recommends:* accept the `(prev, cur)` pairs. The corpus answers this, and the current-value split would
     be a surrogate.
3. **OQ-3, the coupling.** The draft uses `a = 1` only (SM:1602; SM:230; §2.1). At `q = 3`, `a = 2 ≡ −1` is not covered.
   - *Reviewer recommends:* accept `a = 1`. The corpus answers this, and `a = 2` is not a manuscript instance.
4. **OQ-4, the instance list.** The draft has eleven instances, including the non-coprime ones, and excludes W-q2-L7-r2.
   Theorem 22's diameter hypothesis holds only at `L = 8`. The question is which instances count toward the overall
   verdicts.
   - *Reviewer recommends:*
     - accept all eleven, all counting;
     - reinstate W-q2-L7-r2 as recorded, since it costs nothing, VOID does not count, and it gives an RX-ORD point at
       `r = 2`;
     - add a recorded secondary over N10 and N11 for the diameter hypothesis.
5. **OQ-5, the α-rooted family's row set.** The draft uses `V_O` only, horizon `{0, …, |O|}` (§2.4).
   - *Reviewer recommends:* accept `V_O`.
6. **OQ-6, β's P-divisibility on native instances.** The draft records it.
   - *Reviewer recommends:* record it. It is free, and its (⇒) direction is kernel-checked
     (`RootedRecurrenceBridge.lean:93`).
7. **OQ-7, RX-ORD.** In the draft it is recorded only.
   - *Reviewer recommends:* make it gating, expecting `ord = qL` from SM:1606. It is the only whole-map control of the
     native `φ`: a cycle-detection bug that fragments orbits while still partitioning `S` would push instances toward
     VOID_NO_ORBIT, and the WF spot checks cannot see that.
   - Gating would need its own exit code and a halt-text line.
8. **OQ-8, the aggregation.** The draft uses §4.2's map, in which void instances do not count, applied to the primary
   verdict, S1 and S2.
   - *Reviewer recommends:* accept, after the rename of `E` (done: `Ev`).
9. **OQ-9, Lemma PD.** The draft adopts the reduction to "`Γ₁` is a permutation matrix", with the certified definitional
   method on toys (§2.4).
   - *Reviewer recommends:* accept, with the surjectivity line (added) and a certified definitional method (added).
10. **OQ-10, the controls.** The draft's 16 gating controls are §3's.
    - *Reviewer recommends:*
      - accept all as gating;
      - add CC-SKEW and an S1 toy (added: CC-SKEW, CC-PERM);
      - make EX-SCHEMA two-sided (done);
      - add an `n = 3` toy that discriminates the order of `first_mismatch` (not added);
      - add a WF step at `r = 2`, at N6's parameters (not added).
11. **OQ-11, the QB readings.** The draft identifies `T^β` as the QB-2 credence and `T^{α,O}` as the QB-1 target at
    the cycle horizon (§2.6).
    - *Reviewer recommends:* accept, conditional on B1. The open question is which orbits the invariant prior ranges
      over (OQ-13).
12. **OQ-12, the governance form.** The draft proposes a research run on a disposable branch, not a §A.39 native V3
    round, with no `v3-round` or `v3-governed-paths` block, its freeze the owner-designated exact commit `F`, and the
    files placed as listed in the header.
    - *Reviewer recommends:*
      - accept the research-run form if the result is for the record only;
      - use a native V3 round if it is to support the O-OBSMU μ-number proposal (BSB §5.2);
      - under the research-run form, the preregistration should state that the run is not §A.39-protocol-valid and
        supports no status change by itself.
13. **OQ-13, the support of the credence prior.** Should QB-2's invariant prior range over all orbits, giving `T^β`
    and the primary verdict, or over observer-bearing orbits only, giving S2 for long orbits? The answer decides which
    recorded verdict answers C-1's question under QB-1 and QB-2 (§2.5, §9).
    - *Reviewer recommends:* that the owner decide it. The review's B1 shows that the primary verdict alone does not
      settle it.
14. **OQ-14, the rerun policy for a runner failure before step (a) starts.** For example: provisioning, checkout or
    environment set-up fails, and no output exists. `run_attempt = 1` with no exception would let such a failure void
    the freeze.
    - Options:
      - no rerun, so the freeze is spent;
      - a second dispatch, recorded with the failed run's id under a new owner approval, with the invariant restated as
        "the check step ran in exactly one attempt".
    - *Reviewer recommends:* add the policy, as an owner decision and never a silent rerun.

### 8.3 Points in the source sketch that cannot be frozen as stated

These are the points of BSB:404–416 that needed a choice, with the choice this draft makes.

1. **"`ℓ_min` fixed in advance."** No source fixes a value, and Main:62's "small p" is unquantified. The draft uses
   `n + 1` (§2.5), which is OQ-1, and adds the recorded secondaries S1 and S2 for the one-sidedness found in review.
2. **"A declared region R" and "small L".**
   - The sketch fixes neither the visible content of a site nor the sizes.
   - `L ≥ 3` is needed for distinct neighbours at `d = 1`.
   - Theorem 22's hypotheses fit the budget only at `L = 8`.
   - The draft's choices are in §2.1–§2.2 (OQ-2, OQ-4).
3. **The B4 record "per orbit".** Γ^α is undefined on unvisited roots, so a row set must be chosen; the draft uses
   `V_O` (OQ-5). By Lemma PD the record is a function of the comparison data, so it adds no independent information.
4. **"β indivisible" in the CE-8 control.** No horizon is given. The draft uses `{0, …, ord(φ)}`, which is 4 for CE-8.
5. **"An exact-arithmetic check."** As written it has no expected value. The draft makes it concrete as EX-ARITH and
   EX-SCHEMA.
6. **"A transitive toy, which must return equality."** Equality holds by construction (A2), so the toy is non-vacuous
   only with a non-permutation `T`. TT-4 and TT-6 are chosen accordingly.
7. **The verdict rule.** No rule combines instances into an overall verdict. The draft uses §4.2's map (OQ-8).
8. **The coefficient.** The wave rule's coefficient is named `α` in Lean, which clashes with the branch α. The sketch
   does not fix its value. The draft writes it `a` and fixes `a = 1` (OQ-3).

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
- **Cycle horizon only.** By Lemma A, the frequencies compared are those over a whole cycle of the orbit, of order up to
  the recurrence time, which no accessible window reaches (BSB:259; Main:141). C-1 says nothing about accessible-window
  frequencies, which are C-3's subject.
- **No selection.** A FREQ verdict would show that, on those instances, the Born-form numbers coincide with every long
  orbit's cycle frequencies, so the identity of the actual orbit does not matter for one-step numbers there. It would
  not derive β, select a measure, or supply a premise. That is the (Q-sel) question (BSB:77–79), which C-1 leaves where
  BSB:181 left it.
- **What a NOT verdict can and cannot mean.**
  - `ℓ_min` removes short orbits from the orbit side only, and `T^β` averages over every orbit. A primary NOT can
    therefore arise in three ways:
    - (i) the short, observer-lacking orbits skew `T^β` away from the long orbits' frequencies. On every native instance
      the fixed point at state 0, with row `δ₀` (`waveSubstratum_phi_fixes_zero`), is such an orbit;
    - (ii) a long orbit is C4-lacking: its `T^{α,O}` is a permutation matrix, and it disagrees with any
      non-deterministic `T^β` row;
    - (iii) observer-bearing orbits' frequencies genuinely differ from one another or from the credence.
  - The primary verdict does not distinguish these.
  - S2 removes (i): it compares the long orbits with a credence over long orbits only.
  - S1 removes (ii): it drops permutation orbits from the orbit side. It still compares them with `T^β`, so (i) remains
    within S1.
  - A primary NOT with S2 FREQ shows that the mismatch comes from the short orbits' weight in `T^β`. Whether that weight
    belongs in the credence is OQ-13, a question about the prior, not a computation.
  - A NOT in S2 locates a disagreement among long orbits themselves. Under QB-1, β's numbers would then need a further
    premise to be the operational target on that instance, such as a typicality hypothesis or a selection of the actual
    orbit.
  - No verdict says which orbit is actual.
  - S1 and S2 are recorded verdicts frozen in advance. They are not the C-1 verdict, and no other variant can be adopted
    from this run.
- **Interaction with QB-1.**
  - QB-1 makes operational frequencies the target and denies that credences establish a Born law by themselves.
  - C-1 compares the credence side (`T^β`, via QB-2, or `T^{β_long}` in S2) with the frequency side at the cycle horizon
    only. So FREQ cannot establish a Born law under QB-1 either: it establishes a coincidence of numbers at a horizon no
    observer reaches.
  - The one-step numbers are not the Born exponent: the native Born weights `|U_φ|²` lie in `{0, 1}` under every branch
    (BSB:117–121), and C-1 does not touch interface (a).
- **`ℓ_min` is a proxy for C3.** The rule `n + 1` is a necessary condition for an orbit to carry hidden capacity, not a
  characterization of observer-bearing orbits. Other thresholds can change the verdict (CC-SHORT shows the mechanism).
  The verdicts are valid only at the frozen threshold.
- **Present-visible records only.** The credence side is conditioned on `x₀`. Records of longer histories change both
  sides (BSB:250–256, Lemma A3) and are not tested.
- **P-divisibility record.** By Lemma PD it is a function of whether `T^{α,O}` is a 0/1 matrix, so it adds no
  information independent of the comparison data. It carries no verdict.
- **Calibration of the tool.** The controls are constructed toys with hand-derived values. A complete run shows that the
  implementation reproduces them and that the native `φ` matches the hand-derived steps. It does not show that the rule
  behaves as intended on inputs unlike the controls. Without RX-ORD gating (OQ-7), an orbit-fragmenting bug that still
  partitions `S` is not caught on native instances.
- **Consistency axis.** Whatever the verdict, it moves no correctness band (§A.23). A halted run establishes nothing
  about the wave substratum.
