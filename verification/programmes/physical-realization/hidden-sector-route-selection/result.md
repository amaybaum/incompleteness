# Hidden-sector tests: route selection and the relaxation gate

**Outcome:** select **H-NEQ** for the next bounded *derivation*, using a
second-moment/power-spectrum response as the first observable. The first
milestone is complete: the relaxation claim has been separated into a projected
propagator, a rate, an initial condition, and a readout response. Two hidden
assumptions are exposed exactly: order-H relaxation does not fix the exit-scale
exponent, and continued relaxation to a common end removes that exit-scale
trend. This record does not establish a non-equilibrium signal or an empirical
discriminator of the hidden-sector ontology.

This is research/design, not a native execution. The preceding
`decision-rule.md` fixes its scope and controls. No data, fitting, adopted
module, historical record or receipt is added; the manuscript corrections and
the replay workflow that accompany this record are described in §5.
Evidence labels: **W** written argument; **X** exact finite example/check;
**S** external source; **P** physical/model premise still required.
Productivity classification: **ELABORATING**, on the consistency axis; the
elementary permutation theorem is confirming. No maintained prediction's
classification changes here.

## 1. Comparison of the four routes

| Route | Available anchor | Missing input before a prediction | First useful observable | Decision |
|---|---|---|---|---|
| H-GRAV | GR §6.2's geometry-first ordering; the three requirements concern the partition boundary | A laboratory matter-to-field coupling selecting the microstate, hidden average, or emergent near-field reading; mediator locality and allowed ontic parameter dependence | Gravitational entanglement witness / coherence under a specified coupling | Keep open; a BMV prediction cannot be borrowed before the coupling is specified |
| H-NEQ | Main §4.5's selected measure and conditional mixing hypothesis; Chapter 18 §18.2's heuristic dynamical reading | Projected/conditional propagator, rate coefficient, initial family, horizon-exit/end rule, observable map | Mode variance ratio, then the primordial power spectrum under a fixed inflation/readout comparison | **Select for the cheapest precise derivation gate** |
| H-FIN | Finite representative, bijection, and conditional lattice dispersion | Total capacity, prior arithmetic, concrete update and observable response, comparison with other discrete theories | Recurrence/dispersion/capacity signature once a magnitude is derived | Keep open; finiteness alone supplies neither an accessible magnitude nor uniqueness |
| Classical memory | Main §4.5's classical-memory simulability commitment | An outcome-independent operational rule separating fundamental from engineered processes, and the exact source-model applicability of the memory witness | An entanglement-structure memory witness in a system selected by that rule | Keep open; the eligibility rule must precede observing the witness |

This ranking concerns a first derivation's cost and specificity, not predicted
detectability. No completion of any route has been selected as nature's dynamics.

For H-FIN, a two-state bijection with prior `(sqrt(2)/2, 1-sqrt(2)/2)`
already gives an irrational one-slot probability. Recurrence follows from
finite bijectivity, but a universal accessible recurrence time does not.
The Slagle–Preskill construction derives its departures from an explicit
stochastic bulk model; its estimates cannot be transferred to a different
deterministic substratum merely because both use lattices. [S3]

For H-GRAV, the BMV sources specify coherent phase evolution and conditions on
mediation. Their entanglement conclusion is a comparison under those
conditions, not a prediction for an unspecified geometry-first coupling. [S4]
No written underdetermination theorem for the full gravity premises is claimed
by this table.

## 2. Measure reading and the exact relaxation boundary

**Posited reading:** if the physical measure is selected as the stationary
maximal-entropy measure from the outset, there is no freely chosen initial
departure to relax. A non-equilibrium route then requires an added preparation
or initial-condition premise. This is compatible with Main §4.5's epistemic
measure selection; it is not a dynamical derivation.

**Dynamical reading:** allow a stated initial distribution distinct from a
specified stationary reference, then derive what an observer actually sees.
Chapter 18 §18.2 proposes this reading but does not provide its propagator.
Main §3.4's conditional-mixing theorem assumes closeness of realized hidden
conditionals; it gives a bound conditional on that closeness, not a proof that
an arbitrary initial ensemble approaches it.

### 2.1 Fine-grained invariance [W, X]

Let `phi` be a bijection of a finite set, `rho` a probability law, and `pi`
a stationary probability law (`phi_* pi = pi`). For every integer n,

`TV(phi_*^n rho, pi) = TV(rho, pi)`.

Proof: rewrite the defining sum with the permutation `s -> phi^n(s)`:
`sum_s |rho(phi^-n(s)) - pi(phi^-n(s))|` has exactly the original summands.
The same argument preserves any f-divergence whose expression is well-defined.
In particular, uniform `pi` is stationary under every permutation.

Thus arbitrary fine-grained distribution relaxation to that reference does
not follow from finite reversible evolution. This does **not** obstruct
projected observables, conditional distributions, coarse-grained relaxation,
or pre-recurrence approximations. It identifies which distribution an eventual
relaxation law must name.

An exact four-cycle `0 -> 1 -> 2 -> 3 -> 0`, projected to `{0,1}` versus
`{2,3}`, makes the distinction concrete. Starting at
`rho=(1/2,1/2,0,0)`, fine-grained TV stays `1/2`, while projected TV from
the uniform projection is `(1/2,0,1/2,0,1/2)`.
Projection contracts TV at each time; it does not make the time sequence
monotone. Moreover, point masses at 0 and 1 have the same current projection
but different next projections. A closed autonomous projected update is an
additional condition, not a consequence of having a projection.

### 2.2 Conditional scalar law and its coefficient [W, P]

If a *derived* projected mode admits the additional law

`d delta_k/dt = -lambda H(t) delta_k`,

with constant `lambda > 0`, then `H = (d a/dt)/a` gives exactly

`delta_k(a) = delta_i(k) (a_i/a)^lambda`.

The integration uses no constant-H assumption. But `tau_eq ~ H^-1` fixes
neither a scalar autonomous mode nor `lambda = 1`. For example,
`tau_eq = H^-1` and `tau_eq = (2H)^-1` are both of that order and yield
different exponents. If the rate varies, the exponent is replaced by
`exp(-integral lambda(N,k) dN)` with `N=ln a`.

A reset comparison kernel `M_r = r I + (1-r) 1 q` is stochastic,
leaves `q` invariant, and maps `rho-q` to `r(rho-q)`. Choosing retained
fractions `1/2` or `1/4` per `Delta N=ln 2` produces exponents 1 or 2.
This is an exact positive comparison for relaxation; it is not the specified
OI update, and its resetting operation cannot be inferred from bijectivity.

### 2.3 Exit rule versus end rule [W, X, P]

For constant inflationary H, define `k_i=a_i H` and use the horizon-exit
condition `k=a_exit H`. If (i) the scalar law holds, (ii) its initial amplitude
is scale-independent, and (iii) the observable freezes at exit, then

`delta_exit(k)=delta_i (k_i/k)^lambda`.

All three qualifications matter. Scale-dependent initial data
`delta_i(k)=D (k/k_i)^lambda` cancel the trend on a bounded interval where
the perturbation remains a probability law. If relaxation continues at the
same rate to a common `a_end`, then

`delta_end(k)=delta_i (a_i/a_end)^lambda`,

independent of k for scale-independent initial data: the post-exit factor
exactly cancels the exit factor. These are distinct physical histories with
distinct observable consequences. Larger residuals on larger scales are
conditional on the freeze/readout prescription; they are not fixed by
the horizon timescale alone.

## 3. First observable, null, and limits of discrimination

Use `xi(k) = Var(R_k) / Var_QT(R_k)` as the first target after the
readout of a cosmological mode `R_k` has been derived. It is a second-moment
observable. Transfer to measured angular power would require the specified
inflationary and cosmological transfer functions, schematically

`C_l = 4 pi integral d ln k P_QT(k) xi(k) |Delta_l(k)|^2`.

This equation is a conditional cosmological comparison, not an OI-derived
mode readout. Valentini's explicit pilot-wave calculation uses a variance
ratio to modify the primordial spectrum; it also distinguishes power
changes from more general phase/correlation departures. Its guidance law
and persistence result are not imported into OI. [S1]

**Exact finite response example [X]:** reference outcomes `(-1,0,1)` with
`q=(1/4,1/2,1/4)` and perturbation
`rho=(1/4+epsilon,1/2-2epsilon,1/4+epsilon)` are probabilities for
`-1/4 <= epsilon <= 1/4`. Their mean and third moment are zero, while
`Var(rho)=1/2+2epsilon` and `xi=1+4epsilon`. The comparison reset kernel
therefore gives, under the exit assumptions,

`xi(k)=1+A (k_i/k)^lambda`, with `A=4epsilon_i`.

This is an illustrative finite measurement law, not a cosmological
substratum prediction. It demonstrates why a bispectrum is not a necessary
first observable: a departure can change a variance with no third moment.
A centered Gaussian with a changed variance supplies a separate continuous
comparison with no connected cumulants above order two. Neither example
licenses a unique non-Gaussianity shape for the actual OI realization.

**Restricted null:** the same specified inflationary state, transfer model,
and nuisance family, with Born statistics (`xi=1`). A fully derived,
nonzero response would discriminate that fixed null from that specified
completion. It would not by itself discriminate OI from every quantum
initial state or alternative inflationary mechanism. The source literature
also explicitly raises this uniqueness problem. [S1]

**Identifiability gate:** the free initial function absorbs the response:
within the chosen positive-law interval,
`epsilon_i(k)=(xi_target(k)-1)(k/k_i)^lambda/4` produces any sufficiently
small target variance correction. Even a restricted family contains the
null at `A=0`. No data can exclude the whole family solely by observing
no departure unless an independently supplied nonzero lower bound exists.
This is a limitation of this parameterization, not a no-go theorem about
all possible hidden-sector tests.

Planck's non-Gaussianity paper reports limits on specified bispectrum
shapes. A scalar variance response or an unspecified history-dependent
shape has no licensed conversion to its `f_NL` parameters. No Planck data
or bounds are evaluated in this record. [S2]

## 4. Concrete next derivation and its stop conditions

The next target is **H-NEQ-PROPAGATOR**: for one specified cosmological
substratum representative and observer partition, derive the projected or
history-conditioned evolution of a specified mode-deviation observable.

Required inputs must be stated together: the update and its boundary
coupling; initial measure family; coarse-graining/conditioning rule; mapping
to the mode amplitude; scale factor/time identification; and the physical
rule for post-exit evolution. The derivation must obtain the propagator from
these inputs rather than install the reset comparison above.

The bounded decision has three outcomes:

1. **Derived restricted response:** obtain its rate spectrum and visible
   moment response with positive probabilities, identify the restrictions
   on initial data and the freeze/end prescription, and show whether the
   family has any unavoidable nonzero signal. Only then draft an empirical
   preregistration against the fixed null and serious quantum alternatives.
2. **Response vanishes:** show the named observable is insensitive for this
   completion; close this particular observable route, not all H-NEQ.
3. **Underdetermined:** exhibit two allowed choices of a still-open input
   producing distinct responses, retaining the same stated controls; name
   the extra physical principle needed. Do not assign an empirical verdict.

Controls for that future derivation: equilibrium gives the baseline law;
fine-grained reversibility is retained; normalized positive outcome laws;
conditional memory is kept distinct from ensemble non-equilibrium; a
nontrivial response comparison and a zero-response comparison; exact
finite identities before numerical approximations; and an independent
check of the claimed source-to-readout map. A scale/initial-condition
restriction imposed only after seeing data fails the derivation gate.

No empirical statistical threshold is designated here. Before new data,
a separate preregistration must fix the data release, usable scales,
transfer/nuisance model, competing initial states, parameter bounds,
likelihood, coverage controls and rejection criterion. A free amplitude
including zero can support an upper bound on a completion; it cannot
falsify the unrestricted hidden-sector ontology.

## 5. Check record and provenance

The stdlib Fraction checker passes **5,273 exact checks**. Most instantiate
one identity, the total-variation invariance of §2.1: 2,092 against the
uniform reference, and 3,104 against a nonuniform stationary reference
(1,552 permutation–law pairs, each checked for stationarity and invariance).
The exit-rule, common-end and initial-data results of §2.3 are computed by
evolving three-point laws under the reset kernel and are then compared with
the closed forms; 40 checks confirm that every evolved law is a probability
law. Fifteen countercontrols each run a corrupted input through the predicate
that its positive check uses, which must reject it. The corrupted inputs are:

- a nonbijective map;
- a nonstationary reference;
- a cycle that does not revive, and a lumpable partition;
- perturbations with no variance change, with nonzero odd moments, with a
  nonzero third moment, or with a nonzero mean;
- an invalid law;
- an identity kernel and a nonstochastic kernel;
- the wrong exit, exponent or end rule.

The output is saved in `exact-output.json`. `evidence.json` states the recipe
and the provenance of its byte-for-byte replay, and the
`hidden-sector-replay` workflow reruns both checkers of this programme. These
are design-example controls, not kernel certification, a native run, or an
independent implementation of the checker. The independent mathematical
evidence is the reindexing argument and the scalar integrations above.
`decision-rule.md` was committed together with this result, so the history
does not show it preceding the check.

Manuscript anchors were read at the manuscript snapshot `dee3b5ae` named in
`decision-rule.md`: Main §§3.4/4.5, GR §6.2, Chapter 18 §18.2, and ROADMAP's
direct-hidden-sector P2 row. At that snapshot the book labelled the
relaxation estimate heuristic, but it:

- derived an `a_i/a` decay from the relaxation timescale alone;
- named non-Gaussianity as the consequence of modified statistics;
- asserted a distinctive history-dependent shape.

§§2–3 bear on each of these:

- a Hubble-order timescale does not by itself fix a decay law;
- a changed variance does not entail a third moment or any non-Gaussianity;
- a cosmological prediction needs a specified source dynamics,
  initial-deviation family and map to observables.

After independent review, Chapter 18 §18.2, its summaries, Chapter 19,
appendix A's F7 row and ROADMAP H-NEQ items 2–3 were corrected in place on
these three points. The corrections stand on the mathematics stated here. No
actual OI mode evolution has been derived, and F7's classification as a
conditional prospect is unchanged.

## Sources read for the comparison

- **S1:** A. Valentini, *Inflationary Cosmology as a Probe of Primordial
  Quantum Mechanics*, arXiv:0805.0163v2, §§6–7 and 10–11.
  [Full text](https://arxiv.org/html/0805.0163v2). Source supports the
  comparison's variance response and its lack of automatic uniqueness;
  it does not supply OI's missing dynamics.
- **S2:** Planck Collaboration, *Planck 2018 results. IX. Constraints on
  primordial non-Gaussianity*, arXiv:1905.05697.
  [Source](https://arxiv.org/abs/1905.05697). Used to identify the
  observable class, without analysing its data.
- **S3:** K. Slagle and J. Preskill, *Emergent Quantum Mechanics at the
  Boundary of a Local Classical Lattice Model*, arXiv:2207.09465v3,
  §§IV/VI. [Full text](https://arxiv.org/html/2207.09465v3).
  Comparison only; model-specific errors are not transferred.
- **S4:** S. Bose et al., arXiv:1707.06050;
  [source](https://arxiv.org/abs/1707.06050), and C. Marletto and V. Vedral,
  arXiv:1707.06036; [source](https://arxiv.org/abs/1707.06036).
  Their coherent-mediation comparison motivates an observable, not the
  unresolved OI coupling.
- **S5:** A. Valentini, *Signal-Locality in Hidden-Variables Theories*,
  arXiv:quant-ph/0106098v2; [source](https://arxiv.org/abs/quant-ph/0106098v2).
  Its existence-of-signalling theorem is not an assertion that every
  non-equilibrium distribution signals. Transfer to the substratum's
  parameter-dependent responses remains a separate question.
