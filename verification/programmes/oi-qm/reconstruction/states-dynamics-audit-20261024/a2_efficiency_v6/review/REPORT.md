# Separate-engine review of the executed finite-menu A2 certificate

**Accept within its stated finite-menu, three-operation scope; no blocking
findings.** Reviewed author: `bff7b58d951babd4064b60699281ee0a7f3e9f45`
on #911, under `a2_efficiency_v6/`. This is separate-agent internal review,
not formal certification, external validation, native availability or
adoption of the supplied preparation, reset, access or clock assumptions.

All six curated author files were fetched at that immutable revision.
Their Git blob identities and SHA-256 hashes match the local inspected
bytes. `INPUT-HASHES.json` retains those pins. The author manifest verifies;
author normal and optimized executions both reproduce its retained result.
The review imports no author engine.

## Independent finite envelopes

The new engine constructs all six faces directly, computes each rational
geometric weight before flooring, partitions the complete initial seed
interval by integer CDF cuts, and sums rational inward vectors point by
point. Opposite preparations use the stipulated pointwise antipodal sampler.
The source ordering is part of this concrete CDF construction. It is not
replaced by an order-independent quadrature approximation.

Every weight satisfies the floor enclosure, every count is nonnegative,
and counts sum to `2^24` for every ray. Actual rounding is nonzero in all
six canonical positive-ray laws at both executed grid sizes. The exact TV
distance between normalized integer weights and CDF counts obeys the stated
rounding bound. The independently regenerated complete CDF-vector digests
agree with both author grids.

The reviewer derives the real generators from rational-complex 2x2 quantum
unitaries, then evaluates direct quantum matrix evolution for every formal
word and canonical preparation. For each M=8 and M=16 grid this supplies:

- 1,020 ray/word positivity and norm-preservation checks;
- 1,020 direct quantum word controls;
- 1,008 ray/word/read cases, covering all twelve preparations, all words
  of length at most two and all four read axes;
- 324 distinct cached direction/probability cases.

The fixed decoder `alpha=3/2` is positive on every declared ray. Its
maximum squared Bloch norm at M=16 is independently reproduced as

    47716765703861269321503281838235309 /
    50432868877265397685582603223040000 < 1.

Norms and trace distances use rational intervals whose squared endpoints
are checked. No floating-point tolerance certifies positivity or error.
The exact M=16 envelope is

    chi <= 266098754553528263 / 18446744073709551616,
    kappa = 6419131 / 419430400.

The chi witness is Z+. The kappa witness is preparation X+, word r,
read a: source plus probability `6296563/16777216`, associated ideal
probability `9/25`. The independent maxima agree exactly with the author.
Consequently the fixed-input/output-decoder bound is

    3*kappa + 2*chi
      <= 17239332625914280559 / 230584300921369395200
      < 1/10.

M=8 instead has upper bound
`82558218940928118293/461168601842738790400 > 1/10`. The executed ascending
search therefore stops at M=16 as preregistered. No M=32/M=64 result or
unexecuted large alphabet is used to support this certificate.

## Why this covers all policies in the specified menu

The written proof has the right quantifiers and the right input comparison.
An initial positive mixture gives a convex combination of rotated canonical
rays. Before its first measurement, the exhaustive probability envelope
therefore bounds the next outcome error by kappa. After each measurement,
an independently reserved reset block establishes a canonical eigenstate
law conditional on the entire public record. Rotations and absorbing stops
preserve the declared cone and total remaining clock budget.

A coupling of the public binary conditional kernels bounds complete-record
TV by at most `h*kappa`. This does not require an ontic coupling to remain
independent after conditioning on matching histories. For each complete
history, the last fresh reset and remaining exact rotation word give a
decoded state within chi of the associated ideal outgoing state. Histories
with no read retain the initial-mixture estimate. Summing subnormalized
branch operators gives `h*kappa+chi`, including zero-mass branches.

Finally the associated ideal initial mixture differs from the single fixed
decoded input by at most chi. The adaptive quantum experiment, including
its complete classical record and outgoing quantum state, is trace
preserving. Trace-distance contraction supplies the additional chi. The
result is correctly `h*kappa+2chi` for the claimed fixed decoded input,
rather than silently comparing against its pure preparation label.

The same decoder is used before and after every completed operation.
Positivity follows on the full positive-mixture cone by linearity and
convexity. The apparatus does not read an unknown decomposition label.
The fixed menu and total h=3 horizon are essential: arbitrary generators,
additional read/preparation directions or deeper protocols require another
envelope. This result does not supersede the broader all-menu theorem or
give a universal convergence-rate improvement.

## Independent records and nonvacuous controls

The review evaluates nine policies on sixteen pure/mixed inputs: 144
protocol/input cases, 1,472 nodes and 800 complete leaf records. The policies
include adaptive reads and rotations, repeated projective measurements,
unitary-only paths and absorbing stops. All public tick slots, settings,
outcomes and success flags remain in the record. There are 590 nodes where
at least one of the source or quantum branch masses is zero; none is
discarded. Direct subnormalized 2x2 comparisons satisfy the envelope bound.
These trees are independent bounded controls, not an enumeration of all
adaptive policies and not the proof of the all-policy statement above.

Three separate small samplers exhaust 3,072 fair seeds. Linear CDF scans
agree with an independent binary sampler; pointwise antipodal sampling and
all count histograms agree. Actual countercontrols reproduce:

- reset-seed reuse: TV `11/256`;
- ignored adaptive setting: TV `153/1024`;
- insufficient bank: terminal failure mass `1/2`;
- extra private label access between equal-decoder antipodal X/Z mixtures:
  TV `6908569/16777216`;
- a private-label-dependent timing bit: gap `6908567/16777216`.

An additional seed-disclosure control finds 768 nonzero Z+ seed atoms
whose individual fixed-decoder Bloch norm exceeds one. This agrees with
the report's cone qualification: positivity holds for the admissible
completed-operation laws, not arbitrary conditioning on private seeds.
These are changed-contract witnesses; they are not asserted to exceed the
main controller's error allowance or to be native observer operations.

## Resource and physical scope audit

The executed alphabet has 1,536 geometric labels. The 85 formal words
through length three give a conservative 130,560 word/label combinations,
which fit in 17 bits. The public clock has four sectors and needs two bits.
One preparation block and three reserved reset-slot blocks require 96
initial fair bits. Mixture/controller randomness is additional, with
non-dyadic priors explicitly outside this fair-bit count.

The deterministic CDF-table bound is 460,800 bits, and the optional
hemisphere-response-table bound is 522,240 bits. At most three old carrier
registers are retained. The old registers, seeds, blank workspace and
table descriptions remain real resources; 96 bits is not a total device
memory estimate. The envelope verifier's quantum comparisons are not
tables of protocol answers used by the source controller.

Finite tables admit a supplied padded finite reversible schedule. Neither
the Python evaluator nor this review implements that schedule in the native
H lattice. Native preparation, cosine-law selection, fresh-reset sourcing,
clock availability, workspace isolation, general instruments, composition
and full OI equivalence remain open. Matching this finite operational target
does not establish an empirical prediction selected by OI.

## Replay

Run `python3 checks.py` and `python3 -O checks.py` from the review directory.
Both reproduce `result.json` byte for byte. `--author-root` supports a
sparse layout. Python compilation and the author manifest pass. The five
curated review files are REPORT.md, checks.py, result.json,
INPUT-HASHES.json and SHA256SUMS. No Git mutation, #885 edit, dispatch,
designation, merge or full-suite/Lean attestation is part of this review.
