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
  python3 -I -B .../preserve_check.py --reconcile REV         the ledger at REV, splice by splice, against the current
                                                              ledger and base: unchanged, shifted by a base change
                                                              before it, revised at §31, or drift (PREREG §31.2)

  python3 -I -B .../preserve_check.py --verify-run RESULT.json --run-meta RUN.json --plan P [--workflow-base W] [--main REV]
                                                              a trial dispatch's result.json is valid or void: its
                                                              executed workflow commit, the host run record's head_sha
                                                              (RUN.json), on main's first-parent history, containing W
                                                              with W's workflow blob, equal to the self-reported
                                                              workflow_sha and ref_sha, and its trial_sha a single-parent
                                                              child of the ledger base (PREREG §31.12.7, §31.12.8);
                                                              with --run-meta-redacted COPY, a retained redacted copy
                                                              must keep its fields and types and verdict (§31.12.13)
  python3 -I -B .../preserve_check.py --expect-trial T0|T1 --run-out OUT --plan P --jobs JOBS.json --built DIR --trial-sha T --run-id N
                                                              --run-meta RUN.json
                                                              a trial run's outputs against the expected result of
                                                              PREREG §31.12.13: B1's PDF findings, the expected skips
  python3 -I -B .../preserve_check.py --expect-verify JOBS.json --plan P --trial-sha T --run-id N
                                                              T1′'s verify.yml jobs record against its expected skips

In every candidate mode the scope assertions of PREREG §31.7 item 6 (SCOPE_PRESENT, SCOPE_ABSENT) are a recorded check.

--plan REV   the plan commit the owner designates when authorizing execution. The ledger, the pin table and the record
             directory are read from REV's objects, never from the candidate or the working checkout, and this script's
             own bytes must equal REV's copy of it. Without --plan the plan is the working checkout (reported as such);
             its files must still match the pins of PREREG §26.4.
--base REV   compare against REV (a later main) instead of the ledger base; refused unless every ledgered file is
             byte-identical at REV and at the ledger base.
--pdf-compare BUILT
             with --tree: every committed PDF of a ledgered source has the page count and the pdftotext text of the PDF
             the CI build (build.sh) made from the same tree under BUILT. Fails closed (PREREG §31.12.1): the run's
             build.rc is 0, the PDF is a row of its pdf-pages.tsv with the built file's page count, and the built PDF
             is not byte-identical to the committed one; both files are read from --pdf-out DIR, default BUILT/../out.
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
PINNED = ['edits.json', 'ledger.json', 'edits_check.py', 'guards_check.py', 'preserve_check.py', 't0_jobs_44939798305.json']
T0_JOBS = 't0_jobs_44939798305.json'  # §31.12.16: T0's real host jobs record, GET .../runs/44939798305/jobs?per_page=100
BOOK = 'book/The-Incompleteness-of-Observation-FULL'
HEADER = 'tools/unicode-fix.tex'
COVERAGE = 'verification/coverage/LEDGER.json'
STALE = ['MAIN:L-3', 'STRUCTURE:P-9.5', 'SUBSTRATUM:C-effective-finiteness-gauge-class-transfer', 'SUBSTRATUM:T-23',
         # amendment §31, nit 5 (D389-D391): the statements of SM Lemma 1c, Proposition 4b and Theorem 19
         'SM:L-1c-canonical-projection-resummed-kernel', 'SM:P-4b-symmetric-point-custodial-scalarity-component', 'SM:T-19']
# Amendment §31 (PREREG §31.7 item 6): the corrected sentences the candidate must carry, and the superseded forms it must
# not, at the sites of the final scientific review (#1477 c.7074137435); the last two present entries are #1494's book
# statement of Theorem 24(i), on main at the base.
_FC = 'of a finite $\\mathcal{C}_H$'
_SUB, _FULL, _CH2, _CH3, _CH4 = ('papers/Substratum.md', BOOK + '.md', 'book/ch02-substratum.md',
                                 'book/ch03-structural-realism.md', 'book/ch04-methodology.md')
SCOPE_PRESENT = [
    (_SUB, 'no established form for a substratum of unspecified cardinality'),
    (_SUB, 'Corollary (near-return) of [Main §2.3], of which an exact return is a case'),
    (_SUB, 'what is open for a substratum of unspecified cardinality is a source of the return hypothesis'),
    (_SUB, 'a meromorphic continuation of the memory-resummed Schur complement that is not established'),
    (_SUB, 'These do not by themselves extend the complete reconstruction theorem'),
    (_SUB, 'for any density matrix $\\sigma_A$ with $\\operatorname{Tr}\\sigma_A=1$ on a Hilbert space'),
    (_SUB, 'for a classical factor with $\\alpha(A)=1$'),
    (_SUB, 'a density matrix $\\sigma_A$ on $\\ell^2(A)$'),
    (_SUB, 'for $S$ of unspecified cardinality bijectivity is the reversibility posit (REV)'),
    (_SUB, 'thus, for a finite $S$, partly structural'),
    ('papers/Structure.md', 'uniform hidden-coordinate relabelling ' + _FC),
    ('papers/SM.md', 'Lemma 3 on a finite representative'),
    ('papers/SM.md', 'counting measure on a finite representative'),
    ('papers/SM.md', 'the counting measure on a finite $\\mathcal{C}_H$'),
    ('papers/Main.md', 'every representative, or channel-preserving extension,'),
    ('papers/Complexity.md', 'uniform relabelling of a finite set of hidden configurations'),
    ('papers/Methodology.md', 'a permutation of a finite set of hidden states'),
] + [(f, s) for f in (_CH2, _FULL) for s in ('uniform hidden-coordinate relabelling ' + _FC + ' and',
                                              'uniform hidden-coordinate relabelling ' + _FC + ', with the uniform hidden prior')] \
  + [(f, s) for f in (_CH3, _FULL) for s in ('A single hidden permutation ' + _FC,
                                              'A uniform hidden-coordinate relabelling ' + _FC + ' preserves',
                                              'A uniform hidden-coordinate relabelling ' + _FC + ', or')] \
  + [(f, 'Uniform hidden relabelling ' + _FC) for f in (_CH4, _FULL)] \
  + [(f, 'For a finite set of hidden configurations $\\mathcal{C}_H$ with the uniform hidden prior and any bijection')
     for f in (_CH2, _FULL)]
SCOPE_ABSENT = [
    ('papers/Structure.md', 'states uniform hidden-coordinate relabelling and independently'),
    ('papers/Complexity.md', 'uniform hidden relabelling preserves the coherent channel'),
    ('papers/Methodology.md', 'by a permutation of the hidden states applied uniformly'),
] + [(f, s) for f in (_CH2, _FULL) for s in ('uniform hidden-coordinate relabelling and independently prepared finite',
                                              'A uniform hidden-coordinate relabelling, with the uniform hidden prior')] \
  + [(f, s) for f in (_CH3, _FULL) for s in ('A single hidden permutation used identically',
                                              'A uniform hidden-coordinate relabelling preserves the coherent',
                                              'A uniform hidden-coordinate relabelling, or an independently')] \
  + [(f, 'Uniform hidden relabelling and an independently prepared') for f in (_CH4, _FULL)]
# §31.12 (R2, R3): the finite alphabet of waveSubstratum_A1, and the finite instances of the ensemble and observer-theory
# results, in the Lean docstrings, the census registry and the README.
_FIN = 'with finitely many sites and a finite alphabet'
_OI = 'verification/lean-mathlib/OIBridge/'
SCOPE_PRESENT += [
    (_OI + 'SubstratumInterfaceAudit.lean', 'the finiteness predicate `A1` for a finite torus and a finite alphabet'),
    ('verification/lean-manuscript-census.json', '(Q1; the finiteness predicate for a finite torus and a finite alphabet)'),
    ('verification/README.md', 'satisfies the finiteness predicate `A1` for a finite alphabet and A2'),
    (_OI + 'StochasticInterface.lean', 'FOR EVERY SUBSTRATUM WITH FINITELY MANY SITES, A FINITE ALPHABET, A LINEAR'),
    (_OI + 'StochasticInterface.lean', 'For every substratum ' + _FIN + ' whose'),
    (_OI + 'LiftSource.lean', 'the observer theory of every substratum\n  ' + _FIN + ' has its swap layer'),
    (_OI + 'ExecSource.lean', 'the observer theory of every substratum ' + _FIN + ' executes'),
    ('verification/README.md', 'the observer theory of every substratum ' + _FIN + ' executes no such flow'),
    ('verification/README.md', 'the observer theory of every substratum ' + _FIN + ' at its own'),
    ('verification/README.md', 'every substratum ' + _FIN + ' (`permTheory_nonnegBounded`'),
]
SCOPE_PRESENT += [
    (_OI + 'A6Instantiation.lean', "the manuscripts' finite representatives, configurations over a finite periodic quotient"),
    (_OI + 'A6Instantiation.lean', '(`SM.md` §4.1, §4.4), are finite objects'),
    (_OI + 'A6Instantiation.lean', '**The finiteness predicate `A1` is\nnot weakened**'),
    (_OI + 'A6Instantiation.lean', "because the interface's finiteness predicate `A1` requires a finite configuration space\n  and"),
    (_OI + 'A6Instantiation.lean', "because the interface's finiteness predicate `A1` requires a finite\nconfiguration space and"),
]
SCOPE_ABSENT += [
    (_OI + 'A6Instantiation.lean', "the manuscripts' substratum is the finite object of"),
    (_OI + 'A6Instantiation.lean', "finiteness is the first of the interface's axioms"),
    (_OI + 'A6Instantiation.lean', '**the finiteness predicate `A1` is\nnot weakened**'),
    (_OI + 'SubstratumInterfaceAudit.lean', 'the finiteness predicate `A1` on a finite torus and'),
    (_OI + 'StochasticInterface.lean', 'FAILS FOR EVERY SUBSTRATUM WITH A LINEAR RULE'),
    (_OI + 'StochasticInterface.lean', 'For every substratum whose rule is'),
    (_OI + 'LiftSource.lean', 'the observer theory of every substratum\n  has its swap layer'),
    (_OI + 'ExecSource.lean', 'the observer theory of every substratum executes no layer flow'),
    ('verification/README.md', 'the observer theory of every substratum executes no such flow'),
    ('verification/README.md', 'every substratum (`permTheory_nonnegBounded`'),
]
# --reconcile: the records amendment §31 revises (their replacement changes; D369's old text is extended) and adds.
REVISED31 = {'D026', 'D231', 'D363', 'D364', 'D369', 'D276', 'D326', 'D332', 'D319'}  # §31.3, §31.12 (R2), §31.12.9 (R-8)
NEW31 = {'D%03d' % n for n in range(374, 402)}  # D374-D391 (§31.3), D392-D398 (§31.12), D399 (§31.12.9), D400-D401 (§31.12.11)
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
    """The digest table of the last "Record pins" subsection of PREREG (§26.4 for P*, §31.11 from amendment §31):
    rows "| `file` | `sha256` |"."""
    t = prereg.decode('utf-8')
    heads = [m.start() for m in re.finditer(r'^### \d+\.\d+ Record pins\b', t, re.M)]
    if not heads:
        return {}
    i = heads[-1]
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


def pdf_page_count(path):
    """The page count pdfinfo reports for a PDF (N11, §31.12.15); an error when pdfinfo cannot read it."""
    info = subprocess.run(['pdfinfo', path], capture_output=True, text=True, check=True).stdout
    return int(re.search(r'^Pages:\s+(\d+)', info, re.M).group(1))


class PdfinfoUnavailable(Exception):
    pass


def _page_count(path):
    """N12 (§31.12.16): pdf_page_count, with an OSError (pdfinfo absent or not runnable) raised as PdfinfoUnavailable."""
    try:
        return pdf_page_count(path)
    except OSError as e:
        raise PdfinfoUnavailable(str(e))


def pdf_out_dir(built_dir, explicit=None):
    """The run's output directory: --pdf-out, or BUILT/../out (the workflow's $RUNNER_TEMP/out beside $RUNNER_TEMP/build)."""
    return explicit or os.path.join(os.path.dirname(os.path.abspath(built_dir).rstrip(os.sep)), 'out')


def pdf_compare(cand_dir, built_dir, paths, out_dir=None):
    """Fails closed (PREREG §31.12.1): a ledgered PDF's comparison counts only when the run's CI build succeeded
    (build.rc 0), recorded it (a row of pdf-pages.tsv whose page count is the built file's) and rebuilt it (the built
    file is not byte-identical to the committed one); then committed and built must agree in pages and text."""
    bad = []
    out = pdf_out_dir(built_dir, out_dir)
    rc_path, tsv_path = os.path.join(out, 'build.rc'), os.path.join(out, 'pdf-pages.tsv')
    rc = open(rc_path, encoding='utf-8').read().strip() if os.path.isfile(rc_path) else None
    if rc != '0':
        bad.append('the CI build did not succeed (build.rc %s in %s)' % ('absent' if rc is None else repr(rc), out))
    if not paths:
        bad.append('no ledgered PDF to compare: an empty comparison does not pass')
    rows = None
    if os.path.isfile(tsv_path):
        rows = {}
        for line in open(tsv_path, encoding='utf-8').read().splitlines():
            if line.strip():
                cols = line.split('\t')
                if len(cols) != 2 or not cols[1].strip().isdigit():
                    bad.append('malformed build record row in pdf-pages.tsv: %r' % line)
                    continue
                if cols[0] in rows:
                    bad.append('duplicate build record row in pdf-pages.tsv for %s' % cols[0])
                    continue
                rows[cols[0]] = cols[1].strip()
    else:
        bad.append('no build record: pdf-pages.tsv absent from %s' % out)
    for p in sorted(paths):
        a, b = os.path.join(cand_dir, p), os.path.join(built_dir, p)
        if rows is not None and p not in rows:
            bad.append('%s: not rebuilt by the CI build (absent from pdf-pages.tsv)' % p)
        if not os.path.isfile(a) or not os.path.isfile(b):
            bad.append('%s: missing in the candidate or in the CI build' % p); continue
        if open(a, 'rb').read() == open(b, 'rb').read():
            bad.append('%s: stale: the built PDF is byte-identical to the committed one, so it was not rebuilt' % p)
        (pa, ta), (pb, tb) = pdf_facts(a), pdf_facts(b)
        if rows is not None and p in rows and rows[p] != str(pb):
            bad.append('%s: pdf-pages.tsv records %s pages, the built PDF has %d' % (p, rows[p], pb))
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


def scope_check(cand):
    """PREREG §31.7 item 6: every corrected sentence present, every superseded form absent."""
    bad = []
    for f, s in SCOPE_PRESENT:
        if s.encode('utf-8') not in cand.get(f, b''):
            bad.append('scope assertion: %s lacks %r' % (f, s[:70]))
    for f, s in SCOPE_ABSENT:
        if s.encode('utf-8') in cand.get(f, b''):
            bad.append('scope assertion: %s still carries %r' % (f, s[:70]))
    return bad


def changed_region(a, b):
    """(start, end in a, end in b) of the one region enclosing every difference between a and b, or None."""
    if a == b:
        return None
    p = 0
    while p < min(len(a), len(b)) and a[p] == b[p]:
        p += 1
    q = 0
    while q < min(len(a), len(b)) - p and a[-1 - q] == b[-1 - q]:
        q += 1
    return p, len(a) - q, len(b) - q


def reconcile(old_led, led, old_base, base):
    """PREREG §31.2: each splice of an earlier ledger against the current ledger and base. A splice keeps its bytes and is
    unchanged (same span), or shifted by exactly the length change of a base difference wholly before it; a record of
    REVISED31 keeps its file (and, except D369, its old bytes and span); a splice anywhere else is drift."""
    new = {x['id']: x for x in led['splices']}
    rows, drift, regions = [], [], {}
    for x in old_led['splices']:
        f, y = x['file'], new.get(x['id'])
        if f not in regions:
            regions[f] = changed_region(old_base.get(f, b''), base.get(f, b''))
        reg = regions[f]
        if y is None or y['file'] != f:
            drift.append('%s: absent from the current ledger or in another file' % x['id']); continue
        old_bytes = old_base[f][x['start']:x['end']]
        same = y['old_sha256'] == x['old_sha256'] and y['new'] == x['new']
        if x['id'] in REVISED31 and not (same and (y['start'], y['end']) == (x['start'], x['end'])):
            if x['id'] == 'D369':
                ok = old_bytes in base[f][y['start']:y['end']]
            else:
                ok = y['old_sha256'] == x['old_sha256'] and (y['start'], y['end']) == (x['start'], x['end'])
            rows.append((x['id'], f, 'revised at §31', 0))
            if not ok:
                drift.append('%s: revised record does not keep its old text' % x['id'])
            continue
        if y['old_sha256'] != x['old_sha256'] or y['new'] != x['new']:
            drift.append('%s: old or new bytes differ' % x['id']); continue
        shift = y['start'] - x['start']
        if shift == 0 and (reg is None or x['end'] <= reg[0] or (x['start'] >= reg[1] and reg[2] == reg[1])):
            rows.append((x['id'], f, 'unchanged', 0))
        elif reg is not None and x['start'] >= reg[1] and shift == (reg[2] - reg[1]) and y['end'] - y['start'] == x['end'] - x['start']:
            rows.append((x['id'], f, 'shifted by the base change at bytes %d-%d' % (reg[0], reg[1]), shift))
        else:
            drift.append('%s: span moved by %+d, not explained by a base change before it' % (x['id'], shift))
    added = sorted(set(new) - {x['id'] for x in old_led['splices']})
    for i in added:
        if i not in NEW31:
            drift.append('%s: splice added outside the records of amendment §31' % i)
    if set(old_led.get('retained_unchanged', [])) != set(led.get('retained_unchanged', [])):
        drift.append('retained-site records differ')
    return rows, added, drift


WORKFLOW = '.github/workflows/a1exit-trial-verify.yml'
WORKFLOW_BASE = '413b0bb88f39cad901befcf4684355c7ee39480b'  # PREREG §31.12.7: #1543 merged, the nine-PDF trial workflow


def _git_ok(*a):
    return subprocess.run(['git', '-C', ROOT] + list(a), capture_output=True).returncode == 0


def _blob(rev, path):
    r = subprocess.run(['git', '-C', ROOT, 'rev-parse', '%s:%s' % (rev, path)], capture_output=True, text=True)
    return r.stdout.strip() if r.returncode == 0 else None


def verify_run(res, meta, ledger_base, workflow_base, main_rev, plan_sha):
    """PREREG §31.12.7 and §31.12.8. The executed workflow commit is the host run record's head_sha, never a value the
    run reports about itself: (3) the run record (the host API's GET .../actions/runs/{run_id}, saved whole) is present,
    is that run, a first-attempt workflow_dispatch of the trial workflow from main; (4) its head_sha is on main's
    first-parent history, contains the workflow base and carries the workflow base's workflow blob, and result.json's
    workflow_sha and ref_sha each equal it; (2) trial_sha has exactly one parent, the ledger base. Any failure, and any
    missing or malformed value, voids the run; no check is skipped for a missing value (§31.12.10, R5)."""
    bad = []
    if not isinstance(res, dict):
        return ['result.json is not a JSON object']
    # N8 (§31.12.12): the run is bound to the designated plan commit
    if not isinstance(plan_sha, str) or not re.fullmatch(r'[0-9a-f]{40}', plan_sha):
        bad.append('no designated plan: --plan %r missing or not a full commit id' % (plan_sha,))
    rp = res.get('plan_sha')
    if not isinstance(rp, str) or not re.fullmatch(r'[0-9a-f]{40}', rp):
        bad.append('result.json plan_sha %r missing or not a full commit id' % (rp,))
    elif rp != plan_sha:
        bad.append('result.json plan_sha %s is not the designated plan %s' % (rp[:12], str(plan_sha)[:12]))
    head = None
    if not isinstance(meta, dict) or not meta:
        bad.append('run metadata missing: no host record of the run, so the executed workflow commit is unverified')
    else:
        rid, mid = res.get('run_id'), meta.get('id')
        if rid is None or mid is None or str(mid) != str(rid):
            bad.append('run record id %r is not result.json run_id %r (both must be present and equal)' % (mid, rid))
        if meta.get('event') != 'workflow_dispatch':
            bad.append('run event %r, not workflow_dispatch' % meta.get('event'))
        if meta.get('path') != WORKFLOW:
            bad.append('run workflow path %r, not %s' % (meta.get('path'), WORKFLOW))
        if meta.get('head_branch') != 'main':
            bad.append('run head_branch %r, not main' % meta.get('head_branch'))
        if 'inputs' in meta:
            inp = meta.get('inputs')
            if not isinstance(inp, dict) or inp.get('plan_sha') != plan_sha:
                bad.append('host record inputs %r do not carry the designated plan %s' % (inp, str(plan_sha)[:12]))
        if type(meta.get('run_attempt')) is not int or meta.get('run_attempt') != 1:
            bad.append('run attempt %r, not 1' % meta.get('run_attempt'))
        head = meta.get('head_sha')
        if not isinstance(head, str) or not re.fullmatch(r'[0-9a-f]{40}', head):
            bad.append('run record head_sha %r missing or not a full commit id: the executed workflow commit is unverified'
                       % (head,))
            head = None
    if head is not None:
        if not _git_ok('cat-file', '-e', head + '^{commit}'):
            bad.append('run head_sha %r is not a known full commit id' % head)
        else:
            first = set(git('rev-list', '--first-parent', main_rev).decode().split())
            if head not in first:
                bad.append('run head_sha %s is not on the first-parent history of main (%s)' % (head[:12], main_rev))
            if not _git_ok('merge-base', '--is-ancestor', workflow_base, head):
                bad.append('run head_sha %s does not contain the workflow base %s' % (head[:12], workflow_base[:12]))
            want = _blob(workflow_base, WORKFLOW)
            if want is None or _blob(head, WORKFLOW) != want:
                bad.append('run head_sha %s: %s differs from its blob at the workflow base' % (head[:12], WORKFLOW))
    for k in ('workflow_sha', 'ref_sha'):  # unconditional: a self-report never stands in for the host's head_sha
        if head is None or res.get(k) != head:
            bad.append('result.json %s %r differs from the run\'s head_sha %s (self-reported, not the executed commit)'
                       % (k, res.get(k), str(head)[:12]))
    tr = res.get('trial_sha')
    if not isinstance(tr, str) or not re.fullmatch(r'[0-9a-f]{40}', tr) or not _git_ok('cat-file', '-e', tr + '^{commit}'):
        bad.append('trial_sha %r is not a known commit' % tr)
    else:
        parents = git('rev-list', '--parents', '-n', '1', tr).decode().split()[1:]
        if parents != [ledger_base]:
            bad.append('trial_sha %s has parents %s, not exactly the ledger base %s' % (tr[:12], [x[:12] for x in parents], ledger_base[:12]))
    return bad


# ---- §31.12.13: the redacted host record, and the trial's expected result ------------------------------------

RUN_FIELDS = (('id', int), ('event', str), ('path', str), ('head_branch', str), ('head_sha', str), ('run_attempt', int))


def redact_run(meta):
    """The run object with every key named email removed, at any depth (§A.42 item 4)."""
    if isinstance(meta, dict):
        return {k: redact_run(v) for k, v in meta.items() if k != 'email'}
    if isinstance(meta, list):
        return [redact_run(v) for v in meta]
    return meta


def _has_email(v):
    if isinstance(v, dict):
        return 'email' in v or any(_has_email(x) for x in v.values())
    return isinstance(v, list) and any(_has_email(x) for x in v)


def verify_redacted(orig, copy, res, ledger_base, workflow_base, main_rev, plan_sha):
    """PREREG §31.12.13: a retained redacted copy keeps every field verify_run reads with the same value and JSON type,
    removes the e-mail fields and nothing else, and gives verify_run's findings on the original exactly."""
    if not isinstance(orig, dict) or not isinstance(copy, dict):
        return ['redacted copy: the original or the copy is not a JSON object']
    bad = []
    for k, t in RUN_FIELDS + (('inputs', dict),):
        if k == 'inputs' and k not in orig:
            continue
        if k not in copy:
            bad.append('redacted copy lacks %s, which verify_run reads' % k)
        elif type(copy[k]) is not type(orig[k]) or copy[k] != orig[k]:
            bad.append('redacted copy changes %s: %r (%s) in the original, %r (%s) in the copy'
                       % (k, orig[k], type(orig[k]).__name__, copy[k], type(copy[k]).__name__))
    if not _has_email(orig):
        bad.append('the original run record carries no email field, so it is not the host\'s original record')
    if _has_email(copy):
        bad.append('redacted copy still carries an email field')
    elif copy != redact_run(orig):
        bad.append('redacted copy differs from the original in more than its email fields')
    a = verify_run(res, orig, ledger_base, workflow_base, main_rev, plan_sha)
    b = verify_run(res, copy, ledger_base, workflow_base, main_rev, plan_sha)
    if a != b:
        bad.append('redacted copy: verify_run differs from the original (%d against %d findings)' % (len(b), len(a)))
    return bad


PDF_CHECK = 'committed PDFs against the CI build (pages, pdftotext)'
TRIAL_STEPS = ('inputs', 'checkout', 'head', 'python', 'toolchain', 'plan', 'build', 'preserve', 'guards')
# host step names of a1exit-trial-verify.yml at the workflow base whose conclusion at T0 is not success
T0_HOST = {"P's preserve_check.py --commit, then --tree --mutants --pdf-compare": 'failure',
           "P's guards_check.py --mutants": 'skipped',
           'Every required step succeeded (a skipped step fails)': 'failure',
           # R8 (§31.12.16): skipped in T0's real record, where preserve failed; success in T1's passing run
           'Post Run actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065': 'skipped'}
# verify.yml at H on workflow_dispatch: the steps skipped by design, by (job, step)
VERIFY_SKIPS = {('Mathlib bridge', 'KTRANS-SEP-2 marker complete reports with an axiom outside the three'): 'skipped'}
VERIFY_JOBS = (  # §31.12.15: the 41 jobs of verify.yml at H on workflow_dispatch, from T1's run of it (ci-record.json)
    'Lean kernel check',
    'Mathlib bridge',
    'Numerical probes',
    'Numerical probes / A36 hierarchy',
    'Numerical probes / A38 escape',
    'Numerical probes / A40 locus',
    'Numerical probes / A41 hulls',
    'Numerical probes / A41 independent',
    'Numerical probes / A41 production',
    'Numerical probes / A42 census01',
    'Numerical probes / A42 exclusion (cubes:0)',
    'Numerical probes / A42 exclusion (cubes:1)',
    'Numerical probes / A42 exclusion (cubes:2)',
    'Numerical probes / A42 exclusion (dfs:0)',
    'Numerical probes / A42 exclusion (dfs:1)',
    'Numerical probes / A42 exclusion (dfs:2)',
    'Numerical probes / A42 exclusion (dfs:3)',
    'Numerical probes / A42 exclusion (dfs:4)',
    'Numerical probes / A42 exclusion (dfs:5)',
    'Numerical probes / A42 exclusion (n18:0)',
    'Numerical probes / A42 exclusion (n18:1)',
    'Numerical probes / A42 exclusion (n18:2)',
    'Numerical probes / A42 exclusion (paths)',
    'Numerical probes / A42 exclusion (r5)',
    'Numerical probes / A42 exclusion (sathr)',
    'Numerical probes / A42 witness',
    'Numerical probes / A45 ancilla',
    'Numerical probes / ARP-1-MARC exact span check',
    'Numerical probes / BG-2 premise orientation',
    'Numerical probes / KINF-2 foundations',
    'Numerical probes / KT4-PREM-1 premise audit',
    'Numerical probes / KTOKEN-MAXCONE-1 k = 3 exact layer',
    'Numerical probes / KTRANS-SEP-2 Omega4 counterexample',
    'Numerical probes / NB-1 native-gate ball',
    'Numerical probes / OI channel protocol',
    'Numerical probes / OI finite protocol',
    'Numerical probes / OI pair maxCone',
    'Numerical probes / PRESERVE-INDUCT-1 preservation induction',
    'Numerical probes / core A',
    'Numerical probes / core B',
    'Numerical probes / foundations',
)
TRIAL_WORKFLOW_NAME, VERIFY_WORKFLOW_NAME = 'A1-EXIT trial verify', 'verify'


def identity_findings(trial_sha, run_id):
    """R7 (§31.12.15): the designated trial commit and run id, required and well formed."""
    bad = []
    if not isinstance(trial_sha, str) or not re.fullmatch(r'[0-9a-f]{40}', trial_sha):
        bad.append('no designated trial commit: --trial-sha %r missing or not a full commit id' % (trial_sha,))
    if not isinstance(run_id, str) or not re.fullmatch(r'[1-9][0-9]*', run_id):
        bad.append('no designated run: --run-id %r missing or not a positive decimal id' % (run_id,))
    return bad


def job_binding(js, run_id, head_sha, workflow_name):
    """R7: every job belongs to run run_id, at head_sha, first attempt, of the named workflow."""
    bad = []
    for j in js:
        n = j.get('name')
        if type(j.get('run_id')) is not int or str(j.get('run_id')) != str(run_id):
            bad.append('job %r: run_id %r is not the designated run %s' % (n, j.get('run_id'), run_id))
        if j.get('head_sha') != head_sha:
            bad.append('job %r: head_sha %r is not %s' % (n, j.get('head_sha'), head_sha))
        if type(j.get('run_attempt')) is not int or j.get('run_attempt') != 1:
            bad.append('job %r: run_attempt %r, not 1' % (n, j.get('run_attempt')))
        if j.get('workflow_name') != workflow_name:
            bad.append('job %r: workflow_name %r, not %r' % (n, j.get('workflow_name'), workflow_name))
    return bad


def pdf_finding_kind(x, pdfs):
    """B1 (§31.12.13): 'pages' or 'text' for a content finding of a ledgered PDF; None for any other finding."""
    m = re.fullmatch(r'(\S+): \d+ pages committed, \d+ built', x)
    if m and m.group(1) in pdfs:
        return 'pages'
    m = re.fullmatch(r'(\S+): extracted text differs from the CI-built PDF', x)
    if m and m.group(1) in pdfs:
        return 'text'
    return None


def _jobs(rec):
    """Jobs of a complete host jobs record (§31.12.14, R6): GET .../runs/{id}/jobs?per_page=100 saved whole, every page
    concatenated when total_count exceeds 100. The record must be a JSON object whose integer total_count equals the
    number of its jobs; each job carries a unique integer id and a non-empty steps list. Otherwise (a partial page, a
    bare list, a job without steps or listed twice) None."""
    if not isinstance(rec, dict):
        return None
    j, n = rec.get('jobs'), rec.get('total_count')
    if type(n) is not int or not isinstance(j, list) or len(j) != n or not all(isinstance(x, dict) for x in j):
        return None
    ids = [x.get('id') for x in j]
    if not all(type(i) is int for i in ids) or len(set(ids)) != len(ids):
        return None
    if not all(isinstance(x.get('steps'), list) and x['steps'] and all(isinstance(s, dict) for s in x['steps']) for x in j):
        return None
    return j


def _jobs_why(rec):
    if not isinstance(rec, dict):
        return 'not a JSON object with total_count and jobs'
    j, n = rec.get('jobs'), rec.get('total_count')
    if type(n) is not int:
        return 'total_count %r missing or not an integer' % (n,)
    if not isinstance(j, list) or len(j) != n:
        return 'incomplete: %s jobs for total_count %d' % (len(j) if isinstance(j, list) else None, n)
    ids = [x.get('id') if isinstance(x, dict) else None for x in j]
    if not all(type(i) is int for i in ids) or len(set(ids)) != len(ids):
        return 'job ids missing, not integers or not unique'
    return 'a job without steps'


def expect_trial(kind, res, reports, pdfs, jobs=None, built=None, trial_sha=None, run_id=None, run_check=None):
    """PREREG §31.12.13–§31.12.16: the run's structured outputs against the T0′ or T1′ expectation, bound to the
    designated trial commit and run (R7). run_check is verify_run's findings on the same result.json and the host run
    object (§31.12.16): None when it was not run, which is itself a deviation. Returns the deviations."""
    bad = identity_findings(trial_sha, run_id)
    if run_check is None:
        bad.append('the run record is not verified: --expect-trial needs --run-meta, and --verify-run on the same result.json')
    else:
        bad += ['verify-run: %s' % x for x in run_check]
    t0 = kind == 'T0'
    if not isinstance(res, dict):
        return bad + ['result.json missing or not a JSON object']
    if res.get('trial_sha') != trial_sha:
        bad.append('result.json trial_sha %r is not the designated trial commit %r' % (res.get('trial_sha'), trial_sha))
    if res.get('run_id') != run_id:
        bad.append('result.json run_id %r is not the designated run %r' % (res.get('run_id'), run_id))
    wsha = res.get('workflow_sha')
    if not isinstance(wsha, str) or not re.fullmatch(r'[0-9a-f]{40}', wsha):
        bad.append('result.json workflow_sha %r missing or not a full commit id' % (wsha,))
        wsha = None
    steps = res.get('steps') if isinstance(res.get('steps'), dict) else {}
    for s in sorted(set(TRIAL_STEPS) | set(steps)):
        want = {'preserve': 'failure', 'guards': 'skipped'}.get(s, 'success') if t0 else 'success'
        got = steps.get(s, {}).get('outcome') if isinstance(steps.get(s), dict) else None
        if got != want:
            bad.append('step %s: %s, expected %s%s' % (s, got, want, ' (an unexpected skip)' if got == 'skipped' else ''))
    if set(res.get('pdf_pages') or {}) != set(pdfs):
        bad.append('result.json pdf_pages lists %s, not the ledgered PDFs %s' % (sorted(res.get('pdf_pages') or {}), sorted(pdfs)))
    if res.get('tex_files_differing') != []:
        bad.append('result.json tex_files_differing %r, not []' % (res.get('tex_files_differing'),))
    names = ['verify-pins', 'verify-ledger', 'commit', 'tree'] + ([] if t0 else ['guards'])
    for n in names:
        r = reports.get(n)
        if not isinstance(r, dict) or r.get('schema') != 'a1exit-checker-result-v1' or not isinstance(r.get('checks'), list):
            bad.append('report %s missing or not in the a1exit-checker-result-v1 schema' % n)
            continue
        seen = False
        for c in r['checks']:
            if n == 'tree' and c.get('name') == PDF_CHECK:
                seen = True
                ds = c.get('discrepancies') or []
                if t0:
                    if c.get('status') != 'fail' or not ds:
                        bad.append('tree report: the PDF comparison %s, expected to fail with content findings' % c.get('status'))
                    for x in ds:
                        if pdf_finding_kind(x, pdfs) is None:
                            bad.append('tree report: PDF comparison finding not of an allowed kind: %s' % x)
                elif c.get('status') != 'pass' or ds:
                    bad.append('tree report: the PDF comparison %s with %d findings, expected to pass' % (c.get('status'), len(ds)))
            elif c.get('status') != 'pass':
                bad.append('report %s: check %r %s: %s' % (n, c.get('name'), c.get('status'), (c.get('discrepancies') or [''])[0]))
        if n == 'tree' and not seen:
            bad.append('tree report: no PDF comparison check')
        if n != 'tree' and r.get('verdict') != 'pass':
            bad.append('report %s verdict %r, not pass' % (n, r.get('verdict')))
    if jobs is None:
        bad.append('host jobs record not supplied (--jobs): the host step conclusions are unchecked')
    else:
        js = _jobs(jobs)
        if js is None:
            bad.append('host jobs record rejected: %s' % _jobs_why(jobs))
        elif len(js) != 1:
            bad.append('host jobs record: not exactly one job')
        else:
            bad += job_binding(js, run_id, wsha, TRIAL_WORKFLOW_NAME)
            if js[0].get('name') != 'verify':
                bad.append('host job name %r, not verify' % js[0].get('name'))
            seen = set()
            for s in js[0].get('steps') or []:
                want = T0_HOST.get(s.get('name'), 'success') if t0 else 'success'
                seen.add(s.get('name'))
                if s.get('conclusion') != want:
                    bad.append('host step %r: %s, expected %s%s' % (s.get('name'), s.get('conclusion'), want,
                                                                     ' (an unexpected skip)' if s.get('conclusion') == 'skipped' else ''))
            for n in ['Write result.json', 'Upload result.json, logs and the built PDFs'] + (sorted(T0_HOST) if t0 else []):
                if n not in seen:
                    bad.append('host step %r missing from the jobs record' % n)
            want = 'failure' if t0 else 'success'
            if js[0].get('conclusion') != want:
                bad.append('host job conclusion %s, expected %s' % (js[0].get('conclusion'), want))
    if built is None:
        bad.append('artifact not supplied (--built): the uploaded PDFs are unchecked')
    else:
        for p in sorted(pdfs):
            f = os.path.join(built, p)
            if not os.path.isfile(f):
                bad.append('%s: not in the uploaded artifact' % p)
            elif not open(f, 'rb').read(4) == b'%PDF':
                bad.append('%s: in the uploaded artifact, but empty or not a PDF' % p)
            else:  # N11 (§31.12.15): it parses, and has the page count result.json records
                try:
                    n = _page_count(f)
                except PdfinfoUnavailable as e:
                    bad.append('%s: pdfinfo could not be run (%s), so the uploaded PDF is unchecked' % (p, e))
                    continue
                except (subprocess.CalledProcessError, AttributeError, ValueError):
                    bad.append('%s: in the uploaded artifact, but pdfinfo cannot read it' % p)
                    continue
                if n != (res.get('pdf_pages') or {}).get(p):
                    bad.append('%s: the uploaded PDF has %d pages, result.json records %r' % (p, n, (res.get('pdf_pages') or {}).get(p)))
    return bad


def expect_verify(jobs, trial_sha=None, run_id=None):
    """PREREG §31.12.13–§31.12.15: T1′'s verify.yml run, workflow_dispatch: every job belongs to the designated run
    at the trial commit (R7) and is one of the 41 pinned jobs; every job and step succeeds, except the skips listed in
    VERIFY_SKIPS, each of which must conclude as listed."""
    bad = identity_findings(trial_sha, run_id)
    js = _jobs(jobs)
    if js is None:
        return bad + ['host jobs record rejected: %s' % _jobs_why(jobs)]
    bad += job_binding(js, run_id, trial_sha, VERIFY_WORKFLOW_NAME)
    names = [j.get('name') for j in js]
    if sorted(names) != sorted(VERIFY_JOBS):
        bad.append('the jobs are not the %d pinned jobs of verify.yml: missing %s, unexpected %s'
                   % (len(VERIFY_JOBS), sorted(set(VERIFY_JOBS) - set(names)), sorted(set(names) - set(VERIFY_JOBS))))
    seen = set()
    for j in js:
        if j.get('conclusion') != 'success':
            bad.append('job %r: %s, expected success' % (j.get('name'), j.get('conclusion')))
        for s in j.get('steps') or []:
            key = (j.get('name'), s.get('name'))
            want = VERIFY_SKIPS.get(key, 'success')
            seen.add(key)
            if s.get('conclusion') != want:
                bad.append('job %r step %r: %s, expected %s%s' % (key[0], key[1], s.get('conclusion'), want,
                                                                  ' (an unexpected skip)' if s.get('conclusion') == 'skipped' else ''))
    for key in sorted(set(VERIFY_SKIPS) - seen):
        bad.append('job %r step %r missing from the jobs record' % key)
    return bad


def read_reports(out):
    names = {'verify-pins': 'preserve_check-verify-pins.json', 'verify-ledger': 'preserve_check-verify-ledger.json',
             'commit': 'preserve_check-commit.json', 'tree': 'preserve_check-tree.json', 'guards': 'guards_check-mutants.json'}
    reps = {}
    for k, f in names.items():
        try:
            reps[k] = json.load(open(os.path.join(out, f), encoding='utf-8'))
        except (OSError, ValueError):
            reps[k] = None
    try:
        res = json.load(open(os.path.join(out, 'result.json'), encoding='utf-8'))
    except (OSError, ValueError):
        res = None
    return res, reps


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
    expect(not scope_check(good), 'scope assertions: the predicted candidate carries every corrected sentence')
    n_base = len(scope_check(base_files))
    want_base = sum(1 for f, s in SCOPE_PRESENT if s.encode('utf-8') not in base_files.get(f, b'')) + \
        sum(1 for f, s in SCOPE_ABSENT if s.encode('utf-8') in base_files.get(f, b''))
    # the two #1494 statements hold at the base; one absent form (D276's earlier replacement, "`A1` on a finite torus
    # and") is plan text, never at the base
    # likewise D319's earlier lower-case replacement ("**the finiteness predicate `A1` is")
    expect(n_base == want_base == len(SCOPE_PRESENT) - 2 + len(SCOPE_ABSENT) - 2,
           'scope assertions: the unedited base fails every one the plan adds (%d findings)' % n_base)
    c = dict(good); c['papers/SM.md'] = c['papers/SM.md'].replace('the counting measure on a finite $\\mathcal{C}_H$'.encode(), b'the counting measure', 1)
    expect(any('lacks' in x for x in scope_check(c)), 'scope assertions: a candidate without D391 fails')
    r0 = reconcile(led, led, base_files, base_files)
    expect(not r0[2] and all(k == 'unchanged' for _, _, k, _ in r0[0]),
           'reconcile: a ledger against itself has every splice unchanged and no drift')
    t2 = json.loads(json.dumps(led)); g = [x for x in t2['splices'] if x['id'] not in REVISED31][0]; g['new'] += ' '
    expect(any(g['id'] in x for x in reconcile(t2, led, base_files, base_files)[2]), 'reconcile: a changed replacement is drift')
    b2 = dict(base_files); b2['papers/GR.md'] = b'xx' + base_files['papers/GR.md']
    t3 = json.loads(json.dumps(led))
    for x in t3['splices']:
        if x['file'] == 'papers/GR.md':
            x['start'] += 2; x['end'] += 2
    r3 = reconcile(led, t3, base_files, b2)
    expect(not r3[2] and any(s == 2 for _, f, _, s in r3[0] if f == 'papers/GR.md'),
           'reconcile: splices after a base insertion, shifted by its length, are explained')
    [x for x in t3['splices'] if x['file'] == 'papers/GR.md'][0]['start'] += 1
    expect(bool(reconcile(led, t3, base_files, b2)[2]), 'reconcile: a span moved by anything else is drift')
    c = dict(good); c[BOOK + '.md'] = c[BOOK + '.md'] + 'A single hidden permutation used identically\n'.encode()
    expect(any('still carries' in x for x in scope_check(c)), 'scope assertions: a superseded form in FULL fails')
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
        root = tempfile.mkdtemp(prefix='a1exit-pdf-')
        try:
            d1, d2, out = (os.path.join(root, x) for x in ('cand', 'build', 'out'))
            for d in (d1, d2):
                os.makedirs(os.path.join(d, 'papers'))
            os.makedirs(out)
            gr, cx = base_files['papers/GR.pdf'], base_files['papers/Complexity.pdf']
            open(os.path.join(d1, 'papers/GR.pdf'), 'wb').write(gr)
            open(os.path.join(d1, 'papers/Complexity.pdf'), 'wb').write(cx)

            def rebuilt(name, data):  # the same document with other bytes, as a rebuild's creation date makes it
                open(os.path.join(d2, name), 'wb').write(data + b'\n%% rebuilt\n')
            rebuilt('papers/GR.pdf', gr)
            rebuilt('papers/Complexity.pdf', cx)

            def state(rc='0', rows=('papers/GR.pdf', 'papers/Complexity.pdf'), tsv=True, shift=0):
                rcp, tp = os.path.join(out, 'build.rc'), os.path.join(out, 'pdf-pages.tsv')
                for f in (rcp, tp):
                    if os.path.exists(f):
                        os.remove(f)
                if rc is not None:
                    open(rcp, 'w').write(rc + '\n')
                if tsv:
                    open(tp, 'w').write(''.join('%s\t%d\n' % (r, (pdf_facts(os.path.join(d2, r))[0] if os.path.isfile(os.path.join(d2, r)) else 0) + shift)
                                                for r in rows))
            both = ['papers/Complexity.pdf', 'papers/GR.pdf']
            state()
            expect(not pdf_compare(d1, d2, both), 'pdf compare: rebuilt, recorded, build succeeded, equal in pages and text: passes')

            def mutant(name, want, **kw):
                state(**kw)
                b = pdf_compare(d1, d2, both)
                expect(any(want in x for x in b), 'pdf compare %s: fails with "%s"' % (name, want))
            mutant('MT-pdf-build-failed (build.rc 1)', 'the CI build did not succeed', rc='1')
            mutant('MT-pdf-build-rc-missing', 'the CI build did not succeed', rc=None)
            mutant('MT-pdf-pages-missing (no pdf-pages.tsv)', 'no build record', tsv=False)
            mutant('MT-pdf-not-built (Complexity absent from the build record)',
                   'papers/Complexity.pdf: not rebuilt by the CI build', rows=('papers/GR.pdf',))
            mutant('MT-pdf-pages-mismatch (record and built file disagree)', 'pdf-pages.tsv records', shift=1)
            state()
            expect(any('no ledgered PDF to compare' in x for x in pdf_compare(d1, d2, [])),
                   'pdf compare MT-pdf-empty-set (no ledgered PDF): fails with "no ledgered PDF to compare"')
            state()
            open(os.path.join(out, 'pdf-pages.tsv'), 'a').write('papers/GR.pdf 12\n')
            expect(any('malformed build record row' in x for x in pdf_compare(d1, d2, both)),
                   'pdf compare MT-pdf-malformed-row: fails with "malformed build record row"')
            state()
            open(os.path.join(out, 'pdf-pages.tsv'), 'a').write('papers/GR.pdf\t%d\n' % pdf_facts(os.path.join(d2, 'papers/GR.pdf'))[0])
            expect(any('duplicate build record row' in x for x in pdf_compare(d1, d2, both)),
                   'pdf compare MT-pdf-duplicate-row: fails with "duplicate build record row"')
            open(os.path.join(d2, 'papers/Complexity.pdf'), 'wb').write(cx)
            mutant('MT-pdf-stale (the built PDF is the committed copy)', 'papers/Complexity.pdf: stale')
            rebuilt('papers/Complexity.pdf', cx)
            rebuilt('papers/GR.pdf', base_files['papers/Main.pdf'])
            mutant('MT-pdf-other-document (a committed PDF that is not the built one)', 'papers/GR.pdf: extracted text differs')
            os.remove(os.path.join(d2, 'papers/GR.pdf'))
            mutant('MT-pdf-absent (a PDF the CI build did not make)', 'papers/GR.pdf: missing in the candidate or in the CI build')
        finally:
            shutil.rmtree(root, ignore_errors=True)
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
    # controls from existing commits only (nothing is written to the object store): 556cfb08, #1543's commit, is a
    # single-parent child of the ledger base; 98e55009 (#1494's head) has another single parent; W is a merge
    child, other = '556cfb081ce698763578682e73731d80dd7aa616', '98e55009428fb32c87a1f2f8ea6fcaf2427a7ae2'
    if all(_git_ok('cat-file', '-e', x + '^{commit}') for x in (WORKFLOW_BASE, child, other)) and led['base'].startswith('53c6601a'):
        lb = led['base']
        # N8: a plan commit of this record directory and an earlier one with the same ledger base H
        PL, PL_OTHER = 'fef0f1589d66ae6e120b14e73b0ebb70b316e4c7', '9ba8ef10e54d3618685e27d29d31291588ff9a6f'
        ok_run = {'workflow_sha': WORKFLOW_BASE, 'ref_sha': WORKFLOW_BASE, 'trial_sha': child, 'run_id': '1', 'plan_sha': PL}
        ok_meta = {'id': 1, 'event': 'workflow_dispatch', 'path': WORKFLOW, 'head_branch': 'main', 'run_attempt': 1,
                   'head_sha': WORKFLOW_BASE}
        expect(not verify_run(ok_run, ok_meta, lb, WORKFLOW_BASE, WORKFLOW_BASE, PL),
               'verify-run: a host record of a dispatch at the workflow base, and a child of the ledger base: valid')
        for name, ch, mch, want in (
                ('the run metadata missing', {}, None, 'run metadata missing'),
                ('result.json workflow_sha differs from the run\'s head_sha', {'workflow_sha': lb}, {}, 'differs from the run\'s head_sha'),
                ('result.json ref_sha differs from the run\'s head_sha', {'ref_sha': lb}, {}, 'differs from the run\'s head_sha'),
                ('a run head_sha without the workflow base', {'workflow_sha': lb, 'ref_sha': lb}, {'head_sha': lb}, 'does not contain the workflow base'),
                ('a run head_sha whose workflow blob is not the workflow base\'s (the ledger base\'s eight-PDF workflow)',
                 {'workflow_sha': lb, 'ref_sha': lb}, {'head_sha': lb}, 'differs from its blob at the workflow base'),
                ('a run head_sha off the first-parent history of main', {'workflow_sha': child, 'ref_sha': child}, {'head_sha': child},
                 'not on the first-parent history of main'),
                ('a run of another event', {}, {'event': 'push'}, 'not workflow_dispatch'),
                ('a run of another workflow', {}, {'path': '.github/workflows/verify.yml'}, 'run workflow path'),
                ('a run record of another run', {}, {'id': 2}, 'is not result.json run_id'),
                ('a re-run attempt', {}, {'run_attempt': 2}, 'not 1'),
                ('a run from another branch', {}, {'head_branch': 'trial/x'}, 'not main'),
                ('trial_sha whose single parent is not the ledger base', {'trial_sha': other}, {}, 'not exactly the ledger base'),
                ('a merge trial_sha', {'trial_sha': WORKFLOW_BASE}, {}, 'not exactly the ledger base'),
                ('a trial_sha that is not a commit', {'trial_sha': '0' * 40}, {}, 'not a known commit'),
                ('R5: a run record without head_sha', {}, {'head_sha': None, '_drop': 'head_sha'}, 'head_sha None missing'),
                ('R5: a run record with head_sha null', {}, {'head_sha': None}, 'head_sha None missing'),
                ('R5: no head_sha and result.json self-reporting the ledger base', {'workflow_sha': lb, 'ref_sha': lb},
                 {'head_sha': None, '_drop': 'head_sha'}, 'self-reported, not the executed commit'),
                ('a head_sha that is not a hex id', {}, {'head_sha': 'W'}, "head_sha 'W' missing"),
                ('R5: an empty head_sha', {}, {'head_sha': ''}, "head_sha '' missing"),
                ('R5: an upper-case head_sha', {}, {'head_sha': WORKFLOW_BASE.upper()}, 'missing or not a full commit id'),
                ('a run id missing on both sides', {'run_id': None}, {'id': None}, 'both must be present and equal'),
                ('result.json missing workflow_sha', {'workflow_sha': None}, {}, 'self-reported, not the executed commit'),
                ('a trial_sha given as a ref name, not a full id', {'trial_sha': 'HEAD'}, {}, 'not a known commit'),
                ('N8: plan_sha missing', {'plan_sha': None}, {}, 'plan_sha None missing'),
                ('N8: plan_sha upper case', {'plan_sha': PL.upper()}, {}, 'missing or not a full commit id'),
                ('N8: plan_sha a short id', {'plan_sha': PL[:12]}, {}, 'missing or not a full commit id'),
                ('N8: plan_sha differing from the designated plan', {'plan_sha': PL_OTHER}, {}, 'is not the designated plan'),
                ('N8: host inputs carrying another plan', {}, {'inputs': {'plan_sha': PL_OTHER, 'trial_sha': child}},
                 'do not carry the designated plan'),
                ('N8: host inputs malformed', {}, {'inputs': 'x'}, 'do not carry the designated plan'),
                ('N9: run_attempt True', {}, {'run_attempt': True}, 'not 1'),
                ('N9: run_attempt 1.0', {}, {'run_attempt': 1.0}, 'not 1'),
                ('N9: run_attempt "1"', {}, {'run_attempt': '1'}, 'not 1')):
            m = None if mch is None else dict(ok_meta, **{k: v for k, v in mch.items() if k != '_drop'})
            if mch and '_drop' in mch:
                m.pop(mch['_drop'], None)
            expect(any(want in x for x in verify_run(dict(ok_run, **ch), m, lb, WORKFLOW_BASE, WORKFLOW_BASE, PL)),
                   'verify-run void: %s ("%s")' % (name, want))
        expect(any('not a JSON object' in x for x in verify_run([], ok_meta, lb, WORKFLOW_BASE, WORKFLOW_BASE, PL)),
               'verify-run void: result.json not an object ("not a JSON object")')
        for name, pl in (('--plan missing', None), ('--plan malformed', 'fef0f158')):
            expect(any('no designated plan' in x for x in verify_run(ok_run, ok_meta, lb, WORKFLOW_BASE, WORKFLOW_BASE, pl)),
                   'verify-run void: N8: %s ("no designated plan")' % name)
        # the owner's test: an otherwise valid, consistent run of another plan commit with the same ledger base H
        other_base = json.loads(git('show', PL_OTHER + ':' + LEDGER)).get('base')
        other = dict(ok_run, plan_sha=PL_OTHER)
        both = verify_run(other, dict(ok_meta, inputs={'plan_sha': PL_OTHER}), lb, WORKFLOW_BASE, WORKFLOW_BASE, PL)
        expect(other_base == lb and not verify_run(other, dict(ok_meta, inputs={'plan_sha': PL_OTHER}), lb, WORKFLOW_BASE,
                                                   WORKFLOW_BASE, PL_OTHER) and any('is not the designated plan' in x for x in both),
               'verify-run void: N8, the owner\'s test: a consistent run of plan %s (same ledger base %s) against plan %s'
               % (PL_OTHER[:8], lb[:8], PL[:8]))
        # N5: the blob test alone. With workflow base H and main W, W contains H and is on main, so only the blob differs.
        iso = verify_run(ok_run, ok_meta, lb, lb, WORKFLOW_BASE, PL)
        expect(len(iso) == 1 and 'differs from its blob at the workflow base' in iso[0],
               'verify-run void, isolated: only the workflow blob differs (exactly one finding: %s)' % (iso[0][:60] if iso else '-'))
        # §31.12.13: the redacted host record
        orig = dict(ok_meta, head_commit={'id': child, 'author': {'name': 'a', 'email': 'author address'},
                                          'committer': {'name': 'c', 'email': 'committer address'}})
        red = redact_run(orig)
        expect(not _has_email(red) and not verify_redacted(orig, red, ok_run, lb, WORKFLOW_BASE, WORKFLOW_BASE, PL)
               and verify_run(ok_run, red, lb, WORKFLOW_BASE, WORKFLOW_BASE, PL) == verify_run(ok_run, orig, lb, WORKFLOW_BASE, WORKFLOW_BASE, PL) == [],
               'redacted host record: the e-mail fields removed, every field verify_run reads kept, the same verdict (valid)')
        for name, copy, want in (
                ('a copy that drops head_sha', {k: v for k, v in red.items() if k != 'head_sha'}, 'lacks head_sha'),
                ('a copy whose id is the string "1"', dict(red, id='1'), 'changes id'),
                ('a copy that keeps an e-mail field', dict(red, head_commit=orig['head_commit']), 'still carries an email field'),
                ('R6 audit: a copy that is not an object', None, 'not a JSON object')):
            expect(any(want in x for x in verify_redacted(orig, copy, ok_run, lb, WORKFLOW_BASE, WORKFLOW_BASE, PL)),
                   'redacted host record void: %s ("%s")' % (name, want))
        expect(any('not the host\'s original record' in x for x in verify_redacted(red, red, ok_run, lb, WORKFLOW_BASE, WORKFLOW_BASE, PL)),
               'redacted host record void: R6 audit: the copy given as the original ("not the host\'s original record")')
        expect(not verify_run(ok_run, dict(red, id='1'), lb, WORKFLOW_BASE, WORKFLOW_BASE, PL),
               'redacted host record: verify_run alone accepts the string id, so the type check is needed')
    else:
        expect(False, 'verify-run: the workflow base %s is required in the object store' % WORKFLOW_BASE[:12])
    # §31.12.13: the expected result of T0′/T1′ (B1 and the expected skips), on T0's and T1's real evidence at H
    ev = 'verification/audits/foundations/a1exit-trial-%s-20261121/'
    try:
        def load(t, n):
            return json.loads(git('show', '%s:%s' % (led['base'], (ev % t) + n)))
        rep = {}
        for t in ('t0', 't1'):
            out = 'artifact/out/'
            rep[t] = (load(t, out + 'result.json'),
                      {k: load(t, out + f) for k, f in (('verify-pins', 'preserve_check-verify-pins.json'),
                                                        ('verify-ledger', 'preserve_check-verify-ledger.json'),
                                                        ('commit', 'preserve_check-commit.json'), ('tree', 'preserve_check-tree.json'))})
        rep['t1'][1]['guards'] = load('t1', 'artifact/out/guards_check-mutants.json')
        ci = load('t1', 'ci-record.json')
    except (subprocess.CalledProcessError, ValueError, KeyError) as e:
        rep = None
        expect(False, 'expect-trial: T0 and T1 evidence at the ledger base %s is required (%s)' % (led['base'][:12], e))
    if rep:
        import copy as _copy, io as _io, zipfile as _zip
        p8 = set(rep['t0'][0]['pdf_pages'])
        # a jobs record as the host serves it with ?per_page=100 (§31.12.14). ci-record.json keeps each job's id, name,
        # conclusion and steps, and the run's run_id, head_sha and run_attempt once per run; the fixture copies those
        # run-level values and the workflow's name onto each job, as the host serves them (§31.12.15).
        def hostjobs(run, wname):
            js = _copy.deepcopy(run['jobs'])
            for j in js:
                j.update(run_id=run['run_id'], head_sha=run['head_sha'], run_attempt=run['run_attempt'], workflow_name=wname)
            return {'total_count': len(js), 'jobs': js}
        t1run = ci['runs'][0]
        t1jobs = hostjobs(t1run, TRIAL_WORKFLOW_NAME)
        # R8 (§31.12.16): T0's own host jobs record, the pinned fixture of the plan, unchanged
        try:
            t0jobs = json.loads(plan[REC + T0_JOBS])
        except (KeyError, ValueError):
            t0jobs = None
        expect(isinstance(t0jobs, dict), 'expect-trial: T0\'s real host jobs record %s is in the plan' % T0_JOBS)
        t0jobs = t0jobs if isinstance(t0jobs, dict) else {}
        ident = {t: (rep[t][0]['trial_sha'], rep[t][0]['run_id']) for t in ('t0', 't1')}
        # the built PDFs: each run's own artifact.zip at H (N11 compares their page counts with pdf_pages)
        bdirs = {}
        for t in ('t0', 't1'):
            bdirs[t] = tempfile.mkdtemp(prefix='a1exit-built-')
            z = _zip.ZipFile(_io.BytesIO(git('show', '%s:%s' % (led['base'], (ev % t) + 'artifact.zip'))))
            for m in z.namelist():
                if m.endswith('.pdf') and 'build/' in m:
                    f = os.path.join(bdirs[t], m.split('build/', 1)[1])
                    os.makedirs(os.path.dirname(f), exist_ok=True)
                    open(f, 'wb').write(z.read(m))
        tree_pdf = [c for c in rep['t0'][1]['tree']['checks'] if c['name'] == PDF_CHECK]
        expect(len(tree_pdf) == 1 and any(pdf_finding_kind(x, p8) == 'pages' for x in tree_pdf[0]['discrepancies'])
               and not expect_trial('T0', rep['t0'][0], rep['t0'][1], p8, t0jobs, bdirs['t0'], *ident['t0'], run_check=[]),
               'expect-trial: (a) T0\'s real evidence, its real host jobs record unchanged and its built PDFs, the matching '
               'run, with the Structure page-count finding and the setup-python post step skipped, is expected under the '
               'T0 rule (B1, R8)')
        expect(not expect_trial('T1', rep['t1'][0], rep['t1'][1], p8, t1jobs, bdirs['t1'], *ident['t1'], run_check=[]),
               'expect-trial: (a) T1\'s real evidence and built PDFs, the matching run, is expected under the T1 rule')

        def t0mut(name, change, want, kind='T0', src='t0', jobs=None, built=True, idn=None, run_check=()):
            res, reps = _copy.deepcopy(rep[src])
            jb = _copy.deepcopy(jobs if jobs not in (None, 'none') else (t0jobs if kind == 'T0' else t1jobs))
            change(res, reps, jb)
            b = expect_trial(kind, res, reps, p8, None if jobs == 'none' else jb, bdirs[src] if built else None,
                             *(idn if idn is not None else ident[src]), run_check=list(run_check) if run_check is not None else None)
            expect(any(want in x for x in b), 'expect-trial deviation: %s ("%s")' % (name, want))

        def pdfc(reps):
            return [c for c in reps['tree']['checks'] if c['name'] == PDF_CHECK][0]
        t0mut('B1: a fail-closed finding (stale) in the PDF comparison',
              lambda r, p, j: pdfc(p)['discrepancies'].append('papers/GR.pdf: stale: the built PDF is byte-identical to the committed one, so it was not rebuilt'),
              'not of an allowed kind')
        t0mut('B1: a content finding for a PDF outside the ledgered set',
              lambda r, p, j: pdfc(p)['discrepancies'].append('papers/Other.pdf: extracted text differs from the CI-built PDF'),
              'not of an allowed kind')
        t0mut('B1: a finding in another check of the tree report',
              lambda r, p, j: p['tree']['checks'][2].update(status='fail', discrepancies=['papers/Main.md: unauthorized change']),
              'report tree: check')
        t0mut('B1: a failing --commit report',
              lambda r, p, j: (p['commit']['checks'][0].update(status='fail', discrepancies=['x']), p['commit'].update(verdict='fail')),
              'report commit')
        t0mut('B1: the PDF comparison check missing',
              lambda r, p, j: p['tree'].update(checks=[c for c in p['tree']['checks'] if c['name'] != PDF_CHECK]),
              'no PDF comparison check')
        t0mut('B1: the PDF comparison passing at T0',
              lambda r, p, j: pdfc(p).update(status='pass', discrepancies=[]), 'expected to fail with content findings')
        t0mut('B1: T1 with a text finding in its PDF comparison',
              lambda r, p, j: pdfc(p).update(status='fail', discrepancies=['papers/GR.pdf: extracted text differs from the CI-built PDF']),
              'expected to pass', kind='T1', src='t1')
        t0mut('skips: build skipped', lambda r, p, j: r['steps']['build'].update(outcome='skipped'), 'an unexpected skip')
        t0mut('skips: guards failing instead of skipped', lambda r, p, j: r['steps']['guards'].update(outcome='failure'),
              'step guards: failure, expected skipped')
        t0mut('skips: the upload step not succeeding',
              lambda r, p, j: [s.update(conclusion='skipped') for s in j['jobs'][0]['steps'] if s['name'].startswith('Upload')],
              'an unexpected skip')
        # R8 (§31.12.16): a wrong step conclusion on T0's real record, and the run check not run or void
        t0mut('R8: the setup-python post step succeeding at T0',
              lambda r, p, j: [s.update(conclusion='success') for s in j['jobs'][0]['steps'] if s['name'].startswith('Post Run actions/setup-python')],
              'expected skipped')
        t0mut('R8: --expect-trial with the run check not run', lambda r, p, j: None, 'the run record is not verified', run_check=None)
        t0mut('R8: --expect-trial with a void run check', lambda r, p, j: None, 'verify-run: run head_sha',
              run_check=['run head_sha 0000 does not contain the workflow base'])
        # R6 (§31.12.14): a missing host record or artifact
        t0mut('R6: --expect-trial without --jobs', lambda r, p, j: None, 'host jobs record not supplied', jobs='none')
        t0mut('R6: --expect-trial without --built', lambda r, p, j: None, 'artifact not supplied', built=False)
        t0mut('R6: the trial jobs record without total_count', lambda r, p, j: j.pop('total_count'), 'total_count None missing')
        # R7 (§31.12.15), for T1 under --expect-trial: (b) another run, same commit; (c) another commit; (d) missing or
        # malformed evidence
        T1, R1 = ident['t1']
        for name, change, want, idn in (
                ('R7 (b): --run-id another run', lambda r, p, j: None, 'is not the designated run', (T1, '44939798305')),
                ('R7 (b): the jobs\' run_id another run, same commit', lambda r, p, j: j['jobs'][0].update(run_id=44939798305),
                 'is not the designated run', None),
                ('R7 (c): the jobs\' head_sha another commit', lambda r, p, j: j['jobs'][0].update(head_sha='c06259692ddf12f7d3dffe170ec3118dc97682fc'),
                 'head_sha', None),
                ('R7 (c): --trial-sha another commit', lambda r, p, j: None, 'is not the designated trial commit',
                 ('5b6d48b58f45d3032bc33560aa5047c4b400f35a', R1)),
                ('R7 (d): no --run-id', lambda r, p, j: None, 'no designated run', (T1, None)),
                ('R7 (d): no --trial-sha', lambda r, p, j: None, 'no designated trial commit', (None, R1)),
                ('R7 (d): an upper-case --trial-sha', lambda r, p, j: None, 'no designated trial commit', (T1.upper(), R1)),
                ('R7 (d): a 12-character --trial-sha', lambda r, p, j: None, 'no designated trial commit', (T1[:12], R1)),
                ('R7 (d): a run id abc', lambda r, p, j: None, 'no designated run', (T1, 'abc')),
                ('R7 (d): a job without run_id', lambda r, p, j: j['jobs'][0].pop('run_id'), 'run_id None', None),
                ('R7 (d): result.json without workflow_sha', lambda r, p, j: r.pop('workflow_sha'), 'workflow_sha None missing', None),
                ('R7: a job of another workflow', lambda r, p, j: j['jobs'][0].update(workflow_name='verify'), 'workflow_name', None),
                ('R6: an empty built PDF', None, 'empty or not a PDF', None),
                ('N11: a four-byte %PDF built file', None, 'pdfinfo cannot read it', None),
                ('N11: a real PDF with another page count', None, 'the uploaded PDF has', None),
                ('N12: pdfinfo absent', 'nopath', 'pdfinfo could not be run', None)):
            if change == 'nopath':
                path = os.environ.get('PATH')
                os.environ['PATH'] = ''
                try:
                    t0mut(name, lambda r, p, j: None, want, kind='T1', src='t1')
                finally:
                    os.environ['PATH'] = path if path is not None else ''
            elif change is None:
                f = os.path.join(bdirs['t1'], 'papers/GR.pdf')
                keep = open(f, 'rb').read()
                open(f, 'wb').write(b'' if 'empty' in name else b'%PDF' if 'four-byte' in name
                                    else open(os.path.join(bdirs['t1'], 'papers/Main.pdf'), 'rb').read())
                try:
                    t0mut(name, lambda r, p, j: None, want, kind='T1', src='t1')
                finally:
                    open(f, 'wb').write(keep)
            else:
                t0mut(name, change, want, kind='T1', src='t1', idn=idn)
        for t in bdirs.values():
            shutil.rmtree(t, ignore_errors=True)
        vrun = ci['runs'][1]
        vjobs = hostjobs(vrun, VERIFY_WORKFLOW_NAME)
        VT, VR = vrun['head_sha'], str(vrun['run_id'])
        expect(not expect_verify(vjobs, VT, VR) and vjobs['total_count'] == 41 and sorted(VERIFY_JOBS) == sorted(j['name'] for j in vjobs['jobs']),
               'expect-verify: (a) T1\'s real verify.yml record (41 jobs, the pinned names), the matching run and commit, the '
               'KTRANS-SEP-2 marker skipped, is expected')
        other = '5b6d48b58f45d3032bc33560aa5047c4b400f35a'
        for name, change, want, idn in (
                ('the marker step succeeding', lambda j: [s.update(conclusion='success') for x in j['jobs'] for s in x['steps']
                                                          if s['name'].startswith('KTRANS-SEP-2 marker')], 'expected skipped', None),
                ('another step skipped', lambda j: j['jobs'][0]['steps'][1].update(conclusion='skipped'), 'an unexpected skip', None),
                ('a job skipped', lambda j: j['jobs'][2].update(conclusion='skipped'), 'expected success', None),
                ('R6: the default page, 30 of 41 jobs', lambda j: j.update(jobs=j['jobs'][:30]), 'incomplete: 30 jobs for total_count 41', None),
                ('R6: the record without total_count', lambda j: j.pop('total_count'), 'total_count None missing', None),
                ('R6: one job removed, total_count kept', lambda j: j['jobs'].pop(5), 'incomplete: 40 jobs for total_count 41', None),
                ('R6 audit: a job listed twice, total_count raised',
                 lambda j: (j['jobs'].append(_copy.deepcopy(j['jobs'][0])), j.update(total_count=42)), 'not unique', None),
                ('R6 audit: a job\'s steps removed', lambda j: j['jobs'][3].update(steps=[]), 'a job without steps', None),
                ('R7 (b): --run-id another run, same commit', lambda j: None, 'is not the designated run', (VT, '44951832698')),
                ('R7 (b): every job\'s run_id rewritten to another run',
                 lambda j: [x.update(run_id=44951832698) for x in j['jobs']], 'is not the designated run', None),
                ('R7 (b): one job\'s run_id changed (mixed runs)', lambda j: j['jobs'][7].update(run_id=44951832698),
                 'is not the designated run', None),
                ('R7 (c): every job\'s head_sha another commit', lambda j: [x.update(head_sha=other) for x in j['jobs']],
                 'head_sha', None),
                ('R7 (c): --trial-sha another commit', lambda j: None, 'head_sha', (other, VR)),
                ('R7 (d): no --run-id', lambda j: None, 'no designated run', (VT, None)),
                ('R7 (d): no --trial-sha', lambda j: None, 'no designated trial commit', (None, VR)),
                ('R7 (d): an upper-case --trial-sha', lambda j: None, 'no designated trial commit', (VT.upper(), VR)),
                ('R7 (d): a 12-character --trial-sha', lambda j: None, 'no designated trial commit', (VT[:12], VR)),
                ('R7 (d): a run id abc', lambda j: None, 'no designated run', (VT, 'abc')),
                ('R7 (d): a job without run_id', lambda j: j['jobs'][4].pop('run_id'), 'run_id None', None),
                ('R7 (d): a job without head_sha', lambda j: j['jobs'][4].pop('head_sha'), 'head_sha None', None),
                ('R7: run_attempt 2', lambda j: j['jobs'][1].update(run_attempt=2), 'run_attempt 2', None),
                ('R7: workflow_name another workflow\'s', lambda j: j['jobs'][1].update(workflow_name=TRIAL_WORKFLOW_NAME),
                 'workflow_name', None),
                ('R7: the first 30 jobs with total_count 30', lambda j: j.update(jobs=j['jobs'][:30], total_count=30),
                 'not the 41 pinned jobs', None),
                ('R7: a job renamed', lambda j: j['jobs'][9].update(name=j['jobs'][9]['name'] + ' (renamed)'),
                 'not the 41 pinned jobs', None)):
            vj = _copy.deepcopy(vjobs)
            change(vj)
            expect(any(want in x for x in expect_verify(vj, *(idn if idn is not None else (VT, VR)))),
                   'expect-verify deviation: %s ("%s")' % (name, want))
        expect(any('not a JSON object with total_count' in x for x in expect_verify(_copy.deepcopy(vjobs['jobs']), VT, VR)),
               'expect-verify deviation: R6: a bare list of jobs ("not a JSON object with total_count")')
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
    g.add_argument('--verify-run', metavar='RESULT_JSON', help='PREREG §31.12.7: the run record of a trial dispatch is '
                   'valid (workflow base on main, trial commit a single-parent child of the ledger base) or void')
    g.add_argument('--expect-trial', choices=('T0', 'T1'), help='PREREG §31.12.13: the run output directory --run-out '
                   'of a T0′ or T1′ dispatch of the trial workflow against its expected result')
    g.add_argument('--expect-verify', metavar='JOBS_JSON', help='PREREG §31.12.13: the host jobs record of T1′\'s '
                   'verify.yml dispatch against its expected step conclusions and skips')
    g.add_argument('--reconcile', metavar='REV', help='compare the ledger at REV (an earlier plan commit) with the current '
                   'ledger and base, splice by splice (PREREG §31.2)')
    ap.add_argument('--plan')
    ap.add_argument('--base')
    ap.add_argument('--mutants', action='store_true')
    ap.add_argument('--result-json', metavar='PATH', help='write the structured result here (also to RUNNER_TEMP/out/ when '
                    'that directory exists)')
    ap.add_argument('--workflow-base', default=WORKFLOW_BASE, help='with --verify-run (default the merge of #1543)')
    ap.add_argument('--main', default='origin/main', help='with --verify-run: the current main')
    ap.add_argument('--run-meta', metavar='RUN_JSON', help='with --verify-run: the host API record of the run '
                    '(GET .../actions/runs/{run_id}, saved whole); without it the run is void')
    ap.add_argument('--run-meta-redacted', metavar='RUN_JSON', help='with --verify-run: a retained redacted copy of '
                    '--run-meta; it must keep the fields and types verify_run reads and give the same findings')
    ap.add_argument('--run-out', metavar='DIR', help='with --expect-trial: the run\'s out/ directory (result.json and the '
                    'checker result files)')
    ap.add_argument('--trial-sha', metavar='SHA', help='with --expect-trial or --expect-verify: the designated trial commit')
    ap.add_argument('--run-id', metavar='N', help='with --expect-trial or --expect-verify: the id of the run judged')
    ap.add_argument('--jobs', metavar='JOBS_JSON', help='with --expect-trial: the host jobs record of the run, saved whole')
    ap.add_argument('--built', metavar='DIR', help='with --expect-trial: the artifact\'s built PDFs (their repository paths under DIR)')
    ap.add_argument('--pdf-out', metavar='DIR', help='with --pdf-compare: the run\'s output directory holding build.rc and '
                    'pdf-pages.tsv (default BUILT/../out)')
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
            else 'reconcile' if a.reconcile else 'expect-trial' if a.expect_trial else 'expect-verify' if a.expect_verify
            else 'verify-run' if a.verify_run else 'commit' if a.commit else 'tree')
    if a.verify_pins:
        pass
    elif a.verify_run:
        res = json.load(open(a.verify_run, encoding='utf-8'))
        meta = None
        if a.run_meta and os.path.isfile(a.run_meta):
            try:
                meta = json.load(open(a.run_meta, encoding='utf-8'))
            except ValueError:
                meta = None
        vb = verify_run(res, meta, led['base'], a.workflow_base, a.main, a.plan)
        print('verify-run: workflow base %s, ledger base %s, main %s' % (a.workflow_base[:12], led['base'][:12], a.main))
        for x in vb:
            print('  VOID ' + x)
        if a.run_meta_redacted:
            try:
                cb = open(a.run_meta_redacted, 'rb').read()
                copy = json.loads(cb)
            except (OSError, ValueError):
                cb, copy = b'', None
            rb = verify_redacted(meta, copy, res, led['base'], a.workflow_base, a.main, a.plan)
            print('redacted copy %s: sha256 %s; %d findings' % (a.run_meta_redacted, sha(cb), len(rb)))
            vb = vb + rb
            for x in rb:
                print('  VOID ' + x)
        print('RUN ' + ('VALID' if not vb else 'VOID'))
        record('trial run record: workflow base on main, trial a single-parent child of the ledger base', not vb, vb)
        ok = ok and not vb
    elif a.expect_trial or a.expect_verify:
        if a.expect_trial:
            res, reps = read_reports(a.run_out or '.')
            jobs = None
            if a.jobs:
                try:
                    jobs = json.load(open(a.jobs, encoding='utf-8'))
                except (OSError, ValueError):
                    jobs = 'unreadable'
            rc = None
            if a.run_meta:  # §31.12.16: --verify-run on the same result.json, with the same plan and bases
                try:
                    meta = json.load(open(a.run_meta, encoding='utf-8'))
                except (OSError, ValueError):
                    meta = None
                rc = verify_run(res, meta, led['base'], a.workflow_base, a.main, a.plan)
                if a.run_meta_redacted:
                    try:
                        copy = json.load(open(a.run_meta_redacted, encoding='utf-8'))
                    except (OSError, ValueError):
                        copy = None
                    rc = rc + verify_redacted(meta, copy, res, led['base'], a.workflow_base, a.main, a.plan)
            eb = expect_trial(a.expect_trial, res, reps, {t[:-4] + '.pdf' for t in TEX}, jobs, a.built, a.trial_sha, a.run_id, rc)
            label = 'expected result of %s′ (PREREG §31.12.13)' % a.expect_trial
        else:
            try:
                eb = expect_verify(json.load(open(a.expect_verify, encoding='utf-8')), a.trial_sha, a.run_id)
            except (OSError, ValueError):
                eb = identity_findings(a.trial_sha, a.run_id) + ['host jobs record missing or not JSON']
            label = 'expected result of T1′\'s verify.yml run (PREREG §31.12.13)'
        for x in eb:
            print('  DEVIATION ' + x)
        print('TRIAL ' + ('EXPECTED' if not eb else 'DEVIATION'))
        record(label, not eb, eb)
        ok = ok and not eb
    elif a.reconcile:
        old_led = json.loads(plan_files(a.reconcile)[LEDGER])
        rows, added, drift = reconcile(old_led, led, tree_of(old_led['base']), base)
        kinds = {}
        for i, f, k, s in rows:
            kinds[k.split(' at bytes')[0]] = kinds.get(k.split(' at bytes')[0], 0) + 1
        print('reconcile: ledger at %s (base %s, %d splices) against the current ledger (base %s, %d splices)'
              % (a.reconcile[:12], old_led['base'][:12], len(old_led['splices']), led['base'][:12], len(led['splices'])))
        for k, n in sorted(kinds.items()):
            print('  %-45s %d' % (k, n))
        for i, f, k, s in rows:
            if s:
                print('  SHIFT %s %s %+d (%s)' % (i, f, s, k))
        print('  added splices: %d (%s)' % (len(added), ' '.join(added)))
        print('  drift: %d' % len(drift))
        for x in drift:
            print('  DRIFT ' + x)
        record('reconcile against the ledger at %s: every changed splice explained, no drift' % a.reconcile, not drift, drift)
        ok = ok and not drift
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
            sc = scope_check(cand)
            print('scope assertions (PREREG §31.7 item 6): %d present, %d absent required; %d findings'
                  % (len(SCOPE_PRESENT), len(SCOPE_ABSENT), len(sc)))
            for x in sc:
                print('  FAIL ' + x)
            record('scope assertions of amendment §31 in the candidate', not sc, sc)
            ok = ok and not sc
            print('candidate: %d findings; PDFs of ledgered sources rebuilt (checked by the CI build): %d' % (len(fails), len(pdfs)))
            for x in fails:
                print('  FAIL ' + x)
            for x in pdfs:
                print('  PDF ' + x)
            record('candidate against base, ledger, regenerated artifacts and plan record', not fails, fails)
            ok = ok and not fails
            if a.pdf_compare and a.tree:
                pb = pdf_compare(a.tree, a.pdf_compare, {t[:-4] + '.pdf' for t in TEX}, a.pdf_out)
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
