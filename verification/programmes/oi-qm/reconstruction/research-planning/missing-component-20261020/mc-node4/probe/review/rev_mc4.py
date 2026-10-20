"""Independent review checks for node 4 (coherent hidden prior). Exact Fractions; imports nothing
from the author's probe except where a mutation test needs the author's own checker (marked)."""
import sys, random
from fractions import Fraction as Fr
from itertools import permutations

RES = []
def check(name, cond, info=""):
    RES.append(bool(cond)); print(f"{'PASS' if cond else 'FAIL'}  {name}  {info}".rstrip())

# complex numbers as (re, im) Fractions
Z = (Fr(0), Fr(0))
def c(a, b=0): return (Fr(a), Fr(b))
def ad(a, b): return (a[0]+b[0], a[1]+b[1])
def ml(a, b): return (a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0])
def cj(a): return (a[0], -a[1])
def nz(a): return a[0] != 0 or a[1] != 0

def mat(n, m): return [[Z]*m for _ in range(n)]
def mm(A, B):
    n, k, l = len(A), len(B), len(B[0]); R = mat(n, l)
    for i in range(n):
        for t in range(k):
            if nz(A[i][t]):
                for j in range(l): R[i][j] = ad(R[i][j], ml(A[i][t], B[t][j]))
    return R
def dg(A): return [[cj(A[j][i]) for j in range(len(A))] for i in range(len(A[0]))]

def kraus_indep(p, nv, m, h):
    """Independent path: joint permutation matrix U on C x X, Kraus K_x' = (I x <x'|) U (I x |h>)."""
    N = nv * m
    U = mat(N, N)
    for j in range(N): U[p[j]][j] = c(1)
    Ks = []
    for xp in range(m):
        K = mat(nv, nv)
        for vp in range(nv):
            for v in range(nv):
                s = Z
                for x in range(m): s = ad(s, ml(U[vp*m+xp][v*m+x], h[x]))
                K[vp][v] = s
        Ks.append(K)
    return Ks

def channel_joint(p, nv, m, h, rho):
    """Fully independent: Ad_U on rho (x) |h><h|, then partial trace over X (no Kraus at all)."""
    N = nv*m
    J = mat(N, N)
    for v1 in range(nv):
        for x1 in range(m):
            for v2 in range(nv):
                for x2 in range(m):
                    J[v1*m+x1][v2*m+x2] = ml(rho[v1][v2], ml(h[x1], cj(h[x2])))
    J2 = mat(N, N)
    for a in range(N):
        for b in range(N): J2[p[a]][p[b]] = J[a][b]
    out = mat(nv, nv)
    n2 = sum(e[0]*e[0]+e[1]*e[1] for e in h)
    for v1 in range(nv):
        for v2 in range(nv):
            s = Z
            for x in range(m): s = ad(s, J2[v1*m+x][v2*m+x])
            out[v1][v2] = (s[0]/n2, s[1]/n2)
    return out

def channel_K(Ks, h, rho):
    n2 = sum(e[0]*e[0]+e[1]*e[1] for e in h); nv = len(rho); out = mat(nv, nv)
    for K in Ks:
        M = mm(mm(K, rho), dg(K))
        for i in range(nv):
            for j in range(nv): out[i][j] = ad(out[i][j], M[i][j])
    return [[(e[0]/n2, e[1]/n2) for e in r] for r in out]

def units(n): return [[[c(1 if (i, j) == (a, b) else 0) for j in range(n)] for i in range(n)] for a in range(n) for b in range(n)]

def rank1_rep(Ks):
    flat = [[e for r in K for e in r] for K in Ks]
    nzs = [f for f in flat if any(nz(e) for e in f)]
    if not nzs: return None
    r = nzs[0]
    for f in nzs[1:]:
        for i in range(len(r)):
            for j in range(len(r)):
                if ml(r[i], f[j]) != ml(r[j], f[i]): return None
    n = len(Ks[0]); return [r[i*n:(i+1)*n] for i in range(n)]

def normalized(V):
    fl = [e for r in V for e in r]; pv = next(e for e in fl if nz(e)); n2 = pv[0]**2+pv[1]**2
    inv = (pv[0]/n2, -pv[1]/n2); return [ml(e, inv) for e in fl]

def main():
    random.seed(20261020)
    # R1: independent Ad_U + partial trace path agrees with the Kraus channel (author's E-blocks never
    #     build the joint operator); m = 3 exhaustive, signed and complex priors, all matrix units.
    for name, h in (("R", [c(1), c(-1), c(2)]), ("C", [c(1), c(0, 1), c(-1, 1)])):
        ok = True
        for p in permutations(range(6)):
            Ks = kraus_indep(p, 2, 3, h)
            for U in units(2):
                if channel_K(Ks, h, U) != channel_joint(p, 2, 3, h, U): ok = False
        check(f"R1.{name}", ok, "720 bijections: Ad_U then partial trace = Kraus channel (independent code path)")

    # R2: sufficiency counterexample. Sum h = 0 but no nontrivial unimodular ratio h_x/h_y:
    #     no available unitary channel moves the all-ones ray (single step, exhaustive).
    for name, h, m in (("(2,-1,-1)", [c(2), c(-1), c(-1)], 3), ("(3,-1,-2)", [c(3), c(-1), c(-2)], 3),
                       ("(3,-1,-1,-1)", [c(3), c(-1), c(-1), c(-1)], 4)):
        assert sum(e[0] for e in h) == 0
        nr1 = 0; moving = 0; kinds = set()
        for p in permutations(range(2*m)):
            V = rank1_rep(kraus_indep(p, 2, m, h))
            if V is None: continue
            if not all(any(nz(e) for e in r) for r in V): continue
            nr1 += 1
            nv = normalized(V); kinds.add(tuple(nv))
            s0 = ad(V[0][0], V[0][1]); s1 = ad(V[1][0], V[1][1])
            if s0 != s1: moving += 1
        perm_only = all(all(e in (c(0), c(1)) for e in k) for k in kinds)
        check(f"R2.{name}", moving == 0 and perm_only and nr1 > 0,
              f"sum h = 0; {nr1} rank-one channels, normalized V all 0/1 permutations, ray-moving: {moving}")

    # R2b: control for R2 (must find a ray-moving channel): the author's R-sum0 eigenvector prior, m = 4
    h = [c(1), c(-1), c(1), c(-1)]; found = False
    for p in permutations(range(8)):
        V = rank1_rep(kraus_indep(p, 2, 4, h))
        if V is None or not all(any(nz(e) for e in r) for r in V): continue
        if ad(V[0][0], V[0][1]) != ad(V[1][0], V[1][1]): found = True; break
    check("R2b.control", found, "eigenvector prior (1,-1,1,-1): a ray-moving unitary channel is found by the same code")

    # R3: OnesNormal span test for the counterexample prior: is 1 in span{K_x'^H 1} for every bijection?
    h = [c(2), c(-1), c(-1)]; bad = 0
    for p in permutations(range(6)):
        Ks = kraus_indep(p, 2, 3, h)
        vecs = [[ad(cj(K[0][v]), cj(K[1][v])) for v in range(2)] for K in Ks]
        vecs = [w for w in vecs if any(nz(e) for e in w)]
        # 2-dim: 1 in span iff some w not prop. to w0, or w0 prop. to 1
        full = any(ml(vecs[0][0], w[1]) != ml(vecs[0][1], w[0]) for w in vecs[1:])
        ray1 = vecs[0][0] == vecs[0][1]
        if not (full or ray1): bad += 1
    check("R3.info", True, f"h = (2,-1,-1): bijections whose single-outcome family has 1 outside span{{K^H 1}}: {bad} of 720")

    # R4: statistical equivalence with a visible ancilla (not exercised by the author): token + ancilla
    #     bit (|C| = 4), ancilla attached in |0> or uniformly mixed, two-step protocol with readout of
    #     the ancilla and feed-forward, sampled bijections on C x X, m = 3, complex prior.
    h = [c(1), c(0, 1), c(-1, 1)]; m = 3; N = 4*m
    n2 = sum(e[0]**2+e[1]**2 for e in h)
    ok = True; nprot = 0
    for _ in range(400):
        p1 = list(range(N)); random.shuffle(p1)
        q0 = list(range(N)); random.shuffle(q0)
        q1 = list(range(N)); random.shuffle(q1)
        for tok in range(2):
            for anc_mode in ("pure0", "mixed"):
                nprot += 1
                starts = [(tok*2+0, Fr(1))] if anc_mode == "pure0" else [(tok*2+0, Fr(1, 2)), (tok*2+1, Fr(1, 2))]
                # coherent: amplitude vector on C x X for each start, evolve, read ancilla, feed forward, read all
                law_c = {}; law_m = {}
                for (c0, w) in starts:
                    amp = {}
                    for x in range(m): amp[c0*m+x] = h[x]
                    a1 = {p1[j]: a for j, a in amp.items()}
                    a2 = {}
                    for j, a in a1.items():
                        anc = (j // m) % 2
                        k = (q0 if anc == 0 else q1)[j]
                        key = (anc, k // m)
                        a2.setdefault(key, {}); a2[key][k] = ad(a2[key].get(k, Z), a)  # amplitudes would add here
                    for key, d in a2.items():
                        pr = sum(e[0]**2+e[1]**2 for e in d.values()) / n2
                        law_c[key] = law_c.get(key, 0) + w*pr
                    for x in range(m):
                        j = p1[c0*m+x]; anc = (j // m) % 2; k = (q0 if anc == 0 else q1)[j]
                        key = (anc, k // m)
                        law_m[key] = law_m.get(key, 0) + w*(h[x][0]**2+h[x][1]**2)/n2
                if {k: v for k, v in law_c.items() if v} != {k: v for k, v in law_m.items() if v}: ok = False
    check("R4", ok, f"{nprot} two-step protocols with a visible ancilla (pure or uniformly mixed attach): coherent law = mixed law")

    # R5: mutation tests of the author's own checkers (imports the author's probe from its directory).
    sys.path.insert(0, sys.argv[1])
    import coherent_enum as ce
    # row_monomial_tags on a non-injective map must fail
    T = ce.kraus_tags([0, 1, 2, 0, 4, 5], 3)  # (1,0) collides with (0,0)
    check("R5a", not ce.row_monomial_tags(T), "author's row_monomial_tags returns False on a non-injective map")
    # E3 comparison must fail when two amplitudes land in one entry (non-injective map, same start)
    hh = [ce.g(1), ce.g(-1), ce.g(2)]; pbad = [0, 0, 2, 3, 4, 5]
    Kb = ce.kraus(pbad, 3, hh)
    pc = ce.prob_coherent(Kb, 0, 0, hh); pm = ce.prob_mixed(pbad, 3, 0, 0, hh)
    check("R5b", pc != pm, f"author's E3 comparison detects added amplitudes: coherent {pc} vs mixed {pm}")
    # E2 effect check on an X-test Kraus pair through the author's own effect()
    Px = [[(Fr(1, 2), Fr(0)), (Fr(1, 2), Fr(0))], [(Fr(1, 2), Fr(0)), (Fr(1, 2), Fr(0))]]
    E = ce.effect([Px])
    check("R5c", ce.isz(E[0][1]) is False, "author's effect() reports a non-diagonal effect for an X-basis projector")

    print(f"SUMMARY {sum(RES)} PASS, {len(RES)-sum(RES)} FAIL")

if __name__ == "__main__":
    main()
