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

**Checks of identity.** All six branch heads equal the heads in the brief (`git ls-remote`); `main`
is `c3b5f37a`. Blob ids and SHA-256 values in `LANDING-PLAN.md` §5 were computed from the objects;
the ladder's agree with its `OBJECTS.md`, and the BS probe's agrees with BS:300. The landing
candidates at `e1534b08`, `d8e4f80e` and `86a413c8` contain no local path or working-area name.

## Decisions taken in the plan

1. **Order and gates** as the owner fixed them: #1283, then #1274 through its own gates, then one
   combined Bell package (`LANDING-PLAN.md` §1).
2. **BS lands whole and byte-identical**, with its probe. Its line citations from the ladder then
   resolve exactly, and BS:439 makes the probe a gap otherwise.
3. **SB L3 lands as a carried extract**, not as the whole SB draft. The SB results outside the
   owner's option-(c) set (#1169 c.6855167580) stay off `main`.
4. **The ladder lands whole and byte-identical**, NOTES included, because r3 and the confirmations
   cite them.
5. **QH is not preserved by this package.** Its two uses in the ladder are non-load-bearing; the
   stage-7 gap is closed by narrowing in the ladder's STATUS note (`LANDING-PLAN.md` §4).
6. **S5 is provenance for L3.** It checks the CHSH bound for response tables that already factorize,
   not L3's directed-cone step.
7. **Scope checks (owner requirement of 2026-11-14).** #1274 carries N4 at N4's own scope (MI-kept
   routes). The ladder's stage-7 sentence also covers the measurement-dependent branch, which rests on
   Main:360; its §5 settlement criterion adds "and reaches it", which N4 does not contain. L3 names
   Theorem N only; its use with Theorem N′ in the ladder's (MI\*) branch needs a marked, reviewed
   addition in `SB-L3.md`. Every use of Theorem N/N′ is within its accepted scope
   (`LANDING-PLAN.md` §2.5).
8. **Status wording.** The ladder is stated throughout as a conditional paper result, not a native
   OI Bell mechanism.
9. **STATUS-note format** follows #1274's `STATUS.md` and the #1284 notes: accepted record and
   reviews; what the record supports; verification status and remediation with the #1284
   definitions; dependencies; source drift; superseded lines; landing. Hypotheses and Limitations are
   separate sections, as the brief asks. The #1284 notes define "partially verified" and
   "exploratory"; the notes here add one-line definitions of "independently verified" and
   "known-invalid" from §A.46 items 1 and 7.

## Open owner questions

- **OQ-1. #1283 adoption.** Every landing basis in the plan is open until #1283 is adopted. If the
  adopted text differs from `f57e576a`, the condition tables are re-checked against it.
- **OQ-2. Two reviews or one.** #1283 item 8 asks for "an independent non-author review and a
  ChatGPT exact-head review". BS and SB have ChatGPT reviews only; the ladder, #1274 and QH each have
  both kinds. Does a ChatGPT exact-head review that is independent of the author meet both clauses, or
  do BS (Theorem N/N′, §4 and the rest of the record) and SB L3 need a separate non-author review?
  Recommendation: a separate non-author review, as for the other three.
- **OQ-3. Landing form for SB L3.** (B) a carried extract (recommended), or (A) the whole SB draft,
  which would put results the owner left out of #1274's set on `main` and duplicate #1274's corrected
  versions at stale pins.
- **OQ-4. SB L2 and class (a)3.** #1274's gap D3 needs them; the owner's package does not name them
  and the ladder does not use them. Leave D3 open under #1169 (recommended), or add them to the
  extract.
- **OQ-5. Landing form for BS.** Whole record (recommended), or an extract of Theorem N/N′ and §4,
  which would break the ladder's line citations and leave NBA, Lemma G and §§5–6 off `main`.
- **OQ-6. QH as non-load-bearing context.** Accept closure of the ladder's stage-7 QH gap by
  narrowing in the STATUS note (recommended), or require a revision of the ladder text, or preserve
  #1269.
- **OQ-7. SB's historical authorization.** The 2026-11-11 approval cited in #1232's body was not
  located; #1169 c.6854728636 step 5 asks for a current decision to replace it. Which record serves
  for the L3 extract?
- **OQ-8. Probes.** (a) BS's generic probe was run under a writer assignment whose option text reads
  "no runs"; ratify it as covered, as c.6853568040 did for QH's probes, or treat its checks as
  provenance. (b) A replay of `generic_bell_checks.py` from the package head, with a byte comparison
  to its `.out`, is a computation; authorize it with the landing, or land the output as recorded.
- **OQ-9. SB's probe for L3.** Keep S5 as provenance (recommended), or land SB's probe files.
- **OQ-10. Ladder NOTES.** They call themselves "not for landing" but are cited by r3; land them as
  review trail (recommended).
- **OQ-11. This plan directory.** The STATUS notes move into their record directories at packaging;
  this directory stays on its branch as a planning record (recommended), or lands as provenance.
- **OQ-12. Mode.** One pull request; merge commits of `e1534b08` and `d8e4f80e`; landing by merge
  commit (recommended).
- **OQ-13. #1274's STATUS after the package.** Its remediation rows D2 and E2 then name records on
  `main`. Add a forward note in the package (minimal propagation), or leave it to G3.
- **OQ-14. Ladder citations beyond N4's scope.** LD:104's measurement-dependent part rests on
  Main:360, and LD:271's "and reaches it" is not in N4. The ladder's STATUS note records both
  without editing r3 (recommended); alternatively an r4 corrects the attributions.
- **OQ-15. #1231's PR description** still describes r1 ("12/12 PASS", "unreviewed"). Append a
  current status, as was done for #1273, without rewriting the history.

## Not done

- No review of the plan; the owner's authorization provides for one independent review of it.
- No replay of any probe; no CI run; no change to any PR description, Issue or branch.
- `SB-L3.md` is not written; it is a package step (G2).
- QH's sections beyond those the ladder cites, and RC, were not read.
