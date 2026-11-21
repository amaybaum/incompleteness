#!/usr/bin/env python3
"""Preservation checker for the A1 deletion, independent of the transformation. Standard library only; it imports
nothing from edits_check.py, guards_check.py or any script that applies the edits.

The frozen exact-edit ledger (ledger.json) records every edit that changes text as a splice of the base: the file, the
byte span of the old text at the base, the SHA-256 of the old text, the new text, its SHA-256 and the reason. The ledger
is the authorization: nothing outside it may change, apart from the regenerated artifacts named below, each compared
with a rebuild on the candidate.

Usage (from the repository root):
  python3 -I -B .../preserve_check.py --build-ledger          write ledger.json from edits.json at its drafting base
  python3 -I -B .../preserve_check.py --verify-ledger         re-derive ledger.json and compare (spans, hashes, ids)
  python3 -I -B .../preserve_check.py --verify-pins           the record files against the digests pinned in PREREG §26.4
  python3 -I -B .../preserve_check.py --commit REV | --tree DIR [--plan REV] [--base REV] [--mutants]
                                                              check a candidate post-deletion tree
  python3 -I -B .../preserve_check.py --self-test             mutation tests in both directions on the real ledger

--plan REV   the plan commit the owner designates when authorizing execution. The ledger, the pin table and the record
             directory are read from REV's objects, never from the candidate or the working checkout, and this script's
             own bytes must equal REV's copy of it. Without --plan the plan is the working checkout (reported as such);
             its files must still match the pins of PREREG §26.4.
--base REV   compare against REV (a later main) instead of the ledger base; refused unless every ledgered file is
             byte-identical at REV and at the ledger base.
--pdf-compare BUILT
             with --tree: every committed PDF of a ledgered source has the page count and the pdftotext text of the PDF
             the CI build (build.sh) made from the same tree under BUILT.
--mutants    with --tree: mutates the candidate in place, one change at a time, restores it, and requires each mutation
             to fail (a hand-edited TeX file, SC-42 result, ledger, checker, coverage fingerprint, record file).

A candidate passes when, against the base:
  1. every ledgered file equals, byte for byte, the base with exactly the ledger's splices applied;
  2. every other tracked file equals the base, except: the TeX files of the ledgered sources, each byte-identical to
     its rebuild from the candidate's source by build.sh's recipe (pandoc; a base control first rebuilds the base
     sources and must reproduce the base TeX); their PDFs (rebuilt in CI, which records page counts and requires no
     dropped glyph); the SC-42 integration result, byte-identical to the SC-42 checker's output on the candidate, plain
     and with -O, with its self-test equal to the unchanged controls file; and the fingerprints of the four coverage
     entries the edits make stale, each equal to the value the census computes on the candidate;
  3. the record directory equals the plan's, and adds files only under its execution/ subdirectory;
  4. no file is added or deleted elsewhere;
  5. structurally: a Python file changes only in string constants and comments, a Lean file only inside comments, a
     JSON file only in string values.
"""
import argparse, ast, hashlib, json, os, re, shutil, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..'))
REC = os.path.relpath(HERE, ROOT).replace(os.sep, '/') + '/'
SELF = REC + 'preserve_check.py'
EDITS, LEDGER, PREREG = REC + 'edits.json', REC + 'ledger.json', REC + 'PREREG.md'
PINNED = ['edits.json', 'ledger.json', 'edits_check.py', 'guards_check.py', 'preserve_check.py']
BOOK = 'book/The-Incompleteness-of-Observation-FULL'
HEADER = 'tools/unicode-fix.tex'
COVERAGE = 'verification/coverage/LEDGER.json'
STALE = ['MAIN:L-3', 'STRUCTURE:P-9.5', 'SUBSTRATUM:C-effective-finiteness-gauge-class-transfer', 'SUBSTRATUM:T-23']
SC42_DIR = 'verification/audits/manuscript/bell-operational-reconciliation-20261029/'
SC42 = SC42_DIR + 'sc42-integration-result.json'
SC42_CONTROLS = SC42_DIR + 'sc42-integration-controls.json'
SC42_BASE = 'ca3a5bb25ec6fdff3d3ccffcacd2d7bac3bb4caf'


def sha(b):
    return hashlib.sha256(b).hexdigest()


def git(*a):
    return subprocess.run(['git', '-C', ROOT] + list(a), capture_output=True, check=True).stdout


def tree_of(rev):
    """{path: bytes} of every blob of rev, read from the object store."""
    ents = []
    for rec in git('ls-tree', '-r', '-z', rev).split(b'\0'):
        if rec:
            meta, path = rec.split(b'\t', 1)
            mode, typ, oid = meta.split()
            if typ == b'blob':
                ents.append((oid, path.decode('utf-8')))
    p = subprocess.Popen(['git', '-C', ROOT, 'cat-file', '--batch'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    out = {}
    for oid, path in ents:
        p.stdin.write(oid + b'\n'); p.stdin.flush()
        n = int(p.stdout.readline().split()[2])
        out[path] = p.stdout.read(n); p.stdout.read(1)
    p.stdin.close(); p.wait()
    return out


def tree_dir(d):
    out = {}
    for dp, dns, fns in os.walk(d):
        dns[:] = [x for x in dns if x not in ('.git', '__pycache__')]
        for n in fns:
            fp = os.path.join(dp, n)
            rel = os.path.relpath(fp, d).replace(os.sep, '/')
            if rel == '.git':
                continue
            out[rel] = os.readlink(fp).encode('utf-8') if os.path.islink(fp) else open(fp, 'rb').read()
    return out


# ---- plan: ledger, pins and record directory ----------------------------------------------------------------

def plan_files(rev):
    """The record directory of the plan: from REV's objects, or from the working checkout when rev is None."""
    if rev:
        return {p: b for p, b in tree_of(rev).items() if p.startswith(REC)}
    return {REC + n: open(os.path.join(HERE, n), 'rb').read() for n in sorted(os.listdir(HERE))
            if os.path.isfile(os.path.join(HERE, n)) and not n.startswith('.')}


def read_pins(prereg):
    """The digest table of PREREG §26.4: rows "| `file` | `sha256` |"."""
    t = prereg.decode('utf-8')
    i = t.find('### 26.4 Record pins')
    if i < 0:
        return {}
    j = t.find('\n#', i + 5)
    return dict(re.findall(r'^\| `([\w.]+)` \| `([0-9a-f]{64})` \|', t[i:j if j > 0 else None], re.M))


def verify_pins(plan, own_bytes):
    bad = []
    pins = read_pins(plan.get(PREREG, b''))
    for n in PINNED:
        if n not in pins:
            bad.append('PREREG §26.4 pins no digest for %s' % n)
        elif REC + n not in plan:
            bad.append('%s absent from the plan' % n)
        elif sha(plan[REC + n]) != pins[n]:
            bad.append('%s does not match its pinned digest' % n)
    if own_bytes != plan.get(SELF):
        bad.append('this checker is not the plan\'s preserve_check.py (run it from the plan: git show <plan>:%s)' % SELF)
    try:
        led = json.loads(plan.get(LEDGER, b'{}'))
        if led.get('edits_sha256') != sha(plan.get(EDITS, b'')):
            bad.append('ledger.json was not built from the plan\'s edits.json')
    except ValueError:
        bad.append('ledger.json does not parse')
    return bad


# ---- ledger -------------------------------------------------------------------------------------------------

def build_ledger(edits, base_files, edits_bytes):
    spl, kept = [], []
    for e in edits['edits']:
        b = base_files[e['file']]
        o = e['old'].encode('utf-8')
        if b.count(o) != 1:
            raise SystemExit('%s: old text occurs %d times in %s at the base' % (e['id'], b.count(o), e['file']))
        if e['old'] == e['new']:
            kept.append(e['id'])  # a retained-site record: no text changes, so it is no splice
            continue
        s = b.index(o)
        spl.append({'id': e['id'], 'file': e['file'], 'start': s, 'end': s + len(o), 'old_sha256': sha(o),
                    'new': e['new'], 'new_sha256': sha(e['new'].encode('utf-8')), 'reason': e['reason']})
    spl.sort(key=lambda x: (x['file'], x['start']))
    led = {'schema': 'a1exit deletion exact-edit ledger v2', 'base': edits['drafting_base'], 'edits_sha256': sha(edits_bytes),
           'retained_unchanged': kept, 'splices': spl, 'files': {}}
    for f in sorted({x['file'] for x in spl}):
        led['files'][f] = {'base_sha256': sha(base_files[f]), 'expected_sha256': sha(expected(led, base_files, f))}
    return led


def validate_ledger(led, base_files):
    bad, by = [], {}
    for x in led['splices']:
        b = base_files.get(x['file'])
        if b is None:
            bad.append('%s: file %s absent at the base' % (x['id'], x['file'])); continue
        if sha(b[x['start']:x['end']]) != x['old_sha256']:
            bad.append('%s: old-text hash does not match the base span %d-%d of %s' % (x['id'], x['start'], x['end'], x['file']))
        if sha(x['new'].encode('utf-8')) != x['new_sha256']:
            bad.append('%s: new-text hash does not match the new text' % x['id'])
        by.setdefault(x['file'], []).append(x)
    for f, xs in by.items():
        xs = sorted(xs, key=lambda y: y['start'])
        for a, c in zip(xs, xs[1:]):
            if a['end'] > c['start']:
                bad.append('%s and %s overlap in %s' % (a['id'], c['id'], f))
        if f in led['files'] and sha(base_files[f]) != led['files'][f]['base_sha256']:
            bad.append('%s: base hash differs from the ledger' % f)
    return bad


def expected(led, base_files, f, skip=()):
    b = base_files[f]
    out, pos = [], 0
    for x in sorted((y for y in led['splices'] if y['file'] == f), key=lambda y: y['start']):
        out.append(b[pos:x['start']])
        out.append(b[x['start']:x['end']] if x['id'] in skip else x['new'].encode('utf-8'))
        pos = x['end']
    out.append(b[pos:])
    return b''.join(out)


def tex_sources(led):
    """TeX outputs of the ledgered sources: {tex path: (source path, book?)}."""
    out = {}
    for f in led['files']:
        if re.match(r'^papers/[^/]+\.md$', f):
            out[f[:-3] + '.tex'] = (f, False)
        elif f == BOOK + '.md':
            out[BOOK + '.tex'] = (f, True)
    return out


# ---- regeneration -------------------------------------------------------------------------------------------

def rebuild_tex(md, header, book):
    """build.sh's TeX recipe: pandoc -s [--toc --metadata=toc:false] --pdf-engine=xelatex --include-in-header, then the
    source-sha256 stamp line."""
    d = tempfile.mkdtemp(prefix='a1exit-tex-')
    try:
        open(os.path.join(d, 'in.md'), 'wb').write(md)
        os.makedirs(os.path.join(d, 'tools'))
        open(os.path.join(d, HEADER), 'wb').write(header)
        cmd = ['pandoc', 'in.md', '-s'] + (['--toc', '--metadata=toc:false'] if book else []) + \
              ['--pdf-engine=xelatex', '--include-in-header=' + HEADER, '-o', 'out.tex']
        subprocess.run(cmd, cwd=d, check=True, capture_output=True)
        return open(os.path.join(d, 'out.tex'), 'rb').read() + ('%% source-sha256: %s\n' % sha(md)).encode()
    finally:
        shutil.rmtree(d, ignore_errors=True)


def census_fingerprints(files):
    """{id: fingerprint} of tools/proof_census.py run on the given papers/ and tools/ files."""
    d = tempfile.mkdtemp(prefix='a1exit-census-')
    try:
        for p, b in files.items():
            if p.startswith(('papers/', 'tools/')) and (p.endswith('.md') or p.endswith('.py')):
                fp = os.path.join(d, p); os.makedirs(os.path.dirname(fp), exist_ok=True); open(fp, 'wb').write(b)
        r = subprocess.run([sys.executable, '-I', '-B', 'tools/proof_census.py', '--json'], cwd=d, capture_output=True, text=True, check=True)
        return {c['id']: c['fingerprint'] for c in json.loads(r.stdout)}
    finally:
        shutil.rmtree(d, ignore_errors=True)


def sc42_runs(checkout):
    """The SC-42 checker on a git checkout, as verify.yml runs it: (--verbose, -O, --self-test, -O --self-test) outputs."""
    out = []
    for opt, args in (([], ['--verbose']), (['-O'], []), ([], ['--self-test']), (['-O'], ['--self-test'])):
        r = subprocess.run([sys.executable, '-I'] + opt + ['-B', SC42_DIR + 'check_sc42_integration.py'] + args,
                           cwd=checkout, capture_output=True)
        out.append(r.stdout if r.returncode == 0 else None)
    return out


def regenerate(cand, checkout, base_files):
    """What the regenerated artifacts must be, computed on the candidate."""
    reg = {'tex': {}, 'fingerprints': {}, 'sc42': None, 'control': []}
    for tex, (md, book) in TEX.items():
        if md in base_files and tex in base_files and rebuild_tex(base_files[md], base_files[HEADER], book) != base_files[tex]:
            reg['control'].append('base control: rebuilding %s does not reproduce the base %s (toolchain differs)' % (md, tex))
        if md in cand:
            reg['tex'][tex] = rebuild_tex(cand[md], cand.get(HEADER, base_files[HEADER]), book)
    reg['fingerprints'] = census_fingerprints(cand)
    if checkout and os.path.isdir(os.path.join(checkout, '.git')) or (checkout and os.path.isfile(os.path.join(checkout, '.git'))):
        reg['sc42'] = sc42_runs(checkout)
    return reg


# ---- structural checks (independent re-implementation) ------------------------------------------------------

def lean_code(t):
    out, i, depth, n = [], 0, 0, len(t)
    while i < n:
        if t.startswith('/-', i):
            depth += 1; i += 2; continue
        if depth and t.startswith('-/', i):
            depth -= 1; i += 2; continue
        if depth:
            i += 1; continue
        if t.startswith('--', i):
            j = t.find('\n', i); i = n if j < 0 else j; continue
        out.append(t[i]); i += 1
    return re.sub(r'\s+', ' ', ''.join(out)).strip()


class _Blank(ast.NodeTransformer):
    def visit_Constant(self, node):
        return ast.copy_location(ast.Constant(value=''), node) if isinstance(node.value, str) else node


def py_shape(t):
    import warnings
    with warnings.catch_warnings():
        warnings.simplefilter('ignore')
        return ast.dump(_Blank().visit(ast.parse(t)), include_attributes=False)


def json_shape(v):
    if isinstance(v, dict):
        return {k: json_shape(w) for k, w in v.items()}
    if isinstance(v, list):
        return [json_shape(w) for w in v]
    return '' if isinstance(v, str) else v


def structural(f, old, new):
    try:
        o, n = old.decode('utf-8'), new.decode('utf-8')
        if f.endswith('.py'):
            return py_shape(o) == py_shape(n)
        if f.endswith('.lean'):
            return lean_code(o) == lean_code(n)
        if f.endswith('.json'):
            return json_shape(json.loads(o)) == json_shape(json.loads(n))
    except (SyntaxError, ValueError):
        return False
    return True


def pdf_facts(path):
    """(page count, extracted text) of a PDF; its bytes carry build dates, so they are not compared."""
    info = subprocess.run(['pdfinfo', path], capture_output=True, text=True, check=True).stdout
    pages = int(re.search(r'^Pages:\s+(\d+)', info, re.M).group(1))
    text = subprocess.run(['pdftotext', '-enc', 'UTF-8', path, '-'], capture_output=True, check=True).stdout
    return pages, text


def pdf_compare(cand_dir, built_dir, paths):
    """Each committed PDF has the page count and the extracted text of the PDF the CI build made from the same tree."""
    bad = []
    for p in sorted(paths):
        a, b = os.path.join(cand_dir, p), os.path.join(built_dir, p)
        if not os.path.isfile(a) or not os.path.isfile(b):
            bad.append('%s: missing in the candidate or in the CI build' % p); continue
        (pa, ta), (pb, tb) = pdf_facts(a), pdf_facts(b)
        if pa != pb:
            bad.append('%s: %d pages committed, %d built' % (p, pa, pb))
        if ta != tb:
            bad.append('%s: extracted text differs from the CI-built PDF' % p)
    return bad


def set_fingerprints(b, values):
    """The coverage ledger with the fingerprint of each named entry set to the given value."""
    t = b.decode('utf-8')
    for i, v in values.items():
        m = re.search(r'"id": "%s",.*?"fingerprint": "([0-9a-f]*)"' % re.escape(i), t, re.S)
        if m is None:
            continue
        t = t[:m.start(1)] + v + t[m.end(1):]
    return t.encode('utf-8')


# ---- comparison ---------------------------------------------------------------------------------------------

def locate(led, base_files, f, cand):
    for x in led['splices']:
        if x['file'] == f and expected(led, base_files, f, skip=(x['id'],)) == cand:
            return 'missing ledgered change %s (the old text is still there)' % x['id']
    exp = expected(led, base_files, f)
    p = 0
    while p < min(len(exp), len(cand)) and exp[p] == cand[p]:
        p += 1
    q = 0
    while q < min(len(exp), len(cand)) - p and exp[-1 - q] == cand[-1 - q]:
        q += 1
    shift, spans = 0, []
    for x in sorted((y for y in led['splices'] if y['file'] == f), key=lambda y: y['start']):
        s = x['start'] + shift
        nl = len(x['new'].encode('utf-8'))
        spans.append((s, s + nl, x['id']))
        shift += nl - (x['end'] - x['start'])
    hit = [i for s, e, i in spans if s <= len(exp) - q and p <= e]
    line = exp[:p].count(b'\n') + 1
    if hit:
        return 'ledgered change %s altered (first difference at byte %d, line %d)' % (','.join(hit), p, line)
    return 'unauthorized change outside every splice at byte %d, line %d' % (p, line)


def compare(led, base_files, cand, plan, reg):
    """Findings, and the PDFs left to the CI build."""
    bad, pdfs = [], []
    tex = tex_sources(led)
    pdf = {t[:-4] + '.pdf' for t in tex}
    bad += reg.get('control', [])
    for f in sorted(set(base_files) | set(cand) | set(plan)):
        b, c = base_files.get(f), cand.get(f)
        if f.startswith(REC):
            if f in plan:
                if c != plan[f]:
                    bad.append('%s: record file differs from the plan (or is missing)' % f)
            elif c is not None and not f.startswith(REC + 'execution/'):
                bad.append('%s: record file not in the plan, outside execution/' % f)
            continue
        if f in tex:
            want = reg['tex'].get(f)
            if c != want:
                bad.append('%s: differs from its rebuild from the candidate source (build.sh recipe)' % f)
            continue
        if f in pdf:
            if b != c:
                pdfs.append(f)
            if c is None:
                bad.append('%s: file deleted' % f)
            continue
        if f == SC42:
            runs = reg.get('sc42')
            if runs is None:
                bad.append('%s: not regenerated (the candidate is not a git checkout with %s)' % (f, SC42_BASE[:8]))
            else:
                if runs[0] is None or c != runs[0] or runs[1] != runs[0]:
                    bad.append('%s: differs from the SC-42 checker\'s output on the candidate (plain or -O)' % f)
                if runs[2] is None or runs[2] != base_files.get(SC42_CONTROLS) or runs[3] != runs[2]:
                    bad.append('%s: the SC-42 self-test does not reproduce the unchanged controls' % SC42_CONTROLS)
            continue
        if b is None:
            bad.append('%s: file added outside the record directory' % f); continue
        if c is None:
            bad.append('%s: file deleted' % f); continue
        if f in led['files']:
            exp = expected(led, base_files, f)
            if f == COVERAGE:
                exp = set_fingerprints(exp, {i: reg['fingerprints'].get(i, '') for i in STALE})
            if c != exp:
                bad.append('%s: %s' % (f, locate(led, base_files, f, c) if f != COVERAGE else
                                       'differs from the base, the ledger and the census fingerprints of %s' % ', '.join(STALE)))
            if not structural(f, b, c):
                bad.append('%s: structural change outside string constants or comments' % f)
        elif c != b:
            bad.append('%s: unauthorized change in a file the ledger does not touch' % f)
    return bad, pdfs


# ---- self-test and tree mutants -----------------------------------------------------------------------------

def predicted(led, base_files, plan):
    """The predicted candidate assembled in memory (independently of guards_check's builder)."""
    c = dict(base_files)
    for f in led['files']:
        c[f] = expected(led, base_files, f)
    c.update(plan)
    return c


def self_test(led, base_files, plan):
    ok = True

    def expect(cond, msg):
        nonlocal ok
        print('  %s %s' % ('ok ' if cond else 'BAD', msg))
        record('self-test: ' + msg, cond, [] if cond else [msg])
        ok = ok and cond
    good = predicted(led, base_files, plan)
    reg = regenerate(good, None, base_files)
    for t, v in reg['tex'].items():
        good[t] = v
    good[COVERAGE] = set_fingerprints(good[COVERAGE], {i: reg['fingerprints'][i] for i in STALE})
    reg['sc42'] = [good[SC42], good[SC42], base_files[SC42_CONTROLS], base_files[SC42_CONTROLS]]  # as if regenerated
    expect(not reg['control'], 'base control: build.sh\'s recipe reproduces the base TeX of every ledgered source')
    bad, _ = compare(led, base_files, good, plan, reg)
    expect(not bad, 'positive control: base, ledger, rebuilt TeX, census fingerprints and the plan\'s record pass (%d splices)'
           % len(led['splices']))
    for x in bad[:5]:
        print('      ' + x)
    ids = {x['id']: x for x in led['splices']}

    def mut(name, change, want, r=None):
        c = dict(good); change(c)
        b, _ = compare(led, base_files, c, plan, r or reg)
        expect(any(want in x for x in b), '%s: fails with "%s"' % (name, want))
    for i in ('D224', 'D121', 'D302', 'D262', 'D358'):
        f = ids[i]['file']
        mut('MT-missing-%s (one ledgered change not made)' % i,
            lambda c, f=f, i=i: c.__setitem__(f, expected(led, base_files, f, skip=(i,))),
            'missing ledgered change %s' % i)
    mut('MT-altered-D229 (a replacement differs by one space)',
        lambda c: c.__setitem__('papers/Main.md', c['papers/Main.md'].replace(ids['D229']['new'].encode()[:60], ids['D229']['new'].encode()[:60].replace(b' ', b'  ', 1), 1)),
        'ledgered change D229 altered')
    mut('MT-extra-in-ledgered-file (a word outside every splice of papers/Main.md)',
        lambda c: c.__setitem__('papers/Main.md', c['papers/Main.md'].replace(b'\n', b' extra\n', 1)), 'unauthorized change outside every splice')
    mut('MT-extra-in-untouched-file (a comment added to tools/release_gate.py)',
        lambda c: c.__setitem__('tools/release_gate.py', c['tools/release_gate.py'] + b'\n# extra\n'), 'unauthorized change in a file the ledger does not touch')
    mut('MT-guard-code (an operator of the R7 guard)',
        lambda c: c.__setitem__('verification/lean/edge_rigidity_probe.py', c['verification/lean/edge_rigidity_probe.py'].replace(b'ok6 &= ', b'ok6 |= ', 1)),
        'structural change outside string constants or comments')
    mut('MT-guard-literal (a string constant of the R7 guard outside every splice)',
        lambda c: c.__setitem__('verification/lean/edge_rigidity_probe.py', c['verification/lean/edge_rigidity_probe.py'].replace(b"'R7-MAX'", b"'R7-MAY'", 1)),
        'unauthorized change outside every splice')
    mut('MT-lean-code (a Lean definition)',
        lambda c: c.__setitem__('verification/lean-mathlib/OIBridge/HexLatticeGas.lean',
                                c['verification/lean-mathlib/OIBridge/HexLatticeGas.lean'].replace(b'def hexGas', b'def hexGas2', 1)),
        'structural change outside string constants or comments')
    mut('MT-added-file', lambda c: c.__setitem__('papers/New.md', b'x'), 'file added outside the record directory')
    mut('MT-deleted-file', lambda c: c.pop('papers/SM.md'), 'file deleted')
    mut('MT-tex-hand-edit (papers/GR.tex with one word changed)',
        lambda c: c.__setitem__('papers/GR.tex', c['papers/GR.tex'].replace(b'the ', b'teh ', 1)), 'papers/GR.tex: differs from its rebuild')
    mut('MT-tex-untouched (papers/Juno.tex, whose source is not ledgered)',
        lambda c: c.__setitem__('papers/Juno.tex', c['papers/Juno.tex'] + b'%x\n'), 'papers/Juno.tex')
    mut('MT-sc42-hand-edit (the SC-42 result edited)',
        lambda c: c.__setitem__(SC42, c[SC42].replace(b'"ok": true', b'"ok": false', 1)), 'differs from the SC-42 checker')
    mut('MT-sc42-not-regenerated (the candidate is not a git checkout)', lambda c: None, 'not regenerated',
        dict(reg, sc42=None))
    mut('MT-coverage-unnamed-fingerprint (every fingerprint set to deadbeef)',
        lambda c: c.__setitem__(COVERAGE, re.sub(rb'"fingerprint": "[0-9a-f]+"', b'"fingerprint": "deadbeef"', c[COVERAGE])), COVERAGE)
    mut('MT-coverage-named-wrong (MAIN:L-3 with its base fingerprint)',
        lambda c: c.__setitem__(COVERAGE, set_fingerprints(c[COVERAGE], {'MAIN:L-3': '5c04b07980b2be97'})), COVERAGE)
    mut('MT-coverage-field (a field other than a fingerprint)',
        lambda c: c.__setitem__(COVERAGE, c[COVERAGE].replace(b'"kernel": "GAP"', b'"kernel": "K3"', 1)), COVERAGE)
    mut('MT-ledger-replaced (the record\'s ledger.json replaced by {})',
        lambda c: c.__setitem__(LEDGER, b'{}'), 'ledger.json: record file differs from the plan')
    mut('MT-checker-replaced (the record\'s preserve_check.py replaced)',
        lambda c: c.__setitem__(SELF, b'print("RESULT PASS")\n'), 'preserve_check.py: record file differs from the plan')
    mut('MT-record-added (a new record file outside execution/)',
        lambda c: c.__setitem__(REC + 'NOTE.md', b'x'), 'record file not in the plan')
    c = dict(good); c[REC + 'execution/RESULT.md'] = b'execution record'
    expect(not compare(led, base_files, c, plan, reg)[0], 'a new execution record under execution/ passes')
    c = dict(good); c['papers/GR.pdf'] = b'rebuilt'
    b, p = compare(led, base_files, c, plan, reg)
    expect(not b and p == ['papers/GR.pdf'], 'a rebuilt PDF of a ledgered source is left to the CI build')
    if shutil.which('pdftotext') and shutil.which('pdfinfo'):
        d1, d2 = tempfile.mkdtemp(prefix='a1exit-pdf-'), tempfile.mkdtemp(prefix='a1exit-pdf-')
        try:
            for d, src in ((d1, 'papers/GR.pdf'), (d2, 'papers/GR.pdf')):
                os.makedirs(os.path.join(d, 'papers')); open(os.path.join(d, 'papers/GR.pdf'), 'wb').write(base_files[src])
            expect(not pdf_compare(d1, d2, ['papers/GR.pdf']), 'pdf compare: a PDF equal in pages and text to the built one passes')
            open(os.path.join(d2, 'papers/GR.pdf'), 'wb').write(base_files['papers/Main.pdf'])
            expect(bool(pdf_compare(d1, d2, ['papers/GR.pdf'])), 'pdf compare: a committed PDF that is not the built one fails')
            os.remove(os.path.join(d2, 'papers/GR.pdf'))
            expect(bool(pdf_compare(d1, d2, ['papers/GR.pdf'])), 'pdf compare: a PDF the CI build did not make fails')
        finally:
            shutil.rmtree(d1, ignore_errors=True); shutil.rmtree(d2, ignore_errors=True)
    else:
        expect(False, 'pdf compare: pdftotext and pdfinfo are required')
    t = json.loads(json.dumps(led)); t['splices'][0]['old_sha256'] = '0' * 64
    expect(bool(validate_ledger(t, base_files)), 'a ledger whose old-text hash does not match the base is rejected')
    t = json.loads(json.dumps(led)); t['splices'][1]['start'] = t['splices'][0]['start']
    expect(bool(validate_ledger(t, base_files)), 'a ledger with a moved or overlapping span is rejected')
    p2 = dict(plan); p2[LEDGER] = plan[LEDGER] + b' '
    expect(any('ledger.json does not match' in x for x in verify_pins(p2, plan[SELF])), 'pins: a replaced ledger.json fails its pinned digest')
    expect(any('this checker is not the plan' in x for x in verify_pins(plan, plan[SELF] + b'#')), 'pins: a modified checker refuses to run as the plan\'s')
    p3 = dict(plan); p3[REC + 'edits.json'] = plan[REC + 'edits.json'] + b'\n'
    expect(bool(verify_pins(p3, plan[SELF])), 'pins: an edits.json the ledger was not built from fails')
    d3 = tempfile.mkdtemp(prefix='a1exit-res-')
    try:
        doc = write_result(os.path.join(d3, 'r.json'), 'self-test', {'plan': None},
                           [{'name': 'x', 'status': 'pass', 'discrepancies': []}, {'name': 'y', 'status': 'fail', 'discrepancies': ['z']}])
        back = json.load(open(os.path.join(d3, 'r.json'), encoding='utf-8'))
        expect(back == doc and back['verdict'] == 'fail' and back['checks'][1]['status'] == 'fail',
               'result file: it parses, and a failing check is recorded as fail with its discrepancy')
    finally:
        shutil.rmtree(d3, ignore_errors=True)
    print('self-test %s' % ('PASS' if ok else 'FAIL'))
    return ok


def tree_mutants(d, led, base_files, plan):
    """Mutate the candidate directory in place, one change at a time, and restore it."""
    ok = True
    cases = [('papers/GR.tex', lambda b: b.replace(b'the ', b'teh ', 1), 'differs from its rebuild'),
             (SC42, lambda b: b.replace(b'"ok": true', b'"ok": false', 1), 'differs from the SC-42 checker'),
             (LEDGER, lambda b: b'{}', 'record file differs from the plan'),
             (SELF, lambda b: b'print("RESULT PASS")\n', 'record file differs from the plan'),
             (COVERAGE, lambda b: re.sub(rb'"fingerprint": "[0-9a-f]+"', b'"fingerprint": "deadbeef"', b, count=1), COVERAGE)]
    for path, f, want in cases:
        fp = os.path.join(d, path)
        orig = open(fp, 'rb').read()
        open(fp, 'wb').write(f(orig))
        try:
            cand = tree_dir(d)
            bad, _ = compare(led, base_files, cand, plan, regenerate(cand, d, base_files))
        finally:
            open(fp, 'wb').write(orig)
        hit = any(want in x for x in bad)
        ok &= hit
        record('tree mutant %s fails with "%s"' % (path, want), hit, [] if hit else ['the mutation was not detected'])
        print('  %s tree mutant %s: fails with "%s"' % ('ok ' if hit else 'BAD', path, want))
    return ok


TEX = {}
RESULTS = []


def record(name, ok, discrepancies=()):
    RESULTS.append({'name': name, 'status': 'pass' if ok else 'fail', 'discrepancies': list(discrepancies)})


def write_result(path, mode, meta, checks):
    """The structured result (§A.44): each check's name, status and discrepancies, and the verdict."""
    doc = dict(meta, schema='a1exit-checker-result-v1', checker='preserve_check.py', mode=mode, checks=checks,
               verdict='pass' if checks and all(c['status'] == 'pass' for c in checks) else 'fail')
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(doc, f, indent=1, sort_keys=True, ensure_ascii=False)
        f.write('\n')
    return doc


def result_paths(explicit, mode):
    out = [explicit] if explicit else []
    rt = os.environ.get('RUNNER_TEMP')
    if rt and os.path.isdir(os.path.join(rt, 'out')):
        out.append(os.path.join(rt, 'out', 'preserve_check-%s.json' % mode))
    return out


def main():
    global TEX
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument('--build-ledger', action='store_true')
    g.add_argument('--verify-ledger', action='store_true')
    g.add_argument('--verify-pins', action='store_true')
    g.add_argument('--commit')
    g.add_argument('--tree')
    g.add_argument('--self-test', action='store_true')
    ap.add_argument('--plan')
    ap.add_argument('--base')
    ap.add_argument('--mutants', action='store_true')
    ap.add_argument('--result-json', metavar='PATH', help='write the structured result here (also to RUNNER_TEMP/out/ when '
                    'that directory exists)')
    ap.add_argument('--pdf-compare', metavar='BUILT', help='with --tree: compare the committed PDFs of the ledgered sources '
                    'with those the CI build wrote under BUILT (page count and pdftotext text)')
    a = ap.parse_args()
    if a.build_ledger:
        eb = open(os.path.join(ROOT, EDITS), 'rb').read()
        edits = json.loads(eb)
        led = build_ledger(edits, tree_of(edits['drafting_base']), eb)
        open(os.path.join(ROOT, LEDGER), 'w', encoding='utf-8').write(json.dumps(led, indent=1, ensure_ascii=False) + '\n')
        print('ledger: %d splices in %d files at %s (%d retained-site records); sha256 %s' % (
            len(led['splices']), len(led['files']), led['base'][:12], len(led['retained_unchanged']),
            sha(open(os.path.join(ROOT, LEDGER), 'rb').read())))
        return
    plan = plan_files(a.plan)
    own = open(os.path.abspath(__file__), 'rb').read()
    pin_bad = verify_pins(plan, own)
    print('plan: %s; %d record files; pin findings %d' % (a.plan or 'working checkout (not a designated plan commit)', len(plan), len(pin_bad)))
    for x in pin_bad:
        print('  PIN ' + x)
    record('record pins (PREREG §26.4) and the plan\'s own checker', not pin_bad, pin_bad)
    led = json.loads(plan[LEDGER])
    TEX = tex_sources(led)
    base = tree_of(a.base or led['base'])
    bad = validate_ledger(led, base)
    print('ledger: %d splices in %d files at %s; sha256 %s; %d validation findings'
          % (len(led['splices']), len(led['files']), led['base'][:12], sha(plan[LEDGER]), len(bad)))
    for x in bad:
        print('  LEDGER ' + x)
    record('ledger spans and hashes at the base', not bad, bad)
    ok = not bad and not pin_bad
    mode = ('verify-pins' if a.verify_pins else 'verify-ledger' if a.verify_ledger else 'self-test' if a.self_test
            else 'commit' if a.commit else 'tree')
    if a.verify_pins:
        pass
    elif a.verify_ledger:
        re_led = build_ledger(json.loads(plan[EDITS]), base, plan[EDITS])
        same = re_led == led
        print('ledger re-derived from edits.json: %s' % ('identical' if same else 'DIFFERENT'))
        record('ledger re-derived from edits.json', same, [] if same else ['the re-derived ledger differs'])
        ok = ok and same
    elif a.self_test:
        ok = self_test(led, base, plan) and ok
    else:
        work = None
        if a.commit:
            work = tempfile.mkdtemp(prefix='a1exit-cand-')
            os.rmdir(work)
            git('worktree', 'add', '--detach', work, a.commit)
        try:
            d = a.tree or work
            cand = tree_dir(d)
            fails, pdfs = compare(led, base, cand, plan, regenerate(cand, d, base))
            print('candidate: %d findings; PDFs of ledgered sources rebuilt (checked by the CI build): %d' % (len(fails), len(pdfs)))
            for x in fails:
                print('  FAIL ' + x)
            for x in pdfs:
                print('  PDF ' + x)
            record('candidate against base, ledger, regenerated artifacts and plan record', not fails, fails)
            ok = ok and not fails
            if a.pdf_compare and a.tree:
                pb = pdf_compare(a.tree, a.pdf_compare, {t[:-4] + '.pdf' for t in TEX})
                print('pdf compare against the CI build: %d findings' % len(pb))
                for x in pb:
                    print('  FAIL ' + x)
                record('committed PDFs against the CI build (pages, pdftotext)', not pb, pb)
                ok = ok and not pb
            if a.mutants and a.tree:
                ok = tree_mutants(a.tree, led, base, plan) and ok
        finally:
            if work:
                git('worktree', 'remove', '--force', work)
    meta = {'plan': a.plan, 'ledger_sha256': sha(plan[LEDGER]), 'ledger_base': led['base'],
            'candidate': a.commit or (os.path.abspath(a.tree) if a.tree else None), 'base': a.base or led['base']}
    if not ok and all(c['status'] == 'pass' for c in RESULTS):
        record('overall', False, ['a check failed without a recorded entry'])
    for pth in result_paths(a.result_json, mode):
        write_result(pth, mode, meta, RESULTS)
    print('RESULT ' + ('PASS' if ok else 'FAIL'))
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
