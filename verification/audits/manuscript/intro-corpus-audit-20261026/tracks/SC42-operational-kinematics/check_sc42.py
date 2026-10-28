#!/usr/bin/env python3
"""SC-42 checks: Theorem 4's setting against the kernel structure, re-grep counts,
book/FULL mirror parity, and an added-line scan (register, revision voice, caps,
secrets, local paths).

Run from the repository root:  python3 -I <this file> [--base REV]
With --setting-from REV the field check reads papers/GR.md at REV instead of the
working tree; run against the base commit it must FAIL (countercontrol).
"""
import os, re, subprocess, sys

ROOT = os.getcwd()
BASE = '0d917665d32287e5d0ce649012175f2c7bf75b09'
if '--base' in sys.argv:
    BASE = sys.argv[sys.argv.index('--base') + 1]
SETTING_REV = None
if '--setting-from' in sys.argv:
    SETTING_REV = sys.argv[sys.argv.index('--setting-from') + 1]

def read(p, rev=None):
    if rev:
        return subprocess.run(['git', 'show', f'{rev}:{p}'], capture_output=True,
                              text=True, check=True).stdout
    with open(os.path.join(ROOT, p), encoding='utf-8') as f:
        return f.read()

failures = []
def check(ok, msg):
    print(('  ok    ' if ok else '  FAIL  ') + msg)
    if not ok:
        failures.append(msg)

# 1. Field-by-field: every field of FiniteOperationalTheory, and no other, is stated in GR's setting.
lean = read('verification/lean-mathlib/OIBridge/OperationalAssembly.lean')
m = re.search(r'structure FiniteOperationalTheory .*? where\n(.*?)\n\n', lean, re.S)
fields = re.findall(r'^  (\w+) :', m.group(1), re.M)
FIELD_TO_GR = {
    'avail': 'finite outcome families of such maps are available on the system',
    'availExt': 'and at every finite ancilla level',
    'avail_id': '(a) the identity is available on the system',
    'avail_coarse': '(b) coarse-graining the outcome labels of an available family gives an available family, on the system',
    'availExt_coarse': 'and at every level; (c)',
    'availExt_bind': '(c) at every ancilla level, an available family followed by available families chosen by its outcome is available',
    'prepAvail': 'which preparation maps',
    'prepAvail_uniform': '(d) attaching a uniformly mixed ancilla',
    'prepAvail_post': 'an available preparation followed by an available single-outcome operation at its level is an available preparation',
    'readout': '(e) at every level $n$ an available $n$-outcome family reads the ancilla',
    'readout_avail': 'an available $n$-outcome family',
    'readout_local': 'a spectator-independence requirement',
    'prepAvail_discard': '(f) an available preparation, followed by an available family at its level and then by discarding the ancilla',
}
print('[1] FiniteOperationalTheory fields vs GR §3.3 setting'
      + (f' (GR at {SETTING_REV})' if SETTING_REV else ''))
check(sorted(fields) == sorted(FIELD_TO_GR), f'kernel fields {fields} == mapped fields (none added, none omitted)')
gr = read('papers/GR.md', SETTING_REV)
setting = next((ln for ln in gr.splitlines() if ln.startswith('**The operational-completion characterization.**')), '')
for f in fields:
    check(FIELD_TO_GR.get(f, '\0') in setting, f'field {f} stated in the setting')
for phrase in ['The setting takes complex matrix kinematics as given',
               'M_A(\\mathbb{C})', 'A derivation of this kinematics', 'is open']:
    check(phrase in setting, f'kinematics clause: {phrase!r}')
check('`readout_is_localLuders`' in setting and '`FiniteOperationalTheory`' in setting,
      'kernel anchors cited in the setting')
if SETTING_REV:
    print('setting-only mode:', 'FAIL' if failures else 'OK')
    sys.exit(1 if failures else 0)

# 2. Theorem statement unchanged (strength kept).
thm = '**Theorem (operational-completion characterization).** *For every nonempty finite visible system, the available outcome families on the system and on every positive ancilla level are exactly the normalized finite Kraus instruments if and only if conditions (i)–(v) hold.*'
print('[2] theorem statement')
check(thm in gr and thm in read('papers/GR.md', BASE), 'GR theorem line identical at base and head')

# 3. Re-grep: stale phrasings gone, kinematics clause present at each restatement.
CORPUS = ['papers/GR.md', 'papers/Main.md', 'papers/Methodology.md', 'papers/Explainer.md',
          'book/ch01-observation.md', 'book/ch09-universality.md', 'book/ch19-open-problems.md',
          'book/glossary.md', 'book/The-Incompleteness-of-Observation-FULL.md']
STALE = ['delivers QM on a finite-dimensional', 'quantum instruments open)', 'Level three (open)',
         'operational-lifting problem', 'remains open (§19.2.12)', 'instrument algebra still open',
         'residual common coherent/composite lift', 'on every ancilla level are exactly']
print('[3] re-grep')
for s in STALE:
    n = sum(read(p).count(s) for p in CORPUS)
    check(n == 0, f'stale {s!r}: {n}')
counts = {p: read(p).count('complex matrix kinematics') + read(p).count('complex matrices indexed')
          for p in CORPUS}
for p, n in counts.items():
    print(f'        kinematics mentions {p}: {n}')
EXPECT = {'papers/GR.md': 1, 'papers/Main.md': 12, 'papers/Methodology.md': 1, 'papers/Explainer.md': 3,
          'book/ch01-observation.md': 1, 'book/ch09-universality.md': 1, 'book/ch19-open-problems.md': 2,
          'book/glossary.md': 1, 'book/The-Incompleteness-of-Observation-FULL.md': 5}
base_n = sum(read(p, BASE).count('complex matrix kinematics') + read(p, BASE).count('complex matrices indexed')
             for p in CORPUS)
check(base_n == 0, f'kinematics mentions at base: {base_n}')
check(counts == EXPECT, f'kinematics mention counts match the site table ({sum(EXPECT.values())})')

# 4. Mirror parity: each changed chapter paragraph is present verbatim in FULL.
print('[4] book/FULL mirror parity')
full = read('book/The-Incompleteness-of-Observation-FULL.md')
diff = subprocess.run(['git', 'diff', '-U0', BASE, '--', 'book/ch01-observation.md',
                       'book/ch09-universality.md', 'book/ch19-open-problems.md', 'book/glossary.md'],
                      capture_output=True, text=True, check=True).stdout
added = [l[1:] for l in diff.splitlines() if l.startswith('+') and not l.startswith('+++')]
for l in added:
    check(l in full, f'chapter line mirrored in FULL: {l[:60]}...')

# 5. Added-text scan over the whole diff, at word granularity so that pre-existing words on a
#    changed line are not attributed to this change (papers: register; all: revision voice, caps,
#    secrets, local paths).
print('[5] added-text scan')
diff = subprocess.run(['git', 'diff', '-U0', '--word-diff=porcelain', BASE, '--', '*.md', '*.py'],
                      capture_output=True, text=True, check=True).stdout
cur = None; hits = []; scanned = 0
REGISTER = re.compile(r'should not be read|the reader should|reader should note|discipline|honest|'
                      r'temptation|stated in that register|neither borrows', re.I)
HISTORY = re.compile(r'is now settled|now settled|in its current form|the corrected form|as redefined|'
                     r'no longer|formerly|withdrawn|earlier revisions|previously stated', re.I)
CAPS = re.compile(r'(?<=[a-z,;:] )([A-Z]{4,})\b')
CAPS_OK = {'PASS', 'FAIL', 'NEW', 'POSITIVE'}
SECRET = re.compile(r'ghp_[A-Za-z0-9]{20,}|github_pat_|sk-[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}|'
                    r'-----BEGIN [A-Z ]*PRIVATE KEY|[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[a-z]{2,}')
LOCAL = re.compile(r'/(?:tmp|home|root|Users)/|scratch' + r'pad|[A-Z]:\\\\')
for l in diff.splitlines():
    if l.startswith('+++ b/'):
        cur = l[6:]; continue
    if not l.startswith('+') or l.startswith('+++') or cur.endswith('check_sc42.py'):
        continue
    t = l[1:]; scanned += 1
    if cur.startswith('papers/') and REGISTER.search(t):
        hits.append((cur, 'register', REGISTER.search(t).group(0)))
    if not cur.endswith('README.md') and HISTORY.search(t):
        hits.append((cur, 'history', HISTORY.search(t).group(0)))
    for c in CAPS.findall(t):
        if c not in CAPS_OK and not cur.endswith('README.md'):
            hits.append((cur, 'caps', c))
    if SECRET.search(t):
        hits.append((cur, 'secret', SECRET.search(t).group(0)))
    if LOCAL.search(t):
        hits.append((cur, 'local-path', LOCAL.search(t).group(0)))
print(f'        scanned {scanned} added text chunk(s)')
for h in hits:
    print('        hit', h)
check(not hits, f'added-text scan: {len(hits)} hit(s)')

print('check_sc42:', 'FAIL' if failures else 'OK', f'({len(failures)} failure(s))')
sys.exit(1 if failures else 0)
