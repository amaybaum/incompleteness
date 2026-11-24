Bounded confirmation of DESIGN-v5.5.1 against review-v5.5

Verdict: ACCEPT

Reviewer: the independent, non-author session that wrote review-v5.5.

Limits kept:
- read-only;
- no repository, git or GitHub write;
- no workflow run and no host call;
- new files only under `D/review-v5.5.1/`;
- my own scripts only, which import P's frozen `edits_check.py` after checking its hash.

Date 2026-11-23.

Inputs (sha256, verified; both match the coordinator's values)

- DESIGN-v5.5.1.md 8befd35c74b8e4dfa241e360d891de3222b3f878ca2aaf23ceaae1d00fbed649
- CHANGES-v5.5.1.md 89629ad8e286dac897ef30f8d46bde54307301a44426ad25f00f07e1e26ddd4c
- Base: DESIGN-v5.5.md 74db584a5bdb861519f9703e3b5d102ba07a60dfd0e8f89ea183bd89a80b52a4
- Review: review-v5.5/review-v5.5.md 8c77254a7291e75fe8caff01185e3f9896ace2a18a881497241fc4c51cc5f9ac

Scope: F2, F1 and N1 of review-v5.5, and that the diff changes nothing else. Stopping rule as approved: a finding blocks only if it is demonstrated or reproducibly supported, and it violates an existing requirement or an agreed pass condition.

1. F2: resolved

- **The snapshot.** Sec. 6.3 now adds "the delegated evidence", for every delegated and native class, at `X` and, where `C` differs, at `C`. It contains:
  - the host records the tool read, as returned and in canonical JSON: run and job records with ids, `head_sha`, workflow path, names and conclusions, and the artifact record for `pdf`;
  - the sha256 of every artifact and result file used;
  - for every native checker run: the checker blob sha256, command line, working directory, exit status, and the complete bytes of each result file and of each output the class compares (SC-42's `--verbose` and `--self-test` outputs, `proof_census.py --json`, and preserve_check's result files);
  - the class's recorded re-derivations.

  This covers what sec. 7.2 and 7.3 decide from.
- **Replay.** Sec. 5 now decides every class of an op-C replay from the snapshot's delegated evidence, with no host call, clone, PDF build or checker run. It re-applies the tool's verification rules of sec. 7.2 and 7.3 to the recorded data and the git objects, requires each recorded result file to hash to its recorded sha256, and requires byte-for-byte equality, apart from the admission field, for op B, op C and op D results.
- **TR45.** It now covers an op-B result and an op-C result across all six classes. It requires equality and non-acceptance, and it makes the replay refuse when a recorded file does not match its hash or when the evidence for a class the result decided is missing.

R-D5's condition, that an accepted result can be regenerated from preserved inputs independently of temporary CI artifacts, is met. Not blocking.

2. F1: resolved

S11-58k is now fully specified: `H` = `"ab qc"`; edit 1 `{old: "ab q", new: "xy"}`; edit 2 `{old: "qc", new: "Q", old_step2: "yc", new_step2: "Q"}`.

Verified with P's own `variant()` and P's application, and with my implementation of the v5.5 rule (`rv551_s1158k.py`):
- at `H`, P selects edit 2's `old`;
- after edit 1, P selects `old_step2`;
- P applies the list with result `"xQ"`;
- my v5.5 rule refuses it as chained.

The expectation "ERROR `SOURCE_CHANGED` naming edit 2 (chained); P applies the list, with result `"xQ"`" therefore follows from the rules.

3. N1: resolved

Sec. 6.1 (iii) now also covers an occurrence that "spans the point where an earlier edit's image, possibly empty (a deletion), was inserted; in the segment model it then crosses more than one segment". This matches the binding rule and my crafted deletion case in review-v5.5.

4. Nothing else changed

`diff DESIGN-v5.5.md DESIGN-v5.5.1.md` has 7 hunks:

1. the title;
2. the status note, which lists F2, F1 and N1 and cites review-v5.5 by hash;
3. sec. 5, offline replay (F2);
4. sec. 6.1 (iii) (N1, plus the S11-58k reference);
5. the sec. 6.3 snapshot, which gains the delegated evidence (F2);
6. TR45 (F2);
7. S11-58k (F1).

No rule, form, pass condition, other control or count changed.

Findings

None blocking and none required.

Optional and not verified

- Not verified: no implementation of v5.5.1 exists, and no host behaviour was exercised.
- The owner decisions listed in review-v5.5 remain open:
  - the undetected-deletion residual;
  - the three refusals stricter than P;
  - the freeze ledger, and whether acceptance-time appends need their own approval comment;
  - final authorization of the writer's choices.

Files (D/review-v5.5.1/; MANIFEST.sha256 covers them)

- `rv551_s1158k.py` and `out551-s1158k.txt`: S11-58k under P's code and my v5.5 rule.
- `rv55_parity.py`: copied unchanged from review-v5.5.
- `data/`: P's `edits_check.py`, `edits.json` and `ledger.json`.
- `diff-v55-v551.txt`.
