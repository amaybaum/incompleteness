import os
S = os.path.dirname(os.path.abspath(__file__))
p = os.path.join(S, 'stage38.py'); s = open(p, encoding='utf-8').read()
def sub(old, new, n=1):
    global s
    assert s.count(old) == n, (old[:70], s.count(old)); s = s.replace(old, new)
i = s.index("HZS = HZ('z', 'w', 'u')"); j = s.index("thm('a38_shared_flat_core'")
Q = "'''"
NEW = (
"HZS = HZ('z', 'w', 'u')\n"
"ROWTAC = \"  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hsu, hsz', hsw', hsu', a38_shared_conj_half, a38_shared_conj_half', a38_shared_conj_two, a38_shared_conj_two', map_ofNat] <;> (try simp only [a38_shared_conj_two, a38_shared_conj_two']) <;> (try field_simp) <;> ring\"\n"
"UNITH = (\"  have hsz : star z = z⁻¹ := a38_shared_inv_of_unit z hz\\n\"\n"
"         \"  have hsw : star w = w⁻¹ := a38_shared_inv_of_unit w hw\\n\"\n"
"         \"  have hsu : star u = u⁻¹ := a38_shared_inv_of_unit u hu\\n\"\n"
"         \"  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz\\n\"\n"
"         \"  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw\\n\"\n"
"         \"  have hsu' : (starRingEnd ℂ) u = u⁻¹ := hsu\\n\"\n"
"         \"  have hz0 : z ≠ 0 := a38_shared_ne_zero_of_unit z hz\\n\"\n"
"         \"  have hw0 : w ≠ 0 := a38_shared_ne_zero_of_unit w hw\\n\"\n"
"         \"  have hu0 : u ≠ 0 := a38_shared_ne_zero_of_unit u hu\\n\")\n"
"for a in range(4):\n"
"    for b in range(4):\n"
"        row = '((%d : Fin 4), (%d : Fin 4))' % (a, b)\n"
"        for c in range(4):\n"
"            col = '((%d : Fin 4), d)' % c\n"
"            thm('a38_shared_row_core_%d%d_%d' % (a, b, c), '∀ z w u : ℂ, ' + UNITS + '∀ d : Fin 4, ∑ k, ' + HZS + ' ' + row + ' k * star (' + HZS + ' ' + col + ' k) = if ' + row + ' = ' + col + ' then (1 : ℂ) else 0', '  intro z w u hz hw hu d\\n' + UNITH + ROWTAC)\n"
"        thm('a38_shared_row_core_%d%d' % (a, b), '∀ z w u : ℂ, ' + UNITS + '∀ j : Fin 4 × Fin 4, ∑ k, ' + HZS + ' ' + row + ' k * star (' + HZS + ' j k) = if ' + row + ' = j then (1 : ℂ) else 0', '  intro z w u hz hw hu j\\n  obtain ⟨c, d⟩ := j\\n  fin_cases c\\n' + '\\n'.join('  · exact a38_shared_row_core_%d%d_%d z w u hz hw hu d' % (a, b, c) for c in range(4)))\n"
"for a in range(4):\n"
"    thm('a38_shared_rowblock_core_%d' % a, '∀ z w u : ℂ, ' + UNITS + '∀ (b : Fin 4) (j : Fin 4 × Fin 4), ∑ k, ' + HZS + ' ((%d : Fin 4), b) k * star (' % a + HZS + ' j k) = if ((%d : Fin 4), b) = j then (1 : ℂ) else 0' % a, '  intro z w u hz hw hu b j\\n  fin_cases b\\n' + '\\n'.join('  · exact a38_shared_row_core_%d%d z w u hz hw hu j' % (a, b) for b in range(4)))\n"
"thm('a38_shared_rows_core', '∀ z w u : ℂ, ' + UNITS + '∀ i j : Fin 4 × Fin 4, ∑ k, ' + HZS + ' i k * star (' + HZS + ' j k) = if i = j then (1 : ℂ) else 0', '  intro z w u hz hw hu i j\\n  obtain ⟨a, b⟩ := i\\n  fin_cases a\\n' + '\\n'.join('  · exact a38_shared_rowblock_core_%d z w u hz hw hu b j' % a for a in range(4)))\n"
"thm('a38_shared_unitary_core', '∀ z w u : ℂ, ' + UNITS + HZS + ' ∈ Matrix.unitaryGroup (Fin 4 × Fin 4) ℂ', '  intro z w u hz hw hu\\n  rw [Matrix.mem_unitaryGroup_iff]\\n  ext i j\\n  rw [Matrix.mul_apply, Matrix.one_apply]\\n  simp only [Matrix.star_apply]\\n  exact a38_shared_rows_core z w u hz hw hu i j')\n"
)
s = s[:i] + NEW + s[j:]
sub("      (try simp)\n      (try ring)\n    simp (config := { decide := true }) [Matrix.of_apply] at key\n",
    "      (try simp (config := { decide := true }) [a36_shared_div, a36_shared_mod])\n      (try ring)\n    simp (config := { decide := true }) [Matrix.of_apply] at key\n")
old_cay = ("  · rw [Complex.star_def, map_div₀, map_add, map_sub, map_one, map_mul, Complex.conj_ofReal, Complex.conj_I]\n"
           "    first\n"
           "    | (rw [div_mul_div_comm, div_eq_one_iff_eq (mul_ne_zero h2 h1)]; ring)\n"
           "    | (field_simp; ring)\n"
           "    | (field_simp; ring_nf; simp [Complex.I_sq]; ring)")
new_cay = ("  · have hc1 : (starRingEnd ℂ) (1 + (t : ℂ) * Complex.I) = 1 - (t : ℂ) * Complex.I := by\n"
           "      rw [map_add, map_one, map_mul, Complex.conj_ofReal, Complex.conj_I]\n"
           "      ring\n"
           "    have hc2 : (starRingEnd ℂ) (1 - (t : ℂ) * Complex.I) = 1 + (t : ℂ) * Complex.I := by\n"
           "      rw [map_sub, map_one, map_mul, Complex.conj_ofReal, Complex.conj_I]\n"
           "      ring\n"
           "    rw [Complex.star_def, map_div₀, hc1, hc2, div_mul_div_comm, div_eq_one_iff_eq (mul_ne_zero h2 h1)]\n"
           "    ring")
sub(old_cay, new_cay)
open(p, 'w', encoding='utf-8').write(s); print('patched')
