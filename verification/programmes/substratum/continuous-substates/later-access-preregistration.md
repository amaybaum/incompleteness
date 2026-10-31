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
public ports' full raw triples at every tick t with L+6 <= t <= H*=2L.
A stop rule may end the read early. It is a fixed function of the prefix
of the accessible history A(X), defined below, read so far, and never of
R.A. H*=2L is the largest horizon whose bank geometry the sourced
theorem audits.

### Its status

The access convention is a retained candidate convention. It is
not an adopted access rule (`CURRENT-HANDOFF.md` lines 6-7). It is
carried as hypothesis H-access, together with the stipulation that a port
read exposes the raw triple and writes nothing. The cited sources do not
state that stipulation explicitly, so it enters only as part of H-access.
A test result is conditional on it, as on the other hypotheses below.

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
stop policy, a function of A(X)-prefixes only, is applied in both settings.

**Complete joint history.** Write X=(R.B, R.D, W_tau without R, K0, K1,
K2, deltaW1, deltaW2, Tail) and A(X) for its accessible part (all
coordinates except K0, K1, K2). A(X) does not contain R.A. Let k0 range
over the incoming-packet values together with k0=⊥, the value taken in
the 16 terminal source contexts, which offer no carrier. For c in {0,1}
and each k0, define the **unnormalized** setting-conditioned measures

    mu_c(x)  = Pr(X=x | R.A=c),
    mu_c^k0  = mu_c restricted to K0=k0, with its mass retained,

and, with TV(mu,nu) = 1/2 sum_x |mu(x)-nu(x)| on unnormalized measures,

    TV_win(k0) = TV(mu_0^k0, mu_1^k0),
    TV_acc(k0) = TV(A_* mu_0^k0, A_* mu_1^k0),

where A_* is the pushforward under A, so TV_acc(k0) <= TV_win(k0).

No branch is renormalized and no history is dropped. Earlier terminal
branches keep their flags and masses and offer no carrier. The tail law of
`history_v11/REPORT.md` lines 116-124 is stated conditional on any
nonzero-probability past, terminal records included, so their public
streams are in Tail. All 48 continuing and 16 terminal source contexts are
carried. Following the accepted definition review on #866, equality after
a fixed history is not used in place of equality of the history masses.

X is the window object. No carrier is offered after K2, and X excludes the
outgoing environment at H* (G_(H*)), which `shared_v12/INTERFACE-CONTRACT.md`
line 107 would compare jointly with the public record. TV_win therefore
says nothing about G_(H*).

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
  than the side 256L+64T+1 and every source, ready, target and record
  coordinate span less than half the side (`history_v11/REPORT.md` lines
  87-89).

## Decision rule (fixed before computation)

The scale is astronomical, so no history law is enumerated. The test is
decided by a written chronological-triangular proof whose every geometric
and algebraic precondition is checked exactly, with all controls green.
The rule fixes which measurements decide each token. It does not fix
their values.

1. **Preconditions (P1-P6b), each measured exactly:**
   - **P1.** Each f_i(t) in beta has a unique straight own path of length
     t to p_i and reaches no other port before t.
   - **P2.** No element of beta reaches any record of the pre-cut
     history W_tau or any label of the accepted 42-key path. The records
     are R, the old q9 record at L, the V read at L+2, the herald record
     and every pre-cut flag and timing cell; the labels are every slice
     of K0, K1 and K2 and deltaW1 and deltaW2. For each f_i(t) and each
     such (cell, time), dist(f_i(t), cell) > time.
   - **P3.** beta is disjoint from the 42 eta cells, all 1479 compiled
     sources, the 17 named exceptions and the 25 ready balls.
   - **P4.** The same-tick cross-edges are exactly 2->5 and 3->5, which
     is consistent with ordering by (t, i).
   - **P5.** H-torus holds, both the 2H* comparison and the span bound.
   - **P6a.** The rule H is a bijection on all 8 codes, checked
     exhaustively.
   - **P6b (mechanism control).** Every first-front step is a permutation
     of its own triple in arbitrary background, including a background
     that depends on the setting and on eta. It is checked on dense small
     native worlds. It tests the mechanism and is not a measurement of
     the astronomical preparation.

   For P1-P3, minimize over all t in (L+5, H*] at the endpoints and every
   absolute-value breakpoint, recomputed independently of the
   `history_v11` checker.
2. **Tokens.** When every control passes, exactly one token is printed.
   Otherwise the run is VOID.
   - **LA-EQUAL** iff P1-P6b all hold. Under the hypotheses, the written
     proof then gives mu_0^k0 = mu_1^k0 exactly for every k0, k0=⊥
     included, so TV_win(k0)=0 and TV_acc(k0)=0 as exact Fractions.
   - **LA-DIFFERENT** iff a precondition fails and the bounded witness
     search (item 3) returns an exact witness: a k0, a set of accessible
     coordinates and a value of them whose masses under mu_0^k0 and
     mu_1^k0 differ. Since the TV of a projection of A(X) is at most
     TV_acc(k0), this gives TV_acc(k0) > 0.
   - **LA-UNDETERMINED** in every other case: a precondition fails and
     the search returns no witness or is outside its bound. Failure of a
     sufficient condition is not a difference, and nothing is
     extrapolated. The output names the failing precondition, the first
     (cell, tick) at which it fails and the search outcome, and the test
     parks with that named gap. A window difference confined to K0, K1
     and K2 falls in this case.
   - **hidden_only flag (reported, decides no token).** It is true when
     TV_win(k0) > 0 for some k0 and TV_acc(k0) = 0 for every k0. At
     actual scale the only route that establishes TV_acc = 0 for every k0
     is the proof of LA-EQUAL, which also gives TV_win = 0. So the flag is
     false under LA-EQUAL and LA-DIFFERENT and unknown under
     LA-UNDETERMINED. CP-HIDDEN checks its computation on a small world.
3. **Bounded witness search** (run only when a precondition fails). Let Y
   be the accessible port triple at the first failing (cell, tick), and S
   the original variables in its dependence set within the window. The
   search runs only if S has at most six triples, and if the joint law of
   S with (c, K0) is derived exactly from H-prior and the checked
   geometry, in a written derivation with every input checked. It then
   evaluates the native rule over all 8^|S| assignments and both values
   of c, for each k0 class the derivation distinguishes. It computes the
   law of Y under each c in Fractions. Unequal laws are a witness. Equal
   laws, or a failed bound or derivation, give no witness. The procedure
   is asymmetric: LA-EQUAL is certified by proof over the whole window,
   and LA-DIFFERENT only by a local exact witness. A difference that needs
   more than six triples to exhibit, or appears only in the joint law of
   several tail coordinates, is reported LA-UNDETERMINED.
4. **Informativeness flag (always reported, decides no token):**
   EMPTY if Tail is independent of (eta, K0, K1, K2) given D', and
   INFORMATIVE otherwise. Under LA-EQUAL it is computed from the same
   triangular proof. Under LA-DIFFERENT it is INFORMATIVE, since c is a
   function of b5 in eta given D'. Under LA-UNDETERMINED it is UNKNOWN.
   An LA-EQUAL with EMPTY means the sourced later read carries no packet
   or key information at all. Its equality across settings then has the
   same cause as its emptiness, and it is reported in that form.

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
  pinned (unpadded). The joint comparator must report TV > 0, and the
  bounded witness search, run on this fixture, must return a witness.
- **ACCESS (extra access).** The same world, with a background that
  depends on c and reaches the padded port's first front, gives the
  observer an extra read of that port's own bank triple or of a private
  pre-pad field. The comparator must report TV > 0 with the extra read and
  TV 0 with LA alone, as in `history_v11`'s extra-read control (lines
  141-142). This shows that changing access changes the verdict.
- **PRIOR (correlated prior).** The setting-bearing key b5
  (`native-random-setting-test.md` line 40) is set equal to a tail bank
  triple, with fair marginals. The joint TV at fixed k0 must be nonzero,
  and marginal fairness must not hide it. Correlating any other eta key
  gives TV 0 at fixed k0 and is not a valid fixture.
- **MARG (marginal comparator).** A supplied joint-only dependence of
  Tail on (c, R.B/D, K0) with c-independent per-port, per-tick marginals.
  The joint comparator must report TV > 0, and a per-coordinate marginal
  comparator must report 0 on the same fixture. If the marginal
  comparator does not miss it, the fixture is vacuous and the run is VOID.
- **LEAK (record/carrier leak).** A joint-only leak through R.B/D, as in
  the accepted unit: TV 1 with R.B/D retained and TV 0 without.
- **NULL.** Two identical branch laws must give TV exactly 0, and the
  bounded witness search on them must return no witness.
- **SUPPORT.** On four frontier triples the tail support is 4096. Pinning
  one must reduce it to 512 and be detected, as in `history_v11` line 140.
- **HIDDEN.** A fixture whose window laws differ only in K coordinates,
  with equal accessible laws, must give TV_win > 0, TV_acc = 0 and
  hidden_only=true.
- **INFO.** A fixture whose Tail is uniform and independent of
  (eta, K0, K1, K2) must report EMPTY. INFO-COUNTER: a fixture whose Tail
  depends on K0 but not on c must report INFORMATIVE with TV 0.
- **GEO-COUNTER.** A frontier ray moved by a fixed offset onto the
  packet's cone, a ray placed on an eta cell, and a ray that reaches the
  old q9 record cell at L or the V read cell at L+2 by that record's time
  must each fail P2 or P3.
- **BREAKPOINT.** A geometry fixture whose minimum lies only at an
  absolute-value breakpoint must be found by the breakpoint method and
  missed by sampling at the endpoints and a fixed tick grid.
- **ORDER-COUNTER.** A reversed equal-time order must fail P4.
- **PERM-COUNTER.** A non-bijective rule H'(A,B,D)=(B,D,BD) must fail
  P6a and P6b.
- **READSET.** The declared read set must equal the LA set (8 ports at
  every tick L+6..H*) plus the pre-cut accessible records. Any other read
  field must be flagged as an access change.
- **STOP.** On the small world, the law under each enumerated stop rule
  on A(X)-prefixes must be the pushforward of the full-window law, with TV
  no larger than the full-window TV. STOP-COUNTER: a stop rule that takes
  R.A as an input must be rejected by the stop-rule domain check before it
  is evaluated.
- **BRANCH.** 48 continuing and 16 terminal contexts, the latter compared
  at k0=⊥, with unnormalized masses retained. The masses must sum to the
  source-context masses, not to 1 per branch.

## Invariant -> checkpoint table (§A.41)

| Invariant asserted | Checkpoint |
| --- | --- |
| Pinned inputs unchanged: `native_vread_v15/checks.py` 93b4161f32e02874769d57d8a670d1a460d26fa2c953d517db5c6564fb649824; `shared_v12/INTERFACE-CONTRACT.md` 1a0b34ebb0c7115dd5faae11d2ab20c25ecf8a6f091ea292eb184e4311be7633; `history_v11/REPORT.md` 413c9595a6def923ba62e1c0d34c12c0516997fe1c928e5438abaf6a990fdb81; `parallel_v3/history_control/SOURCE-GEOMETRY.json` 2642e1a68825faa5d3bb1049e8722adec1ec33bd3f56b9e4416b2c902a85ec5d; `native_random_setting_probe.py` 1609a902350de46aa051b771725eaf1bec611d0ce843ee5e005e2ee3dde0753b | CP-PIN: sha256 equality, else VOID |
| Native rule unchanged and nonlinear | CP-RULE: h equals the pinned rule on all 8 codes |
| P1 own paths, no early other-port arrival | CP-GEO-OWN: exact breakpoint minimization, all 8 rays over the full window |
| P2 beta excluded from every pre-cut record and the 42-key path | CP-GEO-EXCL: dist(f_i(t), cell) > time for every record and label (cell, time) |
| P3 disjointness | CP-GEO-DISJ: exact affine-ray intersection against eta, sources, exceptions, balls |
| P4 order | CP-ORDER: all equal-time cross-edges enumerated |
| P5 no wrap and span bound | CP-TORUS: integer comparisons 2H* < side and every span < side/2 |
| P6a bijective rule | CP-PERM-A: exhaustive over 8 codes |
| P6b diagonal permutations (mechanism) | CP-PERM-B: dense small worlds, setting- and key-dependent backgrounds |
| Comparator detects coupling; search finds it | CP-POS: TV > 0 and a witness |
| Access change detected | CP-ACCESS: TV > 0 with extra read, 0 without |
| Correlated prior detected | CP-PRIOR: joint TV > 0 at fixed k0 with fair marginals, b5 correlated |
| Marginal comparator misses joint-only difference | CP-MARG: joint > 0, marginal = 0 |
| R.B/D retained | CP-LEAK: TV 1 with R.B/D, 0 without |
| Comparator and search not trivially positive | CP-NULL: TV = 0, no witness |
| Frontier triples padded | CP-SUPPORT: 4096 -> 512 on pinning |
| Hidden-only case reported | CP-HIDDEN: TV_win > 0, TV_acc = 0, hidden_only=true |
| Informativeness flag can take both values | CP-INFO: EMPTY fixture and INFO-COUNTER |
| Geometry check can fail | CP-GEO-COUNTER, CP-BREAKPOINT, CP-ORDER-COUNTER, CP-PERM-COUNTER |
| Access is exactly LA | CP-READSET |
| Stop policies add nothing and never read R.A | CP-STOP, CP-STOP-COUNTER |
| Pre-cut factor equal across c (use-cut independence re-measured, not assumed) | CP-PRECUT: the law of (R.B, R.D, K0, other pre-cut records) is checked as a function of c on the fixture, and the geometry of R's exclusion from K0 is re-checked |
| All branches retained, no renormalization | CP-BRANCH: 64 contexts, 16 at k0=⊥, masses summing to source-context masses |
| Exact arithmetic only | CP-EXACT: every measured quantity is int or Fraction; a float anywhere is VOID |
| Replay | CP-REPLAY: normal and `-O` structured outputs byte-identical to each other and to the committed expected JSON; controls use explicit checks, never `assert` |
| Verdict over green controls only | CP-GATE: token generated from measurements after all controls. Exit 0 with the token (LA-EQUAL, LA-DIFFERENT or LA-UNDETERMINED) in the JSON; exit 2 VOID; exit 3 output differs from the committed expected JSON |

## Mutation targets

Each mutant must exit 2 with VOID naming its control, in both modes:

| Mutant | Control that catches it |
| --- | --- |
| drop R.B/D from X | CP-LEAK |
| replace the joint comparator by the marginal one | CP-MARG |
| pin one frontier triple | CP-SUPPORT |
| shift one ray onto the packet cone | CP-GEO-EXCL |
| truncate the minimization to sampled ticks | CP-BREAKPOINT |
| reverse the equal-time order | CP-ORDER-COUNTER |
| substitute the non-bijective rule | CP-RULE, CP-PERM-A |
| omit the terminal contexts | CP-BRANCH (count) |
| renormalize branch masses | CP-BRANCH (mass sums) |
| introduce a float | CP-EXACT |
| expose an extra field without flagging an access change | CP-READSET |
| let a stop rule read R.A | CP-STOP-COUNTER |
| compute the token before the controls | CP-GATE |

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
