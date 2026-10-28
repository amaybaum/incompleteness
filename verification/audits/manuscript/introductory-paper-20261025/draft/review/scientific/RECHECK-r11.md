# Re-check of Introduction r11 and of `papers/introduction_repro/`

**Scope.** This is an independent, read-only review. Outputs are in scratch only; no repository file was changed and no Lean build was run (§A.40).

**Commits:**
- Branch `draft/oi-introductory-paper-20261025` at `b2d8cbd2`.
- Evidence package at `ed3ca911`.
- `origin/main` = `17b830bc`, confirmed with `ls-remote`.

**Rules applied:** §A.42 (reduced form) and §A.44, both read at `origin/main`.

***

## A. Introduction r11

### A.1 Reproduction and diff

- **Script output.** `python3 -I build_r11.py Introduction-r10.md out.md` reports "applied 9 edits". `cmp` with `Introduction-r11.md` shows the files are **byte-identical** (sha256 `a25e973c…d1f7`, which matches `SHA256SUMS`).
- **Diff.** `diff r10 r11` has 7 hunks, which hold exactly the 9 edits:
  1. T3 reverted;
  2. "only once" → "only after";
  3. the landing-gate sentence added to the Weinberg marker;
  4. the Conventions commit changed to `17b830bc`;
  5. the OWNER decision-2 marker removed;
  6. the OWNER retention marker removed;
  7. the Code-section sentence replaced;
  8. the Appendix A commit changed;
  9. the Corpus commit changed.

  Items 2 and 3 share one hunk, and items 6 and 7 share one hunk. Nothing else changed: 6 lines are added.
- **r10 unchanged.** r10 is unchanged (`b87ef6f9…9830`).
- **RECHECK-r10 retention.** The retained `review/scientific/RECHECK-r10.md` is byte-identical to the report I wrote.

### A.2 Nits of RECHECK-r10

All four are addressed:
1. **T3 is reverted.** The text reads "[Main §3.4, Theorem (finite-horizon stochastic–reversible–unitary equivalence); EGGH26, Prop. 13]".
2. **The T4 reversal of REVIEW.md:173 / F10 is recorded** in CHANGES-r11, together with the reason the theorem stays findable (GR:216 and GR:218).
3. **The Weinberg marker** now reads "only after the source is read and checked", and it gates landing (see A.3).
4. **Status records.**
   - `draft/README.md` gains an r10/r11 section. It records that title hyphenation is resolved, that there are four VERIFY markers, that Weinberg is an open landing gate, and that there are no OWNER markers.
   - CHANGES-r10's Method path is corrected to `draft/scripts/build_r10.py`. CHANGES-r10 is a mutable draft record, not frozen.

### A.3 Weinberg landing gate

- **Marker text (r11:140).** It reads: "VERIFY: Landing gate (owner, 2026-10-26): the paper does not land until this source is read first-hand and checked. Weinberg 1989 … is not read first-hand and is not treated as verified … No claim in the next sentence is attributed to Weinberg; it is cited for that sentence only after the source is read and checked."
- **README.** It lists the gate first under "Before the draft lands".
- **The guarded sentence** is unchanged and cites nothing.
- **PASS.**

### A.4 Corpus pointers at `17b830bc`

**Unchanged files.** `git diff --stat 687e885b 17b830bc` over `papers/ book/ verification/programmes/black-hole-information/ verification/lean verification/lean-mathlib` lists only:
- `papers/GR.*`;
- book files: FULL, ch07, ch09, ch18, ch19, appendix-a, glossary, bibliography, README.

So `papers/Main.md`, book ch01, the BH programme and both Lean trees are unchanged. The tree ids at the two commits are equal: `277d2822…` and `8624ba39…`.

**Main pointers.** I checked them independently at `17b830bc`. All ten cited sections exist (§1.2, §1.3, §1.5, §2.3, §2.4, §3.1–§3.4 and §4.5). Each of the 15 named Theorem, Remark and Proposition labels, and the "realization clause of (C4)", occurs inside its cited section.

**GR pointers.**

| Pointer | Location at `17b830bc` |
|---|---|
| §2.2 | GR:44, with (C4) at GR:52 |
| §3.3 | GR:168, with Theorem (operational-completion characterization) at GR:218 |
| §6.2 | GR:342, with the two completions at GR:356 |
| App. A | GR:715 |
| A.1 | GR:719 |
| A.6 | GR:793 |
| A.7 | GR:807 |
| Theorem A.7 | GR:813 |
| Theorem A.8 | GR:819 |
| Theorem A.9 | GR:847 |

**Book pointers.** §1.11 is at ch01:265, §7.6 at ch07:108 and §18.5 at ch18:128.

**No `687e885b` remains in r11.** **PASS.**

### A.5 The Code-section sentence against the evidence

| Claim in r11 | Evidence | Status |
|---|---|---|
| "Lean 4.33.0" | `lean-toolchain` = `leanprover/lean4:v4.33.0`. The job log, line 630, reads `Lean (version 4.33.0, …, commit d8b18978…)` | ✓ |
| "Mathlib v4.33.0" | `lakefile.toml` has `rev = "v4.33.0"`. `git ls-remote` of mathlib4 shows that `refs/tags/v4.33.0` = `db584cd6…`, which is the revision the job checked out (log line 633) | ✓ |
| "at commit 17b830bc…" | The job and run records (API) give `head_sha` = `17b830bc…`, and `17b830bc` is `main` | ✓ |
| The recipe: `lake exe cache get`, `lake --rehash build`, `python3 tools/release_gate.py` | `verify.yml` at `17b830bc`, job "Mathlib bridge", steps Build and Release gate. Step conclusions from the jobs API: Build `success`, Release gate `success` | ✓ |
| "`lean-axioms` step requires every `#print axioms` report to lie within" the three | `release_gate.py:148` runs `lean_axiom_check.py --require-lake`, whose rules 1–4 fail on `sorryAx`, a nonzero lake exit, an axiom outside the three, or a missing report | ✓ |
| "Each declaration in Appendix A reports exactly these three" | 28 of 28 are verified against the job log itself (see B) | ✓ |
| "expected result and comparison recipe are in `papers/introduction_repro/`" | True on the branch (`ed3ca911`). It is not on `main` yet: see B, finding 6 | ✓, conditional on landing |

**Build-cache replay.** The sentence says the check was done "by building the Lean project". In the cited job, all 226 `OIBridge` modules were *Replayed* from an exact-key Actions cache: there are 226 "Replayed OIBridge" lines and 0 "Built OIBridge" lines in log lines 1–38918. The reports are therefore those logged by an earlier elaboration of byte-identical sources under the same toolchain and dependency set. `--rehash` re-hashes the sources against the restored traces.

The paper's sentence describes the recipe, not the job, and the recipe run without a cache does elaborate. I read this as not an overclaim; the package README states the replay openly. No change is required.

### A.6 Build

The paper was built with `pandoc r11.md -s --pdf-engine=xelatex --include-in-header=tools/unicode-fix.tex`, plus two xelatex passes to obtain the log.

- **Pages and boxes.** 17 pp, **0 overfull boxes, 0 missing characters** (2 underfull).
- **Title.** Three lines, with no hyphen.
- **Main text.** §6.4 ends at p.12, line 40, and "Code, data and formal verification" starts at **p.13, line 1**. The main text is ≤ 12 pp and unchanged from r10.

### A.7 Register

- The 6 added lines have 0 §A.32/§A.33 phrase hits.
- Prose outside comments and code spans has no ALL-CAPS words. VERIFY and FINDINGS occur only in the comment.
- `tools/voice_check.py` reports OK on r11 and on the added lines.

### Findings (A)

1. **(Owner record) Authorization for the two marker removals and the Code-section rewrite.** CHANGES-r11 does not record an owner decision for these two things:
   - The removed decision-2 marker said "the owner chooses the word ('machine-checked' or 'checked in Lean 4/Mathlib at commit X by recipe Y')". The retention half of that marker is met; the choice-of-word half is closed without a recorded owner decision.
   - CHANGES-r10 records the owner's 2026-10-26 instruction that the Code section be "left as it is", and r11 rewrites it.

   If the owner authorized either, quote the authorization (author and time, §A.42 item 7) in CHANGES-r11. Otherwise put the question to the owner.
2. **(Nit) Landing list.** `draft/README.md`'s "Before the draft lands" should also list that `papers/introduction_repro/` reaches `main` no later than the paper (§A.42 item 2). The Code sentence and the Conventions rest on it.
3. **(Cosmetic) Line break in a command.** In the PDF the code span breaks as "lake / --rehash build" across lines 3–4 of the Code section. This is optional to fix.

**Verdict A: ACCEPT WITH NITS.** Finding 1 is a record and owner item, not a text defect.

***

## B. `papers/introduction_repro/` (`ed3ca911`)

### Against the source

**Job and run records (API).**
- Job `121598983127`, "Mathlib bridge": `success`, `head_sha` `17b830bc…`, run `40330683786`, attempt 1, branch `main`.
- Step conclusions: Build `success`, Release gate `success`. The later KTOKEN, PRESERVE and KTRANS steps are `success`, and the KTRANS marker step is `skipped`.
- Run `40330683786`: workflow `verify` (`.github/workflows/verify.yml`), event `push`, conclusion `success`.
- The other Lean job, `121598983232` "Lean kernel check", is `success`. Its log shows `Lean (version 4.35.0, … eb6cafb7…)`, as the README states.

**Log.** Fetched with `gh api …/actions/jobs/121598983127/logs`.

| Item | Result |
|---|---|
| Lines and digest | 43064 lines, sha256 `bc2291bc…0c81` ✓ |
| Lines 1–38918 | sha256 `1a83921f…e09df` = `source.served_sha256` ✓. Line 38918 is the gate verdict line ✓ |
| Toolchain | log:630 `Lean (version 4.33.0, x86_64-unknown-linux-gnu, commit d8b18978…, Release)` ✓ |
| Mathlib | log:633 `mathlib: checking out revision 'db584cd6…'` ✓. All 8 dependency revisions in the README match log:636–650 ✓ |
| Build | log:38886 `Build completed successfully (3656 jobs).` ✓ |
| Gate | log:38893–38918: 22 PASS steps, summaries identical to `expected.gate.steps`, verdict `release gate: PASS  (note: --label bNNN …)` ✓. `lean-axioms` reads "6082 named result(s)" ✓ |
| Markers in lines 1–38918 | `sorryAx` 0, `Lean.ofReduceBool` 0, `declaration uses 'sorry'` 0, `error:` 0 ✓ |
| Replay | 226 "Replayed OIBridge", 0 "Built OIBridge"; cache restored from the exact key (log:607) ✓ |

**Five random declarations** (seed 20261026), from the log:

| Declaration | Log line | Report | Axioms |
|---|---|---|---|
| `Qfb_imp_S` | 769 | Equivalence:474 | [propext, Classical.choice, Quot.sound] |
| `exactAll_of_levelOne` | 2442 | LevelOneSeam:407 | same |
| `capacity_floor` | 764 | HiddenMemory:201 | same |
| `exactAll_of_physical_general` | 2864 | GeneralCarrier:220 | same |
| `permMatrix_mem_unitaryGroup` | 747 | EquivalenceChain:392 | same |

I went beyond the spot check:
- **All 286 reports.** Every report in `expected.modules` (14 modules) matches the log by line, name and axiom list, with multi-line reports joined. Each module's report count equals the number of its log reports. Each module's `prints` count and report lines equal the `#print axioms` lines of its source at `17b830bc`. The only non-standard report is `PhysicalCharacterization.levelOne_eq` with `[propext]`, which is not cited, as the README states.

### The 28 Appendix A declarations

- **Axioms.** Each has exactly one report, and each is exactly `[propext, Classical.choice, Quot.sound]`, both in the JSON and in the log.
- **Lines.** Each README "decl." line holds `theorem <name>` at `17b830bc`, and each "print" line holds `#print axioms <name>`. This is 28 of 28.

### Commit reachable

These are all ancestors of `origin/main`: `17b830bc` (the head), `687e885b`, `48b18ac5`, `5c4e5087` and `df9e601e`.

The cited objects resolve:
- blob `e6f69713…` = `48b18ac5:…/extract_result.py`;
- tree `c8b7e886…` = `48b18ac5:verification/audits/evidence-retention`.

`ed3ca911` itself is not on `main` yet; see finding 6.

### Recipe

- **Tools exist.** `extract_result.py` and `compare_result.py` exist at `48b18ac5`. The CLI forms in the recipe match their `__main__` blocks: `extract_result.py <log>` writes JSON to stdout, and `compare_result.py <expected> <reproduced> --tree <dir>` reads `verification/lean-mathlib/<mod>` under `<dir>`.
- **Workflow match.** The build and gate commands match `verify.yml` at `17b830bc`.
- **Cheap independent run (no Lean build).**
  - `extract_result.py` on log lines 1–38918, then `compare_result.py <json> … --tree <git archive of 17b830bc>`, gives **REPRODUCTION HOLDS (0 failures)**.
  - The same holds on a simulated *local* log, with timestamps and `##[group]` lines stripped. So the extractor does not depend on CI log decoration, and the recipe's local log is parseable.
  - `compare_result.py --self-test <json>` gives OK.
- **Path error.** The README's last step is run "from the root of a full-history clone" but names the expected file as bare `results-121598983127.json`, which does not exist at the root. See finding 1.
- **Gate summaries.** I checked the gate tools at `17b830bc` for environment dependence: there are no mtime reads, and the only environment values read are `PATH` and `LAKE`. The comparison of summaries is therefore not environment-sensitive. The full recipe was not run.

### Sensitive data

A scan of `README.md` and the JSON for tokens (`gh*_`, `github_pat_`, AWS keys, PEM headers), signed-URL parameters, `AUTHORIZATION`/`Bearer`, IPv4 addresses, e-mail addresses, and runner or home paths found nothing. The only hits are the README's own description of masked values (`token: ***`). No raw log is committed.

### §A.42 items 1–6 (reduced form, `origin/main`)

1. **What a claim rests on.**
   - The commit `17b830bc` is reachable.
   - The command is the README's "Reproducing it" and the JSON's `reproduce.recipe`.
   - The result to expect is a small structured file beside the paper.
   - Only deterministic outputs are expected; timestamps, cache and job counts are under `observed` and not compared.
   - ✓
2. **Provenance.** The run and job ids and the log digest are labelled provenance (`source.note`); the claim rests on regeneration. Content the claim needs from `ed3ca911` must reach `main` no later than the paper (finding 6). ✓
3. **Identifiers.** Every full id of *this* repository resolves and is reachable from `main`. The upstream ids (Lean `d8b18978` and `eb6cafb7`, Mathlib `db584cd6` and 8 dependency revisions) are not objects of this repository. They are labelled as upstream, and the Mathlib tag was verified. See finding 5.
4. **Exact bytes.** No raw log is committed, and the scan is clean. However, the package makes exact-byte claims about an off-`main` artifact: the log's sha256, its 43064 lines, its lines 1–38918, `observed.report_served_lines` (286 line positions), `cache.served_line` and `gate_served_lines`. See finding 3.
5. **Necessity.**
   - The 286 reports of 14 modules exceed the 28 cited. That is justified, because the comparator checks whole modules (every `#print axioms` line, fail-closed).
   - `observed`'s line positions serve no claim and are not compared. See finding 3.
6. **Forward only.** `ed3ca911` only adds two new files under `papers/`. No frozen record is touched, and `legacy-records.json` names nothing under `papers/introduction_repro`. ✓

**§A.44.**
- **Structured records.** Build success and the gate verdict are also carried by the jobs API step conclusions, which are structured.
- **Log-only facts.** The per-declaration axiom sets exist only in printed output. They enter as an expected result that the fail-closed comparator regenerates.
- **Served-log caveat.** The log was read whole: 43064 lines, with a matching digest, which I confirmed by refetching. The caveat about a partially served log therefore does not bite.

### Findings (B)

1. **(Fix) The recipe path is wrong as written.**
   - The README says to run from the repository root, but its last line passes `results-121598983127.json`. It should pass `papers/introduction_repro/results-121598983127.json`, from a checkout that contains the package, which will be `main` after landing.
   - The JSON's recipe uses the placeholder `<this results.json>` and is fine.
2. **(Fix) The build-cache statement overclaims.** "Reproduction by the recipe below uses no build cache, so it elaborates every module afresh" is not accurate:
   - `lake exe cache get` installs Mathlib's prebuilt oleans, so only the 226 `OIBridge` modules are elaborated afresh.
   - Reword along these lines: "uses no Actions build cache, so every `OIBridge` module is elaborated afresh; Mathlib's prebuilt oleans are fetched by `lake exe cache get`, as in the job".
   - The other replay statements are accurate: the replay itself, the 226 count, and what `--rehash` does.
3. **(Nit / owner) Item 4 and exact bytes of the off-`main` log.**
   - `source.served_sha256`, `served_lines` and `original_lines` are required by the archive schema (`check_retention.py` R4 at `48b18ac5`:916). They read as naming provenance by digest, which item 2 permits.
   - `observed.report_served_lines`, `cache.served_line` and `gate_served_lines` are line-position claims about a log that is not on `main`. They serve no claim and are not compared.
   - Either drop them, or have the owner accept them explicitly as provenance under item 2. The README's "lines 1–38918" sentence falls under the same point.
4. **(Nit) Prerequisites are unstated.** The recipe assumes:
   - elan on `PATH`, which installs `leanprover/lean4:v4.33.0` from `lean-toolchain`;
   - network access for the Mathlib clone and `lake exe cache get`;
   - `python3`.

   State them in one line.
5. **(Observation) Item 3 and upstream ids.** The upstream commit ids are not objects of this repository. They are clearly labelled, and the Mathlib tag is verified with `ls-remote`. The owner may wish to confirm that item 3 is read as covering ids of this repository only.
6. **(Landing order) `ed3ca911` is not on `main`.** The package must land on `main` no later than the paper that cites it (§A.42 items 1–2), for example in the same pull request or before it.

**Verdict B: ACCEPT WITH NITS.**
- Findings 1 and 2 are small text fixes to the README and should be made before landing.
- Finding 6 is a landing-order condition.
- Findings 3–5 are nits and owner questions.
- The data itself is verified complete and exact against the source: 286 of 286 reports, 22 of 22 gate steps, the markers, the toolchain and the Mathlib revision.
