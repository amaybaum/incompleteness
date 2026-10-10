"""Emit the A37 module (stage 1 or, with --verdict, stage 2) from props37.json: hand-written core lemmas plus the
frozen statements verbatim. usage: python3 stage37.py [--verdict] > mod37.lean"""
import json, os, sys
S = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, S)
import build37 as B
P = json.load(open(os.path.join(S, 'props37.json'))); PR = P['PROPS']
WIT = json.load(open(os.path.join(S, 'witness37.json')))
VERDICT = '--verdict' in sys.argv
sys.path.insert(0, os.path.join(S, '..', 'a36'))
# the A36 emitter's text builders, reused verbatim
src36 = open(os.path.join(S, '..', 'a36', 'stage36.py'), encoding='utf-8').read()
exec(src36[src36.index('E16 = '):src36.index('# the witnesses of the line')])
M16 = 'Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ'
def MAT(n): return 'Matrix (Fin %d) (Fin %d) ℂ' % (n, n)
PUC = PU(ZC, WC, 'u'); SIGC = SIG(ZC, WC)
def POS(i): return '((%d : Fin 4), (%d : Fin 4))' % (i // 4, i % 4)
def DITAX(name, m, n, cp, rows):
    """the class's Dita form, beta-reduced as `dsimp only` leaves it in the frozen statement"""
    cblk = [None] * 16; cpos = [None] * 16; ra = [None] * 16; rb = [None] * 16
    for c in range(m):
        for d in range(n): cblk[cp[c][d]] = c; cpos[cp[c][d]] = d
    for b in range(n):
        for a in range(m): ra[rows[b][a]] = a; rb[rows[b][a]] = b
    return ('(Matrix.of fun i j : Fin 4 × Fin 4 => ' + DG('X', 'Y', 'D', 'Fin %d × Fin %d' % (m, n)) +
            ' (%s i.1 i.2, %s i.1 i.2) (%s j.1 j.2, %s j.1 j.2))' % (B.table(ra), B.table(rb), B.table(cblk), B.table(cpos)))
def EXQ(m, n, form):
    return ('(∃ (X : %s) (Y : Fin %d → %s) (D : Fin %d → Fin %d → ℂ), ' % (MAT(m), m, MAT(n), m, n) + FLG('Fin %d' % m, 'X') +
            ' ∧ (∀ c, ' + FLG('Fin %d' % n, 'Y c') + ') ∧ (∀ c b, ‖D c b‖ = 1) ∧ ' + PUC + ' = ' + form + ')')

out = []
def thm(name, stmt, proof):
    out.append('theorem %s :\n    %s := by\n%s\n#print axioms %s\n' % (name, stmt, proof, name))

# ---------------------------------------------------------------- symmetry
F4V = '((1 / 2 : ℂ) * ![![1, 1, 1, 1], ![1, t, -1, -t], ![1, -1, 1, -1], ![1, -t, -1, t]] a c)'
thm('a37_shared_f4_symm', '∀ (t : ℂ) (a c : Fin 4), ' + F4V + ' = ' + F4V.replace(' a c)', ' c a)'), '''  intro t a c
  fin_cases a <;> fin_cases c <;> simp''')
thm('a37_shared_wt_symm', '∀ i j : Fin 4 × Fin 4, ' + WT + ' = ' + WT.replace('i.1', 'J1').replace('j.1', 'i.1').replace('J1', 'j.1').replace('i.2', 'J2').replace('j.2', 'i.2').replace('J2', 'j.2'), '''  intro i j
  by_cases h1 : i.1.val % 2 = 0 <;> by_cases h2 : j.1.val % 2 = 0 <;> simp [h1, h2, add_comm]''')
thm('a37_shared_sym_core', '∀ z w u : ℂ, ' + PU('z', 'w', 'u') + 'ᵀ = ' + PU('z', 'w', 'u'), '''  intro z w u
  ext i j
  simp only [Matrix.transpose_apply, Matrix.of_apply]
  rw [a37_shared_f4_symm z j.1 i.1, a37_shared_f4_symm w j.2 i.2, a37_shared_wt_symm j i]''')

# ---------------------------------------------------------------- persistence in both orientations
thm('a37_shared_persist_core', G0 + '∀ u : ℂ, star u * u = 1 → ' + EXQ(2, 8, DITA28('X', 'Y', 'D')) + ' ∧ ' + EXQ(2, 8, DITA28('X', 'Y', 'D') + 'ᵀ'), '''  intro Γ₀ hΓ₀ u hu
  obtain ⟨X, Y, D, hX, hY, hD, h⟩ := (a36_shared_line_core Γ₀ hΓ₀ _ _ u a36_shared_z_unit a36_shared_w_unit hu).1
  refine ⟨⟨X, Y, D, hX, hY, hD, h⟩, ⟨X, Y, D, hX, hY, hD, ?_⟩⟩
  rw [← h]
  exact (a37_shared_sym_core _ _ u).symm''')

# ---------------------------------------------------------------- the eight exclusions
def excl_core(name, m, n, cp, rows):
    w = WIT[name]; p = w['p']; coef = w['coef']
    form = DITAX(name, m, n, cp, rows)
    def key(h):
        return ('    have key : ' + PUC + ' ' + POS(p[0][0]) + ' ' + POS(p[0][1]) + ' * ' + PUC + ' ' + POS(p[1][0]) + ' ' + POS(p[1][1]) +
                ' = ' + PUC + ' ' + POS(p[2][0]) + ' ' + POS(p[2][1]) + ' * ' + PUC + ' ' + POS(p[3][0]) + ' ' + POS(p[3][1]) + ''' := by
      rw [''' + h + ''']
      simp only [Matrix.of_apply]
      (try simp)
      (try ring)
    simp (config := { decide := true }) [Matrix.of_apply] at key
    first
    | linear_combination (''' + str(coef) + ''' : ℂ) * key
    | exact key
    | (ring_nf at key; linear_combination (''' + str(coef) + ''' : ℂ) * key)''')
    thm('a37_shared_excl_core_' + name, '∀ u : ℂ, star u * u = 1 → (' + EXQ(m, n, form) + ' → u = 1) ∧ (' + EXQ(m, n, form + 'ᵀ') + ' → u = 1)', '''  intro u hu
  have hsym := a37_shared_sym_core ''' + ZC + ' ' + WC + ''' u
  refine ⟨?_, ?_⟩
  · rintro ⟨X, Y, D, -, -, -, h⟩
''' + key('h') + '''
  · rintro ⟨X, Y, D, -, -, -, h⟩
    have h' : ''' + PUC + ' = ' + form + ''' := by
      rw [← hsym, h, Matrix.transpose_transpose]
''' + key("h'"))
for cl in B.CLASSES:
    excl_core(*cl)

# ---------------------------------------------------------------- the base control
K1 = B.CLASSES[0]
thm('a37_shared_base_core', G0 + PU(ZC, WC, '1') + ' = ' + SIGC + ' ∧ ' + FLG('Fin 4', F4(ZC)) + ' ∧ (∀ c : Fin 4, ' + FLG('Fin 4', F4(WC)) + ') ∧ ' + SIGC + ' = ' +
    DITAX(*K1).replace('X i.1 j.1', F4(ZC) + ' i.1 j.1').replace('D j.1 i.2', '(fun (_ : Fin 4) (_ : Fin 4) => (1 : ℂ)) j.1 i.2').replace('Y j.1 i.2 j.2', '(fun (_ : Fin 4) => ' + F4(WC) + ') j.1 i.2 j.2'), '''  intro Γ₀ hΓ₀
  have hf : ∀ (t : ℂ), star t * t = 1 → ''' + FLG('Fin 4', F4('t')) + ''' := by
    intro t ht
    refine ⟨(a35_shared_f4_flat Γ₀ hΓ₀ t ht).1, ?_⟩
    intro a c
    have h := a35_shared_half t ht a c
    simp only [Matrix.of_apply] at h ⊢
    rw [h]
    norm_num [Fintype.card_fin]
  have hA : ∀ p q : Fin 4, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] p q = p := by
    intro p q; fin_cases p <;> fin_cases q <;> rfl
  have hB : ∀ p q : Fin 4, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] p q = q := by
    intro p q; fin_cases p <;> fin_cases q <;> rfl
  refine ⟨(a36_shared_one_core Γ₀ hΓ₀).1, hf _ a36_shared_z_unit, fun _ => hf _ a36_shared_w_unit, ?_⟩
  ext i j
  simp only [Matrix.of_apply, hA, hB, mul_one]''')

# ---------------------------------------------------------------- the frozen theorems
def frozen(name, key, tail):
    thm(name, PR[key], '  intro Γ₀ hΓ₀\n  dsimp only\n' + tail)
frozen('a37_shared_symmetric', 'SYM', '  intro u\n  exact a37_shared_sym_core _ _ u')
frozen('a37_shared_persistence', 'PERSIST', '  intro u hu\n  exact a37_shared_persist_core Γ₀ hΓ₀ u hu')
for nm, m, n, _, _ in B.CLASSES:
    frozen('a37_shared_excl_' + nm, 'EXCL_' + nm, '  exact a37_shared_excl_core_' + nm)
frozen('a37_control_base', 'BASE', '  exact a37_shared_base_core Γ₀ hΓ₀')
if VERDICT:
    cores = ['fun u => a37_shared_sym_core _ _ u', 'fun u hu => a37_shared_persist_core Γ₀ hΓ₀ u hu'] + ['a37_shared_excl_core_' + nm for nm, _, _, _, _ in B.CLASSES]
    frozen('a37_exclusivity', 'P_R', '  exact ⟨' + ', '.join(cores) + '⟩')
    n = len(P['PARTS'])
    alts = ' | '.join(['h'] * n)
    proj = ['r' + '.2' * k + ('.1' if k < n - 1 else '') for k in range(n)]
    out.append('theorem a37_c_exclusive :\n    (' + PR['P_N'] + ') → ¬ (' + PR['P_R'] + ''') := by
  intro hN hR
  have h := hN _ rfl
  have r := hR _ rfl
  dsimp only at h r
  rcases h with ''' + alts + '\n' + '\n'.join('  · exact h ' + pj for pj in proj) + '''
#print axioms a37_c_exclusive
''')
HEADER = P['IMPORT'] + '\n' + P['DOC'] + '\nnamespace OIBridge\nnamespace DitaArcExclusivity\n\n' + P['OPEN'] + '\n'
sys.stdout.write(HEADER + '\n'.join(out) + 'end DitaArcExclusivity\nend OIBridge\n')
