"""A34 builder: the frozen propositions from shared components (single source).
Writes: props34.json (COMPONENTS, PROPS, THEOREMS), elab34.lean (the #check module for the disposable
branch), and prints nothing else. controls.py and the preregistration embed the same texts."""
import json, os
S = os.path.dirname(os.path.abspath(__file__))

E4 = 'EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4))'
E16 = 'EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))'
TUP = 'Fin 4 → Matrix (Fin 4) (Fin 4) ℂ'
RG = 'RealizableGram (Fin 1) Γ₀'
RTAB = '![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]'
F4 = '!![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z]'
TW = '(if j.1.val % 2 = 0 then Complex.I else -Complex.I)'
F4I = '!![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1; 1, -Complex.I, -1, Complex.I]'
F4T = '!![1, 1, 1, 1; 1, %s, -1, -%s; 1, -1, 1, -1; 1, -%s, -1, %s]' % (TW, TW, TW, TW)

HEAD = (
 '∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →\n'
 '  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ' + RTAB + '\n'
 '  let tup : Fin 9 → ℂ → (' + TUP + ') := fun r z i =>\n'
 '    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>\n'
 '        (1 / 2 : ℂ) * ' + F4 + ' p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2\n'
 '  let pt : Fin 9 → ℂ → ' + E4 + ' := fun r z => featureVec (tup r z)\n'
 '  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]\n'
 '  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]\n'
 '  let prod : (' + TUP + ') → (' + TUP + ') → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2\n'
 '  let S : Set (' + E16 + ') := {x | ∃ X Y : ' + TUP + ', ' + RG + ' X ∧ ' + RG + ' Y ∧ featureVec (prod X Y) = x}\n'
 '  let tor : Fin 9 → Fin 9 → Set (' + E16 + ') := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}\n'
 '  let adj : Fin 9 → Fin 9 → Prop := fun r r\' => r ≠ r\' ∧ (v₁ r = v₁ r\' ∨ v₁ r = v₂ r\' ∨ v₂ r = v₁ r\' ∨ v₂ r = v₂ r\')\n'
 '  let μ : Fin 9 → Fin 9 → ℂ := fun r r\' => if v₁ r = v₁ r\' ∨ v₁ r = v₂ r\' then (1 : ℂ) else -1\n'
)
FIN = (
 '  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]\n'
 '  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]\n'
)
ADJ = "(q.1.1 ≠ q.2.1 ∧ (v₁ q.1.1 = v₁ q.2.1 ∨ v₁ q.1.1 = v₂ q.2.1 ∨ v₂ q.1.1 = v₁ q.2.1 ∨ v₂ q.1.1 = v₂ q.2.1))"
ADJ2 = "(q.1.2 ≠ q.2.2 ∧ (v₁ q.1.2 = v₁ q.2.2 ∨ v₁ q.1.2 = v₂ q.2.2 ∨ v₂ q.1.2 = v₁ q.2.2 ∨ v₂ q.1.2 = v₂ q.2.2))"
IDX1 = '((p.1.1.1, p.1.2.1.1, p.1.2.2.1), (p.2.1.1, p.2.2.1.1, p.2.2.2.1))'
IDX2 = '((p.1.1.2, p.1.2.1.2, p.1.2.2.2), (p.2.1.2, p.2.2.1.2, p.2.2.2.2))'
SURJ4 = 'IsSurjIsometryOn (normalizedSet Γ₀)'
NF = ("(∀ r : Fin 9, ∃ s : Fin 9, (νε.1 (v₁ r) = v₁ s ∧ νε.1 (v₂ r) = v₂ s) ∨ (νε.1 (v₁ r) = v₂ s ∧ νε.1 (v₂ r) = v₁ s))\n"
      "    ∧ (∀ r s : Fin 9, νε.1 (v₁ r) = v₁ s → νε.1 (v₂ r) = v₂ s → ∀ z : ℂ, star z * z = 1 →\n"
      "        %s (pt r z) = pt s (if νε.2 r then z else star z))\n"
      "    ∧ (∀ r s : Fin 9, νε.1 (v₁ r) = v₂ s → νε.1 (v₂ r) = v₁ s → ∀ z : ℂ, star z * z = 1 →\n"
      "        %s (pt r z) = pt s (-(if νε.2 r then z else star z)))")
GDEF = 'fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => star (H i j) * H i k'

# ---- bodies (what follows the head)
FACT = ('∀ (X Y : ' + TUP + ') (p : ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4))),\n'
        '    mixedTriple (prod X Y) p = mixedTriple X ' + IDX1 + ' * mixedTriple Y ' + IDX2)
INNER = ('∀ (X Y X\' Y\' : ' + TUP + '),\n'
         '    inner ℂ (featureVec (prod X Y)) (featureVec (prod X\' Y\')) = inner ℂ (featureVec X) (featureVec X\') * inner ℂ (featureVec Y) (featureVec Y\')')
FIBRE = ('∀ (X X\' Y : ' + TUP + '), ' + RG + ' Y →\n'
         '    dist (featureVec (prod X Y)) (featureVec (prod X\' Y)) = dist (featureVec X) (featureVec X\')\n'
         '    ∧ dist (featureVec (prod Y X)) (featureVec (prod Y X\')) = dist (featureVec X) (featureVec X\')')
PAIR = ('∀ (X Y X\' Y\' : ' + TUP + '), ' + RG + ' X → ' + RG + ' Y → ' + RG + ' X\' → ' + RG + ' Y\' →\n'
        '    featureVec (prod X Y) = featureVec (prod X\' Y\') → featureVec X = featureVec X\' ∧ featureVec Y = featureVec Y\'')
COVER = 'S = ⋃ (r : Fin 9) (s : Fin 9), tor r s'
POINT = ('∀ r r\' s s\' : Fin 9, adj r r\' → adj s s\' →\n'
         '    tor r s ∩ tor r\' s\' = {featureVec (prod (tup r (μ r r\')) (tup s (μ s s\')))}')
CIRC_L = ('∀ r s s\' : Fin 9, adj s s\' →\n'
          '    tor r s ∩ tor r s\' = {x | ∃ z : ℂ, star z * z = 1 ∧ x = featureVec (prod (tup r z) (tup s (μ s s\')))}')
CIRC_R = ('∀ r r\' s : Fin 9, adj r r\' →\n'
          '    tor r s ∩ tor r\' s = {x | ∃ w : ℂ, star w * w = 1 ∧ x = featureVec (prod (tup r (μ r r\')) (tup s w))}')
APART = ('∀ r r\' s s\' : Fin 9, (r ≠ r\' ∧ ¬ adj r r\') ∨ (s ≠ s\' ∧ ¬ adj s s\') →\n'
         '    tor r s ∩ tor r\' s\' = ∅')
COUNT = ('(Finset.univ.filter (fun q : (Fin 9 × Fin 9) × (Fin 9 × Fin 9) => ' + ADJ + ' ∧ ' + ADJ2 + ')).card = 1296\n'
         '  ∧ (Finset.univ.filter (fun q : (Fin 9 × Fin 9) × (Fin 9 × Fin 9) => (q.1.1 = q.2.1 ∧ ' + ADJ2 + ') ∨ (q.1.2 = q.2.2 ∧ ' + ADJ + '))).card = 648')
TENSOR = ('∀ f g : ' + E4 + ' → ' + E4 + ', ' + SURJ4 + ' f → ' + SURJ4 + ' g →\n'
          '    ∃ F : ' + E16 + ' → ' + E16 + ', IsSurjIsometryOn S F ∧\n'
          '      ∀ X Y X\' Y\' : ' + TUP + ', ' + RG + ' X → ' + RG + ' Y → ' + RG + ' X\' → ' + RG + ' Y\' →\n'
          '        f (featureVec X) = featureVec X\' → g (featureVec Y) = featureVec Y\' → F (featureVec (prod X Y)) = featureVec (prod X\' Y\')')
SWAP = ('∃ F : ' + E16 + ' → ' + E16 + ', IsSurjIsometryOn S F ∧\n'
        '    ∀ X Y : ' + TUP + ', ' + RG + ' X → ' + RG + ' Y → F (featureVec (prod X Y)) = featureVec (prod Y X)')
LOCAL_HYP = ('∀ (F : ' + E16 + ' → ' + E16 + ') (Φ₁ Φ₂ : (' + TUP + ') → (' + TUP + ')), IsSurjIsometryOn S F →\n'
             '    (∀ X Y : ' + TUP + ', ' + RG + ' X → ' + RG + ' Y → ' + RG + ' (Φ₁ X) ∧ ' + RG + ' (Φ₂ Y) ∧ F (featureVec (prod X Y)) = featureVec (prod (Φ₁ X) (Φ₂ Y))) →\n')
LOCAL_CONCL = ('∃ f g : ' + E4 + ' → ' + E4 + ', ' + SURJ4 + ' f ∧ ' + SURJ4 + ' g ∧\n'
               '      ∀ X Y : ' + TUP + ', ' + RG + ' X → ' + RG + ' Y → featureVec (Φ₁ X) = f (featureVec X) ∧ featureVec (Φ₂ Y) = g (featureVec Y)')
LOCAL = LOCAL_HYP + '    ' + LOCAL_CONCL
NFORM = (LOCAL_HYP + '    ∃ f g : ' + E4 + ' → ' + E4 + ', ' + SURJ4 + ' f ∧ ' + SURJ4 + ' g ∧\n'
         '      (∀ X Y : ' + TUP + ', ' + RG + ' X → ' + RG + ' Y → featureVec (Φ₁ X) = f (featureVec X) ∧ featureVec (Φ₂ Y) = g (featureVec Y))\n'
         '      ∧ (∃! νε : Equiv.Perm (Fin 6) × (Fin 9 → Bool),\n    ' + NF % ('f', 'f') + ')\n'
         '      ∧ (∃! νε : Equiv.Perm (Fin 6) × (Fin 9 → Bool),\n    ' + NF % ('g', 'g') + ')')
PROPER = ('let H : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Matrix.of fun i j => (1 / 4 : ℂ) * ' + F4I + ' i.1 j.1 * ' + F4T + ' i.2 j.2\n'
          '  RealizableGram (Fin 1 × Fin 1) (Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2) (' + GDEF + ')\n'
          '  ∧ ∀ X Y : ' + TUP + ', featureVec (prod X Y) ≠ featureVec (' + GDEF + ')')
PRODUCT = ('let H : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Matrix.of fun i j => (1 / 4 : ℂ) * ' + F4I + ' i.1 j.1 * ' + F4I + ' i.2 j.2\n'
           '  ∃ X Y : ' + TUP + ', ' + RG + ' X ∧ ' + RG + ' Y ∧ featureVec (prod X Y) = featureVec (' + GDEF + ')')
BITS = ('featureVec (prod (tup 0 1) (tup 3 Complex.I)) = featureVec (prod (tup 4 1) (tup 3 Complex.I))\n'
        '  ∧ featureVec (prod (tup 0 1) (tup 3 Complex.I)) ≠ featureVec (prod (tup 0 1) (tup 3 (star Complex.I)))')
SQUARE = ('dist (featureVec (prod (tup 0 (Complex.I * Complex.I)) (tup 3 Complex.I))) (featureVec (prod (tup 0 1) (tup 3 Complex.I)))\n'
          '    ≠ dist (featureVec (prod (tup 0 Complex.I) (tup 3 Complex.I))) (featureVec (prod (tup 0 1) (tup 3 Complex.I)))')

INC = '(' + COVER + ')\n  ∧ (' + POINT + ')\n  ∧ (' + CIRC_L + ')\n  ∧ (' + CIRC_R + ')\n  ∧ (' + APART + ')'
ACT = '(' + TENSOR + ')\n  ∧ (' + SWAP + ')'
P_R = HEAD + '  (' + INC + ')\n  ∧ (' + ACT + ')\n  ∧ (' + LOCAL + ')'
P_N = HEAD + '  ¬ (' + INC + ')\n  ∨ ¬ (' + ACT + ')\n  ∨ ¬ (' + LOCAL + ')'

COMPONENTS = {'HEAD': HEAD, 'FIN': FIN, 'INC': INC, 'ACT': ACT, 'LOCAL': LOCAL, 'COVER': COVER, 'POINT': POINT,
              'CIRC_L': CIRC_L, 'CIRC_R': CIRC_R, 'APART': APART, 'TENSOR': TENSOR, 'SWAP': SWAP,
              'LOCAL_HYP': LOCAL_HYP, 'LOCAL_CONCL': LOCAL_CONCL, 'NF_F': NF % ('f', 'f'), 'NF_G': NF % ('g', 'g'),
              'GDEF': GDEF, 'F4I': F4I, 'F4T': F4T, 'ADJ': ADJ, 'ADJ2': ADJ2}
PROPS = {'P_R': P_R, 'P_N': P_N,
         'FACT': HEAD + '  ' + FACT, 'INNER': HEAD + '  ' + INNER, 'FIBRE': HEAD + '  ' + FIBRE, 'PAIR': HEAD + '  ' + PAIR,
         'COVER': HEAD + '  ' + COVER, 'POINT': HEAD + '  ' + POINT, 'CIRC_L': HEAD + '  ' + CIRC_L, 'CIRC_R': HEAD + '  ' + CIRC_R,
         'APART': HEAD + '  ' + APART, 'COUNT': FIN + '  ' + COUNT,
         'TENSOR': HEAD + '  ' + TENSOR, 'SWAP': HEAD + '  ' + SWAP, 'LOCAL': HEAD + '  ' + LOCAL, 'NFORM': HEAD + '  ' + NFORM,
         'PROPER': HEAD + '  ' + PROPER, 'PRODUCT': HEAD + '  ' + PRODUCT, 'BITS': HEAD + '  ' + BITS, 'SQUARE': HEAD + '  ' + SQUARE}
THEOREMS = [
 ('A34-STRATIFIED', 'a34_stratified', 'P_R'),
 ('A34-NOT-STRATIFIED', 'a34_not_stratified', 'P_N'),
 ('A34-1', 'a34_shared_factor', 'FACT'),
 ('A34-1', 'a34_shared_inner', 'INNER'),
 ('A34-2', 'a34_shared_cover', 'COVER'),
 ('A34-2', 'a34_shared_point', 'POINT'),
 ('A34-2', 'a34_shared_circle_left', 'CIRC_L'),
 ('A34-2', 'a34_shared_circle_right', 'CIRC_R'),
 ('A34-2', 'a34_shared_apart', 'APART'),
 ('A34-2', 'a34_shared_count', 'COUNT'),
 ('A34-3', 'a34_shared_tensor', 'TENSOR'),
 ('A34-3', 'a34_shared_swap', 'SWAP'),
 ('A34-5', 'a34_shared_fibre', 'FIBRE'),
 ('A34-5', 'a34_shared_pairing', 'PAIR'),
 ('A34-5', 'a34_shared_local', 'LOCAL'),
 ('A34-5 corollary', 'a34_c_normal_form', 'NFORM'),
 ('A34-4', 'a34_control_proper', 'PROPER'),
 ('control', 'a34_control_product', 'PRODUCT'),
 ('control', 'a34_control_bits', 'BITS'),
 ('control', 'a34_control_square', 'SQUARE'),
]
COROLLARY = ('a34_c_exclusive', ['P_N'], 'P_R')

OPEN = ("open Matrix CoherentLiftGauge DilationChoice TwoSidedGauge GramTrajectorySelection\n"
        "  IntermediateCrossTimeStructure RepresentativeNaturality OrbitLawRigidityTwisted\n"
        "  OrbitLawNaturalityFactorization OrbitLawGaps OrbitGeometrySelector OrbitGeometryIsometries\n"
        "  OrbitGeometryRigidity OrbitIsometryGroup\n")
IMPORT = 'import OIBridge.OrbitIsometryGroup\n'
DOC = '''/-!
# Act 34 — the product-embedded stratum: product geometry, incidence, action, properness, factorized isometries

At act 29's product configuration (`V = Fin 4 × Fin 4`, the ancilla `Fin 1 × Fin 1`, `Γ ≡ 1/16`, the
ordered decomposition `Equiv.refl`), this module studies the product-embedded stratum: the feature
vectors of the products `X ⊠ Y` of two realizable single-carrier tuples.

The module carries no definition. Every theorem prints its axioms.
-/
'''

def elab_module():
    parts = [IMPORT, '\n', DOC, '\nnamespace OIBridge\nnamespace ProductStratum\n\n', OPEN, '\n']
    for role, nm, key in THEOREMS:
        parts.append('-- %s, `%s`\n#check (%s)\n\n' % (role, nm, PROPS[key]))
    parts.append('-- corollary, `a34_c_exclusive`\n#check ((%s) → ¬ (%s))\n\n' % (PROPS['P_N'], PROPS['P_R']))
    parts.append('end ProductStratum\nend OIBridge\n')
    return ''.join(parts)

if __name__ == '__main__':
    json.dump({'COMPONENTS': COMPONENTS, 'PROPS': PROPS, 'THEOREMS': THEOREMS, 'COROLLARY': COROLLARY,
               'OPEN': OPEN, 'IMPORT': IMPORT, 'DOC': DOC}, open(os.path.join(S, 'props34.json'), 'w'), ensure_ascii=False, indent=1)
    open(os.path.join(S, 'elab34.lean'), 'w', encoding='utf-8').write(elab_module())
    print('props', len(PROPS), 'theorems', len(THEOREMS), 'P_R chars', len(P_R))
