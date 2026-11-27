# A1 staging allow root: dependency map, second derivation, W1-a analysis and record skeletons

**Status: WIP / UNVERIFIED staging drafts. Not frozen, not reviewed, not adopted, not admitted, not activated.**
Nothing here is a review record, a designation, an activation, a freeze or a trial.

**Authority.** Owner decision of 2026-11-27 (`amaybaum`, recorded at #1169 comment 7209216541), quoted: "Continue
preparing the allow-root records wherever dependencies permit. When session designations are required, present the
exact `oi-designate` comments, including the required identity and scope fields, for me to post manually." Paper and
record preparation only: no GitHub write, no push. The designation texts are not in the repository; they are given to
the owner separately.

**Goal link (AGENTS.md sec. A.47).** A1 retirement (#1169), staging checklist item 4.3: it would decide whether the
designated first allow record can be reviewed, activated and pinned at `F` with the five allowances, and what each
remaining step waits on.

**Rules applied.** Staging amendment r2 (`a1exit-staging-amendment-20261126/AMENDMENT.md`, tool branch, with S11-2a
merged) sec. 2; its supplement S-1 r5 (`AMENDMENT-S-1.md` at `3bc3693c66c65d768bc072b65d07f045fe8a23f5`, adopted
with every open-question default, admitted threads #1577 and #1169); design r6 as amended by r13 (on `main`):
R6.RULE.2, .4, .5, .7, .10 to .12, R6.REC.1, .2, .6, .7, .13, .14, .16, R6.RECON.29, .31, R6.RDIR.1, .5, R6.PLACE.4,
R6.EVID.8; the retirement plan on PR #1477 (`PREREG.md` at `4c79be642ca631573f06b444903be75ec4f5e2b6`).

## 1. Placement

| Record | Path | Fixed by |
|---|---|---|
| allow root | `D_rec/a1-staging-allow-root.json` | staging r2 sec. 2 "Placement and exact designation"; `record_authority.transition_roles[1]` |
| transition descriptor | `D_rec/a1-staging-transition.json` | staging r2 sec. 2 "In a later, separately approved activation"; `record_authority.transition_descriptor` |
| prior-freeze declaration | `D_rec/a1-staging-prior.json` | staging r2 sec. 2 "Prior-freeze continuity"; `record_authority.transition_prior` |
| session registry | `D_rec/a1-staging-sessions.json` | S-1 S1.1 |
| ordinary, widening and registry reviews | **not fixed** | see sec. 6, question A |

`D_rec` is `verification/audits/foundations/a1exit-deletion-20261121` (R6.PLACE.4's one admitted record directory;
R6.RDIR.1: the directory part of `P_cfg`). It holds no entry at `H` or at `main` `ec1d6ccea5a7be2579092d5c380b209c582f81dd`
(Dir2, R6.RDIR.5). The four records above are committed at their paths as skeletons. The reviews are not: their
directory and file names are not fixed by staging r2 or S-1, and a JSON file shaped as a review anywhere under
`verification/audits/` is read by detection (R6.RECON.35, every JSON-shaped file), so a review skeleton with pending
verdicts could count as a non-accepting review of the root (R6.REC.6). Their contents are specified as templates in
sec. 5 instead.

## 2. Dependency map

"Now" means preparable from bytes already fixed. Every other row names the unfixed input it waits on.

| Element | Waits on | Requirement | State |
|---|---|---|---|
| Rule content of the five allowances (scope, matcher, fingerprints, contexts, `max_instances`, `negative_allowance`, examples) | `H` (ledger base; `recorded_at`), the configuration's sentence abbreviations and splitter version (item 4.8), the profile specs and their pinned sources, the deny set (for self-pass), the ledger pin (for `X_rep`) | staging r2 sec. 2 "Allow-rule record"; R6.REC.14; R6.RULE.2, .5; R6.EVID.8 | **prepared at `H` = 53c6601a** (sec. 3); invalidated by any change to those inputs |
| W1-a exclusion and adverse case | the same | staging r2 sec. 2 "Never admit W1-a ... Include the historical adverse case in review" | **prepared** (sec. 4) |
| `recorded_at` | the choice of eligible commit (stop S-2 of the staging drafts README) and item 4.1 (whether `H` moves, stop S-3) | R6.RULE.2, R6.REC.14 | `H`, provisional |
| `author` (root and each rule) | the owner's designation of the writer and the registry entry it fixes | staging r2 sec. 2 "One-time transition" as amended by S-1 sec. 5; S-1 S1.1, S1.8 | **pending marker** `PENDING-S1-REGISTRY-ID-OF-DESIGNATED-WRITER` (fails closed) |
| `status` text | stop S-6 (timeless or absent before review) | R6.REC.12 (immutability) | WIP text, open |
| Root blob (`blob_sha256`) | `author`, `status`, and every input of the first row | R6.REC.6; staging r2 sec. 2 | pending |
| Lint by the tool | the final tool tree (S-1 sec. 7 identity checks; R6.RULE.11, .12 checks the current tool lacks) | R6.RULE.10 to .12; R6.REC.14 | the current tool's `rules.lint_rule` passes all five (writer's report); final tool pending |
| Ordinary review by R | the root blob; R's registry entry (`reviewer`, `platform_ref`); a `revision` commit reachable from `F` whose tree holds the root (in practice `B`, or a commit on `B`'s first-parent history); review placement (sec. 6 A) | R6.REC.2, .6; R6.RECON.31 `review.record`; S-1 sec. 3, S1.6 to S1.8 | template only (sec. 5.1) |
| Widening review by X | as the ordinary review, and the ordinary reviewer's identity (X outside both parties) | staging r2 sec. 2 "Initial widening review"; R6.REC.13; S-1 S1.7 | template only (sec. 5.2) |
| Session registry | the owner's three designation comments (their URLs are the `designation` values) and their exact entries | S-1 S1.1, S1.2, S1.4 | **skeleton**, every value pending |
| Registry review | the registry blob; a reviewer outside the registry author's party; `revision` reachable from `F` | S-1 S1.2 | template only (sec. 5.3) |
| Transition descriptor | `B` (owner activation); the custody archive's SHA-256 at `B` (it lands with #1577; today `5ab330c7...070d` on the tool branch, provisional); the class root's SHA-256 (its tool-landing pins are derived from the fixed tool-landing candidate under R6.TREE.5, so it waits on the final tool tree); the allow root's SHA-256 | staging r2 sec. 2 "In a later, separately approved activation" | **skeleton**: paths filled, `base` and the three digests pending |
| Prior-freeze declaration | only the fact that no earlier freeze used these lineages | staging r2 sec. 2 "Prior-freeze continuity" ("The initial owner designation for these lineages binds the null predecessor") | **prepared**: `freeze: null`; the owner confirms it is the initial designation |
| `B` | roots, their reviews and the widening review available from verified Git objects; the custody archive; owner activation (separately approved) | staging r2 sec. 2 | owner act; not authorized |
| `M` | not an input of the allow root. The class root's tool-landing pins (R6.TREE.5) and the RT-D representative control at a snapshot `S` (whose class reference must equal the landed class tip in `M`) wait on it | staging r2 sec. 2, R6.EVID.8 paragraph | n/a for this record |
| `F` | the `PREREG.md` Record pins table pinning the configuration, its reviews, the descriptor, the prior declaration and the registry with its review; the owner's `F` approval quoting the registry's SHA-256 | R6.REC.16; staging r2 sec. 2 and 3; S-1 S1.1, S1.2 | last; AGENTS.md sec. A.50 items 2 and 5 |

## 3. Second derivation of the five allowances (R6.REC.14)

`rederive_allow_root.py` re-derives every field R6.REC.14 names from the bytes at `H` alone, taking only each rule's
meaning (profiles, literal, context and negative literals, `context_required`, reason) from the draft. It does not
read the writer's script, its report or the superseded `w1-w2-allow-v3.json`. The tool supplies only splitter
version 2 and profile loading; context hashes (R6.RULE.5), trigger coverage, case-insensitive negative counts
(R6.RULE.7), self-pass through R6.RULE.4 steps 1-6 and example behaviour are computed in the script.

Recipe, from the repository root of this branch:

```
python3 -I verification/audits/foundations/a1exit-staging-drafts-20261127/allow-root/rederive_allow_root.py \
  --repo . --tool . \
  --root verification/audits/foundations/a1exit-deletion-20261121/a1-staging-allow-root.json \
  --deny verification/audits/foundations/a1exit-deletion-20261121/dr-deny.json \
  | cmp - verification/audits/foundations/a1exit-staging-drafts-20261127/allow-root/rederive-report.json
python3 -I verification/audits/foundations/a1exit-staging-drafts-20261127/allow-root/countercontrols.py \
  --repo "$PWD" --tool "$PWD" \
  --root verification/audits/foundations/a1exit-deletion-20261121/a1-staging-allow-root.json \
  --deny verification/audits/foundations/a1exit-deletion-20261121/dr-deny.json
```

Expected: the first prints nothing and exits 0 (`"holds": true`; the output is identical under hash seeds 1 and 99);
the second prints eight `True` lines and exits 0. Inputs are checked by digest: ledger blob `ba37c1cd`
(`2055e68f...`), base `H`; the six profile sources and pattern pins; the four deny pattern pins of the draft
`dr-deny.json`. Corpus: the 42 files `papers/*.md` and `book/*.md` at `H` (R6.A1CFG.2).

**Derivation.** For each rule, the fingerprint set is every corpus sentence at `H` containing the literal on which a
hit of one of the rule's profiles lies inside an occurrence of the literal. For all five rules it equals the
draft's: the same files (so `scope.files` is exactly the files where the allowance is needed, mirrors included), the
same sentence and context hashes, `max_instances` equal to the count, and the same allowances.

| Rule | File (`book/`) | Line at `H` | Line at `X_rep` | sentence sha256 | context sha256 | context equal at `X_rep` | trigger (profile, span) | negative counts |
|---|---|---|---|---|---|---|---|---|
| W1-b | The-Incompleteness-of-Observation-FULL.md | 2552 | 2554 | 91cc0436fa80 | d03916e7d2af | yes | count-grep `six structural` | none |
| W1-b | ch09-universality.md | 137 | 137 | 91cc0436fa80 | d03916e7d2af | yes | count-grep `six structural` | none |
| W1-c | The-Incompleteness-of-Observation-FULL.md | 5268 | 5270 | d4a11b15d8ca | 6c16e6e13e2e | yes | count-grep `six structural` | `finit`: 1 |
| W1-c | ch19-open-problems.md | 198 | 198 | d4a11b15d8ca | 6c16e6e13e2e | yes | count-grep `six structural` | `finit`: 1 |
| W1-d | The-Incompleteness-of-Observation-FULL.md | 5282 | 5284 | 085a5e05d6e0 | d781e6cab0ad | no | count-grep `six structural` | none |
| W1-d | ch19-open-problems.md | 212 | 212 | 085a5e05d6e0 | d781e6cab0ad | no | count-grep `six structural` | none |
| W2-a | The-Incompleteness-of-Observation-FULL.md | 5912 | 5914 | 0b0e05e69657 | bba1a3b01644 | yes | ptr `A1`, repo `A1` | none |
| W2-a | appendix-b-derivations.md | 235 | 235 | 0b0e05e69657 | bba1a3b01644 | yes | ptr `A1`, repo `A1` | none |
| W2-b | The-Incompleteness-of-Observation-FULL.md | 5923 | 5925 | 32ebfb906b72 | 7ee521657fdd | yes | ptr `A1`, repo `A1` | none |
| W2-b | appendix-b-derivations.md | 246 | 246 | 32ebfb906b72 | 7ee521657fdd | yes | ptr `A1`, repo `A1` | none |

(Hashes shortened here; full values in `rederive-report.json`.) Further results, each checked:

- Every literal is at least 8 characters (R6.RULE.11) and every rule has at least one fingerprint (R6.RULE.12).
- No sentence at `H` contains a literal without a covered trigger, so no in-scope or out-of-scope occurrence is left
  outside the fingerprint set.
- Every fingerprinted sentence passes its own rule through R6.RULE.4 steps 1-6: all of the rule's profile spans
  covered, context literals present in the sentence or a neighbour, no deny match, negative counts within its own
  allowance, unique in its file.
- W1-c's one `finit` is the allowance `{finit: 1}`; it names a literal of the rule's negative matcher (R6.REC.14).
- At `X_rep` every fingerprinted sentence is present once. W1-d's context changes there because its preceding
  sentence (earlier on the same line, ch19:212 and its FULL mirror: "... together with the open hypothesis A1 of
  finiteness constrain the class") is edited by the ledger; W1-d has `context_required: false` and no allowance, so the change does not affect
  its decision (R6.RULE.4 steps 3-4).
- Each positive example contains the literal and the context literals and is within its allowance; each fingerprinted
  sentence is a positive example in full. Each negative example is rejected, and the reason is recorded in the report
  (the W1-x first negatives by a `finit` beyond the allowance, most also by a deny match; the W1-a sentence by an
  absent literal and absent context).
- Rule ids are exactly W1-b, W1-c, W1-d, W2-a, W2-b.

**Countercontrols.** `countercontrols.py` runs seven mutants of the draft through the same script, and each makes it
fail: a changed W1-b context hash; W1-c's allowance raised to 2; W2-a's scope without its mirror; a W1-a equivalent
under the id W1-z; W1-d's literal shortened to `six structural`; the W1-a sentence dropped from W1-b's negative
examples; W2-b's `max_instances` set to 3.

**Agreement with the writer's derivation.** `../derive_rule_drafts.py --check` reproduces all three drafts on disk
after the `author` change below, and its report is regenerated with the new allow-root digest (sha256
`4e51e4725e25da544c2d15f7e0197f0f49c15d5c044089a7c0a47f3d8e6610e7`, git blob
`e4a3aed042b88139f82cc621958d37e93389bd37`). The second derivation agrees with it on every field.

**Observation for the tool reviewers.** The current tool's example lint (`rules.lint_rule`) calls
`matcher_holds(rule, example, [], [])` with no spans, so it checks context literals but never the literal: a positive
example without the literal passes it, and a negative example that differs from the rule only by lacking the literal
is reported as accepted. The second derivation checks the literal as well. No tool change is made here.

## 4. W1-a: adverse-case analysis

W1-a is not in the root under any id, and no rule is equivalent to it.

- **The sentence.** `papers/SM.md` line 1394 at `H` (sentence sha256 `df203079707e...`): "**Structural predictions**
  are properties of the equivalence class ... — they hold for every bijection satisfying the six structural
  properties." Its one profile hit is count-grep `six structural`; it matches no deny profile.
- **Why no allowance is justified.** The adverse review (#1577 comment 7187883838, F1 and F2) found that SM defines no
  "six structural properties", the G2 list is an output list, and the most plausible referent, A1-A6, includes the
  retired posit. Unlike W1-b to W1-d, the sentence neither enumerates the six nor qualifies them as properties "of the
  bijection" "developed in Chapter 5"; its count cannot be told apart from the retired posit count. An allowance
  would turn a REVIEW_REQUIRED hit on a possible retired-posit count into a PASS, which is the substitution the
  owner's instruction excludes ("If no valid justification exists, remove the allowance rather than inventing one").
- **Mechanical result.** None of the five literals occurs in the sentence; none covers its hit even if `papers/SM.md`
  were in every rule's scope; it is a negative example of every rule, so the lint itself exercises it.
- **Every generic occurrence accounted for.** "six structural propert" occurs in nine corpus sentences at `H`: the
  six W1-b/c/d fingerprints, held only by their own rules; ch09:104 and its FULL mirror (FULL:2519), "... are six
  structural properties of the substratum ...", held by no rule (none of the five literals occurs in it; it also
  carries `of the substratum`, a negative literal of every W1 rule) and edited away by the ledger, absent at `X_rep`; and SM:1394. At `X_rep` seven remain: the six
  fingerprints and SM:1394, which stays REVIEW_REQUIRED `unclassified`. This is RT-D's expectation as amended (ten
  W1/W2 PASS lines, SM:1394 REVIEW_REQUIRED; amendment 5 RT-D row).
- **Base dependence (stop S-3).** At `main` `ec1d6ccea5a7be2579092d5c380b209c582f81dd` "six structural propert"
  occurs in no corpus file (the book correction and the SM:1394 correction have landed); the W2-a and W2-b sentences
  are present. If item 4.1 moves `H` past those corrections, W1-b, W1-c and W1-d have nothing to classify and fail
  lint at a new `recorded_at`, and the W1-a adverse case has no sentence; whether the root may then carry fewer than
  five rules is not stated by staging r2 ("may carry exactly"), and is the owner's decision.

## 5. Record skeletons and review templates

### 5.1 Ordinary review of the allow root (template; schema `oi-review-record/1`, R6.RECON.31 as amended by S-1)

```
{"schema": "oi-review-record/1",
 "reviewer": "<R's registry id>",
 "platform_ref": "<R's registry platform_ref>",
 "revision": "<commit reachable from F holding the root at this path and blob; in practice B>",
 "reviewed": {"path": "verification/audits/foundations/a1exit-deletion-20261121/a1-staging-allow-root.json",
              "blob_sha256": "<the root's final sha256>"},
 "method": "<how each rule was re-derived, naming at least one full 40-character object id read>",
 "verdicts": [{"item": "W1-b", "verdict": "accept|reject|dissent", "reason": "..."},
              {"item": "W1-c", ...}, {"item": "W1-d", ...}, {"item": "W2-a", ...}, {"item": "W2-b", ...}]}
```

`kind` absent (ordinary). The checklist for the reviewer is in `../README.md`, "Ordinary reviewer of the allow root".

### 5.2 Widening review of the allow root (template)

As 5.1 with `"kind": "widening"`, `"replaces": null` (valid only because the reviewed record is the exact designated
root with `supersedes: null`; staging r2 sec. 2 "Initial widening review"), the same `reviewed` path and digest,
`reviewer` and `platform_ref` X's, and verdicts on all five rule ids, each `accept` for admission. Checklist:
`../README.md`, "Widening reviewer of the allow root".

### 5.3 Registry review (template)

As 5.1 with `reviewed` the registry's path and blob, `reviewer` outside the registry author's party, items
`party:<id>` for each entry and `withdrawn:<id>` for each withdrawal, `revision` reachable from `F`, and scope over
`D_rec` (S-1 S1.2). The reviewer checks each entry and withdrawal against its form comment.

### 5.4 Committed skeletons in `D_rec`

- `a1-staging-sessions.json`: canonical JSON (R6.RECON.29), `author` and three `parties` entries (writer, ordinary
  reviewer, widening reviewer) with every value `PENDING-...`, scope `D_rec`, `withdrawn: []`.
- `a1-staging-transition.json`: canonical JSON with the three paths filled and `base` and the three `blob_sha256`
  values `PENDING-...`.
- `a1-staging-prior.json`: `{"freeze":null,"schema":"oi-a1-staging-prior/1"}`, complete for the initial designation.
- `a1-staging-allow-root.json`: the five re-derived rules, `author` the pending marker.

Every `PENDING-...` value breaks its encoding (a commit id, a sha256, an identity string or a URL), so none of these
skeletons can be admitted by mistake.

## 6. Open questions

- **A. Review placement.** Directory and file names of the ordinary, widening and registry reviews. Proposed: `D_rec`
  (R6.REC.1, records frozen with the plan), with names outside the `a1-staging-allow-` prefix (staging r2: `B` holds
  only the root in that namespace), inside the reviewers' scope (S1.6). Not decided here.
- **B. Widening-review items for a root.** R6.RECON.31 lists widening items as changed elements plus `field:<key>` for
  each other differing top-level key; with `replaces: null` there is no superseded record to compare. Staging r2
  states the item list "covers every initial allow rule". Whether `field:<key>` items are also required for the
  root is not stated; the tool implementation should state it.
- **C. Stops S-2, S-3 and S-6** of `../README.md` remain open; each changes the root's bytes.
- **D. Designations** (supplied separately to the owner): which session is the writer, the scope variant, and the
  two reviewer sessions, each started directly by the owner.
