#!/usr/bin/env python3
"""Builds verification/audits/evidence-retention/ tranche 1 from retrieved CI responses.

This script is retained as the record of how the archive was cut: which fields a derived file selects, how each
expected result was extracted, and how each gap was found. It cannot be re-run from the repository tree alone,
because its inputs are not retained:
  - the staging directory of retrieved job lists and Mathlib-bridge job-log texts, copied byte for byte from
    saved tool output;
  - the re-served responses for the four BG-3 logs;
  - the saved runs-API listing pages (run.json's source);
  - the per-citation claim annotations.
The archive records each input's digest. What it retains is checked by check_retention.py from the tree, and
each expected result is reproducible at its commit by reproduce.py.

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

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from extract_result import extract  # noqa: E402

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

# ---------------------------------------------------------------- expected results
PRINT = re.compile(r'^#print axioms\b')
PERMITTED = ['propext', 'Classical.choice', 'Quot.sound']
EXTRACTOR = 'verification/audits/evidence-retention/extract_result.py'
RECIPE = ['git checkout <head_sha>', 'cd verification/lean-mathlib && lean --version && lake exe cache get && lake --rehash build',
          'cd ../.. && python3 tools/release_gate.py',
          'python3 -I %s <captured output> > reproduced.json' % EXTRACTOR,
          'python3 -I verification/audits/evidence-retention/compare_result.py <this results.json> reproduced.json --tree .']
SOURCE_NOTE = ('the digest identifies the text this result was read from: it is provenance of the extraction, not '
               'independent proof of the result, which reproduction at the commit supplies')


def spans(nums):
    out = []
    for n in sorted(nums):
        if out and n == out[-1][1] + 1:
            out[-1][1] = n
        else:
            out.append([n, n])
    return out


def results_for(text, head, mods, run, source, tool_recipe=None):
    """The structured expected result of a Mathlib bridge job: what reproduction at head must reproduce."""
    x = extract(text)
    modules, gaps = {}, []
    for mod in mods:
        reps = x['reports'].get(mod, [])
        src_text = show('verification/lean-mathlib/' + mod, head)
        rec = {'reports': [{'line': r['line'], 'name': r['name'], 'axioms': r['axioms']} for r in reps]}
        if any(r.get('unclosed') for r in reps):
            problems.append('%s: an unclosed report of %s' % (run['id'], mod))
        if src_text is None:
            rec.update(status='absent', prints=None, print_lines=None, note='the module is not in the tree at %s' % head[:12])
            if reps:
                problems.append('%s: reports for %s, which is absent at the head' % (run['id'], mod))
        else:
            prints = [i + 1 for i, l in enumerate(src_text.decode('utf-8').split('\n')) if PRINT.match(l)]
            reported = {r['line'] for r in reps}
            if reported - set(prints):
                problems.append('%s: %s reports at lines %s with no #print axioms there' % (run['id'], mod, sorted(reported - set(prints))[:5]))
            lost = sorted(set(prints) - reported)
            rec.update(status='complete' if not lost else 'partial' if reported else 'none', prints=len(prints), print_lines=spans(prints))
            if lost:
                rec['unreported_print_lines'] = spans(lost)
                gaps.append({'what': 'axiom reports of %s' % mod,
                             'why': '%d of the module\'s %d #print axioms reports are in the served lines; the served text is the '
                                    'last %d of the log\'s %s lines; reproduction at the commit reports all %d'
                                    % (len(reported), len(prints), x['lines'], source.get('original_lines'), len(prints))})
        modules[mod] = rec
    if not x['build'] or not x['gate'] or not x['gate']['verdict']:
        problems.append('%s: no build line or no release-gate verdict in the served text' % run['id'])
    expected = {
        'build_success': bool(x['build'] and x['build']['success']),
        'gate': {'verdict': x['gate']['verdict']['text'] if x['gate'] and x['gate']['verdict'] else None,
                 'steps': [{'name': s['name'], 'status': s['status'], 'summary': s['summary']} for s in (x['gate']['steps'] if x['gate'] else [])],
                 'steps_total': len(x['gate']['steps']) if x['gate'] else 0,
                 'steps_pass': sum(1 for s in x['gate']['steps'] if s['status'] == 'PASS') if x['gate'] else 0},
        'modules': modules,
        'markers': x['markers'],
        'permitted_axioms': PERMITTED,
    }
    observed = {
        'build_line': 'Build completed successfully (%d jobs).' % x['build']['jobs'] if x['build'] else None,
        'built': x['built'],
        'cache': x['cache'],
        'reports_in_served_text': sum(len(v) for v in x['reports'].values()),
        'report_served_lines': {mod: {r['name']: r['served_line'] for r in x['reports'].get(mod, [])} for mod in mods},
        'gate_served_lines': {'start': x['gate']['start_line'] if x['gate'] else None,
                              'verdict': x['gate']['verdict']['served_line'] if x['gate'] and x['gate']['verdict'] else None},
    }
    res = {'schema': 'oi-evidence-result', 'version': 1, 'kind': 'bridge', 'run': run,
           'source': dict(source, extractor=EXTRACTOR, note=SOURCE_NOTE),
           'reproduce': {'recipe': RECIPE, 'tool': 'python3 -I verification/audits/evidence-retention/reproduce.py --run %s' % run['id'],
                         'workflow': '.github/workflows/reproduce-evidence.yml',
                         'compared': 'build success; the gate\'s steps and verdict; each governed module\'s reports and axioms; the markers',
                         'not_compared': 'timestamps, durations, cache behaviour, job counts, output order'},
           'expected': expected, 'observed': observed}
    if tool_recipe:
        res['reproduce'] = tool_recipe
    return res, gaps


def design_results(text, run, source):
    """The structured expected result of the BG2-orientation-design diagnostic job: its own check lines."""
    lines = [re.sub(r'^\d{4}-\d\d-\d\dT[\d:.]+Z ', '', l) for l in text.split('\n')]
    oks = [l for l in lines if re.match(r'^(verification/\S+|\.github/workflows/\S+): OK$', l)]
    alls = [l for l in lines if re.match(r'^All .* (use only standard axioms|match axiom-reports\.txt)', l)]
    co = next((l for l in lines if 'HEAD is now at' in l), None)
    expected = {'sha256sum_ok': oks, 'checks': alls,
                'silent_diffs': ['exact_check.py', 'independent_check.py', 'quoted_family_check.py'],
                'note': 'each silent diff is a check whose output must equal the committed JSON; the job runs under '
                        'pipefail and -e, so any difference fails it'}
    return {'schema': 'oi-evidence-result', 'version': 1, 'kind': 'design-diagnostic', 'run': run,
            'source': dict(source, extractor='a line filter in build_archive.py (design_results)', note=SOURCE_NOTE),
            'reproduce': {'recipe': ['dispatch .github/workflows/bg2-orientation-design.yml at %s, or run its diagnostic job\'s commands at that commit' % run['head_sha'][:12]],
                          'compared': 'the sha256sum OK lines, the three "All …" check lines, and the silent diffs',
                          'not_compared': 'timestamps and runner metadata', 'tool': None},
            'expected': expected, 'observed': {'checkout_line': co}}


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
    srcinfo = {'kind': 'the complete-as-cited log bg3/%s' % os.path.basename(src), 'sha256': f['sha256'],
               'lines': len(lines_of(text)), 'original_lines': rs.get('original_length')}
    if eid == 'bg3-e-design-log':
        res = design_results(text, {'id': prov['run_id'], 'head_sha': prov['head_sha'], 'workflow': 'bg2-orientation-design.yml',
                                    'job_id': prov['job_id'], 'job_name': prov['job_name']}, srcinfo)
    else:
        res, _ = results_for(text, prov['head_sha'], round_lean.get('BG-3', []),
                             {'id': prov['run_id'], 'head_sha': prov['head_sha'], 'workflow': 'verify.yml',
                              'job_id': prov['job_id'], 'job_name': prov['job_name']}, srcinfo)
    files.append(dict(write('bg3/results-%s.json' % prov['job_id'], dumps(res)), kind='derived', source_sha256=f['sha256']))
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
    ent = {'id': eid, 'run_id': rid, 'roles': [], 'files': [], 'notes': []}
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
        if len(per) > 1:
            ent['notes'].append('the job list holds attempts %s; the run\'s run_attempt is %d, and the expected result is from '
                                'that attempt\'s Mathlib bridge job' % (', '.join(sorted(per)), mm['run_attempt']))
    else:
        why = 'served inline and not saved' if os.path.exists(os.path.join(d, 'jobs.INLINE')) else 'not retrieved'
        missing.append({'id': eid, 'run_id': rid, 'what': 'job list', 'why': why})
    # the expected result, from the served bridge-job log
    if not os.path.exists(os.path.join(d, 'bridge.json')):
        problems.append('%s: no saved bridge log' % rid)
        continue
    raw = open(os.path.join(d, 'bridge.json'), 'rb').read()
    b = json.loads(raw)
    text = b['logs_content']
    job = open(os.path.join(d, 'bridge.job')).read().split(None, 1)
    if str(b.get('job_id')) != job[0]:
        problems.append('%s: bridge.job id %s differs from the saved response job_id %s' % (rid, job[0], b.get('job_id')))
    if jobs_sel is not None and not any(str(x['id']) == job[0] and x['name'] == 'Mathlib bridge'
                                        and x['run_attempt'] == mm['run_attempt'] for x in jobs_sel):
        problems.append('%s: bridge job %s is not the Mathlib bridge job of attempt %d' % (rid, job[0], mm['run_attempt']))
    mods = sorted({m for rnd in rounds for m in round_lean.get(rnd, [])})
    res, gaps = results_for(text, head, mods,
                            {'id': rid, 'head_sha': head, 'event': mm['event'], 'conclusion': mm['conclusion'],
                             'attempt': mm['run_attempt'], 'workflow': 'verify.yml', 'job_id': job[0], 'job_name': 'Mathlib bridge'},
                            {'kind': 'GitHub Actions job log, read through the session\'s job-log tool, which returns at most the last 5000 lines',
                             'served_sha256': sha256(text.encode('utf-8')), 'served_lines': len(lines_of(text)),
                             'original_lines': b.get('original_length')})
    if secret_hits(json.dumps(res)):
        problems.append('%s: secret-pattern hits in the result' % rid)
    ent['files'].append(dict(write('ci/%s/results.json' % rid, dumps(res)), kind='derived',
                             source_sha256=sha256(text.encode('utf-8'))))
    for g in gaps:
        missing.append(dict(g, id=eid, run_id=rid))
    if res['expected']['gate']['verdict'] is None:
        ent['notes'].append('no release-gate verdict line in the served lines')
    ent['citations'] = dedupe(citing(rid))
    entries.append(ent)

# the archive's own retained record files
own = []
for rel, srcp in (('build_archive.py', os.path.abspath(__file__)),
                  ('extract_result.py', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'extract_result.py')),
                  ('compare_result.py', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'compare_result.py')),
                  ('reproduce.py', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'reproduce.py')),
                  ('audit/offmain_audit.py', os.path.join(AUDITDIR, 'offmain_audit.py')),
                  ('audit/offmain_audit-output.txt', os.path.join(AUDITDIR, 'offmain_audit-output.txt')),
                  ('audit/audit.md', os.path.join(AUDITDIR, 'audit.md'))):
    data = open(srcp, 'rb').read()
    if secret_hits(data.decode('utf-8')):
        problems.append('%s: secret-pattern hits' % rel)
    own.append(dict(write(rel, data), kind='complete'))
entries.append({'id': 'tranche-record', 'kind': 'complete', 'files': own, 'citations': [],
                'provenance': {'source': 'written for this tranche: its build script, extractor, comparator and reproduction tool, '
                                         'and the off-main audit it acts on'}})

for e in entries:
    if e['citations']:
        attach_claims(e)

manifest = {
    'schema': 'oi-evidence-retention', 'version': 3, 'tranche': 1, 'base': BASE,
    'line_convention': 'lines are counted by splitting on newline characters; a text that ends without one has one '
                       'more line than wc -l reports',
    'kinds': {
        'complete-as-cited': 'byte-identical to the artifact the citing record names by digest; retained only where a frozen '
                             'record pins an artifact by digest',
        'complete': 'a file of this tranche, in full',
        'derived': 'a structured file read from a source that is not retained; source_sha256 is that source\'s digest, which '
                   'is provenance of the derivation, not independent proof',
    },
    'reproduction': {
        'rule': 'every results.json of kind "bridge" is an expected result reproducible at its run.head_sha by its reproduce '
                'recipe; reproduce.py performs it and compare_result.py decides it, failing closed on any mismatch, missing '
                'item or extraction failure; only deterministic results are compared',
        'verifier': ['verification/audits/evidence-retention/reproduce.py', 'verification/audits/evidence-retention/extract_result.py',
                     'verification/audits/evidence-retention/compare_result.py'],
        'workflow': '.github/workflows/reproduce-evidence.yml',
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
