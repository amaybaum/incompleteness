# Q-C2-1: next owner decisions, R1–R10

WIP / UNVERIFIED paper decision packet. Writer: Codex, 2026-11-10. Accountable issue: #1169.
Guiding research draft: [#1218](https://github.com/amaybaum/incompleteness/pull/1218).
All ten rulings are **PENDING**. Recommendations below are proposals, not owner decisions.

This packet accompanies the paper-only r14d preparation repair and implementation plan. It is not a
round control plane, candidate F, execution request, new experiment or physical-source investigation.
The published scripts have not been updated or run by this pass. Review of this packet cannot certify them.

## Why the list has ten decisions

The prior #1218 description lists R1–R9 from published r14b at
`8f969ab6f6cbd2d04fff86cdff2b85d92433a12f`. The later archived r14c adds **R10**, concerning host-time
evidence retention. Its independent preparation review returned REVISE (minor), with R14C-B1, B2 and B3.
The archived handoff says the r14d writer was interrupted with nothing written. This pass supplies r14d;
it does not attribute the r14b or r14c review verdict to r14d. Exact publication and review SHAs belong in
the guiding PR checkpoint comments, so the files do not contain circular self-identities.

The latest source is the archived r14c, not the older `DECISIONS.md` r9a sheet. The present decisions
preserve D19–D23 and SG-1–SG-4 unless the owner explicitly rules on one of the open alternatives below.

## Authority and limits

The owner-authorized preparation record is [#1169 comment 6740078002](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-6740078002),
amaybaum, OWNER, 2026-11-09T12:29:10Z. It records the answer **“Adopt and authorize”** to:

> Authorized now: r14, bringing the scripts up to date, ordinary non-scientific self-tests, and independent
> preparation review.
>
> Not authorized: design run, gate tests, F designation or dispatch, any scientific computation.
> Q-C2-1 is completed before Q-C2-2 is activated.

The owner-approved research-branch publication is
[#1169 comment 6742190154](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-6742190154),
2026-11-09: **“Q-C2-1: a research-branch draft PR only, with no splice tree before the design run is authorized.”**
That record leaves the R1–R9 rulings undecided. Its historical numbering does not decide the later R10.
The [writer transfer](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-6748265756)
assigns Codex new #1169 writing and coordination while Claude is paused. Historical authorship stays intact.
The current owner request is to complete #1228's focused review and prepare the Q-C2-1 decisions; it
expressly grants no new execution authority.

No numerical/scientific/Lean program, fixture solver, stress test, gate test, workflow dispatch or rerun
was executed for this paper pass. No new physical premise is adopted. #1216 remains outside this task,
#1210's frozen designs are untouched, and the #866 physical-source gate remains **NOT PASSED**.

## Decision sheet

Each default below is the r14c draft's labelled default, not a recorded owner choice. The recommendation
set is intended to limit scope and preserve fail-closed evidence checks; it is not selected from run outcomes.
No measurements exist in this pass from which to infer feasibility or choose successful caps.

| Ruling | Choices and consequence | Coordinator recommendation, pending owner decision |
| --- | --- | --- |
| **R1 — ST-BP budget `S_max`** | **Default:** initial positive integer at least 100,000, bounding visited `(d−1)`-subsets separately in solver and verifier. After a red design run the owner may retain or lower it, never increase it; the floor may be removed by the same decision if the red run used at most 100,000. **Alternative:** no floor at any stage, with the same positive, nonincreasing owner-rule requirement. The 1,200-second timeout test and 60-minute workflow limit remain separate constraints. | Default form/floor/lowering rule; **proposed initial `S_max = 100000`**. This is the smallest value allowed by that initial floor, not an affordability finding. It need not raise the copied binomial cap above 100,000. Other caps and budgets stay pending until a separately authorized design run fixes them. The owner may instead specify a different positive integer with the selected rule. |
| **R2 — red fixture control at S1 or E** | **Default:** A3 exits 3; reproducibility failure halts the whole round, every result VOID. **Alternative:** only tokens in the red control's `for` column are void. That alternative requires the complete keyed fixture-exit, artifact, note/verdict, reading and Control-B/M-GUARD changes specified in r14d; keeping A3 red and merely adding `always()` does not give a green exact-head E attestation. | Default whole-round halt. This preserves the conservative fixture-validation treatment while decisive C-only failures still have D21(b)'s test-level effect. The alternative is available only with its entire implementation and review obligation; the owner is not asked to approve an incomplete shortcut. |
| **R3 — reported-only work volume** | **Default:** charge `1203 × W_max` for B-P completions, construction A, up to 600 B-C fragments and their completions. SF-2 is measured without a cap/budget in the stress phase and enters the general maxima. **Alternative:** an owner-fixed aggregate `W_RO`, with build-order processing and all remaining fragments explicitly `out_of_scope` once exhausted; R5 sets each fragment's caps. | Default. If the complete timeout test fails, no F is requested. Incompleteness must be reported rather than silently dropping work. No stress measurement is authorized by this recommendation. |
| **R4 — B-P versus reported-only priority** | **Default:** choose B-P's reference with the full reported-only term in the timeout test, even if that yields a smaller reference or copied caps. **Alternative:** choose the B-P reference with that term zero, then allocate `W_RO = (1200 − t_810)/σ − W_max^BP − 2 W_fix − W_stress` to reported-only work, in build order. This forces the aggregate-budget treatment whatever R3 selected. | Default whole-volume accounting. Do not prioritize a favourable B-P scope by silently reducing reported coverage. A future measured feasibility problem returns to the owner. |
| **R5 — raised caps** | **Default:** raised caps apply to B-P only; all other B fragments use general caps/budgets. **Alternative:** every B fragment uses B-P's raised caps/budget triple; fixtures and QM-P's restricted fragment retain general caps. The reported term becomes `1203 × W_max^BP`, so the full default timeout left side is `σ × (1204 W_max^BP + 2 W_fix + W_stress) + t_810`; R4 applies if selected. | Default B-P-only increase, matching the narrow interpretation. No current numerical cap is filled in. |
| **R6 — S1 measurements evidence expired at verdict capture** | **Default:** S1 binding fails and the whole round is VOID; E verdict capture must occur within the artifact's 90-day retention. **Alternative:** print “not checkable”; tokens stand only with E replay binding, explicitly without an S1-output binding claim. | Default fail-closed. This concerns the measurements artifact. Under R2's alternative, a missing/expired/unreadable **fixtures** artifact is still whole-round VOID, regardless of R6. R10 never waives an operational artifact check. |
| **R7 — REP-INV table changes beyond relabelling** | **Default:** do not re-decide the changed B-P/B-C table; record the changed input and reclassify the identification as imported. **Alternative:** re-decide under the role's caps/budget and charge each additional table in the timeout test; use the re-decided verdict for reclassification. | Default explicit imported classification, without adding computations. A representation invariance label cannot substitute for the required physical source. |
| **R8 — E dispatch's own approval entry** | **Default:** `e-entry` prints the canonical entry and digest; the executor posts it; a separate owner comment ratifies its hash before verdict capture. **Alternative:** the E designation quotes that entry hash alongside `order.json`'s hash, and verdict checks the designation. Under either, every host-VOID retake at E has its own entry and ratification. Both use the owner's identity, which is not independent of the session credential. | Alternative: include each E-entry hash in the E designation. This removes one owner act and adds no assurance claim. It is not an E designation now; all inputs, hashes, author checks and the owner act remain required at that later gate. |
| **R9 — UPR-BC completion not decided** | **Default:** when the specified completion is `out_of_scope` or `undecided`, print no UPR-BC label, do not reclassify L-UPRIME, and print B-C's measured result with completion status. **Alternative:** reclassify L-UPRIME as imported for B-C and label the result as a benchmark with that status. | Default, preserving the explicit unresolved completion. Neither choice changes any Level: B-C does not count toward Level 2 under D17(a). Unresolved never means a positive or negative completion verdict. |
| **R10 — host-time evidence** | **No default.** **Exception:** recorded owner exceptions for each unretainable host-time record, naming each claim left unsupported; those claims remain unestablished under A.46. **Narrowing:** state only conditional landing requirements and do not assert they were met or infer a governance fact from unretained content. Both options require revising and independently reviewing every named dependent passage before F. Scientific tokens require their separately authorized replay at E; neither option retrospectively supplies it. | Narrowing. Keep actual checks as conditions that must pass, retain their records as provenance, and omit an enduring assertion that the unretained host-time checks passed. This is proposed claim scope, not an evidence-retention exception, operational waiver or established governance result. |

The proposed initial R1 number is new **advice** only. The preparer does not enter it into the draft,
scripts or `stress.json`. Choosing the other recommendations would not implicitly choose R1's number.
The owner must quote the actual value and each selected option; a partial decision leaves other rows pending.

## Three r14c review findings and the paper repair

| Finding | r14d repair | Still required before a round can proceed |
| --- | --- | --- |
| **R14C-B1 — designation comment not identified** | C.3 requires author `amaybaum`, association `OWNER`, full 40-hex F identity as the designation, and records quoted words, identity and times. APPROVAL-ENTRIES and implementation rows D20/D29/D30 carry rejection cases for wrong/missing F and wrong owner/association. | Implement and verify the requirements; supply a real owner designation only at its separate gate. No arbitrary earlier owner comment can discharge the check. |
| **R14C-B2 — R2 alternative omitted guard changes** | R2's conditional alternative explicitly names the ZipFile member-read allowlist and the single extra fixture-exit `DISPATCH_EVENT` reference site, with M-GUARD/ZIP mutations. D36 matches. S1 red controls go through `derive-run`'s committed record for `note`; verdict re-reads the artifact. | If the owner selects the alternative, implement all changes and review them together. Under the default these conditional widenings are not adopted. |
| **R14C-B3 — R10 narrowing asserted checks were met** | R10 says only “conditions of landing”, not “conditions met”; it lists all dependent sites to revise before F and states the different governance/scientific consequences of each option. | Owner selects the disposition; revise/review the actual sites accordingly. A comment ID alone changes neither the assertions nor their evidence. |

The r14c review's nine nits are also disposed in `DISPOSITIONS-r14d.md`. Their paper edits include unfinished
capture handling, the checker-bearing executor precondition and local-run authorization boundary, explicit
two-bit fixtures, and the unbound confirmation copy's vacuous-pass limitation. No new fixture was executed.

## Decision dependencies and the next gate

1. Independently review the exact pushed r14d preparation/implementation-plan/decision checkpoint. This is
   separate from #1228's completed focused review and from the old r14c REVISE verdict.
2. Owner decides R1–R10 individually. R3–R5 must yield one consistent timeout expression; R7's alternative
   adds the declared work for each re-decision. R2's evidence obligations are not relaxed by R6 or R10.
3. Apply the decisions to all draft sites and the implementation plan, update the scripts under the
   already bounded preparation authority as appropriate, and obtain the applicable independent review
   and ordinary CI. This pass has not performed those implementation steps.
4. Only then prepare a **separate** request for a design run, explicitly including the local A3 fixture
   runs required before each checker-bearing recorded-branch push. No frozen-splice tree is pushed before
   that authorization. Neither a ruling on this sheet nor ordinary research-PR CI authorizes such a run.
5. F still needs every precondition: retained source/proof records, reviewed representation ledger and
   ATTR, the owner's commitments, no blocking review finding or pending item, authorized design/confirmation/
   gate tests with fixed caps and budgets, and the required exact-head attestations and owner designation.
   E, later scientific execution, integration and merge retain their own gates. Q-C2-2 is not activated.

Any later execution request must disclose the known incomplete-run residual and the scope of the
repository-wide event/attempt inventory. `Forbidden`, missing pages or missing records do not prove an
empty inventory. No inventory has been collected by this paper pass, and no access gap is waived here.

## Scientific scope retained

P's primary contrast is detector **off versus on**. Shams test attribution and remain controls; they do
not replace the primary contrast. Valid record probabilities, quantum-state closure, quantum compatibility
and operational coverage have separate verdicts. P, B and C do not by themselves form one physically sourced
reusable preparation–controller–record mechanism. Encoded or comparison-map choices are accounted for as
imported unless their source is independently established. Success in a fragment is not full equivalence.

The previously completed Lemma P and cone proof reviews are not repeated. Lemma P retains its explicit
conditional hypotheses. The cone result requires STAB(K); it does not determine the actual K=6/12 cases,
and its unqualified use is not reinstated. Full OI–QM equivalence, uniform OI-derived approximation,
Born-rule derivation, Bell/composition and native apparatus availability remain separate obligations.

## Source ledger

All paths below are immutable repository sources. Off-main references remain off-main support: a future
landing must retain the material actually used, re-establish it on main, or narrow the attached claim
under A.42/A.46. A link or this source table is not evidence retention or integration authority.

| Source | Identity and use |
| --- | --- |
| Main D and AGENTS | `cac5d26441dd33e9348151487e4df7b547195481`; AGENTS blob `496eb7018c736a064dddcf00fd1a278790872f49`. Governance baseline, not a run result. |
| Prior guiding checkpoint | `8f969ab6f6cbd2d04fff86cdff2b85d92433a12f`, path `verification/programmes/oi-qm/reconstruction/drafts/arp2-qc21/`. Published r14b and unchanged scripts/proof reviews. |
| Archive checkpoint | `820519cf011c09b37690213a758106ed3aa15cc2`, path `handoff-20261109/qc21/`. The archived r14c is the input to this repair. |
| r14c draft | `preregistration.draft.md`, blob `237434d57ed694d55f209f5dde2c84040838d309`; SHA-256 `d4e0fca90180400b77f6290eb1c1df305be14a7f86591cecd76337b907651ef7`. R1–R10 and all repaired sites. |
| r14c review | `review/REVIEW-QC21-r14c.md`, blob `6677f389a603e249a9e0e8c7e0e80ef5edeebf67`; SHA-256 `f41ac442a715a37924e3563665bafc8d61b3751f89f6fef89e2ec05bc051ee8d`. REVISE (minor), B1–B3 and N1–N9; not an acceptance of r14d. |
| r14c dispositions | `DISPOSITIONS-r14c.md`, blob `0fe9d39e3453fae8cc44f8b6ac5f55170b92ad4c`; SHA-256 `61cff2885c87495ad19ced5421c34447d2888b3b282e9fcc459f9fe5c9ced43f`. Historical r14b-to-r14c account, not disposition of the later review. |
| r14c implementation plan | `IMPL-DELTA-r14c.md`, blob `4242589420eda93fcdb4e2701c9700d4fa8b5c8e`; SHA-256 `80df27b0656e33fefeb63e01f2e7160beb44ccd37fd500486450aeeff5a1682d`. D20/D29/D30/D31/D36/D39 consistency repairs; no script-validation claim. |
| Archived handoff | `820519cf011c09b37690213a758106ed3aa15cc2:handoff-20261109/HANDOFF.md`, blob `6f5824b965237a08557ad090dcc3ed79737acac9`. r14d interrupted; #1218 carried r14b; next sequence was r14d, review, R1–R10 sheet. |

Status: **owner decisions pending; execution not authorized; physical source NOT PASSED; draft/unmerged**.
