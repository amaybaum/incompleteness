"""Reviewer probe P1 (QPHEN Phase 1 review). Exact, integer arithmetic only.

Checks QX6 §2 'stabilizer settings' claim: for any stabilizer state and Pauli
settings (two per wing), |S_CHSH| <= 2.  Also checks QX6 §2 GHZ row claim that a
GHZ/Mermin argument 'needs Y-type reads'.

States are stored unnormalized with Gaussian-integer amplitudes (re, im) in
{0, +-1, +-i}; <P> = <v|P|v>/<v|v> is computed exactly as a Fraction.
"""
import itertools
from fractions import Fraction
import numpy as np

# ---------- Gaussian integer helpers ----------
def gmul(a, b):
    return (a[0]*b[0] - a[1]*b[1], a[0]*b[1] + a[1]*b[0])
def gadd(a, b):
    return (a[0]+b[0], a[1]+b[1])
def gconj(a):
    return (a[0], -a[1])
ZERO = (0, 0)

def canon(v):
    """Divide by first nonzero entry; assert every ratio is a unit (stabilizer)."""
    first = next(x for x in v if x != ZERO)
    n = first[0]**2 + first[1]**2
    out = []
    for x in v:
        # x / first = x * conj(first) / n
        y = gmul(x, gconj(first))
        assert y[0] % n == 0 and y[1] % n == 0, "non-unit ratio"
        y = (y[0]//n, y[1]//n)
        assert y in (ZERO, (1,0), (-1,0), (0,1), (0,-1)), y
        out.append(y)
    return tuple(out)

def apply_1q(v, n, k, M):
    """M is 2x2 of Gaussian ints, acting on qubit k (qubit 0 = most significant)."""
    out = [ZERO]*len(v)
    for idx, amp in enumerate(v):
        if amp == ZERO:
            continue
        bit = (idx >> (n-1-k)) & 1
        for nb in (0, 1):
            m = M[nb][bit]
            if m == ZERO:
                continue
            j = idx & ~(1 << (n-1-k)) | (nb << (n-1-k))
            out[j] = gadd(out[j], gmul(m, amp))
    return out

def apply_cnot(v, n, c, t):
    out = list(v)
    for idx in range(len(v)):
        if (idx >> (n-1-c)) & 1:
            j = idx ^ (1 << (n-1-t))
            out[j] = v[idx]
    return out

H = [[(1,0),(1,0)],[(1,0),(-1,0)]]
S = [[(1,0),ZERO],[ZERO,(0,1)]]

def stabilizer_states(n):
    start = tuple([(1,0)] + [ZERO]*(2**n - 1))
    seen = {start}
    frontier = [start]
    while frontier:
        new = []
        for v in frontier:
            imgs = []
            for k in range(n):
                imgs.append(apply_1q(v, n, k, H))
                imgs.append(apply_1q(v, n, k, S))
            for c in range(n):
                for t in range(n):
                    if c != t:
                        imgs.append(apply_cnot(v, n, c, t))
            for w in imgs:
                w = canon(w)
                if w not in seen:
                    seen.add(w)
                    new.append(w)
        frontier = new
    return sorted(seen)

# ---------- Paulis ----------
P1 = {
    'I': [[(1,0),ZERO],[ZERO,(1,0)]],
    'X': [[ZERO,(1,0)],[(1,0),ZERO]],
    'Y': [[ZERO,(0,-1)],[(0,1),ZERO]],
    'Z': [[(1,0),ZERO],[ZERO,(-1,0)]],
}

def apply_pauli(v, n, label):
    w = list(v)
    for k, ch in enumerate(label):
        if ch != 'I':
            w = apply_1q(w, n, k, P1[ch])
    return w

def expval(v, n, label):
    w = apply_pauli(v, n, label)
    num = ZERO
    for a, b in zip(v, w):
        num = gadd(num, gmul(gconj(a), b))
    assert num[1] == 0
    nrm = sum(a[0]**2 + a[1]**2 for a in v)
    return Fraction(num[0], nrm)

def main():
    report = {}
    # Control: stabilizer state counts (known: 6, 60, 1080).
    st = {n: stabilizer_states(n) for n in (1, 2, 3)}
    counts = {n: len(st[n]) for n in st}
    report['stabilizer_counts'] = counts
    assert counts == {1: 6, 2: 60, 3: 1080}, counts

    signs = list(itertools.product((1, -1), repeat=4))
    # ---- 1+1 qubits: settings among +-{I,X,Y,Z} on each wing ----
    max11 = 0
    for v in st[2]:
        E = {}
        for a in 'IXYZ':
            for b in 'IXYZ':
                E[(a, b)] = expval(v, 2, a + b)
                assert E[(a, b)] in (-1, 0, 1)
        for A0, A1, B0, B1 in itertools.product('IXYZ', repeat=4):
            e = (E[(A0,B0)], E[(A0,B1)], E[(A1,B0)], E[(A1,B1)])
            for sa0, sa1, sb0, sb1 in signs:
                s = sa0*sb0*e[0] + sa0*sb1*e[1] + sa1*sb0*e[2] - sa1*sb1*e[3]
                max11 = max(max11, abs(s))
    report['max_abs_S_1+1'] = int(max11)

    # ---- 1+2 qubits: wing A qubit 0 (4 Paulis), wing B qubits 1,2 (16 Paulis) ----
    pa = list('IXYZ')
    pb = [x + y for x in 'IXYZ' for y in 'IXYZ']
    max12 = 0
    sg = np.array(signs)  # (16,4)
    for v in st[3]:
        E = np.array([[int(expval(v, 3, a + b)) for b in pb] for a in pa])  # exact ints
        # vectorise over A0,A1 (4x4) and B0,B1 (16x16)
        E00 = E[:, None, :, None]; E01 = E[:, None, None, :]
        E10 = E[None, :, :, None]; E11 = E[None, :, None, :]
        for sa0, sa1, sb0, sb1 in signs:
            S_ = sa0*sb0*E00 + sa0*sb1*E01 + sa1*sb0*E10 - sa1*sb1*E11
            max12 = max(max12, int(np.abs(S_).max()))
    report['max_abs_S_1+2'] = max12

    # ---- Positive control: |Phi+>, A0=Z, A1=X, B_{0,1}=(Z +- X)/sqrt2 ----
    phi = [(1,0), ZERO, ZERO, (1,0)]
    ZZ, ZX, XZ, XX = (expval(phi, 2, l) for l in ('ZZ', 'ZX', 'XZ', 'XX'))
    # sqrt2 * E_xy computed exactly: sqrt2*E00 = <Z(Z+X)> = ZZ+ZX etc.
    r2S = (ZZ + ZX) + (ZZ - ZX) + (XZ + XX) - (XZ - XX)
    report['phi+_sqrt2_times_S'] = str(r2S)  # expect 4, i.e. S = 2*sqrt2
    assert r2S == 4

    # ---- GHZ row: X/Z-only all-versus-nothing on the triangle graph state ----
    # triangle graph state = CZ12 CZ13 CZ23 |+++>; build exactly.
    n = 3
    v = [(1,0)] * 8
    for i, j in ((0,1), (0,2), (1,2)):
        v = [(-a[0], -a[1]) if ((idx >> (n-1-i)) & 1 and (idx >> (n-1-j)) & 1) else a
             for idx, a in enumerate(v)]
    vals = {l: expval(v, 3, l) for l in ('XZZ', 'ZXZ', 'ZZX', 'XXX')}
    report['triangle_graph_expvals'] = {k: str(x) for k, x in vals.items()}
    assert vals == {'XZZ': 1, 'ZXZ': 1, 'ZZX': 1, 'XXX': -1}
    mermin_q = vals['XZZ'] + vals['ZXZ'] + vals['ZZX'] - vals['XXX']
    lhv = max(x1*z2*z3 + z1*x2*z3 + z1*z2*x3 - x1*x2*x3
              for x1, x2, x3, z1, z2, z3 in itertools.product((1, -1), repeat=6))
    report['triangle_XZ_only_mermin_quantum'] = str(mermin_q)
    report['triangle_XZ_only_mermin_LHV_max'] = lhv
    # Standard GHZ with X/Z only: no full-weight X/Z stabilizer element except XXX
    ghz = [(1,0)] + [ZERO]*6 + [(1,0)]
    xz_full = {''.join(t): expval(ghz, 3, ''.join(t)) for t in itertools.product('XZ', repeat=3)}
    report['GHZ_full_weight_XZ_nonzero'] = {k: str(x) for k, x in xz_full.items() if x != 0}

    for k, x in report.items():
        print(f'{k}: {x}')

if __name__ == '__main__':
    main()
