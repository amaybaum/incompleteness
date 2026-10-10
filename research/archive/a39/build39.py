"""A39 builder: the frozen propositions from shared components (single source).
Writes props39.json and elab39.lean. controls.py and the preregistration embed the same texts."""
import json, os, sys
S = os.path.dirname(os.path.abspath(__file__))
P38 = json.load(open(os.path.join(S, '..', 'a38', 'props38.json')))
HEAD38 = P38['COMPONENTS']['HEAD']          # act 38's frozen head: act 36's head, act 37's tables, act 38's Ew and Hu
M16 = 'Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ'
EA = '(if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0)'
EB = '(if i.1 = 2 ∧ j.2 = 1 then 1 else 0)'
EC = '(if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)'
assert P38['EW'] == EA + ' + ' + EB + ' + ' + EC, 'act 38 Ew is not the sum of the three pieces as written'
HEAD39 = ('  let Ea : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => ' + EA + '\n'
          '  let Eb : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => ' + EB + '\n'
          '  let Ec : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => ' + EC + '\n'
          '  let H3 : ℂ → ℂ → ℂ → ' + M16 + ' := fun u₁ u₂ u₃ => Matrix.of fun i j => SIG i j * u₁ ^ Ea i j * u₂ ^ Eb i j * u₃ ^ Ec i j\n')
HEAD = HEAD38 + HEAD39
REAL = ('∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →\n'
        '    H3 u₁ u₂ u₃ ∈ Matrix.unitaryGroup (Fin 4 × Fin 4) ℂ ∧ (∀ i j, ‖H3 u₁ u₂ u₃ i j‖ = 1 / 4)\n'
        '    ∧ RealizableGram (Fin 1 × Fin 1) Γ (gram (H3 u₁ u₂ u₃)) ∧ featureVec (gram (H3 u₁ u₂ u₃)) ∈ N')
BASE = 'H3 1 1 1 = SIG'
DIAG = '∀ u : ℂ, H3 u u u = Hu u'
PARTS = ['REAL']
COMP = {'HEAD': HEAD, 'HEAD38': HEAD38, 'HEAD39': HEAD39, 'REAL': REAL, 'BASE': BASE, 'DIAG': DIAG}
PKG = '\n  ∧ '.join('(' + COMP[k] + ')' for k in PARTS)
COMP['PKG'] = PKG
P_R = HEAD + '  ' + PKG
P_N = HEAD + '  ' + '\n  ∨ '.join('¬ (' + COMP[k] + ')' for k in PARTS)
PROPS = {'P_R': P_R, 'P_N': P_N, 'REAL': HEAD + '  ' + REAL, 'BASE': HEAD + '  ' + BASE, 'DIAG': HEAD + '  ' + DIAG}
THEOREMS = [
 ('A39-REALIZABLE-PROVED', 'a39_realizable', 'P_R'),
 ('A39-REALIZABLE-FAILS', 'a39_not_realizable', 'P_N'),
 ('A39-1', 'a39_shared_realizable', 'REAL'),
 ('control', 'a39_control_base', 'BASE'),
 ('control', 'a39_control_diagonal', 'DIAG'),
]
COROLLARY = ('a39_c_exclusive', ['P_N'], 'P_R')
OPEN = P38['OPEN'].rstrip('\n') + ' DitaLocalEscape\n'
IMPORT = 'import OIBridge.DitaLocalEscape\n'
DOC = '''/-!
# Act 39 — the three-parameter realizable family through the product-embedded stratum point

Act 38 exhibited an exponent matrix `E = A + B + C` with entries in `{0, 1}`, three disjoint pieces, for
which the arc `SIG ∘ u^E` through the certified rational stratum point `SIG = F₄(z) ⊗ F₄(w)`,
`z = (3+4i)/5`, `w = (5+12i)/13`, is a complex Hadamard matrix at every unit `u`. This module states the
three-parameter family `H3 u₁ u₂ u₃ = SIG ∘ u₁^A u₂^B u₃^C` realizable on the whole torus: for all units
`u₁, u₂, u₃`, `H3 u₁ u₂ u₃` is a flat unitary, its Gram family is realizable, and its feature vector lies
in the product normalized set. It also states the family through the stratum point, `H3 1 1 1 = SIG`,
and its diagonal equal to act 38's arc, `H3 u u u = Hu u`. It says nothing about which points of the
torus admit a Diţă structure.

The module carries no definition. Every theorem prints its axioms.
-/
'''
def elab_module():
    parts = [IMPORT, '\n', DOC, '\nnamespace OIBridge\nnamespace DitaTorus\n\n', OPEN, '\n']
    for role, nm, key in THEOREMS:
        parts.append('-- %s, `%s`\n#check (%s)\n\n' % (role, nm, PROPS[key]))
    parts.append('-- corollary, `a39_c_exclusive`\n#check ((%s) → ¬ (%s))\n\n' % (PROPS['P_N'], PROPS['P_R']))
    parts.append('end DitaTorus\nend OIBridge\n')
    return ''.join(parts)
if __name__ == '__main__':
    json.dump({'COMPONENTS': COMP, 'PROPS': PROPS, 'THEOREMS': THEOREMS, 'COROLLARY': COROLLARY, 'PARTS': PARTS,
               'OPEN': OPEN, 'IMPORT': IMPORT, 'DOC': DOC, 'EA': EA, 'EB': EB, 'EC': EC},
              open(os.path.join(S, 'props39.json'), 'w'), ensure_ascii=False, indent=1)
    open(os.path.join(S, 'elab39.lean'), 'w', encoding='utf-8').write(elab_module())
    print('props', len(PROPS), 'theorems', len(THEOREMS), 'P_R chars', len(P_R), 'HEAD39 lines', HEAD39.count('\n'))
