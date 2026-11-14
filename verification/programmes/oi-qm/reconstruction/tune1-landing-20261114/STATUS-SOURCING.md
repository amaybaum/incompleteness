# Status note: TUNE-1 sourcing unit r2

**Draft for the TUNE-1 package (`LANDING-PLAN.md` §5).** At landing this note becomes
`verification/programmes/oi-qm/reconstruction/drafts/tune-1-sourcing-20261113/STATUS.md`. It gives the
standing of the records in that directory and changes none of them; r2 is the accepted text.

The unit is a bounded sourcing assessment of one candidate. Its stop is not an OI-wide no-go, not a
minimum-cost proof and not a native mechanism. TUNE-1 is paused scientifically (#1236 c.6873565446).

## Accepted record and reviews

- **Record.** `TUNE-1-SOURCING-r2.md` at `c539a60c5081540be033e07aa4f141caa1d0014b` (PR #1272), blob
  `35c5c116c017ed03a2eacfbeccfed457bae4649b`, SHA-256
  `c0e53684daedfa32e62bf6af26f8b778916c230baa4ac5d76a09e77ded9cb758`, 442 lines. "SRC:n" is line n of
  that file. Commits: `890fe3dd` (r1, review, r2; parent `c3b5f37a`), `c539a60c` (the confirmation and
  its cosmetic nit). `OBJECTS.md` lists the reviewed SHA-256 of six files; for r2 and `RESPONSE-r1.md`
  those values are of the bytes at `890fe3dd`, before the nit, as `OBJECTS.md` states.
- **Review trail.** r1 (`TUNE-1-SOURCING-r1.md`) and the notes stay unchanged because the review and
  the confirmation cite their lines.
  - `REVIEW-r1.md`: "Fresh non-author reviewer (not the writer of this unit, Step 3A, or REC-1)",
    ACCEPT WITH CHANGES (R1–R6, m1–m10); dispositions in `RESPONSE-r1.md`, all applied in r2.
  - `CONFIRM-r2.md`: focused confirmation of r2 at `890fe3dd`, CONFIRMED, one cosmetic nit, applied at
    `c539a60c` (SRC:3–6; `RESPONSE-r1.md`:3–4).
  - ChatGPT review 5892912253 (posted under `amaybaum`, 2026-11-13T14:39:29Z) at `c539a60c`: "ACCEPT
    (bounded paper-only sourcing result)". It states: "This is a sourcing stop, not an OI-wide
    no-go", and that the resource bound is "**necessary inside TUNE-1's initial-condition apparatus
    schema**, not universal resource lower bounds or a sufficient apparatus construction."
- **Nature of the reviews.** All are model reviews; none is a human review, a GitHub approval or an
  owner decision, and none is verification (§A.46 item 7). The non-author reviewer checked every
  pinned blob and line citation (REVIEW-r1 §0) and the resource arithmetic (REVIEW-r1 §2).
- **Authority.**
  - Unit: #1169 c.6854241002 (`amaybaum`, 2026-11-13T13:24:47Z), item 1, quoted at SRC:27–37.
  - Safeguard: #1169 c.6854774010 (`amaybaum`, 2026-11-13T13:47:03Z), quoted at SRC:45–50.
  - Preservation plan: #1236 c.6873565446 (`amaybaum`, 2026-11-14T07:07:09Z).

## What the record supports, and at what strength

| § | Result | Strength in the record |
|---|---|---|
| 1, N0 | Candidate TC-A: R-lin on finite tori, initial-condition mode, `D_0`-form initial law, heralded witnesses, unbounded control region; every other surviving class adds an unadopted hypothesis first | [W] selection on [R] and [P] |
| N1 | No hypothesis of NL-C fails for any interface of TC-A; the bound applies and is reported (NL-C′); the FAIL-CLASS family condition is not met because `|C_n|` grows; this is not an escape | [W] on [R] (S4) |
| 2, N3, 5 | **Stop at part (b), the ready resource:** no stated premise is shown to supply known-value cells for `r_{O,n}` and the program blocks, renewed per run; excluded under μ-G (Lemma P-1); not supplied unconditionally under μ-O, conditional route open; undecided under μ-R; covered only by the unadopted MP-0a, the open H-PREP and the open obligation O-RDY | [W] reading of [R] and [P]; N3.2 [W, here] |
| 2 | (a) premise-relative (ledger posits); (c) the form of the action derived (translation), its content blocked with (b), its adequacy L5.4; (d) the read rule imported; (e) the named convention MP-0b only; (f) the growth of the control region unsourced | [W] on [R], [P] |
| 4 | F-S1: NL-C's counting covers gates of `m` rounds with `m + 1 ≤ L`, giving `m|C| ≥ ½ log_q((1−4ε)/(4ε))`; gates of `L` or more rounds open | [W, here], reviewed |
| 4 | F-S2: within the initial-condition schema, at least `(K + 1) log_q((1−4ε)/(4ε))` known `q`-ary cells per run; under μ-G any event fixing every designated site has probability at most `(4ε/(1−4ε))^{K+1}`; with `D` known cells per run, `ε ≥ 1/(4(1 + q^{D/(K+1)}))`; necessity only | [W, here] arithmetic on NL-C′, reviewed |
| 4 | F-S3 (CONFIRMING), F-S4 (BORDERLINE), F-S5 (CONFIRMING; spatial copies give independent runs given a supply per copy) | [W] on [R]; [W, here] |

**Claim supported by this record:** "For candidate TC-A (R-lin on finite tori, initial-condition
mode, a designated-cell initial law, heralded witnesses, an unbounded control region), NL-C applies at
every interface and is not escaped, and the first part not shown to follow from OI's stated premises
is the ready resource: a native producer of known-value cells for the ready configuration and program
content, renewed each run, which is excluded under the global counting measure, not supplied
unconditionally under the orbit measure, undecided under the record-compatible measure, and named in
the corpus only as the unadopted MP-0a, the open H-PREP and the open obligation O-RDY; within TUNE-1's
initial-condition schema the needed supply is at least `(K + 1) log_q((1−4ε)/(4ε))` known `q`-ary cells
per run (paper readings and hand arithmetic on research records not independently established,
model-reviewed by a non-author reviewer and by ChatGPT, not independently verified; a bounded
sourcing stop, not an OI-wide no-go; not adopted; no manuscript claim affected)."

## Hypotheses

- **Ledger posits for part (a):** items (ii), (vii), (viii), (ix), (x), (xi), (xiii) of Main:724; the
  alphabet `q` fixed (imported convention); one world per precision on `𝓛_fin` (SRC:139).
- **Named, unadopted:** MP-0a (the `D_0`-form law, as a realization datum Main:58 admits; selecting it
  is a new premise), MP-0b (records held outside the observer), H-μ (independence of the unread world
  from the labels), H-PREP (open).
- **Measures:** each statement about (b) is relative to μ-G, μ-O or μ-R as stated (SRC:282–287).
- **Schema:** F-S1 and F-S2 hold within TUNE-1's schema with a finite alphabet; F-S1 within the proviso
  `m + 1 ≤ L`; F-S2 in initial-condition mode with blocks translates of `C` and `r_O` fixed on all of
  `O` (SRC:342–345).
- **Step 2 results** (NL-C, NL-C′, Lemma A-T, the class definitions): paper derivations reviewed under
  Step 2's gates, not kernel-checked.

## Limitations

- One candidate. Other candidates are set aside by N0 because each adds an unadopted hypothesis first;
  they are not assessed.
- Continuous-valued cells are out of TUNE-1's scope, not refuted (SRC:163–166, :356–357).
- The statement that no native producer exists on `main` for R-lin is scoped to the searches and the
  records read (SRC:403–407).
- Nothing after the stop is derived beyond F-S2's arithmetic (SRC:289–297).
- F-S2 is necessity only: that a ready supply yields the larger control region is not shown
  (SRC:341–342).
- Gates of `L` or more rounds are open (SRC:209).
- The member specification of TC-A (encoder, layout, `O_n`, `C_n`, `τ`) and L5.4 remain open and are
  not the stop (SRC:383–384).

## Accountable Issue

#1236 for the record. The physical sourcing gap is O-RDY, accountable under #1147; native apparatus
sourcing (#866) is the owner's stated first priority (#1236 c.6873565446).

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
- **Known-invalid:** none stated. r1, kept as the review trail, words several measure-relative or
  schema-relative negatives as unscoped (REVIEW-r1 R2–R4: for example "OI's stated premises do not
  supply known-value cells", and "Splitting a gate over rounds moves the growth from space to time");
  r2 narrows them. These r1 statements are overstatements, not refuted results, and they are not
  results of the record.

| Result | Status | Current evidence | Missing verification | Resolving evidence or decision |
| --- | --- | --- | --- | --- |
| TC-A selection (N0) | partially verified | [W] on [R], [P]; non-author review; ChatGPT review | Independent check of the selection against the Step 2 class definitions | A human review recorded on `main` |
| NL-C applies at every interface (N1) | partially verified; conditional on NL-C (Step 2 [W]) | [W] on S4; non-author review; ChatGPT review | Independent verification of NL-C and of its application | An independent mathematical verification recorded on `main` (for example a kernel formalization or a human review) |
| Stop at (b) under μ-G (N3.1) | partially verified; conditional on μ-G | Lemma P-1 and OA-1 D2–D3 [R]; reviews | Independent verification of Lemma P-1 and D2–D3 as premises (§A.46 item 7) | A recorded validation of those premises on `main` |
| (b) under μ-O (N3.2) | partially verified | [W, here]; reviews | Independent verification | As for N1 |
| (b) under μ-R (N3.3) | open; no verdict | — | Not applicable | Remains open under #1147 |
| Coverage only by MP-0a, H-PREP, O-RDY (N3.4–N3.5) | partially verified; scoped to the searches made | Source reading; reviews | An independent check of the searches | A human review of the cited sources recorded on `main` |
| F-S1 | partially verified; within `m + 1 ≤ L` | [W, here]; non-author review (R3), confirmation, ChatGPT | Independent verification | As for N1 |
| F-S2 | partially verified; necessity only, within the initial-condition schema | [W, here] hand arithmetic; checked by the non-author reviewer (REVIEW-r1 §2) and ChatGPT | Independent verification | As for N1 |
| F-S3 to F-S5 | partially verified | [W] on [R]; [W, here]; reviews | Independent verification; validation of the [R] premises | As for N1 and N3.1 |
| Statements resting on [R] records (TUNE-1 Steps 1–2; OA-1; OA-2; OBS; NPS1; NIS2) | partially verified | Research records not independently established | Independent validation of each [R] premise used (§A.46 item 7) | A recorded validation of that premise on `main`, or the statement narrowed to carry it as a named condition |

Where a gap cannot be closed, the result is narrowed or withdrawn where it is stated (§A.46 item 5).

**The physical sourcing gap (O-RDY).** The first missing physical ingredient is a native producer,
inside the joint dynamics, of known-value cells for the ready configuration and the program blocks,
renewed for every run (SRC:374–379). The stated premises are not shown to supply it, and the corpus
names it only as the unadopted MP-0a, the open H-PREP and the open obligation O-RDY.
- **Current evidence:** this record's stop, with OA-1 gap 1 (OA1:522), OBS:100, :121 and the first stops
  of NPS1 and NIS2 for the binary SM ring (F-S3). The owner accepted #1278's bounded source assessment
  (#1236 c.6873565446: "It found no physically supplied O-RDY mechanism. Physical source remains NOT
  PASSED."); ChatGPT review 5898054706 at `d8b74527`: "**Physical source NOT PASSED**. No new
  apparatus candidate, quantum operation, OI→QM equivalence, impossibility theorem, or native producer
  follows." That assessment concerns the binary SM ring branch, not R-lin, and reads this record only
  as off-`main` context; it leaves this gap open for TC-A.
- **Missing:** a physically justified ready resource.
- **Accountable Issue:** #1147 (`not authorized`), under the owner's priority #866.
- **Resolving evidence or decision:** a physically sourced producer recorded on `main`, or an owner
  decision adopting a premise under §A.29. Neither is authorized here.

This gap is distinct from Step 3A's candidate-specification gap (no member of any INCONCLUSIVE class
is exhibited), which this record leaves open as "not the stop" (SRC:383–384). Supplying O-RDY would not
specify a member, and a specified member inside the schema would inherit O-RDY at least at the F-S2
rate (`LANDING-PLAN.md` §4). L5.4 is a third open item, mathematical, and neither gap.

## Dependencies

The record's own table (SRC:419–442) classifies each reference against `main` at `c3b5f37a`. At the
package landing:

| Reference | Classification at landing |
| --- | --- |
| Step 3A r3 at `8228b3c2` (candidate A; statement (i); "no member is exhibited", 3A:896–905) | Support on `main`: lands in the same merge, blob `7bbec04d` unchanged. |
| 3A:493, :501, :505, :794–805, :436–439, :969–986 | Provenance, as the record classifies them; the content used is on `main`. |
| REC-1 r7 at `9f7d2612` (§0 safeguards; REC:215 C4; REC:222 C11; REC:223 C12) | Provenance, or support on `main` through OA1:111–114, :556–562, Main:42, :58, P:145 and Main:724, as the record states. |
| REC:217 (C6), "status undetermined" for MP-0b (part (e)) | Support off `main`, closed by narrowing: part (e)'s marking "named hypothesis MP-0b only" rests on OA1:563–564 on `main`; "status undetermined" is REC-1's classification and context, not a result of this record. |
| REC:220 (C9), μ-R presupposes the observer's records (N3.3) | Support off `main`, closed by narrowing: N3.3 reaches no verdict ("Undecided; no source"); the same concern is on `main` at NPS1:85; the REC quotation is context. |
| REC-1 P0 (SRC:297; `NOTES-r2.md` item 7) | Provenance. |
| OA-1 r5, OA-2 r4, OBS, NPS1, NIS2, P, AF, S3, S4, T1, Main, SUB, `LA-EQUAL-REVIEW.md` at `c3b5f37a` | Support on `main`. OA-1, OA-2, NPS1 and NIS2 are research records graded partially verified in their status notes; NPS1 and NIS2 concern the binary SM ring and are used as confirming context only (F-S3). |
| Commits `890fe3dd`, `c539a60c` | On `main` once the package lands by merge commit. |
| #1169 c.6848268369, c.6854241002, c.6854774010; #1236 c.6817129920, c.6828822665, c.6873565446; #866 c.6765161496; #1147 body; #914 c.6563412926 | Governance and planning provenance, quoted. |
| #1278 at `d8b74527`; review 5898054706 | Governance provenance for the statement that physical source is not passed. |
| Review 5892912253 | Review provenance. |
| #1283 at `f57e576a`; #1284 at `6e2d1ee8` | Provenance until adopted or landed (see Landing). |

REC-1 rows C4, C6, C9, C11 and C12 are byte-identical at REC-1 r9 (`3a3aa146`, lines 223, 225, 228,
230, 231). If REC-1 lands, the two narrowed rows may be re-pointed to it as a correction in place.

## Source drift from `c3b5f37a` to `main` (`c3b5f37a`)

None at this writing: the record's pin is the `main` commit against which this note is measured. It
is re-measured when the package is assembled (`LANDING-PLAN.md` §1, G2).

## Superseded lines in the accepted text

- Lines 8–12, "WIP / UNVERIFIED author record … Independent non-author review, then ChatGPT review
  at the exact head, are the next steps": the non-author review is `REVIEW-r1.md`, its confirmation
  `CONFIRM-r2.md`, and the ChatGPT exact-head review is 5892912253.
- Lines 78–85, Step 3A "Off `main`" and "Neither branch head is an ancestor of `c3b5f37a`": Step 3A
  lands in the same merge. REC-1 stays off `main`.
- Line 359, "Both are unreviewed [W, here]": F-S1 and F-S2 were reviewed by `REVIEW-r1.md` (R3, R4),
  confirmed in `CONFIRM-r2.md`, and covered by 5892912253. The tag [W, here] keeps its meaning of a
  derivation made in this file.
- Lines 441–442, "Before any landing, each row marked "support off `main`" is closed by landing its
  source or narrowed": the Step 3A rows close by landing; the REC-1 rows close by narrowing, as stated
  under Dependencies.
- `NOTES-r1.md` and `NOTES-r2.md` call themselves working notes, "not a record"; they land as review
  trail because the review and the confirmation cite them.

## Landing

- **Together.** In one merge with Step 3A, after it (`LANDING-PLAN.md` §1).
- **Mode.** Merge commit of `c539a60c`, so that `890fe3dd` and `c539a60c` remain ancestors of `main`.
- **Basis.** The proposed basis is §A.46 item 8 as drafted in #1283 at `f57e576a`, which is not
  adopted; the basis is open until #1283 is adopted. Record-specific check of the draft's conditions:
  - substantive, nonredundant result: met (the TC-A stop, F-S1 and F-S2; productivity "gem
    (ELABORATING)", SRC:355–360);
  - scope and limits documented: met (SRC §§4–5; this note);
  - independent non-author review and ChatGPT exact-head review: met for the record (`REVIEW-r1.md`,
    `CONFIRM-r2.md` at `890fe3dd`; ChatGPT 5892912253 at `c539a60c`, which covers the cosmetic delta);
    this note and the package head need the package's non-author and ChatGPT exact-head reviews;
  - landing checks and §A.42 item 8 tracing: tracing in `LANDING-PLAN.md` §6, with the two REC-1 rows
    narrowed above; package checks pending;
  - accountable Issue, verification status, remediation plan: #1236 (O-RDY under #1147), this note;
  - explicit rationale: #1236 c.6873565446, "This preserves accepted research without falsely
    treating preservation as progress toward a native mechanism"; #1278 cites this record;
  - separate owner merge decision: not recorded;
  - historical authorization: #1169 c.6854241002, item 1.

  The record is preserved, not established (§A.46 item 1). Its removal is not automatic and is
  governed by §A.46 item 6.
- **Scientific standing.** TUNE-1 stays paused. Step 3B, a new candidate search and a `G_SM`
  computation are not authorized "until a physically justified O-RDY resource exists and the relevant
  candidate class is adequately specified" (#1236 c.6873565446). Preserving this record is not progress
  toward a native mechanism.
