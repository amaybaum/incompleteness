# PR #855: independent acceptance verdict on `8021c1fc` (2026-10-17)

**Verdict: ACCEPT-WITH-NOTES.** It comes from a fresh reviewer that had not worked on #855, and every check was
re-run independently. It is an acceptance verdict, not merge authorization: the PR stays a draft until the owner
decides.

| Condition | Result |
| --- | --- |
| The five entries (PE-1 to PE-5) | **Met.** Citing blob, verbatim line and its sha256, receipt pin, and shared digits (8/8/8/8/7, none a prefix) all match on `main`. GitHub `get_commit` finds no commit for any of the five cited ids; the control `08502810` resolves. Run and job `head_sha` equal the real heads across 3/3/3/13/32 jobs, and job ids, names and conclusions equal `errata.json`. README and json agree cell for cell, and statuses follow the rule table. Content checks were confirmed through git; the PE-4 frozen-edit replay gives `876f2e6d`. |
| PE-3 wording | **Met.** The owner's sentence appears verbatim in the README and in `detail`. Counts recomputed from the served log of job 108596164217 (sha256 `8bcc3331…`): 52 reports with distinct names; 30 with `sorryAx`; 21 with exactly the three standard axioms; 1 with none (`a35_shared_wit_core`). 491:2 is at line 1455 and the timeouts at 646 and 651, with 41 errors. The connector's 5000-line cap does not limit this, since the section starts at served line 520 and the CI's own diagnostics agree. Nothing calls the other 22 proofs. |
| Retained objects | **Met.** 52 files, 444,060 bytes: 7 commits, 37 trees, 8 blobs. sha1 equals the name, each body equals the repository's object, and the manifest equals the directory. The checker holds in a clean copy without the real heads. Credential scan: none. The `Claude-Session` URLs are not credentials. |
| Fail-closed behaviour | **Met** in both settings: removed, corrupted or emptied objects or entries, and wrong or mismatched cells. Each gives FAILS (exit 1) or UNCHECKED (exit 2), and `--require-objects` turns every UNCHECKED into FAILS. |
| Exact-head evidence | **Met.** Run 39006747889, `workflow_dispatch` at `8021c1fc`, has **37 jobs**, all successful. Bridge job 117320660295's release gate shows 22 PASS ("release gate: PASS"), including `lean-axioms` and `evidence-retention` HOLDS. The checkout of the exact SHA is shown in sibling job 117320660243. |
| Scope | **Met.** 58 files added, none modified or deleted, all under `verification/audits/provenance-errata/`. At the head, legacy-records shows 303 intact and v3-receipts 48 holding. |

## Notes

1. **Medium-low.** Consistent *judgment* edits are not detected. A verdict and its status changed the same way in both
   files, or the PE-3 sentence rewritten in both, still gives HOLDS. `ENTRY_IDS` guards the entry set, but not the
   judgment cells or the prose. The documentation does not claim otherwise. A cheap fix, if the owner wants it: pin
   each id's (verdict, explanation, status) in the checker next to `ENTRY_IDS`.
2. **Low.** The exact-head run has 37 jobs; an earlier summary said 30.
3. **Low.** The bridge job's own checkout lines fall outside the served 5000-line tail. The full log is on a host the
   proxy refuses, so the exact SHA rests on the job records plus the sibling job's checkout.
4. **Cosmetic.** The stored workflow blob `876f2e6d` contains a public `elan-init.sh` URL twice. It is not a credential,
   and the README does not mention it.
5. **Info.** Unknown command-line arguments are ignored: a mistyped `--require-object` runs the plain check.
