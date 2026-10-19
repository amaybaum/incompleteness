"""Isolated real-vs-mutant experiments for the survivors and the crash family (scratch; never committed).
argv: <worktree> <scratch dir> <section...>. The worktree is only read; fixtures live under <scratch dir>. Each mutant is
the committed checker's source with exactly the edit mutants_all.py records, executed in memory with __file__ at the
real path (so it reads the same archive). Every verdict printed is the function's own output.
Sections: headless, farline, digitbound, pin, decimal, crash."""
import contextlib, hashlib, io, json, os, shutil, subprocess, sys, types

WT, SD = sys.argv[1:3]
SECTIONS = sys.argv[3:]
A = os.path.join(WT, 'verification/audits/evidence-retention')
HERE = os.path.dirname(os.path.abspath(__file__))
_src = open(os.path.join(HERE, 'mutants_all.py')).read().split('origin, fn, kind, reason, edits, want = M[which]')[0]
_ns = {}
exec(_src.replace('wt, which, outdir = sys.argv[1:4]', 'wt, which, outdir = %r, None, None' % WT), _ns)
MUT = _ns['M']


def module(fn, mutant=None, extra=()):
    p = os.path.join(A, fn)
    src = open(p, encoding='utf-8').read()
    for old, new in (MUT[mutant][4] if mutant else []) + list(extra):
        assert src.count(old) == 1, (mutant, old[:60])
        src = src.replace(old, new)
    m = types.ModuleType('m_%s_%s' % (fn[:8], mutant))
    m.__file__ = p
    exec(compile(src, p, 'exec'), m.__dict__)
    return m


def land(root, files):
    if os.path.isdir(root):
        shutil.rmtree(root)
    os.makedirs(root)
    for rel, body in files.items():
        p = os.path.join(root, rel)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        open(p, 'w', encoding='utf-8').write(body)


def hdr(t):
    print('\n' + '=' * 8 + ' ' + t)


OBJM = json.load(open(os.path.join(A, 'objects', 'manifest.json'), encoding='utf-8'))
BY = {e['oid']: e for e in OBJM['objects']}
OID = '1ab0fd9dd2c6701197f2e0ab18401cafb76a090d'
OTHER = '6959ced4c327ebb800cf6d463a049e4066e37288'
REC = 'verification/ZZ-ISOLATED/record.md'
RID = '70000000001'


def o10(m, root, run=RID):
    fails = []
    st = m.pending_citation(OID, {'pull_request': 1, 'round': 'ISO', 'record': REC, 'run': run}, root, fails.append)
    return (fails, st[0] if st else None)


def o7(m, root, cites, oid=OID):
    fails, texts = [], {}

    def lines_of(f):
        if f not in texts:
            p = os.path.join(root, f)
            texts[f] = open(p, encoding='utf-8').read().split('\n') if os.path.isfile(p) else None
        return texts[f]
    e = dict(BY[oid], cited=[dict({'location': '%s:%d' % (REC, n), 'tokens': t}, **({'run': r} if r else {}))
                             for n, t, r in cites])
    e.pop('awaiting_citation', None)
    m.o7_entry(oid, e, lines_of, root, fails.append)
    return (fails, 'cited' if not fails else None)


R13_EID, R13_RID, R13_HEAD = 'research-38450187534', '38450187534', 'e684897da41b1c3d066b880194c9beb87a19b7ad'


def r13(m, root, line=3, mapped=None, rid=R13_RID, head=R13_HEAD):
    m.R13_STATES.clear()
    fails = []
    aw = {'pull_request': 1, 'record': REC, 'round': 'ISO', 'line': line, 'head': head}
    e = {'awaiting_citation': aw} if mapped is None else {'citations': [{'path': REC, 'line': n} for n in mapped]}
    m.research_lifecycle(e, 'research-' + rid, rid, head, aw if mapped is None else None, True,
                         os.path.join(root, '__archive__'), root, fails.append)
    return (fails, m.R13_STATES.get('research-' + rid, (None,))[0])


def show(label, res):
    fails, st = res
    print('  %-58s verdict %-5s state %-8s failures %s' % (label, 'FAIL' if fails else 'PASS', st, fails))


root = os.path.join(SD, 'root')
# ---------------------------------------------------------------------------------------------------- headless
if 'headless' in SECTIONS:
    hdr('X-r13-headless-pending: unmutated vs mutated report() on a scratch archive whose research-38450187534 '
        'run.json has no head_sha (the record absent, so the entry is otherwise pending)')
    arch = os.path.join(SD, 'archive')
    if os.path.isdir(arch):
        shutil.rmtree(arch)
    shutil.copytree(A, arch, ignore=shutil.ignore_patterns('__pycache__', 'objects'))
    os.symlink(os.path.join(A, 'objects'), os.path.join(arch, 'objects'))   # unchanged; no copy
    rj = os.path.join(arch, 'ci', R13_RID, 'run.json')
    d = json.load(open(rj, encoding='utf-8'))
    d.pop('head_sha')
    data = json.dumps(d).encode()
    open(rj, 'wb').write(data)
    man = json.load(open(os.path.join(arch, 'manifest.json'), encoding='utf-8'))
    for e in man['entries']:
        for f in e.get('files', []):
            if f['path'] == 'ci/%s/run.json' % R13_RID:
                f['bytes'], f['sha256'] = len(data), hashlib.sha256(data).hexdigest()
    open(os.path.join(arch, 'manifest.json'), 'w', encoding='utf-8').write(json.dumps(man))
    # a root that shows the repository through symlinks, with the archive's path pointing at the scratch archive,
    # so the scratch archive is the archive of the tree under check (citing_lines skips it, as it skips the real one;
    # it does not descend the symlinked top-level directories, and no file outside the archive cites the runs at the
    # commit: the real plain check shows both entries pending with no R13 failure)
    hroot = os.path.join(SD, 'hroot')
    if os.path.isdir(hroot):
        shutil.rmtree(hroot)
    os.makedirs(hroot)
    src, dst = WT, hroot
    parts = 'verification/audits/evidence-retention'.split('/')
    for nm in os.listdir(src):
        os.symlink(os.path.join(src, nm), os.path.join(dst, nm))
    for part in parts[:-1]:
        src, dst = os.path.join(src, part), os.path.join(dst, part)
        os.unlink(dst)
        os.makedirs(dst)
        for nm in os.listdir(src):
            os.symlink(os.path.join(src, nm), os.path.join(dst, nm))
    os.unlink(os.path.join(dst, parts[-1]))
    os.symlink(arch, os.path.join(dst, parts[-1]))
    outs = {}
    for name in (None, 'X-r13-headless-pending'):
        m = module('check_retention.py', name)
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            rc = m.report(os.path.join(hroot, *parts), hroot)
        out = buf.getvalue().split('\n')
        outs[name] = (rc, [l for l in out if l.startswith('FAIL')], [l for l in out if 'citations (R13)' in l],
                      [l for l in out if l.startswith('RETENTION  ')])
        print('  %-26s exit %s' % (name or 'unmutated', rc))
        for l in outs[name][1] + outs[name][2] + outs[name][3]:
            print('      ' + l[:200])
    a, b = outs[None], outs['X-r13-headless-pending']
    print('  same exit: %s; same FAIL lines: %s; same verdict line: %s; summary lines differ: %s'
          % (a[0] == b[0], a[1] == b[1], a[3] == b[3], a[2] != b[2]))
    shutil.rmtree(arch)
    shutil.rmtree(hroot)
# ---------------------------------------------------------------------------------------------------- far line
if 'farline' in SECTIONS:
    hdr('X-r13-eligible-recorded-line-only: the d-far record, isolated (one entry) and with the self-test\'s sibling')
    real, mut = module('check_retention.py'), module('check_retention.py', 'X-r13-eligible-recorded-line-only')
    other = hashlib.sha1(b'another head ' + R13_HEAD.encode()).hexdigest()
    iso = '# isolated\nThe design compiled at `%s`, workflow run\n[%s](runs/%s).\n\nRun %s was dispatched on `%s…`.\n' % (
        R13_HEAD, R13_RID, R13_RID, R13_RID, other[:8])
    sib_rid, sib_head = '38454439833', 'febfe5e2668d3c000ec1d4ce7e4041f4feabd3c3'
    withsib = ('# with sibling\nThe design compiled at `%s`, workflow run\n[%s](runs/%s).\n\nThe design compiled at `%s`, '
               'workflow run\n[%s](runs/%s).\nRun %s was dispatched on `%s…`.\n' % (
                   R13_HEAD, R13_RID, R13_RID, sib_head, sib_rid, sib_rid, R13_RID, other[:8]))
    print('  isolated record:\n    ' + iso.replace('\n', '\n    '))
    land(root, {REC: iso})
    show('isolated, real: intended entry', r13(real, root))
    show('isolated, mutant: intended entry', r13(mut, root))
    land(root, {REC: withsib})
    show('with sibling, real: intended entry', r13(real, root))
    show('with sibling, mutant: intended entry', r13(mut, root))
    show('with sibling, real: sibling entry (line 6)', r13(real, root, line=6, rid=sib_rid, head=sib_head))
    show('with sibling, mutant: sibling entry (line 6)', r13(mut, root, line=6, rid=sib_rid, head=sib_head))
# ---------------------------------------------------------------------------------------------------- digit bound
if 'digitbound' in SECTIONS:
    hdr('X-run-digit-bounded: VALID vs INVALID (the run attached to a letter), isolated, real vs mutant')
    cr_, crm = module('check_retention.py'), module('check_retention.py', 'X-run-digit-bounded') \
        if MUT['X-run-digit-bounded'][1] == 'check_retention.py' else None
    co_, com = module('check_objects.py'), module('check_objects.py', 'X-run-digit-bounded')
    valid = '# valid\n- `%s`: the head of a design run.\n- The workflow was dispatched on exactly that head: run %s, `head_sha` `%s…`.\n' % (OID, RID, OID[:8])
    invalid = valid.replace('run %s,' % RID, 'run%s,' % RID)
    for nm, t in (('VALID', valid), ('INVALID', invalid)):
        print('  %s record:\n    %s' % (nm, t.replace('\n', '\n    ')))
    for nm, t in (('VALID', valid), ('INVALID', invalid)):
        land(root, {REC: t})
        show('O10 pending, %s, real' % nm, o10(co_, root))
        show('O10 pending, %s, mutant' % nm, o10(com, root))
        cites = [(2, [OID], None), (3, [OID[:8]], RID)]
        show('O7 promoted (lifecycle), %s, real' % nm, o7(co_, root, cites))
        show('O7 promoted (lifecycle), %s, mutant' % nm, o7(com, root, cites))
    # R13: the same two records for a research run (R13 never calls run_word; the mutant is in check_objects)
    rvalid = '# valid\nThe design compiled at `%s`, workflow run\n[%s](runs/%s).\n' % (R13_HEAD, R13_RID, R13_RID)
    rinvalid = '# invalid\nThe design compiled at `%s`, workflow run\nrun%s.\n' % (R13_HEAD, R13_RID)
    for nm, t in (('VALID', rvalid), ('INVALID', rinvalid)):
        print('  R13 %s record:\n    %s' % (nm, t.replace('\n', '\n    ')))
        land(root, {REC: t})
        # R13 loads check_objects' rules: the mutant is given to it as its objects_rules module
        cr_._OBJECTS_RULES = co_
        show('R13 pending, %s, real' % nm, r13(cr_, root))
        show('R13 cited (line 3 mapped), %s, real' % nm, r13(cr_, root, mapped=[3]))
        cr_._OBJECTS_RULES = com
        show('R13 pending, %s, mutant' % nm, r13(cr_, root))
        show('R13 cited (line 3 mapped), %s, mutant' % nm, r13(cr_, root, mapped=[3]))
        cr_._OBJECTS_RULES = None
    # the token-rule path O7 keeps for tranche 2's pinned (legacy) commits, which has no R13 counterpart
    leg = '0004afc9360117ba61523b72854de1aaf63705f0'
    lrun = next(c['run'] for c in BY[leg]['cited'] if c.get('run'))
    for nm, t in (('VALID', '# legacy\n- The run %s passed at that head.\n' % lrun),
                  ('INVALID', '# legacy\n- The run%s passed at that head.\n' % lrun)):
        land(root, {REC: t})
        print('  legacy token-rule %s line: %r' % (nm, t.split('\n')[1]))
        show('O7 legacy (tranche-2 pinned) %s, real' % nm, o7(co_, root, [(2, [lrun], lrun)], oid=leg))
        show('O7 legacy (tranche-2 pinned) %s, mutant' % nm, o7(com, root, [(2, [lrun], lrun)], oid=leg))
# ---------------------------------------------------------------------------------------------------- pin
PIN_PART = next((x.split(':')[1] for x in SECTIONS if x.startswith('pin:')), None)
if 'pin' in SECTIONS or PIN_PART:
    hdr('N-pin-digest-off: tamper controls on the code pin, real vs mutant (archive unchanged unless stated)')
    X = '0004afc9360117ba61523b72854de1aaf63705f0'      # a pinned tranche-2 commit the manifest labels 2
    W = OID                                             # a pinned tranche-4 commit (lifecycle)
    ABSENT = '0' * 40
    tampers = [('baseline (pin unchanged)', lambda s: s),
               ('SAME-COUNT swap: tranche-2 commit X -> tranche-4 commit W', lambda s: (s - {X}) | {W}),
               ('SAME-COUNT swap: X -> an id absent from the manifest', lambda s: (s - {X}) | {ABSENT}),
               ('COUNT add: W (tranche-4 commit) added', lambda s: s | {W}),
               ('COUNT add: an id absent from the manifest added', lambda s: s | {ABSENT}),
               ('COUNT remove: X removed', lambda s: s - {X})]
    sel = {None: tampers, 'a': tampers[:3], 'b': tampers[3:], 'c': []}[PIN_PART]
    for name in (None, 'N-pin-digest-off'):
        m = module('check_objects.py', name)
        base2 = m.TRANCHE_MEMBERS[2]
        for label, fn in sel:
            m.TRANCHE_MEMBERS[2] = frozenset(fn(set(base2)))
            fails, info = m.check(m.OBJ, m.ROOT)
            m.TRANCHE_MEMBERS[2] = base2
            print('  %-14s %-60s exit %d  failures %s' % (name or 'real', label, 1 if fails else 0, fails))
    # the add tamper together with the CN-1 near-miss promotion of W on #829's record (label kept 4): the real
    # checker vs the mutant; tree mode, then history mode (what check_objects --reconstitute runs)
    if PIN_PART not in (None, 'c'):
        sys.exit(0)
    print('  -- the COUNT add of W together with the CN-1 near-miss promotion of W on #829\'s record (tranche label 4 kept)')
    objd = os.path.join(SD, 'objects')
    if os.path.isdir(objd):
        shutil.rmtree(objd)
    os.makedirs(objd)
    # the stored object files by symlink (no copy); only manifest.json is this experiment's own
    for nm in os.listdir(os.path.join(A, 'objects')):
        if nm != 'manifest.json':
            os.symlink(os.path.join(A, 'objects', nm), os.path.join(objd, nm))
    man = json.load(open(os.path.join(A, 'objects', 'manifest.json'), encoding='utf-8'))
    R9 = 'verification/programmes/oi-qm/reconstruction/round-ktoken-maxcone-1/preregistration.md'
    d9 = subprocess.run(['git', '-C', WT, 'show', 'e12c1573:' + R9], capture_output=True).stdout.decode('utf-8')
    d9 = d9.replace('`%s`' % W, '`%s0`' % W[:-1], 1)
    e = next(x for x in man['objects'] if x['oid'] == W)
    e.pop('awaiting_citation')
    e['cited'] = [{'location': '%s:422' % R9, 'tokens': [W[:8]], 'via': 'token'},
                  {'location': '%s:423' % R9, 'tokens': [W[:8]], 'run': '39043849411', 'via': 'run'}]
    json.dump(man, open(os.path.join(objd, 'manifest.json'), 'w'), indent=1, sort_keys=True)
    oroot = os.path.join(SD, 'oroot')
    if os.path.isdir(oroot):
        shutil.rmtree(oroot)
    os.makedirs(oroot)
    # the repository through symlinks, except along the record's path (as the self-test's overlay does)
    src, dst = WT, oroot
    for nm in os.listdir(src):
        os.symlink(os.path.join(src, nm), os.path.join(dst, nm))
    for part in R9.split('/')[:-1]:
        src, dst = os.path.join(src, part), os.path.join(dst, part)
        if os.path.islink(dst):
            os.unlink(dst)
            os.makedirs(dst)
            for nm in os.listdir(src):
                os.symlink(os.path.join(src, nm), os.path.join(dst, nm))
        elif not os.path.isdir(dst):
            os.makedirs(dst)
    p9 = os.path.join(oroot, R9)
    open(p9, 'w', encoding='utf-8').write(d9)
    for name in (None, 'N-pin-digest-off'):
        m = module('check_objects.py', name)
        base2 = m.TRANCHE_MEMBERS[2]
        for label, s in (('pin unchanged', base2), ('pin + W (count add)', base2 | {W})):
            m.TRANCHE_MEMBERS[2] = frozenset(s)
            fails, info = m.check(objd, oroot)
            hf = m.Fails()
            if not fails and os.environ.get('HISTORY') == '1':      # writes ~15 MB of temp: CI only
                m.history_checks(WT, info, hf)
            m.TRANCHE_MEMBERS[2] = base2
            print('  %-14s near-miss + %-22s tree exit %d failures %s; history %s' % (
                name or 'real', label, 1 if fails else 0, fails, ('exit %d %s' % (1 if hf else 0, list(hf)))
                if not fails and os.environ.get('HISTORY') == '1' else
                'not run (%s)' % ('tree mode failed' if fails else 'local run: HISTORY=1 in CI')))
    shutil.rmtree(objd)
    shutil.rmtree(oroot)
# ---------------------------------------------------------------------------------------------------- decimal
if 'decimal' in SECTIONS:
    hdr('N-41-63-ignored: an isolated record whose only defect is another head in a 52-digit hex word beside the run; '
        'and the input class the mutant changes (an all-decimal word of 41-63 digits)')
    co_, com = module('check_objects.py'), module('check_objects.py', 'N-41-63-ignored')
    cr_ = module('check_retention.py')
    base = '# iso\n- `%s`: the head of a design run.\n- The workflow was dispatched on exactly that head: run %s, `head_sha` `%s…`.\n' % (OID, RID, OID[:8])
    glued = base + '\n| `evidence/run1-%sa%s.json` |\n' % (RID, OTHER)
    dec = base + '\n| `evidence/run1-%s.json` | `%s` |\n' % (RID, '9' * 45)
    rbase = '# iso\nThe design compiled at `%s`, workflow run\n[%s](runs/%s).\n' % (R13_HEAD, R13_RID, R13_RID)
    for nm, t, rt in (('glued 52-digit hex head', glued, rbase + '\n| `evidence/run1-%sa%s.json` |\n' % (R13_RID, OTHER)),
                      ('45-digit decimal word', dec, rbase + '\n| `evidence/run1-%s.json` | `%s` |\n' % (R13_RID, '9' * 45))):
        print('  %s: appended line %r' % (nm, t.rstrip('\n').split('\n')[-1]))
        land(root, {REC: t})
        show('O10, %s, real' % nm, o10(co_, root))
        show('O10, %s, mutant' % nm, o10(com, root))
        land(root, {REC: rt})
        cr_._OBJECTS_RULES = co_
        show('R13, %s, real' % nm, r13(cr_, root))
        cr_._OBJECTS_RULES = com
        show('R13, %s, mutant' % nm, r13(cr_, root))
        cr_._OBJECTS_RULES = None
# ---------------------------------------------------------------------------------------------------- crash
if 'crash' in SECTIONS:
    hdr('the crash family: each mutant\'s target fixtures, isolated, through pending_citation (real vs mutant)')
    co_ = module('check_objects.py')
    dg = co_.sha256(b'a stand-in log\n')
    base = '# iso\n- `%s`: the head of a design run.\n- The workflow was dispatched on exactly that head: run %s, `head_sha` `%s…`.\n' % (OID, RID, OID[:8])
    fx = {'evidence file name with its digest': base + '| path | sha256 |\n| --- | --- |\n| `evidence/run1-%s.json` | `%s` |\n' % (RID, dg),
          'boundary (a): digest beside the citation': base.replace('`%s…`.' % OID[:8], '`%s…`. Log `evidence/run1-%s.json`, sha256 `%s`.' % (OID[:8], RID, dg)),
          'documented limitation (64-digit word with another head)': base + '| `evidence/run1-%s.json` | `%s%s` |\n' % (RID, '0' * 24, OTHER)}
    for mut in ('N-all-free', 'N-no-joiners', 'N-64-as-head'):
        m = module('check_objects.py', mut)
        for nm, t in fx.items():
            land(root, {REC: t})
            show('%s | %s, real' % (mut, nm), o10(co_, root))
            show('%s | %s, mutant' % (mut, nm), o10(m, root))
if os.path.isdir(root):
    shutil.rmtree(root)
