# Owner decisions: implementation correction 2 (owner amaybaum, 2026-11-24, coordinating session)

Basis: review-corr1/review.md sha256 3b99a0899d7cd5b167fa9f557461ea901540f551f85d997cdc8cc9f69c47a68f (REJECT on R-B1).

Quoted decision:
"Approve Correction 2, choosing option (a) for R-B1 and option (b) for D-2.
| R-B1 — Import restriction | Option (a). Enforce the standard-library restriction and test it. |
| D-2 — Workflow commands | Option (b). Correct them now to match the r5 plan requirements, including --certified C. |
| controls.json | Update the four affected rows. |
| C04 — Owner-name test | Add the missing test. |
| C08 — System Git configuration test | Add the missing test. |
| C11 — Import-check coverage | Address through the R-B1 correction and its negative control. |
| Other nonblocking observations | Record them; do not expand the correction scope. |
Authorize one bounded Correction 2 commit on top of 3184c7f9.
1. R-B1: Select option (a). Enforce the standard-library import restriction, including exclusion of installed-package directories. Add the negative control and confirm that all legitimate imports remain accepted.
2. D-2: Select option (b). Correct the fixed workflow commands to match the r5 configuration's paths and arguments. Restore the required classification operations and include --certified C in the landing check. Preserve Reading 3 where the reviewer confirmed no correction is necessary.
3. Update the EI5, EI6, EI7 and GV4 rows in controls.json to match the implemented controls.
4. Add the C04 and C08 tests. Address C11 through the R-B1 correction.
5. Record the remaining nonblocking observations without expanding the implementation scope.
6. Re-pin the affected files, regenerate the configuration in a separate directory and rerun the full suite.
7. Obtain a focused independent review of the exact correction commit.
Preserve all existing scientific and technical guarantees. Do not amend the frozen A1 plan.
No further design revisions, optional optimization or unrelated changes are authorized.
Implementation acceptance, push, real-GitHub CI execution and merge remain separately authorized actions."

## Review criteria for the correction-2 focused review (owner, 2026-11-24, quoted)
"The final review should confirm that: The import restriction is actually enforced. All 18 workflow commands perform their intended checks against the amended plan. The three previously surviving mutations are now detected. All existing verification guarantees remain intact. No unrelated changes have been introduced. No further optional improvements or design revisions are needed."

## Disposable CI validation run (owner, 2026-11-24, quoted)
"Authorize one disposable CI validation run, subject to completion of the current local suite and successful independent review of the exact Correction 2 implementation commit.
Requirements:
- Create a disposable CI branch from the exact reviewed implementation commit.
- Add only the temporary workflow required to execute the validation suite.
- Verify the additional commit contains no other changes.
- Run the full suite, A1 controls, mutation tests and applicable real-GitHub controls.
- Use a hash-verified configuration and full Git history.
- Record the exact commits, workflow, environment, results, runtime and resource consumption.
- Explicitly mark TR5, G-A1 and EI14 as deferred to post-landing validation.
- Preserve the disposable branch and its evidence.
Authorize the single push that triggers this validation run.
Keep the actual tool branch unchanged. Do not open a PR, merge, dispatch additional runs or modify the frozen A1 plan.
This validation does not replace final implementation acceptance or post-landing workflow validation."
