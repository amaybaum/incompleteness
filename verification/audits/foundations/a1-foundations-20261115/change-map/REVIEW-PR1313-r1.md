# Independent review of PR #1313 (A1 minimum-change correction, Stage 2a), r1

**Reviewer.** Independent of the map and of the implementation. Paper-only: no repository file edited, nothing committed, pushed or posted. Read-only checks only (git diff/show, grep, `tools/coverage_check.py`, `tools/voice_check.py`, `tools/claims_check.py`, `tools/staleness_check.py`, the SC-42 checker in its normal, `-O` and `--self-test` modes, and pandoc to stdout).

**Object.** Branch `paper/a1-min-correction-20261116`: `e56b39b65` (the correction) and `8bf6ecf99` (SC-42 receipt regeneration) on `main` at `e4c6ba7f20da39fd57e67c8225457fe5f6c1f6f6`.

**Authority.** The owner's minimum-change policy and Stage 2a authorization on #1169 (as summarized in the review brief); CHANGEMAP-A1C-r6-min (133 entries) with Addendum 1 and its review (21 pairs; 3 sub-edits dropped); implementation record IMPLEMENT-2a-r2; AGENTS.md §A.14, §A.25, §A.27, §A.30, §A.32, §A.33.

## Verdict

**REVISE.**

- The diff matches the approved map and Addendum 1 exactly. Every hunk has a map entry, every entry is applied, and the three drops are correct.
- Mirrors, the registry, artifacts and the SC-42 receipt are in order.
- The independent survivor scan (check 3) found unsupported physical assertions that the map does not cover:
  - two of them are the same sentences the map itself corrects elsewhere (F1, F2);
  - four more are companion or book restatements of corrected claims, or residue of the Q10 (c) removal (F3–F6).
- The authorization requires that no unsupported physical assertion survive. And because each edit must match a reviewed map entry, these can be fixed only through a reviewed Addendum 2, not by editing the branch directly.
- One applied map text produces a doubled em-dash (F7).

Counts: **2 blocking, 5 required, 5 recommended.**

## Findings

### F1 (blocking): ch01:85 / FULL:420 still says nature's realization uses the counting measure

- **Evidence.** ch01:85 ends: "Partition-relativity is therefore relative to the declared measure, and the framework's baseline transition matrices and its physical realization use the canonical one."
  - This is the book mirror of the clause that N-M09 deletes at Main:58 ("…and the physical realization use it", with the map's diagnosis "The physical realization (nature) said to use the maximal-entropy counting measure").
  - N-G01b deletes the same clause at GR:20.
  - N-K01-85 edits a different sentence of the same line ("The selection is a principle the framework adopts for constructed realizations").
  - In r3, M-09 listed K-ch01-85 as its propagation target, but K-ch01-85's row picked the earlier sentence. No map version and no check-table row covers this clause.
- **Classification.** (a) map miss, and a §A.25 mirror miss.
- **Exact fix** (Addendum 2 pair, ch01:85 and FULL:420, byte-identical):
  - Old: `and the framework's baseline transition matrices and its physical realization use the canonical one.`
  - New: `and the framework's baseline transition matrices use the canonical one.`

### F2 (blocking): ch03:84 / FULL:949 keeps "the substratum is a finite set with a bijection on it"

- **Evidence.** ch03:84: "There is no Lagrangian at the substratum level; the substratum is a finite set with a bijection on it, governed by a discrete update rule …".
  - ch02:136 carries the identical clause. N-K02-136 narrows it to "the substratum is a set (finite under A1) with a bijection on it", as a book mirror of the Sub:389 ontology claim. The PR now reads "a set (finite under A1)" at ch02:136 and "a finite set" at ch03:84 for the same statement.
  - The map's Part E split of r3 row K-ch03-84/88/196/230 classes :84 as model, class or conditional (RES/MOD). That classification cannot hold for a sentence the map narrows verbatim one chapter earlier.
- **Classification.** (a) map miss: an inconsistent split decision.
- **Exact fix** (ch03:84 and FULL:949):
  - Old: `the substratum is a finite set with a bijection on it, governed`
  - New: `the substratum is a set (finite under A1) with a bijection on it, governed`

### F3 (required): SM:308 is the unscoped source of the narrowed ch05:95

- **Evidence.**
  - SM:308: "Main's readback lemma supplies the memory content, and its recurrence-cycle theorem the P-indivisibility content, independently of center independence."
  - ch05:95, which cites SM §4.3 for this, is narrowed by N-K05-95 to "and, on finite reversible representatives, its recurrence-cycle theorem the P-indivisibility".
  - The companion statement is untouched, and SM:308 appears in no check-table row.
- **Classification.** (a) map miss; §A.25 step 3 (companion restatements must agree).
- **Exact fix** (SM:308):
  - Old: `and its recurrence-cycle theorem the P-indivisibility content`
  - New: `and, on finite reversible representatives, its recurrence-cycle theorem the P-indivisibility content`

### F4 (required): ch14:278 / FULL:3944 states the maximal-entropy measure theorem without the finite-representative scope

- **Evidence.**
  - ch14:278: "the framework's own theorems (the maximal-entropy measure, the gauge status of the microstate) close the planted-measure escape".
  - Its companion, Computation:120, is narrowed by N-P04 to "the substratum measure of a finite representative is the unique $\varphi$-invariant maximal-entropy measure …, which excludes a planted-measure escape". The map's reason is that on an infinite carrier the measure is not normalizable (N-M46).
  - ch14:278 appears in no check-table row.
- **Classification.** (a) map miss, §A.25.
- **Exact fix** (ch14:278 and FULL:3944):
  - Old: `(the maximal-entropy measure, the gauge status of the microstate)`
  - New: `(the maximal-entropy measure of a finite representative, the gauge status of the microstate)`

### F5 (required): ch18:162 / FULL:4968 still lists recurrence among forward predictions that test the framework

- **Evidence.** ch18:162: "The chapter's broader content on forward predictions continues with the framework's substratum commitments — finite information under A1, recurrence, the arrow of time, cosmic topology, and consciousness — that test the framework at scales and levels distinct from …".
  - N-K18-20 edited only "finite information" on this line.
  - Q10 (c) removes cosmic recurrence as a prediction. The rest of the removal is complete: F8 is deleted, along with ch18:20's "definite structural prediction", ch18:28, the Falsifiability paragraph, ch18:328, appendix-c:132 and README:90.
  - This line still names recurrence as a substratum commitment that tests the framework. Under the owner's ruling it is not to be restored as a conditional either.
- **Classification.** (a) map miss (Q10 (c) residue).
- **Exact fix** (ch18:162 and FULL:4968):
  - Old: `finite information under A1, recurrence, the arrow of time`
  - New: `finite information under A1, the arrow of time`
  - The §18.7 heading and the recurrence mathematics stay, as Addendum 1 kept them.

### F6 (required): Computation:176 and ch14:184 / FULL:3850 present total finiteness as the framework's axiomatic content

- **Evidence.**
  - Computation:176: "The framework's axiomatic content concerns finite physical structures (with possibly unbounded history but always finite at any moment)". ch14:184 has the same clause.
  - In the same paper, Computation:180 is narrowed by N-P06 to "The framework's finiteness hypothesis (A1) — that the substratum has finitely many tokens at any moment —". So "finite at any moment" is A1 in that paper's own terms.
  - :176 presents it as axiomatic content, and so as adopted, which is policy item 1's case. The conclusion of the passage (no bridge from finite-structure axioms to asymptotic complexity classes) does not depend on this.
  - Neither line appears in any check-table row of r3 or r6-min.
- **Classification.** (a) map miss.
- **Exact fix:**
  - Computation:176: Old `The framework's axiomatic content concerns finite physical structures`, New `The framework's axiomatic content concerns, under A1, finite physical structures`.
  - ch14:184 and FULL:3850, the same pair in lowercase: Old `the framework's axiomatic content concerns finite physical structures`, New `the framework's axiomatic content concerns, under A1, finite physical structures`.
  - The neighbouring "finiteness-per-moment" in the commitment list at Computation:174 and ch14:184 can be read as Lemma 1's per-moment visible finiteness (Main:36). It is left to the Addendum 2 author, with a recorded reason either way.

### F7 (required): Main:728 item (ii) has a doubled em-dash from N-M44

- **Evidence.** The applied text reads "(ii) total finiteness of the bijective representative of the status Remark of §1.2 — an open hypothesis, not adopted — — Lemma 1 delivers …".
  - N-M44 inserts " — an open hypothesis, not adopted —" directly before the item's existing parenthetical dash pair (" — Lemma 1 delivers … (deep-sector enlargement, developed there) — consumed here by …").
  - The implementation matches the map byte for byte, so this is a defect in the map text. It typesets as "— —" in the PDF.
- **Exact fix** (Main:728, Addendum 2 pair):
  - Old: `of the status Remark of §1.2 — an open hypothesis, not adopted — — Lemma 1 delivers`
  - New: `of the status Remark of §1.2, an open hypothesis, not adopted — Lemma 1 delivers`
  - The pair keeps one dash pair and the one status form.

### F8 (recommended): the Main:728 (iii) parenthetical cites wording N-M11 removed

- **Evidence.**
  - Main:728 (iii): "(a reader who declines the recovery may instead adopt reversibility as the standard information-conservation postulate … at no cost to the downstream results — see the remark following Lemma 3)".
  - The remark following Lemma 3 (Main:64) no longer contains the "reader unwilling to grant that recovery may simply take reversibility as the standard postulate" sentence. It now says that reversibility of nature's dynamics "is not adopted as a postulate" and that "the emergence results of §3.4 do not use it".
  - The parenthetical is not false: a reader may still adopt the postulate, and the remark supports "no cost". But its pointer now lands on text that says something different.
- **Fix.** Either leave it (no unsupported assertion), or in Addendum 2 change "— see the remark following Lemma 3" to "— the emergence results of §3.4 do not use it; see the remark following Lemma 3". I prefer leaving it under the minimum-change policy.

### F9 (recommended): bijectivity of nature stated as a commitment at ch18:188 (old :190) and ch14:106

- **Evidence.**
  - ch18:188: "bijection dynamics (the framework's commitment to $\varphi$ as a bijection)", in the sentence N-K18-192 edits for the $|S|<\infty$ clause.
  - ch14:106: "The framework's deterministic bijection $\varphi$ guarantees unitarity at the substratum level."
  - Main:64 (N-M11) now states that reversibility of nature's dynamics is not adopted as a postulate, and the map narrows the "bijectivity premise" sites to "the framework's models" (N-K07-12, N-K09-129, N-K18-122, N-K19-22).
- **Classification.** (b) mostly outside the A1 total-finiteness scope (Q5 (a)). Surjectivity from injectivity needs a finite set, so there is an A1 link. The owner should decide whether Addendum 2 takes these two sites.
- **Fix if taken.**
  - ch18:188: "(the framework's commitment to $\varphi$ as a bijection)" → "(the framework's models take $\varphi$ to be a bijection)".
  - ch14:106: "The framework's deterministic bijection $\varphi$" → "In the framework's models the deterministic bijection $\varphi$".
  - Both with FULL mirrors.

### F10 (recommended): ch14:92 / FULL:3758 "closed by the framework's structural commitments"

- **Evidence.** "The infinite-resource routes are closed by the framework's structural commitments". This line follows ch14:90, which N-K14-90 narrows to "precludes under A1 (a structural exclusion conditional on A1)". The infinite-time route is closed only under A1.
- **Fix.** "closed by the framework's structural commitments" → "closed by the framework's structural commitments, under A1 for the infinite-time route", or record a reason for leaving it.

### F11 (recommended): census-statement paragraph edited (Main:760, N-M51); record it in the change note

- **Evidence.** N-M51 edits the last sentence of the paragraph headed "**Corollary (observer-selection rule, with its rate condition).**". That is why the `MAIN:C-observer-selection-rule-rate-condition` fingerprint moved (N-D2d).
  - The selection rule itself ("observers exist where (C1)–(C4), with (C2) read as (C2-slow), are satisfiable, and … not satisfiable in the coarse-grained description of the equilibrium phase") is unchanged. Only the interpretive "replaces the past hypothesis" gloss is removed.
  - It is within the approved map, but the authorization's exception list names only Main:449 and GR:342.
- **Fix.** None to the text. State in the PR description that N-M51 touches a corollary paragraph without changing its mathematical content.

### F12 (recommended; nits, no change required)

- N-U27 (Sub:401) rewrites `$(S, \varphi)$` as `$(S,\varphi)$`. This is the map's own new text, and it renders identically.
- N-K19-80 lowercases "Reciprocity" after the inserted prefix. This is the necessary consequence of a sentence-initial insertion.

## Checks

### 1. Diff ⊆ map

- I extracted every changed line of the 26 sources and `LEDGER.json` as a word-level diff and compared each hunk with its r6-min row or Addendum 1 pair.
- Every hunk has an entry, and the applied text equals the map text. The only differences are the two nits of F12 and the F7 dash, which is in the map text itself.
- No hunk lacks an entry.
- `8bf6ecf99` is a non-map, necessary-propagation artifact (check 9).

### 2. Map ⊆ diff

All 133 r6-min IDs are accounted for:

- 130 text entries applied in full or in part;
- N-K01-16 and N-K03-40 applied in part per the Addendum 1 review;
- N-Kgl-19 dropped;
- N-D2d applied, and N-D2x applied as a check: `coverage_check.py` reports OK, 133 canonical statements.

All 21 Addendum 1 primary pairs are applied, and no fallback (`-alt`) pair is applied. Nothing is missing.

### 3. No unsupported physical assertion survives

**Fails** on F1–F6 (map misses); F9 and F10 are borderline.

I grepped all `papers/*.md` and `book/*.md` for the following, and read each hit in context:

- "cosmic recurrence", "F8", "falsifiable only in the logical", "cyclic", "universe returns/recurs";
- "finite universe", "finite deterministic universe", "finite substratum", "finite configuration space", "finite bijection", "finite deterministic system/construction/object";
- "commitment … finite", "finiteness commitment", "is posited", "posit A1", "supported by E3", "past hypothesis";
- "physical realization", "counting measure", "maximal-entropy measure", "corner-occupancy", "recurrence-cycle theorem", "planted-measure".

I also grepped every old string of every map row across the corpus, to find unpropagated twins.

Hits left alone, with the reason:

| Hit | Reason it stands |
|---|---|
| Main:60 "by the corner-occupancy claim of §3.1" | §3.1 (iii) still states the near-unitary-corner confinement of a finite deterministic substratum, which uses finiteness, so the inventory item is accurate. |
| ch00:59, ch05:11 "an observer embedded in a finite deterministic universe" | Restrictive. |
| ch00:69, ch03:230, Structure:108 "starting from a finite deterministic substratum" | Method statements. |
| SM:20, :222, :232, :316; Complexity:21, :314; Computation:21; Sub:288; ch14:100, :105 | Classed MOD in the reviewed check table. I accept that classing as the map's decision; I note that SM:222/:232 "the fundamental object is the finite bijection" read close to policy item 2's "the fundamental object is …". |
| ch18:20 "Section 18.7 develops, under A1, … exact recurrence" | Describes conditional mathematics, not a prediction. |
| ch18:166, :168 | Conditional on A1. |
| Main:222 heading "the finite-substratum commitment" | Classed RES; headings are not renamed under the policy. |

A1 is nowhere presented as disproved, and after the PR it is presented as adopted only at the F6 sites.

### 4. Unchanged where required

- **A4.** Sub:98 and Sub:157 are untouched.
- **Theorem statements.** No theorem, lemma or proposition statement is changed. Main:449 ("For a finite reversible realization there is no relaxation …") and GR:342 (the "Ontological commitment" list) carry the owner's named wording. The one census-statement paragraph touched is the Main:760 corollary (F11), with its mathematical content unchanged.
- **Proofs.** No proof text is changed.
- **Ledger.** `LEDGER.json` changes exactly one line: the `MAIN:C-observer-selection-rule-rate-condition` fingerprint `df04fba6b2d81e20` → `38127d106435567a`. `coverage_check.py` is OK.

### 5. Mirrors

The multiset of removed chapter lines equals the multiset of removed FULL lines (93 each), and the same holds for added lines (88 each). Every added chapter line occurs verbatim in FULL. The two whole-line deletions (appendix-a F8 row; appendix-c :132 with its blank) and the ch18:188–189 deletion are mirrored. Each F1–F6 fix in a chapter must carry its FULL twin (lines given above).

### 6. Register

- **History voice, caps and meta phrases.** A scan of every added word-diff segment (395 segments) found no history-voice phrase ("formerly", "no longer", "is now", "withdrawn", "corrected", "retired"), no caps emphasis and no meta-commentary.
- **Pre-existing text.** Hits for "honest", "discipline" and "now entering" are in unchanged text on changed lines, and the book's essay register is exempt.
- **Assert-and-disclaim.** None introduced. Sub:216 "motivated by E3, which does not establish it" and ch09:106 "as a claim about nature, the open hypothesis A1, not adopted" state status declaratively. The status phrase has one form throughout.
- **Tools.** `voice_check.py` and `claims_check.py` are OK.
- **Defect.** F7's doubled dash is the only register or typography defect.

### 7. The three drops

ch01:183, ch03:186 and glossary:19 are unchanged. Each assumes parameter independence (with measurement independence, determinism and $\pm1$ outcomes) rather than deriving it from the cone, so it states Bell's theorem, which needs no finite site set. The cone sentence on ch01:183 is already scoped ("exactly for finite-range substrata"). The drops are correct, and no A1-dependent claim survives at those sites.

### 8. Artifacts

`.tex`/`.pdf` changed for exactly Main, GR, SM, Substratum, Structure, Methodology, Complexity, Computation and the book (18 files); no other artifact changed.

- **Stamps.** `staleness_check.py` reports OK (13 matched).
- **`.tex` content.** Regenerating each `.tex` with pandoc to stdout differs from the committed file only by the two-line source-sha256 stamp.
- **Build.** The build logs report OK with plausible page counts (Main 104, GR 96, SM 152, Substratum 56, Structure 100, Methodology 55, Complexity 37, Computation 23, book 565).
- **After Addendum 2.** Applying F1–F7 requires rebuilding Main, SM, Computation and the book again.

### 9. `8bf6ecf99` (SC-42 receipt)

- **Scope.** It changes only `verification/audits/manuscript/bell-operational-reconciliation-20261029/sc42-integration-result.json`.
- **Status of the file.** It is not listed in `verification/infrastructure/legacy-records.json` or in any receipt. It is a mutable deterministic receipt, regenerated by many earlier commits, and CI compares it byte for byte (`.github/workflows/verify.yml`, step "SC-42 integration source scope and must-fail controls").
- **Reproduction.** Running the checker at this head reproduces the committed file byte for byte in both normal and `-O` modes: verdict PASS, 1063 checks, no failed predicate.
- **Controls.** `--self-test` reproduces the unchanged `sc42-integration-controls.json` byte for byte.
- **Content of the change.** The diff only replaces the "chapter line mirrored in FULL" predicate texts for the edited lines.
- **Assessment.** Acceptable as necessary propagation. It must be regenerated again after Addendum 2, because F1, F2, F4, F5 and F6 change chapter lines.

## Required path to ACCEPT

1. Draft Addendum 2 with the exact pairs of F1–F7. Add F9 and F10 if the owner takes them, or record a reason for each.
2. Have it independently reviewed.
3. Apply it to sources and FULL mirrors.
4. Rebuild the affected artifacts, regenerate the SC-42 receipt, and re-run `coverage_check.py`. SM:308 and Main:728 may sit inside census statement bodies, so check for STALE.
5. Report F11 in the PR description.

## Not checked

- The owner's #1169 comments themselves; I worked from the brief's summary.
- Byte identity of the local r6-min copy with the published research commit, beyond the header note in IMPLEMENT-2a-r2.
- GitHub CI results at either head.
- Visual inspection of the rebuilt PDFs beyond page counts and the build logs.
- Lean, the guard and the release gate.
