# Response to the focused review of S3-PLAN-r5

**UNREVIEWED.** This is the writer's disposition of `REVIEW-S3-PLAN-r5.md` (ACCEPT WITH CHANGES at
`ac70c70a`), with the root-cause sweep the coordinator asked for. The changes are in `S3-PLAN-r6.md`.
`S3-PLAN-r5.md` is left unchanged (SHA-256
`b61c5c497c70decb4f9777a290e1d19d824f30d689cdef33014287757ce17882`).

## R6 and its root cause

**R6.** Confirmed against r5. The native-marker miss branch could be reached with an assumed retention
of `s_A` and still count toward (a′).

**Root cause.** R5 and R6 are the same defect: a negative outcome counted toward closing route M
while it rests on an unsourced or assumed capability.

**Fix, NC-1** (§8.6). A negative outcome counts toward closing route M, or toward any other negative
closure in the plan, only if every capability it relies on is sourced under the §3 criterion. That
covers preparations, markers, retention, erasure, settings, renewal and the quantum references.
Otherwise it is reported as *unsourced* or as concerning an *assumed apparatus*, and it does not
count. The conditioning reading (α) is not a capability: outcomes are counted per reading of P-vii.

## Every site checked

| # | Site in r6 | Counts toward a negative closure? | Change |
|---|---|---|---|
| 1 | §8.4 check 1, the (β)–(δ) coupling bullet | Feeds D-1's outcomes | None needed: R5's "unsourced at (β)–(δ)" rule stands |
| 2 | §8.4 check 1, outcome "Undecided at (γ)" | No | None |
| 3 | §8.4 check 1, outcome "Unsourced at (β)–(δ)" | No, by R5 | None |
| 4 | §8.4 check 1, outcome "Empty on K1" | Yes | It now also excludes a (β) failure resting on any other unsourced or assumed capability (NC-1) |
| 5 | §8.4 check 1, miss branch, *native marker* | Yes | **R6 applied:** it needs a sourced retention of `s_A`, and an executable uncomputation for the erasure it compares against. If either is assumed, the miss concerns an assumed apparatus, is reported as such, and does not count toward (a′) |
| 6 | §8.4 check 1, miss branch, *quiet marker* | No | It now says explicitly that it does not count toward (a′) |
| 7 | §8.4 check 1, "Why the test is nontrivial" | Its falsification sentence states what a miss falsifies | "A miss" → "A miss that counts under NC-1" |
| 8 | §8.4 checks 2–7 | No: they record dependencies and read records | None |
| 9 | §8.3 Point 1, configuration-level conclusion | No: definitional, and not counted toward closure since r2 (F1(a)) | None |
| 10 | §8.3 Point 2, "U and P are not shown available" | No: a record of status, not a closure | None |
| 11 | §8.6 (a′) | Yes | It counts only "empty on K1", or a native-marker miss with sourced retention and executable erasure once (γ) is supplied. A miss resting on assumed retention, erasure or a quiet marker leaves route M open |
| 12 | §8.6 (b′), observer-level lift | Yes | A "no operator" result counts only for a reason other than an unsourced capability. Otherwise it is "unsourced" |
| 13 | §8.6 (c′), σ12 screen | Yes | Any negative must rest on sourced capabilities only (NC-1) |
| 14 | §8.6 (d′), soundness reduces to §§3–4 | A reduction, relying on no capability | None |
| 15 | §8.6 (e′), returned interference | Yes, via M-1 and M-2 | It counts only where the cited generalized-noncontextual model is fully specified. M-1 and M-2 need an MR-1 stage-2 authorization, so (e′) is reported as pending until then |
| 16 | §8.6, "U4 alone cannot close route M negatively" | No | None |
| 17 | §8.6, the Stop (non-functional record) | No: a stop | None |
| 18 | §4.1 H-RR, "Would refute it" | Yes: a negative closure of H-RR | Each refutation route now requires sourced operations: for the PR execution, for the quantum Bell reference, and for both sets of operations in the cost comparison. A refutation relying on an unsourced or assumed capability is reported as such and does not refute H-RR |
| 19 | §4.1 H-RR, "Leaves it undetermined" | No | None |
| 20 | §4.1 H-RR, "Would support it" | No: positive, not a closure. It already requires the model's own production of fresh cells | None |
| 21 | §9, AC-1, "reported as failing AC-1" | A negative finding about a restriction's *content*: it disables operations the quantum references need. It does not rely on an executed capability | None |
| 22 | §9, U4 row | Yes, for any negative it reports | "Any negative it reports counts only under NC-1 (§8.6)" added |
| 23 | §9, U1–U3 rows | No: definitions, ledgers and requirements | None |
| 24 | §8.5, negative controls M-7, M-8, M-1 to M-3 | They are controls, not closures. Their use in (e′) is covered by site 15 | None |
| 25 | §10, owner question 6 (D-1's consequence) | It states D-1's miss outcome | "If D-1's identifications hold" → "If D-1 ends in a miss that counts under NC-1" |
| 26 | §2, the #866 and #913 statuses (NOT PASSED, stopped) | They are records of other Issues, not closures made by this plan | None |

The revision header lists the sites changed. Nothing else changes.
