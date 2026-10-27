#!/usr/bin/env python3
"""sc23 F1 — exponential bound vs exact zero. Implements PREREG.txt (+ amendment A1) exactly.
Run: python3 -I f1.py   (exit 0 iff all controls green)."""
import sys, itertools
from fractions import Fraction as F
from collections import defaultdict
from decimal import Decimal, getcontext
getcontext().prec = 200
LN2 = Decimal(2).ln()

def D(q):  # Fraction -> Decimal
    return Decimal(q.numerator) / Decimal(q.denominator)

def erode_cell(v, r):
    """distribution of a cell with value v after one erosion interval"""
    return {v: r + (1 - r) / 2, 1 - v: (1 - r) / 2}

def hmm_law(d, r, K, written_x0):
    """Model E (written_x0=False) or E' (True). Returns joint law over x_0..x_K (Fraction),
    and per-record the post-erosion register law at the next coupling (for eps)."""
    ens = defaultdict(F)  # (hist, cells) -> prob
    for x0 in (0, 1):
        for cells in itertools.product((0, 1), repeat=d):
            if written_x0:
                if cells[0] != x0:
                    continue
                w = F(1, 2) * F(1, 2 ** (d - 1))
            else:
                w = F(1, 2) * F(1, 2 ** d)
            ens[((x0,), cells)] += w
    eroded_given = {}  # hist -> dict cells -> prob (post-erosion, pre-read), unnormalized
    for t in range(K):
        new = defaultdict(F)
        for (h, cells), p in ens.items():
            # erosion of every cell independently
            dists = [erode_cell(v, r) for v in cells]
            for ec in itertools.product((0, 1), repeat=d):
                q = p
                for i in range(d):
                    q *= dists[i][ec[i]]
                if q == 0:
                    continue
                eroded_given.setdefault(h, defaultdict(F))[ec] += q
                x1 = ec[d - 1]
                nc = (x1,) + ec[:d - 1]
                new[(h + (x1,), nc)] += q
        ens = new
    law = defaultdict(F)
    for (h, cells), p in ens.items():
        law[h] += p
    return law, eroded_given

def marg(law, n):
    m = defaultdict(F)
    for h, p in law.items():
        m[h[:n]] += p
    return m

def gaps(law, K):
    """delta_k for k=1..K-1 (D1), with witnessing p0."""
    out = {}
    for k in range(1, K):
        Pk1 = marg(law, k + 2); Pk = marg(law, k + 1)
        best = (F(0), F(0))
        hists = [h for h in Pk if Pk[h] > 0]
        for c in (0, 1):
            hs = [h for h in hists if h[-1] == c]
            cond = {h: Pk1.get(h + (1,), F(0)) / Pk[h] for h in hs}
            for a, b in itertools.combinations(hs, 2):
                tv = abs(cond[a] - cond[b])
                p0 = min(Pk[a], Pk[b])
                if (tv, p0) > best:
                    best = (tv, p0)
        out[k] = best
    return out

def cmi(law, k):
    """M_k = I(X_<k; X_{k+1} | X_k) in bits, Decimal; exact-zero flag if all ratios are 1."""
    Pk1 = marg(law, k + 2); Pk = marg(law, k + 1)
    pair = defaultdict(F); single = defaultdict(F)
    for h, p in Pk1.items():
        pair[(h[-2], h[-1])] += p
    for h, p in Pk.items():
        single[h[-1]] += p
    tot = Decimal(0); allone = True
    for h, p in Pk1.items():
        if p == 0:
            continue
        a = p / Pk[h[:-1]]
        b = pair[(h[-2], h[-1])] / single[h[-2]]
        ratio = a / b
        if ratio != 1:
            allone = False
            tot += D(p) * D(ratio).ln() / LN2
    return tot, allone

def hbin(e):
    e = D(e) if isinstance(e, F) else e
    if e == 0:
        return Decimal(0)
    return -(e * e.ln() + (1 - e) * (1 - e).ln()) / LN2

def tv_uniform(dist, n):
    tot = sum(dist.values())
    return sum(abs(dist.get(c, F(0)) / tot - F(1, n)) for c in itertools.product((0, 1), repeat=n.bit_length() - 1)) / 2

def eps_values(eroded_given, d, k):
    """max over realized records of length k+1 (x_0..x_k) of eps_coarse and eps_full at coupling k+1"""
    ec_max = F(0); ef_max = F(0)
    for h, dist in eroded_given.items():
        if len(h) != k + 1:
            continue
        tot = sum(dist.values())
        p1 = sum(q for c, q in dist.items() if c[d - 1] == 1) / tot
        ec_max = max(ec_max, abs(p1 - F(1, 2)))
        ef_max = max(ef_max, tv_uniform(dist, 2 ** d))
    return ec_max, ef_max

# ---------- independent realizations ----------
def bijection_Eprime_d2(rnum, rden, L):
    """E'(2,r) with keep-prob r^2 at read realized as (x, m, coin tape, fresh tape); coin symbol
    in Z_{rden^2}, keep iff symbol < rnum^2."""
    N = rden * rden; KEEP = rnum * rnum
    def phi(s):
        x, m, c, f = s
        if c[0] < KEEP:
            x2, other = m, f[0]
        else:
            x2, other = f[0], m
        return (x2, x, c[1:] + (c[0],), f[1:] + (other,))
    space = [(x, m, c, f) for x in (0, 1) for m in (0, 1)
             for c in itertools.product(range(N), repeat=L) for f in itertools.product((0, 1), repeat=L)]
    return phi, space

def bruteforce_E(d, r, K):
    """Model E by enumerating all erosion coins (keep/replace) and fresh bits explicitly."""
    law = defaultdict(F)
    nev = K * d
    for x0 in (0, 1):
        for cells0 in itertools.product((0, 1), repeat=d):
            for keeps in itertools.product((0, 1), repeat=nev):
                wk = F(1)
                for kk in keeps:
                    wk *= r if kk else (1 - r)
                if wk == 0:
                    continue
                for fresh in itertools.product((0, 1), repeat=nev):
                    w = F(1, 2) * F(1, 2 ** d) * wk * F(1, 2 ** nev)
                    x = x0; cells = list(cells0); hist = [x0]; idx = 0
                    for t in range(K):
                        for i in range(d):
                            if not keeps[idx]:
                                cells[i] = fresh[idx]
                            idx += 1
                        x = cells[d - 1]
                        cells = [x] + cells[:d - 1]
                        hist.append(x)
                    law[tuple(hist)] += w
    return law

fail = 0
def check(name, ok, info=""):
    global fail
    print(f"  [{'PASS' if ok else 'FAIL'}] {name} {info}")
    if not ok:
        fail += 1

K = 7
RS = [F(0), F(1, 10 ** 12), F(1, 2 ** 20), F(1, 1000), F(1, 2), F(1)]
results = {}
print("== F1: Model E (frozen) and E' (amendment A1): exact gaps delta_k, k=1..6 ==")
for model, wx0 in (("E", False), ("E'", True)):
    for d in (2, 3):
        for r in RS:
            law, eg = hmm_law(d, r, K, wx0)
            assert sum(law.values()) == 1
            g = gaps(law, K)
            results[(model, d, r)] = (law, eg, g)
            print(f" {model} d={d} r={r if r < F(1,1000) or r in (0,1) else r}: " +
                  " ".join(f"k{k}:{'0' if g[k][0]==0 else ('r^%d' % next((j for j in range(0,40) if g[k][0]*2 == 2*r**j), -1) if 0<r<1 else str(g[k][0]))}" for k in g))

print("== Controls ==")
for model in ("E", "E'"):
    for d in (2, 3):
        law, eg, g = results[(model, d, F(0))]
        ok = all(g[k][0] == 0 for k in g) and all(cmi(law, k)[1] for k in g)
        check(f"CF1-a {model} d={d} r=0: delta_k=0 and all next-step conditionals equal (M_k=0 exactly)", ok)
        law, eg, g = results[(model, d, F(1))]
        lo = max(1, d - 1)
        okb = all(g[k][0] == 1 for k in g if k >= lo)
        check(f"CF1-b {model} d={d} r=1: delta_k=1 for k>={lo}", okb,
              f"(values {[str(g[k][0]) for k in g]})")
# CF1-c: bijection for E'(2,1/2), horizon 4, tape length 4
phi, space = bijection_Eprime_d2(1, 2, 4)
img = set(phi(s) for s in space)
check("CF1-c bijection is a bijection", len(img) == len(space), f"(|S|={len(space)})")
blaw = defaultdict(F)
w = F(1, len(space))
for s in space:
    hist = [s[0]]; cur = s
    for t in range(4):
        cur = phi(cur); hist.append(cur[0])
    blaw[tuple(hist)] += w
hlaw4, _ = hmm_law(2, F(1, 2), 4, True)
check("CF1-c bijection visible law == E'(2,1/2) HMM law on all 2^5 trajectories",
      dict(blaw) == {h: p for h, p in hlaw4.items() if p}, f"({len(blaw)} trajectories)")
# CF1-c': brute force for E
bl = bruteforce_E(2, F(1, 2), 4)
hl, _ = hmm_law(2, F(1, 2), 4, False)
check("CF1-c' brute-force enumeration == HMM forward for E(2,1/2), horizon 4",
      {h: p for h, p in bl.items() if p} == {h: p for h, p in hl.items() if p})
# CF1-d, CF1-e
for model in ("E", "E'"):
    for d in (2, 3):
        for r in RS[1:5]:
            law, eg, g = results[(model, d, r)]
            for k in g:
                Mk, _ = cmi(law, k)
                dl, p0 = g[k]
                lb = D(p0) * D(dl) ** 2 / LN2
                ec, ef = eps_values(eg, d, k)
                okd = Mk >= lb
                oke = (Mk <= 2 * hbin(ec) if ec <= F(1, 2) else True) and (Mk <= 2 * hbin(ef) if ef <= F(1, 2) else True)
                if not (okd and oke):
                    check(f"CF1-d/e {model} d={d} r={r} k={k}", False, f"M={Mk:.6e} lb={lb:.6e} ec={ec} ef={float(ef)}")
print("  [checked] CF1-d (backflow lower bound) and CF1-e (physical-memory upper bound) on all "
      "E/E' x d x r in (0,1) x k; failures, if any, listed above")
cf_ok = (fail == 0)

print("== Verdict data ==")
for model in ("E", "E'"):
    for d in (2, 3):
        for r in RS[1:5]:
            law, eg, g = results[(model, d, r)]
            x = -D(r).ln()
            row = []
            for k in g:
                Mk, _ = cmi(law, k)
                ec, ef = eps_values(eg, d, k)
                env = 2 / LN2 * D(r) * (x + 1)
                row.append((k, g[k][0], Mk, ec, ef, env))
            print(f" {model} d={d} r={r} tauB/tauS=1/ln(1/r)={float(1/x):.4f}")
            for k, dl, Mk, ec, ef, env in row:
                print(f"   k={k} delta_k={'0' if dl==0 else '%.6e' % float(dl)}  r^(k-1)={float(r**(k-1)):.3e}  "
                      f"refutes={'Y' if dl > r**(k-1) else 'n'}  M_k={float(Mk):.6e}  eps_coarse={float(ec):.3e} "
                      f"eps_full={float(ef):.3e}  2h(eps_coarse)={float(2*hbin(ec)):.3e}  envelope(eps=r)={float(env):.3e}")
# closed form check for E' : M_k = 1 - h((1 - r^d)/2) for k>=d-1
for d in (2, 3):
    for r in RS[1:5]:
        law, eg, g = results[("E'", d, r)]
        for k in g:
            if k >= d - 1:
                Mk, _ = cmi(law, k)
                cf = 1 - hbin((1 - r ** d) / 2)
                if abs(Mk - cf) > Decimal(10) ** -150 * (1 + abs(cf)):
                    check(f"closed form E' d={d} r={r} k={k}", False, f"{Mk} vs {cf}")
print("  [checked] closed form M_k = 1 - h((1-r^d)/2) for E', k>=d-1 (failures listed above)")
cf_ok = (fail == 0)

print("== Verdicts ==")
if not cf_ok:
    print("  VOID: a control failed")
else:
    v11 = [(m, d, r, k) for (m, d, r), (_, _, g) in results.items() if 0 < r < 1 for k in g if g[k][0] > r ** (k - 1)]
    print(f"  V1-1: {'PRINT' if v11 else 'no'} — lemma inequality (reading R1) refuted at {len(v11)} (model,d,r,k) cells; "
          f"smallest k per (model,d): " + str(sorted({(m, d): min(kk for (mm, dd, rr, kk) in v11 if (mm, dd) == (m, d)) for (m, d, r, k) in v11}.items())))
    def v12(model, lo_fn):
        hits = []
        for (m, d, r), (law, eg, g) in results.items():
            if m != model or not (0 < r < 1):
                continue
            if 1 / (-D(r).ln()) >= Decimal("0.2"):
                continue
            ks = [k for k in g if k >= lo_fn(d)]
            if all(g[k][0] > 0 and g[k][1] > 0 for k in ks):
                hits.append((d, r))
        return hits
    h12 = v12("E", lambda d: max(1, d - 1))
    print(f"  V1-2 (frozen, Model E): {'PRINT' if h12 else 'no'} {h12}")
    h12p = v12("E'", lambda d: d - 1)
    print(f"  V1-2' (A1, Model E'): {'PRINT' if h12p else 'no'} {[(d, str(r)) for d, r in h12p]}")
print("f1:", "ALL CONTROLS GREEN" if fail == 0 else f"{fail} FAILURE(S)")
sys.exit(1 if fail else 0)
