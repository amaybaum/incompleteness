"""Emit the A40 design module from props40.json: core lemmas plus the frozen statements verbatim.
usage: python3 stage40.py [--verdict] [--ns NAME] > mod40.lean"""
import importlib.util, json, os, sys, itertools
S = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, S)
P = json.load(open(os.path.join(S, 'props40.json'))); PR = P['PROPS']
spec = importlib.util.spec_from_file_location('build40', os.path.join(S, 'build40.py')); B = importlib.util.module_from_spec(spec); spec.loader.exec_module(B)
import face40, named40
VERDICT = '--verdict' in sys.argv
COUNTER = '--counter' in sys.argv   # design countercontrol: absent face u2 = -1 under the t1 map; one exclusion value flipped
NS = sys.argv[sys.argv.index('--ns') + 1] if '--ns' in sys.argv else 'DitaTorusLocus'
src36 = open(os.path.join(S, '..', 'a36', 'stage36.py'), encoding='utf-8').read()
exec(src36[src36.index('E16 = '):src36.index('# the witnesses of the line')])
P39 = json.load(open(os.path.join(S, '..', 'a39', 'props39.json')))
EA, EB, EC = P39['EA'], P39['EB'], P39['EC']
def H3Z(z, w, a1, a2, a3):
    return ('(Matrix.of fun i j : Fin 4 × Fin 4 => ' + SIG(z, w) + ' i j * ' + a1 + ' ^ ' + EA + ' * ' + a2 + ' ^ ' + EB +
            ' * ' + a3 + ' ^ ' + EC + ')')
def MAT(n): return 'Matrix (Fin %d) (Fin %d) ℂ' % (n, n)
def tables(m, n, cp, rows):
    cblk = [None] * 16; cpos = [None] * 16; ra = [None] * 16; rb = [None] * 16
    for c in range(m):
        for d in range(n): cblk[cp[c][d]] = c; cpos[cp[c][d]] = d
    for b in range(n):
        for a in range(m): ra[rows[b][a]] = a; rb[rows[b][a]] = b
    return ra, rb, cblk, cpos
STRUCT = {nm: (m, n, cp, rows) for nm, m, n, cp, rows in B.CLASSES}
STRUCT['mc'] = (2, 8) + B.M_COL; STRUCT['mr'] = (2, 8) + B.M_ROW
def DITAX(nm, X, Y, D):
    m, n, cp, rows = STRUCT[nm]
    if nm == 't1': return DITA28(X, Y, D)
    ra, rb, cblk, cpos = tables(m, n, cp, rows)
    return ('(Matrix.of fun i j : Fin 4 × Fin 4 => ' + DG(X, Y, D, 'Fin %d × Fin %d' % (m, n)) +
            ' (%s i.1 i.2, %s i.1 i.2) (%s j.1 j.2, %s j.1 j.2))' % (B.B37.table(ra), B.B37.table(rb), B.B37.table(cblk), B.B37.table(cpos)))
def FORMX(nm, o, X='X', Y='Y', D='D'):
    return DITAX(nm, X, Y, D) + ('ᵀ' if o == 'r' else '')
def EXQ(nm, o, h3):
    m, n = STRUCT[nm][:2]
    return ('(∃ (X : %s) (Y : Fin %d → %s) (D : Fin %d → Fin %d → ℂ), ' % (MAT(m), m, MAT(n), m, n) + FLG('Fin %d' % m, 'X') +
            ' ∧ (∀ c, ' + FLG('Fin %d' % n, 'Y c') + ') ∧ (∀ c b, ‖D c b‖ = 1) ∧ ' + h3 + ' = ' + FORMX(nm, o) + ')')
out = []
def thm(name, stmt, proof):
    out.append('theorem %s :\n    %s := by\n%s\n#print axioms %s\n' % (name, stmt, proof, name))
UV = {1: 'u₁', 2: 'u₂', 3: 'u₃'}
def unith(vs):
    s = ''
    for v, hv, t in vs:
        s += ('  have hs%s : star %s = %s⁻¹ := a40_shared_inv_of_unit %s %s\n  have hs%s\' : (starRingEnd ℂ) %s = %s⁻¹ := hs%s\n'
              '  have h0%s : %s ≠ 0 := a40_shared_ne_zero_of_unit %s %s\n  have hn%s : ‖%s‖ = 1 := a35_shared_norm_of_unit %s %s\n'
              % (t, v, v, v, hv, t, v, v, t, t, v, v, hv, t, v, v, hv))
    return s
def simpset(ts): return ', '.join('hs%s, hs%s\'' % (t, t) for t in ts)

# ---------------------------------------------------------------- scalars, units, the two scaled unitaries
thm('a40_shared_inv_of_unit', '∀ x : ℂ, star x * x = 1 → star x = x⁻¹', '  intro x h\n  exact eq_inv_of_mul_eq_one_left h')
thm('a40_shared_ne_zero_of_unit', '∀ x : ℂ, star x * x = 1 → x ≠ 0', '  intro x h hx\n  rw [hx, mul_zero] at h\n  exact zero_ne_one h')
KAPPA_TAC = '''  first
  | (apply Complex.ext <;> simp [Complex.star_def] <;> norm_num)
  | (apply Complex.ext <;> simp [Complex.conj_re, Complex.conj_im] <;> norm_num)
  | (simp [Complex.ext_iff, Complex.star_def]; norm_num)
  | (rw [Complex.ext_iff]; simp; norm_num)'''
thm('a40_shared_k2', '(1 + Complex.I) / 2 * star ((1 + Complex.I) / 2) = 1 / 2', KAPPA_TAC)
thm('a40_shared_k8', '(1 + Complex.I) / 4 * star ((1 + Complex.I) / 4) = 1 / 8', KAPPA_TAC)
SQ_TAC = '''  have e : ‖%s‖ ^ 2 = Complex.normSq (%s) := by
    first
    | exact Complex.sq_norm _
    | exact Complex.sq_abs _
    | simp [Complex.sq_abs]
    | (rw [← Complex.normSq_eq_norm_sq])
  rw [e]
  first
  | (simp [Complex.normSq_apply]; norm_num)
  | (rw [Complex.normSq_apply]; simp; norm_num)
  | norm_num [Complex.normSq_apply]'''
thm('a40_shared_k2sq', '‖(1 + Complex.I) / 2‖ ^ 2 = 1 / 2', SQ_TAC % ('(1 + Complex.I) / 2', '(1 + Complex.I) / 2'))
thm('a40_shared_k8sq', '‖(1 + Complex.I) / 4‖ ^ 2 = 1 / 8', SQ_TAC % ('(1 + Complex.I) / 4', '(1 + Complex.I) / 4'))
thm('a40_shared_one_add_I', '(1 + Complex.I) ≠ 0', '''  intro h
  have := congrArg Complex.re h
  simp at this''')
thm('a40_shared_dval', '(2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I)) = -Complex.I', '''  have h := a40_shared_one_add_I
  rw [div_eq_iff (mul_ne_zero h h)]
  first
  | linear_combination (Complex.I + 2) * Complex.I_sq
  | linear_combination (-(Complex.I + 2)) * Complex.I_sq
  | (ring_nf; rw [Complex.I_sq]; ring)
  | (apply Complex.ext <;> simp <;> norm_num)''')
thm('a40_shared_fpe', '∀ (a : Fin 2) (b : Fin 4), @finProdFinEquiv 2 4 (a, b) = ![![(0 : Fin 8), 1, 2, 3], ![4, 5, 6, 7]] a b', '  decide')
thm('a40_shared_dnorm', '‖(2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))‖ = 1', '  rw [a40_shared_dval, norm_neg, Complex.norm_I]')
for n, k in ((2, 'k2'), (8, 'k8')):
    thm('a40_shared_scaled_unitary%d' % n, '∀ M : Matrix (Fin %d) (Fin %d) ℂ, (∀ b b\' : Fin %d, ∑ d : Fin %d, M b d * star (M b\' d) = if b = b\' then (%d : ℂ) else 0) → (Matrix.of fun b d : Fin %d => (1 + Complex.I) / %d * M b d) ∈ Matrix.unitaryGroup (Fin %d) ℂ' % (n, n, n, n, n, n, n // 2 if n == 8 else 2, n), '''  intro M hM
  rw [Matrix.mem_unitaryGroup_iff]
  ext b b'
  rw [Matrix.mul_apply, Matrix.one_apply]
  simp only [Matrix.star_apply, Matrix.of_apply]
  have e : ∀ d, (1 + Complex.I) / %d * M b d * star ((1 + Complex.I) / %d * M b' d) = ((1 + Complex.I) / %d * star ((1 + Complex.I) / %d)) * (M b d * star (M b' d)) := by
    intro d
    rw [star_mul']
    ring
  simp only [e, ← Finset.mul_sum, hM b b', a40_shared_%s]
  split_ifs <;> norm_num''' % ((n // 2 if n == 8 else 2,) * 4 + (k,)))
# X: the 2 x 2 Fourier matrix scaled by (1 + i)/2, flat unitary
XLIT = '(Matrix.of fun a c : Fin 2 => (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] a c)'
thm('a40_shared_x_flat', FLG('Fin 2', XLIT), '''  refine ⟨?_, ?_⟩
  · apply a40_shared_scaled_unitary2
    intro b b'
    fin_cases b <;> fin_cases b' <;> simp [Fin.sum_univ_two] <;> norm_num
  · intro a c
    simp only [Matrix.of_apply]
    rw [norm_mul, mul_pow, a40_shared_k2sq]
    fin_cases a <;> fin_cases c <;> simp''')
DLIT = '(fun (_ : Fin 2) (_ : Fin 8) => (2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I)))'

def mono_text(x):
    """(k, (p, q, r)) with p in {0, 2}, q, r, k in {0, 1} -> Lean text over z w u₁ u₂ u₃"""
    k, (p, q, r) = x
    fs = ['z'] * q + ['w'] * r + [UV[t + 1] for t in range(3) for _ in range(k[t])]
    assert p in (0, 2) and all(e in (0, 1) for e in (q, r) + k), x
    body = ' * '.join(fs) if fs else '1'
    return ('(-(' + body + '))' if fs else '(-1)') if p == 2 else ('(' + body + ')' if fs else '1')
# ---------------------------------------------------------------- the twenty named exclusions
def ent_val(i, j):
    """(1/4) * sign * z^q w^r u1^a u2^b u3^c as Lean text, for H3 u₁ u₂ u₃ at (i, j)"""
    k = (named40.EA(i, j), named40.EB(i, j), named40.EC(i, j)); p, q, r = named40.SIGE[i][j]
    return '((1 / 4 : ℂ) * ' + mono_text((k, (p, q, r))) + ')'
def POS(i): return '((%d : Fin 4), (%d : Fin 4))' % (i // 4, i % 4)
HZG = H3Z('z', 'w', 'u₁', 'u₂', 'u₃')
def mono_vec(i, j):
    k = (named40.EA(i, j), named40.EB(i, j), named40.EC(i, j)); p, q, r = named40.SIGE[i][j]
    return p, (q, r) + k       # sign exponent, (z, w, u1, u2, u3) exponents
for nm, o in B.NAMED:
    m, n, cp, rows = STRUCT[nm]
    form = 'column' if o == 'c' else 'row'
    ws = named40.witnesses(form, tuple(map(tuple, cp)), tuple(map(tuple, rows)))
    parts = []
    for coord, v in B.EQS[(nm, o)]:
        kk = tuple(1 if t == coord - 1 else 0 for t in range(3))
        cand = [w for w in ws if tuple(abs(x) for x in w[0]) == kk and sorted(map(abs, w[0])) == [0, 0, 1]]
        want = (0, 0, 0) if v == '1' else (2, 0, 0)
        cand = [w for w in cand if (w[1] if sum(w[0]) > 0 else named40.vsub((0, 0, 0), w[1])) == want]
        assert cand, (nm, o, coord, v)
        k, c, (i, j, i2, j0) = cand[0]
        # H[i,j] H[i2,j0] = H[i,j0] H[i2,j] for the oriented matrix M; M = H3 (column) or H3ᵀ (row)
        pos = [(i, j), (i2, j0), (i, j0), (i2, j)]
        if o == 'r': pos = [(b_, a_) for a_, b_ in pos]          # entries of H3 itself
        L = [mono_vec(*pos[0]), mono_vec(*pos[1])]; R = [mono_vec(*pos[2]), mono_vec(*pos[3])]
        sL = (L[0][0] + L[1][0]) % 4; sR = (R[0][0] + R[1][0]) % 4
        eL = tuple(x + y for x, y in zip(L[0][1], L[1][1])); eR = tuple(x + y for x, y in zip(R[0][1], R[1][1]))
        C = tuple(min(x, y) for x, y in zip(eL, eR))
        dL = tuple(x - y for x, y in zip(eL, C)); dR = tuple(x - y for x, y in zip(eR, C))
        var = 1 + coord          # index into (z, w, u1, u2, u3)
        unitv = tuple(1 if t == var else 0 for t in range(5))
        assert {dL, dR} == {unitv, (0,) * 5}, (nm, o, coord, dL, dR)
        sgnL = 1 if sL == 0 else -1; sgnR = 1 if sR == 0 else -1
        assert sL in (0, 2) and sR in (0, 2)
        names = ['z', 'w', 'u₁', 'u₂', 'u₃']
        Ctext = ' * '.join(names[t] for t in range(5) for _ in range(C[t])) or '1'
        if dL == unitv:
            coef = 16 * sgnL; vv = sgnR * sgnL       # sL C x = sR C  => x = sR/sL
        else:
            coef = -16 * sgnR; vv = sgnL * sgnR
        assert (vv == 1) == (v == '1'), (nm, o, coord)
        E = [HZG + ' ' + POS(a_) + ' ' + POS(b_) for a_, b_ in pos]
        V = [ent_val(a_, b_) for a_, b_ in pos]
        rw_h = 'rw [h]\n      simp only [%sMatrix.of_apply]\n      (try simp (config := { decide := true }) [a36_shared_div, a36_shared_mod, a40_shared_fpe])\n      (try ring)' % ('Matrix.transpose_apply, ' if o == 'r' else '')
        prf = ''.join('    have e%d : %s = %s := by\n      conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]\n      first\n      | ring\n      | (simp; ring)\n      | norm_num\n' % (t, E[t], V[t]) for t in range(4))
        prf += '    have key : %s * %s = %s * %s := by\n      %s\n' % (E[0], E[1], E[2], E[3], rw_h)
        prf += '    rw [e0, e1, e2, e3] at key\n'
        prf += '    have hC : (%s : ℂ) ≠ 0 := by simp [h0z, h0w, h01, h02, h03]\n' % Ctext
        prf += '    have h5 : (%s : ℂ) * (%s - %s) = 0 := by linear_combination (%d : ℂ) * key\n' % (Ctext, UV[coord], ('1' if v == '1' else '(-1)') if not (COUNTER and (nm, o) == ('k1', 'c')) else ('(-1)' if v == '1' else '1'), coef)
        prf += '    rcases mul_eq_zero.1 h5 with h6 | h6\n    · exact absurd h6 hC\n    · linear_combination h6'
        parts.append(prf)
    stmt = ('∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → '
            + EXQ(nm, o, HZG) + ' → ' + B.EQTEXT(B.EQS[(nm, o)]))
    UH = ('  have h0z : z ≠ 0 := a40_shared_ne_zero_of_unit z hz\n  have h0w : w ≠ 0 := a40_shared_ne_zero_of_unit w hw\n'
          '  have h01 : u₁ ≠ 0 := a40_shared_ne_zero_of_unit u₁ h1\n  have h02 : u₂ ≠ 0 := a40_shared_ne_zero_of_unit u₂ h2\n'
          '  have h03 : u₃ ≠ 0 := a40_shared_ne_zero_of_unit u₃ h3\n')
    body = '  intro z w u₁ u₂ u₃ hz hw h1 h2 h3\n' + UH + '  rintro ⟨X, Y, D, -, -, -, h⟩\n'
    if len(parts) == 1:
        body += '\n'.join(l[2:] for l in parts[0].split('\n'))
    else:
        body += '  refine ⟨' + ', '.join(['?_'] * len(parts)) + '⟩\n' + '\n'.join('  · ' + p[4:] for p in parts)
    thm('a40_shared_excl_%s_%s_core' % (nm, o), stmt, body)

# ---------------------------------------------------------------- the five faces (v2: one generic lemma per structure)
thm('a40_shared_k1', '(1 + Complex.I) * star (1 + Complex.I) = 2', KAPPA_TAC)
thm('a40_shared_ones', '∀ c : Fin 2, ![(1 : ℂ), 1] c = 1', '  intro c\n  fin_cases c <;> rfl')
thm('a40_shared_scal', '∀ s m : ℂ, (1 + Complex.I) / 2 * s * ((2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) * ((1 + Complex.I) * m) = s * m',
    '''  intro s m
  have e : (1 + Complex.I) / 2 * ((2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) * (1 + Complex.I) = 1 := by
    rw [a40_shared_dval]
    linear_combination (-(Complex.I + 2) / 2) * Complex.I_sq
  calc (1 + Complex.I) / 2 * s * ((2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) * ((1 + Complex.I) * m)
      = ((1 + Complex.I) / 2 * ((2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) * (1 + Complex.I)) * (s * m) := by ring
    _ = s * m := by rw [e, one_mul]''')
thm('a40_shared_f0', '∀ c : Fin 2, ![![(1 : ℂ), 1], ![1, -1]] 0 c = 1', '  intro c\n  fin_cases c <;> rfl')
thm('a40_shared_f1', '∀ c : Fin 2, ![![(1 : ℂ), 1], ![1, -1]] 1 c = ![(1 : ℂ), -1] c', '  intro c\n  fin_cases c <;> rfl')
thm('a40_shared_k1sq', '‖(1 + Complex.I)‖ ^ 2 = 2', SQ_TAC % ('(1 + Complex.I)', '(1 + Complex.I)'))
def PAIR(i): return '((%d : Fin 4), (%d : Fin 4))' % (i // 4, i % 4)
GEN = {}
for snm in ('t2', 'mc', 't1', 'mr'):
    m, n, cp, rows = STRUCT[snm]
    ra, rb, cblk, cpos = tables(m, n, cp, rows)
    REP = '(![' + ', '.join(PAIR(rows[b][0]) for b in range(8)) + '] : Fin 8 → Fin 4 × Fin 4)'
    PART = '(![' + ', '.join(PAIR(rows[b][1]) for b in range(8)) + '] : Fin 8 → Fin 4 × Fin 4)'
    COL = '(![' + ', '.join('![' + ', '.join(PAIR(cp[c][d]) for d in range(8)) + ']' for c in range(2)) + '] : Fin 2 → Fin 8 → Fin 4 × Fin 4)'
    if snm == 't1':
        BLK = '(@Fin.modNat 2 2 j.1)'; POSN = '(@finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))'
    else:
        BLK = '(%s j.1 j.2)' % B.B37.table(cblk); POSN = '(%s j.1 j.2)' % B.B37.table(cpos)
    SIGMA = '(fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] %s)' % BLK
    YM = '(fun c : Fin 2 => Matrix.of fun b d : Fin 8 => (1 + Complex.I) * M (%s b) (%s c d))' % (REP, COL)
    GEN[snm] = dict(REP=REP, PART=PART, COL=COL, SIGMA=SIGMA, rows=rows, cp=cp)
    MT = 'Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ'
    HYPS = ('∀ M : %s, M ∈ Matrix.unitaryGroup (Fin 4 × Fin 4) ℂ → (∀ i j, ‖M i j‖ = 1 / 4) → ' % MT
            + ''.join('(∀ j : Fin 4 × Fin 4, M %s j = %s j * M %s j) → ' % (PAIR(rows[b][1]), SIGMA, PAIR(rows[b][0])) for b in range(8)))
    # the column-block split of a row inner product, the column tables' inverse, the sign on each block
    thm('a40_shared_gen_%s_split' % snm, '∀ M : %s, ∀ x y : Fin 4 × Fin 4, ∑ k, M x k * star (M y k) = ∑ d : Fin 8, M x (%s 0 d) * star (M y (%s 0 d)) + ∑ d : Fin 8, M x (%s 1 d) * star (M y (%s 1 d))' % (MT, COL, COL, COL, COL),
        '''  intro M x y
  simp only [Fintype.sum_prod_type, Fin.sum_univ_four, Fin.sum_univ_eight]
  first
  | (simp; ring)
  | ring
  | (simp only [Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.head_cons, Matrix.cons_val']; ring)''')
    thm('a40_shared_gen_%s_col' % snm, '∀ j : Fin 4 × Fin 4, %s %s %s = j' % (COL, BLK, POSN),
        '''  intro j
  obtain ⟨c, d⟩ := j
  fin_cases c <;> fin_cases d <;> first | rfl | decide | (simp (config := { decide := true }) [a36_shared_div, a36_shared_mod, a40_shared_fpe])''')
    thm('a40_shared_gen_%s_sig0' % snm, '∀ d : Fin 8, %s (%s 0 d) = 1' % (SIGMA, COL),
        '  intro d\n  fin_cases d <;> simp (config := { decide := true }) [a36_shared_div, a36_shared_mod, a40_shared_fpe]')
    thm('a40_shared_gen_%s_sig1' % snm, '∀ d : Fin 8, %s (%s 1 d) = -1' % (SIGMA, COL),
        '  intro d\n  fin_cases d <;> simp (config := { decide := true }) [a36_shared_div, a36_shared_mod, a40_shared_fpe]')
    thm('a40_shared_gen_%s_reps' % snm, '∀ b b\' : Fin 8, (%s b = %s b\' ↔ b = b\') ∧ %s b ≠ %s b\'' % (REP, REP, PART, REP),
        '  intro b b\'\n  fin_cases b <;> fin_cases b\' <;> decide')
    EVAL = "[a36_shared_div, a36_shared_mod, a40_shared_fpe, a40_shared_ones]"
    L = []
    L.append('  intro M hU hF r0 r1 r2 r3 r4 r5 r6 r7\n  have hI : (1 + Complex.I) ≠ 0 := a40_shared_one_add_I')
    L.append('  have hrel : ∀ (b : Fin 8) (j : Fin 4 × Fin 4), M (%s b) j = %s j * M (%s b) j := by' % (PART, SIGMA, REP))
    L.append('    intro b j\n    fin_cases b\n' + '\n'.join('    · exact r%d j' % k for k in range(8)))
    L.append("""  have hrows : ∀ i j, ∑ k, M i k * star (M j k) = if i = j then (1 : ℂ) else 0 := by
    intro i j
    have h := congrFun (congrFun (Matrix.mem_unitaryGroup_iff.mp hU) i) j
    rw [Matrix.mul_apply, Matrix.one_apply] at h
    simpa only [Matrix.star_apply] using h""")
    for c in (0, 1):
        combos = ['-e1 - e2', 'e1 + e2', '-e1 + e2', 'e1 - e2'] if c == 0 else ['-e1 + e2', 'e1 - e2', '-e1 - e2', 'e1 + e2']
        L.append(("""  have hblk%d : ∀ b b' : Fin 8, 2 * ∑ d : Fin 8, M (REP b) (COL %d d) * star (M (REP b') (COL %d d)) = if b = b' then (1 : ℂ) else 0 := by
    intro b b'
    have e1 := a40_shared_gen_SN_split M (REP b) (REP b')
    have e2 := a40_shared_gen_SN_split M (PART b) (REP b')
    rw [hrows] at e1 e2
    have h0 : ∀ d : Fin 8, M (PART b) (COL 0 d) = M (REP b) (COL 0 d) := fun d => by rw [hrel b, a40_shared_gen_SN_sig0 d, one_mul]
    have h1 : ∀ d : Fin 8, M (PART b) (COL 1 d) = -M (REP b) (COL 1 d) := fun d => by rw [hrel b, a40_shared_gen_SN_sig1 d, neg_one_mul]
    simp only [h0, h1, neg_mul, Finset.sum_neg_distrib] at e2
    have hr := a40_shared_gen_SN_reps b b'
    rw [if_neg hr.2] at e2
    simp only [hr.1] at e1
    first
""" % (c, c, c)) + '\n'.join('    | linear_combination %s' % x for x in combos))
    for i in range(16):
        part = ra[i] == 1
        hyp = ('(∀ j : Fin 4 × Fin 4, M %s j = %s j * M %s j) → ' % (PAIR(rows[rb[i]][1]), SIGMA, PAIR(rows[rb[i]][0]))) if part else ''
        stmt = '∀ M : %s, %s∀ j : Fin 4 × Fin 4, M %s j = %s %s j' % (MT, hyp, PAIR(i), DITAX(snm, XLIT, YM, DLIT), PAIR(i))
        RR = PAIR(rows[rb[i]][0])
        SCAL = '(1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] %d %s * ((2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) * ((1 + Complex.I) * M %s j)' % (ra[i], BLK, RR)
        LHS = ('![(1 : ℂ), -1] %s * M %s j' % (BLK, RR)) if part else ('M %s j' % PAIR(i))
        prf = ('  intro M ' + ('r ' if part else '') + 'j\n  simp only [Matrix.of_apply]\n  rw [a40_shared_gen_%s_col j]\n' % snm
               + ('  rw [r j]\n' if part else '')
               + '  show %s = %s\n' % (LHS, SCAL)
               + ('  rw [a40_shared_scal, a40_shared_f1]' if part else '  rw [a40_shared_scal, a40_shared_f0, one_mul]'))
        thm('a40_shared_gen_%s_row%d' % (snm, i), stmt, prf)
        L.append('  have i%d := a40_shared_gen_%s_row%d M%s' % (i, snm, i, (' r%d' % rb[i]) if part else ''))
    L.append("""  have hblk : ∀ (c : Fin 2) (b b' : Fin 8), 2 * ∑ d : Fin 8, M (REP b) (COL c d) * star (M (REP b') (COL c d)) = if b = b' then (1 : ℂ) else 0 := by
    intro c
    fin_cases c
    · exact hblk0
    · exact hblk1""")
    L.append("""  refine ⟨XLIT, YM, DLIT, a40_shared_x_flat, ?_, fun _ _ => a40_shared_dnorm, ?_⟩
  · intro c
    refine ⟨?_, ?_⟩
    · rw [Matrix.mem_unitaryGroup_iff]
      ext b b'
      rw [Matrix.mul_apply, Matrix.one_apply]
      simp only [Matrix.star_apply, Matrix.of_apply]
      calc _ = ((1 + Complex.I) * star (1 + Complex.I)) * ∑ d : Fin 8, M (REP b) (COL c d) * star (M (REP b') (COL c d)) := by
            rw [Finset.mul_sum]
            exact Finset.sum_congr rfl (fun d _ => by (try simp only [star_mul']); ring)
        _ = _ := by rw [a40_shared_k1]; exact hblk c b b'
    · intro b d
      simp only [Matrix.of_apply]
      rw [norm_mul, mul_pow, a40_shared_k1sq, hF]
      norm_num""")
    L.append('  · ext i j\n    obtain ⟨a, bb⟩ := i\n    fin_cases a <;> fin_cases bb\n' + '\n'.join('    · exact i%d j' % i for i in range(16)))
    body = '\n'.join(L)
    body = body.replace('REP', REP).replace('PART', PART).replace('COL', COL).replace('SN', snm).replace('XLIT', XLIT).replace('YM', YM).replace('DLIT', DLIT)
    thm('a40_shared_gen_%s' % snm, HYPS + EXQ(snm, 'c', 'M')[1:-1], body)
    GEN[snm]['BLK'] = BLK; GEN[snm]['POSN'] = POSN

FKEY = {'FACE_1p': 'u1=+1', 'FACE_1m': 'u1=-1', 'FACE_2p': 'u2=+1', 'FACE_3p': 'u3=+1', 'FACE_3m': 'u3=-1'}
for key, coord, val, nm, o in B.FACES:
    g = GEN[nm]; tag = key[5:].lower()
    free = [t for t in (1, 2, 3) if t != coord]; fv = [UV[t] for t in free]
    args = {1: 'u₁', 2: 'u₂', 3: 'u₃'}; args[coord] = '1' if val == '1' else '(-1)'
    if COUNTER and key == 'FACE_2p': args[coord] = '(-1)'
    HZ3 = H3Z('z', 'w', args[1], args[2], args[3])
    MM = HZ3 if o == 'c' else HZ3 + 'ᵀ'
    HYP = '∀ z w %s %s : ℂ, star z * z = 1 → star w * w = 1 → star %s * %s = 1 → star %s * %s = 1 → ' % (fv[0], fv[1], fv[0], fv[0], fv[1], fv[1])
    INTRO = '  intro z w %s %s hz hw ha hb\n' % (fv[0], fv[1])
    rows = g['rows']
    for b in range(8):
        PP, RR = rows[b][1], rows[b][0]
        lhs = '%s %s j' % (MM, PAIR(PP)); rhs = '%s j * %s %s j' % (g['SIGMA'], MM, PAIR(RR))
        thm('a40_shared_face_%s_rel%d' % (tag, b), HYP + '∀ j : Fin 4 × Fin 4, ' + lhs + ' = ' + rhs,
            INTRO[:-1] + ' j\n' + ('  simp only [Matrix.transpose_apply]\n' if o == 'r' else '') + '  obtain ⟨c, d⟩ := j\n'
            '  fin_cases c <;> fin_cases d <;> simp (config := { decide := true }) [Matrix.of_apply, a36_shared_div, a36_shared_mod, a40_shared_fpe] <;> first | done | ring | tauto | (field_simp; ring)')
    uv = {1: 'u₁', 2: 'u₂', 3: 'u₃'}
    hyp_unit = {t: ('ha' if t == free[0] else 'hb') for t in free}
    hyp_unit[coord] = '(by norm_num)'
    UARGS = 'z w %s %s %s hz hw %s %s %s' % (args[1], args[2], args[3], hyp_unit[1], hyp_unit[2], hyp_unit[3])
    unit_t = 'a39_shared_unitary_core %s' % UARGS
    flat_t = 'a39_shared_flat_core %s' % UARGS
    rel_t = ') ('.join('a40_shared_face_%s_rel%d z w %s %s hz hw ha hb' % (tag, b, fv[0], fv[1]) for b in range(8))
    if o == 'c':
        proof = INTRO + '  exact a40_shared_gen_%s _ (%s) (%s) (%s)' % (nm, unit_t, flat_t, rel_t)
    else:
        proof = (INTRO + '  obtain ⟨X, Y, D, h1, h2, h3, h4⟩ := a40_shared_gen_%s _ (transpose_unitary (%s)) (fun i j => by rw [Matrix.transpose_apply]; exact %s j i) (%s)\n' % (nm, unit_t, flat_t, rel_t)
                 + '  exact ⟨X, Y, D, h1, h2, h3, by rw [← h4, Matrix.transpose_transpose]⟩')
    thm('a40_shared_face_%s_core' % tag, HYP + EXQ(nm, o, HZ3)[1:-1], proof)

# ---------------------------------------------------------------- the frozen theorems
def frozen(name, key, tail):
    thm(name, PR[key], '  intro Γ₀ hΓ₀\n  dsimp only\n' + tail)
FACEARGS = {}
for key, coord, val, nm, o in B.FACES:
    tag = key[5:].lower(); free = [UV[t] for t in (1, 2, 3) if t != coord]
    frozen('a40_shared_' + key.lower(), key, '  intro %s %s ha hb\n  exact a40_shared_face_%s_core _ _ %s %s a36_shared_z_unit a36_shared_w_unit ha hb' % (free[0], free[1], tag, free[0], free[1]))
for nm, o in B.NAMED:
    frozen('a40_shared_excl_%s_%s' % (nm, o), 'EXCL_%s_%s' % (nm, o), '  intro u₁ u₂ u₃ h1 h2 h3\n  exact a40_shared_excl_%s_%s_core _ _ u₁ u₂ u₃ a36_shared_z_unit a36_shared_w_unit h1 h2 h3' % (nm, o))
if VERDICT:
    cores = []
    for key, coord, val, nm, o in B.FACES:
        tag = key[5:].lower(); free = [UV[t] for t in (1, 2, 3) if t != coord]
        cores.append('fun %s %s ha hb => a40_shared_face_%s_core _ _ %s %s a36_shared_z_unit a36_shared_w_unit ha hb' % (free[0], free[1], tag, free[0], free[1]))
    for nm, o in B.NAMED:
        cores.append('fun u₁ u₂ u₃ h1 h2 h3 => a40_shared_excl_%s_%s_core _ _ u₁ u₂ u₃ a36_shared_z_unit a36_shared_w_unit h1 h2 h3' % (nm, o))
    frozen('a40_locus_kernel', 'P_R', '  exact ⟨' + ',\n    '.join(cores) + '⟩')
    n = len(P['PARTS'])
    alts = ' | '.join(['h'] * n)
    proj = ['r' + '.2' * k + ('.1' if k < n - 1 else '') for k in range(n)]
    out.append('theorem a40_c_exclusive :\n    (' + PR['P_N'] + ') → ¬ (' + PR['P_R'] + ''') := by
  intro hN hR
  have h := hN _ rfl
  have r := hR _ rfl
  dsimp only at h r
  rcases h with ''' + alts + '\n' + '\n'.join('  · exact h ' + pj for pj in proj) + '''
#print axioms a40_c_exclusive
''')
HEADER = P['IMPORT'] + '\n' + P['DOC'] + ('\nset_option linter.unusedSimpArgs false\nset_option linter.unreachableTactic false\nset_option linter.unusedTactic false\n' if '--design' in sys.argv else '') + '\nnamespace OIBridge\nnamespace %s\n\n' % NS + P['OPEN'] + '\n'
TAIL = ''
if '--design' in sys.argv:
    import re as _re
    TAIL = '\n-- design: every theorem\'s axioms, repeated at the end\n' + ''.join('#print axioms %s\n' % n for n in _re.findall(r'(?m)^theorem (\S+)', '\n'.join(out)))
sys.stdout.write(HEADER + '\n'.join(out) + TAIL + 'end %s\nend OIBridge\n' % NS)
