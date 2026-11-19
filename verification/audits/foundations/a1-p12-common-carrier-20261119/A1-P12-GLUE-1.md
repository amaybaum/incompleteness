# A1-P12-GLUE-1 — Stationary Markov laws on one local reversible carrier

**A1-FREE CONDITIONAL THEOREM.** Paper proof by Codex O. Independent
non-author model review returned [ACCEPT][math-review] at
`4212e600752b77d4095cd8191915493c584cacb8`.
The source pin is `baeb7723743e99b137ae3d0a1694e99ff97e2a73`. The goal
is to determine when a fixed local update, spatial readout and common hidden
law can reproduce one family of passive observations at every integer
horizon. [#1398][issue] · [Owner direction relayed in #1169][authority]

## Compatible family and prescribed interface

Let $V=\{0,1\}$ for the controls, with time zero at the first passive read
and uniform visible preparation. For $p\in(0,1)$ define

$$
M_p=\begin{pmatrix}1-p&p\\p&1-p\end{pmatrix},
\qquad
P_K^{(p)}(x_0,\ldots,x_K)=\tfrac12\prod_{t=0}^{K-1}M_p(x_t,x_{t+1}).
$$

The positive family uses $p=1/4$. The countercontrol uses $p=1/3$. Summing
over the last symbol uses the row sums of $M_p$ and gives projective
consistency. The uniform distribution is invariant for $M_p$, so both
families specify stationary windows.

For the construction let $V$ be any finite set with $|V|\ge2$ and let
$A$ be a finite bath alphabet with $q=|A|\ge1$. Fix the spatial sites
$j\in\mathbb Z$ and two registers $(v_j,b_j)\in V\times A$ at each site.
Take $S=(V\times A)^\mathbb Z$, its cylinder $\sigma$-algebra $\Sigma$ and
the countable product probability $\mu$ of independent uniform visible
and bath registers at all sites. Write $X(s)=v_0$. Under the given
identification $S=V\times H$, the hidden coordinates are
$H=V^{\mathbb Z\setminus\{0\}}\times A^\mathbb Z$, and
$\mu=u_V\otimes\rho$, with $\rho$ the uniform product on those registers.
Thus every visible root $a$ has conditional preparation
$\delta_a\otimes\rho$ with the same normalized $\rho$.

The update transports each bath symbol one site to the right and applies
the same bijection $g\colon V\times A\to V\times A$ at each site, at every
tick. In coordinates,

$$
(v'_j,b'_j)=g(v_j,b_{j-1}).
$$

The gate reads the on-site visible register and the left neighbour's
bath register. It writes both registers at the receiving site. The
update commutes with spatial translations. The observer reads just $v_0$
at integer ticks and leaves the state unchanged.
The lattice, direction of transport, product law and readout are stipulated
mathematical inputs, fixed independently of the horizon and sampled
outcomes. The gate is selected once for a given transition matrix.

## Local reversible realization

**Theorem.** On this interface every doubly stochastic matrix $M$ on $V$
with all $qM(a,c)$ integers is realized by one choice of $g$. Under $\mu$
the resulting $(S,\Sigma,\mu,T,X)$ is measure-preserving and gives the
stationary Markov law of $M$ on every integer window. Under each
$\delta_a\otimes\rho$ the forward law is the same chain started at $a$.
Every update of the prescribed form has a doubly stochastic $M$ with
these integer counts.

**Gate counts.** For a given gate, count the input bath labels $b$ for
which $\pi_V g(a,b)=c$. Calling the counts $N_{ac}$, each row sums to $q$
because there are $q$ inputs at visible label $a$. Each column sums to
$q$ because there are $q$ outputs at visible label $c$, all attained once.
The rooted one-tick matrix is $M(a,c)=N_{ac}/q$. Conversely, for the
specified matrix set $N_{ac}=qM(a,c)$. Partition the bath labels at each
input $a$ into blocks indexed by $c$ of sizes $N_{ac}$. Partition the
bath labels at each output $c$ into blocks indexed by $a$ of those same
sizes. Biject each input block to its associated output block. This
defines the required permutation on $V\times A$, including any empty
blocks. Main §3.2 gives the one-step uniform-prior correspondence. The
history argument below supplies the additional conclusion on this fixed
lattice. [Main §3.2][one-step]

**Inverse and measure preservation.** From each output pair calculate
$(u_j,d_j)=g^{-1}(v'_j,b'_j)$. Then $v_j=u_j$ and $b_j=d_{j+1}$. The
forward and inverse maps each use at most two neighbouring sites per
output site and are measurable on $\Sigma$. Transport permutes the bath
coordinates, preserving their product law and independence from the
visible coordinates. After transport the pairs are independent uniform
points of $V\times A$. Applying $g$ at each site preserves their product
law. This proves $T_*\mu=\mu$.

**Independence along a history.** At time $t\ge0$ let $L_t$ be all
registers strictly left of the origin and let $B_t=b_{-1}(t)$. We show
that $L_t$ has the left half-line product law and is independent of
$(X_0,B_0,\ldots,B_{t-1})$. The statement at time zero follows from the
product preparation $\eta\otimes\rho$ for any visible law $\eta$,
including each fixed root.
Given the statement at time $t$, the inputs to the next left half-line
are the pairs $(v_j(t),b_{j-1}(t))$ for $j<0$. These pairs use each left
visible register and all left bath registers except $B_t$, each once.
They are independent uniform pairs, independent of $B_t$ and of
$(X_0,B_0,\ldots,B_{t-1})$. Applying $g$ to each of the pairs gives
$L_{t+1}$ with the same product law and independent of the enlarged
tuple. This proves the induction. The observation history through $t$
is a function of $(X_0,B_0,\ldots,B_{t-1})$ since
$X_{r+1}=\pi_V g(X_r,B_r)$. Thus $B_t$ is uniform even conditional on the
whole positive-probability history through $t$. In particular the bath
arrivals are independent across forward ticks.

The joint probability for any word on $0,\ldots,K$ under an initial
visible law $\eta$ with the same hidden law $\rho$ is

$$
\mathbb P_{\eta\otimes\rho}(X_0=x_0,\ldots,X_K=x_K)
=\eta(x_0)\prod_{t=0}^{K-1}M(x_t,x_{t+1}).
$$

This follows by multiplication of the conditional probabilities, with
zero-probability words having zero product. Set $\eta=u_V$ for the
stationary law or $\eta=\delta_a$ for each rooted law. Under $\mu$,
invariance shifts the formula to every integer interval
$[\ell,r]$, and summing over omitted times gives all finite joint laws.
In particular, conditional on $X_0=x_0$ the word on $[-m,n]$ has weight
$\prod_{t=-m}^{n-1}M(x_t,x_{t+1})$. The past and future then factor, and
the backward kernel is $M^{\mathsf T}$, also the one-step count from
$g^{-1}$. The same conditional law on $[-m,n]$ applies to the rooted
preparation. Invariance is proved for $\mu=u_V\otimes\rho$. An alternative
preparation can be nonstationary on the same invertible carrier. For
example with $M_{1/4}$ a nonuniform $\eta$ gives different time-zero and
time-one visible laws $\eta$ and $\eta M_{1/4}$.

## Exact controls and resource cost

For $P_K^{(1/4)}$ take $A=\mathbb Z/4\mathbb Z$ and choose

$$
c=v\oplus\mathbf 1_{\{b=0\}},\qquad
d=b+c\pmod 4,\qquad
g(v,b)=(c,d).
$$

The inverse subtracts $c$ from $d$ modulo four to obtain $b$ and then
recovers $v=c\oplus\mathbf 1_{\{b=0\}}$. The bath output depends on the
visible output and travels to the next site on the next tick. At the
collision, the output pair retains the preceding visible value and the
incoming bath label. Exactly one of the four uniform incoming labels
flips the visible bit, giving $M_{1/4}$. A four-symbol bath is the
smallest possible bath in this interface for that matrix, since $q/4$
must be an integer.

The same gate and readout are reused on the same trajectory indefinitely.
At time zero there are already countably many sites with three bits per
site in this control. One symbol is supplied per tick at the origin by
the initially prepared left half-line, and the outgoing symbol enters the
rightward transport. The system applies the gate simultaneously at every
site, with no resets, clock or external draws. The initial sites used by
a window $0,\ldots,K$ lie in $[-K,0]$, by iteration of the forward
neighbourhood. This finite dependence at each $K$ uses an unbounded set
of available sites across horizons. [Finiteness classification][fclass]

For **any** deterministic rule on sites with finitely many bits per site,
finitely many input sites per output and the same direct, single-bit
readout convention, suppose the remaining bits have the independent fair
product law in the declared rooted coordinates. For a fixed root, the
window through $K$ depends on some finite set of $m_K$ distinct initial
hidden bits, by finite iteration. Each word probability is an integer
multiple of $2^{-m_K}$. This gives two consequences.

- The stationary $P_K^{(1/3)}$ has one-step flip probability $1/3$ at
  each root. It is impossible throughout this fair-bit class, already at
  one tick, regardless of the size of the finite input sets. Both
  families have per-horizon finite realizations under Main §3.4. A
  ternary uniform bath in the lattice construction also realizes
  $P_K^{(1/3)}$ at every $K$ by the same gate formula with arithmetic
  modulo three. This locates the obstruction in the imposed law and
  finite dependence of the fair-bit interface. [Main §3.4][dilation]
- For $P_K^{(1/4)}$, the word which flips at every tick conditional on
  either root has probability $4^{-K}$. Thus any set of initial fair
  hidden bits determining that rooted window has at least $2K$ bits.
  A fixed finite supply of initial fair bits cannot meet the exact
  probabilities even though each tick uses a bounded neighbourhood.

There is a separate finite-total-carrier obstruction with any initial
prior. For the two controls the rooted map is $M_p^L$ at time $L$.
Its diagonal is $(1+(1-2p)^L)/2<1$ for every $L\ge1$, as is seen by
diagonalizing on the constant and sign vectors. A finite permutation of
order $L$ forces $X_L=X_0$ on every trajectory, contradicting that
diagonal. Stationary joint laws are invariant under translations of the
time window. A finite permutation forces equality *within* each
trajectory at a common positive lag. Main's finite classification of
rooted matrices concerns one-time marginals from each root. Main's
questions about recurrent multi-time gluing and approximation before
finite recurrence have different hypotheses from these exact aperiodic
controls.
[Main §3.4 all-time scope][finite-all-time]

## Scope of the result

For finite alphabets, stationary projective consistency already yields
the bilateral outcome law by Kolmogorov extension and the canonical
measure-preserving shift, with the time-zero coordinate as readout.
To define each finite distribution, translate its time indices into
nonnegative time and use stationarity to make the choice immaterial.
For merely one-sided compatible laws, one may extend to bilateral
sequences with a fixed past and retain an invertible shift. A
nonstationary observed law precludes invariance of its realizing
initial law. On the canonical outcome carrier, conditioning on the root
can change the distribution of the remaining outcome coordinates.
The lattice result prescribes a common spatial product law in its
specified register coordinates, establishes forward and reverse local
updates, and has the finite-input restrictions quantified above.
Main's $S\iff D\iff Q_{\mathrm{fb}}$ applies per finite horizon.
[Main §3.4 equivalence][equivalence]

The independently reviewed A1-RIGID-1 record (#1396, on `main`) concerns compactness
of the visible indicator orbits and the rooted near-return route to
P-indivisibility. In the positive flip chain the squared $L^2(\mu)$
distance between indicator iterates at distinct times $s,t$ is
$\Pr(X_s\ne X_t)=(1-2^{-|t-s|})/2\ge1/4$, so the orbit has noncompact
closure. The matrices $M_{1/4}^t$ admit the stochastic divisors
$M_{1/4}^{t-s}$ for $s<t$. That record and its review document the
comparison of scopes. The result here follows from the explicit local
construction and cylinder counts. [#1396 record][rigid] · [Independent review][rigid-review]

The theorem concerns passive integer-time readout for the declared
first-order Markov class. Physical preparation, the readout mechanism
and action-labelled laws are separate obligations. The one-dimensional
directed lattice is stipulated. The common observer cut and native
scalar field needed to identify the SM Markov kernel, its companion
wave block, gauge selection and operational QM remain open at their
respective scopes. The on-main A1-11 forward gauge algebra uses supplied
local carrier, kinetic, condensate and action inputs. A1 remains open
and unadopted, and physical measurement sourcing remains NOT PASSED.
[A1 matrix][matrix] · [#1055 assessment][assessment] · [#1321 observer trace][trace]
· [A1-11 forward algebra][forward]

[issue]: https://github.com/amaybaum/incompleteness/issues/1398
[authority]: https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7005796462
[math-review]: https://github.com/amaybaum/incompleteness/pull/1399#pullrequestreview-5973094703
[one-step]: https://github.com/amaybaum/incompleteness/blob/baeb7723743e99b137ae3d0a1694e99ff97e2a73/papers/Main.md#L274-L278
[dilation]: https://github.com/amaybaum/incompleteness/blob/baeb7723743e99b137ae3d0a1694e99ff97e2a73/papers/Main.md#L520-L526
[equivalence]: https://github.com/amaybaum/incompleteness/blob/baeb7723743e99b137ae3d0a1694e99ff97e2a73/papers/Main.md#L550-L558
[finite-all-time]: https://github.com/amaybaum/incompleteness/blob/baeb7723743e99b137ae3d0a1694e99ff97e2a73/papers/Main.md#L642-L646
[matrix]: https://github.com/amaybaum/incompleteness/blob/baeb7723743e99b137ae3d0a1694e99ff97e2a73/verification/audits/foundations/a1-recovery-matrix-20261116/RECOVERY-MATRIX.md#L40-L56
[assessment]: https://github.com/amaybaum/incompleteness/blob/baeb7723743e99b137ae3d0a1694e99ff97e2a73/verification/audits/foundations/a1-necessity-20261117/ASSESSMENT.md#L31-L47
[trace]: https://github.com/amaybaum/incompleteness/blob/baeb7723743e99b137ae3d0a1694e99ff97e2a73/verification/audits/foundations/a1-free-p12b-observer/TRACE.md#L13-L23
[forward]: https://github.com/amaybaum/incompleteness/blob/baeb7723743e99b137ae3d0a1694e99ff97e2a73/verification/audits/foundations/a1-11-local-gauge-forward/FORWARD-ALGEBRA.md#L9-L35
[fclass]: https://github.com/amaybaum/incompleteness/blob/baeb7723743e99b137ae3d0a1694e99ff97e2a73/verification/audits/foundations/a1-finiteness-classes-20261117/CLASSIFICATION.md#L20-L28
[rigid]: https://github.com/amaybaum/incompleteness/blob/a932a1f6398bdd3f9a1e46b3fecba2bf3145a344/verification/audits/foundations/a1-rigid-visible-recurrence-20261119/A1-RIGID-1.md
[rigid-review]: https://github.com/amaybaum/incompleteness/pull/1396#pullrequestreview-5972282779
