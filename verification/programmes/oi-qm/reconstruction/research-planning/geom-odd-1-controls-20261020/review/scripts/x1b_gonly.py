# countercontrol: the G-side tight rows alone must NOT admit a Stiemke certificate (R is a vertex of a polytope, not isolated in it)
import sys, runpy
sys.argv = ['x1_exact.py', sys.argv[1], '/dev/null']
src = open('scripts/x1_exact.py').read().split('# ---- Stiemke')[0]
g = {}
exec(compile(src, 'x1', 'exec'), g)
import numpy as np
from scipy.optimize import linprog
for name, rows in (('G-only', g['rowsG']), ('H-only', g['rowsH'])):
    A = np.array(rows, float); m = len(rows)
    c = np.zeros(m + 1); c[-1] = -1
    Aeq = np.zeros((A.shape[1] + 1, m + 1)); Aeq[:-1, :m] = A.T; Aeq[-1, :m] = 1
    beq = np.zeros(A.shape[1] + 1); beq[-1] = m
    res = linprog(c, A_ub=np.hstack([-np.eye(m), np.ones((m, 1))]), b_ub=np.zeros(m), A_eq=Aeq, b_eq=beq,
                  bounds=[(0, None)] * m + [(None, None)], method='highs')
    # witness direction: find delta with rows.delta >= 0, sum = 1 (Farkas alternative)
    r2 = linprog(np.zeros(A.shape[1]), A_ub=-A, b_ub=np.zeros(m), A_eq=A.sum(0, keepdims=True), b_eq=[1.0],
                 bounds=[(None, None)] * A.shape[1], method='highs')
    print(name, ': Stiemke LP status', res.status, '(0 optimal, 2 infeasible)', 't*' if res.status == 0 else '', res.x[-1] if res.status == 0 else '', '; feasible direction with rows>=0, sum=1: status', r2.status)
