"""Independent [NUM] end-to-end KrausDense instance for TU (mc2), different target and outcome count from the node:
a THREE-outcome instrument (m = 3) on the level-one carrier C^2 (Fin 2 x Fin 1), Stinespring on C^2 (x) C^3 (d = 6).
Decomposition: own Givens/Euler (ZXZ) into exact X-flows exp(i t X_ab) and phase letters exp(i t P_c); every phase letter
replaced by the TU realization: corrected phase gadget = (1-2^-(n+1)) Ad D + 2^-(n+1) Ad(Z_c D)  (exact identity G4).
Per-outcome bound: eps_a = sqrt(2) * sigma_max(superop difference)  (valid: ||Y||_op <= ||Y||_HS <= sqrt2 ||Y||_op on 2x2).
Also FIN mode on d = 2: Euler angles realized by powers of the fixed steps (angle 1 for X, pi/2-2 for phases)."""
import cmath, math, random, sys
import mpmath as mp
random.seed(7)
def mm(A, B): return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def H(A): return [[A[j][i].conjugate() for j in range(len(A))] for i in range(len(A[0]))]
def eye(n): return [[1 + 0j if i == j else 0j for j in range(n)] for i in range(n)]
def add(A, B, a=1, b=1): return [[a * A[i][j] + b * B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def gs(cols, dim):
    out = []
    for v in cols:
        for u in out:
            c = sum(u[k].conjugate() * v[k] for k in range(dim)); v = [v[k] - c * u[k] for k in range(dim)]
        nv = math.sqrt(sum(abs(x) ** 2 for x in v))
        if nv > 1e-9: out.append([x / nv for x in v])
    return out
# target: random 3-outcome Kraus instrument on C^2 (K_j = j-th block of a random isometry C^2 -> C^2 (x) C^3)
dS, m = 2, 3; d = dS * m
cols = gs([[complex(random.gauss(0, 1), random.gauss(0, 1)) for _ in range(d)] for _ in range(2)], d)
# index convention: carrier index = s*m + j (system s, seed j)
Kr = [[[cols[c][s * m + j] for c in range(2)] for s in range(2)] for j in range(m)]
S = [[0j] * 2 for _ in range(2)]
for K in Kr: S = add(S, mm(H(K), K))
assert max(abs(S[i][j] - (i == j)) for i in range(2) for j in range(2)) < 1e-12
# Stinespring unitary U on C^6 with U|s,0> = sum_j K_j|s>|j>
basis = [[1.0 + 0j if k == i else 0j for k in range(d)] for i in range(d)]
full = gs(cols + basis, d)
U = [[0j] * d for _ in range(d)]
seed_cols = [s * m + 0 for s in range(2)]
others = [i for i in range(d) if i not in seed_cols]
for idx, c in enumerate(seed_cols):
    for r in range(d): U[r][c] = full[idx][r]
for idx, c in enumerate(others):
    for r in range(d): U[r][c] = full[2 + idx][r]
assert max(abs(x - (i == j)) for i, row in enumerate(mm(H(U), U)) for j, x in enumerate(row)) < 1e-10
# --- own decomposition: left-multiply Givens to reduce U to diagonal; each 2-level U(2) via ZXZ Euler with letters
def Xflow(a, b, t):   # exp(i t X_ab), X_ab = transposition matrix (identity off {a,b})
    M = [[cmath.exp(1j * t) if (i == j and i not in (a, b)) else 0j for j in range(d)] for i in range(d)]
    M[a][a] = M[b][b] = math.cos(t); M[a][b] = M[b][a] = 1j * math.sin(t); return M
def Pphase(c, t, dd=d):
    M = eye(dd); M[c][c] = cmath.exp(1j * t); return M
letters = []   # list of ('X',a,b,t) or ('P',c,t); product = letters applied left to right in time
def apply_letters(L):
    M = eye(d)
    for lt in L:
        G = Xflow(lt[1], lt[2], lt[3]) if lt[0] == 'X' else Pphase(lt[1], lt[2])
        M = mm(G, M)
    return M
def two_level(a, b, G):
    """letters (time order) realizing, up to global phase, the 2-level unitary G on span{a,b}, identity elsewhere.
    G = e^{i al} P(be) Xf(ga) P(de), P(t) = diag(1, e^{it}), Xf(g) = [[cos g, i sin g],[i sin g, cos g]]."""
    ga = math.acos(min(1.0, abs(G[0][0])))
    if abs(math.sin(ga)) < 1e-13:
        al = cmath.phase(G[0][0]); be = cmath.phase(G[1][1]) - al; de = 0.0
    elif abs(math.cos(ga)) < 1e-13:
        al = 0.0; be = cmath.phase(G[1][0]) - math.pi / 2; de = cmath.phase(G[0][1]) - math.pi / 2
    else:
        al = cmath.phase(G[0][0]); be = cmath.phase(G[1][0]) - al - math.pi / 2; de = cmath.phase(G[0][1]) - al - math.pi / 2
    return [('P', b, de), ('X', a, b, ga)] + [('P', c, -ga - al) for c in range(d) if c not in (a, b)] + [('P', b, be)]
work = [row[:] for row in U]
for col in range(d):
    for row in range(d - 1, col, -1):
        x, y = work[col][col], work[row][col]
        if abs(y) < 1e-14: continue
        r = math.sqrt(abs(x) ** 2 + abs(y) ** 2)
        G2 = [[x.conjugate() / r, y.conjugate() / r], [-y / r, x / r]]   # maps (x,y) -> (r,0)
        L = two_level(col, row, G2)
        Gfull = apply_letters(L)
        # verify Gfull equals G2 on {col,row} block up to global phase, identity elsewhere (up to same phase)
        ph = None; okb = True
        Gt = eye(d); Gt[col][col], Gt[col][row], Gt[row][col], Gt[row][row] = G2[0][0], G2[0][1], G2[1][0], G2[1][1]
        for i in range(d):
            for j in range(d):
                if abs(Gt[i][j]) > 1e-9:
                    ph = Gfull[i][j] / Gt[i][j]; break
            if ph: break
        if max(abs(Gfull[i][j] - ph * Gt[i][j]) for i in range(d) for j in range(d)) > 1e-9:
            # fall back: try conjugate Euler branch by brute search on beta/delta signs
            raise SystemExit('decomposition branch failed at (%d,%d)' % (col, row))
        letters += L; work = mm(Gt, work)
# remaining diagonal
for c in range(d):
    letters.append(('P', c, -cmath.phase(work[c][c])))
W = apply_letters(letters)   # W U = phase * I  ->  U = W^dag (up to phase)
ph = (mm(W, U))[0][0]
err_word = max(abs(x - ph * (i == j)) for i, row in enumerate(mm(W, U)) for j, x in enumerate(row))
print('N0 exact-angle word with %d letters (%d X, %d P): ||W U - c I||_max = %.1e' % (
    len(letters), sum(l[0] == 'X' for l in letters), sum(l[0] == 'P' for l in letters), err_word))
# invert: U ~ W^dag ; letters of W^dag = reversed letters with negated angles
inv = [(l[0], l[1], l[2], -l[3]) if l[0] == 'X' else (l[0], l[1], -l[2]) for l in reversed(letters)]
# --- channel simulation on 6x6 matrices
def conj(M, X): return mm(mm(M, X), H(M))
def phase_letter_channel(c, t, n, X):
    # realized via the gadget: D_c(phi) has relative phase i e^{-2i phi}; choose phi with that phase = t.
    D = Pphase(c, t); Zc = eye(d); Zc[c][c] = -1
    q = 2.0 ** (-(n + 1))
    return add(conj(D, X), conj(mm(Zc, D), X), 1 - q, q)
def run(X6, n):
    for lt in inv:
        if lt[0] == 'X': X6 = conj(Xflow(lt[1], lt[2], lt[3]), X6)
        else: X6 = phase_letter_channel(lt[1], lt[2], n, X6)
    return X6
def family(X2, n):
    X6 = [[0j] * d for _ in range(d)]
    for s in range(2):
        for t in range(2): X6[s * m][t * m] = X2[s][t]          # attach seed |0>
    Y = run(X6, n)
    outs = []
    for j in range(m):                                          # Lueders seed readout j, then discard seed
        outs.append([[Y[s * m + j][t * m + j] for t in range(2)] for s in range(2)])
    return outs
def target(X2): return [mm(mm(K, X2), H(K)) for K in Kr]
Eb = [[[1 + 0j if (i, j) == (a, b) else 0j for j in range(2)] for i in range(2)] for a in range(2) for b in range(2)]
def eps_per_outcome(n):
    cols_ = [family(Xb, n) for Xb in Eb]; tcols = [target(Xb) for Xb in Eb]
    res = []
    for a in range(m):
        M = mp.matrix(4, 4)
        for c in range(4):
            Dm = add(cols_[c][a], tcols[c][a], 1, -1)
            for r in range(4): M[r, c] = Dm[r // 2][r % 2]
        res.append(float(math.sqrt(2) * max(mp.svd_c(M, compute_uv=False))))
    return res
nP = sum(l[0] == 'P' for l in inv)
ok = True; prev = None
for n in (2, 6, 12, 24, 48):
    e = eps_per_outcome(n)
    print('N1 n=%2d  eps_a (a=0,1,2) = %s   bound-scale 3*nP*2^-n=%.2e' % (n, ['%.2e' % x for x in e], 3 * nP * 2.0 ** -n))
    ok &= (prev is None or max(e) < max(prev)); prev = e
ok &= max(prev) < 1e-12
# trace preservation in aggregate at n = 6
tp = max(abs(sum(sum(family(Xb, 6)[a][i][i] for i in range(2)) for a in range(m)) - sum(Xb[i][i] for i in range(2))) for Xb in Eb)
print('N2 aggregate trace preservation defect at n=6: %.1e' % tp); ok &= tp < 1e-12
# --- FIN mode on d = 2: approximate a random SU(2) by powers of exp(i X) (angle 1) and D (relative phase pi/2 - 2)
def best_power(target_angle, step, kmax):
    best = (9, 0)
    for k in range(kmax):
        e = abs(((k * step - target_angle + math.pi) % (2 * math.pi)) - math.pi)
        if e < best[0]: best = (e, k)
    return best
random.seed(11)
fin_ok = True
for kmax in (10 ** 3, 10 ** 4, 10 ** 5):
    errs = []
    for trial in range(5):
        al, be, ga = (random.uniform(-math.pi, math.pi) for _ in range(3))
        # target V = diag(1,e^{i al}) exp(i be X) diag(1, e^{i ga}); realize angles by powers
        e1, k1 = best_power(al, math.pi / 2 - 2, kmax); e2, k2 = best_power(be, 1.0, kmax); e3, k3 = best_power(ga, math.pi / 2 - 2, kmax)
        P_ = lambda t: [[1, 0], [0, cmath.exp(1j * t)]]
        Xf = lambda t: [[math.cos(t), 1j * math.sin(t)], [1j * math.sin(t), math.cos(t)]]
        V = mm(mm(P_(al), Xf(be)), P_(ga)); Va = mm(mm(P_(k1 * (math.pi / 2 - 2)), Xf(k2 * 1.0)), P_(k3 * (math.pi / 2 - 2)))
        Dm = add(V, Va, 1, -1)
        M = mp.matrix(2, 2)
        for i in range(2):
            for j in range(2): M[i, j] = Dm[i][j]
        errs.append(float(max(mp.svd_c(M, compute_uv=False))))
    print('N3 FIN d=2, powers up to %d: max ||V - V_word||_op over 5 random targets = %.2e' % (kmax, max(errs)))
    fin_ok &= max(errs) < 50.0 / kmax
ok &= fin_ok
print('SUMMARY', 'ALL PASS' if ok else 'FAIL'); sys.exit(0 if ok else 1)
