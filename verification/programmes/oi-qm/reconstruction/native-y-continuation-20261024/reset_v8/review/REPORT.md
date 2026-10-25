# Separate-author review of the workspace-assisted native-Y route

Reviewed author revision: `e46d30fdd2c237b70ee7569f0044f2486f07f8ce`,
`reset_v8/` on draft #910. Verdict: **accept within the stated bounded scope;
no blocking findings**. This is a separate-agent internal review, not external
peer review, a Lean certificate, a native-round designation or owner adoption.
The reviewer did not author the candidate or its checker.

## Findings

The candidate's native-family witness is correct: initial W=111 and G=011
for u=0 / G=101 for u=1 give the full q8 triple `(0,y,0)` at R+8, preserving
the earlier q7 `(0,0,y)`. All 32 common ordered code pairs are reproduced.
The arbitrary q7.D intervention has no common injective two-code solution
in the enumerated family. For the clean witness, u=0 and intervened p=0
produce 000 at x=0 and 001 at x=1. This verifies the report's distinction
between routing the correlated native input and supplying a reusable socket.

The ray proof uses an actual interaction of W with the origin wave. It is
not a superposition of independently evolved pulses: four scalar first
collision cases explicitly reject that surrogate. Before the first origin/W
collision both arrive along unique axial paths. At subsequent points of the
ray, the -y predecessor contains their coupled value, while the -z predecessor
contains the origin-only multinomial parity. The other predecessors and old
local term have not yet been reached. This yields the stated forced recurrence.

The forcing is 384-periodic because its parity mask depends on seven bits
and H has order dividing 12. Its finite-state block is bijective; 840 is a
valid uniform exponent. Actual P is divisible by 384*840, so the reduction
to j=176 is exact. The independent control in fact finds identity monodromy
for both x values, but the larger bound used by the author remains valid.
The unique initial entry point at R-1 and absence of an entry at R-2 also
check at the actual giant coordinates. No reduced-scale extrapolation is used.

## Independent computation and its dependencies

`checks.py` never imports the new author's `reset_v8/probe.py`. It starts
from the retained and previously reviewed sibling `reset_v7/probe.py` to
obtain the Q/C/G baseline. It then evolves an independently implemented scalar
perturbation along the unique nine-edge first-arrival W path. At every step
it computes `H(baseline_neighbor_xor XOR delta) XOR H(baseline_neighbor_xor)`.
The old local value is unaffected at a first-arrival point. This organization
is different from the author's packed full-diamond evolution.

This check reproduces all 6,144 diagnostic assignments, all 1,536 retained
mask-reduced table rows, their selector-mask independence, both encoding
censuses, the clean witness and the late-input counterexample. Eight selected
full scalar diamonds independently agree with the one-path calculation.
These selected diamond checks reuse the inherited upper-strip initial values;
the review does not independently reprove every prior upper-strip theorem.
It explicitly inherits that earlier reviewed dependency.

The reviewed six author files were fetched at the immutable revision above
and their Git blob IDs matched the local reviewed bytes. `INPUT-HASHES.json`
retains that correspondence. The author checksum file verifies, and its
normal/optimized replay was independently confirmed. Reviewer normal and
optimized runs are byte-identical to `result.json`; the recorded input hashes
pin the exact author probe/result and inherited evaluator inputs.

## Scope and remaining obligations

The report correctly leaves the post-Y 5:3:2 sampler, fresh fair z, herald and
failure behavior, complete outgoing carrier, and joint public-record law open.
W preserves the designated earlier reads but can affect later old-port
backgrounds. Thus old designated-value preservation does not establish the
extended masking/resource-independence theorem. No access restriction,
initial readiness, physical premise or calibration has been derived here.
The one-source obstruction remains valid for its earlier family; the present
positive result adds a genuine second source and earlier interaction.

The clean route is useful input to the next bounded reset construction.
Neither this computation nor its review claims reusable native reset, A1
coverage, A2 full-protocol agreement, composite reconstruction or OI–QM
equivalence.

## Replay

From `reset_v8/review/` in the retained tree:

```sh
python3 checks.py > /tmp/oi-v8-review.json
cmp /tmp/oi-v8-review.json result.json
python3 -O checks.py > /tmp/oi-v8-review-O.json
cmp /tmp/oi-v8-review-O.json result.json
sha256sum -c SHA256SUMS
```

The checker requires only the standard library and the sibling retained
`reset_v7/` evaluators. Controls raise before a pass verdict on failure.
