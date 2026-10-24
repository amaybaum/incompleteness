# Separate review of the native short-window gate checkpoint

**Verdict: ACCEPT WITHIN THE STATED SCOPE. No blockers found.**

This separate-agent internal review pins author
`8ae927163c0fa340b312d634fc352df73753314f`, under
`verification/programmes/oi-qm/reconstruction/native-y-continuation-20261024/native_gate_v13/`.
All six published Git blobs equal the local curated author files, including
the plan, report, program, structured result, provenance and manifest. Exact
blob IDs and sizes are retained in INPUT-HASHES.json. The review does not
import the author's engine or modify the author files, Git refs, PRs or #885.

The accepted positive result is actual native nonlinear old-sign/pool
coupling in the declared small original-time source family. The negative
result concerns passive single-cell acceptance readouts in seven explicit
families, 25 sites and a three-deadline window. It is not a no-go for the
programme's huge-L boundary, distributed circuits, different initialization,
later deadlines, alternative encodings or OI generally. No physical access
rule, implemented acceptance instrument or equivalence proof is established.

## 1. Independent native reconstruction and input provenance

The review uses a newly written iterative forward engine. It initializes both
slices of a shrinking Manhattan cone directly from the published background
formula and four original-time payload sources, rather than invoking the
author's recursive cached field evaluator. Each of the 4,096 payload worlds
is a separate bit in three integer Boolean columns. Evolution applies all
six neighbors, old-local fields and the native B*D product at every site.

For the latest queried time n+3 and sites of radius at most two, the necessary
initial current slice lies inside radius n+5. The previous slice needs
radius n+4. The engine initializes exactly those cones, then shrinks its
computed spatial domain by one at every tick. Thus the spatial restriction
includes every incoming path of the infinite dirty background. It does not
set an unexamined outside neighbor to zero or cut away off-axis paths.

All seven families are rebuilt: n=1,2,3 with background seeds 0 and 3, plus
the n=1 zero-complement family. They cover 28,672 complete worlds. The source
positions and finite-speed distances agree. For all 56 old-input sectors,
P is constant in the three apparatus payloads; the eight old source inputs
permute all P triples. Both (Q8,Q10,M) and (Q8,Q10,V) attain 512 distinct
triples per fixed old input. Additional direct controls verify that Q8
ignores the other two fresh payloads, Q10 ignores the other two, and M
permutes its final source conditional on its predecessors. The fixed
seven-site inverse recovers the actual P on every world.

These independent finite calculations validate the bounded source family.
They do not replace Native A's separately stated actual-L source theorem.
The old-input comparison ensemble is explicitly equal-weight over its eight
payloads; it is not adopted as a physical prior for an unknown carrier.

## 2. Every terminal pointer and complete same-site prefix

The review independently evaluates the acceptance predicate through its four
integer cases and counts every terminal triple and source-world label. It
checks all 525 terminal candidates and all 525 complete same-site prefixes,
separately on all P triples and on the prepared-shape P.A=0 sector. It retains
zero-count raw cells. For each terminal candidate and sector it exhausts all
256 Boolean readouts and compares the optimum with the grouped Bayes error.
Opposite-label raw collisions are checked directly; the published compact
payload witnesses are reproduced.

The full terminal and prefix count tables regenerate exactly the published
fingerprint in every family. The minima, best sites, exact-readout counts,
raw and prefix support ranges and individual reported collision witnesses
all agree. Every terminal and every prefix has a collision in both sectors.
A synthetic whole triple containing the actual A bit passes the identical
classification mechanism, so the all-fail verdict is not built into it.

The smallest prepared-sector terminal error is 5/32, in n=2, seed=0 at the
first deadline. The smallest prepared-sector complete-prefix error is
37/256, in the same family at the third deadline. The pooled common-terminal
readout minimum is 5/16 at all three deadlines. These are exact errors for
the fixed equal-weight native comparison ensembles. They are neither quantum
prediction errors nor universal approximation floors. Access to the prefixes
is not granted, and their public safety is not claimed.

## 3. Native interaction algebra and mutants

The zero-complement origin polynomial agrees with the fresh native evaluator
on all 4,096 original-payload worlds. A separate subset-inclusion Möbius
inversion reconstructs the A/B/D polynomials: respectively 2,11,12 monomials
of degrees 1,2,3. Its exact terms match the author output. Removing the native
B*D term changes 2,432 worlds; removing the old-local term changes 3,584.
These nonvacuous controls catch linearized propagation and a lost retained
state. The polynomial uses actual original-time source payloads.

The actual measured world table also gives a bijective change of coordinates
to (P,Q8,Q10,M). On the attained original-input sector P=(0,s,1), direct
field evaluation independently confirms

    V.A = B XOR 1,
    V.B = D,
    V.D = 1 XOR E XOR D XOR B*D XOR s*B,

where E,B,D are the respective XORs of Q8,Q10,M components. Möbius inversion
in these actual pool coordinates gives the same 19-term prepared D polynomial
and the three old-sign products s*Q8.B, s*Q10.B and s*M.B. Q8.B is the actual
prospective Y operand, rather than an arbitrarily substituted apparatus bit.

The intended acceptance ANF independently has 28 terms and degree four in
the stated seven logical coordinates. Substituting the fixed two-slice sign
identity gives 72 terms and degree four in the stated eleven-coordinate
phase basis (one coordinate is unused). Full truth reconstruction checks
both transforms. Prepared-state causal relations can cancel formal degree;
neither the author nor this review uses those degrees to decide physical
pointer impossibility. A masked native product is also not an isolated
clean Toffoli gate or permission to read its masks.

## 4. Evidence, replay and remaining work

Run `python3 checks.py --author-root <native_gate_v13>` and compare stdout
with result.json; repeat with `python3 -O`. Both executions match the retained
structured result byte for byte. Every required condition is checked through
explicit exceptions before a successful verdict can be emitted. The checker
reads the pinned author result as reference data but imports no author code.
All six input blobs are revalidated on every replay. SHA256SUMS lists the
other four curated review artifacts.

This is a separate internal review. It is not external or coordinator-
commissioned programme review, Lean/kernel certification, full-suite testing
or an exact-head CI attestation. The actual native acceptance gate, operand
storage through its latency, complete physical pointer/history law, access
closure and reusable output boundary remain open. No merge, dispatch,
F/E designation, premise adoption or full A1/A2 equivalence follows.
