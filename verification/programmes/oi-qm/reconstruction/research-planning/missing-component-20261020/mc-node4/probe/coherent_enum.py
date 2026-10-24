"""Node 4 (coherent hidden prior): exhaustive exact enumeration, pure Python, Gaussian rationals.

Model: visible bit v in {0,1}, hidden x in {0..m-1}, joint index v*m+x. A process is a bijection p of
the joint carrier (kappa2), acting on descriptions by its permutation operator (kappa3). The hidden
sector starts in a fixed coherent vector h (kappa1 dropped: a vector, not a mixture). Readouts are
visible configuration readouts with feed-forward (kappa4). Amplitudes are unnormalized Gaussian
integers/rationals; every quadratic quantity is divided by |h|^2.

Blocks
  E1  Kraus form: every Kraus operator K_{x'} = (I x <x'|) U (I x |h>) is row-monomial and each nonzero
      entry is a single amplitude h_x (tag check, all bijections at m = 3 and m = 4).
  E2  effects sum_{x'} K^H K are diagonal, for every bijection and every test prior.
  E3  native statistics: for every bijection, start and prior, the law of the final visible
      configuration equals the law under the mixed prior mu_x = |h_x|^2.
  E4  unitary channels: whenever all Kraus operators are proportional to one V (Choi rank one), V is
      monomial; the distinct V found are classified per prior form.
  E5  ones identity: sum_{x'} K_{x'}^H 1 = conj(sum_x h_x) 1 for every bijection.
  E6  nonnegative priors: every channel preserves entrywise nonnegativity and reality; signed priors
      keep reality only; complex priors keep neither.
  E7  purification: (a) an untouched purifier reproduces the mixed-prior channel exactly; (b) a
      purifier acted on, nonnegative amplitudes: nonnegativity kept, unitary channels ones-fixing;
      (c) a purifier sign changes the channel for some bijection.
  E8  two-step protocols with a visible readout and feed-forward: row-monomial single-amplitude
      Kraus, statistics equal to the mixed prior, rank-one coarse channels monomial.
  E9  countercontrols: a Hadamard step (kappa2 dropped) or an X-basis test (kappa4 dropped) makes the
      checks fail and the coherent prior statistically visible.
"""
from fractions import Fraction as Fr
from itertools import permutations

# ---------- Gaussian rationals as (re, im) ----------
Z0 = (Fr(0), Fr(0))
def g(a, b=0): return (Fr(a), Fr(b))
def add(a, b): return (a[0] + b[0], a[1] + b[1])
def mul(a, b): return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])
def conj(a): return (a[0], -a[1])
def isz(a): return a[0] == 0 and a[1] == 0
def nrm2(a): return a[0] * a[0] + a[1] * a[1]

RESULTS = []
def check(name, cond, info=""):
    RESULTS.append((name, bool(cond)))
    print(f"{'PASS' if cond else 'FAIL'}  {name}  {info}".rstrip())

# ---------- core constructions ----------
def kraus(p, m, h, nv=2):
    """K[x'][v'][v] = sum_x h_x [p(v,x) = (v',x')]."""
    K = [[[Z0 for _ in range(nv)] for _ in range(nv)] for _ in range(m)]
    for v in range(nv):
        for x in range(m):
            j = p[v * m + x]
            vp, xp = divmod(j, m)
            K[xp][vp][v] = add(K[xp][vp][v], h[x])
    return K

def kraus_tags(p, m, nv=2):
    T = [[[set() for _ in range(nv)] for _ in range(nv)] for _ in range(m)]
    for v in range(nv):
        for x in range(m):
            vp, xp = divmod(p[v * m + x], m)
            T[xp][vp][v].add(x)
    return T

def row_monomial_tags(T):
    for Kx in T:
        for row in Kx:
            if sum(1 for s in row if s) > 1: return False
            if any(len(s) > 1 for s in row): return False
    return True

def matmul(A, B):
    n, k, l = len(A), len(B), len(B[0])
    return [[ (lambda i, j: _sum([mul(A[i][t], B[t][j]) for t in range(k)]))(i, j) for j in range(l)] for i in range(n)]
def _sum(xs):
    s = Z0
    for x in xs: s = add(s, x)
    return s
def dag(A): return [[conj(A[j][i]) for j in range(len(A))] for i in range(len(A[0]))]

def effect(K):
    nv = len(K[0])
    E = [[Z0] * nv for _ in range(nv)]
    for Kx in K:
        M = matmul(dag(Kx), Kx)
        E = [[add(E[i][j], M[i][j]) for j in range(nv)] for i in range(nv)]
    return E

def prob_coherent(K, c, vp, h):
    n2 = sum(nrm2(a) for a in h)
    return sum(nrm2(Kx[vp][c]) for Kx in K) / n2

def prob_mixed(p, m, c, vp, h):
    n2 = sum(nrm2(a) for a in h)
    s = Fr(0)
    for x in range(m):
        if p[c * m + x] // m == vp: s += nrm2(h[x])
    return s / n2

def proportional_all(mats):
    """Return a nonzero representative V if every nonzero matrix is proportional to it, else None."""
    flat = [[e for row in M for e in row] for M in mats]
    nz = [f for f in flat if any(not isz(e) for e in f)]
    if not nz: return None
    ref = nz[0]
    for f in nz[1:]:
        for i in range(len(ref)):
            for j in range(len(ref)):
                if mul(ref[i], f[j]) != mul(ref[j], f[i]): return None
    nv = len(mats[0])
    return [ref[i * nv:(i + 1) * nv] for i in range(nv)]

def is_monomial(V):
    n = len(V)
    rows = [sum(1 for e in r if not isz(e)) for r in V]
    cols = [sum(1 for i in range(n) if not isz(V[i][j])) for j in range(n)]
    return all(r == 1 for r in rows) and all(c == 1 for c in cols)

def normalize(V):
    """Scale V so that its first nonzero entry (row-major) is 1; return a hashable key."""
    flat = [e for r in V for e in r]
    piv = next(e for e in flat if not isz(e))
    n2 = nrm2(piv)
    inv = (piv[0] / n2, -piv[1] / n2)
    return tuple(mul(e, inv) for e in flat)

def ones_fixing(V):
    s = [_sum(r) for r in V]
    return all(mul(s[0], g(1)) == s[i] for i in range(len(s)))  # V 1 proportional to 1

def channel(K, h, rho):
    n2 = sum(nrm2(a) for a in h)
    nv = len(rho)
    out = [[Z0] * nv for _ in range(nv)]
    for Kx in K:
        M = matmul(matmul(Kx, rho), dag(Kx))
        out = [[add(out[i][j], M[i][j]) for j in range(nv)] for i in range(nv)]
    return [[(e[0] / n2, e[1] / n2) for e in r] for r in out]

UNITS = [[[g(1 if (i, j) == (a, b) else 0) for j in range(2)] for i in range(2)] for a in range(2) for b in range(2)]

def classify(key):
    vals = [e for e in key if not isz(e)]
    if all(e == g(1) for e in vals): return "perm"
    if all(e[1] == 0 for e in vals): return "signed"
    return "complex"

# ---------- priors (unnormalized) ----------
PRI4 = {
    "N-uniform":   [g(1), g(1), g(1), g(1)],
    "N-nonunif":   [g(3), g(4), g(0), g(0)],
    "R-sum0":      [g(1), g(-1), g(1), g(-1)],
    "R-sum2":      [g(1), g(1), g(1), g(-1)],
    "C-fourier1":  [g(1), g(0, 1), g(-1), g(0, -1)],
    "C-sum1+i":    [g(1), g(0, 1), g(1), g(0, 1)],
}

def main():
    print("Node 4 coherent-prior enumeration (exact, Gaussian rationals)")
    # E1 tags, m = 3 and m = 4, all bijections
    for m in (3, 4):
        perms = list(permutations(range(2 * m)))
        ok = all(row_monomial_tags(kraus_tags(p, m)) for p in perms)
        check(f"E1.m{m}", ok, f"all {len(perms)} bijections: Kraus row-monomial, single-amplitude entries")
    perms4 = list(permutations(range(8)))
    # E2-E6 over all 40320 bijections at m = 4 for every prior
    for name, h in PRI4.items():
        diag_ok = stat_ok = ones_ok = True
        nonneg_ok = real_ok = True
        uni = {}
        sh = _sum(h)
        for p in perms4:
            K = kraus(p, 4, h)
            E = effect(K)
            if not (isz(E[0][1]) and isz(E[1][0])): diag_ok = False
            for c in range(2):
                for vp in range(2):
                    if prob_coherent(K, c, vp, h) != prob_mixed(p, 4, c, vp, h): stat_ok = False
            S = [Z0, Z0]
            for Kx in K:
                for v in range(2):
                    S[v] = add(S[v], _sum([conj(Kx[vp][v]) for vp in range(2)]))
            if not (S[0] == conj(sh) and S[1] == conj(sh)): ones_ok = False
            if name[0] in "NR":
                for U in UNITS:
                    out = channel(K, h, U)
                    for r in out:
                        for e in r:
                            if e[1] != 0: real_ok = False
                            if name[0] == "N" and e[0] < 0: nonneg_ok = False
            V = proportional_all(K)
            if V is not None and all(not isz(V[i][i]) or not isz(V[i][1 - i]) for i in range(2)):
                key = normalize(V)
                uni[key] = (is_monomial(V), ones_fixing(V))
        check(f"E2.{name}", diag_ok, "effects diagonal, 40320 bijections")
        check(f"E3.{name}", stat_ok, "final-configuration law = mixed prior |h|^2, both starts")
        check(f"E5.{name}", ones_ok, "sum_x' K^H 1 = conj(sum h) 1")
        mono = all(v[0] for v in uni.values())
        kinds = sorted({classify(k) for k in uni})
        rayfix = all(v[1] for v in uni.values())
        check(f"E4.{name}", mono, f"{len(uni)} distinct rank-one V, all monomial; kinds {kinds}; all ones-fixing: {rayfix}")
        ratios = set()
        for x in h:
            for y in h:
                if not isz(y):
                    n2y = nrm2(y)
                    ratios.add(mul(x, (y[0] / n2y, -y[1] / n2y)))
        check(f"E4r.{name}", all(e in ratios for k in uni for e in k if not isz(e)),
              "every entry of a normalized rank-one V is a ratio h_x/h_y of prior coordinates")
        if sh != Z0:
            check(f"E4b.{name}", rayfix, "sum h != 0: every unitary channel fixes the all-ones ray")
        if name[0] == "N":
            check(f"E6.{name}", nonneg_ok and real_ok and kinds == ["perm"],
                  "nonnegative prior: nonnegativity and reality preserved; unitary channels are permutations")
        if name[0] == "R":
            check(f"E6.{name}", real_ok and set(kinds) <= {"perm", "signed"},
                  f"signed prior: reality preserved; unitary kinds {kinds}")
    # E6 sign break witness: R-sum0 contains Z = diag(1,-1)
    Zkey = (g(1), Z0, Z0, g(-1))
    Skey = (g(1), Z0, Z0, g(0, 1))
    found = {}
    for name in ("R-sum0", "C-fourier1", "N-uniform", "R-sum2", "C-sum1+i"):
        h = PRI4[name]
        ks = set()
        for p in perms4:
            V = proportional_all(kraus(p, 4, h))
            if V is not None and is_monomial(V): ks.add(normalize(V))
        found[name] = ks
    check("E6.Z-signed", Zkey in found["R-sum0"] and Skey not in found["R-sum0"], "signed sum-0 prior gives Z, never S")
    check("E6.S-complex", Skey in found["C-fourier1"], "Fourier prior on a 4-cycle gives S = diag(1,i)")
    check("E6.none-moving-if-sum!=0", Zkey not in found["R-sum2"] and Skey not in found["C-sum1+i"] and Zkey not in found["N-uniform"],
          "priors with sum h != 0 give neither Z nor S")
    # nonnegativity broken by a signed prior: witness
    h = PRI4["R-sum0"]
    wit = None
    for p in perms4:
        K = kraus(p, 4, h)
        for U in UNITS:
            out = channel(K, h, U)
            if any(e[0] < 0 for r in out for e in r): wit = p; break
        if wit: break
    check("E6.signed-breaks-nonneg", wit is not None, f"witness bijection {wit}")

    # E7 purification: X = 2, R = 2, prior a|00> + b|11>
    def joint_kraus(p, nh, hj):
        return kraus(p, nh, hj)
    a, b = g(3), g(4)
    # (a) untouched purifier: bijection acts on C x X only; trace over X and R
    perms_cx = list(permutations(range(4)))
    ok_a = True
    for q in perms_cx:
        # lift q to C x X x R with R untouched: index (v, x, r) -> v*4 + x*2 + r
        p = [0] * 8
        for v in range(2):
            for x in range(2):
                vq, xq = divmod(q[v * 2 + x], 2)
                for r in range(2):
                    p[v * 4 + x * 2 + r] = vq * 4 + xq * 2 + r
        hj = [a, Z0, Z0, b]          # hidden index x*2 + r over X x R
        Kp = kraus(p, 4, hj)
        Km = [kraus(q, 2, [g(1), Z0]), kraus(q, 2, [Z0, g(1)])]   # point priors
        for U in UNITS:
            out_p = channel(Kp, hj, U)
            o0 = channel(Km[0], [g(1), Z0], U)
            o1 = channel(Km[1], [Z0, g(1)], U)
            w0, w1 = Fr(9, 25), Fr(16, 25)
            mix = [[(w0 * o0[i][j][0] + w1 * o1[i][j][0], w0 * o0[i][j][1] + w1 * o1[i][j][1]) for j in range(2)] for i in range(2)]
            if out_p != mix: ok_a = False
    check("E7a", ok_a, "untouched purifier: channel = mixed prior (9/25, 16/25) channel, all 24 bijections, matrix units")
    # (b) purifier acted on: all 8! bijections of C x X x R
    hj = [a, Z0, Z0, b]
    ok_nn = True; ok_fix = True; nuni = 0
    for p in perms4:
        K = kraus(p, 4, hj)
        for U in UNITS:
            out = channel(K, hj, U)
            if any(e[0] < 0 or e[1] != 0 for r in out for e in r): ok_nn = False
        V = proportional_all(K)
        if V is not None and is_monomial(V):
            nuni += 1
            if not ones_fixing(V): ok_fix = False
    check("E7b", ok_nn and ok_fix, f"purifier acted on, amplitudes (3,4): nonnegativity kept; {nuni} rank-one cases, all ones-fixing")
    # (c) purifier sign: a|00> - b|11> versus a|00> + b|11>
    hm = [a, Z0, Z0, g(-4)]
    diff = 0
    for p in perms4:
        Kp, Km_ = kraus(p, 4, hj), kraus(p, 4, hm)
        if any(channel(Kp, hj, U) != channel(Km_, hm, U) for U in UNITS): diff += 1
    check("E7c", diff > 0, f"purifier sign changes the visible channel for {diff} of 40320 bijections")

    # E8 two-step protocols, m = 4, priors R-sum0 and C-fourier1
    sub1 = perms4[::401]
    sub2 = perms4[::4001]
    for name in ("R-sum0", "C-fourier1"):
        h = PRI4[name]
        ok_tag = ok_stat = ok_mono = True
        nprot = nrank1 = 0
        for p1 in sub1:
            for p20 in sub2:
                for p21 in sub2:
                    nprot += 1
                    # joint path: start (c,x) -> p1 -> readout a = visible -> p2_a -> final (v',x')
                    # Kraus K[(a,x')][v'][c] = sum_x h_x [path]
                    K = {}
                    T = {}
                    for c in range(2):
                        for x in range(4):
                            j1 = p1[c * 4 + x]
                            aa = j1 // 4
                            j2 = (p20 if aa == 0 else p21)[j1]
                            vp, xp = divmod(j2, 4)
                            K.setdefault((aa, xp), [[Z0, Z0], [Z0, Z0]])
                            T.setdefault((aa, xp), [[set(), set()], [set(), set()]])
                            K[(aa, xp)][vp][c] = add(K[(aa, xp)][vp][c], h[x])
                            T[(aa, xp)][vp][c].add(x)
                    if not row_monomial_tags(list(T.values())): ok_tag = False
                    n2 = sum(nrm2(e) for e in h)
                    for c in range(2):
                        for aa in range(2):
                            for vp in range(2):
                                pc = sum(nrm2(K[k][vp][c]) for k in K if k[0] == aa) / n2
                                pm = Fr(0)
                                for x in range(4):
                                    j1 = p1[c * 4 + x]
                                    if j1 // 4 != aa: continue
                                    j2 = (p20 if aa == 0 else p21)[j1]
                                    if j2 // 4 == vp: pm += nrm2(h[x])
                                if pc != pm / n2: ok_stat = False
                    V = proportional_all(list(K.values()))
                    if V is not None and all(any(not isz(e) for e in r) for r in V):
                        nrank1 += 1
                        if not is_monomial(V): ok_mono = False
        check(f"E8.{name}", ok_tag and ok_stat and ok_mono,
              f"{nprot} two-step protocols: single-amplitude row-monomial Kraus, mixed-prior statistics, {nrank1} rank-one coarse channels all monomial")


    # E9 countercontrols: dropping kappa2 or kappa4 makes the coherence visible
    # (a) m = 2, prior (1, -1): swap hidden into visible, then visible Hadamard (unnormalized
    #     [[1,1],[1,-1]], weight 1/2), then readout. Coherent: P(v' = 1) = 1; mixed: 1/2.
    hneg = [g(1), g(-1)]
    swap = [0, 2, 1, 3]                      # (v,x) -> (x,v) on index v*2+x
    Kc = kraus(swap, 2, hneg)
    Hm = [[g(1), g(1)], [g(1), g(-1)]]
    KH = [matmul(Hm, Kx) for Kx in Kc]
    n2 = Fr(2)
    p1_coh = sum(nrm2(Kx[1][0]) for Kx in KH) / n2 / 2
    p1_mix = Fr(0)
    for x, w in ((0, Fr(1, 2)), (1, Fr(1, 2))):
        Kp = kraus(swap, 2, [g(1) if y == x else Z0 for y in range(2)])
        p1_mix += w * sum(nrm2(matmul(Hm, Kx)[1][0]) for Kx in Kp) / 2
    check("E9a", p1_coh == 1 and p1_mix == Fr(1, 2), f"Hadamard after swap-in: coherent P(1) = {p1_coh}, mixed P(1) = {p1_mix}")
    # (b) the row-monomial tag check fails once a Hadamard step is interposed
    #     (a Hadamard after the swap acts on a single column and leaves rows single-entry; the
    #     Hadamard is placed before the bijection, where it mixes two input columns)
    KHb = [matmul(Kx, Hm) for Kx in Kc]
    rows_bad = any(sum(1 for e in r if not isz(e)) > 1 for Kx in KHb for r in Kx)
    check("E9b", rows_bad, "with a Hadamard step before the bijection the Kraus operators are not row-monomial (check can fail)")
    # (c) an X-basis test projector gives a non-diagonal effect
    Px = [[g(1), g(1)], [g(1), g(1)]]
    Eff = matmul(dag(Px), Px)
    check("E9c", not isz(Eff[0][1]), "X-basis test effect is non-diagonal (diagonal-effect check can fail)")

    npass = sum(1 for _, c in RESULTS if c)
    print(f"SUMMARY {npass} PASS, {len(RESULTS) - npass} FAIL")

if __name__ == "__main__":
    main()
