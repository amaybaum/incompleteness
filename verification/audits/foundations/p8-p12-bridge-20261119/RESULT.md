# P8–P12(b) bridge on a local reversible lattice

**Author result — A1-free conditional construction.** One rightward bath
shift and one site permutation give a stationary observer law with successive
requests, a locally recoverable write and a second response that depends on
the written carrier value. Two positive-mass histories with the same current
outcome have next-read total variation $1/15$. All three outcome-labelled
matrices are positive, and they give an explicit common-suffix bound. The
construction uses an autonomous request track and a stipulated product
preparation. The guiding draft linked from [#1403][issue] records the
independent mathematical review of the immutable checkpoint.

**Provenance.** Worker P, 2026-11-19, for [#1403][issue] under the [owner
decision relayed in #1169][authorization], drafted from
`baeb7723743e99b137ae3d0a1694e99ff97e2a73`.
The [P12(b) lattice][p12] and [P8 operation and bound][p8] specify the
comparison problems. The site map, law, fixed-input witness and bound are
proved below.

**Goal link (§A.47).** Decide whether one spatially local reversible carrier
with a common preparation can supply the retained write and history law
needed for the P8 bound, and which observer and preparation conditions a
construction requires.

## Carrier, readout and request protocol

Use sites $j\in\mathbb Z$, a persistent site register $v_j\in V$ and
a rightward bath register $b_j\in A$. Set
$$
\mathcal X=\{0,1,\bot\},\qquad V=\mathcal X\times\{1,2,3,4\},\qquad
A=\{0,1,2\}\times\{0,1,2,3\}^2\times\{0,1\}\times\{0,\ldots,5\}.
$$
The microscopic law $\mu$ is the normalized product of the uniform
laws on these two registers at every site, on the cylinder
$\sigma$-algebra of $S=(V\times A)^{\mathbb Z}$.
At the origin, write $v_0(t)=(X_t,r_t)$ and decode its active carrier bit
as $Z_t=z(X_t,r_t)$, where
$$
z(a,r)=\mathbf 1_{\{r\le c_a\}},\qquad
(c_0,c_1,c_\bot)=(1,3,2).
$$
The present read projection exposes $X_t$. At the initial cut it is the
only exposed value. The actual hidden coordinates are $r_0$, every
other persistent register, and all bath registers, including the one at
the origin. Thus $\mu=\pi\otimes\rho$, with $\pi$ uniform on
$\mathcal X$ and a single normalized product $\rho$ for every root.
In particular the rooted laws are $\delta_a\otimes\rho$.
The active bit depends on both the visible and hidden coordinates.
The probability of $Z_0=1$ at root $a$ is $c_a/4$ under that common
hidden preparation.

The site gate receives $v$ and one incoming bath symbol
$\alpha=(D,F,K,U,W)\in A$. The request arrives as $D\in\{1,2\}$.
The component $D=0$ delivers no request and displays $\bot$. Every
arriving request receives a binary response on that tick. With
$i=z(v)$, the desired new displayed outcome $a$ and carrier value
$z'$ are
$$
a=\begin{cases}
\bot & D=0,\\
i\oplus\mathbf 1_{\{F=0\}} & D\in\{1,2\},
\end{cases}
\qquad
z'=\begin{cases}
i & K\in\{0,1\},\\
a & K=2,\ D\ne0,\\
U & K=3\ \text{or}\ (K=2,\ D=0).
\end{cases}
$$
Here $K=2$ with a request writes the outcome into the active carrier.
In the keep mode the active bit persists even when the displayed symbol
changes. Set $C_{a,z'}=\{r:z(a,r)=z'\}$. In increasing order on this set
choose the slot with zero-based index $W\bmod|C_{a,z'}|$, and write
$v'=(a,r')$ with that slot. The possible slot counts are $1,2,3$,
which all divide six. A uniform $W$ therefore assigns equal weight to
each slot for a given $(a,z')$. Requests are autonomous. Their incoming
track and all the other bath components are prepared in the same
spatial product law. The protocol displays the outcome of each tick,
including every $\bot$ in the declared window.

## One bijection and its law

For a uniform incoming symbol, the labelled matrices are
$$
M_0=\frac{1}{48}\begin{pmatrix}21&3\\3&5\end{pmatrix},\quad
M_1=\frac{1}{48}\begin{pmatrix}5&3\\3&21\end{pmatrix},\quad
M_\bot=\frac{1}{48}\begin{pmatrix}12&4\\4&12\end{pmatrix}.
\tag{1}
$$
Rows and columns are ordered $0,1$ for the old and new active bits.
For a real label $a$, the second-column probability conditional on
that label and old bit $i$ is $i/2+a/4+1/8$. Its label probability
is $1/2$ if $a=i$ and $1/6$ otherwise. For $\bot$ those
probabilities are $i/2+1/4$ and $1/3$, respectively. This gives (1) by
multiplication and subtraction from each row's label probability. Each
label is possible and every entry is positive.

Under uniform $v$, the active bit is fair. Averaging (1) over that
bit gives the probabilities on $(a,z')$ as $(3,1)/12$ for $a=0$,
$(1,3)/12$ for $a=1$, and $(2,2)/12$ for $a=\bot$.
These are exactly the fractions of slots of each type in $V$.
Routing therefore gives uniform $v'$. Put $q=|A|=576$.
Every target $v'$ has exactly $q$ input pairs $(v,\alpha)$, because
the input pairs have equal weights. Order $V\times A$ lexicographically
using $0<1<\bot$ in the first component and increasing numerical order
elsewhere. On each fiber of the map $(v,\alpha)\mapsto v'$, set $b'$
to the element of $A$ with the same rank as the input's rank in its
fiber. The map $g(v,\alpha)=(v',b')$ is a fixed permutation of $V\times A$.

The global time step is
$$
(v_j(t+1),b_j(t+1))=g(v_j(t),b_{j-1}(t)).
\tag{2}
$$
Applying $g^{-1}$ at site $j$ recovers the old $v_j$ and the old
$b_{j-1}$; the old $b_j$ comes from site $j+1$. This gives a
measurable local inverse to (2). The shift rearranges independent bath
coordinates and leaves a product of uniform input pairs. The permutation
preserves the uniform law of each pair, so (2) preserves $\mu$.
The new local alphabet is $V$ with twelve states. One bath symbol of
size 576 per site per tick includes the request and routing components.
Both the shift direction and the site permutation are the same at all
sites and all ticks. The initial sites feeding the forward origin window
$0,\ldots,L$ lie in $[-L,0]$. One infinite product preparation
supports all finite windows, with a finite region for each window.

For freshness let $L_t$ consist of every register strictly left of
the origin and let $\alpha_t=b_{-1}(t)$, which arrives at the origin
on the transition from $t$ to $t+1$. At time zero $L_0$ has its
product law independent of $v_0(0)$, including at each fixed visible
root. If $L_t$ has that law independent of
$(v_0(0),\alpha_0,\ldots,\alpha_{t-1})$, the inputs for the next
left half-line use all its current persistent registers and all its bath
registers except $\alpha_t$, each once. They form independent uniform
pairs independent of $\alpha_t$ and the preceding tuple. Applying $g$
makes $L_{t+1}$ again independent of the enlarged tuple and preserves
its product law. Induction gives a uniform $\alpha_t$ independent of
the entire origin history through $t$, including the active registers.
Since $X_{t+1},Z_{t+1}$ depend on that symbol and $Z_t$, the same
labelled matrices govern all complete histories in every finite window.
Under $\mu$ stationarity translates these windows to any integer times.

## Two requests and a recoverable write

Fix the initial $v_0(0)$ with $Z_0=0$. Fix the first input's request
component at $D=1$ and mode at $K=2$, and fix its $U,W$.
Take $F=1$ in one branch and $F=0$ in the other. The first
response $X_1$ is respectively 0 and 1, and $Z_1=X_1$ in both cases.
For the second input use exactly the same symbol in both branches with
$D=1,F=1,K=0$, and the same $U,W$. Then $X_2=Z_1$ and
$Z_2=Z_1$, so the second response differs. These paired inputs have
positive mass under the one law. The second input can be kept literally
fixed when changing only the first incoming symbol in the initial
lattice state, because the update producing $b_{-1}(1)$ uses
$v_{-1}(0),b_{-2}(0)$, neither of which is changed. If the first mode
is instead held at $K=0$ in both branches, the same first flip change
still changes $X_1$, but leaves $Z_1=0$ and both second responses at
0. This is a control for the effect of the written carrier value.
Also, at any fixed current displayed $a$, both active bits have
nonempty slot sets. With the same next input $D=1,F=1$, varying the
slot across those sets changes the next response at the same current
display.

Immediately after the second response, the one-step record projection
is the displayed component of the old $v_0$ decoded from
$g^{-1}(v_0(2),b_0(2))$. By (2) it returns $X_1$ for every
trajectory, including both branches of the paired write. Successive
applications of the local inverse recover each earlier displayed symbol.
For a fixed accessible horizon $H=5$ use the log at time $t\le H$
whose entries are $X_t,X\circ T^{-1},\ldots,X\circ T^{-t}$, evaluated
at the current state, where $T$ is (2) and $X$ is the origin
display. This is a declared observation of the stored values in sites
$[0,t]$, through the specified projections. The protocol exposes
only those displayed values, and starts the log at time zero.
The decoded entries equal $X_t,\ldots,X_0$ on the trajectory, so the
log supplies exactly the history used in the freshness proof. The
same-present test compares current entries with the preceding entries
in the respective histories. The initial cut with product preparation
and the later conditional laws given the log use that same observation
protocol.

## History contrast and bound

Let $p_h=\Pr_\mu(Z_t=1\mid h)$ for a word $h=(x_0,\ldots,x_t)$
of positive mass. With $B(i,a)=\sum_jM_a(i,j)$ and row posterior
$\eta_h=(1-p_h,p_h)$, Bayes' rule and freshness give the recursions
$$
\eta_{ha}=\frac{\eta_hM_a}{\eta_h M_a\mathbf 1},\qquad
q_h=\Pr_\mu(X_{t+1}\in\cdot\mid h)=\eta_h B,\qquad
B=\begin{pmatrix}1/2&1/6&1/3\\1/6&1/2&1/3\end{pmatrix}.
\tag{3}
$$
The columns of $B$ are $0,1,\bot$. All finite words have positive
mass since the root law is uniform and all entries of $B$ are at
least $1/6$.

Take $h=(0,0)$ and $h'=(1,0)$, where $X_0$ and $X_1$ are the
responses to two consecutive requests in the stationary process. The
process has the same law if this two-response window starts after any fixed
tick. Their root bit probabilities are $1/4,3/4$. For the second label
0, (3) sends $p$ to $(3+2p)/(24-16p)$. The history masses are
$5/36,1/12$, and the two posterior bit masses are $7/40,3/8$.
The next symbol is 1 with probabilities $9/40,7/24$, respectively.
Its $\bot$ mass remains $1/3$ in both histories, so (3) gives
$$
\operatorname{TV}(q_h,q_{h'})=\frac{1}{15}.
\tag{4}
$$
This compares the complete law of the third attempt, including a tick
without a request.

For completeness the positive-matrix suffix bound can be proved directly
for this binary register. For a label matrix
$M=\begin{pmatrix}a&b\\c&d\end{pmatrix}$, put
$\Delta_M=|\log(ad/bc)|$ and
$\rho_M=\tanh(\Delta_M/4)$. In log odds $s=\log(p/(1-p))$,
the normalized update is
$$
f_M(s)=\log(b+de^s)-\log(a+ce^s).
$$
The diameter of its range is $\Delta_M$, from the two limiting
odds $b/a,d/c$ and monotonicity. Its derivative has absolute value
$$
\frac{|ad-bc|}{ab e^{-s}+ad+bc+cd e^s}
\ \le\ \frac{|\sqrt{ad}-\sqrt{bc}|}{\sqrt{ad}+\sqrt{bc}}
=\rho_M,
$$
where $ab e^{-s}+cd e^s\ge 2\sqrt{abcd}$.
For log odds at distance $\gamma$, the difference between the two
binary probabilities is at most $\tanh(\gamma/4)$.
Indeed, with $u>0$ the smaller odds and $R=e^\gamma$, the difference
is $(R-1)/(u^{-1}+1+R+Ru)$, bounded by
$(\sqrt R-1)/(\sqrt R+1)$.
Finally (3) has row distance $d(B)=1/3$, and the TV distance of
its two mixtures is exactly $d(B)|p_h-p_{h'}|$.

If two distinct histories have a common suffix of length
$1\le\ell\le t<H$, the first shared label bounds the log-odds distance
by its diameter and each later shared label contracts it by its own
$\rho_M$. Here the largest odds cross-ratio is $35/3$ for either
real label, and the $\bot$ cross-ratio is $9$. With
$\Delta=\log(35/3)$, $\rho=\tanh(\Delta/4)$, this yields the P8
form of the bound on the exact next read,
$$
\operatorname{TV}(q_h,q_{h'})
\le \frac13\,\tanh\!\left(\frac{\Delta}{4}\rho^{\ell-1}\right).
$$
At length one the right side is $\rho/3>1/15$, since
$\sqrt{35/3}>3/2$. The bound decreases geometrically with the length
of the shared suffix, with the same constants for any fixed finite
horizon. The comparison uses the complete last-tick law under the
single invariant preparation.

## Controls and reach

The passive P12(b) control can use its two-state site register $v$ and
four-symbol bath $b$, with
$c=v\oplus\mathbf 1_{\{b=0\}}$ and $g(v,b)=(c,b+c\bmod 4)$.
The same freshness induction shows a flip probability $1/4$ after
each complete history given its current $v$. When the entire
persistent register is the display, the same-present gap is zero.
Reading the full $v_0(t)$ in (2) has the same Markov property for its
own transition table. The coarser display is the projection used in
(3) and (4).

With a deterministic $(i,\alpha)\mapsto(a,z')$ and one uniform draw
from $q=4$ symbols, every labelled probability at a fixed $i$ is an
integer multiple of $1/4$. The P8 benchmark assigns
$M_0(0,0)=9/32$: a real 0 from old bit 0 has probability
$(1/2)(3/4)=3/8$, and the conditional new bit is 0 with probability
$1/4+1/4+(1/2)(1/2)=3/4$ in the benchmark keep, write and refresh
modes. Exact reproduction of that entry using a single uniform symbol
and a deterministic labelled operation requires $32\mid q$. This
construction tests the same structural criterion with the table (1).
It changes request frequency to $2/3$, the keep probability to
$1/2$, and ordinary refresh to $1/4$. Together these choices give
equal populations for all three displayed symbols and the finite
product cut above.

The conclusion is a mathematical realization on the declared
shift-and-permute class, with a prepared upstream bath, a chosen site
gate, and a declared inverse projection for retained records. The first
physical premise still to be supplied is an independently sourced
preparation and native update implementing the request, active write and
record access in one candidate observer. Physical measurement sourcing
remains NOT PASSED. The construction provides fixed-protocol laws; the
action laws of freely chosen or adaptive requests remain open.

[issue]: https://github.com/amaybaum/incompleteness/issues/1403
[authorization]: https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7006732977
[p12]: https://github.com/amaybaum/incompleteness/blob/4212e600752b77d4095cd8191915493c584cacb8/verification/audits/foundations/a1-p12-common-carrier-20261119/A1-P12-GLUE-1.md
[p8]: https://github.com/amaybaum/incompleteness/blob/62edb8168ceeaa1cb5c5e6e779217aed069d63b1/verification/audits/foundations/a1-p8-history-bridge-20261119/RESULT.md
