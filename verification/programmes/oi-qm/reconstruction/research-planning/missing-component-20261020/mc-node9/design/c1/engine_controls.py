"""Engine controls for search3.py / search4.py (must pass before their null results count).

PC-1 (positive): replace the lattice update by the target coupling itself on n = 2
      (toy site 0 hidden; pointer site 1 with Q = u1 visible, P = v1 hidden), u = (1,0),
      (q,p) = (u0,v0).  Both engines must report E with clean records at k = 1, ops = none.
PC-2 (positive, needs an observer operation): n = 3, site 2 fully visible idle; the "update"
      is the target composed with a visible swap Q <-> u2.  Ops = none must fail at k = 1;
      ops = cell and GL must find E at k = 1 (the final visible operation undoes the swap).
PC-3 (positive): each of the three read functionals (u_toy, v_toy, u_toy+v_toy) is detected by
      search5.py when the "update" is the corresponding target.
LC-1 (leak): the target followed by the symplectic exchange (Q, P) -> (P, Q) on the pointer
      site; the designated rows then differ, and the record reveals P: no record-safe class
      may survive, so both engines must report nothing.
"""
from search2 import Cfg
import search3, search4
from f2 import compose, is_symplectic

def target_matrix(n, uq, up, Qc, Pc, q=0, p=None):
    p = n if p is None else p
    rows = [1 << i for i in range(2 * n)]
    rows[Qc] = (1 << Qc) | (up << q) | (uq << p)
    rows[q] = (1 << q) | (uq << Pc)
    rows[p] = (1 << p) | (up << Pc)
    rows[Pc] = 1 << Pc
    return tuple(rows)

def run_both(cfg, cls):
    r3, _ = search3.run_cfg(cfg, cls, kmax=2)
    vc = search4.VCfg(cfg)
    _, G = search4.op_bits(cls, cfg.dv)
    r4, _ = search4.run(vc, cls, G, kmax=2)
    out = {}
    for k in (1, 2):
        a = sorted(set((tl, d) for (tl, d, key) in r3[k][1]))
        b = sorted(set(x for row in r4[k] for x in search4.final_check(vc, cls, row)))
        out[k] = (a, b, r3[k][0], r4[k].shape[0])
    return out

ok = True
# PC-1
n = 2
cfg = Cfg(n, (), [1], 1, 3, "PC-1")
cfg.M = target_matrix(n, 1, 0, 1, 3)
print("PC-1 target matrix symplectic:", is_symplectic(cfg.M, n))
for cls in ("none", "cell", "GL"):
    o = run_both(cfg, cls)
    a, b, s3, s4 = o[1]
    found = any(d == "E" and "u=(1, 0)" in tl and "(u0,v0)" in tl for (tl, d) in a)
    print(f"  ops={cls} k=1: search3={a} search4={b} classes {s3}/{s4}")
    ok &= found and a == b and s3 == s4
# PC-2
n = 3
vis = [1, 2, 5]
cfg = Cfg(n, (), vis, 1, 4, "PC-2")
T = target_matrix(n, 1, 0, 1, 4)
swap = list(range(6)); swap[1], swap[2] = 2, 1
S = tuple(1 << swap[i] for i in range(6))
cfg.M = compose(S, T)
for cls in ("none", "cell", "GL"):
    o = run_both(cfg, cls)
    a, b, s3, s4 = o[1]
    found = any(d == "E" and "u=(1, 0)" in tl and "(u0,v0)" in tl for (tl, d) in a)
    want = (cls != "none")
    print(f"PC-2 ops={cls} k=1: search3={a} search4={b} classes {s3}/{s4}  expected E: {want}")
    ok &= (found == want) and a == b and s3 == s4
# LC-1
n = 2
cfg = Cfg(n, (), [1], 1, 3, "LC-1")
T = target_matrix(n, 1, 0, 1, 3)
X = list(1 << i for i in range(4)); X[1], X[3] = 1 << 3, 1 << 1
cfg.M = compose(tuple(X), T)
print("LC-1 map symplectic:", is_symplectic(cfg.M, n))
for cls in ("none", "GL"):
    o = run_both(cfg, cls)
    for k in (1, 2):
        a, b, s3, s4 = o[k]
        print(f"  ops={cls} k={k}: search3={a} search4={b} record-safe classes {s3}/{s4}")
        ok &= (a == [] and b == [] and s3 == 0 and s4 == 0)
# PC-3: every read functional is detectable (u = (1,0), (0,1), (1,1)), via search5's relabelled check
import search5
for (uq, up, fname) in ((1, 0, "v_toy"), (0, 1, "u_toy"), (1, 1, "u_toy+v_toy")):
    n = 2
    cfg = Cfg(n, (), [1], 1, 3, "PC-3")
    cfg.M = target_matrix(n, uq, up, 1, 3)
    vc = search4.VCfg(cfg)
    r4, _ = search4.run(vc, "none", search4.op_bits("none", 1)[1], kmax=1)
    hits = set((fn, d) for row in r4[1] for (fn, d, oa) in search5.final_check_relabel(vc, "none", row, "relaxed", search5.out_assignments(cfg, "relaxed")))
    print(f"PC-3 target u=({uq},{up}) in (q,p)=(u0,v0): search5 reports {sorted(hits)}")
    ok &= (fname, "E") in hits
print("ENGINE CONTROLS:", "GREEN" if ok else "RED")
