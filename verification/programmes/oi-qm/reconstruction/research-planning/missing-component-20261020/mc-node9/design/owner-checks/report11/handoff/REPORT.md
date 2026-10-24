# Bounded independent resources from a finite wave rule

**Handoff v1 — 2026-10-22. Research result for independent review.**

This package records the native-wave construction discussed in the read-only
investigation of `amaybaum/incompleteness`, PR #885. It supplies a written
finite-window independence proof and a standalone exact checker. It does not
designate a repository freeze, adopt a physical premise, or change the closed
C-SPH-1 numerical checkpoint.

The earlier checks were executed in memory. This package reconstructs them as
a stable, reviewable implementation and adds checks of adaptive window length,
adaptive station choice, and an independent numeric wave update. Its hashes
identify this handoff, not the earlier ephemeral script. No claim of byte
identity to that earlier script is made.

## 1. Result and boundary

Under uniform counting on the full initial phase space, a particular finite
wave realization supplies independent uniform symbols at finitely many ports
for a bounded time. The result survives conditioning on the initial port
readings and on any readiness event determined by those readings. It also
survives subsequent adaptive calls based on past port records.

The construction is native in a limited, precise sense: its update has the
finite modular wave form stated in the manuscript. It is an instance of that
class, not a proof that OI selects its parameters, prior, observer, or physical
implementation. No quantum reference probabilities enter the checker.

**These are field symbols, not a constructed particle source.** Calls only
select which passive field readings are reported. They do not change the wave
update. The construction has no implemented shutter, physical carrier,
absorption, measurement backreaction, or outgoing quantum state. Turning the
sampler into an embedded apparatus remains work to do.

## 2. Source anchors and additional choices

The following manuscript anchors are pinned to main commit
`48b18ac54e39920a4fc4bbb8ee1d1b6cebea2c29`, the revision reviewed when the
construction was developed:

- [Main.md, Lemma 3 and the measure-as-datum remark](https://github.com/amaybaum/incompleteness/blob/48b18ac54e39920a4fc4bbb8ee1d1b6cebea2c29/papers/Main.md#L56-L62):
  counting measure is selected by a maximum-entropy principle; invariance alone
  does not select it, and structured preparations can change visible laws.
- [SM.md, finite wave form and scope](https://github.com/amaybaum/incompleteness/blob/48b18ac54e39920a4fc4bbb8ee1d1b6cebea2c29/papers/SM.md#L224-L236):
  the center-free, nearest-neighbour, cubic-symmetric linear rule has the
  second-order wave form. Its functional center independence does not, by
  itself, establish statistical independence.
- [SM.md, symmetric component branch](https://github.com/amaybaum/incompleteness/blob/48b18ac54e39920a4fc4bbb8ee1d1b6cebea2c29/papers/SM.md#L332):
  a finite-alphabet rule acting identically and independently on components is
  an explicitly considered branch. This report uses two scalar copies as a
  resource candidate; it does not identify them with the physical carrier.

| Ingredient | Status here |
| --- | --- |
| Finite reversible modular wave form | Manuscript-supported candidate class |
| Full Cartesian phase space and uniform counting | Explicit ensemble assumption; compatible with the cited counting branch |
| Three dimensions, prime alphabet, nonzero scalar coupling | Restrictions of the theorem; the concrete checker uses q=3 and alpha=1 |
| Two uncoupled field components | Explicit candidate choice |
| Port locations and a bounded observation horizon | Explicit geometry and resource budget |
| Readiness depends only on specified initial port readings | Explicit restriction on conditioning |
| Calls use only past port records and independent protocol randomness | Explicit information restriction |
| Nonzero herald symbol means success | Chosen sampler interface, not a derived detector law |

In particular, uniform counting on a conserved-energy shell is not generally
the product counting measure used here. No extension to that ensemble is
proved. Alpha=1 below is a finite-field coefficient; no claim is made that a
real-valued continuum wave lift at that coefficient is stable or normalized.

## 3. Exact finite model

Let q be prime, alpha a nonzero element of F_q, and
Lambda=(Z/LZ)^3 the cubic torus. For one component the state is a pair of
fields (p,c), interpreted as u(-1),u(0). The update is

\[
u_x(t+1)=\alpha\sum_{y\sim x}u_y(t)-u_x(t-1)\pmod q.
\]

With A the six-neighbour adjacency operator,

\[
\Phi(p,c)=(c,\alpha Ac-p),\qquad
\Phi^{-1}(c,f)=(\alpha Ac-f,c).
\]

Thus Phi is a bijection on a finite set and preserves uniform counting.
Take two independent components H and M, each with this update. Their joint
initial law is uniform on the full Cartesian phase space; independence of
initial coordinates follows from that assumption. The dynamics transports
initial uncertainty into the observed variables; it creates no new entropy.

The one-port check uses L=9, q=3, alpha=1, K=4. The eight-port realization uses
L=18 with centres in {0,9}^3, keeping q=3, alpha=1, K=4. Its total phase space
has 2 components x 2 time slices x 18^3 = 23,328 trits.

## 4. Bounded independence theorem

**One port.** Suppose L>2K. Fix a port x. Let C_x contain u_x(-1) and
u_x(0). Then (u_x(1),...,u_x(K)) is uniform on F_q^K and independent of C_x.

**Proof.** Regard every reading as a linear form in the initial fields.
For each t=1,...,K select the initial variable u_(x+t e1)(0). Its coefficient
in u_x(t) is alpha^t: reaching that site in t nearest-neighbour steps requires
the unique straight path. Terms from the retarded register have lower spatial
degree and cannot contribute to that extreme coefficient. L>2K excludes a
shorter wrapped path. The selected variable cannot appear in any earlier
reading, or in C_x.

Condition on all initial variables except these K selected coordinates. Those
coordinates remain independent uniform elements of F_q. The map from them to
the K outputs is affine triangular with diagonal alpha,alpha^2,...,alpha^K,
all nonzero. It is therefore bijective. Every output string has conditional
probability q^(-K), independently of the conditioned variables. Averaging
proves the claim, including independence from C_x. QED.

**Multiple ports.** If the radius-K graph balls of the ports are disjoint,
all their output arrays are jointly independent uniform, independent of the
combined initial port readings C. Each port's outputs use only initial
variables in its ball; apply the preceding proof to the disjoint sets.
The two uncoupled components give the direct product of these laws.

For L=18, K=4 and centres {0,9}^3, distinct centres are at graph distance at
least 9>2K. For one component the 16 initial-port rows have rank 16, and the
16 initial plus 32 future rows have rank 48. Equivalently,

\[
\operatorname{rank}\binom{C}{Y}-\operatorname{rank}(C)=32.
\]

For two components this gives 64 jointly independent future trits conditional
on all 32 initial port trits. The checker verifies these ranks over F_3 and
the disjoint supports. It does not enumerate the entire phase space.

The rank criterion is the standard finite-field counting statement: for a
uniform vector X, linear rows Y are uniform and independent of linear rows C
when their joint rank increases by the full number of Y rows. Every nonempty
affine fibre then has the same number of preimages.

## 5. Readiness and adaptive calls

Let E be any positive-probability event determined by C. Since Y is independent
of C, its product law is unchanged conditional on E, on the value of C, or on
any public readiness record that is a function of C. Choosing all zero initial
port values is one example, not a necessary preparation. This proves no high
probability or low cost for producing a specified ready apparatus.

The admissible protocol may also use a random seed independent of the initial
wave state. At tick t it may choose a station and a positive integer window n,
with t+n<=K, using C, that seed, and port records from ticks at most t. It may
inspect the chosen station at ticks t+1,...,t+n, stopping at the first success.
No call reuses a tick it already selected, and later sequential calls start
after the previous success or timeout. No access to future or neighbouring
microscopic variables is included.

The future arrays are independent of the complete past array, not merely of
the coarser returned records. Therefore adaptive choices based on those
records preserve freshness. Formally, condition on the chosen time, station,
window and history; the next unused future entries have their original product
law. Finite induction gives this statement for every admissible adaptive
protocol within the horizon.

A readiness search based on port observations during the same finite window
can be treated as a stopping rule, but its elapsed ticks consume the horizon.
The theorem does not cover an unbounded search, a pre-window observation history
not represented by C, or additional initial constraints. It does not prove
operational equivalence between differently implemented preparations: readiness
success probabilities or other records could already distinguish them.

## 6. The marked first-success sampler

At the chosen port, call H_t the herald component and M_t the mark component.
H_t=0 means no emission; H_t!=0 means success and returns M_t. A call records
its station, start time, window, success/failure and, on success, the waiting
tick k and mark d. The first-success/timeout record is a deterministic function
of the field. This is a sampler definition, not an implemented particle map.

Conditional on any admissible history and the selected call parameters,

\[
\Pr(F\mid h,w,t,n)=q^{-n},
\]
\[
\Pr(U=k,M=d,S\mid h,w,t,n)
=q^{-(k-1)}\frac{q-1}{q}\frac1q
=\frac{q-1}{q^{k+1}},\quad 1\le k\le n.
\]

Waiting time is a truncated geometric law; the mark is uniform independently
of waiting time conditional on success. The waiting-time statistics are the
same at every station. This is a discrete-time result, not a Poisson or
continuous-crossing-time theorem.

For q=3 and n=2, failure has probability 1/9. Each of the three marks has
probability 2/9 at wait 1 and 2/27 at wait 2. Two successive two-tick calls
have 49 possible record pairs. The second call starts immediately after the
first succeeds, or after its timeout, so both calls fit in four ticks.
All 3^8=6,561 histories of H_1,M_1,...,H_4,M_4 are enumerated exactly and give
the product of the displayed call laws.

Further finite checks use a history-dependent second window and a second
station chosen by the first mark. The all-protocol assertion comes from the
written product-law argument, not from those finite test families alone.

## 7. Countercontrols

**N1: shared preparation constraint.** In the one-port model, impose the extra
initial linear condition u_x(2)-u_x(1)=0. Both future readings are linear forms
of the initial fields; this is a correlated initial ensemble, not an allowed
C-only readiness event. With C fixed, the two individual readings remain
uniform, but they are equal. Two one-tick heralds then have probability zero
of success followed by failure, instead of 2/9. The checker verifies the
constraint and marginal/joint ranks exactly. Uniform marginals are insufficient.

**N2: no spatial coupling.** Set alpha=0. Once the initial port values are
known, the future is the deterministic recurrence u_(t+1)=-u_(t-1); the
conditional output rank is zero. The nonzero frontier coefficient is essential.

**N3: expanded microscopic access.** Give the observer the six initial current
neighbour values, as well as the initial port readings. Their sum determines
u_x(1), so the next herald is predictable. The checker verifies no rank
increase from appending that output to the expanded observations. Causal
geometry alone is not a justification for hiding these variables.

**N4: finite return.** On the 3^3 torus over F_3 with alpha=1, A^3=0:
the shifts commute, cubing is additive in characteristic 3, each shift cubed
is the identity, and the six contributions sum to zero. The recurrence gives
u(5)=-u(-1) and u(6)=-u(0), hence Phi^6=-I. Conditional output ranks at a
port are [1,2,3,4,4,4]. Independence cannot continue indefinitely. A separate
numeric implementation checks the inverse, the sparse forms and this six-step
return on all 54 phase-space basis vectors. Linearity extends the basis check
to the whole small phase space.

The nonwrap and separation bounds are sufficient, not claimed optimal: N4
actually retains four independent readings despite its smaller lattice.

## 8. What the result supplies toward C-SPH-1

It supplies a concrete bounded resource mechanism: initial product counting,
the native wave rule, and finite propagation together deliver independent
symbols at several ports even though the dynamics is coupled. Independence
need not be postulated anew after every encounter. The initial ensemble,
component structure and observation interface remain declared inputs.

It does **not** supply:

1. an isotropic particle-direction distribution or the cosine-weighted flux
   law mu_w(dlambda)=(w dot lambda)_+ dOmega/pi;
2. a physical map from field coordinates to particles, positions, velocities,
   crossings or spherical-collector signals;
3. measurement/reset backreaction compatible with the unmodified wave law;
4. a preparation factory or the validity of the product prior after arbitrary
   preparation or conserved-energy conditioning;
5. physical closure of address, absorber or microscopic-probe access;
6. indefinite freshness, continuous timestamps, quantum instruments, composite
   behaviour or Bell violations.

An arbitrary decoder of uniform symbols can synthesize many probability laws.
Therefore this result does not select quantum probabilities. Its useful next
application is to an explicitly derived geometric emission/readout map with
the preparation procedure, feedback and accessible record included.

This finite-window resource trace is iid. It does not itself exhibit C4
history readback in that window. The smaller-lattice return control illustrates
how predictive memory can reappear, without proving that this passive sampler
is a complete embedded-observer model.

## 9. Evidence and review status

`native_wave_checks.py` uses only Python's standard library, modular integers,
and `fractions.Fraction`. It makes no network calls, imports no repository code,
writes no files, and uses no random sampling. `native_wave_checks.out` is its
deterministic expected stdout. `SHA256SUMS` identifies all substantive package
files. See `README.md` for replay instructions.

The general theorem is a written proof. The finite instances and countercontrols
are exact computations. This is not a Lean formalization, an independent
second-author verification, or a preregistered acceptance experiment. The
checker and proof are being supplied for that independent scrutiny. No
repository status should change merely because this package reports PASS.
