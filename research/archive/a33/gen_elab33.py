"""A33 pre-freeze: the elaboration file -- the candidate frozen propositions as `#check`s, nothing else.
Output: OIBridge/OrbitIsometryGroup.lean text on stdout."""
import sys

E = "EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4))"
T = "Fin 4 → Matrix (Fin 4) (Fin 4) ℂ"
FZ = lambda z: ("FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>\n"
                f"        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, {z}, -1, -{z}; 1, -1, 1, -1; 1, -{z}, -1, {z}] p.1 q.1))")
P1, S23, S12 = "(1 : Equiv.Perm (Fin 4))", "Equiv.swap (2 : Fin 4) 3", "Equiv.swap (1 : Fin 4) 2"
R9 = [(P1, P1), (P1, S23), (P1, S12), (S23, P1), (S23, S23), (S23, S12), (S12, P1), (S12, S23), (S12, S12)]
RTXT = "![" + ", ".join(f"({a}, {b})" for a, b in R9) + "]"
V1, V2 = "![0, 2, 4, 2, 0, 3, 4, 5, 0]", "![1, 3, 5, 5, 4, 1, 3, 1, 2]"

CONFIG = ("∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →\n"
          f"  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := {RTXT}\n"
          f"  let pt : Fin 9 → ℂ → {E} := fun r z => featureVec (fun i =>\n"
          f"    ({FZ('z')} ((R r).1 i)).submatrix (R r).2 (R r).2)\n"
          f"  let v₁ : Fin 9 → Fin 6 := {V1}\n"
          f"  let v₂ : Fin 9 → Fin 6 := {V2}\n")
EDGE = ("(∀ r : Fin 9, ∃ s : Fin 9, (ν (v₁ r) = v₁ s ∧ ν (v₂ r) = v₂ s) ∨ (ν (v₁ r) = v₂ s ∧ ν (v₂ r) = v₁ s))")
def NF(f, nu, ep):
    return (f"(∀ r : Fin 9, ∃ s : Fin 9, ({nu} (v₁ r) = v₁ s ∧ {nu} (v₂ r) = v₂ s) ∨ ({nu} (v₁ r) = v₂ s ∧ {nu} (v₂ r) = v₁ s))\n"
            f"    ∧ (∀ r s : Fin 9, {nu} (v₁ r) = v₁ s → {nu} (v₂ r) = v₂ s → ∀ z : ℂ, star z * z = 1 →\n"
            f"        {f} (pt r z) = pt s (if {ep} r then z else star z))\n"
            f"    ∧ (∀ r s : Fin 9, {nu} (v₁ r) = v₂ s → {nu} (v₂ r) = v₁ s → ∀ z : ℂ, star z * z = 1 →\n"
            f"        {f} (pt r z) = pt s (-(if {ep} r then z else star z)))")
SURJ = "IsSurjIsometryOn (normalizedSet Γ₀) f"
DEG = lambda v, ep: f"((Finset.univ.filter (fun r : Fin 9 => (v₁ r = {v} ∨ v₂ r = {v}) ∧ {ep} r = false)).card % 2)"
FAM = (f"(∃ π τ : Equiv.Perm (Fin 4),\n"
       f"      (∀ G : {T}, RealizableGram (Fin 1) Γ₀ G → f (featureVec G) = featureVec (fun i => (G (π i)).submatrix τ τ))\n"
       f"      ∨ (∀ G : {T}, RealizableGram (Fin 1) Γ₀ G →\n"
       f"          f (featureVec G) = featureVec (fun i => Matrix.of fun j k => star ((G (π i)).submatrix τ τ j k)))\n"
       f"      ∨ (∀ G : {T}, RealizableGram (Fin 1) Γ₀ G → ∀ U, AdmissibleDilationAt Γ₀ (0 : Fin 1) U →\n"
       f"          FibreGram (0 : Fin 1) U = G → f (featureVec G) = featureVec (fun i => (FibreGram (0 : Fin 1) Uᵀ (π i)).submatrix τ τ))\n"
       f"      ∨ (∀ G : {T}, RealizableGram (Fin 1) Γ₀ G → ∀ U, AdmissibleDilationAt Γ₀ (0 : Fin 1) U →\n"
       f"          FibreGram (0 : Fin 1) U = G → f (featureVec G) = featureVec (fun i => Matrix.of fun j k =>\n"
       f"            star ((FibreGram (0 : Fin 1) Uᵀ (π i)).submatrix τ τ j k))))")

props = {}
# ---- A33-1: the classification, both directions
props['P_R'] = CONFIG + (
    f"  (∀ f : {E} → {E}, {SURJ} →\n"
    f"      ∃! νε : Equiv.Perm (Fin 6) × (Fin 9 → Bool),\n    " + NF('f', 'νε.1', 'νε.2') + ")\n"
    f"  ∧ (∀ (ν : Equiv.Perm (Fin 6)) (ε : Fin 9 → Bool),\n      {EDGE} →\n"
    f"      ∃ f : {E} → {E}, {SURJ} ∧\n    " + NF('f', 'ν', 'ε') + ")")
props['P_N'] = "¬ (" + props['P_R'] + ")"
# ---- A33-2: the old family inside the kernel and its cosets
props['PAR_K'] = CONFIG + (
    f"  ∀ f : {E} → {E}, {SURJ} → ∀ ε : Fin 9 → Bool,\n    " + NF('f', '(1 : Equiv.Perm (Fin 6))', 'ε') + " →\n"
    f"    ({FAM} ↔ ∀ v w : Fin 6, {DEG('v', 'ε')} = {DEG('w', 'ε')})")
props['PAR_COUNT'] = (
    f"  let v₁ : Fin 9 → Fin 6 := {V1}\n  let v₂ : Fin 9 → Fin 6 := {V2}\n"
    f"  (Finset.univ.filter (fun ε : Fin 9 → Bool => ∀ v w : Fin 6, {DEG('v', 'ε')} = {DEG('w', 'ε')})).card = 32")
EPSPROD = "(fun r => decide (ε r = ε' r))"
props['PAR_COSET'] = CONFIG + (
    f"  ∀ (ν : Equiv.Perm (Fin 6)) (ε ε' : Fin 9 → Bool) (f f' : {E} → {E}), {SURJ} → IsSurjIsometryOn (normalizedSet Γ₀) f' →\n    "
    + NF('f', 'ν', 'ε') + " →\n    " + NF("f'", 'ν', "ε'") + " →\n"
    f"    {FAM} →\n    ({FAM.replace('f (featureVec G)', chr(102)+chr(39)+' (featureVec G)')} ↔\n"
    f"      ∀ v w : Fin 6, {DEG('v', EPSPROD)} = {DEG('w', EPSPROD)})")
props['PAR_ONTO'] = CONFIG + (
    f"  ∀ ν : Equiv.Perm (Fin 6), {EDGE} → ∃ (ε : Fin 9 → Bool) (f : {E} → {E}), {SURJ} ∧ {FAM} ∧\n    " + NF('f', 'ν', 'ε'))
# ---- A33-3: the composition law (the semidirect structure in coordinates) and the finite facts
props['COMP'] = CONFIG + (
    f"  ∀ (ν ν' : Equiv.Perm (Fin 6)) (ε ε' : Fin 9 → Bool) (f f' : {E} → {E}), {SURJ} → IsSurjIsometryOn (normalizedSet Γ₀) f' →\n    "
    + NF('f', 'ν', 'ε') + " →\n    " + NF("f'", "ν'", "ε'") + " →\n"
    f"    ∀ ε'' : Fin 9 → Bool, (∀ r s : Fin 9, (ν' (v₁ r) = v₁ s ∧ ν' (v₂ r) = v₂ s) ∨ (ν' (v₁ r) = v₂ s ∧ ν' (v₂ r) = v₁ s) →\n"
    f"        ε'' r = decide (ε' r = ε s)) →\n    " + NF("(f ∘ f')", "(ν * ν')", "ε''"))
FIN = f"  let v₁ : Fin 9 → Fin 6 := {V1}\n  let v₂ : Fin 9 → Fin 6 := {V2}\n"
AUT = "(Finset.univ.filter (fun ν : Equiv.Perm (Fin 6) => ∀ r : Fin 9, ∃ s : Fin 9, (ν (v₁ r) = v₁ s ∧ ν (v₂ r) = v₂ s) ∨ (ν (v₁ r) = v₂ s ∧ ν (v₂ r) = v₁ s)))"
props['FIN_ORDER'] = FIN + f"  {AUT}.card = 72"
props['FIN_TRANS_CIRCLES'] = FIN + (f"  ∀ r s : Fin 9, ∃ ν ∈ {AUT}, (ν (v₁ r) = v₁ s ∧ ν (v₂ r) = v₂ s) ∨ (ν (v₁ r) = v₂ s ∧ ν (v₂ r) = v₁ s)")
props['FIN_STAB_CIRCLE'] = FIN + (f"  ({AUT}.filter (fun ν => (ν (v₁ 0) = v₁ 0 ∧ ν (v₂ 0) = v₂ 0) ∨ (ν (v₁ 0) = v₂ 0 ∧ ν (v₂ 0) = v₁ 0))).card = 8")
props['FIN_TRANS_POINTS'] = FIN + f"  ∀ v w : Fin 6, ∃ ν ∈ {AUT}, ν v = w"
props['FIN_STAB_POINT'] = FIN + f"  ({AUT}.filter (fun ν => ν 0 = 0)).card = 12"
# ---- the bridge lemmas B1-B3
props['B1_CIRCLES'] = CONFIG + (
    f"  ∀ g : {E} ≃ᵃⁱ[ℝ] {E}, g '' normalizedSet Γ₀ = normalizedSet Γ₀ →\n"
    f"    ∀ r : Fin 9, ∃ s : Fin 9, g '' (pt r '' {{z : ℂ | star z * z = 1}}) = pt s '' {{z : ℂ | star z * z = 1}}")
props['B2_FORM'] = CONFIG + (
    f"  ∀ g : {E} ≃ᵃⁱ[ℝ] {E}, ∀ r s : Fin 9, g '' (pt r '' {{z : ℂ | star z * z = 1}}) = pt s '' {{z : ℂ | star z * z = 1}} →\n"
    f"    ∃ (l : ℂ) (ε : Bool), star l * l = 1 ∧ ∀ z : ℂ, star z * z = 1 → g (pt r z) = pt s (l * (if ε then z else star z))")
props['B3_SIGNS'] = CONFIG + (
    f"  ∀ f : {E} → {E}, {SURJ} → ∀ (σ : Fin 9 → Fin 9) (l : Fin 9 → ℂ) (ε : Fin 9 → Bool),\n"
    f"    (∀ r, star (l r) * l r = 1) → (∀ r, ∀ z : ℂ, star z * z = 1 → f (pt r z) = pt (σ r) (l r * (if ε r then z else star z))) →\n"
    f"    ∀ r, l r = 1 ∨ l r = -1")
# ---- controls
props['C_ID'] = CONFIG + f"  " + NF("(id : {E} → {E})".replace("{E}", E), "(1 : Equiv.Perm (Fin 6))", "(fun _ => true)")
props['C_CONJ'] = CONFIG + (f"  ∃ f : {E} → {E}, {SURJ} ∧\n    " + NF('f', '(1 : Equiv.Perm (Fin 6))', '(fun _ => false)'))
props['C_A32'] = CONFIG + (f"  ∃ f : {E} → {E}, {SURJ} ∧ ¬ {FAM} ∧\n    " + NF('f', '(1 : Equiv.Perm (Fin 6))', '(fun r => decide (r ≠ 0))'))
props['C_N1_LAMBDA'] = CONFIG + (
    "  dist (pt 0 (Complex.I * Complex.I)) (pt 4 Complex.I) ≠ dist (pt 0 Complex.I) (pt 4 Complex.I)")
props['C_N2_TRANSPOSITION'] = CONFIG + (
    f"  (∀ z w : ℂ, star z * z = 1 → star w * w = 1 → 1 ≤ dist (pt 0 z) (pt 3 w))\n"
    f"  ∧ pt 1 1 = pt 3 1\n"
    f"  ∧ ¬ ∃ f : {E} → {E}, {SURJ} ∧ f '' (pt 0 '' {{z : ℂ | star z * z = 1}}) = pt 1 '' {{z : ℂ | star z * z = 1}}\n"
    f"      ∧ f '' (pt 3 '' {{z : ℂ | star z * z = 1}}) = pt 3 '' {{z : ℂ | star z * z = 1}}")
# ---- an API probe for the structural corollary, kept apart: does SemidirectProduct elaborate here?
props['API_SEMIDIRECT'] = ("∀ (φ : Equiv.Perm (Fin 6) →* MulAut (Fin 9 → ℤˣ)),\n"
                           "  Nonempty ((Fin 9 → ℤˣ) ⋊[φ] Equiv.Perm (Fin 6))")
props['API_ISOMETRY_EQUIV'] = ("∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ),\n"
                               "  Nonempty ((normalizedSet Γ₀) ≃ᵢ (normalizedSet Γ₀))")

out = ["import OIBridge.OrbitGeometryRigidity", "import Mathlib.GroupTheory.SemidirectProduct", "", "/-! Act 33 — elaboration of the candidate frozen propositions. Design evidence before any freeze:",
       "every `#check` below must elaborate; nothing is proved and nothing is defined. -/", "",
       "namespace OIBridge", "namespace OrbitIsometryGroup", "",
       "open Matrix CoherentLiftGauge DilationChoice TwoSidedGauge GramTrajectorySelection",
       "  IntermediateCrossTimeStructure RepresentativeNaturality OrbitLawRigidityTwisted",
       "  OrbitLawNaturalityFactorization OrbitLawGaps OrbitGeometrySelector OrbitGeometryIsometries",
       "  OrbitGeometryRigidity", "open scoped InnerProductSpace", ""]
for k, v in props.items():
    out += [f"-- {k}", f"#check (\n  {v}\n  : Prop)", ""]
out += ["end OrbitIsometryGroup", "end OIBridge", ""]
sys.stdout.write("\n".join(out))
