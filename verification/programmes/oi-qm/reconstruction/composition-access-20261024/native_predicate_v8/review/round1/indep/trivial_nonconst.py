"""Reviewer: cells trivial given V but not constant. python3 -I -B trivial_nonconst.py <rederive.py> seed"""
import sys, importlib.util
spec = importlib.util.spec_from_file_location('rd', sys.argv[1]); rd = importlib.util.module_from_spec(spec); spec.loader.exec_module(rd)
seed = int(sys.argv[2]); prev, cur = rd.background(seed)
for f in rd.src: cur.pop(f, None)
F = rd.evolve_all(prev, cur)
get = lambda t, x: F[t][x[0]+4, x[1]+4, x[2]+4, :].tolist()
V = get(rd.n+2, (0,0,0))
for t in range(-1, rd.tend+1):
    for x in rd.region:
        w = get(t, x)
        if len(set(w)) > 1 and all(len({w[l] for l in range(512) if V[l] == v}) == 1 for v in range(8)):
            print(seed, x, t)
