# Older accepted-evidence preservation and integration decision packet

Status: WIP writer checkpoint; evidence reconciliation in progress; no integration recommendation is accepted yet.

Audit cut: `main` at `c3b5f37a354bb26437e2e0165c576a347a63c153`, 2026-11-13. Owner authority: PR #1226 comment 6863602829 and #1169 comment 6863608722. Proposed repository destination: `verification/audits/integration/older-evidence-20261113/`.

This is a read-only research [R] preservation proposal. No evidence has been landed, retired, rewritten, promoted or executed. #1216 remains Backlog. #1214 and #1270 are provenance references only; Claude's #1268–#1276 assessment is outside this packet.

## First checkpoint: verified identities and unresolved gates

| PR | Exact current head | Host state | Distinct question before an owner preservation decision |
| --- | --- | --- | --- |
| #1226 | `f1a8f1a55ff0da200edc6908f64f00f684911109` | Draft, open, unmerged; mergeable=true; behind | Preserve accepted #1049 r5 assessment/dispositions and matrix reconciliation while separating stale planning statements from the external matrix and missing historical sources. |
| #1221 | `e41cf6137be165add39c7e557e97d3dddf110239` | Draft, open, unmerged; mergeable=true; behind | Preserve APPROX r4a with its r4 evidence chain; focused r4a review is claimed in the PR body but no PR review submission or discussion receipt is present. Recover or explicitly label the missing record. |
| #1219 | `4c7f3f86191847592de18de55b364cc8cf591bb3` | Draft, open, unmerged; mergeable=true; behind | Frozen r7c dispositions hash differs from the independent check's reviewed ledger pin. Ratification is distinct from independent review; OICORE cited version also needs exact provenance. |
| #1082 | `29430f7b43a824c5d6f58c1233032c6d16861d79` | Draft, open, unmerged; mergeable=true; behind | Preserve distinct BORN-SEL mathematical units without treating the already landed QB3 subset as acceptance of the whole assessment or freezing/running C1. |

All four changed-file lists contain additions only relative to their historical base. GitHub's mergeability flag is not an assessment of semantic compatibility or a merge authorization. Exact comparisons with pinned current main, complete review scopes, unit inventory, minimum preservation manifest, and CI receipts follow in the completed packet.

## Provisional owner options

Each PR requires a separate later YES/NO decision: keep it open with named gaps; authorize a minimal new evidence landing proposal after evidence gaps are resolved or accurately retained; or retire it only after proving every surviving claim has retained support. These are options, not actions, approvals or recommendations to merge existing branches.

The smallest currently visible gaps are the exact r4a focused-review record (#1221), review of the exact frozen dispositions bytes (#1219), precise OICORE version bridge (#1219/#1214), and durable matrix snapshot/status reconciliation (#1226). Historical green CI will be checked separately from current-main compatibility.

## Evidence at this checkpoint

Raw PR metadata, complete page-1 discussion/review/changed-file responses for the four scoped PRs and the two provenance references are in `evidence/`. None of those lists reaches the 100-item page boundary. Sources are GitHub API read-only queries. Source-byte comparisons and review receipt extracts remain in progress.
