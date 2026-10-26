# Separate-author review: states and dynamics

**Verdict: ACCEPT within the stated research scope, with no blocking
findings.** The reviewed author checkpoint is
`69aa29783971ef33f1ae6e4f34203a8579b93c03` on draft PR #911. Its five
top-level files were independently fetched by immutable revision, and the
author manifest verifies. `INPUT-HASHES.json` binds these reviewed bytes.

The initial source/proof report was first inspected at
`721dcd1799e186ff1e1f8dca0c0c3b6a34e341cb`; the final verdict covers the
subsequent resource diagnostic as well. This is separate-author internal
review, not external review, Lean certification or programme adoption.

## Source audit

The reviewer independently fetched the initial report and these main sources
at `de6fe29324ade8a0826c18f7829786086dd590da`:

- `verification/lean-mathlib/OIBridge/PairFlowEquivalence.lean`:
  `countable_not_pairFlowSourced` requires a countable set of matrix rays
  covering every available level-one single-outcome conjugation, with no
  unitarity restriction on its `V` quantifier. The report states that stronger
  source hypothesis explicitly. The exact-QM necessary pair-flow direction
  is present as `derivedOI_pairFlowSourced_of_qm`.
- `verification/lean-mathlib/OIBridge/DiscreteCompletion.lean`:
  the fixed-gate theory has dense unitary control when its angle divided by
  pi is irrational, and is not exact QM for every fixed angle.
  `DenseFiniteQM` is the conjunction of `KrausSoundExt` and `KrausDense`.
  The report does not confuse gate density with the full latter property.

These are source-reading checks, not a Lean rebuild or a new kernel theorem.
The report's countability conclusion depends on its explicit sourcing and
availability hypotheses. It neither excludes every finite classical model
nor claims that a clean Y readout supplies arbitrary quantum operations.

The review also read the applied corrections at the end of #885's
`oa-node1/NODE.md`, pinned at
`2d555f17c23bea31d32b3f5eb4c49d245b413a76`. The initial report respects those
corrections instead of reviving the superseded novelty claim or the broad
primary/non-primary-logarithm statement.

The primary-source abstracts of Dawson and Nielsen,
<https://arxiv.org/abs/quant-ph/0505030>, and Hardy,
<https://arxiv.org/abs/quant-ph/0101012>, support the narrow background use:
finite-sequence approximation and continuous reversible transformations as
an axiom, respectively. Neither is evidence of native lattice availability.

## Resource proof and scope

The six-bit lower bound correctly concerns all randomness in the conditional
sampler at fixed input and relevant history, with a uniform `2^B`-atom sample.
It is not presented as a universal lower bound on newly allocated bits when
old reservoirs or nonuniform conditioning remain available. Fresh fair `z`
is independent of the post-Y `(a,b)` pair on success.

The six cell probabilities are `(5,5,3,3,2,2)/20`. The `3/20` cell forces
`20 | M` for a positive successful atom count M. This immediately excludes
always-success finite fair-bit sampling. At the explicitly illustrative rate
`5/16`, M is `5*2^B/16`, so the first feasible bank has B=6 and M=20.
Retaining the seed while XOR-writing a label into three initially blank bits
is a reversible extension, not an erasure or a native implementation proof.
The additional blank-register resource is explicitly counted.

For `p=(2+sqrt(2))/4`, the residual of `8q^2-8q+1` at `q=n/M` has nonzero
integer numerator, hence magnitude at least `1/M^2`. Its factorization is
`8(q-p)(q+p-1)`. Since `0<p<1` and `0<=q<=1`, the second factor in absolute
value is strictly below 8, giving the claimed strict bound. This analytic
argument is general; the finite enumeration only tests its implementation.
The bracket construction proves convergence of the Bernoulli examples, not
approximation of every quantum instrument. The irrational-prior countercontrol
correctly prevents a no-go based only on finite hidden-state cardinality.

## Executable checks

Both normal and optimized executions of the author's `checks.py` reproduced
its structured `result.json` byte for byte. The reviewer inspected the exact
quadratic-field arithmetic and the deliberately wrong calibration/fixed-z
controls. A required failure raises before a PASS object is produced.

The reviewer's `checks.py` imports no author module. It independently:

- checks the success-rate feasibility threshold at bit counts 0 through 16;
- constructs an interleaved seed allocation, verifies all 512 reversible
  states, the six-cell successful law, 44 failures, and both decoded carrier
  laws;
- rejects a fixed-z model despite its correct `(a,b)` marginal;
- verifies 2,144 rational error comparisons by rational ordering and squaring,
  without the author's quadratic-field sign implementation;
- locates 16 dyadic brackets using binary search, independently of the
  author's integer-square-root formula.

Run `python3 checks.py` or `python3 -O checks.py` from this review directory.
Both reviewer outputs match `result.json`; Python compilation also succeeds.
The only dependencies are Python's standard library. `SHA256SUMS` binds the
review files, and `INPUT-HASHES.json` binds the author files at the revision
named above. Neither output is a kernel certificate or a native-reset result.

## Remaining limits

The native lattice must still implement the reset and preserve the complete
conditional resource law. The supplied calibration and private-access policy
are not derived by this audit. The countability conclusion remains conditional
on the stated realization and availability hypotheses. A native operation
map, a full state-space correspondence, unrestricted composition and a full
equivalence proof remain open. No manuscript claim is changed by this review.

No remote file, PR comment or branch was changed by the reviewer.
