# The rest of A32's module, appended after the separation lemmas. Runs inside build_mod32.py's scope
# (FZ, thm, T, P, R9, R8TXT, HX, HI, CONFIG, out, d, sys).
STAGE = int(sys.argv[2]) if len(sys.argv) > 2 else 2
A_ = "((Equiv.swap (0 : Fin 4) 3).trans (Equiv.swap (1 : Fin 4) 2))"
B_ = "((Equiv.swap (0 : Fin 4) 1).trans (Equiv.swap (2 : Fin 4) 3))"
GS = {'A': (P1, A_), 'B': (P1, B_), 'C': (A_, P1), 'D': (B_, P1)}
CONJ_PH = {'A': None, 'B': None, 'C': '![1, -star z, -1, star z]', 'D': '![1, star z, -1, -star z]'}
# for each of the eight other circles (index into R9): the relabelling that fixes it, and its phases
FIX = {1: ('A', None), 2: ('B', None), 3: ('C', '![1, -1, 1, -1]'), 4: ('A', None), 5: ('B', None),
       6: ('D', '![1, -1, 1, -1]'), 7: ('A', None), 8: ('B', None)}


def par(x):
    return x if x.startswith('(') else f"({x})"


def circ(r1, r2, w):
    return f"(fun i => ({FZ(w)} ({par(r1)} i)).submatrix {par(r2)} {par(r2)})"


UNIT = """  have hx : ∀ y : Fin 1, y = 0 := fun y => Subsingleton.elim y 0
  have hzn : ‖z‖ = 1 := by
    have h1 : ((‖z‖ ^ 2 : ℝ) : ℂ) = 1 := by rw [← a32_shared_star_mul_self, hz]
    have h2 : ‖z‖ ^ 2 = 1 := by exact_mod_cast h1
    exact (pow_eq_one_iff_of_nonneg (norm_nonneg z) two_ne_zero).mp h2
  have hz0 : z ≠ 0 := by rintro rfl; simp at hz
  have hw : (starRingEnd ℂ) z = z⁻¹ := eq_inv_of_mul_eq_one_left hz
"""
ENTRYWISE = """  fin_cases i <;> fin_cases j <;> fin_cases k <;>
    simp [Matrix.submatrix_apply, fibreGram_unique (0 : Fin 1) hx, Equiv.swap_apply_def, hw] <;>
    first | ring1 | field_simp
"""


def phase_intro(ph):
    if ph is None:
        return "  refine ⟨fun _ => 1, fun _ => by simp, fun i j k => ?_⟩\n"
    return f"  refine ⟨{ph}, fun j => by fin_cases j <;> simp [hzn], fun i j k => ?_⟩\n"


# ---- two general facts: the squared norm, and relabelling respects equivalence
thm('a32_shared_star_mul_self', "∀ z : ℂ, star z * z = ((‖z‖ ^ 2 : ℝ) : ℂ)",
    "  intro z\n  rw [mul_comm, RCLike.star_def, Complex.mul_conj]\n  norm_cast\n  exact Complex.normSq_eq_norm_sq _\n")
thm('a32_shared_relabel',
    f"∀ (π τ : Equiv.Perm (Fin 4)) (G G' : {T}), GramPhaseEquiv G G' →\n"
    "      GramPhaseEquiv (fun i => (G (π i)).submatrix τ τ) (fun i => (G' (π i)).submatrix τ τ)",
    "  intro π τ G G' h\n  obtain ⟨c, hc, hG⟩ := h\n  exact ⟨fun j => c (τ j), fun j => hc (τ j), fun i j k => by\n"
    "    simp only [Matrix.submatrix_apply]; exact hG (π i) (τ j) (τ k)⟩\n")

# ---- the Fourier tuple: conjugation of the parameter, and injectivity on unit parameters
thm('a32_shared_fourier_star',
    f"∀ z : ℂ, {FZ('star z')} = fun i => Matrix.of fun j k => star ({FZ('z')} i j k)",
    HX + "  intro z\n  funext i\n  ext j k\n  simp only [Matrix.of_apply, fibreGram_unique (0 : Fin 1) hx]\n"
    "  fin_cases i <;> fin_cases j <;> fin_cases k <;> simp [star_mul'] <;> ring\n")
thm('a32_shared_coord_inj', f"∀ z : ℂ, mixedTriple ({FZ('z')}) ((1, 0, 0), (0, 1, 0)) = z / 64",
    HX + "  intro z\n  simp [mixedTriple, fibreGram_unique (0 : Fin 1) hx] <;> ring\n")
thm('a32_shared_fourier_inj', f"∀ z w : ℂ, GramPhaseEquiv ({FZ('z')}) ({FZ('w')}) → z = w",
    "  intro z w h\n  have hc := congrFun (mixedTriple_gauge h) ((1, 0, 0), (0, 1, 0))\n"
    "  rw [a32_shared_coord_inj, a32_shared_coord_inj] at hc\n  linear_combination -64 * hc\n")

# ---- the pair relabellings: each conjugates the Fourier circle and fixes one of the other circles
for n, (s, r) in GS.items():
    thm(f'a32_shared_conj_{n}',
        f"∀ z : ℂ, star z * z = 1 → GramPhaseEquiv (fun i => ({FZ('z')} ({s} i)).submatrix {r} {r}) ({FZ('star z')})",
        "  intro z hz\n" + UNIT + phase_intro(CONJ_PH[n]) + ENTRYWISE)
for ci, (n, ph) in FIX.items():
    s, r = GS[n]
    r1, r2 = R9[ci]
    thm(f'a32_shared_fix_{ci}',
        f"∀ z : ℂ, star z * z = 1 → GramPhaseEquiv "
        f"(fun i => (({FZ('z')} ({par(r1)} ({s} i))).submatrix {par(r2)} {par(r2)}).submatrix {r} {r}) {circ(r1, r2, 'z')}",
        "  intro z hz\n" + UNIT + phase_intro(ph) + ENTRYWISE)
RR = "(r.1 i)"
PAIR_STMT = (f"∀ r ∈ {R8TXT}, ∃ σ ρ : Equiv.Perm (Fin 4),\n"
             f"      (∀ z : ℂ, star z * z = 1 → GramPhaseEquiv (fun i => ({FZ('z')} (σ i)).submatrix ρ ρ) ({FZ('star z')}))\n"
             f"      ∧ (∀ w : ℂ, star w * w = 1 → GramPhaseEquiv (fun i => ((fun i => ({FZ('w')} (r.1 i)).submatrix r.2 r.2) (σ i)).submatrix ρ ρ)\n"
             f"          (fun i => ({FZ('w')} (r.1 i)).submatrix r.2 r.2))")
pf = ("  intro r hr\n  simp only [List.mem_cons, List.mem_nil_iff, or_false] at hr\n"
      "  rcases hr with rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl\n")
for ci in range(1, 9):
    n, _ = FIX[ci]
    s, r = GS[n]
    pf += f"  · exact ⟨{s}, {r}, a32_shared_conj_{n}, a32_shared_fix_{ci}⟩\n"
thm('a32_shared_pair', PAIR_STMT, pf)

# ---- every realizable class lies on the Fourier circle or on one of the other eight
FOURIER_OR = (f"(∃ z : ℂ, star z * z = 1 ∧ GramPhaseEquiv G ({FZ('z')}))\n"
              f"      ∨ (∃ r ∈ {R8TXT}, ∃ z : ℂ, star z * z = 1 ∧ GramPhaseEquiv G (fun i => ({FZ('z')} (r.1 i)).submatrix r.2 r.2))")
pf = """  intro Γ₀ hΓ₀ G hG
  obtain ⟨π, τ, z, hz, hGe⟩ := (iso2_classes_single Γ₀ hΓ₀).1 G hG
  have hc := a26_1_circle_count
  dsimp only at hc
  obtain ⟨-, -, -, h3⟩ := hc
  obtain ⟨r, hr, hfw, -⟩ := h3 π τ
  obtain ⟨z', hz', h⟩ := hfw z hz
  have hG' := gramPhaseEquiv_trans hGe h
  simp only [List.mem_cons, List.mem_nil_iff, or_false] at hr
  rcases hr with rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl
  · left
    refine ⟨z', hz', ?_⟩
    convert hG' using 1
    funext i
    ext j k
    simp
  all_goals exact Or.inr ⟨_, by decide, z', hz', hG'⟩
"""
thm('a32_shared_classify', CONFIG + f"∀ G : {T}, RealizableGram (Fin 1) Γ₀ G →\n      {FOURIER_OR}", pf)

# ---- the controls
OV = {1: ('clash', '((0, 0, 2), (0, 0, 2))', '1 / 64', '-1 / 64'), 2: ('clash', '((0, 0, 2), (0, 0, 1))', '-1 / 64', '1 / 64'),
      3: ('clash', '((0, 0, 2), (0, 0, 2))', '1 / 64', '-1 / 64'), 4: ('force', '((0, 0, 1), (3, 0, 0))'),
      5: ('force', '((0, 0, 1), (1, 0, 0))'), 6: ('clash', '((0, 0, 1), (0, 0, 2))', '-1 / 64', '1 / 64'),
      7: ('force', '((0, 0, 1), (1, 0, 0))'), 8: ('force', '((0, 0, 1), (1, 0, 0))')}
SIMPV = "simp [mixedTriple, Matrix.submatrix_apply, fibreGram_unique (0 : Fin 1) hx, Equiv.swap_apply_def] <;> norm_num"
SIMPC = "norm_num [mixedTriple, Matrix.submatrix_apply, fibreGram_unique (0 : Fin 1) hx, Equiv.swap_apply_def] at hc"
pf = HX + ("  intro r hr z w hz hw h\n  simp only [List.mem_cons, List.mem_nil_iff, or_false] at hr\n"
           "  rcases hr with rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl\n")
for ci in range(1, 9):
    kind, q = OV[ci][:2]
    if kind == 'clash':
        vl, vr = OV[ci][2:]
        r1, r2 = R9[ci]
        pf += (f"  · have hL : mixedTriple ({FZ('z')}) {q} = {vl} := by\n      {SIMPV}\n"
               f"    have hR : mixedTriple {circ(r1, r2, 'w')} {q} = {vr} := by\n      {SIMPV}\n"
               f"    have e : ({vl} : ℂ) = {vr} := hL.symm.trans ((congrFun (mixedTriple_gauge h) {q}).symm.trans hR)\n"
               "    norm_num at e\n")
    else:
        pf += f"  · have hc := congrFun (mixedTriple_gauge h) {q}\n    {SIMPC}\n"
        pf += ("    have him : z.im = 0 := by\n      have := congrArg Complex.im hc\n      simp at this\n      linarith\n"
               "    have hs : star z = z := Complex.conj_eq_iff_im.mpr him\n    rw [hs]\n    exact gramPhaseEquiv_refl _\n")
thm('a32_control_overlap', P['S_OVL'].replace('\n', '\n    '), pf)

REAL_F = "sh1_necessity (hadamard_z_admissible Γ₀ hΓ₀ _ ‹_›)"
thm('a32_shared_exists', P['S_EXIST'].replace('\n', '\n    '), """  intro Γ₀ hΓ₀ d hd
  classical
  refine ⟨fun G => if h : ∃ z : ℂ, star z * z = 1 ∧ GramPhaseEquiv G (@@FZ@@) then @@FZC@@ else G, ?_, ?_⟩
  · intro G _ z hz hGz
    have h : ∃ z : ℂ, star z * z = 1 ∧ GramPhaseEquiv G (@@FZ@@) := ⟨z, hz, hGz⟩
    simp only [dif_pos h]
    have e : h.choose = z :=
      a32_shared_fourier_inj _ _ (gramPhaseEquiv_trans (gramPhaseEquiv_symm h.choose_spec.2) hGz)
    rw [e]
    exact gramPhaseEquiv_refl _
  · intro r hr G _ w hw hGw
    by_cases h : ∃ z : ℂ, star z * z = 1 ∧ GramPhaseEquiv G (@@FZ@@)
    · simp only [dif_pos h]
      have hov := a32_control_overlap r hr h.choose w h.choose_spec.1 hw
        (gramPhaseEquiv_trans (gramPhaseEquiv_symm h.choose_spec.2) hGw)
      exact gramPhaseEquiv_trans hov (gramPhaseEquiv_symm h.choose_spec.2)
    · simp only [dif_neg h]
      exact gramPhaseEquiv_refl G
""".replace('@@FZ@@', FZ('z')).replace('@@FZC@@', FZ('star h.choose')))

# the isometry: the three hypotheses of every map satisfying the witness equations
RELF = lambda x: f"(fun i => ({x} (σ i)).submatrix ρ ρ)"
pf = HI + f"""  intro Γ₀ hΓ₀ d hd φ hW
  obtain ⟨hW1, hW2⟩ := hW
  have hsu : ∀ z : ℂ, star z * z = 1 → star (star z) * star z = 1 := fun z hz => by
    rw [star_star, mul_comm]
    exact hz
  have hFr : ∀ z : ℂ, star z * z = 1 → RealizableGram (Fin 1) Γ₀ ({FZ('z')}) :=
    fun z hz => sh1_necessity (hadamard_z_admissible Γ₀ hΓ₀ z hz)
  have img : ∀ G, RealizableGram (Fin 1) Γ₀ G →
      (∃ z : ℂ, star z * z = 1 ∧ GramPhaseEquiv G ({FZ('z')}) ∧ GramPhaseEquiv (φ G) ({FZ('star z')}))
      ∨ (∃ r ∈ {R8TXT}, ∃ z : ℂ, star z * z = 1 ∧
          GramPhaseEquiv G (fun i => ({FZ('z')} (r.1 i)).submatrix r.2 r.2) ∧ GramPhaseEquiv (φ G) G) := by
    intro G hG
    rcases a32_shared_classify Γ₀ hΓ₀ G hG with ⟨z, hz, h⟩ | ⟨r, hr, z, hz, h⟩
    · exact Or.inl ⟨z, hz, h, hW1 G hG z hz h⟩
    · exact Or.inr ⟨r, hr, z, hz, h, hW2 r hr G hG z hz h⟩
  refine ⟨fun G hG => ?_, fun H hH => ?_, fun G H hG hH => ?_⟩
  · rcases img G hG with ⟨z, hz, _, h⟩ | ⟨r, hr, z, hz, _, h⟩
    · exact realizable_of_gramPhaseEquiv (0 : Fin 1) (hFr (star z) (hsu z hz)) (gramPhaseEquiv_symm h)
    · exact realizable_of_gramPhaseEquiv (0 : Fin 1) hG (gramPhaseEquiv_symm h)
  · rcases img H hH with ⟨z, hz, hHz, _⟩ | ⟨r, hr, z, hz, _, h⟩
    · refine ⟨{FZ('star z')}, hFr (star z) (hsu z hz), ?_⟩
      have e := hW1 _ (hFr (star z) (hsu z hz)) (star z) (hsu z hz) (gramPhaseEquiv_refl _)
      rw [star_star] at e
      exact gramPhaseEquiv_trans e (gramPhaseEquiv_symm hHz)
    · exact ⟨H, hH, h⟩
  · rcases img G hG with ⟨z, hz, hGz, hφG⟩ | ⟨r, hr, z, hz, hGz, hφG⟩ <;>
      rcases img H hH with ⟨w, hw, hHw, hφH⟩ | ⟨s, hs, w, hw, hHw, hφH⟩
    · rw [geo1_class_invariant d hd _ _ _ _ hφG hφH, geo1_class_invariant d hd G _ H _ hGz hHw,
        a32_shared_fourier_star, a32_shared_fourier_star]
      exact conj_isometry d hd _ _
    · obtain ⟨σ, ρ, ha, hb⟩ := a32_shared_pair s hs
      have hHH : GramPhaseEquiv {RELF('H')} H :=
        gramPhaseEquiv_trans (a32_shared_relabel σ ρ _ _ hHw)
          (gramPhaseEquiv_trans (hb w hw) (gramPhaseEquiv_symm hHw))
      calc d (φ G) (φ H) = d ({FZ('star z')}) H := geo1_class_invariant d hd _ _ _ _ hφG hφH
        _ = d {RELF(FZ('z'))} {RELF('H')} :=
            geo1_class_invariant d hd _ _ _ _ (gramPhaseEquiv_symm (ha z hz)) (gramPhaseEquiv_symm hHH)
        _ = d ({FZ('z')}) H := relabel2_isometry d hd σ ρ _ _
        _ = d G H := geo1_class_invariant d hd _ _ _ _ (gramPhaseEquiv_symm hGz) (gramPhaseEquiv_refl H)
    · obtain ⟨σ, ρ, ha, hb⟩ := a32_shared_pair r hr
      have hGG : GramPhaseEquiv {RELF('G')} G :=
        gramPhaseEquiv_trans (a32_shared_relabel σ ρ _ _ hGz)
          (gramPhaseEquiv_trans (hb z hz) (gramPhaseEquiv_symm hGz))
      calc d (φ G) (φ H) = d G ({FZ('star w')}) := geo1_class_invariant d hd _ _ _ _ hφG hφH
        _ = d {RELF('G')} {RELF(FZ('w'))} :=
            geo1_class_invariant d hd _ _ _ _ (gramPhaseEquiv_symm hGG) (gramPhaseEquiv_symm (ha w hw))
        _ = d G ({FZ('w')}) := relabel2_isometry d hd σ ρ _ _
        _ = d G H := geo1_class_invariant d hd _ _ _ _ (gramPhaseEquiv_refl G) (gramPhaseEquiv_symm hHw)
    · exact geo1_class_invariant d hd _ _ _ _ hφG hφH
"""
thm('a32_shared_isometry', P['S_ISO'].replace('\n', '\n    '), pf)

thm('a32_control_moves', P['S_MOVE'].replace('\n', '\n    '), HI + f"""  intro Γ₀ hΓ₀ d _ φ hW
  have hR : RealizableGram (Fin 1) Γ₀ ({FZ('Complex.I')}) := sh1_necessity (hadamard_z_admissible Γ₀ hΓ₀ Complex.I hI)
  refine ⟨_, hR, fun h => ?_⟩
  have e := hW.1 _ hR Complex.I hI (gramPhaseEquiv_refl _)
  have hs := a32_shared_fourier_inj _ _ (gramPhaseEquiv_trans (gramPhaseEquiv_symm e) h)
  rw [Complex.star_def, Complex.conj_I] at hs
  norm_num [Complex.ext_iff] at hs
""")

thm('a32_control_global', P['S_GLOBAL'].replace('\n', '\n    '), """  intro Γ₀ hΓ₀ d hd φ hφ
  subst hφ
  have hc := (iso1_single_carrier Γ₀ hΓ₀).2.1
  refine ⟨⟨fun G hG => hc G hG, fun H hH => ⟨_, hc H hH, ⟨fun _ => 1, fun _ => by simp, fun i j k => by simp⟩⟩,
    fun G H _ _ => conj_isometry d hd G H⟩, 1, 1,
    Or.inr (Or.inl fun G _ => ⟨fun _ => 1, fun _ => by simp, fun i j k => by simp⟩)⟩
""")
thm('a32_control_identity', P['S_ID'].replace('\n', '\n    '), """  intro Γ₀ _ d _ φ hφ
  subst hφ
  exact ⟨⟨fun G hG => hG, fun H hH => ⟨H, hH, gramPhaseEquiv_refl H⟩, fun G H _ _ => rfl⟩, 1, 1,
    Or.inl fun G _ => ⟨fun _ => 1, fun _ => by simp, fun i j k => by simp⟩⟩
""")

# the quarter-turn: well defined, and not distance-preserving
W0 = "(⟨89999 / 90001, 600 / 90001⟩ : ℂ)"
C4 = lambda x: circ(S23, S23, x)
pf = HX + HI + f"""  intro Γ₀ hΓ₀ d hd
  classical
  refine ⟨⟨fun G => if h : ∃ z : ℂ, star z * z = 1 ∧ GramPhaseEquiv G ({FZ('z')}) then {FZ('(Complex.I * h.choose)')} else G, ?_, ?_⟩, ?_⟩
  · intro G _ z hz hGz
    have h : ∃ z : ℂ, star z * z = 1 ∧ GramPhaseEquiv G ({FZ('z')}) := ⟨z, hz, hGz⟩
    simp only [dif_pos h]
    have e : h.choose = z :=
      a32_shared_fourier_inj _ _ (gramPhaseEquiv_trans (gramPhaseEquiv_symm h.choose_spec.2) hGz)
    rw [e]
    exact gramPhaseEquiv_refl _
  · intro G _ hn
    have h : ¬ ∃ z : ℂ, star z * z = 1 ∧ GramPhaseEquiv G ({FZ('z')}) := fun ⟨z, hz, hz'⟩ => hn z hz hz'
    simp only [dif_neg h]
    exact gramPhaseEquiv_refl G
  · intro φ hQ h3
    obtain ⟨hQ1, hQ2⟩ := hQ
    have h1 : star (1 : ℂ) * 1 = 1 := by simp
    have hw₀ : star {W0} * {W0} = 1 := by
      apply Complex.ext <;> simp [Complex.mul_re, Complex.mul_im] <;> norm_num
    have hGr : RealizableGram (Fin 1) Γ₀ {C4('1')} := (iso2_classes_single Γ₀ hΓ₀).2 _ _ 1 h1
    have hHr : RealizableGram (Fin 1) Γ₀ {C4(W0)} := (iso2_classes_single Γ₀ hΓ₀).2 _ _ _ hw₀
    have hG1 : GramPhaseEquiv {C4('1')} ({FZ('1')}) := ⟨fun _ => 1, fun _ => by simp, fun i j k => by
      fin_cases i <;> fin_cases j <;> fin_cases k <;>
        simp [Matrix.submatrix_apply, fibreGram_unique (0 : Fin 1) hx, Equiv.swap_apply_def]⟩
    have hφG := hQ1 _ hGr 1 h1 hG1
    rw [mul_one] at hφG
    have hoff : ∀ z : ℂ, star z * z = 1 → ¬ GramPhaseEquiv {C4(W0)} ({FZ('z')}) := by
      intro z _ h
      have hA : ∀ w : ℂ, mixedTriple {C4('w')} ((0, 0, 1), (2, 0, 0)) = -w / 64 := by
        intro w
        simp [mixedTriple, Matrix.submatrix_apply, fibreGram_unique (0 : Fin 1) hx, Equiv.swap_apply_def] <;> ring
      have hB : mixedTriple ({FZ('z')}) ((0, 0, 1), (2, 0, 0)) = -1 / 64 := by
        simp [mixedTriple, fibreGram_unique (0 : Fin 1) hx] <;> norm_num
      have e : -{W0} / 64 = -1 / 64 := (hA _).symm.trans ((congrFun (mixedTriple_gauge h) ((0, 0, 1), (2, 0, 0))).symm.trans hB)
      have e2 : {W0} = 1 := by linear_combination -64 * e
      have e3 := congrArg Complex.im e2
      norm_num at e3
    have hφH := hQ2 _ hHr hoff
    have heq := h3 _ _ hGr hHr
    rw [geo1_class_invariant d hd _ _ _ _ hφG hφH, relabel2_isometry d hd _ _ _ _] at heq
    have hlow := coord_le_dist d hd ({FZ('Complex.I')}) {C4(W0)} ((0, 0, 1), (3, 0, 0))
    have hup := fourier_dist_le d hd 1 {W0} h1 hw₀
    have eA : mixedTriple ({FZ('Complex.I')}) ((0, 0, 1), (3, 0, 0)) = -Complex.I / 64 := by
      simp [mixedTriple, fibreGram_unique (0 : Fin 1) hx] <;> ring
    have eB : mixedTriple {C4(W0)} ((0, 0, 1), (3, 0, 0)) = -1 / 64 := by
      simp [mixedTriple, Matrix.submatrix_apply, fibreGram_unique (0 : Fin 1) hx, Equiv.swap_apply_def] <;> norm_num
    rw [eA, eB, heq] at hlow
    have ha : ‖-Complex.I / 64 - -1 / 64‖ ^ 2 = 2 / 4096 := by
      rw [← Complex.normSq_eq_norm_sq, Complex.normSq_apply]
      simp [Complex.div_re, Complex.div_im] <;> norm_num
    have hb : ‖{W0} - 1‖ ^ 2 = 4 / 90001 := by
      rw [← Complex.normSq_eq_norm_sq, Complex.normSq_apply]
      simp [Complex.div_re, Complex.div_im] <;> norm_num
    have hab := le_trans hlow hup
    have hsq := mul_self_le_mul_self (norm_nonneg _) hab
    nlinarith [norm_nonneg ({W0} - 1)]
"""
thm('a32_control_quarter', P['S_QUARTER'].replace('\n', '\n    '), pf)

if STAGE >= 2:
    thm('a32_not_rigid', P['P_N'].replace('\n', '\n    '), """  intro Γ₀ hΓ₀ d hd
  obtain ⟨φ, hW⟩ := a32_shared_exists Γ₀ hΓ₀ d hd
  exact ⟨φ, a32_shared_isometry Γ₀ hΓ₀ d hd φ hW, a32_shared_separation Γ₀ hΓ₀ d hd φ hW⟩
""")
    thm('a32_c_exclusive', ('(' + P['P_N'] + ') →\n¬ (' + P['P_R'] + ')').replace('\n', '\n    '), """  intro hN hR
  obtain ⟨φ, hH, hF⟩ := hN _ rfl _ rfl
  exact hF (hR _ rfl _ rfl φ hH)
""")

out += ['end OrbitIsometryClassification', 'end OIBridge', '']
open(sys.argv[1], 'w', encoding='utf-8').write('\n'.join(out))
