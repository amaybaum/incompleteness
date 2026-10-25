# Separate review of the affine local phase-code controller

**Verdict: accept the native affine witness within its stated scope, with
no blocking findings.**

Reviewed author commit:
`bf1bc9fb067e38417d8968e26a691debf7d3eb5f`, subtree
`branch_v10/local-controller/`. All eight published file blobs were fetched
at that immutable SHA and match the local bytes used here.
`INPUT-HASHES.json` retains their SHA-256 hashes.

This reviewer did not author the local-controller report or evaluator.
`checks.py` independently implements integer-coded scalar native recursion,
the signed upper strip, the coupled W lower front and the complete late
collision diamond. It imports no author or predecessor evaluator. Its reuse
of the native rule and actual coordinate formulas is explicit. This is
internal separate-author review, not external peer review or a kernel proof.

## Independently reproduced result

For C=100, Vplus=101, Vminus=111, the original-time controls are

    J=(u XOR b,a,u XOR a),
    Kplus=(a XOR b,0,a XOR b),
    Kminus=(a XOR b,a XOR b,a XOR b).

All 64 x,u,mY,mR,a,b assignments were evolved independently. In all 48 rows
with (a,b)=00,10,11, previous q8 at R+8 is (0,y,0), and current q9 at R+9 is
(0,y XOR a,y XOR b), with y=x XOR u. The complete triples agree with the
author's retained output table. The earlier qY and q7 endpoints also survive
inside the scalar calculation.

The rejected pattern01 has the independently reproduced raw triple
(u,y,x(1 XOR u)). Across (x,u)=00,01,10,11 these are 000,110,011,100,
respectively, for every selector mask. All sixteen such rows are retained.
They are not replaced by a chosen quantum failure state.

Swapping the K payloads gives the second witness: reflection in the signed
x coordinate exchanges Kplus/Kminus and the old mY/mR control labels, while
leaving the axial q8/q9 output sites fixed. The first witness was checked
for every mY,mR assignment, so this symmetry establishes the swapped case
within the same actual causal diamond. The independent scalar evolution is
reported for the primary witness, not falsely counted twice.

The review also recalculates the decision rule on all 512 candidates in the
published 32,768-row table. Exactly (4,5,7) and (4,7,5) pass the accepted-mask
test. This independently checks exhaustive verdict extraction; it is not a
second native evolution of every rejected candidate. The primary existence
claim rests on the separately evolved witness above.

## Dynamics, periods and initial geometry

The signed upper evaluator is required: Kplus and Kminus break the prior
x-reflection reduction. The reviewed construction correctly retains signed x
and only the surviving y reflection. Its initial Q,C,G,J,Kplus,Kminus fields
are evolved together; no independent-pulse superposition is used.

The review compares 9,240 scalar entries with direct native recursion across
the actual eight u,a,b configurations. The strip budget remains 18. In the
triangular recurrence, other transverse sites enter at lower lag; each
same-lag site's axial evolution is an eight-state permutation driven by
those lower lags. The product of parallel same-lag permutations still has
exponent dividing 840. Hence the inherited sufficient period 12*840^18
applies without x reflection, and divides actual P exactly. The lower W
entry is computed separately by first-front spatial recursion, including
the interaction of W with the physical origin input. The final diamond
keeps all six neighbors and the old local term.

All three added/controller source positions are at distance R+9 from q9
and R+10 from q8. The reviewer checks their exclusion from all seventeen
earlier ready balls, their distinction from all 1,479 inherited source
positions, and separation from the four lower controls and W by at least
2R. This gives 51 ready-ball and 4,437 source-position comparisons. They are
current-boundary exceptions in the original-time depth-nine preparation;
no late-time pin or unknown-input copy is introduced.

A Boolean-coefficient check verifies that every initial source component
has degree at most one in u,a,b. The complete controller encoding has rank
three in those variables; it retains two fresh dimensions conditional on
the old seed u. Unknown x does not occur in the source-definition arguments.
This verifies the absence of a nonlinear initial seed prior. It does not
physically derive the stipulated independent a,b resource.

## Countercontrols and six-seed assembly check

Replacing only q8.B by a forced p while retaining the actual past gives
exactly 24 mismatches among the 48 accepted-mask rows for each p=0 and p=1.
The reviewer reproduces both counts. This is a concrete obstruction to
using q8 alone as an arbitrary late-input socket; it is compatible with the
positive correlated native-family result.

As a limited finite assembly check, combine the scalar local output with the
specified predicate K<n(a,b), n00=5,n01=0,n10=3,n11=2, and independent z.
For each fixed x,u, enumeration of all 64 a,b,K,z assignments gives twenty
accepted and forty-four failed cases. Decoding only the named phase cells
as (current q9.B, previous q8.B, current q9.D, z) gives the exact 5:3:2 plane
weights with z jointly fair. This is pointwise in old x,u, so it does not
assume that a previously used u remains uniform after earlier observations.

That finite assembly check does not independently certify the remote compiler
geometry or the complete public-history theorem. The reviewer authored the
remote herald proposal; its separate independent review and the root's joint
integration assessment must carry those claims. They are not folded into this
local review under a misleading independence label.

## Scope retained

The three signs occupy a **two-slice phase encoding**. Y is in previous q8;
X and R share the same whole current q9 port. This does not give three
independent current public ports or a native rule permitting selective reads
of those components. The previous-slice access question, whole-port metadata,
additional readout/reset back-action and arbitrary next-stage closure remain
open. No new observer access is adopted by interpreting the phase coordinates.

The accepted witness is an actual native processing result under the stated
initial preparation. It does not establish a complete reusable quantum
instrument or full OI–QM equivalence.

## Replay

From the retained review directory:

```sh
python3 checks.py > /tmp/oi-controller-review.json
cmp /tmp/oi-controller-review.json result.json
python3 -O checks.py > /tmp/oi-controller-review-O.json
cmp /tmp/oi-controller-review-O.json result.json
```

Normal and optimized outputs are byte-identical. The checker reads the
hash-pinned author files and retained source geometry but imports none of
their evaluation code. `SHA256SUMS` covers this review's source and result.
