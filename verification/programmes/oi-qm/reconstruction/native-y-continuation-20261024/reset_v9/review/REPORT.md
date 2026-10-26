# Separate review of the native masked route

**Verdict: accept within the stated pointwise scope; no blocking findings.**

Reviewed author commit:
`328b74b88eaeddc798bf4693af78a571bf429787`, subtree `reset_v9/`.
The report, plan, checker, structured result, provenance and checksum file
were fetched at that immutable SHA; their Git blob IDs match the six local
files used in this review. `INPUT-HASHES.json` pins the reviewed bytes.

The reviewer did not author the masked-route checker or report. This review
uses a separately written scalar evaluator that imports none of the author
or predecessor evaluator code. It is an internal separate-author review,
not external peer review, a Lean certificate, or an F/E attestation.

## Findings

1. The coupled W front is valid. At z=76, the only active first-front
   predecessors are the preceding coupled ray and the origin-only lower
   layer. At z=77, they are the preceding upper ray and the coupled z=76
   layer. At j=0 the W-only predecessor contributes zero by shortest-path
   parity. The reviewer evaluates that spatial first-front recursion
   directly through j=176 and obtains all 708 two-layer entries reported
   by the corresponding recurrence. No isolated-pulse superposition is used.

2. The giant-delay reduction is justified in the stated family. The forcing
   of F0 has period 384. A forcing block is a permutation of eight triples,
   so 384*840 is a sufficient F0 period. Over this period F1 is driven
   periodically, and its block also permutes eight triples. Thus
   384*840^2 suffices for the joint state. P divides by this period exactly.
   The separately inherited upper-strip bound 12*840^18 also divides P;
   the argument applies to the complete Q/C/G/J cluster, not to four
   independent pulses. The review reimplements its scalar recurrence.

3. The actual late boundary is retained. Thirty-two scalar masked-route
   diamonds reproduce q9 and all its six incoming triples and old-local
   values. All sixteen q8 input/mask cases satisfy the report's displayed
   incoming formulas and nonzero old-local term. Earlier qY,q7,q8 endpoints
   remain intact throughout the independent calculation.

4. The full common-code census agrees. The scalar evaluator reproduces all
   128 entries in the two native/intervention tables. The native common
   pairs are (0,3),(1,2),(2,1),(3,0),(4,6),(5,7),(6,4),(7,5), using code
   4A+2B+D. No common injective code exists for the arbitrary q8.B
   intervention with its past retained. In particular neither clean-A nor
   clean-B targets, nor the stated standalone mixer target, supplies the
   required common family. The positive route J=(u XOR a,a,u XOR a)
   gives q9=(0,y XOR a,y XOR a) in every tested native x,u,mask,a case.

5. Initial placement and resource accounting are scoped correctly. W and J
   lie on q9's original-time current boundary; the depth-nine balls contain
   the preceding depth-eight balls. J cannot reach q8 before R+10. The
   inherited unknown previous field at the origin is outside the new
   previous ball. J overwrites no inherited source: its position is beyond
   the known upper sources and is an explicit new boundary exception.
   The report's inherited-source and frontier checks are consistent with
   these distances. The map from (u,a) to J has rank two, and for fixed u
   it retains one independent a dimension; it contains neither x nor y.
   This accounting does not derive a's conditional freshness physically.

The review confirms the scoped route, not a calibrated reset. There is one
masked sign, no simultaneous outgoing y register, no 5:3:2 selector, no fair-z
output, and no native new herald/failure instrument. The report correctly
leaves whole-history freshness and complete future-boundary closure separate.
Its explicit distinction between the q8-creating boundary and the future
neighborhood is necessary and is retained.

## Replay and additional deduction

From this review directory in the published tree:

```sh
python3 checks.py > /tmp/oi-masked-review.json
cmp /tmp/oi-masked-review.json result.json
python3 -O checks.py > /tmp/oi-masked-review-O.json
cmp /tmp/oi-masked-review-O.json result.json
```

The two runs are byte-identical. The checker reads the sibling author's
structured result for comparison and verifies its pinned input hashes; its
physical scalar computation imports no author code.

`COROLLARY.md` and `history_corollary.py` are a **new review-side deduction**,
separate from the reviewed author claim. They apply the seven-port history
proof through R+9 and state the resulting conditional fair-bit refinement
under explicit original-time independence of a. They are not represented as
content proved by the author checkpoint or as independently reviewed by their
own author. Root integration must assess that additional deduction separately.
