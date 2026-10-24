# From native symbols to a flux law: a conditional route and a timing witness

**Exploratory handoff v1, 2026-10-22. Read-only investigation of PR #885.**

This is a new kinematic candidate diagnostic, not further numerical refinement
of C-SPH-1 and not a new preregistered acceptance experiment. No repository
files, status, freeze, or accepted result are changed. The construction below
is not claimed to be a physical instrument implemented by the native wave.

## 1. Reading the independent review

The published review is at
[`1ca2cf6a`](https://github.com/amaybaum/incompleteness/commit/1ca2cf6a6f0f4f45c0b2766875f6731e89143ed8),
under `mc-node9/design/owner-checks/report11/`. Its confirmation of the native
resource lemma and its bounded-history extension are consistent with the
written argument.

Two scope refinements matter:

- For history u(-1-s),...,u(0), use the shifted initial pair
  (u(-1-s),u(-s)) and horizon K+s. Invariance of uniform counting then gives
  the stated result when L>2(K+s). This is a sufficient condition. Violating
  it ends this guarantee; it does not imply predictability. The review's own
  L=9, K=4 tests with positive s demonstrate that distinction. The L=3 return
  is a particular counterexample, not a universal threshold theorem.
- The 186 separation cases use offsets with coordinates in {0,1,2,3} and
  L1 norm 1..4. They omit the offsets (4,0,0) and its permutations in that
  parameter sweep. Signs can be related by cubic symmetry, but the phrase
  "every offset at L1 distance 1 to 4" should be narrowed to the actual set.
  The separate axial scan has different parameters. None of this changes the
  original sufficient separation theorem or the reported successful ranks.

No additional separation or history sweep was run for this handoff. The next
question remains the emission/readout map.

## 2. A specified kinematic candidate

Use the prime-two version of the native-wave resource lemma, with nonzero
coupling alpha=1. Its fresh symbols are fair bits. The general frontier proof
applies over F_2 as over other prime fields. The horizon, prior and history
conditions of that lemma remain in force; the full product prior is not an
energy-shell prior.

For a positive odd n, take 3n independent fresh bits, identify each bit with
epsilon=+1 or -1, and form three equal block sums

\[
S_n=(S_x,S_y,S_z),\qquad S_i=\sum_{j=1}^n\epsilon_{ij}.
\]

**Additional map, not derived from OI:** interpret the equal block averages as
a physical velocity V=5 S_n/n. Draw an independent depth label D uniformly
from {1,...,M}, where M is the smallest power of two at least 9n. Exactly
log2(M) fresh bits supply D. Set the initial normal depth to D/n, and stipulate
straight motion toward a plane of unit normal w. Count a crossing within one
time unit as success.

For the menu X,Y,Z,R, with R=(4/5,3/5,0), the quantity

\[
P_w=5w\cdot S_n
\]

is an integer. A crossing occurs exactly when 1<=D<=P_w, and its time offset is
T=D/P_w. For X, P_X=5 S_x; for R, P_R=4 S_x+3 S_y. All possible normal speeds
satisfy |P_w|<=5 sqrt(3)n<9n<=M, so the depth range does not truncate positive
crossings. The emitted direction is lambda=S_n/|S_n|. Odd n removes all sign
ties for the four menu axes, as well as zero speed.

This is a full-plane crossing rule, not an implemented finite aperture or
spherical collector. Velocity averaging, real coordinate interpretation,
straight motion, clock readout, and a physical mechanism for creating these
carriers are supplied here. The sampler does not derive them from the wave
update and does not include backreaction. The goal is to isolate what this
specific geometric map would imply if supplied.

Independent fresh blocks are used for successive trials. They can fit a
finite native source by enlarging its lattice/horizon budget to cover every
bit consumed, including depth labels and prior observation history. Nothing
here assumes freshness beyond the proved finite budget.

## 3. The limiting angular law follows conditionally

Counting the permitted depths gives a success weight (P_w)_+ for each S_n.
Thus, for a set of directions A,

\[
\Pr(\lambda\in A\mid\mathrm{success},w)
=\frac{\mathbb E[(w\cdot S_n)_+\,1_{S_n/|S_n|\in A}]}
        {\mathbb E[(w\cdot S_n)_+]}.
\]

The factor w dot S was not chosen to fit a quantum probability: it is the
number of initial depths that cross the plane. Cosine weighting of an
isotropic incident flux is standard kinetic geometry, not a novel OI effect;
see, for background, *The correct and incorrect generation of a cosine
distribution of scattered particles for Monte-Carlo modelling of vacuum
systems* ([primary paper](https://www.sciencedirect.com/science/article/pii/S0042207X02001732)).
The finite counting argument above is independent of that citation.

The characteristic function of S_n/sqrt(n) is
product_i cos(t_i/sqrt(n))^n, which tends to exp(-|t|^2/2). Therefore the limit
is the isotropic three-dimensional standard Gaussian G. Its direction is
uniform on the sphere and independent of its radius. Weighting by
(w dot G)_+=|G|(w dot lambda)_+ and cancelling the radial factor gives

\[
\mu_w(d\lambda)=\frac{(w\cdot\lambda)_+}{\pi}\,d\Omega.
\]

The passage to these weighted expectations is justified: the second moments
of S_n/sqrt(n) are uniformly bounded, hence the linear weights are uniformly
integrable. Fixed hemisphere boundaries have Gaussian probability zero.
Consequently the fixed-menu read probabilities converge to

\[
\mu_w\{a\cdot\lambda>0\}=\frac{1+a\cdot w}{2}.
\]

This is a weak angular limit and convergence of fixed hemisphere tests. It
is not convergence in total variation of the hidden direction distribution:
each finite-n distribution is atomic whereas the limiting spherical law is
continuous. It is also not a full-record convergence theorem.

There is a resource cost: M is of order n while the expected positive normal
projection is of order sqrt(n), so success per trial falls as n^(-1/2).
Maintaining a nonvanishing completion probability as n grows requires a
growing trial budget. No fixed-throughput or fixed-horizon limit is claimed.

The equal averaging rule is an explicit structural candidate, more specific
than an arbitrary probability decoder. Nevertheless, the native wave does not
yet select it as a velocity map or implement the stipulated ballistic carrier.

## 4. Finite angular diagnostics

The checker uses exact binomial multiplicities
Pr(S_i=2k-n)=binom(n,k)/2^n. For the quantities shown, S_z integrates out.
All underlying calculations are rational; displayed decimals are summaries.

| n | P(R+ given X emission) | P(X+ given R emission) |
| --- | --- | --- |
| 1 | 1.000000000 | 1.000000000 |
| 3 | 0.937500000 | 0.932432432 |
| 7 | 0.913281250 | 0.912504028 |
| 15 | 0.900039566 | 0.905411714 |
| 31 | 0.898054012 | 0.902568017 |
| 63 | 0.898957278 | 0.901261268 |
| 127 | 0.899481770 | 0.900625280 |

The limiting comparison value is 9/10. It is not used in sampling or in
selecting weights. There is no acceptance tolerance attached to this table.

## 5. Exact crossing timestamps expose an arithmetic record

Suppose the public record returns the exact rational crossing time T=D/P_w.
Let E be the event that the denominator of T in lowest terms is divisible by
5. The test depends only on the timestamp, not on the hidden station or impact.

Write a positive P as 5^k b, with 5 not dividing b. Among the P successful
depth labels, T has denominator divisible by 5 unless D is a multiple of
5^k. Exactly P-b depths therefore satisfy E. This gives exact finite sums for
Pr(E given success,w).

The X station has P_X=5 S_x, while the R station has P_R=4 S_x+3 S_y. Their
timestamp arithmetic retains the orientation difference even as their coarse
angular probabilities approach the desired values. At n=63,

| Preparation axis | Pr(E given success) |
| --- | --- |
| X | 0.834554985 |
| R | 0.167339144 |

This conditional difference alone is not used as the full-record TV witness.
To include every failure, allow at most m=256 fresh trials, stopping at the
first crossing. Here M=1024. Each trial has success probability p_w, as fixed
by its exact depth count. The probability of the full-record event "a success
occurs by trial m and its timestamp satisfies E" is exactly

\[
\left[1-(1-p_w)^m\right]\Pr(E\mid\mathrm{success},w).
\]

The results are:

| Quantity | X axis | R axis |
| --- | --- | --- |
| Success by trial 256 | 0.981776369544 | 0.981543683592 |
| Full-record event probability | 0.819346363181 | 0.164250679444 |

Hence the full public record distributions obey

\[
d_{TV}\ge 0.655095683736\ldots >\tfrac12.
\]

The strict comparison with 1/2 is checked in exact rational arithmetic. The
displayed decimal is not used to decide that inequality.

For the preparation-equivalence witness, take equal mixtures of the +X/-X
stations and of the +R/-R stations. Simultaneously reversing w and S leaves
the crossing time unchanged and flips every menu read outcome. The timing
statistics above therefore apply to these mixtures, while each mixture gives
exactly unbiased menu reads, even conditional on its herald record. They are
the two intended I/2 preparations, yet their herald records distinguish them.
This is a failure of this candidate with this exact-time interface, not a
failure of OI or of all emission maps.

If trial start times are known integers, adding a trial's start to T does not
change its reduced denominator. More generally the observer can subtract its
known start time. The witness is not removed by writing absolute timestamps.

## 6. A clock countercontrol, not an access-closure result

Replace the exact time by one of B=16 equal bins of (0,1], keeping the attempt
index and the all-fail record. For positive P, the count in bin j is

\[
\lfloor jP/B\rfloor-\lfloor(j-1)P/B\rfloor.
\]

The checker computes the complete first-success attempt/bin distribution and
the all-fail probability exactly. At the same n=63 and m=256 its TV distance
between the two mixtures is 0.015685376945975646... . The denominator event
is not measurable from these bins; for example 1/5 and 2/9 share bin 4 but
disagree on E, and both times occur in the candidate's support.

This does not pass or revise the C-SPH-1 freeze. The model, attempt budget and
record interface differ. Nor does it justify hiding the finer time: a physical
clock and detector must establish which distinctions are available to every
permitted probe. The native wave is a discrete-time system; its additional
real-valued ballistic interpolation is not automatically an accessible clock.
The witness applies only if that interpolation's exact crossing time is public.

For comparison, replacing the discrete depths by an independent continuous
uniform depth on [0,M/n] preserves the success weight and angular law, but
conditional on any successful velocity the crossing time becomes exactly
uniform on [0,1]. That removes this arithmetic timing witness, at the cost of
supplying a continuous resource that the finite native source does not contain.
No continuous jitter or clock restriction is silently added to the candidate.

## 7. What follows and what remains

The conditional route to the projected-area law is now explicit:
bounded native independent bits -> equal three-component averages -> a
Gaussian angular limit -> geometric plane-crossing selection. This provides
a testable physical-map proposal rather than prescribed quantum reset weights.
It does not derive the averaging-to-velocity identification or the ballistic
motion from the native dynamics.

The timestamp witness shows why angular agreement is not enough. It also
identifies a concrete next obligation: specify the native clock, emission and
detector registers together, derive their accessible record, and then analyze
the joint angular/timing law. Merely increasing n or imposing a convenient
readout restriction is not that derivation.

Still unsupplied are a finite aperture, collector, reset/routing dynamics,
backreaction, protection of address and absorber data, a preparation factory,
the energy-shell prior, and composite behaviour. This handoff claims neither
a completed physical instrument nor OI-QM equivalence.

## 8. Evidence and replay

`emission_map_checks.py` is standard-library Python. It uses integer counts
and exact fractions, with no file writes, network or random sampling. It
checks the closed counts against separate direct enumeration of bit strings,
depths and reduced timestamps at n=1,3. It then checks the finite witness and
the clock countercontrol. Its PASS means those identities and witnesses hold;
it is explicitly not candidate acceptance.

Two runs in separate directories have byte-identical stdout, stored in
`emission_map_checks.out`. The package also includes `SHA256SUMS`. The
limiting angular result is a written argument; the finite witnesses are exact
computations. This is not a Lean proof or an independent second-author review.
