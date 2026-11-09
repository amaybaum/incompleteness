"""p13 (writer, r7): exact checks of SHARED Q4-P20 and Q4-D8 on generic objects.

Generic objects only: affine maps of F_q^4 (q = 2, 3) with coordinates (c, x, m, m'),
symplectic pairs (c, x) and (m, m'), omega(u, v) = u_c v_x - u_x v_c + u_m v_m' - u_m' v_m.
No OI mechanism is computed.  Standard library only; imports no earlier probe.

Definitions (as in Q4-P20):
- a meter ready law is a set of (m, m') values, uniform on it:
    sharp:   one point;
    SA-1(c): the whole line {l(m, m') = k} for a nonzero linear functional l (the known functional);
    unknown: the whole meter plane;
- the carrier's x ranges over all of F_q on each branch c in {0, 1};
- 'records readably': some nonzero linear functional f of the OUTPUT meter slots takes, on
  {c} x F_q x R, one value for c = 0 and one different value for c = 1;
- 'K_null = id': x' = x on every input state with c = 0, x in F_q, meter in R.
"""
import itertools
import sys

N_PASS = 0
N_FAIL = 0


def check(name, cond, detail=""):
    global N_PASS, N_FAIL
    if cond:
        N_PASS += 1
    else:
        N_FAIL += 1
    print(("PASS " if cond else "FAIL ") + name + (("  -- " + detail) if detail else ""))


C, X, MM, MP = 0, 1, 2, 3
# Gram matrix J of omega: omega(u, v) = u^T J v
J = ((0, 1, 0, 0), (-1, 0, 0, 0), (0, 0, 0, 1), (0, 0, -1, 0))


def matmul(A, B, q):
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(4)) % q for j in range(4)) for i in range(4))


def transpose(A):
    return tuple(tuple(A[j][i] for j in range(4)) for i in range(4))


def red(A, q):
    return tuple(tuple(a % q for a in row) for row in A)


def is_symplectic(M, q):
    # M^T J M == J  (mod q)
    return matmul(matmul(transpose(M), red(J, q), q), M, q) == red(J, q)


def apply(M, b, y, q):
    return tuple((sum(M[i][j] * y[j] for j in range(4)) + b[i]) % q for i in range(4))


def nonzero_funcs(q):
    return [f for f in itertools.product(range(q), repeat=2) if f != (0, 0)]


def projective_funcs(q):
    # one representative per line through 0 in the dual plane
    reps = []
    seen = set()
    for f in nonzero_funcs(q):
        if f in seen:
            continue
        reps.append(f)
        for s in range(1, q):
            seen.add(((s * f[0]) % q, (s * f[1]) % q))
    return reps


def meter_laws(q):
    laws = {}
    for p in itertools.product(range(q), repeat=2):
        laws["sharp%s" % (p,)] = ("sharp", [p])
    for l in projective_funcs(q):
        for k in range(q):
            R = [p for p in itertools.product(range(q), repeat=2) if (l[0] * p[0] + l[1] * p[1]) % q == k]
            laws["SA1c l=%s k=%d" % (l, k)] = ("sa1c", R)
    laws["unknown"] = ("unknown", list(itertools.product(range(q), repeat=2)))
    return laws


def readable(M, b, R, q):
    for f in nonzero_funcs(q):
        vals = {0: set(), 1: set()}
        for c in (0, 1):
            for x in range(q):
                for (m, mp) in R:
                    out = apply(M, b, (c, x, m, mp), q)
                    vals[c].add((f[0] * out[MM] + f[1] * out[MP]) % q)
        if len(vals[0]) == 1 and len(vals[1]) == 1 and vals[0] != vals[1]:
            return True
    return False


def knull_id(M, b, R, q):
    return all(apply(M, b, (0, x, m, mp), q)[X] == x for x in range(q) for (m, mp) in R)


# ---------------------------------------------------------------------------
print("== 1. symplectic linear parts, built by filtering M^T J M = J")
# F_2: all 4x4 matrices
SP2 = []
for e in itertools.product(range(2), repeat=16):
    M = tuple(tuple(e[4 * i:4 * i + 4]) for i in range(4))
    if is_symplectic(M, 2):
        SP2.append(M)
check("1a |Sp(4,F_2)| = 720", len(SP2) == 720, str(len(SP2)))
# F_3: location-preserving linear parts only (row c = e_c^T)
LP3 = []
for e in itertools.product(range(3), repeat=12):
    M = ((1, 0, 0, 0), tuple(e[0:4]), tuple(e[4:8]), tuple(e[8:12]))
    if is_symplectic(M, 3):
        LP3.append(M)
check("1b location-preserving symplectic linear parts over F_3 = 648 (= 51,840 / 80)", len(LP3) == 648, str(len(LP3)))
# control of the proof step: brackets of linear functionals are preserved, M J^{-1} M^T = J^{-1}
Jinv = lambda q: red(tuple(tuple(-a for a in row) for row in J), q)  # J^{-1} = -J
ok = all(matmul(matmul(M, Jinv(2), 2), transpose(M), 2) == Jinv(2) for M in SP2) and \
    all(matmul(matmul(M, Jinv(3), 3), transpose(M), 3) == Jinv(3) for M in LP3)
check("1c every enumerated symplectic M satisfies M J^-1 M^T = J^-1 (bracket preservation)", ok)

AFF2 = [(M, b) for M in SP2 for b in itertools.product(range(2), repeat=4)]
check("1d affine-symplectic maps of F_2^4 = 11,520", len(AFF2) == 11520, str(len(AFF2)))
LPAFF2 = [(M, b) for (M, b) in AFF2 if M[C] == (1, 0, 0, 0) and b[C] == 0]
check("1e location-preserving ones over F_2 = 384", len(LPAFF2) == 384, str(len(LPAFF2)))
LPAFF3 = [(M, b) for M in LP3 for b in itertools.product(range(3), repeat=4) if b[C] == 0]
check("1f location-preserving affine-symplectic maps over F_3 = 17,496", len(LPAFF3) == 17496, str(len(LPAFF3)))

# ---------------------------------------------------------------------------
print("== 2. Q4-P20: under every SA-1(c) meter law, every readable recorder has K_null != id")
summary = {}
for (label, q, maps) in (("F_2, all affine-symplectic", 2, AFF2),
                         ("F_2, location-preserving", 2, LPAFF2),
                         ("F_3, location-preserving", 3, LPAFF3)):
    laws = meter_laws(q)
    res = {}
    for name, (kind, R) in laws.items():
        rd = [(M, b) for (M, b) in maps if readable(M, b, R, q)]
        nid = sum(1 for (M, b) in rd if knull_id(M, b, R, q))
        res[name] = (kind, len(rd), nid)
        print("   %-28s %-22s readable %5d ; with K_null = id %5d" % (label, name, len(rd), nid))
    summary[label] = res
    sa = [v for v in res.values() if v[0] == "sa1c"]
    check("2 [%s] SA-1(c): readable recorders exist under every law (non-vacuous)" % label,
          all(v[1] > 0 for v in sa))
    check("2 [%s] SA-1(c): no readable recorder has K_null = id" % label, all(v[2] == 0 for v in sa))
    sh = [v for v in res.values() if v[0] == "sharp"]
    check("2 [%s] sharp meters: some readable recorder has K_null = id under every sharp law (countercontrol)" % label,
          all(v[2] > 0 for v in sh))

lp2 = summary["F_2, location-preserving"]
check("2x F_2 location-preserving, sharp (0, 0): 288 readable, 144 with K_null = id",
      lp2["sharp(0, 0)"][1:] == (288, 144), str(lp2["sharp(0, 0)"][1:]))
check("2y location-preserving: with both meter slots unknown no map records readably (F_2 and F_3)",
      summary["F_2, location-preserving"]["unknown"][1] == 0 and summary["F_3, location-preserving"]["unknown"][1] == 0)

# ---------------------------------------------------------------------------
print("== 3. Q4-D8: the reciprocal coupling (c, x, m, m') -> (c, x - m', m + c, m')")
for q in (2, 3):
    Mrec = ((1, 0, 0, 0), (0, 1, 0, (-1) % q), (1, 0, 1, 0), (0, 0, 0, 1))
    b0 = (0, 0, 0, 0)
    check("3a q=%d: linear, symplectic, location-preserving" % q, is_symplectic(Mrec, q) and Mrec[C] == (1, 0, 0, 0))
    check("3b q=%d: meter write depends on c (records occupation)" % q,
          apply(Mrec, b0, (1, 0, 0, 0), q)[MM] != apply(Mrec, b0, (0, 0, 0, 0), q)[MM])
    check("3c q=%d: sharp meter (0, 0): records readably and K_null = id" % q,
          readable(Mrec, b0, [(0, 0)], q) and knull_id(Mrec, b0, [(0, 0)], q))
    Rc = [(0, mp) for mp in range(q)]
    check("3d q=%d: SA-1(c) meter (m known 0, m' uniform): records readably and K_null != id" % q,
          readable(Mrec, b0, Rc, q) and not knull_id(Mrec, b0, Rc, q))

# ---------------------------------------------------------------------------
print("== 4. countercontrol on the symplectic hypothesis: the copy coupling m <- m + c")
Mcopy = ((1, 0, 0, 0), (0, 1, 0, 0), (1, 0, 1, 0), (0, 0, 0, 1))
Rc = [(0, 0), (0, 1)]
check("4a the copy coupling is not symplectic", not is_symplectic(Mcopy, 2))
check("4b with an SA-1(c) meter it records readably and has K_null = id (symplecticity is load-bearing)",
      readable(Mcopy, (0, 0, 0, 0), Rc, 2) and knull_id(Mcopy, (0, 0, 0, 0), Rc, 2))

print("== %d of %d checks pass" % (N_PASS, N_PASS + N_FAIL))
sys.exit(0 if N_FAIL == 0 else 1)
