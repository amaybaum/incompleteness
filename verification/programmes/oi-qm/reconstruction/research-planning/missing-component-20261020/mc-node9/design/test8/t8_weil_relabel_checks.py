# Test-8 design, exact checks on Weil lifts of the shear layer and on relabellings.
# Run: python3 -I t8_weil_relabel_checks.py > t8_weil_relabel_checks.out
# Integers and Gaussian integers (as pairs) only.
from itertools import product, permutations

# Gaussian integers as (re, im); fourth roots of unity
ROOTS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
def gmul(a, b): return (a[0]*b[0] - a[1]*b[1], a[0]*b[1] + a[1]*b[0])
def gconj(a): return (a[0], -a[1])

def bits(c, n): return tuple((c >> k) & 1 for k in range(n))
def frombits(v): return sum(b << k for k, b in enumerate(v))

def diag_lifts(L, n):
    """All diagonal D = diag(d_c), d_0 = 1, d_c fourth roots, with
    D X^a D^dag = d_a X^a Z^{La} for every a: the Weil lifts of the shear (p,c) -> (p + Lc, c)
    that fix the position basis.  (Completeness of fourth roots: d_a^2 = (-1)^{a.La}, see design.)"""
    N = 1 << n; found = []
    for ds in product(ROOTS, repeat=N - 1):
        d = [(1, 0)] + list(ds); ok = True
        for a in range(N):
            av = bits(a, n)
            La = [sum(L[i][j]*av[j] for j in range(n)) % 2 for i in range(n)]
            for c in range(N):
                cv = bits(c, n)
                s = (-1)**(sum(La[i]*cv[i] for i in range(n)) % 2)
                lhs = gmul(d[a ^ c], gconj(d[c]))
                rhs = (d[a][0]*s, d[a][1]*s)
                if lhs != rhs: ok = False; break
            if not ok: break
        if ok: found.append(d)
    return found

out = []
def say(*a): out.append(" ".join(str(x) for x in a))

say("== node 4: diagonal Weil lifts of the shear (p,c) -> (p + Lc, c) over F2, positions c in F2^n")
cases = [
    ("n=1, L=[1] (centre term, the C5 audit's site shear)", 1, [[1]]),
    ("n=1, L=[0] (isolated centre-free site)", 1, [[0]]),
    ("n=2, path, centre-free (Main.md:290 form)", 2, [[0, 1], [1, 0]]),
    ("n=2, path + centre term at site 0", 2, [[1, 1], [1, 0]]),
    ("n=3, path, centre-free", 3, [[0, 1, 0], [1, 0, 1], [0, 1, 0]]),
    ("n=3, triangle, centre-free", 3, [[0, 1, 1], [1, 0, 1], [1, 1, 0]]),
    ("n=3, triangle, centre terms everywhere", 3, [[1, 1, 1], [1, 1, 1], [1, 1, 1]]),
]
for name, n, L in cases:
    lifts = diag_lifts(L, n)
    nonreal = [d for d in lifts if any(x[1] != 0 for x in d)]
    # criterion: d_a is +-i exactly when sum_x L_xx a_x is odd
    crit = all(((d[a][1] != 0) == (sum(L[x][x]*bits(a, n)[x] for x in range(n)) % 2 == 1))
               for d in lifts for a in range(1 << n))
    say(f"{name}: {len(lifts)} lifts (expected 2^n = {1 << n}); any non-real entry: {bool(nonreal)};"
        f" criterion 'd_a = +-i iff sum_x L_xx a_x odd' holds: {crit}")
    if n == 1:
        say("   lifts:", [[f"{x[0]}+{x[1]}i" for x in d] for d in lifts])

say("\n== addendum (1): which position permutations are Clifford (normalize the Pauli group), n = 3 positions")
n = 3; N = 8
def is_affine(pi):
    b = pi[0]
    cols = [pi[1 << k] ^ b for k in range(n)]
    for x in range(N):
        y = b
        for k in range(n):
            if (x >> k) & 1: y ^= cols[k]
        if pi[x] != y: return False
    return True
def is_clifford_perm(pi):
    inv = [0]*N
    for x, y in enumerate(pi): inv[y] = x
    # P X_k P^dag is the permutation x -> pi(inv(x) ^ e_k): Pauli (up to phase) iff a translation
    for k in range(n):
        f = [pi[inv[x] ^ (1 << k)] for x in range(N)]
        t = f[0] ^ 0
        if any(f[x] != x ^ t for x in range(N)): return False
    # P Z_k P^dag = diag((-1)^{bit_k(inv(x))}): Pauli up to phase iff bit_k o inv is affine
    for k in range(n):
        g = [(inv[x] >> k) & 1 for x in range(N)]
        ok = False
        for lin in range(N):
            for c0 in (0, 1):
                if all(g[x] == (bin(lin & x).count("1") + c0) % 2 for x in range(N)): ok = True
        if not ok: return False
    return True
cnt_aff = cnt_cl = agree = 0; total = 0
for pi in permutations(range(N)):
    total += 1
    a, c = is_affine(pi), is_clifford_perm(pi)
    cnt_aff += a; cnt_cl += c; agree += (a == c)
say(f"permutations of 8 positions: {total}; affine: {cnt_aff}; Clifford: {cnt_cl}; agree everywhere: {agree == total}")
tof = [x ^ 4 if (x & 3) == 3 else x for x in range(N)]
say("Toffoli (flip bit 2 when bits 0,1 set) affine:", is_affine(tof), "| Clifford:", is_clifford_perm(tof))
say("single exchange |110> <-> |111> is the Toffoli; at n = 2 every one of the 24 permutations is affine:",
    sum(1 for p in permutations(range(4))
        if all(p[x] == (p[0] ^ (p[1] ^ p[0] if x & 1 else 0) ^ (p[2] ^ p[0] if x & 2 else 0)) for x in range(4))) == 24)

say("\n== addendum (1): the shear layer read on the position carrier vs its Weil image")
# configurations (p,c) of one site; the shear fixes c, so as a relabelling it acts on positions as the identity
shear = lambda p, c: ((c - p) % 2, c)
say("shear preserves the current value at every configuration:", all(shear(p, c)[1] == c for p in (0, 1) for c in (0, 1)),
    "-> position-carrier permutation it induces: identity; Weil image (L=[1]): diag(1, +-i), not identity")

say("\n== addendum (1): the card-report witness, recomputed")
# product of Bloch vectors a, b each in {+-x, +-z}: <X(x)Z> + <Z(x)X> = a_x b_z + a_z b_x
verts = [(1, 0), (-1, 0), (0, 1), (0, -1)]       # (x, z) components
best = max(a[0]*b[1] + a[1]*b[0] for a in verts for b in verts)
say("max over products of X/Z card vertices of <XZ>+<ZX>:", best, "(affine mixtures cannot exceed the max)")
# graph state (|00>+|01>+|10>-|11>)/2, amplitudes times 2
psi = {0: 1, 1: 1, 2: 1, 3: -1}           # index = 2*q0 + q1
def expXZ(xfirst):
    # <psi| X (x) Z |psi> (xfirst) or Z (x) X, times 4
    s = 0
    for i in range(4):
        q0, q1 = i >> 1, i & 1
        if xfirst: j = ((1 - q0) << 1) | q1; ph = (-1)**q1
        else: j = (q0 << 1) | (1 - q1); ph = (-1)**q0
        s += psi[j]*ph*psi[i]
    return s
say("graph state 4*<X(x)Z> =", expXZ(True), ", 4*<Z(x)X> =", expXZ(False), "-> sum =", (expXZ(True) + expXZ(False)) // 4)

say("\n== addendum (2): squared moduli of entries of PolC unitaries lie in Z[1/sqrt2]; rational ones in Z[1/2]")
from fractions import Fraction as Fr
def in_Z_half(q): q = Fr(q); d = q.denominator; return d & (d - 1) == 0
for name, cos2 in [("T6 rotation, cos^2 = 4/5", Fr(4, 5)), ("report-3 R, cos^2 = 9/25", Fr(9, 25)),
                   ("H-type, cos^2 = 1/2", Fr(1, 2)), ("cos^2 = 5/8 (alpha/pi irrational, not excluded)", Fr(5, 8))]:
    say(f"{name}: cos^2 in Z[1/2]: {in_Z_half(cos2)}, sin^2 in Z[1/2]: {in_Z_half(1 - cos2)}")

print("\n".join(out))
