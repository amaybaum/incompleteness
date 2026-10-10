"""z4_fe.py -- thread Z, finite extensions of G16 (FE): Clifford-type groups, the Bell-defect conjecture, exact seeds.

Groups of table maps (signed permutations, as in z1): G16 = <cnot, Ad(ZI), Ad(IZ), T>; G_H = <G16, Ad(I(x)H)>;
G_S = <G16, Ad(S(x)I)> (S = diag(1, i), a quarter turn of the S2 torus); G_Cl = <cnot, Ad(HI), Ad(IH), Ad(SI), Ad(IS), T>
(the two-qubit Clifford group with the transpose: its 'even' part, i.e. unitary or antiunitary conjugations).
For a pure state psi with table T, m_G(psi) = max_{g in G} sum_{mu=1..3} ((g T)_{mu 0})^2 (squared length of the
token-1 Bloch vector of the image); f_G(psi) = max over R(G) of |<psi|phi>|^2 = (1 + sqrt(m_G))/2 [W: largest Schmidt
coefficient = (1 + |r|)/2]. Bell-type defect for G <=> a maximally entangled psi with m_G(psi) = 0.
DECISION RULE (fixed before the first run). PASS/FAIL per line, exact (sympy rationals, integer signed permutations).
  F1  the new generators Ad(IH), Ad(SI), Ad(IS) equal their conjugation formulas on all 16 basis tables.
  F2  orders: |G16| = 16; |G_H|, |G_S| finite (printed); |G_Cl| = 23040 (= 2 x 11520); G16 <= G_H, G_S <= G_Cl;
      <G16, SWAP> <= Stab_Cl(Z_F) := {g in G_Cl : g permutes Z_F} (order printed).
  F3  conjecture test, symbolic: for T = E00 + sum C_ij E_ij (any maximally entangled psi: zero marginals), the token
      marginals of cnot T and of cnot Ad(IH) T contain +-C_11, +-C_21, +-C_31 (the whole first column of C).
      With [W] C orthogonal for maximally entangled psi, no psi has a maximally entangled G_H-orbit: G_H (finite,
      contains G16) excludes all Bell-type defects; so does every group containing G_H (e.g. G_Cl).
  F4  Bell seeds where they exist: psi_F = (1, 1, 1, -1)/2 (F's state) has m_{G16} = m_{G_S} = 0; the G_S-orbit of
      e_F has a pair with ipW = 1/8 (squared overlap 1/2), so it is not orthogonal (SD2 does not apply).
  F5  general seeds: candidates in fixed order psi_a = (15,-1,7,7)/18, psi_b = (1,2,3,4)/sqrt30, psi_c = (4,3i,2,1)/sqrt30;
      for G in (G_H, G_Cl) the first candidate with m_G < 1 is used, with alpha the first of (3/4, 4/5, 5/6, 7/8,
      9/10, 19/20, 99/100) with (2 alpha - 1)^2 >= m_G; then e = alpha E00 - T_psi/4 is a seed (claim D).
  F6  K(Z_F) is invariant under Stab_Cl(Z_F) (all elements permute Z_F; they are Q3-automorphisms by F1/z1).
 Countercontrols (each must be REJECTED):
  CC1 a product state has m = 1 for every group (never certified as a seed).
  CC2 for psi_F and G_H: m > 0 (psi_F is a Bell seed for G16 but not for G_H), consistent with F3.
  CC3 a wrong table map for Ad(SI) (one sign flipped) fails the conjugation test of F1.
  CC4 alpha = 1/2 (Bell normalization) is not admissible for the chosen general seed of G_H: (2 alpha - 1)^2 = 0 < m.
VERDICT 'VERDICT FE-...' only if all checks PASS and all countercontrols are REJECTED; else 'VERDICT FE-FAILED'.
"""
import sympy as sp

I, R = sp.I, sp.Rational
s0 = sp.eye(2)
sx = sp.Matrix([[0, 1], [1, 0]])
sy = sp.Matrix([[0, -I], [I, 0]])
sz = sp.Matrix([[1, 0], [0, -1]])
SIG = [s0, sx, sy, sz]
kr = sp.kronecker_product
KR = [[kr(SIG[m], SIG[n]) for n in range(4)] for m in range(4)]
results = []


def check(name, ok, note=''):
    results.append((name, bool(ok)))
    print(f"{name:5s} {'PASS' if ok else 'FAIL'}  {note}")


def pauliW(w):
    return sum((w[4 * m + n] * KR[m][n] for m in range(4) for n in range(4)), sp.zeros(4)) / 4


def table(rho):
    return [sp.expand((rho * KR[m][n]).trace()) for m in range(4) for n in range(4)]


def sp_map(f):
    return tuple((4 * f(m, n)[1] + f(m, n)[2], f(m, n)[0]) for m in range(4) for n in range(4))


PC = [[0, 0, 3, 3], [1, 1, 2, 2], [2, 2, 1, 1], [3, 3, 0, 0]]
PT = [[0, 1, 2, 3], [1, 0, 3, 2], [1, 0, 3, 2], [0, 1, 2, 3]]
CNOT_T = sp_map(lambda m, n: (-1 if (m, n) in ((1, 3), (2, 2)) else 1, PC[m][n], PT[m][n]))
ZI = sp_map(lambda m, n: (-1 if m in (1, 2) else 1, m, n))
IZ = sp_map(lambda m, n: (-1 if n in (1, 2) else 1, m, n))
TT = sp_map(lambda m, n: ((-1) ** ((m == 2) + (n == 2)), m, n))
SW = sp_map(lambda m, n: (1, n, m))
ID = tuple((k, 1) for k in range(16))


def local_perm(u):
    """k -> (sign, j) with u s_k u^* = sign s_j (k = 0..3)."""
    out = {0: (1, 0)}
    for k in (1, 2, 3):
        img = u * SIG[k] * u.H
        for j in (1, 2, 3):
            for sg in (1, -1):
                if sp.expand(img - sg * SIG[j]) == sp.zeros(2):
                    out[k] = (sg, j)
    return out


def local_map(u, token):
    p = local_perm(u)
    inv = {p[k][1]: (p[k][0], k) for k in range(4)}
    if token == 0:
        return sp_map(lambda m, n: (inv[m][0], inv[m][1], n))
    return sp_map(lambda m, n: (inv[n][0], m, inv[n][1]))


Hm = sp.Matrix([[1, 1], [1, -1]]) / sp.sqrt(2)
Sm = sp.diag(1, I)
HI, IH, SI, IS = local_map(Hm, 0), local_map(Hm, 1), local_map(Sm, 0), local_map(Sm, 1)


def act(g, w):
    return [g[k][1] * w[g[k][0]] for k in range(16)]


def comp(g, h):
    return tuple((h[g[k][0]][0], g[k][1] * h[g[k][0]][1]) for k in range(16))


def closure(gens):
    seen, frontier = {ID}, [ID]
    while frontier:
        nxt = []
        for a in frontier:
            for gg in gens:
                b = comp(gg, a)
                if b not in seen:
                    seen.add(b)
                    nxt.append(b)
        frontier = nxt
    return seen


E = [[1 if k == j else 0 for k in range(16)] for j in range(16)]


def conj_ok(g, U):
    return all(sp.expand(pauliW(act(g, E[j])) - U * pauliW(E[j]) * U.H) == sp.zeros(4) for j in range(16))


print('== F1  new generators as conjugations')
okF1 = conj_ok(IH, kr(s0, Hm)) and conj_ok(SI, kr(Sm, s0)) and conj_ok(IS, kr(s0, Sm)) and conj_ok(HI, kr(Hm, s0))
check('F1', okF1, 'Ad(I(x)H), Ad(S(x)I), Ad(I(x)S), Ad(H(x)I) as signed permutations of tables')

print('== F2  group orders')
G16 = closure([CNOT_T, ZI, IZ, TT])
GH = closure([CNOT_T, ZI, IZ, TT, IH])
GS = closure([CNOT_T, ZI, IZ, TT, SI])
GCl = closure([CNOT_T, HI, IH, SI, IS, TT])
SS = [(1, 1), (1, -1), (-1, 1), (-1, -1)]


def e_s(s):
    w = [0] * 16
    w[0], w[7], w[10], w[13] = R(1, 4), R(-s[0], 4), R(-s[1], 4), R(-s[0] * s[1], 4)
    return w


ZF = {tuple(e_s(s)) for s in SS}
StabZF = [gg for gg in GCl if {tuple(act(gg, list(z))) for z in ZF} == ZF]
G48 = closure([CNOT_T, ZI, IZ, TT, SW])
okF2 = len(G16) == 16 and len(GCl) == 23040 and G16 <= GH <= GCl and G16 <= GS <= GCl and G48 <= set(StabZF)
check('F2', okF2, f'|G16| = {len(G16)}, |G_H| = {len(GH)}, |G_S| = {len(GS)}, |G_Cl| = {len(GCl)}, '
      f'|Stab_Cl(Z_F)| = {len(StabZF)}; <G16,SWAP> inside Stab_Cl(Z_F)')

print('== F3  the conjecture: G_H excludes every Bell-type defect')
C = sp.Matrix(3, 3, lambda i, j: sp.Symbol(f'C{i + 1}{j + 1}'))
Tsym = [1 if k == 0 else (C[k // 4 - 1, k % 4 - 1] if (k // 4 >= 1 and k % 4 >= 1) else 0) for k in range(16)]


def marginals(w):
    return [w[4 * mu] for mu in (1, 2, 3)] + [w[nu] for nu in (1, 2, 3)]


forms = set()
for gg in (CNOT_T, comp(CNOT_T, IH)):
    for f_ in marginals(act(gg, Tsym)):
        forms.add(sp.expand(f_))
need = {C[0, 0], C[1, 0], C[2, 0]}
okF3 = all((c_ in forms) or (-c_ in forms) for c_ in need)
check('F3', okF3, f'marginal entries of cnot T and cnot Ad(IH) T: {sorted(str(x) for x in forms)} include the first '
      'column of C')

print('== F4  Bell seeds for G16 and G_S; non-orthogonal G_S orbit')


def m_of(Tpsi, G):
    best = 0
    for gg in G:
        wv = act(gg, Tpsi)
        v = wv[4] ** 2 + wv[8] ** 2 + wv[12] ** 2
        if v > best:
            best = v
    return best


psiF = sp.Matrix([1, 1, 1, -1]) / 2
TF = table(psiF * psiF.H)
eF = [(R(1, 2) if k == 0 else 0) - TF[k] / 4 for k in range(16)]
orbit = {tuple(act(gg, eF)) for gg in GS}
gram = {sp.nsimplify(sum(a * b for a, b in zip(o1, o2))) for o1 in orbit for o2 in orbit if o1 != o2}
okF4 = m_of(TF, G16) == 0 and m_of(TF, GS) == 0 and R(1, 8) in gram
check('F4', okF4, f'm(psi_F) = 0 for G16 and G_S (Bell seed); G_S-orbit of e_F: {len(orbit)} defects, off-diagonal '
      f'ipW values {sorted(gram)}')

print('== F5  general seeds (claim D) for G_H and G_Cl')
cands = [('psi_a', sp.Matrix([15, -1, 7, 7]) / 18), ('psi_b', sp.Matrix([1, 2, 3, 4]) / sp.sqrt(30)),
         ('psi_c', sp.Matrix([4, 3 * I, 2, 1]) / sp.sqrt(30))]
alphas = [R(3, 4), R(4, 5), R(5, 6), R(7, 8), R(9, 10), R(19, 20), R(99, 100)]
chosen, okF5 = {}, True
for gname, G in (('G_H', GH), ('G_Cl', GCl)):
    sel = None
    for name, v in cands:
        Tv = table(v * v.H)
        mv = m_of(Tv, G)
        print(f'F5    {gname}: m({name}) = {mv}')
        if sel is None and mv < 1:
            al_ = next((a_ for a_ in alphas if (2 * a_ - 1) ** 2 >= mv), None)
            sel = (name, v, mv, al_)
    okF5 &= sel is not None and sel[3] is not None
    if sel is not None and sel[3] is not None:
        name, v, mv, al_ = sel
        Tv = table(v * v.H)
        e = [(al_ if k == 0 else 0) - Tv[k] / 4 for k in range(16)]
        rho = pauliW(e)
        okF5 &= sp.expand(rho * v - (al_ - 1) / 4 * v) == sp.zeros(4, 1)
        okF5 &= al_ ** 2 - al_ / 2 > 0
        chosen[gname] = (name, mv, al_)
check('F5', okF5, f'chosen seeds (name, m, alpha): {chosen}; rho(e) psi = (alpha - 1)/4 psi < 0; alpha^2 - alpha/2 > 0')

print('== F6  K(Z_F) for the Clifford stabilizer of Z_F')
okF6 = all({tuple(act(gg, list(z))) for z in ZF} == ZF for gg in StabZF) and len(StabZF) > len(G48)
check('F6', okF6, f'every element of Stab_Cl(Z_F) (order {len(StabZF)}) permutes Z_F')

print('== CC countercontrols (each must be REJECTED)')
prod_ = kr(sp.Matrix([3, 4]) / 5, sp.Matrix([5, 12]) / 13)
Tp = table(prod_ * prod_.H)
rej1 = all(m_of(Tp, G) == 1 for G in (G16, GH, GS, GCl))
print(f"CC1   {'REJECTED' if rej1 else 'NOT REJECTED'}  product state: m = 1 for every group")
mFH = m_of(TF, GH)
rej2 = bool(mFH > 0)
print(f"CC2   {'REJECTED' if rej2 else 'NOT REJECTED'}  psi_F under G_H: m = {mFH} > 0")
bad = list(SI)
bad[4] = (bad[4][0], -bad[4][1])
rej3 = not conj_ok(tuple(bad), kr(Sm, s0))
print(f"CC3   {'REJECTED' if rej3 else 'NOT REJECTED'}  sign-flipped table map for Ad(S(x)I) fails the conjugation test")
rej4 = bool('G_H' in chosen and (2 * R(1, 2) - 1) ** 2 < chosen['G_H'][1])
print(f"CC4   {'REJECTED' if rej4 else 'NOT REJECTED'}  alpha = 1/2 inadmissible for the G_H seed (0 < m)")

allok = all(ok for _, ok in results) and rej1 and rej2 and rej3 and rej4
print(f"SUMMARY checks {sum(ok for _, ok in results)}/{len(results)} PASS; countercontrols rejected "
      f"{int(rej1) + int(rej2) + int(rej3) + int(rej4)}/4")
if allok:
    print(f"VERDICT FE-CONJECTURE-REFUTED G_H (order {len(GH)}) excludes all Bell-type defects; EXOTIC(existence) "
          f"seeds {chosen}; K(Z_F) explicit for Stab_Cl(Z_F) (order {len(StabZF)})")
else:
    print('VERDICT FE-FAILED')
