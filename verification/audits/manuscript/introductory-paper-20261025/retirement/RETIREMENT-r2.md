# Explainer retirement plan, revision 2

Revision 2 applies the independent review `S/paper/retire-review/REVIEW.md` (ACCEPT WITH CHANGES).
It covers RC1–RC7 and the nits, and records the owner decisions of 2026-10-26. `RETIREMENT.md`
(revision 1) is kept unchanged as the reviewed object; `CHANGES-r2.md` lists every change.
`S` = `S`.

**Owner decisions recorded (2026-10-26).** These are decided and are no longer open:
- **OD1.** The retirement strategy is approved, conditional on the Introduction passing independent
  review and being accepted.
- **OD2.** The move to `papers/legacy/` is approved, to be made after acceptance.
- **OD3.** A superseded notice is required.
- **OD4.** `Main.md:66` → `[Substratum §6.2]` is approved.
- **OD5.** The shape is one PR with two commits (§2.0).
- **OD6, safeguard S1: historical reproducibility.** The move must not break reproduction of earlier
  certified results. Old paths in immutable receipts and records are preserved, not rewritten (§2.5).
- **OD7, safeguard S2: external access.** A minimal `papers/Explainer.md` redirect notice points to
  the Introduction and to the archived document. It is excluded from active checks where possible.
  The review's dry run shows that no exclusion is needed (§3.2).

Planning document. No repository file is changed and nothing is committed. All `path:line`
references are at `main` `687e885b1cfd24d6f17eee439101afc8acf07015`. Dependents were found with
`git -c gc.auto=0 -c maintenance.auto=false grep -n -i explainer 687e885b`: 57 files.
The companion content audit is `MIGRATION-r2.md` in this directory.

**Owner policy, restated as gates.**
- This is a controlled replacement, not a deletion.
- The Explainer's content and history are preserved.
- No redundant material is carried forward.
- Index, link and documentation changes happen only after the Introduction passes independent
  scientific and editorial review.
- The Introduction inherits no unsupported claim (MIGRATION-r2 §2 class (d)).
- Earlier certified results stay reproducible, and immutable records keep their old paths (S1).
- The old path keeps resolving, to a redirect (S2).

***

## 1. Preconditions (all must hold before the retirement commit is cut)

| # | Precondition | Evidence that discharges it |
|---|---|---|
| P1 | The Introduction has passed **independent scientific review** and **independent editorial review**. Each review is a separate pass with a recorded verdict at an exact SHA | Review records cited from the Introduction's guiding draft PR (§A.43); verdicts are ACCEPT (or ACCEPT with changes applied and re-checked) at the SHA that lands. The scientific review carries the P6 checklist |
| P2 | The Introduction is in the tree with its own gate dependents. Three are needed. **LEDGER rows:** one for every `**Theorem**`/`**Lemma**`/`**Definition**`/… heading `tools/proof_census.py:34` detects; coverage completeness runs in both directions (`tools/coverage_check.py:102–107`). **Census anchors:** for each family the Introduction carries, e.g. the act 11 family that §6-b relies on; §A.35 requires these in the same commit. **Built artifacts:** `papers/Introduction.tex/.pdf` via `sh ./build.sh Introduction`, carrying the source-sha256 stamp | `release_gate.py` green at that commit (CI exact head). The Introduction may land in the same PR as the retirement, as its first commit. Recommended sequencing is in §2.0 |
| P3 | **Content migrations landed.** MIGRATION-r2 §1: none is required. Optional items, only if the owner opts in: the double-difference display from `Main.md:232–238` into B.7.5c, a navigation table, a ch03 lineage paragraph, a holography objection in Appendix C (MIGRATION-r2 row 23a) | Owner's choice recorded on the guiding PR. Absent any choice, nothing to land |
| P4 | **Remaining owner decisions** of §5 taken (OQ1–OQ6: M1/M2; README:115 target; the holography objection; the optional book items; LICENSE wording and the pre-existing gaps; the README Core-papers row and §1). The recorded decisions OD1–OD7 are not reopened | Recorded on the guiding PR |
| P5 | **Owner approval** of the retirement change at an exact SHA. Under §A.43 item 4, publication is not authorization | Owner comment on the guiding PR |
| P6 | **Scientific-review checklist, part of P1.** (a) The Introduction states the characterization, if at all, with `Main.md:522`'s binding, and carries none of MIGRATION-r2 §2's (d) items. (b) **Kernel map (RC7).** The accepted text carries the kernel map, as Appendix A or as the Alt-L §3 table, with unformalized links listed. This is the condition on which MIGRATION-r2 §3's supersession of the Explainer tables rests. The draft at #918 `8fcc6443` reportedly has 16 rows (not verified here: the object is not in the local store); the accepted text is what counts. (c) **Probe pre-check (RC5a; was D7).** Check every identifier and phrase the C2-substituted negative loops of §2.3 forbid against the accepted text, so the substitution cannot invalidate a text after acceptance. Examples: :2877–2882 (`reversible implementation locality`, superseded package names), :3113 (passive-observation misreadings), :3273 (`Route B`, `DerivedOI`, `routeB_target`), :3737 and :4691/:4833 (kernel-only module and predicate names; these two exempt only GR and Main). Any legitimate need is resolved before acceptance, either by rewording the text or by an explicitly reviewed per-loop exemption | P1's scientific review record, which lists (a)–(c) with verdicts |
| P7 | **Re-derivation at the cut base (RC5b).** The change list is valid at `687e885b` only. At the base C2 is cut from: (a) re-run `git -c gc.auto=0 -c maintenance.auto=false grep -n -i explainer <base>` (§A.25 step 1) and reconcile every path:line of §2.1–§2.5, including the probe's alias lines that do not contain the word (§2.3); (b) confirm that no open native round with a designated `F` lists any C2 path among its governed paths (`v3-governed-paths` blocks of open preregistrations); (c) if the evidence-retention archive (`verification/audits/evidence-retention/`) has landed on `main`, confirm that no file C2 edits is a mapped citing file, since `check_retention.py` requires an unchanged citing blob. It is not on `main` at 687e885b, and the review found none in the branch copy; (d) confirm the Introduction's filename. `papers/Introduction.md` is the planned name, per `SOURCES-r3.md:317–318`, which cites "audit README.md:112", i.e. `verification/audits/manuscript/introductory-paper-20261025/README.md` on the audit branch; the local copy at `S/pintro/repo` does not state the filename at :112 | A reconciliation note on the guiding PR, at the exact base SHA |

Not a precondition: Issue #931 (the every-horizon display at `appendix-b-derivations.md:454–455` =
`FULL.md:6243–6244`). Retiring the Explainer removes one #931 site (`Explainer.md:373`) from the
active corpus. The book sites need their own correction.

***

## 2. The retirement change

### 2.0 Shape and sequencing

- **One guiding draft PR** (§A.43), linked to an Issue. This is decided (OD5). It holds two commits:
  - **C1**, the accepted Introduction and its own gate dependents (P2);
  - **C2**, the single retirement commit below.

  C2 replaces the Explainer with the Introduction in tuples and indexes, so it needs C1's file to
  exist. Landing them together avoids a window in which the Introduction is on `main` but
  unindexed. It also avoids a window in which the paper count reads 13. If the owner prefers
  separate PRs, land C1 first and C2 after; the content of C2 is unchanged. OD5 settles this:
  one PR.
- **Ordinary reviewed PR, not a native round** (plan default PD5). Nothing in C2 touches a frozen record, a
  receipt or a governed path of an open round. If the owner wants preregistered controls, model them
  on CC-2 (`verification/audits/manuscript/round-cc-2-corpus-correction/`).
- **Pushes.** Every push is checked against `push`-triggered workflows. `verify.yml` runs on
  `pull_request`, and on `push` only for `main`, so a branch push launches nothing governed. No
  `workflow_dispatch` without owner approval (§A.43 item 4).

### 2.1 The Explainer file and the redirect stub (option B′ of §3: approved move OD2, plus redirect S2)

| Path:line | Change | Why |
|---|---|---|
| `papers/Explainer.md` (1059 lines) | `git mv papers/Explainer.md papers/legacy/Explainer.md` | Removes it from every `papers/*.md` scanner (§3); `git log --follow` keeps history |
| `papers/legacy/Explainer.md:3` (current `*[Document status. This Explainer is retained …]*`) | Replace that one line with the standing notice of §3.3 | §A.27 exception |
| `papers/legacy/Explainer.md:682, 686, 763, 781, 818, 822` (8 link targets: `Structure.md`, `Substratum.md`, `SM.md`) | Prefix each target with `../`. Link text unchanged (plan default PD2) | They would otherwise resolve inside `papers/legacy/` and break |
| All other lines | **No edit.** The (d) items of MIGRATION-r2 §2 stay as they stand; the notice states the file's standing | Preserve current content; no reader-side correction layer (§A.27, §A.30) |
| `papers/Explainer.md` (new, at the old path) | **Redirect stub**, the exact text of §3.3(b). It must stay inert: no `kernel:` span, no `**Theorem**`/`**Lemma**`/`**Definition**`/… heading, no code-file (`*.py`) citation, none of `voice_check`'s words | S2 / OD7: external deep links to the `.md` keep resolving |
| `papers/Explainer.tex`, `papers/Explainer.pdf` (stamp `e1167acd…`, `:180` notice) | **M1 (recommended; owner decision OQ1):** regenerate both from the stub with `sh ./build.sh Explainer` and commit them. `staleness_check` then guards the pair; the old `.pdf` URL resolves to a one-page pointer. **M2 (alternative):** delete both and add one skip for `Explainer` to `build.sh`'s full-build loop (`build.sh:84`). Staleness passes with the stub unstamped (`staleness_check.py:58–65` reports a missing `.tex`, it does not fail). The `.pdf` URL breaks, and a hard-coded name enters `build.sh` | The full Explainer PDF stays in history and in every earlier Zenodo version. No PDF of the full text is kept at HEAD, so none can contradict its source (§A.25 step 5) |
| `papers/legacy/Explainer.tex/.pdf` | Not created | Nothing would rebuild them (§3.2) |

### 2.2 Same-commit dependents: change

| Path:line at 687e885b | Current | Proposed change |
|---|---|---|
| `papers/Main.md:66` | "…the same information$\leftrightarrow$energy link that the companion Explainer draws via Noether's theorem…" | "…the same information$\leftrightarrow$energy link that [Substratum §6.2] draws via Noether's theorem…". Counterpart: `Substratum.md:408` (heading :406). Main's citation style is `[Substratum §3.3]`. Main:66 is a Remark, not a ledgered statement (`proof_census`: Main rows at :44/:48/:50/:56 only), so no LEDGER fingerprint moves |
| `papers/Main.tex:545` (+ `papers/Main.pdf`) | generated | Rebuild: `sh ./build.sh Main` (new source-sha256 stamp) |
| `README.md:12–21` ("Start here" table, header :14) | no Introduction row | Add a first row: "A short scientific introduction to OI (entry point for physicists) → [`papers/Introduction.md`](papers/Introduction.md)". Order follows the owner's structure: Introduction → Main → Book. Optionally add a row to the "Core papers" table (`README.md:68–78`); the role wording is the owner's |
| `README.md:115` | "- [`papers/Explainer.md`](papers/Explainer.md) — older overview, superseded by the book and retained for reference." | Owner decision OQ2: point the bullet at the stub (`papers/Explainer.md`, which links on) or straight at `papers/legacy/Explainer.md`. Proposed text: "- [`papers/legacy/Explainer.md`](papers/legacy/Explainer.md) — superseded overview, kept for provenance and not maintained." Either target satisfies the survivor list of §2.4 |
| `book/README.md:110` | "…**Methodology** (…), and **Explainer** (superseded by this book and the technical papers), **Complexity**, …" | Remove the Explainer item and add "**Introduction** (short-form entry point)" at the head of the list. "twelve technical papers" stays true: one paper in, one out. Directory documentation, not manuscript (`voice_check.py:21–23`) |
| `book/bibliography.md:9` = `book/The-Incompleteness-of-Observation-FULL.md:6793` (identical; §A.14 mirror) | "…the methodology paper Physics Modulo Gauge, and the companion documents Explainer, Complexity, Medicine, and Bioinformatics.]" | "…the methodology paper Physics Modulo Gauge, the introductory paper Introduction, and the companion documents Complexity, Medicine, and Bioinformatics.]". The same bytes go in both files. Computation is already missing from this list; that pre-existing omission is flagged, not fixed here (§5 R9) |
| `book/The-Incompleteness-of-Observation-FULL.tex:29795` (+ `.pdf`) | generated | Rebuild: `sh ./build.sh --book` |
| `.zenodo.json:26` | "…and the companion documents Explainer, Complexity, Medicine and Bioinformatics." | Same edit as the bibliography, in its HTML. It takes effect at the next Zenodo release; earlier versions keep the Explainer |
| `LICENSE:27–29` (the list spans :27–:29) | "The accompanying papers (Main.md, SM.md, GR.md, Substratum.md, Explainer.md, Complexity.md, Medicine.md and their compiled .tex/.pdf forms) are research manuscripts…" | Owner decision OQ5. Under B′, `Explainer.md` still names an existing file (the stub), so the minimal edit, adding `Introduction.md`, is optional. Better: "The accompanying papers under `papers/` (including `papers/legacy/`) and the book under `book/`, with their compiled .tex/.pdf forms, are research manuscripts…". That also fixes the pre-existing omission of Structure, Juno, Methodology, Computation and Bioinformatics. Legal text, so it is the owner's wording |
| `build.sh:12` | "build everything (12 papers + book)" | Plan default PD3: "build every paper under papers/ and the book" (no count). Or leave it: the count under M1 is 13 `.md` files, the stub included, so a numeric comment would mislead. Under M1, `build.sh:84` (`for md in papers/*.md`) needs no change and builds the stub. Under M2 it gains the one skip of §2.1 |
| `verification/lean-manuscript-census.json:6` (`"manuscripts"`) | lists `papers/Explainer.md` | Replace with `papers/Introduction.md`. The key is descriptive: no tool reads it (`git grep` finds no consumer). It should still match the tree |
| `verification/lean-manuscript-census.json:289–292, 402–405, 436–439, 793–796, 971–974, 997–1000, 1296–1299` | the seven Explainer anchor objects (families: completion classification, CT2, minimal repertoire, OI-N, act 11, act 12, act 45; anchors at `Explainer.md:377/381/383`) | Delete the seven objects, fixing the trailing comma at 788–792, where OI-N's last anchor becomes the Main one. Every family keeps a non-Explainer anchor: 5, 5, 7, 5, 3, 5, 5 remain. The probe's `len(manuscript) >= 5` checks still hold: CT2 at `edge_rigidity_probe.py:3040` has 5; OI-N at `:3126` has 5. If the Introduction carries a family's statement, its anchor is added in C1 (P2), not here |
| census notes at `:298` (completion classification), `:411` (CT2), `:453` (minimal repertoire), `:551` (phase source), `:573` (Q3), `:798` (OI-N) | "…the Explainer note…", "Main 3.4, the Explainer and the book chapters carry…" | Drop "the Explainer" from the current-state notes. Leave the act 12 note (`:1014`) unchanged, since it narrates what that round executed. No probe pins these note substrings: a substring search of `verification/lean/*.py` and `tools/*.py` finds none |
| `verification/coverage/LEDGER.json:44–99` | four entries `EXPLAINER:D-unnamed-2883898d`, `EXPLAINER:L-1`, `L-2`, `L-3` (all DEF/MIRROR, unscored) | Delete them. `coverage_check` completeness fails in both directions otherwise ("ledger entry names no canonical statement"). The scored denominator is unchanged. The unscored tally becomes DEF 7, MIRROR 0, SUM 1; no count is quoted anywhere. Their `line` fields (43/49/51/61) are already stale against the census lines (38/44/46/56). This is not checked |
| `verification/audits/manuscript/lean-manuscript-census.md:54, 60, 61, 68, 69, 121, 138` | current-state table rows and sentences naming the Explainer | Drop "the Explainer" (mutable audit note describing the census "at this commit"). Leave `:95`, the historical repair record. The probe pins only `'| continuous time (CT2) | 4 | current |'` (`:3041`) and `'| OI-N passive observation | 4 | current |'` (`:3127`) here; both are unaffected |
| `verification/programmes/oi-qm/PROGRAMME.md:626` | "`papers/GR.md`, `papers/Main.md`, the Explainer, and book chapters — publication-facing statements…" | Drop "the Explainer" (current-state list in a mutable programme index) |
| `verification/lean/edge_rigidity_probe.py` (CI step `edge_rigidity`, `.github/workflows/verify.yml:257`) | 58 lines name the Explainer | See §2.3 |

### 2.3 `edge_rigidity_probe.py`: site-by-site (plan default PD4; its pre-check is P6(c))

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
| 3273, 3476, 3596, 3737, 3831, 3928, 4054, 4156, 4259, 4351–4353, 4475, 4568–4570, 4691, 4833, 4949–4951, 5080, 5241, 5381, 5538, 5694, 5847, 6011, 6180, 6345, 6462, 6567, 6659, 6746, 6898 | negative (superseded identifiers, kernel-only module names, stale clauses) | Substitute the Introduction (`.md`, and `.tex` where the tuple has `.tex`). In 4691 and 4833 the `_rel in ('papers/GR.md','papers/Main.md') or …` exemption is unchanged, so the Introduction is held to the stricter non-GR/Main rule. Checked against the accepted text at P6(c) |
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

Under the alternative (drop rather than substitute in negative loops), the Introduction gets no
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
| `verification/coverage/LEDGER.json:3100` (the `route` of backlog rank 1, `GR:T-d-gauge-completeness-two-branch`; it contains "Main/Explainer/ledger are to be updated…", "NEXT: … then the Main/Explainer update", and further development notes) | mutable work-queue narrative (RC1) | **Default: unchanged.** The route text itself labels these notes historical ("The following independent-track development notes are historical"), and `coverage_check` does not read route text. Owner option: correct it forward in C2 by dropping "Explainer" from the pending-action sentences only, leaving the historical notes as they are |
| `.github/workflows/verify.yml:257` | CI step list | Unchanged; the probe still runs |
| `tools/*.py`, `papers/oi_lattice_code/*.py`, `verification/lean/bohr_frequency_probe.py:277` | glob/listdir scanners | No change. They stop seeing the Explainer by the move. `bohr_frequency_probe`'s `len(CORPUS) > 10` still holds (11 papers + the Introduction + book files) |

**Expected surviving `git grep -n -i explainer` hits after C2:**
- every file and line of §2.4, including `LEDGER.json:3100` (unless the owner takes the RC1
  forward-correction option);
- `papers/legacy/Explainer.md` itself;
- the stub `papers/Explainer.md`, and under M1 `papers/Explainer.tex` (in the pandoc title, from the
  stub heading). The `.pdf` may also match, as "Binary file … matches", if pandoc writes the title
  into uncompressed PDF metadata; run the re-grep with `git grep -I` to skip binaries, and check the
  `.pdf` by the build instead;
- `README.md:115`, the bullet (OQ2);
- `LICENSE`, if the owner keeps `Explainer.md` in the list (OQ5);
- the census act 12 note (`lean-manuscript-census.json:1014`) and the census note's historical
  `:95`.

Nothing else. In particular there is no hit in any other `papers/*.md` or `papers/*.tex`, in
`book/`, in `.zenodo.json` or in `verification/lean/`, and `git grep -n "companion Explainer"` is
empty.

### 2.5 Historical reproducibility (safeguard S1; RC3)

**Rule.** No receipt, seal record, certificate, legacy record, native-round record or retained object
is rewritten. Old `papers/Explainer.*` paths inside them stay as they are. Reproduction of a frozen
result runs on a materialized historical tree, never on HEAD.

Every place an old Explainer path occurs in immutable or historical evidence was audited (review §6,
spot-checked here). **Nothing that re-verifies a certified result reads the path at HEAD**, apart
from the live guard C2 edits:

| Location | Reads the path at | Effect of the move |
|---|---|---|
| `verification/receipts/*.json` (53) and `verification/seals/` | — | No Explainer path occurs (`git grep -l -i explainer` finds none) |
| `tools/v3_verifier.py --receipts` | git objects at each receipt commit. G13 (`records_unchanged`, `v3_verifier.py:979–1001`) compares only the record directory and seal records at HEAD | None. C2 touches no record directory |
| Native record preregistrations: CC-1/CC-2 `:35–37`, A45 `:32–34` (`execution M papers/Explainer.{md,tex,pdf}`), A45 `:151` (blob pin `b0926875…`) | their own commits | Immutable under G13; preserved as written |
| Legacy records, e.g. `verification/certificates/A12P.json:23–29`, and the `h-d`/`lemma-24-1b` blob pins | — | Kept blob for blob by `legacy-records`. The V2 certificate verifier is retired, so nothing re-reads them at HEAD |
| A45 `controls.py`, CONSC-2 `controls.py` | `git show <commit>:<path>` (A45 `:207–212`; CONSC-2 `:364–387`) | Safe: they read history, not the working tree |
| CC-1/CC-2 `controls.py` | a working-tree directory (`--repo` defaults to `.`, CC-1 `:388`; `--base DIR`) | Already non-reproducible at HEAD independently of the move, because later rounds changed their governed sources. The recorded recipe runs on materialized D/E trees (`controls.py --check E` at the candidate, CC-1 `result.md:54`). The move adds no new break. Not run by CI |
| `verification/audits/provenance-errata/check_errata.py` | E1: citing-record blobs at HEAD (five frozen round files); E3: `papers/Explainer.*` in historical trees | Safe; not run by CI |
| Evidence-retention archive (development branches; not on `main` at 687e885b): `reproduce.py`, `check_objects.py`, `objects/manifest.json` | `reproduce.py` checks the attested commit out as a detached worktree; object paths are inside reconstituted historical trees | Safe. P7(c) re-checks the mapped citing files at the cut base |
| `verification/lean/edge_rigidity_probe.py` | **HEAD** | The one live reader; edited in C2 (§2.3) |

**C2 commit-message text (required, RC3).** C2's message states:
- "No receipt, seal record, certificate, legacy record, native-round record or retained object is
  modified; old `papers/Explainer.*` paths in them are preserved."
- "Frozen controls that read `papers/Explainer.*` (CC-1, CC-2, A45, CONSC-2) are reproduced only on
  materialized historical trees (`git -c gc.auto=0 -c maintenance.auto=false worktree add --detach
  <dir> <D|E>` in an independently recoverable clone, or `git archive <D|E>`), never on HEAD."
- "`papers/Explainer.md` becomes a redirect; the superseded text is at `papers/legacy/Explainer.md`.
  Review the rename with `git diff -B -M` and history with `git log --follow`."

It also carries the attribution lines that apply at the time.

**Checkpoint.** The `v3-receipts` and `legacy-records` gate steps (§4.1(2)) measure "no record
rewritten". The §2.4 re-grep measures "old paths preserved": every hit in a frozen location
survives unchanged. This covers the §A.41 invariant→checkpoint requirement.

***

## 3. What "preserve for provenance" means

### 3.1 Options

| | (A) keep at `papers/Explainer.md`, notice only | (B) move to `papers/legacy/Explainer.md`, notice | **(B′) B plus a redirect stub at `papers/Explainer.md`** (approved: OD2 + OD7) | (C) delete; history and a tag only |
|---|---|---|---|---|
| Preserves content and history | yes | yes (`git log --follow`; one-line notice and 8 link targets changed) | yes. `--follow` was verified in a scratch repository even with the stub at the old path in the same commit (review §4) | history only |
| "Marked superseded" in the tree | yes | yes | yes, at both paths | no file to mark |
| "Stop maintaining" actually holds | **no**, see 3.2 | yes, with one residual (3.2) | yes. The stub is inert and passes every check unmodified (3.2) | yes |
| External deep links to `papers/Explainer.md` | kept | break | **kept** for the `.md` (landing on the stub), and for the `.pdf` under M1 | break |
| Repo footprint (§A.28) | 1 md + tex + pdf, all maintained | 1 md, frozen | 1 frozen md + a 3-line stub (+ its tex/pdf under M1) | none |

(A) fails the owner's "stop maintaining it as an active manuscript", for the reasons in 3.2. (C)
fails "mark the Explainer as superseded" and is not "controlled replacement". (B) breaks external
access. **(B′) is the approved shape** (OD2, OD7). `papers/` already holds subdirectories (`oi_lattice_code/`, `main_repro/`), so the
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

**The redirect stub (S2).** The stub sits at `papers/Explainer.md`, so every `papers/*.md` scanner
sees it. The review applied the move, the census and LEDGER deletions and the stub to an archive
extract at 687e885b, and ran each tool once, unmodified (review §7):
- `staleness_check`: OK ("12 matched, 1 unstamped"; a missing `.tex` is reported, not failed). Under
  M1 the stub's `.tex` is stamped, so it is matched.
- `voice_check` and `voice_scope_test`: OK. `dependency_label_check --strict`: OK.
- `lean_manuscript_census`: OK. It reads only `kernel:` spans and `OIBridge/*.lean` paths, and no
  family names the stub.
- `proof_census`/`coverage_check`: OK, 124 canonical statements. The stub has no statement heading,
  so no LEDGER row is demanded.
- `architecture_check`, `citation_check`: OK (negative patterns only).
- `claims_check`, `duplicate_check`, `baseline_label_check`: OK.
- `bohr_frequency_probe` F8: PASS.
- `build.sh:84`: builds the stub (M1). Not run in the dry run (no pandoc); behaviour read from code.

A formal exclusion would have to be written into at least nine places, because the repository has no
single manuscript-file list: `build.sh`, staleness, voice + `voice_scope_test`, dependency-label,
census, `proof_census`, architecture, citation, bohr, plus the three whole-tree walkers. **No
exclusion is proposed** (§A.28). OD7's "excluded from active checks if possible" is met in
substance: the checks run over the stub and find nothing to check. The stub's inertness is a
checkpoint (§4.1(8)), so it cannot quietly gain checkable content.

**Should a superseded file pass voice/claims checks?** Under (B) it is outside the voice scope by
construction: `voice_check` scans the manuscript only, and the file is no longer manuscript. It
stays inside claims/duplicate, which it currently passes. Keeping it passing is free while it is
frozen, so exclusions are not needed now.

### 3.3 The two notices (§A.27 exception)

**(a) The legacy file's standing notice.** It replaces line 3 of `papers/legacy/Explainer.md`. One
line. It states the standing fact and nothing about history:

> `*[Superseded document, kept for provenance and not maintained. The current presentation of the framework is the Introduction paper ([`../Introduction.md`](../Introduction.md)), the technical papers and the book; where this text differs from them, they govern.]*`

Checks on the wording:
- None of `voice_check.py`'s PATTERNS matches it: "withdrawn", "earlier draft", "formerly", "now
  states", "previously said", "no longer …" and "has since been …" are all absent.
- There is no date and no "was" or "earlier".
- Under option (A) the link would read `Introduction.md` (no `../`).
- "kept for provenance" is used rather than "kept unchanged", because PD2 edits 8 link targets.
- The review confirmed compliance with §A.27/§A.30 (review §4).

**(b) The redirect stub at `papers/Explainer.md`.** This is the review's text (§7), which passed
`voice_check` in its dry run. The whole file is:

```markdown
# The Incompleteness of Observation: Explainer

*[Superseded document. The current introduction to the framework is the Introduction paper ([`Introduction.md`](Introduction.md)). The superseded text is kept for provenance, unmaintained, at [`legacy/Explainer.md`](legacy/Explainer.md).]*
```

It deliberately has no "moved", "formerly", "now" or date: those narrate history (§A.27/§A.30), and
"formerly" is also a `voice_check` pattern. The stub carries no `kernel:` span, no statement
heading, no `*.py` citation and no `---` rule (AGENTS build recipe).

***

## 4. Checks after the change, and a dry-run recipe

### 4.1 Required to pass at C2

1. **Build.** Run `sh ./build.sh Main`, `sh ./build.sh --book` and, under M1, `sh ./build.sh Explainer` (the stub; one page). The Introduction is built in C1.
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
     `reversible implementation locality` for R7-MSP, or `qm requires oi` for R7-OINN (a reading it forbids: only core containment is proved). The
     corresponding R7 check must fail. This shows the §2.3 substitution is live.
   - (iii) Restore one deleted LEDGER entry in a copy. `coverage_check.py --ledger <copy>` must
     fail with "ledger entry names no canonical statement".
   - (iv) The retargeted `_a12p_m3` runs inside the probe and must be caught. R7-A12P passes only if
     the mutant is rejected.
5. **Re-grep** (§A.25 step 6). `git grep -n -i explainer` must equal the expected survivor list of
   §2.4, as revised for RC1 and the stub. Record the surviving count in the PR description. Separately, `git grep -n "companion
   Explainer"` must have zero hits.
6. **Mirror.** `diff <(sed -n 9p book/bibliography.md) <(grep -F 'The Observational Incompleteness
   Framework*. Zenodo' book/The-Incompleteness-of-Observation-FULL.md)` must be empty (one match in FULL at
   687e885b).
   `mirror_check.py` covers chapters; the bibliography line is checked by this diff.
7. **Legacy-file invariant (RC4; R13).** With the stub at the old path, GitHub's default diff shows a
   full rewrite plus a 1059-line addition, so "only line 3 and 8 link targets changed" cannot be seen
   there. The invariant is measured mechanically:
   - `git -c gc.auto=0 -c maintenance.auto=false diff --no-index <(git -c gc.auto=0 -c
     maintenance.auto=false show <base>:papers/Explainer.md) papers/legacy/Explainer.md` shows
     exactly **7 changed lines**: line 3 (the notice) and lines 682, 686, 763, 781, 818, 822. Those six
     lines hold the 8 link targets. Each change must be the expected replacement and nothing else:
     a script compares every `-`/`+` pair against the list of §2.1. The review's "9 changed lines"
     counts link targets (1 + 8). Counted by line it is 7; either count is fine provided the script
     checks each pair;
   - the file length stays 1059 lines;
   - `git log --follow --oneline papers/legacy/Explainer.md` reaches the history before C2;
   - `git diff -B -M --stat <C1> <C2>` shows `papers/{ => legacy}/Explainer.md` with a small count,
     plus a new `papers/Explainer.md`. Reviewers review C2 under `-B -M`.
8. **Stub inertness (S2).** `papers/Explainer.md` equals the §3.3(b) text byte for byte (sha256
   recorded in the PR description). Its grep for `kernel:`, `^\*\*(Theorem|Lemma|Definition|Proposition|Corollary)`, `` `[A-Za-z0-9_]+\.py` `` and the `voice_check` PATTERNS is empty. Under M1, `staleness_check` reports
   the stub matched.

### 4.2 Dry-run recipe (local, bounded, no shared-store risk; §A.40)

```sh
S=S
G="git -c gc.auto=0 -c maintenance.auto=false"
# 1. an independent tree from the candidate head (C1 applied); no linked worktree, no fetch into the shared store
mkdir -p $S/retire/dry && cd <checkout-with-C1> && $G archive <C1-sha> | tar -x -C $S/retire/dry
cd $S/retire/dry
# 2. apply C2 by script (git mv is replaced by mv in the archive copy)
mkdir -p papers/legacy && mv papers/Explainer.md papers/legacy/Explainer.md && rm -f papers/Explainer.tex papers/Explainer.pdf
#    write the §3.3(b) stub to papers/Explainer.md (M1: then sh ./build.sh Explainer where pandoc/xelatex exist)
#    … the line-3 notice, the 8 link targets, and the §2.2/§2.3 edits, each as an exact old→new replacement that must match once
# 3. bounded local checks (each once)
python3 -m py_compile verification/lean/edge_rigidity_probe.py tools/*.py
for t in staleness_check voice_check voice_scope_test claims_check duplicate_check dependency_label_check coverage_check lean_manuscript_census; do
  python3 -I tools/$t.py $( [ $t = dependency_label_check ] && echo --strict ) || echo "FAIL $t"; done
python3 -I papers/oi_lattice_code/mirror_check.py; python3 -I papers/oi_lattice_code/citation_check.py; python3 -I papers/oi_lattice_code/architecture_check.py
(cd verification/lean && python3 -I edge_rigidity_probe.py | tail -40 && python3 -I bohr_frequency_probe.py | tail -5)
# 4. countercontrols 4.1(4)(i)–(iii) on throwaway copies; the re-grep 4.1(5) with grep -rni (no .git in the archive);
#    the 4.1(7) line diff against the base blob (git show <base>:papers/Explainer.md from the repo, not the archive); the 4.1(8) stub checks
# 5. history checks of 4.1(7) (--follow, -B -M) need a repository: run them in CI or in an independent scratch clone, never by gc-ing or re-initializing the shared store
```

- The full gate, including the history-dependent steps and `lean-axioms`, runs in CI on the
  guiding draft PR (automatic `pull_request` run).
- An exact-head attestation is needed only if the owner makes this a native round (PD5).
- If any local step is slow, stop and leave it to CI (§A.40).

***

## 5. Decisions and risks

**Recorded owner decisions (2026-10-26).** OD1–OD7 at the head of this document: strategy approved
conditional on acceptance; legacy move after acceptance; superseded notice; Main:66 →
[Substratum §6.2]; one PR, two commits; S1 historical reproducibility; S2 redirect.

**Remaining owner decisions** (review §10):

| ID | Decision | Recommendation |
|---|---|---|
| OQ1 | M1 (build and commit the stub's `.tex/.pdf`) or M2 (no stub artifacts; one skip in `build.sh`) | **M1**: no tool change, the old `.pdf` URL keeps resolving, and staleness guards the pair |
| OQ2 | What `README.md:115` points to: the stub or `papers/legacy/Explainer.md` | Point to the legacy file. The stub serves external links; the README should lead straight to the content |
| OQ3 | Whether the holography objection (Explainer:694–699) goes into book Appendix C (MIGRATION-r2 row 23a) | Default (c), not migrated. If yes: a new Appendix C section from primary sources, without :699's list |
| OQ4 | The optional book items: the ch03 lineage paragraph, the navigation table (waits for #931), the double-difference display from Main:232–238 | None by default |
| OQ5 | LICENSE wording; whether to fix the pre-existing gaps (Computation missing from `bibliography.md:9`/FULL and `.zenodo.json:26`; five papers missing from LICENSE; `.zenodo.json`'s `cc-by-4.0` while `LICENSE:27–29` names no manuscript licence) | The generalized LICENSE wording of §2.2. Gap fixes only on an explicit owner instruction, in C2 or separately |
| OQ6 | Whether to add the Introduction to README's "Core papers" table (`README.md:68–78`) and to the core list at `README.md:45` | Owner's wording. The "Start here" row of §2.2 is part of C2 either way |

**Plan defaults.** These are not open owner decisions per review §10, and are adopted unless the
owner objects:

| ID | Default | Reason |
|---|---|---|
| PD1 | The legacy notice text of §3.3(a) and the stub text of §3.3(b) | Both review-confirmed compliant (OD3) |
| PD2 | Fix the 8 relative link targets in the legacy file | Otherwise they break silently; measured by §4.1(7) |
| PD3 | `build.sh:12` without a count | The count changes with the stub and the Introduction |
| PD4 | Probe: substitute the Introduction in negative loops; drop it from positive ones | Pre-checked at acceptance (P6(c)) |
| PD5 | Ordinary reviewed PR, not a native V3 round | C2 touches no frozen record or open round's governed paths (re-checked at P7(b)) |
| PD6 | `LEDGER.json:3100` left unchanged | Route text labels its notes historical; `coverage_check` does not read it |

**Risks**

| ID | Risk | Mitigation |
|---|---|---|
| R1 | External deep links and citations to `papers/Explainer.md` | **Mitigated by the stub (B′).** Under M1 the `.pdf` URL also resolves. Zenodo keeps older versions |
| R2 | The legacy file keeps its (d) statements (e.g. :373 every-horizon form, :745 "unique algorithm", :771 "nothing to tune"), and a reader may cite them | The standing notice and the stub say the maintained sources govern. Rewriting is excluded by policy, and annotating would be assert-then-qualify (§A.30) |
| R3 | A future rule in claims/duplicate/baseline-label flags the frozen file or the stub | §3.2 residual: a narrow exclusion with an updated self-test, owner-approved, at that time |
| R4 | Probe edits weaken coverage (positive checks lose one file; one mutation retargeted) | Substitution keeps negative coverage on the Introduction; m3 retargeted to ch01; countercontrols §4.1(4) |
| R5 | Partial landing: census edited without the probe's `_a12p_reg` set (9005–9010), or the reverse | Both in C2; R7-A12P fails in CI if they diverge |
| R6 | Frozen controls (CC-1, CC-2, A45, CONSC-2) and historical reproduction | §2.5: no record rewritten; reproduction only on materialized historical trees; stated in the C2 message |
| R7 | Bibliography ↔ FULL mirror drift | Same-bytes edit plus the diff in §4.1(6) |
| R8 | `verification/README.md:1959–1960` reads as present-tense state ("OI-N is narrated … one of the Explainer") | Default: leave it as round history. Option: forward correction of that one sentence |
| R9 | Pre-existing list and licence gaps (OQ5) | Flag on the PR; fix only on instruction |
| R10 | Shared object store: an auto-gc during the work | Every git command with `-c gc.auto=0 -c maintenance.auto=false`. The dry run uses `git archive`; history checks run in CI or in an independent scratch clone |
| R11 | #931 still open: the book's B.7.6 display (`appendix-b:454–455` = `FULL:6243–6244`) | Not a precondition. Retirement removes the Explainer site; the book sites need their own correction |
| R12 | The Introduction's scope does not cover the Explainer's §§4–6 (ħ, cosmology, SM) | Accepted by design (OUTLINE-r3/r4). The book and GR carry it. The README "Start here" order makes the route explicit |
| R13 | Review legibility: with the stub at the old path the default diff shows a full rewrite | §4.1(7): an exact line diff against the base blob, `--follow`, and review under `-B -M` |
| R14 | Zenodo: the concept DOI resolves to the latest version, which under M1 carries the stub PDF and the legacy `.md` but no full Explainer PDF | Earlier versions keep the full PDF. `papers/legacy/` is not `export-ignore`d, so the legacy text ships, consistent with preservation. `.zenodo.json:26`'s "Sources and built PDFs are both included" stays true of the listed companions |
| R15 | Drift between this plan (687e885b) and the cut base | P7 |
| R16 | A probe mutation or self-test reading the Explainer | Only `_a12p_m3` does (review §8); retargeted to ch01 |
