"""C-i verification of the explicit lattice construction found by search5.py (exact).

Construction C1 (strict region partition of Main.md l.292):
  graph: path 1 - 0 - 2 (n = 3); region R = {1} visible; sites 0 and 2 hidden.
  coordinates (f2.py order): u0 u1 u2 v0 v1 v2  (indices 0..5).
  roles at input:  toy h = (q, p) = (u0, v0)          hidden, the system
                   pointer Q = v1, its conjugate Qb = u1   visible, clean at 0
                   P = u2                               hidden, the bath site's u
                   Pb = v2                              hidden, idle (bath site's v)
  word: ONE update step of Main.md l.290, no observer operation.
  roles at output: q at v0, p at u0, Q at u1, P at v2 (the step exchanges u and v; pure
                   bookkeeping), Qb' at v1, Pb' at u2.
Target read: u = (0, 1) in the (q, p) labelling, i.e. omega(u, h) = q: Q' = Q + q, p' = p + P.

Checks:
  C1.1 bijective and symplectic (whole map);
  C1.2 designated rows equal the target on the declared clean inputs (Qb = 0), and the exact
       residual is listed;
  C1.3 with Q = Qb = 0, P and Pb uniform and independent, the joint law of (every visible
       record, h') equals R_u for every h (Fractions);
  C1.4 countercontrol: bath site known (P = 0) -> reads without disturbance;
  C1.5 the other two reads (omega = p, omega = q + p) are not produced by this word;
  C1.6 continued waiting on the fixed graph (the graph cannot be rewired): learnable space
       and hidden support given all records, tick by tick, with and without the observer
       resetting the visible pointer by feedback; compared with model A's support bound.
"""
from fractions import Fraction
from itertools import product
from f2 import (lattice_update, compose, apply, is_invertible, is_symplectic, fmt_matrix,
                identity, rank)

ALL_OK = True


def check(label, cond):
    global ALL_OK
    ALL_OK &= bool(cond)
    print(f"  [{'PASS' if cond else 'FAIL'}] {label}")


n = 3
U0, U1, U2, V0, V1, V2 = range(6)
names = ["u0", "u1", "u2", "v0", "v1", "v2"]
M = lattice_update(n, ((0, 1), (0, 2)))
print("C1  path 1-0-2, R = {1}; one update step")
print(fmt_matrix(M, n, names))
check("C1.1 bijective", is_invertible(M))
check("C1.1 symplectic (M J M^T = J)", is_symplectic(M, n))

# dense matrices
print("  M (rows = outputs u0 u1 u2 v0 v1 v2; columns = inputs in the same order):")
for i in range(6):
    print("    " + names[i].ljust(3) + " [" + " ".join(str((M[i] >> j) & 1) for j in range(6)) + "]")
roles = ["q", "p", "Q", "Qb", "P", "Pb"]
rin = {"q": U0, "p": V0, "Q": V1, "Qb": U1, "P": U2, "Pb": V2}
rout = {"q": V0, "p": U0, "Q": U1, "Qb": V1, "P": V2, "Pb": U2}
print("  the same step in role coordinates (input roles at their input cells, output roles at their")
print("  output cells; columns q p Q Qb P Pb):")
A = []
for r in roles:
    row = M[rout[r]]
    A.append([(row >> rin[c]) & 1 for c in roles])
    print("    " + (r + "'").ljust(4) + "[" + " ".join(map(str, A[-1])) + "]")
print("  target on (q, p, Q, P) for omega(u,h) = q  [u = (0,1)]:  Q' = Q + q, q' = q, p' = p + P, P' = P;")
print("  the only extra entry in the four designated rows is p' <- Qb (a visible clean input).")

# designated rows (input coordinates): q=u0, p=v0, Q=v1, P=u2
role_in = {"q": U0, "p": V0, "Q": V1, "P": U2}
role_out = {"q": V0, "p": U0, "Q": U1, "P": V2}
tgt = {"Q": (1 << V1) | (1 << U0), "q": 1 << U0, "p": (1 << V0) | (1 << U2), "P": 1 << U2}
print("  designated rows, output position <- input functional:")
resid = {}
for r in ("Q", "q", "p", "P"):
    row = M[role_out[r]]
    resid[r] = row ^ tgt[r]
    print(f"    {r}' (at {names[role_out[r]]}) = {' + '.join(names[j] for j in range(6) if row >> j & 1)}"
          f"   target {' + '.join(names[j] for j in range(6) if tgt[r] >> j & 1)}"
          f"   residual {' + '.join(names[j] for j in range(6) if resid[r] >> j & 1) or '0'}")
check("C1.2 residuals involve only the visible clean coordinate Qb = u1",
      all(x & ~(1 << U1) == 0 for x in resid.values()) and any(resid.values()))
print("  idle outputs: Qb' (v1) =", " + ".join(names[j] for j in range(6) if M[V1] >> j & 1),
      "; Pb' (u2) =", " + ".join(names[j] for j in range(6) if M[U2] >> j & 1))


def st(**kw):
    s = 0
    for k, v in kw.items():
        s |= (v & 1) << names.index(k)
    return s


def b(s, i):
    return (s >> i) & 1


# C1.3: R_u with all visible records
good = True
for hq, hp in product((0, 1), repeat=2):
    dist = {}
    for P_, Pb in product((0, 1), repeat=2):
        s1 = apply(M, st(u0=hq, v0=hp, u1=0, v1=0, u2=P_, v2=Pb))
        key = (b(s1, U1), b(s1, V1), b(s1, V0), b(s1, U0))      # records (u1, v1), then h' = (q', p')
        dist[key] = dist.get(key, Fraction(0)) + Fraction(1, 4)
    ref = {}
    for r in (0, 1):
        key = (hq, 0, hq, hp ^ r)        # pointer reads q; Qb' = 0; q' = q; p' = p + r
        ref[key] = ref.get(key, Fraction(0)) + Fraction(1, 2)
    good &= dist == ref
check("C1.3 Q = Qb = 0, P, Pb uniform: joint law of (u1', v1', q', p') equals R_u (read q, kick p) for all h", good)

# C1.4 countercontrol: bath site known
kn = all(apply(M, st(u0=hq, v0=hp, u2=0, v2=Pb)) & ((1 << U1) | (1 << V0) | (1 << U0))
         == ((hq << U1) | (hq << V0) | (hp << U0))
         for hq, hp, Pb in product((0, 1), repeat=3))
check("C1.4 P = 0 known: pointer reads q and h' = h exactly (no disturbance)", kn)

# C1.5 which toy functional does the visible record carry?
rec_rows = [M[U1], M[V1]]
toy_part = {r & ((1 << U0) | (1 << V0)) for r in rec_rows} - {0}
check("C1.5 the visible records carry the toy functional u0 = q only (not p, not q + p)",
      toy_part == {1 << U0})


# C1.6 continued waiting
def learnable_support(n_ticks, reset):
    """Return per tick: (rank of learnable hidden functionals, max/min support of hidden
    (u0, v0, u2, v2) given all records)."""
    out = []
    hidden = [U0, V0, U2, V2]
    for T in range(1, n_ticks + 1):
        branches = {}
        for hq, hp, P_, Pb in product((0, 1), repeat=4):
            s = st(u0=hq, v0=hp, u2=P_, v2=Pb)
            recs = []
            for t in range(T):
                s = apply(M, s)
                recs.append((b(s, U1), b(s, V1)))
                if reset:   # feedback: XOR the known record back out -> visible site back to (0, 0)
                    s &= ~((1 << U1) | (1 << V1))
            hid = tuple(b(s, i) for i in hidden)
            branches.setdefault(tuple(recs), set()).add(hid)
        sizes = [len(v) for v in branches.values()]
        out.append((T, min(sizes), max(sizes), len(branches)))
    return out


for reset in (False, True):
    print(f"  C1.6 continued waiting, pointer reset by feedback each tick: {reset}")
    for (T, mn, mx, nb) in learnable_support(6, reset):
        print(f"    after {T} tick(s): record branches {nb:2d}; hidden (toy + bath, 4 bits) support given records: min {mn}, max {mx}")

res_reset = learnable_support(6, True)
first_viol = next((T for (T, mn, mx, nb) in res_reset if mn < 2), None)
print(f"  first tick at which some record branch leaves hidden support < 2 (the bound 2^N with N >= 1): {first_viol}")
check("C1.6 continued waiting exhausts the single bath site: support 1 reached within 6 ticks",
      first_viol is not None)

# C1.7 K-SYMP2 correspondence: C1 with the bath site supplied KNOWN (u2 = v2 = 0)
ok7 = True
for hq, hp in product((0, 1), repeat=2):
    s = st(u0=hq, v0=hp)
    s1 = apply(M, s)
    s2 = apply(M, s1 & ~((1 << U1) | (1 << V1)))      # pointer reset by feedback
    ok7 &= (b(s1, U1), b(s2, U1)) == (hq, hp)          # tick 1 reveals q, tick 2 reveals p
check("C1.7 bath supplied known: records reveal q at tick 1 and p at tick 2 (toy support 1): K-SYMP2's failure mode", ok7)

# model A comparison: sequential reads with FRESH baths keep toy support 2 forever
print("  model A reference: reads with fresh independent kicks leave the toy support at 2 after every read")

print("VERIFY2:", "ALL PASS" if ALL_OK else "SOME FAIL")
