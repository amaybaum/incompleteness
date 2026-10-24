# Parallel equivalence investigations

Research synthesis for 24 October 2026. This is a coordination supplement for
the native-Y continuation, not a replacement for the programme owner's index.
No physical premise, target extension, F/E designation or manuscript status is
adopted here.

## Common target and evidence boundary

The source synthesis is `INTEGRATION.md` on #885 at
`2d555f17c23bea31d32b3f5eb4c49d245b413a76`, under
`verification/programmes/oi-qm/reconstruction/research-planning/missing-component-20261020/`.
That source is read-only for this effort. The native-Y source is #910 at
`328b74b88eaeddc798bf4693af78a571bf429787`.

The finite calibrated menu and its supplied probabilities are a restricted
instrument target. They are not the full quantum state space. A1 (exact
equivalence on the specified full target) and A2 (a stated operational error
bound on a specified protocol class) require separate verdicts. A theorem for
one finite depth is not an arbitrary-depth theorem, and a family of finite
approximations is not an available exact limiting operation.

## Division of responsibility

| Track | Owns | First decisive obligation | Does not establish by itself |
| --- | --- | --- | --- |
| Native measurement and reset (#910) | Actual lattice construction, resources, diagnostic interventions, full record/carrier law | Starting from the actual corrected q7/q8/q9 neighborhood, produce the calibrated post-Y carrier with every failure branch accounted for | Full state space, calibration selection, arbitrary menu/depth or composites |
| States and dynamics (#911) | Exact target, representation map, preparation/operation availability and structural obstructions | Identify precisely which assumptions obstruct A1 and whether the native route changes any of them | Native implementation of a mathematically representable channel |
| Composition and access (#912) | Conditional composition theorem, observable history, adaptive choices and composite-system boundary | State sufficient local contracts and prove their finite-depth consequence; exhibit controls for weaker inadequate contracts | Satisfaction of those contracts by the actual lattice or a tensor-product/Bell reconstruction |

Each track uses a disjoint directory and its own forward checkpoints. Reviews
remain with the result they inspect; they do not create separate PRs. Draft
publication is not adoption or durable evidence on main. Before landing any
claim, its required source and executable evidence must be reachable from main
under AGENTS §A.42.

## Shared contracts

1. **State and operation map.** Specify the source preparations, allowed
   protocols, target states/instruments and correspondence. Distinguish a
   representation from a physically available preparation or operation. If
   equivalence is claimed, provide both coverage of the target and preservation
   of all permitted source observations.
2. **Measurement boundary.** The clean native q7 code is `(0,0,y)` at `R+7`.
   It is clean on the retained native family; it does not supply an arbitrary
   late-time input socket. The actual previous slice and neighborhood are part
   of the downstream initial-value problem. The workspace-assisted q8 route
   gives (0,y,0) on the native family; its arbitrary q7 socket still fails,
   and W-modified old-port noise is now controlled by the conditional
   history_v9 theorem. The actual full outgoing boundary remains a separate
   problem. The next initial source gives q9=(0,y XOR a,y XOR a),
   still one sign rather than a simultaneous calibrated carrier.
3. **Post-Y target.** The outgoing carrier must decode to
   `(y XOR a, y, y XOR b, z)` with `(a,b)=00,10,11` in ratio `5:3:2`
   and fresh fair `z`. This calibration is supplied, not derived. The decoder
   must be native to the next stage's interface, without history-dependent
   interpretation smuggled into that stage.
4. **Joint law.** Keep public records, heralds, timing and outgoing carrier in
   the same law; retain failures. Conditional freshness is relative to the
   entire relevant earlier history, not only an unconditioned initial prior.
   A terminal R read is needed beside X→Y→X to detect the known swapped-weight
   calibration counterexample.
5. **Access and preparation.** List every private field, allowed read and
   timing restriction. The q7 prefix `(u,u,1)` remains informative. Initial
   ready regions, seed correlations, new independent banks, clock and settings
   are explicit resources. None is silently derived from the local update.
6. **Composition.** A proof must preserve its interface invariant after each
   branch. If it needs equality of hidden states, justify that requirement;
   a sufficient operational equivalence relation may be weaker. Multi-system
   composition needs an additional operation/state correspondence and cannot
   be inferred from a one-carrier sequential theorem.

## Integration gates

The structural audit has priority for A1 viability. A blocked A1 architecture
does not refute OI generally or a separately specified A2 claim. Native reset
work can still settle the finite instrument obligation without settling A1.

A candidate result enters the combined handoff only with its explicit
assumptions, proof or replay command, scope, source revision and separate-author
review status. A computational diagnostic does not certify a universal theorem.
Only accepted scoped findings are offered to the #885 owner for synthesis.

Open broader obligations remain: calibration selection; native preparation,
clock and settings; access closure; unrestricted depth and menu; composite
systems and Bell structure; exact state/operation coverage. This document does
not declare any of them closed.

## Reviewed parallel checkpoints

- [#911](https://github.com/amaybaum/incompleteness/pull/911), `81bc53e482158072869b916116a4fc0f8b28f99e`: unchanged reviewed almost-sure sampler and joint timing diagnostic. The fixed pointwise/G3 operation invariant remains; fair-reservoir enlargement alone does not source A1.
- [#912](https://github.com/amaybaum/incompleteness/pull/912), `69540662b234e37c6805ded244962a80f15f63a2`: reviewed tagged-post-Y comparison and terminal-R positivity countercontrols. A fixed global history decoder is algebraically possible; strict raw encoding still fails for that standalone gadget and no relaxation is adopted. Independent resampling is an abstract positive control, with native reset/closure open.
- #910 history author `96e7b6249eedc221a364b79d996a080f0b850438`: separate review accepts the seven-port noise/complement theorem through R+8. Independent reviewer geometry extends it through R+9 under 189 supplied post-R fair bits.
- #910 masked-route author `328b74b88eaeddc798bf4693af78a571bf429787`: separate review accepts the original-time J source and pointwise q9=(0,y XOR a,y XOR a) identity, retaining actual boundary values and the failure of arbitrary q8 socket targets. The combined conditional fresh-bit/noise corollary is separately stated in reset_v9/review/COROLLARY.md.

The old noise law is controlled under its explicit bank/access assumptions;
it does not give an independent entire two-slice neighborhood. Next construct
simultaneous retained-Y, X-mask and R-mask branches, then z and a synchronized
herald, with the exact joint 5:3:2 law and every failure branch. Each new
source/readiness region must preserve the bank and conditional seed law.
A1 correspondence/coverage, native preparation/clock/settings, arbitrary
protocol closure and composites remain separate obligations.
