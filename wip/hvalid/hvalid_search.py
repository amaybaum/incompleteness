"""Thread A decisive test: does hvalid follow from availability plus PairCompat at k = 2?

Object (kernel, origin/main 66a981d5 and design PID @ c9f16498):
  hvalid    : prep ⊆ maxConeOf avail                (EqvK2MaxCone.lean:196, :209; PID:437)
  PairCompat: ∀ U ∈ 𝓘(Fin2×Fin2), UᴴU = 1 → ∀ ω ∈ prep, ∃ ω' ∈ prep, dict ω' = U dict ω Uᴴ   (PID:206)
  avail     : sharpFamily 3 ⊆ avail (or denseTests ⊆ avail), EffectsOn (eball 3) avail, MixingClosed, unit.
PairCompat is antitone in 𝓘, so fullClass (every matrix admitted) is the strongest premise;
a countermodel there is a countermodel for every class.

DECISION RULE (fixed before the run; no expected numbers):
  A candidate counts as a countermodel iff, by exact arithmetic,
    (i)  its generator set is closed under U(4) conjugation by construction (spectral cone), so
         PairCompat 𝓘 holds for every class [W], it contains Q3 (hence all products) and is a convex cone;
    (ii) every generator passes the exact marginal-validity test (both one-token marginals in the
         Lorentz cone) through every permutation conjugate, AND lies in K2 = {A2(dict ω) ⪰ 0};
    (iii) an exact witness gives a negative product-test value at a pair of sharp tests.
  Verdict INDEPENDENT iff at least one countermodel is found AND every control below is green.
  Verdict NO-COUNTERMODEL-IN-CLASS iff none is found with all controls green (a bounded statement).
  Any failed control voids the verdict.
"""
import sys, random
from fractions import Fraction as Fr
from itertools import combinations, permutations, product
sys.path.insert(0, __import__("os").path.dirname(__file__))
import qexact as q
from qexact import G
import os
MUT = os.environ.get("HVALID_MUTATION", "")
if MUT == "M1":   # dictionary normalization 1/2 instead of 1/4
    _d = q.dict_; q.dict_ = lambda w, scale=Fr(1, 2): _d(w, scale)
elif MUT == "M2": # sharp effect coefficients b instead of b/2
    q.sharpVec = lambda b: [Fr(1, 2)] + [Fr(c) for c in b]
elif MUT == "M3": # additive compound without its antisymmetric terms
    _A2 = q.A2
    def _bad(H):
        M = _A2(H); pairs = list(combinations(range(len(H)), 2))
        for r, (i, j) in enumerate(pairs):
            for c, (k, l) in enumerate(pairs):
                if j == k: M[r][c] = M[r][c] + H[i][l]
                if i == l: M[r][c] = M[r][c] + H[j][k]
        return M
    q.A2 = _bad
elif MUT == "M4": # control marginal read from the wrong index
    q.margA = lambda w: [w[0][m] for m in range(4)]
elif MUT == "M5": # tensor factors in the wrong order
    _k = q.kron; q.kron = lambda A, B: _k(B, A)

random.seed(20261017)
CHECKS = {"pass": 0, "fail": 0}
def chk(code, desc, ok, detail=""):
    CHECKS["pass" if ok else "fail"] += 1
    print(f"{'PASS' if ok else 'FAIL'} {code}: {desc}" + (f"  [{detail}]" if detail else ""))
    return ok

def rand_table(lo=-2, hi=2):
    return [[Fr(random.randint(lo, hi), random.choice([1, 2, 3])) for _ in range(4)] for _ in range(4)]
def rand_ball_pt():
    # rational points of the closed ball: a rational sphere point scaled by r in [0,1]
    s = q.rat_sphere(Fr(random.randint(-5, 5), random.randint(1, 4)), Fr(random.randint(-5, 5), random.randint(1, 4)))
    r = Fr(random.randint(0, 4), 4)
    return [r*c for c in s]
SPH = [q.rat_sphere(Fr(u), Fr(v)) for u in (-2, Fr(-1, 2), 0, Fr(1, 3), 1, 3) for v in (-1, 0, Fr(1, 2), 2)]
SPH += [[0, 0, 1], [0, 0, -1], [1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0]]
def rand_herm(k=2):
    A = q.zeros(4)
    for i in range(4):
        A[i][i] = G(random.randint(-k, k))
        for j in range(i+1, 4):
            z = G(random.randint(-k, k), random.randint(-k, k)); A[i][j] = z; A[j][i] = z.conj()
    return A
UNITARIES = [q.cayley(rand_herm(2)) for _ in range(10)]

def is_psd_fast(H):
    """Exact symmetric elimination test for Hermitian PSD (O(n^3))."""
    n = len(H); M = [r[:] for r in H]; alive = list(range(n))
    while alive:
        p = next((i for i in alive if M[i][i].re > 0), None)
        for i in alive:
            assert M[i][i].im == 0
            if M[i][i].re < 0: return False
        if p is None:
            return all(M[i][j].iszero() for i in alive for j in alive)
        alive.remove(p)
        for i in alive:
            f = M[i][p] / M[p][p]
            for j in alive:
                M[i][j] = M[i][j] - f * M[p][j]
    return True

def spec_value(ehat_a, ehat_b, w): return q.pairVal(ehat_a, ehat_b, w)

# ===================================================================== C: transcription controls
print("== C: transcription controls (the kernel's pair vocabulary)")
ok = all(q.coordOf(q.dict_(w)) == w for w in (rand_table() for _ in range(6)))
chk("C1", "coordOf (dict ω) = ω on 6 random rational tables (coordOf_dict)", ok)
ok = True
for _ in range(6):
    x, y = rand_ball_pt(), rand_ball_pt()
    D = q.dict_(q.prodState(x, y))
    tok = lambda v: q.madd(q.msc(Fr(1, 2), q.eye(2)), q.madd(q.msc(Fr(v[0], 2), q.PAULI[1]),
                    q.madd(q.msc(Fr(v[1], 2), q.PAULI[2]), q.msc(Fr(v[2], 2), q.PAULI[3]))))
    ok &= q.meq(D, q.kron(tok(x), tok(y))) and q.is_psd(D)
chk("C2", "dict (prodState x y) = tokMat(hom x) ⊗ tokMat(hom y), PSD, 6 random ball pairs (dict_prodState)", ok)
ok = True
for _ in range(8):
    a, b, x, y = random.choice(SPH), random.choice(SPH), rand_ball_pt(), rand_ball_pt()
    ok &= q.pairVal(q.sharpVec(a), q.sharpVec(b), q.prodState(x, y)) == q.eff_at(q.sharpVec(a), x) * q.eff_at(q.sharpVec(b), y)
chk("C3", "product law: prodEffVal (sharp a)(sharp b)(prodState x y) = sharp a x · sharp b y, 8 samples", ok)
def proj(a):
    return q.madd(q.msc(Fr(1, 2), q.eye(2)), q.madd(q.msc(Fr(a[0], 2), q.PAULI[1]),
                  q.madd(q.msc(Fr(a[1], 2), q.PAULI[2]), q.msc(Fr(a[2], 2), q.PAULI[3]))))
ok = True
for _ in range(8):
    a, b, w = random.choice(SPH), random.choice(SPH), rand_table()
    t = q.tr(q.mmul(q.kron(proj(a), proj(b)), q.dict_(w)))
    ok &= t.im == 0 and t.re == q.pairVal(q.sharpVec(a), q.sharpVec(b), w)
chk("C4", "table route = trace route: prodEffVal (sharp a)(sharp b) ω = tr((Π_a⊗Π_b) dict ω), 8 samples", ok)
ok = True; seen = set()
for _ in range(30):
    w = rand_table()
    r1 = q.lor(q.margA(w)) == q.is_psd(q.ptrace_B(q.dict_(w)))
    r2 = q.lor(q.margB(w)) == q.is_psd(q.ptrace_A(q.dict_(w)))
    ok &= r1 and r2; seen.add(q.lor(q.margA(w)))
chk("C5", "marginal route agreement: Lorentz test on ω(·,0), ω(0,·) = PSD test on tr_B, tr_A of dict ω (30 samples)",
    ok and seen == {True, False}, f"both outcomes seen: {seen == {True, False}}")
ok = True
for lam in [(-1, 1, 1, 1), (-2, 1, 1, 3), (0, 0, 1, 2), (-1, -1, 2, 5)]:
    A = q.A2(q.diagm(lam)); pairs = list(combinations(range(4), 2))
    ok &= all(A[r][c] == (G(lam[pairs[r][0]] + lam[pairs[r][1]]) if r == c else G(0)) for r in range(6) for c in range(6))
chk("C6a", "A2(diag λ) = diag(λ_a + λ_b, a<b) on 4 spectra (additive compound)", ok)
ok = True
for _ in range(6):
    H = rand_herm(2); U = random.choice(UNITARIES)
    ok &= q.is_psd(q.A2(H)) == q.is_psd(q.A2(q.conj_by(U, H)))
    ok &= q.charpoly(H) == q.charpoly(q.conj_by(U, H))
chk("C6b", "unitary conjugation preserves the characteristic polynomial and A2-PSD membership (6 samples)", ok)
ok = all(q.meq(q.mmul(q.dag(U), U), q.eye(4)) for U in UNITARIES)
chk("C7", "the 10 Cayley matrices are exactly unitary", ok)
ok = True
for _ in range(25):
    H = rand_herm(3); ok &= (is_psd_fast(H) == q.is_psd(H)) and (is_psd_fast(q.A2(H)) == q.is_psd(q.A2(H)))
chk("C8", "fast PSD test agrees with the principal-minor test (25 random Hermitian, on H and A2 H)", ok)

# ===================================================================== S1: spectral class, exhaustive box
print("== S1: U(4)-invariant spectral cones C_λ = cone(Q3 ∪ U(4)·diag λ), λ sorted in [-3,3]^4, tr > 0")
def perm_marginal_min(lam):
    best = None
    for p in permutations(range(4)):
        P = q.perm_matrix(p); H = q.conj_by(P, q.diagm(lam))
        w = q.coordOf(H)
        okm = q.mv_ok(w)
        vals = [H[0][0].re + H[1][1].re, H[2][2].re + H[3][3].re, H[0][0].re + H[2][2].re, H[1][1].re + H[3][3].re]
        m = min(vals)
        best = m if best is None else min(best, m)
        if not okm: return False, best
    return True, best
results = []; pc_ok = True; nc_ok = True; route_ok = True
for lam in product(range(-3, 4), repeat=4):
    if list(lam) != sorted(lam) or sum(lam) <= 0: continue
    D = q.diagm(lam); w = q.coordOf(D)
    mv_perm, mmin = perm_marginal_min(lam)
    k2 = q.is_psd(q.A2(D))
    route_ok &= (mv_perm == k2) and (mmin == lam[0] + lam[1])
    # hvalid witness: the permutation conjugate is diag itself with λ1 at |00>; z⊗z sharp test
    vz = q.pairVal(q.sharpVec([0, 0, 1]), q.sharpVec([0, 0, 1]), w)
    viol = vz < 0
    if lam[0] >= 0 and not viol:
        # sampled search for a violation (must find none, since C_λ = Q3 ⊆ maxCone)
        for U in UNITARIES[:6]:
            wu = q.coordOf(q.conj_by(U, D))
            for a in SPH[::3]:
                for b in SPH[::3]:
                    if q.pairVal(q.sharpVec(a), q.sharpVec(b), wu) < 0: viol = True
    pc_ok &= (viol == (lam[0] < 0))          # reproduces subset_Q3_of_maxCone_block's contrapositive + Q3 ⊆ maxCone
    cm = (k2 and mv_perm and viol) if MUT != "M6" else viol   # M6: decision rule without marginal validity
    if lam[0] + lam[1] < 0: nc_ok &= not cm   # negative control: marginal-invalid spectra are never counted
    if lam[0] >= 0: nc_ok &= not cm           # negative control: PSD spectra (valid) are never counted
    results.append((lam, k2, viol, cm, vz))
n_cm = sum(r[3] for r in results)
chk("S1.route", "two exact routes agree: permutation-conjugate marginal validity ⟺ A2(diag λ) ⪰ 0, min = λ1+λ2", route_ok)
chk("S1.PC", "positive control: violation found ⟺ λ1 < 0 on every spectrum (kernel subset_Q3_of_maxCone_block "
    "contrapositive for U(4)-invariant cones; none found for λ1 ≥ 0, consistent with Q3 ⊆ maxCone)", pc_ok)
chk("S1.NC", "negative control: no spectrum with λ1+λ2 < 0 or λ1 ≥ 0 is counted as a countermodel", nc_ok)
print(f"   S1 spectra examined: {len(results)}; countermodels (λ1 < 0 ≤ λ1+λ2): {n_cm}")
print(f"   S1 first countermodels: {[r[0] for r in results if r[3]][:6]}; z⊗z values: {[str(r[4]) for r in results if r[3]][:6]}")

# ===================================================================== CM-2: the Ky Fan cone K2 and its witness
print("== CM-2: K2 = {ω : A2(dict ω) ⪰ 0}; witness ω* = coordOf diag(-1,1,1,1)")
Wst = q.coordOf(q.diagm((-1, 1, 1, 1)))
print("   ω* table:", [[str(c) for c in row] for row in Wst])
chk("CM2.a", "ω* ∈ K2 (A2 PSD), ω* ∉ Q3", q.in_K2(Wst) and not q.in_Q3(Wst))
chk("CM2.b", "ω* has valid one-token marginals (Lorentz)", q.mv_ok(Wst), f"margA={[str(c) for c in q.margA(Wst)]}")
vz = q.pairVal(q.sharpVec([0, 0, 1]), q.sharpVec([0, 0, 1]), Wst)
chk("CM2.c", "prodEffVal (sharp z3)(sharp z3) ω* < 0, so ω* ∉ maxConeOf avail for any avail ∋ sharp z3", vz < 0, f"value {vz}")
ok = True; negs = 0
for U in UNITARIES:
    wu = q.coordOf(q.conj_by(U, q.diagm((-1, 1, 1, 1))))
    ok &= q.in_K2(wu) and q.mv_ok(wu)
    negs += any(q.pairVal(q.sharpVec(a), q.sharpVec(b), wu) < 0 for a in SPH[::2] for b in SPH[::2])
chk("CM2.d", "orbit control: 10 Cayley images of ω* stay in K2 with valid marginals (PairCompat fullClass on samples)", ok,
    f"{negs}/10 images also show a negative sharp product value on the sampled grid")
ok = True
gens = [q.coordOf(q.diagm((-1, 1, 1, 1)))] + [q.prodState(rand_ball_pt(), rand_ball_pt()) for _ in range(3)]
gens += [q.coordOf(q.conj_by(U, q.diagm((-1, 1, 1, 1)))) for U in UNITARIES[:3]]
for g1, g2 in combinations(gens, 2):
    s = [[g1[m][n] + g2[m][n] for n in range(4)] for m in range(4)]
    ok &= q.in_K2(s) and q.mv_ok(s)
chk("CM2.e", "cone control: 21 pairwise sums of K2 generators (products and orbit points) stay in K2 with valid marginals", ok)
ok = all(q.in_K2(q.prodState(rand_ball_pt(), rand_ball_pt())) for _ in range(5))
chk("CM2.f", "products of ball states lie in K2 (5 samples)", ok)
Wbad = q.coordOf(q.diagm((-2, 1, 1, 1)))
chk("CM2.g", "maximality negative control: diag(-2,1,1,1) ∉ K2 and its own A-marginal is invalid", (not q.in_K2(Wbad)) and not q.mv_ok(Wbad))

# ===================================================================== S2: seeded with #820's fixtures
print("== S2: #820 fixtures K_B = SEP + R+ B and K(Z_F) = (Q3 ∩ Z_F*) + cone(Z_F), closed under fullClass")
Bvec = [G(1), G(0), G(0), G(1)]
B = [[Bvec[i]*Bvec[j].conj()*Fr(1, 2) for j in range(4)] for i in range(4)]
wB = q.coordOf(B)
chk("S2.B", "B = |00+11><00+11|/2 is PSD of rank one, so U(4)·B ⊆ Q3: closure of K_B under fullClass is Q3 (valid)",
    q.in_Q3(wB) and q.det(B) == 0 and q.tr(B) == 1)
defects = {}
for s, t in product((1, -1), repeat=2):
    z = [[Fr(0)]*4 for _ in range(4)]
    z[0][0] = Fr(1, 4); z[1][3] = Fr(s, 4); z[2][2] = Fr(t, 4); z[3][1] = Fr(-s*t, 4)
    defects[(s, t)] = z
ok = True
for (s, t), z in defects.items():
    e = q.dict_(z)
    target = q.msc(Fr(1, 16), q.madd(q.eye(4), q.madd(q.msc(s, q.PT[1][3]), q.madd(q.msc(t, q.PT[2][2]), q.msc(-s*t, q.PT[3][1])))))
    ok &= q.meq(e, target)
chk("S2.Z0", "dict z_(s,t) = (I + s X⊗Z + t Y⊗Y - st Z⊗X)/16 for all four sign pairs (#820 result.md:202-204)", ok)
ok = True
for (s, t), z in defects.items():
    cp = q.charpoly(q.dict_(z))   # (t + 1/8)(t - 1/8)^3 = t^4 - (1/4) t^3 + 0 t^2 + (1/256)... compare exactly
    ref = q.charpoly(q.diagm((Fr(-1, 8), Fr(1, 8), Fr(1, 8), Fr(1, 8))))
    ok &= cp == ref and q.in_K2(z) and not q.in_Q3(z) and q.mv_ok(z)
    ok &= all(q.pairVal(q.sharpVec(a), q.sharpVec(b), z) >= 0 for a in SPH for b in SPH)
chk("S2.Z1", "each defect: spectrum (-1/8, 1/8, 1/8, 1/8) exactly, in K2 (boundary), not in Q3, valid marginals, "
    "nonnegative on the sampled sharp product grid (block-positive per #820 [W])", ok)
# explicit unitary: columns 2 P_i |00>, P_i = I/2 - 4 e_i (#820 spectrality.md:90-93)
cols = []
order = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
for st in order:
    P = q.msub(q.msc(Fr(1, 2), q.eye(4)), q.msc(4, q.dict_(defects[st])))
    cols.append([2*P[i][0] for i in range(4)])
Ucols = [[cols[j][i] for j in range(4)] for i in range(4)]
unit_ok = q.meq(q.mmul(q.dag(Ucols), Ucols), q.eye(4))
e11 = q.dict_(defects[(1, 1)])
Dg = q.mmul(q.mmul(q.dag(Ucols), e11), Ucols)
diag_entries = [Dg[i][i] for i in range(4)]
offdiag_zero = all(Dg[i][j].iszero() for i in range(4) for j in range(4) if i != j)
idx = next(i for i in range(4) if Dg[i][i] == G(Fr(-1, 8)))
p = list(range(4)); p[0], p[idx] = p[idx], p[0]
V = q.mmul(q.perm_matrix(p), q.dag(Ucols))     # V e11 V† has -1/8 at |00>
wV = q.coordOf(q.conj_by(V, e11))
vV = q.pairVal(q.sharpVec([0, 0, 1]), q.sharpVec([0, 0, 1]), wV)
chk("S2.Z2", "seeded countermodel: V (exact unitary from the Bell-type columns) diagonalizes e_(1,1); V e V† ∈ K2, "
    "valid marginals, and its z3⊗z3 sharp value is -1/8", unit_ok and offdiag_zero and q.in_K2(wV) and q.mv_ok(wV) and vV == Fr(-1, 8),
    f"diag {diag_entries}; value {vV}")

# ===================================================================== S3: structured Pauli-support box
print("== S3: tables ω00 = a ∈ {1,2,3,4}, at most three non-identity Pauli coefficients ±1 (exhaustive)")
strings = [(m, n) for m in range(4) for n in range(4) if (m, n) != (0, 0)]
cnt = {"total": 0, "Q3": 0, "K2notQ3": 0, "outside": 0, "tried": 0, "witnessed": 0, "nowitness_in_box": 0}
first_cm = []
def householder_witness(H):
    """Search v in {-1,0,1}+i{-1,0,1} with rational norm and v†Hv < 0; return exact unitary V with (V H V†)_00 < 0."""
    for v in product([G(0), G(1), G(-1), G(0, 1), G(0, -1), G(1, 1), G(1, -1)], repeat=4):
        n2 = sum(x.n2() for x in v)
        if n2 == 0: continue
        r = next((k for k in range(1, 20) if k*k == n2), None)
        if r is None: continue
        hv = sum((v[i].conj()*H[i][j]*v[j] for i in range(4) for j in range(4)), G())
        if hv.re >= 0: continue
        if not (v[0].re == 0 or v[0].im == 0) or (not v[0].iszero() and v[0].n2() not in (1, 4)): continue
        ph = G(1) if v[0].iszero() else v[0] / G(Fr(1) if v[0].n2() == 1 else Fr(2))
        wv = [v[i] - (G(r)*ph if i == 0 else G(0)) for i in range(4)]
        ww = sum(x.n2() for x in wv)
        if ww == 0:
            Vm = q.eye(4)
        else:
            Vm = q.msub(q.eye(4), [[wv[i]*wv[j].conj()*Fr(2)/ww for j in range(4)] for i in range(4)])
        if not q.meq(q.mmul(q.dag(Vm), Vm), q.eye(4)): continue
        val = q.conj_by(Vm, H)[0][0]
        if val.re < 0: return Vm, val.re
    return None, None
for k in (1, 2, 3):
    for S in combinations(strings, k):
        for sg in product((1, -1), repeat=k):
            for a in (1, 2, 3, 4):
                w = [[Fr(0)]*4 for _ in range(4)]; w[0][0] = Fr(a)
                for (m, n), sgn in zip(S, sg): w[m][n] = Fr(sgn)
                H = q.dict_(w); cnt["total"] += 1
                if is_psd_fast(H): cnt["Q3"] += 1; continue
                if is_psd_fast(q.A2(H)):
                    cnt["K2notQ3"] += 1
                    if cnt["tried"] < 60:
                        cnt["tried"] += 1
                        Vm, val = householder_witness(H)
                        if Vm is not None:
                            wv = q.coordOf(q.conj_by(Vm, H))
                            if q.mv_ok(wv) and q.pairVal(q.sharpVec([0, 0, 1]), q.sharpVec([0, 0, 1]), wv) < 0:
                                cnt["witnessed"] += 1; first_cm.append((S, sg, a, val))
                        else:
                            cnt["nowitness_in_box"] += 1
                else:
                    cnt["outside"] += 1
print("   S3 counts:", cnt)
print("   S3 first witnessed countermodel generators (support, signs, a, (VHV†)_00):",
      [(s, g, a, str(v)) for s, g, a, v in first_cm[:4]])
chk("S3.W", "the first 60 K2∖Q3 generators were tried for an exact Householder witness (v in a small Gaussian box with "
    "perfect-square norm); every witness found has valid marginals after conjugation and a negative z3⊗z3 value",
    cnt["witnessed"] + cnt["nowitness_in_box"] == cnt["tried"] and cnt["witnessed"] > 0,
    f"tried {cnt['tried']}, witnessed {cnt['witnessed']}, no witness in the small box {cnt['nowitness_in_box']}")

# ===================================================================== S4: the sourcing implication's controls
print("== S4: JS (stage-test validity) + local compatibility + availOf ⟹ hvalid [W]: controls")
# CM-4: stage tests {±z3 sharp, unit}; prep = cone(Q3 ∪ {ω_x}), ω_x = coordOf(I + 2 X⊗X)
Hx = q.madd(q.eye(4), q.msc(2, q.PT[1][1])); wx = q.coordOf(Hx)
stage = [q.sharpVec([0, 0, 1]), q.sharpVec([0, 0, -1]), q.UNIT]
js = all(q.pairVal(e, f, wx) >= 0 for e in stage for f in stage)
vxx = q.pairVal(q.sharpVec([1, 0, 0]), q.sharpVec([-1, 0, 0]), wx)
Hd = [[G(1), G(1)], [G(1), G(-1)]]   # sqrt(2)·Hadamard; conjugation by (Hd⊗Hd)/2 is unitary
Hd2 = q.msc(Fr(1, 2), q.kron(Hd, Hd))
wrot = q.coordOf(q.conj_by(Hd2, Hx))
js_rot = all(q.pairVal(e, f, wrot) >= 0 for e in stage for f in stage)
chk("S4.CM4", "local compatibility is load-bearing: ω_x = coordOf(I + 2X⊗X) passes every stage-test product "
    "(±z3, unit) and has valid marginals, yet sharp x ⊗ sharp(-x) is negative; its local Hadamard image fails a z3 stage product",
    js and q.mv_ok(wx) and vxx < 0 and not js_rot and q.meq(q.mmul(q.dag(Hd2), Hd2), q.eye(4)),
    f"x⊗(-x) value {vxx}")
# positive controls: Q3 samples, SEP (products), classical M_class pass JS and the sampled hvalid grid
ok = True
for _ in range(6):
    A = rand_herm(2); P = q.mmul(A, q.dag(A)); wp = q.coordOf(P)
    ok &= all(q.pairVal(q.sharpVec(a), q.sharpVec(b), wp) >= 0 for a in SPH[::2] for b in SPH[::2])
    U = random.choice(UNITARIES); ok &= q.is_psd(q.conj_by(U, P))
chk("S4.PC", "positive control: 6 random PSD tables are nonnegative on the sampled sharp grid and stay PSD under "
    "Cayley unitaries (pairCompat_Q3 [D PID:286] on samples)", ok)
cls = [q.prodState([0, 0, s], [0, 0, t]) for s in (1, -1) for t in (1, -1)]
ok = all(q.pairVal(q.sharpVec(a), q.sharpVec(b), w) >= 0 for w in cls for a in SPH for b in SPH)
chk("S4.CL", "classical comparison: the four products of ±z3 (M_class generators) pass the whole sampled sharp grid", ok)

# ===================================================================== S5: four-copy coherence (FCC)
print("== S5: FCC (FourCopyCoherent, FourCopyDefs.lean:56-60 @ ff9c3a35)")
def tabMul(A, B): return [[sum(A[m][k]*B[k][n] for k in range(4)) for n in range(4)] for m in range(4)]
def tabT(A): return [[A[n][m] for n in range(4)] for m in range(4)]
def ipW(E, X): return sum(E[m][n]*X[m][n] for m in range(4) for n in range(4))
def famI(X, Y, E, F): return ipW(X, tabMul(tabMul(E, Y), tabT(F)))
def fourVal(X, Y, E, F):
    return sum(X[a][b]*Y[c][d]*E[a][c]*F[b][d] for a in range(4) for b in range(4) for c in range(4) for d in range(4))
phiW = [[Fr(0)]*4 for _ in range(4)]
for m in range(4): phiW[m][m] = Fr(-1) if m == 2 else Fr(1)
Ecc = [[c/4 for c in row] for row in phiW]
Ftw = [[Fr(0)]*4 for _ in range(4)]
for m, v in enumerate((1, -1, 1, -1)): Ftw[m][m] = Fr(v, 4)
reflY = [1, 1, -1, 1]      # homMap of reflY = diag(1,-1,1) on Fin 3
actT_reflY = lambda w: [[w[m][n]*reflY[n] for n in range(4)] for m in range(4)]
v10 = famI(phiW, phiW, Ecc, Ftw)
chk("S5.F10", "reproduce KT4-PREM-1 F10: famI(phiW, phiW, phiW/4, diag(1,-1,1,-1)/4) = -1/8, with phiW ∈ Q3, "
    "phiW/4 ∈ dualW Q3, F ∈ dualW twin (actT reflY F ∈ Q3)",
    v10 == Fr(-1, 8) and q.in_Q3(phiW) and q.in_Q3(Ecc) and q.in_Q3(actT_reflY(Ftw)) and famI(phiW, phiW, Ecc, Ftw) == fourVal(phiW, phiW, Ecc, Ftw),
    f"value {v10}")
# cross route: fourVal = 16 tr((dict E on 02 ⊗ dict F on 13)(dict X on 01 ⊗ dict Y on 23))
def reorder_0213(M):
    # M acts on (0,2,1,3) ordering; return the operator on (0,1,2,3)
    def idx(bits): return bits[0]*8 + bits[1]*4 + bits[2]*2 + bits[3]
    out = q.zeros(16)
    for r in product((0, 1), repeat=4):
        for c in product((0, 1), repeat=4):
            out[idx(r)][idx(c)] = M[idx((r[0], r[2], r[1], r[3]))][idx((c[0], c[2], c[1], c[3]))]
    return out
ok = True
for _ in range(2):
    X, Y, E, F = rand_table(), rand_table(), rand_table(), rand_table()
    rho = q.kron(q.dict_(X), q.dict_(Y)); M = reorder_0213(q.kron(q.dict_(E), q.dict_(F)))
    t = q.tr(q.mmul(M, rho)); ok &= t.im == 0 and 16*t.re == fourVal(X, Y, E, F)
chk("S5.X", "cross route: fourVal = 16 · tr(M ρ) on 16×16 matrices (2 random rational quadruples)", ok)
# FCC ⟹ pair maxCone, spectator-unit specialization [W]: fourVal(X, Y, ê⊗û, f̂⊗û) = prodEffVal e f X · Y_00
ok = True
for _ in range(5):
    X, Y = rand_table(), rand_table(); a, b = random.choice(SPH), random.choice(SPH)
    E = [[q.sharpVec(a)[m]*q.UNIT[n] for n in range(4)] for m in range(4)]
    F = [[q.sharpVec(b)[m]*q.UNIT[n] for n in range(4)] for m in range(4)]
    ok &= famI(X, Y, E, F) == q.pairVal(q.sharpVec(a), q.sharpVec(b), X) * Y[0][0]
chk("S5.ID", "identity: famI(X, Y, ê⊗û, f̂⊗û) = prodEffVal e f X · Y00 (5 random rational samples)", ok)
E = [[q.sharpVec([0, 0, 1])[m]*q.UNIT[n] for n in range(4)] for m in range(4)]
Y0 = q.prodState([0, 0, 1], [0, 0, 1])
dual_ok = all(ipW(E, g) >= 0 for g in [Wst] + [q.coordOf(q.conj_by(U, q.diagm((-1, 1, 1, 1)))) for U in UNITARIES])
vK2 = famI(Wst, Y0, E, E)
chk("S5.K2", "uniform K2 violates FCC: ẑ⊗û is nonnegative on ω* and its 10 Cayley images (it lies in dualW K2 by marginal "
    "validity [W]); famI(ω*, prodState z3 z3, ẑ⊗û, ẑ⊗û) < 0", dual_ok and vK2 < 0, f"value {vK2}")
ok = True
for _ in range(4):
    Ps = []
    for _ in range(4):
        A = rand_herm(1); Ps.append(q.coordOf(q.mmul(A, q.dag(A))))
    ok &= famI(*Ps) >= 0
chk("S5.PC", "positive control: uniform Q3 passes famI on 4 random PSD quadruples (Kronecker positivity [W])", ok)

# ===================================================================== verdict
print("== verdict")
green = CHECKS["fail"] == 0
found = n_cm > 0 or cnt["witnessed"] > 0
if not green:
    print(f"VOID: {CHECKS['fail']} control(s) failed; no verdict.")
elif found:
    print(f"VERDICT INDEPENDENT: {n_cm} spectral countermodels (S1), the fullClass closure of K(Z_F) (S2), and "
          f"{cnt['K2notQ3']} K2∖Q3 generators in the S3 box ({cnt['witnessed']} with an explicit unitary witness).")
else:
    print("VERDICT NO-COUNTERMODEL-IN-CLASS (bounded; shows nothing universal)")
print(f"checks: {CHECKS['pass'] + CHECKS['fail']}, failures: {CHECKS['fail']}")
