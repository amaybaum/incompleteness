# Independent review r1 of INTEGRATION-ASSESS-r1 (#1169, draft PR #1279)

**Verdict: ACCEPT WITH CHANGES.** The mechanical claims all reproduce. Every §A.42 item 8
classification I spot-checked holds, and none of the "gap" rows is in fact on `main`. The landing
order respects the dependencies, and the gates match the ChatGPT review texts. Nothing in the
assessment overreaches: it implies no authorization, promotes no claim and proposes no manuscript
edit. Still, ten changes are needed before the proposals go to the owner:

- **Three stale-state errors**, all from head movement or records posted before the assessment
  commit (F1–F3). The most consequential: #1275's branch now carries unit 2(a) r1, which is
  unreviewed, and the owner directed that unit 2(a) continue on that branch. Step 2 therefore cannot
  be done "any time".
- **Two incomplete dependency treatments** (F4, F5).
- **An unflagged and inconsistently applied §A.46 item 2 basis** (F6).
- **Four corrections to the #1274 `STATUS.md` proposal and its rationale** (F7–F10).

Eight Low findings follow. None of the findings is blocking for a read-only proposal record.

**Object.** Branch `research/integration-assess-20261113`, fetched by name with full history, at
exact head `79b4d4cd1936db107cd41f89dc403252c5a4b831`. It is a single commit on `main`
`c3b5f37a354bb26437e2e0165c576a347a63c153` and adds the two files only. Line numbers are
`INTEGRATION-ASSESS-r1.md` (IA) and `NOTES-r1.md` (N) at that head. Authority read through the host
API: #1169 c.6863414487 and #1274 c.6863419164 (both `amaybaum`, 2026-11-13T19:58Z). I also read
#873 c.6863416405, #1268 c.6863418087 and c.6863753317, #1273 c.6860580909, and #1265 c.6846206075.

**What I ran** (git read commands and repository check scripts only; nothing written to any branch):
- `git merge-tree --write-tree origin/main <head>`.
- `git diff --name-status c3b5f37a <head>`.
- The assessment's local battery: `artifact_placement_check`, `claims_check`, `staleness_check`,
  `voice_check`, `duplicate_check`, `dependency_label_check --strict`,
  `legacy_records_check <full id>`, `citation_roles_check <full id>`, and
  `check_sc42_integration.py --verbose` compared with `cmp` to the committed result.
- `v3_verifier.py --receipts e81e4fb2…`.
- Check-run and job-step conclusions through the host API.

**Heads.** I read each PR at the head the assessment pinned and at its current head:

| PR | Assessment's head | Current head | Change |
|---|---|---|---|
| #1268 | `2a9f10ba` | `3a3aa146` | `+REC-1-r9.md`, `REC-1-NOTES-r9.md`, `REC-1-CONFIRM-r9.md` |
| #1275 | `e81e4fb2` | `46a548fb` | `+G3-UNIT2A-r1.md`, `NOTES-U2A-r1.md` |
| others | as listed in IA §1 | unchanged | none |

***

## Answers to the review questions

1. **Dependency claims.** At least two classifications per PR were checked against the citing claim.
   - **#1274.** Row B: `ExecSource.lean:52` is `exists_nonMonomial_of_layerFlowExecutable`, and
     GR:266 names it. Rows E3/E4: Main:412 carries "bounded-degree long edges"; Main:414 carries the
     window Δt/√3 < d ≤ Δt/‖n̂‖₁ and "outside ledger item (vii)". Row F: Main:362. Row H: `REC-1-r7.md`
     is blob `f1ffac0e` at every REC-1 head through `3a3aa146`.
   - **#1268.** r8 §6, rows C6, C11 and OC1:359–363, read against r8:400–403.
   - **#1272.** §7 rows C4, C6 and 3A:896–905.
   - **#1273.** §6 rows SB, QH and OA2.
   - **#1269.** The OBJECTS.md item 8 section. `ASSESS-868.md` and `REVIEW-868-r3.md` match the cited
     sha256 values `d97c4b6b…` and `2a5014a5…`, and `fd539e15` is an ancestor of `main`.
   - **#1270.** ARP-1-MARC `preregistration.md`:124 and :885. `PACKAGE.md` sha256 `33075f9f…`,
     `AUDIT-C3.md` `d143754b…`, and `PACKAGE.md`:413.
   - **#1276.** §8 rows OC and DEP, and the on-`main` pins Main `0db17597` and OA2 `8f8ddf73`.
   - **#1275.** W1-1 r4, `AUDIT.md` and `ROADMAP.md` are on `main`; its review commits are ancestors of
     `e81e4fb2`.
   - **Off-`main` ids.** Every off-`main` id the assessment lists as a gap is off `main`
     (`git merge-base --is-ancestor`, 17 ids).

   No provenance row is in fact support, and no gap is on `main`. The exceptions are in how rows are
   attributed and in completeness: F4, F5, F12, F13, F14.
2. **Mechanical claims.** All reproduce.
   - **merge-tree.** Exit 0 with a single tree line for all eleven heads, current heads included.
   - **Add-only, disjoint.** Every PR is add-only (status `A` only), each under its own directory, and
     no path is added by two PRs. This holds at the current heads too.
   - **Battery.** It exits 0 on `main` (control) and on every head, with two exceptions:
     - `ffc9cda4` (#1269): SC-42 FAIL, "added-text scan: 3 hit(s)", at `ASSESS-868.md`:142, :151 and
       `REVIEW-868-r3.md`:67.
     - `4cd39871` (#1270): SC-42 FAIL, 8 hits, all in the six files named at N:61–63; and
       `claims_check` FAIL at `eoi-package/eoi-audit/AUDIT-C5.md`:149.
   - **Added ids.** The added 40-hex ids number 10, 16, 4, 3, 3, 55, 3, 6 and 102, and all resolve.
     Sensitive-pattern scan: 0 hits on every head.
   - **CI.** Matches N:71–77, with one correction (F13).
3. **The §A.46 item 2 basis.** The #1265 reading is the owner's own recorded pattern (c.6846206075:
   "one status note per unit naming the claim it supports"; merged as `c3b5f37a`). Following it is
   defensible. It is not item 2's literal text, however, and the assessment applies it unevenly (F6).
4. **Landing order and gates.**
   - **Order.** The order respects every support edge.
   - **Gates.** Each gate matches its review:
     - #1274: 5895564670, items 1–3.
     - #1268: 5896999901, items 1–2 and "Existing #1214/#1267 off-main support gaps remain
       integration gates".
     - #1272: 5892912253.
     - #1273: 5892919040, safeguards 1–2 and owner Q1–Q4.
     - #1275: 5896999577, "Important limit" and Q4/Q7/Q8.
     - #1276: 5896999231.
     - #1269: 5891666660. The newer recheck is missing (F2).
   - **`STATUS.md` for #1274.** It is consistent with §A.27 and §A.30 as a status artifact in the
     #1265 idiom. It needs F7 (§A.46 items 1 and 4) and F8 (§A.28: it lists true lines as superseded).
   - **DEPENDENCIES:18 nit.** Skipping it is right, but the stated reason is wrong (F9).
5. **What must wait.**
   - **The list.** It is correct, except that #1275 now belongs on it (F1), and #1268's and #1269's
     review states are stale (F2, F3).
   - **#1270.** Its problems are stated accurately: no review, CI red, references untraced, and owner
     decisions relayed rather than quoted. Two caveats: the PR body's own standing ("Preservation
     only. Not for merge.") is not quoted, and N:109–111 contradicts IA:377–378 (F6).
6. **Overreach.** None found.
   - Merge authority is disclaimed in IA:3–7 and on every step.
   - The manuscript points are flagged as follow-ons (IA:537–555).
   - Dropping "(WIP)" from PR titles is a draft-PR update within c.6863414487.
7. **Register and barred strings.** Both files are clean. A grep for the four path prefixes and the
   session-storage word finds no match, and the battery and SC-42 pass at `79b4d4cd`.

***

## Findings

### F1 (Medium). #1275 is no longer landable "any time": its branch now carries unreviewed unit 2(a), by owner direction

- **Where:** IA:20–24, :35–37, :73, :349, :430–439, :573; N:103.
- **Evidence.**
  - `research/g3-offset-873-20261113` is at `46a548fb`. That head adds `G3-UNIT2A-r1.md` and
    `NOTES-U2A-r1.md` ("unit 2(a) r1 … (WIP / UNVERIFIED)"), which are not yet reviewed.
  - #873 c.6863416405 (`amaybaum`, 2026-11-13T19:58:10Z), Q4: unit 2(a) "continues on #1275's
    branch". The same comment records Q7 and Q8. IA:435 makes those answers conditional on their
    being "recorded on #873", which they are.
  - Landing the PR head would land unit 2(a) unreviewed. Landing unit 1 alone would need a separate
    branch at `e81e4fb2`.
  - CI at `46a548fb`: Mathlib bridge succeeded and "Numerical probes" was queued. This confirms that
    the `e81e4fb2` failure was an installation failure.
- **Fix.**
  - Re-pin #1275 at `46a548fb`.
  - Retitle IA:349 to "**#1275 G3 unit 1 — wait for unit 2(a) review or a separate unit-1 landing
    branch**".
  - Replace IA:430 with "### Step 2. #1275 (after unit 2(a) r1 is reviewed, or from a separate
    branch at `e81e4fb2`)". Add as item 0: "The branch carries unit 2(a) r1 (`46a548fb`), unreviewed;
    by #873 c.6863416405 it continues there. Either (a) land after unit 2(a) has its independent
    review and ChatGPT exact-head review, with both units in `STATUS.md`, or (b) on an owner decision,
    open a landing branch at `e81e4fb2` plus `STATUS.md`. Option (b) involves no movement of the
    research branch (§A.43 item 4)."
  - At IA:435, quote c.6863416405 for Q4/Q7/Q8 with author and time.
  - Add #1275 to the §5 table with the reason "unit 2(a) r1 unreviewed on the same branch".
  - Reword OQ-6 to the (a)/(b) choice.

### F2 (Medium). #1269 has a ChatGPT exact-head review at `ffc9cda4`, posted before the assessment

- **Where:** IA:38–41, :322–327, :458, :522.
- **Evidence.** Review 5897397957 on #1269, commit `ffc9cda4`, 2026-11-13T20:15:15Z. The assessment
  commit is 20:21:28Z. The review reads "ACCEPT — both prior documentation nits resolved, scientific
  verdict unchanged", and it gates integration: "the off-main ASSESS-868 support, retained
  original-byte SC-42 hits and §A.42 obligations need separate treatment, along with an explicit
  owner landing decision."
- **Fix.**
  - At IA:39–41, replace "and an exact-head ChatGPT review (the review on file is at `acf28d3a`, not
    the head `ffc9cda4`)" with "and a ChatGPT exact-head review of the prepared head (the focused
    recheck 5897397957 at `ffc9cda4` accepts the two nit commits)".
  - At IA:324, replace "no ChatGPT review is at the head" with "ChatGPT focused recheck 5897397957 at
    `ffc9cda4`: ACCEPT, nits resolved".
  - Add the recheck's integration sentence to the Gates bullet.
  - At IA:458, add 5897397957 to the review trail.
  - In IA §5, #1269 row, delete "no exact-head ChatGPT review at `ffc9cda4`".

### F3 (Medium). REC-1 r9 is confirmed, and a later owner record changes P5

- **Where:** IA:20–23, :42–44, :269–271, :466, :473–476, :518; N:100–102.
- **Evidence.**
  - `3a3aa146` adds `REC-1-CONFIRM-r9.md`: "**Verdict: ACCEPT.** No changes are required."
  - #1268 c.6863753317 (`amaybaum`, 2026-11-13T20:14:06Z) sets r9's P5 to name the C3 check, which
    was authorized at #1169 c.6863414487.
  - Blobs r7 `f1ffac0e`, r8 `615b7de8` and P0 r3 `611a4d9a` are unchanged at `3a3aa146`.
- **Fix.**
  - At IA:466, write "1. r9 (`2594d474`) has its focused check, `REC-1-CONFIRM-r9.md` ACCEPT at
    `3a3aa146`; a ChatGPT exact-head review is outstanding."
  - At IA:474–475, add #1268 c.6863753317 and #1169 c.6863414487 to the owner records.
  - At IA:518, replace "r9 unchecked" with "r9 lacks a ChatGPT exact-head review".
  - Update the pins at IA:21–22 and N:100–102.

### F4 (Medium). QPHEN r5 gap: only landing is offered, though the files are hypotheses, and landing them brings untraced references

- **Where:** IA:39–40, :200–201, :449–453, :575–576.
- **Evidence.**
  - `ASSESS-868.md` r3a at `ffc9cda4` lists BRIDGE-UNIT1 and the QPHEN r5 texts together under
    "**Draft inputs (D; hypotheses per §A.46 item 7)**" (:141–155). The same block says
    `REVIEW-PHASE1-r4.md` "is REVISE (narrow) on r4".
  - The assessment offers narrowing for BRIDGE-UNIT1 (step 3.3, OQ-5) but only landing for QPHEN
    (step 3.2).
  - The four files are hash-matched: sha256 `a7206701`, `9e9c0d02`, `7f4cd21d` and `755c3af0`. They
    cite content not on `main`: `oicore/OICORE-1.md` (#1214), `arp/qc21/DECISIONS.md`,
    `lg_comb_probes.py`, `p6_r3rev_lg.py`, `REVIEW-PHASE1-r3.md` and a working copy `main_fd.md`.
  - #1270's README says its references "were not each traced".
  - Landing the four files as proposed would therefore put records on `main` whose own item 8 trace
    has not been done, and whose last review was REVISE.
- **Fix.** Replace step 3.2 with: "**QPHEN r5 gap.** Either (a) land the four hash-matched files, each
  with its own §A.42 item 8 table, its SC-42 disposition and a stated status (REVIEW-PHASE1-r4 is
  REVISE on r4; not established, §A.46 items 3–4), from #1270's subset or beside #1269 (OQ-7); or (b)
  narrow: state in `STATUS.md` that every Q-868-H verdict that uses a QPHEN r5 row is conditional on
  it as a named draft hypothesis, as ASSESS r3a §2 already labels it." Mirror the change at IA:39–40
  and in OQ-7.

### F5 (Medium). Under OQ-2(b), REC-1 r7's rows keep an off-`main` dependency that step 5.1 hides

- **Where:** IA:471–472, :482–484, :506.
- **Evidence.**
  - r8 §6 classifies C6's "undetermined" status as "Support off `main`" through 3A:501 (#1267).
  - The C6 and C9 rows are byte-identical in r7, r8 and r9 (checked).
  - #1272 §7 uses "REC:217 (C6)", which is r7, for that status word. #1276 §8 uses R7 for C4–C7.
  - If #1268 closes its gaps by a narrowing r10 (OQ-2(b)), `REC-1-r7.md` lands with C6 unchanged. A
    #1272 or #1276 row re-pointed to r7 "on `main`" would then rest on a record whose own support for
    that cell is off `main`.
- **Fix.** At IA:482, append: "Under OQ-2(a) this holds as stated. Under OQ-2(b), re-point #1272's C6
  and C9 rows and #1276's R7 rows (C4–C7) to the narrowed r10 rows, or state them conditional on
  #1267; r7 on `main` does not close them." At IA:506, add "(and, under OQ-2(b), the R7 rows)".

### F6 (Medium). The §A.46 item 2 basis is unflagged in IA, and it is applied unevenly

- **Where:** IA:249–252, :274, :287, :303, :315–316, :344–345, :362–363, :380–381; N:108–111.
- **Evidence.**
  - Item 2 admits evidence that "an established claim needs", or that is needed "for reproducibility
    or to support records already on `main`". IA:5–6 itself says landing "establishes nothing", and
    model ACCEPT is not verification (5895564670, item 1).
  - The #1265 basis is owner practice: c.6846206075, merged as `c3b5f37a`. It appears only in N §5,
    though IA states it as the basis for every PR.
  - IA applies the lenient test to #1274, #1275 and #1276, but the strict "needed by" test to #1271
    (IA:315–316: "Not needed").
  - N:109–111 says a stricter reading would hold back "every PR except the EOI package and, once their
    dependents land, the records those dependents cite". Both parts are wrong:
    - IA:377–378 shows that no `main` record has an item 8 gap without the EOI package (ARP-1-MARC
      `preregistration.md`:124 classes it as provenance).
    - Under the strict reading the dependents do not land either.
- **Fix.**
  - Add to IA §6: "**Basis.** Each landing follows the #1265 precedent (#1265 c.6846206075;
    `oa-1-20261112/STATUS.md`, 'Landing'): a record lands as the evidence for the scoped claim it
    states, at the strength stated. Whether model-reviewed paper results meet §A.46 item 1 so that
    item 2's first condition applies is an owner question (OQ-10)." Add OQ-10.
  - Replace IA:315–316 with: "Under the #1265 basis it would qualify. It stays on its branch because
    its verdicts use the #1230/#1232 drafts off `main` (item 8), and option (c) chose the extract
    (#1169 c.6854728636)."
  - Replace N:109–111 from "would hold back" with: "would hold back all nine PRs: no record on `main`
    has an item 8 gap that any of them closes (ARP-1-MARC classes the EOI package as provenance,
    `preregistration.md`:124)."

### F7 (Low). The #1274 `STATUS.md` proposal says "establishes" and omits §A.46 item 4's elements

- **Where:** IA:411–415, :424–425.
- **Evidence.**
  - The heading "What the record establishes" conflicts with IA:5–6 and with review gate 1.
  - §A.46 item 4 requires, for a claim on `main` whose verification is incomplete, "a stated status,
    an accountable Issue and a remediation plan". It also requires the record to distinguish
    verified, partially verified, exploratory and known-invalid results.
  - The proposal names #1169 but gives no remediation entry per gap.
- **Fix.**
  - Rename the heading to "**What the record supports, and at what strength**".
  - Add: "Verification status (§A.46 item 4): [A] paper arguments, hand-checked and model-reviewed,
    not independently verified; [L] imported; [K] statements on `main` read, not rebuilt."
  - Add a remediation line per gap: "A1: the separate T5(a), (b), (d) assessment (#1274 c.6863419164;
    OQ-9). D2, D3, E2: closure by #1232 L2/L3 and #1231 Theorem N, under #868/#1169."

### F8 (Low). The "superseded lines" list includes lines that are true

- **Where:** IA:255–258, :419–421.
- **Evidence.**
  - `PROVENANCE.md`:100 describes how the package was produced: "Nothing was committed, pushed or
    posted in producing the package; its landing, the fresh exact-head review and any merge are
    separate steps …". It is still accurate.
  - Rows A1, C, D1, E1 and I say "open, draft". #1221, #1230, #1232, #1231 and #1271 are all open
    drafts today.
  - Only row H is stale. It is time-indexed ("at this writing"), and the head has since moved again,
    to `3a3aa146`.
  - Listing true lines as superseded adds text with no verified defect (§A.28), and the list will need
    re-measurement at landing.
- **Fix.** Reduce the bullet to: "**Drafting-time state:** `DEPENDENCIES.md` row H names the REC-1
  head at writing (`cd38655c`). The head at landing is <measured then>; `REC-1-r7.md` is still blob
  `f1ffac0e`." Delete `PROVENANCE.md`:100 and "rows A1, C, D1, E1, I".

### F9 (Low). The reason given for skipping the DEPENDENCIES:18 nit is wrong; the conclusion stands

- **Where:** IA:259–261, :504–505, :563; N:119.
- **Evidence.**
  - #1276 pins `DEPENDENCIES.md` as blob `6c127b0a` "at `d015131d`" (`SYNTHESIS-r3.md`:40, :730), and
    classifies it as **provenance** (:730).
  - A merge-commit landing keeps `d015131d`, and with it the blob, reachable. A later edit would
    therefore not break the pin.
  - The nit does not touch `NEW-RESULTS.md`, which #1276 uses as support.
  - The good reasons to skip the nit are different: CONFIRM-r2 calls it optional and "consistent with"
    the `NEW-RESULTS.md` labels, and applying it would change a reviewed file without a defect (§A.25,
    minimum necessary changes).
- **Fix.**
  - At IA:259–261, replace with: "**Do not apply the optional nit** (DEPENDENCIES.md:18). CONFIRM-r2
    marks it optional and consistent with `NEW-RESULTS.md`:144–153; it corrects no defect, and it
    would change a reviewed file. Put any wording note in the status file."
  - At IA:504–505, restrict the "unchanged on `main`" check to blobs used as support. `6c127b0a` is
    provenance in #1276.
  - At N:119, replace "to keep #1276's blob pins valid" with "it corrects no defect".

### F10 (Low). IA §4's preamble contradicts step 3

- **Where:** IA:393 against :443–453.
- **Evidence.** IA:393 reads "Every step: add-only files; no change to any reviewed text". Step 3.1
  and 3.2, however, substitute words in `ASSESS-868.md`, `REVIEW-868-r3.md` and
  `REVIEW-PHASE1-r4.md`.
- **Fix.** Replace with "Every step: add-only files and no change to reviewed text, except the
  recorded SC-42 substitutions of step 3 (OQ-4), each recorded with its source and committed digests".

### F11 (Low). The list of #1274's own-branch commits is incomplete

- **Where:** IA:142, :416–417.
- **Evidence.** The review files name `bac44eeb` (`REVIEW-r1.md`), `1ef60d92`, `3f56d543`
  (`CONFIRM-r2.md`, `RESPONSE-r1.md`) and `4b40dcdc` (`CONFIRM-r2.md`). Only two of these are listed.
- **Fix.** At both places, write "own branch commits `bac44eeb`, `1ef60d92`, `3f56d543`, `4b40dcdc`".

### F12 (Low). The GR:426 corpus grep missed the book mirror

- **Where:** IA:539–542.
- **Evidence.** `book/ch19-open-problems.md`:116 and `book/The-Incompleteness-of-Observation-FULL.md`:5263
  state that ρ_s = ρ_crit follows "by the Clausius relation and the shell theorem". `papers/GR.tex`:3030
  is GR's derived artifact.
- **Fix.** Replace "no book mirror of the GR:426 sentence was found" with "the same attribution
  appears at `book/ch19-open-problems.md`:116 and its FULL mirror (:5263); `papers/GR.tex`:3030 is the
  derived artifact."

### F13 (Low). N treats a skipped step as evidence

- **Where:** N:74–77; IA:359–360.
- **Evidence.** At `e81e4fb2` the Mathlib bridge job shows step 3 "Install elan" failure and step 6
  "Release gate" **skipped**. "Did not fail" therefore supports no conclusion about content (§A.44).
  I ran `v3_verifier.py --receipts` at `e81e4fb2`: "54 receipt(s), all hold". The Mathlib bridge job
  succeeded at `46a548fb`.
- **Fix.** Replace "an installation failure, not a content failure, since the release-gate step did
  not fail" with "an installation failure: the Release gate step was skipped, not run. The job
  succeeded at the later head `46a548fb`."

### F14 (Low). #1273's rows are misattributed, and its wait on #1269 has an avoidable form

- **Where:** IA:46, :179–180, :494.
- **Evidence.**
  - `BELL-LADDER-r3.md` §6 classifies the SB reference as a gap "for L3 and N4" only. IA:179 lists
    "routes A/B/C, N3" as gap rows without marking that as the assessor's reading.
  - The QH stage-7 illustration is a gap "on which no verdict rests".
- **Fix.**
  - At IA:179, write "SB N4 [gap, #1273]; routes A/B/C, N3 [assessor: cited, not classified by
    #1273]".
  - At IA:494 and IA:46, add: "or narrow the stage-7 illustration to a conditional remark, which
    removes the wait on #1269".

### F15 (Low). The #1269 reference table omits one off-`main` commit

- **Where:** IA:195–204.
- **Evidence.** `ASSESS-868.md`:139 cites `0e0b3ddc` (#868 planning note, on
  `plan/joint-tests-source-20261013`, off `main`) and classifies it as provenance. Neither OBJECTS.md
  nor IA §2.2 lists it.
- **Fix.** Add the row "`0e0b3ddc` (#868 planning note) | Issue question text | provenance (as
  ASSESS:139-140 classes it)", and carry it into step 3's `STATUS.md`.

### F16 (Low). #1276's landing basis mixes a scientific claim with a ranking

- **Where:** IA:344–345, :508–509.
- **Evidence.**
  - SQ8 keeps §1's metric as a "**descriptive** ranking … not a board-priority change".
  - ChatGPT 5896999231 calls the three metrics "different counting conventions, not three theorems".
  - Priorities live in Issues (§A.45 rule 1).
- **Fix.** At IA:344–345, write: "It is the evidence for its per-entry classifications (MM-1 to MM-9,
  T1–T7) once its inputs are on `main`. The §1 ranking lands only as the descriptive convention SQ8
  fixes, or stays on the branch (owner question)." Add the question to §7.

### F17 (Low). NOTES misstates how an unclosed gap can land

- **Where:** N:113–115.
- **Evidence.** §A.42 item 8: a gap that cannot be closed lands "only by a recorded owner decision",
  and the claim is then not established (§A.46 item 1). "Accepted" does not say this.
- **Fix.** Replace "the gap would then have to be accepted or closed" with "the gap would then be
  closed by landing #1230/#1232, or landed under a recorded owner exception (§A.42 item 8), which
  leaves those verdicts not established (§A.46 item 1)".

### F18 (Low). The assessment does not state its own disposition

- **Where:** IA:3–7; on #1270, IA:368–387.
- **Evidence.**
  - The record is planning output (§A.45 rule 1). PR #1279 is titled "not for merge", but the file
    says nothing about its own landing.
  - #1270's body opens "**Preservation only. Not for merge.**" IA §3 does not quote it, though steps 3
    and OQ-8 propose landing parts of it.
- **Fix.**
  - At IA:7, add: "This record is not proposed for landing; its proposals go to #1169 and to each PR."
  - At IA:370, add: "PR body: 'Preservation only. Not for merge.' Landing any part changes that
    standing and needs the owner decision of OQ-7 or OQ-8."

***

## Not findings (checked and confirmed)

- **Merge mode.** Merge-commit-only landing is needed by every PR (IA:56–58, :528).
- **#1270 `eoi-package/` placement.** It cannot go into the G13-frozen ARP-1-MARC directory (IA:382–384).
- **#1274 gaps.** A1, D2, D3 and E2 are carried as named conditions; "No reference other than those of
  gaps 1–2 is a gap" (`DEPENDENCIES.md`:75).
- **#1273 safeguards.**
  - MI* is read only conditionally at r3:79–81 ("Theorem N′ if (xiv) is read as MI\*").
  - AL4's fixed regions are at r3:198–200: "independent of the state and the settings", "every record
    the wing holds or can obtain".
- **Ledger item (vii).** It is a posit at Main:724, so no manuscript change follows from #1273 Q1.
- **Correctness bands.** Unchanged (IA:556), which is right for consistency-axis landings.
