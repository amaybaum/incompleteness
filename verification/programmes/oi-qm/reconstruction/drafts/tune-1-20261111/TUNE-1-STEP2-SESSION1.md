# TUNE-1, Step 2, writer session 1: M0 record and M1 controls

**WIP / UNVERIFIED research record.** Writer session 1 of 3 for Step 2 of TUNE-1 (Issue #1236),
under the owner's paper-only authorization recorded at Issue #1236 comment 6816189419
(2026-11-12), as relayed to the writer; the writer did not read that comment. Paper derivations
only: no code, interpreter or numerical computation was run; no manuscript or Lean file is
changed; no premise is adopted; nothing is frozen, dispatched, merged or promoted.

**Approved text.** `TUNE-1-STEP2-PROPOSAL.md` in this directory at
`e676c42adfe7ff1b4de171d37018d8a569dad1e6`, sha256
`2a081101efae469b39b747ef8f3641f259e55892705bc0f7759adf3ac7499fd5` (checked at the start of the
session; the proposal is not edited here). Section and clause names below are the proposal's.

**Labels.** As in the proposal: **[K]** a Lean statement under `verification/lean-mathlib/OIBridge/`
(statement read, nothing built); **[P]** a manuscript statement; **[R]** a research record on
`main` that states it is not independently reviewed; **[W]** this writer's derivation, unreviewed
and not kernel-checked.

**Sources.** Records are read at the Step 1 pin `cac5d26441dd33e9348151487e4df7b547195481`, as the
proposal fixes. `origin/main` was fetched at `1b27369816e0e26b39b9dcf1ad0335016c6082c9`. Between
the pin and that head, of the files read for M1 only `papers/Main.md` and `papers/SM.md` changed
(PR #1243). The changed lines of Main are the posit ledger (pin :726; it now lists a fourteenth
posit, measurement independence, and rewords items (ii) and (v)) and lines other than :560, :566,
:582, :596, :598; no M1 derivation below uses a changed line.

***

## 1. M0: the owner's choices

Recorded from the owner's authorization (Issue #1236, comment 6816189419, 2026-11-12, as relayed).
They are fixed for this question and are not reopened after a verdict (proposal, M0).

| Choice (proposal section 9) | Owner's option | Effect on Step 2 |
|---|---|---|
| 1. Rule | (b) R-lin first (node L5), then R-nl as a separate verdict under H-nl | R-lin node before any R-nl work; H-nl carried by every R-nl conclusion |
| 2. Alphabet | (a) every fixed `q ≥ 2`, `q = 2` first | Statements per fixed `q` |
| 3. World | (b) finite tori, and `𝓛_∞` under H-∞ as a separate conditional result | Separate tokens for `𝓛_fin` and `𝓛_∞` |
| 4. Error measure and horizon | (a) TV on complete records, every `K`, `N(ε, K)` explicit | Fixed-`K` results are `PARTIAL-FIXEDK` |
| 5. How the observer chooses | (c) both modes, reported separately | `init` and `exch` (under H-write) tokens kept apart |
| 6. Ensemble | (i)(c) every law of the list, each with its own token, with the robustness clause of D3 | Uniform law, level-set law (on `𝓛_fin`, exchange mode; "not defined" elsewhere, 6(iii)), non-uniform product law |
| 7. Rebit or qubit | (a) the whole Bloch ball (Q6) | A disk is `PARTIAL-REBIT` |
| 8. Partial results | (a) reported, each labelled as not answering the question | |
| 9. [R] premises of a negative | (a) re-derive in the unit (MECH-1 Lemma A, MECH-2 Lemma F) | |
| 10. Effort bound | (a) three writer sessions with reviews | This is session 1 |
| 11. Compiled simulators | (a) supplied (`OPERATIONAL-ONLY`) | D6 consists of tests (a) and (b) |

**Hypothesis ledger at M0.** H-μ, H-∞, H-nl and H-write are named and not adopted. No M1
derivation below uses any of them: the controls are classified from their own constructions.

**M0 approval statement.** The proposal requires the owner's approval record to state: "A
`PASS-DERIVED` would be a consistency-axis result (§A.23); it would move no correctness
assessment." The writer has not read the approval comment and cannot confirm that it does; the
reviewer is asked to check it.

***
