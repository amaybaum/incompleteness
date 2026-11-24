# O-13 adoption record

Owner decision (`amaybaum`, 2026-11-24, in the coordinating session), quoted:

> Adopt O13-DECISION-ADOPT.md exactly as supplied, with SHA-256:
>
> c6414f74b11d11fa7ba0d522905d22e3d0c93a285a1cd1cf2a4b5c965e350e5d
>
> The adoption is based on the independent ACCEPT-WITH-NITS verdicts for r4 and r5, with no blocking findings.
>
> Do not apply optional nits (a) or (b). No further revision or review is required for O-13.
>
> Confirm adoption of exactly D402–D412, bound to the reviewed hashes, and the limited supersession of the scientific-preservation clause for those edits only.
>
> Preserve:
> - The ledger base H.
> - All original 399 splices, byte for byte.
> - Item 7, exactly as frozen.
> - All historical trial evidence, including the expected T0′ failure.
> - Every scientific conclusion outside the exact adopted edits.
>
> Record this adoption locally and on #1169 through the checked write tool, quoting this decision and verifying the stored text byte for byte.
>
> This does not authorize amendment of the frozen plan, re-freezing, trial execution, push, dispatch, premise changes or merge.

Adopted text: `O13-DECISION-ADOPT.md`, sha256 `c6414f74b11d11fa7ba0d522905d22e3d0c93a285a1cd1cf2a4b5c965e350e5d`, reproduced below unchanged.

> **Owner decision (O-13): adoption of the A1-plan manuscript edits D402–D412, and a limited supersession of the
> scientific-preservation clause.**
>
> 1. **Adopted edits.** I adopt, as part of the amendment to the A1 retirement plan in preparation, exactly the
>    eleven edit records D402–D412 of amendment proposal r5, and no others.
>    - Each is identified by its file, its old bytes at the ledger base H `53c6601a10419b6b333cc992474272501ab542af`,
>      and its new bytes, through the sha256 values below.
>    - They are contained in the edit list `edits.json` with sha256
>      `f99d705ae896c891806ee99c2217e24237cada5ac49e607b0b013bd43c6dd38d`, and in the exact-edit ledger `ledger.json`
>      with sha256 `65c8c866fa1ebebb338c869113ed3e1275a9aca1ededab58f6bdf286aab1a2e8`.
>    - That ledger has 410 splices in 44 files: the 399 splices of the frozen plan `4c79be642ca631573f06b444903be75ec4f5e2b6`,
>      unchanged byte for byte, and the splices of D402–D412.
>
>    | Edit | File | old_sha256 | new_sha256 |
>    |---|---|---|---|
>    | D402 | `papers/SM.md` | `227117bc96e597894158fe4ba53ceb3b0c426e3a7f6ed5f414698db95e08d3c6` | `ac5a1b8504586ec1432cba5ec278947a6ecc025f2df101e1d794bd7c78592c32` |
>    | D403 | `papers/SM.md` | `13d29b79536f017b85ed3a098ed71fa523cb869b86e71e16be06a68c6edd2d7c` | `9b4e94b118f933c8f6bbfa5e0a3b24f7f83c9e0ebcd62a288a90dffde9b5f230` |
>    | D404 | `book/ch09-universality.md` | `8eb676bc135a4dcb4b48b654894ca36f5a0e24c1e09f5596c4f7267d37bd6284` | `b88d10778c8dc87370c5109a846d07d232116e735db5432e4dd2490b49df88fe` |
>    | D405 | `book/The-Incompleteness-of-Observation-FULL.md` | `8eb676bc135a4dcb4b48b654894ca36f5a0e24c1e09f5596c4f7267d37bd6284` | `b88d10778c8dc87370c5109a846d07d232116e735db5432e4dd2490b49df88fe` |
>    | D406 | `book/ch19-open-problems.md` | `9890b8e5e5101e09af0a8f72f9575321c2892d16bbb8511b3707783dcaa19d68` | `4ddee078457fb2cc5cfcef75b2b0a52036b7483fc0124a40c9e5b0aae4e1cc9b` |
>    | D407 | `book/The-Incompleteness-of-Observation-FULL.md` | `9890b8e5e5101e09af0a8f72f9575321c2892d16bbb8511b3707783dcaa19d68` | `4ddee078457fb2cc5cfcef75b2b0a52036b7483fc0124a40c9e5b0aae4e1cc9b` |
>    | D408 | `book/ch19-open-problems.md` | `085a5e05d6e02f7ce357fd0bef703c27fab50937c99b261c7c6269f8066a8c6d` | `2ba6e306addc5776dbe65b83c8a98386134502ff8262d8b24c77bd9319c6980b` |
>    | D409 | `book/The-Incompleteness-of-Observation-FULL.md` | `085a5e05d6e02f7ce357fd0bef703c27fab50937c99b261c7c6269f8066a8c6d` | `2ba6e306addc5776dbe65b83c8a98386134502ff8262d8b24c77bd9319c6980b` |
>    | D410 | `papers/SM.md` | `61aee339b7b5fd2258bc76da5f5536f9b7767d50d8d495da76839a2ac39e1a14` | `60165e7ced64da66c2da633a41acb475290fa7a6429712c762c1f3d350bc0582` |
>    | D411 | `papers/SM.md` | `d19aeb52bf949a18fd801ae3981493a6bc7cc29e2c4b8058230f1676f811dfea` | `ec826227c78a97aa02321a0f6bb751cd7b2be4c2fce018c3802407ce837591f9` |
>    | D412 | `papers/SM.md` | `84248f693bafe923251c44979e5382f7d0f1a5cc0361f2e34cb99c85cb1875bc` | `758c165782d84541bf4e4c2612d50adb5d3710da0c4949bccc5669b8d8e82210` |
>
>    The adopted texts are those of `O13-INVENTORY-r5.md` Appendix A (sha256
>    `440934e5efb725ac2aec9fae994f4e24467965146b8f8e99a6e653b33909be8a`). Independent non-author review: `review-r4/review.md` (sha256
>    `be8879aa6f86d97581c39f5e025fa152b42f9a09b36c02c51ce912ab9b2183f4`), verdict ACCEPT-WITH-NITS, and, for the
>    corrections of r5, `review-r5/review.md` (sha256 `1ed3d4bf6a75c07fede5669a6d5b3c47f3da075078b6574efe851277dbeff1b6`), verdict ACCEPT-WITH-NITS. If any later revision changes a hash above, this decision does not apply to it.
>
> 2. **Limited supersession.** My decision of 2026-11-23 (#1169 c.7093128173) states: "No change to the ledger base H
>    `53c6601a10419b6b333cc992474272501ab542af`, the 399 ledgered splices or any scientific conclusion is authorized."
>    - For the eleven edits listed in item 1, and for them only, this decision supersedes the words "or any scientific
>      conclusion".
>    - The ledger base H and the 399 ledgered splices remain unchanged and protected.
>    - Every scientific conclusion not changed by those exact bytes remains protected by c.7093128173 as written.
>    - Any change to the old or new bytes of D402–D412, and any further edit, needs a new owner decision.
>    - Adding the splices of D402–D412 to the ledger leaves each of the 399 ledgered splices byte for byte unchanged
>      and is not a change to them; the words "the ledger base H" and "the 399 ledgered splices" of c.7093128173 are
>      not superseded.
>    - The frozen plan `4c79be642ca631573f06b444903be75ec4f5e2b6` and the trials T0′ and T1′ of that plan remain
>      unchanged. Their three workflow runs are all kept as historical evidence of what they tested.
>    - **Run 45077568347 is the T0′ trial.**
>      - It ran `A1-EXIT trial verify` (`.github/workflows/a1exit-trial-verify.yml`), `workflow_dispatch` from `main`
>        at `413b0bb8`, with trial commit T0′ `02172b20` and plan `4c79be64`, on 2026-11-22T22:24:42Z.
>      - Host conclusion: **failure**. This is the outcome preregistered for T0′ (§31.8; N1). Step 9 `preserve`
>        failed only on the committed-PDF comparison, and step 13, the final gate, failed.
>      - `preserve_check.py --expect-trial T0` gave TRIAL EXPECTED, RESULT PASS. Its record is #1169 c.7087039188,
>        which states "Unexpected failures, unexpected skips, infrastructure problems or missing evidence: none" and
>        "T0' acceptance awaits the owner's decision".
>      - The owner accepted it as the T0′ trial in session, as recorded at #1169 c.7088175248: "Owner decisions in this
>        session accepting the T0' trial (run 45077568347, recorded at c.7087039188)".
>    - **Run 45080985924 is the T1′ trial.** It ran the same workflow, `workflow_dispatch` from `main` at `413b0bb8`,
>      with trial commit T1′ `14ac71b4` and plan `4c79be64`, on 2026-11-22T23:02:06Z. Host conclusion: success.
>      `--expect-trial T1` gave TRIAL EXPECTED.
>    - **Run 45083256017 is the T1′ verification.** It ran `verify` (`.github/workflows/verify.yml`),
>      `workflow_dispatch` on `trial/a1exit-T1prime-4c79be64` at T1′ `14ac71b4`, on 2026-11-22T23:26:21Z. Host
>      conclusion: success, 41 of 41 jobs. It is the `verify.yml` dispatch on T1′ that the T1′ procedure requires
>      (§31.8), and `--expect-verify` gave TRIAL EXPECTED (#1169 c.7088175248).
>    - None of the three runs is acceptance evidence for the amended plan. The T0′ run's failure conclusion is kept
>      as recorded. It is neither discarded nor presented as acceptance evidence.
>
> 3. **Basis.** The edits correct the stated scope and dependencies of existing conclusions; they establish no new
>    scientific result, and none of them may be cited as one. None strengthens a claim.
>    - They state dependencies that the cited derivations already use.
>    - They name previously unstated hypotheses, and they state the existing A1 dependence of the action-scale and
>      Bekenstein-Hawking relations (H-count).
>    - They mark unresolved dependencies, and they name sets the corpus already enumerates. These are classified in
>      `O13-INVENTORY-r5.md`, sha256 `440934e5efb725ac2aec9fae994f4e24467965146b8f8e99a6e653b33909be8a`.
>    - "No use of A1 found in the cited derivation" is not a finding that any prediction is independent of A1. No
>      manuscript text adopted here states such independence.
>    - Independent review: independent non-author reviewer, `review-r4/review.md`, sha256
>      `be8879aa6f86d97581c39f5e025fa152b42f9a09b36c02c51ce912ab9b2183f4`, verdict ACCEPT-WITH-NITS; for the
>      corrections of r5, `review-r5/review.md` (sha256 `1ed3d4bf6a75c07fede5669a6d5b3c47f3da075078b6574efe851277dbeff1b6`), verdict ACCEPT-WITH-NITS.
>
> 4. **Item 7.** Item 7 of the frozen plan's §11 is unchanged.
>
> 5. **What this does not authorize.** It authorizes no plan amendment, re-freeze or designation of `F`, no trial, push,
>    dispatch, execution or merge, and no premise change. Each keeps its own approval under AGENTS.md §A.50. The edits
>    take effect only through a later, separately approved amendment and freeze, and through the retirement's own
>    execution and landing.
