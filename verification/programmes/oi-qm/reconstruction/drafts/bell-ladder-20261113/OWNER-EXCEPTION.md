# Bell package: owner exception under §A.42 item 8, and status note for BS findings 1–3

This is a mutable record on `main`. It names the statements in the Bell package that land without
support on `main`, under a recorded owner exception to §A.42 item 2, and it records the limitations of
three Bell-scope passages. It covers the files of `drafts/bell-ladder-20261113/` and
`drafts/bell-scope-868-20261111/` and the `main` record that cites them. Those files are byte-identical
copies and are not edited; `SYNTHESIS-r3.md` is pinned by
`selection-discriminator-20261113/ARTIFACTS.sha256` and `RETENTION.json` and is not edited. This record
names the statements in them that the exception leaves unsupported (§A.42 item 8; §A.46 items 4 and 7).
It establishes no claim and changes no scientific status.

Abbreviations: "BL:n" is line n of `drafts/bell-ladder-20261113/BELL-LADDER-r3.md`; "BS:n" is line n of
`drafts/bell-scope-868-20261111/BELL-SCOPE-UNIT1.md`; "RV:n" is line n of
`drafts/bell-scope-868-20261111/REVIEW-BS-r2-NONAUTHOR.md`; "SR3:n" is line n of
`selection-discriminator-20261113/support/synthesis/SYNTHESIS-r3.md`. Paths are relative to
`verification/programmes/oi-qm/reconstruction/`.

## Owner decision

Owner `amaybaum`, 2026-11-20T05:57:03Z, #1169 comment 7031779559
(<https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7031779559>), "Owner decision:
#1441 merge, a #1440 exception, and UNIV-2", item 2, quoted in full:

> **2. #1440 (Bell package): a limited owner exception under §A.42 item 8.** The exception preserves the reviewed Bell evidence. It does not establish the unsupported claims.
> - **SB L3:** the directed-separation claim and its MM-9 dependency stay marked as support held off `main`, not independently established. Promoting that claim needs a separate reviewed landing.
> - **QH (BL:104, stage 7):** kept as non-load-bearing context. It does not need to land first.
> - **BS findings 1–3:** a superseding status note records the limitations. No silent correction or promotion of the historical results.
> - **Unlanded Bell probes:** provenance only, not independently reproduced support.
> - The exception is recorded **in a file on `main`**, landed by #1440. That file names this owner decision, the unsupported statements and their remaining obligations.
> - After those changes: a fresh independent exact-head review and green CI before merge.

The same comment closes: "A1 OPEN/UNADOPTED; physical measurement sourcing NOT PASSED; Bell/Tsirelson
open." The preservation itself was authorized at #1169 comment 7030839727 (`amaybaum`,
2026-11-20T04:56:12Z). Under §A.42 item 8 and §A.46 item 1, a claim that lands under this exception is
not established.

## Statements left unsupported

### E1. SB L3: the directed form of (Sep), and MM-9's dependency on it

- **Statements.**
  - BL:57–59, in the stage-3 hypothesis list: "(Sep) no directed `G_φ` path … (BS states (Sep) with the
    symmetrized distance, which is sufficient; the directed form is SB L3)".
  - BL:100, stage 3: "directed form SB L3 (SB:167–171) [D]".
  - BL:156, toy check 4: "`λ_A0` is a common cause (SB L3)".
  - BL:299, r3's own reference row, which classes SB L3 as "support off `main`: gap".
  - SR3:415–416, MM-9: "N2's necessity rests on SB's L3 (off `main`), carried conditionally", and
    SR3:732, the reference row for SB L3.
- **Why unsupported.** L3 is lemma L3 of SUBSTATE-BRIDGE-1 r2 (draft S:167–171, #1232 at `86a413c8`).
  Neither that file nor the narrow extract `SB-L3.md` (#1285, blob `82b5a6a2`) is on `main`. The extract
  rests on a status note whose blob at #1285's head (`7327726d`) has no review. The support is held off
  `main` and is not independently established. On `main`, `intervene-substate-results-20261113/NEW-RESULTS.md`:507
  and `DEPENDENCIES.md`:23 (row D2) carry N2's necessity conditional on L3.
- **What stands without it.** Theorem N and N′ (BS:159–196), which land here, are stated with BS's
  symmetrized (Sep), which BL:57–59 calls sufficient. The directed form and MM-9's necessity claim are
  what remain unsupported.
- **Remaining obligation.** A separate reviewed landing of L3: the extract and the status note it rests
  on, each covered by an independent review at its landed blob, landed with the owner's authorization
  (OQ-7, the historical authorization for L3, is open at #868 comment 6874036684). Until then, BL's
  directed form of (Sep) and SR3's MM-9 necessity are support off `main`.
- **Accountable Issues.** #868 (ladder stage 3); #1169 (SR3 MM-9 and `DEPENDENCIES.md` row D2).

### E2. QH: the stage-7 illustration

- **Statement.** BL:104, stage 7: "The native encoded U′ composite reaches the non-quantum table SWAP/2
  (QH:68–97) [D], which is Bell-local over Pauli-axis product tests [A]"; and BL:300, which classes QH as
  "support off `main`: gap for the stage-7 illustration, on which no verdict rests".
- **Why unsupported.** QH is Q-868-H unit 1 r3 (#1269 at `ffc9cda4`), not on `main`. By the owner
  decision it is non-load-bearing context: the stage-7 verdict, UNDETERMINED, rests on stage 5, Main:360
  and SB N4 (SB:190), which `intervene-substate-results-20261113/NEW-RESULTS.md` §5 carries on `main`.
- **Remaining obligation.** None before this landing. Any later use of the SWAP/2 illustration as support
  needs QH landed with a review covering its landed blob. OQ-6 (#868 comment 6874036684) is resolved by
  this decision for this landing.
- **Accountable Issue.** #868.

### E3. The unlanded Bell probes

- **Statements.** The X tags of BS, which cite `probes/generic_bell_checks.py` and its output
  `probes/generic_bell_checks.out` (#1231 at `e1534b08`; blobs `e47f3179` and `0798db76`): the X legend
  (BS:23); rows C4–C7 (BS:100–104); the parenthetical "X: G1 …" in Theorem N's proof (BS:178); the X
  tags of Lemma G (BS:198, :212–213, :218), §4.1 (BS:317, :332) and §4.2 (BS:345); §3.6 (BS:298–311),
  including "run with `python3 -I -B`, exit 0, all seventeen checks PASS" (BS:301); and BS:439,
  which classes the probe as a gap if the record lands.
- **Why unsupported.** The probe files are not on `main`, and the run has not been ratified or replayed
  from `main`. They are provenance only, not independently reproduced support. The ladder runs no
  probe (BL:15). The review read the probe without running it and found that, until ratification, the checks rest
  on the hand arguments (RV:167–185). It re-derived Theorem N,
  N′, Lemma G (one direction), the §4.1 bound and §4.2–4.3 by hand (RV:27–29); those are paper
  derivations, model-reviewed, and do not rest on the X checks.
- **Remaining obligation.** OQ-8 (#868 comment 6874036684): owner ratification of the run, a replay from
  `main` that matches the recorded output, and the probe landed with its output. Until then no BS
  statement takes support from an X tag.
- **Accountable Issue.** #868.

## Status note: BS findings 1–3

The independent non-author review of BS r2 at `e1534b08` (`REVIEW-BS-r2-NONAUTHOR.md`, ACCEPT WITH
CHANGES) found three statements outside the proved core that need correction (RV:244–291). By the owner
decision above, this note records their limitations. The passages stay as written in
`BELL-SCOPE-UNIT1.md`; where a passage and this note differ, this note gives the record's status. The
review's replacement text (RV:246–291) is not adopted here: it is a model review, evidence of review
and not independent verification (§A.46 item 7), and no corrected wording is promoted to a result.
None of the three affects Theorem N, Theorem N′, Lemma G, the §4 bound or BS's verdicts: (C)
indeterminate for OI, (A) an obstruction for 𝒞_sep only, (B) not established (RV:27–36).

| Finding | Passages | Limitation | Status of the passages |
| --- | --- | --- | --- |
| 1 | BS:49–54, :73–74, :246–253, :410, :453–456 | The O1 analysis does not take ledger item (vii) into account, although (vii) is in NBA's stated domain (BS:232). The review finds that under (vii) the two readings of (x) do not differ for `G_φ`, so inside NBA's domain O1 is closed, and the conflict is between (vii) and Main §3.3(a)'s adopted branch rather than a reading of (x) (RV:246–269). The finding concerns the record at its pin, not later drift in its sources. | Not relied on as stated: BS's "O1 open" for NBA's domain, its "(x) read globally / reference-class" dichotomy, the P-a disposition and F1. |
| 2 | BS:72–74 | The sentence "its failure through a sourced native coupling with complete-history no-signalling would give (B)" treats a necessary condition for (B) as sufficient; it omits CHSH > 2 under (MI) with every-run outputs. The review gives a counterexample (RV:271–278). BS §3.4 (BS:267–272) states the (B) lemma with that condition. | Not relied on as stated; (B) needs the conditions of BS §3.4. |
| 3 | BS:381–385 | The Level-A disjunction lists a cross-wing `G_φ` path, failure of measurement independence and failure of every-run accounting. It omits failure of (D), (F), (Gen) or (Rec), so it is not exhaustive (RV:280–291). | Not relied on as an exhaustive classification of constructions near the Tsirelson box. |

**Remaining obligation.** An r3 of the Bell-scope record, or a reviewed correction landed in its own
change, if any later record needs the corrected statements as support. Until then these passages are not
support for any statement on `main`. Accountable Issue: #868.

## What this record does not do

It does not land the content listed above, edit a copied file or `SYNTHESIS-r3.md`, adopt a premise,
or authorize work (§A.45 rule 3; §A.46 item 4). It changes no classification in `SYNTHESIS-r3.md`.
