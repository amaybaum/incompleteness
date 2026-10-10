"""o5_src.py -- research/origin, round 2, the SRC side of HO-5's joint statement (if KB-D were SRC's source).

QUESTION. HO-5 item 6 (a proposal, not adopted) asks for SRC(B): one balanced mixer available on one token from a
premise passing the disguise test. If KB-D were that source, what exactly is the premise, does J = cyc3
(KInfFoundations.lean:425, :427) become available, and is the result usable where SPEC needs it (the pair cone)?

MODEL. One token: configurations (z, x) in {0,1}^2, all permutations available; the frame readout is KB-D (read the
partition, re-prepare uniformly within the outcome's cell), exclusive (no passive readout). Pure states: the six pair
states; Bloch coordinates (X, Y, Z) = (P(x=0) - P(x=1), P(z xor x = 0) - P(z xor x = 1), P(z=0) - P(z=1)), so the
pure states are the six unit vectors +-e_X, +-e_Y, +-e_Z (the octahedron) and cyc3 acts as (X, Y, Z) -> (Z, X, Y).
CHECKS.
  S1  exactly one permutation sigma of the four configurations induces cyc3 on the six pure states; it is a
      permutation of configurations (monomial on the carrier), of order 3, and its action is a rotation (the
      induced linear map on Bloch vectors has determinant +1).
  S2  sigma maps the pure frame state z+ to the pure state x+, balanced for the frame readout; the owner's sandwich
      with sigma, sigma^-1 and the KB-D frame dephasing (observe-and-forget of z) is exactly (1, 1/2).
  S3  composites of such tokens built from product registers with local readouts (each token read once, by any
      of its three partitions): over the 16 joint configurations every CHSH value lies in [-2, 2] and 2 is attained;
      every joint distribution is a mixture of configurations, so |S| <= 2 for every composite state.
DECISION RULE (fixed before the first run; the verdict is generated from the measured booleans):
  VERDICT VOID if any countercontrol is True.
  VERDICT SRC-KB-TOKEN-ONLY iff S1 and S2 and S3: on the premise "all configuration permutations + exclusive
    KB-D readout", J is available on one token as a configuration permutation with the exact witness, while every
    product-register composite is Bell-local (|S| <= 2), so it is not a realization of any candidate pair cone, all
    of which contain phiW with S = 14/5 (HO-3 v1 items 1-2, received); otherwise VERDICT MIXED.
COUNTERCONTROLS (must be False):
  CC1 a transposition of two configurations induces cyc3 (it must not: it acts as a reflection);
  CC2 a deterministic table in which token B's outcome depends on token A's setting stays within |S| <= 2 (it must
      not: the CHSH functional detects it, reaching 4).

Run: python3 -I -B o5_src.py > o5_src.out 2> o5_src.err; echo "exit $?" >> o5_src.err
"""

from fractions import Fraction as F
from itertools import permutations, product

OMEGA = [(0, 0), (0, 1), (1, 0), (1, 1)]   # (z, x)
N = 4
READ = {"Z": lambda c: c[0], "X": lambda c: c[1], "Y": lambda c: c[0] ^ c[1]}


def unif(cells):
    return tuple(F(1, len(cells)) if i in cells else F(0) for i in range(N))


def cells(name):
    return [tuple(i for i in range(N) if READ[name](OMEGA[i]) == v) for v in (0, 1)]


PURE = {}
for name in "ZXY":
    c0, c1 = cells(name)
    PURE[name + "+"], PURE[name + "-"] = unif(c0), unif(c1)


def bloch(w):
    def e(name):
        c0, c1 = cells(name)
        return sum(w[i] for i in c0) - sum(w[i] for i in c1)
    return (e("X"), e("Y"), e("Z"))


def apply_perm(sig, w):
    v = [F(0)] * N
    for i in range(N):
        v[sig[i]] += w[i]
    return tuple(v)


def cyc3(v):
    X, Y, Z = v
    return (Z, X, Y)


def induces_cyc3(sig):
    return all(bloch(apply_perm(sig, w)) == cyc3(bloch(w)) for w in PURE.values())


def det3(M):
    return (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1]) - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
            + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))


def bloch_matrix(sig):
    cols = [bloch(apply_perm(sig, PURE[a + "+"])) for a in "XYZ"]
    return [[cols[j][i] for j in range(3)] for i in range(3)]


RES = {}
CC = {}
print("== o5_src ==")
print(f"pure states (Bloch): " + ", ".join(f"{k} {bloch(v)}" for k, v in sorted(PURE.items())))
S4 = list(permutations(range(N)))
hits = [s for s in S4 if induces_cyc3(s)]
sig = hits[0] if len(hits) == 1 else None
s1 = False
if sig is not None:
    s2_ = tuple(sig[sig[i]] for i in range(N))
    s3_ = tuple(sig[s2_[i]] for i in range(N))
    order3 = s3_ == tuple(range(N)) and s2_ != tuple(range(N)) and sig != tuple(range(N))
    s1 = order3 and det3(bloch_matrix(sig)) == 1
RES["S1"] = s1
print(f"S1  permutations inducing cyc3: {len(hits)} ({hits}); order 3 and a rotation "
      f"(det of the induced map {det3(bloch_matrix(sig)) if sig else None}): {s1}")
transp = (1, 0, 2, 3)
CC["CC1"] = induces_cyc3(transp)
print(f"    transposition (00 01) induces a map of determinant {det3(bloch_matrix(transp))}")


def kbd_z_forget(w):
    out = [F(0)] * N
    for c in cells("Z"):
        m = sum(w[i] for i in c)
        for i in c:
            out[i] += m / len(c)
    return tuple(out)


inv = tuple(sig.index(i) for i in range(N)) if sig else None
s2 = False
if sig is not None:
    zp = PURE["Z+"]
    mid = apply_perm(sig, zp)
    p_coh = sum(apply_perm(inv, mid)[i] for i in cells("Z")[0])
    p_deph = sum(apply_perm(inv, kbd_z_forget(mid))[i] for i in cells("Z")[0])
    balanced = sum(mid[i] for i in cells("Z")[0]) == F(1, 2)
    s2 = mid == PURE["X+"] and balanced and p_coh == 1 and p_deph == F(1, 2)
    print(f"S2  sigma(z+) = x+: {mid == PURE['X+']}; frame probability of sigma(z+): "
          f"{sum(mid[i] for i in cells('Z')[0])}; sandwich (P_coh, P_deph) = ({p_coh}, {p_deph})  -> {s2}")
RES["S2"] = s2


def chsh(resp, a0, a1, b0, b1, cfgs):
    """max and min of S over joint configurations; resp(token, setting, config) in {+1, -1}."""
    vals = []
    for c in cfgs:
        def E(a, b):
            return resp(0, a, c) * resp(1, b, c)
        vals.append(E(a0, b0) + E(a0, b1) + E(a1, b0) - E(a1, b1))
    return max(vals), min(vals)


JOINT = list(product(OMEGA, OMEGA))


def local_resp(tok, setting, c):
    return 1 if READ[setting](c[tok]) == 0 else -1


mx, mn = -10, 10
for a0, a1, b0, b1 in product("ZXY", repeat=4):
    if a0 == a1 or b0 == b1:
        continue
    hi, lo = chsh(local_resp, a0, a1, b0, b1, JOINT)
    mx, mn = max(mx, hi), min(mn, lo)
RES["S3"] = mx == 2 and mn == -2
print(f"S3  product registers, local readouts: CHSH over the 16 joint configurations and all setting pairs: max {mx}, "
      f"min {mn}  -> |S| <= 2 with 2 attained: {RES['S3']}")


# CC2: B's outcome depends on A's setting: PR-type deterministic table, S = 4
def pr_value():
    def A(a):
        return 1

    def B(a, b):
        return -1 if (a == 1 and b == 1) else 1
    return sum((1 if (a, b) != (1, 1) else -1) * A(a) * B(a, b) for a in (0, 1) for b in (0, 1))


CC["CC2"] = abs(pr_value()) <= 2
print(f"    setting-dependent table: S = {pr_value()}")
print()
print("-- countercontrols (must be False)")
for k in sorted(CC):
    print(f"{k}  {'CC-OK (False as required)' if not CC[k] else 'CC-FAIL (True)'}")
print()
for k in sorted(RES):
    print(f"  {k}: {RES[k]}")
if any(CC.values()):
    print("VERDICT VOID: a countercontrol returned True.")
elif all(RES.values()):
    print("VERDICT SRC-KB-TOKEN-ONLY: with all configuration permutations and an exclusive KB-D frame readout, J = cyc3")
    print("  is available on one token as a configuration permutation of order 3 with the exact witness (1, 1/2); every")
    print("  composite of such tokens built from product registers with local readouts has |S| <= 2, so it realizes no")
    print("  candidate pair cone (each contains phiW, S = 14/5, HO-3 v1).")
else:
    print(f"VERDICT MIXED: failing items {[k for k, v in RES.items() if not v]}")
