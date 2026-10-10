# RANK: the affine rank of the infinite-lattice protocol completion — RESULT (read-only)

**Base.** `0f2687b7b87925b53c6e3d8c6d1a233f36624dea`.

**What was not done.** No branch, round, preregistration, repository edit or GitHub write.

**Evidence levels.**
- **exact**: integer counts, with ranks over ℚ by fraction elimination. A rank over F_p is an exact **lower bound**
  for the rank over ℚ, since any nonzero minor mod p is a nonzero integer minor. Two primes are used, and they agree
  everywhere.
- **written**: an argument given here.

**Scripts**, all in `scratchpad/rank/`, all deterministic:
- `lattice_rank.py`: passive Hankel ranks;
- `protocol_rank.py` and `protocol_L3.py`: ranks with actions;
- `r0_check.py`: the rank identity R0;
- `certain.py`: deterministic continuations.

**Substratum.** The second-order (leap) rule of the corpus on ℤ, v^{t+1}_i = F(v^t)_i + v^{t−1}_i (mod 2), with
readout v₀ at one site. The measure is the uniform product measure, which every bijective cellular automaton
preserves. Three choices of F:

| rule | F(v)_i | type |
|---|---|---|
| linear | v_{i−1} + v_{i+1} | linear |
| nonlinear | v_{i−1}v_{i+1} + v_i | the earlier OI-STAGE case |
| majority | maj(v_{i−1}, v_i, v_{i+1}) | nonlinear |

**Method.** The rule is time-symmetric, so the uniform pair (v⁰, v¹) on [−(n−1), n−1] determines v₀ at 2n
consecutive times. That is exact for the infinite lattice through the causal cone (RegionTower:283), and it costs
2^{4n−2} configurations instead of 2^{8n+2}. The method reproduces the earlier OI-STAGE ranks 1, 4, 6 independently.

***

## 0. Verdict

1. **R0 (written proof; exact on six instances).** CMP-1's `FiniteRank` is exactly finiteness of the
   protocol-probability matrix:

   dim aff{prepVec x} = rank [p(e | x)] − 1 = rank [joint probability(x, e)] − 1,

   with both sides infinite together. For passive preparations of a stationary process, the joint matrix is the
   classical Hankel matrix.
2. **The nonlinear rule: a rigorous lower bound, and growth through n = 8.**

   | n | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
   |---|---|---|---|---|---|---|---|---|
   | rank H_n | 1 | 4 | 6 | 11 | 21 | 50 | 89 | 154 |

   - Ranks are over ℚ for n ≤ 4 and over F_p (a lower bound) for n ≥ 5.
   - So any finite predictive-state representation of this rule's passive visible process has dimension at least
     154, and **the raw completion has affine dimension ≥ 153**.
   - It is therefore **not** a qubit body (dimension 3), nor the state space of any d-level quantum system with
     d² − 1 < 153, i.e. d ≤ 12.
   - Unboundedness is **not proved**. The growth (ratio ≈ 1.7 per step) is strong evidence, and the obvious proof
     route fails (§3.3).
3. **The majority rule: 1, 4, 8, 16, 32, 64, 120** through n = 7, close to the maximum 2^n at every horizon.
4. **The linear rule: the passive rank is 1 at every horizon (written proof; exact to n = 8).** The rule is permutive
   at the edges, so each visible bit carries a fresh uniform bit. The passive completion is a single point.
   - **Actions raise the rank.** With flip and swap actions at the site, the full protocol tower has rank 3 at L = 2.
     L = 3 is in §4.
   - So passive rank and full-protocol rank genuinely separate.
5. **The nonlinear rule's passive and full-protocol ranks agree at L ≤ 2** (both 4). L = 3 is in §4.
6. **No finite quotient that keeps the readout and the time step.** Any operation-closed quotient that keeps the
   readout and the time step contains every passive future effect, so its rank is at least rank H_n for every n
   (written). For the nonlinear rule that is at least 154. A finite-dimensional quotient would have to drop the time
   step or the readout, or restrict the preparations.

***

## 1. R0: CMP-1's FiniteRank equals the rank of the protocol matrix

**Setting.** D : `DirectedStages` with SC∞. M(x, a) = `val D a x` for x ∈ `Prep D` and a ∈ `Label D`. Its rows are
the vectors prepVec x ∈ ℓ^∞. The rank of M is the dimension of its row span in ℝ^{Label}, which equals the supremum of
the ranks of its finite submatrices: finitely many vectors of ℝ^{Label} are independent iff they are independent on
some finite set of coordinates.

**Claim.** `FiniteRank (body D)` ⟺ rank M < ∞, and then finrank(direction(affineSpan(body D))) = rank M − 1.

**Proof (written).**
1. **The body and the preparation vectors have the same affine span.** Let S = range prepVec. Then
   affineSpan(body) = affineSpan(S).
   - ⊇ holds because S ⊆ body (`prepVec_mem_body` SC:167).
   - ⊆: if affineSpan(S) is finite-dimensional it is closed and contains conv S, so it contains the closure, which is
     the body.
   - If affineSpan(S) is infinite-dimensional, so is the larger affineSpan(body).
2. **The span is one dimension bigger.** S lies in the hyperplane {f : f(unit) = 1}, which misses 0 (`val_unit`
   SC:198). For such a set, dim span S = dim affineSpan S + 1.
3. **The span is the row span.** span S is the row span of M, so its dimension is rank M.
4. **Joint form.** In a protocol tower M(x, e) = J(x, e)/w(x), with w(x) = μ(C_x) > 0. Scaling rows does not change
   rank, so rank M = rank J. For passive preparations of a stationary process, J(h, f) = P(hf), the Hankel matrix.

**Exact check (`r0_check.py`).** On the OI-STAGE toy tower, stages 2 and 3: (dim aff, rank) = (2, 3) and (3, 4). On
the nonlinear lattice tables for n = 1 … 4, dim aff = rank − 1 with ranks 1, 4, 6, 11. Conditional and joint ranks
agree in every case.

**Kernel cost.** Moderate. It needs the finite-submatrix characterization of rank for vectors in an `lp` space.

***

## 2. The linear rule: passive rank 1 (written proof; exact n ≤ 8)

- With F = v_{i−1} + v_{i+1}, the coefficient of v⁰_{t} in v^{t}_0 is 1, by induction along the right edge of the
  cone.
- The earlier bits v^{1..t−1}_0 do not involve v⁰_t, because the cone has radius t − 1.
- So each visible bit is uniform and independent of the earlier ones: the visible process is i.i.d.
- Hence H_n has rank 1 and the passive body is a single point.
- Exact checks: rank 1 for n = 1 … 8, and P(0^m) = 2^{−m}.

**With actions** (the full protocol, `protocol_rank.py`):
- L = 2: rank 3 with 31 preparations.
- **Why actions add rank.** A swap of (u₀, v₀) can make a read return a stored copy instead of a fresh bit.
- **Why they may stay bounded.** Information sent to the neighbours is masked by fresh edge bits, so a bound by the
  centre memory (at most 4 states) is plausible but not proved. L = 3 is in §4.

***

## 3. The nonlinear rule

### 3.1 Exact data

| quantity | value |
|---|---|
| passive rank H_n, n = 1 … 8 | 1, 4, 6, 11 (over ℚ), 21, 50, 89, 154 (over F_p, two primes) |
| P(0^m) · 2^{30}, m = 0 … 16 | 2^{30}, 2^{29}, 2^{28}, 3·2^{26}, 9·2^{24}, 7·2^{24}, then constant |
| Hankel rank of the scalar sequence P(0^{i+j}) | 6 (it does not grow) |
| full protocol (flip and swap) vs passive | L = 2: 4 vs 4 (L = 3 in §4) |
| certain continuations of length m (pasts of length 7) | 2, 4, 3, 1, 1, 1, 1 for m = 1 … 7 |

### 3.2 Structure (written, exact where stated)

Write x = v₀, a = v_{−1}, b = v_{+1}.
1. **The centre equation.** x_{t+1} + x_t + x_{t−1} = a_t b_t. The visible record determines the products a_t b_t
   exactly.
2. **The neighbours decouple during zeros.** While x_t = 0, the columns a and b run on their own:
   a_{t+1} = a_t + a_{t−1}, of period 3, and likewise for b. The outer columns reach a and b only at times when
   x_t = 1.
3. **Freezing.** Five consecutive visible zeros force zeros forever, since a_t b_t = 0 then holds at three
   consecutive times of a period-3 pattern. That is why P(0^m) is constant from m = 5 (exact). The absorbing frozen
   sector has probability 7·2^{−6}.
4. **Where the memory lives.** Unbounded memory, if it exists, must come from the outer columns, which reach the
   centre only through 1s in the record. That is the mechanism the growth of H_n reflects.

### 3.3 Two directions, both attempted

**A finite sufficient statistic: none found.**
- A finite predictive-state representation of dimension r bounds every H_n by r. H_8 = 154 rules out r < 154.
- The finite statistics that do exist are sub-sectors with finite memory:
  - the frozen sector, which is why the scalar Hankel rank is 6;
  - the centre pair while the record is zero.

  Neither bounds the whole process.

**An unbounded lower bound: not proved.** Two routes were tried.
- **Certain continuations.** If K distinct futures of length m are each certain after some past, rank ≥ K. The
  counts are bounded (above): they are frozen periodic patterns. The majority rule has the same feature, with 4
  certain futures for each m ≥ 4. **This route fails** for both rules.
- **Scalar recurrences.** If the rank r is finite, every k ↦ P(u w^k v) satisfies a linear recurrence of order ≤ r.
  - Zero runs freeze, so the family w = 0 gives only 6.
  - Cylinder probabilities decay only exponentially (at least 2^{−O(m)}), so super-exponential decay is not
    available as a criterion either.

**What a proof would need.** A family of pasts that store k independent bits in the outer columns and release them
through 1s at distinct later times. This is the open mathematical step.

***

## 4. Full protocol at L = 3, and the passive/protocol separation

Ranks are over F_p (lower bounds, two primes agreeing), from `protocol_rank.py`/`protocol_L3.py` with the exact
cone radius per protocol. "Preparations" counts the positive-probability (protocol, record) pairs.

| rule | action set | L = 1 | L = 2 | L = 3 |
|---|---|---|---|---|
| linear | passive (observe only) | 1 | 1 | 1 |
| linear | observe + idle | 1 | 1 | 1 |
| linear | observe + flip | — | — | 1 |
| linear | observe + swap | — | — | 3 |
| linear | full (observe, idle, flip, swap) | 1 | 3 | 3 |
| nonlinear | passive | 1 | 4 | 6 |
| nonlinear | observe + idle | 1 | 4 | 6 |
| nonlinear | observe + flip | — | — | 6 |
| nonlinear | observe + swap | — | — | 7 |
| nonlinear | full | 1 | 4 | 7 |

- **Passive and full-protocol ranks separate** (linear: 1 versus 3), so the linear rule's controlled theory is not
  trivial even though its passive completion is a point.
- **Only the swap adds dimension.** Idle adds nothing (it is already implicit in observation spacing). The flip adds
  nothing: inverting the visible bit creates no new distinguishable history. The swap, which exchanges the two
  layers at the visible site and so reads a stored copy, adds exactly one dimension in both rules at L = 3.
- **For the nonlinear rule the full-protocol rank is bounded below by the passive rank**, 154 at horizon 8, since
  the passive table is a submatrix. The action calculations change nothing about that bound.
- The linear full rank, 3 at L = 2 and L = 3, is consistent with a bound by the four states of the visible site's two
  layers, but no bound is proved.


***

## 5. What this means for the roadmap (for the owner)

- **The rigorous part.** The raw passive completion of the nonlinear rule has affine dimension at least 153. That
  already excludes it as a qubit-sized body, whether or not the rank is finite.
- **The likely situation.** For a nonlinear rule, with exact evidence for two of them: FiniteRank fails for the raw
  completion. By R0 and §0.6, no quotient closed under the readout and the time step can repair this.
- **What a finite-dimensional operational quotient must give up.** At least one of:
  - the time step as an operation — e.g. restrict to a fixed horizon, though then the quotient is not closed under
    W;
  - the readout itself — keep only coarser effects;
  - the full preparation set — e.g. preparations in a sub-sector such as the frozen or decoupled-centre sectors,
    which have finite memory.

  This should be decided explicitly before CMP-1/OPACT-1 are retargeted. Nothing here weakens FiniteRank.
- **The open mathematical item.** An unbounded lower bound for the nonlinear rule (§3.3). It would turn "the raw
  completion is not qubit-sized" into "the raw completion is infinite-dimensional".

***

## 6. The analytic lower-bound search (started; majority first, as directed)

### 6.1 R2: a decay criterion for infinite rank (written proof + citation)

**Statement.** Suppose a stationary process has Hankel rank r < ∞. Then:
1. It has an r-dimensional observable-operator representation, P(v₁…v_k) = σ τ_{v_k} ⋯ τ_{v₁} w₀ (Heller 1965;
   Jaeger 2000; citation).
2. Hence, for any words u, w, v, the sequence s_k = P(u w^k v) = σ τ_v τ_w^k τ_u w₀ obeys the linear recurrence of
   the characteristic polynomial of τ_w, of order ≤ r. Finite sums of such sequences obey one as well.
3. A real linear-recurrent sequence that converges to a limit L does so **exponentially fast**.
   - s_k − L = Σ p_i(k) λ_i^k.
   - The part with |λ_i| ≥ 1 tends to 0 only if it vanishes identically, because exponential polynomials with
     unimodular frequencies are almost periodic.

**Criterion.** If any such sequence, or finite sum of them, converges sub-exponentially, the rank is infinite.
Through R0, `FiniteRank` then fails for the raw completion.

### 6.2 The shared mechanism of the two nonlinear rules (exact, elementary)

**The local rules.**
- **Majority:** maj(v_{i−1}, v_i, v_{i+1}) = v_i whenever site i agrees with at least one neighbour.
- **Nonlinear:** F_i = v_i whenever v_{i−1}v_{i+1} = 0.

**Period-3 columns where the condition holds (exact).** Wherever that local condition holds, the column obeys
x_{t+1} = x_{t−1} + x_t, i.e. period 3. Call a site where the condition fails a *defect*: an isolated value for
majority, two neighbouring 1s for the nonlinear rule.

**But no domain picture.** A Monte Carlo census (`defects.py`; evidence) **does not** show quiescent domains
separated by moving defects:
- In the stationary measure, defects have density 0.250 in both rules. That is exactly the density for a uniformly
  random row.
- Their space–time correlations stay within |dx| ≤ 1 (majority) or |dx| ≲ 4 (nonlinear), and do not spread with the
  time lag up to 32. There is no ballistic and no diffusive motion.
- So the period-3 stretches at the visible site are local events, not domain interiors.

**The R2 family.** The persistence of a fresh stretch is still a finite sum of sequences of the R2 form, so finite
rank would force exponential convergence.

### 6.3 Evidence (Monte Carlo — not exact, not a proof): inconclusive

**Setup.** Survival S(m) of a fresh period-3 stretch at one site. A ring of 200,000 sites, exact for the horizon by
the causal cone. 1,500 independent initial configurations, giving about 1.1·10⁸ starts (`persist_mc.py`,
`persist_majority_big.txt`).

**Majority.**

| m | 16 | 32 | 48 | 64 | 80 | 96 | 112 | 128 |
|---|---|---|---|---|---|---|---|---|
| S(m) | 6.2e−4 | 6.7e−5 | 1.4e−5 | 4.4e−6 | 2.1e−6 | 9.5e−7 | 4.5e−7 | 2.3e−7 |

- The local exponential rate −Δ ln S/Δm falls from about 0.18 (m ≈ 10) to about 0.10 (m ≈ 40).
- It then **levels off at 0.042–0.049 over m = 64 … 128**.
- The local power-law exponent keeps rising, from 3.3 to 5.0, so a power law is excluded.
- What remains consistent with the data is an exponential tail of rate ≈ 0.045, reached after a long transient. A
  stretched exponential is not excluded either.
- An earlier, five-times-smaller run suggested exp(−c√m). **The larger run does not support that reading.**
- So this observable gives **no evidence of infinite rank** under R2 at the accuracy reached. A rate that settles
  exponentially is what finite rank predicts, although it does not imply finite rank.

**Nonlinear.**
- S(16) = 4.8e−4, S(24) = 2.0e−5, S(32) = 3.1e−6; no events at m = 48.
- The decay is fast. The statistics beyond m ≈ 32 are too thin to fit.

### 6.4 Where the analytic search stands

**The first route is unsupported.** Persistence of quiescent stretches under R2 had a single word family as its
target. The data are consistent with an exponential tail, which finite rank permits. R2 still stands as a valid
criterion, but this family does not trigger it.

**The rank growth is real and needs another mechanism.** Ranks 1, 4, 8, … 64, 120 for majority at least are exact.
Infinite rank is compatible with every single family P(u w^k v) converging exponentially, because the decay rates can
vary without bound across families.

**The next analytic steps:**
1. **Defect kinematics, done (§6.2): negative.** There are no moving defects and no domain structure, so there is
   no defect-gas model to build on.
2. **Triangular families, still the target, but without a mechanism yet.** Pasts that certify a defect's position and velocity; for example, an observed
   passage at the visible site fixes its distance at a later time. Futures that detect its effect at a determined
   time. Together these give zero patterns P(f_j | h_i) = 0 for j > i and > 0 for j = i, hence rank ≥ i for every i.
3. **Zero sets: scanned (exact), negative.**
   - By Skolem–Mahler–Lech, finite rank forces every zero set {k : P(u w^k v) = 0} to be a finite union of arithmetic
     progressions plus a finite set. A non-periodic zero set would prove infinite rank exactly.
   - `zeroscan.py` scanned every u, v of length ≤ 2 and w of length 1–2 against the exact n = 8 tables (window 16).
   - Every pattern found is eventually periodic, mostly "eventually zero". There is no candidate.
4. **Exact verification** of any candidate family on the n ≤ 8 tables, before attempting a proof for all n.

**Not done.** None of the three steps. Unbounded rank remains unproved for every rule. The proved results are the
finite lower bounds (≥ 154 for the nonlinear rule, ≥ 120 for majority), R0 and R2.

***

**Scope note.** A1's finite representative is a gauge for statistics determined by finite visible and boundary
data. The completion and all-horizon geometry studied here are not known to be invariant under that gauge: on a
finite representative the body is a polytope (NG1), while the infinite lattice gives the growing ranks above. The
full refinement is maintained separately in the design constraints, not here.
