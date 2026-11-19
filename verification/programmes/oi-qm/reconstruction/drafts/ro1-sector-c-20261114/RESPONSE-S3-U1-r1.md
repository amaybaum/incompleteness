# Response to the review of S3-U1-r1

**Review.** `REVIEW-S3-U1-r1.md` (blob `cc1a8bdcca7e1dc59a27e3d83024d9900892757e`), on PR #1294 at
`db710b7a`; separate non-author Claude reviewer; verdict REVISE. The reviewed object is
`S3-U1-r1.md` at `e7f4db9d` (blob `163193c980c830e46cf657d4c1d7073077d535f2`); the review's `U1:N`
are r1's lines.

**Revision.** `S3-U1-r2.md`. r1 is left unchanged. Each finding below was checked at its source
before it was applied. Status: unreviewed; paper-only, under #1169 c.6890079967. No new premise is
adopted; the S7 and O11 stops, S5's separation, H-RR's status as a hypothesis, AC-1 and SNR-1 are
unchanged.

## Blocking

**B1. The PR-gate finding. Accepted; r2 §§4.3, 5.1(iv), 5.2, 7 (AW-3), 8.**
- *Checked.* At SEL-EXCL-1 `0ecfddeb` l. 33 the gate is `T(x,y,r,A,B)=(x,y,r,A⊕r,B⊕r⊕(x∧y))`. The
  reviewer is right on both points. r1's flag (r1:274–278) covers `x∧y`, and §5.1(iv) omitted it.
  The non-setting-carrier clause (r1:269–270) has no source; S-C1(a) quantifies over "every value of
  every other region" (MR★:501–503). With `y` as carrier, `x` selects whether `y` reaches `B`.
- *Carrier clause.* Dropped. r2's C-INT quantifies over any region other than the selecting
  setting, following S-C1(a).
- *Q1* (also R4). Applied as the plan requires: the I-sel label is withheld when a common refinement
  is available under AD-1 and the same preparation. [A-inf] For `T` with `y` as carrier, Bob's held
  record of `y`, which C-SET and SEL-EXCL-1 l. 44 both require, is such a refinement, so the label is
  withheld. This rests on the owner's working definition, which the owner states is "not a proof".
- *Flag.* Now stated for `T`: averaged over `y`, `r` is legible in `B` for `x = 0` and masked for
  `x = 1`. Under Q1 a flag awards no label. A refinement for the flag case exists only through a
  cross-wing joint comparison, and r2 does not rely on it.
- *Alternatives.* A three-row table in §5.1(iv) gives the class under each definition:
  - r1's carrier restriction: I-off with the flag;
  - any non-selecting carrier, without Q1: I-sel;
  - any non-selecting carrier, with Q1 (frozen): I-off.

  It also says whether a restriction on I-sel reaches `T` under each. Under the second row, whether
  the restriction also reaches the adopted Bell branch (Main:412), and so fails AC-1, is not decided.
- *AW-3.* Restated as a property of `T` under the frozen definitions. It is reclassified from NEW to
  BORDERLINE, because its constraint holds only relative to the definition, and that definition rests
  on Q1. It stays author-side and off `main` (§8).

**B2. S-A7 readmits R-seq. Accepted; r2 §2.1, G4, AD-1(e), C-PREP, C-SET, C-REC, C-RET, C-COMP,
§§5.3, 7 (AW-4).**
- *Checked.* The leak is real: r1's execution clause (r1:91–93) together with S-A7 (r1:448–449)
  yields R-seq's joint law.
- *Fix.* A program declares one comparison tick `t_c`. Every record entering its complete record or
  any joint comparison is held at `t_c`. Earlier records enter only if retained to `t_c` (C-RET) or
  carried there (S-A6); otherwise the joint law is a representation (K-4).
- *Where applied.* Outcome records, setting records (K-rec), herald and failure marks, adaptivity
  (the record is held at the tick of the write), SEL-EXCL-1's `H_A^(i)` (l. 91, cited), and same-seed
  reuse. AW-4 now names multi-tick schedules compared jointly.

## Required

**R1. "Not available" vocabulary. Accepted; r2 §2.3, §5.1(iii), §5.3.**
- Four outcomes replace r1's single "not available": available (derived, or relative to `μ`);
  unsourced; requires assumed apparatus; not available (disproved at scope and status).
- Only the last counts as a negative under SNR-1, and only conditionally if the disproof is [NP]
  (PLAN:791–794).
- §5.3's "removes" now lists all three non-available outcomes. The table of first missing steps now
  writes "not available on R-lin, at that scope".

**R2. C-RET is weaker than R2. Accepted; r2 §§4.4, 4.5, 7 (AW-6), 9.**
- "R2 holds by C-RET" is replaced by "MR-1's R2 is replaced by C-RET". The divergence is stated where
  it is made, with its source (Main:74; PLAN:293).
- MR-1 positives stated with R2 carry over to C-RET; R2-type negatives do not without a check.
  S-C4a's is named, and so is Theorem N's family.
- The parked-record clause is now stated to define what would count for U4's named hypothesis
  (decision A) and to assume no mechanism.
- The choice between C-RET and R2 is added as owner question (3).
- I kept the readback form rather than strengthening to R2, because it has a source and AD-1(f)
  already bounds the budget. The choice is listed as U1's own [P] in §5.2.

**R3. §4.4(iv) and Q-b1. Accepted; r2 §4.4.**
- §4.4(iv) now reads "not excluded under μ-G, since D2 is an equal-time statement; undecided on K1
  (C-3, C-4); not sourced".
- Q-b1 is labelled [NP]. I checked that the `observer-interface-obsmu-20261104/` directory holds only
  `ANALYSIS.md` and `README.md`.
- The citation now runs to :917, to include "all open".

**R4. Q1 not applied. Accepted; r2 §4.3, §5.1(iv), §8.**
- The working definition is quoted in full from #866 c.6719811801, which quotes #1007 c.6719788955.
- It enters C-INT as the Q1 test, which withholds I-sel when an available common refinement exists
  under AD-1 and the same preparation.
- Its second sentence, "Do not award the label merely with a qualification flag", governs the flag.
- Consequence recorded: a setting acting on another, held setting never earns I-sel. In §8 it is
  classed as an owner working definition, not a result.

**R5. AC-1 halves and "bare model". Accepted; r2 §2.1, §4.3, §5.3, §6.1.**
- *Bare model.* Defined: no extension E, `Obs` read-only, and no stated intervention principle
  (neither P-phase nor P-mix). Interface B is bare; Interface A is not (DEPS:178, :275–283).
- *D-iv.* Moved out of the bare-model losses. It is now context for an extension typed into `φ` or
  `Γ`. D-nonneg stays as the bare-model statement.
- *P-phase.* Placed consistently: absent from a bare model; for an extension, governed by its typing.
- *The two halves.* §5.3 reports AC-1 in two halves:
  - a per-clause table covering G4 with joint-hold, AD-1(c), AD-1(e), C-RET and C-INT with Q1;
  - the coverage half for bare models, stated as "criterion-neutral, coverage absent by model; not
    positive coverage";
  - the soundness half, which gives no result, for the stated reason: no restriction aimed at
    soundness is proposed, and K-1 (i)–(ii) show PR and the quantum references are treated alike.

  §9 matches.

**R6. C-SET "named producer". Accepted; r2 §4.2.** Now reads "a named source", with verdict
*derived* under the derived `μ` and *assumed* under a declared datum.

**R7. K-2 overstates sourcing. Accepted; r2 §5.2, AD-1(e).**
- §5.2 now separates the clauses taken from sources from a table of nine U1 [P] choices, each with
  its ground and with "Refers to an outcome? No". The choices are:
  - G3's μ-relative availability;
  - the joint-hold clause;
  - carrying both slice forms;
  - AD-1(e);
  - I-sel and its carrier quantifier;
  - the flag;
  - C-RET's readback form;
  - the parked-record clause;
  - the two resource kinds.
- AD-1(e) is re-grounded on G1. OA-1 D7 is now quoted with its antecedent, "If the setting does not
  change `φ`'s action" (OA1:204–205), as a consistency check only.

## Also requested

- **Narrowing S7(a).** Checked and applied (O10). The `φ` typing gets the criterion unchanged (P-L3's
  conflict is a model question, DEPS X3). The `Γ` typing gets "requires assumed apparatus" under
  either reading of S7(b). Only the `Obs` typing contradicts AD-1(c). The stop is narrowed to that
  typing, and which typing applies stays S7(a), unchosen (r2 §6.1).
- **S5 exposure.** Recorded at two sites:
  - R-fresh: `X_relevant` includes settings (REPORT.md:59–63), so S5 is named at later use
    boundaries (r2 §4.6);
  - SPEC:318's single-use row: a pointer for U2 to carry the independence as S5, not as an
    availability condition (r2 §4.2(v)).
- **Citation note.** Added to F-2: #1223 and #1225 were merged by `7fc6e0fc` and `bc7f817d`, both
  2026-11-13. Both were checked as ancestors of `main`.

## Optional findings

| # | Disposition | Reason |
|---|---|---|
| O1 | Applied (header) | Checked with `git diff --stat d8b74527 7086bd30`: `EVIDENCE.md` changed, and `support/`, `reviews/` and status/retention files were added. ASSESSMENT's scientific text is unchanged |
| O2 | Applied (§4.6(v)) | SEL-DISC-1 l. 79 is the entropy bound for fair outputs. The blank half is now cited to SEL-EXCL-1 l. 87, and l. 53 to comparable entropy accounting |
| O3 | Applied (§4.1, §9) | Gap 1 concerns selected hidden carriers. Visible carriers are native at the D3 cost (OA1:328, :358). The first missing step is scoped to hidden carriers and to heralds that later steps must hold |
| O4 | Applied (§4.6) | As above, under "S5 exposure" |
| O5 | Applied (G3) | Restated as refitting `μ` across programs, which makes a different model; G6 then applies |
| O6 | Applied (§6.2, §3) | Reading (ii) treated in one line (SPEC:205–208); G6's slice-form rule noted as presupposing reading (i) |
| O7 | Applied (§8) | #1234, #1032, #913, #914 and #1143 added as provenance |
| O8 | Applied (§4.2(v), §9) | Pointer for U2 on SPEC:318 |
| O9 | Applied (header, §3) | "Frozen here" becomes "frozen on acceptance of this unit" |
| O10 | Applied (§6.1) | As above, under "Narrowing S7(a)" |

**Answers-section note (8).** r1's last line, "No other decision is needed for U2–U4 to start", is
replaced. U2–U4 start in the order set by #1169 c.6890079967 and its review gates, and nothing in U1
authorizes them.

## Not changed

- The verdict, "criterion delivered with one named stop". The stop is the same S7(a), now narrowed.
- AD-1's two slice forms.
- F-1 and F-3.
- The seven first missing steps. Only their scope and wording changed (preparation and composition).

## Not checked in this revision

These are as in r1:
- the Lean statements, which were read through Main and DEPS only;
- the internal proofs of MR★, OA-1, Theorem N and REPORT.md.

Also not checked: whether Theorem N's criteria are at least as weak as C-RET's. r2 records this as a
check owed (§4.5).
