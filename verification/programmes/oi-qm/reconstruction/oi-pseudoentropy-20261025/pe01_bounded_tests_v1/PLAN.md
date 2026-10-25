# PE-01 stage plan: bounded tests on one fixed generator family (v1)

Stage plan for PE-01 of thread OI-PE-1 (`../README.md`). It is pinned before any PE-01 code exists and is committed alone.
Drafted on `research/oi-pseudoentropy-20261025` at `25e77a3cbd81cd10cd5161dca94d1da6f2a01eb5`. Corpus line numbers are at
the thread's drafting snapshot `c37700ad`. `papers/` and `book/` are unchanged between the two commits.

**Question.** For one fixed finite reversible realization, which observational restrictions keep the visible record
indistinguishable from a fixed random reference, and up to which horizon? The comparison begins with bounded tests.
The unrestricted observer is computed only as a calibration and countercontrol, because its outcome is already
covered by `Structure.md:1256` and `Main.md` §3.4 (`../README.md`, "What the corpus already settles").

## 1. Objects

**Template.** Let $\mathcal{C}_V = \{0,1\}$ and $\mathcal{C}_H = \mathbb{F}_2^n$. Each generator is $\varphi = \tau_f \circ \kappa_\sigma$, where:
- $\kappa_\sigma(x,h) = (x, \sigma_x(h))$, with $\sigma_0, \sigma_1$ bijections of $\mathbb{F}_2^n$;
- $\tau_f(x,h) = (x \oplus f(h), h)$.

Both factors are fibrewise bijections, so $\varphi$ is a bijection by construction (checked as EX1).
- The visible output map is $\pi_V(x,h) = x$.
- The record at horizon $K$ is $X_{0:K}$: $K+1$ symbols over $K$ steps.
- The increments $Y_t = X_{t+1} \oplus X_t = f(h_{t+1})$ are the generator's output stream.

Let $L_p$ be the Fibonacci companion map of a primitive $p$ of degree $n$:
$(h_0,\dots,h_{n-1}) \mapsto (h_1,\dots,h_{n-1}, \sum_i c_i h_i)$. Set $\ell(h) = h_0$ and $g(h) = h_0 \oplus h_1 h_2$.

| Name | $\sigma_0$ | $\sigma_1$ | $f$ | Role |
|---|---|---|---|---|
| `G_lin(p)` | $L_p$ | $L_p$ | $\ell$ | primary: linear, autonomous hidden dynamics |
| `G_filt(p)` | $L_p$ | $L_p$ | $g$ | nonlinear comparator: balanced quadratic filter |
| `G_clk(p)` | $L_p$ | $L_p^2$ | $\ell$ | nonlinear comparator: visible-to-hidden backaction (self-clocked) |
| `G_lin(p')` | $L_{p'}$ | $L_{p'}$ | $\ell$ | negative-control sibling that keeps the stated reason |
| `G_dec(p)` | $L_p$ | $L_p$ | $0$ | positive-control target. It is visible-decoupled and violates (C1). |
| `G_tape(N)` | clock | clock | tape read | negative-control mutant that removes the reason (form of `Main.md:496`) |

`G_tape(N)` is defined as follows:
- $\mathcal{C}_H = \{0,1\}^N \times \mathbb{Z}_{N+1}$;
- $\sigma_x(u,c) = (u, c+1)$;
- $f(u,c) = u_{c-1}$ for $1 \le c \le N$, and $0$ for $c = 0$. Then $Y_t = u_t$ for $t < N$, so $X_{0:K}$ is exactly
  uniform for $K \le N$.

The polynomials are fixed. $p_n$ is primary, and $p'_n$ is its reciprocal, used for the sibling.

| $n$ | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|
| $p_n$ | $z^3{+}z{+}1$ | $z^4{+}z{+}1$ | $z^5{+}z^2{+}1$ | $z^6{+}z{+}1$ | $z^7{+}z{+}1$ | $z^8{+}z^4{+}z^3{+}z^2{+}1$ |
| $p'_n$ | $z^3{+}z^2{+}1$ | $z^4{+}z^3{+}1$ | $z^5{+}z^3{+}1$ | $z^6{+}z^5{+}1$ | $z^7{+}z^6{+}1$ | $z^8{+}z^6{+}z^5{+}z^4{+}1$ |

**Initial law.** $\mu$ is uniform on $\mathcal{C}_V \times \mathcal{C}_H$. That is the maximal-entropy invariant measure, posit
(iv) of `Main.md:708`. `G_tape` instead uses a uniform tape with the clock at $0$, the prior form of `Main.md:496`.

**Why these objects.** The controls need known structure:
- **`G_lin`.** Its record is an $\mathbb{F}_2$-linear image of the seed. Its windows of up to $n+1$ symbols are exactly
  uniform: $\mu$ is uniform and $(\ell, L_p)$ is observable. Its linear complexity is at most $n+1$. That gives one
  exact zero (the positive control) and two exact firing reasons (the negative controls).
- **`G_filt`.** It adds nonlinearity and keeps the hidden dynamics autonomous.
- **`G_clk`.** It adds dependence of the hidden trajectory on the visible bit. It is the only generator here whose
  hidden trajectory visible-sector interventions change.

Every primary generator satisfies T-level (C1): the one-step visible matrix under $\mu$ is a non-permutation (EX6).

**Families for K0.** $\mathfrak{F}_{\rm lin}(n)$, $\mathfrak{F}_{\rm filt}(n)$ and $\mathfrak{F}_{\rm clk}(n)$ each range over
all primitive $p$ of degree $n$, with $\ell$ and $g$ fixed. $\nu$ is uniform on each family.

**Parameter and horizon ranges (fixed).**

| Item | Range |
|---|---|
| $n$ | $3,\dots,8$ (local $n \le 6$, CI $n = 7, 8$) |
| $K$ | $0 \le K \le K_{\max}(n) = 4(2^n - 1)$, except where a class's row in §3 sets a smaller cap |
| $m$ (observer memory) | exhaustive: $m \le 2$; $m = 3$ passive, up to conjugacy (CI, $n \le 6$); linear-filter observers $m \le 4$ (CI) |
| $\delta$ | $1/8$ and $1/4$ |
| Runs $r$ | 1 |

## 2. Advantage

**Reference law.** $Q$ is fixed: independent fair visible symbols. This is a pseudorandomness-type notion. For a
protocol $p$, $Q_p$ is the process in which each generator step's visible output is replaced by a fresh fair bit,
independent of everything else, settings included. The class form $\mathcal{Q}$ (HILL-like or metric-like) is not
computed in PE-01 (see §10).

**Single test.** For a Boolean, deterministic test $D$ on the record of protocol $p$ at horizon $K$:
$$\mathrm{adv}_D(\varphi) = \bigl|\Pr_{P^{\varphi,\mu}_{p,K}}[D=1] - \Pr_{Q_{p,K}}[D=1]\bigr|.$$
A **prediction test** guesses $\chi(X_{0:K-1})$ and outputs $D = 1[\chi = X_K]$. Then $\Pr_Q[D=1] = 1/2$ exactly, and
$\mathrm{adv}^{\rm pred}_D = |\Pr_P[\chi = X_K] - 1/2|$.

**Knowledge levels** (`../README.md`, K0/K1).
- **K1:** $\mathrm{adv}^{K1}_{\mathcal{D}}(\varphi,K) = \max_{D \in \mathcal{D}} \mathrm{adv}_D(\varphi)$.
- **K0, worst case:** $\max_{D \in \mathcal{D}} \min_{\varphi \in \mathfrak{F}} \mathrm{adv}_D(\varphi)$, with $D$ chosen once,
  before $\varphi$.
- **K0, average case:** $\max_{D \in \mathcal{D}} \mathbb{E}_{\varphi\sim\nu}\, \mathrm{adv}_D(\varphi)$.

Both K0 forms are reported, over deterministic tests. Randomized mixtures of tests are not computed in PE-01.

**Settings.** Passive classes have none. In the embedded class, the settings are the observer's interventions, as
follows:
- they are functions of its own memory, so they enter the record through its final state;
- the same policy defines $Q_p$;
- they are measurement-independent because the joint prior is the product of $\mu$ with a fixed prepared memory state
  (EX7).

**Reported horizons.** Each class, knowledge level, generator, $n$ and $m$ gets two horizons:
- $K_{\rm zero}$, the largest $K$ with $\mathrm{adv} = 0$ exactly at every $K' \le K$;
- $K_\delta$, the least $K$ with $\mathrm{adv} \ge \delta$.

Together with the full exact curve, these answer "for how long".

**Record entropies.** The record law is reported as its exact count multiset, so $\max P$, and with it $H_\infty$, is
exact. $H$ is printed for display only and never enters a verdict.

## 3. Observer classes, all on the same generators

**U: unrestricted** (all Boolean tests on $X_{0:K}$). This is the calibration and countercontrol.
- K1 is the exact TV, computed from support counts, together with the exact K1 Bayes next-symbol predictor curve.
- K0 worst case over $\mathfrak{F}$ is reported as an interval. Its lower end is the exact value of the explicit test
  $D_\cup = 1[X_{0:K} \in \bigcup_{\varphi\in\mathfrak{F}} \mathrm{supp}\,P_\varphi]$. Its upper end is
  $\min_{\varphi \in \mathfrak{F}} \mathrm{TV}(P_\varphi, Q)$.
- The K0 value is exact only where the two ends coincide. Otherwise the interval is reported and bears on no verdict.

**B: computationally bounded, named structured classes.** No circuit-size class is used in PE-01.

| Class | Tests | Exact computation and limits |
|---|---|---|
| B1 linear | $D_T = \bigoplus_{t\in T} X_t$, $\emptyset \ne T \subseteq [0,K]$ | All $T$ via an integer Walsh–Hadamard transform for $K \le 23$. For larger $K$, only the bias-$\pm1$ tests are covered, via the $\mathbb{F}_2$ affine hull of the support; this gives a lower bound. |
| B2 Berlekamp–Massey | $D_\lambda = 1[\mathrm{LC}(X_{0:K}) \le \lambda]$, $0 \le \lambda \le K+1$ | $\Pr_P$ by enumeration. $\Pr_Q$ by the closed-form count $N_N(0)=1$, $N_N(L) = 2^{\min(2L-1,\,2N-2L)}$ for $1 \le L \le N$, with $N = K+1$. $D_\lambda$ does not depend on $\varphi$, so K0 fixes $\lambda$ before $\varphi$, and K1 maximises over $\lambda$ per $\varphi$. |
| B3 $k$-wise / window | all tests on any $k \le 3$ positions ($K \le 127$); all tests on any window of $w \le 16$ consecutive positions | exact marginal TV, maximised over position sets |
| B4 low degree | $D_q = 1[q(X)=0]$ for $q \ne 0$ of degree $\le d$ vanishing on $\mathrm{supp}\,P_K$; $d=1,2$ for $K \le 255$, $d=3$ for $K \le 63$ | The least $K$ at which an annihilator exists, by exact $\mathbb{F}_2$ elimination (binary search, since existence is monotone in $K$). The certified bound is $\mathrm{adv} \ge 2^{-d}$ (Reed–Muller minimum distance). The exact maximum is computed only where the annihilator space has dimension $\le 20$. |

**𝒫ᵉᵐᵇ(m): physically restricted OI observers.** The visible sector is enlarged to
$\{0,1\}_{\rm sys} \times \{0,1\}^m_{\rm mem} \times \{0,1\}_{\rm out}$, so the observer's footprint is $m+1$ bits.

An observer is $(\rho_0, \rho_1, a, F)$:
- $\rho_x \in \mathrm{Sym}(\{0,1\}^m)$;
- $a: \{0,1\}^m \to \{0,1\}$ (the passive subclass has $a \equiv 0$);
- $F \subseteq \{0,1\}^m \times \{0,1\}$;
- the prepared initial memory is $v_0 = 0^m$, and the output bit starts at $0$.

Each round $t < K$ applies three maps:
1. $v \leftarrow \rho_x(v)$;
2. $x \leftarrow x \oplus a(v)$;
3. $(x,h) \leftarrow \varphi(x,h)$.

At $K$: $\mathrm{out} \leftarrow \mathrm{out} \oplus 1[(v_K, x_K) \in F]$.

Every map is a bijection of $\mathcal{C}_V' \times \mathcal{C}_H$, and the observer's maps act as the identity on
$\mathcal{C}_H$. There is no hidden-sector access (`Computation.md:15`).
- **Time-invariance.** The observer's rule is time-invariant because it is part of the one fixed dynamics
  (`Main.md:560`: "One dynamics; the program is paid for as an initial condition, not obtained free"). A time-dependent
  rule is realized by a time-invariant one with a clock in memory, and the footprint counts that clock.
- **Evaluation time.** $K$ is the evaluation time, not a clock the observer holds.
- **Prediction tests.** $v_K$ depends on $X_{0:K-1}$ only. The prediction subclass is therefore $F$ equal to the graph of
  some $\chi(v)$.

The enumerated subclasses are:
- all observers with $m \le 2$: 16 at $m=1$ and 9216 at $m=2$, each with every $F$;
- passive observers with $m = 3$, up to simultaneous conjugacy fixing $v_0$;
- linear-filter observers $\rho_x(v) = Av \oplus xb$, with $A \in \mathrm{GL}(m,2)$ and $m \le 4$.

Named larger observers are admissible only as explicit tables, verified by EX1 and IM3. By definition, the passive
𝒫ᵉᵐᵇ(m) is a class of time-invariant permutation automata of width $2^m$. PE-01 asserts no relation between it and
the B classes. That relation is PE-02's question.

## 4. Controls

- **PC (positive, non-vacuous).**
  - **The zero.** Every class above is evaluated on `G_lin(p_n)` at every $K \le n$. Each must return
    $\mathrm{adv} = 0$ exactly. This is proved independently: $X_{0:n}$ is an invertible linear image of a uniform
    vector (EX5).
  - **The firing.** Each class must also fire on `G_dec`, whose record is constant. It must reach the exact value its
    closed form gives on the constant record, at $K = 1$:
    - U: $1/2$;
    - B1: $1/2$;
    - B2 at $\lambda = 1$: $1/4$;
    - B3: $1/2$;
    - B4 at $d = 1$: $1/2$;
    - 𝒫ᵉᵐᵇ(1), via $\rho_0 = \mathrm{id}$, $\rho_1 = $ flip, $a \equiv 0$ and $F = \{v = x\}$: $1/2$.
- **NC-1 (support, U at K1).**
  - On `G_lin(p_n)` and `G_lin(p'_n)`, the TV must equal $\max(0, 1 - 2^{n-K})$ exactly. The reason is that the record
    determines the seed for $K \ge n$, so $|\mathrm{supp}| = 2^{n+1}$.
  - The mutant `G_tape(K_max)` removes the support deficit. It must give $\mathrm{adv} = 0$ for every class and every
    $K \le K_{\max}$.
- **NC-2 (linear complexity, B2 at $\lambda = n+1$).**
  - The reason is that $\mathrm{LC}(X_{0:K}) \le n+1$ surely, because the minimal polynomial divides $(1+z)p(z)$.
  - On both siblings, the advantage must equal $1 - \Pr_Q[\mathrm{LC} \le n+1]$.
  - The mutant `G_tape` must give $0$.
  - Limitation: no mutant in this plan separates linear complexity from support size. NC-2's specificity rests on the
    sibling identity and the closed form.
- **Exactness and implementation.** EX1–EX7 and IM1–IM5 in §5.
- **Symmetry (§A.21).** `G_lin`, `G_filt`, `G_dec` and `G_tape` commute with the global flip $x \mapsto x \oplus 1$, and $\mu$
  is flip-invariant. Their record laws, and $Q$, must therefore be complement-invariant exactly. `G_clk` does not
  commute with the flip and is exempt.

## 5. Invariant → checkpoint (§A.41)

Every numerical row is computed in exact integer or `Fraction` arithmetic. Failing any row makes the stage VOID (§6).

| Invariant | Checkpoint | Measured by |
|---|---|---|
| Every $\varphi$, mutant and observer composite is a bijection | EX1 | image cardinality equals the domain size. All generators are checked at every $n$. Composites are checked exhaustively at $n \le 4$, and for every verdict-bearing witness. |
| $\mu$, every $P$ and every $Q$ sum to 1 | EX2 | exact sum |
| No float on the verdict path | EX3 | a type assertion on every verdict input |
| $p_n$ and $p'_n$ are primitive | EX4 | order of $z$ is $2^n-1$ |
| $(\ell, L_p)$ is observable | EX5 | $\mathbb{F}_2$ rank $n$ |
| T-level (C1) holds for the primary generators and fails for `G_dec` | EX6 | exact one-step visible matrix |
| Settings are measurement-independent | EX7 | the joint prior factorises as $\mu \otimes \delta_{v_0}$ |
| BM is correct | IM1 | agrees with brute-force minimal-LFSR search on all sequences of length $\le 12$ |
| The LC count formula holds | IM2 | agrees with enumeration of $\{0,1\}^N$ for $N \le 20$ |
| The embedded simulation is correct | IM3 | the aggregated transfer computation and a full-state simulation of the composite bijection agree for all observers at $n \le 4$ and for every verdict-bearing witness |
| WHT biases are correct | IM4 | equal to direct bias computation for $K \le 10$ |
| The annihilator search is correct | IM5 | equal to brute-force polynomial search for $K \le 5$, $d \le 2$ |
| PC zero and PC firing | PC | §4 |
| NC-1 and NC-2, with their mutant and sibling | NC | §4 |
| Complement symmetry | SY | §4 |
| Inclusions | MO | Each passive class is at most U. K0 worst case is at most $\min_\varphi$ K1; K0 average is at most $\mathbb{E}_\nu$ K1. 𝒫ᵉᵐᵇ(m) is at most 𝒫ᵉᵐᵇ(m+1). Passive is at most active. B4 at $d=1$ exists iff B1 has a bias-$\pm1$ test. All are checked pointwise. |
| The K0 test is chosen before $\varphi$ | K0 | each K0 record names one test id, evaluated across all of $\mathfrak{F}$ |
| Deterministic replay (§A.26) | RP | a rerun's measurement JSON is byte-identical |
| The plan precedes the code | PIN | the measurement JSON records this file's blob id, and this commit is an ancestor of every code commit |
| Verdicts are generated from measurements | VG | the verdict is regenerated from the JSON and compared. A copy with any control flag flipped must yield VOID (self-test). |

## 6. Decision rule and outcome classes (fixed before computation)

1. **VOID.** VOID takes precedence: if any checkpoint in §5 fails, the stage verdict is VOID, it names the failed
   checkpoint, and nothing else is printed as a verdict. The controls run first, and a failure halts the stage before
   any measurement is printed.
2. **Generated text.** Otherwise `verdict.py` produces the verdict text from the measurement JSON alone. Every number in
   it is read from the measurements.
3. **Classification.** Each statement is classified as follows:
   - **PROVED (exhaustive finite).** The quantifiers range only over the enumerated scope, which is printed with it.
   - **PROVED.** Over a class beyond the enumeration, for example all $n$. This requires a written proof that passes
     independent review; the computation is then a regression, not the proof.
   - **CONDITIONAL.** The hypothesis is named.
   - **OPEN.** None of the above.

   The verification layers stay distinct.
4. **COUNTEREXAMPLE.** The universal form of `book/ch18-beyond.md:114` is that every embedded observer of every finite
   reversible realization is unable to predict. It is refuted when a witness $(\varphi, O, K)$ meets all of:
   - (a) $\varphi$ is `G_lin`, `G_filt` or `G_clk` with $n$ in range, and passes EX6;
   - (b) $O \in$ 𝒫ᵉᵐᵇ(m) is given as explicit tables and passes EX1, EX7 and IM3;
   - (c) $K \le K_{\rm cx}(\varphi) = \lfloor \ell_{\rm med}(\varphi)/2 \rfloor$, where $\ell_{\rm med}$ is the $\mu$-median orbit
     length of $\varphi$, i.e. below recurrence scale;
   - (d) $\mathrm{adv}^{\rm pred}_O(\varphi, K) \ge \delta_{\rm cx} = 1/8$, exactly;
   - (e) every control is green.

   The verdict prints the footprint $m+1$ and tags the regime: `small` if $m+1 \le n$, `large` otherwise.
   - A witness that fails only (c) is reported as a recurrence-scale measurement, not as a COUNTEREXAMPLE. At that scale
     the record's entropy is exhausted (`Structure.md:1256`), and $K_{\rm cx}$ is this plan's stated bound.
   - Distinguishing witnesses, as opposed to prediction witnesses, are reported as measurements and are not
     COUNTEREXAMPLEs.
   - No finite result here establishes the universal form (`../README.md`, Question).
5. **Productivity tag (§A.31).** Each result also gets one tag:
   - **COVERED-corpus:** class U, or anything implied by the support bound or by PC;
   - **COVERED-literature:** a B-class horizon equal to a cited closed form;
   - **candidate-NEW:** 𝒫ᵉᵐᵇ results not implied by MO together with a covered result, and K0–K1 gaps. These stay
     candidates until independent review.

   Favorable readings get the hardest scrutiny. These are $K_{\rm zero} = K_{\max}$ for an embedded class, or no
   witness found. For each, the verdict states the enumerated scope it rests on, and it does not extend that reading
   beyond the enumeration.
6. **Bounded-theorem targets.** These are questions, not expectations:
   - **T1.** An exact characterisation of $\mathrm{adv}^{\rm pred}$ for $\mathfrak{F}_{\rm lin}(n)$ against linear-filter
     observers, as a function of $(n, m, K)$.
   - **T2.** Whether active 𝒫ᵉᵐᵇ(m) reduces to passive 𝒫ᵉᵐᵇ(m′) for autonomous-hidden generators, and for which $m'$.
     `G_clk` is the case outside that hypothesis.
   - **T3.** The K0–K1 gap of B and 𝒫ᵉᵐᵇ on $\mathfrak{F}_{\rm lin}(n)$.
7. **Milestone.** The outcome is one or more of: a bounded theorem over a named class; a COUNTEREXAMPLE; a COVERED
   finding, with its covering statement cited. If none is reached, it is OPEN. VOID takes precedence over all of them.

## 7. Scope and non-claims

- Every positive (indistinguishability) result holds only for the computed class, knowledge level, generator,
  parameters and horizon. No asymptotic statement and no circuit-security statement is made.
- A COUNTEREXAMPLE refutes only the universal form. It says nothing about the realization of the actual world, nor
  about the $10^{-32}$ statement (`ch18-beyond.md:56–58`).
- No claim is made that OI guarantees cryptographic security, that deterministic dynamics creates Shannon entropy, or
  that pseudoentropy reproduces quantum mechanics.
- No identification of 𝒫ᵉᵐᵇ with any B class, or with any computational notion, is made (PE-02).
- The class-$\mathcal{Q}$ forms, $r > 1$ runs and persistent seeds across runs are out of scope (PE-02, PE-03).
- No manuscript change, workflow dispatch, theorem designation or merge is made without separate owner approval.

## 8. Resources and CI (§A.40)

Seeds number $2^{n+1} \le 512$. Generator laws, U, B2 and B3 cost seconds per generator. The cost is dominated by the
𝒫ᵉᵐᵇ sweeps and the B1 WHT.

| Work | Estimate | Where |
|---|---|---|
| EX/IM/PC/NC/SY controls; U, B1–B4 and 𝒫ᵉᵐᵇ($m \le 2$, passive) for $n \le 5$ | under 10 min | local smoke |
| B1 WHT for $K \le 23$, all generators, $n \le 8$ | about 10 min | CI |
| 𝒫ᵉᵐᵇ($m=2$, active) for $n = 6, 7, 8$: K1 with the optimal $F$; K0 over all 256 $F$, capped at $K \le 255$ | 0.5–2 h in total. Dominated by exact big-integer comparison against $Q$, which is computed once per observer and reused across $\varphi$. | CI, sharded by $(n, \text{family})$ |
| 𝒫ᵉᵐᵇ($m=3$, passive, up to conjugacy); linear-filter observers with $m \le 4$ | 1–3 h in total | CI, sharded |
| B4 with $d = 3$ | minutes | CI |

The estimates are not measurements. A local run that exceeds its row by a factor of 3 is stopped and moved to CI.
The CI job definition is part of the code commits. Dispatching it needs owner approval (§A.43, item 4). Exact
arithmetic uses Python integers and `Fraction`; numpy is used only on integer arrays.

## 9. Literature dependence (cited, not rederived)

The verdict path uses three cited results:
- **Massey 1969 (Berlekamp–Massey).** B2's test, cross-checked by IM1.
- **Gustavson 1976 and Rueppel 1986: the number of length-$N$ binary sequences of linear complexity $L$.**
  F. G. Gustavson, *IBM J. Res. Dev.* 20(3), 1976; R. A. Rueppel, *Analysis and Design of Stream Ciphers*, Springer
  1986. Used for $\Pr_Q$ in B2 and NC-2. It is cross-checked by enumeration for $N \le 20$ (IM2), and relied on as
  cited for $N > 20$.
- **Reed–Muller minimum distance (MacWilliams–Sloane).** The B4 lower bound.

Other results enter only as design rationale:
- Golomb, *Shift Register Sequences*: m-sequence window and balance properties. Every one that is used is re-verified
  exactly (EX4, EX5, PC).
- Key 1976: linear complexity of filter generators.
- Clock-controlled shift registers (Gollmann–Chambers 1989 review): the `G_clk` rationale. The bibliographic details are
  to be verified before any use.
- Fine–Wilf: the K1 calibration horizon (`../README.md`).

Other papers are cited for framing only:
- HILL 1999, BSW 2003 and RTTV 2008, for the class-$\mathcal{Q}$ forms (deferred).
- Yao 1982, for prediction against distinguishing. Prediction tests are used directly, so no reduction is relied on.
- Reingold–Steinke–Vadhan 2013 (regular and permutation branching programs), as PE-02 positioning.

Each is read in full before any closure claim relies on it (`../README.md`).

## 10. Defaults the owner may amend before code

1. $Q$ is fixed and uniform. The class-$\mathcal{Q}$ forms are deferred.
2. COUNTEREXAMPLE is based on prediction advantage. Distinguishing witnesses are reported but do not qualify.
3. Footprint is a regime tag (`small` or `large`), not an admissibility bar.
4. $\delta_{\rm cx} = 1/8$, and $K_{\rm cx} = \lfloor \ell_{\rm med}/2 \rfloor$.
5. The readout predicate costs one output bit, with no further workspace charge.

## 11. Package

This directory will hold:
- `PLAN.md`, this commit, alone;
- the code;
- `results/measurements.json` and `results/verdict.json`;
- `REPORT.md`;
- `review/`, holding an independent review.

Any amendment to this plan goes in `amendments/` before the code it governs.
