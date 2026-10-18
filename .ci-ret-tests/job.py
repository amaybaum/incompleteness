"""One CI job (disposable harness for PR #860's retention correction). argv: <target> <kind> <name> <outdir> [<base>]
kinds:
  baseline      name: co, co-recon, co-self, cr, cr-self, cr-gate, legacy -- the seven commands at TARGET, unmutated
  regression42  the 39 prototype controls and 3 boundary controls against TARGET's real functions (<base>: 7c5f97d9)
  mutant        name: a mutant of mutants_all.py, its checker's full self-test
  cli           name: a mutant run as check_objects.py --self-test (exit code, and no traceback)
  iso           name: an isolated.py section, checked against iso-expected.json
Writes <outdir>/<kind>__<name>.log (the run's own output) and <kind>__<name>.verdict (one line), prints the verdict line
and a ::notice annotation. Statuses: PASS / FAIL (baseline, regression42, cli, iso); KILLED / SURVIVED /
INCONCLUSIVE (mutant); NOT-RUN (an infrastructure fault: exit 137, ENOSPC, 'unable to write'), never a result."""
import os, re, shutil, subprocess, sys, time

TGT, KIND, NAME, OUT = sys.argv[1:5]
BASE = sys.argv[5] if len(sys.argv) > 5 else None
H = os.path.dirname(os.path.abspath(__file__))
A = 'verification/audits/evidence-retention'
REC9 = 'verification/programmes/oi-qm/reconstruction/round-ktoken-maxcone-1/preregistration.md'
REC1 = 'verification/programmes/oi-qm/reconstruction/round-preserve-induct-1/preregistration.md'
MIN_CASES = {'co-self': 120, 'cr-self': 188}
os.makedirs(OUT, exist_ok=True)
tag = '%s__%s' % (KIND, NAME.replace(':', '_'))
tmp = os.path.join(OUT, 'tmp-' + tag)
os.makedirs(tmp, exist_ok=True)
env = dict(os.environ, TMPDIR=tmp)


def run(argv, cwd):
    s = time.time()
    p = subprocess.run(argv, cwd=cwd, capture_output=True, text=True, env=env)
    return p.returncode, p.stdout + ('\n--- stderr ---\n' + p.stderr if p.stderr else ''), time.time() - s


def co_names(out):
    rows = [l for l in out.split('\n') if l.startswith('  ') and
            re.search(r'\s(FAILS as required|PASSES as required|NOT DETECTED|FAILS)(\s|$)', l)]
    for w in range(1, 400):
        if rows and all(len(l) > w + 4 and l[2 + w:4 + w] == '  ' and l[4 + w] != ' ' for l in rows):
            return [l[2:2 + w].rstrip() for l in rows], [l for l in rows if 'as required' not in l]
    return [], rows


def cr_names(out):
    return [m.group(2) for m in re.finditer(r'^(PASS|FAIL) self: (.*)$', out, re.M)], \
        [l for l in out.split('\n') if l.startswith('FAIL self: ')]


py = [sys.executable, '-I', '-B']
detail = ''
if KIND == 'baseline':
    argv = {'co': [A + '/check_objects.py'], 'co-recon': [A + '/check_objects.py', '--reconstitute'],
            'co-self': [A + '/check_objects.py', '--self-test'], 'cr': [A + '/check_retention.py'],
            'cr-self': [A + '/check_retention.py', '--self-test'], 'cr-gate': [A + '/check_retention.py', '--gate'],
            'legacy': ['tools/legacy_records_check.py',
                       subprocess.run(['git', '-C', TGT, 'rev-parse', 'HEAD'], capture_output=True,
                                      text=True).stdout.strip()]}[NAME]
    rc, text, el = run(py + argv, TGT)
    ok = rc == 0
    key = {'co': r'check_objects: \S+', 'co-recon': r'reconstituted: .*', 'co-self': r'self-test: .*',
           'cr': r'RETENTION  (HOLDS|FAILS).*', 'cr-self': r'self-test: \S+', 'cr-gate': r'EVIDENCE-RETENTION  .*',
           'legacy': r'LEGACY  .*'}[NAME]
    m = re.findall(key, text)
    detail = m[-1] if m else '(no result line)'
    if NAME in MIN_CASES:
        names, red = (co_names if NAME == 'co-self' else cr_names)(text)
        prev = open(os.path.join(H, '%s-names-d3d09572.txt' % NAME[:2]), encoding='utf-8').read().split('\n')
        dropped = [n for n in prev if n and n not in set(names)]
        ok = ok and not red and len(names) >= MIN_CASES[NAME] and not dropped and len(names) == len(set(names))
        detail += '; %d cases (minimum %d), %d red, %d of d3d09572\'s cases missing%s' % (
            len(names), MIN_CASES[NAME], len(red), len(dropped), (': ' + '; '.join(dropped[:5])) if dropped else '')
    if NAME == 'cr-gate':
        ok = ok and 'EVIDENCE-RETENTION  HOLDS' in text
    status = 'PASS' if ok else 'FAIL'
elif KIND == 'regression42':
    rf = os.path.join(OUT, 'rf')
    os.makedirs(rf, exist_ok=True)
    for name, spec, blob in (('r829.md', 'e12c1573dc1605baf6ed299f9fe11cdb31ef56ee:' + REC9,
                              'ffbcab2918a4e1e7594f7ab4b827b70bb25b9f9f'),
                             ('r831.md', '65b85147f85aa01770e0e60551152bc5f1d9ef29:' + REC1,
                              '096f14170e1b6198e862131da5455c4ed2a57436')):
        data = subprocess.run(['git', '-C', TGT, 'show', spec], capture_output=True).stdout
        open(os.path.join(rf, name), 'wb').write(data)
        got = subprocess.run(['git', '-C', TGT, 'hash-object', os.path.join(rf, name)], capture_output=True,
                             text=True).stdout.strip()
        assert got == blob, (name, got, blob)
    rc, text, el = run(py + [os.path.join(H, 'cn3_real.py'), BASE, rf, TGT, OUT], TGT)
    m = re.findall(r'controls: (\d+), mismatches: (\d+)', text)
    detail = 'controls %s, mismatches %s' % m[-1] if m else '(no result line)'
    status = 'PASS' if rc == 0 and m and m[-1] == ('42', '0') else 'FAIL'
elif KIND == 'mutant':
    rc, text, el = run(py + [os.path.join(H, 'mutants_all.py'), TGT, NAME, OUT], TGT)
    v = re.findall(r'^%s: (KILLED|SURVIVED|INCONCLUSIVE \(crash\))$' % re.escape(NAME), text, re.M)
    head = re.search(r'self-test rc (.*?); red cases (\d+)', text)
    status = 'INCONCLUSIVE' if (v and v[-1].startswith('INCONCLUSIVE')) or not v else v[-1]
    detail = 'self-test rc %s, red cases %s' % (head.group(1), head.group(2)) if head else '(no outcome line)'
elif KIND == 'cli':
    rc, text, el = run(py + [os.path.join(H, 'crash_family.py'), TGT, NAME, 'cli', OUT], TGT)
    side = open(os.path.join(OUT, NAME + '.cli.out'), encoding='utf-8', errors='replace').read() \
        if os.path.exists(os.path.join(OUT, NAME + '.cli.out')) else ''
    m = re.search(r'cli: exit (\d+); stdout case lines (\d+)', text)
    tb = 'Traceback' in side
    detail = ('cli exit %s, %s case lines, %s' % (m.group(1), m.group(2), 'TRACEBACK' if tb else 'no traceback')) if m \
        else '(no result line)'
    # the mutant must make the self-test fail case by case: a non-zero exit with its cases reported, never a crash
    status = 'PASS' if m and m.group(1) == '1' and int(m.group(2)) > 0 and not tb else 'FAIL'
    text += '\n--- cli output ---\n' + side
elif KIND == 'iso':
    rc, text, el = run(py + [os.path.join(H, 'isolated.py'), TGT, tmp, NAME], TGT)
    open(os.path.join(OUT, tag + '.iso.out'), 'w', encoding='utf-8').write(text)
    rc2, text2, _ = run(py + [os.path.join(H, 'iso_parse.py'), os.path.join(H, 'iso-expected.json'),
                              os.path.join(OUT, tag + '.iso.out')], TGT)
    text += '\n--- check ---\n' + text2
    detail = (text2.strip().split('\n') or [''])[-1]
    status = 'PASS' if rc == 0 and rc2 == 0 else 'FAIL'
else:
    sys.exit('unknown kind %s' % KIND)
infra = rc == 137 or any(x in text for x in ('No space left', 'Errno 28', 'unable to write'))
if infra:
    status, detail = 'NOT-RUN', 'infrastructure fault (exit %s); ' % rc + detail
line = '%s %s %s (%ds) %s' % (KIND, NAME, status, el, detail)
open(os.path.join(OUT, tag + '.log'), 'w', encoding='utf-8').write(line + '\n' + text)
open(os.path.join(OUT, tag + '.verdict'), 'w', encoding='utf-8').write(line + '\n')
shutil.rmtree(tmp, ignore_errors=True)
print('VERDICT ' + line)
print('::notice title=%s %s::%s' % (KIND, NAME, line.replace('%', '%25').replace('\n', '%0A')))
sys.exit(0 if status in ('PASS', 'KILLED') else 1)
