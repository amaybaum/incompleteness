## Summary

A research-carrier form of #829's conditional k-token theorem compiles for every k, in matrix form and in Pauli-table form, with nothing beyond the standard axioms: the carriers are the recursive `Bits k`/`Labels k`, and the table actions are defined by dictionary conjugation. #829's own statement surface (`WK k`, `cnotK`/`actK`, its frozen names, Q-PAIR) is not yet reached. An independent exact check agrees with #829's `cnotK`/`actK` on basis tables at k = 1..4 (finite evidence, not a proof for all k). The final source head `11fbcd59` passed in run 38866415970, job 116860178759, all green.
- Two new modules: `FiniteReach.lean` (77 theorems) and `FiniteReachTable.lean` (29 theorems).
- All 38 axiom reports in the package read exactly `[propext, Classical.choice, Quot.sound]`.
- The log has no `sorryAx`, no "declaration uses 'sorry'" and no errors. There is no sorry, admit, axiom or native_decide anywhere.
- The docs head `29857749` passed too (run 38866922142, job 116861771680).

I could not write report.md. The harness refused writing a report file from a subagent, and I did not work around that. The full report is below; the file it was meant for is /tmp/claude-0/-home-user-incompleteness/ce7104bc-8508-557b-9490-8c1ce0f7a1ca/scratchpad/research/trackA/report.md, which does not exist.

**Status of the four #829 items:**
- **Gray schedule (item 1):** not formalized and not needed. The multiplexor is proved another way, which handles zero controls directly.
- **Items 2–4:** done in the form the theorem uses (qubit spectators only). That covers the gates with qubit spectators, the Euler multiplexors in factor order, recursive preparation, and both inclusions, each direction with its own witness.

**Gaps I found:**
- The carrier's equality instance in `FinitePauli` is classical and does not match the instances Lean builds at explicit carrier sizes. That broke push 1; a structural instance fixes it.
- `argument.md` left two steps unstated: unit scalars have to be in the words, and the y-rotation multiplexor is the cyclic conjugate of the z one. Both are now written in.
- Only one direction of the "equivalently" in §1 item 3 is compiled.
- The table actions are defined by dictionary conjugation. They are not yet shown equal to #829's coordinate formulas.

**What remains, in order:**
1. Show the table actions match #829's coordinate formulas.
2. Reindex the recursive carriers to `Fin k`-indexed ones.
3. The five k = 2 transports and recovery of the existing two-token theorem.
4. Optionally, the Gray identities.
5. Sourcing the premises, which is outside the mathematics.

**Non-claims:** this is a conditional theorem, not a physical derivation. It is research design only: not adopted, not a native round, and no F is designated.

## Full report

### Where things are
- **Branch:** `research/finite-reconstruction-design-20261013`, pushed fast-forward only from local `trackA-local`.
- **Package:** `verification/programmes/oi-qm/reconstruction/finite-reconstruction-design/`.
- **Base:** D `dee3b5ae6fd3fb20fa1bad3337963e5af947f3a4`. `verification/lean-mathlib` on the branch is identical to D.

### (a) Items and status

**The certifying run** is head `11fbcd597accf7fbe2eed9ef9c81107cd100f2f2`, run 38866415970, job 116860178759. Every step passed:
- hash check and exact replays;
- compilation of the five design modules and KN-DESC;
- legacy check (303 records), receipts (46 hold), artifact placement.

**The new modules:**
- `FiniteReach.lean`: 77 theorems, 13 axiom reports.
- `FiniteReachTable.lean`: 29 theorems, 11 axiom reports.

**The four #829 items:**
1. **Gray schedule and prefix-parity/Walsh correspondence.** Not formalized and not needed. The multiplexor comes from sign-character induction (`sign_induction`, `isWord_rzFam`), with zero controls as the constant case. The Gray identities would only show that the compiled word equals the Gray-ordered word.
2. **Gate instantiation and spectator transport.** Done for qubit spectators at every token count.
   - Gates are built recursively: `cnotM`, `localM`, `blockFam`, `liftM`.
   - Supporting results: `isWord_lift`, `isWord_conjTranspose`, `pres_of_isWord`.
   - Arbitrary finite spectator carriers are not treated; the cone theorem does not need them.
3. **Spectator SU(2) Euler construction and multiplexor ordering.** Done.
   - The adopted `su_euler` is applied branch by branch.
   - The real-rotation multiplexor is obtained as the cyclic conjugate of the diagonal one (`isWord_rotReFam`).
   - The three multiplexors are composed in Euler-factor order (`isWord_local_dUnit`, `isWord_dUnitFam`, `isWord_suFam`).
4. **Recursive preparation and both inclusions.** Done.
   - Preparation: `reach_prod`, `reach_norm`. Zero blocks use `suTo 0 = 1`, the first token is never driven, and k = 0 uses a unit-scalar word.
   - Upper inclusion: `subset_psd_of_maxCone_drive`.
   - Lower inclusion: `psd_subset_of_products_cone_drive`.
   - Combined: `kCone_eq_psd_of_drive_maxCone`.

**The equivalence, matrix form.** Each direction has its own witness:
- equality gives preservation: `driveInvariant_of_eq_psd`;
- preservation gives equality: `kCone_eq_psd_of_drive_maxCone`;
- the statement itself: `kCone_eq_psd_iff_drive_maxCone`.

**The table form**, on the recursive `Labels k` carrier:
- Supporting results: `dictionary_prodTab`, `trace_dictionary_mul`, `tokMat_blochH`, `lor_blochH`, `quad_dictionary_prodVec`.
- Lower inclusion from pure products only: `psd_subset_of_pure_cone_drive`.
- Theorem with forward-cone product tests: `tableCone_eq_psd_of_drive_maxCone`.
- Effect-form tests imply forward-cone tests: `lorPair_nonneg_of_maxConeTab`.
- Theorem with effect-form tests: `tableCone_eq_psd_of_drive_maxConeTab`.
- Equivalence: `tableDrive_of_eq_psd` (one direction) and `tableCone_eq_psd_iff_drive_maxConeTab`.

**Exact axiom lines.** Each line is printed verbatim as `'FiniteReconstructionDesign.<name>' depends on axioms: [propext, Classical.choice, Quot.sound]`, for these names:
- **FiniteReach:** blockFam_mul, isWord_conjTranspose, isWord_lift, sign_induction, isWord_rzFam, isWord_suFam, reach_prod, reach_norm, subset_psd_of_maxCone_drive, psd_subset_of_products_cone_drive, kCone_eq_psd_of_drive_maxCone, driveInvariant_of_eq_psd, kCone_eq_psd_iff_drive_maxCone.
- **FiniteReachTable:** dictionary_prodTab, trace_dictionary_mul, tokMat_blochH, lor_blochH, quad_dictionary_prodVec, psd_subset_of_pure_cone_drive, tableCone_eq_psd_of_drive_maxCone, lorPair_nonneg_of_maxConeTab, tableCone_eq_psd_of_drive_maxConeTab, tableDrive_of_eq_psd, tableCone_eq_psd_iff_drive_maxConeTab.
- **Earlier modules:** FinitePauli (8), FiniteWalsh (3) and FiniteCircuit (3) print the same line.

**Earlier green runs** on the subsets of these statements present then:
- 45c05e31: run 38863665456, job 116851471776.
- 03cd311d: run 38864882901, job 116855304721.
- 0edc62db: run 38865689246, job 116857872390.

The final source head 11fbcd59 changes only comments and docstrings.

**Workflow change, on this research branch only.** In `.github/workflows/finite-reconstruction-design.yml` I made the minimal change needed to compile the new files:
- it now builds `OIBridge.EqvK2Generation`;
- it copies `FiniteReach.lean` and `FiniteReachTable.lean`;
- it compiles both.

**Documentation:**
- `formalization.md` is updated in its existing register: module names, run, job, hashes, counts, axiom reports, the equality instance, and what remains.
- `argument.md` is corrected in place in the header, §2, §3 and the §7 status.
- `SHA256SUMS` is updated, and `sha256sum -c` passes.

### (b) Pushed commits (6 of the 8 allowed)
1. `7a96c4d49effdbb66095ff13e129fd82cd41b55a` — run 38862753654, failed with 6 errors: five equality-instance mismatches and one `simp` that did not fire.
2. `45c05e3161147fd6bda8641e406dc81ffce13c65` — green.
3. `03cd311d162f09ef0a9a174a7d176c1d79be6bf1` — green.
4. `0edc62db96a8c9eb25bca728d8548bdd30eb6c1c` — green.
5. `11fbcd597accf7fbe2eed9ef9c81107cd100f2f2` — green; the certifying run.
6. `298577494feff446c4d1424a2fd2d6e52a728c2c` — docs only; run 38866922142, job 116861771680, green.

### (c) Defects and gaps
1. **Equality instance.** `FinitePauli` declares `carrierDecidableEq := Classical.decEq`. The instances Lean builds at `Bits (n+1)` and `Bits 0` are the `Prod` and `Fin 1` instances, which are not definitionally equal to the classical one. As a result, identity matrices written at explicit carrier sizes fail to unify. The structural high-priority `bitsDecEq` fixes this. Adoption should make the carrier instance structural at the source.
2. **Unit scalars.** `argument.md` §2/§3 left them implicit. `phaseMat` = diag(1, e^{it}) is not special unitary, so a word needs a unit scalar to reach diagonal SU(2). Scalar conjugation is trivial, so this adds no premise. The fix is now written into §2.
3. **Real-rotation multiplexor.** §3 treated the y-rotation family as directly available. The inventory only has the diagonal flow, and the real family is its cyclic conjugate. This is now written into §3.
4. **"Equivalently" in §1 item 3.** Only the direction from effect tests to forward-cone tests is compiled. The converse is not needed for the theorem but rests on prose (§A.34).
5. **Table actions.** `tabAct` is defined by dictionary conjugation. It is not shown equal to #829's explicit coordinate formulas: the CNOT sign/label map and the homogeneous action on the target slot.
6. **Premise sharpening, seen but not compiled.** The upper proof uses the product bound only on unit vectors of the form (arbitrary first token) ⊗ |0…0⟩. The lower proof uses only pure products, and that part is compiled as `psd_subset_of_pure_cone_drive`.

### (d) What remains, in order
1. Show `tabAct` matches #829's coordinate actions.
2. Reindex `Bits k`/`Labels k` to `Fin k → Fin 2`/`Fin 4`.
3. The five k = 2 transports and recovery of `pairCone_eq_Q3_of_drive_maxCone` without using it.
4. Optionally, the Gray schedule and the prefix-parity/Walsh identification.
5. Sourcing of the premises, which is outside the mathematics.

### (e) Non-claims
- **Conditional only.** This is not a physical derivation, and no premise is sourced.
- **Research only.** The modules sit outside `OIBridge` and are not adopted. This is not a native round and not an F or E attestation, and no F is designated.
- **Scope.** No arbitrary-unitary universality is claimed, only pure-state reachability.
- **Untouched:** KN-DESC membership, K2/Kn, manuscripts, the registry, receipts, `main`, `verify.yml`, `OIBridge/**`, PRs and issues. No workflow was dispatched by hand.