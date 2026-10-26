# States and dynamics: current research handoff

This directory holds separate exact-architecture and finite-approximation
research paths. Its results are internally reviewed research. None of them
establishes native availability, probability selection, premise or access
adoption, or full OI-to-QM equivalence.

## Executed finite-menu approximation

`a2_efficiency_v6/`, author
`bff7b58d951babd4064b60699281ee0a7f3e9f45`, has an accepting separate-engine
internal review retained at `15b316122d5e2907d33282bc1895ff4fbf72efab`.
Its actual six-face M=16 grid has 1536 labels, W=16 integer weights and
B=24 initially fair CDF bits per reserved source block. It uses the same
positive decoder D=(mass I+(3/2)E[R_word ell] dot sigma)/2 at input and output.

The preparation menu is both signs of X,Y,Z,a=(3/5,4/5,0) and
p/q=(2/3,-2/3,+/-1/3), plus positive mixtures. Read axes are X,Y,Z,a;
rotation generators are H,S and the rational Z rotation with first row
(3/5,-4/5,0), and its inverse. All policies have one total budget h=3,
including rotations, reads and absorbing stops; a reset never restarts it.

All 1020 ray/word positivity and 1008 ray/word/read cases are evaluated
exactly. The resulting envelopes are

    kappa=6419131/419430400,
    chi<=266098754553528263/18446744073709551616,
    CQ error<=3*kappa+2chi
      <=17239332625914280559/230584300921369395200 <0.074764.

The uniform guarantee covers every adaptive policy within that menu/horizon,
including complete public records and decoded outgoing states, begun at the
fixed decoded input. Exact finite envelopes, fresh-reset induction and
quantum trace-distance contraction supply the proof. Independently evaluated
protocol trees and seed/access mutants are controls, not an enumeration of
all adaptive policies. M=8 fails the prescribed 0.1 target; M=16 passes, so
M=32/64 were not executed. No unexecuted grid supports this certificate.

Resources include 96 initially fair bits excluding mixtures, at most 130560
word-tagged carrier labels (17 bits), a 2-bit clock, CDF tables up to 460800
bits, optional response tables up to 522240 bits and up to 3 retained old
carrier registers. Blank workspace, table descriptions and non-dyadic
mixture sources are additional. This is not a 96-bit total-device claim.

The prior `finite-a2-v5/` all-menu geometric theorem and its conservative
billion-label example remain unchanged. The new certificate gains from a
narrower exhaustive menu/horizon envelope and its verified positive 3/2
decoder. It is not an improved universal convergence theorem. Enlarged menus
or horizons need recertification. Geometric priors, reset, private access,
clock and reversible gate scheduling remain supplied rather than native.

## Depth extension of the finite controller

`a2_depth_v7/`, author head `2668343631ba7e80bc3588219578b1b7362fddb7`, has
separate-engine internal reviews retained under `a2_depth_v7/review/`: two
blocking rounds and a third, accepting round. Its `REPORT.md` was later edited
at `dc210283` and `49e1a119` to restate the lower bound for the executed
extension in three lines. The checker and every number are unchanged; no
retained review round covers that restatement. On the in-menu protocol "prepare
X+, then read a, X, a, X, ...", the executed M=16, W=16, B=24 controller,
extended by one fresh 24-bit block per slot, has complete-record TV from the
quantum protocol tending to 1 with depth (certified TV>1/2 for h>=67382091).

The same holds for every controller in the memoryless reset class, for every
fixed B. In that class the post-reset carrier depends only on that slot's
fresh block of at most B fair bits and the public record, responses depend
only on carrier, public word and setting, and the preparation read is
unconstrained. A retained-seed reset lies outside the class and escapes the
obstruction on this protocol, with TV<=1/(2^B-2) at every depth for B>=2; it
is a protocol-specific sampler, not a geometric controller.

`a2_memory_v8/`, whose checker was last changed at
`5beb12b78747c2c752b6abca2cb94ac491d06441` and whose `result.json` at
`03a31cf9029582162bc82508a4eacf28e098701f`, has internal reviews retained
under `a2_memory_v8/review/`; the last retained round reviews
`70faede0..3ca0d8ba`, which contains package commits `03a31cf9` and
`12863de8`. It proves that every
controller whose whole persistent state is finite, with a time-independent
update and B fair fresh bits per slot, also has T(h)->1 on this protocol, for
any initial law. The obstruction is arithmetic: dyadic fresh randomness
against a run law with ratio 4/5. It holds for resets that carry no private
randomness across slots, whatever their record dependence (`a2_depth_v7/`),
and for every controller with finite whole state (`a2_memory_v8/`). The
retained-seed reset, granted the target cuts, escapes it with linearly
growing private memory. Restarted every k reads (B=2,3,4, k<=16), that reset
is certified to have T>1/2 beyond a finite depth for every tested member.
Arbitrary depth remains open for bounded private memory with unbounded public
state (an unbounded clock or full-record dependence), for time-dependent
updates, for growing per-slot blocks, and for the least memory growth that
keeps T bounded. The class result does not cover non-dyadic fresh sources.
For a fair five-valued source the arithmetic argument fails (lambda = 4), and
a memoryless sampler that agrees on four of five values gives T = 0 (computed
exactly through h = 12). The h=3 certificate above is unchanged.

## Exact reset-resource audit

`a1_reset_v6/`, author `41992cc0b7f8901195f70ff47b34f1a0ed5eba5e`, has
an accepting separate-engine internal review retained at
`bdd897852d3f44089a5476205a949c8ecc54f981`. The credited Montina two-vector
model has a correct two-time quantum transition. Iterating the tested fixed
vectors and bit update from Z+ gives X then Z record masses 1/3,1/6,1/3,1/6,
where the quantum masses are all 1/4. Final Z+ is 2/3 instead of 1/2 and
record TV is 1/6. Longer alternating reads have only four possible paths.

The exact witness uses six equal-measure coordinate-square difference
patterns and independent reflection signs. The source symmetry/density
proof is distinct from its 96-cell exact checker. Separate reference-basis
and rational-vector engines confirm the result. The author and separate reviewer read the
primary sources and preserve Montina's original two-consecutive-measurement
scope; no missing extra forcing is silently discarded in the literal maps.
This is a fixed-vector repeated-use failure, not a general hidden-variable
or OI no-go and not a refutation of the original scoped theorem.

The declared bit map is two-to-one even with its record; an explicit total
reversible lift retains one garbage bit per invocation. That repairs
invertibility without repairing the reused conditional source law. Supplied
independent pair renewal restores the full finite-adaptive record/state law,
using 2(h+1) initially provisioned sphere points for this particular repair.
It is sufficient, not minimal or native. Continuous preparation/reset,
private retained vectors, access and timing remain explicit resources.

## Retained architecture and native bridge

The credited `history-architecture-v5/` KS sphere comparison covers all
single-qubit states, rotations and finite adaptive rank-one projective
records/outgoing states under its supplied continuum/reset/access contract.
Its known reproduction is not a new quantum theory or native source theorem.

`native-code-bridge-v6/` exactly matches the calibrated post-X/Y target
measures to sign projections of that sphere model. Its sharp 1/10 pair error
for a broader rational read assumes an autonomous common twelve-code input
with the same independent continuation. The actual native full phase,
history/clock tags and response memory are outside that exclusion. Selected
signs alone do not establish universal native operation coverage.

Native construction is in `../native-y-continuation-20261024/` (#910).
Complete-record composition is developed on #912 and wider gates are tracked
in Issue #913; their results are not established here. Calibration selection,
initialization, general instruments, arbitrary depth, composites/Bell and
full A1/A2 coverage remain open.

## Packages and replay

The top-level `REPORT.md`, `PROBE-SPEC.md`, `checks.py` and `result.json`,
with their independent review in `review/`, are the exactness and sourcing
audit. The packages are `stopping-source-v2/`, `operational-quotient-v3/`
(with `product-section-v4/`), `history-architecture-v5/`, `finite-a2-v5/`,
`native-code-bridge-v6/`, `a1_reset_v6/`, `a2_efficiency_v6/`,
`a2_depth_v7/` and `a2_memory_v8/`. Each holds its checker, its structured
output, a `SHA256SUMS` manifest and its retained review. Each `REPORT.md`,
or its review, gives the package's replay recipe. Every checker reproduces its retained
`result.json` byte for byte under `python3 -I -B`, normally and with `-O`.
The full mutant campaigns are recorded in their packages and are not part of
that replay.

The top-level `REPORT.md`, `stopping-source-v2/REPORT.md`, `review/REVIEW.md`
and the `PROVENANCE.json` of `operational-quotient-v3/` and
`history-architecture-v5/` cite programme snapshot `2d555f17` on branch
`research/missing-component-20261020` as provenance. The claims there rest on their own checkers and, where they cite
Lean, on declarations at `de6fe293`, which is on `main`.
