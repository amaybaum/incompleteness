# Status note: TUNE-1 Step 3A r3

**Draft for the TUNE-1 package (`LANDING-PLAN.md` §5).** At landing this note becomes
`verification/programmes/oi-qm/reconstruction/drafts/tune-1-20261111/TUNE-1-STEP3A-STATUS.md`. It
covers the five `TUNE-1-STEP3A*` files in that directory and no other file there; the TUNE-1 Step 1–2
records in the same directory are outside it. It changes none of the five files; r3 is the accepted
text.

Step 3A is a classification and specification record. It is not a quantum test, not a negative result
about any candidate class, and not progress toward a native mechanism. TUNE-1 is paused
scientifically (#1236 c.6873565446).

## Accepted record and reviews

- **Record.** `TUNE-1-STEP3A-r3.md` at `8228b3c24e17a17f324b6779b53b04ad296b4308` (PR #1267), blob
  `7bbec04d7bee91673c3241e78a289bba28fb1ea5`, SHA-256
  `8b44fe4f9ca2e31a1dfec5a8c485eb1547e8ccd4961c7f79cb614d886d89b385`, 1157 lines. "3A:n" is line n of
  that file. Commits: `b923fa7f` (r1, review, r2; parent `62bdc2cf`), `8228b3c2` (r3 and the extended
  review). `TUNE-1-STEP3A-OBJECTS.md` ties each reviewed working copy to its committed blob: the
  committed files differ from the reviewed copies only where the name of the session's working
  directory is replaced by `working`.
- **Review trail.** r1 (`TUNE-1-STEP3A.md`) and r2 (`TUNE-1-STEP3A-r2.md`) stay unchanged because the
  review and r3 cite their lines. All reviews are in `TUNE-1-STEP3A-REVIEW.md`:
  - review of r1, "Independent internal review (same model family)" (REVIEW:6): ACCEPT WITH CHANGES
    (R1–R7, m1–m4, optional R8), applied in r2 (3A §10);
  - recheck of r2: ACCEPT; nits N1–N2 applied;
  - review of r3 (§2A): ACCEPT WITH CHANGES (E1–E7, n1–n4), applied in r3 (3A §11);
  - confirmation of r3: ACCEPT;
  - ChatGPT review 5887947616 (posted under `amaybaum`, 2026-11-13T08:08:27Z) at `8228b3c2`: "ACCEPT
    WITH SCOPE QUALIFICATIONS". It states that "no exhibited candidate includes a fully specified
    family, preparation and concrete readout interface, so **none qualifies for Step 3B**. That is a
    specification gap, **not** a failure or no-go for all deterministic substrata."
- **Nature of the reviews.** All are model reviews; none is a human review, a GitHub approval or an
  owner decision, and none is verification (§A.46 item 7). The internal reviewer confirmed by search
  that no member of any class is exhibited (REVIEW:355–359).
- **Authority.**
  - Unit: #1236 c.6846408321 (`amaybaum`, 2026-11-13): "Authorize Step 3A"; c.6846442383
    (`amaybaum`, 2026-11-13T06:59:24Z): "Start; this session writes (Recommended)", with the guidance
    3A §0 quotes.
  - r3: #1236 c.6847314661 (`amaybaum`, 2026-11-13T07:51:30Z): "Add to Step 3A as r3 (Recommended)".
  - Standing after review: #1236 c.6847882040 (`amaybaum`, 2026-11-13): "Keep as draft (Recommended)",
    with "the header wording is left for a status note at any later landing stage".
  - Preservation plan: #1236 c.6873565446 (`amaybaum`, 2026-11-14T07:07:09Z).

## What the record supports, and at what strength

| § | Result | Strength in the record |
|---|---|---|
| 5 | Stop condition met: none of L5.4, L5.5, L5.6 (unbounded control region) and NL-A/NL-P has fully specified dynamics, preparation and readout; a specification gap, not a quantum failure; every class stays INCONCLUSIVE | [W] reading of Step 2 records [R]; confirmed by the reviewer's search |
| 5 | No candidate qualifies for Step 3B; the seven items a qualifying candidate must contain | [W] |
| 1, 3 | Each class primarily **underspecified**, secondarily **lacks a sourced apparatus** (read as "not shown derivable from the joint dynamics", §2A.6); H-write adds to the second group for B and the exchange rows of C and D | [W] on [R] and [P] |
| 3 | Conditional: specified initial-condition members of A and C, with (SP), have a simplex-embeddable prepare–measure fragment; without (SP), preparation-noncontextual, and whether that excludes T1 is open at [L] level; B and exchange rows outside OA-2 Theorem E(b); D classified by no result | [W] hypothesis match on OA-2 Theorem E(b) [R] |
| 3 | For R-lin, labels act only by translation under every law on the list | [R] (Lemma A-T; OA-2 E(a); OA-1 D5) |
| 7 | F-3A-1 (ELABORATING), F-3A-2 run repetition used but not stated (ELABORATING), F-3A-3 to F-3A-6 | [W] on [R], [P] |
| 4 | T1, the approximate single-qubit test with the L4 escape audit | restatement of Step 2's conditions [R] |
| 4 | T2, a classical-reduction test | a proposal for the owner; claims no result |
| 2A | Inclusion, access and control distinguished; reachable versus definable; Level A and Level B; preparation as a derivation question; embeddedness plus incomplete observation does not by itself select quantum mechanics; no classification changes | framing; [W] reading of [P] and [R] |

**Claim supported by this record:** "None of the classes TUNE-1 Step 2 left INCONCLUSIVE (L5.4, L5.5,
L5.6 with unbounded control regions, and NL-A/NL-P) has an exhibited member with fully specified
dynamics, preparation and readout, so none qualifies for Step 3B; this is a specification gap, not a
quantum failure, and every class stays INCONCLUSIVE; each class also relies on unsourced ingredients
(ready configuration and program blocks, run repetition, the law of the unread world, the growth of
the control region); for R-lin, a specified initial-condition member meeting OA-2 Theorem E(b)'s
hypotheses would have a simplex-embeddable prepare–measure fragment with (SP) and a
preparation-noncontextual one without it (paper derivations and readings on research records not
independently established, model-reviewed by an internal same-family reviewer and by ChatGPT, not
independently verified; not adopted; no manuscript claim affected)."

## Hypotheses

- **Named, unadopted:** H-μ (law of the unread world, independent of the observer), H-∞ (`𝓛_∞`
  rows), H-write (B; exchange rows of C and D), H-nl (D; adoption a Layer-0 revision) (3A:1008–1013).
- **Ledger posits used as premises:** items (ii), (iv), (vii), (xiii), (xiv) of Main:724.
- **Conditional groups of A and C:** OA-2 Theorem E(b)'s (H1), H-AR, (H3), (H4), (xiv) and (SP), with
  the match of TUNE-1's interface to them a [W] reading (3A:595–598); (SP) undecided for TUNE-1.
- **Used but not stated in TUNE-1's governing texts:** run repetition (F-3A-2); MP-0a-type ready
  supply and MP-0b-type complete history (3A:1014–1016).
- **Step 2 results** (Lemma A-T, FC-1, FC-2, Lemma I, NL-C, NL-C′, W-nl, Lemma F, exact U2(ii)): paper
  derivations reviewed under Step 2's gates, not kernel-checked (3A:1022).

## Limitations

- No member of any class is exhibited, so no class is tested; T1 and T2 are not applied (3A:780–781).
- The A and C conditional groups are a classification, not an exclusion (3A:955–957).
- No result classifies R-nl (D); that is an absence of results, not evidence for it (3A:771–774).
- OA-3's Lemma OBS and Theorem S do not apply to TUNE-1's candidates as stated (3A:572–574,
  :618–623).
- Whether a preparation-noncontextual model can meet T1 at small `ε` is open at [L] level.
- The claim "no member is exhibited" is scoped to the records read (3A:1054–1058).
- Kochen–Specker contextuality and Bell correlations are separate obligations; neither is settled by
  T1 or T2 (3A:882–892).

## Accountable Issue

#1236.

## Verification status and remediation (§A.46 item 4)

The owner's ruling, #1169 comment 6865680499 (`amaybaum`, 2026-11-13T21:44:54Z), states that "Model
acceptance is evidence of review, not independent mathematical verification", and that "A remediation
plan does not authorize new work. It may state that the obligation remains open." This plan
authorizes no work. Each gap below remains open until the evidence or decision named for it is
recorded on `main`.

Here "independently verified" means verified from `main` to the standard for its kind, for example
kernel-checked or independently verified mathematically (§A.46 item 1); "partially verified" means
reviewed by at least one separate AI-agent reviewer, or resting in part on kernel-checked statements,
without independent mathematical verification of the result; "exploratory" means a result not
reviewed by anyone but its writer, or a proposal that claims no result; "known-invalid" means refuted
on `main` by a counterexample or disproof.

- **Independently verified:** none of the record's own results.
- **Known-invalid:** none in r3. In r1, kept as the review trail, r1:546 states that C-POS-1 "passes
  T1 at `ε = 0` on its protocol class"; T1's pass is `PASS-DERIVED` with D1–D7, and C-POS-1 is a
  supplied construction (P:675), so the statement is false under T1's definition (REVIEW, R6(b)). r2
  and r3 replace it. Also in r1, superseded as overstatements rather than refuted: r1:425–428 on D's
  control (R7), the "(SP) as single pivot" statements (R2), and F-3A-2 classed NEW (R1). The r1
  statements are not results of the record.

| Result | Status | Current evidence | Missing verification | Resolving evidence or decision |
| --- | --- | --- | --- | --- |
| Stop condition and specification gap | partially verified | [W] reading; reviewer's search confirmation; ChatGPT review | An independent check of the record search | A human review of the Step 2 records' class definitions recorded on `main`, or an exhibited member (not authorized, c.6873565446) |
| Step 3B gate answer and the seven qualifying items | partially verified | [W]; internal and ChatGPT reviews | Independent review | As for the stop condition |
| Classification A–D, primary and secondary groups | partially verified | [W] on [R] Step 2 records and [P] | Independent verification; validation of the Step 2 premises used (§A.46 item 7) | A recorded validation of those premises on `main`, or the statements narrowed to carry them as named conditions |
| Conditional groups of A and C | partially verified; conditional on OA-2 Theorem E(b)'s hypotheses and on (SP), and on a [W] hypothesis match | [W] match on OA-2 Theorem E(b), itself partially verified (OA-2 `STATUS.md`) | Independent verification of the match and of Theorem E(b) | An independent mathematical verification of Theorem E(b) and of the match recorded on `main`; (SP) for TUNE-1 interfaces stays open under #1236 |
| F-3A-1 to F-3A-6 | partially verified | [W] on [R], [P]; internal review | Independent verification | As for the classification |
| T1 definition | partially verified | Restatement of Step 2's conditions, checked row by row by the internal reviewer | Independent check against the governing Step 2 texts | A human review recorded on `main` |
| T2 | exploratory | A proposal for the owner; claims no result | Not applicable | An owner decision whether T2 belongs to any later Step 3B; Step 3B is not authorized |
| §2A framing | partially verified | [W] reading of [P] and [R]; review of r3 and its confirmation; ChatGPT review | Independent review | A human review recorded on `main` |
| Statements resting on [R] records (TUNE-1 Steps 1–2; OA-1, OA-2, OA-3) | partially verified | Research records not independently established | Independent validation of each [R] premise used (§A.46 item 7) | A recorded validation of that premise on `main`, or the statement narrowed to carry it as a named condition |

Where a gap cannot be closed, the result is narrowed or withdrawn where it is stated (§A.46 item 5).

**The candidate-specification gap.** No member of any INCONCLUSIVE class is exhibited (3A:896–908).
This gap is distinct from the physical sourcing gap of the TUNE-1 sourcing unit (O-RDY, #1147), which
concerns the ready resource of one candidate and is recorded in that unit's status note. Neither gap
closes the other (`LANDING-PLAN.md` §4). A new candidate search is not authorized (#1236
c.6873565446); the gap remains open under #1236.

## Dependencies

At the package landing:

| Reference | Classification at landing |
| --- | --- |
| OA-1 r5, OA-2 r4, OA-3 r4, cited at `2d064a71` as off `main` (3A:29–33, each [R-off] tag) | Support on `main`. `2d064a71` is an ancestor of `main`. OA-1 r5 (`5a16b213`) and OA-3 r4 (`0a36fd05`) are the same blobs; OA-2 r4 is `8f8ddf73` on `main` and differs from `2d064a71` only on lines 65 and 958, neither cited here. Each OA statement used is a research record, partially verified (the OA `STATUS.md` notes), with its hypotheses. |
| OA-3 Theorem S (OA3:294–347) and N4.1 (OA3:394–416) | Support on `main`. Each range contains one line of delta-review text graded exploratory in the OA-3 status note (OA3:323, :415). 3A uses Theorem S as context and as a T2 control expectation, and N4.1's held-at-use branch; neither line carries a conclusion here. |
| TUNE-1 Steps 1–2 (P, AF, AF1, S3, S4, T1) at `080cd2be` | Support on `main`; byte-identical at `c3b5f37a`. [R] records with no status note on `main`. |
| W1-1 r4 at `2d064a71` | Provenance ("no bearing found", 3A:1047–1049). |
| Commits `080cd2be`, `62bdc2cf`, `59557ee8` | On `main`. |
| Commits `b923fa7f`, `8228b3c2` | On `main` once the package lands by merge commit. |
| `.r3-pre-review.md` (3A:8, :1125) | Provenance: not retained. The r3 confirmation's verdict rests on the committed r3 and its diff map; ChatGPT reviewed the committed blob. |
| Reviewed working copies in `TUNE-1-STEP3A-OBJECTS.md` | Provenance. Their full ids name no object in the repository; the package's §A.42 item 3 treatment is recorded under Landing. |
| Second guidance message, relay only (3A:139–150) | Provenance: not on #1236; no classification rests on it. |
| #1236 c.6816189419, c.6817129920, c.6828822665, c.6846408321, c.6846442383, c.6847314661, c.6847882040, c.6873565446 | Governance provenance, quoted. |
| Review 5887947616 | Review provenance. |
| #1283 at `f57e576a`; #1284 at `6e2d1ee8` | Provenance until adopted or landed (see Landing). |

## Source drift from `080cd2be` to `main` (`c3b5f37a`)

None on the cited paths. `papers/Main.md` (`0db17597`), `papers/SM.md` (`a5202371`) and the TUNE-1
Step 1–2 directory are byte-identical at `080cd2be`, `62bdc2cf` and `c3b5f37a`. The OA reports moved
onto `main` as stated under Dependencies. Re-measured when the package is assembled.

## Superseded lines in the accepted text

- Lines 3–4, "WIP / UNVERIFIED author report … review edits E1–E7 applied, awaiting confirmation": the
  confirmation of r3 is ACCEPT (`TUNE-1-STEP3A-REVIEW.md`, "Confirmation of r3"). ChatGPT review
  5887947616 names this header as a nonblocking documentary caveat.
- Lines 13–14, "nothing committed, pushed or posted. A ChatGPT review follows before the owner": the
  record is committed at `8228b3c2`, and the ChatGPT review is 5887947616.
- Lines 21–26 (pins): `main` at `c3b5f37a` has no change on the cited paths.
- Lines 29–33, "Off `main`", and lines 37–39: the OA-1, OA-2 and OA-3 reports are on `main` (see
  Dependencies). Every [R-off] tag on an OA citation (line 42's definition and its uses) reads as [R],
  partially verified.
- Line 956, "off-`main`, WIP result", and line 1002, "conditional on off-`main` work": OA-2 Theorem
  E(b) is a research record on `main`, partially verified, not established. The classification stays
  conditional as stated.
- Line 1041, "Read, off `main`": the branch commit `2d064a71` is an ancestor of `main`.
- The headers of r1 (lines 3–8) and r2 carry the writer-stage standing of those revisions; they are
  review trail.

## Landing

- **Together.** In one merge with the TUNE-1 sourcing unit, which cites this record (`LANDING-PLAN.md`
  §1).
- **Mode.** Merge commit of `8228b3c2`, so that `b923fa7f` and `8228b3c2` remain ancestors of `main`.
- **§A.42 item 3.** `TUNE-1-STEP3A-OBJECTS.md` names five reviewed working copies by full id, and none
  is in the repository. The planned treatment is an owner decision (`NOTES-PLAN.md` OQ-2); under
  option (a) the five ids are abbreviated to 8 characters, the reviewed SHA-256 values stay in full,
  and no line of r1, r2, r3 or the review changes.
- **Basis.** The proposed basis is §A.46 item 8 as drafted in #1283 at `f57e576a`, which is not
  adopted; the basis is open until #1283 is adopted. Record-specific check of the draft's conditions:
  - substantive, nonredundant result: met (the conditional classification with both (SP) halves,
    F-3A-2, T1 with the L4 audit, the Step 3B gate answer and §2A; the record's productivity verdict
    is "gem, BORDERLINE", 3A:999–1002);
  - scope and limits documented: met (3A §§5–8; this note);
  - independent non-author review and ChatGPT exact-head review: ChatGPT 5887947616 at `8228b3c2`;
    the internal review names itself "Independent internal review (same model family)", and whether
    that is the non-author review item 8 asks for is an owner question (`NOTES-PLAN.md` OQ-1); this
    note and the package head need the package's non-author and ChatGPT exact-head reviews;
  - landing checks and §A.42 item 8 tracing: tracing in `LANDING-PLAN.md` §6; item 3 decision and
    package checks pending;
  - accountable Issue, verification status, remediation plan: #1236, this note;
  - explicit rationale: #1236 c.6873565446, "This preserves accepted research without falsely
    treating preservation as progress toward a native mechanism"; the sourcing unit and REC-1 cite
    this record;
  - separate owner merge decision: not recorded;
  - historical authorization: #1236 c.6846408321, c.6846442383, c.6847314661.

  The record is preserved, not established (§A.46 item 1). Its removal is not automatic and is
  governed by §A.46 item 6.
- **Scientific standing.** TUNE-1 stays paused. Step 3B, a new candidate search and a `G_SM`
  computation are not authorized "until a physically justified O-RDY resource exists and the relevant
  candidate class is adequately specified" (#1236 c.6873565446). Preserving this record is not progress
  toward a native mechanism.
