#!/usr/bin/env python3
"""Builds verification/audits/evidence-retention/ tranche 1 from retrieved CI responses.

This script is retained as the record of how the archive was cut: which lines an excerpt keeps, which fields a
derived file selects, and how each gap was found. It cannot be re-run from the repository tree alone, because its
inputs are not retained:
  - the staging directory of retrieved job lists and Mathlib-bridge job-log tails, copied byte for byte from
    saved tool output;
  - the re-served responses for the four BG-3 logs;
  - the saved runs-API listing pages (run.json's source);
  - the per-citation claim annotations.
The archive records each input's digest. Its retained copies are checked by check_retention.py from the tree.

Run from the repository root of a clone containing BASE and every attested commit; it reads the receipts,
control planes, citing records and the governed Lean modules with `git show`. Standard library only.

Usage: build_archive.py BASE STAGE BG3DIR REPLAYDIR AUDITDIR RUNS_JSON META_JSON CLAIMS_JSON OUTDIR RUNLIST_PAGE1

Lines are counted by splitting on newline characters: a text that ends without one has one more line than
`wc -l` reports. The served job-log texts end without one.
"""
import hashlib
import json
import os
import re
import subprocess
import sys

BASE, STAGE, BG3DIR, REPLAY, AUDITDIR, RUNS_JSON, META_JSON, CLAIMS_JSON, OUT, PAGE1 = sys.argv[1:11]


def git(*args):
    return subprocess.run(['git'] + list(args), capture_output=True)


def show(path, rev=None):
    r = git('show', '%s:%s' % (rev or BASE, path))
    return r.stdout if r.returncode == 0 else None


def blob_id(data):
    return hashlib.sha1(b'blob %d\0' % len(data) + data).hexdigest()


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def lines_of(text):
    """The convention above: split on newline characters; a final newline ends the last line."""
    ls = text.split('\n')
    return ls[:-1] if text.endswith('\n') else ls


def citing(token, paths=None):
    """Every (path, line) on BASE whose line contains token, with the citing file's blob id."""
    out = subprocess.run(['git', 'grep', '-n', '-F', token, BASE, '--'] + (paths or ['.']),
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


SECRET = re.compile(r'gh[pousr]_[A-Za-z0-9]{20,}|github_pat[_]|AKIA[0-9A-Z]{16}|-{5}BEGIN|bearer [a-z0-9]'
                    r'|x-access-toke[n]|[?&](sig|signature|sv|se|token)=|passw(or)?d\s*[:=]|api[_-]?key\s*[:=]'
                    r'|private[_-]?key'
                    r'|(?<![\w.])(?:\d{1,3}\.){3}\d{1,3}(?![\w.])|[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}', re.I)


def secret_hits(text):
    return [l for l in text.split('\n') if SECRET.search(l)]


def write(rel, data):
    p = os.path.join(OUT, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, 'wb') as fh:
        fh.write(data)
    return {'path': rel, 'sha256': sha256(data), 'bytes': len(data)}


def dumps(obj):
    return (json.dumps(obj, indent=1, sort_keys=True, ensure_ascii=False) + '\n').encode('utf-8')


problems = []

# ---------------------------------------------------------------- receipts: rounds, governed Lean files, attestations
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


RUN_URL = re.compile(r'/actions/runs/(\d+)(?:/attempts/(\d+))?')
round_lean, attested, coverage = {}, {}, []
receipt_paths = git('ls-tree', '--name-only', BASE, 'verification/receipts/').stdout.decode().split()
for r in receipt_paths:
    raw = show(r)
    coverage.append({'path': r, 'blob': blob_id(raw)})
    rec = json.loads(raw)
    leans = []
    for b in rec.get('control_plane_blobs', []):
        leans += governed_lean(show(b['path']).decode('utf-8'))
    # OIBridge/<Name>.lean as the log prints it, and its path in the tree
    round_lean[rec['round']] = sorted({p.split('verification/lean-mathlib/', 1)[-1] for p in leans})
    for a in rec.get('attestations', []):
        if a.get('kind') == 'check-run':
            m = RUN_URL.search(a['record'])
            attested.setdefault(m.group(1), []).append(
                {'round': rec['round'], 'subject': a['subject'], 'commit': a['commit'],
                 'attempt': int(m.group(2)) if m.group(2) else None})
CERT = 'verification/certificates/attestations/CV1.json'
cert_raw = show(CERT)
coverage.append({'path': CERT, 'blob': blob_id(cert_raw)})
cert_runs = {v['run']: dict(v, role=k) for k, v in json.loads(cert_raw)['ci'].items()}

# ---------------------------------------------------------------- excerpt rules
GATE_START = re.compile(r'^\S+ release gate$')
GATE_END = re.compile(r'^\S+ release gate: ')
GATE_STEP = re.compile(r'^\S+\s+(PASS|FAIL|SKIP)\s')   # timestamp, then the step's status
KEEP = re.compile(r'Build completed successfully|error:|declaration uses .sorry.|sorryAx|Lean\.ofReduceBool'
                  r'|Cache saved with key|Cache hit occurred on the primary key|Cache restored from key'
                  r'|Cache not found for input keys|Failed to save|Failed to restore')
PRINT = re.compile(r'^#print axioms\b')


def report_re(mod):
    return re.compile(r' %s:(\d+):\d+: .*?(depends on axioms|does not depend on any axioms)' % re.escape(mod))


def excerpt(lines, modules):
    """Line numbers (0-based) to keep: the release-gate block, build status, errors and sorry markers, cache
    lines, and each governed module's build line and axiom reports (with wrapped continuation lines)."""
    keep = set()
    for s in [i for i, l in enumerate(lines) if GATE_START.match(l)]:
        e = next((j for j in range(s, len(lines)) if GATE_END.match(lines[j])), None)
        if e is not None:
            keep.update(range(s, e + 1))
    for i, l in enumerate(lines):
        if KEEP.search(l):
            keep.add(i)
    for mod in modules:
        built = 'Built ' + mod[:-len('.lean')].replace('/', '.') + ' '
        rr = report_re(mod)
        for i, l in enumerate(lines):
            if built in l + ' ':
                keep.add(i)
            m = rr.search(l)
            if m:
                keep.add(i)
                j = i
                while m.group(2) == 'depends on axioms' and ']' not in lines[j] and j + 1 < len(lines):
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


def spans(nums):
    return [[a, b] for a, b in ranges([n - 1 for n in sorted(nums)])]


def gate_summary(kept):
    block, inside = [], False
    for l in kept:
        if GATE_START.match(l):
            block, inside = [], True
        elif inside:
            block.append(l)
            inside = not GATE_END.match(l)
    steps = [GATE_STEP.match(l) for l in block]
    verdict = [l for l in block if GATE_END.match(l)]
    return {'steps': sum(1 for s in steps if s), 'pass': sum(1 for s in steps if s and s.group(1) == 'PASS'),
            'fail': sum(1 for s in steps if s and s.group(1) == 'FAIL'),
            'verdict': verdict[-1].split(' ', 1)[1] if verdict else None}


# ---------------------------------------------------------------- build
runs = json.load(open(RUNS_JSON))
meta = json.load(open(META_JSON))
claims = json.load(open(CLAIMS_JSON)) if os.path.exists(CLAIMS_JSON) else {}
entries, missing = [], []


def attach_claims(ent):
    """Per-citation claims: verbatim fragments of the citing file, each marked retained / not retained / differs."""
    for c in ent['citations']:
        key = '%s|%s:%d' % (ent['id'], c['path'], c['line'])
        if key in claims:
            c['claims'] = claims[key]
        else:
            problems.append('%s: no claim annotation' % key)
    for k in claims:
        if k.startswith(ent['id'] + '|') and not any(k == '%s|%s:%d' % (ent['id'], c['path'], c['line']) for c in ent['citations']):
            problems.append('%s: annotation for a location that is not a citation' % k)


def dedupe(cites):
    """One citation per (path, line); the tokens it carries are listed."""
    out = {}
    for c in cites:
        k = (c['path'], c['line'])
        if k in out:
            if c['token'] not in out[k]['tokens']:
                out[k]['tokens'].append(c['token'])
        else:
            out[k] = {'path': c['path'], 'line': c['line'], 'blob': c['blob'], 'tokens': [c['token']]}
    return [out[k] for k in sorted(out)]


# BG-3 logs (complete as cited). Provenance values are transcribed from the citing records and the re-served
# responses; each is re-checked below against the re-served response or the citing file.
BG3 = [
    ('bg3-e-bridge-tail', 'exec/bridge-116826161407-tail.log', '84de2bc0e2b2a2f6b34d27d25e5abad9037c5c42a8c12cdf7c1ce7ccc0acf649',
     {'run_id': '38855576525', 'job_id': '116826161407', 'job_name': 'Mathlib bridge', 'workflow': 'verify',
      'head_sha': '194eb3fd0c0a58ee843a574d93d4a0fa94f6cb79'}),
    ('bg3-e-design-log', 'exec/design-116831668411.log', 'bf1ab94553e857faf1b684fbaee5b538270e78dac35a5c13df370c6c234f5bf7',
     {'run_id': '38857340321', 'job_id': '116831668411', 'job_name': 'diagnostic', 'workflow': 'BG2 orientation design',
      'head_sha': '194eb3fd0c0a58ee843a574d93d4a0fa94f6cb79'}),
    ('bg3-design-bridge-tail', 'design/bridge-116805436638-tail.log', '9f1abf3c88899306609cb3c02485892fcd6b97dfd12cbf05e128ad029e05e7b7',
     {'run_id': '38848873989', 'job_id': '116805436638', 'job_name': 'Mathlib bridge', 'workflow': 'verify',
      'head_sha': 'e3ef9358d6690220c21a9b32924af9b3f70cb890'}),
    ('bg3-first-design-bridge-tail', 'design/bridge-116761232088-tail.log', 'e77b0ded140a70ae90514a2d923bae20a062415c45ab3c8ec62ed65ce26bac47',
     {'run_id': '38834744516', 'job_id': '116761232088', 'job_name': 'Mathlib bridge', 'workflow': 'verify',
      'head_sha': '6c160ad26a9831448e6e4cfca5761efb876a1baf'}),
]
for eid, src, digest, prov in BG3:
    data = open(os.path.join(BG3DIR, src), 'rb').read()
    text = data.decode('utf-8')
    if secret_hits(text):
        problems.append('%s: secret-pattern hits %r' % (eid, secret_hits(text)[:3]))
    rs = json.load(open(os.path.join(REPLAY, 'job-%s.json' % prov['job_id'])))
    served = rs['logs_content'].encode('utf-8')
    if str(rs['job_id']) != prov['job_id']:
        problems.append('%s: re-served job id %s' % (eid, rs['job_id']))
    n = len(lines_of(text))
    orig = rs.get('original_length')
    if 'design' in eid and 'bridge' not in eid:
        m = re.search(r'Complete job name: (.*)', text)
        if not m or m.group(1).strip() != prov['job_name']:
            problems.append('%s: job name in the log is %r' % (eid, m and m.group(1)))
    form = ('the complete job log: %d lines' % n) if orig == n else \
        ('the last %d lines of the %d-line job log' % (n, orig))
    form += ' (%d newline characters: the text ends without one)' % text.count('\n') if not text.endswith('\n') else ''
    f = write('bg3/' + os.path.basename(src), data)
    files = [f]
    if eid in ('bg3-design-bridge-tail', 'bg3-first-design-bridge-tail'):
        # the design runs' metadata, from the saved runs-API listing page 1 (same field selection as ci/*/run.json)
        page = open(PAGE1, 'rb').read()
        r = next(x for x in json.loads(page)['workflow_runs'] if str(x['id']) == prov['run_id'])
        sel = {k: r[k] for k in ('conclusion', 'created_at', 'display_title', 'event', 'head_branch', 'head_sha', 'id',
                                 'path', 'run_attempt', 'run_number', 'status', 'updated_at')}
        if sel['head_sha'] != prov['head_sha']:
            problems.append('%s: listing head_sha %s' % (eid, sel['head_sha']))
        files.append(dict(write('bg3/run-%s.json' % prov['run_id'], dumps(dict(
            sel, run_id=prov['run_id'], source='GitHub Actions runs API listing, selected fields'))), kind='derived',
            source_sha256=sha256(page), source_page=1, source_api='GitHub Actions runs API, workflow verify.yml, per_page 100'))
    cites = citing(digest)
    cited_lines = [show(c['path']).decode('utf-8').split('\n')[c['line'] - 1] for c in cites]
    found = [t for t in (prov['run_id'], prov['job_id'], prov['head_sha'][:8]) if any(t in l for l in cited_lines)]
    entries.append({
        'id': eid, 'kind': 'complete-as-cited', 'files': files, 'cited_digest': digest,
        'matches_cited_digest': f['sha256'] == digest,
        'provenance': dict(prov, source='GitHub Actions job log, read through the session\'s GitHub job-log tool, '
                                         'which returns at most the last 5000 lines', form=form,
                           original_lines=orig,
                           replay={'served_sha256': sha256(served), 'identical': served == data,
                                   'note': 'the log re-served on 2026-10-16, after the tranche was cut'},
                           tokens_on_citing_lines=found,
                           transcribed=[k for k in ('run_id', 'job_id', 'head_sha') if
                                        (prov[k] if k != 'head_sha' else prov[k][:8]) not in found] + ['workflow', 'job_name']),
        'citations': dedupe(cites)})
    if served != data:
        problems.append('%s: re-served bytes differ from the retained copy' % eid)
    if f['sha256'] != digest:
        problems.append('%s: digest mismatch' % eid)
missing.append({'id': 'bg3-e-design-log', 'run_id': '38857340321', 'what': 'run metadata of the design run',
                'why': 'served inline and not saved; the log alone does not state the run\'s conclusion'})

# CI runs
for r in runs:
    rid = r['run_id']
    d = os.path.join(STAGE, rid)
    eid = 'ci-' + rid
    ent = {'id': eid, 'run_id': rid, 'roles': [], 'files': [], 'notes': [], 'retains': {}}
    for a in attested.get(rid, []):
        ent['roles'].append(dict(a, kind='receipt check-run'))
    if rid in cert_runs:
        cr = cert_runs[rid]
        ent['roles'].append({'kind': 'V2 certificate', 'round': 'CV1', 'subject': cr['role'], 'commit': cr['head_sha']})
    if not ent['roles']:
        problems.append('%s: no role found in receipts or certificates' % rid)
    rounds = sorted({x['round'] for x in ent['roles'] if x['kind'] == 'receipt check-run'})
    # run metadata (derived from a saved listing page)
    mm = dict(meta[rid])
    src = mm.pop('source')
    run_sel = dict(mm, run_id=rid, source='GitHub Actions runs API listing, selected fields')
    ent['files'].append(dict(write('ci/%s/run.json' % rid, dumps(run_sel)), kind='derived', source_sha256=src['sha256'],
                             source_page=src['page'], source_api=src['api']))
    head = mm['head_sha']
    for x in ent['roles']:
        if x['commit'] != head:
            problems.append('%s: head_sha %s is not the attested commit %s' % (rid, head, x['commit']))
        if x.get('attempt') is not None and x['attempt'] != mm['run_attempt']:
            ent['notes'].append('the attestation names attempt %d; the listing reports run_attempt %d'
                                % (x['attempt'], mm['run_attempt']))
    ent['retains']['run'] = {k: mm[k] for k in ('head_sha', 'event', 'status', 'conclusion', 'run_attempt', 'created_at')}
    if mm['event'] != 'workflow_dispatch':
        ent['notes'].append('the run\'s event is %s' % mm['event'])
    # jobs (derived from a saved jobs response)
    jobs_sel = None
    if os.path.exists(os.path.join(d, 'jobs.json')):
        raw = open(os.path.join(d, 'jobs.json'), 'rb').read()
        j = json.loads(raw)
        jl = j['jobs']['jobs'] if isinstance(j.get('jobs'), dict) else j['jobs']
        jobs_sel = [{k: x.get(k) for k in ('id', 'name', 'status', 'conclusion', 'run_attempt', 'head_sha',
                                            'head_branch', 'workflow_name', 'started_at', 'completed_at')} for x in jl]
        jobs_sel.sort(key=lambda x: (x['run_attempt'] or 0, x['name'] or '', x['id']))
        ent['files'].append(dict(write('ci/%s/jobs.json' % rid, dumps(
            {'run_id': rid, 'source': 'GitHub Actions jobs API, selected fields', 'jobs': jobs_sel})),
            kind='derived', source_sha256=sha256(raw)))
        if {x['head_sha'] for x in jobs_sel} != {head}:
            problems.append('%s: job head_sha %s differs from the run\'s' % (rid, {x['head_sha'] for x in jobs_sel}))
        per = {}
        for x in jobs_sel:
            p = per.setdefault(str(x['run_attempt']), {'jobs': 0, 'conclusions': {}})
            p['jobs'] += 1
            p['conclusions'][str(x['conclusion'])] = p['conclusions'].get(str(x['conclusion']), 0) + 1
        ent['retains']['jobs'] = per
        if len(per) > 1:
            ent['notes'].append('the job list holds attempts %s; the run\'s run_attempt is %d, and the excerpt is from '
                                'that attempt\'s Mathlib bridge job' % (', '.join(sorted(per)), mm['run_attempt']))
    else:
        why = 'served inline and not saved' if os.path.exists(os.path.join(d, 'jobs.INLINE')) else 'not retrieved'
        ent['retains']['jobs'] = None
        missing.append({'id': eid, 'run_id': rid, 'what': 'job list', 'why': why})
    # bridge excerpt
    if not os.path.exists(os.path.join(d, 'bridge.json')):
        problems.append('%s: no saved bridge log' % rid)
        continue
    raw = open(os.path.join(d, 'bridge.json'), 'rb').read()
    b = json.loads(raw)
    text = b['logs_content']
    lines = lines_of(text)
    mods = sorted({m for rnd in rounds for m in round_lean.get(rnd, [])})
    idx = excerpt(lines, mods)
    kept = [lines[i] for i in idx]
    ex = '\n'.join(kept) + '\n'
    if secret_hits(ex):
        problems.append('%s: secret-pattern hits in excerpt %r' % (rid, secret_hits(ex)[:3]))
    job = open(os.path.join(d, 'bridge.job')).read().split(None, 1)
    if str(b.get('job_id')) != job[0]:
        problems.append('%s: bridge.job id %s differs from the saved response job_id %s' % (rid, job[0], b.get('job_id')))
    if jobs_sel is not None and not any(str(x['id']) == job[0] and x['name'] == 'Mathlib bridge'
                                        and x['run_attempt'] == mm['run_attempt'] for x in jobs_sel):
        problems.append('%s: bridge job %s is not the Mathlib bridge job of attempt %d' % (rid, job[0], mm['run_attempt']))
    orig = b.get('original_length')
    modrec = []
    for mod in mods:
        src_text = show('verification/lean-mathlib/' + mod, head)
        rr = report_re(mod)
        reported = sorted({int(rr.search(l).group(1)) for l in kept if rr.search(l)})
        built = any(('Built ' + mod[:-len('.lean')].replace('/', '.') + ' ') in l + ' ' for l in kept)
        rec = {'module': mod, 'reported_lines': spans(reported), 'reported': len(reported), 'build_line': built}
        if src_text is None:
            rec['status'] = 'absent'
            rec['note'] = 'the module is not in the tree at %s' % head[:12]
            if reported:
                problems.append('%s: reports for %s, which is absent at the head' % (rid, mod))
        else:
            prints = [i + 1 for i, l in enumerate(src_text.decode('utf-8').split('\n')) if PRINT.match(l)]
            rec['print_lines'] = spans(prints)
            rec['prints'] = len(prints)
            extra = set(reported) - set(prints)
            if extra:
                problems.append('%s: %s reports at lines %s with no #print axioms there' % (rid, mod, sorted(extra)[:5]))
            lost = sorted(set(prints) - set(reported))
            rec['status'] = 'complete' if not lost else 'partial' if reported else 'none'
            if lost:
                rec['unreported_print_lines'] = spans(lost)
                missing.append({'id': eid, 'run_id': rid, 'what': 'axiom reports of %s' % mod,
                                'why': '%d of the module\'s %d #print axioms reports are in the served lines; '
                                       'the served text is the last %d of the log\'s %s lines, and the build line is %s'
                                       % (len(reported), len(prints), len(lines), orig, 'in them' if built else 'not in them')})
        modrec.append(rec)
    ent['retains']['gate'] = gate_summary(kept)
    ent['retains']['modules'] = modrec
    ent['retains']['cache'] = [l[29:] for l in kept if re.search(r'Cache (saved|hit|restored|not found)|Failed to (save|restore)', l)]
    ent['retains']['markers'] = sum(1 for l in kept if re.search(r'error:|declaration uses .sorry.|sorryAx|Lean\.ofReduceBool', l))
    ent['files'].append(dict(write('ci/%s/bridge-excerpt.log' % rid, ex.encode('utf-8')), kind='excerpt',
                             source={'job_id': job[0], 'job_name': 'Mathlib bridge', 'served_lines': len(lines),
                                     'served_sha256': sha256(text.encode('utf-8')), 'original_lines': orig,
                                     'line_ranges': ranges(idx), 'modules': mods}))
    if ent['retains']['gate']['verdict'] is None:
        ent['notes'].append('no release-gate verdict line in the served lines')
    ent['citations'] = dedupe(citing(rid))
    entries.append(ent)

# the archive's own retained record files
own = []
for rel, srcp in (('build_archive.py', os.path.abspath(__file__)),
                  ('audit/offmain_audit.py', os.path.join(AUDITDIR, 'offmain_audit.py')),
                  ('audit/offmain_audit-output.txt', os.path.join(AUDITDIR, 'offmain_audit-output.txt')),
                  ('audit/audit.md', os.path.join(AUDITDIR, 'audit.md'))):
    data = open(srcp, 'rb').read()
    if secret_hits(data.decode('utf-8')):
        problems.append('%s: secret-pattern hits' % rel)
    own.append(dict(write(rel, data), kind='complete'))
entries.append({'id': 'tranche-record', 'kind': 'complete', 'files': own, 'citations': [],
                'provenance': {'source': 'written for this tranche: its build script and the off-main audit it acts on'}})

for e in entries:
    if e['citations']:
        attach_claims(e)

manifest = {
    'schema': 'oi-evidence-retention', 'version': 2, 'tranche': 1, 'base': BASE,
    'line_convention': 'lines are counted by splitting on newline characters; a text that ends without one has one '
                       'more line than wc -l reports',
    'kinds': {
        'complete-as-cited': 'byte-identical to the artifact the citing record names by digest',
        'complete': 'a file of this tranche, in full',
        'excerpt': 'exact lines cut from a served log; line_ranges are 1-based within the served text, whose digest is '
                   'served_sha256; the served text itself is not retained',
        'derived': 'selected fields of an API response saved byte for byte; source_sha256 is that response, which is '
                   'not retained',
    },
    'claim_status': {
        'retained': 'the archived files named in "in" carry the fragment',
        'not retained': 'no archived file carries the fragment',
        'differs': 'the archived files named in "in" show something other than the fragment; "note" says what',
    },
    'coverage': {'files': coverage, 'later': [],
                 'rule': 'every receipt in the tree, and every certificate attestation citing runs, is in files or in '
                         'later; every check-run attestation of a file in files, and every run it cites, has an entry. '
                         'later names a receipt landed after this tranche, with where its evidence is retained'},
    'entries': entries, 'missing': missing,
}
open(os.path.join(OUT, 'manifest.json'), 'wb').write(dumps(manifest))
print('entries', len(entries), 'missing', len(missing),
      'citations', sum(len(e['citations']) for e in entries))
for p in problems:
    print('PROBLEM', p)
sys.exit(1 if problems else 0)
