"""Track B act 32 -- the round's own static controls, frozen with the control plane.

Written before F; its blob is frozen in the preregistration beside it, and the execution adds it
with that exact blob. It reads nothing but the repository at D and at the commit under check, and
it certifies nothing on its own: the Lean kernel, the axiom audit and the release gate establish
the mathematics, and the V3 verifier the protocol. What it checks is that the execution carries
the frozen statements, the frozen outcome grammar, the frozen surface edits and the frozen guard
ledger, and nothing else.

    python3 controls.py --self-test     the duality of the two verdict propositions, the single
                                        source of every shared text, the mutation controls on
                                        synthetic inputs, and the agreement of the constants
                                        below with the preregistration beside this file
    python3 controls.py check <commit>  every control against the tree at <commit>, read from git

Exit 1 on any failure.
"""
import hashlib
import json
import os
import re
import subprocess
import sys

D = '@@D@@'
RDIR = 'verification/programmes/oi-qm/track-b/act-32-orbit-isometry-classification/'
MODULE = 'verification/lean-mathlib/OIBridge/OrbitIsometryClassification.lean'
ROOT = 'verification/lean-mathlib/OIBridge.lean'
GUARD = 'verification/lean/edge_rigidity_probe.py'
CENSUS = 'verification/lean-manuscript-census.json'
ROADMAP = 'verification/ROADMAP.md'
ROADMAP_BLOB_D = '@@ROADMAP_BLOB_D@@'
GUARD_BLOB_D = '@@GUARD_BLOB_D@@'
GUARD_BLOB_RETIRED = '@@GUARD_BLOB_RETIRED@@'

IMPORT = 'import OIBridge.OrbitGeometryRigidity\n'
WIRE_AFTER = 'import OIBridge.StrictNaturalLift\n'
WIRE = 'import OIBridge.OrbitIsometryClassification\n'
OPEN = @@OPEN@@
NAMESPACE = 'OrbitIsometryClassification'

# ---- the frozen propositions, verbatim
PROPS = @@PROPS@@
# ---- the components every proposition is built from
COMPONENTS = @@COMPONENTS@@

# ---- the label theorems: (label, theorem name, proposition)
LABELS = (('A32-RIGID', 'a32_rigid', 'P_R'), ('A32-NOT-RIGID', 'a32_not_rigid', 'P_N'))
UNDECIDED = 'A32-UNDECIDED'
ROWS = ('A32-RIGID', 'A32-NOT-RIGID', 'A32-UNDECIDED')
# ---- the corollary, required in every case
COROLLARY = ('a32_c_exclusive', ('P_N',), 'P_R')
# ---- the statements each decided label requires: (theorem name, proposition)
WITNESS = (('a32_shared_exists', 'S_EXIST'), ('a32_shared_isometry', 'S_ISO'),
           ('a32_shared_separation', 'S_SEP'))
CONTROLS = (('a32_control_overlap', 'S_OVL'), ('a32_control_moves', 'S_MOVE'),
            ('a32_control_global', 'S_GLOBAL'), ('a32_control_identity', 'S_ID'),
            ('a32_control_quarter', 'S_QUARTER'))
REQUIRED = {'A32-NOT-RIGID': WITNESS + CONTROLS,
            'A32-RIGID': (('a32_control_global', 'S_GLOBAL'), ('a32_control_identity', 'S_ID')),
            'A32-UNDECIDED': ()}
SHARED = re.compile(r'a32_shared_[A-Za-z0-9_]+\Z')
OUTCOME_RE = re.compile(r'\*\*Outcome:\*\* `(A32-[A-Z-]+)`')
LABEL_RE = re.compile(r'A32-(?:NOT-RIGID|RIGID|UNDECIDED)')

SENTENCES = @@SENTENCES@@
# the clause's body; its heading names the artifact carrying it
CLAUSE = @@CLAUSE@@
MENTION = 'THE CLAUSE, carried at this mention'

# ---- the P0 cell: the clause of acts 25 and 26 that a decided outcome makes stale, act 30's closing
# sentence and standing clause, and this round's sentence per case with its standing clause
P0_STALE = @@P0_STALE@@
P0_ADMITS = @@P0_ADMITS@@
P0_STANDING = @@P0_STANDING@@
P0_CASE = @@P0_CASE@@
P0_STANDING_32 = @@P0_STANDING_32@@

# ---- the guard-retirement ledger: each entry an exact splice of the guard at D
LEDGER = @@LEDGER@@
# the bindings the ledger removes; the retired guard must not reference any of them
REMOVED_BINDINGS = ('_OGCROAD', '_CGRROAD', '_ogc_m11', '_cgr_m11')

CENSUS_MODULES = ['OrbitIsometryClassification']

_BAD_CMD = re.compile(
    r'(?m)^[ \t]*(?:@\[[^\]\n]*\][ \t]*)?(?:(?:private|protected|noncomputable|partial|unsafe)'
    r'[ \t]+)*(?:def|abbrev|structure|class|instance|axiom|opaque|inductive|variable|include|omit|'
    r'export|notation|infix|infixl|infixr|prefix|postfix|macro|macro_rules|syntax|elab|elab_rules|'
    r'attribute|universe|mutual|local|scoped|import|#check|#eval|#reduce|#exit|#guard)\b')
_BAD_TOKEN = re.compile(r'\b(?:sorry|admit|native_decide)\b')


# ------------------------------------------------------------------------------------------------
def norm(t):
    t = ' '.join(t.split())
    t = re.sub(r'\( ', '(', t)
    return re.sub(r' \)', ')', t)


def qnorm(t):
    return ' '.join(re.sub(r'(?m)^[ \t]*>[ \t]?', '', t).split())


def sha(t):
    return hashlib.sha256(t.encode('utf-8')).hexdigest()


def dual_texts(c):
    """The two verdict propositions, rebuilt from their shared components."""
    r = c['HEAD'] + '  ∀ ' + c['PHI'] + ',\n    (' + c['HYP'] + ') →\n    (' + c['FOUR'] + ')'
    n = c['HEAD'] + '  ∃ ' + c['PHI'] + ',\n    (' + c['HYP'] + ')\n    ∧ ¬ (' + c['FOUR'] + ')'
    return r, n


def duality_ok(props, comps):
    """P_R is `∀ φ, H → FOUR` and P_N is `∃ φ, H ∧ ¬ FOUR` over one head, one hypothesis text H and
    one four-shape text FOUR, so each is the other's negation; every other statement carries the
    same H, H3, FOUR, WIT and QTR strings, verbatim."""
    f = []
    r, n = dual_texts(comps)
    if norm(props['P_R']) != norm(r):
        f.append('duality:P_R-is-not-the-frozen-universal-form')
    if norm(props['P_N']) != norm(n):
        f.append('duality:P_N-is-not-the-frozen-existential-form')
    if norm(comps['H3']) not in norm(comps['HYP']):
        f.append('source:the-distance-conjunct-is-not-the-hypotheses-own')
    for key, comp, k in (('S_ISO', 'HYP', 1), ('S_GLOBAL', 'HYP', 1), ('S_ID', 'HYP', 1),
                         ('S_SEP', 'FOUR', 1), ('S_GLOBAL', 'FOUR', 1), ('S_ID', 'FOUR', 1),
                         ('S_EXIST', 'WIT', 1), ('S_ISO', 'WIT', 1), ('S_SEP', 'WIT', 1),
                         ('S_MOVE', 'WIT', 1), ('S_QUARTER', 'QTR', 2), ('S_QUARTER', 'H3', 1)):
        if norm(props[key]).count(norm(comps[comp])) != k:
            f.append('source:%s-does-not-carry-%s' % (key, comp))
    if not norm(props['S_QUARTER']).startswith(norm(comps['HEAD']) + ' (∃ ' + norm(comps['PHI'])):
        f.append('source:S_QUARTER-without-its-existence-conjunct')
    return f


def strip_comments(src):
    out, i, depth, n = [], 0, 0, len(src)
    while i < n:
        if src.startswith('/-', i):
            depth += 1
            i += 2
        elif depth and src.startswith('-/', i):
            depth -= 1
            i += 2
        elif depth:
            out.append('\n' if src[i] == '\n' else ' ')
            i += 1
        elif src.startswith('--', i):
            j = src.find('\n', i)
            i = n if j < 0 else j
        else:
            out.append(src[i])
            i += 1
    return ''.join(out)


_THM = re.compile(r'(?m)^[ \t]*(?:@\[[^\]\n]*\][ \t]*)?(?:private[ \t]+|protected[ \t]+)?'
                  r'(?:theorem|lemma)[ \t]+(\S+)')


def theorems(code):
    out = {}
    for m in _THM.finditer(code):
        nm = m.group(1)
        rest = code[m.end():]
        j = rest.find(':=')
        out[nm] = None if nm in out else (rest if j < 0 else rest[:j])
    return out


def statement(key):
    return norm(': ' + PROPS[key])


def corollary_statement():
    nm, prem, concl = COROLLARY
    return norm(': ' + ' → '.join('(' + PROPS[p] + ')' for p in prem) + ' → ¬ (' + PROPS[concl] + ')')


# ---- the module -------------------------------------------------------------------------------
def module_label(src):
    f = []
    if not src.startswith(IMPORT):
        f.append('module:first-line-is-not-the-frozen-import')
    code = strip_comments(src)
    body = code[len(IMPORT):] if code.startswith(IMPORT) else code
    if _BAD_CMD.search(body):
        f.append('module:forbidden-command:' + _BAD_CMD.search(body).group(0).strip())
    if _BAD_TOKEN.search(code):
        f.append('module:forbidden-token:' + _BAD_TOKEN.search(code).group(0))
    opens = [m.start() for m in re.finditer(r'(?m)^[ \t]*open\b', code)]
    if len(opens) != 1 or not code[opens[0]:].startswith(OPEN):
        f.append('module:open-is-not-exactly-the-frozen-one')
    if 'namespace OIBridge\nnamespace %s\n' % NAMESPACE not in code or \
            not code.rstrip().endswith('end %s\nend OIBridge' % NAMESPACE):
        f.append('module:namespace')
    th = theorems(code)
    if any(v is None for v in th.values()):
        f.append('module:theorem-declared-twice')
    if opens and th and min(m.start() for m in _THM.finditer(code)) < opens[0]:
        f.append('module:theorem-before-open')
    printed = re.findall(r'(?m)^[ \t]*#print[ \t]+axioms[ \t]+(\S+)[ \t]*$', code)
    if sorted(printed) != sorted(set(printed)):
        f.append('module:axioms-printed-twice')
    for nm in th:
        if nm not in printed:
            f.append('module:no-print-axioms:' + nm)
    for nm in printed:
        if nm not in th:
            f.append('module:print-axioms-of-no-theorem:' + nm)
    names = {x[1] for x in LABELS} | {COROLLARY[0]} | {x[0] for x in WITNESS + CONTROLS}
    for nm in th:
        if nm not in names and not SHARED.match(nm):
            f.append('module:theorem-name-outside-the-frozen-set:' + nm)
    earned = []
    for lab, nm, key in LABELS:
        if nm in th and th[nm] is not None:
            if norm(th[nm]) != statement(key):
                f.append('module:statement-not-frozen:' + nm)
            earned.append(lab)
    if len(earned) > 1:
        f.append('module:both-labels')
        return None, f
    label = earned[0] if earned else UNDECIDED
    if COROLLARY[0] not in th:
        f.append('module:required-corollary-absent:' + COROLLARY[0])
    elif th[COROLLARY[0]] is not None and norm(th[COROLLARY[0]]) != corollary_statement():
        f.append('module:statement-not-frozen:' + COROLLARY[0])
    for nm, key in WITNESS + CONTROLS:
        if nm in th and th[nm] is not None and norm(th[nm]) != statement(key):
            f.append('module:statement-not-frozen:' + nm)
    for nm, key in REQUIRED[label]:
        if nm not in th:
            f.append('module:required-statement-absent:' + nm)
    return label, f


# ---- the result note ---------------------------------------------------------------------------
def note_ok(note, label):
    f = []
    found = OUTCOME_RE.findall(note)
    if found != [label]:
        f.append('note:outcome-line:%s' % found)
    q = qnorm(note)
    if q.count(qnorm(SENTENCES[label])) != 1:
        f.append('note:frozen-sentence:' + label)
    for lab in SENTENCES:
        if lab != label and qnorm(SENTENCES[lab]) in q:
            f.append('note:sentence-of-a-label-not-earned:' + lab)
    body = qnorm(CLAUSE)
    if note.count(MENTION) != 1 or q.count(body) != 1 or \
            not 0 <= q.index(body) - q.index(MENTION) <= 80:
        f.append('note:the-clause')
    for nm, _ in REQUIRED[label]:
        if '`%s`' % nm not in note:
            f.append('note:required-statement-not-named:' + nm)
    if label != UNDECIDED:
        for e in LEDGER:
            if '`%s`' % e['entry'] not in note:
                f.append('note:ledger-entry-not-named:' + e['entry'])
    return f


# ---- the surfaces ------------------------------------------------------------------------------
def expected_roadmap(road_d, label):
    if label == UNDECIDED:
        return road_d
    if road_d.count(P0_STALE) != 2:
        return None
    r = road_d.replace(P0_STALE, '')
    old = ' ' + P0_ADMITS + ' ' + P0_STANDING + ' |'
    if r.count(old) != 1:
        return None
    return r.replace(old, ' ' + P0_ADMITS + ' ' + P0_STANDING + ' ' + P0_CASE[label] + ' '
                     + P0_STANDING_32 + ' |', 1)


def retired_guard(guard_d):
    g = guard_d
    for e in LEDGER:
        if sha(e['old']) != e['old_sha256'] or sha(e['new']) != e['new_sha256'] or g.count(e['old']) != 1:
            return None
        g = g.replace(e['old'], e['new'], 1)
    return g


def bindings_ok(guard):
    """No surviving code resolves to a binding the ledger removes."""
    return ['ledger:removed-binding-still-referenced:' + b for b in REMOVED_BINDINGS
            if re.search(r'\b%s\b' % re.escape(b), guard)]


def expected_guard(guard_d, label):
    return guard_d if label == UNDECIDED else retired_guard(guard_d)


def census_ok(cen_d, cen_e, label):
    f = []
    try:
        d, e = json.loads(cen_d), json.loads(cen_e)
    except ValueError:
        return ['census:not-json']
    if cen_e != json.dumps(e, indent=2, ensure_ascii=False) + '\n':
        f.append('census:not-in-the-registry-format')
    fams = e.get('families', [])
    mine = [x for x in fams if CENSUS_MODULES[0] in x.get('modules', [])]
    if len(mine) != 1 or fams[-1:] != mine:
        return f + ['census:family-count-or-place']
    m = mine[0]
    if m.get('modules') != CENSUS_MODULES or m.get('status') != 'kernel-only' or \
            m.get('manuscript') != []:
        f.append('census:family-disposition')
    if LABEL_RE.findall(m.get('note', '')) != [label]:
        f.append('census:outcome')
    if dict(e, families=fams[:-1]) != d:
        f.append('census:another-entry-changed')
    return f


def wire_ok(root_d, root_e):
    if root_d.count(WIRE_AFTER) != 1:
        return ['wire:anchor']
    return [] if root_e == root_d.replace(WIRE_AFTER, WIRE_AFTER + WIRE, 1) else ['wire:root']


def expected_paths(label):
    p = {RDIR + 'preregistration.md': 'A', RDIR + 'controls.py': 'A', RDIR + 'result.md': 'A',
         MODULE: 'A', ROOT: 'M', CENSUS: 'M'}
    if label != UNDECIDED:
        p[ROADMAP] = 'M'
        p[GUARD] = 'M'
    return p


def check_all(files_d, files_e, delta):
    f = duality_ok(PROPS, COMPONENTS)
    label, g = module_label(files_e.get(MODULE, ''))
    f += g
    if label is None:
        return f
    f += note_ok(files_e.get(RDIR + 'result.md', ''), label)
    road = expected_roadmap(files_d[ROADMAP], label)
    if road is None or files_e.get(ROADMAP) != road:
        f.append('roadmap:not-as-frozen-for-the-case')
    guard = expected_guard(files_d[GUARD], label)
    if guard is None or files_e.get(GUARD) != guard:
        f.append('guard:not-as-frozen-for-the-case')
    if label != UNDECIDED:
        f += bindings_ok(files_e.get(GUARD, ''))
    f += census_ok(files_d[CENSUS], files_e.get(CENSUS, ''), label)
    f += wire_ok(files_d[ROOT], files_e.get(ROOT, ''))
    if delta != expected_paths(label):
        f.append('paths:delta-is-not-the-frozen-set')
    return f


# ---- git ---------------------------------------------------------------------------------------
def git(*a):
    return subprocess.run(('git',) + a, capture_output=True, check=True).stdout


def blob_id(text):
    b = text.encode('utf-8')
    return hashlib.sha1(b'blob %d\0' % len(b) + b).hexdigest()


def cmd_check(commit):
    paths = (MODULE, ROOT, GUARD, CENSUS, ROADMAP, RDIR + 'result.md')
    fd, fe = {}, {}
    for p in paths:
        for ref, dst in ((D, fd), (commit, fe)):
            try:
                dst[p] = git('show', '%s:%s' % (ref, p)).decode('utf-8')
            except subprocess.CalledProcessError:
                pass
    f = []
    if blob_id(fd[ROADMAP]) != ROADMAP_BLOB_D or blob_id(fd[GUARD]) != GUARD_BLOB_D:
        f.append('base:D-is-not-the-frozen-base')
    rg = retired_guard(fd[GUARD])
    if rg is None or blob_id(rg) != GUARD_BLOB_RETIRED:
        f.append('ledger:does-not-reproduce-the-frozen-retired-guard')
    delta = {}
    for ln in git('diff', '--no-renames', '--name-status', D, commit).decode().splitlines():
        st, p = ln.split('\t', 1)
        delta[p] = st
    f += check_all(fd, fe, delta)
    label, _ = module_label(fe.get(MODULE, ''))
    print('controls: label read off the module:', label)
    print('controls: %d path(s) changed from D' % len(delta))
    return f


# ---- the self-test -----------------------------------------------------------------------------
def _module(label, extra='', drop=(), stmt=None):
    parts = [IMPORT, '/-! synthetic -/\n', 'namespace OIBridge\nnamespace %s\n\n' % NAMESPACE,
             OPEN, '\n']

    def th(nm, s):
        parts.append('theorem %s :\n    %s := by\n  exact test\n#print axioms %s\n\n' % (nm, s, nm))
    th('a32_shared_x', 'True')
    for nm, key in REQUIRED[label]:
        if nm not in drop:
            th(nm, (stmt or {}).get(nm, PROPS[key]))
    for lab, nm, key in LABELS:
        if lab == label and nm not in drop:
            th(nm, (stmt or {}).get(nm, PROPS[key]))
    if COROLLARY[0] not in drop:
        th(COROLLARY[0], (stmt or {}).get(COROLLARY[0], corollary_statement()[2:]))
    parts.append(extra)
    parts.append('end %s\nend OIBridge\n' % NAMESPACE)
    return ''.join(parts)


def _note(label):
    parts = ['# result\n\n**Outcome:** `%s`\n\n' % label, '> ' + SENTENCES[label] + '\n\n']
    parts.append('> **' + MENTION + ' — the result note.**\n'
                 + '\n'.join('> ' + l for l in CLAUSE.split('\n')) + '\n\n')
    parts.append(' '.join('`%s`' % nm for nm, _ in REQUIRED[label]) + '\n')
    if label != UNDECIDED:
        parts.append(' '.join('`%s`' % e['entry'] for e in LEDGER) + '\n')
    return ''.join(parts)


def _synthetic_d():
    road = ('| **P0** | q | x | Act 25 a.' + P0_STALE + ' b. Act 26 c.' + P0_STALE + ' d. '
            + P0_ADMITS + ' ' + P0_STANDING + ' | y |\n')
    guard = '# guard\n' + ''.join('\n#%d\n%s\n' % (i, e['old']) for i, e in enumerate(LEDGER))
    cen = json.dumps({'families': [{'name': 'x', 'modules': ['X'], 'status': 'kernel-only',
                                    'manuscript': [], 'note': 'n'}]},
                     indent=2, ensure_ascii=False) + '\n'
    return {ROADMAP: road, CENSUS: cen, ROOT: 'import A\n' + WIRE_AFTER + 'import B\n', GUARD: guard}


def _synthetic_e(fd, label):
    fe = {MODULE: _module(label), RDIR + 'result.md': _note(label),
          ROADMAP: expected_roadmap(fd[ROADMAP], label), GUARD: expected_guard(fd[GUARD], label)}
    c = json.loads(fd[CENSUS])
    c['families'].append({'name': 'act 32', 'modules': CENSUS_MODULES,
                          'status': 'kernel-only', 'manuscript': [],
                          'note': 'Outcome: ' + label + '.'})
    fe[CENSUS] = json.dumps(c, indent=2, ensure_ascii=False) + '\n'
    fe[ROOT] = fd[ROOT].replace(WIRE_AFTER, WIRE_AFTER + WIRE, 1)
    return fe, expected_paths(label)


def self_test():
    bad = []
    here = os.path.dirname(os.path.abspath(__file__))
    pre = os.path.join(here, 'preregistration.md')
    if not os.path.exists(pre):
        bad.append('agreement: preregistration.md not beside controls.py')
    else:
        text = open(pre, encoding='utf-8').read()
        q, n = qnorm(text), norm(text)
        for k, v in PROPS.items():
            if norm(v) not in n:
                bad.append('agreement: proposition %s not in the preregistration' % k)
        for k, v in list(SENTENCES.items()) + [('clause', CLAUSE), ('standing', P0_STANDING),
                                               ('admits', P0_ADMITS), ('stale', P0_STALE),
                                               ('standing-32', P0_STANDING_32)] + list(P0_CASE.items()):
            if qnorm(v) not in q:
                bad.append('agreement: %s not in the preregistration' % k)
        for b in (ROADMAP_BLOB_D, GUARD_BLOB_D, GUARD_BLOB_RETIRED, D):
            if b not in text:
                bad.append('agreement: %s not in the preregistration' % b)
        for e in LEDGER:
            if e['entry'] not in text or e['old_sha256'] not in text or e['new_sha256'] not in text:
                bad.append('agreement: ledger entry %s not in the preregistration' % e['entry'])
    for a, x in SENTENCES.items():
        for b, y in SENTENCES.items():
            if a != b and qnorm(x) in qnorm(y):
                bad.append('distinctness: the sentence of %s lies inside that of %s' % (a, b))
    # the duality and the single source hold of the frozen texts, and fail when either is altered
    if duality_ok(PROPS, COMPONENTS):
        bad.append('duality: the frozen texts fail: %s' % duality_ok(PROPS, COMPONENTS))
    dmuts = 0
    for nm, key, old, new in (
            ('P_R-existential', 'P_R', '  ∀ φ :', '  ∃ φ :'),
            ('P_N-negation-dropped', 'P_N', '∧ ¬ (∃ π τ', '∧ (∃ π τ'),
            ('P_N-conjugate-shape-unstarred', 'P_N', 'Matrix.of fun j k => star ((G (π i)).submatrix τ τ j k)',
             'Matrix.of fun j k => ((G (π i)).submatrix τ τ j k)'),
            ('P_R-distance-conjunct-dropped', 'P_R', '∧ (∀ G H, RealizableGram', '∧ True ∧ (∀ G H, RealizableGram'),
            ('S_SEP-four-shape-drift', 'S_SEP', '(fun i => (G (π i)).submatrix τ τ)', '(fun i => (G i).submatrix τ τ)'),
            ('S_ISO-witness-drift', 'S_ISO', 'GramPhaseEquiv (φ G) G)', 'True)'),
            ('S_QUARTER-existence-dropped', 'S_QUARTER', '  (∃ φ :', '  (∀ φ :'),
            ('S_QUARTER-distance-drift', 'S_QUARTER', '→\n    ¬ (∀ G H,', '→\n    ¬ (∀ H G,')):
        props = dict(PROPS)
        if props[key].count(old) < 1:
            bad.append('duality mutation %s: pattern absent' % nm)
            continue
        props[key] = props[key].replace(old, new, 1)
        dmuts += 1
        if not duality_ok(props, COMPONENTS):
            bad.append('duality mutation %s: accepted' % nm)
    comps = dict(COMPONENTS, FOUR=COMPONENTS['FOUR'].replace('submatrix τ τ', 'submatrix τ π', 1))
    dmuts += 1
    if not duality_ok(PROPS, comps):
        bad.append('duality mutation component-drift: accepted')

    fd = _synthetic_d()
    for label in ROWS:
        fe, delta = _synthetic_e(fd, label)
        r = check_all(fd, fe, delta)
        if r:
            bad.append('positive %s: %s' % (label, r))
    RG, NR, X = ROWS
    muts = []

    def mut(name, label, fn, want):
        fe, delta = _synthetic_e(fd, label)
        fe, delta = fn(dict(fe), dict(delta))
        r = check_all(fd, fe, delta)
        muts.append(name)
        if not any(x.startswith(want) for x in r):
            bad.append('mutation %s: expected %s, got %s' % (name, want, r))

    def modstmt(label, nm, s):
        return lambda fe, dl: (dict(fe, **{MODULE: _module(label, stmt={nm: s})}), dl)
    E_ = 'end ' + NAMESPACE
    mut('definition-added', NR, lambda fe, dl: (dict(fe, **{MODULE: fe[MODULE].replace(
        E_, 'noncomputable def zz := 1\n' + E_)}), dl), 'module:forbidden-command')
    mut('variable-added', NR, lambda fe, dl: (dict(fe, **{MODULE: fe[MODULE].replace(
        '\ntheorem a32_shared_x', '\nvariable (h : False)\ntheorem a32_shared_x')}), dl),
        'module:forbidden-command')
    mut('include-added', NR, lambda fe, dl: (dict(fe, **{MODULE: fe[MODULE].replace(
        '\ntheorem a32_shared_x', '\ninclude h\ntheorem a32_shared_x')}), dl), 'module:forbidden-command')
    mut('second-open', NR, lambda fe, dl: (dict(fe, **{MODULE: fe[MODULE].replace(
        '\ntheorem a32_shared_x', '\nopen Classical in\ntheorem a32_shared_x')}), dl), 'module:open')
    mut('second-import', NR, lambda fe, dl: (dict(fe, **{MODULE: fe[MODULE].replace(
        '/-! synthetic -/', 'import Mathlib\n/-! synthetic -/')}), dl), 'module:forbidden-command')
    mut('sorry', NR, lambda fe, dl: (dict(fe, **{MODULE: fe[MODULE].replace('exact test', 'sorry', 1)}), dl),
        'module:forbidden-token')
    mut('native-decide', NR, lambda fe, dl: (dict(fe, **{MODULE: fe[MODULE].replace('exact test', 'native_decide', 1)}), dl),
        'module:forbidden-token')
    mut('print-axioms-dropped', NR, lambda fe, dl: (dict(fe, **{MODULE: fe[MODULE].replace(
        '#print axioms a32_not_rigid\n', '')}), dl), 'module:no-print-axioms')
    mut('stray-theorem-name', NR, lambda fe, dl: (dict(fe, **{MODULE: fe[MODULE].replace(
        E_, 'theorem a32_n : True := trivial\n#print axioms a32_n\n' + E_)}), dl),
        'module:theorem-name-outside')
    mut('not-rigid-witness-class-fixed', NR, modstmt(NR, 'a32_not_rigid', PROPS['P_N'].replace(
        '∧ ¬ (∃ π τ', '∧ ¬ (∀ π τ', 1)), 'module:statement-not-frozen:a32_not_rigid')
    mut('rigid-hypothesis-dropped', RG, modstmt(RG, 'a32_rigid', PROPS['P_R'].replace(
        '∧ (∀ G H, RealizableGram', '∧ True ∧ (∀ G H, RealizableGram', 1)),
        'module:statement-not-frozen:a32_rigid')
    mut('separation-weakened', NR, modstmt(NR, 'a32_shared_separation', PROPS['S_SEP'].replace(
        '¬ (∃ π τ', '¬ (∀ π τ', 1)), 'module:statement-not-frozen:a32_shared_separation')
    mut('existence-altered', NR, modstmt(NR, 'a32_shared_exists', PROPS['S_EXIST'].replace(
        '∃ φ :', '∀ φ :', 1)), 'module:statement-not-frozen:a32_shared_exists')
    mut('quarter-vacuous', NR, modstmt(NR, 'a32_control_quarter', PROPS['S_QUARTER'].replace(
        '  (∃ φ :', '  (∀ φ :', 1)), 'module:statement-not-frozen:a32_control_quarter')
    mut('overlap-conclusion-dropped', NR, modstmt(NR, 'a32_control_overlap', PROPS['S_OVL'].rsplit('→', 1)[0]
        + '→ True'), 'module:statement-not-frozen:a32_control_overlap')
    for nm, _ in REQUIRED[NR]:
        mut('required-absent:' + nm, NR, lambda fe, dl, nm=nm: (dict(fe, **{MODULE: _module(NR, drop=(nm,))}), dl),
            'module:required-statement-absent:' + nm)
    for nm, _ in REQUIRED[RG]:
        mut('required-absent-rigid:' + nm, RG, lambda fe, dl, nm=nm: (dict(fe, **{MODULE: _module(RG, drop=(nm,))}), dl),
            'module:required-statement-absent:' + nm)
    mut('corollary-absent', X, lambda fe, dl: (dict(fe, **{MODULE: _module(X, drop=('a32_c_exclusive',))}), dl),
        'module:required-corollary-absent')
    mut('corollary-altered', X, lambda fe, dl: (dict(fe, **{MODULE: _module(
        X, stmt={'a32_c_exclusive': corollary_statement()[2:].replace('→ ¬ (', '→ (', 1)})}), dl),
        'module:statement-not-frozen:a32_c_exclusive')
    mut('both-labels', NR, lambda fe, dl: (dict(fe, **{MODULE: fe[MODULE].replace(
        E_, 'theorem a32_rigid :\n    ' + PROPS['P_R'] + ' := by\n  exact test\n'
        '#print axioms a32_rigid\n' + E_)}), dl), 'module:both-labels')
    mut('note-outcome-mismatch', NR, lambda fe, dl: (dict(fe, **{RDIR + 'result.md': fe[RDIR + 'result.md'].replace(
        '**Outcome:** `A32-NOT-RIGID`', '**Outcome:** `A32-RIGID`')}), dl), 'note:outcome-line')
    mut('note-second-outcome', NR, lambda fe, dl: (dict(fe, **{RDIR + 'result.md': fe[RDIR + 'result.md']
        + '\n**Outcome:** `A32-NOT-RIGID`\n'}), dl), 'note:outcome-line')
    mut('note-sentence-altered', NR, lambda fe, dl: (dict(fe, **{RDIR + 'result.md': fe[RDIR + 'result.md'].replace(
        'evidence level 2', 'evidence level 3', 1)}), dl), 'note:frozen-sentence')
    mut('note-unearned-sentence', X, lambda fe, dl: (dict(fe, **{RDIR + 'result.md': fe[RDIR + 'result.md']
        + '\n' + SENTENCES['A32-RIGID'] + '\n'}), dl), 'note:sentence-of-a-label-not-earned')
    mut('note-clause-twice', NR, lambda fe, dl: (dict(fe, **{RDIR + 'result.md': fe[RDIR + 'result.md']
        + '\n' + CLAUSE + '\n'}), dl), 'note:the-clause')
    mut('note-clause-detached', NR, lambda fe, dl: (dict(fe, **{RDIR + 'result.md': fe[RDIR + 'result.md'].replace(
        ' — the result note.**\n', ' — the result note.**\n' + 'x ' * 60 + '\n', 1)}), dl), 'note:the-clause')
    mut('note-control-unnamed', NR, lambda fe, dl: (dict(fe, **{RDIR + 'result.md': fe[RDIR + 'result.md'].replace(
        '`a32_control_quarter`', 'x')}), dl), 'note:required-statement-not-named')
    mut('note-ledger-entry-unnamed', RG, lambda fe, dl: (dict(fe, **{RDIR + 'result.md': fe[RDIR + 'result.md'].replace(
        '`' + LEDGER[0]['entry'] + '`', 'x')}), dl), 'note:ledger-entry-not-named')
    mut('roadmap-wrong-case', NR, lambda fe, dl: (dict(fe, **{ROADMAP: expected_roadmap(fd[ROADMAP], RG)}), dl),
        'roadmap:')
    mut('roadmap-stale-clause-kept', NR, lambda fe, dl: (dict(fe, **{ROADMAP: fe[ROADMAP].replace(
        ' Act 26 c.', ' Act 26 c.' + P0_STALE, 1)}), dl), 'roadmap:')
    mut('roadmap-standing-dropped', NR, lambda fe, dl: (dict(fe, **{ROADMAP: fe[ROADMAP].replace(
        P0_CASE[NR] + ' ' + P0_STANDING_32, P0_CASE[NR])}), dl), 'roadmap:')
    mut('roadmap-touched-when-undecided', X, lambda fe, dl: (dict(fe, **{ROADMAP: expected_roadmap(fd[ROADMAP], NR)}),
        dict(dl, **{ROADMAP: 'M'})), 'roadmap:')
    mut('guard-one-byte', NR, lambda fe, dl: (dict(fe, **{GUARD: fe[GUARD] + ' '}), dl), 'guard:')
    mut('guard-untouched-when-decided', RG, lambda fe, dl: (dict(fe, **{GUARD: fd[GUARD]}),
        dict((k, v) for k, v in dl.items() if k != GUARD)), 'guard:')
    mut('guard-retired-when-undecided', X, lambda fe, dl: (dict(fe, **{GUARD: retired_guard(fd[GUARD])}),
        dict(dl, **{GUARD: 'M'})), 'guard:')
    mut('guard-one-leg-restored', NR, lambda fe, dl: (dict(fe, **{GUARD: fe[GUARD].replace(
        '#1\n' + LEDGER[1]['new'], '#1\n' + LEDGER[1]['old'], 1)}), dl), 'guard:')
    mut('census-status-promoted', NR, lambda fe, dl: (dict(fe, **{CENSUS: fe[CENSUS].replace(
        '"status": "kernel-only",\n      "manuscript": [],\n      "note": "Outcome',
        '"status": "manuscript-cited",\n      "manuscript": [],\n      "note": "Outcome')}), dl),
        'census:family-disposition')
    mut('census-other-entry-changed', NR, lambda fe, dl: (dict(fe, **{CENSUS: fe[CENSUS].replace(
        '"note": "n"', '"note": "m"')}), dl), 'census:another-entry-changed')
    mut('census-outcome-wrong', NR, lambda fe, dl: (dict(fe, **{CENSUS: fe[CENSUS].replace(
        'A32-NOT-RIGID.', 'A32-RIGID.')}), dl), 'census:outcome')
    mut('census-entry-absent', NR, lambda fe, dl: (dict(fe, **{CENSUS: fd[CENSUS]}), dl), 'census:family-count-or-place')
    mut('wire-absent', NR, lambda fe, dl: (dict(fe, **{ROOT: fd[ROOT]}), dl), 'wire:')
    mut('wire-misplaced', NR, lambda fe, dl: (dict(fe, **{ROOT: fd[ROOT] + WIRE}), dl), 'wire:')
    mut('path-extra', NR, lambda fe, dl: (fe, dict(dl, **{'papers/SM.md': 'M'})), 'paths:')
    mut('path-missing-note', NR, lambda fe, dl: (fe, dict((k, v) for k, v in dl.items()
                                                         if k != RDIR + 'result.md')), 'paths:')
    mut('guard-removed-binding-referenced', NR, lambda fe, dl: (dict(fe, **{GUARD: fe[GUARD] + '\nprint(_OGCROAD)\n'}), dl),
        'ledger:removed-binding-still-referenced')
    # a tampered ledger entry does not apply
    saved = [dict(e) for e in LEDGER]
    LEDGER[0] = dict(LEDGER[0], old=LEDGER[0]['old'] + ' ')
    if retired_guard(fd[GUARD]) is not None:
        bad.append('mutation ledger-tampered: accepted')
    LEDGER[:] = saved
    muts.append('ledger-tampered')
    return bad, len(ROWS), dmuts, len(muts)


def main():
    if sys.argv[1:] == ['--self-test']:
        bad, rows, dmuts, muts = self_test()
        for b in bad:
            print('  FAIL', b)
        if bad:
            print('controls: self-test FAILED')
            return 1
        print('controls: the two verdict propositions are duals and every shared text has one source; '
              '%d duality mutations fail as required' % dmuts)
        print('controls: %d rows hold as frozen, %d mutation controls fail as required' % (rows, muts))
        print('controls: self-test OK')
        return 0
    if len(sys.argv) == 3 and sys.argv[1] == 'check':
        f = cmd_check(sys.argv[2])
        for x in f:
            print('  FAIL', x)
        print('controls: check %s' % ('FAILED' if f else 'OK'))
        return 1 if f else 0
    print(__doc__)
    return 2


if __name__ == '__main__':
    sys.exit(main())
