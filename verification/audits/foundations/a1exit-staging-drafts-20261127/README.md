# A1 retirement staging drafts: allow root, rule records, parity script

**Status: WIP / UNVERIFIED staging drafts. Not frozen, not reviewed, not adopted, not admitted.** Nothing here is a
review record, an owner adoption, an activation, a freeze or a trial. Checklist items 4.3, 4.4 and 4.10 of the
consolidated A1 retirement checklist, version 1 (#1169 comment 7207860923).

**Authority.** Owner decision of 2026-11-27 (`amaybaum`, received 2026-11-27 in the coordinating session, recorded
at #1169 comment 7207765697, 2026-11-27T02:01:22Z), item 3: "In parallel, prepare and independently review the
remaining retirement staging requirements wherever dependencies permit." Item 4 of the same decision bars expanding
the verification infrastructure beyond the adopted requirements. Freezing, admission, activation and trials are
not authorized (AGENTS.md sec. A.50 items 2 and 5).

**Goal link.** Retirement staging items 4.3, 4.4 and 4.10. The drafts decide nothing; their reviews would decide
whether the five allowances, the deny set and `resid`, and the OBL-1/OBL-2 comparisons can be frozen at `F`.

The JSON records cannot carry this README's text beyond their `status` field; the parity script's expected output
carries no status field because it must equal the script's output byte for byte. This README is the WIP marker for
both.

## Files and the design clauses they serve

| File | Item | Design clauses |
|---|---|---|
| `../a1exit-deletion-20261121/a1-staging-allow-root.json` | 4.3 | staging amendment r2 (tool branch, `a1exit-staging-amendment-20261126/AMENDMENT.md`) sec. 2 "Placement and exact designation", "Allow-rule record", "Initial widening review"; R6.RULE.1, .2, .4 to .12; R6.REC.2, .6, .7, .13, .14; R6.DENY.5; OBL-3; the fixed selector in `tools/ledger_coverage/record_authority.py` (`transition_roles[1]`: directory `D_rec`, root `a1-staging-allow-root.json`, `record_id` `a1-staging-w1-w2`, schema `oi-term-rules/2`) |
| `../a1exit-deletion-20261121/dr-deny.json` | 4.4 | R6.RULE.1, .3, .10; R6.DENY.1, .3, .5; OBL-3 (DR-1 alternatives a, b, c; DR-3; DR-4; DR-5); OBL-4 (the terminology decision DR-1a/b encode is plan text, not drafted here); R6.A1CFG.2 (rule files under `rules`; DR-3's witness under `controls`) |
| `../a1exit-deletion-20261121/resid.json` | 4.4 | R6.DENY.1, .4, .5, .6; OBL-3 (resid-a, resid-b, resid-c); OBL-5 |
| `derive_rule_drafts.py` | 4.3, 4.4 | the writer's derivation and evidence (R6.REC.2); reviewers re-derive without it |
| `derive-report.json` | 4.3, 4.4 | its output at H (every check, fingerprint line numbers at H and `X_rep`, the classification sweep) |
| `../a1exit-parity-20261127/obl12_parity.py` | 4.10 | OBL-1, OBL-2, R6.PROF.12, the sec. 32 evidence table (OBL-1: kind 4 at `F` by a script on `main` before `F`; OBL-2: kind 2) |
| `../a1exit-parity-20261127/expected-output.json` | 4.10 | the script's output at the inputs it names |

`D_rec` is `verification/audits/foundations/a1exit-deletion-20261121/`, the one admitted record directory
(`record_authority.authorized_record_directories`, R6.PLACE.4, R6.RDIR.2). The plan itself lives on PR #1477's
branch (`research/a1exit-deletion-20261121`, head 4c79be64); on this staging branch `D_rec` holds only the three
drafts, at the paths the plan would carry them. The design fixes the allow root's file name; it fixes no file names
for the deny and `resid` files (R6.PLAN.12 names `repo-scope.json` and `repo-rules.json` for item 11 only), so
`dr-deny.json` and `resid.json` are proposals. No other file in `D_rec` starts with `a1-staging-allow-`.

## How the drafts were derived

Recipe (from the repository root, any checkout holding the objects):

```
python3 -I verification/audits/foundations/a1exit-staging-drafts-20261127/derive_rule_drafts.py \
  --repo . --tool . --out verification/audits/foundations/a1exit-deletion-20261121 --check
python3 -I verification/audits/foundations/a1exit-parity-20261127/obl12_parity.py --repo . --tool . \
  | cmp - verification/audits/foundations/a1exit-parity-20261127/expected-output.json
```

Expected: the first prints `derive-report.json` with every `on_disk_equal:*` true; the second prints nothing and
exits 0 (`"holds": true`). Both are deterministic (checked under two hash seeds).

**Eligible bytes.** Only H (`53c6601a10419b6b333cc992474272501ab542af`, on `main`), the R6.EVID.8 pins of the
ledger (blob `ba37c1cd`, sha256 `2055e68f…`) and edit list (blob `ec384fdf`, sha256 `528f146d…`), P's checker
(sha256 `2856e58c…`; on `main` at `3e73633308bdef99f65f6117733aaf86097c7b22` as the design's
`inputs/edits_check.py`), the profile sources at their pinned commits, and the superseded drafts on the tool branch
(custody inputs) are read. `T1'` is never read. `X_rep`'s ledgered files are rebuilt from H and the ledger and
match every `expected_sha256`.

**Allow root.** Each of W1-b, W1-c, W1-d, W2-a and W2-b keeps the superseded draft's profiles, scope, matcher,
`context_required`, fingerprinted sentences, `negative_allowance` (W1-c `finit: 1`, recomputed), positive examples
and reason. What changes: `recorded_at` is H (stop S-2), each `context_sha256` is recomputed at H, `author` is the
placeholder of stop S-1, and the W1-a sentence (papers/SM.md at H, "…satisfying the six structural properties.
…") is appended to every rule's negative examples so that the lint itself exercises the adverse case. Results at H
(`derive-report.json`): every rule passes the tool's own `rules.lint_rule` with `recorded_at` H; all ten
fingerprinted sentences are unique at H and at `X_rep`; contexts are equal at H and `X_rep` except W1-d's two
(harmless only because W1-d has `context_required: false` and no allowance); the sweep of every profile hit in the
scope files at H and at `X_rep` classifies exactly the ten fingerprinted sentences (W1-c's two lines keep their
`ledger-ext` "periodic quotient" hit unclassified, as the earlier review found); the W1-a sentence's one hit
(`count-grep`) stays REVIEW_REQUIRED `unclassified`, and no rule's matcher holds for it even out of scope.

**W1-a: documented exclusion.** W1-a is not in the root under any id. The adverse review (#1577 comment
7187883838, F1/F2) found no valid justification: SM does not define "the six structural properties", the G2 list is
an output list, and the most plausible referent, A1–A6, includes the retired posit. SM:1394 at H therefore stays
REVIEW_REQUIRED under `count-grep`, and RT-D's expectation is the ten W1/W2 lines, not eleven.

**Deny and `resid`.** Patterns, levels, combine, scope, examples and countercontrols are byte-equal to
`dr-deny-v1.json` and `resid-v1.json` (tool branch), so the configuration's staged `pattern_sha256` pins still hold;
the reasons now cite r6 clauses instead of design v6.0e; new `record_id`s (`a1-plan-deny-dr`, `a1-plan-resid`) with
`supersedes: null`, because a plan record in `D_rec` reusing `a1-deny-v1` or `a1-resid-v1` without a supersedes chain
is a reused `record_id` (R6.REC.7). All four deny rules and `resid` pass `lint_rule` (countercontrols at H:
FULL:6504, glossary:13, ch09:104, FULL:718, Substratum:92, Main:736, and AGENTS.md's sentence at line 37 through the
control input `agents-md-at-H`). Deny matches over the corpus (lines plus sentences): 190 at H (DR-1 132, DR-3 0,
DR-4 56, DR-5 2), 0 at `X_rep`.

**Parity.** All comparisons hold at the pinned inputs: the three per-edit profile pins; P's sentence regex equals the params
`splitter` and splits all 802 edit texts identically; the A1 edit list gives 0/0/0 under both; 24 crafted cases
and 4000 seeded random cases (3722 with findings) give no difference; 401 edits, 399 splices bound, retained D032
and D039, no `old_step2`, no engine correspondence error, and P's own application reproduces all 44 files'
`expected_sha256`; 20000 seeded random selection cases split 2518 accepted / 17157 refused by both / 325 chained
(P applies, the engine refuses) / 0 differences. Countercontrols (five perturbed params and 200 shifted splices) are
all detected.

## Reviews required (three distinct identities: writer, ordinary reviewer, widening reviewer)

No review record is written here. Each review is a separate `oi-review-record/1` file bound by exact path and blob
sha256 to the exact candidate, by a non-author, re-deriving from the git object store (R6.REC.2, R6.REC.6). A review
citing only a passing tool run, or this README, or `derive-report.json`, is invalid.

**Ordinary reviewer of the allow root** (identity distinct from the writer):
1. Schema `oi-term-rules/2`, `record_id` `a1-staging-w1-w2`, `supersedes: null`, path exactly
   `D_rec/a1-staging-allow-root.json`, regular file; rule ids exactly W1-b, W1-c, W1-d, W2-a, W2-b.
2. For each of the ten fingerprints: read the file at H from the object store, split with splitter version 2 and the
   configuration's abbreviations, recompute `sentence_sha256` and `context_sha256` (R6.RULE.5); rebuild the file at
   `X_rep` from H and the ledger and confirm the sentence there, and that its context matches except W1-d.
3. Lint by hand (R6.RULE.10–.12, R6.REC.14): exact-path scopes with mirrors named; literal of at least 8 characters
   covering every trigger span; `max_instances` equal to the fingerprint count; W1-c's `negative_allowance` equal to
   the count of `finit` in its sentence; each fingerprinted sentence a full positive example that passes its own rule;
   each negative example rejected.
4. No overreach: every profile hit in the scope files at H and at `X_rep` that some rule covers is a fingerprinted
   sentence; the W1-c lines keep their `ledger-ext` hit.
5. The W1-a adverse case: the SM sentence at H is classified by no rule, under any profile hit, in or out of scope;
   no literal is a generic "six structural properties" allowance under another id.
6. Each reason is true of its text: W1-b/W1-d count the enumerated or "of the bijection" six, which exclude
   finiteness; W1-c's one `finit` lies in "finite periodic quotient … a qualified case of A4"; W2-a/W2-b are the
   anomaly-condition label (A1), unrelated to the posit. Decide stop S-3 for W1-b, W1-c and W1-d.
7. Item list: one verdict per rule id, each `accept`, with the object ids read named in `method`.

**Widening reviewer of the allow root** (a third identity, distinct from writer and ordinary reviewer; staging r2
sec. 2 "Initial widening review"; R6.REC.13):
1. `replaces` present as JSON `null`; valid only because this record is the exact designated root with
   `supersedes: null`; `reviewed` names the same path and digest as the ordinary review.
2. Verdicts cover every initial allow rule (all five, each a new allowance, so every field is a widened item), each
   `accept`.
3. For each allowance: a hit exists at the candidate that needs it; the scope, fingerprints and `max_instances` are
   minimal; no allowance is W1-a or equivalent; the allowance does not reach any sentence the A1 retirement must still
   review (re-check against the deny set and the W1-a sentence).
4. Base dependence (stop S-3): whether W1-b, W1-c and W1-d remain justified, given the owner's classification of
   ch09:36/137 and ch19:198/212 as defective passages (#1169 comment 7186075741 item 2) and their absence at current
   `main`.
5. The mandatory negative cases of staging r2 (successor, omitted field, wrong path, invented predecessor) and
   STAGING-FIRST-ALLOW are tool controls, not this review; the reviewer confirms they exist and hold at the tool
   candidate before activation.

**Ordinary reviewer of `dr-deny.json` and `resid.json`** (distinct from the writer): patterns byte-equal to the
v1 drafts or each re-judged; every countercontrol a real line or sentence at H (R6.RULE.3: no constructed text);
examples behave; DR-1's ordinal alternatives match the OBL-4 terminology decision the plan amendment states; the
V4/V27/V15 residuals of R6.DENY.6 (owner decision 3) are `resid`'s negatives; zero deny matches at `X_rep`; reasons
true; one verdict per rule id. My reading of R6.REC.13 is that new deny and review-pattern records with
`supersedes: null` need no widening review (only "a new allow rule without `supersedes`" is listed); the reviewer
confirms or rejects that reading.

**Reviewer of the parity script** (distinct from the writer): P is executed from its pinned blob as itself, never
retyped; the 2b base mapping is the script's own, not the engine's `Running`; every input is read by object id and
checked by sha256; the countercontrols detect each perturbation; output is deterministic; the comparison at `F`
re-runs with `--checker F:<D_rec>/edits_check.py --checker-sha <its sha256>` and the landed params rule file, and the
script itself is on `main` before `F` (OBL-1, OBL-2 evidence kinds); decide stop S-5.

## Stopped points (each needs a design or owner disposition)

- **S-1, writer and reviewer identity.** Staging r2 sec. 2: each root carries "the independently verified GitHub
  identity of its actual author", and "the writer, ordinary reviewer and widening reviewer are distinct eligible
  identities". Agent sessions commit as one generic identity and write to GitHub through the owner's account, so no
  GitHub identity distinguishes them. The drafts carry the placeholder `a1-staging-writer-20261127`. Recommended
  default: the owner fixes the identity convention before review (distinct GitHub accounts, or session designations
  recorded in the owner's activation record and used verbatim as `author` and `reviewer`), and the candidate is re-cut
  with the designated writer's identity.
- **S-2, which commit is "eligible" for `recorded_at`.** Staging r2 sec. 2 and R6.REC.14 ask for re-derivation
  "from eligible pinned bytes" without naming the commit; R6.EVID.8 excludes `T1'`, and `X_rep` is not a commit in the
  repository. Recommended default: `recorded_at` = H with contexts taken at H, as drafted; the alternative is the
  plan's final candidate once item 4.1 fixes it.
- **S-3, W1-b, W1-c, W1-d depend on the base.** Their sentences (ch09:137, ch19:198, ch19:212 and the FULL mirrors)
  exist at H and `X_rep` but not at `main` `7fe011f5af64023331f235691b5549528348f539`, after the owner-approved book
  correction (#1169 comment 7186638587 item 1); W2-a and W2-b exist at all three. If item 4.1 rebases the plan past
  that correction, W1-b..d have nothing to classify and fail lint at a new `recorded_at`. Staging r2 says the root
  "may carry exactly" the five; whether it may carry fewer is not stated. Recommended default: keep the five for the
  ledger base H = 53c6601a; if H moves, re-derive and carry only the rules whose sentences exist there, and treat any
  rule the widening reviewer cannot justify as blocked for a separate decision, as staging r2 requires.
- **S-4, the converted `EXPLAINED` entries (OBL-3; R6.A1CFG.2; R6.PLAN.12 `repo-rules.json`).** Not drafted. P's
  `EXPLAINED` has 52 entries: 4 are the appendix-B and FULL anomaly lines that W2-a/W2-b replace; 26 are whole-file
  or prefix entries with no literal, which no R6.RULE.2 allow rule can express (a literal covering the trigger and a
  fingerprint per sentence are required); 12 are `pending R-1` entries that P's `--final` rejects, so an allow rule for
  them would turn P's failure into a PASS; the rest are substring entries. Recommended default: substring entries of
  the classes `unrelated label`, `historical record label`, `preserved historical evidence` and `registry identifier
  (kept)` become fingerprinted exact-path allow rules at the final base; whole-file entries become explicit
  `repo-scope.json` entries under their own widening review (R6.RULE.13); `pending R-1` entries stay
  `final-unclassified` until the owner's rename decision R-1.
- **S-5, OBL-2's figures.** The design-time scripts (`work-v55/parity55.py`, `work-v54/parity.py`) were not
  retained, so 2822 / 16905 / 273 and the "4000 regression cases" cannot be recomputed as stated; the retained script
  recomputes 401 / 399 exactly and reports its own seeded counts. Recommended default: discharge OBL-2 by its stated
  narrowing ("measured during design, not retained") for those figures, with this script's seeded counts recorded as
  the retained measurement of the same comparison; that a new seeded generator counts needs a design ruling.
- **S-6, `status` text in immutable records.** The drafts carry a WIP `status` because the schema permits it, but a
  reviewed record keeps its bytes for ever (the v1 review raised the same point). Recommended default: before review
  the writer re-cuts each candidate with a timeless `status` (or none), and the reviews bind that exact blob.

## Dependencies that invalidate the drafts if they change

The configuration's sentence abbreviations and profile specs (copied from the last staged configuration; item 4.8);
H and the ledger and edit list (item 4.1 may rebase them); P's checker as frozen at `F`; the params rule file and
the engine files named in the parity output (`engine_files_sha256`), that is the final tool candidate (item 2.15).
A change to any of them requires re-running both recipes and new reviews.

## Observation

An edit carrying `old_step2` without `new_step2` raises `KeyError` in both P's `variant` and the adapter's
`pairs_of` (P's `static_new` ignores such a pair). The edit list has no such edit; the parity script generates none.
Recorded for the tool reviewers; no tool change is made here.
