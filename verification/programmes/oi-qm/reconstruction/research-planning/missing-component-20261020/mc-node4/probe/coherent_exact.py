"""Node 4 (coherent hidden prior): symbolic exact checks (SymPy).

S1  symbolic prior on X = 3: for all 720 bijections of {0,1} x {0,1,2}, the final-configuration law is
    a polynomial in |h_x|^2 only (no cross terms h_x conj(h_y), x != y), and effects are diagonal.
S2  continuum hidden circle, controlled rotation (v, x) -> (v, x + v t mod 1), coherent prior psi:
    (a) psi = exp(2 pi i k x): Gram matrix rank one, channel = Ad diag(1, exp(-2 pi i k t)) for every t;
    (b) psi = sqrt(2) cos(2 pi x) (real, signed): coherence cos(2 pi t); rank one only at t in Z/2,
        where t = 1/2 gives Ad Z;
    (c) psi = 1 (nonnegative, the KvN uniform prior): identity for every t.
S3  the moving-boundary flow of node 3 (B2) with coherent prior psi = sqrt(f) exp(i alpha): the Gram
    matrix of the transported functions, computed from psi and the flow, carries no hidden phase; the
    channel is the mixture of I and X (the mixed-prior channel) and differs from Ad R_x(pi t).
S4  X- and Y-basis Lueders tests with the native CNOT and X give R_x(pi/2) deterministically.
S5  exact R_z(theta) for every theta with exact R_x(pi/2): R_y(theta) and the ZYZ form (products lie in
    SU(2); that every element is reached is the Euler-angle theorem, not checked here); Hadamard exact;
    R_y(theta) non-monomial off pi Z.
S6  the circle returns unentangled (catalytic phase reference).
S7  diag(1, exp(i theta)) moves the all-ones ray for theta not in 2 pi Z.
S8  native statistics of circle protocols depend on |psi|^2 = 1 only.
"""
from itertools import permutations
import sympy as sp

RES = []
def check(name, cond, info=""):
    RES.append(bool(cond))
    print(f"{'PASS' if cond else 'FAIL'}  {name}  {info}".rstrip())

def main():
    print("Node 4 coherent-prior symbolic checks (SymPy %s)" % sp.__version__)
    # ---------------- S1 ----------------
    h = sp.symbols('h0:3')
    hc = sp.symbols('hc0:3')
    m = 3
    cross_free = True
    diag_eff = True
    for p in permutations(range(2 * m)):
        # Kraus K[x'][v'][v]
        K = [[[0, 0], [0, 0]] for _ in range(m)]
        Kc = [[[0, 0], [0, 0]] for _ in range(m)]
        for v in range(2):
            for x in range(m):
                vp, xp = divmod(p[v * m + x], m)
                K[xp][vp][v] += h[x]
                Kc[xp][vp][v] += hc[x]
        for c in range(2):
            for vp in range(2):
                P = sp.expand(sum(K[xp][vp][c] * Kc[xp][vp][c] for xp in range(m)))
                for mon in sp.Poly(P, *h, *hc).monoms():
                    a, b = mon[:m], mon[m:]
                    if a != b: cross_free = False
        for xp in range(m):
            off = sp.expand(sum(Kc[xp][vp][0] * K[xp][vp][1] for vp in range(2)))
            if off != 0: diag_eff = False
    check("S1a", cross_free, "720 bijections: outcome probabilities contain only h_x conj(h_x) monomials")
    check("S1b", diag_eff, "720 bijections: every effect K^H K is diagonal")

    # ---------------- S2 ----------------
    x, t = sp.symbols('x t', real=True)
    k = sp.symbols('k', integer=True, nonzero=True)
    def gram(psi):
        # G[v1][v2] = <psi_{v2}, psi_{v1}> with psi_0 = psi, psi_1 = psi(x - t); integrals over [0,1)
        ps = [psi, psi.subs(x, x - t)]
        G = [[sp.simplify(sp.integrate(sp.expand(ps[a] * sp.conjugate(ps[b])), (x, 0, 1))) for b in range(2)] for a in range(2)]
        return sp.Matrix(G)
    psi_a = sp.exp(2 * sp.pi * sp.I * k * x)
    Ga = gram(psi_a)
    ok = sp.simplify(Ga - sp.Matrix([[1, sp.exp(2 * sp.pi * sp.I * k * t)], [sp.exp(-2 * sp.pi * sp.I * k * t), 1]])) == sp.zeros(2, 2)
    # rho -> sum_{v1 v2} rho_{v1 v2} G_{v1 v2} |v1><v2| ; Ad V with V = diag(1, e^{-2 pi i k t}) gives rho_{01} e^{+2 pi i k t}
    V = sp.diag(1, sp.exp(-2 * sp.pi * sp.I * k * t))
    r = sp.Matrix(2, 2, sp.symbols('r00 r01 r10 r11'))
    out = sp.Matrix(2, 2, lambda i, j: r[i, j] * Ga[i, j])
    adv = V * r * V.H
    check("S2a", ok and sp.simplify(out - adv) == sp.zeros(2, 2) and Ga.rank(simplify=True) == 1,
          "psi = exp(2 pi i k x): channel = Ad diag(1, exp(-2 pi i k t)) exactly, Gram rank 1, every real t")
    psi_b = sp.sqrt(2) * sp.cos(2 * sp.pi * x)
    Gb = gram(psi_b)
    okb = sp.simplify(Gb[0, 1] - sp.cos(2 * sp.pi * t)) == 0 and sp.simplify(Gb[0, 0] - 1) == 0
    Gb_half = Gb.subs(t, sp.Rational(1, 2))
    Gb_q = Gb.subs(t, sp.Rational(1, 8))
    check("S2b", okb and Gb_half == sp.Matrix([[1, -1], [-1, 1]]) and Gb_q.rank() == 2,
          "psi = sqrt2 cos: coherence factor cos(2 pi t); t = 1/2 gives Ad Z (Gram [[1,-1],[-1,1]]); t = 1/8 rank 2")
    psi_c = sp.Integer(1)
    Gc = sp.Matrix([[1, 1], [1, 1]])
    check("S2c", gram(psi_c + 0 * x) == Gc, "psi = 1 (KvN uniform): identity channel for every t")

    # ---------------- S3 ----------------
    # Flow x -> x + T mod 2 on [0, 2), v = floor(x), h = x - v, 0 < T < 1, coherent prior psi on the
    # hidden coordinate for both visible starts. The transported functions psi_{v -> v'}(h') are built
    # from the flow itself: the preimage of (v', h') is y = v' + h' - T (mod 2); its integer part, read
    # at a representative point of each region of h', fixes the source visible value and the source
    # hidden point. The Gram matrix G[(v1,v1'),(v2,v2')] = int psi_{v1->v1'} conj(psi_{v2->v2'}) dh' is
    # then integrated from psi directly.
    hh = sp.symbols('hh', real=True)
    hp = sp.symbols('hp', real=True)
    T = sp.symbols('T', positive=True)
    Fn = sp.Function('F', positive=True)
    def psi_of(z, alpha): return sp.sqrt(Fn(z)) * sp.exp(sp.I * alpha(z))
    regions = [(sp.Integer(0), T, sp.Rational(1, 6)), (T, sp.Integer(1), sp.Rational(2, 3))]  # (lo, hi, representative at T = 1/3)
    Tr = sp.Rational(1, 3)
    def transported(v, vp, alpha):
        """List over regions of the transported amplitude psi_{v->vp}(hp), or 0."""
        out = []
        for lo, hi, rep in regions:
            y_rep = vp + rep - Tr
            fl = sp.floor(y_rep)
            v_src = int(fl) % 2
            h_src = vp + hp - T - fl
            out.append(psi_of(h_src, alpha) if v_src == v else sp.Integer(0))
        return out
    fsub = lambda e: e.replace(Fn, sp.Lambda(hh, sp.pi / 2 * sp.sin(sp.pi * hh)))
    def gram(alpha):
        G = {}
        integrands_alpha_free = True
        for v1 in range(2):
            for v1p in range(2):
                for v2 in range(2):
                    for v2p in range(2):
                        A = transported(v1, v1p, alpha); B = transported(v2, v2p, alpha)
                        tot = 0
                        for r, (lo, hi, rep) in enumerate(regions):
                            ig = sp.simplify(A[r] * sp.conjugate(B[r]))
                            if ig.has(sp.exp) or ig.has(sp.I): integrands_alpha_free = False
                            tot += sp.integrate(fsub(ig), (hp, lo, hi))
                        G[(v1, v1p, v2, v2p)] = sp.simplify(tot)
        return G, integrands_alpha_free
    al1 = lambda z: 5 * z**2 + 3 * z
    al0 = lambda z: 0 * z
    G1, free1 = gram(al1)
    G0, _ = gram(al0)
    def chan_from(G, rho):
        return sp.Matrix(2, 2, lambda i, j: sp.simplify(sum(rho[v1, v2] * G[(v1, i, v2, j)] for v1 in range(2) for v2 in range(2))))
    E00 = sp.Matrix([[1, 0], [0, 0]]); E01 = sp.Matrix([[0, 1], [0, 0]])
    same = all(sp.simplify(chan_from(G1, U) - chan_from(G0, U)) == sp.zeros(2, 2) for U in (E00, E01, E01.T, sp.Matrix([[0, 0], [0, 1]])))
    check("S3a", free1 and same,
          "Gram integrands from psi carry no hidden phase (every product pairs one source point); channel with alpha = 5h^2+3h equals alpha = 0")
    c00 = chan_from(G1, E00); c01 = chan_from(G1, E01)
    R = sp.Matrix([[sp.cos(sp.pi * T / 2), -sp.I * sp.sin(sp.pi * T / 2)], [-sp.I * sp.sin(sp.pi * T / 2), sp.cos(sp.pi * T / 2)]])
    lay00 = sp.simplify(R * E00 * R.H)
    flip = sp.sin(sp.pi * T / 2)**2
    check("S3b", sp.simplify(c00[1, 1] - flip) == 0 and sp.simplify(c00[1, 1] - lay00[1, 1]) == 0
          and sp.simplify(c00[0, 0] + c00[1, 1] - 1) == 0,
          "flip probability sin^2(pi T/2) = layer-flow flip probability (rooted law reproduced); trace preserved")
    check("S3c", sp.simplify(c00[0, 1]) == 0 and sp.simplify(lay00[0, 1] - sp.I * sp.sin(sp.pi * T) / 2) == 0,
          "from |0><0| the layer flow carries coherence i sin(pi T)/2, the coherent-prior flow 0")
    mixed01 = sp.Matrix([[0, 1 - flip], [flip, 0]])
    check("S3d", sp.simplify(c01 - mixed01) == sp.zeros(2, 2)
          and sp.simplify((c01 - R * E01 * R.H).subs(T, sp.Rational(1, 2))) != sp.zeros(2, 2),
          "on |0><1| the coherent-prior channel is (1-p)|0><1| + p|1><0| (the mixture of I and X) and differs from Ad R_x(pi/2)")

    ig_bad = sp.simplify(psi_of(hp, al1) * sp.conjugate(psi_of(hp + sp.Rational(1, 4), al1)))
    check("S3e", ig_bad.has(sp.exp) or ig_bad.has(sp.I),
          "countercontrol: a product pairing two distinct source points keeps the hidden phase (the S3a test can fail)")

    # ---------------- S4 ----------------
    a0, a1 = sp.symbols('a0 a1')
    I2 = sp.eye(2); X = sp.Matrix([[0, 1], [1, 0]]); Zm = sp.diag(1, -1)
    ket0 = sp.Matrix([1, 0])
    ypl = sp.Matrix([1, sp.I]) / sp.sqrt(2); ymi = sp.Matrix([1, -sp.I]) / sp.sqrt(2)
    # Y test on |0>: outcome +i -> |+i>, outcome -i -> |-i>, then native X maps |-i> to (i)|+i>
    br_p = ypl * (ypl.H * ket0)[0]
    br_m = X * ymi * (ymi.H * ket0)[0]
    # proportionality check
    prop = sp.simplify(br_m[0] * br_p[1] - br_m[1] * br_p[0]) == 0
    anc = sp.Matrix([1, sp.I]) / sp.sqrt(2)
    data = sp.Matrix([a0, a1])
    # joint order (data, ancilla): CNOT with ancilla as control, data as target
    def kron(A, B): return sp.kronecker_product(A, B)
    P0 = sp.diag(1, 0); P1 = sp.diag(0, 1)
    CN = kron(I2, P0) + kron(X, P1)
    st = CN * kron(data, anc)
    w = sp.Matrix([1, -1]) / sp.sqrt(2); wp = sp.Matrix([1, 1]) / sp.sqrt(2)   # X-basis outcomes
    bw = kron(I2, w.H) * st
    bwp = X * (kron(I2, wp.H) * st)
    Rx = (sp.cos(sp.pi / 4) * I2 - sp.I * sp.sin(sp.pi / 4) * X)
    target = Rx * data
    def propto(u, v):
        return all(sp.simplify(u[i] * v[j] - u[j] * v[i]) == 0 for i in range(2) for j in range(2))
    check("S4", prop and propto(bw, target) and propto(bwp, target)
          and sp.simplify((bw.H * bw)[0] + (bwp.H * bwp)[0] - (data.H * data)[0]) == 0,
          "Y-test prep of |+i>, CNOT, X-basis test, X on one outcome: both branches prop. to R_x(pi/2), total weight 1")

    # ---------------- S5 ----------------
    th, al, be, ga = sp.symbols('theta alpha beta gamma', real=True)
    def Rz(a): return sp.diag(sp.exp(-sp.I * a / 2), sp.exp(sp.I * a / 2))
    def Rxm(a): return sp.Matrix([[sp.cos(a / 2), -sp.I * sp.sin(a / 2)], [-sp.I * sp.sin(a / 2), sp.cos(a / 2)]])
    def Ry(a): return sp.Matrix([[sp.cos(a / 2), -sp.sin(a / 2)], [sp.sin(a / 2), sp.cos(a / 2)]])
    lhs = sp.simplify(Rxm(sp.pi / 2) * Rz(th) * Rxm(-sp.pi / 2))
    rhs = Ry(-th)
    okY = sp.simplify(lhs - rhs) == sp.zeros(2, 2)
    Hd = sp.Matrix([[1, 1], [1, -1]]) / sp.sqrt(2)
    Hp = sp.simplify(Rz(sp.pi / 2) * Rxm(sp.pi / 2) * Rz(sp.pi / 2))
    okH = all(sp.simplify(Hp[i, j] * Hd[0, 0] - Hd[i, j] * Hp[0, 0]) == 0 for i in range(2) for j in range(2))
    U = sp.simplify(Rz(al) * Ry(be) * Rz(ga))
    # generic SU(2) element [[A, -conj B],[B, conj A]] with |A|^2+|B|^2 = 1: check the form
    okU = sp.simplify(U[1, 1] - sp.conjugate(U[0, 0])) == 0 and sp.simplify(U[0, 1] + sp.conjugate(U[1, 0])) == 0 \
        and sp.simplify(sp.Abs(U[0, 0])**2 + sp.Abs(U[1, 0])**2 - 1) == 0
    nm = Ry(sp.pi / 3)
    check("S5", okY and okH and okU and all(nm[i, j] != 0 for i in range(2) for j in range(2)),
          "R_x(pi/2) R_z(theta) R_x(-pi/2) = R_y(-theta); H prop. to R_z R_x R_z (pi/2); ZYZ products lie in SU(2); R_y(pi/3) non-monomial")

    # ---------------- S6, S7, S8 ----------------
    shift = sp.simplify(psi_a.subs(x, x - t) - sp.exp(-2 * sp.pi * sp.I * k * t) * psi_a)
    check("S6", shift == 0, "psi(x - t) = exp(-2 pi i k t) psi(x): the circle returns in a product state")
    one = sp.Matrix([1, 1])
    Vt = sp.diag(1, sp.exp(sp.I * th))
    mv = sp.simplify((Vt * one)[1] - (Vt * one)[0])
    check("S7", sp.simplify(mv - (sp.exp(sp.I * th) - 1)) == 0 and mv.subs(th, sp.pi / 3) != 0,
          "diag(1, e^{i theta}) moves the all-ones ray unless e^{i theta} = 1")
    check("S8", sp.simplify(psi_a * sp.conjugate(psi_a)) == 1,
          "|psi|^2 = 1: native statistics of circle protocols are those of the uniform prior")

    print(f"SUMMARY {sum(RES)} PASS, {len(RES) - sum(RES)} FAIL")

if __name__ == "__main__":
    main()
