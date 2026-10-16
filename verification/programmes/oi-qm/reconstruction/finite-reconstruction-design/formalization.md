# Finite algebra and reachability design

This record accompanies the five research Lean modules in this directory.
They are design sources outside the adopted `OIBridge` population. They change
neither the mathematical hypotheses of the written cone theorem nor a native
round's control plane. No F is designated.

Compilation status: all five modules compile against the adopted library at D
`dee3b5ae6fd3fb20fa1bad3337963e5af947f3a4`; the design branch leaves
`verification/lean-mathlib` unchanged from D. The exact design head is
`11fbcd597accf7fbe2eed9ef9c81107cd100f2f2`; GitHub Actions
[run 38866415970](https://github.com/amaybaum/incompleteness/actions/runs/38866415970),
job `116860178759`, is all green. The run checks this directory's `SHA256SUMS`
before it compiles, so the compiled bytes are those listed. The source hashes
are:

| Module | SHA256 |
| --- | --- |
| `FinitePauli.lean` | `4af38e2e151390edf8ca23cdec94be06b7b4b1f9c72c57292a5374b7ca195b8e` |
| `FiniteWalsh.lean` | `d4815ec809fa37fefabe786886efb860f1da02788cea4f7e048e34726da8a5f0` |
| `FiniteCircuit.lean` | `70ce411d9cd830b8d73a5eee3e1eed758da4633802b9734961a6a0021ecc9763` |
| `FiniteReach.lean` | `5112671f1317d60e23b2fcb4a20953f38771e9c1f2f03b2c553f1360947985b4` |
| `FiniteReachTable.lean` | `8c397a06510a9f447590c1662029d6d9e21fa31a97fd4893116f51f447044df5` |

The modules contain 129 theorems: 14 Pauli/tensor/dictionary theorems, six
Walsh theorems, three circuit theorems, 77 gate, word, multiplexor,
reachability and matrix-cone theorems, and 29 table theorems. All 38 requested
main axiom reports list only `propext`, `Classical.choice` and `Quot.sound`.
The successful log contains no `sorryAx` and no errors. No `sorry`, additional
axiom or admitted synthesis hypothesis appears in these sources.

That same run replays the 242 finite controls and five mutations, the historical
descent probe and the independent descent controls, checks the saved hashes,
and compiles the historical KN-DESC design. It also passes the 303-record
legacy check, all 46 receipts and artifact placement. This is research design
evidence; it is not an F attestation or a native execution. Documentation added
after this exact head reports its build and does not change these source bytes.

Earlier development builds rejected type transparency, finite-sum ordering,
delta-case simplification and division-normalization steps in the proof sources,
and an equality-instance mismatch in the reachability module, described below.
Those failed builds supplied no certification. The corrections retain the
mathematical statements and the all-k argument's stated hypotheses.

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
algebraic laws, rather than a physical compatibility postulate. The cone
theorems below do not use these two modules.

## Gates, words and exact multiplexors

`FiniteReach.lean` imports `FinitePauli` and the adopted `EqvK2Generation`.
`cnotM k i j` and `localM k j V` are defined by recursion on the token count: a
gate on the last token is a block-diagonal family over the earlier tokens
(`blockFam`), and a gate on an earlier token is tensored with the identity on
the last. `IsWord k` is the closure under products of unit scalars, `cnotM k i j`
with `i < j < k`, and the third-axis flow `phaseMat (cos t) (sin t)` and the
cyclic matrix `cycMat` at each token `j` with `0 < j < k`. Unit scalars
conjugate every matrix to itself (`pres_scalar`), so every word preserves any
set that the named generators preserve (`pres_of_isWord`). They are needed
because `phaseMat` has determinant `cis t`: a unit scalar times the flow gives
each diagonal special unitary on a token (`isWord_local_dUnit`). The conjugate
transpose of a word is a word (`isWord_conjTranspose`), which supplies the
inverse-word step of argument section 2.

The multiplexor of argument section 3 is proved without the Gray schedule.
`sign_induction` shows that a predicate on real functions of n bits holds for
every function when it is closed under addition, holds for constants and is
stable under multiplication by the sign of each bit; zero controls are the
constant case. For families of diagonal rotations, addition is block
multiplication, a constant is the local flow on the target, and multiplication
by the sign of bit `i` is conjugation by `cnotM (n+1) i n` (`flipX_rz`). Hence
`isWord_rzFam`: every family of diagonal rotations on a target other than the
first token, controlled by all earlier tokens, is a word. Real rotation
families are the cyclic conjugates of diagonal families on the target
(`rotRe_eq`, `isWord_rotReFam`). `isWord_suFam` applies the adopted exact
Euler factorization `su_euler` branchwise and composes the three multiplexors in
the factor order. Spectators are qubit tokens: `isWord_lift` adds a later token
with the identity. Arbitrary finite spectator carriers are not needed for the
cone theorem and are not treated in this module.

`FinitePauli` declares its carrier equality instance classically. An instance
synthesized at an explicit successor carrier `Bits (n+1)` is the product
instance, and at `Bits 0` the `Fin 1` instance; neither is definitionally equal
to the classical one, so an identity matrix written at such a carrier does not
unify with one elaborated generically. `FiniteReach` declares the structural
instance `bitsDecEq` at high priority, and the two added modules elaborate
their matrices with it.

## Reachability and the matrix-form cone theorem

`reach_prod` proves that every vector x on k + 1 tokens is `U` applied to
`a ⊗ |0⟩ ⊗ … ⊗ |0⟩` for a word `U` and a first-token vector `a`. Each step
applies the multiplexor of the inverse blocks `(suTo v_b)†` of argument section
4 to the lifted word for the vector of block norms; a zero block uses the
identity, which is the adopted value of `suTo` at zero. The first token is never
driven. `reach_norm` rescales to unit one-token vectors with a nonnegative
factor, and uses a unit-scalar word for the scalar empty tensor at k = 0.

For a set C of k-token matrices, with preservation by the named generators
written `drive`:

- `subset_psd_of_maxCone_drive`: Hermitian members, nonnegative expectation on
  every product vector and `drive` give C ⊆ PSD. Products in C and cone
  closure are not hypotheses.
- `psd_subset_of_products_cone_drive`: every product of trace-one PSD one-token
  matrices in C, closure under addition and nonnegative real scaling, and
  `drive` give PSD ⊆ C. The product-test bound is not a hypothesis. A PSD
  matrix is a finite sum of rank-one terms by the adopted
  `psdFactorization_discharged`.
- `kCone_eq_psd_of_drive_maxCone` combines the two inclusions.
- `driveInvariant_of_eq_psd`: C = PSD gives `drive`, by PSD conjugation.
- `kCone_eq_psd_iff_drive_maxCone`: under the Hermitian, product, cone and
  product-test hypotheses, C = PSD if and only if `drive`, with
  `driveInvariant_of_eq_psd` and `kCone_eq_psd_of_drive_maxCone` as the two
  directional witnesses.

## Table form

`FiniteReachTable.lean` carries these statements to real Pauli tables on the
recursive label carrier. `dictionary_prodTab` identifies the dictionary image
of a product table with the product of one-token matrices, and
`trace_dictionary_mul` gives the trace pairing of two dictionary images as their
table pairing divided by `2^n`. `blochH u` is the homogeneous Bloch vector of a
one-token vector; `tokMat_blochH` identifies its matrix with `u u†`, and
`lor_blochH` places it in the forward cone. `quad_dictionary_prodVec` writes the
expectation on a product vector as a forward-cone product pairing. The generator
actions on tables are conjugation through the dictionary,
`tabAct k U w = coordinates k (U · dictionary k w · U†)`.

- `tableCone_eq_psd_of_drive_maxCone`: a set K of tables that contains the
  product tables of ball states, is closed under addition and nonnegative
  scaling, is nonnegative on every product of forward-cone vectors and is
  carried into itself by the actions of the named generators is the set of
  tables with PSD dictionary image. Its lower inclusion uses only pure products
  (`psd_subset_of_pure_cone_drive`).
- `maxConeTab k` is the set of tables nonnegative on every product of effects
  of the ball. `lorPair_nonneg_of_maxConeTab` scales each forward-cone vector to
  an effect (`isEffectOn_lorScale`, through the adopted `affOf`), so the effect
  form of the bound implies the forward-cone form. Only this direction is
  compiled; the theorem does not use the converse.
- `tableCone_eq_psd_of_drive_maxConeTab` is the table theorem with
  `K ⊆ maxConeTab k`.
- `tableDrive_of_eq_psd` gives the actions from equality, and
  `tableCone_eq_psd_iff_drive_maxConeTab` states the equivalence with these two
  directional witnesses.

## Remaining obligations

The synthesis steps between the generic algebra and the all-k theorem, namely
concrete gates with qubit spectators, exact multiplexors in the Euler factor
order, recursive preparation including zero blocks, the undriven first token and
the scalar phase, and both cone inclusions, are established in the form above.
The following steps separate the compiled theorems from the statement proposed
in #829 and from the k = 2 recovery in `argument.md`:

1. Prove that `tabAct` of each named generator equals the explicit coordinate
   action proposed in #829: the CNOT sign-and-label map and the one-token
   homogeneous action on the target slot. The table hypotheses are otherwise
   stated through the dictionary.
2. Transport the recursive carriers `Bits k` and `Labels k`, with the
   dictionary, product tables and gates, to `Fin k → Fin 2` and
   `Fin k → Fin 4`.
3. Implement the five k = 2 transports of argument section 5 and recover the
   statement of `pairCone_eq_Q3_of_drive_maxCone` without using it.
4. Optionally, construct the cyclic Gray schedule and prove the prefix-parity
   and Walsh correspondence, including zero controls. This identifies the
   compiled multiplexor with the Gray-ordered word of argument section 3; the
   cone theorems do not need it.

In particular, these modules do not prove arbitrary unitary universality. The
target remains exact pure-state reachability from a product preparation. They
also supply no implementation-class membership for KN-DESC and discharge no
physical source or state/operation compatibility premise. Identifying the
named generators with physical operations, and the cone with a physical state
space, remains a premise.

The existing exact three-token checker remains a finite design comparison; it
does not certify the declarations above.
Productivity classification: ELABORATING, on the consistency axis.
