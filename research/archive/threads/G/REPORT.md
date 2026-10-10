# Thread G — Effect-family reconstruction (P2/O1): report

Written by the coordinating session from the thread's returned report (the harness refused report files from the
subagent). Content is the thread's; the verification section at the end is the coordinator's.
Sources: NOTES.md, g_controls.py (exact arithmetic; `OK -- 50 checks, 17 written notes`; sha256 240ee0fa…332550).

## Answer
No canonical, representation-independent effect family E_OI is constructible from landed machinery; P2 stays open.
The missing principle is an effect-generation theorem, not geometry: every relative-boundary state of Ω∞ must be made
certain by carrying a native sharp readout through available non-classical reversible operations (system + register,
then discard), with limits. In the matrix regime (imported ℂ) this is a landed theorem given `DrivesElementary` plus
the D3 limit closure. In the field-neutral vocabulary it cannot be stated: KInfFoundations has no composite system,
register readout or transport of effects. The only alternative is to postulate "no restriction" for Ω∞.

## Candidates and verdicts
| Candidate | Verdict | Reason |
|---|---|---|
| C1 response effects of one fixed finite ontic realization | INSUFFICIENT | fails on the tight SIC ball (F2, Thread F CM-SIC) and the loose SIC ball; no closure repairs it |
| C2 a finite stage's table under mixing/complement/coarse-graining | INSUFFICIENT | triangle stage: edge midpoint unsupported (δ = 1/4); KInf1 vacuous on stages |
| C3 C1 closed under pullback by the drive group | INSUFFICIENT (realization-dependent); also BLOCKED on K∞-R | loose SIC fails; bidisk realization R1 fails (δ = 1/22) |
| C4 limit over a refining family of realizations | BLOCKED | needs a refining-realization theorem; the region limit does not refine (`inclObs`, RegionLimit.lean:102); Main.md:538 fixes the realization |
| C5 union of responses over all realizations | BLOCKED | SEC on every compact convex body (written), but nothing in OI sources a union over realizations |
| C6 no restriction (`fullEffects`) | BLOCKED | restates the target; Main.md:540: no fixed realization supplies it |
| C7a substratum-class effects | INSUFFICIENT | diagonal only; supports only the Bloch poles |
| C7b quantum-architecture effects | DERIVED, matrix regime only | `genTheory_qm_of_quantumArchitecture` (SubstratumSource:136); imports ℂ, needs `DrivesElementary` |
| C7c fixed-gate theory effects | INSUFFICIENT without D3; DERIVABLE with it | BLOCKED on adopting D3 (`ClosureAvail`, DiscreteCompletion:63) |
| C8 native readout carried by the drive | BLOCKED | needs composites, a native readout, drivability and covering of the boundary |

Best candidate: C8, the field-neutral analogue of the matrix Naimark route (`circuit_available`, OperationalAssembly:757).

## Key results
1. Closure stability (written; exact checks in section ONT). For a fixed realization p, Resp(p) is closed under every
   operation implemented on the ontic states (mixing, complement, coarse-graining, sequential instruments, conditioning,
   attach/stochastic map/readout/discard, copy, limits): each sends c to Mᵀc ∈ [0,1]^N. So the closure of operationally
   generated effects of one realization is Resp(p) itself.
2. Domination certificate (written; exact instances). If δ(1 − h(z)) ≤ 1 − h(x) for all h in a family and all states z
   with δ > 0, the inequality is affine in h and survives convex hulls, limits and δ-uniform pullbacks, so no closure
   contains a proper effect certain at x. For responses δ = minᵢ pᵢ(x). Exact criterion: for compact G, the G-closure
   of Resp(p) has SEC iff G·T(p) covers the relative boundary, T(p) = {points with some pᵢ = 0}. This makes Thread F's
   B9 covering hypothesis exact.
3. Representation dependence (exact). Same body, same group, opposite verdicts: tight SIC + SO(3) has SEC; loose SIC
   (t = 1/2) has δ = 1/8 everywhere. Bidisk R1 fails, R2 (a facet on a flat face) passes.
4. The drive is not implementable on the ontic states of a fixed SIC realization: p∘R_t∘p⁻¹ has negative entries
   (−2/5, −5/26, −10/101); the half-turn control is a permutation matrix as it must be.
5. Matrix regime: monomial (substratum) unitaries keep the Bloch z-axis up to sign, so the off-axis J clause fails,
   matching `substratum_residual` (StructuralClosure:383). Substratum effects are diagonal. The Naimark circuit gives
   V|0⟩⟨0|V†, diagonal for monomial V. Sharpness comes from the postulated native register readout (`readout_avail`,
   OperationalAssembly:642) carried by a driving operation.

## Surprising
- The landed fixed-gate theory fails SEC on the Bloch ball: `fixedGateTheory` (DiscreteCompletion:1926) is dense finite
  QM but generates only countably many effects (written, from `mixR_countable_upToScalar`, StateMixingCoupling:662).
  Limit closure is needed even in the matrix regime; that is D3, defined and deliberately not adopted (the module
  header: "dense availability is never identified with exact availability").
- The OI core does not determine P2: `substratumTheory` (RouteB:279) has diagonal effects only; `diagTheory`
  (DiagonalTheory:246) carries every sharp effect through measure-and-prepare instruments (checked exactly). Full
  effects do not need a drive; the drive is only the sole landed source of non-response effects.
- NB-1 needs more than SEC: K1 consumes the sharp effects (1 + b·r)/2 for every unit b (`lorentz_of_effects`,
  NativeGateBall:105); on the ball SEC only guarantees 1 − s(1 − b·r), s ∈ (0, 1/2]. A P2 discharge aimed at K1 must
  deliver sharpness, not support alone.

## 1. Effect-source inventory
| Source | Location | Maps to [0,1] | Canonical | Repr.-indep. | Functorial | Survives completion | Evidence |
|---|---|---|---|---|---|---|---|
| FiniteStage table | KF:63–84 | v ↦ v e | for the stage | n/a | no stage maps in kernel | design note only | kernel |
| Stage closure | none | — | — | — | — | — | absent |
| Response maps | KF:889–947 | c·q, c ∈ [0,1]^N | no | no | closed under ontic ops | ≤ N exposed points | kernel + exact |
| Unit | KF:69, :206, :234 | 1 | yes | yes | yes | yes | kernel, never proper |
| `fullEffects` | KF:149 | all affine [0,1] maps | yes | yes | yes | finite dim only | definition, unsourced |
| FiniteOperationalTheory | OA:594 | tr F_a(ρ) | parameter | — | coarse/bind/discard | — | kernel |
| Native readout | OA:642, `readout_is_localLuders` OA:658 | sharp register projectors | form derived, existence postulated | label-invariant | yes | X ↦ X⊗1 | kernel |
| Circuit / InstAvail / genTheory | OA:757, IL:268, IL:852 | V†(1⊗\|k⟩⟨k\|)V | given the class | `genFamily_relabelling` IL:893 | yes | no refinement (RL:102) | kernel |
| Substratum effects | RouteB:279, SC:180, IL:530 | diagonal | yes | yes | yes | yes | written + exact |
| Quantum-architecture effects | SS:136 | all quantum effects | given QuantumArchitecture | yes | yes | finite carriers | kernel (ℂ) |
| Fixed-gate effects | DC:1926, DC:1948 | countable, dense | yes | yes | — | only via D3 | kernel + written |
| `diagTheory` | DT:246 | all effects | countermodel | — | — | — | kernel + exact |
| Itinerary indicators | ObservabilityQuotient:270 | classical responses | yes | yes | — | — | kernel |
| Native gate ball | NGB:105 | consumer, not a source | — | — | — | — | kernel |
| Copy | `CopyNatural` KF:284 | a proposition about two NOTs; no copy operation | — | — | — | — | kernel |

Field-neutral sources: the stage table, the response maps and the unit (plus classical itinerary indicators). No
field-neutral module has a composite, ancilla, readout, conditioning or copy operation.

## 3. Control matrix
| | 3-ball | SIC tight / loose | Bidisk | Stages | Unit-only | Copy / attach |
|---|---|---|---|---|---|---|
| C1 | ✗ (F2) | ✗ / ✗ | ✗ (R1, R2) | trivially ✓ on simplices | ✗ | does not enlarge |
| C2 | — | — | — | ✗ (triangle) | ✗ | no field-neutral op |
| C3 | depends on p | ✓ / ✗ | ✗ R1 / ✓ R2 | vacuous | ✗ | drive not ontic |
| C4 | depends | depends | depends | — | ✗ | no OI family |
| C5 | ✓ | ✓ | ✓ | ✓ | ✗ | n/a |
| C6 | ✓ | ✓ | ✓ | ✓ | n/a | n/a |
| C7a | ✗ (poles) | n/a | n/a | n/a | ✗ | does not enlarge |
| C7b | ✓ | n/a | n/a | n/a | ✗ | the mechanism |
| C7c | ✗ / ✓ with D3 | n/a | n/a | n/a | ✗ | circuit |
| C8 | ✓ if transitive | ✓ | point-seed ✗ / face-seed ✓ | vacuous | ✗ | needs composites |

Every ✓ under C3, C5, C7b and C8 rests on an unsourced ingredient or a favourable choice of realization or seed, and
each has a ✗ beside it on the same body.

## 4–5. Representation independence; minimal closure
Response families and all their closures depend on the realization. The body-intrinsic candidates (C5, C6) are
realization-independent but unsourced. The matrix regime is functorial (IL:893) but imports the body; with substratum
effects the operational body collapses to a segment, so P1 depends on P2 there.
Closure provenance: mixing, coarse-graining, sequential composition, attach/readout/discard — matrix-only (OA:594,
IL:268); pullback by automorphisms — needs K∞-R; limits — D3 defined, not adopted. Ontic versions stay inside Resp(p).
The minimal closure that would work: D3 limits plus transport of a native sharp readout by non-ontic operations; it
succeeds exactly when Ḡ·T ⊇ ∂_rel Ω∞.

## Coordinator verification (2026-10-01)
- Identifiers checked at 6d0abf6b, each at the cited line: fixedGateTheory DC:1926; ClosureAvail DC:63;
  mixR_countable_upToScalar SMC:662; genTheory_qm_of_quantumArchitecture SS:136; circuit_available OA:757;
  substratumTheory RouteB:279; diagTheory DT:246; lorentz_of_effects NGB:105; inclObs RegionLimit:102;
  genFamily_relabelling IL:893; substratum_residual SC:383; response_eq_one_forces KF:899; readout_avail OA:642.
  DiscreteCompletion's header carries "dense availability is never identified with exact availability".
- g_controls.py re-run: identical output, `OK -- 50 checks, 17 written notes`.
- C7b pressure test: SS:136 concludes ExactAllFiniteEndomorphicQuantumOps from QuantumArchitecture, whose
  `drives : DrivesElementary` field is a hypothesis over ℂ matrix carriers. DERIVED holds only in that regime and
  presupposes the quantum body; it does not discharge field-neutral P2.
- Countability of fixed-gate effects is a written argument (from SMC:662), not a kernel theorem.
