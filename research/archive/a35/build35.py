"""A35 builder: the frozen propositions from shared components (single source).
Writes props35.json (COMPONENTS, PROPS, THEOREMS, ...) and elab35.lean (the #check module for the
disposable branch). controls.py and the preregistration embed the same texts.
Constants filled from probe7: RELAB_IDX / RELAB_VAL, REAL2_ROWS / REAL2_VAL."""
import json, os, sys
S = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(S, '..', 'a34'))
import build34 as B  # A34's frozen texts, reused verbatim where A35 carries them

C = json.load(open(os.path.join(S, 'consts35.json')))
RELAB_IDX, RELAB_VAL = C['RELAB_IDX'], C['RELAB_VAL']      # (a, b, b', c, c', d), value as a Lean literal
REAL2_ROWS, REAL2_VAL = C['REAL2_ROWS'], C['REAL2_VAL']    # four row indices of Fin 4 × Fin 4, value as a Lean literal

E4, E16, TUP, RG = B.E4, B.E16, B.TUP, B.RG
M4 = 'Matrix (Fin 4) (Fin 4) ℂ'
M16 = 'Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ'
TUP16 = 'Fin 4 × Fin 4 → ' + M16
RG16 = 'RealizableGram (Fin 1 × Fin 1) Γ'
HYP = 'fl X → (∀ c, fl (Y c)) → (∀ c b, ‖D c b‖ = 1) →'
HYPT = 'fl X → (∀ a, fl (Y a)) → (∀ a d, ‖E a d‖ = 1) →'
BIND = '(X : ' + M4 + ') (Y : Fin 4 → ' + M4 + ') (D : Fin 4 → Fin 4 → ℂ)'
BINDT = '(X : ' + M4 + ') (Y : Fin 4 → ' + M4 + ') (E : Fin 4 → Fin 4 → ℂ)'
FAM = '{x : ' + E16 + ' | ∃ D : Fin 4 → Fin 4 → ℂ, (∀ c b, ‖D c b‖ = 1) ∧ x = featureVec (gram (dita (F4 Complex.I) (fun _ => F4 Complex.I) D))}'

# ---- the head: act 34's head verbatim, then this round's let-bound objects
HEAD34 = B.HEAD
HEAD35 = (
 '  let Γ : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ := Matrix.of fun i j => Γ₀ i.1 j.1 * Γ₀ i.2 j.2\n'
 '  let N : Set (' + E16 + ') := {x | ∃ G : ' + TUP16 + ', ' + RG16 + ' G ∧ featureVec G = x}\n'
 '  let gram : ' + M16 + ' → (' + TUP16 + ') := fun H i => Matrix.of fun j k => star (H i j) * H i k\n'
 '  let fl : ' + M4 + ' → Prop := fun X => X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a c : Fin 4, ‖X a c‖ = 1 / 2\n'
 '  let dita : ' + M4 + ' → (Fin 4 → ' + M4 + ') → (Fin 4 → Fin 4 → ℂ) → ' + M16 + ' := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2\n'
 '  let ditaT : ' + M4 + ' → (Fin 4 → ' + M4 + ') → (Fin 4 → Fin 4 → ℂ) → ' + M16 + ' := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2\n'
 '  let Δc : Set (' + E16 + ') := {x | ∃ ' + BIND + ', fl X ∧ (∀ c, fl (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ featureVec (gram (dita X Y D)) = x}\n'
 '  let Δr : Set (' + E16 + ') := {x | ∃ ' + BINDT + ', fl X ∧ (∀ a, fl (Y a)) ∧ (∀ a d, ‖E a d‖ = 1) ∧ featureVec (gram (ditaT X Y E)) = x}\n'
 '  let F4 : ℂ → ' + M4 + ' := fun z => Matrix.of fun a c => (1 / 2 : ℂ) * ' + B.F4 + ' a c\n'
)
HEAD = HEAD34 + HEAD35

# ---- bodies
HULL = ('∀ ' + BIND + ', ' + HYP + '\n'
        '    dita X Y D ∈ Matrix.unitaryGroup (Fin 4 × Fin 4) ℂ ∧ (∀ i j, ‖dita X Y D i j‖ = 1 / 4) ∧ ' + RG16 + ' (gram (dita X Y D))')
HULLT = ('∀ ' + BINDT + ', ' + HYPT + '\n'
         '    ditaT X Y E ∈ Matrix.unitaryGroup (Fin 4 × Fin 4) ℂ ∧ (∀ i j, ‖ditaT X Y E i j‖ = 1 / 4) ∧ ' + RG16 + ' (gram (ditaT X Y E))')
SUB = 'Δc ⊆ N ∧ Δr ⊆ N'
SIGMA = 'S ⊆ Δc ∧ S ⊆ Δr'
CROSS = ('∀ X Y : ' + TUP + ', ' + RG + ' X → ' + RG + ' Y → ∀ a b b\' c c\' d : Fin 4,\n'
         '    prod X Y (a, b) (c, d) (c\', d) * prod X Y (a, b\') (c\', d) (c, d) = 1 / 256')
WITH = 'let H : ' + M16 + ' := Matrix.of fun i j => (1 / 4 : ℂ) * ' + B.F4I + ' i.1 j.1 * ' + B.F4T + ' i.2 j.2\n'
RHO = "(Equiv.swap ((1 : Fin 4), (1 : Fin 4)) ((1 : Fin 4), (3 : Fin 4))).trans (Equiv.swap ((3 : Fin 4), (1 : Fin 4)) ((3 : Fin 4), (3 : Fin 4)))"
WIT = (WITH +
       '  let ρ : Equiv.Perm (Fin 4 × Fin 4) := ' + RHO + '\n'
       '  H = dita (F4 Complex.I) (fun c => F4 (if c.val % 2 = 0 then Complex.I else -Complex.I)) (fun _ _ => 1)\n'
       '  ∧ featureVec (gram H) ∈ Δc ∧ featureVec (gram H) ∉ S\n'
       '  ∧ gram H (0, 1) (0, 1) (1, 1) * gram H (0, 0) (1, 1) (0, 1) = -(1 / 256)\n'
       '  ∧ (∀ i j, H i j = dita (F4 Complex.I) (fun _ => F4 Complex.I) (fun _ _ => 1) i (ρ j))\n'
       '  ∧ featureVec (gram H) = featureVec (fun i => (gram (dita (F4 Complex.I) (fun _ => F4 Complex.I) (fun _ _ => 1)) i).submatrix ρ ρ)')
TW_ROWS, TW_VAL = C['TW_ROWS'], C['TW_VAL']
w0, w1, w2, w3 = TW_ROWS
TWIST = ('let Dw : Fin 4 → Fin 4 → ℂ := fun c b => if c = 1 then ![1, Complex.I, 1, -Complex.I] b else 1\n'
         '  let Hw : ' + M16 + ' := dita (F4 Complex.I) (fun _ => F4 Complex.I) Dw\n'
         '  featureVec (gram Hw) ∈ Δc ∧ featureVec (gram Hw) ∉ S\n'
         '  ∧ ∑ k : Fin 4 × Fin 4, Hw (%d, %d) k * star (Hw (%d, %d) k) * Hw (%d, %d) k * star (Hw (%d, %d) k) = %s' % (w0[0], w0[1], w1[0], w1[1], w2[0], w2[1], w3[0], w3[1], TW_VAL))
a, b, bp, c, cp, d = RELAB_IDX
RELAB = ('let σ : Equiv.Perm (Fin 4 × Fin 4) := Equiv.swap ((0 : Fin 4), (1 : Fin 4)) ((1 : Fin 4), (0 : Fin 4))\n'
         '  let P : ' + TUP16 + ' := prod (tup 0 Complex.I) (tup 0 Complex.I)\n'
         '  let Pσ : ' + TUP16 + ' := fun i => (P (σ i)).submatrix σ σ\n'
         '  ' + RG16 + ' Pσ\n'
         '  ∧ (∀ G G\' : ' + TUP16 + ', dist (featureVec (fun i => (G (σ i)).submatrix σ σ)) (featureVec (fun i => (G\' (σ i)).submatrix σ σ)) = dist (featureVec G) (featureVec G\'))\n'
         '  ∧ featureVec P ∈ S ∧ featureVec Pσ ∉ S\n'
         '  ∧ Pσ (%d, %d) (%d, %d) (%d, %d) * Pσ (%d, %d) (%d, %d) (%d, %d) = %s' % (a, b, c, d, cp, d, a, bp, cp, d, c, d, RELAB_VAL))
EXT = ('∀ (π₁ π₂ τ₁ τ₂ : Equiv.Perm (Fin 4)) ' + BIND + ', ' + HYP + '\n'
       '    featureVec (fun i => (gram (dita X Y D) ((π₁.prodCongr π₂) i)).submatrix (τ₁.prodCongr τ₂) (τ₁.prodCongr τ₂)) ∈ Δc\n'
       '    ∧ featureVec (fun i => Matrix.of fun j k => star (gram (dita X Y D) i j k)) ∈ Δc\n'
       '    ∧ featureVec (gram (dita X Y D)ᵀ) ∈ Δr')
MOD = ('∀ (X Y : ' + M4 + ') (D D\' : Fin 4 → Fin 4 → ℂ), fl X → fl Y → (∀ c b, ‖D c b‖ = 1) → (∀ c b, ‖D\' c b‖ = 1) →\n'
       '    featureVec (gram (dita X (fun _ => Y) D)) = featureVec (gram (dita X (fun _ => Y) D\')) →\n'
       '    ∃ u v : Fin 4 → ℂ, ∀ c b, D\' c b = u c * v b * D c b')
INF = ('Set.Infinite ' + FAM + '\n'
       '  ∧ ∀ (G : Finset (' + E16 + ' → ' + E16 + ')) (T : Finset (' + E16 + ')), ∃ D : Fin 4 → Fin 4 → ℂ, (∀ c b, ‖D c b‖ = 1) ∧\n'
       '    ∀ g ∈ G, ∀ t ∈ T, g t ≠ featureVec (gram (dita (F4 Complex.I) (fun _ => F4 Complex.I) D))')
UNTW = 'featureVec (gram (dita (F4 Complex.I) (fun _ => F4 Complex.I) (fun _ _ => 1))) ∈ S'
r0, r1, r2, r3 = REAL2_ROWS
REAL2 = ('let Dr : Fin 4 → Fin 4 → ℂ := fun c b => if c = 3 ∧ b = 3 then -1 else 1\n'
         '  let Hr : ' + M16 + ' := dita (F4 1) (fun _ => F4 1) Dr\n'
         '  (∀ i j, (Hr i j).im = 0) ∧ featureVec (gram Hr) ∈ Δc ∧ featureVec (gram Hr) ∉ S\n'
         '  ∧ ∑ k : Fin 4 × Fin 4, Hr (%d, %d) k * Hr (%d, %d) k * Hr (%d, %d) k * Hr (%d, %d) k = %s' % (r0[0], r0[1], r1[0], r1[1], r2[0], r2[1], r3[0], r3[1], REAL2_VAL))

PKG = '(' + HULL + ')\n  ∧ (' + HULLT + ')\n  ∧ (' + SIGMA + ')\n  ∧ (' + EXT + ')\n  ∧ (' + MOD + ')\n  ∧ (' + INF + ')'
P_R = HEAD + '  ' + PKG
P_N = HEAD + '  ¬ (' + HULL + ')\n  ∨ ¬ (' + HULLT + ')\n  ∨ ¬ (' + SIGMA + ')\n  ∨ ¬ (' + EXT + ')\n  ∨ ¬ (' + MOD + ')\n  ∨ ¬ (' + INF + ')'

COMPONENTS = {'HEAD': HEAD, 'HEAD34': HEAD34, 'HEAD35': HEAD35, 'PKG': PKG, 'HULL': HULL, 'HULLT': HULLT, 'SUB': SUB,
              'SIGMA': SIGMA, 'CROSS': CROSS, 'WITH': WITH, 'WIT': WIT, 'RELAB': RELAB, 'EXT': EXT, 'MOD': MOD, 'INF': INF,
              'UNTW': UNTW, 'REAL2': REAL2, 'TWIST': TWIST, 'RHO': RHO, 'FAM': FAM, 'F4I': B.F4I, 'F4T': B.F4T, 'GDEF': B.GDEF}
PROPS = {'P_R': P_R, 'P_N': P_N,
         'HULL': HEAD + '  ' + HULL, 'HULLT': HEAD + '  ' + HULLT, 'SUB': HEAD + '  ' + SUB, 'SIGMA': HEAD + '  ' + SIGMA,
         'CROSS': HEAD + '  ' + CROSS, 'WIT': HEAD + '  ' + WIT, 'RELAB': HEAD + '  ' + RELAB, 'EXT': HEAD + '  ' + EXT,
         'MOD': HEAD + '  ' + MOD, 'INF': HEAD + '  ' + INF, 'UNTW': HEAD + '  ' + UNTW, 'REAL2': HEAD + '  ' + REAL2, 'TWIST': HEAD + '  ' + TWIST}
THEOREMS = [
 ('A35-DITA-STRATIFIED', 'a35_dita_stratified', 'P_R'),
 ('A35-NOT-DITA-STRATIFIED', 'a35_not_dita_stratified', 'P_N'),
 ('A35-1', 'a35_shared_hull', 'HULL'),
 ('A35-1', 'a35_shared_hull_t', 'HULLT'),
 ('A35-1 corollary', 'a35_shared_hull_sub', 'SUB'),
 ('A35-2', 'a35_shared_sigma_hull', 'SIGMA'),
 ('A35-3', 'a35_shared_cross', 'CROSS'),
 ('A35-3', 'a35_control_witness', 'WIT'),
 ('A35-4', 'a35_control_twist', 'TWIST'),
 ('A35-6', 'a35_control_relabel', 'RELAB'),
 ('A35-7', 'a35_shared_extend', 'EXT'),
 ('A35-7', 'a35_shared_modulus', 'MOD'),
 ('A35-7', 'a35_shared_infinite', 'INF'),
 ('control', 'a35_control_untwisted', 'UNTW'),
 ('A35-5', 'a35_control_real', 'REAL2'),
]
COROLLARY = ('a35_c_exclusive', ['P_N'], 'P_R')
OPEN = ("open Matrix CoherentLiftGauge DilationChoice TwoSidedGauge GramTrajectorySelection\n"
        "  IntermediateCrossTimeStructure RepresentativeNaturality OrbitLawRigidityTwisted\n"
        "  OrbitLawNaturalityFactorization OrbitLawGaps OrbitGeometrySelector OrbitGeometryIsometries\n"
        "  OrbitGeometryRigidity OrbitIsometryGroup ProductStratum\n")
IMPORT = 'import OIBridge.ProductStratum\n'
DOC = '''/-!
# Act 35 — the Diţă hulls of the product-embedded stratum

At act 29's product configuration (`V = Fin 4 × Fin 4`, the ancilla `Fin 1 × Fin 1`, `Γ ≡ 1/16`), this
module studies the two twisted-tensor families through act 34's stratum: the column construction
`X[a,c] · D[c,b] · Y_c[b,d]` and the row construction `X[a,c] · E[a,d] · Y_a[b,d]`, each realizable
for every choice of flat unitary factors and unit twist phases, each containing the stratum, and
each preserved by the product relabellings and the conjugation, the transpose exchanging them. Act
34's properness witness is a point of the column hull; the identity every product tuple satisfies
on its same-row-block, same-column-in-block cross ratios is what it violates. A non-product
relabelling carries a stratum point off the stratum inside its isometry class. The twist phases
enter the feature vector injectively modulo the two gauges, so the hull through one point is
infinite and no finite set of maps applied to a finite set reaches it.

The module carries no definition. Every theorem prints its axioms.
-/
'''

def elab_module():
    parts = [IMPORT, '\n', DOC, '\nnamespace OIBridge\nnamespace DitaHull\n\n', OPEN, '\n']
    for role, nm, key in THEOREMS:
        parts.append('-- %s, `%s`\n#check (%s)\n\n' % (role, nm, PROPS[key]))
    parts.append('-- corollary, `a35_c_exclusive`\n#check ((%s) → ¬ (%s))\n\n' % (PROPS['P_N'], PROPS['P_R']))
    parts.append('end DitaHull\nend OIBridge\n')
    return ''.join(parts)

if __name__ == '__main__':
    json.dump({'COMPONENTS': COMPONENTS, 'PROPS': PROPS, 'THEOREMS': THEOREMS, 'COROLLARY': COROLLARY,
               'OPEN': OPEN, 'IMPORT': IMPORT, 'DOC': DOC}, open(os.path.join(S, 'props35.json'), 'w'), ensure_ascii=False, indent=1)
    open(os.path.join(S, 'elab35.lean'), 'w', encoding='utf-8').write(elab_module())
    print('props', len(PROPS), 'theorems', len(THEOREMS), 'P_R chars', len(P_R))
