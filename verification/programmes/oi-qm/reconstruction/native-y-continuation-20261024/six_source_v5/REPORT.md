# Exact six-source junction: residual dependence prevents clean Y transfer

24 October 2026. Author-checked research checkpoint; independent review pending.
This evaluates the conditional initial preparation accepted geometrically in
`junction_v4/REPORT.md`, without changing its sources, masks, M2 law or access.

## Result

The prepared endpoint `s=(0,S-1,70)` at `N=R+3` is still not a clean Y
transfer. Its whole raw output depends on M2 and the inherited selector masks.
The output supports for opposite native Y values overlap even at fixed known
X. Thus no deterministic decoder of this triple and X alone recovers Y over
the allowed inputs. The claim is limited to this endpoint and preparation;
history-aware decoding, later processing, and other initial designs remain open.

The exact calculation covers all 128 native assignments and all 256 diagnostic
assignments of `(x,M2.A,M2.B,M2.D,mY,mR,u,p)`. The diagnostic substitutes p for
qY.D at R; native evolution is the subset `p=x XOR u`. The complete table and
Boolean polynomials are in `RESULT.json`. No samples, floating-point arithmetic,
late cleaning, new seed, or discarded failure configuration is used.

## 1. Exact treatment of the astronomical delay

Retain T=185, P=12*840^185, S=T+P, d=68, R=S+d and the six initial sources
specified in v4. The upper reset pulse is separated from the origin and each
selector control by 2R, and from M2 by 2R+2. Therefore it cannot interact with
the lower system before tick R. The origin/selector interactions begin no
earlier than S; M2/selector interactions begin no earlier than S+1.

The lower origin/M2 subsystem must be evolved together: its sources interact
already at tick 1. A sum of isolated-pulse solutions is invalid. The exact
reduction in [period/REPORT.md](period/REPORT.md) handles their interaction.
The closed radial strip map is triangular in layer ell, with each diagonal
map a permutation of eight triples. H has exponent 12 and every permutation
of eight objects has exponent dividing 840, giving the global bound

    F_L^(12*840^L)=identity.

The required pre-S slices lie within strip budget L=144. Their actual maximal
weights are 142 and 140. Since P is divisible by 12*840^144, the origin/M2
values at times S-1 and S-2 and axial coordinate S+j equal their values at
times 184 and 183 and coordinate 185+j. Reduced axial coordinates stay
positive. This is an exact identity for the nonlinear cluster, not an
extrapolation from a small apparatus.

Only 286 and 71 cluster locations on the needed pre-S slices can be nonzero.
Memoized direct native recursion evaluates them simultaneously for all 16
x/M2 assignments, retaining all six neighbors and the previous local term.
The selector fronts are added using their **actual** large-coordinate
multinomial parity. Only low ten bits of the long displacement can overlap
the bounded transverse displacements; P is divisible by 1024. The checker
independently compares this reduction against full Python integers on all
5,467 relevant selector boundary contributions.

Next the unchanged native rule advances the lower data from S through R-1
on shrinking balls. This includes every origin/M2/selector interaction.
`lower.cpp` exports the exact 192 triples required at R-2 and R-1, packing
all 64 lower assignments in bit lanes. It uses only bounded arrays and
integer Boolean operations. The actual lower run has 31,807 memoized cluster
states; it does not enumerate an astronomical strip or evolution.

The separately verified upper-pulse recurrence supplies its exact contributions
on these slices. The upper strip budget is at most six, already covered by
the prior depth-three calculation. Since upper/lower interaction has not yet
occurred, adding the fields on these two slices is valid. Four full native
updates then compute R through R+3. Superposition is not used after R.

## 2. Complete native endpoint law

For each fixed x,u, retain all eight M2 values and four mask assignments with
equal weights. The entries below are counts out of 32, in raw `(A,B,D)` order.
Here y=x XOR u. This is a terminal marginal at the specified initial prior,
not a distribution conditional on the complete earlier public history.

| x | u | y | 000 | 001 | 010 | 011 | 100 | 101 | 110 | 111 |
|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 8 | 10 | 4 | 8 | 0 | 2 | 0 | 0 |
| 0 | 1 | 1 | 0 | 0 | 0 | 2 | 18 | 8 | 4 | 0 |
| 1 | 0 | 1 | 4 | 6 | 6 | 6 | 4 | 4 | 2 | 0 |
| 1 | 1 | 0 | 6 | 2 | 0 | 2 | 6 | 8 | 4 | 4 |

Two explicit native collisions have the same raw output 011:

| x | u | y | M2 | mY | mR | output |
|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 000 | 0 | 0 | 011 |
| 0 | 1 | 1 | 001 | 1 | 0 | 011 |
| 1 | 0 | 1 | 000 | 0 | 0 | 011 |
| 1 | 1 | 0 | 110 | 1 | 0 | 011 |

These exclude every decoder based only on `(known x, terminal triple)`;
they do not exclude using the complete earlier record or a retained physical
M2 register. Nor do they show failure of every possible native instrument.

As a local information benchmark with equally likely u values at fixed x,
the best decoder from this triple and x has error 1/16 at x=0 and 9/32 at
x=1. These follow from half the overlap of the two distributions, using all
32 backgrounds in each row. They are not a full-protocol approximation bound.

## 3. Diagnostic and inherited controls

No raw output field or its complement equals arbitrary diagnostic p on all
256 assignments. This test is not vacuous: the retained q2.A still equals p
on every assignment, and its whole triple matches the earlier checked
native-second-step calculation. qY before intervention and the earlier
sidecar also match their inherited formulas.

For every fixed assignment of the seven other bits, the two diagnostic p
values nevertheless give distinct whole output triples. Thus the result is
not literal erasure of p. Different background-dependent encodings overlap;
an unavailable background-dependent decoder cannot be substituted for a
common usable interface. Global reversibility is retained throughout.

The old M2 variable was not removed just because its isolated first-arrival
coefficient cancels. It participates in the nonlinear lower computation.
Setting it to zero changes the output table and would change the specified
resource law. Even that hypothetical restriction does not make this endpoint
a uniform clean Y code across all inherited masks.

## 4. Verification and remaining work

`checks.py` rebuilds the C++17 solver in a temporary directory and reproduces
the retained lower slices byte-for-byte. Two small five-source geometries
are checked against an independent full native causal recursion: 384 slice
triples times 64 assignments. These test the bounded implementation; the
strip theorem, not those small cases, justifies the actual huge P.

The separate period checks cover 1,872 nonlinear dipole/strip comparisons,
the complete 512-state L2 permutation and all 40,320 eight-state permutation
exponents. The main checks verify actual control parity, the complete truth
table and distributions, all inherited endpoint controls, and the explicit
overlap witnesses. Normal and Python -O must match. Python 3.12, its standard
library, and a C++17 compiler (`g++`) suffice; no external Python packages or
network access are required.

Run from this checkpoint root:

    python3 six_source_v5/period/checks.py
    python3 six_source_v5/checks.py

This candidate fails the clean-transfer prerequisite, so there is no successful
new carrier law to certify. The complete joint record law for a modified
candidate remains a separate task; terminal marginals do not supply it.
The next useful design must alter the initial controls or route the actual
operand through a compatible extractor while retaining the unwanted
information elsewhere. The untouched junction and this precisely specified
six-source preparation are now excluded as clean interfaces. No broader
impossibility or conclusion against OI follows.
