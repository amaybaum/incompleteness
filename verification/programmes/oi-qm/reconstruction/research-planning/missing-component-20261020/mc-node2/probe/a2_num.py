"""Node 2, part B [NUM]: an end-to-end instance of KrausDense for the TU theory, outcome by outcome.

Target: a two-outcome Kraus instrument F on the level-one carrier Fin 2 x Fin 1, with Stinespring
unitary U on (system qubit) x (ancilla qubit), carrier index 2*s + a. The available family is
  attach |0> -> composite channel C -> Lueders readout of the ancilla (configuration basis) -> discard,
where C replaces each letter of an exact word for U by its TU realization:
  X-letters exp(i phi X_ab): exact deterministic (gadget A2);
  P-letters exp(i t P_c):    the phase gadget A3 with its Z_c branch corrected by repeat-until-success
                             truncated at depth n (channel (1-2^(-n-1)) Ad D + 2^(-n-1) Ad(Z_c D), A6).
Mode CONT: the letter angles are exact (a continuum of real test bases).
Mode FIN:  only the bases X, Y and w(1) are used; each letter is a power of the fixed step
           exp(i X_ab) (angle 1) or D_c with relative phase pi/2 - 2, to tolerance delta.
Reported: eps_j = sqrt(2) * sigma_max(G_j - F_j), an upper bound for the ChanWithin constant of
outcome j (||Y||_op <= ||Y||_HS <= sqrt(2) ||Y||_op on 2x2 matrices). Floating point (mpmath, 40 digits):
evidence of approximation, never of exactness.
"""
import mpmath as mp

mp.mp.dps = 40
PASS = []
def check(name, cond):
    PASS.append(bool(cond)); print(("PASS " if cond else "FAIL ") + name)

d = 4
def eye(k): return mp.eye(k)
def kron(A, B):
    M = mp.matrix(A.rows * B.rows, A.cols * B.cols)
    for i in range(A.rows):
        for j in range(A.cols):
            for k in range(B.rows):
                for l in range(B.cols):
                    M[i * B.rows + k, j * B.cols + l] = A[i, j] * B[k, l]
    return M
def dag(A):
    M = mp.matrix(A.cols, A.rows)
    for i in range(A.rows):
        for j in range(A.cols):
            M[j, i] = mp.conj(A[i, j])
    return M
def conjm(A):
    M = mp.matrix(A.rows, A.cols)
    for i in range(A.rows):
        for j in range(A.cols):
            M[i, j] = mp.conj(A[i, j])
    return M
def sup_conj(K):           # vec(K X K^dag) = (conj(K) (x) K) vec X, column stacking
    return kron(conjm(K), K)
def maxabs(A):
    return max(abs(A[i, j]) for i in range(A.rows) for j in range(A.cols))
def opnorm(A):
    return max(mp.svd_c(A, compute_uv=False))

# --- the target ---------------------------------------------------------------------------
Hh = mp.matrix([[0.3, 0.2 - 0.7j, 0.5j, 0.1], [0.2 + 0.7j, -0.4, 0.6, -0.3j],
                [-0.5j, 0.6, 0.9, 0.25 + 0.15j], [0.1, 0.3j, 0.25 - 0.15j, -0.2]])
Hh = (Hh + dag(Hh)) / 2
U = mp.expm(1j * Hh)
check("T0 U is unitary", maxabs(dag(U) * U - eye(d)) < mp.mpf(10) ** -35)
def anc_bra(j):   # I_sys (x) <j| : 2 x 4
    M = mp.matrix(2, 4)
    for s in range(2): M[s, 2 * s + j] = 1
    return M
K = [anc_bra(j) * U * dag(anc_bra(0)) for j in range(2)]
check("T1 target Kraus completeness sum K_j^dag K_j = I", maxabs(dag(K[0]) * K[0] + dag(K[1]) * K[1] - eye(2)) < mp.mpf(10) ** -35)
F = [sup_conj(Kj) for Kj in K]
ones4 = mp.matrix([1, 1, 1, 1])
Uo = U * ones4
check("T2 K_0 has four nonzero entries (non-monomial) and U moves the all-ones ray of the carrier",
      sum(1 for i in range(2) for j in range(2) if abs(K[0][i, j]) > 1e-6) == 4 and
      max(abs(Uo[i] - Uo[0]) for i in range(4)) > 1e-3)

# --- exact word for U in X- and P-letters -----------------------------------------------------
def Xab(a, b):
    M = eye(d)
    M[a, a] = 0; M[b, b] = 0; M[a, b] = 1; M[b, a] = 1
    return M
def letterU(L):
    kind, a, b, ang = L
    if kind == 'X':
        return mp.cos(ang) * eye(d) + 1j * mp.sin(ang) * Xab(a, b)
    M = eye(d); M[a, a] = mp.expj(ang); return M
def two_level_word(G, a, b):
    """letters (applied right to left) equal to the two-level unitary G on the pair (a, b)."""
    c, s = abs(G[0, 0]), abs(G[0, 1])
    ea = 1j * G[0, 1] / s          # e^{ia}
    eb = G[1, 1] / c               # e^{ib}
    eac = G[0, 0] / c              # e^{i(a+c)}
    A, B, Cc = mp.arg(ea), mp.arg(eb), mp.arg(eac / ea)
    th = mp.atan2(s, c)            # Rx part [[cos, -i sin], [-i sin, cos]] = exp(-i th sigma_x)
    phi = -th
    comp = [x for x in range(d) if x not in (a, b)]
    word = [('P', a, None, A), ('P', b, None, B), ('X', a, b, phi)] + \
           [('P', x, None, -phi) for x in comp] + [('P', a, None, Cc)]
    return word
def mul_word(word):
    M = eye(d)
    for L in word:
        M = M * letterU(L)
    return M
# Givens elimination: G_r ... G_1 U = diagonal; U = G_1^dag ... G_r^dag diag
V = U.copy(); left = []
for j in range(d - 1):
    for i in range(d - 1, j, -1):
        x, y = V[i - 1, j], V[i, j]
        r = mp.sqrt(abs(x) ** 2 + abs(y) ** 2)
        if r < mp.mpf(10) ** -30: continue
        G2 = mp.matrix([[mp.conj(x) / r, mp.conj(y) / r], [-y / r, x / r]])
        Gf = eye(d)
        Gf[i - 1, i - 1] = G2[0, 0]; Gf[i - 1, i] = G2[0, 1]; Gf[i, i - 1] = G2[1, 0]; Gf[i, i] = G2[1, 1]
        V = Gf * V
        left.append((i - 1, i, dag(G2)))
word = []
for (a, b, G2) in left:                      # U = Gf_1^dag Gf_2^dag ... diag
    word += two_level_word(G2, a, b)
word += [('P', k, None, mp.arg(V[k, k])) for k in range(d)]
Uw = mul_word(word)
check(f"T3 exact word of {len(word)} letters reproduces U to 1e-30", maxabs(Uw - U) < mp.mpf(10) ** -30)
nP = sum(1 for L in word if L[0] == 'P'); nX = len(word) - nP
print(f"     word: {nX} X-letters (exact), {nP} P-letters (phase gadget + RUS)")

# --- channels ---------------------------------------------------------------------------------
def Pchan(c, t, n):
    D = eye(d); D[c, c] = mp.expj(t)
    Zc = eye(d); Zc[c, c] = -1
    q = mp.mpf(2) ** (-n - 1)
    return (1 - q) * sup_conj(D) + q * sup_conj(Zc * D)
def Pchan_uncorrected(c, t):
    D = eye(d); D[c, c] = mp.expj(t)
    Zc = eye(d); Zc[c, c] = -1
    return sup_conj(D) / 2 + sup_conj(Zc * D) / 2
def compose(word, n, uncorrected=False):
    C = eye(d * d)
    for L in word:              # U = W1 W2 ... WL : W_L acts first, so C = S1 S2 ... SL
        if L[0] == 'X':
            S = sup_conj(letterU(L))
        else:
            S = Pchan_uncorrected(L[1], L[3]) if uncorrected else Pchan(L[1], L[3], n)
        C = C * S
    return C
# attach |0><0| on the ancilla, Lueders readout j, discard
def attach():
    E = dag(anc_bra(0))                      # 4 x 2 isometry
    return sup_conj(E)                       # 16 x 4
def readdiscard(j):
    return sup_conj(anc_bra(j))              # 4 x 16 : X -> <j| X |j>
def instrument(C):
    A = attach()
    return [readdiscard(j) * C * A for j in range(2)]
def eps(G, Ft):
    return mp.sqrt(2) * opnorm(G - Ft)
vecI = mp.matrix([1, 0, 0, 1])
def tp_defect(Gs):
    S = Gs[0] + Gs[1]
    row = dag(vecI) * S
    return maxabs(row - dag(vecI))

print("Mode CONT (exact angles), per-outcome bounds eps_0, eps_1, and the coarse-grained one-outcome channel:")
prev = None; ok_dec = True; ok_tp = True
for n in (1, 2, 4, 8, 16, 32, 64):
    Gs = instrument(compose(word, n))
    e0, e1 = eps(Gs[0], F[0]), eps(Gs[1], F[1])
    ec = eps(Gs[0] + Gs[1], F[0] + F[1])
    ok_tp = ok_tp and tp_defect(Gs) < mp.mpf(10) ** -30
    print(f"  n={n:3d}  eps_0={mp.nstr(e0, 4):>10}  eps_1={mp.nstr(e1, 4):>10}  eps_coarse={mp.nstr(ec, 4):>10}"
          f"  nP*2^-n={mp.nstr(nP * mp.mpf(2) ** -n, 4)}")
    m = max(e0, e1)
    if prev is not None and not m < prev: ok_dec = False
    prev = m
    if n == 64: last = m; lastbound = nP * mp.mpf(2) ** -n * 2 * 4
check("T4 per-outcome error decreases strictly with the RUS depth n", ok_dec)
check("T5 every available family built is trace-preserving in aggregate (sum of outcomes)", ok_tp)
check("T6 at n = 64 both outcomes are within 1e-17 (bound scale nP * 2^-n)", last < mp.mpf(10) ** -17)
Gu = instrument(compose(word, 0, uncorrected=True))
eu = max(eps(Gu[0], F[0]), eps(Gu[1], F[1]))
print(f"  countercontrol, phase gadget without RUS correction: max eps = {mp.nstr(eu, 4)}")
check("T7 countercontrol: without the RUS correction the error stays of order one (> 0.05)", eu > 0.05)

# --- mode FIN ---------------------------------------------------------------------------------
TWO_PI = 2 * mp.pi
th0 = mp.pi / 2 - 2                       # relative phase of D_c at phi = 1
def best_power(target, step, tol, kmax):
    tf = float(mp.fmod(target, TWO_PI)); sf = float(step); tp = float(TWO_PI)
    best = None
    for k in range(1, kmax + 1):
        r = (k * sf - tf) % tp
        e = min(r, tp - r)
        if e < tol:
            return k
    return None
def matpow(M, k):
    R = eye(M.rows); B = M
    while k:
        if k & 1: R = R * B
        B = B * B; k >>= 1
    return R
def compose_fin(word, n, tol, kmax):
    C = eye(d * d); total_k = 0
    for L in word:
        if L[0] == 'X':
            k = best_power(L[3], mp.mpf(1), tol, kmax)
            S = matpow(sup_conj(letterU(('X', L[1], L[2], mp.mpf(1)))), k)
        else:
            k = best_power(L[3], th0, tol, kmax)
            S = matpow(Pchan(L[1], th0, n), k)
        total_k += k
        C = C * S
    return C, total_k
print("Mode FIN (bases X, Y, w(1) only; RUS depth n = 100):")
res = []
for tol in (mp.mpf('1e-2'), mp.mpf('1e-3'), mp.mpf('1e-4')):
    C, tk = compose_fin(word, 100, tol, 400000)
    Gs = instrument(C)
    e = max(eps(Gs[0], F[0]), eps(Gs[1], F[1]))
    res.append(e)
    print(f"  delta={mp.nstr(tol, 2):>6}  gadget applications={tk:8d}  max eps={mp.nstr(e, 4)}  "
          f"(<= 2 * {len(word)} letters * delta = {mp.nstr(2 * len(word) * tol, 3)})")
check("T8 mode FIN: the error tracks the angle tolerance and falls below 2 * letters * delta at each delta",
      all(res[i] <= 2 * len(word) * t for i, t in enumerate((mp.mpf('1e-2'), mp.mpf('1e-3'), mp.mpf('1e-4'))))
      and res[2] < res[1] < res[0])

# --- one-outcome target Ad Z on the system qubit (the A1 obstruction's own target) -------------
Zs = mp.matrix([[1, 0], [0, -1]])
def phi_n(n):
    q = mp.mpf(2) ** -n
    return (1 - q) * sup_conj(Zs) + q * eye(4)
vals = [eps(phi_n(n), sup_conj(Zs)) for n in (1, 4, 16)]
print("  Ad Z by RUS depth n=1,4,16: eps =", ", ".join(mp.nstr(v, 4) for v in vals))
check("T9 the one-outcome family Phi_n is within ChanWithin 2^(1-n) of Ad Z (HS-bound <= 2*sqrt2*2^-n)",
      all(v <= 2 * mp.sqrt(2) * mp.mpf(2) ** -n + mp.mpf(10) ** -30 for v, n in zip(vals, (1, 4, 16))))

print()
print(f"{sum(PASS)} PASS, {len(PASS) - sum(PASS)} FAIL")
