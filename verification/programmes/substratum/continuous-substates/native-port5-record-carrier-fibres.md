# Port-5 record/key fibres and the outgoing-carrier boundary

**Conditional research analysis at input `917d8992654b2950883f06dc4759da9dd290966a`.** This uses the first-arrival and original-key geometry in `native-port5-cone-reduction.md`. It computes the conditional fibre law implied by that geometry; it does not compute the full native operational carrier at time H or supply two selectable measurements.

## Fixed variables and protocol guard

Keep the same native update, source geometry, prior scope and prospective horizon `H=L+79`. Write κ for the original-time triple at `(0,S+H,0)=f5(H)`, avoiding confusion with the acceptance pool integer K_acc. Let C collect **all other original-time variables**, with their inherited source/readiness correlations. The masking premise is

`Pr(κ=k | C=c)=1/8`

for every positive-mass c and all eight raw triples k. It must be retained as an explicit source/prior hypothesis, not deduced from a late-slice marginal.

Let W be all permitted records through H **except** the potential raw port5 symbol Y at H. This includes old q9 at L, the stipulated V read at L+2 where applicable, every earlier raw port record, timing and every success/failure flag. The cone reduction proves W is κ-independent as a deterministic function: `W=w(C)`. It does not assert that its components are mutually independent. The original source law may correlate them.

Let D be the read-enabled indicator determined by the past record. An earlier terminal failure has D=0 and remains terminal. The actual protocol record is

`Y_obs = Y if D=1, and bottom (no attempted read) if D=0.`

The native field at H may still be mathematically defined on failure trajectories, but this does not execute a read or offer a new carrier. All conditional formulas below apply only to positive-mass branches; no zero-mass history is normalized.

The unique axial source proof supplies a permutation f_c of the eight κ values for every fixed c:

`Y=f_C(κ).`

Neither its permutation property nor the previous 78-step checker computes f_c from an observer's public record. Most of C is private.

## Exact record/key posterior

Fix a positive-mass record w and write μ_w for the conditional law of C given W=w. Since W depends only on C, κ remains uniform and independent of C on this branch.

On an enabled branch D(w)=1,

`Pr(C in dc, κ=k, Y_obs=y | W=w) = μ_w(dc) * 1[y=f_c(k)] / 8.`

Summing k gives

`Pr(Y_obs=y | W=w)=1/8,`
`Law(C | W=w,Y_obs=y)=μ_w.`

Thus the new symbol provides no additional information about **any** variable determined by C, even one not already present in W. This is stronger than testing a selected moment, but it is still a statement about the marginal/past, not a carrier law.

The key posterior is different:

`Pr(κ=k | W=w,Y_obs=y) = μ_w{c : f_c(k)=y}.`

Consequently it is incorrect to conclude “the key is not disclosed” from uniform Y. Conditional on C=c, the inverse κ=f_c^{-1}(y) is exact. For an observer knowing only w, an inverse exists only if this posterior is concentrated. Uniform endpoint statistics permit either extreme:

- If f_c is the same known permutation on a record fibre, Y reveals κ completely.
- If private c selects balanced translations, the posterior of κ can remain uniform after Y.

A public key-decoder g(w,y) exists exactly when, for every positive-mass enabled (w,y) branch, `f_c^{-1}(y)=g(w,y)` for μ_w-almost every c. The reduction does not establish this record-fibre constancy. The chronological bank inverse of `history_v9` conditions on the whole private bank-complement C0; its existence is not permission to replace C0 by the public transcript.

On a terminal branch D(w)=0, only bottom is recorded and

`Pr(C in dc,κ=k,Y_obs=bottom | W=w)=μ_w(dc)/8.`

No new conditioning of the initial key or remaining state occurs from a read that was not attempted.

## A newly proposed acceptance flag is a separate native input

The old read-enable D is not the missing post-read acceptance predicate. If a later construction supplies an actual native binary flag A=alpha(C,W,Y), its complete joint law on an enabled branch would be

`Pr(A=a,Y_obs=y | W=w) = (1/8) * integral 1[alpha(c,w,y)=a] d mu_w(c).`

Both a=0 and a=1 remain in the record, with their physical carrier states. Conditioning on A=a reweights the c fibre by that indicator and can change its law; the unconditioned uniform-Y result does not justify erasing this selection. The fixed acceptance thresholds in the old phase are an abstract target, not a supplied native alpha at H. No new acceptance flag is invented here.

## Why “recover s” is already settled but the physical operation is not

The old whole-q9 record at L contains s and r_old. Under the fewest-seed q10.A=s source law, s is therefore already a function of W on the declared accepted phase. Asking whether the later transcript can determine s is vacuous. In particular `I(s;Y_obs | W)=0` would hold merely because s is recorded, even without the independent-pad hypothesis.

That does not physically deliver s to a private operand, implement the acceptance predicate or select a new measurement. The distinction is between observer-side stored knowledge and an actual native actuator/circuit acting on the correct carrier.

The fewest-seed laws `E=(1,1 XOR mY,1)`, `N=(mY,1,1 XOR mY)` are original source/preparation choices. Changing them is not an independently selectable setting on one fixed preparation. q10's B/D fields and the other physical masks must remain part of any carrier audit.

## Full microscopic outgoing cut: a diagnostic, not an operational instrument

Declare the full global two-slice cut

`C_H=(U_H,U_(H-1))=G_H(C,κ).`

The native second-order update has the inverse already stated in the source. Hence G_H is injective on the prior support: this full mathematical cut retains the original κ, s and every other original variable. Global inverse reconstruction does not make these values publicly readable or locally available.

On an enabled branch, the full conditional joint law is the pushforward

`Law(C_H | W=w,Y_obs=y) = (c -> G_H(c,f_c^{-1}(y)))_# μ_w.`

On a terminal branch it is the pushforward of `μ_w x Uniform(8)`, with no new read. This formula is an exact reduction of the joint-kernel problem, not its native operational evaluation: the actual private-background-dependent f_c and the physically relevant quotient of G_H still have to be specified.

The raw endpoint Y is a coordinate of C_H. Its uniformity cannot imply independence from the full outgoing cut. Indeed, on each enabled fixed-c branch it is a uniform deterministic function of that cut, and the joint law differs from the product law by total variation 7/8. Thus “uniform outcome, therefore unchanged or independent outgoing carrier” is false. Conversely full microscopic correlation does not itself refute an operational interface: a justified quotient may discard irrelevant degrees of freedom. That quotient cannot be chosen ad hoc to hide a failed carrier test.

## Existing operational target and the present stop

The retained `shared_v12/INTERFACE-CONTRACT.md`, “Fixed post-X target and physical acceptance gap”, specifies a phase-specific target at L+2: actual s, six fresh pool bits, K_acc, the acceptance thresholds (5,0,4,1), full accepted mask weights 5:4:1 and all failure branches. It explicitly requires a later stage to transport or re-encode the carrier over its latency. The route-v13 source variant does not inherit Native A's six-bit pool unchanged.

No maintained source here supplies a corresponding operational carrier dictionary at H=L+79, its reusable boundary, or two physically selectable setting maps acting on that same source/preparation. The full-cut diagnostic cannot fill those missing fields by itself.

The next useful question is therefore: **which fixed, source-compatible operational carrier should the port5 record update, and can its joint conditional law be derived from the fibre formula above?** Pin that target/quotient and actual allowed operation before evaluating a carrier marginal. If a proposal instead asks only for observer-side s recovery, the old record already solves that bookkeeping question and the proposal does not advance native measurement sourcing.

## Source anchors and bounded controls

At the input snapshot, the relevant retained sources are under
`verification/programmes/oi-qm/reconstruction/native-y-continuation-20261024/`:

- `shared_v12/INTERFACE-CONTRACT.md`: native rule; old q9 record; pool assumptions; selected target; terminal failures and joint record/carrier requirements.
- `native_decode_v14/REPORT.md`: fewest-seed q10.A=s source law; private q10; B/D correlations; absence of a read/post-read/reusable boundary.
- `history_v9/REPORT.md`, “Joint chronological permutation proof”: conditional bank inverse and public-noise law; “What follows for resources” limits that law to bank-complement quantities and warns against extending it to an outgoing neighborhood.
- `native-port5-cone-reduction.md`: later source geometry and the κ-independence of W.

Run `python3 -I -B native_port5_fibre_probe.py` and repeat with `-O`. The finite checker tests all64 translated native one-step permutation contexts (512 joint rows), exact singleton key fibres conditional on private context, a must-reject record/full-state independence test with TV7/8, two opposite key-disclosure countercontrols sharing a uniform public marginal, and a context-measurable terminal guard with retained mass and no attempted terminal read. Its synthetic enable flag tests the algebraic guard, not the native failure probabilities. None of these finite controls is a native78-tick replay or a computation of f_c over the actual large original prior.
