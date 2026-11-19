# A1-P8-HIST-1 · Full-history bounds from a positive read/write operation

**Author outcome — PROVED A1-FREE CONDITIONAL.** A finite active register with a positive outcome-labelled read/write table gives an explicit total variation bound for next reads conditioned on complete histories. The upper bound is nonincreasing in the length of a common suffix. A stationary reversible register exhibits both an attributable write and a strictly positive gap below the bound. A stationary reversible countercontrol has identical exact and iterated endpoint operators at every lag and still has a gap of $1/3$.

**Scope and evidence.** Codex N, 2026-11-19. Paper-only result for [#1397][issue] under the [owner direction recorded in #1169][authority]. The drafting and source pin is `baeb7723743e99b137ae3d0a1694e99ff97e2a73`, with [AGENTS.md][policy] at blob `81a26ba552d6096da8d097fc0289c0f1163df949`. The issue and direction identify the obligation and authority. The proof and exact controls below supply its mathematical evidence. Independent non-author model review returned [ACCEPT WITH NITS][math-review] on the proof, arithmetic and scope at `62edb8168ceeaa1cb5c5e6e779217aed069d63b1`.

**Goal link (§A.47).** Decide whether a structural property of one fixed record operation suffices to bound exact next reads on the declared histories without total finiteness. This addresses the history-law comparison left open by [A1-05][matrix].

## Fixed law and record operation

Fix a measurable invertible $T:S\to S$ with measurable inverse, a normalized invariant probability $\mu$, a finite visible alphabet $\mathcal A$, a measurable present record $X:S\to\mathcal A$, and a finite accessible horizon $H\ge 1$. Write $X_t=X\circ T^t$. Tick $t$ displays $X_t$ and appends it to the record log. Within the model this log is the rolling register $(X\circ T^{-H},\ldots,X)$. Its next contents are the shifted old entries and the new $X_1$. The accessible log starts at tick $0$ and exposes exactly the entries dispensed through the current tick, including the outcome $\bot$ when a tick yields no read. The present record is the current entry $X_t$. The complete history is $h=(x_0,\ldots,x_t)$ with event $C_h=\{X_0=x_0,\ldots,X_t=x_t\}$. This fixes which record variables are available and which pairs share a present. Each model below keeps its own update, invariant law and protocol fixed across all comparisons.

**Structural condition.** The protocol has a finite active hidden register $Z:S\to\mathcal Z$. Its read/write operation uses one map $\Phi$ and a fresh input $\xi_{t+1}$ of one law $\nu$ to set $(X_{t+1},Z_{t+1})=\Phi(Z_t,\xi_{t+1})$. Under $\mu$, this input is independent of the active registers and records through $t$ in the declared window. For each declared label $a$, the operation table
$$
M_a(i,j)=\nu\{\xi:\Phi(i,\xi)=(a,j)\}
$$
is strictly positive in every entry or is identically zero. Thus each possible label has a common full transition rectangle for the active register. The table is determined by the wiring and the input law. The active register can depend on previous writes and differ from both the present record and the full hidden state. Independence is with respect to the declared past and active registers. A reversible carrier may contain the entire input tape, including future inputs, as well as the log.

Put $M=\sum_a M_a$ and $B(i,a)=\sum_j M_a(i,j)$. Both $M$ and $B$ have stochastic rows. Let $\mathcal A_+$ consist of the nonzero labels and set $\pi(a)=\mu(X_0=a)$. Invariance and the table imply $\pi(a)>0$ exactly on $\mathcal A_+$. Define $p_{x_0}=\mu(Z_0\in\cdot\mid X_0=x_0)$ at positive $x_0$, allowing an arbitrary correlation of $Z_0$ with that root under $\mu$. For every $C_h$ of positive mass, multiplication of the labelled kernels gives
$$
\begin{split}
 \mu(C_h)&=\pi(x_0)\,p_{x_0}M_{x_1}\cdots M_{x_t}\mathbf 1,\\
 p_h&=\mu(Z_t\in\cdot\mid C_h)
     =\frac{p_{x_0}M_{x_1}\cdots M_{x_t}}
      {p_{x_0}M_{x_1}\cdots M_{x_t}\mathbf 1},\\
 q_h&=\mu(X_{t+1}\in\cdot\mid C_h)=p_h B,\qquad t<H .
\end{split} \tag{1}
$$
The product follows by conditioning at each tick on the old register and the entire record to date, then integrating against the fresh input law. All conditionals in (1) require positive mass. If $b_*=\min_{i\in\mathcal Z,\ a\in\mathcal A_+}B(i,a)$, every word over $\mathcal A_+$ has mass at least $\pi(x_0)b_*^t$. A factor $M_a=0$ gives an impossible outcome, including at the root by stationarity. When $\bot\in\mathcal A_+$, a word entirely of no-read outcomes is admissible and uses the same formula.

## Full-history next-read bound

For a row-stochastic matrix $R$, write $d(R)=\max_{i,j}\operatorname{TV}(R(i,\cdot),R(j,\cdot))$. Let
$$
 \Delta_a=\max_{i,j,k,l\in\mathcal Z}
       \log\frac{M_a(i,k)M_a(j,l)}{M_a(i,l)M_a(j,k)},
 \qquad
 \rho_a=\tanh(\Delta_a/4),\qquad
 \Delta=\max_{a\in\mathcal A_+}\Delta_a,\quad
 \rho=\max_{a\in\mathcal A_+}\rho_a .
$$
Here $\Delta_a$ and $\rho_a$ are defined for $a\in\mathcal A_+$.

**Claim.** For $1\le t<H$, take distinct positive histories $h,h'$ of length $t+1$ with common present $x_t=x'_t$. If their common suffix is $a_1,\ldots,a_\ell$ of length $1\le\ell\le t$, then
$$
 \operatorname{TV}(q_h,q_{h'})
 \le d(B)\tanh\!\left(\frac{\Delta_{a_1}}{4}
                  \prod_{r=2}^{\ell}\rho_{a_r}\right)
 \le \delta_\ell:=d(B)\tanh\!\left(\frac{\Delta}{4}\rho^{\ell-1}\right). \tag{2}
$$
Empty products are $1$, including $\rho^0$ when $\rho=0$. At $t=0$ histories sharing the present coincide. Identical histories have distance zero. For any pair sharing only the present, the uniform guarantee is $\delta_1=d(B)\rho$. Elapsed time by itself gives no additional power of $\rho$. The constants are independent of history masses once those histories have positive mass. The forward calculation uses only a measure-preserving measurable update and the stated operation. Invertibility supplies the state realization of the rolling log and the reversal comparison below.

**Proof.** For positive row vectors $v,w$, let
$$
D(v,w)=\max_i\log(v_i/w_i)-\min_i\log(v_i/w_i).
$$
Rescaling either vector leaves $D$ unchanged. For probability vectors $v,w$ with positive entries let $m=\min_i v_i/w_i$, $L=\max_i v_i/w_i$ and $r=L/m$. The ratio has mean $1$ under $w$. Bounding its positive deviation from $1$ by the secant line on $[m,L]$ gives
$$
 \operatorname{TV}(v,w)
 \le \frac{(L-1)(1-m)}{L-m}
 =\frac{r+1-rm-1/m}{r-1}
 \le \frac{\sqrt r-1}{\sqrt r+1}
 =\tanh(D(v,w)/4).
$$
When $m=L=1$ the distance vanishes. The second inequality follows from $rm+1/m\ge2\sqrt r$.

For one positive label matrix $A=M_a$ and nonzero nonnegative $v,w$, expand
$$
 \frac{(vA)_k(wA)_l}{(vA)_l(wA)_k}
 =\frac{\sum_{i,j}v_iw_j A(i,k)A(j,l)}
        {\sum_{i,j}v_iw_j A(i,l)A(j,k)}
 \le e^{\Delta_a}.
$$
Thus $D(vA,wA)\le\Delta_a$, including when one prefix posterior has zero entries. For positive $v,w$ set $u_i=\log(v_i/w_i)$ and
$$
 F_k(s)=\log\sum_i w_i e^{su_i}A(i,k),\quad
 \omega_i^{k}(s)=\frac{w_i e^{su_i}A(i,k)}{\sum_j w_j e^{su_j}A(j,k)}.
$$
The derivative $F'_k(s)$ is the expectation of $u$ under $\omega^{k}(s)$. For any $k,l$, the log ratio of $\omega^k(s)$ and $\omega^l(s)$ ranges over an interval of length at most $\Delta_a$ by the cross-ratio definition. Their TV is at most $\rho_a$ by the preceding inequality. Consequently $|F'_k-F'_l|\le\rho_a(\max_i u_i-\min_i u_i)$. Integrate from $0$ to $1$ and maximize over $k,l$ to get
$$
 D(vA,wA)\le \rho_a D(v,w).
$$
Apply the finite diameter bound at the first common label, then the contraction at each remaining common label. The filters in (1) differ only by normalized propagation from the respective prefix posteriors, so this bounds $D(p_h,p_{h'})$. Finally $\operatorname{TV}(vR,wR)\le d(R)\operatorname{TV}(v,w)$ for stochastic $R$: write the difference of the input laws as its TV times the difference of two probability vectors supported on its positive and negative parts, then average row differences across the two supports. Apply this to $B$ to obtain (2).

### Conditioning costs

For joint finite laws $L,L'$ at TV distance $\varepsilon$, and a history event of masses $p,p'>0$, the conditional next-read rows have distance at most $\min(1,\varepsilon/\max(p,p'))$. To see this, take $p\ge p'$. Inside the event the sum of the pointwise minima of the joint probabilities is at least $p-\varepsilon$, since the positive part of $L-L'$ has total mass $\varepsilon$. Dividing the two restricted laws by $p,p'$ gives conditional overlap at least $(p-\varepsilon)/p$ when this quantity is positive. Marginalizing to the next read preserves the bound. A two-history contrast comparison incurs the sum of the two respective errors. In particular a lower mass bound $p_\star$ on the histories used in both laws gives error at most $2\varepsilon/p_\star$ in the pair distance. This concerns transfer from a different joint law. Equation (2) applies within the fixed $\mu$.

The same inequality applies to conditioning $q_h,q_{h'}$ on a successful next read. With masses $r_h,r_{h'}>0$, the distance after discarding $\bot$ is at most $\min(1,\delta_\ell/\max(r_h,r_{h'}))$. The factor is necessary in general. Two rows that give mass $r$ to different successful symbols and both give $1-r$ to $\bot$ have distance $r$ including no-read and distance $1$ given success. The same example with a history mass $r$ and mutually singular predictions inside that history saturates the joint-law conditioning cost. A zero-mass history or zero-mass success event has no conditional row under the stated law.

## The two compressions

Let $Uf=f\circ T$ and $Pf=\mathbb E_\mu[f\mid X]$. On the range of $P$, the one-step compression $\mathcal K=PUP$ is the stochastic matrix $Q(x,y)=\mu(X_1=y\mid X_0=x)$ on the positive cells. Its invariant law is $\pi$. For visible functions $f,g$ and $n\ge1$,
$$
 \langle f,\mathcal K^n g\rangle_\mu
 =\sum_{x,y}\pi(x)\overline{f(x)}\,Q^n(x,y)g(y).
$$
This is the correlation of the Markov chain with transition $Q$ started in $\pi$. The Markov interpretation samples the microscopic conditional from the current cell afresh at each step. The forward operator bound in A1-05 constrains these correlations if a centred power-norm bound is supplied. In the positive-table class, $Q$ itself has all positive entries on $\mathcal A_+$, and $\operatorname{TV}(Q^n(x,\cdot),\pi)\le d(Q)^n$. The projection throughout is the declared record projection. [A1-05 P8-M][matrix]

The exact endpoint compression $PU^nP$ instead has rows $E_n(x,\cdot)=\mu(X_n\in\cdot\mid X_0=x)$. In the positive-table class, (1) yields $E_n(x,\cdot)=p_xM^{n-1}B$ for $1\le n\le H$, by summing all intervening labels. The invariant law $\eta$ of the realized $Z_t$ satisfies $\eta M=\eta$ and $\eta B=\pi$ by stationarity, so
$$
 \operatorname{TV}(E_n(x,\cdot),\pi)
 \le d(B)d(M)^{n-1}\operatorname{TV}(p_x,\eta).
$$
There is also a comparison to $Q^n$ from (2). For $1\le s<H$, the stationary row $Q(x_s,\cdot)$ is the mixture of $q_{h'}$ over complete histories ending at $x_s$. Hence each $q_h$ with that present is within $\delta_1$ of the row. Average conditional on the initial cell to obtain $\operatorname{TV}(E_{s+1}(x,\cdot),E_s(x,\cdot)Q)\le\delta_1$. Contracting differences through $Q$ and using $E_1=Q$ gives, for $2\le n\le H$,
$$
 \max_x\operatorname{TV}(E_n(x,\cdot),Q^n(x,\cdot))
 \le \min\!\left(1,\ \delta_1\sum_{j=0}^{n-2}d(Q)^j\right).
$$
The separate exact endpoint formula and finite-window comparison use the structural condition. The example below gives different exact and iterated rows even within that class.

**Main's exact-versus-iterated control.** Let $H=5$, let $T$ be the cyclic shift on five equiprobable states, and mark one state with label $1$ and the other four with $0$. The conditional endpoint row from $1$ goes to $0$ for each lag $1,\ldots,4$. Exactly one of the four $0$-states reaches the marked state at each such lag. Thus $E_n=Q=\left(\begin{smallmatrix}3/4&1/4\\1&0\end{smallmatrix}\right)$ for $1\le n\le4$, and $E_5=I$. The stationary row is $\pi=(4/5,1/5)$, and $Q^n=\Pi+(-1/4)^n(I-\Pi)$ where each row of $\Pi$ equals $\pi$. At lag five the row from the marked cell has TV separation $205/256$ from $Q^5(1,\cdot)$. This is Main's counterexample with the operator mismatch quantified. [Main §4.6, scope (ii)][main-control]

## Exact positive example with a retained write

Take $H=5$, $\mathcal Z=\{0,1\}$, $\mathcal A=\{0,1,\bot\}$, and a two-sided product tape with independent tick variables. A tick presents a read with probability $1/2$. On a read, $X_{t+1}$ is $Z_t$ flipped with probability $1/4$; otherwise $X_{t+1}=\bot$. An independent mode draw then keeps $Z_t$ with probability $1/4$, writes the real label $X_{t+1}$ into $Z_{t+1}$ with probability $1/4$, or refreshes $Z_{t+1}$ to an independent fair bit with probability $1/2$. The write mode on a no-read also refreshes to a fair bit. Every mode uses the same declared visible log, with $\bot$ in the no-read slot.

The microscopic carrier is the tape and $T$ shifts it one tick forward. With product law $\mu$, ordinary refresh slots occur arbitrarily far into the past almost surely. Starting from the latest such refresh gives $Z_t$ from inputs at times through $t$. This defines the recursive register consistently on a shift-invariant full-measure set. The read at tick $t$ uses $Z_{t-1}$ and the inputs at $t$. The shift is invertible, preserves $\mu$, and supplies the rolling log. The inputs at the next tick are independent of all previous records and registers. The total state space here is infinite.

The three matrices, in row and column order $0,1$, are
$$
 M_0=\frac1{32}\begin{pmatrix}9&3\\2&2\end{pmatrix},\qquad
 M_1=\frac1{32}\begin{pmatrix}2&2\\3&9\end{pmatrix},\qquad
 M_\bot=\frac1{16}\begin{pmatrix}5&3\\3&5\end{pmatrix}.
$$
For example on $X_{t+1}=a\in\{0,1\}$ the probability of setting the register to $1$ is $(Z_t+a+1)/4$. With $X_{t+1}=\bot$ it is $3/8+Z_t/4$. Combining these probabilities with the read probabilities gives the displayed entries. The largest cross-ratio is $3$, attained on labels $0,1$; the one for $\bot$ is $25/9$. Thus $\Delta=\log 3,\ \rho=2-\sqrt3,\ d(B)=1/4$. The uniform same-present bound is $(2-\sqrt3)/4$.

The sum $M$ has diagonal $21/32$ and off-diagonal $11/32$. Its stationary register law is fair and $\pi=(1/4,1/4,1/2)$ in order $0,1,\bot$. Let $v_a=\mu(Z_0=1\mid X_0=a)$. Multiplying the fair register row by each $M_a$ and normalizing gives $v_0=5/16,\ v_1=11/16,\ v_\bot=1/2$.

A write and a later read can be attributed directly in this protocol. With the old register and write mode fixed, both real labels have positive probability from the flip input. Changing that label changes the written register, and a successful noiseless next read of the register transmits the difference. Also, conditional on the real root labels $1$ and $0$, the difference $v_1-v_0=3/8$ has a contribution $1/4$ from the write mode and $1/8$ from keep. The keep contribution comes from the difference $1/2$ between the two posterior probabilities that the register *before* the root read was $1$, multiplied by the keep probability $1/4$. The refresh contribution is zero. This separates an actual write from a correlation that precedes it in the same invariant law.

For $1\le\ell\le4$ compare the complete histories $(0,\bot^\ell)$ and $(1,\bot^\ell)$. Each has mass $2^{-(\ell+2)}$, since the next no-read gate is fair and independent of the past. Each no-read step sends a posterior register mass $v$ to $3/8+v/4$. The next outcome has mass $1/2$ on $\bot$ and mass $1/8+v/4$ on $1$. Thus the exact TV gap is
$$
 \frac{3}{32}\,4^{-\ell}>0 .
$$
This gap doubles if the next outcome is conditioned on a successful read. A pair sharing a successful present is $h=(0,0),\ h'=(1,0)$, with masses $19/256,\ 13/256$. Applying the label-$0$ posterior map $v\mapsto (3-v)/(12-8v)$ gives $43/152,\ 37/104$, respectively, and the next-read TV is $9/494$. For $2\le t<H$, prepend $t-1$ copies of $\bot$ to both $(0,\bot)$ and $(1,\bot)$. These histories have the same positive gap $3/128$ as the original one-suffix pair, since the preceding no-read block leaves the prior register fair before the first real label. They show why time elapsed with only the last label shared gives no automatic improvement. The rolling log retains all these distinctions in the full state.

For an endpoint check, put $g(0)=-1,\ g(1)=1,\ g(\bot)=0$. Then $Qg=(3/32)g$, while one unobserved register step multiplies the deviation from the fair register law by $5/16$. Directly,
$$
 E_n(x,1)=\frac14+\frac3{64}(5/16)^{n-1}g(x),\qquad
 Q^n(x,1)=\frac14+\frac3{64}(3/32)^{n-1}g(x).
$$
Both leave mass $1/2$ on $\bot$ for $n\ge1$. The row TV discrepancy at $n=2$ for either real root is $21/2048$.

## Adverse retained record and correlated preparation

Again set $H=5$. Use a tape of independent fair pairs $(A_j,B_j)_{j\in\mathbb Z}$ and an independent uniform phase $c\in\{0,1,2\}$. The invariant update increments the phase, and on phase $2$ wraps it to $0$ and shifts the pair tape forward. Each branch is invertible between its phase slices, and uniform phase and product tape give the normalized invariant $\mu$. The fixed readout in phases $0,1,2$ is, respectively, $A_0,\ B_0,\ A_0\oplus B_0$ on the current tape. Use the same rolling log of binary readings.

In phase $0$, the current pair is stored as the visible $x=A_0$ and the pending $b=B_0$. The first tick writes $m\gets x$ into a hidden memory slot and displays $b$. The next tick displays $m\oplus b$ and retains $m$. Reconstructing $(A_0,B_0)=(m,m\oplus X)$ at phase $2$ puts the old pair into the past tape at wrap. These are phase-dependent coordinates of the stated bijection. At phase $0$, fixing $b$ and the other pairs and varying $x$ gives the same present $b$ after the write and a different parity on the next read.

Any two distinct positions in a block have independent fair labels. Different blocks are independent. Conditioning on the initial phase thus gives independent fair labels at any two distinct times. In particular $Q$ has identical fair rows, $Q^n=Q$, and $E_n=Q$ at all positive lags. Now compare the full histories $h=(0,0)$ and $h'=(1,0)$ at $t=1$. Each has probability $1/4$ in every initial phase, so the phase posterior stays uniform in both. For initial phase $0$, the stored first label is $m=X_0$, and $X_2=X_0\oplus X_1$. For initial phases $1$ and $2$, $X_2$ is fair independent of the two read labels: it is, respectively, the first bit of a fresh pair and the second bit of a pair whose first bit was just read. Consequently
$$
 \mu(X_2=1\mid h)=1/3,\qquad \mu(X_2=1\mid h')=2/3 .
$$
The TV gap is $1/3$ at equal, positive history mass and with identical exact and iterated endpoint operators. The protected register and deterministic read in the parity phase show why this wiring fails the positive-table condition for the register containing phase and memory. Any positive-table realization of this same record law would need $\delta_1\ge 1/3$ by (2). This stationary control gives an all-lag counterpart to [Main §3.4's finite-window XOR example][main-xor].

There is a separate way to generate a gap by correlated preparation alone. Keep a hidden fair bit $R$ fixed under a shift of an independent two-sided noise tape with independent flips of probability $1/4$. Display $X_t=R$ flipped by noise at tick $t$ and write it only to the declared rolling log. This is one invariant product law with the same $H=5$ and protocol recording all binary outcomes. Here $\mu(R=1\mid 00)=1/10$ and $\mu(R=1\mid 10)=1/2$, at word masses $5/16$ and $3/16$. Both end in $0$. Since the next read has conditional probability $1/4+R/2$ of being $1$, their TV gap is $1/5$. The different root-conditioned memory was present before the log wrote either history. The hidden bit is conserved and the operation table for $R$ has zero off-diagonal entries. Its $Q$ has diagonal $5/8$, so the centred eigenvalue of $\mathcal K$ is $1/4$, whereas the same exact endpoint diagonal $5/8$ persists at every positive lag. This control keeps the update and prior fixed and attributes the gap to the hidden preparation selected by the histories.

## Reach and first unsupported inference

The mathematical conclusion supplies an actual history-law bound on one record projection and one finite window. Its observable is a different quantity from Main's iterated local memory time. The two results require distinct inputs: the theorem of §4.6 uses bounded coupling geometry, total finiteness of its representative, local equilibrium for the thermal application, and effective mixing for the iterated channel. Its rate comparison addresses partitions and (C2-slow). The present result supplies a finite-channel record estimate under a declared operation with no count of total states and no equilibrium clock or memory-time threshold. It is narrower than the printed selection rule in physical reach. The two bounds are incomparable as inequalities because one bounds the exact next-read contrast and the other bounds memory time in the iterated description. The endpoint controls show that vanishing centred iterated correlations alone cannot supply the exact conditional history bound. Main §2.3 posits uniform erosion for its gap estimate. Section 3.4 assumes TV closeness of each actual history's hidden law to a supplied reference prior. Here the bound follows from the labelled operation matrices and applies to same-present pairs, with an improved rate for a common suffix. [Main §2.3][main-erasure] · [Main §3.4][main-filter] · [Main §4.6][main-p8]

The root rows here are the stationary conditionals at positive cells. Main §2.3's finite-return divisibility results address a different rooted family with a prescribed common hidden preparation and include rows at zero-mass visible roots. [Main §2.3][main-recurrence]

The positive example keeps the log and exhibits readback. The bound controls the difference in the declared next observable, with the hidden mechanism and accessible register distinguished. Physical erasure or exclusion would require separately identified writes, reads and candidate preparations with a verified conditional law and operational threshold. For the reverse microscopic update using the same $P$, the compression is $PU^{-1}P=\mathcal K^*$ and has the same centred power norms. The orientation in (1) is the declared order of writes and reads. Symmetric power decay supplies no physical arrow of time.

The first unsupported physical step is identifying a normalized invariant $\mu$ and a matching native write/store/read operation with the stated input independence and positivity for an actual candidate observer. A1-05 already stops at state selection, before such a transfer. Full physical P8 and OI–QM remain open. A1 remains OPEN/UNADOPTED and physical measurement sourcing remains NOT PASSED. [A1-05 source decision][matrix]

[issue]: https://github.com/amaybaum/incompleteness/issues/1397
[authority]: https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7005796462
[math-review]: https://github.com/amaybaum/incompleteness/pull/1400#pullrequestreview-5973102338
[policy]: https://github.com/amaybaum/incompleteness/blob/baeb7723743e99b137ae3d0a1694e99ff97e2a73/AGENTS.md
[matrix]: https://github.com/amaybaum/incompleteness/blob/baeb7723743e99b137ae3d0a1694e99ff97e2a73/verification/audits/foundations/a1-05-p8-observer-selection/SOURCE-MATRIX.md
[main-recurrence]: https://github.com/amaybaum/incompleteness/blob/baeb7723743e99b137ae3d0a1694e99ff97e2a73/papers/Main.md#L131-L157
[main-erasure]: https://github.com/amaybaum/incompleteness/blob/baeb7723743e99b137ae3d0a1694e99ff97e2a73/papers/Main.md#L159-L178
[main-filter]: https://github.com/amaybaum/incompleteness/blob/baeb7723743e99b137ae3d0a1694e99ff97e2a73/papers/Main.md#L457-L473
[main-xor]: https://github.com/amaybaum/incompleteness/blob/baeb7723743e99b137ae3d0a1694e99ff97e2a73/papers/Main.md#L477
[main-p8]: https://github.com/amaybaum/incompleteness/blob/baeb7723743e99b137ae3d0a1694e99ff97e2a73/papers/Main.md#L746-L764
[main-control]: https://github.com/amaybaum/incompleteness/blob/baeb7723743e99b137ae3d0a1694e99ff97e2a73/papers/Main.md#L764
