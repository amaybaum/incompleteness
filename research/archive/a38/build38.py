"""A38 builder: the frozen propositions from shared components (single source).
Writes props38.json and elab38.lean. controls.py and the preregistration embed the same texts."""
import importlib.util, json, os, sys
S = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('build37', os.path.join(S, '..', 'a37', 'build37.py')); B37 = importlib.util.module_from_spec(spec); spec.loader.exec_module(B37)
HEAD36, HEAD37 = B37.HEAD36, B37.HEAD37
M16 = 'Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ'
def MAT(n): return 'Matrix (Fin %d) (Fin %d) ℂ' % (n, n)

# the nine factorization classes of SIG (column form, index sets as measured at D and frozen by act 37): t1 is act 36's
# frozen class at dita28; the other eight carry act 37's lookup tables in HEAD37
CLASSES = [cl for cl in B37.CLASSES[:4]] + [cl for cl in B37.CLASSES[4:6]] + [B37.FROZEN] + [cl for cl in B37.CLASSES[6:]]
FORM = {nm: ('dita28' if nm == 't1' else 'dita' + nm) for nm, *_ in CLASSES}
ORDER = [nm for nm, *_ in CLASSES]          # k1 k2 k3 k4 e1 e2 t1 t2 t3

# this round's objects: the witness exponent E = A + B + C, closed form on the product index, and the arc
EW = ('(if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + '
      '(if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)')
HEAD38 = ('  let Ew : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => ' + EW + '\n'
          '  let Hu : ℂ → ' + M16 + ' := fun u => Matrix.of fun i j => SIG i j * u ^ Ew i j\n')
HEAD = HEAD36 + HEAD37 + HEAD38

def EX(nm, m, n, form):
    return '(∃ (X : %s) (Y : Fin %d → %s) (D : Fin %d → Fin %d → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Hu u = %s)' % (MAT(m), m, MAT(n), m, n, form)
def EXCL(nm, m, n):
    return ('∀ u : ℂ, star u * u = 1 →\n    (' + EX(nm, m, n, '%s X Y D' % FORM[nm]) + ' → u = 1)\n    ∧ (' + EX(nm, m, n, '(%s X Y D)ᵀ' % FORM[nm]) + ' → u = 1)')
REAL = ('∀ u : ℂ, star u * u = 1 →\n'
        '    Hu u ∈ Matrix.unitaryGroup (Fin 4 × Fin 4) ℂ ∧ (∀ i j, ‖Hu u i j‖ = 1 / 4)\n'
        '    ∧ RealizableGram (Fin 1 × Fin 1) Γ (gram (Hu u)) ∧ featureVec (gram (Hu u)) ∈ N')
BASE = 'Hu 1 = SIG ∧ flg (F4 z) ∧ (∀ c : Fin 4, flg (F4 w)) ∧ SIG = ditak1 (F4 z) (fun _ => F4 w) (fun _ _ => (1 : ℂ))'
NEG = '\n    ∧ '.join('¬ ' + EX(nm, m, n, '%s X Y D' % FORM[nm]) + '\n    ∧ ¬ ' + EX(nm, m, n, '(%s X Y D)ᵀ' % FORM[nm]) for nm, m, n, _, _ in CLASSES)
ESCAPE = ('∀ ε : ℝ, 0 < ε → ∃ u : ℂ, star u * u = 1 ∧ u ≠ 1 ∧ ‖u - 1‖ < ε ∧ (∀ i j, ‖Hu u i j - SIG i j‖ < ε)\n'
          '    ∧ RealizableGram (Fin 1 × Fin 1) Γ (gram (Hu u)) ∧ featureVec (gram (Hu u)) ∈ N\n    ∧ ' + NEG)
EXCLS = {'EXCL_' + nm: EXCL(nm, m, n) for nm, m, n, _, _ in CLASSES}
PARTS = ['REAL'] + list(EXCLS)
COMP = {'HEAD': HEAD, 'HEAD36': HEAD36, 'HEAD37': HEAD37, 'HEAD38': HEAD38, 'REAL': REAL, 'BASE': BASE, 'ESCAPE': ESCAPE}
COMP.update(EXCLS)
PKG = '\n  ∧ '.join('(' + COMP[k] + ')' for k in PARTS)
COMP['PKG'] = PKG
P_R = HEAD + '  ' + PKG
P_N = HEAD + '  ' + '\n  ∨ '.join('¬ (' + COMP[k] + ')' for k in PARTS)
PROPS = {'P_R': P_R, 'P_N': P_N, 'REAL': HEAD + '  ' + REAL, 'BASE': HEAD + '  ' + BASE, 'ESCAPE': HEAD + '  ' + ESCAPE}
PROPS.update({k: HEAD + '  ' + v for k, v in EXCLS.items()})
THEOREMS = [
 ('A38-NON-DITA-WITNESS-PROVED', 'a38_witness', 'P_R'),
 ('A38-WITNESS-FAILS', 'a38_not_witness', 'P_N'),
 ('A38-1', 'a38_shared_realizable', 'REAL'),
] + [('A38-2', 'a38_shared_excl_' + nm, 'EXCL_' + nm) for nm, _, _, _, _ in CLASSES] + [
 ('A38-3', 'a38_c_local_escape', 'ESCAPE'),
 ('control', 'a38_control_base', 'BASE'),
]
COROLLARY = ('a38_c_exclusive', ['P_N'], 'P_R')
P37 = json.load(open(os.path.join(S, '..', 'a37', 'props37.json')))
OPEN = P37['OPEN'].rstrip('\n') + ' DitaArcExclusivity\n'
IMPORT = 'import OIBridge.DitaArcExclusivity\n'
DOC = '''/-!
# Act 38 — a genuine non-Diţă local escape at the product-embedded stratum point

Acts 36 and 37 ran an exact arc of realizable classes through the certified rational stratum point
`SIG = F₄(z) ⊗ F₄(w)`, `z = (3+4i)/5`, `w = (5+12i)/13`, and found it exclusive to its frozen `2 × 8` Diţă
class: an arc that lies in one Diţă hull at every parameter. This module states, for one explicit
exponent matrix `E = A + B + C` in `{0, 1}` and the arc `Hu u = SIG ∘ u^E`: that `Hu u` is a flat unitary
— a complex Hadamard matrix, realizable — at every unit `u`; that for each of the nine Diţă factorization
classes of `SIG` — four `4 × 4`, two `8 × 2` and three `2 × 8`, the complete census of the stratum point's
Diţă structures modulo its stabilizer — a Diţă form of `Hu u` at that class's index maps, in either
orientation, forces `u = 1`; and, as the corollary, that every neighbourhood of `SIG` contains a
realizable matrix admitting none of the eighteen forms. The exact-computation layer carries the
exhaustive complement: at every unit `u ∉ {1, −1}`, no index maps whatever admit a Diţă form of `Hu u`,
and at `u = −1` exactly one `2 × 8` structure per orientation does.

The module carries no definition. Every theorem prints its axioms.
-/
'''
def elab_module():
    parts = [IMPORT, '\n', DOC, '\nnamespace OIBridge\nnamespace DitaLocalEscape\n\n', OPEN, '\n']
    for role, nm, key in THEOREMS:
        parts.append('-- %s, `%s`\n#check (%s)\n\n' % (role, nm, PROPS[key]))
    parts.append('-- corollary, `a38_c_exclusive`\n#check ((%s) → ¬ (%s))\n\n' % (PROPS['P_N'], PROPS['P_R']))
    parts.append('end DitaLocalEscape\nend OIBridge\n')
    return ''.join(parts)
if __name__ == '__main__':
    json.dump({'COMPONENTS': COMP, 'PROPS': PROPS, 'THEOREMS': THEOREMS, 'COROLLARY': COROLLARY, 'PARTS': PARTS,
               'CLASSES': [list(c[:3]) for c in CLASSES], 'FORM': FORM, 'OPEN': OPEN, 'IMPORT': IMPORT, 'DOC': DOC, 'EW': EW},
              open(os.path.join(S, 'props38.json'), 'w'), ensure_ascii=False, indent=1)
    open(os.path.join(S, 'elab38.lean'), 'w', encoding='utf-8').write(elab_module())
    print('props', len(PROPS), 'theorems', len(THEOREMS), 'P_R chars', len(P_R), 'HEAD38 lines', HEAD38.count('\n'))
