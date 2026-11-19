# Forward native requests have stationary laws and label-dependent transition support

**Paper result.** Along the forward \(A\to B\to C\) schedule, the moving-frame
observation law is stationary. The declared four-state native register has a
time-independent transition with inputs independent of the complete prior
record and active-register history. Every observed word in the three-tick
window has positive mass. Each outcome-labelled matrix nonetheless has zero
columns. Strict matrix support is the first failed hypothesis for this
register. For this schedule and gated readout, it is proved to fail only
for finite registers of the P8 operation form that satisfy (N): the
tick-2 native inputs are independent of the register, the complete
accessible past and the two frontier bits \((m_1,a_1)\). Every such
register determines the displayed label.

**Scope and evidence.** Worker P, 2026-11-19. Paper-only proof for
[Issue #1411][issue]. The [separate non-author mathematical
review][review] returned ACCEPT on Worker P's sections at
0cd60a76e1f8d6832a51e73f7ea31f6e1a3be69f. The sections “Every
native-fresh register determines its label” and “Exact arithmetic
check” were added afterwards by the Main thread, the writer under the
[2026-11-19 staffing record][staffing], against main at
0d02d8d3b6a53a43168eabead12e1ff675a4d048; they are pending independent
review. Alex Maybaum's “Approved”
is relayed in the [2026-11-19 owner decision][authority]. The
[Codex PRs assessment][readiness] records readiness and the disposition
of the off-main P8 attribution. The drafting and published-rule source
pin is adf41d3f833692e33628008d3c82ce3779f343e0. The reviewed
[neighboring-site proof][predecessor] locates the comparison reproduced
below. The [P8 draft][p8] records the origin of the structural test, and
its [preservation candidate][p8-preservation] carries the same condition.
The P8 record and its structural condition are on main as
[landed][p8-main]; the neighboring-site proof is off main and provides
provenance. The recurrence, law,
control and matrix condition used in the argument are given explicitly here.

**Goal link (§A.47).** Test whether the neighboring response from #1409 can
satisfy P8 under a stationary native read and request schedule.

## Stationary moving-frame readout

Let \(e=e_1\), let \(N(i)\) be the six nearest neighbors of \(i\) in
\(\mathbb Z^3\), and use the binary specialization of the [published
rounded-cubic rule][rule]. If \(x_t\) is the field slice at time \(t\),
then
\[
g_i(y)=\left\lfloor\frac{1+\sum_{j\in N(i)}y(j)}{3}\right\rfloor\bmod 2,
\qquad
x_{t+1}(i)=g_i(x_t)\oplus x_{t-1}(i),
\]
where \(\oplus\) denotes addition modulo two. The value of \(g_i\) is 1
exactly for stencil sums 2, 3 and 4. The reference law \(\mu\) on a pair
of consecutive slices makes all bits on both slices independent and fair.
The update \(F(x,y)=(y,g(y)\oplus x)\) preserves this law. For fixed \(y\),
each finite list of output bits in \(g(y)\oplus x\) is masked by distinct
independent fair bits from \(x\). Its conditional distribution is the
same for every \(y\). The inverse is \(F^{-1}(y,z)=(g(y)\oplus z,y)\).

Use the three ticks \(t=0,1,2\), with receivers \(A=0\), \(B=e\),
\(C=2e\), respectively. At tick \(t\), the request is the pre-update bit
one step ahead of the receiver and the field response is the newly
computed bit at the receiver. The complete readout is
\[
m_t=x_{t-1}((t+1)e),\qquad a_t=x_t(te),\qquad
L_t=\begin{cases}
\bot,&m_t=0,\\
a_t,&m_t=1 .
\end{cases}
\]
In particular the three request locations are \(e,2e,3e\) on the
respective pre-update slices. The accessible history through tick \(t\)
is \((L_0,\ldots,L_t)\), including every no-request label. Its entries
are projections of the two current slices through the inverse update.
In this window each projection uses a finite neighborhood by locality
of \(F^{-1}\). The oldest and newest entries can therefore refer to the
same native trajectory without supplying a separate field or log as an
input to the update.

For \(\tau x(j)=x(j+e)\), write
\[
Y_t=(\tau^t x_{t-1},\tau^t x_t),\qquad T=\tau F .
\]
Translation acts on both slices, commutes with \(F\), and preserves
\(\mu\). Consequently \(Y_{t+1}=TY_t\) with \(T\) preserving \(\mu\).
The readout is one fixed function of \(Y_t\): the older bit at \(e\)
gates the newer bit at 0. The same function read on an invariant orbit
has identical joint laws on time-translated blocks. This establishes
stationarity of the observations in the moving frame. The window
\(t=0,1,2\) selects three successive observations from that law.

## Native active register and conditional freshness

Use \(Z_t=(m_t,a_t)\) with state space \(\{0,1\}^2\).
For the next receiver at \((t+1)e\), the older subtracted bit is
\(m_t\), and its trailing neighbor contributes \(a_t\).
The remaining five pre-update stencil inputs, all on slice \(x_t\),
are the next request \(r=x_t((t+2)e)=m_{t+1}\) and the four transverse
bits at \((t+1)e\pm e_2,(t+1)e\pm e_3\).
Denote this five-bit vector by \(\xi_{t+1}\), and let \(S\) be its
transverse sum. The transition is
\[
b=\left(\left\lfloor\frac{1+a_t+r+S}{3}\right\rfloor\bmod2\right)
   \oplus m_t,\qquad
Z_{t+1}=(r,b),\qquad
L_{t+1}=\begin{cases}\bot,&r=0,\\ b,&r=1.\end{cases}
\]

To check freshness against the full history, let \(\mathcal F_t\) be
generated by the entire older slice \(x_{t-1}\) and the coordinates of
\(x_t\) with first coordinate at most \(t\). This is a conditioning
sigma field for the proof. The active register and readout still use
the specified finite projections. Every \(Z_s,L_s\) for \(0\le s\le t\)
is \(\mathcal F_t\)-measurable. At \(s=t\) this holds by their definitions.
For an earlier time \(u\le t-2\), a projected bit \(x_u(i)\) has potential
dependence on the newer slice \(x_t\) only within distance \(t-u-2\)
of \(i\) in the nearest-neighbor lattice metric. Indeed the first
backward step \(x_{t-2}(i)=g_i(x_{t-1})\oplus x_t(i)\) uses only one
coordinate of \(x_t\), and each further step adds at most one spatial
step to its dependence region. The slice \(x_{t-1}\) itself already
belongs to \(\mathcal F_t\). Thus for \(m_s=x_{s-1}((s+1)e)\) with
\(s<t\), the latest-slice dependence has first coordinate at most
\((s+1)+(t-s-1)=t\). For \(a_s=x_s(se)\) with \(s\le t-2\), the bound
is \(s+(t-s-2)=t-2\), and \(a_{t-1}\) is on the older slice.

The five coordinates of \(\xi_{t+1}\) lie strictly ahead of the
half-space of \(x_t\) in \(\mathcal F_t\). By the pair product law at time
\(t\), their joint conditional law given \(\mathcal F_t\) is uniform on
\(\{0,1\}^5\). In particular it is uniform conditional on all earlier
active registers and displayed labels, including the current register
and label. These are bits of the native field.

## Matched-input \(A\to B\) control

Write \(u=x_{-1}\), \(v=x_0\), \(w=x_1\), and let \(D=e_2\). For
each \(a\in\{0,1\}\), take the following cylinder in the product pair
\((u,v)\).

| Slice | Prescribed bits |
| --- | --- |
| \(u\) | \(u(B)=1\), \(u(D)=a\), all four other neighbors of \(A\) equal to 0 |
| \(v\) | \(v(A)=a\), \(v(C)=1\), all four other neighbors of \(B\) equal to 0 |

Each cylinder has mass \(2^{-12}\). The precursor bit at \(A\) is
\(x_{-2}(A)=g_A(u)\oplus v(A)=a\oplus a=0\).
The first request and precursor at \(A\) are fixed. Changing \(u(D)\)
changes the written label \(v(A)\). At \(B\) the request \(v(C)=1\),
the subtracted bit \(u(B)=1\), and the four transverse inputs are fixed.
As the sum at \(B\) is \(1+a\), the response is \(w(B)=1-a\).
The first label is retained in the projection from \((v,w)\): the
written bit \(v(A)\) is in the older slice and its request bit
\(u(B)=g_B(v)\oplus w(B)\) is recovered locally.

## Full history law

Given \(m,a,r\), the probability that the next stencil value is 1 is
\[
p(a,r)=
\begin{cases}
11/16,&a=r,\\
14/16,&a\ne r.
\end{cases}
\]
Indeed for \(a+r=0,1,2\), the allowed values of the sum of four fair bits
are respectively \(\{2,3,4\}\), \(\{1,2,3\}\), and \(\{0,1,2\}\).
The corresponding binomial counts are \(11,14,11\) out of 16.
Multiplying the conditional response probabilities by the fair request
probability gives the following transition matrix \(K\) in state order
\((0,0),(0,1),(1,0),(1,1)\):
\[
K=\frac1{32}
\begin{pmatrix}
5&11&2&14\\
2&14&5&11\\
11&5&14&2\\
14&2&11&5
\end{pmatrix}.
\]
At the first tick \(Z_0\) is uniform with row distribution
\(\lambda=(1,1,1,1)/4\). For \(\ell\in\{0,1,\bot\}\), let \(D_\ell\)
be the diagonal matrix with entry 1 in the states that display \(\ell\)
and 0 elsewhere. Set \(M_\ell=K D_\ell\). By conditional freshness, all
word probabilities in the declared window, including their prefixes,
are
\[
\Pr(L_0=\ell_0,\ldots,L_k=\ell_k)
=\lambda D_{\ell_0}M_{\ell_1}\cdots M_{\ell_k}\mathbf{1},
\qquad 0\le k\le 2 .
\]
At \(k=0\) there are no \(M_\ell\) factors. For any history of positive
mass, the row before multiplication by \(\mathbf 1\), normalized by
that mass, is the posterior law of \(Z_k\). Multiplication by
\(M_\ell\mathbf 1\) then gives the conditional probability of the next
label \(\ell\).

The first-label marginal in order \(0,1,\bot\) is
\((1/4,1/4,1/2)\). The second rows are as follows.

| \(L_0\) | \(\Pr(L_1=0\mid L_0)\) | \(\Pr(L_1=1\mid L_0)\) | \(\Pr(L_1=\bot\mid L_0)\) |
| --- | ---: | ---: | ---: |
| \(0\) | \(7/16\) | \(1/16\) | \(1/2\) |
| \(1\) | \(11/32\) | \(5/32\) | \(1/2\) |
| \(\bot\) | \(7/64\) | \(25/64\) | \(1/2\) |

The two real first labels give second rows at total-variation distance
\(3/32\). Conditional on the raw first bit \(v(A)\) alone, \(u(B)\)
is fair and independent of \(v\), so the second field response is masked
and the second row is \((1/4,1/4,1/2)\) for either raw bit.

For the third tick, if \(L_1\) is real, \(Z_1=(1,L_1)\) and the
conditional law is the second row indexed by that same real label,
regardless of \(L_0\). If \(L_1=\bot\), then \(m_1=0\). The posterior
probabilities of \(a_1=1\) for \(L_0=0,1,\bot\) are respectively
\(5/16,1/8,25/32\), obtained by restricting the transitions to the first
two columns of \(K\) and dividing by \(1/2\). For such a posterior
probability \(\theta\), the next real label 1 has probability
\(\frac12(14/16-3\theta/16)\). The resulting rows are

| Complete history \((L_0,L_1)\) | \(\Pr(L_2=0\mid L_0,L_1)\) | \(\Pr(L_2=1\mid L_0,L_1)\) | \(\Pr(L_2=\bot\mid L_0,L_1)\) |
| --- | ---: | ---: | ---: |
| \((0,\bot)\) | \(47/512\) | \(209/512\) | \(1/2\) |
| \((1,\bot)\) | \(38/512\) | \(218/512\) | \(1/2\) |
| \((\bot,\bot)\) | \(139/1024\) | \(373/1024\) | \(1/2\) |

In particular the first two histories in this last table have the same
present \(\bot\) and a third-label total-variation gap of \(9/512\).
Every history in the window has positive mass. The no-request probability
is \(1/2\) given each supported prior history, and both real labels have
positive conditional probability because each row of \(K\) gives
positive weight to both \(r=1\) states.

## Strict outcome-labelled support

The structural test requires each possible label matrix of a fixed
operation with fresh input to be strictly positive in every entry.
A label that is impossible can have an identically zero matrix.
For the declared register, \(M_\bot\) has positive entries in columns
\((0,0),(0,1)\) and zeros in columns \((1,0),(1,1)\). The matrix
\(M_0\) has positive entries only in column \((1,0)\), and \(M_1\)
only in column \((1,1)\). Each has some positive entries and some
zero entries. The unconditional \(K\) is strictly positive, and
the row sums of each \(M_\ell\) are strictly positive, while the
matrices themselves fail the full transition rectangle requirement.

The same support incompatibility applies to any refinement of this
register from which both \(m_t\) and \(a_t\) are decoded from the target
active state alone. The label then restricts the target to the states
decoding to that label. Since the stationary law gives positive mass
to all three labels, each nonzero label matrix must exclude some
target states. This obstruction is scoped to the displayed native
register and such refinements. The next section extends it to every
finite register whose tick-2 native inputs are fresh in the sense (N)
stated there. Physical preparation, request production
and executing read coupling remain open under [#866][physical].

## Every native-fresh register determines its label

This section concerns an arbitrary finite register, not only
\((m_t,a_t)\). Let \(Z_0,Z_1,Z_2\) be random variables with values in a
finite set \(\mathcal Z\), defined on the same probability space as the
field pair \((x_{-1},x_0)\) under \(\mu\). Assume the P8 structural
condition on the window: one map \(\Phi\) and inputs \(\eta_1,\eta_2\)
of one law \(\nu\) give \((L_s,Z_s)=\Phi(Z_{s-1},\eta_s)\) for
\(s=1,2\), with \(\eta_s\) independent of
\((Z_0,\ldots,Z_{s-1},L_0,\ldots,L_{s-1})\). Write
\(M_\ell(i,j)=\nu\{\eta:\Phi(i,\eta)=(\ell,j)\}\) and
\(B(i,\ell)=\sum_j M_\ell(i,j)\). The abstract inputs \(\eta_s\) need
not be native bits.

Let \(\xi_2\) be the five native inputs of tick 2: the bits of \(x_1\)
at \(3e\), \(2e\pm e_2\) and \(2e\pm e_3\). The first of them is the
request \(m_2\). The hypothesis is

**(N)** \(\xi_2\) is independent of \((Z_1,L_0,L_1,m_1,a_1)\).

(N) holds whenever \(Z_1\) is measurable with respect to \(x_0\) and the
coordinates of \(x_1\) other than the five coordinates of \(\xi_2\). A
register written in coordinates of \(x_{-1}\) need not qualify: for
example \(x_{-1}(3e)=g_{3e}(x_0)\oplus m_2\). Indeed \(L_0,L_1,m_1,a_1\) are
\(\mathcal F_1\)-measurable by the freshness section, \(\mathcal F_1\)
does not contain those five coordinates, and the pair law of
\((x_0,x_1)\) is the product law. In particular (N) holds for every
\(\mathcal F_1\)-measurable register, including the declared one.

**Claim.** Under the structural condition and (N), there is a function
\(\lambda\) on the states of positive mass with \(L_1=\lambda(Z_1)\)
almost surely. For each \(\ell\in\{0,1,\bot\}\), the table \(M_\ell\)
has a zero entry and is not identically zero. Hence no finite register
satisfying (N) meets the P8 strict support condition on this schedule
and readout.

**Proof.** The next label is a fixed function of \((m_1,a_1,\xi_2)\):
\(L_2=\bot\) if \(m_2=0\), and otherwise
\(L_2=g_{2e}(x_1)\oplus m_1\), whose stencil is
\(a_1+m_2\) plus the four transverse bits. Let
\(\beta(m,a)=\Pr(L_2=1\mid m_1=m,a_1=a)=K((m,a),(1,1))\). From the
last column of \(K\),
\[
\beta(0,0)=\tfrac{14}{32},\quad \beta(0,1)=\tfrac{11}{32},\quad
\beta(1,0)=\tfrac{2}{32},\quad \beta(1,1)=\tfrac{5}{32}.
\]
By (N),
\(\Pr(L_2=1\mid Z_1,L_0,L_1,m_1,a_1)=\beta(m_1,a_1)\), so
\[
\Pr(L_2=1\mid Z_1,L_0,L_1)=\mathbb E[\beta(m_1,a_1)\mid Z_1,L_0,L_1].
\]
By the structural condition at \(s=2\), the left side equals
\(B(Z_1,1)\). Fix \(z\) with \(\Pr(Z_1=z)>0\) and consider the atoms
\(\{Z_1=z,L_0=\ell_0,L_1=\ell_1\}\) of positive mass. On an atom with
\(\ell_1=\bot\), \(m_1=0\), and the conditional expectation is a convex
combination of \(14/32\) and \(11/32\), hence at least \(11/32\). On an
atom with real \(\ell_1\), \(m_1=1\) and \(a_1=\ell_1\), and the value is
\(\beta(1,\ell_1)\in\{2/32,5/32\}\). Every atom with the same \(z\) has
the common value \(B(z,1)\). Since \(11/32>5/32\) and
\(2/32\ne5/32\), all positive-mass atoms with \(Z_1=z\) share one
\(\ell_1\), which defines \(\lambda(z)\).

Take \(i\) with \(\Pr(Z_0=i)>0\). The structural condition at \(s=1\)
gives \(M_\ell(i,j)=\Pr(L_1=\ell,Z_1=j\mid Z_0=i)\). This vanishes when
\(\Pr(Z_1=j)=0\), and when \(\Pr(Z_1=j)>0\) with \(\lambda(j)\ne\ell\).
The labels of tick 1 have marginal \((1/4,1/4,1/2)\), obtained by
averaging the second-label rows above against the first-label marginal.
Hence \(\sum_i\Pr(Z_0=i)\,M_\ell(i,\cdot)\mathbf 1=\Pr(L_1=\ell)>0\), so
\(M_\ell\ne0\). A different label also has positive mass, so some \(j\)
of positive mass has \(\lambda(j)\ne\ell\), and \(M_\ell(i,j)=0\).
\(\square\)

**Mechanism and scope.** The proof uses the gated readout and the
three-tick window, and does not use the stationarity of the moving
frame. The request bit of tick 1 is the older bit that the tick-2
receiver subtracts. The label reveals it, through \(\bot\), and after a
request it also reveals the written bit that enters the next stencil.
Both change the next real-label probability, so a register that screens
the next label from the present label must determine the present
label. The matched-input control exhibits the same two roles at
\(A\to B\): \(u(B)\) is both the first request and the bit subtracted
at \(B\), and the written \(v(A)\) enters the stencil at \(B\).

The argument does not apply to a register that violates (N), that is,
one correlated with the tick-2 native inputs given the complete
accessible past and \((m_1,a_1)\); a register that reads the next
request bit is an example. Whether some such register has strictly
positive operation tables for this schedule is not decided here.
Other read schedules and readouts are outside this test.

## Exact arithmetic check

The following script recomputes \(K\) from the reduced register
transition over all \(4\times32\) register and input values, the column
\(\beta\), the two separations used in the proof, and the second- and
third-label rows. It uses exact rational arithmetic. It checks the
arithmetic from the reduced transition only. It is not an independent
control of the reduction from the field.

```python
from fractions import Fraction as Fr
from itertools import product
S = [(0, 0), (0, 1), (1, 0), (1, 1)]           # register (m, a)
g = lambda s: ((1 + s) // 3) % 2               # binary rounded-cubic stencil value
lab = lambda z: 'bot' if z[0] == 0 else z[1]   # displayed label of a target state
K = {z: {w: Fr(0) for w in S} for z in S}
for (m, a) in S:                               # all 32 fresh inputs (r, transverse bits)
    for r, *tr in product((0, 1), repeat=5):
        K[(m, a)][(r, g(a + r + sum(tr)) ^ m)] += Fr(1, 32)
print("32K:", [[int(32 * K[z][w]) for w in S] for z in S])
beta = {z: K[z][(1, 1)] for z in S}            # Pr(next label = 1 | m, a)
print("beta:", [str(beta[z]) for z in S])
lo_bot = min(beta[(0, 0)], beta[(0, 1)])
hi_real = max(beta[(1, 0)], beta[(1, 1)])
print("min beta(0,.) > max beta(1,.):", lo_bot > hi_real,
      "| beta(1,0) != beta(1,1):", beta[(1, 0)] != beta[(1, 1)])
def step(v, l):                                # row vector times M_l = K D_l
    return {w: (sum(v[z] * K[z][w] for z in S) if lab(w) == l else Fr(0)) for w in S}
labels = (0, 1, 'bot')
def nxt(v):
    tot = sum(v.values())
    return [str(sum(step(v, l).values()) / tot) for l in labels]
for l0 in labels:
    v0 = {z: (Fr(1, 4) if lab(z) == l0 else Fr(0)) for z in S}
    print("L0 =", l0, "| L1 row:", nxt(v0), "| L2 row after L1=bot:", nxt(step(v0, 'bot')))
```

Output under Python 3:

```text
32K: [[5, 11, 2, 14], [2, 14, 5, 11], [11, 5, 14, 2], [14, 2, 11, 5]]
beta: ['7/16', '11/32', '1/16', '5/32']
min beta(0,.) > max beta(1,.): True | beta(1,0) != beta(1,1): True
L0 = 0 | L1 row: ['7/16', '1/16', '1/2'] | L2 row after L1=bot: ['47/512', '209/512', '1/2']
L0 = 1 | L1 row: ['11/32', '5/32', '1/2'] | L2 row after L1=bot: ['19/256', '109/256', '1/2']
L0 = bot | L1 row: ['7/64', '25/64', '1/2'] | L2 row after L1=bot: ['139/1024', '373/1024', '1/2']
```

The values agree with \(K\), the two history tables and the column
\(\beta\) above (\(19/256=38/512\), \(109/256=218/512\)).

[issue]: https://github.com/amaybaum/incompleteness/issues/1411
[review]: https://github.com/amaybaum/incompleteness/pull/1412#pullrequestreview-5981021883
[staffing]: https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7019013461
[p8-main]: https://github.com/amaybaum/incompleteness/blob/0d02d8d3b6a53a43168eabead12e1ff675a4d048/verification/audits/foundations/a1-p8-history-bridge-20261119/RESULT.md#L13-L19
[authority]: https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7014855892
[readiness]: https://github.com/amaybaum/incompleteness/pull/1410#issuecomment-7017201143
[rule]: https://github.com/amaybaum/incompleteness/blob/adf41d3f833692e33628008d3c82ce3779f343e0/papers/SM.md#L294
[predecessor]: https://github.com/amaybaum/incompleteness/blob/5551039a1c0f622d17b07497b2d752d5a2bcb863/verification/audits/foundations/p8-p12-neighbor-response-20261119/RESULT.md
[p8]: https://github.com/amaybaum/incompleteness/blob/62edb8168ceeaa1cb5c5e6e779217aed069d63b1/verification/audits/foundations/a1-p8-history-bridge-20261119/RESULT.md#L9-L29
[p8-preservation]: https://github.com/amaybaum/incompleteness/blob/645ccc669290a7529498cd256b2101dcf836772c/verification/audits/foundations/a1-p8-history-bridge-20261119/RESULT.md#L9-L29
[physical]: https://github.com/amaybaum/incompleteness/issues/866
