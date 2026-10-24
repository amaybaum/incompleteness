# Native-Y continuation: current research handoff

24 October 2026. Draft #910 contains the current native candidate and internal
separate-author reviews. #885 stays read-only for this effort, with programme
synthesis pinned at 2d555f17c23bea31d32b3f5eb4c49d245b413a76. No physical
premise, observer-access rule, F/E designation, merge or full-equivalence
verdict is adopted. A1 and A2 retain separate targets and verdicts.

## Current result: conditional post-Y phase preparation

The [combined result](phase_joint_v10/REPORT.md), reviewed at author revision
9b334367864c39e969072d9fbd46b0c049584963, gives the supplied calibrated post-Y
law in selected fields of the actual two-slice native state. On success:

    previous q8=(0,y,0), current q9=(0,y XOR a,y XOR b),
    current remote Z=(0,0,z), current remote herald=(0,1,0).

Here y=x XOR u is the existing native Y result. There is one fixed phase
coordinate map to (X,Y,R,Z)=(y XOR a,y,y XOR b,z), with no history-selected
extraction. Conditional mask weights are 5:3:2 on 00,10,11 and z is jointly
fair. Success is 5/16 and terminal failure 11/16. No nonlinear initial seed
prior or unknown-input copy is used. This closes the calibrated selected
phase-preparation calculation on the retained native family; it does not
close a reusable measurement interface.

Keep T=185, P=12*840^185, S=T+P, d=68, R=S+d and L=R+9. The local controller
uses the existing original-time depth-nine preparation and three affine
boundary sources:

| Source | Initial position | Payload |
| --- | --- | --- |
| J | (0,S,S+154) | (u XOR b,a,u XOR a) |
| Kplus | (1,S,S+153) | (a XOR b,0,a XOR b) |
| Kminus | (-1,S,S+153) | (a XOR b,a XOR b,a XOR b) |

Their coupled evolution produces the nonlinear dependence required by the
accepted two-mask outputs. Previous q8 retains Y as part of the second-order
Markov phase; current q9 carries X and R together. The remainder of the
apparatus is retained workspace, with no erasure or full-boundary independence
asserted. The [native controller](branch_v10/local-controller/REPORT.md) and
its [independent review](branch_v10/local-controller/review/REPORT.md) pin the
exact dynamics, source geometry, physical failures and intervention limits.

At (+48L,0,0), the [remote herald](herald_v10/REPORT.md) executes the retained
2684-step predicate, (P-2424)/6 six-step identity words and two final H steps.
At (-48L,0,0), an independently phased z pulse arrives at the same L. All
sources are supplied initially and are affine in six shared fresh bits
(a,b,k0,k1,k2,z). No large-radius transport period is substituted for P.
The exact arbitrary-length wing formula and its terminal source row are
independently reviewed. The enlarged no-wrap torus is explicit.

## Full record and failures

The old seven-port noise word N through L remains uniform conditional on
its initial-bank complement. Its bit count is B=6P+18d+189. The combined
local and remote readiness/source regions preserve that independent bank.
The new herald has a blank raw prefix and exposes only (0,G,0) at L.

For every nonzero-probability incoming offered-carrier history D satisfying the retained
native-family assumptions, including the allowed earlier Y record y,

    Pr(N=n,G=1,E_phase(j) | D) = 2^(-B) (5/16) mu_Y,y(j),
    Pr(N=n,G=0,offered=none | D) = 2^(-B) (11/16).

This is a joint selected-phase/public-record law, rather than separate
matching marginals. Prior flags remain in D; a previous terminal failure
never offers a new carrier merely because the physical new G is one.
The used old u is not assumed fresh. The new six-bit prior, readiness,
clock and access convention are explicit supplied resources.

The named selected phase fields are retained on every rejected branch. The rejected K counts on
00,01,10,11 are 3,8,5,6. For01, q9=(u,y,x(1 XOR u)), giving 000,110,011,100
by lexicographic (x,u). No chosen quantum failure state replaces those fields.
The full success and failure measures are checked over 1024 old/new worlds.
The huge noise factor follows from the written chronological-bijection
proof and geometry, not enumeration of all L ticks.

## Bounded terminal records and remaining interface

Under the candidate's permitted single whole-q9 terminal read, the complete
(X,R) raw record on a post-Y_y success has masses 1/2,3/10,1/5 on
(y,y),(1-y,y),(1-y,1-y). These give the correct designated terminal X or R
probabilities with supplementary-record factors depending only on public y,
setting and outcome. Both raw fields are retained. Thus the bounded terminal
X-to-Y-to-X and X-to-Y-to-R record comparison passes, inheriting the
predecessor's conditional native-family and terminal-access assumptions.
It is not a general menu read on arbitrary preparations or a direction
selector. Extra terminal metadata on failure must retain the actual rejected
law, without asserting a successful measurement or offered state there.

After the whole q9 port is read, the unchanged selected phase conditions on
sharp X and old Y; its fixed Bloch decoder has determinant -1/4. It is not
a valid post-read quantum output. The next construction must provide actual
back-action/reset before another successful instrument is claimed.

The precise next target is a native continuation accepting this actual
phase. It must deliver previous-slice Y when required, handle both exposed
X/R fields, retain the complete physical neighborhood and old-record
correlations, and preserve a joint quantum branch law. The arbitrary q8.B
socket still fails when its past is held fixed. Do not replace the phase
by a separately cold late-time apparatus or use a history-selected decoder.
Future public records beyond L also need a new bank audit including the
new herald port; the current proof stops at L.

## Other findings and broader programme

The [one-source affine audit](branch_v10/REPORT.md) rules out three accepted
mask codes from one affine J; it is superseded constructively by the richer
native controller, not contradicted. The [alternate remote fanout](layout_v10/REPORT.md)
fails its positive direction's old-Z readiness and its safe direction's
order-three full-law condition. Those exclusions remain specific to their
examined families. Reviews are retained with each result.

#912 remains at 69540662b234e37c6805ded244962a80f15f63a2. Its fixed history
comparison, strict raw-tag obstruction and post-read positivity controls
remain valid. #911 remains at 81bc53e482158072869b916116a4fc0f8b28f99e:
almost-sure irrational sampling does not overcome the examined fixed-G3
operation obstruction. Neither audit is a no-go for OI generally or a
separately specified record-level A2 model.

Calibration selection; native initialization, clock and settings; observer
access derivation; arbitrary menu/depth; composite/Bell structure and full
state/operation coverage remain open. The present finite calibrated family
does not resolve A1. A2 needs its own protocol class and error bound.

## Replay and checkpoint discipline

Run python3 replay.py --latest for the eleven new author/reviewer/controller
mode groups. Both normal and -O runs must match their retained structured
outputs. The full driver has 41 groups. This continuation freshly runs only
the 11 new groups, verifies the complete manifest and compiles sources; the
preceding 30 groups retain unchanged sources and earlier passing evidence.
No new full-suite run, Lean certificate or exact-head attestation is claimed.

All new calculations and separate-agent internal reviews are committed on
the existing draft branch. Internal review is not external validation or
owner adoption. Required off-main evidence must land with any dependent
enduring claim under AGENTS section A.42. Preserve forward history; no merge,
force-push, special dispatch, F/E designation or branch deletion follows.
No unattended future work is scheduled.
