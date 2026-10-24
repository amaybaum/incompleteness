# Separate review of the coupled-pool composition checkpoint

**ACCEPT the scoped joint-kernel result, with no blocking findings.** Author
revision: `621e1a05776be4bcf870e2db61fa05244a354f1c`, #912 directory
`native-coupling-v5/`. All six author files match their immutable GitHub
blob IDs and SHA-256 pins. The new checker imports no author code.

This is internal separate-author review. It accepts an exact native scaled
control and a conditional actual-phase comparison. It does not certify a
physical acceptance gate, new observer access or a reusable instrument.
Native A's actual-scale source/readiness proof is an explicit dependency,
not established by the two-tick scaled test.

The reviewer authored Native B's source checkpoint. The Native B section
here independently checks its use as pinned literal input by the composition
author; it is not an independent revalidation of that source engine.

## 1. Independent native reconstruction

The review computes both ticks from the complete backward cone of the central
tick2 output and its six tick1 neighbors. Initial fields outside radius2
cannot influence any of these values. The previous slice is zero; the
current slice contains oldP at the origin and the three supplied source
triples at (-1,0,-1),(-1,0,1),(-2,0,0). This forward cone calculation differs
from the author's full sparse-lattice step implementation and retains every
relevant off-axis neighbor and the old-local term.

All4096 source worlds agree with the native source-response formulas and
the fixed seven-site inverse. With F9=0, the exact XOR of the six tick1
neighbors is the quadratic second difference of H. Applying H once more
gives the asserted tick2 central value

    V=oldP XOR(0,F8.B*F10.D XOR F10.B*F8.D,0).

The complete raw law has masses5/8 and3/8 on oldP and oldP XOR010. Omitting
the shared neighbor predicts a uniform raw triple and changes that law by
TV3/4. For every old triple, Q8,Q10,M have64 distinct joint outputs and all
three pair marginals are uniform over64 values. Their triple law differs
from the512-point product law by TV7/8. Pairwise independence is insufficient
for this source-reachable native step.

On the four old successful triples (0,s,r_old), the pooled abstractly
accepted carrier still equals the intended5:4:1 selected measure. The review
independently constructs each normalized two-by-two Hermitian density matrix
after exposing whole current q9. All eight nonzero raw posteriors reproduce
the author's masses and negative determinants exactly: -1/64, -1/4,
-5/196, -5/36, twice -1/20 and twice -1/25. Thus the unchanged selected
carrier and this extra raw read do fail the proposed quantum output
comparison. This is the explicit scaled six-bit control, not a proof that
the actual enormous-L candidate has that same dirty-neighbor function.

## 2. F9 repairs the conditional whole-port kernel

In the scaled three-source native world, the map from F8,F10,F9 to Q8,Q10,M
is triangular: Q8 determines F8, Q10 determines F10, and M then determines
F9. Each step uses an eight-state permutation. The review verifies every
one of the512 outputs for each old triple. It also verifies that Q8,Q10,V
are jointly uniform in those actual source worlds.

For the actual-scale proposal the corresponding source theorem is inherited
from Native A. That theorem must supply the original-time geometry, initial
conditional independence and first-arrival permutation hypotheses. Given
those hypotheses, let C be the XOR of the three remaining neighbor triples.
For every fixed oldP and C,

    V=oldP XOR H(Q8 XOR Q10 XOR M XOR C).

The change from M to V is a permutation while Q8,Q10 remain fixed. Hence
the conditional full Q8/Q10/V law is uniform. No assumption of linear
superposition or independence of arbitrarily chosen dirty neighbors enters
this argument.

The review exhausts all32768 oldP/C/pool/M combinations. On valid oldP it
checks the entire (whole V, abstract A, selected output) kernel, including
zero target cells and rejected selected coordinates. Acceptance is5/16;
rejected mask counts are3,8,4,7 on00,01,10,11 with fair Z. Every whole-V
accepted posterior is exactly mu_X,s and its density matrix has determinant0
and nonnegative diagonal entries. These256 posterior checks include all
eight fixed C values; the author's32 posteriors correspond to its fixed
scaled native C. The difference in counts is deliberate.

The success and failure submeasures remain distinct. Previous terminal
failure never offers a new carrier, even when the new reference A happens
to equal1. The rejected selected coordinates retain their actual classical
measure; no chosen quantum failure state is inserted.

The inverse comparison is also exact at the actual phase:

    oldP=current q9 XOR H(XOR six previous neighbor triples).

It is a fixed local two-slice formula, not a history lookup. It is also
a consequence of the native update and does not implement an observer read
or a native unmasking/predicate circuit. Preserving that mathematical
comparison and masking a whole port are useful partial results; they do
not provide the missing actuator or next-stage acceptance invariant.

## 3. Flag countercontrols are substantive

After the F9 repair, whole V is independent of the specified reference A.
The review enumerates all256 deterministic Boolean functions of V. Their
minimum total variation error on (flag,V) is5/16, whereas their best flag
marginal error is only1/16. Current q9 therefore cannot simply be renamed
as the intended A port.

An unrelated independent flag with the exact5/16 rate also fails. It leaves
the selected mask distribution uniform rather than calibrated5:4:1. The
review checks conditional carrier TV2/5 and full success/failure/raw-port/
offered-carrier TV1/8. The retained R comparison attains that error because
R=s has probabilities1/2 and9/10, respectively. Both pooled XYZ Bloch
vectors can still equal the pure X vector. Thus positivity or those moments
alone would miss a real fixed-menu discrepancy.

These bounds concern the stated fake-flag extensions with the output
comparison held fixed. They do not bound a future native gate using other
operands, another accepted physical carrier or a properly computed flag.
The R comparison is stipulated in the target; no later native R read has
been constructed here.

## 4. Native B adapter and scope

The review statically extracts the author's512-entry Native B literal table,
checks its hash against the pinned Native B source, and applies a fresh
lookup implementation. It executes no author source engine. All64 fixed
context/N permutations, the144 pad-sensitive rows and the witness
[1,3,1,3] agree. The witness preserves selected q9 but does not establish
equal complete earlier public history; pad changes may alter informative
ciphertexts. The report correctly avoids operational-inequivalence claims.

The32 opposite-sign pairs at u=0,a=b=1 also agree. Current q10 is identical
for both unknown signs for every N and pad pair, while previous q9 retains
the distinction. This excludes q10-only pointwise decoding in that source
geometry, not a multi-site/two-slice decoder, a different source contract
or a general native reset. A uniformly random N would make that current
port uniform conditional on its old context; this is a fresh resource,
not evidence of unknown-X transfer.

## 5. Evidence and remaining obligations

All source-file hashes and published blob IDs are pinned in INPUT-HASHES.json.
The referenced Native A/B local snapshots also match their hashes in the
composition provenance. The review verifies4096 two-tick source worlds,
24 pairwise controls, all eight nonpositive raw posteriors,32768 conditional
kernel worlds,256 positive accepted raw posteriors, all flag controls and
the compact Native B adapter. Normal and optimized executions match
result.json byte for byte with explicit exceptions enabled.

Run `python3 checks.py --author-root <native-coupling-v5>` and compare stdout
with result.json; repeat with `python3 -O`.

The accepted positive conclusion is conditional whole-port metadata masking
and preservation of a selected phase code under the intended abstract
acceptance. A physical predicate and full raw flag/prefix law remain open,
as do preservation through its delay, native output-boundary closure,
observer access, arbitrary menu/depth, full A1 coverage, A2 guarantees and
composites. The scaled native control is not actual-scale simulation, and
the fixed inverse is not an available native gate. No stronger status is
supported or asserted by this checkpoint.
