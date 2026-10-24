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
`5f6786d6f02605f8e8821a536b678495e19015da`.

The finite calibrated menu and its supplied probabilities are a restricted
instrument target. They are not the full quantum state space. A1 (exact
equivalence on the specified full target) and A2 (a stated operational error
bound on a specified protocol class) require separate verdicts. A theorem for
one finite depth is not an arbitrary-depth theorem, and a family of finite
approximations is not an available exact limiting operation.

## Division of responsibility

| Track | Owns | First decisive obligation | Does not establish by itself |
| --- | --- | --- | --- |
| Native measurement and reset (#910) | Actual lattice construction, resources, diagnostic interventions, full record/carrier law | Starting from the actual corrected q7 neighborhood, produce the calibrated post-Y carrier with every failure branch accounted for | Full state space, calibration selection, arbitrary menu/depth or composites |
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
   of the downstream initial-value problem.
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

- [#911](https://github.com/amaybaum/incompleteness/pull/911), `2f09be040b12c894e28bafd46bd82fcb724c68f6`: scoped sourcing audit and abstract finite-resource sampler accepted by separate-author internal review. The illustrative 5/16 sampler benchmark needs six fair bits covering all conditional randomness and uses three blank label bits; it is not a native reset.
- [#912](https://github.com/amaybaum/incompleteness/pull/912), `5b57321a39525ccd486560628a10ecedefb8dc65`: conditional finite-depth composition proof and exact countercontrols accepted by separate-author internal review. Actual native application, composite systems and full target coverage remain open.
- #910 retains the clean q7 readout. The next-tick `reset_v7` checkpoint computes its actual incoming neighborhood and excludes the tested one-source outward routing family; separate-author internal review accepts the exact family at author revision `f7058d59ea2136601a679a7fdd7b7573b1e4bfa7`; native reset and joint-history certification remain open.
