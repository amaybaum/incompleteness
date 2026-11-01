# Separate internal review: logical acceptance and whole-pointer law

24 October 2026. **ACCEPT WITHIN STATED SCOPE. No blockers.**

Reviewed author: `1cb224db6c17e083849a0f82768e991beac39399`, #912,
`verification/programmes/oi-qm/reconstruction/composition-access-20261024/composition_flag_v6/`.
All six curated Git blobs were fetched at that immutable commit and match
the local candidate byte for byte. INPUT-HASHES.json retains their Git object
identities and SHA-256 digests. This is a separate-agent internal review,
not external certification or the programme's commissioned proof review.

The accepted result is an explicit supplied-gate reversible implementation
of the intended acceptance predicate, with input/workspace restoration and
an exact complete logical pointer/carrier law. Native gate compilation,
operand preservation during native latency, the physical pointer channel,
private-access isolation and the clock remain unproved supplied conditions.
The actual native acceptance gate remains open. #885 is read-only.

## Independent derivation and engine

The review checker imports no author module and executes no author code.
It rebuilds the gate program with a different wire ordering, represents
each gate as a tuple of Boolean control locations and a target, and applies
the controlled XOR directly to a Boolean array. The Native A conditional
kernel is independently evaluated with scalar triple XOR and

    H(A,B,D)=(B,D,A XOR(B AND D)).

The enormous-L independence/source geometry is inherited from the pinned
Native A theorem; this review verifies its stated finite conditional law,
not astronomical evolution or the full preparation proof.

For a=Y XOR s, b=R XOR s and K in{0,...,7}, the threshold partition is
independently obtained by listing its accepted integers:

- b=0 and K in{0,1,2,3};
- a=b=0 and K=4;
- a=b=1 and K=0.

These sets are disjoint and recover thresholds5,0,4,1 on masks00,01,10,11.
The elementary circuit realizes their XOR. Seven CNOTs collect the actual
seven-wire parity s; four collect a,b. Paired NOTs implement negative
controls. Each five-control term uses a three-Toffoli conjunction ladder,
one target Toffoli, and the reversed ladder. Independent truth rows detect
an omitted first ladder gate on16 assignments.

Forward computation therefore has44 gates:11 CNOT,18 NOT and15 Toffoli.
One flag copy and the reversed computation give89 gates:23 CNOT,36 NOT,
30 Toffoli. The31 wires are21 incoming phase bits, seven clean temporary
bits and a three-bit pointer. Its B field is initially clean; its A/D fields
are two independently preloaded fair bits in this specified reference.
All1,024 relevant input assignments and all four pointer-pad pairs are
executed, giving4,096 complete truth/prefix/restoration controls.
Irrelevant phase bits are varied as well and do not enter the predicate.

## Global inverse and final boundary

Each elementary gate is an involution on its entire register space:
its target is distinct from every control, so applying it does not change
its own control condition. Consequently reversing the full gate list is a
global inverse, including dirty temporary bits and a dirty flag/pointer.
Clean initialization is needed for the specified acceptance function, but
not for invertibility. The checker tests every local truth assignment of
each primitive and512 independent deterministic dirty full-register states.

On the ready subspace, every phase bit and all seven clean temporary bits
return exactly to their input values, and only pointer B acquires A. The
pointer pads never enter a gate control or target. Its whole prefix is
therefore constant(q_A,0,q_D) through tick44 and constant(q_A,A,q_D) from
tick45 through89. Both flag values and every padding pair are retained.
Restoration of logical wires is not restoration of an evolving native
lattice phase after the same number of ticks.

The optional explicit record bank adds270 clean bits and270 CNOTs. The
independent expansion reproduces301 total wires,359 gates and flag-copy
tick180. It stores each of the90 core raw samples and retains the complete
360-sample observed prefix during record copying; added ticks repeat the
same known pointer values. All256 ready record-bank cases and64 dirty
301-wire inverse cases pass. This is an explicit upper bound with a
supplied schedule, not a minimality or autonomous-clock theorem.

## Complete conditional source, pointer and outgoing law

For each fixed old triple p and complementary neighbor XOR c, enumerate
all512 equally likely Q8,Q10,M values. Set

    V=p XOR H(Q8 XOR Q10 XOR M XOR c).

The decoded seven-site parity recovers p.B on every source world. The
independent engine checks32,768 worlds and131,072 explicit padding worlds,
conditioning on p and c rather than averaging them away. It checks every
complete pointer prefix jointly with V, the new flag and the selected
X,Y,R,Z coordinates, including65,536 target cells and every zero cell.
The phase-kernel digest independently matches the author:

    65e0e1dab316ef79e64ffa1369402c8d66f8de9585045dd4d5b1d5cbf9940c27.

For each V and pad pair, the20 accepted counts have weights5,4,1 on the
three allowed masks with independently fair Z. Every one of1,024 valid
accepted full-record posteriors has the stipulated positive X-eigenstate
decoder with determinant zero. The16,384 nonzero rejected selected cells
remain actual failed fields. No artificial qubit failure state replaces
them. The96 valid old-flag/context cases preserve earlier terminal failures:
the physical flag still has a law, but no outgoing carrier is offered.
Omitting that interface guard would offer40,960 padded terminal-source
worlds, a nonvacuous control of the guard's role.

The individual three complementary neighbors are not assumed mutually
independent. Their relevant parity is part of fixed c. All their unused
fields are preserved. The whole Boolean truth check includes the three D
bits separately, so the representative(c,0,0) source enumeration does not
conceal additional gate dependence on their decomposition.

## Independent access, reuse and delay controls

- Exposing the private M key gives1,024 negative accepted posteriors.
  The minimum determinant is-1/18, including the reported
  p=000,c=000,V=001,M=000 witness. This concerns the stipulated decoder
  and enlarged access contract, not every possible encoding.
- Exposing the temporary a fixes both X and Y on acceptance and gives
  determinant-1/4. Later uncomputation cannot remove a public prefix.
- Omitting uncomputation leaves workspace dirty in31,232 source worlds.
  Idle padding can preserve the pointer prefix while violating this
  candidate's clean final-workspace boundary. Other retained-garbage
  constructions would need a separately stated future coupling contract.
- An unrelated flag with the same5/16 rate gives complete offered-carrier
  TV error1/8 for either sign. Tensoring independent V/pads and mapping
  the flag to the full fixed prefix preserves this discrepancy.
- Reused unused pad pairs differ by TV3/4 from the chosen independent-noise
  reference across two stages. The pads remain carrier independent;
  correlated public noise can be declared separately. This is not a
  universal quantum-instrument failure or a universal fresh-padding bound.
- A separately written4,096-world bit-sliced evaluator evolves every
  affected site of the full six-neighbor second-order lattice for three
  ticks, retaining off-axis fields. The original two-tick phase inverse
  works. Applying the unchanged code one tick later changes the old sign
  in2,048 worlds and the selected pool in3,584. This is the scoped small
  original-time source control, not actual-L delay evidence or a general
  storage impossibility.

The hypothetical serial identification of one logical gate with one native
tick would finish the core at L+91 and the explicit recording variant at
L+361. The earlier source causal exclusions end at L+77/L+79, so those
exclusions alone do not certify the longer physical history. Native routing
and timing have not been constructed. Causal reach of a receiver is not
proof of leakage; a later full joint mask/history/carrier audit is needed.

## Verdict and limits

The Boolean implementation, global inverse, exact resources, initialized
boundary, whole logical prefix and complete conditional record/carrier
law are supported. The countercontrols are nonvacuous and their negative
claims have the appropriate narrow scope. No correction is required.

Normal and optimized independent checker outputs reproduce result.json
byte for byte; Python compilation and SHA256SUMS verification pass. The
five retained review files are REPORT.md, checks.py, result.json,
INPUT-HASHES.json and SHA256SUMS. Mathematical general proofs, bounded
exact computation, source inheritance and native availability remain
separate evidence layers. No access or physical premise is adopted;
no full A1/A2 equivalence, Lean/exact-head attestation, dispatch,
F/E designation, merge or #885 mutation follows.
