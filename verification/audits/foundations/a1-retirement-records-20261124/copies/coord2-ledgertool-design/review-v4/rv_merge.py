"""Check region mergers per sec. 3.2 definition: same post-region at the same step."""
import sys, os, json, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rv_git as g, rv_hp as hp
res = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'out-hp.json')))
groups = collections.defaultdict(list)
for r in res:
    if r['status'] != 'changed': continue
    s = hp.SM[r['idx']]; w = hp.walk(s)
    for k, st in enumerate(w['steps']):
        groups[(s['file'], st['commit'], tuple(st['post']))].append((s['line'], k))
n = 0
for key, v in groups.items():
    if len(v) > 1:
        n += 1
        r0 = [r for r in res if r['file'] == key[0] and r['line'] == v[0][0]][0]
        print(key[0], key[1][:8], 'sites', [x[0] for x in v], 'post lines', len(key[2]), 'H', r0.get('H_lines'), 'overlap', r0.get('overlap'))
print('merger groups', n)
