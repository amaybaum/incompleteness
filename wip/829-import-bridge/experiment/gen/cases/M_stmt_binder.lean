import FiniteReachTable

namespace FiniteReconstructionDesign.Mutation

open Matrix
open OIBridge.MonoidalCompletion OIBridge.EqvK2Schema OIBridge.EqvK2Converse
  OIBridge.EqvK2Block OIBridge.EqvK2Generation OIBridge.CompositeDimension
open scoped ComplexOrder

set_option linter.unusedVariables false in
theorem pairCone_eq_Q3_of_kToken (K : Set (W 3))
    (hH1 : ∀ x ∈ OIBridge.TransitiveBody.eball 3, ∀ y ∈ OIBridge.TransitiveBody.eball 3,
      prodState x y ∈ K)
    (hadd : ∀ ω ∈ K, ∀ η ∈ K, ω + η ∈ K)
    (hsmul : ∀ c : ℝ, 0 ≤ c → ∀ ω ∈ K, c • ω ∈ K)
    (hmax : K ⊆ maxCone (OIBridge.TransitiveBody.eball 3))
    (hH2 : ∀ ω ∈ K, cnot ω ∈ K)
    (hA : ∀ t : ℝ, ∀ ω ∈ K, actT (OIBridge.KInfFoundations.rotLin t) ω ∈ K ∧
      actT (OIBridge.KInfFoundations.cycEquiv : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) ω ∈ K) :
    K = Q3 :=
  @FiniteReconstructionDesign.pairCone_eq_Q3_of_kToken K hH1 hadd hsmul hmax hH2 hA

end FiniteReconstructionDesign.Mutation

/- Executable control STMT-IDENTITY (meta-level; the `example` is a kernel-checked `rfl`). The
   recovery's statement and the adopted theorem's must be alpha-equivalent (`==`, which ignores
   binder names and binder annotations: Lean/Expr.lean `instance : BEq Expr := ⟨Expr.eqv⟩`), carry
   the same binder annotations in traversal order, and the same outermost hypothesis names. Plain
   `Expr.equal` is not used: it also compares hygienic binder names, which carry the declaring
   module in their macro scopes. -/
namespace ImportBridge

partial def binderInfos : Lean.Expr → Array Lean.BinderInfo
  | .forallE _ t b bi => #[bi] ++ binderInfos t ++ binderInfos b
  | .lam _ t b bi => #[bi] ++ binderInfos t ++ binderInfos b
  | .app f a => binderInfos f ++ binderInfos a
  | .letE _ t v b _ => binderInfos t ++ binderInfos v ++ binderInfos b
  | .mdata _ e => binderInfos e
  | .proj _ _ e => binderInfos e
  | _ => #[]

partial def topBinderNames : Lean.Expr → List Lean.Name
  | .forallE n _ b _ => n :: topBinderNames b
  | .mdata _ e => topBinderNames e
  | _ => []

end ImportBridge

example : type_of% @FiniteReconstructionDesign.Mutation.pairCone_eq_Q3_of_kToken =
    type_of% @OIBridge.EqvK2MaxCone.pairCone_eq_Q3_of_drive_maxCone := rfl

open Lean in
#eval show Lean.Meta.MetaM Unit from do
  let r ← getConstInfo `FiniteReconstructionDesign.Mutation.pairCone_eq_Q3_of_kToken
  let p ← getConstInfo `OIBridge.EqvK2MaxCone.pairCone_eq_Q3_of_drive_maxCone
  unless r.levelParams == p.levelParams do
    throwError "STMT-IDENTITY universe parameters differ"
  unless r.type == p.type do
    throwError "STMT-IDENTITY the statements are not alpha-equivalent"
  unless ImportBridge.binderInfos r.type == ImportBridge.binderInfos p.type do
    throwError "STMT-IDENTITY binder annotations differ"
  unless ImportBridge.topBinderNames r.type == ImportBridge.topBinderNames p.type do
    throwError "STMT-IDENTITY hypothesis names differ"
  logInfo "STMT-IDENTITY ok"
