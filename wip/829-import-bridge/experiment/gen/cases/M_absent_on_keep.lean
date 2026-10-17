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
