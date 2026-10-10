"""Emit the A38 module (stage 1 or, with --verdict, stage 2) from props38.json: hand-written core lemmas plus the
frozen statements verbatim. usage: python3 stage38.py [--verdict] > mod38.lean"""
import importlib.util, json, os, sys
S = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, S)
spec = importlib.util.spec_from_file_location('build38', os.path.join(S, 'build38.py')); B = importlib.util.module_from_spec(spec); spec.loader.exec_module(B)
P = json.load(open(os.path.join(S, 'props38.json'))); PR = P['PROPS']
WIT = json.load(open(os.path.join(S, 'witness38.json')))
VERDICT = '--verdict' in sys.argv
# the A36 emitter's text builders, reused verbatim
src36 = open(os.path.join(S, '..', 'a36', 'stage36.py'), encoding='utf-8').read()
exec(src36[src36.index('E16 = '):src36.index('# the witnesses of the line')])
M16 = 'Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ'
def MAT(n): return 'Matrix (Fin %d) (Fin %d) ℂ' % (n, n)
EW = B.EW
def HZ(z, w, u):
    return '(Matrix.of fun i j : Fin 4 × Fin 4 => ' + SIG(z, w) + ' i j * ' + u + ' ^ (' + EW + '))'
HUC = HZ(ZC, WC, 'u'); SIGC = SIG(ZC, WC)
def POS(i): return '((%d : Fin 4), (%d : Fin 4))' % (i // 4, i % 4)
def tables(m, n, cp, rows):
    cblk = [None] * 16; cpos = [None] * 16; ra = [None] * 16; rb = [None] * 16
    for c in range(m):
        for d in range(n): cblk[cp[c][d]] = c; cpos[cp[c][d]] = d
    for b in range(n):
        for a in range(m): ra[rows[b][a]] = a; rb[rows[b][a]] = b
    return ra, rb, cblk, cpos
def DITAX(name, m, n, cp, rows):
    """the class's Dita form, beta-reduced as `dsimp only` leaves it in the frozen statement"""
    if name == 't1': return DITA28('X', 'Y', 'D')
    ra, rb, cblk, cpos = tables(m, n, cp, rows)
    return ('(Matrix.of fun i j : Fin 4 × Fin 4 => ' + DG('X', 'Y', 'D', 'Fin %d × Fin %d' % (m, n)) +
            ' (%s i.1 i.2, %s i.1 i.2) (%s j.1 j.2, %s j.1 j.2))' % (B.B37.table(ra), B.B37.table(rb), B.B37.table(cblk), B.B37.table(cpos)))
def EXQ(m, n, form):
    return ('(∃ (X : %s) (Y : Fin %d → %s) (D : Fin %d → Fin %d → ℂ), ' % (MAT(m), m, MAT(n), m, n) + FLG('Fin %d' % m, 'X') +
            ' ∧ (∀ c, ' + FLG('Fin %d' % n, 'Y c') + ') ∧ (∀ c b, ‖D c b‖ = 1) ∧ ' + HUC + ' = ' + form + ')')
UNITS = 'star z * z = 1 → star w * w = 1 → star u * u = 1 → '
out = []
def thm(name, stmt, proof):
    out.append('theorem %s :\n    %s := by\n%s\n#print axioms %s\n' % (name, stmt, proof, name))

# ---------------------------------------------------------------- units and conjugates
thm('a38_shared_conj_half', 'star (1 / 2 : ℂ) = 1 / 2', '''  first
  | (simp [Complex.ext_iff, Complex.star_def]; norm_num)
  | simp [Complex.ext_iff, Complex.star_def]
  | norm_num [Complex.ext_iff, Complex.star_def]''')
thm('a38_shared_conj_half\'', '(starRingEnd ℂ) (1 / 2 : ℂ) = 1 / 2', '''  first
  | exact a38_shared_conj_half
  | (simp [Complex.ext_iff]; norm_num)
  | simp [Complex.ext_iff]
  | norm_num [Complex.ext_iff]''')
thm('a38_shared_conj_two', 'star (2 : ℂ) = 2', '''  first
  | (simp [Complex.ext_iff, Complex.star_def]; norm_num)
  | simp [Complex.ext_iff, Complex.star_def]
  | norm_num [Complex.ext_iff, Complex.star_def]''')
thm('a38_shared_conj_two\'', '(starRingEnd ℂ) (2 : ℂ) = 2', '''  first
  | exact a38_shared_conj_two
  | (simp [Complex.ext_iff]; norm_num)
  | simp [Complex.ext_iff]
  | norm_num [Complex.ext_iff]''')
thm('a38_shared_inv_of_unit', '∀ x : ℂ, star x * x = 1 → star x = x⁻¹', '''  intro x h
  exact eq_inv_of_mul_eq_one_left h''')
thm('a38_shared_ne_zero_of_unit', '∀ x : ℂ, star x * x = 1 → x ≠ 0', '''  intro x h hx
  rw [hx, mul_zero] at h
  exact zero_ne_one h''')

# ---------------------------------------------------------------- realizability: sixteen row identities, unitarity, flatness
HZS = HZ('z', 'w', 'u')
ROWTAC = "  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hsu, hsz', hsw', hsu', a38_shared_conj_half, a38_shared_conj_half', a38_shared_conj_two, a38_shared_conj_two', map_ofNat] <;> (try simp only [a38_shared_conj_two, a38_shared_conj_two']) <;> (try field_simp) <;> ring"
UNITH = ("  have hsz : star z = z⁻¹ := a38_shared_inv_of_unit z hz\n"
         "  have hsw : star w = w⁻¹ := a38_shared_inv_of_unit w hw\n"
         "  have hsu : star u = u⁻¹ := a38_shared_inv_of_unit u hu\n"
         "  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz\n"
         "  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw\n"
         "  have hsu' : (starRingEnd ℂ) u = u⁻¹ := hsu\n"
         "  have hz0 : z ≠ 0 := a38_shared_ne_zero_of_unit z hz\n"
         "  have hw0 : w ≠ 0 := a38_shared_ne_zero_of_unit w hw\n"
         "  have hu0 : u ≠ 0 := a38_shared_ne_zero_of_unit u hu\n")
for a in range(4):
    for b in range(4):
        row = '((%d : Fin 4), (%d : Fin 4))' % (a, b)
        for c in range(4):
            col = '((%d : Fin 4), d)' % c
            thm('a38_shared_row_core_%d%d_%d' % (a, b, c), '∀ z w u : ℂ, ' + UNITS + '∀ d : Fin 4, ∑ k, ' + HZS + ' ' + row + ' k * star (' + HZS + ' ' + col + ' k) = if ' + row + ' = ' + col + ' then (1 : ℂ) else 0', '  intro z w u hz hw hu d\n' + UNITH + ROWTAC)
        thm('a38_shared_row_core_%d%d' % (a, b), '∀ z w u : ℂ, ' + UNITS + '∀ j : Fin 4 × Fin 4, ∑ k, ' + HZS + ' ' + row + ' k * star (' + HZS + ' j k) = if ' + row + ' = j then (1 : ℂ) else 0', '  intro z w u hz hw hu j\n  obtain ⟨c, d⟩ := j\n  fin_cases c\n' + '\n'.join('  · exact a38_shared_row_core_%d%d_%d z w u hz hw hu d' % (a, b, c) for c in range(4)))
for a in range(4):
    thm('a38_shared_rowblock_core_%d' % a, '∀ z w u : ℂ, ' + UNITS + '∀ (b : Fin 4) (j : Fin 4 × Fin 4), ∑ k, ' + HZS + ' ((%d : Fin 4), b) k * star (' % a + HZS + ' j k) = if ((%d : Fin 4), b) = j then (1 : ℂ) else 0' % a, '  intro z w u hz hw hu b j\n  fin_cases b\n' + '\n'.join('  · exact a38_shared_row_core_%d%d z w u hz hw hu j' % (a, b) for b in range(4)))
thm('a38_shared_rows_core', '∀ z w u : ℂ, ' + UNITS + '∀ i j : Fin 4 × Fin 4, ∑ k, ' + HZS + ' i k * star (' + HZS + ' j k) = if i = j then (1 : ℂ) else 0', '  intro z w u hz hw hu i j\n  obtain ⟨a, b⟩ := i\n  fin_cases a\n' + '\n'.join('  · exact a38_shared_rowblock_core_%d z w u hz hw hu b j' % a for a in range(4)))
thm('a38_shared_unitary_core', '∀ z w u : ℂ, ' + UNITS + HZS + ' ∈ Matrix.unitaryGroup (Fin 4 × Fin 4) ℂ', '  intro z w u hz hw hu\n  rw [Matrix.mem_unitaryGroup_iff]\n  ext i j\n  rw [Matrix.mul_apply, Matrix.one_apply]\n  simp only [Matrix.star_apply]\n  exact a38_shared_rows_core z w u hz hw hu i j')
thm('a38_shared_flat_core', '∀ z w u : ℂ, ' + UNITS + '∀ i j, ‖' + HZS + ' i j‖ = 1 / 4', '''  intro z w u hz hw hu i j
  have hz1 := a35_shared_half z hz i.1 j.1
  have hw1 := a35_shared_half w hw i.2 j.2
  simp only [Matrix.of_apply] at hz1 hw1 ⊢
  rw [norm_mul, norm_mul, hz1, hw1, norm_pow, a35_shared_norm_of_unit u hu, one_pow]
  norm_num''')
thm('a38_shared_real_core', G0 + '∀ z w u : ℂ, ' + UNITS + HZS + ' ∈ Matrix.unitaryGroup (Fin 4 × Fin 4) ℂ ∧ (∀ i j, ‖' + HZS + ' i j‖ = 1 / 4) ∧ RealizableGram (Fin 1 × Fin 1) ' + GAM + ' ' + gram(HZS) + ' ∧ featureVec ' + gram(HZS) + ' ∈ ' + NSET, '''  intro Γ₀ hΓ₀ z w u hz hw hu
  have hU := a38_shared_unitary_core z w u hz hw hu
  have hF := a38_shared_flat_core z w u hz hw hu
  have hR := a35_shared_gram_realizable Γ₀ hΓ₀ _ hU hF
  exact ⟨hU, hF, hR, ⟨_, hR, rfl⟩⟩''')

# ---------------------------------------------------------------- the nine exclusions, column and row forms
def excl_core(name, m, n, cp, rows):
    form = DITAX(name, m, n, cp, rows)
    def key(h, w, transposed):
        p = w['p']
        def ENT(k): return HUC + ' ' + POS(p[k][0]) + ' ' + POS(p[k][1])
        lines = ('    have key : ' + ENT(0) + ' * ' + ENT(1) + ' = ' + ENT(2) + ' * ' + ENT(3) + ''' := by
      rw [''' + h + ''']
      simp only [''' + ('Matrix.transpose_apply, ' if transposed else '') + '''Matrix.of_apply]
      (try simp (config := { decide := true }) [a36_shared_div, a36_shared_mod])
      (try ring)
    simp (config := { decide := true }) [Matrix.of_apply] at key
''')
        if w['rational']:
            coef = w['coef']
            return lines + '''    first
    | linear_combination (''' + str(coef) + ''' : ℂ) * key
    | exact key
    | (ring_nf at key; linear_combination (''' + str(coef) + ''' : ℂ) * key)'''
        # the non-rational identity: c * u^e1 = c * u^e2 with c = z / 16 (monomial i^p z^q w^r / 16)
        p_, q_, r_ = w['monomial']
        cval = ' * '.join(['(Complex.I)'] * p_ + [ZC] * q_ + [WC] * r_) or '(1 : ℂ)'
        sgn = '' if w['e'][0] > w['e'][1] else '-'
        return lines + '''    have h2 : ''' + cval + ''' * (u - 1) = 0 := by
      first
      | linear_combination (''' + sgn + '''16 : ℂ) * key
      | (ring_nf at key; linear_combination (''' + sgn + '''16 : ℂ) * key)
    rcases mul_eq_zero.1 h2 with h3 | h3
    · exfalso
      revert h3
      first
      | (norm_num [Complex.ext_iff])
      | (simp [Complex.ext_iff]; norm_num)
    · linear_combination h3'''
    wc, wr = WIT[name + '_col'], WIT[name + '_row']
    thm('a38_shared_excl_core_' + name, '∀ u : ℂ, star u * u = 1 → (' + EXQ(m, n, form) + ' → u = 1) ∧ (' + EXQ(m, n, form + 'ᵀ') + ' → u = 1)', '''  intro u hu
  refine ⟨?_, ?_⟩
  · rintro ⟨X, Y, D, -, -, -, h⟩
''' + key('h', wc, False) + '''
  · rintro ⟨X, Y, D, -, -, -, h⟩
''' + key('h', wr, True))
for cl in B.CLASSES:
    excl_core(*cl)

# ---------------------------------------------------------------- the base control
K1 = B.CLASSES[0]
BASE_STMT = (G0 + HZ(ZC, WC, '1') + ' = ' + SIGC + ' ∧ ' + FLG('Fin 4', F4(ZC)) + ' ∧ (∀ c : Fin 4, ' + FLG('Fin 4', F4(WC)) + ') ∧ ' + SIGC + ' = ' +
             DITAX(*K1).replace('X i.1 j.1', F4(ZC) + ' i.1 j.1').replace('D j.1 i.2', '(fun (_ : Fin 4) (_ : Fin 4) => (1 : ℂ)) j.1 i.2').replace('Y j.1 i.2 j.2', '(fun (_ : Fin 4) => ' + F4(WC) + ') j.1 i.2 j.2'))
thm('a38_shared_base_core', BASE_STMT, '''  intro Γ₀ hΓ₀
  have hf : ∀ (t : ℂ), star t * t = 1 → ''' + FLG('Fin 4', F4('t')) + ''' := by
    intro t ht
    refine ⟨(a35_shared_f4_flat Γ₀ hΓ₀ t ht).1, ?_⟩
    intro a c
    have h := a35_shared_half t ht a c
    simp only [Matrix.of_apply] at h ⊢
    rw [h]
    norm_num [Fintype.card_fin]
  have hA : ∀ p q : Fin 4, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] p q = p := by
    intro p q; fin_cases p <;> fin_cases q <;> rfl
  have hB : ∀ p q : Fin 4, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] p q = q := by
    intro p q; fin_cases p <;> fin_cases q <;> rfl
  refine ⟨?_, hf _ a36_shared_z_unit, fun _ => hf _ a36_shared_w_unit, ?_⟩
  · ext i j
    simp only [Matrix.of_apply, one_pow, mul_one]
  · ext i j
    simp only [Matrix.of_apply, hA, hB, mul_one]''')

# ---------------------------------------------------------------- the local escape: a unit near 1, entrywise closeness
thm('a38_shared_pow_sub_one', '∀ (u : ℂ) (n : ℕ), ‖u‖ = 1 → ‖u ^ n - 1‖ ≤ n * ‖u - 1‖', '''  intro u n hu
  induction n with
  | zero => simp
  | succ n ih =>
    have e : u ^ (n + 1) - 1 = u ^ n * (u - 1) + (u ^ n - 1) := by ring
    rw [e]
    calc ‖u ^ n * (u - 1) + (u ^ n - 1)‖ ≤ ‖u ^ n * (u - 1)‖ + ‖u ^ n - 1‖ := norm_add_le _ _
      _ = ‖u - 1‖ + ‖u ^ n - 1‖ := by rw [norm_mul, norm_pow, hu, one_pow, one_mul]
      _ ≤ ‖u - 1‖ + n * ‖u - 1‖ := by linarith
      _ = ((n + 1 : ℕ) : ℝ) * ‖u - 1‖ := by push_cast; ring''')
thm('a38_shared_ew_le', '∀ i j : Fin 4 × Fin 4, (' + EW + ') ≤ 3', '''  intro i j
  split_ifs <;> norm_num''')
CAY = '((1 + (t : ℂ) * Complex.I) / (1 - (t : ℂ) * Complex.I))'
thm('a38_shared_cayley_core', '∀ t : ℝ, 0 < t → star ' + CAY + ' * ' + CAY + ' = 1 ∧ ' + CAY + ' ≠ 1 ∧ ‖' + CAY + ' - 1‖ ≤ 2 * t', '''  intro t ht
  have h1 : (1 : ℂ) - (t : ℂ) * Complex.I ≠ 0 := by
    intro h
    have h' := congrArg Complex.re h
    simp at h'
  have h2 : (1 : ℂ) + (t : ℂ) * Complex.I ≠ 0 := by
    intro h
    have h' := congrArg Complex.re h
    simp at h'
  refine ⟨?_, ?_, ?_⟩
  · have hc1 : (starRingEnd ℂ) (1 + (t : ℂ) * Complex.I) = 1 - (t : ℂ) * Complex.I := by
      rw [map_add, map_one, map_mul, Complex.conj_ofReal, Complex.conj_I]
      ring
    have hc2 : (starRingEnd ℂ) (1 - (t : ℂ) * Complex.I) = 1 + (t : ℂ) * Complex.I := by
      rw [map_sub, map_one, map_mul, Complex.conj_ofReal, Complex.conj_I]
      ring
    rw [Complex.star_def, map_div₀, hc1, hc2, div_mul_div_comm, div_eq_one_iff_eq (mul_ne_zero h2 h1)]
    ring
  · intro h
    rw [div_eq_iff h1] at h
    have h' := congrArg Complex.im h
    simp at h'
    linarith
  · have e : ''' + CAY + ''' - 1 = (2 * (t : ℂ) * Complex.I) / (1 - (t : ℂ) * Complex.I) := by
      field_simp
      ring
    have hI : ‖Complex.I‖ = 1 := by
      first
      | exact Complex.norm_I
      | simp
      | norm_num
    rw [e, norm_div, norm_mul, norm_mul, hI, mul_one]
    have hn : 1 ≤ ‖(1 : ℂ) - (t : ℂ) * Complex.I‖ := by
      have h : |((1 : ℂ) - (t : ℂ) * Complex.I).re| ≤ ‖(1 : ℂ) - (t : ℂ) * Complex.I‖ := by
        first
        | exact Complex.abs_re_le_norm _
        | (rw [Complex.norm_eq_abs]; exact Complex.abs_re_le_abs _)
      simpa using h
    have h2n : ‖(2 : ℂ)‖ = 2 := by norm_num
    have htn : ‖(t : ℂ)‖ = t := by rw [Complex.norm_real, Real.norm_eq_abs, abs_of_pos ht]
    rw [h2n, htn]
    have hpos : 0 < ‖(1 : ℂ) - (t : ℂ) * Complex.I‖ := by linarith
    first
    | (rw [div_le_iff hpos]; nlinarith)
    | (rw [div_le_iff₀ hpos]; nlinarith)''')
UC = '((1 + ((ε / 8 : ℝ) : ℂ) * Complex.I) / (1 - ((ε / 8 : ℝ) : ℂ) * Complex.I))'
HUε = HZ(ZC, WC, UC)
EWij = EW
negs = []
for nm, m, n, cp, rows in B.CLASSES:
    negs.append('fun h => hne ((a38_shared_excl_core_%s _ hu).1 h)' % nm)
    negs.append('fun h => hne ((a38_shared_excl_core_%s _ hu).2 h)' % nm)
thm('a38_shared_escape_core', G0 + '∀ ε : ℝ, 0 < ε → ∃ u : ℂ, star u * u = 1 ∧ u ≠ 1 ∧ ‖u - 1‖ < ε ∧ (∀ i j, ‖' + HUC + ' i j - ' + SIGC + ' i j‖ < ε) ∧ RealizableGram (Fin 1 × Fin 1) ' + GAM + ' ' + gram(HUC) + ' ∧ featureVec ' + gram(HUC) + ' ∈ ' + NSET + ' ∧ ' +
    ' ∧ '.join('¬ ' + EXQ(m, n, DITAX(nm, m, n, cp, rows)) + ' ∧ ¬ ' + EXQ(m, n, DITAX(nm, m, n, cp, rows) + 'ᵀ') for nm, m, n, cp, rows in B.CLASSES), '''  intro Γ₀ hΓ₀ ε hε
  obtain ⟨hu, hne, hb⟩ := a38_shared_cayley_core (ε / 8) (by linarith)
  have hR := a38_shared_real_core Γ₀ hΓ₀ _ _ _ a36_shared_z_unit a36_shared_w_unit hu
  refine ⟨_, hu, hne, ?_, ?_, hR.2.2.1, hR.2.2.2, ''' + ', '.join(negs) + '''⟩
  · linarith
  · intro i j
    have hz1 := a35_shared_half _ a36_shared_z_unit i.1 j.1
    have hw1 := a35_shared_half _ a36_shared_w_unit i.2 j.2
    have hn1 := a35_shared_norm_of_unit _ hu
    have h1 := a38_shared_pow_sub_one ''' + UC + ''' (''' + EWij + ''') hn1
    have h2 : (((''' + EWij + ''') : ℕ) : ℝ) ≤ 3 := by exact_mod_cast a38_shared_ew_le i j
    have h3 : (((''' + EWij + ''') : ℕ) : ℝ) * ‖''' + UC + ''' - 1‖ ≤ 3 * ‖''' + UC + ''' - 1‖ := mul_le_mul_of_nonneg_right h2 (norm_nonneg _)
    simp only [Matrix.of_apply] at hz1 hw1 ⊢
    rw [show ∀ x y : ℂ, x * y - x = x * (y - 1) from fun x y => by ring, norm_mul, norm_mul, hz1, hw1]
    linarith [norm_nonneg (''' + UC + ''' ^ (''' + EWij + ''') - 1)]''')

# ---------------------------------------------------------------- the frozen theorems
def frozen(name, key, tail):
    thm(name, PR[key], '  intro Γ₀ hΓ₀\n  dsimp only\n' + tail)
frozen('a38_shared_realizable', 'REAL', '  intro u hu\n  exact a38_shared_real_core Γ₀ hΓ₀ _ _ u a36_shared_z_unit a36_shared_w_unit hu')
for nm, m, n, _, _ in B.CLASSES:
    frozen('a38_shared_excl_' + nm, 'EXCL_' + nm, '  exact a38_shared_excl_core_' + nm)
frozen('a38_c_local_escape', 'ESCAPE', '  exact a38_shared_escape_core Γ₀ hΓ₀')
frozen('a38_control_base', 'BASE', '  exact a38_shared_base_core Γ₀ hΓ₀')
if VERDICT:
    cores = ['fun u hu => a38_shared_real_core Γ₀ hΓ₀ _ _ u a36_shared_z_unit a36_shared_w_unit hu'] + ['a38_shared_excl_core_' + nm for nm, _, _, _, _ in B.CLASSES]
    frozen('a38_witness', 'P_R', '  exact ⟨' + ', '.join(cores) + '⟩')
    n = len(P['PARTS'])
    alts = ' | '.join(['h'] * n)
    proj = ['r' + '.2' * k + ('.1' if k < n - 1 else '') for k in range(n)]
    out.append('theorem a38_c_exclusive :\n    (' + PR['P_N'] + ') → ¬ (' + PR['P_R'] + ''') := by
  intro hN hR
  have h := hN _ rfl
  have r := hR _ rfl
  dsimp only at h r
  rcases h with ''' + alts + '\n' + '\n'.join('  · exact h ' + pj for pj in proj) + '''
#print axioms a38_c_exclusive
''')
HEADER = P['IMPORT'] + '\n' + P['DOC'] + '\nnamespace OIBridge\nnamespace DitaLocalEscape\n\n' + P['OPEN'] + '\n'
sys.stdout.write(HEADER + '\n'.join(out) + 'end DitaLocalEscape\nend OIBridge\n')
