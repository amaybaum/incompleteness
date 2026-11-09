"""P1 -- exact generic check (#1049 re-assessment, WIP / UNVERIFIED, model-written).

Claim checked (a paper claim about an implication, on generic functions over Z/q):
  "Uniform amplitude-scale covariance does not imply an affine rule in d >= 2."
That is: there exist local update functions f : (Z/q)^{2d} -> Z/q (the 2d nearest-neighbour
values; no centre slot) such that
  (a) f(lam*v + c*1) = lam*f(v) + 2c  for every unit lam and every c   [so every uniform
      x -> lam*x + c is an exact symmetry of x(t+1) = f(nbrs) - x(t-1)];
  (b) f is invariant under the point group acting on the 2d neighbour slots (D4 for d=2,
      O_h for d=3), i.e. isotropy;
  (c) f is NOT affine: some first difference depends on its base point.
Controls:
  - positive control (d=1, q=3, exhaustive over all 3^9 functions): (a)+(b) force f = s, linear;
  - the linear rule f = alpha*s passes (a),(b) and is reported affine;
  - the affine-offset rule f = alpha*s + 1 fails (a) at some unit lam != 1 (odd q).
This is not a proposed OI rule and adopts no premise. No OI mechanism is computed.
"""
import itertools, sys

def units(q):
    from math import gcd
    return [l for l in range(1, q) if gcd(l, q) == 1]

def legendre(z, q):
    z %= q
    if z == 0:
        return 0
    return 1 if pow(z, (q - 1) // 2, q) == 1 else -1

def is_affine(f, n, q):
    """f affine on (Z/q)^n iff f(v) - f(0) is additive."""
    f0 = f((0,) * n)
    pts = list(itertools.product(range(q), repeat=n))
    # additive check via basis decomposition: g(v) = sum v_i g(e_i)
    g = lambda v: (f(v) - f0) % q
    ge = [g(tuple(1 if j == i else 0 for j in range(n))) for i in range(n)]
    for v in pts:
        if g(v) != sum(v[i] * ge[i] for i in range(n)) % q:
            return False, v
    return True, None

def witness_base_point(f, n, q):
    """find base points w, w' and step d with f(w+d)-f(w) != f(w'+d)-f(w')."""
    pts = list(itertools.product(range(q), repeat=n))
    zero = (0,) * n
    for d in pts:
        ref = (f(d) - f(zero)) % q
        for w in pts:
            wd = tuple((a + b) % q for a, b in zip(w, d))
            if (f(wd) - f(w)) % q != ref:
                return d, w
    return None

def check_cov(f, n, q):
    pts = list(itertools.product(range(q), repeat=n))
    for lam in units(q):
        for c in range(q):
            for v in pts:
                lv = tuple((lam * a + c) % q for a in v)
                if f(lv) % q != (lam * f(v) + 2 * c) % q:
                    return False, (lam, c, v)
    return True, None

def check_iso(f, n, q, group):
    pts = list(itertools.product(range(q), repeat=n))
    for g in group:
        for v in pts:
            if f(tuple(v[g[i]] for i in range(n))) % q != f(v) % q:
                return False, (g, v)
    return True, None

def oh_group():
    # slots: 0:+x 1:-x 2:+y 3:-y 4:+z 5:-z ; slot(a,e) = 2a + (0 if e>0 else 1)
    G = []
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product([1, -1], repeat=3):
            img = [None] * 6
            for a in range(3):
                for e in (1, -1):
                    src = 2 * a + (0 if e > 0 else 1)
                    e2 = signs[a] * e
                    dst = 2 * perm[a] + (0 if e2 > 0 else 1)
                    img[dst] = src
            G.append(tuple(img))
    assert len(set(G)) == 48
    return G

def d4_group():
    # slots: 0:E 1:W 2:N 3:S as (axis, sign) with axis 0=x,1=y
    G = []
    for perm in itertools.permutations(range(2)):
        for signs in itertools.product([1, -1], repeat=2):
            img = [None] * 4
            for a in range(2):
                for e in (1, -1):
                    src = 2 * a + (0 if e > 0 else 1)
                    e2 = signs[a] * e
                    dst = 2 * perm[a] + (0 if e2 > 0 else 1)
                    img[dst] = src
            G.append(tuple(img))
    assert len(set(G)) == 8
    return G

def report(name, f, n, q, group):
    cov = check_cov(f, n, q)
    iso = check_iso(f, n, q, group)
    aff = is_affine(f, n, q)
    wit = None if aff[0] else witness_base_point(f, n, q)
    print(f"{name}: q={q} n={n} covariance(a)={cov[0]} isotropy(b)={iso[0]} affine={aff[0]}"
          + (f" base-point witness (step d, base w)={wit}" if wit else "")
          + ("" if cov[0] else f" cov-fail={cov[1]}"))
    return cov[0], iso[0], aff[0]

ok = True
# ---- d = 3, O_h, q = 5 and q = 7 (3 must be invertible) --------------------------------
for q in (5, 7):
    alpha = pow(3, -1, q)            # 2d*alpha = 6*alpha = 2  <=> alpha = 1/3 = 1/d
    def G3(v, q=q):
        px, py, pz = v[0] + v[1], v[2] + v[3], v[4] + v[5]
        a, b, c = 2*px - py - pz, 2*py - pz - px, 2*pz - px - py
        C, P = a * b * c, a*a + b*b + c*c
        return (C * pow(P % q, q - 2, q)) % q
    f3 = lambda v, q=q, alpha=alpha, G3=G3: (alpha * sum(v) + G3(v)) % q
    c_, i_, a_ = report(f"d=3 counterexample f=s/3+C*P^(q-2)", f3, 6, q, oh_group())
    ok &= c_ and i_ and (not a_)
    flin = lambda v, q=q, alpha=alpha: (alpha * sum(v)) % q
    c_, i_, a_ = report("d=3 control linear f=s/3", flin, 6, q, oh_group())
    ok &= c_ and i_ and a_
    foff = lambda v, q=q, alpha=alpha: (alpha * sum(v) + 1) % q
    c_, i_, a_ = report("d=3 countercontrol affine-offset f=s/3+1", foff, 6, q, oh_group())
    ok &= (not c_) and i_ and a_

# ---- d = 3, O_h, q = 2 (only unit is 1; 2c = 0): f = s + [all six neighbours equal] -------
q = 2
f3b = lambda v: (sum(v) + (1 if len(set(v)) == 1 else 0)) % 2
c_, i_, a_ = report("d=3 counterexample q=2 f=s+[all nbrs equal]", f3b, 6, q, oh_group())
ok &= c_ and i_ and (not a_)

# ---- d = 2, D4, q = 7 (q = 3 mod 4 so chi(-1) = -1) -------------------------------------
q = 7
alpha = pow(2, -1, q)                # 2d*alpha = 4*alpha = 2  <=> alpha = 1/2 = 1/d
def f2(v):
    E, W, N, S = v
    y1, y2, y3 = E - W, N - S, E + W - N - S
    return (alpha * sum(v) + y3 * legendre(y1*y1 - y2*y2, q)) % q
c_, i_, a_ = report("d=2 counterexample f=s/2+y3*chi(y1^2-y2^2)", f2, 4, q, d4_group())
ok &= c_ and i_ and (not a_)

# ---- d = 1 positive control: (a)+(b) force the linear rule f = s (q = 3, exhaustive) ------
q = 3
pts = list(itertools.product(range(q), repeat=2))
refl = [(0, 1), (1, 0)]
sols = []
for vals in itertools.product(range(q), repeat=len(pts)):
    tab = dict(zip(pts, vals))
    f = lambda v, tab=tab: tab[tuple(x % q for x in v)]
    if check_iso(f, 2, q, refl)[0] and check_cov(f, 2, q)[0]:
        sols.append(vals)
lin = tuple((a + b) % q for a, b in pts)
print(f"d=1 control q=3: functions satisfying (a)+(b): {len(sols)}; equals f=s: {sols == [lin]}")
ok &= (sols == [lin])

print("ALL PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
