"""Run the landed V3 verifier's control-plane and execution predicates on a local chain (executor evidence only).
usage: v3local.py <repo> <D> <F> <E>"""
import importlib.util, sys
repo_dir, D, F, E = sys.argv[1:5]
spec = importlib.util.spec_from_file_location('v3', repo_dir + '/tools/v3_verifier.py')
v3 = importlib.util.module_from_spec(spec); spec.loader.exec_module(v3)
repo = v3.Repo(repo_dir)
D, F, E = repo.need(D), repo.need(F), repo.need(E)
rdir, rid, kind, entries, files, codes = v3.control_plane(repo, D, F)
print('control_plane:', rdir, rid, kind, 'codes', codes)
print('governed entries:', entries)
print('t1:', v3.check_t1(repo, D, F, files))
own = ('verification/receipts/%s.json' % rid, None)
print('execution F..E:', v3.check_execution(repo, F, E, rdir, entries, own))
