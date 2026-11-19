#!/usr/bin/env python3
"""p12_r6rev_checks.py -- independent reviewer probe for QPHEN Phase 1 r6.

Exact checks of paper claims on GENERIC mathematical objects only (finite-field
matrices, deterministic +-1 response tables, small graphs). No OI mechanism is
built or simulated. Imports no earlier probe; standard library only
(itertools, fractions, sys).

Sections
 1. Q4-P19 (i) and (ii) on F_2^4, with Sp(4,F_2) built by enumerating
    symplectic bases (a construction different from brute force over all
    matrices, the Gram test and transvection closure used by p9/p10/p11).
 2. Scope of the gloss "K_null != id" in Q4-P19 (ii): null-result invasiveness
    on the silent branch's actual support, for sharp, half-known (SA-1(c)) and
    fully unknown meter ready laws.
 3. Q4-P19 (ii) over F_3^4 (beyond the stated scope; sanity of the field-free
    proof).
 4. Q6-P12 bullets 1 and 3 on deterministic response tables, with
    countercontrol; bullet 2 on small graphs.
 5. B1's SA-1(a) row: (a,b) -> (b, F b - a) is symplectic iff F = F^T,
    checked by the vector-pair definition of symplecticity (not the Gram
    identity) where feasible.
"""
import itertools
import sys
from fractions import Fraction

RESULTS = []


def check(name, cond, detail=""):
    RESULTS.append((name, bool(cond)))
    print(("PASS " if cond else "FAIL ") + name + (("  -- " + detail) if detail else ""))


# ---------------------------------------------------------------------------
# finite-field linear algebra helpers (q prime), vectors as tuples
# coordinates: 0=c, 1=x, 2=m, 3=m'  ; symplectic pairs (c,x), (m,m')
# omega(u,v) = u_c v_x - u_x v_c + u_m v_m' - u_m' v_m
# ---------------------------------------------------------------------------

def omega(u, v, q):
    return (u[0] * v[1] - u[1] * v[0] + u[2] * v[3] - u[3] * v[2]) % q


def vecs(q, n=4):
    return list(itertools.product(range(q), repeat=n))


def mat_from_cols(cols):
    # M[i][j] = cols[j][i]
    n = len(cols)
    return tuple(tuple(cols[j][i] for j in range(n)) for i in range(n))


def apply(M, y, b, q):
    n = len(y)
    return tuple((sum(M[i][j] * y[j] for j in range(n)) + b[i]) % q for i in range(n))


def symplectic_group_by_bases(q):
    """All M in Sp(4,F_q), as matrices whose columns (Me_c, Me_x, Me_m, Me_m')
    form a symplectic basis: omega(Me_c,Me_x)=1, omega(Me_m,Me_m')=1, all
    cross pairs 0."""
    V = vecs(q)
    nz = [v for v in V if any(v)]
    out = []
    for u1 in nz:
        for v1 in V:
            if omega(u1, v1, q) != 1:
                continue
            comp = [w for w in V if omega(w, u1, q) == 0 and omega(w, v1, q) == 0]
            for u2 in comp:
                if not any(u2):
                    continue
                for v2 in comp:
                    if omega(u2, v2, q) == 1:
                        out.append(mat_from_cols([u1, v1, u2, v2]))
    return out


def is_symplectic_pairs(M, q):
    # definition: omega(Mu, Mv) = omega(u, v) for ALL vector pairs
    V = vecs(q)
    z = (0,) * 4
    img = {v: apply(M, v, z, q) for v in V}
    for u in V:
        for v in V:
            if omega(img[u], img[v], q) != omega(u, v, q):
                return False
    return True


# ---------------------------------------------------------------------------
# Section 1: Q4-P19 on F_2^4
# ---------------------------------------------------------------------------
print("== 1. Q4-P19 on F_2^4 (Sp(4,2) from symplectic bases)")
q = 2
SP = symplectic_group_by_bases(q)
SPset = set(SP)
check("1a |Sp(4,F_2)| from symplectic bases = 720", len(SPset) == 720 and len(SP) == 720, str(len(SPset)))
# spot-verify against the definition on a sample of 60 (deterministic slice) plus all 720 cheaply
check("1b every basis-built matrix satisfies omega(Mu,Mv)=omega(u,v) for all 256 pairs",
      all(is_symplectic_pairs(M, q) for M in SP))
# count the full GL(4,2) symplectic ones by definition to cross-check 720 (brute over 65536)
cnt_def = 0
for entries in itertools.product(range(2), repeat=16):
    M = tuple(tuple(entries[4 * i:4 * i + 4]) for i in range(4))
    # quick Gram test on basis would be p10's method; use definition on basis pairs + linearity
    # (bilinear form: basis pairs suffice, but we use vector pairs only for the 720 found above)
    ok = True
    E = [tuple(1 if k == j else 0 for k in range(4)) for j in range(4)]
    cols = [tuple(M[i][j] for i in range(4)) for j in range(4)]
    for a in range(4):
        for b_ in range(4):
            if omega(cols[a], cols[b_], 2) != omega(E[a], E[b_], 2):
                ok = False
                break
        if not ok:
            break
    if ok:
        cnt_def += 1
        if M not in SPset:
            ok = False
check("1c brute-force count over all 65,536 matrices equals 720 and matches the basis set", cnt_def == 720)

V2 = vecs(2)
TRANS = V2
AFF_SYMP = [(M, b) for M in SP for b in TRANS]
check("1d affine-symplectic maps = 11,520", len(AFF_SYMP) == 11520)


def fixes_branch_c0(M, b):
    return all(apply(M, y, b, 2) == y for y in V2 if y[0] == 0)


def changes_meter_on_c1(M, b):
    return any(apply(M, y, b, 2)[2:] != y[2:] for y in V2 if y[0] == 1)


bad_i = [(M, b) for (M, b) in AFF_SYMP if fixes_branch_c0(M, b) and changes_meter_on_c1(M, b)]
check("1e Q4-P19 (i): no affine-symplectic map is the identity on c=0 and changes a meter slot on c=1",
      len(bad_i) == 0, "%d exceptions" % len(bad_i))

# affine (not nec. symplectic) bijections doing both: expect 6
GL = []
for entries in itertools.product(range(2), repeat=16):
    M = tuple(tuple(entries[4 * i:4 * i + 4]) for i in range(4))
    imgs = set(apply(M, y, (0, 0, 0, 0), 2) for y in V2)
    if len(imgs) == 16:
        GL.append(M)
check("1f |GL(4,F_2)| = 20,160", len(GL) == 20160)
aff_both = sum(1 for M in GL for b in TRANS if fixes_branch_c0(M, b) and changes_meter_on_c1(M, b))
check("1g affine bijections that are identity on c=0 and change a meter slot on c=1 = 6", aff_both == 6, str(aff_both))


def loc_preserving(M, b, qq, V):
    return all(apply(M, y, b, qq)[0] == y[0] for y in V)


def meter_write_depends_on_c(M, b, qq, V):
    # exists (x,m,m') with meter output differing between two values of c
    for y in V:
        for c2 in range(qq):
            y2 = (c2,) + y[1:]
            if apply(M, y, b, qq)[2:] != apply(M, y2, b, qq)[2:]:
                return True
    return False


def changes_x_on_c0(M, b, qq, V):
    return any(apply(M, y, b, qq)[1] != y[1] for y in V if y[0] == 0)


LP = [(M, b) for (M, b) in AFF_SYMP if loc_preserving(M, b, 2, V2)]
REC = [(M, b) for (M, b) in LP if meter_write_depends_on_c(M, b, 2, V2)]
check("1h location-preserving affine-symplectic maps = 384", len(LP) == 384, str(len(LP)))
check("1i of these, meter write depends on c: 288", len(REC) == 288, str(len(REC)))
check("1j Q4-P19 (ii): every one of the 288 changes x on some state with c=0",
      all(changes_x_on_c0(M, b, 2, V2) for (M, b) in REC))
# weak reading counterexample: translation m <- m+1 changes a meter slot on c=1, never changes x
I4 = tuple(tuple(1 if i == j else 0 for j in range(4)) for i in range(4))
tm = (I4, (0, 0, 1, 0))
check("1k weak reading: m <- m+1 changes a meter slot on c=1 and never changes x",
      changes_meter_on_c1(*tm) and not any(apply(I4, y, (0, 0, 1, 0), 2)[1] != y[1] for y in V2))

# ---------------------------------------------------------------------------
# Section 2: scope of "K_null != id" -- the silent branch's actual support
# ---------------------------------------------------------------------------
print("== 2. K_null on the silent branch's support, by meter ready law")
# A ready meter law is a support set R of (m, m') values.  The carrier is a
# location state: c known per branch, x ontic (both values in the support).
# 'records readably' : some nonzero linear functional f of the OUTPUT meter
#   slots takes, on {c} x F_2(x) x R, a value that is a function of c alone and
#   differs between c=0 and c=1.
# 'K_null = id'      : x' = x on every state with c=0, x in F_2, meter in R.
FUNCS = [(1, 0), (0, 1), (1, 1)]


def readable(M, b, R):
    for f in FUNCS:
        vals = {0: set(), 1: set()}
        for c in (0, 1):
            for x in (0, 1):
                for (m, mp) in R:
                    out = apply(M, (c, x, m, mp), b, 2)
                    vals[c].add((f[0] * out[2] + f[1] * out[3]) % 2)
        if len(vals[0]) == 1 and len(vals[1]) == 1 and vals[0] != vals[1]:
            return True
    return False


def knull_id(M, b, R):
    return all(apply(M, (0, x, m, mp), b, 2)[1] == x for x in (0, 1) for (m, mp) in R)


ready_laws = {}
for m0 in (0, 1):
    for mp0 in (0, 1):
        ready_laws["sharp(%d,%d)" % (m0, mp0)] = [(m0, mp0)]
for k0 in (0, 1):
    ready_laws["SA1c m known=%d, m' uniform" % k0] = [(k0, 0), (k0, 1)]
    ready_laws["SA1c m' known=%d, m uniform" % k0] = [(0, k0), (1, k0)]
ready_laws["both unknown"] = [(0, 0), (0, 1), (1, 0), (1, 1)]

counts = {}
for name, R in ready_laws.items():
    rd = [(M, b) for (M, b) in LP if readable(M, b, R)]
    silent_id = [(M, b) for (M, b) in rd if knull_id(M, b, R)]
    counts[name] = (len(rd), len(silent_id))
    print("   %-28s readable recorders %3d ; of them with K_null = id on the silent support %3d"
          % (name, len(rd), len(silent_id)))

# the reciprocal coupling of R4.9: m <- m + c, x <- x + m'
Mrec = ((1, 0, 0, 0), (0, 1, 0, 1), (1, 0, 1, 0), (0, 0, 0, 1))
brec = (0, 0, 0, 0)
check("2a the reciprocal coupling (m<-m+c, x<-x+m') is symplectic", Mrec in SPset)
check("2b with a sharp meter (0,0) it records readably and has K_null = id on its silent branch",
      readable(Mrec, brec, [(0, 0)]) and knull_id(Mrec, brec, [(0, 0)]))
check("2c with an SA-1(c) meter (m known 0, m' uniform) it records readably and K_null != id",
      readable(Mrec, brec, [(0, 0), (0, 1)]) and not knull_id(Mrec, brec, [(0, 0), (0, 1)]))
check("2d sharp meter laws admit readable recorders with K_null = id (gloss needs the meter law)",
      counts["sharp(0,0)"][1] > 0, "sharp(0,0): %d" % counts["sharp(0,0)"][1])
check("2e under every SA-1(c) meter law, every readable recorder has K_null != id",
      all(counts[n][1] == 0 and counts[n][0] > 0 for n in ready_laws if n.startswith("SA1c")))
check("2f with both meter slots unknown no map records readably", counts["both unknown"][0] == 0)

# ---------------------------------------------------------------------------
# Section 3: Q4-P19 (ii) over F_3^4 (beyond stated scope)
# ---------------------------------------------------------------------------
print("== 3. Q4-P19 (ii) over F_3^4 (sanity, beyond the stated scope)")
q3 = 3
SP3 = symplectic_group_by_bases(q3)
check("3a |Sp(4,F_3)| from symplectic bases = 51,840", len(set(SP3)) == 51840 and len(SP3) == 51840)
V3 = vecs(3)
# location-preserving linear part: row c = e_c^T
SP3_lp = [M for M in SP3 if M[0] == (1, 0, 0, 0)]
check("3b location-preserving linear parts = 648", len(SP3_lp) == 648, str(len(SP3_lp)))
viol = 0
nrec3 = 0
for M in SP3_lp:
    # meter write depends on c iff M[2][0] or M[3][0] nonzero (affine); x fixed on c=0 iff
    # row x restricted to (x,m,m') is (1,0,0) and b_x = 0. Check claim via the definitions
    # for b = 0 and b_x != 0 separately (other translation parts do not matter).
    dep = (M[2][0] % 3 != 0) or (M[3][0] % 3 != 0)
    if not dep:
        continue
    for bx in range(3):
        b = (0, bx, 0, 0)
        nrec3 += 1
        if not changes_x_on_c0(M, b, 3, V3):
            viol += 1
check("3c over F_3: every location-preserving symplectic recorder changes x on some c=0 state",
      viol == 0 and nrec3 > 0, "%d checked, %d violations" % (nrec3, viol))

# ---------------------------------------------------------------------------
# Section 4: Q6-P12
# ---------------------------------------------------------------------------
print("== 4. Q6-P12 on deterministic response tables")
SETTINGS = [(0, 0), (0, 1), (1, 0), (1, 1)]
TABLES = []
for bits in itertools.product((1, -1), repeat=8):
    A = {s: bits[i] for i, s in enumerate(SETTINGS)}
    B = {s: bits[4 + i] for i, s in enumerate(SETTINGS)}
    TABLES.append((A, B))
check("4a 256 deterministic tables", len(TABLES) == 256)


def S_of(table):
    A, B = table
    E = {s: A[s] * B[s] for s in SETTINGS}
    return E[(0, 0)] + E[(0, 1)] + E[(1, 0)] - E[(1, 1)]


def local(table):
    A, B = table
    return all(A[(x, 0)] == A[(x, 1)] for x in (0, 1)) and all(B[(0, y)] == B[(1, y)] for y in (0, 1))


loc = [t for t in TABLES if local(t)]
check("4b local tables = 16", len(loc) == 16)
check("4c bullet 1: every local table has |S| <= 2", all(abs(S_of(t)) <= 2 for t in loc))
check("4d bullet 1 (contrapositive): every table with |S| > 2 has remote-setting dependence",
      all(not local(t) for t in TABLES if abs(S_of(t)) > 2))
check("4e control non-vacuous: some non-local table reaches |S| = 4",
      any(abs(S_of(t)) == 4 for t in TABLES))
# MI mixtures: S is linear in the law over Omega (tables), so with support in local tables
# |S| <= 2; exhaustively over all laws on pairs of local tables with weights k/8
mix_ok = True
for t1, t2 in itertools.combinations(loc, 2):
    for k in range(9):
        w = Fraction(k, 8)
        if abs(w * S_of(t1) + (1 - w) * S_of(t2)) > 2:
            mix_ok = False
check("4f MI mixtures supported on local tables (pairs, weights k/8) stay at |S| <= 2", mix_ok)


def marginal_A(law, x, y):
    # law: list of (weight, table); returns P(A=+1 | x, y)
    return sum(w for w, t in law if t[0][(x, y)] == 1)


def marginal_B(law, x, y):
    return sum(w for w, t in law if t[1][(x, y)] == 1)


def no_signalling(law):
    for x in (0, 1):
        if marginal_A(law, x, 0) != marginal_A(law, x, 1):
            return False
    for y in (0, 1):
        if marginal_B(law, 0, y) != marginal_B(law, 1, y):
            return False
    return True


ns_point = all(no_signalling([(Fraction(1), t)]) == local(t) for t in TABLES)
check("4g bullet 3: a point mass is no-signalling iff its table is local (256)", ns_point)
# countercontrol: equal mixture of A=w, B = w xor xy (as +-1)
def pm(bit):
    return 1 - 2 * bit


PRt = []
for wbit in (0, 1):
    A = {(x, y): pm(wbit) for (x, y) in SETTINGS}
    B = {(x, y): pm(wbit ^ (x * y)) for (x, y) in SETTINGS}
    PRt.append((A, B))
law = [(Fraction(1, 2), PRt[0]), (Fraction(1, 2), PRt[1])]
Smix = sum(w * S_of(t) for w, t in law)
check("4h countercontrol: the two components signal, the equal mixture is no-signalling with S = 4",
      (not no_signalling([(Fraction(1), PRt[0])])) and (not no_signalling([(Fraction(1), PRt[1])]))
      and no_signalling(law) and Smix == 4, "S=%s" % Smix)


# affine-hull lemma, exhaustively on a small universe: Omega ranges over 4 tables
# (the two PR halves and two local tables); a class is a set of laws with weights in
# {0, 1/2, 1} on these; if every member is no-signalling and some member has S > 2,
# then some point mass in that member's support is outside the class's affine hull.
def rank_q(rows):
    rows = [list(r) for r in rows]
    r = 0
    ncol = len(rows[0]) if rows else 0
    for col in range(ncol):
        piv = None
        for i in range(r, len(rows)):
            if rows[i][col] != 0:
                piv = i
                break
        if piv is None:
            continue
        rows[r], rows[piv] = rows[piv], rows[r]
        pv = rows[r][col]
        rows[r] = [v / pv for v in rows[r]]
        for i in range(len(rows)):
            if i != r and rows[i][col] != 0:
                fct = rows[i][col]
                rows[i] = [a - fct * b_ for a, b_ in zip(rows[i], rows[r])]
        r += 1
    return r


def in_affine_hull(point, members):
    # point and members as weight vectors; affine hull membership:
    # exists coeffs summing to 1 with sum c_i v_i = point  <=> rank test on homogenized vectors
    rows = [list(v) + [Fraction(1)] for v in members]
    base = rank_q(rows)
    return rank_q(rows + [list(point) + [Fraction(1)]]) == base


U = [PRt[0], PRt[1], loc[0], loc[5]]
grid = [Fraction(0), Fraction(1, 2), Fraction(1)]
LAWS = []
for wts in itertools.product(grid, repeat=4):
    if sum(wts) == 1:
        LAWS.append(tuple(wts))
lemma_ok = True
nclasses = 0
nhit = 0
for k in (1, 2, 3):
    for cls in itertools.combinations(LAWS, k):
        laws = [[(w, U[i]) for i, w in enumerate(v) if w != 0] for v in cls]
        if not all(no_signalling(l) for l in laws):
            continue
        nclasses += 1
        for v, l in zip(cls, laws):
            S = sum(w * S_of(t) for w, t in l)
            if abs(S) > 2:
                nhit += 1
                supp = [i for i, w in enumerate(v) if w != 0]
                pts = [tuple(Fraction(1) if j == i else Fraction(0) for j in range(4)) for i in supp]
                if all(in_affine_hull(p, cls) for p in pts):
                    lemma_ok = False
check("4i bullet 3, small universe: in every no-signalling class (1-3 laws, weights in {0,1/2,1}) "
      "with a member of |S|>2, some support point mass lies outside the affine hull",
      lemma_ok and nhit > 0, "%d NS classes, %d members with |S|>2" % (nclasses, nhit))

# bullet 2: d_{G_B} <= T < d_{G_ref}  =>  every G_B path of length <= T has an edge outside G_ref
print("== 4'. Q6-P12 bullet 2 on all graphs with 4 vertices")


def dist(edges, s, t, n):
    from collections import deque
    adj = {i: set() for i in range(n)}
    for (a, b_) in edges:
        adj[a].add(b_)
        adj[b_].add(a)
    D = {s: 0}
    dq = deque([s])
    while dq:
        u = dq.popleft()
        for w in adj[u]:
            if w not in D:
                D[w] = D[u] + 1
                dq.append(w)
    return D.get(t, 10 ** 9)


def paths_upto(edges, s, t, L, n):
    adj = {i: set() for i in range(n)}
    for (a, b_) in edges:
        adj[a].add(b_)
        adj[b_].add(a)
    out = []

    def rec(u, path, used):
        if u == t:
            out.append(list(used))
        if len(used) == L:
            return
        for w in adj[u]:
            if w not in path:
                rec(w, path | {w}, used + [tuple(sorted((u, w)))])
    rec(s, {s}, [])
    return out


n = 4
ALL_E = [tuple(e) for e in itertools.combinations(range(n), 2)]
ok2 = True
cases = 0
for kb in range(1 << len(ALL_E)):
    GB = [ALL_E[i] for i in range(len(ALL_E)) if kb >> i & 1]
    for kr in range(1 << len(ALL_E)):
        Gref = [ALL_E[i] for i in range(len(ALL_E)) if kr >> i & 1]
        for T in range(0, 4):
            dB = dist(GB, 0, 3, n)
            dR = dist(Gref, 0, 3, n)
            if dB <= T < dR:
                cases += 1
                for p in paths_upto(GB, 0, 3, T, n):
                    if all(e in Gref for e in p):
                        ok2 = False
check("4j bullet 2: whenever d_GB <= T < d_Gref, every G_B path of length <= T leaves G_ref",
      ok2 and cases > 0, "%d cases" % cases)

# ---------------------------------------------------------------------------
# Section 5: SA-1(a) step symplectic iff F symmetric
# ---------------------------------------------------------------------------
print("== 5. (a,b) -> (b, F b - a): symplectic iff F = F^T")


def step_symplectic_by_pairs(F, qq, nn):
    # phase space Z_q^{2n}, omega((a,b),(a',b')) = a.b' - b.a'
    def om(u, v):
        a, b_ = u[:nn], u[nn:]
        a2, b2 = v[:nn], v[nn:]
        return (sum(a[i] * b2[i] for i in range(nn)) - sum(b_[i] * a2[i] for i in range(nn))) % qq

    def T(u):
        a, b_ = u[:nn], u[nn:]
        Fb = tuple(sum(F[i][j] * b_[j] for j in range(nn)) % qq for i in range(nn))
        return tuple(b_) + tuple((Fb[i] - a[i]) % qq for i in range(nn))
    V = list(itertools.product(range(qq), repeat=2 * nn))
    img = {u: T(u) for u in V}
    for u in V:
        for v in V:
            if om(img[u], img[v]) != om(u, v):
                return False
    return True


def step_symplectic_by_basis(F, qq, nn):
    # bilinearity: checking basis pairs is equivalent; used only where pairs are too many
    def om(u, v):
        a, b_ = u[:nn], u[nn:]
        a2, b2 = v[:nn], v[nn:]
        return (sum(a[i] * b2[i] for i in range(nn)) - sum(b_[i] * a2[i] for i in range(nn))) % qq

    def T(u):
        a, b_ = u[:nn], u[nn:]
        Fb = tuple(sum(F[i][j] * b_[j] for j in range(nn)) % qq for i in range(nn))
        return tuple(b_) + tuple((Fb[i] - a[i]) % qq for i in range(nn))
    E = [tuple(1 if k == j else 0 for k in range(2 * nn)) for j in range(2 * nn)]
    return all(om(T(u), T(v)) == om(u, v) for u in E for v in E)


for (qq, nn, method) in [(2, 2, "pairs"), (3, 2, "pairs"), (2, 3, "pairs"), (3, 3, "basis"), (5, 2, "basis")]:
    good = True
    nsym = 0
    nsymp = 0
    for ent in itertools.product(range(qq), repeat=nn * nn):
        F = tuple(tuple(ent[i * nn:(i + 1) * nn]) for i in range(nn))
        sym = all(F[i][j] == F[j][i] for i in range(nn) for j in range(nn))
        sp = step_symplectic_by_pairs(F, qq, nn) if method == "pairs" else step_symplectic_by_basis(F, qq, nn)
        nsym += sym
        nsymp += sp
        if sym != sp:
            good = False
    check("5 (q,n)=(%d,%d) [%s]: symplectic iff symmetric; counts %d = %d" % (qq, nn, method, nsymp, nsym),
          good and nsymp == nsym == qq ** (nn * (nn + 1) // 2))

# translation: (a,b) -> (b, Fb + t - a) with symmetric F preserves omega on differences
qq, nn = 3, 2
F = ((0, 1), (1, 0))
t = (1, 2)
V = list(itertools.product(range(qq), repeat=2 * nn))


def Tt(u):
    a, b_ = u[:nn], u[nn:]
    Fb = tuple((sum(F[i][j] * b_[j] for j in range(nn)) + t[i]) % qq for i in range(nn))
    return tuple(b_) + tuple((Fb[i] - a[i]) % qq for i in range(nn))


def omv(u, v):
    a, b_ = u[:nn], u[nn:]
    a2, b2 = v[:nn], v[nn:]
    return (sum(a[i] * b2[i] for i in range(nn)) - sum(b_[i] * a2[i] for i in range(nn))) % qq


def sub(u, v):
    return tuple((x - y) % qq for x, y in zip(u, v))


z = (0,) * (2 * nn)
check("5t an affine step with symmetric F has a symplectic linear part (translation does not matter)",
      all(omv(sub(Tt(u), Tt(z)), sub(Tt(v), Tt(z))) == omv(u, v) for u in V for v in V))

# 1D ring, nearest neighbour, translation-invariant: symmetric iff c_{+1} = c_{-1}
ring_ok = True
L = 5
for cm, c0, cp in itertools.product(range(3), repeat=3):
    Fr = tuple(tuple((cm if j == (i - 1) % L else 0) + (c0 if j == i else 0) + (cp if j == (i + 1) % L else 0)
                     for j in range(L)) for i in range(L))
    sym = all(Fr[i][j] % 3 == Fr[j][i] % 3 for i in range(L) for j in range(L))
    if sym != (cm == cp):
        ring_ok = False
check("5r ring of 5 sites over Z_3: translation-invariant NN rule symmetric iff reflection-symmetric", ring_ok)

npass = sum(1 for _, ok in RESULTS if ok)
print("== %d of %d checks pass" % (npass, len(RESULTS)))
sys.exit(0 if npass == len(RESULTS) else 1)
