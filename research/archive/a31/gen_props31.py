"""A31's frozen proposition texts, built from the same components act 30 used, so that the two
verdict propositions are duals by construction."""
import json, sys
sys.path.insert(0, '../a30')
import gen_props as g

T1, TP, MP, A0 = g.T1, g.TP, g.MP, g.A0
R1, RP = g.R1, g.RP

PAIR = (f"  ∀ (f₁ f₂ : ({T1}) → ({T1})), f₁ = RelabelTransition (Equiv.swap (2 : Fin 4) 3) →\n"
        f"    f₂ = (fun G => G) →\n")


def law(F):
    return (f"(fun 𝔾 : ℕ → {TP} =>\n"
            f"        ∀ t : ℕ, GramPhaseEquiv (𝔾 (t + 1)) ({F} t (𝔾 t)))")


def admitted(F, ind):
    """Full admission of the family F: act 30's P_0 body with F substituted."""
    return (f"ProperAt {A0} Γ\n{ind}  {law(F)}\n"
            f"{ind}∧ PropagatesFrom {A0} Γ\n{ind}  {law(F)}\n"
            f"{ind}∧ {g.conj37(F, ind)}\n"
            f"{ind}∧ {g.c8(F, ind)}\n"
            f"{ind}∧ {g.factor(F, ind)}\n"
            f"{ind}∧ {g.pairclause(F, ind)}")


def off(G):
    return (f"(∀ X Y : {T1}, {R1('X')} → {R1('Y')} →\n"
            f"      ¬ GramPhaseEquiv (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>\n"
            f"        X i.1 j.1 k.1 * Y i.2 j.2 k.2) {G})")


def locus(G):
    return (f"(∃ X Y : {T1}, {R1('X')} ∧ {R1('Y')} ∧\n"
            f"      GramPhaseEquiv (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>\n"
            f"        X i.1 j.1 k.1 * Y i.2 j.2 k.2) {G})")


A_PHI = admitted('Φ', '      ')
A_PHI2 = admitted("Φ'", '      ')
EQ = "GramPhaseEquiv (Φ 0 G) (Φ' 0 G)"
HEAD = g.CONFIG + PAIR

P_N = (HEAD +
       f"  ∃ Φ Φ' : ℕ → ({TP}) → ({TP}),\n"
       f"    ({A_PHI})\n"
       f"    ∧ ({A_PHI2})\n"
       f"    ∧ ∃ G : {TP}, {RP('G')}\n"
       f"      ∧ {off('G')}\n"
       f"      ∧ ¬ {EQ}")

P_U = (HEAD +
       f"  ∀ Φ Φ' : ℕ → ({TP}) → ({TP}),\n"
       f"    ({A_PHI}) →\n"
       f"    ({A_PHI2}) →\n"
       f"    ∀ G : {TP}, {RP('G')} →\n"
       f"      {off('G')} →\n"
       f"      {EQ}")

H1 = ("Matrix.of (fun p q : Fin 4 × Fin 1 =>\n"
      "      (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, 1, -1; 1, -1, -1, 1] p.1 q.1)")
HI = ("Matrix.of (fun p q : Fin 4 × Fin 1 =>\n"
      "      (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1;\n"
      "        1, -Complex.I, -1, Complex.I] p.1 q.1)")
TAU0 = "Equiv.swap ((0 : Fin 4), (1 : Fin 4)) ((1 : Fin 4), (0 : Fin 4))"

S_W = (g.CONFIG +
       f"  ∀ X Y : {T1}, X = FibreGram (0 : Fin 1) ({H1}) →\n"
       f"    Y = FibreGram (0 : Fin 1) ({HI}) →\n"
       f"  ∀ W W₂ : {TP},\n"
       f"    W = RelabelTransition ({TAU0})\n"
       f"      (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => X i.1 j.1 k.1 * Y i.2 j.2 k.2) →\n"
       f"    W₂ = RelabelTransition ({TAU0})\n"
       f"      (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>\n"
       f"        X i.1 j.1 k.1 * RelabelTransition (Equiv.swap (2 : Fin 4) 3) Y i.2 j.2 k.2) →\n"
       f"    {RP('W')} ∧ {RP('W₂')}\n"
       f"    ∧ {off('W')}\n"
       f"    ∧ {off('W₂')}\n"
       f"    ∧ ¬ GramPhaseEquiv W W₂")

TAUPROPS = [
    f"(∀ G : {TP}, {RP('G')} → {RP('(τ G)')})",
    f"(∀ G G' : {TP}, GramPhaseEquiv G G' → GramPhaseEquiv (τ G) (τ G'))",
    f"(∀ G : {TP}, GramPhaseEquiv (τ (τ G)) G)",
    f"(∀ G : {TP}, {locus('G')} → τ G = G)",
]

S_TAU = (g.CONFIG +
         f"  ∀ W W₂ : {TP}, {RP('W')} → {RP('W₂')} →\n"
         f"    {off('W')} →\n"
         f"    {off('W₂')} →\n"
         f"    ¬ GramPhaseEquiv W W₂ →\n"
         f"  ∃ τ : ({TP}) → ({TP}),\n"
         f"    {TAUPROPS[0]}\n"
         f"    ∧ {TAUPROPS[1]}\n"
         f"    ∧ {TAUPROPS[2]}\n"
         f"    ∧ {TAUPROPS[3]}\n"
         f"    ∧ GramPhaseEquiv (τ W) W₂")

FPRE = "(fun (t : ℕ) (G : " + TP + ") => Φ t (τ G))"
S_PRE = (HEAD +
         f"  ∀ Φ : ℕ → ({TP}) → ({TP}),\n"
         f"    ({g.elig('Φ', '      ')}) →\n"
         f"  ∀ τ : ({TP}) → ({TP}),\n"
         f"    {TAUPROPS[0]} →\n"
         f"    {TAUPROPS[1]} →\n"
         f"    {TAUPROPS[2]} →\n"
         f"    {TAUPROPS[3]} →\n"
         f"    ({g.elig(FPRE, '      ')})")

PROPS = {'P_N': P_N, 'P_U': P_U, 'S_W': S_W, 'S_TAU': S_TAU, 'S_PRE': S_PRE}
COMPONENTS = {'HEAD': HEAD, 'A_PHI': A_PHI, 'A_PHI2': A_PHI2, 'RPG': RP('G'), 'OFFG': off('G'),
              'EQ': EQ, 'TP': TP}
HEADER = 'import OIBridge.ProductStrictLift\n'
OPEN = ("open Matrix DilationChoice CoherentLiftGauge TwoSidedGauge GramTrajectorySelection\n"
        "  IntermediateCrossTimeStructure RepresentativeNaturality OrbitLawRigidityTwisted OrbitLawGaps\n"
        "  OrbitGeometryIsometries StrictNaturalLift ProductLocusFreedom ProductAdmission ProductStrictLift\n")
if __name__ == '__main__':
    json.dump({'props': PROPS, 'components': COMPONENTS, 'header': HEADER, 'open': OPEN},
              open(sys.argv[1], 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    for k, v in PROPS.items():
        print(k, len(v), 'chars', v.count('\n') + 1, 'lines')
