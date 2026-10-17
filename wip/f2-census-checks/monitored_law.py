#!/usr/bin/env python3
"""monitored_law.py -- audit check B (exact, q = 3, N = 1). Decides nothing for any round.

Question: does E1's registration (Lueders, i.e. F2-5's re-randomizing readout) reproduce OI's
multi-time visible law, the trajectory law P(x0, x1, x2) read off a reversible system under
incomplete observation ([Main] Sec. 3.4 class (D); kernel RevReal.traj, Equivalence.lean:174)?
Three laws for the leap L_m(x, xi) = (m x - xi, x), registered start x0 = a, hidden xi0 uniform:
  (OI)  classical trajectory law, x1 and x2 read without disturbance;
  (RR)  classical law with the hidden half re-randomized at the t = 1 registration (F2-5 T'_k);
  (QM)  E1's quantum law: |a><a|, Weil-covariant unitary V_m, Lueders P_k at t = 1, P_l at t = 2.
Controls: the unmonitored rooted law P(x2 | x0) is computed both classically and quantumly and
must agree (F2-1 C1 (ii) at word length 2); V_m is checked covariant, V A(z) V^dag = lam A(L z).
"""
import contextlib, hashlib, io, sys
from fractions import Fraction
from itertools import product
MAIN = sys.argv[1]
PIN = '211ce708440e3f6fd02558113dcb1aea2ca3723da780f0c32c838b3a454f6b04'
src = open(MAIN, encoding='utf-8').read()
assert hashlib.sha256(src.encode('utf-8')).hexdigest() == PIN, 'pin'
ns = {'__name__': 'f2_5_defs'}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(src[:src.index('# ---------------------------------------------------------------- K-order')], MAIN, 'exec'), ns)
g = ns
PTS1, D1, A1, K, zeros, add, mm, dag, scal, meq, tr, eye, E = (g[k] for k in
    ('PTS1', 'D1', 'A1', 'K', 'zeros', 'add', 'mm', 'dag', 'scal', 'meq', 'tr', 'eye', 'E'))
q = 3
ok = True
for m in range(q):
    L = lambda z, m=m: ((m * z[0] - z[1]) % q, z[0])
    V = zeros(3)
    for z in PTS1:
        V = add(V, mm(D1[L(z)], dag(D1[z])))
    VV = mm(V, dag(V)); lam = VV[0][0]
    cov = (not lam.iszero()) and lam.is_real() and lam.a > 0 and meq(VV, scal(lam, eye(3)))
    cov &= all(meq(mm(mm(V, A1[z]), dag(V)), scal(lam, A1[L(z)])) for z in PTS1)
    ok &= cov
    ev = lambda rho: scal(K(1) / lam, mm(mm(V, rho), dag(V)))
    P = [E(k, k) for k in range(q)]
    diffs = 0; mem_oi = False; mem_qm = False
    for a in range(q):
        oi, rr, qm = {}, {}, {}
        for k, l in product(range(q), repeat=2):
            oi[(k, l)] = Fraction(0); rr[(k, l)] = Fraction(0)
        for xi0 in range(q):
            x1, xi1 = L((a, xi0)); x2, _ = L((x1, xi1))
            oi[(x1, x2)] += Fraction(1, q)
            for xir in range(q):                       # re-randomized hidden half at t = 1
                y2, _ = L((x1, xir)); rr[(x1, y2)] += Fraction(1, q * q)
        rho0 = E(a, a)
        r1 = ev(rho0)
        for k in range(q):
            rk = mm(mm(P[k], r1), P[k]); r2 = ev(rk)
            for l in range(q):
                p = tr(mm(mm(P[l], r2), P[l])); assert p.is_real()
                qm[(k, l)] = p.a
        # unmonitored control: P(x2 | x0) classical vs quantum
        r2u = ev(ev(rho0))
        for l in range(q):
            pc = sum(v for (k, l2), v in oi.items() if l2 == l)
            pq = tr(mm(mm(P[l], r2u), P[l])); ok &= pq.is_real() and pq.a == pc
        ok &= all(qm[x] == rr[x] for x in qm)
        diffs += sum(qm[x] != oi[x] for x in qm)
        # readback: does P(x2 | x1, x0) depend on x0?  record conditionals for comparison across a
        g.setdefault('cond', {}).setdefault(m, {})[a] = (
            {k: tuple(oi[(k, l)] / sum(oi[(k, j)] for j in range(q)) if sum(oi[(k, j)] for j in range(q)) else None for l in range(q)) for k in range(q)},
            {k: tuple(qm[(k, l)] / sum(qm[(k, j)] for j in range(q)) for l in range(q)) for k in range(q)})
    c = g['cond'][m]
    for k in range(q):
        oi_rows = {c[a][0][k] for a in range(q) if c[a][0][k][0] is not None}
        qm_rows = {c[a][1][k] for a in range(q)}
        mem_oi |= len(oi_rows) > 1; mem_qm |= len(qm_rows) > 1
    print('m=%d  covariant V: %s   QM == re-randomized classical: yes   entries QM != OI: %d of 27   '
          'P(x2|x1,x0) depends on x0 -- OI: %s, QM: %s' % (m, cov, diffs, mem_oi, mem_qm))
    ok &= diffs > 0 and mem_oi and not mem_qm
print('CHECK-B', 'PASS' if ok else 'FAIL', ': E1 registration reproduces the rooted law but not OI\'s monitored '
      'trajectory law; the readback dependence of x2 on x0 given x1 is present in OI and absent under E1')
