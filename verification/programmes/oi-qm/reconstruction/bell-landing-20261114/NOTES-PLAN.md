# Notes on the Bell landing plan (#868)

Writer's notes for `LANDING-PLAN.md`: what was read, what was decided, and what is left to the owner.
Paper-only. No computation, commit, push or post was made in writing the plan.

## Sources read

**Owner and governance records, read first-hand through the host API.**
- #868 body and comments, including c.6791565399 (Bell-scope contract), c.6791606126 (writer
  assignment), c.6794392080 (mixed-path unit), c.6853568040 (QH r3, probes ratified), c.6854708572
  (ladder authorization) and c.6873193841 (this plan's authorization).
- #1273 body (with its appended 2026-11-14 current status), comments c.6855862977 and c.6860580909
  (owner decisions Q1–Q4), and review 5892919040.
- #1231 body, comment c.6793517593, reviews 5857227567 and 5857981727.
- #1232 comment c.6794991453, reviews 5858000929 and 5859960068.
- #1269 body, reviews 5891666660 and 5897397957.
- #1274 reviews 5895564670, 5900794367 and 5901837851.
- #1283 body (review trail, R6, C2).

**Records, read with `git show <commit>:<path>`.**
- `BELL-SCOPE-UNIT1.md`, `DISPOSITIONS-r2.md`, the probe and its output at `e1534b08`.
- `SUBSTATE-BRIDGE-UNIT1.md`, `DISPOSITIONS-r2.md`, the probe's S5 section and its output at
  `86a413c8`.
- `Q868H-UNIT1.md` (lines 1–100, 205–220) and `OBJECTS.md` (head) at `ffc9cda4`.
- The twelve ladder files at `d8e4f80e`: r3 in full; NOTES-r3, CONFIRM-r3, OBJECTS in full;
  REVIEW-r1 §§0, 6, 7; RESPONSE-r2; CONFIRM-r2 headings.
- `STATUS.md`, `DEPENDENCIES.md`, `NEW-RESULTS.md` (§0 head, §0.4, §5, §7) and `PROVENANCE.md` §§4–6
  at `fef94857`.
- The §A.46 diff from `c3b5f37a` to `f57e576a` (#1283).
- `oa-2-20261112/STATUS.md` and `oa-1-20261112/STATUS.md` ("Landing") at `6e2d1ee8` (#1284), and the
  definition paragraph in all nine reconciled notes.
- On `main` at `c3b5f37a`: Main:360–416, :652, :724; `Equivalence.lean`:245, :294, :422, :462; spot
  checks of PPS:134–145, OA2:606–613, OA1:176, :556, T1:56, :73, Substratum:131–133; SM:108–112;
  `observer-interface-source.md`:199; the SC-42 integration check (`check_sc42_integration.py`
  §5) and its workflow step.
- `git diff cac5d264 c3b5f37a` for `papers/Main.md`, `papers/SM.md`, `papers/Substratum.md`,
  `book/ch18-beyond.md` and the BS-cited records.

**Review.** `REVIEW-BELL-PLAN-r1.md` in this directory (ACCEPT WITH CHANGES; B1–B2, S1–S14,
N1–N11), read in full; dispositions in `RESPONSE-BELL-PLAN-r1.md`. For S14, the r1 and r2 texts of
L3 were compared with `git show b94b283a:…` and `git show 86a413c8:…`.

**Checks of identity.** All six branch heads equal the heads in the brief (`git ls-remote`); `main`
is `c3b5f37a`. Blob ids and SHA-256 values in `LANDING-PLAN.md` §5 were computed from the objects;
the ladder's agree with its `OBJECTS.md`, and the BS probe's agrees with BS:300. The landing
candidates at `e1534b08`, `d8e4f80e` and `86a413c8` contain no local path or working-area name. The
independent review (`REVIEW-BELL-PLAN-r1.md`) re-derived the blob and SHA-256 values of all sixteen
files, and SB's blob `9ff0f077` / SHA-256 `662b9cba…48fd`, and found that they match.

## Decisions taken in the plan

1. **Order and gates** as the owner fixed them: #1283, then #1274 through its own gates, then one
   combined Bell package (`LANDING-PLAN.md` §1).
2. **BS lands whole and byte-identical**, with its probe, if the owner so chooses (OQ-5). Its line
   citations from the ladder then resolve exactly, and BS:439 makes the probe a gap otherwise.
3. **SB L3 lands as a carried extract**, not as the whole SB draft. The SB results outside the
   owner's option-(c) set (#1169 c.6855167580) stay off `main`.
4. **The ladder lands whole and byte-identical**, NOTES included, because r3 and the confirmations
   cite them.
5. **QH is not preserved by this package.** Its two uses in the ladder are non-load-bearing. The
   stage-7 sentence remains support off `main` and lands as owner-identified non-load-bearing
   context, stated with QH's conditions in the ladder's STATUS note (`LANDING-PLAN.md` §4).
6. **S5 is provenance for L3.** It checks the CHSH bound for response tables that already factorize,
   not L3's directed-cone step.
7. **Scope checks (owner requirement of 2026-11-14).** #1274 carries N4 at N4's own scope (MI-kept
   routes), at all four ladder uses that fall within it (LD:104's MI-kept part, LD:271's bound,
   LD:284, LD:299). LD:104 also covers the measurement-dependent branch: its PR reachability is the
   ladder's check 2, and the absence of a selector rests on Main:360's general sentence and Main:416.
   LD:271's settlement criterion adds "and reaches it", which N4 does not contain. L3 names Theorem N
   only; its use with Theorem N′ in the ladder's (MI\*) branch needs a marked, reviewed addition in
   `SB-L3.md`. Every use of Theorem N/N′ is within its accepted scope (`LANDING-PLAN.md` §2.5).
8. **Status wording.** The ladder is stated throughout as a conditional paper result, not a native
   OI Bell mechanism.
9. **STATUS-note format** follows #1274's `STATUS.md` and the #1284 notes: accepted record and
   reviews; what the record supports; verification status and remediation with the #1284
   definitions; dependencies; source drift; superseded lines; landing. Hypotheses and Limitations are
   separate sections, as the brief asks. The #1284 notes define "partially verified" and
   "exploratory"; the notes here add one-line definitions of "independently verified" and
   "known-invalid" from §A.46 items 1 and 7.
10. **Self-contained STATUS notes.** The notes that land on `main` cite neither `LANDING-PLAN.md` nor
    `NOTES-PLAN.md` (review B1), and state their own package review and merge decision at the
    package head only; the merge decision is quoted in a forward note after landing (review S4).

## Open owner questions

"Writer" is this plan's recommendation; "Reviewer" is the recommendation of the independent review,
`REVIEW-BELL-PLAN-r1.md`.

- **OQ-1. #1283 adoption.** Every landing basis in the plan is open until #1283 is adopted. If the
  adopted text differs from `f57e576a`, the condition tables are re-checked against it.
  - Writer: adopt #1283 first.
  - Reviewer: agree; re-check LP §7 and each note's condition list against the adopted text, and if
    the adopted text keeps the reconciliation sentence, do not apply it to these new records.
- **OQ-2. Two reviews or one.** #1283 item 8 asks for "an independent non-author review and a
  ChatGPT exact-head review". BS and SB have ChatGPT reviews only; the ladder, #1274 and QH each have
  both kinds. Does a ChatGPT exact-head review that is independent of the author meet both clauses, or
  do BS (Theorem N/N′, §4 and the rest of the record) and SB L3 need a separate non-author review?
  - Writer: a separate non-author review, as for the other three.
  - Reviewer: separate non-author review. For BS a full review of r2, because 5857981727 was a
    focused closure of five findings and the only reader of N′ and the six-site member; for SB L3 a
    review of the written `SB-L3.md` with its N′ composition.
- **OQ-3. Landing form for SB L3.** (B) a carried extract, or (A) the whole SB draft, which would put
  results the owner left out of #1274's set on `main` and duplicate #1274's corrected versions at
  stale pins.
  - Writer: (B).
  - Reviewer: (B), with the composition rules of review S7.
- **OQ-4. SB L2 and class (a)3.** #1274's gap D3 needs them; the owner's package does not name them
  and the ladder does not use them.
  - Writer: leave D3 open under #1169.
  - Reviewer: leave D3 open under #1169; note in the L3 STATUS note that "however deep" stops at
    finite depth without L2 (done).
- **OQ-5. Landing form for BS.** Whole record, or an extract of Theorem N/N′ and §4, which would break
  the ladder's line citations and leave NBA, Lemma G and §§5–6 off `main`. The whole record lands
  Lemma G, NBA, §5 and §6, beyond the components named in c.6873193841, each with its own STATUS
  row; this is an explicit owner choice.
  - Writer: whole record.
  - Reviewer: whole record, asked as an explicit choice that lands content beyond "Theorem N and N′";
    after the decision, update the appended status of #1273.
- **OQ-6. QH as non-load-bearing context.** The stage-7 sentence lands unchanged, stated in the
  ladder's STATUS note as off `main`, conditional on NNB, P2 and H-PREP, and non-load-bearing.
  Should the merge decision also record it under §A.42 item 8's final sentence, as a named claim left
  unsupported?
  - Writer: yes; no ladder r4, and #1269 not preserved for this sentence.
  - Reviewer: the same; do not write r4, given #1169 c.6865177667 ("Do not write narrowing revisions
    just to unblock integration"), and do not preserve #1269 for this sentence.
- **OQ-7. SB's historical authorization.** The 2026-11-11 approval cited in #1232's body was not
  located; #1169 c.6854728636 step 5 asks for a current decision to replace it. Which record serves
  for the L3 extract?
  - Writer: an owner decision covering the extract.
  - Reviewer: required before G2; c.6873193841 is planning-only and does not replace it; fold it
    into the G2 merge decision, worded to cover the L3 extract explicitly.
- **OQ-8. Probes.** (a) BS's generic probe was run under a writer assignment whose option text reads
  "no runs"; ratify it as covered, as c.6853568040 did for QH's probes, or treat its checks as
  provenance (the BS STATUS note now says so until ratification). (b) A replay of
  `generic_bell_checks.py` from the package head, with a byte comparison to its `.out`, is a
  computation; authorize it with the landing, or land the output as recorded.
  - Writer: (a) ratify; (b) authorize the replay with the landing.
  - Reviewer: (a) ratify, otherwise the [X] tags are provenance; (b) authorize the replay as a
    package check (generic, deterministic, no OI rule; §A.42 item 1).
- **OQ-9. SB's probe for L3.**
  - Writer: keep S5 as provenance.
  - Reviewer: S5 as provenance, marked as such inside `SB-L3.md`.
- **OQ-10. Ladder NOTES.** They call themselves "not for landing" but are cited by r3.
  - Writer: land them as review trail.
  - Reviewer: the same.
- **OQ-11. This plan directory.** The STATUS notes move into their record directories at packaging,
  and after review B1's replacements they no longer cite this directory.
  - Writer: this directory stays on its branch as a planning record.
  - Reviewer: keep it off `main` only once every reference to it is removed from the landed notes
    (done); otherwise land it as provenance.
- **OQ-12. Mode.** One pull request; merge commits of `e1534b08` and `d8e4f80e`; landing by merge
  commit.
  - Writer and Reviewer: as stated.
- **OQ-13. #1274's STATUS after the package.** Its remediation rows D2 and E2 then name records on
  `main`. Add a forward note in the package, or leave it to G3.
  - Writer: a forward note in the package.
  - Reviewer: a forward note in the package, keeping #1274's "conditional on L3" and "conditional on
    L2 and Theorem N" wording, and adding nothing that changes #1274's status.
- **OQ-14. Ladder citations beyond N4's scope.** LD:104's measurement-dependent part rests on check
  2, Main:360's general sentence and Main:416, and LD:271's "and reaches it" is not in N4.
  - Writer: the ladder's STATUS note records both without editing r3.
  - Reviewer: the same, with the corrected attribution of review S1 and the added use LD:284 of
    review S2 (done).
- **OQ-15. #1231's PR description** still describes r1 ("12/12 PASS", "unreviewed").
  - Writer: append a current status, as was done for #1273, without rewriting the history.
  - Reviewer: the same (it also calls the bound "tight" without scope); after OQ-3 and OQ-5, also
    append to #1232's description and update #1273's appended status.

## Not done

- No replay of any probe; no CI run; no change to any PR description, Issue or branch.
- `SB-L3.md` is not written; it is a package step (G2).
- QH's sections beyond those the ladder cites, and RC, were not read.
