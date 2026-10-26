# PE-02 stage plan: charged observer tables, activity and backaction (revision 2, draft)

**Status: WIP / UNREVIEWED; planning only; no execution authorized.** Revision 2 is not frozen and needs re-review.

Stage plan for Issue #934 in thread OI-PE-1 (`../README.md`). No PE-02 code exists.
- **Revision 1:** `902c4c0d`, reviewed at `2bb45e0b` (`review/REVIEW.md`: ACCEPT WITH CHANGES, R1–R15).
- **Revision 2** applies R1–R5 and R7–R15, R6's reporting change and the review's UX specification. The edit for each
  item is mapped in `CHANGES-r2.md`.
- R6's choices, and O1–O10, are owner decisions. They appear below as marked placeholders **[OWNER: Ox]**, each with
  the review's recommendation, and are collected in §9.
- **Drafting base:** `research/oi-pseudoentropy-20261025`, at `efbfd0d7` for revision 1 and `2bb45e0b` for revision 2.
  The corpus sentence it bears on is read on `main` at `c967d6a931c294e456053be5e3bf5bb4f2d9ad1c`.
- The drafter's sources and readings of #934 are in `NOTES.md`.

**[OWNER: O8, stage name.]** This file keeps the name "PE-02" from #934. PE-01's frozen PLAN (§3, §7, §10 item 5) and
the thread README bind "PE-02" to a different stage: computational versus physical observers. The review recommends
renaming this stage to the next unused identifier, PE-04, and retitling #934 and this directory before freeze. Until
the owner decides, "PE-02" in this file means the stage of #934.

PE-01 (`../pe01_bounded_tests_v1/`) is an immutable reference. Its plan, amendments A1–A3, results, verdict and
reviews are read, never edited. PE-02 neither re-runs PE-01 as a study nor optimizes it. It does three things with it:
- reads PE-01's retained measurements;
- replays one PE-01 shard byte for byte as a control (§5, RP-01);
- recomputes PE-01 cells only where the secondary question needs the full witness population (§4.3), cross-checked
  against PE-01's recorded counts (UX).

## 0. Question

PE-01 returned COUNTEREXAMPLE at one admissible cell: `G_clk`, n = 5, `emb_m2_all`, K = 7, footprint 6 = θ = n + 1.
The observer's 31 table bits were held in the dynamics and not charged.

**Main question.** Does an admissible prediction witness of PE-01's kind exist when the observer's description, or a
fixed encoding of it, is charged against the footprint threshold? Which parts of the description are charged is
owner decision O10 (§2.1).

**Secondary question.** Is the advantage tied to the clock responding to the observer's interventions? It is answered
by three comparisons on the same tables:
- the active observer on `G_clk`;
- the same tables with interventions disabled (§3.2);
- the same tables on a `G_clk` variant whose clock ignores the observer's input (§1.2).

**The factors.** Activity (active, passive), accounting (uncharged, charged), and generator (with visible-to-hidden
backaction, autonomous). §6 fixes, before any computation, the outcome each factor combination receives at each $n$.

## 1. Objects

### 1.1 Generators carried over from PE-01

The template, `G_lin`, `G_filt`, `G_clk`, the Fibonacci companion map $L_p$, $\ell(h) = h_0$,
$g(h) = h_0 \oplus h_1 h_2$, the initial law $\mu$ uniform on $\mathcal{C}_V \times \mathcal{C}_H$, the record $X_{0:K}$
and the increments $Y_t$ are exactly those of PE-01 `PLAN.md` §1.

**Polynomials beyond n = 8.** PE-02 extends $n$ for the charged sweep (§3.4). The rule is fixed now.
- $p_n$ is the least primitive polynomial of degree $n$ by integer value, in PE-01's convention
  $p(z) = z^n + \sum_i c_i z^i$ with new bit $\sum_i c_i h_i$. $p'_n$ is its reciprocal.
- The rule reproduces PE-01's $p_n$ and $p'_n$ for $n = 3,\dots,8$ (`design/least_primitive.py`; EX4 checks both
  this and the table below).
- Drafting-time values follow. EX4 re-derives them at run time, and any difference halts the stage.

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

The rule favours sparse feedback, the case most exposed to clock-control prediction. It is kept because it is PE-01's
rule, not chosen for its effect. No other polynomial is substituted after any result.

### 1.2 The clock-ablated generator `G_clkfix(p)`

`G_clk` selects its hidden step by the visible bit after intervention, so an intervention changes the hidden
trajectory. The ablation needs a clock that is the generator's own running parity, out of reach of every intervention.
No variant of `G_clk` on $\{0,1\} \times \mathbb{F}_2^n$ does this, because the pre-intervention visible bit already
carries every earlier intervention. One hidden bit $q$ is therefore added.

- $\mathcal{C}_H = \mathbb{F}_2^n \times \{0,1\}$, state $(x, h, q)$.
- $\varphi^{\rm fix}(x,h,q) = (x \oplus \ell(h'),\ h',\ q \oplus \ell(h'))$ with $h' = \sigma_q(h)$, $\sigma_0 = L_p$,
  $\sigma_1 = L_p^2$.
  - It is a bijection: $\ell(h')$ is read from the image, which gives $q$, $x$ and $h = \sigma_q^{-1}(h')$ (EX1).
  - Its hidden component does not depend on $x$.
- **Prior (matched, primary).** $\mu^{\rm fix}$ is uniform on $S = \{(x,h,q) : q = x\}$.
  - $S$ is invariant without an observer, and $\varphi^{\rm fix}$ restricted to $S$ is isomorphic to `G_clk(p)` through
    $(x, h, x) \mapsto (x, h)$. The visible record is pathwise that of `G_clk(p)` from $(x_0, h_0)$ (CA-EQ).
  - **θ.** $\theta = \log_2|\mathrm{supp}\,\mu^{\rm fix}| = n + 1$, PE-01's $\log_2|\mathcal{C}_V \times \mathcal{C}_H|$
    applied to the invariant support. It is the same value as for `G_clk(p)`.
- **Prior (uniform, reported variant).** `G_clkfix_u(p)` is the same map with $\mu$ uniform on the whole state space.
  - The clock phase $q_0$ is then hidden from the observer, which changes the passive record law.
  - It is reported as its own generator and never pooled with the matched form.
  - **θ.** Every cell is reported at both $\theta = n + 1$ and $\theta = n + 2$
    ($= \log_2|\mathcal{C}_V \times \mathcal{C}_H| = \log_2|\mathrm{supp}\,\mu|$). **[OWNER: O5, the governing value;
    the review recommends $n + 2$, PE-01's definition, with $n + 1$ also reported.]**
- Within the composite, the observer's action changes $x$ only; $(h, q)$ evolves autonomously.

### 1.3 Control generators

- **`G_weak(n)` (planted passive witness).** The template with $\sigma_0 = \sigma_1 = L_{p_n}$ and
  $f(h) = \prod_{i<n} h_i$ (the all-ones indicator), with prior $x_0 = 0$ and $h$ uniform on $\mathbb{F}_2^n$.
  - $L_{p_n}$ cycles the $2^n - 1$ nonzero states, so $\Pr[X_K = 1] = K/2^n$ exactly for $1 \le K \le 2^n - 1$.
  - The memoryless passive observer ($m = 0$, $a = 0$, $\chi \equiv 0$) therefore has
    $\Pr[\chi = X_K] - 1/2 = 1/2 - K/2^n$, which is $\ge 1/8$ for $K \le 3 \cdot 2^{n-3}$.
  - $Z(\text{`G\_weak`}) = 0$, because $Y_0$ is not uniform.
  - **Use.** At $n_{\rm ctl} = 13$, with window $[4,7]$, the planted observer is admissible under all three accounting
    models of §2. $F_E$ equals θ = 14 there, so the control also exercises the boundary.
  - It is a control, never a candidate under (a′).
- **`G_weak_mut(n)` (countercontrol).** As `G_weak` with $f = \ell$.
  - Given $x_0 = 0$ the hidden state is uniform, and the generalized zero argument (§4.2) gives prediction advantage
    exactly 0 for every observer at every $1 \le K \le n$.
  - At $K = 0$ the advantage of $\chi \equiv 0$ is $1/2$, because $x_0 = 0$ is known; $K = 0$ is excluded from the
    countercontrol.
- PE-01's `G_dec`, `G_tape(N)` and `G_lin(p'_n)` are reused for the controls PE-01 used them for (§5).

## 2. Accounting models

### 2.1 What is charged

For an observer $O = (m, \rho_0, \rho_1, a, F)$ with readout trigger $K$, $N = 2^m$ and $c(K) = \lceil \log_2(K+1) \rceil$.
Memory states are the integers $v = 0,\dots,N-1$ in PE-01's labelling: the index $v$ of the tables
`R[o, x, v] = ρ_x(v)` and `Aact[o, v] = a(v)` of `pe01/observers.py`, with $v_0 = 0$.

- **U (uncharged; PE-01).** $F_U(O,K) = m + c(K) + 1$ bits: memory, clock and output. The tables are part of the
  composite dynamics.
- **R (raw tables).** $T_R(O,K) = 2mN + N + 2N + c(K)$, the table size PE-01 prints, and $F_R = F_U + T_R$.
  - **Serialization $S_R$**, which fixes the bit count TR measures:
    - $\rho_0(v)$, then $\rho_1(v)$, as $m$-bit MSB-first entries for $v = 0,\dots,N-1$;
    - $a(v)$ for $v = 0,\dots,N-1$;
    - the indicator of $F$ over $(v,x)$, $v$ major and $x$ minor;
    - $K$ in $c(K)$ bits, MSB-first.
  - **Components:** $\rho_0$: $mN$; $\rho_1$: $mN$; $a$: $N$; readout: $2N$; trigger: $c(K)$.
  - R charges the full readout set $F$ because PE-01's recorded `table_size_bits` does, which lets CH-IFF compare
    against PE-01's records.
- **E (fixed universal encoding).** $T_E(O,K) = |E(O,K)|$ and $F_E = F_U + T_E$, where
  $$E(O,K) = \gamma(m+1)\ \|\ \mathrm{rk}(\rho_0)\ \|\ \mathrm{rk}(\rho_1)\ \|\ a\ \|\ \chi\ \|\ \gamma(K+1).$$
  - **$\gamma(x)$**, for an integer $x \ge 1$, is the Elias gamma code: $\lfloor \log_2 x \rfloor$ zeros, then $x$ in
    binary, most significant bit first ($2\lfloor \log_2 x \rfloor + 1$ bits; its first bit after the zeros is 1).
  - **$\mathrm{rk}(\rho)$** is the Lehmer rank of $\rho \in \mathrm{Sym}(\{0,\dots,N-1\})$:
    $\sum_{i=0}^{N-1} d_i\,(N-1-i)!$ with $d_i = \#\{j > i : \rho(j) < \rho(i)\}$, written MSB-first in exactly
    $\lceil \log_2 N! \rceil$ bits (0 bits at $m = 0$). It is computed on the PE-01 labelling above.
  - **$a$ and $\chi$** are $N$-bit truth tables, $v = 0$ first. E is defined for prediction tests,
    $F = \mathrm{graph}(\chi)$, the only verdict-bearing tests (PE-01 §6).
  - **Components:** $\gamma(m+1)$; $\mathrm{rk}(\rho_0)$; $\mathrm{rk}(\rho_1)$; $a$: $N$; $\chi$: $N$;
    $\gamma(K+1)$.
  - **Prefix-free.** $\gamma$ is prefix-free, and once $m$ is decoded every field up to $\gamma(K+1)$ has fixed length.
    The decoder rejects ranks $\ge N!$ (EN).
  - **Lengths:** $|E| - |\gamma(K+1)| = 3, 9, 21, 53, 127$ for $m = 0,\dots,4$.
  - E is one decoder for every $m$ and $K$; it is not tuned to any observer class. It is not minimal for structured
    classes; a linear filter has a shorter class-specific code. Results under E are statements about E only.
- **Charge scope. [OWNER: O10.]** The models above charge the full description: $\rho_0, \rho_1, a$, the readout and
  the trigger constant. #934's literal wording is "its transition and action tables, or a fixed encoding of them".
  - **Reason for the full description:** an interpreter needs the readout and the trigger to run the observer.
  - **Effect:** charging the readout and trigger shrinks the admissible region, which favours the claim under audit.
    It moves $m = 1$'s onset from roughly $n \approx 10$–$13$ (transition and action only; review §3) to $n = 17$ (R)
    and $18$ (E).
  - The review recommends that the full description govern, as drafted, with the reason stated.
  - Whatever the owner decides, every witness reports its components (above), and the verdict prints both
    $F_C$ and $F_C^{\rm TA} = F_U + $ (the $\rho_0$, $\rho_1$ and $a$ components). The transition-and-action charge is
    then readable within the searched $K$ range without a re-run. The search range itself stays as §3.4 fixes it.
- **Invariance caveat.** Every charge is relative to a fixed interpreter whose own description is not charged, just as
  the generator's $\varphi$ is not charged. §5 (INT) builds that interpreter for every verdict-bearing witness:
  - the charged bits sit in a read-only program register in the visible sector;
  - the composite stays a bijection with no hidden-sector access.

### 2.2 Description-complexity proxy

**[OWNER: O3; the review recommends information only.]** As drafted, no separate description-complexity model governs
any outcome.
- **Reported for every witness, as information only:** $|E|$ of its reduced form.
  - The reduced form is the observer restricted to the memory states reachable from $v_0$, quotiented by Moore
    equivalence of its $(a, \chi)$ outputs, relabelled canonically, and padded with the identity to $2^{m'}$ states.
  - Restriction and quotient keep $\rho_0, \rho_1$ permutations: the reachable set of a permutation pair is invariant,
    and a surjection of a finite set onto itself is a bijection.
  - RF checks that the reduced form has the same exact curves and is an enumerated member at its $m'$.
- **Why information only.** All $m \le 2$ are enumerated, so for the existence question the minimum E-charge over a
  behaviour class is already attained inside the enumeration.
- **Limit.** That argument covers E only. It does not address class-specific codes. The review's arithmetic for a
  linear-filter code (`review/REVIEW.md` §3) is not yet a checked design fact in `design/`.

### 2.3 Threshold

**[OWNER: O1; the review recommends option (i).]**
- **Option (i), as drafted:** $\theta = n + 1$ under U, R and E for `G_lin`, `G_filt`, `G_clk` and `G_clkfix`.
  `G_clkfix_u` follows §1.2 and O5.
- **Option (ii):** $\theta = n + 1 + D_C(\varphi)$, with the generator's own description charged under the same model.
- **Comparison.** Any $D_C \ge 0$ makes (ii) admit a superset of what (i) admits. Option (i) is the most stringent rule
  considered, so it is the one most favourable to the claim under audit. Its hard-to-vary property comes from fixing θ
  independently of the charge, not from any defect of (ii).
- **θ-independent reporting (R6, applied whatever the owner decides):**
  - per witness, $F_U$, $F_R$ and $F_E$ with their components (§2.1) and $F_C^{\rm TA}$;
  - per cell, the minimum $F_C$ over the U-witnesses in the searched $K$ range, for each $C$.

  A reader can then apply another θ, or another charge scope, without re-running anything.

**Condition (f) restated.** For model $C \in \{U, R, E\}$: (f$_C$) $F_C(O, K) \le \theta$. (f$_U$) is PE-01's (f).

### 2.4 Drafting-time facts (not results)

These follow from the definitions alone (`design/charge_arith.py`). AR-C, M0 and INC-RE re-derive or check them at run
time, and any difference halts the stage.

| $m$ | $F_U$ | $F_R$ | $F_E$ (K = 4..6; K = 7) |
|---|---|---|---|
| 0 | $c+1$ | $2c + 4$ | 12; 14 at $c = 3$ |
| 1 | $c+2$ | $2c + 12$ | 19; 21 at $c = 3$ |
| 2 | $c+3$ | $2c + 31$ | 32; 34 at $c = 3$ |
| 3 | $c+4$ | $2c + 76$ | 65; 67 at $c = 3$ |
| 4 | $c+5$ | $2c + 181$ | 140; 142 at $c = 3$ |

- **PE-01's witness** ($m = 2$, $K = 7$): $F_U = 6$, $F_R = 37$, $F_E = 34$, against $\theta = 6$.
- **The K′ = 0 zero.** On every (a′) generator $x_0$ is uniform: under $\mu$ for `G_lin`, `G_filt`, `G_clk` and
  `G_clkfix_u`, and under $\mu^{\rm fix}$ for `G_clkfix`. So $\mathrm{adv}^{\rm pred} = 0$ at $K' = 0$ for every
  observer, and every window needs $K - 3 \ge 1$, i.e. $K \ge 4$ and $c \ge 3$. This uses only the $K' = 0$ zero, not
  $Z(\varphi)$.
- **Least $n$ with $n + 1 \ge F_C$ at $K = 4$:**

  | $m$ | R | E |
  |---|---|---|
  | 0 | 9 | 11 |
  | 1 | 17 | 18 |
  | 2 | 36 | 31 |
  | 3 | 81 | 64 |
  | 4 | 186 | 139 |

  A window may need a larger $K$, which raises these values.
- **m = 0 is identically zero on every (a′) generator (M0).**
  - An $m = 0$ observer's round ($x \leftarrow x \oplus a$, then the generator step) is a bijection of the state space.
  - Under $\mu$ uniform on the whole space (`G_lin`, `G_filt`, `G_clk`, `G_clkfix_u`) the law stays uniform, so $x_K$
    is uniform.
  - Under $\mu^{\rm fix}$, after $t$ rounds the law is uniform on $\{x \oplus q = a t \bmod 2\}$, which is balanced in
    $x$.
  - Its guess $\chi$ is a constant, so $\mathrm{adv}^{\rm pred} = 0$ at every $K$. `emb_m0_all` can never produce a
    witness on an (a′) generator.
- **E's region lies inside R's for $m \le 1$ (INC-RE).**
  - $T_E - T_R = |\gamma(K{+}1)| - c(K)$ at $m = 0$, which is $\ge 1$ for $K \ge 1$.
  - $T_E - T_R = |\gamma(K{+}1)| - c(K) - 1$ at $m = 1$, which is $\ge 0$ for $K \ge 1$.
  - So $F_E \ge F_R$, and every E-admissible witness with $m \le 1$ is R-admissible. Within PE-02's computed scope no
    E-only witness can arise. E adds an independent verdict only where it is stricter, which the per-witness $F_E$
    shows. E is shorter than $S_R$ only for $m \ge 2$, where every region in scope is empty.
- **Consequences, as facts about the accounting models:**
  - at $n \le 8$ every charged region is empty, for every observer class of PE-01 and PE-02: the cheapest case, $m = 0$
    under R, needs $2c + 4 \le 9$, so $K \le 3$;
  - for $m \ge 2$, every charged region is empty below $n = 31$ (E) or $36$ (R), beyond the reach of exact
    enumeration, and PE-02 does not compute there;
  - with M0, a charged witness in PE-02's scope can only have $m = 1$, at $n \ge 17$ (R) or $n \ge 18$ (E).
- **Reading.** An empty region is reported as a property of the accounting model, never as a measurement and never as
  "no witness found" (PE-01 §6 item 5). M0 is a proved zero with a computational check, not a search result.

## 3. Classes and scope

### 3.1 Observer classes

All observers are PE-01 §3 observers $(\rho_0, \rho_1, a, F)$ on the enlarged visible sector. They keep PE-01's round
order ($v \leftarrow \rho_x(v)$; $x \leftarrow x \oplus a(v)$; generator step), prepared memory $v_0 = 0^m$, the
clocked readout, and no hidden-sector access.

| Class | Members | Activity | Role |
|---|---|---|---|
| `emb_m0_all` (new) | $m = 0$: $a \in \{0, 1\}$ constant, every $\chi$ | active if $a = 1$ | exact-zero control (M0) |
| `emb_m1_all`, `emb_m2_all` (PE-01) | all 16 and 9216 tables, every $\chi$ | active iff $a \not\equiv 0$ | search |
| `emb_m3_passive` (PE-01) | canonical forms up to conjugacy fixing $v_0$ | passive | search (Part A) |
| `plin_m1`–`plin_m4` (PE-01) | $\rho_x(v) = Av \oplus xb$, $A \in \mathrm{GL}(m,2)$ | passive | search (Part A); `plin_m1` ⊂ `emb_m1_all` |

- **Change from PE-01: $m = 0$ is added, as a control.** It has the smallest charged footprint (§2.4), but M0 proves its
  advantage is identically 0 on every (a′) generator. It therefore enters as an exact-zero control that can fail (M0),
  not as a source of candidate witnesses. Its exclusion from the witness search follows from the proof, not from its
  effect on the claim. On the control generators `G_weak` and `G_weak_mut` its advantage is not zero, and it is the
  planted observer of PL.
- **Activity is a property of the table, not of the class name.** Factor reporting (§6) splits `emb_m*_all` into its
  active ($a \not\equiv 0$) and passive ($a \equiv 0$) members. PE-01's per-subclass cells stay as recorded.
- **Prediction tests only bear on verdicts**, as in PE-01. Distinguishing tests are not computed in PE-02.

### 3.2 The intervention-ablated observer

For $O = (\rho_0, \rho_1, a, \chi)$, $\mathrm{abl}(O) = (\rho_0, \rho_1, 0, \chi)$. As a set,
$\mathrm{abl}(\text{`emb\_m}k\text{\_all'})$ is PE-01's passive subclass of the same $m$ (checked as IA). Class-level
coverage of the ablation is therefore complete. The secondary question uses the map witness by witness (§4.3).

### 3.3 Lemma A-SIM

**[OWNER: O9; the review recommends adopting it with this revision's added step.]** The review checked the proof and
the toy cases (`review/REVIEW.md` §1). It is relied on only after the owner's decision.

**Hypothesis (one step).** The hidden component of $\varphi(x, \eta)$ does not depend on $x$. This holds for `G_lin`,
`G_filt`, `G_clkfix` and `G_clkfix_u`, and fails for `G_clk`.

**Lemma.** Under the hypothesis, for every observer $O$ with memory $m$ there is a passive observer $\mathrm{sim}(O)$
with memory $m + 1$, on the same generator, whose prediction advantage equals that of $O$ at every $K$, under both
`abs` and `signed`, for every prior on the generator state (with memory prepared at $v_0$).

*Proof.*
1. **The visible update is a flip.** Fix the hidden state $\eta$. By the hypothesis, $\varphi(0,\eta)$ and
   $\varphi(1,\eta)$ have the same hidden component, and $\varphi$ is injective, so their visible components differ.
   Hence $x \mapsto x'$ is the identity or the flip, and $x' = x \oplus b(\eta)$ for a function $b$ of the hidden state
   alone. The hidden path is then fixed by the initial state, whatever the interventions.
2. **Pathwise identity.** Let $x^{\rm p}_t$ be the visible bit without interventions and
   $A_t = \bigoplus_{s<t} a(v_{s+1})$. By step 1, $x_t = x^{\rm p}_t \oplus A_t$ pathwise.
3. **The simulator.** Define $\mathrm{sim}(O)$ on states $(v, A)$, start $(v_0, 0) = 0^{m+1}$, by
   $\rho'_{y}(v, A) = (v', A \oplus a(v'))$ with $v' = \rho_{y \oplus A}(v)$, and guess
   $\chi'(v, A) = \chi(v) \oplus A$. For each $y$ the map $\rho'_y$ is a bijection, with inverse given by
   $A = A' \oplus a(v')$ and $v = \rho^{-1}_{y \oplus A}(v')$.
4. **Induction.** Reading $x^{\rm p}_t$, $\mathrm{sim}(O)$ holds $(v_t, A_t)$ at every $t$, so
   $\{\chi'(v_K, A_K) = x^{\rm p}_K\} = \{\chi(v_K) = x_K\}$ pathwise.
5. **Reference.** Under $Q_p$ both guesses are correct with probability exactly 1/2. ∎

Consequences used by the plan:
- **PE-01's target T2.** On autonomous generators A-SIM gives the upper bound $m' \le m + 1$: activity is worth at most
  one memory bit under U. Minimality is open, and the review's toy instances show that $m' = m$ does not suffice in
  general (`review/tightness.py`). ACT-SIM (§5) checks the identity exactly, with a countercontrol and two mutants that
  must fail.
- **The clock ablation.** With the matched prior, `G_clkfix` and `G_clk` have the same passive record law (CA-EQ). An
  active $m$-bit observer on `G_clkfix` therefore has exactly the advantage of the passive $(m+1)$-bit
  $\mathrm{sim}(O)$ on `G_clk` (SIM-P1). The ablation separates backaction from the extra bit that activity carries on
  any generator.
- **The twin footprint.** Every active U-witness on an autonomous generator has a passive twin $\mathrm{sim}(O)$ with
  $F_U(\mathrm{sim}(O)) = F_U(O) + 1$. The verdict prints that value beside each such witness, so that an
  `ACTIVE_ONLY` caused by one footprint bit can be read as such (§6 item 5).

### 3.4 Generators, $n$ and $K$ per part

| Part | Generators | $n$ | Observer classes | $K$ range | Models |
|---|---|---|---|---|---|
| A: PE-01 range | `G_lin`, `G_filt`, `G_clk` (PE-01 data, read-only); `G_clkfix`, `G_clkfix_u` (new) | 3..8 | New generators: every class of §3.1, with `emb_m3_passive` under PE-01's A1 caps at $n = 7, 8$. PE-01 generators: `emb_m0_all` only (M0). | $1 \le K \le K_{\rm cx}(\varphi)$ | U computed; R and E structurally empty (§2.4) |
| A-pop: secondary population | `G_clk`, with the ablations of §4.3 | 3..8 | every member of `emb_m1_all`, `emb_m2_all` (for UX); the active ones form the population | $1 \le K \le K_{\rm cx}(\varphi)$ | U |
| B: charged sweep | `G_lin`, `G_filt`, `G_clk`, `G_clkfix`, `G_clkfix_u` | 9..$N_{\max}$ | search: `emb_m1_all` (passive members included; `plin_m1` is a subset). Control: `emb_m0_all` (M0), $1 \le K \le 63$ | search: $4 \le K \le \min(K_{\rm cx}(\varphi), K^{R}_{\max}(n, 1))$ | U, R, E on the same cells |
| C: controls | §5 | as stated | as stated | as stated | as stated |

- **The Part B search starts at $K = 4$,** from the $K' = 0$ zero alone (§2.4). $Z(\varphi)$ never bounds the search;
  it serves only the ZC cross-check (§4.2). The search's coverage therefore does not depend on how Z is computed.
- **$K^{C}_{\max}(n, m)$** is the largest $K$ with $F_C \le n + 1$. The search uses $K^{R}_{\max}$, which by INC-RE
  contains $K^{E}_{\max}$. U is evaluated on the same cells, so every U value in Part B is labelled "uncharged, within
  the charged search range". At $n$ where $K^{R}_{\max}(n,1) < 4$ ($n \le 16$), the $m = 1$ cells are `REGION_EMPTY`.
- **$N_{\max}$. [OWNER: O4; the review recommends 24.]** From §2.4, $m = 1$ cannot be admissible under either charged
  model below $n = 17$. Per-$n$ values for every candidate $N_{\max} \le 24$ are in the parameters block (§9).
- **No extension.** $N_{\max}$, every $K$ range of this table and every cap of §9 are fixed by the amendment that
  resolves §9, before any code. They are never extended or narrowed after any result is seen. A change needs a further
  amendment, committed before the run it governs, and is reported with its reason.
- **Coverage within the enumeration.** In Part B, every observer of every PE-01 class that can meet (f$_R$) or (f$_E$) at
  $n \le N_{\max}$ is enumerated or covered by a proved zero:
  - $m \ge 2$ is structurally empty (§2.4);
  - $m = 0$ is zero by M0;
  - $m = 1$ is enumerated in full.

  No observer is excluded for any other reason.
- **K0.** **[OWNER: O6; the review recommends not computing it at $n > 8$.]** As drafted, family status is reported as
  in PE-01 at $n \le 8$, including for $\mathfrak{F}_{\rm clkfix}(n)$, and not computed at $n > 8$. It bears on no
  outcome.
- **Not run in PE-02:** PE-01's unrestricted class and classes B1–B4, distinguishing tests, $r > 1$ runs and
  class-$\mathcal{Q}$ references.

## 4. Advantage, witnesses and the secondary population

### 4.1 Advantage

As PE-01 §2:
- prediction tests, against the reference $Q$ with independent fair visible outputs under the same policy;
- $\mathrm{adv}^{\rm pred}_O(\varphi, K') = |\Pr[\chi(v_{K'}) = X_{K'}] - 1/2|$ (`abs`, governing, PE-01 A2 D-SIGN);
- the signed form as a sensitivity analysis on the same data.

Counts are exact integers over the prior's support, and every advantage is an exact rational.

### 4.2 Witness conditions

PE-01's conditions (a)–(f) stand, except as stated here, each with its reason.

- **(a′)** $\varphi \in \{$`G_lin`$(p_n)$, `G_filt`$(p_n)$, `G_clk`$(p_n)$, `G_clkfix`$(p_n)$, `G_clkfix_u`$(p_n)\}$,
  with $3 \le n \le 8$ in Part A and $9 \le n \le N_{\max}$ in Part B, passing EX6 under its own prior.
  - *Change:* $n$ beyond 8, because every charged region is empty at $n \le 8$ (§2.4). The two ablated generators are
    admitted because a witness on them must count, not be excluded as a comparator.
  - The fixed-generator reading of PE-01 A2 WIT-A is kept: other family members enter only through K0 status.
- **(b′)** $O$ is a member of a §3.1 search class, given as explicit tables with its readout clock. It passes EX1, EX7,
  EX8 and IM3 on the clocked composite, and, for a witness under R or E, INT on the interpreted composite (§5).
- **(c)** $K \le K_{\rm cx}(\varphi) = \lfloor \ell_{\rm med}(\varphi)/2 \rfloor$, with the median orbit length taken
  under the generator's own prior. Unchanged except for that clause, which `G_clkfix` and `G_weak` need.
- **(d)** Unchanged: the same $O$ and $\chi$ give $\mathrm{adv}^{\rm pred} \ge \delta_{\rm cx} = 1/8$ exactly at every
  $K' \in [K - 3, K]$, $K \ge 3$. `abs` governs and `signed` is the sensitivity analysis.
- **(e)** Every PE-02 checkpoint (§5) is green.
- **(f$_C$)** $F_C(O,K) \le \theta$, for the model $C$ under which the witness is stated (§2.3).

A witness meeting (a′)–(e) and (f$_C$) is **admissible under C**.
- Under U it refutes the universal form PE-01 refuted. That is a restatement and is recorded only.
- Under R or E it refutes a stronger statement: every embedded observer whose memory, clock, output and charged
  description fit in θ is unable to predict, for every finite reversible realization.

**The zero argument, generalized and restricted.**
- **Definition.** $Z(\varphi)$ is the largest $k$ such that, for every control sequence $c_{0:k-1}$ and every value of
  $x_0$ in the prior's support, the first $k$ increments are jointly uniform under the conditional prior of the hidden
  state given $x_0$.
- **Statement.** $\mathrm{adv}^{\rm pred} = 0$ for every observer at every $1 \le K' \le Z$.
  - PE-01's proof (§7) goes through conditionally on $x_0$: $X_{K'} = c_{K'-1} \oplus Y_{K'-1}$, the guess is a function
    of $x_0$ and $Y_{0:K'-2}$, and $Y_{K'-1}$ is uniform given those.
  - At $K' = 0$ the advantage is 0 iff $x_0$ is uniform. That holds on every (a′) generator (§2.4) and fails on
    `G_weak` and `G_weak_mut`.
  - *Change from PE-01:* PE-01 assumed the hidden state independent of $x_0$, which fails for `G_clkfix`
    ($q_0 = x_0$) and for the control generators. The conditional form reduces to PE-01's where that independence
    holds.
- **Use.** Z is a cross-check (ZC) and an input to the AR-C region tables. It bounds no search range (§3.4).
- **Methods, fixed now:**
  - **`G_lin`, `G_clk`.** For each fixed control sequence the hidden step is $\mathbb{F}_2$-linear, so joint uniformity
    is equivalent to $\mathbb{F}_2$-rank $k$ of the increments' linear forms, over all $2^k$ sequences. At
    $n \le 12$ an exhaustive enumeration over all control sequences and hidden states must agree.
  - **`G_filt`.** $\sigma_0 = \sigma_1$, so every control sequence gives the same increments. Joint uniformity is
    decided by enumerating all $h \in \mathbb{F}_2^n$ ($2^n$ states, $n \le 24$).
  - **`G_clkfix`, `G_clkfix_u`.** The hidden pair is autonomous, so the control sequence is irrelevant. The increments
    are not affine in $h$ (review T6), and the rank method does not apply. Joint uniformity given $x_0$ is decided by
    enumerating the hidden states in the conditional prior's support: $(h, q_0 = x_0)$ for the matched prior, and
    $(h, q_0)$ for the uniform prior.
  - **Bound, also checked.** $Z(\texttt{G\_clkfix}) \ge Z(\texttt{G\_clk})$ and
    $Z(\texttt{G\_clkfix\_u}) \ge Z(\texttt{G\_clk})$. *Proof:* given $x_0$ (and $q_0$), the clock $q_t$ is
    $q_0 \oplus Y_0 \oplus \dots \oplus Y_{t-1}$, a function of earlier increments. So
    $\Pr[Y_{0:k-1} = z \mid x_0, q_0]$ equals the probability, under uniform $h$, that `G_clk`'s increments equal $z$
    for the fixed control sequence $c_t = q_0 \oplus z_0 \oplus \dots \oplus z_{t-1}$. That is $2^{-k}$ for
    $k \le Z(\texttt{G\_clk})$. Averaging over $q_0$ gives the uniform-prior case.

### 4.3 The secondary population and its comparisons

**[OWNER: O7; the review recommends all members.]**
- **Population.** $W_{\rm act}$ is every triple $(O, \chi, K)$ with $O$ active ($a \not\equiv 0$), $m \le 2$, on
  `G_clk`$(p_n)$, $n = 3,\dots,8$, meeting (a′)–(e). Condition (f) is not required for membership; each member records
  whether it meets (f$_U$).
- **What PE-01's retained data already fix,** stated in advance from the `windows` entries of `results/shards/n*-clk*.json`
  for $K \le K_{\rm cx}$. UX confirms each of these against PE-02's own computation.
  - `emb_m1_all` has no window on `G_clk` at any $n$; $m = 0$ is zero (M0).
  - Active `emb_m2_all` windows exist only at $n = 4$ ($K = 7, 8, 9$; $K_{\rm cx} = 9$) and at $n = 5$ ($K = 7, 10$;
    $K_{\rm cx} = 20$). So $W_{\rm act}$ is $m = 2$ at $n \in \{4, 5\}$ only.
  - `emb_m2_passive` has no window on `G_clk` at any $n$. Since $\mathrm{abl}(O)$ is a passive $m = 2$ observer, every
    member of $W_{\rm act}$ is `INTERVENTION_NEEDED`. That label restates PE-01 and is recorded only (§6 item 10).
  - **Not fixed:** `BACKACTION_NEEDED`. By A-SIM and CA-EQ, $O$ on `G_clkfix` has the window iff the passive $m = 3$
    observer $\mathrm{sim}(O)$ has it on `G_clk`. PE-01 records passive $m = 3$ windows there ($n = 4$: $K = 7$–$9$;
    $n = 5$: $K = 7$–$20$), so the outcome is open.
- **Per member, three exact curves over the window $[K-3, K]$:**
  - $O$ on `G_clk` (the witness itself);
  - $\mathrm{abl}(O)$ on `G_clk`;
  - $O$ on `G_clkfix`, and on `G_clkfix_u` if O5 retains it.
- **Per-member labels:**
  - `INTERVENTION_NEEDED` if $\mathrm{abl}(O)$ fails (d) at $K$; otherwise `INTERVENTION_NOT_NEEDED`;
  - `BACKACTION_NEEDED` if $O$ on `G_clkfix` fails (d) at $K$; otherwise `BACKACTION_NOT_NEEDED`.
- **Twin footprint.** Each member prints $F_U(O)$ and $F_U(\mathrm{sim}(O)) = F_U(O) + 1$.
- **Class level,** per $(n, m)$: whether any active observer has a window meeting (a′)–(e) on `G_clkfix`, given that
  one does on `G_clk`.
- **What is reported:** the four-way table of counts (exact integers) per $(n, m, K)$ cell, never pooled across cells.
- **The generated sentence,** printed for an $(n, m, K)$ cell only when every member there is `BACKACTION_NEEDED` and no
  active window exists on `G_clkfix` at that $(n, m, K)$:
  "On `G_clk`$(p_n)$ at $(n, m, K)$, every active window is lost when the clock is made unresponsive (`G_clkfix`,
  matched prior)." Otherwise the counts are printed without it. No broader sentence about the advantage being "tied to"
  the clock is generated.

## 5. Controls and the invariant→checkpoint table (§A.41)

Every numerical row is exact integer or `Fraction` arithmetic. A failed or unevaluated row makes the stage VOID (§6).

**Structured evidence (§A.44).**
- **Files.** Each shard writes `results/shards/<id>.json` in schema `pe02-shard/1`, with these top-level keys:
  - `schema`, `shard`, `mode`, `commit`, `tree`, `recipe`, `params` (the §9 block with its amendment's blob and commit);
  - `controls`: a map from checkpoint id to `{pass: bool, checks: int, failures: [..]}`;
  - `cells`: a list of `{generator, n, subclass, model, theta, K_range, status, min_F: {U, R, E}, witnesses: [..]}`;
  - each witness: `{tables, chi, K, window, adv: [str], signed: [str], F_U, F_R, F_E, components: {R: {..}, E: {..}},
    F_TA: {R, E}, conditions: {a, b, c, d, e, f_U, f_R, f_E: bool}, reduced_E, twin_F_U}`.
  
  `<id>.provenance.json` holds the run id and timings and is not part of the replay. `collect` writes
  `measurements.json` (`pe02-measurements/1`); `verdict.py` writes `verdict.json` (`pe02-verdict/1`) and
  `verdict.txt`. The field lists may be completed by amendment before code, and not after.
- **Exit statuses.** These come from the host, not from files a process writes about itself.
  - Each check runs as its own workflow step, and its exit status is the step's conclusion.
  - A fact visible only in printed output is turned into a marker step, whose `if:` condition is part of the frozen
    workflow and whose name states the fact.
  - The collect job fetches the run's job and step records (identity and conclusion) from the host API into
    `host_conclusions.json`.
  - `verdict.py` reads only the shard files, `measurements.json` and `host_conclusions.json`, never log text.

**The four controls #934 requires, each able to fail:**

1. **RP-01 (PE-01 witness, uncharged, byte-identical replay).**
   - **Where:** at PE-01's run head `549641460b8ddb536178f95fac2ec9390e84a987`, in a detached checkout with history
     back to `af38dc2d`, under PE-01's pinned environment (Python 3.12, numpy 2.2.6, as in
     `.github/workflows/pe01-bounded-tests.yml`).
   - **Command:**
     `python3 -I -B .../pe01_bounded_tests_v1/run.py replay n5-clk --mode result --against <PE-01 results/shards> --out <dir>`.
   - **Pass:** the step concludes success (exit 0), and the new `n5-clk.json` has sha256
     `3f6121e83e75ed7ed5d43817bb8fc63dc73ad5fbf7acd763c3261e11d972a963`, equal to `results/shards/n5-clk.json`.
   - The witness record in it (observer 2361, χ 0, K = 7, `adv_pred` 1/8, 5/32, 5/32, 1/8, footprint 6,
     `table_size_bits` 31, window counts 36 and 12) is the object R, E and §4.3 act on.
   - **Also:** PE-01's `verdict.py` regenerates `verdict.json` and `verdict.txt` byte-identically from
     `measurements.json` (sha256 `f17109f10379d648fcb055c2a1868666205fae8499b35ca65ecedae7a41f067a`).
2. **CH-IFF (charged rejection iff charged footprint > θ, relative to the record's other conditions).** The
   admissibility classifier runs for R and E. For each record it computes the failed-condition set independently, from
   the record's fields and its recomputed $F_C$ (TR, EN).
   - **(1) Records meeting (a′)–(e) and (f$_U$):** admit iff $F_C \le \theta$, and every refusal's condition set is
     exactly $\{$(f$_C$)$\}$.
   - **(2) Every other record:** the refusal's condition set equals the independently computed set of failed
     conditions, and contains (f$_C$) iff $F_C > \theta$.
   - **Inputs:**
     - every witness record in PE-01's 38 shards (271 records; only the reported witness falls under (1));
     - the planted witness of control 3;
     - eight synthetic boundary records, with conditions (a′)–(e) and (f$_U$) set true, $K = 7$:

       | $m$ | C | $F_C$ | record at $F_C = \theta$ | record at $F_C = \theta + 1$ |
       |---|---|---|---|---|
       | 0 | R | 10 | $n = 9$ | $n = 8$ |
       | 0 | E | 14 | $n = 13$ | $n = 12$ |
       | 1 | R | 18 | $n = 17$ | $n = 16$ |
       | 1 | E | 21 | $n = 20$ | $n = 19$ |

       Each must be admitted at $F_C = \theta$ and refused at $\theta + 1$ with condition set $\{$(f$_C$)$\}$. They test
       the classifier only: they are not generator states and enter no outcome.
3. **PL (planted passive witness on a weak generator).** The production sweep, unchanged, on `G_weak(13)`, with classes
   `emb_m0_all` and `emb_m1_all` and $1 \le K \le 15$.
   - It must report the passive $m = 0$ observer with $a = 0$, $\chi \equiv 0$ as meeting (b′)–(e) and (f$_C$) under U,
     R and E at $K = 7$, window $[4,7]$, with $\Pr[\chi = X_{K'}] - 1/2 = 1/2 - K'/2^{13}$ exactly.
   - Condition (a′) is replaced by membership in the control set, and the record is labelled a control, never a
     witness.
   - On `G_weak_mut(13)` every observer must give advantage exactly 0 at every $1 \le K \le 13$, and no window with
     $K \le 16$ may be reported. $K = 0$ is excluded (§1.3).
4. **MUT-NC (mutant that drops the charge).** The full classifier runs with $T_C \equiv 0$.
   - Its R and E outputs must equal the U outputs byte for byte after the model label is normalized.
   - The real R and E outputs must differ from the mutant's on PE-01's witness (mutant admits, real refuses) and on
     every U-admissible witness with $F_C > \theta$.
   - If the real charged outputs equal the mutant's, the charge is inert and the stage is VOID.

| Invariant | Checkpoint | Measured by |
|---|---|---|
| PE-01's witness and verdict are reproduced exactly, in PE-01's environment | RP-01 | control 1: the step conclusion, the sha256 of the replayed shard, the verdict regeneration; the job pins Python 3.12 and numpy 2.2.6, and the shard records `sys.version` and `numpy.__version__`, which must match |
| PE-02's own code agrees with PE-01 where both compute | UX | For `G_clk`, $n = 3..8$, $K \le K_{\rm cx}$, under both `abs` and `signed`: PE-02's window counts for the full subclasses `emb_m1_all` and `emb_m2_all` (active plus passive), and for `emb_m1_passive` and `emb_m2_passive`, equal PE-01's `windows[subclass]` entries K by K. The witness curve equals RP-01's. The §4.3 statements about PE-01's data are confirmed or the stage halts |
| Admissibility under C holds iff $F_C \le \theta$, given the other conditions | CH-IFF | control 2 |
| A planted passive witness is found, and its mutant gives none | PL | control 3 |
| The charge is not inert | MUT-NC | control 4 |
| $T_R$ is measured, not reprinted | TR | the bit length of $S_R$ equals the §2.1 formula, component by component, for every enumerated observer; for every PE-01 witness record it equals the recorded `table_size_bits` |
| E is the stated code and is prefix-free | EN | For every observer with $m \le 2$, every $\chi$ and every $K \le 63$: decode(encode) is the identity, the length equals the §2.1 formula component by component, and no codeword in that set is a prefix of another. $\gamma$ alone is checked for every $x \le 2^{20}$, MSB-first. At $m = 3, 4$ the same checks run on every observer that appears in any record |
| E-admissible implies R-admissible for $m \le 1$ | INC-RE | $F_E \ge F_R$ for every $m \le 1$ observer and every $K \le 2^{20}$ by formula, and for every computed record; no cell has an E-witness without an R-witness at the same $(n, m, K)$ |
| m = 0 is identically zero on (a′) generators | M0 | `emb_m0_all`, both actions and both guesses: advantage exactly 0 at every $1 \le K \le K_{\rm cx}$ for $n \le 8$, and at every $1 \le K \le 63$ for each Part B $n$, on every (a′) generator. On `G_weak(13)` the planted value of PL must appear, so M0 is not vacuous |
| The reduced form is behaviourally equivalent and enumerated | RF | for every witness, the reduced form's exact curves equal the observer's at every $K$ computed, and its tables are a member of the enumerated class at its $m'$ |
| The zero argument holds as computed | ZC | For every computed observer and generator: advantage exactly 0 at every $1 \le K' \le Z(\varphi)$, and at $K' = 0$ where $x_0$ is uniform. The hypotheses are checked: Z's definition is evaluated by the §4.2 method, rank and exhaustive agree at $n \le 12$, and $Z(\texttt{G\_clkfix}), Z(\texttt{G\_clkfix\_u}) \ge Z(\texttt{G\_clk})$ |
| The charge is physical: the program sits in a read-only visible register | INT | For each verdict-bearing R or E witness, and for PE-01's witness as calibration, on the interpreted composite with a program register of width $T_C$: it is a bijection on each program slice (EX1); the register, $h$ and $q$ are untouched by the observer maps, and $\varphi$ is the identity on the observer registers (EX8); its record law and prediction curve equal those of the tables-in-dynamics composite (IM3-C); its visible width less the system bit equals $F_C$ (FP-C). For $m \le 1$ every valid program is checked |
| Every map is a bijection | EX1 | as PE-01, for every generator including `G_clkfix`, `G_clkfix_u`, `G_weak` and `G_weak_mut`, at every $n$ used |
| Priors and laws sum to 1 | EX2 | exact sums |
| No float on the verdict path | EX3 | type assertion on every verdict input |
| $p_n$ and $p'_n$ follow §1.1 and are primitive | EX4 | the least-primitive rule is recomputed; it must reproduce PE-01's $p_n$ and $p'_n$ for $n = 3..8$ and equal §1.1's table for $n = 9..24$; the order of $z$ is $2^n - 1$ |
| $(\ell, L_p)$ is observable | EX5 | $\mathbb{F}_2$ rank $n$, every $n$ |
| T-level (C1) holds for every (a′) generator | EX6 | exact one-step visible matrix under the generator's own prior |
| Settings are measurement-independent | EX7 | the joint prior is the generator's prior $\otimes\,\delta_{v_0}$, and EX8 holds |
| No hidden-sector access | EX8 | as PE-01, with $q$ part of the hidden sector |
| The embedded simulation is correct | IM3 | aggregated and full-state simulations agree for all observers at $n \le 4$ on every generator, and for every verdict-bearing witness |
| The $Q_p$ side is correct | IM6 | `G_tape(K)` gives $P_p = Q_p$ exactly for every observer of `emb_m0_all`, `emb_m1_all` and `emb_m2_all` at $K \le 12$ |
| The clock ablation does what it says | CA-STRUCT | the hidden step of `G_clkfix` is the same for $x = 0$ and $x = 1$ on every state, and that of `G_clk` differs on some state. Self-test: substituting `G_clk` for `G_clkfix` must fail |
| The ablation changes only responsiveness | CA-EQ | for every $n$ used, every seed of $\mu^{\rm fix}$ and every $K \le K_{\rm cx}$, the passive record of `G_clkfix` equals that of `G_clk` from the same $(x_0, h_0)$ |
| The intervention ablation is the stated map | IA | $\mathrm{abl}(O)$ has $a \equiv 0$ and the same $\rho_0, \rho_1, \chi$; the image of each `emb_mk_all` equals PE-01's passive subclass as a set. Self-test: the identity map in place of abl must fail |
| Lemma A-SIM holds as computed, and the check is not vacuous | ACT-SIM | **Identity:** on `G_lin`, `G_filt`, `G_clkfix` and `G_clkfix_u`, for every active observer with $m \le 1$ at every $n$ used, and with $m = 2$ at $n \le 6$, the exact curve of $O$ equals that of $\mathrm{sim}(O)$, computed through the passive code path, at every $K \le K_{\rm cx}$. **Non-vacuity, required:** (i) on `G_clk` ($n = 3, 4$; $m \le 1$; $K \le 9$) the identity must fail for at least one observer; (ii) mutant sim with $\chi'$ lacking $\oplus A$ (on `G_lin`) and (iii) mutant sim with $\rho'$ lacking the $A$-correction (on `G_filt`), same ranges, must each fail for at least one observer |
| The ablation's prediction through the lemma | SIM-P1 | Every active $m$-bit window on `G_clkfix` at $(n, K)$ is a window of the passive $(m+1)$-bit $\mathrm{sim}(O)$ on `G_clk`, computed. Where $m + 1 \le 3$ and the cell is in PE-01's computed range, PE-01 must record a passive $(m+1)$ window there (`emb_m2_passive` for $m = 1$; `emb_m3_passive` for $m = 2$) |
| PC zero and firing | PC | as PE-01 §4 for the embedded search classes; the zero at $1 \le K \le n$ on `G_lin(p_n)` at every Part B $n$ |
| Complement symmetry | SY | as PE-01 for the flip-commuting generators; `G_clk`, `G_clkfix` and `G_clkfix_u` are exempt |
| Inclusions | MO | as PE-01, plus: every R- or E-admissible witness is U-admissible ($F_C \ge F_U$) |
| Footprints are measured | FP | as PE-01, on the clocked composite, for U; FP-C under INT for R and E |
| The witness conditions are evaluated mechanically | CX | As PE-01 §5 CX, with (f) evaluated per model. Self-test mutants, each refused on its own condition: a window value $1/8 - 2^{-K-2}$ (d); $F_U = \theta + 1$ (f$_U$); $F_R = \theta + 1$ with $F_U \le \theta$ (f$_R$); $F_E = \theta + 1$ with $F_U \le \theta$ (f$_E$); $K = K_{\rm cx} + 1$ (c) |
| The admissible regions are derived | AR-C | $Z(\varphi)$ by the §4.2 methods, and $K_{\rm cx}(\varphi)$, for every generator and $n$ used. The regions under U, R and E (both θ values for `G_clkfix_u`) are recomputed from them and from the measured footprints, and must equal §2.4's drafting values and the §9 per-$n$ values where those apply |
| The workflow cannot be launched by a push | WF | the workflow file is parsed, and its `on:` key has `workflow_dispatch` as its only trigger |
| Deterministic replay | RP | every PE-02 shard's measurement JSON is byte-identical on rerun |
| The plan precedes the code | PIN | the measurement JSON records this file's blob and the commit that froze it, and that commit is an ancestor of every code commit |
| Runs wait for the fixed parameters | TH | The measurement JSON records the `pe02-parameters` block of the amendment that resolves §9, with its blob and commit. Each formula is evaluated at every $n$ that has an explicit value and compared with it, as PE-01 A1. A run refuses to start without the block, on any `OPEN` value, or on any disagreement |
| Verdicts are generated from measurements | VG | As PE-01: the regeneration is byte-identical; a copy with any control flag flipped yields VOID; a verdict lacking the §7 resource-model sentence fails. The verdict's inputs are exactly the files named under "Structured evidence" |

## 6. Decision rule and outcome classes (fixed before computation)

1. **VOID** takes precedence. Any failed or unevaluated checkpoint voids the stage, the verdict names it, and nothing
   else is printed as a verdict. Controls run first.
2. **Generated text.** `verdict.py` writes the verdict from the files named in §5 alone; every number in it is read
   from them.
3. **Cell status,** per (generator, $n$, subclass, model, and θ where §1.2 gives two):
   - `WITNESS`: some $(O, \chi, K)$ in the cell meets (a′)–(e) and (f$_C$);
   - `NONE`: the cell's region is non-empty, every $K$ in it was computed, and none meets them;
   - `REGION_EMPTY`: AR-C finds the region empty. This is a property of the accounting model, not a search result;
   - `NOT_RUN` or `INCOMPLETE` (completed cells kept, as PE-01 A1): no verdict.

   Cells are never pooled for attribution. Resource attribution follows PE-01 §6 item 4 within each cell and model.
   Each cell prints its minimum $F_U$, $F_R$ and $F_E$ over U-witnesses (§2.3).
4. **Factor outcome, per $n$.** For each $n$, activity $\alpha$, generator $\gamma$ and charged model $C \in \{R, E\}$,
   reported separately for each $C$. Let $\mathrm{wit}_n(\alpha, \gamma, M)$ mean that some cell at that $n$, activity,
   generator and model $M$ is `WITNESS`.
   - `SURVIVES_CHARGED[C]`: $\mathrm{wit}_n(\alpha, \gamma, C)$.
   - `UNCHARGED_ONLY[C]`: not $\mathrm{wit}_n(\alpha, \gamma, C)$, and $\mathrm{wit}_n(\alpha, \gamma, U)$, and no
     $C$-cell at $n$ is `NOT_RUN` or `INCOMPLETE`. It carries the sub-label `structural` if every $C$-cell at $n$ is
     `REGION_EMPTY`, and `searched` otherwise.
   - `NO_WITNESS_IN_SCOPE`: neither $\mathrm{wit}_n(\alpha, \gamma, U)$ nor $\mathrm{wit}_n(\alpha, \gamma, C)$, and no
     cell of either model at $n$ is `NOT_RUN` or `INCOMPLETE`.
   - `INCOMPLETE` otherwise: no factor verdict.

   Constraints and scope:
   - The U-witnesses compared are those at the same $n$ and, in Part B, in the same $K$ range as the $C$-cells. No
     U-witness at one $n$ is set against a $C$-cell at another.
   - A summary across $n$ is printed only as the list of per-$n$ labels, each with the $n$ and $K$ ranges on which U
     and C were searched.
   - Since every $C$-witness is a U-witness (MO), `SURVIVES_CHARGED` without a U-witness at the same $n$ voids the
     stage. By INC-RE, `SURVIVES_CHARGED[E]` without `SURVIVES_CHARGED[R]` at the same $n$ also voids the stage.
5. **Activity contrast,** per ($n$, generator $\gamma$, model $M \in \{U, R, E\}$):
   - `ACTIVE_ONLY`: $\mathrm{wit}_n(\text{active}, \gamma, M)$ and not $\mathrm{wit}_n(\text{passive}, \gamma, M)$, with
     every passive cell at $n$ complete;
   - `PASSIVE_ALSO`: both;
   - `PASSIVE_ONLY`: passive only;
   - `NEITHER`: neither, every cell at $n$ complete;
   - `INCOMPLETE` otherwise.

   On an autonomous generator, every `ACTIVE_ONLY` prints each active witness's $F_U$, its twin's
   $F_U(\mathrm{sim}(O))$, and whether $\mathrm{sim}(O)$ meets (f$_M$) (§3.3).
6. **Factor scope.** Each factor outcome prints the cells it rests on: $n$, subclasses, $K$ ranges, which cells are
   `REGION_EMPTY`, and, for Part A generators carried from PE-01, that their U cells are PE-01's frozen results.
7. **Secondary question.** Reported as §4.3 fixes, per cell, with the generated sentence only under the stated
   condition. Labels that §4.3 marks as fixed by PE-01's data are printed "restates PE-01".
8. **Classification of each statement:**
   - PROVED (exhaustive finite, with the scope printed);
   - PROVED (with a reviewed written proof; Lemma A-SIM, M0, INC-RE and the Z bound are the candidates);
   - CONDITIONAL (with the hypothesis named);
   - OPEN.

   Verification layers stay distinct (§8).
9. **Favourable readings** for the claim under audit are `UNCHARGED_ONLY`, `NO_WITNESS_IN_SCOPE` and
   `BACKACTION_NEEDED`.
   - Each is printed with its enumerated scope and not extended beyond it.
   - `UNCHARGED_ONLY[structural]` and M0 zeros are printed as properties of the accounting model or as proved zeros,
     never as measurements.
   - Choices that lean the same way are printed beside the outcome they affect: θ option (i), the charge scope (O10),
     and the fixed clock charge.
10. **Productivity test (§A.31), fixed now.** PE-01's REPORT already states that charging the 31 table bits would put
    its witness outside θ. A PE-02 result is a candidate gem only if it is strictly stronger than that sentence, and it
    either constrains `book/ch18-beyond.md:114` as scoped on `main` or exposes a hidden assumption.
    - Recorded only, because they restate PE-01 or the definitions: `UNCHARGED_ONLY[structural]`, the arithmetic of
      §2.4, M0, INC-RE, and the `INTERVENTION_NEEDED` labels.

## 7. Scope and non-claims

- No statement about the actual world's hidden sector, nor about the $10^{-32}$ statement (`ch18-beyond.md:56–58`).
- No cryptographic, circuit-security or distinguishing claim.
- A negative result covers only the enumerated class, generators, $n$, $K$, accounting model and charge scope.
- No PE-02 outcome establishes the narrower claim the scoped ch18 sentence leaves open, about observers of bounded
  memory that only read the source. A charged witness, its absence and the ablation counts are each stated for their
  class only.
- Results under E are about E; no result is stated as one about description complexity.
- The realization conditions stay "T-level (C1) holds; C2–C4 not checked" for every generator.
- **Resource-model sentence,** repeated in the generated verdict: "Admissibility under R and E is a consequence of the
  selected accounting model: memory + clock + output + charged description ≤ θ, relative to a fixed uncharged
  interpreter. It is not a limit OI imposes on observers."
- No manuscript change, dispatch, theorem designation or merge happens without separate owner approval. A finding
  bearing on `ch18-beyond.md:114`, or on its mirror `The-Incompleteness-of-Observation-FULL.md:4932`, is reported here
  only.

## 8. Verification layer

Exact enumeration of the joint state with integer counts and `Fraction` advantages, as PE-01. Numpy is used on integer
arrays only.

Lemma A-SIM, M0, INC-RE and the Z bound are written proofs with computational regressions (ACT-SIM, M0, INC-RE, ZC).
The computation does not stand in for the proof, and the proof does not stand in for the computation of any cell.

## 9. Owner decisions before freeze, and the parameters block

Each decision is fixed by an amendment in `amendments/`, before any code, and carried into the `pe02-parameters` block
that TH reads. No value may stay `OPEN` at run time.

| Id | Decision | Options | Review's recommendation |
|---|---|---|---|
| O1 | θ under charged models | (i) $n+1$ for U, R, E; (ii) $n+1+D_C(\varphi)$ (a superset of (i)) | (i), as the most stringent rule; F_C components and per-cell minima reported (R6) |
| O2 | Which charged models govern | R and E, each reported separately; R only; E only | both, with INC-RE stated (in scope, E ⊆ R) |
| O3 | Description-complexity proxy | information only (§2.2); a third governing model | information only, plus the class-code arithmetic as a checked design fact |
| O4 | $N_{\max}$ | 8 (no charged computation); 22; 24 | 24, with the §3.4 no-extension clause; optionally drop m = 0 beyond M0 (done in revision 2) |
| O5 | Clock-ablated prior, and θ for `G_clkfix_u` | matched primary with uniform variant; matched only; uniform only. θ for `_u`: n+2 or n+1 | matched primary with uniform variant; θ for `_u` = n+2 governing, n+1 also reported |
| O6 | K0 status at $n > 8$ | not computed; computed on a fixed subfamily | not computed |
| O7 | Secondary population | all active (a′)–(e) members; admissible (f$_U$) only | all, with the known extent stated in advance (§4.3) |
| O8 | Stage name | keep "PE-02"; rename (e.g. PE-04) and retitle #934 before freeze | rename to PE-04 |
| O9 | Lemma A-SIM | adopt for ACT-SIM, SIM-P1 and interpretation; drop | adopt, with the R12 step and "upper bound" wording |
| O10 | Charge scope | full description (ρ, a, readout, K) governs; transition and action tables only govern | full description governs, with the reason stated and per-witness components |

Draft block. `OPEN` values are owner placeholders; the per-$n$ values are computed from the formulas by
`design/charge_arith.py` and are re-derived by TH, which refuses on any disagreement.

```json pe02-parameters
{
  "amendment": "OPEN",
  "decisions": {
    "O1_theta_rule": "OPEN (review: i)",
    "O2_models": "OPEN (review: R and E, separately)",
    "O3_proxy": "OPEN (review: information only)",
    "O4_N_max": "OPEN (review: 24)",
    "O5_clkfix_priors": "OPEN (review: matched primary, uniform variant)",
    "O5_theta_clkfix_u": "OPEN (review: n+2 governing, n+1 reported)",
    "O6_K0_beyond_8": "OPEN (review: not computed)",
    "O7_secondary_population": "OPEN (review: all members)",
    "O8_stage_name": "OPEN (review: rename to PE-04)",
    "O9_lemma_A_SIM": "OPEN (review: adopt)",
    "O10_charge_scope": "OPEN (review: full description)"
  },
  "theta": {
    "G_lin": "n+1", "G_filt": "n+1", "G_clk": "n+1", "G_clkfix": "n+1",
    "G_clkfix_u": ["n+1", "n+2"],
    "G_weak": "n+1", "G_weak_mut": "n+1"
  },
  "theta_by_n": {"3": 4, "4": 5, "5": 6, "6": 7, "7": 8, "8": 9, "9": 10, "10": 11, "11": 12, "12": 13,
                 "13": 14, "14": 15, "15": 16, "16": 17, "17": 18, "18": 19, "19": 20, "20": 21, "21": 22,
                 "22": 23, "23": 24, "24": 25},
  "partB_K_min": 4,
  "K_R_max_m1": "max K with 2*ceil(log2(K+1)) + 12 <= n+1",
  "K_R_max_m1_by_n": {"9": null, "10": null, "11": null, "12": null, "13": 1, "14": 1, "15": 3, "16": 3,
                      "17": 7, "18": 7, "19": 15, "20": 15, "21": 31, "22": 31, "23": 63, "24": 63},
  "K_E_max_m1": "max K with ceil(log2(K+1)) + 2 + 9 + |gamma(K+1)| <= n+1",
  "K_E_max_m1_by_n": {"9": null, "10": null, "11": null, "12": null, "13": null, "14": 1, "15": 2, "16": 2,
                      "17": 3, "18": 6, "19": 6, "20": 7, "21": 14, "22": 14, "23": 15, "24": 30},
  "M0_K_max_partB": 63,
  "partA_K_max": "K_cx(phi)",
  "m3_passive_K_cap": {"7": 15, "8": 31},
  "secondary_n": [3, 4, 5, 6, 7, 8],
  "n_ctl": 13,
  "PL_K_max": 15,
  "PL_mut_K_range": [1, 13],
  "ACT_SIM_m2_n_max": 6,
  "Z_rank_vs_exhaustive_n_max": 12,
  "delta_cx": "1/8",
  "w": 3,
  "d_rule": "abs",
  "d_sensitivity": "signed",
  "RP01_env": {"python": "3.12", "numpy": "2.2.6", "pe01_head": "549641460b8ddb536178f95fac2ec9390e84a987"}
}
```

`null` means that no $K \ge 1$ meets the bound. The Part B search at $n$ covers $4 \le K \le$ `K_R_max_m1_by_n[n]`
(capped at $K_{\rm cx}$) when that value is at least 4, and is `REGION_EMPTY` otherwise. Values for $n > N_{\max}$ are
not used.

## 10. Resources and CI (§A.40)

The estimates are not measurements. A local run that exceeds its row by a factor of 3 is stopped and moved to CI.
PE-01's own timings scale them: its `n8-clk` shard took about 1150 s and `n8-clk-m3` about 850 s.

| Work | Estimate | Where |
|---|---|---|
| EX, EN, TR, INC-RE, CH-IFF, MUT-NC, CA-STRUCT, IA, WF, PL ($2^{13}$ seeds), CX self-test; Part A at $n \le 5$ | under 10 min | local smoke |
| RP-01: PE-01 `n5-clk` replay at `54964146` in PE-01's pinned environment, and PE-01 verdict regeneration | about 5 min | CI, one job |
| Part A: `G_clkfix` and `G_clkfix_u`, every class, $n = 3..8$; M0 on all (a′) generators | 2–4 h in total | CI, sharded by $(n, \text{generator})$, with `emb_m3_passive` in its own jobs as in PE-01 |
| A-pop: `emb_m1_all` and `emb_m2_all` on `G_clk`, $K \le K_{\rm cx}$, with ablations, UX and SIM-P1 | under 1 h | CI, sharded by $n$ |
| ACT-SIM with non-vacuity cases; $m = 2$ at $n \le 6$ | under 30 min | CI |
| Part B, $N_{\max} = 24$: `emb_m1_all` at $n = 17..24$ with $4 \le K \le 63$, about $2^{25}$ seeds at the top $n$; M0 with $K \le 63$ at every $n$ | 1–3 h in total | CI, sharded by $(n, \text{generator})$, each job under 1 h |
| AR-C at $n > 8$: Z by the §4.2 methods, and cycle decomposition for $K_{\rm cx}$ | under 1 h | CI, with the Part B shards |
| INT on verdict-bearing witnesses | minutes | CI |

- The workflow's only trigger is `workflow_dispatch` (WF), and it is part of the code commits, so no push launches it.
  Every dispatch needs owner approval (§A.43 item 4).
- Shard outputs are committed as the structured files of §5, recording the commit, the recipe and the run id
  (§A.42 item 1). They are never relied on as logs (§A.44).
- Local work respects §A.40's disk thresholds. Part B never runs locally.

## 11. Literature (cited, not rederived)

- **Tagging rule.** PE-01 amendment A3's rule applies. It is fixed now, before any of the works below is read, with its
  scope set to PE-02's results: admissible witnesses under R or E, the §4.3 counts, and Lemma A-SIM.
  - COVERED-literature needs a first-hand reading that states or directly implies the result, for the same kind of
    generator and observer.
  - Coverage in kind is recorded as such.
  - A work read only through an abstract, a survey or a citing paper supports no tag.
- **No novelty claim** is made, and candidate-NEW is not assignable, until at least these are read first-hand:
  - Rueppel, "When shift registers clock themselves", EUROCRYPT '87, LNCS 304;
  - Gollmann–Chambers, "Clock-controlled shift registers: a review", IEEE JSAC 7(4):525–533 (1989);
  - the works PE-01's tag annex lists as unread: Chambers–Gollmann 1988; Beth–Piper 1984; Meier–Staffelbach 1989 and
    1994; Golić–O'Connor 1994; Živković 1991; Kholosha 2001; Gomułkiewicz et al., WEA 2005 and 2006.
- **What PE-02 must add beyond the two covered-in-kind results** (owner, #934):
  - beyond the 2006 clock-control fault attack (Gomułkiewicz–Kutyłowski–Wlaź): whether the PE-01 witness survives an
    explicit charge on the observer's description, and whether its advantage needs the clock to respond;
  - beyond AGHP's mechanism: whether passive observers of any accounted size gain on these generators, including on
    `G_clkfix`, where AGHP does not apply.

  Neither is claimed novel before the reading above.
- **Bearing on the accounting model, to read before any closure claim:**
  - Feder–Merhav–Gutman, "Universal prediction of individual sequences", IEEE Trans. IT 38(4) (1992): finite-state
    predictability, with the number of states as the resource;
  - Raz, "Fast learning requires good memory", FOCS 2016: bounded-memory learning in which the program is not charged;
  - Li–Vitányi, *An Introduction to Kolmogorov Complexity*: the invariance caveat of §2.1.
- **Definitions only:** Elias, IEEE Trans. IT 21(2) (1975), for $\gamma$; the Lehmer code.

## 12. Package

This directory holds:
- `PLAN.md` (this file);
- `NOTES.md`;
- `CHANGES-r2.md`;
- `design/` (drafting-time scripts and outputs);
- `review/` (independent reviews).

It will also hold `amendments/`, the code, `results/` and `REPORT.md`. Any amendment goes in `amendments/` before
the code it governs. The plan is committed alone when frozen.
