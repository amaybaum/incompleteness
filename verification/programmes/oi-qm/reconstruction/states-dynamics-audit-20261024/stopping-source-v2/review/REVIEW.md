# Independent review of the almost-sure stopping candidate

**Verdict: ACCEPT within the stated scope; no blocking findings.**

Reviewed author commit: `2bf6cb952fe7bdec42c9ffdb8ce4fb7242921152` on #911.
The reviewed directory is
`verification/programmes/oi-qm/reconstruction/states-dynamics-audit-20261024/stopping-source-v2/`.
This is a separate-agent internal review by the continuation session's
`states_resume` reviewer, who did not author the inherited report or checker.
It is not external peer review, a new Lean certificate, or an owner designation.

## Provenance and replay

The preceding published commit `70a9b00ce85545ab918a84bcbcbc749d1ca16762`
contains the written candidate, claims and decision rule before the numerical
checkpoint. The four author files were recovered from the preceding session
without changing their bytes. Their retained SHA256SUMS passed. Fetches at
the reviewed immutable commit confirmed the Git blob identities of all four
files against the local review snapshot; INPUT-HASHES.json records both Git
blob identities and SHA-256 digests. Normal and optimized author executions
reproduced result.json byte for byte. Compilation succeeded.

The incomplete prior reviewer scratch was not adopted as review evidence.
The accompanying checks.py was written anew, imports no author code, and
uses only Python's standard library. It classifies whole dyadic cylinders
using rational root inequalities, rather than the author's integer-square-root
target digits. It agrees with the author's twelve cutoff results and adds
bounded tree controls at depths 32 and 64. These are implementation checks;
they are not a proof by finite extrapolation.

## Findings

1. The sampler proof is sound. Exactly one depth-n cylinder remains live,
   with probability 2^-n. The first differing digit terminates the comparison,
   so the tail vanishes, the expected coin-query count is 2, and the output-1
   probability is the supplied threshold. Unbounded worst-case resources,
   digit-computation cost, and unsourced native execution remain explicit.
2. The complementary thresholds have complementary nonterminating binary
   expansions. At each finite stopping depth they assign opposite outcomes.
   Their eventual joint laws have disjoint support and TV distance 1, despite
   equal stopping-depth marginals. Through cutoff K, the common timeout atom
   has mass 2^-K, giving TV 1-2^-K. The outcome marginal distance is sqrt(2)/2.
   The positive common-refinement control with independent timing is valid;
   the candidate's depth-1/outcome-1 support prevents such a refinement.
3. Countability concerns finitely described operations under a fixed
   realization map. It does not claim irrational probabilities are impossible,
   and does not dispose of an additional real-valued setting/oracle resource.
4. The pointwise mixed-hidden-state and fixed-G3 premises are essential.
   The remote mc-node3 source explicitly supplies those premises. On that
   reading finite branches have nonnegative partial-permutation Kraus maps;
   nonnegative sums and entrywise limits retain the invariant. Almost-sure
   termination on every relevant input is separately required for normalization.
   The Hadamard image of |1><1| has off-diagonal entry -1/2. Any invariant
   output differs in that entry by at least 1/2, hence in operator norm by
   at least 1/2. This is an operation-level fixed-identification separation.
5. FrozenSourcing.lean at `de6fe29324ade8a0826c18f7829786086dd590da` states
   finite-carrier sourcing and its unitary approximation ceiling. The author
   correctly treats the extension to stopping-time sums as a written argument,
   rather than claiming that finite Lean theorem certifies the infinite native
   substratum. No Lean build was run for this review.

The independent checker additionally enumerates all 720 bijections on a
two-visible-by-three-hidden configuration space. For each of three fixed
hidden inputs and four visible matrix units it compares direct permutation
and hidden trace with independently extracted output-fiber Kraus matrices:
8,640 exact comparisons pass. Exactly seven partial-permutation shapes,
including zero, occur. This checks the finite mechanism underlying the
invariant without substituting that enumeration for the written general proof.

## Replay and limits

From this review directory:

```sh
python3 checks.py --output replay.json
python3 -O checks.py --output replay-O.json
cmp result.json replay.json
cmp result.json replay-O.json
```

Both executions were byte-identical with structured verdict PASS. Every
required control raises an exception before PASS is produced. This review
accepts the abstract candidate and its bounded checks, not a physical source
for the supplied threshold, native timing, an infinite resource bank, a
reversible implementation, or full quantum equivalence. An alternative
operational quotient and restricted record-level A2 target remain distinct
questions. #885 and the manuscripts were not changed.

The cited Buffon-machines primary-source abstract was checked at
<https://arxiv.org/abs/0906.5560>; it supports the limited statement that exact
irrational-probability sampling from fair coins is established prior work.
No novelty is claimed for that phenomenon.
