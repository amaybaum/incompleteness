"""Countercontrol scan: two mutants of the prototype over every shard-4 row set where the landed search prunes.
M1 (BROKEN, as dfsR2's own flag): prune on constancy alone. M2: drop the assigned rows' contribution (fixedsum = 0).
Reports how many row sets each mutant changes (nodes, pruned, leaves) relative to the landed counts."""
import sys, runpy, json, time
tools = sys.argv[1]
sys.argv = ['dfs_proto.py', '4', tools, '0', 'new']
ns = runpy.run_path(__file__.replace('dfs_counter2.py', 'dfs_proto.py'), run_name='proto')
Fast, np, NK = ns['RSearch2Fast'], ns['np'], len(ns['AR'])
class M1(Fast):
    def _dita_subtree(self, cand, fixedsum):
        const = np.ones(NK, dtype=bool)
        for r, c in cand.items():
            sub = self.ids[r][c]; const &= sub.min(axis=0) == sub.max(axis=0)
        return int(np.flatnonzero(const)[0]) if const.any() else None
class M2(Fast):
    def _dita_subtree(self, cand, fixedsum):
        return Fast._dita_subtree(self, cand, np.zeros_like(fixedsum))
per = json.load(open(sys.argv[0].replace('dfs_proto.py', '') + 'dfs4_proto_per.json' if False else
                     __file__.replace('dfs_counter2.py', 'dfs4_proto_per.json')))
rows = [r for r in per if r['old'][2] > 0 and r['R'] not in (0xfafa, 0xafaf)]
ch = {'M1': 0, 'M2': 0}; t0 = time.time()
for r in rows:
    want = tuple(r['old'][1:])
    for nm, cls in (('M1', M1), ('M2', M2)):
        S = cls(r['R'], 39, True); S.run()
        if (S.nodes, S.pruned, len(S.leaves)) != want:
            ch[nm] += 1
            if ch[nm] <= 3: print(nm, hex(r['R']), 'landed', want, 'mutant', (S.nodes, S.pruned, len(S.leaves)), flush=True)
print('row sets scanned %d; changed by M1 %d, by M2 %d (%.0fs)' % (len(rows), ch['M1'], ch['M2'], time.time() - t0))
