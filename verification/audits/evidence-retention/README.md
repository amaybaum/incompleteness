# Evidence retention (AGENTS §A.42)

This archive makes the computational claims of records already frozen reproducible from `main`. Those records cite CI runs that GitHub's log retention will delete, and four logs that existed only in a session scratchpad. For each cited run the archive holds the *expected result*: the deterministic outputs the record's claims rest on, in a small structured file, with the commit it holds at and the recipe that regenerates it. A reviewer reproduces a claim by rebuilding that commit, not by trusting a copied log.

It is a governed audit record. It is not a research round and changes no historical result.

- **Frozen records stay unchanged.** No native-round record (`G13`), legacy record or receipt is edited. The manifest maps each citing `file:line` to its retained files, and states which of the claims made there those files carry.
- **No claim is affected.** Nothing here strengthens a claim, repairs a check, or changes what any record says it measured.
- **Retention is not verification.** `tools/v3_verifier.py`'s verdicts are unchanged, and no retained file is a host attestation.
- **Reproduction verifies the stated Lean and CI properties.** Whether the formal statements capture the intended physical claims is a separate scientific question, outside this archive.

## Tranche 1: expected results

| path | what | kind |
| --- | --- | --- |
| `ci/<run>/results.json` | for each of the 96 runs below, the expected result of its Mathlib bridge job: build success, the release gate's steps and verdict, each governed Lean module's `#print axioms` reports with their axioms, and the failure-marker counts; the commit, job and reproduction recipe; and, as provenance, what else the served log showed (build lines, cache lines, the served line of each report) | `derived` from the served log, whose digest is `source_sha256` |
| `ci/<run>/run.json` | the run's identity and outcome (`id`, `head_sha`, `event`, `conclusion`, `run_attempt`, …) | `derived` from a saved runs-API listing page |
| `ci/<run>/jobs.json` | for 57 of the runs, every job with its name, attempt and conclusion | `derived` from a saved jobs-API response |
| `bg3/*.log` | BG-3's four cited job logs, byte for byte: the bridge-log tails of jobs 116826161407 (`E`), 116805436638 and 116761232088 (design trees), and the design-run log of job 116831668411 | `complete-as-cited`: the sole raw artifacts, kept because frozen records name them by digest and assert line positions in them |
| `bg3/results-*.json`, `bg3/run-*.json` | the expected result read from each BG-3 log, and the two design-tree runs' metadata | `derived` |
| `extract_result.py`, `compare_result.py`, `reproduce.py`, `build_archive.py`, `audit/` | the extractor and comparator, the reproduction tool, the script that cut this tranche, and the off-`main` audit at `fc5abade` | `complete`, hash-pinned |

**The 96 runs** are of two kinds:
- every check run that a receipt under `verification/receipts/` records as `F`'s or `E`'s `check-run` attestation (93 runs);
- the three runs CV-1's certificate attestation cites.

They span 2026-09-22 to 2026-10-16.

## Expected results and reproduction

An expected result is read from the served job log by `extract_result.py`, the same extractor that reads a fresh build's output, so the archive and a reproduction are compared on equal terms. **The served log's digest is provenance of the extraction, not independent proof**: the same process wrote the records and this archive. Independent evidence is the reproduction.

`reproduce.py --run <run_id>` performs it: it validates its arguments, checks that the attested commit is in the repository, checks it out as a detached worktree, runs `lean --version`, `lake exe cache get` and `lake --rehash build` in its `verification/lean-mathlib`, runs that commit's own `tools/release_gate.py`, extracts the result, and compares it with `compare_result.py`. It writes the outcome as `verdict.json`: each command's exit code, whether the reproduced build and gate passed, and every comparison failure. It writes it on every exit path once `--work` names a directory it can write: a rejected argument, a missing entry, a failed checkout, and an exception raised by any step, extraction and comparison included, whose type and message it records under `stopped`. `holds` is true only with exit code 0, so an exception still fails closed. The verifier (manifest, extractor, comparator, this tool) is the checkout the command runs from; the historical commit supplies only its sources, its toolchain pin and its gate. The workflow passes its inputs to the shell only through environment variables and validates them (a decimal run id, a full 40-hex commit id) before use; `reproduce.py` validates them again. Each results.json states the same steps as its manual recipe, run from the verifier checkout against a worktree of the commit, never inside the commit, which predates these tools. The `reproduce evidence` workflow (`.github/workflows/reproduce-evidence.yml`) runs exactly this, from Mathlib's cache alone and with no build cache of its own, so the verdict never depends on what an earlier run left behind. A cache miss costs time, never correctness.

**What is compared, and what is not.** `compare_result.py` compares build success; the gate's verdict and every step's name, status and summary; each governed module's reports, declaration by declaration with its axiom list; and the failure markers. Each module's `#print axioms` lines are read from its source at the built commit, not from the expected result: the reproduction must report exactly one report per such line, and the expected result's recorded lines must equal the source's, so the count a reproduction must reach does not rest on archive metadata. It does not compare timestamps, durations, cache behaviour, job counts or output order. It fails closed: a missing report, an unexpected axiom, an axiom outside `propext`, `Classical.choice` and `Quot.sound`, an absent gate step, a changed summary, an extraction without a build line or gate, or any mismatch fails it, and nothing is skipped. Its `--self-test` applies each of these mutations to real expected results, one for each module status, and requires the failure.

**Negative controls.** `reproduce.py --override-sha <commit> --expect-scientific-mismatch [--expect-failure <text>]` builds another commit against the same expected result. The control passes only if every command succeeded and the reproduced build and gate passed there, so that the failure cannot be an infrastructure or build failure, and the comparison then failed on scientific results alone (rules C2–C4), including each expected text. A flag's value may follow it as the next argument or after `=` (`--expect-failure=<text>`); the two forms are parsed identically and give the same verdict. Every argument must be a known flag or a flag's value. An expected text must be non-empty: an empty or whitespace-only `--expect-failure`, in either form, or one without a value, is rejected, since the empty text is contained in every failure; so is an unknown argument such as `--expect-failures`, which would otherwise drop the expectation, and each rejection is an arguments error in `verdict.json`. Building BG-3's `F` (`777ddf8d`) against `E`'s expected result is the recorded control: at `F` the gate reports 5988 named results against 5989, and `TurnpikeScopeTransfer.lean` has 7 `#print axioms` commands against 8, without `real_to_integer_surrogate`.

**Partial expected results.** The served logs were read through a tool that returns at most the last 5000 lines of a log. Where a module's reports precede that tail, the expected result records the reports it has and the module's `#print axioms` lines at the commit, with status `partial` or `none`, and the manifest lists the gap. Reproduction at the commit produces every report: the comparison then requires each recorded report to match, and one reproduced report for every `#print axioms` line of the module's source at that commit. A module recorded `absent` is not in the tree at that commit (a module the round adds in execution, at its `F` run), and reproduction confirms its absence. Of the 164 module records of the 96 runs' expected results, 84 are complete, 5 partial, 31 none and 44 absent.

**Lines are counted by splitting on newline characters.** The served texts end without a newline, so a 5000-line text has 4999 newline characters, which is what `wc -l` and the records' "last 4999 lines" count.

## What each entry states

**`claims`**: for every citing location, the claims that record makes about the cited run or log. Each claim is a verbatim fragment of the citing file, on a stated line, with one of three statuses: `retained` (the archived files it names carry it), `not retained` (no archived file carries it), `differs` (the archived files show something else, with a note). Tranche 1 annotates 752 claims at 172 citing locations: 686 retained, 66 not retained, none differing. The claims not retained are mostly job counts for runs whose job list was not saved, outputs of other jobs, statements a log tail cannot establish, and job identities the log bytes do not state. The annotations were made from the archived files alone and are a reading of those files, which a reviewer can repeat from the tree.

**`missing`**: the evidence items found absent: 39 job lists, which were served inline and not saved; the axiom reports of the 36 partial and none module records, with counts; and the run metadata of the BG-3 design run 38857340321.

**66 claims not retained and 76 gaps are different measurements**, and neither is a proof failure.

## The BG-3 exception

The four logs under `bg3/` are the only raw artifacts. BG-3's receipt and preregistration name each by its sha256 and assert positions in it ("the module's eight reports are at lines 4907–4916"). Such a claim is about one artifact and can only be re-checked against that artifact, never reproduced; so the artifact is kept byte for byte, and `check_retention.py` verifies each digest. Their substantive claims, the reports and their axioms and the gate's verdict, are recorded as expected results beside them (`bg3/results-*.json`), each with the manual recipe. `E`'s is also the expected result of entry `ci-38855576525`, which `reproduce.py` reproduces at `194eb3fd`. The two design-tree results hold at commits off `main` (`6c160ad2`, `e3ef9358`). Tranche 2 retains both, so that `check_objects.py --materialize` can write them into a clone's object store (see below). The exception is not widened: no other raw log is retained. Tranche 2 names the raw logs under its commits and withholds them; the only stored files with log names are the empty blob (0 bytes; named `r5.log`, `channel_check.replay.err`, `channel_check.run1.err` and `native-controls.selftest.final.err`) and `research/round7-channel/LOG.md`, a hand-written journal kept with R3's inclusion path.

## Tranche 2: retained off-main objects

`objects/` holds git objects that frozen records cite and `main` does not reach. It covers those most at risk: the
objects that no host ref held when the host's refs were listed on 2026-10-17, together with the R3 pair and BG-3's
off-`main` heads and blob. Objects that a host branch or pull ref still holds are left to later tranches.

| path | what | kind |
| --- | --- | --- |
| `objects/manifest.json` | every object: id, type, mechanism, stored form, size and sha256 of the stored file and of the content, its citations or the cited objects that need it, its parents and the parents it names without retaining them, and the blobs it withholds | `complete` |
| `objects/commit/<aa>/<id>`, `objects/blob/<aa>/<id>` | 137 cited commits as raw commit text, and 25 cited blobs as their raw bytes | `complete`: each file's content hashes to its id |
| `objects/loose/<aa>/<rest>` | every tree, and every dependency blob, as a git loose object (`zlib("<type> <size>\0" + content)`) | `complete`: likewise |
| `check_objects.py` | the checker of `objects/` (its rules are in its docstring) | `complete`, hash-pinned |

- **Counts.** 920 entries in all:
  - 165 cited objects;
  - 892 stored files: 162 raw (2.1 MB), 730 loose (7.9 MB), with 73.5 MB of content;
  - 28 withheld blobs: 22 raw logs, 3 small raw outputs and 3 build PDFs.
- **Mechanisms.** A commit is retained in one of four ways:
  - `raw:connected`: with every tree and blob `main` lacks, and every parent on `main` or retained (102 commits);
  - `raw:tree`: the same, but with a parent that is neither on `main` nor a retained connected commit (31): 9 name
    such a parent without retaining it, and the parent of each of the other 22 is a retained `raw:tree` commit;
  - `raw:partial-tree`: every tree is retained, and the raw logs, raw outputs or PDFs under it are named by id (2);
  - `inclusion-proof`: the commit, its root tree, the trees on each cited path and what lies under it, the raw logs
    there named by id (2, the R3 pair; `e7d380fc` withholds 4).
- **Withheld.** Raw logs and transcripts are not committed (§A.42 item 1). By the owner's decision of 2026-10-17,
  neither are captured `.out` and `.err` output nor the small raw outputs written beside the logs (three integer
  lists under `1f19a347`). Empty files are the exception: the empty blob, retained wherever it occurs, carries
  three `.err` names and one `.log` name. The three PDFs, under act 45's head `ad64b603`, are build outputs whose bytes no record
  freezes. Each withheld blob keeps its id, size and paths in the manifest, its mechanism states why it is withheld,
  and the check (O9) confirms that a retained tree of a commit listing it names it at exactly those paths, each
  of a file type its mechanism covers (`.log`, `.out` or `.err`; `.txt`; `.pdf`). A file type does not authorize
  withholding: `check_objects.py` holds the approved withheld entries (`APPROVED_WITHHELD`: id, mechanism and exact
  paths), the manifest's withheld set must equal it, and no withheld blob is empty. No retained object records a blob's
  size; the sizes were read from the recovery copies when the archive was built.
- **Cited blobs are plain files.** Committing them makes those blob ids reachable from `main`, so a frozen control
  that reads them with `git cat-file` works in any clone.
- **Recorded mappings.**
  - `id_discrepancies` maps four cited ids that name no object to the run heads the provenance errata (PE-1 to PE-4)
    record, and the check confirms each mapping against `../provenance-errata/errata.json`.
  - `missing` lists the six cited ids that the host refuses and that no preserved copy holds, with their citing
    lines.
- **TRB-1's reference head** `7de2d549` (preregistration `:110`, `:207`) was held only in a local clone. It is
  retained here as a `raw:tree` commit whose parent `6027be54` is named.

**Not adopted as code.** The retained objects are evidence of what off-`main` heads contained:
- nothing under `objects/` is a path that a build, the release gate or CI picks up;
- the checker hashes and parses the objects but never executes them;
- running a retained tree, after `--materialize`, is reproduction of a historical claim at that commit, with
  `main`'s checkout as the verifier, as `reproduce.py` does for commits on `main`;
- retention changes no verdict and no claim's status, and no retained object is a `check-run` attestation.

**Identities and secrets.**
- Every stored object was scanned with the secret patterns of `check_retention.py`'s R5 plus four more token shapes.
- The scan exempts three things:
  - commit identity lines and `Co-Authored-By:` trailers whose address digest is listed, provided the address is
    already in `main`'s history (the check verifies this);
  - commit signature blocks;
  - addresses in reserved example domains.
- Nothing was redacted, because a redacted copy would not keep its id.

**Excerpts.** None of the 194 bridge-log excerpts of R1's drafting branches is stored, named by a stored tree, or
reachable from `HEAD`. The manifest lists the sha256 digests of their ids, never the ids themselves.

## Tranche 3: cited runs that no receipt attests

Frozen records also cite CI runs that no receipt or certificate attests: push runs that certified a base, pull-request runs at a candidate merge, and the runs whose output a precondition table quotes. Tranche 3 retains them in the tranche-1 form, an expected result with a recipe, earliest log expiry first.

**The cited set.** At `main` `b96662e6` the tracked text outside this archive cites 487 runs. The count takes every 11-digit run id and 12-digit job id on a line that says run, job or `actions/` (the audit's rule R), the same id shapes on other lines when they name a run of this repository, and the inner runs of the corpus's one cited range (act 40's `preregistration.md:744`); a job id counts for its run. The set equals the 487 runs of the inventory accepted on 2026-10-17. Tranche 1 holds 99 of them: the 96 `ci-` entries and BG-3's three further runs. That leaves 388. This tranche retains the 22 whose 90-day expiry falls on 2026-12-17 or 2026-12-18. The manifest's `tranche3.remaining` lists the other 366 with their creation dates and expiries (2026-12-19 to 2027-01-14), in order of creation. No cited run's log had expired when this tranche was cut. The expiry is creation plus 90 days, GitHub's default for a public repository; the repository's own setting could not be read.

| path | what | kind |
| --- | --- | --- |
| `runs/<run>/run.json` | the run's identity and outcome, selected fields of the runs API's answer | `derived`; `source_sha256` is the answer's digest |
| `runs/<run>/jobs.json` | every job, with its attempt, conclusion and steps, from the jobs API's answer | `derived`, likewise |
| `runs/<run>/expected.json` | for the 15 runs whose citing claims rest on what a job printed, that output, extracted by `job_outputs.py` from the served job log: the commit it holds at, the recipe that regenerates it, and the served text's line counts and digest | `derived` from the served log, whose digest is `source_sha256` |
| `job_outputs.py`, `build_tranche3.py` | the extractor, reproduction tool and comparator for these outputs, and the script that cut the tranche | `complete`, hash-pinned |

**Two outputs are retained.**
- **The control-plane base check** (8 runs). These are its PASS, SKIP and FAIL lines, its header and its summary, such as `OK (mode B, 16 row(s), no failure)`. The header's REF is masked and kept beside the output as provenance. A push run's REF is its head. A pull-request run's REF is GitHub's synthetic merge, a commit not reachable from `main`. The expected result therefore records the merge's base and head, as the run's checkout reported them ("HEAD is now at 28ed5c98 Merge c6d94dda… into d08b932d…"). A reproduction rebuilds the merge from those two commits, both on `main`, under a new id.
- **The guard,** `edge_rigidity_probe.py` in the probes job (7 runs). For each check it records the status, the tag and the sha256 of the message, with the counts and the verdict, and quotes in full only the lines a claim rests on (`R7-OGS … PASS (ARCHIVED; …)`).

The other 7 runs are cited for their identity, outcome and jobs alone, which `run.json` and `jobs.json` carry.

**What the served logs were.** They were read on 2026-10-17 through the session's job-log tool, which returns at most the last 5000 lines of a log, or fewer when asked. The seven probes logs were served whole (2181 to 2369 lines). Of the eight base-check logs, two were served whole, and six as their last 80 to 160 lines, which hold the base check's output and, for a pull-request run, the checkout's merge line. Each output records `original_lines`, `served_lines` and the served text's sha256. That digest identifies the text the result was read from. It is provenance of the extraction, not a copy of GitHub's log archive, and no served text is retained (§A.42 item 1).

**Claims.** Tranche 3 annotates 94 claims at 46 citing locations: 83 retained and 11 not retained. Ten of the 11 are statements that `_SI2_LEGACY_RE` finds no assignment statement in the guard file, which is a reading of the file's text and not an output of the run; it is reproducible from the tree at that commit. The eleventh is SI-3's "local run at `L`", which was not a CI run. One count needed reading: SI-3's "92 tags" is the guard's 92 checks, R1 to R9 and 83 `R7-*` tags. Acts 21 to 25 count `R7-*` tags alone.

**Reproduction.** `job_outputs.py reproduce --run <run> --work <dir>` runs each recorded command at its commit from a full-history clone. The guard needs numpy and scipy, as the probes job installs them. It compares every line, check, digest, summary, verdict and quoted line, and the exit code, but not timestamps, durations, REF's id or the order of the guard's checks. It fails closed and writes `verdict.json` on every exit. All 15 outputs were reproduced this way in a local clone before commit; that is evidence for the preparer, not an attestation. The `reproduce evidence` workflow runs `reproduce.py`, which handles bridge results only; it does not yet run these.

**Not adopted as attestations.** None of these runs is a `check-run` attestation, and retention changes no verdict or claim.

## Checking

From the repository root:

```
python3 -I verification/audits/evidence-retention/check_retention.py
python3 -I verification/audits/evidence-retention/check_retention.py --self-test
python3 -I verification/audits/evidence-retention/check_retention.py --later-provenance
python3 -I verification/audits/evidence-retention/check_retention.py --module-sets
python3 -I verification/audits/evidence-retention/check_retention.py --gate
python3 -I verification/audits/evidence-retention/compare_result.py --self-test
python3 -I verification/audits/evidence-retention/reproduce.py --run <run_id> --work <dir>   # needs elan and history
python3 -I verification/audits/evidence-retention/check_objects.py                 # tree mode, no git
python3 -I verification/audits/evidence-retention/check_objects.py --reconstitute  # history mode
python3 -I verification/audits/evidence-retention/check_objects.py --self-test
python3 -I verification/audits/evidence-retention/check_objects.py --materialize   # adds the objects to the clone's object store; no refs
python3 -I verification/audits/evidence-retention/job_outputs.py --self-test
python3 -I verification/audits/evidence-retention/job_outputs.py reproduce --run <run_id> --work <dir>   # tranche 3; needs history, numpy and scipy
```

`check_retention.py` leaves the files under `objects/` to `check_objects.py`, whose manifest it pins, and `--gate`
also runs `check_objects.py --reconstitute` and `--self-test`, and `job_outputs.py --self-test`.

The check uses the tree alone: no git history, network or third-party package. Its rules (R1–R9 and R12, in its docstring) verify:
- every archived file's size and sha256, and the digest match of each `complete-as-cited` file;
- that each citing file has its recorded blob id, the cited line still holds its tokens, and each claim's text stands verbatim where it says;
- that every expected result is well formed and names its commit, job and recipe, with module statuses consistent with their reports;
- the absence of secret patterns, IP addresses and e-mail addresses in every file here;
- that no unlisted file sits in the archive;
- the manifest's form, and that each entry's files agree with each other and with the gap list, a CI entry's expected result being a bridge result;
- coverage, recomputed from the tree: every receipt under `verification/receipts/`, and every certificate attestation that cites runs, is covered by this tranche or named in the manifest's `coverage.later`; each of their check-run attestations and cited runs has an entry that matches it.
- for tranche 3 (R12): that each `run-` entry's files agree: the run, its head commit and attempt, its jobs, each output's job, commit, recipe, source and expectation, and its expiry, creation plus 90 days. It also checks that no retained or remaining run is attested or already retained by tranche 1, that `tranche3.remaining` lists each run once in order of creation, that no retained run expires after a remaining one, and that the counts agree.

At `fc5abade` every receipt is covered and `coverage.later` is empty. A receipt that lands after this tranche keeps its own evidence in its record directory (§A.42), and the plain check fails on it until `coverage.later` names it with that directory; a path named there may be neither covered nor cited by this tranche. The tree cannot order commits, so `--later-provenance` (R10) checks against git history that the tranche base is an ancestor of HEAD and that no path named as later existed at the base.

`--module-sets` (R11) re-derives each expected result's module table from git history rather than from the archive. The receipts and certificate attestations at `fc5abade`, read from git and not from the manifest, fix the runs to check, the rounds that attest each run, and the commit each attests, which must be the expected result's. The runs with a checked bridge result must be exactly the runs they attest, whatever the archive classifies its results as; a run with several bridge results has each checked and counts once, and a CI entry's expected result must be a bridge result. At that commit, each round's control-plane files must have the blobs its receipt pins, their `v3-governed-paths` block, its opener and closer recognized as `G10` states and its entries hashed as `S7` states, must hash to the receipt's `governed_paths_digest`, and its `.lean` paths under `verification/lean-mathlib/` are the governed modules. `S7`'s validity rules are not applied here: the digest ties the entries to the receipt, whose block the V3 verifier validated. CV-1's three runs have no `v3-governed-paths` block: for them the certificate, `verification/certificates/CV1.json`, is read at the run's commit at the blob its attestation pins, and its contributions name no Lean module. The table must equal the union over the run's rounds. It checks 97 expected results, the 96 runs' own and BG-3's `E` tail, a second result of one of those runs, with 165 module records. Three results, all of runs no attestation names, are listed as outside its scope, each with its reason: BG-3's design diagnostic, which records no module table, and its two design-tree results, at commits off `main`. A result of another kind whose run an attestation names fails the check, and so does a bridge result of an unattested run at a commit on `main`. **It is a consistency check, not an independent derivation.** `build_archive.py` took the module sets from the same governed-paths blocks, read at the tranche base with its own parser, so R11 shows that the archive applied those blocks faithfully, as they stand at each run's commit and as the receipts' digests commit to them. It cannot show that the governed paths name the right modules.

`--gate` is the release gate's `evidence-retention` step. It runs the check in history mode, where R9's scope is read from git rather than from the tree: every receipt, and every certificate attestation citing runs, that existed at `fc5abade` must be covered, nothing else may be, and a receipt landed later needs no declaration. It runs R10 and R11, printing the results outside R11's scope, then the self-test, whose R10 and R11 cases need that history and fail without it. The Mathlib bridge job, which runs the gate, checks out the full history. The gate does not rebuild anything; reproduction is the separate workflow above.

It prints the gaps and every claim not retained. The self-test mutates a copy once for each of the checker's failure messages, and requires that message.

**`build_archive.py` documents how the tranche was cut.** It cannot be re-run from the tree, because its inputs (the saved API responses and served logs) are not retained; their digests are. The checker and the reproduction tool are the reproducible parts.

## Secrets and operational data

Every file here was scanned before commit for token and key patterns, key-file headers, signed-URL parameters, IP addresses and e-mail addresses. There were no matches. The design log shows GitHub's own masked values (`token: ***`, `AUTHORIZATION: basic ***`) and runner metadata that GitHub publishes for public runs: worker id, region, and the repository's branch list. The only URLs are public ones, including the public Mathlib cache. Nothing was redacted.

## Not yet retained

Recorded here so the gap is visible, not resolved. Counts are from `audit/offmain_audit-output.txt`:
- **Commits not reachable from `main`:** 107, cited at 236 locations in native-round records and one in a mutable script. Host refs held all 107 when they were listed on 2026-10-17. Tranche 2 retains 6 of them: the R3 pair, BG-3's three heads, and `19985424`, the parent of a retained connected commit. The other 101 are not retained yet.
- **Blobs and trees not reachable from `main`:** 75, all held by host refs when listed. Tranche 2 retains 14 of them. Of the other 61, four are CONSC-2's build PDFs (its preregistration `:516`–`:517`), which as build outputs are to be named, not retained.
- **Other CI evidence:** 842 citations of 438 run ids and 173 job ids by the audit's rule R. The full cited set is 487 runs (tranche 3 above). Tranche 1 covers 96 runs and BG-3's four logs, whose entries name three more runs. Tranche 3 covers 22. The other 366 are listed with their expiries in `tranche3.remaining`, the earliest on 2026-12-19.
- **Act-26's scratchpad computation** (`result.md:931`), which the audit found saved nowhere.

Each needs a documented resolution in a later tranche: an expected result with a recipe, or a recorded gap.
