# An explicit reversible acceptance circuit and its full pointer law

Research checkpoint, 24 October 2026, under #912. The plan was published
before computation at `b355f81e550c7c6328837c5423bfe2d903b2a008`.

**An explicit logical reversible circuit computes the intended acceptance
bit, restores its temporary workspace and incoming phase, and has the
correct complete raw-pointer/outgoing-carrier law under the Native A source
contract.** It uses 89 elementary NOT/CNOT/Toffoli ticks, seven clean temporary
bits, one clean flag bit and two independently preloaded fair pointer-padding
bits. All old information is retained.

This is a gate-level positive control and a concrete compiler target. The
fixed native lattice has not been shown to supply its gates, isolation,
operand storage or clock. Restoring logical input registers after 89 logical
ticks is not proof of restoring an actual lattice boundary after a native
delay. The native physical acceptance gate remains OPEN.

## 1. Exact inputs and conditional source assumptions

The existing phase consists of current q9 triple V and its six previous
neighbors. There are 21 phase bits; no unknown input is copied into a
preloaded register. The previous Q8 and Q10 fields are

    Q8=(b0,b1,b2), Q10=(b3,b4,b5).

Let M be the negative-x neighbor and let c be the XOR of the other three
neighbors. On Native A's original-time F8/F10/F9 source family, conditional
on its original complementary initial variables eta, excluding the three
source triples and the separately supplied new pointer-padding bits,

    oldP=p, c are fixed,
    (Q8,Q10,M) is uniform on 512 values,
    V=p XOR H(Q8 XOR Q10 XOR M XOR c).

The actual-L source geometry and conditional independence theorem are
inherited from Native A author
`f24a57a7c23cc1818c04265cec7604f8bc2f410d`. This checkpoint does not reprove
that large-scale source theorem or simulate astronomical time L. Its exact
kernel enumerates the stated conditional phase law for every p and c.
The individual three complementary neighbors enter this circuit only through
the XOR of their D bits, so representative values (c,0,0) exhaust their
relevant parity; their other bits are preserved without being read.

The fixed phase map is

    s=V.B XOR XOR(previous neighbor.D),
    Y=b1, R=b5, Z=b4, K=b0+2*b2+4*b3,
    a=Y XOR s, b=R XOR s,
    A=[K<n(a,b)], n(00,01,10,11)=(5,0,4,1).

On the stipulated successful old phase p=(0,s,r_old), this is the actual
retained X sign. It is a fixed current/previous coordinate computation;
it reads no unavailable historical field. Its physical gate availability
is a separate question.

## 2. Gate list, inverses and exact resource count

Write k0,k1,k2 for the binary digits of K. The predicate has the disjoint
Boolean partition

    A=(not b and not k2)
      XOR (not a and not b and k2 and not k1 and not k0)
      XOR (a and b and not k2 and not k1 and not k0).

The first term accepts K=0,1,2,3 when b=0. The second adds K=4 only when
(a,b)=(0,0). The third adds K=0 only when (a,b)=(1,1). The supports do not
overlap. These three cases independently recover the threshold table.

Seven CNOTs compute s into a clean temporary bit. Four more compute a and b
into two other clean bits. One two-control term and two five-control terms
XOR the predicate into a clean temporary f. A five-control NOT is explicitly
decomposed into three scratch-producing Toffolis, one target Toffoli and
three reversing Toffolis. Negative controls use paired NOTs. Thus computing
s,a,b,f takes 44 elementary gates: 11 CNOT, 18 NOT and 15 Toffoli.

One CNOT copies f into the initially zero public flag B. Reverse all 44
computation gates afterward. The final transformation on initialized
workspace is

    (phase,0^7,pad_A,0,pad_D)
      -> (phase,0^7,pad_A,A(phase),pad_D).

The 31 core register bits comprise the 21 existing phase bits, seven clean
workspace bits and a three-bit pointer. The pointer needs one clean B bit
and two independently preloaded fair A/D bits in this chosen record contract.
Core circuit cost is exactly 89 elementary logical ticks: 30 Toffoli,
36 NOT and 23 CNOT. No deletion or reset of old phase information occurs.
Every elementary gate is an involution on its full register space; reversing
the list is consequently a global inverse even on arbitrary dirty temporary
and pointer states. The desired function itself requires the listed clean
initialization. A dirty B would contain its original value XOR A.

The stated gate count assumes logical wire access and scheduled gates.
It includes no native routing, native H compilation, latency conversion,
causal isolation or giant-time initialization cost. It is not a minimality
result. If all 90 logical raw samples must be retained in explicit registers,
a simple recording dilation supplies 270 additional initially clean bits,
three per sample, and copies each whole pointer triple using three CNOTs.
It retains every record and is globally reversible. This optional upper bound
has 301 total register bits and 359 elementary ticks: 293 CNOT, 36 NOT and
30 Toffoli. The complete pointer prefix during these recording gates has
360 samples and changes B at tick 180. Every added tick merely repeats the
same stated raw pointer value. The checker verifies the stored bank, the
longer complete prefix and its inverse on 256 initialized controls. No
minimal record-memory bound or autonomous clock is claimed. A fixed gate
schedule is supplied for both variants. The external public record is not
silently counted as zero-cost physical storage. In particular, the two random unused pointer fields are a chosen
reference law; deterministic fixed unused fields can be harmless under a
different declared raw-record contract.

## 3. Whole raw pointer prefix, timing and every failure

The candidate public channel reads the *whole* pointer triple initially and
after every elementary gate, giving 90 samples at fixed ticks 0 through 89.
Only its B wire is a gate target, once, at tick 45. With q_A,q_D the two
initial pads, the full history is exactly

    (q_A,0,q_D), ticks 0..44;
    (q_A,A,q_D), ticks 45..89.

Every gate executes on every branch. There is no outcome-dependent runtime,
retry count or early stop. Internal s,a,b,f, scratch wires and phase/pool
wires are not extra public channels under this candidate access contract.
They remain physical inputs/workspace, not erased or declared nonexistent.
This logical pointer prefix is checked directly; finite-speed independence
of newly arriving sources is not used to infer safety of an actual native
pointer or q9 prefix. Old eta-dependent fields could leak in a later native
implementation and need their own proof.

For fixed eta, the bijection M -> V makes V uniform independently of Q8,Q10.
For any fixed s, Y,R,Z combination, exactly n(Y XOR s,R XOR s) of the eight
K values pass. Therefore for each v, each pad pair q, each selected j and
each f in {0,1},

    Pr(V=v, complete_history=T(f,q), A=f, J=j | eta)
      = count_f(s,j)/2048,

where count_1(s,j)=n(j.Y XOR s,j.R XOR s) if j.X=s and is zero otherwise;
count_0 is 8-n on that same sector. Both success and rejected physical
fields are retained. Summing gives success 5/16 and failure 11/16. On every
accepted complete record the carrier has the full 5:4:1 post-X mask law
with jointly fair Z. Its stipulated XYZ moment decoder is the positive
X-eigenstate, determinant zero. No conditional carrier is assigned to a
zero-mass success cell.

The reference includes the old whole-q9 record p and the allowed single
whole-V record. Conditioning on eta is stronger than conditioning on the
old permitted history, so the same identity survives its allowed mixtures.
On an earlier terminal failure the circuit still has an actual pointer and
physical phase, but no carrier is offered for either new flag value.
Only the stipulated p.A=0 old-success sector is used for positive quantum
offers; arbitrary old triples are retained for old-failure accounting.

This proves a conditional logical record/state law for this stage. It does
not construct a new unrestricted measurement, a native R read, a complete
access closure theorem or an arbitrary-depth reusable native boundary.

## 4. Load-bearing access, initialization and delay controls

Several countercontrols identify the exact remaining obligations.

- **Extra private-key access:** augmenting the record with the whole M triple
  creates 1,024 negative accepted posteriors across the tested valid fixed
  old/complement sectors. The minimum decoder determinant is -1/18; one
  witness has p=000,c=000,V=001,M=000. This is a conditional code/access
  witness, not a claim that every possible physical preparation or alternative
  decoder fails whenever M is exposed.
- **Workspace-prefix access:** exposing the temporary a=Y XOR s after forward
  computation fixes Y on the accepted branch. X is also fixed, so the
  stipulated decoder determinant is -1/4. Returning a to zero later does
  not undo that public record. Thus final pointer padding cannot justify
  workspace isolation.
- **Omitted uncomputation:** the seven-bit workspace is dirty in 31,232 of
  32,768 conditional phase worlds if the reverse gates are omitted. Padding
  the omitted gates with idle ticks leaves the public pointer prefix correct,
  but fails this candidate's final clean-workspace boundary. No claim is made
  that every construction must return all workspace to zero; retained garbage
  requires its own later coupling/access and resource contract.
- **Wrong flag with the right rate:** an unrelated four-fair-bit flag with
  success probability 5/16 gives complete flag/offered-carrier TV error 1/8
  for both s values. Tensoring the independent V and pad fields and mapping
  the flag to its full fixed pointer prefix preserves that error.
- **Reusing the unused pads:** fresh independent pad pairs across two operations
  have 16 equally likely pair records; reusing one pair gives four diagonal
  records. Their full-record TV difference is 3/4. This is failure of the
  declared independent-noise reference only. The repeated pads remain
  independent of the carrier, and a separately declared correlated public
  noise convention can be admissible. No universal quantum-instrument failure
  or universal need for fresh padding is inferred.
- **Uncontrolled native delay:** the independent sparse evaluator evolves the
  retained two-tick original-time source control by one additional *full*
  native tick, preserving all off-axis fields. Reusing the same seven-site
  decoder afterward gives the wrong old X sign in 2,048 of 4,096 source
  worlds; its selected pool changes in 3,584. At the third cut the unchanged
  formula recovers the field from the immediately earlier inverse slice,
  rather than the original old field. This is a scaled countercontrol, not
  an actual-L delay calculation or a general storage no-go. It demonstrates
  why logical input restoration cannot certify native operand preservation.

Even an optimistic serial alignment of one core elementary gate with one
native tick, beginning at phase L+2, would finish at L+91. F8 can first
reach an old public receiver at L+77; F10/F9 can first arrive at L+79.
The earlier unchanged-prefix finite-speed argument therefore does not cover
this duration. Under that same hypothetical alignment, the explicitly recorded
359-tick dilation finishes at L+361 and needs a longer audit. Neither is an
established native runtime or a lower bound on every possible parallel
compiler. Reaching a receiver cone is not proof of a leak: masks could still
protect the complete joint law. The required proof must check those later
old public histories jointly with the preserved carrier and the new pointer;
the earlier history-noise theorem does not supply that carrier independence.

These failures do not change the positive logical circuit theorem. They
prevent that theorem from being promoted into a native availability result.

## 5. Evidence and next gate

The standalone checker imports no author engine. It exhausts all 1,024
assignments of the ten relevant phase bits, compares them with an independent
integer threshold test, and verifies phase/workspace restoration and the
whole pointer prefix. It separately checks 72 multiple-control truth rows,
520 dirty inverse rows, 4,129 full-register inverse controls and 128 explicitly
padded traces. A broken decomposition changes 16 controlled rows.

The complete conditional kernel checks 32,768 phase worlds, 131,072 padded
worlds and 65,536 selected cells including zeros. All 1,024 valid accepted
whole-record posteriors have the correct positive X-state decoder; all
16,384 nonzero rejected selected cells remain. The 96 valid old-flag/context
cases retain terminal guards. The general bijection/kernel proof above is
distinct from these exhaustive bounded controls and from the inherited
actual-L source theorem.

Run `python3 checks.py` and `python3 -O checks.py`; stdout is byte-identical
to result.json. The result is structured and successful only after every
required control passes. PROVENANCE.json pins source snapshots and hashes;
SHA256SUMS lists the other five curated artifacts. No raw logs, independent-review
claim or full-suite/Lean/exact-head attestation is supplied by this author
checkpoint.

The next native task is explicit: realize this or a cheaper equivalent
predicate while delivering the actual distributed operands, preserving a
suitable carrier through native latency, and proving the complete physical
pointer/prefix law against all coupled workspace. The chosen logical pointer
channel and isolation are supplied conditions awaiting that bridge. No
operational-map or access-rule adoption, F/E designation, special dispatch,
merge, full A1/A2 equivalence or OI-wide no-go follows.
