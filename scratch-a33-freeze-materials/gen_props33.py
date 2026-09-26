"""A33: the frozen propositions and their shared components -> props33.json.
Every text here was elaborated on the disposable branch claude/a33-elaboration (run 36257659584)."""
import json, sys

E = "EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4))"
T = "Fin 4 → Matrix (Fin 4) (Fin 4) ℂ"
FZ = lambda z: ("FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>\n"
                f"        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, {z}, -1, -{z}; 1, -1, 1, -1; 1, -{z}, -1, {z}] p.1 q.1))")
P1, S23, S12 = "(1 : Equiv.Perm (Fin 4))", "Equiv.swap (2 : Fin 4) 3", "Equiv.swap (1 : Fin 4) 2"
R9 = [(P1, P1), (P1, S23), (P1, S12), (S23, P1), (S23, S23), (S23, S12), (S12, P1), (S12, S23), (S12, S12)]
RTXT = "![" + ", ".join(f"({a}, {b})" for a, b in R9) + "]"
V1, V2 = "![0, 2, 4, 2, 0, 3, 4, 5, 0]", "![1, 3, 5, 5, 4, 1, 3, 1, 2]"

HEAD = ("∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →\n"
        f"  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := {RTXT}\n"
        f"  let pt : Fin 9 → ℂ → {E} := fun r z => featureVec (fun i =>\n"
        f"    ({FZ('z')} ((R r).1 i)).submatrix (R r).2 (R r).2)\n"
        f"  let v₁ : Fin 9 → Fin 6 := {V1}\n"
        f"  let v₂ : Fin 9 → Fin 6 := {V2}\n")
FIN = f"  let v₁ : Fin 9 → Fin 6 := {V1}\n  let v₂ : Fin 9 → Fin 6 := {V2}\n"
CIRC = "{z : ℂ | star z * z = 1}"
EDGE = lambda nu: (f"(∀ r : Fin 9, ∃ s : Fin 9, ({nu} (v₁ r) = v₁ s ∧ {nu} (v₂ r) = v₂ s) ∨ ({nu} (v₁ r) = v₂ s ∧ {nu} (v₂ r) = v₁ s))")


def NF(f, nu, ep):
    return (EDGE(nu) + "\n"
            f"    ∧ (∀ r s : Fin 9, {nu} (v₁ r) = v₁ s → {nu} (v₂ r) = v₂ s → ∀ z : ℂ, star z * z = 1 →\n"
            f"        {f} (pt r z) = pt s (if {ep} r then z else star z))\n"
            f"    ∧ (∀ r s : Fin 9, {nu} (v₁ r) = v₂ s → {nu} (v₂ r) = v₁ s → ∀ z : ℂ, star z * z = 1 →\n"
            f"        {f} (pt r z) = pt s (-(if {ep} r then z else star z)))")


SURJ = lambda f: f"IsSurjIsometryOn (normalizedSet Γ₀) {f}"
DEG = lambda v, ep: f"((Finset.univ.filter (fun r : Fin 9 => (v₁ r = {v} ∨ v₂ r = {v}) ∧ {ep} r = false)).card % 2)"
PARITY = lambda ep: f"∀ v w : Fin 6, {DEG('v', ep)} = {DEG('w', ep)}"


def FAM(f):
    return (f"(∃ π τ : Equiv.Perm (Fin 4),\n"
            f"      (∀ G : {T}, RealizableGram (Fin 1) Γ₀ G → {f} (featureVec G) = featureVec (fun i => (G (π i)).submatrix τ τ))\n"
            f"      ∨ (∀ G : {T}, RealizableGram (Fin 1) Γ₀ G →\n"
            f"          {f} (featureVec G) = featureVec (fun i => Matrix.of fun j k => star ((G (π i)).submatrix τ τ j k)))\n"
            f"      ∨ (∀ G : {T}, RealizableGram (Fin 1) Γ₀ G → ∀ U, AdmissibleDilationAt Γ₀ (0 : Fin 1) U →\n"
            f"          FibreGram (0 : Fin 1) U = G → {f} (featureVec G) = featureVec (fun i => (FibreGram (0 : Fin 1) Uᵀ (π i)).submatrix τ τ))\n"
            f"      ∨ (∀ G : {T}, RealizableGram (Fin 1) Γ₀ G → ∀ U, AdmissibleDilationAt Γ₀ (0 : Fin 1) U →\n"
            f"          FibreGram (0 : Fin 1) U = G → {f} (featureVec G) = featureVec (fun i => Matrix.of fun j k =>\n"
            f"            star ((FibreGram (0 : Fin 1) Uᵀ (π i)).submatrix τ τ j k))))")


NF_UNIQ = NF('f', 'νε.1', 'νε.2')
NF_REAL = NF('f', 'ν', 'ε')
UNIQ = f"(∀ f : {E} → {E}, {SURJ('f')} →\n      ∃! νε : Equiv.Perm (Fin 6) × (Fin 9 → Bool),\n    {NF_UNIQ})"
REAL = (f"(∀ (ν : Equiv.Perm (Fin 6)) (ε : Fin 9 → Bool),\n      {EDGE('ν')} →\n"
        f"      ∃ f : {E} → {E}, {SURJ('f')} ∧\n    {NF_REAL})")
NUNIQ = f"(∃ f : {E} → {E}, {SURJ('f')} ∧\n      ¬ ∃! νε : Equiv.Perm (Fin 6) × (Fin 9 → Bool),\n    {NF_UNIQ})"
NREAL = (f"(∃ (ν : Equiv.Perm (Fin 6)) (ε : Fin 9 → Bool),\n      {EDGE('ν')} ∧\n"
         f"      ∀ f : {E} → {E}, {SURJ('f')} →\n    ¬ ({NF_REAL}))")
AUT = "(Finset.univ.filter (fun ν : Equiv.Perm (Fin 6) => " + EDGE('ν')[1:-1] + "))"

P = {}
P['P_R'] = HEAD + "  " + UNIQ + "\n  ∧ " + REAL
P['P_N'] = HEAD + "  " + NUNIQ + "\n  ∨ " + NREAL
# A33-1 circle preservation
P['B1'] = HEAD + (f"  ∀ f : {E} → {E}, {SURJ('f')} →\n"
                  f"    ∀ r : Fin 9, ∃ s : Fin 9, f '' (pt r '' {CIRC}) = pt s '' {CIRC}")
# A33-2 normal form and signs
P['B2'] = HEAD + (f"  ∀ f : {E} → {E}, {SURJ('f')} → ∀ r s : Fin 9, f '' (pt r '' {CIRC}) = pt s '' {CIRC} →\n"
                  f"    ∃ (l : ℂ) (ε : Bool), star l * l = 1 ∧ ∀ z : ℂ, star z * z = 1 → f (pt r z) = pt s (l * (if ε then z else star z))")
P['B3'] = HEAD + (f"  ∀ f : {E} → {E}, {SURJ('f')} → ∀ (σ : Fin 9 → Fin 9) (l : Fin 9 → ℂ) (ε : Fin 9 → Bool),\n"
                  f"    (∀ r, star (l r) * l r = 1) → (∀ r, ∀ z : ℂ, star z * z = 1 → f (pt r z) = pt (σ r) (l r * (if ε r then z else star z))) →\n"
                  f"    ∀ r, l r = 1 ∨ l r = -1")
# A33-3 the group law in coordinates, the identity, the order of the incidence group
P['COMP'] = HEAD + (
    f"  ∀ (ν ν' : Equiv.Perm (Fin 6)) (ε ε' : Fin 9 → Bool) (f f' : {E} → {E}), {SURJ('f')} → {SURJ(chr(102)+chr(39))} →\n    "
    + NF_REAL + " →\n    " + NF("f'", "ν'", "ε'") + " →\n"
    f"    ∀ ε'' : Fin 9 → Bool, (∀ r s : Fin 9, (ν' (v₁ r) = v₁ s ∧ ν' (v₂ r) = v₂ s) ∨ (ν' (v₁ r) = v₂ s ∧ ν' (v₂ r) = v₁ s) →\n"
    f"        ε'' r = decide (ε' r = ε s)) →\n    " + NF("(f ∘ f')", "(ν * ν')", "ε''"))
P['C_ID'] = HEAD + "  " + NF(f"(id : {E} → {E})", "(1 : Equiv.Perm (Fin 6))", "(fun _ => true)")
P['ORDER'] = FIN + f"  {AUT}.card = 72"
P['TRANS_C'] = FIN + f"  ∀ r s : Fin 9, ∃ ν ∈ {AUT}, (ν (v₁ r) = v₁ s ∧ ν (v₂ r) = v₂ s) ∨ (ν (v₁ r) = v₂ s ∧ ν (v₂ r) = v₁ s)"
P['STAB_C'] = FIN + f"  ({AUT}.filter (fun ν => (ν (v₁ 0) = v₁ 0 ∧ ν (v₂ 0) = v₂ 0) ∨ (ν (v₁ 0) = v₂ 0 ∧ ν (v₂ 0) = v₁ 0))).card = 8"
P['TRANS_V'] = FIN + f"  ∀ v w : Fin 6, ∃ ν ∈ {AUT}, ν v = w"
P['STAB_V'] = FIN + f"  ({AUT}.filter (fun ν => ν 0 = 0)).card = 12"
# A33-4 the old family
P['FAM_K'] = HEAD + (f"  ∀ f : {E} → {E}, {SURJ('f')} → ∀ ε : Fin 9 → Bool,\n    "
                     + NF('f', '(1 : Equiv.Perm (Fin 6))', 'ε') + f" →\n    ({FAM('f')} ↔ {PARITY('ε')})")
P['FAM_COUNT'] = FIN + f"  (Finset.univ.filter (fun ε : Fin 9 → Bool => {PARITY('ε')})).card = 32"
EPSPROD = "(fun r => decide (ε r = ε' r))"
P['FAM_COSET'] = HEAD + (
    f"  ∀ (ν : Equiv.Perm (Fin 6)) (ε ε' : Fin 9 → Bool) (f f' : {E} → {E}), {SURJ('f')} → {SURJ(chr(102)+chr(39))} →\n    "
    + NF_REAL + " →\n    " + NF("f'", "ν", "ε'") + " →\n"
    f"    {FAM('f')} →\n    ({FAM(chr(102)+chr(39))} ↔ {PARITY(EPSPROD)})")
P['FAM_ONTO'] = HEAD + (f"  ∀ ν : Equiv.Perm (Fin 6), {EDGE('ν')} → ∃ (ε : Fin 9 → Bool) (f : {E} → {E}), {SURJ('f')} ∧ {FAM('f')} ∧\n    "
                        + NF_REAL)
# the controls
P['C_CONJ'] = HEAD + f"  ∃ f : {E} → {E}, {SURJ('f')} ∧\n    " + NF('f', '(1 : Equiv.Perm (Fin 6))', '(fun _ => false)')
P['C_A32'] = HEAD + f"  ∃ f : {E} → {E}, {SURJ('f')} ∧ ¬ {FAM('f')} ∧\n    " + NF('f', '(1 : Equiv.Perm (Fin 6))', '(fun r => decide (r ≠ 0))')
P['C_PHASE'] = HEAD + "  dist (pt 0 (Complex.I * Complex.I)) (pt 4 Complex.I) ≠ dist (pt 0 Complex.I) (pt 4 Complex.I)"
P['C_INCID'] = HEAD + (f"  (∀ z w : ℂ, star z * z = 1 → star w * w = 1 → 1 ≤ dist (pt 0 z) (pt 3 w))\n"
                       f"  ∧ pt 1 1 = pt 3 1\n"
                       f"  ∧ ¬ ∃ f : {E} → {E}, {SURJ('f')} ∧ f '' (pt 0 '' {CIRC}) = pt 1 '' {CIRC}\n"
                       f"      ∧ f '' (pt 3 '' {CIRC}) = pt 3 '' {CIRC}")

COMPONENTS = {'HEAD': HEAD, 'FIN': FIN, 'UNIQ': UNIQ, 'REAL': REAL, 'NUNIQ': NUNIQ, 'NREAL': NREAL,
              'NF_UNIQ': NF_UNIQ, 'NF_REAL': NF_REAL, 'EDGE': EDGE('ν'), 'AUT': AUT, 'FAM': FAM('f'),
              'PARITY': PARITY('ε'), 'SURJ': SURJ('f'), 'CIRC': CIRC}
OPEN = ("open Matrix CoherentLiftGauge DilationChoice TwoSidedGauge GramTrajectorySelection\n"
        "  IntermediateCrossTimeStructure RepresentativeNaturality OrbitLawRigidityTwisted\n"
        "  OrbitLawNaturalityFactorization OrbitLawGaps OrbitGeometrySelector OrbitGeometryIsometries\n"
        "  OrbitGeometryRigidity\n")
THEOREMS = [  # (role, name, key)
    ('A33-CLASSIFIED', 'a33_classified', 'P_R'), ('A33-NOT-CLASSIFIED', 'a33_not_classified', 'P_N'),
    ('corollary', 'a33_c_exclusive', None),
    ('A33-1', 'a33_shared_circles', 'B1'),
    ('A33-2', 'a33_shared_form', 'B2'), ('A33-2', 'a33_shared_signs', 'B3'),
    ('A33-3', 'a33_shared_composition', 'COMP'), ('A33-3', 'a33_shared_identity', 'C_ID'),
    ('A33-3', 'a33_shared_order', 'ORDER'),
    ('A33-3 corollary', 'a33_c_transitive_circles', 'TRANS_C'), ('A33-3 corollary', 'a33_c_stabilizer_circle', 'STAB_C'),
    ('A33-3 corollary', 'a33_c_transitive_points', 'TRANS_V'), ('A33-3 corollary', 'a33_c_stabilizer_point', 'STAB_V'),
    ('A33-4', 'a33_shared_family_kernel', 'FAM_K'), ('A33-4', 'a33_shared_family_count', 'FAM_COUNT'),
    ('A33-4', 'a33_shared_family_coset', 'FAM_COSET'), ('A33-4', 'a33_shared_family_onto', 'FAM_ONTO'),
    ('control', 'a33_control_conjugation', 'C_CONJ'), ('control', 'a33_control_a32', 'C_A32'),
    ('control', 'a33_control_phase', 'C_PHASE'), ('control', 'a33_control_incidence', 'C_INCID'),
]
json.dump({'props': P, 'components': COMPONENTS, 'open': OPEN, 'theorems': THEOREMS},
          open(sys.argv[1] if len(sys.argv) > 1 else 'props33.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(P), 'propositions')
