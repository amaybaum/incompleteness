#!/usr/bin/env python3
"""Controls for the batch extractor: an end-to-end pass, and code mutations each self-test must catch.

  python3 -I controls.py --extractor PATH [--work DIR]

1. End to end. assemble.py's own fixture shard is assembled with the given extractor, its output is timestamped and
   wrapped as the job-log tool serves a log, and collect.py's reader must accept it whole: every run usable, each
   collected block byte-identical to the block assemble.py printed. Served as a tail, it must be refused. This ties
   the collector to the assembler's real output rather than to the collector's own synthetic writer.
2. Mutations. Each entry changes one decisive line (or a few) of assemble.py, host.py or collect.py in a copy of
   batchx/; the copy's self-test must then fail (the mutant is killed). A mutant runs only the suites that can read
   its file (SUITES): collect.py's suite for a collect.py mutant, assemble.py's for an assemble.py mutant, and both
   for a host.py mutant. The unmutated copy's self-tests must pass
   first, so a kill is not an artefact of the copy. Two mutants run at a time, each in its own copy, and their results
   are printed in MUTANTS order. The free space under --work is read before and after each mutant: a reading under
   DISK_FLOOR makes that mutant an INFRASTRUCTURE failure of the run, never a kill or a survival; an exception in a
   worker fails the run. A self-check shows both on simulated readings and workers, and another drives main's own tally
   with a simulated INFRASTRUCTURE result. A mutation whose text is not
   found exactly once is itself a failure. An entry that names expected tests is killed only when every one of them fails by name and no suite
   stopped with a traceback, so the catch is shown to be that regression test's, not only an unrelated one's; the
   table printed at the end lists, for each such mutant, every test it fails.
3. Plan and pins (with --plan WORKFLOW). runs.json is the 223 runs, each once, in expiry order, in contiguous
   shards of at most shard_size; the three scripts pin its sha256 and assemble.py pins crosscheck.json's; the pins
   are cross-validated: collect.py's ASSEMBLER_BLOB and HOST_BLOB are the files' blobs, its EXTRACT_RESULT_BLOB and
   MAIN_COMMIT are assemble.py's, and the workflow's extract_result.py checkouts are at that MAIN_COMMIT; the
   workflow's matrix lists exactly shards 1..N; it triggers only on a push to its own branch; its permissions are
   actions: read and contents: read and nothing else; every `uses:` is pinned by a full SHA and is actions/checkout;
   every checkout sets persist-credentials: false; GH_TOKEN is set once, on the host step, from github.token, and
   no other secret, artifact, cache or summary is named; every job and every step has timeout-minutes. Each rule has
   a negative control that edits the workflow text and must be caught.
Exit 0 when every part holds and every mutant is killed, 1 otherwise. Local and CI; no network.
"""
import argparse
import concurrent.futures
import hashlib
import io
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import types

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
FILES = ("assemble.py", "host.py", "collect.py", "runs.json", "crosscheck.json")

MUTANTS = [
    ("assemble.py", 'logged == head, logged[:12])', 'True, logged[:12])', "the head check is skipped"),
    ("assemble.py", 'm.group(2) == head\n                  and', 'True\n                  and',
     "a pull-request merge of any head is accepted"),
    ("assemble.py", 'and any(l == "Cleaning up orphan processes" for l in lg.s[-12:]),', 'and True,',
     "a log cut before its cleanup is accepted"),
    ("assemble.py", 'if run_set_problem(verdicts, runs, expected_ids) is not None:\n        return "UNVERIFIED"',
     'if False:\n        return "UNVERIFIED"', "the run-set rule is skipped"),
    ("assemble.py", "if fixed + used + n + 1 > budget:", "if False:", "the line budget is ignored"),
    ("assemble.py", 'C("gate: a PASS verdict under a successful Release gate step", gv and gv["pass"],',
     'C("gate: a PASS verdict under a successful Release gate step", True,', "a red verdict under a green step passes"),
    ("assemble.py", "    if unparsed:\n        gaps.append(", "    if False:\n        gaps.append(",
     "an unparsed report line is dropped silently"),
    ("assemble.py", "hits = scan(text)", "hits = []", "the credential scan is skipped"),
    ("assemble.py", 'C("build: no \'Build completed successfully\' line under a failed Build step", not built)',
     'C("build: no \'Build completed successfully\' line under a failed Build step", True)',
     "a build line under a failed step passes"),
    ("assemble.py", "if pinned and git_blob_id(data) != EXTRACT_RESULT_BLOB:", "if False:",
     "the extractor's blob is not checked"),
    ("assemble.py", 'C.need("format: one %s section for a step that ran" % nm,',
     'C("format: one %s section for a step that ran" % nm,', "an unknown format reads as FAILS (review note N3)"),
    ("assemble.py", 'return RUNNER_PATH.sub("", text).rstrip()', "return text.rstrip()",
     "runner paths stay in the error lines"),
    ("assemble.py", 'if bconc == "cancelled" and not gv:\n        outcome = "cancelled"',
     'if bconc == "cancelled" and not gv:\n        outcome = "gate-verdict"', "a cancelled run is labelled as reaching a verdict"),
    ("host.py", 'if kind == "log" and not u.query and u.path in t.log_paths:', 'if kind == "log":',
     "the log allow-list admits any job"),
    ("host.py", 'req2 = urllib.request.Request(loc, method="GET", headers={"User-Agent": UA})',
     'req2 = urllib.request.Request(loc, method="GET", headers={"User-Agent": UA, "Authorization": "Bearer " + token})',
     "the token is sent to the storage host"),
    ("host.py", 'if kind != "rate" and t.remaining is not None and t.remaining < t.reserve:', "if False:",
     "the rate-limit reserve is ignored for JSON reads"),
    ("host.py", "            if len(jobs) != total:", "            if False:", "a short jobs list is accepted"),
    ("collect.py", "    if len(raw) != orig:", "    if False:", "a served tail is accepted"),
    ("collect.py", 'sm.group(2) != hashlib.sha256(body.encode("utf-8")).hexdigest()', "False",
     "a block's digest is not checked"),
    # Each entry from here: (file, edits, None, what, expected tests). edits is (old, new) pairs; the mutant must fail
    # every expected test, matched by its exact name, so the catch is shown to be that regression test's.
    ('collect.py', (('        elif len({identity(a[1]) for a in ans}) > 1:\n', '        elif False:\n'), ), None,
     "N2: a job's copies that differ are not detected",
     ['[R2d] a clean shard 1, then a conflicting copy of the same job arriving after it: shard 1 UNVERIFIED', 'a shard collected twice with contradicting content: UNVERIFIED, none taken (good copy first)', 'copies differing only in a tampered block are UNVERIFIED, whichever comes first']),
    ('collect.py', (('enumerate(L)) if m]\n    want', 'enumerate(L) if i >= len(L) - 30) if m]\n    want'), ), None,
     'N1: the verdict line is looked for only in the last 30 lines',
     ['a verdict line followed by 40 runner lines is found']),
    ('collect.py', (('    if len(vs) != 1:\n', '    if not vs:\n'), ), None,
     'N1/R3: a second verdict line is allowed',
     ['two verdict lines', '[R3f] two verdict lines inside the output is refused', '[R3g] a verdict-like line before the start, with a real verdict inside is refused', '[R3i] a verdict-like line after the end, with a real verdict inside is refused']),
    ('collect.py', (('    elif span is not None and vs[0][0] != span[1] - 1:\n', '    elif False:\n'), ), None,
     "N1/R3: a verdict line other than the assembler's last line before its end marker is allowed",
     ['[R3h] a verdict-like line before the start, with no verdict inside is refused', '[R3j] a verdict-like line after the end, with no verdict inside is refused', 'a verdict line before the last block']),
    ('collect.py', (('            bad = True  # an answer of a job outside the run\n', ''), ('                voided.setdefault(s_, set()).add("an answer of job %s, which is no job of the run, names it" % job)\n', '                pass\n'), ), None,
     'N3: an answer of a job outside the run is not refused',
     ['a log from another job (another push of this branch) is refused and voids the shard it names']),
    ('collect.py', (('        elif not pins:\n', '        elif False:\n'), ), None,
     'N3: the blobs a result names are not checked',
     ['a block naming another assembler_blob is refused', 'a block naming another host_reader_blob is refused', 'a block naming another extractor_blob is refused', 'a block naming another extractor_commit is refused', 'a block naming another runs_sha256 is refused']),
    ('collect.py', (('    if not ab or any(m.groups() != (', '    if not ab or False and any(m.groups() != ('), ), None,
     "N3: the banner's blobs are not checked",
     ['a banner naming another host-reader blob is refused']),
    ('collect.py', (('    if orig >= MAX_LINES:\n', '    if False:\n'), ), None,
     'N9: a log of 5,000 lines or more is accepted',
     ['a whole answer of 5,000 lines is refused: not under 5,000']),
    ('assemble.py', (('    if nblocks > 1:\n', '    if False:\n'), ), None,
     'N5: of two gate blocks the last is taken',
     ['two gate blocks in one gate section (FAILED, then PASS) are UNVERIFIED; the last is not taken']),
    ('assemble.py', (('run["conclusion"] == cfg.get("run_conclusion"), str(run["conclusion"]))', 'True, str(run["conclusion"]))'), ), None,
     'N6: the pinned run conclusion is not compared',
     ["a run's attempt-1 conclusion other than the pinned one FAILS", 'a pinned conclusion of another value FAILS']),
    ('host.py', (('        write_record(rec_path, record)  # every read is on disk as soon as it is done\n', '        pass\n'), ), None,
     'N8: the fetch record is not written after each read',
     ["a step stopped during run 9002's log keeps run 9001's reads and run 9002's run and jobs reads on disk"]),
    ('collect.py', (('            for s_ in sorted(involved):  # every shard involved\n', '            for s_ in sorted(involved)[-1:]:  # every shard involved\n'), ), None,
     'R1: a job under two shards voids only the highest-numbered one',
     ["[R1a] shard 3's job serving shard 1's content, beside genuine shards 1 and 3, voids both", "[R1b] the mirror, shard 1's job serving shard 3's content, voids the same two shards"]),
    ('collect.py', (('            for s_ in sorted(involved):  # every shard involved\n', '            for s_ in sorted(involved - {inv[job]}):  # every shard involved\n'), ), None,
     "R1 (reviewer M1): only the shards the foreign content names are voided, never the job's own",
     ["[R1a] shard 3's job serving shard 1's content, beside genuine shards 1 and 3, voids both", "[R1b] the mirror, shard 1's job serving shard 3's content, voids the same two shards"]),
    ('collect.py', (('            for s_ in sorted(involved):  # every shard involved\n', '            for s_ in sorted(involved)[:1]:  # every shard involved\n'), ), None,
     'R1 (reviewer M1b): only the lowest-numbered shard involved is voided',
     ["[R1a] shard 3's job serving shard 1's content, beside genuine shards 1 and 3, voids both", "[R1b] the mirror, shard 1's job serving shard 3's content, voids the same two shards"]),
    ('collect.py', (('        ans = by_job[job]\n', '        ans = [a for a in by_job[job] if a[3] is not None]\n'), ), None,
     "R2: a bannerless or malformed-banner duplicate is left out of its job's copies",
     ['[R2a] a whole shard 1, then a bannerless duplicate of the same job: shard 1 UNVERIFIED, none of its runs usable', '[R2a] a bannerless duplicate, then the whole shard 1: the same', '[R2b] a whole shard 1, then a contradicting bannerless duplicate of the same job: shard 1 UNVERIFIED, none of its runs usable', '[R2b] a contradicting bannerless duplicate, then the whole shard 1: the same', '[R2c] a whole shard 1, then a malformed-banner duplicate of the same job: shard 1 UNVERIFIED, none of its runs usable', '[R2c] a malformed-banner duplicate, then the whole shard 1: the same', '[R2e] a lone bannerless answer of an indexed job leaves its shard void, never usable']),
    ('collect.py', (('    for a in answers:\n        by_job.setdefault(', "    for a in answers:\n        if a[3] is None:\n            P('COLLECT FAIL %s: names no shard' % a[0])\n            bad = True\n            continue\n        by_job.setdefault("), ), None,
     'R2 (reviewer M2): a bannerless answer is refused but never grouped with its job',
     ['[R2a] a whole shard 1, then a bannerless duplicate of the same job: shard 1 UNVERIFIED, none of its runs usable', '[R2a] a bannerless duplicate, then the whole shard 1: the same', '[R2b] a whole shard 1, then a contradicting bannerless duplicate of the same job: shard 1 UNVERIFIED, none of its runs usable', '[R2b] a contradicting bannerless duplicate, then the whole shard 1: the same', '[R2c] a whole shard 1, then a malformed-banner duplicate of the same job: shard 1 UNVERIFIED, none of its runs usable', '[R2c] a malformed-banner duplicate, then the whole shard 1: the same', '[R2e] a lone bannerless answer of an indexed job leaves its shard void, never usable']),
    ('collect.py', (('        involved = named | {inv[job]}\n', '        involved = {inv[job]}\n'), ('        elif len({identity(a[1]) for a in ans}) > 1:\n', '        elif False:\n'), ), None,
     'R1/R2 (reviewer M6): the first answer per job decides, no identity comparison, the log names nothing',
     ["[R1a] shard 3's job serving shard 1's content, beside genuine shards 1 and 3, voids both", "[R1b] the mirror, shard 1's job serving shard 3's content, voids the same two shards", '[R2d] a clean shard 1, then a conflicting copy of the same job arriving after it: shard 1 UNVERIFIED']),
    ('collect.py', (('    return named  # every shard the log names\n', '    return {int(m.group(1)) for m in [next((BANNER.match(l) for l in L if BANNER.match(l)), None)] if m}\n'), ('        named |= set().union(*(a[5] for a in ans))  # the raw scan of every answer\n', ''), ), None,
     'F1: only the first readable RUNSET line names a shard (the 56913c6e reading)',
     ["[F1b] shard 3's job serving shard 1's log with its RUNSET line malformed voids shards 1 and 3, only shard 2's runs eligible, none usable", "[F1c] shard 3's job serving shard 1's log with its RUNSET line deleted voids shards 1 and 3, only shard 2's runs eligible, none usable", "[F1d] shard 3's job serving shard 1's log as shard 3's log followed by shard 1's in one answer voids shards 1 and 3, only shard 2's runs eligible, none usable"]),
    ('collect.py', (('    if span is not None and any(L[i].startswith("CHECK all ") for i in range(span[0], span[1])):\n', '    if False:\n'), ), None,
     "F2: a CHECK all line inside the assembler's output is ignored",
     ["[F2] a 'CHECK all UNVERIFIED stopped' line inside the assembler's output voids the shard"]),
    ('collect.py', (('    if len(ends) != 1:\n', '    if False:\n'), ), None,
     'R3: no single end-of-output marker is required (the pre-fix acceptance)',
     ['[R3a] the assembler died before its verdict; a verdict-shaped line appears later in the trailer is refused', '[R3b] a missing end-of-output marker (truncated output) is refused', '[R3d] two end-of-output markers is refused']),
    ('collect.py', (('    if len(starts) != 1:\n', '    if False:\n'), ), None,
     'R3: two start markers are allowed',
     ['[R3c] two start markers is refused']),
    ('collect.py', (('        if span[1] < span[0]:\n', '        if False:\n'), ), None,
     'R3: an end marker before the start marker is allowed',
     ['[R3e] the end-of-output marker before the start marker is refused']),
    ('collect.py', (('        elif AEND.match(L[span[1]]).groups() != (str(k), str(nsh), ASSEMBLER_BLOB[:12]):\n', '        elif False:\n'), ), None,
     "R3: the end marker's assembler is not checked",
     ['[R3k] an end-of-output marker naming another assembler blob is refused']),
    ('collect.py', (('    elif span is not None and vs[0][0] != span[1] - 1:\n', '    elif span is not None and vs[0][0] < span[0]:\n'), ), None,
     'R3 (reviewer M3): a verdict anywhere after the start marker is accepted',
     ['[R3j] a verdict-like line after the end, with no verdict inside is refused', 'a verdict line before the last block']),
    ('collect.py', (('    if len(vs) != 1:\n', '    vs = [x for x in vs if span is None or span[0] < x[0] < span[1]]\n    if len(vs) != 1:\n'), ), None,
     'R3 (reviewer M3b): only verdict lines inside the span are counted',
     ['two verdict lines', '[R3g] a verdict-like line before the start, with a real verdict inside is refused', '[R3h] a verdict-like line before the start, with no verdict inside is refused', '[R3i] a verdict-like line after the end, with a real verdict inside is refused', '[R3j] a verdict-like line after the end, with no verdict inside is refused']),
    ('collect.py', (('              "launched_commit": head,\n', ''), ), None,
     'R4: collected.json does not record the launched commit',
     ['[R4a] collected.json records the full 40-hex launched commit, the --head value the job index required']),
    ('collect.py', (('              "launched_commit": head,\n', '              "launched_commit": head and head[:12],\n'), ), None,
     'R4 (reviewer M4): only a 12-hex prefix of the launched commit is recorded',
     ['[R4a] collected.json records the full 40-hex launched commit, the --head value the job index required']),
    ('collect.py', (('    return {"path": rel, "commit": commit,', '    return {"path": rel, "commit": None,'), ), None,
     "R4: the collector's commit is not recorded",
     ["[R4c] the collector's commit and committed blob come from git, and local uncommitted changes are recorded by the executed bytes' sha256 and a false match flag"]),
    ('collect.py', (('            "executed_matches_committed_blob": committed is not None and committed == executed}', '            "executed_matches_committed_blob": True}'), ), None,
     'R4: uncommitted collector changes are not marked',
     ["[R4c] the collector's commit and committed blob come from git, and local uncommitted changes are recorded by the executed bytes' sha256 and a false match flag"]),
    ('collect.py', (('    if not re.fullmatch(r"[0-9a-f]{40}", str(head)):\n', '    if False:\n'), ), None,
     'R4: a launched commit that is not a full sha is accepted',
     ['[R4d] a launched commit that is not a full 40-hex sha is refused']),
    ('collect.py', (('            quarantine.append({"kind": "missing", "shard": k, "job_id": job_index.get(k),\n', '            ({"kind": "missing", "shard": k, "job_id": job_index.get(k),\n'), ), None,
     'I/completeness: a shard whose expected answer was not served is ignored',
     ["[I5] one shard's answer missing quarantines the whole collection, recorded by its expected name: zero runs eligible or usable, read back from disk", 'a shard missing quarantines the whole collection']),
    ('collect.py', (('            failed.append({"file": name, "sha256": dig, "sha256s": digests, "shard": k, "problems": probs})  # traceability\n', ''), ), None,
     'I/traceability: a file that fails validation is not recorded',
     ['[I6] a file that fails validation is recorded by name and digest, read back from disk']),
    ('collect.py', (('            quarantine.append({"kind": "unattributable", "file": e["name"], "sha256": e["sha256"], "size": e["size"],\n', '            ({"kind": "unattributable", "file": e["name"], "sha256": e["sha256"], "size": e["size"],\n'), ), None,
     'I: an unattributable file is dropped silently (no quarantine)',
     ['[I1] an unreadable (compressed) served file with no recoverable shard identifier quarantines the whole collection: no run eligible or usable', '[I1] the quarantined file is recorded by name and digest', "[G1a] shard 3's job saving shard 1's log cut off halfway (not JSON) quarantines the whole collection: no run eligible or usable", "[G1b] shard 3's job saving shard 1's log with its job_id written as a string quarantines the whole collection: no run eligible or usable", "[G1c] shard 3's job saving shard 1's log wrapped in a tool envelope quarantines the whole collection: no run eligible or usable", "[G1d] shard 3's job saving shard 1's log with a byte that is not UTF-8 quarantines the whole collection: no run eligible or usable"]),
    ('collect.py', (('            quarantine.append({"kind": "unattributable", "file": e["name"], "sha256": e["sha256"], "size": e["size"],\n', '            [voided.setdefault(s_, set()).add("named by an unparseable file") for s_ in (e["names_shards"] or [])]\n            bad = True\n            ({"kind": "unattributable", "file": e["name"], "sha256": e["sha256"], "size": e["size"],\n'), ), None,
     'I/G1: an unattributable file voids only the shards it names (the previous design), no quarantine',
     ['[I1] an unreadable (compressed) served file with no recoverable shard identifier quarantines the whole collection: no run eligible or usable', "[G1a] shard 3's job saving shard 1's log cut off halfway (not JSON) quarantines the whole collection: no run eligible or usable", "[G1b] shard 3's job saving shard 1's log with its job_id written as a string quarantines the whole collection: no run eligible or usable", "[G1c] shard 3's job saving shard 1's log wrapped in a tool envelope quarantines the whole collection: no run eligible or usable", "[G1d] shard 3's job saving shard 1's log with a byte that is not UTF-8 quarantines the whole collection: no run eligible or usable"]),
    ('collect.py', (('        if job not in inv and not named:\n', '        if False:\n'), ), None,
     'I: an answer of a job outside the run that names no shard is not quarantined',
     ['[I4] an answer of a job outside the run that names no shard quarantines the whole collection']),
    ('collect.py', (('        e["usable"] = bool(e["eligible"] and verdict == "HOLDS")\n', '        e["usable"] = bool(e["eligible"])\n'), ), None,
     "I: a run is usable on its own result, whatever the collection's verdict (the withdrawn DESIGN rule)",
     ['[I2] a COLLECT FAILS outcome marks zero runs usable and writes no result file, read back from disk: a truncated mislabelled copy (quarantined) and a reformatted one (two runs still eligible)', '[I2b] an UNVERIFIED outcome (one run UNVERIFIED) marks zero runs usable and writes no result file, though five runs are eligible']),
    ('collect.py', (('        e["usable"] = bool(e["eligible"] and verdict == "HOLDS")\n', '        e["usable"] = bool(e["eligible"] and False)\n'), ), None,
     'I: no run is ever usable (the invariant met vacuously)',
     ['[I3] positive control: a clean collection marks all six runs usable and writes all six result files']),
    ('collect.py', (('    return named  # the raw scan\n', '    return set()  # the raw scan\n'), ), None,
     'G2: no raw scan (only the parsed, line-anchored reading)',
     ["[G2a] shard 3's job saving shard 1's log with timestamps without fractional seconds voids shards 1 and 3, only shard 2's runs eligible, none usable", "[G2b] shard 3's job saving shard 1's log with an ANSI code after each timestamp voids shards 1 and 3, only shard 2's runs eligible, none usable", "[G2c] shard 3's job saving shard 1's log with each line indented by one space voids shards 1 and 3, only shard 2's runs eligible, none usable", "[G2d] shard 3's job saving shard 1's log reduced to its block bodies, END and SHA256 lines voids shards 1 and 3, only shard 2's runs eligible, none usable", "[G2e] shard 3's job saving shard 1's log reduced to one RUNSET line with an ANSI code inside the name voids shards 1 and 3, only shard 2's runs eligible, none usable", "[G2f] shard 3's job saving shard 1's log reduced to one RUNSET line with a tab and doubled spaces voids shards 1 and 3, only shard 2's runs eligible, none usable", "[G2g] shard 3's job saving shard 1's log reduced to one RUNSET line in lower case voids shards 1 and 3, only shard 2's runs eligible, none usable", '[G2h] a bare 11-digit run id or 12-digit bridge job id anywhere names its shard', "[G2i] a job_id of another shard's job written inside an answer's log voids both shards"]),
    ('collect.py', (('        named |= set().union(*(a[5] for a in ans))  # the raw scan of every answer\n', ''), ), None,
     "G2: a parseable answer's raw names are not added",
     ["[G2a] shard 3's job saving shard 1's log with timestamps without fractional seconds voids shards 1 and 3, only shard 2's runs eligible, none usable", "[G2b] shard 3's job saving shard 1's log with an ANSI code after each timestamp voids shards 1 and 3, only shard 2's runs eligible, none usable", "[G2c] shard 3's job saving shard 1's log with each line indented by one space voids shards 1 and 3, only shard 2's runs eligible, none usable", "[G2d] shard 3's job saving shard 1's log reduced to its block bodies, END and SHA256 lines voids shards 1 and 3, only shard 2's runs eligible, none usable", "[G2e] shard 3's job saving shard 1's log reduced to one RUNSET line with an ANSI code inside the name voids shards 1 and 3, only shard 2's runs eligible, none usable", "[G2f] shard 3's job saving shard 1's log reduced to one RUNSET line with a tab and doubled spaces voids shards 1 and 3, only shard 2's runs eligible, none usable", "[G2g] shard 3's job saving shard 1's log reduced to one RUNSET line in lower case voids shards 1 and 3, only shard 2's runs eligible, none usable", "[G2i] a job_id of another shard's job written inside an answer's log voids both shards"]),
    ('collect.py', (('    text = ANSI.sub("", data.decode("utf-8", "replace"))\n', '    text = data.decode("utf-8", "replace")\n'), ), None,
     'G2: ANSI codes are not removed before the scan',
     ["[G2e] shard 3's job saving shard 1's log reduced to one RUNSET line with an ANSI code inside the name voids shards 1 and 3, only shard 2's runs eligible, none usable"]),
    ('collect.py', (('_SP = r"(?:\\s|\\\\[ntr]|\\\\u0020|\\\\u00[aA]0)+"\n', '_SP = r" "\n'), ), None,
     'G2: only a single space separates the words of a name',
     ["[G2f] shard 3's job saving shard 1's log reduced to one RUNSET line with a tab and doubled spaces voids shards 1 and 3, only shard 2's runs eligible, none usable"]),
    ('collect.py', (('                       r"(?:\\s|\\\\[ntr])*/".format(_SP), re.I)\n', '                       r"(?:\\s|\\\\[ntr])*/".format(_SP))\n'), ), None,
     'G2: names are matched case-sensitively',
     ["[G2g] shard 3's job saving shard 1's log reduced to one RUNSET line in lower case voids shards 1 and 3, only shard 2's runs eligible, none usable"]),
    ('collect.py', (('    for rx in (RAW_ID, RAW_LONG):\n', '    for rx in (RAW_LONG,):\n'), ), None,
     'G2: run and job ids in their contexts (ci/, RESULT, id keys...) are not read',
     ["[G2d] shard 3's job saving shard 1's log reduced to its block bodies, END and SHA256 lines voids shards 1 and 3, only shard 2's runs eligible, none usable"]),
    ('collect.py', (('    for rx in (RAW_ID, RAW_LONG):\n', '    for rx in (RAW_ID,):\n'), ), None,
     'G2: a bare long run or job id is not read',
     ['[G2h] a bare 11-digit run id or 12-digit bridge job id anywhere names its shard']),
    ('collect.py', (('    named |= {inv[int(m.group(1))] for m in RAW_JOB.finditer(text) if int(m.group(1)) in inv}\n', ''), ), None,
     "G2: a job_id written in the raw bytes does not name its job's shard",
     ["[G2i] a job_id of another shard's job written inside an answer's log voids both shards"]),
    ('collect.py', (('            for s_ in sorted(named):\n', '            for s_ in sorted({a[3] for a in ans if a[3] is not None}):\n'), ), None,
     'N3 (reviewer A7): a job outside the run voids only the shard of its first RUNSET line',
     ["[N3] a job outside the run saving shard 1's log with its RUNSET line deleted voids shard 1"]),
    ('collect.py', (('    if set(res) != set(byid):\n', '    if not set(byid) <= set(res):\n'), ), None,
     'N2 (reviewer C1): an extra RESULT run is no longer detected',
     ['[N2] a RESULT line for a run outside runs.json is refused']),
    ('collect.py', (('any(L[i].startswith("CHECK all ") for i in range(span[0], span[1]))', 'any(L[i].startswith("CHECK all ") for i in range(span[0], first if first is not None else span[1]))'), ), None,
     'F2 (reviewer B1): CHECK all is looked for only before the first RESULT line',
     ["[F2] a 'CHECK all UNVERIFIED stopped' line inside the assembler's output voids the shard"]),
    ('collect.py', (('any(L[i].startswith("CHECK all ") for i in range(span[0], span[1]))', 'any(raw[i].startswith("CHECK all ") for i in range(span[0], span[1]))'), ), None,
     'F2 (reviewer B2): CHECK all is looked for on the raw, timestamped lines',
     ["[F2] a 'CHECK all UNVERIFIED stopped' line inside the assembler's output voids the shard"]),
    ('collect.py', (('any(L[i].startswith("CHECK all ") for i in range(span[0], span[1]))', 'any(L[i].startswith("CHECK all UNVERIFIED the run set") for i in range(span[0], span[1]))'), ), None,
     "F2 (reviewer B3): only 'CHECK all UNVERIFIED the run set' counts",
     ["[F2] a 'CHECK all UNVERIFIED stopped' line inside the assembler's output voids the shard"]),
    ('collect.py', (('_shard_text(pd, perm[k - 1], verdicts, dict(mut,', '_shard_text(pd, perm[k - 1], None, dict(mut,'), ), None,
     'RP (reviewer D1): the permuted fixture drops its verdicts again',
     ['[RP] permutation: contradicting copies of shard 2 gives exit 2 and 4 eligible runs, none usable unless it holds, under all 6 shard numberings and 4 orders and name pairings of the answers', '[RP] permutation: a conflicting copy of shard 1 after a clean one gives exit 2 and 4 eligible runs, none usable unless it holds, under all 6 shard numberings and 4 orders and name pairings of the answers']),
    ("collect.py", 'if res.get(rid) != "HOLDS":', "if False:", "a block of a run that does not hold is taken"),
    # TRUST-BOUNDARY.md 6: the old behaviours the trust boundary removes (L1-L20 and L2j), each with the tests it
    # must fail by exact name.
    ('collect.py', (('    return _served_answer(data)\n', '    try:\n        obj = json.loads(data.decode("utf-8"))\n    except ValueError:\n        return None, "not a job-log answer"\n    if not (isinstance(obj, dict) and isinstance(obj.get("logs_content"), str)\n            and isinstance(obj.get("original_length"), int) and not isinstance(obj.get("original_length"), bool)\n            and isinstance(obj.get("job_id"), int) and not isinstance(obj.get("job_id"), bool)):\n        return None, "not a job-log answer"\n    return obj, None\n'),), None,
     "L1: lenient parsing inside the new interface (09d439d0's json.loads and three isinstance checks)",
     ["[TB-D5] two logs_content keys in shard 1's only file are refused in either order, shard 1 missing with the file as its candidate", "[TB-D1] a duplicated job_id (a foreign id or another shard's first) or an earlier logs_content holding shard 3's log is refused (D1, D2, D3)", "[TB-D1b] a foreign job's answer with a trailing job_id 77001 is refused, as shard 1's only file and beside genuine shard 1 (D1b, D1c)", '[TB-D4] an earlier logs_content naming no shard is refused', "[TB-X3] a message other than the tool's success message is refused: a contradicting log (X3), a RUNSET line (X1), 'm' beside genuine S1 (C4), one character, case, a trailing space, a non-string", '[TB-KEY] unknown keys are refused: an extra key (X2), Message, a tool envelope (G1c), the failed-jobs answer']),
    ('collect.py', (('SERVED_DECODER = json.JSONDecoder(strict=True, object_pairs_hook=_no_duplicates,', 'SERVED_DECODER = json.JSONDecoder(strict=True, object_pairs_hook=dict,'),), None,
     "L2: SERVED_DECODER's object_pairs_hook replaced by dict (last-wins)",
     ["[TB-D5] two logs_content keys in shard 1's only file are refused in either order, shard 1 missing with the file as its candidate", "[TB-D1] a duplicated job_id (a foreign id or another shard's first) or an earlier logs_content holding shard 3's log is refused (D1, D2, D3)", "[TB-D1b] a foreign job's answer with a trailing job_id 77001 is refused, as shard 1's only file and beside genuine shard 1 (D1b, D1c)", '[TB-D4] an earlier logs_content naming no shard is refused', '[TB-DEEP2a] a duplicate key inside a nested value is refused as a duplicate, before any type check']),
    ('collect.py', (('JOBS_DECODER = json.JSONDecoder(strict=True, object_pairs_hook=_no_duplicates,', 'JOBS_DECODER = json.JSONDecoder(strict=True, object_pairs_hook=dict,'),), None,
     "L2j: JOBS_DECODER's object_pairs_hook replaced by dict (last-wins in the jobs list and runs.json)",
     ['[TB-DEEP2b] a jobs list with a duplicated id inside a job object is refused, through main and read from disk']),
    ('collect.py', (('SERVED_DECODER = json.JSONDecoder(strict=True, object_pairs_hook=_no_duplicates,', 'SERVED_DECODER = json.JSONDecoder(strict=True, object_pairs_hook=lambda p: dict(reversed(p)),'),), None,
     "L3: SERVED_DECODER's hook keeps the first value of a duplicated key (first-wins)",
     ["[TB-D5] two logs_content keys in shard 1's only file are refused in either order, shard 1 missing with the file as its candidate", "[TB-D1b] a foreign job's answer with a trailing job_id 77001 is refused, as shard 1's only file and beside genuine shard 1 (D1b, D1c)"]),
    ('collect.py', (('    if keys != REQUIRED_KEYS and keys != REQUIRED_KEYS | {"message"}:\n', '    if not REQUIRED_KEYS <= keys:\n'),), None,
     'L4: the key-set check relaxed to required <= keys (extra keys allowed)',
     ['[TB-KEY] unknown keys are refused: an extra key (X2), Message, a tool envelope (G1c), the failed-jobs answer']),
    ('collect.py', (('    if "message" in obj and obj["message"] != SUCCESS_MESSAGE:\n', '    if False:\n'),), None,
     'L5: the message value is not checked',
     ["[TB-X3] a message other than the tool's success message is refused: a contradicting log (X3), a RUNSET line (X1), 'm' beside genuine S1 (C4), one character, case, a trailing space, a non-string"]),
    ('collect.py', (('BLOCK_DECODER = json.JSONDecoder(strict=True, object_pairs_hook=_no_duplicates, parse_constant=_no_constant)', 'BLOCK_DECODER = json.JSONDecoder(strict=True, object_pairs_hook=_no_duplicates)'),), None,
     "L6: BLOCK_DECODER's parse_constant removed",
     ['[TB-NAN] NaN, Infinity and -Infinity are refused in a served file and in a result block (B1)']),
    ('collect.py', (('    if data[:3] == b"\\xef\\xbb\\xbf":\n        return None, "byte-order mark before the object"\n', ''), ('        text = data.decode("utf-8")\n', '        text = data.decode("utf-8-sig")\n')), None,
     'L7: the BOM check of 2.2 step 2 removed and the bytes decoded as utf-8-sig',
     ['[TB-BOM] a byte-order mark before the object is refused (E7)']),
    ('collect.py', (('    if end != len(text) and (served or text[end:].strip(" \\t\\n\\r")):\n        return None, "data after the object"\n', ''),), None,
     'L8: the end == len(text) check removed (data after the object allowed)',
     ['[TB-TRAIL] exactly one object and nothing before or after it: E8, a trailing payload, a trailing newline, a leading space']),
    ('collect.py', (('        target = staging\n', '        target = out\n        os.makedirs(out, exist_ok=True)\n'), ('        os.rename(staging, out)  # the commit point: out appears whole, or not at all\n', '        pass\n')), None,
     'L9: no staging: the collection is written directly into --out and the rename is skipped',
     ['[TB-O5] a failed rename after a complete staging is ABORTED (exit 4), --out absent, no COLLECT PUBLISHED line', '[TB-O6] a failed result write is ABORTED (exit 4), --out absent, and the COLLECT FILE lines trace every served file']),
    ('collect.py', (('        if os.path.lexists(out):\n', '        if False:\n'),), None,
     'L10: the S1 existence check removed',
     ['[TB-O1] a collection into an existing --out holding a stale ci/800/results.json is refused (exit 3), the stale file untouched', '[TB-O2] a collection into an existing --out holding a stale HOLDS collected.json is refused (exit 3), untouched', '[TB-O3] an --out that is an empty directory, a file, a symbolic link or a dangling link is refused (exit 3), untouched']),
    ('collect.py', (('    return run_collection(a.served, a.out, head=a.head, durable=durable, inputs=(a.runs, a.run_jobs))\n', '    try:   # an exception here is left to the collection below, so the mutant never crashes a suite\n        iv0 = inventory([], lambda s_: None, a.runs, a.run_jobs)\n        d0, _, q3 = interpret_runs(iv0["runs"])\n        early = q3 or interpret_jobs(iv0["jobs"], d0, a.head)[2]\n    except BaseException:\n        early = False\n    if early:\n        emit(sys.stdout, "COLLECT FAILS")\n        return 1\n    return run_collection(a.served, a.out, head=a.head, durable=durable, inputs=(a.runs, a.run_jobs))\n'),), None,
     'L11: the early S3 and S4 failures return before publishing (the 09d439d0 main)',
     ['[TB-RUNS] a runs.json other than the pinned file is published quarantined (exit 1), its digest recorded with pinned false, every served file recorded', '[TB-JOBS] a jobs list omitting shard 32, not JSON, not UTF-8 or with a BOM is published quarantined (exit 1), recorded by digest, every expected answer undetermined']),
    ('collect.py', (("        digests = sorted({c[2] for c in copies})   # every copy's digest (N3)\n", '        digests = [dig]\n'),), None,
     "L12: only the first copy's digest is recorded (N3)",
     ["[TB-N3] byte-distinct copies with one identity (C3, C4s) hold, and every copy's name and digest is recorded"]),
    ('collect.py', (('        raw = raw if raw is None else raw | raw_named(obj["logs_content"].encode("utf-8"), doc, inv)  # the decoded scan\n', '        pass\n'),), None,
     'L13: the decoded scan removed',
     ['[TB-ESC] a trailer line naming shard 1 in genuine S3 voids shards 1 and 3, spelled plainly or with a JSON escape (E-esc)']),
    ('collect.py', (('        if len(set(index.values())) != len(index):   # one id under two shard names (TRUST-BOUNDARY.md 1, J1)\n', '        if False:\n'),), None,
     "L14: the jobs list's shard job ids are not required distinct",
     ['[TB-JOBID] one job id under two shard names is refused, through main and read from disk']),
    ('collect.py', (('    raw = text.split("\\n")   # a whole answer: original_length == count("\\n") + 1, no trailing "\\n" (2.4)\n', '    raw = text.split("\\n")\n    if raw and raw[-1] == "":\n        raw.pop()\n'),), None,
     'L15: the trailing-newline tolerance restored',
     ['[TB-NL] a whole answer ending in a newline is refused as not whole']),
    ('collect.py', (('            ok = ok and isinstance(r.get("expected"), dict) and isinstance(r["expected"].get("outcome"), str)\n', ''),), None,
     'L16: the expected.outcome check removed',
     ['[TB-K1] a canonical block whose expected is null is a validation failure, recorded with its digest']),
    ('collect.py', (('SCAN_ERRORS = (ValueError,)', 'SCAN_ERRORS = ()'),), None,
     "L17: the per-file catch removed (a scan's ValueError reaches S10's internal quarantine)",
     ["[TB-SCAN] a scan's conversion error (a 5,000-digit job_id, shard number, escaped job_id digits, or EXTRACT SHARD number) rejects only that file, with all 4 files recorded and the collection published quarantined"]),
    ('collect.py', (('SCAN_ERRORS = (ValueError,)', 'SCAN_ERRORS = (Exception,)'),), None,
     'L18: the per-file catch widened from ValueError to Exception',
     ["[TB-SCANX] a host failure at intake (MemoryError, ENOSPC or EIO in the byte scan, EIO or MemoryError in the read, an interrupt) is ABORTED (exit 4), nothing published, never a file's rejection"]),
    ('collect.py', (('    except HOST_FAILURES:   # a host failure is never an internal quarantine: ABORTED (2.5)\n        _lines_once(P, st)\n        raise\n', ''),), None,
     'L19: S10 catches a host failure (MemoryError, OSError) as an internal quarantine and publishes it',
     ["[TB-SCANX] a host failure at intake (MemoryError, ENOSPC or EIO in the byte scan, EIO or MemoryError in the read, an interrupt) is ABORTED (exit 4), nothing published, never a file's rejection"]),
    ('collect.py', (('        if e.errno not in OWN_ACCESS:   # the read: EIO and every other host failure propagate (2.5)\n            raise\n', '        if False:\n            raise\n'),), None,
     "L20: step 1 records every OSError of a read as the file's unreadable kind, EIO included",
     ["[TB-SCANX] a host failure at intake (MemoryError, ENOSPC or EIO in the byte scan, EIO or MemoryError in the read, an interrupt) is ABORTED (exit 4), nothing published, never a file's rejection"]),
    # TRUST-BOUNDARY.md 6 at 009b7062: L21-L33, the old behaviours of the inventory-first revision, and L34-L35 for the
    # design review's note N3, each with the tests it must fail by exact name.
    ('collect.py', (('    except SCAN_ERRORS as e:\n        entry["reason"] = "decoded scan failed', '    except Exception as e:\n        entry["reason"] = "decoded scan failed'),), None,
     "L21: the review's X1: the decoded scan's catch widened from SCAN_ERRORS to Exception (the other two catches unchanged)",
     ['[TB-SCANXd] a host failure in the decoded scan (MemoryError, ENOSPC, EIO) is ABORTED (exit 4), nothing published, never decoded scan failed']),
    ('collect.py', (('    except SCAN_ERRORS as e:\n        entry["reason"] = "parsed scan failed', '    except Exception as e:\n        entry["reason"] = "parsed scan failed'),), None,
     "L22: the review's X2: the parsed readings' catch widened from SCAN_ERRORS to Exception (the other two catches unchanged)",
     ['[TB-SCANXp] a host failure in the parsed readings (MemoryError, ENOSPC, EIO from shard_of, EIO from shards_named) is ABORTED (exit 4), nothing published, never parsed scan failed']),
    ('collect.py', (('        if e.errno in NAMES_NOTHING:   # a missing, mistyped or mangled path\n', '        if True:\n'),), None,
     "L23: the review's X6: every OSError from lstat recorded as missing, EIO included",
     ['[TB-LSTATX] a host failure at lstat (EIO, ENOSPC, MemoryError, a path through a symbolic-link loop) is ABORTED in S2b, never missing', "[TB-LSTATC] ENOENT and EACCES at lstat are the file's own conditions, missing and unreadable: published (exit 1), all four files recorded"]),
    ('collect.py', (('        if e.errno not in OWN_ACCESS + (errno.ELOOP,):   # ELOOP: it became a link between lstat and open\n            raise\n', '        if False:\n            raise\n'),), None,
     "L24: the review's X7: every OSError from open recorded as unreadable (the re-raise removed)",
     ['[TB-OPENX] a host failure at open (EIO, ENOSPC, MemoryError) is ABORTED in S2b, never unreadable']),
    ('collect.py', (('            if e.errno not in NAMES_NOTHING + OWN_ACCESS + (errno.ELOOP,):   # a dangling or looping link: no digest\n                raise\n', '            if False:\n                raise\n'),), None,
     "L25: the review's X14: every OSError while hashing a link's target swallowed, the link recorded with a null digest",
     ["[TB-LINKX] a host failure while hashing a symbolic link's target (EIO at stat, ENOSPC or MemoryError at the read) is ABORTED in S2b, never a symlink record with a null digest"]),
    ('collect.py', (('        _inventory_served(inv, served_files)\n', ''), ('    st["stage"] = "S5"\n', '    _inventory_served(iv, iv["paths"])\n    st["stage"] = "S5"\n'),), None,
     "L26: a77c85a5's order: the served arguments are inventoried only after S3 and S4 have interpreted runs.json and the jobs list",
     ['[TB-INVINT] an unforeseen exception while the jobs list is interpreted (S4) publishes the full inventory, every served file unjudged']),
    ('collect.py', (('    except BaseException:   # S2b: the inventory is incomplete, so nothing may be published (exit 4)\n        _file_lines(P, inv["files"])\n        raise\n', '    except Exception as e:\n        if isinstance(e, HOST_FAILURES):\n            _file_lines(P, inv["files"])\n            raise\n        inv["deferred"] = e\n'), ('def _evaluate(iv, given, head, P, st):\n', 'def _evaluate(iv, given, head, P, st):\n    if iv.get("deferred") is not None:\n        raise iv["deferred"]\n'),), None,
     "L27: an exception inside S2b that is no file's condition, host failure or interrupt becomes S10's internal quarantine, the entries so far published",
     ['[TB-INVX] an unforeseen exception in the inventory (read_input on argument 1) is ABORTED in S2b, nothing published']),
    ('collect.py', (('        _lines_once(P, st)   # the arguments S5 had not judged stay unjudged (TRUST-BOUNDARY.md 3, S10)\n', '        st["files"][:] = [x for x in st["files"] if x["status"] != "unjudged"]\n        _lines_once(P, st)\n'),), None,
     "L28: declared deviation (4) restored: an internal error's record keeps only the entries S5 had judged",
     ['[TB-INVINTf] an unforeseen exception in the intake of argument 1 (S5) publishes every served file, the ones not judged marked unjudged', '[TB-INVINT] an unforeseen exception while the jobs list is interpreted (S4) publishes the full inventory, every served file unjudged']),
    ('collect.py', (('                                parse_float=_no_float, parse_int=_jobs_int)', '                                parse_int=_jobs_int)'), ('            probs = jobs_schema(jobsd)   # J-1 to J-5, before build_job_index reads any value (2.3)\n', '            probs = []\n'), ('    except (KeyError, TypeError, AttributeError):\n', '    except (KeyError, TypeError, AttributeError, OverflowError):\n'),), None,
     "L29: the label fix: JOBS_DECODER admits floats, jobs_schema skipped, OverflowError added to build_job_index's except tuple",
     ['[TB-INVJ] a jobs list whose total_count is 1e400 is refused at the jobs-input gate (non-integer number) with the full inventory, published (exit 1)', '[TB-JNUM] every fraction, exponent, constant, bool, string, null, out-of-range or absent count or id of the jobs list is refused with its exact problem, in the unit and through main']),
    ('collect.py', (('    if type(tc) is not int or not 0 <= tc <= MAX_JOBS:\n', '    if False:\n'), ('            if f not in j or type(j[f]) is not int or not 1 <= j[f] <= MAX_ID:\n', '            if f not in j:\n'), ('            if f not in j or type(j[f]) is not str:\n', '            if f not in j:\n'),), None,
     "L30: the integer schema's type and range conditions removed (J-2, J-4 and J-5 test presence only)",
     ['[TB-JNUM] every fraction, exponent, constant, bool, string, null, out-of-range or absent count or id of the jobs list is refused with its exact problem, in the unit and through main']),
    ('collect.py', (('    text = json.dumps(record, indent=1, sort_keys=True, allow_nan=False) + "\\n"', '    text = json.dumps(record, indent=1, sort_keys=True) + "\\n"'),), None,
     'L31: allow_nan=False dropped from the serialization of collected.json',
     ['[TB-NANOUT] a non-finite run id given directly is never published: ABORTED (exit 4) at the strict serialization']),
    ('collect.py', (('    print("".join(out), file=outp)\n', '    print(line, file=outp)\n'),), None,
     "L32: the review's X9: the emit backstop removed (the line printed as given)",
     ['[TB-EMIT] emit writes one printable-ASCII line, writing a line feed, a carriage return, a form feed, U+0085, U+2028, U+2029 and U+00E9 as their JSON escapes']),
    ('collect.py', (('(" " + esc(e.get("outcome", ""))) if e["usable"] else', '(" " + e.get("outcome", "")) if e["usable"] else'),), None,
     "L33: a usable run's outcome printed raw on its RUN line (a77c85a5)",
     ["[TB-OUTC] a usable run's outcome holding a line feed, COLLECT FAILS and U+2028 is JSON-escaped on its RUN line"]),
    ('collect.py', (('        P("COLLECT FAIL internal error at %s: %s; the whole collection is quarantined" % (st["stage"], type(e).__name__))\n', '        st["inputs"] = {"runs_json": None, "jobs_list": None}\n        P("COLLECT FAIL internal error at %s: %s; the whole collection is quarantined" % (st["stage"], type(e).__name__))\n'),), None,
     "L34 (design review N3): an internal error's record loses collection.inputs (AR-B1's null inputs)",
     ['[TB-INVINTr] an unforeseen exception while runs.json is interpreted (S3) publishes the full inventory, every served file unjudged', '[TB-INVINT] an unforeseen exception while the jobs list is interpreted (S4) publishes the full inventory, every served file unjudged']),
    ('collect.py', (('    rec, data = read_input(path)\n    rec.pop("_id")\n    meta = ', '    try:\n        rec, data = read_input(path)\n    except OSError as e:\n        rec, data = {"name": os.path.basename(path), "kind": "unreadable", "size": None, "sha256": None,\n                     "reason": "not a regular file (unreadable: %s)" % _errname(e), "_id": None}, None\n    rec.pop("_id")\n    meta = '),), None,
     "L35 (design review N3): a host failure while --runs or --run-jobs is read is recorded as that input's unreadable condition",
     ["[TB-INVHX] a host failure in S2b's read of --runs or --run-jobs (EIO, ENOSPC, MemoryError) is ABORTED (exit 4), nothing published"]),
    # The acceptance review of de9c56a1: its surviving mutants R3, R12, X15, R5 and R6, each with its regression test.
    ('collect.py', (('            probs = jobs_schema(jobsd)   # J-1 to J-5, before build_job_index reads any value (2.3)\n            if not probs and doc is not None:\n                index, run_id, probs = build_job_index(jobsd, head, doc["shards"])\n', '            probs = []\n            if doc is not None:\n                index, run_id, probs = build_job_index(jobsd, head, doc["shards"])\n            probs = probs or jobs_schema(jobsd)\n'),), None,
     "L36 (acceptance review R3, note N1): the jobs schema runs after build_job_index, only when the index found no problem",
     ['[TB-JNUMp] through main with the pinned runs.json, which builds the job index for a list the schema passes, a bool, string or out-of-range count, id or run_id and a null head_sha are refused by the schema with its exact problem, before build_job_index reads them']),
    ('collect.py', ((' or any(type(j) is not dict for j in jobs):', ':'),), None,
     "L37 (acceptance review R12, note N2): J-3's every-job-is-an-object check dropped",
     ['[TB-JOBJ] a job that is not an object (a number, a string, a list, an empty list, null, a bool) is refused by J-3 with its exact problem, in the unit and through main with the pinned runs.json, never an internal error']),
    ('collect.py', (('        except HOST_FAILURES:\n            raise\n        except Exception:  # noqa: BLE001 - a run set too malformed to list\n', '        except Exception:  # noqa: BLE001 - a run set too malformed to list\n'),), None,
     "L38 (acceptance review X15, note N3): the S10 fallback swallows a host failure again (a77c85a5:745)",
     ["[TB-INVINTh] a host failure (MemoryError, ENOSPC, EIO) while S10's internal handler lists the run set, after an unforeseen exception in S5, is ABORTED (exit 4), nothing published, never an internal record"]),
    ('collect.py', (('sort_keys=True, ensure_ascii=True,\n                                         allow_nan=False))', 'sort_keys=True, ensure_ascii=True))'),), None,
     "L39 (acceptance review R5, note N5): allow_nan=False dropped from the COLLECT FILE lines",
     ['[TB-NANLINE] esc and the COLLECT FILE lines refuse NaN, Infinity and -Infinity (ValueError) and print nothing']),
    ('collect.py', (('    return json.dumps(v, ensure_ascii=True, allow_nan=False)\n', '    return json.dumps(v, ensure_ascii=True)\n'),), None,
     "L40 (acceptance review R6, note N5): allow_nan=False dropped from esc",
     ['[TB-NANLINE] esc and the COLLECT FILE lines refuse NaN, Infinity and -Infinity (ValueError) and print nothing']),
]


# The mutant phase runs two mutants at a time (TRUST-BOUNDARY.md 6, the runtime budget). Each runs in its own copy of
# batchx/ and its suites in their own mkdtemp under --work; results are printed in MUTANTS order, so the output, the
# kill rule and the table are what one worker gives. Two conditions of the design review of 009b7062 (note N1):
# - the free space on the work filesystem is read before and after each mutant. A reading under DISK_FLOOR makes that
#   mutant an INFRASTRUCTURE failure of this run: never a kill, never a survival, and the run fails. One collect
#   self-test peaks at 23.7 MB of temporary files, so two workers need about 50 MB; the floor leaves a margin over that.
# - an exception in a worker (a copy that fails, a suite that times out) fails this run; it is never dropped.
WORKERS = 2
DISK_FLOOR = 64 << 20


def free_bytes(path):
    st = os.statvfs(path)
    return st.f_bavail * st.f_frsize


def run_mutant(i, entry, base, extractor, work):
    """One mutant in its own copy: {lines, killed, row}. Printing is left to the caller."""
    fname, old, new, what = entry[:4]
    expect = entry[4] if len(entry) > 4 else None
    d = os.path.join(work, "m%02d" % i)
    pairs = old if isinstance(old, tuple) else ((old, new),)
    src = open(os.path.join(base, fname), encoding="utf-8").read()
    counts = [src.count(o) for o, _ in pairs]
    if counts != [1] * len(pairs):
        return {"lines": ["  FAIL  mutant %02d (%s): its text occurs %s times" % (i, what, counts)], "killed": False,
                "row": None}
    shutil.copytree(base, d)
    try:
        for o, nw in pairs:
            src = src.replace(o, nw)
        with open(os.path.join(d, fname), "w", encoding="utf-8") as f:
            f.write(src)
        outs = []
        rc = selftests(d, extractor, work, outs, only=SUITES[fname])
        names, crashed = failing_cases(outs)
        k = any(rc)
        missing = [e for e in (expect or []) if e not in names]   # exact names, never substrings
        specific = expect is None or (not missing and not crashed)
        line = "  %s  mutant %02d %s: %s (exit codes %s)%s" % (
            "ok  " if k and specific else "FAIL", i, fname, what, rc,
            "" if specific else " -- expected tests not failing: %s%s" % (missing, " (a suite crashed)" if crashed else ""))
        return {"lines": [line], "killed": bool(k and specific),
                "row": (i, what, expect, names) if expect is not None else None}
    finally:
        shutil.rmtree(d, ignore_errors=True)


def mutant_phase(entries, run_one, free, floor, workers):
    """Every entry through run_one(i, entry), at most `workers` at a time; the results in entries' order. Each result
    is {lines, killed, infra, row}. free(i, when) reads the free space before and after mutant i."""
    def guarded(i, entry):
        before = free(i, "before")
        if before < floor:
            return {"lines": ["  FAIL  mutant %02d: INFRASTRUCTURE: %d MiB free before it ran, under the %d MiB floor; "
                              "not run, neither a kill nor a survival" % (i, before >> 20, floor >> 20)],
                    "killed": False, "infra": True, "row": None}
        r = run_one(i, entry)
        after = free(i, "after")
        if after < floor:
            return {"lines": ["  FAIL  mutant %02d: INFRASTRUCTURE: %d MiB free after it ran, under the %d MiB floor; "
                              "its result is void, neither a kill nor a survival" % (i, after >> 20, floor >> 20)],
                    "killed": False, "infra": True, "row": None}
        return dict(r, infra=False)
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as ex:
        futs = [ex.submit(guarded, i, e) for i, e in enumerate(entries)]
        results = []
        for i, fut in enumerate(futs):
            try:
                results.append(fut.result())
            except Exception as e:  # noqa: BLE001 - a worker's exception fails the run, never dropped
                results.append({"lines": ["  FAIL  mutant %02d: the worker raised %s: %s" % (i, type(e).__name__, e)],
                                "killed": False, "infra": False, "row": None})
    return results


def phase_selfcheck():
    """The two conditions of the mutant phase, shown on simulated readings and workers (no disk is filled, no suite
    runs): a free-space reading under the floor, before or after a mutant, is INFRASTRUCTURE and fails the run;
    a worker's exception fails the run; neither counts as a kill; and results come back in entries' order."""
    entries = [("collect.py", "a", "b", "m%d" % k) for k in range(5)]
    low = {(1, "after"), (3, "before")}
    ran = []

    def run_one(i, entry):
        time.sleep(0.02 * (5 - i))   # finish out of order
        ran.append(i)
        if i == 2:
            raise OSError(28, "simulated: No space left on device")
        return {"lines": ["  ok    mutant %02d" % i], "killed": True, "row": None}
    res = mutant_phase(entries, run_one, lambda i, when: (1 << 20) if (i, when) in low else (1 << 40), 64 << 20, 2)
    disk = (len(res) == 5 and res[1]["infra"] and not res[1]["killed"] and "INFRASTRUCTURE" in res[1]["lines"][0]
            and res[3]["infra"] and not res[3]["killed"] and 3 not in ran and "not run" in res[3]["lines"][0]
            and all(res[k]["killed"] and not res[k]["infra"] for k in (0, 4)))
    worker = (not res[2]["killed"] and not res[2]["infra"] and "the worker raised OSError" in res[2]["lines"][0]
              and all(("mutant %02d" % k) in res[k]["lines"][0] for k in range(5)) and sorted(ran) == [0, 1, 2, 4]
              and ran != sorted(ran))
    print("  %s  [N1-DISK] the mutant phase reports a free-space reading under the floor, before or after a mutant, as "
          "INFRASTRUCTURE: never a kill or a survival, and the run fails" % ("ok  " if disk else "FAIL"))
    print("  %s  [N1-WORKER] an exception in a mutant-phase worker fails the run and is never dropped; results come "
          "back in MUTANTS order" % ("ok  " if worker else "FAIL"))
    return int(not disk) + int(not worker)


def tally_selfcheck(work):
    """main's own tally of the mutant phase (the acceptance review's note N4), on a fresh copy of this module whose
    main runs unchanged: the end-to-end pass, the suites, the self-checks and four mutants are simulated (no suite
    runs), and the free-space reading after mutant 1, in the worker that ran it, is under the floor. main must report
    that mutant INFRASTRUCTURE and nothing else, count it neither as a kill nor as a survival, and fail the run."""
    import contextlib
    import threading
    m = load(os.path.abspath(__file__), "controls_tally")
    tl = threading.local()

    def fake_free(path):
        if getattr(tl, "low", False):
            tl.low = False
            return 1 << 20
        return 1 << 40

    def fake_run(i, entry, base, extractor, work_):
        tl.low = i == 1
        return {"lines": ["  ok    mutant %02d %s: %s (exit codes [1])" % (i, entry[0], entry[3])], "killed": True,
                "row": None}
    m.MUTANTS = [("collect.py", "a", "b", "simulated %d" % k) for k in range(4)]
    m.end_to_end = lambda extractor, work_: 0
    m.selftests = lambda d, extractor, work_, outputs=None, only=None: [0, 0, 0]
    m.phase_selfcheck = lambda: 0
    m.tally_selfcheck = lambda work_: 0
    m.run_mutant, m.free_bytes = fake_run, fake_free
    buf = io.StringIO()
    try:
        with contextlib.redirect_stdout(buf):
            rc = m.main(["--extractor", os.devnull, "--work", work])
        err = None
    except Exception as e:  # noqa: BLE001 - a crash of main is this check's failure, never the run's traceback
        rc, err = None, type(e).__name__
    L = buf.getvalue().split("\n")
    m01 = [l for l in L if "mutant 01" in l]
    ok = (err is None and rc == 1 and len(m01) == 1 and m01[0].startswith("  FAIL  mutant 01: INFRASTRUCTURE")
          and "neither a kill nor a survival" in m01[0]
          and all(sum(1 for l in L if l.startswith("  ok    mutant %02d " % k)) == 1 for k in (0, 2, 3))
          and "controls: 3 of 4 mutants killed" in L and "controls: 1 failure(s)" in L
          and any(l.startswith("controls: 1 mutant(s) not judged: INFRASTRUCTURE") for l in L))
    print("  %s  [N4-TALLY] main reports a mutant whose free-space reading falls under the floor as INFRASTRUCTURE: it "
          "fails the run and is counted neither as a kill nor as a survival" % ("ok  " if ok else "FAIL"))
    if not ok:
        print("        | exit %s, raised %s; %s" % (rc, err, [l for l in L if "mutant" in l or l.startswith("controls:")]))
    return int(not ok)


FAILED_CASE = re.compile(r"^  FAIL  (.*?)(?: -> .*)?$")


# The suites a mutant of each file can change (TRUST-BOUNDARY.md 6, the runtime budget): no suite reads collect.py
# but its own; assemble.py's self-test reads host.py (assemble.py:1294). The unmutated copy runs all three.
SUITES = {"assemble.py": ("assemble",), "host.py": ("assemble", "host"), "collect.py": ("collect",)}


def selftests(d, extractor, work, outputs=None, only=None):
    cmds = [("assemble", [sys.executable, "-I", "-B", os.path.join(d, "assemble.py"), "--self-test", "--extractor", extractor, "--work", work]),
            ("host", [sys.executable, "-I", "-B", os.path.join(d, "host.py"), "--self-test", "--work", work]),
            ("collect", [sys.executable, "-I", "-B", os.path.join(d, "collect.py"), "--self-test", "--work", work])]
    cmds = [c for nm, c in cmds if only is None or nm in only]
    rcs = []
    for c in cmds:
        p = subprocess.run(c, capture_output=True, text=True, timeout=900)
        rcs.append(p.returncode)
        if outputs is not None:
            outputs.append(p.stdout + p.stderr)
    return rcs


def failing_cases(outputs):
    """The names of the self-test cases that failed, and whether a suite stopped with a traceback."""
    names, crashed = [], False
    for out in outputs:
        crashed = crashed or "Traceback (most recent call last)" in out
        names += [m.group(1).strip() for m in (FAILED_CASE.match(l) for l in out.split("\n")) if m]
    return names, crashed


def load(path, name):
    mod = types.ModuleType(name)
    mod.__file__ = path
    with open(path, "rb") as f:
        exec(compile(f.read(), path, "exec"), mod.__dict__)  # noqa: S102 - this directory's own sources
    return mod


def end_to_end(extractor, work):
    A = load(os.path.join(HERE, "assemble.py"), "assemble")
    K = load(os.path.join(HERE, "collect.py"), "collect")
    ex = A.load_extractor(extractor)
    base = tempfile.mkdtemp(prefix="controls-e2e-", dir=work)
    try:
        def serve(mut, red):
            inputs, doc, xc = A._fixture(os.path.join(base, "f%d" % len(os.listdir(base))), 0, mut)
            buf = io.StringIO()
            code = A.run_all(ex, doc, 1, inputs, xc, out=buf)
            out = buf.getvalue()
            # the runner's own lines after the verdict, as a real shard log has them: two post-checkout blocks of
            # 12 lines, the orphan cleanup and the Node.js warning, and the exit annotation when the shard is red
            after = (["##[error]Process completed with exit code %d." % code] if red else []) + \
                (["Post job cleanup.", "[command]/usr/bin/git version"] + ["[command]/usr/bin/git config --local x"] * 10) * 2 \
                + ["Cleaning up orphan processes", "##[warning]Node.js 20 is deprecated."]
            # the host step's own lines, from host.py's own format strings, for this shard's runs
            hsrc = open(os.path.join(HERE, "host.py"), encoding="utf-8").read()
            fmts = re.findall(r'print\("(host [^"]*)"', hsrc)
            sh_runs = [r for r in doc["runs"] if r["shard"] == 1]
            host_lines = []
            for f_ in fmts:
                for r in sh_runs:
                    vals = iter([1, r["run_id"], r["bridge_job_id"], "ok", "ok", "ok", "", 7, 1000, "ok"])
                    host_lines.append(re.sub(r"%[sd]", lambda m_: str(next(vals)), f_))
            lines = ["Current runner version: '2.337.0'", "Complete job name: Extract shard 1", "env:", "  SHARD: 1",
                     "##[group]Run python3 -I batchx/host.py --runs batchx/runs.json --shard \"$SHARD\" --out x"] \
                + host_lines + ["##[group]Run python3 -I batchx/assemble.py", "##[endgroup]"] \
                + out.rstrip("\n").split("\n") + after
            text = "\n".join("2026-12-01T10:%02d:%02d.1234567Z %s" % (i // 60 % 60, i % 60, l) for i, l in enumerate(lines))
            return code, dict(A._blocks(out)), doc, text, len(lines)

        code, printed, doc, text, nl = serve({}, False)
        # the full intake in the job-log tool's real byte format (TRUST-BOUNDARY.md 2.1): the strict grammar, then
        # read_shard; U+FEFF first, the success message, compact, sorted keys, HTML escapes
        real = K._tool_json({"job_id": 1, "logs_content": chr(0xfeff) + text, "message": K.SUCCESS_MESSAGE,
                             "original_length": nl}).encode("utf-8")
        obj, why = K.parse_served(real)
        k, probs, res = K.read_shard(obj, doc, {1: 1}) if obj is not None else (None, [why], {})
        ok = code == 0 and k == 1 and not probs and sorted(res) == ["901", "902", "903"] and all(
            v == "HOLDS" and body == printed[rid] for rid, (v, body) in res.items())
        print("  %s  assemble.py's real output, served whole with 26 runner lines after it in the job-log tool's byte "
              "format, passes the strict grammar and is collected: 3 runs, blocks byte-identical, the pinned blobs named%s"
              % ("ok  " if ok else "FAIL", "" if ok else " -- %s %s" % (code, probs[:3])))
        k2, probs2, _ = K.read_shard({"job_id": 1, "logs_content": "\n".join(text.split("\n")[5:]), "original_length": nl},
                                     doc, {1: 1})
        ok2 = k2 is None and probs2 and "not whole" in probs2[0]
        print("  %s  the same output served as a tail is refused" % ("ok  " if ok2 else "FAIL"))
        code3, printed3, doc3, text3, nl3 = serve({"901": {"head": "f" * 40}}, True)
        k3, probs3, res3 = K.read_shard({"job_id": 1, "logs_content": text3, "original_length": nl3}, doc3, {1: 1})
        ok3 = code3 == 1 and k3 == 1 and not probs3 and res3["901"][0] == "FAILS" and res3["902"] == ("HOLDS", printed3["902"])
        print("  %s  a red shard's real output, with its exit annotation and runner lines after the verdict, is read: "
              "its FAILS run named, its holding runs collected%s" % ("ok  " if ok3 else "FAIL", "" if ok3 else " -- %s" % probs3[:3]))
        # N1: the real output, the host step's lines and the runner's lines name the shard's own shard only
        inv = {1: 1}
        names = [K.raw_named(json.dumps({"job_id": 1, "logs_content": t_, "original_length": n_}).encode(), d_, inv)
                 for t_, n_, d_ in ((text, nl, doc), (text3, nl3, doc3))]
        # the decoded scan (TRUST-BOUNDARY.md 2.5 step 5), compared with the byte scan on the same basis: the answer's
        # own job_id envelope excluded
        decoded = [K.raw_named(t_.encode("utf-8"), d_, inv) for t_, d_ in ((text, doc), (text3, doc3))]
        no_env = [K.raw_named(json.dumps({"logs_content": t_}).encode(), d_, inv) for t_, d_ in ((text, doc), (text3, doc3))]
        ok4 = names == [{1}, {1}] and decoded == [{1}, {1}] and no_env == decoded
        print("  %s  [N1] the assembler's real output, host.py's own lines and the runner's lines name only their own "
              "shard (green and red shard), in the byte scan and in the decoded scan, which agree without the job_id "
              "envelope%s" % ("ok  " if ok4 else "FAIL", "" if ok4 else " -- %s %s %s" % (names, decoded, no_env)))
        return int(not ok) + int(not ok2) + int(not ok3) + int(not ok4)
    finally:
        shutil.rmtree(base, ignore_errors=True)


BRANCH = "tmp/ci-batch-extract-design-20261017"


def plan_problems(wf, runs_text, scripts, xc_text):
    """The static checks of part 3; returns a list of problems (empty when the plan holds)."""
    P = []
    # comment lines are prose; only the workflow's code lines are checked (an inline "# v4" after a pin is dropped)
    wf = "\n".join(re.sub(r"\s+#.*$", "", l) for l in wf.split("\n") if not l.lstrip().startswith("#")) + "\n"
    doc = json.loads(runs_text)
    rs = doc["runs"]
    ids = [r["run_id"] for r in rs]
    if len(rs) != 223 or len(set(ids)) != len(ids) or len({r["bridge_job_id"] for r in rs}) != len(rs):
        P.append("runs.json: not 223 distinct runs and jobs")
    if [r["expires"] for r in rs] != sorted(r["expires"] for r in rs):
        P.append("runs.json: not in expiry order")
    sh = [r["shard"] for r in rs]
    if sh != sorted(sh) or set(sh) != set(range(1, doc["shards"] + 1)) or \
            max(sh.count(k) for k in set(sh)) > doc["shard_size"]:
        P.append("runs.json: shards not contiguous 1..%s of at most %s" % (doc["shards"], doc["shard_size"]))
    digest = hashlib.sha256(runs_text.encode()).hexdigest()
    for name, text in scripts.items():
        if not re.search(r'^RUNS_SHA256 = "%s"$' % digest, text, re.M):
            P.append("%s does not pin runs.json's sha256" % name)
    if not re.search(r'^CROSSCHECK_SHA256 = "%s"$' % hashlib.sha256(xc_text.encode()).hexdigest(), scripts["assemble.py"], re.M):
        P.append("assemble.py does not pin crosscheck.json's sha256")
    for const in ("EXTRACT_RESULT_BLOB", "MAIN_COMMIT"):
        vals = {n_: re.findall(r'^%s = "([0-9a-f]{40})"$' % const, scripts[n_], re.M) for n_ in ("assemble.py", "collect.py")}
        if any(len(v) != 1 for v in vals.values()) or vals["assemble.py"] != vals["collect.py"]:
            P.append("collect.py's %s is not assemble.py's" % const)
    mc = re.findall(r'^MAIN_COMMIT = "([0-9a-f]{40})"$', scripts["assemble.py"], re.M)
    refs = re.findall(r"^\s+ref: (\S+)$", wf, re.M)
    if not mc or len(refs) != 2 or any(r_ != mc[0] for r_ in refs):
        P.append("workflow: the extract_result.py checkouts are not at assemble.py's MAIN_COMMIT")
    steps = re.split(r"^\s+- name:", wf, flags=re.M)[1:]
    main_src = [st for st in steps if re.search(r"^\s+path: main-src$", st, re.M)]
    if len(main_src) != 2 or any(re.findall(r"^\s+ref: (\S+)$", st, re.M) != mc[:1] for st in main_src) \
            or any("ref:" in st and st not in main_src for st in steps):
        P.append("workflow: a ref is not on exactly the two main-src checkouts, or they are not at MAIN_COMMIT")
    for const, name in (("ASSEMBLER_BLOB", "assemble.py"), ("HOST_BLOB", "host.py")):
        blob = hashlib.sha1(b"blob %d\0" % len(scripts[name].encode()) + scripts[name].encode()).hexdigest()
        if not re.search(r'^%s = "%s"$' % (const, blob), scripts["collect.py"], re.M):
            P.append("collect.py's %s is not %s's blob %s" % (const, name, blob[:12]))
    m = re.findall(r"^\s+shard: \[([0-9, ]+)\]$", wf, re.M)
    if len(m) != 1 or [int(x) for x in m[0].split(",")] != list(range(1, doc["shards"] + 1)):
        P.append("workflow: the matrix does not list exactly shards 1..%d" % doc["shards"])
    on = re.search(r"^on:\n((?:  .*\n)+)", wf, re.M)
    if not on or on.group(1) != "  push:\n    branches: ['%s']\n" % BRANCH:
        P.append("workflow: the trigger is not a push to %s alone" % BRANCH)
    if wf.count("if: github.ref == 'refs/heads/%s'" % BRANCH) != 2:
        P.append("workflow: a job lacks the branch guard")
    perm = re.search(r"^permissions:\n((?:  .*\n)+)", wf, re.M)
    if not perm or perm.group(1) != "  actions: read\n  contents: read\n" or wf.count("permissions:") != 1:
        P.append("workflow: permissions are not exactly actions: read and contents: read")
    uses = re.findall(r"^\s+(?:- )?uses: (\S+)", wf, re.M)
    if not uses or any(not re.fullmatch(r"actions/checkout@[0-9a-f]{40}", u) for u in uses):
        P.append("workflow: an action is not actions/checkout pinned by a full SHA")
    if wf.count("persist-credentials: false") != len(uses):
        P.append("workflow: a checkout does not set persist-credentials: false")
    if wf.count("GH_TOKEN") != 1 or wf.count("${{ github.token }}") != 1 or "secrets." in wf:
        P.append("workflow: GH_TOKEN is not set exactly once from github.token, or a secret is named")
    tok = wf.find("GH_TOKEN: ${{ github.token }}")
    step = wf.rfind("- name:", 0, tok)
    if tok < 0 or "batchx/host.py" not in wf[step:wf.find("- name:", tok)]:
        P.append("workflow: GH_TOKEN is not on the host step")
    for bad in ("upload-artifact", "actions/cache", "GITHUB_STEP_SUMMARY", "GITHUB_OUTPUT", "GITHUB_ENV", "git push",
                "workflow_dispatch", "pull_request", "schedule:", "contents: write", "actions: write"):
        if bad in wf:
            P.append("workflow: names %s" % bad)
    jobs = re.split(r"^  (?=[a-z]+:\n    name:)", wf.split("\njobs:\n", 1)[1], flags=re.M)
    jobs = [j for j in jobs if j.strip()]
    for j in jobs:
        if "\n    timeout-minutes:" not in j:
            P.append("workflow: a job has no timeout-minutes")
        for st in re.split(r"^      - name:", j, flags=re.M)[1:]:
            if "timeout-minutes:" not in st:
                P.append("workflow: step %r has no timeout-minutes" % st.split("\n", 1)[0].strip()[:50])
    return P


def plan(path):
    fails = 0
    wf = open(path, encoding="utf-8").read()
    runs_text = open(os.path.join(HERE, "runs.json"), encoding="utf-8").read()
    xc_text = open(os.path.join(HERE, "crosscheck.json"), encoding="utf-8").read()
    scripts = {n: open(os.path.join(HERE, n), encoding="utf-8").read() for n in ("assemble.py", "host.py", "collect.py")}
    p = plan_problems(wf, runs_text, scripts, xc_text)
    print("  %s  the plan and pins hold%s" % ("ok  " if not p else "FAIL", "" if not p else ": " + "; ".join(p)))
    fails += bool(p)
    negs = [
        ("a shard dropped from the matrix", lambda w: w.replace(", 32]", "]")),
        ("a second trigger", lambda w: w.replace("on:\n  push:", "on:\n  workflow_dispatch:\n  push:")),
        ("a write permission", lambda w: w.replace("  contents: read\n", "  contents: write\n")),
        ("an action pinned by tag", lambda w: w.replace("actions/checkout@11d5960a326750d5838078e36cf38b85af677262", "actions/checkout@v4", 1)),
        ("a checkout keeping credentials", lambda w: w.replace("          persist-credentials: false", "          persist-credentials: true", 1)),
        ("the token on the assemble step", lambda w: w.replace("        if: ${{ !cancelled() }}\n        timeout-minutes: 8\n",
                                                             "        if: ${{ !cancelled() }}\n        timeout-minutes: 8\n"
                                                             "        env:\n          GH_TOKEN: ${{ github.token }}\n")),
        ("an artifact upload", lambda w: w + "      - name: up\n        timeout-minutes: 1\n        uses: actions/upload-artifact@"
                                         + "0" * 40 + "\n"),
        ("a step without a timeout", lambda w: w.replace("        timeout-minutes: 8\n", "", 1)),
        ("a job without a timeout", lambda w: w.replace("    timeout-minutes: 25\n", "", 1)),
        ("a job without the branch guard", lambda w: w.replace("    if: github.ref == 'refs/heads/%s'\n" % BRANCH, "", 1)),
    ]
    for name, edit in negs:
        w2 = edit(wf)
        caught = w2 != wf and bool(plan_problems(w2, runs_text, scripts, xc_text))
        print("  %s  plan negative control: %s is caught" % ("ok  " if caught else "FAIL", name))
        fails += not caught
    s2 = dict(scripts, **{"collect.py": scripts["collect.py"].replace("RUNS_SHA256 = \"", "RUNS_SHA256 = \"0", 1)})
    caught = bool(plan_problems(wf, runs_text, s2, xc_text))
    print("  %s  plan negative control: a script pinning another runs.json is caught" % ("ok  " if caught else "FAIL"))
    fails += not caught
    for const in ("EXTRACT_RESULT_BLOB", "MAIN_COMMIT"):
        s4 = dict(scripts, **{"collect.py": re.sub(r'^(%s = ")([0-9a-f])' % const,
                                                   lambda m: m.group(1) + ("1" if m.group(2) == "0" else "0"),
                                                   scripts["collect.py"], count=1, flags=re.M)})
        caught = s4 != scripts and bool(plan_problems(wf, runs_text, s4, xc_text))
        print("  %s  plan negative control: a collect.py %s other than assemble.py's is caught" % ("ok  " if caught else "FAIL", const))
        fails += not caught
    MC = "b96662e6be4f537502c772db369ea32a35b213a8"
    w6 = wf.replace("          ref: %s\n" % MC, "", 1)
    w6 = w6.replace("        with:\n          persist-credentials: false\n",
                    "        with:\n          ref: %s\n          persist-credentials: false\n" % MC, 1)
    caught = w6 != wf and w6.count("ref: %s" % MC) == 2 and bool(plan_problems(w6, runs_text, scripts, xc_text))
    print("  %s  plan negative control: the ref moved from a main-src checkout onto a batchx checkout is caught"
          % ("ok  " if caught else "FAIL"))
    fails += not caught
    w5 = wf.replace("ref: b96662e6be4f537502c772db369ea32a35b213a8", "ref: " + "0" * 40, 1)
    caught = w5 != wf and bool(plan_problems(w5, runs_text, scripts, xc_text))
    print("  %s  plan negative control: an extract_result.py checkout at another commit is caught" % ("ok  " if caught else "FAIL"))
    fails += not caught
    s3 = dict(scripts, **{"assemble.py": scripts["assemble.py"] + "\n"})
    caught = bool(plan_problems(wf, runs_text, s3, xc_text))
    print("  %s  plan negative control: an assemble.py other than the one collect.py pins is caught" % ("ok  " if caught else "FAIL"))
    fails += not caught
    r2 = json.loads(runs_text)
    r2["runs"] = r2["runs"][1:]
    caught = bool(plan_problems(wf, json.dumps(r2, indent=1, sort_keys=True) + "\n", scripts, xc_text))
    print("  %s  plan negative control: a run dropped from runs.json is caught" % ("ok  " if caught else "FAIL"))
    fails += not caught
    return fails


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--extractor", required=True)
    ap.add_argument("--plan", help="the workflow file, for part 3")
    ap.add_argument("--work")
    a = ap.parse_args(argv)
    extractor = os.path.abspath(a.extractor)
    work = tempfile.mkdtemp(prefix="controls-", dir=a.work)
    fails = 0
    try:
        print("controls (local, no network):")
        if a.plan:
            fails += plan(a.plan)
        fails += end_to_end(extractor, work)
        base = os.path.join(work, "pristine")
        os.makedirs(base)
        for f in FILES:
            shutil.copy(os.path.join(HERE, f), base)
        rc = selftests(base, extractor, work)
        ok = rc == [0, 0, 0]
        print("  %s  the unmutated copy's three self-tests pass (exit codes %s)" % ("ok  " if ok else "FAIL", rc))
        fails += not ok
        fails += phase_selfcheck()
        fails += tally_selfcheck(work)
        results = mutant_phase(MUTANTS, lambda i, entry: run_mutant(i, entry, base, extractor, work),
                               lambda i, when: free_bytes(work), DISK_FLOOR, WORKERS)
        killed, infra, table = 0, 0, []
        for r in results:   # in MUTANTS order, whatever order the workers finished in
            for l in r["lines"]:
                print(l)
            killed += r["killed"]
            infra += r["infra"]
            fails += not r["killed"]
            if r["row"] is not None:
                table.append(r["row"])
        if infra:
            print("controls: %d mutant(s) not judged: INFRASTRUCTURE (free space under the %d MiB floor); neither a kill "
                  "nor a survival, and the run fails" % (infra, DISK_FLOOR >> 20))
        print("controls: %d of %d mutants killed" % (killed, len(MUTANTS)))
        print("mutant -> the tests it fails (each expected regression test must be among them):")
        for i, what, expect, names in table:
            print("  TABLE %02d | %s | expected %s | failing (%d): %s" % (i, what, expect, len(names), "; ".join(names)))
    finally:
        shutil.rmtree(work, ignore_errors=True)
    print("controls: %s" % ("OK" if not fails else "%d failure(s)" % fails))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
