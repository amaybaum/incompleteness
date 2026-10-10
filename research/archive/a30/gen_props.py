"""Generate A30's frozen proposition texts (one source for the preregistration, the elaboration
file and controls.py)."""
import json, sys

T1 = "Fin 4 → Matrix (Fin 4) (Fin 4) ℂ"
TP = "Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ"
MP = "Matrix ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ℂ"
A0 = "((0 : Fin 1), (0 : Fin 1))"


def R1(x):
    return f"RealizableGram (Fin 1) Γ₀ {x}"


def RP(x):
    return f"RealizableGram (Fin 1 × Fin 1) (Γ 0) {x}"


CONFIG = (
    "∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →\n"
    "  ∀ (Γ : ℕ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ),\n"
    "    Γ = (fun _ => Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2) →\n")

PAIR = (
    f"  ∀ (f₁ f₂ : ({T1}) → ({T1})),\n"
    f"    (∀ G : {T1}, {R1('G')} → {R1('(f₁ G)')}) →\n"
    f"    (∀ G : {T1}, {R1('G')} → {R1('(f₂ G)')}) →\n"
    f"    (∀ G G' : {T1}, {R1('G')} → {R1(chr(71) + chr(39))} →\n"
    f"      GramPhaseEquiv G G' → GramPhaseEquiv (f₁ G) (f₁ G')) →\n"
    f"    (∀ G G' : {T1}, {R1('G')} → {R1(chr(71) + chr(39))} →\n"
    f"      GramPhaseEquiv G G' → GramPhaseEquiv (f₂ G) (f₂ G')) →\n"
    f"    (∀ G G' : {T1}, {R1('G')} → {R1(chr(71) + chr(39))} →\n"
    f"      GramPhaseEquiv (f₁ G) (f₁ G') → GramPhaseEquiv G G') →\n"
    f"    (∀ G G' : {T1}, {R1('G')} → {R1(chr(71) + chr(39))} →\n"
    f"      GramPhaseEquiv (f₂ G) (f₂ G') → GramPhaseEquiv G G') →\n"
    f"    (∀ G' : {T1}, {R1(chr(71) + chr(39))} →\n"
    f"      ∃ G : {T1}, {R1('G')} ∧ GramPhaseEquiv (f₁ G) G') →\n"
    f"    (∀ G' : {T1}, {R1(chr(71) + chr(39))} →\n"
    f"      ∃ G : {T1}, {R1('G')} ∧ GramPhaseEquiv (f₂ G) G') →\n")

PROD_IN = ("(fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>\n"
           "          G₁ i.1 j.1 k.1 * G₂ i.2 j.2 k.2)")
PROD_OUT = ("(fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>\n"
            "          f₁ G₁ i.1 j.1 k.1 * f₂ G₂ i.2 j.2 k.2)")


def conj37(F, ind):
    """Conjuncts 3 to 7 of the prefix, for the family term F."""
    return (
        f"EvolvesTotally (Fin 1 × Fin 1) Γ {F}\n"
        f"{ind}∧ PreservesAdmissible (Fin 1 × Fin 1) Γ {F}\n"
        f"{ind}∧ (∃ Φh : ({TP}) → ({TP}), ∀ t : ℕ, {F} t = Φh)\n"
        f"{ind}∧ Reversible (Fin 1 × Fin 1) Γ {F}\n"
        f"{ind}∧ (∀ (t : ℕ) (G G' : {TP}),\n"
        f"{ind}    GramPhaseEquiv G G' → GramPhaseEquiv ({F} t G) ({F} t G'))")


def factor(F, ind):
    return (f"FactorizesOnProduct (Fin 1 × Fin 1) (Fin 1) (Fin 1) (Equiv.refl (Fin 4 × Fin 4))\n"
            f"{ind}    (fun _ => Γ₀) (fun _ => Γ₀) Γ {F}")


def pairclause(F, ind):
    return (f"(∀ (t : ℕ) (G₁ G₂ : {T1}), {R1('G₁')} → {R1('G₂')} →\n"
            f"{ind}    GramPhaseEquiv ({F} t {PROD_IN})\n"
            f"{ind}      {PROD_OUT})")


def c8(F, ind):
    return (f"(∀ t : ℕ, ∃ Ψ αL αR : {MP} → {MP},\n"
            f"{ind}    (∀ U : {MP}, AdmissibleDilationAt (Γ t) {A0} U →\n"
            f"{ind}      FibreGram {A0} (Ψ U) = {F} t (FibreGram {A0} U))\n"
            f"{ind}    ∧ (∀ U : {MP}, AdmissibleDilationAt (Γ t) {A0} U →\n"
            f"{ind}      AdmissibleDilationAt (Γ (t + 1)) {A0} (Ψ U))\n"
            f"{ind}    ∧ TwistedNatural {A0} αL αR Ψ)")


def elig(F, ind):
    return (f"{conj37(F, ind)}\n{ind}∧ {factor(F, ind)}\n{ind}∧ {pairclause(F, ind)}")


LAW = (f"(fun 𝔾 : ℕ → {TP} =>\n"
       f"        ∀ t : ℕ, GramPhaseEquiv (𝔾 (t + 1)) (Φ t (𝔾 t)))")

P_S = (CONFIG +
       f"  ∀ (Φ₀ : ({TP}) → ({TP})),\n"
       f"    (∀ G : {TP}, {RP('G')} → {RP('(Φ₀ G)')}) →\n"
       f"    (∀ G G' : {TP}, {RP('G')} → {RP(chr(71) + chr(39))} →\n"
       f"      GramPhaseEquiv G G' → GramPhaseEquiv (Φ₀ G) (Φ₀ G')) →\n"
       f"    ∃ (Φ₁ : ({TP}) → ({TP})) (Ψ : {MP} → {MP}),\n"
       f"      (∀ G : {TP}, {RP('G')} → GramPhaseEquiv (Φ₁ G) (Φ₀ G))\n"
       f"      ∧ (∀ G : {TP}, ¬ {RP('G')} → Φ₁ G = Φ₀ G)\n"
       f"      ∧ (∀ G : {TP}, {RP('G')} → {RP('(Φ₁ G)')})\n"
       f"      ∧ (∀ U : {MP}, AdmissibleDilationAt (Γ 0) {A0} U →\n"
       f"          FibreGram {A0} (Ψ U) = Φ₁ (FibreGram {A0} U))\n"
       f"      ∧ (∀ U : {MP}, AdmissibleDilationAt (Γ 0) {A0} U →\n"
       f"          AdmissibleDilationAt (Γ 0) {A0} (Ψ U))\n"
       f"      ∧ StrictNatural {A0} Ψ")

F0 = "(fun _ : ℕ => Φ₀)"
F1 = "(fun _ : ℕ => Φ₁)"
P_T = (CONFIG + PAIR +
       f"  ∀ (Φ₀ Φ₁ : ({TP}) → ({TP})),\n"
       f"    (∀ G : {TP}, {RP('G')} → GramPhaseEquiv (Φ₁ G) (Φ₀ G)) →\n"
       f"    (∀ G : {TP}, ¬ {RP('G')} → Φ₁ G = Φ₀ G) →\n"
       f"    ({elig(F0, '      ')}) →\n"
       f"    ({elig(F1, '      ')})")

P_N = (CONFIG + PAIR +
       f"  ∃ Φ : ℕ → ({TP}) → ({TP}),\n"
       f"    {elig('Φ', '    ')}\n"
       f"    ∧ {c8('Φ', '    ')}")

P_0 = (CONFIG + PAIR +
       f"  ∃ Φ : ℕ → ({TP}) → ({TP}),\n"
       f"    ProperAt {A0} Γ\n"
       f"      {LAW}\n"
       f"    ∧ PropagatesFrom {A0} Γ\n"
       f"      {LAW}\n"
       f"    ∧ {conj37('Φ', '    ')}\n"
       f"    ∧ {c8('Φ', '    ')}\n"
       f"    ∧ {factor('Φ', '    ')}\n"
       f"    ∧ {pairclause('Φ', '    ')}")

PROPS = {'P_S': P_S, 'P_T': P_T, 'P_N': P_N, 'P_0': P_0}

HEADER = (
    "import OIBridge.ProductAdmission\n")
OPEN = ("open Matrix DilationChoice CoherentLiftGauge TwoSidedGauge GramTrajectorySelection\n"
        "  IntermediateCrossTimeStructure RepresentativeNaturality OrbitLawRigidityTwisted OrbitLawGaps\n"
        "  OrbitGeometryIsometries StrictNaturalLift ProductLocusFreedom ProductAdmission\n")

if __name__ == '__main__':
    out = sys.argv[1]
    json.dump({'props': PROPS, 'header': HEADER, 'open': OPEN}, open(out, 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)
    for k, v in PROPS.items():
        print(k, len(v), 'chars', v.count('\n') + 1, 'lines')
