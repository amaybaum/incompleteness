# PE-01 stage plan: bounded tests on one fixed generator family (v1)

Stage plan for PE-01 of thread OI-PE-1 (`../README.md`). It is pinned before any PE-01 code exists and is committed alone.
Drafted on `research/oi-pseudoentropy-20261025` at `25e77a3cbd81cd10cd5161dca94d1da6f2a01eb5`. Corpus line numbers are at
the thread's drafting snapshot `c37700ad`. `papers/` and `book/` are unchanged between the two commits.

**Question.** For one fixed finite reversible realization, which observational restrictions keep the visible record
indistinguishable from a fixed random reference, and up to which horizon? The comparison begins with bounded tests.
The unrestricted observer is computed only as a calibration and countercontrol, because its outcome is already
covered by `Structure.md:1256` and `Main.md` §3.4 (`../README.md`, "What the corpus already settles").

**Purpose (owner).** The stage tests whether apparent randomness is unpredictable because of the observations
available, or only because the observer lacks resources. Wherever unpredictability is traced to a lack of resources, it
is reported as a limitation of the resource model (§7), not as a property of observation. Attribution follows the rule
in §6, item 4.

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
- $f(u,c) = u_{c-1}$ for $1 \le c \le N$, and $0$ for $c = 0$. Then $Y_t = u_t$ for $t < N$.

It is used as `G_tape(K)`, with $N = K$, for every $K \le K_{\rm tape} = 20$. Its prior is $x_0$ uniform, independent
of a uniform tape, with the clock at $0$. Its record law is obtained by full enumeration through the bijection, never
from the closed form, and the mutant's checks cover only $K \le K_{\rm tape}$.

The polynomials are fixed. $p_n$ is primary, and $p'_n$ is its reciprocal, used for the sibling.

| $n$ | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|
| $p_n$ | $z^3{+}z{+}1$ | $z^4{+}z{+}1$ | $z^5{+}z^2{+}1$ | $z^6{+}z{+}1$ | $z^7{+}z{+}1$ | $z^8{+}z^4{+}z^3{+}z^2{+}1$ |
| $p'_n$ | $z^3{+}z^2{+}1$ | $z^4{+}z^3{+}1$ | $z^5{+}z^3{+}1$ | $z^6{+}z^5{+}1$ | $z^7{+}z^6{+}1$ | $z^8{+}z^6{+}z^5{+}z^4{+}1$ |

**Initial law.** $\mu$ is uniform on $\mathcal{C}_V \times \mathcal{C}_H$. That is the maximal-entropy invariant measure, posit
(iv) of `Main.md:708`. `G_tape` instead uses the prior stated above, in the form of `Main.md:496`.

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
| $K$ | $0 \le K \le K_{\max}(n) = 4(2^n - 1)$, except where §3 sets a smaller cap for a class or knowledge level |
| $m$ (observer memory) | exhaustive: $m \le 2$; $m = 3$ passive, up to conjugacy (CI, $n \le 6$; extension to $n = 7, 8$ per the open decision in §10); linear-filter observers $m \le 4$, $n = 3,\dots,8$ (CI) |
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

Both K0 forms are reported. Over deterministic tests, the worst case is only a lower bound on the worst case over
randomized tests. The average case is unaffected, because a pure test attains it. The per-class K0 computation is
fixed in §3, and T3 uses the stronger forms that §6 names.

**Settings.** Passive classes have none. In the embedded class, the settings are the observer's interventions, as
follows:
- they are functions of its own memory, so they enter the record through its final state;
- the same policy defines $Q_p$;
- they are measurement-independent because the joint prior is the product of $\mu$ with a fixed prepared memory state
  (EX7).

**Reported horizons.** Each class, knowledge level, generator, $n$ and $m$ gets two horizons:
- $K_{\rm zero}$, the largest $K$ with $\mathrm{adv} = 0$ exactly at every $K' \le K$;
- $K_\delta$, the least $K$ with $\mathrm{adv} \ge \delta$. If no $K$ in the computed range reaches $\delta$, $K_\delta$ is
  `null`, reported with the scope $K \le K_{\rm cap}$ of the computation.

Together with the full exact curve, these answer "for how long".

**Record entropies.** The record law is reported as its exact count multiset, so $\max P$, and with it $H_\infty$, is
exact. $H$ is printed for display only and never enters a verdict.

## 3. Observer classes, all on the same generators

**U: unrestricted** (all Boolean tests on $X_{0:K}$). This is the calibration and countercontrol.
- K1 is the exact TV, computed from support counts, together with the exact K1 Bayes next-symbol predictor curve.
- K0 worst case over $\mathfrak{F}$ is reported as an interval. Its lower end is the exact value of the explicit test
  $D_\cup = 1[X_{0:K} \in \bigcup_{\varphi\in\mathfrak{F}} \mathrm{supp}\,P_\varphi]$. Its upper end is
  $\min_{\varphi \in \mathfrak{F}} \mathrm{TV}(P_\varphi, Q)$.
- K0 average case is reported as the interval
  $[\mathrm{TV}(\mathbb{E}_\nu P_\varphi, Q),\ \mathbb{E}_\nu \mathrm{TV}(P_\varphi, Q)]$.
- Each K0 value is exact only where the two ends of its interval coincide. Otherwise the interval is reported and
  bears on no verdict.

**B: computationally bounded, named structured classes.** No circuit-size class is used in PE-01.

| Class | Tests | Exact computation and limits |
|---|---|---|
| B1 linear | $D_T = \bigoplus_{t\in T} X_t$, $\emptyset \ne T \subseteq [0,K]$ | All $T$ via an integer Walsh–Hadamard transform for $K \le 23$. For larger $K$, only the bias-$\pm1$ tests are covered, via the $\mathbb{F}_2$ affine hull of the support. That is a lower bound in general, and exact for `G_lin`, `G_dec` and `G_tape`, whose biases are all $0$ or $\pm1$. K0: $\max_T \min_\varphi$ over the same range. Beyond $K = 23$, the tests are the $T$ in the intersection over $\varphi \in \mathfrak{F}$ of the annihilators of each support's direction space. That is a lower bound, exact for $\mathfrak{F}_{\rm lin}$. |
| B2 Berlekamp–Massey | $D_\lambda = 1[\mathrm{LC}(X_{0:K}) \le \lambda]$, $0 \le \lambda \le K+1$ | $\Pr_P$ by enumeration. $\Pr_Q$ by the closed-form count $N_N(0)=1$, $N_N(L) = 2^{\min(2L-1,\,2N-2L)}$ for $1 \le L \le N$, with $N = K+1$. $D_\lambda$ does not depend on $\varphi$, so K0 fixes $\lambda$ before $\varphi$, and K1 maximises over $\lambda$ per $\varphi$. |
| B3 $k$-wise / window | all tests on any $k \le 3$ positions ($K \le 127$); all tests on any window of $w \le 16$ consecutive positions | exact marginal TV, maximised over position sets. K0: $\max$ over (position set, test) of $\min_\varphi$, exact. |
| B4 low degree | $D_q = 1[q(X)=0]$ for $q \ne 0$ of degree $\le d$ vanishing on $\mathrm{supp}\,P_K$; $d=1,2$ for $K \le 255$, $d=3$ for $K \le 63$ | The least $K$ at which an annihilator exists, by exact $\mathbb{F}_2$ elimination (binary search, since existence is monotone in $K$). The certified bound is $\mathrm{adv} \ge 2^{-d}$ (Reed–Muller minimum distance). The exact maximum is computed over an annihilator space of dimension $\le 20$ only: for $d \le 2$ by Dickson rank, and for $d = 3$ only where $K+1 \le 24$, by enumeration. Otherwise the $2^{-d}$ bound is reported. K0: $q$ annihilates $\bigcup_\varphi \mathrm{supp}\,P_\varphi$. |

**Counting horizon for B4.** If $\sum_{i \le d} \binom{K+1}{i} > 2^{n+1}$, an annihilator of degree $\le d$ exists for
every generator, by counting alone. B4 results at or beyond this horizon are tagged COVERED-corpus (§6), because the
support bound implies them.

**𝒫ᵉᵐᵇ(m): physically restricted OI observers.** The visible sector is enlarged to
$\{0,1\}_{\rm sys} \times \{0,1\}^m_{\rm mem} \times \{0,1\}_{\rm out}$. Memory and output together take $m+1$ bits.

**Footprint.** The observer's footprint at horizon $K$ is $m + \lceil \log_2(K+1) \rceil + 1$ bits: memory, readout
clock and output. Every footprint-bearing statement uses this value:
- the admissibility condition (f) of §6;
- any bounded-resource claim;
- any statement of the form "for observers of footprint $\le f$".

The reported curves are indexed by $m$ and labelled "evaluation time uncharged".
- The fixed clock charge can overcharge an observer whose memory already keeps time.
- (f) is then stricter than necessary. That is conservative toward the claim under audit, and the verdict says so
  whenever it reports that no admissible witness was found.

An observer is $(\rho_0, \rho_1, a, F)$:
- $\rho_x \in \mathrm{Sym}(\{0,1\}^m)$;
- $a: \{0,1\}^m \to \{0,1\}$ (the passive subclass has $a \equiv 0$);
- $F \subseteq \{0,1\}^m \times \{0,1\}$;
- the prepared initial memory is $v_0 = 0^m$, and the output bit starts at $0$.

Each round $t < K$ applies three maps:
1. $v \leftarrow \rho_x(v)$;
2. $x \leftarrow x \oplus a(v)$;
3. $(x,h) \leftarrow \varphi(x,h)$.

At $K$: $\mathrm{out} \leftarrow \mathrm{out} \oplus 1[(v_K, x_K) \in F]$. This readout is a time-dependent operation:
- In the reported curves, the evaluation time $K$ is supplied by the analyst and is not charged.
- A verdict-bearing witness (§6) is realized with a clock register of $\lceil \log_2(K+1) \rceil$ bits. The clock
  starts at $0$, ticks as a cyclic permutation and triggers the readout. It is counted in the footprint, and EX1, EX8, IM3 and FP run
  on the clocked composite.

Every map is a bijection of $\mathcal{C}_V' \times \mathcal{C}_H$, and the observer's maps act as the identity on
$\mathcal{C}_H$. There is no hidden-sector access (`Computation.md:15`).
- **Time-invariance.** The observer's rule is time-invariant because it is part of one fixed dynamics (`Main.md:560`).
  That anchor is cited for time-invariance only.
- **Tables.** The modelling choice is that the tables $(\rho_0, \rho_1, a, F)$ belong to the composite dynamics
  $\varphi'$, not to its state. `Main.md:560` charges a program register as state, so every witness also records its
  table size next to its footprint. The table size is $2m \cdot 2^m + 2^m + 2^{m+1} + \lceil \log_2(K+1) \rceil$ bits,
  the last term being the clock's trigger constant.
- **Clock.** A time-dependent rule is realized by a time-invariant one with a clock in memory, and the footprint counts
  that clock.
- **Prediction tests.** $v_K$ depends on $X_{0:K-1}$ only. The prediction subclass is therefore $F$ equal to the graph of
  some $\chi(v)$.

The enumerated subclasses are:
- all observers with $m \le 2$: 16 at $m=1$ and 9216 at $m=2$, each with every $F$;
- passive observers with $m = 3$, up to simultaneous conjugacy fixing $v_0$;
- linear-filter observers $\rho_x(v) = Av \oplus xb$, with $A \in \mathrm{GL}(m,2)$, $m \le 4$ and $n = 3,\dots,8$.

K0 for each subclass:
- **$m \le 2$.** The test is $(\rho, a, F)$, over all 256 sets $F$, for $K \le 255$.
  - The deterministic worst case is reported, as a lower bound.
  - The average case is exact.
  - The randomized worst case is exact for $|\mathfrak{F}| \le 6$ ($n \le 6$) and $K \le K_{\rm LP}(n) = 2^{n-1} - 1$.
    - There is one exact rational LP per sign pattern $s$ on $\mathfrak{F}$, modulo a global flip, over the
      complement-closed test class.
    - Each LP is solved in its dual form, with one variable per $\varphi \in \mathfrak{F}$:
      $\min_{\pi \in \Delta(\mathfrak{F})} \max_{(\rho,a)} \sum_{(v,x)} \bigl(\sum_\varphi \pi_\varphi s_\varphi \Delta_\varphi(v,x)\bigr)_+$.
      For each observer, the inner maximum over $F$ is the sum of positive parts.
    - The all-positive pattern is reported separately, as the value for an observer that fixes its decision orientation
      in advance.
- **Passive $m = 3$.** K1 with the optimal $F$. K0 only over prediction tests, every $\chi$.
- **Linear-filter $m \le 4$.** K1 with the optimal $F$. K0 only over linear prediction tests $\chi(v) = c \cdot v \oplus e$.

Named larger observers are admissible only as explicit tables, verified by EX1, EX8, IM3 and FP. By definition, the passive
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
  - The mutant `G_tape(K)` removes the support deficit. It must give $\mathrm{adv} = 0$ at every $K \le K_{\rm tape}$
    for U and B1–B4, and at every $K \le 12$ for 𝒫ᵉᵐᵇ($m \le 2$), active observers included. The cap of 12 is set by
    enumeration cost.
- **NC-2 (linear complexity, B2 at $\lambda = n+1$).**
  - The reason is that $\mathrm{LC}(X_{0:K}) \le n+1$ surely, because the minimal polynomial divides $(1+z)p(z)$.
  - On both siblings, the advantage must equal $1 - \Pr_Q[\mathrm{LC} \le n+1]$.
  - The mutant `G_tape(K)` must give $0$ at every $K \le K_{\rm tape}$.
  - Specificity: `G_filt` keeps the support reason and removes the linear-complexity reason. At every $K$ where the
    records of both `G_filt` and `G_lin` are injective, U's NC-1 value on `G_filt` must equal that on `G_lin`.
    - B2 at $\lambda = n+1$ must be $\le$ on `G_filt` at every such $K$, and strictly smaller at some such $K$, for each
      $n$.
    - The converse separation is impossible: $\mathrm{LC} \le n+1$ bounds the support.
- **Exactness and implementation.** EX1–EX8 and IM1–IM6 in §5.
- **Symmetry (§A.21).** `G_lin`, `G_filt`, `G_dec` and `G_tape` commute with the global flip $x \mapsto x \oplus 1$, and $\mu$
  is flip-invariant. Their record laws, and $Q$, must therefore be complement-invariant exactly. `G_clk` does not
  commute with the flip and is exempt.

## 5. Invariant → checkpoint (§A.41)

Every numerical row is computed in exact integer or `Fraction` arithmetic. Failing any row makes the stage VOID (§6).

| Invariant | Checkpoint | Measured by |
|---|---|---|
| Every $\varphi$, mutant and observer composite is a bijection | EX1 | image cardinality equals the domain size. All generators are checked at every $n$, and `G_tape(N)` at every $N \le K_{\rm tape}$. Composites are checked exhaustively at $n \le 4$, and for every verdict-bearing witness. |
| $\mu$, every $P$ and every $Q$ sum to 1 | EX2 | exact sum |
| No float on the verdict path | EX3 | a type assertion on every verdict input |
| $p_n$ and $p'_n$ are primitive | EX4 | order of $z$ is $2^n-1$ |
| $(\ell, L_p)$ is observable | EX5 | $\mathbb{F}_2$ rank $n$ |
| T-level (C1) holds for the primary generators and fails for `G_dec` | EX6 | exact one-step visible matrix |
| The observer has no hidden-sector access, and the generator does not touch the observer | EX8 | Each observer map is checked as a table on $\mathcal{C}_V' \times \mathcal{C}_H$: the $\rho$-step, the $a$-step, the clock tick and the readout. For each, the $h$-component is the identity, and the $(v, \mathrm{clk}, x, \mathrm{out})$-component is constant across $h$. The generator step $\varphi$ must act as the identity on $(v, \mathrm{clk}, \mathrm{out})$. Checked exhaustively at $n \le 4$ and for every verdict-bearing witness. |
| Settings are measurement-independent | EX7 | EX8 holds, and the joint prior factorises as $\mu \otimes \delta_{v_0}$ |
| BM is correct | IM1 | agrees with brute-force minimal-LFSR search on all sequences of length $\le 12$ |
| The LC count formula holds | IM2 | Equals enumeration of $\{0,1\}^N$ for $N \le 20$. Equals, for every $N$ used, an independent exact DP on the Berlekamp–Massey length process under fair bits; that process's Markov premise is itself checked by enumeration for $N \le 20$. |
| The embedded simulation is correct | IM3 | the aggregated transfer computation and a full-state simulation of the composite bijection agree for all observers at $n \le 4$ and for every verdict-bearing witness |
| WHT biases are correct | IM4 | equal to direct bias computation for $K \le 10$ |
| The annihilator search is correct | IM5 | equal to brute-force polynomial search for $K \le 5$, $d \le 2$, and for $K \le 3$, $d = 3$ |
| The $Q_p$ computation is correct | IM6 | `G_tape(K)` gives $P_p = Q_p$ exactly for every enumerated observer, active included, at $K \le 12$. This is the only check of the $Q$ side independent of the plan's own $Q$ code. |
| PC zero and PC firing | PC | §4 |
| NC-1 and NC-2, with their mutant, sibling and `G_filt` specificity | NC | §4 |
| Complement symmetry | SY | §4 |
| Inclusions | MO | Each passive class is at most U. K0 worst case is at most $\min_\varphi$ K1; K0 average is at most $\mathbb{E}_\nu$ K1. 𝒫ᵉᵐᵇ(m) is at most 𝒫ᵉᵐᵇ(m+1). Passive is at most active. B4 at $d=1$ exists iff B1 has a bias-$\pm1$ test. All are checked pointwise. |
| The footprint is measured | FP | For every witness, the printed footprint equals the total bit width of the visible registers of its clocked composite (the one checked by EX1, EX8 and IM3), less the system bit. It is computed from the composite and compared with the formula of §3. |
| The counterexample conditions are evaluated mechanically | CX | For every candidate witness, the JSON records: the exact $\mathrm{adv}^{\rm pred}_O(\varphi, K')$ at each $K' \in [K-3, K]$, from full-state simulation of the clocked composite (the IM3 path); $K_{\rm cx}(\varphi)$; the FP footprint; EX6; the per-witness EX1, EX7, EX8 and IM3 flags; and the global control flag. The checker evaluates (a)–(f) of §6 from those fields alone. A COUNTEREXAMPLE is printed only if all hold. Self-test: three mutant witnesses must each be refused, and reported as a measurement, on their own condition: one $K'$ in the window at $1/8 - 2^{-K-2}$; footprint $\theta + 1$; and $K = K_{\rm cx} + 1$. A refusal counts only if it names that condition. |
| The K0 test is chosen before $\varphi$ | K0 | each K0 record names one test id, evaluated across all of $\mathfrak{F}$ |
| Deterministic replay (§A.26) | RP | a rerun's measurement JSON is byte-identical |
| The plan precedes the code | PIN | the measurement JSON records this file's blob id, and this commit is an ancestor of every code commit |
| Verdicts are generated from measurements | VG | The verdict is regenerated from the JSON and compared. Self-test: a copy with any control flag flipped must yield VOID. A verdict text lacking the resource-model limitation sentence of §7 must fail. |
| The admissible region is derived, not reprinted | AR | Z(φ) (§7) is computed by exhaustive equidistribution over all control sequences, at every $n$ and for all three primary generators. Z(`G_lin`) $= n$ is cross-checked against PC. The assumptions of the zero argument are checked: $\mu$ factorises with $h$ uniform and independent of $x_0$, and every observer register (memory, clock, output) starts at a fixed value. The region is recomputed from Z(φ), $K_{\rm cx}(\varphi)$ and $\theta$, and must equal the §7 tables cell for cell. The verdict prints the recomputed region. |
| Runs wait for the fixed thresholds | TH | The measurement JSON records $\theta$, $K_{\rm LP}$, the $m = 3$ scope decision (§10) and the blob id of the amendment that fixes them. That amendment's commit must be an ancestor of every run commit, checked as PIN is. A run without that record refuses to start. |

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
   - (b) $O \in$ 𝒫ᵉᵐᵇ(m) is given as explicit tables, with its readout clock (§3), and passes EX1, EX7, EX8 and IM3;
   - (c) $K \le K_{\rm cx}(\varphi) = \lfloor \ell_{\rm med}(\varphi)/2 \rfloor$, where $\ell_{\rm med}$ is the
     $\mu$-median orbit length of $\varphi$, i.e. below recurrence scale;
   - (d) the same $O$ and $\chi$ give $\mathrm{adv}^{\rm pred}_O(\varphi, K') \ge \delta_{\rm cx} = 1/8$, exactly,
     at every $K' \in [K - w, K]$, with $w = 3$ fixed and $K \ge w$;
   - (e) every control is green;
   - (f) the footprint (FP) is at most $\theta$.

   A **bounded-resource claim** is a COUNTEREXAMPLE meeting (a)–(f). $\theta$ and the $m = 3$ scope are the open owner
   decisions (§10); $K_{\rm LP}$ awaits confirmation. No run starts before $\theta$, $K_{\rm LP}$ and the $m = 3$ scope
   are fixed by amendment (TH). Witnesses meeting (a)–(e) but not (f) are reported for comparison as
   unrestricted-footprint witnesses. They are not COUNTEREXAMPLEs.

   Knowledge level: $O$ may depend on $\varphi$, so the witness is K1. The verdict also reports its K0 status, that is,
   whether the same $O$ is a witness for every $\varphi$ in its family $\mathfrak{F}$.

   The verdict prints:
   - the footprint $m + \lceil \log_2(K+1) \rceil + 1$ (memory, clock, output), as measured by FP;
   - the table size;
   - the admissibility result (f). Condition (f) implements the embedded-memory condition of `../README.md:155–159`;
   - the resource-model limitation sentence of §7, and the admissible region for the chosen $\theta$, recomputed (AR)
     from the measured Z(φ) and $K_{\rm cx}(\varphi)$;
   - the realization conditions the witness satisfies, in the form "T-level (C1) holds; C2–C4 not checked". The
     refuted statement is therefore exactly the one tested.

   Exclusions:
   - A witness that fails only (c) is reported as a recurrence-scale measurement, not as a COUNTEREXAMPLE. At that scale
     the record's entropy is exhausted (`Structure.md:1256`), and $K_{\rm cx}$ is this plan's stated bound.
   - Distinguishing witnesses, as opposed to prediction witnesses, are reported as measurements and are not
     COUNTEREXAMPLEs. They are labelled as bearing on the second clause of `ch18-beyond.md:114` ("the cryptographic
     properties depend on unpredictability"). For 𝒫ᵉᵐᵇ, Yao's reduction from distinguishing to prediction does not stay
     inside the class.
   - No finite result here establishes the universal form (`../README.md`, Question).

   **Attribution.** The rule is applied separately for each (generator, $n$, observer subclass); it is never pooled
   across them.
   - Within a combination, unpredictability is attributed to resources if and only if some witness in that combination
     meets (a)–(e) but fails (f). That case is reported as a limitation of the resource model.
   - In every other combination without a COUNTEREXAMPLE, the verdict states "no witness within the enumerated scope at
     any footprint". It never states that the record is unpredictable because of the observations available on the
     strength of a finite enumeration.
5. **Productivity tag (§A.31).** Each result also gets one tag:
   - **COVERED-corpus:** class U, anything implied by the support bound or by PC, and B4 at or beyond its counting
     horizon (§3);
   - **COVERED-literature:** a B-class horizon equal to one of the closed forms fixed now:
     - B1 K1 fires on `G_lin` at $K = n+1$;
     - Berlekamp–Massey determines a sequence from $2\,\mathrm{LC}$ symbols;
     - the B4 counting bound;
     - the NC-1 value.

     The only other admissible citation is a result listed in §9 under "before any candidate-NEW tag" that covers the
     candidate. The tag then cites that result.
   - **candidate-NEW:** 𝒫ᵉᵐᵇ results not implied by MO together with a covered result, and K0–K1 gaps.
     - A worst-case gap qualifies only in the average-case form or the exact randomized form (§3), never in the
       deterministic lower bound.
     - The tag is assigned only after the literature marked "before any candidate-NEW tag" in §9 has been checked
       against the result.
     - These stay candidates until independent review.

   Favorable readings get the hardest scrutiny. These are $K_{\rm zero} = K_{\max}$ for an embedded class, or no
   witness found.
   - For each, the verdict states the enumerated scope it rests on, and it does not extend that reading beyond the
     enumeration.
   - Where the admissible region of §7 is empty, or narrower than the measured range, "no admissible witness" is
     reported as a fact about the resource model, not as a measurement.
6. **Bounded-theorem targets.** These are questions, not expectations:
   - **T1.** An exact characterisation of $\mathrm{adv}^{\rm pred}$ for $\mathfrak{F}_{\rm lin}(n)$ against linear-filter
     observers, as a function of $(n, m, K)$.
   - **T2.** Whether active 𝒫ᵉᵐᵇ(m) reduces to passive 𝒫ᵉᵐᵇ(m′) for autonomous-hidden generators, and for which $m'$.
     `G_clk` is the case outside that hypothesis.
   - **T3.** The K0–K1 gap of B and 𝒫ᵉᵐᵇ on $\mathfrak{F}_{\rm lin}(n)$, in the average-case form or the exact
     randomized form.
7. **Stage outcome.** The outcome is one or more of: a bounded theorem over a named class; a COUNTEREXAMPLE; a COVERED
   finding, with its covering statement cited. If none is reached, it is OPEN. VOID takes precedence over all of them.
   The thread's first milestone closes only after PE-02 (`../README.md:265`).

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
- **Resource-model limitation.** The horizon bound $K < 2^{\,n-m-1}$ ($\theta = n$), or $K < 2^{\,n-m}$ ($\theta = n+1$),
  is a consequence of the selected resource model: memory + clock + output $\le \theta$. It is not a limit OI imposes on
  observers. The generated verdict text repeats this sentence.
  - **Universal zero horizon.** Let Z(φ) be the largest $k$ such that, for every control sequence $c_0, \dots, c_{k-1}$,
    the increments $f(\sigma_{c_0} h), f(\sigma_{c_1}\sigma_{c_0} h), \dots$ (the first $k$) are jointly uniform under
    uniform $h$.
  - **The zero holds for every observer.** For every 𝒫ᵉᵐᵇ observer, passive or adaptive, $\mathrm{adv}^{\rm pred} = 0$
    exactly at every $K' \le$ Z(φ):
    - The control at round $t$ is $c_t = x_t \oplus a(v_{t+1})$. Given $x_0$, it is a function of the earlier increments
      only.
    - So $\Pr[Y_{0:k-1} = z \mid x_0]$ equals the probability, for the fixed sequence $c(z)$, that the increments equal
      $z$. That is $2^{-k}$.
    - $x_{K'} = c_{K'-1} \oplus Y_{K'-1}$, and the guess $\chi(v_{K'})$ is a function of $X_{0:K'-1}$. The guess is
      therefore correct with probability exactly $1/2$.
    - $K' = 0$ is zero trivially.
    - The argument uses the product prior, under which $x_0$ is independent of $h$.
  - **Window floor.** Condition (d) therefore needs $K \ge$ Z(φ) $+ 4$ for every generator. Together with the clock bound
    and $K \le K_{\rm cx}(\varphi)$, that gives the region below.
  - **Drafting-time values.** The Z values at drafting are:

    | | $n=3$ | 4 | 5 | 6 | 7 | 8 |
    |---|---|---|---|---|---|---|
    | Z(`G_lin`) | 3 | 4 | 5 | 6 | 7 | 8 |
    | Z(`G_filt`) | 2 | 2 | 3 | 4 | 5 | 6 |
    | Z(`G_clk`) | 2 | 3 | 3 | 4 | 4 | 5 |

    Z(`G_lin`) $= n$ is the PC floor. These values and the tables below are drafting-time values, not results. AR
    re-derives them, and any difference halts the stage.
  - **Reading a cell.** A cell outside the region is structurally excluded. A cell inside it is not a claim that a
    witness exists.

  Each cell gives `G_lin` | `G_filt` | `G_clk`; – means empty.

  $\theta = n$:

  | $n$ | $m=1$ | $m=2$ | $m=3$ | $m=4$ |
  |---|---|---|---|---|
  | 3 | – \| – \| – | – \| – \| – | – \| – \| – | – \| – \| – |
  | 4 | – \| – \| – | – \| – \| – | – \| – \| – | – \| – \| – |
  | 5 | – \| [7,7] \| [7,7] | – \| – \| – | – \| – \| – | – \| – \| – |
  | 6 | [10,15] \| [8,15] \| [8,15] | – \| – \| – | – \| – \| – | – \| – \| – |
  | 7 | [11,31] \| [9,31] \| [8,31] | [11,15] \| [9,15] \| [8,15] | – \| – \| – | – \| – \| – |
  | 8 | [12,63] \| [10,63] \| [9,63] | [12,31] \| [10,31] \| [9,31] | [12,15] \| [10,15] \| [9,15] | – \| – \| – |

  $\theta = n+1$:

  | $n$ | $m=1$ | $m=2$ | $m=3$ | $m=4$ |
  |---|---|---|---|---|
  | 3 | – \| – \| – | – \| – \| – | – \| – \| – | – \| – \| – |
  | 4 | – \| [6,7] \| [7,7] | – \| – \| – | – \| – \| – | – \| – \| – |
  | 5 | [9,15] \| [7,15] \| [7,15] | – \| [7,7] \| [7,7] | – \| – \| – | – \| – \| – |
  | 6 | [10,31] \| [8,31] \| [8,31] | [10,15] \| [8,15] \| [8,15] | – \| – \| – | – \| – \| – |
  | 7 | [11,63] \| [9,63] \| [8,63] | [11,31] \| [9,31] \| [8,31] | [11,15] \| [9,15] \| [8,15] | – \| – \| – |
  | 8 | [12,127] \| [10,127] \| [9,127] | [12,63] \| [10,63] \| [9,63] | [12,31] \| [10,31] \| [9,31] | [12,15] \| [10,15] \| [9,15] |

  Consequences:
  - **At $\theta = n$:**
    - the region is empty for $n \le 4$;
    - at $n = 5$ only $m = 1$, $K = 7$ survives, on `G_filt` and `G_clk`;
    - $m = 3$ is non-empty only at $n = 8$;
    - every $m = 4$ cell is empty.
  - **At $\theta = n+1$:**
    - $m = 3$ is non-empty only from $n = 7$;
    - $m = 4$ is non-empty only at $n = 8$.
  - **The two sweeps.** The passive $m = 3$ sweep ($n \le 6$) can yield no admissible witness at either $\theta$. The
    linear-filter $m = 4$ sweep can do so only at $n = 8$ with $\theta = n+1$.

## 8. Resources and CI (§A.40)

Seeds number $2^{n+1} \le 512$. Generator laws, U, B2 and B3 cost seconds per generator. The cost is dominated by the
𝒫ᵉᵐᵇ sweeps and the B1 WHT.

| Work | Estimate | Where |
|---|---|---|
| EX/IM/PC/NC/SY controls; U, B1–B4 and 𝒫ᵉᵐᵇ($m \le 2$, passive) for $n \le 5$ | under 10 min | local smoke |
| B1 WHT for $K \le 23$, all generators, $n \le 8$ | about 10 min | CI |
| 𝒫ᵉᵐᵇ($m=2$, active) for $n = 6, 7, 8$: K1 with the optimal $F$; K0 per §3 | 0.5–2 h in total, vectorised over seeds and observers. About $6 \times 10^{10}$ elementary updates at $n = 8$. Dominated by exact big-integer comparison against $Q$, which is computed once per observer and reused across $\varphi$. | CI, sharded by $(n, \text{family})$ |
| 𝒫ᵉᵐᵇ($m=3$, passive, canonical form by BFS labelling of the component reachable from $v_0$); linear-filter observers with $m \le 4$ | 1–3 h in total | CI, sharded |
| Only under option (ii) of §10: 𝒫ᵉᵐᵇ($m=3$, passive) at $n = 7, 8$, with K capped at the top of the admissible region ($K \le 15$ at $n = 8$ for $\theta = n$; $K \le 15$ at $n = 7$ and $K \le 31$ at $n = 8$ for $\theta = n+1$) | about 1–2 h | CI, sharded by $n$ |
| `G_tape` checks: U and B1–B4 to $K = 20$; 𝒫ᵉᵐᵇ to $K = 12$ | minutes | CI |
| B4 with $d = 3$ | minutes | CI |
| Randomized K0, dual LP: $m \le 2$, $n \le 6$, $K \le K_{\rm LP}(n)$, at most 32 sign patterns | under 1 h | CI |

The estimates are not measurements. A local run that exceeds its row by a factor of 3 is stopped and moved to CI.
The CI job definition is part of the code commits.
- The job is `workflow_dispatch`-only, so no push launches it.
- Dispatching it needs owner approval (§A.43, item 4).
- Shard outputs are committed as structured JSON that records the commit, the recipe and the run id (§A.42, item 1).
  They are never relied on as logs.

Exact arithmetic uses Python integers and `Fraction`; numpy is used only on integer arrays.

## 9. Literature dependence (cited, not rederived)

The verdict path uses three cited results:
- **Massey 1969 (Berlekamp–Massey).** B2's test, cross-checked by IM1.
- **Gustavson 1976 and Rueppel 1986: the number of length-$N$ binary sequences of linear complexity $L$.**
  F. G. Gustavson, *IBM J. Res. Dev.* 20(3), 1976; R. A. Rueppel, *Analysis and Design of Stream Ciphers*, Springer
  1986. Used for $\Pr_Q$ in B2 and NC-2. It is checked by enumeration for $N \le 20$, and by the independent DP for
  every $N$ used (IM2).
- **Reed–Muller minimum distance (MacWilliams–Sloane).** The B4 lower bound.

Other results enter only as design rationale:
- Golomb, *Shift Register Sequences*: m-sequence window and balance properties. Every one that is used is re-verified
  exactly (EX4, EX5, PC).
- Key 1976: linear complexity of filter generators.
- D. Gollmann, W. G. Chambers, "Clock-controlled shift registers: a review", IEEE JSAC 7(4):525–533 (1989): the
  `G_clk` rationale.
- Fine–Wilf: the K1 calibration horizon (`../README.md`).

Other papers are cited for framing only:
- HILL 1999, BSW 2003 and RTTV 2008, for the class-$\mathcal{Q}$ forms (deferred).
- Yao 1982, for prediction against distinguishing. Prediction tests are used directly, so no reduction is relied on.

Each is read in full before any closure claim relies on it (`../README.md`).

To read before any candidate-NEW tag. Passive 𝒫ᵉᵐᵇ(m) are width-$2^m$ oblivious read-once permutation branching
programs, and these results bear on them directly:
- O. Reingold, T. Steinke, S. Vadhan, "Pseudorandomness for regular branching programs via Fourier analysis",
  RANDOM 2013, LNCS 8096, pp. 655–670, arXiv:1306.3004.
- N. Alon, O. Goldreich, J. Håstad, R. Peralta, "Simple constructions of almost k-wise independent random variables",
  Random Struct. Algorithms 3(3) (1992). Its LFSR small-bias construction is close to the K0 average over
  $\mathfrak{F}_{\rm lin}$. The construction's exact distribution on feedback polynomials is to be verified before use.
- Bogdanov–Dvir–Verbin–Yehudayoff 2013: small-bias results for width-2 branching programs.

## 10. Owner decisions

The owner has decided the following, and they replace the earlier defaults:

1. **Footprint.** Footprint is an admissibility condition for the bounded-resource claim: condition (f), footprint
   $\le \theta$ (§6). Results without the restriction are also reported, for comparison.
2. **Clock and window.** The clock charge of $\lceil \log_2(K+1) \rceil$ bits and the fixed four-step window
   $[K-3, K]$ are approved.
3. **Knowledge level.** K1 observers are allowed. Whether one observer works across the whole family (K0) is reported
   separately.
4. **Thresholds.** Prediction advantage $\ge \delta_{\rm cx} = 1/8$ stays as preregistered. All other thresholds are
   fixed before any run. The fixed values are: $\delta \in \{1/8, 1/4\}$, $w = 3$, $K_{\rm cx}$, $K_{\max}$,
   $K_{\rm tape} = 20$, the 𝒫ᵉᵐᵇ tape cap of 12, the $K \le 255$ K0 cap, the B4 limits and the IM ranges. Two values
   remain:
   - $\theta$, which is open;
   - $K_{\rm LP}(n) = 2^{n-1} - 1$, proposed by this plan and awaiting owner confirmation.
5. **Reference.** The reference $Q$ stays fixed throughout PE-01. Alternative reference classes go to PE-02.
6. **Prediction and distinguishing.** Both are recorded. A distinguishing-only witness is not treated as proof of
   predictability.
7. **Gap claims.** Average-case or exact randomized evaluation is required for any claimed new gap. Deterministic
   worst-case results are reported as bounds only.

**Open owner decision: the value of $\theta$.** The candidates are $\theta = n$, the hidden register, and
$\theta = n+1 = \log_2|\mathcal{C}_V \times \mathcal{C}_H|$, the whole generator. The consequences are in the §7
tables:
- **At $\theta = n$:**
  - the region is empty for $n \le 4$ on every generator;
  - at $n = 5$ it is only $m = 1$, $K = 7$, on `G_filt` and `G_clk`;
  - every $m = 4$ cell is empty;
  - $m = 3$ is non-empty only at $n = 8$.
- **At $\theta = n+1$:** the region is wider, with $m = 3$ from $n = 7$ and $m = 4$ at $n = 8$.
- **The two sweeps.** The passive $m = 3$ sweep ($n \le 6$) is not admissible under either value.

**Open owner decision: the scope of the passive $m = 3$ sweep.** There are two options:
- **(i)** Keep $m = 3$ at $n \le 6$, as comparison data only. Under either $\theta$, no admissible region exists there.
- **(ii)** Extend it to $n = 7, 8$, with $K$ capped at the top of the admissible region:
  - for $\theta = n$: $K \le 15$ at $n = 8$;
  - for $\theta = n+1$: $K \le 15$ at $n = 7$ and $K \le 31$ at $n = 8$.

  Option (ii) has its own §8 row.

The independent review notes that (ii) is the only way an $m = 3$ observer can bear on condition (f). This plan does
not make that decision.

No PE-01 run starts before $\theta$, $K_{\rm LP}$ and the $m = 3$ scope are fixed in an amendment to this plan (TH).

## 11. Package

This directory will hold:
- `PLAN.md`, this commit, alone;
- the code;
- `results/measurements.json` and `results/verdict.json`;
- `REPORT.md`;
- `review/`, holding an independent review.

Any amendment to this plan goes in `amendments/` before the code it governs.
