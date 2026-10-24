# Composition and access: current research handoff

24 October 2026. #912 now retains an explicit logical acceptance circuit
and its complete raw-pointer/outgoing-state law. Author
`1cb224db6c17e083849a0f82768e991beac39399` is under `composition_flag_v6/`,
with separate-engine internal review retained beside it. This is a conditional
compiler target, not an implemented native gate, adopted observer access or
full quantum instrument. #885 remains read-only.

## What is constructed

The inputs are actual21 phase wires: current V and six previous native
neighbors, including Q8/Q10. The fixed local inverse supplies s. The circuit
computes A=[K<n(Y XOR s,R XOR s)] for thresholds(5,0,4,1) with NOT/CNOT/
Toffoli gates, copies A into the public flag B, then uncomputes temporary
wires. Every phase bit and all seven clean temporary bits are restored.

The core has 89 logical ticks:30 Toffoli,36 NOT,23 CNOT. Its31 register bits
include the existing21, seven clean temporaries, one clean flag and two
initially fair unused pointer fields. This chosen three-field public channel
is read at every tick. Its complete90-sample prefix is (padA,0,padD) through
tick44 and (padA,A,padD) from tick45. All branches have the same schedule.

An optional explicit90-sample record-bank dilation uses 270 additional clean
bits and 270 copying CNOTs:301 total register bits,359 logical ticks and a
360-sample whole-pointer prefix. The added copies retain, rather than erase,
the public record. These are explicit upper bounds, not minimal costs or
native/autonomous clock implementations.

## Conditional complete law

Native A's inherited initial-source theorem makes(Q8,Q10,M) uniform on 512
values conditional on the remaining initial variables. OldP=p and the XOR
of the other three neighbors are then fixed; V=p XOR H(sum neighbors).
The circuit's full raw pointer history, V, old record and selected carrier
are checked jointly, with all rejected physical fields, zero cells and
parent terminal guards. Every accepted whole-record posterior has the
correct5:4:1 post-X mask law, fair Z and positive X-state decoder.

The checker exhausts32768 conditional phase worlds,131072 padded worlds,
65536 selected cells and 1024 valid accepted raw-record posteriors. Gate
truth tables, arbitrary-dirty global inverses, optional recording and a
separate threshold/kernel engine are additional controls. Written bijection
and conditional-kernel proofs remain separate from bounded enumeration and
the inherited actual-scale source theorem.

## What the circuit still assumes

Logical phase storage, scheduled gates, pointer coupling, fixed clock and
workspace isolation are supplied. The evolving native field has not been
shown to implement them. Native masks and garbage are real physical state;
uncomputing them later does not remove an earlier public leak.

Actual countercontrols show that revealing private M/key fields gives
negative fixed-decoder posteriors (minimum determinant-1/18); revealing
temporary a gives determinant-1/4. Omitting uncomputation fails this chosen
clean-workspace boundary. A flag with the right rate but independent of the
pool has complete offered-carrier error1/8. Reusing unused pads gives TV3/4
against the chosen independent-noise reference only; a separately specified
correlated public-noise convention can remain admissible.

A small original-time native one-tick control changes the old-sign and pool
code if the same phase formula is reused after uncontrolled evolution.
Logical input restoration therefore proves no native storage theorem.
Even a hypothetical serial one-gate/native-tick core from L+2 finishes
L+91, after F8's first old-receiver arrival at L+77 and F10/F9 at L+79.
The optional recorded dilation would finish L+361. Neither timing is an
established native runtime or a lower bound for a parallel compiler.
The earlier unchanged-prefix causal argument does not cover these delays;
a new joint public-history/carrier proof is required. Cone arrival alone
does not prove leakage because masking may protect the joint law.

## Related work and next gate

The preceding `native-coupling-v5/` conditional law and wrong-flag controls
remain unchanged. #910 adds a small-family native nonlinear-product witness
and an actual-scale second-front source result: common raw X response pairs
are restored, but no jointly affine source controller selects a common raw
binary code. Distributed/richer encodings remain open. #911 adds a reviewed
finite-menu approximation and a scoped fixed-vector reset-reuse failure;
neither supplies native gates or access closure.

The next gate is native compilation or a cheaper native predicate with
actual operand delivery, preserved/re-encoded carrier, full pointer metadata
and complete delayed history. General instruments, composites/Bell and full
A1/A2 reconstruction remain in #913. Author and review replay normally and
with -O; no full-suite, Lean or exact-head attestation, premise/access adoption,
F/E designation, dispatch, merge or equivalence verdict follows.
