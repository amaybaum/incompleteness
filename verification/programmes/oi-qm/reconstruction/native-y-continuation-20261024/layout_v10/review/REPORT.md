# Separate-author review of the alternative remote fanout

**Verdict: accept within the stated fourteen-endpoint family; no blocking findings.**

Reviewed author revision: `8dc85bce24569a2ee80e8150d2aa7e05ac24f540`,
`layout_v10/` on #910. The reviewer did not author the candidate or checker.
This is internal separate-agent review, not owner adoption, external
validation, a Lean theorem or a general reset impossibility.

## Provenance and replay

The five author files were fetched at the immutable revision and their Git
blob identities matched the local review inputs. The source geometry is the
retained 1,479-entry census; its pinned SHA-256 is
`2642e1a68825faa5d3bb1049e8722adec1ec33bd3f56b9e4416b2c902a85ec5d`.
The author manifest verifies. Normal and optimized author runs reproduce
results.json byte for byte. INPUT-HASHES.json records the reviewed inputs.

The new reviewer checker imports no author evaluator. It encodes triples as
integers, computes the coupled strip by memoized scalar spatial recursion,
and uses exact binomial coefficients for shortest-path parity instead of
the author's binary no-carry implementation. The published result is read
only as a pinned comparison expectation, not as the physical evaluator.

## Geometry and period argument

All 20,706 inherited-source/endpoint comparisons and all 98 complete frontier
family exclusions pass independently. Each ray's exact nearest point on its
finite index interval is checked, so this is not finite sampling of a large
ray. Origin and W meet every endpoint on their first fronts; other named
selector/upper sources are excluded. Negative-x payload sources preserve
old informative deadlines, do not reach q8 before its read, and cannot
coincide with old bank coordinates. Their pairwise endpoint exclusions
justify independent response maps for simultaneous outputs through L.

The positive-x source has distance S-401 to the old selector-Z port for every
endpoint in the family. It therefore cannot be accepted as a harmless new
boundary source under the existing ready/informative-record contract. The
report rejects it rather than counting its isolated collision law as a
native construction.

The 11-by-16 strip has 176 triple coordinates. At each j step, a coordinate
depends on its own preceding value and already-updated lower r/k coordinates.
The lower-coordinate dependence is triangular; H and XOR translations make
each diagonal action bijective. The boundary forcing is 384-periodic.
A 384-step block retains this triangular permutation form. Inducting over
the coordinates, restoring lower coordinates leaves a permutation of eight
values on the next coordinate; 840 is a sufficient common exponent for
that permutation. Thus 840^176 bounds the block order, and
384*840^176 is a valid sufficient sequence period. Exact integer arithmetic
confirms divisibility by actual P. This proof retains all coupled origin/W
terms; it does not superpose isolated waves or infer giant-scale behavior
from a reduced P.

## Coupled seed response and cycle result

The negative-x payload first meets the input front at x=0, not at the final
receiver x=10. Its single first-arrival path gives eleven coupled updates.
At each update the two off-axis input/W terms cannot yet depend on that
payload. The reviewer reconstructs all sixteen payload/input outputs for
all fourteen endpoints: 224 scalar entries agree with the author.
Both payload maps are permutations at every endpoint. Their relative
permutation has cube equal to identity. At delta13,17,21 its cycle type is
3+3+1+1; at the other eleven it is the identity. The reported uncontrolled
input pairs also agree.

A separate six-neighbor, two-slice scalar recurrence checks 64 bounded cases
with both x values, both zero/nonzero W choices, all eight payloads, and two
old-origin triples. All match the coupled formula and have blank receiver
prefixes. Sixteen cases disagree with a false final-tick collision shortcut,
so the control detects the omitted interaction. The two-cycle search accepts
the four genuine XOR-translation pairs as a positive control.

## Full-law deduction and its exact scope

The stronger proof is valid under its explicit four-history condition:
accepted payload laws nu_0,nu_1 depend on apparatus seeds and old u, but not
on unknown x, and the full raw accepted output law must be common at fixed
y=x XOR u. Correlations between endpoint payloads are allowed. A seed-only
herald can be absorbed into these laws, including unnormalized accepted
measures if success weights are part of the contract.

Cross-exclusion makes the simultaneous response a product of the endpoint
permutations. Its relative permutation T satisfies T^3=id. The four-history
equalities imply nu_0=T nu_1 and nu_1=T nu_0, hence T^2 nu_0=nu_0. Since
T=(T^2)^2, nu_0 is also T-invariant; the two desired output measures are
identical. This uses no independence among payloads and survives adding an
independent untouched Z factor. It excludes two distinguishable full raw
output laws in this family under that contract.

It does not exclude an input-coupled herald, a different endpoint/controller,
or a different coarse-grained or pooled-history acceptance criterion. A
postselection rule that discards one u history is not a repair satisfying
the four-history common-law equations with nonzero signal. These qualifications
are consistent with the report's stated equations and scope. No target or
acceptance rule is changed here.

The endpoints are outside q8's one-tick light cone. They consequently cannot
respond to an isolated late-q8 operand intervention. The report presents
this as an alternative native-family recomputation, never as a reusable
q8 socket. No new readiness, seed law, full carrier, herald, calibrated
reset or broader equivalence is adopted.

## Replay

From `layout_v10/review/` in the retained tree:

```sh
python3 checks.py > replay.json
python3 -O checks.py > replay-O.json
cmp results.json replay.json
cmp results.json replay-O.json
sha256sum -c SHA256SUMS
```

The reviewer normal and optimized runs are byte-identical with verdict PASS.
The script needs only Python's standard library, the pinned source geometry,
and the pinned author result. `--source-root PATH` can name their containing
checkpoint in a sparse copy. The previous full native suite is not rerun.
#885, frozen records, premises and interface criteria are unchanged.
