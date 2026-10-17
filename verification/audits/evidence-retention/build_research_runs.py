#!/usr/bin/env python3
"""build_research_runs.py -- how the archive's research-build entries were cut (AGENTS §A.42).

By the owner's instruction of 2026-10-17 the archive retains, ahead of their citing record, the two research
builds that PRESERVE-INDUCT-1's control-plane draft (#831) cites: runs 38450187534 and 38454439833 of
.github/workflows/preservation-induction-design.yml, job design-build, at source commits e684897d and febfe5e2 on
research/preservation-induction-design-20261013. For each it writes ci/<run>/run.json, jobs.json and results.json,
the last read from the served job log by main's extract_result.py (blob 05c41bce), unchanged, and adds one entry
research-<run> to manifest.json, with a named gap for every item the result needs and the extraction does not
carry. The results establish what those runs logged at those sources, nothing about later trees.

It cannot be re-run from the tree: its inputs (the API answers and the served logs) are not retained, as raw logs
are withheld by §A.42 item 1; their digests are. Inputs: INPUTS/run-<id>.json, INPUTS/jobs-<id>.json,
INPUTS/served-<job>.txt and INPUTS/served-meta.json (original_length per job).
Usage: build_research_runs.py INPUTS ARCHIVE REPO
"""
import hashlib
import json
import os
import re
import subprocess
import sys

INP, ARCH, REPO = sys.argv[1:4]
sys.path.insert(0, ARCH)
from extract_result import extract  # noqa: E402  (main's extractor, blob 05c41bce)

EXTRACTOR = 'verification/audits/evidence-retention/extract_result.py'
EXTRACTOR_BLOB = '05c41bce610b8d02ccbaca8e69377b771bef4a35'
PRINT = re.compile(r'^#print axioms\b')
PERMITTED = ['propext', 'Classical.choice', 'Quot.sound']
WORKFLOW = '.github/workflows/preservation-induction-design.yml'
BRANCH = 'research/preservation-induction-design-20261013'
HOLDER = '468e0f79cabb01c215a252721ee65a1ad1301a2f'
CITER = 'verification/programmes/oi-qm/reconstruction/round-preserve-induct-1/preregistration.md'
DESIGN = 'verification/programmes/oi-qm/reconstruction/preservation-induction-design/'
SCOPE = 'what this run logged at its source commit; nothing about any later tree'
RUNS = [
    # run, job, source, the build targets the workflow names there, the design files it compiles, citing line in #831
    ('38450187534', 115478781754, 'e684897da41b1c3d066b880194c9beb87a19b7ad', ['OIBridge/ImplementationLocality.lean'],
     ['PreservationInduction.lean'], 69),
    ('38454439833', 115493410133, 'febfe5e2668d3c000ec1d4ce7e4041f4feabd3c3',
     ['OIBridge/ImplementationLocality.lean', 'OIBridge/StructuralClosure.lean'],
     ['PreservationInduction.lean', 'ResearchInstances.lean'], 127),
]
RUN_FIELDS = ('conclusion', 'created_at', 'display_title', 'event', 'head_branch', 'head_sha', 'id', 'path', 'run_attempt',
              'run_number', 'status', 'updated_at')
JOB_FIELDS = ('completed_at', 'conclusion', 'head_branch', 'head_sha', 'id', 'name', 'run_attempt', 'started_at', 'status',
              'workflow_name')
BARE = re.compile(r"^'[^ ]+' (depends on axioms|does not depend on any axioms)")
TS = re.compile(r'^\ufeff?\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d\.\d+Z ')


def sha(b):
    return hashlib.sha256(b).hexdigest()


def dump(obj):
    return (json.dumps(obj, indent=1, sort_keys=True) + '\n').encode('utf-8')


def show(rev, path):
    p = subprocess.run(['git', '-C', REPO, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return p.stdout if p.returncode == 0 else None


def spans(nums):
    out = []
    for n in sorted(nums):
        if out and n == out[-1][1] + 1:
            out[-1][1] = n
        else:
            out.append([n, n])
    return out


assert sha(open(os.path.join(ARCH, 'extract_result.py'), 'rb').read()) and \
    hashlib.sha1(b'blob %d\0' % len(open(os.path.join(ARCH, 'extract_result.py'), 'rb').read()) +
                 open(os.path.join(ARCH, 'extract_result.py'), 'rb').read()).hexdigest() == EXTRACTOR_BLOB
meta = json.load(open(os.path.join(INP, 'served-meta.json')))
man_path = os.path.join(ARCH, 'manifest.json')
man = json.load(open(man_path, encoding='utf-8'))
ids = {'research-' + r[0] for r in RUNS} | {'research-runs-record'}
man['entries'] = [e for e in man['entries'] if e.get('id') not in ids]
man['missing'] = [g for g in man['missing'] if g.get('id') not in ids]
for rid, job, head, targets, design, cline in RUNS:
    araw = open(os.path.join(INP, 'run-%s.json' % rid), 'rb').read()
    jraw = open(os.path.join(INP, 'jobs-%s.json' % rid), 'rb').read()
    a, jl = json.loads(araw), json.loads(jraw)
    assert str(a['id']) == rid and a['head_sha'] == head and a['path'] == WORKFLOW and jl['total_count'] == len(jl['jobs'])
    jb = next(j for j in jl['jobs'] if j['id'] == job)
    text = open(os.path.join(INP, 'served-%d.txt' % job), 'rb').read()
    m = meta[str(job)]
    lines = text.decode('utf-8').split('\n')
    assert m['served_lines'] == len(lines) == m['original_length'], (rid, m)
    x = extract(text.decode('utf-8'))
    gaps, modules = [], {}
    for mod in targets:
        reps = x['reports'].get(mod, [])
        src = show(head, 'verification/lean-mathlib/' + mod)
        assert src is not None and not any(r.get('unclosed') for r in reps)
        prints = [i + 1 for i, l in enumerate(src.decode('utf-8').split('\n')) if PRINT.match(l)]
        got = {r['line'] for r in reps}
        assert got <= set(prints)
        lost = sorted(set(prints) - got)
        rec = {'reports': [{'line': r['line'], 'name': r['name'], 'axioms': r['axioms']} for r in reps],
               'status': 'complete' if not lost else 'partial' if got else 'none', 'prints': len(prints), 'print_lines': spans(prints)}
        if lost:
            rec['unreported_print_lines'] = spans(lost)
            src_lines = src.decode('utf-8').split('\n')
            primed = [n for n in lost if "'" in src_lines[n - 1].split('#print axioms', 1)[1]]
            served = [i + 1 for i, l in enumerate(lines) if any(TS.sub('', l).startswith('info: %s:%d:' % (mod, n)) for n in lost)]
            why = ('%d of the module\'s %d #print axioms lines have no extracted report. The log was served whole (%d lines); '
                   % (len(lost), len(prints), len(lines)))
            if len(primed) == len(lost) and len(served) == len(lost):
                why += ('each of the %d names a declaration ending in a prime, its report stands in the served text (served '
                        'lines %s), and extract_result.py\'s report pattern does not match a name that contains an apostrophe, '
                        'so the report is not extracted' % (len(lost), ', '.join(map(str, served))))
            else:
                why += 'the reports were not found in the served text'
            gaps.append({'what': 'axiom reports of %s' % mod, 'why': why})
        modules[mod] = rec
    assert x['build'] and x['build']['success'] and x['gate'] is None
    bare = [i + 1 for i, l in enumerate(lines) if BARE.match(TS.sub('', l))]
    gaps.append({'what': 'release gate', 'why': 'the workflow runs no release gate, and the served log holds no gate block; '
                 'its last step, Check retained records and artifact placement, runs legacy_records_check.py, '
                 'v3_verifier.py --receipts and artifact_placement_check.py, whose output extract_result.py does not read; '
                 'jobs.json records the step\'s conclusion'})
    gaps.append({'what': 'axiom reports of the research design (%s)' % ', '.join(design),
                 'why': '`lean` run on the design files prints its %d reports without the file:line prefix of a lake build '
                        '(served lines %d to %d); extract_result.py reads only prefixed reports, so none is extracted, and '
                        'they are not inferred here' % (len(bare), bare[0], bare[-1])})
    gaps.append({'what': 'exact-control replay output',
                 'why': 'the step Replay independent exact controls compares the design\'s two scripts with their saved '
                        'outputs and prints them; extract_result.py does not read that output; jobs.json records the step\'s '
                        'conclusion'})
    gaps.append({'what': 'source commit %s' % head,
                 'why': 'the commit is not reachable from main; on 2026-10-17 host branch %s held it (head %s). It is not '
                        'retained under objects/: its tree holds the non-empty captured outputs %sexact-output.txt (196 bytes) '
                        'and independent-output.txt (175 bytes), which the withholding policy withholds only once the owner '
                        'approves them, and check_objects.py\'s approved list does not name them' % (BRANCH, HOLDER[:12], DESIGN)})
    run = {'attempt': a['run_attempt'], 'conclusion': jb['conclusion'], 'event': a['event'], 'head_sha': head, 'id': rid,
           'job_id': str(job), 'job_name': jb['name'], 'workflow': os.path.basename(WORKFLOW)}
    res = {'schema': 'oi-evidence-result', 'version': 1, 'kind': 'research-build', 'run': run, 'scope': SCOPE,
           'source': {'kind': 'GitHub Actions job log, read on 2026-10-17 through the session\'s job-log tool, which returns at '
                              'most the last 5000 lines; this log was served whole',
                      'original_lines': m['original_length'], 'served_lines': len(lines), 'served_sha256': sha(text),
                      'extractor': EXTRACTOR, 'extractor_blob': EXTRACTOR_BLOB,
                      'note': 'the digest identifies the text this result was read from: it is provenance of the extraction, '
                              'not independent proof of the result, which reproduction at the commit supplies; the text is not '
                              'a byte copy of GitHub\'s log archive, and it is not retained'},
           'expected': {'build_success': True, 'gate': None, 'modules': modules, 'markers': x['markers'],
                        'permitted_axioms': PERMITTED},
           'observed': {'build_line': 'Build completed successfully (%d jobs).' % x['build']['jobs'], 'built': x['built'],
                        'cache': x['cache'], 'reports_in_served_text': sum(len(v) for v in x['reports'].values()),
                        'report_served_lines': {mod: {r['name']: r['served_line'] for r in x['reports'].get(mod, [])}
                                                for mod in targets},
                        'unprefixed_report_lines': len(bare)},
           'reproduce': {
               'recipe': ['run from the root of a full-history clone at a commit that carries this archive (the verifier); '
                          'the source commit is not on main, so fetch it first (git fetch origin %s, while that branch '
                          'exists); <dir> is a new directory and <log> a file outside it' % BRANCH,
                          'git worktree add --detach <dir> %s' % head,
                          '(cd <dir>/verification/lean-mathlib && lean --version && lake exe cache get && lake --rehash build %s) > <log> 2>&1'
                          % ' '.join(t[:-5].replace('/', '.') for t in targets),
                          'python3 -I verification/audits/evidence-retention/extract_result.py <log> > reproduced.json',
                          'compare build success, the markers, and each target module\'s reports and axioms with expected; '
                          'compare_result.py requires a release gate, which this build has none of, so the comparison is by hand'],
               'tool': None,
               'compared': 'build success; each target module\'s reports and axioms; the markers',
               'not_compared': 'timestamps, durations, cache behaviour, job counts, output order; the design files\' reports '
                               'and the exact-control output (recorded gaps)'}}
    d = os.path.join(ARCH, 'ci', rid)
    os.makedirs(d, exist_ok=True)
    runj = {k: a[k] for k in RUN_FIELDS}
    runj.update({'run_id': rid, 'source': 'GitHub Actions runs API, GET runs/<run_id>, read 2026-10-17; selected fields'})
    jobs = {'run_id': rid, 'source': 'GitHub Actions jobs API, GET runs/<run_id>/jobs?filter=all, read 2026-10-17; selected fields',
            'jobs': [dict({k: j[k] for k in JOB_FIELDS},
                          steps=[{'number': s['number'], 'name': s['name'], 'conclusion': s['conclusion']} for s in j['steps']])
                     for j in sorted(jl['jobs'], key=lambda j: j['id'])]}
    files = []
    for name, obj, src in (('run.json', runj, araw), ('jobs.json', jobs, jraw), ('results.json', res, text)):
        b = dump(obj)
        open(os.path.join(d, name), 'wb').write(b)
        files.append({'path': 'ci/%s/%s' % (rid, name), 'bytes': len(b), 'sha256': sha(b), 'kind': 'derived', 'source_sha256': sha(src)})
    man['entries'].append({
        'id': 'research-' + rid, 'kind': 'derived', 'run_id': rid, 'files': files, 'citations': [],
        'awaiting_citation': {'pull_request': 831, 'record': CITER, 'line': cline, 'head': '65b85147f85aa01770e0e60551152bc5f1d9ef29',
                              'note': 'retained ahead of its citing record by the owner\'s instruction of 2026-10-17; no tracked '
                                      'file outside this archive cites the run'},
        'roles': [{'kind': 'research build', 'workflow': WORKFLOW, 'branch': BRANCH, 'commit': head}],
        'notes': ['the result establishes what this run logged at %s, nothing about later trees' % head[:12]]})
    man['missing'] += [dict(g, id='research-' + rid, run_id=rid) for g in gaps]
here = os.path.join(ARCH, 'build_research_runs.py')
man['entries'].append({'id': 'research-runs-record', 'kind': 'complete', 'citations': [], 'files': [
    {'path': 'build_research_runs.py', 'bytes': os.path.getsize(here), 'sha256': sha(open(here, 'rb').read()), 'kind': 'complete'}],
    'provenance': {'source': 'written for this archive: the script that cut the research-build entries'}})
open(man_path, 'w', encoding='utf-8').write(json.dumps(man, indent=1, sort_keys=True, ensure_ascii=False) + '\n')
for rid in (r[0] for r in RUNS):
    print(rid, [f['sha256'] for e in man['entries'] if e['id'] == 'research-' + rid for f in e['files'] if f['path'].endswith('results.json')],
          [g['what'] for g in man['missing'] if g['id'] == 'research-' + rid])
