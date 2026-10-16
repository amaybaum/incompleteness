#!/usr/bin/env python3
"""check_retention.py -- verifies the evidence-retention archive from the repository tree alone.

No git history, network or third-party package is used. From the repository root:

    python3 -I verification/audits/evidence-retention/check_retention.py           # check, exit 1 on any failure
    python3 -I verification/audits/evidence-retention/check_retention.py --self-test

Rules:
  R1  every listed file exists, and its size and sha256 are the recorded ones;
  R2  a "complete-as-cited" file has exactly the digest the citing record names, and that digest is one of the
      tokens its citations carry;
  R3  every citing file exists with its recorded git blob id (the historical record is unchanged), its cited line
      holds every recorded token, and every claim's text stands verbatim on the line it names;
  R4  an excerpt's ranges are non-empty, sorted, disjoint and within the served text, and name exactly its lines;
  R5  no file in the archive directory matches the secret patterns, an IPv4 address or an e-mail address;
  R6  every file in the archive directory is listed, or is README.md, manifest.json or this checker;
  R7  the manifest is well formed: known kinds and claim statuses, paths inside the archive, every entry but the
      tranche's own record cited, every citing location annotated, every gap naming an entry;
  R8  each CI entry's summary ("retains") is what its files say: run metadata, job counts per attempt, the
      release-gate block, each governed module's reported lines and status, cache lines and markers; every
      partial or missing set of axiom reports, and every missing job list, is a recorded gap; a BG-3 entry's
      run metadata names the run and head commit of its provenance;
  R9  coverage: every check-run attestation in the receipts the manifest names, and every run in the certificate
      attestation it names, has an entry whose run metadata matches it, and those files keep their blob ids.
The self-test mutates a copy once per failure message of these checks and requires that message.
The gap list is printed: a gap is recorded, not a failure. R1-R9 check the archive against itself and against the
tree. Whether a claim marked "retained" is carried by the files it names is a reading of those files; the claim
annotations name the files, so a reviewer can make that reading from the tree.
"""
import hashlib
import json
import os
import re
import shutil
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
FIXED = {'README.md', 'manifest.json', 'check_retention.py'}
SECRET = re.compile(r'gh[pousr]_[A-Za-z0-9]{20,}|github_pat[_]|AKIA[0-9A-Z]{16}|-{5}BEGIN|bearer [a-z0-9]'
                    r'|x-access-toke[n]|[?&](sig|signature|sv|se|token)=|passw(or)?d\s*[:=]|api[_-]?key\s*[:=]'
                    r'|private[_-]?key'
                    r'|(?<![\w.])(?:\d{1,3}\.){3}\d{1,3}(?![\w.])|[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}', re.I)
GATE_START = re.compile(r'^\S+ release gate$')
GATE_END = re.compile(r'^\S+ release gate: ')
GATE_STEP = re.compile(r'^\S+\s+(PASS|FAIL|SKIP)\s')
CACHE = re.compile(r'Cache (saved|hit|restored|not found)|Failed to (save|restore)')
MARKER = re.compile(r'error:|declaration uses .sorry.|sorryAx|Lean\.ofReduceBool')
RUN_URL = re.compile(r'/actions/runs/(\d+)(?:/attempts/(\d+))?')
RUN_KEYS = ('head_sha', 'event', 'status', 'conclusion', 'run_attempt', 'created_at')


def blob_id(data):
    return hashlib.sha1(b'blob %d\0' % len(data) + data).hexdigest()


def lines_of(text):
    ls = text.split('\n')
    return ls[:-1] if text.endswith('\n') else ls


def spans(nums):
    out = []
    for n in sorted(nums):
        if out and n == out[-1][1] + 1:
            out[-1][1] = n
        else:
            out.append([n, n])
    return out


def expand(sp):
    return {n for a, b in sp for n in range(a, b + 1)}


def inside(rel):
    return isinstance(rel, str) and bool(rel) and not os.path.isabs(rel) and '\\' not in rel and \
        os.path.normpath(rel) == rel and rel.split('/')[0] != '..'


def gate_summary(kept):
    block, on = [], False
    for l in kept:
        if GATE_START.match(l):
            block, on = [], True
        elif on:
            block.append(l)
            on = not GATE_END.match(l)
    steps = [GATE_STEP.match(l) for l in block]
    verdict = [l for l in block if GATE_END.match(l)]
    return {'steps': sum(1 for s in steps if s), 'pass': sum(1 for s in steps if s and s.group(1) == 'PASS'),
            'fail': sum(1 for s in steps if s and s.group(1) == 'FAIL'),
            'verdict': verdict[-1].split(' ', 1)[1] if verdict else None}


def check(archive, root):
    fails = []
    F = fails.append
    try:
        man = json.load(open(os.path.join(archive, 'manifest.json'), encoding='utf-8'))
    except (OSError, ValueError) as exc:
        return ['R7 manifest unreadable: %s' % exc], []
    if man.get('schema') != 'oi-evidence-retention' or man.get('version') != 2:
        return ['R7 manifest schema or version'], []
    kinds, statuses = set(man.get('kinds', {})), set(man.get('claim_status', {}))
    listed, ids, texts = set(), set(), {}

    def read_tree(path):
        p = os.path.join(root, path)
        return open(p, 'rb').read() if inside(path) and os.path.isfile(p) else None

    for e in man['entries']:
        eid = e.get('id')
        if not eid or eid in ids:
            F('R7 entry id %r missing or repeated' % eid)
        ids.add(eid)
        is_ci = 'kind' not in e and str(eid).startswith('ci-')
        if not is_ci and e.get('kind') not in kinds:
            F('R7 %s: unknown kind %r' % (eid, e.get('kind')))
        if not e.get('files'):
            F('R7 %s: no files' % eid)
        files = {}
        for f in e.get('files', []):
            rel = f.get('path', '')
            if not inside(rel):
                F('R7 %s: path %r is not inside the archive' % (eid, rel))
                continue
            if f.get('kind', e.get('kind')) not in kinds:
                F('R7 %s: %s has unknown kind %r' % (eid, rel, f.get('kind')))
            listed.add(rel)
            p = os.path.join(archive, rel)
            if not os.path.isfile(p):
                F('R1 %s: %s missing' % (eid, rel))
                continue
            data = open(p, 'rb').read()
            if len(data) != f.get('bytes'):
                F('R1 %s: %s size %d, recorded %r' % (eid, rel, len(data), f.get('bytes')))
            if hashlib.sha256(data).hexdigest() != f.get('sha256'):
                F('R1 %s: %s sha256 differs' % (eid, rel))
            files[rel] = texts[rel] = data.decode('utf-8', 'replace')
            if f.get('kind') == 'excerpt':
                src = f.get('source', {})
                rg, n = src.get('line_ranges') or [], src.get('served_lines')
                ok = bool(rg) and isinstance(n, int) and \
                    all(isinstance(r, list) and len(r) == 2 and 1 <= r[0] <= r[1] <= n for r in rg) and \
                    all(rg[i][1] < rg[i + 1][0] for i in range(len(rg) - 1))
                if not ok:
                    F('R4 %s: %s ranges are empty, unsorted, overlapping or outside the %r served lines' % (eid, rel, n))
                named = sum(b - a + 1 for a, b in rg if isinstance(a, int) and isinstance(b, int))
                if files[rel].count('\n') != named or not files[rel].endswith('\n'):
                    F('R4 %s: %s has %d lines, its ranges name %d' % (eid, rel, files[rel].count('\n'), named))
        cites = e.get('citations', [])
        if e.get('kind') != 'complete' and not cites:
            F('R7 %s: no citations' % eid)
        tokens = set()
        for c in cites:
            data = read_tree(c.get('path', ''))
            if data is None:
                F('R3 %s: citing file %s missing' % (eid, c.get('path')))
                continue
            if blob_id(data) != c.get('blob'):
                F('R3 %s: citing file %s changed (blob %s, recorded %s)' % (eid, c['path'], blob_id(data)[:12],
                                                                          str(c.get('blob'))[:12]))
            L = data.decode('utf-8', 'replace').split('\n')
            ln = c.get('line', 0)
            here = L[ln - 1] if isinstance(ln, int) and 0 < ln <= len(L) else None
            if not c.get('tokens'):
                F('R7 %s: %s:%s carries no token' % (eid, c['path'], ln))
            for t in c.get('tokens', []):
                tokens.add(t)
                if len(t) < 6:
                    F('R7 %s: token %r is too short to identify anything' % (eid, t))
                elif here is None or t not in here:
                    F('R3 %s: %s:%s no longer contains %s' % (eid, c['path'], ln, t[:16]))
            if not c.get('claims'):
                F('R7 %s: %s:%s has no claim annotation' % (eid, c['path'], ln))
            for k in c.get('claims') or []:
                n, t = k.get('line', 0), k.get('text', '')
                if len(t) < 3 or not (isinstance(n, int) and 0 < n <= len(L)) or t not in L[n - 1]:
                    F('R3 %s: claim %r is not verbatim at %s:%s' % (eid, t[:40], c['path'], n))
                if k.get('status') not in statuses:
                    F('R7 %s: claim status %r' % (eid, k.get('status')))
                if k.get('status') in ('retained', 'differs') and (not k.get('in') or not set(k['in']) <= set(files)):
                    F('R7 %s: claim %r names files %r outside the entry' % (eid, t[:40], k.get('in')))
                if k.get('status') == 'differs' and not k.get('note'):
                    F('R7 %s: a "differs" claim without a note' % eid)
        if e.get('kind') == 'complete-as-cited':
            f0 = (e.get('files') or [{}])[0]
            if f0.get('sha256') != e.get('cited_digest') or e.get('matches_cited_digest') is not True \
                    or e.get('cited_digest') not in tokens:
                F('R2 %s: not byte-identical to a digest its citations carry' % eid)
            pv = e.get('provenance', {})
            for rel, text in files.items():
                if rel.startswith('bg3/run-'):
                    run = json.loads(text)
                    if str(run.get('id')) != pv.get('run_id') or run.get('head_sha') != pv.get('head_sha') or \
                            rel != 'bg3/run-%s.json' % pv.get('run_id'):
                        F('R8 %s: %s differs from the entry\'s provenance' % (eid, rel))
        if is_ci:
            check_summary(e, files, man, F)
    for g in man.get('missing', []):
        if g.get('id') not in ids or not g.get('what') or not g.get('why'):
            F('R7 gap %r names no entry, or has no what/why' % g)
    check_coverage(man, archive, read_tree, F)
    for dirpath, _, names in os.walk(archive):
        for fn in names:
            rel = os.path.relpath(os.path.join(dirpath, fn), archive).replace(os.sep, '/')
            if '__pycache__' in rel:
                continue
            if rel not in listed and rel not in FIXED:
                F('R6 unlisted file %s' % rel)
            text = texts.get(rel)
            if text is None:
                text = open(os.path.join(dirpath, fn), 'rb').read().decode('utf-8', 'replace')
            hit = next((i + 1 for i, l in enumerate(text.split('\n')) if SECRET.search(l)), None)
            if hit:
                F('R5 %s:%d matches a secret pattern' % (rel, hit))
    return fails, man.get('missing', [])


def check_summary(e, files, man, F):
    eid, rid, R = e['id'], e.get('run_id'), e.get('retains', {})
    gaps = {(g.get('id'), g.get('what')) for g in man.get('missing', [])}
    run = files.get('ci/%s/run.json' % rid)
    if run is None:
        F('R8 %s: no run.json' % eid)
        return
    run = json.loads(run)
    if str(run.get('id')) != rid or run.get('run_id') != rid or R.get('run') != {k: run.get(k) for k in RUN_KEYS}:
        F('R8 %s: run summary differs from run.json' % eid)
    exf = next((f for f in e['files'] if f.get('kind') == 'excerpt'), None)
    jobs = files.get('ci/%s/jobs.json' % rid)
    if jobs is None:
        if R.get('jobs') is not None or (eid, 'job list') not in gaps:
            F('R8 %s: no jobs.json, and its absence is not a recorded gap' % eid)
    else:
        per, jl = {}, json.loads(jobs)['jobs']
        for x in jl:
            p = per.setdefault(str(x['run_attempt']), {'jobs': 0, 'conclusions': {}})
            p['jobs'] += 1
            p['conclusions'][str(x['conclusion'])] = p['conclusions'].get(str(x['conclusion']), 0) + 1
            if x['head_sha'] != run.get('head_sha'):
                F('R8 %s: job %s head_sha differs from the run' % (eid, x['id']))
        if R.get('jobs') != per:
            F('R8 %s: job summary differs from jobs.json' % eid)
        if exf and not any(str(x['id']) == exf['source'].get('job_id') and x['name'] == 'Mathlib bridge'
                           and x['run_attempt'] == run.get('run_attempt') for x in jl):
            F('R8 %s: the excerpt is not from attempt %s\'s Mathlib bridge job' % (eid, run.get('run_attempt')))
    kept = lines_of(files.get(exf['path'], '')) if exf else []
    if not exf:
        F('R8 %s: no excerpt' % eid)
        return
    if R.get('gate') != gate_summary(kept):
        F('R8 %s: gate summary differs from the excerpt' % eid)
    if R.get('cache') != [l[29:] for l in kept if CACHE.search(l)] or \
            R.get('markers') != sum(1 for l in kept if MARKER.search(l)):
        F('R8 %s: cache lines or marker count differ from the excerpt' % eid)
    if sorted(m.get('module') for m in R.get('modules', [])) != sorted(exf['source'].get('modules', [])):
        F('R8 %s: module list differs from the excerpt\'s' % eid)
    for m in R.get('modules', []):
        rr = re.compile(r' %s:(\d+):\d+: .*?(depends on axioms|does not depend on any axioms)' % re.escape(m['module']))
        rep = {int(rr.search(l).group(1)) for l in kept if rr.search(l)}
        if spans(rep) != m.get('reported_lines') or len(rep) != m.get('reported'):
            F('R8 %s: %s reported lines differ from the excerpt' % (eid, m['module']))
        has_src = 'print_lines' in m
        pl = expand(m.get('print_lines', []))
        want = ('complete' if pl == rep else 'partial' if rep else 'none') if has_src else 'absent'
        if m.get('status') != want or (rep - pl if has_src else rep) or (has_src and m.get('prints') != len(pl)):
            F('R8 %s: %s status %r, the lines give %r' % (eid, m['module'], m.get('status'), want))
        if ((eid, 'axiom reports of %s' % m['module']) in gaps) != (want in ('partial', 'none')):
            F('R8 %s: %s is %s, and its gap record is %s' % (eid, m['module'], want,
                                                         'present' if want not in ('partial', 'none') else 'absent'))


def check_coverage(man, archive, read_tree, F):
    cov = man.get('coverage', {}).get('files', [])
    if not cov:
        F('R9 the manifest names no coverage files')
    by_run = {e.get('run_id'): e for e in man['entries'] if e.get('run_id')}

    def run_of(rid):
        p = os.path.join(archive, 'ci', str(rid), 'run.json')
        if rid not in by_run or 'ci/%s/run.json' % rid not in {f['path'] for f in by_run[rid]['files']} or \
                not os.path.isfile(p):
            return None
        return json.load(open(p, encoding='utf-8'))

    for c in cov:
        data = read_tree(c['path'])
        if data is None or blob_id(data) != c['blob']:
            F('R9 coverage file %s missing or changed' % c['path'])
            continue
        doc = json.loads(data)
        if c['path'].startswith('verification/receipts/'):
            for a in doc.get('attestations', []):
                if a.get('kind') != 'check-run':
                    continue
                m = RUN_URL.search(a['record'])
                rid = m and m.group(1)
                run = run_of(rid) if m else None
                if run is None:
                    F('R9 %s %s: check run %s has no entry' % (doc.get('round'), a.get('subject'), rid))
                elif run.get('head_sha') != a['commit'] or (m.group(2) and int(m.group(2)) != run.get('run_attempt')):
                    F('R9 %s %s: run %s is at %s attempt %s; attested %s attempt %s' % (
                        doc.get('round'), a['subject'], rid, str(run.get('head_sha'))[:12], run.get('run_attempt'),
                        a['commit'][:12], m.group(2)))
                elif not any(r.get('round') == doc.get('round') and r.get('subject') == a['subject']
                             and r.get('commit') == a['commit'] for r in by_run[rid].get('roles', [])):
                    F('R9 %s %s: the entry for run %s does not record this role' % (doc.get('round'), a['subject'], rid))
        else:
            for role, v in doc.get('ci', {}).items():
                run = run_of(v['run'])
                if run is None or run.get('head_sha') != v['head_sha'] or run.get('conclusion') != v['conclusion']:
                    F('R9 %s %s: run %s has no matching entry' % (doc.get('round'), role, v['run']))


def report(archive, root):
    fails, gaps = check(archive, root)
    man = json.load(open(os.path.join(archive, 'manifest.json'), encoding='utf-8'))
    nfiles = sum(len(e.get('files', [])) for e in man['entries'])
    cites = [(e['id'], c) for e in man['entries'] for c in e.get('citations', [])]
    st = {}
    for _, c in cites:
        for k in c.get('claims', []):
            st[k.get('status')] = st.get(k.get('status'), 0) + 1
    print('RETENTION  %d entries, %d archived files, %d citing locations, %d claims (%s)' % (
        len(man['entries']), nfiles, len(cites), sum(st.values()),
        ', '.join('%d %s' % (v, k) for k, v in sorted(st.items()))))
    for g in gaps:
        print('GAP  %s' % json.dumps(g, sort_keys=True))
    for eid, c in cites:
        for k in c.get('claims', []):
            if k.get('status') in ('not retained', 'differs'):
                print('%s  %s  %s:%d  %r%s' % ('DIFFERS' if k['status'] == 'differs' else 'NOT RETAINED', eid, c['path'],
                                              k['line'], k['text'], ': ' + k['note'] if k.get('note') else ''))
    for f in fails:
        print('FAIL  %s' % f)
    print('RETENTION  %s (%d failure(s), %d gap(s))' % ('HOLDS' if not fails else 'FAILS', len(fails), len(gaps)))
    return 0 if not fails else 1


def self_test(archive, root):
    """Each mutation must be reported by the check it targets, identified by that check's own message; the
    unmutated copy must pass. Every failure message of check() has a mutation here."""
    man = json.load(open(os.path.join(archive, 'manifest.json'), encoding='utf-8'))
    ok = True
    with tempfile.TemporaryDirectory() as tmp:
        troot = os.path.join(tmp, 'root')
        tarch = os.path.join(troot, 'archive')
        shutil.copytree(archive, tarch, ignore=shutil.ignore_patterns('__pycache__'))
        need = {c['path'] for e in man['entries'] for c in e.get('citations', [])} | \
            {c['path'] for c in man['coverage']['files']}
        for rel in need:
            dst = os.path.join(troot, rel)
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.copyfile(os.path.join(root, rel), dst)
        mp = os.path.join(tarch, 'manifest.json')
        morig = open(mp, 'rb').read()

        def expect(name, mutate, restore, rule=None, msg=''):
            nonlocal ok
            mutate()
            fails, _ = check(tarch, troot)
            restore()
            good = (not fails) if rule is None else any(f.startswith(rule + ' ') and msg in f for f in fails)
            ok &= good
            print('%s self: %s%s' % ('PASS' if good else 'FAIL', name, '' if rule is None else ' (%s)' % rule))
            if not good:
                print('      got: %s' % (fails[:3],))

        def edit(fn):
            def go():
                m = json.loads(morig)
                fn(m)
                open(mp, 'w', encoding='utf-8').write(json.dumps(m))
            return go
        back = lambda: open(mp, 'wb').write(morig)

        def file_edit(path, fn):
            orig = open(path, 'rb').read()
            return (lambda: open(path, 'wb').write(fn(orig))), (lambda: open(path, 'wb').write(orig))

        def json_edit(path, fn):
            def change(b):
                d = json.loads(b)
                fn(d)
                return json.dumps(d).encode('utf-8')
            return file_edit(path, change)

        noop = lambda: None
        ents = man['entries']
        idx = lambda pred: next(i for i, e in enumerate(ents) if pred(e))
        ci = idx(lambda e: e.get('retains', {}).get('jobs'))
        nojobs = idx(lambda e: 'retains' in e and e['retains'].get('jobs') is None)
        cac = idx(lambda e: e.get('kind') == 'complete-as-cited' and len(e['citations']) == 1)
        bgr = idx(lambda e: any(f['path'].startswith('bg3/run-') for f in e['files']))
        part = idx(lambda e: any(m['status'] == 'partial' for m in e.get('retains', {}).get('modules', [])))
        cert = idx(lambda e: any(r.get('kind') == 'V2 certificate' for r in e.get('roles', [])))
        rec = idx(lambda e: any(r.get('kind') == 'receipt check-run' for r in e.get('roles', [])))
        e_ci = ents[ci]
        rid = e_ci['run_id']
        exj = next(j for j, f in enumerate(e_ci['files']) if f.get('kind') == 'excerpt')
        runj = next(j for j, f in enumerate(e_ci['files']) if f['path'].endswith('/run.json'))
        xp = os.path.join(tarch, e_ci['files'][exj]['path'])
        cp = os.path.join(troot, e_ci['citations'][0]['path'])
        ret = next((j, k) for j, c in enumerate(e_ci['citations']) for k, x in enumerate(c['claims'])
                   if x['status'] == 'retained')
        pmod = next(m['module'] for m in ents[part]['retains']['modules'] if m['status'] == 'partial')
        X = lambda m: m['entries'][ci]['files'][exj]
        C0 = lambda m: m['entries'][ci]['citations'][0]
        RC = lambda m: m['entries'][ci]['citations'][ret[0]]['claims'][ret[1]]

        expect('unmutated copy passes', noop, noop)
        # manifest form (R7)
        expect('an unreadable manifest', *file_edit(mp, lambda b: b[:-2]), rule='R7', msg='manifest unreadable')
        expect('a manifest of another version', edit(lambda m: m.__setitem__('version', 1)), back, 'R7', 'schema or version')
        expect('a repeated entry id', edit(lambda m: m['entries'][nojobs].__setitem__('id', e_ci['id'])), back, 'R7',
               'missing or repeated')
        expect('an unknown entry kind', edit(lambda m: m['entries'][cac].__setitem__('kind', 'complete-ish')), back, 'R7',
               ': unknown kind')
        expect('an entry with no files', edit(lambda m: m['entries'][cac].__setitem__('files', [])), back, 'R7', 'no files')
        expect('a listed path outside the archive', edit(lambda m: m['entries'][ci]['files'].append(
            {'path': '../x', 'bytes': 0, 'sha256': '', 'kind': 'derived'})), back, 'R7', 'not inside the archive')
        expect('a file of unknown kind', edit(lambda m: m['entries'][ci]['files'][runj].__setitem__('kind', 'derived-ish')),
               back, 'R7', 'has unknown kind')
        expect('a CI entry with no citations', edit(lambda m: m['entries'][ci].__setitem__('citations', [])), back, 'R7',
               'no citations')
        expect('a citation with no token', edit(lambda m: C0(m).__setitem__('tokens', [])), back, 'R7', 'carries no token')
        expect('a token too short to identify anything', edit(lambda m: C0(m)['tokens'].append('abc')), back, 'R7',
               'too short')
        expect('a citing location with no claim annotation', edit(lambda m: C0(m).pop('claims')), back, 'R7',
               'no claim annotation')
        expect('an unknown claim status', edit(lambda m: C0(m)['claims'][0].__setitem__('status', 'proved')), back, 'R7',
               'claim status')
        expect('a retained claim naming a file outside the entry', edit(lambda m: RC(m).__setitem__('in', ['bg3/none.log'])),
               back, 'R7', 'outside the entry')
        expect('a "differs" claim without a note', edit(lambda m: (RC(m).__setitem__('status', 'differs'), RC(m).pop('note', None))),
               back, 'R7', 'without a note')
        expect('a gap that names no entry', edit(lambda m: m['missing'].append({'id': 'nowhere', 'what': 'x', 'why': 'y'})),
               back, 'R7', 'names no entry')
        # files (R1, R2, R4, R5, R6)
        expect('a flipped byte in an archived file', *file_edit(xp, lambda b: bytes([b[0] ^ 1]) + b[1:]), rule='R1',
               msg='sha256 differs')
        expect('a removed archived file', lambda: os.rename(xp, xp + '.x'), lambda: os.rename(xp + '.x', xp), 'R1', 'missing')
        expect('a recorded size that differs', edit(lambda m: X(m).__setitem__('bytes', X(m)['bytes'] + 1)), back, 'R1', 'size')
        expect('a complete-as-cited entry whose match flag is false',
               edit(lambda m: m['entries'][cac].__setitem__('matches_cited_digest', False)), back, 'R2', 'not byte-identical')

        def drop_digest(m):
            c = m['entries'][cac]['citations'][0]
            c['tokens'] = [t for t in c['tokens'] if t != m['entries'][cac]['cited_digest']] or [m['entries'][cac]['files'][0]['path']]
        expect('a complete-as-cited digest that no citation carries', edit(drop_digest), back, 'R2', 'not byte-identical')

        def shift_out(m):
            s = X(m)['source']
            a, b = s['line_ranges'][-1]
            s['line_ranges'][-1] = [s['served_lines'] + 1, s['served_lines'] + 1 + b - a]
        expect('an excerpt range beyond the served text, line count unchanged', edit(shift_out), back, 'R4', 'ranges are empty')

        def overlap(m):
            s = X(m)['source']
            n = sum(b - a + 1 for a, b in s['line_ranges'])
            s['line_ranges'] = [[1, n + 1], [100, 98]]
        expect('malformed ranges whose total equals the line count', edit(overlap), back, 'R4', 'ranges are empty')
        expect('an excerpt with one line more than its ranges name', *file_edit(xp, lambda b: b + b'extra\n'), rule='R4',
               msg='its ranges name')
        expect('a token pattern in an archived file', *file_edit(xp, lambda b: b + b'ghp_' + b'A' * 36 + b'\n'), rule='R5',
               msg='secret pattern')
        expect('an IPv4 address in an archived file', *file_edit(xp, lambda b: b + b'connect 10.1.2' + b'.3 refused\n'),
               rule='R5', msg='secret pattern')
        expect('an e-mail address in an archived file',
               *file_edit(xp, lambda b: b + b'author someone' + b'@' + b'example.org\n'), rule='R5', msg='secret pattern')
        expect('a secret pattern in the README',
               *file_edit(os.path.join(tarch, 'README.md'), lambda b: b + b'ghp_' + b'B' * 36 + b'\n'), rule='R5',
               msg='README.md')
        extra = os.path.join(tarch, 'ci', 'unlisted.txt')
        expect('an unlisted file in the archive', lambda: open(extra, 'w').write('x'), lambda: os.remove(extra), 'R6', 'unlisted')
        # citing files (R3)
        expect('a changed historical record', *file_edit(cp, lambda b: b + b'\n'), rule='R3', msg='changed (blob')
        expect('a removed historical record', lambda: os.rename(cp, cp + '.x'), lambda: os.rename(cp + '.x', cp), 'R3',
               'citing file')
        expect('a recorded token absent from its line', edit(lambda m: C0(m)['tokens'].append('Z' * 12)), back, 'R3',
               'no longer contains')
        expect('a claim whose text is not on its line', edit(lambda m: C0(m)['claims'][0].__setitem__('text', 'Z' * 12)),
               back, 'R3', 'not verbatim')
        # summaries (R8)
        expect('a BG-3 entry whose provenance names another head commit',
               edit(lambda m: m['entries'][bgr]['provenance'].__setitem__('head_sha', '0' * 40)), back, 'R8',
               'differs from the entry\'s provenance')
        expect('a CI entry without run.json', edit(lambda m: m['entries'][ci]['files'].pop(runj)), back, 'R8', 'no run.json')
        expect('a run summary that contradicts run.json',
               edit(lambda m: m['entries'][ci]['retains']['run'].__setitem__('conclusion', 'failure')), back, 'R8',
               'run summary differs')
        expect('a missing job list that is not a recorded gap', edit(lambda m: m.__setitem__('missing', [
            g for g in m['missing'] if not (g['id'] == ents[nojobs]['id'] and g['what'] == 'job list')])), back, 'R8',
               'not a recorded gap')
        jp = os.path.join(tarch, 'ci', rid, 'jobs.json')
        expect('a job at another head commit',
               *json_edit(jp, lambda d: d['jobs'][0].__setitem__('head_sha', '0' * 40)), rule='R8', msg='head_sha differs')
        expect('a job summary that contradicts jobs.json',
               edit(lambda m: m['entries'][ci]['retains'].__setitem__('jobs', {'9': {'jobs': 1, 'conclusions': {}}})), back,
               'R8', 'job summary differs')
        expect('an excerpt from another job', edit(lambda m: X(m)['source'].__setitem__('job_id', '1')), back, 'R8',
               'is not from attempt')
        expect('a CI entry without an excerpt', edit(lambda m: m['entries'][ci]['files'].pop(exj)), back, 'R8', 'no excerpt')
        expect('a gate summary that contradicts the excerpt',
               edit(lambda m: m['entries'][ci]['retains']['gate'].__setitem__('pass', -1)), back, 'R8', 'gate summary')
        expect('a marker count that contradicts the excerpt',
               edit(lambda m: m['entries'][ci]['retains'].__setitem__('markers', -1)), back, 'R8', 'marker count')
        expect('a module list that differs from the excerpt\'s',
               edit(lambda m: X(m)['source']['modules'].append('OIBridge/None.lean')), back, 'R8', 'module list')
        expect('a module\'s reported count that contradicts the excerpt',
               edit(lambda m: m['entries'][part]['retains']['modules'][0].__setitem__(
                   'reported', m['entries'][part]['retains']['modules'][0]['reported'] + 1)), back, 'R8',
               'reported lines differ')
        expect('a partial module recorded as complete',
               edit(lambda m: [x.__setitem__('status', 'complete') for x in m['entries'][part]['retains']['modules']
                               if x['status'] == 'partial']), back, 'R8', 'the lines give')
        expect('a partial module whose gap record is removed', edit(lambda m: m.__setitem__('missing', [
            g for g in m['missing'] if not (g['id'] == ents[part]['id'] and g['what'] == 'axiom reports of %s' % pmod)])),
               back, 'R8', 'its gap record is absent')
        # coverage (R9)
        expect('a manifest that names no coverage files', edit(lambda m: m['coverage'].__setitem__('files', [])), back, 'R9',
               'no coverage files')
        expect('a coverage file whose blob changed',
               *file_edit(os.path.join(troot, man['coverage']['files'][0]['path']), lambda b: b + b' '), rule='R9',
               msg='missing or changed')

        def drop(i):
            def go(m):
                eid = m['entries'][i]['id']
                m['entries'].pop(i)
                m['missing'] = [g for g in m['missing'] if g.get('id') != eid]
            return go
        expect('an attested check run with no entry', edit(drop(rec)), back, 'R9', 'has no entry')
        rp = os.path.join(tarch, 'ci', ents[rec]['run_id'], 'run.json')
        expect('an attested run whose metadata names another head',
               *json_edit(rp, lambda d: d.__setitem__('head_sha', '0' * 40)), rule='R9', msg='attested')
        expect('an entry that does not record its attested role', edit(lambda m: m['entries'][rec].__setitem__(
            'roles', [r for r in m['entries'][rec]['roles'] if r.get('kind') != 'receipt check-run'])), back, 'R9',
               'does not record this role')
        expect('a certificate run with no entry', edit(drop(cert)), back, 'R9', 'no matching entry')
    print('self-test: %s' % ('OK' if ok else 'FAILED'))
    return 0 if ok else 1


if __name__ == '__main__':
    root = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
    if sys.argv[1:] == ['--self-test']:
        sys.exit(self_test(HERE, root))
    if sys.argv[1:]:
        print(__doc__)
        sys.exit(2)
    sys.exit(report(HERE, root))
