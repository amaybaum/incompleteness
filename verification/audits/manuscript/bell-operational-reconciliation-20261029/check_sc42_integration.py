#!/usr/bin/env python3
"""SC-42 integration successor: retains the historical scientific guards and adds an explained static site table,
structured results and bounded must-fail text controls. Theorem 4 setting against the kernel structure, re-grep counts,
book/FULL mirror parity, and an added-line scan (register, revision voice, caps,
secrets, local paths).

Run from the repository root:  python3 -I <this file> [--base REV]
With --setting-from REV the field check reads papers/GR.md at REV instead of the
working tree; run against the base commit it must FAIL (countercontrol).
"""
import os, re, subprocess, sys, json, difflib, hashlib
from pathlib import Path

ROOT = os.getcwd()
BASE = 'ca3a5bb25ec6fdff3d3ccffcacd2d7bac3bb4caf'
if '--base' in sys.argv:
    BASE = sys.argv[sys.argv.index('--base') + 1]
SETTING_REV = None
if '--setting-from' in sys.argv:
    SETTING_REV = sys.argv[sys.argv.index('--setting-from') + 1]

def original_read(p, rev=None):
    if rev:
        return subprocess.run(['git', 'show', f'{rev}:{p}'], capture_output=True,
                              text=True, check=True).stdout
    with open(os.path.join(ROOT, p), encoding='utf-8') as f:
        return f.read()

SITE_TABLE_PATH = 'verification/audits/manuscript/bell-operational-reconciliation-20261029/sc42-intended-sites.json'
MUTANT = sys.argv[sys.argv.index('--mutant') + 1] if '--mutant' in sys.argv else None
MUTATED_READS = {}
MUTATIONS = {
    'single_outcome': ('papers/GR.md', 'an available preparation followed by an available single-outcome operation at its level', 'an available preparation followed by an available operation at its level', 'field prepAvail_post stated in the setting'),
    'ancilla_validity': ('papers/GR.md', '(i) *Valid probabilities*: at every ancilla level, every available family', '(i) *Valid probabilities*: on the system, every available family', 'GR (i) stated at every ancilla level'),
    'unqualified_kinematics': ('papers/Main.md', 'takes the complex matrix kinematics as given, the tensor-product composite and with it local tomography included, and deriving that kinematics is open', 'derives the complex matrix kinematics, the tensor-product composite and with it local tomography', 'pinned in papers/Main.md: The operational-completion characterization'),
    'mirror': ('book/The-Incompleteness-of-Observation-FULL.md', 'which of them the substratum supplies, and a derivation of that kinematics, are open.', 'which of them the substrate supplies, and a derivation of that kinematics, are open.', 'glossary and preface pins mirrored in FULL'),
    'count': ('papers/Methodology.md', None, '\ncomplex matrix kinematics\n', 'kinematics mention counts match the site table'),
    'paper_caps': ('papers/Methodology.md', None, '\nThis sentence is EMPHASIS.\n', 'added-text scan:'),
    'achieved_no_signaling': ('papers/Main.md', 'with operational no-signaling required.', 'with operational no-signaling established.', 'Bell summary requires rather than derives no-signaling'),
    'fr_partition_escape': ('papers/Methodology.md', "The Wigner's-friend construction is an observer-relative interpretation of a common underlying law; an unconditional Frauchiger–Renner resolution does not follow from it.", 'The Frauchiger–Renner theorem does not apply because the framework has multiple observer partitions.', 'FR scope requires the actual protocol rather than partition multiplicity'),
}

def read(p, rev=None):
    text = original_read(p, rev)
    if rev is None and MUTANT:
        if MUTANT not in MUTATIONS:
            raise SystemExit('unknown mutation')
        target, before, after, _ = MUTATIONS[MUTANT]
        if p == target:
            if before is None:
                changed = text + after
            else:
                if text.count(before) != 1:
                    # The no-signaling guard intentionally targets the summary sentence only.
                    if MUTANT == 'achieved_no_signaling':
                        line = next(l for l in text.splitlines(True) if l.startswith('**Theorem statement.**'))
                        if line.count(before) != 1:
                            raise SystemExit('mutation target is not unique in summary')
                        changed = text.replace(line, line.replace(before, after), 1)
                    else:
                        raise SystemExit('mutation target is not unique: ' + MUTANT)
                else:
                    changed = text.replace(before, after, 1)
            MUTATED_READS[p] = (text, changed)
            return changed
    return text

failures = []
records = []

def diagnostic(*args, **kwargs):
    if '--verbose' in sys.argv:
        print(*args, file=sys.stderr, **kwargs)

def check(ok, msg):
    records.append({'ok': bool(ok), 'predicate': msg})
    if not ok:
        failures.append(msg)
    diagnostic(('ok ' if ok else 'FAIL ') + msg)

def finish():
    value = {'schema': 'sc42-integration-result-v1', 'base': BASE,
             'mode': 'setting-countercontrol' if SETTING_REV else (MUTANT or 'source'),
             'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
             'site_table_sha256': hashlib.sha256(Path(ROOT, SITE_TABLE_PATH).read_bytes()).hexdigest(),
             'checks': records, 'failed_predicates': failures,
             'verdict': 'PASS' if not failures else 'FAIL'}
    if 'counts' in globals():
        value['kinematics_counts'] = counts
        value['intended_counts'] = EXPECT
    print(json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2))
    sys.exit(1 if failures else 0)

if '--self-test' in sys.argv:
    command = [sys.executable, '-I', '-B'] + (['-O'] if sys.flags.optimize else []) + [str(Path(__file__).resolve()), '--base', BASE]
    result = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
    try:
        baseline = json.loads(result.stdout)
    except (ValueError, TypeError):
        baseline = {}
    controls = [{'control': 'unchanged_source', 'exit_code': result.returncode,
                 'passed': result.returncode == 0 and baseline.get('verdict') == 'PASS'}]
    for name, (_, _, _, expected) in MUTATIONS.items():
        run = subprocess.run(command + ['--mutant', name], cwd=ROOT, capture_output=True, text=True)
        try:
            data = json.loads(run.stdout)
        except (ValueError, TypeError):
            data = {}
        found = any(p.startswith(expected) for p in data.get('failed_predicates', []))
        controls.append({'control': name, 'exit_code': run.returncode,
                         'expected_failed_predicate': expected,
                         'failed_predicates': data.get('failed_predicates', []),
                         'passed': run.returncode == 1 and data.get('verdict') == 'FAIL' and found})
    passed = all(c['passed'] for c in controls)
    print(json.dumps({'schema': 'sc42-integration-controls-v1', 'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), 'site_table_sha256': hashlib.sha256(Path(ROOT, SITE_TABLE_PATH).read_bytes()).hexdigest(), 'controls': controls,
                      'verdict': 'PASS' if passed else 'FAIL'}, ensure_ascii=False, sort_keys=True, indent=2))
    sys.exit(0 if passed else 1)

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
diagnostic('[1] FiniteOperationalTheory fields vs GR §3.3 setting'
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
    finish()

# 2. Theorem statement unchanged (strength kept).
thm = '**Theorem (operational-completion characterization).** *For every nonempty finite visible system, the available outcome families on the system and on every positive ancilla level are exactly the normalized finite Kraus instruments if and only if conditions (i)–(v) hold.*'
diagnostic('[2] theorem statement')
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
         '*conditionally*: it holds exactly when the explicit completion principles',
         # round 5
         'on the relevant class', 'these three principles are respectively equivalent']
diagnostic('[3] re-grep')
for s in STALE:
    n = sum(read(p).count(s) for p in CORPUS)
    check(n == 0, f'stale {s!r}: {n}')
counts = {p: read(p).count('complex matrix kinematics') + read(p).count('complex matrices indexed')
          for p in CORPUS}
for p, n in counts.items():
    diagnostic(f'        kinematics mentions {p}: {n}')
SITE_TABLE = json.loads(read(SITE_TABLE_PATH))
check(SITE_TABLE.get('schema') == 'sc42-integration-sites-v1', 'intended-site table schema')
EXPECT = {p: e['expected_mentions'] for p, e in SITE_TABLE['files'].items()}
check(set(EXPECT) == set(CORPUS), 'intended-site table covers the original scientific corpus exactly')
for p, entry in SITE_TABLE['files'].items():
    lines = read(p).splitlines()
    listed = 0
    for site in entry['sites']:
        matching = [l for l in lines if l.startswith(site['anchor'])]
        check(len(matching) == 1, 'intended scope paragraph exists exactly once: ' + p + ': ' + site['anchor'][:48])
        actual = sum(l.count('complex matrix kinematics') + l.count('complex matrices indexed') for l in matching)
        check(actual == site['mentions'], 'intended scope paragraph mention count: ' + p + ': ' + site['anchor'][:48])
        check(bool(site['role'].strip()), 'intended scope paragraph rationale: ' + p + ': ' + site['anchor'][:48])
        listed += site['mentions']
    check(listed == entry['expected_mentions'], 'intended scope paragraph sum: ' + p)
base_n = sum(read(p, BASE).count('complex matrix kinematics') + read(p, BASE).count('complex matrices indexed')
             for p in CORPUS)
check(base_n == 0, f'kinematics mentions at base: {base_n}')
check(counts == EXPECT, f'kinematics mention counts match the site table ({sum(EXPECT.values())})')

# 3b. Pinned texts (round 3), with the kernel witnesses of the characterization's two directions.
diagnostic('[3b] pinned texts and witnesses')
PINS = {
 'papers/Main.md': ["the instrument algebra is reached, on a finite carrier within complex matrix kinematics taken as given, exactly when the five operational completion conditions hold ([GR §3.3]; Remark below), none of them supplied by the fixed-basis layer, and",
                    "reached, on a finite carrier within complex matrix kinematics taken as given, exactly under the operational completion conditions (§3.4; [GR §3.3])",
                    "Within the same complex matrix kinematics, observational independence is equivalent to inert spectators on every finite carrier; reversible richness implies sufficient reversible control, and conversely for well-formed theories on a nonempty carrier; observer recursion implies iterated composition, and conversely when the identity and the relative ancilla readout are available at every level, which sufficient reversible control and inert spectators supply. Hence, on every nonempty finite carrier,",
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
# Round 5: the hypotheses Main:580 states for each OI+ principle are those of the kernel converses.
cg = read('verification/lean-mathlib/OIBridge/CarrierGeneralOIPlus.lean')
co = read('verification/lean-mathlib/OIBridge/CompletedOI.lean')
check('theorem observationalIndependence_iff_inert :\n    ObservationalIndependence T ↔ InertSpectatorCompositionality T' in cg,
      'observationalIndependence_iff_inert: unconditional iff')
check('theorem control_of_reversibleRichness (h : ReversibleRichness T) :' in cg,
      'control_of_reversibleRichness: no side condition')
check('theorem reversibleRichness_of_control [Nonempty A] (hwf : WellFormed T)\n    (hctrl : HasCompositeUnitaryControl T)' in cg,
      'reversibleRichness_of_control: Nonempty A and WellFormed')
check('theorem closure_of_observerRecursion {T : FiniteOperationalTheory A} (h : ObserverRecursion T) :' in co,
      'closure_of_observerRecursion: no side condition')
m5 = re.search(r'theorem observerRecursion_of_closure .*?: ObserverRecursion T :=', co, re.S).group(0)
check('hid : ∀ n, T.availExt n Unit (fun _ => LinearMap.id)' in m5 and 'hread' in m5 and 'hclos' in m5,
      'observerRecursion_of_closure: identity and relative readout at every level')
ac = read('verification/lean-mathlib/OIBridge/AncillaClosure.lean')
check('theorem availExt_id_of_control (T : FiniteOperationalTheory A)\n    (hctrl : HasCompositeUnitaryControl T)' in ac
      and 'theorem availExt_relativeReadout (T : FiniteOperationalTheory A)\n    (hin : InertSpectatorCompositionality T)' in ac,
      'identity from control, relative readout from inert spectators')
ka = read('verification/lean-mathlib/OIBridge/KrausSoundness.lean')
check('T.avail (Fin m) F ↔ IsFiniteEndomorphicKrausInstrument F' in ka,
      'exactness is about the available families (T.avail), not a representation of a law')

# 4. Mirror parity: each changed chapter paragraph is present verbatim in FULL.
diagnostic('[4] book/FULL mirror parity')
full = read('book/The-Incompleteness-of-Observation-FULL.md')
CHAPTERS = sorted(str(p) for p in Path(ROOT, 'book').glob('*.md') if p.name not in {'README.md', 'The-Incompleteness-of-Observation-FULL.md'})
CHAPTERS = [os.path.relpath(p, ROOT) for p in CHAPTERS]
diff = subprocess.run(['git', 'diff', '-U0', BASE, '--'] + CHAPTERS,
                      capture_output=True, text=True, check=True).stdout
added = [l[1:] for l in diff.splitlines() if l.startswith('+') and not l.startswith('+++')]
for l in added:
    check(l in full, f'chapter line mirrored in FULL: {l[:60]}...')

# 5. Added-text scan over the whole diff, at word granularity so that pre-existing words on a
#    changed line are not attributed to this change (papers: register; all: revision voice, caps,
#    secrets, local paths).
diagnostic('[5] added-text scan')
diff = subprocess.run(['git', 'diff', '-U0', '--word-diff=porcelain', BASE, '--', '*.md', '*.py'],
                      capture_output=True, text=True, check=True).stdout
if MUTANT:
    extra = []
    for path, (before, after) in MUTATED_READS.items():
        extra.append('+++ b/' + path)
        extra.extend('+' + line[2:] for line in difflib.ndiff(before.splitlines(), after.splitlines()) if line.startswith('+ '))
    diff += '\n' + '\n'.join(extra)
cur = None; hits = []; scanned = 0
REGISTER = re.compile(r'should not be read|the reader should|reader should note|discipline|honest|'
                      r'temptation|stated in that register|neither borrows', re.I)
HISTORY = re.compile(r'is now settled|now settled|in its current form|the corrected form|as redefined|'
                     r'no longer|formerly|withdrawn|earlier revisions|previously stated', re.I)
CAPS = re.compile(r'(?<=[a-z,;:] )([A-Z]{4,})\b')
CAPS_OK = {'PASS', 'FAIL', 'NEW', 'POSITIVE', 'CHSH', 'CLPW'}  # CLPW names the cited GR [39] authors, not emphasis.
SECRET = re.compile(r'ghp_[A-Za-z0-9]{20,}|github_pat_|sk-[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}|'
                    r'-----BEGIN [A-Z ]*PRIVATE KEY|[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[a-z]{2,}')
LOCAL = re.compile(r'/(?:tmp|home|root|Users)/|scratch' + r'pad|[A-Z]:\\\\')
for l in diff.splitlines():
    if l.startswith('+++ b/'):
        cur = l[6:]; continue
    if not l.startswith('+') or l.startswith('+++') or cur.endswith('check_sc42.py') or cur.endswith('check_sc42_integration.py'):
        continue
    t = l[1:]; scanned += 1
    if cur.startswith('papers/') and REGISTER.search(t):
        hits.append((cur, 'register', REGISTER.search(t).group(0)))
    if cur.startswith('papers/') and HISTORY.search(t):
        hits.append((cur, 'history', HISTORY.search(t).group(0)))
    for c in CAPS.findall(t):
        if cur.startswith('papers/') and c not in CAPS_OK:
            hits.append((cur, 'caps', c))
    if SECRET.search(t):
        hits.append((cur, 'secret', SECRET.search(t).group(0)))
    if LOCAL.search(t):
        hits.append((cur, 'local-path', LOCAL.search(t).group(0)))
diagnostic(f'        scanned {scanned} added text chunk(s)')
for h in hits:
    diagnostic('        hit', h)
check(not hits, f'added-text scan: {len(hits)} hit(s)')

# Additional integration guards keep the newly repaired scientific summaries bounded.
main = read('papers/Main.md')
summary = next(l for l in main.splitlines() if l.startswith('**Theorem statement.**'))
check('with operational no-signaling required' in summary, 'Bell summary requires rather than derives no-signaling')
method = read('papers/Methodology.md')
for phrase in ['not piecemeal evasion but a single structural feature',
               'six manifestations of the same architectural feature',
               'meets all of them with one structural feature',
               'Part III\'s unifying formulation', 'by this single move']:
    check(phrase not in method, 'no automatic unified escape: ' + phrase)
check('The deterministic Bell ceiling gives' in method and 'five additional conditions that bare OI does not imply' in method,
      'Methodology substantive comparison retains distinct Bell and completion premises')
check("an unconditional Frauchiger–Renner resolution does not follow from it" in method
      and "the operational probabilities of its full protocol" in method,
      'FR scope requires the actual protocol rather than partition multiplicity')
check("Multiple partitions alone neither eliminate the joint law above nor establish failure of a Frauchiger–Renner premise." in main,
      'Main keeps the joint law and scopes FR application separately')
for path in ['papers/Methodology.md', 'papers/Main.md', 'book/appendix-c-objections.md', 'book/glossary.md', 'book/ch04-methodology.md', 'book/ch12-evolution-intelligence.md', 'book/The-Incompleteness-of-Observation-FULL.md']:
    text = read(path)
    for phrase in ['The framework therefore dissolves the Frauchiger-Renner paradox',
                   'Resolves several no-go theorems including Frauchiger-Renner',
                   'the universal description the theorem needs as its target does not exist',
                   'the substratum-emergent distinction dissolves several classical interpretive puzzles']:
        check(phrase.lower() not in text.lower(), 'no automatic FR/property-placement resolution: ' + path + ': ' + phrase[:48])
finish()
