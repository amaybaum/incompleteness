"""A45 Q1 exact classifier probe (research, not frozen).

Five admissible static realizations at the product configuration, all flat unitaries (scaled by 4), hence all
admissible dilations (trivial ancilla) of the same visible slice J/16:
  R0 SIG;  R1 D1 SIG D2 (two-sided gauge, Gaussian-rational unit diagonals);  R2 a row and column relabelling of SIG;
  R3 H3(1, v2, v3) (a Dita face point of act 39's family);  R4 SIG o v^E40 (A42's support-40 line, off every structure).
For each carrier applicable to a single dilation, the value on each realization, and the classification rule fixed in
the A45 note: VISIBLE-ONLY needs equality on every pair sharing the visible slice (here: all pairs) together with a
factorization proof cited in the note; LIFT-DEPENDENT needs an exhibited pair with equal visible slice and different
values. CLASS-LEVEL marks a lift-dependent carrier equal on R0/R1 (two-sided invariant) and separating R3/R4.
Q_fb is instantiated through a NAMED embedding the corpus does not certify (U := H/4, init uniform, read = id).
"""
import itertools, json, random, sys
from fractions import Fraction as Fr

class G:
    __slots__ = ('a', 'b')
    def __init__(s, a, b=0): s.a = Fr(a); s.b = Fr(b)
    def __mul__(s, o): return G(s.a * o.a - s.b * o.b, s.a * o.b + s.b * o.a)
    def __add__(s, o): return G(s.a + o.a, s.b + o.b)
    def __sub__(s, o): return G(s.a - o.a, s.b - o.b)
    def __neg__(s): return G(-s.a, -s.b)
    def conj(s): return G(s.a, -s.b)
    def __eq__(s, o): return s.a == o.a and s.b == o.b
    def __hash__(s): return hash((s.a, s.b))
    def n2(s): return s.a * s.a + s.b * s.b
    def __repr__(s): return '(%s%+si)' % (s.a, s.b)
ZERO, ONE, I_ = G(0), G(1), G(0, 1)
def F4(t): return [[ONE, ONE, ONE, ONE], [ONE, t, G(-1), -t], [ONE, G(-1), ONE, G(-1)], [ONE, -t, G(-1), t]]
z, w = G(Fr(3, 5), Fr(4, 5)), G(Fr(5, 13), Fr(12, 13))
FZ, FW = F4(z), F4(w)
SIG = [[FZ[i // 4][j // 4] * FW[i % 4][j % 4] for j in range(16)] for i in range(16)]
def gpow(u, k):
    out = ONE
    for _ in range(abs(k)): out = out * (u if k > 0 else u.conj())
    return out
def piece(f): return [[f(i // 4, i % 4, j // 4, j % 4) for j in range(16)] for i in range(16)]
EA = piece(lambda a, b, c, d: int(a % 2 == 1 and b == 3 and c % 2 == 1)); EB = piece(lambda a, b, c, d: int(a == 2 and d == 1))
EC = piece(lambda a, b, c, d: int((a + b) % 2 == 1 and (c, d) in ((0, 2), (2, 0))))
E40 = piece(lambda a, b, c, d: -int(b == 0 and c == 0) + int(a == 2 and b % 2 == 1 and d % 2 == 0) - int(a % 2 == 0 and c % 2 == 1 and d == 0))
v1, v2, v3 = G(Fr(3, 5), Fr(4, 5)), G(Fr(5, 13), Fr(12, 13)), G(Fr(8, 17), Fr(15, 17))
def H3(u1, u2, u3): return [[SIG[i][j] * gpow(u1, EA[i][j]) * gpow(u2, EB[i][j]) * gpow(u3, EC[i][j]) for j in range(16)] for i in range(16)]
rng = random.Random(45)
units = [G(Fr(3, 5), Fr(4, 5)), G(Fr(5, 13), Fr(12, 13)), G(Fr(8, 17), Fr(15, 17)), G(Fr(7, 25), Fr(24, 25)), I_, G(-1), ONE]
d1 = [rng.choice(units) for _ in range(16)]; d2 = [rng.choice(units) for _ in range(16)]
R1 = [[d1[i] * SIG[i][j] * d2[j] for j in range(16)] for i in range(16)]
pr = list(range(16)); rng.shuffle(pr); pc = list(range(16)); rng.shuffle(pc)
R2 = [[SIG[pr[i]][pc[j]] for j in range(16)] for i in range(16)]
R3 = H3(ONE, v2, v3)
R4 = [[SIG[i][j] * gpow(v1, E40[i][j]) for j in range(16)] for i in range(16)]
REAL = {'R0 SIG': SIG, 'R1 D1.SIG.D2': R1, 'R2 relabelled SIG': R2, 'R3 H3(1,v2,v3) Dita': R3, 'R4 SIG o v^E40 non-Dita': R4}

def flat_unitary(H):
    if any(x.n2() != 1 for r in H for x in r): return False
    for i in range(16):
        for k in range(16):
            s = ZERO
            for j in range(16): s = s + H[i][j] * H[k][j].conj()
            if s != (G(16) if i == k else ZERO): return False
    return True
# ---- carriers on a single dilation pad H (trivial ancilla), H scaled by 4: U = H / 4 ------------------------------------
def visible_slice(H): return tuple(tuple(x.n2() / 16 for x in r) for r in H)                    # O0 = readback |pad H|^2
def qfb_rooted(H, T=3):                                                                           # named embedding
    M = [[H[b2][b].n2() / 16 for b2 in range(16)] for b in range(16)]                           # born(b, b2) = |U b2 b|^2
    P = [[Fr(int(i == j)) for j in range(16)] for i in range(16)]; out = []
    for t in range(T + 1):
        out.append(tuple(tuple(r) for r in P))
        P = [[sum(P[i][k] * M[k][j] for k in range(16)) for j in range(16)] for i in range(16)]
    return tuple(out)
def fibre_gram(H, i): return [[H[i][j].conj() * H[i][k] for k in range(16)] for j in range(16)]   # x 16
FG = {}
def fg(nm, i):
    if (nm, i) not in FG: FG[(nm, i)] = fibre_gram(REAL[nm], i)
    return FG[(nm, i)]
COORDS = [tuple(rng.randrange(16) for _ in range(6)) for _ in range(3000)]
def feature_sample(nm):                                                                           # mixedTriple coordinates (x 16^3)
    return tuple(fg(nm, i1)[j1][j2] * fg(nm, i2)[j2][j3] * fg(nm, i3)[j3][j1] for (i1, i2, i3, j1, j2, j3) in COORDS)
def fibre_gram_all(nm): return tuple(tuple(tuple(x for x in r) for r in fg(nm, i)) for i in range(16))
def anchored_channel(H, rho):                                                                     # O1 (x 16): H rho H^*
    A = [[sum((H[i][k] * rho[k][l] for k in range(16)), ZERO) for l in range(16)] for i in range(16)]
    return tuple(tuple(sum((A[i][l] * H[i2][l].conj() for l in range(16)), ZERO) for i2 in range(16)) for i in range(16))
RHO = [[ONE if (k, l) == (0, 1) else ZERO for l in range(16)] for k in range(16)]
def entry01(H): return H[0][1]

CARRIERS = {
    'O0 visible slice (readback of |pad H|^2)': lambda nm: visible_slice(REAL[nm]),
    'Q_fb rooted family t<=3 [named embedding]': lambda nm: qfb_rooted(REAL[nm]),
    'FibreGram tuple (raw)': fibre_gram_all,
    'featureVec (3000 mixedTriple coordinates)': feature_sample,
    'O1 AnchoredChannel on rho = E_01': lambda nm: anchored_channel(REAL[nm], RHO),
    'toy: entry H[0][1]': lambda nm: entry01(REAL[nm]),
}
out = {'flat_unitary': {nm: flat_unitary(H) for nm, H in REAL.items()}}
print('flat unitary (hence admissible dilations of J/16):', out['flat_unitary'], flush=True)
vis = {nm: visible_slice(H) for nm, H in REAL.items()}
out['same_visible_slice'] = len(set(vis.values())) == 1
names = list(REAL)
out['carriers'] = {}
for cn, f in CARRIERS.items():
    vals = {nm: f(nm) for nm in names}
    pairs = {(a, b): vals[a] == vals[b] for a, b in itertools.combinations(names, 2)}
    all_equal = all(pairs.values())
    gauge_inv = pairs[(names[0], names[1])]; relabel_inv = pairs[(names[0], names[2])]; separates_34 = not pairs[(names[3], names[4])]
    first_diff = next((p for p, e in pairs.items() if not e), None)
    cls = 'VISIBLE-CANDIDATE (equal on all pairs; needs a factorization proof)' if all_equal else ('LIFT-DEPENDENT, CLASS-LEVEL' if gauge_inv else 'LIFT-DEPENDENT, REPRESENTATIVE-LEVEL')
    out['carriers'][cn] = {'all_equal': all_equal, 'two_sided_invariant_R0R1': gauge_inv, 'relabel_invariant_R0R2': relabel_inv,
                           'separates_Dita_R3_from_nonDita_R4': separates_34, 'exhibited_pair': list(first_diff) if first_diff else None, 'class': cls}
    print('%-46s %-62s gauge-inv %-5s relabel-inv %-5s R3|R4 %-5s pair %s' % (cn, cls, gauge_inv, relabel_inv, separates_34, first_diff), flush=True)
# the controls fixed in the note
c = out['carriers']
out['controls'] = {
    'O0 comes out visible (all equal)': c['O0 visible slice (readback of |pad H|^2)']['all_equal'],
    'featureVec comes out lift-dependent with an exhibited pair (not visible)': not c['featureVec (3000 mixedTriple coordinates)']['all_equal'],
    'O1 comes out lift-dependent with an exhibited pair (not visible)': not c['O1 AnchoredChannel on rho = E_01']['all_equal'],
    'FibreGram comes out lift-dependent': not c['FibreGram tuple (raw)']['all_equal'],
    'toy entry is representative-level, not class-level and not visible': (not c['toy: entry H[0][1]']['all_equal']) and not c['toy: entry H[0][1]']['two_sided_invariant_R0R1'],
    'all five realizations share the visible slice': out['same_visible_slice'],
}
print('controls:', out['controls'])
print('ALL CONTROLS GREEN' if all(out['controls'].values()) else 'A CONTROL IS RED')
json.dump(out, open(sys.argv[1] if len(sys.argv) > 1 else 'q1_probe.json', 'w'), indent=1, sort_keys=True)
