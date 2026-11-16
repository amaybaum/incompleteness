# Focused publication-metadata supplement: APPROX-UNIT1 r4a

**Verdict: ACCEPT for the final r4 → r4a diff at `e41cf6137be165add39c7e557e97d3dddf110239`. No remaining findings.**

Reviewer: the independent non-author r4 reviewer, Codex task `review_approx_r4`, 2026-11-09. I did not author either cleanup. This supplement examines only the publication-metadata child of the previously accepted cleanup; it does not reopen the scientific audit.

## Scope and identity

- Draft PR: [#1221](https://github.com/amaybaum/incompleteness/pull/1221), still draft and unmerged when checked remotely.
- PR base: `cac5d26441dd33e9348151487e4df7b547195481`.
- Preserved r4 baseline: `4e526de57b0a4fedf7821d63722a1733c0f49298`.
- Previously reviewed cleanup: `b1a17e01160f7dffde7ba63f7b7f69e8b95c1997`.
- **Final reviewed head: `e41cf6137be165add39c7e557e97d3dddf110239`**, whose sole parent is the previously reviewed cleanup.

The GitHub pull-request API reports that exact final head and the stated base. I fetched the assessment at the immutable final ref; its Git blob `2cbaab4353d274b3f467c889a3c227cfbbd1fc17` matches the local pinned object. The local worktree was clean at the final head.

The previous focused report remains unchanged at `REVIEW-APPROX-UNIT1.r4a-diff.md`, SHA-256 `ceeab15fedcfd40e373b4c270df8af3d2d78a0960093727f2fc9878be0f72c49`. Its ACCEPT applies to baseline → b1a17e01. This supplement extends the final diff verdict to the new head and supersedes its artifact-identity statements only where explicitly updated below.

| Final or preserved artifact | Independently checked SHA-256 |
| --- | --- |
| **Final r4a assessment** | **`3b2d0db54ac0cab078d668ba906f1a1d84577d5df9052ec0a76071664e08b280`** |
| Publication copy of the full-text r4 review | `4ec1af4ded45c7b4f28febc3dc7c12d9ebf2861868fad06a949dbe6a407338ff` |
| Final r4a writer disposition ledger | `25494b099a6894661bb11dc844d7d72d1b31edcd522c6e7f00d4fc5536825b50` |
| Original r4 writer ledger, unchanged in the final tree | `ef669e30e72c71e17db058081c05934abab098d4561aa60c4599a43fd982897a` |
| Original full-text r4 review at baseline and in the original local report | `e2749ff93827e368d375e0329fa9f70804fb6b4099ae5114c13f894dd707cb5a` |

The assessment, writer ledgers and publication review are under `verification/programmes/oi-qm/approximation/unit1/`. I rechecked the original review's baseline and local hashes; the original report has not been overwritten.

## Complete child-diff check

I read the full b1a17e01 → e41cf613 diff: **three files, 11 insertions and 8 deletions**, with every hunk accounted for below. `git diff --check` passes.

| File / final line anchors | Observed publication change | Assessment |
| --- | --- | --- |
| Assessment **3, 903** | “revision metadata” becomes “revision/publication metadata”. | Accurately describes the added publication edits; no substantive status change. |
| Assessment **134** | The [D] definition describes an “off-main working draft” instead of its session workspace location. | The crucial “unreviewed or in-revision” and “used as a hypothesis only” qualifications are identical. No source is promoted. |
| Assessment **214** | The reference-table label describes “off-main drafts” generically. | The support-off-main classification, hypothesis-only status, cited restrictions and re-derivation qualification are unchanged. |
| Publication r4 review **3, 7, 205** | Adds an explicit publication-copy note with the original baseline/digest; removes the runtime prefix from the reviewer task identifier; describes the temporary work location generically. | Accurate. The identifying task name remains, and the generic temporary-directory description truthfully describes the original review. The original bytes remain available at the named baseline with the stated digest. |
| r4a ledger **11–12, 22** | Records the original/publication review distinction, new publication-copy and assessment digests, and the four locality-reference edits. | Matches the actual diff and measured hashes. It does not imply that the publication copy is byte-identical to the original or that off-main support has been validated. |

**I confirm that the publication copy preserves my full-text r4 review's verdict, N1–N3, proofs, scientific conclusions, source/evidence qualifications, comparison limits and authorization boundaries.** Its only changes are the explicit copy-provenance note and the two locality descriptions. I accept this publication adaptation of my review; it is not a revised scientific verdict.

The assessment's scientific content is likewise unchanged by the child. N1–N3 remain resolved exactly as accepted at b1a17e01. No additional paths change, including no checker, workflow, scientific code, probe output or source-pin changes. The baseline → final-head file set now consists of the corrected assessment, the new r4a ledger and this metadata-only publication copy of the r4 review. The original r4 writer ledger remains unchanged.

## Final scope and gates

Combining the earlier accepted N1–N3 diff with this accepted child gives **ACCEPT for the complete baseline `4e526de5` → final head `e41cf613` diff**. There are no genuine scientific or provenance findings in these publication edits, and they do not trigger another full scientific review.

I did not replay the static source checker or attest the new ordinary CI result. The coordinator's reported SC-42 pass and the ongoing final-head CI remain separate verification evidence. **Green ordinary CI, the unchanged §1.1 off-main-support obligations, and a separate owner integration decision remain required.** This focused acceptance neither closes those support gaps nor grants a landing exception.

The original full-review limits, including unavailable r3/original-review comparison bytes, remain in force. No scientific program, probe, simulation, enumeration, Lean import/build or workflow was executed for this check. No repository, input, ref, branch, GitHub or external write was made by this reviewer. The earlier review files remain untouched; only this new off-repository supplement was written.
