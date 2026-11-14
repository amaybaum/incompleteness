"""Reviewer probe P4 (QPHEN Phase 1 r2 re-review). Exact arithmetic only.

(1) QX6 r2 A6.1, literal reading: a one-tick composite map (op_A o phi o op_B)
    satisfying (D), (L), (R), (MI) as worded, giving the PR box (S = 4).
    The same map violates the tighter (L'): 'the b-dependence of each tick map
    is confined to components at B's sites'.
(2) QX4 r2 R4.9: a copy coupling m <- m + c is affine; an occupation-conditional
    kick x <- x + c*m' is not.
(3) Standard GHZ (|000>+|111>)/sqrt2, Mermin's X/Y operators: exact values.
"""
import itertools
from fractions import Fraction

# ---------- (1) A6.1 literal counterexample ----------
# sites: A region = {rho, rho_out, lamA}; B region = {beta_set, beta_out, lamB}
SITES = ['rho', 'rho_out', 'lamA', 'beta_set', 'beta_out', 'lamB']
A_REG = {'rho', 'rho_out', 'lamA'}
B_REG = {'beta_set', 'beta_out', 'lamB'}

def op_B(s, b):            # reads/writes only B's region
    s = dict(s); s['beta_set'] ^= b; return s
def phi(s):                # setting-independent step: rho <- rho xor beta_set
    s = dict(s); s['rho'] ^= s['beta_set']; return s
def op_A(s, a):            # reads/writes only A's region
    s = dict(s); s['rho_out'] ^= (a & s['rho']) ^ s['lamA']; return s
def tick(s, a, b):         # the composite map applied at tick 0 = t_A = t_B = T_A = T_B
    return op_A(phi(op_B(s, b)), a)

def init(lam):
    return {'rho': 0, 'rho_out': 0, 'lamA': lam, 'beta_set': 0, 'beta_out': lam, 'lamB': lam}

def all_states():
    for bits in itertools.product((0, 1), repeat=len(SITES)):
        yield dict(zip(SITES, bits))

def check_bijection(a, b):
    imgs = {tuple(tick(s, a, b)[k] for k in SITES) for s in all_states()}
    return len(imgs) == 2 ** len(SITES)

def dependency_edges():
    """union over settings of one-step dependencies of the tick map: i <- j"""
    E = set()
    for a, b in itertools.product((0, 1), repeat=2):
        for s in all_states():
            base = tick(s, a, b)
            for j in SITES:
                t = dict(s); t[j] ^= 1
                img = tick(t, a, b)
                for i in SITES:
                    if img[i] != base[i]:
                        E.add(frozenset((i, j)) if i != j else frozenset((i,)))
    return {e for e in E if len(e) == 2}

def graph_dist(E, src, dst):
    adj = {v: set() for v in SITES}
    for e in E:
        u, v = tuple(e); adj[u].add(v); adj[v].add(u)
    frontier, seen, d = set(src), set(src), 0
    while frontier:
        if frontier & dst:
            return d
        frontier = {w for v in frontier for w in adj[v]} - seen
        seen |= frontier; d += 1
    return float('inf')

def chsh():
    E = {}
    for a, b in itertools.product((0, 1), repeat=2):
        tot = 0
        for lam in (0, 1):
            s = tick(init(lam), a, b)
            q, r = s['rho_out'], s['beta_out']          # A outcome, B outcome (bits)
            tot += (-1) ** (q ^ r)
        E[(a, b)] = Fraction(tot, 2)
    return E[(0, 0)] + E[(0, 1)] + E[(1, 0)] - E[(1, 1)], E

def b_dependence_outside_B():
    """Does any component outside B's region of the tick map depend on b?"""
    for a in (0, 1):
        for s in all_states():
            t0, t1 = tick(s, a, 0), tick(s, a, 1)
            if any(t0[i] != t1[i] for i in SITES if i not in B_REG):
                return True
    return False

# ---------- (2) R4.9: copy vs conditional kick ----------
def is_affine(F, n):
    V = list(itertools.product((0, 1), repeat=n))
    for x, y, z in itertools.product(V, repeat=3):
        w = tuple((p + q + r) % 2 for p, q, r in zip(x, y, z))
        if any((F(x)[i] + F(y)[i] + F(z)[i] + F(w)[i]) % 2 for i in range(n)):
            return False
    return True

copy_cnot = lambda v: (v[0], v[1], (v[2] + v[0]) % 2, v[3])          # (c, x, m, m'): m <- m + c
recip_cnot = lambda v: (v[0], (v[1] + v[3]) % 2, (v[2] + v[0]) % 2, v[3])  # plus unconditional kick x <- x + m'
cond_kick = lambda v: (v[0], (v[1] + v[0] * v[3]) % 2, (v[2] + v[0]) % 2, v[3])  # kick only if c = 1

# ---------- (3) Standard GHZ with Mermin's X/Y operators ----------
def ghz_expect(label):
    # |GHZ> = (|000> + |111>)/sqrt2 ; Pauli action on basis states, exact with i-powers
    # X: flip; Y: flip with phase i*(-1)^bit; Z: phase (-1)^bit
    def apply(label, idx):
        bits = [(idx >> (2 - k)) & 1 for k in range(3)]
        ph = 0  # power of i
        for k, ch in enumerate(label):
            if ch == 'X':
                bits[k] ^= 1
            elif ch == 'Y':
                ph += 1 + 2 * bits[k]; bits[k] ^= 1
            elif ch == 'Z':
                ph += 2 * bits[k]
        return (bits[0] << 2) | (bits[1] << 1) | bits[2], ph % 4
    amp = {0: 1, 7: 1}
    out = {}
    for idx, a in amp.items():
        j, ph = apply(label, idx)
        out[j] = out.get(j, 0) + a * [1, 1j, -1, -1j][ph]
    val = sum(out.get(k, 0) * amp[k] for k in amp) / 2   # integer-valued complex
    assert val.imag == 0 and float(val.real).is_integer()
    return int(val.real)

if __name__ == '__main__':
    S, E = chsh()
    Edges = dependency_edges()
    print('(1) A6.1 literal counterexample')
    print('    tick map bijective for all settings:', all(check_bijection(a, b) for a in (0, 1) for b in (0, 1)))
    print('    dependency graph G (union over settings):', sorted(tuple(sorted(e)) for e in Edges))
    print('    d_G(B region, R_A={rho_out}) =', graph_dist(Edges, B_REG, {'rho_out'}),
          '> T_A - t_B = 0 :', graph_dist(Edges, B_REG, {'rho_out'}) > 0)
    print('    d_G(A region, R_B={beta_out}) =', graph_dist(Edges, A_REG, {'beta_out'}), '> 0')
    print('    correlators', {k: str(v) for k, v in E.items()}, ' S =', S)
    print("    b-dependence outside B's region of the tick map (violates L'):", b_dependence_outside_B())
    print('(2) copy coupling affine:', is_affine(copy_cnot, 4),
          '| reciprocal CNOT affine:', is_affine(recip_cnot, 4),
          '| occupation-conditional kick affine:', is_affine(cond_kick, 4))
    vals = {l: ghz_expect(l) for l in ('XXX', 'XYY', 'YXY', 'YYX', 'ZZI'.replace('I', 'Z'))}
    print('(3) GHZ (|000>+|111>)/sqrt2:', vals,
          '| Mermin XXX - XYY - YXY - YYX =', vals['XXX'] - vals['XYY'] - vals['YXY'] - vals['YYX'])
