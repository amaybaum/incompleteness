# Conditional preservation induction: research design

Status: research/design milestone, not native execution, freeze, receipt,
adopted kernel module or physical compatibility principle. Base: #831 at
`5f614d60c3234cf35bc9b15e892388d576f77aa1`; drafting snapshot D remains
`dee3b5ae6fd3fb20fa1bad3337963e5af947f3a4`.

Evidence legend: [W] written universal argument; [X] exact finite controls;
[D] research design source; [K] compiled research-design theorem. Lean/lake
and a Mathlib cache remain absent locally. GitHub compiled the design at
`e684897da41b1c3d066b880194c9beb87a19b7ad`; see [build-status.md](build-status.md)
for the exact source, successful run and checked standard axiom reports.

## Fixed question, decision rule and productivity test

The question is whether independently given preparation sets C_S are
preserved branchwise by every available finite protocol if they satisfy the
primitive, attachment/discard and additive-closure premises stated below.
Productivity test: identify precisely which preparation hypotheses the
actual five-constructor induction uses; do not merely rename protocol
preservation as a physical source.

Before the exact controls were run, the decision rule was: all finite
positive and countercontrols must pass, the independently implemented paths
must agree on the full sample-manifest digest, and every named wrong-step
guard must reject its corresponding variant. These tests certify their
finite examples only. The universal research-design kernel verdict also
requires compilation and checked axiom reports. These passed at the pinned
build; native adoption and positive-premise Lean instances remain separate. No
native-round verdict token is emitted by either script.

## Universal conditional statement [W, D]

Fix an implementation class I on every finite carrier, and independently
specified sets C_S of matrices on those carriers. Assume:

1. Each C_S contains 0 and is closed under addition.
2. For each admitted K with K†K=I, KXK† belongs to C_S whenever X does.
3. Each branch PXP of each admitted native register readout preserves C_S.
   The projector is the actual reindexed `readProj` in `InstAvail.readout`.
4. For every positive m, X ↦ X⊗I_m/m sends C_S into C_(S×Fin m).
5. For every positive m, partial trace sends C_(S×Fin m) into C_S.

Then every branch of every derivation of `InstAvail I S O F` preserves C_S.
The preparation family is not defined by reachability, by the operations,
or by PSD. Hermiticity, closedness, convexity, real scaling and trace
normalization are not used. In particular, a full cone-structure package is
sufficient but stronger than the proof needs; no minimality is asserted.

Proof by induction on the actual constructors at D:

- `op`: apply premise 2 to its admitted isometry.
- `readout`: apply premise 3 to its indexed projector branch. A nontrivial
  projector is not an isometry, so premise 2 cannot discharge this case.
- `coarse`: apply the induction hypothesis to each summand in the finite
  fibre. Addition closes the fibre sum; the empty fibre uses 0∈C_S.
- `bind`: apply the first induction hypothesis to X, then the continuation
  induction hypothesis for that particular first outcome to its output.
- `discard`: attach I_m/m using premise 4, apply the induction hypothesis
  on the enlarged carrier S×Fin m, then use premise 5. The attached label is
  summed inside discard and is not a new exposed outcome.

The sum of all unnormalized branches also belongs to C_S, using finite
addition. This is a separate statement from aggregate trace preservation.
The same all-carrier hypotheses apply to `instAvail_spectator` after its
inventory premises `ContextStable` and `LabelInvariant` establish spectator
availability. These inventory premises are not cone-preservation premises.

Transport has two distinct readings. The supplied design corollary says
the transported instrument preserves C_S' by the all-carrier theorem and
label-invariant inventory. It does not assert that reindexing maps C_S to
C_S'. Identifying the two preparation spaces requires an additional
explicit cone-covariance premise. Similarly, no cone-covariance premise is
needed merely to prove preservation of the assigned cone on S×R.

`PreservationInduction.lean` states the core, finite branch sum, spectator
and transport results outside the adopted OIBridge tree. Only zero/additive
closure is exposed. The four design theorems compile with standard axioms.
Positive-premise Lean instances remain obligations before a freeze is proposed.

## Positive comparisons [W, X]

Quantum: take C_S to be all PSD matrices. Isometric conjugation and
projection preserve PSD since v†KXK†v=(K†v)†X(K†v)≥0. Uniform attachment
is block-diagonal copies of X/m, up to tensor ordering. Partial trace is
a sum of compressed PSD blocks. Zero/additive closure is immediate.
These are universal written instances, not new kernel-certified instances.

Classical: take C_S to be nonnegative diagonal matrices on each labelled
carrier, and the admitted class to consist of matrices with at most one
nonzero entry in each row and column. Its isometric members are monomial
unitaries, and its coordinate readout projectors are admitted. The unitaries
permute diagonal entries; native coordinate projectors select entries.
Uniform attachment copies/rescales nonnegative entries, and discard sums
them. All five constructor cases therefore remain within the classical cone.

Exact examples use two classical basis preparations, a mixed classical
preparation, a real quantum pure preparation and a complex quantum pure
preparation. A single protocol contains all five constructors: two nested
positive-size uniform-ancilla discards; native readout of the inner ancilla;
a CNOT continuation selected by that outcome; coarse-graining with an empty
fibre; and a final outcome-dependent swap or rational rotation. All final
unnormalized branches are checked for PSD; classical branches additionally
remain diagonal. A separate nontrivially reindexed register readout checks
that the implementation does not ignore carrier labels. The largest
intermediate carrier has dimension 8; final outputs have dimension 2.

The primary path interprets the protocol constructors with exact SymPy
matrices. The independent path uses its own rational complex arithmetic,
enumerating the uniform preparation labels, projected label and discarded
labels as Kraus paths. It imports neither SymPy nor the primary script.
For PSD of the final 2×2 matrices it checks the two diagonal entries and
determinant; the primary checker uses all principal minors. The digest
covers every entry of every final branch on all five preparations.

## Countercontrols and named wrong-step guards [W, X]

Operation: H|0⟩⟨0|H† has off-diagonal entry 1/2. Hadamard is an isometry,
and the output has trace 1, but it lies outside the classical diagonal cone.
Thus inventory availability plus normalization does not supply primitive
preparation preservation. This is not asserted to be a model satisfying
every other all-carrier hypothesis of the conditional theorem.

Readout: the all-carrier scalar-positive family C_S={λI_S:λ≥0} is preserved
by each square isometry (finite-dimensional K†K=I implies KK†=I), zero,
addition, uniform attachment and discard. Uniform attachment sends λI_S
to (λ/m)I_(S×Fin m); discard sends λI_(S×Fin m) to mλI_S.
But coordinate readout on C_(Fin 2) sends I to diag(1,0), a nonscalar
projector. All the other preparation hypotheses hold, even with fullClass.
The aggregate of its two readout branches is still I. This witnesses that
the separate readout clause cannot be replaced by isometry preservation or
aggregate normalization.

Discard: a second all-carrier example sets C_S=diagonal PSD when |S|=2,
and C_S=PSD otherwise. Admit matrices with at most one nonzero per row and
column at dimension 2, and every matrix otherwise. Additive closure,
primitive operation preservation and native readout preservation hold on
every carrier. Uniform attachment also preserves these sets: its only
nontrivial destination of dimension 2 comes from a one-dimensional source,
which attaches a scalar multiple of I_2; attachment from dimension 2 either
has m=1 or lands in the ordinary PSD cone. Nonetheless, at dimension 4 an
admitted H⊗I_2 sends |0⟩⟨0|⊗I_2/2 to |+⟩⟨+|⊗I_2/2, and partial trace
returns |+⟩⟨+| outside C_(Fin 2). This inventory is label invariant and
context stable: a nontrivial added context enlarges dimension 2 into a
full-class carrier; a context enlarged into dimension 2 comes from a
one-dimensional scalar operator. Thus even those inventory conditions do
not supply the omitted all-carrier discard premise. The exact layer checks
the enlarged isometry, PSD, normalization and failing reduced preparation.

Seven finite guards reject: aggregate substituted for branch membership;
projectors treated as isometries; pure attachment substituted for I/m;
an empty coarse fibre omitted; partial trace replaced by a single block;
the cone-discard premise omitted; and inventory label invariance treated as covariance of arbitrary labelled
preparation sets. For the last guard, a relabelled diagonal pure state does
not belong to a scalar cone assigned to the destination carrier, although
fullClass remains label invariant. These are wrong-step countercontrols,
not proofs that the full premise package is minimal. They do not mutate or
test a Lean proof.

## Measured results and replay [X]

On 2026-10-13, using SymPy 1.14.0 for the primary path and only Python's
standard library for the independent path:

- Primary: 107 exact controls pass; seven named wrong-step guards reject.
- Independent: 43 exact controls pass.
- Sample manifests agree at SHA256
  `a1f82e289ba07a4c60dd6b56396dcdf7c0c217b2ff49a8d779f1c4e923842ea9`.
- Saved stdout replays byte for byte. `SHA256SUMS` covers the source and
  saved outputs; it excludes this mutable research result note.

Run from the repository root:

```sh
python3 verification/programmes/oi-qm/reconstruction/preservation-induction-design/exact_check.py
python3 verification/programmes/oi-qm/reconstruction/preservation-induction-design/independent_check.py
```

The first command requires SymPy 1.14.0; neither command claims the
universal theorem is kernel certified. Conditional soundness is [K] at the
pinned research-design build; these scripts remain finite evidence. They stop before
printing checked-result text when any required check fails.

## Earned scope and remaining obligations

The protocol-level argument is CONFIRMING: closure under constructors is
the anticipated induction. Its premise audit is ELABORATING: only zero/add
is used, and the actual mixed-ancilla and readout obligations are explicit.
It reduces preservation verification to five kinds of constructor
obligations, not to a finite inventory of concrete physical operators.
No preservation premise is physically sourced, and no bridge cone is
asserted to extend to an all-carrier family satisfying them. No claim of
K2, P0, Q3 reconstruction, native execution or adoption changes.

Before any F proposal: retain a reviewed compiled design,
instantiate quantum/classical premise controls in Lean, settle prospective
adoption/registry/workflow edits, and pin a concrete reviewed design package.
No historical record or maintained manuscript is edited by this milestone.
