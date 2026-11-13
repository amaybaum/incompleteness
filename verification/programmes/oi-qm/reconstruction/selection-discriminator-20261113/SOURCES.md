# SEL-DISC-1 — Source, review and retention ledger

**Main pin:** `c3b5f37a354bb26437e2e0165c576a347a63c153`. **Writer recovery:** 2026-11-13. This ledger supports [ASSESSMENT.md](ASSESSMENT.md); it does not promote draft inputs to established-on-main results.

**Public package:** `ASSESSMENT.md`, `SOURCES.md`, `ARTIFACTS.sha256`. The `evidence/` names below identify **local writer audit caches**, not files proposed for publication. Immutable GitHub sources and receipts linked here are the public review inputs. Local capture and off-main URLs do not themselves satisfy a later main-retention or integration decision.

## 1. Authority and exact metadata retained

- `evidence/authority-1143.json`: full owner handoff [#1143 comment 6863602000](https://github.com/amaybaum/incompleteness/issues/1143#issuecomment-6863602000). One bounded paper-only discriminator, non-author review then ChatGPT exact-head review. No new execution, premise, selection/measure/rule, merge or manuscript authority.
- `evidence/coordination-1169.json`: [#1169 comment 6863608722](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-6863608722). Separate Codex/Claude task ownership.
- `evidence/pr-1224.json`, `pr-1228.json`, `pr-1276.json`: primary recovered PR head/draft/base metadata. These are time-specific observations, not guarantees that remote heads never change.
- `evidence/comments-1143-full.json`: all returned comments since 2026-11-10, 17 entries; includes source/selection crosswalk `6777830496`, renewal handoff `6772831173`, earlier stopped-source crosswalk `6764740008`, and the author-only generalization `6779166594`. `comments-1143-latest.json` is the initially narrower recovery. The requested window is not a claim of entire issue-history coverage.
- `evidence/issue-1143.json`: body snapshot; its planning fields are historically stale on review status. Exact review receipts take precedence for the review identity claims below.
- `evidence/comments-1169-latest.json`: recovered Nov12–13 comments, including the FH→SOURCE trace `6829596317`, owner clarification `6829898892`, synthesis decisions `6863414487` and coordination handoff. This is not a complete history of #1169.

## 2. Main-supported sources actually consumed

The entries below were read from the supplied read-only snapshot. `evidence/main-source-tree.json` retains their primary tree identities. The flattened copies under `evidence/` are byte-identical as verified by Git blob hashing; no original was changed.

| Repository path at the main pin | Exact Git blob | Retained local copy | Role consumed / scope |
| --- | --- | --- | --- |
| [`AGENTS.md`](https://github.com/amaybaum/incompleteness/blob/c3b5f37a354bb26437e2e0165c576a347a63c153/AGENTS.md) | `8900fe1ff55e45a64732e6751c2601a91367dcfd` | `main-AGENTS.md` | Operative §A.29 hard-to-vary/non-import rule and evidence/scope requirements. In advance: preserve controls, give an independent consequence beyond the target problem, reject adjustable fit-any-outcome variants. |
| [`papers/Main.md`](https://github.com/amaybaum/incompleteness/blob/c3b5f37a354bb26437e2e0165c576a347a63c153/papers/Main.md) | `0db1759754bfaa85d1f5271f03dc6e0ca55d2209` | `main-Main.md` | Definition and early status remarks distinguish finite visible capacity, representation choices and priors; the fixed-basis finite-history theorem does not supply the complete physical operation class. No downstream-dependent claim is used to prove Main. |
| [`oa-1-20261112/OA-1-REPORT-r5.md`](https://github.com/amaybaum/incompleteness/blob/c3b5f37a354bb26437e2e0165c576a347a63c153/verification/programmes/oi-qm/reconstruction/oa-1-20261112/OA-1-REPORT-r5.md) | `5a16b213ebe96846e53072bf1cac226e455f9f72` | `main-OA-1-r5.md` | §1 non-import test; §5 distinguishes classical preparation/control from the configuration-interface quantum-operation gap. Does not prove an all-interface no-go. |
| [`oi-qm-ext-1/prepared-pair-source.md`](https://github.com/amaybaum/incompleteness/blob/c3b5f37a354bb26437e2e0165c576a347a63c153/verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/prepared-pair-source.md) | `9123157c7b5ce41c72af10edab1c92de5a705bcc` | `main-prepared-pair-source.md` | §§4–5 complete-history linear balance equations, and full-affine-span diagnostic with common source; classical CHSH consequence needs its stated binary every-run conditions. Full span is not supplied by OI. |
| [`oi-qm-ext-1/composition-source-map.md`](https://github.com/amaybaum/incompleteness/blob/c3b5f37a354bb26437e2e0165c576a347a63c153/verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/composition-source-map.md) | `c4eeb4670b281e3d18ee3ca69c57d823d6eeb045` | `main-composition-source-map.md` | §§4–6 distinguish micro-local response, setting independence, complete histories, common positive quantum representation and closure; quantum local instruments are a sufficient comparator, not a native source. |
| [`native-preparation-source-1-20261110/PREPARATION-SCREEN.md`](https://github.com/amaybaum/incompleteness/blob/c3b5f37a354bb26437e2e0165c576a347a63c153/verification/programmes/oi-qm/reconstruction/native-preparation-source-1-20261110/PREPARATION-SCREEN.md) | `8f1edce39bec7069608d9dc2e34f281a81caa47a` | `main-PREPARATION-SCREEN.md` | Bounded quiescent-bank proposal stopped at missing executing producer; no universal source impossibility. Used as a source-boundary control, not a new source candidate. |

The report's negative conclusion is limited to its proved weak-model countercontrols and named recovered dependencies. It is not a full review of all 2,663 snapshot files or a claim that every possible native OI principle has been excluded. No current Claude C3/G3/REC-1 work is consumed.

## 3. Off-main reviewed papers: exact bytes and receipts

### SEL-ACCESS-1 (#1224)

- Repository path: `verification/programmes/oi-qm/reconstruction/oiqmsel-access-20261110/SELECTION-ACCESS-1.md`.
- Accepted corrected head: `1b966a0383e1dabe867d41816ee9743e99502938`.
- [Immutable accepted source](https://github.com/amaybaum/incompleteness/blob/1b966a0383e1dabe867d41816ee9743e99502938/verification/programmes/oi-qm/reconstruction/oiqmsel-access-20261110/SELECTION-ACCESS-1.md).
- Git blob: `5c125be576fd9552acabe891ff851fa19046fc3a`.
- SHA-256: `811fd989ed7a25cf14f614c20ea295f35fdad9b2feb2ac2e67a6995e884d43f1`.
- Exact retained text: `evidence/SEL-ACCESS-1.md`; connector blob/URL metadata: `SEL-ACCESS-1-metadata.json`.
- Full review: `evidence/review-1224-full.json`, [review 5840425454](https://github.com/amaybaum/incompleteness/pull/1224#pullrequestreview-5840425454), COMMENTED 2026-11-10T10:36:00Z, ACCEPT WITH NITS at `ea8827ff6b4c3e405310216c75bcc32157d069bb`; original blob `c2b2ddd2efe7984d19bfe08b3a55005fb340b84d`. Original source SHA in receipt: `6b9063170a6378081a59017bbc89ca6edf0be99f4d0276aeb4c77971b847c9e0`.
- Focused correction review: `evidence/review-1224-focused.json`, [review 5840851253](https://github.com/amaybaum/incompleteness/pull/1224#pullrequestreview-5840851253), COMMENTED 2026-11-10T11:07:22Z, ACCEPT exact corrected head. Reviewer attributed as non-author Codex `/root/review_sel_access_1`; author remains ChatGPT. Closes protocol/history typing and calibrated raw-register versus postprocessed-report distinction.
- Mathematical premise consumed: conditional SEL-MENU theorem and its explicit hypotheses; detailed C0/C1 external Page construction is not consumed as a newly established theorem.

### SEL-EXCL-1 (#1228)

- Repository path: `verification/programmes/oi-qm/reconstruction/oiqmsel-exclusion-20261110/SEL-EXCL-1.md`.
- Accepted scientific head: `0ecfddeb89540aedf1e2dc3ae7c377516641066c`.
- [Immutable accepted source](https://github.com/amaybaum/incompleteness/blob/0ecfddeb89540aedf1e2dc3ae7c377516641066c/verification/programmes/oi-qm/reconstruction/oiqmsel-exclusion-20261110/SEL-EXCL-1.md).
- Git blob: `1e8892ff94a8f0dcf306e3f43cd57e951a446ca7`.
- SHA-256: `9a99344998ea78f345df1a6362a622ea9a2e764dc70d0f75a79f1c2a1259f74f`.
- UTF-8 size: 25,988 bytes. Exact retained text: `evidence/SEL-EXCL-1-accepted.md`; metadata: `SEL-EXCL-1-accepted-metadata.json`.
- Full review: `evidence/review-1228-full.json`, [review 5845436861](https://github.com/amaybaum/incompleteness/pull/1228#pullrequestreview-5845436861), ACCEPT WITH NITS at `4813bc0b04548248581a137c88d43a64d73bd1a9`; original blob `50e77005e23dde490906fbdb0b848a6eeb6a497c`; original SHA in receipt `ff9805e6b1dae4b7d7404457e8a67ae547291c2c3cbe703e78e3e828bbc3f573`.
- Focused correction review: `evidence/review-1228-focused.json`, [review 5848321039](https://github.com/amaybaum/incompleteness/pull/1228#pullrequestreview-5848321039), COMMENTED 2026-11-10T19:48:26Z, ACCEPT exact scientific head. Non-author reviewer `/root/review_sel_excl_p3`; relayed report SHA `76da2795ceb5ef0557852b571b70af8bacb12fcdc33b72e3cd34fcf56e2a081e`. Closes complete-history/controller typing and single-marginal versus record-pair same-source diagnostics.
- Current recovered documentary descendant: head `756811051bbc0670714f4d77d62339c12adaba34`, blob `7811e4493ab471b9e968483c9d18de4a5756de43`; text `evidence/SEL-EXCL-1-documentary.md` and accompanying metadata. The static diff changes review/antecedent/status descriptions, not the displayed map or identities. Its separately requested narrow review was **not recovered as complete**. No ACCEPT is attributed to this descendant.
- [Immutable documentary source](https://github.com/amaybaum/incompleteness/blob/756811051bbc0670714f4d77d62339c12adaba34/verification/programmes/oi-qm/reconstruction/oiqmsel-exclusion-20261110/SEL-EXCL-1.md); not substituted for the accepted source above.
- Mathematical premise consumed: specified finite globally coupled PR control and exact fresh/reuse grammar. D1–D3 are also rechecked directly in this report; D5 is a new application requiring its own review.

### #1169 synthesis r3 (#1276)

- Head read: `9eeee392fcfe7489fab3e007d95488ecf4a3eb13`.
- [Immutable synthesis r3](https://github.com/amaybaum/incompleteness/blob/9eeee392fcfe7489fab3e007d95488ecf4a3eb13/verification/programmes/oi-qm/reconstruction/drafts/synthesis-1169-20261113/SYNTHESIS-r3.md) and [retained non-author confirmation](https://github.com/amaybaum/incompleteness/blob/9eeee392fcfe7489fab3e007d95488ecf4a3eb13/verification/programmes/oi-qm/reconstruction/drafts/synthesis-1169-20261113/CONFIRM-r3.md).
- Path root: `verification/programmes/oi-qm/reconstruction/drafts/synthesis-1169-20261113/`.
- `SYNTHESIS-r3.md`: blob `e68295098577f4ec28cdc52726e83395deee915f`; SHA-256 `00421b3338384891277234b2fe15f396b2c673472c83e952f5aba30ed55a5f53`. Complete retained text and metadata under `evidence/`.
- `CONFIRM-r3.md`: blob `e420539ac312c6a4ebefa44d2cb31112fc6ce2c5`; complete retained text and metadata under `evidence/`. It reviews r3 at `027f2b93a8f1849b287695c6db5d50fbc96f34b0`. An independent exact-ref file fetch at that earlier head returns the **same** r3 blob; evidence: `SYNTHESIS-r3-confirmed-metadata.json`. Thus the narrow non-author confirmation applies to identical r3 text, not merely an assumed unchanged descendant.
- [ChatGPT exact-head review 5896999231](https://github.com/amaybaum/incompleteness/pull/1276#pullrequestreview-5896999231): `evidence/review-1276.json`, COMMENTED 2026-11-13T19:41:54Z, ACCEPT at the full head above. It explicitly limits itself to synthesis/provenance and disclaims independent rederivation of every input.
- `evidence/files-1276.json` retains the API file inventory. MM-2/MM-3/MM-7/MM-8 are consumed as **scoped dependency classifications**, not as proofs of every off-main source behind them. The full synthesis is off-main input; its dependency table still marks that support gap.

## 4. Independent references and missing artifacts

The report attributes IC₂ to the standard information-causality research direction: M. Pawłowski et al., *Information causality as a physical principle*, Nature **461**, 1101–1104 (2009), [doi:10.1038/nature08400](https://doi.org/10.1038/nature08400). The special-case PR/classical/quantum arguments are written out in the report; no conclusion is borrowed from an unexamined full-set characterization theorem. The reference's complete text and later literature were not retrieved in this unit. In particular no claim about all quantum correlations, general information-causality sufficiency, or the unreviewed 2026 link in comment `6779166594` is consumed.

Missing or deliberately unconsumed:

1. The original full C0/C1 Page assessment, its complete proof/access contract and independent review artifacts. The report does not depend on them beyond accurately recording their status in accepted SEL-ACCESS-1.
2. A completed exact-head documentary review at #1228 head `75681105`; earlier acceptance is not substituted.
3. A native executing input/controller/message/readout/renewal certificate and independently sourced native information-budget principle. These are missing scientific/source obligations, not evidence satisfied by a GitHub acceptance.
4. An independent non-author review of **this** report and a later ChatGPT exact-head review. Both remain pending at the writer stage.
5. A main integration/retention decision. Immutable off-main links and local evidence copies make this draft reviewable; they do not themselves make every support item reachable from main or authorize a merge.

## 5. Verification actually performed

- Exact-ref read-only GitHub file/API retrievals, supplied snapshot reads and source inspection.
- Static Git blob hashes of retained text agree with the source tree or connector identities. SHA-256 of #1224 and #1228 accepted files also agrees with the independent correction receipts.
- Static identity check confirms synthesis r3's reviewed earlier text equals the final-head r3 blob. Static accepted-to-documentary #1228 diff inspected only for provenance; it is not represented as an independently completed review.
- Local cache JSON syntax checked with `jq empty`. The two public Markdown artifact digests are in `ARTIFACTS.sha256`; the larger evidence-cache inventory is retained locally and excluded from publication.
- All scientific arguments are hand derivations. No script evaluates a model, entropy, Bell statistic, random-access success rate, state space or proof search. No simulation, Lean/kernel run, numerical approximation, source screen, experiment, fixture solve, workflow dispatch/rerun, branch rewrite or remote mutation occurred.

No CI result for this new report is claimed here. Publication, exact-head CI, independent review and eventual integration remain the coordinator's separate steps.
