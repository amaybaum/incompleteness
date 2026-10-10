#!/usr/bin/env python3
"""Scratch: apply V3-12's two stage commits from exactly F, reading every frozen value back from the
preregistration as it stands at F; refuse on any mismatch. Never landed.
Usage: exec312.py <F> <census.py source>"""
import hashlib, json, os, re, shutil, subprocess, sys, tempfile
REPO = '/home/user/incompleteness'
F, SRC = sys.argv[1], sys.argv[2]
RD = 'verification/infrastructure/round-v3-12-retirement-census/'
def git(*a):
    return subprocess.run(['git', '-C', REPO] + list(a), check=True, capture_output=True).stdout.decode()
def die(m):
    raise SystemExit('exec312: REFUSED: ' + m)
if git('rev-parse', 'HEAD').strip() != F or git('status', '--porcelain').strip():
    die('the checkout is not exactly F, clean')
text = git('show', '%s:%spreregistration.md' % (F, RD))
D = re.search(r'`D` = `([0-9a-f]{40})`', text).group(1)
tool_blob = re.search(r'adds `census\.py` to the record directory, blob\s+`([0-9a-f]{40})`', text).group(1)
tool_sha = re.search(r'SHA-256\s+`([0-9a-f]{64})`', text).group(1)
cen_blob = re.search(r'`census\.json`, blob `([0-9a-f]{40})`', text).group(1)
leg_blob = re.search(r'`legacy-records\.json`, blob\s+`([0-9a-f]{40})`', text).group(1)
selftest = re.search(r'`census\.py --self-test` prints `([^`]+)`', text).group(1)
cmd = re.search(r'adds the output of `python3 census\.py \. ([0-9a-f]{40})\s+(\S+)`', text)
if cmd.group(1) != D or cmd.group(2) != RD or git('rev-parse', F + '^').strip() != D:
    die('the frozen command or D disagrees')
data = open(SRC, 'rb').read()
if hashlib.sha256(data).hexdigest() != tool_sha:
    die('census.py SHA-256')
dst = os.path.join(REPO, RD, 'census.py')
open(dst, 'wb').write(data)
if git('hash-object', '--no-filters', dst).strip() != tool_blob:
    die('census.py blob')
r = subprocess.run([sys.executable, dst, '--self-test'], cwd=REPO, capture_output=True, text=True)
line = r.stdout.strip().split('\n')[-1]
print('C1 blob %s sha256 %s' % (tool_blob[:12], tool_sha[:12]))
print('C2', line)
if r.returncode or line != selftest:
    die('self-test')
git('add', RD + 'census.py')
msg1 = ('V3-12 stage 1: the census tool\n\nAdds census.py to the record directory, byte-identical to the '
        'content the\npreregistration freezes at F.\n\nCo-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>\n'
        'Claude-Session: https://claude.ai/code/session_01XEQMD5kRhaU9WyeZt6dmM1\n')
subprocess.run(['git', '-C', REPO, 'commit', '-q', '-F', '-'], input=msg1.encode(), check=True)
S1 = git('rev-parse', 'HEAD').strip()
r = subprocess.run([sys.executable, RD + 'census.py', '.', D, RD], cwd=REPO, capture_output=True, text=True)
print(r.stdout.strip())
if r.returncode:
    die('the census run: ' + r.stderr[-400:])
b1 = git('hash-object', '--no-filters', RD + 'census.json').strip()
b2 = git('hash-object', '--no-filters', RD + 'legacy-records.json').strip()
print('C3 census.json %s  legacy-records.json %s' % (b1, b2))
if b1 != cen_blob or b2 != leg_blob:
    die('output blobs')
tmp = tempfile.mkdtemp()
r = subprocess.run([sys.executable, RD + 'census.py', '.', D, tmp], cwd=REPO, capture_output=True)
for n in ('census.json', 'legacy-records.json'):
    if open(os.path.join(tmp, n), 'rb').read() != open(os.path.join(REPO, RD, n), 'rb').read():
        die('rerun differs: ' + n)
print('C3 a second run gives the same bytes')
shutil.rmtree(tmp)
c = json.load(open(os.path.join(REPO, RD, 'census.json')))
lr = json.load(open(os.path.join(REPO, RD, 'legacy-records.json')))
ok = (len(c['predicates']) == 4202 and c['guard']['accumulator_writes'] == 4199
      and c['legacy_records']['v2_pins_agreeing'] == 199 and len(lr['records']) == 303
      and len(lr['closed_namespaces']) == 75
      and c['guard']['dispositions'] == {'removed whole': 14, 'retained whole': 50, 'split': 41}
      and c['guard']['totals'] == {'redundant': 1268, 'retain': 2492, 'retire-history': 291,
                                   'retire-machinery': 49, 'retire-whole': 2, 'structural': 100})
print('C4', 'as frozen' if ok else 'DIFFERS')
if not ok:
    die('figures')
git('add', RD + 'census.json', RD + 'legacy-records.json')
msg2 = ('V3-12 stage 2: the census at D\n\nAdds census.json and legacy-records.json, the output of census.py '
        'run at\nthe stage 1 commit against D, with the blobs the preregistration predicts.\n\n'
        'Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>\n'
        'Claude-Session: https://claude.ai/code/session_01XEQMD5kRhaU9WyeZt6dmM1\n')
subprocess.run(['git', '-C', REPO, 'commit', '-q', '-F', '-'], input=msg2.encode(), check=True)
S2 = git('rev-parse', 'HEAD').strip()
print('STAGE1 %s\nSTAGE2 %s' % (S1, S2))
