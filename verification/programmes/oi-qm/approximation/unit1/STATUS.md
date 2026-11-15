# APPROX-UNIT1: status, review record and retained support

Accountable Issue: #1216 (OI-QM-APPROX-1). Parent programme: #1169. Physical source: **NOT PASSED**.

## Standing

`APPROX-UNIT1.md` is revision r4b, the current text of unit 1. Its answers are unchanged from r4a:
Level A is met in three forms, none OI-derived, within exact-ring arithmetic, and the finite-b
realized-law bound is open; OI-derived Level B is not met; nothing is adopted, promoted or proposed
for the manuscripts. Each result carries the evidence layer stated in its §1. Results labelled [A]
(this unit's hand argument) or [W] (a model-written record on `main`) are not established under
§A.46 item 1.

r4b was written under the owner decision of #1169 c.6893687398 (amaybaum, posted
2026-11-15T11:33:23Z): "Write a fix commit, followed by an independent review. Each claim is
narrowed to its evidence, and the evidence an accepted Level-A result needs is kept; no valid result
is dropped only because its support is off `main`." The independent review of r4b is required by
that decision and is not recorded here. The reviews below cover r4 and the r4 → r4a diff; they do
not cover r4b. Integration requires a separate owner decision.

## Review record

| File in this directory | SHA-256 (Git blob) | Reviewed subject | Scope | Verdict |
| --- | --- | --- | --- | --- |
| `REVIEW-APPROX-UNIT1.r4.md` | `4ec1af4ded45c7b4f28febc3dc7c12d9ebf2861868fad06a949dbe6a407338ff` (`93360c44`) | r4, `cb5c4c6a37d3a5ab321b4ad0aba464104aeed4b1d9c57c298704b376b2269b44` | Full text of r4 and its writer ledger | ACCEPT WITH NITS (N1–N3) |
| `REVIEW-APPROX-UNIT1.r4a-diff.md` | `136fb32188607b902140dc60795fbb1236c208cec7849084daedf5542163343d` (`7a4336e6`) | `4e526de57b0a4fedf7821d63722a1733c0f49298` → `b1a17e01160f7dffde7ba63f7b7f69e8b95c1997` | N1–N3 and necessary metadata only; not a full scientific review | ACCEPT |
| `REVIEW-APPROX-UNIT1.r4a-final.md` | `f17ccc0e2f74f44ce03f41884668478823ce869c3df36623c9b595dfe28df32d` (`4cbca9d6`) | `b1a17e01160f7dffde7ba63f7b7f69e8b95c1997` → `e41cf6137be165add39c7e557e97d3dddf110239`, and cumulatively `4e526de5` → `e41cf613` | Publication-metadata child; supplements the r4a-diff report | ACCEPT, no findings |

All three reports are by the same non-author reviewer, Codex task `review_approx_r4`, dated
2026-11-09.

- **Full-text r4 review.** The file here is its publication copy. The original, SHA-256
  `e2749ff93827e368d375e0329fa9f70804fb6b4099ae5114c13f894dd707cb5a` (blob `fcbc7488`), is in
  commit `4e526de57b0a4fedf7821d63722a1733c0f49298`. The copy states its two changes in its first
  paragraph, and the r4a-final report accepts it.
- **Focused r4a-diff report.** Original SHA-256
  `ceeab15fedcfd40e373b4c270df8af3d2d78a0960093727f2fc9878be0f72c49` (blob `7cd18a7f`, 7,367
  bytes). The copy here is the original with three machine-local paths replaced, under owner
  decision Q2(a) (#1169 c.6892224647, amaybaum, posted 2026-11-15T09:17:55Z): "remove
  machine-local paths, record the redactions, generate new digests, preserve the original evidence
  and provenance". The original literals are not recorded. Offsets refer to the original bytes.

  | Site | Line | Byte offset | Original length | Prefix class | Replacement |
  | --- | ---: | ---: | ---: | --- | --- |
  | P1 | 5 | 200 | 22 | home directory | `review_approx_r4` |
  | P2 | 15 | 1136 | 27 | workspace root | `[local worktree]` |
  | P3 | 63 | 7197 | 4 | system temporary directory | `[local scratch directory]` |

- **Focused r4a-final report.** Byte-identical to the original.

Both focused reports are copied from the custody archive of draft PR #1280
(`verification/audits/integration/older-evidence-20261113/evidence/preserved-artifacts.zip` at
`7d4ab40aea3398f43552636cc2eea311da1d10ee`, members R1 and R2), where the redaction above is
recorded. That archive is provenance: the copies here carry their own digests, and no claim needs
the archive.

The reviewed commits `4e526de5`, `b1a17e01` and `e41cf613` are commits of #1221. They are
reachable from `main` only if #1221 lands with its commits.

Ordinary pull-request CI at `e41cf613`, run 42662313573, attempt 1, completed with 26 successful
checks and one expected skip. It is provenance (§A.42 item 2), and it is not a run at r4b.

## Retained support for the computation-supported results

The [G] scripts and the [RV] scripts, with their recorded outputs, are in `probes/` and `review/`
beside the assessment. Each file is byte-identical to `handoff-20261109/1216-approx/<path>` at
`820519cf011c09b37690213a758106ed3aa15cc2`; the Git blob ids are equal. They support the
computation-supported results of the assessment (F1–F5, C1–C7, N5, G1–G5 and their [RV]
co-citations).

| Path | SHA-256 | Git blob |
| --- | --- | --- |
| `probes/approx_generic_checks.py` | `12aac10f6e8f8d6a7bfb7603b35aac8253132534e353791508c3cda443f172c0` | `33ee0275` |
| `probes/approx_generic_checks.out` | `4337d4afc70c4fdd22deafda2eefeaa926abe044f3b7993ad47b37e9d2865c35` | `22b672fe` |
| `probes/r2_frames.py` | `aa02e479a0d93ba7ccb6ccb5f9a40c7b0e2065e5f3d7c30d3bdbb2d78010548a` | `1bf9f136` |
| `probes/r2_frames.out` | `a116e91999a566f9d409f857325be4e1d94a47c24da62f7ec6eb73e491be0209` | `ca7cea09` |
| `probes/r2_routeC.py` | `b71749e47f742338d6373aaccae08bdaa96c985c29172b36ba1267e60ac72f97` | `a73278fd` |
| `probes/r2_routeC.out` | `5626b5a8db40d7ade57542ea297c1c6afb2da32bcd5838ed013d9b02d2e538ec` | `d2f558ed` |
| `probes/r2_finiteb.py` | `383c21567671c73e9565b65c8846dfdc4ab385bf285321cd22b83b72c9b6e07c` | `37a386f9` |
| `probes/r2_finiteb.out` | `6350b5c11822166bff80b9eacde330a14513390cbda0dc117cc45f26ed4df7b1` | `5c4c25e5` |
| `review/rv_Er.py` | `0b74887ef3ca13e3d80ea6d61cfccf31efc318d15d7fdc42955ebba4ec92478e` | `a9558d72` |
| `review/rv_Er.out` | `62534a343989f0593c8797b742794734743b02a51e8bbbb12fc506a508805f61` | `79cef1e9` |
| `review/rv_finiteb.py` | `7676fcf29358a668ece160f4326b65c6539d6a291e6dab5c69f9c0dfaed38f47` | `9a256354` |
| `review/rv_finiteb.out` | `1e15387c77587412ca3962f0d81c560eaa4351eadee880a50b4d0d55c472cb6f` | `fc1a2f63` |
| `review/rv_frames.py` | `7169b7d38a637a24fe1d315161996178c887fee1483fe51369b3662067ee6d22` | `4cbc1f15` |
| `review/rv_frames.out` | `45790a004ddf96e82ed79cb2a3b3c8774723262701fdaa7424f48002b2bb6642` | `70bb7b88` |
| `review/rv_routeC.py` | `6b9a4cead5df01f01b4bbfe813c6f03129a59a33f4bc210fb1e410eec79f4c15` | `98ced621` |
| `review/rv_routeC.out` | `bded494419ac8dbee719519ee6c4ec478c208338ff31ed6d3460408002ef1a01` | `65d1436e` |

**Recipe.** From this directory, `python3 -I -B probes/<name>.py > <name>.out.new`, and likewise
for `review/rv_<name>.py`; each script needs `sympy` and imports nothing from the repository. The
expected result is exit status 0 and output identical to the recorded `.out`. §11 of the assessment
records the r2 writer's two byte-identical regenerations and the reviewer's byte-identical re-runs;
no sympy version is recorded. The scripts were not re-run for r4b, which is a paper-only revision.

## References off `main`

§1.1 of `APPROX-UNIT1.md` classifies every reference the assessment makes to content not on
`main`; none is support off `main`. This file's own references to #1280's archive, to CI run
42662313573 and to owner comments are provenance.

## r4b change map

| Passage | Finding | Change |
| --- | --- | --- |
| Header, authorization | Status wording that becomes false on landing; r4a's authority cited without a comment id | Status pointer to this file; r4a and r4b authorities cited with comment id, author and time |
| §0 item 1, §2.2, D4a, D4b, D5, §8 initial-register row | Claims resting on the #945 assessment comments and the proof review at `6d494e30`, held only off `main` | Narrowed to Main:578 on `main`; the assessment, the candidate repair and the complex-entry constant are recorded as #945's questions, not assessed here |
| §1 evidence key | "nothing here lands"; [D] stated as hypothesis input | [OFF] key removed; [D] cited for labels, open questions and provenance only; [G] and [RV] located |
| §1.1 | Incomplete list | Lead sentence restated; rows added for the [G]/[RV] files, the §7.1 preregistrations, the r4a/r4b authorities, D-SUP/D-CQ, the r1 review and the r3 records |
| §5.1 QP node-10 row; "Independence and limits" | Validity, closure and coverage cells resting on A868 [D] | Not assessed here; the quantum-compatibility cell ([W], [G] C7) is unchanged |
| §7.1 table, "Design provenance" | Cells restating off-`main` preregistration content | Not restated; the Level-B requirements are kept without the round-specific labels |
| §7.1 scope note | Soundness treated as a Level-B condition; D-SUP and D-CQ make the sector/quantum relation open | Scope note added |
| §9, §11, §12 | Gate wording met or stale; r3 review digest "to be reported"; location of r0/r1 | Gate wording replaced; r4b pass recorded; digest and locations stated |
| `DISPOSITIONS-APPROX-UNIT1.r4a.md` header | WIP status | Standing notice of a historical writer ledger |
| `probes/`, `review/`, two focused reports, this file | Support and review records held only off `main` | Added |

No other passage changes. The r4a texts are in commit `e41cf6137be165add39c7e557e97d3dddf110239`:
`APPROX-UNIT1.md` SHA-256 `3b2d0db54ac0cab078d668ba906f1a1d84577d5df9052ec0a76071664e08b280`
(blob `2cbaab43`), `DISPOSITIONS-APPROX-UNIT1.r4a.md` SHA-256
`25494b099a6894661bb11dc844d7d72d1b31edcd522c6e7f00d4fc5536825b50` (blob `3a67f1f1`).
`DISPOSITIONS-APPROX-UNIT1.r4.md` (`ef669e30e72c71e17db058081c05934abab098d4561aa60c4599a43fd982897a`)
and `REVIEW-APPROX-UNIT1.r4.md` are unchanged; their status lines describe r4 when they were
written. The r4b digests are not self-recorded.

## Remaining obligations

| Obligation | Home |
| --- | --- |
| Independent non-author review of r4b, and ordinary CI at its head | #1216 |
| Separate owner integration decision | #1216, #1169 |
| `SYNTHESIS-r3.md` (selection-discriminator support, line 734) classifies #1221 at `e41cf613` as support off `main` for the E_f classical-class definition; its row is to be reclassified if #1221 lands | #1169 |
| The per-parent step, the candidate repair F945-R and the Rounding Lemma's complex-entry constant | #945 |
