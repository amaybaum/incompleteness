# A native local fresh pool and the precise remaining X-predicate gate

Research checkpoint. Author review pending. The native source is the reviewed
one-tick boundary lemma in native_v11, revised on #910 at
`7ec3f8234a148cadb58ebc6c8212b3b0233acabe`. Its constructive consequence is an
actual local six-bit fresh pool at phase L+1. A separate exact calculation
shows that this pool has enough randomness for the full supplied post-X
carrier law. The acceptance predicate used in that calculation is abstract;
it is not a native flag or implemented measurement instrument.

## 1. Physical conditional resource

Supply independent uniform current triples at the two original-time sites

    f8=(-(L+1),S,76), f10=(-(L+1),S,78),

independent of all other initial variables. These are outside the existing
ready balls, source programs and reserved banks. Native_v11 proves that their
unique axial responses at q8=(0,S,76) and q10=(0,S,78), time L+1, are separate
permutations in their initial triples for every fixed dense background.
Consequently Q8=U_(L+1)(q8) and Q10=U_(L+1)(q10) are jointly uniform over64
pairs conditional on every other initial variable. This is stronger than
separate fair output marginals, and no fresh data are inserted after time0.

Previous q9 at this phase is the actual whole native q9 triple at L. On a
valid prepared post-Y branch it is (0,s,r_old), with s the designated X
outcome. Thus retained X and a local fresh pool coexist in one native
second-order phase. This does not provide an observer operation on previous
fields or an adapter that can already use s in a new gate.

The two initial cells cannot reach any specified old/new public receiver
until L+77 and L+79 respectively. In particular the public history through
L+1 depends only on the remaining initial variables, so the pool is jointly
independent of it under the stated initial factorization. This does not
automatically hold after an arbitrary computation delay. The pool may depend
on old bank variables through its background; later public records may also
depend on the witness seeds. Separate marginal uniformity of the pool and
noise would not establish their required joint law.

## 2. Fixed decoder and abstract predicate

Write current Q8=(b0,b1,b2), Q10=(b3,b4,b5). At this fixed phase define

    Xnew = previous q9.B = s,
    Ynew = b1, Rnew = b5, Znew = b4,
    K = b0 + 2*b2 + 4*b3.

This coordinate map is fixed across histories. All other actual fields,
including the full previous q9, previous old Z/herald and the unused pool
coordinates, remain physical workspace. No history-selected decoding,
discarding of source information or cold late-time phase is used.

Let a=Ynew XOR s and b=Rnew XOR s. Define the **abstract** flag A by
K<n(a,b), with

| a,b | 00 | 01 | 10 | 11 |
| --- | --- | --- | --- | --- |
| n(a,b) | 5 | 0 | 4 | 1 |

Because the six pool bits are jointly uniform conditional on the complete
old initial state, there are20 accepted and44 rejected pairs per s. Thus

    Pr(A=1 | old state/history)=5/16,
    Pr(A=0 | old state/history)=11/16.

Conditional on A=1, the masks (Ynew XOR s,Rnew XOR s) have probabilities
5/10,4/10,1/10 on00,10,11. Znew is jointly independent and fair. This is
exactly the supplied six-state post-X law mu_X,s, including its support;
matching only X/Y/Z/R expectation values would not establish that claim.

The raw pool cells are private inputs in this abstract comparison. Treating
A as a reference outcome does not authorize reading only one field of a
native public port or suppressing its other exposed metadata. A physical
implementation must specify and check every actual public raw field.

## 3. Joint law with the retained old raw record and failures

For each valid offered-carrier incoming history D and its earlier Y result y,
the actual whole-q9 X-terminal record h=(0,s,r_old), conditional on the old
Y-preparation success, has the retained three-point law:

    (s,r_old)=(y,y),(1-y,y),(1-y,1-y),
    probabilities 1/2,3/10,1/5.

The exact assembly checks, for every such whole record h,

    Pr(h,A=1,j_new | D,old G=1)
        = Pr(h | D,old G=1) * (5/16) * mu_X,s(j_new),
    Pr(h,A=0,offered=none | D,old G=1)
        = Pr(h | D,old G=1) * (11/16).

Both old raw fields are retained; old r_old is neither discarded from the
record nor reused as a fresh reset variable. This supplies a finite full-law
target for an eventual native gate, inheriting the stipulated whole-q9 X
terminal read from phase_joint_v10. A is not yet a physical herald.

Before conditioning on the old Y-preparation flag, the finite probabilities
for valid incoming offered histories are:

| Branch | Probability |
| --- | --- |
| old G=1, A=1 | 25/256 |
| old G=1, A=0 | 55/256 |
| old G=0, offered=none regardless of A | 11/16 |

All65536 old/new finite worlds are retained across16 old input/history rows.
Each row has400 successes,880 new failures after old success, and2816 old
terminal failures among4096 worlds. Rejected selected physical measures keep
the actual previous q9, previous old Z and old herald triples, and both
current pool triples. No quantum failure state replaces them. Earlier
terminal flags continue to forbid offering a carrier. Omitting that
condition would falsely offer on55/256 of runs.

## 4. Decisive controls

All controls pass before the verdict:

- Swapping the4:1 plane weights retains the5/16 rate but changes the whole
  conditional target measure by TV3/10.
- Accepting a forbidden01 plane changes success to11/32 and introduces an
  excluded carrier code.
- Using stale prior Y instead of actual s gives TV4/5 whenever s differs
  from that Y.
- Reusing the already public old R produces TV1/10 or9/10, depending on
  whether it equals s.
- Setting new Z equal to Ynew XOR s leaves its marginal fair but changes
  the joint carrier law by TV1/2.
- Resurrecting after old G=0 has false-offer mass55/256.

The checker imports no author engine. It reconstructs the retained native
old controller table and the actual2684-step old herald truth word from
pinned source data, then performs exact-count assembly. Normal and optimized
replays are byte-identical. Source and result hashes are retained.

## 5. Remaining native construction

The new initial resource is specified, and its native conditional freshness
is proved. The precise outstanding task is to deliver **actual** previous-q9
X to a native predicate gate that consumes the actual Q8/Q10 pool, preserving
the calibrated joint carrier/public-record law through its computation and
producing a natively usable next boundary. The predicate depends on unknown
X, so it cannot simply be precomputed into an initial source. A new compiler
word in a cold isolated register would not establish this adapter.

Old-X delivery, a native whole-record flag, any additional delay/history
audit, access closure, native back-action/reuse, arbitrary menu/depth, full
A1 coverage, A2 error guarantees and composites remain open. This checkpoint
identifies a useful actual resource and an exact local target for that
missing gate; it does not close the reusable-instrument obligation.

Replay: `python3 checks.py --source-root <retained-native-root>
--native-author-root <native_v11>` must equal result.json; repeat with `-O`.
