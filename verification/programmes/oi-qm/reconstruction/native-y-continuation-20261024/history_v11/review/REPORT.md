# Separate-author review of the eight-port history extension

Author checkpoint: `c326546f228a1769856fded2268b76d976a171d3`,
`history_v11/` on #910. **Accept the stated conditional finite-horizon
theorem; no blocking findings.** This is an internal separate-agent review.
It establishes no native reusable instrument or future whole-boundary
independence and is not an external review or formal certificate.

## Exact geometry reconstructed independently

All eight source rays are axial, at own distance t, with intervals
`a_i < t <= H`, H=2L for the maximal declared window. The new herald ray
points outward in +x from 48L; its first reserved triple is strictly beyond
the original radius-L herald source/ready region.

The reviewer checker imports no author code. It uses two closed-form
minimizations instead of the author's breakpoint enumerator:

- For another receiver, `distance(f_i(t),p_j)-t` has the form
  `constant+abs(t-root)-t`. It is monotone nonincreasing, so its exact
  minimum is its value at H. All 64 ordered family/receiver pairs pass.
- For a ready or selected-phase center, the distance has one varying
  absolute-value term. Its exact minimum is obtained by clamping the axial
  root to the integer interval. All 192 ready exclusions and 32 selected
  phase exclusions are strict.

The only equal-time cross-edges are 2->5 and 3->5. Both follow the proposed
same-time ordering. No new edge is introduced by the outward herald ray.
Since no source reaches another receiver before its assigned t, later
source blocks cannot affect earlier output blocks. These results hold
through 2L and consequently on every smaller declared interval.

Distinctness is independently proved using complete coordinate intervals
of the rays: their minimum Manhattan distance is the sum of interval gaps.
All 28 family pairs have strictly positive separation. This covers all
indices, rather than sampled triples or one shared-tick slice.

All 1,479 retained finite source entries are inside the declared enclosing
ready balls; the eight named local source exceptions are also covered.
Exclusion from these balls therefore excludes aliases with those sources.
The enormous remote programs are enclosed by their own included balls and
need not be materialized. The previous ready balls are smaller than the
current balls at the same centers. The stated integer torus lift is valid:
all coordinate spans are below half the side, and own axial lengths are
also below half the side. No wrapped short path changes these distances.

## Whole-history permutation and conditioning

For fixed initial-bank complement C, order the independent bank triples
and their corresponding raw outputs chronologically, with the stated
topological order at equal times. Along each triple's unique axial path,
the other five neighbors and the previous local term are too early to
depend on it. Each step is H composed with XOR translations. Each diagonal
output is therefore a permutation of its own triple, conditional on C
and all earlier bank inputs. Successive inversion gives a bijection of
the complete bank to the complete noise word.

The initial triple law is explicitly supplied as independent uniform
conditional on C and readiness. Thus the full noise word is uniform
independent of C. Its old portion N_L and future portion N_tail are also
independent uniform coordinates, conditional on C. Informative flags and
permitted selected-phase records D are functions of C by the separate
cone exclusions. For each admissible history and nonzero conditioning
event, the future tail remains uniform given C,D,N_L. Averaging over the
posterior of C preserves that law. This is stronger than marginal or
per-port freshness and does not require treating the already observed
N_L as fresh afterward.

No earlier failed offered-carrier branch is restarted. Used old seeds
need not become fair or independent after heralding. The current prepared
selected phase at L is a complement function, but a future carrier or its
neighborhood can depend on the same bank. The author correctly declines
to append an independent noise factor to such a future state without a
new joint-law calculation. Exposing a private bank coordinate or adding
another public port similarly changes the contract.

## Resources and independent native controls

The old seven-stream bank contains

    7L - (2T+4S+R) = 2P+6d+63

triples. Extending the seven streams and adding the eighth gives eight
triples per extra tick. Therefore the complete bit count is exactly

    6P+18d+189+24Delta,   1<=Delta<=L.

All resources are at the original initial time. This is an explicit finite
resource extension, with a supplied independent prior, access convention
and clock. It provides no unlimited privacy for one fixed finite apparatus
or physical derivation of that prior.

The new independent scalar native controls evaluate 256 worlds in two
nonzero backgrounds. They exhaust a same-time old two-port block and two
consecutive future-herald blocks. The two test clusters have disjoint
causal cones and cannot affect each other; their 64-by-64 product therefore
proves the complete 4,096-output four-block map in each background, covering
8,192 assignments by exact factorization. This is a separate scalar engine,
not the author's packed computation. It checks 36 diagonal conditions and
128 unchanged past-prefix assignments.

Pinning or sharing one future source reduces the global four-block support
to 512. Reading a previously private source together with its later output
has support 8 instead of the 64 required by independence. These controls
demonstrate the resource and access hypotheses. A cyclic same-time layout
can also fail joint invertibility despite individually bijective responses,
as the separately retained transport audit shows; the present eight-ray
layout passes the required acyclic check.

## Replay and retained scope

Run `python3 checks.py` and `python3 -O checks.py`, with optional
`--source-root` and `--author-root` arguments for sparse checkouts. Both
outputs equal result.json byte for byte. INPUT-HASHES.json pins the six
author files and retained finite source geometry. All checks use explicit
exceptions; SHA256SUMS covers the five review files.

The all-index finite-window result follows from the exact geometric
minimizations and triangular inversion proof. The short native controls
exercise those mechanisms and are not simulations of the astronomical
window. The inherited informative instrument/calibration law, a new native
reset, access closure, general A1 coverage and A2 error guarantees remain
separate obligations.
