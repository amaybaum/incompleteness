import FiniteReachTable
import OIBridge.EqvK2MaxCone

/- Executable controls ABSENT and SPELL (meta-level; not kernel proofs), run in an environment that
   imports the design module and `OIBridge.EqvK2MaxCone`. ABSENT: the design module's import
   closure, read from the header, meets no EXTRA module (EXTRA as in WALK). SPELL: the name the
   design's `#eval` tests is a constant of this environment, so that `#eval` is not vacuous. -/
open Lean in
#eval show Lean.Meta.MetaM Unit from do
  let env ← getEnv
  let design : Name := `FiniteReachTable
  let closure : Name → MetaM (Std.HashSet Name) := fun root => do
    if (env.getModuleIdx? root).isNone then
      throwError "ABSENT-VACUOUS module {root} is not imported"
    let mut seen : Std.HashSet Name := ({} : Std.HashSet Name).insert root
    let mut stack : Array Name := #[root]
    while !stack.isEmpty do
      let x := stack.back!
      stack := stack.pop
      let some i := env.getModuleIdx? x
        | throwError "ABSENT-INCOMPLETE module {x} has no index"
      let some md := env.header.moduleData[i.toNat]?
        | throwError "BRIDGE-INCOMPLETE module {x} has no module data"
      for imp in md.imports do
        unless seen.contains imp.module do
          seen := seen.insert imp.module
          stack := stack.push imp.module
    return seen
  let a ← closure `OIBridge.EqvK2MaxCone
  let g ← closure `OIBridge.EqvK2Generation
  let extra := (a.toArray.filter fun m => !g.contains m).qsort Name.lt
  for m in #[`OIBridge.EqvK2MaxCone, `OIBridge.EffectSpace, `OIBridge.CompositeInterface] do
    unless extra.contains m do
      throwError "ABSENT-VACUOUS {m} is not in EXTRA"
  let d ← closure design
  let met := extra.filter fun m => d.contains m
  unless met.isEmpty do
    throwError "ABSENT FAIL {design} imports {met.toList}"
  logInfo m!"ABSENT ok: {design} imports none of the {extra.size} EXTRA modules {extra.toList}"
  unless env.contains `OIBridge.EqvK2MaxCone.pairCone_eq_Q3_of_drive_maxCone do
    throwError "SPELL FAIL the name tested by the design's #eval is not a constant"
  logInfo "SPELL ok"

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

example : type_of% @FiniteReconstructionDesign.pairCone_eq_Q3_of_kToken =
    type_of% @OIBridge.EqvK2MaxCone.pairCone_eq_Q3_of_drive_maxCone := rfl

open Lean in
#eval show Lean.Meta.MetaM Unit from do
  let r ← getConstInfo `FiniteReconstructionDesign.pairCone_eq_Q3_of_kToken
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

/- Executable control DEPCHECK (meta-level; not a kernel proof). It reads the kernel-checked
   `ConstantInfo` of the target from the final environment and walks the constants occurring in
   types and values (`ConstantInfo.getUsedConstantsAsSet`) to a fixed point. -/
open Lean in
#eval show Lean.Meta.MetaM Unit from do
  let env ← getEnv
  let kenv := env.toKernelEnv
  -- frozen inputs
  let target : Lean.Name := `FiniteReconstructionDesign.pairCone_eq_Q3_of_kToken
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
