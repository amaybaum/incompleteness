# ARP-3, Q-C2-2: the access and noncontextuality of P★'s `G_SM` fragment, with attributed completions. Native round ARP-3-QC22 — PREREGISTRATION (draft r14b)

**Status: WIP / UNVERIFIED preregistration, drafting, not a candidate `F`.** Model-written.
- **Review history.**
  - r1 (`e2b58ae6…`, kept in `r1/`) was reviewed REVISE (`review/REVIEW-ACCESS.md`).
  - r2 (`1e994da4…`, kept in `r2/`) was re-reviewed ACCEPT WITH CHANGES, with two blockers
    (`review/REVIEW-ACCESS-r2.md`).
  - r3 (`96f40e55…`, kept in `r3/`) was reviewed REVISE, with four blockers (`review/REVIEW-ACCESS-r3.md`,
    `86c6c8ad…`; independent probes in `review/probes3/`).
  - r4 (`5be64077…`, kept in `r4/`) was reviewed REVISE, with three blockers (`review/REVIEW-ACCESS-r4.md`,
    `91934582…`; probes in `review/probes4/`).
  - r5 (`9dc8fe83…`, kept in `r5/`) was reviewed ACCEPT WITH NITS, with no blocker (`review/REVIEW-ACCESS-r5.md`,
    `5fe0ec53…`). r6 applies its N1–N4. Earlier, r5 applied r4's review, and r4 applied r3's review and the owner's
    direction c.6724832474.
  - r6 (`1ff41c90…`, kept in `r6/`) was reviewed REVISE, with one blocker present since r1 (`review/REVIEW-ACCESS-r6.md`,
    `d44ecc06…`): F1 would have been computed by the S1 and `E` pull-request runs. r7 applied it with the event guard,
    and applied N1–N2.
  - r7 (`8da96f9d…`, kept in `r7/`) was reviewed REVISE (`review/REVIEW-ACCESS-r7.md`, `947bd3b0…`). The review found
    two gaps: re-run attempts and dispatches on other refs bypassed the rules, and the guard was incompletely measured,
    with `mode` unchecked. r8 applied both and N1–N4.
  - r8 (`cd71b3f9…`, kept in `r8/`) was reviewed REVISE (`review/REVIEW-ACCESS-r8.md`, `553e90bb…`). The review found
    two gaps: the guard's static rule was a literal-string blacklist, and the enumeration's completeness was
    unproved. r9 applied both, N1 and N3.
  - r9 (`71534757…`, kept in `r9/`) was reviewed REVISE by a new reviewer (`review/REVIEW-ACCESS-r9.md`, `d7e95d74…`;
    host facts H1–H10). r10 applied its four blockers and N1–N7.
  - r10 (`6bd22d31…`, kept in `r10/`) was reviewed REVISE (`review/REVIEW-ACCESS-r10.md`, `3431a98a…`; host facts
    H11–H16), with three blockers.
  - r11 applied those three blockers and N1–N5, on the owner's decisions c.6726548830: the Environment gate as the
    primary enforcement, landing gaps closed, no re-run attestation, and no run deletion.
  - r11 (`681b9fab…`, kept in `r11/`) was reviewed REVISE (`review/REVIEW-ACCESS-r11.md`, `22d9cda8…`; host facts
    H17–H23), with two blockers.
  - r12 (`391d2003…`, kept in `r12/`) applied them and N1–N9. Its independent review was ACCEPT WITH NITS
    (`review/REVIEW-ACCESS-r12.md`, `ba2ac209…`; host facts H24–H25). r13 applies its nits N1–N6 and changes
    nothing else.
  - r12's main changes were the Environment's reader and channel and the identity limit, each a neutral owner
    decision in precondition 2b. The dispositions are in `PLAN.md`.
  - r13 (`15d90b24…`, kept in `r13/`) had a full independent review, REVISE (`review/REVIEW-QC22-r13-full.md`,
    `6d1a8f8a…`; host facts HF-1 to HF-6), with six blockers in the execution machinery (B1–B6) and nits N1–N25.
    r14 applies them under #1169 c.6740747027 (amaybaum), reusing Q-C2-1 r14's repaired wording (`ae6f0e26…`) where
    the method is shared. Tags `R13-B…` and `R13-N…` below name that review's findings. The dispositions are in
    `DISPOSITIONS-r14.md`.
  - r14 (`9e3ef0c9…`, kept in `r14/`) had an independent review, REVISE (`review/REVIEW-QC22-r14.md`, `d344e277…`),
    with three blockers (Rb1–Rb3) and nits N1–N11. r14a applies them, reusing Q-C2-1 r14a's wording
    (`1dd595d3…`) where the machinery is shared. Tags `R14-Rb…` and `R14-N…` below name that review's findings.
    The dispositions are in `DISPOSITIONS-r14a.md`.
  - r14a (`d751a127…`, kept in `r14a/`) had an independent review, REVISE (`review/REVIEW-QC22-r14a.md`,
    `c63ca1cc…`), with one blocker (Rc1) and nits N1–N9. r14b applies them, reusing Q-C2-1 r14b's wording
    (`57053e08…`) where the machinery is shared. Tags `R14a-Rc1` and `R14a-N…` below name that review's findings.
    The dispositions are in `DISPOSITIONS-r14b.md`. r14b is not yet reviewed.
  - **Authorization of the revisions.** c.6740747027 authorized r14 and a further independent review. That it also
    covers r14a, r14b and their reviews, as fix-and-review iterations until this file is ready, is the coordinating
    session's reading, not the owner's words (R14a-N1).
- **Governance.** This file is the control plane of a native round under `AGENTS.md` §A.39, to be drafted on its own
  guiding pull request from `D`. Execution is under #1169 c.6723277401. The owner designates `F` and `E` and approves
  each dispatch (#1169 c.6723329527).
- **Not before ARP-2.** This round is not frozen before ARP-2 (Q-C2-1) has completed and its result has been
  independently reviewed (precondition 1).
- **Run at all?** Whether to run F1 at all is an owner decision at the freeze, because the audit's literal check is
  predicted feasible on paper and is decided in-run by CC-F0 (*The specification and its outcome*; R14-Rb2).
- **`PENDING` discipline.** Every `PENDING` field is filled before `F` is requested. Control P refuses, under
  `--freeze`, any occurrence of the word `PENDING` that is not inside backticks. This text's own mentions of the word
  are backticked; the unbackticked ones are the fields (re-review N5).
- **Definitions.** The paper analysis is `ACCESS.md` (r14a), a preparation note outside the control plane. Every
  definition used here is restated below.
- **Off-`main` references (§A.42 item 8; R13-N24, R14-Rb2).** Each reference this file makes to content not on
  `main` is classified separately in *Off-`main` references*, after *Authority*.

```v3-round
round ARP-3-QC22
kind non-sealing
record-directory verification/programmes/oi-qm/reconstruction/round-arp3-qc22-20261108/
```

```v3-governed-paths
record AM verification/programmes/oi-qm/reconstruction/round-arp3-qc22-20261108/
record AM verification/receipts/ARP-3-QC22.json
execution M .github/workflows/verify.yml
```

**Frozen expectation for the two blocks.**
- **Round lines:** `round ARP-3-QC22`, `kind non-sealing` and
  `record-directory verification/programmes/oi-qm/reconstruction/round-arp3-qc22-20261108/`.
- **Governed-paths digest:** computed as `S7` defines it, with `governed_digest` from `tools/v3_verifier.py` at
  `2cd49dc0`, it is `9f3808ac33d65a27dc363a88a0d0e7df16c77fa33f49d2c0f22b0df279b049b6`.
- **Re-derivation:** precondition 7 and control T re-derive both.

**Record directory.** It holds:
- this file and its amendments (before `F` only);
- `qc22_check.py` and `controls.py`, at their pinned blobs;
- `evidence/`;
- `result.md`.

**Execution path.** The only execution path is `.github/workflows/verify.yml`. No manuscript, built artifact, kernel
module, source record, `verification/ROADMAP.md` or other round's record changes under any outcome (`S7`).

## Authority (quoted with author and time)

All entries below are amaybaum on #1169, quoted verbatim.

- **c.6723277401** (2026-11-08T15:21:11Z):
  - "3. **Q-C2-2** — Execute after Q-C2-1 has completed and its results have been independently reviewed."
  - "Preserve negative, inconclusive and vacuous results without reinterpretation or post-hoc changes to acceptance
    criteria."
  - "Stop and report any failed gate, unresolved blocker or material deviation rather than bypassing it."
  - "The priority is genuine assumption removal, not obtaining a positive result by introducing equivalent
    assumptions under different names."
- **c.6723329527** (15:25:55Z):
  - "Before each freeze, present the reviewed candidate F, exact commit, independent-review verdict, controls and
    outstanding blockers for my designation."
  - "Before each execution, present the exact execution head E and proposed dispatch for my approval."
  - "No automatic freezes or dispatches. The halt-only rule remains mandatory, and any failed gate stops
    progression."
- **c.6723491138** (15:40:41Z):
  - "The preregistered outcomes should remain unchanged. Any broader conclusion should be separately qualified, and
    new variants should be tested in new rounds rather than retroactively modifying the original experiment."
  - "Conversely, relaxing an assumption is not sufficient by itself. The resulting model must still produce valid
    probabilities, observable quantum predictions and consistent behavior across repeated experiments."
  - "We should not weaken the empirical standards for equivalence. We should instead challenge whether our chosen
    mathematical framework for testing equivalence is unnecessarily restrictive."
- **c.6723571280** (15:47:58Z):
  - "Q-C2-2: Require instance-specific witnesses. Distinguish genuine operational accessibility from an inability to
    certify it within a particular mathematical framework."
  - "One additional principle should guide interpretation: failure to construct a witness is not proof that no
    witness exists, unless a theorem establishes that impossibility within a clearly stated scope."
  - "Which apparent obstacles survive when we retain only native OI principles and genuinely observable quantum
    requirements?"
  - "The third is what ultimately matters. We cannot establish equivalence merely by escaping a no-go theorem."
    This refers to the ladder rung "The mechanism reproduces the required quantum predictions, measurements and
    composition | We advance toward operational equivalence".
- **c.6723889799** (16:16:38Z):
  - "The accessible but uncertifiable functionals are equally interesting conceptually. They may reveal that requiring
    an observer to certify an operation is stronger than requiring the observer to experience its measurable
    consequences."
  - "Neither route is established yet, but both merit investigation."
  - **How this file uses it.** EXP below, read-record dependence, is this round's correlational reading of
    "experience its measurable consequences". It does not separate experiencing `g` from experiencing a correlate of
    `g`.
- **c.6723585151** (15:49:15Z):
  - "Add a hidden-prior sensitivity requirement. When a result changes under correlated hidden distributions, its
    stated scope must identify that dependence."
  - "Hidden information can influence physical dynamics without being accessible to the embedded observer."
  - "A proof that excludes such memory is valid only within that restricted model; it cannot automatically establish
    a limitation of OI generally."
- **c.6724832474** (17:42:02Z), the owner's direction on this preregistration's r3:
  - "R-U′: The corrected substitute law must genuinely test whether the observed behavior depends on the specific
    hidden quantity, rather than producing a misleading negative."
  - "Exact linear programme: Certificate-checked decisions and a fixed computational budget prevent uncertain results
    from being presented as established."
  - "Prefer declaring the configuration out of scope if it cannot be decided within the fixed resource budget, rather
    than weakening the test merely to obtain an answer."
  - "However, if pre-freeze timing evidence supports a scientifically meaningful narrower configuration, that
    alternative may be proposed before F, provided its scope and controls are independently reviewed."
  - "Once frozen, no opportunistic narrowing or additional computational budget should be permitted. Undecidable cases
    must receive the preregistered VOID outcome."
  - "This is a preference, not yet the formal freeze decision."
  - "One additional requirement for the Q-C2-2 review: verify that certificate validation is genuinely independent of
    the decision procedure. A solver accepting its own unchecked output would undermine the purpose of the control."
  - **How this file uses it.** R-Uc and `g_specific` (*The model*); C-INDEP and the certificate mutations (*The
    controls*); the budget rules and the stop rule. The F1+R-S decision stays the owner's at the freeze
    (precondition 2), with both options kept.
- **c.6726548830** (amaybaum, 2026-11-08T20:14:37Z), the owner's decisions on execution safeguards, recorded from
  the coordinating session's chat:
  - "My recommendation is to use the stronger GitHub Environment gate rather than accept the remaining landing gaps."
  - "CI evidence retention | Approve. No CI run deletion until Q-C2-2 closes."
  - "Two remaining landing gaps | Do not accept. Require a technical solution."
  - "Re-run as attestation | Reject. A blocked, non-computing re-run cannot attest to an F1 result."
  - "GitHub Environment gate | Approve. Require explicit owner approval before every decisive execution."
  - "Freeze readiness | Conditional. Wait for independent ACCEPT of r10 and verification of the complete gate."
  - "The Environment gate should verify the exact approved commit, run identity, inputs, and approval. Unauthorized
    executions must remain blocked, including after landing on `main`."
  - The record adds: "The owner creates the Environment and its protection rule."
  - **How this file uses it.**
    - Job B and the Environment (*The workflow edit*; precondition 2a).
    - The review-to-run binding (*Runs, evidence, approvals*).
    - The re-run rule.
    - The gate tests (precondition 6″).
    - Precondition 2's decided items.
    - The freeze condition (item 4).
- **The specification and its outcome.** Q-C2-2 as accepted in the EOI classification audit, cluster C2 (`AUDIT-C2.md`
  §13, §17; REVIEW-C2-r2 N5; REVIEW-C2 N10), and the gate draft r4's imitation rule with its R3-B2 text. These are
  paper-only, model-written and model-reviewed; nothing in them is adopted.
  - **The audit's literal check is predicted feasible on paper and decided in-run (R14-Rb2).** Its preparations are
    P★'s branches and mechanism-off `Z±`; its reads are the frame-time `Z` and `X`. The paper analysis (`ACCESS.md`
    Proposition F0) gives an explicit noncontextual model. The round decides it as CC-F0, whose model the independent
    verifier checks. If CC-F0 is feasible, then by the audit's rule ("Feasibility closes the instance") the instance
    is closed for that fragment, at the prepare-measure level, and that is preserved as the outcome of Q-C2-2 as
    specified.
  - **This round adds a new question, F1.** It declares four changes from the audit's check:
    - **Preparations:** the P2 carrier inputs `Z±, X±` × herald replace P★'s input plus the mechanism-off branches.
    - **Reads:** 36 `G_SM`-mediated single-slot reads.
    - **Access notion:** the audit's L1, with EXP (read-record dependence, correlational) reported beside it.
    - **The functional's reading:** G-Y, with G-H1 reported.

    Contextuality is not monotone, so F1's result does not bear on the literal fragment.

## Off-`main` references (§A.42 item 8; R14-Rb2)

Each reference this file makes to content not on `main` is traced to the claim it is attached to, and classified by
reading that claim. **Provenance**: the claim does not use the referenced content. **Support on `main`**: what the
claim uses is stated in this file or in a record on `main`. **Gap**: the claim uses content held only off `main`; a gap
is closed by narrowing the claim, or by a recorded owner decision.

| reference | where | the claim it is attached to | classification |
| --- | --- | --- | --- |
| owner comments on #1169, cited as `c.<id>` | *Authority*; wherever a `c.<id>` is cited | the owner's directions, decisions and authorizations | support on `main`: each is quoted with author and time in *Authority* (§A.42 item 7). c.6740747027, which authorized r14 and a further review, is provenance; that it covers the later revisions is the coordinator's reading (R14a-N1) |
| the scratch drafts r1–r14a and their review notes and probes under `review/`; `DISPOSITIONS-r14.md`, `DISPOSITIONS-r14a.md`, `DISPOSITIONS-r14b.md`, `PLAN.md` | *Status* (review history) | the drafting history | provenance |
| each bracketed review tag, such as "(re-review r4 B1)", "(r11 N3)", "(R13-B1)" or "(R14-Rb1)" | throughout | the finding that prompted the passage; the passage states its own content | provenance, tag by tag. The tags that carry a host fact or a result have their own rows below |
| Q-C2-1's drafts r14 (`ae6f0e26…`), r14a (`1dd595d3…`) and r14b (`57053e08…`) | "Q-C2-1 r14's wording", "Q-C2-1 r14a's wording", "Q-C2-1 r14b's wording", "Q-C2-1's D19 (0)(c)" | the origin of shared wording | provenance: the wording used is stated here in full |
| `ACCESS.md` (r14a) as a whole | *Definitions*; *The question* ("`ACCESS.md` §6"); precondition 3 ("`ACCESS.md` F-2"); precondition 4 | where the paper analysis was drafted; what the owner disposes of and the review covers | provenance: every definition, law and argument that a control uses is stated here (H3's laws, the restriction argument in GX's row, Lemma NC-F, step 4's completeness, step 1b) |
| `ACCESS.md` Proposition F0 | *The specification and its outcome*; *Run at all?*; precondition 2 (O-7) | the audit's literal check F0 is feasible | gap, closed by narrowing: a paper prediction, decided in-run by CC-F0 with its model verified; the result note's common clause is printed only over a green CC-F0 |
| `ACCESS.md` §5 and §6 (the paper predictions for F1) | conditions (a)–(c) and their *Consequence*; *Expected bounds on paper*; *What infeasibility licenses* (R14a-N4) | L1 and EXP hold in F1; `r_S ≤ 6`; the bounds on `d` | gap, closed by narrowing: stated as predictions, which the round measures. No control or verdict rests on them |
| `AUDIT-C2.md` §13 and §17, REVIEW-C2-r2 N5, REVIEW-C2 N10, the gate draft r4 and its R3-B2 text | *The specification and its outcome* | where Q-C2-2 was specified | provenance: the round's question is stated in *The question*, and the one rule it applies, "Feasibility closes the instance", is quoted and used only as "the audit's rule" |
| `review/REVIEW-ACCESS-r4.md` §1.3 ("reviewer r4 §1.3") | GX's row | GX+R-Y is infeasible by restriction to X's sector | support on `main`: the restriction argument is stated in GX's row, and the confirmation run decides GX+R-Y (precondition 6′) |
| HF-1, the artifacts API's `digest` is the archive's sha256 (`review/REVIEW-QC22-r13-full.md`) | *`--stress`*; *Scripts*; *Runs, evidence, approvals* | no condition compares a `digest` with a file's sha256; the S1 binding requires `sha256(archive) = digest` | gap, closed by narrowing: a host premise. If it fails, the S1 binding's digest condition fails and the round halts (fail-closed); no other condition reads a `digest` |
| H17, the session's proxy refuses the Environments API (`review/REVIEW-ACCESS-r11.md`) | control N; 2b | why E-READ offers three channels | provenance: no condition rests on it; GT-6 tests the chosen channel |
| H20, a `waiting` status occurs without a review (r11) | *Runs, evidence, approvals*, *Order* | the review's time is bounded by the deployment's statuses | support on `main` from S1: the gate tests record the actual status sequence in `gate-tests.json` |
| H21, a skipped job lists no steps (r11) | precondition 6, `t_810` | B6 has no design-run step record | support on `main` from S1: `check --freeze` reads the step records from `design-run.json` |
| H22, host records cannot tell the owner's comment from the session's (r11) | *Authorship*; 2b (b) | a limit, under E-ID (i)–(iii) | provenance: the design treats the two as indistinguishable whether or not the host can tell them apart |
| H24, teams exist only in organizations (r12) | 2b, E-ID (i) | why no team option is offered | provenance: no control rests on it |
| H25, the MCP connector's tool surface (r12) | 2a | the session's second channel | provenance: the commitments there do not depend on the connector's schema, and (ii)'s reach is stated for its current surface only |
| "r10 review §3, H11–H15" and a read-only count of 2026-11-08 | *The call budget* | an estimate of a capture's calls | gap, closed by narrowing: an estimate that no condition uses; each capture measures and records its call count |
| the final capture's record; the `E`-stage Environment reads (A11's conclusion in the `E` run under E-READ (a); `check --stage E`'s and `verdict`'s reads under (b) or (c)); the approval entries `verdict` builds for the dispatches at `E` | *The window between `E`'s capture and `Q`'s push*; control N; *Approval entries* | no unapproved checker-bearing run between `E`'s capture and landing; the Environment as frozen at `E`; the dispatches at `E` approved | gap: host-time records that no round tree can hold, and that a later dispatch at `E` does not re-establish. Their disposition under §A.42 item 8 is an owner decision (precondition 2) |
| the `E` run's other records, read by `verdict` | `verdict` | the conditions on the run at `E` | support re-established from `main` by a dispatch at `E` (§A.42 item 7). Its route: after Q-C2-2 closes, the owner adds a branch at `E` to the Environment's deployment-branch policy, dispatches on it with `arp3qc22_decisive` true and `arp3qc22_sha` `E`, and approves its deployment review (*After merging to `main`*; R14a-N5) |
| S1's measurements artifact, `arp3-qc22-measurements` of S1's run (R14a-N4) | `verdict`'s S1 binding; *Retention* | the committed measurements are S1's output | support when it is read, provenance after it expires; the enduring support is `E`'s committed measurements, the binding's record at `E` and a dispatch at `E` (§A.42 item 7; *Retention*) |

## The objects

- **`D`** = PENDING: a full 40-hex id, the head of `main` after ARP-2's landing.
- **`F`**: the owner-designated commit carrying this file. `delta(D, F)` is this file and any amendments.
- **S1**: a single-parent child of `F`. It adds both scripts, `evidence/design-run.json`,
  `evidence/confirmation-run.json`, `evidence/confirmation-measurements.json`, `evidence/f-run/results.json` and the
  frozen workflow splice. Its owner-approved dispatch is the decisive computation, and the first computation of the F1
  family anywhere. The round PR's runs on pushing S1 or `E` skip job B and run job A in fixture mode (job B's
  condition; A3's literal; the no-unapproved-F1 rule). S1 also adds `evidence/gate-tests.json` and
  `evidence/env-pin.json`.
  - `confirmation-measurements.json` is the `fixtures.json` file inside 6′'s `arp3-qc22-fixtures` archive, copied
    by the executor (R13-B2; R14-N3). It is provenance for 6′, and the input of C-STATELESS (re-review r5 N1(c),
    (d)). It is committed before S1's run exists. No workflow step reads either 6′ record.
- **`E`**: a single-parent child of S1. It adds `evidence/measurements.json` (the file inside S1's measurements
  artifact archive; bound to the approved decisive computation by B6 at `E`, and to S1's output by the S1 binding,
  *Runs, evidence, approvals*; R13-B1, B2), `evidence/s1-run/results.json` (with the S1 binding's inputs; R14-N6),
  `evidence/order.json`,
  `evidence/order-s1.json` (the order-rule records captured at S1, with control N's S1 read under E-READ (b) or (c);
  re-review r7 N1; R13-B5), `evidence/approvals.json` (R13-B4) and `result.md`. The owner designates `E`.
- **`W`, `Λ`, `Q`**: as in §A.39 and `S12`.

**Drift.** No path under the inputs' directories, `tools/` or `.github/` changed from `5ce4f98e` to `2cd49dc0`. The
check is extended to `D` (PENDING), and DS re-measures it at S1 and `E`.

## Inputs (blobs at `2cd49dc0`, re-checked by DS)

`R/` = `verification/programmes/oi-qm/reconstruction/`. All are WIP / UNVERIFIED, model-reviewed records. This round
uses the rule, the instance P★ and definitions from them, all restated here. No result of theirs is a premise
(§A.46 item 7).

| short | path | blob | used for |
| --- | --- | --- | --- |
| M2D | `R/mechanism-2-20261108/DESIGN.md` | `9352d9da7da6a55a52e6ada235034219638b34d2` | `G_SM` (M2D:155-168); P★ (M2D:630-670); Theorem NC (M2D:485-507); Proposition B (M2D:543-591); the dichotomy (M2D:728-733); M-INACC (M2D:832-871) |
| M1D | `R/mechanism-1-20261107/DESIGN.md` | `7f8a142be31222b1aee74b05990bb58648387cae` | CC-IMIT′ (M1D:356, :729-733); C-COMP (M1D:360-376) |
| AP1 | `R/apparatus-1-20261107/DESIGN.md` | `51c24aeb7b42a915b8942462435fd9fe129861de` | SA-1(b), (c) (AP1:292-299); type grading (AP1:521-529); Lemma 4′ (AP1:698-727) |
| MID | `R/minacc-1-20261108/DESIGN.md` | `737047be04dcf94f1ddcf7eae0abf736e2c0d52e` | determined/biased (MID:135-139); protected class (MID:429-432); C-IMPORT (MID:573) |
| MIR | `R/minacc-1-20261108/RESULT.md` | `5adf76ebc8afa95cc51f45fb84c909b13876516c` | the form of a witness (`E_A`/`E_B`, `G_σ`; MIR:44-60), template only |

## The question

**F1 (new; declared above).** Take the finite class Π_fin (below). Decide whether the prepare-measure fragment F1
admits a preparation- and measurement-noncontextual model. If it does not, decide which supplied completion restores
one: R-G (the `g` read), R-U′ (the carrier decorrelated, `g`'s law kept), R-Y (the carrier's `g`-completion) or R-S (the switch-supply
completion), each reported separately. R-Uc (decorrelation keeping the joint law of `g` and `η`) is reported beside them, and defines
`g_specific` and `g_eta`. Report the access fields L1 and EXP, and the counterfactual diagnostic INT.
R-U′ replaces r2's R-U, which changed `g`'s law in `g`-biased branches.

**Conditions (a)–(c) of the audit, as measured fields** (`ACCESS.md` §6):
- **(a)** is L1, the audit's notion and the reference, with EXP (read-record dependence, correlational) beside it.
  The paper analysis predicts both in F1 from P★'s published law, and the round measures them (R14-Rb2).
- **(b)** is a degenerate pairing (`d < r_S` or `d < r_E`). By Lemma NC-F it follows from (c).
  - The paper analysis predicts the weaker non-spanning form ¬X1 in F1 (`r_S ≤ 6 < 16`), and the round measures
    `r_S`. Spanning implies nondegeneracy, not conversely.
  - `cert_X3`, whether some read equals `g` on `Ω_reach`, is reported beside it.
- **(c)** is the exact infeasibility of F1's LP.
- **Consequence (predicted).** If (a) holds in F1, as the paper analysis predicts, the conjunction there reduces to
  (c). The round's discriminating content is then the attribution, and the per-herald-block location of the
  conjunction (R14a-N4).

**The model (frozen).**
- **Rule and sizes.** `G_SM`: `f_i(u) = u_{i−1} ⊕ u_{i+1} ⊕ u_{i+2} ⊕ u_{i+1}u_{i+2}`, `(u, v) ↦ (f(u) ⊕ v, u)` on
  `Z_L` over `F_2`, with `L ∈ {25, 29}`.
- **Mechanism off** (CC-OFF only): class N, `f_i = u_{i−1} ⊕ u_{i+1}`.
- **Supplies (P★'s mixed class, O-3).** Switch sites 1 and 2 have `u` unknown and `v = 0`. Every other site except
  the carrier is `(0, 0)`.
- **Carrier inputs (P2), at `t = 0`.** `Z±`: `u_0` known 0 or 1, `v_0` unknown. `X±`: `v_0` known, `u_0` unknown.
  There are three unknown bits per input, uniform and independent (A-N2).
- **Herald.** `h = u_{−1}(3)` (site −1, time 3), a non-terminal configuration record, as in P★.
- **`τ = 3`, the carrier and `η`.** The carrier is `(z, x) = (u_0(2), u_0(3))`, and `η` is every other slot at `τ`.
  `Ω_reach` is the set of reachable configurations at `τ`.
- **The functionals (O-1).** `g = z + x` (G-Y), decided. `g_1 = u_1(3) + u_1(2)` and `g_2 = u_2(3) + u_2(2)`, the
  switch cells' `Q* = 1` functionals at `τ` (G-H1), reported.
- **F1 preparations.** The conditional law at `τ` given input and herald, for each pair with positive probability:
  at most 8.
- **F1 reads.** One read per run of `u_s(t)`, for `s ∈ W = {−2, …, 3}` and `t ∈ {2, …, 7}`, with
  `u_s(2) ≡ v_s(3)`. That is 36 binary reads. They are non-disturbing configuration-function reads (P-c, or the
  H-PREP type), not SA-1(b) meter registrations.
  - `(−1, 3)` is the herald itself.
  - `(0, 2)` and `(0, 3)` are the T1 reads `z` and `x`.
- **Completions (supplied, test-only, each reported separately).**
  - **R-G** adds the read `g` at `τ`.
  - **R-U′, a `g`-law-preserving decorrelation.** For each branch `p` of input `Z+` (P★'s own input), the law
    `μ_p(η) ⊗ [P_p(g = 0)·U_{Y+} + P_p(g = 1)·U_{Y−}]`. The carrier is decorrelated from `η`, with `⟨Z⟩ = ⟨X⟩ = 0`
    and `g`'s law kept. `U_{Y+}` and `U_{Y−}` are the carrier laws uniform on `g = 0` and on `g = 1` (R14-Rb2).
  - **R-Uc, a `(g, η)`-law-preserving decorrelation** (re-review r3 B1). For each branch `p` of input `Z+`, the law
    `Σ_η μ_p(η) δ_η ⊗ [P_p(g = 0 | η)·U_{Y+} + P_p(g = 1 | η)·U_{Y−}]`. It keeps the joint law of `(g, η)` and
    decorrelates only the rest of the carrier. R-Uc is a reported field, not a token letter.
  - **R-Y.** For the same branches, the two laws `μ_p(η) ⊗ U_{Y±}`. These vary `g`'s law, marginal and conditional.
  - **Derived fields (reported; never change the token):**
    - **`g_specific := (F1+R-Y feasible) ∧ (F1+R-Uc infeasible)`**: the contextuality depends on `g`'s law, marginal
      or conditional on `η`. Keeping that law while decorrelating everything else does not restore, and varying it
      does.
    - **`g_eta := (F1+R-U′ feasible) ∧ (F1+R-Uc infeasible)`**: it depends on `g`'s correlation with `η`.
    - Fixture Q (`g`'s law fixed conditionally on `η`, marginally uniform) gives both true. Under r3's definition it
      gave the misleading negative the owner excluded (c.6724832474).
  - **R-S.** P★'s input `Z+` with the switch cells supplied as a pair in `Z±` × `Z±` (`u` known, `v` unknown): 4
    patterns × herald.
    - Each switch's `v` then becomes uniform, which adds hidden bits and configurations. F1+R-S is completed on a
      larger `Ω` than F1's `Ω_reach`, so a restoration by R-S is not a completion of F1's `Ω_reach`.
    - Mixed patterns (`X+` with `Z±`) and other carrier inputs are not included.
    - Whether F1+R-S is in scope is decided before `F` (precondition 2).

  Reads are evaluated on every configuration these laws charge, including configurations outside `Ω_reach`.
- **F0 (CC-F0).** The carrier laws P★0 and P★1 from input `Z+`, and the mechanism-off branches, with reads `z` and
  `x`.

**Measured quantities (exact; at both sizes).**
- **The table and ranks.**
  - `N(p, e) = Pr(read e = 0 | p)` as a `Fraction`.
  - `d = rank N`; `r_S` and `r_E` are the ranks of the laws and responses on the configurations charged.
- **L1(f)**, for `f ∈ {g, g_1, g_2}`. The witness is the first branch, in input order `Z+ < Z− < X+ < X−` and then by
  herald, where `f` is determined or its conditional law is non-uniform.
- **EXP(f), read-record dependence (correlational).** The witness is the first `(p, e)`, with reads ordered by
  `(t, s)`, such that
  `P_p(e = 0, f = 0) ≠ P_p(e = 0)·P_p(f = 0)`. It is computed on the charged laws only.
- **INT (counterfactual diagnostic; decides nothing; for `g` only).** The number of reads with `ξ̂_e(y | η) ≠ 0` for
  some `η` in `Ω_reach`, where `ξ̂_e(y | η) = ¼ Σ_{z,x} [e = 0 | carrier set to (z, x), η fixed] (−1)^{z+x}`. INT is
  not defined for `g_1` and `g_2`.
- **`cert_X3(f)`.** Some F1 read equals `f` or `1 ⊕ f` on `Ω_reach`.
- **LP verdicts.** For F1, F1+R-G, F1+R-U′, F1+R-Uc, F1+R-Y, F1+R-S (if in scope) and F0. Each records the rank its
  completion adds and the method step that decided it.
- **Per herald block, for `h ∈ {0, 1}`.** The verdict of F1 restricted to the herald-`h` preparations (all reads).
  Also, whether *any* branch of that block has L1(g), and whether *any* has EXP(g) (re-review N7).

## The exact method

**The accessible GPT.**
- **The effects (R13-N4).** A fragment's effect set is both outcomes of every binary read, `[e = 0]` and `[e = 1]`,
  and the unit effect `u`: 73 effects for F1's 36 reads. Every effect's complement `u − e` is therefore in the set,
  which step 4's zero-`κ_j` drop and the bound `ξ ≤ 1` use.
- Factor `N = A Bᵀ` by exact elimination: rows `a_p ∈ Q^d` and `b_e ∈ Q^d`, with the unit effect included.
- Operational equivalences are the linear relations among the rows. They are certified by the fragment's own reads
  and preparations and by nothing else.

**The decision procedure (frozen).** Each fragment is decided by the first step below that returns a verified
certificate. Every outcome carries a certificate, which the independent verifier checks against the definition.

1. **Effect reduction.** Remove every effect vector that duplicates, or is a positive multiple of, an earlier one in
   the frozen order. The unit effect is kept, and non-extreme effects are not pruned.
1b. **Extreme-ray reduction (R14-Rb1; Q-C2-1's D19 (0)(c), its C.8 item 15).** It runs only when the fragment's listed
   rows exceed a cap on `n` (more than 16 of them, or `C(n, d − 1) > 10^5` with `n` their number); otherwise every
   listed row is retained.
   - The rows `a_p` are taken in the frozen preparation order. A row is removed when it is a nonnegative combination
     of the rows still retained other than itself. That is decided by a phase-1 simplex on `Σ_q λ_q a_q = a_p`,
     `λ ≥ 0`, with step 5's rules, drawing on the fragment's budget (step 6). A feasible solution is the removal
     certificate `(p, {q: λ_q})`.
   - Every row satisfies `b_u · a_p = 1`, so `cone{a_p}` is pointed, and the retained rows are one row for each
     extreme ray. They generate the same cone, so its facets are unchanged.
   - The retained rows serve only the caps on `n` and `C(n, d − 1)` and the facet enumeration, in the solver and in
     the verifier. Steps 2–4 and every model check use all listed rows, so a model covers every preparation.
   - C-SYM applies this step with the roles of `a_p` and `b_e` exchanged (*The controls*).
2. **Rank fast path (Lemma NC-F).** On the charged configurations `Ω_c`, compute `d`, `r_S` and `r_E` exactly. If
   `d = r_S = r_E`, the fragment is **feasible**, and the certificate is the configuration model: the charged laws
   `μ_p` and the response functions `ξ_e`.
   - **Lemma NC-F** (stated here with its proof; R13-N24). Take a finite `Ω`, laws `μ_p` on `Ω` and responses
     `ξ_e: Ω → [0, 1]` whose outcomes sum to 1, and let `P = span{μ_p}` and `R = span{ξ_e}`. If `d = r_S = r_E`,
     equivalently `P ∩ R^⊥ = 0` and `R ∩ P^⊥ = 0`, the configuration model is preparation- and
     measurement-noncontextual. *Proof.* An operational equivalence `Σ_p c_p N(p, ·) = 0` puts `Σ_p c_p μ_p` in
     `P ∩ R^⊥ = 0`, so the laws themselves satisfy it; the same argument applies to effects. ∎
   - The lemma is one-directional: F10 is degenerate (`d = 2 < r_S = 4`) and feasible.
3. **Sufficient test** (applicable only when `r_S = d`). Look for a linear `K: Q^d → Q^{Ω_c}` with `K b_e ≥ 0`,
   `K b_u = 1` and `μ_pᵀ K b_e = N(p, e)`.
   - It is solved by the same phase-1 simplex and pivot rules as step 4, drawing on the same budget.
   - A solution is an explicit model.
   - Infeasibility, or inapplicability, implies nothing, and the procedure goes on to step 4.
4. **Reduced state-facet LP**, with orientation fixed.
   - Let `{g_j}` (`m` of them) be the facets of `cone{a_p}`. A noncontextual model regroups as `Σ_j g_j κ_jᵀ = I_d`,
     with `κ_j · b_e ≥ 0`.
   - Solve the equality exactly: `κ = κ_0 + N t`, with `t ∈ Q^T` and `T = (m − d)·d`.
   - Decide `{t : (κ_0 + N t)_j · b_e ≥ 0 for all j, e}` through its Farkas alternative. That is a phase-1 simplex
     with `T + 1` equality rows and `m·E` nonnegative columns.
   - **Farkas system feasible.** Its multipliers `y_{je} ≥ 0` define `W` with `W g_j = Σ_e y_{je} b_e` and
     `tr W < 0`. The fragment is **infeasible**. Soundness: `tr W = Σ_{λ,j} c_{λj} κ_λ · (W g_j) ≥ 0` for any model,
     a contradiction.
   - **Farkas system infeasible.** Its phase-1 dual gives `t`, hence `κ`, hence an explicit model. The fragment is
     **feasible**. Drop each `j` with `s_j := κ_j · b_u = 0` (each such `κ_j` is zero, because complements are present),
     and set `μ_p(j) = (g_j · a_p) s_j` and `ξ_e(j) = (κ_j · b_e)/s_j`.
   - **Completeness (R13-N24).** By Farkas' lemma exactly one of the system on `t` and its Farkas system is
     feasible, so one of the two certificates always exists; the soundness of each is shown above. The infeasibility
     certificate's soundness needs the complete facet list, which the verifier re-derives (M-FACET).
5. **Arithmetic and pivoting (frozen tie-breaks; re-review N6).**
   - The tableau is fraction-free: integer rows with a common denominator, and exact integer (Bareiss) pivot updates.
   - **Entering column:** Dantzig's rule, the most negative reduced cost, with ties going to the lowest column index.
   - **Leaving row:** the minimum ratio, with ties going to the lowest basic-variable index.
   - **Anti-cycling:** after 50 consecutive degenerate pivots, Bland's rule applies for the rest of that phase, with
     no return to Dantzig's rule.
   - Pivoting affects speed only. Soundness rests on the verified certificates.
6. **Deterministic budget (re-review B3).** Each fragment, across steps 1b, 3 and 4 and all phases (R14-Rb1), has
   three budgets:
   - a pivot budget `P_max`;
   - a bit budget `B_max`, on the bit length of any tableau entry;
   - a work budget `W_max`, on the cumulative bit length of all entries updated. This is a deterministic proxy for
     tableau work. Facet enumeration, rank computations and the verifier are not counted; their cost enters the
     timeout test through measured seconds (r4 N5).

   Exceeding any of the three gives **`out_of_scope`**: the fragment is recorded as such, the checker exits 3, and the
   round is VOID. The checker does not crash. No wall clock enters a result, so the replay at `E` is exact.
   - **Mechanical freeze rule** (applied once, before `F`):
     - `P_max := 3 × (maximum pivots)`;
     - `B_max := 3 × (maximum bit length)`;
     - `W_max := 3 × (maximum work)`.

     Each maximum is taken over **every non-F1 fragment** that the design run decides (re-review r4 B2(a)):
     - the stress fixtures kept in scope: SF-1 to SF-3, or SF-1 to SF-2 if R-S is out of scope, or SF-1, SF-2 and
       SF-3n if R-S is narrowed;
     - every frozen fixture and each of its completions, with C-SYM's effect-facet decisions on them (R13-N10);
     - CC-F0;
     - the self-tests, which reuse the fixture decisions; their mutations act on certificates, not on the solver,
       except M-BUDGET, which sets its own budgets.

     All of these are read from the structured `stress.json` of the design run (schema v2, below). The values, and
     the pinned sha256 of `stress.json`, are entered under precondition 6. The fixtures are not exempt from the
     budgets.
   - **The timeout test** (mechanical; applied once, before `F`). `σ` is the design run's stress-step seconds per
     unit of work, defined exactly (re-review r5 N2):
     - `σ := t_5 / (W_stress + W_fix)`, an exact `Fraction`. `t_5` is the integer number of seconds of step 5, from its
       step record's start and completion times in the jobs API. Step 5 decides the stress fixtures *and* the frozen
       fixtures with CC-F0, so its work is `W_stress + W_fix`.
     - `t_810` is the integer number of seconds of A8 and A9 (the two self-tests), from the same records. B6 (replay,
       a canonical-JSON comparison) has no design-run record and counts 0 (r11 N6).
     - The test is `σ × (14·W_max + 2·W_fix + W_stress) + t_810 ≤ 1200`, evaluated exactly. 1200 s is ⅓ of
       `timeout-minutes: 60`. `W_fix` appears twice because the fixtures are decided in A3 (and in B4) and again in
       A5. The left side bounds each job separately:
       - job B's work, B4 and B6, is at most `σ × (14·W_max + W_fix) + t_B6`;
       - job A's work, A3 to A9, is at most `σ × (2·W_fix + W_stress) + t_A8 + t_A9`;
       - each bound is at most the left side, and each job has its own 60-minute limit. The sum of the two bounds,
         `σ × (14·W_max + 3·W_fix + W_stress) + t_810`, is not what the test bounds (R13-N8).
     - `check --freeze` evaluates the inequality from the pinned inputs and fails if it does not hold.
     - The 14 terms are 7 fragments (F1, R-G, R-U′, R-Uc, R-Y, R-S, F0) × 2 sizes. With R-S out of scope there are
       12.
     - `W_fix` is the fixtures' total work (with CC-F0 and C-SYM's decisions), and `W_stress` the stress fixtures'
       total work. Both come from the design run's `stress.json`.
     - `σ` absorbs the uncounted operations of the stress step (facets, ranks, verifier) proportionally. It is an
       estimate, not a bound. A timeout remains a checker outcome: VOID, with no retake.
     - **The enumerations, C-SYM's included (R14-Rb1).** Every facet enumeration visits at most `10^5`
       `(d − 1)`-subsets, in the solver and again in the verifier: the preparation side's by the cap on
       `C(n, d − 1)`, and C-SYM's effect side by its own cap (*The controls*). A5 performs every C-SYM decision that
       A3 and B4 perform, so their enumerations are part of `t_5`, σ attributes them to `W_fix`, and the left side
       counts `W_fix` again for A3 and, in job B's bound, for B4.
     - **Not counted (R13-N14).** In decisive mode the work outside steps 3 and 4 is in neither `W_max` nor the test:
       building the F1 family, the access fields, INT, IS-SIZE and C-EVAL. So are job A's A3b and A11, which are
       reads and comparisons. Its size is fixed by the frozen lists: inputs with three unknown bits each (A-N2), at
       most 16 preparations, 37 reads and horizon 7, at two ring sizes. It is small beside the LP but is not measured
       before `F`, since F1 is not built; a timeout from it is a checker outcome.
     - If the test fails with R-S kept, the R-S decision of precondition 2 is taken before `F`. If it fails without
       R-S, no `F` is requested.
   - **The job timeout is frozen.** `timeout-minutes: 60` on each of the jobs `probes_arp3qc22` and
     `probes_arp3qc22_decisive` (*The workflow edit*). Job B's limit counts from its start, after the approval.

**The independent verifier (re-review B2).** It is a separate function namespace in `qc22_check.py`: every function
whose name begins `v_`. C-INDEP checks it mechanically.
- **Its inputs** are only these:
  - the fragment's charged laws `μ_p`;
  - the read response tables `ξ_e`, as produced by the fragment builder (C-EVAL-checked), not by the solver;
  - the solver's reported `A`, `B` and certificate.
- **It re-derives the table from the definition.** It computes `N(p, e) = Σ_ω μ_p(ω) ξ_e(ω)` itself, checks
  `A Bᵀ = N` exactly, and checks `rank A = rank B = rank N = d` with its own elimination. A wrong factorization fails
  here.
- **Its own facet list.** It first checks step 1b's removal certificates, if any, in their removal order, each
  exactly: `λ ≥ 0`, `Σ_q λ_q a_q = a_p`, and every `q` a row other than `p` not removed before it. By induction every
  removed row lies in the cone of the retained rows. A failed check makes the fragment `undecided` (R14-Rb1). It then
  re-enumerates the facets of `cone{a_p}` by its own brute force over `(d − 1)`-subsets of the retained rows.
  It checks that each listed facet is supporting, with `d − 1` independent tight generators, and that the solver's
  list equals its own as normalized primitive integer normals.
- **Infeasibility.** It checks `W` and nonnegative `y` with `W g_j = Σ_e y_{je} b_e`, and `tr W < 0`, against its own
  list.
- **Feasibility.** It checks every model (steps 2–4) by definition: nonnegativity, normalization, `0 ≤ ξ ≤ 1`, exact
  reproduction of its own `N`, and linearity in `a` and `b`, by solving exactly for the linear maps and checking them
  on every `p` and `e`.
- **Neither verifies.** The fragment is `undecided`, and the round is VOID.

**Caps (frozen).** A fragment over a cap is `out_of_scope`, and the round is VOID.
- At most 16 preparation generators.
- `d ≤ 16`.
- `C(n, d − 1) ≤ 10^5`.
- At most 200 effects before reduction.

**How the caps count (R13-N5; R14-Rb1; Q-C2-1's D19 (0)(c)).** "Preparation generators" are the extreme rays of
`cone{a_p}`, and `n` in `C(n, d − 1)` is their number. "Effects before reduction" are the fragment's effects (*The
accessible GPT*) that have positive probability under some preparation, with the unit effect.
- **How they are checked.** The cap on effects and `d ≤ 16` are checked on the listed effects (two outcomes per listed
  read, plus the unit), before step 1. The caps on `n` and `C(n, d − 1)` are checked on the listed rows, and, only when
  the listed rows exceed one of them, on the rows step 1b retains. Each count used is at least the quantity it bounds,
  so a fragment within a cap as checked is within it as counted.
- The raised caps Q-C2-1 sets for its fragment B-P are its own and are not used here.

**Every frozen fragment is within the caps as checked (R14-Rb1).**
- **F1's family** lists at most 16 preparations (F1 at most 8; F1+R-U′ and F1+R-Uc at most 10; F1+R-Y at most 12;
  F1+R-S at most 16) and at most 37 reads, so at most 75 effects. F0 lists at most 6 preparations (P★'s two branches
  and the mechanism-off `Z±`, each with at most two herald values), with two reads.
- **The stress fixtures** list 8 (SF-1), 12 (SF-2) and 16 (SF-3) preparations, with 36 reads.
- **The frozen fixtures** list at most 8 base preparations each (H3 and GX 8, NEG-1 6, ZPT 2, every other 4). Their
  reads are point reads on at most 12 configurations (GX), with R-G's `g` read, or at most seven reads (SW and SW−
  with R-G), so they have at most 27 effects. Under their frozen construction (*The controls*) a completion adds at
  most one law per base preparation (R-U′, R-Uc) or two (R-Y); H3's come from block B's four preparations, and SW's
  R-S adds the switch's two `Y±` laws. So every completed fixture lists at most 16 preparations, apart from GX+R-Y.
- With at most 16 rows, `d ≤ 16` and `C(n, d − 1) ≤ C(16, 8) = 12,870`.
- **GX+R-Y** lists 18 preparations: GX's 8; two R-Y laws from G's sector, `δ_2 ⊗ U_{Y±}`; and eight from X's sector,
  `μ ⊗ U_{Y±}` for each of the `η`-marginals `μ = (¾, ¼)`, `(1, 0)`, `(0, 1)` and `(¼, ¾)` of X's four laws. Its
  `d ≤ 12`, the number of its configurations. Its reads are point reads, so each row determines its law.
  - The four laws with `μ = (¾, ¼)` or `(¼, ¾)` are `¾·(δ_0 ⊗ U_{Y±}) + ¼·(δ_1 ⊗ U_{Y±})` and
    `¼·(δ_0 ⊗ U_{Y±}) + ¾·(δ_1 ⊗ U_{Y±})`, nonnegative combinations of two listed laws.
  - Those two are extreme, since no other listed law is supported inside their support, so step 1b never removes
    them, and it removes each of the four at its turn, with its certificate.
  - Hence `n ≤ 14` and `C(n, d − 1) ≤ C(14, 7) = 3,432`.
- **C-SYM's effect side** has its own cap, `C(E, d − 1) ≤ 10^5` (*The controls*).
  - In the fixtures whose reads are point reads on all their configurations (NEG-2, DUAL, ZPT, G, H3, X, Q and GX,
    with their completions), every complement, the unit and both outcomes of R-G's `g` read are sums of point
    effects. So when step 1b runs with the roles exchanged it leaves at most one effect row per configuration, at
    most 12, and `C(E, d − 1) ≤ C(12, 6) = 924`; when it does not run, the cap already holds.
  - POS-1, POS-2, NEG-1, GBIT and F10 have at most three reads (`Z`, `X`, `g`) on four configurations, so `E ≤ 7`
    and `d ≤ 4`. SW and SW− have at most seven reads: with R-G they keep four preparations, so `E ≤ 15` and
    `d ≤ 4`; otherwise `E ≤ 13`. So `C(E, d − 1) ≤ max(C(15, 3), C(13, 6)) = 1,716`.

No frozen fragment is therefore `out_of_scope` by a cap.

**Expected bounds on paper.**
- F1: `d ≤ 6`.
- F1+R-G: `≤ 6`, since an added read cannot raise `d` above `r_S ≤ 6` (R13-N20).
- F1+R-U′ and F1+R-Uc: `≤ 8`.
- F1+R-Y: `≤ 10`.
- F1+R-S: at most 16 generators, on a larger `Ω`.

**Stress fixtures (frozen, synthetic, not `G_SM`).** These are classical fragments with F1's preparation structure.
The generator is frozen in `qc22_check.py`: stdlib only, with a 32-bit xorshift whose seeds are part of the pinned
blob.
- **SF-1** (seeds 20261108, 1 and 2). `Ω = F_2⁴`. The four inputs are `Z±, X±` on bits 0–1, with bits 2–3 uniform.
  The herald is `h = (ω_0 ∧ ω_2) ⊕ ω_1 ⊕ ω_3`. That gives 8 conditional preparations and 36 seeded boolean reads.
  This is F1's size.
- **SF-2.** SF-1 with `Y±` inputs added: 12 preparations, F1+R-Y's size.
- **SF-3.** `Ω = F_2⁶`, 8 inputs × herald, giving 16 preparations, and 36 seeded reads. This is F1+R-S's size.
  Its eight inputs, its herald and every seeded read are fixed by the generator in the pinned blob, not by this text;
  stress fixtures carry no frozen verdict, so no decision rests on them (R13-N21).
- **SF-3n.** Defined only if R-S is narrowed before `F` (precondition 2).

**`--stress` and `stress.json` (§A.44).**
- `qc22_check.py --stress` decides every kept stress fixture, every frozen fixture with its completions and C-SYM's
  decisions on them, and CC-F0. It
  never builds the F1 family. It writes canonical-JSON `stress.json`, schema `arp3-qc22-stress` v2. For each
  fragment the schema records the verdict, the deciding step, the pivots, the maximum bits, the work and the
  certificate-verified flag. It also records the totals `W_fix` and `W_stress`. There is no timestamp. It is run with
  no budget, apart from the job timeout.
- The workflow runs it on every event and uploads `stress.json` as an artifact on every event. The design run's
  `stress.json` is the file inside that run's `arp3-qc22-stress` archive, retrieved by the executor (R14-N3).
- **The marker step** "ARP-3-QC22 stress output equals the pinned sha256" runs `controls.py stress-check`.
  - It exits 0 iff `stress.json` meets schema v2, every fragment in it is certificate-verified, and its sha256 equals
    the frozen pin.
  - On the design tree the last condition is replaced by recording (no pin exists yet). The schema and
    certificate conditions are still enforced there (r4 N6).
  - At S1 and `E` its conclusion is a step conclusion read by `verdict`.
- **The pin is bound by A7 in the confirmation run (R13-B2).** The artifacts API's `digest` is the sha256 of the
  uploaded zip archive, not of the file inside it (HF-1). `design-run.json` records it as provenance, and no condition
  compares it with a file's sha256. A7's `success` in the confirmation run (6′) binds the pin instead: there A7
  compares the sha256 of the `stress.json` that 6′'s own A5 wrote with the pin, so the pinned figures are those the
  exact S1 tree produces. `check --freeze` also requires the `stress.json` it is given to have the pinned sha256.

**Fixture mode and its exit semantics (frozen; re-review r4 B2(b), r6 B1).** Fixture mode is what A3 always runs, and
what B4 runs unless the event is a dispatch at its first attempt, the tree carries no receipt, and all three of the
checker's keys hold (*The workflow edit*). In it the checker builds no
F1-family fragment under `G_SM`, and prints the synthetic F1 placeholders of the measurement schema, with
`mode: "fixture"`. It decides every frozen
fixture, its completions and CC-F0 with the full method and the independent verifier.

**Fixture mode's exit rule (re-review r8 N1).** Fixture mode **exits 0** unless one of the three conditions below holds,
whatever `complete` says: fixture output always has `complete: false`, by the schema. The default exit rule
(0 when complete and green, 3 otherwise) applies in decisive mode only. Fixture mode **exits 3** when any of these
holds:
- a verdict, frozen deciding step, derived field or token differs from its frozen expectation;
- a certificate fails;
- a fragment is `out_of_scope` under the budgets in force.

Before the budgets exist, the design run uses no budget; the confirmation run uses the final budgets. A green step 3
in either run is therefore the writer's own computation of every frozen expectation: the base infeasibilities,
X+R-Y and GX's four completions included (the circularity noted in re-review r4 §1.4).

**F1+R-S scope: the owner's two options, kept (c.6724832474; precondition 2).**
- **(i) Out of scope.** If SF-3 is undecided, or the timeout test fails with R-S kept, F1+R-S may be declared
  `out_of_scope` by design before `F`. RS is then dropped from the token alphabet, and the frozen texts select the
  RS-dropped forms. This is the owner's stated preference.
- **(ii) Narrowed.** A narrower R-S may be proposed before `F` only as a revision of this file that states:
  - its scope;
  - its stress fixture SF-3n at the narrowed size;
  - its controls.

  The revision is independently reviewed under precondition 4 before `F`.
- **(iii) After `F`** neither is available. No narrowing, no change to `P_max`, `B_max`, `W_max`, the caps or
  `timeout-minutes`, and no re-run with another budget is admissible. These are control-plane values; any change is
  a control-plane change after `F`, and the round halts (*Stop rule*). An undecided fragment receives the
  preregistered VOID.

**Not adopted (named only).** A floating-point solver could propose a basis, from which exact rational reconstruction
gives a certificate that is then verified. It conflicts with C-EXACT and the no-package workflow, and would need a
recorded owner decision.

**Arithmetic.** Integers and `Fraction` only, with no floating point (C-EXACT). The procedure decides preparation and
measurement noncontextuality of a prepare-measure fragment, not transformation noncontextuality.

## The controls

Each control is evaluated in the decisive run, at both sizes where it depends on size. `decide` recomputes every flag
from the raw fields.

**The fixtures' objects (frozen; R14-Rb1, Rb2).**
- Unless its row adds `η` or a switch cell, a fixture lives on the carrier's four configurations `(z, x)`, with no `η`.
- A carrier law with moments `(⟨Z⟩, ⟨X⟩, ⟨Y⟩)` is `μ(z, x) = ¼(1 + ⟨Z⟩(−1)^z + ⟨X⟩(−1)^x + ⟨Y⟩(−1)^{z+x})`, so
  `⟨Y⟩` is the bias of `g`. `Z±`, `X±` and `Y±` are the laws with that moment `±1` and the other two 0; `Y±` are
  `U_{Y±}`. The `Z` and `X` reads are `z` and `x`, and point laws and point reads are on the fixture's configurations.
- **Completions.** A fixture's R-U′, R-Uc and R-Y are built by F1's formulas (*The model*) from each of its
  preparations `p`, in its preparation order, with `η` the fixture's coordinates other than `(z, x)`, and with a law
  equal to one already listed listed once. H3's are built from block B's preparations only, and SW's act on its
  carrier. R-G adds the read `g`.

| code | what | green when | route to failure |
| --- | --- | --- | --- |
| **POS-1** | rectangle laws: Bloch `(±3/5, ±4/5)` with `⟨Y⟩ = ±2/5` (product sign), nonnegative; `Z`, `X` reads; **through the same `N`-factor path** | infeasible, `W` verified | an LP that cannot report contextuality; known bound: score `17/10 > 3/2`, two-bit parity-oblivious multiplexing |
| **POS-2** | `(±1/2, ±1/2)`, `⟨Y⟩ = 0` | feasible, model verified | spurious infeasibility on the diamond's boundary |
| **NEG-1** | the octahedron (`Z±, X±, Y±` as uniform laws on pairs), with `Z`, `X` and `g` reads | feasible | spurious infeasibility; Spekkens' toy bit |
| **NEG-2** | point laws, point reads | feasible | spurious infeasibility on a simplex |
| **GBIT** | point laws, `Z`/`X` reads; completions R-G, R-U′, R-Uc, R-Y | infeasible (step 4); restored by R-G only (each R-U′, R-Uc and R-Y law lies in the convex hull of the point laws); `decide` gives `CONTEXTUAL-RG` | restricted reads not attributed |
| **DUAL** | `Z±, X±`, point reads; completions R-G, R-U′, R-Uc, R-Y | infeasible (step 4); restored by R-Y only (R-U′ = R-Uc = `U`, inside the hull); `g_specific` true, `g_eta` false; `decide` gives `CONTEXTUAL-RY` | restricted preparations not attributed |
| **H3** | `(z, x, η)`, `η` one bit. Block A (`η = 0`): the four point laws on `(z, x)`. Block B (`η = 1`), the rectangle: `(¾, ¼, 0, 0)`, `(¾, 0, ¼, 0)`, `(0, ¼, 0, ¾)` and `(0, 0, ¼, ¾)` in the order `(z, x) = 00, 01, 10, 11`. Point reads on all 8 configurations; completions from block B (R14-Rb2) | infeasible (step 4); R-Y restores; R-U′ = R-Uc (one `η` per preparation; block B's centroid `(3/8, 1/8, 1/8, 3/8)`) and R-G do not; `g_specific` true, `g_eta` false; block A feasible and block B infeasible; L1(g) in some branch of both blocks; `decide` gives `CONTEXTUAL-RY` | `g`-fixed-law contextuality misattributed |
| **G** (re-review r3, O-1) | H3's block B alone: the rectangle of carrier laws at fixed `P(g = 0) = ¾`, `η = 1`; point reads on H3's eight configurations `(z, x, η)` (R14a §4) | infeasible; R-U′ and R-Uc infeasible (both are the centroid); R-Y feasible; `g_specific` true, `g_eta` false; `decide` gives `CONTEXTUAL-RY` | a `g`-specific cause reported as not specific |
| **X** (O-1) | the same rectangle on `(x, η)`, in the order `(x, η) = 00, 01, 10, 11` (fixed `P(x ⊕ η = 0) = ¾`), `z` uniform and independent, so `P(g = 0) = ½` everywhere; point reads on 8 points | infeasible; R-U′ and R-Uc feasible; R-Y infeasible; `g_specific` false, `g_eta` false; `decide` gives `CONTEXTUAL-RUP` | a cause that is not `g` reported as `g`-specific |
| **Q** (O-1; the r3 counterexample) | each preparation `½·(block-B law ⊗ δ_{η=1}) + ½·(its x-flip ⊗ δ_{η=0})`: `g` marginally uniform, `P(g = 0 \| η = 1) = ¾`; point reads | infeasible; R-U′ feasible; R-Uc infeasible (the centroid); R-Y feasible; `g_specific` true, `g_eta` true; `decide` gives `CONTEXTUAL-RUP+RY` | the misleading negative the owner excluded (c.6724832474) |
| **GX** (two causes; re-review r4 B1) | G's sector at `η = 2` (fixed `g` law) beside X's sector at `η ∈ {0, 1}` (fixed `x ⊕ η` correlation); point reads on all 12 points | infeasible; R-U′, R-Uc and R-Y all infeasible (R-Y by restriction to X's sector, reviewer r4 §1.3: X's sector with its R-Y laws charges only `η ∈ {0, 1}` and G's only `η = 2`, and the reads are point reads with their complements and the unit, so every relation among X's sector's preparations, or among its effects with the unit written as the sum of its point reads, also holds in GX+R-Y, and a noncontextual model of GX+R-Y restricted to the configurations X's sector charges would be one of X+R-Y, which is infeasible (R13-N19; R14-Rb2); computed by the writer's code before `F`, precondition 6′); R-G does not restore; `g_specific` "no" and `g_eta` "no", each with its frozen caveat; `decide` gives `CONTEXTUAL-NONE` | a "no" rendered as independence from `g`'s law, or the NONE addendum asserting where the degeneracy lies |
| **SW** (two cells) | carrier fixed at `(0, 0)`; the switch cell in the dual-gbit configuration (`Z±, X±` on the switch, point reads on the switch, `z` and `x` reads on the carrier); completions R-G, R-U′, R-Uc and R-Y on the carrier, and R-S (switch `Y±`) | infeasible; restored by R-S only; `decide` gives `CONTEXTUAL-RS` | the RS token path. SW's R-S (switch `Y±`) is not F1's R-S (`Z±` × `Z±` on an `X+`-type switch). SW checks the decision path and bookkeeping only (re-review N4) |
| **SW−** | SW with R-S withheld | infeasible; no completion restores; `decide` gives `CONTEXTUAL-NONE`, with the RS-in-scope addendum | `NONE` unreachable |
| **F10** (step 4 feasible; re-review B2(e)) | four point laws, `Z` read only: `d = 2 < r_S = 4` | feasible, decided by step 4's feasible branch (steps 2 and 3 inapplicable); model verified | step 4's model construction untested |
| **ZPT** (step 3) | `Z±` with point reads: `r_S = d = 2 < r_E = 4` | feasible, decided by step 3 (a model `K` exists: `ξ = α[z = 0] + β[z = 1]`); model verified | step 3 untested |
| **X+RU′** | fixture X with R-U′ | feasible, decided by step 3 or 4 (`r_S = d = 4 < r_E = 8`); the deciding step is recorded; model verified | a degenerate feasible path untested on a fragment with a hidden `η` |
| **CC-F0** (paper-predicted) | F0 at both sizes | feasible | a misread instance, or a checker error |
| **CC-OFF** | F1 rebuilt with class N | INT count 0; input `Z+` gives `Z±` branches | an evaluation error, or wrap-around. The prediction holds under class N, with no wrap within the window and horizon: each `u_i(t)` combines `τ`-slots of one type, and `z` and `x` differ in type. The ring (odd `L`) is not bipartite globally, so the prediction is local to the cone |
| **C-EVAL** (B6) | (i) for every site in `W`, every `t ∈ {4, …, 7}` and every charged configuration, the evaluator's `u_s(t)` equals an independent per-site computation from SM's `R`-rule (`x_{R(i,x)}` selection); (ii) on the fibre path, the R-G read gives `ξ̂(y \| η) = ½` at every `η`, and the T1 reads `z`, `x` give 0 | all hold | an always-zero or wrong evaluator; a zeroed fibre path |
| **IS-RULE** | `G_SM` against SM's `R`-rule: exhaustive over every configuration of `Z_L` for `L = 4, …, 7`; at `L = 25` and `29`, on every configuration the run evaluates under `G_SM` at that size, at each step up to `t = 7` (P★'s, for IS-PSTAR, and in decisive mode every configuration an F1-family law charges) (R13-N12); exactly two rules defined, `G_SM` and N; no `G_σ` | holds | a wrong rule or a template rule |
| **IS-PSTAR** | P★ at `L = 9, 12, 13` and at both sizes | M2D's table exactly | the instance is not P★ |
| **IS-SIZE** (N4) | every read value, the herald and every fibre evaluation, as functions of (input, unknowns), agree at `L = 25` and `29` | `disagreements = 0` | wrap-around within the horizon |
| **C-CERT** | every verdict certificate-verified by the independent verifier, which re-derives `N`, checks `A Bᵀ = N` and the ranks, checks step 1b's removals, and re-enumerates the facets over the retained rows; for every step (2, 3, 4) that decided | `unverified = 0` | a solver result taken on trust, a wrong factorization, an incomplete facet list, or a removal taken on trust (R14-Rb1) |
| **C-INDEP** (re-review B2; r4 N2; c.6724832474) | An AST check on `qc22_check.py` (rules below). The driver serializes the solver's output (`A`, `B`, step 1b's removal certificates, the facet list, the certificate) to canonical JSON, whose sha256 is `cert_sha256`. The verifier receives that byte string, the charged laws and the read tables, and calls `json.loads` on it itself. So the certificate and the solver's facet list reach it only as plain data, never as solver objects. **Rules:** inside every `v_*` function, calls may target only (i) other `v_*` functions, (ii) `Fraction`, `json.loads` and `itertools.combinations`, (iii) the builtins `len`, `range`, `sum`, `min`, `max`, `abs`, `sorted`, `enumerate`, `zip`, `all`, `any`, `int`, `tuple`, `list`, `dict`, `isinstance`, and (iv) attribute calls on local variables (for example `.append`). `globals`, `locals`, `vars`, `getattr`, `setattr`, `eval`, `exec`, `compile` and `__import__` are forbidden. Every other module-level name referenced must be a `v_*` function or a whitelisted name. **Coverage (r5 N4):** the rules apply to the entire `FunctionDef`: its body, default argument values, decorators, and every nested function and lambda in it. **Runtime types:** the verifier's non-JSON inputs, the charged laws and the read tables, are checked on entry to be built only from plain `dict`, `list`, `tuple`, `Fraction` and `int`, recursively; anything else is `unverified` | holds | a verifier that reuses solver code or solver-internal state, by direct call or by alias |
| **C-STATELESS** (re-review r5 N1(d)) | at `E`, the `fixtures` section of S1's committed `measurements.json`, in canonical JSON (verdicts, deciding steps, derived fields, tokens, pivots, bits, work), is byte-equal to that of `evidence/confirmation-measurements.json`. S1 decides F1 too, while 6′ does not, so equality shows that the F1 computation did not perturb any fixture decision | byte-equal; evaluated by `controls.py check --stage E`; a mismatch is a failed check at `E`, so the round halts with VOID (r6 N1) | cross-fragment solver state, or nondeterminism |
| **C-BUDGET** | in the decisive run, every fragment decided within `P_max`, `B_max` and `W_max` (frozen at `F`); a fragment over budget is recorded `out_of_scope` | holds; otherwise C-BUDGET is red, the checker exits 3, and `decide` gives VOID | an over-budget fragment given a token, or a crash. M-BUDGET exercises the path. A wall-clock timeout is not prevented by the budget, only made unlikely by the timeout test, and is a checker outcome (*Stop rule*) |
| **C-NCF** | every nondegenerate fragment (`d = r_S = r_E`) is decided feasible by step 2 and its certificate verifies; on the fixtures, step 4 is also run where steps 2 or 3 decide, and must agree, with its own certificate verified (r4 N4) | holds | a rank, fast-path or LP error |
| **C-SYM** | on the fixtures, the effect-facet LP gives the same verdict. **The effect-facet LP** (R13-N10) is step 4 with the roles of `a_p` and `b_e` exchanged: `{h_k}` are the facets of `cone{b_e}` (the effect set of *The accessible GPT*, unit included), and it decides `Σ_k h_k κ′_kᵀ = I_d` with `κ′_k · a_p ≥ 0` by the same Farkas route, step 5's rules and step 6's budgets. A noncontextual model regroups on the effect side as step 4's does on the preparation side, so the two verdicts agree on every fragment whose effect set holds the complements and the unit. The verifier checks its certificates with the roles exchanged: for infeasibility, `W` and `y ≥ 0` with `W h_k = Σ_p y_{kp} a_p` and `tr W < 0`; for feasibility, the model `μ_p(k) = (κ′_k · a_p)(h_k · b_u)`, `ξ_e(k) = (h_k · b_e)/(h_k · b_u)`, by definition. The verifier re-enumerates the facets of `cone{b_e}` by its own brute force over `(d − 1)`-subsets of the retained effects (R14 §3). Each C-SYM decision counts as a fragment decision for the budgets: its counters enter the freeze rule's maxima, and its work is part of `W_fix`. **Its enumeration's cap (R14-Rb1).** The caps of *The exact method* apply to the fixture as counted there. C-SYM's effect-side enumeration has its own cap, `C(E, d − 1) ≤ 10^5`, with `E` the effects after step 1. Above it, step 1b runs with the roles exchanged, removing each effect row that is a nonnegative combination of the retained ones, with its certificate, which the verifier checks in order, and `E` is then the number retained. A fixture still above the cap has C-SYM `out_of_scope` there. Every frozen fixture is within it (*Caps*) | `mismatches = 0`; every C-SYM certificate, removals included, verified; no C-SYM `out_of_scope` | a formulation error, or an unbounded enumeration |
| **C-EXACT** | AST scan: no float literal, no `float` call, no `math` import, and `/` only inside the one `Fraction` helper | no hit | floating point in a verdict |
| **C-ISO-NAME** | F1's lists are exactly the frozen ones; completion items occur only in their completion; completions are supersets; the lists' sha256 recorded | holds | a completion leaking into F1 |

**Self-tests** (never building F1 under `G_SM`):
- `decide` and the note generator are driven through every token and through VOID for each control flipped and for
  each malformed field;
- **M-FACET:** the solver's facet list with one facet dropped must fail C-CERT on POS-1, GBIT, DUAL and H3. These are
  fragments that step 4 decides (re-review B2(d));
- **M-W** (invalid by construction; r4 N3): `W ← −W`, and separately `W ← W + c·I` with
  `c = 1 − tr W / d`, so that `tr W = d > 0`. Each must fail C-CERT on GBIT, DUAL, POS-1 and H3;
- **M-MODEL** (invalid by construction): in a feasible certificate, add 1 to `ξ_e(j)` for the first pair `(e, j)` in
  frozen order with `μ_p(j) > 0` for some `p`. This changes `Σ_j μ_p(j) ξ_e(j)` and breaks exact reproduction. It must
  fail C-CERT on a step-2 certificate (NEG-2), on step-3 certificates (ZPT, X+RU′) and on step-4 certificates (F10 with
  `T = 0`, Q+RY with `T = 5`);
- **M-SOLVER:** a solver returning its verdict with no certificate, or with the other verdict's certificate, must give
  `unverified > 0` and VOID;
- **M-FACTOR** (invalid by construction): add 1 to `A[0][0]`. Row 0 of `A Bᵀ` then changes by the first row of
  `Bᵀ`, which is nonzero because `B` has full column rank. It must fail the verifier's `A Bᵀ = N` check;
- **M-RAY** (R14-Rb1; Q-C2-1's mutation of the same name; invalid by construction): in GX+R-Y's certificate, one
  removal multiplier altered; and, separately, an extreme row removed under a fabricated certificate (Q-C2-1
  r14b's wording; R14a-N6). Each must fail C-CERT. The same two mutations of C-SYM's effect-side removals on GX+R-Y,
  each with an extreme effect row, must each fail C-SYM's certificate check;
- **M-INDEP:** three variants must each fail C-INDEP (re-review r5 N4):
  - a `v_*` function edited to call a solver function directly;
  - a `v_*` function given a default argument bound to a solver function (`x=s_solve`);
  - a `v_*` function containing a nested function or lambda that closes over a solver function;
- **M-BUDGET:** with `P_max = 1`, and separately with `B_max = 1` and with `W_max = 1`, on a step-4 fixture (GBIT)
  and on a step-3 fixture (ZPT).
  - The checker must record `out_of_scope`, set C-BUDGET red and exit 3, and `decide` must give VOID, with no
    exception.
  - The recorded counters at the abort must not exceed the budget by more than one pivot's increment. That shows the
    check is inside the pivot loop (r4 N3);
- **mutation M-EVAL (B6):** an evaluator returning 0 must fail C-EVAL and IS-PSTAR, and zeroed fibre components must
  fail C-EVAL (ii);
- **mutation M-SWAP:** the carrier slots swapped must fail IS-PSTAR.
- **M-GUARD** (re-review r6 B1, r7 B2(a), r8 B1(c), r9 B2(g)). Each variant must fail, as stated.
  - **Checker keys.**
    - `--event pull_request`, `--event push` and A3's `--event fixture` (the last also with both event variables set
      to `workflow_dispatch` and `GITHUB_RUN_ATTEMPT=1`) must yield `mode: "fixture"` with placeholders only, and zero
      F1-builder calls (an instrumented counter).
    - A missing `--event` must exit 4.
    - **B4's argv (r11 N3).** The entry, driven with B4's exact argument forms
      (`--event closed-or-other --dispatch-sha <40 hex>`) and a synthetic dispatch, attempt-1 environment, must give
      `mode: "fixture"`, zero builder calls and `parameters.dispatch_sha` equal to the given value.
      - A `--dispatch-sha` that is not 40 lowercase hex must exit 4. `qc22_check.py` checks it itself, as length 40
        over `0123456789abcdef`, because `a_ok` lives in `controls.py`.
      - This self-test runs as A8 in the design run, in 6′ and in every later run.
      - **Residual.** The host's evaluation of B4's `${{ … }}` expression and its redirect are first exercised at
        S1. A fault there is a checker outcome: VOID, with no retake.
    - `s_mode` must return `"fixture"` for each single-key failure: `--event workflow_dispatch` with
      `GITHUB_EVENT_NAME=pull_request`; the converse; and both event keys with `GITHUB_RUN_ATTEMPT=2`. Each, run
      through the entry with the synthetic environment, must produce `mode: "fixture"` with zero builder calls.
    - The self-test checks only that `s_mode` returns `"decisive"` when all three keys hold; it never runs that case
      through the entry, which would build F1.
    - `t_builder_refuses` runs once, under A8's real environment, and must record the refusal (r10 B2). The refusal
      reads only the real `os.environ`, so the synthetic environments above are exercised through `s_mode` and the
      entry function `s_entry(argv, environ)`, never through the refusal (R13-N2).
  - **Workflow keys (control W).** A splice with any of these removed or altered must fail W:
    - the event key, the attempt key or the receipt key, from B4 or from B6;
    - any key of job B's `if:`;
    - job B's `environment:` line, or a different Environment name;
    - B3;
    - A3's literal `--event fixture`;
    - the marker A10;
    - the marker A3b, or its `if:` (R13-B2; R14-N10).
  - **`qc22_check.py` name rules (control B).** Each of these must fail B:
    - a second occurrence of `"workflow_dispatch"`;
    - an alias `b = <builder>` in a self-test function;
    - a second self-test function that references the builder (r10 B2);
    - `t_builder_refuses` with a statement other than the stated `try` form;
    - `globals()[...]`;
    - `getattr(...)`;
    - a `__*__` attribute walk;
    - a call to `set` or `frozenset`, a set display or a set comprehension (R13-N17).
  - **`controls.py` routes (control B).** Each of these must fail B. They are the r9 review's BYP-1 to BYP-12, plus
    the earlier variants:
    - **BYP-1:** `["git", "-c", "alias.q=!…", "q"]`;
    - **BYP-2:** `["gh", "api", ".../dispatches", "--input", "body.json"]`;
    - **BYP-3:** `["gh", "api", "--method=POST", …]` and `["gh", "api", "-XPOST", …]`;
    - **BYP-4:** `["gh", "api", "graphql", …]`;
    - **BYP-5:** `os.path.os.system(…)`;
    - **BYP-6:** `subprocess.os.system(…)` and `tempfile._os…`;
    - **BYP-7:** `sys.modules["os"]`;
    - **BYP-8:** `getattr(subprocess, "Po" + "pen")`;
    - **BYP-9:** `import subprocess as s`;
    - **BYP-10:** `from subprocess import Popen`;
    - **BYP-11:** `().__class__.__base__.__subclasses__()`;
    - **BYP-12:** a write-mode `open` of a `.pth` path, together with control T's argv lacking `-S`;
    - **BYP-13:** `p = subprocess.run; p(["sh", "-c", …])` (r10 B1);
    - **BYP-14:** `list(map(subprocess.run, [["sh", "-c", …]]))`;
    - **BYP-15:** `o = open; o("<site-packages>/z.pth", "w")`;
    - **BYP-16:** `subprocess.run(["git", "show", "--no-textconv", "--no-ext-diff", "-s", "main"], cwd=<a path>)`;
    - **BYP-17:** a `git show` list carrying `--ext-diff` or `--textconv` after the required `--no-…` flags;
    - **BYP-18:** an `a_ok(x)` element whose value is `--output=…`, as a validator call on a string with a leading `-`
      or a `=` (the self-test drives `a_ok` on it, which must raise), and an `a_ok(...)` element placed before
      `--end-of-options`;
    - `["gh", "api", "--method", "POST", ".../actions/runs/{id}/pending_deployments", …]`, and any template outside
      the frozen list;
    - **BYP-19:** `["git", "cat-file", "--filters", "--end-of-options", a_ok(…)]` (r11 N1);
    - **BYP-20:** `a_ok = str` followed by `a_ok("…")`; and the same for `w_path`;
    - **BYP-21:** `help(…)`;
    - **BYP-23 to BYP-26** (r12 N1): `(a_ok := str)`; `match x:` with `case a_ok:` (a capture); `except E as w_path:`;
      `class a_ok: …`. Each must fail B, and so must the same forms for `w_path` and the root check;
    - `w_path(td, name)` with a non-literal name, and `w_path(td, "a/b.pth")` with a `/` in it;
    - an `import qc22_check` with a call to its entry;
    - `subprocess.run` with a computed path, a run-time-built list or a variable first element;
    - `os.system(…)`;
    - `gh` with `-X POST`, and `gh workflow run`;
    - a `git` subcommand outside the frozen list;
    - **ZIP-1 to ZIP-3** (R13-B2; Q-C2-1 r14's variants): `zipfile.ZipFile(io.BytesIO(b), "w")`; an `extractall(…)`
      or `open(…)` call on a `ZipFile`; `zipfile.ZipFile(<a path>)`;
    - a `gh` path f-string with a formatted value that is not an `a_ok(...)` call (R13-N6).

- **M-MODE** (re-review r7 B2(b)): `decide` on a fixture-mode `measurements.json` must give VOID. It must do so
  independently on each of three conditions, testing each with the other two repaired: `mode` is not `"decisive"`;
  `complete` is `false`; an F1 `lp` field is `"placeholder"`.
- **REPLAY** (R13-B1). `replay`'s comparison, on synthetic byte strings in memory: a fresh output that differs from
  the committed file only in `parameters.dispatch_sha` must give 0; a changed token must give 3; the absent-file branch
  must print `{"replay":"not-applicable"}` and give 0.
- **S1-BIND** (R13-B2; Q-C2-1 r14's wording). `verdict`'s S1 binding, on synthetic records built in memory. An
  artifact list and an archive holding a `measurements.json` that differs from the committed file only in
  `parameters.dispatch_sha` must bind. Each of these must fail it: a changed token; a second member in the archive;
  a `digest` that differs from the archive's sha256; a `workflow_run.id` or `head_sha` of another run; no artifact
  (for an expired or deleted artifact, draft default, pending the owner's ruling in precondition 2; R14a §2);
  a fresh read whose `id`, `digest` or member list differs from the record in `evidence/s1-run/results.json`
  (R14-N6). No file is written.
- **APPROVALS** (R13-B4). `order` and `verdict` on synthetic records: an approval entry whose comment follows its
  run's `created_at`, whose `updated_at` follows it, whose author is not `amaybaum`, whose quoted words name another
  commit or stage, or whose comment is reused must each fail; so must an `F` designation comment that follows the
  first execution run. An entry of a host-VOID run with a rejected review and B3 not run must hold, and the same
  entry offered as the run that attests at its stage must fail. Two `E`-stage comment ids must give two built entries
  (R14-N2).
- **NOF1** (R14a-Rc1). The no-unapproved-F1 rule, in `order` and `verdict`, on synthetic non-dispatch attempt records
  with job B and B4 `skipped`: A3 absent, and A3 `skipped` with A3b `failure`, must each hold; A3 `failure` with A3b
  `success` must hold; A3 `failure`, `cancelled` or with no conclusion, each with A3b `failure`, must fail; A3
  `success` with A3b `failure` must fail; and B4 `success` must fail whatever A3 and A3b record.

## The decision rule (frozen; `controls.py decide`)

Inputs: `evidence/measurements.json`, read as structured data, and the checker's exit status.

1. **VOID** when any of these holds:
   - the exit status is not 0;
   - the file is missing, unparseable or off-schema;
   - `complete` is not `true`;
   - `mode` is not `"decisive"` (re-review r7 B2(b));
   - any F1-family `lp` field is not `"feasible"` or `"infeasible"` (a fixture-mode placeholder is `"placeholder"`);
   - any control is red;
   - any fragment is `undecided` or `out_of_scope`;
   - the two sizes give different verdicts on any fragment (N4);
   - the flags, or the derived fields `g_specific` and `g_eta` (which `decide` recomputes from the completion
     verdicts), disagree with `decide` (re-review r4 N1).
2. **Otherwise:**
   - **IMITABLE** when F1 is feasible;
   - **CONTEXTUAL-{S}** when F1 is infeasible. `{S}` is the set of completions whose fragment is feasible, written in
     the fixed order `RG`, `RUP` (R-U′), `RY`, `RS`, joined by `+`, or `NONE`. R-Uc is not a token letter. If F1+R-S
     is declared `out_of_scope` by design before `F` (precondition 2), `RS` is dropped from **F1's** token alphabet,
     and the RS-dropped forms of the frozen texts are selected.
     - The drop applies to F1's alphabet only: the fixtures SW and SW− keep their R-S completion and their frozen
       expectations (re-review r4 B3).
     - The self-test drives the RS-dropped note path, with S4.
   - **The second structured line.** `verdict` prints, after the token line,
     `DERIVED RUc_restores=<yes|no> RY_restores_and_RUc_not=<yes|no> RUP_restores_and_RUc_not=<yes|no>`. So a Q-like
     outcome is not read from the token alone. Each key names the test it reports, so a bare "no" cannot read as
     independence (re-review r5 N3). The schema's `derived.g_specific` and `derived.g_eta` hold the same booleans. This
     line never changes the token.

**Tokens.** `ARP3-QC22-IMITABLE`, `ARP3-QC22-CONTEXTUAL-<S>` and `ARP3-QC22-VOID`.
- **Reported beside the token, never changing it:** the R-Uc verdict, `g_specific`, `g_eta`, L1, EXP, INT, `cert_X3`
  for `g`, `g_1` and `g_2`, the ranks, the ranks added, the deciding steps, and the per-block fields.
- **No measured number is preregistered.**
- **What infeasibility licenses.** LP infeasibility licenses only the statement "no preparation- and
  measurement-noncontextual model over F1's own equivalences". By Lemma NC-F it implies a degenerate pairing, and
  hence non-spanning, on the charged configurations. CONTEXTUAL is the generic outcome for F1's preparation structure
  (`r_S ≤ 6` against 36 reads, as the paper analysis predicts; the round measures `r_S`; R14a-N4), so a CONTEXTUAL
  token carries its information in `{S}`. No text reads it as non-imitability beyond F1, or as a nonclassicality
  witness.

## Frozen texts of the result note

`controls.py note` prints the following, in order:
- the token;
- the control table;
- the per-condition table: (a) L1 and EXP with witnesses; (b) `d`, `r_S`, `r_E` and `cert_X3`; (c) the LP; the
  completions, separately; the per-block fields. Every cell uses the frozen renderings below;
- exactly one text below;
- the section `ADA`.

**Common clause:** "The audit's literal check (P★'s branches and mechanism-off `Z±`, frame-time `Z`/`X` reads) is
classically imitable by an explicit model (decided in this round as CC-F0, with its model verified), which closes
it under the audit's rule, 'Feasibility closes the instance'; this round does not revisit it. F1 is a new question
in the finite class Π_fin:
- the rule `G_SM` at `q = 2` on rings of 25 and 29 sites;
- P★'s supplies, including sharp background cells, and P★'s herald;
- carrier inputs `Z±, X±`;
- one read per run of one `u` slot of a site in `{−2, …, 3}` at a time in `{2, …, 7}`.

The hidden slots (the carrier's unknown slot and the switch cells) are uniform and independent in every F1
preparation. {hidden-law sentence} The round tests preparation and measurement noncontextuality of a prepare-measure
fragment, not transformation noncontextuality. P★'s instrument fails C-CP (M2D:85-92), so no statement here concerns
quantum behaviour."

`{hidden-law sentence}` is one of two frozen forms (re-review r4 B3):
- with R-S in scope: "A correlated or non-uniform hidden law is not tested, apart from R-S's switch supplies, and any
  conclusion is scoped to this hidden law.";
- RS-dropped, replacing that sentence: "A correlated or non-uniform hidden law is not tested, and any conclusion is
  scoped to this hidden law. The switch-supply completion R-S was declared out of scope before `F` (precondition 2)
  and was not tested."

**Frozen renderings** (re-review N4). Only these words are interpolated:
- `{L1}` renders as "determined or biased in a record branch (witness: input {i}, herald {h})" or "not determined or
  biased in any record branch".
- `{EXP}` renders as "read-record dependent, correlationally (witness: input {i}, herald {h}, read u_{s}({t}))" or
  "not read-record dependent in any branch".
- `{cert_X3}` renders as "yes (read u_{s}({t}))" or "no".
- `{g_specific}` renders as "R-Y restores and R-Uc does not: yes" or "R-Y restores and R-Uc does not: no". On "no"
  it is followed by the frozen sentence: "A 'no' does not show that the contextuality is independent of `g`'s law:
  when several independent directions are degenerate, no single supplied completion restores." (re-review r4 B1;
  fixture GX).
- `{g_eta}` renders as "R-U′ restores and R-Uc does not: yes" or "R-U′ restores and R-Uc does not: no". On "no" it is
  followed by: "A 'no' does not show that the contextuality is independent of `g`'s correlation with `η`: when
  several independent directions are degenerate, no single supplied completion restores."
- `{RUc}` renders as "feasible" or "infeasible".
- `{S}` renders as the token suffix.
- Block fields render as "herald {h}: sub-fragment {feasible|infeasible}; L1 in some branch of the block: {yes|no};
  EXP in some branch of the block: {yes|no}".

- **IMITABLE.** "F1 has an exact preparation- and measurement-noncontextual model, verified against the definition.
  In Π_fin, F1's encoded record statistics are classically imitable in the gate's fixed class, restricted to this
  prepare-measure fragment. `g` is {L1}, and {EXP}." + common clause.
- **CONTEXTUAL-{S}.** "F1 admits no preparation- and measurement-noncontextual model over its own equivalences
  (Farkas certificate verified against independently enumerated facets). By Lemma NC-F, the pairing of F1's
  preparation and read spans is degenerate on the charged configurations. The supplied completions that restore a
  noncontextual model are {S}. Decorrelation keeping the joint law of `g` and `η` (R-Uc): {RUc}. Test of dependence
  on `g`'s law, marginal or conditional on `η`: {g_specific}. Test of dependence on `g`'s correlation with `η`:
  {g_eta}. `g` is {L1}, and {EXP}. An F1 read equal to `g` on `Ω_reach`: {cert_X3}.
  Per herald block: {block fields}. These are measured conjunctions. A classical configuration model (fixture H3)
  produces the same kinds of conjunction through independent sectors, and M2D's Proposition B names the structure, a
  fixed conditional law. Nothing here is a nonclassicality witness, and nothing here establishes that a missing read
  or preparation is physically absent." + common clause.
  - **Added when `S = NONE`, with RS in the alphabet:** "No single supplied completion of `g` or of the switch
    supplies restores a noncontextual model. The degenerate directions may lie in several of the completed directions
    at once, or in others, and are not attributed in this round."
  - **Added when `S = NONE`, with RS dropped:** "No single supplied completion of `g` restores a noncontextual model.
    The switch-supply completion was declared out of scope before `F` and was not tested. The degenerate directions
    may lie in several of the completed directions at once, or in others, and are not attributed in this round."
- **VOID.** "A required control failed, a fragment was undecided or out of scope, the sizes disagreed, or the output
  was incomplete: {codes}. No reading is made. The measurements are preserved as produced."

**What no outcome shows** (carried after the token):
- It does not show that the dichotomy (M2D:728-733) holds or fails.
- It does not adopt M-INACC, M-FIX or any premise.
- It makes no statement outside Π_fin.
- It changes no manuscript claim, and no status of P1, P2 or H-PREP.
- MIR's `E_A`/`E_B` (`G_σ`) are not used.

**S4 phrase screen.** It is applied to the note outside the frozen texts, and to the frozen texts in the self-test.
The phrases are: "proves", "proved", "theorem", "never", "permanently", "physically absent beyond",
"quantum advantage", "genuinely quantum", " iff ", "if and only if", "is equivalent to", "in general",
"for every observer", "native protection", "should not be read", "does not hold for", "refutes",
"operationally accessible", "not operationally accessible", "nonclassical mechanism", "witnesses nonclassicality".
A hit fails V.

## Assumption-dependence analysis (ADA)

The ADA implements c.6723491138.
- It is generated after the token, from frozen sentences and measured fields.
- `decide` reads no ADA field.
- A sentence broader than Π_fin carries "outside this round's model, not established".
- New variants are named as candidate rounds and are not run here.

### Part 1. The ledger (frozen at `F`)

Types follow c.6723491138: native (preserve), empirical (reproduce the observable consequences), imported
(challenge). An uncertain type is carried both ways.

| id | assumption, as used | type | source |
| --- | --- | --- | --- |
| A-BIJ | second-order bijective form | native | M2D:203; SM:106 |
| A-CONF | every read reports a configuration function (P-c) | **uncertain**: OI's observation premise, or a modelling identification | M1D (P-a)–(P-c) |
| A-Q2 | `q = 2` | **uncertain** | M2D:206 |
| A-GSM | the ring `G_SM` | **uncertain**: the state-dependence principle is a stated hypothesis; the particular ring is imported | M2D:199-209 |
| A-RING | `Z_L`, `L ∈ {25, 29}`, window `{−2, …, 3}`, horizon 7 | imported (bounds) | this file |
| A-SUP | P★'s mixed supply class, including sharp `(0, 0)` background cells | imported (outside SA-1(c)) | M2D:634-637; AP1:297-299 |
| A-P2 | carrier inputs `Z±, X±` only | imported (SA-1(c)); not varied (R-Y completes at `τ`, not at the inputs) | AP1:297-299 |
| A-SWITCH | switch cells `X+`, `u` hidden uniform | imported (P★'s supply), a hidden law. With R-S in scope: **varied by R-S**. RS-dropped: **not varied** (R-S declared out of scope before `F`) | M2D:635-636 |
| A-HPREP | herald as a non-terminal record read as a preparation | imported (H-PREP) | M2D:692-694, :775 |
| A-READ1 | one non-disturbing configuration-function read per run; no joint records | imported (read class) | this file (*The model*, F1 reads) |
| A-N2 | hidden slots uniform and independent | **uncertain**: a native measure applied through H-PREP; a hidden-prior assumption (c.6723585151) | M2D:774 |
| A-SPLIT | carrier/`η` split; `g = z + x` at `τ = 3` (G-Y) | imported (definitional; a declared departure from the audit's hidden-cell wording) | this file (*The model*) |
| A-ACC | L1 (audit), EXP (owner), INT (counterfactual) as the access notions | imported (definitional) | this file (*Measured quantities*) |
| A-NC | generalized preparation and measurement noncontextuality | imported (the gate class) | M2D:485-498 |
| A-PM | prepare-measure folding; transformation NC not tested | imported | this file (*The exact method*, *Arithmetic*) |
| A-LP | the state-facet LP reduction | imported (mathematical; certificates checked against the definition) | this file (*The exact method*, steps 2 and 4) |
| E-CTX | observed quantum statistics violate noncontextuality inequalities on fragments with tomographically certified equivalences | empirical; not tested here, and unsupported in this round | none on `main` |
| E-EQ | the standard for operational equivalence | **uncertain**: empirical (do not weaken it), or the imported spanning requirement | c.6723491138; M2D:488-490 |

**Obstacle directions.** The programme question is whether nonclassical observer statistics need an inaccessible
functional (M2D:832-844).
- **IMITABLE** is an obstacle to contextuality in F1.
- **CONTEXTUAL-{S}** with `S ≠ NONE` is contextuality that the named supplied completion removes. It is an obstacle
  only in the sense that the contextuality rests on that missing completion.
- **CONTEXTUAL-NONE** is unattributed.
- **VOID** gets no ADA beyond the record of what was measured.

The owner's significance ladder (c.6723571280) is printed as context, as exactly its three table rows, verbatim
(re-review N3):
- "An imported assumption causes an apparent obstruction | We identify an unnecessarily restrictive test";
- "Removing that assumption yields a valid OI mechanism | We overcome a genuine obstruction in the tested model";
- "The mechanism reproduces the required quantum predictions, measurements and composition | We advance toward
  operational equivalence".

The note then adds one frozen sentence: "None of this round's outcomes reaches the third row." The comment's closing
sentence is not printed. The S4 screen applies to all printed text, and these rows contain no S4 phrase.

### Part 2. The post-result template

**Used or idle, by measurement.**

| item | status rule |
| --- | --- |
| A-READ1 (the `g` read missing) | **essential in this model** when F1 is infeasible and F1+R-G is feasible |
| A-SPLIT (`g`'s law, marginal or conditional on `η`, fixed at `τ`) | **essential in this model** when F1 is infeasible and `g_specific` holds |
| (no single completion restores) | When F1 is infeasible and `g_specific` and `g_eta` are both "no": **not attributed**. The note prints "a 'no' does not show that the contextuality is independent of `g`; several causes may be present (fixture GX)". No item is marked idle because of a "no" (re-review r4 B1) |
| A-SPLIT (`g`'s correlation with `η` at `τ`; its origin, A-GSM dynamics or A-HPREP conditioning, is not attributed) | **essential in this model** when F1 is infeasible and `g_eta` holds. Printed with both origin readings (re-review N2) |
| A-SPLIT (the carrier's correlation with `η` beyond `g`) | **essential in this model** when F1 is infeasible and F1+R-Uc is feasible |
| A-P2 | **not varied**: R-Y completes at `τ`, not at the inputs. A `Y±`-input round (NR-3, or a successor) would vary it (re-review N2) |
| A-SWITCH, A-N2 (the fixed hidden switch law) | **essential in this model** when F1 is infeasible and F1+R-S is feasible |
| A-GSM | **used for access** when INT > 0 under `G_SM` while CC-OFF is green (diagnostic; counterfactual) |
| A-SUP, A-HPREP, A-RING, A-Q2, A-CONF, A-BIJ, A-NC, A-PM, A-LP, A-ACC | **used, not varied** (`L` varied: IS-SIZE) |

**The five questions** (printed for every substantive token):
1. *Which assumptions were essential?* The items marked essential above.
2. *Their types?* From the ledger, both readings for an uncertain item.
3. *Does removing an imported assumption eliminate the obstacle?*
   - Measured for the `g` read (R-G), the carrier's correlations with `η` (R-U′ and R-Uc), `g`'s law (R-Y against
     R-Uc) and the switch law (R-S, on a larger `Ω`; unless declared `out_of_scope` before `F`).
   - Not decided otherwise: candidate rounds.
4. *A counterexample with the same observable requirements without it?* Not decided: no observable quantum
   requirement is measured (NR-7). H3 is a classical fixture, not such a counterexample.
5. *All OI models or this one?* This one: Π_fin, under the common clause.

**Synthesis (c.6723571280).** One row per obstacle. Its status is one of:
- **survives at native/empirical level in this model**, when every essential item is native or empirical;
- **depends on an imported item in this model**, naming the item and the completion that removed it;
- **undecided**, when it depends on an imported item that is not varied, naming the candidate round.

An uncertain item prints both rows. No row is stated outside Π_fin. Where a completion removes contextuality, the
note adds the owner's standard verbatim (c.6723491138): "Conversely, relaxing an assumption is not sufficient by
itself. The resulting model must still produce valid probabilities, observable quantum predictions and consistent
behavior across repeated experiments."

**Candidate new rounds (named, not run).**
- **NR-1:** joint records.
- **NR-2:** sequential and transformation-NC fragments.
- **NR-3:** P2 throughout, with no sharp background cells.
- **NR-4:** a larger window and horizon.
- **NR-5:** an invariant for `G_SM` (physical absence).
- **NR-6:** the physical status of a fixed conditional law (N2, M2D:584-587).
- **NR-7:** the observable level: probabilities, repeatability and quantum predictions.
- **NR-8:** G-H1 or G-H2 as the decided functional.
- **NR-9:** correlated hidden laws (c.6723585151).

## Scripts

- **`qc22_check.py`** (blob PENDING; sha256 PENDING).
  - It imports `fractions`, `itertools`, `json`, `os` and `sys`, and reads no file. `os` is referenced at exactly two
    sites, each `os.environ` passed whole: the `if __name__ == "__main__":` block, which calls
    `s_entry(sys.argv, os.environ)`, and the F1 builder's own refusal check, `s_mode(sys.argv, os.environ)`
    (control B; R13-N2). The entry function `s_entry(argv, environ)` calls `s_mode(argv, environ)`, and then refuses
    with exit 4, runs fixture mode, or calls the F1 builder.
  - **`cert_sha256` (R13-N1; Q-C2-1 r14's wording).** `qc22_check.py` does not import `hashlib`. `cert_sha256` is
    computed by `h_sha256(data) → str`, a pure-Python SHA-256 (FIPS 180-4) in its own namespace `h_*`. C-INDEP's
    rules do not admit it among the calls a `v_*` function may make. The checker's self-test (A8) checks three FIPS
    180-4 examples:
    - the empty message: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`;
    - `abc`: `ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad`;
    - `abcdbcdecdefdefgefghfghighijhijkijkljklmklmnlmnomnopnopq`:
      `248d6a61d20638b8e5c026930c3e6039a33ce45964ff2167f6ecedd419db06c1`.
  - **No sets (R13-N17).** `-I` leaves string-hash randomization on, so the iteration order of a `set` of strings can
    differ between processes. `qc22_check.py` constructs no `set` or `frozenset` (control B). It uses lists and `dict`
    keys, whose order is insertion order, so its outputs are byte-identical across processes.
  - The solver's functions are named `s_*` and the verifier's `v_*` (C-INDEP).
  - **Modes:**
    - the default prints canonical-JSON `measurements.json`, exiting 0 when the output is complete and every control
      is green, and 3 when a control is red or a fragment is `out_of_scope`. Any other exit is incomplete;
    - `--stress` prints canonical-JSON `stress.json`;
    - `--self-test`;
    - `--event <name>` is required for the default computation. **Three keys select decisive mode (re-review r8
      B1(a), r9 B4(a)):**
      - `<name>` is `workflow_dispatch`;
      - the environment variable `GITHUB_EVENT_NAME` is `workflow_dispatch`;
      - `GITHUB_RUN_ATTEMPT` is `1`.

      If any key fails, the checker runs fixture mode, whose exit rule is in *Method*. Without `--event` it refuses,
      with exit 4. `--event fixture`, job A's literal, always fails the first key.
    - `--dispatch-sha <40-hex>` (job B only) is recorded as `parameters.dispatch_sha`. It selects no mode. A value
      that is not 40 lowercase hex makes it refuse, with exit 4.
      - The host sets both variables for every step, and child processes inherit them.
      - The decision is the pure function `s_mode(argv, environ) → "decisive" | "fixture" | "refuse"`. The entry calls
        it with `os.environ`; the self-test calls it with synthetic mappings.
    - **The builder refuses on its own (r9 B2(h)).** The F1 builder's first statement checks
      `s_mode(sys.argv, os.environ) == "decisive"`, and raises otherwise, which is a crash and hence VOID. Even a
      call reached by an unforeseen route therefore cannot compute F1 outside a decisive run.
    - **The builder's name (r10 B2).** It is referenced, as a `Name` node, at exactly two sites (control B):
      - the entry function `s_entry` (the default computation);
      - the single self-test function `t_builder_refuses`. Its body is one `try` statement:
        - the `try` calls the builder with no argument;
        - the handler catches the refusal exception and records a pass;
        - an `else` clause records a failure.

      **Why the second site is safe.** The self-test runs only as A8, whose real `sys.argv` is
      `qc22_check.py --self-test`, with no `--event`. So `s_mode(sys.argv, os.environ)` returns `"refuse"`
      whatever the environment, and the builder raises at its first statement, before any work. That holds in a
      decisive dispatch too.
- **Schema `arp3-qc22-measurements` v3.**
  - `parameters`; `complete`; `mode` (`"decisive"` or `"fixture"`).
  - In fixture mode, `complete` is `false`, and every F1-family fragment has `lp: "placeholder"` and no certificate.
    Fixture-mode output is therefore decision-invalid on three independent conditions (r7 B2(b)).
  - For each size, `"25"` and `"29"`:
    - for F1, F1_RG, F1_RUP, F1_RUC, F1_RY, F1_RS (if in scope) and F0: `preps`, `reads`, `effects_reduced`, `d`,
      `r_S`, `r_E`, `rank_added`, `lp`, `decided_by`, `pivots`, `max_bits`, `work`, `cert_sha256`;
    - `derived`: `g_specific`, `g_eta`;
    - `access`: `L1`, `EXP` and `cert_X3` for each of `g`, `g_1` and `g_2`, with witnesses; `INT` for `g` only;
    - `blocks`; `cc_off`; `is_pstar`; `c_eval`; `lists_sha256`.
  - `fixtures`: verdicts, deciding steps, the derived fields and `decide` tokens for POS-1, POS-2, NEG-1, NEG-2, GBIT,
    DUAL, H3, G, X, Q, SW, SW−, F10, ZPT and X+RU′.
  - `budget`: `P_max`, `B_max`, `W_max`, and per fragment whether each was respected.
  - `is_rule`, `is_size`, `c_cert`, `c_indep`, `c_ncf`, `c_sym`, `c_iso_name`, `flags`.
  - There is no timestamp, host or duration field.
- **Schema `arp3-qc22-stress` v2** (`--stress`). Per fragment (stress fixtures, frozen fixtures and their
  completions, CC-F0): `verdict`, `decided_by`, `pivots`, `max_bits`, `work`, `certificate_verified`; the totals
  `W_fix` and `W_stress`. There is no timestamp.
- **Schema `arp3-qc22-run` v1 (R13-N13).** `controls.py derive-run <run_id>` prints it from the runs, jobs (every page)
  and artifacts APIs: `run_id`, `run_attempt`, `head_sha`, `event`, `created_at`, the run's `conclusion`, the base and
  head `sha` of its `pull_requests` entries, and for every attempt each job's name and conclusion and each step's name,
  number, conclusion, `started_at` and `completed_at`; and each artifact's name, id and `digest` (provenance; HF-1);
  and, for S1's run only, the S1 binding's inputs (*Runs, evidence, approvals*; R14-N6). It has no other field.
  `design-run.json`, `confirmation-run.json`, `evidence/f-run/results.json` (the run at `F`,
  precondition 8; committed at S1), `evidence/s1-run/results.json` (the run at S1; committed at `E`) and each
  gate-test entry's run record use it.
- **Schema `arp3-qc22-approvals` v1 (R13-B4).** `evidence/approvals.json` holds one entry, with the fields of *Runs,
  evidence, approvals*, for each decisive dispatch made before `E` is committed (S1, and any retake). The executor
  writes it from the comments and approvals APIs. It is committed at `E`, and `check --stage E` and `verdict` verify
  every entry against those APIs.
- **`controls.py`** (blob PENDING; sha256 PENDING).
  - **Modes:** `check <commit> --freeze F [--stage S1|E|W]`, `decide`, `note`, `replay <run output>`,
    `stress-check <stress.json>`, `fixture-mode-check <fixtures.json>` (R13-B2),
    `env-read` (E-READ (a) or (c) only), `approval-check <run_id> <sha>` (E-BIND only),
    `derive-run <run_id>`, `order`, `verdict`, `--self-test`.
  - **Arguments that exist only after `F`** (R13-B4; Q-C2-1 r14's reading) are supplied at each capture as `a_ok`
    values: the stage commits (HEX40), and the comment ids (DEC) of `F`'s designation, of each stage's approval and,
    under E-READ (b), of each posted read. Before `F`, `order` and `verdict` run only in the self-test, on synthetic
    records. Their first real run is the capture of `check --stage S1`, where a fault is a failed capture.
  - **Codes:**
    - T: chain and blocks;
    - G: paths;
    - R: record files by stage (S1 includes `confirmation-run.json`, `confirmation-measurements.json`, `gate-tests.json`
      and `env-pin.json`; `E` includes `order-s1.json` and `approvals.json`; R13-B4, B5);
    - B: blobs, allowlists, C-EXACT, C-INDEP, and **the guard's node-form rules** (re-review r7 B2(a), r8 B1(b), r9
      B2), checked by AST on every node of each script.
      - **In `qc22_check.py`:**
        - the string `"workflow_dispatch"` occurs exactly once, as the module constant `DISPATCH_EVENT`;
        - `DISPATCH_EVENT` is referenced only in `s_mode` and in M-GUARD's self-test functions;
        - `os` is referenced at exactly the two sites named above, each as the expression `os.environ`;
        - the F1 builder's name is referenced only at the two sites named above (`s_entry` and
          `t_builder_refuses`, in the stated form), and the builder carries its own refusal check;
        - no call to `set` or `frozenset`, no set display and no set comprehension occurs (R13-N17);
        - module-wide, it uses no `getattr`, `setattr`, `delattr`, `globals`, `locals`, `vars`, `breakpoint`, `exec`,
          `eval`, `compile` or `__import__`, and no name or attribute of the form `__*__` other than the single
          statement `if __name__ == "__main__":`.
      - **In `controls.py`, a node-form allowlist:**
        - **(a) Imports.** Only `import X`, with `X` in the frozen list `ast`, `fractions`, `hashlib`, `io`, `json`,
          `os.path`, `re`, `subprocess`, `sys`, `tempfile`, `zipfile` (`io` and `zipfile` for the S1 binding;
          R13-B2). No `as`, and no `from … import`.
        - **(b) Attributes.** An attribute of a module name must come from that module's frozen list:
          - `subprocess.run`, `subprocess.PIPE`;
          - `os.path.join`, `os.path.isfile`;
          - `json.loads`, `json.dumps`;
          - `hashlib.sha256`;
          - `re.fullmatch`;
          - `sys.argv`, `sys.exit`, `sys.stdout`, `sys.stderr`;
          - `fractions.Fraction`;
          - `tempfile.TemporaryDirectory`;
          - `io.BytesIO` and `zipfile.ZipFile` (R13-B2). A `ZipFile` is constructed only as
            `zipfile.ZipFile(io.BytesIO(<bytes>))`, with one argument, and only `namelist()` and
            `read("measurements.json")` are called on it;
          - `ast.parse`, `ast.walk` and the `ast` node classes.

          Hence no `os.path.os`, `sys.modules`, `subprocess.os` or `tempfile._os`.
        - **(c) Forbidden everywhere.** No name or attribute of the form `__*__` other than the single
          `if __name__ == "__main__":`. No `getattr`, `setattr`, `delattr`, `globals`, `locals`, `vars`,
          `breakpoint`, `help`, `exec`, `eval`, `compile` or `__import__`.
        - **(c″) The frozen helpers (r11 N1, BYP-20; r12 N1).** `a_ok`, `w_path`, and the entry's root check are
          each bound exactly once, by a top-level `def`. Apart from that `def`, their names occur only as `Name`
          nodes in `Load` context. No other node of any kind binds them: no assignment, augmented or annotated
          assignment, walrus, `del`, `global` or `nonlocal`, `for`, `with` or `except … as` target, comprehension
          target, `match` capture or `as` pattern, argument, `import` alias, second `def`, or `class`. Their bodies
          are fixed by the blob pin.
        - **(c′) Call position only (r10 B1(a)).**
          - `subprocess.run` and the builtin `open` occur only as the `func` of a `Call` node.
          - They are never assigned, passed as an argument, returned, stored in a container, used as a default value,
            or given to `map` or any other function.
          - The names `subprocess` and `open` are never rebound.
        - **(d) `open`.** Every read uses a literal read mode (`"r"` or `"rb"`). The only write-mode `open` is in the
          self-test, with a path that the single helper `w_path` builds from a `tempfile.TemporaryDirectory` and a
          literal file name. That file-name argument is a string literal matching `[A-Za-z0-9_.-]+` (no `/`), and
          `w_path` joins it under the temporary directory (r12 N1). Nothing else in `controls.py` writes a file, so a `.pth` or other startup file cannot be planted.
          A record that a mode produces (`order-s1.json`, the run records, A11's `env.json`, a capture's record) is
          that mode's standard output, which the executor's shell or the step's `run:` line redirects into the file
          (R13-B5).
        - **(e) Process starts.** Only as `subprocess.run(<list display>, ...)`.
          - No keyword other than `capture_output`, `check` and `text`. There is no `shell=`, `env=`, `executable=`
            or `cwd=` (r10 B1(b)).
            - Every process starts in the invoking shell's directory.
            - The entry refuses, with exit 2, unless `git rev-parse --show-prefix` prints an empty line, that is,
              unless it runs at the top of the repository's work tree.
            - The workflow runs it at the workspace root (control W).
          - Every list element is a string literal, a call to the frozen validator `a_ok(x)`, or, as `gh`'s path
            only (rule (g)), an f-string whose every formatted value is an `a_ok(...)` call and whose text, with
            those values replaced, is a frozen template (R13-N6).
          - **`a_ok`'s patterns** (r10 B1(c)): `re.fullmatch` against exactly one of these, else it raises:
            - HEX40 `[0-9a-f]{40}`;
            - DEC `[1-9][0-9]{0,19}`;
            - TIME `[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z`;
            - PATH `C(/C)*`, with component `C = (?!\.\.?(?:/|$))[A-Za-z0-9_.][A-Za-z0-9_.-]*`;
            - HEX40 `:` PATH.

            None of them admits a leading `-`, a `=`, whitespace, or a `..` component.
        - **(f) `git`.** The list is `["git", <subcommand>, ...]`.
          - `<subcommand>` is a literal from the frozen read-only list `rev-parse`, `cat-file`, `ls-tree`,
            `rev-list`, `merge-base`, `diff-tree`, `show`.
          - `show` and `diff-tree` always carry `--no-textconv` and `--no-ext-diff`.
          - No element is, or begins with, `-c`, `--config-env`, `--exec-path`, `-C`, `--git-dir`, `--work-tree`,
            `--upload-pack`, `--output`, `--ext-diff`, `--textconv` or `--filters` (r10 B1(c); r11 N1, BYP-19).
          - The literal `--end-of-options` precedes the first `a_ok(...)` element, and every element after it is an
            `a_ok(...)` call. A `rev-parse` that takes an `a_ok` argument also carries `--verify`.
            - **Why.** The rule ties each admitted form to one object name. Whether a given git echoes the literal
              `--end-of-options` in some form is not assumed: the self-test below checks each form's output on the
              runner's git (R14-Rb2).
            - **The self-test.** It runs one call of each admitted subcommand form on the runner's git, and checks
              each one's **output**, not only its exit status. So a git that rejects or echoes `--end-of-options`
              fails the self-test.
          - **What this gives.** No alias or other config-borne command can run through these rules, given:
            - the process's directory is the repository root;
            - no `cwd=`;
            - no `-c`.

            The repository's own `.git/config` is not in the tree. In CI it is written by `actions/checkout`.
        - **(g) `gh`.** The list is exactly `["gh", "api", "--method", "GET", <path>, ...]`.
          - `<path>` is an f-string over the frozen templates `repos/amaybaum/incompleteness/...`, with `a_ok`-validated
            values.
          - The frozen templates are these:
            - `actions/runs?...`;
            - `actions/runs/{DEC}`;
            - `actions/runs/{DEC}/attempts/{DEC}`;
            - `actions/runs/{DEC}/attempts/{DEC}/jobs?per_page=100`;
            - `actions/runs/{DEC}/artifacts`;
            - `actions/artifacts/{DEC}/zip` (R13-B2), read as bytes by `verdict` and, for S1's measurements
              artifact before `E` is committed, by `derive-run` (R14-N6);
            - `issues/comments/{DEC}` (R13-B4);
            - `actions/runs/{DEC}/approvals`;
            - `environments/arp3-qc22-decisive`;
            - `environments/arp3-qc22-decisive/deployment-branch-policies`;
            - `deployments?environment=arp3-qc22-decisive&per_page=100`;
            - `deployments/{DEC}/statuses`;
            - `git/trees/{HEX40}?recursive=1`;
            - `git/trees/{HEX40}`;
            - `activity?ref=refs/heads/...`;
            - the repository itself.
          - Every further element comes from the frozen set `--paginate`, `-H`,
            `"Accept: application/vnd.github+json"`.
          - So there is no `--input`, `graphql`, `--hostname`, `-f`, `-F`, `--field` or `--raw-field`, and no other
            `-X` or `--method`, in any spelling.
        - **(h) Control T's exception.** The one process start that is not `git` or `gh` is
          `["python3", "-I", "-S", "-c", <the frozen string>, a_ok(D), a_ok(F)]`. It inherits the repository root as
          its directory, as rule (e) requires, and that is needed for `tools/`.
          - `-S` disables `site`, so no startup file runs.
          - Its code imports only `tools/v3_verifier.py`, whose blob the inputs pin.
        - The string `"workflow_dispatch"` occurs only inside the module-level string constants named `SPLICE_*`,
          which hold the frozen splice byte-exactly for control W, and inside functions named `run_class_*`, which
          `derive-run`, `order` and `verdict` call (R13-N3).
        - `replay` compares files only: it reads two files in `"rb"` mode, parses each with `json.loads`, removes
          `parameters.dispatch_sha` from both, and compares their canonical serializations (R13-B1; B6).
      - **What these rules give, as checked by B and exercised by M-GUARD (BYP-1 to BYP-21, BYP-23 to BYP-26, ZIP-1
        to ZIP-3 and the unnumbered variants; R14 §5).** This is all that B
        claims (r10 review, overall design). For the two frozen blobs that B checks, and for every route these rules
        admit:
        - `controls.py` starts no process other than read-only `git`, GET-only `gh api` and control T's frozen
          command;
        - it writes no file outside a self-test temporary directory;
        - so it cannot create, trigger, re-run or approve a workflow run (r8 N2). That covers
          `POST …/pending_deployments`, the deployment-review endpoint, which is excluded by the GET-only form and
          named as a variant in M-GUARD;
        - it cannot import or execute `qc22_check`.

        B claims nothing about routes it does not model, such as the interpreter, the runner or the host. It does not
        stand in for the Environment gate, which is the primary enforcement (*The workflow edit*).
        - **Who approves.** The session acts under the owner's GitHub identity, `amaybaum`. It never calls the
          deployment-review endpoint or writes to the Environment by any route. Only the owner approves or rejects,
          through the host's interface.
        - **The identity limit (r11 B2).** Under E-ID option (iii) the required reviewer is `amaybaum` and
          `prevent_self_review` is `false`, so the host would accept an approval or an Environment edit made with
          the credential the session holds. Against that credential, approval and edits are held back only by the
          owner's procedural commitment (precondition 2a). The host's records cannot tell the owner's act from a
          session's. Options (i) and (ii) of E-ID change this, as stated there;
    - W: `verify.yml` as a whole file (re-review r9 N3). At the design run, at 6′, at S1 and at `E` it must be
      byte-equal to `D`'s `verify.yml` with the frozen splice. Hence no workflow-level `env:`, `defaults:` or shell
      override can reach either job. The splice includes:
      - the two `workflow_dispatch` inputs;
      - both jobs, with their display names and `timeout-minutes`;
      - A3's literal `--event fixture`;
      - job B's job-level `if:`, its `environment: arp3-qc22-decisive` line, its `env:` and B3;
      - B4's compound `--event` expression and B6's `if:`;
      - the markers A10 and A3b;
      - the aggregate's lines;
      - per precondition 2b: A11 and job A's `permissions:` (E-READ (a)), and B3b and job B's `permissions:`
        (E-BIND). Each is present exactly when its option is adopted.

      Its self-test shows that each of these removals fails W:
      - the event key, the attempt key or the receipt key, from B4 or from B6;
      - any key of job B's `if:`;
      - the `environment:` line;
      - B3;
      - A3's literal;
      - the marker A10;
      - the marker A3b;
      - A11 or B3b, when adopted;
    - **N: the Environment** (owner decision c.6726548830, item 4; r11 B1). It compares a read of the Environment with
      the pin, through the channel fixed by E-READ (precondition 2b).
      - **The read.** It is the Environment's `GET environments/arp3-qc22-decisive` and
        `…/deployment-branch-policies`, reduced to the frozen fields of precondition 2a, in canonical JSON:
        - `id`, `name`, `created_at`, `updated_at`;
        - the protection rules;
        - `can_admins_bypass`;
        - the branch policy and each branch policy's `id`, `name` and `type`.
      - **The pin.** `evidence/env-pin.json`, committed at S1 under every option.
      - **The stage reads: order and placement by channel (r12 N3; R13-B2, B5).** A stage's read is taken after that
        stage's commit exists, so it is never in that stage's own tree.
        - **Under E-READ (a).** A11, in job A of the S1 and `E` runs, reads the Environment and compares the read with
          the committed `env-pin.json` inside the job. Its step conclusion carries the result (§A.44); the `env.json`
          artifact's `digest` is provenance. `verdict` reads A11's conclusion in attempt 1 of the S1 and `E` runs from
          the jobs API, and S1's is also in `evidence/s1-run/results.json`, committed at `E`. `verdict`'s read is the
          `E` run's A11. A11 runs in parallel with job B, so these reads are **detection after the fact**. There is no
          read before either dispatch, unless the owner also wants a pre-dispatch read through (b).
        - **Under E-READ (b) and (c).** `check --stage S1`, run after S1 is pushed and before the S1 dispatch, reads
          the Environment through the channel (under (b), the owner's posted read, through `issues/comments/{DEC}`;
          under (c), directly) and fails unless the read equals the pin. The read is the `environment` section of the
          capture that `check --stage S1` prints and the executor redirects into `evidence/order-s1.json`, committed
          at `E`. `check --stage E`, after `E` is pushed and before the `E` dispatch, reads the same way and fails
          unless the read equals the pin, and `verdict` reads once more. These two reads are in no round tree: each
          is printed in its capture's record and posted on the round PR, their disposition under §A.42 item 8 is the
          owner's (precondition 2; R14-Rb2), and each check fails closed. Both stage reads precede their dispatches,
          so either can stop one.
      - **Pass condition.** Every field must equal the pin. A difference is a failed check, and the round halts VOID.
        That includes a different `id` or `created_at` (the Environment deleted and re-created) and a different
        `updated_at` (an edit) (r11 N2).
      - **This session cannot read the Environments API.** The session's proxy refuses it with 403 (r11 H17). So
        `controls.py`, run by the session, reads it only under E-READ (c); under (a) it reads it in job A, as A11
        (`env-read`), with the job's token (R14-N7).
      - **Residual.**
        - The host keeps no readable history of an Environment's settings.
        - Whether `updated_at` moves on every rule or policy edit is unverified, unless GT-6b shows it.
        - Until then, a change reverted between two reads may go undetected;
    - DS: inputs and drift;
    - X: schema and flags;
    - V: note regeneration and S4;
    - P: no unbackticked `PENDING` under `--freeze`; evidence pins, including `stress.json`'s sha256.

## The workflow edit (frozen text; control W)

**Two jobs (owner decision c.6726548830, item 4).** The splice adds two jobs.
- **Job A** (key `probes_arp3qc22`) runs on every event and never computes F1.
- **Job B** (key `probes_arp3qc22_decisive`) is the only job that can compute F1. It is gated by a GitHub Environment
  whose required reviewer is the owner.

They are split because an Environment's protection applies to every run of a job that names it, so a single job
would hold every pull-request run for approval. Both jobs go after the last job before the `probes` aggregate at
`D` (anchor PENDING).

**`workflow_dispatch` inputs (frozen addition to `on:`).** Two inputs, both optional, so a dispatch without them
behaves as before:
- `arp3qc22_decisive`, a boolean, default `false`;
- `arp3qc22_sha`, a string, default empty, carrying the approved commit's full id.

**Aggregate.**
- Both jobs are added to the aggregate's `needs`, with `ARP3QC22_RESULT: ${{ needs.probes_arp3qc22.result }}` and
  `ARP3QC22D_RESULT: ${{ needs.probes_arp3qc22_decisive.result }}` in `env`.
- After the last round's lines (anchors PENDING), the aggregate gets:
  - `echo` lines for both results;
  - `test "${ARP3QC22_RESULT}" = success`;
  - `test "${ARP3QC22D_RESULT}" = success -o "${ARP3QC22D_RESULT}" = skipped`.
- Job B is skipped on every run that is not an owner-gated dispatch. That keeps every other run green, later
  rounds' `F` and `E` dispatches included. Whether job B succeeded at S1 and `E` is checked by `verdict` from the
  jobs API, not by the aggregate.

### Job A — `probes_arp3qc22`, display name `Numerical probes / ARP-3-QC22 fixtures and stress` (frozen)

`timeout-minutes: 60`. No `environment:`. Its steps:
- A1. checkout with `fetch-depth: 0`.
- A2. `actions/setup-python@v5` with `python-version: '3.11'`.
- A3. **"ARP-3-QC22 fixture decision"**:
  `mkdir -p "$RUNNER_TEMP/arp3-qc22" && python3 -I -S -B <record dir>/qc22_check.py --event fixture > "$RUNNER_TEMP/arp3-qc22/fixtures.json"`.
  - The literal `--event fixture` means that job A runs fixture mode on every event, whatever the checker's other
    keys say.
  - This is the output used by 6′ and by C-STATELESS.
  - `mkdir -p` creates the output directory, which A3b, A5, A7 and A11 then use in the same job (R13-B3).
- A3b. **"ARP-3-QC22 fixture output is fixture mode"** (a marker; §A.44; R13-B2):
  `python3 -I -S -B <record dir>/controls.py fixture-mode-check "$RUNNER_TEMP/arp3-qc22/fixtures.json"`, with
  `if: ${{ always() }}` (R14-N10).
  - It runs whether or not A3 succeeded. A red A3 whose output is complete fixture-mode output, a fixture mismatch
    for example, still gives A3b `success`; a missing or non-fixture output gives `failure`. When A3 is `skipped`,
    A3b fails on the missing file, and the no-unapproved-F1 rule reads A3's own conclusion (R14a-Rc1).
  - It exits 0 iff the file parses as schema `arp3-qc22-measurements` v3 with `mode: "fixture"`, `complete: false`
    and every F1-family field the synthetic placeholder, and 3 otherwise.
  - Its conclusion is the structured record of A3's mode that the no-unapproved-F1 rule and 6′ read (*Runs,
    evidence, approvals*; precondition 6′).
- A4. `actions/upload-artifact@v4` of `fixtures.json` as the artifact `arp3-qc22-fixtures` (R14-N3), on every
  event, with `if-no-files-found: error` and `retention-days: 90`.
- A5. **"ARP-3-QC22 stress"**: `python3 -I -S -B <record dir>/qc22_check.py --stress > "$RUNNER_TEMP/arp3-qc22/stress.json"`.
- A6. `actions/upload-artifact@v4` of `stress.json` as the artifact `arp3-qc22-stress` (R14-N3), on every event,
  with `if-no-files-found: error` and `retention-days: 90`.
- A7. **"ARP-3-QC22 stress output equals the pinned sha256"**:
  `python3 -I -S -B <record dir>/controls.py stress-check "$RUNNER_TEMP/arp3-qc22/stress.json"`.
- A8. `python3 -I -S -B <record dir>/qc22_check.py --self-test`.
- A9. `python3 -I -S -B <record dir>/controls.py --self-test`.
- A10. **"ARP-3-QC22 receipt absent"** (a marker; r9 N6): `true`, with `if: ${{ hashFiles('verification/receipts/ARP-3-QC22.json') == '' }}`.
  - It is `success` on the design run, at 6′, at S1 and at `E`.
  - It is `skipped` on any tree carrying the receipt.
  - It is recorded in `design-run.json` and `confirmation-run.json`, and `check --freeze` requires `success`.

### Job B — `probes_arp3qc22_decisive`, display name `Numerical probes / ARP-3-QC22 exact decision (gated)` (frozen)

`timeout-minutes: 60`.

**Its condition, `if:`** (job level, so it is evaluated before the Environment is consulted):

`${{ github.event_name == 'workflow_dispatch' && github.run_attempt == '1' && inputs.arp3qc22_decisive == true }}`.

**It names the Environment, `environment: arp3-qc22-decisive`** (frozen). GitHub holds the job before it starts, until
a required reviewer approves the deployment, and blocks it if the ref is outside the Environment's deployment-branch
policy.

**Its `env:`** (job level): `ARP3QC22_SHA: ${{ inputs.arp3qc22_sha }}`. The input reaches the shell only as this
variable, never by interpolation into a `run:` line.

Its steps:
- B1. checkout with `fetch-depth: 0`.
- B2. `actions/setup-python@v5` with `python-version: '3.11'`.
- B3. **"ARP-3-QC22 approved commit and receipt"**:
  `test "$GITHUB_SHA" = "$ARP3QC22_SHA" && test ! -e verification/receipts/ARP-3-QC22.json`.
  - It fails unless the run's commit is exactly the commit named in the dispatch input, and unless the tree carries no
    receipt.
  - B3 stops a run whose commit differs from the **input**, even when its deployment was approved (r11 N4). A run
    whose approved review names a commit other than its own is not stopped by B3. Without B3b it is detected
    afterwards by the review-to-run binding (*Runs, evidence, approvals*), and the round halts VOID.
- B3b (**only if E-BIND is adopted**, precondition 2b; r11 N4). **"ARP-3-QC22 approval names this commit"**:
  `python3 -I -S -B <record dir>/controls.py approval-check "$GITHUB_RUN_ID" "$GITHUB_SHA"`.
  - It runs with `GH_TOKEN: ${{ github.token }}` in the step's `env:`, and job B carries `permissions:` with
    `actions: read` and `contents: read`.
  - It reads `GET actions/runs/{run_id}/approvals` and requires exactly one review with all of these:
    `state: "approved"`, `user.login` the E-ID reviewer, `environments` exactly `["arp3-qc22-decisive"]`, and
    `comment` matching `ARP-3-QC22 (S1|E|GT-2) <GITHUB_SHA>`. The gate-test stage `GT-2` is admitted so that GT-2's
    frozen comment can pass (R13-B6). B3b binds the commit; the stage is bound afterwards by the approval entry, whose
    review comment must name the entry's stage.
  - It sits before B3, so it makes the commit binding preventive.
  - Whether `github.token` with `actions: read` may read `approvals` is unverified. GT-2 and GT-2b test it.
- B4. **"ARP-3-QC22 exact decision"**:
  `mkdir -p "$RUNNER_TEMP/arp3-qc22" && python3 -I -S -B <record dir>/qc22_check.py --event "${{ (github.event_name == 'workflow_dispatch' && github.run_attempt == '1' && hashFiles('verification/receipts/ARP-3-QC22.json') == '') && 'workflow_dispatch' || 'closed-or-other' }}" --dispatch-sha "$ARP3QC22_SHA" > "$RUNNER_TEMP/arp3-qc22/measurements.json"`.
  - **The in-tree keys are kept as defence in depth:** the event key, the attempt key, the receipt key, and the
    checker's three keys (`--event`, `GITHUB_EVENT_NAME`, `GITHUB_RUN_ATTEMPT`). The builder also has its own
    refusal check.
  - `--dispatch-sha` records the input, after the checker's own 40-hex check (exit 4 otherwise; r11 N3), as
    `parameters.dispatch_sha` in `measurements.json`. It selects nothing.
  - **Fixture mode evaluates nothing of the F1 family under `G_SM`:** no F1-family table, no access fields, no INT,
    no IS-SIZE, and no C-EVAL on F1's charged configurations. C-EVAL's self-test version uses P★ and frozen
    synthetic configurations.
  - A missing `--event` makes the checker refuse, with exit 4, and the output's `mode` is `"decisive"` or
    `"fixture"`.
- B5. `actions/upload-artifact@v4` of `measurements.json` as the artifact `arp3-qc22-measurements` (R14-N3), with
  `if-no-files-found: error` and `retention-days: 90`.
- B6. `python3 -I -S -B <record dir>/controls.py replay "$RUNNER_TEMP/arp3-qc22/measurements.json"`, against the
  committed `<record dir>/evidence/measurements.json`, with
  `if: ${{ (github.event_name == 'workflow_dispatch' && github.run_attempt == '1' && hashFiles('verification/receipts/ARP-3-QC22.json') == '') }}`.
  It replays exactly when B4 ran in decisive mode. B6 runs after B4, in the same job, so the directory exists.
  - **The comparison (R13-B1; Q-C2-1 r14's wording).** Each file is parsed with `json.loads`,
    `parameters.dispatch_sha` is removed from both, and the serializations
    `json.dumps(x, sort_keys=True, separators=(",", ":"), ensure_ascii=False)`, encoded as UTF-8, are compared byte
    for byte. It exits 0 on equality and 3 otherwise. When the committed file is absent from the checked-out tree it
    prints `{"replay":"not-applicable"}` and exits 0.
  - At S1 the committed file is absent (`E` adds it), so B6 is `success` with "not-applicable". At `E`, control R
    requires the file, so "not-applicable" cannot arise there.
  - `parameters.dispatch_sha` is removed because B4 records the dispatched commit, so `E`'s fresh output and S1's
    committed output always differ in it.

**Common.** No step continues on error, masks a status or installs a package. Every interpreter the splice starts
(A3, A3b, A5, A7, A8, A9, A11, B3b, B4, B6) is `python3 -I -S -B`, so no `.pth` or other startup file runs in any step,
including A11 with `GH_TOKEN` set (r12 N2). Both scripts are stdlib-only. `pull_request` and `push` runs never reach
job B: its job-level `if:` is false for them, so the job is `skipped` before the Environment is consulted, and no
deployment is created (verified at the design run, precondition 6).

**Enforcement, in order (owner decision c.6726548830, item 4; r10 review, overall design).**
1. **Primary: the Environment gate.** Every decisive execution of the frozen splice happens in job B, and job B starts
   only after the required reviewer (the owner's identity fixed by E-ID, precondition 2b) approves its deployment to
   `arp3-qc22-decisive`, on a ref the Environment's
   deployment-branch policy admits. This holds before `F`, during execution, before landing and after it. On `main`
   it holds because `main` is outside the policy, so job B is refused there.
   - Its settings are frozen (precondition 2a), read at S1 and `E` (control N), and tested before `F` (gate tests,
     precondition 6″).
   - **Its reach is runs of the frozen splice** (r10 N2). A workflow that is modified, or that omits `environment:`,
     is not gated by it.
   - **Its reach in identity is every account but the reviewer's (r11 B2).** Under E-ID option (iii) the reviewer
     is `amaybaum`, the credential the session holds. Against that credential, approval and Environment edits are
     held back only by the owner's procedural commitment, not by the host. Under (i), the host refuses that
     credential's approval, and its edits remain procedural, detected by control N's timestamps if they persist.
     Under (iv), the same holds for approval, and edits depend on the session identity's permissions. Under (ii), the
     agent proxy would refuse both. GT-7 tests only the approval half, and the MCP connector is outside the rule
     (r12 N4).
2. **Defence in depth: the in-tree keys.** These are:
   - job B's job-level `if:`;
   - B3;
   - the workflow keys in B4 and B6;
   - the checker's three keys and the builder's own refusal;
   - controls W and B, with M-GUARD.

   They make a run of the frozen splice compute nothing of F1 on any path the gate might miss, for example if the
   Environment were deleted and then re-created without protection by a later dispatch. Control B's claims are
   scoped to exactly what it checks (*Scripts*).
3. **Detection: the enumeration and VOID.** A modified workflow on another branch, or one that omits `environment:`,
   is outside both 1 and 2. Up to the final capture before landing, the enumeration (*Runs, evidence, approvals*)
   catches every such run that carries the pinned checker blob or the frozen job or step names, under **any** event:
   - a dispatch: whole history;
   - any other event: from `T0`.

   Any such run that is not an approved or gate-test entry, and is not a recorded fixture-mode run, is a violation, and
   the round halts VOID. This holds even if the run passed both the in-tree keys and the gate.

**References to steps elsewhere in this file.**
- "Step 3" means B4 (the decisive decision) where a decisive run is meant, and A3 where fixture output is meant.
  "Step 8" means B6.
- "Steps 5, 7" mean A5 and A7; "steps 8–10" mean B6, A8 and A9, and `t_810` sums A8 and A9 (B6 counts 0); "step 11" means A10.
- The host-VOID rule and the run-at-a-stage rules concern job B.

**Which steps can compute the F1 family (re-review r6 B1, r9 B1, N7).**
- **B4**, only when all of these hold together:
  - the Environment approved job B's deployment, on a ref the policy admits;
  - job B's condition: a dispatch, attempt 1, `arp3qc22_decisive` true;
  - B3: the run's commit equals the dispatch input, and the tree has no receipt;
  - the workflow keys in B4's expression;
  - the checker's three keys;
  - the F1 builder's own refusal check passes.
- **B6** runs only under the same workflow keys, and compares canonical JSON only (B6's comparison).
- **A3** runs fixture mode by its literal `--event fixture`, and A3b records that mode as a step conclusion.
- **A5** (`--stress`) decides only the stress fixtures, the frozen fixtures and CC-F0.
- **A3b, A7, A8, A9 and A10** compute nothing of F1. Control B's name rule and the builder's refusal guard this.

**Scope of this guarantee (N7; r10 N2).** No run of the frozen splice and the pinned checker, at any commit, computes
F1 or any F1-dependent output unless both of these hold:
- it is an owner-approved, first-attempt, gated dispatch whose commit is the approved one;
- the tree carries no receipt.

Two things are outside every in-tree mechanism and outside the gate:
- a modified workflow, or a modified checker, on another branch;
- a local run of the public code, which is public from S1's push.

For the first, the enumeration detects every run that carries the pinned blob or the frozen names, under any event,
up to the final capture (*Enforcement*, item 3). A modified checker with a different blob, renamed jobs and steps,
and a local run are not attributable from host records. The claim that F1 was computed once, under approval, is
scoped to the pinned checker accordingly.

**No automatic replay.**
- B6 runs only under the workflow keys. At `E` the only replay is the owner-approved `E` dispatch.
- `replay` recomputes nothing: it reads the fresh B4 output and the committed file, and compares them as canonical
  JSON with `parameters.dispatch_sha` removed from both (r7 N2; R13-B1).
- In a dispatch the decisive computation is B4's alone, which the timeout test's `14·W_max` term covers.

**After merging to `main` (owner's restated requirement 3; c.6726548830, items 2 and 4).**
- **On `main`.** A dispatch with `arp3qc22_decisive` true is refused by the Environment, because `main` is outside the
  deployment-branch policy. Even past the gate, B3 would fail on the receipt, and B4's receipt key would select
  fixture mode. A push or a dispatch without the input skips job B, and job A is green, so later rounds' `F` and `E`
  attestations are unaffected.
- **At pre-`Q` round commits** (S1, `E`, a `Λ`, or a branch made from one). A gated dispatch on the round branch
  waits for the owner's approval, and none is given outside the approved entries. A dispatch on any other branch is
  refused by the policy. These were the two landing gaps of r10.
  - **For runs of the frozen splice and every account other than `amaybaum`,** both are closed by prevention.
  - **For `amaybaum`'s credential, which the session holds,** approval and Environment edits are held back by the
    owner's procedural commitment (precondition 2a), not by the host. E-ID (precondition 2b) records which of its
    options narrows this (r11 B2).
- **Re-establishing the claim later (§A.42 item 7)** is a dispatch at `E`, made deliberately. It passes through the
  same gate, needs its own recorded owner approval, lies outside this round, and changes no token. Its ref is a
  branch at `E` that the owner adds to the deployment-branch policy after Q-C2-2 closes, since the policy admits only
  the round and gate-test branches and the Environment is unchanged until then (precondition 2a; R14a-N5).
- **What remains.** After the final capture no enumeration runs. A modified workflow on another branch after that
  point is neither prevented nor detected by this round. This is the scope limit stated above, and it is not a
  landing gap of the frozen splice. F1's output is public from `E`, and the landed record is protected by the
  receipt's immutability (`G13`).

**The window between `E`'s capture and `Q`'s push.** Reconciliation commits (`Λ`) carry no receipt.
- **A gated dispatch on one** waits for the owner's approval, which is not given. B3 also requires the input to
  name that commit.
- **Final capture.** `verdict`'s capture, and a final capture `controls.py order --final` taken immediately before the
  round PR lands, both enumerate to their capture time.
- **Its record.** The final capture's record (structured JSON with its sha256) is posted on the round PR. The claim
  that no unapproved checker-bearing run occurred between `E`'s capture and landing uses it, and no round tree can
  hold it; its disposition under §A.42 item 8 is the owner's (precondition 2; R14-Rb2). The claims up to `E`'s
  capture rest on `E`'s `order.json` and the receipt.
- **Violations.** An unapproved checker-bearing run in either capture is a violation. The round does not land, and the
  owner is told that it is VOID.

**Cost after landing (r7 N3; r9 B1).**
- Every later pull request, push and ordinary dispatch on the repository runs job A, costing about the design run's
  measured job-A time.
- Job B is skipped and costs nothing.
- Any further change belongs to a successor change outside the round (§A.40).

**A latent route (r7 N4).** No `workflow_call` trigger exists in `verify.yml`. Adding one would let a caller's
`workflow_dispatch` reach job B's condition as `github.event_name`, so it would be a route into decisive mode. The
Environment would still gate that route, because it gates the job. Any such
change after landing is outside the round and must account for this guard.

**Design, confirmation, S1 and `E` trees.** Control W makes the workflow identical across all four.
- **The design run's tree** equals S1's apart from the record files. Its job B is `skipped`. Its step 7 records rather than compares, because
  the preregistration's stress pin is still an unbackticked `PENDING` field there. `stress-check` reads the pin from
  the tree and enforces the schema and certificates in either case.
- **The confirmation run (6′)** is the exact S1 tree, apart from the record files listed in precondition 6′. Its
  `verify.yml` is byte-equal to the frozen splice, and its step 7 compares against the final pin.
- **At S1 and `E`** the tree is exactly as frozen.
- **Synthetic merges (R13-N9).** The design run and 6′ are `pull_request` runs, which execute the host's merge of the
  pull request's head into its base, not `head_sha` itself. Each of their pull requests therefore has as its base a
  branch held at `D`, and its head descends from `D`, so the merge's tree is `head_sha`'s tree. `check --freeze`
  verifies this from the run record (schema `arp3-qc22-run`): its `pull_requests` entry has base `sha` equal to `D` and
  head `sha` equal to the run's `head_sha`. A record without that entry fails the check; whether the host fills it is
  first seen in the design run's record.

## Runs, evidence, approvals

- **The run at a stage.** The `workflow_dispatch` run of `verify.yml` whose `head_sha` is that stage's commit, dispatched
  with `arp3qc22_decisive` true and `arp3qc22_sha` equal to that commit, at attempt 1. It is read by `derive-run` from
  the runs and jobs APIs (every page). Its artifacts' `digest`s come from the artifacts API, never from a log
  (§A.44). A `digest` is the sha256 of the uploaded zip archive, not of the file inside it (HF-1); it is recorded as
  provenance, and no condition compares it with a file's sha256 (R13-B2).
- **Approval entries, keyed on `(run_id, run_attempt)` (re-review r7 B1, r9 B4(a); c.6726548830, item 4).** Each
  decisive dispatch (S1, `E`, or a retake after a host VOID as defined below) has its own entry:
  `{run_id, run_attempt, head_sha, stage, approval_comment_id, approval_created_at, approval_updated_at, approval_author, quoted_words, review}`.
  - **Where the entries are (R13-B4).** The entries for the decisive dispatches made before `E` is committed are
    `evidence/approvals.json` (schema `arp3-qc22-approvals` v1), committed at `E`. The entries of the dispatches at
    `E`, the `E` dispatch and any retake of it, cannot be in `E`'s tree: `verdict` builds one for each `E`-stage
    approval comment id given as an argument, verifies it as below, and prints it in its record (R14-N2).
  - **The prior authorization.** `approval_comment_id`, `approval_created_at` and `quoted_words` are the owner's
    comment on the round PR authorizing the dispatch.
    - The quoted words name the full commit id and the stage.
    - The comment precedes the run's `created_at`.
    - No comment is reused.
    - The comment is read through `GET issues/comments/{DEC}` (R13-B4).
  - **The edited-comment rule (R13-B4; Q-C2-1 r14's wording).** `approval_updated_at` must equal
    `approval_created_at`, or precede the run's `created_at`. A comment edited after its run is a violation, and the
    round halts VOID.
  - **Authorship.** `approval_author` must be `amaybaum`, with author association `OWNER`. Under E-ID (i)–(iii),
    where the session holds `amaybaum`'s credential, host records cannot tell the owner's comment from one posted
    with it (H22; the identity limit, *Scripts*; R14-N1).
  - **The deployment review** (`review`). It is read from `GET actions/runs/{run_id}/approvals`. The entry holds
    exactly one review, with all of these:
    - `state: "approved"`;
    - `user.login` equal to the reviewer identity E-ID fixes (`amaybaum` under (ii), (iii) and (iv); the second
      account under (i); R13-N7);
    - `environments` exactly `["arp3-qc22-decisive"]`;
    - `comment` exactly `ARP-3-QC22 <stage> <full commit id>`, naming the same stage and commit as the quoted words.
  - **Binding the review to the run (the owner's words: "the exact approved commit, run identity, inputs, and
    approval").** For the run that attests at each stage, all of these must hold (R14-N2):
    - the run's `head_sha` equals the commit in the review comment;
    - job B's B3 is `success`, so `github.sha` equals the `arp3qc22_sha` input;
    - at S1, the committed measurements' `parameters.dispatch_sha` equals S1 (at `E`, B3's `success` binds the input);
    - job B ran, so the `arp3qc22_decisive` input was true;
    - the run's `run_attempt` is `1`.
  - **The entry of a host-VOID run** that a retake replaces holds when its prior authorization, the edited-comment
    rule and its authorship hold, its run is a host VOID as the *Stop rule* defines it, and any review it carries is
    the reviewer's and names its stage and commit. A run voided by a rejection or an expiry has no approved review,
    and its B3 need not be `success` (R14-N2).
  - **The deployment record.** Every deployment in `GET deployments?environment=arp3-qc22-decisive` (every page) maps
    to exactly one approved entry or gate-test entry, by its `sha` and by the run id that its statuses' `target_url`
    or `log_url` names.
    - A deployment that maps to neither is a violation.
    - The gate tests record the exact fields that carry the run id (precondition 6″), and the mapping uses only
      those fields.
  - **Order (r11 N5).** The documented approvals record carries no time, and a `waiting` status occurs even
    without any review (r11 H20). So the review's time is bounded by the deployment's statuses: after its
    `waiting` status, and before its first `queued` or `in_progress` status after that. The run's `created_at`
    precedes `waiting`. The gate tests record the actual status sequence.
  - **Re-runs (c.6726548830, item 3).** A re-run attempt never attests. "The run at a stage" is attempt 1 alone.
    - In attempt `≥ 2`, job B's job-level `if:` is false, so job B is `skipped` before the Environment is consulted.
    - `derive-run` reads every attempt.
    - An attempt `≥ 2` of an approved dispatch whose job B is anything but absent or `skipped` is a violation, and
      the round halts VOID.
    - A re-run that computes nothing is recorded and ignored. It cannot repair a red attempt 1, and the stop rule
      applies to attempt 1 as it stands.
    - Whether the host would ask for approval again on a re-run of an Environment-gated job is not relied on and was
      not verified (r10 N2).
  - **Gate-test entries** (precondition 6″) are the only other checker-bearing dispatches admitted. Each carries:
    - its frozen expectation;
    - its review record, if any;
    - the conclusions of job B and of B3 and B4;
    - in every gate-test entry, B4 must be absent or `skipped`. A gate-test run in which B4 ran is a violation.
- **`order.json`.** `F`'s designation precedes the first execution run. The owner's designation comment is read
  through `GET issues/comments/{DEC}`, its id given as an argument; its `created_at`, and its `updated_at` under the
  edited-comment rule, precede the first execution run's `created_at`. `order.json` records its id, author and times
  (R13-B4).
- **Repository-wide run enumeration (r7 B1, r8 B2, r9 B3; r10 B3, N1, N3, N4).** `order.json` enumerates two sets:
  - **(1)** every `workflow_dispatch` run of every workflow in the repository, over `[T_repo, capture]`;
  - **(2)** every run of every workflow under every other event, over `[T0, capture]`.

  Both cover every branch and ref and every attempt. **Every listed attempt is read, but only a checker-bearing
  attempt can be a violation** (r10 N1). Old dispatches of other workflows are read and cannot match.
  - **`T0` bounds set (2) (r11 N8).** No run created before `T0` can be checker-bearing, re-run or not, because a
    re-run uses the run's original `head_sha`, provided no commit carrying the pinned blob or the frozen names
    predates `D`.
    - **The check.** Every capture checks it for the recorded branches: every commit on them that carries the pinned
      blob or the frozen names descends from `D` (`git merge-base --is-ancestor --end-of-options D <commit>`).
    - **Residual.** A draft pushed before `D` on some other branch, under a non-dispatch event, falls outside set
      (2). This round does not check whether such a draft exists (R14-Rb2; R14a-N7).
  - **The queries.** Each is `GET actions/runs?<event filter>&created=<a>..<b>&per_page=100`, paginated to the end. Set
    (1) uses `event=workflow_dispatch`. Set (2) lists without an event filter, and drops `workflow_dispatch` runs,
    which set (1) holds.
    - The slices are disjoint at one-second granularity (`a..b`, then `b+1s..c`). Their union is recorded to equal the
      set's window, where `T_repo` is the repository's `created_at` from `GET` on the repository.
    - `total_count` is read from page 1 and must be the same on every page. The listed count must equal it, and it
      must be below 1,000 (r9 N2). A slice that fails this is split, and the split is recorded.
    - Runs are deduplicated by `id`.
    - `order.json` records every query, its window, its `total_count` and its listed count.
  - **Run numbers (R13-N18).** For each workflow, the `run_number`s of the runs created in `[T0, capture]` (sets (1)
    and (2) together) must form one contiguous range. A gap is reported to the owner and halts the stage, as an
    unreadable tree does. Whether `run_number` is gap-free without deletion is unverified host behaviour, so the check
    applies only if GT-8 (precondition 6″) found every range contiguous.
  - **Attempts and jobs (r10 N3).** For every listed run, every attempt from 1 to `run_attempt` is read through
    `GET actions/runs/{run_id}/attempts/{n}` and its jobs through `GET actions/runs/{run_id}/attempts/{n}/jobs?per_page=100`,
    every page. The `filter=all` endpoint (`/runs/{id}/jobs`) is not used.
  - **Identification, conservative (r9 B3(a)–(c)).** An attempt is **checker-bearing** if either of these holds. Its
    step and job conclusions are not consulted.
    - **(i) By name.** Any of its jobs has the display name `Numerical probes / ARP-3-QC22 exact decision (gated)` or
      `Numerical probes / ARP-3-QC22 fixtures and stress`, or contains a step named "ARP-3-QC22 exact decision".
    - **(ii) By blob.** Its `head_sha` tree carries the pinned blob of `qc22_check.py` at any path. The tree is a
      function of `head_sha`, so it is read once per distinct `head_sha`, and that covers every attempt of every
      listed run.
  - **Reading a tree (r10 B3).**
    - From the local object store when `git cat-file -e` finds the commit (`git ls-tree -r`).
    - Otherwise from `GET git/trees/{head_sha}?recursive=1`, requiring `truncated == false`. On truncation, the tree is
      walked subtree by subtree with the non-recursive form.
    - `order.json` records the source (`local` or `api`) for each `head_sha`.
    - A tree that cannot be read (a 404, or any other failure) makes the capture **failed**, to be retried. It is never
      "not checker-bearing". A tree that stays unreadable halts the stage, and is reported to the owner.
  - **The rule.** Every checker-bearing attempt must be one of these:
    - **(a)** an approved entry's attempt 1, matched on `(run_id, run_attempt)`;
    - **(b)** a gate-test entry;
    - **(c)** an attempt `≥ 2` of (a) or (b) whose job B is absent or `skipped`;
    - **(d)** a non-`workflow_dispatch` attempt whose `head_sha` is a commit of a recorded branch, satisfying the
      no-unapproved-F1 rule below. The recorded branches are the round branch, the design branch, the confirmation
      branch and the gate-test branch, whose commits since `D` are listed in `order.json`.

    Any other checker-bearing attempt is a violation, and the round halts VOID. That includes any checker-bearing
    attempt at a commit outside the recorded branches, under any event, and any checker-bearing dispatch that is not
    an approved or gate-test entry.
    - This VOIDs nothing legitimate. The round's trees are dispatched only at `F` (which carries no checker and has
      neither job), at S1, at `E` and at the gate tests.
    - **The design and confirmation branches are never dispatched.**
  - **The call budget (r10 N4).** One capture costs about:
    - the listings;
    - one call per attempt for the attempt record, and one per jobs page;
    - one trees call per distinct `head_sha` absent locally;
    - a few calls for the Environment, approvals and deployments.

    An estimate, which no condition uses, is about 770 calls for set (1) (r10 review §3, H11–H15), plus set (2)'s
    runs since `T0`, at about 100 runs a day on this repository (a read-only count, 2026-11-08; R14-Rb2). There are
    three captures (`check --stage S1`, `verdict` and `order --final`), each recording its own call count.
    - A rate-limit response (403 or 429 with an exhausted limit) or a 5xx makes the capture **failed**, to be retried
      after the reset. It is never a pass and never a VOID.
    - Set (2)'s size is measured at the first capture. If one capture would exceed one hour of the token's limit, the
      stage stops and the owner is told; no capture is shortened.
  - **Residual (stated).** A deleted run cannot be enumerated. The owner's decision c.6726548830, item 1 ("No CI run
    deletion until Q-C2-2 closes") covers this. `T0` is also its anchor: `D`'s host time, the `timestamp` of the entry
    with `after = D` in `GET activity?ref=refs/heads/main` (`pr_merge` or `push`; r9 N4). Its value: PENDING.
- **The no-unapproved-F1 rule (re-review r6 B1; §A.44).** For every non-dispatch checker-bearing attempt at a
  recorded-branch commit, `order.json` records:
  `{run_id, run_attempt, head_sha, event, jobB_conclusion, B4_conclusion, A3_conclusion, A3b_conclusion, fixtures_artifact_digest}`.
  These are read from the jobs API. `fixtures_artifact_digest` is the artifacts API's `digest` field, recorded as
  provenance and read by no condition; no artifact content is downloaded (R13-B2). The rule holds exactly when, for
  every such attempt:
  - job B is absent or `skipped`;
  - B4 is absent or `skipped`;
  - A3 is absent or `skipped`, or A3b's conclusion is `success`, so A3's output had `mode: "fixture"` with the
    synthetic placeholders (R14a-Rc1).

  An A3 that is absent or `skipped` started no checker process in job A: A1 and A2 run none, and every later step
  whose `if:` has no status function, which implies `success()`, is skipped with it, A5, A8, A10 and A11 included,
  while A3b, the one `always()` step, runs `controls.py` only. So a failure before A3, of the checkout, of
  `setup-python` or of the runner, and a job A that never started, are not violations. Nor is a red A3 whose output
  is complete fixture-mode output, such as a design-branch fixture mismatch (A3b runs `always()`; R14-N10). A
  non-dispatch checker-bearing attempt at a recorded-branch commit whose A3 ran, or was cancelled, and whose A3b is
  not `success`, because A3's output is missing, incomplete or not fixture mode, is a violation: an A3 timeout or
  crash, for example.
  - **Residual (stated; R14a-Rc1).** Such an attempt cannot be told from one whose A3 computed F1, so it stays a
    violation, which voids the round with no retake. Its mitigation is the executor precondition below. What remains
    is a runner-side timeout, crash or cancellation of an A3 whose command completed locally.
  - **Executor precondition: no push without a local fixture run (R14a-Rc1; §A.41).** No commit carrying the checker
    is pushed to a recorded branch, as that branch's head, unless A3's command, run locally on that commit's tree with
    Python 3.11, has completed within `timeout-minutes` and `controls.py fixture-mode-check` exits 0 on its output.
    The executor cancels no run on a recorded branch while its job A runs.

  `verdict` re-checks the rule on a fresh capture. A violation is a failed check, and the round halts VOID.
- **Retention (r7 N1).** Every upload carries `retention-days: 90`. `controls.py check --stage S1`, run before the S1
  dispatch, also captures the rule's records for every run then existing: the enumeration and the non-dispatch
  records. It prints them, and the executor redirects them into `evidence/order-s1.json`, which is committed at `E`
  (R13-B5).
  - The no-unapproved-F1 rule reads no artifact, so a missing artifact is not a violation. `order-s1.json` keeps each
    record's `fixtures_artifact_digest` as provenance (R13-B2).
  - The S1 binding reads S1's measurements artifact at `verdict`. If it has expired or been deleted, the binding
    fails and the round halts VOID, so `verdict`'s capture falls within 90 days of S1's run (fail-closed; draft
    default, pending the owner's ruling in precondition 2; R14-Rb3).
  - S1's artifact is support for the binding when it is read, and provenance after it expires. The enduring support is
    `E`'s committed measurements, the binding's record at `E` and a dispatch at `E` (§A.42 item 7; R14-N6).
- **`verdict`.** It prints `VERDICT <token>` only when all of the following hold. Otherwise it prints `VERDICT VOID`
  and exits 1.
  - every check at `E` passes, control N included (under E-READ (a), through A11's conclusion in the S1 and `E`
    runs);
  - in attempt 1 of the runs at S1 and `E`, every job's conclusion is `success`, every step of job B is `success`
    (B6 included, at S1 with "not-applicable"), and every step of job A is `success` (A3b, A7 and A10 included, and
    A11 under E-READ (a)). The run's own conclusion is `success` (r10 N5).
  - every approval entry holds as stated for its run, the run that attests at its stage or a host-VOID run a retake
    replaced, the entries `verdict` builds for the dispatches at `E` included (R13-B4; R14-N2);
  - B6 at `E` is `success` and its replay result is a match, which binds the committed measurements to the approved
    decisive computation (R13-B1);
  - **the S1 binding** (R13-B2; Q-C2-1 r14's wording). `verdict` reads S1's measurements artifact and compares it with
    the committed file:
    - `GET actions/runs/{DEC}/artifacts` for S1's run (every page) must list exactly one artifact with B5's frozen
      name, `arp3-qc22-measurements` (R14-N3), whose `workflow_run.id` is S1's run id and whose
      `workflow_run.head_sha` is S1;
    - `GET actions/artifacts/{DEC}/zip` returns its archive as bytes, whose sha256 must equal the artifact's `digest`
      (`sha256:` followed by the hex digest);
    - the archive is opened in memory, `zipfile.ZipFile(io.BytesIO(<bytes>))`; its member list must be exactly
      `["measurements.json"]`, and that member is read;
    - it is compared with the committed `evidence/measurements.json` by B6's comparison, `parameters.dispatch_sha`
      removed from both;
    - **the binding's record at `E`** (§A.42 items 2, 7 and 8; R14-N6; Q-C2-1 r14a's wording): `derive-run`, run on
      S1's run before `E` is committed, records in `evidence/s1-run/results.json` the binding's inputs, the
      artifact's `id`, `name`, `digest`, `workflow_run.id`, `workflow_run.head_sha` and `expires_at` and the
      archive's member list, read in memory as above; `verdict`'s own read must equal that record.

    A failed condition, including an artifact that is missing, expired or unreadable, fails the binding (fail-closed;
    for an expired or deleted artifact, draft default, pending owner ruling, precondition 2). A rate-limited or 5xx
    response is a failed capture, retried. No file is written;
  - the note's token line equals the token.

  A red job elsewhere in attempt 1 is therefore a failed `verdict` condition. A re-run cannot repair it (c.6726548830,
  item 3), and the round halts VOID.

## Stop rule (halt-only)

**Host VOID, defined (re-review B3(d); by conclusions, r9 B3(b)).** A host VOID is an approved dispatch in which B4
never ran. In attempt 1's jobs records of the job named `Numerical probes / ARP-3-QC22 exact decision (gated)`, that
means one of:
- the job is absent;
- B4 is absent;
- B4's `conclusion` is `skipped`.

That covers a deployment the host rejected or let expire, a ref the policy refused, and a B3 failure.

`started_at` is not used, because skipped steps carry one. A host VOID may be retaken only by a **fresh** dispatch: a
new `run_id`, at attempt 1, under a recorded owner decision made after the void-run record and its sha256 are posted,
with its own approval entry. A re-run attempt is never a retake.

**Checker outcome.** Any of the following is a checker outcome, not a host VOID:
- a timeout, cancellation or crash in a run whose B4 ran: a B4 conclusion other than `skipped`, or a missing
  conclusion on a job B that timed out;
- any `out_of_scope`;
- any exit status other than 0.

A checker outcome halts the round with VOID, with **no retake, no re-run and no budget change**.

The round halts under `S12` on any of the following:
- a failed `check` at S1 or `E`;
- at S1, any checker outcome other than exit 0 with complete output;
- at `E`, a failed control, a checker outcome, a replay mismatch, a failed S1 binding (for an expired or deleted
  artifact, draft default, pending the owner's ruling in precondition 2; R14a §2), or a `verdict` VOID arising
  from the checker;
- a host VOID without a recorded retake decision;
- any need to change the control plane after `F`. This includes any narrowing of a fragment or completion, any
  change to `P_max`, `B_max`, `W_max`, the caps, `timeout-minutes` or the stress pin, and any addition of a fragment,
  completion, control or premise.

**After `F` (c.6724832474).** No opportunistic narrowing and no additional computational budget is admissible.
Undecidable cases receive the preregistered VOID. No checker rerun is preregistered. A substantive token is not a halt.

**At a halt.** `W` restores `verify.yml` to `F`'s state and keeps the record. It adds the S1 artifact when one exists,
preserved as produced, the run or void-run record, `order.json` and the VOID note. Progression to ARP-4 stops.

## Invariants and their checkpoints (§A.41)

| invariant | checkpoint |
| --- | --- |
| rule, fragments, completions, controls, texts, ledger and budgets fixed before any decisive computation | `F` designated before the first execution run (P on `order.json`); checker blob, `P_max`, `B_max`, `W_max`, `timeout-minutes` and the stress pin frozen at `F` (B, P, W); self-tests never build F1 under `G_SM` |
| instance-specific: `G_SM`, P★, carrier site 0, `g` at `τ = 3` | IS-RULE, IS-PSTAR, CC-OFF, C-EVAL; no `G_σ` code |
| the read evaluator can detect a nonzero `g`-dependence | C-EVAL (ii); M-EVAL |
| certificate validation is independent of the decision procedure (c.6724832474) | C-INDEP (AST); the verifier re-derives `N` and checks `A Bᵀ = N` and the ranks; it re-enumerates the facets; M-INDEP (direct, default-argument and closure variants), M-FACTOR, M-SOLVER; C-INDEP covers the whole `FunctionDef`, and a runtime type check guards the non-JSON inputs |
| a mutated certificate fails, in each direction | M-W (infeasible side: GBIT, DUAL, POS-1, H3); M-MODEL (feasible side: steps 2, 3 and 4); M-FACET on step-4 fragments |
| the caps count extreme rays, every removal is certified, and every enumeration is bounded (R14-Rb1) | step 1b's removal certificates, checked in order by the verifier on both sides (C-CERT, C-SYM); M-RAY; the caps on `n`, `C(n, d − 1)` and C-SYM's `C(E, d − 1)`, each a recorded `out_of_scope` when exceeded; the *Caps* fit for every frozen fragment, with fixture mode exiting 3 on any `out_of_scope` |
| every method step's certificate path is exercised | step 1b: GX+R-Y, on both sides; step 2: NEG-2, POS-2 and others; step 3: ZPT, X+RU′; step 4 infeasible: GBIT, DUAL, POS-1, H3; step 4 feasible with `T = 0`: F10; step 4 feasible with `T > 0` (phase-1-dual extraction of `t`): Q+RY (`m = 6`, `T = 5`; step 3 finds no model) |
| no reading beyond the measured conjunctions | the token is the LP verdict and the restoring set; derived and access fields reported beside it; S4 |
| `g`-specificity tested without a misleading negative, marginal or conditional (c.6724832474) | R-Uc and `g_specific := RY ∧ ¬RUc`; `g_eta`; fixtures G (specific), X (not specific; RUP), Q (conditional; specific and `g_eta`); a "no" rendered as a test result with its frozen caveat, never as independence, with GX (two causes; NONE) as its control |
| completions attributed separately | separate verdicts for R-G, R-U′, R-Uc, R-Y and R-S; the token alphabet |
| restricted reads and restricted preparations both detectable | GBIT (RG), DUAL (RY) |
| every token family reachable by a real fixture | IMITABLE: POS-2, NEG-1, NEG-2, CC-F0, F10, ZPT; CONTEXTUAL-RG: GBIT; CONTEXTUAL-RY: DUAL, H3, G; CONTEXTUAL-RUP: X; CONTEXTUAL-RUP+RY: Q; CONTEXTUAL-RS: SW (decision path only; N4); CONTEXTUAL-NONE: SW−, GX; VOID: M-BUDGET and the self-tests |
| a budget overrun is a recorded VOID, never a crash, a timeout retake or a re-run | the deterministic `P_max`/`B_max`/`W_max` with the mechanical freeze rule; the timeout test; C-BUDGET; M-BUDGET; the host-VOID definition; the stop rule |
| the stress figures are structured | `stress.json` (schema v2), uploaded on every event; step 7 (`stress-check`) as a step conclusion, enforcing the schema and certificates on every tree; its sha256 pinned and bound by A7's `success` at 6′; the archive `digest` is provenance (R13-B2) |
| the final configuration runs before `F`, and the frozen fixture expectations are the writer's own computation before `F` | fixture mode exits 3 on any mismatch; precondition 6′'s confirmation run of the exact S1 tree (record files aside), with the final budgets and pin, its run id and record pinned |
| **F1 is computed, by the frozen splice and the pinned checker, only in an owner-approved, first-attempt, gated dispatch at the approved commit, on a tree without the receipt** (re-review r6 B1, r9 B1, N1, N7; r10 N2; c.6723329527, c.6726548830 item 4; §A.43 item 4) | primary: the Environment gate (`environment: arp3-qc22-decisive`; frozen settings, precondition 2a; reader, identity and binding, precondition 2b; control N at S1, `E` and `verdict`; gate tests GT-1 to GT-7 as applicable, precondition 6″). Defence in depth: job B's `if:`; B3; the workflow keys in B4 and B6; the checker's three keys and refusal without `--event`; A3's literal; the builder's own refusal; control W's whole-file check, with removal self-tests; control B's node-form rules; M-GUARD (BYP-1 to BYP-21, BYP-23 to BYP-26, ZIP-1 to ZIP-3 and the unnumbered variants); the marker A10; the no-unapproved-F1 rule; `mode = "decisive"` and placeholder invalidity in `decide` (M-MODE); `order-s1.json` against artifact expiry. Scope: runs of the frozen splice and the pinned checker |
| **(owner requirement 1) an unapproved `workflow_dispatch` cannot bypass authorization** — **prevented** for runs of the frozen splice by the Environment gate, for every account other than `amaybaum`; **detected and VOID** for a modified workflow that carries the pinned blob or the frozen names (r9 B4; r10 N2; r11 B2; c.6726548830 item 4) | the gate (as above); the deployment-review record bound to run, commit, inputs and stage, with every deployment of the Environment mapped to an entry; the enumeration: set (1) whole-history dispatches of every workflow, set (2) every other event from `T0`, disjoint sliced queries, `total_count` checks, every attempt, trees from the object store or the trees API with the source recorded, an unreadable tree a failed capture; checker-bearing attempts by name or pinned blob; rule (a)–(d), otherwise VOID; the final capture before landing; the no-deletion decision (c.6726548830 item 1). Unverified host behaviour (named): administrator bypass with `can_admins_bypass: false`; expiry of a pending approval. Identity qualification (r11 B2): prevented for every account other than `amaybaum`; against `amaybaum`'s credential, which the session holds, approval and Environment edits are held back by the owner's procedural commitment (precondition 2a), not by the host, except as E-ID (i) or (ii) narrows it (precondition 2b) |
| **(owner requirement 2) re-runs cannot repeat the decisive computation without fresh approval** — **prevented**; a re-run never attests (c.6726548830 item 3) | job B's job-level attempt key (skipped before the Environment is consulted; GT-4), the attempt key in B4 and B6, the checker's `GITHUB_RUN_ATTEMPT` key; retakes are fresh, separately approved dispatches; every attempt is enumerated, and an attempt `≥ 2` whose job B ran is VOID; `verdict` reads attempt 1 only. Whether the host itself re-asks approval on a re-run is not relied on |
| **(owner requirement 3) after merging to `main`, neither a push nor a new dispatch can silently execute F1** — **prevented** for runs of the frozen splice, on `main` and at pre-`Q` round commits, for every account other than `amaybaum` (c.6726548830 items 2 and 4; r11 B2) | on `main`: the deployment-branch policy refuses job B (GT-3), B3's receipt test and the receipt key; push and input-less dispatch skip job B; at pre-`Q` round commits: the Environment's required approval; the owner's commitment to keep the Environment unchanged until Q-C2-2 closes (precondition 2a). Scope limit (stated, not a landing gap of the splice): a modified workflow on another branch after the final capture is neither prevented nor detected. Identity qualification (r11 B2): prevented for every account other than `amaybaum`; against `amaybaum`'s credential, which the session holds, approval and Environment edits are held back by the owner's procedural commitment (precondition 2a), not by the host, except as E-ID (i) or (ii) narrows it (precondition 2b). On `main` the branch policy, B3's receipt test and the receipt key stop F1 whatever the approval, so this qualification bears only on pre-`Q` round commits |
| **(owner requirement 4) any violation is VOID even if the mathematics looks correct** | `decide`'s VOID conditions, the order rule and the stop rule; no token is printed over a violation, whatever the measurements |
| a recorded-branch attempt whose A3 ran leaves fixture-mode output, so that the no-unapproved-F1 rule does not void the round on a run that computed nothing (R14a-Rc1) | the no-unapproved-F1 rule's A3 and A3b conclusions, read from the jobs API, a failure being a violation; the NOF1 self-test; mitigation: the executor precondition *No push without a local fixture run*; residual named (a runner-side timeout, crash or cancellation) |
| 6′ is what it claims to be, and fragment decisions are stateless | `check --freeze`'s mechanical verification of `confirmation-run.json` (pin, conclusions including A3b and A7, blobs, splice, the pull request's base; R13-B2, N9), with the run re-derived from the host by its pinned run id, as the design run is (R14-N4); C-STATELESS at `E` |
| budgets cover every non-F1 fragment | the freeze rule's maxima over stress fixtures, frozen fixtures with completions, CC-F0 and self-tests |
| a scope cut never reads as a result | the RS-dropped forms of the common clause and of the NONE addendum; precondition 2's options; precondition 4's review of any narrowing |
| the Environment is what was frozen, at S1 and at `E` | control N against `env-pin.json` (with `id`, `created_at` and `updated_at`), read through the E-READ channel (precondition 2b): under (a), A11's in-job comparison as a step conclusion in the S1 and `E` runs; under (b) and (c), `check --stage S1` and `check --stage E` before each dispatch, S1's read kept in `order-s1.json`, and `verdict` (R13-B5); verified by GT-6; residual named (a change reverted between reads, unless GT-6b shows `updated_at` moves) |
| the gate works as frozen before `F` (c.6726548830 item 5) | gate tests GT-1 to GT-6, with GT-2b if E-BIND is adopted and GT-7 if E-ID (ii) is adopted (precondition 6″), recorded in `gate-tests.json` from the runs, jobs, approvals and deployments APIs |
| no floating point | C-EXACT, C-CERT; the floating-point basis is not adopted |
| the LP is right | POS-1/POS-2, NEG-1/NEG-2, C-NCF, C-SYM |
| no wrap; both sizes agree | IS-SIZE; size disagreement is VOID |
| hidden-prior scope named | the common clause's `{hidden-law sentence}` in its two frozen forms; A-N2; A-SWITCH's two entries; R-S when in scope |
| ADA cannot change the label | `decide` reads no ADA field; V regenerates; S4 |
| verdicts read structured data only | exit statuses; the jobs API, including the A3b, A7 and A11 step conclusions; `replay`'s exit status; S1's measurements archive through the artifacts API (the S1 binding, against its record at `E`, with the S1-BIND self-test; R14 §5, N6); the comments and approvals APIs. No condition compares an archive `digest` with a file's sha256 (R13-B2) |
| the run's output directory exists, and the replay compares the computation | `mkdir -p` in A3 and B4 (W); `replay`'s canonical comparison without `parameters.dispatch_sha`, with the REPLAY self-test (R13-B1, B3) |
| outputs do not depend on string-hash order, which `-I` leaves randomized | control B's no-`set` rule on `qc22_check.py`, with its M-GUARD variant; A7 at 6′ and the replay at `E` across processes (R13-N17) |
| a deleted run is detected where the host allows it | the run-number contiguity check, if GT-8 shows contiguous ranges; otherwise the no-deletion decision (c.6726548830 item 1) alone (R13-N18) |
| designations and approvals precede what they govern | the approval entries (`approvals.json`, and the entries `verdict` builds, one per `E`-stage approval comment id; R14a §2) and `F`'s designation, each read through `issues/comments/{DEC}` and checked against the run's `created_at`, with the edited-comment rule; `order`; `verdict`; the APPROVALS self-test (R13-B4) |
| execution changes only `verify.yml` and the record | `S7`, G, R, W |
| ARP-2 completed and reviewed before `F`; F1 run only on the owner's decision | preconditions 1–2 |
| the receipt holds; legacy records untouched | `--verify-round Q` prints `VERDICT  HOLDS`; `legacy_records_check.py` |

## Preconditions of `F`

1. **Sequence.** ARP-1 and ARP-2 have completed and been independently reviewed, recorded on #1169 (record ids,
   authors and times: PENDING). If ARP-2's result bears on this round, this file is revised and re-reviewed (the
   disposition: PENDING).
2. **Owner decisions, recorded with author and time** (record id: PENDING):
   - whether to run F1 at all, given that the literal check is predicted feasible on paper and decided in-run by
     CC-F0 (O-7; R14-Rb2);
   - O-1, the functional's reading (G-Y, G-H1 or G-H2);
   - O-2, the read class;
   - O-3, the supply class;
   - the incorporation of the accepted C2 audit and the consolidated package, with each bearing finding's
     disposition;
   - **Decided (c.6726548830, amaybaum, 2026-11-08T20:14:37Z; quoted in *Authority*).** These are recorded here and
     are not reopened:
     - **item 1:** no workflow run is deleted until Q-C2-2 closes. The enumeration's completeness holds relative to
       this decision.
     - **item 2:** the two landing gaps (a dispatch before landing, and post-landing dispatches at pre-`Q` round
       commits) are not accepted. They are closed by the Environment gate for runs of the frozen splice (*The
       workflow edit*, *After merging*).
     - **item 3:** a re-run attempt never serves as an attestation (*Runs, evidence, approvals*).
     - **item 4:** a GitHub Environment with the owner as required reviewer gates every decisive execution, after
       landing included (precondition 2a).
     - **item 5:** the freeze is conditional on an independent ACCEPT (item 4 below) and on verification of the
       complete gate (preconditions 2a and 6″).
   - **the scope of F1+R-S**, with both options kept (c.6724832474):
     - kept, only if SF-3 is decided and the timeout test passes with R-S;
     - declared `out_of_scope` by design (the owner's stated preference when it cannot be decided within the fixed
       budget);
     - narrowed, only by a revision of this file stating SF-3n, the scope and the controls, reviewed under item 4;
   - the floating-point basis proposal: named only; adopting it would need this decision and a revision of C-EXACT;
   - **paired completions** (for example R-Y+R-S, or R-Y+R-Uc), which would measure `g`'s contribution in the presence
     of a second cause (re-review r4 B1). They are not adopted. If the owner wants them, they are frozen before `F` by
     a reviewed revision of this file, and never added after `F`.
   - **Q12, modified workflows:** whether the scope limit stated in *After merging to `main`* is the reading of
     "must remain blocked, including after landing", or a measure outside the round is added (a ruleset on workflow
     files, the fork-workflow approval setting, or a later monitoring round). Each option acts outside this round's
     files, so the text here holds under each. Record id: PENDING.
   - **An S1 measurements artifact expired or deleted by `verdict`'s capture** (R14-Rb3; the same question as
     Q-C2-1's owner ruling R6). Draft default: the S1 binding fails and the round halts VOID (fail-closed), so
     `verdict`'s capture at `E` falls within 90 days of S1's run (*Runs, evidence, approvals*, *Retention*).
     Alternative: the binding is reported as not checkable, and the token stands with that limitation printed; the
     committed measurements are then bound to the approved computation by B6's replay at `E` only, not to S1's output
     (Q-C2-1 r14b's wording; R14a-N2). No frozen text renders that limitation, so the alternative is applied by a
     reviewed revision of this file before `F` (item 4). Record id: PENDING.
   - **§A.42 item 8 dispositions** (R14-Rb2; R14a-N3). The final capture's record, the `E`-stage Environment reads
     and the approval entries `verdict` builds for the dispatches at `E` are host-time records that no round tree can
     hold (*Off-`main` references*). The options are:
     - **a recorded owner exception** for each, naming the claim it leaves unsupported (§A.42 item 8). Such a claim
       is not established (§A.46 item 1);
     - **narrowing.** The landed record states those checks only as conditions of landing: the round lands only if
       they pass. It does not state that they passed, and their records are provenance.

     **What each option leaves of the token.** Under either option, the token's scientific content, F1's verdict as
     replay-matched at `E`, is re-established from `main` by a dispatch at `E` (§A.42 item 7). The governance claims,
     that the dispatches at `E` were approved, that the Environment at `E` was as frozen, and that no unapproved
     checker-bearing run occurred between `E`'s capture and landing, are left not established under an exception,
     and are not claimed under narrowing.

     **Applying the choice.** Filling the record id changes no text. The chosen option is applied before `F` by a
     reviewed revision of this file (item 4), which revises every passage that states these properties: control
     N's stage reads (*Scripts*); *Its record* (*The window between `E`'s capture and `Q`'s push*); *Where the
     entries are* (*Approval entries*); the invariant rows on F1's computation, on owner requirements 1 to 3, on the
     Environment at S1 and `E`, and on designations and approvals; and the row on these records in *Off-`main`
     references*. Record id: PENDING.
2a. **The Environment (owner action before any commit carrying the splice is pushed; c.6726548830, item 4).**
   - **Who creates it.** The owner creates it. The session cannot change repository settings, and it makes no
     settings write.
   - **Its settings (frozen):**
     - name `arp3-qc22-decisive`;
     - exactly one `required_reviewers` protection rule, whose only reviewer is the identity E-ID fixes
       (precondition 2b): the user `amaybaum` under options (ii), (iii) and (iv), and the second account under (i);
     - `prevent_self_review` as E-ID fixes it: `true` under (i) and (iv); `false` under (ii) and (iii), where the dispatching
       account and the reviewing account are the same, so `true` would refuse every approval;
     - no `wait_timer` rule;
     - no custom deployment protection rule;
     - `can_admins_bypass: false`;
     - `deployment_branch_policy` `{protected_branches: false, custom_branch_policies: true}`, with exactly two policies,
       each of type `branch`: the round branch (name: PENDING) and the gate-test branch (name: PENDING).
   - **Why it must exist first.** If a job names an Environment that does not exist, the host creates it without
     protection when the job runs. So no ref carrying the splice is pushed before the Environment exists.
   - **The read (r11 B1).** It is made through the channel E-READ fixes (precondition 2b), never by a direct session
     `GET`, unless E-READ (c) is adopted.
     - The canonical JSON of the frozen fields, including `id`, `created_at` and `updated_at`, is
       `evidence/env-pin.json`. Its sha256 is pinned here: PENDING.
     - Under E-READ (a) the pin is the `env.json` file inside the `arp3-qc22-env` archive of an A11 run made after
       GT-6b, copied by the executor; A11 at S1 then checks it in-job against the live Environment (R13-B2; R14-N3).
     - Control N compares the reads at S1, at `E` and at `verdict` with it.
   - **Owner commitments recorded with the action** (record id: PENDING):
     - the Environment is neither edited nor deleted until Q-C2-2 closes. This is decision 4's "including after
       landing" made operational; whether it is kept after closure is the owner's;
     - every deployment review is the reviewer's own act, through the host's interface. The session never calls the
       review endpoint and never writes to the Environment. Under E-ID (iii) this commitment is the only thing holding
       back the credential the session holds (r11 B2). **The single exception** is GT-7, if E-ID (ii) is adopted and
       the owner authorizes it, with its frozen request body (precondition 6″; r12 N4);
     - **the session's second channel (r12 N4; r12 H25).** The session also holds the GitHub MCP connector, which
       bypasses the agent proxy. Its current schema has no review or Environment method, but it can dispatch with
       inputs, re-run, re-run failed jobs, cancel, and delete run logs. Through it, as through the proxy, the session:
       - makes no dispatch, re-run or cancellation without the recorded owner authorization each needs (§A.43 item 4);
       - never deletes a run or a run's logs. Log deletion is listed under the no-deletion commitment
         (c.6726548830 item 1) for this round.

       Any dispatch or re-run it makes is a run like any other, so the enumeration and the order rule cover it,
       whoever initiated it;
     - the deployment-review comment uses the frozen form `ARP-3-QC22 <stage> <full commit id>`.
   - **Unverified host behaviour (named; r10 N2):**
     - whether `can_admins_bypass: false` stops an administrator's bypass in the interface;
     - how long a pending review waits before it expires (an expiry is a host VOID);
     - whether a re-run of a gated job would ask for approval again. The design does not rely on it, because job B's
       `if:` skips it on attempt `≥ 2`;
     - whether `updated_at` moves on every rule or policy edit (GT-6b);
     - whether the session's proxy refuses `POST …/pending_deployments` and Environment writes (only relevant to
       E-ID (ii); GT-7).
2b. **Owner decisions on the gate's reader, identity and binding** (neutral; record id: PENDING). Each is fixed before
   `F`, and its verification is a gate test.
   - **E-READ: who reads the Environment's settings, and through what channel (r11 B1).** This session's proxy
     refuses `GET environments/…` (r11 H17). The options are:
     - **(a) A CI step.**
       - Job A gains step A11, **"ARP-3-QC22 Environment read"**:
         `python3 -I -S -B <record dir>/controls.py env-read > "$RUNNER_TEMP/arp3-qc22/env.json"`, with
         `GH_TOKEN: ${{ github.token }}` in the step's `env:` and `if: ${{ hashFiles('verification/receipts/ARP-3-QC22.json') == '' }}`.
       - Its `env.json` is uploaded as the artifact `arp3-qc22-env` (R14-N3), with `retention-days: 90`.
       - Job A gains `permissions:` with `actions: read`, `deployments: read` and `contents: read`. Whether these
         scopes let the job's token read the Environments API is **unverified**; GT-6 tests it.
       - **Its exit (§A.44; R13-B2, B5).** `env-read` prints the reduced read, which the step redirects into
         `env.json`, and exits 0 iff the read has every frozen field and, when the tree carries
         `evidence/env-pin.json` (at S1 and `E`), equals it; 3 otherwise. On the design, confirmation and gate-test
         trees, which carry no pin, it records only.
       - The reader is the host's job token. Each stage's read is A11's conclusion in that stage's dispatch run,
         taken inside the decisive run itself (control N). The pin is taken as precondition 2a states.
       - W pins A11, its `if:` and the permission block.
     - **(b) The owner.**
       - Before the S1 dispatch, before the `E` dispatch, and before `verdict`, the owner runs the frozen read
         command, reduces it to the frozen fields, and posts the canonical JSON and its sha256 as a comment on the
         round PR.
       - `controls.py` reads the comment through the issue-comments API (readable here; template
         `issues/comments/{DEC}`, the comment id an argument; R13-B4) and quotes it with author and time. Each post
         precedes the check that reads it: the S1 post `check --stage S1`, the `E` post `check --stage E`, the third
         `verdict` (control N; R13-B5).
       - It is structured, but its integrity rests on the owner, and under E-ID (i)–(iii) the host cannot tell the
         poster from the session (H22; R14-N1).
     - **(c) The owner permits the session's proxy to `GET` the two paths.** The change is outside the repository,
       and recorded with author and time. `controls.py` then reads directly, as the templates of control B allow.
   - **E-ID: the reviewer identity (r11 B2).** The session acts as `amaybaum`. The options are:
     - **(i) A reviewer the session does not hold.** The required reviewer is a second owner-controlled account, added
       as a collaborator, whose credential the session does not hold. It is set with `prevent_self_review: true`.
       - **No team option.** A team is not available: the repository is user-owned, and teams exist only in
         organizations (r12 H24).
       - **Account terms.** Whether a second personal account is consistent with GitHub's account terms is
         **unverified**, and it is the owner's to check (r12 N5).
       - **Effect.** The host refuses an approval made with the session's credential.
       - **What stays possible (r12 N6).** The session's administrator credential can still edit the Environment,
         which remains procedural; control N detects such an edit if it persists (`updated_at`). The session can
         still dispatch with inputs, through either channel, but under (i) such a dispatch only waits for a review.
       - **Cost.** A second identity, and a re-read of the Environment.
       - **Who dispatches (R13-N23).** Every decisive and gate-test dispatch is made by an identity other than the
         reviewer, because `prevent_self_review: true` refuses the reviewer's approval of a run the reviewer
         dispatched.
     - **(ii) A proxy rule.** A rule on the session's proxy refuses `POST …/pending_deployments`, the review
       endpoint, and Environment writes for the session's credential.
       - **Effect, if it holds.** It covers both approval and edits by the session.
       - **Unverified.** GT-7 tests only its review half, by an authorized attempt to **reject** a pending gate-test
         deployment. Even if the rule is absent, that attempt is harmless, because B4 is unreachable with the
         all-zero input. Its Environment-write half stays untested.
       - **Its reach.** It applies to the agent proxy only, not to the MCP connector (precondition 2a), whose current
         schema has no review or Environment method.
     - **(iii) Accept the procedural limit.** The reviewer is `amaybaum` with `prevent_self_review: false`, and the
       limit is stated as a residual.
     - **(iv) Change the session's identity, not the reviewer's (r12 N5).** The session acts through a credential
       other than `amaybaum`'s, for example a GitHub App or a machine-account token. The reviewer stays `amaybaum`,
       with `prevent_self_review: true`.
       - **Effect.** The same as (i): the host refuses an approval made with the session's credential.
       - **Edits.** Environment edits by the session depend on the permissions granted to its identity. Without
         administration permission, it cannot make them.
       - **Cost.** A new identity for the session, with its permissions to be set and recorded, and a re-read of the
         Environment.
       - **Who dispatches (R13-N23).** As under (i): no decisive or gate-test run is dispatched by `amaybaum`, the
         reviewer, so the owner does not dispatch them himself.
   - **The identity E-ID adds (R14-Rb3).** Under (i), the second account's login, frozen into the Environment's
     reviewer (2a), B3b's `user.login` condition and the approval entries' `review`. Under (iv), the session's
     identity and its permissions, recorded so that the record shows which identity dispatches and whether it can
     edit the Environment. No condition reads it: under (iv), B3b and the approval entries' `review` use `amaybaum`,
     authorship requires `amaybaum`, and `prevent_self_review` enforces the dispatcher rule on the host (R14a-N8).
     Under (ii) and (iii), none. Recorded with E-ID: PENDING.
   - **E-BIND: the in-job approval check B3b (r11 N4).** The choice is to adopt it or not.
     - **Adopted.** The commit binding becomes preventive.
     - **Not adopted.** A mis-approved commit is detected afterwards and VOID.
     - **Cost.** Job B gets a token permission, whose sufficiency is unverified until GT-2 and GT-2b.
3. **Gate.** The disposition of the preparation-side guard (`ACCESS.md` F-2) is recorded (PENDING). The round applies
   both sides either way.
4. **Independent review** of this file at its candidate revision, and of `ACCESS.md`, including any R-S narrowing (its
   scope, SF-3n and controls). It must be an independent ACCEPT with no open blocking finding (c.6726548830, item 5),
   recorded on the round PR.
   - c.6726548830 says "independent ACCEPT of r10".
   - r10 has been superseded, so this file reads that as an ACCEPT of the candidate revision presented for `F`.
     That reading is the coordinating session's interpretation (r11 N7), and the owner can correct it.
   - The owner's confirmation or correction of this reading (R14-Rb3): PENDING.
5. **No `PENDING` field** remains (control P).
6. **Design run, self-tests and budget.**
   - **The design run.** A disposable branch carries the predicted S1 tree. Its `pull_request` run uses fixture mode
     through job B's condition and A3's literal, and is green, with job B `skipped`. The Environment's deployment list is unchanged across
     it (no deployment created by a skipped job). `design-run.json` records every job and step conclusion, each step's
     `started_at` and `completed_at` from the jobs API, and the artifacts' `digest`s as provenance (schema
     `arp3-qc22-run`; R13-B2, N13). Its pull request's base is a branch held at `D` (R13-N9). Its sha256 is pinned
     here: PENDING.
   - **The self-tests**, including every mutation above, pass.
   - **No F1.** F1 under `G_SM` has not been built.
   - **Stress figures.** Step 5 of the design run produces `stress.json`, retrieved by the executor as the file
     inside that run's `arp3-qc22-stress` archive; its pin is bound by A7 at 6′ (R13-B2; R14-N3). Every
     kept stress fixture must be certificate-verified. Its sha256 is pinned here: PENDING.
   - **Budgets.** `P_max`, `B_max` and `W_max` are set by the mechanical freeze rule (*Method*, step 6) and entered
     here: PENDING.
   - **The timeout test** (*Method*, step 6) passes. If it fails with R-S kept, item 2's R-S decision is taken first.
     If it fails without R-S, no `F` is requested.
     - **Its inputs are computed, not hand-filled (re-review r6 N2).** `check --freeze` recomputes them from the pinned
       `design-run.json` and `stress.json`:
       - `t_5` is step 5's `completed_at − started_at`, in whole seconds;
       - `t_810` is the same quantity summed over A8 and A9. B6's term is 0 (r11 N6): B6 compares canonical JSON
         only, and in the design run job B is `skipped`, which lists no steps (r11 H21), so B6 has no step record;
       - `W_fix` and `W_stress` are read from `stress.json`;
       - `σ` is computed exactly.
     - **The recorded values must match.** The values below are recorded for reading, and `check --freeze` fails if
       any differs from its recomputation:
       - the design run's run id: PENDING;
       - the step ids of A5, A8 and A9: PENDING (B6: none, by the above);
       - `t_5` and the exact `σ`: PENDING;
       - `W_fix` and `W_stress`: PENDING;
       - `t_810`: PENDING.
     - **Edge cases (frozen).** If `t_5 = 0` (a step under one second), `t_5 := 1` is used, an upper bound on the true
       duration. If `W_stress + W_fix = 0`, σ is undefined and the test **fails**, and no `F` is requested until the
       stress step is revised and reviewed.
   - **A frozen fixture the design run cannot decide (R14a-Rc1).** The design run uses no budget, so a fixture
     undecided within the job timeout is an A3 timeout, which the no-unapproved-F1 rule makes a violation. Its run
     time is therefore established locally first: the executor precondition *No push without a local fixture run*
     (*Runs, evidence, approvals*) applies to the design branch, so such a fixture is found before the design run.
     - A fixture found undecided there, or a design run whose A3 exits 3 with complete fixture-mode output, leads
       to the fixture set being revised before `F` and reviewed under item 4.
     - A design-run A3 that times out, crashes or is cancelled despite the local run is a violation (the rule's
       stated residual). It is known before `F` from the design run's record, and `F` is then not requested, since
       `check --stage S1`'s capture would halt the round VOID.
     - No fixture is dropped after `F`.
6′. **Confirmation run (re-review r4 B2(c)).** A second disposable-branch run of the exact predicted S1 tree.
   - **No substitution is needed.** It is a `pull_request` run, so job B is `skipped` and job A runs fixture mode by
     A3's literal. F1 stays unbuilt (re-review r6 B1).
   - **In force:** the final `P_max`, `B_max`, `W_max`, the final `stress.json` pin and `timeout-minutes: 60`.
   - **It must be green on every step.** Step 3 green means every frozen expectation was reproduced by the writer's
     own solver and verifier within the final budgets. Step 7 green means the stress output matches its pin.
   - **Its record.** `derive-run` turns it into `confirmation-run.json`: the run id, `head_sha`, every job and step
     conclusion, and the `digest`s of its `arp3-qc22-fixtures` and `arp3-qc22-stress` artifacts as provenance (schema
     `arp3-qc22-run`; R13-B2, N13). Its run id is pinned here:
     PENDING. Its sha256 is pinned here: PENDING.
   - **Mechanical verification (re-review r5 N1(a)).** `check --freeze` verifies:
     - the sha256 of `confirmation-run.json` (committed at S1; supplied to `check --freeze` before `F`) equals the
       pin;
     - every job and step conclusion in it is `success`, A3, A3b, A7 and A10 included, except job B, which is
       `skipped`;
     - its `head_sha` exists in the repository, and its tree carries `qc22_check.py` and `controls.py` at the
       pinned blobs;
     - its `verify.yml` is byte-equal to `D`'s with the frozen splice;
     - A3b is `success`, so A3's output had `mode: "fixture"`, and its artifact list has no
       `arp3-qc22-measurements` artifact (job B `skipped`; R14-N3);
     - A7 is `success`, so 6′'s own `stress.json` has the pinned sha256 (R13-B2);
     - its pull request's base `sha` is `D` and its head `sha` is the run's `head_sha` (R13-N9);
     - **re-derived from the host (R14-N4).** `derive-run` on the pinned run id gives the same job and step
       conclusions, `head_sha` and `pull_requests` entries as `confirmation-run.json`. The design run is re-derived
       the same way against `design-run.json`, so neither record rests on the supplied copy alone.
   - **`confirmation-measurements.json`** is an executor copy that no condition binds to 6′'s archive. C-STATELESS
     compares it with S1's committed `fixtures` section, and any fixture-mode output of the S1 tree yields that same
     section, so a wrong copy can make C-STATELESS fail but cannot make a perturbed decision pass unseen (R14-N4).
   - **The tree differences between 6′ and S1 (N1(b)).**
     - `verify.yml`: none.
     - Record files: `evidence/f-run/results.json`, `evidence/confirmation-run.json`,
       `evidence/confirmation-measurements.json`, `evidence/gate-tests.json` and `evidence/env-pin.json` are absent
       from 6′'s tree, because they come into existence after 6′. `evidence/design-run.json` is present, as at S1,
       because the design run precedes 6′ (R13-N25). The preregistration in 6′'s tree carries unfilled the fields
       filled after 6′: 6′'s own, `env-pin.json`'s and `gate-tests.json`'s pins, and anything recorded from the `F`
       dispatch (R14-N11).
     - No workflow step reads any of these.
   - **Retention.** The design and confirmation branches are not deleted before `E`'s receipt is captured, so their
     `head_sha` trees stay checkable.
   - **Statelessness (N1(d)).** Each fragment decision builds its own tableau and carries no solver state across
     fragments. The order in which fragments are decided cannot change any fixture's verdict, step or counters. This
     is measured by **C-STATELESS** (*The controls*). `controls.py check --stage E` evaluates it, and a mismatch is a
     failed check at `E`: the round halts with VOID (re-review r6 N1).
6″. **Gate tests (c.6726548830, item 5: "verification of the complete gate").**
   - **The branch.** The gate-test branch carries the confirmation tree, 6′'s exact tree. It is admitted by the
     Environment's policy and is otherwise never dispatched.
   - **Authorization.** Each gate-test dispatch and re-run is a launch, with its own recorded owner authorization
     (§A.43 item 4).
   - **No gate test can compute F1.** Every gate-test dispatch that sets `arp3qc22_decisive` true sets
     `arp3qc22_sha` to forty zeros, which names no commit, so B3 fails before B4 whatever the review and whatever
     B3b does.
   - **The tests** (frozen expectations):
     - **GT-1 (rejection).** A dispatch on the gate-test branch with the input true. The owner rejects the review.
       Expected: job B is not `success` and has no B3 or B4; the approvals API shows `state: "rejected"`; job A is
       `success`.
     - **GT-2 (approval, wrong commit).** As GT-1, but the owner approves, with comment
       `ARP-3-QC22 GT-2 <gate-test commit>`. Expected: B1 and B2 are `success`, B3 is `failure` and B4 is `skipped`.
       This test records:
       - the approvals API's fields, its time if any, and the reviewer;
       - the deployment and its statuses;
       - the field that names the run id, which fixes the mapping rule.
     - **GT-2b (only if E-BIND is adopted).** As GT-2, but the approval comment names a commit other than the run's.
       Expected: B3b is `failure`, and B3 and B4 are `skipped`. In GT-2 itself B3b must be `success`.
     - **GT-3 (branch policy).** A dispatch with the input true on a branch outside the policy, at the gate-test
       commit. Expected: job B is refused with no review requested, and has no B4.
     - **GT-4 (re-run).** The owner re-runs GT-2's run. Expected: in attempt 2, job B is `skipped` and no review is
       requested.
     - **GT-5 (ordinary dispatch).** A dispatch on the gate-test branch without inputs. Expected: job B is `skipped`,
       job A and the aggregate are `success`, and no deployment is created.
     - **GT-6 (the E-READ channel; r11 B1).** The chosen channel yields the canonical JSON of every frozen field.
       - Under (a): A11 is `success` in GT-5's run under the frozen permissions. The `env.json` file inside its
         `arp3-qc22-env` archive (R14-N3), copied by the executor, is compared with one owner-posted read of the same
         fields, made at the same time: `check --freeze` reads the comment, whose id `gate-tests.json`'s GT-6 entry
         records (R14-N5), through `issues/comments/{DEC}` and requires the posted sha256 to equal the copy's (a
         one-time cross-check of the channel; the archive's `digest` is provenance; R13-B2).
       - Under (b): the owner's comment has the frozen form, and its sha256 matches its JSON.
       - Under (c): both `GET`s return 200 to the session.
     - **GT-6b (optional; host behaviour).** The owner makes one recorded settings edit and reverts it, for example
       adding a wait timer and removing it. Read before and after. If `updated_at` moves, the residual on reverted
       edits is narrowed. Otherwise it stays as stated. The pin is taken after GT-6b.
     - **GT-7 (only if E-ID (ii) is adopted; r12 N4).** It is the single owner-authorized exception to precondition
       2a's commitment that the session never calls the review endpoint.
       - **The request.** On a pending GT-1-style deployment, whose input is all zeros, the session sends exactly
         `gh api --method POST repos/amaybaum/incompleteness/actions/runs/<run_id>/pending_deployments --input <file>`,
         where `<file>` holds exactly the frozen body
         `{"environment_ids": [<pinned id>], "state": "rejected", "comment": "ARP-3-QC22 GT-7"}` (R13-N16), through
         the agent proxy. It is run by hand under the authorization, never by `controls.py`.
       - **Expected:** the proxy refuses it, the deployment stays pending, and the owner then rejects it.
       - **If the rule is absent,** the request is a host write: it records a rejection review by `amaybaum`, and
         job B in that gate-test run fails. That is harmless, because B4 is unreachable with the all-zero input. It is
         recorded as a GT-7 entry, and (ii) counts as not verified.
       - **What GT-7 does not test.** It tests no Environment write. So (ii)'s Environment-write half stays
         unverified.
       - **What a proxy rule does not cover.** A rule on the agent proxy does not reach the MCP connector (precondition
         2a). That connector has no review or Environment method today, so (ii)'s effect holds for its current tool
         surface only.
       - **Before GT-7,** this session makes no such attempt.
     - **GT-8 (read-only; run numbers; R13-N18).** For each workflow, the `run_number`s of the runs created in
       `[T0, the test]` are listed with set (2)'s queries and set (1)'s dispatches. Expected: each forms one contiguous
       range. If one does not, the gap is reported to the owner and recorded, and the run-number check of *Runs,
       evidence, approvals* is not applied; the deletion residual then stands as stated. GT-8 is not a gate failure.
   - **The record.** `derive-run` turns each run into a gate-test entry. Together they make `evidence/gate-tests.json`,
     committed at S1. Its sha256 is pinned here: PENDING, and `check --freeze` re-reads every run against it.
   - **Failure.** Any expectation not met means no `F` is requested. The design and this file are revised and
     reviewed again (item 4).
   - **Retention.** The gate-test branch and the GT-3 branch are kept until `E`'s receipt is captured.
7. **Chain and blocks.** From the repository root, this command exits 0:

   ```sh
   python3 -I -S -c "import sys; sys.path.insert(0, 'tools'); import v3_verifier as v; r = v.Repo('.'); d, f = sys.argv[1], sys.argv[2]; rd, rid, kind, ent, cp, codes = v.control_plane(r, d, f); t1 = v.check_t1(r, d, f, cp); dig = v.governed_digest(ent) if ent else None; print(rid, kind, rd, dig, codes + t1); sys.exit(0 if not (codes or t1) and (rid, kind, rd) == ('ARP-3-QC22', 'non-sealing', b'verification/programmes/oi-qm/reconstruction/round-arp3-qc22-20261108/') and dig == '9f3808ac33d65a27dc363a88a0d0e7df16c77fa33f49d2c0f22b0df279b049b6' else 1)" <D> <candidate F>
   ```

8. **`F` dispatch.** With its §A.43 launch authorization, a recorded owner comment (R13-N22), the run at candidate
   `F` is green on every job. `F`'s `verify.yml` is `D`'s, so it is dispatched without inputs, and it has no
   Environment or deployment review. `derive-run` records it as `evidence/f-run/results.json`, committed at S1
   (R13-N13).
9. **Designation request.** The owner receives the candidate `F`, the commit, the review verdict, the controls, the
   resource evidence (`stress.json`, the timeout test and the confirmation run), the gate evidence (`env-pin.json`
   and `gate-tests.json`) and the blockers, and designates `F`.

**If any precondition cannot be met, no `F` is requested**, preparation stops, and the finding is reported on the
round PR.
