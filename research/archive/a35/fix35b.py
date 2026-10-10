import re
p = 'build35_mod.py'
s = open(p, encoding='utf-8').read()
def rep(old, new, count=1):
    global s
    assert s.count(old) == count, (s.count(old), old[:80])
    s = s.replace(old, new)

# (j) notin cores: normalise hc, hd and the goal alike before rewriting
rep("             '    simp only [mixedTriple]\\n'\n             '    rw [hc, hd]\\n'",
    "             '    simp only [mixedTriple, Matrix.of_apply] at hc hd ⊢\\n'\n             '    rw [hc, hd]\\n'")
rep("      simp only [mixedTriple]\n      rw [hc, hd]", "      simp only [mixedTriple, Matrix.of_apply] at hc hd ⊢\n      rw [hc, hd]")

# (l) real_core: beta-reduce before split_ifs
rep("  · intro c b\n    split_ifs <;> simp\n  · ''' + SIMPEV", "  · intro c b\n    dsimp only\n    split_ifs <;> simp\n  · ''' + SIMPEV")

# (k) real_im: factorwise imaginary parts
old_start = s.index("thm('a35_shared_real_im'")
old_end = s.index("thm('a35_shared_real_core'")
new_real_im = ("thm('a35_shared_real_im', '∀ i j : Fin 4 × Fin 4, ((' + HR + ') i j).im = 0', '''  intro i j\n"
"  have hM : ∀ a c : Fin 4, ((1 / 2 : ℂ) * (!![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, 1, -1; 1, -1, -1, 1] : Matrix (Fin 4) (Fin 4) ℂ) a c).im = 0 := by\n"
"    intro a c\n"
"    fin_cases a <;> fin_cases c <;> simp\n"
"  have h2 : ∀ c b : Fin 4, (if c = 3 ∧ b = 3 then (-1 : ℂ) else 1).im = 0 := by\n"
"    intro c b\n"
"    split_ifs <;> simp\n"
"  have key : ∀ x y w : ℂ, x.im = 0 → y.im = 0 → w.im = 0 → (x * y * w).im = 0 := by\n"
"    intro x y w hx hy hw\n"
"    simp [Complex.mul_im, hx, hy, hw]\n"
"  exact key _ _ _ (hM i.1 j.1) (h2 j.1 i.2) (hM i.2 j.2)''')\n")
s = s[:old_start] + new_real_im + s[old_end:]

# (m) conj_unitary without unitary.star_mem
old_start = s.index("thm('a35_shared_conj_unitary'")
old_end = s.index("DC = 'fun i : Fin 4 × Fin 4")
new_conj = ("thm('a35_shared_conj_unitary', '∀ A : ' + M4 + ', A ∈ Matrix.unitaryGroup (Fin 4) ℂ → (Matrix.of fun a c : Fin 4 => star (A a c)) ∈ Matrix.unitaryGroup (Fin 4) ℂ', '''  intro A hA\n"
"  rw [Matrix.mem_unitaryGroup_iff] at hA ⊢\n"
"  ext i j\n"
"  have h := congrFun (congrFun hA j) i\n"
"  rw [Matrix.mul_apply, Matrix.one_apply] at h ⊢\n"
"  simp only [Matrix.star_apply, Matrix.of_apply, star_star] at h ⊢\n"
"  rw [Finset.sum_congr rfl (fun k _ => mul_comm (star (A i k)) (A j k)), h]\n"
"  by_cases hij : i = j\n"
"  · subst hij\n"
"    simp\n"
"  · simp [hij, Ne.symm hij]''')\n")
s = s[:old_start] + new_conj + s[old_end:]

# (n) ext_core: beta/submatrix/transpose normalisation in the norm obligations
rep("fun a c => hX.2 _ _⟩, fun c => ⟨a35_shared_perm_unitary _ π₂ τ₂ (hY _).1, fun a d => (hY _).2 _ _⟩",
    "fun a c => by simp only [Matrix.submatrix_apply]; exact hX.2 _ _⟩, fun c => ⟨a35_shared_perm_unitary _ π₂ τ₂ (hY _).1, fun a d => by simp only [Matrix.submatrix_apply]; exact (hY _).2 _ _⟩")
rep("fun a c => by rw [Matrix.transpose_apply]; exact hX.2 c a⟩, fun a => ⟨transpose_unitary (hY a).1, fun b d => by rw [Matrix.transpose_apply]; exact (hY a).2 d b⟩",
    "fun a c => by simp only [Matrix.transpose_apply]; exact hX.2 c a⟩, fun a => ⟨transpose_unitary (hY a).1, fun b d => by simp only [Matrix.transpose_apply]; exact (hY a).2 d b⟩")

# (p) mod_core: rw closes the goal; use exact
rep("  rw [this]\n  ring''')", "  exact this''')")

# (o) zn: the surviving side goal is ‖n + I‖ ≠ 0
rep("""  refine ⟨?_, hne⟩
  have hst : star ((n : ℂ) + Complex.I) = (n : ℂ) - Complex.I := by
    simp [Complex.star_def, Complex.conj_I, sub_eq_add_neg]
  rw [norm_div, ← hst, norm_star, div_self]
  rw [hst]
  exact norm_ne_zero_iff.2 hne''')""",
"""  have hne2 : ((n : ℂ) + Complex.I) ≠ 0 := by
    intro h
    have := congrArg Complex.im h
    simp at this
  refine ⟨?_, hne⟩
  have hst : star ((n : ℂ) + Complex.I) = (n : ℂ) - Complex.I := by
    simp [Complex.star_def, Complex.conj_I, sub_eq_add_neg]
  rw [norm_div, ← hst, norm_star, div_self (norm_ne_zero_iff.2 hne2)]''')""")

# (inf) explicit forms of the four twist equations
rep("""      have h00 := huv 0 0
      have h01 := huv 0 1
      have h10 := huv 1 0
      have h11 := huv 1 1
      simp only [] at h00 h01 h10 h11
      simp at h00 h01 h10 h11
      apply a35_shared_zn_inj
      linear_combination h11 + ''' + ZN + ''' * u 1 * v 1 * h00 - ''' + ZN + ''' * u 0 * v 1 * h10 - ''' + ZN + ''' * h01""",
"""      have hx00 : ¬((0 : Fin 4) = 1 ∧ (0 : Fin 4) = 1) := by decide
      have hx01 : ¬((0 : Fin 4) = 1 ∧ (1 : Fin 4) = 1) := by decide
      have hx10 : ¬((1 : Fin 4) = 1 ∧ (0 : Fin 4) = 1) := by decide
      have hx11 : ((1 : Fin 4) = 1 ∧ (1 : Fin 4) = 1) := by decide
      have h00 : ''' + ITE('0', '0', ZNM) + ''' = u 0 * v 0 * ''' + ITE('0', '0', ZN) + ''' := huv 0 0
      have h01 : ''' + ITE('0', '1', ZNM) + ''' = u 0 * v 1 * ''' + ITE('0', '1', ZN) + ''' := huv 0 1
      have h10 : ''' + ITE('1', '0', ZNM) + ''' = u 1 * v 0 * ''' + ITE('1', '0', ZN) + ''' := huv 1 0
      have h11 : ''' + ITE('1', '1', ZNM) + ''' = u 1 * v 1 * ''' + ITE('1', '1', ZN) + ''' := huv 1 1
      rw [if_neg hx00, if_neg hx00] at h00
      rw [if_neg hx01, if_neg hx01] at h01
      rw [if_neg hx10, if_neg hx10] at h10
      rw [if_pos hx11, if_pos hx11] at h11
      apply a35_shared_zn_inj
      linear_combination -h11 + ''' + ZN + ''' * h10 + ''' + ZN + ''' * u 1 * v 0 * h01 - ''' + ZN + ''' * u 1 * v 1 * h00""")
rep("DN = '(fun c b : Fin 4 => if c = 1 ∧ b = 1 then ' + ZN + ' else (1 : ℂ))'\n",
    "DN = '(fun c b : Fin 4 => if c = 1 ∧ b = 1 then ' + ZN + ' else (1 : ℂ))'\n"
    "ZNM = ZN.replace('(n : ℂ)', '(m : ℂ)')\n"
    "def ITE(c, b, z): return '(if (%s : Fin 4) = 1 ∧ (%s : Fin 4) = 1 then %s else (1 : ℂ))' % (c, b, z)\n")

# (i) witness core split into per-conjunct lemmas
old_start = s.index("thm('a35_shared_wit_core', HYP0 + ' ' + CO['WIT']")
old_end = s.index("# ---------------------------------------------------------------- off-stratum by a coordinate")
wit_body_start = s.index("WIT_BODY = (", old_start)
wit_body_end = s.index("thm('a35_shared_wit_core', HYP0 + '\\n  ' + WIT_BODY", wit_body_start)
wit_body = s[wit_body_start:wit_body_end]
new_wit = wit_body + (
"HULLSET = '{x : ' + E16 + ' | ∃ (X : ' + M4 + ') (Y : Fin 4 → ' + M4 + ') (D : Fin 4 → Fin 4 → ℂ), ' + FL('X') + ' ∧ (∀ c, ' + FL('(Y c)') + ') ∧ (∀ c b, ‖D c b‖ = 1) ∧ featureVec (' + GRAM(DITA()) + ') = x}'\n"
"SSET = '{x : ' + E16 + ' | ∃ X Y : ' + TUP + ', ' + RG + ' X ∧ ' + RG + ' Y ∧ featureVec (' + PROD + ') = x}'\n"
"thm('a35_shared_wit_mem', HYP0 + ' featureVec (' + GRAM(H34) + ') ∈ ' + HULLSET, '''  intro Γ₀ hΓ₀\n"
"  have hI : star Complex.I * Complex.I = 1 := by simp\n"
"  refine ⟨''' + F4('Complex.I') + ''', ''' + YTW + ''', fun _ _ => 1, a35_shared_f4_flat Γ₀ hΓ₀ Complex.I hI, ?_, fun _ _ => by simp, ?_⟩\n"
"  · intro c\n"
"    show ''' + FL(F4('(if c.val % 2 = 0 then Complex.I else -Complex.I)')) + '''\n"
"    exact a35_shared_f4_flat Γ₀ hΓ₀ _ (by split_ifs <;> simp)\n"
"  · rw [a35_shared_wit_eq]''')\n"
"thm('a35_shared_wit_notin', HYP0 + ' featureVec (' + GRAM(H34) + ') ∉ ' + SSET, '''  intro Γ₀ hΓ₀ hS\n"
"  have h34 := a34_control_proper Γ₀ hΓ₀\n"
"  dsimp only at h34\n"
"  obtain ⟨X, Y, hX, hY, hxy⟩ := hS\n"
"  exact h34.2 X Y hxy''')\n"
"thm('a35_shared_wit_val', '(' + GRAM(H34) + ') (0, 1) (0, 1) (1, 1) * (' + GRAM(H34) + ') (0, 0) (1, 1) (0, 1) = -(1 / 256)', '  ' + SIMPEV + ' <;> norm_num')\n"
"thm('a35_shared_wit_feat', 'featureVec (' + GRAM(H34) + ') = featureVec (fun i => ((' + GRAM(KU) + ') i).submatrix (' + RHO + ') (' + RHO + '))', '  congr 1\\n  funext i\\n  ext j k\\n  show star ((' + H34 + ') i j) * (' + H34 + ') i k = star ((' + KU + ') i ((' + RHO + ') j)) * (' + KU + ') i ((' + RHO + ') k)\\n  rw [a35_shared_wit_rel i j, a35_shared_wit_rel i k]')\n"
"thm('a35_shared_wit_core', HYP0 + '\\n  ' + WIT_BODY, '''  intro Γ₀ hΓ₀\n"
"  exact ⟨a35_shared_wit_eq, a35_shared_wit_mem Γ₀ hΓ₀, a35_shared_wit_notin Γ₀ hΓ₀, a35_shared_wit_val, a35_shared_wit_rel, a35_shared_wit_feat⟩''')\n\n")
s = s[:old_start] + new_wit + s[old_end:]
open(p, 'w', encoding='utf-8').write(s)
print('edits h-p applied')
