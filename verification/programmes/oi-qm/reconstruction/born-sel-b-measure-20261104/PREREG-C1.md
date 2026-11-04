# BORN-SEL C-1 preregistration: single-orbit frequencies against the Born-form weights on small wave substrata (#1059, part (b))

**Status.** WIP / UNVERIFIED preregistration, draft r1. Paper only; nothing has been run, written as code, or
enumerated. Candidate freeze: it becomes frozen when the owner designates an exact commit `F` that carries this file
and its two data files. **Not authorized to run.** A run needs the owner's go on the reviewed `F`, then the tool, then
its review, then a separate dispatch approval (§7).

- **Frozen inputs at `F`** (proposed home: `verification/programmes/oi-qm/reconstruction/born-sel-b-measure-20261104/`,
  beside the assessment, per §A.36):
  - this file, `PREREG-C1.md`;
  - `C1-INSTANCES.json`, the instance list, order, encodings, explicit toy maps and the wave rule's parameters;
  - `C1-CONTROLS-EXPECTED.json`, the hand-derived expected values of every control and mutation.
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

**Notation clash, resolved.** The Lean wave rule's coupling coefficient is named `α` (`SubstratumInterfaceAudit.lean:160`),
and the assessment's measure branch is also α. In this file the **coupling coefficient is written `a`**, and α always
means the measure branch "uniform on the actual orbit" [D].

***

## 1. Objective and non-objectives

**Objective.** By exhaustive exact enumeration over ℚ, on small instances of the manuscripts' wave substratum, decide
for each instance whether "β's one-step numbers are single-orbit frequencies" (BSB:406): whether, for every orbit `O`
of `φ` with `|O| ≥ ℓ_min`, the orbit's cycle transition frequencies `T^{α,O}` equal the Born-form matrix `T^β` on every
visible row the orbit visits. On the same instances, record per orbit whether the α-rooted family is P-divisible on
`{0, …, |O|}` (BSB:411, B4).

**What the question is, in the owner's terms [D].** Under QB-2, the embedded observer's assignment given the present
visible value `x₀ = a` is the invariant maximal-entropy prior conditioned on that record, which is `unif({a} × 𝒞_H)`
(BSB:206–208, γ-c with a present-visible record); its one-step numbers are `T^β` (Main:117, Main:288–290). Under QB-1
the physical target is operational frequencies. By BSB:239–241 (Lemma A), the transition frequencies along the actual
trajectory over a whole cycle of the actual orbit `O*` are `T^{α,O*}`. C-1 asks, on native instances, whether these two
coincide for every orbit that the corpus admits as a candidate `O*`.

**Non-objectives.** The run does not cover:
- accessible-window frequencies (C-3, deferred until after QB-1; BSB:424);
- any Lean work (C-2);
- `d ≥ 2`, `d = 3`, the rounded (nonlinear) rule, or a coupling other than `a = 1`;
- record-constrained measures beyond the present-visible record;
- any selection of a measure, a new premise, a manuscript edit, a status change, merge or publication.

**What a completed run establishes.** For each evaluated native instance, at the frozen sizes and conventions, one of:
every long orbit's cycle frequencies equal `T^β` on its visited rows (FREQ); some long orbit's do not (NOT); or no orbit
is long (VOID_NO_ORBIT). Plus the per-orbit P-divisibility record. This is a result on the consistency axis (§A.23):
it compares two objects the framework itself defines and confronts no external measurement.

**What it does not establish.** See §9. In particular, it does not select a measure, does not bear on accessible
windows, and does not extend beyond the frozen instances.

***

## 2. Frozen preconditions

### 2.0 Conventions common to every instance

- **Arithmetic.** All counts are exact integers. A probability is a pair of integers reduced to lowest terms. Equality
  of two probabilities `x/y` and `u/v` is decided by `x·v = u·y` on integers. No floating-point value enters the
  computation, the comparison or the verdict path; one appearing in an output probability field is a schema violation
  (exit 2) [D].
- **Configurations.** Every instance is a finite set `S = 𝒞_V × 𝒞_H` with `n = |𝒞_V|`, `m = |𝒞_H|`. A state is an
  integer `s ∈ {0, …, nm − 1}`, with visible value `π_V(s) = s mod n` and hidden value `s div n`, so `s = v + n·h` [D].
- **Map.** `φ` is given as an array `φ[s]` over all of `S`: by an explicit table for toy instances
  (`C1-INSTANCES.json`), and by the wave rule of §2.1 for native instances.
- **Enumeration method.** Full: every state of `S`, for every instance. No sampling, no sequential method.
- **Bijectivity check.** For every instance the tool first checks that `φ` is injective on `S`. For an instance not
  marked as expected non-injective, a failure exits 5 before any other field of that instance is computed. For
  mutation M-INJ, which is expected non-injective, the detection is the compared field (§3.3).
- **Orbits.** The orbits are the cycles of `φ`. An orbit's representative `rep(O)` is its least state index; orbits are
  listed in increasing `rep`. `|O|` is the cycle length. `ord(φ)` is the least common multiple of the cycle lengths.

### 2.1 The native wave substratum [P, with file:line]

- **Structure.** A substratum is a site type `ι` with translations, an additive alphabet `V`, and a second-order rule
  `R` (`SubstratumInterfaceAudit.lean:60`). Its configuration space is the phase-space form `ι → V × V`
  (`SubstratumInterfaceAudit.lean:78`), and its dynamics is `φ := leapEquiv R.F` (`SubstratumInterfaceAudit.lean:81`).
- **The step.** `leap F x i = ((x i).2, F (curOf x) i − (x i).1)` (`SecondOrderCircuit.lean:67–68`), with
  `prevOf x i = (x i).1` and `curOf x i = (x i).2` (`SecondOrderCircuit.lean:48, 51`). So the per-site pair is
  `(prev, cur)` and the step is `(p, c) ↦ (c, F(c) − p)`. This is the manuscripts' second-order form
  `x_i(t+1) = f(neighbours of i at t) − x_i(t−1) mod q` (SM:106, SM:228).
- **The rule.** `waveF α c i = α * ∑_{p : Fin d × Bool} c (i + dir p)` (`SubstratumInterfaceAudit.lean:160–161`), with
  `dir (k, true) = +e_k` and `dir (k, false) = −e_k` (`SubstratumInterfaceAudit.lean:142–143`). The manuscript form is
  `f = α(x₁ + ⋯ + x_{2d}) mod q` (SM:228), and SM Appendix A writes the `d = 1` ring with coefficient 1:
  `x(n, t+1) = x(n−1, t) + x(n+1, t) − x(n, t−1) (mod q)` (SM:1602).
- **The lattice and the boundary.** Sites `Fin d → ZMod L`, the periodic torus; alphabet `ZMod q`
  (`SubstratumInterfaceAudit.lean:177–180`, with the docstring at :175–176: "the manuscripts' rule on a finite cubic
  torus with alphabet ℤ/qℤ").
  Boundary conditions are therefore periodic.
- **Kernel facts used as controls.** `φ` is a bijection (`waveSubstratum_A2`, `SubstratumInterfaceAudit.lean:190`); the
  rule commutes with translations (`waveSubstratum_A4Exact`, :202); it is additive (`waveSubstratum_A5`, :211); `φ`
  fixes the zero configuration (`waveSubstratum_phi_fixes_zero`, `StochasticInterface.lean:101`); and the wave
  substratum is not transitive (`waveSubstratum_stochastic_interface_gap`, `StochasticInterface.lean:191`).
- **The frozen instance of the rule [D, from the above].** `d = 1`, `a = 1` (the coefficient; "the manuscript instance
  `α = 1`", `PhysicalC4Discharge.lean:570–571`, and SM:1602), ring of `L` sites, `q ∈ {2, 3}`. At site `i`, with
  indices mod `L`:
  - `p′_i = c_i`;
  - `c′_i = (c_{i−1} + c_{i+1} − p_i) mod q`.

  The Lean sum ranges over `p : Fin 1 × Bool`, so both terms are always present. `L ≥ 3` is required so that
  `i − 1 ≠ i + 1` and the two neighbours are distinct sites; at `L = 2` the sum is `2c_{i+1}`, and at `L = 1` it is a
  self-coupling, which center independence excludes (SM:228) [D].
- **The visible/hidden split [P].** The kernel's cut realization takes "the visible carrier [as] the region's
  phase-space data, the hidden carrier the complement's, and the step is `𝒮.φ` transported along the split"
  (`PhysicalC4Discharge.lean:578–581`, def `cutRealization` at :582). The region `Vs` is a parameter, and "[SM]
  Theorem 22 quantifies over connected regions with `|V| ≤ N/3`" (`PhysicalC4Discharge.lean:561`; SM:1376).
- **The frozen region [D].** `R = {0, 1, …, r−1}`, a contiguous block of `r` sites, with `r ≤ L/3`. The visible
  configuration is the `(prev, cur)` pair at each site of `R`, so `n = q^{2r}`; the hidden configuration is the pair at
  each site outside `R`, so `m = q^{2(L−r)}`. Because the rule commutes with translations (A4Exact), every contiguous
  block of `r` sites gives the same instance up to relabelling; the block at the origin is chosen.
- **The state encoding [D].** Site digit `δ_i = p_i·q + c_i ∈ {0, …, q²−1}`; state index `s = Σ_i δ_i·(q²)^i`. Then
  `π_V(s) = s mod q^{2r}` and the hidden value is `s div q^{2r}`, consistent with §2.0's `s = v + n·h`.
- **Two implementations [D].** The tool computes `φ` twice: (i) by the site loop above; (ii) as the linear map
  `F = [[0, I], [−I, A]]` on `(p, c) ∈ (ℤ/q)^{2L}` with `A` the circulant ring adjacency (SM:1602), applied to the
  digit vector. The two arrays must be identical on all of `S` (exit 4 otherwise).

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

- **Budget.** Every instance has `|S| ≤ 2¹⁶`. `q = 2` reaches `2¹⁶` at `L = 8`; `q = 3` stays below it through `L = 5`
  (`3^{10} = 59,049`), and `L = 6` (`3^{12} = 531,441`) is excluded.
- **Region sizes.** `r ≤ L/3` gives `r = 1` for `L ≤ 5` and `r ∈ {1, 2}` for `L ∈ {6, 7, 8}`.
- **Excluded by design: W-q2-L7-r2.** By SM Theorem A.1 (SM:1604–1606, "For q prime with gcd(L, q) = 1 — q = 2
  included: ord(F mod q) = qL"), every orbit length divides `qL = 14 < 17 = ℓ_min`, so that instance would be void by
  construction. This uses the theorem's statement only; no orbit of any instance was computed [D]. Dropping it is an
  owner item (§8, OQ-4).
- **Coprime and non-coprime.** N1, N4, N7, N8 and N9 satisfy `gcd(L, q) = 1`, inside Theorem A.1's scope; the others
  have `q | L`, where the parabolic Jordan blocks of SM Appendix A are present. Both kinds are included.
- **Theorem 22's hypotheses [P, SM:1376].** "connected bounded-degree coupling graph with diameter D ≥ 4 … any connected
  subgraph V with |V| ≤ N/3". Every frozen `R` is connected and has `|R| ≤ N/3`. The ring's diameter `⌊L/2⌋` is at least
  4 only at `L = 8` (N10, N11). C1 holds on every instance by Theorem 22's own proof step, which uses only `∂V ≠ ∅`
  (SM:1378) [D]. The diameter hypothesis is not needed by C-1 and is recorded as unmet for N1–N9.

### 2.3 The compared objects [D, from the cited definitions]

For an instance with map `φ` on `S = 𝒞_V × 𝒞_H`:

- **Counts.** `c(a, j) := #{h ∈ 𝒞_H : π_V φ(a, h) = j}`. For an orbit `O`:
  - `c_O(a, j) := #{h : (a, h) ∈ O, π_V φ(a, h) = j}`;
  - `n_a(O) := #{h : (a, h) ∈ O}`.
- **`T^β`, the Born-form matrix.** `T^β(a, j) := c(a, j)/m` for every `a, j ∈ 𝒞_V`. This is Main:117's `T_ij`, the
  matrix of the Born-form theorem (Main:288–290), and `Γ^κ_1` with `κ_a` uniform on `𝒞_H` (BSB:126).
- **Rows an orbit visits.** `V_O := {a ∈ 𝒞_V : n_a(O) > 0}`. The rows in `𝒞_V ∖ V_O` are the orbit's **unvisited
  rows**; they are recorded and excluded from that orbit's comparison (BSB:407–408).
- **`T^{α,O}`, the single-orbit frequencies.** For `a ∈ V_O` and every `j ∈ 𝒞_V`:
  `T^{α,O}(a, j) := c_O(a, j)/n_a(O)`.
  - This is `Γ^κ_1` with `κ_a` uniform on `{h : (a, h) ∈ O}`, which is α conditioned on the root `a` (BSB:134–136).
  - By BSB:240–241 (Lemma A), for every `s* ∈ O` and every positive multiple `N` of `|O|`, the empirical frequency of
    the transition `a → j` among visits to `a` along `s*, φ(s*), …, φ^{N−1}(s*)` is exactly `T^{α,O}(a, j)`.
  - Since `φ` maps `O` into `O`, `T^{α,O}(a, j) = 0` for `j ∉ V_O`; the comparison still runs over every column `j`.
- **Orbit equality.** `eq(O)` holds iff `T^{α,O}(a, j) = T^β(a, j)` for every `a ∈ V_O` and every `j ∈ 𝒞_V`, i.e. iff
  `c_O(a, j)·m = c(a, j)·n_a(O)` for all such `(a, j)`. If `eq(O)` fails, its **first mismatch** is the
  lexicographically least `(a, j)` with inequality, reported with both values.
- **Mixture identity (an internal check, not a hypothesis) [D].** Because the orbits partition `S`,
  `Σ_O c_O(a, j) = c(a, j)` and `Σ_O n_a(O) = m` for every `a, j`; hence
  `T^β(a, ·) = Σ_{O ∋ a} (n_a(O)/m)·T^{α,O}(a, ·)`. The tool computes `c` directly over the `(a, h)` grid and
  separately as the orbit sum, and the two must agree exactly (exit 4 otherwise).
- **Double stochasticity [P, Main:62].** "the marginal of a bijection under the uniform prior is doubly stochastic,
  since each set `{x_j} × 𝒞_H` has exactly `|𝒞_H|` preimages". So `Σ_j c(a, j) = m` and `Σ_a c(a, j) = m`. Checked;
  exit 4 on failure.

### 2.4 P-divisibility (B4)

- **The kernel definition [P].** `PDivisible K Γ := ∀ s t, s < t → t ≤ K → ∃ Λ, IsRowStochastic Λ ∧ Γ t = Γ s * Λ`
  (`CausalReadback.lean:54`), with `IsRowStochastic` at `CausalReadback.lean:47`. The rooted maps with a shared prior are
  `rootedMap R t a j = Σ_h [π_V(step^t(a, h)) = j]·prior h` (`CausalReadback.lean:190`).
- **The α-rooted family on an orbit [D].** For `t ≥ 0`, `a, j ∈ V_O`:
  `Γ^{α,O}_t(a, j) := #{h : (a, h) ∈ O, π_V φ^t(a, h) = j} / n_a(O)`.
  It is square on `V_O`, row-stochastic, `Γ^{α,O}_0 = I`, `Γ^{α,O}_1 = T^{α,O}` restricted to `V_O`, and
  `Γ^{α,O}_{|O|} = I` because `φ^{|O|}` is the identity on `O`. Its rows are indexed by `V_O` only, because α gives no
  hidden conditional on an unvisited root; BSB:147 lets `κ_a` be arbitrary there for the implication, which would make a
  full-`𝒞_V` record depend on an arbitrary choice. Restricting to `V_O` is an owner item (§8, OQ-5).
- **The recorded quantity.** `pdiv_alpha(O) := PDivisible |O| Γ^{α,O}`, on `V_O`, horizon `{0, …, |O|}` (BSB:411).
- **The β family (recorded only) [D].** `Γ^β_t(a, j) := #{h : π_V φ^t(a, h) = j}/m` on `𝒞_V`, the kernel's
  `rootedMap` with the uniform prior. `pdiv_beta := PDivisible ord(φ) Γ^β`, horizon `{0, …, ord(φ)}`, where
  `Γ^β_{ord(φ)} = I`. Recording it on native instances is an owner item (§8, OQ-6); it is required on CE-8 (§3).
- **Lemma PD [D, one direction resting on a kernel lemma].** Let `Γ_t` be either family above, on its row set `W`
  (`V_O` or `𝒞_V`), with return time `N` (`|O|` or `ord(φ)`), so `Γ_N = I`. Then `PDivisible N Γ` holds iff `Γ_1` is a
  permutation matrix on `W`.
  - (⇒) Suppose `Γ_1` is not a permutation matrix. Then `N ≥ 2`, since `Γ_1 = I` when `N = 1`. A stochastic `Λ` with
    `Γ_N = Γ_1 Λ = I` would be a stochastic right inverse of `Γ_1`, which Main:133 forbids ("If a finite square stochastic
    matrix has a stochastic left or right inverse, then it is a permutation matrix"; kernel
    `isPermMatrix_of_stochastic_inverse`, `EquivalenceChain.lean:110`). So the pair `(1, N)` fails.
  - (⇐) Suppose `Γ_1` is a permutation matrix `P_f` with `f` a bijection of `W`. For α: every `(a, h) ∈ O` has
    `π_V φ(a, h) = f(a)`, so along the cycle `x_{k+1} = f(x_k)`, hence `π_V φ^t(a, h) = f^t(a)` and `Γ_t = P_{f^t}`. For
    β: `π_V φ(b, h′) = f(b)` for every `b, h′`, so by induction on `t`, `π_V φ^t(a, h) = f^t(a)`, and again
    `Γ_t = P_{f^t}`. Then `Λ_{s,t} := P_{f^s}^{T} P_{f^t} = P_{f^{t−s}}` is a permutation matrix, so row-stochastic, and
    `Γ_s Λ_{s,t} = Γ_t` for every `s < t ≤ N`.
  - So, on these horizons, `pdiv_alpha(O)` holds iff `T^{α,O}` is a 0/1 matrix on `V_O`, and `pdiv_beta` holds iff
    `T^β` is a permutation matrix. The B4 record is therefore a function of the comparison data. It is recorded because
    BSB:411 asks for it, and it carries no independent verdict.
- **How the tool computes it.** On every instance, by Lemma PD, with witness `(s, t) = (1, N)` when it fails. On every
  control in §3.1, also by the definition: for each pair `s < t ≤ N`, an exact rational feasibility test for a
  row-stochastic `Λ` with `Γ_t = Γ_s Λ` (at most 3 × 3 unknowns there). The two methods must agree, and both must match
  the hand-derived values. This is the countercontrol for Lemma PD.

### 2.5 `ℓ_min` (fixed before any result) [D; owner item OQ-1]

- **What the corpus says [P].** Main:62: "the atypical short orbits of the idealized linear dynamics (fixed points,
  low-period cycles) are precisely observer-lacking substrata — an orbit of period `p` makes at most `p` states
  dynamically accessible, so for small `p` no partition of it can satisfy the high-capacity condition C3". C3 is
  `log₂|𝒞_H| ≥ I*` (Main:78). The corpus does not quantify "small `p`".
- **The frozen rule [D].** `ℓ_min(I) := n_I + 1`, where `n_I = |𝒞_V|` of instance `I`. It depends only on the instance's
  declared parameters, so it is fixed before any result.
- **Justification [D].**
  - By pigeonhole, an orbit with `|O| ≥ n + 1` revisits some visible value, so `n_a(O) ≥ 2` for some `a`: some root
    carries at least two hidden states on the orbit.
  - An orbit with `|O| ≤ n` can have `n_a(O) = 1` at every visited root. Then `T^{α,O}` is deterministic, the orbit is
    its own visible sequence, and no hidden state on it mediates anything. That is the C3 failure that Main:62
    describes, in its weakest form: orbit-restricted hidden capacity `log₂ max_a n_a(O) = 0`.
  - So `n + 1` is the least length at which the orbit-restricted hidden capacity is guaranteed positive at some root
    by length alone. It is a necessary condition, not a sufficient one, for an orbit to be observer-bearing.
  - It is consistent with the assessment's control: in CE-8, `n = 2`, `ℓ_min = 3`, and both orbits (length 4) count,
    as BSB:137 requires ("no period-based or C3-based exclusion … separates them").
- **Comparison is `|O| ≥ ℓ_min`**, inclusive. Control CC-UNVIS has an orbit of length exactly `ℓ_min`.
- **No other threshold yields a verdict.** Every orbit's `eq(O)` and `|O|` are recorded, so the record would support
  other thresholds. This run issues a verdict only at the frozen `ℓ_min`. Any other threshold needs a new freeze.

### 2.6 Owner decisions, and how this preregistration reads them [O, with readings D]

- **QB-1 [O].** "Operational frequencies are the physical target; observer credences cannot by themselves establish a
  Born law." Reading [D]: the target of C-1's comparison is `T^{α,O}`, the cycle frequencies (Lemma A, BSB:240–241). A
  FREQ verdict would show that the Born-form numbers coincide with that target for every long orbit on the instance; it
  does not establish a Born law (§9).
- **QB-2 [O].** "γ is read as an invariant prior followed by conditioning, with the prior's physical source left open."
  Reading [D]: with the present-visible record `x₀ = a`, γ read this way is `unif(U_r)` conditioned on `A_r`, which is
  `unif({a} × 𝒞_H)` (BSB:209–216), whose one-step numbers are row `a` of `T^β`. C-1 takes `T^β` as the credence side and
  is silent on the prior's physical source.

***

## 3. The frozen control set

The expected values are hand derivations of constructed toys, frozen in `C1-CONTROLS-EXPECTED.json`. §A.29's "rule, not
numbers" applies to the native decision rule of §4, which is frozen without reference to any native value. **No expected
value is given for any native instance.**

**Execution order.** The 13 controls and mutations run first, in the order of `C1-INSTANCES.json` (orders 1–13): the
seven toys of §3.1, M-INJ, EX-ARITH, EX-SCHEMA, WF-q2-L5, WF-q3-L4 and WF-0. The 11 native instances follow
(orders 14–24, in §2.2's order). Native instances run only if every control and mutation has matched. A mismatch halts the run before any native instance is evaluated, so no native
verdict is ever printed over a failed control (§A.29).

### 3.1 Toy controls (explicit maps; `s = v + n·h`)

| id | `n`, `m` | `φ` as an array over `s = 0, 1, …` | Purpose |
|---|---|---|---|
| CE-8 | 2, 4 | `[1, 2, 3, 0, 6, 7, 5, 4]` | the assessment's counterexample (BSB:129–138); must give NOT |
| TT-4 | 2, 2 | `[1, 3, 0, 2]` | transitive toy, A2 (BSB:246); must give equality |
| TT-6 | 3, 2 | `[1, 4, 3, 5, 2, 0]` | transitive toy with unequal rows and `n = 3` |
| CC-TWIN | 2, 4 | `[1, 3, 0, 2, 5, 7, 4, 6]` | non-transitive with two matching orbits; FREQ must be reachable |
| CC-SHORT | 2, 4 | `[1, 3, 0, 2, 4, 6, 5, 7]` | short mismatching orbits excluded by `ℓ_min` |
| CC-UNVIS | 3, 2 | `[1, 3, 5, 4, 0, 2]` | a long orbit with an unvisited row; orbit length exactly `ℓ_min` |
| CC-VOID | 2, 1 | `[1, 0]` | no orbit reaches `ℓ_min`; void takes precedence over equality |

**Hand derivations [D].**

- **CE-8.** States: `(0,0)=0, (1,0)=1, (0,1)=2, (1,1)=3, (0,2)=4, (1,2)=5, (0,3)=6, (1,3)=7`.
  - `O_A` (rep 0): `0→1→2→3→0`, i.e. `(0,0)→(1,0)→(0,1)→(1,1)`, visible `0101`.
  - `O_B` (rep 4): `4→6→5→7→4`, i.e. `(0,2)→(0,3)→(1,2)→(1,3)`, visible `0011`.
  - Next visible values from root 0 over `h = 0..3`: `1, 1, 0, 1`; from root 1: `0, 0, 1, 0`. So
    `T^β = [[1/4, 3/4], [3/4, 1/4]]`, as at BSB:133.
  - `T^{α,O_A} = [[0, 1], [1, 0]]` and `T^{α,O_B} = [[1/2, 1/2], [1/2, 1/2]]`, as at BSB:135–136.
  - The sketch's check: `T^β(0, 1) = 3/4` against `T^{α,O_A}(0, 1) = 1` and `T^{α,O_B}(0, 1) = 1/2` (BSB:414).
  - `ℓ_min = 3`, so both orbits are long. Both have `eq = false`, with first mismatch `(0, 0)`: `0` against `1/4` for
    `O_A`, and `1/2` against `1/4` for `O_B`. Verdict NOT.
  - P-divisibility: `O_A` is divisible (`Γ₁` = swap, `Γ₂ = I`); `O_B` is not (`Γ₁ = J/2`, `Γ₄ = I`); β is not, with
    `ord(φ) = 4` (BSB:153–154).
- **TT-4.** One orbit `0→1→3→2→0`, i.e. `(0,0)→(1,0)→(1,1)→(0,1)`. `T^β = T^{α,S} = [[1/2, 1/2], [1/2, 1/2]]`. Verdict
  FREQ. α and β both indivisible (`Γ₁` not a permutation). `ord(φ) = 4`.
- **TT-6.** States `(v,h) = v + 3h`. One orbit `0→1→4→2→3→5→0`, i.e. `(0,0)→(1,0)→(1,1)→(2,0)→(0,1)→(2,1)`, visible
  `011202`. `T^β = T^{α,S} = [[0, 1/2, 1/2], [0, 1/2, 1/2], [1, 0, 0]]`. `ℓ_min = 4 ≤ 6`. Verdict FREQ. α and β
  indivisible. `ord(φ) = 6`.
- **CC-TWIN.** Orbits: rep 0, `0→1→3→2→0`; rep 4, `4→5→7→6→4` (the TT-4 pattern on `h ∈ {2, 3}`). `T^β = J/2`, and
  both orbits give `J/2`. Verdict FREQ, on a non-transitive map. All families indivisible. `ord(φ) = 4`.
- **CC-SHORT.** Orbits: rep 0, length 4 (TT-4 on `h ∈ {0, 1}`); rep 4, the fixed point `(0,2)`; rep 5, the 2-cycle
  `(1,2) ↔ (0,3)`; rep 7, the fixed point `(1,3)`.
  - `T^β = J/2` (root 0 over `h = 0..3`: `1, 0, 0, 1`; root 1: `1, 0, 0, 1`).
  - `ℓ_min = 3`, so only rep 0 is long, and it has `eq = true`. Verdict FREQ.
  - The short orbits have `eq = false`: rep 4, `V_O = {0}`, row `[1, 0]`, unvisited `{1}`; rep 5, rows
    `[[0, 1], [1, 0]]`; rep 7, `V_O = {1}`, row `[0, 1]`, unvisited `{0}`. At a threshold of 1 the verdict would be NOT;
    this is what makes the `ℓ_min` exclusion visible.
  - P-divisibility: rep 0 no; reps 4, 5 and 7 yes; β no. `ord(φ) = 4`.
- **CC-UNVIS.** States `v + 3h`. Orbits: rep 0, `0→1→3→4→0`, i.e. `(0,0)→(1,0)→(0,1)→(1,1)`, visiting rows `{0, 1}`
  only; rep 2, the 2-cycle `(2,0) ↔ (2,1)`.
  - `T^β = [[0, 1, 0], [1, 0, 0], [0, 0, 1]]`.
  - `ℓ_min = 4 = |O|` for rep 0 (the inclusive boundary). Row 2 is unvisited and excluded. On rows 0 and 1, `eq = true`.
    Verdict FREQ.
  - A tool that compared the unvisited row, or failed on `n_2(O) = 0`, returns NOT or errors, and the control fails.
  - P-divisibility: both orbits yes; β yes (`T^β` is a permutation). `ord(φ) = 4`.
- **CC-VOID.** One orbit, `(0,0) ↔ (1,0)`, of length 2 < `ℓ_min = 3`. The map is transitive and `eq = true`, but the
  verdict is VOID_NO_ORBIT. α and β are P-divisible; `ord(φ) = 2`.

### 3.2 Native-faithfulness controls (hand-derived, [D])

These check that the implemented `φ` is the §2.1 rule. They run in the control phase, before any native instance, and
compute `φ` on the listed states only, with both implementations of §2.1. A mismatch, or a disagreement between the
two implementations, exits 1 and halts.

- **WF-0** (for the parameters of each of N1–N11): `φ[0] = 0` (`waveSubstratum_phi_fixes_zero`,
  `StochasticInterface.lean:101`). In the native phase this makes the orbit of state 0 a fixed point.
- **WF-q3-L4** (the parameters of N7): from `p = (0,0,0,0)`, `c = (1,0,0,0)`:
  - step 1: `p′ = (1,0,0,0)`, `c′ = (0,1,0,1)`;
  - step 2: `p″ = (0,1,0,1)`, `c″ = (1,0,2,0)`.

  As state indices: `1 → 741 → 2377`; visible values (`n = 9`): `1 → 3 → 1`.
- **WF-q2-L5** (the parameters of N4): from `p = 0`, `c = (1,0,0,0,0)`:
  - step 1: `p′ = (1,0,0,0,0)`, `c′ = (0,1,0,0,1)`;
  - step 2: `p″ = (0,1,0,0,1)`, `c″ = (1,0,1,1,0)`.

  As state indices: `1 → 262 → 601`; visible values (`n = 4`): `1 → 2 → 1`.

### 3.3 Mutations and countercontrols

- **M-INJ (bijectivity check).** The §2.1 rule with the `−p` term deleted, `(p, c) ↦ (c, A c)`, at `q = 2`, `L = 3`,
  `r = 1`. Two states with the same `c` and different `p` collide, so `φ` is not injective [D]. Expected:
  `injective = false`, nothing further computed for this mutation. If the tool reports `true`, exit 1.
- **EX-ARITH (exact comparison).** The comparator used in §2.3 is applied to frozen pairs:
  - `("1/3", "6004799503160661/18014398509481984")` → unequal. The second value is the IEEE-754 double nearest `1/3`
    (`(2⁵⁴ − 1)/(3·2⁵⁴)`), so a floating-point comparison would report equality.
  - `("2/6", "1/3")` → equal, after reduction to lowest terms.
  - `("3/4", "3/4")` → equal; `("0", "0/5")` → equal.
- **EX-SCHEMA.** The schema validator is run on a frozen fragment with a JSON number `0.75` in a probability field. The
  expected result is rejection, naming the field `T_beta`.
- For EX-ARITH and EX-SCHEMA, the comparator and the validator are called as units on the frozen inputs. The expected
  outcome (unequal, rejection) is a compared field and does not exit; a different outcome exits 1.
- **The countercontrols built into §3.1.**
  - CC-TWIN shows that FREQ is reachable on a non-transitive map, so the rule does not return NOT on every
    non-transitive map.
  - CE-8 shows that NOT is reachable.
  - CC-SHORT shows that `ℓ_min` excludes short orbits.
  - CC-UNVIS shows that unvisited rows are excluded.
  - CC-VOID shows that the void rule takes precedence over equality.
  - The definition-level P-divisibility test on every toy is the countercontrol for Lemma PD (§2.4).

### 3.4 Recorded cross-checks (recorded only; not gating, owner item OQ-7)

- **RX-ORD.** For N1, N4, N7, N8 and N9 (`gcd(L, q) = 1`), SM Theorem A.1 states `ord(φ) = qL` (SM:1604–1606). The tool
  records `ord(φ)` and the boolean `ord_phi == q·L`. A disagreement would be a finding about SM Appendix A or the tool,
  diagnosed after the run, and it does not void C-1.

***

## 4. Decision rule

### 4.1 Per native instance (a deterministic map from the computed data)

1. `Long(I) := {O : |O| ≥ ℓ_min(I)}`.
2. If `Long(I) = ∅`: `verdict(I) = VOID_NO_ORBIT`.
3. Otherwise, if `eq(O)` holds for every `O ∈ Long(I)`: `verdict(I) = FREQ`, meaning "β's one-step numbers are
   single-orbit frequencies on I".
4. Otherwise: `verdict(I) = NOT`. The first mismatching long orbit (least `rep`) and its first mismatch are reported.

Recorded with every verdict:
- `|Long(I)|` and `#{O ∈ Long(I) : eq(O)}`;
- the orbit-length histogram and `ord(φ)`;
- `#{O ∈ Long(I) : pdiv_alpha(O)}`.

The P-divisibility counts are descriptive and carry no verdict.

### 4.2 Overall C-1 verdict

Let `E` be the set of native instances whose verdict is not VOID_NO_ORBIT.
- `FREQ_ALL` if `E ≠ ∅` and every instance in `E` is FREQ;
- `NOT_ALL` if `E ≠ ∅` and every instance in `E` is NOT;
- `MIXED` if `E` contains both;
- `VOID_ALL` if `E = ∅`.

### 4.3 Run validity

- The run is **complete** iff all of the following hold:
  - every control and mutation matches its frozen expected values (§3);
  - every invariant of §2 holds on every instance: injectivity, the two implementations of `φ`, the mixture identity,
    double stochasticity, the partition `Σ_O |O| = |S|`, and the agreement of the two P-divisibility methods on controls;
  - the frozen-input check passes (§5);
  - the schema check passes.
- Otherwise the run **halts** at the first failure, and the C-1 verdict is `null`. A native instance's file written
  before a halt carries no verdict of the run: the summary's `native_verdicts` is empty whenever `run_status = HALT`.
- Under §A.29 a halted run establishes nothing about the wave substratum. There is no partial verdict, no rerun within
  a freeze and no amendment after `F`.
- **PASS** (the result reviewer's test). All four of these hold:
  - the host's conclusion for the C-1 job is `success`, read from its API;
  - the check step exits 0;
  - `summary.json` has `run_status = COMPLETE`;
  - the `verdict_text` regenerated from `summary.json` equals the stored one byte for byte.

  Only under PASS is `summary.json`'s `c1_verdict` read as the result.

***

## 5. Outputs (§A.44)

**Per instance**, `c1/<id>.json`, schema `bornsel-c1/1`:
- `id`, `order`, `kind` (`control` | `mutation` | `native`), `params` (`q`, `L`, `d`, `a`, `r`, `R`, `n`, `m`,
  `state_count`), `encoding`;
- `injective`, `phi_impls_agree` (native only), `phi_zero_fixed` (native only), `hand_steps` (WF controls: the list of
  `{step, state, visible}`);
- `ell_min`, `ell_min_rule` (`"n+1"`);
- `orbit_count`, `orbit_length_histogram` (a map from length to count), `ord_phi`, `ord_phi_eq_qL` (RX-ORD instances,
  otherwise `null`);
- `T_beta` (a map from each row `a` to the list of `n` rational strings);
- `doubly_stochastic`, `mixture_identity`;
- `beta_is_permutation`, `pdiv_beta`, `pdiv_beta_horizon`, and for toy controls `pdiv_beta_definitional`;
- `long_orbit_count`, `long_orbits_equal`, `long_orbits_pdiv_alpha`;
- `first_mismatch` (`null`, or `{rep, a, j, alpha, beta}`);
- `orbits_file` (path) and `orbits_sha256`: the SHA-256 of the per-orbit file below, in its canonical serialization
  (UTF-8, one JSON object per line, keys sorted, no insignificant whitespace, lines in increasing `rep`);
- `verdict` (`FREQ` | `NOT` | `VOID_NO_ORBIT`, or `null` for a mutation);
- for controls and mutations: `expected`, `comparisons` (a list of `{field, expected, computed, match}`) and `match`;
- `frozen_inputs`: for each of the three frozen files, its path, its git blob id at `F`, and the git blob id of the
  bytes read;
- `run`: `F`, the run commit and `run_attempt`.

**Per orbit**, `c1/<id>.orbits.jsonl`, one object per orbit:
- `rep`, `length`, `cycle` (the states `rep, φ(rep), …`), `visited_rows`, `unvisited_rows`, `n_a` (a map from row to
  count);
- `T_alpha` (a map from each visited row to the list of `n` rational strings);
- `long`, `eq`, `first_mismatch`;
- `pdiv_alpha`, `pdiv_witness` (`null` or `[1, length]`);
- for controls only, `pdiv_alpha_definitional`.

**`c1/summary.json`**:
- `schema` (`bornsel-c1-summary/1`), `controls_frozen`, `controls_matched`, `natives_frozen` (11),
  `natives_evaluated` (the ids, in order);
- `native_verdicts` (a map from id to verdict);
- `c1_verdict` (`FREQ_ALL` | `NOT_ALL` | `MIXED` | `VOID_ALL` | `null`);
- `run_status` (`COMPLETE` | `HALT`);
- `first_failure` (`null`, or `{exit, id, field, expected, computed, detail}`);
- `verdict_text`.

**Encodings.** Every probability is a string matching `^(0|[1-9][0-9]*)(/[1-9][0-9]*)?$` in lowest terms, with the
denominator omitted only when it is 1. A JSON number in any probability field is a schema violation (exit 2).

**Verdict text**, rendered from the summary fields only. `<ids>` is a comma-separated list in run order, or `none`.
- COMPLETE, FREQ_ALL: "C-1: all <k> controls matched. On every evaluated native instance (<ids>), T^{α,O} = T^β exactly
  on visited rows for every orbit with |O| ≥ ℓ_min. Void instances: <ids>."
- COMPLETE, NOT_ALL: "C-1: all <k> controls matched. On every evaluated native instance (<ids>), some orbit with
  |O| ≥ ℓ_min has T^{α,O} ≠ T^β on a visited row. Void instances: <ids>."
- COMPLETE, MIXED: "C-1: all <k> controls matched. FREQ on <ids>; NOT on <ids>; void on <ids>."
- COMPLETE, VOID_ALL: "C-1: all <k> controls matched. No native instance has an orbit with |O| ≥ ℓ_min; the C-1
  verdict is void."
- Exit 1: "C-1 halted at <id>: <field> expected <expected>, computed <computed>. The run is void."
- Exit 2: "C-1 halted at <id or 'start'>: schema violation in <field>. The run is void."
- Exit 3: "C-1 halted at start: frozen input <detail> does not match its git blob id at F. The run is void."
- Exit 4: "C-1 halted at <id>: invariant <detail> failed. The run is void."
- Exit 5: "C-1 halted at <id>: φ is not injective. The run is void."
- Any other exit: "C-1 halted with exit <exit>. The run is void."

**Exit status.**

| Code | Meaning |
|---|---|
| 0 | complete |
| 1 | a control, mutation or WF value mismatch |
| 2 | schema violation, or a floating-point value in a probability field |
| 3 | a frozen input does not match its git blob id at `F`, or `F` is not in the checkout |
| 4 | an invariant failure: the `φ` implementations disagree, the mixture identity fails, double stochasticity fails, the orbits do not partition `S`, or the two P-divisibility methods disagree on a control |
| 5 | `φ` is not injective on an instance not marked as expected non-injective |
| other nonzero | error |

**Where the verdict is read from.** The exit status of the check step; the host's job and step conclusions, from its
API; and `summary.json`. Never log text.

***

## 6. Invariant → checkpoint (§A.41)

| Invariant asserted in this file | Checkpoint |
|---|---|
| exact rationals; no floating point in the verdict path | EX-ARITH (compared); EX-SCHEMA (compared); the schema regex on every probability field, exit 2; the tool review (§7 step 3) checks that the comparison and verdict path use integer arithmetic only |
| the three frozen inputs exist at `F` and are unchanged | git blob ids at `F` against the loaded bytes, at start; exit 3; `frozen_inputs` in every output |
| `F` is the reviewed constant and present in the checkout | `F` fixed in the reviewed workflow; its absence exits 3; `run.F` in every output |
| `φ` is a bijection on every non-mutation instance | the injectivity check; exit 5; `injective` recorded |
| the bijectivity check detects a non-bijection | M-INJ, `injective = false` compared; exit 1 if not detected |
| the implemented `φ` is the §2.1 rule | WF-0 on every native instance; WF-q3-L4 and WF-q2-L5 compared; the two implementations agree on all of `S` (exit 4) |
| `T^β` is Main:117's matrix | the mixture identity and double stochasticity (exit 4); `T_beta` compared on every toy control |
| `T^{α,O}` on visited rows only; unvisited rows excluded and recorded | CC-UNVIS (compared, including `unvisited_rows`); `unvisited_rows` recorded per orbit |
| `ℓ_min = n + 1`, inclusive, fixed by parameters | `ell_min` compared on every control, and checked against `params.n + 1` on every native instance; CC-UNVIS exercises `|O| = ℓ_min`; CC-SHORT exercises exclusion |
| the void rule takes precedence | CC-VOID (compared) |
| FREQ and NOT are both reachable on non-transitive maps | CC-TWIN and CE-8 (compared) |
| A2: transitive gives equality | TT-4 and TT-6 (compared) |
| CE-8 gives `3/4` against `{1, 1/2}`; α on `O_A` divisible; β indivisible | `T_beta`, `T_alpha`, `pdiv_alpha` and `pdiv_beta` compared on CE-8 |
| Lemma PD agrees with the definition | the definitional P-divisibility test on every toy, compared with the Lemma PD value and with the expected value; exit 4 on disagreement |
| the verdict is a deterministic function of the per-orbit record | a re-application step recomputes each `eq(O)` from `T_alpha` and `T_beta` in the orbits file, and each instance verdict from `long`, `eq` and `ell_min`, and compares them with the stored fields |
| per-orbit records are those the summary describes | `orbits_sha256` recomputed from the canonical file in the re-application step |
| no native verdict over a failed control | controls first; halt on the first mismatch; `natives_evaluated` is empty whenever `first_failure` is a control |
| frozen order; no adaptive extension | `order` compared with `C1-INSTANCES.json`; `natives_evaluated` a prefix of the frozen order |
| one pass | the host run record shows `run_attempt = 1` |
| budget (§A.40) | `|S| ≤ 2¹⁶` checked from `params` before enumeration (exit 2 if exceeded); the job's `timeout-minutes`; its conclusion read from the host |
| PASS combines four signals | the job emits the exit status, `summary.json` and the regenerated-`verdict_text` comparison; the result reviewer reads the job conclusion from the host's API (§4.3) |
| verdict text generated only from structured output | a step regenerates `verdict_text` from `summary.json` and compares it byte for byte |

***

## 7. Execution boundary and governance

- **CI only (§A.40).** Locally, only cheap static checks of the tool may run. The instance set runs only in CI.
- **One pass**, halting on the first red. A void run is not repaired by re-running.
- **Order of steps.**
  1. **Freeze.** An independent reviewer reviews the exact candidate commit carrying the three frozen files. The owner
     then designates `F` (§8).
  2. **Owner go.** The owner gives the go on that reviewed `F`. The go explicitly accepts each [D] choice listed in §8.
  3. **Tool.** Only then does the designated writer write the tool and the workflow, on a disposable research branch.
     The workflow carries `F` as a constant.
  4. **Review.** An independent reviewer reviews the tool and the workflow at their exact commit, `F`'s value included,
     before any dispatch. The push-triggered workflows are inspected before any push (§A.43 item 4).
  5. **Dispatch approval.** Dispatch is a separate owner approval (§A.43). Any `workflow_dispatch` launch is a special
     launch.
  6. **Result review.** The independent reviewer applies the four-signal PASS of §4.3 from the host's API record.
- **Budget (an estimate, not measured).** The largest instances have `2¹⁶` states. The per-instance work is: two
  computations of `φ` (each `O(L·|S|)`), a cycle decomposition (`O(|S|)`), the counts (`O(|S|)`) and the comparisons
  (`O(n²)` per orbit). P-divisibility uses Lemma PD on native instances, so no linear program runs there. Minutes are
  expected. The job timeout is 30 minutes; a timeout is red, and there is no extension.
- **Evidence (§A.42).** The result note states the commit, the command, `summary.json` (small, with its digest) and the
  owner's designations, quoted with author and time. The per-orbit files are regenerable by the command and need not
  land on `main`. A run on a disposable branch is provenance only until its record lands on `main`.
- **Exclusions.** No C-2, no C-3, no Lean, no manuscript edit, no status change, no merge or publication.

***

## 8. Open items blocking freeze (owner questions)

1. **Independent review** of the exact candidate `F`: this file, the two data files, and their agreement with each
   other and with BSB:402–416.
2. **The owner's go on that `F`**, accepting or replacing each of these:
   - **OQ-1, `ℓ_min`.** The rule `ℓ_min = n + 1` (§2.5). The corpus leaves "small p" unquantified (Main:62).
     Alternatives:
     - `ℓ_min = 2`, which excludes fixed points only;
     - a fixed number common to all instances;
     - an orbit-level predicate instead of a length, such as "`T^{α,O}` is not a permutation matrix" (an orbit-level
       C1). That predicate is defined in advance but depends on computed data, so it departs from the sketch's
       "`ℓ_min` fixed in advance".
   - **OQ-2, the visible content of a site.** The full `(prev, cur)` pair at each site of `R`, following
     `cutRealization` (`PhysicalC4Discharge.lean:578–582`). The alternative is the current value only, with `prev` on
     `R` hidden. The block `R = {0, …, r−1}` with `r ≤ L/3`.
   - **OQ-3, the coupling.** `a = 1` only (`PhysicalC4Discharge.lean:570–571`; SM:1602). At `q = 3`, `a = 2 ≡ −1` is
     also nondegenerate and is not covered. The observer-level `a = 1/d` (SM:228 remark) is `1` at `d = 1`.
   - **OQ-4, the instance list.**
     - The eleven instances of §2.2, including the non-coprime ones.
     - W-q2-L7-r2 is dropped because Theorem A.1 makes it void by construction.
     - Theorem 22's diameter hypothesis holds only at `L = 8`.
     - Whether all eleven count toward the overall verdict, or only some, such as those meeting the diameter hypothesis.
   - **OQ-5, the α-rooted family's row set.** Rows `V_O` only, horizon `{0, …, |O|}` (§2.4). The alternative is full
     `𝒞_V` with some convention for `κ_a` on unvisited roots, for which the source leaves `κ_a` arbitrary (BSB:147).
   - **OQ-6, β's P-divisibility on native instances.** Record `pdiv_beta` (horizon `ord(φ)`), or omit it there. It is
     required on CE-8 either way.
   - **OQ-7, RX-ORD.** Recorded only (the default), or a gating control. Gating would make C-1 void if SM Theorem A.1
     fails on these instances.
   - **OQ-8, the aggregation.** The overall map of §4.2, in which void instances do not count.
   - **OQ-9, Lemma PD.** Acceptance of the reduction of P-divisibility to "`Γ₁` is a permutation matrix", with the
     definitional cross-check on controls only. It has not been independently reviewed.
   - **OQ-10, the controls.**
     - The constructed controls TT-6, CC-TWIN, CC-SHORT, CC-UNVIS and CC-VOID, the WF steps, M-INJ, EX-ARITH and
       EX-SCHEMA. The sketch names only a transitive toy, CE-8 and an exact-arithmetic check.
     - All are gating.
   - **OQ-11, the QB readings.** The readings of QB-1 and QB-2 in §2.6, i.e. the identification of `T^β` as the
     QB-2 credence and of `T^{α,O}` as the QB-1 target at the cycle horizon.
   - **OQ-12, the governance form.** A research run on a disposable branch, not a §A.39 native V3 round, with no
     `v3-round` or `v3-governed-paths` block, and its freeze the owner-designated exact commit `F`. The proposed home
     of the frozen files.

***

## 9. Limitations: what C-1 can and cannot show

- **Scope of the comparison.**
  - The assessment's B3 and CE-8 already show that on generic finite bijections β's numbers need not be single-orbit
    frequencies (BSB:129–142, BSB:248).
  - C-1 asks only whether the native wave dynamics behaves like that at the eleven frozen sizes: `d = 1`, `a = 1`,
    `q ∈ {2, 3}`, `L ≤ 8`, one contiguous region, the visible content fixed by OQ-2.
  - Neither verdict extends to larger `L`, to `d ≥ 2`, to `d = 3` (the manuscript instance), to other couplings, to the
    rounded rule, or to other regions or splits.
  - At `d = 1` the instances are outside posit (v)'s splitting clause (`d ≥ 2`, BSB:225; Main:726).
- **Cycle horizon only.** By Lemma A, the frequencies compared are those over a whole cycle of the orbit, of order up
  to the recurrence time, which no accessible window reaches (BSB:259; Main:141). C-1 says nothing about
  accessible-window frequencies, which are C-3's subject.
- **No selection.**
  - A FREQ verdict would show that, on those instances, the Born-form numbers coincide with every long orbit's cycle
    frequencies, so that the identity of the actual orbit does not matter for one-step numbers there.
  - A FREQ verdict would not derive β, select a measure, or supply a premise. That is the (Q-sel) question
    (BSB:77–79), which C-1 leaves where BSB:181 left it.
  - A NOT verdict would show that the Born-form numbers are not the cycle frequencies of at least one admissible orbit.
    Under QB-1, β's numbers would then need a further premise to be the operational target on that instance, such as
    a typicality hypothesis or a selection of the actual orbit. A NOT verdict says nothing about which orbit is actual.
- **Interaction with QB-1.**
  - QB-1 makes operational frequencies the target and denies that credences establish a Born law by themselves.
  - C-1 compares the credence side (`T^β`, via QB-2) with the frequency side at the cycle horizon only. So FREQ cannot
    establish a Born law under QB-1 either: it establishes a coincidence of numbers at a horizon no observer reaches.
  - The one-step numbers are not the Born exponent: the native Born weights `|U_φ|²` lie in `{0, 1}` under every
    branch (BSB:117–121), and C-1 does not touch interface (a).
- **`ℓ_min` is a proxy for C3.** The rule `n + 1` is a necessary condition for an orbit to carry hidden capacity, not
  a characterization of observer-bearing orbits. Other thresholds can change the verdict (CC-SHORT shows the mechanism).
  The verdict is valid only at the frozen threshold.
- **Present-visible records only.** The credence side is β conditioned on `x₀`. Records of longer histories change
  both sides (BSB:250–256, Lemma A3) and are not tested.
- **P-divisibility record.** By Lemma PD it is a function of whether `T^{α,O}` is a 0/1 matrix, so it adds no
  information independent of the comparison data. It carries no verdict.
- **Calibration of the tool.** The controls are constructed toys with hand-derived values. A complete run shows that
  the implementation reproduces them and that the native `φ` matches the hand-derived steps. It does not show that the
  rule behaves as intended on inputs unlike the controls.
- **Consistency axis.** Whatever the verdict, it moves no correctness band (§A.23). A halted run establishes nothing
  about the wave substratum.
