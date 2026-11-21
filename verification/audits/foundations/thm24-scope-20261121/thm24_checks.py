#!/usr/bin/env python3
"""THM24-SCOPE exact checks (NOTE.md section 5).

Exact arithmetic only: rationals from `fractions`, complex numbers as pairs of rationals.
Carrier |C_V| = 2, |C_H| = 2, all 24 bijections of S = C_V x C_H, times t = 1..4, every matrix
unit |x><y| as visible input. Writes thm24_checks.json beside this file and exits 0 iff every
claim and every control comes out as preregistered.

Usage: python3 thm24_checks.py [--out PATH]
"""
import itertools
import json
import os
import sys
from fractions import Fraction as Fr

NV, NH, TMAX = 2, 2, 4


# ---------- exact Gaussian rationals ----------
class Q:
    __slots__ = ("re", "im")

    def __init__(self, re=0, im=0):
        self.re, self.im = Fr(re), Fr(im)

    def __add__(self, o):
        return Q(self.re + o.re, self.im + o.im)

    def __sub__(self, o):
        return Q(self.re - o.re, self.im - o.im)

    def __mul__(self, o):
        return Q(self.re * o.re - self.im * o.im, self.re * o.im + self.im * o.re)

    def conj(self):
        return Q(self.re, -self.im)

    def iszero(self):
        return self.re == 0 and self.im == 0

    def __eq__(self, o):
        return self.re == o.re and self.im == o.im

    def __repr__(self):
        return f"{self.re}+{self.im}i"


ZERO, ONE = Q(0), Q(1)


# ---------- sparse matrices: dict (i, j) -> Q ----------
def mat(dense):
    return {(i, j): Q(*v) if isinstance(v, tuple) else Q(v)
            for i, row in enumerate(dense) for j, v in enumerate(row)
            if not (Q(*v) if isinstance(v, tuple) else Q(v)).iszero()}


def mul(A, B):
    rows = {}
    for (k, j), b in B.items():
        rows.setdefault(k, []).append((j, b))
    out = {}
    for (i, k), a in A.items():
        for j, b in rows.get(k, ()):
            out[(i, j)] = out.get((i, j), ZERO) + a * b
    return {k: v for k, v in out.items() if not v.iszero()}


def dag(A):
    return {(j, i): v.conj() for (i, j), v in A.items()}


def eye(n):
    return {(i, i): ONE for i in range(n)}


def kron(A, nA, B, nB):
    return {(i * nB + k, j * nB + l): a * b for (i, j), a in A.items() for (k, l), b in B.items()}


def power(A, n, t):
    R = eye(n)
    for _ in range(t):
        R = mul(A, R)
    return R


def scale(A, c):
    return {k: v * c for k, v in A.items() if not (v * c).iszero()}


def trace(A, n):
    s = ZERO
    for i in range(n):
        s = s + A.get((i, i), ZERO)
    return s


def same(A, B):
    keys = set(A) | set(B)
    return all(A.get(k, ZERO) == B.get(k, ZERO) for k in keys)


def perm_matrix(p):
    """Permutation unitary |i> -> |p(i)>."""
    return {(p[i], i): ONE for i in range(len(p))}


# ---------- the substratum ----------
def idx(v, h):
    return v * NH + h


BIJECTIONS = list(itertools.permutations(range(NV * NH)))  # phi as a tuple on idx(v,h)
UNIFORM_H = {(h, h): Q(Fr(1, NH)) for h in range(NH)}


def reduced(G, dimHA, rho_full):
    """Tr_{HA}[G rho G^dag] on C^NV."""
    M = mul(mul(G, rho_full), dag(G))
    out = {}
    for (i, j), val in M.items():
        v, r = divmod(i, dimHA)
        v2, r2 = divmod(j, dimHA)
        if r == r2:
            out[(v, v2)] = out.get((v, v2), ZERO) + val
    return {k: x for k, x in out.items() if not x.iszero()}


def unit(x, y, n):
    return {(x, y): ONE}


def channel(Ufull, dimHA, omega_HA, t):
    """Return {(x,y): Phi_t(|x><y|)} for the dynamics Ufull on C^NV (x) C^dimHA."""
    n = NV * dimHA
    G = power(Ufull, n, t)
    return {(x, y): reduced(G, dimHA, kron(unit(x, y, NV), NV, omega_HA, dimHA))
            for x in range(NV) for y in range(NV)}


def chan_same(P, R):
    return all(same(P[k], R[k]) for k in P)


def chan_scaled(P, R, c):
    return all(same(P[k], scale(R[k], c)) for k in P)


# ---------- unitaries and states for C1 / C3 ----------
def W_cases():
    cases = []
    for d in (1, 2, 3):
        for p in itertools.permutations(range(d)):
            cases.append((f"perm{d}{''.join(map(str, p))}", d, perm_matrix(p)))
    cases.append(("rot_3/5_4/5", 2, mat([[Fr(3, 5), Fr(-4, 5)], [Fr(4, 5), Fr(3, 5)]])))
    cases.append(("diag(1,i)", 2, mat([[1, 0], [0, (0, 1)]])))
    cases.append(("diag(1,-1)", 2, mat([[1, 0], [0, -1]])))
    R3 = mat([[Fr(2, 3), Fr(-2, 3), Fr(1, 3)], [Fr(2, 3), Fr(1, 3), Fr(-2, 3)], [Fr(1, 3), Fr(2, 3), Fr(2, 3)]])
    cases.append(("R3", 3, R3))
    cyc = perm_matrix((1, 2, 0))
    cases.append(("R3*cyc*R3^T", 3, mul(mul(R3, cyc), dag(R3))))
    return cases


def sigma_cases(d):
    if d == 1:
        return [("pure1", mat([[1]]))]
    if d == 2:
        return [("diag", mat([[Fr(3, 4), 0], [0, Fr(1, 4)]])),
                ("real_offdiag", mat([[Fr(1, 2), Fr(1, 4)], [Fr(1, 4), Fr(1, 2)]])),
                ("complex_offdiag", mat([[Fr(1, 2), (0, Fr(1, 4))], [(0, Fr(-1, 4)), Fr(1, 2)]]))]
    return [("diag", mat([[Fr(1, 2), 0, 0], [0, Fr(1, 3), 0], [0, 0, Fr(1, 6)]])),
            ("real_offdiag", mat([[Fr(1, 3), Fr(1, 6), 0], [Fr(1, 6), Fr(1, 3), 0], [0, 0, Fr(1, 3)]])),
            ("complex_offdiag", mat([[Fr(1, 3), (0, Fr(1, 6)), 0], [(0, Fr(-1, 6)), Fr(1, 3), 0], [0, 0, Fr(1, 3)]]))]


def charpoly(W, d):
    """Coefficients [1, -c1, c2, -c3] of det(xI - W) for d <= 3, exact."""
    g = lambda i, j: W.get((i, j), ZERO)
    if d == 1:
        return [ONE, ZERO - g(0, 0)]
    tr = trace(W, d)
    if d == 2:
        det = g(0, 0) * g(1, 1) - g(0, 1) * g(1, 0)
        return [ONE, ZERO - tr, det]
    m2 = ZERO
    for i, j in ((0, 1), (0, 2), (1, 2)):
        m2 = m2 + (g(i, i) * g(j, j) - g(i, j) * g(j, i))
    det = (g(0, 0) * (g(1, 1) * g(2, 2) - g(1, 2) * g(2, 1))
           - g(0, 1) * (g(1, 0) * g(2, 2) - g(1, 2) * g(2, 0))
           + g(0, 2) * (g(1, 0) * g(2, 1) - g(1, 1) * g(2, 0)))
    return [ONE, ZERO - tr, m2, ZERO - det]


def perm_charpolys(d):
    return {tuple((c.re, c.im) for c in charpoly(perm_matrix(p), d)) for p in itertools.permutations(range(d))}


# ---------- C1, K1, K2 (Hilbert factor) ----------
def run_C1():
    res = {"cases": 0, "equal": 0, "failures": [], "unitary_checks": {}}
    k1 = {"cases": 0, "scaled_by_2": 0, "unequal": 0}
    base = {}
    for phi in BIJECTIONS:
        U = perm_matrix(phi)
        for t in range(1, TMAX + 1):
            base[(phi, t)] = channel(U, NH, UNIFORM_H, t)
    for name, d, W in W_cases():
        res["unitary_checks"][name] = same(mul(dag(W), W), eye(d)) and same(mul(W, dag(W)), eye(d))
        for sname, sig in sigma_cases(d):
            for phi in BIJECTIONS:
                U = perm_matrix(phi)
                Ufull = kron(U, NV * NH, W, d)
                omega = kron(UNIFORM_H, NH, sig, d)
                for t in range(1, TMAX + 1):
                    res["cases"] += 1
                    if chan_same(channel(Ufull, NH * d, omega, t), base[(phi, t)]):
                        res["equal"] += 1
                    elif len(res["failures"]) < 5:
                        res["failures"].append([name, sname, list(phi), t])
        if d == 2:  # K1: unnormalized factor state, trace 2
            sig2 = scale(sigma_cases(2)[1][1], Q(2))
            for phi in BIJECTIONS:
                Ufull = kron(perm_matrix(phi), NV * NH, W, d)
                omega = kron(UNIFORM_H, NH, sig2, d)
                for t in range(1, TMAX + 1):
                    k1["cases"] += 1
                    P = channel(Ufull, NH * d, omega, t)
                    if chan_scaled(P, base[(phi, t)], Q(2)):
                        k1["scaled_by_2"] += 1
                    if not chan_same(P, base[(phi, t)]):
                        k1["unequal"] += 1
    # K2: coupled dynamics, hidden <-> factor swap after phi (factor dim 2, sigma diag(3/4,1/4))
    k2 = {"cases": 0, "changed": 0, "example": None}
    sig = sigma_cases(2)[0][1]
    for phi in BIJECTIONS:
        U = kron(perm_matrix(phi), NV * NH, eye(2), 2)
        swap = {}
        for v in range(NV):
            for h in range(NH):
                for a in range(2):
                    swap[((v * NH + a) * 2 + h, (v * NH + h) * 2 + a)] = ONE
        Ufull = mul(U, swap)
        omega = kron(UNIFORM_H, NH, sig, 2)
        for t in range(1, TMAX + 1):
            k2["cases"] += 1
            if not chan_same(channel(Ufull, NH * 2, omega, t), base[(phi, t)]):
                k2["changed"] += 1
                if k2["example"] is None:
                    k2["example"] = {"phi": list(phi), "t": t}
    return res, k1, k2, base


# ---------- K3 (Theorem 24(i) relabelling prior) ----------
def run_K3(base):
    sw = (1, 0)
    pi = tuple(idx(v, sw[h]) for v in range(NV) for h in range(NH))
    P = perm_matrix(pi)
    nonuni = mat([[Fr(2, 3), 0], [0, Fr(1, 3)]])
    out = {"cases": 0, "uniform_equal": 0, "nonuniform_changed": 0, "nonuniform_populations_changed": 0, "example": None}
    for phi in BIJECTIONS:
        U = perm_matrix(phi)
        Uc = mul(mul(P, U), dag(P))
        for t in range(1, TMAX + 1):
            out["cases"] += 1
            if chan_same(channel(Uc, NH, UNIFORM_H, t), base[(phi, t)]):
                out["uniform_equal"] += 1
            Pc, Po = channel(Uc, NH, nonuni, t), channel(U, NH, nonuni, t)
            # supplementary (not a gating control): the rooted populations <j|Phi_t(|i><i|)|j>
            if any(not Pc[(i, i)].get((j, j), ZERO) == Po[(i, i)].get((j, j), ZERO) for i in range(NV) for j in range(NV)):
                out["nonuniform_populations_changed"] += 1
            if not chan_same(Pc, Po):
                out["nonuniform_changed"] += 1
                if out["example"] is None:
                    out["example"] = {"phi": list(phi), "t": t}
    return out


# ---------- C2, K4 (classical factor; Main:336 family) ----------
def main336_family(step, hidden, prior, t):
    """Phi_t(|x><y|) = sum_hid prior(hid) [K_t(x,hid) = K_t(y,hid)] |A_t(x,hid)><A_t(y,hid)|.

    step maps (x, hid) -> (x', hid'). Also returns whether x -> F^t(x, hid) is injective for all hid.
    """
    def Ft(x, hid):
        for _ in range(t):
            x, hid = step(x, hid)
        return x, hid
    inj = True
    fam = {}
    for x in range(NV):
        for y in range(NV):
            acc = {}
            for hid in hidden:
                ax, kx = Ft(x, hid)
                ay, ky = Ft(y, hid)
                if x != y and (ax, kx) == (ay, ky):
                    inj = False
                if kx == ky:
                    acc[(ax, ay)] = acc.get((ax, ay), ZERO) + Q(prior[hid])
            fam[(x, y)] = {k: v for k, v in acc.items() if not v.iszero()}
    return fam, inj


def run_C2(base):
    res = {"maps": 0, "bijective_iff": True, "injective_hyp_all": True, "cases": 0, "equal": 0,
           "failures": [], "nonbijective_maps": 0, "minimal_example": None}
    k4 = {"cases": 0, "equal": 0}
    k2c = {"cases": 0, "changed": 0, "example": None}
    orig = {}
    for phi in BIJECTIONS:
        step0 = lambda x, h, phi=phi: divmod(phi[idx(x, h)], NH)
        for t in range(1, TMAX + 1):
            fam, _ = main336_family(step0, list(range(NH)), {h: Fr(1, NH) for h in range(NH)}, t)
            orig[(phi, t)] = fam
            k4["cases"] += 1
            if chan_same(fam, base[(phi, t)]):
                k4["equal"] += 1
    laws = {1: [[Fr(1)]], 2: [[Fr(1, 2), Fr(1, 2)], [Fr(2, 3), Fr(1, 3)]],
            3: [[Fr(1, 3)] * 3, [Fr(1, 2), Fr(1, 3), Fr(1, 6)]]}
    for na in (1, 2, 3):
        for w in itertools.product(range(na), repeat=na):
            res["maps"] += 1
            w_bij = len(set(w)) == na
            if not w_bij:
                res["nonbijective_maps"] += 1
            for phi in BIJECTIONS:
                prod = {(v, h, a): (divmod(phi[idx(v, h)], NH), w[a]) for v in range(NV) for h in range(NH) for a in range(na)}
                images = {(vh[0], vh[1], a2) for vh, a2 in prod.values()}
                if (len(images) == NV * NH * na) != w_bij:
                    res["bijective_iff"] = False
                step = lambda x, hid, phi=phi, w=w: (divmod(phi[idx(x, hid[0])], NH)[0], (divmod(phi[idx(x, hid[0])], NH)[1], w[hid[1]]))
                hidden = [(h, a) for h in range(NH) for a in range(na)]
                for alpha in laws[na]:
                    prior = {(h, a): Fr(1, NH) * alpha[a] for h, a in hidden}
                    for t in range(1, TMAX + 1):
                        fam, inj = main336_family(step, hidden, prior, t)
                        res["injective_hyp_all"] &= inj
                        res["cases"] += 1
                        if chan_same(fam, orig[(phi, t)]):
                            res["equal"] += 1
                        elif len(res["failures"]) < 5:
                            res["failures"].append([list(w), list(phi), t])
                if res["minimal_example"] is None and not w_bij and na == 2:
                    res["minimal_example"] = {"phi": list(phi), "w": list(w),
                                              "phi_x_w_bijective": len(images) == NV * NH * na}
    # K2 (classical): factor map depending on the visible coordinate: w_0 = id, w_1 = swap on |A| = 2
    for phi in BIJECTIONS:
        def step(x, hid, phi=phi):
            x2, h2 = divmod(phi[idx(x, hid[0])], NH)
            return x2, (h2, hid[1] if x == 0 else 1 - hid[1])
        hidden = [(h, a) for h in range(NH) for a in range(2)]
        prior = {(h, a): Fr(1, NH) * Fr(1, 2) for h, a in hidden}
        for t in range(1, TMAX + 1):
            fam, _ = main336_family(step, hidden, prior, t)
            k2c["cases"] += 1
            if not chan_same(fam, orig[(phi, t)]):
                k2c["changed"] += 1
                if k2c["example"] is None:
                    k2c["example"] = {"phi": list(phi), "t": t}
    return res, k4, k2c


# ---------- C3 spectral criterion ----------
def run_C3():
    out = {}
    pcs = {d: perm_charpolys(d) for d in (1, 2, 3)}
    for name, d, W in W_cases():
        cp = tuple((c.re, c.im) for c in charpoly(W, d))
        out[name] = {"dim": d, "charpoly": [f"{a}+{b}i" for a, b in cp],
                     "is_permutation_matrix": all(v == ONE for v in W.values()) and len(W) == d,
                     "similar_to_permutation": cp in pcs[d]}
    return out



# ---------- C3b rebased-datum control (NOTE.md section 14) ----------
def run_C3b():
    out = {"a_HZH_eq_2X": None, "cases": 0, "full_state_equal": 0, "rebased_state_density": True,
           "c_R3_rebase": None, "counter_cases": 0, "counter_failed": 0}
    Hp = mat([[1, 1], [1, -1]])
    Z = mat([[1, 0], [0, -1]])
    X = perm_matrix((1, 0))
    out["a_HZH_eq_2X"] = same(mul(mul(Hp, Z), Hp), scale(X, Q(2)))
    R3 = [w for n, d, w in W_cases() if n == "R3"][0]
    conj = [w for n, d, w in W_cases() if n == "R3*cyc*R3^T"][0]
    out["c_R3_rebase"] = same(mul(mul(dag(R3), conj), R3), perm_matrix((1, 2, 0)))
    dimHA = NH * 2
    n = NV * dimHA
    L = kron(eye(NV * NH), NV * NH, Hp, 2)
    for _, sig in sigma_cases(2):
        sig2 = scale(mul(mul(Hp, sig), Hp), Q(Fr(1, 2)))
        if not (trace(sig2, 2) == ONE and same(sig2, dag(sig2))):
            out["rebased_state_density"] = False
        for phi in BIJECTIONS:
            U = perm_matrix(phi)
            for t in range(1, TMAX + 1):
                GZ = power(kron(U, NV * NH, Z, 2), n, t)
                GX = power(kron(U, NV * NH, X, 2), n, t)
                GI = power(kron(U, NV * NH, eye(2), 2), n, t)
                for x in range(NV):
                    for y in range(NV):
                        rho = kron(kron(unit(x, y, NV), NV, UNIFORM_H, NH), NV * NH, sig, 2)
                        lhs = mul(mul(L, mul(mul(GZ, rho), dag(GZ))), L)
                        rr = mul(mul(L, rho), L)
                        out["cases"] += 1
                        if same(lhs, mul(mul(GX, rr), dag(GX))):
                            out["full_state_equal"] += 1
                        out["counter_cases"] += 1
                        if not same(lhs, mul(mul(GI, rr), dag(GI))):
                            out["counter_failed"] += 1
    # (c) full-state check for W = R3 C R3^T, rebased by R3 to the 3-cycle C (sigma_A of dimension 3)
    out.update({"c_cases": 0, "c_full_state_equal": 0, "c_rebased_state_density": True,
                "c_counter_cases": 0, "c_counter_failed": 0})
    C = perm_matrix((1, 2, 0))
    n3 = NV * NH * 3
    L3 = kron(eye(NV * NH), NV * NH, dag(R3), 3)
    for _, sig in sigma_cases(3):
        sigr = mul(mul(dag(R3), sig), R3)
        if not (trace(sigr, 3) == ONE and same(sigr, dag(sigr))):
            out["c_rebased_state_density"] = False
        for phi in BIJECTIONS:
            U = perm_matrix(phi)
            for t in range(1, TMAX + 1):
                GW = power(kron(U, NV * NH, conj, 3), n3, t)
                GC = power(kron(U, NV * NH, C, 3), n3, t)
                GI = power(kron(U, NV * NH, eye(3), 3), n3, t)
                for x in range(NV):
                    for y in range(NV):
                        rho = kron(kron(unit(x, y, NV), NV, UNIFORM_H, NH), NV * NH, sig, 3)
                        lhs = mul(mul(L3, mul(mul(GW, rho), dag(GW))), dag(L3))
                        rr = mul(mul(L3, rho), dag(L3))
                        out["c_cases"] += 1
                        if same(lhs, mul(mul(GC, rr), dag(GC))):
                            out["c_full_state_equal"] += 1
                        out["c_counter_cases"] += 1
                        if not same(lhs, mul(mul(GI, rr), dag(GI))):
                            out["c_counter_failed"] += 1
    return out


def main():
    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "thm24_checks.json")
    if "--out" in sys.argv:
        out_path = sys.argv[sys.argv.index("--out") + 1]
    c1, k1, k2, base = run_C1()
    k3 = run_K3(base)
    c2, k4, k2c = run_C2(base)
    c3 = run_C3()
    c3b = run_C3b()
    expected_c3 = {"rot_3/5_4/5": False, "diag(1,i)": False, "diag(1,-1)": True, "R3": False, "R3*cyc*R3^T": True}
    checks = {
        "C1_hilbert_identity_all_cases": c1["equal"] == c1["cases"] and all(c1["unitary_checks"].values()),
        "C2a_product_bijective_iff_w_bijective": c2["bijective_iff"],
        "C2b_main336_hypothesis_holds_for_every_w": c2["injective_hyp_all"],
        "C2c_main336_family_unchanged_for_every_w": c2["equal"] == c2["cases"],
        "C3_spectral_classification_as_computed": all(c3[k]["similar_to_permutation"] == v for k, v in expected_c3.items())
                                                  and all(c3[k]["similar_to_permutation"] for k in c3 if k.startswith("perm")),
        "C3b_rebased_datum_full_state": c3b["a_HZH_eq_2X"] and c3b["c_R3_rebase"] and c3b["rebased_state_density"]
                                        and c3b["full_state_equal"] == c3b["cases"]
                                        and c3b["c_rebased_state_density"] and c3b["c_full_state_equal"] == c3b["c_cases"],
        "K5_C3b_countercontrol_identity_factor_fails": c3b["counter_failed"] > 0 and c3b["c_counter_failed"] > 0,
        "K1_unnormalized_state_scales_channel_by_trace": k1["scaled_by_2"] == k1["cases"] and k1["unequal"] == k1["cases"],
        "K2_coupled_hilbert_factor_changes_channel": k2["changed"] > 0,
        "K2_visible_dependent_classical_factor_changes_family": k2c["changed"] > 0,
        "K3_uniform_relabelling_preserves_nonuniform_changes": k3["uniform_equal"] == k3["cases"] and k3["nonuniform_changed"] > 0,
        "K4_main336_family_equals_coherent_channel": k4["equal"] == k4["cases"],
    }
    controls = [k for k in checks if k.startswith("K")]
    verdict = "pass" if all(checks.values()) else ("void: control failed" if not all(checks[k] for k in controls) else "fail")
    result = {
        "script": "thm24_checks.py",
        "carrier": {"C_V": NV, "C_H": NH, "bijections": len(BIJECTIONS), "times": TMAX},
        "checks": checks,
        "verdict": verdict,
        "C1": c1, "K1": k1, "K2_hilbert": k2, "K3": k3,
        "C2": c2, "K2_classical": k2c, "K4": k4, "C3": c3, "C3b": c3b,
    }
    with open(out_path, "w") as f:
        json.dump(result, f, indent=1, sort_keys=True)
        f.write("\n")
    for k, v in checks.items():
        print(f"{'PASS' if v else 'FAIL'}  {k}")
    print("VERDICT", verdict)
    return 0 if verdict == "pass" else 1


if __name__ == "__main__":
    sys.exit(main())
