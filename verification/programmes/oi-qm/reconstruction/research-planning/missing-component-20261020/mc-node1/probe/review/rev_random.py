"""Independent numeric checks (plain Python complex, seeded):
 C1  random TU protocols (arbitrary complex single- and two-token Lueders bases, random permutations,
     outcome-conditioned subtrees, configuration attach/discard) satisfy sum_i K_i^H 1 = 1 with the Lueders
     Kraus K = P (the projector itself) -- the readout-case identity of instAvail_onesNormal, transferred.
 C2  negative control: one Z inserted in one branch breaks it.
 C3  exhaustive search, 2 tokens from |00>, up to 3 Pauli-basis Lueders tests on either token with arbitrary
     outcome-conditioned permutation corrections (all 24): deterministic |-> on token 0?  Positive control |+i>."""
import random, cmath, math, itertools, sys
random.seed(20261020)
def mm(A, B): return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def H(A): return [[A[j][i].conjugate() for j in range(len(A))] for i in range(len(A[0]))]
def eye(n): return [[1.0 + 0j if i == j else 0j for j in range(n)] for i in range(n)]
def kron(A, B): return [[A[i // len(B)][j // len(B[0])] * B[i % len(B)][j % len(B[0])] for j in range(len(A[0]) * len(B[0]))] for i in range(len(A) * len(B))]
def mv(A, v): return [sum(A[i][k] * v[k] for k in range(len(v))) for i in range(len(A))]
def gs(vs):
    out = []
    for v in vs:
        for u in out:
            c = sum(u[k].conjugate() * v[k] for k in range(len(v))); v = [v[k] - c * u[k] for k in range(len(v))]
        n = math.sqrt(sum(abs(x) ** 2 for x in v)); out.append([x / n for x in v])
    return out
def rbasis(d): return gs([[complex(random.gauss(0, 1), random.gauss(0, 1)) for _ in range(d)] for _ in range(d)])
def proj(u): return [[u[i] * u[j].conjugate() for j in range(len(u))] for i in range(len(u))]
N = 3; D = 2 ** N
def perm_mat(p): return [[1.0 + 0j if p[j] == i else 0j for j in range(len(p))] for i in range(len(p))]
def embed_token_op(A, toks):
    """operator A on the tokens `toks` (len 1 or 2, in that order), identity elsewhere, on N qubits."""
    M = [[0j] * D for _ in range(D)]
    for x in range(D):
        bits = [(x >> (N - 1 - q)) & 1 for q in range(N)]
        sub_in = 0
        for q in toks: sub_in = 2 * sub_in + bits[q]
        for sub_out in range(2 ** len(toks)):
            a = A[sub_out][sub_in]
            if a == 0: continue
            nb = bits[:]
            for k, q in enumerate(toks): nb[q] = (sub_out >> (len(toks) - 1 - k)) & 1
            y = 0
            for b in nb: y = 2 * y + b
            M[y][x] += a
    return M
def rand_tree(depth, inject_Z=False):
    """returns list of Kraus operators (D x D) of a random protocol."""
    if depth == 0 or random.random() < 0.15:
        return [eye(D)]
    r = random.random()
    if r < 0.35:
        p = list(range(D)); random.shuffle(p)
        A = perm_mat(p)
        if inject_Z:
            A = mm(embed_token_op([[1, 0], [0, -1]], [0]), A)
        return [mm(K, A) for K in rand_tree(depth - 1)]
    toks = random.sample(range(N), random.choice([1, 2]))
    B = rbasis(2 ** len(toks))
    out = []
    for k, u in enumerate(B):
        Pk = embed_token_op(proj(u), toks)
        sub = rand_tree(depth - 1, inject_Z=(inject_Z and k == 0))
        out += [mm(K, Pk) for K in sub]
    return out
ones = [1.0 + 0j] * D
def defect(Ks):
    s = [0j] * D
    for K in Ks:
        v = mv(H(K), ones); s = [s[i] + v[i] for i in range(D)]
    return max(abs(s[i] - 1) for i in range(D))
def tp_defect(Ks):
    S = [[0j] * D for _ in range(D)]
    for K in Ks:
        M = mm(H(K), K); S = [[S[i][j] + M[i][j] for j in range(D)] for i in range(D)]
    return max(abs(S[i][j] - (1 if i == j else 0)) for i in range(D) for j in range(D))
ok = True
worst = 0; worst_tp = 0; nk = 0
for trial in range(150):
    Ks = rand_tree(5)
    worst = max(worst, defect(Ks)); worst_tp = max(worst_tp, tp_defect(Ks)); nk += len(Ks)
print('C1 150 random TU protocols (%d Kraus ops): max |sum K^H 1 - 1| = %.2e ; max |sum K^H K - I| = %.2e' % (nk, worst, worst_tp))
ok &= worst < 1e-9 and worst_tp < 1e-9
# with attach/discard of token 2 by configuration Kraus: K' = (I (x) <c|) K (I (x) |0>), carrier 4
def attach_discard(Ks):
    out = []
    for K in Ks:
        for c in (0, 1):
            Kp = [[K[2 * i + c][2 * j + 0] for j in range(4)] for i in range(4)]
            out.append(Kp)
    return out
w2 = 0
for trial in range(60):
    Ks = attach_discard(rand_tree(5))
    s = [0j] * 4
    for K in Ks:
        v = mv(H(K), [1.0 + 0j] * 4); s = [s[i] + v[i] for i in range(4)]
    w2 = max(w2, max(abs(x - 1) for x in s))
print('C1b 60 random protocols with attach |0>/configuration discard of token 2: max defect = %.2e' % w2)
ok &= w2 < 1e-9
# C2 negative control: Z injected in one branch
fired = 0; tries = 0
while tries < 60:
    random.seed(1000 + tries); tries += 1
    Ks = rand_tree(5, inject_Z=True)
    if defect(Ks) > 1e-6: fired += 1
print('C2 control: Z inserted in a branch -> invariant broken in %d of %d random protocols (some trees never reach the injection point)' % (fired, tries))
ok &= fired > 0
# ---- C3 exhaustive search, 2 qubits ----
s2 = 1 / math.sqrt(2)
bases = {'Z': [[1, 0], [0, 1]], 'X': [[s2, s2], [s2, -s2]], 'Y': [[s2, 1j * s2], [s2, -1j * s2]]}
perms2 = [perm_mat(p) for p in itertools.permutations(range(4))]
def apply(M, v): return [sum(M[i][k] * v[k] for k in range(4)) for i in range(4)]
def norm(v):
    n = math.sqrt(sum(abs(x) ** 2 for x in v)); v = [x / n for x in v]
    k = max(range(4), key=lambda i: abs(v[i]) - 1e-9 * i); ph = v[k] / abs(v[k])
    return tuple(complex(round((x / ph).real, 9), round((x / ph).imag, 9)) for x in v)
def tok_proj(u, tok):
    P1 = proj(u)
    return kron(P1, eye(2)) if tok == 0 else kron(eye(2), P1)
tests = [(tok, b, [tok_proj(u, tok) for u in bases[b]]) for tok in (0, 1) for b in 'XYZ']
def data_is(v, tgt):
    # token 0 reduced state pure = tgt  <=>  v = tgt (x) a  for some a
    a0 = sum(tgt[i].conjugate() * v[2 * i + 0] for i in range(2)); a1 = sum(tgt[i].conjugate() * v[2 * i + 1] for i in range(2))
    return abs(abs(a0) ** 2 + abs(a1) ** 2 - 1) < 1e-7
memo = {}
def win(v, k, tgt):
    key = (v, k, tgt)
    if key in memo: return memo[key]
    res = any(data_is(apply(Pm, v), tgt) for Pm in perms2)
    if not res and k > 0:
        for tok, b, Ps in tests:
            good = True
            for Pk in Ps:
                w = apply(Pk, v)
                if sum(abs(x) ** 2 for x in w) < 1e-12: continue
                wn = norm(w)
                if not any(win(norm(apply(Pm, list(wn))), k - 1, tgt) for Pm in perms2): good = False; break
            if good: res = True; break
    memo[key] = res; return res
start = norm([1, 0, 0, 0])
MINUS = (complex(s2), complex(-s2)); PLUSI = (complex(s2), complex(0, s2))
r_plusi = win(start, 2, PLUSI)
r_minus = [win(start, k, MINUS) for k in (1, 2, 3)]
print('C3 positive control: |+i> deterministic within 2 tests: %s ; |-> deterministic within 1/2/3 tests: %s ; memo states=%d'
      % (r_plusi, r_minus, len(memo)))
ok &= r_plusi and not any(r_minus)
print('SUMMARY', 'ALL PASS' if ok else 'FAIL')
sys.exit(0 if ok else 1)
