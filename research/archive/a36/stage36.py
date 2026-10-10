"""Emit the A36 module (stage 1 or stage 2) from props36.json: hand-written core lemmas plus the frozen
statements verbatim. usage: python3 stage36.py [--verdict] > mod36.lean"""
import json, os, sys
S = os.path.dirname(os.path.abspath(__file__))
P = json.load(open(os.path.join(S, 'props36.json')))
PR = P['PROPS']
VERDICT = '--verdict' in sys.argv

E16 = 'EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))'
GAM = '(Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2)'
def gram(H):
    return '(fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => star (' + H + ' i j) * ' + H + ' i k)'
NSET = '{x : ' + E16 + ' | ∃ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, RealizableGram (Fin 1 × Fin 1) ' + GAM + ' G ∧ featureVec G = x}'
SSET = '{x : ' + E16 + ' | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => X i.1 j.1 k.1 * Y i.2 j.2 k.2) = x}'
def F4(z):
    return '(Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, ' + z + ', -1, -' + z + '; 1, -1, 1, -1; 1, -' + z + ', -1, ' + z + '] a c)'
def SIG(z, w):
    return '(Matrix.of fun i j : Fin 4 × Fin 4 => ' + F4(z) + ' i.1 j.1 * ' + F4(w) + ' i.2 j.2)'
WT = '(if i.1.val % 2 = 0 ∧ j.1.val % 2 = 0 then (if i.2 = 1 then 1 else 0) + (if j.2 = 1 then 1 else 0) else 0)'
def PU(z, w, u):
    return '(Matrix.of fun i j : Fin 4 × Fin 4 => ' + SIG(z, w) + ' i j * ' + u + ' ^ ' + WT + ')'
def DG(X, Y, D, ab):
    return '(Matrix.of fun i j : ' + ab + ' => ' + X + ' i.1 j.1 * ' + D + ' j.1 i.2 * ' + Y + ' j.1 i.2 j.2)'
def DGT(X, Y, E, ab):
    return '(Matrix.of fun i j : ' + ab + ' => ' + X + ' i.1 j.1 * ' + E + ' i.1 j.2 * ' + Y + ' i.1 i.2 j.2)'
R28 = '(@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2))'
C28 = '(@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))'
R82 = '(@finProdFinEquiv 4 2 (i.1, @Fin.divNat 2 2 i.2), @Fin.modNat 2 2 i.2)'
C82 = '(@finProdFinEquiv 4 2 (j.1, @Fin.divNat 2 2 j.2), @Fin.modNat 2 2 j.2)'
def DITA28(X, Y, D):
    return '(Matrix.of fun i j : Fin 4 × Fin 4 => ' + DG(X, Y, D, 'Fin 2 × Fin 8') + ' ' + R28 + ' ' + C28 + ')'
def DITA82(X, Y, D):
    return '(Matrix.of fun i j : Fin 4 × Fin 4 => ' + DG(X, Y, D, 'Fin 8 × Fin 2') + ' ' + R82 + ' ' + C82 + ')'
def FLG(n, X):
    return '(' + X + ' ∈ Matrix.unitaryGroup (' + n + ') ℂ ∧ ∀ a₁ c₁, ‖' + X + ' a₁ c₁‖ ^ 2 = 1 / (Fintype.card (' + n + ') : ℝ))'
ZC = '(3 / 5 + (4 / 5) * Complex.I)'
WC = '(5 / 13 + (12 / 13) * Complex.I)'
U60 = '(3599 / 3601 + (120 / 3601) * Complex.I)'
G0 = '∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) → '
FPE = '(@finProdFinEquiv 2 4)'

# the witnesses of the line
XO = '(Matrix.of fun a c : Fin 2 => ((1 + Complex.I) / 2) * !![1, 1; 1, -1] a c)'
XI = '(Matrix.of fun a c : Fin 2 => ((1 - Complex.I) / 2) * !![1, 1; 1, -1] a c)'
def EP(c, u):
    return '(fun (a : Fin 2) (d : Fin 4) => if ' + c + ' = 0 ∧ a = 0 then ' + u + ' ^ (if d = 1 then 1 else 0) else (1 : ℂ))'
def ZP(c, z, w, u):
    return '(fun a : Fin 2 => Matrix.of fun b d : Fin 4 => (if ' + c + ' = 1 ∧ a = 1 then ' + z + ' else (1 : ℂ)) * (if ' + c + ' = 0 ∧ a = 0 then ' + u + ' ^ (if b = 1 then 1 else 0) else (1 : ℂ)) * ' + F4(w) + ' b d)'
def YIN(c, z, w, u):
    return DGT(XI, ZP(c, z, w, u), EP(c, u), 'Fin 2 × Fin 4')
def YE(z, w, u):
    return '(fun c : Fin 2 => Matrix.of fun k l : Fin 8 => ' + YIN('c', z, w, u) + ' (' + FPE + '.symm k) (' + FPE + '.symm l))'
DE = '(fun (_ : Fin 2) (_ : Fin 8) => (1 : ℂ))'

E28R = '(((@finProdFinEquiv 2 2).symm.prodCongr (Equiv.refl (Fin 4))).trans ((Equiv.prodAssoc (Fin 2) (Fin 2) (Fin 4)).trans ((Equiv.refl (Fin 2)).prodCongr (@finProdFinEquiv 2 4))))'
E28C = '((((@finProdFinEquiv 2 2).symm.trans (Equiv.prodComm (Fin 2) (Fin 2))).prodCongr (Equiv.refl (Fin 4))).trans ((Equiv.prodAssoc (Fin 2) (Fin 2) (Fin 4)).trans ((Equiv.refl (Fin 2)).prodCongr (@finProdFinEquiv 2 4))))'
E82 = '(((Equiv.refl (Fin 4)).prodCongr (@finProdFinEquiv 2 2).symm).trans ((Equiv.prodAssoc (Fin 4) (Fin 2) (Fin 2)).symm.trans ((@finProdFinEquiv 4 2).prodCongr (Equiv.refl (Fin 2)))))'

out = []
def thm(name, stmt, proof):
    out.append('theorem %s :\n    %s := by\n%s\n#print axioms %s\n' % (name, stmt, proof, name))

# ---------------------------------------------------------------- scalar and unit lemmas
thm('a36_shared_sq_quarter', '∀ x : ℝ, 0 ≤ x → x ^ 2 = 1 / 16 → x = 1 / 4', '''  intro x hx h
  have h2 : (x - 1 / 4) * (x + 1 / 4) = 0 := by ring_nf; linarith
  rcases mul_eq_zero.1 h2 with h3 | h3
  · linarith
  · linarith''')
thm('a36_shared_pow_unit', '∀ (u : ℂ) (n : ℕ), star u * u = 1 → star (u ^ n) * u ^ n = 1', '''  intro u n hu
  rw [star_pow, ← mul_pow, hu, one_pow]''')
thm('a36_shared_z_unit', 'star ' + ZC + ' * ' + ZC + ' = (1 : ℂ)', '''  simp [Complex.ext_iff, Complex.star_def] <;> norm_num''')
thm('a36_shared_w_unit', 'star ' + WC + ' * ' + WC + ' = (1 : ℂ)', '''  simp [Complex.ext_iff, Complex.star_def] <;> norm_num''')
thm('a36_shared_u60_unit', 'star ' + U60 + ' * ' + U60 + ' = (1 : ℂ)', '''  simp [Complex.ext_iff, Complex.star_def] <;> norm_num''')
thm('a36_shared_div', '∀ a : Fin 4, @Fin.divNat 2 2 a = ![0, 0, 1, 1] a', '''  decide''')
thm('a36_shared_mod', '∀ a : Fin 4, @Fin.modNat 2 2 a = ![0, 1, 0, 1] a', '''  decide''')

# ---------------------------------------------------------------- the general construction
GENB = '∀ {α β : Type} [Fintype α] [DecidableEq α] [Fintype β] [DecidableEq β] '
thm('a36_shared_dg_unitary', GENB + '(X : Matrix α α ℂ) (Y : α → Matrix β β ℂ) (D : α → β → ℂ), X ∈ Matrix.unitaryGroup α ℂ → (∀ c, Y c ∈ Matrix.unitaryGroup β ℂ) → (∀ c b, ‖D c b‖ = 1) → ' + DG('X', 'Y', 'D', 'α × β') + ' ∈ Matrix.unitaryGroup (α × β) ℂ', '''  intro α β _ _ _ _ X Y D hX hY hD
  rw [Matrix.mem_unitaryGroup_iff]
  have hX' := Matrix.mem_unitaryGroup_iff.1 hX
  have hY' := fun c => Matrix.mem_unitaryGroup_iff.1 (hY c)
  have hDD : ∀ c b, D c b * star (D c b) = 1 := fun c b => by
    rw [mul_comm]; exact a35_shared_unit_of_norm _ (hD c b)
  ext i i'
  rw [Matrix.mul_apply, Matrix.one_apply]
  simp only [Matrix.star_apply, Matrix.of_apply]
  rw [Fintype.sum_prod_type]
  have key : ∀ c : α, ∑ d : β, X i.1 c * D c i.2 * Y c i.2 d * star (X i'.1 c * D c i'.2 * Y c i'.2 d)
      = X i.1 c * star (X i'.1 c) * (D c i.2 * star (D c i'.2)) * (Y c * star (Y c)) i.2 i'.2 := by
    intro c
    rw [Matrix.mul_apply, Finset.mul_sum]
    refine Finset.sum_congr rfl fun d _ => ?_
    simp only [Matrix.star_apply, star_mul]
    ring
  simp only [key, hY', Matrix.one_apply]
  have hx := congrFun (congrFun hX' i.1) i'.1
  rw [Matrix.mul_apply, Matrix.one_apply] at hx
  simp only [Matrix.star_apply] at hx
  by_cases h2 : i.2 = i'.2
  · simp only [h2, if_true, mul_one, hDD]
    rw [hx]
    by_cases h1 : i.1 = i'.1
    · simp [h1, Prod.ext_iff, h2]
    · simp [h1, Prod.ext_iff]
  · simp [h2, Prod.ext_iff]''')
thm('a36_shared_dgT_eq', '∀ {α β : Type} (X : Matrix α α ℂ) (Y : α → Matrix β β ℂ) (E : α → β → ℂ), ' + DGT('X', 'Y', 'E', 'α × β') + ' = ' + DG('Xᵀ', '(fun a => (Y a)ᵀ)', 'E', 'α × β') + 'ᵀ', '''  intro α β X Y E
  ext i j
  simp only [Matrix.transpose_apply, Matrix.of_apply]''')
thm('a36_shared_dgT_unitary', GENB + '(X : Matrix α α ℂ) (Y : α → Matrix β β ℂ) (E : α → β → ℂ), X ∈ Matrix.unitaryGroup α ℂ → (∀ a, Y a ∈ Matrix.unitaryGroup β ℂ) → (∀ a d, ‖E a d‖ = 1) → ' + DGT('X', 'Y', 'E', 'α × β') + ' ∈ Matrix.unitaryGroup (α × β) ℂ', '''  intro α β _ _ _ _ X Y E hX hY hE
  rw [a36_shared_dgT_eq]
  exact transpose_unitary (a36_shared_dg_unitary Xᵀ (fun a => (Y a)ᵀ) E (transpose_unitary hX) (fun a => transpose_unitary (hY a)) hE)''')
thm('a36_shared_reindex_unitary', '∀ {m n : Type} [Fintype m] [DecidableEq m] [Fintype n] [DecidableEq n] (M : Matrix n n ℂ) (r c : m → n), Function.Bijective r → Function.Bijective c → M ∈ Matrix.unitaryGroup n ℂ → (Matrix.of fun i j : m => M (r i) (c j)) ∈ Matrix.unitaryGroup m ℂ', '''  intro m n _ _ _ _ M r c hr hc hM
  rw [Matrix.mem_unitaryGroup_iff] at hM ⊢
  ext i i'
  rw [Matrix.mul_apply, Matrix.one_apply]
  simp only [Matrix.star_apply, Matrix.of_apply]
  have h := congrFun (congrFun hM (r i)) (r i')
  rw [Matrix.mul_apply, Matrix.one_apply] at h
  simp only [Matrix.star_apply] at h
  rw [show (∑ j, M (r i) (c j) * star (M (r i') (c j))) = ∑ j, M (r i) j * star (M (r i') j) from
    Function.Bijective.sum_comp hc (fun j => M (r i) j * star (M (r i') j)), h]
  simp only [hr.injective.eq_iff]''')
thm('a36_shared_dg_norm_sq', GENB + '(X : Matrix α α ℂ) (Y : α → Matrix β β ℂ) (D : α → β → ℂ), (∀ a c, ‖X a c‖ ^ 2 = 1 / (Fintype.card α : ℝ)) → (∀ c, ∀ b d, ‖Y c b d‖ ^ 2 = 1 / (Fintype.card β : ℝ)) → (∀ c b, ‖D c b‖ = 1) → ∀ i j : α × β, ‖X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2‖ ^ 2 = 1 / ((Fintype.card α : ℝ) * (Fintype.card β : ℝ))', '''  intro α β _ _ _ _ X Y D hX hY hD i j
  rw [norm_mul, norm_mul, mul_pow, mul_pow, hX, hD, hY, one_pow, mul_one, div_mul_div_comm, one_mul]''')
thm('a36_shared_dgT_norm_sq', GENB + '(X : Matrix α α ℂ) (Y : α → Matrix β β ℂ) (E : α → β → ℂ), (∀ a c, ‖X a c‖ ^ 2 = 1 / (Fintype.card α : ℝ)) → (∀ a, ∀ b d, ‖Y a b d‖ ^ 2 = 1 / (Fintype.card β : ℝ)) → (∀ a d, ‖E a d‖ = 1) → ∀ i j : α × β, ‖X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2‖ ^ 2 = 1 / ((Fintype.card α : ℝ) * (Fintype.card β : ℝ))', '''  intro α β _ _ _ _ X Y E hX hY hE i j
  rw [norm_mul, norm_mul, mul_pow, mul_pow, hX, hE, hY, one_pow, mul_one, div_mul_div_comm, one_mul]''')

# ---------------------------------------------------------------- the hull cores
def SUB(M):
    return M + '.submatrix eR.symm eC.symm'
HG = DG('X', 'Y', 'D', 'α × β')
HGT = DGT('X', 'Y', 'E', 'α × β')
thm('a36_shared_hullg_core', G0 + GENB + '(eR eC : α × β ≃ Fin 4 × Fin 4) (X : Matrix α α ℂ) (Y : α → Matrix β β ℂ) (D : α → β → ℂ), ' + FLG('α', 'X') + ' → (∀ c, ' + FLG('β', 'Y c') + ') → (∀ c b, ‖D c b‖ = 1) →\n    ' + SUB(HG) + ' ∈ Matrix.unitaryGroup (Fin 4 × Fin 4) ℂ ∧ (∀ i j, ‖' + SUB(HG) + ' i j‖ = 1 / 4) ∧ RealizableGram (Fin 1 × Fin 1) ' + GAM + ' ' + gram(SUB(HG)), '''  intro Γ₀ hΓ₀ α β _ _ _ _ eR eC X Y D hX hY hD
  have hcard0 : Fintype.card α * Fintype.card β = 16 := by
    rw [← Fintype.card_prod, Fintype.card_congr eR]; simp
  have hcard : (Fintype.card α : ℝ) * (Fintype.card β : ℝ) = 16 := by exact_mod_cast hcard0
  have hu : ''' + SUB(HG) + ''' ∈ Matrix.unitaryGroup (Fin 4 × Fin 4) ℂ :=
    a36_shared_reindex_unitary ''' + HG + ''' eR.symm eC.symm eR.symm.bijective eC.symm.bijective (a36_shared_dg_unitary X Y D hX.1 (fun c => (hY c).1) hD)
  have hn : ∀ i j, ‖''' + SUB(HG) + ''' i j‖ = 1 / 4 := by
    intro i j
    apply a36_shared_sq_quarter _ (norm_nonneg _)
    simp only [Matrix.submatrix_apply, Matrix.of_apply]
    rw [a36_shared_dg_norm_sq X Y D hX.2 (fun c => (hY c).2) hD, hcard]
  exact ⟨hu, hn, a35_shared_gram_realizable Γ₀ hΓ₀ _ hu hn⟩''')
thm('a36_shared_hullgt_core', G0 + GENB + '(eR eC : α × β ≃ Fin 4 × Fin 4) (X : Matrix α α ℂ) (Y : α → Matrix β β ℂ) (E : α → β → ℂ), ' + FLG('α', 'X') + ' → (∀ c, ' + FLG('β', 'Y c') + ') → (∀ c d, ‖E c d‖ = 1) →\n    ' + SUB(HGT) + ' ∈ Matrix.unitaryGroup (Fin 4 × Fin 4) ℂ ∧ (∀ i j, ‖' + SUB(HGT) + ' i j‖ = 1 / 4) ∧ RealizableGram (Fin 1 × Fin 1) ' + GAM + ' ' + gram(SUB(HGT)), '''  intro Γ₀ hΓ₀ α β _ _ _ _ eR eC X Y E hX hY hE
  have hcard0 : Fintype.card α * Fintype.card β = 16 := by
    rw [← Fintype.card_prod, Fintype.card_congr eR]; simp
  have hcard : (Fintype.card α : ℝ) * (Fintype.card β : ℝ) = 16 := by exact_mod_cast hcard0
  have hu : ''' + SUB(HGT) + ''' ∈ Matrix.unitaryGroup (Fin 4 × Fin 4) ℂ :=
    a36_shared_reindex_unitary ''' + HGT + ''' eR.symm eC.symm eR.symm.bijective eC.symm.bijective (a36_shared_dgT_unitary X Y E hX.1 (fun c => (hY c).1) hE)
  have hn : ∀ i j, ‖''' + SUB(HGT) + ''' i j‖ = 1 / 4 := by
    intro i j
    apply a36_shared_sq_quarter _ (norm_nonneg _)
    simp only [Matrix.submatrix_apply, Matrix.of_apply]
    rw [a36_shared_dgT_norm_sq X Y E hX.2 (fun c => (hY c).2) hE, hcard]
  exact ⟨hu, hn, a35_shared_gram_realizable Γ₀ hΓ₀ _ hu hn⟩''')

H28 = DITA28('X', 'Y', 'D'); H82 = DITA82('X', 'Y', 'D')
thm('a36_shared_hull28_core', G0 + '∀ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), ' + FLG('Fin 2', 'X') + ' → (∀ c, ' + FLG('Fin 8', 'Y c') + ') → (∀ c b, ‖D c b‖ = 1) →\n    ' + H28 + ' ∈ Matrix.unitaryGroup (Fin 4 × Fin 4) ℂ ∧ (∀ i j, ‖' + H28 + ' i j‖ = 1 / 4) ∧ RealizableGram (Fin 1 × Fin 1) ' + GAM + ' ' + gram(H28), '''  intro Γ₀ hΓ₀ X Y D hX hY hD
  first
  | exact a36_shared_hullg_core Γ₀ hΓ₀ ''' + E28R + '''.symm ''' + E28C + '''.symm X Y D hX hY hD
  | (have hr : Function.Bijective (fun i : Fin 4 × Fin 4 => ''' + R28 + ''') :=
      (Fintype.bijective_iff_injective_and_card _).2 ⟨by decide, by decide⟩
     have hc : Function.Bijective (fun j : Fin 4 × Fin 4 => ''' + C28 + ''') :=
      (Fintype.bijective_iff_injective_and_card _).2 ⟨by decide, by decide⟩
     have hu : ''' + H28 + ''' ∈ Matrix.unitaryGroup (Fin 4 × Fin 4) ℂ :=
      a36_shared_reindex_unitary ''' + DG('X', 'Y', 'D', 'Fin 2 × Fin 8') + ''' (fun i => ''' + R28 + ''') (fun j => ''' + C28 + ''') hr hc (a36_shared_dg_unitary X Y D hX.1 (fun c => (hY c).1) hD)
     have hn : ∀ i j, ‖''' + H28 + ''' i j‖ = 1 / 4 := by
       intro i j
       apply a36_shared_sq_quarter _ (norm_nonneg _)
       simp only [Matrix.of_apply]
       rw [a36_shared_dg_norm_sq X Y D hX.2 (fun c => (hY c).2) hD]
       norm_num [Fintype.card_fin]
     exact ⟨hu, hn, a35_shared_gram_realizable Γ₀ hΓ₀ _ hu hn⟩)''')
thm('a36_shared_hull82_core', G0 + '∀ (X : Matrix (Fin 8) (Fin 8) ℂ) (Y : Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) (D : Fin 8 → Fin 2 → ℂ), ' + FLG('Fin 8', 'X') + ' → (∀ c, ' + FLG('Fin 2', 'Y c') + ') → (∀ c b, ‖D c b‖ = 1) →\n    ' + H82 + ' ∈ Matrix.unitaryGroup (Fin 4 × Fin 4) ℂ ∧ (∀ i j, ‖' + H82 + ' i j‖ = 1 / 4) ∧ RealizableGram (Fin 1 × Fin 1) ' + GAM + ' ' + gram(H82), '''  intro Γ₀ hΓ₀ X Y D hX hY hD
  first
  | exact a36_shared_hullg_core Γ₀ hΓ₀ ''' + E82 + '''.symm ''' + E82 + '''.symm X Y D hX hY hD
  | (have hr : Function.Bijective (fun i : Fin 4 × Fin 4 => ''' + R82 + ''') :=
      (Fintype.bijective_iff_injective_and_card _).2 ⟨by decide, by decide⟩
     have hc : Function.Bijective (fun j : Fin 4 × Fin 4 => ''' + C82 + ''') :=
      (Fintype.bijective_iff_injective_and_card _).2 ⟨by decide, by decide⟩
     have hu : ''' + H82 + ''' ∈ Matrix.unitaryGroup (Fin 4 × Fin 4) ℂ :=
      a36_shared_reindex_unitary ''' + DG('X', 'Y', 'D', 'Fin 8 × Fin 2') + ''' (fun i => ''' + R82 + ''') (fun j => ''' + C82 + ''') hr hc (a36_shared_dg_unitary X Y D hX.1 (fun c => (hY c).1) hD)
     have hn : ∀ i j, ‖''' + H82 + ''' i j‖ = 1 / 4 := by
       intro i j
       apply a36_shared_sq_quarter _ (norm_nonneg _)
       simp only [Matrix.of_apply]
       rw [a36_shared_dg_norm_sq X Y D hX.2 (fun c => (hY c).2) hD]
       norm_num [Fintype.card_fin]
     exact ⟨hu, hn, a35_shared_gram_realizable Γ₀ hΓ₀ _ hu hn⟩)''')

# ---------------------------------------------------------------- the line: witnesses
thm('a36_shared_xo_flat', FLG('Fin 2', XO), '''  refine ⟨?_, ?_⟩
  · rw [Matrix.mem_unitaryGroup_iff]
    ext i j
    rw [Matrix.mul_apply, Matrix.one_apply, Fin.sum_univ_two]
    simp only [Matrix.star_apply, Matrix.of_apply]
    fin_cases i <;> fin_cases j <;> simp [Complex.ext_iff, Complex.star_def] <;> norm_num
  · intro a c
    rw [← Complex.normSq_eq_norm_sq, Complex.normSq_apply, Fintype.card_fin]
    simp only [Matrix.of_apply]
    fin_cases a <;> fin_cases c <;> simp <;> norm_num''')
thm('a36_shared_xi_flat', FLG('Fin 2', XI), '''  refine ⟨?_, ?_⟩
  · rw [Matrix.mem_unitaryGroup_iff]
    ext i j
    rw [Matrix.mul_apply, Matrix.one_apply, Fin.sum_univ_two]
    simp only [Matrix.star_apply, Matrix.of_apply]
    fin_cases i <;> fin_cases j <;> simp [Complex.ext_iff, Complex.star_def] <;> norm_num
  · intro a c
    rw [← Complex.normSq_eq_norm_sq, Complex.normSq_apply, Fintype.card_fin]
    simp only [Matrix.of_apply]
    fin_cases a <;> fin_cases c <;> simp <;> norm_num''')
thm('a36_shared_phase_unitary', '∀ {n : Type} [Fintype n] [DecidableEq n] (M : Matrix n n ℂ) (s : ℂ) (p : n → ℂ), M ∈ Matrix.unitaryGroup n ℂ → star s * s = 1 → (∀ b, star (p b) * p b = 1) → (Matrix.of fun b d : n => s * p b * M b d) ∈ Matrix.unitaryGroup n ℂ', '''  intro n _ _ M s p hM hs hp
  have hs' : s * star s = 1 := by rw [mul_comm]; exact hs
  have hp' : ∀ b, p b * star (p b) = 1 := fun b => by rw [mul_comm]; exact hp b
  rw [Matrix.mem_unitaryGroup_iff] at hM ⊢
  ext b b'
  have h := congrFun (congrFun hM b) b'
  rw [Matrix.mul_apply, Matrix.one_apply] at h
  simp only [Matrix.star_apply] at h
  rw [Matrix.mul_apply, Matrix.one_apply]
  simp only [Matrix.star_apply, Matrix.of_apply]
  have key : ∀ d, s * p b * M b d * star (s * p b' * M b' d) = (s * star s) * (p b * star (p b')) * (M b d * star (M b' d)) := by
    intro d; simp only [star_mul]; ring
  simp only [key, ← Finset.mul_sum, h]
  by_cases hb : b = b'
  · subst hb
    rw [if_pos rfl, mul_one, hs', hp', mul_one]
  · rw [if_neg hb, mul_zero]''')
ZPA = ZP('c', 'z', 'w', 'u')
thm('a36_shared_zp_flat', G0 + '∀ (z w u : ℂ), star z * z = 1 → star w * w = 1 → star u * u = 1 → ∀ (c a : Fin 2), ' + FLG('Fin 4', ZPA + ' a'), '''  intro Γ₀ hΓ₀ z w u hz hw hu c a
  have hs : star (if c = 1 ∧ a = 1 then z else (1 : ℂ)) * (if c = 1 ∧ a = 1 then z else (1 : ℂ)) = 1 := by
    split_ifs <;> first | exact hz | simp
  have hp : ∀ b : Fin 4, star (if c = 0 ∧ a = 0 then u ^ (if b = 1 then 1 else 0) else (1 : ℂ)) * (if c = 0 ∧ a = 0 then u ^ (if b = 1 then 1 else 0) else (1 : ℂ)) = 1 := by
    intro b
    split_ifs <;> first | exact a36_shared_pow_unit u _ hu | simp
  refine ⟨?_, ?_⟩
  · exact a36_shared_phase_unitary ''' + F4('w') + ''' _ _ (a35_shared_f4_flat Γ₀ hΓ₀ w hw).1 hs hp
  · intro b d
    show ‖(if c = 1 ∧ a = 1 then z else (1 : ℂ)) * (if c = 0 ∧ a = 0 then u ^ (if b = 1 then 1 else 0) else (1 : ℂ)) * ((1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] b d)‖ ^ 2 = 1 / (Fintype.card (Fin 4) : ℝ)
    have h3 : ‖(1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] b d‖ = 1 / 2 := a35_shared_half w hw b d
    rw [norm_mul, norm_mul, a35_shared_norm_of_unit _ hs, a35_shared_norm_of_unit _ (hp b), h3, Fintype.card_fin]
    norm_num''')
YEA = YE('z', 'w', 'u')
thm('a36_shared_y8_flat', G0 + '∀ (z w u : ℂ), star z * z = 1 → star w * w = 1 → star u * u = 1 → ∀ c : Fin 2, ' + FLG('Fin 8', YEA + ' c'), '''  intro Γ₀ hΓ₀ z w u hz hw hu c
  have hE : ∀ (a : Fin 2) (d : Fin 4), ‖''' + EP('c', 'u') + ''' a d‖ = 1 := by
    intro a d
    show ‖(if c = 0 ∧ a = 0 then u ^ (if d = 1 then 1 else 0) else (1 : ℂ))‖ = 1
    split_ifs <;> first | exact a35_shared_norm_of_unit _ (a36_shared_pow_unit u _ hu) | simp
  have hZ := a36_shared_zp_flat Γ₀ hΓ₀ z w u hz hw hu c
  have hU := a36_shared_dgT_unitary ''' + XI + ''' ''' + ZPA + ''' ''' + EP('c', 'u') + ''' a36_shared_xi_flat.1 (fun a => (hZ a).1) hE
  refine ⟨?_, ?_⟩
  · exact a36_shared_reindex_unitary ''' + YIN('c', 'z', 'w', 'u') + ''' ''' + FPE + '''.symm ''' + FPE + '''.symm ''' + FPE + '''.symm.bijective ''' + FPE + '''.symm.bijective hU
  · intro k l
    show ‖''' + XI + ''' (''' + FPE + '''.symm k).1 (''' + FPE + '''.symm l).1 * ''' + EP('c', 'u') + ''' (''' + FPE + '''.symm k).1 (''' + FPE + '''.symm l).2 * ''' + ZPA + ''' (''' + FPE + '''.symm k).1 (''' + FPE + '''.symm k).2 (''' + FPE + '''.symm l).2‖ ^ 2 = 1 / (Fintype.card (Fin 8) : ℝ)
    rw [a36_shared_dgT_norm_sq ''' + XI + ''' ''' + ZPA + ''' ''' + EP('c', 'u') + ''' a36_shared_xi_flat.2 (fun a => (hZ a).2) hE]
    norm_num [Fintype.card_fin]''')
thm('a36_shared_nested_eq', '∀ z w u : ℂ, ' + PU('z', 'w', 'u') + ' = ' + DITA28(XO, YEA, DE), '''  intro z w u
  ext ⟨a, b⟩ ⟨c, d⟩
  simp only [Matrix.of_apply, Equiv.symm_apply_apply]
  fin_cases a <;> fin_cases c <;> simp (config := { decide := true }) [a36_shared_div, a36_shared_mod] <;> (try split_ifs) <;> ring_nf <;> (try simp only [Complex.I_sq]) <;> (try ring)''')
PUZ = PU('z', 'w', 'u')
thm('a36_shared_line_core', G0 + '∀ (z w u : ℂ), star z * z = 1 → star w * w = 1 → star u * u = 1 →\n    (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), ' + FLG('Fin 2', 'X') + ' ∧ (∀ c, ' + FLG('Fin 8', 'Y c') + ') ∧ (∀ c b, ‖D c b‖ = 1) ∧ ' + PUZ + ' = ' + DITA28('X', 'Y', 'D') + ')\n    ∧ RealizableGram (Fin 1 × Fin 1) ' + GAM + ' ' + gram(PUZ) + ' ∧ featureVec ' + gram(PUZ) + ' ∈ ' + NSET, '''  intro Γ₀ hΓ₀ z w u hz hw hu
  have hX := a36_shared_xo_flat
  have hY := a36_shared_y8_flat Γ₀ hΓ₀ z w u hz hw hu
  have hD : ∀ (c : Fin 2) (b : Fin 8), ‖''' + DE + ''' c b‖ = 1 := fun c b => by simp
  have hid := a36_shared_nested_eq z w u
  have hh := a36_shared_hull28_core Γ₀ hΓ₀ ''' + XO + ''' ''' + YEA + ''' ''' + DE + ''' hX hY hD
  refine ⟨⟨_, _, _, hX, hY, hD, hid⟩, ?_, ?_⟩
  · rw [hid]; exact hh.2.2
  · rw [hid]; exact ⟨_, hh.2.2, rfl⟩''')

# ---------------------------------------------------------------- the point and the control
PUC = PU(ZC, WC, U60)
COORD = '((((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (1 : Fin 4))), (((0 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (0 : Fin 4))))'
thm('a36_shared_p_val', gram(PUC) + ' (0, 0) (0, 0) (1, 0) * ' + gram(PUC) + ' (0, 1) (1, 0) (0, 0) = ' + U60 + ' / 256', '''  simp (config := { decide := true }) [Matrix.of_apply, Complex.star_def, Complex.ext_iff] <;> norm_num''')
thm('a36_shared_p_notin', G0 + 'featureVec ' + gram(PUC) + ' ∉ ' + SSET, '''  intro Γ₀ hΓ₀ hS
  obtain ⟨X, Y, hX, hY, hxy⟩ := hS
  have hq := (a34_shared_feature_ext _ _).1 hxy ''' + COORD + '''
  have hc := a35_shared_cross_core Γ₀ hΓ₀ X Y hX hY 0 0 1 0 1 0
  have hd := a35_shared_diag_core Γ₀ hΓ₀ X Y hX hY 0 1 0 0
  have hL : mixedTriple (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => X i.1 j.1 k.1 * Y i.2 j.2 k.2) ''' + COORD + ''' = 1 / 4096 := by
    simp only [mixedTriple, Matrix.of_apply] at hc hd ⊢
    rw [hc, hd]
    norm_num
  rw [hL] at hq
  simp (config := { decide := true }) [mixedTriple, Matrix.of_apply, Complex.star_def, Complex.ext_iff, map_add, map_mul, map_div₀, map_ofNat, map_neg, map_one] at hq <;> norm_num at hq''')
thm('a36_shared_point_core', G0 + 'star ' + U60 + ' * ' + U60 + ' = 1 ∧ RealizableGram (Fin 1 × Fin 1) ' + GAM + ' ' + gram(PUC) + ' ∧ featureVec ' + gram(PUC) + ' ∈ ' + NSET + ' ∧ featureVec ' + gram(PUC) + ' ∉ ' + SSET + '\n  ∧ ' + gram(PUC) + ' (0, 0) (0, 0) (1, 0) * ' + gram(PUC) + ' (0, 1) (1, 0) (0, 0) = ' + U60 + ' / 256', '''  intro Γ₀ hΓ₀
  have hl := a36_shared_line_core Γ₀ hΓ₀ _ _ _ a36_shared_z_unit a36_shared_w_unit a36_shared_u60_unit
  exact ⟨a36_shared_u60_unit, hl.2.1, hl.2.2, a36_shared_p_notin Γ₀ hΓ₀, a36_shared_p_val⟩''')
SIGC = SIG(ZC, WC)
def UD(z):
    return '(Matrix.of fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, ' + z + ', -1, -' + z + '; 1, -1, 1, -1; 1, -' + z + ', -1, ' + z + '] p.1 q.1)'
thm('a36_shared_one_core', G0 + PU(ZC, WC, '1') + ' = ' + SIGC + ' ∧ featureVec ' + gram(SIGC) + ' ∈ ' + SSET, '''  intro Γ₀ hΓ₀
  refine ⟨?_, ?_⟩
  · ext i j
    simp only [Matrix.of_apply, one_pow, mul_one]
  · refine ⟨FibreGram (0 : Fin 1) ''' + UD(ZC) + ''', FibreGram (0 : Fin 1) ''' + UD(WC) + ''', sh1_necessity (hadamard_z_admissible Γ₀ hΓ₀ _ a36_shared_z_unit), sh1_necessity (hadamard_z_admissible Γ₀ hΓ₀ _ a36_shared_w_unit), ?_⟩
    congr 1
    funext i
    ext j k
    simp only [Matrix.of_apply]
    rw [fibreGram_apply, fibreGram_apply, Fin.sum_univ_one, Fin.sum_univ_one]
    simp only [Matrix.of_apply, star_mul]
    ring''')

# ---------------------------------------------------------------- the frozen theorems
def frozen(name, key, tail):
    thm(name, PR[key], '  intro Γ₀ hΓ₀\n  dsimp only\n' + tail)
frozen('a36_shared_hull_g', 'HULLG', '  intro α β _ _ _ _ eR eC X Y D hX hY hD\n  exact a36_shared_hullg_core Γ₀ hΓ₀ eR eC X Y D hX hY hD')
frozen('a36_shared_hull_gt', 'HULLGT', '  intro α β _ _ _ _ eR eC X Y E hX hY hE\n  exact a36_shared_hullgt_core Γ₀ hΓ₀ eR eC X Y E hX hY hE')
frozen('a36_control_hull28', 'HULL28', '  intro X Y D hX hY hD\n  exact a36_shared_hull28_core Γ₀ hΓ₀ X Y D hX hY hD')
frozen('a36_control_hull82', 'HULL82', '  intro X Y D hX hY hD\n  exact a36_shared_hull82_core Γ₀ hΓ₀ X Y D hX hY hD')
frozen('a36_shared_line', 'LINE', '  intro u hu\n  exact a36_shared_line_core Γ₀ hΓ₀ _ _ u a36_shared_z_unit a36_shared_w_unit hu')
frozen('a36_shared_point', 'POINT', '  exact a36_shared_point_core Γ₀ hΓ₀')
frozen('a36_control_stratum', 'ONE', '  exact a36_shared_one_core Γ₀ hΓ₀')
if VERDICT:
    frozen('a36_hierarchy', 'P_R', '''  refine ⟨?_, ?_, ?_, ?_⟩
  · intro α β _ _ _ _ eR eC X Y D hX hY hD
    exact a36_shared_hullg_core Γ₀ hΓ₀ eR eC X Y D hX hY hD
  · intro α β _ _ _ _ eR eC X Y E hX hY hE
    exact a36_shared_hullgt_core Γ₀ hΓ₀ eR eC X Y E hX hY hE
  · intro u hu
    exact a36_shared_line_core Γ₀ hΓ₀ _ _ u a36_shared_z_unit a36_shared_w_unit hu
  · exact a36_shared_point_core Γ₀ hΓ₀''')
    out.append('theorem a36_c_exclusive :\n    (' + PR['P_N'] + ') → ¬ (' + PR['P_R'] + ''') := by
  intro hN hR
  have h := hN _ rfl
  have r := hR _ rfl
  dsimp only at h r
  rcases h with h | h | h | h
  · exact h r.1
  · exact h r.2.1
  · exact h r.2.2.1
  · exact h r.2.2.2
#print axioms a36_c_exclusive
''')

HEADER = P['IMPORT'] + '\n' + P['DOC'] + '\nnamespace OIBridge\nnamespace DitaHierarchy\n\n' + P['OPEN'] + '\n'
text = HEADER + '\n'.join(out) + 'end DitaHierarchy\nend OIBridge\n'
sys.stdout.write(text)
