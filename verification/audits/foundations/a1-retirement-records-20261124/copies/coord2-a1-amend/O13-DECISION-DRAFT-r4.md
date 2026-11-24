# O-13 decision, draft for the owner (r4): paper-only, not a decision

**Use.** This is draft wording for the owner to adopt, amend or reject. It is not an owner decision, and nothing here
is recorded on GitHub. Bring it for approval together with the independent review verdict on r4, which is pending: a
non-author review of `PROPOSAL-r4.md`, `O13-INVENTORY-r4.md` and `diffs-r4/`.

**Fill in before posting.**

- The independent review of r4: reviewer, file sha256 and verdict.
- The final r4 file hashes, if a later revision changes them. The digests below are those of r4.

***

## Draft wording

> **Owner decision (O-13): adoption of the A1-plan manuscript edits D402–D412, and a limited supersession of the
> scientific-preservation clause.**
>
> 1. **Adopted edits.** I adopt, as part of the amendment to the A1 retirement plan in preparation, exactly the
>    eleven edit records D402–D412 of amendment proposal r4, and no others.
>    - Each is identified by its file, its old bytes at the ledger base H `53c6601a10419b6b333cc992474272501ab542af`,
>      and its new bytes, through the sha256 values below.
>    - They are contained in the edit list `edits.json` with sha256
>      `19eb79bd478275110b4ff1cd3ae2271c37574e849d45be272f53b8e75e726b4b`, and in the exact-edit ledger `ledger.json`
>      with sha256 `d20495f0084f29ac5c58c5a0480be5f0ed342334381e6680e9cca58952940976`.
>    - That ledger has 410 splices in 44 files: the 399 splices of the frozen plan `4c79be642ca631573f06b444903be75ec4f5e2b6`,
>      unchanged byte for byte, and the splices of D402–D412.
>
>    | Edit | File | old_sha256 | new_sha256 |
>    |---|---|---|---|
>    | D402 | `papers/SM.md` | `227117bc96e597894158fe4ba53ceb3b0c426e3a7f6ed5f414698db95e08d3c6` | `c46d5981668cd855168395667e9ed51cf12fa62295e3addedc1a6d50b5a071d9` |
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
> 2. **Limited supersession.** My decision of 2026-11-23 (#1169 c.7093128173) states: "No change to the ledger base H
>    `53c6601a10419b6b333cc992474272501ab542af`, the 399 ledgered splices or any scientific conclusion is authorized."
>    - For the eleven edits listed in item 1, and for them only, this decision supersedes the words "or any scientific
>      conclusion".
>    - The ledger base H and the 399 ledgered splices remain unchanged and protected.
>    - Every scientific conclusion not changed by those exact bytes remains protected by c.7093128173 as written.
>    - Any change to the old or new bytes of D402–D412, and any further edit, needs a new owner decision.
>
> 3. **Basis.** The edits narrow or make explicit; none strengthens a claim.
>    - They state dependencies that the cited derivations already use.
>    - They name previously unstated hypotheses, and they state the existing A1 dependence of the action-scale and
>      Bekenstein-Hawking relations (H-count).
>    - They mark unresolved dependencies, and they name sets the corpus already enumerates. These are classified in
>      `O13-INVENTORY-r4.md`, sha256 `497950bd721b9cdbaffd3f1d8a3174fc53fe91b8c100468186f0362c42902458`.
>    - "No use of A1 found in the cited derivation" is not a finding that any prediction is independent of A1. No
>      manuscript text adopted here states such independence.
>    - Independent review: <reviewer, file and sha256, verdict>.
>
> 4. **Item 7.** Item 7 of the frozen plan's §11 is unchanged.
>
> 5. **What this does not authorize.** It authorizes no plan amendment, re-freeze or designation of `F`, no trial, push,
>    dispatch, execution or merge, and no premise change. Each keeps its own approval under AGENTS.md §A.50. The edits
>    take effect only through a later, separately approved amendment and freeze, and through the retirement's own
>    execution and landing.
