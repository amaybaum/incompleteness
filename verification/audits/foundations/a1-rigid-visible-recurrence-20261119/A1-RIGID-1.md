# A1-RIGID-1 — Observable recurrence and rooted P-indivisibility

**Status.** Conditional paper proof by Codex M, pending independent review.
The source base is `416f546d076299ab70d0c12df55808f930accddc` (`3.1.7`). The
issue and coordination comment identify the scope of this attempt. [#1394][scope]
· [#1169][coordination]

## Theorem

Let $(S,\Sigma,\mu)$ be a probability space and $T:S\to S$ a bimeasurable
bijection preserving $\mu$. Let $X:S\to V$ be a measurable readout into a finite
set with $|V|\ge2$, $C_a=X^{-1}(\{a\})$ and $p_a=\mu(C_a)>0$ for all $a$.
Use integer times $n\ge0$, $U f=f\circ T$ on $L^2(\mu)$, and $f_a=1_{C_a}$.
Suppose the joint forward orbit

$$
\bigl\{(U^n f_a)_{a\in V}:n\ge0\bigr\}
$$

has compact closure in the finite product of $L^2(\mu)$ spaces, with the
maximum of the component norms. Set

$$
\Gamma_n(a,b)=\frac{\mu(C_a\cap T^{-n}C_b)}{p_a}.
$$

1. For each $\varepsilon>0$ there is a finite integer $M\ge0$ such that for
   every integer $q\ge1$, some $n\in[q,q+M]$ satisfies
   $\max_{a\in V}(1-\Gamma_n(a,a))<\varepsilon$. In particular there is a
   strictly increasing sequence $n_k$ with $\Gamma_{n_k}\to I$.
2. If some $\Gamma_s$ is a non-permutation, then the rooted family is
   P-indivisible on a finite horizon $\{0,\ldots,n\}$ with $n>s$. More
   precisely, if $a\ne b$ and $m=\min(\Gamma_s(a,x),\Gamma_s(b,x))>0$ for
   any common column $x$, the pair $(s,n)$ witnesses strict total-variation
   revival for these same roots whenever $n>s$ and
   $(1-\Gamma_n(a,a))+(1-\Gamma_n(b,b))<m$. This holds for all sufficiently
   large members of the return sequence in part 1.

The matrices are row-stochastic because the preimages $T^{-n}C_b$ partition
$S$, and $\Gamma_0=I$. Here P-divisibility on a horizon $K$ means that for
every $0\le s<t\le K$ there is a row-stochastic $\Lambda_{s,t}$ satisfying
$\Gamma_t=\Gamma_s\Lambda_{s,t}$. It acts on the outcome index by right
multiplication. [CausalReadback.lean, definitions][cr-def]

For Main's common hidden-prior convention, take a declared measurable
identification $S=V\times H$ with $X(a,h)=a$ and invariant
$\mu=\nu\otimes\rho$, where $\nu(a)>0$ for all $a$ and $\rho$ is one
normalized probability on $H$. Then $p_a=\nu(a)$ and conditioning on $C_a$
gives $\delta_a\otimes\rho$ for each root. In those coordinates the formula
is exactly $\Gamma_n(a,b)=\rho\{h:X(T^n(a,h))=b\}$. An arbitrary measured
partition supplies the conditional law on each cell. Agreement with a
specified common hidden prior is a separate requirement on that law and the
root identification. [Main §2.3][main-root] · [A1-10 §3.3][ladder]

## Proof

Invariance makes $U$ an isometry, and the measurable inverse makes it
unitary. With the forward convention $U^n f_a=1_{T^{-n}C_a}$, where
$T^{-n}C_a$ denotes the preimage under $T^n$. The squared $L^2$ distance of
two indicators is the mass of their symmetric difference. Since both sets
here have measure $p_a$,

$$
\|U^n f_a-f_a\|_2^2
=\mu(C_a\triangle T^{-n}C_a)
=2\bigl(p_a-\mu(C_a\cap T^{-n}C_a)\bigr)
=2p_a(1-\Gamma_n(a,a)).
$$

This is REC-1's visible-rigidity identity in the declared sign convention.
[REC-1 Lemma 3.1 and Proposition 3.2][rec-identity]

Write $f=(f_a)_{a\in V}$, and let $W$ act as $U$ on each component. Set
$p_* = \min_a p_a>0$. By total boundedness choose a finite cover of the
orbit by balls of radius $\sqrt{2p_*\varepsilon}$ centered at orbit points
$W^{m_1}f,\ldots,W^{m_r}f$. Centers in the orbit can be obtained from a cover
by balls of half that radius by selecting an orbit point in each nonempty
ball. Set $M=\max_i m_i$. Given $q\ge1$, cover $W^{q+M}f$ by the ball with
center $W^{m_i}f$ and put $n=q+M-m_i$. Then $q\le n\le q+M$ and the
isometry gives

$$
\|W^n f-f\|_{\max}
=\|W^{q+M}f-W^{m_i}f\|_{\max}<\sqrt{2p_*\varepsilon}.
$$

The indicator identity proves the uniform diagonal estimate in part 1.
Apply it with $\varepsilon=1/k$ and $q>n_{k-1}$, starting with $n_0=0$.
Every diagonal tends to one and every off-diagonal is bounded by its row's
diagonal deficit, so $\Gamma_{n_k}\to I$ entrywise. The gap bound depends on
the model and the tolerance through the finite cover.

If the $|V|$ nonempty row supports of $\Gamma_s$ were pairwise disjoint,
each would consist of one of the $|V|$ columns and the matrix would be a
permutation. Thus a non-permutation gives $a,b,x,m$ as in part 2. Use total
variation $d(p,q)=\tfrac12\sum_y|p_y-q_y|$ for probability rows. At $s$,
$d(\Gamma_s(a,\cdot),\Gamma_s(b,\cdot))=1-\sum_y\min(\Gamma_s(a,y),\Gamma_s(b,y))\le1-m$.
At $n$, testing $\{a\}$ and using $\Gamma_n(b,a)\le1-\Gamma_n(b,b)$ gives

$$
d(\Gamma_n(a,\cdot),\Gamma_n(b,\cdot))
\ge\Gamma_n(a,a)-\Gamma_n(b,a)
\ge 1-(1-\Gamma_n(a,a))-(1-\Gamma_n(b,b)).
$$

This exceeds $1-m$ when the stated strict margin holds. Right multiplication
by a row-stochastic $\Lambda$ is a contraction because

$$
\frac12\sum_y\left|\sum_x(p_x-q_x)\Lambda(x,y)\right|
\le\frac12\sum_x|p_x-q_x|\sum_y\Lambda(x,y)=d(p,q).
$$

Thus no stochastic $\Lambda_{s,n}$ exists. This is the matrix predicate C4r
on a horizon containing $(s,n)$, with the same pair of roots at both times.
The estimate is A1-10's near-return argument (F11), also used in REC-1 under
its assumed rigidity (RIG). The compactness argument above supplies (RIG)
and gives bounded gaps for each fixed tolerance. [A1-10 §3.4][ladder]
· [REC-1 Proposition 3.4][rec-rig] · [CausalReadback.lean, contraction][cr-tv]
· [CausalReadback.lean, `c4r_implies_pIndivisible`][cr-no-go]

## Infinite-state example and Bernoulli control

On the circle $\mathbb T=\mathbb R/\mathbb Z$ use normalized Lebesgue measure
$\lambda$, and let $I_a=[a/2,(a+1)/2)$ for $a\in\{0,1\}$. Independently take
$B=\{0,1\}^{\mathbb Z}$ with the fair product law $\beta$ and the bilateral
shift $(\sigma b)_j=b_{j+1}$. On $\mathbb T\times B$ take
$T(\theta,b)=(\theta+\alpha,\sigma b)$, observing the half-circle label of
$\theta$. Translation and the shift preserve their respective probabilities
and are bimeasurable bijections. In the rooted coordinates

$$
(a,h,b)\longmapsto (a/2+h\bmod 1,b),\qquad 0\le h<1/2,
$$

the map to $\mathbb T\times B$ is bimeasurable and bijective. The probability
$\lambda\otimes\beta$ pulls back to $\mathrm{Unif}(\{0,1\})\otimes\rho$ for
the common hidden prior $\rho=(2\lambda|_{[0,1/2)})\otimes\beta$. The same
normalized law of $(h,b)$ prepares either root. The circle construction is
REC-1's rotation, with an independent invisible shift added to separate
the two Koopman conditions. [REC-1 Proposition 3.3][rec-rotation]

For a displacement $\zeta$, let $\|\zeta\|_{\mathbb Z}$ be the distance to
the nearest integer. The overlap of $I_a$ with $I_a-\zeta$ has length
$1/2-\|\zeta\|_{\mathbb Z}$. Translation reduces this to $a=0$, and symmetry
reduces to $\zeta\in[0,1/2]$, where the intersection has length $1/2-\zeta$.
The squared $L^2$ distance between indicators of translates of one
half-circle is therefore twice the circle distance
between the shifts. The translated pair of indicators is thus a continuous
image of the compact circle in the joint $L^2$ norm, establishing the required
relative compactness. Also, at every integer $n$,

$$
\Gamma_n=\begin{pmatrix}1-r_n&r_n\\r_n&1-r_n\end{pmatrix},\qquad
r_n=2\|n\alpha\|_{\mathbb Z},\qquad
d(\Gamma_n(0,\cdot),\Gamma_n(1,\cdot))=|1-2r_n|.
$$

Choose $\alpha=1/4+\eta$ with $\eta=\sqrt{2}/100$. Then

$$
\Gamma_1=\begin{pmatrix}1/2-2\eta&1/2+2\eta\\1/2+2\eta&1/2-2\eta\end{pmatrix},
\qquad
\Gamma_4=\begin{pmatrix}1-8\eta&8\eta\\8\eta&1-8\eta\end{pmatrix}.
$$

At $s=1$, column $0$ gives shared mass $m=1/2-2\eta>0$. At $n=4$, both
diagonal deficits are $8\eta$, and $16\eta<m$ since $\eta<1/50$. The two
row distances are $4\eta$ and $1-16\eta$, respectively. Thus the common
near-return witnesses C4r and P-indivisibility already on $\{0,\ldots,4\}$.
For every $n\ge1$, irrationality gives $r_n>0$, so there is no exact positive
identity time. Exact periodicity of the rooted family would repeat
$\Gamma_0=I$. Any one fixed finite bijective realization, with any shared
hidden prior, would also repeat $I$ by finite order. The infinite example
therefore cannot be obtained from a finite exact all-time rooted
realization by adding invisible coordinates. [Main §3.4][main-all-time]

On the same product system, the observable $g(\theta,b)=b_0-1/2$ has
$U^n g=b_n-1/2$. Distinct translates are orthogonal with squared norms
$1/4$, so their squared pairwise distances are $1/2$. This orbit is not
totally bounded, although the two chosen partition indicators have compact
orbit closure. Full Koopman almost periodicity (relative compactness for
every $L^2$ orbit) is strictly stronger.

**Bernoulli control.** Following A1-10 and REC-1, use $(B,\beta,\sigma)$ alone
with $X(b)=b_0$. The hidden coordinates indexed by $\mathbb Z\setminus\{0\}$
have one normalized
fair product law, independent of the root. Poincaré recurrence applies:
almost every point in each positive-measure event returns to it infinitely
often. At each fixed $n\ge1$ the new bit is independent of the root, so
$\Gamma_0=I$ and $\Gamma_n=A$ for $n\ge1$, where all entries of $A$ are
$1/2$. There is overlap at $s=1$, but diagonal deficits stay at $1/2$, and
the orbit of $1_{\{b_0=1\}}$ is pairwise separated in $L^2$ as above.
The divisors $\Lambda_{0,t}=A$ for $t>0$ and $\Lambda_{s,t}=I$ for
$0<s<t$ give P-divisibility at every horizon. Thus point-dependent
recurrence can coexist with P-divisibility and a fixed diagonal deficit.
[A1-10 control C−1][ladder-coin]
· [REC-1 Theorem 2.1][rec-poincare] · [REC-1 Bernoulli countercontrol][rec-bernoulli]

## Scope of the replacement

- Within the class of bimeasurable bijections with a normalized invariant
  law and a finite positive-mass partition, finite $S$ implies the compactness
  hypothesis: a finite permutation has some order $L$ with $U^L=I$.
  The infinite example proves strictness, also in the subclass with a
  common invariant product law and a non-permutation first step. In that
  class the conclusion of Main's one-step theorem transfers exactly as
  rooted P-indivisibility. The finite theorem gives the specific exact
  return $\Gamma_L=I$ and periodicity by iterating the microscopic
  permutation. Its overlap and history versions permit a common hidden
  prior without an invariant product law or positive sampling weight on
  every visible root. For example on $\{0,1\}^2$ the register swap with
  hidden prior $\delta_0$ gives both rows of $\Gamma_1$ equal to $\delta_0$
  and $\Gamma_2=I$. Every $\nu\otimes\delta_0$ with $\nu(1)>0$ assigns positive
  mass to $(1,0)$ and zero to its image $(0,1)$, so the product hypothesis
  fails for that prior with full visible support. The strict weakening
  concerns the recurrence premise within the invariant-law class.
  [Main §2.3][main-one] · [Main, history and overlap theorems][main-root]

- If two distinct positive-probability histories with the same endpoint
  are witnessed through time $k$ under the common hidden prior, then
  some $\Gamma_s$, $1\le s\le k$, is a non-permutation. Otherwise all
  those maps would be permutations and every history would be determined
  by its root with probability one, with the endpoint identifying that
  root. Part 2 then supplies a later indivisible horizon. The finite
  theorem's tighter bound $s\le\min(k,L-1)$ and its conclusion at the
  specified cycle endpoint use the exact return that finite order supplies.
  C4r here is a rooted marginal witness on horizons containing the
  exhibited pair. Accessible
  history readback and a physical write, store and read mechanism are
  separate claims about the history law and its implementation.
  [Main §2.3][main-root] · [REC-1 Proposition 6.1][rec-history]
  · [CausalReadback.lean, scope][cr-scope]

- Compactness is a condition on the whole indicator orbit and derives
  return even when no earlier overlap is assumed, for example when
  $X\circ T=X$. It is sufficient for the recurrence step. REC-1's
  overlapping-cylinder Bernoulli readout has P-indivisibility on
  $\{0,1,2\}$ and $\Gamma_n=A$ for all $n\ge3$, so it shows that even
  subsequential return, and hence compactness, is unnecessary for
  P-indivisibility by other routes. A model-dependent gap bound for near
  returns gives no common upper bound on the first indivisible horizon
  across the class: REC-1 Proposition 5.1 exhibits for every fixed $K$
  a finite model with a non-permutation first step and P-divisibility
  through $K$. The theorem concerns integer times. A laboratory timescale
  requires an independent link to a selected dynamics and accessible
  window. [REC-1 Proposition 3.5][rec-converse] · [REC-1 Proposition 5.1][rec-time]

- NR-1 provides a check on candidate applicability. Under its nonnilpotent
  coefficient hypothesis, infinite-lattice Haar law and full two-slice
  window readout, $\Gamma_t(a,a)\le1/2$ for every positive $t$, so the
  indicator orbits in that class fail joint relative compactness. The
  prime-field, nonzero-coefficient, lattice-convex-window revival exclusion
  is a separate result. The torus comparison gives equality of the rooted
  laws through $t$ under the prewrap condition
  $\operatorname{ext}_j(W)+2t<L$ in every coordinate, where $L$ is the torus
  side. A torus witness must occur at or beyond
  $(L-\max_j\operatorname{ext}_j(W))/2$ for F11 near-return under
  nonnilpotence, and for C4r or C4e under the prime-field, nonzero-coefficient
  and lattice-convex-window hypotheses. The mixed composite example
  $q=12$, $\alpha=2$ exhibits C4e while F11 fails. Finite visibility and
  finite causal support on a specified horizon (F3 and F4) give no
  compactness guarantee.
  [NR-1 Proposition 2.3][nr-rig]
  · [NR-1 Theorem 3.3 and Proposition 4.1][nr-compare]
  · [NR-1 §3, node 5][nr-exceptions] · [#1349 classification, rows 06–15][classification]

The result supplies a mathematical replacement for the recurrence input
to one theorem family. Its invariant preparation law, compact observable
orbits and earlier overlap are hypotheses of the application. Their
realization by a physically selected OI system, and access to a witnessing
horizon, require separate evidence. The conclusion concerns classical
rooted probabilities. Native quantum operations and physical measurement
sourcing have their own evidence requirements. A1 remains open and
unadopted, and physical measurement sourcing remains **NOT PASSED**.
[A1-NECESSITY, recurrence row][necessity]

[scope]: https://github.com/amaybaum/incompleteness/issues/1394
[coordination]: https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7004593019
[main-one]: https://github.com/amaybaum/incompleteness/blob/416f546d076299ab70d0c12df55808f930accddc/papers/Main.tex#L927-L982
[main-root]: https://github.com/amaybaum/incompleteness/blob/416f546d076299ab70d0c12df55808f930accddc/papers/Main.tex#L998-L1096
[main-all-time]: https://github.com/amaybaum/incompleteness/blob/416f546d076299ab70d0c12df55808f930accddc/papers/Main.tex#L4632-L4646
[ladder]: https://github.com/amaybaum/incompleteness/blob/416f546d076299ab70d0c12df55808f930accddc/verification/audits/foundations/a1-10-recurrence-premises/PREMISE-LADDER.md#L83-L105
[ladder-coin]: https://github.com/amaybaum/incompleteness/blob/416f546d076299ab70d0c12df55808f930accddc/verification/audits/foundations/a1-10-recurrence-premises/PREMISE-LADDER.md#L117-L128
[rec-poincare]: https://github.com/amaybaum/incompleteness/blob/416f546d076299ab70d0c12df55808f930accddc/verification/audits/foundations/rec1-recurrence-normalized-20261116/REC-1.md#L131-L147
[rec-identity]: https://github.com/amaybaum/incompleteness/blob/416f546d076299ab70d0c12df55808f930accddc/verification/audits/foundations/rec1-recurrence-normalized-20261116/REC-1.md#L228-L258
[rec-rotation]: https://github.com/amaybaum/incompleteness/blob/416f546d076299ab70d0c12df55808f930accddc/verification/audits/foundations/rec1-recurrence-normalized-20261116/REC-1.md#L260-L289
[rec-bernoulli]: https://github.com/amaybaum/incompleteness/blob/416f546d076299ab70d0c12df55808f930accddc/verification/audits/foundations/rec1-recurrence-normalized-20261116/REC-1.md#L291-L293
[rec-rig]: https://github.com/amaybaum/incompleteness/blob/416f546d076299ab70d0c12df55808f930accddc/verification/audits/foundations/rec1-recurrence-normalized-20261116/REC-1.md#L295-L322
[rec-converse]: https://github.com/amaybaum/incompleteness/blob/416f546d076299ab70d0c12df55808f930accddc/verification/audits/foundations/rec1-recurrence-normalized-20261116/REC-1.md#L324-L347
[rec-time]: https://github.com/amaybaum/incompleteness/blob/416f546d076299ab70d0c12df55808f930accddc/verification/audits/foundations/rec1-recurrence-normalized-20261116/REC-1.md#L454-L475
[rec-history]: https://github.com/amaybaum/incompleteness/blob/416f546d076299ab70d0c12df55808f930accddc/verification/audits/foundations/rec1-recurrence-normalized-20261116/REC-1.md#L503-L519
[cr-def]: https://github.com/amaybaum/incompleteness/blob/416f546d076299ab70d0c12df55808f930accddc/verification/lean-mathlib/OIBridge/CausalReadback.lean#L45-L68
[cr-tv]: https://github.com/amaybaum/incompleteness/blob/416f546d076299ab70d0c12df55808f930accddc/verification/lean-mathlib/OIBridge/CausalReadback.lean#L94-L113
[cr-no-go]: https://github.com/amaybaum/incompleteness/blob/416f546d076299ab70d0c12df55808f930accddc/verification/lean-mathlib/OIBridge/CausalReadback.lean#L132-L144
[cr-scope]: https://github.com/amaybaum/incompleteness/blob/416f546d076299ab70d0c12df55808f930accddc/verification/lean-mathlib/OIBridge/CausalReadback.lean#L10-L31
[nr-rig]: https://github.com/amaybaum/incompleteness/blob/416f546d076299ab70d0c12df55808f930accddc/verification/audits/foundations/nr1-near-return-20261116/NR-1.md#L165-L183
[nr-compare]: https://github.com/amaybaum/incompleteness/blob/416f546d076299ab70d0c12df55808f930accddc/verification/audits/foundations/nr1-near-return-20261116/NR-1.md#L237-L311
[nr-exceptions]: https://github.com/amaybaum/incompleteness/blob/416f546d076299ab70d0c12df55808f930accddc/verification/audits/foundations/nr1-near-return-20261116/NR-1.md#L335-L390
[classification]: https://github.com/amaybaum/incompleteness/blob/416f546d076299ab70d0c12df55808f930accddc/verification/audits/foundations/a1-finiteness-classes-20261117/CLASSIFICATION.md#L26-L35
[necessity]: https://github.com/amaybaum/incompleteness/blob/416f546d076299ab70d0c12df55808f930accddc/verification/audits/foundations/a1-necessity-20261117/ASSESSMENT.md#L29-L39
