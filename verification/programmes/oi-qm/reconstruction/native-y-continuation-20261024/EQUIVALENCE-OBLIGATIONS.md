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
`e46d30fdd2c237b70ee7569f0044f2486f07f8ce`.

The finite calibrated menu and its supplied probabilities are a restricted
instrument target. They are not the full quantum state space. A1 (exact
equivalence on the specified full target) and A2 (a stated operational error
bound on a specified protocol class) require separate verdicts. A theorem for
one finite depth is not an arbitrary-depth theorem, and a family of finite
approximations is not an available exact limiting operation.

## Division of responsibility

| Track | Owns | First decisive obligation | Does not establish by itself |
| --- | --- | --- | --- |
| Native measurement and reset (#910) | Actual lattice construction, resources, diagnostic interventions, full record/carrier law | Starting from the actual corrected q7/q8 neighborhood, produce the calibrated post-Y carrier with every failure branch accounted for | Full state space, calibration selection, arbitrary menu/depth or composites |
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
   and W-modified public histories need a new joint-law audit.
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

- [#911](https://github.com/amaybaum/incompleteness/pull/911), `81bc53e482158072869b916116a4fc0f8b28f99e`: separate-author review accepts the almost-sure irrational sampler and its joint timing diagnostic within scope. The fixed pointwise/G3 operation invariant remains; an enlarged fair reservoir alone does not source A1. Prior finite-resource results remain unchanged.
- [#912](https://github.com/amaybaum/incompleteness/pull/912), `7be889a88987cb0a4ab248b3787982958fca1a97`: separate-author review accepts the actual native-X finite success/failure kernel under inherited source hypotheses. Terminal-metadata plus unchanged-carrier reuse fails joint TV and positivity checks. This does not refute the original terminal-only claim or simulate later native ticks. Prior conditional-composition theorem remains unchanged.
- #910: separate-author review accepts reset_v8 author revision `e46d30fdd2c237b70ee7569f0044f2486f07f8ce`, giving q8=(0,y,0) using two additional initial sources and the actual coupled origin/W front. The arbitrary late-q7 socket remains excluded. The earlier one-source obstruction remains intact. Calibrated native reset and the W-modified public-history law are open.

Next first check: establish conditional resource independence for the W-modified
public history, then construct the calibrated native reset and prove a valid
joint post-read carrier law including metadata and failures. This is a local
instrument task; A1 identification/coverage and composites remain separate.
