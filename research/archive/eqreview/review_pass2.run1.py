"""Design pass 2 (coordinator; research only, base bcbc516f). Exact checks for the owner's qualifications.

Decision rules, fixed before the run:
  C1  The kernel point idW (identity table; landed: actT reflY phiW = idW, K2Guard) is fixed by EVERY uniform chart
      actC a . actT a with a orthogonal (tested on two proper and two improper exact rational a), and its Pauli image is
      F/2 (F = flip), with value -1/2 at the singlet.  Hence no uniform chart carries the twin into Q3.
      PASS iff all fixed-point identities hold, pauli(idW) == F/2 and <singlet|F/2|singlet> == -1/2.
  C2  Controls: the per-token chart (I, R) carries idW to phiW (PSD, spectrum {0,0,0,1}); countercontrol: the same chart
      carries phiW (a point of Q3) to idW (not PSD), so that chart presents the twin and not Q3.
  C3  The twin's native exchange (omega -> omega^T) under the per-token chart (I, R) is T.SWAP on Pauli tables, and its
      idle extension to a third copy maps |0><0| (x) Phi+ to a matrix with eigenvalue -1/2 (not positive).
      Control: Q3's native exchange under the standard chart is Ad(SWAP); its idle extension keeps the same state PSD.
  G   Generation for EVERY unlabelled tree on n = 3..7 copies: the 2-local Pauli strings on the tree edges close under
      anticommuting products to all 4^n - 1 non-identity strings (su(2^n)).  Countercontrol: deleting any one edge gives
      a forest whose closure is exactly the sum over components with >= 2 vertices of (4^|C| - 1).
"""
import sys
import itertools
import numpy as np
from sympy import Matrix, I, Rational as R, eye, zeros, kronecker_product as kron

checks = []


def check(name, cond):
    checks.append((name, bool(cond)))
    print(("PASS " if cond else "FAIL ") + name)
    sys.stdout.flush()


s0 = eye(2)
sx = Matrix([[0, 1], [1, 0]])
sy = Matrix([[0, -I], [I, 0]])
sz = Matrix([[1, 0], [0, -1]])
P = [s0, sx, sy, sz]


def pauli2(om):
    out = zeros(4, 4)
    for m in range(4):
        for n in range(4):
            if om[m, n] != 0:
                out += om[m, n] * kron(P[m], P[n])
    return out / 4


def coords2(rho):
    return Matrix(4, 4, lambda m, n: (rho * kron(P[m], P[n])).trace())


def hom_mat(a):
    """1 (+) a acting on homogeneous coordinates (index 0 = unit)."""
    M = eye(4)
    M[1:, 1:] = a
    return M


def chart(a, b, om):
    """actC a . actT b on W 3: omega -> (1+a) omega (1+b)^T."""
    return hom_mat(a) * om * hom_mat(b).T


def cayley(A):
    return (eye(3) - A) * (eye(3) + A).inv()


Rf = Matrix.diag(1, -1, 1)                 # reflY on the Bloch vector
idW = eye(4)
phiW = Matrix.diag(1, 1, -1, 1)
check("C1 landed identity reproduced: actT reflY phiW == idW", chart(eye(3), Rf, phiW) == idW)
skews = [Matrix([[0, R(1, 2), R(-1, 3)], [R(-1, 2), 0, R(2, 5)], [R(1, 3), R(-2, 5), 0]]),
         Matrix([[0, 3, 1], [-3, 0, R(-7, 4)], [-1, R(7, 4), 0]])]
orths = []
for A in skews:
    q = cayley(A)
    orths.append(("proper", q))
    orths.append(("improper", q * Rf))
ok_orth = all((q.T * q - eye(3)).is_zero_matrix for _, q in orths)
dets = [q.det() for _, q in orths]
check(f"C1 test charts are exactly orthogonal with determinants {dets}", ok_orth and sorted(dets) == [-1, -1, 1, 1])
check("C1 idW is fixed by every tested uniform chart actC a . actT a (proper and improper a)",
      all(chart(q, q, idW) == idW for _, q in orths))
F = Matrix(4, 4, lambda i, j: 1 if (i // 2, i % 2) == (j % 2, j // 2) else 0)
check("C1 pauli(idW) == F/2 (F the flip of two qubits)", pauli2(idW) == F / 2)
singlet = Matrix([0, 1, -1, 0])
val = (singlet.T * pauli2(idW) * singlet)[0, 0] / (singlet.T * singlet)[0, 0]
check(f"C1 <singlet| pauli(idW) |singlet> = {val} = -1/2, so pauli(idW) is not PSD", val == R(-1, 2))
img = pauli2(chart(eye(3), Rf, idW))
ev = img.eigenvals()
check(f"C2 per-token chart (I, R) carries idW to phiW, spectrum {dict(ev)}",
      chart(eye(3), Rf, idW) == phiW and ev == {0: 3, 1: 1})
check("C2 countercontrol: the same chart carries phiW (in Q3) to idW (not PSD)", chart(eye(3), Rf, phiW) == idW)


# three copies: tables om3[m][n][k], Pauli map with 1/8
def pauli3(om3):
    out = zeros(8, 8)
    for m in range(4):
        for n in range(4):
            for k in range(4):
                c = om3[(m, n, k)]
                if c != 0:
                    out += c * kron(kron(P[m], P[n]), P[k])
    return out / 8


def coords3(rho):
    return {(m, n, k): (rho * kron(kron(P[m], P[n]), P[k])).trace()
            for m in range(4) for n in range(4) for k in range(4)}


def idle_ext(g2, om3):
    """(g (x) id) on three-copy tables, g given as a function on 4x4 tables."""
    out = {}
    for k in range(4):
        sl = Matrix(4, 4, lambda m, n: om3[(m, n, k)])
        im = g2(sl)
        for m in range(4):
            for n in range(4):
                out[(m, n, k)] = im[m, n]
    return out


Rh = hom_mat(Rf)
native_swap = lambda om: om.T
twin_swap_presented = lambda om: Rh * (Rh * om * Rh).T * Rh      # chi . X_nat . chi^{-1}, chi = (I, R)
T_swap = lambda om: Rh * om.T * Rh                                 # T . SWAP on Pauli tables
probe = Matrix(4, 4, lambda m, n: R(m * 4 + n + 1, 7) * (-1) ** (m + n))
check("C3 the twin's native exchange under the per-token chart is T.SWAP (exact on a generic table)",
      twin_swap_presented(probe) == T_swap(probe))
zero = Matrix([1, 0])
phi_plus = Matrix([1, 0, 0, 1])
rho = kron(zero * zero.T, phi_plus * phi_plus.T / 2)              # |0><0|_A (x) Phi+_BC
om3 = coords3(rho)
out_twin = pauli3(idle_ext(T_swap, om3))
spec = out_twin.eigenvals()
check(f"C3 idle extension of T.SWAP maps |0><0| (x) Phi+ to spectrum {dict(spec)}: eigenvalue -1/2, not positive",
      R(-1, 2) in spec)
out_q3 = pauli3(idle_ext(native_swap, om3))
spec_q = out_q3.eigenvals()
check(f"C3 control: Q3's native exchange (Ad SWAP) idly extended keeps the state PSD, spectrum {dict(spec_q)}",
      all(e >= 0 for e in spec_q))

# ---- G: generation over all unlabelled trees, n = 3..7 ----
def prufer_trees(n):
    for seq in itertools.product(range(n), repeat=n - 2):
        degree = [1] * n
        for v in seq:
            degree[v] += 1
        edges = []
        seq = list(seq)
        for v in seq:
            leaf = min(i for i in range(n) if degree[i] == 1)
            edges.append((leaf, v))
            degree[leaf] -= 1
            degree[v] -= 1
        u, w = [i for i in range(n) if degree[i] == 1]
        edges.append((u, w))
        yield edges


def canon(n, edges):
    adj = {i: [] for i in range(n)}
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)

    def enc(v, parent):
        return "(" + "".join(sorted(enc(c, v) for c in adj[v] if c != parent)) + ")"
    return min(enc(r, -1) for r in range(n))


def unlabelled_trees(n):
    seen = {}
    for e in prufer_trees(n):
        c = canon(n, e)
        if c not in seen:
            seen[c] = e
    return list(seen.values())


def edge_generators(n, edges):
    gens = set()
    for a, b in edges:
        for pa in range(4):
            for pb in range(4):
                if pa == 0 and pb == 0:
                    continue
                x = z = 0
                for site, p in ((a, pa), (b, pb)):
                    if p in (1, 2):
                        x |= 1 << site
                    if p in (2, 3):
                        z |= 1 << site
                gens.add(x | (z << n))
    return gens


def closure_size(n, gens):
    mask = (1 << n) - 1
    parity = np.array([bin(v).count("1") & 1 for v in range(1 << n)], dtype=np.uint8)
    member = np.zeros(1 << (2 * n), dtype=bool)
    members = np.zeros(1 << (2 * n), dtype=np.int64)
    cnt = 0
    queue = []
    for g in gens:
        if not member[g]:
            member[g] = True
            members[cnt] = g
            cnt += 1
            queue.append(g)
    qi = 0
    while qi < len(queue):
        p = queue[qi]
        qi += 1
        xp, zp = p & mask, p >> n
        cur = members[:cnt]
        xq, zq = cur & mask, cur >> n
        anti = parity[(xp & zq) ^ (zp & xq)].astype(bool)
        prods = np.unique(cur[anti] ^ p)
        new = prods[~member[prods]]
        if new.size:
            member[new] = True
            members[cnt:cnt + new.size] = new
            cnt += new.size
            queue.extend(int(v) for v in new)
    return cnt


def components(n, edges):
    parent = list(range(n))

    def find(v):
        while parent[v] != v:
            parent[v] = parent[parent[v]]
            v = parent[v]
        return v
    for a, b in edges:
        parent[find(a)] = find(b)
    comp = {}
    for v in range(n):
        comp.setdefault(find(v), []).append(v)
    return [len(c) for c in comp.values()]


expected_counts = {3: 1, 4: 2, 5: 3, 6: 6, 7: 11}
for n in range(3, 8):
    trees = unlabelled_trees(n)
    sizes = [closure_size(n, edge_generators(n, t)) for t in trees]
    check(f"G n = {n}: {len(trees)} unlabelled trees, every closure = {4 ** n - 1}",
          len(trees) == expected_counts[n] and all(s == 4 ** n - 1 for s in sizes))
    cc_ok = True
    for t in trees:
        for k in range(len(t)):
            forest = t[:k] + t[k + 1:]
            exp = sum(4 ** c - 1 for c in components(n, forest) if c >= 2)
            if closure_size(n, edge_generators(n, forest)) != exp:
                cc_ok = False
    check(f"G n = {n} countercontrol: every one-edge-deleted forest closes at the sum over its components", cc_ok)

npass = sum(1 for _, c in checks if c)
print(f"review_pass2: {npass}/{len(checks)} checks pass")
sys.exit(0 if npass == len(checks) else 1)
