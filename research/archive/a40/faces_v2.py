# ---------------------------------------------------------------- the five faces (v2: one generic lemma per structure)
thm('a40_shared_k1', '(1 + Complex.I) * star (1 + Complex.I) = 2', KAPPA_TAC)
thm('a40_shared_ones', '∀ c : Fin 2, ![(1 : ℂ), 1] c = 1', '  intro c\n  fin_cases c <;> rfl')
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
    L.append('  intro M hU hF r0 r1 r2 r3 r4 r5 r6 r7')
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
        rw_rel = '' if ra[i] == 0 else '    rw [r%d j]\n' % rb[i]
        L.append(('  have i%d : ∀ j : Fin 4 × Fin 4, M %s j = %s %s j := by\n    intro j\n    simp only [Matrix.of_apply]\n    rw [a40_shared_gen_SN_col j]\n' % (i, PAIR(i), DITAX(snm, XLIT, YM, DLIT), PAIR(i)))
                 + rw_rel
                 + '    (try conv_lhs => simp (config := { decide := true }) %s)\n    (try conv_rhs => simp (config := { decide := true }) %s)\n    first\n    | (field_simp; ring)\n    | ring\n    | (simp; field_simp; ring)' % (EVAL, EVAL))
    ycase = """      · rw [Matrix.mem_unitaryGroup_iff]
        ext b b'
        rw [Matrix.mul_apply, Matrix.one_apply]
        simp only [Matrix.star_apply, Matrix.of_apply, star_mul']
        have e : ∀ d : Fin 8, (1 + Complex.I) * M (REP b) (COL %d d) * (star (M (REP b') (COL %d d)) * star (1 + Complex.I)) = ((1 + Complex.I) * star (1 + Complex.I)) * (M (REP b) (COL %d d) * star (M (REP b') (COL %d d))) := fun d => by ring
        simp only [e, ← Finset.mul_sum, a40_shared_k1]
        exact hblk%d b b'
      · intro b d
        simp only [Matrix.of_apply]
        rw [norm_mul, mul_pow, a40_shared_k1sq, hF]
        norm_num"""
    L.append('  refine ⟨XLIT, YM, DLIT, a40_shared_x_flat, ?_, fun _ _ => a40_shared_dnorm, ?_⟩\n  · intro c\n    fin_cases c\n'
             + '\n'.join('    · refine ⟨?_, ?_⟩\n' + ycase % (c, c, c, c, c) for c in (0, 1)))
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
    HZ3 = H3Z('z', 'w', args[1], args[2], args[3])
    MM = HZ3 if o == 'c' else HZ3 + 'ᵀ'
    HYP = '∀ z w %s %s : ℂ, star z * z = 1 → star w * w = 1 → star %s * %s = 1 → star %s * %s = 1 → ' % (fv[0], fv[1], fv[0], fv[0], fv[1], fv[1])
    INTRO = '  intro z w %s %s hz hw ha hb\n' % (fv[0], fv[1])
    rows = g['rows']
    for b in range(8):
        PP, RR = rows[b][1], rows[b][0]
        lhs = '%s %s j' % (MM, PAIR(PP)); rhs = '%s j * %s %s j' % (g['SIGMA'], MM, PAIR(RR))
        thm('a40_shared_face_%s_rel%d' % (tag, b), HYP + '∀ j : Fin 4 × Fin 4, ' + lhs + ' = ' + rhs,
            INTRO + '  intro j\n' + ('  simp only [Matrix.transpose_apply]\n' if o == 'r' else '') + '  obtain ⟨c, d⟩ := j\n'
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
