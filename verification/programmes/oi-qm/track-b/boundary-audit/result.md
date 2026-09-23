# Barandes exact-input and indivisibility-role audit — result

Determination for `BARANDES-BOUNDARY-AUDIT.md`, executed on branch `barandes-boundary-audit` from
`main` at `44cb78080d48c786a27257271bff78cf99afd530`.

## Headline verdict

**Outcome B — rooted/conditional stochastic data suffice; a unique global invariant ensemble is not a prerequisite of the Barandes representation route.**

The result is version-sensitive but stable across the source history.

- In arXiv:2309.03085v1 (3 September 2023), Barandes defines a **generalized stochastic system** as
  a tuple `(C, T, Γ, p, A)`. The transition object `Γ` consists of first-order conditional
  probabilities `Γ_ij(t) = p(i,t | j,0)`. The standalone initial distribution `p(0)` is freely
  adjustable, and the paper explicitly states that `Γ` can be varied independently of the choice
  of initial standalone probabilities. The theorem then states that **every generalized stochastic
  system can be regarded as a subsystem of a unistochastic system**. No separate indivisibility
  hypothesis is imposed on that 2023 theorem.
- The current accepted version of arXiv:2302.10778 makes the logical boundary more explicit. An
  indivisible stochastic process has two basic fixed ingredients: the configuration space and its
  family of first-order transition maps. Standalone probability distributions are contingent data
  that may vary from physical run to physical run. The paper further identifies an indivisible
  process with an equivalence class of non-Markovian realizers sharing the same first-order
  conditional probabilities; higher-order trajectory probabilities are not fixed by those
  minimalist ingredients.
- arXiv:2309.03085v2 (5 February 2026) changes the terminology and time-indexing: the input is called
  an indivisible stochastic process and carries a conditioning-time set in addition to the
  transition family. It still explicitly separates the transition law from the freely adjustable
  standalone initial probabilities. The unitarization proof begins from the transition matrix
  entries, not from a stationary ensemble.
- arXiv:2507.21192v1 (27 July 2025) likewise treats the first-order transition probabilities as the
  nomological stochastic law and the standalone probabilities as contingent/epistemic run data.

The 2023 and later papers therefore differ in terminology and in how indivisibility is organized,
but not in the point relevant to #537: no primary-source theorem examined here requires a uniquely
selected invariant probability law on the entire stochastic state space as the input that makes the
transition law representable in Hilbert/unitary/Born form.

## Q1 — minimal input object

### 2309.03085v1: formal tuple versus load-bearing representation datum

The 2023 source formally defines a generalized stochastic system by

`(C, T, Γ, p, A)`,

where:

- `C` is the configuration space;
- `T` is the time set;
- `Γ` is the family of first-order transition probabilities from the reference time;
- `p` is the family of standalone probabilities;
- `A` is the stochastic evolution map/data associated with the standalone probabilities.

For the representation construction, however, the load-bearing probabilistic object is `Γ`: the
proof begins by using nonnegativity to write each transition probability as the squared modulus of
a complex amplitude, `Γ_ij = |Θ_ij|^2`, and then constructs the unistochastic dilation. The source
explicitly separates `Γ` from the freely adjustable initial standalone distribution.

Accordingly, the correct answer is layered:

- the **formal 2023 system object** includes `p`;
- the **transition-law representation datum** is the conditional transition family `Γ`, together
  with its state/time indexing;
- a particular run additionally chooses standalone probabilities if one wants standalone outcome
  probabilities, not merely transition probabilities.

### Current correspondence formulation

The accepted/current arXiv:2302.10778 formulation sharpens this to two basic fixed model ingredients:
configuration space plus the family of first-order transition maps. Standalone distributions are
contingent. It also states that the same first-order transition law admits many higher-order
non-Markovian realizers, so the complete path-space law is deliberately not part of the minimalist
quantum-correspondence input.

### Mapping consequence for OI

The OI object closest to the Barandes fixed transition datum is therefore a rooted conditional
family of the form

`Γ_t(a,j) = P(X_t = j | X_0 = a)`,

not a unique probability law over all of `Substratum.Conf`.

That is only a type-level correspondence. This audit does **not** yet prove that the C1–C4 physical
realization sources such a family; that is the next sourcing question.

## Q2 — ensemble requirement

The four frozen subquestions have these answers.

1. **A probability law on the full state/configuration space as a unique model datum — NO.**
   The current correspondence formulation treats standalone distributions as contingent run data.
2. **A stationary or invariant law — NO.**
   No audited theorem requires stationarity, invariance, or uniqueness of the initial distribution.
3. **A family of rooted/conditional transition probabilities — YES.**
   This is the central stochastic law used in the representation.
4. **A fixed preparation distribution for a particular experiment/run — MAY BE CHOSEN, BUT IS NOT
   CANONICALLY SELECTED BY THE CORRESPONDENCE.**
   If one wants standalone probabilities or a density operator for a run, an initial distribution is
   supplied. It is not required to be invariant and is not uniquely selected by the theorem.

### Consequence for #537

`EnsembleDetermined φ` asks for exactly one invariant probability law on the full configuration
space. That remains a valid theorem target and #537's negative result is unchanged. But it is a
**strictly stronger statistical-mechanics question than the Barandes transition-law representation
requires**.

Therefore the post-#537 gap must not be phrased as though a canonical global invariant ensemble is a
necessary prerequisite for applying the stochastic-quantum correspondence. The relevant OI sourcing
target is instead the preparation-level/rooted stochastic family.

No #537 theorem is retracted by this result.

## Q3 — what indivisibility adds

The source history makes a distinction that the corpus must preserve.

### 2023 theorem

The September 2023 theorem is stated for every generalized stochastic system. Hence indivisibility
is not a separate prerequisite for **existence** of the unistochastic/Hilbert representation in that
version. Ordinary Markov/divisible examples are not excluded from representability.

### Later correspondence and indivisibility work

The later papers reorganize the theory around **indivisible stochastic processes**. Their physical
claim is that generic indivisibility/non-Markovian failure of ordinary stochastic composition is
what supplies the specifically quantum-looking content: interference, and in the broader discussion
entanglement and quantum-information advantages, are interpreted through the mismatch between the
actual indivisible dynamics and a divisible/Markov approximation.

This does not license the converse gloss “unitary representability iff OI-style P-indivisibility.”
The terminology changed between versions, and the later definition organizes division around
conditioning/division times. Any comparison with OI's `PDivisible` predicate must therefore be made
as a separate definition-level audit rather than by matching the English word “indivisible.”

### Frozen answer

Indivisibility contributes **nonclassical structural/physical content**, not the bare existence of a
complex-amplitude/unitary dilation in the 2023 theorem. The later papers make indivisibility central
to the physical interpretation, but they do not turn a unique invariant global ensemble into an
input requirement.

## Q4 — representation freedom

The primary sources leave substantial freedom after `Γ` is fixed.

### Entrywise phase freedom

The first construction writes

`Γ_ij = |Θ_ij|^2`.

The complex matrix `Θ` is explicitly nonunique. Arbitrary entrywise phases leave the transition
probabilities unchanged. The later papers treat this as a Schur/Hadamard-type gauge freedom rather
than as physically fixed information in `Γ`.

### Hilbert-space/basis gauge freedom

The later formulation also develops a time-dependent unitary/Foldy–Wouthuysen gauge. Time-independent
members include ordinary basis changes; time-dependent members change the Hilbert-space trajectory
while preserving the stochastic/empirical content. Thus the Hilbert representative is not uniquely
selected by the transition probabilities.

### Hamiltonian freedom

Because of the time-dependent unitary gauge, the Hamiltonian transforms as a gauge potential and is
not itself gauge-invariant; in the corresponding Heisenberg-picture choice it can be gauged away.
Consequently no unique physical Hamiltonian or logarithm is obtained merely from `Γ`.

### Dilation/ancilla freedom

When the immediate amplitude matrix is not itself unitary, the correspondence uses a larger
unistochastic/unitary dilation and recovers the original transition law by marginalizing ancillary
variables. The dilation is a representation device, not a unique ontology fixed by `Γ`.

### Overall conclusion on freedom

The stochastic transition law fixes probabilities, not a unique amplitude matrix, phase structure,
Hilbert-space gauge, Hamiltonian, or dilation. OI therefore cannot cite Barandes representability as
sourcing its missing phase/control resources or its full operational quantum repertoire.

## Provenance sub-audit

The primary records resolve the chronology as follows.

- **arXiv:2302.10778**: v1 20 February 2023; v2 7 September 2023; v3 30 July 2025; journal
  publication in *Philosophy of Physics* 3(1):8 (2025). The current arXiv abstract notes that some
  material from the earlier manuscript was moved to arXiv:2507.21192.
- **arXiv:2309.03085**: v1 3 September 2023; v2 5 February 2026. Thus “2023” correctly describes
  the original theorem and “2026” the current revision. A corpus citation calling this source
  “2024” is not supported by the arXiv submission history inspected here.
- **arXiv:2507.21192**: v1 27 July 2025, *Quantum Systems as Indivisible Stochastic Processes*.
  The source explicitly identifies itself as carrying material removed from the earlier
  arXiv:2302.10778 manuscript.

The experimental arXiv HTML renderings of the two later sources currently display an internal
manuscript date different from the arXiv submission-history date. For provenance this audit uses the
arXiv version history, not that internal front-matter date.

No bibliography is edited in this round.

## Effect on the research frontier

The frontier is narrower than #537's post-audit paraphrase suggested.

The next sourcing target is **not**

> find a unique invariant measure on all of `Substratum.Conf`.

It is the realization-level object actually needed to induce the rooted stochastic law:

`visible/hidden split + visible preparation a + one common hidden prior μ_H + reversible evolution + visible readout`.

The next audit should ask whether the intended C1–C4 physical realization already supplies those
five pieces, and exactly which are primitive, derived, selected, or preparation data. It should not
ask bare `Substratum.Conf` to select an arbitrary observer map or a stationary ensemble unless a
later theorem genuinely requires one.

After that sourcing question is settled, the causal-readback question should be opened at the
**realization level**, not on a rooted matrix family alone. A neutral `CausalReadback` predicate can
then be tested independently for two consequences:

- history-conditioned readback (`C4w`-type content);
- marginal collision/revival (`C4e`, hence `C4r`, hence P-indivisibility).

This result does not assume that both implications hold; they must be proved or countercontrolled.

Only after those steps should the sourced rooted family be mapped back across the exact Barandes
boundary audited here.

## Preserved boundaries

This result does not:

- retract #537's invariant-ensemble theorem;
- prove that OI already sources a common hidden prior;
- identify Barandes's English “indivisible” with `OIBridge.CausalReadback.PDivisible`;
- redefine C4;
- prove `CausalReadback => C4e` or `C4r`;
- source phases, coherent controls, Hamiltonians, instruments, or composites;
- turn mathematical representability into a physical operational-equivalence theorem;
- edit manuscripts or Lean.

Status: **Outcome B recorded. #537 is stronger than the ensemble structure required by the Barandes transition-law representation; the next target is the rooted preparation family.**