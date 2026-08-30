/-
  OIBridge/PiccardBridge.lean — the parametric μ-orbit bridge to the Piccard exceptional family.

  PROVENANCE, STATED EXACTLY. A later peer-reviewed treatment citing Bekir–Golomb (IEEE Trans.
  Inform. Theory 53(8) (2007) 2864–2867) quotes the sole exceptional six-point family, in listed
  order and parameterized by (p₁, p₂) ∈ ℝ²:

      X = {0, p₁, p₂ − 2p₁, 2p₂ − 2p₁, 2p₂, 3p₂ − p₁}
      Y = {0, p₁, 2p₁ + p₂, p₁ + 2p₂, 2p₂ − p₁, 3p₂ − p₁}.

  THE PRIMARY 2007 TEXT HAS NOT YET BEEN AUDITED: what this file proves is a statement about the
  QUOTED formula, namely that it induces exactly the repository's forced correspondence μ — the
  same μ-orbit that `homometricSix_unrealizable` kills. When the primary paper confirms (1) the
  arbitrary-real distinct-difference scope and (2) this family up to equivalent parameterization,
  the K2 consumption of the classification is immediate: this bridge already delivers the third
  alternative of `twoBranch_of_spectral_classification` in its verbatim shape.

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

#print axioms piccard_mu_bridge
#print axioms piccard_realizes_mu
#print axioms piccardX_at_printed
#print axioms piccardY_at_printed

end HomometricSix
end OIBridge
