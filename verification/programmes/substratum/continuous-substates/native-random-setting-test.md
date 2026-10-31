# Native randomized port-5 setting: fixed two-step comparison

Research-only unit after independent ACCEPT and successful CI on
`4095d98564c835de4a1d4584af5275e3b91d668b`. This unit awaits its own
independent review. It tests an actual existing native random record,
without assuming a commanded write or adding any source. The original
preparation, complete 42-bit carrier, fields and record dictionary remain.

**Candidate result:** port 5 supplies a setting independent of the incoming
packet, but both setting branches have the same joint future record/carrier
kernel in the existing L+3 -> L+4 -> L+5 passive window, under the stated
joint product prior. This candidate fails the distinct-interaction test.
No general obstruction to native randomized control follows.

## Fixed experiment and relation to earlier work

Use the whole raw record R=U_(S+4)(port5), with setting c=R.A. Keep R.B/D
in the public record. The incoming carrier is K0=K_(L+3), all fourteen
raw triples. Outputs are K1=K_(L+4), K2=K_(L+5), together with all eight
raw public-port triples at each of those two ticks. Keep the whole public
past, old flags/timing and the stipulated V record where present.

The decision rule is conditional joint-kernel comparison at the same
incoming packet under both setting values, with independence checked at
the use cut. A changed setting tag alone is not an outcome difference.
Retain all failures; introduce no setting-dependent herald or stop filter.
A nonzero joint difference would justify a further operational study;
equality closes only this setting/carrier/read dictionary and time window.

The earlier accepted selector checkpoint `53bf7ac8` tested the S+2 record
and an L+1 -> L+3 adapter. Here S+4 is tested at the actual accepted K_(L+3)
input, using its full-packet law and the already accepted two-step successor.
This is a source-specific combination of those results, not an added passive
horizon or a new foundational no-go theorem.

## Trace the original bank source, not an external perturbation

The original current bank cell is

    b5=port5+(S+4)e_y=(0,2S+4,0).

It is an already reserved independent BANK block, distinct from all old
source exceptions. Its unique straight first arrival at port 5 is S+4.
It reaches no earlier public record or other same-tick port. Thus R is a
permutation of that original triple for every fixed original remainder.

The minimum distance from b5 to the incoming seven-site footprint is L+4.
It affects neither slice of K0. It also cannot affect Q=U_(L+1)(q10) or
the earlier qY,...,q9 source phases and their original flags. Under the
retained independent bank law, R is uniform on eight triples, c is fair,
and R is independent of K0 at the use cut on the fixed original continuing
preparation. This is use-boundary independence, not only initial fairness.

| Native event | Original-bank dependence allowed by the stencil |
| --- | --- |
| R at port5, S+4 | Unique axial first arrival, bijective in b5 |
| Both incoming slices at L+3 | Excluded |
| Current packet at L+4 | Possible at +y and -z boundaries only |
| Current packet at L+5 | Possible at center only; prior L+4 boundary fields remain in the previous slice |

The last two rows are possible-dependency bounds, not certified nonzero
signals. The source-to-packet route has multiple shortest paths. We do not
superpose separately propagated responses or replace the original bank
variation by an isolated late port toggle. The comparison below retains
all native effects of that source in arbitrary complementary backgrounds.

## One joint original-key calculation

Form a single collection eta of 42 distinct original current triples:

- one bank triple b5 for the setting;
- thirteen incoming-packet witness triples from the accepted parent;
- twelve boundary triples and sixteen public-bank triples for the two
  accepted passive successor ticks.

All geometry is checked directly against the 25 ready balls, 1479 compiled
sources, 17 named exceptions, bank lines and inherited torus. There are
25 FREE complement triples and 17 BANK triples. All forty-two are distinct.
Every own output path is uniquely axial. Ordering the setting first,
incoming labels chronologically, then each future boundary block and
public-port block, gives a triangular first-arrival graph: no later key
can reach any earlier label. Its diagonal maps are bijections because each
native step is K XOR H(V XOR B), with H bijective and arbitrary fixed
backgrounds. The new probe checks the entire 42-by-42 conservative graph.

Let D contain every other original variable. Require explicitly

    Pr(eta=z | D=d)=8^-42.

The retained full independent complement/bank preparation supplies this
option. It is not inferred from the previous thirteen-key and twenty-eight-
key marginal hypotheses separately. The native_route_v13 arbitrary-complement
contract alone does not supply it. Correlated priors need a separate test.

Write pi(K0)=Q for the exact inverse packet coordinate from the parent,
and S(k,k') for the native support constraint: the previous output slice
is the current input slice, and the new center is the native update.
For any complete raw setting r, compatible packet path and future raw
eight-triple increments w1,w2, the joint law conditional on D is

    Pr(R=r,K0=k0,K1=k1,K2=k2,deltaW1=w1,deltaW2=w2 | D=d)
      = 8^-42 * 1[pi(k0)=Q(d)] * S(k0,k1)*S(k1,k2).

The free labels are one setting triple, thirteen incoming triples, and
fourteen triples per future step. Their triangular map is bijective,
so the mass is normalized over 8^42 label paths. Dividing by the setting
and input masses gives, in every positive-mass continuing branch,

    Pr(K1=k1,K2=k2,deltaW1=w1,deltaW2=w2 | K0=k0,W_tau=w,R=r)
      = 8^-28 * S(k0,k1)*S(k1,k2).

The formula is the same for every whole r, hence for both c=R.A values.
Every step retains six new boundary triples and eight public triples.
No equality of isolated marginals is substituted for this joint result.
The two existing passive stages consume their outgoing native fields as
before; this adds neither a controlled gate nor reuse beyond L+5.

## Full histories, failures and environment

W_tau includes R, so its complete value differs across setting branches.
Keep that prefix as conditioning data; do not count the tag difference as
an interaction or erase its B/D fields. For fixed D the pre-cut history is
a function of r and the optional V packet coordinate: future keys reach
none of it, and the incoming thirteen keys reach no port through the cut.
V is an actual previous -z packet triple, not a separate independent factor.
Keeping it changes the initial fibre mass to 8^-12 where conditioned,
but does not change the future kernel above.

The setting/input independence statement concerns the original continuing
preparation and fixed baseline protocol. A new selection rule such as
keeping only V.A=c can create a correlated incident ensemble. Such a
postselection is not silently included or used as evidence of physical
control; its failed branches and changed preparation law must be retained.
General controller seeds or adaptive actions require their joint source
audit at use time.

For earlier terminal branches, use their original flags/masses: no new
setting read after termination and no offered carrier. If R was recorded
before a later terminal event, it stays in the record. There are no new
failure predicates or success probabilities inferred from microscopic row
counts. The 48 continuing and 16 terminal source rows remain diagnostics.

The environment is the full native pushforward G_(L+5)(D,eta). Conditional
on D and the complete label path, the context-dependent triangular inverse
reconstructs eta and hence that outgoing cut. The unconditional joint law
integrates the original conditional D law, including every earlier record
and failure constraint. This retains all setting/key/environment correlations.
The environment is not claimed to be setting-independent, reset or
accessible to a private decoder. A later interaction using those correlations
could evade this fixed-window result and needs its own native/access proof.

Thus a random setting is allowed in principle; this actual candidate simply
does not yield distinct declared joint kernels. The test permits disturbance
after preparation. It leaves physical control elsewhere, later readouts,
repeatability, adaptive choice and composability open. No full-carrier
benchmark or #866 quotient is changed, and no manuscript claim is upgraded.

## Bounded checks and replay

`native_random_setting_probe.py` pins the primary preparation code, source
inventory and shared contract under the retained native continuation root.
It checks all42 source classes and the complete chronological dependency
matrix, the original-bank trace, input exclusion, future history exclusion,
and every native background/old-local permutation. No astronomical field
simulation or native actuator is run.

A 4096-row exact arithmetic triangular fixture verifies whole-setting
joint factors with all R.B/D fields retained. It is a bookkeeping control,
not a surrogate native measurement. A deliberately supplied center actuator
has TV1 at fixed inputs. A joint-only record/carrier leak has TV1 with
R.B/D retained but TV0 when those fields are discarded, ensuring that a
marginal-only comparison fails. Four mutation classes reject in normal
and optimized execution. The full kernel equality rests on the written
42-key source proof, not on the small fixture alone.

From the repository root:

```
python3 -B verification/programmes/substratum/continuous-substates/native_random_setting_probe.py
python3 -O -B verification/programmes/substratum/continuous-substates/native_random_setting_probe.py
```

Both emit identical structured PASS; a failed control emits VOID/exit2
before a verdict. This is exact algebra and a conditional paper proof,
not Lean certification or operational QM. Inputs retain the accepted
`native-packet-operand-and-setting.md`, `native-packet-stochastic-kernel.md`,
`native-interface-selector.md` and the original native_vread/shared source
qualifications. Earlier acceptance is not transferred to this new unit.
PR #1009 remains research-only, draft and unmerged. No manuscript edit,
new preparation/access adoption, F/E designation or special workflow launch.
