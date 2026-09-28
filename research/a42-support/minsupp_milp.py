"""Minimal support over the gauge class by integer programming (HiGHS), as an independent method to minsupp.py:
maximise sum z_ij subject to |E_ij + a_i + b_j| <= M (1 - z_ij), a_0 = 0, integer potentials in [-P, P].
The returned potentials are re-applied in exact integer arithmetic, so the upper bound (support attained) is exact;
the optimality (lower bound) rests on the solver's branch-and-bound certificate (mip_gap = 0).
Box: within one component of the zero graph the potentials spread by at most 2*15*max|E|; components can be shifted
into a common box without losing zeros, so P = 32*max|E| + 2 is without loss of generality."""
import sys, numpy as np, highspy

def min_support_milp(E, time_limit=600):
    E = np.array(E, dtype=np.int64); n = 16; mx = int(np.abs(E).max()) or 1
    P = 32 * mx + 2; M = 2 * P + mx + 1
    h = highspy.Highs(); h.setOptionValue('output_flag', False)
    h.setOptionValue('mip_rel_gap', 0.0); h.setOptionValue('mip_abs_gap', 0.0); h.setOptionValue('time_limit', float(time_limit))
    inf = highspy.kHighsInf
    # variables: a_0..a_15, b_0..b_15, z_00..z_ff
    for k in range(32): h.addVar(-P if k else 0, P if k else 0)
    for k in range(256): h.addVar(0, 1)
    h.changeColsIntegrality(288, np.arange(288, dtype=np.int32), np.array([highspy.HighsVarType.kInteger] * 288))
    h.changeColsCost(256, np.arange(32, 288, dtype=np.int32), -np.ones(256))
    for i in range(n):
        for j in range(n):
            z = 32 + i * 16 + j
            # E + a_i + b_j + M z <= M ;  -(E + a_i + b_j) + M z <= M
            h.addRow(-inf, M - E[i, j], 3, np.array([i, 16 + j, z], dtype=np.int32), np.array([1.0, 1.0, M]))
            h.addRow(-inf, M + E[i, j], 3, np.array([i, 16 + j, z], dtype=np.int32), np.array([-1.0, -1.0, M]))
    h.run()
    st = h.getModelStatus(); sol = h.getSolution().col_value
    a = np.rint(sol[:16]).astype(np.int64); b = np.rint(sol[16:32]).astype(np.int64)
    Estar = E + a[:, None] + b[None, :]
    info = h.getInfo()
    return int((Estar != 0).sum()), Estar, str(st), info.mip_dual_bound, info.objective_function_value

if __name__ == '__main__':
    import pickle
    from lib42 import A38, WIT38
    for nm, E in (('A', A38), ('act-38 witness', WIT38)):
        s, Es, st, db, ob = min_support_milp(E)
        print(nm, 'min support', s, 'status', st, 'dual bound zeros', db, flush=True)
        if nm != 'A':
            for r in Es: print(' '.join('%2d' % x for x in r))
    for f in sys.argv[1:]:
        d = pickle.load(open(f, 'rb')); X = np.array([x for R, x in d['nond']])
        s, Es, st, db, ob = min_support_milp(X[0].reshape(16, 16))
        print(f, 'leaf 0 support', int((X[0] != 0).sum()), 'min support', s, 'status', st, 'dual bound zeros', db, flush=True)
