"""A32's frozen proposition texts. Every statement is assembled from the same components, so the
hypothesis text H and the four-shape text FOUR are literally one string wherever they occur, and the
negative label is the exact negation of the positive one: P_R = ∀ φ, H → FOUR and
P_N = ∃ φ, H ∧ ¬ FOUR."""
import json, sys

TT = "Fin 4 → Matrix (Fin 4) (Fin 4) ℂ"
P1 = "(1 : Equiv.Perm (Fin 4))"
S23 = "Equiv.swap (2 : Fin 4) 3"
S12 = "Equiv.swap (1 : Fin 4) 2"

# act 26's nine circle representatives, in a26_1_circle_count's order; the first is the designated
# (Fourier) circle, and the other eight are R8
R9 = [(P1, P1), (P1, S23), (P1, S12), (S23, P1), (S23, S23), (S23, S12), (S12, P1), (S12, S23),
      (S12, S12)]
R8 = R9[1:]
R8TXT = "[" + ", ".join(f"({a}, {b})" for a, b in R8) + "]"


def F(z):
    """act 23's Fourier tuple at the parameter z, the lambda act 26's statements carry"""
    return ("FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>\n"
            f"        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, {z}, -1, -{z}; 1, -1, 1, -1; 1, -{z}, -1, {z}] p.1 q.1))")


def circ(r, z):
    return f"(fun i => ({F(z)} ({r}.1 i)).submatrix {r}.2 {r}.2)"


HEAD = ("∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →\n"
        f"  ∀ (d : ({TT}) → ({TT}) → ℝ),\n"
        "    d = (fun G H => Real.sqrt (∑ p, ‖mixedTriple G p - mixedTriple H p‖ ^ 2)) →\n")

# act 26's frozen hypotheses (its preregistration L671-675), verbatim, as three conjuncts
H1 = "(∀ G, RealizableGram (Fin 1) Γ₀ G → RealizableGram (Fin 1) Γ₀ (φ G))"
H2 = "(∀ H, RealizableGram (Fin 1) Γ₀ H → ∃ G, RealizableGram (Fin 1) Γ₀ G ∧ GramPhaseEquiv (φ G) H)"
H3 = "(∀ G H, RealizableGram (Fin 1) Γ₀ G → RealizableGram (Fin 1) Γ₀ H → d (φ G) (φ H) = d G H)"
HYP = f"{H1}\n      ∧ {H2}\n      ∧ {H3}"

# act 26's frozen four-shape conclusion (its preregistration L697-710), verbatim
FOUR = """∃ π τ : Equiv.Perm (Fin 4),
          (∀ G, RealizableGram (Fin 1) Γ₀ G →
              GramPhaseEquiv (φ G) (fun i => (G (π i)).submatrix τ τ))
        ∨ (∀ G, RealizableGram (Fin 1) Γ₀ G →
              GramPhaseEquiv (φ G) (fun i => Matrix.of fun j k => star ((G (π i)).submatrix τ τ j k)))
        ∨ (∀ G, RealizableGram (Fin 1) Γ₀ G → ∀ U, AdmissibleDilationAt Γ₀ (0 : Fin 1) U →
              FibreGram (0 : Fin 1) U = G →
              GramPhaseEquiv (φ G) (fun i => (FibreGram (0 : Fin 1) Uᵀ (π i)).submatrix τ τ))
        ∨ (∀ G, RealizableGram (Fin 1) Γ₀ G → ∀ U, AdmissibleDilationAt Γ₀ (0 : Fin 1) U →
              FibreGram (0 : Fin 1) U = G →
              GramPhaseEquiv (φ G) (fun i => Matrix.of fun j k =>
                star ((FibreGram (0 : Fin 1) Uᵀ (π i)).submatrix τ τ j k)))"""

# the witness equations: conjugation of the Fourier parameter on the designated circle, and the
# identity up to GramPhaseEquiv on each of the other eight circles
WIT = ("(∀ G, RealizableGram (Fin 1) Γ₀ G → ∀ z : ℂ, star z * z = 1 →\n"
       f"        GramPhaseEquiv G ({F('z')}) →\n"
       f"        GramPhaseEquiv (φ G) ({F('star z')}))\n"
       f"      ∧ (∀ r ∈ {R8TXT},\n"
       "        ∀ G, RealizableGram (Fin 1) Γ₀ G → ∀ z : ℂ, star z * z = 1 →\n"
       f"        GramPhaseEquiv G {circ('r', 'z')} →\n"
       "        GramPhaseEquiv (φ G) G)")

# the quarter-turn countercontrol's equations: the parameter turned by i on the designated circle,
# and the identity on every class off it
QTR = ("(∀ G, RealizableGram (Fin 1) Γ₀ G → ∀ z : ℂ, star z * z = 1 →\n"
       f"        GramPhaseEquiv G ({F('z')}) →\n"
       f"        GramPhaseEquiv (φ G) ({F('(Complex.I * z)')}))\n"
       "      ∧ (∀ G, RealizableGram (Fin 1) Γ₀ G →\n"
       "        (∀ z : ℂ, star z * z = 1 →\n"
       f"          ¬ GramPhaseEquiv G ({F('z')})) →\n"
       "        GramPhaseEquiv (φ G) G)")

PHI = f"φ : ({TT}) → ({TT})"
GCONJ = f"(fun G : {TT} => fun i => Matrix.of fun j k => star (G i j k))"
GID = f"(fun G : {TT} => G)"

P_R = HEAD + f"  ∀ {PHI},\n    ({HYP}) →\n    ({FOUR})"
P_N = HEAD + f"  ∃ {PHI},\n    ({HYP})\n    ∧ ¬ ({FOUR})"

S_EXIST = HEAD + f"  ∃ {PHI},\n    ({WIT})"
S_ISO = HEAD + f"  ∀ {PHI},\n    ({WIT}) →\n    ({HYP})"
S_SEP = HEAD + f"  ∀ {PHI},\n    ({WIT}) →\n    ¬ ({FOUR})"

S_OVL = (f"∀ r ∈ {R8TXT},\n"
         "  ∀ z w : ℂ, star z * z = 1 → star w * w = 1 →\n"
         f"    GramPhaseEquiv ({F('z')}) {circ('r', 'w')} →\n"
         f"    GramPhaseEquiv ({F('star z')}) ({F('z')})")
S_MOVE = (HEAD + f"  ∀ {PHI},\n    ({WIT}) →\n"
          "    ∃ G, RealizableGram (Fin 1) Γ₀ G ∧ ¬ GramPhaseEquiv (φ G) G")
S_GLOBAL = HEAD + f"  ∀ {PHI}, φ = {GCONJ} →\n    ({HYP})\n    ∧ ({FOUR})"
S_ID = HEAD + f"  ∀ {PHI}, φ = {GID} →\n    ({HYP})\n    ∧ ({FOUR})"
S_QUARTER = (HEAD + f"  (∃ {PHI},\n    ({QTR}))\n"
             f"  ∧ ∀ {PHI},\n    ({QTR}) →\n    ¬ {H3}")

PROPS = {'P_R': P_R, 'P_N': P_N, 'S_EXIST': S_EXIST, 'S_ISO': S_ISO, 'S_SEP': S_SEP,
         'S_OVL': S_OVL, 'S_MOVE': S_MOVE, 'S_GLOBAL': S_GLOBAL, 'S_ID': S_ID,
         'S_QUARTER': S_QUARTER}
COMPONENTS = {'HEAD': HEAD, 'HYP': HYP, 'H3': H3, 'FOUR': FOUR, 'WIT': WIT, 'QTR': QTR,
              'R8': R8TXT, 'PHI': PHI, 'GCONJ': GCONJ, 'GID': GID}
HEADER = 'import OIBridge.OrbitGeometryRigidity\n'
OPEN = ("open Matrix CoherentLiftGauge DilationChoice TwoSidedGauge GramTrajectorySelection\n"
        "  IntermediateCrossTimeStructure RepresentativeNaturality OrbitLawRigidityTwisted\n"
        "  OrbitLawNaturalityFactorization OrbitLawGaps OrbitGeometrySelector OrbitGeometryIsometries\n"
        "  OrbitGeometryRigidity\n")

if __name__ == '__main__':
    # the duality and single-source checks, by construction and asserted
    assert P_R.count(FOUR) == 1 and P_N.count(FOUR) == 1 and P_R.count(HYP) == 1 and P_N.count(HYP) == 1
    assert P_R.replace(f"∀ {PHI}", f"∃ {PHI}").replace(f"({HYP}) →\n    ({FOUR})",
                                                      f"({HYP})\n    ∧ ¬ ({FOUR})") == P_N
    for k in ('S_ISO', 'S_GLOBAL', 'S_ID'):
        assert PROPS[k].count(HYP) == 1, k
    for k in ('S_SEP', 'S_GLOBAL', 'S_ID'):
        assert PROPS[k].count(FOUR) == 1, k
    for k in ('S_EXIST', 'S_ISO', 'S_SEP', 'S_MOVE'):
        assert PROPS[k].count(WIT) == 1, k
    assert S_QUARTER.count(QTR) == 2 and S_QUARTER.count(H3) == 1 and HYP.count(H3) == 1
    assert '\t' not in ''.join(PROPS.values()) and 'Classical' not in ''.join(PROPS.values())
    json.dump({'props': PROPS, 'components': COMPONENTS, 'header': HEADER, 'open': OPEN},
              open(sys.argv[1], 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    for k, v in PROPS.items():
        print(k, len(v), 'chars', v.count('\n') + 1, 'lines')
