# OI explanatory carrier revision — finite model, recursive alternative, hard-to-vary test

**Working-explanation revision, not a theorem/physical-premise adoption.**
Prepared October 30, 2026 in response to a request to keep OI corrigible
in the Deutschian sense. This document is a **project-facing guide to the
best live explanatory questions**; it does not alter a formal hypothesis,
theorem, manuscript, frozen native round or proof status. Existing OI
finite-carrier results remain in force at exactly their proved scope.

## Observer-relative finite *accessible physics*, not finite total S

**Adopted working explanatory refinement:** for each embedded observer with
a *sourced bounded information budget* (e.g. the finite-area, finite-mode
horizon premises in GR's cosmological branch), the accessible physics over
a bounded protocol menu and time window admits a finite classification
of deterministic complete record words. That is the precise sense in which
the substratum is **relatively finite** to that observer. It is not a
theorem that the total substratum is finite, that every observer has a
finite-area event horizon, or that all exact operational probability
laws form a finite set. Mere embeddedness, finite horizon area and
finite statistical entropy each require distinct physical/mathematical
premises before an exact finite-state-count conclusion follows.

See [observer-relative finiteness](OBSERVER-RELATIVE-FINITENESS.md)
for the conditional finite-index theorem, its all-observer and
continuous-preparation counterexamples, a finite-time dynamic
nonclosure witness, and criteria for physical sourcing. The
intended OI ontology remains **a family of observer-relative
effective descriptions with non-unique microscopic
representations**, not a finite global carrier inferred from
the relative finiteness of each observer's causal access.

## Operational gauge: what "cardinality of S is gauge" can mean

**Refined working principle:** the number of total ontic states is **not
an invariant of the observational equivalence class at a specified
physical interface**. This extends OI's established deep-sector-gauge
motivation to a carefully scoped working research principle; it does
NOT assert that every finite and infinite system yields the same laws
or that the physical carrier has a proved infinite gauge orbit.

Specify a theory as a measured deterministic dynamical system
\(M=(S,T,\mu,\pi,\mathcal I)\), with normalized state/measure \(\mu\),
public readout \(\pi\), and an *explicit menu* \(\mathcal I\) of
physically available interventions, preparations and records. Two
models are operationally equivalent relative to an interface class
\(\mathcal P\) and horizon class \(\mathcal H\) iff for every admissible
protocol and horizon their **full joint record distributions**
(including heralds, losses, and correlated branches) agree. Denote this
\(M\sim_{\mathcal P,\mathcal H}M'\). The **gauge/representation
interpretation** is relative to this equality of accessible physics;
it is not automatically a microscopic automorphism group or a gauge
transformation in the Yang–Mills sense. **A bijection of one fixed
state space preserves its cardinality**, so changing |S| is
not literally a bijective gauge transformation of the same
configuration space. It can be an *equivalence of differently sized
presentations* after unused fibres are adjoined or quotiented.

### Exact positive control: cardinality-changing hidden extension

Let \(M=(S,T,\mu,\pi)\) be a finite reversible model and let \(D\)
be any nonempty probability space. Define
\[
M_D=(S\times D,\ T\times\mathrm{id}_D,\
      \mu\otimes\nu,\ \pi\circ\mathrm{pr}_S).
\]
For every finite visible word and, in fact, every time index,
\[
\Pr_{M_D}[(O_0,\ldots,O_K)=w]
=\Pr_M[(O_0,\ldots,O_K)=w].
\]
The proof is exact: the recorded trajectory depends only on \(S\)
and integrating the independent \(D\)-factor multiplies each
record probability by \(\nu(D)=1\). Taking \(D\) of size 1, 3,
countably infinite (with a normalized law), or \([0,1]\) with
Lebesgue probability changes \(|S\times D|\) while preserving the
complete passive observed process **at all times**. If all allowed
interventions also act trivially on \(D\) and their public records
factor through \(S\), the equivalence extends to that menu.

This is an **inert enlargement**, not the sourced nontrivial
recursive-feedback theory. It proves that raw total cardinality
cannot be recovered from the specified accessible physics, even
from complete passive histories, without a minimality/observability
condition. The existing finite-kernel source
\`OIBridge.PassiveQuotient.hiddenExt_same_law\` proves a
finite hidden-fibre analogue and constructs the minimal passive
observational quotient. **Its explanatory comment explicitly
distinguishes observer-relative (Level G4) redundancy from
the substratum gauge group (G3).** This research note does not
claim that the kernel theorem already handles arbitrary
uncountable \(D\), or arbitrary intervention menus.

### Exact negative control: cardinality is not universally gauge

Let \(X=\{0,1\}^{\mathbb Z}\), let \(T\) be the invertible
bi-infinite Bernoulli shift with product-fair measure, and let
\(\pi(x)=x_0\). This has one-bit visible records that are iid
fair across time. For every \(L>0\),
\[
\Pr[O_L=O_0]=\tfrac12.
\]
Every **fixed finite** reversible model has a positive integer
\(L\) with \(T^L=\mathrm{id}_S\); therefore it satisfies
\(\Pr[O_L=O_0]=1\) under every preparation. No fixed finite
permutation model has this Bernoulli shift's **entire all-time
visible record law**. The two may nevertheless agree on
any *predeclared finite horizon* via the finite-horizon
realization theorem, using a realization that may depend
on the horizon. This separates "gauge to finite experimental
precision/horizon" from "gauge across one unlimited
operational theory".

Nor is mere matching of single-time marginals or rooted
transition matrices sufficient; SUBSTATE-2 has an explicit
classical pair with identical rooted two-time matrices and
different complete three-time records. Enlarging the
observer's protocol menu can distinguish extensions that
were invisible to a weaker passive menu.

**Executed bounded checks (author, not an independent review).**
An exact rational enumeration found identical complete visible word
laws for inert hidden fibres of sizes 1, 2, 3 and 7 at horizons
0 through 8. A separate finite sweep checked all **153** permutations
of sets with 1 through 5 states and **4,282** binary readout
assignments, confirming the common-period return. These are
regression controls only; the arbitrary-cardinality enlargement
and infinite Bernoulli non-equivalence are supported by their
separate analytic arguments, **not** by an extrapolation from
finite computation. The attempted standalone replay-file
publication was not completed in this writer round; no retained
executable evidence or CI acceptance is claimed for these
bounded sweeps.

### How this relates to already stated OI results

- **GR §3.2**, Corollary *deep-sector cardinality is gauge*:
  boundary-conditioned, slow deep sector is absent from the
  **leading-order** visible transition law, with an explicit
  \(\mathcal O(\tau_S/\tau_B)\) backreaction error. Exact
  invariance is *not* claimed at arbitrary time for a coupled
  deep sector. GR identifies the finite and infinite
  deep-sector cardinalities as indistinguishable **within
  that leading-order transition scope**.
- **Substratum §4 Theorem 24(iii):** exactly decoupled
  **finite** ancillary factors preserve the stated
  channel under its fixed-interface hypotheses; no
  arbitrary-infinite theorem is silently inherited.
- **OIBridge.PassiveQuotient:** finite passive
  itineraries admit an observer-relative quotient and
  hidden extensions that preserve the passive law.
  Whether these redundancies remain invisible under
  all physical interventions or changing observers
  is an additional source question.
- **Full-system cardinality versus model minimality:**
  identifying the physically relevant *minimal
  observable representative* may make that
  representative finite at a given horizon, but
  does not force a finite total physical ontology.
  Conversely, some infinite processes have no
  fixed finite all-time observational realization.

**Adopt now:** cardinality of total \(S\) is **non-observable
and gauge-like within any verified observational-equivalence
scope**. Do not elevate it to an unconditional Yang–Mills
gauge symmetry or assert all infinite microstates are
physically dispensable. Require invariant complete
record laws under the **actual** available protocols
before accepting two differently sized models as
gauge-equivalent. The physical theory must explain the
interface and its limits; otherwise a claim that any
unobserved change is "gauge" could immunize OI against
falsification, contrary to the Deutschian rule.

## Cardinality clarification: finite observer does not imply finite ontology

The three propositions that must be kept distinct are:

1. **Finite accessible outcome alphabet at a specified resolution and time.**
   OI's visible-sector Lemma 1 is scoped to this. Its retained Lean Finiteness
   certificate is **conditional** on finitely many boundary modes, finitely many
   settings per mode and an observer state determined by those modes. Mere
   *embeddedness* does not logically entail finite observer capacity:
   an embedded infinite register is a possible countermodel unless a capacity
   restriction is also supplied.
2. **Finite recorded law at a specified finite horizon.** If there are n
   observable outcomes and K+1 observation moments, at most n^(K+1)
   histories can be resolved. The established finite-horizon equivalence
   supplies finite reversible representatives of these laws; that is not
   a theorem about the cardinality of the actual world's hidden carrier.
3. **Total substratum finiteness.** The full ontic configuration set is
   finite, giving a finite permutation's exact global recurrence. This is
   the separate **physical A1 posit** under which the spatial
   reconstruction and exact finite-total recurrence have been derived.
   Neither proposition 1 nor proposition 2 implies proposition 3.

**Revised working baseline:** remain **cardinality-neutral** about the
total ontic substrate, while keeping a finite observable readout and a
properly specified dynamics, preparation state and observer interface.
Total finiteness remains the useful, already analyzed model branch,
not an explanatory necessity silently inferred from observation.
This is a working foundation-level research stance, not a theorem
that nature is infinite.

### Strict infinite-state mathematical countermodel

Take the compact hidden-state space
\[
X=\{0,1\}\times\{0,1\}\times\{0,1\}^{\mathbb Z}
\]
with product-fair probability. Let
\[
T(a,r,c)=(a\oplus r\oplus c_0,\ r,\ Sc),
\qquad (Sc)_i=c_{i+1},
\]
and let the observer register only the four-valued record
\(O(a,r,c)=(a,c_0)\). The microscopic space is uncountable.
The rule is a bijective, continuous measure-preserving homeomorphism,
and the hidden r-bit genuinely influences the visible evolution.
The two-step visible records recover r from
\(r=a_{t-1}\oplus a_t\oplus c_{t-1}\), so the hidden sector
does not merely sit alongside observation as an inert enlargement.

Its rooted two-time conditional matrices have entries 1/4 for all
positive times, yet the full three-time visible law has one bit
of conditional predictive memory, with no common exact visible
return period. The paper-level proof and independently matched
classical controls are retained under SUBSTATE-2 draft PR #1011,
at the fixed-scale-skew result folder; independent mathematical
review is still pending.

This construction disproves the purported **logical entailment**
"finite observation plus reversibility and hidden readback forces
finite S". It is not evidence that *nature's* S is infinite or that
this is OI's physical update. Indeed, finite-horizon recorded
laws of this model admit finite reversible representatives under
the already established S⇔D⇔Qfb correspondence. Finite-window
observations do not uniquely determine microscopic cardinality;
a physical preference requires an additional hard-to-vary
source or scale-sensitive prediction.

### A narrow source inconsistency (correction required separately)

The existing Main §1.2 paragraph says the dynamics "acts on a
finite S (Lemma 1)", while **Lemma 1 itself** only asserts that the
visible configuration space is finite. A nearby status remark
correctly labels finite total S as a separate *physical posit*.
The former inference is therefore invalid as written. The
Explainer's Lemma-1 exposition likewise slides from finite
visible configuration to "the configuration space is finite"
when discussing exact recurrence. These errors are distinct
from deciding whether the true physical ontology is infinite.

The minimal source-correction task is tracked in [issue #1013](https://github.com/amaybaum/incompleteness/issues/1013), separately from the ontology revision. The correction should remove only those mistaken inferences,
while retaining every properly scoped finite-carrier theorem
and the independently named A1 posit. All affected book
mirrors, generated artifacts and Lean prose summaries must
be reviewed under AGENTS.md §A.25. This research-only PR
records the concrete defect rather than silently modifying
the publication sources without their required propagation.
The science error can be corrected regardless of which
carrier conjecture survives later tests.

## 1. What is retained

The established finite mathematical model uses finite visible sectors and
finite reversible realizations. Its finite-horizon law equivalence
\(S\Leftrightarrow D\Leftrightarrow Q_{\rm fb}\) is a statement about
*representation of finite recorded laws*, not an independently sourced
physical Hilbert-space apparatus.

The finite-*total*-carrier posit is deliberately stronger than the
finite-observer-resolution condition; the latter alone does **not**
prove the former. The fixed-total-finite recurrence theorem relies on a
microscopic permutation of finite order. Neither generic continuous
measure-preserving dynamics nor ordinary Poincaré recurrence supplies
an exact common visible period. The readback and finite-horizon
representation routes have their own, independently stated conditions.

Do not revise Main's finite theorems to "prove the infinite case" or
remove hypotheses from Substratum A1. Treat the original finite
reversible carrier as a precise **established model branch**, not
as an enforced unique ontology for future physical explanations.

## 2. Revised working conjecture — recursive carrier as a serious alternative

A possible improved explanation is that each finitely distinguishable
visible state corresponds to a *hierarchy of less accessible internal
distinctions*. The hierarchy may be mathematically represented by
an inverse limit, a compact group, or another precisely specified
measured space. **"Fractal" is a structural metaphor until a scale
law, an internal metric and a physical readout are sourced.** The
three-dimensional lattice need not become fractal in physical space.

The explanatory proposal is more demanding than cardinality:
one **fixed**, reversible, hard-to-vary microscopic dynamics must
couple the levels, and the same ontology must supply finite public
observations, intervention records and a prior. Merely adding infinitely
many hidden labels to a finite model contributes no new observable
physics if the deeper labels never affect the measured factor.

This is **an adopted investigation priority**, not a selected physical
postulate, theorem, gauge field or proof that quantum mechanics emerges
from that hierarchy. A future better explanation may discard the
recursive architecture; OI has no privileged conclusion.

## 3. Results that already criticize specific routes

The following are bounded **research findings on active draft branches**,
not results merged into main. Their sources are linked so every status
change is independently reviewable.

- **SUBSTATE-1**, issue #1007, draft PR #1009: a compact reversible
  3-solenoid automorphism with a finite binary readout can generate
  a stationary Markov process with **no common exact observable
  return**. Thus continuity and division-by-three capability do not
  select quantum behavior. Separately, the naive scalar-site-gradient
  link assignment gives trivial closed plaquette holonomies; a manually
  added gauge-covariant link/pointer toy demonstrates reversible
  classical back-action, **not** quantum operations or Yang–Mills.
- **SUBSTATE-2**, issue #1010, draft PR #1011: a fixed reversible
  skew/shift rule on an infinite fair binary tape yields **uniform
  P-divisible rooted two-time matrices but one bit of three-time
  conditional memory**, with no common exact visible period.
  A matched iid classical shift has the *same* two-time matrices
  and different three-time laws. These are actual classical
  countercontrols; they do not demonstrate nonclassical physics.
- **NATIVE-PADIC-1**, on draft PR #1011: the actual integer-coefficient
  cubic two-slice wave rule commutes with all congruence reductions
  \(2^n\to2^m\). A **fixed low-m passive observation cannot read
  information added solely in higher digits** under this unchanged
  linear rule. A separate reversible bit-to-bit kick breaks the
  obstruction but is **not the OI-native rule**. The author reports
  exact finite regression with 9,344 modular controls and a written
  all-state proof, pending independent review and exact-head Lean.
  Therefore the simple "replace q by an infinite p-adic alphabet"
  proposal is **not** the desired physical explanation.
- **Yang–Mills bridge**, draft PR #1003: local gauge covariance
  permits both \(S_1=\sum w(U_p)\) and \(S_2=\sum w(U_p)^2\);
  a continuous carrier or Haar prior does not select a Wilson
  action. The theory must separately source non-flat link variables,
  dynamics and a measure. A gauge redundancy is not a measurement
  interaction.

These results are useful **because they could have failed** under
named countercontrols. Their role is to **exclude the exact shortcuts
tested**, not to refute every possible continuous, recursive or
gauge-coupled architecture.

## 4. What would justify actually changing OI's physical postulates?

Treat the recursive hypothesis as a testable **replacement candidate**
for the fixed-total-finiteness posit, not a cosmetic addition.

A candidate must specify, before comparing with desired quantum/QCD
data:

1. **One sourced microdynamic**, including a fixed site/internal
   alphabet or inverse-limit space, a reversible time update,
   invariant normalized measure, and finite accessible observer
   channels. A chosen alphabet is not an observed fact.
2. **Nontrivial scale coupling**: an explicit dynamic influence
   from deep to observable degrees of freedom that survives
   the NATIVE-PADIC-1 congruence control, with a decoupled
   version in which the claimed effect vanishes.
3. **Physical quantum sourcing**: a real, selectable,
   repeatable preparation/measurement intervention from the
   same update. It must supply more than classical conditional
   memory or classical coherent-wave interference, and must
   pass complete-record, spectator/composition and
   Bell/no-signaling controls at the stated target.
4. **Physical gauge sourcing**: a non-pure-gradient
   covariant link carrier, a dynamically induced invariant
   measure/effective action, a connected-gauge/continuum
   scope where required, and a discriminating Wilson-versus-
   squared-action/loop-correlator test with full attempt and
   selection records.
5. **Entropy and recurrence integrity**: retain finite
   observational resolution; account separately for any
   infinite hidden entropy, physical boundary density and
   finite/approximate visible return. No inference from
   a finite quotient's period to a single global infinite
   return period.
6. **A new independent prediction or retrodiction** that
   was not used to choose the scale coupling, gauge action,
   observation decoder or hidden prior. State its admissible
   range and a result that would **reject** the revision.
   Without such a payoff, a recursive model that explains
   everything by adjustable hidden layers is not Deutschian.

**Gate:** only after a candidate survives these conditions
and independent mathematical, formal and physical review
should a separately governed minimal manuscript correction
replace A1 or another physical commitment. Success in a
finite exact toy or formal proof **relative to assumed
operations** is not sufficient. An untested interpretation
may be kept in the research programme but cannot be
presented as established quantum or Yang–Mills emergence.

## 5. What OI adopts *now* in Deutschian mode

- **Adopt a revised working explanatory stance:** total
  microscopic finiteness is one useful physical *posit*,
  not a theorem of observation; recursive measured carriers
  are a live rival **conjecture** to be tested in parallel.
- **Adopt criticism of the naive p-adic route:** the
  unchanged linear scalar wave has no high-to-low-digit
  backflow at a fixed congruence observer. Do not appeal to
  recursion alone to rescue the OI-to-QM or YM sourcing gaps.
- **Adopt the burden of a genuine improvement:** one
  independently constrained scale-coupling rule must predict
  something that the current finite representation,
  the matched classical-memory controls, and the
  competing gauge actions do not simply reproduce by choice.
- **Do not adopt as physical facts:** fractal microscopic
  geometry, an infinite ontology, an F2 quantum
  extension, YM action selection or scale-log-periodic
  signals. These remain openly corrigible conjectures.

The working explanation changes prospectively as criticism
arrives, while proved finite statements and negative
countercontrols remain intact. That separation is a
requirement of the scientific method, not resistance to
updating the theory.

## 6. Provenance and change control

This is a project-facing **working-hypothesis revision** rather
than an edit to a theorem. It is intentionally separated
from SUBSTATE-1 and SUBSTATE-2 drafts so their research
evidence, checks and negative results remain unchanged.
The manuscript synchronization rule in the OI→QM programme,
AGENTS.md §A.25 minimal-change policy, §A.29 hard-to-vary
revision test and §A.43 draft-PR lifecycle still apply.

A future manuscript change must name the specific accepted
finding, preserve all unaffected claims, propagate genuine
changes across manuscript mirrors and generated artifacts,
and receive exact-head CI and independent scientific review.
