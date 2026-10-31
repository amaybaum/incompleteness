# Native port-5 first-arrival reduction

**Research-only conditional result.** Input snapshot: `7c4e45f723711b6d2c512b492a1dfa899a3c0e4c`. This reduces one proposed q10-to-port5 transport calculation. It is not a full 78-tick source/history/carrier replay, a selectable measurement, or a native quantum instrument. No preparation or access extension is adopted.

## Retained model and sources

The native rule is
`U_(t+1)(v)=U_(t-1)(v) XOR H(XOR_(w~v)U_t(w))`,
`H(A,B,D)=(B,D,A XOR BD)`.

Keep `T=185, P=12*840^185, S=P+T, R=S+68, L=R+9`, torus side `256L+64T+1`, q10 at `(0,S,78)` and t0=L+1. The declared public port5 is p5=(0,S,0). Its first possible response to a late-cut q10 operand is at
`horizon=t0+78=L+79`.

Source anchors under `verification/programmes/oi-qm/reconstruction/native-y-continuation-20261024/`:
- `shared_v12/INTERFACE-CONTRACT.md`: rule, supplied prior, whole-record/carrier obligations, eight-port bank scope.
- `native_route_v13/checks.py`, `geometry()`: ports, 24 inherited ready balls, q10 ready extension, E/N exceptions and 1479 old sources.
- `native_vread_v15/REPORT.md`, “Permitted reads and the choice of stage”: q10/p5 distance and the one-tick obstruction.
- `native_v11/REPORT.md`, “Native proof in arbitrary background”: unique axial first-arrival response is a permutation.
- `history_v9/REPORT.md`, “Fixed dynamics, ports and bank” and “Joint chronological permutation proof”: independent original-time bank triples and triangular public-noise proof. That earlier report has older deadlines/torus; the geometry here uses the later native_route/shared values, not the old constants.

The prospective public record horizon must be explicitly extended from the previously checked cuts to L+79, including every raw field, every earlier failure and the old q9/V terminal reads. The retained independent-uniform original complement/bank law must explicitly cover the initial key below. The general bank family through horizon <=2L supplies a conditional template; this note does not adopt an unlimited-access or fresh-bit resource.

## Structural late-cut cone

In 78 steps the endpoint's current-slice structural dependency support is the parity ball of radius78 and its previous-slice support is the parity ball of radius77. Their cardinalities are respectively328719 and316394 initial triples. These are structural supersets, not claims that every variable survives nonlinear/XOR cancellation. No wrap shortcut exists at the declared torus size.

q10 lies on the axial boundary: the only length78 path is 78 steps in -z. At its jth step the other five current predecessors and old-local term are too early to depend on the varied q10 coordinate. Fix every other two-slice value at t0. The response at each path site is
`w -> a_j XOR H(w XOR b_j)`,
with a_j,b_j fixed under that variation. H and XOR translations are permutations, so q10's whole raw triple reaches p5 by a bijective response for each fixed late-cut remainder.

This is conditional sensitivity, not a preparation theorem. The original source prior can correlate the late-cut q10/remainder. In a dirty background the response is not generally H^78; the constants cannot be omitted.

## An original-time fresh masking key

Set
`K=p5+(L+79)e_y=(0,S+L+79,0)=f5(L+79)`,
a current initial triple on port5's own +y bank ray.

Exact geometry gives:
- distance(K,p5)=L+79.
- Every other declared public port is farther than L+79. Ports2/3 have excess370, port4 excess925.
- distance(K,q10)-(L+1)=156, so q10 at the input cut is K-independent.
- K is outside old q9 at L and the V read at L+2.
- Minimum slack to all24 inherited ready balls plus the q10 ready extension is156.
- K equals none of the1479 inherited sources, E, N, the fourth selector or the opposite reset pulse.

All comparisons use the later source geometry and exact astronomical integers. Inventory completeness remains the same explicit input as in the prior v15 classification.

The source K has one straight +y-to-p5 axial path of length L+79. The established arbitrary-background unique-path argument applies directly from original time: for every fixed complementary original configuration, p5's full raw triple at L+79 is a permutation of K. The old-local/off-path terms are too early to depend on K. K affects no other declared port through that horizon and no earlier p5 record; it also cannot affect the old terminal records/flags or q10 input.

**Conditional masking theorem.** If K is an independent uniform initial triple conditional on all other initial variables, then p5's raw triple at L+79 is uniform conditional on those variables and on every other permitted record through that cut. It therefore adds no information about q10.A at its first possible arrival. This is a real original-time pad argument, not an inference from marginal uniformity at the late cut. Conditioning on earlier nonzero-probability terminal-success/failure branches preserves it because those branches are K-independent.

This does **not** say that the complete transcript is independent of s: the old whole-q9 record already contains s. It says that this particular later raw record supplies no additional operand information under the stated prior. Nor does it imply independence from the outgoing carrier, which can depend on K and all other bank variables. A joint record/carrier kernel, later key disclosure and alternate readouts remain separate questions. A uniform measurement record may still have useful carrier correlations, so no general instrument no-go is claimed.

## Next affordable decision and limits

The fixed-key positive control shows the first-arrival map transports a distinguishable whole operand; the independent-uniform-key control shows why that signal is not an unmasked public operand under the retained prior. There is no reason to run a giant replay merely to rediscover this marginal.

The next useful task is a **joint history/carrier congruence test**, after declaring an actual two-slice outgoing cut and operational target: which carrier variables depend on K, can any already permitted joint record disclose K, and does conditioning preserve the intended reusable interface? If a candidate needs K pinned or read privately, report that exact preparation/access addition. If the target is clean q10.A delivery in the p5 raw symbol at first arrival, the conditional masking theorem rejects that target under the supplied uniform-key law. It does not decide later routes or two-setting availability.

The scalar torus revival candidate is a different model and prior; no distributed torus readout or setting actuator is imported here.

## Reproduction

From the repository root, run:
```sh
python3 -I -B verification/programmes/substratum/continuous-substates/native_port5_cone_probe.py --source-inventory verification/programmes/oi-qm/reconstruction/native-y-continuation-20261024/parallel_v3/history_control/SOURCE-GEOMETRY.json
```
Repeat with `-O`; output must be identical. The checker hash-pins the1479-source input, checks the actual geometry and parity-cone cardinalities, checks all64 one-step translated-permutation families, three78-step algebraic compositions and512 uniform-key local laws, and retains the fixed-key positive control. The finite algebraic compositions validate the permutation mechanism; they are not simulated native78-tick backgrounds. The astronomical conclusion rests on the unique-path proof and the supplied independent original-time prior.
