"""EQ4-SIX probe s3 -- the glue network contains the theta network; the PN_5 control.  Research only.

Usage:  python3 -I -B s3_glue_theta.py <base>/verification/lean-mathlib/OIBridge
Imports only the copied library eq4_lib.py (sha256 cc2c6aca94007ac8).

Glue network (crossing split, NOTES N1):  N(x, y, e, f; w, z) = tr[ Glue_e Glue_s ],
  Glue_s = tr_pq[(w_pq (x) 1)(x_{p r1 r2} (x) y_{q u1 u2})],  Glue_e = tr_st[(z_st (x) 1)(e_{s r1 u1} (x) f_{t r2 u2})].
Written claim W2 (NOTES N1.1).  With product effect nodes e = rho_s (x) eta_{r1 u1}, f = rho'_t (x) zeta_{r2 u2} (in BS,
hence in K3* whenever K3 <= BS*):  N = tr[z (rho (x) rho')] * tr[(w (x) eta (x) zeta)(x (x) y)]  — the theta network
of the states x, y with pair effects w, eta, zeta; with Bell w, eta, zeta it is (1/8) tr(x T(y')) (y' renamed).
Symmetrically, product state nodes reduce N to the theta network of the effects.  Hence (A4) together with (A1) implies
T-self-positivity of K3 and of K3*, i.e. K3 = T(K3*) (A3).  For the five-token countermodel PN (K3 = BS, K3* = BS*),
product states x = rho (x) Phi+, y = rho' (x) Phi+ and the effects GHZ, W3 (both in BS*) give a negative glue-network
value: PN violates (A4) at six tokens, through the same conflict as the theta network.

DECISION RULE (fixed before the first run; rules, not expected numbers).  VERDICT `S3-GLUE-THETA-EXACT` iff all:
  K  transcription control.
  A  identity (product effects): for 3 random exact (x, y) and random exact PSD rho, rho', eta, zeta, w, z the glue value
     equals tr[z (rho (x) rho')] * tr[(w (x) eta (x) zeta)(x (x) y)]  (exact equality).
  B  with Bell w, eta, zeta and z = Phi+, rho = rho' = 1/2 the value equals (1/4)(1/8) tr(x T(y renamed)) (exact, 3
     random instances); countercontrol: without T the value differs.
  C  identity (product states): x = rho_p (x) sigma_{r1 r2}, y = rho'_q (x) tau_{u1 u2} gives
     tr[w (rho (x) rho')] * tr[(e (x) f)(z (x) sigma (x) tau)] (exact, 3 random instances).
  P  PN control: x = (1/2) (x) Phi+_{r1 r2}, y = (1/2) (x) Phi+_{u1 u2}, e = GHZ_{s r1 u1}, f = W3_{t r2 u2}, Bell w, z:
     value < 0 (exact); same with e = f = W3: value >= 0; QM control e = f = GHZ: value >= 0.
"""
import random
import sys
from fractions import Fraction as Fr

sys.path.insert(0, __file__.rsplit("/", 1)[0] if "/" in __file__ else ".")
import eq4_lib as L  # noqa: E402

BASE = sys.argv[1]
rep = L.Report("s3_glue_theta")
rng = random.Random(2026100953)
rep.check("K0 transcription control", L.transcription_control(BASE)[0])
P_, Q_, R1, R2, U1, U2, S_, T_ = 10, 11, 12, 13, 14, 15, 16, 17


def rel(A, m, qs):
    return L.reorder(L.relabel(A, m), qs)


def glue(x, y, e, f, w, z):
    gs = L.cond(w, L.tensor(x, y))
    ge = L.cond(z, L.tensor(e, f))
    return L.pair(ge, gs)


ok_a = True
for _ in range(3):
    x = L.rand_op(rng, (P_, R1, R2))
    y = L.rand_op(rng, (Q_, U1, U2))
    rho = L.rand_psd(rng, (S_,), rank=1)
    rhop = L.rand_psd(rng, (T_,), rank=1)
    eta = L.rand_psd(rng, (R1, U1), rank=2)
    zeta = L.rand_psd(rng, (R2, U2), rank=2)
    w = L.rand_psd(rng, (P_, Q_), rank=2)
    z = L.rand_psd(rng, (S_, T_), rank=2)
    e = L.tensor(rho, eta)
    f = L.tensor(rhop, zeta)
    lhs = glue(x, y, e, f, w, z)
    rhs = L.pair(z, L.tensor(rho, rhop)) * L.pair(L.tensor(w, eta, zeta), L.tensor(x, y))
    ok_a &= lhs == rhs
rep.check("A product effect nodes: glue value = tr[z (rho (x) rho')] * theta(x, y; w, eta, zeta) (3 random exact "
          "instances)", ok_a)

ok_b = True
ok_bc = False
for _ in range(3):
    x = L.rand_op(rng, (P_, R1, R2))
    y = L.rand_op(rng, (Q_, U1, U2))
    half = L.identity((S_,)).scale(Fr(1, 2))
    e = L.tensor(half, L.phi_plus(R1, U1))
    f = L.tensor(L.identity((T_,)).scale(Fr(1, 2)), L.phi_plus(R2, U2))
    v = glue(x, y, e, f, L.phi_plus(P_, Q_), L.phi_plus(S_, T_))
    yren = rel(y, {Q_: P_, U1: R1, U2: R2}, (P_, R1, R2))
    pred = L.pair(x, L.transpose(yren)) * Fr(1, 32)
    ok_b &= v == pred
    if not (v == L.pair(x, yren) * Fr(1, 32)):
        ok_bc = True
rep.check("B Bell links and maximally mixed single effects: glue value = (1/4)(1/8) tr(x T(y)) (3 random exact "
          "instances); countercontrol without T differs", ok_b and ok_bc)

ok_c = True
for _ in range(3):
    rho = L.rand_psd(rng, (P_,), rank=1)
    rhop = L.rand_psd(rng, (Q_,), rank=1)
    sig = L.rand_psd(rng, (R1, R2), rank=2)
    tau = L.rand_psd(rng, (U1, U2), rank=2)
    e = L.rand_op(rng, (S_, R1, U1))
    f = L.rand_op(rng, (T_, R2, U2))
    w = L.rand_psd(rng, (P_, Q_), rank=2)
    z = L.rand_psd(rng, (S_, T_), rank=2)
    lhs = glue(L.tensor(rho, sig), L.tensor(rhop, tau), e, f, w, z)
    rhs = L.pair(w, L.tensor(rho, rhop)) * L.pair(L.tensor(e, f), L.tensor(z, sig, tau))
    ok_c &= lhs == rhs
rep.check("C product state nodes: glue value = tr[w (rho (x) rho')] * theta(e, f; z, sigma, tau) (3 random exact "
          "instances)", ok_c)

X3 = (0, 1, 2)
GHZ = L.ghz(X3)
W3 = L.w3(X3)
xs = L.tensor(L.identity((P_,)).scale(Fr(1, 2)), L.phi_plus(R1, R2))
ys = L.tensor(L.identity((Q_,)).scale(Fr(1, 2)), L.phi_plus(U1, U2))


def place(A, qs):
    return rel(A, {0: qs[0], 1: qs[1], 2: qs[2]}, qs)


vPN = glue(xs, ys, place(GHZ, (S_, R1, U1)), place(W3, (T_, R2, U2)), L.phi_plus(P_, Q_), L.phi_plus(S_, T_))
vWW = glue(xs, ys, place(W3, (S_, R1, U1)), place(W3, (T_, R2, U2)), L.phi_plus(P_, Q_), L.phi_plus(S_, T_))
vGG = glue(xs, ys, place(GHZ, (S_, R1, U1)), place(GHZ, (T_, R2, U2)), L.phi_plus(P_, Q_), L.phi_plus(S_, T_))
rep.check("P PN control: product states (1/2 (x) Phi+) with effects GHZ and W3 (both in BS* = K3* of PN) give %s < 0: "
          "PN violates (A4); W3, W3 give %s >= 0; QM GHZ, GHZ give %s >= 0" % (vPN, vWW, vGG),
          vPN.im == 0 and vPN.re < 0 and vWW.im == 0 and vWW.re >= 0 and vGG.im == 0 and vGG.re >= 0)
rep.verdict("S3-GLUE-THETA-EXACT")
