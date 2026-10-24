# Executed finite-menu A2 certificate with 1,536 geometric labels

24 October 2026. This is a conditional single-qubit approximation result
for a specified finite menu and a total horizon of three operations. It
uses the supplied Kochen–Specker geometric preparation/response/reset
architecture. Native OI sourcing, probability selection, a physical native
clock, access closure, general instruments and composites remain open.

The plan was published before computation at
`cf1855ed1576adf446fbc505c027928bce4c4cb7` on #911. Its base is #911 at
`f2426f16d0054943ca4937648a9ff9613d08f960`. The earlier uniform all-menu
geometric theorem and its conservative resources remain valid and unchanged.

## Result and scope

The fully instantiated M=16, W=16, B=24 controller has 1,536 geometric
labels. A single fixed decoder is positive on every declared preparation,
reset, rotation and positive-mixture ray. For **every adaptive policy over
the specified menu with at most three total operations**, the complete
public record and decoded outgoing state differ from the quantum protocol
started at the decoded input by CQ trace distance at most

    17239332625914280559 / 230584300921369395200
      < 0.074764 < 1/10.

The rational comparison with 1/10 is exact. Decimal displays are rounded
readability aids, not computational evidence. This is an error upper bound,
not a confidence percentage or a success probability.

The finite menu is explicit:

- Preparations: both signs of X, Y, Z, a=(3/5,4/5,0), and both signs of
  p=(2/3,-2/3,1/3), q=(2/3,-2/3,-1/3), plus their positive mixtures.
- Projective read axes: X, Y, Z, a. Each read resets to the corresponding
  measured eigenstate distribution using a fresh reserved initial block.
- Rotation generators: H: (x,y,z)->(z,-y,x); S: (x,y,z)->(-y,x,z);
  R: (x,y,z)->((3x-4y)/5,(4x+3y)/5,z); and r=R inverse.
- The same total clock advances through three operation slots. A read
  clears the rotation word, but does not restart the clock or bit budget.
  Absorbing stop slots retain their state and pad the public record.

This guarantee covers every policy in that menu, including arbitrary
choices based on earlier public outcomes. Independent randomized choices
inherit it by convexity, with their resources counted separately. Arbitrary
rotation generators, an enlarged preparation/read menu or a longer horizon
need a fresh envelope certificate. The old all-menu continuum bound has a
broader quantifier; the two resource statements must not be interchanged.

## Actual geometric controller

The carrier construction is the earlier six-face grid, not a lookup of
quantum protocol answers. A label is an integer point z on a cube face,
with one coordinate +/-M and two odd coordinates from -M+1 to M-1.
Its inward rational vector is

    ell(z)=z/ceil(sqrt(z dot z)).

For a preparation direction n, the integer geometric weight is

    I_n(z)=floor(2^W M^3 (n dot z)_+ / (z dot z)^2).

CDF cuts are floor(2^B cumulative_weight / total_weight). Their differences
are exact counts of initially supplied B-bit seeds. Opposite preparations
sample antipodal labels with the same seed. This ordering preserves exact
zero means for antipodal mixtures. The seed-to-index and geometric-sign
controller depends only on its actual label, retained word and requested
setting after preparation; it never consults an unknown preparation label.
The known preparation instruction is used only to establish its initial law.

A rotation appends its exact rational generator to the current word. A read
returns + iff a dot R_word z>=0, with zero assigned to +, and otherwise -.
It then prepares the chosen reset law from a fresh independent block and
clears the current word. All old labels, used seeds and workspace are
retained privately in a generic reversible dilation; no information is
physically erased. That dilation is not a compilation into the native H
field rule. No observer access to its private registers is supplied.

## Exhaustive finite envelope and positive fixed decoder

Let m_n be the exact rational grid mean E_n ell. Use the **same** linear
map in every clock sector, at input and output:

    D(mu)=(mass(mu) I + (3/2) E_mu[R_word ell] dot sigma)/2.

The verifier does not select a decoder from a favorable protocol result.
The preregistered first choice alpha=3/2 passes the complete ray check.
The maximum squared decoded Bloch norm at M=16 is

    47716765703861269321503281838235309 /
    50432868877265397685582603223040000 < 1.

There are twelve canonical preparation/reset directions and 85 formal
words of length zero through three. All 1,020 ray/word positivity checks
are exact. Rational rotation orthogonality preserves both squared norm and
the raywise target error. Thus positive mixtures are positive too. This
phase cone is closed at each completed operation within the remaining clock
budget. No positivity is asserted for privately conditioned individual
atoms or an exposed pre-reset intermediate cut.

Define chi as the maximum trace distance between D(nu_n) and its associated
pure target n. The norm is enclosed by rational intervals whose squared
endpoints are checked. The executed bound is

    chi <= 266098754553528263 / 18446744073709551616.

It is approximately 0.014426. The witness ray is Z+. The source response is
computed exactly for every canonical ray, each word of length at most two,
and every read axis. That is 12*21*4=1,008 cases, with 324 distinct cached
direction/probability cases. Their exact maximum single-read error from the
associated quantum pure-ray law is

    kappa = 6419131 / 419430400.

The witness is X+, word r, read a: actual plus probability is
6296563/16777216, whereas the associated pure target gives 9/25. These
numbers are measured results of the predeclared envelope, not fitted inputs.

The probability envelope checks every ray/word/read combination. It is a
verification computation; the physical source controller stores geometric
CDF/sign maps and has no table of quantum protocol outcomes.

## Why the envelope covers every adaptive record and outgoing state

Before the first read, an initial positive mixture evolves by a known exact
word. Its next binary-record probability differs from the associated ideal
mixture by at most kappa, by convexity of the exhaustive ray envelope.
After a read, its independent fresh reset produces nu_(s a), regardless of
older hidden data. Conditional on any complete public history, subsequent
pre-read laws are again rotated canonical reset rays. Maximal coupling of
the next binary outcomes therefore gives complete-record TV at most h*kappa.
This is an argument about public conditional kernels, not an assertion that
an ontic coupling remains independent after conditioning on matching records.

For each complete history, the last reset and remaining exact word make the
normalized source outgoing decoder at most chi from the associated ideal
outgoing quantum state. On a history with no read, the initial-mixture bound
applies. Summing subnormalized branch operators gives CQ distance at most
h*kappa+chi. Branches of zero mass are included without normalization.

The source's associated ideal preparation and its single fixed decoded input
are themselves within chi. The adaptive quantum experiment, with its full
record and output, is a trace-preserving quantum channel, so this initial
comparison contracts. A triangle inequality gives

    CQ(source experiment, quantum experiment from D(source input))
      <= min(1,h*kappa+2chi).

With h=3 and the exact envelope above this is below 1/10. The proof covers
all positive-mixture decompositions in the stated preparation cone; the
source apparatus receives no private decomposition label after preparation.

Properly provisioned public success flags are always one. Public ticks,
settings, outcomes and absorbing-stop metadata are retained and have the
same deterministic adaptive format on both sides. An existing terminal
failure sector can be adjoined identically with its actual mass and no
carrier; this does not implement any new native acceptance flag.

## Resources and measured comparison

The fixed clock reserves one 24-bit preparation block and one fresh 24-bit
block per operation slot, even if the slot is a rotation or stop. Hence the
initial fair-bank requirement is **96 bits**, plus preparation-mixture and
randomized-controller bits when applicable. An exactly sampled dyadic
mixture uses its own finite initial block; non-dyadic mixture priors require
an additional sampling resource and are outside this fair-bit count.

| Resource | Executed finite-menu controller |
| --- | ---: |
| Grid labels | 1,536 |
| Word-tagged carrier label upper bound | 130,560 |
| Current carrier register width upper bound | 17 bits |
| Public clock width | 2 bits |
| Initially fair bits, excluding mixtures | 96 bits |
| Twelve distinct geometric CDF tables | at most 460,800 bits |
| Optional hemisphere response tables | at most 522,240 bits |
| Retained old carrier registers | at most 3 |

The CDF table bound uses 12*1536*(B+1) bits, including duplicated antipodal
storage if desired. The response-table bound is 4*1536*(1+4+16+64) bits.
These are deterministic descriptions computed from geometry. The old
billion-label resource example was a conservative arbitrary-menu bound;
this 1,536-label example is certified only for the displayed menu/horizon.
The improvement comes from a narrower exhaustive envelope and using the
actually positive fixed 3/2 decoder, not from a universal convergence-rate
improvement.

Every grid point, weight, seed-count mass, required moment and envelope
probability was executed. We did not enumerate all 2^24 seeds or all adaptive
policies. Exact CDF counting accounts algebraically for every seed, and the
exhaustive local envelopes plus the preceding proof account for all policies.

The prescribed ascending search tested M=8 and M=16. M=8 has certified CQ
upper about 0.179020 and fails the 1/10 threshold. M=16 has upper about
0.074764 and passes, so the predeclared stop rule did not execute M=32 or64.
No unexecuted large alphabet supports this result.

Finite tables and fixed-width scans admit a finite padded Boolean/reversible
schedule. This supplies a mathematical fixed-clock implementation contract;
the Python evaluator is not constant-time hardware, and native gate/time
cost has not been established. The 96 fair bits exclude controller tables,
blank registers and retained workspace, all of which remain explicit costs.

## Controls, replay and limits

The checker uses exact rational weights, CDF counts, moments, signs, matrix
products and branch operators. Rational square-root intervals certify CQ
norm upper endpoints. It imports no prior checker. Its rational-complex
2x2 reference independently agrees with all 48 generator/direction rotation
cases, and twelve inverse-word controls detect no unitary rounding drift.

Eighty independent adaptive protocol/input trees give 672 nodes, 352 complete
leaf records and 178 zero-mass nodes. They include mixed inputs, adaptive
settings, repeated measurements, absorbing stops and a unitary-only path.
They check the quantum experiment started at the actual decoded input,
using the same fixed decoder on all outgoing branches.

A 1,024-seed small sampler is exhausted against a separate full scan, with
pointwise antipodal sampling checked. Countercontrols detect reset seed
reuse (TV=11/256), ignored adaptive setting (TV=153/1024), and an insufficient
bank (terminal failure mass=1/2). Equal-decoder antipodal X/Z mixtures are
distinguishable by extra private carrier or timing access, with the exact
positive gaps retained in result.json. These mutants demonstrate changed
contracts; their errors are not labelled violations of the main controller's
bound.

Run `python3 checks.py` or `python3 -O checks.py` from this directory. Both
emit result.json byte for byte; Python compilation passes. SHA256SUMS covers
the other five curated artifacts. PROVENANCE.json pins inherited source reports and
the published plan. No full-suite/Lean certification, physical premise,
observer-access adoption, F/E designation, dispatch, merge or #885 change
is included. The supplied cosine prior, projective reset, private workspace
isolation and clock are still load-bearing assumptions.
