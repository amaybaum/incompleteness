# #1062 OBS-EMERGE report r4: change map

- **Base.** `REPORT-r3.md` at commit `f89d6861f2dabe095e2d5a6836d7fd6a32188b28`. `REPORT-r4.md` is r3 with exactly the changes below, and `REPORT-r3.md` stays unchanged beside it. `REPORT.md` (r1) and `REPORT-r2.md` each receive one prepended superseded notice and are otherwise unchanged.
- **Owner decision.** #1169 comment 7167657546 (amaybaum, 2026-11-25T16:10:25Z), quoted: "#1062 | Replace the collective provenance classification with a per-reference trace." "Both | Add the preservation rationale and remediation plan required by §A.46 item 8." "Keep r1 and r2 with explicit superseded notices. Each notice should identify the authoritative revision and its corresponding correction record. Preserving the research history is valuable, provided obsolete conclusions cannot be mistaken for current results." "Obtain bounded independent reviews and fresh CI at the corrected heads."
- **Trigger.** r3's Pin line labelled the #1558 branch reports "cited as provenance only (§A.42 item 8)" as a group, which item 8 forbids ("'Provenance only' is a finding about each reference, never a label applied to a group of them"). The r1 review raised the same point as a nit (PR #1562 comment 7166647951, "§A.42 item 8"), and r2 did not apply it because it lay outside that revision's scope.
- **Result.** No result, conclusion, support class or table row of r3 is changed. The trace finds no reference that is support off `main`.

## Applied

### 1. Group label replaced (Status, Pin line)

- Old: "They are cited as provenance only (§A.42 item 8)."
- New: "Each off-main reference in this report is classified, by the claim it is attached to, in §8 (§A.42 item 8)."

### 2. `InternalObserver.lean` cited directly on `main` (Status, Sources, kernel modules)

- Old: "`InternalObserver.lean` (via the #1558 report)"
- New: "`InternalObserver.lean` (`verification/lean-mathlib/OIBridge/InternalObserver.lean`, on `main` at the pin)"

The module is present at the pin. No conclusion of the report uses it (§8, T8).

### 3. New §8, "Off-main references (§A.42 item 8)"

Rows T1–T20 classify every off-main reference in the report:
- the #1558 branch and its head (T1);
- each #1558 report section read (T2–T7);
- the former indirect module citation (T8);
- #1062 (T9) and the #1169 owner decisions (T10);
- the three PR #1562 reviews (T11–T13);
- each use of the #914 matrix comments (T14–T19);
- #903 (T20).

All are provenance, apart from T8, which is now on `main`. For every claim to which an off-main reference is attached, the support was checked on `main` at the pin.

Two checks were made for this trace:
- T16: a search of `papers/`, `book/` and `verification/` at the pin for the self-measurement label. It found no development, and the only hits cite Breuer's 1995 bound. This puts the §1.3 claim on `main` instead of on the #914 matrix.
- T17: #914 does not itself record that O-REC is downstream of bare formation. It records that bare formation has no prerequisite and that a recording observer needs O-REC. The §2 Q4 claim rests on MR-1 §3.1–3.2 on `main`. The attribution "as #914 records" is listed in §9.5 and §9.6 and is not edited, because that lies outside this decision.

### 4. New §9, "Preservation and verification status (§A.46 items 4 and 8)"

- 9.1: the substantive, nonredundant result.
- 9.2: scope and evidence limits.
- 9.3: the independent reviews (PR #1562 comments 7166647951 and 7167101212; the delta review of r3, ACCEPT), with their limitation.
- 9.4: the accountable Issue (#1062).
- 9.5: verification status by claim class, and the statements known to be overstated or incorrect, taken from review findings outside the earlier bounded revisions (R6, R10, R11) and from T17.
- 9.6: a remediation plan for each open verification gap.
- 9.7: the preservation rationale.

9.5 records the review verdicts on G1–G5 and states how §6's "unreviewed" reads beside them. §6 itself is not edited.

### 5. Status line

One bullet is added after "Revision r3": "**Revision r4.** This revision replaces the collective provenance label for the off-main reports with a per-reference trace (§8), cites `InternalObserver.lean` directly on `main`, and adds the preservation and verification status (§9), under the owner decision quoted in #1169 comment 7167657546 (2026-11-25T16:10:25Z): "#1062 | Replace the collective provenance classification with a per-reference trace." and "Both | Add the preservation rationale and remediation plan required by §A.46 item 8." (amaybaum, 2026-11-25, coordinating session). The change map is `CHANGES-r4.md`. No result, conclusion or classification of r3 is changed. All other text is unchanged from r3."

### 6. Superseded notices on r1 and r2

One paragraph is prepended to `REPORT.md` and one to `REPORT-r2.md`. Each names `REPORT-r4.md` as the authoritative revision and `CHANGES-r4.md` as its correction record, and states that the file is superseded, kept as history and not current. The rest of each file is unchanged.

## Not changed

- The review findings R6–R11, nits 4–5 of the r2 delta review and the r1 review's other nits are not applied. They are listed in §9.5 and §9.6 because they fall outside this decision.
- The §2 Q4 wording "as #914 records" (T17) and §6's "unreviewed" are not edited. §9 states their status.
- `REPORT-r3.md` is unchanged.
