# #1280: exact proposed preservation scope

**Owner decision proposed, not executed.** Accountable Issue: #1169. The accepted custody checkpoint is 584c757b949de7dc017373fa5e1d1f540e740a7c. Main dfeec843… has made §A.46(8) operative. This proposal does not change any of the eleven existing files or archive members.

## Recommended selected payload

Retain the four actual historical artifacts in their existing byte-identical archive, with exactly these six proposed repository paths under verification/audits/integration/older-evidence-20261113/:

| File | Intended content/change |
| --- | --- |
| evidence/preserved-artifacts.zip | Unchanged 148,006-byte ZIP; four original members totaling 147,390 bytes |
| PRESERVED-ARTIFACTS.json | Keep exact member identities and source-date metadata; update only selected-manifest linkage and current landing status |
| PRESERVATION-STATUS.md | Scope, current policy/review state, rationale, accountability and explicit unresolved evidence limits |
| SELECTED-ARTIFACTS.tsv | Four rows: R1, R2, M1, M2, with exact paths, sizes and digests |
| RETENTION-TRACE.md | Each retained custody/history/scientific use and its actual support/disposition |
| reviews/CUSTODY-REVIEWS.json | Full verbatim bodies of non-author custody review 5902077541 and ChatGPT custody review 5902527446, selected identity fields and body hashes |

[LANDING-SCOPE.json](LANDING-SCOPE.json) gives the full paths and exact original byte identities. For the five mutable/new metadata files this is an exact path/content contract, not a claim that their eventual bytes already exist or have been reviewed. The ZIP is the fixed existing artifact.

The eight parent audit files are **not automatically selected** by this recommendation. They remain unchanged and reachable at the accepted research checkpoint; their complete paths are in the JSON. Their 101-row preservation proposal and 116-copy audit do not become an authorization to retain that entire corpus. This scoped preparation does not delete those files, re-cut a branch, or move any source checkpoint.

Merging the current PR would still land its full eleven-file proposal (plus these planning documents), not this six-path selection. After the owner selects the scope, a separate documentary child must express the selected current-tree payload while preserving the accepted history. The scope proposal itself is planning material; it is not automatically part of the proposed main payload.

## Four selected artifacts and supporting evidence

- R1/R2 are the actual original focused #1221 model-review reports. Their complete bodies support what the reports record about their subjects and verdicts. They do not, by themselves, establish the reviewed approximation assessment or its Git ancestry.
- M1 is the captured 84-block Page; M2 is its exact Markdown projection. Both bytes are already present. The deterministic verification recipe checks all four members, their digests and the projection; it executes no scientific content.
- Custody reviews 5902077541 and 5902527446 support the independently checked research-branch custody status. Retain their actual bodies when that status is asserted on main.
- Source URLs, original source dates, capture sequence and historical commit pins identify provenance. They do not replace proof/check/review content consumed by a scientific assertion in the matrix.
- No current scientific claim is strengthened by preserving the originals. A historical wrapper is not a blanket §A.42 exception.

The six-path scope is therefore **not yet certified sufficient for every scientific assertion in M1/M2**. Before a final landing, RETENTION-TRACE must identify every assertion actually retained as a supported result, its needed content/history, and any unresolved use. Close such a use by retaining its content, permissible narrowing, or a separately recorded owner exception naming that precise unsupported claim. This proposal selects no exception and does not claim the unresolved trace complete.

## Frozen-ledger discrepancy: #1280 disposition

The actual frozen DISPOSITIONS-r7c.md at #1219 head 4c7f3f86191847592de18de55b364cc8cf591bb3 has SHA-256 d3adc82369b45c0a5fcb43cacf33a823a937984c2ee7f07d1028bd56f4c88045. CHECK-r7c names historical 856fa01d7010855a2f6dad75ce41b5c4adbf81d6f8d917b2cd20314253c1b0ba.

[Fresh review 5903131037](https://github.com/amaybaum/incompleteness/pull/1219#pullrequestreview-5903131037) accepts the actual ledger's documentary accuracy at a stated scope. It neither recovers the missing historical bytes nor retroactively transfers the earlier review. The published CHECK-r7c is review/CHECK-r7c.md in the same package, blob bfeaadef540c39a4bb97d956ea39e74139c0a0bb, SHA-256 ab7ae7236fa517f19a009a287d54d811fa9768df1d60e0c167a7d3f04a44d73a.

Recommended disposition: preserve the different identities and record the new review as a distinct event. Do not replace the historical pin, invent a reverse diff or edit frozen bytes. If the selected landing asserts actual-ledger accuracy rather than merely recording the receipt, add the actual ledger and review's necessary comparison support to the explicit selected file list before approval. Accountable Issue: #1210.

## OICORE discrepancy: #1280 disposition

The published OICORE-1.md at #1214 head 7722612883f5fc694f3e4dafae84f00f4407073d has SHA-256 a30d8d7969920334a0ad569ec85a47d6d417bb69674e3c81a272d861cba7371a. Historical final 9b82ecc2… and r6 ec7966c9… are different, unrecovered byte identities; full values and path are in the JSON.

[Landing receipt 6740618570](https://github.com/amaybaum/incompleteness/pull/1214#issuecomment-6740618570) requires the exact version bridge. [Owner restriction 6742190639](https://github.com/amaybaum/incompleteness/pull/1214#issuecomment-6742190639) keeps the Q-C2-1/Q-C2-2 dependency requirements separate.

Recommended disposition: retain the discrepancy as open. No acceptance transfer to a30d8d79…, no fabricated original, and no implied resolution of REACHABLE Theorem C / ACCESS-F0 or consumed FIX/noncontextuality/M6/M8/M12/T3/Lemma M support. Their proof/support closure is owed only when a retained claim actually uses it. Accountable Issue: #1169.

## Next decision and limits

The owner can select this six-path preparation scope without authorizing merge or closing the stated gaps. The eventual exact child needs focused independent review, ordinary final-head CI, ChatGPT confirmation and its own owner merge decision. Substantive scientific changes require renewed scientific review.

These ledger/OICORE questions belong to #1280's disposition. They are not dependencies of #1278's bounded producer-source stop or #1281's D5–D7 information discriminator. No scientific execution, physical-source investigation, new premise, frozen edit or merge is performed. Physical source remains **NOT PASSED**.
