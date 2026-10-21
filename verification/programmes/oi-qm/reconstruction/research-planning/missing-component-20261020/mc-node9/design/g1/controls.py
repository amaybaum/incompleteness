"""Controls: K-G1 witnesses (fixed), trivial extension = cards, calibration extensions = QM, K-STAB-GAP."""
from g1lib import *
from fractions import Fraction as Fr
n = 2; R = card_relmaps(n)
print("== relation push-forwards (Schroedinger) of the card maps; must equal Clifford conjugation labels")
names = {XB(0): "XA", ZB(0): "ZA", XB(1): "XB", ZB(1): "ZB"}
def lab(u): return "*".join(names[1 << i] for i in range(4) if (u >> i) & 1) or "I"
for nm, S in R.items():
    print(" ", nm, {lab(1 << i): lab(S[1 << i]) for i in range(4)})
# symplectic check
for nm, S in R.items():
    assert all(omega(S[u], S[v], n) == omega(u, v, n) for u in range(16) for v in range(16)), nm
print("  all card maps symplectic: True")

card = CardTheory(n); qm = QMTheory(n)
print("== K-G1 (fixed words; never tuned): W6 = (swap_A, couple)^3 then read q_B ; W7 = W6 + swap_A")
for nm, T in (("cards", card), ("QM (calibration)", qm)):
    print("  %-18s W6 -> %s   W7 -> %s" % (nm, {o: str(p) for o, p in run_word(T, W6, "read1").items()},
                                           {o: str(p) for o, p in run_word(T, W7, "read1").items()}))
# card W7 returns to start
s = card.init()
for op in W7: s = card.step(op, s)
print("  cards: state after W7 equals initial state:", s == card.init())

# trivial extension (abelian, C=Z2, beta=0, commutator 0) with card value-transport lifts
E0 = Ext(n, 2, [[0]*16 for _ in range(16)]); d0 = default_dict(E0)
lifts0 = {nm: E0.extend(S, [E0.el(0, S[1 << i]) for i in range(4)]) for nm, S in R.items()}
assert all(E0.is_hom(p) for p in lifts0.values())
T0 = ExtTheory(E0, d0, ext_theory_ops(E0, d0, lifts0))
print("== trivial extension engine vs direct card simulation, all words over", ALPH_FULL)
print("  ", equivalent(T0, card, ALPH_FULL))
print("   (flips = value twists; in this abelian extension they are NOT inner, every inner automorphism is trivial:",
      all(E0.inner(g) == tuple(range(E0.size)) for g in range(E0.size)), ")")

for m, scale, tag in ((2, 1, "C=Z2 real Pauli (beta = z.x')"), (4, 2, "C=Z4 complex Pauli (beta = 2 z.x')")):
    E = Ext(n, m, bilinear_beta(n, m, real_pauli_coeff(n, scale)))
    assert E.is_cocycle() and E.commutator_is(lambda u, v: (m//2)*omega(u, v, n))
    d = default_dict(E)
    L = {}
    for nm, S in R.items():
        phi, st = ert_lift(E, S, d); assert phi is not None, st; L[nm] = phi
    T = ExtTheory(E, d, ext_theory_ops(E, d, L))
    assert all(value_twist(E, w) == E.inner(g) for w in range(16) for g in range(E.size) if E.proj(g) == w)
    print("== calibration", tag, "with ERT lifts")
    print("   W6 ->", {o: str(p) for o, p in run_word(T, W6, "read1").items()},
          " W7 ->", {o: str(p) for o, p in run_word(T, W7, "read1").items()})
    print("   vs exact QM, all words over full alphabet:", equivalent(T, qm, ALPH_FULL))
    print("   vs cards:", equivalent(T, card, ALPH_FULL)[:2])

print("== reachable sets (full alphabet)")
for nm, T in (("cards", card), ("QM", qm), ("trivial ext", T0)):
    st, ntr, nbr = reachable(T, ALPH_FULL)
    print("  %-12s states %d, gate transitions %d, read branches %d" % (nm, len(st), ntr, nbr))
st, _, _ = reachable(qm, ["swap0", "swap1", "couple", "flipq0", "flipq1", "read0", "read1"])
print("  QM under {H_A,H_B,CNOT,X_A,X_B,Z-meas}: states", len(st))

print("== K-STAB-GAP (exact): single-qubit Bloch components of every reachable QM state")
def bloch(v, j):
    rho = dm_key(v)   # 4x4 flattened, entries (re, im) Fractions
    M = [[rho[4*r+c] for c in range(4)] for r in range(4)]
    # reduced state of qubit j
    def red(a, b):
        acc = [Fr(0), Fr(0)]
        for k in (0, 1):
            r = (a << 1 | k) if j == 0 else (k << 1 | a); c = (b << 1 | k) if j == 0 else (k << 1 | b)
            acc[0] += M[r][c][0]; acc[1] += M[r][c][1]
        return acc
    r00, r01, r10, r11 = red(0, 0), red(0, 1), red(1, 0), red(1, 1)
    return (2*r01[0], -2*r01[1] if False else 2*r10[1], r00[0]-r11[0])  # (<X>, <Y>, <Z>)
vals = set()
for v in st.values():
    for j in (0, 1): vals |= set(bloch(v, j))
print("  components:", sorted(vals))
stf, _, _ = reachable(qm, ALPH_FULL); vals = set()
for v in stf.values():
    for j in (0, 1): vals |= set(bloch(v, j))
print("  full alphabet (with Z flips too):", len(stf), "states, components:", sorted(vals))

print("== preserved results (stated before the extension runs; these are the revision's controls)")
E1 = Ext(1, 2, bilinear_beta(1, 2, real_pauli_coeff(1, 1))); dd1 = default_dict(E1)
R1 = card_relmaps(1); L1 = {nm: ert_lift(E1, S, dd1)[0] for nm, S in R1.items()}
T1 = ExtTheory(E1, dd1, ext_theory_ops(E1, dd1, L1))
A1 = ["swap0", "flipq0", "flipp0", "read0"]
print("  P1 single system, D4 real class + ERT == cards (n=1):", equivalent(T1, CardTheory(1), A1),
      " == QM (n=1):", equivalent(T1, QMTheory(1), A1))
E = Ext(2, 2, bilinear_beta(2, 2, real_pauli_coeff(2, 1))); d = default_dict(E)
L = {nm: ert_lift(E, S, d)[0] for nm, S in R.items()}; T = ExtTheory(E, d, ext_theory_ops(E, d, L))
A2 = ["couple", "flipq0", "flipq1", "flipp0", "flipp1", "read0", "read1"]
print("  P2 coupling without swaps (classical reversible sector) == cards:", equivalent(T, card, A2))
A3 = ["swap0", "swap1", "flipq0", "flipq1", "flipp0", "flipp1", "read0", "read1"]
print("  P3 two systems, local operations only == cards:", equivalent(T, card, A3))
print("  shortest word distinguishing cards from QM (BFS):", equivalent(card, qm, ALPH_FULL))
st, _, _ = reachable(T, ALPH_FULL); vals = set()
for S in st.values():
    for j in range(2):
        for u in (XB(j), ZB(j)):
            vals.add(1 if d[u] in S else (-1 if E.mul[d[u]][E.z] in S else 0))
print("  K-STAB-GAP on the passing extension engine (C=Z2, ERT): %d reachable record states; elementary-relation expectations %s"
      % (len(st), sorted(vals)))
