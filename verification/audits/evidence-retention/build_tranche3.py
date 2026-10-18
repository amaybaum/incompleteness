#!/usr/bin/env python3
"""build_tranche3.py -- how tranche 3 of the evidence-retention archive was cut (AGENTS §A.42).

Tranche 3 retains CI runs that frozen records cite and that tranches 1 and 2 do not cover, earliest log expiry
first. For each run it writes, under runs/<run_id>/:
  run.json       the run's identity and outcome, selected fields of the runs API's answer;
  jobs.json      every job of the run, with its steps and their conclusions, from the jobs API's answer;
  expected.json  where a citing claim rests on what a job printed: that output, extracted by job_outputs.py from
                 the served job log, with the commit it holds at and the recipe that regenerates it.
and it adds to manifest.json one entry per run (id run-<run_id>), with every citing location and the claims made
there, and the tranche3 section: the cited set, the cut, and every uncovered run left for a later tranche with
its creation date and log expiry.

It cannot be re-run from the tree: its inputs, the saved API answers and served logs, are not retained (raw logs
are withheld by AGENTS §A.42 item 1 and the owner's decision of 2026-10-17); their digests are. Inputs:
  INPUTS/api-runs/<id>.json, INPUTS/api-jobs/<id>.json   the API answers, as received;
  INPUTS/served/served-<job_id>.txt                       the served job-log text;
  INPUTS/served-meta.json                                 per job: original_length and served line count;
  INPUTS/priority-388.csv                                 the accepted ranking of the uncovered runs.
Usage: build_tranche3.py INPUTS ARCHIVE
"""
import csv
import datetime
import hashlib
import json
import os
import sys

INP, ARCH = sys.argv[1], sys.argv[2]
ROOT = os.path.abspath(os.path.join(ARCH, '..', '..', '..'))
sys.path.insert(0, ARCH)
import job_outputs  # noqa: E402  (the archive's own extractor)

BASE = 'b96662e6be4f537502c772db369ea32a35b213a8'
SOURCE_LOG = 'GitHub Actions job log, read on 2026-10-17 through the session\'s job-log tool, which returns at most the last 5000 lines, or the last tail_lines lines when fewer were asked for'
EXTRACTOR = 'verification/audits/evidence-retention/job_outputs.py'

SI2 = 'verification/infrastructure/round-si-2-authority-cutover/'
SI3 = 'verification/infrastructure/round-si-3-legacy-seal-retirement/'
TB = 'verification/programmes/oi-qm/track-b/'
A21, A22, A23 = TB + 'act-21-orbit-law-rigidity-twisted/', TB + 'act-22-orbit-law-naturality-factorization/', TB + 'act-23-orbit-law-gaps/'
A24, A25 = TB + 'act-24-orbit-geometry-selector/', TB + 'act-25-orbit-geometry-isometries/'
LEGACY = ('a measurement of the guard file\'s text, not an output of the run; no retained file carries it, and it is '
          'reproducible from the tree at that commit')


def guard_out(job, commit, quoted=()):
    return {'job': job, 'kind': 'guard', 'step': 'Probes', 'at': {'commit': commit}, 'quoted': list(quoted),
            'recipe': {'cwd': 'verification/lean', 'argv': ['python3', 'edge_rigidity_probe.py'],
                       'env': {'GITHUB_EVENT_NAME': 'push'}, 'exit': 0,
                       'requires': 'numpy and scipy, which the probes job installs with pip'}}


def bc_push(job, commit):
    return {'job': job, 'kind': 'base-check', 'step': 'Preconditions at B (merge commit on main)', 'at': {'commit': commit},
            'recipe': {'cwd': '.', 'argv': ['python3', 'tools/control_plane_base_check.py', '--mode', 'B', '--ref', commit],
                       'env': {}, 'exit': 0, 'requires': 'a full-history clone: ancestry rows read it'}}


def bc_pr(job, base, head, merge):
    return {'job': job, 'kind': 'base-check', 'step': 'Preconditions at M (candidate merge)',
            'at': {'base': base, 'head': head, 'synthetic_merge': merge},
            'recipe': {'cwd': '.', 'argv': ['python3', 'tools/control_plane_base_check.py', '--mode', 'M', '--ref', 'HEAD'],
                       'env': {}, 'exit': 0, 'requires': 'a full-history clone: ancestry rows read it; HEAD is the '
                       'merge of head into base, rebuilt with git merge --no-ff (GitHub\'s merge commit is not retained, '
                       'and the rebuilt one has another id, so REF is not compared)'}}


R, J, X = 'run', 'jobs', 'expected'
OGS = ('    R7-OGS authority: U3 keyed on OGS.json -> PASS (ARCHIVED; pinned == derived 995ad859d0dc; second parent is the '
       'sealed head; ancestry and reachability hold); legacy shadow -> no verdict, gating nothing')

# run id -> (outputs, citations); a citation is (path, line, [(claim line, text, status, files, note)])
RUNS = {
    '35317349625': ([], [
        (SI2 + 'preregistration.md', 12, [
            (11, '`66eea646fcbf242df89b168bcce3336ff1b77802`', 'retained', [R], 'run.json head_sha 66eea646…'),
            (12, 'certified by push run 35317349625', 'retained', [R, J], 'run.json: event push, conclusion success; jobs.json: three jobs, each success')])]),
    '35321848352': ([], [
        (SI2 + 'amendments/amendment-1.md', 13, [
            (12, '`da9d69d60b19482abfeb27b16af5aaebebba0e83`, certified by', 'retained', [R], 'run.json head_sha da9d69d6…'),
            (13, 'push run 35321848352', 'retained', [R, J], 'run.json: event push, conclusion success; jobs.json: three jobs, each success')]),
        (SI2 + 'amendments/amendment-2.md', 13, [
            (13, '`da9d69d60b19482abfeb27b16af5aaebebba0e83`, certified by push run 35321848352', 'retained', [R, J],
             'run.json: head_sha da9d69d6…, event push, conclusion success; jobs.json: three jobs, each success')])]),
    '35340667434': ([], [
        (SI2 + 'amendments/amendment-2.md', 16, [
            (16, '`9ca82958cfaa3ff926d8a80baf2ee22eb468a917`, certified by push run 35340667434', 'retained', [R, J],
             'run.json: head_sha 9ca82958…, event push, conclusion success; jobs.json: three jobs, each success')])]),
    '35351379664': ([], [
        (SI2 + 'result.md', 4, [
            (3, '`df54b99dba99dc043b11752163d8d348c9e54472`, the certified', 'retained', [R, J],
             'run.json: head_sha df54b99d…, conclusion success; jobs.json: three jobs, each success'),
            (4, 'push run 35351379664', 'retained', [R], 'run.json: event push')])]),
    '35371369465': ([guard_out(105685869149, 'd89fff8abb20e2c63a33949b79947650bf47df6a')], [
        (SI3 + 'preregistration.md', 14, [
            (11, '`d89fff8abb20e2c63a33949b79947650bf47df6a`', 'retained', [R],
             'run.json head_sha d89fff8a…, the commit `B0`; the line names its second parent `E` (df2fab57…)'),
            (13, 'certified as the state of `main` by push run', 'retained', [R, J],
             'run.json: event push, conclusion success, at `B0`; jobs.json: three jobs, each success')]),
        (SI3 + 'preregistration.md', 472, [
            (471, '92 tags, all `PASS`', 'retained', [X],
             'expected.json: the guard\'s 92 check lines (R1 to R9 and 83 `R7-*` tags), every one PASS, verdict ALL CHECKS PASS'),
            (471, '`R7-SI1` and `R7-SI2` included', 'retained', [X], 'expected.json: R7-SI1 and R7-SI2 are among the checks, both PASS'),
            (472, 'push run 35371369465', 'retained', [R], 'run.json: event push, at `B0`'),
            (472, 'a local run at `L`', 'not retained', [], 'a local run, not a CI run: no output of it is held')])]),
    '35377254073': ([], [
        (SI3 + 'amendments/amendment-1.md', 14, [
            (14, '`220827b89c038d98dbe643a53c72a8fd00ed8480`, certified by push run 35377254073', 'retained', [R, J],
             'run.json: head_sha 220827b8…, event push, conclusion success; jobs.json: three jobs, each success')])]),
    '35407019610': ([], [
        (SI3 + 'result.md', 4, [
            (3, '`b0ee87bae34c6f8dcd3a4a75d958bb4e8a1cbca5`, the certified', 'retained', [R, J],
             'run.json: head_sha b0ee87ba…, conclusion success; jobs.json: three jobs, each success'),
            (4, 'push run 35407019610', 'retained', [R], 'run.json: event push')])]),
    '35412319426': ([guard_out(105814214367, '63d8ca08cbea2e05e4f9fdc5a9b36006b9f104ed')], [
        (A21 + 'amendments/amendment-1.md', 22, [
            (21, '`63d8ca08cbea2e05e4f9fdc5a9b36006b9f104ed`', 'retained', [R], 'run.json head_sha 63d8ca08…'),
            (22, 'certified by main-push run 35412319426', 'retained', [R, J],
             'run.json: event push, conclusion success; jobs.json: three jobs, each success')]),
        (A21 + 'preregistration.md', 85, [
            (84, '`63d8ca08cbea2e05e4f9fdc5a9b36006b9f104ed`', 'retained', [R], 'run.json head_sha 63d8ca08…'),
            (85, 'certified by main-push run 35412319426', 'retained', [R, J],
             'run.json: event push, conclusion success; jobs.json: three jobs, each success')]),
        (A21 + 'preregistration.md', 2337, [
            (2337, 'prints eighty-four `R7-*` tags, all `PASS`, on main-push run 35412319426', 'retained', [X, R],
             'expected.json: 84 `R7-*` check lines among 93, every one PASS; the run is at 63d8ca08…, the snapshot the freeze was measured at'),
            (2337, '`_SI2_LEGACY_RE` finds zero assignment statements in it', 'not retained', [], LEGACY)])]),
    '35418734887': ([], [
        (A21 + 'amendments/amendment-1.md', 20, [
            (18, '`aeb0b91d20b4e307c293c06afda9db64fe2a3b09`', 'retained', [R], 'run.json head_sha aeb0b91d…'),
            (19, 'certified by main-push run', 'retained', [R], 'run.json: event push, conclusion success'),
            (20, '35418734887 with all three jobs green', 'retained', [J], 'jobs.json: three jobs, each success')])]),
    '35419924625': ([guard_out(105835534407, '10d1041bcc10f25d9f643629d4431acbd0f65a1e')], [
        (A21 + 'result.md', 921, [
            (921, 'it prints eighty-four `R7-*` tags, all `PASS`, on `B`\'s own main-push run 35419924625', 'retained', [X, R],
             'expected.json: 84 `R7-*` check lines among 93, every one PASS; run.json: event push at 10d1041b…'),
            (921, '`_SI2_LEGACY_RE` finds zero assignment statements', 'not retained', [], LEGACY)])]),
    '35433619877': ([guard_out(105872461384, 'd08b932da492891bdadaa5b867fd337250859b99')], [
        (A22 + 'preregistration.md', 26, [
            (25, '`d08b932da492891bdadaa5b867fd337250859b99`', 'retained', [R], 'run.json head_sha d08b932d…'),
            (26, 'whose main-push run 35433619877 is fully green', 'retained', [R, J],
             'run.json: event push, conclusion success; jobs.json: four jobs, each success'),
            (27, 'the control-plane base check in mode `B`', 'retained', [J],
             'jobs.json: the Control-plane base check job ran its step at B, which succeeded, and skipped its step at M')]),
        (A22 + 'preregistration.md', 1206, [
            (1206, 'eighty-five `R7-*` tags, all `PASS`, on main-push run 35433619877', 'retained', [X, R],
             'expected.json: 85 `R7-*` check lines among 94, every one PASS'),
            (1206, '`_SI2_LEGACY_RE` finds zero assignment statements', 'not retained', [], LEGACY)]),
        (A22 + 'result.md', 519, [
            (519, 'eighty-five tags on run 35433619877', 'retained', [X], 'expected.json: 85 `R7-*` check lines, every one PASS'),
            (519, 'zero legacy statements', 'not retained', [], LEGACY)])]),
    '35436171509': ([bc_pr(105879086578, 'd08b932da492891bdadaa5b867fd337250859b99', 'c6d94dda513b7918bcaff0e79abc51e2ff81f093',
                           '28ed5c98f0c7934d334933036891a070a7069bbc')], [
        (A22 + 'result.md', 48, [
            (48, 'the base check verified at `M` (run 35436171509)', 'retained', [X, R],
             'expected.json: the base check in mode M, its 16 rows and 9 frozen-blob lines PASS; run.json: event pull_request')]),
        (A22 + 'result.md', 512, [
            (512, '`OK (mode M, 16 row(s), no failure)`', 'retained', [X], 'expected.json summary line'),
            (512, 'at the candidate merge `28ed5c98…` on run 35436171509', 'retained', [X],
             'expected.json: REF 28ed5c98…, the merge of c6d94dda… into d08b932d…, as the run\'s checkout reports')])]),
    '35436608551': ([bc_push(105880234823, 'ccd5704fd157348903cbdea746d24cf5d5498b78')], [
        (A22 + 'result.md', 6, [
            (4, '`ccd5704fd157348903cbdea746d24cf5d5498b78`', 'retained', [R], 'run.json head_sha ccd5704f…'),
            (6, 'by main-push run 35436608551 with all four jobs green', 'retained', [R, J],
             'run.json: event push, conclusion success; jobs.json: four jobs, each success'),
            (6, 'the control-plane base check in mode `B`', 'retained', [X, J], 'expected.json: the base check in mode B'),
            (7, 'reporting sixteen rows and no failure', 'retained', [X], 'expected.json summary: OK (mode B, 16 row(s), no failure)')]),
        (A22 + 'result.md', 49, [
            (48, 'and at `B` (run', 'retained', [X], 'expected.json: the base check in mode B at ccd5704f…, every line PASS')]),
        (A22 + 'result.md', 513, [
            (513, '`OK (mode B, 16 row(s), no failure)` at `B` on run 35436608551', 'retained', [X, R], 'expected.json summary line')])]),
    '35441377788': ([guard_out(105892625482, '59c1b7efe36d7768cf53120997ff201e32c8e458')], [
        (A23 + 'preregistration.md', 28, [
            (27, '`59c1b7efe36d7768cf53120997ff201e32c8e458`', 'retained', [R], 'run.json head_sha 59c1b7ef…'),
            (28, 'whose main-push run 35441377788 is fully green', 'retained', [R, J],
             'run.json: event push, conclusion success; jobs.json: four jobs, each success'),
            (29, 'control-plane base check in mode `B`', 'retained', [J],
             'jobs.json: the Control-plane base check job ran its step at B, which succeeded, and skipped its step at M')]),
        (A23 + 'preregistration.md', 1493, [
            (1493, 'eighty-six `R7-*` tags, all `PASS`, on main-push run 35441377788', 'retained', [X, R],
             'expected.json: 86 `R7-*` check lines among 95, every one PASS'),
            (1493, '`_SI2_LEGACY_RE` finds zero assignment statements', 'not retained', [], LEGACY)]),
        (A23 + 'result.md', 773, [
            (773, 'eighty-six tags on run 35441377788', 'retained', [X], 'expected.json: 86 `R7-*` check lines, every one PASS'),
            (773, 'zero legacy statements', 'not retained', [], LEGACY)])]),
    '35445184572': ([bc_pr(105902791118, '59c1b7efe36d7768cf53120997ff201e32c8e458', 'feaa0891170b2e17baed8e2c8abb76f554499f85',
                           '370fb34dc05f770603a33743aa3d5dd098d218e0')], [
        (A23 + 'result.md', 71, [
            (71, 'the base check verified at `M` (run 35445184572, at the candidate', 'retained', [X, R],
             'expected.json: the base check in mode M, its 20 rows and 13 frozen-blob lines PASS; run.json: event pull_request'),
            (72, 'merge of pull request #686)', 'retained', [X],
             'expected.json: REF 370fb34d…, pull/686/merge, the merge of feaa0891… into 59c1b7ef…, as the run\'s checkout reports')]),
        (A23 + 'result.md', 767, [
            (766, '`OK (mode M, 20 row(s), no failure)` at the candidate merge of pull request #686 on run', 'retained', [X],
             'expected.json summary line; REF is pull/686/merge'),
            (767, '35445184572 and', 'retained', [R], 'run.json id')])]),
    '35445878205': ([bc_push(105904588663, '64214bfb0ae41b9f0a4fb11159089fff32d4dd85')], [
        (A23 + 'result.md', 6, [
            (4, '`64214bfb0ae41b9f0a4fb11159089fff32d4dd85`', 'retained', [R], 'run.json head_sha 64214bfb…'),
            (6, 'by main-push run 35445878205 with all four jobs green', 'retained', [R, J],
             'run.json: event push, conclusion success; jobs.json: four jobs, each success'),
            (6, 'the control-plane base check in mode `B`', 'retained', [X, J], 'expected.json: the base check in mode B'),
            (7, 'reporting twenty rows and no failure', 'retained', [X], 'expected.json summary: OK (mode B, 20 row(s), no failure)')]),
        (A23 + 'result.md', 72, [
            (72, 'and at `B` (run 35445878205)', 'retained', [X, R], 'expected.json: the base check in mode B at 64214bfb…, every line PASS or SKIP')]),
        (A23 + 'result.md', 767, [
            (767, '`OK (mode B, 20 row(s), no failure)` at `B` on run 35445878205', 'retained', [X, R], 'expected.json summary line')])]),
    '35451692651': ([guard_out(105919852549, '9907d3acefb2bd5e2cc66c007400cc0e194d36ec')], [
        (A24 + 'preregistration.md', 28, [
            (27, '`9907d3acefb2bd5e2cc66c007400cc0e194d36ec`', 'retained', [R], 'run.json head_sha 9907d3ac…'),
            (28, 'whose main-push run 35451692651 is fully green', 'retained', [R, J],
             'run.json: event push, conclusion success; jobs.json: four jobs, each success'),
            (29, 'control-plane base check in mode `B`', 'retained', [J],
             'jobs.json: the Control-plane base check job ran its step at B, which succeeded, and skipped its step at M')]),
        (A24 + 'preregistration.md', 1780, [
            (1780, 'eighty-seven `R7-*` tags, all `PASS`, on main-push run 35451692651', 'retained', [X, R],
             'expected.json: 87 `R7-*` check lines among 96, every one PASS'),
            (1780, '`_SI2_LEGACY_RE` finds zero assignment statements', 'not retained', [], LEGACY)]),
        (A24 + 'result.md', 903, [
            (903, 'eighty-seven tags on run 35451692651', 'retained', [X], 'expected.json: 87 `R7-*` check lines, every one PASS'),
            (903, 'zero legacy statements', 'not retained', [], LEGACY)])]),
    '35457437686': ([bc_pr(105935118922, '9907d3acefb2bd5e2cc66c007400cc0e194d36ec', '98b567578098ff3bf6e3576d94302c7d3a2157b1',
                           'a1dcf0e9450b6b4b6d2bb972ceddcd6dca97fca3')], [
        (A24 + 'result.md', 71, [
            (71, 'the base check verified at `M` (run 35457437686, at the candidate merge of pull request #689)', 'retained', [X, R],
             'expected.json: the base check in mode M at pull/689/merge (REF a1dcf0e9…, the merge of 98b56757… into 9907d3ac…), '
             'its 25 rows and 23 frozen-blob lines PASS; run.json: event pull_request')]),
        (A24 + 'result.md', 897, [
            (896, '`OK (mode M, 25 row(s), no failure)` at the candidate merge of pull request', 'retained', [X], 'expected.json summary line'),
            (897, '#689 on run 35457437686', 'retained', [X, R], 'expected.json: REF is pull/689/merge')])]),
    '35458160449': ([bc_push(105937041519, 'd0fcdbc03c4b828d630f677253cf0914f451b63d')], [
        (A24 + 'result.md', 6, [
            (4, '`d0fcdbc03c4b828d630f677253cf0914f451b63d`', 'retained', [R], 'run.json head_sha d0fcdbc0…'),
            (6, 'by main-push run 35458160449 with all four jobs green', 'retained', [R, J],
             'run.json: event push, conclusion success; jobs.json: four jobs, each success'),
            (6, 'the control-plane base check in mode `B`', 'retained', [X, J], 'expected.json: the base check in mode B'),
            (7, 'reporting twenty-five rows and no failure', 'retained', [X], 'expected.json summary: OK (mode B, 25 row(s), no failure)')]),
        (A24 + 'result.md', 72, [
            (72, 'and at `B` (run 35458160449)', 'retained', [X, R], 'expected.json: the base check in mode B at d0fcdbc0…, every line PASS or SKIP')]),
        (A24 + 'result.md', 897, [
            (897, '`OK (mode B, 25 row(s), no failure)` at `B` on run 35458160449', 'retained', [X, R], 'expected.json summary line')])]),
    '35467053564': ([guard_out(105961211018, '17272da24e8d65a8d0e2417c6a451a1af3461258', [OGS])], [
        (A25 + 'preregistration.md', 33, [
            (32, '`17272da24e8d65a8d0e2417c6a451a1af3461258`', 'retained', [R], 'run.json head_sha 17272da2…'),
            (33, 'whose main-push run 35467053564 is fully green with `R7-OGS` in', 'retained', [R, J, X],
             'run.json: event push, conclusion success; jobs.json: four jobs, each success; expected.json: R7-OGS PASS'),
            (34, '`ARCHIVED` state', 'retained', [X], 'expected.json quotes the guard\'s line "R7-OGS authority: … PASS (ARCHIVED; …)"'),
            (34, 'the control-plane base check in mode `B`', 'retained', [J],
             'jobs.json: the Control-plane base check job ran its step at B, which succeeded, and skipped its step at M')]),
        (A25 + 'preregistration.md', 1871, [
            (1871, 'eighty-eight `R7-*` tags, all `PASS`, on main-push run 35467053564', 'retained', [X, R],
             'expected.json: 88 `R7-*` check lines among 97, every one PASS'),
            (1871, '`_SI2_LEGACY_RE` finds zero assignment statements', 'not retained', [], LEGACY)]),
        (A25 + 'result.md', 811, [
            (811, 'eighty-eight tags on run 35467053564', 'retained', [X], 'expected.json: 88 `R7-*` check lines, every one PASS'),
            (811, 'zero legacy statements', 'not retained', [], LEGACY)])]),
    '35470058510': ([bc_pr(105969253041, '17272da24e8d65a8d0e2417c6a451a1af3461258', 'a6cb0c41acbe790b2f566faa56c9149f3d5e107e',
                           'af1f20c3e1c637b591f42d158f7a63ac36a8416e')], [
        (A25 + 'result.md', 75, [
            (75, 'the base check verified at `M` (run 35470058510, at the candidate merge of pull request #691)', 'retained', [X, R],
             'expected.json: the base check in mode M at pull/691/merge (REF af1f20c3…, the merge of a6cb0c41… into 17272da2…), '
             'its 21 rows and 26 frozen-blob lines PASS; run.json: event pull_request')]),
        (A25 + 'result.md', 805, [
            (804, '`OK (mode M, 21 row(s), no failure)` at the candidate merge of pull request', 'retained', [X], 'expected.json summary line'),
            (805, '#691 on run 35470058510', 'retained', [X, R], 'expected.json: REF is pull/691/merge')])]),
    '35470951442': ([bc_push(105971697710, 'dd3bd2e726e0fb3bccd96df9c46a532119a9ee97')], [
        (A25 + 'result.md', 6, [
            (4, '`dd3bd2e726e0fb3bccd96df9c46a532119a9ee97`', 'retained', [R], 'run.json head_sha dd3bd2e7…'),
            (6, 'by main-push run 35470951442 with all four jobs green', 'retained', [R, J],
             'run.json: event push, conclusion success; jobs.json: four jobs, each success'),
            (6, 'the control-plane base check in mode `B`', 'retained', [X, J], 'expected.json: the base check in mode B'),
            (7, 'reporting twenty-one rows and no failure', 'retained', [X], 'expected.json summary: OK (mode B, 21 row(s), no failure)')]),
        (A25 + 'result.md', 76, [
            (76, 'and at `B` (run 35470951442)', 'retained', [X, R], 'expected.json: the base check in mode B at dd3bd2e7…, every line PASS or SKIP')]),
        (A25 + 'result.md', 805, [
            (805, '`OK (mode B, 21 row(s), no failure)` at `B` on run 35470951442', 'retained', [X, R], 'expected.json summary line')])]),
}

RUN_FIELDS = ('conclusion', 'created_at', 'display_title', 'event', 'head_branch', 'head_sha', 'id', 'path', 'run_attempt',
              'run_number', 'status', 'updated_at')
JOB_FIELDS = ('completed_at', 'conclusion', 'head_branch', 'head_sha', 'id', 'name', 'run_attempt', 'started_at', 'status',
              'workflow_name')


def sha(b):
    return hashlib.sha256(b).hexdigest()


def blob_id(b):
    return hashlib.sha1(b'blob %d\0' % len(b) + b).hexdigest()


def dump(obj):
    return (json.dumps(obj, indent=1, sort_keys=True) + '\n').encode('utf-8')


def expiry(created):
    return (datetime.datetime.strptime(created, '%Y-%m-%dT%H:%M:%SZ') + datetime.timedelta(days=90)).strftime('%Y-%m-%d')


meta = json.load(open(os.path.join(INP, 'served-meta.json')))
man_path = os.path.join(ARCH, 'manifest.json')
man = json.load(open(man_path, encoding='utf-8'))
man['entries'] = [e for e in man['entries'] if not str(e.get('id', '')).startswith('run-') and e.get('id') != 'tranche3-record']
man.pop('tranche3', None)
new = []
for rid, (outs, cites) in sorted(RUNS.items()):
    araw = open(os.path.join(INP, 'api-runs', rid + '.json'), 'rb').read()
    jraw = open(os.path.join(INP, 'api-jobs', rid + '.json'), 'rb').read()
    a, jl = json.loads(araw), json.loads(jraw)
    assert str(a['id']) == rid and jl['total_count'] == len(jl['jobs'])
    run = {k: a[k] for k in RUN_FIELDS}
    run.update({'run_id': rid, 'source': 'GitHub Actions runs API, GET runs/<run_id>, read 2026-10-17; selected fields'})
    jobs = {'run_id': rid, 'source': 'GitHub Actions jobs API, GET runs/<run_id>/jobs?filter=all, read 2026-10-17; selected fields',
            'jobs': [dict({k: j[k] for k in JOB_FIELDS},
                          steps=[{'number': s['number'], 'name': s['name'], 'conclusion': s['conclusion']} for s in j['steps']])
                     for j in sorted(jl['jobs'], key=lambda j: j['id'])]}
    d = os.path.join(ARCH, 'runs', rid)
    os.makedirs(d, exist_ok=True)
    files = []
    for name, obj, src in (('run.json', run, araw), ('jobs.json', jobs, jraw)):
        b = dump(obj)
        open(os.path.join(d, name), 'wb').write(b)
        files.append({'path': 'runs/%s/%s' % (rid, name), 'bytes': len(b), 'sha256': sha(b), 'kind': 'derived',
                      'source_sha256': sha(src)})
    if outs:
        exp_outs = []
        for o in outs:
            job = next(j for j in jl['jobs'] if j['id'] == o['job'])
            text = open(os.path.join(INP, 'served', 'served-%d.txt' % o['job']), 'rb').read()
            got = job_outputs.EXTRACT[o['kind']](text.decode('utf-8'))
            m = meta[str(o['job'])]
            if o['kind'] == 'base-check':
                assert got['summary'] and got['summary'].startswith('control_plane_base_check: OK'), rid
                expected = {'lines': got['lines'], 'summary': got['summary']}
                at = dict(o['at'])
                at['ref_as_served'] = got['ref']
                assert got['ref'] == (at.get('commit') or at.get('synthetic_merge')), (rid, got['ref'])
            else:
                assert got['verdict'] == 'edge_rigidity_probe: ALL CHECKS PASS', rid
                for q in o['quoted']:
                    assert q in got['text'], (rid, q)
                expected = {'checks': got['checks'], 'verdict': got['verdict'], 'quoted': o['quoted'],
                            'counts': {'checks': len(got['checks']), 'R7': sum(1 for c in got['checks'] if c['tag'].startswith('R7-')),
                                       'PASS': sum(1 for c in got['checks'] if c['status'] == 'PASS')}}
                at = dict(o['at'])
            if 'commit' in at:
                assert at['commit'] == a['head_sha'], rid
            else:
                assert at['head'] == a['head_sha'], rid
                served_text = text.decode('utf-8')
                assert ('HEAD is now at %s Merge %s into %s' % (at['synthetic_merge'][:8], at['head'], at['base'])) in served_text, rid
            exp_outs.append({'job_id': str(o['job']), 'job_name': job['name'], 'step': o['step'], 'kind': o['kind'], 'at': at,
                             'recipe': o['recipe'], 'expected': expected,
                             'source': {'kind': SOURCE_LOG, 'extractor': EXTRACTOR, 'original_lines': m['original_length'],
                                        'served_lines': m['served_lines'], 'served_sha256': sha(text),
                                        'note': 'the digest identifies the text this result was read from: it is provenance of '
                                                'the extraction, not independent proof of the result, which reproduction at the '
                                                'commit supplies; the text is not a byte copy of GitHub\'s log archive'}})
        doc = {'schema': 'oi-evidence-job-outputs', 'version': 1,
               'run': {'id': rid, 'head_sha': a['head_sha'], 'event': a['event'], 'attempt': a['run_attempt'], 'workflow': 'verify.yml'},
               'outputs': exp_outs,
               'reproduce': {'tool': 'python3 -I verification/audits/evidence-retention/job_outputs.py reproduce --run %s --work <dir>' % rid,
                             'manual': ['from the root of a full-history clone at a commit that carries this archive; <dir> is a new directory',
                                        'git worktree add --detach <dir> <at.commit, or at.base>',
                                        'for a pull-request run: (cd <dir> && git merge --no-ff --no-edit <at.head>)',
                                        '(cd <dir>/<recipe.cwd> && env <recipe.env> <recipe.argv>) > <log>',
                                        'python3 -I verification/audits/evidence-retention/job_outputs.py extract <kind> <log>, '
                                        'and compare it with expected as job_outputs.py compare() does'],
                             'compared': 'base check: every SKIP, PASS and FAIL line, the header with REF masked, and the summary; '
                                         'guard: every check\'s status, tag and message digest, the verdict, and the quoted lines; '
                                         'the exit code',
                             'not_compared': 'timestamps, durations, REF\'s id, the order of the guard\'s checks'}}
        b = dump(doc)
        open(os.path.join(d, 'expected.json'), 'wb').write(b)
        files.append({'path': 'runs/%s/expected.json' % rid, 'bytes': len(b), 'sha256': sha(b), 'kind': 'derived',
                      'source_sha256': [x['source']['served_sha256'] for x in exp_outs][0] if len(exp_outs) == 1 else None})
    fmap = {R: 'runs/%s/run.json' % rid, J: 'runs/%s/jobs.json' % rid, X: 'runs/%s/expected.json' % rid}
    citations = []
    for path, line, claims in cites:
        data = open(os.path.join(ROOT, path), 'rb').read()
        L = data.decode('utf-8').split('\n')
        assert rid in L[line - 1], (rid, path, line)
        cl = []
        for n, t, st, fs, note in claims:
            assert t in L[n - 1], (rid, path, n, t)
            k = {'line': n, 'text': t, 'status': st, 'note': note}
            if fs:
                k['in'] = [fmap[f] for f in fs]
                assert all(x in {f['path'] for f in files} for x in k['in']), (rid, k)
            cl.append(k)
        citations.append({'path': path, 'line': line, 'blob': blob_id(data), 'tokens': [rid], 'claims': cl})
    new.append({'id': 'run-' + rid, 'kind': 'derived', 'tranche': 3, 'run_id': rid, 'files': files, 'citations': citations,
                'expires': expiry(a['created_at'])})

# the remainder, earliest expiry first
rows = list(csv.DictReader(open(os.path.join(INP, 'priority-388.csv'))))
done = set(RUNS)
remaining = sorted(({'run_id': r['run_id'], 'created_at': r['created_at'], 'expires': expiry(r['created_at']),
                     'event': r['event'], 'conclusion': r['conclusion'], 'tier': r['tier']}
                    for r in rows if r['run_id'] not in done), key=lambda r: (r['created_at'], r['run_id']))
assert len(rows) == 388 and len(remaining) == 388 - len(done)
man['entries'] += new
man['tranche3'] = {
    'base': BASE,
    'cited_runs': 487,
    'covered_before': 99,
    'uncovered': 388,
    'retained': len(new),
    'cut': 'earliest log expiry first: the runs whose 90-day expiry falls on 2026-12-17 or 2026-12-18',
    'how_cited': 'every CI run id in main\'s tracked text at the base outside this archive: 11-digit run ids and 12-digit job ids '
                 'on lines that say run, job or actions/ (the audit\'s rule R), the same id shapes on other lines when they '
                 'name a run of the repository, and the inner runs of the one cited range (act 40, preregistration.md:744); '
                 'job ids count for their runs. It equals the 487 runs of the inventory accepted on 2026-10-17.',
    'expiry_rule': 'created_at plus 90 days, GitHub\'s default for a public repository; the repository\'s own setting was not readable',
    'remaining': remaining,
}
man['entries'].append({'id': 'tranche3-record', 'kind': 'complete', 'citations': [], 'files': [
    {'path': p, 'bytes': os.path.getsize(os.path.join(ARCH, p)), 'sha256': sha(open(os.path.join(ARCH, p), 'rb').read()), 'kind': 'complete'}
    for p in ('job_outputs.py', 'build_tranche3.py')],
    'provenance': {'source': 'written for this archive: tranche 3\'s extractor, reproduction tool and comparator, and the script '
                             'that cut the tranche'}})
open(man_path, 'w', encoding='utf-8').write(json.dumps(man, indent=1, sort_keys=True, ensure_ascii=False) + '\n')
print('tranche 3: %d run entries, %d citing locations, %d claims; %d runs remaining, earliest %s'
      % (len(new), sum(len(e['citations']) for e in new), sum(len(c['claims']) for e in new for c in e['citations']),
         len(remaining), remaining[0]['expires']))
