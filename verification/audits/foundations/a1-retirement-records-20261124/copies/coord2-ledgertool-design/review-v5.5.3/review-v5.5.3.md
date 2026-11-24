Narrow confirmation of DESIGN-v5.5.3 (reopened for K7 only)

Verdict: ACCEPT

Reviewer: the independent, non-author session that wrote review-v5.5 to review-v5.5.2.

Limits kept:
- read-only;
- no repository, git or GitHub write;
- no workflow run and no host call;
- new files only under `D/review-v5.5.3/`.

Date 2026-11-23.

Inputs (sha256, verified; all match the coordinator's values)

- DESIGN-v5.5.3.md 99e9ce3af5476e2ea4be1cab911e1aa2cf1c2d3b3a9bf7cf06fcb2f8cbfe3379
- CHANGES-v5.5.3.md a2b6ad472fbb43a05806c74295066ad2b2f970c8205e4c479f86b2ab9e6e7d63
- Base: DESIGN-v5.5.2.md 835ff356200349db7689ea41ce936349015fb70f47b35a508945d681a8604323

Stopping rule as approved: a finding blocks only if it is demonstrated or reproducibly supported, and it violates an existing requirement or an agreed pass condition.

1. K7 is resolved as the owner required

Sec. 6.3, trust-root point 3, replaces "with no further file under `tools/ledger_coverage/`" with an explicit list. Besides the files `A.engine_pins` names, exactly two files are permitted under the directory, each only at its own path and only as a regular file:

- **The authority record** at `tools/ledger_coverage/authority.json`. Its blob sha256 must equal that of the `A` admitted for the run.
- **The workflow** at `A.workflow.path`, if that path lies under the directory. Its content sha256 must equal `A.workflow.content_sha256`, the same pin point 3 already checks.

Every other file under the directory refuses the run, including a second copy of either permitted file at another path. A permitted path with different content, or holding a symlink, submodule or other non-regular entry, also refuses.

Against the owner's requirements:

| Requirement | Met? |
|---|---|
| The authority record permitted at its path | yes |
| The workflow permitted at its separately pinned path | yes |
| Both subject to exact content-hash verification | yes |
| Every other unapproved file prohibited | yes |
| An explicit allowance for these two components only, not a general exception | yes, stated in so many words |
| No identity, admission or authorization safeguard weakened | yes: the allowance only lets a file pass when its hash equals an already-verified pin, and nothing else in sec. 6.3 changed |

The writer's two interpretations:

- **The authority record verified by blob equality with the admitted `A`.** This is sound. `A` is admitted from `main` through the full authority-change chain, so equality with it is the strongest available check, and no new trust is introduced.
  - Consequence (Note A): if `A` changes on `main` between the run's `head_sha` and admission, through a properly approved change, the run is refused and must be repeated. This fails closed and is consistent with the owner's requirements. Not a defect.
- **A symlink, submodule or non-regular entry at either permitted path refuses.** This is sound, and it reads "substituted" in the strict direction. It weakens nothing.

2. Controls TR48-TR53 cover the cases

| Control | Case |
|---|---|
| TR48 | the positive control: exactly the pinned files, plus the approved authority record (blob equal to the admitted `A`) and the approved workflow if it lies there, is accepted |
| TR49 | a modified authority record is refused |
| TR50 | a modified workflow is refused |
| TR51 | a substituted file at either permitted path is refused, whether it has different content, is a symlink or is a submodule |
| TR52 | an additional unauthorized file is refused |
| TR53 | a byte-identical second copy of the authority record at another path is refused |

Together these cover the owner's list: a valid tree accepted, and modified, substituted and additional unauthorized files rejected.

3. The diff

`diff DESIGN-v5.5.2.md DESIGN-v5.5.3.md` has exactly 5 hunks:

1. the title;
2. the status bullet recording the K7-only reopening;
3. sec. 6.3 point 3, the K7 rule;
4. TR48-TR53, inserted after TR47;
5. the S13 list, from TR1-TR47 to TR1-TR53, a necessary consequence.

Nothing else changed. K1 and every other rule, form, control and count are untouched.

Notes (not blocking under the stopping rule)

- **Note A.** A valid run whose `head_sha` predates an approved change to `A` is refused, as described above. This is fail-closed, and the owner may simply note it.
- **Note B: the scope of `engine_pins`.** The field is defined as "every file of `tools/ledger_coverage.py` and `tools/ledger_coverage/` that the run executes". The Stage 1 tree (8c1e628a) also holds a data file under the directory, `engine/schemas/oi-ledger-coverage-4.schema.json`, which the tool reads but does not execute.
  - Under K7's rule, an `A` whose pins cover only executed files would refuse every run.
  - TR48 already defines a valid tree as one whose files are all pinned, and the reviewers of `A` can pin the schema, so this is not a demonstrated failure.
  - Optional: reword `engine_pins` as "every file under `tools/ledger_coverage/` and `tools/ledger_coverage.py` that the run executes or reads (code and data)". That would remove the ambiguity, and it is the same kind of issue as K7.
- **Note C.** The rule for non-regular entries applies explicitly to the two permitted paths only. For an `engine_pins` path, a submodule has no content, so its pin fails. A symlink resolves to the same pinned bytes, so the executed code is unchanged. Neither is exploitable. Optional: state the regular-file requirement for every pinned path, for consistency.

Not verified

- No implementation exists, so the controls were checked against the rules, not run.
- No host behaviour was exercised, for example how the host's contents API reports symlinks and submodules.
- The owner decision carries no comment id.

Files (D/review-v5.5.3/; MANIFEST.sha256 covers them)

- `review-v5.5.3.md`.
- `diff-v552-v553.txt`.
