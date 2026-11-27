# r6 amendment 9: release of the rule-record rows, and the S11-2c contract (draft r1)

**Owner decision.** amaybaum, in the coordinating session, 2026-11-27, recorded at #1169 comment 7215050737
(2026-11-27T09:45:03Z). Quoted:

> Approved: the 75-row release change and the S11-2c minimum contract.
>
> Record both as a single narrowly scoped Amendment 9.

On the sequencing correction:

> * The 75 affected rows may report `NOT RUN` at tool landing.
>
> * Their reviewed-record requirements remain mandatory for retirement.
>
> * The sequencing must allow OBL-3 reviews to be produced before those requirements are enforced, without creating another circular dependency.
>
> * All other gate requirements remain unchanged and fail-closed.

On S11-2c:

> Adopt the proposed minimum contract. The combination of normal admission, an isolated mutation, a retained byte diff, and an unmutated control is sufficient to test the intended CK5 behavior.
>
> A record-tree integrity rejection is not qualifying evidence.

The same message:

> The sequencing correction must not become an opportunity to redesign the assurance framework. The objective is to finish the existing implementation.

**Status.** Draft r1, recording the approved text. It changes nothing else in r6 or its amendments 1 to 8.

On adoption, the expectation and design changes below are applied by a generator-amendment9, as for earlier
amendments. The tool revision implements them. Adoption authorizes no merge, dispatch, freeze or trial.

**Goal link (AGENTS.md sec. A.47).** A1 retirement (#1477). It decides at which step the rule-record rows gate, and
what counts as S11-2c's evidence.

## 1. Sequencing correction: the 75 rule-record rows

**Rows.** The 75 rows of the class "b: rule records unreviewed (OBL-3)" in the #1577 implementer's classification
(`classes.json`, sha256 `386ba90a9f08a842deca1ea125c3bb600f052046f3546dbcb53d439c66330056`). It was drawn from the gate
result at the tool commit `768825452f230415f7fcde1a718de429eea2cce4`. The rows are:

`A11r`, `A2r`, `A4r`, `A5r`, `A7r`, `A9r`, `G1`, `G2`, `G3`, `L1`, `L2`, `L3`, `L4`, `N-W`, `N3-config-route`, `RT-A`,
`RT-C`, `RT-D`, `RT-D-gr58`, `RT-DR`, `RT-E`, `RT-H0`, `RT-L`, `RT-O9`, `RT-T0`, `RT-X`, `S11-11`, `S11-14`, `S11-2a`,
`S11-3`, `S11-4`, `S11-56`, `S2r`, `V1`, `V10`, `V11`, `V12`, `V13`, `V14`, `V15`, `V16`, `V17`, `V18`, `V19`, `V2`,
`V20`, `V21`, `V22`, `V25`, `V26`, `V27`, `V27-glossary`, `V3`, `V4`, `V5`, `V6`, `V7a`, `V7b`, `V7c`, `V9`, `WB1`,
`WB10`, `WB12`, `WB13`, `WB14`, `WB15`, `WB2`, `WB3`, `WB4`, `WB5`, `WB6`, `WB7`, `WB8`, `WB9`, `item11-T1p`.

**Change.** Each of these rows gains an entry in EXPECTATIONS.json, and R6.GATE.15's list of rows that admit NOT RUN
gains the 75 rows. The entry is:

- `status_allowed`: `["PASS", "NOT RUN"]`;
- a `not_run` entry, in the form of RT-T's, with three parts:
  - reason: "needs the reviewed rule records of OBL-3, which do not yet exist";
  - release condition: "the reviewed rule records of OBL-3 present at F and verifying under the ownership chain and
    record lint of sec. 11 (R6.REC.1 to R6.REC.6)";
  - release check: "the configuration at the commit under check references reviewed rule records (OBL-3)".

Under R6.GATE.15, NOT RUN is admitted only while the release check is false.

Nothing else changes:
- every other expectation of these rows stays as it is, including both directions where a row has them;
- R6.GATE.9's composite rule (Q14) applies;
- a row paired with one of them keeps its own expectation;
- the gate stays fail-closed for every other row.

**Where the rows are enforced.** The rows gate plan freeze F, which is OBL-3's own gate (sec. 32: "Gates: plan freeze
`F`"). At the candidate F, the configuration references the reviewed rule records, so the release check is true. In the
control-suite run at the candidate F, which is part of OBL-16 (a)'s exact-candidate validation, each row must PASS:
NOT RUN is no longer admitted, and FAIL or ERROR fails the gate.

A gate verdict at the tool commit on `main` admits these rows as NOT RUN, and never discharges OBL-3. The same holds for
RT-T and OBL-15 (#1577 comment 7212650464).

**The owner's condition: no circularity.** OBL-3's reviews can be produced before these rows are enforced. Producing
and reviewing the rule records needs neither the tool landed under these rows nor F:

1. *Before:* the rows gated the tool's landing, through the gate of sec. 16. The reviewed rule records are derived at H:
   R6.REC.14 reads fingerprints "at `recorded_at`", and the staging r2 allow root is re-derived "from eligible pinned
   bytes". Under the adopted H-drift mitigation, H is chosen only after the tool lands (owner, #1169 comment 7214186738:
   "Choose H only after the tool lands"). The landing therefore waited on records that wait on the landing. That was
   the cycle.
2. *After:* the order is acyclic:
   - the tool lands, with these rows NOT RUN;
   - H is chosen;
   - the rule records are derived at H;
   - the rule records are reviewed;
   - the configuration at the candidate F references them;
   - the rows run and must PASS at the candidate F;
   - the owner designates F.
3. *Producing the records needs no landed tool.* R6.REC.14 and R6.RULE.4 define the lint over the record and its named
   files at `recorded_at`. The lint is run by the tool's code at any commit; it needs no landing, and it does not depend
   on any of the 75 rows. Staging r2 sec. 2 places the allow root at a preparation commit `B` and requires only "the
   current lint and reviews". In practice it is produced after the landing anyway, because H follows the landing.
4. *Reviewing the records needs no F.* A review of the records needs three things:
   - its fields under S-2 S2.3 (`reviewer`, `reviewed`, `revision`, `independence`);
   - for the first allow root, the widening review of staging r2 sec. 2 ("Initial widening review");
   - the null predecessor of prior-freeze continuity (staging r2 sec. 2).

   None of these needs F to exist. In chain record lint, a review's `revision` must be reachable from F (S-1 sec. 3,
   kept by S-2 S2.3), and a later F that descends from it satisfies this. OBL-3's own text states that the records are
   "independently reviewed and adopted with the amended plan at `F`": review comes first, and adoption happens at F.
5. *No row is needed by its own release.* The release check reads only the configuration and the records it references.
   It reads no result of these 75 rows, so no row waits on itself or on another of them.

## 2. S11-2c minimum contract

**Clauses.**
- Staging r2 sec. 1 ("Before accepting S11-2c, retain independent CK5 evidence bound to the exact mutant, its sole J/S1
  change, evaluated pin and approved op-A evidence contract.").
- Its sec. 4 row "Control metadata and S11-2c".
- The row S11-2c of EXPECTATIONS.json (`expect`: FAIL with `record_checks_failed_include` CK5; operation `record`).

**Contract.** S11-2c is evidence when all of the following hold:
1. An op-A `record` run under normal admission, on a synthetic fixture whose configuration pins a mutant record.
2. The mutant differs from the base only in the J/S1 change, as a retained byte diff shows.
3. The retained invocation and raw result show CK5 in `record_checks_failed`.
4. The same run on the unmutated record shows no CK5 failure.

A record-tree integrity stop does not count.

This contract is the "approved op-A evidence contract" that staging r2 sec. 1 requires. The row's expectation is
unchanged.

## 3. References (AGENTS.md sec. A.42 item 8)

| Reference | Used for | Classification |
|---|---|---|
| #1169 comment 7215050737 | the owner decision, quoted with author and time | owner record, quoted here |
| #1169 comment 7214186738 | the H-drift mitigation, quoted in sec. 1 | owner record, quoted here |
| DESIGN-r6.md (blob `e149009c`) and EXPECTATIONS.json (blob `2f1829da`) on `main`: sec. 32 OBL-3, OBL-15, OBL-16; R6.GATE.9, R6.GATE.15, R6.REC.1–.6, R6.REC.14, R6.RULE.4; the RT-T and S11-2c rows | the clauses changed and the non-circularity argument | support on `main` |
| `classes.json` (sha256 above) and the gate result at `76882545`, on the #1577 tool branch | the list of the 75 rows | provenance. The list is stated in full here, and the amendment rests on that statement, not on the file |
| staging r2 `AMENDMENT.md` (secs. 1, 2, 4) and S-2 `AMENDMENT-S-2.md` (S2.3), on the #1577 tool branch | the S11-2c clause; the allow root, the initial widening review, prior-freeze continuity and the review fields | support off `main` until they land with the tool (Amendment 8, M8-11); the tool's landing therefore precedes the use of this amendment |
| #1577 comment 7212650464 | that a gate verdict at T does not discharge RT-T's obligation | provenance |
