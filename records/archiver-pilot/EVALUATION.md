# Log-archiver pilot: run 39005152534 (evaluation, off-repo)

**Pilot**
- Commit `05df8cc18e0103ae9f3ffbf52b1ecb6a6aedf64b`, parentless, on branch `tmp/log-archive-20261017`; the reviewed commit, unchanged.
- Run 39005152534 (push), 05:08:17–05:09:54Z, conclusion success.
- Jobs: Archive batch 117315985870 and Verify 117316231942.

| Owner's criterion | Result | Evidence |
| --- | --- | --- |
| Workflow | met | Both jobs succeeded and the completeness gate was skipped. The only run created after 03:39Z is 39005152534, on this head and branch. The token printed `Actions: read, Contents: read, Metadata: read`. |
| Attempt semantics | met | `zip:38245409846:1` has 68 members, 34 top-level job logs for 34 jobs. `zip:38245409846:2` has 4 members, 2 job logs for the 2 re-run jobs: Lean kernel check (114806712435) and Mathlib bridge (114806712746). The other 32 attempt-2 jobs are copies: each per-job log is byte-identical (same sha256) to its attempt-1 original. Attempt 1's Lean kernel check (114797918517) and Mathlib bridge (114797918557) logs differ from the re-runs', as expected. |
| Integrity | met | Archive job: 83 archived (5 zips, 78 job logs), 0 failed, 0 unavailable, 0 head mismatches, 0 re-hash mismatches; completeness 92 required, 0 missing. Artifact digest at upload equals digest at download: `sha256:218e615835b501270797a31ac861bb51c75aadc7096d8932415cd810633f08dc`. The verify job re-read every downloaded file against its download-time record: `VERIFY  HOLDS`, 4 runs, 5 zips, 78 job logs, 13,690,747 bytes. |
| Security | met | The archive job's scan found 0 credential-shaped lines; the verify job's own scan agreed, since HOLDS includes it. Neither job's public log carries a token (masked `***`) or a signed query string. The only storage URL printed is `actions/download-artifact`'s own "Redirecting to blob download url: …/artifacts/<hash>.zip", which has no query. |
| Artifact | met | Artifact 12090461970, `ci-logs-05df8cc1…`, 3,840,244 bytes, 87 files. `created_at` 2026-10-17T05:09:37Z, `expires_at` 2026-10-31T05:09:33Z (14 days); the upload step used `retention-days: 14`. The verify job downloaded it. |
| Independent validation | partly met | See below. |

**What the independent validation covered**
- Job logs, checked from this environment over a channel independent of the runners: the GitHub connector's job-log endpoint, which returns the full log when it has 5,000 lines or fewer.
- Four of the 78 archived job logs, re-served and hashed here. Each served text plus the one trailing newline the connector drops gives exactly the archived sha256 that the verify job computed from the downloaded artifact.

| Job | Lines | Bytes | sha256 |
| --- | --- | --- | --- |
| 114806766436 | 1,295 | 480,379 | `4422dc48…` |
| 114797918621 | 298 | 215,967 | `4e0af54a…` |
| 114797918729 (original) | 636 | 121,305 | `689d18bf…` |
| 114806714134 (copy) | 636 | 121,305 | `689d18bf…` |

- The served texts are kept beside this note as `served-*.txt`.

**What it did not cover**
- The zips and the artifact itself. Both download from `*.blob.core.windows.net`, which this environment's proxy blocks, and no workaround was attempted.
- Their check therefore rests on the verify job: a separate runner, code that shares nothing with the fetcher, and expectations derived from the host.

**Not done or authorized:** durable publication; a second batch; any further push to the branch.
