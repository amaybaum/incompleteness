"""Countercontrol for the dfs prototype: a mutated RSearch2Fast whose Lemma NS test drops the zero-sum condition must
change node/pruned counts on row sets where the landed search prunes (else the per-R count comparison is vacuous)."""
import sys, runpy, time
sys.argv = ['dfs_proto.py', '4', sys.argv[1], '0', 'new']        # limit 0: load definitions, run nothing
ns = runpy.run_path(sys.argv[0] if False else __file__.replace('dfs_counter.py', 'dfs_proto.py'), run_name='proto')
Fast, Old, np = ns['RSearch2Fast'], ns['RSearch2'], ns['np']
class Broken(Fast):
    def _dita_subtree(self, cand, fixedsum):              # mutant: drops the assigned rows' contribution
        return Fast._dita_subtree(self, cand, np.zeros_like(fixedsum))
for R in (0x7777, 0xbfbe, 0xd7d7):
    out = []
    for cls in (Old, Fast, Broken):
        t = time.perf_counter(); S = cls(R, 39, True); S.run(); out.append((S.nodes, S.pruned, len(S.leaves), round(time.perf_counter() - t, 1)))
    print(hex(R), 'landed', out[0], 'prototype', out[1], 'mutant', out[2], 'proto==landed', out[0][:3] == out[1][:3], 'mutant differs', out[0][:3] != out[2][:3], flush=True)
