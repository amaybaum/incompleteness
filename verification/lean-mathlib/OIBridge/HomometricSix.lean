/-
  OIBridge/HomometricSix.lean — the two load-bearing finite endpoints of the n = 6 kill chain.

  The printed homometric Golomb pair R₁ = {0,1,4,10,12,17}, R₂ = {0,1,8,11,13,17} forces the
  unique small non-two-branch frequency correspondence μ. The classification probe
  (gap_correspondence_probe) showed that μ admits NO realizing pair of eigenbases, through an
  exact chain whose two decisive ends are kernel-proved here:

    `flat_locus`          — "only flat moduli survive": a log-modulus row satisfies every
                            pulled-back four-cycle identity of μ IFF it is constant. The forward
                            direction uses five explicit relation instances (the first being the
                            L₃ = L₄ relation of the quadruple {0,1,3,4}); the reverse is the
                            general flat control. This is L_μ^⊥ = span(1) exactly — the modulus
                            exceptional locus is the uniform row and nothing else.

    `no_six_orthogonal`   — "even flat moduli cannot be jointly unitary": on the flat locus the
                            triangle-consistent phases make both eigenbases monomial with the
                            exponent tables below, joint row-orthogonality confines all pairwise
                            parameter differences to the eight common mask zeros, and the group
                            they generate inside ℤ/12 × ℤ/4 admits no four pairwise-connected
                            points — so six mutually orthogonal rows are impossible. Sharpness:
                            `three_clique` exhibits three.

  Supporting kernel facts: both rulers are Golomb (`golomb_r1`, `golomb_r2`), μ is the gap-forced
  correspondence and a bijection (`mu_gap`, `mu_forced`, `mu_muInv`, `muInv_mu`), μ is induced by
  no vertex map in either orientation, even mixed per edge (`mu_not_vertex_induced`), both mask
  polynomials factor over ℤ with the shared factor 1 + x + x²y (`maskV_factor`, `maskW_factor`),
  and the ξ/η exponent linkage holds on all fifteen edges (`linkage`).

  HONEST SCOPE. The analytic reduction connecting these endpoints — rank-one forcing of
  z'^{μ(a,b)} = λ z^{ab}, the Smith-normal-form completeness of the phase kernel, and the
  resultant computation showing the eight listed points exhaust the common torus zeros of the two
  masks — is verified exactly at probe level (gap_correspondence_probe M4–M7), not yet in the
  kernel. What the kernel certifies here is: the modulus lattice has full rank n − 1 with the flat
  direction as its entire annihilator, and the final clique obstruction is a true statement about
  the eight-element difference set. General-n K4-rigidity is OIBridge/EdgeRigidity.lean.
-/
import Mathlib.Data.ZMod.Basic
import Mathlib.Data.Fintype.Prod
import Mathlib.Algebra.BigOperators.Fin
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.FinCases

namespace OIBridge
namespace HomometricSix

set_option maxRecDepth 100000

/-- The first printed Golomb ruler. -/
def r1 : Fin 6 → ℤ
  | 0 => 0 | 1 => 1 | 2 => 4 | 3 => 10 | 4 => 12 | 5 => 17

/-- The second printed Golomb ruler, homometric with the first. -/
def r2 : Fin 6 → ℤ
  | 0 => 0 | 1 => 1 | 2 => 8 | 3 => 11 | 4 => 13 | 5 => 17

/-- The forced correspondence on ascending pairs: `mu a b` is the R₂-pair with the same gap. -/
def mu : Fin 6 → Fin 6 → Fin 6 × Fin 6
  | 0, 1 => (0,1) | 0, 2 => (4,5) | 0, 3 => (1,3) | 0, 4 => (1,4) | 0, 5 => (0,5)
  | 1, 2 => (2,3) | 1, 3 => (2,5) | 1, 4 => (0,3) | 1, 5 => (1,5)
  | 2, 3 => (3,5) | 2, 4 => (0,2) | 2, 5 => (0,4)
  | 3, 4 => (3,4) | 3, 5 => (1,2)
  | 4, 5 => (2,4)
  | _, _ => (0,0)

/-- The inverse correspondence on ascending pairs. -/
def muInv : Fin 6 → Fin 6 → Fin 6 × Fin 6
  | 0, 1 => (0,1) | 0, 2 => (2,4) | 0, 3 => (1,4) | 0, 4 => (2,5) | 0, 5 => (0,5)
  | 1, 2 => (3,5) | 1, 3 => (0,3) | 1, 4 => (0,4) | 1, 5 => (1,5)
  | 2, 3 => (1,2) | 2, 4 => (4,5) | 2, 5 => (1,3)
  | 3, 4 => (3,4) | 3, 5 => (2,3)
  | 4, 5 => (0,2)
  | _, _ => (0,0)

/-- R₁ is Golomb: equal gaps between ascending pairs force equal pairs. -/
theorem golomb_r1 : ∀ a b c d : Fin 6, a < b → c < d →
    r1 b - r1 a = r1 d - r1 c → a = c ∧ b = d := by decide

/-- R₂ is Golomb. -/
theorem golomb_r2 : ∀ a b c d : Fin 6, a < b → c < d →
    r2 b - r2 a = r2 d - r2 c → a = c ∧ b = d := by decide

/-- μ preserves the gap and stays ascending — with `golomb_r2` this says μ is well defined. -/
theorem mu_gap : ∀ a b : Fin 6, a < b →
    (mu a b).1 < (mu a b).2 ∧ r2 (mu a b).2 - r2 (mu a b).1 = r1 b - r1 a := by decide

/-- μ is FORCED: any gap-matching ascending pair is the μ-image. Together with `mu_gap` this is
the statement that the homometric pair admits exactly one frequency-preserving correspondence. -/
theorem mu_forced : ∀ a b c d : Fin 6, a < b → c < d →
    r2 d - r2 c = r1 b - r1 a → mu a b = (c, d) := by decide

/-- μ and its inverse compose to the identity on ascending pairs (so μ is an edge bijection). -/
theorem muInv_mu : ∀ a b : Fin 6, a < b →
    muInv (mu a b).1 (mu a b).2 = (a, b) := by decide

theorem mu_muInv : ∀ c d : Fin 6, c < d →
    (muInv c d).1 < (muInv c d).2 ∧ mu (muInv c d).1 (muInv c d).2 = (c, d) := by decide

/-- The edge-product value of a pair on a log-modulus row. -/
def SL (L : Fin 6 → ℚ) (p : Fin 6 × Fin 6) : ℚ := L p.1 + L p.2

/-- The pulled-back four-cycle identities: for every ascending target quadruple, both independent
matching identities hold on the μ-preimages. -/
def PulledRel (L : Fin 6 → ℚ) : Prop :=
  ∀ c d e f : Fin 6, c < d → d < e → e < f →
    SL L (muInv c d) + SL L (muInv e f) = SL L (muInv c e) + SL L (muInv d f)
    ∧ SL L (muInv c d) + SL L (muInv e f) = SL L (muInv c f) + SL L (muInv d e)

/-- THE MODULUS ENDPOINT: L_μ^⊥ = span(1). A log-modulus row satisfies every pulled-back
four-cycle identity iff it is constant — the exceptional locus is exactly the flat row. -/
theorem flat_locus (L : Fin 6 → ℚ) : PulledRel L ↔ ∀ i, L i = L 0 := by
  constructor
  · intro h
    have h1 := (h 0 1 3 4 (by decide) (by decide) (by decide)).1
    have h2 := (h 1 2 3 4 (by decide) (by decide) (by decide)).1
    have h3 := (h 0 2 3 5 (by decide) (by decide) (by decide)).1
    have h4 := (h 0 1 2 5 (by decide) (by decide) (by decide)).2
    have h5 := (h 0 1 2 3 (by decide) (by decide) (by decide)).1
    rw [show muInv 0 1 = (0,1) from rfl, show muInv 3 4 = (3,4) from rfl,
      show muInv 0 3 = (1,4) from rfl, show muInv 1 4 = (0,4) from rfl] at h1
    rw [show muInv 1 2 = (3,5) from rfl, show muInv 3 4 = (3,4) from rfl,
      show muInv 1 3 = (0,3) from rfl, show muInv 2 4 = (4,5) from rfl] at h2
    rw [show muInv 0 2 = (2,4) from rfl, show muInv 3 5 = (2,3) from rfl,
      show muInv 0 3 = (1,4) from rfl, show muInv 2 5 = (1,3) from rfl] at h3
    rw [show muInv 0 1 = (0,1) from rfl, show muInv 2 5 = (1,3) from rfl,
      show muInv 0 5 = (0,5) from rfl, show muInv 1 2 = (3,5) from rfl] at h4
    rw [show muInv 0 1 = (0,1) from rfl, show muInv 2 3 = (1,2) from rfl,
      show muInv 0 2 = (2,4) from rfl, show muInv 1 3 = (0,3) from rfl] at h5
    simp only [SL] at h1 h2 h3 h4 h5
    have g1 : L 1 = L 0 := by linarith
    have g2 : L 2 = L 0 := by linarith
    have g3 : L 3 = L 0 := by linarith
    have g4 : L 4 = L 0 := by linarith
    have g5 : L 5 = L 0 := by linarith
    intro i
    fin_cases i <;> first | rfl | exact g1 | exact g2 | exact g3 | exact g4 | exact g5
  · intro h c d e f _ _ _
    constructor <;> · simp only [SL, h]

/-- μ is genuinely non-two-branch: no vertex map induces it, in either orientation, even with
orientations mixed edge by edge. Proof by `flat_locus` itself: a vertex-induced μ would make
`M ∘ τ` satisfy every pulled-back identity for EVERY `M` (each matching sum telescopes to
`M c + M d + M e + M f`), so `M ∘ τ` would always be constant — but `mu 0 1 = (0, 1)` forces
`τ 0 ≠ τ 1`, and an `M` separating those two values is non-constant on τ's range. -/
theorem mu_not_vertex_induced :
    ¬∃ τ : Fin 6 → Fin 6, ∀ a b : Fin 6, a < b →
      (mu a b = (τ a, τ b) ∨ mu a b = (τ b, τ a)) := by
  rintro ⟨τ, hτ⟩
  have h01 : τ 0 ≠ τ 1 := by
    rcases hτ 0 1 (by decide) with h | h <;>
    · rw [show mu 0 1 = (0, 1) from rfl, Prod.mk.injEq] at h
      intro heq
      rw [← h.1, ← h.2] at heq
      exact absurd heq (by decide)
  have hrel : ∀ M : Fin 6 → ℚ, PulledRel (fun v => M (τ v)) := by
    intro M c d e f hcd hde hef
    have key : ∀ x y : Fin 6, x < y →
        SL (fun v => M (τ v)) (muInv x y) = M x + M y := by
      intro x y hxy
      obtain ⟨hasc, hmu⟩ := mu_muInv x y hxy
      have h2 := hτ (muInv x y).1 (muInv x y).2 hasc
      rw [hmu] at h2
      simp only [SL]
      rcases h2 with h | h
      · rw [Prod.mk.injEq] at h
        rw [← h.1, ← h.2]
      · rw [Prod.mk.injEq] at h
        rw [← h.1, ← h.2]
        ring
    rw [key c d hcd, key e f hef, key c e (lt_trans hcd hde), key d f (lt_trans hde hef),
      key c f (lt_trans (lt_trans hcd hde) hef), key d e hde]
    constructor <;> ring
  have hconst := (flat_locus fun v => if τ v = τ 0 then (0 : ℚ) else 1).mp
    (hrel fun t => if t = τ 0 then (0 : ℚ) else 1) 1
  rw [if_neg (fun h : τ 1 = τ 0 => h01 h.symm), if_pos rfl] at hconst
  exact one_ne_zero hconst

/-- The V-side monomial x-exponents on the phase kernel (ξ = s·u2 + t·u3 per row). -/
def u2 : Fin 6 → ℕ
  | 0 => 0 | 1 => 1 | 2 => 0 | 3 => 2 | 4 => 4 | 5 => 5

/-- The shared y-exponents: the V'-side table w3 + 2 coincides with u3. -/
def u3 : Fin 6 → ℕ
  | 0 => 0 | 1 => 0 | 2 => 1 | 3 => 2 | 4 => 2 | 5 => 3

/-- The V'-side x-exponent table (η = s·w2 + t·w3, here shifted by the gauge +3). -/
def w2 : Fin 6 → ℤ
  | 0 => -3 | 1 => -2 | 2 => 1 | 3 => 0 | 4 => 2 | 5 => 2

def w3 : Fin 6 → ℤ
  | 0 => -2 | 1 => -2 | 2 => -1 | 3 => 0 | 4 => 0 | 5 => 1

/-- THE LINKAGE: the ξ/η exponent identity `ξ_a − ξ_b = η_c − η_d` on all fifteen edges, which is
what makes V' monomial in the SAME two torus parameters as V. -/
theorem linkage : ∀ a b : Fin 6, a < b →
    (u2 a : ℤ) - u2 b = w2 (mu a b).1 - w2 (mu a b).2
    ∧ (u3 a : ℤ) - u3 b = w3 (mu a b).1 - w3 (mu a b).2 := by decide

/-- The V-side mask factors over ℤ. -/
theorem maskV_factor (x y : ℤ) :
    1 + x + y + x^2*y^2 + x^4*y^2 + x^5*y^3
      = (1 + x + x^2*y) * (1 + y - x*y + x^3*y^2) := by ring

/-- The V'-side mask factors over ℤ with the SAME first factor — the shared cube-root component
that survives on both sides. -/
theorem maskW_factor (x y : ℤ) :
    1 + x + x^4*y + x^3*y^2 + x^5*y^2 + x^5*y^3
      = (1 + x + x^2*y) * (1 - x^2*y + x^3*y + x^3*y^2) := by ring

/-- The V-side mask IS the exponent-table sum. -/
theorem maskV_eq_sum (x y : ℤ) :
    (∑ a, x ^ u2 a * y ^ u3 a)
      = 1 + x + y + x^2*y^2 + x^4*y^2 + x^5*y^3 := by
  rw [Fin.sum_univ_six]
  show x ^ u2 0 * y ^ u3 0 + x ^ u2 1 * y ^ u3 1 + x ^ u2 2 * y ^ u3 2
      + x ^ u2 3 * y ^ u3 3 + x ^ u2 4 * y ^ u3 4 + x ^ u2 5 * y ^ u3 5 = _
  norm_num [u2, u3]

/-- The eight allowed differences: the common torus zeros of both masks, as exponent pairs in
ℤ/12 × ℤ/4 (x = ζ₁₂^a, y = i^b). Their completeness is the probe-level resultant computation. -/
def conn : Finset (ZMod 12 × ZMod 4) :=
  {(4,0), (8,0), (0,1), (0,3), (3,2), (9,2), (3,3), (9,1)}

theorem conn_symm : ∀ z ∈ conn, -z ∈ conn := by decide

theorem zero_not_mem_conn : (0 : ZMod 12 × ZMod 4) ∉ conn := by decide

/-- THE CLIQUE ENDPOINT, base case: no three connection-set elements are pairwise connected —
i.e. the Cayley graph on the allowed differences has no 4-clique (through 0, hence anywhere). -/
theorem no_four_clique : ∀ x ∈ conn, ∀ y ∈ conn, ∀ z ∈ conn,
    ¬(y - x ∈ conn ∧ z - x ∈ conn ∧ z - y ∈ conn) := by decide

/-- THE UNITARITY ENDPOINT: no six points of the parameter torus quotient have all pairwise
differences among the allowed eight — six mutually orthogonal rows for V and V' jointly are
impossible. (Four points already are.) -/
theorem no_six_orthogonal :
    ¬∃ P : Fin 6 → ZMod 12 × ZMod 4, ∀ i j : Fin 6, i ≠ j → P i - P j ∈ conn := by
  rintro ⟨P, hP⟩
  refine no_four_clique (P 1 - P 0) (hP 1 0 (by decide))
    (P 2 - P 0) (hP 2 0 (by decide)) (P 3 - P 0) (hP 3 0 (by decide)) ⟨?_, ?_, ?_⟩
  · rw [sub_sub_sub_cancel_right]; exact hP 2 1 (by decide)
  · rw [sub_sub_sub_cancel_right]; exact hP 3 1 (by decide)
  · rw [sub_sub_sub_cancel_right]; exact hP 3 2 (by decide)

/-- SHARPNESS: three mutually connected points exist, so the clique number is exactly three. -/
theorem three_clique :
    ((0,1) : ZMod 12 × ZMod 4) ∈ conn ∧ ((3,3) : ZMod 12 × ZMod 4) ∈ conn
    ∧ (((3,3) : ZMod 12 × ZMod 4) - (0,1)) ∈ conn := by decide

#print axioms golomb_r1
#print axioms golomb_r2
#print axioms mu_gap
#print axioms mu_forced
#print axioms muInv_mu
#print axioms mu_muInv
#print axioms mu_not_vertex_induced
#print axioms flat_locus
#print axioms linkage
#print axioms maskV_factor
#print axioms maskW_factor
#print axioms maskV_eq_sum
#print axioms conn_symm
#print axioms no_four_clique
#print axioms no_six_orthogonal
#print axioms three_clique

end HomometricSix
end OIBridge
