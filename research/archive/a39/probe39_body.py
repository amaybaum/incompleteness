
# ---- A39: the three-parameter family H3(u1, u2, u3) = SIG o u1^A u2^B u3^C ------------------------------------------
# A, B, C are act 38's three pieces (EA, EB, EC above); H3 is a flat unitary on the whole torus iff, for every ordered row
# pair (r, s), the columns grouped by the joint difference triple (A_rj - A_sj, B_rj - B_sj, C_rj - C_sj) have pair sums
# sum SIG_rj conj(SIG_sj) equal to 16 [r = s] on the zero triple and 0 on every other triple.
PA = [[EA(i, j) for j in range(16)] for i in range(16)]
PB = [[EB(i, j) for j in range(16)] for i in range(16)]
PC = [[EC(i, j) for j in range(16)] for i in range(16)]
def madd(*Ms): return [[sum(M[i][j] for M in Ms) for j in range(16)] for i in range(16)]
def gp(u, k):
    out = ONE
    for _ in range(k): out = out * u
    return out
def H3(u1, u2, u3): return [[SIG[i][j] * gp(u1, PA[i][j]) * gp(u2, PB[i][j]) * gp(u3, PC[i][j]) for j in range(16)] for i in range(16)]
def Hu(u): return [[SIG[i][j] * gp(u, EE[i][j]) for j in range(16)] for i in range(16)]
def joint_gate(mats, symbolic):
    """(joint level sets checked, failures) for the multivariate identity of SIG o prod u_k^{M_k}"""
    n = 0; bad = []
    for r in range(16):
        for s in range(16):
            groups = {}
            for j in range(16):
                groups.setdefault(tuple(M[r][j] - M[s][j] for M in mats), []).append(j)
            for t, js in groups.items():
                n += 1
                zero = r == s and not any(t)
                if symbolic:
                    cnt = {}
                    for j in js:
                        a1, q1, r1 = SIGE[r][j]; a2, q2, r2 = SIGE[s][j]
                        cnt[(q1 - q2, r1 - r2)] = cnt.get((q1 - q2, r1 - r2), 0) + (1 if (a1 - a2) % 4 == 0 else -1)
                    got = {k: v for k, v in cnt.items() if v}
                    if got != ({(0, 0): 16} if zero else {}): bad.append((r, s, t))
                else:
                    tot = ZERO
                    for j in js: tot = tot + SIG[r][j] * SIG[s][j].conj()
                    if tot != (G(16) if zero else ZERO): bad.append((r, s, t))
    return n, bad

print('== 1. the three pieces ==')
check("A + B + C is act 38's exponent matrix E; the pieces take values in {0, 1} and are disjoint", (madd(PA, PB, PC) == EE, all(PA[i][j] + PB[i][j] + PC[i][j] <= 1 and min(PA[i][j], PB[i][j], PC[i][j]) >= 0 for i in range(16) for j in range(16))), (True, True))
supp = lambda M: (sorted(i for i in range(16) if any(M[i])), sorted(j for j in range(16) if any(M[i][j] for i in range(16))), sum(map(sum, M)))
check('rows, columns and support of A, B and C', (supp(PA), supp(PB), supp(PC)), (([7, 15], [4, 5, 6, 7, 12, 13, 14, 15], 16), ([8, 9, 10, 11], [1, 5, 9, 13], 16), ([1, 3, 4, 6, 9, 11, 12, 14], [2, 8], 16)))
TRIPLES = sorted(set(tuple(M[r][j] - M[s][j] for M in (PA, PB, PC)) for r in range(16) for s in range(16) for j in range(16)))
check('the joint difference triples occurring over all ordered row pairs', TRIPLES, [(-1, 0, 0), (-1, 1, 0), (0, -1, 0), (0, 0, -1), (0, 0, 0), (0, 0, 1), (0, 1, 0), (1, -1, 0), (1, 0, 0)])
print('  (%.0fs)' % (time.time() - t0))

print('== 2. realizability on the three-torus: the joint level-set identity ==')
n3, b3 = joint_gate([PA, PB, PC], False)
check('exact Gaussian rationals: joint level sets over the 256 ordered row pairs, and failures', (n3, len(b3)), (552, 0))
n3s, b3s = joint_gate([PA, PB, PC], True)
check('monomial by monomial in z and w, symbolic units (the form of the kernel proof): joint level sets, and failures', (n3s, len(b3s)), (552, 0))
print('  (%.0fs)' % (time.time() - t0))

print('== 3. controls ==')
check('the family passes through the stratum point: H3(1, 1, 1) = SIG', H3(ONE, ONE, ONE) == SIG, True)
U5 = G(Fr(3, 5), Fr(4, 5)); U17 = G(Fr(8, 17), Fr(15, 17)); MINUS = G(-1)
check("its diagonal is act 38's arc: H3(u, u, u) = SIG o u^E at u = u5, u60, -1 and i", [H3(u, u, u) == Hu(u) for u in (U5, U60, MINUS, I_)], [True] * 4)
TRIPS = [(U5, w, U17), (I_, MINUS, U60), (z, w.conj(), z.conj()), (U17, U5, I_)]
check('H3 is exactly unitary at four Gaussian-rational points of the torus off the diagonal', [is_unitary16(H3(*t)) for t in TRIPS], [True] * 4)
check('and is not unitary at a non-unit parameter (u1 = 2): the unit hypothesis is used', is_unitary16(H3(G(2), ONE, ONE)), False)
subs = [('E, one variable', [EE]), ('A', [PA]), ('B', [PB]), ('C', [PC]), ('(A, B)', [PA, PB]), ('(A, C)', [PA, PC]), ('(B, C)', [PB, PC]), ('(A + B, C)', [madd(PA, PB), PC])]
res = [(nm,) + joint_gate(ms, False)[:1] + (len(joint_gate(ms, False)[1]),) for nm, ms in subs]
check('the subfamilies, each in its own variables: joint level sets and failures', [(nm, k, f) for nm, k, f in res], [('E, one variable', 512, 0), ('A', 312, 0), ('B', 352, 0), ('C', 384, 0), ('(A, B)', 424, 0), ('(A, C)', 440, 0), ('(B, C)', 480, 0), ('(A + B, C)', 536, 0)])
Cp = [r[:] for r in PC]; Cp[1][2] = 1 - Cp[1][2]
check('a countercontrol: one entry of C flipped, the joint identity fails (failures) and H3 is not unitary at (u5, w, (8+15i)/17)', (len(joint_gate([PA, PB, Cp], False)[1]), is_unitary16([[SIG[i][j] * gp(U5, PA[i][j]) * gp(w, PB[i][j]) * gp(U17, Cp[i][j]) for j in range(16)] for i in range(16)])), (60, False))
# the joint test is strictly stronger than the line tests: on the diagonal x = y = z the triples (1, -1, 0) and (0, 0, 0)
# project to the same integer, so the one-variable identity alone does not see their separate cancellation
merged = sorted(set(t for t in TRIPLES if sum(t) == 0 and any(t)))
check('the joint triples the diagonal projection merges with the zero triple (a line test cannot separate them)', merged, [(-1, 1, 0), (1, -1, 0)])
mset = []
for r in range(16):
    for s_ in range(16):
        for t in merged:
            js = [j for j in range(16) if (PA[r][j] - PA[s_][j], PB[r][j] - PB[s_][j], PC[r][j] - PC[s_][j]) == t]
            if js:
                tot = ZERO
                for j in js: tot = tot + SIG[r][j] * SIG[s_][j].conj()
                mset.append((r, s_, t, len(js), tot == ZERO))
check('each merged joint level set cancels on its own: their number, their column counts, and whether every one sums to zero', (len(mset), sorted(set(x[3] for x in mset)), all(x[4] for x in mset)), (16, [2], True))
print('  (%.0fs)' % (time.time() - t0))

print()
if fails:
    print('dita_torus_probe: FAILED (%d): %s' % (len(fails), fails)); sys.exit(1)
print('dita_torus_probe: OK -- the three-parameter family SIG o u1^A u2^B u3^C through the certified stratum point, A, B, C '
      "act 38's three pieces: every joint level set of every ordered row pair cancels exactly, 552 of them, and monomial by monomial "
      'in z and w, so the family is a complex Hadamard matrix on the whole three-torus; it passes through SIG at (1, 1, 1) and its '
      "diagonal is act 38's arc")
