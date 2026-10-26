# Independent review: Explainer migration audit and retirement plan

Under review: `S/paper/retire/MIGRATION.md` and `S/paper/retire/RETIREMENT.md`.
Base: `main` `687e885b1cfd24d6f17eee439101afc8acf07015` (worktree `S/paper/mainwt`, clean).
`S` = `S`.
Read-only toward the repository. Every git command ran with `-c gc.auto=0 -c maintenance.auto=false`.
The dry runs used a `git archive` extract in `S/paper/retire-review/dry/` and an independent scratch
repository in `S/paper/retire-review/followtest/`. Neither touches the shared store.

Owner decisions of 2026-10-26 are folded in. They approve the strategy conditional on the
Introduction's acceptance, approve the `papers/legacy/` move after acceptance, require a superseded
notice, approve Main:66 → [Substratum §6.2], and fix the shape at one PR with two commits. They also
add safeguards S1 (historical reproducibility) and S2 (a redirect at `papers/Explainer.md`).

## Verdict: ACCEPT WITH CHANGES

The audit and the plan are accurate on almost every point I checked:
- the 58 probe sites and their aliases;
- the census anchors, the anchor counts per family and the comma fix;
- the LEDGER entries and tallies;
- which scanners are recursive and which are not;
- the classification of frozen and legacy records;
- the D-gauge coverage;
- the Main:66 repoint.

What needs changing:
- **Coverage gap.** One dependent is in neither list (RC1).
- **Missing classification.** One unique Explainer section has no class (RC6).
- **Measurement gaps.** Several invariants are stated with no checkpoint (RC4, RC5).
- **New owner safeguards.** The plan does not yet carry S1 and S2. S1 is satisfied as things stand
  and needs only a recorded audit and a recipe rule (RC3). S2 can be met with **no tool exclusion
  at all**, and a dry run confirms it (RC2).

***

## 1. MIGRATION completeness (check 1)

### Confirmed (migration)

These rows were spot-checked against the cited sources at `687e885b`. Each holds in substance.

| Row | Claim checked | Result |
|---|---|---|
| 3 | Definition and Lemmas 1–3 carried at `Main.md:44–56`; C1–C3 at `:72–80` | carried (content, not just the title) |
| 7 | (d): Explainer:135/:169/:272 attach P-indivisibility to C1 alone | Explainer:161 itself states the separate non-permutation hypothesis. `Main.md:119` (hypothesis) and `:719` (C1 row: "sufficient first-step witness, not an equivalence") contradict :135/:169/:272. **Holds.** Nit: the hypothesis is at :119, not :118 |
| 8 | (d): $I\ge I_0(1-k\tau_S/\tau_B)$ | `appendix-b-derivations.md:424`: "holds only as a leading-order estimate". **Holds** |
| 14c | (d): every-horizon form, "Both directions are the foundational paper's own theorems", "is retired" | `Main.md:522` (some order k, every K ≥ k+1), `:608` (the converse is prose), `:610`. **Holds** |
| 15 | (d): Explainer:411 says the horizon satisfies "all conditions" | `GR.md:52`: C4 "**Not presently discharged**". **Holds** |
| 17 | D-gauge walkthrough fully carried | Statement by statement: the problem → `GR.md:170`. Bohr completeness → `GR.md:172–174` = B.7.5a `appendix-b:434–436`. The dimensional obstruction → `GR.md:176` = `appendix-b:438`. The two-branch theorem under H-BG, the `BGIntegerClassification` refutation with the (0,1,4,10,12,17)/(0,4,6,9,16,17) rulers, and the **C₄ ring of SM Prop. 20 in the reflection branch with D_s = diag(1,−1,1,−1)** → `GR.md:178–182` = `appendix-b:444–448` (the C₄ sentence is verbatim at GR:182 and appendix-b:448; also FULL.tex:27522). The double-difference structure and the α_i+β_k gauge → `Main.md:232–238`; the book has the "phase-coboundary" clause. **Nothing Explainer-only. Confirmed** |
| 21 (i) | WHIM vs `GR.md:528` "**not** closable by undetected cluster baryons" | **Holds** |
| 21 (ii) | 1/α₁ is an input | `SM.md:1259` "**E**ᵃ (fixes δ₀)". **Holds** |
| 22 | Lineage: the Cusa, Spinoza, Worrall and Hofstadter material is in ch03 | ch03 has Cusa ×4, Spinoza ×4, Worrall ×2, Hofstadter ×2. Kant, Nāgārjuna, Whitehead, Falque and Advaita appear nowhere else in the corpus. Claim 4 "local" (Explainer:608) against `Main.md:392` (ontic parameter dependence), and the Gödel→Wolpert "chain" against `ch03:214`. **Holds** |
| 23 (iii) | "SM gauge group forced uniquely" vs `glossary.md:75` (conditional on H-link) | **Holds** |
| 24 | "unique algorithm" vs `ch03:10` ("a representation, explicitly non-unique") | **Holds** |
| 28 | "twenty-two zero-parameter" (:862) vs `SM.md:1298` (7 of 22 are S) | **Holds** |
| 30 (i), (ii) | :892 "without recurrence" vs `Main.md:141`; :930 "No additional axiom required" vs `Main.md:726` (conditional on (EM)) and `:740` | **Holds** |
| 33 | Subtleties 1–4 carried at GR 162/164/178/128–134 | carried |

Counts: 34 rows, and 18 rows carry NEW items (rows 2, 6, 7, 11, 16, 18–30). Confirmed.

### Findings

**F1 (RC6). Row 23 leaves one unique section unclassified.** This is the FAQ answer
"Doesn't holographic physics show that spacetime comes from entanglement?" (Explainer:694–699).
- What it contains: Ryu–Takayanagi read as geometry-first, with the area law coming from the
  boundary mode count; van Raamsdonk; the claim that the two orderings break down in different
  places.
- Where the corpus covers part of it: only ER=EPR, at `Substratum.md:236–242`. Ryu–Takayanagi and
  van Raamsdonk appear in no maintained `.md`, and book Appendix C (`appendix-c-objections.md`,
  C.2–C.12) has no such objection.
- What MIGRATION says: it notes the zero hits but still files the whole FAQ as (a).
- Why it matters: the owner asked for unique material to be audited. This is the one substantive
  objection-response that leaves the corpus with the Explainer.
- Proposed class: **(c)** by default, not essential to the Introduction. Owner option: Appendix C,
  rewritten from primary sources.
- What must not be carried: :699's list of consequences, which contains (d) items. "produces the
  observed vacuum energy" conflicts with `GR.md:360`. "the SM gauge group with its coupling
  strengths" is unconditional, against `glossary.md:75` and `SM.md:1259`.

**F2 (RC7). The supersession of the summary tables is conditional, and MIGRATION states it as
settled.**
- The Introduction's Appendix A is still an outline item (`OUTLINE-r4.md:324–336`).
- The Alt-L variant folds it into §3 (`OUTLINE-r4.md:342`).
- The default scope is about 15 kernel-backed rows.
- MIGRATION §3 should read: superseded by the accepted Introduction's kernel map (Appendix A, or its
  Alt-L §3 table) for the in-scope rows, with the ħ/ε/S_BH rows carried by `ch07-gravity.md:292–309`
  and B.4.
- P1/P6 should confirm that the kernel map exists in the accepted text.

The rest of §3 holds: no row text is reused, no "every link" sentence, and the B.7.6 #931
precondition for any book table.

**F3 (nit, accuracy of the (d) list).**
- Rows 2 and 19 cite `GR.md:362` for "does not explain *why* ρ ∼ H²/G". That sentence is at
  **`GR.md:360`**; :362 is "Quantum corrections to gravity".
- `GR.md:358` itself lists the CC dissolution as "cumulative evidence for the ordering", "sits at
  ρ ∼ H²/G … without fine-tuning".
- So the (d) for :22 should rest on the superlative ("strongest piece of existing evidence") and
  §A.23. The (d) for :549/:551 should rest on "predicts the observed value", against GR:360.
- As written, "the value the framework expects" is close to GR:358. Over-broad (d) items matter
  because P6 hands the list to the Introduction's reviewers as a must-not-carry checklist.

**F4 (nit). Anchor revision.** MIGRATION uses OUTLINE-r2 claim IDs, but the accepted outline is r4.
- r4 keeps the claim IDs stable (OUTLINE-r4:61–62 "section numbering … kept").
- r4's "What the paper must not inherit" list (:79–93) equals REVIEW §3.
- So nothing breaks, but the header should name r4 as the governing revision.

**Essential material dropped?** None, other than F1, which is an owner choice.
- The D-gauge walkthrough is fully carried.
- The appendix tables are superseded, with the condition F2 adds.
- The lineage is (c) with a (d) thesis. The decompression section and the Rigidity Test are (d).

## 2. Main.md:66 → [Substratum §6.2] (check 2)

**Confirmed.**
- `Substratum.md:406` is the heading "### 6.2 The ontological hierarchy".
- `Substratum.md:408` reads: "**Conservation laws** are emergent: energy conservation (Noether) is
  what information conservation (bijectivity) looks like in the emergent quantum description."
- This is the same identification as Explainer:802, at the same (interpretive) strength.
- Main's citation form is `[Substratum §3.3]` (2 uses).
- Main:66 is a Remark, which `proof_census` does not ledger, so no LEDGER fingerprint moves.
- "companion Explainer" occurs only at `Main.md:66` and `Main.tex:545–546`, and no probe pins the
  sentence.

## 3. RETIREMENT completeness (check 3)

`git grep -l -i explainer 687e885b` gives 57 files, all accounted for except one line:

**F5 (RC1). `verification/coverage/LEDGER.json:3100` is in neither list.**
- The file has 13 hit lines, not 12.
- Line 3100 is the `route` of backlog rank 1, `GR:T-d-gauge-completeness-two-branch`. It reads
  "Main/Explainer/ledger are to be updated…", "NEXT: … then the Main/Explainer update", and similar.
- `coverage_check` does not read route text.
- Proposed disposition: list it in §2.4 as a mutable work-queue narrative left unchanged, or
  correct it forward (drop "Explainer").
- Either way, §2.4's "Nothing else" survivor list and the §4.1(5) re-grep expectation are currently
  wrong.

### Confirmed (retirement)

- **Probe.** 58 lines name the Explainer. The plan also covers every alias line, which a grep for
  "explainer" does not find:
  - `_oinn_expl`/`_oe`/`_oinn_epar` at 3090–3112;
  - `_A11P_EXPL` at 8563, 8666–8667, 8903, 8917, 8925, 8937, 8956, 8980, 9041–9044;
  - `expl=`/`_ex` at 8882–8892.
- **Summary counts.** Measured at 687e885b: `_qsum`, `_ssum` and `_pqual` each occur 1/1/1/1/2 in
  Main/Explainer/ch01/ch19/FULL, total 6. So `_qcount == 6 → 5` and `_scount`/`_qcount2 → 5` are
  right, and `_pqual`'s `count == 2` applies to FULL alone.
- **The m3 retarget to ch01.** ch01 carries 'each maximal among uniform actions of its kind' once.
  The R7-A12P description's "mutation-tested twice" stays true (m2 on Main, m3 on ch01).
- **R7-A12P registry.** `_a12p_census` (9005–9010) requires `papers/Explainer.md` among the act 12
  family's files, so it must change in the same commit as the census JSON (R5).
- **Census anchors.** The seven objects are at 289–292, 402–405, 436–439, 793–796, 971–974,
  997–1000 and 1296–1299.
  - Only OI-N's is last in its array, so only the comma at 792 needs fixing.
  - The non-Explainer anchors that remain per family are **5, 5, 7, 5, 3, 5, 5**, so every family
    keeps at least 3.
  - The probe's `len(manuscript) >= 5` checks for CT2 and OI-N still hold.
  - The `manuscripts` key (:6) has no consumer.
  - The note lines are 298, 411, 453, 551, 573, 798 and 1014. Nit: give all six current-state line
    numbers, not only 298 and 798.
- **The census-note pins** `| continuous time (CT2) | 4 | current |` and `| OI-N passive
  observation | 4 | current |` are in the modules column, so they are unaffected. No probe or tool
  literal pins any Explainer-bearing note substring.
- **LEDGER.** The four entries are at 44–99. Unscored tallies go from DEF 8 / MIRROR 3 / SUM 1 to
  DEF 7 / MIRROR 0 / SUM 1. No count is quoted anywhere.
- **Other dependents, line by line:**
  - `verification/README.md`: 15 lines, matching the plan;
  - `lean-manuscript-census.md`: 54, 60, 61, 68, 69, 95, 121, 138;
  - `errata.json`: six lines;
  - `PROGRAMME.md:626`, `README.md:115`, `book/README.md:110`, `LICENSE:28`, `.zenodo.json:26`;
  - `bibliography.md:9` is byte-identical to `FULL.md:6793`, and `FULL.tex:29795` is the
    generated copy.
- **Alternate reference forms.** These have no hits outside the Explainer: the title, "Rigidity
  Test", "Decompression Algorithm", "Worst Prediction", the source sha `e1167acd`. "older overview"
  hits only README:115.

## 4. Legacy move versus in place (check 4)

**Confirmed by code and by a dry run.** The dry run applied the move, the census and LEDGER
deletions, and the stub of §7 to an archive extract at 687e885b, then ran the tools once each.
- **Non-recursive scanners:**
  - `staleness_check.py:28`, `voice_check.py:46` and `dependency_label_check.py:226` use top-level
    `os.listdir`;
  - `lean_manuscript_census.py:78`, `proof_census.py:82`, `architecture_check.py:18`,
    `citation_check.py:17` and `bohr_frequency_probe.py:277` glob `papers/*.md`;
  - `build.sh:84` loops over `papers/*.md`.
  - A file in `papers/legacy/` escapes all of them.
- **Whole-tree walkers.** `claims_check.py:103`, `duplicate_check.py:31,49` and
  `baseline_label_check.py:37,90` use `os.walk` and still scan the legacy file. They pass: in the dry
  run, claims, duplicate and baseline-label were all OK.
- **Relative links.** There are 8 relative link targets (682, 686, 763×2, 781×2, 818, 822), so D4's
  `../` prefix is needed.
- **History.** `git log --follow papers/legacy/Explainer.md` follows the rename. This was verified
  in a scratch repository, git 2.43, **including when a new stub occupies the old path in the same
  commit**.
  - In that case the default `git show --stat` reports a full rewrite of `papers/Explainer.md` plus
    a new file.
  - Only `-B -M` shows `papers/{ => legacy}/Explainer.md | 2 +-`. See RC4.
- **The notice text in §3.3 is compliant** with §A.27's standing-notice exception and §A.30.
  - It states standing ("Superseded document, kept for provenance and not maintained … they
    govern").
  - It has no date, no "was/formerly/withdrawn", and none of the `voice_check` PATTERNS.

## 5. Ordering and gates (check 5)

**Confirmed.**
- P1 requires independent scientific and editorial ACCEPT at the landing SHA before C2 is cut.
- C2 touches no frozen record. None of the files it edits lies under any of the 53 receipt record
  directories (G13 prefix rule) or in `legacy-records.json`:
  - `Main.md`/`.tex`/`.pdf`;
  - README, book README, bibliography/FULL;
  - `.zenodo.json`, LICENSE, `build.sh`;
  - the census JSON and census note, LEDGER, `PROGRAMME.md`, `edge_rigidity_probe.py`.
- Push triggers: `verify.yml` runs on `pull_request` and on `push` for main only. The other `push`
  workflows are path-filtered to unrelated directories.

**F6 (RC5). Ordering refinements.**
- (a) The D7 pre-check needs to happen during review. It asks whether the Introduction legitimately
  needs any identifier that the substituted negative loops forbid (e.g. 3273: `Route B`,
  `DerivedOI`; 4691/4833 exempt only GR/Main). Move it into P1/P6, so that C2's guard
  substitution cannot invalidate an accepted text after acceptance.
- (b) Add **P7, re-derivation at the cut base.** Main will move, so the change list is valid only at
  687e885b. At the base C2 is cut from, re-run the `git grep -i explainer` dependency census
  (§A.25 step 1) and reconcile the line numbers. In particular check that:
  - no open native round with a designated `F` governs the census JSON, the LEDGER, the probe or
    the other C2 paths;
  - if the evidence-retention archive has landed on main (it exists on development branches and
    AGENTS §A.42 describes its gate step), no file C2 edits is a mapped citing file, since
    `check_retention.py` requires an unchanged citing blob. In the branch copy I read, none is.

## 6. Owner safeguard S1: historical reproducibility (RC3)

Every place an old Explainer path occurs in immutable or historical evidence was checked. **No
re-verification reads the path at HEAD**, apart from the live guard the plan already edits.

| Location | Reads at | Effect of the move |
|---|---|---|
| `verification/receipts/*.json` (53), seal records | — | No Explainer path occurs |
| `tools/v3_verifier.py --receipts` | `verify_round(repo, Q)` on git objects at the receipt commit; G13 compares only the record directory and seal records at HEAD (`v3_verifier.py:979–1001`) | none |
| Native record preregistrations: CC-1/CC-2 `:35–37`, A45 `:32–34` (`execution M papers/Explainer.{md,tex,pdf}`), A45 `:151` blob pin `b0926875…` | their own commits | Immutable under G13. They stay as written and must not be rewritten |
| Legacy records, e.g. `certificates/A12P.json:23–29` (contributions), `h-d`/`lemma-24-1b` blob pins | — | Kept by `legacy_records_check` blob for blob. The V2 certificate verifier has been retired, so nothing re-reads them at HEAD |
| A45 `controls.py`, CONSC-2 `controls.py` | `git show <commit>:<path>` (A45 `:207–212`, CONSC-2 `:364–387`); self-tests read only the record directory | safe |
| CC-1/CC-2 `controls.py` | **working-tree directories**: `--repo` defaults to `.` (`:388`), `--base DIR` | At HEAD they already fail independently of the move, since later rounds changed their governed sources. Reproduction requires materialized trees at D/E, which is the recorded recipe ("`--check E` at the candidate", CC-1 `result.md:54`). The move adds no new break. Not run in CI |
| `provenance-errata/check_errata.py` | E1: the citing record's blob at HEAD. Citing records are five frozen round files. E3: `papers/Explainer.*` read in historical trees | safe; not run in CI |
| Evidence-retention archive (branch only, not on main at 687e885b): `reproduce.py`, `check_objects.py:197`, `objects/manifest.json:15853` | `reproduce.py` checks out the attested commit as a detached worktree (`:224–230`). Object paths are inside reconstituted historical trees | safe |
| `edge_rigidity_probe.py` | **HEAD** | the one live reader; edited in C2 (§2.3) |

Required: add this table, or a summary of it, to RETIREMENT as §2.5. Also state in C2's message:
- frozen controls are reproduced only on materialized historical trees (`git worktree add --detach
  <dir> <D|E>` or `git archive`), never on HEAD;
- no receipt, seal, certificate or record is rewritten.

## 7. Owner safeguard S2: a redirect at `papers/Explainer.md` (RC2)

**Which tools see a stub at `papers/Explainer.md`, and how it fares:**

| Tool | Sees the stub? | Result in the dry run, unmodified |
|---|---|---|
| `build.sh:84` (full build) | yes: **it would build** `papers/Explainer.tex/.pdf` from the stub | not run (no pandoc); behaviour read from code |
| `staleness_check` | yes | OK, "12 matched, 1 unstamped". Absence of a `.tex` is reported, not failed (`staleness_check.py:58–65`) |
| `voice_check`, `voice_scope_test` | yes | OK, OK |
| `dependency_label_check --strict` | yes | OK |
| `lean_manuscript_census` | yes, but it reads only `kernel:` spans and `` `OIBridge/*.lean` `` paths | OK, with the census anchors removed. No anchor is demanded, because no family names the stub |
| `proof_census` → `coverage_check` | yes, but the stub has no statement headings | OK (124 canonical statements); no LEDGER row demanded |
| `architecture_check`, `citation_check` | yes; negative patterns only | OK, OK |
| `mirror_check` | no (book only) | OK |
| `claims_check`, `duplicate_check`, `baseline_label_check` | yes (and the legacy file) | OK ×3 |
| `bohr_frequency_probe` F8 | yes (`len(CORPUS) > 10`) | PASS |
| `edge_rigidity_probe` | only by explicit path; after C2 no path names the Explainer | n/a |

**Conclusion.** A tiny, inert redirect passes every check unmodified. A formal exclusion would have
to be added in at least 9 separate places, because the repository has no single
manuscript-file list:
- `build.sh`, `staleness`, `voice` (+ `voice_scope_test`), `dependency_label`, `census`,
  `proof_census`, `architecture`, `citation`, `bohr`;
- plus the three whole-tree walkers.

So exclusions are not recommended (§A.28).

**Minimal mechanism (recommended: M1).**
- **M1, no tool change.** Add the stub. Build its `.tex`/`.pdf` with `sh ./build.sh Explainer` and
  commit them.
  - `staleness_check` then guards their consistency.
  - The old `papers/Explainer.pdf` URL keeps resolving, to a one-page pointer.
  - The old full PDF stays in history and in every earlier Zenodo version.
- **M2.** One skip in `build.sh`'s full-build loop; no stub artifacts. Staleness passes with the
  stub unstamped. The `.pdf` URL breaks, and a hard-coded name enters `build.sh`.

Either way, the stub must stay inert:
- no `kernel:` span;
- no theorem, lemma or definition heading;
- no code-file citation;
- none of the `voice_check` words.

**Redirect text.** It states standing fact only and passed `voice_check` in the dry run:

```markdown
# The Incompleteness of Observation: Explainer

*[Superseded document. The current introduction to the framework is the Introduction paper ([`Introduction.md`](Introduction.md)). The superseded text is kept for provenance, unmaintained, at [`legacy/Explainer.md`](legacy/Explainer.md).]*
```

There is deliberately no "moved", "formerly", "now" or date: those narrate history (§A.27/§A.30;
"formerly" is also a `voice_check` pattern).

**Edits to RETIREMENT that S2 requires:**
- **§2.1:** add the stub, plus its artifacts under M1. Replace D2's "remove" with M1 or M2.
- **§2.4 / §4.1(5):** survivors now include the stub, its `.tex`/`.pdf` (M1), `LEDGER.json:3100`
  (RC1), and the README bullet.
- **§3.1:** add a column "(B′) legacy move + redirect stub". External deep links are kept for
  `.md`, and for `.pdf` under M1. Anchors land at the stub's top.
- **R1:** mitigated.
- **D1:** B′.
- **D10:** README:115 points to the stub or to `papers/legacy/Explainer.md` (owner's choice).
- **§3.2:** the stub is scanned, and the dry run shows it passes. The legacy file's residual is
  unchanged.
- **LICENSE (D5):** `Explainer.md` still names an existing file. The minimal edit is optional; the
  generalized wording remains better.

## 8. Risks the plan misses (check 6)

- **R13, review legibility (RC4).** With the stub at the old path, GitHub's diff shows a 1060-line
  addition and a full rewrite, so "only line 3 and 8 link targets changed" cannot be seen. That
  invariant has no checkpoint (§A.41). Add a mechanical check: `git diff --no-index
  <(git show <base>:papers/Explainer.md) papers/legacy/Explainer.md` shows exactly 9 changed lines,
  each the expected replacement. Add `git log --follow` on the legacy path, and review under
  `git diff -B -M`.
- **R14, Zenodo.** The concept DOI resolves to the latest version.
  - Under M1 the latest deposit carries the stub PDF and the legacy `.md`, but no full Explainer
    PDF.
  - `.zenodo.json:26` says "Sources and built PDFs are both included". That stays true for the
    listed companions, since the edit drops the Explainer from the list.
  - `papers/legacy/` is not `export-ignore`d (`.gitattributes`), so the legacy text ships in
    releases. That is consistent with preservation.
  - Pre-existing and out of scope: `.zenodo.json` declares `cc-by-4.0` while `LICENSE:27–29` names
    no licence for the manuscripts. Flag it with R9.
- **R15, drift between plan and base.** Covered by P7 (RC5 b).
- **R16, the probe's mutation tests.** Only `_a12p_m3` reads the Explainer. The plan retargets it.
  No other mutant, countercontrol or self-test reads the Explainer.

## 9. Required changes

| ID | Change |
|---|---|
| RC1 | Account for `verification/coverage/LEDGER.json:3100`: either list it in §2.4 with its reason, or correct it forward. Fix the survivor list and the §4.1(5) expectation |
| RC2 | Adopt S2: the redirect stub at `papers/Explainer.md` (text above), with mechanism M1 (recommended) or M2, and the §2.1/§2.4/§3/D1/D2/D10/R1 edits of §7 |
| RC3 | Adopt S1: add §2.5, the reproducibility audit (§6 table), and the C2-message rule that frozen controls run only on materialized historical trees. No receipt, seal, certificate or record is rewritten |
| RC4 | Checkpoints for the legacy-file invariant (exact 9-line diff against the base blob), `git log --follow`, and `-B -M` review |
| RC5 | Move the D7 pre-check into P1/P6. Add P7: re-derive the dependents at the cut base, check open rounds' governed paths, and check evidence-retention mappings if that archive has landed |
| RC6 | MIGRATION row 23: classify the holography answer (Explainer:694–699) as (c) by default, with an owner option for Appendix C and :699's (d) items excluded |
| RC7 | MIGRATION §3: make the supersession conditional on the accepted Introduction's kernel map (Appendix A or its Alt-L §3 table), checked at P1 |

## 10. Owner decisions

- M1 or M2 for the stub's artifacts (M1 recommended).
- What README:115 points to: the stub or the legacy file.
- Whether the holography objection goes to Appendix C (F1).
- The existing optional items: the lineage paragraph, the navigation table (waits for #931), and
  the double-difference display from Main.
- The LICENSE wording (D5), and whether to fix the pre-existing licence and Computation-omission
  gaps (R9, R14).
- Whether to add the Introduction to the README "Core papers" table and to §1 (README:45).

## 11. Nits

- `GR.md:362` → `:360` (rows 2, 19), and cite `:358` (F3). `Main.md:118` → `:119` (row 7).
- MIGRATION: name OUTLINE-r4 as the governing revision (F4).
- RETIREMENT §2.2: give all six census note lines (298, 411, 453, 551, 573, 798).
- RETIREMENT P1: "audit README.md:112" does not say which README. Give the path.
