"""Track B act 30 -- the round's own static controls, frozen with the control plane.

Written before F; its blob is frozen in the preregistration beside it, and the execution adds it
with that exact blob. It reads nothing but the repository at D and at the commit under check, and
it certifies nothing on its own: the Lean kernel, the axiom audit and the release gate establish
the mathematics, and the V3 verifier the protocol. What it checks is that the execution carries
the frozen statements, the frozen outcome grammar and the frozen surface edits, and nothing else.

    python3 controls.py --self-test     the mutation controls, on synthetic inputs, and the
                                        agreement of the constants below with the preregistration
    python3 controls.py check <commit>  every control against the tree at <commit>, read from git

Exit 1 on any failure.
"""
import hashlib
import json
import os
import re
import subprocess
import sys

D = '48450428f528fe489d454458e21c9394aef6a02f'
RDIR = 'verification/programmes/oi-qm/track-b/act-30-product-strict-lift/'
MODULE = 'verification/lean-mathlib/OIBridge/ProductStrictLift.lean'
ROOT = 'verification/lean-mathlib/OIBridge.lean'
GUARD = 'verification/lean/edge_rigidity_probe.py'
CENSUS = 'verification/lean-manuscript-census.json'
ROADMAP = 'verification/ROADMAP.md'
RECEIPT = 'verification/receipts/A30.json'
GUARD_BLOB_D = '@@GUARD_BLOB_D@@'
GUARD_BLOB_RETIRED = '@@GUARD_BLOB_RETIRED@@'
ROADMAP_BLOB_D = '@@ROADMAP_BLOB_D@@'

IMPORT = 'import OIBridge.ProductAdmission\n'
WIRE_AFTER = 'import OIBridge.ProductAdmission\n'
WIRE = 'import OIBridge.ProductStrictLift\n'
OPEN = @@OPEN@@

# ---- the four frozen propositions, verbatim
PROPS = @@PROPS@@

# ---- the label theorems: (target, label, theorem name, statement form)
LABELS = (
    ('A30-S', 'A30-S-HOLD', 'a30_s_strictify', 'P_S', '+'),
    ('A30-S', 'A30-S-FAILS', 'a30_s_fails', 'P_S', '-'),
    ('A30-T', 'A30-T-HOLD', 'a30_t_transfer', 'P_T', '+'),
    ('A30-T', 'A30-T-FAILS', 'a30_t_fails', 'P_T', '-'),
    ('A30-N', 'A30-N-LIFTS', 'a30_n_lifts', 'P_N', '+'),
    ('A30-N', 'A30-N-NO-LIFT', 'a30_n_no_lift', 'P_N', '-'),
    ('A30-0', 'A30-0-ADMITS', 'a30_0_admits', 'P_0', '+'),
    ('A30-0', 'A30-0-RESTRICTS', 'a30_0_restricts', 'P_0', '-'),
)
UNDECIDED = {'A30-S': 'A30-S-UNDECIDED', 'A30-T': 'A30-T-UNDECIDED',
             'A30-N': 'A30-N-UNDECIDED', 'A30-0': 'A30-0-UNDECIDED'}
# ---- the corollary theorems: name -> (premises, conclusion)
COROLLARIES = {
    'a30_c_lift': (('P_S', 'P_T'), 'P_N'),
    'a30_c_admit': (('P_N',), 'P_0'),
    'a30_c_restrict': (('P_0',), 'P_N'),
}
SHARED = re.compile(r'a30_shared_[A-Za-z0-9_]+\Z')

# ---- the twenty-five rows of the frozen outcome-vector table
_S = ('A30-S-HOLD', 'A30-S-FAILS', 'A30-S-UNDECIDED')
_T = ('A30-T-HOLD', 'A30-T-FAILS', 'A30-T-UNDECIDED')
_N = ('A30-N-LIFTS', 'A30-N-NO-LIFT', 'A30-N-UNDECIDED')
_ZERO = {'A30-N-LIFTS': 'A30-0-ADMITS', 'A30-N-NO-LIFT': 'A30-0-RESTRICTS',
         'A30-N-UNDECIDED': 'A30-0-UNDECIDED'}
ROWS = tuple((s, t, n, _ZERO[n]) for s in _S for t in _T for n in _N
             if not (s == 'A30-S-HOLD' and t == 'A30-T-HOLD' and n != 'A30-N-LIFTS'))
assert len(ROWS) == 25


def row_text(v):
    return ' · '.join('`%s`' % x for x in v)


VECTOR_RE = re.compile(r'A30-S-(?:HOLD|FAILS|UNDECIDED)`? · `?A30-T-(?:HOLD|FAILS|UNDECIDED)`? · '
                       r'`?A30-N-(?:LIFTS|NO-LIFT|UNDECIDED)`? · `?A30-0-(?:ADMITS|RESTRICTS|UNDECIDED)')

# ---- the frozen post-round sentences, one per label
SENTENCES = @@SENTENCES@@

# the clause's body; its heading names the artifact carrying it
CLAUSE = @@CLAUSE@@
MENTION = 'THE CLAUSE, carried at this mention'
WATCH = @@WATCH@@

# ---- the P0 cell
P0_PFR = @@P0_PFR@@
P0_PRA = @@P0_PRA@@
P0_STANDING = @@P0_STANDING@@
P0_ADMITS = @@P0_ADMITS@@
P0_RESTRICTS = @@P0_RESTRICTS@@

# ---- the guard-retirement ledger: exact splices of the guard at D, applied on a decided A30-0
LEDGER = @@LEDGER@@

CENSUS_MODULES = ['ProductStrictLift']

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
    """Normalization for prose that may sit in a blockquote."""
    return ' '.join(re.sub(r'(?m)^[ \t]*>[ \t]?', '', t).split())


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


def theorems(code):
    """name -> statement text (between the name and the first ':='), from comment-free source."""
    out = {}
    for m in re.finditer(r'(?m)^[ \t]*(?:@\[[^\]\n]*\][ \t]*)?(?:private[ \t]+|protected[ \t]+)?'
                         r'(?:theorem|lemma)[ \t]+(\S+)', code):
        nm = m.group(1)
        rest = code[m.end():]
        j = rest.find(':=')
        st = rest if j < 0 else rest[:j]
        if nm in out:
            out[nm] = None
        else:
            out[nm] = st
    return out


def target_statement(key, sign):
    return norm(': ' + (PROPS[key] if sign == '+' else '¬ (' + PROPS[key] + ')'))


def corollary_statement(name):
    prem, concl = COROLLARIES[name]
    return norm(': ' + ' → '.join('(' + PROPS[p] + ')' for p in prem + (concl,)))


# ---- the module -------------------------------------------------------------------------------
def module_labels(src):
    """Check the module and read the labels it earns. Returns (vector or None, failures)."""
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
    if 'namespace OIBridge\nnamespace ProductStrictLift\n' not in code or \
            not code.rstrip().endswith('end ProductStrictLift\nend OIBridge'):
        f.append('module:namespace')
    th = theorems(code)
    if any(v is None for v in th.values()):
        f.append('module:theorem-declared-twice')
    if opens and th:
        first = min(m.start() for m in re.finditer(r'(?m)^[ \t]*(?:@\[[^\]\n]*\][ \t]*)?'
                                                   r'(?:private[ \t]+|protected[ \t]+)?'
                                                   r'(?:theorem|lemma)\b', code))
        if first < opens[0]:
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
    names = {x[2] for x in LABELS} | set(COROLLARIES)
    for nm in th:
        if nm not in names and not SHARED.match(nm):
            f.append('module:theorem-name-outside-the-frozen-set:' + nm)
    earned = {}
    for tgt, lab, nm, key, sign in LABELS:
        if nm in th and th[nm] is not None:
            if norm(th[nm]) != target_statement(key, sign):
                f.append('module:statement-not-frozen:' + nm)
            earned.setdefault(tgt, []).append(lab)
    vec = []
    for tgt in ('A30-S', 'A30-T', 'A30-N', 'A30-0'):
        ls = earned.get(tgt, [])
        if len(ls) > 1:
            f.append('module:both-labels:' + tgt)
            return None, f
        vec.append(ls[0] if ls else UNDECIDED[tgt])
    vec = tuple(vec)
    for nm in COROLLARIES:
        if nm in th and th[nm] is not None and norm(th[nm]) != corollary_statement(nm):
            f.append('module:statement-not-frozen:' + nm)
    for nm in ('a30_c_admit', 'a30_c_restrict'):
        if nm not in th:
            f.append('module:required-corollary-absent:' + nm)
    if vec[0] == 'A30-S-HOLD' and vec[1] == 'A30-T-HOLD' and 'a30_c_lift' not in th:
        f.append('module:required-corollary-absent:a30_c_lift')
    if vec not in ROWS:
        f.append('module:vector-off-table:' + ' · '.join(vec))
    return vec, f


# ---- the result note ---------------------------------------------------------------------------
def note_ok(note, vec):
    f = []
    found = VECTOR_RE.findall(note)
    if len(found) != 1:
        f.append('note:vector-occurrences:%d' % len(found))
    if note.count(row_text(vec)) != 1:
        f.append('note:vector-row-not-carried-once')
    q = qnorm(note)
    for lab in vec:
        if q.count(qnorm(SENTENCES[lab])) != 1:
            f.append('note:frozen-sentence:' + lab)
    for lab in SENTENCES:
        if lab not in vec and qnorm(SENTENCES[lab]) in q:
            f.append('note:sentence-of-a-label-not-earned:' + lab)
    body = qnorm(CLAUSE)
    if note.count(MENTION) != 1 or q.count(body) != 1 or \
            not 0 <= q.index(body) - q.index(MENTION) <= 80:
        f.append('note:the-clause')
    if q.count(qnorm(WATCH)) != 1:
        f.append('note:assumption-watch')
    if vec[3] != 'A30-0-UNDECIDED':
        for e in LEDGER:
            if '`%s`' % e['id'] not in note:
                f.append('note:replaced-leg-not-listed:' + e['id'])
    return f


# ---- the surfaces ------------------------------------------------------------------------------
def expected_roadmap(road_d, vec):
    if vec[3] == 'A30-0-UNDECIDED':
        return road_d
    old = ' ' + P0_PFR + ' ' + P0_STANDING + ' ' + P0_PRA + ' ' + P0_STANDING + ' |'
    new = ' ' + (P0_ADMITS if vec[3] == 'A30-0-ADMITS' else P0_RESTRICTS) + ' ' + P0_STANDING + ' |'
    if road_d.count(old) != 1:
        return None
    return road_d.replace(old, new, 1)


def retired_guard(guard_d):
    out = guard_d
    for e in LEDGER:
        if hashlib.sha256(e['old'].encode()).hexdigest() != e['old_sha256'] or \
                hashlib.sha256(e['new'].encode()).hexdigest() != e['new_sha256'] or \
                guard_d.count(e['old']) != 1 or out.count(e['old']) != 1:
            return None
        out = out.replace(e['old'], e['new'], 1)
    return out


def expected_guard(guard_d, vec):
    return guard_d if vec[3] == 'A30-0-UNDECIDED' else retired_guard(guard_d)


def census_ok(cen_d, cen_e, vec):
    f = []
    try:
        d, e = json.loads(cen_d), json.loads(cen_e)
    except ValueError:
        return ['census:not-json']
    if cen_e != json.dumps(e, indent=2, ensure_ascii=False) + '\n':
        f.append('census:not-in-the-registry-format')
    fams = e.get('families', [])
    mine = [x for x in fams if 'ProductStrictLift' in x.get('modules', [])]
    if len(mine) != 1 or fams[-1:] != mine:
        return f + ['census:family-count-or-place']
    m = mine[0]
    if m.get('modules') != CENSUS_MODULES or m.get('status') != 'kernel-only' or \
            m.get('manuscript') != []:
        f.append('census:family-disposition')
    note = m.get('note', '')
    bare = ' · '.join(vec)
    if note.count(bare) != 1 or len(VECTOR_RE.findall(note)) != 1:
        f.append('census:vector')
    rest = dict(e, families=fams[:-1])
    if rest != d:
        f.append('census:another-entry-changed')
    return f


def wire_ok(root_d, root_e):
    if root_d.count(WIRE_AFTER) != 1:
        return ['wire:anchor']
    return [] if root_e == root_d.replace(WIRE_AFTER, WIRE_AFTER + WIRE, 1) else ['wire:root']


def expected_paths(vec):
    p = {RDIR + 'preregistration.md': 'A', RDIR + 'controls.py': 'A', RDIR + 'result.md': 'A',
         MODULE: 'A', ROOT: 'M', CENSUS: 'M'}
    if vec[3] != 'A30-0-UNDECIDED':
        p[GUARD] = 'M'
        p[ROADMAP] = 'M'
    return p


def check_all(files_d, files_e, delta, vec_expected=None):
    """files_*: path -> text. delta: path -> status letter, D to the commit under check."""
    vec, f = module_labels(files_e.get(MODULE, ''))
    if vec is None:
        return f
    f += note_ok(files_e.get(RDIR + 'result.md', ''), vec)
    road = expected_roadmap(files_d[ROADMAP], vec)
    if road is None or files_e.get(ROADMAP) != road:
        f.append('roadmap:not-as-frozen-for-the-case')
    g = expected_guard(files_d[GUARD], vec)
    if g is None or files_e.get(GUARD) != g:
        f.append('guard:not-as-frozen-for-the-case')
    f += census_ok(files_d[CENSUS], files_e.get(CENSUS, ''), vec)
    f += wire_ok(files_d[ROOT], files_e.get(ROOT, ''))
    if delta != expected_paths(vec):
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
        try:
            fd[p] = git('show', '%s:%s' % (D, p)).decode('utf-8')
        except subprocess.CalledProcessError:
            pass
        try:
            fe[p] = git('show', '%s:%s' % (commit, p)).decode('utf-8')
        except subprocess.CalledProcessError:
            pass
    f = []
    if blob_id(fd[GUARD]) != GUARD_BLOB_D or blob_id(fd[ROADMAP]) != ROADMAP_BLOB_D:
        f.append('base:D-is-not-the-frozen-base')
    rg = retired_guard(fd[GUARD])
    if rg is None or blob_id(rg) != GUARD_BLOB_RETIRED:
        f.append('ledger:does-not-reproduce-the-frozen-retired-guard')
    delta = {}
    for ln in git('diff', '--no-renames', '--name-status', D, commit).decode().splitlines():
        st, p = ln.split('\t', 1)
        delta[p] = st
    f += check_all(fd, fe, delta)
    vec, _ = module_labels(fe.get(MODULE, ''))
    print('controls: vector read off the module:', ' · '.join(vec) if vec else '(none)')
    print('controls: %d path(s) changed from D' % len(delta))
    return f


# ---- the self-test -----------------------------------------------------------------------------
def _module(vec, extra='', drop=(), stmt=None):
    lines = [IMPORT, '/-! synthetic -/\n', 'namespace OIBridge\nnamespace ProductStrictLift\n\n',
             OPEN, '\n', 'theorem a30_shared_x : True := trivial\n#print axioms a30_shared_x\n\n']
    for tgt, lab, nm, key, sign in LABELS:
        if lab in vec and nm not in drop:
            s = (stmt or {}).get(nm, PROPS[key] if sign == '+' else '¬ (' + PROPS[key] + ')')
            lines.append('theorem %s :\n    %s := by\n  exact test\n#print axioms %s\n\n' % (nm, s, nm))
    for nm, (prem, concl) in COROLLARIES.items():
        if nm in drop:
            continue
        s = ' → '.join('(' + PROPS[p] + ')' for p in prem + (concl,))
        lines.append('theorem %s :\n    %s := by\n  exact test\n#print axioms %s\n\n' % (nm, s, nm))
    lines.append(extra)
    lines.append('end ProductStrictLift\nend OIBridge\n')
    return ''.join(lines)


def _note(vec):
    parts = ['# result\n\n| vector |\n|---|\n| ' + row_text(vec) + ' |\n\n']
    for lab in vec:
        parts.append('### `%s`\n\n> %s\n\n' % (lab, SENTENCES[lab]))
    parts.append('> **' + MENTION + ' — the result note.**\n' + '\n'.join('> ' + l for l in CLAUSE.split('\n')) + '\n\n' + WATCH + '\n\n')
    if vec[3] != 'A30-0-UNDECIDED':
        parts.append(' '.join('`%s`' % e['id'] for e in LEDGER) + '\n')
    return ''.join(parts)


def _synthetic_d():
    guard = '# guard\n' + ''.join('\n#%d\n%s\n' % (i, e['old']) for i, e in enumerate(LEDGER))
    road = ('| **P0** | q | x | a sentence. ' + P0_PFR + ' ' + P0_STANDING + ' ' + P0_PRA + ' '
            + P0_STANDING + ' | y |\n')
    cen = json.dumps({'families': [{'name': 'x', 'modules': ['X'], 'status': 'kernel-only',
                                    'manuscript': [], 'note': 'n'}]},
                     indent=2, ensure_ascii=False) + '\n'
    root = 'import A\n' + WIRE_AFTER + 'import B\n'
    return {GUARD: guard, ROADMAP: road, CENSUS: cen, ROOT: root}


def _synthetic_e(fd, vec):
    fe = {MODULE: _module(vec), RDIR + 'result.md': _note(vec)}
    fe[ROADMAP] = expected_roadmap(fd[ROADMAP], vec)
    fe[GUARD] = expected_guard(fd[GUARD], vec)
    c = json.loads(fd[CENSUS])
    c['families'].append({'name': 'act 30', 'modules': ['ProductStrictLift'],
                          'status': 'kernel-only', 'manuscript': [],
                          'note': 'Outcome vector: ' + ' · '.join(vec) + '.'})
    fe[CENSUS] = json.dumps(c, indent=2, ensure_ascii=False) + '\n'
    fe[ROOT] = fd[ROOT].replace(WIRE_AFTER, WIRE_AFTER + WIRE, 1)
    return fe, expected_paths(vec)


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
            if n.count(norm(v)) < 1:
                bad.append('agreement: proposition %s not in the preregistration' % k)
        for k, v in SENTENCES.items():
            if qnorm(v) not in q:
                bad.append('agreement: sentence %s not in the preregistration' % k)
        for k, v in (('clause', CLAUSE), ('watch', WATCH), ('admits', P0_ADMITS),
                     ('restricts', P0_RESTRICTS), ('pfr', P0_PFR), ('pra', P0_PRA),
                     ('standing', P0_STANDING)):
            if qnorm(v) not in q:
                bad.append('agreement: %s not in the preregistration' % k)
        for e in LEDGER:
            if '`%s`' % e['id'] not in text or e['old_sha256'] not in text or \
                    e['new_sha256'] not in text:
                bad.append('agreement: ledger entry %s not in the preregistration' % e['id'])
        for b in (GUARD_BLOB_RETIRED, GUARD_BLOB_D, ROADMAP_BLOB_D):
            if b not in text:
                bad.append('agreement: blob %s not in the preregistration' % b)

    for a, x in SENTENCES.items():
        for b, y in SENTENCES.items():
            if a != b and qnorm(x) in qnorm(y):
                bad.append('distinctness: the sentence of %s lies inside that of %s' % (a, b))
    fd = _synthetic_d()
    # every row holds when the execution is as frozen
    for vec in ROWS:
        fe, delta = _synthetic_e(fd, vec)
        r = check_all(fd, fe, delta)
        if r:
            bad.append('positive %s: %s' % (' · '.join(vec), r))
    base = ('A30-S-HOLD', 'A30-T-HOLD', 'A30-N-LIFTS', 'A30-0-ADMITS')
    und = ('A30-S-UNDECIDED', 'A30-T-UNDECIDED', 'A30-N-UNDECIDED', 'A30-0-UNDECIDED')
    neg = ('A30-S-HOLD', 'A30-T-FAILS', 'A30-N-NO-LIFT', 'A30-0-RESTRICTS')
    muts = []

    def mut(name, vec, fn, want):
        fe, delta = _synthetic_e(fd, vec)
        fe, delta = fn(dict(fe), dict(delta))
        r = check_all(fd, fe, delta)
        muts.append(name)
        if not any(x.startswith(want) for x in r):
            bad.append('mutation %s: expected %s, got %s' % (name, want, r))

    P = PROPS
    def modstmt(nm, s):
        return lambda fe, dl: (dict(fe, **{MODULE: _module(base, stmt={nm: s})}), dl)
    mut('definition-added', base, lambda fe, dl: (dict(fe, **{MODULE: fe[MODULE].replace(
        'end ProductStrictLift', 'def zz := 1\nend ProductStrictLift')}), dl), 'module:forbidden-command')
    mut('private-noncomputable-def', base, lambda fe, dl: (dict(fe, **{MODULE: fe[MODULE].replace(
        'end ProductStrictLift', 'private noncomputable def zz := 1\nend ProductStrictLift')}), dl),
        'module:forbidden-command')
    mut('variable-added', base, lambda fe, dl: (dict(fe, **{MODULE: fe[MODULE].replace(
        '\ntheorem a30_shared_x', '\nvariable (h : False)\ntheorem a30_shared_x')}), dl),
        'module:forbidden-command')
    mut('include-added', base, lambda fe, dl: (dict(fe, **{MODULE: fe[MODULE].replace(
        '\ntheorem a30_shared_x', '\ninclude h\ntheorem a30_shared_x')}), dl),
        'module:forbidden-command')
    mut('second-open', base, lambda fe, dl: (dict(fe, **{MODULE: fe[MODULE].replace(
        '\ntheorem a30_shared_x', '\nopen Foo\ntheorem a30_shared_x')}), dl), 'module:open')
    mut('open-in', base, lambda fe, dl: (dict(fe, **{MODULE: fe[MODULE].replace(
        '\ntheorem a30_n_lifts', '\nopen Foo in\ntheorem a30_n_lifts')}), dl), 'module:open')
    mut('open-altered', base, lambda fe, dl: (dict(fe, **{MODULE: fe[MODULE].replace(
        'ProductAdmission\n\n', 'ProductAdmission Foo\n\n', 1)}), dl), 'module:open')
    mut('second-import', base, lambda fe, dl: (dict(fe, **{MODULE: fe[MODULE].replace(
        '/-! synthetic -/', 'import Mathlib\n/-! synthetic -/')}), dl), 'module:forbidden-command')
    mut('sorry', base, lambda fe, dl: (dict(fe, **{MODULE: fe[MODULE].replace(
        'exact test', 'sorry', 1)}), dl), 'module:forbidden-token')
    mut('print-axioms-dropped', base, lambda fe, dl: (dict(fe, **{MODULE: fe[MODULE].replace(
        '#print axioms a30_n_lifts\n', '')}), dl), 'module:no-print-axioms')
    mut('stray-theorem-name', base, lambda fe, dl: (dict(fe, **{MODULE: fe[MODULE].replace(
        'end ProductStrictLift', 'theorem a30_n_lifts_strict : True := trivial\n'
        '#print axioms a30_n_lifts_strict\nend ProductStrictLift')}), dl),
        'module:theorem-name-outside')
    mut('n-strict-instead-of-twisted', base,
        modstmt('a30_n_lifts', P['P_N'].replace('TwistedNatural ((0 : Fin 1), (0 : Fin 1)) αL αR Ψ',
                                                'StrictNatural ((0 : Fin 1), (0 : Fin 1)) Ψ')),
        'module:statement-not-frozen:a30_n_lifts')
    mut('0-two-existentials', base,
        modstmt('a30_0_admits', P['P_0'].replace('    ∧ (∀ t : ℕ, ∃ Ψ', '    ∧ (∃ Φ\' : ℕ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ), True) ∧ (∀ t : ℕ, ∃ Ψ', 1)),
        'module:statement-not-frozen:a30_0_admits')
    mut('s-off-realizable-clause-dropped', base,
        modstmt('a30_s_strictify', P['P_S'].replace(
            '(∀ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, ¬ RealizableGram (Fin 1 × Fin 1) (Γ 0) G → Φ₁ G = Φ₀ G)',
            'True')), 'module:statement-not-frozen:a30_s_strictify')
    mut('s-binder-added', base, lambda fe, dl: (dict(fe, **{MODULE: fe[MODULE].replace(
        'theorem a30_s_strictify :', 'theorem a30_s_strictify (h : False) :')}), dl),
        'module:statement-not-frozen:a30_s_strictify')
    mut('t-configuration-changed', base,
        modstmt('a30_t_transfer', P['P_T'].replace('(1 / 4 : ℝ)', '(1 / 2 : ℝ)')),
        'module:statement-not-frozen:a30_t_transfer')
    mut('negative-not-negated', neg, lambda fe, dl: (dict(fe, **{MODULE: _module(
        neg, stmt={'a30_n_no_lift': P['P_N']})}), dl), 'module:statement-not-frozen:a30_n_no_lift')
    mut('both-labels', base, lambda fe, dl: (dict(fe, **{MODULE: fe[MODULE].replace(
        'end ProductStrictLift', 'theorem a30_n_no_lift :\n    ¬ (' + P['P_N'] + ') := by\n  exact test\n'
        '#print axioms a30_n_no_lift\nend ProductStrictLift')}), dl), 'module:both-labels')
    mut('corollary-admit-absent', und, lambda fe, dl: (dict(fe, **{MODULE: _module(
        und, drop=('a30_c_admit',))}), dl), 'module:required-corollary-absent:a30_c_admit')
    mut('corollary-restrict-absent', und, lambda fe, dl: (dict(fe, **{MODULE: _module(
        und, drop=('a30_c_restrict',))}), dl), 'module:required-corollary-absent:a30_c_restrict')
    mut('corollary-lift-absent-when-reached', base, lambda fe, dl: (dict(fe, **{MODULE: _module(
        base, drop=('a30_c_lift',))}), dl), 'module:required-corollary-absent:a30_c_lift')
    mut('corollary-lift-altered', base, lambda fe, dl: (dict(fe, **{MODULE: fe[MODULE].replace(
        'theorem a30_c_lift :\n    (', 'theorem a30_c_lift :\n    (True) → (', 1)}), dl),
        'module:statement-not-frozen:a30_c_lift')
    mut('gate-s-t-hold-n-undecided', base, lambda fe, dl: (dict(fe, **{MODULE: _module(
        base, drop=('a30_n_lifts', 'a30_0_admits'))}), dl), 'module:vector-off-table')
    mut('gate-n-lifts-0-undecided', base, lambda fe, dl: (dict(fe, **{MODULE: _module(
        base, drop=('a30_0_admits',))}), dl), 'module:vector-off-table')
    mut('note-vector-mismatch', base, lambda fe, dl: (dict(fe, **{RDIR + 'result.md': _note(
        ('A30-S-HOLD', 'A30-T-HOLD', 'A30-N-LIFTS', 'A30-0-ADMITS')).replace(
        '`A30-S-HOLD` · `A30-T-HOLD`', '`A30-S-HOLD` · `A30-T-UNDECIDED`')}), dl),
        'note:vector-row-not-carried-once')
    mut('note-second-vector', base, lambda fe, dl: (dict(fe, **{
        RDIR + 'result.md': fe[RDIR + 'result.md'] + '\n' + row_text(und) + '\n'}), dl),
        'note:vector-occurrences')
    mut('note-sentence-altered', base, lambda fe, dl: (dict(fe, **{
        RDIR + 'result.md': fe[RDIR + 'result.md'].replace('at evidence level 2', 'at evidence level 3', 1)}), dl),
        'note:frozen-sentence')
    mut('note-unearned-sentence', und, lambda fe, dl: (dict(fe, **{
        RDIR + 'result.md': fe[RDIR + 'result.md'] + '\n' + SENTENCES['A30-N-LIFTS'] + '\n'}), dl),
        'note:sentence-of-a-label-not-earned')
    mut('note-clause-twice', base, lambda fe, dl: (dict(fe, **{
        RDIR + 'result.md': fe[RDIR + 'result.md'] + '\n' + CLAUSE + '\n'}), dl), 'note:the-clause')
    mut('note-mention-twice', base, lambda fe, dl: (dict(fe, **{
        RDIR + 'result.md': fe[RDIR + 'result.md'] + '\n' + MENTION + '\n'}), dl), 'note:the-clause')
    mut('note-clause-detached', base, lambda fe, dl: (dict(fe, **{
        RDIR + 'result.md': fe[RDIR + 'result.md'].replace(' — the result note.**\n', ' — the result note.**\n' + 'x ' * 60 + '\n', 1)}), dl),
        'note:the-clause')
    mut('note-clause-truncated', base, lambda fe, dl: (dict(fe, **{
        RDIR + 'result.md': fe[RDIR + 'result.md'].replace(CLAUSE.split('\n')[-1], '')}), dl),
        'note:the-clause')
    mut('note-watch-dropped', base, lambda fe, dl: (dict(fe, **{
        RDIR + 'result.md': fe[RDIR + 'result.md'].replace(WATCH, '')}), dl), 'note:assumption-watch')
    mut('note-legs-unlisted', base, lambda fe, dl: (dict(fe, **{
        RDIR + 'result.md': fe[RDIR + 'result.md'].replace('`pra-road-leg`', 'x')}), dl),
        'note:replaced-leg-not-listed:pra-road-leg')
    mut('roadmap-stale-pfr-kept', base, lambda fe, dl: (dict(fe, **{ROADMAP: fe[ROADMAP].replace(
        P0_ADMITS, P0_PFR + ' ' + P0_STANDING + ' ' + P0_ADMITS)}), dl), 'roadmap:')
    mut('roadmap-wrong-case', base, lambda fe, dl: (dict(fe, **{ROADMAP: fe[ROADMAP].replace(
        P0_ADMITS, P0_RESTRICTS)}), dl), 'roadmap:')
    mut('roadmap-standing-dropped', neg, lambda fe, dl: (dict(fe, **{ROADMAP: fe[ROADMAP].replace(
        ' ' + P0_STANDING + ' |', ' |')}), dl), 'roadmap:')
    mut('roadmap-touched-when-undecided', und, lambda fe, dl: (dict(fe, **{ROADMAP: expected_roadmap(
        fd[ROADMAP], base)}), dict(dl, **{ROADMAP: 'M'})), 'roadmap:')
    mut('guard-one-byte', base, lambda fe, dl: (dict(fe, **{GUARD: fe[GUARD] + ' '}), dl), 'guard:')
    mut('guard-untouched-when-decided', base, lambda fe, dl: (dict(fe, **{GUARD: fd[GUARD]}),
        dict((k, v) for k, v in dl.items() if k != GUARD)), 'guard:')
    mut('guard-retired-when-undecided', und, lambda fe, dl: (dict(fe, **{GUARD: retired_guard(
        fd[GUARD])}), dict(dl, **{GUARD: 'M'})), 'guard:')
    mut('guard-one-leg-restored', base, lambda fe, dl: (dict(fe, **{GUARD: fe[GUARD].replace(
        '#9\n', '#9\n' + LEDGER[9]['old'])}), dl), 'guard:')
    mut('census-status-promoted', base, lambda fe, dl: (dict(fe, **{CENSUS: fe[CENSUS].replace(
        '"status": "kernel-only",\n      "manuscript": [],\n      "note": "Outcome',
        '"status": "manuscript-cited",\n      "manuscript": [],\n      "note": "Outcome')}), dl),
        'census:family-disposition')
    mut('census-other-entry-changed', base, lambda fe, dl: (dict(fe, **{CENSUS: fe[CENSUS].replace(
        '"note": "n"', '"note": "m"')}), dl), 'census:another-entry-changed')
    mut('census-vector-wrong', base, lambda fe, dl: (dict(fe, **{CENSUS: fe[CENSUS].replace(
        'A30-0-ADMITS.', 'A30-0-UNDECIDED.')}), dl), 'census:vector')
    mut('census-entry-absent', base, lambda fe, dl: (dict(fe, **{CENSUS: fd[CENSUS]}), dl),
        'census:family-count-or-place')
    mut('wire-absent', base, lambda fe, dl: (dict(fe, **{ROOT: fd[ROOT]}), dl), 'wire:')
    mut('wire-misplaced', base, lambda fe, dl: (dict(fe, **{ROOT: fd[ROOT] + WIRE}), dl), 'wire:')
    mut('path-extra', base, lambda fe, dl: (fe, dict(dl, **{'papers/SM.md': 'M'})), 'paths:')
    mut('path-missing-note', base, lambda fe, dl: (fe, dict((k, v) for k, v in dl.items()
                                                           if k != RDIR + 'result.md')), 'paths:')
    # the retired guard reproduces its frozen ledger, and a tampered ledger entry does not apply
    t = [dict(e) for e in LEDGER]
    t[0]['old'] = t[0]['old'] + 'x'
    saved = list(LEDGER)
    LEDGER[:] = t
    if retired_guard(fd[GUARD]) is not None:
        bad.append('mutation ledger-tampered: the tampered ledger still applied')
    LEDGER[:] = saved
    muts.append('ledger-tampered')
    return bad, len(ROWS), len(muts)


def main():
    if sys.argv[1:] == ['--self-test']:
        bad, rows, muts = self_test()
        for b in bad:
            print('  FAIL', b)
        if bad:
            print('controls: self-test FAILED')
            return 1
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
