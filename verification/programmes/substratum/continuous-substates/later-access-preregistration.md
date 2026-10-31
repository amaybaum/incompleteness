# Setting-conditioned later access: preregistration

Research-only preregistration on draft PR #1009, written at
`c981a006` after the native randomized port-5 setting unit
(`native-random-setting-test.md`) was accepted there. **No probe is
written or run here and no outcome is stated.** This file fixes the
compared objects, the decision rule, the controls and their checkpoints
before execution. It changes no manuscript, status, prior, access rule,
benchmark or earlier verdict, and it is not a native V3 control plane
or an `F` candidate.

## Question

The accepted unit established, under its joint product prior, that the
two values of c=R.A, with R=U_(S+4)(port5), give the same joint
record/carrier kernel in the passive window L+3 -> L+4 -> L+5. The full
outgoing environment G_(L+5)(D,eta) was not shown setting-independent.
It is not available to a private decoder, and a later interaction could
in principle use its setting/key correlations.

This test asks one bounded question: does the **only sourced later
interface** available to the embedded observer turn those environmental
correlations into a setting-dependent difference in the complete
accessible history, at the same incoming packet, through a fixed horizon?

## The sourced later interface

### What is sourced

The access declared by the retained candidate contracts is listed in
`native_vread_v15/REPORT.md` lines 62-70 (paths relative to
`verification/programmes/oi-qm/reconstruction/native-y-continuation-20261024/`):
the eight public ports' full raw triples at every tick, the old whole-q9
record at L and the single whole-V read at L+2; q10 and the previous-slice
neighbors of q9 are private. Only the first of these operates after L+5.

The port streams after L are sourced by `history_v11/REPORT.md`
(sha256 `413c9595...0fdb81`, separate-agent review accepted in
`history_v11/review/REPORT.md`):

- lines 10-21: for every 1 <= Delta <= L, the seven old raw public
  streams and the remote herald stream admit a chronological independent
  frontier bank through H=L+Delta;
- lines 34-45: ports p_0..p_7, deadlines a_i, and frontier triples
  f_i(t), reserved for a_i < t <= H;
- lines 48-49: the z port stays private under the retained convention;
- lines 126-129: the future raw-noise factor cannot be adjoined
  independently to a future carrier that already uses the same bank, and
  its joint law with every newly read response-relevant field must be
  established;
- lines 149-151: horizons beyond 2L, new ports and exposed private fields
  need new audits.

`shared_v12/INTERFACE-CONTRACT.md` (sha256 `1a0b34eb...be7633`) lines
100-111 bound the same theorem to H <= 2L and require the full public
record and outgoing carrier to be compared jointly, including raw
fields, timing, all flags and zero-mass branches. Port coordinates and
bank directions are the `PORTS` list of `native_vread_v15/checks.py`
(sha256 `93b4161f...649824`, lines 377-381).

**Candidate later interaction (LA):** the passive read of all eight
public ports' full raw triples at every tick t with L+6 <= t <= H*=2L,
together with any stop rule that is a fixed function of records already
read. H*=2L is the largest horizon whose bank geometry the sourced
theorem audits.

### Its status

The access convention is a retained candidate convention. It is
not an adopted access rule (`CURRENT-HANDOFF.md` lines 6-7). A port read
exposes the raw triple and writes nothing. That is part of the convention
and is carried as hypothesis H-access. A test result is conditional on
it, as on the other hypotheses below.

### What is absent

Checked against `native-packet-operand-and-setting.md` ("None is
compiled by the declared passive/read-stop interface"),
`native-interface-selector.md` (the next construction "must supply an
actual setting-dependent native coupling") and the access list above, no
later **active** interaction is sourced for this construction. That
means no write, actuation, reset or setting-dependent coupling after the
port-5 record. The following are not candidates:

- the whole-V read, which is at L+2 and already in the pre-cut history;
- the private z receiver (-48L,0,0), whose exposure changes the access
  contract;
- any read of q10, of a bank triple or of G, which would be a private
  read or an access change;
- a private triangular inverse of G, which is a mathematical map with no
  native implementation.

The absence of a later active interaction is recorded as a scoped finding,
conditional on the completeness of the source/readiness/access inventory.
It is not tested further here and is not a general no-go. Introducing one
is a contract change and needs its own sourcing unit (#866, #914).

## Compared objects

Keep every element of the accepted unit unchanged:

- the original preparation;
- the 42-triple key collection eta;
- the remainder D;
- the packet path K0=K_(L+3), K1, K2;
- the raw public increments deltaW1 and deltaW2 at L+4 and L+5;
- the pre-cut history W_tau, including the whole R, the stipulated V
  where present, the old q9 record, the herald record and every flag
  and timing value.

Add the tail Tail=(raw triple of port i at tick t : 0 <= i <= 7,
L+6 <= t <= H*). The tick index is part of every record. The same fixed
stop policy is applied in both settings.

**Complete joint history.** Write X=(R.B, R.D, W_tau without R, K0, K1,
K2, deltaW1, deltaW2, Tail) and A(X) for its accessible part (all
coordinates except K0, K1, K2). For c in {0,1} and each positive-mass
incoming packet k0, define the **unnormalized** setting-conditioned
measures

    mu_c(x)  = Pr(X=x | R.A=c),
    mu_c^k0  = mu_c restricted to K0=k0, with its mass retained.

No branch is renormalized and no history is dropped. Earlier terminal
branches keep their flags and masses and offer no carrier. Their public
streams continue under the convention (`history_v11/REPORT.md` line 124)
and remain in Tail. All 48 continuing and 16 terminal source contexts are
carried. Following the accepted definition review on #866, equality after
a fixed history is not used in place of equality of the history masses.

**Prior (hypothesis H-prior).** Let beta be the 8(H*-L-5) tail bank
triples f_i(t), L+6 <= t <= H*, and D' every original variable outside
(eta, beta). Require jointly

    Pr(eta=z, beta=b | D'=d) = 8^-(42+8(H*-L-5)).

It is supplied where the inherited independent-uniform complement and the
independent bank of `history_v11` are both retained. It is not inferred
from the 42-key hypothesis and the bank hypothesis separately. A correlated
prior needs a separate test, and one is used below only as a
countercontrol.

The other hypotheses are:

- **H-inventory:** the source, readiness and bank inventory shared with
  native_route_v13 is complete.
- **H-access:** the retained eight-port convention as stated above.
- **H-rule:** the unchanged native rule with H(A,B,D)=(B,D,A XOR BD).
- **H-torus:** the window lies inside the no-wrap torus, with 2H* less
  than the side 256L+64T+1.

## Decision rule (fixed before computation)

The scale is astronomical, so no history law is enumerated. The test is
decided by a written chronological-triangular proof whose every geometric
and algebraic precondition is checked exactly, with all controls green.
The rule fixes which measurements decide each token. It does not fix
their values.

1. **Preconditions (P1-P6), each measured exactly:**
   - **P1.** Each f_i(t) in beta has a unique straight own path of length
     t to p_i and reaches no other port before t.
   - **P2.** No element of beta reaches any label of the accepted 42-key
     path. That is, no element reaches R, any slice of K0, K1 or K2, or
     deltaW1 or deltaW2 by its own time.
   - **P3.** beta is disjoint from the 42 eta cells, all 1479 compiled
     sources, the 17 named exceptions and the 25 ready balls.
   - **P4.** The same-tick cross-edges are exactly 2->5 and 3->5, which
     is consistent with ordering by (t, i).
   - **P5.** H-torus holds.
   - **P6.** Every first-front step is a permutation of its own triple in
     arbitrary background, including a background that depends on the
     setting and on eta.

   For P1-P3, minimize over all t in (L+5, H*] at the endpoints and every
   absolute-value breakpoint, recomputed independently of the
   `history_v11` checker. P6 is checked on dense small native worlds.
2. **LA-EQUAL** is printed only if P1-P6 all hold and every control
   passes. Under the hypotheses, the written proof then gives
   mu_0^k0 = mu_1^k0 exactly for every positive-mass k0, and so
   TV_full(k0)=0 and TV_acc=0 as exact Fractions. Here TV_acc is the total
   variation between the pushforwards of mu_0 and mu_1 under A.
3. **LA-DIFFERENT** is printed only on an exact witness: a pair of
   positive-mass accessible histories, at the same k0 and under the
   stated hypotheses, with TV_acc > 0 computed in Fractions from a
   written derivation whose inputs are checked.
4. **LA-UNDETERMINED** is printed when a precondition fails and no exact
   witness exists. Failure of a sufficient condition is not a difference,
   and nothing is extrapolated. The output names the failing precondition
   and the first (cell, tick) at which it fails, and the test parks with
   that named gap.
5. **Informativeness flag (always reported, decides no token):**
   EMPTY if, under the same proof, Tail is independent of (eta, K0, K1,
   K2) given D'. Otherwise INFORMATIVE. An LA-EQUAL with EMPTY means the
   sourced later read carries no packet or key information at all. Its
   equality across settings then has the same cause as its emptiness, and
   it is reported in that form.

Any change to this rule, the window or the hypotheses after execution
starts is an append-only amendment, recorded before the affected run.

## What each outcome licenses

- **LA-EQUAL** closes only the LA interface, the window through H*=2L,
  this setting, this carrier and record dictionary, and the stated
  hypotheses. It does not show that G is setting-independent. It says
  nothing about a later active interaction, horizons beyond 2L, an exposed
  private field, a correlated prior, adaptive operations or other
  constructions. With EMPTY, it also does not show that any informative
  later read is setting-blind.
- **LA-DIFFERENT** makes the construction a candidate for measurement-
  context dependence only. It does not establish an operation that the
  observer can select, noncommutation, contextuality, quantum behavior or
  composability. Before any reading beyond that, it needs a source audit
  of the difference: whether it comes through R's own public fields, a
  pad failure or the packet. The difference is not a native instrument.
- **LA-UNDETERMINED** licenses only its named gap.
- No outcome changes an earlier verdict, the 42-bit benchmark, any #866
  quotient, a manuscript claim or a status label.

## Controls and countercontrols

Every control can fail and runs before any verdict text. Controls on
small worlds test the mechanism and the comparator, not the astronomical
preparation.

- **POS (supplied coupling).** In a dense small native world, a supplied
  actuator XORs c into a field on a port's path whose own bank triple is
  pinned (unpadded). The joint comparator must report TV > 0.
- **ACCESS (extra access).** The same world gives the observer an extra
  read of the port's own bank triple or of a private pre-pad field. The
  comparator must report TV > 0 where LA alone gives TV 0, as in
  `history_v11`'s extra-read control. This shows that changing access
  changes the verdict.
- **PRIOR (correlated prior).** A tail bank triple is set equal to an eta
  key, with fair marginals. The joint TV must be nonzero, and marginal
  fairness must not hide it.
- **MARG (marginal comparator).** A supplied joint-only dependence of
  Tail on (c, R.B/D, K0) with c-independent per-port, per-tick marginals.
  The joint comparator must report TV > 0, and a per-coordinate marginal
  comparator must report 0 on the same fixture. If the marginal
  comparator does not miss it, the fixture is vacuous and the run is VOID.
- **NULL.** Two identical branch laws must give TV exactly 0.
- **GEO-COUNTER.** A frontier ray moved by a fixed offset onto the
  packet's cone, and a ray placed on an eta cell, must each fail P2 or P3.
- **ORDER-COUNTER.** A reversed equal-time order must fail P4.
- **PERM-COUNTER.** A non-bijective rule H'(A,B,D)=(B,D,BD) must fail P6.
- **STOP.** On the small world, the law under each enumerated fixed stop
  rule must be the pushforward of the full-window law, with TV no larger
  than the full-window TV.
- **BRANCH.** 48 continuing and 16 terminal contexts, with unnormalized
  masses retained.

## Invariant -> checkpoint table (§A.41)

| Invariant asserted | Checkpoint |
| --- | --- |
| Pinned inputs unchanged (`native_vread_v15/checks.py`, `shared_v12/INTERFACE-CONTRACT.md`, `history_v11/REPORT.md`, `parallel_v3/history_control/SOURCE-GEOMETRY.json`, `native_random_setting_probe.py` at sha256 `1609a902...0753b`) | CP-PIN: sha256 equality, else VOID |
| Native rule unchanged and nonlinear | CP-RULE: h equals the pinned rule on all 8 codes |
| P1 own paths, no early other-port arrival | CP-GEO-OWN: exact breakpoint minimization, all 8 rays over the full window |
| P2 beta excluded from the 42-key path | CP-GEO-EXCL: same method against every label cell and time |
| P3 disjointness | CP-GEO-DISJ: exact affine-ray intersection against eta, sources, exceptions, balls |
| P4 order | CP-ORDER: all equal-time cross-edges enumerated |
| P5 no wrap | CP-TORUS: integer comparison 2H* < side |
| P6 diagonal permutations | CP-PERM: dense small worlds, setting- and key-dependent backgrounds |
| Comparator detects coupling | CP-POS: TV > 0 |
| Access change detected | CP-ACCESS: TV > 0 with extra read, 0 without |
| Correlated prior detected | CP-PRIOR: joint TV > 0 with fair marginals |
| Marginal comparator misses joint-only difference | CP-MARG: joint > 0, marginal = 0 |
| Comparator not trivially positive | CP-NULL: TV = 0 |
| Geometry check can fail | CP-GEO-COUNTER, CP-ORDER-COUNTER, CP-PERM-COUNTER |
| Stop policies add nothing | CP-STOP |
| Pre-cut factor equal across c (use-cut independence re-measured, not assumed) | CP-PRECUT: the law of (R.B, R.D, K0, other pre-cut records) is checked as a function of c on the fixture, and the geometry of R's exclusion from K0 is re-checked |
| All branches retained, no renormalization | CP-BRANCH: 64 contexts, masses carried |
| Exact arithmetic only | CP-EXACT: every measured quantity is int or Fraction; a float anywhere is VOID |
| Replay | CP-REPLAY: normal and `-O` structured outputs byte-identical; controls use explicit checks, never `assert` |
| Verdict over green controls only | CP-GATE: token generated from measurements after all controls; otherwise VOID, exit 2 |
| Mutations caught | CP-MUT (below) |
| Informativeness reported | CP-INFO |

## Mutation targets

Each mutant must exit 2 with VOID naming its control, in both modes. The
targets are:

- drop R.B/D from X;
- replace the joint comparator by the marginal one;
- pin one frontier triple;
- shift one ray onto the packet cone;
- truncate the minimization to sampled ticks, using a breakpoint fixture
  that only the breakpoint method detects;
- reverse the equal-time order;
- substitute the non-bijective rule;
- omit the terminal contexts;
- renormalize branch masses;
- introduce a float;
- expose an extra field without flagging an access change;
- compute the token before the controls.

## Execution, evidence and limits

A later execution commit adds `native_later_access_probe.py` (standard
library, exact integers), its structured JSON output and a result note.
It runs from the repository root:

    python3 -I -B verification/programmes/substratum/continuous-substates/native_later_access_probe.py
    python3 -I -O -B verification/programmes/substratum/continuous-substates/native_later_access_probe.py

The verdict reads the exit status and the JSON fields (controls,
measurements, token, informativeness), never log text (§A.44). The
expected output is committed beside the probe (§A.42). The run is bounded,
local and seconds-scale. No large enumeration, Lean build or special
workflow is used, and no dispatch, `F`/`E` designation or merge is
requested (§A.43 item 4).

The result is exact algebra plus a conditional paper proof, under H-prior,
H-inventory, H-access, H-rule and H-torus. It is not Lean certification,
an operational QM result or a native instrument. PR #1009 remains draft
and unmerged.
