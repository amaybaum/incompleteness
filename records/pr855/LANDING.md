# PR #855 landed on main (2026-10-17 06:28Z)

- **Owner's approval:** "MERGE APPROVED … merging PR #855 at the exact reviewed head
  `8021c1fc4625831c0362ebbd4019ca2fb5e593af`."
- **Pre-merge check** (held): `main` at `66a981d5a9cab35b9ebd253aa0e610c0afbfefb6`, PR head and `refs/pull/855/head` at
  `8021c1fc`, and the base an ancestor of the head.
- **Merge:** marked ready for review, then merged with the repository's merge-commit method, with the head SHA pinned
  (`expectedHeadSha`).
- **Landing commit:** `ea3155fdd7bf1d57ac285303c68ccba529e25b61`, "Merge pull request #855: provenance errata, five cited
  run heads that name no commit".
  - Parents: `66a981d5` (main) and `8021c1fc` (the reviewed head).
  - Tree: `4f3ca10023ebf549aee2c37d90b20d124d9abe12`, byte-identical to the reviewed head's tree.
  - Content: 58 files added (+2,933 lines), all under `verification/audits/provenance-errata/`, with none modified or
    deleted. Nothing outside that directory changed.
- **Push CI on main:** `verify` run 39010013932 at `ea3155fd` succeeded. There were 22 successful jobs and one
  expected skip, including the numerical-probes rollup. All 22 release-gate steps passed; `lean-axioms` reported
  5989 named results, all 48 receipts held, and the 303 legacy records were intact.
