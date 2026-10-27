"""Counterexample search for Main §3.2 Theorem (CP-indivisibility, framework scope).

Family: Phi_t(rho) = Tr_H[ U^t (rho (x) diag mu) U^-t ], U the permutation unitary of a
bijection phi of V x H.  For every bijection at (|V|,|H|) in {(2,2),(2,3),(3,2)}, several
diagonal priors mu, and every ordered pair of times (s,t) (residues mod the order of phi,
s != 0 mod order), compute EXACTLY:

  E1  diagonal preservation of Phi_s (and dephasing covariance D.Phi = Phi.D);
  E2  the populations T(t)_{ij} = <j|Phi_t(|i><i|)|j> against the classical count;
  E3  stochastic divisibility of T(t) by T(s) (exact LP, verified primal / Farkas certificate);
  E4  linear compatibility: does ANY linear Lambda with Lambda.Phi_s = Phi_t exist
      (rowspace(S_t) subset rowspace(S_s), exact rank)?
  E5  the lift: for each P-indivisible pair, the Farkas vector (Y,z) of E3 defines the
      diagonal Choi functional W = sum_{k,j} (sum_i Y_ij T(s)_ik + z_k) |k><k| (x) |j><j|,
      W >= 0, whose pairing with any CPTP Lambda satisfying Lambda.Phi_s = Phi_t would be
      sum Y.T(t) + sum z < 0 -- an exact dual certificate of CP-indivisibility.  (This
      formalizes the paper's proof; it is not independent of it.)
  E6  image-only classical divisibility: a linear L on S = rowspan T(s), with
      L(row_i T(s)) = row_i T(t), nonnegative on S cap R^n_+ (exact extreme-ray test).

NUMERICAL (independent of the proof, floating point):
  N1  distance between the PSD cone and the affine set of Choi matrices of trace-preserving
      Lambda with Lambda.Phi_s = Phi_t, by alternating projections, for every distinct
      P-indivisible pair and every distinct linearly-compatible P-divisible pair, plus
      positive / negative controls.
"""
import itertools, sys, time
from fractions import Fraction as F
import numpy as np
import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from exact_lp import stochastic_divisor

# ----------------------------------------------------------------- exact helpers
def rank(rows):
    M = [list(r) for r in rows]
    if not M:
        return 0
    r, ncol = 0, len(M[0])
    for c in range(ncol):
        piv = next((i for i in range(r, len(M)) if M[i][c] != 0), None)
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        pv = M[r][c]
        M[r] = [v / pv for v in M[r]]
        for i in range(len(M)):
            if i != r and M[i][c] != 0:
                f = M[i][c]
                M[i] = [a - f * b for a, b in zip(M[i], M[r])]
        r += 1
        if r == len(M):
            break
    return r


def perm_power(perm, t):
    N = len(perm)
    p = list(range(N))
    for _ in range(t):
        p = [perm[i] for i in p]
    return p


def order(perm):
    t, p = 1, list(perm)
    while p != list(range(len(perm))):
        p = [perm[i] for i in p]
        t += 1
    return t


def superop(perm_t, nV, nH, mu):
    """S[(c,d)][(a,b)] = <c|Phi(|a><b|)|d>, exact.  U|v,h> = |phi(v,h)>."""
    n = nV
    S = [[F(0)] * (n * n) for _ in range(n * n)]
    for a in range(n):
        for b in range(n):
            for h in range(nH):
                if mu[h] == 0:
                    continue
                pa = perm_t[a * nH + h]
                pb = perm_t[b * nH + h]
                va, ha = divmod(pa, nH)
                vb, hb = divmod(pb, nH)
                if ha == hb:  # partial trace over H
                    S[va * n + vb][a * n + b] += mu[h]
    return S


def classical_T(perm_t, nV, nH, mu):
    T = [[F(0)] * nV for _ in range(nV)]
    for i in range(nV):
        for h in range(nH):
            v, _ = divmod(perm_t[i * nH + h], nH)
            T[i][v] += mu[h]
    return T


def pops(S, n):
    return [[S[j * n + j][i * n + i] for j in range(n)] for i in range(n)]


def diag_checks(S, n):
    dp = all(S[c * n + d][a * n + a] == 0 for a in range(n) for c in range(n) for d in range(n) if c != d)
    cov = all(S[c * n + c][a * n + b] == 0 for a in range(n) for b in range(n) if a != b for c in range(n))
    return dp, cov


def lin_compatible(S1, S2):
    # exists L with L S1 = S2  <=>  rows of S2 in rowspace of S1... in the superop picture
    # L S1 = S2 means every row of S2 is a combination of rows of S1.
    return rank(S1) == rank(S1 + S2)


def lift_certificate(T1, T2, y, n):
    """y = Farkas vector of the exact LP: first n*n entries Y_ij (constraint (T1 M)_ij = T2_ij),
    last n entries z_k (row sums).  Returns True if W >= 0 (diagonal) and <W,.> < 0 on target."""
    Y = [[y[i * n + j] for j in range(n)] for i in range(n)]
    z = y[n * n:]
    w = [[sum(Y[i][j] * T1[i][k] for i in range(n)) + z[k] for j in range(n)] for k in range(n)]
    nonneg = all(w[k][j] >= 0 for k in range(n) for j in range(n))
    val = sum(Y[i][j] * T2[i][j] for i in range(n) for j in range(n)) + sum(z)
    return nonneg and val < 0


def image_divisible(T1, T2, n):
    """Exact: linear compat on rowspan(T1) and nonnegativity of L on S cap R^n_+.
    Extreme rays of the polyhedral cone S cap R^n_+ are found by brute force over supports."""
    if rank(T1) != rank([r1 + r2 for r1, r2 in zip(T1, T2)]):  # colspan(T2) in colspan(T1)
        return False
    # parametrize S by coefficient vectors c (len n): r = c T1, image = c T2.
    # S cap R^n_+ is generated by vectors r in S, r >= 0, with maximal zero sets; enumerate
    # zero sets Z, solve c T1 restricted to Z = 0, collect 1-dim solution spaces.
    rT1 = rank(T1)
    rays = []
    for size in range(n + 1):
        for Z in itertools.combinations(range(n), size):
            # linear system in c: sum_i c_i T1[i][z] = 0 for z in Z
            rows = [[T1[i][z] for i in range(n)] for z in Z]
            # nullspace of rows (n unknowns); modulo the left kernel of T1 (c with cT1=0)
            # compute basis of {c: rows c = 0}
            null = nullspace(rows, n)
            imgs = []
            for c in null:
                r = [sum(c[i] * T1[i][k] for i in range(n)) for k in range(n)]
                imgs.append((r, c))
            # keep the image dimension of the solution space in S
            vecs = [r for r, _ in imgs]
            if rank(vecs) != 1:
                continue
            r, c = next((rc for rc in imgs if any(v != 0 for v in rc[0])))
            if all(v >= 0 for v in r):
                rays.append(c)
            elif all(v <= 0 for v in r):
                rays.append([-v for v in c])
    for c in rays:
        img = [sum(c[i] * T2[i][k] for i in range(n)) for k in range(n)]
        if any(v < 0 for v in img):
            return False
    return True


def nullspace(rows, n):
    if not rows:
        return [[F(1) if i == j else F(0) for i in range(n)] for j in range(n)]
    M = [list(r) for r in rows]
    piv_cols, r = [], 0
    for c in range(n):
        p = next((i for i in range(r, len(M)) if M[i][c] != 0), None)
        if p is None:
            continue
        M[r], M[p] = M[p], M[r]
        pv = M[r][c]
        M[r] = [v / pv for v in M[r]]
        for i in range(len(M)):
            if i != r and M[i][c] != 0:
                f = M[i][c]
                M[i] = [a - f * b for a, b in zip(M[i], M[r])]
        piv_cols.append(c)
        r += 1
        if r == len(M):
            break
    free = [c for c in range(n) if c not in piv_cols]
    basis = []
    for fc in free:
        v = [F(0)] * n
        v[fc] = F(1)
        for i, pc in enumerate(piv_cols):
            v[pc] = -M[i][fc]
        basis.append(v)
    return basis

# ----------------------------------------------------------------- numerical SDP control
def cp_gap(S1, S2, n, iters=4000):
    """Alternating projections between {Choi J >= 0} and the affine set of TP Lambda with
    Lambda S1 = S2.  Returns the final distance (Frobenius)."""
    S1 = np.array(S1, dtype=float); S2 = np.array(S2, dtype=float)
    d2 = n * n
    # unknown L (d2 x d2), vec row-major: x[p*d2+q] = L[p][q]
    rows, rhs = [], []
    # L S1 = S2: for each (p, r): sum_q L[p][q] S1[q][r] = S2[p][r]
    for p in range(d2):
        for r in range(d2):
            row = np.zeros(d2 * d2)
            row[p * d2:(p + 1) * d2] = S1[:, r]
            rows.append(row); rhs.append(S2[p, r])
    # TP: sum_c L[(c,c)][(a,b)] = delta_ab
    for a in range(n):
        for b in range(n):
            row = np.zeros(d2 * d2)
            for c in range(n):
                row[(c * n + c) * d2 + (a * n + b)] = 1.0
            rows.append(row); rhs.append(1.0 if a == b else 0.0)
    C = np.array(rows); dvec = np.array(rhs)
    Cp = np.linalg.pinv(C)
    resid = C @ (Cp @ dvec) - dvec
    if np.linalg.norm(resid) > 1e-9:
        return float("inf")  # affine set empty: no linear TP Lambda
    def projA(x):
        return x - Cp @ (C @ x - dvec)
    # reshuffle L[(c,d),(a,b)] <-> J[(a,c),(b,d)]
    idx = np.zeros((d2, d2, 2), dtype=int)
    def L2J(L):
        L4 = L.reshape(n, n, n, n)          # c,d,a,b
        return L4.transpose(2, 0, 3, 1).reshape(d2, d2)
    def J2L(J):
        J4 = J.reshape(n, n, n, n)          # a,c,b,d
        return J4.transpose(1, 3, 0, 2).reshape(d2, d2)
    def projP(x):
        J = L2J(x.reshape(d2, d2).astype(complex))
        J = 0.5 * (J + J.conj().T)
        w, V = np.linalg.eigh(J)
        J = (V * np.clip(w, 0, None)) @ V.conj().T
        return J2L(J).reshape(-1)
    x = projA(np.zeros(d2 * d2, dtype=complex))
    gap = None
    for _ in range(iters):
        y = projP(x)
        x = projA(y)
        gap = np.linalg.norm(x - y)
    return float(gap)

# ----------------------------------------------------------------- run
def priors(nH):
    if nH == 2:
        return [(F(1, 2), F(1, 2)), (F(1, 3), F(2, 3)), (F(1), F(0))]
    return [(F(1, 3),) * 3, (F(1, 2), F(1, 3), F(1, 6)), (F(1, 2), F(1, 2), F(0))]


def main(do_numeric=True):
    t0 = time.time()
    summary = {}
    num_pairs_indiv = {}
    num_pairs_div = {}
    image_gap_examples = []
    converse_examples = []
    for (nV, nH) in [(2, 2), (2, 3), (3, 2)]:
        N = nV * nH
        stats = dict(perms=0, priors=0, pairs=0, diag_fail=0, cov_fail=0, pop_fail=0,
                     p_indiv=0, p_div=0, lift_ok=0, lift_fail=0,
                     p_div_lin_incompat=0, p_div_lin_compat=0,
                     indiv_but_image_div=0, p_indiv_lin_compat=0)
        for perm in itertools.permutations(range(N)):
            perm = list(perm)
            stats["perms"] += 1
            L = order(perm)
            for mu in priors(nH):
                stats["priors"] += 1
                Ss = {}; Ts = {}
                for t in range(L):
                    pt = perm_power(perm, t)
                    S = superop(pt, nV, nH, mu)
                    Ss[t] = S
                    Ts[t] = pops(S, nV)
                    dp, cov = diag_checks(S, nV)
                    stats["diag_fail"] += (not dp)
                    stats["cov_fail"] += (not cov)
                    stats["pop_fail"] += (Ts[t] != classical_T(pt, nV, nH, mu))
                for s in range(1, L):
                    for t in range(L):
                        if t == s:
                            continue
                        stats["pairs"] += 1
                        T1, T2 = Ts[s], Ts[t]
                        ok, cert = stochastic_divisor(T1, T2)
                        lc = lin_compatible(Ss[s], Ss[t])
                        key = (nV, tuple(map(tuple, Ss[s])), tuple(map(tuple, Ss[t])))
                        if not ok:
                            stats["p_indiv"] += 1
                            if lift_certificate(T1, T2, cert, nV):
                                stats["lift_ok"] += 1
                            else:
                                stats["lift_fail"] += 1
                            if lc:
                                stats["p_indiv_lin_compat"] += 1
                                num_pairs_indiv.setdefault(key, (nV, nH, perm, mu, s, t))
                            if image_divisible(T1, T2, nV):
                                stats["indiv_but_image_div"] += 1
                                if len(image_gap_examples) < 5:
                                    image_gap_examples.append((nV, nH, perm, mu, s, t, T1, T2))
                        else:
                            stats["p_div"] += 1
                            if lc:
                                stats["p_div_lin_compat"] += 1
                                num_pairs_div.setdefault(key, (nV, nH, perm, mu, s, t))
                            else:
                                stats["p_div_lin_incompat"] += 1
                                if len(converse_examples) < 3:
                                    converse_examples.append((nV, nH, perm, mu, s, t, T1, T2))
        summary[(nV, nH)] = stats
        print((nV, nH), stats, f"[{time.time()-t0:.0f}s]", flush=True)

    print("\nconverse-failure examples (P-divisible populations, no linear Lambda at all "
          "=> CP-indivisible, exact):")
    for ex in converse_examples:
        print("  ", ex[:6], "T(s)=", [[str(v) for v in r] for r in ex[6]],
              "T(t)=", [[str(v) for v in r] for r in ex[7]])
    print("\nP-indivisible yet image-only classically divisible (exact):", len(image_gap_examples) and "examples:")
    for ex in image_gap_examples:
        print("  ", ex[:6], "T(s)=", [[str(v) for v in r] for r in ex[6]],
              "T(t)=", [[str(v) for v in r] for r in ex[7]])

    if not do_numeric:
        return
    # ---- numerical controls
    n2 = lambda M: [[F(v) for v in r] for r in M]
    s = F(1, 2)
    # Hadamard pair (outside class): CP-divisible -> gap ~ 0
    def adU(U, n):
        U = np.array(U)
        S = np.zeros((n * n, n * n))
        for a in range(n):
            for b in range(n):
                E = np.zeros((n, n)); E[a, b] = 1
                X = U @ E @ U.T
                for c in range(n):
                    for d in range(n):
                        S[c * n + d, a * n + b] = X[c, d]
        return S.tolist()
    Hd = [[2 ** -0.5, 2 ** -0.5], [2 ** -0.5, -2 ** -0.5]]
    Id4 = np.eye(4).tolist()
    deph = np.diag([1, 0, 0, 1]).astype(float).tolist()
    print("\nNUMERICAL controls (alternating projections, final Frobenius gap):")
    print("  +control Hadamard pair  Ad_H -> id     gap = %.2e  (expect ~0)" % cp_gap(adU(Hd, 2), Id4, 2))
    print("  +control id -> dephasing               gap = %.2e  (expect ~0)" % cp_gap(Id4, deph, 2))
    print("  -control dephasing -> id               gap = %s   (expect inf: no linear Lambda)" % cp_gap(deph, Id4, 2))
    # transposition map is positive, not CP: target id -> transpose
    transp = np.zeros((4, 4))
    for a in range(2):
        for b in range(2):
            transp[b * 2 + a, a * 2 + b] = 1
    print("  -control id -> transpose (P not CP)    gap = %.2e  (expect > 0)" % cp_gap(Id4, transp.tolist(), 2))

    print("\nNUMERICAL: distinct P-indivisible, linearly compatible pairs:", len(num_pairs_indiv))
    gaps = []
    for key, info in num_pairs_indiv.items():
        nV = key[0]
        g = cp_gap([list(r) for r in key[1]], [list(r) for r in key[2]], nV)
        gaps.append((g, info))
    gaps.sort(key=lambda z: z[0])
    if gaps:
        print("  min gap = %.3e  at %s" % (gaps[0][0], gaps[0][1][:6]))
        print("  #gap < 1e-4:", sum(1 for g, _ in gaps if g < 1e-4))
    print("NUMERICAL: distinct P-divisible, linearly compatible pairs:", len(num_pairs_div))
    gd = []
    for key, info in num_pairs_div.items():
        nV = key[0]
        g = cp_gap([list(r) for r in key[1]], [list(r) for r in key[2]], nV)
        gd.append((g, info))
    gd.sort(key=lambda z: z[0])
    print("  #gap < 1e-4 (numerically CP-divisible):", sum(1 for g, _ in gd if g < 1e-4),
          "  #gap > 1e-3 (numerically CP-indivisible):", sum(1 for g, _ in gd if g > 1e-3),
          "  ambiguous:", sum(1 for g, _ in gd if 1e-4 <= g <= 1e-3))
    for g, info in gd[-3:]:
        print("   largest-gap P-divisible pair: gap=%.3e %s" % (g, info[:6]))
    print(f"done [{time.time()-t0:.0f}s]")


if __name__ == "__main__":
    main(do_numeric=("--no-numeric" not in sys.argv))
