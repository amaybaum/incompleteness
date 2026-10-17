import FiniteReachTable

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

/- Executable controls WALK and DUMP (meta-level; not kernel proofs).
   EXTRA is the set of modules in the import closure of `OIBridge.EqvK2MaxCone` and not in that
   of `OIBridge.EqvK2Generation`, read from the environment header (present mode), or the three
   OIBridge modules of that set, required to be absent (absent mode). WALK closes the
   used-constant relation of the kernel-checked `ConstantInfo` of every constant declared in the
   design modules and fails on any reached constant declared in an EXTRA module. DUMP prints,
   for every non-internal constant of the design modules, its kind and its type under `pp.all`,
   and a hash of its value; the comparison across regimes is made outside Lean. -/
open Lean in
#eval show Lean.Meta.MetaM Unit from do
  let env ← getEnv
  let kenv := env.toKernelEnv
  let present : Bool := true
  let designModules : Array Name := #[`FinitePauli, `FiniteReach, `FiniteReachTable]
  let required : Array Name := #[`OIBridge.EqvK2Generation.su_euler, `OIBridge.CompositeDimension.cnot, `Matrix.PosSemidef]
  let theorems : Array Name := #[`FiniteReconstructionDesign.tensor_mul, `FiniteReconstructionDesign.tensor_trace, `FiniteReconstructionDesign.tensor_star, `FiniteReconstructionDesign.tensor_conjugation, `FiniteReconstructionDesign.pauliWord_hermitian, `FiniteReconstructionDesign.pauliWord_orthogonal, `FiniteReconstructionDesign.pauliWord_complete, `FiniteReconstructionDesign.coordinates_dictionary, `FiniteReconstructionDesign.pauliWord_reconstruction, `FiniteReconstructionDesign.dictionary_coordinates, `FiniteReconstructionDesign.dictionary_hermitian, `FiniteReconstructionDesign.coordinates_dictionary_real, `FiniteReconstructionDesign.coordinates_real, `FiniteReconstructionDesign.dictionary_coordinates_real, `FiniteReconstructionDesign.tensorK_smul_left, `FiniteReconstructionDesign.tensorK_smul_right, `FiniteReconstructionDesign.tensorK_vecMulVec, `FiniteReconstructionDesign.quad_conj, `FiniteReconstructionDesign.quad_smul, `FiniteReconstructionDesign.conjK_vecMulVec, `FiniteReconstructionDesign.vecMulVec_ofReal_smul, `FiniteReconstructionDesign.star_mul_mul_nonneg, `FiniteReconstructionDesign.one_pair, `FiniteReconstructionDesign.tensorK_one, `FiniteReconstructionDesign.blockFam_apply, `FiniteReconstructionDesign.blockFam_mul, `FiniteReconstructionDesign.blockFam_const, `FiniteReconstructionDesign.blockFam_conjTranspose, `FiniteReconstructionDesign.blockFam_mulVec, `FiniteReconstructionDesign.liftM_mulVec, `FiniteReconstructionDesign.bitAt_succ, `FiniteReconstructionDesign.bitAt_last, `FiniteReconstructionDesign.bitAt_lift, `FiniteReconstructionDesign.fin2_cases, `FiniteReconstructionDesign.flipX_zero, `FiniteReconstructionDesign.flipX_one, `FiniteReconstructionDesign.xm_conjTranspose, `FiniteReconstructionDesign.flipX_conjTranspose, `FiniteReconstructionDesign.cnotM_succ, `FiniteReconstructionDesign.localM_succ, `FiniteReconstructionDesign.cnotM_last, `FiniteReconstructionDesign.cnotM_lift, `FiniteReconstructionDesign.localM_last, `FiniteReconstructionDesign.localM_lift, `FiniteReconstructionDesign.localM_last_block, `FiniteReconstructionDesign.localM_mul, `FiniteReconstructionDesign.localM_smul, `FiniteReconstructionDesign.localM_conjTranspose, `FiniteReconstructionDesign.cnotM_conjTranspose, `FiniteReconstructionDesign.pres_one, `FiniteReconstructionDesign.pres_mul, `FiniteReconstructionDesign.pres_scalar, `FiniteReconstructionDesign.pres_of_isWord, `FiniteReconstructionDesign.isWord_conjTranspose, `FiniteReconstructionDesign.isWord_lift, `FiniteReconstructionDesign.cisC_add, `FiniteReconstructionDesign.star_cisC, `FiniteReconstructionDesign.cisC_unit, `FiniteReconstructionDesign.exists_cisC, `FiniteReconstructionDesign.dUnit_mul, `FiniteReconstructionDesign.xm_dUnit_xm, `FiniteReconstructionDesign.rz_mul, `FiniteReconstructionDesign.bsign_zero, `FiniteReconstructionDesign.bsign_one, `FiniteReconstructionDesign.flipX_rz, `FiniteReconstructionDesign.pred_congr, `FiniteReconstructionDesign.sign_induction, `FiniteReconstructionDesign.isWord_local_dUnit, `FiniteReconstructionDesign.isWord_rzFam, `FiniteReconstructionDesign.isWord_dUnitFam, `FiniteReconstructionDesign.isWord_rotReFam, `FiniteReconstructionDesign.isWord_suFam, `FiniteReconstructionDesign.ket0_unit, `FiniteReconstructionDesign.prodVec_zero, `FiniteReconstructionDesign.prodVec_succ, `FiniteReconstructionDesign.padSeq_zero, `FiniteReconstructionDesign.padSeq_succ, `FiniteReconstructionDesign.suTo_inv_mulVec, `FiniteReconstructionDesign.reach_prod, `FiniteReconstructionDesign.normz_smul, `FiniteReconstructionDesign.normz_unit, `FiniteReconstructionDesign.prodVec_padSeq_smul, `FiniteReconstructionDesign.reach_norm, `FiniteReconstructionDesign.vecMulVec_prodVec, `FiniteReconstructionDesign.rank1_state, `FiniteReconstructionDesign.subset_psd_of_maxCone_drive, `FiniteReconstructionDesign.psd_subset_of_products_cone_drive, `FiniteReconstructionDesign.kCone_eq_psd_of_drive_maxCone, `FiniteReconstructionDesign.pres_psd, `FiniteReconstructionDesign.driveInvariant_of_eq_psd, `FiniteReconstructionDesign.kCone_eq_psd_iff_drive_maxCone, `FiniteReconstructionDesign.prodTab_succ, `FiniteReconstructionDesign.prodTab_congr, `FiniteReconstructionDesign.prodMat_succ, `FiniteReconstructionDesign.dictionary_prodTab, `FiniteReconstructionDesign.trace_dictionary_mul, `FiniteReconstructionDesign.coordinates_add, `FiniteReconstructionDesign.coordinates_smul, `FiniteReconstructionDesign.blochH_apply_zero, `FiniteReconstructionDesign.blochH_apply_one, `FiniteReconstructionDesign.blochH_apply_two, `FiniteReconstructionDesign.blochH_apply_three, `FiniteReconstructionDesign.tokMat_blochH, `FiniteReconstructionDesign.lor_blochH, `FiniteReconstructionDesign.blochH_zero_of_unit, `FiniteReconstructionDesign.hom_blochX, `FiniteReconstructionDesign.blochX_mem_eball, `FiniteReconstructionDesign.trace_rank1_mul, `FiniteReconstructionDesign.quad_dictionary_prodVec, `FiniteReconstructionDesign.psd_subset_of_pure_cone_drive, `FiniteReconstructionDesign.mem_matCone, `FiniteReconstructionDesign.tableCone_eq_psd_of_drive_maxCone, `FiniteReconstructionDesign.lorScale_pos, `FiniteReconstructionDesign.isEffectOn_lorScale, `FiniteReconstructionDesign.prodTab_lorScale, `FiniteReconstructionDesign.lorPair_nonneg_of_maxConeTab, `FiniteReconstructionDesign.tableCone_eq_psd_of_drive_maxConeTab, `FiniteReconstructionDesign.tabAct_psd, `FiniteReconstructionDesign.tableDrive_of_eq_psd, `FiniteReconstructionDesign.tableCone_eq_psd_iff_drive_maxConeTab, `FiniteReconstructionDesign.toTup_succ, `FiniteReconstructionDesign.toTup_last, `FiniteReconstructionDesign.toTup_castSucc, `FiniteReconstructionDesign.ofTup_toTup, `FiniteReconstructionDesign.toTup_ofTup, `FiniteReconstructionDesign.carrierEquiv_apply, `FiniteReconstructionDesign.bitAt_eq_toTup, `FiniteReconstructionDesign.toTup_eq_bitAt, `FiniteReconstructionDesign.toTup_mk_eq_bitAt, `FiniteReconstructionDesign.pauliWord_apply, `FiniteReconstructionDesign.prodTab_eq_prod, `FiniteReconstructionDesign.cnotK_apply, `FiniteReconstructionDesign.actK_apply, `FiniteReconstructionDesign.tupOf_tabOf, `FiniteReconstructionDesign.tabOf_tupOf, `FiniteReconstructionDesign.dictionary_apply_tabOf, `FiniteReconstructionDesign.dictionary_tabOf, `FiniteReconstructionDesign.mem_QK_iff, `FiniteReconstructionDesign.tupOf_prodTab, `FiniteReconstructionDesign.sum_prodTab_tupOf, `FiniteReconstructionDesign.cnotPerm_succ, `FiniteReconstructionDesign.bitAt_pair, `FiniteReconstructionDesign.flipX_apply, `FiniteReconstructionDesign.bitsPair_eq, `FiniteReconstructionDesign.bitsPair_ne_fst, `FiniteReconstructionDesign.bitsPair_ne_snd, `FiniteReconstructionDesign.cnotM_apply, `FiniteReconstructionDesign.conj_perm_apply, `FiniteReconstructionDesign.bitAt_cnotPerm, `FiniteReconstructionDesign.cflip_apply, `FiniteReconstructionDesign.cflip_ne, `FiniteReconstructionDesign.cflip_self, `FiniteReconstructionDesign.toTup_cnotPerm, `FiniteReconstructionDesign.cnotLabF_j, `FiniteReconstructionDesign.cnotLabF_i, `FiniteReconstructionDesign.cnotLabF_ne, `FiniteReconstructionDesign.cnotLabF_invol, `FiniteReconstructionDesign.cnotLab_apply, `FiniteReconstructionDesign.prod_two_index, `FiniteReconstructionDesign.pairUnit_apply, `FiniteReconstructionDesign.dict_apply, `FiniteReconstructionDesign.sum_pairUnit, `FiniteReconstructionDesign.dict_pairUnit_apply, `FiniteReconstructionDesign.cnot_pairUnit_apply, `FiniteReconstructionDesign.cnot_pairUnit, `FiniteReconstructionDesign.blockMat_one_Xm_apply, `FiniteReconstructionDesign.blockMat_conj_apply, `FiniteReconstructionDesign.pauli_cnot_pair, `FiniteReconstructionDesign.dictK_cflip, `FiniteReconstructionDesign.tabAct_cnotM, `FiniteReconstructionDesign.tabAct_cnotM_eq, `FiniteReconstructionDesign.tabAct_cnotK, `FiniteReconstructionDesign.slotAct_succ, `FiniteReconstructionDesign.slotAct_last, `FiniteReconstructionDesign.slotAct_lift, `FiniteReconstructionDesign.dictionary_succ_tok, `FiniteReconstructionDesign.dictionary_succ_pref, `FiniteReconstructionDesign.localM_conj_dictionary, `FiniteReconstructionDesign.slotAct_toTup, `FiniteReconstructionDesign.tabAct_localM, `FiniteReconstructionDesign.tabAct_localM_eq, `FiniteReconstructionDesign.tabAct_localK, `FiniteReconstructionDesign.tabAct_rotK, `FiniteReconstructionDesign.tabAct_cycK, `FiniteReconstructionDesign.mem_matCone_dictionary, `FiniteReconstructionDesign.pres_matCone, `FiniteReconstructionDesign.maxTest_matCone, `FiniteReconstructionDesign.pure_matCone, `FiniteReconstructionDesign.add_matCone, `FiniteReconstructionDesign.smul_matCone, `FiniteReconstructionDesign.tableCone_subset_psd_of_maxCone_drive, `FiniteReconstructionDesign.psd_subset_tableCone_of_products_cone_drive, `FiniteReconstructionDesign.tabOf_mem_tabSet, `FiniteReconstructionDesign.tabSet_products, `FiniteReconstructionDesign.tabSet_add, `FiniteReconstructionDesign.tabSet_smul, `FiniteReconstructionDesign.tabSet_maxCone, `FiniteReconstructionDesign.tabSet_cnot, `FiniteReconstructionDesign.tabSet_local, `FiniteReconstructionDesign.subset_QK_of_maxCone_drive, `FiniteReconstructionDesign.QK_subset_of_products_cone_drive, `FiniteReconstructionDesign.kCone_eq_QK_of_drive_maxCone, `FiniteReconstructionDesign.driveInvariantK_of_eq_QK, `FiniteReconstructionDesign.kCone_eq_QK_iff_drive_maxCone, `FiniteReconstructionDesign.pairCarrierEquiv_apply, `FiniteReconstructionDesign.pairCarrierEquiv_prodState, `FiniteReconstructionDesign.sum_pairCarrier_eq, `FiniteReconstructionDesign.pairCarrierEquiv_maxCone, `FiniteReconstructionDesign.maxCone_of_pairCarrierEquiv, `FiniteReconstructionDesign.dictK_pairCarrier, `FiniteReconstructionDesign.mem_Q3_iff_pairCarrier, `FiniteReconstructionDesign.pairCarrierEquiv_cnot, `FiniteReconstructionDesign.pairCarrierEquiv_actT, `FiniteReconstructionDesign.fin2_lt, `FiniteReconstructionDesign.fin2_ne_zero, `FiniteReconstructionDesign.pairCone_eq_Q3_of_kToken, `FiniteReconstructionDesign.blochH_real, `FiniteReconstructionDesign.blochH_down, `FiniteReconstructionDesign.lor_blochH_decomp, `FiniteReconstructionDesign.sum_prodTab_succ, `FiniteReconstructionDesign.tokSlice_add, `FiniteReconstructionDesign.tokSlice_smul, `FiniteReconstructionDesign.lorTests_of_blochTests, `FiniteReconstructionDesign.maxConeTab_of_blochTests, `FiniteReconstructionDesign.maxConeTab_of_prodVec_nonneg, `FiniteReconstructionDesign.prodVec_nonneg_of_maxConeTab, `FiniteReconstructionDesign.maxConeTab_iff_prodVec_nonneg]
  let staticExtra : Array Name :=
    #[`OIBridge.EqvK2MaxCone, `OIBridge.EffectSpace, `OIBridge.CompositeInterface]
  -- import closures from the header
  let mut closures : Std.HashMap Name (Std.HashSet Name) := {}
  for root in #[`OIBridge.EqvK2MaxCone, `OIBridge.EqvK2Generation] do
    if (env.getModuleIdx? root).isNone then
      if present || root == `OIBridge.EqvK2Generation then
        throwError "WALK-VACUOUS module {root} is not imported"
      continue
    let mut seen : Std.HashSet Name := ({} : Std.HashSet Name).insert root
    let mut stack : Array Name := #[root]
    while !stack.isEmpty do
      let x := stack.back!
      stack := stack.pop
      let some i := env.getModuleIdx? x
        | throwError "WALK-INCOMPLETE module {x} has no index"
      let some md := env.header.moduleData[i.toNat]?
        | throwError "BRIDGE-INCOMPLETE module {x} has no module data"
      for imp in md.imports do
        unless seen.contains imp.module do
          seen := seen.insert imp.module
          stack := stack.push imp.module
    closures := closures.insert root seen
  let mut extra : Array Name := staticExtra
  if present then
    let a := closures.getD `OIBridge.EqvK2MaxCone {}
    let g := closures.getD `OIBridge.EqvK2Generation {}
    extra := (a.toArray.filter fun m => !g.contains m).qsort Name.lt
    for m in staticExtra do
      unless extra.contains m do
        throwError "WALK-VACUOUS {m} is not in EXTRA"
  else
    for m in staticExtra do
      if (env.getModuleIdx? m).isSome then
        throwError "WALK-ABSENT module {m} is imported"
  logInfo m!"WALK EXTRA-MODULES ({extra.size}): {extra.toList}"
  -- the roots: every constant declared in a design module
  let mut roots : Array Name := #[]
  for m in designModules do
    let some i := env.getModuleIdx? m
      | throwError "WALK-VACUOUS design module {m} is not imported"
    let some md := env.header.moduleData[i.toNat]?
      | throwError "WALK-INCOMPLETE design module {m} has no module data"
    roots := roots ++ md.constNames
  for r in (#[] : Array Name) do
    if (kenv.find? r).isNone then
      throwError "WALK-VACUOUS root {r} is not a constant of the kernel environment"
    roots := roots.push r
  for t in theorems do
    match kenv.find? t with
    | some (.thmInfo _) => pure ()
    | _ => throwError "DUMP-VACUOUS {t} is not a theorem of the kernel environment"
  let modOf : Name → Name := fun c =>
    match env.getModuleIdxFor? c with
    | some i => env.allImportedModuleNames[i.toNat]!
    | none => env.mainModule
  -- WALK
  let mut seen : Std.HashSet Name := {}
  let mut parent : Std.HashMap Name Name := {}
  let mut queue : Array Name := #[]
  for r in roots do
    unless seen.contains r do
      seen := seen.insert r
      queue := queue.push r
  let mut k := 0
  while k < queue.size do
    let c := queue[k]!
    k := k + 1
    let some ci := kenv.find? c <|> env.find? c
      | throwError "WALK-INCOMPLETE {c} has no ConstantInfo"
    for d in ci.getUsedConstantsAsSet do
      unless seen.contains d do
        seen := seen.insert d
        parent := parent.insert d c
        queue := queue.push d
  let mut failures : Array String := #[]
  for r in required do
    unless seen.contains r do
      failures := failures.push s!"WALK-REQUIRED {r} is not reached"
  let hits := (queue.filter fun c => extra.contains (modOf c)).qsort Name.lt
  for h in hits do
    let mut chain : Array String := #[toString h]
    let mut cur := h
    for _ in [0:queue.size] do
      match parent[cur]? with
      | some p => chain := chain.push (toString p); cur := p
      | none => break
    failures := failures.push s!"WALK-EXTRA {h} ({modOf h}): {" <- ".intercalate chain.toList}"
  if failures.isEmpty then
    logInfo m!"WALK PASS: {roots.size} design constants, {queue.size} constants reached, none declared in EXTRA"
  else
    throwError ("WALK FAIL\n" ++ "\n".intercalate failures.toList)
  -- DUMP
  let mut out : Array String := #[]
  for n in roots.qsort Name.lt do
    if n.isInternal then continue
    let some ci := kenv.find? n
      | throwError "DUMP-INCOMPLETE {n} has no ConstantInfo"
    let kind := match ci with
      | .thmInfo _ => "theorem" | .defnInfo _ => "def" | .inductInfo _ => "inductive"
      | .ctorInfo _ => "ctor" | .recInfo _ => "rec" | .opaqueInfo _ => "opaque"
      | .axiomInfo _ => "axiom" | .quotInfo _ => "quot"
    let ty ← withOptions (fun o => o.setBool `pp.all true) (Lean.Meta.ppExpr ci.type)
    let vh := match ci.value? (allowOpaque := true) with
      | some v => toString v.hash
      | none => "-"
    out := out.push s!"STMT {modOf n} {n} {kind} {ci.levelParams} : {ty.pretty 1000000}"
    out := out.push s!"VALUEHASH {n} {vh}"
  logInfo ("DUMP-BEGIN\n" ++ "\n".intercalate out.toList ++ "\nDUMP-END")

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
