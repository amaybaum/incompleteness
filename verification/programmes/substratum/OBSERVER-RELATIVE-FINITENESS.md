# OI: observer-relative finiteness — hypothesis, exact scope and falsifiers

**Research-only working-foundation refinement; draft PR #1012, October 30, 2026.**
This note does not modify Main Lemma 1, finite-carrier A1, theorem
classifications, boundary entropy premises or manuscript bodies.
Its purpose is to sharpen the proposed physical explanation: a
finite *accessible* substratum **relative to an observer**, not a
finite total ontic state space forced by embeddedness.

## 1. Replace the ambiguous claim with three separate meanings

The claim "every embedded observer has a relatively finite horizon,
so the substratum is relatively finite" should be interpreted with
the precise, independent premises below, **not** as a universal
theorem that embeddedness implies a finite-area event horizon.

- **Finite causal/information budget.** For a specified observer o,
  bounded accessible region and observation window, assume an
  effective boundary B_o with finite area A_o, a positive physical
  resolution epsilon_o, finitely many distinguishable settings per
  coupled boundary mode, and an access map determined by these
  modes. This is the conditional premise modeled by
  OIBridge.Finiteness.finite_of_boundary_modes. The GR formula
  N_o ~ A_o/epsilon_o^2 counts the *coupled boundary cells* within
  its selected de Sitter/finite-entropy construction; finite A
  and epsilon>0 are independent assumptions, and one mode per
  cell or finite state count is not obtained from area alone.
- **Finite record information at finite resources.** Even before
  making assumptions about an ontic S, finitely many possible
  visible symbols over a bounded number of observation moments
  give finitely many deterministic *record words*. With a
  finite set of physical protocols there is a finite
  **observational history partition** of all starting states.
  That partition is relative to o, protocol menu and horizon.
- **Finite operational state space or ontic substratum.** A finite
  record alphabet or entropy bound does **not** imply finitely
  many *exactly different statistical response laws*, let
  alone finitely many ontic states. With varying preparations,
  even a one-bit measurement can exhibit continuously many
  response probabilities; a qubit has a two-dimensional
  Hilbert space but continuously many nonorthogonal pure
  preparations. To claim a finite *exact* operational state
  quotient requires extra isolation, finite precision, finite
  menu, and equivalence assumptions stated explicitly.

**Recommended terminology:** "observer-relative *finite information
capacity* and *finite-horizon effective description*" is the
robust thesis. "Observer-relative finite substratum" is legitimate
shorthand only with an explicit operational equivalence relation and
its accessibility/precision scope.

## 2. Conditional finite-index theorem (deterministic complete states)

Let S be any set, finite or infinite. Fix an observer o, a **finite**
set P_o of fully specified deterministic experiment protocols
(including apparatus settings, interactions and outputs), and a
bounded horizon K. Suppose each protocol p produces one of finitely
many *complete* public word records W_{o,p,K}. The record map
R_{o,p,K}:S -> W_{o,p,K} is deterministic on the full microscopic
initial state (include any random seeds in that state).

Define
\[
s\sim_{o,P,K}t
\quad\Longleftrightarrow\quad
  R_{o,p,K}(s)=R_{o,p,K}(t)
  \quad\text{for every }p\in P_o .
\]
Then
\[
|S/\!\sim_{o,P,K}|
 \leq \prod_{p\in P_o}|W_{o,p,K}|<\infty.
\]
**Proof.** Map an equivalence class to the tuple of complete
protocol words. The map into the finite Cartesian product is
injective by definition. It does not matter whether S has
cardinality 4, countable infinity, or the continuum. □

This is **exact for the specified finite deterministic record
interface**. It is not a claim that the quotient is a reversible
dynamical state space: the finite-time equivalence need not be a
congruence respected by the microscopic time update. It also
does not prove that the probability distribution over words for
each accessible preparation is one of finitely many possibilities.

If the model is stochastic at the declared ontic level,
"equal deterministic word" is replaced by equality of *joint
record distributions* for all admitted preparations/protocols.
There may then be infinitely many response laws even with
a binary outcome, unless more assumptions are imposed.

## 3. Positive and negative mathematical countercontrols

### A. Every observer has a finite view, yet there is no global bound

Take S={0,1}^N, an uncountable space of infinite binary tapes.
Observer o_n can resolve only the first n bits. Each observer's
readout alphabet has exactly 2^n words, **finite for every n**,
yet the collection {o_n | n>=1} distinguishes every pair of
different tapes. No finite n works for *all* observers, and
the entire hidden space is uncountable.

This is an exact counterexample to the inference
\[
(\forall o,\ |S_o^{eff}|<\infty)
\Longrightarrow
|\ S\ |<\infty
\quad\text{or}\quad
\exists B<\infty\ \forall o,\ |S_o^{eff}|\le B .
\]
The two conclusions do not follow. If a proposed physical
theory wants a **uniform observer-independent bound**, it
must derive one from additional physical conditions, not from
the quantifier "every observer" alone.

### B. Finite outcomes, infinitely many statistical states

Consider the preparations indexed by theta in [0,1],
each yielding one binary record with
P(1 | theta)=theta. Every individual measurement has two
possible outcomes and at most one bit of Shannon information.
Nevertheless the family of exact preparation response laws
is uncountable, since theta->Bernoulli(theta) is injective.
Repeating independent preparations and using public outcomes
can estimate theta arbitrarily precisely as the number of
trials increases. Fixed finite trial budget and finite
resolution yield a finite experimentally distinguishable
approximation, **not** finite exact operational state count.

This does not assume quantum mechanics; it is an elementary
classical probability example that prevents a finite-horizon
information bound from silently becoming an exact global
state cardinality bound.

### C. A finite two-time interface need not close under evolution

The SUBSTATE-2 fixed reversible Cantor-skew model
has four visible records, uniform P-divisible rooted
two-time laws and one bit of three-time conditional
memory. A finite *two-time* coarse description
therefore need not determine later complete-record laws.
The idempotent 4x4 rooted matrix is not a proof that
the actual four-record process is first-order Markov.

The finite-depth quotient of an observer must be tested
for dynamic closure, repeatable interventions,
history/memory requirements and bounded resource
composition before being identified with an
autonomous finite substratum. Enlarging the horizon
or protocol menu can refine a quotient indefinitely.

## 4. Horizon assumptions: avoid universal overclaim

A finite-area cosmological event horizon is relevant for
GR's specified de Sitter/cosmological physical branch,
not a theorem about **every** mathematically possible
embedded observer. An eternal inertial observer in
Minkowski spacetime has no observer event horizon;
accelerated observers may possess Rindler horizons,
and a local finite causal diamond is a different
construction from a cosmological event horizon.
Cosmological event-horizon existence itself depends
on the future expansion history.

For background, compare:
- García-Heveling and Zeghib (2026), *Isometries of
  Spacetimes Without Observer Horizons*,
  https://link.springer.com/article/10.1007/s00220-026-05569-6
- Causal-structure review (2015), *Causal structures in
  inflation*, https://comptes-rendus.academie-sciences.fr/physique/item/10.1016/j.crhy.2015.07.005.pdf

These are context references, not proof that OI's horizon
thermodynamics applies universally.

## 4A. Finite-data countercontrol and pending source check

The companion bounded_observer_controls.py is a verification-only
finite regression separating finite deterministic record classes
from finite numbers of exact statistical states. An independent
integer-arithmetic implementation passed 30 relevant checks:

- A 12-bit truncation gives each prefix observer of depth n=1..12
  exactly 2^n finite public records. No universal bound over a
  hypothetical infinite family of observers follows.
- A binary response with Bernoulli parameter k/d for d in
  {1,2,3,4,8,16,32,64} has d+1 distinct exact response laws
  despite only two possible outcomes in each trial.
- For each bounded horizon K=0..8, the complete 12-bit source
  census gives 2^(K+1) deterministic K+1-bit records.
- States 0 and 7 have the same current bit-3 readout, yet
  reversible increment takes them to 1 and 8 with different
  next bit-3 readouts. A finite current-record quotient
  is not automatically an autonomous dynamical model.

The finite checks above were reproduced independently using
exact arithmetic. The Python source was pushed for ordinary
CI, but its exact-head Python execution has not been verified.
The all-observer and continuum-preparation results are
mathematical arguments, not extrapolations from these finite sweeps.

## 5. Relationship to OI gauge, and the hard-to-vary physical target

A putative ontology-neutral physics is a *family* of models
M=(S,T,mu,interface) modulo an equivalence defined
by the complete physical records accessible to the chosen
observers. Hidden cardinality is gauge-like **only** when
changing it preserves those laws. The G4 observational
quotient is not necessarily a microscopic G3
gauge-group transformation. A finite model representing
one bounded protocol may fail to represent the same
unbounded-time process (iid shift countercontrol).

The physical thesis to test is:

> For each physically realizable embedded observer whose
> operational access is bounded by a *sourced* finite
> information budget, the observer's finite-budget records
> admit a finite effective description. The underlying
> microstate space need not be finite, and the effective
> description need not be one finite reversible dynamical
> system stable under every extension of the protocol.

**A nontrivial improvement must still:**

1. Source or justify the boundary capacity and what
   qualifies as an embedded observer, without assuming
   a finite-area horizon for all worldlines.
2. Identify a preparation/readout/intervention ensemble,
   not just a collection of visible labels. Specify
   whether probabilities are exact or finite-precision.
3. Establish the dynamics and complete-record laws,
   including C4 hidden readback, without replacing the
   physical update by a fresh history-specific sampler.
4. Produce a hard-to-vary prediction not shared by an
   arbitrarily chosen finite surrogate, matched classical
   hidden-memory models, or a freely selected YM action.
5. Separately verify area-law entropy, physical quantum
   operations, Bell/no-signaling and Yang–Mills link-action
   sourcing. The fact that observers have bounded information
   does not prove those bridges.

**Status:** the finite-index theorem is elementary and
exact under explicitly named assumptions; tests of physical
horizon finiteness and a derived observer contract are OPEN.
No result from this note licenses promoting OI's original
finite-carrier reconstruction to a physically infinite
universal theorem or treating ontic infinity as a fact.
