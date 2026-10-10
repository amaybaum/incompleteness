# Corpus correction round 1 — preregistration (DRAFT; stops at the freeze boundary; no edit is made under it)

Drafting snapshot D = `0f2687b7` (origin/main; identical to the premise ledger's audited base, so every ledger
anchor is a live line). Native §A.39 round; governed paths are manuscript files only. The round is strictly
corrective: it repairs the corpus against its own already-frozen evidence (the premise ledger, checkpoints 1
`19f4bfad` and 2 `407fae0b`) and teaches it nothing new.

[V3 `v3-round` and `v3-governed-paths` blocks: to be inserted in the repository's exact syntax — §V below]

## 1. Scope and boundary

**In scope.** The 27 drift/tension items of the premise ledger (checkpoint 1 §5: T-A1-1, T-A2-1, T-A2-2,
T-A2-3, T-A3-1, T-A3-2, T-A4-1, T-A6-1, T-A6-2, T-HT1-1, R1–R13; checkpoint 2 §6: T-E-1 … T-E-4), each with
exactly one of three dispositions (§2), and nothing else.

**Out of scope, by construction (no textual change at any site for these reasons).**
- Level 3A results: EXPOSED, AT-RANK, R4-CLOSED, LEMMA-3A, the octahedral diagnostic.
- The SELECT thread (selection principle, ORD∞ / TRANS / EO / V4′, the round-2 target theorem).
- 3B claims (edge-permutivity as mechanism, the rule matrix, the H factor).
- Round-2 provenance material (LIMCLOSE-C, completed-body availability, representation-vs-selection framing).
- The ledger's architecture (representation → H-T1 → H-T2 → realization; G / R4 / Q layering; OBS-1 as a
  manuscript notion). These are round 2, after 3B.
- Any banking of 3A as a verification round (a separate decision, not assumed here).
- Any new claim, any reorganization beyond what a listed correction requires, any count change not forced by a
  listed correction.

**Rule of the round.** A site is edited only if its item's disposition is CORRECT-IN-PLACE or REMOVE/QUALIFY
ASSERTION, and then only with the frozen replacement text of §3. If executing a listed correction would require
stating anything from the out-of-scope list, the item is halted at execution and reported, not improvised.

## 2. The three dispositions

| Disposition | Meaning | Manuscript rule applied |
|---|---|---|
| **CORRECT-IN-PLACE** | the sentence is wrong or over-scoped relative to its own derivation; rewrite it to what the derivation supports, in the paper's register | §A.27 correct in place; §A.32/§A.33 register |
| **REMOVE/QUALIFY ASSERTION** | a status word (theorem / derived / proved) or a listed result is not supported by the cited chain; remove the assertion or downgrade the status label using the corpus's **own existing** qualification, keep the derivation | §A.30 remove the assertion, keep the derivation; never assert-then-qualify |
| **DEFER-TO-ROUND-2** | a correct statement at the site cannot be written without the representation/realization/selection or OBS architecture, or without a Track-II interpretation; **literally no textual change** | — |

## 3. Per-item disposition table (frozen with the preregistration)

[Filled from the verbatim site collection: for every item — site(s); disposition; frozen ledger source
(entry and section); exact old text; exact new text (empty for DEFER); mirrors to carry the same edit; the
re-grep phrase(s) and the expected before/after counts. §3 is the authorization: nothing outside its rows changes.]

### 3.1 Deferred set (frozen; no textual change)

| Item | Site | Why a correction would require round-2 material |
|---|---|---|
| R3 | book ch09 (A5 restated at visible-sector level) | stating the right level needs the substrate-route / observer-route (Koopman) distinction of L-A5 — the representation architecture |
| R9 | book ch09 (A4 restated as partition-center independence) | separating A4-T / A4-S / A4-P and saying which the book means needs L-A4's four-claim split and the descent theorem framing |
| R10 | book ch05 (substrate A4-S equated with emergent chiral symmetry) | the level crossing can only be stated with the substrate / emergent / observer layering |
| T-HT1-1 | SM.md:248–250, :274 (field-theory observer is OBS-C, a degenerate point of OBS-M) | the correction is the OBS-1 observer-notion separation itself |
| T-E-3 | Substratum.md:84; SM.md:170 (E5's d ≥ 3 inference is Einstein-gravity-specific) | the finding is a Track-II circularity for the GR/SUBSTRATE BRIDGE; stating it is an interpretation, not a correction |

## 4. Guardrails (frozen)

1. **T-A2-1** (GR.md:669 vs :68–74, stochastic-substratum universality of ħ): narrow the claim to what the
   existing derivation supports — the classical-side microreversibility condition the derivation uses is stated
   as a condition of the result. The Θ-twisted detailed-balance condition of L-A2's replacement obligation
   (A2-GR) is **not** inserted; it stays a ledger obligation until proved.
2. **T-A6-2** (SM.md:140 "Theorem (Discrete Einstein equation)" vs :146 (iv)): remove or downgrade the theorem
   label using the corpus's own qualification at :146 (iv) ("is not established by the cited chain"); the
   derivation stays. The generator / Γ-curvature repair of L-HT2 is **not** introduced.
3. **T-A3-2** (SM.md:146 (i), (iii), |∂V| used as Euclidean area): correct only where the text equates the cubic
   graph-boundary count with isotropic Euclidean area; the Γ-perimeter replacement of L-HT2 is **not** introduced.
   (T-A3-1, the mod-q area-law inequality, is corrected to the inequality its proof gives — a scope correction,
   not a repair.)

## 5. Closure steps (all eight required before landing; each produces a recorded artifact)

1. **Frozen per-item disposition table** — §3, in the preregistration at F.
2. **Governed-path census before editing** — at F: sha256 of every governed file (papers/*.md, *.tex, *.pdf;
   book/*.md, *.tex, *.pdf); recorded in the round's record directory.
3. **Each correction linked to its frozen ledger source** — §3's source column names the ledger entry, section
   and (where applicable) the exact check file; the ledger files' hashes are recorded.
4. **Mirror propagation in the same commit** — for every edited claim: book/ch*.md ↔ FULL.md, companion papers
   that restate it, abstracts/summaries/tables (§A.25 steps 1–4); each mirror is a row of §3.
5. **.tex/.pdf regeneration or explicit governed failure** — `sh ./build.sh <papers…> --book` for every edited
   source; if the toolchain is absent or a package missing, the generated artifacts are flagged STALE in the
   result note and the commit message (AGENTS.md "Constrained-environment caveat"); never left silently stale.
6. **Before/after re-grep counts** — §3's phrases: counts at D and at E for the whole corpus; the surviving
   count must equal the predicted legitimate-use count stated in §3.
7. **§A.32/§A.33 added-lines scan** — the diff's added lines are scanned for the prohibited phrase families
   (meta-commentary, reader instruction, rhetorical parallelism, self-assessment, label-restating, caps emphasis,
   revision-history voice); any hit blocks E.
8. **Claim-surface sweep** — the diff is scanned for every term of the out-of-scope list (§1): EXPOSED, AT-RANK,
   R4-CLOSED, R4, OBS-R, OBS-M, OBS-C, OBS-∞, edge-permutiv*, ORD∞, TRANS, EO, V4′, LIMCLOSE, octahedr*,
   Level 3, 3A, 3B, SELECT, DRIVE, "representation level", "realization", "selection premise", H-T1, H-T2; any
   hit in an added line blocks E.

Order of work: F designated → census (step 2) → edits per §3 rows, mirrors in the same commit (steps 3–4) →
build (step 5) → re-grep (6) → scans (7–8) → result note → E.

## 6. Interpretation limits

- The round changes consistency, not correctness: "bands unchanged" (AGENTS.md honesty conventions). Removing an
  overclaim can only hold or lower correctness; nothing here raises it.
- No change to any claim ID, count or ordinal beyond what a listed correction forces; totals are re-grepped
  corpus-wide after any inventory change (§A.30).
- Historical provenance preserved: the working draft is corrected forward; no dated notes, no "formerly"
  (§A.27, §A.30).
- The round does not resolve any ledger replacement obligation; it only makes the manuscript say what the
  ledger found it already supports.

## V. V3 blocks and record placement

[To be inserted in the repository's exact syntax: round id, `v3-round` block, `v3-governed-paths` block,
record directory under verification/ per §A.36, receipt path, programme index entry.]
