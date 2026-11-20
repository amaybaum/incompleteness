#!/usr/bin/env python3
"""A1-EXIT R6 controls K1-K4 (PREREG.md section 4). Exact rational arithmetic only.

Usage: python3 r6_controls.py [OUT.json]
Writes the outcome of every control to OUT.json (default r6_controls.json beside this file) in the
schema "a1exit-r6-controls/1" and exits nonzero if any control fails. Deterministic.

Operators on C^V are real |V|x|V| matrices of Fractions (every quantity below is real).
"""
import itertools
import json
import os
import sys
from fractions import Fraction as Q

ONE, ZERO = Q(1), Q(0)


# ---------------------------------------------------------------- linear algebra over Q
def zeros(r, c):
    return [[ZERO] * c for _ in range(r)]


def matmul(A, B):
    n, k, m = len(A), len(B), len(B[0])
    out = zeros(n, m)
    for i in range(n):
        Ai = A[i]
        for l in range(k):
            a = Ai[l]
            if a:
                Bl = B[l]
                row = out[i]
                for j in range(m):
                    if Bl[j]:
                        row[j] += a * Bl[j]
    return out


def transpose(A):
    return [list(r) for r in zip(*A)]


def det(A):
    A = [list(r) for r in A]
    n = len(A)
    d = ONE
    for c in range(n):
        p = next((r for r in range(c, n) if A[r][c] != 0), None)
        if p is None:
            return ZERO
        if p != c:
            A[c], A[p] = A[p], A[c]
            d = -d
        d *= A[c][c]
        for r in range(c + 1, n):
            f = A[r][c] / A[c][c]
            if f:
                for j in range(c, n):
                    A[r][j] -= f * A[c][j]
    return d


def inverse(A):
    n = len(A)
    M = [list(A[i]) + [ONE if i == j else ZERO for j in range(n)] for i in range(n)]
    for c in range(n):
        p = next((r for r in range(c, n) if M[r][c] != 0), None)
        if p is None:
            return None
        M[c], M[p] = M[p], M[c]
        pv = M[c][c]
        M[c] = [x / pv for x in M[c]]
        for r in range(n):
            if r != c and M[r][c] != 0:
                f = M[r][c]
                M[r] = [x - f * y for x, y in zip(M[r], M[c])]
    return [row[n:] for row in M]


def is_psd(A):
    """Exact PSD test for a real symmetric matrix by symmetric Gaussian elimination: A is PSD iff a
    positive pivot exists and its Schur complement is PSD, or every remaining diagonal entry is zero
    and so is every remaining entry."""
    n = len(A)
    for i in range(n):
        for j in range(n):
            if A[i][j] != A[j][i]:
                return False
    M = [list(r) for r in A]
    active = list(range(n))
    while active:
        if any(M[i][i] < 0 for i in active):
            return False
        piv = next((i for i in active if M[i][i] > 0), None)
        if piv is None:
            return all(M[i][j] == 0 for i in active for j in active)
        rest = [i for i in active if i != piv]
        d = M[piv][piv]
        for j in rest:
            f = M[j][piv] / d
            if f:
                for k in rest:
                    M[j][k] -= f * M[piv][k]
        active = rest
    return True


# ---------------------------------------------------------------- channels on C^V as superoperators
def unit(n, i, j):
    E = zeros(n, n)
    E[i][j] = ONE
    return E


def superop(channel_on_units, n):
    """channel_on_units[(i,j)] = n x n matrix image of |i><j|. Returns (n^2 x n^2) matrix S with
    vec(Phi(X)) = S vec(X), vec row-major."""
    S = zeros(n * n, n * n)
    for i in range(n):
        for j in range(n):
            img = channel_on_units[(i, j)]
            for a in range(n):
                for b in range(n):
                    S[a * n + b][i * n + j] = img[a][b]
    return S


def choi_of_superop(S, n):
    """Choi J = sum_ij |i><j| (x) Phi(|i><j|), indices (i,a),(j,b)."""
    J = zeros(n * n, n * n)
    for i in range(n):
        for j in range(n):
            for a in range(n):
                for b in range(n):
                    J[i * n + a][j * n + b] = S[a * n + b][i * n + j]
    return J


def is_cptp(S, n):
    for i in range(n):
        for j in range(n):
            tr = sum(S[a * n + a][i * n + j] for a in range(n))
            if tr != (ONE if i == j else ZERO):
                return False
    return is_psd(choi_of_superop(S, n))


def diag_preserving_with(S, n, Gamma):
    """Phi(|x><x|) = sum_b Gamma[x][b] |b><b|."""
    for x in range(n):
        for a in range(n):
            for b in range(n):
                want = Gamma[x][a] if a == b else ZERO
                if S[a * n + b][x * n + x] != want:
                    return False
    return True


# ---------------------------------------------------------------- stochastic divisibility (|V| = 2, exact)
def stochastic_divisor_exists_2(G1, G2):
    """Exists row-stochastic L with G2 = G1 L ? (2x2, exact)."""
    d = G1[0][0] * G1[1][1] - G1[0][1] * G1[1][0]
    if d != 0:
        L = matmul(inverse(G1), G2)
        return all(x >= 0 for r in L for x in r)
    # singular row-stochastic 2x2: identical rows r; G1 L has identical rows rL; take L rows = G2 row
    return G2[0] == G2[1]


def p_divisible_2(Gs):
    T = len(Gs)
    for s in range(T):
        for t in range(s + 1, T):
            if not stochastic_divisor_exists_2(Gs[s], Gs[t]):
                return False, (s, t)
    return True, None


# ---------------------------------------------------------------- finite models
def all_bijections(nV, nH):
    pts = [(x, h) for x in range(nV) for h in range(nH)]
    for perm in itertools.permutations(range(len(pts))):
        yield {pts[i]: pts[perm[i]] for i in range(len(pts))}


def power_map(F, t, nV, nH):
    out = {}
    for x in range(nV):
        for h in range(nH):
            p = (x, h)
            for _ in range(t):
                p = F[p]
            out[(x, h)] = p
    return out


def rooted(Ft, prior, nV, nH):
    G = zeros(nV, nV)
    for x in range(nV):
        for h in range(nH):
            G[x][Ft[(x, h)][0]] += prior[h]
    return G


def mixture_channel(Ft, prior, nV, nH):
    """The T6 family: sum_h prior(h) * pattern channel of x -> F^t(x,h)."""
    out = {(i, j): zeros(nV, nV) for i in range(nV) for j in range(nV)}
    for h in range(nH):
        w = prior[h]
        if not w:
            continue
        for x in range(nV):
            for y in range(nV):
                ax, kx = Ft[(x, h)]
                ay, ky = Ft[(y, h)]
                if kx == ky:
                    out[(x, y)][ax][ay] += w
    return superop(out, nV)


def partial_trace_channel(F, t, rho_H, nV, nH):
    """Main's family Tr_H[U^t (X (x) rho_H) U^{-t}] by explicit matrix products (independent path)."""
    N = nV * nH
    idx = lambda x, h: x * nH + h
    U = zeros(N, N)
    for (x, h), (a, k) in F.items():
        U[idx(a, k)][idx(x, h)] = ONE
    Ut = [[ONE if i == j else ZERO for j in range(N)] for i in range(N)]
    for _ in range(t):
        Ut = matmul(U, Ut)
    Utd = transpose(Ut)
    out = {}
    for i in range(nV):
        for j in range(nV):
            X = zeros(N, N)
            for h in range(nH):
                for k in range(nH):
                    X[idx(i, h)][idx(j, k)] = rho_H[h][k]
            Y = matmul(matmul(Ut, X), Utd)
            R = zeros(nV, nV)
            for a in range(nV):
                for b in range(nV):
                    R[a][b] = sum(Y[idx(a, k)][idx(b, k)] for k in range(nH))
            out[(i, j)] = R
    return superop(out, nV)


def koopman_channel(Ft, psi, nV, nH):
    """Koopman form: Tr_H[U^t (X (x) |psi><psi|) U^{-t}], psi a real vector on H."""
    out = {(i, j): zeros(nV, nV) for i in range(nV) for j in range(nV)}
    # <a,k|U^t|x,psi> = psi(h) for the unique h with F^t(x,h) = (a,k)
    amp = {}
    for x in range(nV):
        for h in range(nH):
            amp[(x,) + Ft[(x, h)]] = psi[h]
    for x in range(nV):
        for y in range(nV):
            for a in range(nV):
                for b in range(nV):
                    s = ZERO
                    for k in range(nH):
                        s += amp.get((x, a, k), ZERO) * amp.get((y, b, k), ZERO)
                    out[(x, y)][a][b] = s
    return superop(out, nV)


def diag(v):
    n = len(v)
    return [[v[i] if i == j else ZERO for j in range(n)] for i in range(n)]


# ---------------------------------------------------------------- K1
def k1():
    cases = [(2, 2), (2, 3), (3, 2)]
    checked, mismatches, not_cptp, not_diag = 0, 0, 0, 0
    first_mismatch = None
    for nV, nH in cases:
        priors = [[Q(1, nH)] * nH]
        if nH == 2:
            priors += [[Q(1, 3), Q(2, 3)], [Q(1), Q(0)]]
        else:
            priors += [[Q(1, 2), Q(1, 3), Q(1, 6)], [Q(0), Q(1, 4), Q(3, 4)]]
        for F in all_bijections(nV, nH):
            for prior in priors:
                rhoH = diag(prior)
                for t in range(1, 7):
                    Ft = power_map(F, t, nV, nH)
                    Sm = mixture_channel(Ft, prior, nV, nH)
                    Sp = partial_trace_channel(F, t, rhoH, nV, nH)
                    checked += 1
                    if Sm != Sp:
                        mismatches += 1
                        if first_mismatch is None:
                            first_mismatch = {"nV": nV, "nH": nH, "t": t}
                    if not is_cptp(Sm, nV):
                        not_cptp += 1
                    if not diag_preserving_with(Sm, nV, rooted(Ft, prior, nV, nH)):
                        not_diag += 1
    ok = mismatches == 0 and not_cptp == 0 and not_diag == 0
    return {"pass": ok, "cases": [list(c) for c in cases], "t_max": 6, "priors_per_case": 3,
            "comparisons": checked, "mismatches": mismatches, "first_mismatch": first_mismatch,
            "mixture_not_cptp": not_cptp, "mixture_not_diagonal_with_rooted_populations": not_diag}


# ---------------------------------------------------------------- K2
def stochastic_divisor_exists(G1, G2):
    """True/False if decided exactly, None if undecided (|V| > 2 with singular G1)."""
    if len(G1) == 2:
        return stochastic_divisor_exists_2(G1, G2)
    inv = inverse(G1)
    if inv is None:
        return None
    L = matmul(inv, G2)
    return all(x >= 0 for r in L for x in r)


def k2_search(cases, t_max, cache):
    out = {"searched": [], "p_indivisible_pairs": 0, "decided_pairs": 0,
           "undecided_singular_channel": 0, "undecided_singular_gamma": 0,
           "countermodels": 0, "first_countermodel": None, "population_mismatch": 0,
           "v2_coherent_part_equal_violations": 0}
    for nV, nH in cases:
        psi = [ONE] * nH
        norm = Q(1, nH)
        prior = [Q(1, nH)] * nH
        n_bij = 0
        for F in all_bijections(nV, nH):
            n_bij += 1
            Ss, Gs = [], []
            for t in range(0, t_max + 1):
                Ft = power_map(F, t, nV, nH)
                S = koopman_channel(Ft, psi, nV, nH)
                S = tuple(tuple(x * norm for x in r) for r in S)
                G = rooted(Ft, prior, nV, nH)
                if not diag_preserving_pop(S, nV, G):
                    out["population_mismatch"] += 1
                if nV == 2 and S[1][0] != S[1][3]:
                    # off-diagonal entry of Phi_t(|0><0|) versus Phi_t(|1><1|)
                    out["v2_coherent_part_equal_violations"] += 1
                Ss.append(S)
                Gs.append(G)
            for t1 in range(1, t_max + 1):
                for t2 in range(t1 + 1, t_max + 1):
                    sd = stochastic_divisor_exists(Gs[t1], Gs[t2])
                    if sd is None:
                        out["undecided_singular_gamma"] += 1
                        continue
                    if sd:
                        continue
                    out["p_indivisible_pairs"] += 1
                    key = (Ss[t1], Ss[t2])
                    if key not in cache:
                        inv = inverse([list(r) for r in Ss[t1]])
                        if inv is None:
                            cache[key] = None
                        else:
                            L = matmul([list(r) for r in Ss[t2]], inv)
                            cache[key] = is_cptp(L, nV)
                    if cache[key] is None:
                        out["undecided_singular_channel"] += 1
                        continue
                    out["decided_pairs"] += 1
                    if cache[key]:
                        out["countermodels"] += 1
                        if out["first_countermodel"] is None:
                            Sm1 = mixture_channel(power_map(F, t1, nV, nH), prior, nV, nH)
                            Sm2 = mixture_channel(power_map(F, t2, nV, nH), prior, nV, nH)
                            out["first_countermodel"] = {
                                "nV": nV, "nH": nH, "t1": t1, "t2": t2,
                                "F": {f"{k[0]},{k[1]}": f"{v[0]},{v[1]}" for k, v in sorted(F.items())},
                                "Gamma_t1": [[str(v) for v in r] for r in Gs[t1]],
                                "Gamma_t2": [[str(v) for v in r] for r in Gs[t2]],
                                "koopman_Phi_t1_on_diagonal_units": [[[str(Ss[t1][a * nV + b][x * nV + x]) for b in range(nV)] for a in range(nV)] for x in range(nV)],
                                "mixture_divisibility_same_pair": cp_divisible_mixture(Sm1, Sm2, nV),
                            }
        out["searched"].append({"nV": nV, "nH": nH, "bijections": n_bij, "t_max": t_max})
    return out


def k2():
    res = {}
    # (i) diagonal preservation: the swap at |V| = |H| = 2
    swap = {(x, h): (h, x) for x in range(2) for h in range(2)}
    S = koopman_channel(power_map(swap, 1, 2, 2), [ONE, ONE], 2, 2)
    S = [[x * Q(1, 2) for x in r] for r in S]
    out00 = [[S[a * 2 + b][0] for b in range(2)] for a in range(2)]
    res["diag_failure_example"] = {"F": "swap (x,h)->(h,x), |V|=|H|=2", "psi": "constant, normalized",
                                   "Phi_1(|0><0|)": [[str(v) for v in r] for r in out00],
                                   "off_diagonal_nonzero": out00[0][1] != 0}
    cache = {}
    # (ii) preregistered search
    res["prereg"] = k2_search([(2, 2), (2, 3), (2, 4)], 12, cache)
    # (iii) exploratory extension added after preregistration (reported separately)
    res["extension_v3"] = k2_search([(3, 2)], 8, cache)
    res["pass"] = (res["prereg"]["population_mismatch"] == 0
                   and res["extension_v3"]["population_mismatch"] == 0)
    return res


def diag_preserving_pop(S, n, Gamma):
    for x in range(n):
        for a in range(n):
            if S[a * n + a][x * n + x] != Gamma[x][a]:
                return False
    return True


def cp_divisible_mixture(S1, S2, n):
    """For the record: is there any linear Lambda with S2 = Lambda S1 (kernel test), and if S1 is
    invertible, is Lambda CP?"""
    inv = inverse(S1)
    if inv is None:
        # a linear Lambda exists iff ker S1 is contained in ker S2; test on the diagonal units
        d = [[S1[r][x * n + x] for r in range(n * n)] for x in range(n)]
        d2 = [[S2[r][x * n + x] for r in range(n * n)] for x in range(n)]
        for x in range(n):
            for y in range(x + 1, n):
                if d[x] == d[y] and d2[x] != d2[y]:
                    return "no linear Lambda (S1 identifies two diagonal inputs that S2 separates)"
        return "undetermined (S1 singular)"
    return "CP" if is_cptp(matmul(S2, inv), n) else "not CP"


# ---------------------------------------------------------------- K3: diffuse carriers on cylinders
def cylinder_family(step_V, step_H, window, t_max):
    """h is a 0/1 sequence on the index set `window` (a cylinder of the diffuse law, mass
    2^-len(window)); step_V(x, h) -> new visible bit; step_H(h) -> new hidden window. The window is
    chosen large enough that F^t on it is exact for t <= t_max (stated per model). Returns, per t,
    the rooted matrix and the mixture superoperator."""
    n = 2
    L = len(window)
    w = Q(1, 2 ** L)
    out = []
    for t in range(t_max + 1):
        G = zeros(2, 2)
        units = {(i, j): zeros(2, 2) for i in range(2) for j in range(2)}
        for bits in itertools.product((0, 1), repeat=L):
            h0 = dict(zip(window, bits))
            traj = {}
            for x in range(2):
                xv, hv = x, h0
                for _ in range(t):
                    xv, hv = step_V(xv, hv), step_H(hv)
                traj[x] = (xv, tuple(sorted(hv.items())))
            for x in range(2):
                G[x][traj[x][0]] += w
                for y in range(2):
                    if traj[x][1] == traj[y][1]:
                        units[(x, y)][traj[x][0]][traj[y][0]] += w
        out.append((G, superop(units, n)))
    return out


def nr_holds(Gs, Gn):
    """Main M:131 (NR) for some pair a != b sharing a column of Gs:
    (1 - Gn[a][a]) + (1 - Gn[b][b]) < min(Gs[a][x], Gs[b][x])."""
    n = len(Gs)
    for a in range(n):
        for b in range(n):
            if a == b:
                continue
            for x in range(n):
                m = min(Gs[a][x], Gs[b][x])
                if m > 0 and (ONE - Gn[a][a]) + (ONE - Gn[b][b]) < m:
                    return True
    return False


def k3():
    t_max = 8
    # K3a Bernoulli skew product F(x,h) = (x xor h_0, sigma h), (sigma h)_i = h_{i+1}.
    # Window {0..t_max+1}: the visible bit after t steps reads h_0..h_{t-1}; sigma^t h is compared on
    # the shifted window (identical for both roots because sigma does not read x).
    win = list(range(0, t_max + 2))
    stepV = lambda x, h: x ^ h[0]
    stepH = lambda h: {i - 1: v for i, v in h.items()}
    fam = cylinder_family(stepV, stepH, win, t_max)
    a_cptp = all(is_cptp(S, 2) for _, S in fam)
    a_diag = all(diag_preserving_with(S, 2, G) for G, S in fam)
    a_pdiv, a_wit = p_divisible_2([G for G, _ in fam])
    # K3b dyadic odometer: h in {0,1}^N, odo(h) = h + 1 with carry to the right (2-adic integers),
    # F(x,h) = (x xor h_0, odo h). Window {0..L-1}; carries out of the window are dropped, which
    # leaves coordinates 0..L-1 of odo^t(h) exact (carry propagates only to higher indices).
    L = 5

    def odo(h):
        h = dict(h)
        i = 0
        while i in h:
            if h[i] == 0:
                h[i] = 1
                break
            h[i] = 0
            i += 1
        return h

    famb = cylinder_family(lambda x, h: x ^ h[0], odo, list(range(L)), t_max)
    b_cptp = all(is_cptp(S, 2) for _, S in famb)
    b_diag = all(diag_preserving_with(S, 2, G) for G, S in famb)
    b_pdiv, b_wit = p_divisible_2([G for G, _ in famb])
    b_cp = None
    if b_wit is not None:
        s, t = b_wit
        b_cp = cp_divisible_mixture([list(r) for r in famb[s][1]], [list(r) for r in famb[t][1]], 2)
    gam = lambda fam_, t: [[str(v) for v in r] for r in fam_[t][0]]
    return {
        "pass": a_cptp and a_diag and b_cptp and b_diag,
        "note": "pass records CPTP and diagonal preservation; the P-divisibility and (NR) entries are reported outcomes",
        "K3a_bernoulli": {"cptp_all_t": a_cptp, "diag_rooted_all_t": a_diag,
                          "Gamma_1": gam(fam, 1), "Gamma_2": gam(fam, 2),
                          "P_divisible_on_0_8": a_pdiv, "first_failing_pair": a_wit},
        "K3b_odometer": {"cptp_all_t": b_cptp, "diag_rooted_all_t": b_diag,
                         "Gamma_1": gam(famb, 1), "Gamma_2": gam(famb, 2), "Gamma_4": gam(famb, 4),
                         "NR_at_s1_n4": nr_holds(famb[1][0], famb[4][0]),
                         "P_divisible_on_0_8": b_pdiv, "first_failing_pair": b_wit,
                         "mixture_divisibility_at_failing_pair": b_cp},
    }


# ---------------------------------------------------------------- K4: relabelling on [0,1) with Lebesgue
def k4():
    # F(x,h) = (x xor [h < 1/2], h). Conjugating by pi(v,h) = (v, s(h)) gives
    # F'(x,h) = (x xor [s^{-1}(h) < 1/2], h). Flip probability = Leb{h : s^{-1}(h) < 1/2} = Leb(s([0,1/2))).
    # s(h) = h^2 (increasing bijection of [0,1), not Lebesgue-preserving): s([0,1/2)) = [0,1/4).
    # s(h) = 1 - h on (0,1), 0 -> 0 (Lebesgue-preserving up to a null set): s([0,1/2)) = (1/2,1] mod null.
    p_orig = Q(1, 2)
    p_sq = Q(1, 2) ** 2                # Leb[0, (1/2)^2)
    p_refl = ONE - Q(1, 2)             # Leb(1/2, 1)
    G = lambda p: [[str(ONE - p), str(p)], [str(p), str(ONE - p)]]
    return {"pass": p_sq != p_orig and p_refl == p_orig,
            "Gamma_1_original": G(p_orig), "Gamma_1_after_h_squared": G(p_sq),
            "Gamma_1_after_reflection": G(p_refl)}


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    out_path = sys.argv[1] if len(sys.argv) > 1 else os.path.join(here, "r6_controls.json")
    controls = {"K1": k1(), "K2": k2(), "K3": k3(), "K4": k4()}
    report = {"schema": "a1exit-r6-controls/1", "controls": controls,
              "all_pass": all(c["pass"] for c in controls.values())}
    with open(out_path, "w") as f:
        json.dump(report, f, indent=1, sort_keys=True)
        f.write("\n")
    for k, c in controls.items():
        print(k, "PASS" if c["pass"] else "FAIL")
    print("K2 countermodels prereg/ext:", controls["K2"]["prereg"]["countermodels"], controls["K2"]["extension_v3"]["countermodels"])
    sys.exit(0 if report["all_pass"] else 1)


if __name__ == "__main__":
    main()
