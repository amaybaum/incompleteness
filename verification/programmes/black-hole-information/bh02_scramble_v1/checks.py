#!/usr/bin/env python3
"""BH-02 / BH-04 checks: permutation dynamics versus quantum scrambling; Page-time fraction.

Preregistration: PLAN.md, amendments/A1-shell-cases.md, amendments/A2-mutant-criterion.md.
Standard library only.  Run:  python3 -I -B checks.py > result.json
Exact claims use fractions.Fraction, Q(sqrt 2) pairs, or rigorous rational interval bounds.
Floating point appears only in quantities labelled NUMERICAL, each controlled (K-eig).
A failed required control prints VOID on stdout and the script exits 2.
Wall times go to stderr only.
"""
import sys
import math
import json
import random
import itertools
import time
from fractions import Fraction as Fr

SEEDS = {
    "C1_sample_q2n4": 20261025,
    "C3_perm_n8": 917001,
    "C3_perm_n10": 917002,
    "C3_iterated": 917003,
    "C3_local": 917004,
    "C3_haar_ct1": 917005,
    "C3_lowH": 917006,
    "C4_classical": 917007,
    "C5_mc": 917008,
    "C5_mc_real": 917009,
    "C5_circuit": 917010,
    "C6_shell_mc": 917011,
    "C6_diag_mc": 917012,
}
PAGE_TOL = 0.10          # nats, preregistered (PLAN §1)
EIG_TOL = 1e-10          # K-eig tolerance (PLAN §1)
TIMES = []


def tick(label, t0):
    TIMES.append((label, time.perf_counter() - t0))


# ---------------------------------------------------------------- indexing

_IMAP = {}


def index_map(n, q, R):
    """For each configuration index x, the pair (r, b) of its R- and B-sub-indices."""
    key = (n, q, tuple(R))
    if key in _IMAP:
        return _IMAP[key]
    Rset = set(R)
    B = [i for i in range(n) if i not in Rset]
    out = []
    for x in range(q ** n):
        d = [(x // q ** (n - 1 - i)) % q for i in range(n)]
        r = 0
        for i in R:
            r = r * q + d[i]
        b = 0
        for i in B:
            b = b * q + d[i]
        out.append((r, b))
    val = (out, q ** len(R), q ** len(B))
    _IMAP[key] = val
    return val


def amp_matrix(psi, n, q, R, zero=0):
    imap, dR, dB = index_map(n, q, R)
    M = [[zero] * dB for _ in range(dR)]
    for x, (r, b) in enumerate(imap):
        M[r][b] = psi[x]
    return M


def proper_subsets(n):
    out = []
    for k in range(1, n):
        out.extend(itertools.combinations(range(n), k))
    return out


# ---------------------------------------------------------------- exact linear algebra

def exact_rank(M):
    A = [[Fr(v) for v in row] for row in M]
    rows, cols = len(A), len(A[0]) if A else 0
    rank = 0
    for c in range(cols):
        piv = None
        for r in range(rank, rows):
            if A[r][c] != 0:
                piv = r
                break
        if piv is None:
            continue
        A[rank], A[piv] = A[piv], A[rank]
        pv = A[rank][c]
        for r in range(rows):
            if r != rank and A[r][c] != 0:
                f = A[r][c] / pv
                A[r] = [a - f * b for a, b in zip(A[r], A[rank])]
        rank += 1
    return rank


def gram_real(M):
    """Gram matrix on the smaller side (same nonzero spectrum as M M^T)."""
    dR, dB = len(M), len(M[0])
    if dR <= dB:
        return [[sum(a * b for a, b in zip(M[i], M[j])) for j in range(dR)] for i in range(dR)]
    cols = [[M[r][c] for r in range(dR)] for c in range(dB)]
    return [[sum(a * b for a, b in zip(cols[i], cols[j])) for j in range(dB)] for i in range(dB)]


def gram_complex(M):
    dR, dB = len(M), len(M[0])
    if dR <= dB:
        rows = M
    else:
        rows = [[M[r][c].conjugate() for r in range(dR)] for c in range(dB)]
    k = len(rows)
    return [[sum(a * b.conjugate() for a, b in zip(rows[i], rows[j])) for j in range(k)]
            for i in range(k)]


def frob2(G):
    return sum(abs(v) ** 2 for row in G for v in row)


# ---------------------------------------------------------------- numerics (controlled)

def jacobi_eigs(A, max_sweeps=60):
    n = len(A)
    a = [list(map(float, row)) for row in A]
    for _ in range(max_sweeps):
        off = 0.0
        for i in range(n):
            for j in range(n):
                if i != j:
                    off += a[i][j] * a[i][j]
        if off < 1e-30:
            break
        for p in range(n - 1):
            for q in range(p + 1, n):
                apq = a[p][q]
                if abs(apq) < 1e-300:
                    continue
                theta = (a[q][q] - a[p][p]) / (2.0 * apq)
                t = (1.0 if theta >= 0 else -1.0) / (abs(theta) + math.sqrt(theta * theta + 1.0))
                c = 1.0 / math.sqrt(t * t + 1.0)
                s = t * c
                for k in range(n):
                    akp, akq = a[k][p], a[k][q]
                    a[k][p] = c * akp - s * akq
                    a[k][q] = s * akp + c * akq
                for k in range(n):
                    apk, aqk = a[p][k], a[q][k]
                    a[p][k] = c * apk - s * aqk
                    a[q][k] = s * apk + c * aqk
    return [a[i][i] for i in range(n)]


def jacobi_herm(A, max_sweeps=60):
    """Complex Hermitian Jacobi: phase-rotate a_pq real, then a real rotation."""
    n = len(A)
    a = [[complex(v) for v in row] for row in A]
    for _ in range(max_sweeps):
        off = 0.0
        for i in range(n):
            for j in range(n):
                if i != j:
                    off += abs(a[i][j]) ** 2
        if off < 1e-30:
            break
        for p in range(n - 1):
            for q in range(p + 1, n):
                apq = a[p][q]
                r = abs(apq)
                if r < 1e-300:
                    continue
                ph = apq / r
                theta = (a[q][q].real - a[p][p].real) / (2.0 * r)
                t = (1.0 if theta >= 0 else -1.0) / (abs(theta) + math.sqrt(theta * theta + 1.0))
                c = 1.0 / math.sqrt(t * t + 1.0)
                s = t * c
                cph = ph.conjugate()
                for k in range(n):
                    akp, akq = a[k][p], a[k][q]
                    a[k][p] = c * akp - s * cph * akq
                    a[k][q] = s * akp + c * cph * akq
                for k in range(n):
                    apk, aqk = a[p][k], a[q][k]
                    a[p][k] = c * apk - s * ph * aqk
                    a[q][k] = s * apk + c * ph * aqk
    return [a[i][i].real for i in range(n)]


def embed_eigs(G):
    """Cross-check path: real symmetric embedding of a Hermitian matrix."""
    k = len(G)
    E = [[0.0] * (2 * k) for _ in range(2 * k)]
    for i in range(k):
        for j in range(k):
            re, im = G[i][j].real, G[i][j].imag
            E[i][j] = re
            E[i + k][j + k] = re
            E[i][j + k] = -im
            E[i + k][j] = im
    return sorted(jacobi_eigs(E))[0::2]


EIG = {"count": 0, "max_trace_dev": 0.0, "max_purity_dev": 0.0, "min_eig": 0.0}


def spectrum(G, is_complex=False, exact_purity=None):
    """Eigenvalues of a normalized density-matrix Gram block (NUMERICAL), with K-eig bookkeeping."""
    if is_complex:
        ev = jacobi_herm(G)
    else:
        ev = jacobi_eigs(G)
    tr = sum(ev)
    pur = sum(v * v for v in ev)
    ref = float(exact_purity) if exact_purity is not None else frob2(G)
    EIG["count"] += 1
    EIG["max_trace_dev"] = max(EIG["max_trace_dev"], abs(tr - 1.0))
    EIG["max_purity_dev"] = max(EIG["max_purity_dev"], abs(pur - ref))
    EIG["min_eig"] = min(EIG["min_eig"], min(ev))
    return ev


def vn(ev):
    return -sum(v * math.log(v) for v in ev if v > 1e-300)


def shannon(p):
    return -sum(v * math.log(v) for v in p if v > 0)


# ---------------------------------------------------------------- rigorous logs / roots

SCALE = 2 ** 200


def _down(x):
    return Fr(math.floor(x * SCALE), SCALE)


def _up(x):
    return Fr(math.ceil(x * SCALE), SCALE)


def atanh2_interval(z, terms=60, remainder=True):
    """2*atanh(z) for rational 0 <= z < 1, as a rational interval."""
    s = Fr(0)
    zp = z
    z2 = z * z
    for k in range(terms):
        s += zp / (2 * k + 1)
        zp *= z2
    s *= 2
    rem = 2 * zp / ((2 * terms + 1) * (1 - z2)) if remainder else Fr(0)
    return s, s + rem


_LN2 = None


def ln2_interval():
    global _LN2
    if _LN2 is None:
        lo, hi = atanh2_interval(Fr(1, 3))
        _LN2 = (_down(lo), _up(hi))
    return _LN2


def ln_interval(x):
    x = Fr(x)
    if x <= 0:
        raise ValueError("ln of nonpositive")
    if x < 1:
        lo, hi = ln_interval(1 / x)
        return -hi, -lo
    e = 0
    while x > 2:
        x /= 2
        e += 1
    lo, hi = atanh2_interval((x - 1) / (x + 1))
    l2lo, l2hi = ln2_interval()
    return _down(e * l2lo + lo), _up(e * l2hi + hi)


def sqrt_interval(x, digits=40):
    x = Fr(x)
    sc = 10 ** digits
    v = math.isqrt(math.floor(x * sc * sc))
    lo = Fr(v, sc)
    hi = Fr(v + 1, sc)
    return lo, hi


def dec(x, places=10):
    """Exact rational truncated (toward -inf) to the given places, as a string."""
    x = Fr(x)
    sc = 10 ** places
    v = math.floor(x * sc)
    sign = "-" if v < 0 else ""
    v = abs(v)
    return "%s%d.%0*d" % (sign, v // sc, places, v % sc)


def fx(v, places=6):
    return "%.*f" % (places, v)


# ---------------------------------------------------------------- Page values (SUPPLIED Haar)

def page_exact(m, k):
    """Page's exact Haar average: sum_{j=k+1}^{mk} 1/j - (m-1)/(2k), m <= k (direct sum)."""
    if m > k:
        m, k = k, m
    s = Fr(0)
    for j in range(k + 1, m * k + 1):
        s += Fr(1, j)
    return s - Fr(m - 1, 2 * k)


_H = [Fr(0)]


def harmonic(N):
    while len(_H) <= N:
        _H.append(_H[-1] + Fr(1, len(_H)))
    return _H[N]


def page_via_H(m, k):
    """Independent code path: H_{mk} - H_k - (m-1)/(2k)."""
    if m > k:
        m, k = k, m
    return harmonic(m * k) - harmonic(k) - Fr(m - 1, 2 * k)


def haar_purity(m, k):
    return Fr(m + k, m * k + 1)


# ---------------------------------------------------------------- permutations and gates

def apply_perm(sigma, psi):
    out = [0] * len(psi)
    for x, a in enumerate(psi):
        out[sigma[x]] = a
    return out


def random_perm(N, rng):
    lst = list(range(N))
    rng.shuffle(lst)
    return lst


def is_bijection(sigma, N):
    return len(sigma) == N and set(sigma) == set(range(N))


def cnot_perm(n, c, t):
    sig = []
    for x in range(2 ** n):
        if (x >> (n - 1 - c)) & 1:
            sig.append(x ^ (1 << (n - 1 - t)))
        else:
            sig.append(x)
    return sig


def apply_1q(U, psi, n, i):
    """Apply a 2x2 matrix U (entries Fraction or complex) to qubit i."""
    out = list(psi)
    bit = 1 << (n - 1 - i)
    for x in range(2 ** n):
        if x & bit:
            continue
        a0, a1 = psi[x], psi[x | bit]
        out[x] = U[0][0] * a0 + U[0][1] * a1
        out[x | bit] = U[1][0] * a0 + U[1][1] * a1
    return out


def rot_gate():
    """Rational rotation used by countercontrol CC2 (not a permutation)."""
    return [[Fr(3, 5), Fr(-4, 5)], [Fr(4, 5), Fr(3, 5)]]


def cc3_unitary(psi, n):
    """Countercontrol CC3: rational rotation on qubit 0, then CNOT 0->1."""
    v = apply_1q(rot_gate(), psi, n, 0)
    return apply_perm(cnot_perm(n, 0, 1), v)


def plus_state_scaled(n):
    """|+^n> with every amplitude 1 (unnormalized, integers)."""
    return [1] * (2 ** n)


def haar_state(dim, rng):
    v = [complex(rng.gauss(0.0, 1.0), rng.gauss(0.0, 1.0)) for _ in range(dim)]
    nrm = math.sqrt(sum(abs(a) ** 2 for a in v))
    return [a / nrm for a in v]


def gram_schmidt_unitary(rng, d=4, normalize=True):
    cols = []
    for _ in range(d):
        v = [complex(rng.gauss(0.0, 1.0), rng.gauss(0.0, 1.0)) for _ in range(d)]
        for u in cols:
            ip = sum(a.conjugate() * b for a, b in zip(u, v))
            v = [b - ip * a for a, b in zip(u, v)]
        if normalize:
            nrm = math.sqrt(sum(abs(a) ** 2 for a in v))
            v = [a / nrm for a in v]
        cols.append(v)
    return [[cols[j][i] for j in range(d)] for i in range(d)]


def unitarity_dev(U):
    d = len(U)
    dev = 0.0
    for i in range(d):
        for j in range(d):
            s = sum(U[k][i].conjugate() * U[k][j] for k in range(d))
            dev = max(dev, abs(s - (1.0 if i == j else 0.0)))
    return dev


def apply_2q(U, psi, n, i, j):
    bi, bj = 1 << (n - 1 - i), 1 << (n - 1 - j)
    out = list(psi)
    for x in range(2 ** n):
        if x & bi or x & bj:
            continue
        idx = [x, x | bj, x | bi, x | bi | bj]
        a = [psi[t] for t in idx]
        for r in range(4):
            out[idx[r]] = sum(U[r][c] * a[c] for c in range(4))
    return out


def apply_3bit(g, psi, n, sites):
    """Reversible 3-bit gate g (a permutation of 0..7) on the given sites."""
    out = [0] * len(psi)
    bits = [1 << (n - 1 - s) for s in sites]
    for x, a in enumerate(psi):
        v = 0
        for b in bits:
            v = (v << 1) | (1 if x & b else 0)
        w = g[v]
        y = x
        for k, b in enumerate(bits):
            if (w >> (2 - k)) & 1:
                y |= b
            else:
                y &= ~b
        out[y] = a
    return out


# ---------------------------------------------------------------- entropies of states

def entropies_real_scaled(v, n, R, norm2):
    """For a real (int/Fraction) scaled amplitude vector with squared norm norm2:
    exact rank, exact purity, NUMERICAL von Neumann entropy at bipartition R."""
    M = amp_matrix(v, n, 2, R)
    G = gram_real(M)
    pur = Fr(sum(x * x for row in G for x in row)) / (Fr(norm2) ** 2)
    Gf = [[float(Fr(x) / norm2) for x in row] for row in G]
    ev = spectrum(Gf, exact_purity=pur)
    return M, pur, vn(ev)


def entropy_complex(psi, n, R):
    M = amp_matrix(psi, n, 2, R, zero=0j)
    G = gram_complex(M)
    ev = spectrum(G, is_complex=True)
    return vn(ev), frob2(G)


# ================================================================ C1

def run_C1(controls, res):
    t0 = time.perf_counter()
    out = {}
    total_bad = 0
    nonbij = 0
    for (q, n) in [(2, 2), (2, 3), (3, 2)]:
        N = q ** n
        bips = proper_subsets(n)
        rank_cache = {}
        nperm = 0
        nstates = 0
        bad = 0
        for sigma in itertools.permutations(range(N)):
            nperm += 1
            if not is_bijection(sigma, N):
                nonbij += 1
                continue
            for x in range(N):
                e = [0] * N
                e[x] = 1
                v = apply_perm(sigma, e)
                nz = [i for i, a in enumerate(v) if a != 0]
                nstates += 1
                if len(nz) != 1 or v[nz[0]] != 1:
                    bad += 1
                    continue
                y = nz[0]
                if y not in rank_cache:
                    rank_cache[y] = max(exact_rank(amp_matrix(v, n, q, R)) for R in bips)
                if rank_cache[y] != 1:
                    bad += 1
        out["q%d_n%d" % (q, n)] = {"permutations": nperm, "state_checks": nstates,
                                   "bipartitions": len(bips), "rank_gt_1": bad,
                                   "mode": "exhaustive over Sym(X)"}
        total_bad += bad
    # seeded sample at (2,4), full orbits
    rng = random.Random(SEEDS["C1_sample_q2n4"])
    n, N = 4, 16
    bips = proper_subsets(n)
    bad = 0
    nst = 0
    cache4 = {}
    for _ in range(500):
        sigma = random_perm(N, rng)
        if not is_bijection(sigma, N):
            nonbij += 1
            continue
        for x0 in range(N):
            e = [0] * N
            e[x0] = 1
            v = e
            for _t in range(N + 1):
                v = apply_perm(sigma, v)
                nst += 1
                nz = [i for i, a in enumerate(v) if a != 0]
                if len(nz) != 1 or v[nz[0]] != 1:
                    bad += 1
                    break
                if nz[0] not in cache4:
                    cache4[nz[0]] = max(exact_rank(amp_matrix(v, n, 2, R)) for R in bips)
                if cache4[nz[0]] != 1:
                    bad += 1
                if v[x0] == 1:
                    break
    out["q2_n4_sample"] = {"permutations": 500, "state_checks": nst, "bipartitions": len(bips),
                           "rank_gt_1": bad, "mode": "seeded sample, full orbits"}
    total_bad += bad
    # countercontrols
    cc1 = exact_rank(amp_matrix([1, 0, 0, 1], 2, 2, (0,)))
    v = apply_1q(rot_gate(), [Fr(1), 0, 0, 0], 2, 0)
    v = apply_perm(cnot_perm(2, 0, 1), v)
    cc2 = exact_rank(amp_matrix(v, 2, 2, (0,)))
    out["CC1_bell_rank"] = cc1
    out["CC2_rotation_cnot_rank"] = cc2
    out["total_rank_gt_1"] = total_bad
    controls["K-bij"] = controls.get("K-bij", True) and nonbij == 0
    controls["K-rank"] = (cc1 == 2 and cc2 == 2)
    if total_bad == 0 and controls["K-rank"]:
        out["verdict"] = ("PROVED: P_pi maps configuration basis vectors to configuration basis "
                          "vectors, so every state on the orbit of a configuration is a product "
                          "basis state, Schmidt rank 1, S(R)=0 exactly, at every aligned "
                          "bipartition. Exhaustive check: %d, %d and %d permutations at "
                          "(q,n)=(2,2),(2,3),(3,2); %d sampled at (2,4) with full orbits; "
                          "0 states of rank > 1; countercontrols CC1, CC2 detected with rank %d, %d."
                          % (out["q2_n2"]["permutations"], out["q2_n3"]["permutations"],
                             out["q3_n2"]["permutations"], 500, cc1, cc2))
    elif total_bad > 0:
        out["verdict"] = "COUNTEREXAMPLE: %d states of rank > 1 under a permutation" % total_bad
    else:
        out["verdict"] = "VOID"
    res["C1"] = out
    tick("C1", t0)


# ================================================================ C2

def run_C2(controls, res):
    t0 = time.perf_counter()
    n, N = 3, 8
    a, b = Fr(3, 5), Fr(4, 5)
    c, d = Fr(5, 13), Fr(12, 13)

    def prod(f0, f1, f2):
        out = []
        for x in range(N):
            bits = [(x >> 2) & 1, (x >> 1) & 1, x & 1]
            out.append(f0[bits[0]] * f1[bits[1]] * f2[bits[2]])
        return out

    s1 = prod((a, b), (a, b), (a, b))
    s2 = prod((a, b), (c, d), (Fr(1), Fr(0)))
    s3 = [Fr(0)] * N
    s3[0b000] = Fr(1, 3)
    s3[0b011] = Fr(2, 3)
    s3[0b101] = Fr(-2, 3)
    states = {"s1_(3/5,4/5)^3": s1, "s2_(3/5,4/5)(5/13,12/13)|0>": s2,
              "s3_entangled_(1/3,2/3,-2/3)": s3}
    bips = proper_subsets(n)
    out = {}
    viol_exact = 0
    min_margin_ii = None
    for name, psi0 in states.items():
        norm = sum(x * x for x in psi0)
        if norm != 1:
            viol_exact += 1
        supp = sum(1 for x in psi0 if x != 0)
        F0 = (sum(psi0) ** 2) / N
        p0 = [float(x * x) for x in psi0]
        H0 = shannon(p0)
        ms0 = sorted(psi0)
        seen = set()
        nperm = 0
        rec = {"support": supp, "F0": str(F0), "H_p0_nats": fx(H0), "distinct_states": 0,
               }
        worst = -1e9
        for sigma in itertools.permutations(range(N)):
            nperm += 1
            v = apply_perm(sigma, psi0)
            key = tuple(v)
            if key in seen:
                continue
            seen.add(key)
            if sorted(v) != ms0:
                viol_exact += 1
            Fv = (sum(v) ** 2) / N
            if Fv != F0:
                viol_exact += 1
            for R in bips:
                M = amp_matrix(v, n, 2, R)
                rk = exact_rank(M)
                if rk > supp:
                    viol_exact += 1
                G = [[sum(x * y for x, y in zip(M[i], M[j])) for j in range(len(M))]
                     for i in range(len(M))]
                dR = len(M)
                pur = sum(x * x for row in G for x in row)
                plusR = sum(x for row in G for x in row) / dR
                if plusR < F0 or pur < F0 * F0:
                    viol_exact += 1
                Gs = gram_real(M)
                ev = spectrum([[float(x) for x in row] for row in Gs],
                              exact_purity=sum(x * x for row in Gs for x in row))
                S = vn(ev)
                pR = [float(sum(x * x for x in M[r])) for r in range(dR)]
                pB = [float(sum(M[r][bb] ** 2 for r in range(dR))) for bb in range(len(M[0]))]
                margin = min(shannon(pR), shannon(pB)) - S
                worst = max(worst, S - H0)
                min_margin_ii = margin if min_margin_ii is None else min(min_margin_ii, margin)
        rec["permutations"] = nperm
        rec["distinct_states"] = len(seen)
        rec["max_S_minus_H_p0"] = fx(worst, 9)
        out[name] = rec
    out["exact_violations_(i)_(iii)"] = viol_exact
    out["min_margin_(ii)_NUMERICAL"] = fx(min_margin_ii, 12)
    # tightness witness
    tight = {}
    tight_ok = True
    for (nn, k) in [(4, 2), (6, 3)]:
        NN = 2 ** nn
        psi = [0] * NN
        for x in range(NN):
            if x % (2 ** (nn - k)) == 0:
                psi[x] = 1
        for i in range(k):
            psi = apply_perm(tight_cnot(nn, i, k), psi)
        R = tuple(range(k))
        M = amp_matrix(psi, nn, 2, R)
        rk = exact_rank(M)
        G = gram_real(M)
        norm2 = sum(x * x for x in psi)
        pur = Fr(sum(x * x for row in G for x in row), norm2 * norm2)
        ok = (rk == 2 ** k and pur == Fr(1, 2 ** k))
        tight_ok = tight_ok and ok
        tight["n%d_k%d" % (nn, k)] = {"rank": rk, "purity": str(pur), "flat_spectrum_certified": ok,
                                      "S_equals": "%d ln 2 = H(p0)" % k if ok else "no"}
    out["tightness_witness"] = tight
    # CC3
    psi0 = [Fr(1)] + [Fr(0)] * 7
    F0 = Fr(1, 8)
    v = cc3_unitary(psi0, 3)
    Fv = (sum(v) ** 2) / 8
    rk = exact_rank(amp_matrix(v, 3, 2, (0,)))
    out["CC3"] = {"F_before": str(F0), "F_after": str(Fv), "rank_after": rk, "support_before": 1}
    controls["K-overlap"] = (Fv != F0 and rk > 1)
    controls["K-tight"] = tight_ok
    num_ok = min_margin_ii is not None and min_margin_ii >= -1e-9
    if viol_exact == 0 and num_ok and tight_ok and controls["K-overlap"]:
        out["verdict"] = ("PROVED: under any permutation the amplitude multiset, the overlap "
                          "F=|<+^n|psi>|^2 and the support size are conserved; hence at every "
                          "step and aligned bipartition Schmidt rank <= |supp psi0|, "
                          "S(R) <= min(H(p_R),H(p_B)) <= H(p0), lambda_max(rho_R) >= F, "
                          "S_2 <= -2 ln F. Exact sweep over all 40320 permutations at n=3 for "
                          "three rational states: 0 violations of (i),(iii); (ii) NUMERICAL, "
                          "minimum margin %s nats. Bound attained exactly (S = k ln 2 = H(p0)) "
                          "by a CNOT network on |+>^k|0>^(n-k) for (n,k)=(4,2),(6,3)."
                          % out["min_margin_(ii)_NUMERICAL"])
    elif viol_exact > 0:
        out["verdict"] = "COUNTEREXAMPLE: %d exact violations" % viol_exact
    else:
        out["verdict"] = "VOID"
    res["C2"] = out
    tick("C2", t0)


def tight_cnot(n, i, k):
    """CNOT used by the tightness witness: control qubit i (in R), target k+i (in B)."""
    return cnot_perm(n, i, k + i)


# ================================================================ C3

def xprod_scaled(n):
    """|->|+>^(n-1), amplitudes (-1)^{x_1}, scaled by 2^{n/2}."""
    return [(-1 if (x >> (n - 1)) & 1 else 1) for x in range(2 ** n)]


def low_entropy_state(n):
    """(24/25|0> + 7/25|1>)^(n-1) (x) |0>, exact rational amplitudes (post-review: H(p0) below
    the Page-like band at the half cut, so C2 implies 'not Page-like')."""
    cth, sth = Fr(24, 25), Fr(7, 25)
    out = []
    for x in range(2 ** n):
        if x & 1:
            out.append(Fr(0))
            continue
        amp = Fr(1)
        for i in range(n - 1):
            amp *= sth if (x >> (n - 1 - i)) & 1 else cth
        out.append(amp)
    return out


def run_C3(controls, res):
    t0 = time.perf_counter()
    out = {}
    nonbij = 0
    # (a) random permutations, n = 8, all cuts
    n = 8
    N = 2 ** n
    rng = random.Random(SEEDS["C3_perm_n8"])
    psi0 = xprod_scaled(n)
    page = {r: page_exact(2 ** r, 2 ** (n - r)) for r in range(1, n)}
    pagef = {r: float(page[r]) for r in page}
    all_ok = 0
    half_ok = 0
    maxdev = 0.0
    pur_half = []
    S_half = []
    for _ in range(200):
        sigma = random_perm(N, rng)
        if not is_bijection(sigma, N):
            nonbij += 1
            continue
        v = apply_perm(sigma, psi0)
        ok_all = True
        for r in range(1, n):
            _, pur, S = entropies_real_scaled(v, n, tuple(range(r)), N)
            dev = abs(S - pagef[r])
            maxdev = max(maxdev, dev)
            if dev > PAGE_TOL:
                ok_all = False
            if r == n // 2:
                pur_half.append(pur)
                S_half.append(S)
                if dev <= PAGE_TOL:
                    half_ok += 1
        if ok_all:
            all_ok += 1
    mean_pur = sum(pur_half) / len(pur_half)
    out["n8_random_perms"] = {
        "samples": 200, "initial_state": "|->|+>^7 (SUPPLIED superposition)",
        "page_like_all_cuts": all_ok, "page_like_half_cut": half_ok,
        "max_abs_dev_from_S_Page_nats_NUMERICAL": fx(maxdev),
        "mean_S_half_NUMERICAL": fx(sum(S_half) / len(S_half)),
        "S_Page_16_16_exact_10dp": dec(page[4]),
        "mean_purity_half_exact": dec(mean_pur, 12),
        "haar_mean_purity_16_16": str(haar_purity(16, 16)),
        "iid_sign_mean_purity_16_16": str(Fr(16 + 16 - 1, 256)),
    }
    # (b) n = 10, half cut
    n2 = 10
    N2 = 2 ** n2
    rng2 = random.Random(SEEDS["C3_perm_n10"])
    psi0b = xprod_scaled(n2)
    p10 = page_exact(32, 32)
    ok10 = 0
    S10 = []
    for _ in range(20):
        sigma = random_perm(N2, rng2)
        if not is_bijection(sigma, N2):
            nonbij += 1
            continue
        v = apply_perm(sigma, psi0b)
        _, pur, S = entropies_real_scaled(v, n2, tuple(range(5)), N2)
        S10.append(S)
        if abs(S - float(p10)) <= PAGE_TOL:
            ok10 += 1
    out["n10_random_perms_half_cut"] = {"samples": 20, "page_like": ok10,
                                         "mean_S_NUMERICAL": fx(sum(S10) / len(S10)),
                                         "min_S_NUMERICAL": fx(min(S10)),
                                         "S_Page_32_32_exact_10dp": dec(p10)}
    # (c) fixed permutation iterated with emission schedule r(t)=t
    rng3 = random.Random(SEEDS["C3_iterated"])
    sigma = random_perm(N, rng3)
    if not is_bijection(sigma, N):
        nonbij += 1
    v = psi0
    curve = []
    curve_ok = True
    for t in range(0, n + 1):
        if t > 0:
            v = apply_perm(sigma, v)
        if t == 0 or t == n:
            curve.append({"t": t, "r": t, "S": "0 (exact: empty or full R of a pure state)"})
            continue
        _, pur, S = entropies_real_scaled(v, n, tuple(range(t)), N)
        ok = abs(S - pagef[t]) <= PAGE_TOL
        curve_ok = curve_ok and ok
        curve.append({"t": t, "r": t, "S_NUMERICAL": fx(S), "S_Page_exact_10dp": dec(page[t]),
                      "page_like": ok})
    out["n8_iterated_fixed_perm_emission_curve"] = {"curve": curve, "page_like_all_interior": curve_ok}
    # (d) local reversible 3-bit gates (diagnostic)
    rng4 = random.Random(SEEDS["C3_local"])
    depths = [1, 2, 4, 8, 16, 32]
    loc = {}
    for dpt in depths:
        vals = []
        for s in range(6):
            v = list(psi0)
            for layer in range(dpt):
                off = layer % n
                for g0 in (off, off + 3):
                    g = random_perm(8, rng4)
                    if not is_bijection(g, 8):
                        nonbij += 1
                    v = apply_3bit(g, v, n, [(g0) % n, (g0 + 1) % n, (g0 + 2) % n])
            _, pur, S = entropies_real_scaled(v, n, tuple(range(4)), N)
            vals.append(S)
        loc["depth_%d" % dpt] = {"mean_S_half_NUMERICAL": fx(sum(vals) / len(vals)),
                                 "min": fx(min(vals)), "max": fx(max(vals))}
    out["n8_local_reversible_3bit_brickwork_DIAGNOSTIC"] = loc
    # CC4: |+^n> invariant
    plus = plus_state_scaled(n)
    rngc = random.Random(SEEDS["C3_perm_n8"])
    inv = True
    rank_plus = 0
    for _ in range(50):
        sigma = random_perm(N, rngc)
        w = apply_perm(sigma, plus)
        if w != plus_state_scaled(n):
            inv = False
        rank_plus = max(rank_plus, exact_rank(amp_matrix(w, n, 2, tuple(range(4)))))
    out["CC4_plus_state"] = {"invariant_under_50_perms": inv, "max_half_cut_rank": rank_plus,
                             "page_like": False if rank_plus == 1 else None}
    controls["K-plus"] = inv and rank_plus == 1
    # CC5: low-H product state
    rng5 = random.Random(SEEDS["C3_lowH"])
    lowpsi = low_entropy_state(n)
    H0 = shannon([float(a * a) for a in lowpsi])
    worst = -1e9
    page_like_low = 0
    for _ in range(40):
        sigma = random_perm(N, rng5)
        if not is_bijection(sigma, N):
            nonbij += 1
        v = apply_perm(sigma, lowpsi)
        _, pur, S = entropies_real_scaled(v, n, tuple(range(4)), 1)
        worst = max(worst, S - H0)
        if abs(S - pagef[4]) <= PAGE_TOL:
            page_like_low += 1
    implied = H0 < pagef[4] - PAGE_TOL
    out["CC5_low_entropy_product"] = {"state": "(24/25|0>+7/25|1>)^7 (x) |0>", "H_p0_nats": fx(H0),
                                      "H_p0_below_page_like_band": implied,
                                      "S_Page_16_16": dec(page[4], 6),
                                      "max_S_minus_H_p0_NUMERICAL": fx(worst, 9),
                                      "page_like_half_cut": page_like_low, "samples": 40}
    cc5_ok = implied and worst <= 1e-9 and page_like_low == 0
    # CT1: Haar states attain criterion
    rng6 = random.Random(SEEDS["C3_haar_ct1"])
    ct_ok = 0
    for _ in range(10):
        psi = haar_state(N, rng6)
        ok = True
        for r in range(1, n):
            S, _ = entropy_complex(psi, n, tuple(range(r)))
            if abs(S - pagef[r]) > PAGE_TOL:
                ok = False
        if ok:
            ct_ok += 1
    out["CT1_haar_attainability"] = {"samples": 10, "page_like_all_cuts": ct_ok}
    controls["K-bij"] = controls.get("K-bij", True) and nonbij == 0
    controls["CT1"] = ct_ok == 10
    controls["CC5"] = cc5_ok
    if all_ok > 0:
        out["verdict"] = ("COUNTEREXAMPLE (scoped) to 'permutation dynamics cannot produce "
                          "Page-like entanglement': from the SUPPLIED superposition |->|+>^7, "
                          "%d/200 random permutations give Page-like states at every cut and "
                          "%d/200 at the half cut (n=8, tolerance %.2f nats, NUMERICAL S with "
                          "exact purity control); %d/20 at the n=10 half cut; a fixed permutation "
                          "iterated with r(t)=t gives a Page-like emission curve: %s. Scope: the "
                          "entanglement is bounded by the supplied initial state's basis entropy "
                          "(C2); from a configuration state it is exactly zero (C1). This is not "
                          "a derivation of H-scramble."
                          % (all_ok, half_ok, PAGE_TOL, ok10, "yes" if curve_ok else "no"))
    else:
        out["verdict"] = "OPEN at the sizes tested: no Page-like permutation state found"
    res["C3"] = out
    tick("C3", t0)


# ================================================================ C4

def evolve_dist(p, sigma):
    q = [0.0] * len(p)
    for x in range(len(p)):
        q[sigma[x]] = p[x]
    return q


def run_C4(controls, res):
    t0 = time.perf_counter()
    n, N = 8, 256
    rng = random.Random(SEEDS["C4_classical"])
    p0 = []
    for x in range(N):
        w = bin(x).count("1")
        p0.append((0.25 ** w) * (0.75 ** (n - w)))
    H0 = shannon(p0)
    sigma = random_perm(N, rng)
    p = list(p0)
    curve = []
    viol = 0
    for t in range(n + 1):
        if t > 0:
            p = evolve_dist(p, sigma)
        marg = [0.0] * (2 ** t)
        for x in range(N):
            marg[x >> (n - t)] += p[x]
        Hm = shannon(marg)
        if Hm > H0 + 1e-12:
            viol += 1
        curve.append({"t": t, "H_R_NUMERICAL": fx(Hm)})
    final_eq = abs(float(curve[-1]["H_R_NUMERICAL"]) - H0) <= 1e-6
    res["C4"] = {"n": n, "p0": "Bernoulli(1/4)^8 over configurations", "H_p0": fx(H0),
                 "curve": curve, "violations": viol, "final_equals_H_p0": final_eq,
                 "verdict": ("PROVED: H(p_R) <= H(p_t) = H(p0) = H(p_final); the classical "
                             "marginal-entropy curve ends at its maximum H(p0) (it may dip in between; "
                             "only the endpoint is controlled) and cannot turn "
                             "over to zero (demonstration: %d violations, final value %s = H(p0))"
                             % (viol, curve[-1]["H_R_NUMERICAL"]))
                 if viol == 0 and final_eq else "VOID"}
    controls["K-classical"] = viol == 0 and final_eq
    tick("C4", t0)


# ================================================================ C5

def mc_haar(m, k, samples, rng, real=False):
    Ss, Ps = [], []
    for _ in range(samples):
        if real:
            v = [complex(rng.gauss(0.0, 1.0), 0.0) for _ in range(m * k)]
            nrm = math.sqrt(sum(abs(a) ** 2 for a in v))
            v = [a / nrm for a in v]
        else:
            v = haar_state(m * k, rng)
        M = [[v[i * k + j] for j in range(k)] for i in range(m)]
        G = gram_complex(M)
        ev = spectrum(G, is_complex=True)
        Ss.append(vn(ev))
        Ps.append(frob2(G))
    def ms(xs):
        mu = sum(xs) / len(xs)
        var = sum((x - mu) ** 2 for x in xs) / (len(xs) - 1)
        return mu, math.sqrt(var / len(xs))
    return ms(Ss), ms(Ps)


def run_C5(controls, res):
    t0 = time.perf_counter()
    out = {}
    # (a) table
    table = []
    fbounds_ok = True
    agree_ok = True
    for a in range(0, 6):
        for b in range(a, 11 - a):
            m, k = 2 ** a, 2 ** b
            if m * k > 1024 or a + b > 10:
                continue
            P = page_exact(m, k)
            if P != page_via_H(m, k):
                agree_ok = False
            hs = P + Fr(m - 1, 2 * k)
            lo = ln_interval(Fr(m * k + 1, k + 1))[0]
            hi = ln_interval(Fr(m))[1]
            if not (lo <= hs <= hi):
                fbounds_ok = False
            if m >= 2:
                lnm = ln_interval(Fr(m))
                approx_lo = lnm[0] - Fr(m, 2 * k)
                approx_hi = lnm[1] - Fr(m, 2 * k)
                table.append({"m": m, "k": k, "S_Page_exact_10dp": dec(P),
                              "GR_approx_ln_m_minus_m_over_2k_10dp": dec(approx_lo),
                              "exact_minus_approx_10dp": dec(P - approx_hi)})
    anchor = page_exact(2, 2)
    out["page_table"] = table
    out["S_Page_2_2"] = str(anchor)
    out["S_Page_4_4_rational"] = str(page_exact(4, 4))
    out["GR_quoted_gap_at_4x4"] = "0.886 (GR uses ln 4 - 1/2)"
    # finite-size correction at n_R = n_B
    fs = []
    for a in range(1, 6):
        m = 2 ** a
        P = page_exact(m, m)
        lnm = ln_interval(Fr(m))
        fs.append({"m": m, "S_Page_minus_ln_m_10dp": dec(P - lnm[1])})
    out["finite_size_at_equal_dims"] = fs
    out["finite_size_limit_analytic"] = ("H_N = ln N + gamma + 1/(2N) - 1/(12N^2) + O(N^-4) gives "
                                         "S_Page(m,m) - ln m = -1/2 + 7/(12 m^2) + O(m^-4)")
    m = 32
    lnm = ln_interval(Fr(m))
    resid = (page_exact(m, m) - lnm[1] + Fr(1, 2)) * m * m
    out["finite_size_check_m32_(S-ln m+1/2)*m^2_10dp"] = dec(resid, 10)
    controls["K-page-formula"] = (anchor == Fr(1, 3) and fbounds_ok and agree_ok)
    # (b) Monte Carlo control
    rng = random.Random(SEEDS["C5_mc"])
    rngr = random.Random(SEEDS["C5_mc_real"])
    mc = {}
    mc_ok = True
    real_rejected = True
    for (m, k) in [(2, 2), (2, 4), (4, 4)]:
        (Sm, Sse), (Pm, Pse) = mc_haar(m, k, 4000, rng)
        Pex = float(page_via_H(m, k))
        Hp = float(haar_purity(m, k))
        okS = abs(Sm - Pex) <= 4 * Sse
        okP = abs(Pm - Hp) <= 4 * Pse
        (Sr, Srse), (Pr, Prse) = mc_haar(m, k, 4000, rngr, real=True)
        Hp_real = (m + k + 1) / (m * k + 2)
        rej = abs(Pr - Hp) > 4 * Prse and abs(Pr - Hp_real) <= 4 * Prse
        mc["%dx%d" % (m, k)] = {"mean_S": fx(Sm), "se_S": fx(Sse), "S_Page": fx(Pex),
                                "mean_purity": fx(Pm), "se_purity": fx(Pse),
                                "haar_purity": fx(Hp), "ok": okS and okP,
                                "real_sampler_mean_purity": fx(Pr),
                                "real_exact_purity": fx(Hp_real), "real_rejected": rej}
        mc_ok = mc_ok and okS and okP
        real_rejected = real_rejected and rej
    out["monte_carlo_control"] = mc
    controls["K-page-mc"] = mc_ok and real_rejected
    # (c) SUPPLIED circuit
    rngc = random.Random(SEEDS["C5_circuit"])
    n, N = 8, 256
    psi = [0j] * N
    psi[0] = 1 + 0j
    maxdev = 0.0
    depth_curve = []
    P16 = float(page_exact(16, 16))
    depths = [1, 2, 3, 4, 6, 8, 12, 16, 24]
    gates = []
    for layer in range(depths[-1]):
        row = []
        for i in range(layer % 2, n - 1, 2):
            U = gram_schmidt_unitary(rngc)
            maxdev = max(maxdev, unitarity_dev(U))
            row.append((i, U))
        gates.append(row)
    controls["K-unitary"] = maxdev <= 1e-12
    if not controls["K-unitary"]:
        raise ValueError("supplied gates not unitary")
    depth = 0
    for target in depths:
        while depth < target:
            for (i, U) in gates[depth]:
                psi = apply_2q(U, psi, n, i, i + 1)
            depth += 1
        S, _ = entropy_complex(psi, n, tuple(range(4)))
        depth_curve.append({"depth": target, "S_half_NUMERICAL": fx(S)})
    emis = []
    for r in range(1, n):
        S, _ = entropy_complex(psi, n, tuple(range(r)))
        emis.append({"r": r, "S_NUMERICAL": fx(S),
                     "S_Page_exact_10dp": dec(page_exact(2 ** r, 2 ** (n - r)))})
    out["supplied_haar_brickwork_n8"] = {"label": "SUPPLIED quantum circuit, not an OI mechanism",
                                         "initial": "|0>^8", "depth_curve": depth_curve,
                                         "S_Page_16_16": fx(P16),
                                         "emission_curve_at_depth_24": emis,
                                         "max_unitarity_dev_le_1e-12": maxdev <= 1e-12}
    res["C5"] = out
    tick("C5", t0)


# ================================================================ C6

def comb(a, b):
    return math.comb(a, b) if 0 <= b <= a else 0


def canonical_entropy_interval(D, secs):
    """Entropy of Tr_B Pi_w / D: eigenvalue b_j/D with multiplicity a_j (rigorous interval)."""
    lo = Fr(0)
    hi = Fr(0)
    for (j, a, b) in secs:
        l1, h1 = ln_interval(Fr(D, b))
        lo += a * Fr(b, D) * l1
        hi += a * Fr(b, D) * h1
    return lo, hi


def canonical_by_enumeration(n, w, k, D, secs):
    """Second route: count weight-w configurations per R-configuration; exact spectrum
    comparison with the sector multiset, and a float entropy (NUMERICAL)."""
    counts = {}
    for x in range(2 ** n):
        if bin(x).count("1") == w:
            r = x >> (n - k)
            counts[r] = counts.get(r, 0) + 1
    spec = sorted(Fr(c, D) for c in counts.values())
    expect = sorted(Fr(b, D) for (j, a, b) in secs for _ in range(a))
    s = -sum((c / D) * math.log(c / D) for c in counts.values())
    total_ok = sum(counts.values()) == comb(n, w) == D
    return spec == expect and total_ok, s


def diag_shell_mean(m):
    """Exact Haar mean entropy on span{|i>|i>}: H_m - 1."""
    return harmonic(m) - 1


def run_C6(controls, res, c1_proved):
    t0 = time.perf_counter()
    out = {}
    out["a_satisfiability_in_configuration_setting"] = (
        "PROVED (from C1): with B/R aligned to configuration coordinates and a definite initial "
        "configuration (GR Theorem A.7 proof: 'deterministic evolution from a definite initial "
        "state'; Theorem A.8 counts initial conditions on the shell by |Sigma_E| and averages "
        "over configurations s in C_j), every state on the orbit is a product basis state, so H-scramble fails for "
        "every bijection phi in that setting." if c1_proved else "VOID (C1 not proved)")
    # (b) textual proof trace
    steps = [
        ("phi restricts to a bijection of the finite shell; cycle decomposition", "no d-dependent value"),
        ("cycle time average equals orbit average (exact)", "no d-dependent value"),
        ("PSW/Page: Haar measure on the shell concentrates at S_Page", "S_Page enters here, as a property of Haar measure"),
        ("H-scramble: orbit counting measure ~ Haar on the shell", "transfers the Haar value to the orbit"),
        ("bad-cycle counting with deviation bound ln d_min", "only the trivial bound ln d_min"),
    ]
    out["b_proof_trace_TEXTUAL"] = [{"step": s, "supplies": v} for s, v in steps]
    only_haar = all(("S_Page" not in v) or ("Haar" in v) for _, v in steps)
    out["b_finding"] = ("The value S_Page enters Theorem A.8 only through the Haar ensemble "
                        "that H-scramble posits for the orbit; the bijection's cycle structure "
                        "contributes exact averaging bookkeeping and the trivial bound ln d_min. "
                        "The Page value therefore follows from the hypothesis H-scramble on the "
                        "orbit, not from bijectivity or the cycle decomposition; a dynamics that "
                        "satisfied H-scramble would produce it." if only_haar else "trace inconclusive")
    # (c) shell factorization
    rng = random.Random(SEEDS["C6_shell_mc"])
    cases = [(6, 3, 3), (8, 4, 4), (10, 5, 5), (8, 2, 4), (10, 2, 5), (12, 3, 6)]
    rows = []
    certified = []
    diag_ok = True
    shell_ok = True
    for (n, w, k) in cases:
        D = comb(n, w)
        secs = []
        for j in range(max(0, w - (n - k)), min(k, w) + 1):
            secs.append((j, comb(k, j), comb(n - k, w - j)))
        lo, hi = canonical_entropy_interval(D, secs)
        # independent route (post-review): explicit basis-state counts of Tr_B Pi_w / D
        spec_ok, s_indep = canonical_by_enumeration(n, w, k, D, secs)
        indep_ok = spec_ok and float(lo) - 1e-12 <= s_indep <= float(hi) + 1e-12
        Pfull = page_exact(2 ** k, 2 ** (n - k))
        if hi < Pfull:
            status = "certified below S_Page"
            certified.append((n, w, k))
        elif lo > Pfull:
            status = "certified above S_Page (concavity bound inconclusive)"
        else:
            status = "undecided"
        # sector formula (diagnostic)
        sf = Fr(0)
        for (j, a, b) in secs:
            dj = a * b
            sf += Fr(dj, D) * (page_via_H(a, b) + harmonic(D) - harmonic(dj))
        # Monte Carlo Haar on shell (diagnostic)
        basis = [x for x in range(2 ** n) if bin(x).count("1") == w]
        layout = []
        for (j, a, b) in secs:
            rk_ = sorted({x >> (n - k) for x in basis if bin(x >> (n - k)).count("1") == j})
            bk_ = sorted({x & ((1 << (n - k)) - 1) for x in basis
                          if bin(x >> (n - k)).count("1") == j})
            ri = {v: i for i, v in enumerate(rk_)}
            bi = {v: i for i, v in enumerate(bk_)}
            pos = [(t, ri[x >> (n - k)], bi[x & ((1 << (n - k)) - 1)])
                   for t, x in enumerate(basis) if bin(x >> (n - k)).count("1") == j]
            layout.append((len(rk_), len(bk_), pos))
        Ss = []
        for _ in range(2000):
            amps = haar_state(D, rng)
            evs = []
            for (da, db, pos) in layout:
                Mj = [[0j] * db for _ in range(da)]
                for (t, ii, jj) in pos:
                    Mj[ii][jj] = amps[t]
                G = gram_complex(Mj)
                if len(G) == 1:
                    evs.append(G[0][0].real)
                else:
                    ev = jacobi_herm(G)
                    EIG["max_purity_dev"] = max(EIG["max_purity_dev"],
                                                abs(sum(v * v for v in ev) - frob2(G)))
                    evs.extend(ev)
            tr = sum(evs)
            EIG["count"] += 1
            EIG["max_trace_dev"] = max(EIG["max_trace_dev"], abs(tr - 1.0))
            EIG["min_eig"] = min(EIG["min_eig"], min(evs))
            Ss.append(vn(evs))
        mu = sum(Ss) / len(Ss)
        se = math.sqrt(sum((s - mu) ** 2 for s in Ss) / (len(Ss) - 1) / len(Ss))
        agree = abs(mu - float(sf)) <= 4 * se
        diag_ok = diag_ok and agree
        mc_le_canon = mu <= float(hi) + 4 * se
        shell_ok = shell_ok and indep_ok and mc_le_canon
        rows.append({"n": n, "w": w, "R": k, "shell_dim": D, "full_dim": 2 ** n,
                     "per_mode_log_dim_ln_C_over_n": fx(math.log(D) / n),
                     "S_canonical_interval_10dp": [dec(lo), dec(hi + Fr(1, 10 ** 10))],
                     "S_Page_full_dims_exact_10dp": dec(Pfull),
                     "concavity_status": status,
                     "sector_formula_mean_DIAGNOSTIC": fx(float(sf)),
                     "sector_formula_below_S_Page_exact_given_formula": sf < Pfull,
                     "haar_on_shell_MC_mean_NUMERICAL": fx(mu), "MC_se": fx(se),
                     "MC_agrees_sector_formula": agree,
                     "canonical_by_enumeration_NUMERICAL": fx(s_indep, 10),
                     "canonical_spectrum_matches_enumeration_exact": spec_ok,
                     "MC_mean_le_canonical_upper_plus_4se": mc_le_canon,
                     "preregistered": (n, w, k) in [(6, 3, 3), (8, 4, 4), (10, 5, 5)]})
    out["c_shell_cases"] = rows
    out["c_sector_formula_below_in_all_cases"] = all(r["sector_formula_below_S_Page_exact_given_formula"] for r in rows)
    out["c_diagnostics_agree"] = diag_ok
    controls["K-shell"] = shell_ok
    # post-review: diagonal shell span{|i>|i>} (energy = Hamming distance of b and r, E = 0)
    drows = []
    above_all = True
    rngd = random.Random(SEEDS["C6_diag_mc"])
    diag_mc_ok = True
    for m in (2, 3, 4, 8, 16):
        dm = diag_shell_mean(m)
        P = page_exact(m, m)
        above = dm > P
        above_all = above_all and above
        row = {"m": m, "haar_mean_on_diagonal_shell_exact": str(dm),
               "value_10dp": dec(dm), "S_Page_m_m_10dp": dec(P), "above_S_Page": above}
        if m in (2, 4, 8):
            Ss = []
            for _ in range(4000):
                c = haar_state(m, rngd)
                Ss.append(shannon([abs(z) ** 2 for z in c]))
            mu = sum(Ss) / len(Ss)
            se = math.sqrt(sum((x - mu) ** 2 for x in Ss) / (len(Ss) - 1) / len(Ss))
            ok = abs(mu - float(dm)) <= 4 * se
            diag_mc_ok = diag_mc_ok and ok
            row.update({"MC_mean_NUMERICAL": fx(mu), "MC_se": fx(se), "MC_agrees": ok})
        drows.append(row)
    out["c_post_review_diagonal_shell"] = {
        "shell": "span{|i>_B|i>_R}, i = 1..m (d_B = d_R = m); rho_R = diag(|c_i|^2), "
                 "c Haar on C^m, so the spectrum is uniform on the simplex",
        "formula": "E[S] = H_m - 1 (expected Shannon entropy of a uniform point of the simplex)",
        "rows": drows, "above_in_all_rows": above_all}
    controls["K-diag"] = diag_mc_ok
    certified_above = above_all
    if certified:
        out["c_verdict"] = ("CONDITIONAL: Theorem A.8 states the Page value with the full factor "
                            "dimensions while positing equidistribution on a shell subspace, and "
                            "the Haar-on-shell mean differs from that value in a direction that "
                            "depends on the shell. For a conserved Hamming weight it lies below "
                            "S_Page(d_R,d_B), certified (concavity, rigorous log intervals) in "
                            "cases %s (all added by amendment A1; the preregistered half-filling "
                            "cases are not certified by this bound). For the diagonal shell "
                            "span{|i>|i>} it is exactly H_m - 1, above S_Page(m,m) for m = 2, 3, 4, "
                            "8, 16 (post-review result): %s. The unstated hypothesis is that the "
                            "shell is the full product space, or that d_B, d_R are replaced by "
                            "the shell's own typical value."
                            % (", ".join("(n,w,|R|)=(%d,%d,%d)" % c for c in certified),
                               "all rows above" if certified_above else "not all rows above"))
    else:
        out["c_verdict"] = "no finding: no case certified"
    out["d_time_average_vs_instantaneous"] = (
        "OPEN proof obligation (textual): Theorem A.8 bounds a cycle time-average at a fixed "
        "bipartition on a fixed shell; Theorem A.9 applies it at each t along one trajectory "
        "with a changing bipartition, starting from a definite state, which C1 shows has S=0 "
        "in the configuration factorization. No computation here settles it.")
    res["C6"] = out
    tick("C6", t0)


# ================================================================ C7

class Q2:
    """a + b*sqrt(2), a, b rational."""
    def __init__(self, a, b=0):
        self.a, self.b = Fr(a), Fr(b)

    def __add__(self, o):
        o = o if isinstance(o, Q2) else Q2(o)
        return Q2(self.a + o.a, self.b + o.b)

    def __sub__(self, o):
        o = o if isinstance(o, Q2) else Q2(o)
        return Q2(self.a - o.a, self.b - o.b)

    def __mul__(self, o):
        o = o if isinstance(o, Q2) else Q2(o)
        return Q2(self.a * o.a + 2 * self.b * o.b, self.a * o.b + self.b * o.a)

    def div_rational(self, r):
        return Q2(self.a / r, self.b / r)

    def interval(self):
        lo, hi = sqrt_interval(2)
        if self.b >= 0:
            return self.a + self.b * lo, self.a + self.b * hi
        return self.a + self.b * hi, self.a + self.b * lo

    def s(self):
        return "%s + (%s)*sqrt(2)" % (self.a, self.b)


def page_fraction_beta(beta):
    """1 - (beta/(1+beta))^{3/2} as a rational interval; S_BH/S0 at turnover."""
    y = Fr(beta) / (1 + Fr(beta))
    lo, hi = sqrt_interval(y)
    return 1 - y * hi, 1 - y * lo, y


def simpson_page_time(alpha_of_M, turnover_M2, steps=200000):
    """NUMERICAL control: integrate dM/dt = -alpha(M)/M^2 from M=1; return t(M^2=turnover)/t_evap."""
    # integrate in M instead of t: dt/dM = -M^2/alpha(M); t(M) = int_M^1 m^2/alpha(m) dm
    def integ(a, b):
        h = (b - a) / steps
        s = 0.0
        f = lambda m: m * m / alpha_of_M(m)
        for i in range(steps):
            x0 = a + i * h
            xm = x0 + h / 2
            x1 = x0 + h
            s += h * (f(x0) + 4 * f(xm) + f(x1)) / 6
        return s
    Mp = math.sqrt(turnover_M2)
    return integ(Mp, 1.0) / integ(0.0, 1.0)


def run_C7(controls, res):
    t0 = time.perf_counter()
    out = {}
    # (a) exact ODE in u = M^3
    ok_a = True
    for a in [Fr(1), Fr(3, 7), Fr(22, 5)]:
        M03 = Fr(1)
        tev = M03 / (3 * a)
        u = lambda t: M03 - 3 * a * t
        for t, h in [(Fr(0), Fr(1, 1000)), (tev / 3, Fr(1, 77)), (tev / 2, Fr(5, 3))]:
            if (u(t + h) - u(t)) / h != -3 * a:
                ok_a = False
            if t / tev != 1 - u(t) / M03:
                ok_a = False
        if u(tev) != 0:
            ok_a = False
    out["a_cubic_law"] = {"exact_ok": ok_a,
                          "statement": "dM/dt=-a/M^2, a const => d(M^3)/dt=-3a, t_evap=M0^3/(3a), t/t_evap=1-(M/M0)^3"}
    # (b) half-entropy turnover
    f = Q2(1, Fr(-1, 4))
    chk = (Q2(1) - f) * (Q2(1) - f) * Q2(8)
    lo, hi = f.interval()
    out["b_half_entropy"] = {"t_P_over_t_evap": f.s(), "check_8(1-x)^2": chk.s(),
                             "interval_12dp": [dec(lo, 12), dec(hi + Fr(1, 10 ** 12), 12)]}
    ok_b = chk.a == 1 and chk.b == 0
    # numerical control
    num_b = simpson_page_time(lambda m: 1.0, 0.5, steps=20000)
    out["b_numerical_control"] = fx(num_b, 10)
    ok_b = ok_b and abs(num_b - float(lo)) < 1e-9
    # (c) multiplicative factor cancels
    ok_c = True
    for MP3 in [Fr(1, 8), Fr(27, 64), Fr(1, 2)]:
        ratios = set()
        for G in [Fr(1, 3), Fr(1), Fr(2), Fr(17, 5)]:
            a = G
            tev = Fr(1) / (3 * a)
            tP = (1 - MP3) / (3 * a)
            ratios.add(tP / tev)
        if ratios != {1 - MP3}:
            ok_c = False
    out["c_multiplicative_greybody"] = {"exact_ok": ok_c,
                                         "statement": "t_P/t_evap = (1-(M_P/M0)^3) for every constant a: a cancels"}
    # (d) mass-dependent coefficient
    pl = {}
    s2lo, s2hi = sqrt_interval(2)
    s4lo = sqrt_interval(s2lo)[0]
    s4hi = sqrt_interval(s2hi)[1]
    # p = 0: 1 - 2^{-3/2}; p = 1/2: 1 - 2^{-7/4} = 1 - 2^{1/4}/4; p = 1: 1 - 1/4
    pl["p=0"] = [dec(lo, 8), dec(hi + Fr(1, 10 ** 8), 8)]
    pl["p=1/2"] = [dec(1 - s4hi / 4, 8), dec(1 - s4lo / 4 + Fr(1, 10 ** 8), 8)]
    pl["p=1"] = str(Fr(3, 4))
    out["d_power_law_a_propto_M^-p"] = pl
    num_p = simpson_page_time(lambda m: m ** -0.5 if m > 0 else 1e300, 0.5, steps=20000)
    out["d_power_law_numerical_control_p=1/2"] = fx(num_p, 10)
    ok_d = abs(num_p - float(1 - s4hi / 4)) < 1e-7
    steps = []
    for ratio in [Fr(3, 2), Fr(2), Fr(4)]:
        rho = 1 / ratio
        for mu in [Fr(1, 100), Fr(1, 10), Fr(1, 2), Fr(3, 4), Fr(9, 10)]:
            m3 = mu ** 3
            Dn = 1 - m3 + rho * m3
            if mu * mu <= Fr(1, 2):
                val = Q2(1, Fr(-1, 4)).div_rational(Dn)
            else:
                val = Q2(1 - m3 + rho * m3, -rho / 4).div_rational(Dn)
            vlo, vhi = val.interval()
            alpha = (lambda mu_, r_: (lambda m: 1.0 if m > float(mu_) else float(r_)))(mu, ratio)
            num = simpson_page_time(alpha, 0.5, steps=4000)
            ok_d = ok_d and abs(num - float(vlo)) < 2e-3
            steps.append({"a2_over_a1": str(ratio), "mu=M*/M0": str(mu), "exact": val.s(),
                          "value_8dp": dec(vlo, 8), "numerical_control": fx(num, 6)})
    out["d_step_model"] = steps
    # (e) turnover criterion with beta
    beta_rows = []
    ok_e = True
    for beta in [Fr(1), Fr(4, 3), Fr(14847, 10000), Fr(3, 2), Fr(2)]:
        flo, fhi, y = page_fraction_beta(beta)
        beta_rows.append({"beta": str(beta), "S_BH_over_S0_at_turnover": dec(y, 6),
                          "BH_entropy_lost_fraction": dec(1 - y, 6),
                          "t_P_over_t_evap_8dp": dec(flo, 8)})
    flo, fhi, y = page_fraction_beta(Fr(14847, 10000))
    lit = (dec(flo + Fr(5, 100000), 4) == "0.5381" and dec(fhi + Fr(5, 100000), 4) == "0.5381"
           and dec(1 - y + Fr(5, 100000), 4) == "0.4025")
    out["e_beta_accounting"] = beta_rows
    out["e_literature_control"] = {"source": "Page 2013 (arXiv:1301.4995v3, read in full): beta = 1.48472 Eq. (2) p.6; t* = 0.53810 t_decay Eq. (8) p.11; 40.25% of S_BH lost p.12",
                                   "quoted_t_fraction": "0.5381", "quoted_entropy_lost": "0.4025",
                                   "computed_t_fraction_4dp": dec(flo + Fr(5, 100000), 4),
                                   "computed_entropy_lost_4dp": dec(1 - y + Fr(5, 100000), 4),
                                   "resolution": "4 decimal places; confirms the beta formula is Page's accounting, not an independent physics test",
                                   "reproduced": lit}
    controls["K-page2013"] = lit
    # (a) and (c) are algebraic identities checked at rational points, not controls;
    # K-ode is the independent Simpson integration of the ODE (b, d) plus the exact Q(sqrt2) check.
    controls["K-ode"] = ok_b and ok_d
    out["a_c_note"] = "a and c are algebraic identities checked at rational points; not counted as controls"
    # verdict
    out["verdict"] = "VOID (algebraic identity check failed)" if not (ok_a and ok_c) else (
        "CONDITIONAL: t_P/t_evap = 1 - 2^{-3/2} = %s holds exactly given (i) constant a in "
        "dM/dt=-a/M^2, (ii) turnover at half the initial black-hole entropy, i.e. radiation "
        "entropy equal to the black-hole entropy lost (beta=1, the identification "
        "n_R(t)=n_B(0)-n_B(t)), (iii) S_BH proportional to M^2. PROVED: a constant multiplicative greybody or "
        "species factor cancels. COUNTEREXAMPLE to the unconditional reading: an M-dependent "
        "effective coefficient changes the fraction (power law p=1/2 gives %s; step model up "
        "to %s for the cases computed), and with Page's coarse-grained accounting beta=1.4847 "
        "the fraction is %s, reproducing Page 2013 Eq. (8); in Page 2013, beta itself is computed from the "
        "species' greybody factors."
        % (dec(lo, 6), pl["p=1/2"][0][:8], max(s["value_8dp"] for s in steps)[:8],
           dec(flo, 4)))
    res["C7"] = out
    tick("C7", t0)


# ================================================================ K-ln

def run_Kln(controls, res):
    ok = True
    rows = []
    for x in [Fr(2), Fr(3), Fr(20, 3), Fr(45), Fr(7, 6)]:
        lo, hi = ln_interval(x)
        fl = math.log(float(x))
        cont = (float(lo) - 1e-12 <= fl <= float(hi) + 1e-12) and (hi - lo) < Fr(1, 10 ** 40)
        ok = ok and cont
        rows.append({"x": str(x), "lo_15dp": dec(lo, 15), "contains_float_log": cont})
    l2 = ln_interval(Fr(2))
    l4 = ln_interval(Fr(4))
    ok = ok and not (l4[1] < 2 * l2[0] or l4[0] > 2 * l2[1])
    res["K_ln"] = rows
    controls["K-ln"] = ok


# ================================================================ main

def run():
    controls = {}
    res = {"schema": "bh02_scramble_v1", "seeds": SEEDS, "page_like_tolerance_nats": PAGE_TOL}
    sections = [("K_ln", lambda: run_Kln(controls, res)),
                ("C1", lambda: run_C1(controls, res)),
                ("C2", lambda: run_C2(controls, res)),
                ("C3", lambda: run_C3(controls, res)),
                ("C4", lambda: run_C4(controls, res)),
                ("C5", lambda: run_C5(controls, res)),
                ("C6", lambda: run_C6(controls, res,
                                      res.get("C1", {}).get("verdict", "").startswith("PROVED"))),
                ("C7", lambda: run_C7(controls, res))]
    for name, fn in sections:
        try:
            fn()
        except Exception as e:  # a crashed section is a failed control, reported cleanly
            controls["section-%s-completed" % name] = False
            res[name] = {"exception": type(e).__name__}
    rngx = random.Random(4242)
    cross = 0.0
    for dim in (2, 3, 5, 8):
        M = [[complex(rngx.gauss(0, 1), rngx.gauss(0, 1)) for _ in range(dim)] for _ in range(dim)]
        H = [[(M[i][j] + M[j][i].conjugate()) / 2 for j in range(dim)] for i in range(dim)]
        e1 = sorted(jacobi_herm(H))
        e2 = embed_eigs(H)
        cross = max(cross, max(abs(x - y) for x, y in zip(e1, e2)))
    res["K_eig_cross_complex_vs_embedding_le_1e-10"] = cross <= 1e-10
    eig_ok = cross <= 1e-10 and (EIG["max_trace_dev"] <= EIG_TOL and EIG["max_purity_dev"] <= EIG_TOL
              and EIG["min_eig"] >= -EIG_TOL)
    controls["K-eig"] = eig_ok
    res["K_eig"] = {"diagonalizations": EIG["count"],
                    "max_trace_dev_le_1e-12": EIG["max_trace_dev"] <= 1e-12,
                    "max_purity_dev_le_1e-12": EIG["max_purity_dev"] <= 1e-12,
                    "min_eig_ge_-1e-12": EIG["min_eig"] >= -1e-12,
                    "tolerance_for_VOID": EIG_TOL}
    res["controls"] = dict(sorted(controls.items()))
    return res, controls


def main():
    res, controls = run()
    failed = sorted(k for k, v in controls.items() if not v)
    for label, dt in TIMES:
        sys.stderr.write("time %-4s %.1fs\n" % (label, dt))
    if failed:
        print("VOID: failed controls: " + ", ".join(failed))
        sys.exit(2)
    print(json.dumps(res, indent=1, sort_keys=True, ensure_ascii=True))


if __name__ == "__main__":
    main()
