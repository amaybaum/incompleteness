# GitHub-native raw-log archiver: design (not deployed)

## Status

Designed and locally tested only. The branch is not pushed, nothing is dispatched or published, and nothing on
`main` changes.

## Where it runs and why it needs no change to `main`

The repository already runs push-triggered workflows that exist only on disposable branches, for example
`finite-reconstruction-design.yml` (36 runs) and the `rebuild-pr8xx-pdfs.yml` builds. The archiver follows that
pattern:
- **The branch.** It is a parentless commit on a `tmp/log-archive-<date>` branch, holding only the workflow and the
  archiver. `verify.yml` is not on that branch, so pushing it starts nothing else.
- **The trigger.** It runs on `push` to `tmp/log-archive-*`.
- **Batches.** Each batch is one push that changes `archiver/batch.json`. The concurrency group runs them one at a
  time.

## Permissions

The token carries `actions: read` and `contents: read` only, so the workflow cannot write to the repository, create
refs or publish releases. Log downloads go from GitHub's own runners to GitHub's log storage. This environment's
proxy blocks that storage, but GitHub's runners are not behind it. The first test run must confirm that the runners
can reach it.

## What each batch records

The manifest records, per run:
- the run's `head_sha` (checked against the inventory) and its `run_attempt`;
- per attempt: the job list (ids, names, status, conclusions, head_sha), the log zip's sha256 and size, every
  member's name, size and sha256, the CRC result, and the completeness flag (top-level job logs against the jobs
  that ran);
- per cited job: the plain-text log's sha256, size and line count;
- every failure, with the host's answer. Signed-URL parameters are redacted before anything is recorded.

## Verification

- **Job 2 (GitHub-side).** It downloads the uploaded artifact and re-hashes every file against job 1's record.
  `--require-clean` fails it on any re-hash or head mismatch.
- **From this environment.** I can read both jobs' summaries through the job-log API and compare them line for line.
  I cannot download the artifact itself, because artifact downloads go to the blocked storage host.

## Durable publication (phase B: a separate decision, not built)

Workflow artifacts on a public repository expire after at most 90 days, so they are a staging area, not
preservation. There are two durable options, both needing `contents: write` and your separate authorization.

| Option | Durable | Effect on clones | Verifiable from this environment | Notes |
| --- | --- | --- | --- | --- |
| Release assets, one release per batch on a tag at the archiver commit | yes | none | no: asset downloads go to a blocked host; a GitHub-side job re-hashes them instead | creates a tag; 2 GB per asset limit; nothing enters git history |
| An evidence-only ref with the zips committed | yes | a branch is fetched by every default clone (`git clone` takes all branches), so roughly 1 GB would reach every clone; a non-branch namespace (`refs/evidence/*`) avoids that, but whether the host accepts a push there is untested | yes: `git fetch` works here, so I could re-hash every file locally | puts the bytes in git; size is permanent |

Recommendation: release assets for the bulk zips. Keep the small manifests and summaries on a tracked path so the
evidence-retention tranche can cite them by digest. The final choice is yours.

## Test batch, after #854's heavy runs finish

| Run | Why |
| --- | --- |
| 35351379664 | rank 1: the oldest tier-A run (push, 2026-09-18) |
| 35436171509 | rank 5: a tier-A `pull_request` run |
| 36247320536 | rank 39: a failed run whose head is unreferenced on the host |
| 38245409846 | a run with two attempts (R1-covered; it tests the per-attempt path) |

**Success criteria:**
- every zip passes its CRC test and the completeness check;
- every head matches the inventory;
- job 2's re-hash is clean;
- the two jobs' summaries are identical;
- no signed URL appears in any log.

The test also measures zip sizes, which fixes the batch size and the volume estimate for publication.

## Fallback

If the runners cannot reach the log storage either, the archiver falls back to the served job-log text through the
API: at most the last 5000 lines per job, labelled as served text with its own digest, never as the raw log. It
would be used first for the highest-risk runs.

## Local evidence

- The fetcher's self-test passes against a stub `gh`. It covers:
  - priority order and explicit ranks;
  - run metadata and the head check;
  - every attempt and all job pages;
  - skipped jobs and the completeness flag;
  - 404/410 versus failure, and signed-URL redaction;
  - per-job logs, resume, an interrupted pass and re-hashing;
  - the scan without echo, and the tier filter.
- `select_batch.py` produces the 4-run test batch and a rank range.
- The workflow YAML parses.
- No real download has been made: this environment cannot reach the log hosts.
