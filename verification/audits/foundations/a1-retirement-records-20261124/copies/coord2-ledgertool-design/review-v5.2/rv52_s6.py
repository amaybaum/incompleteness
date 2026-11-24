"""S6: reproduce the drift writer's probe landing independently from git objects and apply DESIGN-v5.2
sec. 13.1/13.3 rules to it: composed blob (M's AGENTS.md with C's splices at M-translated offsets) versus the
probe's landing blob (X's copy) and the probe record's l."""
import sys, os, json, hashlib, subprocess
REPO = '<repo>'
H = '53c6601a10419b6b333cc992474272501ab542af'; T = '14ac71b4b0a0c0aa2d7068d6799a73f474097060'
MAIN = '8e9b83341cf5bc7fd9fb260892d0385fc9bfab4d'
def show(c, p): return subprocess.run(['git', '-C', REPO, 'show', '%s:%s' % (c, p)], capture_output=True, check=True).stdout
def gid(b): return hashlib.sha1(b'blob %d\0' % len(b) + b).hexdigest()
led = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'ledger.json')))
hb, mb, xb = show(H, 'AGENTS.md'), show(MAIN, 'AGENTS.md'), show(T, 'AGENTS.md')
sp = [s for s in led['splices'] if s['file'] == 'AGENTS.md']
# translate each splice: its old bytes must occur exactly once at H and at M
out = mb; delta = 0; trans = []
for s in sorted(sp, key=lambda s: s['start']):
    old = hb[s['start']:s['end']]
    assert hb.count(old) == 1 and mb.count(old) == 1, s['id']
    assert hashlib.sha256(old).hexdigest() == s['old_sha256']
    pos = mb.index(old); trans.append((s['id'], s['start'], pos))
newb = mb
for sid, st, pos in sorted(trans, key=lambda t: -t[2]):
    s = [x for x in sp if x['id'] == sid][0]
    newb = newb[:pos] + s['new'].encode() + newb[pos + (s['end'] - s['start']):]
comp = newb
print('splices on AGENTS.md', [(t[0], t[1], t[2]) for t in trans])
print('H', gid(hb)[:10], 'M', gid(mb)[:10], 'X', gid(xb)[:10], 'composed', gid(comp)[:10], len(comp))
probe_L = xb; probe_l = gid(xb)
print('probe landing blob == composed?', gid(probe_L) == gid(comp), '-> sec. 13.1 composition: FAIL landing-conflict-unresolved' if gid(probe_L) != gid(comp) else '')
print("probe record l == composed?", probe_l == gid(comp), "-> sec. 13.3 R7 / S6: record-invalid, record does not apply" if probe_l != gid(comp) else '')
print('M change lost in probe landing?', mb[46677:47031] not in probe_L, '; retirement change present?', s['new'].encode() in probe_L)
print('composed keeps M change:', mb[46677:47031] in comp, 'and D296 image:', sp[0]['new'].encode() in comp)
