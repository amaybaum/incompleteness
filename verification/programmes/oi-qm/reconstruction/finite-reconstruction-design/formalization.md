# Generic finite algebra design

This record accompanies the three research Lean modules in this directory.
They are design sources outside the adopted `OIBridge` population. They change
neither the mathematical hypotheses of the written cone theorem nor a native
round's control plane. No F is designated.

Compilation status: pending a fresh build against the library at D
`dee3b5ae6fd3fb20fa1bad3337963e5af947f3a4`. A source proof body is not kernel
certification. Each main declaration requests `#print axioms` in its build log;
there are no `sorry`, additional axioms or admitted synthesis hypotheses in
these sources.

## Pauli coordinates and spectators

`FinitePauli.lean` imports the adopted `EqvK2Schema` and uses its one-token
Pauli matrices and entrywise completeness theorem. Its recursive carriers are
`Bits 0 = Fin 1`, `Bits (n+1) = Bits n × Fin 2` and, correspondingly, Pauli
labels with `Fin 4`. This retains the scalar empty tensor and avoids an
enumeration or fixed-dimensional case split for n.

The generic tensor lemmas establish multiplication, trace, conjugate transpose
and conjugation intertwining for arbitrary finite spectator carriers. The
recursive Pauli proofs establish Hermiticity, trace orthogonality and entrywise
completeness for every n. Completeness and orthogonality give separately named
dictionary inverse directions:

- `coordinates_dictionary_real` reads every real table back after mapping it
  into Hermitian matrices.
- `dictionary_coordinates_real` reconstructs every Hermitian matrix from its
  real Pauli coordinates.

The complex-coordinate versions prove the full matrix expansion before the
Hermitian restriction. These are mathematical carrier identities. Identifying
this carrier with the framework's physical n-token states remains a premise.
The explicit reindexing to `{0,1}^n`, and the five transports to the existing
two-token carrier, are not implemented by these definitions.

## Walsh inversion and finite circuit algebra

`FiniteWalsh.lean` uses the recursive binary carrier. The base Hadamard matrix
is `[[1,1],[1,-1]]`; tensor recursion proves exact row orthogonality for every
number of controls. `walsh_permuted_orthogonal` accepts any bijective column
ordering. `multiplexorAngles_recover` proves the prescribed real branch angles
are recovered from the finite inverse Walsh transform. No density, closure,
rational-angle restriction or asymptotic approximation occurs.

A Gray ordering is only one permissible permutation in that theorem. It is
not assumed to be an already synthesized circuit. `FiniteCircuit.lean` proves
the separate group identity for a chronological list of rotation-then-flip
steps: a one-parameter rotation law, an involutive flip and the exact crossing
law give a normal form with accumulated signed angle and flip parity. A closed
parity word is exactly its accumulated rotation. These hypotheses are explicit
algebraic laws, rather than a physical compatibility postulate.

## Remaining synthesis obligations

The following steps still separate these identities from the all-k cone
theorem in `argument.md`:

1. Construct a cyclic Gray permutation for every positive control count, prove
   consecutive words differ in one named bit, and prove the circuit prefix
   parity equals the associated Walsh character. Handle zero controls
   separately. The inversion lemma supplies angles after that correspondence.
2. Instantiate the abstract circuit in the one-token unitary group, transport
   its rotations and controlled flips to arbitrary spectator carriers, and
   give the concrete finite word under the asymmetric generator inventory.
3. Transport the adopted exact SU(2) Euler argument to a token with arbitrary
   spectators, then concatenate the three multiplexors with a consistent
   circuit order.
4. Formalize recursive block preparation of an arbitrary vector, including
   zero blocks, the undriven first token and scalar phase, and derive both cone
   inclusions separately.

In particular, these modules do not prove arbitrary unitary universality. The
target remains exact pure-state reachability from a product preparation. They
also supply no implementation-class membership for KN-DESC and discharge no
physical source or state/operation compatibility premise.

The existing exact three-token checker remains a finite design comparison; it
does not certify the declarations above or their remaining synthesis links.
Productivity classification: ELABORATING, on the consistency axis.
