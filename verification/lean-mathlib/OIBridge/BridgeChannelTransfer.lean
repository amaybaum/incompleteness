/-!
  Round-six channel transfer bridge — design source.

  The O14 availability/convergence witness is an explicit hypothesis of this module.
  The protocol itself and density of powers are not formalized here.
  Closedness is needed for the limit; self-duality supplies it through EqvOneDictionary.
  No closure of the availability predicate, or exact availability of the limit, is used.
-/
import OIBridge.BridgeOpDrive
import OIBridge.EqvOneDictionary
import OIBridge.EqvK2Generation

namespace OIBridge
namespace BridgeChannelTransfer

open CompositeDimension MonoidalCompletion CoherentExtension InterventionLocality
open ReferenceExtension EqvK2Schema BridgeAvail
open scoped Topology

noncomputable section

abbrev OneChannel := Matrix (Fin 2) (Fin 2) ℂ →ₗ[ℂ] Matrix (Fin 2) (Fin 2) ℂ
abbrev PairMatrix := Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ

/-- The kernel's spectator extension, followed by the same pair dictionary inverse. -/
def channelTransfer (Φ : OneChannel) (ω : W 3) : W 3 :=
  coordOf (amplRefL (Fin 2) Φ (BridgeDictionary.dict ω))

/-- Transfer of actual one-outcome instrument-realized channels. Introduced compatibility
between implementation availability and the P-level cone, rather than a theorem of availability. -/
def ChannelTransferClause (𝓘 : ImplementationClass) (K : Set (W 3)) : Prop :=
  ∀ Φ : OneChannel, InstAvail 𝓘 (Fin 2) Unit (fun _ => Φ) →
    ∀ ω ∈ K, channelTransfer Φ ω ∈ K

/-- An available-channel approximation, with its convergence on every transferred table.
O14 gives a written protocol and exact checks for this witness at zPh; this definition
does not supply that witness and asserts no availability of the limiting unitary. -/
def AvailableChannelApproximation (𝓘 : ImplementationClass)
    (U : Matrix (Fin 2) (Fin 2) ℂ) : Prop :=
  ∃ Φ : ℕ → OneChannel,
    (∀ k, InstAvail 𝓘 (Fin 2) Unit (fun _ => Φ k)) ∧
    ∀ ω : W 3, Filter.Tendsto (fun k => channelTransfer (Φ k) ω) Filter.atTop
      (𝓝 (BridgeConverge.transferMap U ω))

theorem channelTransfer_conjChannel (U : Matrix (Fin 2) (Fin 2) ℂ) (ω : W 3) :
    channelTransfer (conjChannel U) ω = BridgeConverge.transferMap U ω := by
  unfold channelTransfer
  rw [amplRefL_conjChannel]
  rfl

/-- Channel transfer implies the existing unitary transfer clause. -/
theorem unitaryTransfer_of_channelTransfer {𝓘 : ImplementationClass} {K : Set (W 3)}
    (hT : ChannelTransferClause 𝓘 K) : BridgeDictionary.TransferClause 𝓘 K := by
  apply (BridgeConverge.transferClause_iff 𝓘 K).mpr
  intro U hU hu ω hω
  have h := hT (conjChannel U) (InstAvail.op U hU hu) ω hω
  simpa only [channelTransfer_conjChannel] using h

/-- Operational validity on an identified state space gives channel transfer. The
identification and validity are separate hypotheses; neither is sourced by this theorem. -/
theorem channelTransfer_of_identified_stateSpace (𝓘 : ImplementationClass) (K : Set (W 3))
    (C : Set PairMatrix) (hId : C = BridgeDictionary.dict '' K)
    (hValid : ∀ Φ : OneChannel, InstAvail 𝓘 (Fin 2) Unit (fun _ => Φ) →
      ∀ X ∈ C, amplRefL (Fin 2) Φ X ∈ C) : ChannelTransferClause 𝓘 K := by
  intro Φ hΦ ω hω
  have hX : BridgeDictionary.dict ω ∈ C := by
    rw [hId]
    exact ⟨ω, hω, rfl⟩
  have hOut := hValid Φ hΦ _ hX
  rw [hId] at hOut
  rcases hOut with ⟨η, hη, he⟩
  change coordOf (amplRefL (Fin 2) Φ (BridgeDictionary.dict ω)) ∈ K
  rw [← he, BridgeConverge.dict_converge, coordOf_dict]
  exact hη

/-- Positive control at the quantum cone. This uses the target's PSD definition and
therefore is not a derivation of transfer for an arbitrary pair cone. -/
theorem channelTransfer_Q3 (𝓘 : ImplementationClass) :
    ChannelTransferClause 𝓘 Q3 := by
  intro Φ hΦ ω hω
  have hωP : (BridgeDictionary.dict ω).PosSemidef := by
    rw [BridgeConverge.dict_converge]
    exact hω
  have hp : (amplRefL (Fin 2) Φ (BridgeDictionary.dict ω)).PosSemidef :=
    cp_referencePositive (Fin 2) Φ (cp_of_instAvail hΦ ()) _ hωP
  change (dict (coordOf (amplRefL (Fin 2) Φ (BridgeDictionary.dict ω)))).PosSemidef
  rw [dict_coordOf _ hp.isHermitian]
  exact hp

/-- A closed cone invariant under the available approximating channels is invariant
under their unitary limit. No limit is added to InstAvail. -/
theorem transfer_of_channelApproximation {𝓘 : ImplementationClass} {K : Set (W 3)}
    {U : Matrix (Fin 2) (Fin 2) ℂ} (hK : IsClosed K) (hT : ChannelTransferClause 𝓘 K)
    (hApprox : AvailableChannelApproximation 𝓘 U) :
    ∀ ω ∈ K, BridgeConverge.transferMap U ω ∈ K := by
  obtain ⟨Φ, hΦ, hlim⟩ := hApprox
  intro ω hω
  exact hK.mem_of_tendsto (hlim ω)
    (Filter.Eventually.of_forall fun k => hT (Φ k) (hΦ k) ω hω)

/-- O14's candidate against the bridge's actual two generator tables. The RUS witness
remains explicit. J is transferred as an available channel, so no ray-saturation
hypothesis is needed in this lemma. -/
theorem bridge_channel_half {𝓘 : ImplementationClass} {K : Set (W 3)}
    (hK : IsClosed K) (hT : ChannelTransferClause 𝓘 K)
    (hRUS : AvailableChannelApproximation 𝓘 zPh)
    (hJ : InstAvail 𝓘 (Fin 2) Unit (fun _ => conjChannel uJ)) :
    ∀ ω ∈ K, actT (BridgeDictionary.rotZ (3 / 5) (4 / 5)) ω ∈ K ∧
      actT (KInfFoundations.cycEquiv : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) ω ∈ K := by
  intro ω hω
  constructor
  · rw [← BridgeOpDrive.transferMap_zPh]
    exact transfer_of_channelApproximation hK hT hRUS ω hω
  · rw [← BridgeOpDrive.transferMap_uJ, ← channelTransfer_conjChannel]
    exact hT (conjChannel uJ) hJ ω hω

/-- In E19's setting, closedness follows from H3 rather than being a further premise. -/
theorem bridge_channel_half_of_selfDual {𝓘 : ImplementationClass} {K : Set (W 3)}
    (hH3 : K = dualW K) (hT : ChannelTransferClause 𝓘 K)
    (hRUS : AvailableChannelApproximation 𝓘 zPh)
    (hJ : InstAvail 𝓘 (Fin 2) Unit (fun _ => conjChannel uJ)) :
    ∀ ω ∈ K, actT (BridgeDictionary.rotZ (3 / 5) (4 / 5)) ω ∈ K ∧
      actT (KInfFoundations.cycEquiv : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) ω ∈ K :=
  bridge_channel_half (EqvOneDictionary.isClosed_of_selfDual hH3) hT hRUS hJ

end
end BridgeChannelTransfer
end OIBridge

#print axioms OIBridge.BridgeChannelTransfer.channelTransfer_conjChannel
#print axioms OIBridge.BridgeChannelTransfer.unitaryTransfer_of_channelTransfer
#print axioms OIBridge.BridgeChannelTransfer.channelTransfer_of_identified_stateSpace
#print axioms OIBridge.BridgeChannelTransfer.channelTransfer_Q3
#print axioms OIBridge.BridgeChannelTransfer.transfer_of_channelApproximation
#print axioms OIBridge.BridgeChannelTransfer.bridge_channel_half
#print axioms OIBridge.BridgeChannelTransfer.bridge_channel_half_of_selfDual
