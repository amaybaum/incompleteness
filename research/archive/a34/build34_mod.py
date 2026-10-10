"""A34 module builder: the dev module (all theorems, incl. verdict + corollary) for claude/a34-dev.
usage: python3 build34_mod.py out.lean"""
import json, os, sys, re
S = os.path.dirname(os.path.abspath(__file__))
P = json.load(open(os.path.join(S, 'props34.json')))
PR = P['PROPS']

E4 = 'EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4))'
I4 = '(Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)'
I16 = '((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4))'
E16 = 'EuclideanSpace ℂ (' + I16 + ')'
TUP = 'Fin 4 → Matrix (Fin 4) (Fin 4) ℂ'
TUP16 = 'Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ'
RG = 'RealizableGram (Fin 1) Γ₀'
RT = '(![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (2 : Fin 4) 3)), ((1 : Equiv.Perm (Fin 4)), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (2 : Fin 4) 3), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2)), ((Equiv.swap (1 : Fin 4) 2), (1 : Equiv.Perm (Fin 4))), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3)), ((Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2))]'
HEADLINE = '∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →'
V1 = '(![0, 2, 4, 2, 0, 3, 4, 5, 0] : Fin 9 → Fin 6)'
V2 = '(![1, 3, 5, 5, 4, 1, 3, 1, 2] : Fin 9 → Fin 6)'
v1 = [0, 2, 4, 2, 0, 3, 4, 5, 0]; v2 = [1, 3, 5, 5, 4, 1, 3, 1, 2]
PERM = [('(1 : Equiv.Perm (Fin 4))', '(1 : Equiv.Perm (Fin 4))'), ('(1 : Equiv.Perm (Fin 4))', '(Equiv.swap (2 : Fin 4) 3)'), ('(1 : Equiv.Perm (Fin 4))', '(Equiv.swap (1 : Fin 4) 2)'),
        ('(Equiv.swap (2 : Fin 4) 3)', '(1 : Equiv.Perm (Fin 4))'), ('(Equiv.swap (2 : Fin 4) 3)', '(Equiv.swap (2 : Fin 4) 3)'), ('(Equiv.swap (2 : Fin 4) 3)', '(Equiv.swap (1 : Fin 4) 2)'),
        ('(Equiv.swap (1 : Fin 4) 2)', '(1 : Equiv.Perm (Fin 4))'), ('(Equiv.swap (1 : Fin 4) 2)', '(Equiv.swap (2 : Fin 4) 3)'), ('(Equiv.swap (1 : Fin 4) 2)', '(Equiv.swap (1 : Fin 4) 2)')]
RS = ', '.join('a33_shared_R1_%d, a33_shared_R2_%d' % (k, k) for k in range(9))
FIN9 = 'rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl'

def adj(r, s): return r != s and (v1[r] in (v1[s], v2[s]) or v2[r] in (v1[s], v2[s]))
def mu(r, s): return 1 if v1[r] in (v1[s], v2[s]) else -1
def MZ(z): return '(Matrix.of (fun p q : Fin 4 × Fin 1 =>\n        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, %s, -1, -(%s); 1, -1, 1, -1; 1, -(%s), -1, %s] p.1 q.1))' % (z, z, z, z)
def RTAPP(r): return RT + ' ' + r + ')'
def TUPC(r, z): return '(fun i => (FibreGram (0 : Fin 1) %s (%s.1 i)).submatrix %s.2 %s.2)' % (MZ(z), RTAPP(r), RTAPP(r), RTAPP(r))
def TUPP(k, z): return '(fun i => (FibreGram (0 : Fin 1) %s (%s i)).submatrix %s %s)' % (MZ(z), PERM[k][0], PERM[k][1], PERM[k][1])
def PRODC(X, Y): return '(fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => %s i.1 j.1 k.1 * %s i.2 j.2 k.2)' % (X, Y)
def FV(t): return 'featureVec ' + t
def ADJC(r, s): return '(%s ≠ %s ∧ (%s %s = %s %s ∨ %s %s = %s %s ∨ %s %s = %s %s ∨ %s %s = %s %s))' % (r, s, V1, r, V1, s, V1, r, V2, s, V2, r, V1, s, V2, r, V2, s)
def MUCOND(r, s): return '%s %s = %s %s ∨ %s %s = %s %s' % (V1, r, V1, s, V1, r, V2, s)
def MUC(r, s): return '(if %s then (1 : ℂ) else -1)' % MUCOND(r, s)
SC = '{x : %s | ∃ X Y : %s, %s X ∧ %s Y ∧ featureVec %s = x}' % (E16, TUP, RG, RG, PRODC('X', 'Y'))
def TORC(r, s): return '{x : %s | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec %s}' % (E16, PRODC(TUPC(r, 'z'), TUPC(s, 'w')))
IDX1 = '((p.1.1.1, p.1.2.1.1, p.1.2.2.1), (p.2.1.1, p.2.2.1.1, p.2.2.2.1))'
IDX2 = '((p.1.1.2, p.1.2.1.2, p.1.2.2.2), (p.2.1.2, p.2.2.1.2, p.2.2.2.2))'
PAIRE = ('⟨fun p : %s => (%s, %s), fun r : (%s) × (%s) => (((r.1.1.1, r.2.1.1), (r.1.1.2.1, r.2.1.2.1), (r.1.1.2.2, r.2.1.2.2)), ((r.1.2.1, r.2.2.1), (r.1.2.2.1, r.2.2.2.1), (r.1.2.2.2, r.2.2.2.2))), fun _ => rfl, fun _ => rfl⟩' % (I16, IDX1, IDX2, I4, I4))
CONJE = '⟨fun p : %s => ((p.1.1, p.1.2.2, p.1.2.1), (p.2.2.1, p.2.1, p.2.2.2)), fun p : %s => ((p.1.1, p.1.2.2, p.1.2.1), (p.2.2.1, p.2.1, p.2.2.2)), fun _ => rfl, fun _ => rfl⟩' % (I4, I4)
F4I = '!![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I]'
TW = '(if j.1.val % 2 = 0 then Complex.I else -Complex.I)'
F4T = '!![1, 1, 1, 1; 1, %s, -1, -%s; 1, -1, 1, -1; 1, -%s, -1, %s]' % (TW, TW, TW, TW)
HDEF = '(Matrix.of fun i j : Fin 4 × Fin 4 => (1 / 4 : ℂ) * %s i.1 j.1 * %s i.2 j.2)' % (F4I, F4T)
F4IV = '![![1, 1, 1, 1], ![1, Complex.I, -1, -Complex.I], ![1, -1, 1, -1], ![1, -Complex.I, -1, Complex.I]]'
F4TV = '![![1, 1, 1, 1], ![1, %s, -1, -%s], ![1, -1, 1, -1], ![1, -%s, -1, %s]]' % (TW, TW, TW, TW)
H0DEF = '(Matrix.of fun i j : Fin 4 × Fin 4 => (1 / 4 : ℂ) * %s i.1 j.1 * %s i.2 j.2)' % (F4I, F4I)
def GOF(H): return '(fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => star (%s i j) * %s i k)' % (H, H)
GP = 'Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2'
Q11 = '(((2, 1), (0, 0), (2, 2)), ((0, 0), (2, 2), (2, 3)))'
Q22 = '(((2, 0), (3, 3), (2, 2)), ((1, 3), (3, 0), (3, 3)))'
Q12 = '(((2, 0), (0, 3), (2, 2)), ((0, 3), (2, 0), (2, 3)))'
Q21 = '(((2, 1), (3, 0), (2, 2)), ((1, 0), (3, 2), (3, 3)))'
ONE = '(1 : Equiv.Perm (Fin 4))'

out = []
def thm(name, stmt, proof):
    out.append('theorem %s :\n    %s := by\n%s\n#print axioms %s\n\n' % (name, stmt, proof, name))

# ---------------------------------------------------------------- generic helpers
thm('a34_shared_feature_ext', '∀ G H : %s, featureVec G = featureVec H ↔ ∀ p : %s, mixedTriple G p = mixedTriple H p' % (TUP16, I16),
'''  intro G H
  constructor
  · intro h p
    have := congrArg (fun x : %s => x.ofLp p) h
    simpa [featureVec_ofLp] using this
  · intro h
    unfold featureVec
    exact congrArg _ (funext h)''' % E16)

thm('a34_shared_fact', '∀ (X Y : %s) (p : %s), mixedTriple %s p = mixedTriple X %s * mixedTriple Y %s' % (TUP, I16, PRODC('X', 'Y'), IDX1, IDX2),
'''  intro X Y p
  obtain ⟨⟨a, b, c⟩, ⟨d, e, f⟩⟩ := p
  simp only [mixedTriple, Matrix.of_apply]
  ring''')

thm('a34_shared_prod_congr', '∀ X X\' Y Y\' : %s, featureVec X = featureVec X\' → featureVec Y = featureVec Y\' → featureVec %s = featureVec %s' % (TUP, PRODC('X', 'Y'), PRODC("X'", "Y'")),
'''  intro X X' Y Y' hX hY
  rw [a34_shared_feature_ext]
  intro p
  rw [a34_shared_fact, a34_shared_fact, (a33_shared_feature_ext X X').1 hX, (a33_shared_feature_ext Y Y').1 hY]''')

thm('a34_shared_inner_core', '∀ X Y X\' Y\' : %s, inner ℂ (featureVec %s) (featureVec %s) = inner ℂ (featureVec X) (featureVec X\') * inner ℂ (featureVec Y) (featureVec Y\')' % (TUP, PRODC('X', 'Y'), PRODC("X'", "Y'")),
'''  intro X Y X' Y'
  simp only [featureVec, PiLp.inner_apply, RCLike.inner_apply, WithLp.ofLp_toLp]
  rw [Finset.sum_mul_sum, ← Fintype.sum_prod_type']
  exact Fintype.sum_equiv %s _ _ (fun p => by simp only [Equiv.coe_fn_mk, a34_shared_fact, map_mul]; ring)''' % PAIRE)

thm('a34_shared_dist_inner', '∀ {E : Type} [NormedAddCommGroup E] [InnerProductSpace ℂ E] (x y : E), dist x y ^ 2 = ‖x‖ ^ 2 + ‖y‖ ^ 2 - 2 * (inner ℂ x y).re',
'''  intro E _ _ x y
  rw [dist_eq_norm, ← inner_self_eq_norm_sq (𝕜 := ℂ) (x - y), ← inner_self_eq_norm_sq (𝕜 := ℂ) x, ← inner_self_eq_norm_sq (𝕜 := ℂ) y, inner_sub_left, inner_sub_right, inner_sub_right, map_sub, map_sub, map_sub, inner_re_symm y x]
  simp only [RCLike.re_to_complex]
  ring''')

thm('a34_shared_dist_of_sq', '∀ {E E\' : Type} [MetricSpace E] [MetricSpace E\'] (a b : E) (c d : E\'), dist a b ^ 2 = dist c d ^ 2 → dist a b = dist c d',
'''  intro E E' _ _ a b c d h
  have ha : 0 ≤ dist a b := dist_nonneg
  have hc : 0 ≤ dist c d := dist_nonneg
  rw [← Real.sqrt_sq ha, ← Real.sqrt_sq hc, h]''')

thm('a34_shared_entry_norm', HEADLINE + ' ∀ G : %s, %s G → ∀ i j k : Fin 4, ‖G i j k‖ = 1 / 4' % (TUP, RG),
'''  intro Γ₀ hΓ₀ G hG i j k
  obtain ⟨U, hU, hFU⟩ := sh1_sufficiency (0 : Fin 1) hG
  have hn : ∀ a : Fin 4, ‖U (i, 0) (a, 0)‖ = 1 / 2 := by
    intro a
    have h1 := hU.2 i a
    rw [Fin.sum_univ_one, hΓ₀] at h1
    simp only [Matrix.of_apply] at h1
    have h0 : 0 ≤ ‖U (i, 0) (a, 0)‖ := norm_nonneg _
    have h2 : (‖U (i, 0) (a, 0)‖ - 1 / 2) * (‖U (i, 0) (a, 0)‖ + 1 / 2) = 0 := by ring_nf; linarith
    rcases mul_eq_zero.1 h2 with h3 | h3
    · linarith
    · linarith
  rw [← hFU, fibreGram_apply, Fin.sum_univ_one, norm_mul, norm_star, hn j, hn k]
  norm_num''')

thm('a34_shared_norm_sq_one', HEADLINE + ' ∀ G : %s, %s G → ∑ p : %s, ‖mixedTriple G p‖ ^ 2 = 1' % (TUP, RG, I4),
'''  intro Γ₀ hΓ₀ G hG
  have h : ∀ p : %s, ‖mixedTriple G p‖ = 1 / 64 := by
    intro p
    obtain ⟨⟨a, b, c⟩, ⟨d, e, f⟩⟩ := p
    simp only [mixedTriple]
    rw [norm_mul, norm_mul, a34_shared_entry_norm Γ₀ hΓ₀ G hG, a34_shared_entry_norm Γ₀ hΓ₀ G hG, a34_shared_entry_norm Γ₀ hΓ₀ G hG]
    norm_num
  simp only [h, Finset.sum_const, Finset.card_univ, Fintype.card_prod, Fintype.card_fin, nsmul_eq_mul]
  norm_num''' % I4)

thm('a34_shared_norm_one', HEADLINE + ' ∀ G : %s, %s G → ‖featureVec G‖ = 1' % (TUP, RG),
'''  intro Γ₀ hΓ₀ G hG
  rw [EuclideanSpace.norm_eq]
  exact Real.sqrt_eq_one.2 (a34_shared_norm_sq_one Γ₀ hΓ₀ G hG)''')

thm('a34_shared_inner_self', HEADLINE + ' ∀ G : %s, %s G → inner ℂ (featureVec G) (featureVec G) = 1' % (TUP, RG),
'''  intro Γ₀ hΓ₀ G hG
  rw [inner_self_eq_norm_sq_to_K, a34_shared_norm_one Γ₀ hΓ₀ G hG]
  simp''')

thm('a34_shared_real', '∀ G H : %s, (∀ i, (G i).IsHermitian) → (∀ i, (H i).IsHermitian) → (inner ℂ (featureVec G) (featureVec H)).im = 0' % TUP,
'''  intro G H hG hH
  have hg : ∀ (K : %s), (∀ i, (K i).IsHermitian) → ∀ p : %s, mixedTriple K ((p.1.1, p.1.2.2, p.1.2.1), (p.2.2.1, p.2.1, p.2.2.2)) = star (mixedTriple K p) := by
    intro K hK p
    obtain ⟨⟨a, b, c⟩, ⟨d, e, f⟩⟩ := p
    simp only [mixedTriple]
    rw [star_mul', star_mul', (hK a).apply, (hK b).apply, (hK c).apply]
    ring
  have hsum : inner ℂ (featureVec G) (featureVec H) = (starRingEnd ℂ) (inner ℂ (featureVec G) (featureVec H)) := by
    simp only [featureVec, PiLp.inner_apply, RCLike.inner_apply, WithLp.ofLp_toLp, map_sum, map_mul, Complex.conj_conj]
    exact Fintype.sum_equiv %s _ _ (fun p => by simp only [Equiv.coe_fn_mk, hg G hG p, hg H hH p, Complex.star_def, Complex.conj_conj]; try ring)
  exact Complex.conj_eq_iff_im.1 hsum.symm''' % (TUP, I4, CONJE))

thm('a34_shared_hermitian', HEADLINE + ' ∀ G : %s, %s G → ∀ i, (G i).IsHermitian' % (TUP, RG),
'''  intro Γ₀ hΓ₀ G hG i
  exact (hG.1 i).1''')

thm('a34_shared_re_of_dist', HEADLINE + ' ∀ X Z : %s, %s X → %s Z → (inner ℂ (featureVec X) (featureVec Z)).re = 1 - dist (featureVec X) (featureVec Z) ^ 2 / 2' % (TUP, RG, RG),
'''  intro Γ₀ hΓ₀ X Z hX hZ
  have h := a34_shared_dist_inner (featureVec X) (featureVec Z)
  rw [a34_shared_norm_one Γ₀ hΓ₀ X hX, a34_shared_norm_one Γ₀ hΓ₀ Z hZ] at h
  linarith''')

thm('a34_shared_stratum_dist', HEADLINE + ' ∀ X Y Z W : %s, %s X → %s Y → %s Z → %s W → dist (featureVec %s) (featureVec %s) ^ 2 = 2 - 2 * ((inner ℂ (featureVec X) (featureVec Z)).re * (inner ℂ (featureVec Y) (featureVec W)).re)' % (TUP, RG, RG, RG, RG, PRODC('X', 'Y'), PRODC('Z', 'W')),
'''  intro Γ₀ hΓ₀ X Y Z W hX hY hZ hW
  rw [a34_shared_dist_inner, a34_shared_inner_core, ← inner_self_eq_norm_sq (𝕜 := ℂ) (featureVec %s), ← inner_self_eq_norm_sq (𝕜 := ℂ) (featureVec %s), a34_shared_inner_core, a34_shared_inner_core, a34_shared_inner_self Γ₀ hΓ₀ X hX, a34_shared_inner_self Γ₀ hΓ₀ Y hY, a34_shared_inner_self Γ₀ hΓ₀ Z hZ, a34_shared_inner_self Γ₀ hΓ₀ W hW]
  simp only [RCLike.re_to_complex, Complex.mul_re, a34_shared_real X Z (a34_shared_hermitian Γ₀ hΓ₀ X hX) (a34_shared_hermitian Γ₀ hΓ₀ Z hZ), Complex.one_re, Complex.one_im]
  ring''' % (PRODC('X', 'Y'), PRODC('Z', 'W')))

thm('a34_shared_fibre_core', HEADLINE + ' ∀ X X\' Y : %s, %s Y → dist (featureVec %s) (featureVec %s) = dist (featureVec X) (featureVec X\') ∧ dist (featureVec %s) (featureVec %s) = dist (featureVec X) (featureVec X\')' % (TUP, RG, PRODC('X', 'Y'), PRODC("X'", 'Y'), PRODC('Y', 'X'), PRODC('Y', "X'")),
'''  intro Γ₀ hΓ₀ X X' Y hY
  have hYY := a34_shared_inner_self Γ₀ hΓ₀ Y hY
  constructor
  · apply a34_shared_dist_of_sq
    rw [a34_shared_dist_inner, a34_shared_dist_inner, ← inner_self_eq_norm_sq (𝕜 := ℂ) (featureVec %s), ← inner_self_eq_norm_sq (𝕜 := ℂ) (featureVec %s), ← inner_self_eq_norm_sq (𝕜 := ℂ) (featureVec X), ← inner_self_eq_norm_sq (𝕜 := ℂ) (featureVec X'), a34_shared_inner_core, a34_shared_inner_core, a34_shared_inner_core, hYY, mul_one, mul_one, mul_one]
  · apply a34_shared_dist_of_sq
    rw [a34_shared_dist_inner, a34_shared_dist_inner, ← inner_self_eq_norm_sq (𝕜 := ℂ) (featureVec %s), ← inner_self_eq_norm_sq (𝕜 := ℂ) (featureVec %s), ← inner_self_eq_norm_sq (𝕜 := ℂ) (featureVec X), ← inner_self_eq_norm_sq (𝕜 := ℂ) (featureVec X'), a34_shared_inner_core, a34_shared_inner_core, a34_shared_inner_core, hYY, one_mul, one_mul, one_mul]''' % (PRODC('X', 'Y'), PRODC("X'", 'Y'), PRODC('Y', 'X'), PRODC('Y', "X'")))

thm('a34_shared_diag_coord', HEADLINE + ' ∀ Y : %s, %s Y → mixedTriple Y ((0, 0, 0), (0, 0, 0)) = 1 / 64' % (TUP, RG),
'''  intro Γ₀ hΓ₀ Y hY
  have h := hY.2.2.2 0 0
  rw [hΓ₀] at h
  simp only [Matrix.of_apply] at h
  simp only [mixedTriple, h]
  push_cast
  norm_num''')

thm('a34_shared_pair_core', HEADLINE + ' ∀ X Y X\' Y\' : %s, %s X → %s Y → %s X\' → %s Y\' → featureVec %s = featureVec %s → featureVec X = featureVec X\' ∧ featureVec Y = featureVec Y\'' % (TUP, RG, RG, RG, RG, PRODC('X', 'Y'), PRODC("X'", "Y'")),
'''  intro Γ₀ hΓ₀ X Y X' Y' hX hY hX' hY' h
  have hq := (a34_shared_feature_ext _ _).1 h
  have h64 : (1 / 64 : ℂ) ≠ 0 := by norm_num
  constructor
  · rw [a33_shared_feature_ext]
    intro p
    have e := hq (((p.1.1, 0), (p.1.2.1, 0), (p.1.2.2, 0)), ((p.2.1, 0), (p.2.2.1, 0), (p.2.2.2, 0)))
    rw [a34_shared_fact, a34_shared_fact] at e
    simp only [a34_shared_diag_coord Γ₀ hΓ₀ Y hY, a34_shared_diag_coord Γ₀ hΓ₀ Y' hY'] at e
    exact mul_right_cancel₀ h64 e
  · rw [a33_shared_feature_ext]
    intro p
    have e := hq (((0, p.1.1), (0, p.1.2.1), (0, p.1.2.2)), ((0, p.2.1), (0, p.2.2.1), (0, p.2.2.2)))
    rw [a34_shared_fact, a34_shared_fact] at e
    simp only [a34_shared_diag_coord Γ₀ hΓ₀ X hX, a34_shared_diag_coord Γ₀ hΓ₀ X' hX'] at e
    exact mul_left_cancel₀ h64 e''')

thm('a34_shared_unit_mu', '∀ r s : Fin 9, star %s * %s = 1' % (MUC('r', 's'), MUC('r', 's')),
'''  intro r s
  split_ifs <;> simp''')

# ---------------------------------------------------------------- the nine-way and 81-way tables
def cases9(body_fn, hyp_simp=None):
    lines = []
    for r in range(9):
        lines.append('  · ' + body_fn(r))
    return '\n'.join(lines)

thm('a34_shared_tup_real', HEADLINE + ' ∀ (r : Fin 9) (z : ℂ), star z * z = 1 → %s %s' % (RG, TUPC('r', 'z')),
'''  intro Γ₀ hΓ₀ r z hz
  rcases a33_shared_fin9 r with %s <;> simp only [%s]
%s''' % (FIN9, RS, cases9(lambda r: 'exact (iso2_classes_single Γ₀ hΓ₀).2 _ _ z hz')))

thm('a34_shared_pt_inj', '∀ (r : Fin 9) (z w : ℂ), star z * z = 1 → star w * w = 1 → featureVec %s = featureVec %s → z = w' % (TUPC('r', 'z'), TUPC('r', 'w')),
'''  intro r z w hz hw h
  rcases a33_shared_fin9 r with %s <;> simp only [%s] at h
%s''' % (FIN9, RS, cases9(lambda r: 'exact a33_shared_inj_%d z w hz hw h' % r)))

def bullets81(fn):
    lines = []
    for r in range(9):
        for s in range(9):
            b = fn(r, s)
            if b is not None:
                lines.append('  · ' + b)
    return '\n'.join(lines)

def ifrw(r, s):
    return ('rw [if_pos (show %s by decide)]' if mu(r, s) == 1 else 'rw [if_neg (show ¬ (%s) by decide)]') % MUCOND(r, s)

thm('a34_shared_meet_core', '∀ (r r\' : Fin 9) (z z\' : ℂ), %s → star z * z = 1 → star z\' * z\' = 1 → featureVec %s = featureVec %s → z = %s ∧ z\' = %s' % (ADJC('r', "r'"), TUPC('r', 'z'), TUPC("r'", "z'"), MUC('r', "r'"), MUC("r'", 'r')),
'''  intro r r' z z' hadj hz hz' h
  rcases a33_shared_fin9 r with %s <;> rcases a33_shared_fin9 r' with %s <;> (try exact absurd hadj (by decide)) <;> simp only [%s] at h
%s''' % (FIN9, FIN9, RS, bullets81(lambda r, s: None if not adj(r, s) else '%s\n    %s\n    exact ⟨a33_shared_meet_%d_%d z z\' hz hz\' h, a33_shared_meet_%d_%d z\' z hz\' hz h.symm⟩' % (ifrw(r, s), ifrw(s, r), r, s, s, r))))

INC = [(0,'p',4,'p'),(0,'p',8,'p'),(0,'m',5,'m'),(0,'m',7,'m'),(1,'p',3,'p'),(1,'p',8,'m'),(1,'m',5,'p'),(1,'m',6,'m'),(2,'p',4,'m'),(2,'p',6,'p'),(2,'m',3,'m'),(2,'m',7,'p')]
def sgn_at(r, v): return 'p' if v1[r] == v else 'm'
def inc_term(r, s):
    v = [x for x in (v1[r], v2[r]) if x in (v1[s], v2[s])][0]
    sr, ss = sgn_at(r, v), sgn_at(s, v)
    for (a, x, b, y) in INC:
        if (a, x, b, y) == (r, sr, s, ss): return 'a33_shared_inc_%d_%s_%d_%s' % (a, x, b, y)
        if (a, x, b, y) == (s, ss, r, sr): return '(a33_shared_inc_%d_%s_%d_%s).symm' % (a, x, b, y)
    for (a, x, b, y) in INC:
        if (b, y) == (r, sr):
            for (a2, x2, b2, y2) in INC:
                if (a2, x2) == (a, x) and (b2, y2) == (s, ss):
                    return '(a33_shared_inc_%d_%s_%d_%s).symm.trans a33_shared_inc_%d_%s_%d_%s' % (a, x, b, y, a2, x2, b2, y2)
    raise AssertionError((r, s))

thm('a34_shared_vertex_core', '∀ r r\' : Fin 9, %s → featureVec %s = featureVec %s' % (ADJC('r', "r'"), TUPC('r', MUC('r', "r'")), TUPC("r'", MUC("r'", 'r'))),
'''  intro r r' hadj
  rcases a33_shared_fin9 r with %s <;> rcases a33_shared_fin9 r' with %s <;> (try exact absurd hadj (by decide)) <;> simp only [%s]
%s''' % (FIN9, FIN9, RS, bullets81(lambda r, s: None if not adj(r, s) else '%s\n    %s\n    exact %s' % (ifrw(r, s), ifrw(s, r), inc_term(r, s)))))

thm('a34_shared_apart_core', '∀ (r r\' : Fin 9) (z z\' : ℂ), r ≠ r\' → ¬ %s → star z * z = 1 → star z\' * z\' = 1 → featureVec %s ≠ featureVec %s' % (ADJC('r', "r'"), TUPC('r', 'z'), TUPC("r'", "z'")),
'''  intro r r' z z' hne hna hz hz'
  rcases a33_shared_fin9 r with %s <;> rcases a33_shared_fin9 r' with %s <;> (try exact absurd rfl hne) <;> (try exact absurd (by decide) hna) <;> simp only [%s]
%s''' % (FIN9, FIN9, RS, bullets81(lambda r, s: None if (r == s or adj(r, s)) else 'exact a33_shared_apart_%d_%d z z\' hz hz\'' % (r, s))))

# ---------------------------------------------------------------- the tori
thm('a34_shared_cover_core', HEADLINE + ' %s = ⋃ (r : Fin 9) (s : Fin 9), %s' % (SC, TORC('r', 's')),
'''  intro Γ₀ hΓ₀
  ext x
  simp only [Set.mem_iUnion, Set.mem_setOf_eq]
  constructor
  · rintro ⟨X, Y, hX, hY, rfl⟩
    obtain ⟨r, z, hz, hx⟩ := (a33_shared_mem Γ₀ hΓ₀ (featureVec X)).1 (featureVec_mem_normalizedSet hX)
    obtain ⟨s, w, hw, hy⟩ := (a33_shared_mem Γ₀ hΓ₀ (featureVec Y)).1 (featureVec_mem_normalizedSet hY)
    exact ⟨r, s, z, w, hz, hw, a34_shared_prod_congr X %s Y %s hx hy⟩
  · rintro ⟨r, s, z, w, hz, hw, rfl⟩
    exact ⟨_, _, a34_shared_tup_real Γ₀ hΓ₀ r z hz, a34_shared_tup_real Γ₀ hΓ₀ s w hw, rfl⟩''' % (TUPC('r', 'z'), TUPC('s', 'w')))

thm('a34_shared_point_core', HEADLINE + ' ∀ r r\' s s\' : Fin 9, %s → %s → %s ∩ %s = {featureVec %s}' % (ADJC('r', "r'"), ADJC('s', "s'"), TORC('r', 's'), TORC("r'", "s'"), PRODC(TUPC('r', MUC('r', "r'")), TUPC('s', MUC('s', "s'")))),
'''  intro Γ₀ hΓ₀ r r' s s' hrr hss
  ext x
  simp only [Set.mem_inter_iff, Set.mem_setOf_eq, Set.mem_singleton_iff]
  constructor
  · rintro ⟨⟨z, w, hz, hw, rfl⟩, ⟨z', w', hz', hw', h⟩⟩
    obtain ⟨h1, h2⟩ := a34_shared_pair_core Γ₀ hΓ₀ _ _ _ _ (a34_shared_tup_real Γ₀ hΓ₀ r z hz) (a34_shared_tup_real Γ₀ hΓ₀ s w hw) (a34_shared_tup_real Γ₀ hΓ₀ r' z' hz') (a34_shared_tup_real Γ₀ hΓ₀ s' w' hw') h
    obtain ⟨hz1, -⟩ := a34_shared_meet_core r r' z z' hrr hz hz' h1
    obtain ⟨hw1, -⟩ := a34_shared_meet_core s s' w w' hss hw hw' h2
    rw [hz1, hw1]
  · rintro rfl
    refine ⟨⟨_, _, a34_shared_unit_mu r r', a34_shared_unit_mu s s', rfl⟩, ⟨_, _, a34_shared_unit_mu r' r, a34_shared_unit_mu s' s, ?_⟩⟩
    exact a34_shared_prod_congr %s %s %s %s (a34_shared_vertex_core r r' hrr) (a34_shared_vertex_core s s' hss)''' % (TUPC('r', MUC('r', "r'")), TUPC("r'", MUC("r'", 'r')), TUPC('s', MUC('s', "s'")), TUPC("s'", MUC("s'", 's'))))

thm('a34_shared_circle_left_core', HEADLINE + ' ∀ r s s\' : Fin 9, %s → %s ∩ %s = {x : %s | ∃ z : ℂ, star z * z = 1 ∧ x = featureVec %s}' % (ADJC('s', "s'"), TORC('r', 's'), TORC('r', "s'"), E16, PRODC(TUPC('r', 'z'), TUPC('s', MUC('s', "s'")))),
'''  intro Γ₀ hΓ₀ r s s' hss
  ext x
  simp only [Set.mem_inter_iff, Set.mem_setOf_eq]
  constructor
  · rintro ⟨⟨z, w, hz, hw, rfl⟩, ⟨z', w', hz', hw', h⟩⟩
    obtain ⟨-, h2⟩ := a34_shared_pair_core Γ₀ hΓ₀ _ _ _ _ (a34_shared_tup_real Γ₀ hΓ₀ r z hz) (a34_shared_tup_real Γ₀ hΓ₀ s w hw) (a34_shared_tup_real Γ₀ hΓ₀ r z' hz') (a34_shared_tup_real Γ₀ hΓ₀ s' w' hw') h
    obtain ⟨hw1, -⟩ := a34_shared_meet_core s s' w w' hss hw hw' h2
    exact ⟨z, hz, by rw [hw1]⟩
  · rintro ⟨z, hz, rfl⟩
    refine ⟨⟨z, _, hz, a34_shared_unit_mu s s', rfl⟩, ⟨z, _, hz, a34_shared_unit_mu s' s, ?_⟩⟩
    exact a34_shared_prod_congr %s %s %s %s rfl (a34_shared_vertex_core s s' hss)''' % (TUPC('r', 'z'), TUPC('r', 'z'), TUPC('s', MUC('s', "s'")), TUPC("s'", MUC("s'", 's'))))

thm('a34_shared_circle_right_core', HEADLINE + ' ∀ r r\' s : Fin 9, %s → %s ∩ %s = {x : %s | ∃ w : ℂ, star w * w = 1 ∧ x = featureVec %s}' % (ADJC('r', "r'"), TORC('r', 's'), TORC("r'", 's'), E16, PRODC(TUPC('r', MUC('r', "r'")), TUPC('s', 'w'))),
'''  intro Γ₀ hΓ₀ r r' s hrr
  ext x
  simp only [Set.mem_inter_iff, Set.mem_setOf_eq]
  constructor
  · rintro ⟨⟨z, w, hz, hw, rfl⟩, ⟨z', w', hz', hw', h⟩⟩
    obtain ⟨h1, -⟩ := a34_shared_pair_core Γ₀ hΓ₀ _ _ _ _ (a34_shared_tup_real Γ₀ hΓ₀ r z hz) (a34_shared_tup_real Γ₀ hΓ₀ s w hw) (a34_shared_tup_real Γ₀ hΓ₀ r' z' hz') (a34_shared_tup_real Γ₀ hΓ₀ s w' hw') h
    obtain ⟨hz1, -⟩ := a34_shared_meet_core r r' z z' hrr hz hz' h1
    exact ⟨w, hw, by rw [hz1]⟩
  · rintro ⟨w, hw, rfl⟩
    refine ⟨⟨_, w, a34_shared_unit_mu r r', hw, rfl⟩, ⟨_, w, a34_shared_unit_mu r' r, hw, ?_⟩⟩
    exact a34_shared_prod_congr %s %s %s %s (a34_shared_vertex_core r r' hrr) rfl''' % (TUPC('r', MUC('r', "r'")), TUPC("r'", MUC("r'", 'r')), TUPC('s', 'w'), TUPC('s', 'w')))

thm('a34_shared_apart_tori_core', HEADLINE + ' ∀ r r\' s s\' : Fin 9, (r ≠ r\' ∧ ¬ %s) ∨ (s ≠ s\' ∧ ¬ %s) → %s ∩ %s = ∅' % (ADJC('r', "r'"), ADJC('s', "s'"), TORC('r', 's'), TORC("r'", "s'")),
'''  intro Γ₀ hΓ₀ r r' s s' hyp
  ext x
  simp only [Set.mem_inter_iff, Set.mem_setOf_eq, Set.mem_empty_iff_false, iff_false, not_and]
  rintro ⟨z, w, hz, hw, rfl⟩ ⟨z', w', hz', hw', h⟩
  obtain ⟨h1, h2⟩ := a34_shared_pair_core Γ₀ hΓ₀ _ _ _ _ (a34_shared_tup_real Γ₀ hΓ₀ r z hz) (a34_shared_tup_real Γ₀ hΓ₀ s w hw) (a34_shared_tup_real Γ₀ hΓ₀ r' z' hz') (a34_shared_tup_real Γ₀ hΓ₀ s' w' hw') h
  rcases hyp with ⟨hne, hna⟩ | ⟨hne, hna⟩
  · exact a34_shared_apart_core r r' z z' hne hna hz hz' h1
  · exact a34_shared_apart_core s s' w w' hne hna hw hw' h2''')

# ---------------------------------------------------------------- the action
PTENS = '∃ X Y X\' Y\' : %s, %s X ∧ %s Y ∧ %s X\' ∧ %s Y\' ∧ featureVec %s = x ∧ f (featureVec X) = featureVec X\' ∧ g (featureVec Y) = featureVec Y\' ∧ y = featureVec %s' % (TUP, RG, RG, RG, RG, PRODC('X', 'Y'), PRODC("X'", "Y'"))
thm('a34_shared_tensor_core', HEADLINE + ' ∀ f g : %s → %s, IsSurjIsometryOn (normalizedSet Γ₀) f → IsSurjIsometryOn (normalizedSet Γ₀) g → ∃ F : %s → %s, IsSurjIsometryOn %s F ∧ ∀ X Y X\' Y\' : %s, %s X → %s Y → %s X\' → %s Y\' → f (featureVec X) = featureVec X\' → g (featureVec Y) = featureVec Y\' → F (featureVec %s) = featureVec %s' % (E4, E4, E16, E16, SC, TUP, RG, RG, RG, RG, PRODC('X', 'Y'), PRODC("X'", "Y'")),
'''  intro Γ₀ hΓ₀ f g hf hg
  classical
  have hex : ∀ x : %s, x ∈ %s → ∃ y : %s, %s := by
    rintro x ⟨X, Y, hX, hY, rfl⟩
    obtain ⟨X', hX', hfX⟩ := hf.1 _ (featureVec_mem_normalizedSet hX)
    obtain ⟨Y', hY', hgY⟩ := hg.1 _ (featureVec_mem_normalizedSet hY)
    exact ⟨_, X, Y, X', Y', hX, hY, hX', hY', rfl, hfX.symm, hgY.symm, rfl⟩
  let F : %s → %s := fun x => if h : ∃ y : %s, %s then Classical.choose h else x
  have hF : ∀ x : %s, x ∈ %s → ∃ X Y X' Y' : %s, %s X ∧ %s Y ∧ %s X' ∧ %s Y' ∧ featureVec %s = x ∧ f (featureVec X) = featureVec X' ∧ g (featureVec Y) = featureVec Y' ∧ F x = featureVec %s := by
    intro x hx
    have hh := hex x hx
    simp only [F, dif_pos hh]
    exact Classical.choose_spec hh
  refine ⟨F, ⟨?_, ?_, ?_⟩, ?_⟩
  · intro x hx
    obtain ⟨X, Y, X', Y', hX, hY, hX', hY', -, -, -, hFx⟩ := hF x hx
    rw [hFx]
    exact ⟨X', Y', hX', hY', rfl⟩
  · rintro y ⟨Z', W', hZ', hW', rfl⟩
    obtain ⟨x1, hx1, hfx1⟩ := hf.2.1 _ (featureVec_mem_normalizedSet hZ')
    obtain ⟨Z, hZ, rfl⟩ := hx1
    obtain ⟨y1, hy1, hgy1⟩ := hg.2.1 _ (featureVec_mem_normalizedSet hW')
    obtain ⟨W, hW, rfl⟩ := hy1
    refine ⟨featureVec %s, ⟨Z, W, hZ, hW, rfl⟩, ?_⟩
    obtain ⟨X, Y, X', Y', hX, hY, hX', hY', hXY, hfX, hgY, hFx⟩ := hF _ ⟨Z, W, hZ, hW, rfl⟩
    rw [hFx]
    obtain ⟨e1, e2⟩ := a34_shared_pair_core Γ₀ hΓ₀ X Y Z W hX hY hZ hW hXY
    apply a34_shared_prod_congr
    · rw [← hfX, e1, hfx1]
    · rw [← hgY, e2, hgy1]
  · intro x hx y hy
    obtain ⟨X, Y, X', Y', hX, hY, hX', hY', hXY, hfX, hgY, hFx⟩ := hF x hx
    obtain ⟨Z, W, Z', W', hZ, hW, hZ', hW', hZW, hfZ, hgW, hFy⟩ := hF y hy
    rw [hFx, hFy, ← hXY, ← hZW]
    apply a34_shared_dist_of_sq
    rw [a34_shared_stratum_dist Γ₀ hΓ₀ X' Y' Z' W' hX' hY' hZ' hW', a34_shared_stratum_dist Γ₀ hΓ₀ X Y Z W hX hY hZ hW, a34_shared_re_of_dist Γ₀ hΓ₀ X' Z' hX' hZ', a34_shared_re_of_dist Γ₀ hΓ₀ Y' W' hY' hW', a34_shared_re_of_dist Γ₀ hΓ₀ X Z hX hZ, a34_shared_re_of_dist Γ₀ hΓ₀ Y W hY hW, ← hfX, ← hfZ, ← hgY, ← hgW, hf.2.2 _ (featureVec_mem_normalizedSet hX) _ (featureVec_mem_normalizedSet hZ), hg.2.2 _ (featureVec_mem_normalizedSet hY) _ (featureVec_mem_normalizedSet hW)]
  · intro X Y X' Y' hX hY hX' hY' hfX hgY
    obtain ⟨X₁, Y₁, X₁', Y₁', hX₁, hY₁, hX₁', hY₁', hXY, hfX₁, hgY₁, hFx⟩ := hF _ ⟨X, Y, hX, hY, rfl⟩
    rw [hFx]
    obtain ⟨e1, e2⟩ := a34_shared_pair_core Γ₀ hΓ₀ X₁ Y₁ X Y hX₁ hY₁ hX hY hXY
    apply a34_shared_prod_congr
    · rw [← hfX₁, e1, hfX]
    · rw [← hgY₁, e2, hgY]''' % (E16, SC, E16, PTENS, E16, E16, E16, PTENS, E16, SC, TUP, RG, RG, RG, RG, PRODC('X', 'Y'), PRODC("X'", "Y'"), PRODC('Z', 'W')))

PSWAP = '∃ X Y : %s, %s X ∧ %s Y ∧ featureVec %s = x ∧ y = featureVec %s' % (TUP, RG, RG, PRODC('X', 'Y'), PRODC('Y', 'X'))
thm('a34_shared_swap_core', HEADLINE + ' ∃ F : %s → %s, IsSurjIsometryOn %s F ∧ ∀ X Y : %s, %s X → %s Y → F (featureVec %s) = featureVec %s' % (E16, E16, SC, TUP, RG, RG, PRODC('X', 'Y'), PRODC('Y', 'X')),
'''  intro Γ₀ hΓ₀
  classical
  have hex : ∀ x : %s, x ∈ %s → ∃ y : %s, %s := by
    rintro x ⟨X, Y, hX, hY, rfl⟩
    exact ⟨_, X, Y, hX, hY, rfl, rfl⟩
  let F : %s → %s := fun x => if h : ∃ y : %s, %s then Classical.choose h else x
  have hF : ∀ x : %s, x ∈ %s → ∃ X Y : %s, %s X ∧ %s Y ∧ featureVec %s = x ∧ F x = featureVec %s := by
    intro x hx
    have hh := hex x hx
    simp only [F, dif_pos hh]
    exact Classical.choose_spec hh
  refine ⟨F, ⟨?_, ?_, ?_⟩, ?_⟩
  · intro x hx
    obtain ⟨X, Y, hX, hY, -, hFx⟩ := hF x hx
    rw [hFx]
    exact ⟨Y, X, hY, hX, rfl⟩
  · rintro y ⟨Z', W', hZ', hW', rfl⟩
    refine ⟨featureVec %s, ⟨W', Z', hW', hZ', rfl⟩, ?_⟩
    obtain ⟨X, Y, hX, hY, hXY, hFx⟩ := hF _ ⟨W', Z', hW', hZ', rfl⟩
    rw [hFx]
    obtain ⟨e1, e2⟩ := a34_shared_pair_core Γ₀ hΓ₀ X Y W' Z' hX hY hW' hZ' hXY
    exact a34_shared_prod_congr _ _ _ _ e2 e1
  · intro x hx y hy
    obtain ⟨X, Y, hX, hY, hXY, hFx⟩ := hF x hx
    obtain ⟨Z, W, hZ, hW, hZW, hFy⟩ := hF y hy
    rw [hFx, hFy, ← hXY, ← hZW]
    apply a34_shared_dist_of_sq
    rw [a34_shared_stratum_dist Γ₀ hΓ₀ Y X W Z hY hX hW hZ, a34_shared_stratum_dist Γ₀ hΓ₀ X Y Z W hX hY hZ hW]
    ring
  · intro X Y hX hY
    obtain ⟨X₁, Y₁, hX₁, hY₁, hXY, hFx⟩ := hF _ ⟨X, Y, hX, hY, rfl⟩
    rw [hFx]
    obtain ⟨e1, e2⟩ := a34_shared_pair_core Γ₀ hΓ₀ X₁ Y₁ X Y hX₁ hY₁ hX hY hXY
    exact a34_shared_prod_congr _ _ _ _ e2 e1''' % (E16, SC, E16, PSWAP, E16, E16, E16, PSWAP, E16, SC, TUP, RG, RG, PRODC('X', 'Y'), PRODC('Y', 'X'), PRODC("W'", "Z'")))

# ---------------------------------------------------------------- the factorized isometries
LHYP = '∀ (F : %s → %s) (Φ₁ Φ₂ : (%s) → (%s)), IsSurjIsometryOn %s F → (∀ X Y : %s, %s X → %s Y → %s (Φ₁ X) ∧ %s (Φ₂ Y) ∧ F (featureVec %s) = featureVec %s) →' % (E16, E16, TUP, TUP, SC, TUP, RG, RG, RG, RG, PRODC('X', 'Y'), PRODC('(Φ₁ X)', '(Φ₂ Y)'))
LCON = '∃ f g : %s → %s, IsSurjIsometryOn (normalizedSet Γ₀) f ∧ IsSurjIsometryOn (normalizedSet Γ₀) g ∧ ∀ X Y : %s, %s X → %s Y → featureVec (Φ₁ X) = f (featureVec X) ∧ featureVec (Φ₂ Y) = g (featureVec Y)' % (E4, E4, TUP, RG, RG)
Y0 = TUPC('0', '1')
thm('a34_shared_local_core', HEADLINE + ' ' + LHYP + ' ' + LCON,
'''  intro Γ₀ hΓ₀ F Φ₁ Φ₂ hF hfac
  classical
  have hY0 : %s %s := a34_shared_tup_real Γ₀ hΓ₀ 0 1 (by simp)
  -- the factor maps are isometric on realizable inputs
  have iso1 : ∀ X X' : %s, %s X → %s X' → dist (featureVec (Φ₁ X)) (featureVec (Φ₁ X')) = dist (featureVec X) (featureVec X') := by
    intro X X' hX hX'
    have h1 := (a34_shared_fibre_core Γ₀ hΓ₀ (Φ₁ X) (Φ₁ X') (Φ₂ %s) (hfac X _ hX hY0).2.1).1
    have h2 := (a34_shared_fibre_core Γ₀ hΓ₀ X X' %s hY0).1
    rw [← h1, ← (hfac X _ hX hY0).2.2, ← (hfac X' _ hX' hY0).2.2, hF.2.2 _ ⟨X, _, hX, hY0, rfl⟩ _ ⟨X', _, hX', hY0, rfl⟩, h2]
  have iso2 : ∀ Y Y' : %s, %s Y → %s Y' → dist (featureVec (Φ₂ Y)) (featureVec (Φ₂ Y')) = dist (featureVec Y) (featureVec Y') := by
    intro Y Y' hY hY'
    have h1 := (a34_shared_fibre_core Γ₀ hΓ₀ (Φ₂ Y) (Φ₂ Y') (Φ₁ %s) (hfac _ Y hY0 hY).1).2
    have h2 := (a34_shared_fibre_core Γ₀ hΓ₀ Y Y' %s hY0).2
    rw [← h1, ← (hfac _ Y hY0 hY).2.2, ← (hfac _ Y' hY0 hY').2.2, hF.2.2 _ ⟨_, Y, hY0, hY, rfl⟩ _ ⟨_, Y', hY0, hY', rfl⟩, h2]
  have hex1 : ∀ x : %s, x ∈ normalizedSet Γ₀ → ∃ y : %s, ∃ X : %s, %s X ∧ featureVec X = x ∧ y = featureVec (Φ₁ X) := by
    rintro x ⟨X, hX, rfl⟩
    exact ⟨_, X, hX, rfl, rfl⟩
  have hex2 : ∀ x : %s, x ∈ normalizedSet Γ₀ → ∃ y : %s, ∃ X : %s, %s X ∧ featureVec X = x ∧ y = featureVec (Φ₂ X) := by
    rintro x ⟨X, hX, rfl⟩
    exact ⟨_, X, hX, rfl, rfl⟩
  let f : %s → %s := fun x => if h : ∃ y : %s, ∃ X : %s, %s X ∧ featureVec X = x ∧ y = featureVec (Φ₁ X) then Classical.choose h else x
  let g : %s → %s := fun x => if h : ∃ y : %s, ∃ X : %s, %s X ∧ featureVec X = x ∧ y = featureVec (Φ₂ X) then Classical.choose h else x
  have hf1 : ∀ x : %s, x ∈ normalizedSet Γ₀ → ∃ X : %s, %s X ∧ featureVec X = x ∧ f x = featureVec (Φ₁ X) := by
    intro x hx
    have hh := hex1 x hx
    simp only [f, dif_pos hh]
    exact Classical.choose_spec hh
  have hg1 : ∀ x : %s, x ∈ normalizedSet Γ₀ → ∃ X : %s, %s X ∧ featureVec X = x ∧ g x = featureVec (Φ₂ X) := by
    intro x hx
    have hh := hex2 x hx
    simp only [g, dif_pos hh]
    exact Classical.choose_spec hh
  have hfv : ∀ X : %s, %s X → f (featureVec X) = featureVec (Φ₁ X) := by
    intro X hX
    obtain ⟨X₁, hX₁, e, hfx⟩ := hf1 _ (featureVec_mem_normalizedSet hX)
    rw [hfx]
    apply dist_eq_zero.1
    rw [iso1 X₁ X hX₁ hX, e, dist_self]
  have hgv : ∀ Y : %s, %s Y → g (featureVec Y) = featureVec (Φ₂ Y) := by
    intro Y hY
    obtain ⟨Y₁, hY₁, e, hgy⟩ := hg1 _ (featureVec_mem_normalizedSet hY)
    rw [hgy]
    apply dist_eq_zero.1
    rw [iso2 Y₁ Y hY₁ hY, e, dist_self]
  refine ⟨f, g, ⟨?_, ?_, ?_⟩, ⟨?_, ?_, ?_⟩, fun X Y hX hY => ⟨(hfv X hX).symm, (hgv Y hY).symm⟩⟩
  · rintro x ⟨X, hX, rfl⟩
    rw [hfv X hX]
    exact featureVec_mem_normalizedSet (hfac X _ hX hY0).1
  · rintro y ⟨X'', hX'', rfl⟩
    obtain ⟨x₀, hx₀, hFx₀⟩ := hF.2.1 _ ⟨X'', _, hX'', hY0, rfl⟩
    obtain ⟨X, Y, hX, hY, rfl⟩ := hx₀
    rw [(hfac X Y hX hY).2.2] at hFx₀
    obtain ⟨e1, -⟩ := a34_shared_pair_core Γ₀ hΓ₀ _ _ _ _ (hfac X Y hX hY).1 (hfac X Y hX hY).2.1 hX'' hY0 hFx₀
    exact ⟨featureVec X, featureVec_mem_normalizedSet hX, by rw [hfv X hX, e1]⟩
  · rintro x ⟨X, hX, rfl⟩ y ⟨Z, hZ, rfl⟩
    rw [hfv X hX, hfv Z hZ, iso1 X Z hX hZ]
  · rintro x ⟨Y, hY, rfl⟩
    rw [hgv Y hY]
    exact featureVec_mem_normalizedSet (hfac _ Y hY0 hY).2.1
  · rintro y ⟨Y'', hY'', rfl⟩
    obtain ⟨x₀, hx₀, hFx₀⟩ := hF.2.1 _ ⟨_, Y'', hY0, hY'', rfl⟩
    obtain ⟨X, Y, hX, hY, rfl⟩ := hx₀
    rw [(hfac X Y hX hY).2.2] at hFx₀
    obtain ⟨-, e2⟩ := a34_shared_pair_core Γ₀ hΓ₀ _ _ _ _ (hfac X Y hX hY).1 (hfac X Y hX hY).2.1 hY0 hY'' hFx₀
    exact ⟨featureVec Y, featureVec_mem_normalizedSet hY, by rw [hgv Y hY, e2]⟩
  · rintro x ⟨Y, hY, rfl⟩ y ⟨W, hW, rfl⟩
    rw [hgv Y hY, hgv W hW, iso2 Y W hY hW]''' % (RG, Y0, TUP, RG, RG, Y0, Y0, TUP, RG, RG, Y0, Y0, E4, E4, TUP, RG, E4, E4, TUP, RG, E4, E4, E4, TUP, RG, E4, E4, E4, TUP, RG, E4, TUP, RG, E4, TUP, RG, TUP, RG, TUP, RG))

# ---------------------------------------------------------------- the properness witness and controls
thm('a34_shared_f4i_unit', '∀ x y : Fin 4, star (%s x y) * %s x y = 1' % (F4I, F4I),
'''  intro x y
  fin_cases x <;> fin_cases y <;> simp [Complex.star_def, Complex.conj_I]''')

thm('a34_shared_f4t_unit', '∀ (x y : Fin 4) (j : Fin 4 × Fin 4), star (%s x y) * %s x y = 1' % (F4T, F4T),
'''  intro x y j
  fin_cases x <;> fin_cases y <;> split_ifs <;> simp [Complex.star_def, Complex.conj_I]''')

for j1 in range(4):
    for j2 in range(4):
        thm('a34_shared_unit_col_%d_%d' % (j1, j2), '∀ k : Fin 4 × Fin 4, ∑ i : Fin 4 × Fin 4, star (%s i ((%d, %d) : Fin 4 × Fin 4)) * %s i k = if ((%d, %d) : Fin 4 × Fin 4) = k then 1 else 0' % (HDEF, j1, j2, HDEF, j1, j2),
"""  intro k
  rcases k with ⟨k1, k2⟩
  fin_cases k1 <;> fin_cases k2 <;> simp +decide [Fintype.sum_prod_type, Fin.sum_univ_four, Complex.star_def, Complex.conj_I, Complex.ext_iff] <;> norm_num""")

thm('a34_shared_proper_core', HEADLINE + ' RealizableGram (Fin 1 × Fin 1) (%s) %s ∧ ∀ X Y : %s, featureVec %s ≠ featureVec %s' % (GP, GOF(HDEF), TUP, PRODC('X', 'Y'), GOF(HDEF)),
'''  intro Γ₀ hΓ₀
  have hFn : ∀ x y : Fin 4, ‖%s x y‖ = 1 := by
    intro x y
    fin_cases x <;> fin_cases y <;> simp
  have hTn : ∀ (x y : Fin 4) (j : Fin 4 × Fin 4), ‖%s x y‖ = 1 := by
    intro x y j
    fin_cases x <;> fin_cases y <;> split_ifs <;> simp
  have hsum : ∀ f : (Fin 4 × Fin 4) × (Fin 1 × Fin 1) → ℂ, ∑ x, f x = ∑ r : Fin 4 × Fin 4, f (r, ((0 : Fin 1), (0 : Fin 1))) := by
    intro f
    rw [Fintype.sum_prod_type]
    exact Finset.sum_congr rfl (fun r _ => by rw [Fintype.sum_prod_type, Fin.sum_univ_one, Fin.sum_univ_one])
  have hsum1 : ∀ f : Fin 1 × Fin 1 → ℝ, ∑ a, f a = f ((0 : Fin 1), (0 : Fin 1)) := by
    intro f
    rw [Fintype.sum_prod_type, Fin.sum_univ_one, Fin.sum_univ_one]
  have h14 : ‖(1 / 4 : ℂ)‖ = 1 / 4 := by
    rw [show (1 / 4 : ℂ) = ((1 / 4 : ℝ) : ℂ) by push_cast; ring, Complex.norm_real]
    norm_num
  have hU : AdmissibleDilationAt (%s) ((0 : Fin 1), (0 : Fin 1)) (Matrix.of fun p q : (Fin 4 × Fin 4) × (Fin 1 × Fin 1) => %s p.1 q.1) := by
    refine ⟨?_, ?_⟩
    · rw [Matrix.mem_unitaryGroup_iff', Matrix.star_eq_conjTranspose]
      ext ⟨p, a⟩ ⟨q, b⟩
      rw [Matrix.mul_apply, Matrix.one_apply, hsum]
      simp only [Matrix.conjTranspose_apply, Matrix.of_apply]
      have hab : a = b := Subsingleton.elim a b
      subst hab
      simp only [Prod.mk.injEq, and_true]
      rcases p with ⟨p1, p2⟩
      fin_cases p1 <;> fin_cases p2
%s
    · intro i j
      rw [hsum1, hΓ₀]
      simp only [Matrix.of_apply]
      rw [norm_mul, norm_mul, hFn, hTn, h14]
      norm_num
  have hG : %s = FibreGram ((0 : Fin 1), (0 : Fin 1)) (Matrix.of fun p q : (Fin 4 × Fin 4) × (Fin 1 × Fin 1) => %s p.1 q.1) := by
    funext i
    ext j k
    rw [fibreGram_apply, Fintype.sum_prod_type, Fin.sum_univ_one, Fin.sum_univ_one]
    simp only [Matrix.of_apply]
  refine ⟨?_, ?_⟩
  · rw [hG]
    exact sh1_necessity hU
  · intro X Y h
    have hq := (a34_shared_feature_ext _ _).1 h
    have key : mixedTriple %s %s * mixedTriple %s %s = mixedTriple %s %s * mixedTriple %s %s := by
      rw [← hq, ← hq, ← hq, ← hq, a34_shared_fact, a34_shared_fact, a34_shared_fact, a34_shared_fact]
      dsimp only
      ring
    simp [mixedTriple, Complex.star_def, Complex.conj_I, Complex.ext_iff] at key
    norm_num at key''' % (F4IV, F4TV, GP, HDEF, '\n'.join('      · exact a34_shared_unit_col_%d_%d q' % (a, b) for a in range(4) for b in range(4)), GOF(HDEF), HDEF, GOF(HDEF), Q11, GOF(HDEF), Q22, GOF(HDEF), Q12, GOF(HDEF), Q21))

thm('a34_shared_product_core', HEADLINE + ' ∃ X Y : %s, %s X ∧ %s Y ∧ featureVec %s = featureVec %s' % (TUP, RG, RG, PRODC('X', 'Y'), GOF(H0DEF)),
'''  intro Γ₀ hΓ₀
  refine ⟨%s, %s, (iso2_classes_single Γ₀ hΓ₀).2 _ _ Complex.I a33_shared_unit_I, (iso2_classes_single Γ₀ hΓ₀).2 _ _ Complex.I a33_shared_unit_I, ?_⟩
  congr 1
  funext i
  ext j k
  simp only [Matrix.of_apply, Matrix.submatrix_apply, Equiv.Perm.coe_one, id_eq, fibreGram_apply, Fin.sum_univ_one, star_mul', Complex.star_def, map_div₀, map_one, map_ofNat]
  ring''' % (TUPP(0, 'Complex.I'), TUPP(0, 'Complex.I')))

thm('a34_shared_bits_core', HEADLINE + ' featureVec %s = featureVec %s ∧ featureVec %s ≠ featureVec %s' % (PRODC(TUPC('0', '1'), TUPC('3', 'Complex.I')), PRODC(TUPC('4', '1'), TUPC('3', 'Complex.I')), PRODC(TUPC('0', '1'), TUPC('3', 'Complex.I')), PRODC(TUPC('0', '1'), TUPC('3', '(star Complex.I)'))),
'''  intro Γ₀ hΓ₀
  constructor
  · have hv := a34_shared_vertex_core 0 4 (by decide)
    rw [if_pos (show %s by decide), if_pos (show %s by decide)] at hv
    exact a34_shared_prod_congr %s %s %s %s hv rfl
  · intro h
    have hsI : star (star Complex.I) * star Complex.I = 1 := by
      rw [star_star, mul_comm]
      exact a33_shared_unit_I
    obtain ⟨-, h2⟩ := a34_shared_pair_core Γ₀ hΓ₀ _ _ _ _ (a34_shared_tup_real Γ₀ hΓ₀ 0 1 (by simp)) (a34_shared_tup_real Γ₀ hΓ₀ 3 Complex.I a33_shared_unit_I) (a34_shared_tup_real Γ₀ hΓ₀ 0 1 (by simp)) (a34_shared_tup_real Γ₀ hΓ₀ 3 (star Complex.I) hsI) h
    have := a34_shared_pt_inj 3 Complex.I (star Complex.I) a33_shared_unit_I hsI h2
    rw [Complex.star_def, Complex.conj_I] at this
    have h0 := congrArg Complex.im this
    norm_num at h0''' % (MUCOND('0', '4'), MUCOND('4', '0'), TUPC('0', '1'), TUPC('4', '1'), TUPC('3', 'Complex.I'), TUPC('3', 'Complex.I')))

# the nine N tables for circle 0 against itself, from act 33's cross summand with the identity permutations
cross = open(os.path.join(S, 'cross.txt'), encoding='utf-8').read()
i = cross.index('∑ kl ∈ ')
summand = cross[cross.index('((((Finset.univ.filter', i):]
# the summand is `((((filter).sum (...)) : ℤ) : ℝ) * (re part)` ; take the integer part
j = summand.index(' : ℤ) : ℝ) * (((starRingEnd ℂ)')
intpart = summand[:j] + ' : ℤ)'   # '((((Finset...).sum (...) : ℤ)'  -> we want '(((filter).sum (...)) : ℤ)'
intpart = intpart[2:]  # drop two leading parens so it reads `((Finset...).sum ... : ℤ)` as act 33's N lemmas do
NAMES = {-1: 'm', 0: '0', 1: '1'}
NVAL = {(-1, -1): 768, (0, 0): 2560, (1, 1): 768}
for k in (-1, 0, 1):
    for l in (-1, 0, 1):
        body = intpart.replace("(a' p", '(%s p' % ONE).replace("(b' p", '(%s p' % ONE).replace('(a p', '(%s p' % ONE).replace('(b p', '(%s p' % ONE).replace('= kl)', '= ((%d, %d) : ℤ × ℤ))' % (k, l))
        thm('a34_shared_N_0_0_%s_%s' % (NAMES[k], NAMES[l]), body + ' = %d' % NVAL.get((k, l), 0), '  decide +kernel')

INS = 'Finset.sum_insert (by decide), ' * 8 + 'Finset.sum_singleton'
NS = ', '.join('a34_shared_N_0_0_%s_%s' % (NAMES[k], NAMES[l]) for k in (-1, 0, 1) for l in (-1, 0, 1))
thm('a34_shared_square_core', HEADLINE + ' dist (featureVec %s) (featureVec %s) ≠ dist (featureVec %s) (featureVec %s)' % (PRODC(TUPC('0', '(Complex.I * Complex.I)'), TUPC('3', 'Complex.I')), PRODC(TUPC('0', '1'), TUPC('3', 'Complex.I')), PRODC(TUPC('0', 'Complex.I'), TUPC('3', 'Complex.I')), PRODC(TUPC('0', '1'), TUPC('3', 'Complex.I'))),
'''  intro Γ₀ hΓ₀
  rw [(a34_shared_fibre_core Γ₀ hΓ₀ %s %s %s (a34_shared_tup_real Γ₀ hΓ₀ 3 Complex.I a33_shared_unit_I)).1, (a34_shared_fibre_core Γ₀ hΓ₀ %s %s %s (a34_shared_tup_real Γ₀ hΓ₀ 3 Complex.I a33_shared_unit_I)).1]
  simp only [%s]
  intro h
  have hI : star Complex.I * Complex.I = 1 := a33_shared_unit_I
  have hII : star (Complex.I * Complex.I) * (Complex.I * Complex.I) = 1 := by
    rw [Complex.I_mul_I]; simp
  have h1u : star (1 : ℂ) * 1 = 1 := by simp
  have h1 := a33_shared_cross %s %s %s %s (Complex.I * Complex.I) 1 hII h1u
  have h2 := a33_shared_cross %s %s %s %s Complex.I 1 hI h1u
  have hsq := congrArg (fun x : ℝ => x ^ 2) h
  try simp only [] at hsq
  rw [h1, h2] at hsq
  rw [%s] at hsq
  rw [%s] at hsq
  rw [%s] at hsq
  simp [Complex.star_def, Complex.conj_I, Complex.I_mul_I] at hsq
  norm_num at hsq''' % (TUPC('0', '(Complex.I * Complex.I)'), TUPC('0', '1'), TUPC('3', 'Complex.I'), TUPC('0', 'Complex.I'), TUPC('0', '1'), TUPC('3', 'Complex.I'), RS, ONE, ONE, ONE, ONE, ONE, ONE, ONE, ONE, INS, INS, NS))

# ---------------------------------------------------------------- the frozen statements
def frozen(name, key, core, count=False):
    if count:
        thm(name, PR[key], '  decide +kernel')
    else:
        thm(name, PR[key], '  intro Γ₀ hΓ₀\n  dsimp only\n  exact %s Γ₀ hΓ₀' % core)

thm('a34_shared_factor', PR['FACT'], '  intro Γ₀ hΓ₀\n  dsimp only\n  exact a34_shared_fact')
thm('a34_shared_inner', PR['INNER'], '  intro Γ₀ hΓ₀\n  dsimp only\n  exact a34_shared_inner_core')
frozen('a34_shared_cover', 'COVER', 'a34_shared_cover_core')
frozen('a34_shared_point', 'POINT', 'a34_shared_point_core')
frozen('a34_shared_circle_left', 'CIRC_L', 'a34_shared_circle_left_core')
frozen('a34_shared_circle_right', 'CIRC_R', 'a34_shared_circle_right_core')
frozen('a34_shared_apart', 'APART', 'a34_shared_apart_tori_core')
frozen('a34_shared_count', 'COUNT', None, count=True)
frozen('a34_shared_tensor', 'TENSOR', 'a34_shared_tensor_core')
frozen('a34_shared_swap', 'SWAP', 'a34_shared_swap_core')
frozen('a34_shared_fibre', 'FIBRE', 'a34_shared_fibre_core')
frozen('a34_shared_pairing', 'PAIR', 'a34_shared_pair_core')
frozen('a34_shared_local', 'LOCAL', 'a34_shared_local_core')
thm('a34_c_normal_form', PR['NFORM'],
'''  intro Γ₀ hΓ₀
  dsimp only
  intro F Φ₁ Φ₂ hF hfac
  obtain ⟨f, g, hf, hg, hfg⟩ := a34_shared_local_core Γ₀ hΓ₀ F Φ₁ Φ₂ hF hfac
  have hc := a33_classified Γ₀ hΓ₀
  dsimp only at hc
  exact ⟨f, g, hf, hg, hfg, hc.1 f hf, hc.1 g hg⟩''')
frozen('a34_control_proper', 'PROPER', 'a34_shared_proper_core')
frozen('a34_control_product', 'PRODUCT', 'a34_shared_product_core')
frozen('a34_control_bits', 'BITS', 'a34_shared_bits_core')
frozen('a34_control_square', 'SQUARE', 'a34_shared_square_core')

src = ''.join(out)

# ---------------------------------------------------------------- the verdict and the corollary
verdict = '''theorem a34_stratified :
    %s := by
  intro Γ₀ hΓ₀
  dsimp only
  exact ⟨⟨a34_shared_cover_core Γ₀ hΓ₀, a34_shared_point_core Γ₀ hΓ₀, a34_shared_circle_left_core Γ₀ hΓ₀, a34_shared_circle_right_core Γ₀ hΓ₀, a34_shared_apart_tori_core Γ₀ hΓ₀⟩, ⟨a34_shared_tensor_core Γ₀ hΓ₀, a34_shared_swap_core Γ₀ hΓ₀⟩, a34_shared_local_core Γ₀ hΓ₀⟩
#print axioms a34_stratified

theorem a34_c_exclusive :
    (%s) → ¬ (%s) := by
  intro hN hR
  have hN' := hN _ rfl
  have hR' := hR _ rfl
  dsimp only at hN' hR'
  rcases hN' with h | h | h
  · exact h hR'.1
  · exact h hR'.2.1
  · exact h hR'.2.2
#print axioms a34_c_exclusive

''' % (PR['P_R'], PR['P_N'], PR['P_R'])

DOC = P['DOC']
header = P['IMPORT'] + '\n' + DOC + '\nnamespace OIBridge\nnamespace ProductStratum\n\n' + P['OPEN'] + '\n'
module = header + src + verdict + 'end ProductStratum\nend OIBridge\n'
open(sys.argv[1], 'w', encoding='utf-8').write(module)
print('theorems', len(re.findall(r'(?m)^theorem ', module)), 'lines', module.count('\n'))
