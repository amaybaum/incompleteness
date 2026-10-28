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
Proposed exact conclusions to verify:

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
