import FiniteReachTable

namespace FiniteReconstructionDesign.Mutation

open Matrix
open OIBridge.MonoidalCompletion OIBridge.EqvK2Schema OIBridge.EqvK2Converse
  OIBridge.EqvK2Block OIBridge.EqvK2Generation OIBridge.CompositeDimension
open scoped ComplexOrder

set_option linter.unusedVariables false in
theorem pairCone_eq_Q3_of_kToken {K : Set (W 3)}
    (hH1 : ∀ x ∈ OIBridge.TransitiveBody.eball 3, ∀ y ∈ OIBridge.TransitiveBody.eball 3,
      prodState x y ∈ K)
    (hadd : ∀ ω ∈ K, ∀ η ∈ K, ω + η ∈ K)
    (hsmul : ∀ c : ℝ, 0 ≤ c → ∀ ω ∈ K, c • ω ∈ K)
    (hmax : K ⊆ maxCone (OIBridge.TransitiveBody.eball 3))
    (hH2 : ∀ ω ∈ K, cnot ω ∈ K)
    (hA : ∀ t : ℝ, ∀ ω ∈ K, actT (OIBridge.KInfFoundations.rotLin t) ω ∈ K ∧
      actT (OIBridge.KInfFoundations.cycEquiv : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) ω ∈ K) :
    K = Q3 :=
  FiniteReconstructionDesign.pairCone_eq_Q3_of_kToken hH1 hadd hsmul hmax hH2 hA

end FiniteReconstructionDesign.Mutation

/- Executable control DEPCHECK (meta-level; not a kernel proof). It reads the kernel-checked
   `ConstantInfo` of the target from the final environment and walks the constants occurring in
   types and values (`ConstantInfo.getUsedConstantsAsSet`) to a fixed point. -/
open Lean in
#eval show Lean.Meta.MetaM Unit from do
  let env ← getEnv
  let kenv := env.toKernelEnv
  -- frozen inputs
  let target : Lean.Name := `FiniteReconstructionDesign.mem_Q3_iff_pairCarrier
  let pair : Lean.Name := `OIBridge.EqvK2MaxCone.pairCone_eq_Q3_of_drive_maxCone
  let pairPresent : Bool := true
  let forbiddenModules : Array Lean.Name := #[`OIBridge.EqvK2MaxCone]
  let siblings : Array Lean.Name := #[`OIBridge.EqvK2Generation.blockInvariant_of_drive, `OIBridge.EqvK2Generation.pairCone_eq_Q3_of_drive_exact, `OIBridge.EqvK2Generation.pairCone_eq_Q3_iff_drive_exact, `OIBridge.EqvK2Block.pairCone_eq_Q3_of_block, `OIBridge.EqvK2Block.pairCone_eq_Q3_iff_block, `OIBridge.EqvK2Schema.pairCone_eq_Q3_of_drive, `OIBridge.EqvK2Schema.subset_Q3_of_pure_dual, `OIBridge.EqvK2Schema.Q3_subset_of_pure, `OIBridge.EqvK2Converse.pairCone_eq_Q3_iff_drive]
  let required : Array Lean.Name := #[`FiniteReconstructionDesign.kCone_eq_QK_of_drive_maxCone, `OIBridge.EqvK2Generation.su_euler]
  let watch : Lean.Name := `OIBridge
  -- C0: preconditions; a check over an absent name or module would be vacuous
  match kenv.find? target with
  | some (.thmInfo _) => pure ()
  | _ => throwError "DEPCHECK-VACUOUS {target} is not a theorem of the kernel environment"
  if pairPresent then
    if (kenv.find? pair).isNone then
      throwError "DEPCHECK-VACUOUS {pair} is not in the environment"
    for m in forbiddenModules do
      if (env.getModuleIdx? m).isNone then
        throwError "DEPCHECK-VACUOUS module {m} is not imported"
  else
    if env.contains pair then
      throwError "DEPCHECK-ABSENT {pair} is in the environment"
    logInfo m!"DEPCHECK-ABSENT ok: {pair} is not in the environment"
  for n in siblings ++ required do
    if (kenv.find? n).isNone then
      throwError "DEPCHECK-VACUOUS {n} is not a constant of the kernel environment"
  let modOf : Lean.Name → Lean.Name := fun c =>
    match env.getModuleIdxFor? c with
    | some i => env.allImportedModuleNames[i.toNat]!
    | none => env.mainModule
  -- C1: the transitive constant closure of the target
  let mut seen : Std.HashSet Lean.Name := ({} : Std.HashSet Lean.Name).insert target
  let mut parent : Std.HashMap Lean.Name Lean.Name := {}
  let mut queue : Array Lean.Name := #[target]
  let mut i := 0
  while i < queue.size do
    let c := queue[i]!
    i := i + 1
    let some ci := kenv.find? c <|> env.find? c
      | throwError "DEPCHECK-INCOMPLETE {c} has no ConstantInfo"
    for d in ci.getUsedConstantsAsSet do
      unless seen.contains d do
        seen := seen.insert d
        parent := parent.insert d c
        queue := queue.push d
  let par := parent
  let chainOf : Lean.Name → String := fun x => Id.run do
    let mut out : Array String := #[toString x]
    let mut cur := x
    for _ in [0:queue.size] do
      match par[cur]? with
      | some p => out := out.push (toString p); cur := p
      | none => break
    return " <- ".intercalate out.toList
  let closure := (queue.extract 1 queue.size).qsort Lean.Name.lt
  let mut failures : Array String := #[]
  -- C2: the pair theorem (tier 1)
  if seen.contains pair then
    failures := failures.push s!"DEPCHECK-PAIR {chainOf pair}"
  -- C3: constants proved from the pair theorem (tier 2): `c` with `pair` in the closure of `c`,
  -- computed by reverse reachability over the closure's own edges
  if seen.contains pair then
    let mut preds : Std.HashMap Lean.Name (Array Lean.Name) := {}
    for c in queue do
      if let some ci := kenv.find? c <|> env.find? c then
        for d in ci.getUsedConstantsAsSet do
          preds := preds.insert d ((preds.getD d #[]).push c)
    let mut reach : Std.HashSet Lean.Name := ({} : Std.HashSet Lean.Name).insert pair
    let mut stack : Array Lean.Name := #[pair]
    while !stack.isEmpty do
      let c := stack.back!
      stack := stack.pop
      for p in preds.getD c #[] do
        unless reach.contains p do
          reach := reach.insert p
          stack := stack.push p
    for c in closure do
      if c != pair && reach.contains c then
        failures := failures.push s!"DEPCHECK-PROVED-FROM {c}"
  -- C4: constants declared in a forbidden module (tier 2b)
  for c in closure do
    if forbiddenModules.contains (modOf c) then
      failures := failures.push s!"DEPCHECK-MODULE {c} ({modOf c})"
  -- C5: sibling two-token theorems and the adopted proof's core (tier 3)
  for s in siblings do
    if seen.contains s then
      failures := failures.push s!"DEPCHECK-SIBLING {chainOf s}"
  -- C6: positive control: the closure reaches the required constants
  for r in required do
    unless seen.contains r do
      failures := failures.push s!"DEPCHECK-REQUIRED {r} is not in the closure"
  let watched := closure.filter fun c => watch.isPrefixOf (modOf c)
  let listing := "\n".intercalate (watched.toList.map fun c => s!"DEPCHECK watched {c} ({modOf c})")
  logInfo m!"DEPCHECK closure of {target}: {closure.size} constants, {watched.size} from modules under {watch}\n{listing}"
  if failures.isEmpty then
    logInfo m!"DEPCHECK PASS {target}"
  else
    throwError ("DEPCHECK FAIL\n" ++ "\n".intercalate failures.toList)
