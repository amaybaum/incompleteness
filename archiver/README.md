# Disposable log archiver

This branch holds only the archiver. It has no parent, shares no history with `main`, and is never merged. Its
workflow, `.github/workflows/log-archive.yml`, runs on GitHub's runners on a push to a `tmp/log-archive-*` branch,
and only there.

**What it reads.** For the runs `batch.json` names, it reads through the Actions API, using the job's own token
(`actions: read`):
- each run's head and attempt count;
- every attempt's job list and log zip;
- the job logs the batch asks for: the cited jobs, or with `"job_logs": "all"` every job that ran.

**How it downloads.** The log endpoints answer with a redirect to a short-lived download link. Redirects are never
followed automatically. The link is fetched at once with no credentials, and it is never recorded or printed. The
token goes only to the API host.

**What counts as complete.**
- A zip is complete when it passes its CRC test and holds one top-level job log per job the attempt ran. A partial
  re-run lists the jobs it did not re-run as copies of the earlier attempt's (same name, start, end and runner, new
  ids), and its zip omits them; their logs are in the earlier attempt's zip and, by their new ids, at the per-job
  endpoint. A job cancelled before a runner took it has no log and is not expected.
- An empty job log does not count as archived.
- Every file and zip member gets a sha256, and each run's head must equal the inventory's.
- `completeness.json` lists every item the batch requires and its state. If any is missing or incomplete, the run
  fails, after staging what was received.

**The scan.** A credential-pattern scan covers every log, every zip member and the metadata files, and reports
locations only. Any hit stops the batch before anything is staged.

**Where the batch goes.** It is staged as a workflow artifact, which expires after `retention_days` (1 to 90; 14
by default). On a public repository any signed-in GitHub user can download it until then, and the run's logs and
step summaries are public.

**Independent check.** A second job runs `verify_batch.py`, which shares no code with the fetcher.
- It works out what the batch must contain from `batch.json`, the inventory and the host's own answers.
- It re-reads every staged file against its download-time record, and re-tests every zip's CRC, members and job
  count.
- It fails on anything missing, changed or extra, and on any credential-shaped line.

**What it cannot do.** It cannot write to the repository. It creates no commit, ref, tag or release. Durable
publication is a separate, separately authorized step.

**Running a batch.** Batches run one at a time and an active batch is never cancelled. GitHub keeps only one run
pending per concurrency group, so push a new batch only after the previous run has finished. A batch holds 1 to 25
runs. The fetcher stops at 900 API requests per pass (GITHUB_TOKEN allows about 1,000 an hour), so a large batch with
`"job_logs": "all"` fails closed rather than exhausting the limit.

Files:
- `fetch_ci_logs.py`: the fetcher, with its self-test (local HTTP servers, no network).
- `verify_batch.py`: the independent verifier, with its own self-test.
- `select_batch.py`: turns `batch.json` into the fetcher's input.
- `summarize.py`: a deterministic summary, printed by both jobs.
- `priority-388.csv`: the accepted ranking of the 388 runs without an R1 entry.
- `inventory-runs.csv` and `inventory-jobs.csv`: the accepted inventory.

A batch is selected either by ranks from `priority-388.csv` (`{"source": "priority-388.csv", "ranks": [a, b]}`) or
by explicit run ids (`{"source": "inventory-runs.csv", "run_ids": [...]}`).
