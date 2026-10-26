# Workspace-assisted Y continuation: exact bounded result

Research only, consistency axis. Start from #910 head
`9d77dbbaddf5671cb20655934e4a65145c983e57`; preserve existing payloads.
The native q7 endpoint is clean but its actual old slice and neighborhood retain
history. The previous single upper source family cannot produce a common q8
Y code. This probe changes where the physical input meets apparatus data.

Set N=R+7 and q8=qY+8e_z. Retain the initial upper Q and correction C. The two
candidate initial sources are W at h=(0,-76,76), and G at g=f+2e_z. Each payload
may depend on the existing seed u but never on unknown x, y, or a diagnostic
input. The source W is reached by the existing x front; x is not preloaded.
Use an explicit depth8 current/previous ready extension, preserving these
sources and all inherited sources. All changes are at initial time.

W cannot reach q7 before N+2. At the initial diamond slice R−1 it reaches
exactly one site, (0,S−9,76), where the actual lower background is the origin x
source. At all other queried pre-collision sites it is absent. The coupled
origin/W first-front recurrence along y is

F_0=H(H^75(0,x,0) XOR H^75(W)),
F_j=H(F_(j−1) XOR a_j),
a_j=[j AND 75 = 0] H^(j+75)(0,x,0).

The forcing has period lcm(128,12)=384. One block is an eight-state permutation,
whose order divides 840. Hence 384*840 is a global period and divides actual P;
the giant query j=P+176 reduces to j=176. This is a full coupled-source
calculation, not isolated pulse superposition. All later interactions are kept
in the exact q8 collision diamond with the Q/C/G upper strip.

Decision rule: enumerate the 64 (W,G) settings independently per u and test all
native x and selector masks. Report every common two-code encoding of y from
any pair of u-specific settings; separately record standard clean codes. Then
replace only q7.D at N by arbitrary p7 with its actual past retained, and test
whether the whole outgoing triple is an injective common function of p7. A
native-only encoding is not a reusable late-input socket. If no setting works,
report only this explicit two-source, one-tick family as excluded.

Controls precede verdicts: inherited digest checks; exact P divisibility; full
8-state forcing-block permutations; independent direct spatial recursion at
bounded coordinates including the first origin/W collision; W=0 agreement
with the previous model; one-site cone-entry and first-arrival geometry; old
ready/source exclusions; q7 native and original qY/q2 diagnostic preservation;
all selector masks; normal/-O byte identity. Initial compatibility with all
extended public-record banks and their joint-law proof remains an explicit
additional obligation. No private prefix becomes public by this probe.

This is routing research toward post-Y (y XOR a,y,y XOR b,z) with 5:3:2 and
fresh fair z. Clean routing alone does not provide the sampler, independence,
herald, complete carrier, or joint instrument law.

## Exact ray reduction before the new computation

In absolute coordinates W is at `(0,-76,76)` and the ray is `(0,j,76)`,
queried at time `j+76`. For j>=0 both the physical origin source and W have
exactly that first-arrival distance. No earlier local term contributes.
At j=0 the only two active predecessors are the origin's unique +z path
and W's unique +y path, both of length75, giving the displayed F_0.
For j>0 the -y predecessor is F_(j-1). The -z predecessor at `(0,j,75)`
cannot yet have been reached by W; its origin-only first-arrival value is
the multinomial parity times H^(j+75)(0,x,0). The other four neighbors
are outside the source cones at that tick. Binary no-carry parity is exactly
`j AND75=0`, giving the stated recurrence with every source interaction kept.

The parity factor depends only on j modulo128 because 75<128. H has order12.
Therefore the forcing sequence has period384 (a sufficient period, not a
claim of minimality). Each step z -> H(z XOR a_j) permutes the eight triples.
The composition of any384 consecutive steps is consequently a permutation
of eight states, and its order divides lcm(1,...,8)=840. After840 such blocks
the state and forcing phase recur. Thus the sufficient exact period is
384*840, globally for every initial triple and both x values. Its prime
factorization is `2^10*3^2*5*7`; P has valuations `v2=557`, `v3=186`,
`v5=v7=185`, so divisibility is exact. No reduced-scale extrapolation is used.

The q8 backward initialization uses a ball of radius9 at R−1 and radius8
at R−2. Since W and q8 differ only along y, its earliest possible point in
the former is the unique axial predecessor `(0,S−9,76)`, at distance R−1;
it reaches none of the latter. The ray index is S−9=P+176, reducing to176.

W is outside the old ready balls and reaches the original designated
receivers later than their designated read ticks. That geometric claim will
be checked explicitly. Unlike the upper-only G source, W can change the
much later old-record backgrounds. Their joint masking and conditional
resource independence are not inferred from preservation of the earlier
designated values.


## Result and scope

The bounded family contains a native clean Y route. Choose the initial
workspace payload W=111 independently of the unknown input and choose the
upper payload G=011 when u=0, G=101 when u=1. On every retained native history,
the full q8 triple at R+8 is `(0,y,0)`, where y=x XOR u. The earlier clean q7
value at R+7 remains `(0,0,y)`. These choices depend only on the apparatus's
existing seed u; x reaches W through the physical first-arrival dynamics.

The full enumeration finds 32 distinct ordered pairs of output codewords,
realized by 56 pairs of u-specific `(W,G)` choices. Each u has 64 choices;
the common-code test therefore covers all 4,096 pairs of such choices. No
pair provides a common injective full-triple encoding of an arbitrary bit
substituted into q7.D while retaining the actual preceding history.

The clean route illustrates the distinction. With u=0, W=111 and G=011,
setting q7.D to p=0 gives q8=000 when x=0, but q8=001 when x=1. A genuine
late-input socket would give the same full triple for the same p in these
two histories. Thus this construction routes the correlated native family;
it does not erase the surrounding history or make q7 alone the input state.
The separate qY and q2 interventions are retained in `results.json` too.

This positive result changes the one-source routing conclusion only by
changing the explicitly examined family: W supplies a second physical
source with an earlier collision. The previous one-upper-source obstruction
remains intact. The new route supplies neither the 5:3:2 post-Y sampler nor
fresh fair z, herald/failure behavior, or the complete outgoing carrier law.
It does not establish reusable reset or full OI–QM equivalence.

## Validation and replay

`probe.py` uses integer bit packing to evaluate all assignments exactly.
Every control completes before the structured verdict is emitted. The normal
and optimized Python outputs are byte-identical to `results.json`:

```sh
python3 probe.py > /tmp/oi-reset-v8.json
cmp /tmp/oi-reset-v8.json results.json
python3 -O probe.py > /tmp/oi-reset-v8-O.json
cmp /tmp/oi-reset-v8-O.json results.json
```

Run from this directory in the retained #910 tree. The sibling `reset_v7/`
evaluators and `parallel_v3/history_control/SOURCE-GEOMETRY.json` are required;
`PROVENANCE.json` pins their hashes and source commit. The three inherited
code files and geometry file were compared with their published Git blob
IDs at that commit. The replay itself checks their SHA-256 digests.

The controls give:

- 144 scalar comparisons of the coupled first-front recurrence with direct
  spatial recursion at j=0 through 8, covering both x values and all W;
- exact divisibility of actual P by the ray and upper-strip periods, and
  eight-state forcing-block permutations for both x values;
- four explicit counterexamples to isolated-pulse superposition at the
  origin/W collision;
- the unique W entry point in the two-slice collision diamond, 1,479 retained
  source-geometry exclusions and preservation of 15 designated earlier reads;
- 768 W=0 endpoint comparisons with the previous evaluator;
- 6,144 full diagnostic rows, all checked for selector-mask independence,
  with the native q7 and earlier qY/q2 diagnostic formulas preserved.

These are bounded exact computation plus the written period/front argument.
They are not a new Lean certificate, a CI attestation or external review.
This completes the prior session's local probe plan; the plan was not an
owner-designated F and is not retroactively represented as one.

## Remaining constructive obligation

W is outside the designated earlier read cones but can change later old-port
backgrounds. In particular, preservation of the earlier designated values
does not establish compatibility with the whole extended public-history bank.
A proposed reset must account jointly for these public records, apparatus
seeds, retained information, the two-slice carrier and failures.

The next bounded construction should use the explicit clean route and its
actual neighborhood as its starting interface, supply a physical sampler
with the unchanged 5:3:2 law and fair z, and verify the full record/carrier
law after conditioning on the entire allowed history. If a reusable arbitrary
late-input socket is demanded instead, it must change this two-source,
one-tick family; every setting in this family has failed that stronger test.
No physical premise or access change is adopted here.
