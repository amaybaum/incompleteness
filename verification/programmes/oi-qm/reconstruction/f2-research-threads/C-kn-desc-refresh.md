# Thread C — KN-DESC-1 refresh against M (bounded design step)

M = `5bfdaba61b535e2fff83d8ba68e73a1b9dbc5dc5` (main after #844). #823 = `origin/draft/kn-desc-1`, head
`8c3a262a`, three single-parent commits on `dee3b5ae`, one file (the preregistration). Nothing in this
step was pushed except the disposable design-run commit to `ccr-ac945020-v97mrh`.

## 1. Bases

- The design's base: `research/finite-reconstruction-design-20261013` forks from `dee3b5ae`
  (first commit `05d96d71`, parent `dee3b5ae`). So the design base and #823's D are the same commit.
- The compiled design commit is `d3a95be6` (run 38457070337, job 115502431432). The remote head of the
  research branch is `8b431a18`. That commit is docs-only: it changes `result.md`, `argument.md`,
  `formalization.md` and two `SHA256SUMS`. All four `.lean` blobs are identical at `d3a95be6` and
  `8b431a18`. The preregistration and the design rerun cite `d3a95be6` only.
- From `dee3b5ae` to M there are 19 commits (#842, #843, #844). From L (`9f9f8257`) to M there are
  64 commits; L to `dee3b5ae` was 45.

## 2. Dependency-change table (blob or tree ids, 10 hex)

Columns: design base = D(old) `dee3b5ae` | compiled design `d3a95be6` | M `5bfdaba6`.

| path | dee3b5ae | d3a95be6 | M | changed D(old)→M |
|---|---|---|---|---|
| `verification/lean-mathlib/` (tree) | 0289118d4b | 0289118d4b | 0289118d4b | no |
| `OIBridge.lean` | 9c84d95ed3 | same | same | no |
| `OIBridge/SubstratumSource.lean` | 4d053fe6c2 | same | same | no |
| `OIBridge/LiftAudit.lean` | deca05869f | same | same | no |
| `OIBridge/ImplementationLocality.lean` | d96b65bd26 | same | same | no |
| `OIBridge/StructuralClosure.lean` | d6999cd1bd | same | same | no |
| `OIBridge/EqvK2Schema.lean` (import of FinitePauli) | c634beb821 | same | same | no |
| transitive OIBridge import closure of SubstratumSource + LiftAudit + EqvK2Schema (90 modules) | — | — | — | no (`git diff --stat` empty) |
| `lean-toolchain` / `lakefile.toml` (no tracked lake-manifest) | 025e59548e / 5935a5aed3 | same | same | no |
| `.github/workflows/verify.yml` (governed M) | 159936eb42 | same | same | no |
| `verification/lean-manuscript-census.json` (governed M) | a10321b022 | same | c8e0e1844c | YES: only the GR 3.3 family's status (`current` → `scope-consistent`) and note; 106 families at both; none names `KnDescent` |
| `verification/ROADMAP.md` (quoted) | 85232c2c77 | same | 4cbb6a6fa2 | YES: P2 table row (line 71, 1:1) and the P2 section (~:1116); K block :1070–1081 byte-identical |
| `verification/audits/foundations/kn-elementary-carrier-census.md` | 09b81afb2f | same | same | no |
| KT4-PREM-1 record dir (stage/shard pattern adopted by reference) | 6b87c2579c | same | same | no |
| KINF-COPY-1 (controls P,W,V,I,C,R,G adopted by reference) | absent | absent | absent | not on main at either D: draft #822, head `90c72640`, from `dee3b5ae` |
| `verification/infrastructure/legacy-records.json` | 9e48bd3179 | same | same | no (303 records) |
| `verification/receipts/` (tree) | 68452132c9 | same | same | no (46 receipts) |
| `verification/MIGRATION-MANIFEST.md` | 203904c333 | same | same | no |
| `tools/` (tree) | 944b0d2bd4 | same | 31ae7e9421 | YES, only `tools/unicode-fix.tex`; `release_gate.py`, `lean_manuscript_census.py`, `v3_verifier.py`, `v3_receipt.py`, `legacy_records_check.py`, `artifact_placement_check.py`, `lean_axiom_check.py` unchanged |
| `verification/lean/` (tree) | 20749c7af8 | same | a822053d99 | YES: only `bohr_frequency_probe.py` (e8fd41868f→baa135ed52), `edge_rigidity_probe.py` (ef622b48d6→36dfadab69), `gap_correspondence_probe.py` (7a951f2238→a46ff78dbe). None is a KN-DESC-1 dependency. `kn_desc1_probe.py` is absent at M |
| `verification/coverage/LEDGER.json` | 25329275c5 | same | c6b94bf822 | YES. Not referenced by the preregistration |
| `verification/programmes/oi-qm/PROGRAMME.md` | 56b399443d | same | aa5928513b | YES, only the BG/reconstruction-track paragraph (~:597). Arc F / F1 text (:505–527) unchanged. Now cited for F1 |
| governed execution paths `OIBridge/KnDescent.lean`, `verification/lean/kn_desc1_probe.py`, `verification/receipts/KN-DESC-1.json`, the record directory | absent | absent | absent | still free |

Bottom line: no adopted Lean, tool, workflow or record that the design or the preregistration
depends on changed. The changed files (census, ROADMAP, PROGRAMME, LEDGER, three probes) change
outside every span that is quoted or relied on.

## 3. Re-measured references (all at M)

- D line: `5bfdaba61b535e2fff83d8ba68e73a1b9dbc5dc5`, "`main` after #844". Objects bullet: `5bfdaba6`.
- Drift L→D: 64 commits (was 45). The same eight added modules and two import lines. No cited
  landed module changed.
- Kernel line refs, all still valid:
  - SubstratumSource.lean:77 `DrivesElementary`, :86 `QuantumArchitecture`
  - ImplementationLocality.lean:506 `Architecture`, :359 `ContextStable`, :364 `LabelInvariant`
  - StructuralClosure.lean:383 `substratum_residual`
- New refs added for the hypothesis table, measured at M:
  - ImplementationLocality.lean:244 `ImplementationClass`, :514 `Architecture.block`, :374 `fullClass`
  - AncillaClosure.lean:457 `ancBlock`
  - MicroscopicReversibility.lean:216 `DaggerStable`
  - SubstratumSource.lean:136 `genTheory_qm_of_quantumArchitecture`
  - LieRankSource.lean:199 `transition`, :209 `phaseGate`
  - CoherentLift.lean:92 `permMatrix`
  - ReachabilitySeam.lean:95 `flow`
  - LiftAudit.lean:219 `exp_smul_idempotent`, :276 `flow_transition_closedForm`
- ROADMAP K block: :1070–1081, text byte-identical to L and to `dee3b5ae`. The quoted ending and
  "No current theorem supplies the lift." (:1075) still hold.
- Last import line of `OIBridge.lean`: `import OIBridge.EqvK2MaxCone` (unchanged), so the census
  import-line placement holds.
- S2 resolution list: all 15 names resolve at M (same lean-mathlib tree).
- Counts:
  - receipts: 46 at M; the historical run-1 row's 43 is at L and stays as recorded
  - legacy records: 303
  - census registry: blob `c8e0e184`, 106 families
- KINF-COPY-1 is not on M; its draft is #822. This is now stated as a measured fact.
- Design provenance as the coordinator specified: `KnDescentDesign.lean`, namespace
  `OIBridge.KnDescentDesign`, workflow `.github/workflows/finite-reconstruction-design.yml`
  ("finite reconstruction research design"), run 38457070337 / job 115502431432, exact source
  commit `d3a95be6`, all 12 standard axiom reports. The doc commit `8b431a18` is not cited.
- Not re-measured, because it is not D-scoped: "HP-1" (the ROADMAP-wording heading). The identifier
  does not resolve anywhere on main, at either D; it occurs only in draft PR preregistrations. It is
  left as is; owner may want it resolved before F.

## 4. The revising commit (unpushed)

- Worktree: `/tmp/claude-0/-home-user-incompleteness/ce7104bc-8508-557b-9490-8c1ce0f7a1ca/scratchpad/threads/wt-C` (detached).
- Chain on M, each commit single-parent and touching only the preregistration:

  | commit | parent | content |
  |---|---|---|
  | `48c9da9a` | M | cherry-pick of c83954a5 |
  | `5693977e` | `48c9da9a` | cherry-pick of d5fa542b |
  | `9bdce752` | `5693977e` | cherry-pick of 8c3a262a; blob `387fce3a` identical to #823 head |
  | **`487bb3ace2c6633b0cc67281db70ee09367bc12a`** | `9bdce752` | the revising commit |

- Preregistration at head: blob `770ba3f2`, sha256 `40cba2c3846a6375d55dda35caf90c7473fa5c27a605bd622462a48a4d0e7efc`.
- Diff: +66 / −9 in one file:
  1. **D paragraph and objects bullet** re-cut to M, with the drift re-measured as above. Adds the
     facts that bridge `dee3b5ae` and D: the lean-mathlib tree and the other unchanged surfaces,
     where the census and ROADMAP changed, and KINF-COPY-1's draft status.
  2. **New frozen section "What a positive outcome strengthens".** A positive outcome strengthens the
     conditional K3 assembly (`genTheory_qm_of_quantumArchitecture`). It does this by restating
     QuantumArchitecture's drivability clause at the carriers `Fin (2^k)` (`quantumArchitecture_iff_pow`),
     with every other clause unchanged. Certifying the round alone does not close Kₙ and does not
     establish F1 (PROGRAMME.md Arc F, full conditional equivalence). No cell or combination of cells
     is read as either.
  3. **Hypothesis table: "The matrix framework the design assumes: carrier-general architecture and
     spectator closure".** It covers every hypothesis of the 12 theorems, each with its kernel or design
     object and the theorems that take it:
     - carrier-general matrix framework (`ImplementationClass`)
     - carrier-general architecture (`Architecture`; only `block`/`ancBlock` used)
     - spectator closure (`ContextStable`, instantiated with `R := S`, so the descent uses an odd spectator)
     - relabelling (`LabelInvariant` + Mathlib `Equiv.Perm.exists_extending_pair`)
     - `DaggerStable` (iff only)
     - `DrivesElementary`, `DrivesElementaryAt`, `hpow`
     - `ι : S ↪ T`, `[Nonempty S]` (empty carrier handled by vacuity), `𝓘 T K`

     A closing paragraph names the seven theorems that take no hypothesis on 𝓘 and the landed
     definitions and lemmas they use. It ends: "No hypothesis in the table is sourced by the round."
  4. **Controls.** S4 phrases gain "Kₙ is closed", "F1 is established" and "establishes F1". The §A.41
     invariant table gains "the result note reads no outcome as closing Kₙ or establishing F1 → C5: S4".
     This gives the newly stated invariant a checkpoint. It is a control addition, not a decision-rule
     change.
  5. **Design evidence.** The rebuild paragraph is retitled "Research rebuild at `dee3b5ae`". It names
     the exact source commit `d3a95be6`, its branch, and the workflow file and name. It states that
     `lean-mathlib` is tree `0289118d` at `dee3b5ae`, `d3a95be6` and D. A new "Re-measurement at `D`"
     paragraph reports the disposable run (§5) as a separate re-measurement, not a provenance
     replacement and not a `check-run` attestation.
- **Decision rules:** unchanged (the decision-rule table, the earned reading, the non-inference rule,
  the stages and outcomes). No measured fact forced a change.

## 5. Design rebuild at M

- **Trigger filter.** `finite-reconstruction-design.yml` runs on `push` to
  `research/finite-reconstruction-design-20261013` only, plus `workflow_dispatch`. The file is not on
  the default branch, so dispatch is unavailable, and a push to `ccr-ac945020-v97mrh` would not have
  triggered it.
- **Disposable commit.** `22e0d002c2f1439adca8ca5c99cccc9a0debfaa1`, single parent M.
  - Tree: M plus `d3a95be6`'s `finite-reconstruction-design/`, `carrier-descent-design/` and workflow,
    byte for byte. The one exception is the workflow's push `branches` list, which gained
    `ccr-ac945020-v97mrh`; the workflow is not otherwise modified.
  - Both `SHA256SUMS` verify.
  - No Lean changed. `KnDescentDesign.lean` blob `85b23738` = sha256 `fa9c3b08…`.
- **Push.** The first push, with `--force-with-lease=…:1658ec84`, was rejected as "stale info": the
  remote branch no longer existed (deleted after #844 merged; GitHub API 404). It was then created with
  a must-not-exist lease (`--force-with-lease=ccr-ac945020-v97mrh:`). No other branch was touched. Only
  this workflow triggered: verify.yml runs only on push to main and on PRs, and BG2's path filter did
  not match.
- **Run.** [38597304093](https://github.com/amaybaum/incompleteness/actions/runs/38597304093),
  job 115967222595: **success**, every step green, 16:20:54–16:23:47Z.
  - Exact replays step green: `exact_check.py --self-test`, `source_e3_compress.py` and
    `independent_check.py`, each byte-identical to its saved output with empty stderr.
  - `lake build OIBridge.EqvK2Schema OIBridge.SubstratumSource OIBridge.LiftAudit`:
    `Build completed successfully (3172 jobs)`.
  - Axiom reports, all `[propext, Classical.choice, Quot.sound]`:
    - KnDescentDesign 12/12 (`drivesElementaryAt_of_drives`, `compress_mem`, `transition_submatrix`,
      `flow_transition_self`, `flow_transition_submatrix`, `permMatrix_swap_submatrix`,
      `phaseGate_submatrix`, `drivesElementaryAt_of_embedding`, `le_two_pow`, `drivesElementary_of_pow`,
      `quantumArchitecture_iff_pow`, `drivesElementaryAt_fullClass`)
    - FinitePauli 8, FiniteWalsh 3, FiniteCircuit 3
  - Warnings are the same four in KnDescentDesign as in run 38457070337 (unused section binders at
    :102, :134, :141 and the `haveI` hint at :181), plus unused-simp-arg linter warnings in the
    finite-reconstruction files and LiftAudit. No errors.
  - LEGACY 303 intact in 75 namespaces; RECEIPTS 46 hold; artifact placement OK (95 names).
- **Local pre-push replay** (Python 3.13 venv, SymPy 1.14.0): the same three replays matched; legacy 303,
  receipts 46, placement OK.

## 6. Local checks on wt-C head `487bb3ac`

- `tools/artifact_placement_check.py`: OK (no unaccounted root artifact; 95 names; self-test passed).
- `tools/legacy_records_check.py 487bb3ac…`: self-test OK; 303 records in 75 closed namespaces intact.
- `tools/v3_verifier.py --receipts 487bb3ac…`: 46 receipts, all hold. `--self-test`: OK.
- T1 dry-run (script driving the verifier's own `control_plane()` with D = M and candidate F = head):
  - result: codes **none**
  - four commits, each one parent, each touching only `…/round-kn-desc-1-qubit-power-descent/preregistration.md`
  - round `KN-DESC-1`, kind `non-sealing`
  - governed-path digest `b5946338…`, identical to #823's
  - controls: #823 on `dee3b5ae` passes; the disposable commit and the merge M fail with
    `t1:non-control-plane-change` / `t1:not-single-parent`
- Not run: Lean (toolchain host blocked; not routed around); release gate `lean-axioms`.

## 7. Open items for the owner (no action taken)

1. KN-DESC-1's controls P, W, V, I, C, R, G are adopted "as KINF-COPY-1". KINF-COPY-1 is the unfrozen
   draft #822, so before F either #822 lands, or those controls are spelled out in KN-DESC-1, or KN-DESC-1
   names a fixed blob of #822's file.
2. "HP-1" does not resolve on main.
3. The pre-F warning-cleanup choice and the predicted execution tree (module renamed `KnDescent`, census
   family, import line, probe, shard) are still unmeasured at D, as the file already states.
4. A force-push of `wt-C` onto `draft/kn-desc-1` (or a new PR from M) is the owner's call. Its first
   three commits are the cherry-picks, so their SHAs differ from #823's.

***

## 8. Follow-up: self-contained controls, HP-1, native bytes (owner follow-up)

- New head: **`12608076a2bc032ccd93ac947382a37b7d5f05f6`**, single parent `487bb3ac`, unpushed.
  - Worktree: `/tmp/claude-0/-home-user-incompleteness/ce7104bc-8508-557b-9490-8c1ce0f7a1ca/scratchpad/threads/wt-C`.
  - `git diff --stat 487bb3ac..HEAD`: one file (the preregistration), +145/−14.
  - Preregistration blob `438aca73`, sha256 `9f2efb65…9a19`.

### Changes

- **The seven controls are written out** (each with object, expected value, how it is measured, and
  mutations):
  - **P**: probe blob `a8f1ef39`.
  - **W**: `D`'s workflow `159936eb…` plus the frozen edit, giving `f4044098`.
  - **V**: the three tokens; the earned reading and non-inference rule; the probe's last two lines;
    per-cell self-test mutations.
  - **I**: `OIBridge.lean` `9ffd8aa5`.
  - **C**: census `444fedcd`. The family is appended last, with key order fixed, and the file is
    serialized with `json.dumps(indent=2, ensure_ascii=False)` plus a newline, which reproduces D's
    file byte for byte.
  - **R**: the record directory's three files plus any amendments as at F.
  - **G**: the exact `name-status` list from D to E.

  The KINF-COPY-1 sentence in the D paragraph is deleted. The closing line says the controls' form
  follows the KINF-COPY-1 draft and KT4-PREM-1, and that nothing depends on either. #822 is not cited.
  The I/C/R/G content was traced through KTRANS-DENSE-1 → K1-SHARP-TESTS-1 → K2-GUARD-1 → K1-BRIDGE-1
  and KT4-PREM-1 (all landed).
- **New section "The workflow edit (frozen)"**:
  - The `probes_kndesc1` YAML is given in full, inserted after `probes_kt4prem1`, plus four aggregate
    insertions.
  - Measured fact: the frozen probe ends in `sys.exit(0)` under every outcome. So the shard tests the
    last line equals `VERDICT COMPRESSION-DESCENT-EXACT`; otherwise a green shard would not imply the
    verdict.
  - Decision rules are unchanged: Q-EXACT already reads the verdict through `controls.py`.
- **HP-1** names a real file:
  `research/equivalence/handoff-proposals/HP-1-coordinator-roadmap-K-wording.md` at `424aa33b`, blob
  `75ced7d3`. Only research branches carry it. An unrelated `HP-1-lreg-bell.md` exists on
  `research/bridge`.
  - The label is removed from the section heading (it was the only occurrence).
  - One sentence cites the file exactly as the source of the proposed wording (its Kₙ row) and the
    caution (a restatement of its caution (ii)). Both are already stated in full in #823, so nothing
    depends on the file.
- **Native module text, frozen.** `KnDescentDesign.lean` at `d3a95be6` (blob `85b23738`, unmodified)
  with these edits:
  - the 34-line research header is replaced by a neutral header in landed-module style
    (`OIBridge/KnDescent.lean — … (KN-DESC-1)`);
  - the namespace and the 12 print names are renamed;
  - three docstring labels are removed: "(W-DESC)", "(Kₙ-DESC)", "`fullClass_arch` is landed".

  Result: blob `d2c3ebbe47341e3ebc275427c34f05ad3a64db7d`, sha256 `15c8d6a0…3f06a3`, 10688 bytes, 214
  lines. S1's preamble covers the header byte for byte. New mutation: the source header in place of the
  frozen one fails S1 and S4. A scan of the native file for the S4 phrases and research words
  (research, design, disposable, provenance, rebuild, draft, W-DESC, is landed) found 0 hits.
- **New invariant row `C0`:** the exact native bytes (the predicted tree with exactly the named blobs)
  are compiled with `workflow_dispatch`, all jobs green and twelve standard prints, and the ids are
  recorded before F. The predicted-outputs paragraph names the five blobs and records the local
  assembly (below).

### Validation

- **Named-blob regeneration.** A script rebuilds every named blob from the preregistration's own text
  plus D, `d3a95be6` and `424aa33b`. All 11 match: module (blob and sha256), workflow, census,
  `OIBridge.lean`, probe (blob and sha256), the HP-1 file, and the D-workflow and source blobs. Every
  40-hex id in the file is a git object.
- **Local predicted tree** (`wt-C-pred`: D + the five files):
  - release gate: every step PASS except `lean-axioms` (lake download blocked);
  - `lean-manuscript` OK with the family;
  - countercontrol: without the family it fails with `UNCLASSIFIED module KnDescent`;
  - the shard's commands print `checks: 7, failures: 0` and the verdict, and the test passes.

### Checks on `12608076`

- `legacy_records_check`: 303 intact.
- `v3_verifier --receipts`: 46 hold; `--self-test` OK.
- `artifact_placement_check`: OK.
- T1 dry-run from D: five single-parent commits, each touching only the preregistration. Codes: none.
  Governed digest unchanged (`b5946338`).
- Added-lines register scan (S4, §A.32, §A.33 caps and history phrases), 487bb3ac..HEAD: 145 added
  lines, **0 hits** (after quoting one gate token as `` `PASS` ``).
  - Countercontrol: the scan of 9bdce752..487bb3ac reports 11 hits (the S4 phrase list itself, and
    "disposable" in the design-evidence prose).
  - Over the whole round from D, the remaining hits are the quoted S4 list, historical `PASS` cells,
    and "research-only module" / "Disposable commit" describing the historical design objects in the
    evidence section. These are not native text.

### Owner choices flagged (not changed)

1. The frozen probe (blob `a8f1ef39`, byte-identical to `e3_compress.py`) has research labels in its
   docstring: "E3 probe", "quoted in NOTES-E3", "W-DESC", "CONJECTURE [W] + [X]", line refs "at L", and
   "OI supplies". S4 does not scan the probe. Neutralizing the docstring would change P's blob and the
   byte link to the historical source.
2. Every family at D has a `note` key; the frozen family has none. The census tool does not require one.
3. `C0` still needs a CI dispatch of the predicted tree before F. Nothing was pushed this step.
