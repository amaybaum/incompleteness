# Separate-author review of the native fresh pool and abstract X target

Author checkpoint: `6e9a3ec567a1f3472bad3ed23c48b8111d2f0515`,
`native_pool_v11/` on #910. **Accept the native conditional resource and
the abstract full-law calculation within their stated scope; no blocking
findings.** The acceptance predicate remains abstract. This review does not
construct a native X instrument, native flag or reusable interface.

## Physical resource and fixed phase map

The native resource is inherited from `native_v11` at
`7ec3f8234a148cadb58ebc6c8212b3b0233acabe`, separately reviewed with the
wording correction applied. For every fixed complementary initial state,
the two negative-x witness triples map bijectively and independently to
the whole current q8/q10 pair at L+1. With the supplied independent uniform
initial triples, that pair is uniform over 64 values conditional on the
entire complement. The output permutations may depend on the complement;
their conditional uniformity is nevertheless exact. No fresh bit is
inserted at L+1.

The new reviewer independently verifies the public-cone distance bounds:
the earliest specified public arrivals from the two sources are L+77 and
L+79. Hence the entire retained public past through L+1 is a complement
function. Conditioning on that past, old flags or actual previous q9 does
not bias the uniform pool. This statement does not extend automatically
through an unspecified computation delay or arbitrary new access.

At L+1, previous q9.B is the actual designated old X bit s. The mapping

    Y=b1, R=b5, Z=b4, K=b0+2b2+4b3

uses each of the six pool bits once and is a bijection onto the 64 possible
Y/R/Z/K assignments. It is fixed across histories. Reading previous fields
or delivering s to another native gate remains an unconstructed operation.

## Full target measure and independent assembly

The reviewer specifies the target independently as six explicit cells:

| Y,R | Probability for each Z value, with X=s |
| --- | ---: |
| s,s | 1/4 |
| 1-s,s | 1/5 |
| 1-s,1-s | 1/20 |

The union over both signs is the full calibrated 12-state codebook. Direct
enumeration of the actual six-bit field map and predicate thresholds
5,0,4,1 gives exactly this measure, 20 accepted and 44 rejected pool phases
per sign, and independent fair Z jointly with Y/R. This verifies the
complete measure, not just its Bloch coordinates or one terminal outcome.

The checker imports no author engine. It decodes all 64 relevant parent
source-table rows using an independently packed witness index and checks
the successful raw q9 formula. It also checks the physically failed 01
mask explicitly:

    raw q9=(u,x XOR u,x*(1 XOR u)),

including its nonzero A field. No replacement quantum failure state is
inserted. A separate arithmetic implementation of H evaluates the retained
2,684-step herald word and its final phase on all 32 seed rows, confirming
thresholds 5,0,3,2. Independent parent Z doubles this to 64 old seed cases.

The complete old/pool assembly contains 65,536 worlds across 16 old
input/history rows. For each valid incoming offered-carrier history and
each whole old successful raw record h, the checker verifies every
outgoing carrier cell:

    Pr(h,A=1,j)=Pr(h)*(5/16)*mu_X,s(j),
    Pr(h,A=0,offered=none)=Pr(h)*(11/16).

The old raw record retains both s and r_old. The current raw pool and
actual previous q9, old Z and old herald are retained in the selected
physical failure measures. Accepted and rejected measures partition all
worlds, including old G=0. No discarded field is silently assigned a
quantum output. The computation is a finite selected-phase accounting;
the unlisted global workspace remains part of the native state.

Per 4,096-world old history row, the respective branch counts are 400,880
and 2,816. Their probabilities are 25/256,55/256 and 11/16. These numbers
are conditional on a valid incoming offered-carrier history. They do not
replace upstream failure probabilities or permit restarting a carrier
after an earlier terminal flag.

## Controls and remaining native obligations

All six specified negative-control families are detected independently:

- Swapping 4:1 yields TV 3/10 at unchanged 5/16 acceptance.
- A forbidden 01 threshold introduces excluded code and rate 11/32.
- Stale Y in place of s gives TV 4/5.
- Reusing old public R gives TV 1/10 or 9/10.
- Shared Z preserves its fair marginal but gives joint TV 1/2.
- Offering after old G=0 produces false-offer mass 55/256.

The conditional pool theorem and this reference predicate do not imply
that an observer can evaluate A, that the original sources may preload a
function of unknown s, or that a flag port can reveal only one selected
field. A native implementation must deliver actual s, consume the actual
pool, produce its whole raw public flag record, and preserve the joint
carrier/history law for its full computation duration. Extra metadata may
invalidate an otherwise correct scalar acceptance law.

The author correctly leaves old-X delivery, native predicate and flag,
delayed public-history audit, fixed usable next phase, back-action/reuse,
access closure and broader A1/A2/composite questions open. The supplied
5:4:1 calibration is reproduced, not selected by this construction.

## Replay and provenance

Run `python3 checks.py` and `python3 -O checks.py`, optionally specifying
`--source-root`, `--author-root` and `--native-author-root`. Both outputs
match result.json byte for byte. INPUT-HASHES.json pins the six author
files, reviewed native resource files and two retained parent data files.
All verdict checks use explicit exceptions and exact integer/Fraction
arithmetic; SHA256SUMS covers the five review files.
