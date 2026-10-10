"""Emit the A39 module (stage 1 or, with --verdict, stage 2) from props39.json: hand-written core lemmas plus the
frozen statements verbatim. usage: python3 stage39.py [--verdict] > mod39.lean"""
import json, os, sys
S = os.path.dirname(os.path.abspath(__file__))
P = json.load(open(os.path.join(S, 'props39.json'))); PR = P['PROPS']
VERDICT = '--verdict' in sys.argv
src36 = open(os.path.join(S, '..', 'a36', 'stage36.py'), encoding='utf-8').read()
exec(src36[src36.index('E16 = '):src36.index('# the witnesses of the line')])
EA, EB, EC = P['EA'], P['EB'], P['EC']
EW = EA + ' + ' + EB + ' + ' + EC
def H3(z, w, u1, u2, u3):
    return ('(Matrix.of fun i j : Fin 4 × Fin 4 => ' + SIG(z, w) + ' i j * ' + u1 + ' ^ ' + EA + ' * ' + u2 + ' ^ ' + EB +
            ' * ' + u3 + ' ^ ' + EC + ')')
def HU(z, w, u):
    return '(Matrix.of fun i j : Fin 4 × Fin 4 => ' + SIG(z, w) + ' i j * ' + u + ' ^ (' + EW + '))'
H3S = H3('z', 'w', 'u₁', 'u₂', 'u₃')
UNITS = 'star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → '
ARGS = 'z w u₁ u₂ u₃ hz hw h1 h2 h3'
out = []
def thm(name, stmt, proof):
    out.append('theorem %s :\n    %s := by\n%s\n#print axioms %s\n' % (name, stmt, proof, name))

# ---------------------------------------------------------------- conjugates and units
thm('a39_shared_conj_half', 'star (1 / 2 : ℂ) = 1 / 2', '''  first
  | (simp [Complex.ext_iff, Complex.star_def]; norm_num)
  | simp [Complex.ext_iff, Complex.star_def]
  | norm_num [Complex.ext_iff, Complex.star_def]''')
thm('a39_shared_conj_half_ring', '(starRingEnd ℂ) (1 / 2 : ℂ) = 1 / 2', '''  first
  | exact a39_shared_conj_half
  | (simp [Complex.ext_iff]; norm_num)
  | simp [Complex.ext_iff]
  | norm_num [Complex.ext_iff]''')
thm('a39_shared_conj_two', 'star (2 : ℂ) = 2', '''  first
  | (simp [Complex.ext_iff, Complex.star_def]; norm_num)
  | simp [Complex.ext_iff, Complex.star_def]
  | norm_num [Complex.ext_iff, Complex.star_def]''')
thm('a39_shared_conj_two_ring', '(starRingEnd ℂ) (2 : ℂ) = 2', '''  first
  | exact a39_shared_conj_two
  | (simp [Complex.ext_iff]; norm_num)
  | simp [Complex.ext_iff]
  | norm_num [Complex.ext_iff]''')
thm('a39_shared_inv_of_unit', '∀ x : ℂ, star x * x = 1 → star x = x⁻¹', '''  intro x h
  exact eq_inv_of_mul_eq_one_left h''')
thm('a39_shared_ne_zero_of_unit', '∀ x : ℂ, star x * x = 1 → x ≠ 0', '''  intro x h hx
  rw [hx, mul_zero] at h
  exact zero_ne_one h''')

# ---------------------------------------------------------------- realizability: row identities by column block
UNITH = ''.join('  have hs%s : star %s = %s⁻¹ := a39_shared_inv_of_unit %s %s\n  have hs%s\' : (starRingEnd ℂ) %s = %s⁻¹ := hs%s\n  have h0%s : %s ≠ 0 := a39_shared_ne_zero_of_unit %s %s\n'
                % (t, v, v, v, hv, t, v, v, t, t, v, v, hv) for t, v, hv in (('z', 'z', 'hz'), ('w', 'w', 'hw'), ('1', 'u₁', 'h1'), ('2', 'u₂', 'h2'), ('3', 'u₃', 'h3')))
SIMPSET = ('Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hs1, hs2, hs3, hsz\', hsw\', hs1\', hs2\', hs3\', '
           'a39_shared_conj_half, a39_shared_conj_half_ring, a39_shared_conj_two, a39_shared_conj_two_ring, map_ofNat')
ROWTAC = ('  fin_cases d <;> simp (config := { decide := true }) [' + SIMPSET + '] <;> (try simp only [a39_shared_conj_two, a39_shared_conj_two_ring]) '
          '<;> (try field_simp) <;> ring')
for a in range(4):
    for b in range(4):
        row = '((%d : Fin 4), (%d : Fin 4))' % (a, b)
        for c in range(4):
            col = '((%d : Fin 4), d)' % c
            thm('a39_shared_row_core_%d%d_%d' % (a, b, c), '∀ z w u₁ u₂ u₃ : ℂ, ' + UNITS + '∀ d : Fin 4, ∑ k, ' + H3S + ' ' + row + ' k * star (' + H3S + ' ' + col +
                ' k) = if ' + row + ' = ' + col + ' then (1 : ℂ) else 0', '  intro ' + ARGS + ' d\n' + UNITH + ROWTAC)
        thm('a39_shared_row_core_%d%d' % (a, b), '∀ z w u₁ u₂ u₃ : ℂ, ' + UNITS + '∀ j : Fin 4 × Fin 4, ∑ k, ' + H3S + ' ' + row + ' k * star (' + H3S +
            ' j k) = if ' + row + ' = j then (1 : ℂ) else 0',
            '  intro ' + ARGS + ' j\n  obtain ⟨c, d⟩ := j\n  fin_cases c\n' + '\n'.join('  · exact a39_shared_row_core_%d%d_%d %s d' % (a, b, c, ARGS) for c in range(4)))
for a in range(4):
    thm('a39_shared_rowblock_core_%d' % a, '∀ z w u₁ u₂ u₃ : ℂ, ' + UNITS + '∀ (b : Fin 4) (j : Fin 4 × Fin 4), ∑ k, ' + H3S + ' ((%d : Fin 4), b) k * star (' % a + H3S +
        ' j k) = if ((%d : Fin 4), b) = j then (1 : ℂ) else 0' % a,
        '  intro ' + ARGS + ' b j\n  fin_cases b\n' + '\n'.join('  · exact a39_shared_row_core_%d%d %s j' % (a, b, ARGS) for b in range(4)))
thm('a39_shared_rows_core', '∀ z w u₁ u₂ u₃ : ℂ, ' + UNITS + '∀ i j : Fin 4 × Fin 4, ∑ k, ' + H3S + ' i k * star (' + H3S + ' j k) = if i = j then (1 : ℂ) else 0',
    '  intro ' + ARGS + ' i j\n  obtain ⟨a, b⟩ := i\n  fin_cases a\n' + '\n'.join('  · exact a39_shared_rowblock_core_%d %s b j' % (a, ARGS) for a in range(4)))
thm('a39_shared_unitary_core', '∀ z w u₁ u₂ u₃ : ℂ, ' + UNITS + H3S + ' ∈ Matrix.unitaryGroup (Fin 4 × Fin 4) ℂ',
    '  intro ' + ARGS + '\n  rw [Matrix.mem_unitaryGroup_iff]\n  ext i j\n  rw [Matrix.mul_apply, Matrix.one_apply]\n  simp only [Matrix.star_apply]\n  exact a39_shared_rows_core ' + ARGS + ' i j')
thm('a39_shared_flat_core', '∀ z w u₁ u₂ u₃ : ℂ, ' + UNITS + '∀ i j, ‖' + H3S + ' i j‖ = 1 / 4', '''  intro ''' + ARGS + ''' i j
  have hz1 := a35_shared_half z hz i.1 j.1
  have hw1 := a35_shared_half w hw i.2 j.2
  simp only [Matrix.of_apply] at hz1 hw1 ⊢
  rw [norm_mul, norm_mul, norm_mul, norm_mul, hz1, hw1, norm_pow, norm_pow, norm_pow, a35_shared_norm_of_unit u₁ h1, a35_shared_norm_of_unit u₂ h2, a35_shared_norm_of_unit u₃ h3, one_pow, one_pow, one_pow]
  norm_num''')
thm('a39_shared_real_core', G0 + '∀ z w u₁ u₂ u₃ : ℂ, ' + UNITS + H3S + ' ∈ Matrix.unitaryGroup (Fin 4 × Fin 4) ℂ ∧ (∀ i j, ‖' + H3S + ' i j‖ = 1 / 4) ∧ RealizableGram (Fin 1 × Fin 1) ' +
    GAM + ' ' + gram(H3S) + ' ∧ featureVec ' + gram(H3S) + ' ∈ ' + NSET, '''  intro Γ₀ hΓ₀ ''' + ARGS + '''
  have hU := a39_shared_unitary_core ''' + ARGS + '''
  have hF := a39_shared_flat_core ''' + ARGS + '''
  have hR := a35_shared_gram_realizable Γ₀ hΓ₀ _ hU hF
  exact ⟨hU, hF, hR, ⟨_, hR, rfl⟩⟩''')

# ---------------------------------------------------------------- the controls
thm('a39_shared_base_core', H3(ZC, WC, '1', '1', '1') + ' = ' + SIG(ZC, WC), '''  ext i j
  simp only [Matrix.of_apply, one_pow, mul_one]''')
thm('a39_shared_diag_core', '∀ u : ℂ, ' + H3(ZC, WC, 'u', 'u', 'u') + ' = ' + HU(ZC, WC, 'u'), '''  intro u
  ext i j
  simp only [Matrix.of_apply]
  rw [pow_add, pow_add]
  ring''')

# ---------------------------------------------------------------- the frozen theorems
def frozen(name, key, tail):
    thm(name, PR[key], '  intro Γ₀ hΓ₀\n  dsimp only\n' + tail)
frozen('a39_shared_realizable', 'REAL', '  intro u₁ u₂ u₃ h1 h2 h3\n  exact a39_shared_real_core Γ₀ hΓ₀ _ _ u₁ u₂ u₃ a36_shared_z_unit a36_shared_w_unit h1 h2 h3')
frozen('a39_control_base', 'BASE', '  exact a39_shared_base_core')
frozen('a39_control_diagonal', 'DIAG', '  exact a39_shared_diag_core')
if VERDICT:
    frozen('a39_realizable', 'P_R', '  exact fun u₁ u₂ u₃ h1 h2 h3 => a39_shared_real_core Γ₀ hΓ₀ _ _ u₁ u₂ u₃ a36_shared_z_unit a36_shared_w_unit h1 h2 h3')
    out.append('theorem a39_c_exclusive :\n    (' + PR['P_N'] + ') → ¬ (' + PR['P_R'] + ''') := by
  intro hN hR
  have h := hN _ rfl
  have r := hR _ rfl
  dsimp only at h r
  exact h r
#print axioms a39_c_exclusive
''')
HEADER = P['IMPORT'] + '\n' + P['DOC'] + '\nnamespace OIBridge\nnamespace DitaTorus\n\n' + P['OPEN'] + '\n'
sys.stdout.write(HEADER + '\n'.join(out) + 'end DitaTorus\nend OIBridge\n')
