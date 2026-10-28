# Coherent permutation entropy profiles — research only

Base: `20ca05fe9e7e460de29e08f7a21029042fa45b12`. Related: research backlog #970,
source correction SC-36 #978, Introduction #918. This is a separate exploratory
research branch, not a revision of PR #982 or a restoration of GR A.8–A.9.

## Question and explicit candidate

Can coherent preparations and an explicitly specified finite permutation ensemble
yield a nonvacuous finite entropy-profile theorem under nested radiation cuts?
The configuration-state counterexample retained by SC-36 remains binding: every
configuration orbit has zero entanglement across coordinate-aligned partitions.
The two-qubit coherent CNOT witness instead has entropy 0, 1, 0 bits.

The candidate ensemble is deliberately mathematical: prepare k coherent |+>
qubits and n−k configuration |0> qubits, then choose a uniformly random
invertible binary linear map L on n bits and apply its configuration permutation.
The resulting coherent state is uniform on a k-dimensional binary subspace V.
At cut R={1,...,r}, B its complement, define von Neumann entropy in bits.
Written candidate conclusions, with retained exact controls (not yet independently accepted):

- S_R = k − dim(V∩R) − dim(V∩B), with a flat nonzero Schmidt spectrum.
- The mean purity is computable exactly from one- and two-vector incidence in
  uniform binary subspaces. For n=2m, k=m this may give a mean nested-cut profile
  within two bits below min(r,n−r), with zero entropy at both endpoints.

The ensemble is not Haar measure, an OI-derived preparation, a physical scrambling
mechanism, an evaporation law, or a statement about a single permutation's orbit.
A fixed sampled L and a nested cut schedule define the proposed finite profile;
calling the cut radiation does not make qubits propagate or decouple physically.

## Acceptance criteria and controls

Give a self-contained Schmidt-decomposition proof, exact incidence counting,
explicit coherent examples and configuration/unscrambled/non-Haar countercontrols.
Use bounded rational controls that compare independent state-amplitude contraction
against the subspace formula. Obtain independent review before any accepted claim
or manuscript/coverage upgrade. No Lean certificate is presently claimed.

Prior work: Page, Average entropy of a subsystem (1993),
https://arxiv.org/abs/gr-qc/9305007; Smith and Leung, Typical entanglement of
stabilizer states (2006), https://arxiv.org/abs/quant-ph/0510232. These establish
the context; this restricted positive-amplitude binary-subspace ensemble is not
the whole stabilizer ensemble, and no novelty claim is made.

No merge, native-round F/E designation, dispatch or physical premise adoption.

## Constructive checkpoint

`entropy-profile-proof.md` gives a self-contained Schmidt decomposition, exact
subspace-intersection distribution, independently derived mean purity, and a
mean tent bound with a shared-state union bound over all nested cuts. The mirror
Bell-pair example is an exact tent without an evaporation or scrambling claim.
`exact_controls.py` contracts state amplitudes independently of the intersection
formula, checks the full reduced-spectrum polynomial identity, and compares the
counting distribution with direct subspace enumeration. Larger exact moment
checks exercise the two independently derived formulas beyond the enumerated
range. Configuration, unmixed coherent, incoherent-mixture and repeated-CNOT
countercontrols are retained. `exact-results.json` records the bounded run.

This candidate and its controls await independent review and ordinary PR CI.
No manuscript, coverage, Page/black-hole status or physical premise is upgraded.
