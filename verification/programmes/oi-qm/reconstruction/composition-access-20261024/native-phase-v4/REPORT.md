# Native-phase closure needs the full response kernel

Research checkpoint, 24 October 2026. This applies the existing conditional
composition contract to the prepared native post-Y phase. It supplies exact
local boundary controls and a precise next-reset obligation. It does not
construct a native reset, adopt new observer access, or prove that the local
boundary completions below arise from the retained original-time apparatus.

## A fixed operational comparison

The physical boundary includes both native time slices, residual workspace,
unused resources, the clock and public history. Use one tagged space whose
components identify the interface phase and contain those variables. A failed
protocol keeps its actual final metadata and physical fields but offers no
carrier; future testing of that branch stops under the declared terminal
failure policy. Absorbing padding is a record convention, not physical erasure.

For unnormalized boundary measures mu and nu, define mu approximately equal
to nu when every permitted finite adaptive continuation gives the same
complete future-record measure. Include the zero-step stopping test, initial
public-history sectors, timing, all raw fields, heralds and failures. The
protocol and access class are fixed once for the comparison. They may depend
on the public history through a common controller, but the relation is not
replaced after observing an outcome. This definition is an operational
relation on measures; it is not equality of hidden configurations.

There is a useful finite-depth version. At depth zero require equality on
the available stopping/public-history tests. At depth d+1 require, for every
common allowed setting a and complete record increment r, that

    K_(a,r) mu approximately_equal_d K_(a,r) nu.

This recursion identifies all tests of depth at most d+1 when the allowed
protocol class is closed under prefixing and branch continuations. The
forward direction follows by prefixing any depth-d test with the chosen
setting and selecting its record branch. The reverse direction conditions a
depth-(d+1) protocol on its first full record and applies the depth-d equality
on each branch. Summing preserves equality without normalization, including
zero-mass branches. The all-depth relation is the intersection over d. These
are written definitions and elementary arguments, not a new Lean certificate.

Equality under the selected-coordinate map or Bloch decoder is weaker. For
a proposed decoder D, the existing sufficient instrument contract requires
an admissible cone C closed under every complete-record kernel, positivity
and mass preservation of D on C, and

    D_out K_(a,r) mu = I_(a,r) D_in mu.

One necessary consequence is that equal-decoder admissible measures have
equal decoded branch measures under every K. In linear form the kernel of
D_in must lie in the kernel of D_out K on the relevant span. Equality of
selected moments alone does not supply this condition or cone closure.
Conversely, literal equality of every hidden field is unnecessary if unequal
completions have the same response for all permitted continuations. The
positive control below checks that distinction at one native tick only.

## An omitted native neighbor changes the next raw record

The source at #910 has previous q8=(0,y,0) and current q9=(0,X,R), where q9
is the +z neighbor of q8. Let C=(C_A,C_B,C_D) be the XOR of the other five
current neighbors of q8. The native rule H(A,B,D)=(B,D,A XOR BD) gives

    U_(L+1)(q8) =
      (C_B XOR X,
       y XOR C_D XOR R,
       C_A XOR ((C_B XOR X)(C_D XOR R))).

Thus previous-slice Y does not simply reappear at a current raw port. The
five-neighbor parity and both current X/R fields affect that response.

Fix either public y. Compare two local boundary measures with the source's
same complete selected-phase law, old history, whole-q9 raw law and herald
success 5/16. They differ only by C=000 versus C=100 on successful branches.
Their next-q8 raw triples differ only in D. The first two fields recover X
and R at fixed y, so the supports are disjoint: the next complete record has
TV distance 1 conditional on success. Retaining the same terminal failure
law gives full-law TV 5/16. Actual rejected q9 fields, including the exceptional
mask 01 law, are retained in the checker; no failure qubit state is invented.

This is a countercontrol to treating equality of selected phase coordinates
as a one-step transition invariant on an unrestricted boundary cone. It is
not a counterexample to the current native candidate: its existing access
contract ends at a terminal read at L. The test explicitly proposes a new
whole-q8 read at L+1. Original-time reachability and the admissible prior of
the two completions are separate questions for the native construction.

An initialization condition or physical invariant fixing the relevant C can
exclude this countercontrol, but that condition must be checked on the actual
output boundary. A new cold apparatus cannot replace the dirty neighborhood.
Specifying C still only controls this particular one-step response; further
ticks may expose more residual variables.

## Matching the next public record still misses a joint defect

Set C_B=C_D=0. Compare the following local completion laws:

- Fresh control: C_A is fair and independent of X,R,Z and the old history.
- Correlated control: C_A=Z XOR XR, with the same independently fair selected
  Z and the same selected post-Y law.

In both laws C_A is fair conditional on the complete old public history and
whole-q9 record. In both, the next whole-q8 record has the same law. In the
correlated control its D field equals Z; in the fresh control D is independent
of Z. Consequently the joint next-record/retained-Z law has TV distance 1/2
conditional on success, or 5/32 with the original terminal failures included.
At L+1 the old current Z cell is physically in the previous slice; this joint
test uses that retained selected field. It does not assert a new available
public read or native delivery of Z after the extra tick.

This exposes a defect beyond a wrong next-record marginal: even an entire
matching next-record law does not suffice when the record is correlated with
the outgoing comparison field. Conditional freshness relative to public
history alone is too weak. A sufficient fresh-bank condition includes all
other response-relevant incoming variables, or the actual joint seed/input
law must be retained inside K and checked directly. These completion laws
are local mathematical controls, not newly allowed initial seed priors.

The positive local control uses different five-neighbor configurations with
the same XOR C. They give identical next-q8 raw output for all tested selected
states. A field outside the one-step causal cone also has no effect. Thus
this horizon needs a response invariant, not hidden-state identity. Neither
control asserts full future operational equivalence.

## Exact obligation for the next native X reset

On a successful prepared post-Y branch, the public whole-q9 record h=(x,r)
has probabilities 1/2,3/10,1/5 on (y,y),(1-y,y),(1-y,1-y). For designated X,
the outcome x is fair. Its additional r field has refinement

    kappa_y(r | x)=1                  if x=y and r=y,
                    3/5             if x differs from y and r=y,
                    2/5             if x differs from y and r differs from y,
                    0               otherwise.

The source already permits this bounded refinement on the post-Y family.
It is not a general preparation-independent raw-port refinement. The earlier
public y is a reference controller variable; the physical decoder remains
fixed and does not recover a carrier bit by reading history.

For every actual incoming branch, the next native stage must accept the full
two-slice measure conditional on h, all prior flags and the public noise word.
It must then output a positive carrier with the X eigenstate branch, jointly
with every newly exposed record and success/failure flag. If mu_h is the
unnormalized post-read branch, an independently implemented successful reset
with declared refinement lambda would need

    D_out K_(h,new_record,success) mu_h =
      mass(mu_h) lambda(new_record,success | public history,h) rho_X,x.

If its herald probability or metadata has another dependence, the actual
reference instrument must explicitly include it; this equation does not
supply that probability. Failed branches keep their actual physical and raw
record law and offer no carrier under the existing convention. The outgoing
full boundary must satisfy a reusable continuation invariant, not merely the
same selected coordinates or this one equation on a pooled marginal.

The exact positive control preserves h and independently samples the supplied
post-X ensemble (X,Y,R,Z)=(x,x XOR a,x XOR b,z) with mask counts 5:4:1 and fair
z. Its fixed Bloch decoder is rho_X,x and its R mean is (4/5)(-1)^x. It is
only a law-level stochastic control, with no additional reset herald; no
native implementation or original-time resource construction is inferred.
It retains the original 11/16 terminal failure branch. In contrast, offering
the unchanged post-read selected sample fixes X and old Y and has decoder
determinant -1/4, as the earlier source already records.

## Evidence, scope and next use

The self-contained `checks.py` uses exact integers and fractions. All 832
local native-update cases and 832 outside-cone controls pass. Omitting the
five-neighbor parity produces 728 mismatches; dropping the old slice gives
416. The same-parity/unequal-hidden-state control has 384 exact cases. Both y
families pass the complete-record and joint-record/retained-Z TV controls,
including physical failed-phase distributions. The fresh X-reset control
checks six complete whole-port branches and 36 outgoing selected cells.
Normal and optimized replay must be byte-identical to `result.json`.

The new result is a concrete native response dependency and a stronger joint
countercontrol. It does not certify the old transport theorem, actual future
public-bank freshness, current-family complement freedom, a new access rule,
or physical reset. #910 owns those native questions. The existing #912
composition induction and strict raw-tag audit remain unchanged. #911 owns
state/operation coverage; a changed operational comparison must still meet
target coverage and preserve every permitted source observation. No A1/A2
equivalence, adopted physical premise, F/E designation, dispatch or merge is
established, and #885 remains untouched.

Sources are pinned in `PROVENANCE.json`. This checkpoint applies #912 head
`69540662b234e37c6805ded244962a80f15f63a2` to #910 head
`71d291297d0a662cbb9377ab48eef7aa4b839e77`; its local formulas and controls are
new. Off-main references are research provenance. Replay from this directory
with `python3 checks.py` and `python3 -O checks.py`.
