# #941 Unit 5 — independent evidence review (OD-15, EV-28, EV-14, EV-CI-1, EV-CI-3, EV-L)

Reviewer: independent Unit 5 evidence reviewer (did not write the ledger or the evidence).
Date: 2026-11-06. Authority: owner rulings on #941, comment 6677500012 (amaybaum, 2026-11-06T05:11:33Z),
items 11, 12, 13 and 17, and "Unit 5 may perform the approved evidence review, including OD-15 and
EV-28. Any new scientific execution or workflow dispatch beyond that scoped review requires a separate
authorization."

Read-only. No commit, push, PR, comment, workflow dispatch, Lean or Mathlib build. The only executions
were deterministic Python checks on git objects of `main`, the release gate's census check
(`tools/lean_manuscript_census.py`, no Lean) and the self-test of `tools/lean_axiom_check.py` (which
then reported `SKIPPED`, no lake), plus a read-only download of one existing CI artifact.

**`main` under review:** `424f28b1e7b1201e9a13bd0e608e1b0e4ad9f93b` (merge of #1158, 2026-11-06 06:43 +0200).

**Governing section.** §7 applies the standard the owner set afterwards (#1031 c.6678672357) at `main`
`374b2ef3`. Its verdicts and its "to land" list govern wherever §§0–2 are worded differently.

## 0. Recipe (§A.42 item 1 form)

All checks except §2's artifact layer regenerate from `main` alone.

```
git worktree add --detach <wt> 424f28b1e7b1201e9a13bd0e608e1b0e4ad9f93b
python3 -I u5_check.py <repo> 424f28b1e7b1201e9a13bd0e608e1b0e4ad9f93b            # static layer
python3 -I u5_check.py <repo> 424f28b1e7b1201e9a13bd0e608e1b0e4ad9f93b <art-dir>  # + artifact layer
(cd <wt> && python3 -I tools/lean_manuscript_census.py)                          # census, no Lean
```

- `u5_check.py` (reviewer's script, landed as `u5_check.py` in this directory, sha256
  `d71bce27256a626f3084c323e5171b2886f7bf9c37fca95f58c6512b4b36efbc`) reads only git objects and the
  unpacked artifact; it imports nothing from the evidence-retention archive or the gate.
- `<art-dir>`: artifact `lean-fresh-build-40457712855-1` (id 12714762314), downloaded with
  `gh api repos/amaybaum/incompleteness/actions/artifacts/12714762314/zip` and unpacked with Python's
  `zipfile`. Zip sha256 `d5b8256bc7a19db34629a8ddfaba0824f078ee77f30a5ddfa867b580c0a1a0f8`, equal to the
  host's recorded `digest`; internal `SHA256SUMS` 13/13 OK; `reproduced.json` sha256
  `3bd5fa7d99ae7cfea94e2368a036e92196d3b15a4f536530e3fc219629eed00a`. The artifact expires 2027-01-25.
- **Expected and observed:** exit 0, `"verdict": "PASS"`, `"failures": []`. Output digests (deterministic,
  re-run byte-identical): with artifact `731c12a70439432fbdc5d852f9dd4a70ce6b279b37f18ca717e26dbce03dae08`,
  static only `d21449aae2c9d596e89cb589601a8ae12c183bbb397c5334ce3c2ca797a06ae4`. Census: exit 0,
  `lean_manuscript_census: OK (… 25 current families; complete relative to the maintained registry)`.
- **Controls (all green, in the output):** scanner controls — a planted `sorry`, `axiom` declaration and
  `native_decide` are each caught, the same tokens inside comments are ignored, a comment-only change
  compares equal and a code change does not. Entry mutation controls on the `PhaseSource` entry — a
  forbidden axiom, a dropped report, a shifted line, a renamed declaration, a wrong namespace, a wrong
  `prints` count and `status: partial` are each rejected; the unmutated entry passes. Artifact comparison
  countercontrols — a dropped axiom and a dropped report in `reproduced.json` are each caught.
- **To land:** a later record that relies on this review lands the script, its expected output digests
  and, if it relies on the artifact layer (§2), the subset of `reproduced.json` it uses (the 14 modules'
  reports, 248 entries) with its digest — the artifact is off `main` (§A.42 items 2 and 8). The subset and
  the other small artifact files were scanned for tokens, keys, signed-URL parameters, IPv4 and e-mail
  addresses: no matches.

## 1. OD-15 — the three declarations (owner item 11)

| | `OIBridge.PhaseSource.permClass_onesFixing` | `OIBridge.PhaseSource.onesFixing_not_phasesAvailable` | `OIBridge.PhysicalC4StorageReadback.routedAtStorage_forces_indivisible_somewhere` |
| --- | --- | --- | --- |
| declared on `main` | `PhaseSource.lean`:79, `theorem permClass_onesFixing : OnesFixing permClass` | `PhaseSource.lean`:52, `OnesFixing 𝓘 → 2 ≤ card A → ¬ PhasesAvailable (genTheory 𝓘 arch A)` | `PhysicalC4StorageReadback.lean`:256, `RoutedReadbackAtStorage K R → ∃ n, PIndivisibleWithin n (rootedMap R)` |
| `#print axioms` in source | :204 | :203 | :709 (fully qualified, after `end OIBridge`) |
| module in gated build | `OIBridge.lean`:190; lake default target `OIBridge`, whose import closure is all 241 modules on `main` | same | `OIBridge.lean`:254 |
| short name printed elsewhere | no | no | no |
| `sorry`/`admit`/`axiom`/`native_decide`/`implemented_by`/`extern`/`unsafe`/`ofReduceBool`/`trustCompiler` in code of the import closure (comments stripped) | none (85 modules) | none | none (108 modules) |
| module source `17b830bc` → `main` | byte-identical (blob `63599590`) | same | byte-identical (blob `8bdf3c77`) |
| census family (`verification/lean-manuscript-census.json`) | families[19] "phase source …", `current`, modules `[PhaseSource]`; anchors GR `substratumClass_not_onesFixing` (GR:260), GR "The phase intervention enters as an assumption on the substratum class" (GR:260), Main "as a stated intervention principle …" (Main:590) | same family | families[36] "physical C4 round 2 …", `current`; five Main anchors, all at Main:147, including `` `routedAtStorage_forces_indivisible_somewhere` `` |
| manuscript citation | GR:260 (§3.3), "(kernel: `permClass_onesFixing`, `onesFixing_not_phasesAvailable`, `substratumClass_not_onesFixing` in `OIBridge/PhaseSource.lean`)" | GR:260 | Main:147 (§2.3), "(kernel: `routedAtStorage_forces_return_indivisibility`, `routedAtStorage_forces_indivisible_somewhere` …)" |
| Introduction on `main` | cites none of the three | — | — |
| fresh-build report at `17b830bc` (artifact, §2) | `[propext, Classical.choice, Quot.sound]`, line 204 | same, line 203 | same, line 709 |

**What `tools/lean_axiom_check.py` checks for them** (read from the tool; release gate step `lean-axioms`,
`tools/release_gate.py`:148, with `--require-lake`): it runs `lake build` in `verification/lean-mathlib`,
fails on lake exit ≠ 0, on any `sorryAx` anywhere in the output, on any report matched by
`'([A-Za-z0-9_.']+)' depends on axioms: [...]` with an axiom outside `{propext, Classical.choice,
Quot.sound}`, and on any `#print axioms NAME` (ASCII `NAME`) whose **short name** has no report. All
three names are ASCII and unique as printed short names, so each is fully inside both checks. The tool
checks a subset relation, not the exact axiom list.

**CI (structured, §A.44):** run 42164140276 (`verify.yml`, event `push`, attempt 1, `head_sha`
`424f28b1…`), job 127716522424 "Mathlib bridge", step 5 "Build" `success`, step 6 "Release gate"
`success`. The gate exits 0 only when every sub-check exits 0 (`release_gate.py` `run()`/`main()`), so
`lean-axioms` and `lean-manuscript` passed at the exact `main` head. The build restored the Actions cache
(`--rehash`), so the reports are replays of an elaboration of the same sources.

**Independently checked from `main`:** existence and statements (and that they carry the prose at GR:260
and Main:147); `#print axioms` lines; inclusion in the gated build; unique short names; no
axiom-introducing construct in the code of the import closure; byte identity of both modules from
`17b830bc` to `main`; census registration (both families `current`, anchors present at GR:260, Main:147
and Main:590, census tool exit 0 locally); destination = the formal papers (GR §3.3, Main §2.3), not the
Introduction.

**Rests only on CI:** the kernel's axiom output itself — for the current `main`, run 42164140276's
Release gate (cached build, subset check); exactly `[propext, Classical.choice, Quot.sound]`, from the
fresh-build run 40457712855 at `17b830bc` (§2), whose structured artifact this review re-compared
independently. No Lean elaboration was performed by this review (§A.40; brief).

**Verdict OD-15: verified within scope, except the kernel-output layer, which rests on two CI runs and
cannot be re-derived without a Lean build.** The ledger row is accurate for these three declarations,
with one narrowing: its general sentence "fails on any non-standard axiom or missing report on every
gated build" overstates the tool (finding F1). Owner item 11's condition ("existing CI evidence alone does
not automatically settle") is met for every layer that can be checked without Lean; whether the kernel
layer may rest on CI (the venue §A.40 assigns to Lean builds) is the owner's decision.

## 2. EV-28 — the 14 added module entries (owner item 12)

**Object.** `verification/audits/manuscript/intro-corpus-audit-20261026/introduction-repro-ext/results-121598983127-28.json`,
blob `97a2377dbfc30987887dffea2b72e423feed079d` at the pin `2714278a` and on `main` (unchanged). Baseline
`papers/introduction_repro/results-121598983127.json`, blob `61cfd6ea` at `f5efa7a0` and on `main`.

**README claims, checked:** 28 vs 14 modules; every field other than `expected.modules` identical; the 14
shared entries identical; 534 vs 286 reports; permitted axioms `[propext, Classical.choice, Quot.sound]`;
`run.head_sha` `17b830bc`; the 14 added modules are exactly the README's list (:26–30). All hold.

**What each entry asserts:** at `17b830bc`, module `OIBridge/<M>.lean` has `prints` `#print axioms`
commands at `print_lines`, each with exactly one report naming a declaration, with the listed axioms
(all `[propext, Classical.choice, Quot.sound]`), `status: complete`.

**Checks per entry.**
- S1 the module exists at `17b830bc`, at `2714278a` and on `main`, byte-identical at all three;
- S2 the source's `#print axioms` lines equal the entry's report lines and `print_lines` ranges, and the
  count equals `prints` and the number of reports;
- S3 every report name equals the printed name resolved against the namespace stack at that line, and is a
  declaration in the source tree at `17b830bc`;
- S4 the axiom lists lie within the permitted three (the entry's own content);
- S5 no axiom-introducing construct in the code of the module's whole `OIBridge` import closure at
  `17b830bc`;
- S6 the module is in the gated build (import closure of `OIBridge.lean`) at `17b830bc` and on `main`;
- S7 on `main`, the same print lines and names, and every reported declaration still declared;
- A1 (artifact) the fresh-build run's reproduced reports for the module — name, line and axioms — are
  identical to the entry.

Artifact-level preconditions (A0), from structured files and step conclusions only: run 40457712855
(`evidence-replay.yml` at `14804075f8`, on `main`), job "Lean fresh build at 17b830bc", steps 2–12 all
`success`, including "Build from an empty .lake/build, then the release gate (the recipe)", "Mathlib
resolved to the recorded revision" (`db584cd6`), "Every OIBridge source module built in this job, none
replayed", and "Extract and compare with both expected results" (which exits 0 only if both
`compare_result.py` runs exit 0). Artifact files: `build.exit` 0, `gate.exit` 0; `elaboration.txt`
built 228 = source 228, replayed 0, governed 28 built; `run.json` commit `17b830bc`; `expected-28.json`
blob `97a2377d`; `reproduced.json` build success, markers (`sorryAx`, `Lean.ofReduceBool`, `declaration
uses 'sorry'`, `error:`) all 0, gate verdict pass, `lean-axioms` and `lean-manuscript` PASS.

| module | prints | lines | blob (`17b830bc` = `2714278a` = `main`) | import closure | S1–S7 | A1 | verdict |
| --- | --: | --- | --- | --: | --- | --- | --- |
| `CanonicalMeasure` | 9 | 292–300 | `183cc42a` | 2 | pass | identical | verified (kernel layer via CI) |
| `CausalReadback` | 21 | 324–344 | `d7b71cf5` | 102 | pass | identical | verified (kernel layer via CI) |
| `FiniteEntropy` | 5 | 482–486 | `52fbd89d` | 1 | pass | identical | verified (kernel layer via CI) |
| `FrozenSourcing` | 23 | 345–367 | `0e65cb3b` | 97 | pass | identical | verified (kernel layer via CI) |
| `OIRealization` | 22 | 372–393 | `4df632b7` | 44 | pass | identical | verified (kernel layer via CI) |
| `OperationalAssembly` | 28 | 803–830 | `592d8203` | 25 | pass | identical | verified (kernel layer via CI) |
| `PhaseSource` | 10 | 203–212 | `63599590` | 85 | pass | identical | verified (kernel layer via CI) |
| `PhysicalC4StorageReadback` | 25 | 702–726 | `8bdf3c77` | 108 | pass | identical | verified (kernel layer via CI) |
| `QuantumRepresentationT2` | 17 | 177–193 | `ae858b76` | 109 | pass | identical | verified (kernel layer via CI) |
| `ReadWriteControl` | 9 | 222–230 | `b95b0f7f` | 65 | pass | identical | verified (kernel layer via CI) |
| `RootedClassification` | 16 | 349–364 | `ffb7546f` | 105 | pass | identical | verified (kernel layer via CI) |
| `RootedClassificationAllTime` | 16 | 252–267 | `13123378` | 107 | pass | identical | verified (kernel layer via CI) |
| `StructuralClosure` | 35 | 433–467 | `d6999cd1` | 66 | pass | identical | verified (kernel layer via CI) |
| `SubstratumInterface` | 12 | 208–219 | `1c61fa6e` | 64 | pass | identical | verified (kernel layer via CI) |

Total 248 reports = 534 − 286. No report name needed resolution through `open`.

**Differences between `2714278a` and `main`:** none in `verification/lean-mathlib` (tree identical), none
in the expected result. From `17b830bc` to `main`: 13 modules added, `OIBridge.lean` adds 13 imports only,
and `C3Necessity`, `RouteB`, `SecondOrderDrive`, `WordTraceSufficiency` change in comments only
(comment-stripped text equal); `lakefile.toml` and `lean-toolchain` unchanged. None of the 14 modules
imports a code-changed module. So the 14 entries describe `main`'s sources as well, given the same
Mathlib revision; run 42164140276 (§1) confirms the subset property for them at `main`'s head.

**What cannot be verified within scope.** The axiom lists themselves — the kernel's output — for all 14
entries. They are an output of Lean elaboration; reproducing them needs `lake build` against Mathlib,
which §A.40 and this brief place in CI, and the only CI route is a `lean-fresh-build` dispatch of
`evidence-replay.yml` (not authorized). Static checks S4–S5 exclude every source-level route to a
non-standard axiom in the `OIBridge` closure, but not exactness ("exactly the three") and not Mathlib.
The kernel layer here rests on the fresh-build run 40457712855 (an elaboration from an empty
`.lake/build`, 0 replayed) and on the cached runs (job 121598983127, which produced the file; run
42164140276 at `main`). The reviewer's A1 comparison is independent of the archive's comparator but uses
the frozen extractor's parse inside the job; S2–S3 independently exclude a dropped or misattributed
report, and the in-job `lean-axioms` PASS (a different parser) independently gives the subset property.

**Overall EV-28 verdict: every assertion of the 14 entries that can be checked without a Lean build is
independently verified from `main` (S1–S7 pass for all 14); the kernel-output layer is verified only
against an existing CI fresh-build artifact, independently re-compared (A1 identical for all 14), and is
not independently re-elaborated.** EV-28 can be closed by this review only if the owner accepts a CI
fresh build, re-compared by an independent reviewer, as the verification standard for Lean axiom
reports. If accepted, the closing record lands the evidence it uses (§0 "To land") and corrects
`introduction-repro-ext/README.md`:3–6 and :63–67 and `evidence-replay.yml`:22–24. If not, the remaining
route is one separately authorized `lean-fresh-build` dispatch on `main` (it now reads `EXPECTED_28` from
`2714278a`), with its structured outcome reviewed and landed; #941 stays accountable until then (owner
item 12).

## 3. EV-14 — the 14-module historical result (owner item 13)

**Disposition accurate.** The result supports no current claim: `papers/Introduction.md` on `main`
(last changed `64a84b12`) has no Appendix A and cites none of the declarations; it says (L183) that the
formal papers name the checked declarations. On `main` the result is referenced only by
`papers/introduction_repro/README.md`, the ext README, `evidence-replay.yml` and the root `README.md`:117
("historical verification evidence"); no manuscript or record uses it as support. The release gate's
`lean-axioms` step re-checks the current sources on every gated build (run 42164140276). Keeping no
verification obligation is consistent with §A.42 item 5 and §A.46 item 4.

**Every line on `main` naming #941** (`git grep` at `424f28b1`):

| line | text | owner of the change | proposal |
| --- | --- | --- | --- |
| `papers/introduction_repro/README.md`:8–9 | "…extends it. The accountable Issue is #941. It uses…" | EV-14 | replace "The accountable Issue is #941." with "Its review is recorded on Issue #941." (keeps provenance; true after closure). Alternative: delete the sentence. |
| `.github/workflows/evidence-replay.yml`:7 | "…which supports no claim in the Introduction on main (Issue #941)." | EV-14 | no change needed: a provenance citation for a statement that stays true; it names no accountability. If changed for uniformity: "(reviewed on Issue #941)". |
| `.github/workflows/evidence-replay.yml`:22–24 | "The 28-module result has no independent review recorded on main and is not independently verified there; the re-pin to 2714278a preserves evidence and is not its acceptance (Issue #941)." | EV-28 | change only with EV-28's outcome; if this review is accepted and landed, state the review's record path instead. |
| `introduction-repro-ext/README.md`:3–6 | Status: "not independently verified on `main` … The accountable Issue is #941." | EV-28 | as the row above. |
| `introduction-repro-ext/README.md`:8 | "Retained under the owner decision on #941 (comment 6658967061 …)" | — | provenance; no change. |

**Trigger check for a comment-only workflow edit (§A.43 item 4):** `evidence-replay.yml` has only
`workflow_dispatch`, so editing it starts nothing by itself. The path-filtered push workflows
(`bg2-orientation-design.yml`, `bridge-compatibility-research.yml`, `hidden-sector-replay.yml`) do not
match `.github/workflows/evidence-replay.yml` or either README. `verify.yml` runs on every `pull_request`
and on `push` to `main`: ordinary CI, not a governed launch. Pushing a change under `.github/workflows/`
needs a credential with workflow-write permission.

**Verdict EV-14: (b) accurate; pointer correction needed only at `papers/introduction_repro/README.md`:9.
The ledger's inclusion of workflow :7 is not necessary.**

## 4. EV-CI-1, EV-CI-3, EV-L (owner item 17; ledger)

**EV-CI-1** (fresh-build `introduction_repro` at `17b830bc`). Executed once: run 40457712855 is the only
`lean-fresh-build` run of `evidence-replay.yml` (three runs in all, one per activity), dispatched at
`14804075f8` (on `main`), every step `success`; #942 c.6435469998 reports it. It supports no current
claim (§3). **Verdict: accept (b).** Cross-dependency: if the owner accepts §2's route, this run's artifact
becomes support for EV-28, and the content used must land on `main` with the EV-28 record; the (b)
statement "no surviving claim needs a `main`-retained replay" then holds for the 14-module result only.

**EV-CI-3** (BHa/BHb mutants and BHb `-O`). Runs 40457715566 (bh-mutants: "BH-01 mutants.py" and "BH-02
mutants.py" `success`; the BH-01 step exits 0 only if `mutants.py` exits 0 and its output equals the
retained `mutants-output.json`) and 40457717824 (bhb-optimized: the `cmp` step `success`), both at
`14804075f8`, one dispatch each. The records `bh01_access_v1/` and `bh02_scramble_v1/` are byte-identical at
`eae01647` (on `main`) and `424f28b1`; `mutants-output.json` blob `459f7f32`, BH-02 `result.json` blob
`c661f4f6` on `main`, as #942 c.6435105802 states. Introduction L163 and L165 make existence, bound and
obstruction statements with no numeric value, citing [BHa]/[BHb] (L203, L205) for proofs and code under
those directories. **Verdict: accept (b);** no dispatch needed or made. A local re-run of the records'
`checks.py` was not performed (outside the scoped review).

**EV-L** (step-7 evidence levels, 409 rows). EVIDENCE.md at `16fc745d` (off `main`): 44 reproduced, 127
certificate-checked, 235 traced-only, 3 failed = 409; items E1 122, E2 20, E3 36 (178), as the ledger says.
#942 c.6433846714 (2026-10-27) reports "Checkpoint `cb2029ce`: step 7 accepted", with the reviewer's report
recorded verbatim at `cb2029ce:…/review/EVIDENCE-RECHECK-2bc65ae9.md` ("Verdict: ACCEPT", independent
aggregation `reagg3.py`, 0 differences). The levels and item counts are identical at `cb2029ce` and
`16fc745d`; the later commits (`851ffef9`, E3-16 concept DOI; `ccb4f122`, step-9 verdict relabels) are
outside that acceptance (E3-16 is O-26's, owner item 7). The rows map the Introduction at `4a260ca9`
(off `main`), which #1134 (merged `9f9dbc28`) rewrote. **Verdict: accept (b), with two narrowings of the
ledger's wording:** "independently accepted" rests on an author-posted report and an off-`main` review
file, so it is provenance for a disposition that uses no step-7 level as support (§A.46 item 7); and
"superseded … by #1134" rests on the rewritten Introduction on `main`, not on #1134's claim map, which was
dropped before merge (`6bafd2d3`).

**EV-CI-2, X-4:** EV-CI-2 (retention) confirmed: blob `97a2377d` on `main` since `2714278a`. X-4: the
`#941` lines are exactly those of §3's table (four accountability/status lines in three files plus the
provenance line ext README:8).

## 5. Findings (§A.31)

- **F1 (NEW, tool; cross-propagates).** `tools/lean_axiom_check.py` reads report and print names with
  `[A-Za-z0-9_.']+`. On `main`, 15 `#print axioms` commands (in `ClosureObstruction`,
  `PhysicalCharacterization`, `PositiveReachability`, `QuasilocalAlgebra`, `RankGapTheory`) name
  identifiers with subscripts (e.g. `G₀_apply`). Their reports escape both the axiom check and the
  missing-report check; only the global `sorryAx` scan applies. Control: `analyse()` on a log with
  `'OIBridge.R.G₀_apply' depends on axioms: [propext, Lean.ofReduceBool]` returns 0 failures. The
  missing-report check is by short name, and 26 printed short names occur in more than one module, so a
  silent print can be masked. No current exposure: the comment-stripped code of all 241 modules on `main`
  contains no `sorry`, `axiom`, `native_decide`, `implemented_by`, `extern`, `unsafe`, `ofReduceBool` or
  `trustCompiler`, and the frozen extractor (`'(.+?)'`, global `Lean.ofReduceBool` marker) covers these
  names in the replay. Consequence: the ledger's OD-15 sentence and EVIDENCE.md's "Limits" paragraph
  ("every printed report lies within the allow-list and every declared `#print axioms` has a report")
  overstate the gate; they hold for ASCII names with unique short names, which includes all three OD-15
  declarations and all 248 EV-28 reports. Not a #941 closure blocker; it needs an accountable Issue for the
  tool (widen the name pattern, add a global `Lean.ofReduceBool` marker, check missing reports by full name).
- **F2 (BORDERLINE, formal coverage; outside OD-15's axiom/census question).** GR:260 reads "no class whose
  isometries do so realizes a quarter phase at any level with two or more states" with kernel
  `onesFixing_not_phasesAvailable`. The theorem proves `¬ PhasesAvailable`, i.e. not every level carries
  every phase gate, for a carrier with `2 ≤ card A`; its proof refutes the level-1 gate only. A per-level
  reading ("at no level with two or more states") is stronger than the stated theorem, though the same
  argument would prove it. For the GR formal-coverage owner; no change proposed here.
- **F3 (ELABORATING).** EV-CI-1's run is the kernel-layer support for EV-28 if the owner accepts §2; the
  two rows' dispositions must then be recorded together (§4).

## 6. Off-`main` references in this review (§A.42 item 8)

| reference | classification |
| --- | --- |
| run 42164140276 / job 127716522424 (structured step conclusions) | support off `main` for the kernel layer of OD-15 at `main` (CI; provenance under §A.42 item 2) |
| run 40457712855, artifact 12714762314 (`reproduced.json`, `elaboration.txt`, exits) | support off `main` for EV-28/OD-15 exact axiom lists; a gap until the used subset lands (§0) |
| runs 40457715566, 40457717824 | provenance for EV-CI-3 (no claim uses them; records on `main`) |
| job 121598983127 / run 40330683786 | provenance (origin of the expected result) |
| `16fc745d`, `cb2029ce`, `2bc65ae9`, `8f6ea594`, `4a260ca9`, `e73f7be3` | provenance for EV-L / EV-28 history; no conclusion here uses their content as support |
| #942 c.6433846714, c.6435469998, c.6435105802; #941 c.6428100988 | provenance (author-posted reports) |
| `17b830bc`, `2714278a`, `f5efa7a0`, `14804075f8`, `eae01647`, `48b18ac5`, `9f9dbc28` | on `main` |

## 7. Owner-standard verification (c.6678672357)

Standard: #1031 comment 6678672357 (amaybaum, 2026-11-06T06:26:04Z), section 3. The owner chose CI
evidence plus an independent re-comparison, with no new full Lean build. This section meets that
standard. Every report is compared individually by module and by fully qualified name. This review ran
no Lean build and dispatched nothing.

**`main` for this section:** `374b2ef3d0af1f3233a1d6bc74bee3c32683e3c0` (merge of #1159). Diff from
`424f28b1`: `README.md`, `papers/introduction_repro/README.md` (prose only: 28 → 29 declarations and
one added table row; the JSON is unchanged), `CLOSURE-LEDGER.md` and three `tracks/SC*/README.md`. It
changes nothing in `verification/lean`, `verification/lean-mathlib`, `tools/`, `.github/`, the census
registry, `papers/GR.md`, `papers/Main.md`, either expected-result JSON or the ext directory. The census
check run on a checkout at `374b2ef3` exits 0 with the same summary.

### 7.0 Recipe (§A.42 item 1)

```
gh api repos/amaybaum/incompleteness/actions/jobs/121598983127/logs > <H>   # pinned historical log
# <F> = build-and-gate.log in artifact 12714762314 (§0)
python3 -I u5_reextract.py <repo> 374b2ef3d0af1f3233a1d6bc74bee3c32683e3c0 <H> <F> <table.tsv>
```

- `u5_reextract.py`: landed in this directory, sha256
  `105e7e342e082b5479ad1d94656c81fa83483660d8e0cbd5ad1597bca3ed57f0`. It is the reviewer's own log
  parser and source resolver. It imports nothing from the archive's extractor or comparator, the gate,
  or `u5_check.py`.
- **Expected and observed:** exit 0, `"verdict": "PASS"`, `"mismatches": []`. The JSON output has sha256
  `5c905fcaa4027c114eaf4891bc2e5331bfc2ae38feb0e01e562419052f028fa3`; a re-run was byte-identical. The
  per-report table `u5_reports.tsv` has 248 rows and sha256
  `2f4610d54620d67ac9bcab3419ddf377f907827b14db4084622a7c8997f898f2`.
- **Controls, all green.** Parser controls:
  - a wrapped axiom list is joined;
  - the "does not depend on any axioms" form is read;
  - a name with subscripts that carries a forbidden axiom is read as such;
  - a primed name (`f'`) is read;
  - a report attributed to the root `OIBridge.lean` is read;
  - namespace and section resolution of `#print axioms` gives the expected fully qualified names.

  Comparison mutation controls on `OIBridge.PhaseSource.permClass_onesFixing`. Each of these is
  rejected, and the unmutated data passes:
  - a missing report;
  - the report moved to another module;
  - a changed axiom list;
  - a shifted line;
  - a duplicated report.
- **Parser defect found and fixed during the run.** The first run of the parser read report names as
  `'[^']+'`. It therefore missed primed names and the reports attributed to `OIBridge.lean`, and it
  showed two false mismatches in `QuantumRepresentationT2` (`hadData_bornPow_succ'` and `_zero'`). Its
  unparsed-line guard caught both defects. The corrected parser (`'(.+?)'`, with an optional
  `OIBridge/` prefix) reads 6123 reports from the served historical text. That equals the retained
  JSON's own `observed.reports_in_served_text` (6123), a figure the parser was not tuned to.

### 7.1 Objects compared

- **(J) Retained JSON.** On `main`:
  `verification/audits/manuscript/intro-corpus-audit-20261026/introduction-repro-ext/results-121598983127-28.json`,
  blob `97a2377dbfc30987887dffea2b72e423feed079d`. It is the blob `EXPECTED_28` pins (`2714278a`;
  `evidence-replay.yml`:62–63 and :98), and it is unchanged from `2714278a` to `374b2ef3`.
- **(H) The pinned historical log.** The log J names as its source: job 121598983127 ("Mathlib bridge")
  of run 40330683786 (`verify.yml`, `push`, `head_sha` `17b830bc`). J pins it by
  `source.served_sha256` (`1a83921f…`) over the served lines 1–38918 of 43064.
  - Fetched read-only on 2026-11-06: 43064 lines, sha256
    `bc2291bc57d952779f27282211b588321618bf503d39d192840c777074cd0c81`. This equals the full-log digest
    recorded in `papers/introduction_repro/README.md`.
  - Lines 1–38918 hash to `1a83921fb967dad82785ce79b06013f184f4a82e377e39cad21ab4df453e09df`, equal to
    J's `served_sha256`. So H is exactly the text J was extracted from.
  - The log is not committed (§A.42 item 4), and the host's retention of it expires.
- **(F) Archived fresh-build log.** `build-and-gate.log` in artifact 12714762314 of run 40457712855,
  sha256 `31e5045bc9c4d563566a7600dd9e747d658e2ac44b083de232f4d71d37ad8979`. It is covered by the
  artifact's `SHA256SUMS`, and the host's `digest` for the artifact's zip matches.
- **(S) Source.** The `#print axioms` commands of each module at the source commit `17b830bc`, resolved
  to fully qualified names, and at `main` `374b2ef3`.

### 7.2 OD-15: the three declarations, by fully qualified name

**1. `OIBridge.PhaseSource.permClass_onesFixing`**
- Source at `main`: `verification/lean-mathlib/OIBridge/PhaseSource.lean`:79, in `namespace
  OIBridge` / `namespace PhaseSource`. Statement: `theorem permClass_onesFixing : OnesFixing permClass`.
- `#print axioms`: line 204 (`#print axioms permClass_onesFixing`).
- Reported axioms, matched by fully qualified name in module `OIBridge/PhaseSource.lean`:
  - F, line 204: `[propext, Classical.choice, Quot.sound]`;
  - H, line 204: the same;
  - J, line 204: the same.
- No other module reports this name in H or F. The axioms lie within the permitted set, which they
  equal exactly.
- Census: families[19], "phase source: the stated access and the stipulated phases", status `current`.
  Its anchors are present: GR `substratumClass_not_onesFixing` (GR:260); GR "The phase intervention
  enters as an assumption on the substratum class" (GR:260); Main "as a stated intervention principle
  rather than a consequence of its finite states and bijective dynamics" (Main:590).
- GR:260 (§3.3): "every isometry that dynamics and the stated observer access supply carries the
  all-ones vector to a multiple of itself, no class whose isometries do so realizes a quarter phase at
  any level with two or more states, and the quarter phase carries that vector off its ray (kernel:
  `permClass_onesFixing`, `onesFixing_not_phasesAvailable`, `substratumClass_not_onesFixing` in
  `OIBridge/PhaseSource.lean`)".

**2. `OIBridge.PhaseSource.onesFixing_not_phasesAvailable`**
- Source at `main`: `PhaseSource.lean`:52. Statement: `theorem onesFixing_not_phasesAvailable {𝓘}
  (arch : Architecture 𝓘) (hf : OnesFixing 𝓘) (h2 : 2 ≤ Fintype.card A) : ¬ PhasesAvailable
  (genTheory 𝓘 arch A)`.
- `#print axioms`: line 203.
- Reported axioms in `OIBridge/PhaseSource.lean`: F, H and J all give line 203 and
  `[propext, Classical.choice, Quot.sound]`.
- Reported only from this module. Within the permitted set.
- Census family and the GR:260 text: as for item 1.

**3. `OIBridge.PhysicalC4StorageReadback.routedAtStorage_forces_indivisible_somewhere`**
- Source at `main`: `verification/lean-mathlib/OIBridge/PhysicalC4StorageReadback.lean`:256.
  Statement: `theorem routedAtStorage_forces_indivisible_somewhere {K : ℕ} {R : RootedRealization V H}
  (h : RoutedReadbackAtStorage K R) : ∃ n, PIndivisibleWithin n (rootedMap R)`.
- `#print axioms`: line 709, fully qualified, after `end OIBridge`.
- Reported axioms in `OIBridge/PhysicalC4StorageReadback.lean`: F, H and J all give line 709 and
  `[propext, Classical.choice, Quot.sound]`.
- Reported only from this module. Within the permitted set.
- Census: families[36], "physical C4 round 2: the storage-time reading of the store clause, and the two
  readings' relation", status `current`. It has five anchors, all present at Main:147, including
  `` `routedAtStorage_forces_indivisible_somewhere` ``.
- Main:147 (§2.3): "Under either reading, the rooted family is not P-divisible on $\{0, \ldots, n\}$ for
  every $n > s$ with $\Gamma_n = I$, and so for some $n$, because $(\Gamma_t)$ is periodic and
  $\Gamma_0 = I$ (kernel: `routedAtStorage_forces_return_indivisibility`,
  `routedAtStorage_forces_indivisible_somewhere` in `OIBridge/PhysicalC4StorageReadback.lean` for the
  storage-time reading; …)".

The same three rows appear in the §7.4 table at rows 112, 113 and 126. The scientific claims these
declarations support keep their existing proof-status qualifications. F2 (§5) does not identify an
error in GR:260; it notes that one reading is stronger than the stated theorem, and it proposes no edit.

### 7.3 EV-28: all 248 reports of the 14 added modules

Each report is keyed by (module path, fully qualified name). A row passes only if all of the following
hold:
- S at `17b830bc` has exactly one `#print axioms` resolving to that name in that module;
- H and F each have exactly one report of that name attributed to that module file;
- the lines agree across S, H, F and J, and the print line on `main` is the same;
- the axiom lists agree across H, F and J, and equal `[propext, Classical.choice, Quot.sound]`;
- no other module reports the same name in H or F;
- J and S carry the same set of names.

In addition, the check rejects any report in that module file of H or F that has no source print.

| module | S prints | J reports | H reports | F reports | mismatches |
| --- | --: | --: | --: | --: | --: |
| `CanonicalMeasure` | 9 | 9 | 9 | 9 | 0 |
| `CausalReadback` | 21 | 21 | 21 | 21 | 0 |
| `FiniteEntropy` | 5 | 5 | 5 | 5 | 0 |
| `FrozenSourcing` | 23 | 23 | 23 | 23 | 0 |
| `OIRealization` | 22 | 22 | 22 | 22 | 0 |
| `OperationalAssembly` | 28 | 28 | 28 | 28 | 0 |
| `PhaseSource` | 10 | 10 | 10 | 10 | 0 |
| `PhysicalC4StorageReadback` | 25 | 25 | 25 | 25 | 0 |
| `QuantumRepresentationT2` (namespace `OIBridge.QuantumRepresentation`) | 17 | 17 | 17 | 17 | 0 |
| `ReadWriteControl` | 9 | 9 | 9 | 9 | 0 |
| `RootedClassification` | 16 | 16 | 16 | 16 | 0 |
| `RootedClassificationAllTime` | 16 | 16 | 16 | 16 | 0 |
| `StructuralClosure` | 35 | 35 | 35 | 35 | 0 |
| `SubstratumInterface` | 12 | 12 | 12 | 12 | 0 |
| **total** | **248** | **248** | **248** | **248** | **0** |

**Mismatches: none.** No report is missing, and none is extra, duplicated, attributed to another
module, on a different line, or carrying an axiom outside the three. The 248 print commands are on the
same lines at `17b830bc`, `2714278a` and `374b2ef3`, because all 14 module sources are byte-identical
across those commits (§2).

### 7.4 Completeness: the per-report table

The table keyed by (module, fully qualified name) is in Appendix A below. It is rendered from
`u5_reports.tsv`, sha256 `2f4610d54620d67ac9bcab3419ddf377f907827b14db4084622a7c8997f898f2`, which holds
every column in full. P3 = `propext, Classical.choice, Quot.sound`.

### 7.5 CI identities

| run | workflow, event | head SHA | job (id) and conclusions | kind |
| --- | --- | --- | --- | --- |
| 40330683786 | `verify.yml`, `push`, attempt 1, `success` | `17b830bcd0ecc36e10eff5b9eeca03bdd7198d86` | "Mathlib bridge" (121598983127) `success`: "Restore the OIBridge build cache" `success`, "Build" `success`, "Release gate" `success` | historical archived evidence. Source of J and H. The build restored the cache, and lake replayed the modules. |
| 40457712855 | `evidence-replay.yml` at `14804075f8f98588ec25c61fe8908b871fb74231`, `workflow_dispatch`, attempt 1, `success` | `14804075f8…`; checks out `17b830bc` | "Lean fresh build at 17b830bc" (122034819227) `success`: "Build from an empty .lake/build, then the release gate (the recipe)" `success`, "Mathlib resolved to the recorded revision" `success`, "Every OIBridge source module built in this job, none replayed" `success`, "Extract and compare with both expected results" `success`, "No tracked file changed" `success` | historical archived evidence. Source of F: a CI build from an empty `.lake/build` on 2026-10-27, not performed by this review. |
| 42164140276 | `verify.yml`, `push`, attempt 1, `success` | `424f28b1e7b1201e9a13bd0e608e1b0e4ad9f93b` | "Mathlib bridge" (127716522424) `success`: "Build" `success`, "Release gate" `success` | current-source CI. Its Lean sources, tools and census are identical to those at `374b2ef3`. The build used the cache. The gate's `lean-axioms` step checks only that axioms fall within the permitted set (F1 applies). |
| 42174428450 | `verify.yml`, `push`, attempt 1 | `374b2ef3d0af1f3233a1d6bc74bee3c32683e3c0` | "Mathlib bridge" (127749493708): "Build" `success` and "Release gate" `success` when read; the job's later steps were still running, so the job conclusion is pending | current-source CI at `main` |

The "Release gate" step succeeds only if every one of its 22 sub-checks exits 0 (`tools/release_gate.py`).
The current-source runs show that the sources now on `main` pass the subset check. The exact axiom
lists rest on H and F, which are historical.

### 7.6 Gaps

- **Correspondences not established: none.** Every required correspondence holds for all 248 reports
  and all three OD-15 declarations: (module, name) between S and H, F and J; line; axioms; membership
  in the permitted set; census family; anchors.
- **Limits:**
  - No Lean elaboration was performed by this review.
  - H is a CI job log held by the host, not on `main`; it is pinned only by digests in J and in the
    README.
  - F's build was a CI build dispatched by the evidence's author, not by this review.
  - A record that lands this review should carry:
    - `u5_reextract.py` and `u5_check.py`;
    - `u5_reports.tsv`;
    - the output digests;
    - the digests of H and F.

    It should not carry H or F themselves (§A.42 items 2 and 4). The reliance on H and F is then
    provenance-bounded, as this standard accepts.
  - The current-source CI does not record its resolved Mathlib revision (no `lake-manifest.json` is
    committed), and it checks only that axioms fall within the permitted set.

### 7.7 Verdict

- **OD-15:** independently audited historical evidence. The three declarations were checked by fully
  qualified name against:
  - their exact Lean sources on `main`, where both modules are unchanged since `17b830bc`;
  - their `#print axioms` lines;
  - the reports in the pinned historical log and the archived fresh-build log, which match the retained
    JSON;
  - the permitted axiom set;
  - their census families;
  - their manuscript anchors at GR:260 and Main:147.

  No correspondence is missing. Current-source CI at `424f28b1` and at `374b2ef3` ("Build" and "Release
  gate" `success`) shows the current sources pass the gate's subset check.
- **EV-28:** independently audited historical evidence. All 248 reports of the 14 added module entries
  were re-extracted by an independent parser from the pinned historical log (job 121598983127; the
  served text's digest equals the retained JSON's `served_sha256`) and from the archived fresh-build log
  (run 40457712855). Each was compared individually, by module and by fully qualified name, with the
  source at `17b830bc` and with the retained JSON (`97a2377d`, as pinned by `EXPECTED_28` = `2714278a`):
  0 mismatches. This review makes no claim of a fresh reproduction.

# Appendix A — per-report table (§7.4)

| # | module | fully qualified name | S line (`17b830bc`) | S line (`main`) | H line | H axioms | F line | F axioms | J line | J axioms | result |
| --: | --- | --- | --: | --: | --: | --- | --: | --- | --: | --- | --- |
| 1 | `CanonicalMeasure` | `OIBridge.CanonicalMeasure.counting_invariant` | 295 | 295 | 295 | P3 | 295 | P3 | 295 | P3 | ok |
| 2 | `CanonicalMeasure` | `OIBridge.CanonicalMeasure.counting_maximal_entropy` | 297 | 297 | 297 | P3 | 297 | P3 | 297 | P3 | ok |
| 3 | `CanonicalMeasure` | `OIBridge.CanonicalMeasure.determinism_reversibility_selected_measure` | 300 | 300 | 300 | P3 | 300 | P3 | 300 | P3 | ok |
| 4 | `CanonicalMeasure` | `OIBridge.CanonicalMeasure.entropy_counting` | 296 | 296 | 296 | P3 | 296 | P3 | 296 | P3 | ok |
| 5 | `CanonicalMeasure` | `OIBridge.CanonicalMeasure.injective_imp_bijective` | 292 | 292 | 292 | P3 | 292 | P3 | 292 | P3 | ok |
| 6 | `CanonicalMeasure` | `OIBridge.CanonicalMeasure.invariance_does_not_select` | 298 | 298 | 298 | P3 | 298 | P3 | 298 | P3 | ok |
| 7 | `CanonicalMeasure` | `OIBridge.CanonicalMeasure.invariant_iff` | 293 | 293 | 293 | P3 | 293 | P3 | 293 | P3 | ok |
| 8 | `CanonicalMeasure` | `OIBridge.CanonicalMeasure.orbit_invariant_unique` | 294 | 294 | 294 | P3 | 294 | P3 | 294 | P3 | ok |
| 9 | `CanonicalMeasure` | `OIBridge.CanonicalMeasure.two_cycle_witness` | 299 | 299 | 299 | P3 | 299 | P3 | 299 | P3 | ok |
| 10 | `CausalReadback` | `OIBridge.CausalReadback.c4e_implies_c4r` | 329 | 329 | 329 | P3 | 329 | P3 | 329 | P3 | ok |
| 11 | `CausalReadback` | `OIBridge.CausalReadback.c4e_implies_pIndivisible` | 331 | 331 | 331 | P3 | 331 | P3 | 331 | P3 | ok |
| 12 | `CausalReadback` | `OIBridge.CausalReadback.c4e_implies_pIndivisible_via_c4r` | 332 | 332 | 332 | P3 | 332 | P3 | 332 | P3 | ok |
| 13 | `CausalReadback` | `OIBridge.CausalReadback.c4r_implies_pIndivisible` | 330 | 330 | 330 | P3 | 330 | P3 | 330 | P3 | ok |
| 14 | `CausalReadback` | `OIBridge.CausalReadback.causal_readback_verdict` | 344 | 344 | 344 | P3 | 344 | P3 | 344 | P3 | ok |
| 15 | `CausalReadback` | `OIBridge.CausalReadback.control_separation` | 343 | 343 | 343 | P3 | 343 | P3 | 343 | P3 | ok |
| 16 | `CausalReadback` | `OIBridge.CausalReadback.j2_isRowStochastic` | 335 | 335 | 335 | P3 | 335 | P3 | 335 | P3 | ok |
| 17 | `CausalReadback` | `OIBridge.CausalReadback.j2_rows_eq` | 337 | 337 | 337 | P3 | 337 | P3 | 337 | P3 | ok |
| 18 | `CausalReadback` | `OIBridge.CausalReadback.not_c4e_and_not_c4r_of_pDivisible` | 333 | 333 | 333 | P3 | 333 | P3 | 333 | P3 | ok |
| 19 | `CausalReadback` | `OIBridge.CausalReadback.one_isRowStochastic` | 336 | 336 | 336 | P3 | 336 | P3 | 336 | P3 | ok |
| 20 | `CausalReadback` | `OIBridge.CausalReadback.one_rows_ne` | 338 | 338 | 338 | P3 | 338 | P3 | 338 | P3 | ok |
| 21 | `CausalReadback` | `OIBridge.CausalReadback.pdFamily_not_c4e_not_c4r` | 340 | 340 | 340 | P3 | 340 | P3 | 340 | P3 | ok |
| 22 | `CausalReadback` | `OIBridge.CausalReadback.pdFamily_pDivisible` | 339 | 339 | 339 | P3 | 339 | P3 | 339 | P3 | ok |
| 23 | `CausalReadback` | `OIBridge.CausalReadback.peFamily_c4e` | 341 | 341 | 341 | P3 | 341 | P3 | 341 | P3 | ok |
| 24 | `CausalReadback` | `OIBridge.CausalReadback.peFamily_pIndivisible` | 342 | 342 | 342 | P3 | 342 | P3 | 342 | P3 | ok |
| 25 | `CausalReadback` | `OIBridge.CausalReadback.rootedMap_isRowStochastic` | 334 | 334 | 334 | P3 | 334 | P3 | 334 | P3 | ok |
| 26 | `CausalReadback` | `OIBridge.CausalReadback.rows_eq_of_factor` | 328 | 328 | 328 | P3 | 328 | P3 | 328 | P3 | ok |
| 27 | `CausalReadback` | `OIBridge.CausalReadback.tv_eq_zero_iff` | 325 | 325 | 325 | P3 | 325 | P3 | 325 | P3 | ok |
| 28 | `CausalReadback` | `OIBridge.CausalReadback.tv_mul_le` | 327 | 327 | 327 | P3 | 327 | P3 | 327 | P3 | ok |
| 29 | `CausalReadback` | `OIBridge.CausalReadback.tv_nonneg` | 324 | 324 | 324 | P3 | 324 | P3 | 324 | P3 | ok |
| 30 | `CausalReadback` | `OIBridge.CausalReadback.tv_pos_of_ne` | 326 | 326 | 326 | P3 | 326 | P3 | 326 | P3 | ok |
| 31 | `FiniteEntropy` | `OIBridge.FiniteEntropy.cmi3_nonneg` | 484 | 484 | 484 | P3 | 484 | P3 | 484 | P3 | ok |
| 32 | `FiniteEntropy` | `OIBridge.FiniteEntropy.cmi_le_log_card` | 486 | 486 | 486 | P3 | 486 | P3 | 486 | P3 | ok |
| 33 | `FiniteEntropy` | `OIBridge.FiniteEntropy.cmi_le_of_deterministic` | 485 | 485 | 485 | P3 | 485 | P3 | 485 | P3 | ok |
| 34 | `FiniteEntropy` | `OIBridge.FiniteEntropy.entropy_le_log_card` | 483 | 483 | 483 | P3 | 483 | P3 | 483 | P3 | ok |
| 35 | `FiniteEntropy` | `OIBridge.FiniteEntropy.sum_mul_log_le` | 482 | 482 | 482 | P3 | 482 | P3 | 482 | P3 | ok |
| 36 | `FrozenSourcing` | `OIBridge.FrozenSourcing.fixedGateTheory_outside_ceiling` | 367 | 367 | 367 | P3 | 367 | P3 | 367 | P3 | ok |
| 37 | `FrozenSourcing` | `OIBridge.FrozenSourcing.frozen_sourcing_verdict` | 365 | 365 | 365 | P3 | 365 | P3 | 365 | P3 | ok |
| 38 | `FrozenSourcing` | `OIBridge.FrozenSourcing.le_zero_of_forall_pos` | 346 | 346 | 346 | P3 | 346 | P3 | 346 | P3 | ok |
| 39 | `FrozenSourcing` | `OIBridge.FrozenSourcing.mixImage_not_preservesNonneg` | 357 | 357 | 357 | P3 | 357 | P3 | 357 | P3 | ok |
| 40 | `FrozenSourcing` | `OIBridge.FrozenSourcing.nonnegBounded_not_denseUnitaryControl` | 355 | 355 | 355 | P3 | 355 | P3 | 355 | P3 | ok |
| 41 | `FrozenSourcing` | `OIBridge.FrozenSourcing.nonnegBounded_not_denseUnitaryControl_rot` | 358 | 358 | 358 | P3 | 358 | P3 | 358 | P3 | ok |
| 42 | `FrozenSourcing` | `OIBridge.FrozenSourcing.nonnegBounded_not_derivedOI` | 353 | 353 | 353 | P3 | 353 | P3 | 353 | P3 | ok |
| 43 | `FrozenSourcing` | `OIBridge.FrozenSourcing.nonnegBounded_not_phasesAvailable` | 351 | 351 | 351 | P3 | 351 | P3 | 351 | P3 | ok |
| 44 | `FrozenSourcing` | `OIBridge.FrozenSourcing.nonnegBounded_of_bijectionLevel` | 348 | 348 | 348 | P3 | 348 | P3 | 348 | P3 | ok |
| 45 | `FrozenSourcing` | `OIBridge.FrozenSourcing.nonnegBounded_verdict` | 366 | 366 | 366 | P3 | 366 | P3 | 366 | P3 | ok |
| 46 | `FrozenSourcing` | `OIBridge.FrozenSourcing.nonneg_of_forall_pos` | 347 | 347 | 347 | P3 | 347 | P3 | 347 | P3 | ok |
| 47 | `FrozenSourcing` | `OIBridge.FrozenSourcing.norm_entry_le_l2_opNorm` | 345 | 345 | 345 | P3 | 345 | P3 | 345 | P3 | ok |
| 48 | `FrozenSourcing` | `OIBridge.FrozenSourcing.obsTheory_nonnegBounded` | 350 | 350 | 350 | P3 | 350 | P3 | 350 | P3 | ok |
| 49 | `FrozenSourcing` | `OIBridge.FrozenSourcing.obs_dynamics_preservesNonneg` | 361 | 361 | 361 | P3 | 361 | P3 | 361 | P3 | ok |
| 50 | `FrozenSourcing` | `OIBridge.FrozenSourcing.permMatrix_preservesNonneg` | 359 | 359 | 359 | P3 | 359 | P3 | 359 | P3 | ok |
| 51 | `FrozenSourcing` | `OIBridge.FrozenSourcing.permTheory_dense_ceiling` | 356 | 356 | 356 | P3 | 356 | P3 | 356 | P3 | ok |
| 52 | `FrozenSourcing` | `OIBridge.FrozenSourcing.permTheory_nonnegBounded` | 349 | 349 | 349 | P3 | 349 | P3 | 349 | P3 | ok |
| 53 | `FrozenSourcing` | `OIBridge.FrozenSourcing.permTheory_phase_ceiling` | 352 | 352 | 352 | P3 | 352 | P3 | 352 | P3 | ok |
| 54 | `FrozenSourcing` | `OIBridge.FrozenSourcing.phaseOperator_outside_ceiling` | 362 | 362 | 362 | P3 | 362 | P3 | 362 | P3 | ok |
| 55 | `FrozenSourcing` | `OIBridge.FrozenSourcing.phase_ceiling_rule_independent` | 364 | 364 | 364 | P3 | 364 | P3 | 364 | P3 | ok |
| 56 | `FrozenSourcing` | `OIBridge.FrozenSourcing.preservesNonneg_of_approx` | 354 | 354 | 354 | P3 | 354 | P3 | 354 | P3 | ok |
| 57 | `FrozenSourcing` | `OIBridge.FrozenSourcing.readWrite_preservesNonneg` | 360 | 360 | 360 | P3 | 360 | P3 | 360 | P3 | ok |
| 58 | `FrozenSourcing` | `OIBridge.FrozenSourcing.sourcing_rule_independent` | 363 | 363 | 363 | P3 | 363 | P3 | 363 | P3 | ok |
| 59 | `OIRealization` | `OIBridge.OIRealization.admissible_realizesSealedOICore` | 384 | 384 | 384 | P3 | 384 | P3 | 384 | P3 | ok |
| 60 | `OIRealization` | `OIBridge.OIRealization.coreIdx_apply` | 372 | 372 | 372 | P3 | 372 | P3 | 372 | P3 | ok |
| 61 | `OIRealization` | `OIBridge.OIRealization.countermodel_realizesSealedOICore` | 383 | 383 | 383 | P3 | 383 | P3 | 383 | P3 | ok |
| 62 | `OIRealization` | `OIBridge.OIRealization.finiteOI_not_implies_closure` | 393 | 393 | 393 | P3 | 393 | P3 | 393 | P3 | ok |
| 63 | `OIRealization` | `OIBridge.OIRealization.finiteOI_not_implies_inert` | 392 | 392 | 392 | P3 | 392 | P3 | 392 | P3 | ok |
| 64 | `OIRealization` | `OIBridge.OIRealization.fullQuantum_realizesSealedOICore` | 385 | 385 | 385 | P3 | 385 | P3 | 385 | P3 | ok |
| 65 | `OIRealization` | `OIBridge.OIRealization.partIdx_fst` | 386 | 386 | 386 | P3 | 386 | P3 | 386 | P3 | ok |
| 66 | `OIRealization` | `OIBridge.OIRealization.readVisible_apply` | 374 | 374 | 374 | P3 | 374 | P3 | 374 | P3 | ok |
| 67 | `OIRealization` | `OIBridge.OIRealization.readVisible_diagonal` | 378 | 378 | 378 | P3 | 378 | P3 | 378 | P3 | ok |
| 68 | `OIRealization` | `OIBridge.OIRealization.readVisible_eq_localLuders` | 375 | 375 | 375 | P3 | 375 | P3 | 375 | P3 | ok |
| 69 | `OIRealization` | `OIBridge.OIRealization.readVisible_family_eq` | 376 | 376 | 376 | P3 | 376 | P3 | 376 | P3 | ok |
| 70 | `OIRealization` | `OIBridge.OIRealization.readout_relabel_available` | 377 | 377 | 377 | P3 | 377 | P3 | 377 | P3 | ok |
| 71 | `OIRealization` | `OIBridge.OIRealization.realizedFold_diagonal` | 380 | 380 | 380 | P3 | 380 | P3 | 380 | P3 | ok |
| 72 | `OIRealization` | `OIBridge.OIRealization.realizesSealedOICore_of_control` | 382 | 382 | 382 | P3 | 382 | P3 | 382 | P3 | ok |
| 73 | `OIRealization` | `OIBridge.OIRealization.relabel_available` | 381 | 381 | 381 | P3 | 381 | P3 | 381 | P3 | ok |
| 74 | `OIRealization` | `OIBridge.OIRealization.sameCore_both` | 390 | 390 | 390 | P3 | 390 | P3 | 390 | P3 | ok |
| 75 | `OIRealization` | `OIBridge.OIRealization.sameCore_both_sides` | 391 | 391 | 391 | P3 | 391 | P3 | 391 | P3 | ok |
| 76 | `OIRealization` | `OIBridge.OIRealization.sameCore_closure_not_inert` | 388 | 388 | 388 | P3 | 388 | P3 | 388 | P3 | ok |
| 77 | `OIRealization` | `OIBridge.OIRealization.sameCore_inert_not_closure` | 389 | 389 | 389 | P3 | 389 | P3 | 389 | P3 | ok |
| 78 | `OIRealization` | `OIBridge.OIRealization.sealedCore_is_finiteOI` | 387 | 387 | 387 | P3 | 387 | P3 | 387 | P3 | ok |
| 79 | `OIRealization` | `OIBridge.OIRealization.vis_coreIdx_symm_iff` | 373 | 373 | 373 | P3 | 373 | P3 | 373 | P3 | ok |
| 80 | `OIRealization` | `OIBridge.OIRealization.vstepMap_diagonal` | 379 | 379 | 379 | P3 | 379 | P3 | 379 | P3 | ok |
| 81 | `OperationalAssembly` | `OIBridge.OperationalAssembly.blockDephase_apply` | 809 | 809 | 809 | P3 | 809 | P3 | 809 | P3 | ok |
| 82 | `OperationalAssembly` | `OIBridge.OperationalAssembly.blockDephase_classical` | 813 | 813 | 813 | P3 | 813 | P3 | 813 | P3 | ok |
| 83 | `OperationalAssembly` | `OIBridge.OperationalAssembly.blockDephase_classical_eq` | 814 | 814 | 814 | P3 | 814 | P3 | 814 | P3 | ok |
| 84 | `OperationalAssembly` | `OIBridge.OperationalAssembly.blockDephase_cp` | 811 | 811 | 811 | P3 | 811 | P3 | 811 | P3 | ok |
| 85 | `OperationalAssembly` | `OIBridge.OperationalAssembly.blockDephase_ne_localLuders` | 815 | 815 | 815 | P3 | 815 | P3 | 815 | P3 | ok |
| 86 | `OperationalAssembly` | `OIBridge.OperationalAssembly.blockDephase_not_mapSpectatorIndependent` | 816 | 816 | 816 | P3 | 816 | P3 | 816 | P3 | ok |
| 87 | `OperationalAssembly` | `OIBridge.OperationalAssembly.choiMatrix_sum` | 810 | 810 | 810 | P3 | 810 | P3 | 810 | P3 | ok |
| 88 | `OperationalAssembly` | `OIBridge.OperationalAssembly.circuit_available` | 828 | 828 | 828 | P3 | 828 | P3 | 828 | P3 | ok |
| 89 | `OperationalAssembly` | `OIBridge.OperationalAssembly.circuit_available_pureSeed` | 829 | 829 | 829 | P3 | 829 | P3 | 829 | P3 | ok |
| 90 | `OperationalAssembly` | `OIBridge.OperationalAssembly.circuit_branch` | 830 | 830 | 830 | P3 | 830 | P3 | 830 | P3 | ok |
| 91 | `OperationalAssembly` | `OIBridge.OperationalAssembly.compositeControl_hasSwapControl` | 825 | 825 | 825 | P3 | 825 | P3 | 825 | P3 | ok |
| 92 | `OperationalAssembly` | `OIBridge.OperationalAssembly.conj_ancSwap_single` | 822 | 822 | 822 | P3 | 822 | P3 | 822 | P3 | ok |
| 93 | `OperationalAssembly` | `OIBridge.OperationalAssembly.eq_of_agree_on_single` | 807 | 807 | 807 | P3 | 807 | P3 | 807 | P3 | ok |
| 94 | `OperationalAssembly` | `OIBridge.OperationalAssembly.hasFullInstruments_hasUniversalControl` | 818 | 818 | 818 | P3 | 818 | P3 | 818 | P3 | ok |
| 95 | `OperationalAssembly` | `OIBridge.OperationalAssembly.localLuders_classical` | 812 | 812 | 812 | P3 | 812 | P3 | 812 | P3 | ok |
| 96 | `OperationalAssembly` | `OIBridge.OperationalAssembly.localLuders_mapSpectatorIndependent` | 806 | 806 | 806 | P3 | 806 | P3 | 806 | P3 | ok |
| 97 | `OperationalAssembly` | `OIBridge.OperationalAssembly.localLuders_tensor` | 805 | 805 | 805 | P3 | 805 | P3 | 805 | P3 | ok |
| 98 | `OperationalAssembly` | `OIBridge.OperationalAssembly.localLuders_uniform` | 823 | 823 | 823 | P3 | 823 | P3 | 823 | P3 | ok |
| 99 | `OperationalAssembly` | `OIBridge.OperationalAssembly.mapSpectatorIndependent_iff_localLuders` | 808 | 808 | 808 | P3 | 808 | P3 | 808 | P3 | ok |
| 100 | `OperationalAssembly` | `OIBridge.OperationalAssembly.ptraceAnc_localLuders` | 820 | 820 | 820 | P3 | 820 | P3 | 820 | P3 | ok |
| 101 | `OperationalAssembly` | `OIBridge.OperationalAssembly.pureSeedPrep_available` | 826 | 826 | 826 | P3 | 826 | P3 | 826 | P3 | ok |
| 102 | `OperationalAssembly` | `OIBridge.OperationalAssembly.pureSeedPrep_available_of_swap` | 824 | 824 | 824 | P3 | 824 | P3 | 824 | P3 | ok |
| 103 | `OperationalAssembly` | `OIBridge.OperationalAssembly.pureSeedPrep_available_of_swapControl` | 827 | 827 | 827 | P3 | 827 | P3 | 827 | P3 | ok |
| 104 | `OperationalAssembly` | `OIBridge.OperationalAssembly.readout_is_localLuders` | 821 | 821 | 821 | P3 | 821 | P3 | 821 | P3 | ok |
| 105 | `OperationalAssembly` | `OIBridge.OperationalAssembly.spectatorIndependent_iff_mapLevel` | 803 | 803 | 803 | P3 | 803 | P3 | 803 | P3 | ok |
| 106 | `OperationalAssembly` | `OIBridge.OperationalAssembly.tensorOf_add_left` | 819 | 819 | 819 | P3 | 819 | P3 | 819 | P3 | ok |
| 107 | `OperationalAssembly` | `OIBridge.OperationalAssembly.tensorOf_productPreparation` | 817 | 817 | 817 | P3 | 817 | P3 | 817 | P3 | ok |
| 108 | `OperationalAssembly` | `OIBridge.OperationalAssembly.tensorOf_single` | 804 | 804 | 804 | P3 | 804 | P3 | 804 | P3 | ok |
| 109 | `PhaseSource` | `OIBridge.PhaseSource.bijectiveOperator_mulVec_ones` | 206 | 206 | 206 | P3 | 206 | P3 | 206 | P3 | ok |
| 110 | `PhaseSource` | `OIBridge.PhaseSource.conjChannel_phaseGate_ne_id` | 209 | 209 | 209 | P3 | 209 | P3 | 209 | P3 | ok |
| 111 | `PhaseSource` | `OIBridge.PhaseSource.diagonal_conj_phaseGate` | 210 | 210 | 210 | P3 | 210 | P3 | 210 | P3 | ok |
| 112 | `PhaseSource` | `OIBridge.PhaseSource.onesFixing_not_phasesAvailable` | 203 | 203 | 203 | P3 | 203 | P3 | 203 | P3 | ok |
| 113 | `PhaseSource` | `OIBridge.PhaseSource.permClass_onesFixing` | 204 | 204 | 204 | P3 | 204 | P3 | 204 | P3 | ok |
| 114 | `PhaseSource` | `OIBridge.PhaseSource.permTheory_not_phasesAvailable_onesFixing` | 205 | 205 | 205 | P3 | 205 | P3 | 205 | P3 | ok |
| 115 | `PhaseSource` | `OIBridge.PhaseSource.phaseGate_moves_ones` | 211 | 211 | 211 | P3 | 211 | P3 | 211 | P3 | ok |
| 116 | `PhaseSource` | `OIBridge.PhaseSource.phaseGate_not_scalar` | 208 | 208 | 208 | P3 | 208 | P3 | 208 | P3 | ok |
| 117 | `PhaseSource` | `OIBridge.PhaseSource.readWriteOperator_mulVec_ones` | 207 | 207 | 207 | P3 | 207 | P3 | 207 | P3 | ok |
| 118 | `PhaseSource` | `OIBridge.PhaseSource.substratumClass_not_onesFixing` | 212 | 212 | 212 | P3 | 212 | P3 | 212 | P3 | ok |
| 119 | `PhysicalC4StorageReadback` | `OIBridge.PhysicalC4StorageReadback.core_routedReadbackAtStorage_two` | 712 | 712 | 712 | P3 | 712 | P3 | 712 | P3 | ok |
| 120 | `PhysicalC4StorageReadback` | `OIBridge.PhysicalC4StorageReadback.core_statePosterior_odd` | 710 | 710 | 710 | P3 | 710 | P3 | 710 | P3 | ok |
| 121 | `PhysicalC4StorageReadback` | `OIBridge.PhysicalC4StorageReadback.core_storageReadback_and_not_routedReadback` | 717 | 717 | 717 | P3 | 717 | P3 | 717 | P3 | ok |
| 122 | `PhysicalC4StorageReadback` | `OIBridge.PhysicalC4StorageReadback.core_storage_contrast` | 711 | 711 | 711 | P3 | 711 | P3 | 711 | P3 | ok |
| 123 | `PhysicalC4StorageReadback` | `OIBridge.PhysicalC4StorageReadback.product_not_routedReadbackAtStorage` | 713 | 713 | 713 | P3 | 713 | P3 | 713 | P3 | ok |
| 124 | `PhysicalC4StorageReadback` | `OIBridge.PhysicalC4StorageReadback.rootedStatePosterior_marg_eq` | 707 | 707 | 707 | P3 | 707 | P3 | 707 | P3 | ok |
| 125 | `PhysicalC4StorageReadback` | `OIBridge.PhysicalC4StorageReadback.rootedStatePosterior_ne` | 706 | 706 | 706 | P3 | 706 | P3 | 706 | P3 | ok |
| 126 | `PhysicalC4StorageReadback` | `OIBridge.PhysicalC4StorageReadback.routedAtStorage_forces_indivisible_somewhere` | 709 | 709 | 709 | P3 | 709 | P3 | 709 | P3 | ok |
| 127 | `PhysicalC4StorageReadback` | `OIBridge.PhysicalC4StorageReadback.routedAtStorage_forces_return_indivisibility` | 708 | 708 | 708 | P3 | 708 | P3 | 708 | P3 | ok |
| 128 | `PhysicalC4StorageReadback` | `OIBridge.PhysicalC4StorageReadback.routedReadbackAtStorage_mono` | 702 | 702 | 702 | P3 | 702 | P3 | 702 | P3 | ok |
| 129 | `PhysicalC4StorageReadback` | `OIBridge.PhysicalC4StorageReadback.routedReadbackAtStorage_overlap` | 703 | 703 | 703 | P3 | 703 | P3 | 703 | P3 | ok |
| 130 | `PhysicalC4StorageReadback` | `OIBridge.PhysicalC4StorageReadback.routedReadback_not_implies_storageReadback` | 726 | 726 | 726 | P3 | 726 | P3 | 726 | P3 | ok |
| 131 | `PhysicalC4StorageReadback` | `OIBridge.PhysicalC4StorageReadback.sep_not_routedReadbackAtStorage_two` | 725 | 725 | 725 | P3 | 725 | P3 | 725 | P3 | ok |
| 132 | `PhysicalC4StorageReadback` | `OIBridge.PhysicalC4StorageReadback.sep_read_collapse` | 723 | 723 | 723 | P3 | 723 | P3 | 723 | P3 | ok |
| 133 | `PhysicalC4StorageReadback` | `OIBridge.PhysicalC4StorageReadback.sep_realization_exists` | 719 | 719 | 719 | P3 | 719 | P3 | 719 | P3 | ok |
| 134 | `PhysicalC4StorageReadback` | `OIBridge.PhysicalC4StorageReadback.sep_rootedMap` | 720 | 720 | 720 | P3 | 720 | P3 | 720 | P3 | ok |
| 135 | `PhysicalC4StorageReadback` | `OIBridge.PhysicalC4StorageReadback.sep_routedReadback_two` | 724 | 724 | 724 | P3 | 724 | P3 | 724 | P3 | ok |
| 136 | `PhysicalC4StorageReadback` | `OIBridge.PhysicalC4StorageReadback.sep_seedPosterior` | 722 | 722 | 722 | P3 | 722 | P3 | 722 | P3 | ok |
| 137 | `PhysicalC4StorageReadback` | `OIBridge.PhysicalC4StorageReadback.sep_statePosterior` | 721 | 721 | 721 | P3 | 721 | P3 | 721 | P3 | ok |
| 138 | `PhysicalC4StorageReadback` | `OIBridge.PhysicalC4StorageReadback.storageReadback_not_implies_routedReadback` | 718 | 718 | 718 | P3 | 718 | P3 | 718 | P3 | ok |
| 139 | `PhysicalC4StorageReadback` | `OIBridge.PhysicalC4StorageReadback.storageWeight_eq_zero_of_root_ne` | 705 | 705 | 705 | P3 | 705 | P3 | 705 | P3 | ok |
| 140 | `PhysicalC4StorageReadback` | `OIBridge.PhysicalC4StorageReadback.storageWeight_sum` | 704 | 704 | 704 | P3 | 704 | P3 | 704 | P3 | ok |
| 141 | `PhysicalC4StorageReadback` | `OIBridge.PhysicalC4StorageReadback.tapeLedger_not_routedReadbackAtStorage_three` | 714 | 714 | 714 | P3 | 714 | P3 | 714 | P3 | ok |
| 142 | `PhysicalC4StorageReadback` | `OIBridge.PhysicalC4StorageReadback.tapeLedger_routedReadbackAtStorage_four` | 716 | 716 | 716 | P3 | 716 | P3 | 716 | P3 | ok |
| 143 | `PhysicalC4StorageReadback` | `OIBridge.PhysicalC4StorageReadback.tapeLedger_statePosterior_one` | 715 | 715 | 715 | P3 | 715 | P3 | 715 | P3 | ok |
| 144 | `QuantumRepresentationT2` | `OIBridge.QuantumRepresentation.hadAmp_neg_normSq` | 179 | 179 | 179 | P3 | 179 | P3 | 179 | P3 | ok |
| 145 | `QuantumRepresentationT2` | `OIBridge.QuantumRepresentation.hadAmp_normSq` | 178 | 178 | 178 | P3 | 178 | P3 | 178 | P3 | ok |
| 146 | `QuantumRepresentationT2` | `OIBridge.QuantumRepresentation.hadAmp_sq` | 177 | 177 | 177 | P3 | 177 | P3 | 177 | P3 | ok |
| 147 | `QuantumRepresentationT2` | `OIBridge.QuantumRepresentation.hadData_born` | 181 | 181 | 181 | P3 | 181 | P3 | 181 | P3 | ok |
| 148 | `QuantumRepresentationT2` | `OIBridge.QuantumRepresentation.hadData_bornPow_succ` | 184 | 184 | 184 | P3 | 184 | P3 | 184 | P3 | ok |
| 149 | `QuantumRepresentationT2` | `OIBridge.QuantumRepresentation.hadData_bornPow_succ'` | 185 | 185 | 185 | P3 | 185 | P3 | 185 | P3 | ok |
| 150 | `QuantumRepresentationT2` | `OIBridge.QuantumRepresentation.hadData_bornPow_zero'` | 186 | 186 | 186 | P3 | 186 | P3 | 186 | P3 | ok |
| 151 | `QuantumRepresentationT2` | `OIBridge.QuantumRepresentation.hadData_isLaw` | 182 | 182 | 182 | P3 | 182 | P3 | 182 | P3 | ok |
| 152 | `QuantumRepresentationT2` | `OIBridge.QuantumRepresentation.hadData_positiveRootMass` | 188 | 188 | 188 | P3 | 188 | P3 | 188 | P3 | ok |
| 153 | `QuantumRepresentationT2` | `OIBridge.QuantumRepresentation.hadData_rootMass` | 187 | 187 | 187 | P3 | 187 | P3 | 187 | P3 | ok |
| 154 | `QuantumRepresentationT2` | `OIBridge.QuantumRepresentation.hadData_rooted` | 189 | 189 | 189 | P3 | 189 | P3 | 189 | P3 | ok |
| 155 | `QuantumRepresentationT2` | `OIBridge.QuantumRepresentation.hadData_rooted_eq_pdFamily` | 190 | 190 | 190 | P3 | 190 | P3 | 190 | P3 | ok |
| 156 | `QuantumRepresentationT2` | `OIBridge.QuantumRepresentation.hadU_mem_unitaryGroup` | 180 | 180 | 180 | P3 | 180 | P3 | 180 | P3 | ok |
| 157 | `QuantumRepresentationT2` | `OIBridge.QuantumRepresentation.hadU_normSq` | 183 | 183 | 183 | P3 | 183 | P3 | 183 | P3 | ok |
| 158 | `QuantumRepresentationT2` | `OIBridge.QuantumRepresentation.qStar_not_subset_finiteRootedRealizable` | 192 | 192 | 192 | P3 | 192 | P3 | 192 | P3 | ok |
| 159 | `QuantumRepresentationT2` | `OIBridge.QuantumRepresentation.qStar_not_subset_pper` | 193 | 193 | 193 | P3 | 193 | P3 | 193 | P3 | ok |
| 160 | `QuantumRepresentationT2` | `OIBridge.QuantumRepresentation.qStar_pdFamily` | 191 | 191 | 191 | P3 | 191 | P3 | 191 | P3 | ok |
| 161 | `ReadWriteControl` | `OIBridge.ReadWriteControl.memorySwap_nontrivial` | 228 | 228 | 228 | P3 | 228 | P3 | 228 | P3 | ok |
| 162 | `ReadWriteControl` | `OIBridge.ReadWriteControl.memorySwap_operator_monomial` | 229 | 229 | 229 | P3 | 229 | P3 | 229 | P3 | ok |
| 163 | `ReadWriteControl` | `OIBridge.ReadWriteControl.offDiagonal_interp_not_monomial` | 224 | 224 | 224 | P3 | 224 | P3 | 224 | P3 | ok |
| 164 | `ReadWriteControl` | `OIBridge.ReadWriteControl.readWriteControl_independent` | 230 | 230 | 230 | P3 | 230 | P3 | 230 | P3 | ok |
| 165 | `ReadWriteControl` | `OIBridge.ReadWriteControl.readWriteOperator_eq_perm` | 222 | 222 | 222 | P3 | 222 | P3 | 222 | P3 | ok |
| 166 | `ReadWriteControl` | `OIBridge.ReadWriteControl.readWriteOperator_monomial` | 223 | 223 | 223 | P3 | 223 | P3 | 223 | P3 | ok |
| 167 | `ReadWriteControl` | `OIBridge.ReadWriteControl.readWriteSourced_monomialSource` | 225 | 225 | 225 | P3 | 225 | P3 | 225 | P3 | ok |
| 168 | `ReadWriteControl` | `OIBridge.ReadWriteControl.readWriteSourced_not_control` | 226 | 226 | 226 | P3 | 226 | P3 | 226 | P3 | ok |
| 169 | `ReadWriteControl` | `OIBridge.ReadWriteControl.readWriteSourced_not_qm` | 227 | 227 | 227 | P3 | 227 | P3 | 227 | P3 | ok |
| 170 | `RootedClassification` | `OIBridge.RootedClassification.cyclePerm_apply` | 358 | 358 | 358 | P3 | 358 | P3 | 358 | P3 | ok |
| 171 | `RootedClassification` | `OIBridge.RootedClassification.cycleState_injective` | 357 | 357 | 357 | P3 | 357 | P3 | 357 | P3 | ok |
| 172 | `RootedClassification` | `OIBridge.RootedClassification.cycleState_nonzero` | 356 | 356 | 356 | P3 | 356 | P3 | 356 | P3 | ok |
| 173 | `RootedClassification` | `OIBridge.RootedClassification.cycleState_val_zero` | 355 | 355 | 355 | P3 | 355 | P3 | 355 | P3 | ok |
| 174 | `RootedClassification` | `OIBridge.RootedClassification.pper_of_finiteRootedRealizable` | 364 | 364 | 364 | P3 | 364 | P3 | 364 | P3 | ok |
| 175 | `RootedClassification` | `OIBridge.RootedClassification.responsePrior_nonneg` | 362 | 362 | 362 | P3 | 362 | P3 | 362 | P3 | ok |
| 176 | `RootedClassification` | `OIBridge.RootedClassification.responsePrior_sum` | 363 | 363 | 363 | P3 | 363 | P3 | 363 | P3 | ok |
| 177 | `RootedClassification` | `OIBridge.RootedClassification.responseStep_cycle` | 359 | 359 | 359 | P3 | 359 | P3 | 359 | P3 | ok |
| 178 | `RootedClassification` | `OIBridge.RootedClassification.responseWeight_marginal` | 351 | 351 | 351 | P3 | 351 | P3 | 351 | P3 | ok |
| 179 | `RootedClassification` | `OIBridge.RootedClassification.responseWeight_nonneg` | 349 | 349 | 349 | P3 | 349 | P3 | 349 | P3 | ok |
| 180 | `RootedClassification` | `OIBridge.RootedClassification.responseWeight_sum` | 350 | 350 | 350 | P3 | 350 | P3 | 350 | P3 | ok |
| 181 | `RootedClassification` | `OIBridge.RootedClassification.rootedMap_mem_PPer` | 354 | 354 | 354 | P3 | 354 | P3 | 354 | P3 | ok |
| 182 | `RootedClassification` | `OIBridge.RootedClassification.rootedMap_periodic` | 353 | 353 | 353 | P3 | 353 | P3 | 353 | P3 | ok |
| 183 | `RootedClassification` | `OIBridge.RootedClassification.rootedMap_zero` | 352 | 352 | 352 | P3 | 352 | P3 | 352 | P3 | ok |
| 184 | `RootedClassification` | `OIBridge.RootedClassification.tableWeight_nonneg` | 360 | 360 | 360 | P3 | 360 | P3 | 360 | P3 | ok |
| 185 | `RootedClassification` | `OIBridge.RootedClassification.tableWeight_sum` | 361 | 361 | 361 | P3 | 361 | P3 | 361 | P3 | ok |
| 186 | `RootedClassificationAllTime` | `OIBridge.RootedClassification.cyclePerm_iterate_phaseZero_period` | 253 | 253 | 253 | P3 | 253 | P3 | 253 | P3 | ok |
| 187 | `RootedClassificationAllTime` | `OIBridge.RootedClassification.finRotate_iterate_phaseZero_period` | 252 | 252 | 252 | P3 | 252 | P3 | 252 | P3 | ok |
| 188 | `RootedClassificationAllTime` | `OIBridge.RootedClassification.finiteRootedRealizable_iff_pper` | 262 | 262 | 262 | P3 | 262 | P3 | 262 | P3 | ok |
| 189 | `RootedClassificationAllTime` | `OIBridge.RootedClassification.finiteRootedRealizable_of_realization` | 263 | 263 | 263 | P3 | 263 | P3 | 263 | P3 | ok |
| 190 | `RootedClassificationAllTime` | `OIBridge.RootedClassification.pdFamily_not_finiteRootedRealizable` | 266 | 266 | 266 | P3 | 266 | P3 | 266 | P3 | ok |
| 191 | `RootedClassificationAllTime` | `OIBridge.RootedClassification.pdFamily_not_periodicFamily` | 264 | 264 | 264 | P3 | 264 | P3 | 264 | P3 | ok |
| 192 | `RootedClassificationAllTime` | `OIBridge.RootedClassification.peFamily_not_finiteRootedRealizable` | 267 | 267 | 267 | P3 | 267 | P3 | 267 | P3 | ok |
| 193 | `RootedClassificationAllTime` | `OIBridge.RootedClassification.peFamily_not_periodicFamily` | 265 | 265 | 265 | P3 | 265 | P3 | 265 | P3 | ok |
| 194 | `RootedClassificationAllTime` | `OIBridge.RootedClassification.pper_has_responseRealization` | 261 | 261 | 261 | P3 | 261 | P3 | 261 | P3 | ok |
| 195 | `RootedClassificationAllTime` | `OIBridge.RootedClassification.responseLocalWeight_sum` | 255 | 255 | 255 | P3 | 255 | P3 | 255 | P3 | ok |
| 196 | `RootedClassificationAllTime` | `OIBridge.RootedClassification.responseRealization_agrees_all` | 260 | 260 | 260 | P3 | 260 | P3 | 260 | P3 | ok |
| 197 | `RootedClassificationAllTime` | `OIBridge.RootedClassification.responseRealization_pad_sum` | 256 | 256 | 256 | P3 | 256 | P3 | 256 | P3 | ok |
| 198 | `RootedClassificationAllTime` | `OIBridge.RootedClassification.responseStep_iterate_phaseZero_period` | 254 | 254 | 254 | P3 | 254 | P3 | 254 | P3 | ok |
| 199 | `RootedClassificationAllTime` | `OIBridge.RootedClassification.rootedMap_responseRealization_add_period` | 259 | 259 | 259 | P3 | 259 | P3 | 259 | P3 | ok |
| 200 | `RootedClassificationAllTime` | `OIBridge.RootedClassification.rootedMap_responseRealization_first_period` | 258 | 258 | 258 | P3 | 258 | P3 | 258 | P3 | ok |
| 201 | `RootedClassificationAllTime` | `OIBridge.RootedClassification.rootedMap_responseRealization_of_pos_lt` | 257 | 257 | 257 | P3 | 257 | P3 | 257 | P3 | ok |
| 202 | `StructuralClosure` | `OIBridge.StructuralClosure.bijectiveOperator_conjTranspose` | 452 | 452 | 452 | P3 | 452 | P3 | 452 | P3 | ok |
| 203 | `StructuralClosure` | `OIBridge.StructuralClosure.bijectiveOperator_supplied` | 455 | 455 | 455 | P3 | 455 | P3 | 455 | P3 | ok |
| 204 | `StructuralClosure` | `OIBridge.StructuralClosure.fullClass_extendsSubstratum` | 466 | 466 | 466 | P3 | 466 | P3 | 466 | P3 | ok |
| 205 | `StructuralClosure` | `OIBridge.StructuralClosure.monomial_iff_submonomial` | 437 | 437 | 437 | P3 | 437 | P3 | 437 | P3 | ok |
| 206 | `StructuralClosure` | `OIBridge.StructuralClosure.monomial_submonomial` | 435 | 435 | 435 | P3 | 435 | P3 | 435 | P3 | ok |
| 207 | `StructuralClosure` | `OIBridge.StructuralClosure.mul_entry_ne_zero` | 434 | 434 | 434 | P3 | 434 | P3 | 434 | P3 | ok |
| 208 | `StructuralClosure` | `OIBridge.StructuralClosure.of_ite_ne_zero` | 433 | 433 | 433 | P3 | 433 | P3 | 433 | P3 | ok |
| 209 | `StructuralClosure` | `OIBridge.StructuralClosure.phaseOperator_conjTranspose` | 453 | 453 | 453 | P3 | 453 | P3 | 453 | P3 | ok |
| 210 | `StructuralClosure` | `OIBridge.StructuralClosure.phaseOperator_supplied` | 456 | 456 | 456 | P3 | 456 | P3 | 456 | P3 | ok |
| 211 | `StructuralClosure` | `OIBridge.StructuralClosure.qm_generated_by_substratum_extension` | 467 | 467 | 467 | P3 | 467 | P3 | 467 | P3 | ok |
| 212 | `StructuralClosure` | `OIBridge.StructuralClosure.quantumArchitecture_iff_drives_of_closed` | 460 | 460 | 460 | P3 | 460 | P3 | 460 | P3 | ok |
| 213 | `StructuralClosure` | `OIBridge.StructuralClosure.readWriteOperator_supplied` | 457 | 457 | 457 | P3 | 457 | P3 | 457 | P3 | ok |
| 214 | `StructuralClosure` | `OIBridge.StructuralClosure.submonomial_block` | 442 | 442 | 442 | P3 | 442 | P3 | 442 | P3 | ok |
| 215 | `StructuralClosure` | `OIBridge.StructuralClosure.submonomial_conjTranspose` | 449 | 449 | 449 | P3 | 449 | P3 | 449 | P3 | ok |
| 216 | `StructuralClosure` | `OIBridge.StructuralClosure.submonomial_diagonal` | 441 | 441 | 441 | P3 | 441 | P3 | 441 | P3 | ok |
| 217 | `StructuralClosure` | `OIBridge.StructuralClosure.submonomial_monomial` | 436 | 436 | 436 | P3 | 436 | P3 | 436 | P3 | ok |
| 218 | `StructuralClosure` | `OIBridge.StructuralClosure.submonomial_mul` | 439 | 439 | 439 | P3 | 439 | P3 | 439 | P3 | ok |
| 219 | `StructuralClosure` | `OIBridge.StructuralClosure.submonomial_one` | 438 | 438 | 438 | P3 | 438 | P3 | 438 | P3 | ok |
| 220 | `StructuralClosure` | `OIBridge.StructuralClosure.submonomial_reindex` | 447 | 447 | 447 | P3 | 447 | P3 | 447 | P3 | ok |
| 221 | `StructuralClosure` | `OIBridge.StructuralClosure.submonomial_smul` | 440 | 440 | 440 | P3 | 440 | P3 | 440 | P3 | ok |
| 222 | `StructuralClosure` | `OIBridge.StructuralClosure.submonomial_tensor_one` | 445 | 445 | 445 | P3 | 445 | P3 | 445 | P3 | ok |
| 223 | `StructuralClosure` | `OIBridge.StructuralClosure.substratumClass_arch` | 443 | 443 | 443 | P3 | 443 | P3 | 443 | P3 | ok |
| 224 | `StructuralClosure` | `OIBridge.StructuralClosure.substratumClass_contextStable` | 446 | 446 | 446 | P3 | 446 | P3 | 446 | P3 | ok |
| 225 | `StructuralClosure` | `OIBridge.StructuralClosure.substratumClass_daggerStable` | 450 | 450 | 450 | P3 | 450 | P3 | 450 | P3 | ok |
| 226 | `StructuralClosure` | `OIBridge.StructuralClosure.substratumClass_labelInvariant` | 448 | 448 | 448 | P3 | 448 | P3 | 448 | P3 | ok |
| 227 | `StructuralClosure` | `OIBridge.StructuralClosure.substratumClass_not_drivesElementary` | 461 | 461 | 461 | P3 | 461 | P3 | 461 | P3 | ok |
| 228 | `StructuralClosure` | `OIBridge.StructuralClosure.substratumClass_not_quantumArchitecture` | 462 | 462 | 462 | P3 | 462 | P3 | 462 | P3 | ok |
| 229 | `StructuralClosure` | `OIBridge.StructuralClosure.substratumClass_structurallyClosed` | 454 | 454 | 454 | P3 | 454 | P3 | 454 | P3 | ok |
| 230 | `StructuralClosure` | `OIBridge.StructuralClosure.substratumClass_unitaryRaySaturated` | 451 | 451 | 451 | P3 | 451 | P3 | 451 | P3 | ok |
| 231 | `StructuralClosure` | `OIBridge.StructuralClosure.substratumGen_not_control` | 458 | 458 | 458 | P3 | 458 | P3 | 458 | P3 | ok |
| 232 | `StructuralClosure` | `OIBridge.StructuralClosure.substratumGen_not_qm` | 459 | 459 | 459 | P3 | 459 | P3 | 459 | P3 | ok |
| 233 | `StructuralClosure` | `OIBridge.StructuralClosure.substratum_extension_quantum_iff_drives` | 464 | 464 | 464 | P3 | 464 | P3 | 464 | P3 | ok |
| 234 | `StructuralClosure` | `OIBridge.StructuralClosure.substratum_plus_control_qm` | 465 | 465 | 465 | P3 | 465 | P3 | 465 | P3 | ok |
| 235 | `StructuralClosure` | `OIBridge.StructuralClosure.substratum_residual` | 463 | 463 | 463 | P3 | 463 | P3 | 463 | P3 | ok |
| 236 | `StructuralClosure` | `OIBridge.StructuralClosure.tensor_one_entry_ne_zero` | 444 | 444 | 444 | P3 | 444 | P3 | 444 | P3 | ok |
| 237 | `SubstratumInterface` | `OIBridge.SubstratumInterface.bijectiveOperator_monomial` | 210 | 210 | 210 | P3 | 210 | P3 | 210 | P3 | ok |
| 238 | `SubstratumInterface` | `OIBridge.SubstratumInterface.elementary_split` | 219 | 219 | 219 | P3 | 219 | P3 | 219 | P3 | ok |
| 239 | `SubstratumInterface` | `OIBridge.SubstratumInterface.exchange_monomial` | 212 | 212 | 212 | P3 | 212 | P3 | 212 | P3 | ok |
| 240 | `SubstratumInterface` | `OIBridge.SubstratumInterface.monomialSource_not_control` | 217 | 217 | 217 | P3 | 217 | P3 | 217 | P3 | ok |
| 241 | `SubstratumInterface` | `OIBridge.SubstratumInterface.monomialSource_not_qm` | 218 | 218 | 218 | P3 | 218 | P3 | 218 | P3 | ok |
| 242 | `SubstratumInterface` | `OIBridge.SubstratumInterface.monomial_diagonal` | 209 | 209 | 209 | P3 | 209 | P3 | 209 | P3 | ok |
| 243 | `SubstratumInterface` | `OIBridge.SubstratumInterface.monomial_entry` | 214 | 214 | 214 | P3 | 214 | P3 | 214 | P3 | ok |
| 244 | `SubstratumInterface` | `OIBridge.SubstratumInterface.monomial_permMatrix` | 208 | 208 | 208 | P3 | 208 | P3 | 208 | P3 | ok |
| 245 | `SubstratumInterface` | `OIBridge.SubstratumInterface.phaseOperator_monomial` | 211 | 211 | 211 | P3 | 211 | P3 | 211 | P3 | ok |
| 246 | `SubstratumInterface` | `OIBridge.SubstratumInterface.phase_monomial` | 213 | 213 | 213 | P3 | 213 | P3 | 213 | P3 | ok |
| 247 | `SubstratumInterface` | `OIBridge.SubstratumInterface.preservesDiag_conj_of_monomial` | 215 | 215 | 215 | P3 | 215 | P3 | 215 | P3 | ok |
| 248 | `SubstratumInterface` | `OIBridge.SubstratumInterface.rot_not_monomial` | 216 | 216 | 216 | P3 | 216 | P3 | 216 | P3 | ok |
