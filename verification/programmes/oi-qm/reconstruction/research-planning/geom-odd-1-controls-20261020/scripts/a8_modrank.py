"""A8: exact (modular) rank of the tight rows at the reference gate, vectorised; and the maximal margin of the
full pool-A posFwd polytope over the non-forced rows (one LP).  rank_p <= rank_Q, so rank_p == dim F certifies over Q
that the reference is the unique point of F on which all its G-side tight constraints vanish (a vertex of P_A)."""
import json, os, sys, time
from fractions import Fraction as Fr
import numpy as np
from scipy.optimize import linprog
PRE, WORK, control = sys.argv[1:4]
DO_MARGIN = len(sys.argv) > 4 and sys.argv[4] == 'margin'
sys.path.insert(0, PRE)
import controls_gen as cg
import controls_verify as cv
P = 2147483647
body = cv.Body(control)
pool = json.load(open(os.path.join(WORK, 'pool-%s.json' % control)))
prob = cg.Problem(pool)
n, nn = prob.n, prob.n * prob.n
def modf(f):
    f = Fr(f); return (f.numerator % P) * pow(f.denominator % P, P - 2, P) % P
states = body.pools['A']['states']; effs = body.pools['A']['effects']
Sm = np.array([[modf(1)] + [modf(c) for c in s] for s in states], dtype=np.int64)
Em = np.array([[modf(c) for c in e] for e in effs], dtype=np.int64)
Nm = np.array([[modf(v) for v in bv] for bv in prob.basis_exact], dtype=np.int64).T   # nfree x nv
fp, fq = prob.fp, prob.fq
R = body.reference
Rf = np.array([[float(v) for v in r] for r in R])
vals = prob.values(Rf)
tight = np.argwhere(np.abs(vals) < 1e-12)
# exact confirmation of tightness for a sample is in a3/a4 for eball3; here rows mod p
t0 = time.monotonic()
rows = np.zeros((len(tight), prob.nv), dtype=np.int64)
for t, (x, y, a, b) in enumerate(tight):
    ef = (Em[a][:, None] * Em[b][None, :] % P).reshape(-1)
    w = (Sm[x][:, None] * Sm[y][None, :] % P).reshape(-1)
    d = ef[fp] * w[fq] % P
    rows[t] = ((d[:, None] * Nm) % P).sum(axis=0) % P
print('%s: dim F %d; G-side tight quadruples %d; rows mod p built in %.0f s' % (control, prob.nv, len(tight), time.monotonic() - t0), flush=True)
# rank mod p by elimination on a random combination to keep it small: rank(rows) == rank(K rows) w.h.p. is NOT exact;
# do exact elimination on all rows but stream them
def rank_stream(rows):
    basis = {}   # pivot col -> row (normalised)
    for r in rows:
        r = r.copy()
        for c, br in basis.items():
            if r[c]:
                r = (r - r[c] * br) % P
        nz = np.nonzero(r)[0]
        if len(nz):
            c = nz[0]; inv = pow(int(r[c]), P - 2, P)
            r = r * inv % P
            for c2 in list(basis):
                if basis[c2][c]:
                    basis[c2] = (basis[c2] - basis[c2][c] * r) % P
            basis[c] = r
            if len(basis) == rows.shape[1]:
                break
    return len(basis)
t0 = time.monotonic()
rk = rank_stream(rows)
print('rank mod %d of the tight rows: %d of dim F %d (%.0f s)' % (P, rk, prob.nv, time.monotonic() - t0), flush=True)
if DO_MARGIN:
    EF = np.einsum('am,bn->abmn', prob.E, prob.E).reshape(-1, nn)
    W = np.einsum('xk,yl->xykl', prob.S, prob.S).reshape(-1, nn)
    A = (EF[:, None, fp] * W[None, :, fq]).reshape(-1, len(fp))
    Arow = A @ prob.Nmat; Acon = A @ prob.g0free
    forced = (np.abs(Arow).max(axis=1) < 1e-12)
    print('pool-A quadruples %d; rows forced constant by F: %d (constants min %.3e)' % (len(Acon), int(forced.sum()), Acon[forced].min() if forced.any() else np.nan), flush=True)
    Ar, Ac = Arow[~forced], Acon[~forced]
    c = np.zeros(prob.nv + 1); c[-1] = -1
    Aub = np.hstack([-Ar, np.ones((len(Ar), 1))])
    res = linprog(c, A_ub=Aub, b_ub=Ac, bounds=[(-cg.BOX, cg.BOX)] * prob.nv + [(None, 1)], method='highs')
    print('max margin over non-forced pool-A rows (box %g): status %d, t* = %.3e' % (cg.BOX, res.status, -res.fun), flush=True)
