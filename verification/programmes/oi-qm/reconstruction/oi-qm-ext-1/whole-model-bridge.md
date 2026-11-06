# Whole-model bridge assessment for the amplitude/readout extension

**Status: WIP / UNVERIFIED, paper only.**
Accountable Issue #1169; guiding draft PR #1173.
Owner authorization: [6 November 2026](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-6693973889).
Starting checkpoint: `1514d3bbd2f85147fce227b50d2ea3ec6c14ca31`.
The accepted endpoint contract is `endpoints.md`; the B1/B2/B3 sources stay preserved.

## 1. One candidate extension

Assess the natural operational closure E-AR of the current amplitude-control,
public sign-readout and detector-controlled exchange architecture.
Its real carrier, exact signed control, point preparation, sensor coupling,
ready references, seed measure and record access are added physical inputs,
not consequences of finite native OI. Its admissibility is stated through those
primitive equations and operational access, not equality to quantum tables.

Retain B1's complete fixed-duration family U(theta)=exp(i theta X), the point
signal e1, and the reversible copy r <- r XOR 1[x1>0].
The closure under assessment allows preparation by a drive, followed by another
independently chosen drive and the same fixed sign sensor, with a fresh ready
record. It also retains B3's coupled exchange and public record.
This composition closure is an explicit proposed extension condition; B1's
one-record checkpoint alone does not source it. One common reversible finite
controller will be specified for the two-drive sign subinterface.
No inaccessible-reservoir assumption is used to remove an already available read.

## 2. Proposed correspondence and first test

The initial state proposal is z -> zz*/||z||^2, with the existing drive and
basis-instrument interpretations. B1 already refutes that dictionary for the
full sign interface. Assess whether a different, even nonlinear or larger
finite-dimensional, state assignment can preserve the same prepared states
and preparation-independent measurement labels.

The necessary prepare-and-measure bridge asks for a single finite d, density
operators sigma(theta) on C^d, and binary effects F(phi), independent of the
preparation label, that reproduce every native two-drive/sign probability.
The assessment will check the exact operational law, possible distinguishability
bound, access to preparation/controller metadata, and the scope of any resulting
obstruction. A finite menu and per-experiment enlargement are not the full target.

## 3. Full proof obligations

Map this necessary state/readout bridge to the existing FiniteOperationalTheory
interface and GeneralCarrier characterization without reproving that theorem.
Separately track complex-linear/CP operations, all quantum preparations and
instruments, spectators/composites, setting independence, common adaptive history
semantics, and compatible resources for every finite protocol.

Both directions need one fixed interpretation over the full declared interface.
Any unrestricted model class must be independently defined and have a
nonvacuous realization; the completed Gate A class is not asserted nonempty here.
An exact continuum target requires an explicit parameter/resource policy;
the current real-coefficient idealization is not a finite-alphabet derivation.

## 4. Completion and review

Produce the candidate specification, proposed correspondence, first precise
bridge lemma or demonstrated limitation, and an accountable source/dependency
map. #866 keeps physical coupling/access, #1059 measure selection, #1147 ready
supply, #1032 retention/coherence and #1143 its distinguishing test.

Independent review will assess the pushed exact paper, including whether a
counterexample is scoped to this candidate rather than all OI, all encodings
or all quantum realizations. No full equivalence, native availability,
physical premise adoption, execution, implementation, merge or claim promotion
is asserted. Ordinary PR CI is separate verification.
