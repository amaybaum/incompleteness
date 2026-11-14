# SEL-DISC-1 — A target-neutral information test, and the remaining native selection gap

**Status:** Accepted at the bounded paper-review scope recorded in [STATUS.md](STATUS.md); documentary integration remains draft. Paper-only hand argument and source audit; no scientific execution or adopted physical premise.

**Writer:** Codex, 2026-11-13. **Accountable issue:** [#1143](https://github.com/amaybaum/incompleteness/issues/1143). **Authority:** [owner handoff 6863602000](https://github.com/amaybaum/incompleteness/issues/1143#issuecomment-6863602000), coordinated by [#1169 comment 6863608722](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-6863608722). **Main source pin:** `c3b5f37a354bb26437e2e0165c576a347a63c153`. Proposed new repository directory: `verification/programmes/oi-qm/reconstruction/selection-discriminator-20261113/`.

## 0. Decision at the actual scope

The reviewed weak observer/record conditions still admit the reversible PR countercontrol. Extending no-signalling to complete histories rejects its **same-seed reused implementation only when that reuse is available**; it does not reject the accepted fresh-cell implementation.

A more discriminating, target-neutral **conditional test** is available: two independent input bits, one requested input index, one use of the device, and one explicitly transmitted classical bit. Require the two indexed recovery informations to sum to at most one bit. The accepted PR table permits perfect recovery of either requested input bit and gives a sum of two. Classical local models and standard quantum local instruments with shared entanglement satisfy the one-bit inequality. Proofs appear below.

This is the smallest binary random-access test considered here, **not a proved smallest physical restriction**. The information inequality is a standard information-causality condition, not a new OI theorem. Neither its derivation from OI nor the physical availability of its message/input/control protocol is supplied by the recovered sources. The one-bit message budget is an **operational communication budget**: it does not bound ontic information transfer through the globally coupled PR update. No new premise is adopted.

**Verdict:** conditional exclusion plus a precise unresolved source/discriminator gap. This unit establishes no OI-sourced selector. This is not a proof that no such selector exists, that information causality characterizes the full quantum set, or that the source gate has passed. The next obligation is a native availability-and-information argument independent of the PR or quantum target table.

## 1. Exact accepted evidence and status boundaries

| Input | Exact scientific artifact | Review evidence and scope |
| --- | --- | --- |
| SEL-ACCESS-1, #1224 | Head `1b966a0383e1dabe867d41816ee9743e99502938`; `verification/programmes/oi-qm/reconstruction/oiqmsel-access-20261110/SELECTION-ACCESS-1.md`; blob `5c125be576fd9552acabe891ff851fa19046fc3a` | [Full review 5840425454](https://github.com/amaybaum/incompleteness/pull/1224#pullrequestreview-5840425454), ACCEPT WITH NITS at the preceding `ea8827ff6b4c3e405310216c75bcc32157d069bb`; [focused review 5840851253](https://github.com/amaybaum/incompleteness/pull/1224#pullrequestreview-5840851253), ACCEPT at the listed corrected head. Conditional passive-menu obstruction; actual executable repertoire remains unsourced. |
| SEL-EXCL-1, #1228 | Scientific head `0ecfddeb89540aedf1e2dc3ae7c377516641066c`; `verification/programmes/oi-qm/reconstruction/oiqmsel-exclusion-20261110/SEL-EXCL-1.md`; blob `1e8892ff94a8f0dcf306e3f43cd57e951a446ca7` | [Full review 5845436861](https://github.com/amaybaum/incompleteness/pull/1228#pullrequestreview-5845436861), ACCEPT WITH NITS at `4813bc0b04548248581a137c88d43a64d73bd1a9`; [focused review 5848321039](https://github.com/amaybaum/incompleteness/pull/1228#pullrequestreview-5848321039), ACCEPT at the listed scientific head. Specified reversible globally coupled model, finite fresh-cell protocol and separately enlarged same-source protocol; no native apparatus. |
| #1228 documentary descendant | Current recovered head `756811051bbc0670714f4d77d62339c12adaba34`; same path, blob `7811e4493ab471b9e968483c9d18de4a5756de43` | [Independent Claude focused documentary review, comment 6846240488](https://github.com/amaybaum/incompleteness/pull/1228#issuecomment-6846240488), **ACCEPT** at this exact head, 2026-11-13T06:46:27Z. It verifies the six-line antecedent/status correction with the mathematical core unchanged. This report retains the earlier accepted scientific source; documentary acceptance is not physical-source or integration approval. |
| #1169 synthesis r3, #1276 | Head `9eeee392fcfe7489fab3e007d95488ecf4a3eb13`; `verification/programmes/oi-qm/reconstruction/drafts/synthesis-1169-20261113/SYNTHESIS-r3.md`; blob `e68295098577f4ec28cdc52726e83395deee915f` | `CONFIRM-r3.md`, blob `e420539ac312c6a4ebefa44d2cb31112fc6ce2c5`, records the focused non-author confirmation; [ChatGPT review 5896999231](https://github.com/amaybaum/incompleteness/pull/1276#pullrequestreview-5896999231) ACCEPT at this exact head. Bounded synthesis, not an independent rederivation of all inputs. |

The saved review bodies are relayed non-author agent receipts, not author corrections counted as review. Source-file headings that still say “focused review pending” are historically stale at the accepted commits; the separately pinned later review receipt resolves that status, without rewriting the source.

The source/selection crosswalk is [#1143 comment 6777830496](https://github.com/amaybaum/incompleteness/issues/1143#issuecomment-6777830496); the renewal boundary is [comment 6772831173](https://github.com/amaybaum/incompleteness/issues/1143#issuecomment-6772831173). Their audit schema distinguishes SOURCE, COVERAGE and SOUNDNESS. Their author-side entropy observations and [finite-table generalization 6779166594](https://github.com/amaybaum/incompleteness/issues/1143#issuecomment-6779166594) are **not inherited as accepted scientific inputs**. The arguments used here are given directly.

The old C0/C1 Page assessment and apparatus contract remain off-main external support cited by SEL-ACCESS-1. Their complete original independent review artifacts were not recovered in this unit. No positive claim here depends on their detailed construction. The elementary classical and quantum references below are independently specified and proved at their stated mathematical scope.

## 2. Fix the object on which a restriction acts

Write a candidate realization as `(S, φ, μ, E, Γ, R, C)`: microscopic state space and fixed dynamics; common initialization/source law; embedded observer/readout map; actually executable preparation, setting, intervention and continuation programs; typed complete records; and resource/renewal contract. A mathematical response map is not a physical availability certificate.

SEL-ACCESS-1's conditional SEL-MENU result applies when a selector depends only on passive-law data, the candidate class contains a full/restricted-menu pair with identical such data, and a required operation has no alternative implementation in the restricted menu. Then the selector cannot guarantee coverage. It does not prove that all physical OI classes permit arbitrary menu deletion. The new tests here inspect operational continuations and therefore address different data; their actual availability still needs sourcing.

For isolated wings, complete local histories include raw calibrated outcomes, locally retained setting/controller information, local workspaces admitted as readable, heralds, failures, clocks and stopping status. Compare the law of **Bob's own** history under different Alice policies, fixing Bob's policy and preparation contract; likewise with the wings exchanged. Do not require invariance of the later **joined** history, which is expected to carry correlations. A setting-selected terminal read is not a substitute for the whole specified local history.

**Measurement independence:** in the one-shot PR and Bell tests, the same hidden source is independent of exogenous settings. This is a common pre-setting source/intervention condition, not independence of the entire closed-world state from setting bits that are themselves part of that state. In adaptive fresh-cell use, the current unused source is independent of earlier records and the settings chosen before that use; the complete adaptive setting sequence need not be independent of old source bits it has already observed.

**Parameter independence:** pointwise local responses do not depend on the remote setting, at a fixed response-complete latent state. The PR gate violates this for Bob at `y=1` while retaining one-shot measurement independence and operational no-signalling. Averaged no-signalling is weaker than pointwise parameter independence. A microscopic causal-speed constraint and Bell-local factorization must also not be identified without a proof for the particular source/interface.

## 3. Assumption and candidate-restriction ledger

| ID / candidate | What it constrains | Present standing | PR countercontrol | Classical and quantum preservation |
| --- | --- | --- | --- | --- |
| P0. Fixed reversible dynamics, finite partial observers, valid complete records, common source | `φ`, observer embedding, `μ`, record/interface tuple | Already specified in the accepted **designed model**; not all derived from bare OI | Passes; insufficient | Allows classical contexts. Does not establish a deterministic native implementation of the quantum reference. |
| P1. No-signalling for every **admitted** complete isolated local history | `μ` and procedure/effect interface jointly | Already assumed/tested within the accepted fresh-cell grammar | Passes under its exact finite fresh-cell grammar | Local classical and quantum references pass; no quantum selection follows. |
| P2. P1 plus availability of the specified old-seed setting switch, retained first output and second use | Procedure/continuation availability and observer record retention; no change of `T` required | Newly proposed availability hypothesis; conditional exclusion derived in §4 | Same-seed reuse fails. Original fresh-cell grammar does not contain that operation | Ordinary local repeated classical/quantum instruments preserve no-signalling, with their actual state updates. Requiring an unchanged hidden seed after quantum measurement is **not** a quantum-reference assumption. |
| P3. Full affine span of physically preparable latent laws, with P1 for every law and fixed measurement-independent source class | `μ` family and interface | Extra preparation assumption, not sourced; main preparation-span diagnostic applies | Forces pointwise local histories and excludes PR | Also forces CHSH ≤ 2 in the stated deterministic binary Bell scope; cannot retain the quantum Bell target there. |
| P4. Bell-local response factorization with measurement independence | `φ`/embedding/interface as expressed by response-complete functions | Extra whole-theory assumption; standard conditional bound | Excludes PR | Keeps local classical contexts but excludes quantum Bell violation under those same hypotheses. Rejected as the desired selector. |
| P5. Finite entropy/reservoir budget, all renewal paid for | `μ`, source/record resources, horizon | Target-neutral accounting requirement; no native bound selected here | Fresh PR needs a finite bank growing with the chosen finite horizon, which satisfies a correspondingly sized budget | Fair classical outcomes and any deterministic realization of independent fair quantum records need comparable entropy accounting. Scarcity alone is not a separator. |
| P6. Two-input-bit, one-classical-message-bit information inequality (§5) | Complete operational program class, access/communication contract and common independent sources; indirectly the admissible `(φ, μ, E)` tuples | **Newly proposed/testable condition**, not adopted or OI-derived | Excludes PR **if** the explicitly appended one-bit message/input protocol is executable | Passes local classical resources and standard local quantum instruments with shared entanglement, by §6. No assumption of a Tsirelson bound. |
| P7. Admit precisely quantum/Tsirelson-compatible tables | Directly the desired target | Circular as an OI derivation | Excludes by definition | Not investigated as a physical restriction. |

No conclusion about Claude's separate C3 task is assumed. The ledger does not change any existing law, prior, interface convention, task assignment or physical-source status.

## 4. The accepted reversible control and what histories add

The accepted SEL-EXCL-1 map is

`T(x,y,r,A,B) = (x,y,r, A ⊕ r, B ⊕ r ⊕ (x∧y))`.

The controls `x,y,r` remain unchanged, so applying the same XOR masks twice proves `T²=id` on **all** configurations. With `A=B=0` and one common fair `r` independent of the settings,

`a=r`, `b=r⊕xy`, `P(a,b|x,y)=½ 1[a⊕b=xy]`.

For settings `00,01,10`, the possible outcomes are `00,11` with equal weight; at `11` they are `01,10`. Thus each one-wing marginal is fair while `E00=E01=E10=1`, `E11=-1`, giving CHSH 4. At `x=0`, the actual retained raw outputs form an ordinary shared classical bit; this legitimate context is preserved as a control.

**Fresh-cell histories.** For a predetermined finite number `m` of uses, prepare independent fair cells `r_i` and fresh blank output pairs. Carry each wing's private independent seed and full local history as the induction state. Before use `i`, `r_i` is independent of the complete past and the settings just chosen. Both new local output marginals are fair regardless of the remote setting. The local transition kernel of each carried state therefore does not depend on the remote policy. Induction proves complete isolated-history no-signalling, including deterministic local copies, fixed tick labels and always-success flags. This proves nothing about arbitrary source-index choice, probing an unused cell, same-cell reuse, remote-controlled clock/failure fields or an infinite source bank.

**Same source, same output.** First use `y1=0` gives Bob `b1=r`. After allowing a second setting choice while retaining the same `r` and the current `B`, use `y2=1`. Then `b2=b1⊕r⊕x2=x2`. Bob's second marginal itself signals the independently varied remote second setting.

**Same source, blank second output.** The new output is `b2'=r⊕x2`; both one-tick marginals are individually fair, but the retained pair satisfies `b1⊕b2'=x2`. Its complete local law signals. Discarding `b1` would hide the failure.

These are conditional failures of an **enlarged** menu. The accepted fresh-cell model survives P1 for any predeclared finite `m` by using `m` independent cells and keeping used cells, records and garbage. Requiring merely finite repeatability or resource accounting does not turn these old-seed failures into a universal PR exclusion.

**Why a finite entropy cap alone does not discriminate.** For a closed finite deterministic world with a fixed nonadaptive setting program and no new random inputs, a local length-`m` record is a deterministic function of the initial world state `W0`. Therefore `H(A^m)≤H(W0)≤log₂|S|`. Exact independent fair outputs need `H(A^m)=m`. This resource bound applies to PR's local fair outputs, ordinary classical fair records and any deterministic realization of the corresponding independent quantum fair records. External inputs, refreshed banks and environmental couplings must be counted instead of being silently excluded or treated as free. This elementary argument does not select a native resource budget or initiate a preparation-cost investigation.

## 5. A conditional discriminator that also detects fresh one-use PR

### 5.1 Two-bit information test: precise operational contract

Alice receives two independent fair classical bits `Z0,Z1`. Bob receives an independent fair index `K∈{0,1}`. Their shared device/resources and private controller seeds are prepared independently of `(Z0,Z1,K)`. They may use the candidate device once under its declared local setting/output interface. Alice may then transmit **exactly one classical binary symbol `M`** to Bob on a fixed schedule. There is no other operational cross-wing communication, arrival-time encoding, public side channel or uncounted success/ready flag. Bob produces a guess `G` for `ZK`, using his admitted local records, `K` and `M`.

The compared informations are measured on the **unconditional, all-trial** probability laws:

`J = I(Z0 : G | K=0) + I(Z1 : G | K=1)`.

Define candidate condition **IC₂** by `J ≤ 1 bit` for every allowed protocol meeting that contract. A failure symbol may be retained as an extra output value; no successful subensemble is silently renormalized. Complete histories establish that there was no extra communication or hidden rejection. The scalar `J` is a falsifying witness extracted from those histories, not their replacement as the scientific evidence domain.

This is the two-input, one-message-bit instance of information causality, a standard proposed physical principle: M. Pawłowski et al., *Information causality as a physical principle*, Nature **461**, 1101–1104 (2009), [doi:10.1038/nature08400](https://doi.org/10.1038/nature08400). The publication is identified for attribution; no new literature-wide survey or review of its full generalizations was performed. The special-case proofs consumed here are supplied below. IC₂ concerns ordinary classical input recovery and a communication budget, not agreement with a quantum outcome table. One input bit could never violate the one-bit bound because `I(Z:G)≤H(Z)=1`; two inputs provide the first such binary test within this family. No minimality among all conceivable target-neutral restrictions is asserted.

**Availability is an additional hypothesis.** The original isolated-wing #1228 grammar does not itself supply a physical Alice-to-Bob message channel, a native source of `Z0,Z1,K`, or a clock implementing this test. The appended channel is a mathematical operational extension, to be source-certified if tested physically. Local XOR computations can be represented reversibly with blank targets and retained inputs, but that representation does not source their apparatus. Later joining **all** records would transmit more than the budget and would be a different test.

Most importantly, the declared message budget does not assert that the PR map has only one bit of **ontic** cross-wing influence. Its microscopic `xy` coupling is already global. IC₂ is an additional restriction on the resulting operational theory, not a consequence of renaming the explicit message as the only communication in the underlying world.

### 5.2 PR counterprotocol, with all settings fixed before the use

Set `x=Z0⊕Z1`, `y=K`, use the accepted fresh PR source once, and retain `a=r`, `b=r⊕xK`. Alice sends `M=Z0⊕a`. Bob outputs

`G=M⊕b=Z0⊕K(Z0⊕Z1)=ZK`.

For each index the guess is exact. Both requested bits remain unbiased, so each mutual information is one bit and `J=2`. No same-source reuse, access to `r` before the setting, setting-dependent source, postselection or extra explicit message is needed. Reversible local compute/copy workspaces retain inputs and garbage; they do not alter the algebra. The device's pre-message local histories remain no-signalling. After `M` arrives, remote-input dependence is expected and is bounded by IC₂ only if that additional condition is justified.

**Conditional exclusion theorem.** A selected operational theory that obeys IC₂ and is closed under this particular input encoding, single PR use, local XOR processing and fixed-schedule one-bit classical message **cannot contain the accepted PR table at that interface**. Proof: the displayed executable protocol would otherwise give `J=2>1`. This excludes the accepted fresh one-use PR countercontrol under the stated extension, not merely its old-seed reuse variant. It is a mathematical implication with explicit availability hypotheses, not an OI-derived no-PR theorem.

## 6. Classical and quantum preservation proofs

### 6.1 Classical local reference

Let `B0` contain all Bob's preshared classical information and independent private seed, independent of `Z=(Z0,Z1)` and `K`; it may be correlated with Alice's initial resource. Apart from the one-bit message, Alice and Bob use only local classical computations. Any earlier `K`-dependent Bob computation can be deferred to decoding because it does not affect Alice. Before that decoding, write `R=(B0,M)`, a common resource independent of `K`. Shared randomness is allowed, and all local records may be retained. Shannon's chain rule gives

`I(Z:R)=I(Z:B0)+I(Z:M|B0) ≤ H(M) ≤ 1`.

Independence of `Z0,Z1` and nonnegativity of conditional mutual information imply

`I(Z0:R)+I(Z1:R) ≤ I(Z:R)`.

For each query, Bob's guess is a local function or stochastic postprocessing of `R`. Since `K` is independent of `(Z,R)`, data processing yields `I(Zj:G|K=j)≤I(Zj:R)` for `j=0,1`. Thus `J≤1`.

A nontrivial saturating reference sends `M=Z0`. Bob answers `Z0` when `K=0` and a constant when `K=1`: the two informations are `1` and `0`. Raw classical records can be reread and copied with initialized memory. A shared fair bit measured in the same basis is also a retained classical context. The condition does not exclude ordinary classical observation.

This proof assumes classical **local** resources plus the stated channel; applying it to the accepted global PR map would insert an invalid locality premise.

### 6.2 Quantum local-operation reference, including shared entanglement

Fix finite-dimensional shared state `ρAB` independent of `Z,K`. Allow local quantum instruments, adaptive local processing, preshared entanglement and private randomness, with only the declared classical `M` sent from Alice to Bob. Retain outcomes and failure branches. These are **quantum comparator premises**, not derived OI operations.

Bob's index-dependent local operations can be deferred until the message arrives: they act on a different subsystem from Alice's operations and commute with them, including when their classical outcomes and local workspaces are retained. Thus there is a common pre-decoding quantum system `B` and classical message `M` on which a decoder for each index acts. Alice's trace-preserving local operation, after all her branches are summed, leaves `B` independent of `Z` before receiving the message. In the classical–quantum state `ZMB`,

`I(Z:BM)=I(Z:B)+I(Z:M|B)=I(Z:M|B) ≤ H(M) ≤ 1`.

The inequality uses `I(Z:M|B)=H(M|B)−H(M|ZB)`, with `H(M|ZB)≥0` for a classical register `M`, and `H(M|B)≤H(M)`. These are standard classical–quantum entropy inequalities; they are used to verify the **quantum reference**, not to assume quantum entropy as a native OI law.

For independent classical `Z0,Z1`, strong subadditivity gives

`I(Z0:BM)+I(Z1:BM) ≤ I(Z:BM)`.

Explicitly, the left side minus the right side is `I(Z0:Z1)−I(Z0:Z1|BM)=−I(Z0:Z1|BM)≤0`. The same identity proves the classical inequality above. Independence of `K` from this common pre-decoding state is what permits using its same two mutual informations for the two query-conditioned decoders.

Apply data processing to each index-specific local decoder to obtain `J≤1`. Local histories and readable local workspace can be included in the decoder output, so hiding an extra quantum record is not needed. Postselecting a heralded success subset would change the all-trial contract; this proof does not claim the conditional successful-branch value stays below one.

### 6.3 Explicit quantum Bell and classical contexts retained

Take `|Φ+⟩=(|00⟩+|11⟩)/√2`, Alice's dichotomic observables `A0=Z`, `A1=X`, and Bob's `B0=(Z+X)/√2`, `B1=(Z−X)/√2`. Since the `XX` and `ZZ` correlations are one and the cross correlations vanish, `E00=E01=E10=1/√2`, `E11=−1/√2`; CHSH is `2√2`. Local marginals are unbiased. The standard local quantum instruments for this reference satisfy the information bound just proved; no Bell-local hidden-response assumption was introduced.

The same state and local quantum repertoire also admit an ordinary shared-bit context when both measure `Z`. Repeated nondemolition `Z` reads give the same local raw bit. For arbitrary local adaptive instruments during isolation, summing the remote complete instrument tree gives a trace-preserving map; its partial trace leaves the near complete-history probabilities unchanged. This proves complete local-history no-signalling with all branches counted. After classical messages or later joint readout are allowed, compare the correspondingly changed protocol; joined correlations are not local signalling violations.

This is one common **quantum reference** with classical and Bell contexts, not one common OI realization of those contexts. No native preparation, entangled state, complex drive, Born rule or local instrument has been sourced by these calculations.

## 7. Why this does not yet supply an OI selection principle

IC₂ is independently intelligible and gives a checkable target-neutral separation. The recovered native premises do not justify its crucial information-access law. Reversible microscopic evolution conserves global information; finite momentary observer capacity restricts available records. Neither statement implies the chain/data-processing structure used in the classical-local or quantum-local proofs for a globally interacting hidden-variable theory. The accepted PR counterprotocol demonstrates that operational no-signalling alone does not imply the inequality. This countercontrol concerns the accepted weak class R; no claim is made that its stipulated interface satisfies every stronger native OI observer condition.

The sum `J` concerns two different choices of query, not recovery of both input bits in the same physical run. A finite observer can store the records of either run without exceeding its finite capacity. Thus “the observer is finite” or “only one explicit bit was sent” is not a proof of IC₂. An additional non-circular native principle relating actual interventions, accessible records and classical communication is missing.

The non-import test from `AGENTS.md` §A.29 and OA-1 r5 asks whether supplied elements could be retuned, at fixed `φ` and partition, to realize nonquantum targets just as easily. Here:

- The PR map and its fair product initialization are a **designed countercontrol**, not a source-backed candidate to be rescued by a fitted prior.
- The proposed information test contains no quantum table or tunable Tsirelson constant. Its fixed cost is the independently declared binary communication alphabet; retaining clocks and failures protects that contract.
- Imposing IC₂ because it rejects PR would still be an additional physical premise. A native derivation must explain it independently and produce a restriction/test beyond the particular Bell target. The information-recovery tradeoff over all such communication protocols is such a proposed additional test; its physical derivation remains open.
- Importing a density matrix, local completely positive maps, Born probabilities or quantum entropy as the **OI** justification would fail the sourcing task. Their use above is restricted to preservation of the predeclared quantum comparator.

No claim that IC₂ is sufficient for full quantum soundness, reaches all quantum targets or fixes CHSH globally follows. No literature-wide minimality or full information-causality characterization is asserted.

## 8. Fit with the accepted #1169 synthesis and owner crosswalk

| Dependency | What this unit resolves | Remaining obligation |
| --- | --- | --- |
| **MM-2**, record/effect/interface class | Specifies complete local histories, same-seed versus fresh-source extensions, exact communication alphabet, timing and all-branch accounting | Derive which of these operations and records an actual embedded native device can execute. No reliance on the pending C3 answer. |
| **MM-3**, observer operation beyond configuration ceiling | No operation is constructed; a quantum comparator is supplied only as a preservation control | Source native nonclassical operational capability without supplying complex control by fiat. IC₂ alone could also hold in a classical-only theory. |
| **MM-7**, restricted preparation family and masking | Keeps one common independent seed law and shows why fresh masking survives no-signalling tests; recalls the full-span diagnostic's scope | Independently source the restricted family, settings and renewal law. Do not demand full latent-law span to eliminate PR while silently losing the quantum Bell target. |
| **MM-8**, non-circular quantum-set selector | Supplies one explicit target-neutral conditional PR discriminator and proves classical/quantum preservation at its contract | Derive an adequate native restriction. One communication inequality is not the complete quantum-set selector or a coverage theorem. |
| **#866 / INT-AVAIL / #913 O-REUSE** | Identifies concrete availability questions rather than selecting a new source candidate | Existing owners retain preparation, control, record, clock, reset and renewal obligations. Physical source stays **NOT PASSED**. |

The synthesis ranking is descriptive and carries its stated sensitivity analyses. This unit changes no priority, assignment or issue status. It does not enter Claude's C3, G3, REC-1 or integration workstreams.

## 9. Proof and countercontrol ledger

| ID | Proposition / check | Kind and premises | Result |
| --- | --- | --- | --- |
| D1 | PR involution, four one-use tables, common independent source, classical fragment | Direct substitution; accepted SEL-EXCL-1 exact interface | Recovered and rechecked by hand; no native source claim. |
| D2 | Complete-history no-signalling for fixed finite fresh-cell schedule | Independent fresh cells, local adaptive controllers, fixed clock, all records, no extra probes/reuse | Passes; insufficiency countercontrol to no-signalling alone. |
| D3 | Old-source same-output and blank-new-output leakage | Extra specified continuation and retained first record | Fails complete-history no-signalling; original fresh-cell grammar remains distinct. |
| D4 | Bell locality / full preparation-span exclusion | Local response with common setting-independent law, or main span diagnostic plus binary all-trial outcomes | CHSH ≤ 2; excludes quantum Bell coverage as well as PR. |
| D5 | IC₂ PR protocol | One PR use plus independent classical inputs, local XORs and the appended fixed one-bit message channel | `J=2`; conditional exclusion under IC₂. |
| D6 | Classical preservation | Local classical resources independent of inputs, one-bit channel, no additional communication | `J≤1`, with ordinary classical saturation. |
| D7 | Quantum preservation | Fixed input-independent shared quantum state, local instruments, one classical bit, all branches | `J≤1`; entangled Bell and ordinary classical contexts retained. |
| D8 | OI derivation / full selector | Native source and additional access-information principle | **Not supplied** by this unit or the recovered controls. No universal impossibility claim. |

## 10. Next discriminating obligation and stopping rule

The next paper obligation is to connect **one independently source-qualified native interface** to an information/availability statement strong enough to discriminate the PR protocol, without supplying the desired quantum rule:

1. Fix the actual `φ`, preparation law/mechanism, embedded records, local input/setting programs, clock, failure branches, residual state and renewal costs. Identify which old-source, fresh-source and one-bit-message continuations are executable. An abstract declaration of the allowed menu does not close SOURCE.
2. If the native mechanism cannot implement the test protocol, report that precise availability gap. Its absence may be legitimate, but it neither proves IC₂ nor establishes quantum coverage.
3. If the test is executable, derive the information bound from independently motivated native premises, or exhibit a native violation. Identify every added restriction on `φ`, `μ`, embedding or programs. Do not substitute Bell-local factorization if the quantum Bell target is retained.
4. Test the same premise against the classical and quantum references above, with matched communication and reuse budgets. A source-backed theory passing IC₂ still needs independent soundness and coverage tests beyond this witness.

**Stop:** if the producer/interface or information principle is unsourced, preserve **UNSOURCED / DISCRIMINATOR GAP**. This report does not launch another source candidate or computation. The separate non-author reviewer must assess the exact published checkpoint; its verdict cannot be inferred from the accepted inputs. A ChatGPT exact-head review follows. Integration requires its separate owner decision.

## 11. Review brief and verification limits

Review D5–D7 in particular: the one-bit budget is operational rather than an ontic locality assertion; the PR message extension is explicitly additional; the two query-conditioned mutual informations refer to one common input-independent resource and one-bit contract; quantum preservation assumes local instruments/deferrable Bob operations and does not justify OI. Verify all failure/clock records are counted, and that no old-seed exclusion is applied to the accepted fresh-cell grammar.

This is a scoped hand-proof/source audit, not a full manuscript review, a complete corpus rederivation, a literature-wide search for the weakest axiom, a kernel proof, simulation, numerical estimate or physical implementation. The baseline source pins and review receipts are retained in the writer's local `evidence/` cache; that cache is not part of the proposed public package. [SOURCES.md](SOURCES.md) links the immutable original sources and identifies exact main blobs, off-main receipts, missing artifacts and reproduction limits. No earlier accepted document was changed.
