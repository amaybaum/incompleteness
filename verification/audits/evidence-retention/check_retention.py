#!/usr/bin/env python3
"""check_retention.py -- verifies the evidence-retention archive from the repository tree alone.

No network or third-party package is used, and the check uses no git history. From the repository root:

    python3 -I verification/audits/evidence-retention/check_retention.py           # check, exit 1 on any failure
    python3 -I verification/audits/evidence-retention/check_retention.py --self-test
    python3 -I verification/audits/evidence-retention/check_retention.py --later-provenance   # R10, uses git
    python3 -I verification/audits/evidence-retention/check_retention.py --module-sets   # R11, uses git
    python3 -I verification/audits/evidence-retention/check_retention.py --gate   # the release-gate step, uses git

Rules:
  R1  every listed file exists, and its size and sha256 are the recorded ones;
  R2  a "complete-as-cited" file has exactly the digest the citing record names, and that digest is one of the
      tokens its citations carry;
  R3  every citing file exists with its recorded git blob id (the historical record is unchanged), its cited line
      holds every recorded token, and every claim's text stands verbatim on the line it names;
  R4  every results.json is well formed: its schema, its run (id and head commit equal to the entry's run.json, and
      its job the Mathlib bridge job of the attested attempt), a recorded build, a gate with steps and a verdict,
      every governed module with a status consistent with its reports and #print axioms lines, every report's
      axioms a list or null, marker counts for every marker, and the reproduction recipe;
  R5  no file in the archive directory matches the secret patterns, an IPv4 address or an e-mail address;
  R6  every file in the archive directory is listed, or is README.md, manifest.json or this checker;
  R7  the manifest is well formed: known kinds and claim statuses, paths inside the archive, every entry but the
      tranche's own record cited and only it uncited, every citing location annotated, every gap naming an entry;
  R8  each CI entry's files agree: every job in jobs.json is at the run's head commit; every partial or
      missing set of axiom reports, and every missing job list, is a recorded gap; a BG-3 entry's results and
      run metadata name the run, job and head commit of its provenance, and its results derive from its log;
  R9  coverage, recomputed from the tree: every receipt, and every certificate attestation citing runs, is
      covered or named as later than this tranche, and every one an entry cites is covered; every check-run
      attestation in a covered receipt, and every run of a covered certificate attestation, has an entry whose
      run metadata matches it; and covered files keep their blob ids. A path named as later must say where its
      evidence is retained, and may be neither covered nor cited by the tranche;
  R10 (with git history) the tranche base is in the repository and an ancestor of HEAD, and no path named as
      later existed at the base: the tree cannot order commits, so this is the independent check that a receipt
      named as later did land after this tranche. In history mode (--gate) R9's scope is read from git instead of
      the tree: every receipt, and every certificate attestation citing runs, that existed at the base must be
      covered, nothing else may be, and a receipt landed after the base is out of scope without a declaration.
  R11 (with git history; run by --module-sets and --gate) every expected result's module table is the set of Lean
      modules its run's rounds govern, re-derived from the rounds' records rather than from the archive. The
      receipts and certificate attestations at the tranche base name the rounds that attest each run and the
      commit each attests, which must be the expected result's. For a receipt, each control-plane file is read at
      that commit and must be the blob the receipt pins; their one v3-governed-paths block, parsed here from S7
      and G10 of the V3 specification, must hash to the receipt's governed_paths_digest; and its paths under
      verification/lean-mathlib/ ending in .lean are the governed modules. For a certificate attestation, the
      certificate is read at that commit and must be the blob the attestation pins, and the Lean modules among its
      contributions are the governed ones. A governed directory inside verification/lean-mathlib/, or one
      containing it, fails the check: it fixes no module set.
      The table must equal the union over the run's rounds. Expected results of a run no covered file attests
      (BG-3's design trees, at commits off main) are listed as outside its scope.
      R11 is a consistency check, not an independent derivation: build_archive.py read the module sets from the
      same governed-paths blocks, at the tranche base and with its own parser. R11 shows that the archive applied
      those blocks faithfully, as they stand at each run's commit and as the receipts' digests commit to them; it
      cannot show that the governed paths name the right modules.
The self-test mutates a copy once per failure message of these checks and requires that message; its R10 and R11
cases read the repository's history, and the self-test fails when that history is absent.
The gap list is printed: a gap is recorded, not a failure. R1-R9 check the archive against itself and against the
tree; they do not re-derive an expected result, which reproduce.py does at the commit, and R11 re-derives only
its module set. Whether a claim marked "retained" is carried by the files it names is a reading of those files;
the claim annotations name the files, so a reviewer can make that reading from the tree.
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
RUN_URL = re.compile(r'/actions/runs/(\d+)(?:/attempts/(\d+))?')
MARKERS = ('sorryAx', 'Lean.ofReduceBool', "declaration uses 'sorry'", 'error:')
STATUSES = ('complete', 'partial', 'none', 'absent')


def blob_id(data):
    return hashlib.sha1(b'blob %d\0' % len(data) + data).hexdigest()


def inside(rel):
    return isinstance(rel, str) and bool(rel) and not os.path.isabs(rel) and '\\' not in rel and \
        os.path.normpath(rel) == rel and rel.split('/')[0] != '..'


def check(archive, root, scope=None):
    fails = []
    F = fails.append
    try:
        man = json.load(open(os.path.join(archive, 'manifest.json'), encoding='utf-8'))
    except (OSError, ValueError) as exc:
        return ['R7 manifest unreadable: %s' % exc], []
    if man.get('schema') != 'oi-evidence-retention' or man.get('version') != 3:
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
            if rel.endswith('/results.json') or (rel.startswith('bg3/results-') and rel.endswith('.json')):
                check_results(eid, rel, files[rel], e, F)
        cites = e.get('citations', [])
        if e.get('kind') != 'complete' and not cites:
            F('R7 %s: no citations' % eid)
        if e.get('kind') == 'complete' and cites:
            F('R7 %s: a "complete" entry carries citations' % eid)
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
                if rel.startswith('bg3/results-'):
                    try:
                        rr = json.loads(text).get('run') or {}
                    except ValueError:
                        rr = {}
                    fr = next((f for f in e['files'] if f['path'] == rel), {})
                    if rr.get('id') != pv.get('run_id') or rr.get('head_sha') != pv.get('head_sha') or rr.get('job_id') != pv.get('job_id') \
                            or rel != 'bg3/results-%s.json' % pv.get('job_id') or fr.get('source_sha256') != f0.get('sha256'):
                        F('R8 %s: %s names another run, job or head commit than the entry, or does not derive from its log' % (eid, rel))
        if is_ci:
            check_entry_files(e, files, man, F)
    for g in man.get('missing', []):
        if g.get('id') not in ids or not g.get('what') or not g.get('why'):
            F('R7 gap %r names no entry, or has no what/why' % g)
    check_coverage(man, archive, root, read_tree, F, scope)
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


def check_results(eid, rel, text, e, F):
    """R4: a results.json is well formed and names what its entry names."""
    try:
        r = json.loads(text)
    except ValueError:
        F('R4 %s: %s is not JSON' % (eid, rel))
        return
    if r.get('schema') != 'oi-evidence-result' or r.get('version') != 1 or r.get('kind') not in ('bridge', 'design-diagnostic'):
        F('R4 %s: %s has an unknown schema, version or kind' % (eid, rel))
        return
    run, exp = r.get('run') or {}, r.get('expected') or {}
    if not run.get('id') or not re.fullmatch(r'[0-9a-f]{40}', str(run.get('head_sha', ''))) or not run.get('job_id'):
        F('R4 %s: %s names no run, head commit or job' % (eid, rel))
    if r['kind'] == 'design-diagnostic':
        if not exp.get('sha256sum_ok') or not exp.get('checks') or not (r.get('reproduce') or {}).get('recipe'):
            F('R4 %s: %s records no checks or no recipe' % (eid, rel))
        return
    if not r.get('source', {}).get('extractor') or not (r.get('reproduce') or {}).get('recipe'):
        F('R4 %s: %s records no extractor or no reproduction recipe' % (eid, rel))
    if exp.get('build_success') is not True:
        F('R4 %s: %s records no successful build' % (eid, rel))
    g = exp.get('gate') or {}
    if not g.get('verdict') or not g.get('steps') or any(not st.get('name') or st.get('status') not in ('PASS', 'FAIL', 'SKIP')
                                                           for st in g.get('steps', [])):
        F('R4 %s: %s records no gate verdict or malformed gate steps' % (eid, rel))
    mods = exp.get('modules')
    if not isinstance(mods, dict):
        F('R4 %s: %s has no module table' % (eid, rel))
        mods = {}
    for mod, m in mods.items():
        st, reps = m.get('status'), m.get('reports')
        if st not in STATUSES or not isinstance(reps, list):
            F('R4 %s: %s module %s has status %r' % (eid, rel, mod, st))
            continue
        for rp in reps:
            if not rp.get('name') or not isinstance(rp.get('line'), int) or not (rp.get('axioms') is None or isinstance(rp['axioms'], list)):
                F('R4 %s: %s module %s has a malformed report' % (eid, rel, mod))
        lines = {rp.get('line') for rp in reps}
        if st == 'absent':
            if reps or m.get('prints') is not None:
                F('R4 %s: %s module %s is absent but has reports or prints' % (eid, rel, mod))
            continue
        pl = {n for a, b in (m.get('print_lines') or []) for n in range(a, b + 1)}
        if not isinstance(m.get('prints'), int) or m['prints'] != len(pl) or not lines <= pl:
            F('R4 %s: %s module %s has reports outside its #print axioms lines, or a wrong count' % (eid, rel, mod))
            continue
        want = 'complete' if lines == pl else 'partial' if lines else 'none'
        if st != want:
            F('R4 %s: %s module %s is recorded as %s, its lines give %s' % (eid, rel, mod, st, want))
    mk = exp.get('markers') or {}
    if any(k not in mk or not isinstance(mk[k], int) for k in MARKERS):
        F('R4 %s: %s records no count for every marker' % (eid, rel))


def check_entry_files(e, files, man, F):
    """R8: a CI entry's files agree with each other and with the gap list."""
    eid, rid = e['id'], e.get('run_id')
    gaps = {(g.get('id'), g.get('what')) for g in man.get('missing', [])}
    run = files.get('ci/%s/run.json' % rid)
    res = files.get('ci/%s/results.json' % rid)
    if run is None or res is None:
        F('R8 %s: no run.json or no results.json' % eid)
        return
    try:
        run, res = json.loads(run), json.loads(res)
    except ValueError:
        F('R8 %s: run.json or results.json is not JSON' % eid)
        return
    rr = res.get('run') or {}
    if str(run.get('id')) != rid or run.get('run_id') != rid or rr.get('id') != rid or rr.get('head_sha') != run.get('head_sha') \
            or rr.get('attempt') != run.get('run_attempt'):
        F('R8 %s: results.json names another run, head commit or attempt than run.json' % eid)
    jobs = files.get('ci/%s/jobs.json' % rid)
    if jobs is None:
        if (eid, 'job list') not in gaps:
            F('R8 %s: no jobs.json, and its absence is not a recorded gap' % eid)
    else:
        try:
            jl = json.loads(jobs)['jobs']
        except (ValueError, KeyError, TypeError):
            F('R8 %s: jobs.json is not a job list' % eid)
            jl = []
        for x in jl:
            if x['head_sha'] != run.get('head_sha'):
                F('R8 %s: job %s head_sha differs from the run' % (eid, x['id']))
        if not any(str(x['id']) == rr.get('job_id') and x['name'] == 'Mathlib bridge' and x['run_attempt'] == run.get('run_attempt')
                   for x in jl):
            F('R8 %s: the results are not from attempt %s\'s Mathlib bridge job' % (eid, run.get('run_attempt')))
    for mod, m in ((res.get('expected') or {}).get('modules') or {}).items():
        want = m.get('status') in ('partial', 'none')
        if ((eid, 'axiom reports of %s' % mod) in gaps) != want:
            F('R8 %s: %s is %s, and its gap record is %s' % (eid, mod, m.get('status'), 'present' if not want else 'absent'))


def check_coverage(man, archive, root, read_tree, F, scope=None):
    cov = man.get('coverage', {}).get('files', [])
    if not cov:
        F('R9 the manifest names no coverage files')
    by_run = {e.get('run_id'): e for e in man['entries'] if e.get('run_id')}
    listed = {c['path'] for c in cov}
    for p in sorted({c.get('path', '') for e in man['entries'] for c in e.get('citations', [])}):
        if p.startswith(('verification/receipts/', 'verification/certificates/attestations/')) and p not in listed:
            F('R9 cited file %s is not in the coverage list' % p)
    # the files to cover, recomputed from the tree: every receipt, and every certificate attestation citing runs
    later = {c.get('path') for c in man.get('coverage', {}).get('later', [])}
    cited = {c.get('path', '') for e in man['entries'] for c in e.get('citations', [])}
    for c in man.get('coverage', {}).get('later', []):
        if c.get('path') in listed:
            F('R9 %s is named both as covered and as later' % c.get('path'))
        if c.get('path') in cited:
            F('R9 %s is named as later, but the tranche cites it' % c.get('path'))
        if not c.get('evidence'):
            F('R9 %s is named as later without where its evidence is retained' % c.get('path'))
    in_tree = []
    rdir = os.path.join(root, 'verification', 'receipts')
    adir = os.path.join(root, 'verification', 'certificates', 'attestations')
    if os.path.isdir(rdir):
        in_tree += ['verification/receipts/' + f for f in sorted(os.listdir(rdir)) if f.endswith('.json')]
    if os.path.isdir(adir):
        for f in sorted(os.listdir(adir)):
            if f.endswith('.json'):
                d = json.load(open(os.path.join(adir, f), encoding='utf-8'))
                if any(isinstance(v, dict) and v.get('run') for v in (d.get('ci') or {}).values()):
                    in_tree.append('verification/certificates/attestations/' + f)
    if scope is None:
        for p in in_tree:
            if p not in listed and p not in later:
                F('R9 %s is in the tree but neither covered nor named as later than this tranche' % p)
    else:
        for p in sorted(scope):
            if p not in listed:
                F('R10 %s existed at the tranche base but is not covered' % p)
        for p in sorted(listed):
            if p not in scope:
                F('R10 covered file %s did not exist at the tranche base' % p)

    def run_of(rid):
        p = os.path.join(archive, 'ci', str(rid), 'run.json')
        if rid not in by_run or 'ci/%s/run.json' % rid not in {f['path'] for f in by_run[rid]['files']} or \
                not os.path.isfile(p):
            return None
        try:
            return json.load(open(p, encoding='utf-8'))
        except ValueError:
            return None

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


def later_provenance(man, root, later=None, head='HEAD'):
    """R10, which reads git history: no path named as later existed at the tranche base."""
    import subprocess
    base, fails = man.get('base', ''), []
    git = lambda *a: subprocess.run(['git', '-C', root] + list(a), capture_output=True).returncode
    if git('cat-file', '-e', base + '^{commit}') != 0:
        return ['R10 the tranche base %s is not in the repository' % base[:12]]
    if git('merge-base', '--is-ancestor', base, head) != 0:
        fails.append('R10 the tranche base %s is not an ancestor of %s' % (base[:12], head))
    for c in (man.get('coverage', {}).get('later', []) if later is None else later):
        if git('cat-file', '-e', '%s:%s' % (base, c.get('path'))) == 0:
            fails.append('R10 %s existed at the tranche base %s, so it is not later' % (c.get('path'), base[:12]))
    return fails


def base_scope(man, root):
    """R10's scope for R9: the receipts, and the certificate attestations citing runs, at the tranche base."""
    import subprocess
    base = man.get('base', '')
    git = lambda *a: subprocess.run(['git', '-C', root] + list(a), capture_output=True)
    if git('cat-file', '-e', base + '^{commit}').returncode != 0:
        return None, ['R10 the tranche base %s is not in the repository' % base[:12]]
    scope = set()
    names = git('ls-tree', '-r', '--name-only', base, '--', 'verification/receipts',
                'verification/certificates/attestations').stdout.decode('utf-8').split('\n')
    for p in names:
        if p.startswith('verification/receipts/') and p.endswith('.json'):
            scope.add(p)
        elif p.startswith('verification/certificates/attestations/') and p.endswith('.json'):
            d = json.loads(git('show', '%s:%s' % (base, p)).stdout)
            if any(isinstance(v, dict) and v.get('run') for v in (d.get('ci') or {}).values()):
                scope.add(p)
    return scope, []


LEAN_ROOT = 'verification/lean-mathlib/'


def git_show(root):
    """show(rev, path): the bytes of the blob at path in rev, read from root's history, or None."""
    import subprocess

    def show(rev, path):
        p = subprocess.run(['git', '-C', root, 'cat-file', 'blob', '%s:%s' % (rev, path)], capture_output=True)
        return p.stdout if p.returncode == 0 else None
    return show


def governed_entries(texts):
    """The (class, ops, path) lines of the one v3-governed-paths block across a control plane's files, as S7 and
    G10 of the V3 specification state them (an opener and a closer are exact lines, fields are separated by one
    space), or None if there is not exactly one closed block or a line is not a class and two fields. Written here
    from the specification, not taken from build_archive.py or tools/v3_verifier.py."""
    blocks = []
    for t in texts:
        lines = t.split('\n')
        i = 0
        while i < len(lines):
            if lines[i] == '```v3-governed-paths':
                if '```' not in lines[i + 1:]:
                    return None
                j = lines.index('```', i + 1)
                blocks.append(lines[i + 1:j])
                i = j + 1
            else:
                i += 1
    if len(blocks) != 1:
        return None
    out = []
    for ln in blocks[0]:
        if ln.strip() == '' or ln.startswith('#'):
            continue
        parts = ln.split(' ', 2)
        if len(parts) != 3 or parts[0] not in ('execution', 'record') or not parts[1] or not parts[2]:
            return None
        out.append(tuple(parts))
    return out


def governed_digest(entries):
    """S7's digest of a governed-path set: SHA-256 of the canonical bytes, the entries in ascending order of the
    UTF-8 bytes of their path, every field followed by one NUL byte."""
    out = b'v3-governed-paths\0v1\0'
    for e in sorted(entries, key=lambda e: e[2].encode('utf-8')):
        out += b''.join(f.encode('utf-8') + b'\0' for f in e)
    return hashlib.sha256(out).hexdigest()


def governed_modules(kind, doc, commit, show, F, eid):
    """The Lean modules a round governs, read at commit; None once F has recorded why they cannot be read there."""
    rnd, at = doc.get('round'), str(commit)[:12]
    if kind == 'receipt':
        texts = []
        for b in doc.get('control_plane_blobs') or []:
            data = show(commit, str(b.get('path')))
            if data is None or blob_id(data) != b.get('blob'):
                F('R11 %s: control-plane file %s of %s is not at its receipt\'s blob at %s' % (eid, b.get('path'), rnd, at))
                return None
            texts.append(data.decode('utf-8', 'replace'))
        entries = governed_entries(texts)
        if entries is None:
            F('R11 %s: the control plane of %s at %s carries no single well-formed v3-governed-paths block' % (eid, rnd, at))
            return None
        if governed_digest(entries) != doc.get('governed_paths_digest'):
            F('R11 %s: the governed paths of %s at %s do not hash to its receipt\'s governed_paths_digest' % (eid, rnd, at))
            return None
        paths = [p for _, _, p in entries]
    else:
        cpath = 'verification/certificates/%s.json' % rnd
        data, cert = show(commit, cpath), None
        if data is not None and blob_id(data) == doc.get('certificate'):
            try:
                cert = json.loads(data)
            except ValueError:
                cert = None
        if not isinstance(cert, dict) or not isinstance(cert.get('contributions'), list):
            F('R11 %s: %s at %s is not the certificate its attestation pins' % (eid, cpath, at))
            return None
        paths = [str(c.get('path', '')) for c in cert['contributions'] if isinstance(c, dict)]
    dirs = [p for p in paths if p.endswith('/') and (p.startswith(LEAN_ROOT) or LEAN_ROOT.startswith(p))]
    if dirs:
        F('R11 %s: the governed paths of %s at %s name the directory %s, so they fix no module set' % (eid, rnd, at, dirs[0]))
        return None
    return {p[len(LEAN_ROOT):] for p in paths if p.startswith(LEAN_ROOT) and p.endswith('.lean')}


def module_sets(archive, root, man, show=None):
    """R11, which reads git history: every expected result's module table is the set of Lean modules its run's
    rounds govern, re-derived from each round's control plane at that run's commit. Returns (failures, stats)."""
    show = show or git_show(root)
    fails = []
    F = fails.append
    base = man.get('base', '')
    stats = {'checked': 0, 'modules': 0, 'reads': 0, 'unscoped': []}
    attest = {}
    for c in man.get('coverage', {}).get('files', []):
        raw = show(base, str(c.get('path')))
        try:
            doc = json.loads(raw) if raw is not None else None
        except ValueError:
            doc = None
        if not isinstance(doc, dict):
            F('R11 coverage file %s cannot be read at the tranche base %s' % (c.get('path'), base[:12]))
            continue
        if str(c.get('path')).startswith('verification/receipts/'):
            for a in doc.get('attestations') or []:
                m = a.get('kind') == 'check-run' and RUN_URL.search(str(a.get('record', '')))
                if m:
                    attest.setdefault(m.group(1), []).append(('receipt', doc, a.get('commit')))
        else:
            for v in (doc.get('ci') or {}).values():
                if isinstance(v, dict) and v.get('run'):
                    attest.setdefault(str(v['run']), []).append(('certificate', doc, v.get('head_sha')))
    cache = {}
    for e in man.get('entries', []):
        eid = e.get('id')
        for f in e.get('files', []):
            rel = str(f.get('path', ''))
            if not (rel.endswith('/results.json') or (rel.startswith('bg3/results-') and rel.endswith('.json'))):
                continue
            try:
                r = json.load(open(os.path.join(archive, rel), encoding='utf-8'))
                if r.get('kind') != 'bridge':
                    continue
                rid, head, table = str(r['run']['id']), r['run']['head_sha'], r['expected']['modules']
                if not isinstance(table, dict):
                    raise TypeError('module table')
            except (OSError, ValueError, KeyError, TypeError, AttributeError):
                F('R11 %s: %s is not a readable expected result' % (eid, rel))
                continue
            if rid not in attest:
                if str(eid).startswith('ci-'):
                    F('R11 %s: run %s is attested by no covered receipt or certificate, so no round governs its modules'
                      % (eid, rid))
                else:
                    stats['unscoped'].append((rel, rid, head))
                continue
            derived, whole = set(), True
            for kind, doc, commit in attest[rid]:
                if commit != head:
                    F('R11 %s: %s %s attests run %s at %s; the expected result holds at %s' % (
                        eid, kind, doc.get('round'), rid, str(commit)[:12], str(head)[:12]))
                    whole = False
                    continue
                key = (kind, doc.get('round'), commit)
                if key not in cache:
                    cache[key] = governed_modules(kind, doc, commit, show, F, eid)
                    stats['reads'] += 1
                if cache[key] is None:
                    whole = False
                else:
                    derived |= cache[key]
            if not whole:
                continue
            if derived != set(table):
                F('R11 %s: the module table of %s differs from the Lean modules its run\'s rounds govern at %s: '
                  'missing %s, extra %s' % (eid, rel, head[:12], sorted(derived - set(table)), sorted(set(table) - derived)))
            stats['checked'] += 1
            stats['modules'] += len(table)
    if not stats['checked']:
        F('R11 no expected result was checked against its rounds\' governed paths')
    return fails, stats


def module_report(archive, root):
    """--module-sets: R11 alone, with what it checked and what lies outside its scope."""
    man = json.load(open(os.path.join(archive, 'manifest.json'), encoding='utf-8'))
    fails, st = module_sets(archive, root, man)
    for rel, rid, head in st['unscoped']:
        print('UNSCOPED  %s: run %s at %s is attested by no covered receipt or certificate, so R11 does not apply'
              % (rel, rid, str(head)[:12]))
    for f in fails:
        print('FAIL  %s' % f)
    print('MODULE-SETS  %s (%d expected result(s), %d module record(s), %d round control plane(s) read at their run\'s '
          'commit; %d failure(s))' % ('HOLDS' if not fails else 'FAILS', st['checked'], st['modules'], st['reads'], len(fails)))
    return 0 if not fails else 1


def gate(archive, root):
    """The release-gate step: the check in history mode (R1-R11), then the self-test."""
    man = json.load(open(os.path.join(archive, 'manifest.json'), encoding='utf-8'))
    scope, fails = base_scope(man, root)
    if scope is not None:
        fails += check(archive, root, scope)[0] + later_provenance(man, root) + module_sets(archive, root, man)[0]
    for f in fails:
        print('FAIL  %s' % f)
    st = self_test(archive, root)
    print('EVIDENCE-RETENTION  %s (history mode: %d failure(s); self-test %s)' % (
        'HOLDS' if not fails and st == 0 else 'FAILS', len(fails), 'OK' if st == 0 else 'FAILED'))
    return 0 if not fails and st == 0 else 1


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
    for c in man.get('coverage', {}).get('later', []):
        print('LATER  %s: %s (declared; --later-provenance checks it against git history)' % (c.get('path'), c.get('evidence')))
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

        noop = lambda: None
        ents = man['entries']
        idx = lambda pred: next(i for i, e in enumerate(ents) if pred(e))
        has = lambda e, suffix: any(f['path'].endswith(suffix) for f in e.get('files', []))
        ci = idx(lambda e: str(e.get('id', '')).startswith('ci-') and has(e, '/jobs.json'))
        nojobs = idx(lambda e: str(e.get('id', '')).startswith('ci-') and not has(e, '/jobs.json'))
        cac = idx(lambda e: e.get('kind') == 'complete-as-cited' and len(e['citations']) == 1)
        bgr = idx(lambda e: any(f['path'].startswith('bg3/run-') for f in e['files']))
        cert = idx(lambda e: any(r.get('kind') == 'V2 certificate' for r in e.get('roles', [])))
        rec = idx(lambda e: any(r.get('kind') == 'receipt check-run' for r in e.get('roles', [])))
        e_ci = ents[ci]
        rid = e_ci['run_id']
        rsj = next(j for j, f in enumerate(e_ci['files']) if f['path'].endswith('/results.json'))
        runj = next(j for j, f in enumerate(e_ci['files']) if f['path'].endswith('/run.json'))
        xp = os.path.join(tarch, e_ci['files'][rsj]['path'])
        cp = os.path.join(troot, e_ci['citations'][0]['path'])
        ret = next((j, k) for j, c in enumerate(e_ci['citations']) for k, x in enumerate(c['claims'])
                   if x['status'] == 'retained')
        loaded = {e['id']: json.load(open(os.path.join(tarch, next(f['path'] for f in e['files'] if f['path'].endswith('/results.json')))))
                  for e in ents if str(e.get('id', '')).startswith('ci-')}
        part = next(e['id'] for e in ents if e['id'] in loaded and any(m['status'] == 'partial' for m in loaded[e['id']]['expected']['modules'].values()))
        pmod = next(m for m, x in loaded[part]['expected']['modules'].items() if x['status'] == 'partial')
        pp = os.path.join(tarch, 'ci', part.split('-', 1)[1], 'results.json')
        comp = next(e['id'] for e in ents if e['id'] in loaded and any(m['status'] == 'complete' and m['reports'] for m in loaded[e['id']]['expected']['modules'].values()))
        cmod = next(m for m, x in loaded[comp]['expected']['modules'].items() if x['status'] == 'complete' and x['reports'])
        cpth = os.path.join(tarch, 'ci', comp.split('-', 1)[1], 'results.json')
        X = lambda m: m['entries'][ci]['files'][rsj]
        C0 = lambda m: m['entries'][ci]['citations'][0]
        RC = lambda m: m['entries'][ci]['citations'][ret[0]]['claims'][ret[1]]

        def json_edit(path, fn):
            def change(b):
                d = json.loads(b)
                fn(d)
                return json.dumps(d).encode('utf-8')
            mutate, restore = file_edit(path, change)
            # a changed file must still pass R1, so its recorded size and digest follow it
            rel = os.path.relpath(path, tarch).replace(os.sep, '/')

            def go():
                mutate()
                m = json.loads(open(mp, 'rb').read())
                for e in m['entries']:
                    for f in e['files']:
                        if f['path'] == rel:
                            data = open(path, 'rb').read()
                            f['bytes'], f['sha256'] = len(data), hashlib.sha256(data).hexdigest()
                open(mp, 'w', encoding='utf-8').write(json.dumps(m))

            def undo():
                restore()
                back()
            return go, undo

        expect('unmutated copy passes', noop, noop)
        # manifest form (R7)
        expect('an unreadable manifest', *file_edit(mp, lambda b: b[:-2]), rule='R7', msg='manifest unreadable')
        expect('a manifest of another version', edit(lambda m: m.__setitem__('version', 1)), back, 'R7', 'schema or version')
        expect('a repeated entry id', edit(lambda m: m['entries'][nojobs].__setitem__('id', e_ci['id'])), back, 'R7',
               'missing or repeated')
        expect('an unknown entry kind', edit(lambda m: m['entries'][cac].__setitem__('kind', 'complete-ish')), back, 'R7',
               ': unknown kind')
        expect('a cited entry relabelled "complete"', edit(lambda m: m['entries'][cac].__setitem__('kind', 'complete')),
               back, 'R7', 'carries citations')
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
        # files (R1, R2, R5, R6)
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
        # expected results (R4)
        expect('a results.json that is not JSON', *json_edit(xp, lambda d: None) if False else file_edit(xp, lambda b: b[:-3]),
               rule='R4', msg='not JSON')
        expect('a results.json of another schema', *json_edit(xp, lambda d: d.__setitem__('schema', 'x')), rule='R4',
               msg='unknown schema')
        expect('a results.json naming no head commit', *json_edit(xp, lambda d: d['run'].__setitem__('head_sha', 'abc')),
               rule='R4', msg='names no run')
        expect('a results.json without a reproduction recipe', *json_edit(xp, lambda d: d['reproduce'].__setitem__('recipe', [])),
               rule='R4', msg='no reproduction recipe')
        expect('a results.json recording no successful build', *json_edit(xp, lambda d: d['expected'].__setitem__('build_success', False)),
               rule='R4', msg='no successful build')
        expect('a results.json without a gate verdict', *json_edit(xp, lambda d: d['expected']['gate'].__setitem__('verdict', None)),
               rule='R4', msg='no gate verdict')
        expect('a gate step of unknown status',
               *json_edit(xp, lambda d: d['expected']['gate']['steps'][0].__setitem__('status', 'OK')), rule='R4',
               msg='malformed gate steps')
        expect('a results.json without a module table', *json_edit(xp, lambda d: d['expected'].__setitem__('modules', [])),
               rule='R4', msg='no module table')
        expect('a module of unknown status',
               *json_edit(cpth, lambda d: d['expected']['modules'][cmod].__setitem__('status', 'maybe')), rule='R4',
               msg='has status')
        expect('a malformed report',
               *json_edit(cpth, lambda d: d['expected']['modules'][cmod]['reports'][0].__setitem__('axioms', 'propext')), rule='R4',
               msg='malformed report')
        expect('an absent module with reports',
               *json_edit(cpth, lambda d: d['expected']['modules'][cmod].__setitem__('status', 'absent')), rule='R4',
               msg='is absent but has')
        expect('a report outside the module\'s #print axioms lines',
               *json_edit(cpth, lambda d: d['expected']['modules'][cmod]['reports'][0].__setitem__('line', 10 ** 6)), rule='R4',
               msg='outside its #print axioms lines')
        expect('a partial module recorded as complete',
               *json_edit(pp, lambda d: d['expected']['modules'][pmod].__setitem__('status', 'complete')), rule='R4',
               msg='its lines give')
        expect('a results.json without a marker count',
               *json_edit(xp, lambda d: d['expected']['markers'].pop('sorryAx')), rule='R4', msg='no count for every marker')
        # entry files agree (R8)
        expect('a BG-3 entry whose provenance names another head commit',
               edit(lambda m: m['entries'][bgr]['provenance'].__setitem__('head_sha', '0' * 40)), back, 'R8',
               'differs from the entry\'s provenance')
        bgres = next(f['path'] for f in ents[bgr]['files'] if f['path'].startswith('bg3/results-'))
        expect('a BG-3 results file naming another job',
               *json_edit(os.path.join(tarch, bgres), lambda d: d['run'].__setitem__('job_id', '1')), rule='R8',
               msg='names another run, job')
        expect('a CI entry without run.json', edit(lambda m: m['entries'][ci]['files'].pop(runj)), back, 'R8', 'no run.json')
        expect('a results.json naming another head commit than run.json',
               *json_edit(xp, lambda d: d['run'].__setitem__('head_sha', '0' * 40)), rule='R8', msg='names another run, head commit')
        expect('a missing job list that is not a recorded gap', edit(lambda m: m.__setitem__('missing', [
            g for g in m['missing'] if not (g['id'] == ents[nojobs]['id'] and g['what'] == 'job list')])), back, 'R8',
               'not a recorded gap')
        dres = next(f['path'] for e in ents for f in e['files'] if f['path'] == 'bg3/results-116831668411.json')
        expect('a design-log result recording no checks',
               *json_edit(os.path.join(tarch, dres), lambda d: d['expected'].__setitem__('checks', [])), rule='R4',
               msg='records no checks or no recipe')
        rjp = os.path.join(tarch, 'ci', rid, 'run.json')
        expect('a run.json that is not JSON', *file_edit(rjp, lambda b: b[:-3]), rule='R8', msg='run.json or results.json is not JSON')
        jp = os.path.join(tarch, 'ci', rid, 'jobs.json')
        expect('a jobs.json that is not a job list', *json_edit(jp, lambda d: d.pop('jobs')), rule='R8', msg='not a job list')
        expect('a job at another head commit',
               *json_edit(jp, lambda d: d['jobs'][0].__setitem__('head_sha', '0' * 40)), rule='R8', msg='head_sha differs')
        expect('results from another job', *json_edit(xp, lambda d: d['run'].__setitem__('job_id', '1')), rule='R8',
               msg='not from attempt')
        expect('a partial module whose gap record is removed', edit(lambda m: m.__setitem__('missing', [
            g for g in m['missing'] if not (g['id'] == part and g['what'] == 'axiom reports of %s' % pmod)])),
               back, 'R8', 'its gap record is absent')
        # coverage (R9)
        cited = next(c['path'] for c in man['coverage']['files']
                     if any(x['path'] == c['path'] for e in ents for x in e.get('citations', [])))
        expect('a cited receipt dropped from the coverage list', edit(lambda m: m['coverage'].__setitem__(
            'files', [c for c in m['coverage']['files'] if c['path'] != cited])), back, 'R9', 'not in the coverage list')
        newr = os.path.join(troot, 'verification', 'receipts', 'ZZ-LATER.json')
        expect('a receipt in the tree that is neither covered nor named as later',
               lambda: open(newr, 'w').write('{}'), lambda: os.remove(newr), 'R9', 'neither covered')
        expect('a receipt named as later than this tranche passes',
               lambda: (open(newr, 'w').write('{}'), edit(lambda m: m['coverage'].__setitem__(
                   'later', [{'path': 'verification/receipts/ZZ-LATER.json', 'evidence': 'its own record directory'}]))()),
               lambda: (os.remove(newr), back()))
        expect('a cited, covered receipt moved to coverage.later', edit(lambda m: (
            m['coverage'].__setitem__('files', [c for c in m['coverage']['files'] if c['path'] != cited]),
            m['coverage'].__setitem__('later', [{'path': cited, 'evidence': 'x'}]))), back, 'R9', 'the tranche cites it')
        expect('a receipt named both as covered and as later', edit(lambda m: m['coverage'].__setitem__(
            'later', [{'path': cited, 'evidence': 'x'}])), back, 'R9', 'both as covered and as later')
        expect('a later receipt without where its evidence is retained',
               lambda: (open(newr, 'w').write('{}'), edit(lambda m: m['coverage'].__setitem__(
                   'later', [{'path': 'verification/receipts/ZZ-LATER.json'}]))()),
               lambda: (os.remove(newr), back()), 'R9', 'without where its evidence')
        # R10 reads the real repository's history, read-only
        import subprocess
        hist = subprocess.run(['git', '-C', root, 'cat-file', '-e', man['base'] + '^{commit}'], capture_output=True).returncode == 0
        if not hist:
            ok = False
            print('FAIL self: the R10 cases need the tranche base in this repository\'s history')
        else:
            def r10(name, fails, msg=None):
                nonlocal ok
                good = (not fails) if msg is None else any(f.startswith('R10 ') and msg in f for f in fails)
                ok &= good
                print('%s self: %s%s' % ('PASS' if good else 'FAIL', name, '' if msg is None else ' (R10)'))
            r10('a receipt that did not exist at the base passes R10',
                later_provenance(man, root, [{'path': 'verification/receipts/ZZ-LATER.json'}]))
            r10('a frozen-tranche receipt named as later fails R10', later_provenance(man, root, [{'path': cited}]),
                'existed at the tranche base')
            r10('a tranche base absent from the repository fails R10',
                later_provenance(dict(man, base='0' * 40), root, []), 'not in the repository')
            r10('a HEAD that does not descend from the base fails R10',
                later_provenance(man, root, [], head=man['base'] + '^'), 'not an ancestor')
            scope, sf = base_scope(man, root)
            r10('the base scope is read from git', sf)
            r10('a tranche base absent from the repository has no scope', base_scope(dict(man, base='0' * 40), root)[1],
                'not in the repository')
            hist_check = lambda: check(tarch, troot, scope)[0]
            for name, mut, res, msg in (
                    ('history mode passes on the unmutated copy', noop, noop, None),
                    ('a base receipt dropped from coverage, in history mode',
                     edit(lambda m: m['coverage'].__setitem__('files', [c for c in m['coverage']['files'] if c['path'] != cited])),
                     back, 'existed at the tranche base but is not covered'),
                    ('a covered file that did not exist at the base, in history mode',
                     lambda: (open(newr, 'w').write('{}'), edit(lambda m: m['coverage']['files'].append(
                         {'path': 'verification/receipts/ZZ-LATER.json', 'blob': blob_id(b'{}')}))()),
                     lambda: (os.remove(newr), back()), 'did not exist at the tranche base'),
                    ('a receipt landed after the base needs no declaration in history mode',
                     lambda: open(newr, 'w').write('{}'), lambda: os.remove(newr), None)):
                mut()
                fails = hist_check()
                res()
                good = (not fails) if msg is None else any(f.startswith('R10 ') and msg in f for f in fails)
                ok &= good
                print('%s self: %s%s' % ('PASS' if good else 'FAIL', name, '' if msg is None else ' (R10)'))
                if not good:
                    print('      got: %s' % (fails[:3],))
            # R11 reads the real repository's history through show(); a case replaces some reads, or edits a copied
            # expected result, and requires that site's own message
            real = git_show(root)
            base = man['base']

            def r11(name, msg=None, mutate=noop, restore=noop, over=None, m=None, also=None):
                nonlocal ok
                o = over() if over else {}
                mutate()
                try:
                    fails, st = module_sets(tarch, root, man if m is None else m,
                                            lambda rev, path: o[(rev, path)] if (rev, path) in o else real(rev, path))
                finally:
                    restore()
                good = (not fails) if msg is None else any(f.startswith('R11 ') and msg in f for f in fails)
                if also is not None:
                    good = good and also(st)
                ok &= good
                print('%s self: %s%s' % ('PASS' if good else 'FAIL', name, '' if msg is None else ' (R11)'))
                if not good:
                    print('      got: %s' % (fails[:3],))

            def res_edit(path, fn):
                def change(b):
                    d = json.loads(b)
                    fn(d)
                    return json.dumps(d).encode('utf-8')
                return file_edit(path, change)

            def attestation_of(run):
                for c in man['coverage']['files']:
                    d = json.loads(real(base, c['path']))
                    for a in d.get('attestations', []):
                        mm = RUN_URL.search(a.get('record', ''))
                        if a.get('kind') == 'check-run' and mm and mm.group(1) == run:
                            return c['path'], d, a['commit']
                    for v in (d.get('ci') or {}).values():
                        if isinstance(v, dict) and str(v.get('run')) == run:
                            return c['path'], d, v['head_sha']

            def block_edit(text, fn):
                ls = text.decode('utf-8').split('\n')
                i = ls.index('```v3-governed-paths')
                j = ls.index('```', i + 1)
                return '\n'.join(ls[:i + 1] + fn(ls[i + 1:j]) + ls[j:]).encode('utf-8')

            crun = comp.split('-', 1)[1]
            rpath, rdoc, rcommit = attestation_of(crun)
            pre = next(b['path'] for b in rdoc['control_plane_blobs'] if b['path'].endswith('/preregistration.md'))
            ptext = real(rcommit, pre)

            def pinned(text, digest=False):
                """The receipt and the preregistration at the run's commit, with the receipt's pin following the text."""
                d = json.loads(json.dumps(rdoc))
                for b in d['control_plane_blobs']:
                    if b['path'] == pre:
                        b['blob'] = blob_id(text)
                if digest:
                    texts = [(text if b['path'] == pre else real(rcommit, b['path'])).decode('utf-8')
                             for b in d['control_plane_blobs']]
                    d['governed_paths_digest'] = governed_digest(governed_entries(texts))
                return {(rcommit, pre): text, (base, rpath): json.dumps(d).encode('utf-8')}
            ccert = ents[cert]
            cpath_, cdoc, ccommit = attestation_of(ccert['run_id'])
            cres = os.path.join(tarch, 'ci', ccert['run_id'], 'results.json')
            nci = sum(1 for e in ents if str(e.get('id', '')).startswith('ci-'))
            r11('R11 passes on the unmutated copy and checks every CI entry\'s expected result',
                also=lambda st: st['checked'] >= nci and st['modules'] > 0 and all(u[0].startswith('bg3/') for u in st['unscoped']))
            r11('a control plane altered only at the tranche base leaves R11 unchanged: it reads the run\'s commit',
                over=lambda: {(base, pre): b'altered at the base'})
            r11('a coverage file that cannot be read at the tranche base', 'cannot be read at the tranche base',
                m=dict(man, coverage=dict(man['coverage'], files=man['coverage']['files'] + [
                    {'path': 'verification/receipts/ZZ-NONE.json', 'blob': '0' * 40}])))
            r11('an expected result that cannot be read', 'is not a readable expected result',
                *file_edit(cpth, lambda b: b[:-3]))
            r11('an expected result of a run no covered file attests', 'is attested by no covered receipt',
                *res_edit(cpth, lambda d: d['run'].__setitem__('id', '1')))
            r11('an expected result at another commit than its attestation', 'the expected result holds at',
                *res_edit(cpth, lambda d: d['run'].__setitem__('head_sha', '0' * 40)))
            r11('a control-plane file that is not at its receipt\'s blob at the run\'s commit', 'is not at its receipt\'s blob',
                over=lambda: {(rcommit, pre): ptext + b'\n'})
            r11('a control plane without a well-formed governed-paths block, its pin following it',
                'no single well-formed v3-governed-paths block',
                over=lambda: pinned(ptext.replace(b'\n```v3-governed-paths\n', b'\n```v3-governed-pathz\n', 1)))
            r11('governed paths that do not hash to the receipt\'s digest, the pin following them',
                'do not hash to its receipt\'s governed_paths_digest',
                over=lambda: pinned(block_edit(ptext, lambda body: [x for x in body if not x.endswith('.lean')])))
            r11('governed paths naming a directory of Lean modules, pin and digest following them', 'name the directory',
                over=lambda: pinned(block_edit(ptext, lambda body: body + ['execution M ' + LEAN_ROOT + 'OIBridge/']), True))
            r11('a certificate that is not at the blob its attestation pins', 'is not the certificate its attestation pins',
                over=lambda: {(ccommit, 'verification/certificates/%s.json' % cdoc['round']):
                              real(ccommit, 'verification/certificates/%s.json' % cdoc['round']) + b' '})
            r11('a module table missing a governed module', 'differs from the Lean modules',
                *res_edit(cpth, lambda d: d['expected']['modules'].pop(cmod)))
            r11('a module table with a module the round does not govern', 'differs from the Lean modules',
                *res_edit(cpth, lambda d: d['expected']['modules'].__setitem__('OIBridge/NotGoverned.lean', {
                    'status': 'absent', 'reports': [], 'prints': None, 'print_lines': None})))
            r11('a certificate run\'s module table with a module its certificate does not contribute',
                'differs from the Lean modules', *res_edit(cres, lambda d: d['expected']['modules'].__setitem__(
                    'OIBridge/NotGoverned.lean', {'status': 'absent', 'reports': [], 'prints': None, 'print_lines': None})))
            r11('a manifest with no expected result to check', 'no expected result was checked', m=dict(man, entries=[]))
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
    if sys.argv[1:] == ['--gate']:
        sys.exit(gate(HERE, root))
    if sys.argv[1:] == ['--module-sets']:
        sys.exit(module_report(HERE, root))
    if sys.argv[1:] == ['--later-provenance']:
        man = json.load(open(os.path.join(HERE, 'manifest.json'), encoding='utf-8'))
        fails = later_provenance(man, root)
        for f in fails:
            print('FAIL  %s' % f)
        print('LATER-PROVENANCE  %s (%d path(s) named as later, %d failure(s))' % (
            'HOLDS' if not fails else 'FAILS', len(man.get('coverage', {}).get('later', [])), len(fails)))
        sys.exit(1 if fails else 0)
    if sys.argv[1:]:
        print(__doc__)
        sys.exit(2)
    sys.exit(report(HERE, root))
