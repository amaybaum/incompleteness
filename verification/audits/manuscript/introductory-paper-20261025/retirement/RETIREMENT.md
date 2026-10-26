# Explainer retirement plan

Planning document. No repository file is changed and nothing is committed. All `path:line`
references are at `main` `687e885b1cfd24d6f17eee439101afc8acf07015`. Dependents were found with
`git -c gc.auto=0 -c maintenance.auto=false grep -n -i explainer 687e885b`: 57 files.
The companion content audit is `MIGRATION.md` in this directory.

**Owner policy, restated as gates.**
- This is a controlled replacement, not a deletion.
- The Explainer's content and history are preserved.
- No redundant material is carried forward.
- Index, link and documentation changes happen only after the Introduction passes independent
  scientific and editorial review.
- The Introduction inherits no unsupported claim (MIGRATION §2 class (d)).

***

## 1. Preconditions (all must hold before the retirement commit is cut)

| # | Precondition | Evidence that discharges it |
|---|---|---|
| P1 | The Introduction (`papers/Introduction.md`, the filename planned at audit README.md:112, OUTLINE-r3/r4) has passed **independent scientific review** and **independent editorial review**. Each review is a separate pass with a recorded verdict at an exact SHA | Review records cited from the Introduction's guiding draft PR (§A.43); verdicts are ACCEPT (or ACCEPT with changes applied and re-checked) at the SHA that lands |
| P2 | The Introduction is in the tree with its own gate dependents. Three are needed. **LEDGER rows:** one for every `**Theorem**`/`**Lemma**`/`**Definition**`/… heading `tools/proof_census.py:34` detects; coverage completeness runs in both directions (`tools/coverage_check.py:102–107`). **Census anchors:** for each family the Introduction carries, e.g. the act 11 family that §6-b relies on; §A.35 requires these in the same commit. **Built artifacts:** `papers/Introduction.tex/.pdf` via `sh ./build.sh Introduction`, carrying the source-sha256 stamp | `release_gate.py` green at that commit (CI exact head). The Introduction may land in the same PR as the retirement, as its first commit. Recommended sequencing is in §2.0 |
| P3 | **Content migrations landed.** MIGRATION §1: none is required. Optional items, only if the owner opts in: the double-difference display from `Main.md:232–238` into B.7.5c, a navigation table, a ch03 lineage paragraph | Owner's choice recorded on the guiding PR. Absent any choice, nothing to land |
| P4 | **Owner decisions** in §5 taken: D1 path, D2 `.tex/.pdf`, D3 notice text, D4 relative links, D5 LICENSE wording, D6 count wording, D7 probe strategy, D8 round or ordinary PR | Recorded on the guiding PR |
| P5 | **Owner approval** of the retirement change at an exact SHA. Under §A.43 item 4, publication is not authorization | Owner comment on the guiding PR |
| P6 | The Introduction states the characterization, if at all, with `Main.md:522`'s binding, and carries none of MIGRATION §2's (d) items | P1's scientific review checks against MIGRATION §2 and REVIEW §3 |

Not a precondition: Issue #931 (the every-horizon display at `appendix-b-derivations.md:454–455` =
`FULL.md:6243–6244`). Retiring the Explainer removes one #931 site (`Explainer.md:373`) from the
active corpus. The book sites need their own correction.

***

## 2. The retirement change

### 2.0 Shape and sequencing

- **One guiding draft PR** (§A.43), linked to an Issue. It holds two commits:
  - **C1**, the accepted Introduction and its own gate dependents (P2);
  - **C2**, the single retirement commit below.

  C2 replaces the Explainer with the Introduction in tuples and indexes, so it needs C1's file to
  exist. Landing them together avoids a window in which the Introduction is on `main` but
  unindexed. It also avoids a window in which the paper count reads 13. If the owner prefers
  separate PRs, land C1 first and C2 after; the content of C2 is unchanged.
- **Ordinary reviewed PR, not a native round** (D8). Nothing in C2 touches a frozen record, a
  receipt or a governed path of an open round. If the owner wants preregistered controls, model them
  on CC-2 (`verification/audits/manuscript/round-cc-2-corpus-correction/`).
- **Pushes.** Every push is checked against `push`-triggered workflows. `verify.yml` runs on
  `pull_request`, and on `push` only for `main`, so a branch push launches nothing governed. No
  `workflow_dispatch` without owner approval (§A.43 item 4).

### 2.1 The Explainer file itself (recommended: option B of §3)

| Path:line | Change | Why |
|---|---|---|
| `papers/Explainer.md` (1059 lines) | `git mv papers/Explainer.md papers/legacy/Explainer.md` | Removes it from every `papers/*.md` scanner (§3); `git log --follow` keeps history |
| `papers/legacy/Explainer.md:3` (current `*[Document status. This Explainer is retained …]*`) | Replace that one line with the standing notice of §3.3 | §A.27 exception |
| `papers/legacy/Explainer.md:682, 686, 763, 781, 818, 822` (8 link targets: `Structure.md`, `Substratum.md`, `SM.md`) | Prefix each target with `../`. Link text unchanged (D4) | They would otherwise resolve inside `papers/legacy/` and break |
| All other lines | **No edit.** The (d) items of MIGRATION §2 stay as they stand; the notice states the file's standing | Preserve current content; no reader-side correction layer (§A.27, §A.30) |
| `papers/Explainer.tex` (stamp `e1167acd…`, `:180` notice) and `papers/Explainer.pdf` | **Remove** (D2). Recommended: history and every Zenodo release keep them. Alternative: build once from the moved file with the shared header and keep both beside it (`papers/legacy/`), knowing nothing rebuilds them | A PDF that does not carry the notice would contradict its source (§A.25 step 5) |

### 2.2 Same-commit dependents: change

| Path:line at 687e885b | Current | Proposed change |
|---|---|---|
| `papers/Main.md:66` | "…the same information$\leftrightarrow$energy link that the companion Explainer draws via Noether's theorem…" | "…the same information$\leftrightarrow$energy link that [Substratum §6.2] draws via Noether's theorem…". Counterpart: `Substratum.md:408` (heading :406). Main's citation style is `[Substratum §3.3]`. Main:66 is a Remark, not a ledgered statement (`proof_census`: Main rows at :44/:48/:50/:56 only), so no LEDGER fingerprint moves |
| `papers/Main.tex:545` (+ `papers/Main.pdf`) | generated | Rebuild: `sh ./build.sh Main` (new source-sha256 stamp) |
| `README.md:12–21` ("Start here" table, header :14) | no Introduction row | Add a first row: "A short scientific introduction to OI (entry point for physicists) → [`papers/Introduction.md`](papers/Introduction.md)". Order follows the owner's structure: Introduction → Main → Book. Optionally add a row to the "Core papers" table (`README.md:68–78`); the role wording is the owner's |
| `README.md:115` | "- [`papers/Explainer.md`](papers/Explainer.md) — older overview, superseded by the book and retained for reference." | "- [`papers/legacy/Explainer.md`](papers/legacy/Explainer.md) — superseded overview, kept for provenance and not maintained." (or drop the bullet; D1) |
| `book/README.md:110` | "…**Methodology** (…), and **Explainer** (superseded by this book and the technical papers), **Complexity**, …" | Remove the Explainer item and add "**Introduction** (short-form entry point)" at the head of the list. "twelve technical papers" stays true: one paper in, one out. Directory documentation, not manuscript (`voice_check.py:21–23`) |
| `book/bibliography.md:9` = `book/The-Incompleteness-of-Observation-FULL.md:6793` (identical; §A.14 mirror) | "…the methodology paper Physics Modulo Gauge, and the companion documents Explainer, Complexity, Medicine, and Bioinformatics.]" | "…the methodology paper Physics Modulo Gauge, the introductory paper Introduction, and the companion documents Complexity, Medicine, and Bioinformatics.]". The same bytes go in both files. Computation is already missing from this list; that pre-existing omission is flagged, not fixed here (§5 R9) |
| `book/The-Incompleteness-of-Observation-FULL.tex:29795` (+ `.pdf`) | generated | Rebuild: `sh ./build.sh --book` |
| `.zenodo.json:26` | "…and the companion documents Explainer, Complexity, Medicine and Bioinformatics." | Same edit as the bibliography, in its HTML. It takes effect at the next Zenodo release; earlier versions keep the Explainer |
| `LICENSE:27–29` (the list spans :27–:29) | "The accompanying papers (Main.md, SM.md, GR.md, Substratum.md, Explainer.md, Complexity.md, Medicine.md and their compiled .tex/.pdf forms) are research manuscripts…" | D5. Minimal: replace `Explainer.md` with `Introduction.md`. Better: "The accompanying papers under `papers/` (including `papers/legacy/`) and the book under `book/`, with their compiled .tex/.pdf forms, are research manuscripts…". That also fixes the pre-existing omission of Structure, Juno, Methodology, Computation and Bioinformatics. Legal text, so it is the owner's wording |
| `build.sh:12` | "build everything (12 papers + book)" | D6: "build every paper under papers/ and the book" (no count). Or leave it: after C1+C2 the count is 12 again. `build.sh:84` (`for md in papers/*.md`) needs no change; it stops building the Explainer by itself |
| `verification/lean-manuscript-census.json:6` (`"manuscripts"`) | lists `papers/Explainer.md` | Replace with `papers/Introduction.md`. The key is descriptive: no tool reads it (`git grep` finds no consumer). It should still match the tree |
| `verification/lean-manuscript-census.json:289–292, 402–405, 436–439, 793–796, 971–974, 997–1000, 1296–1299` | the seven Explainer anchor objects (families: completion classification, CT2, minimal repertoire, OI-N, act 11, act 12, act 45; anchors at `Explainer.md:377/381/383`) | Delete the seven objects, fixing the trailing comma at 788–792, where OI-N's last anchor becomes the Main one. Every family keeps a non-Explainer anchor: 5, 5, 7, 5, 3, 5, 5 remain. The probe's `len(manuscript) >= 5` checks still hold: CT2 at `edge_rigidity_probe.py:3040` has 5; OI-N at `:3126` has 5. If the Introduction carries a family's statement, its anchor is added in C1 (P2), not here |
| census notes at `:298`, and the current-state notes of CT2, minimal repertoire, phase source, Q3 and OI-N (`:798`) | "…the Explainer note…", "Main 3.4, the Explainer and the book chapters carry…" | Drop "the Explainer" from the current-state notes. Leave the act 12 note (`:1014`) unchanged, since it narrates what that round executed. No probe pins these note substrings: a substring search of `verification/lean/*.py` and `tools/*.py` finds none |
| `verification/coverage/LEDGER.json:44–99` | four entries `EXPLAINER:D-unnamed-2883898d`, `EXPLAINER:L-1`, `L-2`, `L-3` (all DEF/MIRROR, unscored) | Delete them. `coverage_check` completeness fails in both directions otherwise ("ledger entry names no canonical statement"). The scored denominator is unchanged. The unscored tally becomes DEF 7, MIRROR 0, SUM 1; no count is quoted anywhere. Their `line` fields (43/49/51/61) are already stale against the census lines (38/44/46/56). This is not checked |
| `verification/audits/manuscript/lean-manuscript-census.md:54, 60, 61, 68, 69, 121, 138` | current-state table rows and sentences naming the Explainer | Drop "the Explainer" (mutable audit note describing the census "at this commit"). Leave `:95`, the historical repair record. The probe pins only `'| continuous time (CT2) | 4 | current |'` (`:3041`) and `'| OI-N passive observation | 4 | current |'` (`:3127`) here; both are unaffected |
| `verification/programmes/oi-qm/PROGRAMME.md:626` | "`papers/GR.md`, `papers/Main.md`, the Explainer, and book chapters — publication-facing statements…" | Drop "the Explainer" (current-state list in a mutable programme index) |
| `verification/lean/edge_rigidity_probe.py` (CI step `edge_rigidity`, `.github/workflows/verify.yml:257`) | 58 lines name the Explainer | See §2.3 |

### 2.3 `edge_rigidity_probe.py`: site-by-site (D7)

**Strategy.** Where the Explainer appears in a **negative** (forbidden-phrase) loop, substitute the
Introduction, so the new entry-point paper inherits those guards. Where it appears in a
**positive** (must-carry) check, drop it: the Introduction's recommended scope does not carry the
OI⁺, primitive-source, CT2, Q3 and layer-flow summaries (OUTLINE-r2: E4 is Alt-X only).
Retargeting positive checks would force the paper to carry content it deliberately omits. Counts
and countercontrols are adjusted.

| Lines | Kind | Action |
|---|---|---|
| 2870–2875 (`_ms` load: `.md` and `.tex`) | load → negative checks 2877–2882; positive 2921, 2965 | Substitute `papers/Introduction.md` / `.tex` |
| 2917–2923 (`_msum` must appear in Main, Explainer, ch01, ch19, FULL) | positive | Drop the Explainer; fix the comment at 2917 |
| 2965–2966 (`.tex` carries "no closure of the implementations under the adjoint") | positive | Drop `papers/Explainer.tex` |
| 2967–2980 (R7-MSP description, "Main, the Explainer and both book mirrors carry") | text | Reword without the Explainer |
| 2990–2994 (`_ctn_files` load) | load → negative 3020+; positive 3015–3018 | Substitute the Introduction |
| 3015–3016, 3018 (`_ctn_sum`; `.tex` "with no one-parameter-group law…") | positive | Drop the Explainer |
| 3042–3050 (R7-CTN description) | text | Reword |
| 3058, 3090–3112 (`_oinn_expl`, `_oe`, `_oinn_epar`: the Explainer's OI-N paragraph must exist and carry 9 phrases; the forbidden-vocabulary loop over Main's and the Explainer's paragraphs) | positive, plus negative on the paragraph | Delete the Explainer read and positive list. Reduce the vocabulary loop to Main's paragraph `_op`. Main's checks (3059–3089) are unchanged |
| 3113–3121 (forbidden passive-observation readings in Main, Explainer, `.md`/`.tex`) | negative | Substitute the Introduction (`.md` and `.tex`) |
| 3122–3123 (`.tex` "cannot coexist with complete passive observation") | positive | Drop `papers/Explainer.tex` |
| 3128–3140 (R7-OINN description, "the Explainer …") | text | Reword |
| 3273, 3476, 3596, 3737, 3831, 3928, 4054, 4156, 4259, 4351–4353, 4475, 4568–4570, 4691, 4833, 4949–4951, 5080, 5241, 5381, 5538, 5694, 5847, 6011, 6180, 6345, 6462, 6567, 6659, 6746, 6898 | negative (superseded identifiers, kernel-only module names, stale clauses) | Substitute the Introduction (`.md`, and `.tex` where the tuple has `.tex`). In 4691 and 4833 the `_rel in ('papers/GR.md','papers/Main.md') or …` exemption is unchanged, so the Introduction is held to the stricter non-GR/Main rule. Check this against the Introduction's intended kernel citations before C2 |
| 4344–4348 (`_pqual` in Main, Explainer, ch01, ch19, FULL) | positive (`count == 2` applies to the last file, FULL) | Drop the Explainer |
| 4557–4562 (`_qsum` and `_ctn_sum`; `_qcount == 6`) | positive + count | Drop the Explainer. **`_qcount == 6` → `== 5`** (Main 1, ch01 1, ch19 1, FULL 2; measured at 687e885b) |
| 4935–4944 (`_ssum`; `_scount == 6 and _qcount2 == 6`) | positive + count | Drop the Explainer. **Both → `== 5`** (same measurement) |
| 8515 (`_A11P_EXPL`) | load | Delete |
| 8563 (`_a11p_stronger_target_open` over Main, Explainer, ch01) | positive | Drop the Explainer |
| 8657, 8666–8667, 8980 (E16 three statuses: "The bridge therefore has three statuses", "characterized conditionally" in the Explainer) | positive | Drop the Explainer clauses. E16 keeps Main, GR, Methodology and ch19. Reword the docstring at 8657 |
| 8848, 8869, 8908, 9109 (descriptions/docstrings) | text | Reword |
| 8882–8892 (`_a12p_two_sided`, `expl=` parameter; `_ex` in the positive and negative lists) | positive + negative | Remove the `expl` parameter and `_ex` from both lists |
| 8903, 8917, 8925, 8937, 8956 (`… in x for x in (_A11P_EXPL, _A11P_CH01[, _A11P_CH19])`) | positive | Drop `_A11P_EXPL` |
| 9005–9010 (`_a12p_reg`: the act 12 family's files must include `papers/Explainer.md`) | positive (registry) | Drop `papers/Explainer.md` from the required set. **Must change together with the census edit**, or R7-A12P fails |
| 9040–9044 (mutation `_a12p_m3` on the Explainer: "the two-sided action called maximal") | countercontrol | **Retarget to ch01**: `_A11P_CH01.replace('each maximal among uniform actions of its kind', '… forming the maximal two-sided action')` with `ch01=`. ch01 carries the phrase once (measured). This keeps a non-Main countercontrol for the "maximal two-sided" guard (§A.21; Code Review Rules "Exactness and controls") |

Under D7's alternative (drop rather than substitute in negative loops), the Introduction gets no
forbidden-phrase coverage from this probe. That would then have to come from a new guard in C1.

### 2.4 Same-commit dependents: keep unchanged (with reason)

| Path:lines | Status | Why unchanged |
|---|---|---|
| `verification/audits/manuscript/round-cc-1-corpus-correction/` (`controls.py:25,193`; `preregistration.md`, `result.md`) | native round record (receipt `CC-1.json`) | §A.39 G13: the record directory is immutable after its receipt. Its controls hard-code `papers/Explainer.md`. They are not run by CI (no `verify.yml` step) and will not re-run on a tree without the file. That is expected for a frozen record. State it in the C2 commit message |
| `verification/audits/manuscript/round-cc-2-corpus-correction/` (`controls.py:27,198`; prereg; result) | native round record (`CC-2.json`) | same |
| `verification/programmes/oi-qm/track-b/act-45-fixed-basis-image/` (`controls.py:27–37`; prereg 11 hits; result) | native round record (`A45.json`) | same |
| `verification/audits/manuscript/round-consc-2-observation-terminology/preregistration.md` | native round record (`CONSC-2.json`) | same |
| `verification/infrastructure/round-v3-12-retirement-census/census.json`, `round-v3-13-retirement/messages.json`, `round-v3-14-retirement/ledger.json`, `messages.json` | native round records (`V3-12/13/14.json`) | same |
| `verification/certificates/A12P.json`; `verification/audits/foundations/act11-scope-propagation-audit.md`, `…-open-frontier-amendment.md`, `act12-scope-propagation-audit.md`, `a6-covariance-propagation-audit.md`; `verification/programmes/oi-qm/track-b/act-01-indivisibility/result.md`, `act-02-transpose-bridge/{preregistration,result}.md`; `…/round-bg-1-integer-classification/preregistration.md`; `verification/programmes/hydrodynamics/round-h-d-source-reconciliation/{preregistration,result}.md`; `verification/programmes/substratum/lemma-24-1b-framework-data/preregistration.md` | legacy records (`legacy-records.json`; most under closed namespaces) | The `legacy-records` gate step keeps each blob unchanged |
| `verification/audits/provenance-errata/objects/ee91dbb4…`, `ad64b603…` | retained objects (§A.42) | Byte-for-byte evidence; never edited |
| `verification/audits/provenance-errata/errata.json:915,965,995,1014,1064,1212`, `README.md:163` | errata audit (mutable, historical) | They record past citations; true as history (§A.42 item 4 forward-only) |
| `verification/README.md:315, 345, 404, 1196, 1200, 1242, 1246, 1341, 1953, 1960, 1975, 2071, 2105, 2176, 2345` | root landing page (mutable) | Each sits in a round's own narrative and says what that round propagated or rebuilt. They stay true as history. The one present-tense sentence, `:1959–1960` ("OI-N is narrated in one paragraph of Main §3.4 and one of the Explainer"), is inside the census round's paragraph. Recommendation: leave, as round history. Owner may instead correct it forward (§5 R8) |
| `verification/audits/foundations/{q3,phase}-propagation-audit.md`, `verification/audits/operational/{sourcing-propagation,typed-completion,quasilocal-completion,instrument-completion}-audit.md`, `verification/audits/foundations/coherent-continuum-source-audit.md`, `verification/audits/manuscript/representation-sector-audit.md`, `verification/audits/manuscript/liv-coefficient-sigma/correction-2026-10-15.md`, `verification/programmes/substratum/source-audit.md` | audit records (mutable, historical) | Each records the propagation or scope of its own audit ("six occurrences", "the Explainer … rebuilt"). These stay true of the audit. Not current-state claims |
| `.github/workflows/verify.yml:257` | CI step list | Unchanged; the probe still runs |
| `tools/*.py`, `papers/oi_lattice_code/*.py`, `verification/lean/bohr_frequency_probe.py:277` | glob/listdir scanners | No change. They stop seeing the Explainer by the move. `bohr_frequency_probe`'s `len(CORPUS) > 10` still holds (11 papers + the Introduction + book files) |

**Expected surviving `git grep -n -i explainer` hits after C2:** all of §2.4. Also
`papers/legacy/Explainer.md` itself, `README.md` (the legacy bullet, if kept), `LICENSE` (if
"papers/legacy/" is named), the census act 12 note (`:1014`) and the census note's `:95`.
Nothing else: no hit in `papers/*.md`, `papers/*.tex`, `book/`, `.zenodo.json` or
`verification/lean/`.

***

## 3. What "preserve for provenance" means

### 3.1 Options

| | (A) keep at `papers/Explainer.md`, notice only | **(B) move to `papers/legacy/Explainer.md`, notice** (recommended) | (C) delete; history and a tag only |
|---|---|---|---|
| Preserves content and history | yes | yes (`git log --follow`; one-line notice and 8 link targets changed) | history only |
| "Marked superseded" in the tree | yes | yes | no file to mark |
| "Stop maintaining" actually holds | **no**, see 3.2 | yes, with one residual (3.2) | yes |
| External deep links to `papers/Explainer.md` | kept | break (README and Zenodo updated; old Zenodo versions unaffected) | break |
| Repo footprint (§A.28) | 1 md + tex + pdf, all maintained | 1 md, frozen | none |

(A) fails the owner's "stop maintaining it as an active manuscript", for the reasons in 3.2. (C)
fails "mark the Explainer as superseded" and is not "controlled replacement". **(B) is
recommended.** `papers/` already holds subdirectories (`oi_lattice_code/`, `main_repro/`), so the
layout is not new. §A.36 does not apply: it governs `verification/` artifacts.

### 3.2 Which gate tools would still scan it (checked against the code at 687e885b)

| Scanner | How it finds files | (A) in place | (B) `papers/legacy/` |
|---|---|---|---|
| `tools/staleness_check.py:26–28` | `os.listdir('papers')`, top level | scanned: `.tex` stamp must match; `.tex/.pdf` kept | not scanned |
| `tools/voice_check.py:44–48` | `os.listdir('papers')`, top level | scanned. Exempting it would mean editing `PAPERS_EXEMPT` and the mutation-tested `voice_scope_test.py` | not scanned |
| `tools/dependency_label_check.py:222–226` | `os.listdir` of `papers`, `book` | scanned (strict) | not scanned |
| `tools/lean_manuscript_census.py:78` | `glob('papers/*.md')` | **scanned for RESOLUTION and SUPERSESSION** of its `(kernel: \`bridge_traj\`, \`rooted_eq_iff_slice_eq\`)` (`Explainer.md:377`). A future supersession of either identifier would force an edit to the "unmaintained" file | not scanned |
| `tools/proof_census.py:82` → `tools/coverage_check.py` | `glob('papers/*.md')`; its docstring says "Canonical means `papers/*.md`" | scanned: its Definition and Lemmas 1–3 stay "canonical statements" needing LEDGER rows, which contradicts "superseded" | not scanned; LEDGER rows removed |
| `papers/oi_lattice_code/architecture_check.py:18` | `glob('papers/*.md')` | scanned against every future invariant added | not scanned |
| `papers/oi_lattice_code/citation_check.py:17` | `glob('papers/*.md')` | scanned (cites `fastbath_probes.py`, `hchi_selectivity_probes.py`, `review4_probes.py`; a rename forces an edit) | not scanned |
| `build.sh:84` | `papers/*.md` | rebuilt on every full build | not built |
| `verification/lean/bohr_frequency_probe.py:277` | `glob('papers/*.md')` | scanned | not scanned |
| `verification/lean/edge_rigidity_probe.py` | explicit paths | removed in both options (§2.3) | — |
| `tools/claims_check.py:103`, `tools/duplicate_check.py:31,49`, `tools/baseline_label_check.py:37,90` | `os.walk(root)`, every `.md` | scanned | **still scanned** |

**Residual under (B).** Three whole-tree checks still read the legacy file. It passes all three at
687e885b, since the gate is green there. If a future rule added to one of them flags it, do not edit
the frozen text. Add a narrow, documented exclusion of `papers/legacy/` to that tool in the same
change, with the tool's own self-test or mutation test updated. That needs owner approval. Do not
add the exclusion pre-emptively: the risk is unverified (§A.28).

**Should a superseded file pass voice/claims checks?** Under (B) it is outside the voice scope by
construction: `voice_check` scans the manuscript only, and the file is no longer manuscript. It
stays inside claims/duplicate, which it currently passes. Keeping it passing is free while it is
frozen, so exclusions are not needed now.

### 3.3 The standing notice (§A.27 exception)

It replaces `Explainer.md:3`. One line. It states the standing fact and nothing about history:

> `*[Superseded document, kept for provenance and not maintained. The current presentation of the framework is the Introduction paper ([`../Introduction.md`](../Introduction.md)), the technical papers and the book; where this text differs from them, they govern.]*`

Checks on the wording:
- None of `voice_check.py`'s PATTERNS matches it: "withdrawn", "earlier draft", "formerly", "now
  states", "previously said", "no longer …" and "has since been …" are all absent.
- There is no date and no "was" or "earlier".
- Under option (A) the link would read `Introduction.md` (no `../`).
- "kept for provenance" is used rather than "kept unchanged", because D4 edits 8 link targets.

***

## 4. Checks after the change, and a dry-run recipe

### 4.1 Required to pass at C2

1. **Build.** Run `sh ./build.sh Main` and `sh ./build.sh --book`; the Introduction is built in C1.
   - Zero dropped glyphs; plausible page counts for Main and the book (AGENTS build recipe).
   - Without the canonical toolchain the PDFs are provisional; flag them per the
     constrained-environment caveat.
2. **Release gate** (`python3 tools/release_gate.py`). Every step must be green:
   - toolchain, staleness, baseline-label, voice, voice-scope, ci-gate-presence;
   - artifact-placement, manifest-drift;
   - claims, duplicate, mirror (bibliography ↔ FULL), citation, architecture, dependency-label;
   - coverage (the LEDGER deletion; the Introduction's rows from C1), lean-axioms (CI only);
   - lean-manuscript (census: anchors present, no ANCHOR-file-missing, Introduction citations
     resolve);
   - legacy-records (no legacy blob touched), v3-self-test, v3-corpus;
   - v3-receipts (G13: no native record directory touched), citation-roles.
   - legacy-records, v3-receipts and citation-roles need full history, so they run in CI. Note:
     there is no `evidence-retention` step in `tools/release_gate.py` at 687e885b.
3. **Probe.** `python3 verification/lean/edge_rigidity_probe.py` (CI step `edge_rigidity`):
   - every check PASS, in particular R7-MSP, R7-CTN, R7-OINN, R7-PROP, R7-Q3P, R7-SRCP, R7-A11P and
     R7-A12P;
   - also `verification/lean/bohr_frequency_probe.py` (F8 corpus).
4. **Countercontrols** (run on a scratch copy, never committed). Each mutation must fail cleanly on
   its target:
   - (i) Re-add one Explainer anchor object to a copy of the census JSON. `lean_manuscript_census.py
     --root <copy>` must fail with `ANCHOR file papers/Explainer.md … does not exist`.
   - (ii) Insert one forbidden phrase into a copy of `papers/Introduction.md`, e.g.
     `reversible implementation locality` for R7-MSP, or `qm requires oi` for R7-OINN. The
     corresponding R7 check must fail. This shows the §2.3 substitution is live.
   - (iii) Restore one deleted LEDGER entry in a copy. `coverage_check.py --ledger <copy>` must
     fail with "ledger entry names no canonical statement".
   - (iv) The retargeted `_a12p_m3` runs inside the probe and must be caught. R7-A12P passes only if
     the mutant is rejected.
5. **Re-grep** (§A.25 step 6). `git grep -n -i explainer` must equal the expected survivor list of
   §2.4. Record the surviving count in the PR description. Separately, `git grep -n "companion
   Explainer"` must have zero hits.
6. **Mirror.** `diff <(sed -n 9p book/bibliography.md) <(grep -F 'The Observational Incompleteness
   Framework*. Zenodo' book/The-Incompleteness-of-Observation-FULL.md)` must be empty (one match in FULL at
   687e885b).
   `mirror_check.py` covers chapters; the bibliography line is checked by this diff.

### 4.2 Dry-run recipe (local, bounded, no shared-store risk; §A.40)

```sh
S=S
G="git -c gc.auto=0 -c maintenance.auto=false"
# 1. an independent tree from the candidate head (C1 applied); no linked worktree, no fetch into the shared store
mkdir -p $S/retire/dry && cd <checkout-with-C1> && $G archive <C1-sha> | tar -x -C $S/retire/dry
cd $S/retire/dry
# 2. apply C2 by script (git mv is replaced by mv in the archive copy)
mkdir -p papers/legacy && mv papers/Explainer.md papers/legacy/Explainer.md && rm -f papers/Explainer.tex papers/Explainer.pdf
#    … the line-3 notice, the 8 link targets, and the §2.2/§2.3 edits, each as an exact old→new replacement that must match once
# 3. bounded local checks (each once)
python3 -m py_compile verification/lean/edge_rigidity_probe.py tools/*.py
for t in staleness_check voice_check voice_scope_test claims_check duplicate_check dependency_label_check coverage_check lean_manuscript_census; do
  python3 -I tools/$t.py $( [ $t = dependency_label_check ] && echo --strict ) || echo "FAIL $t"; done
python3 -I papers/oi_lattice_code/mirror_check.py; python3 -I papers/oi_lattice_code/citation_check.py; python3 -I papers/oi_lattice_code/architecture_check.py
(cd verification/lean && python3 -I edge_rigidity_probe.py | tail -40 && python3 -I bohr_frequency_probe.py | tail -5)
# 4. countercontrols 4.1(4)(i)–(iii) on throwaway copies; then the re-grep 4.1(5) with grep -rni (no .git in the archive)
```

- The full gate, including the history-dependent steps and `lean-axioms`, runs in CI on the
  guiding draft PR (automatic `pull_request` run).
- An exact-head attestation is needed only if the owner makes this a native round (D8).
- If any local step is slow, stop and leave it to CI (§A.40).

***

## 5. Risks and owner decisions

**Owner decisions**

| ID | Decision | Recommendation |
|---|---|---|
| D1 | Path: (A) in place, (B) `papers/legacy/Explainer.md`, (C) delete | **B** (§3.1–3.2) |
| D2 | `Explainer.tex/.pdf`: remove, or rebuild once into `papers/legacy/` | **Remove**; history and Zenodo versions keep them |
| D3 | Notice text | §3.3 as drafted |
| D4 | Fix the 8 relative link targets in the legacy file | **Fix** (path-only edit); otherwise they break silently |
| D5 | LICENSE scope wording | Generalize to "papers under `papers/` (including `papers/legacy/`) and the book" |
| D6 | Count wording at `build.sh:12` | Remove the count; otherwise it must be re-checked whenever the set changes |
| D7 | Probe: substitute the Introduction in negative loops (recommended), or drop the Explainer only | **Substitute**. Pre-check that the Introduction does not legitimately need any identifier those loops forbid (in particular 4691/4833, which exempt only GR and Main) |
| D8 | Ordinary reviewed PR or native V3 round | Ordinary PR. It touches no frozen record or open round's governed paths |
| D9 | Optional book items (MIGRATION §1.3): the double-difference display from Main, a navigation table, a ch03 lineage paragraph | None by default. The table, if wanted, waits for #931 |
| D10 | `README.md:115`: keep a legacy bullet or drop it | Keep one line pointing to `papers/legacy/Explainer.md`, so the preserved file is discoverable |

**Risks**

| ID | Risk | Mitigation |
|---|---|---|
| R1 | External deep links and citations to `papers/Explainer.md` break under (B) | README bullet; Zenodo keeps older versions; the notice names the replacement. If D1 = A, the risks in §3.2 apply instead |
| R2 | The legacy file keeps its (d) statements (e.g. :373 every-horizon form, :745 "unique algorithm", :771 "nothing to tune"), and a reader may cite them | The standing notice says the maintained sources govern. The policy forbids rewriting it, and annotating would be assert-then-qualify (§A.30). If the owner judges the exposure too high, choose (C) |
| R3 | A future rule in claims/duplicate/baseline-label flags the frozen file | §3.2 residual: a narrow exclusion with an updated self-test, owner-approved, at that time |
| R4 | Probe edits weaken coverage (positive checks lose one file; one mutation retargeted) | Substitution keeps negative coverage on the Introduction; m3 retargeted to ch01; countercontrols 4.1(4) |
| R5 | Partial landing: census edited without the probe's `_a12p_reg` set (9005–9010), or probe without census | Single commit C2; R7-A12P fails in CI if they diverge |
| R6 | Frozen controls (CC-1, CC-2, A45) cannot re-run on the new tree | Expected for frozen records (§A.39); stated in the C2 message; not run by CI |
| R7 | Bibliography ↔ FULL mirror drift | Same-bytes edit plus the diff in 4.1(6) |
| R8 | `verification/README.md:1959–1960` reads as present-tense state ("OI-N is narrated … one of the Explainer") | Default: leave it as round history. Option: forward correction of that one sentence |
| R9 | Pre-existing list gaps surface during the edit: Computation is absent from `bibliography.md:9`/FULL and `.zenodo.json:26`; LICENSE omits five papers | Out of scope for retirement; flag on the PR. Fix in C2 only if the owner says so |
| R10 | Shared object store: an auto-gc during the work | Every git command with `-c gc.auto=0 -c maintenance.auto=false`. The dry-run uses `git archive` into an independent directory, not a linked worktree |
| R11 | #931 still open: the book's B.7.6 display (`appendix-b:454–455` = `FULL:6243–6244`) | Not a precondition. Retirement removes the Explainer site; the book sites need their own narrow correction |
| R12 | The Introduction's scope does not cover the Explainer's §§4–6 (ħ, cosmology, SM) | Accepted by design (OUTLINE-r3). The book and GR carry it. The README "Start here" order (Introduction → Main → book) makes the route explicit |
