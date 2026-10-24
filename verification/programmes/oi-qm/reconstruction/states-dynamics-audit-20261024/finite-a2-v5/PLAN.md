# Finite geometric approximation of the supplied qubit sphere interface

Research plan fixed before new checker execution, 24 October 2026. Source
#911 starts at `088af1453efc7780187bc81f8f765f5005b91870`; the common
five-path contract is #910 at `1324d9a854da60d0274ba77fe80d08e7cf2b1ef1`.
No operational map, prior, private-access rule or physical source is adopted.

## Productivity test and architecture alignment

Construct a common finite geometric controller with an explicit adaptive
full-record/outgoing-state error and finite initial fair-bit budget. A lookup
of quantum protocol answers or another existential reproduction statement is
not sufficient. The model must answer from its actual finite carrier and
known setting, without an external unknown-preparation label. Its supplied
Kochen-Specker sphere density/response/reset contract is aligned with
architecture_v5, not derived from native OI dynamics or calibration selection.

The continuous comparison uses pure densities
mu_n(lambda)=(n dot lambda)_+/pi on S^2, response sign(a dot lambda),
rotations lambda->R lambda and fresh reset mu_(s a). Preparations are pure
rational unit directions and explicitly sampled dyadic mixtures. Allowed
measurement axes and proper rotation generators are fixed finite rational
menus. At most h adaptive operations occur, with fixed public ticks and
certain-success flags; early stopping is absorbing padding. Whole records
and decoded outgoing states are compared, including zero-mass branches.
No failure is hidden or postselected. All seeds are present initially.

## Fixed finite construction to test

Partition the sphere by six cube faces. On one face use p=(+/-1,u,v), with
the appropriate coordinate permutation, lambda=p/||p|| and -1<=u,v<=1.
For a unit n the unnormalized density in these coordinates is

    g_n(u,v)=(n dot p)_+/(1+u^2+v^2)^2.

Its integral over all faces is pi. Use an even M-by-M midpoint grid on
each face, M>=8, giving N=6M^2 finite labels. Round each positive rational
g_n to an integer floor(2^W g_n), W>=4, normalize these integer weights,
then approximate the normalized CDF with one B-bit uniform integer.
Preparation and each measurement reset use their own fresh initial B-bit
block. No rejection sampler, variable stopping depth or fresh insertion is
allowed. A dyadic preparation-mixture label, if needed, has its own initial
bit budget and remains private.

The physical finite carrier stores a grid index and a rotation word of
length at most h. Unitaries append their known generator; the read response
is sign(a dot R_word p_index), with a declared deterministic zero convention.
The response never consults the preparation label. Reset discards no physical
information: it retains old carrier/seed/workspace privately and prepares
a new grid index and empty current rotation word. No return coupling or
extra private read is permitted under this supplied abstract contract.

For a rational decoder point, divide p_index by an upward rational
approximation to ||p_index|| with error at most1/M. This gives ell_index
inside the unit ball and within1/M of lambda_index. The fixed decoder is
linear on measures, with Bloch vector alpha E[R_word ell_index]. Its alpha
is selected from the proved uniform moment-error bound before testing;
it may not be adjusted to make the measured examples pass.

## Proof obligations and decision rule

1. Derive the cube-face area/density formula. Prove positivity and total
   weight>0 for M>=8,W>=4. Prove a global midpoint/floor/CDF cell-TV bound.
2. Couple the finite cell law to the continuous law and bound hemisphere
   disagreements by the boundary-band mass. Atomic/continuous TV is1 and
   is not the approximation metric. Exact stored rotation words must add no
   geometric rounding drift.
3. Use one explicit rational upper bound e for the first-moment error and
   alpha=1/(2/3+e). Prove decoded positivity on the complete admissible cone
   of preparation/reset rays and their rotations/positive mixtures.
4. Derive uniform conditional per-read error kappa and final state error
   chi. Prove joint classical-record/quantum-state trace distance at most
   min(1,h*kappa+chi) for every fixed finite adaptive policy, not only
   pooled outcomes. Keep zero branches and fixed flags/ticks explicitly.
5. Give M,W,B choices achieving any declared epsilon>0, source alphabet,
   word/workspace and initial fair-bank counts. Distinguish finite existence
   from efficient implementation and from physical/native availability.

Candidate conservative constants to audit independently are cell mismatch
48/M+8*2^-W+(N-1)*2^-B, geometric point error<=3/M, hemisphere error
52/M+8*2^-W+(N-1)*2^-B, and moment error
e=99/M+16*2^-W+2*(N-1)*2^-B. If any proof/control fails, revise or reject
the bound before rendering a pass. No measured constant may replace a
universal proof.

## Bounded controls fixed in advance

Use exact rational cube weights, CDFs, response signs and matrix rotations.
Check grids M=8,16 (a larger smoke grid only if cheap); several finite bit
depths; Pauli axes and a=(3/5,4/5,0); H, quarter-Z and the rational
non-Clifford rotation with first row(3/5,-4/5,0). Include mixed Bloch
preparations +/- (2/3,-2/3,0) via explicit rational pure-state mixtures.
Independently compute target projector/rotation laws and exact adaptive
trees at short horizons, with certified rational norm/error intervals.

Controls must detect reuse of a reset block, exposure of a private carrier
or seed/timing label, inadequate bank allocation and omission of adaptive
branch probabilities. All proper rotations preserve geometry; the fixed
shrunk decoder must be positive. A positive no-reset/unitary-only control
must not spuriously accrue geometric rounding error. If a proposed mutant
does not actually change a tested law, report that and select a justified
explicit witness rather than asserting detection.

Normal and optimized Python must emit identical retained structured output.
Use standard-library exact arithmetic and explicit exceptions. No large grid
campaign, Lean build, special dispatch, GitHub mutation or #885 edit is part
of this work. Root publishes the six curated source/evidence files and
commissions separate review before incorporation into the combined handoff.
