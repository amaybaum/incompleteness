#!/usr/bin/env python3
"""CI-compatibility correction of the r6 landing package, round 6: item 1 of the owner decision of 2026-11-25T20:42:35Z.

Reads, read only: landing5/ (the directory verification/audits/foundations/a1exit-design-r6-20261125/ at commit
a902d272, the round-5 landing tree), the layout of the round-5 recipe (out-final4/, c33/, out-final5/ with
generator-round4 as out-final5/build/, and out-final6/build/ as generator-round5), and build/inputs/ beside this
file (#1169 comment 7174085995 as read with a GET request).  Every file of landing5/ is checked against the sha256
that the round-5 manifest states for it, and the manifest against the sha256 pinned below.  generator-round5 is
executed in-process up to its report (it re-checks its own inputs, executes generator-round4 in turn and regenerates
the round-5 files, which must equal landing5/), and the self-checks of rounds 3 to 5 are re-run on the round-6
files.  Writes out-final7/.  Every change is a logged edit tagged with the item of the decision it applies (DUP:
duplicate paragraphs; GEN: generator hygiene checks; HIST: historical integrity; MAN: manifest) or `meta`.  The
generator re-runs itself in a separate process and compares every output's sha256 before writing.
"""
import ast
import collections
import hashlib
import json
import os
import re
import subprocess
import sys
import unicodedata

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
R6 = os.path.dirname(OUT)
L5 = os.path.join(R6, 'landing5')
G5 = os.path.join(R6, 'out-final6', 'build')
G4 = os.path.join(R6, 'out-final5', 'build')
INP = os.path.join(HERE, 'inputs')
DIRPATH = 'verification/audits/foundations/a1exit-design-r6-20261125'
L5_COMMIT = 'a902d272f4a865663c399fb348f960d2b2c8dce8'
R4_COMMIT = '2aec244e283fc49a85af04f2d9c3a72ec4122340'
C33_COMMIT = 'c33d5b71a3e4e15028d19ff153afcee8f5aa90a3'
MAN5_SHA = '58b471c7ade65f47f988e7e6f2ad504cd3b1484344ddc1f5b55eca4030518a63'
DEC6_ID = '7174085995'
DEC6_AT = '2026-11-25T20:42:35Z'
OD6 = 'owner decision of %s' % DEC6_AT
N_REQ, N_ROWS = 428, 558
WORD = 'scratch' + 'pad'  # built, so this file carries none of the words the added-text scan refuses
AT, TMP, HOME = chr(64), '/' + 'tmp', '/' + 'home'
# the generators corrected, each with the commit and git blob of the original used in its round
GENFIX = collections.OrderedDict([
    ('generator-round2/correct2.py', (C33_COMMIT, '809afa8448996c989879e285e6b66bb10033bd1f')),
    ('generator-round3/correct3.py', (C33_COMMIT, 'f7a8aa4be68b6b6874e819fe0d9808102da0ef0d')),
    ('generator-round4/correct4.py', (R4_COMMIT, 'c9a1c5afe8ad9443da854c71ac5362c19a529194'))])


def rdb(p):
    with open(p, 'rb') as f:
        return f.read()


def rd(p):
    return rdb(p).decode('utf-8')


def sha(b):
    if isinstance(b, str):
        b = b.encode('utf-8')
    return hashlib.sha256(b).hexdigest()


def gitblob(b):
    return hashlib.sha1(b'blob %d\0' % len(b) + b).hexdigest()


def rj(s):
    return json.loads(s, object_pairs_hook=collections.OrderedDict)


PROBLEMS = []
LOG = []


def log(dec, target, desc):
    LOG.append((dec, target, desc))


def sedit(dec, name, text, old, new, desc, count=1):
    n = text.count(old)
    if n != count:
        PROBLEMS.append('edit %s/%s: expected %d occurrence(s), found %d: %r' % (dec, name, count, n, old[:80]))
        return text
    log(dec, name, desc)
    return text.replace(old, new)


def md_row(cells):
    return '| ' + ' | '.join(str(x).replace('|', '/') for x in cells) + ' |'


def table_rows(text, head):
    a = text.index(head + '\n')
    lines = text[a:].split('\n')
    rows = []
    for ln in lines[2:]:
        if not ln.startswith('| '):
            break
        rows.append(ln)
    return a, rows


# =====================================================================================================
# inputs
# =====================================================================================================
L5FILES = collections.OrderedDict()
for dp, dn, fn in os.walk(L5):
    dn.sort()
    for f in sorted(fn):
        p = os.path.relpath(os.path.join(dp, f), L5).replace(os.sep, '/')
        L5FILES[p] = rdb(os.path.join(dp, f))
L5FILES = collections.OrderedDict(sorted(L5FILES.items()))
MAN5 = L5FILES['LANDING-MANIFEST.md'].decode('utf-8')
if sha(MAN5) != MAN5_SHA:
    PROBLEMS.append('input LANDING-MANIFEST.md: sha256 %s, expected the pin of a902d272' % sha(MAN5))
_s1a, S1ROWS5 = table_rows(MAN5, '| Path | Role | Source | sha256 |')
S1 = collections.OrderedDict()
for ln in S1ROWS5:
    c = ln[2:-2].split(' | ')
    S1[c[0]] = c
for p, b in L5FILES.items():
    if p == 'LANDING-MANIFEST.md':
        continue
    if p not in S1 or S1[p][3] != sha(b):
        PROBLEMS.append('input %s does not match the sha256 the round-5 manifest states' % p)
if set(S1) != set(L5FILES) or len(L5FILES) != 32:
    PROBLEMS.append('input tree: %d files; differs from the manifest by %s' % (len(L5FILES), sorted(set(S1) ^ set(L5FILES))))
LAYOUT = collections.OrderedDict([
    ('generator-round5/correct5.py', os.path.join(G5, 'correct5.py')),
    ('generator-round5/tree-2aec244e.json', os.path.join(G5, 'inputs', 'tree-2aec244e.json')),
    ('generator-round5/records-1169-round5.json', os.path.join(G5, 'inputs', 'records-1169-round5.json')),
    ('inputs/edits_check.py', os.path.join(G5, 'inputs', 'edits_check.py')),
    ('generator-round4/correct4.py', os.path.join(G4, 'correct4.py')),
    ('generator-round4/owner-decisions-A1-A5.json', os.path.join(G4, 'inputs', 'owner-decisions-A1-A5.json')),
    ('generator-round4/review-r6-round3.md', os.path.join(G4, 'inputs', 'review-r6-round3.md')),
    ('generator-round4/tree-c33d5b71.json', os.path.join(G4, 'inputs', 'tree-c33d5b71.json')),
    ('generator-round4/records-1169.json', os.path.join(G4, 'inputs', 'records-1169.json'))])
for p, lp in LAYOUT.items():
    if rdb(lp) != L5FILES.get(p):
        PROBLEMS.append('layout: %s differs from the landed file %s' % (os.path.relpath(lp, R6), p))
REC6_RAW = rdb(os.path.join(INP, 'records-1169-round6.json'))
REC6 = rj(REC6_RAW.decode('utf-8'))
INPUT6 = collections.OrderedDict([('build/inputs/records-1169-round6.json', sha(REC6_RAW))])
DEC6 = REC6[DEC6_ID]
DEC6_BODY, DEC6_REC_AT = DEC6['body'], DEC6['created_at']
if DEC6['user']['login'] != 'amaybaum' or list(REC6) != [DEC6_ID]:
    PROBLEMS.append('records: unexpected author or comment')
QUOTE6 = [
    'Duplicate paragraphs: Prefix each status paragraph with its requirement ID, making it unique without changing its '
    'meaning or decision basis.',
    'Generator hygiene checks: Construct the flagged string at runtime, following the round-5 approach, without changing '
    'the checks\' behavior.',
    'Historical integrity: Preserve the original generators in Git history. Clearly document that the corrected versions '
    'are functionally equivalent but not byte-identical to those used in earlier rounds.',
    'Manifest: Regenerate the affected files and update their hashes.',
    'Do not introduce checker exceptions.',
    'This is a bounded amendment to the adopted landing package, not a reopening of the A1 verification design.']
if 'Owner decision (amaybaum, %s, coordinating session), quoted in full:' % DEC6_AT not in DEC6_BODY:
    PROBLEMS.append('records: author and time line missing')
for q in QUOTE6:
    if q not in DEC6_BODY:
        PROBLEMS.append('records: quoted sentence missing: %r' % q[:60])

# =====================================================================================================
# generator-round5, executed in-process up to its report
# =====================================================================================================
SRC5 = rd(LAYOUT['generator-round5/correct5.py'])
_SEP = '\n# =====================================================================================================\n'
_c5 = SRC5.index(_SEP + '# self-checks\n')
_r5 = SRC5.index('\ndef report():')
SEG5 = SRC5[_c5:SRC5.index(_SEP + '# CORRECTION-REPORT-round5.md')]
NS5 = {'__file__': LAYOUT['generator-round5/correct5.py'], '__name__': 'correct5', '__builtins__': __builtins__}
exec(compile(SRC5[:_r5], 'correct5', 'exec'), NS5)
for p in NS5['PROBLEMS']:
    PROBLEMS.append('generator-round5: ' + p)
for p, b in NS5['LANDED5'].items():
    if b != L5FILES.get(p):
        PROBLEMS.append('generator-round5 does not reproduce %s of a902d272' % p)
if NS5['MANIFEST'] != MAN5:
    PROBLEMS.append('generator-round5 does not reproduce LANDING-MANIFEST.md of a902d272')
C5_REPRO = len(NS5['LANDED5']) + 1
D2KEY = 'D2: generator-round4 lands byte-identical to 2aec244e, generator-round5 lands, no merge caveat remains'


def rerun5(subst):
    """Re-runs generator-round5's self-check segment with the documents of `subst` in place of its own."""
    ns = dict(NS5)
    ns.update(subst)
    ns['PROBLEMS'] = [p for p in NS5['PROBLEMS'] if not p.startswith('check failed')]
    ns['LOG'] = list(NS5['LOG'])
    exec(compile(SEG5, 'correct5-checks', 'exec'), ns)
    return ns['CHK_AFTER'], ns['VAL_AFTER'], ns['OWN_AFTER'], ns['OWN5']


CHK5, VAL5, OWN4_5, OWN5_5 = NS5['CHK_AFTER'], NS5['VAL_AFTER'], NS5['OWN_AFTER'], NS5['OWN5']
_ctl = rerun5({})
RERUN_CONTROL = (_ctl[0] == CHK5 and _ctl[1] == VAL5 and _ctl[2] == OWN4_5 and _ctl[3] == OWN5_5)

# =====================================================================================================
# FRESH-AUTHORIZATION.md (DUP)
# =====================================================================================================
FRESH5 = L5FILES['FRESH-AUTHORIZATION.md'].decode('utf-8')
_s4 = FRESH5.index('\n## 4. Entries of sec. 1\n')
_STAT = re.compile(r'^### (\S+)\n\nStatus: ', re.M)
STAT_IDS = _STAT.findall(FRESH5[_s4:])
FRESH = FRESH5[:_s4] + _STAT.sub(lambda m: '### %s\n\n**%s.** Status: ' % (m.group(1), m.group(1)), FRESH5[_s4:])
for rid in STAT_IDS:
    log('DUP', 'FRESH-AUTHORIZATION.md', 'status paragraph of %s prefixed with its requirement id' % rid)
_t1a, _T1 = table_rows(FRESH5, '| Requirement | Decision basis | Class | Review\'s class (decision 1) | Status | Decision 2 class |')
T1_IDS = [ln[2:-2].split(' | ')[0] for ln in _T1]
FRESH_UNDO = FRESH
for rid in STAT_IDS:
    FRESH_UNDO = FRESH_UNDO.replace('\n**%s.** Status: ' % rid, '\nStatus: ', 1)

# =====================================================================================================
# the corrected generators (GEN, HIST)
# =====================================================================================================
OLD_T = "('%s', '%s' in c)" % (WORD, WORD)
NEW_T = '(SCR, SCR in c)'
ANCHOR = "LONG_URL = re.compile(r'https?://github\\.com/\\S{60,}')\nfor n, c in CONTENT.items():\n"
INSERT = "SCR = 'scratch' + 'pad'  # built, as generator-round5 builds it, so that this file does not carry the word\n"
ANCHOR_NEW = ANCHOR.replace('\nfor n, c', '\n' + INSERT + 'for n, c')


class _Fold(ast.NodeTransformer):
    """Maps the corrected source's tree onto the original's: drops the assignment of SCR, reads SCR as its value."""

    def visit_Module(self, node):
        node.body = [s for s in node.body if not (isinstance(s, ast.Assign) and len(s.targets) == 1 and
                                                  isinstance(s.targets[0], ast.Name) and s.targets[0].id == 'SCR')]
        self.generic_visit(node)
        return node

    def visit_Name(self, node):
        if node.id == 'SCR':
            return ast.copy_location(ast.Constant(value=WORD), node)
        return node


GEN_NEW = collections.OrderedDict()
GEN_EQ = collections.OrderedDict()
for p, (commit, blob) in GENFIX.items():
    old = L5FILES[p].decode('utf-8')
    if gitblob(L5FILES[p]) != blob:
        PROBLEMS.append('%s: landed file is not blob %s' % (p, blob[:12]))
    new = sedit('GEN', p, old, OLD_T, NEW_T, 'hygiene check: the literal word replaced by SCR')
    new = sedit('GEN', p, new, ANCHOR, ANCHOR_NEW, 'SCR built at run time before the hygiene loop')
    GEN_NEW[p] = new
    undo = new.replace(INSERT, '', 1).replace(NEW_T, OLD_T, 1)
    t_old = ast.dump(ast.parse(old))
    t_new = ast.dump(_Fold().visit(ast.parse(new)))
    GEN_EQ[p] = collections.OrderedDict([
        ('reversing the edit gives the original blob', gitblob(undo.encode('utf-8')) == blob),
        ('syntax tree equal to the original once SCR is read as its value', t_old == t_new),
        ('the word occurs nowhere in the file', WORD not in new),
        ('one assignment of SCR, two uses', new.count('SCR = ') == 1 and new.count('SCR') == 3),
        ('compiles', bool(compile(new, p, 'exec')))])
log('HIST', 'generator-round2/3/4', 'originals left in Git history: correct2.py and correct3.py at c33d5b71, correct4.py at 2aec244e')

# =====================================================================================================
# landed files of round 6
# =====================================================================================================
GEN6 = collections.OrderedDict([
    ('generator-round6/correct6.py', rdb(os.path.abspath(__file__))),
    ('generator-round6/records-1169-round6.json', REC6_RAW)])
LANDED6 = collections.OrderedDict()
for p, b in L5FILES.items():
    if p == 'LANDING-MANIFEST.md':
        continue
    if p == 'FRESH-AUTHORIZATION.md':
        LANDED6[p] = FRESH.encode('utf-8')
    elif p in GEN_NEW:
        LANDED6[p] = GEN_NEW[p].encode('utf-8')
    else:
        LANDED6[p] = b
    if p == 'generator-round5/records-1169-round5.json':
        LANDED6.update(GEN6)
CHANGED6 = ['FRESH-AUTHORIZATION.md'] + list(GEN_NEW)

# =====================================================================================================
# LANDING-MANIFEST.md (MAN, HIST)
# =====================================================================================================
M = MAN5
_q5 = 'authorized. Design adoption and merging into `main` still require separate approval."\n\n'
M = sedit('MAN', 'LANDING-MANIFEST.md', M, _q5, _q5 + (
    'Owner decision of %s (amaybaum, coordinating session; #1169 comment %s, %s), item 1, quoted: %s\n\n'
    % (DEC6_AT, DEC6_ID, DEC6_REC_AT, ' '.join('"%s"' % q for q in QUOTE6))), 'round-6 decision quoted with author and time')
M = sedit('MAN', 'LANDING-MANIFEST.md', M, 'with the round-5 outputs, the files of sec. 1 kept',
          'with the round-5 and round-6 outputs, the files of sec. 1 kept', 'landing tree: the round-6 outputs named')
SRC_TXT = collections.OrderedDict([
    ('FRESH-AUTHORIZATION.md', 'round-6 output: status paragraphs prefixed with their requirement ids (blob %s at 2aec244e)'),
    ('generator-round2/correct2.py', 'round-6 output: hygiene literal built at run time (original: blob %s at c33d5b71)'),
    ('generator-round3/correct3.py', 'round-6 output: hygiene literal built at run time (original: blob %s at c33d5b71)'),
    ('generator-round4/correct4.py', 'round-6 output: hygiene literal built at run time (original: blob %s at 2aec244e)')])
for p, fmt in SRC_TXT.items():
    c = S1[p]
    blob = GENFIX[p][1] if p in GENFIX else gitblob(L5FILES[p])
    M = sedit('MAN', 'LANDING-MANIFEST.md', M, md_row(c) + '\n', md_row([c[0], c[1], fmt % blob[:12], sha(LANDED6[p])]) + '\n',
              'sec. 1: row of %s (source and sha256)' % p)
_last5 = md_row(S1['generator-round5/records-1169-round5.json']) + '\n'
M = sedit('MAN', 'LANDING-MANIFEST.md', M, _last5, _last5 + ''.join(
    md_row([p, 'round-6 generator (produces the round-6 files)', 'round-6 generator', sha(b)]) + '\n' for p, b in GEN6.items()),
    'sec. 1: rows of generator-round6')
M = sedit('MAN', 'LANDING-MANIFEST.md', M, '| LANDING-MANIFEST.md | this manifest (A5) | round-5 output | (this file) |',
          '| LANDING-MANIFEST.md | this manifest (A5) | round-6 output | (this file) |', 'sec. 1: this manifest is a round-6 output')
P6 = (
    'Round 6 (%s, item 1, quoted above): generator-round2/correct2.py, generator-round3/correct3.py and '
    'generator-round4/correct4.py as landed are functionally equivalent to, but not byte-identical with, the versions used '
    'in their rounds. The originals stay in Git history: correct2.py (blob %s) and correct3.py (blob %s) at %s, and '
    'correct4.py (blob %s) at %s. The single change in each is that its hygiene check builds the name of the local '
    'working directory it refuses at run time, from two parts, as generator-round5 does, so that the repository\'s '
    'added-text scan, which refuses that name in added text, does not match the check\'s own source; the check tests the '
    'same string and reports the same name. Run on the inputs of its own round, each corrected generator writes the same '
    'files as its original, except that generator-round4\'s LANDING-MANIFEST.md states the sha256 of correct4.py itself '
    'and its CORRECTION-REPORT-round4.md the sha256 of that manifest. Given the corrected correct2.py as an input, '
    'generator-round3 writes the same files except for that input\'s sha256 in CORRECTION-REPORT-round3.md; generators '
    '4 and 5 refuse a corrected predecessor, since each checks its predecessor against its git blob, so the recipes of '
    'rounds 3 to 5 lay out the originals from those commits. The 46 status paragraphs of FRESH-AUTHORIZATION.md begin with their requirement id; '
    'nothing else in that file changes. Recipe: lay out the directories of the round-5 recipe, `landing5/` as this '
    'directory at %s and `out-final7/build/` as generator-round6 (correct6.py, with records-1169-round6.json in '
    '`inputs/`), and run `python3 -I -B out-final7/build/correct6.py`. It exits 0 and writes the files of sec. 1 marked '
    '"round-6 output" with the sha256 stated, after checking every file of `landing5/` against the sha256 of the round-5 '
    'manifest, regenerating the round-5 files with generator-round5 and re-running the self-checks of rounds 3 to 5 on the '
    'round-6 files. CORRECTION-REPORT-round6.md, which it writes beside its outputs, is not landed.'
    % (OD6, GENFIX['generator-round2/correct2.py'][1][:12], GENFIX['generator-round3/correct3.py'][1][:12], C33_COMMIT[:8],
       GENFIX['generator-round4/correct4.py'][1][:12], R4_COMMIT[:8], L5_COMMIT))
M = sedit('HIST', 'LANDING-MANIFEST.md', M, '\n\n## 2. Files left to Git history\n', '\n\n' + P6 + '\n\n## 2. Files left to Git history\n',
          'sec. 1: paragraph on round 6 (functional equivalence of the corrected generators; recipe)')
M = sedit('MAN', 'LANDING-MANIFEST.md', M, 'except this manifest and the two generator programs,',
          'except this manifest and the three generator programs,', 'sec. 3: correct6.py excluded from the table like correct4.py and correct5.py')
M = sedit('MAN', 'LANDING-MANIFEST.md', M, 'The generator programs correct4.py and correct5.py carry the references',
          'The generator programs correct4.py, correct5.py and correct6.py carry the references', 'sec. 3: note names correct6.py')

# ---- sec. 3 table: rows of the new references, files of every row recomputed by the round-5 patterns
PAT = NS5['PAT']
KORD = list(PAT)
GENS6 = ('generator-round4/correct4.py', 'generator-round5/correct5.py', 'generator-round6/correct6.py')


def scan(landed, paths):
    found = collections.OrderedDict()
    for p in paths:
        t = landed[p].decode('utf-8')
        for kind, rx in PAT.items():
            for m in re.findall(rx, t):
                found.setdefault(m, set()).add(p)
    return found


_REFHEAD = '| Reference | Kind | What it names | Status | Occurs in | Classification |'
_ra, REF5 = table_rows(MAN5, _REFHEAD)
REF5C = collections.OrderedDict((ln[2:-2].split(' | ')[0], ln[2:-2].split(' | ')) for ln in REF5)
_rkey = lambda c: (KORD.index('comment' if c[1] == 'digit run' else c[1]), c[0])
SORT_CONTROL = [c[0] for c in sorted(REF5C.values(), key=_rkey)] == list(REF5C)
F5 = scan(NS5['LANDED5'], [p for p in NS5['LANDED5'] if p not in GENS6])
SCAN_CONTROL = (set(F5) == set(REF5C) and all(', '.join(sorted(F5[t])) == REF5C[t][4] for t in F5))
NEWREF = collections.OrderedDict([
    (DEC6_ID, ['comment', '#1169 comment %s' % DEC6_ID, 'GitHub record', 'support on main: its body, author and time land '
               'in a comment snapshot, and this manifest quotes it with author and time (AGENTS.md sec. A.42 item 7)']),
    ('#1575', ['number', 'Issue or pull request #1575', 'GitHub record', 'provenance: occurs only inside a quoted comment'])])
F6 = scan(LANDED6, [p for p in LANDED6 if p not in GENS6])
REF6C = collections.OrderedDict((t, list(c)) for t, c in REF5C.items())
for t, files in F6.items():
    occ = ', '.join(sorted(files))
    if t in REF6C:
        if REF6C[t][4] != occ:
            REF6C[t][4] = occ
            log('MAN', 'LANDING-MANIFEST.md', 'sec. 3: files of %s recomputed (%s)' % (t, occ))
    elif t in NEWREF:
        k, what, st, cl = NEWREF[t]
        REF6C[t] = [t, k, what, st, occ, cl]
        log('MAN', 'LANDING-MANIFEST.md', 'sec. 3: row of %s added' % t)
    else:
        PROBLEMS.append('manifest: unclassified reference %s in %s' % (t, sorted(files)))
for t in REF5C:
    if t not in F6:
        PROBLEMS.append('manifest: stale row %s' % t)
for t in NEWREF:
    if t not in F6:
        PROBLEMS.append('manifest: classified reference %s not found' % t)
REF6 = [md_row(c) for c in sorted(REF6C.values(), key=_rkey)]
M = M[:_ra] + M[_ra:].replace('\n'.join([_REFHEAD, '|' + '---|' * 6] + REF5), '\n'.join([_REFHEAD, '|' + '---|' * 6] + REF6), 1)

# ---- references of correct6.py outside the table (listed in the note, as for correct4.py and correct5.py)
GEN6_CLASS = collections.OrderedDict([
    (L5_COMMIT, 'on main once the landing merge keeps the branch history: the round-5 landing tree, input of generator-round6'),
    (L5_COMMIT[:8], 'on main once the landing merge keeps the branch history: prefix of the commit of the round-5 landing tree'),
    (MAN5_SHA, 'sha256 of LANDING-MANIFEST.md at a902d272, an input pin of generator-round6')])
G6X = [t for t in scan(LANDED6, ['generator-round6/correct6.py']) if t not in REF6C]
G6NOTE = []
for t in G6X:
    if t in GEN6_CLASS:
        G6NOTE.append('%s (generator-round6/correct6.py, %s)' % (t[:12] if re.fullmatch('[0-9a-f]+', t) else t, GEN6_CLASS[t]))
    elif t in [b for _, b in GENFIX.values()]:
        PROBLEMS.append('manifest: blob %s of an original generator not in the table' % t[:12])
    else:
        PROBLEMS.append('manifest: unclassified reference of correct6.py: %s' % t)
_n5 = 'a false match of the round-4 scanner of the same kind).\n'
M = sedit('MAN', 'LANDING-MANIFEST.md', M, _n5, _n5[:-2] + ''.join('; ' + x for x in G6NOTE) + '.\n',
          'sec. 3: references of correct6.py outside the table listed in the note')
MANIFEST = M

# =====================================================================================================
# self-checks
# =====================================================================================================
SUBST6 = {'FRESH': FRESH, 'MANIFEST': MANIFEST,
          'LANDED5': collections.OrderedDict((p, LANDED6[p]) for p in NS5['LANDED5'])}
CHK6, VAL6, OWN4_6, OWN5_6 = rerun5(SUBST6)
EXPECTED_FAIL = {D2KEY: ['generator-round4/correct4.py']}
SEG_ATTR = collections.OrderedDict(
    [('round-3 ' + k, v) for k, v in CHK6.items()] + [('round-4 ' + k, v) for k, v in OWN4_6.items()] +
    [('round-5 ' + k, v) for k, v in OWN5_6.items()])


def dup_scan(landed):
    hits = []
    for p, b in landed.items():
        if not p.endswith('.md'):
            continue
        t = b.decode('utf-8', errors='replace')
        hc = collections.Counter(m.group(0).strip() for m in re.finditer(r'^#{2,4} .+$', t, re.M))
        hits += ['%s: heading %r' % (p, h[:40]) for h, n in hc.items() if n > 1]
        pc = collections.Counter(x.strip() for x in t.split('\n\n') if len(x.strip()) >= 200)
        hits += ['%s: paragraph %r' % (p, x[:40]) for x, n in pc.items() if n > 1]
    return hits


LOCAL = re.compile(r'/(?:tmp|home|root|Users)/|' + WORD + r'|[A-Z]:\\\\')
SECRET = re.compile(r'ghp_[A-Za-z0-9]{20,}|' + 'github' + r'_pat_|sk-[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}|'
                    r'-----BEGIN [A-Z ]*PRIVATE KEY|[A-Za-z0-9._%+-]+' + AT + r'[A-Za-z0-9.-]+\.[a-z]{2,}')


def scan_text(landed):
    hits = []
    for p, b in landed.items():
        if not p.endswith(('.md', '.py')):
            continue
        for i, ln in enumerate(b.decode('utf-8').split('\n')):
            for what, rx in (('local-path', LOCAL), ('secret', SECRET)):
                if rx.search(ln):
                    hits.append('%s:%d %s %s' % (p, i + 1, what, rx.search(ln).group(0)))
    return hits


L5_NOMAN = collections.OrderedDict((p, b) for p, b in L5FILES.items())
L6_ALL = collections.OrderedDict(list(LANDED6.items()) + [('LANDING-MANIFEST.md', MANIFEST.encode('utf-8'))])
DUP5, DUP6 = dup_scan(L5_NOMAN), dup_scan(L6_ALL)
TXT5, TXT6 = scan_text(L5_NOMAN), scan_text(L6_ALL)
_s1b, S1ROWS6 = table_rows(MANIFEST, '| Path | Role | Source | sha256 |')
S1_6 = collections.OrderedDict((ln[2:-2].split(' | ')[0], ln[2:-2].split(' | ')) for ln in S1ROWS6)
_exp6 = json.loads(LANDED6['EXPECTATIONS.json'].decode('utf-8'))
_req6 = json.loads(LANDED6['REQUIREMENTS.json'].decode('utf-8'))

OWN6 = collections.OrderedDict()
OWN6['inputs: every file of landing5/ has the sha256 the round-5 manifest states; the manifest has the pinned sha256; the layout of the round-5 recipe equals the landed generators'] = [
    p for p in PROBLEMS if p.startswith(('input ', 'layout'))]
OWN6['records: comment 7174085995 by amaybaum, with the decision\'s author and time line and every quoted sentence verbatim'] = [
    p for p in PROBLEMS if p.startswith('records')]
OWN6['generator-round5 regenerates every round-5 landed file and the round-5 manifest byte-identical to a902d272'] = [
    p for p in PROBLEMS if p.startswith('generator-round5')]
OWN6['control: re-running generator-round5\'s self-check segment on the round-5 files gives the results of its own run'] = (
    [] if RERUN_CONTROL else ['differs'])
OWN6['DUP: one status paragraph per entry of sec. 4 (46), each prefixed with its own requirement id; the ids are those of the sec. 1 table'] = (
    ([] if len(STAT_IDS) == 46 == len(set(STAT_IDS)) and sorted(STAT_IDS) == sorted(T1_IDS) else ['ids']) +
    ([] if FRESH5.count('\nStatus: ') == 46 and FRESH.count('\nStatus: ') == 0 else ['count']))
OWN6['DUP: removing the 46 prefixes gives the round-5 FRESH-AUTHORIZATION.md byte for byte'] = (
    [] if FRESH_UNDO == FRESH5 else ['differs'])
for p, chk in GEN_EQ.items():
    OWN6['GEN: %s: %s' % (p, '; '.join(chk))] = [k for k, v in chk.items() if not v]
OWN6['preservation: REQUIREMENTS.json and EXPECTATIONS.json byte-identical; %d requirements, %d expectation rows' % (N_REQ, N_ROWS)] = (
    [p for p in ('REQUIREMENTS.json', 'EXPECTATIONS.json') if LANDED6[p] != L5FILES[p]] +
    ([] if len(_req6) == N_REQ and len(_exp6['rows']) == N_ROWS and len(NS5['REQS']) == N_REQ else ['counts']))
OWN6['preservation: every other landed file byte-identical to a902d272'] = [
    p for p in L5FILES if p not in CHANGED6 and p != 'LANDING-MANIFEST.md' and LANDED6[p] != L5FILES[p]]
OWN6['re-run on the round-6 files: every check of rounds 3 to 5 passes, except the round-5 check that generator-round4 is byte-identical to 2aec244e, which fails only for correct4.py (replaced by the GEN checks)'] = [
    k for k, v in SEG_ATTR.items() if v and not (k == 'round-5 ' + D2KEY and v == EXPECTED_FAIL[D2KEY])] + (
    [] if OWN5_6[D2KEY] == EXPECTED_FAIL[D2KEY] else ['expected failure absent'])
OWN6['MAN: sec. 1 lists every landed file with its sha256 (%d files with this manifest)' % (len(LANDED6) + 1)] = [
    p for p in LANDED6 if p not in S1_6 or S1_6[p][3] != sha(LANDED6[p])] + [p for p in S1_6 if p not in L6_ALL]
OWN6['MAN: control: the round-5 patterns, run on the round-5 files, give the round-5 table (references and files), whose order the sort reproduces'] = (
    [] if SCAN_CONTROL and SORT_CONTROL else ['scan' if not SCAN_CONTROL else 'sort'])
OWN6['MAN: every reference in the landed files is classified, no row is stale, and the references of correct6.py outside the table are in the note'] = [
    p for p in PROBLEMS if p.startswith('manifest')] + [x for x in G6NOTE if x not in MANIFEST]
OWN6['MAN: the list of unsupported statements (sec. 4) and secs. 2 and 4 unchanged'] = (
    [] if MAN5[MAN5.index('\n## 4. '):] == MANIFEST[MANIFEST.index('\n## 4. '):] and
    MAN5[MAN5.index('\n## 2. '):MAN5.index('\n## 3. ')] == MANIFEST[MANIFEST.index('\n## 2. '):MANIFEST.index('\n## 3. ')] else ['differs'])
OWN6['repository duplicate check (paragraph of 200 characters or more, or heading, repeated in one file) on the landed files: no hit'] = DUP6
OWN6['repository added-text scan (local-path and secret patterns) on every landed .md and .py file: no hit'] = TXT6
OWN6['edits: every edit applied exactly once'] = [p for p in PROBLEMS if p.startswith('edit ')]
for k, v in OWN6.items():
    if v:
        PROBLEMS.append('check failed: %s: %s' % (k, v[:10]))

# =====================================================================================================
# CORRECTION-REPORT-round6.md
# =====================================================================================================
CONTENT = collections.OrderedDict([('FRESH-AUTHORIZATION.md', FRESH), ('LANDING-MANIFEST.md', MANIFEST)] +
                                  [(p, s) for p, s in GEN_NEW.items()] +
                                  [(p, b.decode('utf-8')) for p, b in GEN6.items()])


def md_table(head, rows):
    return '\n'.join(['| ' + ' | '.join(head) + ' |', '|' + '---|' * len(head)] + [md_row(r) for r in rows])


def pf(v):
    return 'pass' if not v else 'FAIL %s' % v[:5]


def report():
    hashes = collections.OrderedDict((n, sha(c)) for n, c in CONTENT.items())
    L = ['# r6, round 6: correction report', '',
         'Generator: build/correct6.py (landed as generator-round6/). Applies item 1 of the %s (#1169 comment %s, %s; quoted in '
         'LANDING-MANIFEST.md): a bounded amendment of the adopted landing package for two repository checks, the duplicate '
         'check and the added-text scan. Nothing is adopted, frozen, merged or executed.' % (OD6, DEC6_ID, DEC6_REC_AT), '',
         '## 1. Inputs', '', md_table(['Input', 'sha256'], [('landing5/' + p, sha(b)) for p, b in L5FILES.items()] +
                                      list(INPUT6.items())), '',
         'landing5/ is the directory at %s. generator-round5 is executed in-process up to its report from the layout of the '
         'round-5 recipe; it checks its own inputs against 2aec244e, executes generator-round4, and regenerated %d files, each '
         'byte-identical to a902d272.' % (L5_COMMIT, C5_REPRO), '',
         '## 2. Edits', '', md_table(['#', 'Item', 'Target', 'Edit'], [(i + 1, d, t, e) for i, (d, t, e) in enumerate(LOG)]), '',
         'Items: DUP, duplicate paragraphs; GEN, generator hygiene checks; HIST, historical integrity; MAN, manifest (quoted in '
         'LANDING-MANIFEST.md).', '',
         '## 3. The corrected generators', '',
         md_table(['Generator', 'Original (commit, blob)', 'sha256 before', 'sha256 after'] + list(next(iter(GEN_EQ.values()))),
                  [(p, '%s, %s' % (c[:8], b[:12]), sha(L5FILES[p]), sha(GEN_NEW[p])) + tuple(
                      'yes' if v else 'no' for v in GEN_EQ[p].values()) for p, (c, b) in GENFIX.items()]), '',
         'The edit replaces the literal pair in the hygiene check by `%s` and inserts, before the hygiene loop:' % NEW_T, '',
         '    ' + INSERT.rstrip('\n'), '',
         'The check therefore tests the same string and reports the same name. The syntax-tree comparison reads `SCR` as the '
         'value it is bound to and drops its assignment; the tree is then equal to the original\'s.', '',
         '## 4. Self-checks', '',
         'Round-3 checks (run_checks of correct3.py), on the round-5 files (before) and the round-6 files (after):', '',
         md_table(['Check', 'Before', 'After'], [(k, pf(CHK5[k]), pf(CHK6[k])) for k in CHK6]), '',
         'Round-4 checks (generator-round4\'s own check code), before and after:', '',
         md_table(['Check', 'Before', 'After'], [(k, pf(OWN4_5[k]), pf(OWN4_6[k])) for k in OWN4_6]), '',
         'Round-5 checks (generator-round5\'s own check code), before and after:', '',
         md_table(['Check', 'Before', 'After'], [(k, pf(OWN5_5[k]), pf(OWN5_6[k])) for k in OWN5_6]), '',
         'The one round-5 failure after the change is the byte-identity of generator-round4 with 2aec244e, which the decision '
         'replaces by functional equivalence (sec. 3).', '',
         'Values, before and after: %s.' % '; '.join('%s %s -> %s' % (k, VAL5[k], VAL6[k]) for k in VAL6), '',
         'Round-6 checks:', '', md_table(['Check', 'Result'], [(k, pf(v)) for k, v in OWN6.items()]), '',
         'Repository checks replicated on the landed files, before (a902d272) and after: duplicate check %d -> %d hit(s); '
         'added-text scan %d -> %d hit(s).' % (len(DUP5), len(DUP6), len(TXT5), len(TXT6)), '',
         '## 5. Outputs', '', md_table(['File', 'sha256'], list(hashes.items())), '',
         'The generator re-runs itself in a separate process and writes only if every output\'s sha256 is equal.', '']
    return '\n'.join(L)


CONTENT['CORRECTION-REPORT-round6.md'] = report()

# =====================================================================================================
# hygiene, reproducibility, write
# =====================================================================================================
ALLOWED = set(ch for b in L5FILES.values() for ch in b.decode('utf-8') if ord(ch) > 127)
BAD_SP = re.compile('[\\u00a0\\u1680\\u2000-\\u200b\\u202f\\u205f\\u3000\\ufeff]')
LONG_URL = re.compile(r'https?://github\.com/\S{60,}')
for n, c in CONTENT.items():
    gen = n.startswith('generator-round')  # their own check literals; the added-text scan above covers them
    for what, bad in ((AT, AT in c and not gen), (TMP, TMP in c and not gen), (HOME, HOME in c), (WORD, WORD in c),
                      ('session id', 'session_0' in c and not gen), ('github.com', 'github.com' in c and not gen), ('CR', '\r' in c),
                      ('format character', any(unicodedata.category(ch) == 'Cf' for ch in c) and not gen),
                      ('non-ASCII space', bool(BAD_SP.search(c)) and not gen), ('long github URL', bool(LONG_URL.search(c))),
                      ('non-ASCII character outside inputs', bool(set(ch for ch in c if ord(ch) > 127) - ALLOWED -
                                                                  set(DEC6_BODY)))):
        if bad:
            PROBLEMS.append('hygiene: %s in %s' % (what, n))
HASHES = collections.OrderedDict((n, sha(c)) for n, c in CONTENT.items())
if '--hashes' in sys.argv:
    print(json.dumps(HASHES))
    sys.exit(0)
if PROBLEMS:
    for p in PROBLEMS:
        print('PROBLEM', p)
    sys.exit(1)
rerun = subprocess.run([sys.executable, '-I', '-B', os.path.abspath(__file__), '--hashes'], capture_output=True, text=True, cwd=HERE)
if rerun.returncode != 0 or json.loads(rerun.stdout) != HASHES:
    print('PROBLEM second run differs')
    sys.exit(1)
for n, c in CONTENT.items():
    dst = os.path.join(OUT, n)
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    with open(dst, 'wb') as f:
        f.write(c.encode('utf-8'))
for n, h in HASHES.items():
    print(n, h)
for k, v in OWN6.items():
    print('CHECK', 'pass' if not v else 'FAIL', k)
