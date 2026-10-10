"""A36 builder: the frozen propositions from shared components (single source).
Writes props36.json and elab36.lean. controls.py and the preregistration embed the same texts."""
import json, os, sys
S = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(S, '..', 'a34')); sys.path.insert(0, os.path.join(S, '..', 'a35'))
import build35 as B35
import build34 as B34

E16, TUP, RG = B34.E16, B34.TUP, B34.RG
M4, M16, TUP16, RG16 = B35.M4, B35.M16, B35.TUP16, B35.RG16
M2 = 'Matrix (Fin 2) (Fin 2) ℂ'; M8 = 'Matrix (Fin 8) (Fin 8) ℂ'

HEAD35 = B35.HEAD          # act 34's head + act 35's objects, verbatim
HEAD36 = (
 '  let dg : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2\n'
 '  let dgT : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2\n'
 '  let flg : ∀ {α : Type} [Fintype α] [DecidableEq α], Matrix α α ℂ → Prop := fun {α : Type} [Fintype α] [DecidableEq α] (X : Matrix α α ℂ) => X ∈ Matrix.unitaryGroup α ℂ ∧ ∀ a c, ‖X a c‖ ^ 2 = 1 / (Fintype.card α : ℝ)\n'
 '  let r28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2))\n'
 '  let c28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))\n'
 '  let dita28 : ' + M2 + ' → (Fin 2 → ' + M8 + ') → (Fin 2 → Fin 8 → ℂ) → ' + M16 + ' := fun X Y D => Matrix.of fun i j => dg X Y D (r28 i) (c28 j)\n'
 '  let r82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (@finProdFinEquiv 4 2 (i.1, @Fin.divNat 2 2 i.2), @Fin.modNat 2 2 i.2)\n'
 '  let c82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (@finProdFinEquiv 4 2 (j.1, @Fin.divNat 2 2 j.2), @Fin.modNat 2 2 j.2)\n'
 '  let dita82 : ' + M8 + ' → (Fin 8 → ' + M2 + ') → (Fin 8 → Fin 2 → ℂ) → ' + M16 + ' := fun X Y D => Matrix.of fun i j => dg X Y D (r82 i) (c82 j)\n'
 '  let z : ℂ := 3 / 5 + (4 / 5) * Complex.I\n'
 '  let w : ℂ := 5 / 13 + (12 / 13) * Complex.I\n'
 '  let SIG : ' + M16 + ' := Matrix.of fun i j => F4 z i.1 j.1 * F4 w i.2 j.2\n'
 '  let Wt : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => if i.1.val % 2 = 0 ∧ j.1.val % 2 = 0 then (if i.2 = 1 then 1 else 0) + (if j.2 = 1 then 1 else 0) else 0\n'
 '  let Pu : ℂ → ' + M16 + ' := fun u => Matrix.of fun i j => SIG i j * u ^ Wt i j\n'
 '  let u₆₀ : ℂ := 3599 / 3601 + (120 / 3601) * Complex.I\n'
 '  let P : ' + M16 + ' := Pu u₆₀\n'
)
HEAD = HEAD35 + HEAD36

GEN = '∀ {α β : Type} [Fintype α] [DecidableEq α] [Fintype β] [DecidableEq β] (eR eC : α × β ≃ Fin 4 × Fin 4) (X : Matrix α α ℂ) (Y : α → Matrix β β ℂ) (D : α → β → ℂ), flg X → (∀ c, flg (Y c)) → (∀ c b, ‖D c b‖ = 1) →\n'
HULLG = (GEN + '    (dg X Y D).submatrix eR.symm eC.symm ∈ Matrix.unitaryGroup (Fin 4 × Fin 4) ℂ ∧ (∀ i j, ‖(dg X Y D).submatrix eR.symm eC.symm i j‖ = 1 / 4) ∧ ' + RG16 + ' (gram ((dg X Y D).submatrix eR.symm eC.symm))')
HULLGT = (GEN.replace('(D : α → β → ℂ)', '(E : α → β → ℂ)').replace('‖D c b‖ = 1', '‖E c d‖ = 1').replace('(∀ c b,', '(∀ c d,') +
          '    (dgT X Y E).submatrix eR.symm eC.symm ∈ Matrix.unitaryGroup (Fin 4 × Fin 4) ℂ ∧ (∀ i j, ‖(dgT X Y E).submatrix eR.symm eC.symm i j‖ = 1 / 4) ∧ ' + RG16 + ' (gram ((dgT X Y E).submatrix eR.symm eC.symm))')
HULL28 = ('∀ (X : ' + M2 + ') (Y : Fin 2 → ' + M8 + ') (D : Fin 2 → Fin 8 → ℂ), flg X → (∀ c, flg (Y c)) → (∀ c b, ‖D c b‖ = 1) →\n'
          '    dita28 X Y D ∈ Matrix.unitaryGroup (Fin 4 × Fin 4) ℂ ∧ (∀ i j, ‖dita28 X Y D i j‖ = 1 / 4) ∧ ' + RG16 + ' (gram (dita28 X Y D))')
HULL82 = ('∀ (X : ' + M8 + ') (Y : Fin 8 → ' + M2 + ') (D : Fin 8 → Fin 2 → ℂ), flg X → (∀ c, flg (Y c)) → (∀ c b, ‖D c b‖ = 1) →\n'
          '    dita82 X Y D ∈ Matrix.unitaryGroup (Fin 4 × Fin 4) ℂ ∧ (∀ i j, ‖dita82 X Y D i j‖ = 1 / 4) ∧ ' + RG16 + ' (gram (dita82 X Y D))')
LINE = ('∀ u : ℂ, star u * u = 1 →\n'
        '    (∃ (X : ' + M2 + ') (Y : Fin 2 → ' + M8 + ') (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Pu u = dita28 X Y D)\n'
        '    ∧ ' + RG16 + ' (gram (Pu u)) ∧ featureVec (gram (Pu u)) ∈ N')
POINT = ('star u₆₀ * u₆₀ = 1 ∧ ' + RG16 + ' (gram P) ∧ featureVec (gram P) ∈ N ∧ featureVec (gram P) ∉ S\n'
         '  ∧ gram P (0, 0) (0, 0) (1, 0) * gram P (0, 1) (1, 0) (0, 0) = u₆₀ / 256')
ONE = 'Pu 1 = SIG ∧ featureVec (gram SIG) ∈ S'

PKG = '(' + HULLG + ')\n  ∧ (' + HULLGT + ')\n  ∧ (' + LINE + ')\n  ∧ (' + POINT + ')'
P_R = HEAD + '  ' + PKG
P_N = HEAD + '  ¬ (' + HULLG + ')\n  ∨ ¬ (' + HULLGT + ')\n  ∨ ¬ (' + LINE + ')\n  ∨ ¬ (' + POINT + ')'
COMPONENTS = {'HEAD': HEAD, 'HEAD35': HEAD35, 'HEAD36': HEAD36, 'PKG': PKG, 'HULLG': HULLG, 'HULLGT': HULLGT, 'HULL28': HULL28,
              'HULL82': HULL82, 'LINE': LINE, 'POINT': POINT, 'ONE': ONE}
PROPS = {'P_R': P_R, 'P_N': P_N, 'HULLG': HEAD + '  ' + HULLG, 'HULLGT': HEAD + '  ' + HULLGT, 'HULL28': HEAD + '  ' + HULL28,
         'HULL82': HEAD + '  ' + HULL82, 'LINE': HEAD + '  ' + LINE, 'POINT': HEAD + '  ' + POINT, 'ONE': HEAD + '  ' + ONE}
THEOREMS = [
 ('A36-HIERARCHY', 'a36_hierarchy', 'P_R'),
 ('A36-NOT-HIERARCHY', 'a36_not_hierarchy', 'P_N'),
 ('A36-1', 'a36_shared_hull_g', 'HULLG'),
 ('A36-1', 'a36_shared_hull_gt', 'HULLGT'),
 ('A36-1 instance', 'a36_control_hull28', 'HULL28'),
 ('A36-1 instance', 'a36_control_hull82', 'HULL82'),
 ('A36-2', 'a36_shared_line', 'LINE'),
 ('A36-3', 'a36_shared_point', 'POINT'),
 ('control', 'a36_control_stratum', 'ONE'),
]
COROLLARY = ('a36_c_exclusive', ['P_N'], 'P_R')
OPEN = B35.OPEN.rstrip('\n') + ' DitaHull\n'
IMPORT = 'import OIBridge.DitaHull\n'
DOC = '''/-!
# Act 36 — the Diţă factorization hierarchy at the product-embedded stratum

At act 29's product configuration, act 35's column and row Diţă constructions with `4 × 4` factors
give two fourteen-dimensional hulls through every stratum point. This module states Diţă's
construction over any factorization of the sixteen-point carrier — an outer factor on `α`, inner
factors on `β`, a twist, and any bijections of `α × β` with the product carrier for rows and for
columns — realizable for flat unitary factors and unit twists; its `2 × 8` and `8 × 2` instances;
an exact one-parameter family through the certified rational stratum point `F₄(z) ⊗ F₄(w)`,
`z = (3+4i)/5`, `w = (5+12i)/13`, whose every member is a `2 × 8` Diţă matrix; and the named point
`P = SIG ∘ u^W`, `u = (60+i)/(60−i)`, realizable, off the stratum by an exact cross-ratio value
`u/256`. The exact-computation layer shows that `P` admits no `4 × 4` Diţă factorization of either
orientation under any relabelling: the `4 × 4` hierarchy is locally insufficient at the stratum,
and the first escaping family belongs to the `2 × 8` construction.

The module carries no definition. Every theorem prints its axioms.
-/
'''

def elab_module():
    parts = [IMPORT, '\n', DOC, '\nnamespace OIBridge\nnamespace DitaHierarchy\n\n', OPEN, '\n']
    for role, nm, key in THEOREMS:
        parts.append('-- %s, `%s`\n#check (%s)\n\n' % (role, nm, PROPS[key]))
    parts.append('-- corollary, `a36_c_exclusive`\n#check ((%s) → ¬ (%s))\n\n' % (PROPS['P_N'], PROPS['P_R']))
    parts.append('end DitaHierarchy\nend OIBridge\n')
    return ''.join(parts)

if __name__ == '__main__':
    json.dump({'COMPONENTS': COMPONENTS, 'PROPS': PROPS, 'THEOREMS': THEOREMS, 'COROLLARY': COROLLARY,
               'OPEN': OPEN, 'IMPORT': IMPORT, 'DOC': DOC}, open(os.path.join(S, 'props36.json'), 'w'), ensure_ascii=False, indent=1)
    open(os.path.join(S, 'elab36.lean'), 'w', encoding='utf-8').write(elab_module())
    print('props', len(PROPS), 'theorems', len(THEOREMS), 'P_R chars', len(P_R))
