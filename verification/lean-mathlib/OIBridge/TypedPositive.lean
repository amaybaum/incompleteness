import OIBridge.TypedCompletion
import OIBridge.PositiveReachability

/-!
# The typed determination from the package without dagger stability

`TypedCompletion.typed_determined_of_oiPlusElem` reads the typed characterization from
`OIPlusElem` on every shadow. `PositiveReachability.oiPlusPos_iff_oiPlusElem` makes the two
packages equivalent on every nonempty finite carrier, so the same typed conclusion follows from
`OIPlusPos` — implementation locality, elementary transition richness, embedded observation, with
no dagger stability and no inverse accessibility assumed. One result, so that the manuscript's
typed form cites the current package.
-/

namespace OIBridge
namespace TypedPositive

open TypedCompletion PositiveReachability

/-- **THE TYPED CHARACTERIZATION FROM THE PACKAGE WITHOUT DAGGER STABILITY**: if every shadow
satisfies `OIPlusPos`, the typed theory is the finite typed quantum theory. -/
theorem typed_determined_of_oiPlusPos (𝒯 : TypedOperationalTheory)
    (h : ∀ (A : Type) [Fintype A] [DecidableEq A] [Nonempty A], OIPlusPos (𝒯.shadow A)) :
    ∀ (S S' : Type) [Fintype S] [DecidableEq S] [Fintype S'] [DecidableEq S'] [Nonempty S]
      [Nonempty S'] (m : ℕ) (F : Fin m → Matrix S S ℂ →ₗ[ℂ] Matrix S' S' ℂ),
      𝒯.availT S S' (Fin m) F ↔ IsTypedKrausInstrument F :=
  typed_determined_of_oiPlusElem 𝒯 fun A _ _ _ =>
    (oiPlusPos_iff_oiPlusElem (𝒯.shadow A)).mp (h A)

#print axioms typed_determined_of_oiPlusPos

end TypedPositive
end OIBridge
