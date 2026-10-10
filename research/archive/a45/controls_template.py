#!/usr/bin/env python3
"""controls.py -- act 45's own contracts, FROZEN with the preregistration beside it.

Imports nothing from the repository and changes nothing. Reads D and the commit under check through git, and embeds
every frozen text it compares against: the module's frozen statements and definitions, the frozen manuscript and
roadmap insertions, the census transform, the workflow edit, the import line, the probe blob, the outcome sentences and
the clause.

  controls.py check <commit> [--freeze F]   the execution at <commit> against D (and, with F, the preregistration
                                            unchanged from F and F = D plus the preregistration alone)
  controls.py --self-test                   constants against the preregistration beside this file; two synthetic
                                            rows (PROVED, UNDECIDED) that must hold; mutation controls that must fail
                                            with their named codes
"""
import hashlib, json, os, re, subprocess, sys

D = 'fa6ddf77703a8ce7f9eaf573ef48355194d72541'
RDIR = 'verification/programmes/oi-qm/track-b/act-45-fixed-basis-image/'
MODULE = 'verification/lean-mathlib/OIBridge/TrackBQfbBridge.lean'
PROBE = 'verification/lean/fixed_basis_ancilla_probe.py'
PROBE_BLOB = '@@PROBE_BLOB@@'
REFERENCE_BLOB = '@@REFERENCE_BLOB@@'
IMPORTS = 'verification/lean-mathlib/OIBridge.lean'
CENSUS = 'verification/lean-manuscript-census.json'
WORKFLOW = '.github/workflows/verify.yml'
ROADMAP = 'verification/ROADMAP.md'
MANUSCRIPTS = ['papers/Main.md', 'papers/Explainer.md', 'book/ch01-observation.md', 'book/ch19-open-problems.md',
               'book/The-Incompleteness-of-Observation-FULL.md']
BUILT = {'papers/Main.md': 'papers/Main', 'papers/Explainer.md': 'papers/Explainer',
         'book/The-Incompleteness-of-Observation-FULL.md': 'book/The-Incompleteness-of-Observation-FULL'}
LABELS = ('A45-BRIDGE-PROVED', 'A45-UNDECIDED')

EDITS = @@EDITS@@
FROZEN = @@FROZEN@@
WORKFLOW_EDITS = @@WORKFLOW_EDITS@@
IMPORT_EDIT = ('import OIBridge.DitaTorusLocus\n', 'import OIBridge.DitaTorusLocus\nimport OIBridge.TrackBQfbBridge\n')
FAMILY = @@FAMILY@@
OPSRC_ANCHOR = {'file': 'papers/Main.md', 'anchor': '`padData_rooted`'}
SENTENCES = @@SENTENCES@@
CLAUSE = @@CLAUSE@@
CLAUSE_MENTION = '**THE CLAUSE, carried at this mention — the result.**'
PROBE_OK_PREFIX = 'fixed_basis_ancilla_probe: OK -- 16 checks'
SYNTHETIC_PROBE = b'# synthetic probe for the self-test\n'
FORBIDDEN = ('sorry', 'admit', 'native_decide', 'axiom ', 'unsafe', 'opaque ', 'implemented_by', 'extern')
ALLOWED_OPTION = 'set_option linter.unusedSectionVars false'


def blob(data):
    return hashlib.sha1(b'blob %d\0' % len(data) + data).hexdigest()


# ---- the expected tree ------------------------------------------------------------------------------------------
def expected_census(d_census, label):
    c = json.loads(d_census)
    fam = json.loads(json.dumps(FAMILY))
    if label == 'A45-BRIDGE-PROVED':
        for f in c['families']:
            if f['modules'] == ['OperationalSourcing']:
                f['status'] = 'current'
                f['manuscript'] = [OPSRC_ANCHOR]
    else:
        fam['status'] = 'kernel-only'
        fam['manuscript'] = []
    c['families'].append(fam)
    return (json.dumps(c, indent=2, ensure_ascii=False) + '\n').encode()


def apply_edits(text, edits):
    for anchor, ins in edits:
        if text.count(anchor) != 1:
            raise ValueError('anchor not unique')
        text = text.replace(anchor, anchor + ins)
    return text


def expected_text(d_files, path, label):
    text = d_files[path].decode()
    if path == WORKFLOW:
        for old, new in WORKFLOW_EDITS:
            if text.count(old) != 1:
                raise ValueError('workflow anchor')
            text = text.replace(old, new)
        return text.encode()
    if path == IMPORTS:
        return text.replace(*IMPORT_EDIT).encode()
    if path == CENSUS:
        return expected_census(d_files[path], label)
    if label == 'A45-BRIDGE-PROVED' and path in EDITS:
        return apply_edits(text, EDITS[path]).encode()
    return d_files[path]


# ---- the checks -------------------------------------------------------------------------------------------------
def statement(module, name):
    for sep in (' ', '\n'):
        k = module.find('theorem ' + name + sep)
        if k >= 0:
            return module[k:module.index(':=', k) + 2]
    return None


def check_module(module, label):
    codes = []
    if not module.startswith(FROZEN['header']):
        codes.append('module:header')
    for name, text in FROZEN['defs'].items():
        if module.count(text) != 1:
            codes.append('module:def:' + name)
    if len(re.findall(r'^(?:noncomputable )?def ', module, re.M)) != len(FROZEN['defs']) \
            or re.search(r'^(?:abbrev|instance|structure|class|inductive) ', module, re.M):
        codes.append('module:definition-budget')
    for tok in FORBIDDEN:
        if re.search(r'(?<![A-Za-z_])' + re.escape(tok), module):
            codes.append('module:forbidden:' + tok.strip())
    for opt in re.findall(r'^set_option .*$', module, re.M):
        if opt != ALLOWED_OPTION:
            codes.append('module:set_option')
    names = re.findall(r'^theorem (\S+)', module, re.M)
    for n in names:
        if n not in FROZEN['statements'] and not n.startswith('a45_shared_'):
            codes.append('module:unknown-name:' + n)
        if module.count('#print axioms ' + n + '\n') != 1:
            codes.append('module:print-axioms:' + n)
    for n, text in FROZEN['statements'].items():
        if n == 'a45_bridge_kernel' and label != 'A45-BRIDGE-PROVED':
            if n in names:
                codes.append('module:verdict-under-undecided')
            continue
        if statement(module, n) != text:
            codes.append('module:statement:' + n)
    return codes


def check_note(note, label, module_blob):
    codes = []
    lines = note.split('\n')
    outs = [l for l in lines if l.startswith('**Outcome:**')]
    if outs != ['**Outcome:** `%s`' % label]:
        codes.append('note:outcome-line')
    for lab in LABELS:
        n = note.count(SENTENCES[lab])
        if n != (1 if lab == label else 0):
            codes.append('note:sentence:' + lab)
    if note.count(CLAUSE_MENTION) != 1 or note.count(CLAUSE) != 1 \
            or note.index(CLAUSE) < note.index(CLAUSE_MENTION):
        codes.append('note:clause')
    if sum(1 for l in lines if l.strip().strip('`').startswith(PROBE_OK_PREFIX)) != 1:
        codes.append('note:probe-line')
    if '`%s`' % REFERENCE_BLOB not in note or '`%s`' % module_blob not in note:
        codes.append('note:blobs')
    if module_blob != REFERENCE_BLOB and 'departure from the reference implementation' not in note:
        codes.append('note:departure')
    return codes


def check_tree(d_files, e_files, changed, probe_blob=PROBE_BLOB):
    """d_files/e_files: path -> bytes (None if absent) for every path consulted; changed: {path: 'A'|'M'|'D'}."""
    codes = []
    note = e_files.get(RDIR + 'result.md')
    if note is None:
        return ['note:absent']
    note = note.decode()
    m = re.search(r'^\*\*Outcome:\*\* `([^`]*)`', note, re.M)
    label = m.group(1) if m and m.group(1) in LABELS else None
    if label is None:
        return ['note:outcome-line']
    module = e_files.get(MODULE)
    if module is None:
        return ['module:absent']
    codes += check_module(module.decode(), label)
    codes += check_note(note, label, blob(module))
    if e_files.get(PROBE) is None or blob(e_files[PROBE]) != probe_blob:
        codes.append('probe:blob')
    for path in (WORKFLOW, IMPORTS, CENSUS) + tuple(MANUSCRIPTS):
        try:
            exp = expected_text(d_files, path, label)
        except ValueError:
            exp = None
        if e_files.get(path) != exp:
            codes.append('surface:' + path)
    road_exp = apply_edits(d_files[ROADMAP].decode(), EDITS[ROADMAP]).encode() if label == 'A45-BRIDGE-PROVED' \
        else d_files[ROADMAP]
    if e_files.get(ROADMAP) != road_exp:
        codes.append('surface:' + ROADMAP)
    for md, stem in BUILT.items():
        tex, pdf = e_files.get(stem + '.tex'), e_files.get(stem + '.pdf')
        stamp = re.search(rb'^% source-sha256: ([0-9a-f]{64})\s*$', tex or b'', re.M)
        if not stamp or stamp.group(1).decode() != hashlib.sha256(e_files[md]).hexdigest():
            codes.append('built:stamp:' + stem)
        if label == 'A45-BRIDGE-PROVED' and (pdf is None or pdf == d_files[stem + '.pdf']):
            codes.append('built:pdf:' + stem)
    want = {RDIR + 'preregistration.md': 'A', RDIR + 'controls.py': 'A', RDIR + 'result.md': 'A',
            MODULE: 'A', PROBE: 'A', IMPORTS: 'M', CENSUS: 'M', WORKFLOW: 'M'}
    if label == 'A45-BRIDGE-PROVED':
        want[ROADMAP] = 'M'
        for md in MANUSCRIPTS:
            want[md] = 'M'
        for stem in BUILT.values():
            want[stem + '.tex'] = 'M'
            want[stem + '.pdf'] = 'M'
    if changed != want:
        codes.append('paths')
    return codes


# ---- git access -------------------------------------------------------------------------------------------------
def git(*args):
    return subprocess.run(('git',) + args, capture_output=True, check=True).stdout


def show(commit, path):
    r = subprocess.run(['git', 'show', '%s:%s' % (commit, path)], capture_output=True)
    return r.stdout if r.returncode == 0 else None


def consulted():
    paths = [RDIR + 'result.md', RDIR + 'preregistration.md', MODULE, PROBE, WORKFLOW, IMPORTS, CENSUS, ROADMAP]
    paths += MANUSCRIPTS
    for stem in BUILT.values():
        paths += [stem + '.tex', stem + '.pdf']
    return paths


def cmd_check(commit, freeze=None):
    d_files = {p: show(D, p) for p in consulted()}
    e_files = {p: show(commit, p) for p in consulted()}
    changed = {}
    for line in git('diff', '--no-renames', '--name-status', D, commit).decode().splitlines():
        st, path = line.split('\t', 1)
        changed[path] = st
    codes = check_tree(d_files, e_files, changed)
    if freeze:
        fdiff = git('diff', '--no-renames', '--name-status', D, freeze).decode().split()
        if fdiff != ['A', RDIR + 'preregistration.md']:
            codes.append('freeze:delta')
        if show(freeze, RDIR + 'preregistration.md') != e_files[RDIR + 'preregistration.md']:
            codes.append('freeze:preregistration')
    if codes:
        print('controls: check FAILED: ' + '; '.join(codes))
        return 1
    print('controls: check OK')
    return 0


# ---- self-test --------------------------------------------------------------------------------------------------
def synthetic_module(label):
    parts = [FROZEN['header'], 'namespace OIBridge\n\nnamespace TrackBQfbBridge\n\n' + ALLOWED_OPTION + '\n\n']
    for text in FROZEN['defs'].values():
        parts.append(text + '\n\n')
    for n, text in FROZEN['statements'].items():
        if n == 'a45_bridge_kernel' and label != 'A45-BRIDGE-PROVED':
            continue
        parts.append(text + ' by\n  exact placeholder\n#print axioms %s\n\n' % n)
    parts.append('end TrackBQfbBridge\n\nend OIBridge\n')
    return ''.join(parts).encode()


def synthetic_row(d_files, label):
    e = dict(d_files)
    module = synthetic_module(label)
    e[MODULE] = module
    e[PROBE] = SYNTHETIC_PROBE
    for path in (WORKFLOW, IMPORTS, CENSUS) + tuple(MANUSCRIPTS):
        e[path] = expected_text(d_files, path, label)
    if label == 'A45-BRIDGE-PROVED':
        e[ROADMAP] = apply_edits(d_files[ROADMAP].decode(), EDITS[ROADMAP]).encode()
    for md, stem in BUILT.items():
        e[stem + '.tex'] = b'% source-sha256: ' + hashlib.sha256(e[md]).hexdigest().encode() + b'\n'
        if label == 'A45-BRIDGE-PROVED':
            e[stem + '.pdf'] = b'%PDF synthetic ' + stem.encode()
    e[RDIR + 'preregistration.md'] = b'frozen'
    note = ['# result', '', '**Outcome:** `%s`' % label, '', SENTENCES[label], '', CLAUSE_MENTION, '', CLAUSE, '',
            '`' + PROBE_OK_PREFIX + ' (synthetic)`', '',
            'reference `%s`, module at E `%s`, departure from the reference implementation' % (REFERENCE_BLOB, blob(module))]
    e[RDIR + 'result.md'] = '\n'.join(note).encode()
    changed = {RDIR + 'preregistration.md': 'A', RDIR + 'controls.py': 'A', RDIR + 'result.md': 'A',
               MODULE: 'A', PROBE: 'A', IMPORTS: 'M', CENSUS: 'M', WORKFLOW: 'M'}
    if label == 'A45-BRIDGE-PROVED':
        changed[ROADMAP] = 'M'
        for md in MANUSCRIPTS:
            changed[md] = 'M'
        for stem in BUILT.values():
            changed[stem + '.tex'] = 'M'
            changed[stem + '.pdf'] = 'M'
    return e, changed


def self_test():
    here = os.path.dirname(os.path.abspath(__file__))
    prereg = open(os.path.join(here, 'preregistration.md'), encoding='utf-8').read()
    bad = []
    for lab in LABELS:
        if prereg.count(SENTENCES[lab]) != 1:
            bad.append('prereg:sentence:' + lab)
    if prereg.count(CLAUSE) < 1:
        bad.append('prereg:clause')
    for n, text in FROZEN['statements'].items():
        if text not in prereg:
            bad.append('prereg:statement:' + n)
    for n, text in FROZEN['defs'].items():
        if text not in prereg:
            bad.append('prereg:def:' + n)
    for path, eds in EDITS.items():
        for _, ins in eds:
            if ins.strip() not in prereg:
                bad.append('prereg:insertion:' + path)
    for b in (PROBE_BLOB, REFERENCE_BLOB):
        if b not in prereg:
            bad.append('prereg:blob:' + b)
    if bad:
        print('controls: self-test FAILED (constants): ' + '; '.join(bad))
        return 1
    print('controls: the frozen constants match the preregistration beside this file')

    d_files = {p: show(D, p) for p in consulted()}
    rows = {}
    for lab in LABELS:
        e, ch = synthetic_row(d_files, lab)
        codes = check_tree(d_files, e, ch, probe_blob=blob(SYNTHETIC_PROBE))
        if codes:
            print('controls: self-test FAILED: synthetic row %s: %s' % (lab, codes))
            return 1
        rows[lab] = (e, ch)
    print('controls: 2 rows hold as frozen')

    muts = []
    def mut(name, code, label, fn):
        muts.append((name, code, label, fn))
    P, U = 'A45-BRIDGE-PROVED', 'A45-UNDECIDED'
    def edit_file(path, old, new):
        def f(e, ch):
            e[path] = e[path].replace(old.encode(), new.encode(), 1)
        return f
    first_ins = lambda p: EDITS[p][0][1]
    mut('verdict removed under PROVED', 'module:statement:a45_bridge_kernel', P,
        lambda e, ch: e.__setitem__(MODULE, e[MODULE].replace(b'theorem a45_bridge_kernel', b'theorem a45_other')))
    mut('verdict present under UNDECIDED', 'module:verdict-under-undecided', U,
        lambda e, ch: e.__setitem__(MODULE, e[MODULE] + FROZEN['statements']['a45_bridge_kernel'].encode()
                                    + b' by\n  x\n#print axioms a45_bridge_kernel\n'))
    mut('a frozen statement weakened', 'module:statement:bridge_traj', P,
        edit_file(MODULE, 'permClass V M) (hN : permClass V N) (K : ℕ)', 'permClass V M) (hN : permClass V N) (K : ℕ) (hK : 0 < K)'))
    mut('a definition changed', 'module:def:realData', P, edit_file(MODULE, 'read := id', 'read := fun b => b'))
    mut('an extra definition', 'module:definition-budget', P,
        lambda e, ch: e.__setitem__(MODULE, e[MODULE].replace(b'end TrackBQfbBridge', b'def extra : Nat := 0\n\nend TrackBQfbBridge')))
    mut('a missing #print axioms', 'module:print-axioms:bridge', P,
        edit_file(MODULE, '#print axioms bridge\n', ''))
    mut('sorry in the module', 'module:forbidden:sorry', P, edit_file(MODULE, 'exact placeholder', 'sorry'))
    mut('an unlisted theorem name', 'module:unknown-name:helper', P,
        lambda e, ch: e.__setitem__(MODULE, e[MODULE].replace(b'end TrackBQfbBridge', b'theorem helper : True := trivial\n#print axioms helper\n\nend TrackBQfbBridge')))
    mut('an extra set_option', 'module:set_option', P,
        edit_file(MODULE, ALLOWED_OPTION, ALLOWED_OPTION + '\nset_option maxHeartbeats 0'))
    mut('the header changed', 'module:header', P, edit_file(MODULE, 'import OIBridge.DitaHull', 'import OIBridge.DitaTorus'))
    mut('the probe changed', 'probe:blob', P, lambda e, ch: e.__setitem__(PROBE, b'# not the frozen probe\n'))
    mut('the workflow edited beyond the frozen edit', 'surface:' + WORKFLOW, P,
        lambda e, ch: e.__setitem__(WORKFLOW, e[WORKFLOW] + b'# extra\n'))
    mut('the import misplaced', 'surface:' + IMPORTS, P,
        lambda e, ch: e.__setitem__(IMPORTS, d_files[IMPORTS] + b'import OIBridge.TrackBQfbBridge\n'))
    mut('the census family left kernel-only under PROVED', 'surface:' + CENSUS, P,
        lambda e, ch: e.__setitem__(CENSUS, expected_census(d_files[CENSUS], U)))
    mut('a word changed in Main', 'surface:papers/Main.md', P,
        edit_file('papers/Main.md', 'contractively scaled partial permutations', 'scaled partial permutations'))
    mut('the FULL mirror missing ch19 insertion', 'surface:book/The-Incompleteness-of-Observation-FULL.md', P,
        edit_file('book/The-Incompleteness-of-Observation-FULL.md', first_ins('book/ch19-open-problems.md'), ''))
    mut('manuscripts edited under UNDECIDED', 'surface:papers/Main.md', U,
        lambda e, ch: e.__setitem__('papers/Main.md', rows[P][0]['papers/Main.md']))
    mut('a stale .tex stamp', 'built:stamp:papers/Main', P,
        lambda e, ch: e.__setitem__('papers/Main.tex', b'% source-sha256: ' + b'0' * 64 + b'\n'))
    mut('the pdf not rebuilt', 'built:pdf:book/The-Incompleteness-of-Observation-FULL', P,
        lambda e, ch: e.__setitem__('book/The-Incompleteness-of-Observation-FULL.pdf',
                                    d_files['book/The-Incompleteness-of-Observation-FULL.pdf']))
    mut('the roadmap sentence altered', 'surface:' + ROADMAP, P,
        edit_file(ROADMAP, 'no relation is adopted', 'a relation is adopted'))
    mut('the roadmap touched under UNDECIDED', 'surface:' + ROADMAP, U,
        lambda e, ch: e.__setitem__(ROADMAP, rows[P][0][ROADMAP]))
    mut('an extra path changed', 'paths', P, lambda e, ch: ch.__setitem__('papers/GR.md', 'M'))
    mut('a governed path missing', 'paths', P, lambda e, ch: ch.pop(WORKFLOW))
    mut('two outcome lines', 'note:outcome-line', P,
        lambda e, ch: e.__setitem__(RDIR + 'result.md', e[RDIR + 'result.md'] + b'\n**Outcome:** `A45-UNDECIDED`\n'))
    mut("the other label's sentence", 'note:sentence:A45-UNDECIDED', P,
        lambda e, ch: e.__setitem__(RDIR + 'result.md', e[RDIR + 'result.md'] + b'\n' + SENTENCES[U].encode()))
    mut('the clause missing', 'note:clause', P, edit_file(RDIR + 'result.md', CLAUSE, ''))
    mut('the probe line missing', 'note:probe-line', P, edit_file(RDIR + 'result.md', PROBE_OK_PREFIX, 'probe'))
    mut('the blobs missing', 'note:blobs', P, edit_file(RDIR + 'result.md', REFERENCE_BLOB, 'x'))
    mut('the departure unreported', 'note:departure', P,
        edit_file(RDIR + 'result.md', 'departure from the reference implementation', ''))
    mut('no result note', 'note:absent', P, lambda e, ch: e.__setitem__(RDIR + 'result.md', None))
    failed = 0
    for name, code, lab, fn in muts:
        e, ch = synthetic_row(d_files, lab)
        fn(e, ch)
        codes = check_tree(d_files, e, ch, probe_blob=blob(SYNTHETIC_PROBE))
        if code not in codes:
            print('controls: self-test FAILED: mutation "%s" did not fail with %s (got %s)' % (name, code, codes))
            failed += 1
    if failed:
        return 1
    print('controls: %d mutation controls fail as required' % len(muts))
    print('controls: self-test OK')
    return 0


if __name__ == '__main__':
    a = sys.argv[1:]
    if a == ['--self-test']:
        sys.exit(self_test())
    if len(a) in (2, 4) and a[0] == 'check' and (len(a) == 2 or a[2] == '--freeze'):
        sys.exit(cmd_check(a[1], a[3] if len(a) == 4 else None))
    print(__doc__)
    sys.exit(2)
