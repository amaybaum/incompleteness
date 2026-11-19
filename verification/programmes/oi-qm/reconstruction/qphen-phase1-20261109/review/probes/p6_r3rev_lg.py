"""p6_r3rev_lg -- independent r3 reviewer probe for QX-4 (no p1-p5 imports). Exact (sympy / Fractions).

(1) Two-mode Clifford counterexamples of A4.1(c), both tensor conventions for 'I (x) H', Lueders reads of Z_c.
(2) Measure-and-reprepare instruments: K3 = 3 (w=1), K3 = 6w-3 (exact, symbolic w).
(3) Lueders bound K3 <= 3/2: the algebraic identity (Q1 - Q2 + Q3)^2 = 3 - 2C12 - 2C23 + 2C13 for
    Lueders two-time correlators (any dimension), checked symbolically on the two-qubit example, and
    the identity P+ Q P+ - P- Q P- = {Qi,Q}/2.
(4) A4.1(c) CNOT-from-ancilla: C12 = cos 2 theta.
(5) A4.1(a)/(b): exhaustive scan of all affine-symplectic maps with translations on one and two F_2 modes,
    read model 'Z read records z, adds an independent uniform kick to the carrier x'; supplies sharp,
    half-known (SA-1(c)) or environment; max over the four K3 forms. Witness of A4.1(b) checked.
(6) Q4-D1 strengthening: in the witness G, the t2 read never reaches z3; mixture weights giving K3 = 3/2.
(7) Q4-P10 / A4.6 comparator values; Q4-D7 maximally mixed NSIT.
"""
import itertools
from fractions import Fraction as Fr
import sympy as sp

I2 = sp.eye(2); X = sp.Matrix([[0, 1], [1, 0]]); Z = sp.Matrix([[1, 0], [0, -1]])
Y = sp.Matrix([[0, -sp.I], [sp.I, 0]]); H = sp.Matrix([[1, 1], [1, -1]]) / sp.sqrt(2)
kron = lambda *ms: sp.Matrix(sp.kronecker_product(*ms)) if len(ms) > 1 else ms[0]
P0 = sp.Matrix([[1, 0], [0, 0]]); P1 = sp.Matrix([[0, 0], [0, 1]])

def bloch_state(nx, ny, nz):
    return (I2 + nx * X + ny * Y + nz * Z) / 2

def lueders_C(rho, U, Q, i, j):
    """two-read Lueders correlator: reads only at t_i, t_j; U applied between consecutive times"""
    Ui = U ** (i - 1); Uij = U ** (j - i)
    rho_i = Ui * rho * Ui.H
    Qj = Uij.H * Q * Uij
    return sp.simplify(sp.re(sp.simplify((rho_i * (Q * Qj + Qj * Q) / 2).trace())))

def K3(rho, U, Q):
    c12, c23, c13 = (lueders_C(rho, U, Q, 1, 2), lueders_C(rho, U, Q, 2, 3), lueders_C(rho, U, Q, 1, 3))
    return c12, c23, c13, sp.simplify(c12 + c23 - c13)

b = sp.symbols('beta', real=True)
plus = bloch_state(1, 0, 0)
med = bloch_state(sp.sin(b), 0, sp.cos(b))

def cnot(control_first):
    # 2 qubits, ordering (q1, q2); control_first: control = q1, target = q2
    return kron(P0, I2) + kron(P1, X) if control_first else kron(I2, P0) + kron(X, P1)

print('(1) G = (I (x) H) . CNOT_{m->c}, carrier |+>, mediator (sin b, 0, cos b), Lueders Z_c reads')
results = {}
for order in ('c(x)m', 'm(x)c'):
    if order == 'c(x)m':
        rho = kron(plus, med); Zc = kron(Z, I2); CN = cnot(control_first=False)
        Hc, Hm = kron(H, I2), kron(I2, H)
    else:
        rho = kron(med, plus); Zc = kron(I2, Z); CN = cnot(control_first=True)
        Hc, Hm = kron(I2, H), kron(H, I2)
    # 'I (x) H' acts on the second tensor factor
    second_is_carrier = (order == 'm(x)c')
    for label, Hf in (('H on carrier', Hc), ('H on mediator', Hm)):
        G = Hf * CN
        c12, c23, c13, k = K3(rho, G, Zc)
        print(f'   order {order}, {label}{" [= literal I(x)H]" if (label=="H on carrier")==second_is_carrier else ""}:'
              f' C12={sp.simplify(c12)}, C23={sp.simplify(c23)}, C13={sp.simplify(c13)}, K3={sp.simplify(k)}')
        results[(order, label)] = k
k_target = sp.cos(b) + sp.sin(b)
ok_hc = all(sp.simplify(results[(o, 'H on carrier')] - k_target) == 0 for o in ('c(x)m', 'm(x)c'))
print('   K3 = cos b + sin b when H acts on the carrier:', ok_hc)
print('   values: b=pi/4 ->', sp.nsimplify(k_target.subs(b, sp.pi / 4)), '; (cos,sin)=(4/5,3/5) ->', Fr(4, 5) + Fr(3, 5))

# second construction: G = (I (x) H) . SWAP . CNOT_{m->c}, mediator |0>, carrier (sin b,0,cos b)
SWAP = sp.Matrix([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]])
car = bloch_state(sp.sin(b), 0, sp.cos(b)); m0 = bloch_state(0, 0, 1)
print('    G = (I (x) H) . SWAP . CNOT_{m->c}, mediator |0>, carrier (sin b,0,cos b):')
for order in ('c(x)m', 'm(x)c'):
    if order == 'c(x)m':
        rho = kron(car, m0); Zc = kron(Z, I2); CN = cnot(control_first=False); Hc, Hm = kron(H, I2), kron(I2, H)
    else:
        rho = kron(m0, car); Zc = kron(I2, Z); CN = cnot(control_first=True); Hc, Hm = kron(I2, H), kron(H, I2)
    for label, Hf in (('H on carrier', Hc), ('H on mediator', Hm)):
        c12, c23, c13, k = K3(rho, Hf * SWAP * CN, Zc)
        print(f'   order {order}, {label}: (C12,C23,C13)=({sp.simplify(c12)}, {sp.simplify(c23)}, {sp.simplify(c13)}), K3={sp.simplify(k)}')

# (2) measure-and-reprepare
print('(2) measure-and-reprepare, G = X, preparation |0>')
w = sp.symbols('w')
def mr_K3(w):
    # classical: state is a distribution over |0>,|1>; read Z gives z; reprepare other eigenstate w.p. w
    def evolve(p0):  # G = X swaps
        return 1 - p0
    def read(p0):    # returns list of (z, prob, new p0)
        return [(+1, p0, 1 - w), (-1, 1 - p0, w)]  # z=+1: other eigenstate |1> w.p. w -> p0 = 1-w
    def corr(i, j):
        p0 = sp.Integer(1); tot = 0
        for _ in range(i - 1): p0 = evolve(p0)
        for zi, pi, q0 in read(p0):
            q = q0
            for _ in range(j - i): q = evolve(q)
            tot += pi * zi * (q * 1 + (1 - q) * (-1))
        return sp.expand(tot)
    return corr(1, 2), corr(2, 3), corr(1, 3)
c = mr_K3(w)
Kw = sp.expand(c[0] + c[1] - c[2])
print('   C12, C23, C13 =', c, '; K3 =', Kw, '; w=1 ->', Kw.subs(w, 1), '; K3=2 at w =', sp.solve(sp.Eq(Kw, 2), w))
assert Kw == 6 * w - 3

# (3) Lueders bound identity
print('(3) Lueders bound: (Q1 - Q2 + Q3)^2 >= 0  =>  C12 + C23 - C13 <= 3/2 (any dimension).')
rho = kron(plus, med); Zc = kron(Z, I2); G = kron(H, I2) * cnot(False)
Q1 = Zc; Q2 = G.H * Zc * G; Q3 = (G ** 2).H * Zc * G ** 2
M = (Q1 - Q2 + Q3); lhs = sp.simplify((rho * M * M).trace())
c12, c23, c13, k = K3(rho, G, Zc)
print('   <(Q1-Q2+Q3)^2> - (3 - 2 K3) =', sp.simplify(lhs - (3 - 2 * k)))
Qi, Qj = sp.symbols('Qi Qj', commutative=False)
Pp, Pm = (1 + Qi) / 2, (1 - Qi) / 2
print('   P+ Qj P+ - P- Qj P- - (QiQj+QjQi)/2 =', sp.expand(Pp * Qj * Pp - Pm * Qj * Pm - (Qi * Qj + Qj * Qi) / 2))

# (4) CNOT from ancilla
th = sp.symbols('theta', real=True)
anc = sp.Matrix([sp.cos(th), sp.sin(th)]); anc = anc * anc.T
rho = kron(bloch_state(0, 0, 1), anc)    # carrier first
G = cnot(control_first=False)            # ancilla (q2) controls carrier (q1)
print('(4) CNOT ancilla->carrier: C12 =', sp.simplify(sp.trigsimp(lueders_C(rho, G, kron(Z, I2), 1, 2))))

# (5) affine-symplectic scans over F_2
def matmul(Mx, v): return tuple(sum(Mx[i][k] * v[k] for k in range(len(v))) % 2 for i in range(len(Mx)))
def symplectic_group(nm):
    d = 2 * nm
    J = [[0] * d for _ in range(d)]
    for m in range(nm): J[2 * m][2 * m + 1] = J[2 * m + 1][2 * m] = 1
    out = []
    for bits in itertools.product((0, 1), repeat=d * d):
        Mx = [list(bits[r * d:(r + 1) * d]) for r in range(d)]
        ok = True
        for i in range(d):
            for j in range(d):
                s = sum(Mx[k][i] * J[k][l] * Mx[l][j] for k in range(d) for l in range(d)) % 2
                if s != J[i][j]: ok = False; break
            if not ok: break
        if ok: out.append(Mx)
    return out

def scan(nm, supplies):
    """variables per mode m: (z_m, x_m) at coordinates 2m, 2m+1; carrier = mode 0.
    A configuration is an affine function of random bits; represent each coordinate as (lin: tuple over rand bits, const)."""
    G = symplectic_group(nm); d = 2 * nm
    best = {}
    for Mx in G:
        for t in itertools.product((0, 1), repeat=d):
            for sup_name, sup in supplies.items():
                for prep in sup:
                    vals = []
                    for (i, j) in ((1, 2), (2, 3), (1, 3)):
                        vals.append(corr(Mx, t, prep, i, j, nm))
                    c12, c23, c13 = vals
                    for s1, s2 in itertools.product((1, -1), repeat=2):
                        s3 = -s1 * s2
                        K = s1 * c12 + s2 * c23 + s3 * c13
                        if sup_name not in best or K > best[sup_name][0]:
                            best[sup_name] = (K, Mx, t, prep, (c12, c23, c13))
    return len(G), best

NR = 12  # random bits budget: supply unknowns + kicks
def corr(Mx, t, prep, i, j, nm):
    d = 2 * nm
    # prep: list of d entries, each either ('k', value) known or ('u', idx) unknown uniform bit idx
    state = []
    for e in prep:
        lin = [0] * NR; c = 0
        if e[0] == 'k': c = e[1]
        elif e[0] == 'u': lin[e[1]] = 1
        else:  # ('f', known functional value) handled by caller via linear combos
            raise ValueError
        state.append((tuple(lin), c))
    kick = 10
    def apply(st):
        out = []
        for r in range(d):
            lin = [0] * NR; c = t[r]
            for k in range(d):
                if Mx[r][k]:
                    lin = [(a + bb) % 2 for a, bb in zip(lin, st[k][0])]; c = (c + st[k][1]) % 2
            out.append((tuple(lin), c))
        return out
    st = state
    for _ in range(i - 1): st = apply(st)
    zi = st[0]
    # read at t_i: record z, kick carrier x by fresh uniform bit
    lin = list(st[1][0]); lin[kick] = (lin[kick] + 1) % 2; st = [st[0], (tuple(lin), st[1][1])] + st[2:]
    for _ in range(j - i): st = apply(st)
    zj = st[0]
    tot_lin = tuple((a + bb) % 2 for a, bb in zip(zi[0], zj[0])); tot_c = (zi[1] + zj[1]) % 2
    if any(tot_lin): return 0
    return 1 - 2 * tot_c

def half_known(nm_mode_base, ubit):
    """half-known mode: exactly one known linear functional (z, x, or z+x), other uniform.
    Represent z+x known=v as z = u, x = u + v."""
    out = []
    for f in ('z', 'x', 'zx'):
        for v in (0, 1):
            if f == 'z': out.append([('k', v), ('u', ubit)])
            elif f == 'x': out.append([('u', ubit), ('k', v)])
            else: out.append(('zx', v, ubit))
    return out

def expand_prep(car, med):
    pass

# build supplies for one and two modes; 'zx' entries need linear encoding -> handle by building state directly
def mode_entries(spec, ubit):
    if spec[0] == 'zx':
        v = spec[1]
        lin = [0] * NR; lin[ubit] = 1
        return [(tuple(lin), 0), (tuple(lin), v)]
    out = []
    for e in spec:
        lin = [0] * NR; c = 0
        if e[0] == 'k': c = e[1]
        else: lin[e[1]] = 1
        out.append((tuple(lin), c))
    return out

# override corr's state construction to accept pre-built entries
def corr(Mx, t, prep, i, j, nm):
    d = 2 * nm; kick = 10
    st = list(prep)
    def apply(st):
        out = []
        for r in range(d):
            lin = [0] * NR; c = t[r]
            for k in range(d):
                if Mx[r][k]:
                    lin = [(a + bb) % 2 for a, bb in zip(lin, st[k][0])]; c = (c + st[k][1]) % 2
            out.append((tuple(lin), c))
        return out
    for _ in range(i - 1): st = apply(st)
    zi = st[0]
    lin = list(st[1][0]); lin[kick] ^= 1; st = [st[0], (tuple(lin), st[1][1])] + st[2:]
    for _ in range(j - i): st = apply(st)
    zj = st[0]
    tot_lin = tuple((a + bb) % 2 for a, bb in zip(zi[0], zj[0])); tot_c = (zi[1] + zj[1]) % 2
    return 0 if any(tot_lin) else 1 - 2 * tot_c

def hk_specs(ubit):
    specs = []
    for v in (0, 1):
        specs += [[('k', v), ('u', ubit)], [('u', ubit), ('k', v)], ('zx', v)]
    return specs

carrier_preps = [mode_entries(s, 0) for s in hk_specs(0)]
one = {'carrier half-known': [c for c in carrier_preps]}
n1, best1 = scan(1, one)
print('(5a) one mode: |Sp(2,F2)| =', n1, '; maps with translations =', n1 * 4, '; max K3 =', {k: v[0] for k, v in best1.items()})

med_half = [mode_entries(s, 1) for s in hk_specs(1)]
med_env = [[(tuple(1 if r == 1 else 0 for r in range(NR)), 0), (tuple(1 if r == 2 else 0 for r in range(NR)), 0)]]
med_sharp = [mode_entries([('k', v), ('k', u)], 1) for v in (0, 1) for u in (0, 1)]
two = {'half-known': [c + m for c in carrier_preps for m in med_half],
       'environment': [c + m for c in carrier_preps for m in med_env],
       'sharp': [c + m for c in carrier_preps for m in med_sharp]}
n2, best2 = scan(2, two)
print('(5b) two modes: |Sp(4,F2)| =', n2, '; maps with translations =', n2 * 16)
for k, v in best2.items():
    print(f'   mediator {k}: max K3 = {v[0]} (correlators {v[4]})')
assert best2['half-known'][0] == 1 and best2['environment'][0] == 1 and best2['sharp'][0] == 2

# witness of A4.1(b): z' = z + v, x' = w, w' = z, v' = x + w ; coordinates (z, x, v, w)
# check symplecticity w.r.t. pairs (z,x),(v,w)
Wm = [[1, 0, 1, 0], [0, 0, 0, 1], [0, 1, 0, 1], [1, 0, 0, 0]]  # rows: z', x', v', w'
in_group = Wm in symplectic_group(2)
carX = mode_entries([('u', 0), ('k', 0)], 0)  # X+ : x known 0
medsharp = mode_entries([('k', 0), ('k', 0)], 1)
vals = [corr(Wm, (0, 0, 0, 0), carX + medsharp, i, j, 2) for (i, j) in ((1, 2), (2, 3), (1, 3))]
print('   witness symplectic (pairs (z,x),(v,w)):', in_group, '; (C12,C23,C13) =', vals, '; K3 =', vals[0] + vals[1] - vals[2])
# variant with (v,w) pairing swapped
Wm2 = [[1, 0, 1, 0], [0, 0, 0, 1], [0, 1, 0, 1], [1, 0, 0, 0]]

# (6) Q4-D1: t2 read reaches z3? z3 = z2 + v2 and v2 depends on pre-t2 x only -> kick at t2 lands in v3, not z3.
# mixture: witness (K=2) with environment-mediator run of same G
env = carX + med_env[0]
vals_env = [corr(Wm, (0, 0, 0, 0), env, i, j, 2) for (i, j) in ((1, 2), (2, 3), (1, 3))]
Kenv = vals_env[0] + vals_env[1] - vals_env[2]
p = sp.symbols('p')
sol = sp.solve(sp.Eq(2 * p + Kenv * (1 - p), sp.Rational(3, 2)), p)
print('(6) same G, environment mediator: correlators', vals_env, 'K3 =', Kenv, '; mixture weight on sharp giving K3 = 3/2:', sol)
# verify t2 read is ineffective on z3 for every prep: kick only on x at t2; z3 coefficient of kick bit
def kick_reaches_z3(Mx):
    # z3 = row0 of Mx applied to state after kick; kick on coordinate 1 (x)
    return Mx[0][1] == 1
print('   t2 kick enters z3 in one step for witness G:', kick_reaches_z3(Wm))

# (7) A4.6 values, and Q4-D7
th = sp.symbols('th')
C = lambda nz2, t: nz2 + (1 - nz2) * sp.cos(t)
K = lambda nz2, t: sp.nsimplify(sp.simplify(2 * C(nz2, t) - C(nz2, 2 * t)))
print('(7) K3 axis perp z at pi/3:', K(0, sp.pi / 3), '; at arccos(3/5):', sp.simplify(K(0, sp.acos(sp.Rational(3, 5)))),
      '; body diagonal at pi/3:', K(sp.Rational(1, 3), sp.pi / 3),
      '; order-3, z in plane, C12+C23+C13 =', sp.simplify(2 * C(0, 2 * sp.pi / 3) + C(0, 4 * sp.pi / 3)))
rho = sp.eye(2) / 2; Uq = sp.Matrix([[sp.cos(sp.pi/8), -sp.sin(sp.pi/8)], [sp.sin(sp.pi/8), sp.cos(sp.pi/8)]])
PXp = (I2 + X) / 2; PXm = (I2 - X) / 2
p_without = sp.simplify(((Uq * rho * Uq.H) * P0).trace())
rho2 = PXp * rho * PXp + PXm * rho * PXm
p_with = sp.simplify(((Uq * rho2 * Uq.H) * P0).trace())
print('   Q4-D7 maximally mixed: P(z3=+1) without / with X read at t2:', p_without, p_with)
print('LG PROBE DONE')
