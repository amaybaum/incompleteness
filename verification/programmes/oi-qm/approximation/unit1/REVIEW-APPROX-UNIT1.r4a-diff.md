# Focused independent diff review: APPROX-UNIT1 r4a

**Verdict: ACCEPT for the focused r4 → r4a diff. No remaining diff findings.**

Reviewer: the independent non-author reviewer of r4, Codex task `review_approx_r4`, 2026-11-09. I did not author the cleanup. This is the owner-requested focused check of N1–N3 and necessary metadata, not a new full scientific review or an integration approval.

## Exact reviewed commits and artifacts

- Draft PR: [#1221](https://github.com/amaybaum/incompleteness/pull/1221).
- PR base: `cac5d26441dd33e9348151487e4df7b547195481` (`main`).
- Preserved reviewed-r4 baseline: `4e526de57b0a4fedf7821d63722a1733c0f49298`.
- **Reviewed cleanup head: `b1a17e01160f7dffde7ba63f7b7f69e8b95c1997`.**
- Stable assessment path: `verification/programmes/oi-qm/approximation/unit1/APPROX-UNIT1.md`.

I checked the PR's remote metadata: it is open, draft and unmerged, with the stated base and exact head. I also fetched the assessment at the immutable head; its Git blob `8b48ff9d5349b64aa444752d9c17be084fb491c3` matches the local pinned object used for the diff and SHA-256 check. The clean worktree `[local worktree]` was at that exact head. `AGENTS.md` is unchanged from the base; the previously read repository instructions remain applicable.

| Artifact | Independently checked SHA-256 |
| --- | --- |
| r4 assessment at preserved baseline | `cb5c4c6a37d3a5ab321b4ad0aba464104aeed4b1d9c57c298704b376b2269b44` |
| Original r4 disposition ledger, retained unchanged | `ef669e30e72c71e17db058081c05934abab098d4561aa60c4599a43fd982897a` |
| Independent full-text r4 review, retained unchanged | `e2749ff93827e368d375e0329fa9f70804fb6b4099ae5114c13f894dd707cb5a` |
| **r4a assessment at reviewed head** | **`e2d95d1a67e2d317062ca80b43de5ee59b52ae9ed96d7b60f3dc6c7fec318458`** |
| New `DISPOSITIONS-APPROX-UNIT1.r4a.md` at reviewed head | `f877a0e78231de478c5586d295a342ddbfdf59c1207d586045139b364aa24c0a` |

The baseline identities match the exact r4 artifacts I reviewed. The original ledger and full-text review have no baseline-to-head changes.

## Finding-to-diff check

Line anchors below refer to the assessment at the reviewed r4a head.

| Authorized change | Observed edit | Result |
| --- | --- | --- |
| **N1: numerical-source ambiguity** | At **249–255**, especially **250**, the conflicting `record at 6d494e30` attribution is replaced by `#945 c.6567879503 §2, assessment-review checks R-1/R-2`. The distinct older witness, lack of demonstrated reachability and lack of a final-TV refutation remain stated. | **Resolved exactly within the finding's scope.** No numerical value or mathematical status changes. |
| **N2: numerical instances labelled exact** | The evidence key at **123** defines [N] as a numerical floating-point instance rather than an exact certificate. The A3 evidence cell at **234** and D6 at **676** use [N] for `opglue_probes.py` checks 8–9, with their `1e−12` tolerance. [P] is retained for the paper proof and [X] for the other exact checks. | **Resolved.** The evidence layer is corrected; the exact-regime theorem and its precision/resource qualifications are preserved. |
| **N3: CM admissibility versus availability** | At **480–483**, the assertion that K enters the generated theory through products/blocks is removed. K is described as an admissible nonmonomial FI-1 witness and not an isometric primitive; no availability of its conjugation is claimed or needed. The diagonal-preservation conclusion and the FI-1 ⇏ system-NX-1 countermodel remain. | **Resolved.** This is the safe replacement requested in my r4 report. No native operation is added and no valid countermodel result is weakened. |
| **Necessary metadata** | Header/authorization at **3, 10–14**, review status at **828–833**, verification history at **896–908**, and the digest pointer at **922** identify r4a, accurately record r4's ACCEPT WITH NITS, distinguish the former no-write source phase from the authorized draft-publication phase, and retain focused review/ordinary CI/separate integration approval as gates. | **Within scope.** The edits do not assert that r4a has already passed its gates or authorize another workstream. |
| **New r4a ledger** | All **30 lines** were read. Its identities, N1–N3 map and metadata description match the actual diff; its lines **26–30** retain the review limits, off-main obligations, Level-A precision limits and unsatisfied OI-derived Level-B target. | **Accurate.** It is a writer disposition, not a substitute for this review or CI. |

I read the entire baseline-to-head diff, not just these excerpts. Its complete file set is:

1. Modified assessment: **27 insertions, 18 deletions**.
2. Added r4a ledger: **30 insertions**.

No other files change in this delta. The original r4 ledger, original full-text review, scientific sources, probe scripts/outputs, workflow files and repository instructions are unchanged. The additional commit after the first cleanup only clarifies that focused review and CI remain requirements. `git diff --check` passes.

## Preservation of accepted scope

The edit map accounts for every assessment hunk. There is no new physical premise, mathematical assertion requiring a fresh full scientific review, execution result, source-pin change, broader access claim, resource-uniform no-go, or promotion of a conditional result. In particular:

- Level A retains its accepted exact/finite-accuracy precision regimes; the fixed-b clipped/normalized law bound stays open.
- OI-derived Level B remains unsatisfied. The common physically sourced correspondence and separate complete-history coverage/soundness obligations are unchanged.
- The route-relative matrix comparisons, narrow two-configuration law witness, level-one transport seam, and conditional fixed-frame channel conclusions are unchanged.
- The metadata accurately inherits my r4 **ACCEPT WITH NITS** verdict and its limits. It does not imply a new kernel check or scientific execution.

My original review's inability to certify a byte-diff against unavailable r3 or the exact original r3-review history remains. The cleanup does not purport to remove that limit.

## Integration and verification boundary

**This diff acceptance does not certify landing readiness.** Ordinary CI is being checked separately by the coordinator; I make no green-CI claim in this report. Green ordinary CI and a separate owner integration decision remain required.

The assessment's §1.1 off-main-support classifications and the corresponding AGENTS.md §A.42/§A.46 obligations are unchanged. A non-landing WIP review did not require all research dependencies to be on main. Before integration, the content each surviving claim actually needs must receive the applicable support disposition; this diff review neither closes those gaps nor grants an exception. Preserving cited IDs and hashes is not itself retention or validation of their supporting content.

No scientific programs, probes, simulations, enumerations, Lean imports/builds or workflows were run for this check. I made no repository, input, ref, branch, GitHub or external writes. Only this off-repository report was written under `[local scratch directory]`.

**Final disposition: ACCEPT for the exact baseline-to-head cleanup diff, with no remaining findings.** No new full scientific review is triggered by these edits.
