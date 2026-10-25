# Independent review: exact six-source endpoint

24 October 2026. Review of the local exact files supplied for published checkpoint
`8daae9f6c57d30dec13e140155114aa9298097e2` on PR #910. This review binds the
SHA256 hashes in `INPUT-HASHES.json`; it did not retrieve or modify the remote
repository. Author files were read only. No new premise or encoding was adopted.

**Verdict: ACCEPT, within the stated endpoint/preparation scope.** The independent
actual-scale calculation reproduces all 192 retained lower-slice triples across
64 assignments, all 256 diagnostic endpoint triples and their Boolean
polynomials, all 128 native cases, and the inherited qY, history-sidecar and
complete q2 controls. Opposite native Y values have overlapping endpoint
supports at fixed X. This prevents a deterministic decoder using only X and
this terminal triple. It does not establish a full-history obstruction, a
general impossibility, or failure of another preparation or instrument.

## 1. Independent mathematical audit

The v4 review already accepted the conditional initial active-sector preparation
and its six retained current sources, with zero active previous sector. That
geometry is inherited here, including its local no-wrap qualification on the
odd-sized torus. Preserving M2 is essential: the calculation must retain the
origin/M2 interaction from tick 1, even though M2's isolated shortest-path
coefficient at the final site cancels.

For the dipole alone, write
`W_n(ell,a,b)=U_(n+ell)(a,n,b)`. Both initial sources have axial coordinate at
most zero. Outside `ell >= |a|+|b|` or on the wrong parity the field is zero.
The native second-order rule at axial position `n+1` gives the new coordinate
as an XOR of the already determined new layer `ell-2` and H of the old
coordinate plus lower-layer terms. Its apparently future `W_(n+2)(ell-2)`
term is also determined from lower old layers: each additional axial lookahead
consumes two layers. A transverse displacement changes absolute transverse
weight by at most one while reducing the layer by one. Therefore the budget
`ell+|a|+|b| <= L` is closed.

Ordering coordinates by increasing ell, every diagonal coordinate map is
`z -> a XOR H(z XOR b)`, where a and b depend only on lower old layers. It is
a permutation of eight triples. The base layer is H, whose cycles have lengths
1, 3 and 4. Once all lower layers return after Q steps, each coordinate in the
next layer has undergone an eight-state permutation; multiplying Q by
`lcm(1,...,8)=840` resets every such permutation for every lower state.
Thus the conservative global exponent `12*840^L` is valid. This is a proof
for arbitrary abstract strip states, not an extrapolation of sampled pulse
periods. Finite checks support the recurrence, but do not replace this induction.

The actual pre-S sections independently give:

| Slice | Ball radius about s | Potential dipole sites | Maximum strip weight | Minimum reduced axial coordinate |
|---|---:|---:|---:|---:|
| S-2 | 71 | 71 | 140 | 113 |
| S-1 | 72 | 286 | 142 | 112 |

All are inside budget 144 and forward of the axial origin. Because
`P=12*840^185` is divisible by `12*840^144`, shifting both time and axial
coordinate by P is exact. Reduced native times are 183 and 184.

Every selector is distance 2S from the origin and 2S+2 from M2, so the dipole
does not interact with a selector before S. Although selectors can interact
with each other elsewhere, the relevant pre-S causal cone meets them only
on first-arrival fronts. Their backward cones contain no earlier selector
arrivals, and their fronts share a rotating single-field subspace on which H
is linear. Consequently adding their first-arrival parity contributions here
is justified. The independent checker uses the complete astronomical integer
displacements on all 5,467 relevant boundary contributions, without the
author's ten-bit truncation.

The upper source is distance 2R from the origin and each selector, and 2R+2
from M2. Therefore upper/lower interaction cannot occur before R. Adding its
isolated values only on R-2/R-1 is valid; all subsequent updates must use the
full nonlinear rule, as both implementations do.

## 2. Independent actual-scale computation

`checks.py` is a standard-library implementation with **no imports from author
dynamics code**. Author `lower-slices.json` and `RESULT.json` are comparison
targets only, never inputs to the computed evolution.

- A direct memoized native recursion evaluates the interacting dipole at
  reduced times 183/184 in raw signed coordinates, without the C++ transverse
  reflection/interchange cache quotient. It uses 97,624 cached states.
- Exact giant-integer selector fronts are added. A sparse map then advances
  all 68 native ticks from S through R-1, clipping to the shrinking causal
  balls. The candidate support is the union of old support and neighbors of
  current support; every omitted site has zero old value and zero neighbor
  sum. Peak retained support is only 409 sites. The final 192 triples agree
  with the C++ export in all 64 lower assignments.
- A separately implemented signed-transverse lookahead strip produces the
  upper pulse. It reproduces periods 3600 and 2940, actual residues 253, and
  is checked against direct native evolution at small times. It uses neither
  `period/strip.py` nor `third_step.py`.
- Four complete native updates produce all 256 endpoint triples. The native
  qY triple and earlier sidecar agree. A separate first-front baseline q2
  calculation agrees with the whole q2 triple for all assignments, including
  the positive control `q2.A=p`.
- A Mobius transform reproduces every recorded output ANF. Enumeration of
  native assignments reproduces all four marginal rows, both collision
  witnesses, and equal-prior local error rates 1/16 and 9/32.

The independent signed dipole strip also agrees with 6,336 direct native
values across all 16 x/M2 assignments. This is a second recurrence control;
the actual endpoint comparison above uses the full-size T=185 and actual P.

## 3. C++ and assembly inspection

No discrepancy was found. The reflected cache is legitimate because both
dipole sources lie on the y axis and the rule is symmetric under transverse
reflections and interchange. For these bounded calls the cache key fields do
not overlap: t fits eight bits, shifted n+256 fits nine, and transverse
coordinates fit their allocated fields. The sixteen x/M2 lanes are correctly
replicated into the sixty-four lower lanes.

The selector ten-bit shortcut is justified by `P % 1024 == 0` and transverse
displacements below 1024; the pulse phase uses `P % 3 == 0`. The independent
full-integer calculation bypasses both shortcuts. The initial radii 71/72,
68 shrinking updates, and exported R-2/R-1 balls of radii 3/4 give exactly
the final four-step dependency domain. The in-place previous-slice update
and buffer swap never read a current value being overwritten. The Python
assembly correctly lifts sixty-four lanes to 256 and changes only qY.D at R
for the diagnostic; native cases are selected by `p=x XOR u`.

The author's two checker groups were also replayed normally and under `-O`.
These replays are corroboration, distinct from the independent calculation.

## 4. Meaning and limits

The raw marginal counts agree exactly with the author report. At fixed x=0
the two u rows overlap with total count 4 out of 32; at x=1 the corresponding
count is 18 out of 32. With equally likely u, half these overlaps gives 1/16
and 9/32. These numbers depend on the stated uniform marginal M2/mask prior;
they are not conditional errors given the complete earlier record.

Every fixed-background p pair remains distinct. Accordingly this result is
overlap between background-dependent encodings, not erasure of the diagnostic
operand. The explicit native overlap witnesses nevertheless suffice to rule
out a common decoder based only on X and this endpoint triple. Neither this
pairwise fact nor the marginal table supplies a joint-history law. In
particular, earlier observations may correlate with M2 and selector masks.

Still open: full-history decoding, retained physical auxiliary registers,
later native processing, altered initial controls, compatible extraction,
integrated reusable reset, and the broader inherited transport-proof audit.
No endpoint calculation here closes those questions.

## 5. Reproduction and exact bytes

Place this directory at `six_source_v5/review/` and run:

```
python3 six_source_v5/review/checks.py
python3 -O six_source_v5/review/checks.py
```

The current isolated location also resolves the supplied author checkpoint.
No C++ compiler is needed for the independent checker. The author replay
requires `g++`. Normal and optimized outputs match byte-for-byte for all
three groups. `INPUT-HASHES.json` binds fifteen author/inherited files;
`SHA256SUMS` binds the review artifacts. No duplicate scientific source data
is packaged with this review.

Principal reviewed SHA256 values:

| File | SHA256 |
|---|---|
| REPORT.md | `9fa56cfd67429ea6246398439a0e6114d0f38696c9fdef1c308656f227e8d068` |
| lower.cpp | `07b1a64ecff83462d67559e0d60b6938a2ef0dc742d41bace2b89d4fcf68c0d3` |
| model.py | `1e5130a61b10a857c14149bdeffc0871d888ff224cb78349f33d9dce5674b3bd` |
| lower-slices.json | `86518f9b693af0540e76e61a3ee30ae328881feb3dd3110063508da760070f17` |
| RESULT.json | `bac739e9e3ab1699ac35b89e45556301d434ada56d3300650007066cebc488c0` |
| checks.py | `6ea944a242931c343bb30bfa3bad06bf9e62505784b58fadf264e3acd36093e1` |

These are author file hashes, not hashes of the independently written review
checker or this review report. All additional hashes are in the JSON manifest.
