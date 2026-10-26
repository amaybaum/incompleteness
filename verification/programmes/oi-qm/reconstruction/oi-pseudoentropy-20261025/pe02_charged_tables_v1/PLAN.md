# PE-02 stage plan: charged observer tables, activity and backaction (v1, draft)

**Status: WIP / UNREVIEWED; planning only; no execution authorized.**

Stage plan for Issue #934 in thread OI-PE-1 (`../README.md`). No PE-02 code exists. Drafted on
`research/oi-pseudoentropy-20261025` at `efbfd0d7bae21de298874733df763f25c3727c18`. The corpus sentence it bears on is
read on `main` at `c967d6a931c294e456053be5e3bf5bb4f2d9ad1c`. The drafter's sources, readings of #934 and the open owner
decisions are in `NOTES.md`.

PE-01 (`../pe01_bounded_tests_v1/`) is an immutable reference. Its plan, amendments A1–A3, results, verdict and
reviews are read, never edited. PE-02 neither re-runs PE-01 as a study nor optimizes it. It reads PE-01's retained
measurements, replays one PE-01 shard byte for byte as a control (§5, RP-01), and recomputes PE-01 cells only where the
secondary question needs the full witness population (§4.3), with a cross-check against PE-01's recorded counts (UX).

## 0. Question

PE-01 returned COUNTEREXAMPLE at one admissible cell: `G_clk`, n = 5, `emb_m2_all`, K = 7, footprint 6 = θ = n + 1.
The observer's 31 table bits were held in the dynamics and not charged.

**Main question.** Does an admissible prediction witness of PE-01's kind exist when the observer's description, its
transition, action and readout tables or a fixed encoding of them, is charged against the footprint threshold?

**Secondary question.** Is the advantage tied to the clock responding to the observer's interventions? It is answered
by three comparisons on the same tables:
- the active observer on `G_clk`;
- the same tables with interventions disabled (§3.2);
- the same tables on a `G_clk` variant whose clock ignores the observer's input (§1.2).

**The factors.** Activity (active, passive), accounting (uncharged, charged), and generator (with visible-to-hidden
backaction, autonomous). §6 fixes, before any computation, which outcome each factor combination receives.

## 1. Objects

### 1.1 Generators carried over from PE-01

The template, `G_lin`, `G_filt`, `G_clk`, the Fibonacci companion map $L_p$, $\ell(h) = h_0$,
$g(h) = h_0 \oplus h_1 h_2$, the initial law $\mu$ uniform on $\mathcal{C}_V \times \mathcal{C}_H$, the record $X_{0:K}$
and the increments $Y_t$ are exactly those of PE-01 `PLAN.md` §1.

**Polynomials beyond n = 8.** PE-02 extends $n$ for the charged sweep (§3.4). The rule is fixed now:
$p_n$ is the least primitive polynomial of degree $n$ by integer value, in PE-01's convention
$p(z) = z^n + \sum_i c_i z^i$ with new bit $\sum_i c_i h_i$; $p'_n$ is its reciprocal.
- The rule reproduces PE-01's $p_n$ and $p'_n$ for $n = 3,\dots,8$ (design check, `NOTES.md` §4).
- Drafting-time values, re-derived by EX4 at run time (any difference halts the stage):

| $n$ | $p_n$ | $n$ | $p_n$ |
|---|---|---|---|
| 9 | $z^9{+}z^4{+}1$ | 17 | $z^{17}{+}z^3{+}1$ |
| 10 | $z^{10}{+}z^3{+}1$ | 18 | $z^{18}{+}z^5{+}z^2{+}z{+}1$ |
| 11 | $z^{11}{+}z^2{+}1$ | 19 | $z^{19}{+}z^5{+}z^2{+}z{+}1$ |
| 12 | $z^{12}{+}z^6{+}z^4{+}z{+}1$ | 20 | $z^{20}{+}z^3{+}1$ |
| 13 | $z^{13}{+}z^4{+}z^3{+}z{+}1$ | 21 | $z^{21}{+}z^2{+}1$ |
| 14 | $z^{14}{+}z^5{+}z^3{+}z{+}1$ | 22 | $z^{22}{+}z{+}1$ |
| 15 | $z^{15}{+}z{+}1$ | 23 | $z^{23}{+}z^5{+}1$ |
| 16 | $z^{16}{+}z^5{+}z^3{+}z^2{+}1$ | 24 | $z^{24}{+}z^4{+}z^3{+}z{+}1$ |

The rule favours sparse feedback, which is the case most exposed to clock-control prediction. It is kept because it is
PE-01's rule, not chosen for its effect; no other polynomial is substituted after any result.

### 1.2 The clock-ablated generator `G_clkfix(p)`

`G_clk` selects its hidden step by the visible bit after intervention, so an intervention changes the hidden
trajectory. The ablation needs a clock that is the generator's own running parity and that no intervention reaches.
No variant of `G_clk` on $\{0,1\} \times \mathbb{F}_2^n$ does this: the pre-intervention visible bit already carries
every earlier intervention. One hidden bit $q$ is therefore added.

- $\mathcal{C}_H = \mathbb{F}_2^n \times \{0,1\}$, state $(x, h, q)$.
- $\varphi^{\rm fix}(x,h,q) = (x \oplus \ell(h'),\ h',\ q \oplus \ell(h'))$ with $h' = \sigma_q(h)$, $\sigma_0 = L_p$,
  $\sigma_1 = L_p^2$. It is a bijection: $\ell(h')$ is read from the image, which gives $q$, $x$ and
  $h = \sigma_q^{-1}(h')$ (checked as EX1).
- **Prior (matched, primary).** $\mu^{\rm fix}$ is uniform on $\{(x,h,q) : q = x\}$. Without an observer, $x_t = q_t$ at
  every $t$, and the visible record is pathwise identical to that of `G_clk(p)` from $(x_0, h_0)$. Checked as CA-EQ.
- **Prior (uniform, reported variant; owner decision O5).** `G_clkfix_u(p)`: the same map with $\mu$ uniform on the
  whole state space. The clock phase $q_0$ is then hidden from the observer, which changes the passive record law; it is
  reported as its own generator and never pooled with the matched form.
- Within the composite, the observer's action changes $x$ only; the hidden pair $(h, q)$ evolves autonomously.
- **θ for this generator** is that of `G_clk(p)` at the same $n$, $n + 1$ (§2.3), so that the ablation changes only
  the clock's responsiveness.

### 1.3 Control generators

- **`G_weak(n)` (planted passive witness).** The template with $\sigma_0 = \sigma_1 = L_{p_n}$ and
  $f(h) = \prod_{i<n} h_i$ (the all-ones indicator), prior $x_0 = 0$ and $h$ uniform on $\mathbb{F}_2^n$.
  - $L_{p_n}$ cycles the $2^n - 1$ nonzero states, so for $1 \le K \le 2^n - 1$:
    $\Pr[X_K = 1] = K/2^n$ exactly.
  - The memoryless passive observer ($m = 0$, $a = 0$, $\chi \equiv 0$) therefore has
    $\Pr[\chi = X_K] - 1/2 = 1/2 - K/2^n$, which is $\ge 1/8$ for $K \le 3 \cdot 2^{n-3}$.
  - $Z(\text{`G\_weak`}) = 0$, because $Y_0$ is not uniform.
  - Used at $n_{\rm ctl} = 13$, where the planted observer is admissible under all three accounting models (§2) with
    window $[4,7]$. It is a control, never a candidate under (a′).
- **`G_weak_mut(n)` (countercontrol).** As `G_weak` with $f = \ell$. By the zero argument of PE-01 §7, every
  observer's prediction advantage is exactly 0 at every $K \le n$.
- PE-01's `G_dec`, `G_tape(N)` and `G_lin(p'_n)` are reused, for the controls PE-01 used them for (§5).

## 2. Accounting models

### 2.1 What is charged

For an observer $O = (m, \rho_0, \rho_1, a, F)$ with readout trigger $K$ and $c(K) = \lceil \log_2(K+1) \rceil$:

- **U (uncharged; PE-01).** $F_U(O,K) = m + c(K) + 1$ bits: memory, clock and output. The tables are part of the
  composite dynamics.
- **R (raw tables).** $T_R(O,K) = 2m\,2^m + 2^m + 2^{m+1} + c(K)$, the table size PE-01 prints, and
  $F_R = F_U + T_R$.
  - Serialization $S_R$, which fixes the bit count measured by TR (§5): $\rho_0(v)$ then $\rho_1(v)$ as $m$-bit
    big-endian entries for $v = 0,\dots,2^m-1$; $a(v)$ for $v = 0,\dots,2^m - 1$; the indicator of $F$ over $(v,x)$ in
    order $v$ major, $x$ minor; then $K$ in $c(K)$ bits.
  - R charges the full readout set $F$ ($2^{m+1}$ bits) because PE-01's recorded `table_size_bits` does, which lets
    CH-IFF compare against PE-01's recorded values.
- **E (fixed universal encoding).** $T_E(O,K) = |E(O,K)|$ and $F_E = F_U + T_E$, where
  $$E(O,K) = \gamma(m+1)\ \|\ \mathrm{rk}(\rho_0)\ \|\ \mathrm{rk}(\rho_1)\ \|\ a\ \|\ \chi\ \|\ \gamma(K+1).$$
  - $\gamma(x)$, for an integer $x \ge 1$, is the Elias gamma code: $\lfloor \log_2 x \rfloor$ zeros, then $x$ in binary
    ($2\lfloor \log_2 x \rfloor + 1$ bits).
  - $\mathrm{rk}(\rho)$ is the Lehmer rank of $\rho \in \mathrm{Sym}(\{0,\dots,N-1\})$, $N = 2^m$:
    $\sum_i d_i\,(N-1-i)!$ with $d_i = \#\{j > i : \rho(j) < \rho(i)\}$, written big-endian in exactly
    $\lceil \log_2 N! \rceil$ bits (0 bits at $m = 0$).
  - $a$ and $\chi$ are $2^m$-bit truth tables in order $v = 0,\dots,2^m-1$. E is defined for prediction tests,
    $F = \mathrm{graph}(\chi)$, which are the only verdict-bearing tests (PE-01 §6).
  - E is prefix-free: $\gamma$ is prefix-free, and once $m$ is decoded every field up to $\gamma(K+1)$ has fixed length.
    The decoder rejects ranks $\ge N!$. Checked as EN.
  - Lengths: $|E| = 3 + \gamma$-part at $m = 0$; $9 + \cdot$ at $m = 1$; $21 + \cdot$ at $m = 2$; $53 + \cdot$ at
    $m = 3$; $127 + \cdot$ at $m = 4$, each plus $|\gamma(K+1)|$.
  - E is one decoder for every $m$ and $K$; it is not tuned to any observer class. It is shorter than $S_R$ for
    $m \ge 2$ and not minimal for structured classes (a linear filter has a shorter class-specific code). Results under
    E are statements about E only.
- **Invariance caveat.** Every charge is relative to a fixed interpreter whose own description is not charged, as the
  generator's $\varphi$ is not charged. §5 (INT) builds that interpreter for every verdict-bearing witness: the charged
  bits sit in a read-only program register in the visible sector, and the composite stays a bijection with no
  hidden-sector access.

### 2.2 Description-complexity proxy

No separate description-complexity model governs any outcome (owner decision O3, recommendation in `NOTES.md`).
- For every witness the verdict also reports, as information only, $|E|$ of its reduced form: the observer restricted
  to the memory states reachable from $v_0$, quotiented by Moore equivalence of $(a, \chi)$ outputs, relabelled
  canonically and padded with the identity to $2^{m'}$ states. Restriction and quotient keep $\rho_0, \rho_1$
  permutations, because the reachable set of a permutation pair is invariant and a surjection onto a finite quotient is
  a bijection.
- The reduced form is itself an enumerated observer at its own $m'$ (all $m \le 2$ are enumerated, and $m = 0$ is added
  in §3.1), so for the existence question the minimum E-charge over a behaviour class is already attained inside the
  enumeration. That is why the proxy is information, not a model.

### 2.3 Threshold

$\theta = n + 1$ under U, R and E, with $n$ the LFSR degree, for every generator including `G_clkfix`. θ does not
change with what is charged (owner decision O1). A charge that moved θ with it would re-absorb the charge.

**Condition (f) restated.** For model $C \in \{U, R, E\}$: (f$_C$) $F_C(O, K) \le \theta$. (f$_U$) is PE-01's (f).

### 2.4 Drafting-time arithmetic (not results)

These follow from the definitions alone (`NOTES.md` §4). AR-C re-derives them from the composite and from $Z(\varphi)$,
$K_{\rm cx}(\varphi)$ at run time, and any difference halts the stage.

| $m$ | $F_U$ | $F_R$ | $F_E$ (K = 4..6; K = 7) |
|---|---|---|---|
| 0 | $c+1$ | $2c + 4$ | 12; 14 at $c = 3$ |
| 1 | $c+2$ | $2c + 12$ | 19; 21 at $c = 3$ |
| 2 | $c+3$ | $2c + 31$ | 32; 34 at $c = 3$ |
| 3 | $c+4$ | $2c + 76$ | 65; 67 at $c = 3$ |
| 4 | $c+5$ | $2c + 181$ | 140; 142 at $c = 3$ |

- **PE-01's witness** ($m = 2$, $K = 7$): $F_U = 6$, $F_R = 37$, $F_E = 34$, against $\theta = 6$.
- **Every window needs $K \ge 4$** ($w = 3$ and $K \ge Z + 4$), so $c \ge 3$. The least $n$ with $n + 1 \ge F_C$ at
  $K = 4$ is: $m = 0$: R 9, E 11; $m = 1$: R 17, E 18; $m = 2$: R 36, E 31; $m = 3$: R 81, E 64; $m = 4$: R 186,
  E 139. These are lower bounds: a larger $Z(\varphi)$ raises the least admissible $K$ and with it $c$.
- **Consequences, as facts about the accounting models:**
  - at $n \le 8$ every charged region is empty, for every observer class of PE-01 and PE-02;
  - for $m \ge 2$ the charged region is empty at every $n$ below 31 (E) or 36 (R), beyond the reach of exact
    enumeration; PE-02 does not compute there;
  - a charged witness can exist in PE-02's scope only for $m \le 1$, at $n \ge 9$.
- **Reading.** An empty region is reported as a property of the accounting model, never as a measurement and never as
  "no witness found" (PE-01 §6 item 5).

## 3. Classes and scope

### 3.1 Observer classes

All observers are PE-01 §3 observers $(\rho_0, \rho_1, a, F)$ on the enlarged visible sector, with PE-01's round
order ($v \leftarrow \rho_x(v)$; $x \leftarrow x \oplus a(v)$; generator step), prepared $v_0 = 0^m$, the clocked
readout, and no hidden-sector access.

| Class | Members | Activity |
|---|---|---|
| `emb_m0_all` (new) | $m = 0$: $a \in \{0, 1\}$ constant, every $\chi$ | active if $a = 1$ |
| `emb_m1_all`, `emb_m2_all` (PE-01) | all 16 and 9216 tables, every $\chi$ | active iff $a \not\equiv 0$ |
| `emb_m3_passive` (PE-01) | canonical forms up to conjugacy fixing $v_0$ | passive |
| `plin_m1`–`plin_m4` (PE-01) | $\rho_x(v) = Av \oplus xb$, $A \in \mathrm{GL}(m,2)$ | passive |

- **Change from PE-01: $m = 0$ is added.** Under R and E it is the cheapest observer, and §2.4 shows it is the first
  to become admissible. Leaving it out would exclude the candidates most likely to survive the charge. Under U it is
  behaviourally contained in $m = 1$ ($\rho = \mathrm{id}$) but has a smaller footprint.
- **Activity is a property of the table, not of the class name.** Factor reporting (§6) splits `emb_m*_all` into
  its active ($a \not\equiv 0$) and passive ($a \equiv 0$) members. PE-01's per-subclass cells stay as recorded.
- **Prediction tests only bear on verdicts**, as in PE-01; distinguishing tests are not computed in PE-02.

### 3.2 The intervention-ablated observer

For $O = (\rho_0, \rho_1, a, \chi)$, $\mathrm{abl}(O) = (\rho_0, \rho_1, 0, \chi)$. As a set,
$\mathrm{abl}(\text{`emb\_m}k\text{\_all'})$ is PE-01's passive subclass of the same $m$ (checked as IA), so class-level
coverage of the ablation is complete. The secondary question uses the map witness by witness (§4.3).

### 3.3 A lemma that structures the secondary question

**Lemma A-SIM (stated now; proof below; independent plan review required before it is relied on).** Let the hidden
trajectory not depend on $x$ (`G_lin`, `G_filt`, `G_clkfix`, `G_clkfix_u`). For every observer $O$ with memory $m$
there is a passive observer $\mathrm{sim}(O)$ with memory $m + 1$, on the same generator, whose prediction advantage
equals that of $O$ at every $K$ and for every prior.

*Proof.* Let $x^{\rm p}_t$ be the visible bit without interventions and
$A_t = \bigoplus_{s<t} a(v_{s+1})$. With the hidden path fixed by the initial state, $x_t = x^{\rm p}_t \oplus A_t$
pathwise. Define $\mathrm{sim}(O)$ on states $(v, A)$, start $(v_0, 0)$, by
$\rho'_{y}(v, A) = (v', A \oplus a(v'))$ with $v' = \rho_{y \oplus A}(v)$, and guess $\chi'(v, A) = \chi(v) \oplus A$.
For each $y$ this is a bijection: $A = A' \oplus a(v')$ and $v = \rho^{-1}_{y \oplus A}(v')$. Reading $x^{\rm p}_t$, it
holds $(v_t, A_t)$ at every $t$, so $\{\chi'(v_K, A_K) = x^{\rm p}_K\} = \{\chi(v_K) = x_K\}$ pathwise; under $Q_p$ both
guesses are correct with probability exactly 1/2. ∎

Consequences used by the plan:
- On autonomous generators, activity is worth at most one memory bit under U. ACT-SIM (§5) checks the identity
  exactly; a failure voids the stage.
- With the matched prior, `G_clkfix` and `G_clk` have the same passive record law (CA-EQ). An active $m$ observer on
  `G_clkfix` therefore has exactly the advantage of the passive $(m+1)$ observer $\mathrm{sim}(O)$ on `G_clk`. The clock
  ablation separates backaction from the extra bit that activity carries on any generator.
- On `G_clk` the lemma does not apply, because the hidden step depends on $x$.

### 3.4 Generators, $n$ and $K$ per part

| Part | Generators | $n$ | Observer classes | $K$ range | Models |
|---|---|---|---|---|---|
| A: PE-01 range | `G_lin`, `G_filt`, `G_clk` (PE-01 data, read-only); `G_clkfix`, `G_clkfix_u` (new) | 3..8 | new generators: every class of §3.1, `emb_m3_passive` with PE-01's A1 caps at $n = 7, 8$; PE-01 generators: `emb_m0_all` only | $K \le K_{\rm cx}(\varphi)$ | U computed; R and E structurally empty (§2.4) |
| A-pop: secondary population | `G_clk`, and the ablations of §4.3 | 3..8 | active members of `emb_m1_all`, `emb_m2_all`, `emb_m0_all` | $K \le K_{\rm cx}(\varphi)$ | U |
| B: charged sweep | `G_lin`, `G_filt`, `G_clk`, `G_clkfix`, `G_clkfix_u` | 9..$N_{\max}$ | `emb_m0_all`, `emb_m1_all` (both include their passive members; `plin_m1` is a subset) | $\max(Z+4, w) \le K \le \min(K_{\rm cx}, K^{C}_{\max}(n, m))$ | U, R, E on the same cells |
| C: controls | §5 | as stated | as stated | as stated | as stated |

- $K^{C}_{\max}(n,m)$ is the largest $K$ with $F_C \le n+1$, taken over $C \in \{R, E\}$; U is evaluated on the same
  cells, so every U value in Part B is labelled "uncharged, within the charged search range".
- **$N_{\max}$ is owner decision O4** (recommended 24). From §2.4, $m = 1$ cannot be admissible under either charged
  model below $n = 17$, and its actual onset depends on $Z(\varphi)$, which AR-C computes.
- **Coverage within the enumeration.** In Part B every observer of every PE-01 class, and of `emb_m0_all`, that can
  meet (f$_R$) or (f$_E$) at $n \le N_{\max}$ is enumerated, because §2.4 makes every $m \ge 2$ cell structurally empty
  there. No observer is excluded for any other reason.
- **K0.** Family status is reported as in PE-01 at $n \le 8$, for $\mathfrak{F}_{\rm clkfix}(n)$ as well. At $n > 8$ it
  is not computed (owner decision O6). It bears on no outcome.
- **Not run in PE-02:** PE-01's unrestricted class and classes B1–B4, distinguishing tests, $r > 1$ runs and class-$\mathcal{Q}$ references.

## 4. Advantage, witnesses and the secondary population

### 4.1 Advantage

As PE-01 §2: prediction tests, reference $Q$ with independent fair visible outputs under the same policy,
$\mathrm{adv}^{\rm pred}_O(\varphi, K') = |\Pr[\chi(v_{K'}) = X_{K'}] - 1/2|$ (`abs`, governing, PE-01 A2 D-SIGN) and
the signed form as a sensitivity analysis on the same data. Counts are exact integers over the prior's support; every
advantage is an exact rational.

### 4.2 Witness conditions

PE-01's conditions (a)–(f) stand, except as stated here, each with its reason.

- **(a′)** $\varphi \in \{$`G_lin`$(p_n)$, `G_filt`$(p_n)$, `G_clk`$(p_n)$, `G_clkfix`$(p_n)$, `G_clkfix_u`$(p_n)\}$,
  $3 \le n \le 8$ in Part A and $9 \le n \le N_{\max}$ in Part B, passing EX6 under its own prior.
  - *Change:* $n$ beyond 8, because every charged region is empty at $n \le 8$ (§2.4); the two ablated generators,
    because a witness on them must count, not be excluded as a comparator.
  - The fixed-generator reading of PE-01 A2 WIT-A is kept: other family members enter only through K0 status.
- **(b′)** $O$ is a member of a §3.1 class, given as explicit tables with its readout clock, and passes EX1, EX7, EX8
  and IM3 on the clocked composite. For a witness under R or E it also passes INT on the interpreted composite (§5).
  *Change:* $m = 0$ is admitted (§3.1).
- **(c)** $K \le K_{\rm cx}(\varphi) = \lfloor \ell_{\rm med}(\varphi)/2 \rfloor$, the median orbit length taken under
  the generator's own prior. Unchanged except for that clause, which `G_clkfix` and `G_weak` need.
- **(d)** Unchanged: the same $O$ and $\chi$ give $\mathrm{adv}^{\rm pred} \ge \delta_{\rm cx} = 1/8$ exactly at every
  $K' \in [K - 3, K]$, $K \ge 3$; `abs` governs and `signed` is the sensitivity analysis.
- **(e)** Every PE-02 checkpoint (§5) is green.
- **(f$_C$)** $F_C(O,K) \le \theta = n + 1$, for the model $C$ under which the witness is stated (§2.3).

A witness meeting (a′)–(e) and (f$_C$) is **admissible under C**. Under U it refutes the universal form PE-01 refuted;
that is a restatement and is recorded only. Under R or E it refutes the stronger statement "every embedded observer
whose memory, clock, output and charged description fit in θ is unable to predict, for every finite reversible
realization".

**Zero argument, generalized.** $Z(\varphi)$ is the largest $k$ such that, for every control sequence $c_{0:k-1}$ and
every value of $x_0$, the first $k$ increments are jointly uniform under the conditional prior of the hidden state given
$x_0$. PE-01's proof (§7) goes through unchanged, so $\mathrm{adv}^{\rm pred} = 0$ at every $K' \le Z$ for every
observer and the window floor $K \ge Z + 4$ stands. *Change:* PE-01 assumed the hidden state independent of $x_0$,
which fails for `G_clkfix` ($q_0 = x_0$) and `G_weak`; the conditional form reduces to PE-01's where that holds. For
generators whose hidden step is $\mathbb{F}_2$-linear for each fixed control sequence (`G_lin`, `G_clk`, `G_clkfix`),
joint uniformity is equivalent to $\mathbb{F}_2$-rank $k$ of the increments' linear forms, and AR-C computes it that way
at $n > 8$; at $n \le 12$ both the rank and the exhaustive computation are run and must agree.

### 4.3 The secondary population and its comparisons

- **Population.** $W_{\rm act}$ is every triple $(O, \chi, K)$ with $O$ active ($a \not\equiv 0$), $m \le 2$, on
  `G_clk`$(p_n)$, $n = 3,\dots,8$, meeting (a′)–(e). Condition (f) is not required for membership (owner decision O7),
  and each member records whether it meets (f$_U$). At $n = 5$, $K = 7$, $m = 2$ the admissible members must number
  36 under `abs` and 12 under `signed`, PE-01's recorded counts (UX).
- **Per member, three exact curves over the window $[K-3, K]$:**
  - $O$ on `G_clk` (the witness itself);
  - $\mathrm{abl}(O)$ on `G_clk`;
  - $O$ on `G_clkfix`, and, under O5, on `G_clkfix_u`.
- **Per-member labels:**
  - `INTERVENTION_NEEDED` if $\mathrm{abl}(O)$ fails (d) at $K$; otherwise `INTERVENTION_NOT_NEEDED`;
  - `BACKACTION_NEEDED` if $O$ on `G_clkfix` fails (d) at $K$; otherwise `BACKACTION_NOT_NEEDED`.
- **Class level,** per $(n, m)$: whether any active observer has a window meeting (a′)–(e) on `G_clkfix`, given that
  one does on `G_clk`.
- **What is reported:** the four-way table of counts (exact integers) per $(n, m, K)$ cell, never pooled across cells.
  "The advantage is tied to the clock responding to interventions" is printed for a cell only if every member there is
  `BACKACTION_NEEDED` and no active window exists on `G_clkfix` in that $(n, m)$. Otherwise the counts are printed
  without that sentence.

## 5. Controls and the invariant→checkpoint table (§A.41)

Every numerical row is exact integer or `Fraction` arithmetic. A failure of any row makes the stage VOID (§6). Each
checkpoint writes a JSON record in a stated schema with a `pass` flag and the exit status of the check that computed it;
the verdict reads those records and job conclusions, never log text (§A.44).

**The four controls #934 requires, each able to fail:**

1. **RP-01 (PE-01 witness, uncharged, byte-identical replay).** At PE-01's run head
   `549641460b8ddb536178f95fac2ec9390e84a987`, in a detached checkout with full history to `af38dc2d`, run
   `python3 -I -B .../pe01_bounded_tests_v1/run.py replay n5-clk --mode result --against <PE-01 results/shards> --out <dir>`.
   - It must exit 0, and the new `n5-clk.json` must have sha256
     `3f6121e83e75ed7ed5d43817bb8fc63dc73ad5fbf7acd763c3261e11d972a963`, equal to `results/shards/n5-clk.json`.
   - The witness record in it (observer 2361, χ 0, K = 7, `adv_pred` 1/8, 5/32, 5/32, 1/8, footprint 6,
     `table_size_bits` 31, window counts 36 and 12) is the object R, E and §4.3 act on.
   - Also: PE-01's `verdict.py` regenerates `verdict.json` and `verdict.txt` byte-identically from
     `measurements.json` (sha256 `f17109f10379d648fcb055c2a1868666205fae8499b35ca65ecedae7a41f067a`).
2. **CH-IFF (charged rejection iff charged footprint > θ).** The admissibility classifier, run for R and E on:
   - every witness record in PE-01's 38 shards (all generators, $n$ and subclasses), its $F_C$ computed from the record's
     tables (TR, EN) and its $m$, $K$;
   - synthetic boundary witnesses with $F_C = \theta$ and $F_C = \theta + 1$, for each model and for $m = 0, 1$;
   - the planted witness of control 3.

   It must admit exactly those with $F_C \le \theta$, and every refusal must name (f$_C$) and no other condition.
   The PE-01 records alone exercise only rejection (§2.4), which is why the boundary cases and the planted witness are
   part of the control.
3. **PL (planted passive witness on a weak generator).** The production sweep, unchanged, on `G_weak(13)`, classes
   `emb_m0_all` and `emb_m1_all`, $K \le 15$:
   - it must report the passive $m = 0$ observer with $a = 0$, $\chi \equiv 0$ as meeting (b′)–(e) and (f$_C$) under
     U, R and E at $K = 7$, window $[4,7]$, with $\Pr[\chi = X_{K'}] - 1/2 = 1/2 - K'/2^{13}$ exactly. Condition (a′)
     is replaced by membership in the control set, and the record is labelled a control, never a witness;
   - on `G_weak_mut(13)` every observer must give advantage exactly 0 at every $K \le 13$, and no window may be
     reported.
4. **MUT-NC (mutant that drops the charge).** The full classifier with $T_C \equiv 0$:
   - its R and E outputs must equal the U outputs byte for byte after the model label is normalized;
   - the real R and E outputs must differ from the mutant's on PE-01's witness (mutant admits, real refuses) and on
     every U-admissible witness with $F_C > \theta$.

   If the real charged outputs equal the mutant's, the charge is inert and the stage is VOID.

| Invariant | Checkpoint | Measured by |
|---|---|---|
| PE-01's witness and verdict are reproduced exactly | RP-01 | control 1: exit status, sha256 of the replayed shard, verdict regeneration |
| PE-02's own code agrees with PE-01 where both compute | UX | §4.3: for `G_clk`, $m \le 2$, $n \le 8$, PE-02's admissible window cells and counts equal PE-01's recorded `windows` entries; the witness curve equals RP-01's |
| Admissibility under C holds iff $F_C \le \theta$ | CH-IFF | control 2 |
| A planted passive witness is found, and its mutant gives none | PL | control 3 |
| The charge is not inert | MUT-NC | control 4 |
| $T_R$ is measured, not reprinted | TR | the bit length of $S_R$ equals the §2.1 formula for every enumerated observer; for every PE-01 witness record it equals the recorded `table_size_bits` |
| E is the stated code and is prefix-free | EN | for every observer with $m \le 2$, every $\chi$ and every $K \le 63$: decode(encode) is the identity, the length equals the §2.1 formula, and no codeword in that set is a prefix of another; $\gamma$ alone for every $x \le 2^{20}$; at $m = 3, 4$ the same on every observer that appears in any record |
| The charge is physical: the program sits in a read-only visible register | INT | for each verdict-bearing R or E witness, and for PE-01's witness as calibration: the interpreted composite with a program register of width $T_C$ is a bijection on each program slice (EX1); the register, $h$ and $q$ are untouched by observer maps, and $\varphi$ is the identity on the observer registers (EX8); its record law and prediction curve equal those of the tables-in-dynamics composite (IM3-C); its visible width less the system bit equals $F_C$ (FP-C). For $m \le 1$ every valid program is checked |
| Every map is a bijection | EX1 | as PE-01, for every generator including `G_clkfix`, `G_clkfix_u`, `G_weak`, `G_weak_mut`, at every $n$ used |
| Priors and laws sum to 1 | EX2 | exact sums |
| No float on the verdict path | EX3 | type assertion on every verdict input |
| $p_n$, $p'_n$ follow §1.1 and are primitive | EX4 | the least-primitive rule is recomputed and must equal §1.1's table; order of $z$ is $2^n - 1$ |
| $(\ell, L_p)$ is observable | EX5 | $\mathbb{F}_2$ rank $n$, every $n$ |
| T-level (C1) holds for every (a′) generator | EX6 | exact one-step visible matrix under the generator's own prior |
| Settings are measurement-independent | EX7 | the joint prior is the generator's prior $\otimes\,\delta_{v_0}$ and EX8 holds |
| No hidden-sector access | EX8 | as PE-01, with $q$ part of the hidden sector |
| The embedded simulation is correct | IM3 | aggregated and full-state simulations agree for all observers at $n \le 4$ on every generator, and for every verdict-bearing witness |
| The $Q_p$ side is correct | IM6 | `G_tape(K)` gives $P_p = Q_p$ exactly for every observer of `emb_m0_all`, `emb_m1_all`, `emb_m2_all` at $K \le 12$ |
| The clock ablation does what it says | CA-STRUCT | the hidden step of `G_clkfix` is the same for $x = 0$ and $x = 1$ on every state; that of `G_clk` differs on some state. Self-test: substituting `G_clk` for `G_clkfix` must fail it |
| The ablation changes only responsiveness | CA-EQ | for every $n$ used, every seed of $\mu^{\rm fix}$ and every $K \le K_{\rm cx}$, the passive record of `G_clkfix` equals that of `G_clk` from the same $(x_0, h_0)$ |
| The intervention ablation is the stated map | IA | $\mathrm{abl}(O)$ has $a \equiv 0$ and the same $\rho_0, \rho_1, \chi$; the image of each `emb_mk_all` equals PE-01's passive subclass as a set. Self-test: the identity map in place of abl must fail it |
| Lemma A-SIM holds as computed | ACT-SIM | for every active observer with $m \le 1$ at every $n$ used, and with $m = 2$ at $n \le 6$, on `G_lin`, `G_filt`, `G_clkfix`, `G_clkfix_u`: the exact curve of $O$ equals that of $\mathrm{sim}(O)$, computed through the passive code path, at every $K \le K_{\rm cx}$; on `G_clk` the check is reported, not required |
| PC zero and firing | PC | as PE-01 §4 for the embedded classes, including `emb_m0_all`; the zero at $K \le n$ on `G_lin(p_n)` at every $n$ of Part B |
| Complement symmetry | SY | as PE-01 for the flip-commuting generators; `G_clk`, `G_clkfix`, `G_clkfix_u` exempt |
| Inclusions | MO | as PE-01, plus: every R- or E-admissible witness is U-admissible ($F_C \ge F_U$); $m = 0$ curves are contained in $m = 1$ ($\rho = \mathrm{id}$) |
| Footprints are measured | FP | as PE-01, on the clocked composite, for U; FP-C under INT for R and E |
| The witness conditions are evaluated mechanically | CX | as PE-01 §5 CX, with (f) evaluated per model. Self-test mutants, each refused on its own condition: a window value $1/8 - 2^{-K-2}$ (d); $F_U = \theta + 1$ (f$_U$); $F_R = \theta + 1$ with $F_U \le \theta$ (f$_R$); $F_E = \theta + 1$ with $F_U \le \theta$ (f$_E$); $K = K_{\rm cx} + 1$ (c) |
| The admissible regions are derived | AR-C | $Z(\varphi)$ (generalized, §4.2) and $K_{\rm cx}(\varphi)$ for every generator and $n$ used; the regions under U, R and E are recomputed from them and from the measured footprints, and must equal §2.4's drafting values where those apply. Z by $\mathbb{F}_2$ rank and by exhaustive enumeration must agree at $n \le 12$ |
| Deterministic replay | RP | every PE-02 shard's measurement JSON is byte-identical on rerun |
| The plan precedes the code | PIN | the measurement JSON records this file's blob and the commit that froze it; that commit is an ancestor of every code commit |
| Runs wait for the fixed parameters | TH | the measurement JSON records the `pe02-parameters` block of the amendment that resolves §9 and that amendment's blob and commit; a run refuses to start without it, or if any value differs from it |
| Verdicts are generated from measurements | VG | as PE-01: regeneration is byte-identical; a copy with any control flag flipped yields VOID; a verdict lacking the §7 resource-model sentence fails |

## 6. Decision rule and outcome classes (fixed before computation)

1. **VOID** takes precedence: any failed or unevaluated checkpoint voids the stage, the verdict names it, and nothing
   else is printed as a verdict. Controls run first.
2. **Generated text.** `verdict.py` writes the verdict from the measurement JSON alone; every number in it is read from
   the measurements.
3. **Cell status,** per (generator, $n$, subclass, model):
   - `WITNESS`: some $(O, \chi, K)$ in the cell meets (a′)–(e) and (f$_C$);
   - `NONE`: the cell's region is non-empty, every $K$ in it was computed, and none meets them;
   - `REGION_EMPTY`: AR-C finds the region empty. This is a property of the accounting model, not a search result;
   - `NOT_RUN` or `INCOMPLETE` (with completed cells kept, as PE-01 A1): no verdict.

   Cells are never pooled for attribution. Resource attribution follows PE-01 §6 item 4 within each cell and model.
4. **Factor outcome, per (activity $\alpha$, generator $\gamma$) and per charged model $C \in \{R, E\}$,** reported
   separately for each $C$. Let $\mathrm{wit}(\alpha, \gamma, M)$ mean that some cell of that activity, generator and
   model $M$ is `WITNESS`:
   - `SURVIVES_CHARGED[C]`: $\mathrm{wit}(\alpha, \gamma, C)$;
   - `UNCHARGED_ONLY[C]`: not $\mathrm{wit}(\alpha, \gamma, C)$, and $\mathrm{wit}(\alpha, \gamma, U)$, and no $C$-cell
     is `NOT_RUN` or `INCOMPLETE`. It carries the sub-label `structural` if every $C$-cell is `REGION_EMPTY`, and
     `searched` otherwise;
   - `NO_WITNESS_IN_SCOPE`: neither $\mathrm{wit}(\alpha, \gamma, U)$ nor $\mathrm{wit}(\alpha, \gamma, C)$, and no cell
     of either model is `NOT_RUN` or `INCOMPLETE`;
   - `INCOMPLETE` otherwise: no factor verdict.

   Since every $C$-witness is a U-witness (MO), `SURVIVES_CHARGED` without a U-witness cannot occur, and its occurrence
   voids the stage.
5. **Activity contrast, per (generator $\gamma$, model $M \in \{U, R, E\}$):**
   - `ACTIVE_ONLY`: $\mathrm{wit}(\text{active}, \gamma, M)$ and not $\mathrm{wit}(\text{passive}, \gamma, M)$, with
     every passive cell complete;
   - `PASSIVE_ALSO`: both;
   - `PASSIVE_ONLY`: passive only;
   - `NEITHER`: neither, every cell complete;
   - `INCOMPLETE` otherwise.
6. **Factor scope.** Each factor outcome prints the cells it rests on: $n$ range, subclasses, $K$ ranges, which cells are
   `REGION_EMPTY`, and, for Part A generators carried from PE-01, that their U cells are PE-01's frozen results.
7. **Secondary question.** Reported as §4.3 fixes, per cell, with the generated sentence only under the stated
   condition.
8. **Classification of each statement:** PROVED (exhaustive finite, scope printed), PROVED (with a reviewed written
   proof; Lemma A-SIM is the only candidate), CONDITIONAL (hypothesis named), OPEN. Verification layers stay distinct
   (§8).
9. **Favourable readings** for the claim under audit are `UNCHARGED_ONLY`, `NO_WITNESS_IN_SCOPE` and
   `BACKACTION_NEEDED`. Each is printed with its enumerated scope and is not extended beyond it.
   `UNCHARGED_ONLY[structural]` is printed as a property of the accounting model, never as a measurement.
10. **Productivity test (§A.31), fixed now.** PE-01's REPORT already states that charging the 31 table bits would put
    its witness outside θ. A PE-02 result is a candidate gem only if it is strictly stronger than that sentence and
    either constrains `book/ch18-beyond.md:114` as scoped on `main`, or exposes a hidden assumption. Results that only
    restate it (`UNCHARGED_ONLY[structural]` for $m \ge 2$, the arithmetic of §2.4) are recorded only.

## 7. Scope and non-claims

- No statement about the actual world's hidden sector, nor about the $10^{-32}$ statement (`ch18-beyond.md:56–58`).
- No cryptographic, circuit-security or distinguishing claim.
- A negative result covers only the enumerated class, generators, $n$, $K$ and accounting model.
- No PE-02 outcome establishes the narrower claim the scoped ch18 sentence leaves open, about observers of bounded
  memory that only read the source. A charged witness, its absence and the ablation counts are each stated for their
  class only.
- Results under E are about E, and no result is stated as one about description complexity.
- The realization conditions stay "T-level (C1) holds; C2–C4 not checked" for every generator.
- **Resource-model sentence,** repeated in the generated verdict: "Admissibility under R and E is a consequence of the
  selected accounting model: memory + clock + output + charged description ≤ θ = n + 1, relative to a fixed uncharged
  interpreter. It is not a limit OI imposes on observers."
- No manuscript change, dispatch, theorem designation or merge without separate owner approval. A finding bearing on
  `ch18-beyond.md:114` and its mirror `The-Incompleteness-of-Observation-FULL.md:4932` is reported here only.

## 8. Verification layer

Exact enumeration of the joint state with integer counts and `Fraction` advantages, as PE-01. Lemma A-SIM is a written
proof with a computational regression (ACT-SIM); the computation does not stand in for the proof, and the proof does not
stand in for the computation of any cell. Numpy is used on integer arrays only.

## 9. Owner decisions before freeze

Each is fixed by an amendment in `amendments/`, before any code, and carried into the `pe02-parameters` block that TH
reads. The recommendations and their reasons are in `NOTES.md` §6.

| Id | Decision | Options | Recommended |
|---|---|---|---|
| O1 | θ under charged models | (i) $n+1$ for U, R, E; (ii) $n+1 + D_C(\varphi)$, the generator's own description charged alike | (i) |
| O2 | Which charged models govern | R and E, each reported separately; R only; E only | both |
| O3 | Description-complexity proxy | information only (§2.2); a third governing model | information only |
| O4 | $N_{\max}$ | 8 (no charged computation); 22; 24 | 24 |
| O5 | Clock-ablated prior | matched primary with uniform variant; matched only; uniform only | matched primary with uniform variant |
| O6 | K0 status at $n > 8$ | not computed; computed on a fixed subfamily | not computed |
| O7 | Secondary population | all active (a′)–(e) witnesses; admissible (f$_U$) only | all |
| O8 | Stage name | PE-02 per #934, with the thread README's PE-02 renamed; or this stage renamed | owner's choice |
| O9 | Lemma A-SIM | adopt for ACT-SIM and interpretation after plan review; drop | adopt |

Draft block (values open):

```json pe02-parameters
{
  "amendment": "TBD",
  "theta_U": "n+1",
  "models": "OPEN (O2)",
  "theta_rule": "OPEN (O1)",
  "N_max": "OPEN (O4)",
  "clkfix_priors": "OPEN (O5)",
  "K0_beyond_8": "OPEN (O6)",
  "secondary_population": "OPEN (O7)",
  "n_ctl": 13,
  "delta_cx": "1/8",
  "w": 3,
  "d_rule": "abs",
  "d_sensitivity": "signed"
}
```

## 10. Resources and CI (§A.40)

The estimates below are not measurements; a local run exceeding its row by a factor of 3 is stopped and moved to CI.
PE-01's own timings scale them: its `n8-clk` shard took about 1150 s and `n8-clk-m3` about 850 s.

| Work | Estimate | Where |
|---|---|---|
| EX, EN, TR, CH-IFF, MUT-NC, CA-STRUCT, IA, PL ($2^{13}$ seeds), CX self-test; Part A at $n \le 5$ | under 10 min | local smoke |
| RP-01: PE-01 `n5-clk` replay at `54964146`, and PE-01 verdict regeneration | about 5 min | CI, one job |
| Part A: `G_clkfix` and `G_clkfix_u`, every class, $n = 3..8$ | 2–4 h in total | CI, sharded by $(n, \text{generator})$, `emb_m3_passive` in its own jobs as PE-01 |
| A-pop: active $m \le 2$ on `G_clk`, $K \le K_{\rm cx}$, with ablations | under 1 h | CI, sharded by $n$ |
| ACT-SIM at $m = 2$, $n \le 6$ | under 30 min | CI |
| Part B, $N_{\max} = 24$: about $2^{25}$ seeds at $n = 24$; $m = 1$ to $K \le 63$, $m = 0$ to $K \le K^{R}_{\max}$ | 3–6 h in total, about $10^{11}$ elementary updates at the top $n$ | CI, sharded by $(n, \text{generator})$, each job under 1 h |
| AR-C at $n > 8$ ($\mathbb{F}_2$ rank for Z; cycle decomposition for $K_{\rm cx}$) | under 30 min | CI, with Part B shards |
| INT on verdict-bearing witnesses | minutes | CI |

- The workflow is `workflow_dispatch`-only and is part of the code commits; no push launches it. Every dispatch needs
  owner approval (§A.43 item 4).
- Shard outputs are committed as structured JSON recording the commit, the recipe and the run id (§A.42 item 1); they
  are never relied on as logs (§A.44).
- Local work respects §A.40's disk thresholds; Part B never runs locally.

## 11. Literature (cited, not rederived)

- **Tagging rule.** PE-01 amendment A3's rule applies, fixed now and before any of the works below is read, with its
  scope set to PE-02's results: admissible witnesses under R or E, the §4.3 counts, and Lemma A-SIM. COVERED-literature
  needs a first-hand reading that states or directly implies the result for the same kind of generator and observer;
  coverage in kind is recorded as such; a work read through an abstract, survey or citing paper supports no tag.
- **No novelty claim** is made, and candidate-NEW is not assignable, until at least these are read first-hand:
  Rueppel, "When shift registers clock themselves", EUROCRYPT '87, LNCS 304; Gollmann–Chambers, "Clock-controlled
  shift registers: a review", IEEE JSAC 7(4):525–533 (1989); and the works PE-01's tag annex lists as unread
  (Chambers–Gollmann 1988; Beth–Piper 1984; Meier–Staffelbach 1989 and 1994; Golić–O'Connor 1994; Živković 1991;
  Kholosha 2001; Gomułkiewicz et al., WEA 2005 and 2006).
- **What PE-02 must state it adds beyond the two covered-in-kind results** (owner, #934): beyond the 2006 clock-control
  fault attack (Gomułkiewicz–Kutyłowski–Wlaź), whether the PE-01 witness survives an explicit charge on the observer's
  description, and whether its advantage needs the clock to respond; beyond AGHP's mechanism, whether passive observers
  of any accounted size gain on these generators. Neither is claimed novel before the reading above.
- **Bearing on the accounting model, to read before any closure claim:** Feder–Merhav–Gutman, "Universal prediction of
  individual sequences", IEEE Trans. IT 38(4) (1992), finite-state predictability with the state count as the resource;
  Raz, "Fast learning requires good memory", FOCS 2016, bounded-memory learning in which the program is not charged;
  Li–Vitányi, *An Introduction to Kolmogorov Complexity*, for the invariance caveat of §2.1.
- **Definitions only:** Elias, IEEE Trans. IT 21(2) (1975), for $\gamma$; the Lehmer code.

## 12. Package

This directory will hold `PLAN.md` (this file, committed alone when frozen), `NOTES.md`, `amendments/`, the code,
`results/`, `REPORT.md` and `review/`. Any amendment goes in `amendments/` before the code it governs.
