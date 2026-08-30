/-
  OIBridge/PiccardBridge.lean — the parametric μ-orbit bridge to the Piccard exceptional family.

  PROVENANCE, NOW AT PRIMARY-SOURCE LEVEL. Bekir–Golomb, "There Are No Further Counterexamples
  to S. Piccard's Theorem", IEEE Trans. Inform. Theory 53(8) (2007) 2864–2867 (p. 2865, family
  attributed to Yovanof–Golomb, ARS Combinatoria 48 (1998) 43–48), represents the unique
  exceptional family of six-mark homometric spanning-ruler pairs by the two-parameter
  factorization

      r(x) = Φ₁(x)Φ₂(x)  = (1 + xᵃ + xᵇ)(1 + x^{b−2a} − x^{b−a} + x^{2b−a})
      s(x) = Φ₁(x)Φ₂*(x) = (1 + xᵃ + xᵇ)(1 − xᵇ + x^{b+a} + x^{2b−a}),

  with Φ₂* the reversal of Φ₂. Expanding (the mixed terms cancel in pairs) gives exactly, with
  (p₁, p₂) = (a, b), the mark lists this file formalizes — confirming the formula previously
  known only through a quoting treatment:

      X = {0, p₁, p₂ − 2p₁, 2p₂ − 2p₁, 2p₂, 3p₂ − p₁}
      Y = {0, p₁, 2p₁ + p₂, p₁ + 2p₂, 2p₂ − p₁, 3p₂ − p₁}.

  `piccard_factor_r` / `piccard_factor_s` below kernel-verify those expansions in chamber
  coordinates s = x^{p₁}, t = x^{p₂−2p₁} (every mark is a ℕ-combination i·p₁ + j·(p₂−2p₁);
  `piccardX_marks` / `piccardY_marks` pin the exponent bookkeeping), so the whole chain — primary
  factorization → mark lists → μ-orbit — is kernel-checked. AUDIT CAVEAT THAT REMAINS: the 2007
  text presents its polynomial model with integer marks-as-exponents and never explicitly
  quantifies over real configurations; its Section III argument manipulates symbolic exponents
  through linear relations only (hence is domain-agnostic), but the real-scope reading is an
  interpretation, recorded in the ledger, not a sentence of the paper. This bridge already
  delivers the third alternative of `twoBranch_of_spectral_classification` in its verbatim shape.

  THE BRIDGE. With source labels untouched (e_S = id) and the single target transposition
  e_T = (3 4) — which merely aligns the quoted LISTED order of Y with ascending order, since
  Y₃ > Y₄ in the printed chamber — all fifteen gap identities

      Y_{e_T(μ(a,b)₂)} − Y_{e_T(μ(a,b)₁)} = X_b − X_a     (a < b)

  hold as polynomial identities in p₁, p₂ over any commutative ring: no chamber restriction, no
  choice of Bloom's numerical example. The companion probe (gap_correspondence_probe M11) checks
  in exact arithmetic that (3 4) is the UNIQUE permutation of target labels with this property,
  that both families are symbolically Golomb (no gap collision as linear forms), and that the
  specialization p = (1, 6) is the printed pair {0,1,4,10,12,17} / {0,1,8,11,13,17}.
-/
import OIBridge.HomometricSix

namespace OIBridge
namespace HomometricSix

variable {K : Type*} [CommRing K]

/-- The quoted exceptional source family, in the quoted LISTED order. -/
def piccardX (p1 p2 : K) : Fin 6 → K
  | 0 => 0 | 1 => p1 | 2 => p2 - 2 * p1 | 3 => 2 * p2 - 2 * p1 | 4 => 2 * p2
  | 5 => 3 * p2 - p1

/-- The quoted exceptional target family, in the quoted LISTED order (NOT ascending: in the
printed chamber `Y 3 > Y 4`, which is exactly why the bridge needs the transposition below). -/
def piccardY (p1 p2 : K) : Fin 6 → K
  | 0 => 0 | 1 => p1 | 2 => 2 * p1 + p2 | 3 => p1 + 2 * p2 | 4 => 2 * p2 - p1
  | 5 => 3 * p2 - p1

/-- The alignment transposition (3 4) between the quoted listed order and ascending order. -/
def alignT : Fin 6 → Fin 6
  | 3 => 4 | 4 => 3 | i => i

/-- `alignT` as an equivalence — it is its own inverse. -/
def alignEquiv : Fin 6 ≃ Fin 6 := ⟨alignT, alignT, by decide, by decide⟩

/-- **THE PARAMETRIC μ-ORBIT BRIDGE.** Over any commutative ring, with source labels untouched
and targets realigned by the single transposition (3 4), the quoted exceptional family satisfies
all fifteen gap identities of the forced correspondence μ — as polynomial identities in
`p₁, p₂`, independent of any chamber or specialization. -/
theorem piccard_mu_bridge (p1 p2 : K) : ∀ a b : Fin 6, a < b →
    piccardY p1 p2 (alignT (mu a b).2) - piccardY p1 p2 (alignT (mu a b).1)
      = piccardX p1 p2 b - piccardX p1 p2 a := by
  intro a b hab
  fin_cases a <;> fin_cases b <;> try exact absurd hab (by decide)
  · show p1 - 0 = p1 - 0; ring
  · show (3 * p2 - p1) - (p1 + 2 * p2) = (p2 - 2 * p1) - 0; ring
  · show (2 * p2 - p1) - p1 = (2 * p2 - 2 * p1) - 0; ring
  · show (p1 + 2 * p2) - p1 = 2 * p2 - 0; ring
  · show (3 * p2 - p1) - 0 = (3 * p2 - p1) - 0; ring
  · show (2 * p2 - p1) - (2 * p1 + p2) = (p2 - 2 * p1) - p1; ring
  · show (3 * p2 - p1) - (2 * p1 + p2) = (2 * p2 - 2 * p1) - p1; ring
  · show (2 * p2 - p1) - 0 = 2 * p2 - p1; ring
  · show (3 * p2 - p1) - p1 = (3 * p2 - p1) - p1; ring
  · show (3 * p2 - p1) - (2 * p2 - p1) = (2 * p2 - 2 * p1) - (p2 - 2 * p1); ring
  · show (2 * p1 + p2) - 0 = 2 * p2 - (p2 - 2 * p1); ring
  · show (p1 + 2 * p2) - 0 = (3 * p2 - p1) - (p2 - 2 * p1); ring
  · show (p1 + 2 * p2) - (2 * p2 - p1) = 2 * p2 - (2 * p2 - 2 * p1); ring
  · show (2 * p1 + p2) - p1 = (3 * p2 - p1) - (2 * p2 - 2 * p1); ring
  · show (p1 + 2 * p2) - (2 * p1 + p2) = (3 * p2 - p1) - 2 * p2; ring

/-- The bridge in the VERBATIM shape of the third alternative of
`twoBranch_of_spectral_classification`'s classification premise (at `m = 6`): the quoted family
realizes the exceptional gap correspondence μ through explicit equivalences. -/
theorem piccard_realizes_mu (p1 p2 : K) :
    ∃ eS eT : Fin 6 ≃ Fin 6, ∀ a b : Fin 6, a < b →
      piccardY p1 p2 (eT (mu a b).2) - piccardY p1 p2 (eT (mu a b).1)
        = piccardX p1 p2 (eS b) - piccardX p1 p2 (eS a) :=
  ⟨Equiv.refl _, alignEquiv, fun a b hab => piccard_mu_bridge p1 p2 a b hab⟩

/-- The printed pair is the specialization `p = (1, 6)`: the source family is `r1` verbatim. -/
theorem piccardX_at_printed : ∀ i, piccardX (1 : ℤ) 6 i = r1 i := by decide

/-- ... and the target family is `r2` composed with the alignment transposition — the quoted
listed order differs from ascending order exactly at labels 3, 4. -/
theorem piccardY_at_printed : ∀ i, piccardY (1 : ℤ) 6 i = r2 (alignT i) := by decide

/-! ### The primary factorization (Bekir–Golomb 2007, p. 2865), kernel-verified

In chamber coordinates `s = x^{p₁}`, `t = x^{p₂−2p₁}` every exponent of the two-parameter
representation is a ℕ-combination, and the products expand — with the printed cancellations —
to 0/1-coefficient six-term sums: valid spanning-ruler polynomials. -/

/-- `Φ₁·Φ₂` expands to the six source marks: the exponent pairs `(i, j)` of the right-hand
side are exactly `expX` below. -/
theorem piccard_factor_r (s t : K) :
    (1 + s + s ^ 2 * t) * (1 + t - s * t + s ^ 3 * t ^ 2)
      = 1 + s + t + s ^ 2 * t ^ 2 + s ^ 4 * t ^ 2 + s ^ 5 * t ^ 3 := by ring

/-- `Φ₁·Φ₂*` (with `Φ₂*` the reversal of `Φ₂`) expands to the six target marks: the exponent
pairs of the right-hand side are exactly `expY` below. -/
theorem piccard_factor_s (s t : K) :
    (1 + s + s ^ 2 * t) * (1 - s ^ 2 * t + s ^ 3 * t + s ^ 3 * t ^ 2)
      = 1 + s + s ^ 3 * t ^ 2 + s ^ 4 * t + s ^ 5 * t ^ 2 + s ^ 5 * t ^ 3 := by ring

/-- The `(s, t)`-exponent pairs of `Φ₁·Φ₂`, in the listed order of `piccardX`. -/
def expX : Fin 6 → ℕ × ℕ
  | 0 => (0, 0) | 1 => (1, 0) | 2 => (0, 1) | 3 => (2, 2) | 4 => (4, 2) | 5 => (5, 3)

/-- The `(s, t)`-exponent pairs of `Φ₁·Φ₂*`, in the listed order of `piccardY`. -/
def expY : Fin 6 → ℕ × ℕ
  | 0 => (0, 0) | 1 => (1, 0) | 2 => (4, 1) | 3 => (5, 2) | 4 => (3, 2) | 5 => (5, 3)

/-- The chamber substitution: the mark carried by the `(s, t)`-exponent pair `(i, j)`. -/
def markOf (p1 p2 : K) (e : ℕ × ℕ) : K := (e.1 : K) * p1 + (e.2 : K) * (p2 - 2 * p1)

/-- The exponent bookkeeping for the source family: `piccardX` IS the mark list of the
`Φ₁·Φ₂` expansion. -/
theorem piccardX_marks (p1 p2 : K) : ∀ i, piccardX p1 p2 i = markOf p1 p2 (expX i) := by
  intro i
  fin_cases i
  · show (0 : K) = ((0 : ℕ) : K) * p1 + ((0 : ℕ) : K) * (p2 - 2 * p1); push_cast; ring
  · show p1 = ((1 : ℕ) : K) * p1 + ((0 : ℕ) : K) * (p2 - 2 * p1); push_cast; ring
  · show p2 - 2 * p1 = ((0 : ℕ) : K) * p1 + ((1 : ℕ) : K) * (p2 - 2 * p1); push_cast; ring
  · show 2 * p2 - 2 * p1 = ((2 : ℕ) : K) * p1 + ((2 : ℕ) : K) * (p2 - 2 * p1)
    push_cast; ring
  · show 2 * p2 = ((4 : ℕ) : K) * p1 + ((2 : ℕ) : K) * (p2 - 2 * p1); push_cast; ring
  · show 3 * p2 - p1 = ((5 : ℕ) : K) * p1 + ((3 : ℕ) : K) * (p2 - 2 * p1); push_cast; ring

/-- The exponent bookkeeping for the target family: `piccardY` IS the mark list of the
`Φ₁·Φ₂*` expansion. -/
theorem piccardY_marks (p1 p2 : K) : ∀ i, piccardY p1 p2 i = markOf p1 p2 (expY i) := by
  intro i
  fin_cases i
  · show (0 : K) = ((0 : ℕ) : K) * p1 + ((0 : ℕ) : K) * (p2 - 2 * p1); push_cast; ring
  · show p1 = ((1 : ℕ) : K) * p1 + ((0 : ℕ) : K) * (p2 - 2 * p1); push_cast; ring
  · show 2 * p1 + p2 = ((4 : ℕ) : K) * p1 + ((1 : ℕ) : K) * (p2 - 2 * p1); push_cast; ring
  · show p1 + 2 * p2 = ((5 : ℕ) : K) * p1 + ((2 : ℕ) : K) * (p2 - 2 * p1); push_cast; ring
  · show 2 * p2 - p1 = ((3 : ℕ) : K) * p1 + ((2 : ℕ) : K) * (p2 - 2 * p1); push_cast; ring
  · show 3 * p2 - p1 = ((5 : ℕ) : K) * p1 + ((3 : ℕ) : K) * (p2 - 2 * p1); push_cast; ring

#print axioms piccard_mu_bridge
#print axioms piccard_realizes_mu
#print axioms piccardX_at_printed
#print axioms piccardY_at_printed
#print axioms piccard_factor_r
#print axioms piccard_factor_s
#print axioms piccardX_marks
#print axioms piccardY_marks

end HomometricSix
end OIBridge
