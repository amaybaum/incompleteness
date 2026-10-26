# Separate-author review of native-phase composition v4

Verdict: **ACCEPT WITHIN THE STATED SCOPE**, with no blocking findings.

Reviewed immutable author commit:
`5b77352f50ddfe750b1cf5cbc72ebdded046df31`, #912,
`verification/programmes/oi-qm/reconstruction/composition-access-20261024/native-phase-v4/`.
The remote manifest at that commit matches the five author-file hashes read
locally; the manifest itself is included in `INPUT-HASHES.json`. This review
has a separate checker and does not import or execute the author's checker.
It is an internal separate-agent review, not external validation, a Lean
certificate, a native implementation or an owner adoption.

## Native formula

I independently computed the six-neighbor parity using three-component bit
vectors and applied H(A,B,D)=(B,D,A XOR BD), then XORed the old local field.
Previous q8 is (0,y,0), its current +z neighbor q9 is (0,X,R), and the other
five current neighbors have total parity C. The resulting raw q8 field is

    (C_B XOR X,
     y XOR C_D XOR R,
     C_A XOR ((C_B XOR X)(C_D XOR R))).

All 5,120 controls using arbitrary pairs of the five other neighbor positions
and arbitrary values agree with the formula. All 5,120 additions outside the
one-step causal cone leave the output unchanged. Omitting C fails in 4,480
cases and dropping the old slice fails in 2,560 cases. The dependence on C
is therefore not an artifact of a first-order update or a chosen source
direction. A further 4,096 tests with three unequal private neighbor values
and the same total XOR give the same next whole-q8 field. This establishes
the stated one-step response invariant; it does not establish all-future
equivalence of those hidden completions.

## Joint-law countercontrols, including failures

The review independently assembles the initial fair seed atoms and the
5:3:2 successful post-Y law. Unlike the author's pooled old-X diagnostic,
the review conditions separately on all four fixed old_x,y public-history
contexts. Thus none of these conclusions depends on averaging those
histories.

In every context, changing C_A from zero to one at fixed C_B=C_D=0 flips only
the next raw D field. Since the other fields determine X,R at fixed y, the
conditional-success supports are disjoint and their TV is 1. The same
terminal failure law of mass 11/16 on both sides gives unconditional TV
5/16. The failure mask 01 retains its actual q9 triples, namely 000,110,011,
100 in lexicographic (old_x,old_u) order. No failed branch is assigned a
successful output state.

For the stronger control, independent fair C_A and C_A=Z XOR XR have identical
distributions conditional on every retained old-history/current-q9 sector.
They also give exactly the same next public q8 law. In the second control,
however, that next q8.D equals retained previous-slice Z; in the first it is
independent of Z. The joint record/Z laws have TV 1/2 on success and 5/32
with the common failures retained. All four old-history contexts give the
same exact numbers.

This supports the report's claim: freshness conditional only on past public
records does not imply the independence from incoming hidden fields needed
by a proposed factorized reset. Keeping the actual joint seed/input measure
inside the response kernel is an alternative to asserting such independence.
The law does not establish a new public Z read. It is a joint outgoing-field
test, as the author explicitly states.

## Operational relation and composition

The report defines a single relation using every allowed finite adaptive
future-record test on the tagged full boundary, with stopping/public-history
tests at depth zero. Under the stated prefix and branch closure of the
common protocol class, its recursive characterization is valid: prefix a
depth-d test by the chosen setting and full record to obtain necessity;
condition a depth-(d+1) test on its first record to obtain sufficiency.
Using unnormalized measures handles zero-probability branches and avoids
changing the relation after an outcome.

The full physical boundary includes both slices and relevant resources.
Equality of every hidden variable is not required, but equality of selected
fields is not sufficient. The sufficient decoder contract correctly adds
an invariant admissible cone, positive mass-preserving decoding and the
complete-record intertwining identity. Stability of decoder fibres under
each response kernel is a necessary consequence. The concrete C controls
exhibit a possible failure of that stability on an unrestricted boundary
space. They do not claim failure on the actual reachable preparation cone.

The report repeatedly and correctly limits the two completions to local
mathematical boundary controls. It does not assert that both can arise from
the retained original-time native sources. It also distinguishes the new
proposed whole-q8 read at L+1 from the source's already stipulated terminal
access ending at L. Consequently no reachability result or access extension
is silently inferred.

## X-reset target and outgoing state

I independently checked all six y/current-whole-port branches. Their
conditional-success probabilities 1/2,3/10,1/5 equal (1/2) times the stated
extra-R refinement factors 1,3/5,2/5. A supplied independent 5:4:1 post-X
sampler with fair Z has fixed-decoder Bloch vector ((-1)^x,0,0), and its R
expectation is (4/5)(-1)^x. All 36 outgoing selected cells agree with the
claimed law. The review constructs the entire full raw-record/outgoing-cell
measure, multiplies success by 5/16, retains failure 11/16 as offered=none,
and verifies equality with the reference branch factorization and total
mass one for each y.

The unchanged post-read sample instead has sharp X and old Y; with fair Z
its fixed Bloch decoder has determinant -1/4 on every nonzero branch.
Thus the report correctly requires actual back-action/reset and a reusable
full-boundary invariant. Its fresh sampler is clearly a law-level positive
control with no additional reset herald, rather than a native source or a
new physical reset.

## Verification and boundary

`python3 checks.py` and `python3 -O checks.py` produce byte-identical retained
`result.json`; source compilation passes. The review checker reconstructs
the formulas and laws without author-code imports, uses exact Fraction and
bit-vector arithmetic, and raises on failed controls before printing its
acceptance result. It supports execution from the published review directory
with author files in its parent.

The accepted result is the local native response dependency, the two scoped
joint-law controls and the precise conditional continuation contract.
Original-time reachability, actual future public-bank freshness, physical
observer access, reusable native reset, unrestricted depth/menu, A1 state
and operation coverage, A2 bounds, composites and transport certification
remain open. The review does not alter #885 or any physical premise.
