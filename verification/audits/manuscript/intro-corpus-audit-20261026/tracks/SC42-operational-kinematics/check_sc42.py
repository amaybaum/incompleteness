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
# Condition (i) is quantified over the ancilla levels, as CompositeOperationalValidity is; a
# system-level (i) would be failed by the (ii)-witness systemLoose, whose system carries X -> 2X.
val = read('verification/lean-mathlib/OIBridge/OperationalValidity.lean')
vdef = re.search(r'def CompositeOperationalValidity.*?\n\n', val, re.S).group(0)
check('T.availExt n O F' in vdef and 'T.avail O' not in vdef,
      'kernel (i) quantifies over availExt (ancilla levels) only')
seam = read('verification/lean-mathlib/OIBridge/LevelOneSeam.lean')
check('theorem systemLoose_amplifier_available' in seam and 'avail := fun _ _ _ _ => True' in seam,
      'systemLoose makes every system family available (amplifier X -> 2X included)')
check('(i) *Valid probabilities*: at every ancilla level, every available family' in setting,
      'GR (i) stated at every ancilla level')
check('no premise beyond its stated setting' in setting, 'GR: no premise beyond its stated setting')
if SETTING_REV:
    print('setting-only mode:', 'FAIL' if failures else 'OK')
    sys.exit(1 if failures else 0)

# 2. Theorem statement unchanged (strength kept).
thm = '**Theorem (operational-completion characterization).** *For every nonempty finite visible system, the available outcome families on the system and on every positive ancilla level are exactly the normalized finite Kraus instruments if and only if conditions (i)–(v) hold.*'
print('[2] theorem statement')
check(thm in gr and thm in read('papers/GR.md', BASE), 'GR theorem line identical at base and head')

# 3. Re-grep: stale phrasings gone, kinematics clause present at each restatement.
CORPUS = ['papers/GR.md', 'papers/Main.md', 'papers/Methodology.md', 'papers/Explainer.md',
          'papers/Structure.md', 'papers/Substratum.md', 'papers/SM.md',
          'book/preface.md', 'book/ch00-introduction.md', 'book/ch01-observation.md',
          'book/ch02-substratum.md', 'book/ch03-structural-realism.md', 'book/ch04-methodology.md',
          'book/ch09-universality.md', 'book/ch14-quantum-computing.md', 'book/ch18-beyond.md',
          'book/ch19-open-problems.md', 'book/glossary.md', 'book/appendix-b-derivations.md',
          'book/appendix-c-objections.md', 'book/readers-guide.md',
          'book/The-Incompleteness-of-Observation-FULL.md']
STALE = ['delivers QM on a finite-dimensional', 'quantum instruments open)', 'Level three (open)',
         'operational-lifting problem', 'remains open (§19.2.12)', 'instrument algebra still open',
         'residual common coherent/composite lift', 'on every ancilla level are exactly',
         'lifting problem', 'operational lifting', 'operational-lifting', 'lifting debt',
         'lifting result', 'lifting frontier', 'active-lifting', 'open coherent operational lift',
         'stated as open (§3.2', 'states as open (§3.2', 'stated as open ([Main §3.2',
         'with no external premise', 'one-step coherence for the linear lattice realization, and',
         # round 3: the characterization concerns an operational theory's available instruments,
         # not the fixed-basis representation; the tensor composite and local tomography are
         # in the assumed kinematics, not characterized by the conditions
         'the fixed-basis representation extends to the standard noncommuting',
         'Whether they do is characterized', 'full operational theory of instruments on that space',
         'The step from that exact representation class',
         'full coherent observable/instrument structure holds',
         'instrument and composite structure of standard quantum mechanics holds',
         'tensor/composite instrument structure is part of the coherent operational lift',
         # round 4
         'by five operational conditions which instruments are available',
         'the instrument algebra is reached exactly when',
         'reached exactly under the operational completion conditions',
         'On every nonempty finite carrier these three principles',
         '*conditionally*: it holds exactly when the explicit completion principles']
print('[3] re-grep')
for s in STALE:
    n = sum(read(p).count(s) for p in CORPUS)
    check(n == 0, f'stale {s!r}: {n}')
counts = {p: read(p).count('complex matrix kinematics') + read(p).count('complex matrices indexed')
          for p in CORPUS}
for p, n in counts.items():
    print(f'        kinematics mentions {p}: {n}')
EXPECT = {'papers/GR.md': 3, 'papers/Main.md': 17, 'papers/Methodology.md': 1, 'papers/Explainer.md': 8,
          'papers/Structure.md': 1, 'papers/Substratum.md': 2, 'papers/SM.md': 0,
          'book/preface.md': 1, 'book/ch00-introduction.md': 1, 'book/ch01-observation.md': 3,
          'book/ch02-substratum.md': 2, 'book/ch03-structural-realism.md': 2, 'book/ch04-methodology.md': 1,
          'book/ch09-universality.md': 1, 'book/ch14-quantum-computing.md': 1, 'book/ch18-beyond.md': 0,
          'book/ch19-open-problems.md': 3, 'book/glossary.md': 2, 'book/appendix-b-derivations.md': 0,
          'book/appendix-c-objections.md': 0, 'book/readers-guide.md': 0,
          'book/The-Incompleteness-of-Observation-FULL.md': 17}
base_n = sum(read(p, BASE).count('complex matrix kinematics') + read(p, BASE).count('complex matrices indexed')
             for p in CORPUS)
check(base_n == 0, f'kinematics mentions at base: {base_n}')
check(counts == EXPECT, f'kinematics mention counts match the site table ({sum(EXPECT.values())})')

# 3b. Pinned texts (round 3), with the kernel witnesses of the characterization's two directions.
print('[3b] pinned texts and witnesses')
PINS = {
 'papers/Main.md': ["the instrument algebra is reached, on a finite carrier within complex matrix kinematics taken as given, exactly when the five operational completion conditions hold ([GR §3.3]; Remark below), none of them supplied by the fixed-basis layer, and",
                    "reached, on a finite carrier within complex matrix kinematics taken as given, exactly under the operational completion conditions (§3.4; [GR §3.3])",
                    "On every nonempty finite carrier, within the same complex matrix kinematics, these three principles",
                    "The operational-completion characterization ([GR §3.3]) takes the complex matrix kinematics as given, the tensor-product composite and with it local tomography included, and deriving that kinematics is open; within it, whether the available interventions on a finite carrier and its composites are exactly the quantum instruments is characterized by the five completion conditions of §3.4."],
 'book/glossary.md': ["What remains is operational: on a finite carrier, within complex matrix kinematics taken as given, an operational theory's available instruments on the carrier and its composites are the standard noncommuting quantum instruments exactly when the five completion conditions of the operational-completion characterization ([GR §3.3]) hold; which of them the substratum supplies, and a derivation of that kinematics, are open."],
 'papers/GR.md': ["The OI⁺, primitive-source, substratum-source, layer-flow and typed forms below are stated over the same kinematics, the typed form over the complex matrices of every finite carrier.",
                  "whether an operational theory's available instruments on a finite carrier and its composites are the quantum instruments is a separate question, which §3.3 characterizes, within complex matrix kinematics taken as given, by its completion conditions."],
 'papers/Explainer.md': ["The full operational theory is a separate question from that exact representation class:",
                         "takes the tensor-product composite as part of the complex matrix kinematics it assumes",
                         "and within that kinematics characterizes by five operational conditions when the available instruments are exactly the quantum instruments."],
 'book/ch19-open-problems.md': ["*conditionally*: within complex matrix kinematics taken as given, it holds exactly when the explicit completion principles hold"],
 'papers/Structure.md': ["whether an operational theory's available instruments on a finite carrier and its composites are exactly the quantum instruments, simultaneously across all interventions, is a separate question"],
 'book/preface.md': ["within complex matrix kinematics taken as given, the tensor-product composite included, an operational theory's available instruments"],
}
for pth, ss in PINS.items():
    for s in ss:
        check(read(pth).count(s) == 1, f'pinned in {pth}: {s[:60]}...')
check(PINS['book/glossary.md'][0] in read('book/The-Incompleteness-of-Observation-FULL.md')
      and PINS['book/preface.md'][0] in read('book/The-Incompleteness-of-Observation-FULL.md'),
      'glossary and preface pins mirrored in FULL')
gc = read('verification/lean-mathlib/OIBridge/GeneralCarrier.lean').splitlines()
pc = read('verification/lean-mathlib/OIBridge/PhysicalCharacterization.lean').splitlines()
check(gc[92].startswith('theorem exactAll_of_physical_general'),
      'witness conditions => exact: exactAll_of_physical_general (GeneralCarrier.lean:93)')
check(pc[300].startswith('theorem physical_of_exactAll'),
      'witness exact => conditions: physical_of_exactAll (PhysicalCharacterization.lean:301)')
ka = read('verification/lean-mathlib/OIBridge/KrausSoundness.lean')
check('T.avail (Fin m) F ↔ IsFiniteEndomorphicKrausInstrument F' in ka,
      'exactness is about the available families (T.avail), not a representation of a law')

# 4. Mirror parity: each changed chapter paragraph is present verbatim in FULL.
print('[4] book/FULL mirror parity')
full = read('book/The-Incompleteness-of-Observation-FULL.md')
CHAPTERS = [p for p in CORPUS if p.startswith('book/') and not p.endswith('FULL.md')]
diff = subprocess.run(['git', 'diff', '-U0', BASE, '--'] + CHAPTERS,
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
