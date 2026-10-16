#!/usr/bin/env python3
"""Builds verification/audits/evidence-retention/ tranche 1 from retrieved CI responses.

Run from the repository root of the base commit (it reads the receipts, the round control planes and the
citing records with `git show BASE:path`). Inputs outside the repository: the staging directory of retrieved
GitHub API responses (job lists and Mathlib-bridge job-log tails, copied byte for byte from saved tool output)
and the four BG-3 logs. Those inputs are provenance; the archive records their digests, and the retained
copies are the only form the archive relies on.

Standard library only. Usage: build_archive.py BASE STAGE BG3DIR RUNS_JSON META_JSON OUTDIR
"""
import hashlib
import json
import os
import re
import subprocess
import sys

BASE, STAGE, BG3DIR, RUNS_JSON, META_JSON, OUT = sys.argv[1:7]


def show(path):
    return subprocess.run(['git', 'show', '%s:%s' % (BASE, path)], capture_output=True, check=True).stdout


def blob_id(data):
    return hashlib.sha1(b'blob %d\0' % len(data) + data).hexdigest()


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def citing(token):
    """Every (path, line) on BASE whose line contains token, with the citing file's blob id."""
    out = subprocess.run(['git', 'grep', '-n', '-F', token, BASE, '--', '.'],
                         capture_output=True, text=True).stdout
    res = []
    for ln in out.split('\n'):
        if not ln:
            continue
        _, path, line, _ = ln.split(':', 3)
        if path.endswith(('.pdf', '.tex')):
            continue
        res.append({'path': path, 'line': int(line), 'token': token, 'blob': blob_id(show(path))})
    return res


SECRET = re.compile(r'gh[pousr]_[A-Za-z0-9]{20,}|github_pat_|AKIA[0-9A-Z]{16}|-----BEGIN|bearer [a-z0-9]'
                    r'|x-access-token|[?&](sig|signature|sv|se|token)=|passw(or)?d\s*[:=]|api[_-]?key\s*[:=]'
                    r'|private[_-]?key', re.I)
SECRET_OK = re.compile(r'Secret source: Actions|AUTHORIZATION: basic \*\*\*')


def secret_hits(text):
    return [l for l in text.split('\n') if SECRET.search(l) and not SECRET_OK.search(l)]


def write(rel, data):
    p = os.path.join(OUT, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, 'wb') as fh:
        fh.write(data)
    return {'path': rel, 'sha256': sha256(data), 'bytes': len(data)}


def dumps(obj):
    return (json.dumps(obj, indent=1, sort_keys=True, ensure_ascii=False) + '\n').encode('utf-8')


# ---------------------------------------------------------------- the rounds' governed Lean files
def governed_lean(prereg_text):
    m = re.search(r'```v3-governed-paths\n(.*?)```', prereg_text, re.S)
    if not m:
        return []
    paths = []
    for ln in m.group(1).split('\n'):
        parts = ln.split()
        if len(parts) == 3 and parts[0] == 'execution' and parts[2].endswith('.lean'):
            paths.append(parts[2])
    return paths


round_lean = {}
for r in subprocess.run(['git', 'ls-tree', '--name-only', BASE, 'verification/receipts/'],
                        capture_output=True, text=True).stdout.split():
    rec = json.loads(show(r))
    leans = []
    for b in rec.get('control_plane_blobs', []):
        leans += governed_lean(show(b['path']).decode('utf-8'))
    # OIBridge/<Name>.lean as the log prints it
    round_lean[rec['round']] = sorted({p.split('verification/lean-mathlib/', 1)[-1] for p in leans})


# ---------------------------------------------------------------- excerpt rules
GATE_START = re.compile(r'^\S+ release gate$')
GATE_END = re.compile(r'^\S+ release gate: ')
KEEP = re.compile(r'Build completed successfully|error:|declaration uses .sorry.|sorryAx|Lean\.ofReduceBool')


def excerpt(lines, modules):
    """Line numbers (1-based) to keep: the release-gate block, build status, errors and sorry markers, and
    the axiom reports (with their wrapped continuation lines) of the round's own governed modules."""
    keep = set()
    starts = [i for i, l in enumerate(lines) if GATE_START.match(l)]
    for s in starts:
        e = next((j for j in range(s, len(lines)) if GATE_END.match(lines[j])), None)
        if e is not None:
            keep.update(range(s, e + 1))
    for i, l in enumerate(lines):
        if KEEP.search(l):
            keep.add(i)
    for mod in modules:
        built = 'Built ' + mod[:-len('.lean')].replace('/', '.')
        for i, l in enumerate(lines):
            if built in l:
                keep.add(i)
            if (' %s:' % mod) in l and 'depends on axioms' in l:
                keep.add(i)
                j = i
                while ']' not in lines[j] and j + 1 < len(lines):
                    j += 1
                    keep.add(j)
    return sorted(keep)


def ranges(idx):
    out = []
    for i in idx:
        if out and i == out[-1][1] + 1:
            out[-1][1] = i
        else:
            out.append([i, i])
    return [[a + 1, b + 1] for a, b in out]


# ---------------------------------------------------------------- build
runs = json.load(open(RUNS_JSON))
meta = json.load(open(META_JSON)) if os.path.exists(META_JSON) else {}
entries, problems, missing = [], [], []

# BG-3 logs (complete as cited)
BG3 = [
    ('bg3-e-bridge-tail', 'exec/bridge-116826161407-tail.log', '84de2bc0e2b2a2f6b34d27d25e5abad9037c5c42a8c12cdf7c1ce7ccc0acf649',
     {'run_id': '38855576525', 'job_id': '116826161407', 'job_name': 'Mathlib bridge',
      'head_sha': '194eb3fd0c0a58ee843a574d93d4a0fa94f6cb79', 'form': 'the last 4999 lines of the job log, as GitHub served them'}),
    ('bg3-e-design-log', 'exec/design-116831668411.log', 'bf1ab94553e857faf1b684fbaee5b538270e78dac35a5c13df370c6c234f5bf7',
     {'run_id': '38857340321', 'job_id': '116831668411', 'job_name': 'BG2 orientation design (job log)',
      'head_sha': '194eb3fd0c0a58ee843a574d93d4a0fa94f6cb79', 'form': 'the job log as GitHub served it under a 5000-line tail limit; 957 lines were returned'}),
    ('bg3-design-bridge-tail', 'design/bridge-116805436638-tail.log', '9f1abf3c88899306609cb3c02485892fcd6b97dfd12cbf05e128ad029e05e7b7',
     {'run_id': '38848873989', 'job_id': '116805436638', 'job_name': 'Mathlib bridge',
      'head_sha': 'e3ef9358d6690220c21a9b32924af9b3f70cb890', 'form': 'the last 4999 lines of the job log, as GitHub served them'}),
    ('bg3-first-design-bridge-tail', 'design/bridge-116761232088-tail.log', 'e77b0ded140a70ae90514a2d923bae20a062415c45ab3c8ec62ed65ce26bac47',
     {'run_id': '38834744516', 'job_id': '116761232088', 'job_name': 'Mathlib bridge',
      'head_sha': '6c160ad26a9831448e6e4cfca5761efb876a1baf', 'form': 'the last 4999 lines of the job log, as GitHub served them'}),
]
for eid, src, digest, prov in BG3:
    data = open(os.path.join(BG3DIR, src), 'rb').read()
    hits = secret_hits(data.decode('utf-8'))
    if hits:
        problems.append('%s: secret-pattern hits %r' % (eid, hits[:3]))
    f = write('bg3/' + os.path.basename(src), data)
    cites = citing(digest) + citing(prov['job_id'])
    entries.append({'id': eid, 'kind': 'complete-as-cited', 'files': [f], 'cited_digest': digest,
                    'matches_cited_digest': f['sha256'] == digest, 'provenance': dict(prov, source='GitHub Actions job log'),
                    'citations': cites})
    if f['sha256'] != digest:
        problems.append('%s: digest mismatch' % eid)

# CI runs
for r in runs:
    rid = r['run_id']
    d = os.path.join(STAGE, rid)
    ent = {'id': 'ci-' + rid, 'run_id': rid, 'roles': r['roles'], 'files': [], 'notes': []}
    rounds = [x.get('round') for x in r['roles'] if x.get('round')]
    expected = sorted({x['commit'] for x in r['roles'] if x.get('commit')})
    # jobs
    jobs_sel = None
    if os.path.exists(os.path.join(d, 'jobs.json')):
        raw = open(os.path.join(d, 'jobs.json'), 'rb').read()
        j = json.loads(raw)
        jl = j['jobs']['jobs'] if isinstance(j.get('jobs'), dict) else j['jobs']
        jobs_sel = [{k: x.get(k) for k in ('id', 'name', 'status', 'conclusion', 'run_attempt', 'head_sha',
                                            'head_branch', 'workflow_name', 'started_at', 'completed_at')} for x in jl]
        jobs_sel.sort(key=lambda x: (x['name'] or '', x['id']))
        ent['files'].append(dict(write('ci/%s/jobs.json' % rid, dumps(
            {'run_id': rid, 'source': 'GitHub Actions jobs API, selected fields', 'jobs': jobs_sel})),
            kind='derived', source_sha256=sha256(raw)))
        heads = sorted({x['head_sha'] for x in jobs_sel})
        ent['head_sha'] = heads
        ent['conclusions'] = sorted({str(x['conclusion']) for x in jobs_sel})
    else:
        why = 'served inline and not saved' if os.path.exists(os.path.join(d, 'jobs.INLINE')) else 'not retrieved'
        ent['notes'].append('job list not retained (%s)' % why)
        missing.append({'run_id': rid, 'what': 'job list', 'why': why})
    if rid in meta:
        mm = dict(meta[rid])
        src = mm.pop('source')
        ent['files'].append(dict(write('ci/%s/run.json' % rid, dumps(dict(mm, run_id=rid,
            source='GitHub Actions runs API listing, selected fields'))), kind='derived', source_sha256=src['sha256'],
            source_page=src['page']))
        ent.setdefault('head_sha', [mm['head_sha']])
        ent['run_conclusion'] = mm['conclusion']
        if ent.get('head_sha') and mm['head_sha'] not in ent['head_sha']:
            problems.append('%s: listing head_sha %s differs from the job list %s' % (rid, mm['head_sha'], ent['head_sha']))
    else:
        missing.append({'run_id': rid, 'what': 'run metadata'})
    if expected and ent.get('head_sha'):
        for c in expected:
            if not any(h.startswith(c) for h in ent['head_sha']):
                problems.append('%s: head_sha %s does not match attested commit %s' % (rid, ent['head_sha'], c))
    # bridge excerpt
    if os.path.exists(os.path.join(d, 'bridge.json')):
        raw = open(os.path.join(d, 'bridge.json'), 'rb').read()
        b = json.loads(raw)
        text = b['logs_content']
        lines = text.split('\n')
        mods = sorted({m for rnd in rounds for m in round_lean.get(rnd, [])})
        idx = excerpt(lines, mods)
        ex = '\n'.join(lines[i] for i in idx) + '\n'
        hits = secret_hits(ex)
        if hits:
            problems.append('%s: secret-pattern hits in excerpt %r' % (rid, hits[:3]))
        job = open(os.path.join(d, 'bridge.job')).read().split(None, 1)
        if str(b.get('job_id')) != job[0]:
            problems.append('%s: bridge.job id %s differs from the saved response job_id %s' % (rid, job[0], b.get('job_id')))
        if jobs_sel is not None and not any(str(x['id']) == job[0] and x['name'] == 'Mathlib bridge' for x in jobs_sel):
            problems.append('%s: bridge job %s is not the job list\'s Mathlib bridge' % (rid, job[0]))
        ent['files'].append(dict(write('ci/%s/bridge-excerpt.log' % rid, ex.encode('utf-8')), kind='excerpt',
                                 source={'job_id': job[0], 'job_name': job[1].strip() if len(job) > 1 else None,
                                         'served_lines': len(lines), 'served_sha256': sha256(text.encode('utf-8')),
                                         'original_length': b.get('original_length'),
                                         'line_ranges': ranges(idx), 'modules': mods}))
        if not any(GATE_END.match(lines[i]) for i in idx):
            ent['notes'].append('no release-gate verdict line in the served tail')
        for mod in mods:
            if not any((' %s:' % mod) in lines[i] for i in idx):
                ent['notes'].append('no axiom report for %s in the served tail (module not rebuilt in this run, or reports outside the tail)' % mod)
                missing.append({'run_id': rid, 'what': 'axiom reports of %s' % mod, 'why': 'not in the served lines: the module was not rebuilt in this run, or its reports precede the served tail'})
    else:
        why = 'bridge job log served inline and not saved' if os.path.exists(os.path.join(d, 'bridge.INLINE')) else \
              'no Mathlib bridge job' if os.path.exists(os.path.join(d, 'bridge.ABSENT')) else 'bridge job log not retrieved'
        ent['notes'].append(why)
        missing.append({'run_id': rid, 'what': 'Mathlib bridge excerpt', 'why': why})
    ent['citations'] = citing(rid)
    entries.append(ent)

manifest = {
    'schema': 'oi-evidence-retention', 'version': 1, 'tranche': 1, 'base': BASE,
    'kinds': {
        'complete-as-cited': 'byte-identical to the artifact the citing record names by digest',
        'excerpt': 'exact lines cut from a served log; line_ranges are 1-based within the served text, whose digest is served_sha256',
        'derived': 'selected fields of an API response saved byte for byte; source_sha256 is that response',
    },
    'entries': entries, 'missing': missing,
}
open(os.path.join(OUT, 'manifest.json'), 'wb').write(dumps(manifest))
print('entries', len(entries), 'missing', len(missing))
for p in problems:
    print('PROBLEM', p)
sys.exit(1 if problems else 0)
