"""Thread C — exact controls for the update-rule source audit.

Exact arithmetic only (fractions.Fraction, sympy rationals). No floating point.

Part A  square gbit, maximal sharp test e = (t+x)/2 whose certain face is an edge:
        ideal branch / measure-and-prepare branch / selector-forced branch.
Part B  positive controls: classical trit (coarse and fine effects), and the
        non-uniqueness countercontrol for the selector query.
Part C  the corpus's own classical update (Bayesian conditioning) on the
        coin-and-die model of Main.md:178-196 / ch01:133-151, and the card
        table of ch01:271-280 (peek with and without re-burn).

A branch of a binary test with effect e is a linear map T on the state cone with
  (N) normalisation   u(T w) = e(w)            (u = unit effect)
  (P) positivity      T(cone) <= cone
Ideal on the certain face F_e = {w in Omega : e(w) = 1}: T w = w for w in F_e.
State-independent (SI): T w = e(w) * w0 for a fixed state w0.
"""
from fractions import Fraction as Fr
from itertools import product
import sympy as sp

# ---------------------------------------------------------------- utilities

def fm_feasible_and_bounds(G, h, nvars):
    """Fourier-Motzkin over Fractions for {w : G w <= h}.
    Returns (feasible, [(lo, hi) for each var]) with lo/hi exact or None (unbounded)."""
    def eliminate(rows, j):
        pos, neg, zero = [], [], []
        for a, b in rows:
            if a[j] > 0:
                pos.append((a, b))
            elif a[j] < 0:
                neg.append((a, b))
            else:
                zero.append((a, b))
        out = list(zero)
        for (ap, bp) in pos:
            for (an, bn) in neg:
                lp, ln = -an[j], ap[j]
                a = [lp * ap[k] + ln * an[k] for k in range(len(ap))]
                b = lp * bp + ln * bn
                out.append((a, b))
        return out

    rows = [([Fr(x) for x in g], Fr(b)) for g, b in zip(G, h)]
    # feasibility: eliminate all variables
    r = rows
    for j in range(nvars):
        r = eliminate(r, j)
    feasible = all(b >= 0 for a, b in r)  # all a are zero now
    bounds = []
    if feasible:
        for i in range(nvars):
            r = rows
            for j in range(nvars):
                if j != i:
                    r = eliminate(r, j)
            lo, hi = None, None
            for a, b in r:
                if a[i] > 0:
                    v = b / a[i]
                    hi = v if hi is None else min(hi, v)
                elif a[i] < 0:
                    v = b / a[i]
                    lo = v if lo is None else max(lo, v)
            bounds.append((lo, hi))
    return feasible, bounds


def branch_query(rays, cone_ineqs, unit, e, eq_maps, label):
    """Unknown 3x3 (or n x n) T. eq_maps: list of (input vector, required output vector).
    Normalisation u(T w) = e(w) is imposed on a basis. Positivity: T r in cone for each ray.
    Returns (feasible, free-parameter bounds, parametrised T)."""
    n = len(unit)
    Ts = sp.Matrix(n, n, lambda i, j: sp.Symbol(f"T{i}{j}"))
    eqs = []
    U = sp.Matrix([unit])
    E = sp.Matrix([e])
    eqs += list(U * Ts - E)                      # (N) on all of R^n
    for v, w in eq_maps:
        eqs += list(Ts * sp.Matrix(v) - sp.Matrix(w))
    syms = list(Ts)
    sol = sp.linsolve(eqs, syms)
    if sol == sp.EmptySet:
        print(f"  [{label}] equalities inconsistent")
        return False, None, None
    (tup,) = list(sol)
    Tpar = sp.Matrix(n, n, list(tup))
    free = sorted(Tpar.free_symbols, key=lambda s: s.name)
    G, h = [], []
    for r in rays:
        img = Tpar * sp.Matrix(r)
        for c in cone_ineqs:                      # c . img >= 0  ->  -c.img <= 0
            expr = sp.expand(-(sp.Matrix([c]) * img)[0])
            coeffs = [Fr(str(expr.coeff(s))) for s in free]
            const = expr.subs({s: 0 for s in free})
            G.append(coeffs)
            h.append(-Fr(str(const)))
    if not free:
        ok = all(hh >= 0 for hh in h)
        return ok, [], Tpar
    feas, bounds = fm_feasible_and_bounds(G, h, len(free))
    return feas, list(zip(free, bounds)) if feas else None, Tpar


def in_cone(v, cone_ineqs):
    return all(sum(Fr(c[i]) * Fr(v[i]) for i in range(len(v))) >= 0 for c in cone_ineqs)


def apply(M, v):
    return [sum(Fr(M[i][j]) * Fr(v[j]) for j in range(len(v))) for i in range(len(M))]

# ---------------------------------------------------------------- Part A

print("PART A — square gbit (homogeneous coords (t,x,y); state iff |x|,|y| <= t = 1)")
SQ_RAYS = [(1, 1, 1), (1, 1, -1), (1, -1, 1), (1, -1, -1)]
SQ_CONE = [(1, -1, 0), (1, 1, 0), (1, 0, -1), (1, 0, 1)]   # t-x, t+x, t-y, t+y >= 0
u = (1, 0, 0)
e = (Fr(1, 2), Fr(1, 2), 0)
ue = tuple(Fr(a) - Fr(b) for a, b in zip(u, e))

def val(f, v):
    return sum(Fr(a) * Fr(b) for a, b in zip(f, v))

# e is an effect and the test (e, u-e) is maximal: each vanishes on two rays spanning a plane
ev = [val(e, r) for r in SQ_RAYS]
print("  e on vertices:", ev, "| u-e on vertices:", [val(ue, r) for r in SQ_RAYS])
assert all(0 <= a <= 1 for a in ev)
zero_e = [r for r in SQ_RAYS if val(e, r) == 0]
zero_ue = [r for r in SQ_RAYS if val(ue, r) == 0]
rk_e = sp.Matrix(zero_e).rank()
rk_ue = sp.Matrix(zero_ue).rank()
print(f"  rank of rays where e=0: {rk_e}; where u-e=0: {rk_ue}  (2 = extreme ray of the 3-d dual cone)")
assert rk_e == 2 and rk_ue == 2
F_e = [r for r in SQ_RAYS if val(e, r) == 1]
print("  certain face F_e vertices:", F_e, "-> an edge (two vertices)")
assert len(F_e) == 2

# A1: ideal branch (T fixes F_e pointwise)
feas, bnds, _ = branch_query(SQ_RAYS, SQ_CONE, u, e, [(v, v) for v in F_e], "A1 ideal")
print("  A1 ideal branch for e exists?", feas)
assert feas is False

# A2: SI measure-and-prepare onto v1 = (1,1,1): T = v1 e^T
v1 = (1, 1, 1)
T_mp = [[Fr(v1[i]) * Fr(e[j]) for j in range(3)] for i in range(3)]
pos = all(in_cone(apply(T_mp, r), SQ_CONE) for r in SQ_RAYS)
norm = all(val(u, apply(T_mp, r)) == val(e, r) for r in SQ_RAYS)
repeat = val(e, v1) == 1
v3 = (1, 1, -1)
nonideal = apply(T_mp, v3) != [Fr(c) for c in v3]
print(f"  A2 measure-and-prepare T = v1 e^T: positive={pos} normalised={norm} "
      f"repeatable={repeat} disturbs certain state (1,1,-1)={nonideal}")
assert pos and norm and repeat and nonideal

# A3: selector query (analogue of BranchSelector.cp_rankOneSelector_iff_luders):
#     T v1 = v1, T v2 = 0 on the frame {v1, v2} = {(1,1,1), (1,-1,-1)}
v2 = (1, -1, -1)
feas, bnds, Tpar = branch_query(SQ_RAYS, SQ_CONE, u, e, [(v1, v1), (v2, (0, 0, 0))], "A3 selector")
print("  A3 selector-constrained branch exists?", feas, "| free-parameter bounds:", bnds)
assert feas
unique = all(lo is not None and lo == hi for _, (lo, hi) in bnds)
print("  A3 unique?", unique)
assert unique
Tfix = Tpar.subs({s: sp.Rational(lo.numerator, lo.denominator) for s, (lo, hi) in bnds})
print("  A3 forced branch:", Tfix.tolist(), "== v1 e^T ?",
      Tfix == sp.Matrix(3, 3, [sp.Rational(x.numerator, x.denominator) for row in T_mp for x in row]))
assert Tfix == sp.Matrix(3, 3, [sp.Rational(x.numerator, x.denominator) for row in T_mp for x in row])

# ---------------------------------------------------------------- Part B

print("\nPART B — positive controls (classical trit; cone = nonnegative orthant)")
TR_RAYS = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
TR_CONE = TR_RAYS
uT = (1, 1, 1)
e_coarse = (1, 1, 0)
e_fine = (1, 0, 0)

feas, bnds, Tpar = branch_query(TR_RAYS, TR_CONE, uT, e_coarse,
                                [((1, 0, 0), (1, 0, 0)), ((0, 1, 0), (0, 1, 0))], "B1 trit coarse ideal")
print("  B1 trit coarse e=d0+d1: ideal branch exists?", feas, "| bounds:", bnds)
assert feas
# ideal branch on the trit coarse effect: post-states of d0, d1 differ -> not SI
print("     ideal branch maps d0->d0, d1->d1: post-state depends on input within the outcome (not SI)")

feas, bnds, Tpar = branch_query(TR_RAYS, TR_CONE, uT, e_fine, [((1, 0, 0), (1, 0, 0))], "B2 trit fine ideal")
print("  B2 trit fine e=d0: ideal branch exists?", feas, "| bounds:", bnds)
assert feas
unique = all(lo is not None and lo == hi for _, (lo, hi) in bnds)
print("     unique?", unique, "-> forced T =", Tpar.subs({s: 0 for s, _ in bnds}).tolist(),
      "(SI: every input with e>0 goes to d0)")

# B3 countercontrol for A3's uniqueness: selector query on the trit coarse effect with frame {d0, d2}
feas, bnds, Tpar = branch_query(TR_RAYS, TR_CONE, uT, e_coarse,
                                [((1, 0, 0), (1, 0, 0)), ((0, 0, 1), (0, 0, 0))], "B3 trit selector")
unique = all(lo is not None and lo == hi for _, (lo, hi) in bnds)
print("  B3 trit coarse selector T d0=d0, T d2=0: feasible?", feas, "unique?", unique, "| bounds:", bnds)
assert feas and not unique

# B4 disk (rebit), by hand and exact: F_e for e=(t+x)/2 on x^2+y^2<=1 at x=1 forces y=0
x, y = sp.symbols("x y", real=True)
sol = sp.solve([sp.Eq(x, 1), sp.Eq(x**2 + y**2, 1)], [x, y], dict=True)
print("  B4 disk: boundary points with e=1:", sol, "-> F_e is the single state (1,1,0);",
      "T w = e(w)(1,1,0) is positive (e>=0 on states), ideal and SI")

# ---------------------------------------------------------------- Part C

print("\nPART C — corpus's classical update: Bayesian conditioning on a visible outcome")
H = range(1, 7)
def sigma(s):
    xx, hh = s
    if hh in (1, 2):
        return (1 - xx, hh)
    swap = {3: 4, 4: 3, 5: 6, 6: 5}
    return (xx, swap[hh])

states = [(xx, hh) for xx in (0, 1) for hh in H]
assert sorted(map(sigma, states)) == sorted(states)          # bijection
assert all(sigma(sigma(s)) == s for s in states)             # sigma^2 = id

def joint_after_step(x0):
    """law of (X1, H1) for root x0 and uniform die"""
    law = {}
    for hh in H:
        s1 = sigma((x0, hh))
        law[s1] = law.get(s1, Fr(0)) + Fr(1, 6)
    return law

def condition(law, xobs):
    z = sum(p for (xx, hh), p in law.items() if xx == xobs)
    return {s: p / z for s, p in law.items() if s[0] == xobs}

def next_vis_law(law):
    out = {0: Fr(0), 1: Fr(0)}
    for s, p in law.items():
        out[sigma(s)[0]] += p
    return out

def tv(a, b):
    keys = set(a) | set(b)
    return Fr(1, 2) * sum(abs(a.get(k, Fr(0)) - b.get(k, Fr(0))) for k in keys)

post0 = condition(joint_after_step(0), 1)
post1 = condition(joint_after_step(1), 1)
n0, n1 = next_vis_law(post0), next_vis_law(post1)
print("  C1 post-states after the certain visible outcome X1=1:")
print("     root x0=0:", post0, "next law", n0)
print("     root x0=1:", post1, "next law", n1)
print("     TV(next laws) =", tv(n0, n1), "(Main.md:194: P(x2=0|x1=1,x0=0) = 1)")
assert n0[0] == 1 and n1[0] == 0 and tv(n0, n1) == 1
mix = {}
for x0 in (0, 1):
    for s, p in joint_after_step(x0).items():
        mix[s] = mix.get(s, Fr(0)) + p / 2
print("     unrooted P(x2=0|x1=1) =", next_vis_law(condition(mix, 1))[0], "(Main.md:194: 1/3)")
assert next_vis_law(condition(mix, 1))[0] == Fr(1, 3)

# re-burn (state-independent) update: after reading X=xobs, replace the die by a uniform die
def reburn(law, xobs):
    return {(xobs, hh): Fr(1, 6) for hh in H}
r0, r1 = reburn(post0, 1), reburn(post1, 1)
print("  C2 re-burn update: post-states equal?", r0 == r1, "; next law", next_vis_law(r0),
      "-> history gap at this step killed")
assert r0 == r1
d13 = {(1, 3): Fr(1)}
print("     re-burn is not ideal: delta_(1,3) is certain for X=1 but is sent to",
      "uniform die (changed:", reburn(d13, 1) != d13, ")")
assert reburn(d13, 1) != d13
print("     conditioning is ideal: condition(delta_(1,3), 1) == delta_(1,3):", condition(d13, 1) == d13)
assert condition(d13, 1) == d13

print("\n  C3 card table (ch01:271-280): hole c, burn b in {R,B} uniform; shuffle = swap")
cards = ("R", "B")
def protocol(n_shuffles, peek=None):
    """peek in {None,'passive','reburn-uniform','reburn-fixed'} after first shuffle"""
    tot = Fr(0)
    cases = 0
    for c, b, r in product(cards, cards, cards):  # r = fresh burn card if needed
        w = Fr(1, 8)
        hole, burn = c, b
        for k in range(n_shuffles):
            hole, burn = burn, hole
            if k == 0 and peek == "reburn-uniform":
                burn = r
            if k == 0 and peek == "reburn-fixed":
                burn = "R"
        cases += 1
        tot += w * (hole == c)
    return tot
p1 = protocol(1)
p2 = protocol(2)
# chained through the unobserved middle: one-street matrix squared
T1 = [[protocol(1), 1 - protocol(1)], [1 - protocol(1), protocol(1)]]
chained = T1[0][0] * T1[0][0] + T1[0][1] * T1[1][0]
pp = protocol(2, "passive")
pr = protocol(2, "reburn-uniform")
pf = protocol(2, "reburn-fixed")
print(f"     one shuffle {p1}; two shuffles {p2}; chained {chained}; "
      f"passive peek {pp}; peek+re-burn(uniform) {pr}; peek+re-burn(fixed card) {pf}")
assert (p1, p2, chained, pr, pf) == (Fr(1, 2), 1, Fr(1, 2), Fr(1, 2), Fr(1, 2)) and pp == 1

print("\nALL ASSERTIONS PASSED")
