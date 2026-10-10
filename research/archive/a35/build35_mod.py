"""A35 development module generator: shared lemmas + frozen theorems (proofs), for the disposable branch.
usage: python3 build35_mod.py [--no-verdict]  -> writes mod35.lean"""
import json, os, sys
S = os.path.dirname(os.path.abspath(__file__))
P = json.load(open(os.path.join(S, 'props35.json')))
PR, T, CO = P['PROPS'], P['THEOREMS'], P['COMPONENTS']
import importlib.util
spec = importlib.util.spec_from_file_location('b35', os.path.join(S, 'build35.py')); B = importlib.util.module_from_spec(spec); spec.loader.exec_module(B)
sys.path.insert(0, os.path.join(S, '..', 'a34')); import build34 as B34

V = 'Fin 4 × Fin 4'
M4 = 'Matrix (Fin 4) (Fin 4) ℂ'
M16 = 'Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ'
TUP16 = 'Fin 4 × Fin 4 → ' + M16
TUP = B34.TUP
E16 = B34.E16
GAM = 'Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2'
RG16 = 'RealizableGram (Fin 1 × Fin 1) (' + GAM + ')'
RG = B34.RG
HYP0 = '∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →'
def DITA(X='X', Y='Y', D='D'): return 'Matrix.of fun i j : Fin 4 × Fin 4 => %s i.1 j.1 * %s j.1 i.2 * %s j.1 i.2 j.2' % (X, D, Y)
def DITAT(X='X', Y='Y', E='E'): return 'Matrix.of fun i j : Fin 4 × Fin 4 => %s i.1 j.1 * %s i.1 j.2 * %s i.1 i.2 j.2' % (X, E, Y)
def GRAM(H): return 'fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => star ((%s) i j) * (%s) i k' % (H, H)
def FL(X): return '(%s ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a₁ c₁ : Fin 4, ‖%s a₁ c₁‖ = 1 / 2)' % (X, X)
F4LIT = '!![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z]'
def F4(z): return '(Matrix.of fun a₀ c₀ : Fin 4 => (1 / 2 : ℂ) * %s a₀ c₀)' % F4LIT.replace('z', z)
F4I, F4T = B34.F4I, B34.F4T
H34 = 'Matrix.of fun i j : Fin 4 × Fin 4 => (1 / 4 : ℂ) * ' + F4I + ' i.1 j.1 * ' + F4T + ' i.2 j.2'
H34U = 'Matrix.of fun i j : Fin 4 × Fin 4 => (1 / 4 : ℂ) * ' + F4I + ' i.1 j.1 * ' + F4I + ' i.2 j.2'
PROD = 'fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => X i.1 j.1 k.1 * Y i.2 j.2 k.2'
def PRODXY(X, Y): return 'fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => (%s) i.1 j.1 k.1 * (%s) i.2 j.2 k.2' % (X, Y)
RHO = CO['RHO']
FTW = 'F4 (if c.val % 2 = 0 then Complex.I else -Complex.I)'
YTW = '(fun c : Fin 4 => ' + F4('(if c.val % 2 = 0 then Complex.I else -Complex.I)') + ')'
KU = DITA(F4('Complex.I'), '(fun _ : Fin 4 => ' + F4('Complex.I') + ')', '(fun _ _ : Fin 4 => (1 : ℂ))')
DW = '(fun c b : Fin 4 => if c = 1 then ![1, Complex.I, 1, -Complex.I] b else (1 : ℂ))'
HW = DITA(F4('Complex.I'), '(fun _ : Fin 4 => ' + F4('Complex.I') + ')', DW)
DR = '(fun c b : Fin 4 => if c = 3 ∧ b = 3 then (-1 : ℂ) else 1)'
HR = DITA(F4('1'), '(fun _ : Fin 4 => ' + F4('1') + ')', DR)
TUP0 = '(fun i => (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I] p.1 q.1)) ((' + B34.RTAB + ' 0).1 i)).submatrix (' + B34.RTAB + ' 0).2 (' + B34.RTAB + ' 0).2)'
SIG = 'Equiv.swap ((0 : Fin 4), (1 : Fin 4)) ((1 : Fin 4), (0 : Fin 4))'
FAMX = '{x : ' + E16 + ' | ∃ D : Fin 4 → Fin 4 → ℂ, (∀ c b, ‖D c b‖ = 1) ∧ x = featureVec (' + GRAM(DITA(F4('Complex.I'), '(fun _ : Fin 4 => ' + F4('Complex.I') + ')', 'D')) + ')}'
SIMPEV = 'simp [mixedTriple, Matrix.submatrix_apply, fibreGram_apply, Fin.sum_univ_one, Equiv.swap_apply_def, Equiv.trans_apply, Matrix.of_apply, Complex.star_def, Complex.conj_I, Complex.ext_iff, Fintype.sum_prod_type, Fin.sum_univ_four]'

L = []
def thm(name, stmt, proof):
    L.append('theorem %s :\n    %s := by\n%s\n#print axioms %s\n' % (name, stmt, proof, name))

# ---------------------------------------------------------------- arithmetic helpers
thm('a35_shared_star_mul', '∀ z : ℂ, star z * z = ((‖z‖ ^ 2 : ℝ) : ℂ)', '''  intro z
  rw [mul_comm, RCLike.star_def, Complex.mul_conj]
  norm_cast
  exact Complex.normSq_eq_norm_sq _''')
thm('a35_shared_unit_of_norm', '∀ z : ℂ, ‖z‖ = 1 → star z * z = 1', '''  intro z h
  rw [a35_shared_star_mul, h]
  norm_num''')
thm('a35_shared_norm_of_unit', '∀ z : ℂ, star z * z = 1 → ‖z‖ = 1', '''  intro z h
  have h2 : ‖z‖ ^ 2 = 1 := by
    have := a35_shared_star_mul z
    rw [h] at this
    exact_mod_cast this.symm
  have h0 : 0 ≤ ‖z‖ := norm_nonneg z
  have h3 : (‖z‖ - 1) * (‖z‖ + 1) = 0 := by ring_nf; linarith
  rcases mul_eq_zero.1 h3 with h4 | h4
  · linarith
  · linarith''')
thm('a35_shared_ne_zero', '∀ (z : ℂ) (r : ℝ), 0 < r → ‖z‖ = r → z ≠ 0', '''  intro z r hr h hz
  rw [hz, norm_zero] at h
  linarith''')
thm('a35_shared_half', '∀ z : ℂ, star z * z = 1 → ∀ a c : Fin 4, ‖((1 / 2 : ℂ) * ![![1, 1, 1, 1], ![1, z, -1, -z], ![1, -1, 1, -1], ![1, -z, -1, z]] a c)‖ = 1 / 2', '''  intro z hz a c
  have h1 : ‖z‖ = 1 := a35_shared_norm_of_unit z hz
  have h12 : ‖(1 / 2 : ℂ)‖ = 1 / 2 := by
    rw [show (1 / 2 : ℂ) = ((1 / 2 : ℝ) : ℂ) by push_cast; ring, Complex.norm_real]
    norm_num
  rw [norm_mul, h12]
  fin_cases a <;> fin_cases c <;> simp [h1]''')
thm('a35_shared_f4_flat', HYP0 + ' ∀ z : ℂ, star z * z = 1 → ' + FL(F4('z')), '''  intro Γ₀ hΓ₀ z hz
  refine ⟨?_, ?_⟩
  · have h := vpart_unitary (hadamard_z_admissible Γ₀ hΓ₀ z hz).1
    have e : (Matrix.of fun i j : Fin 4 => (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * ''' + F4LIT + ''' p.1 q.1)) (i, 0) (j, 0)) = ''' + F4('z') + ''' := by
      ext a c
      simp only [Matrix.of_apply]
    rw [e] at h
    exact h
  · intro a c
    show ‖(1 / 2 : ℂ) * ''' + F4LIT + ''' a c‖ = 1 / 2
    exact a35_shared_half z hz a c''')

# ---------------------------------------------------------------- the constructions
thm('a35_shared_dita_unitary', '∀ (X : ' + M4 + ') (Y : Fin 4 → ' + M4 + ') (D : Fin 4 → Fin 4 → ℂ), X ∈ Matrix.unitaryGroup (Fin 4) ℂ → (∀ c, Y c ∈ Matrix.unitaryGroup (Fin 4) ℂ) → (∀ c b, ‖D c b‖ = 1) → (' + DITA() + ') ∈ Matrix.unitaryGroup (Fin 4 × Fin 4) ℂ', '''  intro X Y D hX hY hD
  rw [Matrix.mem_unitaryGroup_iff]
  have hX' := Matrix.mem_unitaryGroup_iff.1 hX
  have hY' := fun c => Matrix.mem_unitaryGroup_iff.1 (hY c)
  have hDD : ∀ c b, D c b * star (D c b) = 1 := fun c b => by
    rw [mul_comm]; exact a35_shared_unit_of_norm _ (hD c b)
  ext i i'
  rw [Matrix.mul_apply, Matrix.one_apply]
  simp only [Matrix.star_apply, Matrix.of_apply]
  rw [Fintype.sum_prod_type]
  have key : ∀ c : Fin 4, ∑ d : Fin 4, X i.1 c * D c i.2 * Y c i.2 d * star (X i'.1 c * D c i'.2 * Y c i'.2 d)
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
thm('a35_shared_dita_norm', '∀ (X : ' + M4 + ') (Y : Fin 4 → ' + M4 + ') (D : Fin 4 → Fin 4 → ℂ), (∀ a c : Fin 4, ‖X a c‖ = 1 / 2) → (∀ c, ∀ a d : Fin 4, ‖Y c a d‖ = 1 / 2) → (∀ c b, ‖D c b‖ = 1) → ∀ i j : Fin 4 × Fin 4, ‖(' + DITA() + ') i j‖ = 1 / 4', '''  intro X Y D hX hY hD i j
  show ‖X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2‖ = 1 / 4
  rw [norm_mul, norm_mul, hX, hD, hY]
  norm_num''')
thm('a35_shared_pad_unitary', '∀ H : ' + M16 + ', H ∈ Matrix.unitaryGroup (Fin 4 × Fin 4) ℂ → (Matrix.of fun p q : (Fin 4 × Fin 4) × (Fin 1 × Fin 1) => H p.1 q.1) ∈ Matrix.unitaryGroup ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ℂ', '''  intro H hH
  have hsum : ∀ f : (Fin 4 × Fin 4) × (Fin 1 × Fin 1) → ℂ, ∑ x, f x = ∑ r : Fin 4 × Fin 4, f (r, ((0 : Fin 1), (0 : Fin 1))) := by
    intro f
    rw [Fintype.sum_prod_type]
    exact Finset.sum_congr rfl (fun r _ => by rw [Fintype.sum_prod_type, Fin.sum_univ_one, Fin.sum_univ_one])
  rw [Matrix.mem_unitaryGroup_iff', Matrix.star_eq_conjTranspose] at hH ⊢
  ext ⟨p, a⟩ ⟨q, b⟩
  have hab : a = b := Subsingleton.elim a b
  subst hab
  have hpq := congrFun (congrFun hH p) q
  rw [Matrix.mul_apply, Matrix.one_apply] at hpq
  simp only [Matrix.conjTranspose_apply] at hpq
  rw [Matrix.mul_apply, Matrix.one_apply, hsum]
  simp only [Matrix.conjTranspose_apply, Matrix.of_apply, Prod.mk.injEq, and_true]
  exact hpq''')
thm('a35_shared_gram_realizable', HYP0 + ' ∀ H : ' + M16 + ', H ∈ Matrix.unitaryGroup (Fin 4 × Fin 4) ℂ → (∀ i j, ‖H i j‖ = 1 / 4) → ' + RG16 + ' (' + GRAM('H') + ')', '''  intro Γ₀ hΓ₀ H hH hn
  have hsum1 : ∀ f : Fin 1 × Fin 1 → ℝ, ∑ a, f a = f ((0 : Fin 1), (0 : Fin 1)) := by
    intro f
    rw [Fintype.sum_prod_type, Fin.sum_univ_one, Fin.sum_univ_one]
  have hU : AdmissibleDilationAt (''' + GAM + ''') ((0 : Fin 1), (0 : Fin 1)) (Matrix.of fun p q : (Fin 4 × Fin 4) × (Fin 1 × Fin 1) => H p.1 q.1) := by
    refine ⟨a35_shared_pad_unitary H hH, ?_⟩
    intro i j
    rw [hsum1, hΓ₀]
    simp only [Matrix.of_apply, hn]
    norm_num
  have hG : FibreGram ((0 : Fin 1), (0 : Fin 1)) (Matrix.of fun p q : (Fin 4 × Fin 4) × (Fin 1 × Fin 1) => H p.1 q.1) = ''' + GRAM('H') + ''' := by
    funext i
    ext j k
    rw [fibreGram_apply, Fintype.sum_prod_type, Fin.sum_univ_one, Fin.sum_univ_one]
    simp only [Matrix.of_apply]
  rw [← hG]
  exact sh1_necessity hU''')
thm('a35_shared_hull_core', HYP0 + ' ∀ (X : ' + M4 + ') (Y : Fin 4 → ' + M4 + ') (D : Fin 4 → Fin 4 → ℂ), ' + FL('X') + ' → (∀ c, ' + FL('(Y c)') + ') → (∀ c b, ‖D c b‖ = 1) → (' + DITA() + ') ∈ Matrix.unitaryGroup (Fin 4 × Fin 4) ℂ ∧ (∀ i j, ‖(' + DITA() + ') i j‖ = 1 / 4) ∧ ' + RG16 + ' (' + GRAM(DITA()) + ')', '''  intro Γ₀ hΓ₀ X Y D hX hY hD
  have hu := a35_shared_dita_unitary X Y D hX.1 (fun c => (hY c).1) hD
  have hn := a35_shared_dita_norm X Y D hX.2 (fun c => (hY c).2) hD
  exact ⟨hu, hn, a35_shared_gram_realizable Γ₀ hΓ₀ _ hu hn⟩''')
thm('a35_shared_ditaT_eq', '∀ (X : ' + M4 + ') (Y : Fin 4 → ' + M4 + ') (E : Fin 4 → Fin 4 → ℂ), (' + DITAT() + ') = (' + DITA('Xᵀ', '(fun a => (Y a)ᵀ)', 'E') + ')ᵀ', '''  intro X Y E
  ext i j
  simp only [Matrix.transpose_apply, Matrix.of_apply]''')
thm('a35_shared_hull_t_core', HYP0 + ' ∀ (X : ' + M4 + ') (Y : Fin 4 → ' + M4 + ') (E : Fin 4 → Fin 4 → ℂ), ' + FL('X') + ' → (∀ a, ' + FL('(Y a)') + ') → (∀ a d, ‖E a d‖ = 1) → (' + DITAT() + ') ∈ Matrix.unitaryGroup (Fin 4 × Fin 4) ℂ ∧ (∀ i j, ‖(' + DITAT() + ') i j‖ = 1 / 4) ∧ ' + RG16 + ' (' + GRAM(DITAT()) + ')', '''  intro Γ₀ hΓ₀ X Y E hX hY hE
  have hXt : Xᵀ ∈ Matrix.unitaryGroup (Fin 4) ℂ := transpose_unitary hX.1
  have hYt : ∀ a, (Y a)ᵀ ∈ Matrix.unitaryGroup (Fin 4) ℂ := fun a => transpose_unitary (hY a).1
  have hu : (''' + DITAT() + ''') ∈ Matrix.unitaryGroup (Fin 4 × Fin 4) ℂ := by
    rw [a35_shared_ditaT_eq]
    exact transpose_unitary (a35_shared_dita_unitary Xᵀ (fun a => (Y a)ᵀ) E hXt hYt hE)
  have hn : ∀ i j, ‖(''' + DITAT() + ''') i j‖ = 1 / 4 := by
    intro i j
    show ‖X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2‖ = 1 / 4
    rw [norm_mul, norm_mul, hX.2, hE, (hY _).2]
    norm_num
  exact ⟨hu, hn, a35_shared_gram_realizable Γ₀ hΓ₀ _ hu hn⟩''')

# ---------------------------------------------------------------- Σ ⊆ hulls
thm('a35_shared_vpart_flat', HYP0 + ' ∀ U : Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ, AdmissibleDilationAt Γ₀ (0 : Fin 1) U → ' + FL('(Matrix.of fun a c : Fin 4 => U (a, 0) (c, 0))'), '''  intro Γ₀ hΓ₀ U hU
  refine ⟨vpart_unitary hU.1, ?_⟩
  intro a c
  have h1 := hU.2 a c
  rw [Fin.sum_univ_one, hΓ₀] at h1
  simp only [Matrix.of_apply] at h1 ⊢
  have h0 : 0 ≤ ‖U (a, 0) (c, 0)‖ := norm_nonneg _
  have h2 : (‖U (a, 0) (c, 0)‖ - 1 / 2) * (‖U (a, 0) (c, 0)‖ + 1 / 2) = 0 := by ring_nf; linarith
  rcases mul_eq_zero.1 h2 with h3 | h3
  · linarith
  · linarith''')
thm('a35_shared_gram_of_dilation', HYP0 + ' ∀ (U : Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ) (X : ' + TUP + '), FibreGram (0 : Fin 1) U = X → ∀ a j k : Fin 4, X a j k = star (U (a, 0) (j, 0)) * U (a, 0) (k, 0)', '''  intro Γ₀ hΓ₀ U X hX a j k
  rw [← hX, fibreGram_apply, Fin.sum_univ_one]''')
thm('a35_shared_sigma_core', HYP0 + ' ({x : ' + E16 + ' | ∃ X Y : ' + TUP + ', ' + RG + ' X ∧ ' + RG + ' Y ∧ featureVec (' + PROD + ') = x} ⊆ {x : ' + E16 + ' | ∃ (X : ' + M4 + ') (Y : Fin 4 → ' + M4 + ') (D : Fin 4 → Fin 4 → ℂ), ' + FL('X') + ' ∧ (∀ c, ' + FL('(Y c)') + ') ∧ (∀ c b, ‖D c b‖ = 1) ∧ featureVec (' + GRAM(DITA()) + ') = x}) ∧ ({x : ' + E16 + ' | ∃ X Y : ' + TUP + ', ' + RG + ' X ∧ ' + RG + ' Y ∧ featureVec (' + PROD + ') = x} ⊆ {x : ' + E16 + ' | ∃ (X : ' + M4 + ') (Y : Fin 4 → ' + M4 + ') (E : Fin 4 → Fin 4 → ℂ), ' + FL('X') + ' ∧ (∀ a, ' + FL('(Y a)') + ') ∧ (∀ a d, ‖E a d‖ = 1) ∧ featureVec (' + GRAM(DITAT()) + ') = x})', '''  intro Γ₀ hΓ₀
  constructor
  · intro x hx
    obtain ⟨X, Y, hX, hY, rfl⟩ := hx
    obtain ⟨UX, hUX, hFX⟩ := sh1_sufficiency (0 : Fin 1) hX
    obtain ⟨UY, hUY, hFY⟩ := sh1_sufficiency (0 : Fin 1) hY
    refine ⟨Matrix.of fun a c : Fin 4 => UX (a, 0) (c, 0), fun _ => Matrix.of fun a c : Fin 4 => UY (a, 0) (c, 0), fun _ _ => 1, a35_shared_vpart_flat Γ₀ hΓ₀ UX hUX, fun _ => a35_shared_vpart_flat Γ₀ hΓ₀ UY hUY, fun _ _ => by simp, ?_⟩
    congr 1
    funext i
    ext j k
    simp only [Matrix.of_apply]
    rw [a35_shared_gram_of_dilation Γ₀ hΓ₀ UX X hFX i.1 j.1 k.1, a35_shared_gram_of_dilation Γ₀ hΓ₀ UY Y hFY i.2 j.2 k.2]
    simp only [star_mul, mul_one]
    ring
  · intro x hx
    obtain ⟨X, Y, hX, hY, rfl⟩ := hx
    obtain ⟨UX, hUX, hFX⟩ := sh1_sufficiency (0 : Fin 1) hX
    obtain ⟨UY, hUY, hFY⟩ := sh1_sufficiency (0 : Fin 1) hY
    refine ⟨Matrix.of fun a c : Fin 4 => UX (a, 0) (c, 0), fun _ => Matrix.of fun a c : Fin 4 => UY (a, 0) (c, 0), fun _ _ => 1, a35_shared_vpart_flat Γ₀ hΓ₀ UX hUX, fun _ => a35_shared_vpart_flat Γ₀ hΓ₀ UY hUY, fun _ _ => by simp, ?_⟩
    congr 1
    funext i
    ext j k
    simp only [Matrix.of_apply]
    rw [a35_shared_gram_of_dilation Γ₀ hΓ₀ UX X hFX i.1 j.1 k.1, a35_shared_gram_of_dilation Γ₀ hΓ₀ UY Y hFY i.2 j.2 k.2]
    simp only [star_mul, mul_one]
    ring''')

# ---------------------------------------------------------------- the cross-ratio identity
thm('a35_shared_cross_core', HYP0 + ' ∀ X Y : ' + TUP + ', ' + RG + ' X → ' + RG + ' Y → ∀ a b b\' c c\' d : Fin 4, (' + PROD + ') (a, b) (c, d) (c\', d) * (' + PROD + ') (a, b\') (c\', d) (c, d) = 1 / 256', '''  intro Γ₀ hΓ₀ X Y hX hY a b b' c c' d
  simp only [Matrix.of_apply]
  have hYd : ∀ b, Y b d d = ((1 / 4 : ℝ) : ℂ) := fun b => by rw [hY.2.2.2 b d, hΓ₀]; simp
  have hXh : X a c' c = star (X a c c') := ((a34_shared_hermitian Γ₀ hΓ₀ X hX a).apply c' c).symm
  have h := a35_shared_star_mul (X a c c')
  rw [a34_shared_entry_norm Γ₀ hΓ₀ X hX a c c'] at h
  rw [hYd, hYd, hXh]
  push_cast at h ⊢
  linear_combination (1 / 16 : ℂ) * h''')
thm('a35_shared_diag_core', HYP0 + ' ∀ X Y : ' + TUP + ', ' + RG + ' X → ' + RG + ' Y → ∀ a b c d : Fin 4, (' + PROD + ') (a, b) (c, d) (c, d) = 1 / 16', '''  intro Γ₀ hΓ₀ X Y hX hY a b c d
  simp only [Matrix.of_apply]
  rw [hX.2.2.2 a c, hY.2.2.2 b d, hΓ₀]
  simp
  norm_num''')

# ---------------------------------------------------------------- the witness (act 34's) as a hull point and a relabelled stratum point
thm('a35_shared_wit_eq', '(' + H34 + ') = ' + DITA(F4('Complex.I'), YTW, '(fun _ _ : Fin 4 => (1 : ℂ))'), '''  ext i j
  simp only [Matrix.of_apply]
  ring''')
thm('a35_shared_untw_eq', '(' + H34U + ') = ' + KU, '''  ext i j
  simp only [Matrix.of_apply]
  ring''')
thm('a35_shared_wit_rel', '∀ i j : Fin 4 × Fin 4, (' + H34 + ') i j = (' + KU + ') i ((' + RHO + ') j)', '''  intro i j
  obtain ⟨a, b⟩ := i
  obtain ⟨c, d⟩ := j
  simp only [Matrix.of_apply, Equiv.trans_apply, Equiv.swap_apply_def]
  fin_cases c <;> fin_cases b <;> fin_cases d <;> simp <;> ring''')
WIT_BODY = ('((' + H34 + ') = ' + DITA(F4('Complex.I'), YTW, '(fun _ _ : Fin 4 => (1 : ℂ))') + ')\n'
            '  ∧ featureVec (' + GRAM(H34) + ') ∈ {x : ' + E16 + ' | ∃ (X : ' + M4 + ') (Y : Fin 4 → ' + M4 + ') (D : Fin 4 → Fin 4 → ℂ), ' + FL('X') + ' ∧ (∀ c, ' + FL('(Y c)') + ') ∧ (∀ c b, ‖D c b‖ = 1) ∧ featureVec (' + GRAM(DITA()) + ') = x}'
            ' ∧ featureVec (' + GRAM(H34) + ') ∉ {x : ' + E16 + ' | ∃ X Y : ' + TUP + ', ' + RG + ' X ∧ ' + RG + ' Y ∧ featureVec (' + PROD + ') = x}\n'
            '  ∧ (' + GRAM(H34) + ') (0, 1) (0, 1) (1, 1) * (' + GRAM(H34) + ') (0, 0) (1, 1) (0, 1) = -(1 / 256)\n'
            '  ∧ (∀ i j, (' + H34 + ') i j = (' + KU + ') i ((' + RHO + ') j))\n'
            '  ∧ featureVec (' + GRAM(H34) + ') = featureVec (fun i => ((' + GRAM(KU) + ') i).submatrix (' + RHO + ') (' + RHO + '))')
HULLSET = '{x : ' + E16 + ' | ∃ (X : ' + M4 + ') (Y : Fin 4 → ' + M4 + ') (D : Fin 4 → Fin 4 → ℂ), ' + FL('X') + ' ∧ (∀ c, ' + FL('(Y c)') + ') ∧ (∀ c b, ‖D c b‖ = 1) ∧ featureVec (' + GRAM(DITA()) + ') = x}'
SSET = '{x : ' + E16 + ' | ∃ X Y : ' + TUP + ', ' + RG + ' X ∧ ' + RG + ' Y ∧ featureVec (' + PROD + ') = x}'
thm('a35_shared_wit_mem', HYP0 + ' featureVec (' + GRAM(H34) + ') ∈ ' + HULLSET, '''  intro Γ₀ hΓ₀
  have hI : star Complex.I * Complex.I = 1 := by simp
  refine ⟨''' + F4('Complex.I') + ''', ''' + YTW + ''', fun _ _ => 1, a35_shared_f4_flat Γ₀ hΓ₀ Complex.I hI, ?_, fun _ _ => by simp, ?_⟩
  · intro c
    show ''' + FL(F4('(if c.val % 2 = 0 then Complex.I else -Complex.I)')) + '''
    exact a35_shared_f4_flat Γ₀ hΓ₀ _ (by split_ifs <;> simp)
  · rw [a35_shared_wit_eq]''')
thm('a35_shared_wit_notin', HYP0 + ' featureVec (' + GRAM(H34) + ') ∉ ' + SSET, '''  intro Γ₀ hΓ₀ hS
  have h34 := a34_control_proper Γ₀ hΓ₀
  dsimp only at h34
  obtain ⟨X, Y, hX, hY, hxy⟩ := hS
  exact h34.2 X Y hxy''')
thm('a35_shared_wit_val', '(' + GRAM(H34) + ') (0, 1) (0, 1) (1, 1) * (' + GRAM(H34) + ') (0, 0) (1, 1) (0, 1) = -(1 / 256)', '  ' + SIMPEV + ' <;> norm_num')
thm('a35_shared_wit_feat', 'featureVec (' + GRAM(H34) + ') = featureVec (fun i => ((' + GRAM(KU) + ') i).submatrix (' + RHO + ') (' + RHO + '))', '  congr 1\n  funext i\n  ext j k\n  show star ((' + H34 + ') i j) * (' + H34 + ') i k = star ((' + KU + ') i ((' + RHO + ') j)) * (' + KU + ') i ((' + RHO + ') k)\n  rw [a35_shared_wit_rel i j, a35_shared_wit_rel i k]')
thm('a35_shared_wit_core', HYP0 + '\n  ' + WIT_BODY, '''  intro Γ₀ hΓ₀
  exact ⟨a35_shared_wit_eq, a35_shared_wit_mem Γ₀ hΓ₀, a35_shared_wit_notin Γ₀ hΓ₀, a35_shared_wit_val, a35_shared_wit_rel, a35_shared_wit_feat⟩''')

# ---------------------------------------------------------------- off-stratum by a coordinate
def notin_core(name, HTXT, ia, ib, ibp, jc, jcp, jd, rhs_hint):
    """featureVec (GRAM HTXT) ∉ S, through the coordinate ((a,b),(a,b'),(a,b')), ((c,d),(c',d),(c,d))."""
    p0 = '((((%s : Fin 4), (%s : Fin 4)), ((%s : Fin 4), (%s : Fin 4)), ((%s : Fin 4), (%s : Fin 4))), (((%s : Fin 4), (%s : Fin 4)), ((%s : Fin 4), (%s : Fin 4)), ((%s : Fin 4), (%s : Fin 4))))' % (ia, ib, ia, ibp, ia, ibp, jc, jd, jcp, jd, jc, jd)
    proof = ('  intro Γ₀ hΓ₀ hS\n'
             '  obtain ⟨X, Y, hX, hY, hxy⟩ := hS\n'
             '  have hq := (a34_shared_feature_ext _ _).1 hxy ' + p0 + '\n'
             '  have hc := a35_shared_cross_core Γ₀ hΓ₀ X Y hX hY %d %d %d %d %d %d\n' % (ia, ib, ibp, jc, jcp, jd) +
             '  have hd := a35_shared_diag_core Γ₀ hΓ₀ X Y hX hY %d %d %d %d\n' % (ia, ibp, jc, jd) +
             '  have hL : mixedTriple (' + PROD + ') ' + p0 + ' = 1 / 4096 := by\n'
             '    simp only [mixedTriple, Matrix.of_apply] at hc hd ⊢\n'
             '    rw [hc, hd]\n'
             '    norm_num\n'
             '  rw [hL] at hq\n'
             '  ' + SIMPEV + ' at hq <;> norm_num at hq')
    thm(name, HYP0 + ' featureVec (' + GRAM(HTXT) + ') ∉ {x : ' + E16 + ' | ∃ X Y : ' + TUP + ', ' + RG + ' X ∧ ' + RG + ' Y ∧ featureVec (' + PROD + ') = x}', proof)
notin_core('a35_shared_twist_notin', HW, 0, 0, 1, 0, 1, 0, '-I/4096')
notin_core('a35_shared_real_notin', HR, 0, 0, 3, 0, 3, 0, '-1/4096')

# ---------------------------------------------------------------- TWIST, REAL2, UNTW cores
thm('a35_shared_twist_core', HYP0 + '\n  featureVec (' + GRAM(HW) + ') ∈ {x : ' + E16 + ' | ∃ (X : ' + M4 + ') (Y : Fin 4 → ' + M4 + ') (D : Fin 4 → Fin 4 → ℂ), ' + FL('X') + ' ∧ (∀ c, ' + FL('(Y c)') + ') ∧ (∀ c b, ‖D c b‖ = 1) ∧ featureVec (' + GRAM(DITA()) + ') = x} ∧ featureVec (' + GRAM(HW) + ') ∉ {x : ' + E16 + ' | ∃ X Y : ' + TUP + ', ' + RG + ' X ∧ ' + RG + ' Y ∧ featureVec (' + PROD + ') = x}\n  ∧ ∑ k : Fin 4 × Fin 4, (' + HW + ') (0, 0) k * star ((' + HW + ') (0, 1) k) * (' + HW + ') (0, 2) k * star ((' + HW + ') (1, 1) k) = Complex.I / 32', '''  intro Γ₀ hΓ₀
  have hI : star Complex.I * Complex.I = 1 := by simp
  refine ⟨⟨''' + F4('Complex.I') + ''', fun _ => ''' + F4('Complex.I') + ''', ''' + DW + ''', a35_shared_f4_flat Γ₀ hΓ₀ Complex.I hI, fun _ => a35_shared_f4_flat Γ₀ hΓ₀ Complex.I hI, ?_, rfl⟩, a35_shared_twist_notin Γ₀ hΓ₀, ?_⟩
  · intro c b
    by_cases hc : c = 1
    · simp only [hc, if_true]
      fin_cases b <;> simp
    · simp [hc]
  · ''' + SIMPEV + '''
    norm_num''')
thm('a35_shared_real_im', '∀ i j : Fin 4 × Fin 4, ((' + HR + ') i j).im = 0', '''  intro i j
  have hM : ∀ a c : Fin 4, ((1 / 2 : ℂ) * (!![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, 1, -1; 1, -1, -1, 1] : Matrix (Fin 4) (Fin 4) ℂ) a c).im = 0 := by
    intro a c
    fin_cases a <;> fin_cases c <;> simp
  have h2 : ∀ c b : Fin 4, (if c = 3 ∧ b = 3 then (-1 : ℂ) else 1).im = 0 := by
    intro c b
    split_ifs <;> simp
  have key : ∀ x y w : ℂ, x.im = 0 → y.im = 0 → w.im = 0 → (x * y * w).im = 0 := by
    intro x y w hx hy hw
    simp [Complex.mul_im, hx, hy, hw]
  exact key _ _ _ (hM i.1 j.1) (h2 j.1 i.2) (hM i.2 j.2)''')
thm('a35_shared_real_core', HYP0 + '\n  (∀ i j, ((' + HR + ') i j).im = 0) ∧ featureVec (' + GRAM(HR) + ') ∈ {x : ' + E16 + ' | ∃ (X : ' + M4 + ') (Y : Fin 4 → ' + M4 + ') (D : Fin 4 → Fin 4 → ℂ), ' + FL('X') + ' ∧ (∀ c, ' + FL('(Y c)') + ') ∧ (∀ c b, ‖D c b‖ = 1) ∧ featureVec (' + GRAM(DITA()) + ') = x} ∧ featureVec (' + GRAM(HR) + ') ∉ {x : ' + E16 + ' | ∃ X Y : ' + TUP + ', ' + RG + ' X ∧ ' + RG + ' Y ∧ featureVec (' + PROD + ') = x}\n  ∧ ∑ k : Fin 4 × Fin 4, (' + HR + ') (0, 0) k * (' + HR + ') (0, 1) k * (' + HR + ') (0, 2) k * (' + HR + ') (0, 3) k = 1 / 32', '''  intro Γ₀ hΓ₀
  have h1 : star (1 : ℂ) * 1 = 1 := by simp
  refine ⟨a35_shared_real_im, ⟨''' + F4('1') + ''', fun _ => ''' + F4('1') + ''', ''' + DR + ''', a35_shared_f4_flat Γ₀ hΓ₀ 1 h1, fun _ => a35_shared_f4_flat Γ₀ hΓ₀ 1 h1, ?_, rfl⟩, a35_shared_real_notin Γ₀ hΓ₀, ?_⟩
  · intro c b
    dsimp only
    split_ifs <;> simp
  · ''' + SIMPEV + '''
    norm_num''')
thm('a35_shared_untw_core', HYP0 + ' featureVec (' + GRAM(KU) + ') ∈ {x : ' + E16 + ' | ∃ X Y : ' + TUP + ', ' + RG + ' X ∧ ' + RG + ' Y ∧ featureVec (' + PROD + ') = x}', '''  intro Γ₀ hΓ₀
  have h := a34_control_product Γ₀ hΓ₀
  dsimp only at h
  obtain ⟨X, Y, hX, hY, hxy⟩ := h
  refine ⟨X, Y, hX, hY, ?_⟩
  rw [← a35_shared_untw_eq]
  exact hxy''')

# ---------------------------------------------------------------- RELAB core
PSIG = '(fun i => ((' + PRODXY(TUP0, TUP0) + ') ((' + SIG + ') i)).submatrix (' + SIG + ') (' + SIG + '))'
thm('a35_shared_relab_core', HYP0 + '\n  ' + RG16 + ' ' + PSIG + '\n  ∧ (∀ G G\' : ' + TUP16 + ', dist (featureVec (fun i => (G ((' + SIG + ') i)).submatrix (' + SIG + ') (' + SIG + '))) (featureVec (fun i => (G\' ((' + SIG + ') i)).submatrix (' + SIG + ') (' + SIG + '))) = dist (featureVec G) (featureVec G\'))\n  ∧ featureVec (' + PRODXY(TUP0, TUP0) + ') ∈ {x : ' + E16 + ' | ∃ X Y : ' + TUP + ', ' + RG + ' X ∧ ' + RG + ' Y ∧ featureVec (' + PROD + ') = x} ∧ featureVec ' + PSIG + ' ∉ {x : ' + E16 + ' | ∃ X Y : ' + TUP + ', ' + RG + ' X ∧ ' + RG + ' Y ∧ featureVec (' + PROD + ') = x}\n  ∧ ' + PSIG + ' (0, 0) (0, 2) (1, 2) * ' + PSIG + ' (0, 1) (1, 2) (0, 2) = -(Complex.I / 256)', '''  intro Γ₀ hΓ₀
  have hI : star Complex.I * Complex.I = 1 := by simp
  have hT := a34_shared_tup_real Γ₀ hΓ₀ 0 Complex.I hI
  have hP : ''' + RG16 + ''' (''' + PRODXY(TUP0, TUP0) + ''') := by
    obtain ⟨U1, hU1, hF1⟩ := sh1_sufficiency (0 : Fin 1) hT
    obtain ⟨U, hU, hFU⟩ := product_realizable hU1 hU1
    have := sh1_necessity hU
    rw [hFU, hF1] at this
    exact this
  refine ⟨?_, ?_, ⟨_, _, hT, hT, rfl⟩, ?_, ?_⟩
  · exact relabel2_realizable (A := Fin 1 × Fin 1) _ (fun i j i' j' => by rw [hΓ₀]; simp) _ _ _ hP
  · intro G G'
    let d : (Fin 4 × Fin 4 → ''' + M16 + ''') → (Fin 4 × Fin 4 → ''' + M16 + ''') → ℝ := fun G H => Real.sqrt (∑ p, ‖mixedTriple G p - mixedTriple H p‖ ^ 2)
    have h1 := dist_featureVec d rfl (fun i => (G ((''' + SIG + ''') i)).submatrix (''' + SIG + ''') (''' + SIG + ''')) (fun i => (G' ((''' + SIG + ''') i)).submatrix (''' + SIG + ''') (''' + SIG + '''))
    have h2 := dist_featureVec d rfl G G'
    rw [← h1, ← h2]
    exact relabel2_isometry d rfl _ _ G G'
  · intro hS
    obtain ⟨X, Y, hX, hY, hxy⟩ := hS
    have hq := (a34_shared_feature_ext _ _).1 hxy ((((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (1 : Fin 4))), (((0 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (2 : Fin 4))))
    have hc := a35_shared_cross_core Γ₀ hΓ₀ X Y hX hY 0 0 1 0 1 2
    have hd := a35_shared_diag_core Γ₀ hΓ₀ X Y hX hY 0 1 0 2
    have hL : mixedTriple (''' + PROD + ''') ((((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (1 : Fin 4))), (((0 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)))) = 1 / 4096 := by
      simp only [mixedTriple, Matrix.of_apply] at hc hd ⊢
      rw [hc, hd]
      norm_num
    rw [hL] at hq
    ''' + SIMPEV + ''' at hq <;> norm_num at hq
  · ''' + SIMPEV + '''
    norm_num''')

# ---------------------------------------------------------------- EXT core
thm('a35_shared_perm_unitary', '∀ (A : ' + M4 + ') (e f : Equiv.Perm (Fin 4)), A ∈ Matrix.unitaryGroup (Fin 4) ℂ → A.submatrix e f ∈ Matrix.unitaryGroup (Fin 4) ℂ', '''  intro A e f hA
  rw [Matrix.mem_unitaryGroup_iff] at hA ⊢
  ext i j
  have h := congrFun (congrFun hA (e i)) (e j)
  rw [Matrix.mul_apply, Matrix.one_apply] at h ⊢
  simp only [Matrix.star_apply, Matrix.submatrix_apply] at h ⊢
  rw [Equiv.sum_comp f (fun k => A (e i) k * star (A (e j) k)), h]
  simp [e.injective.eq_iff]''')
thm('a35_shared_conj_unitary', '∀ A : ' + M4 + ', A ∈ Matrix.unitaryGroup (Fin 4) ℂ → (Matrix.of fun a c : Fin 4 => star (A a c)) ∈ Matrix.unitaryGroup (Fin 4) ℂ', '''  intro A hA
  rw [Matrix.mem_unitaryGroup_iff] at hA ⊢
  ext i j
  have h := congrFun (congrFun hA j) i
  rw [Matrix.mul_apply, Matrix.one_apply] at h ⊢
  simp only [Matrix.star_apply, Matrix.of_apply, star_star] at h ⊢
  rw [Finset.sum_congr rfl (fun k _ => mul_comm (star (A i k)) (A j k)), h]
  by_cases hij : i = j
  · subst hij
    simp
  · simp [hij, Ne.symm hij]''')
DC = 'fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => star (star ((' + DITA() + ') i j) * (' + DITA() + ') i k)'
thm('a35_shared_ext_core', HYP0 + ' ∀ (π₁ π₂ τ₁ τ₂ : Equiv.Perm (Fin 4)) (X : ' + M4 + ') (Y : Fin 4 → ' + M4 + ') (D : Fin 4 → Fin 4 → ℂ), ' + FL('X') + ' → (∀ c, ' + FL('(Y c)') + ') → (∀ c b, ‖D c b‖ = 1) →\n'
    '    featureVec (fun i => ((' + GRAM(DITA()) + ') ((π₁.prodCongr π₂) i)).submatrix (τ₁.prodCongr τ₂) (τ₁.prodCongr τ₂)) ∈ {x : ' + E16 + ' | ∃ (X : ' + M4 + ') (Y : Fin 4 → ' + M4 + ') (D : Fin 4 → Fin 4 → ℂ), ' + FL('X') + ' ∧ (∀ c, ' + FL('(Y c)') + ') ∧ (∀ c b, ‖D c b‖ = 1) ∧ featureVec (' + GRAM(DITA()) + ') = x}\n'
    '    ∧ featureVec (fun i => Matrix.of fun j k => star ((' + GRAM(DITA()) + ') i j k)) ∈ {x : ' + E16 + ' | ∃ (X : ' + M4 + ') (Y : Fin 4 → ' + M4 + ') (D : Fin 4 → Fin 4 → ℂ), ' + FL('X') + ' ∧ (∀ c, ' + FL('(Y c)') + ') ∧ (∀ c b, ‖D c b‖ = 1) ∧ featureVec (' + GRAM(DITA()) + ') = x}\n'
    '    ∧ featureVec (' + GRAM('(' + DITA() + ')ᵀ') + ') ∈ {x : ' + E16 + ' | ∃ (X : ' + M4 + ') (Y : Fin 4 → ' + M4 + ') (E : Fin 4 → Fin 4 → ℂ), ' + FL('X') + ' ∧ (∀ a, ' + FL('(Y a)') + ') ∧ (∀ a d, ‖E a d‖ = 1) ∧ featureVec (' + GRAM(DITAT()) + ') = x}', '''  intro Γ₀ hΓ₀ π₁ π₂ τ₁ τ₂ X Y D hX hY hD
  refine ⟨?_, ?_, ?_⟩
  · refine ⟨X.submatrix π₁ τ₁, fun c => (Y (τ₁ c)).submatrix π₂ τ₂, fun c b => D (τ₁ c) (π₂ b), ⟨a35_shared_perm_unitary X π₁ τ₁ hX.1, fun a c => by simp only [Matrix.submatrix_apply]; exact hX.2 _ _⟩, fun c => ⟨a35_shared_perm_unitary _ π₂ τ₂ (hY _).1, fun a d => by simp only [Matrix.submatrix_apply]; exact (hY _).2 _ _⟩, fun c b => hD _ _, ?_⟩
    congr 1
  · refine ⟨Matrix.of fun a c : Fin 4 => star (X a c), fun c => Matrix.of fun a d : Fin 4 => star (Y c a d), fun c b => star (D c b), ⟨a35_shared_conj_unitary X hX.1, fun a c => by simp only [Matrix.of_apply, norm_star]; exact hX.2 a c⟩, fun c => ⟨a35_shared_conj_unitary _ (hY c).1, fun a d => by simp only [Matrix.of_apply, norm_star]; exact (hY c).2 a d⟩, fun c b => by rw [norm_star]; exact hD c b, ?_⟩
    congr 1
    funext i
    ext j k
    simp only [Matrix.of_apply, star_mul, star_star]
    ring
  · refine ⟨Xᵀ, fun a => (Y a)ᵀ, D, ⟨transpose_unitary hX.1, fun a c => by simp only [Matrix.transpose_apply]; exact hX.2 c a⟩, fun a => ⟨transpose_unitary (hY a).1, fun b d => by simp only [Matrix.transpose_apply]; exact (hY a).2 d b⟩, hD, ?_⟩
    congr 1''')

# ---------------------------------------------------------------- MOD core
thm('a35_shared_unit_solve', '∀ p q r s p\' q\' r\' s\' : ℂ, star p * p = 1 → star q * q = 1 → star r * r = 1 → star s * s = 1 → star p\' * p\' = 1 → star q\' * q\' = 1 → star r\' * r\' = 1 → star s\' * s\' = 1 →\n    star p * q * star r * s * star s * s = star p\' * q\' * star r\' * s\' * star s\' * s\' → p\' = (s\' * star s) * (q\' * star q * r * star r\') * p', '''  intro p q r s p' q' r' s' hp hq hr hs hp' hq' hr' hs' h
  have h1 : star p * q * star r * s = star p' * q' * star r' * s' := by
    linear_combination h - (star p * q * star r * s) * hs + (star p' * q' * star r' * s') * hs'
  linear_combination (p' * p * r * star q * star s) * h1 - p' * (q * star q * (star r * r) * (s * star s)) * hp - p' * (star r * r * (s * star s)) * hq - p' * (s * star s) * hr - p' * hs + (s' * star s * (q' * star q * r * star r') * p) * hp\'''')
thm('a35_shared_mod_core', HYP0 + ' ∀ (X Y : ' + M4 + ') (D D\' : Fin 4 → Fin 4 → ℂ), ' + FL('X') + ' → ' + FL('Y') + ' → (∀ c b, ‖D c b‖ = 1) → (∀ c b, ‖D\' c b‖ = 1) →\n    featureVec (' + GRAM(DITA('X', '(fun _ => Y)', 'D')) + ') = featureVec (' + GRAM(DITA('X', '(fun _ => Y)', "D'")) + ') →\n    ∃ u v : Fin 4 → ℂ, ∀ c b, D\' c b = u c * v b * D c b', '''  intro Γ₀ hΓ₀ X Y D D' hX hY hD hD' hfeat
  refine ⟨fun c => D' c 0 * star (D c 0), fun b => D' 0 b * star (D 0 b) * D 0 0 * star (D' 0 0), fun c b => ?_⟩
  have hq := (a34_shared_feature_ext _ _).1 hfeat ((((0 : Fin 4), b), ((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (0 : Fin 4))), ((c, (0 : Fin 4)), ((0 : Fin 4), (0 : Fin 4)), (c, (0 : Fin 4))))
  simp only [mixedTriple, Matrix.of_apply, star_mul] at hq
  have hXne : ∀ a c : Fin 4, X a c ≠ 0 := fun a c => a35_shared_ne_zero _ _ (by norm_num) (hX.2 a c)
  have hYne : ∀ a c : Fin 4, Y a c ≠ 0 := fun a c => a35_shared_ne_zero _ _ (by norm_num) (hY.2 a c)
  have hK : star (X 0 c) * X 0 0 * star (X 0 0) * X 0 c * star (X 0 c) * X 0 c * star (Y b 0) * Y b 0 * star (Y 0 0) * Y 0 0 * star (Y 0 0) * Y 0 0 ≠ 0 := by
    repeat' apply mul_ne_zero
    all_goals first
      | exact hXne _ _
      | exact hYne _ _
      | (rw [ne_eq, star_eq_zero]; exact hXne _ _)
      | (rw [ne_eq, star_eq_zero]; exact hYne _ _)
  have hf : star (D c b) * D 0 b * star (D 0 0) * D c 0 * star (D c 0) * D c 0 = star (D' c b) * D' 0 b * star (D' 0 0) * D' c 0 * star (D' c 0) * D' c 0 := by
    apply mul_left_cancel₀ hK
    linear_combination hq
  have u := fun c b => a35_shared_unit_of_norm _ (hD c b)
  have u' := fun c b => a35_shared_unit_of_norm _ (hD' c b)
  have := a35_shared_unit_solve (D c b) (D 0 b) (D 0 0) (D c 0) (D' c b) (D' 0 b) (D' 0 0) (D' c 0) (u c b) (u 0 b) (u 0 0) (u c 0) (u' c b) (u' 0 b) (u' 0 0) (u' c 0) hf
  exact this''')

# ---------------------------------------------------------------- INF core
ZN = '(((n : ℂ) + Complex.I) / ((n : ℂ) - Complex.I))'
DN = '(fun c b : Fin 4 => if c = 1 ∧ b = 1 then ' + ZN + ' else (1 : ℂ))'
ZNM = ZN.replace('(n : ℂ)', '(m : ℂ)')
def ITE(c, b, z): return '(if (%s : Fin 4) = 1 ∧ (%s : Fin 4) = 1 then %s else (1 : ℂ))' % (c, b, z)
thm('a35_shared_zn', '∀ n : ℕ, ‖' + ZN + '‖ = 1 ∧ ((n : ℂ) - Complex.I) ≠ 0', '''  intro n
  have hne : ((n : ℂ) - Complex.I) ≠ 0 := by
    intro h
    have := congrArg Complex.im h
    simp at this
  have hne2 : ((n : ℂ) + Complex.I) ≠ 0 := by
    intro h
    have := congrArg Complex.im h
    simp at this
  refine ⟨?_, hne⟩
  have hst : star ((n : ℂ) + Complex.I) = (n : ℂ) - Complex.I := by
    simp [Complex.star_def, Complex.conj_I, sub_eq_add_neg]
  rw [norm_div, ← hst, norm_star, div_self (norm_ne_zero_iff.2 hne2)]''')
thm('a35_shared_zn_inj', '∀ n m : ℕ, ' + ZN + ' = ' + ZN.replace('(n : ℂ)', '(m : ℂ)') + ' → n = m', '''  intro n m h
  have hn := (a35_shared_zn n).2
  have hm := (a35_shared_zn m).2
  rw [div_eq_div_iff hn hm] at h
  have him := congrArg Complex.im h
  simp [Complex.mul_im, Complex.mul_re] at him
  have : (n : ℝ) = m := by linarith
  exact_mod_cast this''')
thm('a35_shared_inf_core', HYP0 + '\n  Set.Infinite ' + FAMX + '\n  ∧ ∀ (G : Finset (' + E16 + ' → ' + E16 + ')) (T : Finset (' + E16 + ')), ∃ D : Fin 4 → Fin 4 → ℂ, (∀ c b, ‖D c b‖ = 1) ∧\n    ∀ g ∈ G, ∀ t ∈ T, g t ≠ featureVec (' + GRAM(DITA(F4('Complex.I'), '(fun _ : Fin 4 => ' + F4('Complex.I') + ')', 'D')) + ')', '''  intro Γ₀ hΓ₀
  have hI : star Complex.I * Complex.I = 1 := by simp
  have hF := a35_shared_f4_flat Γ₀ hΓ₀ Complex.I hI
  have hDn : ∀ n : ℕ, ∀ c b : Fin 4, ‖(''' + DN + ''') c b‖ = 1 := by
    intro n c b
    simp only []
    split_ifs
    · exact (a35_shared_zn n).1
    · simp
  have hinf : Set.Infinite ''' + FAMX + ''' := by
    refine Set.infinite_of_injective_forall_mem (f := fun n : ℕ => featureVec (''' + GRAM(DITA(F4('Complex.I'), '(fun _ : Fin 4 => ' + F4('Complex.I') + ')', DN)) + ''')) ?_ ?_
    · intro n m h
      obtain ⟨u, v, huv⟩ := a35_shared_mod_core Γ₀ hΓ₀ _ _ _ _ hF hF (hDn n) (hDn m) h
      have hx00 : ¬((0 : Fin 4) = 1 ∧ (0 : Fin 4) = 1) := by decide
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
      linear_combination -h11 + ''' + ZN + ''' * h10 + ''' + ZN + ''' * u 1 * v 0 * h01 - ''' + ZN + ''' * u 1 * v 1 * h00
    · intro n
      exact ⟨_, hDn n, rfl⟩
  refine ⟨hinf, ?_⟩
  intro G T
  by_contra hcon
  push_neg at hcon
  apply hinf
  have hK : (⋃ g ∈ G, ⋃ t ∈ T, ({g t} : Set (''' + E16 + '''))).Finite :=
    Set.Finite.biUnion (Finset.finite_toSet G) (fun g _ => Set.Finite.biUnion (Finset.finite_toSet T) (fun t _ => Set.finite_singleton _))
  refine hK.subset ?_
  rintro x ⟨D, hD, rfl⟩
  obtain ⟨g, hg, t, ht, hgt⟩ := hcon D hD
  simp only [Set.mem_iUnion, Set.mem_singleton_iff]
  exact ⟨g, hg, t, ht, hgt.symm⟩''')

# ---------------------------------------------------------------- frozen theorems
def frozen(name, key, proof):
    thm(name, PR[key], proof)
frozen('a35_shared_hull', 'HULL', '  intro Γ₀ hΓ₀\n  dsimp only\n  exact a35_shared_hull_core Γ₀ hΓ₀')
frozen('a35_shared_hull_t', 'HULLT', '  intro Γ₀ hΓ₀\n  dsimp only\n  exact a35_shared_hull_t_core Γ₀ hΓ₀')
frozen('a35_shared_hull_sub', 'SUB', '''  intro Γ₀ hΓ₀
  dsimp only
  constructor
  · intro x hx
    obtain ⟨X, Y, D, hX, hY, hD, rfl⟩ := hx
    exact ⟨_, (a35_shared_hull_core Γ₀ hΓ₀ X Y D hX hY hD).2.2, rfl⟩
  · intro x hx
    obtain ⟨X, Y, E, hX, hY, hE, rfl⟩ := hx
    exact ⟨_, (a35_shared_hull_t_core Γ₀ hΓ₀ X Y E hX hY hE).2.2, rfl⟩''')
frozen('a35_shared_sigma_hull', 'SIGMA', '  intro Γ₀ hΓ₀\n  dsimp only\n  exact a35_shared_sigma_core Γ₀ hΓ₀')
frozen('a35_shared_cross', 'CROSS', '  intro Γ₀ hΓ₀\n  dsimp only\n  exact a35_shared_cross_core Γ₀ hΓ₀')
frozen('a35_control_witness', 'WIT', '  intro Γ₀ hΓ₀\n  dsimp only\n  exact a35_shared_wit_core Γ₀ hΓ₀')
frozen('a35_control_twist', 'TWIST', '  intro Γ₀ hΓ₀\n  dsimp only\n  exact a35_shared_twist_core Γ₀ hΓ₀')
frozen('a35_control_real', 'REAL2', '  intro Γ₀ hΓ₀\n  dsimp only\n  exact a35_shared_real_core Γ₀ hΓ₀')
frozen('a35_control_relabel', 'RELAB', '  intro Γ₀ hΓ₀\n  dsimp only\n  exact a35_shared_relab_core Γ₀ hΓ₀')
frozen('a35_shared_extend', 'EXT', '  intro Γ₀ hΓ₀\n  dsimp only\n  exact a35_shared_ext_core Γ₀ hΓ₀')
frozen('a35_shared_modulus', 'MOD', '  intro Γ₀ hΓ₀\n  dsimp only\n  exact a35_shared_mod_core Γ₀ hΓ₀')
frozen('a35_shared_infinite', 'INF', '  intro Γ₀ hΓ₀\n  dsimp only\n  exact a35_shared_inf_core Γ₀ hΓ₀')
frozen('a35_control_untwisted', 'UNTW', '  intro Γ₀ hΓ₀\n  dsimp only\n  exact a35_shared_untw_core Γ₀ hΓ₀')
if '--no-verdict' not in sys.argv:
    frozen('a35_dita_stratified', 'P_R', '''  intro Γ₀ hΓ₀
  dsimp only
  exact ⟨a35_shared_hull_core Γ₀ hΓ₀, a35_shared_hull_t_core Γ₀ hΓ₀, a35_shared_sigma_core Γ₀ hΓ₀, a35_shared_ext_core Γ₀ hΓ₀, a35_shared_mod_core Γ₀ hΓ₀, a35_shared_inf_core Γ₀ hΓ₀⟩''')
    thm('a35_c_exclusive', '(' + PR['P_N'] + ') → ¬ (' + PR['P_R'] + ')', '''  intro hN hR
  have h := hN _ rfl
  have r := hR _ rfl
  dsimp only at h r
  rcases h with h | h | h | h | h | h
  · exact h r.1
  · exact h r.2.1
  · exact h r.2.2.1
  · exact h r.2.2.2.1
  · exact h r.2.2.2.2.1
  · exact h r.2.2.2.2.2''')

parts = [B.IMPORT, '\n', B.DOC, '\nnamespace OIBridge\nnamespace DitaHull\n\n', B.OPEN, '\n'] + L + ['end DitaHull\nend OIBridge\n']
text = ''.join(parts)
open(os.path.join(S, 'mod35.lean'), 'w', encoding='utf-8').write(text)
print('mod35.lean', len(text), 'bytes,', text.count('#print axioms'), 'theorems')
