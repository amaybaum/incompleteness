"""Generates the S_SEP timing-rehearsal module: the frozen S_SEP statement proved through
exponent tables decided over Perm (Fin 4) x Perm (Fin 4). Disposable design evidence."""
import json, sys

d = json.load(open('props32.json', encoding='utf-8'))
P = d['props']
covers = {int(k): v for k, v in json.load(open('covers.json')).items()}

T = "Fin 4 → Matrix (Fin 4) (Fin 4) ℂ"
P1 = "(1 : Equiv.Perm (Fin 4))"
S23 = "Equiv.swap (2 : Fin 4) 3"
S12 = "Equiv.swap (1 : Fin 4) 2"
R9 = [(P1, P1), (P1, S23), (P1, S12), (S23, P1), (S23, S23), (S23, S12), (S12, P1), (S12, S23),
      (S12, S12)]
R8TXT = "[" + ", ".join(f"({a}, {b})" for a, b in R9[1:]) + "]"
TAB = "(![![0, 0, 0, 0], ![0, 1, 2, 3], ![0, 2, 0, 2], ![0, 3, 2, 1]] : Fin 4 → Fin 4 → ℕ)"


def FZ(z):
    return ("FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 => (1 / 2 : ℂ) * "
            f"!![1, 1, 1, 1; 1, {z}, -1, -{z}; 1, -1, 1, -1; 1, -{z}, -1, {z}] p.1 q.1))")


def EXP(i, j, k):
    return f"({TAB} ({i}) ({k}) + 4 - {TAB} ({i}) ({j}))"


def NQ(a1, a2, a3, b1, b2, b3):
    return f"({EXP(a1, b1, b2)} + {EXP(a2, b2, b3)} + {EXP(a3, b3, b1)})"


def proj(q):
    return (f"{q}.1.1", f"{q}.1.2.1", f"{q}.1.2.2", f"{q}.2.1", f"{q}.2.2.1", f"{q}.2.2.2")


def pt(p):
    """the tuple indices of p as Lean terms"""
    return proj(p)


def relab(r1, r2, idx):
    a1, a2, a3, b1, b2, b3 = idx
    return (f"{r1} ({a1})", f"{r1} ({a2})", f"{r1} ({a3})", f"{r2} ({b1})", f"{r2} ({b2})", f"{r2} ({b3})")


def sw(idx):
    a1, a2, a3, b1, b2, b3 = idx
    return (b2, b3, b1, a1, a2, a3)


def lhs(shape, r, idx):
    """the exponent the shape side carries at the index tuple idx (before the test circle r)"""
    q = idx if shape in (1, 2) else sw(idx)
    if r is not None:
        q = relab(r[0], r[1], q)
    n = NQ(*q)
    return n if shape in (1, 4) else f"(3 * {n})"


def rhs(r, idx):
    if r is None:
        return f"(3 * {NQ(*idx)})"
    return NQ(*relab(r[0], r[1], idx))


HX = "  have hx : ∀ y : Fin 1, y = 0 := fun y => Subsingleton.elim y 0\n"
HI = ("  have hI : star Complex.I * Complex.I = 1 := by\n"
      "    rw [Complex.star_def, Complex.conj_I, neg_mul, Complex.I_mul_I, neg_neg]\n")
ENTRY_TAC = """  intro i j k
  rw [fibreGram_unique (0 : Fin 1) hx]
  fin_cases i <;> fin_cases j <;> fin_cases k <;>
    norm_num [Matrix.of_apply, Complex.ext_iff, pow_succ, Complex.star_def, Complex.conj_I]
"""

out = [d['header'], "/-!\n# Act 32 — S_SEP timing rehearsal (disposable, never landed)\n-/\n",
       'namespace OIBridge', 'namespace OrbitIsometryClassification', '', d['open']]


def thm(name, stmt, proof):
    out.append(f"theorem {name} :\n    {stmt} := by\n{proof.rstrip()}\n\n#print axioms {name}\n")


thm('a32_shared_entry_I', f"∀ i j k : Fin 4, {FZ('Complex.I')} i j k = Complex.I ^ {EXP('i', 'j', 'k')} / 4",
    HX + ENTRY_TAC)
thm('a32_shared_entry_starI',
    f"∀ i j k : Fin 4, {FZ('star Complex.I')} i j k = Complex.I ^ (3 * {EXP('i', 'j', 'k')}) / 4",
    HX + ENTRY_TAC)
thm('a32_shared_pow3', "∀ a b c : ℕ, Complex.I ^ a / 4 * (Complex.I ^ b / 4) * (Complex.I ^ c / 4) = "
    "Complex.I ^ (a + b + c) / 64", "  intro a b c\n  rw [pow_add, pow_add]\n  ring\n")
thm('a32_shared_pow3s', "∀ a b c : ℕ, Complex.I ^ (3 * a) / 4 * (Complex.I ^ (3 * b) / 4) * "
    "(Complex.I ^ (3 * c) / 4) = Complex.I ^ (3 * (a + b + c)) / 64",
    "  intro a b c\n  rw [mul_add, mul_add, pow_add, pow_add]\n  ring\n")
Q = "((i₁, i₂, i₃), (j₁, j₂, j₃))"
thm('a32_shared_value_I',
    f"∀ q : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4), mixedTriple ({FZ('Complex.I')}) q = "
    f"Complex.I ^ {NQ(*proj('q'))} / 64",
    "  intro q\n  obtain ⟨⟨i₁, i₂, i₃⟩, ⟨j₁, j₂, j₃⟩⟩ := q\n"
    "  simp only [mixedTriple, a32_shared_entry_I]\n  exact a32_shared_pow3 _ _ _\n")
thm('a32_shared_value_starI',
    f"∀ q : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4), mixedTriple ({FZ('star Complex.I')}) q = "
    f"Complex.I ^ (3 * {NQ(*proj('q'))}) / 64",
    "  intro q\n  obtain ⟨⟨i₁, i₂, i₃⟩, ⟨j₁, j₂, j₃⟩⟩ := q\n"
    "  simp only [mixedTriple, a32_shared_entry_starI]\n  exact a32_shared_pow3s _ _ _\n")
thm('a32_shared_star_pow', "∀ n : ℕ, star (Complex.I ^ n / 64) = Complex.I ^ (3 * n) / 64",
    "  intro n\n  have h3 : Complex.I ^ 3 = -Complex.I := by\n    rw [pow_succ, Complex.I_sq]\n    ring\n"
    "  rw [star_div₀, star_pow, star_ofNat, Complex.star_def, Complex.conj_I, ← h3, ← pow_mul]\n")
thm('a32_shared_pow_mod', "∀ a b : ℕ, Complex.I ^ a / 64 = Complex.I ^ b / 64 → a % 4 = b % 4", """
  intro a b h
  have h64 : (64 : ℂ) ≠ 0 := by norm_num
  have h' : Complex.I ^ a = Complex.I ^ b := (div_left_inj' h64).mp h
  have h4 : Complex.I ^ 4 = 1 := by
    rw [show (4 : ℕ) = 2 * 2 from rfl, pow_mul, Complex.I_sq]
    norm_num
  have hm : ∀ n : ℕ, Complex.I ^ n = Complex.I ^ (n % 4) := fun n => by
    conv_lhs => rw [← Nat.div_add_mod n 4, pow_add, pow_mul, h4, one_pow, one_mul]
  have key : ∀ x y : ℕ, x < 4 → y < 4 → Complex.I ^ x = Complex.I ^ y → x = y := by
    intro x y hx hy hxy
    interval_cases x <;> interval_cases y <;>
      first | rfl | (exfalso; norm_num [Complex.ext_iff, pow_succ] at hxy)
  exact key _ _ (Nat.mod_lt _ (by norm_num)) (Nat.mod_lt _ (by norm_num)) (by rw [← hm a, ← hm b]; exact h')
""")

# the two conversions of the conjugated and transposed shapes
thm('a32_shared_star_relabel',
    f"∀ (π τ : Equiv.Perm (Fin 4)) (G : {T}) (p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)), "
    "mixedTriple (fun i => Matrix.of fun j k => star ((G (π i)).submatrix τ τ j k)) p = "
    "star (mixedTriple G ((π p.1.1, π p.1.2.1, π p.1.2.2), (τ p.2.1, τ p.2.2.1, τ p.2.2.2)))",
    "  intro π τ G p\n  obtain ⟨⟨i₁, i₂, i₃⟩, ⟨j₁, j₂, j₃⟩⟩ := p\n"
    "  simp only [mixedTriple, Matrix.of_apply, Matrix.submatrix_apply, star_mul']\n")
thm('a32_shared_transpose_relabel',
    "∀ (π τ : Equiv.Perm (Fin 4)) (U : Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ) "
    "(p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)), "
    "mixedTriple (fun i => (FibreGram (0 : Fin 1) Uᵀ (π i)).submatrix τ τ) p = "
    "star (mixedTriple (FibreGram (0 : Fin 1) U) ((τ p.2.2.1, τ p.2.2.2, τ p.2.1), (π p.1.1, π p.1.2.1, π p.1.2.2)))",
    HX + "  intro π τ U p\n  rw [mixedTriple_relabel2, mixedTriple_transpose (0 : Fin 1) hx (0 : Fin 1) U]\n")
thm('a32_shared_transpose_star_relabel',
    "∀ (π τ : Equiv.Perm (Fin 4)) (U : Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ) "
    "(p : (Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)), "
    "mixedTriple (fun i => Matrix.of fun j k => star ((FibreGram (0 : Fin 1) Uᵀ (π i)).submatrix τ τ j k)) p = "
    "mixedTriple (FibreGram (0 : Fin 1) U) ((τ p.2.2.1, τ p.2.2.2, τ p.2.1), (π p.1.1, π p.1.2.1, π p.1.2.2))",
    HX + "  intro π τ U p\n  rw [a32_shared_star_relabel, mixedTriple_transpose (0 : Fin 1) hx (0 : Fin 1) U, star_star]\n")

HW1 = (f"(∀ G, RealizableGram (Fin 1) Γ₀ G → ∀ z : ℂ, star z * z = 1 → GramPhaseEquiv G ({FZ('z')}) → "
       f"GramPhaseEquiv (φ G) ({FZ('star z')}))")
HW2 = (f"(∀ r ∈ {R8TXT}, ∀ G, RealizableGram (Fin 1) Γ₀ G → ∀ z : ℂ, star z * z = 1 → "
       f"GramPhaseEquiv G (fun i => ({FZ('z')} (r.1 i)).submatrix r.2 r.2) → GramPhaseEquiv (φ G) G)")
SH = {
    1: "(∀ G, RealizableGram (Fin 1) Γ₀ G → GramPhaseEquiv (φ G) (fun i => (G (π i)).submatrix τ τ))",
    2: "(∀ G, RealizableGram (Fin 1) Γ₀ G → GramPhaseEquiv (φ G) (fun i => Matrix.of fun j k => star ((G (π i)).submatrix τ τ j k)))",
    3: ("(∀ G, RealizableGram (Fin 1) Γ₀ G → ∀ U, AdmissibleDilationAt Γ₀ (0 : Fin 1) U → FibreGram (0 : Fin 1) U = G → "
        "GramPhaseEquiv (φ G) (fun i => (FibreGram (0 : Fin 1) Uᵀ (π i)).submatrix τ τ))"),
    4: ("(∀ G, RealizableGram (Fin 1) Γ₀ G → ∀ U, AdmissibleDilationAt Γ₀ (0 : Fin 1) U → FibreGram (0 : Fin 1) U = G → "
        "GramPhaseEquiv (φ G) (fun i => Matrix.of fun j k => star ((FibreGram (0 : Fin 1) Uᵀ (π i)).submatrix τ τ j k)))"),
}
PIDX = relab('π', 'τ', proj('p'))  # the (π, τ)-relabelled index of p
PAIR_TYPE = "(Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)"
CONFIG = "∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →\n    "

# the four cores, stated for an abstract test tuple G and its known image class K
PQ = "((π p.1.1, π p.1.2.1, π p.1.2.2), (τ p.2.1, τ p.2.2.1, τ p.2.2.2))"
SQ = "((τ p.2.2.1, τ p.2.2.2, τ p.2.1), (π p.1.1, π p.1.2.1, π p.1.2.2))"
CORE_HEAD = (f"∀ (φ : ({T}) → ({T})) (π τ : Equiv.Perm (Fin 4)) (G K : {T}), "
             "GramPhaseEquiv (φ G) K → ")
M = "  have m := congrFun (mixedTriple_gauge (gramPhaseEquiv_trans (gramPhaseEquiv_symm e1) e2)) p\n"
thm('a32_shared_core_1', CORE_HEAD + "GramPhaseEquiv (φ G) (fun i => (G (π i)).submatrix τ τ) → "
    f"∀ p : {PAIR_TYPE}, mixedTriple G {PQ} = mixedTriple K p",
    "  intro φ π τ G K e1 e2 p\n" + M + "  rw [mixedTriple_relabel2] at m\n  exact m\n")
thm('a32_shared_core_2', CORE_HEAD + "GramPhaseEquiv (φ G) (fun i => Matrix.of fun j k => star ((G (π i)).submatrix τ τ j k)) → "
    f"∀ p : {PAIR_TYPE}, star (mixedTriple G {PQ}) = mixedTriple K p",
    "  intro φ π τ G K e1 e2 p\n" + M + "  rw [a32_shared_star_relabel] at m\n  exact m\n")
thm('a32_shared_core_3', CORE_HEAD + "∀ U : Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ, FibreGram (0 : Fin 1) U = G → "
    "GramPhaseEquiv (φ G) (fun i => (FibreGram (0 : Fin 1) Uᵀ (π i)).submatrix τ τ) → "
    f"∀ p : {PAIR_TYPE}, star (mixedTriple G {SQ}) = mixedTriple K p",
    "  intro φ π τ G K e1 U hUG e2 p\n" + M + "  rw [a32_shared_transpose_relabel, hUG] at m\n  exact m\n")
thm('a32_shared_core_4', CORE_HEAD + "∀ U : Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ, FibreGram (0 : Fin 1) U = G → "
    "GramPhaseEquiv (φ G) (fun i => Matrix.of fun j k => star ((FibreGram (0 : Fin 1) Uᵀ (π i)).submatrix τ τ j k)) → "
    f"∀ p : {PAIR_TYPE}, mixedTriple G {SQ} = mixedTriple K p",
    "  intro φ π τ G K e1 U hUG e2 p\n" + M + "  rw [a32_shared_transpose_star_relabel, hUG] at m\n  exact m\n")


def bridge(shape, desig):
    name = f"a32_shared_bridge_{shape}{'d' if desig else 'r'}"
    if desig:
        concl = f"∀ p : {PAIR_TYPE}, {lhs(shape, None, PIDX)} % 4 = {rhs(None, proj('p'))} % 4"
        stmt = (CONFIG + f"∀ φ : ({T}) → ({T}), {HW1} →\n    ∀ π τ : Equiv.Perm (Fin 4), {SH[shape]} →\n    {concl}")
        G = FZ('Complex.I')
        real = "sh1_necessity (hadamard_z_admissible Γ₀ hΓ₀ Complex.I hI)"
        k = "hW _ hR Complex.I hI (gramPhaseEquiv_refl _)"
        intro = "  intro Γ₀ hΓ₀ φ hW π τ h p\n"
        rel = ""
    else:
        concl = (f"∀ r ∈ {R8TXT}, ∀ p : {PAIR_TYPE}, "
                 f"{lhs(shape, ('r.1', 'r.2'), PIDX)} % 4 = {rhs(('r.1', 'r.2'), proj('p'))} % 4")
        stmt = (CONFIG + f"∀ φ : ({T}) → ({T}), {HW2} →\n    ∀ π τ : Equiv.Perm (Fin 4), {SH[shape]} →\n    {concl}")
        G = f"(fun i => ({FZ('Complex.I')} (r.1 i)).submatrix r.2 r.2)"
        real = "(iso2_classes_single Γ₀ hΓ₀).2 r.1 r.2 Complex.I hI"
        k = "hW r hr _ hR Complex.I hI (gramPhaseEquiv_refl _)"
        intro = "  intro Γ₀ hΓ₀ φ hW π τ h r hr p\n"
        rel = "  rw [mixedTriple_relabel2, mixedTriple_relabel2] at m\n"
    pf = HI + intro + f"  have hR : RealizableGram (Fin 1) Γ₀ ({G}) := {real}\n  have e1 := {k}\n"
    if shape in (1, 2):
        pf += f"  have m := a32_shared_core_{shape} φ π τ _ _ e1 (h _ hR) p\n"
    else:
        pf += ("  obtain ⟨U, hU, hUG⟩ := (iso1_single_carrier Γ₀ hΓ₀).2.2.2.1 _ hR\n"
               f"  have m := a32_shared_core_{shape} φ π τ _ _ e1 U hUG (h _ hR U hU hUG) p\n")
    pf += rel
    pf += ("  simp only [a32_shared_value_I, a32_shared_value_starI, a32_shared_star_pow] at m\n"
           "  exact a32_shared_pow_mod _ _ m\n")
    thm(name, stmt, pf)
    return name


for s in (1, 2, 3, 4):
    bridge(s, True)
    bridge(s, False)


def lit(p):
    (a1, a2, a3), (b1, b2, b3) = p
    return f"((({a1} : Fin 4), ({a2} : Fin 4), ({a3} : Fin 4)), (({b1} : Fin 4), ({b2} : Fin 4), ({b3} : Fin 4)))"


def table(shape):
    hyps = []
    for ri, p in covers[shape]:
        p = tuple(tuple(x) for x in p)
        L = lit(p)
        idx = relab('π', 'τ', proj(L))
        if ri == 0:
            hyps.append(f"{lhs(shape, None, idx)} % 4 = {rhs(None, proj(L))} % 4")
        else:
            r = (f"({R9[ri][0]}, {R9[ri][1]}).1", f"({R9[ri][0]}, {R9[ri][1]}).2")
            hyps.append(f"{lhs(shape, r, idx)} % 4 = {rhs(r, proj(L))} % 4")
    name = f"a32_shared_table_{shape}"
    thm(name, "∀ π τ : Equiv.Perm (Fin 4),\n      " + " →\n      ".join(hyps) + " →\n      False", "  decide +kernel\n")
    return name


for s in (1, 2, 3, 4):
    table(s)

# the assembly
parts = []
for s in (1, 2, 3, 4):
    args = []
    for ri, p in covers[s]:
        p = tuple(tuple(x) for x in p)
        if ri == 0:
            args.append(f"(a32_shared_bridge_{s}d Γ₀ hΓ₀ φ hW1 π τ h {lit(p)})")
        else:
            args.append(f"(a32_shared_bridge_{s}r Γ₀ hΓ₀ φ hW2 π τ h ({R9[ri][0]}, {R9[ri][1]}) (by decide) {lit(p)})")
    parts.append(f"  · exact a32_shared_table_{s} π τ\n      " + "\n      ".join(args))
thm('a32_shared_separation', P['S_SEP'].replace('\n', '\n    '),
    "  intro Γ₀ hΓ₀ d _ φ hW\n  obtain ⟨hW1, hW2⟩ := hW\n  rintro ⟨π, τ, h | h | h | h⟩\n" + "\n".join(parts) + "\n")

out += ['end OrbitIsometryClassification', 'end OIBridge', '']
open(sys.argv[1], 'w', encoding='utf-8').write('\n'.join(out))
