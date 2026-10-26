# OI Native-Y: Parallel Continuation and Session Handoff

24 October 2026 | Repository-read-only research | Version 3

## Parallel continuation: outcome and status

The native-Y problem is now a concrete junction problem. We have an actual nearby x register, a clean A-extraction gadget, and a standalone direct-reset apparatus. We do not yet have one compatible native construction joining the actual late Y phase to either gadget.

Four avenues and an independent review were run in parallel. All repository activity remained read-only. No physical premise, tagged-encoding relaxation, or certification claim was adopted.

| Avenue | Established result | Remaining boundary |
| --- | --- | --- |
| Auxiliary routing | 5-tick native extractor: Q=(A,B,D) -> (0,A,0) | Specified ready input cone; actual late splice fails a readiness condition |
| History control | Nearby native x at s,R+1, with blank prefix through R | Earlier slice of phase; not persistent memory or an implemented gate |
| Direct reset | Standalone native 5:3:2 candidate at tick 2700 | Late socket unbuilt; common raw encoding still fails |
| Other geometry | Actual q3=(u,xu,u); exact 13-triple recurrence | Third straight step supplies no new raw Y operand |
| Independent review | Separate local proofs, geometry and contract checks | General transport-proof review remains open |

### Recommended next milestone

Construct one native junction on the actual two-slice state near q2. It must use the arriving A operand, handle the neighboring fields as they actually are, and deliver a common usable carrier interface. Add resources only at the original initial time, independently of the unknown input.

The strongest candidates are a tolerant variant of the five-tick extractor, or a coupled update using the nearby previous-slice x. The standalone direct reset is a downstream target, not a license to reload the late state into a clean apparatus.

Status: research checkpoint with scoped independent review. Exact-QM reconstruction and the wider finite-precision OI programme remain distinct. Failure of one gadget family is not a no-go for OI.

## Actual apparatus: nearby history and the next step

### Native x is already adjacent

```text
s = qY + (0,-1,2)
U_(R+1)(s) = (0, 1 XOR y, x),  y=x XOR u
U_t(s) = 000 for every t <= R
```

At phase time R+2, this D=x occupies the previous slice one spatial step from the current q2.A=y. It uses the inherited depth-two construction and consumes no new initial seed or frontier coordinate. Long historical transport is therefore unnecessary merely to locate x nearby.

Replacing qY.D by diagnostic p at R leaves this sidecar unchanged, while q2.A becomes p. The sidecar B remains 1 XOR native y; it cannot substitute for the actual operand. The next current sidecar value can depend on the old input and frontier symbols. This is local phase availability, not persistent storage or permission to read indefinitely.

### The third outward step is exact but not useful as a clean socket

```text
q3 = qY + 3e_z
U_(R+3)(q3) = (u, x*u, u)
Early prefix at R-3: (u,1,u)
```

A closed recurrence on thirteen triples has exact pulse periods 3600 and 2940; the actual R has remainder 253 in both. All 1,479 original source positions were checked for the enlarged receiver. The result is not extrapolated from a small simulation or from R modulo 12.

The 96 site-times in the shrinking diamond give 576 field/complement candidates. Across all 32 diagnostic assignments, only the already known qY.D and q2.A equal p uniformly. This bounded census excludes neither other geometries nor new controls.

The depth-three ready extension preserves the inherited frontier separation. If seven old public ports remain exposed through R+3, the inherited joint-frontier theorem requires 21 more preloaded fair bits beyond R+2, or 63 beyond R. The informative q3 prefix remains private under the supplied access convention.

Evidence: history_control/REPORT.md and checks.py; new_geometry/REPORT.md and checks.py; independent review sidecar_check.py and geometry_check.py. Wider transport and access closure are not established.

## A genuine five-tick extractor, with a failed splice

For arbitrary Q=(A,B,D) localized once at the gadget origin, the unchanged native rule produces the complete output (0,A,0) at r=(3,2,0), tick 5.

| Initial current site | Triple |
| --- | --- |
| (0,0,0) | Q=(A,B,D), unknown |
| (0,1,-1) | 010 |
| (1,1,-2) | 111 |
| (8,2,0) | 010 |

Prepare the current Manhattan ball B5(r) and previous ball B4(r), zero except for the listed sources. The old input triple lies outside B4(r) and remains arbitrary. The ready region fixes 1,077 apparatus bits, independently of Q. All exterior coordinates may be arbitrary.

```text
Receiver prefix: 000 for ticks 0..4
Receiver at tick 5: (0,A,0)
```

All four sources lie on the first-arrival boundary. An exact eight-input shell certificate gives incoming argument (1,0,A) before the correcting source. Its isolated contribution 100 changes that to (0,0,A), whose H-image is (0,A,0). Independent native recursion and the shell calculation agree.

A-only diagnostics pass with B,D fixed. Full 15^3 torus tests cover all eight inputs and two dense exteriors; reversing all five updates restores the complete initial phase. Information is retained globally, but no reusable single garbage register or restored ready workspace is claimed.

### The actual late phase violates a required zero

```text
At q2+e_x, tick R+1:
    actual old triple = (0, 1 XOR u XOR mY, mY)
```

A direct translation of the extractor to q2 at R+2 requires that previous-slice triple to be zero. With Q=001, the clean gadget outputs 000; changing only that old neighbor to 010 changes the result to 010. This is a controlled counterexample to ignoring readiness, not a full simulation of every possible integration.

Evidence: aux_routing/REPORT.md, checks.py and source provenance; independent review/gadgets_check.py. A smaller two-tick B-copy was rejected because it fails the actual-A diagnostic.

## Direct reset: standalone native candidate and tag

### Native fanout and mixing

```text
M_a(A,B,D) = (A XOR a, B, D XOR a*B)
M_a(M_a(Q)) = Q
```

For any positive L divisible by 12, place Q once at the origin and pure-A seed sources at +/-2L e_x. Prepared first-arrival receivers at +/-L e_x produce M_a(Q) and M_b(Q); a receiver at L e_y receives Q. The old input triple is outside their previous-slice cones. These formulas respond to arbitrary A, not just A=B on native inputs.

### Compiled native herald

A new herald accepts counts 5,3,2,0 on fresh seed pairs 00,10,11,01. Its unpadded register word has length 2,684; the synchronized deadline is L=2,700. There are 7,832 affine source entries, checked against every receiver. The complete 2,700-step native wing/axis recurrence yields raw herald (0,G,0), with 10 of 32 seed settings accepted.

| Branch | Probability | Offered carrier |
| --- | --- | --- |
| Success | 5/16 | Supplied Y plane weights 5:3:2; independent fair Z |
| Failure | 11/16 | No offered carrier; Y and herald record retained |

Herald and Z are remote, with compatible initial ready cones. Six fresh fair seed bits, including Z, are independent of Q and prior history. The five receiver prefixes are blank. No unknown input copies are preloaded. This proves a standalone prepared apparatus, not its embedding into the actual late q2 phase.

### A public-history tag remains in the raw output

```text
Input C = (y,y,1 XOR x*y)
Mixed cell = (r,y,1 XOR x*y XOR (y XOR r)*y)
Fixed tag extraction: g = D XOR 1 XOR A*B XOR B = x*y
```

Each whole terminal cell reveals only its designated new sign plus public history. Nevertheless, at y=1 the entire raw-output distributions for x=0 and x=1 have disjoint supports: TV=1. The unchanged common raw-carrier requirement therefore does not pass. The tagged interface is a candidate, and no relaxation has been adopted.

Evidence: direct_reset/REPORT.md, checks.py, herald.json and copied compiler provenance. Full readiness and source ownership are part of the standalone theorem; old-apparatus frontier compatibility is still unproved.

## Joint-law accounting and what can be combined

### The tagged terminal law is exact

```text
Pr(success, raw=E_(x,y)(j) | x,y) = (5/16) * mu_(Y,y)(j)
Pr(failure, no carrier | x,y) = 11/16
```

E_(x,y) is an injective, history-indexed encoding of the four-sign target carrier. The complete raw distribution is checked, including every failure. This is an information contract for a candidate interface; it is not acceptance under a history-independent physical encoding or a proof of native reuse.

| Event or diagnostic | Exact value |
| --- | --- |
| Both new reset heralds succeed, conditional on earlier x | 25/256 |
| Including older independent 5/8 predecessor | 125/2048 |
| 5:3:2 versus 5:2:3: terminal R TV on second success | 1/10 |
| Same R TV including second failure | 1/32 |
| Same R TV including preceding 25/128 success | 25/4096 |

These sequential rates compose supplied independent kernels. They are not success claims for an integrated native X->Y sequence. Reusing the first-reset sample makes X_new=x and fails the fresh post-Y law. Terminal X alone misses the swapped calibration; terminal R and the full carrier are required.

### Compatibility findings

The nearby x sidecar belongs to the actual inherited phase. The extractor and direct-reset apparatus start from specified ready sockets. Their separate proofs cannot be concatenated by relabeling the encounter time as a fresh initialization. The extractor has a concrete dirty-neighbor obstruction, while the direct candidate additionally retains a history tag.

The previous twenty-entry boundary repair remains excluded: on y=1 its whole output always satisfies B XOR D=x, even with history-dependent control choices. This obstruction is informationally harmless after x is public, but prevents a clean Y-only triple in that family. It does not exclude larger native junctions.

Future native operations can react to the retained tag. A tag-conditioned R flip can change agreement from 4/5 to 1/5 despite a correct terminal decoded reset. Proving that the next allowed instrument has the required law is therefore essential.

Evidence: integration/tagged_contract.py and REPORT.md; direct_reset checks; independent review. Joint frontier independence, clocks, shutters and arbitrary observer access are not inferred from these terminal laws.

## Session handoff: review, replay and next work

### Independent review and evidence boundaries

The separate reviewer accepted, within stated scopes, the v2 reversible maps and boundary obstruction, the native x sidecar, the five-tick extractor and dirty-socket counterexample, the native mixer/fanout identity, the source-defined 2,700-step herald, the extended third-step calculation, and the tagged-law/strict-encoding distinction. Review reports and exact examined-byte hashes are retained in review/. This is not formal Lean certification or closure of the wider transport-proof review.

Author checks and parent normal/-O replays cover all four avenues. The reviewer independently evaluated all 7,832 herald sources by shortest-path parity, all 2,700 native axis steps, all 32 seeds, source rank and receiver ownership. This validates this source-defined herald instance under its clean cones, not a general compiler theorem.

### First task for the next session

Calculate a complete junction using current q2 and the adjacent previous-slice x at s, or synthesize a tolerant extractor using the actual neighboring fields. Start with s at R+3 as a concrete candidate, but include all five other current neighbors and lower-source behind-front contributions. The previous first-arrival-only formula is insufficient there.

Before counting a solution, specify all added pins and seed correlations at the original initial time; preserve the existing frontier bank; test actual operand interventions; prove full prefixes and the joint record/carrier law; retain every failure; and physically separate the history tag or meet the unchanged common carrier criterion. Do not adopt a new access convention or tagged-encoding relaxation silently.

### Portable handoff contents

- START-HERE.md: status, reading order, next task and exact replay commands.
- parallel_v3/: four avenue reports, independent review, parent contract, checkers, retained outputs and provenance.
- dependencies/: unchanged v1 and v2 source bundles, pinned by SHA-256.
- replay.py and SHA256SUMS: fresh extraction, hash verification and normal/-O replay. Python standard library suffices for scientific checks.

```text
python3 replay.py
python3 replay.py --baseline
```

The default replay checks the new checkpoint and v2. The --baseline option also runs the ten retained v1 checkers. No network or repository actions are needed. Reports identify copied proof components and which review was independent. The PDF is a combined guide; the detailed per-track reports and executable evidence control technical scope.

Unresolved: actual junction, common reusable carrier, native Y sequence, broader transport review, initialization, clock/settings/access closure, probability selection, unrestricted depth/menu and composites. These remain open research obligations, not adverse conclusions about OI generally.

